import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_47 = relay.var("var_47", dtype = "int64", shape = (9, 7, 9))#candidate|47|(9, 7, 9)|var|int64
var_48 = relay.var("var_48", dtype = "int64", shape = (9, 7, 9))#candidate|48|(9, 7, 9)|var|int64
bop_49 = relay.equal(var_47.astype('bool'), relay.reshape(var_48.astype('bool'), relay.shape_of(var_47))) # shape=(9, 7, 9)
output = bop_49
output2 = bop_49
func_52 = relay.Function([var_47,var_48,], output)
mod['func_52'] = func_52
mod = relay.transform.InferType()(mod)
mutated_mod['func_52'] = func_52
mutated_mod = relay.transform.InferType()(mutated_mod)
func_52_call = mutated_mod.get_global_var('func_52')
var_54 = relay.var("var_54", dtype = "int64", shape = (9, 7, 9))#candidate|54|(9, 7, 9)|var|int64
var_55 = relay.var("var_55", dtype = "int64", shape = (9, 7, 9))#candidate|55|(9, 7, 9)|var|int64
call_53 = func_52_call(var_54,var_55,)
output = call_53
func_56 = relay.Function([var_54,var_55,], output)
mutated_mod['func_56'] = func_56
mutated_mod = relay.transform.InferType()(mutated_mod)
var_132 = relay.var("var_132", dtype = "float32", shape = (10, 9, 14))#candidate|132|(10, 9, 14)|var|float32
var_133 = relay.var("var_133", dtype = "float32", shape = (10, 9, 14))#candidate|133|(10, 9, 14)|var|float32
bop_134 = relay.less_equal(var_132.astype('bool'), relay.reshape(var_133.astype('bool'), relay.shape_of(var_132))) # shape=(10, 9, 14)
bop_144 = relay.logical_and(bop_134.astype('bool'), relay.reshape(var_133.astype('bool'), relay.shape_of(bop_134))) # shape=(10, 9, 14)
var_150 = relay.var("var_150", dtype = "bool", shape = (10, 9, 14))#candidate|150|(10, 9, 14)|var|bool
bop_151 = relay.mod(bop_144.astype('float64'), relay.reshape(var_150.astype('float64'), relay.shape_of(bop_144))) # shape=(10, 9, 14)
bop_160 = relay.bitwise_xor(var_133.astype('uint32'), relay.reshape(var_132.astype('uint32'), relay.shape_of(var_133))) # shape=(10, 9, 14)
output = relay.Tuple([bop_151,bop_160,])
output2 = relay.Tuple([bop_151,bop_160,])
func_169 = relay.Function([var_132,var_133,var_150,], output)
mod['func_169'] = func_169
mod = relay.transform.InferType()(mod)
mutated_mod['func_169'] = func_169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_169_call = mutated_mod.get_global_var('func_169')
var_171 = relay.var("var_171", dtype = "float32", shape = (10, 9, 14))#candidate|171|(10, 9, 14)|var|float32
var_172 = relay.var("var_172", dtype = "float32", shape = (10, 9, 14))#candidate|172|(10, 9, 14)|var|float32
var_173 = relay.var("var_173", dtype = "bool", shape = (10, 9, 14))#candidate|173|(10, 9, 14)|var|bool
call_170 = func_169_call(var_171,var_172,var_173,)
output = call_170
func_174 = relay.Function([var_171,var_172,var_173,], output)
mutated_mod['func_174'] = func_174
mutated_mod = relay.transform.InferType()(mutated_mod)
const_181 = relay.const([[[9,-8,-7,-1,-5,-3,-2,9,7,-1],[-9,-2,6,7,-8,-4,8,-6,-4,3],[-7,-2,-9,-5,2,-3,-4,10,-6,2],[8,1,-1,-3,3,6,-4,9,9,2],[-1,-4,10,6,1,-2,-5,6,-9,1],[-7,-3,5,-2,7,10,9,-4,-8,-4],[8,9,-10,-9,6,-2,9,3,7,-2],[9,4,-6,6,-1,-2,-8,-2,9,-9],[3,7,-7,6,6,-10,-10,5,-5,9],[-3,4,-3,2,-10,-9,2,-5,-6,1],[-8,1,7,3,8,5,2,-5,-6,9],[7,8,-3,6,-3,3,10,-9,-9,9],[4,-9,3,-1,8,-6,-5,-4,-7,-8],[-1,-4,-5,10,-7,3,2,8,-5,-6]],[[-9,10,9,2,6,8,3,10,7,5],[-8,-5,-10,8,4,-10,8,-6,-6,1],[-10,-1,1,2,3,1,-6,4,1,-1],[5,5,1,-10,-2,1,2,-7,-5,-10],[-8,10,7,-10,-5,1,-4,3,10,4],[-4,7,7,8,5,-10,9,5,-1,4],[7,6,-4,7,-2,-7,6,-4,-8,-4],[-8,-5,4,3,-6,1,-2,3,8,1],[10,8,-4,8,-5,-6,-9,-10,-3,-8],[1,10,-8,1,-4,-8,4,10,-10,-3],[-3,8,2,-2,-2,-3,10,8,8,-6],[6,7,-1,10,-7,4,4,1,9,-10],[-6,6,8,-5,-7,-9,6,3,-2,7],[-7,-9,-3,6,6,5,-1,-9,8,5]],[[7,-6,-1,10,-3,-3,6,-9,4,2],[-1,3,9,1,8,-1,-2,-7,6,-8],[-4,9,-3,-10,-4,-9,9,-9,4,4],[-9,-6,-3,-6,2,-8,-3,6,-5,-4],[-9,8,-5,-6,8,-10,6,8,2,-10],[5,1,-5,7,3,1,-4,-2,5,-9],[-10,9,-8,-7,10,5,5,7,-2,2],[-6,9,-1,1,1,-10,-3,-8,8,1],[5,5,-9,2,5,-9,8,-10,-1,6],[5,4,4,8,9,10,-5,-6,7,8],[-1,-4,-6,-7,-7,8,6,9,6,-2],[7,1,-6,6,4,-7,2,-3,6,-5],[10,7,7,-5,-5,10,-8,-4,7,-8],[-6,5,6,6,5,-7,5,2,-1,-5]],[[-6,8,5,8,4,2,-1,-9,4,-1],[7,7,-3,5,7,-2,-6,-7,-2,2],[1,5,-2,10,-2,-8,-6,-2,-3,-5],[-7,-3,7,4,7,7,-10,9,-9,-10],[10,9,-3,7,5,6,8,5,-9,7],[4,3,8,-10,3,-7,7,8,-4,6],[8,-3,1,-4,-6,-8,6,-6,5,1],[-5,-10,-4,-4,5,10,-4,-2,1,-5],[10,1,7,10,3,-10,2,5,-10,6],[1,-3,-9,7,-2,8,8,-7,7,6],[1,-2,-8,10,-6,-5,2,-1,2,2],[-2,5,-10,-6,-2,-8,-10,7,-5,-6],[-3,9,9,-8,-6,7,1,-2,4,9],[-10,-10,-7,-8,4,-5,-5,4,-2,6]]], dtype = "uint32")#candidate|181|(4, 14, 10)|const|uint32
const_182 = relay.const([[[-2,3,-1,10,2,9,-6,-6,7,-5],[-5,-6,-8,2,-7,1,1,5,-8,10],[-2,-9,-9,1,4,8,8,6,6,5],[1,3,3,-2,2,-2,10,-1,6,-6],[-9,-8,10,-5,4,-8,-10,-4,8,4],[7,-4,-7,7,8,-2,8,4,-5,-4],[10,1,4,3,-3,-4,4,9,-3,-5],[-2,10,8,-7,4,2,-5,4,-10,1],[-3,-4,-1,8,-3,-8,1,-4,1,-2],[7,9,-6,-9,-1,10,3,10,-8,1],[3,-6,-7,-5,-6,-5,10,-2,8,-3],[-2,-2,-4,1,3,5,1,-2,4,7],[2,-2,6,9,5,-3,-2,2,-9,1],[-4,10,8,4,-9,1,-2,6,-8,2]],[[-6,2,1,-7,6,-2,4,6,6,-3],[10,6,8,-10,4,10,8,-9,6,9],[4,2,5,-10,-9,-6,9,-1,-2,1],[-4,8,-3,-8,5,-10,-1,8,4,9],[-1,2,-4,6,5,-4,10,-8,-10,-3],[8,-5,8,6,-1,5,1,1,4,3],[-7,-8,-8,-10,-7,-5,-8,3,-4,-8],[-8,-7,4,-4,7,8,6,-1,-2,-5],[5,3,10,7,-7,-7,2,3,3,-4],[9,-6,-8,7,7,-9,2,4,-10,-6],[-10,3,8,-7,7,3,5,-9,4,5],[10,4,7,-3,-10,3,1,-1,-4,-10],[-2,-5,10,-2,-1,-6,10,-2,7,-2],[-6,7,5,-6,6,9,9,-5,-1,-5]],[[-1,-3,2,-7,-5,-8,-8,-8,-10,-1],[2,-4,-6,-2,-5,9,-10,8,10,-5],[-4,5,5,-4,-10,1,5,-3,-4,9],[-3,-7,3,-9,9,-9,4,-7,-7,-5],[-4,-9,2,3,10,-5,-2,-8,-8,-9],[10,1,10,-2,-9,-6,-3,-3,8,3],[9,2,10,6,6,6,3,-9,-5,2],[10,-8,-2,10,-8,9,-10,-9,-1,-10],[-2,5,4,-10,5,-5,-9,-7,-4,2],[-9,1,4,-4,7,-3,10,6,-10,-3],[6,9,10,6,-5,8,-3,-5,-9,1],[-3,-6,-2,7,9,-8,-7,-2,-3,3],[-9,1,-9,9,7,5,6,-1,6,-2],[-9,1,9,2,-2,-1,-5,-4,-1,2]],[[3,-8,-9,-9,8,-9,6,-2,1,-9],[9,5,2,-8,-2,-1,-6,-6,-9,-1],[8,1,-9,-9,6,-7,-5,1,-2,2],[-9,-1,-3,1,5,8,-1,-7,3,5],[3,-6,-2,10,6,-10,-7,10,-1,4],[3,9,-1,8,-4,5,3,-10,8,3],[-1,1,-5,8,1,1,-3,2,9,-10],[-3,4,6,-2,-1,-2,-7,10,1,-9],[-9,-10,3,8,2,-6,-3,-10,4,7],[5,8,10,4,-8,-6,5,9,8,9],[5,4,8,9,5,7,-3,2,5,-7],[-10,9,-8,3,-8,-5,-2,1,2,1],[-5,-7,-7,4,-6,-4,3,-4,-4,9],[1,-2,-3,-4,4,2,8,-10,8,-5]]], dtype = "uint32")#candidate|182|(4, 14, 10)|const|uint32
bop_183 = relay.logical_xor(const_181.astype('uint32'), relay.reshape(const_182.astype('uint32'), relay.shape_of(const_181))) # shape=(4, 14, 10)
func_169_call = mod.get_global_var('func_169')
func_174_call = mutated_mod.get_global_var('func_174')
const_195 = relay.const([-4.758678,0.344653,-2.284544,-7.344058,-5.326458,-6.145107,-1.446013,9.733218,8.200542,-4.882005,5.624234,-9.512883,-1.991831,3.849109,-8.594297,-3.234610,-0.597975,-4.442608,8.599352,-1.577003,-2.248420,-5.408209,-4.539614,-2.352675,-9.893704,8.234549,-5.140182,1.909304,5.324484,8.914905,5.405453,-1.534167,6.056436,-2.925279,-2.788348,-8.918080,-4.851447,8.031915,-0.462118,-8.594345,9.259901,-5.783874,9.665294,-0.798614,-9.274886,4.324596,4.885963,2.342638,-5.665844,3.195556,-3.771262,5.451765,7.372657,7.050542,-2.495781,-3.555958,-4.114198,-0.267558,7.563173,-0.199750,-8.231271,5.428587,-4.569527,-4.018673,-7.273753,1.700391,8.702942,6.661345,0.164104,-1.996639,6.490132,4.150409,2.720481,7.568703,-1.190806,-5.850470,4.307077,6.347630,-1.509205,3.403021,7.440211,3.039496,9.356514,8.857556,6.071840,9.381607,6.721168,-4.702317,-9.299027,9.274846,-3.581779,6.419023,7.640697,1.179791,-1.946796,-4.215167,3.155738,-6.028312,4.981794,8.955543,7.545212,8.767260,-2.809164,3.624697,3.008868,0.159327,-0.534016,-2.587775,6.566362,7.975825,-8.976928,-3.588741,3.892118,-2.844423,-8.001813,7.532623,-6.493982,-7.849875,0.111160,6.049788,-3.955853,-8.510707,3.219002,-8.226037,-9.723972,-2.284176,-6.546698,-6.375912,8.833982,-3.835403,-4.573897,8.861438,-7.609216,1.148263,2.524008,-8.931412,-9.222559,-4.682011,5.097835,-1.086189,-4.345018,-7.499996,0.232998,-3.808343,-6.467090,6.370925,8.896964,9.043839,-5.368276,3.606473,-7.631113,-0.442642,-3.866752,-0.920180,0.659014,8.254358,-0.829324,-5.900808,-5.130223,-6.237549,2.141592,1.252025,8.233450,-0.291028,-6.662617,4.937460,-1.080448,7.163815,8.165015,-4.078250,-1.094311,-6.979982,-4.712785,1.695186,-2.935004,0.794061,0.322639,-5.544349,3.680031,-7.125469,-4.919303,-3.050625,3.504336,9.449956,-4.492861,-2.739966,9.122972,7.400951,3.431205,-2.690375,-3.194656,-7.535315,-3.673787,-2.137095,8.052777,8.753549,4.486073,-8.499637,9.188723,9.497672,-0.066848,4.759399,-0.704008,1.060436,1.833412,4.278100,0.671464,9.525876,-4.479281,7.873395,-1.438847,0.329232,8.873359,4.036875,6.081519,-9.732977,-3.468317,1.699751,-4.318822,-8.375849,-5.777493,3.825312,4.918246,-3.157759,2.619094,-2.254915,-8.421510,8.600664,9.066452,1.242952,1.693442,-0.869046,4.353708,-3.756291,-8.845614,7.308448,3.194118,-2.476207,3.445069,-5.088246,8.812911,-4.669221,3.759194,4.130040,-7.874981,5.370305,-3.863750,5.841207,-7.548760,7.157164,9.509438,3.913881,3.144468,8.334122,-1.427692,3.221238,-3.710938,-1.203294,8.234202,3.192968,-4.668393,1.724764,-7.544510,-1.103739,0.999699,-3.481106,-8.280935,7.122365,0.662821,-8.658561,-8.920344,7.120622,3.818673,-5.983264,6.413210,7.753963,0.659772,-8.802806,7.907949,-2.559569,-2.243599,7.514412,-0.007909,0.751722,-5.518326,-7.162008,0.969110,6.430524,7.073929,-7.115494,6.499897,-5.768237,-1.569162,7.809932,0.528800,-2.441889,-3.765340,-7.213529,-7.996155,-5.623948,7.119750,-2.574397,1.557844,1.015671,5.734902,9.486072,8.724531,5.137787,7.901538,-2.317577,-3.192905,-8.774555,-5.916990,-6.571364,-0.281975,3.559255,3.422271,5.662719,-3.566036,3.633200,-8.607908,-7.731994,-2.761738,1.772975,-8.636117,-9.405632,4.545155,3.256463,7.957533,-3.181039,7.542977,3.826318,5.293633,8.804688,4.099295,-7.923962,8.750510,-6.751085,-5.628714,9.017205,5.781288,-4.106140,9.036282,-4.674526,2.882507,-8.966523,4.500371,0.506309,-3.549467,-2.144600,2.818763,3.087749,8.145547,-6.190300,-8.012097,0.604528,5.971293,-7.849356,3.810460,8.314220,9.533694,5.565561,0.022678,-9.444222,9.158001,7.941370,2.857254,-7.015034,-1.051163,-5.791271,-8.081450,-4.409497,3.830370,-2.008336,-1.502245,8.440623,-2.227849,-5.723259,3.941246,6.858626,2.753125,9.647827,-9.366150,2.986115,-5.401319,0.600926,7.770139,-2.943223,-3.011633,-1.796276,-6.387500,-4.803319,-5.085538,-2.746603,0.706000,1.521619,0.286866,3.270060,-8.902468,-6.592438,3.224863,4.589938,-4.471628,7.491631,8.352081,4.791914,-8.157348,-3.852203,-7.304260,-9.650812,-6.594330,-3.915818,6.847937,5.268768,-5.820132,-4.752984,0.620250,1.940299,-6.930623,-8.101636,-8.375279,8.419786,-0.242973,3.442343,6.658522,-0.210828,4.829787,6.085682,0.457983,-2.193243,-1.410080,8.767544,1.288933,4.176459,7.237888,9.334808,9.960166,-2.616423,-1.605597,-1.720316,-6.778990,4.234690,1.715336,-3.686598,-1.946778,3.697903,5.349955,-5.272315,1.457739,-0.537674,-2.669101,-2.220656,2.372887,0.718819,-3.149936,7.822881,-7.319602,3.131566,5.577628,-1.787177,-8.838744,-4.537162,-9.200174,-1.584621,5.103100,4.707298,-8.508507,9.360943,-9.676082,4.055794,4.396764,0.874626,-6.364552,0.114750,-3.403799,0.620271,6.905182,5.139405,-9.473828,5.177401,-9.934107,4.666091,-1.863326,-9.906104,7.357735,-2.129985,-1.911054,5.746604,-3.660853,-8.383554,-7.443120,1.803759,-5.377260,-9.530908,1.516722,-9.122042,-9.160916,-0.745346,-8.965565,2.147444,3.808609,-4.578766,-0.686423,-4.044608,0.506574,1.726972,-0.127697,2.298123,0.996988,8.530667,-7.191855,2.090179,-6.198992,3.636189,-5.469061,-1.612710,-5.912181,-9.296458,-5.252740,7.629757,3.100962,-8.141136,-5.326931,-1.008378,8.889703,-2.003144,4.259555,-7.074646,5.568579,8.594019,-5.663888,5.960742,-9.351376,8.252748,-9.721134,-4.003461,-4.758224,7.683005,2.289595,-7.571336,-4.670298,-2.075515,-4.163208,9.086806,-7.732910,-8.250542,-0.106447,-8.978883,3.465409,-5.824382,-3.496584,9.118579,6.882071,3.588859,8.424902,4.342500,-0.058355,9.677619,-2.573736,4.193464,3.839882,3.832439,4.269078,3.292043,-5.403500,9.216582,-0.673690,2.750066,6.883068,-3.282368,-6.485731,-8.001754,1.356484,-6.089834,-7.956362,3.949628,5.943949,-2.376894,-4.943762,4.712650,8.088715,6.135635,1.875123,6.273846,-3.005384,0.402085,8.432273,3.924146,-2.483345,-2.718738,3.509501,-7.087383,-8.009654,-6.827942,-2.374345,4.184982,-5.329182,-8.654730,6.171764,-9.052465,8.900571,4.446763,-0.033822,-4.941384,-9.122930,2.878310,-0.547102,-9.028126,-1.027925,0.358039,-0.433986,-5.847968,8.036488,-5.019469,-3.482697,-0.558517,3.621339,-2.165284,5.898765,-7.570160,0.774991,7.058012,6.680661,6.414297,-9.295131,4.760081,9.229320,9.676232,-6.796496,-2.149684,7.574207,-9.255125,-4.526428,-1.780860,0.289688,6.120252,-8.504083,-5.602008,-9.074557,-0.464862,-2.990267,8.213502,0.807672,6.910114,-5.259396,4.864095,-4.560400,-4.203728,-8.219985,-4.173313,2.013693,4.270964,5.850330,-7.356245,9.452822,-7.306485,-6.796784,1.148628,5.926543,5.271804,-9.905931,0.113495,-9.624663,0.213958,-3.262444,4.668901,9.733641,0.811119,-7.318689,-2.515041,-0.045531,-4.570227,-2.330604,2.665983,-4.321964,-3.939103,9.556492,3.728255,4.724593,-8.144592,3.407257,-2.985797,-4.868047,4.419749,6.840613,-1.657199,-3.153596,-0.390115,6.707734,-8.397579,-3.986337,-8.037679,-2.027714,5.223143,1.174681,0.535457,6.004568,5.324865,-7.499422,1.919499,1.884204,4.429102,-5.436281,-6.775062,5.747399,7.495619,8.941018,4.610438,4.828662,-6.132979,7.646685,2.852664,9.036628,-3.461753,8.008745,2.888376,-5.407432,5.664140,-0.956411,-1.284803,-6.968462,3.652523,8.008921,-5.191003,6.740374,1.303091,-8.329386,-6.707712,-4.129655,6.895039,-7.264274,-5.510774,-3.994482,3.108799,8.583924,-2.533505,1.158157,-1.218545,4.309524,1.245330,1.076740,0.831330,-4.045302,9.499760,-6.804408,-3.825609,7.819645,9.118445,-2.835752,-3.439363,-1.203869,-0.548105,-0.487791,6.630003,6.801393,-6.621775,7.957074,-6.396889,4.613407,-6.464557,1.647559,-9.463582,7.277196,-0.061605,-9.950483,-2.106920,3.069246,-7.139829,2.595186,8.324420,5.468833,8.770742,6.018736,-5.943875,2.654048,7.565825,8.852494,2.400051,6.767707,6.533512,-8.473031,3.026003,-6.325306,1.761189,5.877866,-2.879545,-9.227301,7.268020,1.103946,0.886355,9.213859,5.900613,-1.124080,5.545285,-1.820810,-0.026931,-7.563972,7.367823,9.091131,-4.041308,3.570838,1.146785,-1.221221,-8.497562,-1.086862,-5.094643,-7.556656,5.194261,-4.066589,-5.449038,3.743360,0.844610,-2.886596,-1.356932,9.055036,-4.858840,1.718750,3.282720,7.082891,4.031608,5.477528,3.934810,-9.180859,-7.195922,0.340359,3.248111,5.108935,5.819786,4.342651,-8.747816,-7.213477,-1.396354,-8.651586,-8.781562,9.754057,-4.088831,6.139311,-8.576293,-1.512592,3.060697,7.545084,-8.245774,5.974866,3.862264,3.557394,-3.536532,-6.152748,4.150525,-6.675109,-4.287072,6.872846,-8.807401,-7.336552,-6.078436,3.983723,0.963778,7.755161,-3.732791,9.892783,3.819109,9.229999,-2.550065,-6.468551,-5.344944,7.754372,-0.949034,4.937095,-8.703738,0.208242,-1.147108,-8.200848,-2.714540,0.490541,-6.870582,-4.403275,1.395309,5.558615,2.844145,2.670072,-1.941196,4.590724,-5.928412,0.045367,-2.254115,3.849493,-9.298253,-5.511964,5.987127,1.390236,-0.572495,-9.537172,6.391628,-7.048057,4.567568,-7.118527,-8.622110,9.795568,0.683677,0.080829,2.114434,-6.667558,-8.741364,-4.242715,8.872967,-9.057409,6.733872,4.573741,-0.080784,-2.512573,-2.166912,-5.647934,-7.736990,7.009428,-1.495723,3.770582,5.521549,0.073582,7.086382,-5.000003,5.585050,-4.414055,0.176243,2.950297,0.296553,8.669634,3.374572,5.976254,9.584671,9.410890,0.911590,-6.788559,-6.106445,3.490084,8.159295,-9.260538,-3.062688,-5.918248,2.740810,3.217146,9.145494,-1.308270,-6.682332,-2.069807,-9.988126,-9.065252,-7.699196,-7.420740,-3.688912,-7.596616,9.518197,1.802807,-8.377440,6.163650,7.441438,-1.328651,-2.630628,7.920494,-2.955205,-0.900901,0.379913,6.518862,8.506725,0.804455,5.240608,-4.819771,-9.382031,-3.738170,1.241909,-2.865025,-6.942983,1.985984,8.466722,-2.470297,-4.646562,-5.761875,5.454555,2.360142,-0.814200,-0.467467,5.552953,-6.507305,-9.193309,-6.517884,3.876113,1.079204,9.165128,-0.421682,8.880311,0.846963,9.363221,-9.234613,3.362826,-5.012101,-9.276758,0.421390,4.123215,1.576501,-0.613698,8.366315,8.881410,6.300529,8.745142,0.734922,-7.436215,-0.150827,5.110041,-6.038312,-2.590471,-6.281410,-8.604179,-3.443461,1.930412,0.842688,7.624051,2.233249,4.367181,-1.614338,-1.332644,-0.347980,-6.980584,7.975173,2.262758,-9.210525,-2.352065,-1.065947,-0.845155,-8.257229,-9.931367,9.956656,-7.562408,-4.736632,4.478470,-2.997600,8.231743,4.199794,0.019436,8.006603,-1.264889,-6.527458,-0.358154,4.590984,-6.000233,-0.153073,-2.465054,-0.513076,1.807235,-3.421531,5.210120,-9.778270,6.677606,-7.507342,-8.689469,1.890686,1.653192,0.453750,-7.660525,-1.331333,-7.027888,-6.810391,-6.769476,8.856421,2.267909,4.057853,-6.021575,7.110582,5.912751,-3.486871,0.427701,-6.328479,-1.989279,-5.887289,0.852319,2.509559,-4.782603,-7.774580,-3.079951,-4.041882,4.874856,6.746761,7.049464,-1.176698,-0.547045,7.946598,-4.489670,2.452327,7.549908,-7.589210,-3.339607,6.808373,6.746873,-2.059948,0.896607,3.798576,-3.949496,4.836403,-9.693450,-4.807451,-3.393947,-5.356740,7.080749,4.501355,-3.111858,1.944941,5.478460,0.752724,-9.299815,7.149525,-2.967933,6.497674,6.264279,-3.548603,-2.581172,-4.090671,-1.113379,9.864428,-0.280909,1.241379,-8.388973,-9.504324,5.748538,-5.465000,9.871625,2.887782,8.278649,-2.650822,6.542520,-5.198547,7.169808,9.190269,6.482315,9.210595,3.754999,-4.421754,-5.988413,-5.350720,-5.797925,9.158511,-8.841632,3.338922,0.962841,-4.697806,5.843840,-2.825054,2.312919,-4.640012,5.975673,7.449402,-0.507065,-6.287281,-3.249917,-8.557462,-0.237118,-2.252469,9.809606,-5.373554,9.661788,1.427532,2.770926,8.192461,6.411411,7.178481,1.945748,-9.256772,8.552233,-1.603944,5.873399,-1.332674,2.264765,-0.885615,8.274437,0.724579,0.950784,2.694393,6.403470,0.445142,-2.734232,2.172867,8.081681,-1.356471,-9.163158,-0.493020,0.703713,0.109667,3.198966,5.500515,-2.093750,6.850060,-3.992792,-0.807182,3.129269,-0.645526,8.650579,-3.379976,7.700736,0.540548,1.852121,5.927134,-5.432110,3.417082,-6.960352,-8.720884,-4.171239,-5.388843,-8.309579,-2.840006,4.432315,-0.785718,-7.752795,9.976583,7.668416,8.964585,6.827066,8.009444,-4.956298,8.456628,-7.753882,6.106270,-9.942327,9.886325,8.378239,-2.775746,-4.164584,2.604364,5.511298,0.958253,3.690678,-7.079862,6.073874,-7.236265,-6.902887,0.828613,-6.320090,4.678608,-3.707317,3.915234,-4.303875,-5.032048,-4.972969,2.765141,5.114514,-6.251080,-5.840747,6.133259,1.622243,4.540998,0.582543,-8.458463,4.151526,-1.126849,-6.532993,0.492120,-6.582305,8.320177,1.555114,-8.823192,9.533940,6.985268,3.446064,-7.363344,3.915277], dtype = "float32")#candidate|195|(1260,)|const|float32
call_194 = relay.TupleGetItem(func_169_call(relay.reshape(const_195.astype('float32'), [10, 9, 14]), relay.reshape(const_195.astype('float32'), [10, 9, 14]), relay.reshape(const_195.astype('bool'), [10, 9, 14]), ), 0)
call_196 = relay.TupleGetItem(func_174_call(relay.reshape(const_195.astype('float32'), [10, 9, 14]), relay.reshape(const_195.astype('float32'), [10, 9, 14]), relay.reshape(const_195.astype('bool'), [10, 9, 14]), ), 0)
func_52_call = mod.get_global_var('func_52')
func_56_call = mutated_mod.get_global_var('func_56')
const_201 = relay.const([-6,8,-6,6,-6,2,8,-7,-7,1,-6,1,4,-4,3,-6,2,1,-9,-8,5,-5,5,2,-4,7,3,-1,8,-5,7,-10,-7,8,1,1,8,-6,9,-5,2,2,2,4,9,10,3,4,4,-4,-10,8,-2,-10,-4,-5,-1,-4,10,-2,5,6,2,8,4,1,-8,3,-3,2,-10,-6,3,3,-5,-4,-6,10,2,6,-1,-1,5,-10,7,-8,8,7,3,5,-4,2,-1,2,2,9,-4,-4,-2,-7,-6,-5,8,-6,-1,-3,-1,-9,-1,6,-8,9,-5,10,7,8,2,-8,5,-5,4,-5,5,1,-4,9,4,-3,1,8,-1,-1,-10,-5,-10,3,-10,-3,10,-1,1,-8,10,-5,5,8,10,10,6,-4,8,2,-6,3,9,2,-5,-4,-2,-3,2,4,1,-3,9,-5,7,-7,2,-8,-3,10,1,-3,3,-9,-9,9,6,9,9,4,-9,8,-8,-2,-7,1,6,-10,-1,-6,-1,-2,-6,4,-5,3,7,7,6,-10,-2,2,8,1,-10,-2,9,-9,7,10,2,-7,-5,-8,-4,5,-1,5,8,9,-2,-2,-8,-6,6,8,1,9,-10,8,-5,-9,9,-6,-2,6,9,-5,-1,-4,8,5,9,-7,8,10,-8,10,5,-6,-4,-8,-2,-9,-3,10,-7,5,6,3,-9,7,-4,-7,-6,5,-7,10,8,-4,4,-6,-8,7,5,10,-4,1,6,6,-3,10,6,3,1,6,-1,6,-3,5,-2,-10,-2,2,-9,1,-1,-3,-3,10,-4,-9,9,6,8,-10,8,7,-2,-9,-9,-4,3,7,4,10,-6,-2,-6,-8,2,5,7,2,-10,10,-1,-10,-2,10,6,1,-1,-8,-5,-1,2,9,-9,9,-1,-1,-3,-9,-7,8,-1,7,6,-10,2,8,-9,-5,5,10,-1,8,-1,9,-8,-5,-8,2,10,4,3,-7,-8,-5,-4,-1,-5,1,8,5,-8,6,3,-1,7,-4,-9,7,3,2,-4,-6,-6,6,-8,-1,-9,2,2,-4,9,1,1,5,7,-1,4,1,-4,-3,6,-9,-10,1,-6,-3,5,3,2,-9,-7,2,-8,9,-10,6,-8,-4,-8,10,-10,-9,7,-10,-7,-7,-9,-4,-4,9,-7,9,-2,4,8,3,9,2,1,-4,-10,5,-2,6,-3,-9,10,8,2,1,9,7,-6,-3,-10,-7,2,2,10,9,3,-4,7,-6,-5,9,2,2,-5,-5,4,9,-4,9,7,7,-7,4,6,-2,-6,7,-9,6,-5,-10,4,4,-10,-4,-2,-8,6,2,-1,-3,5,5,-8,-9,1,-2,1,-7,-1,-8,3,-2,8,-1,6,4,-5,-7,-9,7,-6,-8,-7,7,-5,-10,1,-7,6,5,-1,5,-9,10,9,-1,4,-1,4,8,-3,8,-2,2,-1,10,-10,-10,9,1,5,4,-1,2,-5,7,-1,-1,-7,9,-3,-2,5], dtype = "int64")#candidate|201|(567,)|const|int64
call_200 = func_52_call(relay.reshape(const_201.astype('int64'), [9, 7, 9]), relay.reshape(const_201.astype('int64'), [9, 7, 9]), )
call_202 = func_52_call(relay.reshape(const_201.astype('int64'), [9, 7, 9]), relay.reshape(const_201.astype('int64'), [9, 7, 9]), )
uop_203 = relay.atanh(const_182.astype('float64')) # shape=(4, 14, 10)
bop_210 = relay.not_equal(uop_203.astype('bool'), relay.reshape(bop_183.astype('bool'), relay.shape_of(uop_203))) # shape=(4, 14, 10)
func_52_call = mod.get_global_var('func_52')
func_56_call = mutated_mod.get_global_var('func_56')
call_227 = func_52_call(relay.reshape(const_201.astype('int64'), [9, 7, 9]), relay.reshape(const_201.astype('int64'), [9, 7, 9]), )
call_228 = func_52_call(relay.reshape(const_201.astype('int64'), [9, 7, 9]), relay.reshape(const_201.astype('int64'), [9, 7, 9]), )
bop_231 = relay.greater(call_227.astype('bool'), relay.reshape(const_201.astype('bool'), relay.shape_of(call_227))) # shape=(9, 7, 9)
bop_234 = relay.greater(call_228.astype('bool'), relay.reshape(const_201.astype('bool'), relay.shape_of(call_228))) # shape=(9, 7, 9)
func_169_call = mod.get_global_var('func_169')
func_174_call = mutated_mod.get_global_var('func_174')
call_248 = relay.TupleGetItem(func_169_call(relay.reshape(const_195.astype('float32'), [10, 9, 14]), relay.reshape(const_195.astype('float32'), [10, 9, 14]), relay.reshape(const_195.astype('bool'), [10, 9, 14]), ), 0)
call_249 = relay.TupleGetItem(func_174_call(relay.reshape(const_195.astype('float32'), [10, 9, 14]), relay.reshape(const_195.astype('float32'), [10, 9, 14]), relay.reshape(const_195.astype('bool'), [10, 9, 14]), ), 0)
output = relay.Tuple([call_194,const_195,call_200,bop_210,bop_231,call_248,])
output2 = relay.Tuple([call_196,const_195,call_202,bop_210,bop_234,call_249,])
func_252 = relay.Function([], output)
mod['func_252'] = func_252
mod = relay.transform.InferType()(mod)
mutated_mod['func_252'] = func_252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mutated_mod.get_global_var('func_252')
call_253 = func_252_call()
output = call_253
func_254 = relay.Function([], output)
mutated_mod['func_254'] = func_254
mutated_mod = relay.transform.InferType()(mutated_mod)
var_303 = relay.var("var_303", dtype = "float32", shape = (16, 5, 12))#candidate|303|(16, 5, 12)|var|float32
uop_304 = relay.cos(var_303.astype('float32')) # shape=(16, 5, 12)
output = uop_304
output2 = uop_304
func_315 = relay.Function([var_303,], output)
mod['func_315'] = func_315
mod = relay.transform.InferType()(mod)
var_316 = relay.var("var_316", dtype = "float32", shape = (16, 5, 12))#candidate|316|(16, 5, 12)|var|float32
output = func_315(var_316)
func_317 = relay.Function([var_316], output)
mutated_mod['func_317'] = func_317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_350 = relay.TupleGetItem(func_252_call(), 5)
call_351 = relay.TupleGetItem(func_254_call(), 5)
output = call_350
output2 = call_351
func_365 = relay.Function([], output)
mod['func_365'] = func_365
mod = relay.transform.InferType()(mod)
output = func_365()
func_366 = relay.Function([], output)
mutated_mod['func_366'] = func_366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_419 = func_365_call()
call_420 = func_365_call()
uop_421 = relay.rsqrt(call_419.astype('float64')) # shape=(10, 9, 14)
uop_423 = relay.rsqrt(call_420.astype('float64')) # shape=(10, 9, 14)
uop_440 = relay.sin(call_419.astype('float32')) # shape=(10, 9, 14)
uop_442 = relay.sin(call_420.astype('float32')) # shape=(10, 9, 14)
uop_446 = relay.cos(uop_421.astype('float64')) # shape=(10, 9, 14)
uop_448 = relay.cos(uop_423.astype('float64')) # shape=(10, 9, 14)
uop_451 = relay.sigmoid(uop_446.astype('float32')) # shape=(10, 9, 14)
uop_453 = relay.sigmoid(uop_448.astype('float32')) # shape=(10, 9, 14)
uop_456 = relay.asinh(uop_451.astype('float32')) # shape=(10, 9, 14)
uop_458 = relay.asinh(uop_453.astype('float32')) # shape=(10, 9, 14)
output = relay.Tuple([uop_440,uop_456,])
output2 = relay.Tuple([uop_442,uop_458,])
func_465 = relay.Function([], output)
mod['func_465'] = func_465
mod = relay.transform.InferType()(mod)
mutated_mod['func_465'] = func_465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mutated_mod.get_global_var('func_465')
call_466 = func_465_call()
output = call_466
func_467 = relay.Function([], output)
mutated_mod['func_467'] = func_467
mutated_mod = relay.transform.InferType()(mutated_mod)
var_483 = relay.var("var_483", dtype = "int8", shape = ())#candidate|483|()|var|int8
var_484 = relay.var("var_484", dtype = "int8", shape = (13, 9, 3))#candidate|484|(13, 9, 3)|var|int8
bop_485 = relay.right_shift(var_483.astype('int8'), var_484.astype('int8')) # shape=(13, 9, 3)
output = bop_485
output2 = bop_485
func_513 = relay.Function([var_483,var_484,], output)
mod['func_513'] = func_513
mod = relay.transform.InferType()(mod)
var_514 = relay.var("var_514", dtype = "int8", shape = ())#candidate|514|()|var|int8
var_515 = relay.var("var_515", dtype = "int8", shape = (13, 9, 3))#candidate|515|(13, 9, 3)|var|int8
output = func_513(var_514,var_515,)
func_516 = relay.Function([var_514,var_515,], output)
mutated_mod['func_516'] = func_516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_526 = relay.TupleGetItem(func_252_call(), 5)
call_527 = relay.TupleGetItem(func_254_call(), 5)
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_531 = relay.TupleGetItem(func_252_call(), 4)
call_532 = relay.TupleGetItem(func_254_call(), 4)
var_563 = relay.var("var_563", dtype = "float64", shape = (10, 9, 14))#candidate|563|(10, 9, 14)|var|float64
bop_564 = relay.bitwise_or(call_526.astype('uint8'), relay.reshape(var_563.astype('uint8'), relay.shape_of(call_526))) # shape=(10, 9, 14)
bop_567 = relay.bitwise_or(call_527.astype('uint8'), relay.reshape(var_563.astype('uint8'), relay.shape_of(call_527))) # shape=(10, 9, 14)
output = relay.Tuple([call_531,bop_564,])
output2 = relay.Tuple([call_532,bop_567,])
func_569 = relay.Function([var_563,], output)
mod['func_569'] = func_569
mod = relay.transform.InferType()(mod)
var_570 = relay.var("var_570", dtype = "float64", shape = (10, 9, 14))#candidate|570|(10, 9, 14)|var|float64
output = func_569(var_570)
func_571 = relay.Function([var_570], output)
mutated_mod['func_571'] = func_571
mutated_mod = relay.transform.InferType()(mutated_mod)
var_576 = relay.var("var_576", dtype = "float64", shape = (5, 7, 5))#candidate|576|(5, 7, 5)|var|float64
const_577 = relay.const([[[7.765176,5.671713,-2.049262,6.685747,7.813717],[9.228450,-0.744812,-3.046653,-6.305049,-3.963117],[2.093153,9.734755,-8.702185,-4.737386,-0.214653],[0.030491,3.264457,1.856025,-5.536514,-7.930905],[-6.517546,4.115941,-6.045918,-4.900211,2.691503],[3.494330,-2.053894,4.676930,2.562780,7.738737],[4.218273,9.482513,-3.561766,-2.251591,-5.292338]],[[-7.451702,0.284479,8.340414,1.447323,-0.819721],[-8.230239,5.913533,-6.224192,1.209393,-9.883798],[6.642673,8.963837,7.373954,5.161392,-1.056437],[-3.357156,-3.324685,-2.273460,5.195970,6.009920],[-6.498347,6.406430,-5.942127,3.375416,5.110847],[4.107140,9.756345,-2.325562,-2.498054,5.462992],[7.121983,5.335033,3.745514,0.985901,6.965342]],[[-1.581093,-3.222807,-1.070371,4.048463,-2.457047],[3.806125,0.145606,-4.802878,4.092887,-0.813634],[-9.868608,-3.586494,1.638688,3.679526,-3.040463],[-1.364393,0.933631,-6.240630,1.634592,6.821712],[1.015180,0.423171,2.975400,-0.562199,-1.064526],[0.242430,-3.037555,-0.983900,0.920008,-1.350900],[9.275438,-2.202858,0.625866,-8.860289,-8.707988]],[[-1.334157,-7.279522,3.883962,4.104364,0.424419],[-2.663494,-8.466318,-7.274853,-6.651994,9.974026],[-4.399640,0.582225,5.262611,6.592739,-7.546675],[3.785891,3.906051,-0.740404,8.243726,-1.996015],[-3.176227,-6.873850,6.929744,2.803505,-1.540103],[-5.876721,6.131312,-6.625781,-1.488919,-1.759213],[1.598138,2.244464,-4.139114,6.491148,-0.831460]],[[-6.199320,-0.433990,2.966921,6.936419,-0.203051],[0.211507,-9.814806,-8.004921,6.316816,5.165862],[9.260627,0.157002,9.214504,9.606266,-8.880269],[3.395819,-9.821047,7.100971,3.627511,-3.992057],[-8.761571,5.623753,8.768283,0.785278,-3.300033],[-3.558004,-4.675281,6.294476,3.388658,-6.404046],[-6.139455,-6.145498,-1.507866,-7.820298,0.688182]]], dtype = "float64")#candidate|577|(5, 7, 5)|const|float64
bop_578 = relay.divide(var_576.astype('float64'), relay.reshape(const_577.astype('float64'), relay.shape_of(var_576))) # shape=(5, 7, 5)
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_589 = relay.TupleGetItem(func_252_call(), 3)
call_590 = relay.TupleGetItem(func_254_call(), 3)
output = relay.Tuple([bop_578,call_589,])
output2 = relay.Tuple([bop_578,call_590,])
func_610 = relay.Function([var_576,], output)
mod['func_610'] = func_610
mod = relay.transform.InferType()(mod)
mutated_mod['func_610'] = func_610
mutated_mod = relay.transform.InferType()(mutated_mod)
var_611 = relay.var("var_611", dtype = "float64", shape = (5, 7, 5))#candidate|611|(5, 7, 5)|var|float64
func_610_call = mutated_mod.get_global_var('func_610')
call_612 = func_610_call(var_611)
output = call_612
func_613 = relay.Function([var_611], output)
mutated_mod['func_613'] = func_613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_680 = relay.var("var_680", dtype = "float32", shape = (14, 1, 9))#candidate|680|(14, 1, 9)|var|float32
uop_681 = relay.rsqrt(var_680.astype('float32')) # shape=(14, 1, 9)
bop_686 = relay.less_equal(uop_681.astype('bool'), relay.reshape(var_680.astype('bool'), relay.shape_of(uop_681))) # shape=(14, 1, 9)
output = relay.Tuple([bop_686,])
output2 = relay.Tuple([bop_686,])
func_689 = relay.Function([var_680,], output)
mod['func_689'] = func_689
mod = relay.transform.InferType()(mod)
var_690 = relay.var("var_690", dtype = "float32", shape = (14, 1, 9))#candidate|690|(14, 1, 9)|var|float32
output = func_689(var_690)
func_691 = relay.Function([var_690], output)
mutated_mod['func_691'] = func_691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_705 = relay.TupleGetItem(func_465_call(), 0)
call_706 = relay.TupleGetItem(func_467_call(), 0)
uop_714 = relay.sinh(call_705.astype('float32')) # shape=(10, 9, 14)
uop_716 = relay.sinh(call_706.astype('float32')) # shape=(10, 9, 14)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_720 = func_365_call()
call_721 = func_365_call()
output = relay.Tuple([uop_714,call_720,])
output2 = relay.Tuple([uop_716,call_721,])
func_730 = relay.Function([], output)
mod['func_730'] = func_730
mod = relay.transform.InferType()(mod)
output = func_730()
func_731 = relay.Function([], output)
mutated_mod['func_731'] = func_731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_816 = relay.var("var_816", dtype = "float64", shape = (2, 6, 11))#candidate|816|(2, 6, 11)|var|float64
uop_817 = relay.atanh(var_816.astype('float64')) # shape=(2, 6, 11)
func_730_call = mod.get_global_var('func_730')
func_731_call = mutated_mod.get_global_var('func_731')
call_819 = relay.TupleGetItem(func_730_call(), 1)
call_820 = relay.TupleGetItem(func_731_call(), 1)
func_730_call = mod.get_global_var('func_730')
func_731_call = mutated_mod.get_global_var('func_731')
call_821 = relay.TupleGetItem(func_730_call(), 1)
call_822 = relay.TupleGetItem(func_731_call(), 1)
func_689_call = mod.get_global_var('func_689')
func_691_call = mutated_mod.get_global_var('func_691')
var_825 = relay.var("var_825", dtype = "float32", shape = (126,))#candidate|825|(126,)|var|float32
call_824 = relay.TupleGetItem(func_689_call(relay.reshape(var_825.astype('float32'), [14, 1, 9])), 0)
call_826 = relay.TupleGetItem(func_691_call(relay.reshape(var_825.astype('float32'), [14, 1, 9])), 0)
output = relay.Tuple([uop_817,call_819,call_821,call_824,var_825,])
output2 = relay.Tuple([uop_817,call_820,call_822,call_826,var_825,])
func_830 = relay.Function([var_816,var_825,], output)
mod['func_830'] = func_830
mod = relay.transform.InferType()(mod)
mutated_mod['func_830'] = func_830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_830_call = mutated_mod.get_global_var('func_830')
var_832 = relay.var("var_832", dtype = "float64", shape = (2, 6, 11))#candidate|832|(2, 6, 11)|var|float64
var_833 = relay.var("var_833", dtype = "float32", shape = (126,))#candidate|833|(126,)|var|float32
call_831 = func_830_call(var_832,var_833,)
output = call_831
func_834 = relay.Function([var_832,var_833,], output)
mutated_mod['func_834'] = func_834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_730_call = mod.get_global_var('func_730')
func_731_call = mutated_mod.get_global_var('func_731')
call_862 = relay.TupleGetItem(func_730_call(), 0)
call_863 = relay.TupleGetItem(func_731_call(), 0)
output = call_862
output2 = call_863
func_876 = relay.Function([], output)
mod['func_876'] = func_876
mod = relay.transform.InferType()(mod)
mutated_mod['func_876'] = func_876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mutated_mod.get_global_var('func_876')
call_877 = func_876_call()
output = call_877
func_878 = relay.Function([], output)
mutated_mod['func_878'] = func_878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_881 = func_365_call()
call_882 = func_365_call()
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_890 = relay.TupleGetItem(func_252_call(), 3)
call_891 = relay.TupleGetItem(func_254_call(), 3)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_894 = func_365_call()
call_895 = func_365_call()
const_896 = relay.const([[[True,False,True,False,True,False,False,True,True,False],[True,True,False,True,True,True,False,True,True,True],[True,True,False,True,False,True,False,False,True,False],[False,False,False,True,False,True,True,False,False,False],[False,True,True,False,True,False,True,True,True,False],[False,True,False,False,False,False,True,False,False,False],[True,False,False,True,True,True,True,False,True,True],[True,False,True,False,False,False,True,False,True,False],[False,True,True,False,True,True,True,False,False,True],[False,True,False,False,False,True,True,True,False,True],[True,True,True,False,True,True,False,False,True,True],[True,False,False,False,False,True,False,True,True,False],[True,True,True,True,True,True,False,True,True,False],[False,False,True,True,False,True,False,False,True,False]],[[True,False,False,True,True,False,False,True,False,True],[True,True,False,False,False,True,True,False,False,False],[True,False,False,False,True,False,True,False,False,True],[False,True,True,False,False,False,False,False,True,False],[True,False,True,True,False,True,True,False,False,True],[False,True,False,True,True,True,True,True,True,False],[False,True,True,True,True,False,False,False,False,True],[False,False,False,False,True,False,True,False,False,True],[False,True,False,False,False,False,True,True,True,True],[True,True,False,True,False,False,True,False,False,True],[False,False,True,False,False,True,False,False,True,True],[True,True,False,False,True,False,False,True,True,True],[False,True,False,False,False,False,False,True,True,False],[False,True,True,False,True,True,True,True,True,False]],[[False,True,False,False,True,True,False,True,False,False],[False,False,True,False,True,True,False,True,False,True],[False,False,False,True,False,True,False,True,True,False],[False,True,True,False,False,False,True,False,True,False],[False,True,False,True,True,True,False,True,True,False],[True,True,True,True,False,True,True,False,True,False],[False,True,True,True,True,True,True,False,False,False],[False,False,True,True,False,False,False,False,False,True],[True,True,False,False,False,False,True,True,True,False],[True,True,True,True,True,False,False,False,True,False],[True,True,True,False,False,True,True,True,True,True],[False,False,False,True,False,False,True,False,False,False],[False,True,False,False,False,True,False,True,True,True],[True,False,True,False,True,True,True,False,False,True]],[[True,True,True,True,False,False,True,True,False,True],[False,False,True,False,False,True,True,True,False,False],[False,False,True,True,False,False,True,False,False,True],[True,True,False,False,False,False,False,True,False,False],[True,False,True,False,False,True,True,True,False,False],[True,True,False,False,False,False,False,True,False,False],[True,True,True,True,False,True,False,False,True,False],[True,False,False,False,False,False,True,True,True,False],[True,False,True,True,True,True,False,True,True,False],[False,False,False,True,True,False,True,True,False,False],[True,True,False,True,True,False,True,True,True,False],[True,True,True,False,False,False,True,False,True,False],[True,True,False,True,True,False,True,False,True,True],[False,True,True,False,False,False,False,False,True,True]]], dtype = "bool")#candidate|896|(4, 14, 10)|const|bool
bop_897 = relay.minimum(call_890.astype('float32'), relay.reshape(const_896.astype('float32'), relay.shape_of(call_890))) # shape=(4, 14, 10)
bop_900 = relay.minimum(call_891.astype('float32'), relay.reshape(const_896.astype('float32'), relay.shape_of(call_891))) # shape=(4, 14, 10)
uop_903 = relay.acosh(call_890.astype('float32')) # shape=(4, 14, 10)
uop_905 = relay.acosh(call_891.astype('float32')) # shape=(4, 14, 10)
output = relay.Tuple([call_881,call_894,bop_897,uop_903,])
output2 = relay.Tuple([call_882,call_895,bop_900,uop_905,])
func_909 = relay.Function([], output)
mod['func_909'] = func_909
mod = relay.transform.InferType()(mod)
output = func_909()
func_910 = relay.Function([], output)
mutated_mod['func_910'] = func_910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_1059 = func_876_call()
call_1060 = func_876_call()
const_1067 = relay.const([[[1.654566,6.630904,6.253019,2.891484,-9.411701,-9.288325,-4.068875,-0.809539,6.915113,9.284081,-4.374390,-2.973442,1.387862,-3.707657],[-2.528296,-1.499941,0.115291,-4.276010,9.113007,-1.985129,5.487054,7.880184,8.485445,-8.767126,-5.696531,7.667566,-8.138023,0.979920],[1.301524,8.138267,6.309828,7.258634,2.840131,-1.843668,-4.064334,4.160280,6.983175,3.759572,-1.012546,5.077259,-7.103920,0.691701],[6.366343,-8.771037,-2.215409,-4.389846,-7.578711,-6.261226,9.047207,-9.460166,-3.336078,-6.174422,-6.443993,-5.734616,1.420231,-9.843938],[-9.917994,-6.494297,-6.043793,1.351516,-7.710760,7.988869,9.346749,-4.992057,-3.449955,-5.048352,-4.428793,-0.292170,0.687376,0.543757],[1.396985,-5.132332,0.247657,1.166159,9.286019,-0.337926,-0.659769,-0.223703,-0.243425,2.563297,-0.295200,3.310639,-1.735836,2.473989],[-5.469701,-1.843635,-7.606778,8.030314,2.172425,-1.055558,1.662535,-7.766463,-0.267007,-1.810654,9.919403,0.755020,0.823826,6.667458],[-8.142388,3.024801,6.155079,-4.219077,-3.704112,-1.979030,-0.494091,7.033936,5.686390,-5.557148,-3.537216,-7.904442,-0.039001,7.632075],[-1.371363,1.375951,-8.564607,8.898265,-5.513778,0.328891,-0.092511,-1.612355,-0.063292,-1.740597,6.434122,4.980030,1.154964,0.124120]],[[1.019838,-6.262523,8.933052,0.419551,-2.973073,-8.492603,-1.494274,-9.401890,4.522200,-9.839821,-5.678433,3.346024,1.044754,6.052422],[3.917517,-5.999290,-8.689700,-6.857046,-8.464542,2.140466,5.408186,7.221631,2.680946,-9.977842,-1.703821,9.938347,8.945338,-0.598652],[0.530787,-4.083041,-6.920739,-0.732762,9.368480,0.579652,-2.585827,-4.995861,-3.595747,5.857864,7.139939,-1.186879,-5.992759,-8.890129],[-1.386580,-2.695100,0.628761,-7.040658,4.159900,-6.883957,-3.755578,-3.965782,-1.434867,-4.246101,-8.217610,-9.929664,0.171934,8.064138],[-3.409289,9.576046,-5.225958,5.185996,-8.029610,-3.318977,-0.930413,-2.540430,-6.316744,4.688658,-8.987962,9.648227,3.286610,-5.030744],[-8.810780,6.643097,-8.760883,3.690585,-1.733511,-0.485640,0.733256,2.411985,2.814006,-4.009026,-8.611150,-1.664209,1.014343,-8.646358],[7.313329,7.978681,-1.548104,2.502468,9.980855,-1.730709,2.353960,7.858629,1.962839,-4.927066,-3.155798,-9.537508,-4.207824,3.320778],[-7.521684,-5.951777,7.410175,1.855046,-8.468451,-9.164185,0.147243,-0.268020,8.967577,4.681605,-4.126357,6.511021,-1.392194,8.297568],[-4.952182,-4.020590,-4.915875,-8.252866,-4.203836,-8.772660,-7.270515,5.231162,2.413167,-3.688817,2.765771,2.883212,8.287434,-2.079417]],[[-7.051389,-1.913273,9.105878,8.762150,-7.355995,3.746789,9.696007,8.764080,-7.898442,7.965382,-4.722053,-7.458865,-9.556744,0.743344],[-1.080696,4.281179,-5.417521,4.516419,5.902778,8.655034,-2.113304,-4.889528,-6.014830,-6.541317,-3.281447,-8.321844,5.415758,-3.455984],[-9.147644,-2.233505,-1.456828,9.954067,1.133685,-5.308227,8.400104,-7.702389,-1.953029,5.943915,8.411148,7.942542,-1.447685,-2.084855],[-5.695753,3.916965,7.970518,6.042119,8.146935,-6.636816,1.852327,2.618417,-2.276325,-6.253783,2.161054,-0.650329,3.851337,-6.490984],[3.283571,-9.264667,-9.035645,7.161980,3.499612,3.029421,0.150321,4.018800,-7.188799,-2.773589,1.252517,6.885404,-2.786189,3.966277],[1.848430,8.440778,-8.429727,-4.520429,4.599858,-9.912858,-5.894875,-7.945675,2.508317,-6.893955,-1.491447,9.061896,2.425375,-5.471329],[-9.345789,-0.513578,-5.507185,-3.520026,2.432484,5.593005,-9.114071,0.711316,0.496280,7.037910,8.728415,-9.664316,-7.319833,3.831272],[-6.612010,4.364512,7.886299,-6.661506,-1.942297,5.820582,6.998166,-5.733981,-5.317873,-0.937400,9.784676,3.826850,3.467170,3.780122],[8.257654,3.413538,-5.329991,-8.061303,-1.195479,4.761670,2.508471,-0.494005,3.626446,1.785045,-1.080634,1.191270,7.345951,1.578251]],[[-1.256839,-2.937703,8.847160,8.254754,-2.950781,-3.527812,-3.999465,2.312699,-6.548195,-9.513018,3.522011,8.165646,5.626313,2.778438],[3.276974,5.792945,3.534895,8.790259,-0.037764,9.887226,-5.495795,8.196817,5.889186,3.634443,5.307001,-2.488042,5.442696,-3.960893],[-1.145157,0.960853,-8.583793,-5.063960,-1.698169,5.082551,-6.122450,7.670033,-7.999088,-2.148384,-9.540473,7.863456,0.636901,-8.066378],[0.042011,-8.310505,-8.636318,-8.646257,-9.096607,4.177366,-0.614446,6.922977,5.829561,-0.112482,-0.265085,1.108185,-0.596903,-3.189811],[-9.206677,-7.768223,1.976290,-7.199620,-2.825238,9.032783,0.280795,3.138717,8.561606,-3.808938,2.575412,-5.852309,4.226937,-1.391229],[-4.353969,-4.257337,6.606099,-5.581997,3.065464,0.665106,6.270245,-2.415078,1.117170,9.667884,8.825988,3.224341,-1.862725,-8.537782],[2.218302,3.634777,9.709531,7.704166,-0.179539,4.712795,-0.083988,8.317652,0.888650,-4.300596,6.327436,8.548281,4.521310,0.854259],[-6.074798,-9.399273,4.342771,7.672616,3.115866,3.026422,1.422815,5.034950,9.885372,3.048199,-1.757098,7.257697,5.066076,-0.113597],[3.358709,-0.667536,5.697131,-7.191744,-9.806303,0.051122,-3.761634,2.482039,-7.158259,9.963613,5.536788,-7.803274,-9.019199,9.097393]],[[8.074297,-3.751899,-0.938730,-2.187007,9.140920,-3.754762,9.909482,8.243251,-3.987876,7.447308,9.542259,5.147169,0.382002,1.010407],[7.734630,-2.540994,-1.205559,-2.547691,1.165181,6.428320,6.186276,9.851988,0.788862,-6.555191,1.538367,-7.222670,-2.368199,-8.047491],[-4.828985,4.034532,-0.061368,-8.810677,-2.788877,7.643047,9.986318,1.607104,-4.021116,7.528332,2.919787,-9.232881,0.400359,-0.343469],[-9.639096,-2.689544,-8.018498,-7.697162,3.801997,5.408320,8.197146,5.376823,9.409590,6.721153,0.198281,-8.213042,-9.664485,-6.890273],[4.589343,4.478271,7.122421,-7.302129,0.846048,-6.542254,1.179386,8.090007,5.634050,-1.457623,8.401842,-3.995638,-9.534005,4.519490],[7.676502,2.556141,-4.267012,-4.236840,-4.547795,4.471062,-3.778465,-1.568274,-2.283072,-0.578412,-5.064245,-0.179076,1.853901,8.419421],[2.789237,-2.121503,-6.024273,-4.967641,9.481977,-7.356331,9.902025,0.863513,4.252924,-4.334267,5.832730,2.050689,7.955332,6.728307],[7.755775,-4.434084,-9.368931,6.667881,-3.209003,4.438978,6.866320,2.590264,-8.282237,-7.338500,-1.803195,6.218850,4.675076,-2.305548],[-3.902750,7.911023,-6.425181,7.927284,3.709671,5.119615,-7.414230,4.432731,-4.052497,-3.267185,5.729547,-8.635998,1.357655,-0.427363]],[[0.153516,7.256596,-5.211927,1.472839,9.108047,8.040447,0.290374,-0.652234,-9.501149,2.879998,3.626246,4.911590,-7.780028,-7.725032],[4.136965,7.663631,1.593323,-1.089154,7.983974,-1.817584,-6.094321,0.487979,-5.578135,2.346891,4.417330,9.310962,2.378919,-7.846506],[8.057208,1.502748,1.554395,9.466669,-4.825647,-0.381501,9.557056,-9.113144,7.291305,1.466398,6.329809,-2.336581,-4.640340,9.192877],[-8.562214,1.822882,6.625068,-0.133319,4.691603,7.719222,2.643316,-5.871590,1.778121,5.788232,-0.670453,-4.197641,5.152625,1.136961],[5.331076,2.276598,-3.286114,5.064944,-1.793860,-7.505109,8.485900,0.653427,1.559909,1.082534,-0.302889,2.610493,1.936785,-2.781584],[-0.736517,-0.479963,2.370866,4.891494,9.967645,4.272882,-4.856652,8.692892,3.781964,3.064564,-4.234957,2.154475,3.242154,-7.150065],[5.907837,2.060880,-6.601889,7.508018,-8.361489,3.538132,3.592701,2.111097,-0.191248,6.581521,5.407993,-7.155151,8.189835,-2.716104],[1.985766,8.451115,9.594674,-1.926341,1.237027,6.573282,3.853099,9.544969,5.664577,-3.420830,0.335434,-4.103993,-0.085693,3.273799],[-2.878409,-2.958589,-7.874923,-7.546112,1.409186,6.653813,-4.398147,-9.430725,1.078369,-9.605287,-9.851266,-3.056794,-0.169853,-8.682086]],[[6.373622,-3.607866,2.103535,7.088485,2.403850,5.874244,0.726049,6.302461,-9.160570,6.693546,4.975150,-0.019532,-8.161544,1.988638],[8.267762,-4.126571,0.836180,2.529735,7.187093,-4.267822,-0.005503,5.650879,-3.266416,-8.086151,-0.560042,-8.804637,7.545254,8.289255],[5.149677,6.483898,-7.989213,-7.678450,-0.684461,-0.070778,-2.359274,-0.728004,9.697023,-4.853233,-3.155961,-3.745122,-1.187034,-0.018447],[0.800754,-8.655223,6.153961,-7.466973,6.025226,1.637813,-2.215331,8.366668,6.796695,1.484751,-2.713732,-1.734525,-6.253756,0.106035],[-5.190156,5.789208,-4.220838,-8.688407,0.103453,6.510101,7.741426,-2.969696,6.912674,2.979803,-0.476123,6.367268,-0.944992,1.089829],[-1.616209,-9.238703,0.747294,-9.969757,5.014914,4.999140,5.456404,0.276613,3.888376,-1.464951,0.202372,8.811564,4.884019,-9.916510],[7.741016,-6.604159,5.676721,-9.822281,-7.050623,-2.652694,5.705442,-0.531512,-7.553686,-5.948633,-4.995678,-2.891811,-7.779092,3.020148],[-8.286078,0.886038,8.994733,0.718668,-4.207382,2.041911,8.097899,-5.741525,3.206711,9.254871,-7.819874,-5.813209,1.031172,9.049974],[-9.481405,0.088889,-0.763488,-7.920024,-1.392960,-6.627857,8.181998,-1.839511,5.893711,-3.184947,4.138628,6.314907,5.840568,-4.173905]],[[-0.021939,-4.096817,-6.182470,-1.656808,-3.349890,4.353346,-4.555721,-3.033576,7.144764,-9.862277,7.331396,-6.126435,7.473715,4.138401],[6.132500,7.828085,0.115797,-5.862890,6.898872,-8.964937,-5.456437,-9.576815,-2.494870,-0.365460,2.850759,-9.422747,1.845111,-0.694571],[-3.560879,7.299942,3.494234,-6.144561,-6.800684,9.569284,8.910690,-7.270394,8.963173,-6.602976,5.487546,0.630932,-6.197979,9.791116],[-4.764083,-3.131213,7.577936,-0.276610,-2.194261,3.901182,-0.683350,-5.648822,6.931801,5.657915,2.953664,-7.124842,-0.026890,-6.770185],[6.718441,9.599536,8.610102,6.849811,4.487288,9.211897,-9.937865,8.591319,9.004871,-0.872572,-0.009802,8.924774,4.703894,-9.077765],[-6.799015,-9.647316,-5.365707,4.334525,2.101579,5.161877,4.842364,-5.073842,6.152763,-7.477536,1.894715,9.458344,-4.296351,-5.969848],[-1.136466,2.230609,1.322007,2.467223,3.071414,0.983063,9.440930,-2.269885,8.208877,-3.215152,-3.742448,-6.180033,2.272486,1.451441],[-7.334036,2.243893,-2.480708,7.316722,0.505455,6.050924,-1.646023,1.139325,8.789463,-1.841762,6.119008,-1.693960,8.908903,9.432738],[-1.143184,-3.595172,-4.611301,-2.046666,-6.304808,-6.305762,-9.521423,9.833765,-3.889643,-8.055639,-2.062294,9.388266,5.615366,5.101199]],[[-4.520643,9.830981,8.629302,4.275578,9.522191,-7.175124,-5.981304,1.338078,-9.528283,7.079630,-2.335585,3.343438,-2.465693,-3.329883],[-2.308943,-3.276539,-5.930401,4.371999,5.794043,-2.642272,-4.468733,-6.945352,5.041956,8.601921,-3.820196,4.853423,-8.240331,8.948418],[5.274078,-8.362002,0.983002,-6.934555,-2.263073,2.576082,-0.987244,3.342351,-5.795260,9.321040,5.820378,-1.726798,1.880289,-2.150330],[-5.432517,-1.441618,8.298625,1.165978,8.700635,3.794975,5.020603,2.046595,-3.058199,6.303855,0.400131,-7.783221,3.220949,-0.583358],[-5.814252,2.695678,1.490088,-9.133316,-5.169278,2.166419,0.801641,-0.018283,-0.449296,7.629970,-4.463529,4.272044,9.349779,-1.855075],[-1.529474,-2.341471,-3.117545,8.413953,0.654826,-3.154279,9.565422,-9.125562,-6.702351,-5.975455,-7.406363,8.346123,-8.868601,-7.680302],[7.745644,-2.756670,-6.965898,-3.273823,-4.716577,-8.944572,-9.954827,-5.850944,-5.103328,-6.522844,1.123503,1.510301,-4.593153,-4.214649],[-6.525291,3.156850,2.073203,2.759994,-2.844078,-9.512946,-9.963924,-4.679960,-1.723842,-1.616063,0.031047,0.513241,3.282024,4.046251],[-0.196965,-4.867118,-4.747891,-5.269024,-8.052391,5.677390,5.258350,9.657990,-6.748937,-3.420387,-5.812102,-5.126295,-8.050649,-0.048716]],[[-6.972627,1.242489,1.802944,2.289545,1.745610,-9.912056,-3.258564,-8.683979,2.394891,4.492922,-8.463967,-9.971046,-2.130343,-3.282784],[8.596215,9.718689,-7.940288,-1.675628,-4.448716,-2.090806,6.757127,7.771394,-7.454481,0.709241,-7.319343,-0.889880,0.212560,0.340281],[3.281131,-5.943809,1.851829,-9.187448,-4.255324,2.634669,3.701946,5.651180,-4.329265,-4.513372,-7.288673,8.729528,-0.150205,3.883054],[-9.476740,9.210686,4.884656,-3.134154,7.212317,-6.548994,8.418346,4.392603,7.644251,6.258566,7.025433,7.428950,-4.457523,-4.777954],[-9.068892,-9.918199,7.259871,-3.995353,8.242202,5.442028,4.591457,-5.083243,8.444574,9.633943,-3.299245,9.630416,-3.236471,-8.169098],[1.965543,7.676699,-2.607787,-1.781583,-6.763002,-8.811007,-2.401803,-2.148670,-0.253245,-3.246931,-7.660827,-0.742401,8.822744,9.372918],[-6.589915,-9.348055,-8.304839,4.828795,3.956337,-6.383537,-2.472936,7.146174,-4.842168,9.551555,-3.711539,3.124677,8.015692,-6.204816],[1.556785,9.003860,0.697575,6.385897,4.704652,-1.915271,-3.154931,-2.529511,-8.812203,9.146954,-5.433217,0.641649,5.859146,3.869464],[-8.371321,2.112828,7.569676,-3.558453,-0.773489,1.251154,-0.852903,-9.519139,-4.303805,-4.839037,-0.758719,-5.613729,-8.383061,6.759853]]], dtype = "float32")#candidate|1067|(10, 9, 14)|const|float32
bop_1068 = relay.subtract(call_1059.astype('int8'), relay.reshape(const_1067.astype('int8'), relay.shape_of(call_1059))) # shape=(10, 9, 14)
bop_1071 = relay.subtract(call_1060.astype('int8'), relay.reshape(const_1067.astype('int8'), relay.shape_of(call_1060))) # shape=(10, 9, 14)
func_169_call = mod.get_global_var('func_169')
func_174_call = mutated_mod.get_global_var('func_174')
call_1075 = relay.TupleGetItem(func_169_call(relay.reshape(call_1059.astype('float32'), [10, 9, 14]), relay.reshape(bop_1068.astype('float32'), [10, 9, 14]), relay.reshape(bop_1068.astype('bool'), [10, 9, 14]), ), 1)
call_1076 = relay.TupleGetItem(func_174_call(relay.reshape(call_1059.astype('float32'), [10, 9, 14]), relay.reshape(bop_1068.astype('float32'), [10, 9, 14]), relay.reshape(bop_1068.astype('bool'), [10, 9, 14]), ), 1)
output = relay.Tuple([bop_1068,call_1075,])
output2 = relay.Tuple([bop_1071,call_1076,])
func_1083 = relay.Function([], output)
mod['func_1083'] = func_1083
mod = relay.transform.InferType()(mod)
output = func_1083()
func_1084 = relay.Function([], output)
mutated_mod['func_1084'] = func_1084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_1136 = func_365_call()
call_1137 = func_365_call()
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_1146 = relay.TupleGetItem(func_465_call(), 1)
call_1147 = relay.TupleGetItem(func_467_call(), 1)
uop_1148 = relay.atanh(call_1146.astype('float64')) # shape=(10, 9, 14)
uop_1150 = relay.atanh(call_1147.astype('float64')) # shape=(10, 9, 14)
var_1154 = relay.var("var_1154", dtype = "float64", shape = (10, 9, 14))#candidate|1154|(10, 9, 14)|var|float64
bop_1155 = relay.greater(uop_1148.astype('bool'), relay.reshape(var_1154.astype('bool'), relay.shape_of(uop_1148))) # shape=(10, 9, 14)
bop_1158 = relay.greater(uop_1150.astype('bool'), relay.reshape(var_1154.astype('bool'), relay.shape_of(uop_1150))) # shape=(10, 9, 14)
func_569_call = mod.get_global_var('func_569')
func_571_call = mutated_mod.get_global_var('func_571')
call_1159 = relay.TupleGetItem(func_569_call(relay.reshape(bop_1155.astype('float64'), [10, 9, 14])), 1)
call_1160 = relay.TupleGetItem(func_571_call(relay.reshape(bop_1155.astype('float64'), [10, 9, 14])), 1)
output = relay.Tuple([call_1136,bop_1155,call_1159,])
output2 = relay.Tuple([call_1137,bop_1158,call_1160,])
func_1163 = relay.Function([var_1154,], output)
mod['func_1163'] = func_1163
mod = relay.transform.InferType()(mod)
mutated_mod['func_1163'] = func_1163
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1164 = relay.var("var_1164", dtype = "float64", shape = (10, 9, 14))#candidate|1164|(10, 9, 14)|var|float64
func_1163_call = mutated_mod.get_global_var('func_1163')
call_1165 = func_1163_call(var_1164)
output = call_1165
func_1166 = relay.Function([var_1164], output)
mutated_mod['func_1166'] = func_1166
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1190 = relay.var("var_1190", dtype = "float32", shape = (1, 2, 16))#candidate|1190|(1, 2, 16)|var|float32
uop_1191 = relay.sinh(var_1190.astype('float32')) # shape=(1, 2, 16)
output = relay.Tuple([uop_1191,])
output2 = relay.Tuple([uop_1191,])
func_1197 = relay.Function([var_1190,], output)
mod['func_1197'] = func_1197
mod = relay.transform.InferType()(mod)
var_1198 = relay.var("var_1198", dtype = "float32", shape = (1, 2, 16))#candidate|1198|(1, 2, 16)|var|float32
output = func_1197(var_1198)
func_1199 = relay.Function([var_1198], output)
mutated_mod['func_1199'] = func_1199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_1215 = relay.TupleGetItem(func_909_call(), 1)
call_1216 = relay.TupleGetItem(func_910_call(), 1)
output = call_1215
output2 = call_1216
func_1223 = relay.Function([], output)
mod['func_1223'] = func_1223
mod = relay.transform.InferType()(mod)
output = func_1223()
func_1224 = relay.Function([], output)
mutated_mod['func_1224'] = func_1224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_1250 = relay.TupleGetItem(func_252_call(), 1)
call_1251 = relay.TupleGetItem(func_254_call(), 1)
func_169_call = mod.get_global_var('func_169')
func_174_call = mutated_mod.get_global_var('func_174')
call_1255 = relay.TupleGetItem(func_169_call(relay.reshape(call_1250.astype('float32'), [10, 9, 14]), relay.reshape(call_1250.astype('float32'), [10, 9, 14]), relay.reshape(call_1250.astype('bool'), [10, 9, 14]), ), 1)
call_1256 = relay.TupleGetItem(func_174_call(relay.reshape(call_1250.astype('float32'), [10, 9, 14]), relay.reshape(call_1250.astype('float32'), [10, 9, 14]), relay.reshape(call_1250.astype('bool'), [10, 9, 14]), ), 1)
uop_1260 = relay.erf(call_1250.astype('float32')) # shape=(1260,)
uop_1262 = relay.erf(call_1251.astype('float32')) # shape=(1260,)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_1277 = relay.TupleGetItem(func_465_call(), 1)
call_1278 = relay.TupleGetItem(func_467_call(), 1)
output = relay.Tuple([call_1255,uop_1260,call_1277,])
output2 = relay.Tuple([call_1256,uop_1262,call_1278,])
func_1289 = relay.Function([], output)
mod['func_1289'] = func_1289
mod = relay.transform.InferType()(mod)
mutated_mod['func_1289'] = func_1289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1289_call = mutated_mod.get_global_var('func_1289')
call_1290 = func_1289_call()
output = call_1290
func_1291 = relay.Function([], output)
mutated_mod['func_1291'] = func_1291
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1292 = relay.const(-4, dtype = "uint64")#candidate|1292|()|const|uint64
var_1293 = relay.var("var_1293", dtype = "uint64", shape = (10, 7, 3))#candidate|1293|(10, 7, 3)|var|uint64
bop_1294 = relay.maximum(const_1292.astype('uint64'), var_1293.astype('uint64')) # shape=(10, 7, 3)
uop_1319 = relay.rsqrt(var_1293.astype('float32')) # shape=(10, 7, 3)
output = relay.Tuple([bop_1294,uop_1319,])
output2 = relay.Tuple([bop_1294,uop_1319,])
func_1331 = relay.Function([var_1293,], output)
mod['func_1331'] = func_1331
mod = relay.transform.InferType()(mod)
mutated_mod['func_1331'] = func_1331
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1332 = relay.var("var_1332", dtype = "uint64", shape = (10, 7, 3))#candidate|1332|(10, 7, 3)|var|uint64
func_1331_call = mutated_mod.get_global_var('func_1331')
call_1333 = func_1331_call(var_1332)
output = call_1333
func_1334 = relay.Function([var_1332], output)
mutated_mod['func_1334'] = func_1334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mod.get_global_var('func_1223')
func_1224_call = mutated_mod.get_global_var('func_1224')
call_1386 = func_1223_call()
call_1387 = func_1223_call()
func_513_call = mod.get_global_var('func_513')
func_516_call = mutated_mod.get_global_var('func_516')
const_1389 = relay.const(5, dtype = "int8")#candidate|1389|()|const|int8
var_1390 = relay.var("var_1390", dtype = "int8", shape = (351,))#candidate|1390|(351,)|var|int8
call_1388 = func_513_call(relay.reshape(const_1389.astype('int8'), []), relay.reshape(var_1390.astype('int8'), [13, 9, 3]), )
call_1391 = func_513_call(relay.reshape(const_1389.astype('int8'), []), relay.reshape(var_1390.astype('int8'), [13, 9, 3]), )
output = relay.Tuple([call_1386,call_1388,const_1389,var_1390,])
output2 = relay.Tuple([call_1387,call_1391,const_1389,var_1390,])
func_1414 = relay.Function([var_1390,], output)
mod['func_1414'] = func_1414
mod = relay.transform.InferType()(mod)
mutated_mod['func_1414'] = func_1414
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1415 = relay.var("var_1415", dtype = "int8", shape = (351,))#candidate|1415|(351,)|var|int8
func_1414_call = mutated_mod.get_global_var('func_1414')
call_1416 = func_1414_call(var_1415)
output = call_1416
func_1417 = relay.Function([var_1415], output)
mutated_mod['func_1417'] = func_1417
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1423 = relay.var("var_1423", dtype = "float64", shape = (1, 15, 9))#candidate|1423|(1, 15, 9)|var|float64
var_1424 = relay.var("var_1424", dtype = "float64", shape = (15, 15, 9))#candidate|1424|(15, 15, 9)|var|float64
bop_1425 = relay.floor_divide(var_1423.astype('float64'), var_1424.astype('float64')) # shape=(15, 15, 9)
func_1197_call = mod.get_global_var('func_1197')
func_1199_call = mutated_mod.get_global_var('func_1199')
var_1432 = relay.var("var_1432", dtype = "float32", shape = (32,))#candidate|1432|(32,)|var|float32
call_1431 = relay.TupleGetItem(func_1197_call(relay.reshape(var_1432.astype('float32'), [1, 2, 16])), 0)
call_1433 = relay.TupleGetItem(func_1199_call(relay.reshape(var_1432.astype('float32'), [1, 2, 16])), 0)
output = relay.Tuple([bop_1425,call_1431,var_1432,])
output2 = relay.Tuple([bop_1425,call_1433,var_1432,])
func_1436 = relay.Function([var_1423,var_1424,var_1432,], output)
mod['func_1436'] = func_1436
mod = relay.transform.InferType()(mod)
mutated_mod['func_1436'] = func_1436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1436_call = mutated_mod.get_global_var('func_1436')
var_1438 = relay.var("var_1438", dtype = "float64", shape = (1, 15, 9))#candidate|1438|(1, 15, 9)|var|float64
var_1439 = relay.var("var_1439", dtype = "float64", shape = (15, 15, 9))#candidate|1439|(15, 15, 9)|var|float64
var_1440 = relay.var("var_1440", dtype = "float32", shape = (32,))#candidate|1440|(32,)|var|float32
call_1437 = func_1436_call(var_1438,var_1439,var_1440,)
output = call_1437
func_1441 = relay.Function([var_1438,var_1439,var_1440,], output)
mutated_mod['func_1441'] = func_1441
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1466 = relay.const([[[-2.819610,-8.137681,-4.603194,9.683503,5.008321],[-0.942239,6.460419,-4.738157,-0.690338,7.818194],[-8.558836,2.164532,4.273081,3.111030,-1.304112],[6.510938,-1.977760,-3.938514,-7.634845,5.653710],[5.210204,2.412565,-8.415248,-9.989054,0.769889],[-4.518028,0.244001,7.597322,3.000586,4.778904]],[[3.362974,9.496224,2.668068,-1.283262,6.787682],[4.042951,-1.864376,6.324707,-6.271181,6.289834],[4.207116,7.002965,7.514686,8.236695,7.954849],[-5.076647,-1.369186,-0.701627,-7.872311,1.767437],[-4.762942,-2.251573,5.067945,2.521498,7.496475],[-3.824121,3.488721,0.070873,-2.213674,7.852041]],[[-1.203926,-2.644414,3.710517,-9.234157,-6.034927],[-4.689117,-9.721609,9.409804,-4.321720,5.289339],[9.707811,8.563661,8.597905,3.762009,8.259041],[9.894542,-8.293351,-7.731531,-0.860991,8.459011],[3.947967,8.536546,-5.991838,7.300252,-0.751456],[-8.275084,-0.560702,-3.328171,0.270897,3.840532]],[[-7.377802,-4.518795,8.841713,9.115380,4.348367],[-5.978289,-4.059841,-2.534088,-5.499591,9.515184],[-6.006694,-0.251174,2.354378,-6.749470,-7.826831],[-7.543782,-5.265899,0.453855,5.200416,2.352597],[-0.187586,2.877069,0.275278,2.805968,-3.576325],[-6.696692,6.922272,8.827063,1.532642,8.667360]],[[-3.893832,3.816818,-5.709660,-6.033941,1.258867],[-9.162028,2.297273,-9.958387,6.908602,-0.309552],[-8.426243,-2.633521,1.305108,8.427400,9.641158],[-3.203807,-7.081123,-4.912964,-1.393218,-3.193949],[-6.332808,3.788711,6.838164,-7.201772,-4.310978],[-7.601441,-2.124357,-7.694518,-0.845527,-0.074843]],[[-6.338812,6.549768,-5.660460,6.842989,-6.750051],[-4.793720,-0.915486,-6.326561,1.210110,-0.647481],[3.434024,3.485605,5.497161,3.435737,6.669513],[7.650913,-1.894413,-4.445559,-0.464860,-0.994904],[5.012229,0.097398,-0.153376,3.521203,-1.489511],[2.820224,-7.241411,1.012962,-3.978667,-0.515298]],[[8.562628,2.117845,-7.833615,-6.368233,6.555061],[-6.205510,-6.767514,-9.244601,5.222249,-1.325789],[6.316315,-5.079264,-3.860660,1.099155,-2.668726],[-5.595780,0.256444,-7.453221,4.961680,-6.228504],[8.358691,-4.199129,-6.829983,-8.041604,-6.315081],[-8.386744,6.317184,-8.517384,-5.011744,-0.935429]],[[0.030334,-1.064868,1.077793,-5.895904,-5.347950],[0.660631,5.891171,6.076176,9.507689,-2.322330],[-9.370474,4.898364,0.707753,-1.014021,-4.108471],[-8.781670,2.110160,-4.747687,5.552245,-5.616844],[-1.945244,7.076503,8.430674,9.819844,6.627517],[-6.930650,-3.799463,3.723859,0.302303,-1.587301]],[[-8.828697,0.896725,4.873316,-2.120623,1.128187],[-5.376151,2.771796,9.797546,-5.137272,5.634227],[-4.109833,-7.448834,9.502317,-1.245175,7.169651],[-0.333941,-3.685149,4.846486,-6.642054,-1.910835],[-2.712142,5.107038,2.327111,-7.063056,7.562561],[2.530274,-0.854720,3.653343,1.472953,-1.483945]],[[-9.021506,-2.292582,9.386447,-2.724901,-4.269138],[6.601680,-2.588289,-7.000508,4.614811,2.427111],[-6.173159,8.988884,-9.027624,-2.693303,-9.906507],[-6.101063,-1.409485,4.690431,7.409836,3.842490],[3.330199,-9.517686,2.419723,3.846005,-0.423419],[0.767667,9.940527,7.400469,9.586951,0.449175]]], dtype = "float64")#candidate|1466|(10, 6, 5)|const|float64
var_1467 = relay.var("var_1467", dtype = "float64", shape = (10, 6, 5))#candidate|1467|(10, 6, 5)|var|float64
bop_1468 = relay.power(const_1466.astype('float64'), relay.reshape(var_1467.astype('float64'), relay.shape_of(const_1466))) # shape=(10, 6, 5)
output = bop_1468
output2 = bop_1468
func_1472 = relay.Function([var_1467,], output)
mod['func_1472'] = func_1472
mod = relay.transform.InferType()(mod)
mutated_mod['func_1472'] = func_1472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1473 = relay.var("var_1473", dtype = "float64", shape = (10, 6, 5))#candidate|1473|(10, 6, 5)|var|float64
func_1472_call = mutated_mod.get_global_var('func_1472')
call_1474 = func_1472_call(var_1473)
output = call_1474
func_1475 = relay.Function([var_1473], output)
mutated_mod['func_1475'] = func_1475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_1526 = relay.TupleGetItem(func_909_call(), 2)
call_1527 = relay.TupleGetItem(func_910_call(), 2)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_1537 = func_876_call()
call_1538 = func_876_call()
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_1541 = relay.TupleGetItem(func_252_call(), 3)
call_1542 = relay.TupleGetItem(func_254_call(), 3)
output = relay.Tuple([call_1526,call_1537,call_1541,])
output2 = relay.Tuple([call_1527,call_1538,call_1542,])
func_1544 = relay.Function([], output)
mod['func_1544'] = func_1544
mod = relay.transform.InferType()(mod)
mutated_mod['func_1544'] = func_1544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mutated_mod.get_global_var('func_1544')
call_1545 = func_1544_call()
output = call_1545
func_1546 = relay.Function([], output)
mutated_mod['func_1546'] = func_1546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mod.get_global_var('func_1544')
func_1546_call = mutated_mod.get_global_var('func_1546')
call_1553 = relay.TupleGetItem(func_1544_call(), 1)
call_1554 = relay.TupleGetItem(func_1546_call(), 1)
output = relay.Tuple([call_1553,])
output2 = relay.Tuple([call_1554,])
func_1558 = relay.Function([], output)
mod['func_1558'] = func_1558
mod = relay.transform.InferType()(mod)
output = func_1558()
func_1559 = relay.Function([], output)
mutated_mod['func_1559'] = func_1559
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1591 = relay.const([[[0.385411,1.867687,3.809180,0.963357,-5.043509,-2.367727,9.411649,-6.600526,-1.339221,-9.908175,1.660314],[-8.323118,7.199896,3.861337,1.335268,-1.000079,-0.874402,8.122115,-4.834295,-1.955035,9.778150,1.230022],[-5.480078,-0.605476,-7.380959,9.335611,7.408005,-8.693460,7.119395,2.716126,-2.052240,-2.361266,6.620855]],[[-0.279296,-3.340389,2.735624,9.930248,-0.867673,-4.015018,-1.995117,-7.561974,7.685654,-4.144906,-7.166786],[0.697887,-4.923939,9.361781,-3.568359,5.918424,-6.540920,1.969194,8.868244,-3.141870,-0.669057,-5.166478],[-7.019314,-4.632946,-2.665850,1.430970,4.542758,6.984566,-9.073115,-2.322370,1.723797,3.337637,0.104684]],[[9.142894,6.807052,-1.600115,4.881403,3.154358,9.097936,3.435254,-0.910426,4.694401,5.131856,1.770232],[9.771394,2.824327,4.840043,7.788033,2.180097,0.504909,-5.599756,6.228920,-8.595505,8.925109,-3.560495],[-9.334085,7.359380,-4.433817,-1.856724,-7.329324,7.298304,-8.886926,-0.166442,4.019563,0.370239,4.315317]],[[9.559572,5.086585,8.913157,9.533578,3.263665,-2.708321,2.536383,7.951726,-3.102600,-7.003486,6.235401],[9.799615,-5.413406,-1.477344,7.747455,0.294920,-7.855557,7.832166,-0.931810,8.908762,-2.605046,-1.361080],[0.855508,2.967485,-4.372917,4.079094,-3.069181,3.863635,-0.209567,-1.471203,2.990925,-9.167641,-2.549733]],[[0.003922,-7.632802,-0.414807,-2.873244,1.053270,7.456189,-6.597192,-9.432472,7.059470,-0.406660,7.193950],[-1.689476,-2.458575,5.879198,4.055304,-9.447074,-3.137220,-8.681051,7.290997,-6.101093,-6.473349,4.206046],[6.989590,-5.290508,5.299784,2.943723,0.557391,-1.317134,-3.675607,-2.237063,-4.589993,-8.778004,-9.346904]],[[4.807033,-9.356393,-2.813065,2.538203,4.521331,0.783292,-7.518524,-5.697278,0.066732,4.524248,1.433652],[3.346521,-2.279947,0.857152,9.684351,9.864922,9.680619,-5.786988,-3.026864,-5.597887,-3.636831,1.421679],[-5.036878,-3.806173,-9.697929,9.907470,5.219158,7.427686,-4.043842,3.090183,-9.760265,2.206797,-3.584578]],[[6.997910,9.608282,-4.321454,3.365129,-9.131695,5.781470,1.836075,5.356455,4.889735,-4.692781,-9.284289],[9.050711,-9.735147,-6.228039,-7.868359,1.093574,6.589230,1.802834,-1.058375,3.924590,-0.768095,2.602188],[-3.368754,-2.734566,-2.204196,0.700447,-2.517327,-5.816121,-5.989839,-2.663413,2.539355,1.893999,-9.031865]],[[-8.846259,5.301701,-8.538453,-2.703332,-1.417281,-9.778990,-5.717165,2.230007,8.120725,5.299465,-5.376228],[-6.683341,-3.891107,-7.669903,-2.369573,-6.500079,7.872539,-4.554247,5.858817,8.044317,-0.875705,-1.804429],[-0.463642,-8.258705,6.327440,4.898791,7.924984,-2.426759,7.397157,2.719341,-2.007709,-7.890198,-4.231698]],[[5.426754,2.197761,6.445812,-5.299515,3.162617,4.312280,-7.729716,9.013599,-5.187727,5.165037,-1.909366],[0.961143,-0.542309,0.441485,6.310267,2.568241,7.643540,6.137890,-8.002045,-0.144677,1.791129,7.075951],[6.569223,9.332930,-1.631082,-1.357727,-2.085617,-4.665141,1.223097,4.072718,9.700790,6.785843,-8.193238]],[[2.880787,-8.988911,-2.642709,8.280695,8.965156,-8.793768,-9.566069,6.307729,6.301306,-8.041365,-2.314813],[8.104850,-0.488460,5.092854,9.161550,2.671755,-0.157027,-9.810175,8.923693,4.206828,-1.675861,3.997442],[-1.435250,-5.344274,-6.973685,2.977559,-5.848555,6.427051,-6.931849,1.815883,-9.777992,-3.873431,-0.286320]],[[9.352304,2.652108,3.677970,-4.680250,-3.232096,6.054441,-8.561612,-2.304033,1.582876,-2.264982,5.713947],[8.318491,-2.159868,1.548382,-7.292618,9.500171,3.019302,-0.805395,5.226267,-0.939683,2.109831,-8.918392],[5.042796,-4.624765,8.478437,5.725866,0.887292,1.910788,-0.203948,-4.321878,6.697164,-8.041521,-0.195199]],[[0.434447,2.699454,-3.616148,3.964339,-0.772765,4.500447,5.878449,1.756091,6.779477,8.585453,-8.570044],[-7.032478,0.692049,7.957348,-0.946205,-6.306707,3.608326,7.295486,9.345029,-6.365947,-8.395848,-0.761607],[-8.804285,-3.808308,-0.925175,4.136906,-1.689200,2.321646,1.192395,0.134290,0.995679,0.267684,-4.239053]],[[-1.855834,6.834126,2.862178,-2.856742,-7.930503,-3.730215,-0.498252,-3.146826,6.331313,5.159865,-8.507590],[0.197731,6.835925,-1.799607,3.318805,1.893991,-8.791125,-1.981616,-7.994938,0.115574,-3.129747,-2.986882],[-2.932761,-7.994167,3.277611,-0.886009,-8.596610,6.400191,-0.286423,-1.890137,-1.258660,8.910834,-0.212430]],[[2.621631,-2.633227,2.462556,-0.259674,-3.263880,6.559872,-6.208249,-3.412571,-7.569851,5.504773,-3.881361],[3.709837,2.910477,2.503327,-3.784310,3.791633,-4.386709,-2.588121,-7.559127,3.557481,4.472188,5.543444],[2.866603,8.717087,-8.095958,-0.906813,-8.031732,5.559247,4.723899,7.383468,-5.299504,1.124445,-1.835208]]], dtype = "float32")#candidate|1591|(14, 3, 11)|const|float32
uop_1592 = relay.asin(const_1591.astype('float32')) # shape=(14, 3, 11)
func_1083_call = mod.get_global_var('func_1083')
func_1084_call = mutated_mod.get_global_var('func_1084')
call_1596 = relay.TupleGetItem(func_1083_call(), 1)
call_1597 = relay.TupleGetItem(func_1084_call(), 1)
uop_1605 = relay.exp(uop_1592.astype('float32')) # shape=(14, 3, 11)
bop_1616 = relay.divide(uop_1592.astype('float64'), relay.reshape(uop_1605.astype('float64'), relay.shape_of(uop_1592))) # shape=(14, 3, 11)
func_1558_call = mod.get_global_var('func_1558')
func_1559_call = mutated_mod.get_global_var('func_1559')
call_1623 = relay.TupleGetItem(func_1558_call(), 0)
call_1624 = relay.TupleGetItem(func_1559_call(), 0)
func_1544_call = mod.get_global_var('func_1544')
func_1546_call = mutated_mod.get_global_var('func_1546')
call_1628 = relay.TupleGetItem(func_1544_call(), 1)
call_1629 = relay.TupleGetItem(func_1546_call(), 1)
output = relay.Tuple([call_1596,bop_1616,call_1623,call_1628,])
output2 = relay.Tuple([call_1597,bop_1616,call_1624,call_1629,])
func_1631 = relay.Function([], output)
mod['func_1631'] = func_1631
mod = relay.transform.InferType()(mod)
output = func_1631()
func_1632 = relay.Function([], output)
mutated_mod['func_1632'] = func_1632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1631_call = mod.get_global_var('func_1631')
func_1632_call = mutated_mod.get_global_var('func_1632')
call_1638 = relay.TupleGetItem(func_1631_call(), 2)
call_1639 = relay.TupleGetItem(func_1632_call(), 2)
uop_1665 = relay.tan(call_1638.astype('float32')) # shape=(10, 9, 14)
uop_1667 = relay.tan(call_1639.astype('float32')) # shape=(10, 9, 14)
func_730_call = mod.get_global_var('func_730')
func_731_call = mutated_mod.get_global_var('func_731')
call_1684 = relay.TupleGetItem(func_730_call(), 0)
call_1685 = relay.TupleGetItem(func_731_call(), 0)
output = relay.Tuple([uop_1665,call_1684,])
output2 = relay.Tuple([uop_1667,call_1685,])
func_1687 = relay.Function([], output)
mod['func_1687'] = func_1687
mod = relay.transform.InferType()(mod)
output = func_1687()
func_1688 = relay.Function([], output)
mutated_mod['func_1688'] = func_1688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_1689 = relay.TupleGetItem(func_909_call(), 3)
call_1690 = relay.TupleGetItem(func_910_call(), 3)
func_1472_call = mod.get_global_var('func_1472')
func_1475_call = mutated_mod.get_global_var('func_1475')
var_1705 = relay.var("var_1705", dtype = "float64", shape = (300,))#candidate|1705|(300,)|var|float64
call_1704 = func_1472_call(relay.reshape(var_1705.astype('float64'), [10, 6, 5]))
call_1706 = func_1472_call(relay.reshape(var_1705.astype('float64'), [10, 6, 5]))
func_513_call = mod.get_global_var('func_513')
func_516_call = mutated_mod.get_global_var('func_516')
const_1730 = relay.const(5, dtype = "int8")#candidate|1730|()|const|int8
var_1731 = relay.var("var_1731", dtype = "int8", shape = (1, 351))#candidate|1731|(1, 351)|var|int8
call_1729 = func_513_call(relay.reshape(const_1730.astype('int8'), []), relay.reshape(var_1731.astype('int8'), [13, 9, 3]), )
call_1732 = func_513_call(relay.reshape(const_1730.astype('int8'), []), relay.reshape(var_1731.astype('int8'), [13, 9, 3]), )
func_1083_call = mod.get_global_var('func_1083')
func_1084_call = mutated_mod.get_global_var('func_1084')
call_1733 = relay.TupleGetItem(func_1083_call(), 0)
call_1734 = relay.TupleGetItem(func_1084_call(), 0)
output = relay.Tuple([call_1689,call_1704,var_1705,call_1729,const_1730,var_1731,call_1733,])
output2 = relay.Tuple([call_1690,call_1706,var_1705,call_1732,const_1730,var_1731,call_1734,])
func_1738 = relay.Function([var_1705,var_1731,], output)
mod['func_1738'] = func_1738
mod = relay.transform.InferType()(mod)
mutated_mod['func_1738'] = func_1738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1738_call = mutated_mod.get_global_var('func_1738')
var_1740 = relay.var("var_1740", dtype = "float64", shape = (300,))#candidate|1740|(300,)|var|float64
var_1741 = relay.var("var_1741", dtype = "int8", shape = (1, 351))#candidate|1741|(1, 351)|var|int8
call_1739 = func_1738_call(var_1740,var_1741,)
output = call_1739
func_1742 = relay.Function([var_1740,var_1741,], output)
mutated_mod['func_1742'] = func_1742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1631_call = mod.get_global_var('func_1631')
func_1632_call = mutated_mod.get_global_var('func_1632')
call_1803 = relay.TupleGetItem(func_1631_call(), 1)
call_1804 = relay.TupleGetItem(func_1632_call(), 1)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_1826 = relay.TupleGetItem(func_909_call(), 2)
call_1827 = relay.TupleGetItem(func_910_call(), 2)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_1831 = relay.TupleGetItem(func_909_call(), 3)
call_1832 = relay.TupleGetItem(func_910_call(), 3)
func_315_call = mod.get_global_var('func_315')
func_317_call = mutated_mod.get_global_var('func_317')
var_1840 = relay.var("var_1840", dtype = "float32", shape = (10, 96))#candidate|1840|(10, 96)|var|float32
call_1839 = func_315_call(relay.reshape(var_1840.astype('float32'), [16, 5, 12]))
call_1841 = func_315_call(relay.reshape(var_1840.astype('float32'), [16, 5, 12]))
bop_1844 = relay.mod(call_1826.astype('float64'), relay.reshape(call_1831.astype('float64'), relay.shape_of(call_1826))) # shape=(4, 14, 10)
bop_1847 = relay.mod(call_1827.astype('float64'), relay.reshape(call_1832.astype('float64'), relay.shape_of(call_1827))) # shape=(4, 14, 10)
func_689_call = mod.get_global_var('func_689')
func_691_call = mutated_mod.get_global_var('func_691')
const_1853 = relay.const([4.969170,-9.459528,-0.974636,-6.607222,-4.288143,6.170359,-7.078006,0.705338,8.456455,2.607449,0.957676,1.460113,-1.523126,9.726336,-1.557988,-0.671531,-7.485127,0.884752,-3.804349,-6.195041,8.874155,-4.646128,9.560980,-4.926692,-2.691624,4.523826,7.226520,-2.255338,1.848184,7.371976,-8.928369,8.870728,-8.307989,0.292649,-4.481637,3.506694,5.186791,5.924657,9.713824,6.034285,-7.784142,-0.603970,4.694021,2.830474,-3.838619,-8.865956,-9.915364,5.225761,1.079755,1.097385,-4.352084,0.055812,-6.319324,-8.831469,-6.244658,-5.564285,-6.237576,-0.544634,5.144765,-1.637325,-6.827638,-0.149510,4.015214,7.217151,-6.676180,-4.182355,-9.454175,-7.039724,6.573244,-3.253548,-2.987461,-9.190771,2.322226,-2.070699,-5.586505,-8.424036,6.946050,8.813824,-2.962756,2.817799,9.910045,-9.563030,1.121786,4.051638,8.126510,4.326460,-5.450170,4.494269,-2.913854,-7.481769,-5.233797,-9.299810,3.349238,-0.752791,-2.711332,-5.279493,-0.945114,2.818566,8.976868,-8.062583,2.796060,-7.176939,5.546562,7.341574,5.801258,-9.576071,9.891049,8.443248,-9.971864,-3.501008,-1.143842,-1.087806,9.405904,-5.412438,-4.213078,-9.040604,-9.902587,8.223699,-6.969278,-3.272925,-4.369377,7.281575,2.506813,-9.746208,4.190265,-7.152219], dtype = "float32")#candidate|1853|(126,)|const|float32
call_1852 = relay.TupleGetItem(func_689_call(relay.reshape(const_1853.astype('float32'), [14, 1, 9])), 0)
call_1854 = relay.TupleGetItem(func_691_call(relay.reshape(const_1853.astype('float32'), [14, 1, 9])), 0)
func_513_call = mod.get_global_var('func_513')
func_516_call = mutated_mod.get_global_var('func_516')
const_1869 = relay.const(1, dtype = "int8")#candidate|1869|()|const|int8
var_1870 = relay.var("var_1870", dtype = "int8", shape = (351,))#candidate|1870|(351,)|var|int8
call_1868 = func_513_call(relay.reshape(const_1869.astype('int8'), []), relay.reshape(var_1870.astype('int8'), [13, 9, 3]), )
call_1871 = func_513_call(relay.reshape(const_1869.astype('int8'), []), relay.reshape(var_1870.astype('int8'), [13, 9, 3]), )
uop_1872 = relay.log(call_1826.astype('float64')) # shape=(4, 14, 10)
uop_1874 = relay.log(call_1827.astype('float64')) # shape=(4, 14, 10)
output = relay.Tuple([call_1803,call_1839,var_1840,bop_1844,call_1852,const_1853,call_1868,const_1869,var_1870,uop_1872,])
output2 = relay.Tuple([call_1804,call_1841,var_1840,bop_1847,call_1854,const_1853,call_1871,const_1869,var_1870,uop_1874,])
func_1887 = relay.Function([var_1840,var_1870,], output)
mod['func_1887'] = func_1887
mod = relay.transform.InferType()(mod)
mutated_mod['func_1887'] = func_1887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1887_call = mutated_mod.get_global_var('func_1887')
var_1889 = relay.var("var_1889", dtype = "float32", shape = (10, 96))#candidate|1889|(10, 96)|var|float32
var_1890 = relay.var("var_1890", dtype = "int8", shape = (351,))#candidate|1890|(351,)|var|int8
call_1888 = func_1887_call(var_1889,var_1890,)
output = call_1888
func_1891 = relay.Function([var_1889,var_1890,], output)
mutated_mod['func_1891'] = func_1891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_1930 = relay.TupleGetItem(func_252_call(), 0)
call_1931 = relay.TupleGetItem(func_254_call(), 0)
uop_1945 = relay.log(call_1930.astype('float64')) # shape=(10, 9, 14)
uop_1947 = relay.log(call_1931.astype('float64')) # shape=(10, 9, 14)
output = uop_1945
output2 = uop_1947
func_1951 = relay.Function([], output)
mod['func_1951'] = func_1951
mod = relay.transform.InferType()(mod)
output = func_1951()
func_1952 = relay.Function([], output)
mutated_mod['func_1952'] = func_1952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_730_call = mod.get_global_var('func_730')
func_731_call = mutated_mod.get_global_var('func_731')
call_1964 = relay.TupleGetItem(func_730_call(), 0)
call_1965 = relay.TupleGetItem(func_731_call(), 0)
uop_1974 = relay.acos(call_1964.astype('float32')) # shape=(10, 9, 14)
uop_1976 = relay.acos(call_1965.astype('float32')) # shape=(10, 9, 14)
output = relay.Tuple([uop_1974,])
output2 = relay.Tuple([uop_1976,])
func_1990 = relay.Function([], output)
mod['func_1990'] = func_1990
mod = relay.transform.InferType()(mod)
mutated_mod['func_1990'] = func_1990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1990_call = mutated_mod.get_global_var('func_1990')
call_1991 = func_1990_call()
output = call_1991
func_1992 = relay.Function([], output)
mutated_mod['func_1992'] = func_1992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1687_call = mod.get_global_var('func_1687')
func_1688_call = mutated_mod.get_global_var('func_1688')
call_2006 = relay.TupleGetItem(func_1687_call(), 1)
call_2007 = relay.TupleGetItem(func_1688_call(), 1)
var_2009 = relay.var("var_2009", dtype = "float32", shape = (10, 9, 14))#candidate|2009|(10, 9, 14)|var|float32
bop_2010 = relay.maximum(call_2006.astype('uint64'), relay.reshape(var_2009.astype('uint64'), relay.shape_of(call_2006))) # shape=(10, 9, 14)
bop_2013 = relay.maximum(call_2007.astype('uint64'), relay.reshape(var_2009.astype('uint64'), relay.shape_of(call_2007))) # shape=(10, 9, 14)
output = relay.Tuple([bop_2010,])
output2 = relay.Tuple([bop_2013,])
func_2022 = relay.Function([var_2009,], output)
mod['func_2022'] = func_2022
mod = relay.transform.InferType()(mod)
var_2023 = relay.var("var_2023", dtype = "float32", shape = (10, 9, 14))#candidate|2023|(10, 9, 14)|var|float32
output = func_2022(var_2023)
func_2024 = relay.Function([var_2023], output)
mutated_mod['func_2024'] = func_2024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_2037 = relay.TupleGetItem(func_909_call(), 1)
call_2038 = relay.TupleGetItem(func_910_call(), 1)
output = relay.Tuple([call_2037,])
output2 = relay.Tuple([call_2038,])
func_2041 = relay.Function([], output)
mod['func_2041'] = func_2041
mod = relay.transform.InferType()(mod)
output = func_2041()
func_2042 = relay.Function([], output)
mutated_mod['func_2042'] = func_2042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_2043 = relay.TupleGetItem(func_252_call(), 4)
call_2044 = relay.TupleGetItem(func_254_call(), 4)
func_2022_call = mod.get_global_var('func_2022')
func_2024_call = mutated_mod.get_global_var('func_2024')
const_2048 = relay.const([[1.832502,-9.797947,-4.214733,8.779058,-9.040191,5.064955,-0.095331,-2.307014,-9.107731,0.721423,8.422581,0.061712,-1.381579,0.651767,-3.912840,-3.576597,2.322471,-5.162395,-7.838302,-6.627678,-4.763963,-8.638726,-2.486137,-5.952158,-1.111796,4.800509,-1.018167,-9.470283,6.674325,4.815871,4.964536,-7.954888,-2.760589,-6.030630,-2.611685,-1.544232,-0.159015,3.056397,4.069785,4.762717,-5.906100,-7.645790,9.430135,6.841260,-1.322881,4.296578,-0.875473,-6.220263,-3.189631,-1.363200,1.552877,-9.744248,8.028285,6.541699,2.093507,-7.330310,9.857460,3.095077,0.642939,-7.143098,4.719585,9.161913,3.611413,0.833113,-6.147866,-7.371104,-8.000694,6.769094,-4.555964,-0.278303,-0.153314,5.390925,7.133234,-2.042610,-3.536492,-6.622550,-1.963777,2.896502,-2.111999,-2.629828,-1.785980,-7.598050,9.221776,7.252080,-4.080195,0.043055,-4.925775,7.773086,1.724208,6.208459,-4.419911,-5.554461,9.139162,-8.818191,-5.919512,8.617043,4.220458,3.673834,5.571657,-8.330161,-1.549249,-6.915132,4.501803,5.913342,-7.514051,-2.452976,-1.976806,7.976846,-4.048563,4.262241,-7.566307,-4.581367,6.988624,-0.051303,-7.311438,-3.453275,5.630683,1.079290,-4.265395,8.984728,9.868773,2.933112,-6.007835,-7.965846,-3.869981,7.794103,-6.972432,-9.805514,9.026349,-7.009056,-0.486622,0.700851,-0.043498,-1.221736,9.873476,4.636795,4.449504,-5.350660,7.824668,-8.893194,2.504007,5.158075,4.384999,2.858844,-9.997513,-5.133802,-5.903321,-2.367797,6.138126,-5.336027,6.818917,1.422804,-7.775164,-6.899681,-6.184348,-5.691329,9.131932,8.399776,4.912196,8.346293,9.752260,-7.301872,6.988962,-7.749952,5.402178,3.163152,-2.664414,7.708267,6.244790,-0.164202,6.047410,9.554806,-9.454139,4.756532,9.631875,-4.097900,4.766150,-1.429515,4.053870,2.658755,9.771415,9.050438,7.114502,3.135599,7.735228,0.928809,-9.756226,5.958472,4.313278,-5.218001,2.826646,5.509915,-3.908126,-3.813360,-5.580842,-0.316696,-8.188580,9.455996,2.644643,-5.598529,9.079712,0.428271,-5.203933,-1.129708,7.417557,-2.737586,4.150124,8.706478,-5.360826,-1.229184,6.555374,-5.722950,-4.329204,-5.516500,-3.314591,-3.544437,-9.164400,0.794330,-5.842452,-6.758328,5.356997,3.288453,6.475966,-8.086708,-3.296081,-7.685587,3.790422,2.120887,4.371752,3.014314,9.590612,4.599180,2.103024,-1.432430,-1.700100,-3.593198,-6.843711,5.682015,-5.755118,9.651261,-7.253552,8.316755,-7.198016,6.472375,-1.711440,-1.806707,9.446320,3.303817,-6.885520,-3.471468,-2.230962,-7.831764,-0.560647,-7.770120,9.083665,0.760682,-6.858515,-1.430348,-1.903830,-2.270394,-7.422664,-7.205302,-3.834530,7.279990,5.611717,6.986860,-0.404894,-7.344623,1.391356,7.027110,-9.108391,-1.198767,8.912615,-6.741369,8.779094,-2.245084,6.752984,7.698900,-2.068320,-7.416289,-1.311569,-0.339632,-3.781237,-7.701770,9.977056,-8.249360,-2.212573,-9.587755,1.106060,1.928441,5.339729,2.780522,-8.370706,-5.936754,8.932025,0.281778,7.747620,-3.097651,-4.877373,8.575237,-7.650251,-7.218288,3.805041,6.208415,8.975981,4.794593,-3.549817,0.912760,2.517443,-0.257736,-4.466952,-1.501614,0.149437,3.502266,3.968401,4.613160,6.235536,6.440949,1.598548,1.277592,9.103371,6.799211,8.336488,4.951773,9.372117,4.898011,6.447671,8.596360,-1.366756,-9.309732,6.987653,-8.937959,7.896601,2.574366,-5.234827,4.751874,3.990766,9.039460,1.953635,2.163048,-2.749381,0.874570,6.429624,-2.142484,8.051690,0.410315,6.265905,4.974136,2.818223,4.579237,-5.184505,-8.003342,2.951250,-1.927721,-4.182109,9.923318,1.228445,-6.187752,3.499530,-4.958928,7.846368,-0.312744,8.521679,-1.471564,-8.797417,-6.908882,-0.278415,0.864452,6.087206,5.733321,1.341177,-2.283434,0.557853,5.725032,-8.956773,8.743777,-3.698973,-5.546399,-5.448004,-5.261818,-6.550038,4.706210,9.293836,-0.730828,-2.786017,-9.071795,0.157046,-2.141151,1.844178,3.015644,-0.064043,-1.300324,-1.177100,-3.585124,8.761892,-9.979585,-5.939920,-5.618046,-3.614031,-3.648787,-9.708279,-8.463183,2.496920,-8.394879,3.871828,-7.368035,3.149337,-8.368613,8.740364,-4.315613,5.238608,-0.314360,-8.581546,-2.613489,-1.661777,6.540493,4.275057,-1.785462,7.699089,-5.668532,-5.940055,-3.367621,3.751486,-2.640209,3.709568,8.404766,1.535081,-2.704319,-4.013010,-8.680536,6.384067,-6.334930,1.972722,-3.489236,3.723794,9.456355,7.140854,0.128835,-0.972799,-0.063740,-5.264717,3.982287,5.346476,5.319379,-2.845126,-7.707573,-8.867160,-4.306232,7.194936,-5.912557,1.606368,2.620689,9.532039,9.087650,-3.912577,8.420457,2.450504,-4.195407,2.341845,6.583896,7.068368,6.571153,-2.050524,3.850994,-3.828733,-3.505972,-1.273335,4.542420,8.403891,3.970543,-6.093097,-3.897029,1.571889,-7.249581,7.028108,-6.599559,-8.255838,-8.492813,-6.600423,-4.971655,9.957847,-7.471047,-5.819397,4.646026,5.761410,7.819350,7.235784,5.359789,-1.884903,7.991213,9.414380,-9.487800,-6.695985,-0.348829,9.823748,1.121591,-2.805453,-2.396708,0.712709,-1.207905,-9.744742,-2.874631,1.399316,8.112398,-3.753798,0.301382,-7.732753,1.807654,-9.670010,3.519159,-1.679273,-8.901093,3.046464,-5.816952,-7.786901,5.048973,-0.232935,8.534679,3.768275,-9.550129,3.522956,-2.965948,4.783147,-7.410724,8.261674,0.803504,1.182723,-8.111137,-1.492912,8.511437,7.743791,-6.502163,8.640984,-2.296366,-5.503414,-7.798249,-5.003902,8.528369,-5.672611,-3.471132,-4.198876,2.963368,1.913522,-6.099009,-6.932555,2.106131,-6.373421,-6.968476,0.196460,-7.391991,4.783674,3.621589,0.399225,1.366262,3.564167,-9.015099,-1.807920,7.889646,7.333117,4.822522,7.348733,-6.341421,-8.826399,1.800770,0.238411,7.076585,-0.341755,-9.465564,-3.825980,7.204340,0.884045,3.753091,-9.663060,-4.927705,-3.226904,8.149450,-6.729170,6.544864,-8.756078,-4.300654,-3.227933,-1.328855,-5.390856,9.182538,0.624691,-1.961624,-0.628242,-6.412503,-3.430937,-1.723636,-5.148002,6.394550,8.478218,-6.124457,5.399986,6.324872,-8.933620,5.757796,0.353478,5.512538,0.108396,1.284987,1.882761,-7.153384,-4.542995,-3.359090,4.034848,8.125116,-2.325248,-2.152832,-4.654950,-4.160950,-2.953661,-5.255251,-6.581433,-8.446948,7.956881,9.909433,4.248008,1.502454,-9.490974,-1.488055,1.123357,3.993656,3.643596,2.771401,2.664045,5.431063,5.148106,3.796953,7.452858,-8.734764,-1.203840,-2.904627,1.470241,4.607428,9.826297,4.490777,-8.093104,6.884795,5.820156,6.332394,-8.727537,-7.235052,-0.811569,3.320975,3.827237,2.512749,8.087938,6.576868,8.812010,-0.183391,-4.362858,1.263670,-9.397910,4.365982,1.170685,3.382989,2.453903,-7.942245,7.753216,8.576485,6.343649,-0.366011,-8.280799,9.902193,3.430991,6.904234,-7.394286,-2.800223,7.927300,-2.044470,-9.049495,-9.938960,3.606788,-5.203039,-1.339977,3.855811,-0.649642,-3.503672,9.162595,-2.570250,8.563611,-3.184667,-4.745179,1.115087,-2.119586,-2.957132,3.676606,-9.606218,0.285663,7.327993,6.948515,3.545506,9.591301,-4.380082,-7.654445,0.309616,-5.919137,9.401710,-9.063916,-4.754689,-5.345217,5.153310,6.369397,-1.045200,-4.838932,-8.535066,-1.196438,6.951567,5.823982,-2.162066,-8.435071,-8.158872,2.232707,0.341897,-8.993596,8.042208,0.881797,-9.875212,-1.894300,1.592687,-3.081297,-1.330475,-7.318771,-2.953234,-3.946410,1.830565,-7.045773,2.961904,5.748147,3.828195,3.058617,-1.378819,-8.105943,9.935506,1.838603,1.517510,7.774898,-1.758240,-3.982792,6.422862,2.824798,7.236572,-2.464402,7.810725,-0.318895,2.728714,2.692930,-8.337932,-8.967713,6.598344,-8.244751,-6.786370,-1.324822,0.657797,1.308231,2.421840,3.656566,4.631126,-0.649668,5.311056,5.846023,-2.868477,-0.717867,-8.753983,-0.846748,-3.558578,2.776574,-9.542503,0.066715,-7.363197,3.169982,1.267897,-6.499150,-5.808850,-5.413463,2.094016,7.067167,-7.372728,-4.100527,-8.501919,-6.531691,-2.155847,9.440892,-7.308038,-3.137815,-7.051502,-0.020879,1.754218,-9.888717,8.646997,7.188022,-5.478413,-3.086290,9.576679,-1.691006,-3.151852,-5.440528,-3.420935,1.791315,1.576117,3.738667,2.809857,8.067946,-2.627759,7.527332,-9.560630,2.314143,6.523012,-6.109173,-8.350811,-5.260413,3.615900,2.586660,5.797396,-3.451735,5.653501,-5.163206,-0.882653,4.796147,2.151531,-5.038010,3.119294,-4.370884,-6.079382,2.680433,6.666908,4.226806,9.706545,-4.065228,3.463986,8.914622,-9.171869,-2.785401,9.774091,-4.545723,-7.002959,8.169798,-6.039875,-8.111110,-5.885057,3.574430,2.575697,-9.507009,-9.429443,5.886547,-0.743858,-0.126903,-8.463830,2.746325,-1.945332,-1.756099,-0.304799,-3.726786,-9.278604,2.941408,0.640574,-3.477458,4.282071,0.731313,-8.389666,-6.305053,2.930953,0.272544,9.295493,2.281411,-5.631650,-7.188085,2.221510,0.706071,6.324540,-4.490486,-7.729866,3.011499,-3.071576,1.837707,-7.054257,3.029029,-8.179173,9.977068,8.781157,1.720660,4.255642,-1.803958,-8.362209,-7.899736,9.487004,-8.571376,8.928584,7.342364,-5.458593,-5.736327,-4.604934,-5.188094,4.066836,-3.715610,7.035917,-9.208116,1.081722,0.035849,8.632565,4.632628,6.925881,-5.533288,-5.324361,-5.143123,-3.747946,4.861848,-8.363359,1.521092,9.249613,-6.459752,3.715826,8.813362,7.842868,-5.350766,-8.323161,2.812069,-3.312529,5.566263,-4.392156,3.465143,-4.450646,2.567606,7.277120,-2.329060,0.508674,6.351603,-6.899221,1.769978,6.002757,-0.307084,-7.725969,3.232214,0.482098,8.347693,-2.931482,-2.953189,6.753390,9.886490,-4.578089,0.639968,-1.830983,-3.525277,-2.008283,2.820398,7.200229,0.527890,0.669972,-0.267657,1.503401,-1.446784,9.976008,1.719656,6.577497,9.322245,-7.576092,8.254977,0.392227,7.669203,6.424468,0.748111,-3.992291,-2.049185,-0.369874,-4.830717,-5.187215,0.219476,9.522556,-0.362389,-7.105385,-1.604195,3.799233,2.754160,7.436007,-0.356906,6.689510,-0.732278,-1.673645,-5.808539,0.079584,0.947753,7.016660,9.619089,0.134239,4.379516,1.021721,-4.328641,0.860532,0.359711,3.928566,-8.502019,-5.982772,-3.621939,8.928130,2.748514,-9.924335,8.056562,8.666384,-4.026783,-4.323005,-1.011009,-5.063085,-1.720672,3.510965,-5.277892,1.579846,2.286840,4.337993,8.026096,-4.134729,-6.877458,0.744947,5.748943,-5.165608,5.273286,5.084029,2.966275,-3.739916,-8.875714,1.037186,-8.562568,5.380196,-6.511033,-8.893506,0.775160,-5.991622,4.978952,6.315978,8.742440,-9.767144,4.793278,-7.393737,0.911031,-4.692571,-1.709597,4.007823,4.123966,2.379552,5.847167,2.518951,-8.229213,-3.852351,1.702587,-4.726019,-6.854028,9.133596,8.796196,-0.797027,-7.142106,-1.265885,-3.003175,-8.169022,-2.229982,-2.710272,7.363574,-8.796016,3.513711,8.016169,8.609405,6.742525,-8.245547,2.167189,5.912332,1.943206,-8.009909,-9.905166,6.374654,-2.642055,-0.548264,5.354159,-0.319112,-3.860092,0.730714,-2.163166,3.792146,-2.790060,-4.140619,2.156921,2.142072,-2.938557,-2.331807,-0.695553,6.181159,2.419571,9.105051,2.606293,9.076908,-2.433818,1.841657,1.413728,-5.178068,-6.927513,6.046205,-0.854822,-1.062840,-0.811852,-8.373057,-8.985216,-2.480513,5.928605,9.904641,3.475960,-7.509371,6.105966,0.864902,9.458415,-0.489554,-9.257506,0.901539,-5.765071,5.428251,2.180693,5.578089,9.842927,9.742898,-0.628991,7.178184,5.716110,3.309083,5.057903,6.676724,-6.328811,5.072483,4.872072,-0.478685,-7.434801,6.580981,1.223817,-5.613083,-2.348950,2.452853,-0.663222,-9.124272,1.384929,-3.106573,-4.466380,3.990580,8.890779,-0.841035,7.300588,-4.561100,-4.598285,5.096970,-0.017199,1.692324,-0.815699,4.441376,5.662799,-9.688982,5.881515,-2.683471,1.289268,9.628708,-4.730325,7.091412,-8.261417,2.524629,2.746525,-0.544251,-9.353333,-3.971146,-2.859855,3.045242,-7.016407,-0.032098,-6.049317,5.008739,-0.615596,-0.324315,-2.740742,3.217461,2.251007,-6.845157,5.113971,3.467893,-5.627323,-3.240934,8.305799,-7.687591,-3.230269,-0.155372,1.888076,-4.024418,-9.627093,-8.646246,-4.327077,9.860466,7.324150,9.973014,-1.973842,-3.520570,-3.871102,1.699777,5.422442,7.673268,5.819592,-7.596107,-7.683100,-9.808270,-2.572553,0.191716,-6.057739,-4.009252,-5.213986,2.178462,-0.184160,0.695913,-1.112712,3.257239,8.128187,6.289469,-5.627957,2.986293,-5.332029,3.978959,4.097805,-9.491393,6.149007,7.102421,-9.548805,-8.673234,-2.295734,8.339905,-2.965675,-9.807011,-1.888241,-7.436797,-3.059812,9.682938,-5.221980,6.946407,3.765402,6.417950,-8.291445,5.756375,1.533508,-0.031656,0.760391,5.330311,-6.869666,2.503472,4.708934,7.993402,-3.471238,5.087640,8.089776,-6.854514,-6.848038,6.571905,-3.566651,1.489759,-4.481241,9.169376,5.783179,3.848510,3.805272,-8.331664,1.165771]], dtype = "float32")#candidate|2048|(1, 1260)|const|float32
call_2047 = relay.TupleGetItem(func_2022_call(relay.reshape(const_2048.astype('float32'), [10, 9, 14])), 0)
call_2049 = relay.TupleGetItem(func_2024_call(relay.reshape(const_2048.astype('float32'), [10, 9, 14])), 0)
output = relay.Tuple([call_2043,call_2047,const_2048,])
output2 = relay.Tuple([call_2044,call_2049,const_2048,])
func_2054 = relay.Function([], output)
mod['func_2054'] = func_2054
mod = relay.transform.InferType()(mod)
output = func_2054()
func_2055 = relay.Function([], output)
mutated_mod['func_2055'] = func_2055
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2086 = relay.var("var_2086", dtype = "float32", shape = (16, 1, 16))#candidate|2086|(16, 1, 16)|var|float32
uop_2087 = relay.sigmoid(var_2086.astype('float32')) # shape=(16, 1, 16)
output = relay.Tuple([uop_2087,])
output2 = relay.Tuple([uop_2087,])
func_2104 = relay.Function([var_2086,], output)
mod['func_2104'] = func_2104
mod = relay.transform.InferType()(mod)
var_2105 = relay.var("var_2105", dtype = "float32", shape = (16, 1, 16))#candidate|2105|(16, 1, 16)|var|float32
output = func_2104(var_2105)
func_2106 = relay.Function([var_2105], output)
mutated_mod['func_2106'] = func_2106
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2168 = relay.const([[[-1.091073,-5.541166,1.732866,8.801359,-6.908621,4.870505,-1.069566,-1.703079],[-1.107053,6.882269,7.203932,-5.194449,8.843686,0.428344,2.276960,1.630128],[-6.126262,-9.068460,1.668071,7.415801,0.664847,1.180169,-4.453717,-9.990686]],[[4.175381,4.953772,1.068567,-9.117268,8.887287,9.688328,-1.835685,-8.943178],[-1.906763,-7.309326,-9.433451,-7.577908,5.924065,-4.499523,2.646146,-8.568927],[-2.510026,7.895964,2.254640,-3.462472,-1.273919,6.306686,1.248048,0.248733]],[[-4.333018,8.534980,-8.569643,-6.294590,0.613382,1.115132,-1.482095,5.149270],[4.331691,-5.877865,3.777832,8.825152,-9.168429,-6.141025,-2.215786,-6.732347],[-7.334592,-9.138912,6.408992,-7.530343,6.911179,6.426050,8.956754,-9.248697]],[[8.928227,5.924751,-6.286217,-6.335276,7.178221,-2.751227,6.745822,7.044343],[-1.227753,-4.085329,-0.133596,-6.591120,-8.192474,8.558648,3.227353,-8.348607],[3.003843,7.749289,-2.255735,-5.803011,-3.362137,0.945410,5.823521,6.222096]],[[-4.778658,7.980378,-6.284954,-6.589394,4.243125,-1.912685,-5.471784,-7.150082],[-6.394833,3.143272,1.820460,3.722753,-0.951809,6.336072,8.034815,3.551439],[-0.139170,-8.106437,-0.154910,8.780278,7.843295,-0.325881,-3.538614,5.510063]],[[-3.477528,2.257250,-8.436330,-3.596692,-2.944232,9.159373,-9.057691,4.340350],[7.973599,-4.576446,5.018471,-8.770543,6.649521,-3.538569,2.555586,5.397376],[-4.475106,1.673078,3.058505,4.063943,-9.375897,0.593207,4.979166,2.047995]],[[-8.598887,-0.036130,-2.056635,-9.065140,-8.814767,1.108966,-7.361754,2.946233],[-2.037298,-7.311525,-2.018074,0.369134,-0.285080,-8.832240,5.503800,-3.395528],[6.515536,7.628050,0.629313,3.461019,-0.180032,6.781178,2.583199,6.475836]],[[-0.546996,2.126636,1.164746,8.854533,2.596244,3.953118,9.060311,9.958772],[1.486723,-1.673699,-0.047271,-6.560525,3.899368,-1.755207,-5.444513,-7.710462],[9.952661,-6.063495,-4.563084,-8.856538,0.800495,-1.878198,7.934272,5.366969]],[[2.309008,-2.818021,7.225822,-8.918146,-1.358949,-0.084164,4.280346,5.889429],[-7.226240,8.435137,8.883711,4.675583,-5.083253,-1.489423,0.519940,-1.574599],[0.655471,-3.155196,8.855979,5.204331,4.868127,-0.247871,-5.311105,6.007049]],[[3.326516,5.399952,-0.715520,9.927488,5.673960,3.832307,4.618857,4.716277],[-4.743658,-1.632095,-5.403936,7.537282,0.114222,-1.387836,-2.926972,-1.568852],[1.620236,-5.319513,-2.519567,-4.161435,5.184158,-6.649800,3.334893,-1.804918]],[[-2.194815,2.891134,-5.140405,-7.459015,-2.058537,-0.411340,4.038074,3.133878],[-4.343945,-3.681899,0.727510,-7.733525,-6.775785,-3.304156,-6.874597,1.827809],[2.392225,-6.405968,-6.395329,1.914205,6.977710,6.900503,-6.274606,4.023383]],[[-4.441520,-2.736958,-0.997267,3.130224,5.133100,-0.539040,-2.699428,-5.338762],[-9.970037,7.008825,-6.826106,-9.067788,-0.562103,-1.675974,-7.374502,-3.029684],[2.945860,-2.365090,4.772684,6.008337,2.520517,9.419032,6.552928,6.038895]]], dtype = "float32")#candidate|2168|(12, 3, 8)|const|float32
uop_2169 = relay.cosh(const_2168.astype('float32')) # shape=(12, 3, 8)
output = uop_2169
output2 = uop_2169
func_2184 = relay.Function([], output)
mod['func_2184'] = func_2184
mod = relay.transform.InferType()(mod)
output = func_2184()
func_2185 = relay.Function([], output)
mutated_mod['func_2185'] = func_2185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_2201 = func_876_call()
call_2202 = func_876_call()
output = relay.Tuple([call_2201,])
output2 = relay.Tuple([call_2202,])
func_2203 = relay.Function([], output)
mod['func_2203'] = func_2203
mod = relay.transform.InferType()(mod)
mutated_mod['func_2203'] = func_2203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2203_call = mutated_mod.get_global_var('func_2203')
call_2204 = func_2203_call()
output = call_2204
func_2205 = relay.Function([], output)
mutated_mod['func_2205'] = func_2205
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2229 = relay.var("var_2229", dtype = "uint64", shape = (4, 1, 5))#candidate|2229|(4, 1, 5)|var|uint64
var_2230 = relay.var("var_2230", dtype = "uint64", shape = (4, 4, 5))#candidate|2230|(4, 4, 5)|var|uint64
bop_2231 = relay.less(var_2229.astype('bool'), var_2230.astype('bool')) # shape=(4, 4, 5)
func_2041_call = mod.get_global_var('func_2041')
func_2042_call = mutated_mod.get_global_var('func_2042')
call_2239 = relay.TupleGetItem(func_2041_call(), 0)
call_2240 = relay.TupleGetItem(func_2042_call(), 0)
func_2054_call = mod.get_global_var('func_2054')
func_2055_call = mutated_mod.get_global_var('func_2055')
call_2243 = relay.TupleGetItem(func_2054_call(), 0)
call_2244 = relay.TupleGetItem(func_2055_call(), 0)
output = relay.Tuple([bop_2231,call_2239,call_2243,])
output2 = relay.Tuple([bop_2231,call_2240,call_2244,])
func_2245 = relay.Function([var_2229,var_2230,], output)
mod['func_2245'] = func_2245
mod = relay.transform.InferType()(mod)
var_2246 = relay.var("var_2246", dtype = "uint64", shape = (4, 1, 5))#candidate|2246|(4, 1, 5)|var|uint64
var_2247 = relay.var("var_2247", dtype = "uint64", shape = (4, 4, 5))#candidate|2247|(4, 4, 5)|var|uint64
output = func_2245(var_2246,var_2247,)
func_2248 = relay.Function([var_2246,var_2247,], output)
mutated_mod['func_2248'] = func_2248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_2269 = relay.TupleGetItem(func_909_call(), 1)
call_2270 = relay.TupleGetItem(func_910_call(), 1)
func_2245_call = mod.get_global_var('func_2245')
func_2248_call = mutated_mod.get_global_var('func_2248')
var_2322 = relay.var("var_2322", dtype = "uint64", shape = (20,))#candidate|2322|(20,)|var|uint64
const_2323 = relay.const([-10,9,4,2,10,-2,-9,-7,10,-6,5,-3,-1,-3,4,5,-7,-1,8,2,3,10,-5,-9,-7,3,-10,-7,1,-8,-5,8,9,-2,5,3,-8,-10,-10,-9,5,-8,-8,7,-4,4,-10,-9,6,-8,-5,-8,5,-5,6,-1,6,5,-2,-5,9,-4,-6,10,8,2,8,-8,8,8,-9,-3,8,-1,2,9,-9,-10,9,6], dtype = "uint64")#candidate|2323|(80,)|const|uint64
call_2321 = relay.TupleGetItem(func_2245_call(relay.reshape(var_2322.astype('uint64'), [4, 1, 5]), relay.reshape(const_2323.astype('uint64'), [4, 4, 5]), ), 1)
call_2324 = relay.TupleGetItem(func_2248_call(relay.reshape(var_2322.astype('uint64'), [4, 1, 5]), relay.reshape(const_2323.astype('uint64'), [4, 4, 5]), ), 1)
output = relay.Tuple([call_2269,call_2321,var_2322,const_2323,])
output2 = relay.Tuple([call_2270,call_2324,var_2322,const_2323,])
func_2325 = relay.Function([var_2322,], output)
mod['func_2325'] = func_2325
mod = relay.transform.InferType()(mod)
mutated_mod['func_2325'] = func_2325
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2326 = relay.var("var_2326", dtype = "uint64", shape = (20,))#candidate|2326|(20,)|var|uint64
func_2325_call = mutated_mod.get_global_var('func_2325')
call_2327 = func_2325_call(var_2326)
output = call_2327
func_2328 = relay.Function([var_2326], output)
mutated_mod['func_2328'] = func_2328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mod.get_global_var('func_1544')
func_1546_call = mutated_mod.get_global_var('func_1546')
call_2354 = relay.TupleGetItem(func_1544_call(), 0)
call_2355 = relay.TupleGetItem(func_1546_call(), 0)
output = call_2354
output2 = call_2355
func_2356 = relay.Function([], output)
mod['func_2356'] = func_2356
mod = relay.transform.InferType()(mod)
mutated_mod['func_2356'] = func_2356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2356_call = mutated_mod.get_global_var('func_2356')
call_2357 = func_2356_call()
output = call_2357
func_2358 = relay.Function([], output)
mutated_mod['func_2358'] = func_2358
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2359 = relay.var("var_2359", dtype = "float32", shape = (12, 5, 9))#candidate|2359|(12, 5, 9)|var|float32
uop_2360 = relay.sigmoid(var_2359.astype('float32')) # shape=(12, 5, 9)
func_1289_call = mod.get_global_var('func_1289')
func_1291_call = mutated_mod.get_global_var('func_1291')
call_2362 = relay.TupleGetItem(func_1289_call(), 1)
call_2363 = relay.TupleGetItem(func_1291_call(), 1)
var_2383 = relay.var("var_2383", dtype = "float32", shape = (1260,))#candidate|2383|(1260,)|var|float32
bop_2384 = relay.logical_xor(call_2362.astype('uint16'), relay.reshape(var_2383.astype('uint16'), relay.shape_of(call_2362))) # shape=(1260,)
bop_2387 = relay.logical_xor(call_2363.astype('uint16'), relay.reshape(var_2383.astype('uint16'), relay.shape_of(call_2363))) # shape=(1260,)
output = relay.Tuple([uop_2360,bop_2384,])
output2 = relay.Tuple([uop_2360,bop_2387,])
func_2404 = relay.Function([var_2359,var_2383,], output)
mod['func_2404'] = func_2404
mod = relay.transform.InferType()(mod)
var_2405 = relay.var("var_2405", dtype = "float32", shape = (12, 5, 9))#candidate|2405|(12, 5, 9)|var|float32
var_2406 = relay.var("var_2406", dtype = "float32", shape = (1260,))#candidate|2406|(1260,)|var|float32
output = func_2404(var_2405,var_2406,)
func_2407 = relay.Function([var_2405,var_2406,], output)
mutated_mod['func_2407'] = func_2407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_2423 = func_876_call()
call_2424 = func_876_call()
output = call_2423
output2 = call_2424
func_2428 = relay.Function([], output)
mod['func_2428'] = func_2428
mod = relay.transform.InferType()(mod)
output = func_2428()
func_2429 = relay.Function([], output)
mutated_mod['func_2429'] = func_2429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1951_call = mod.get_global_var('func_1951')
func_1952_call = mutated_mod.get_global_var('func_1952')
call_2430 = func_1951_call()
call_2431 = func_1951_call()
func_1472_call = mod.get_global_var('func_1472')
func_1475_call = mutated_mod.get_global_var('func_1475')
const_2443 = relay.const([[-6.653102],[6.227882],[6.760797],[7.530052],[5.850330],[-8.127085],[3.177588],[-6.419790],[-9.002504],[3.051043],[-2.110743],[0.931578],[2.478880],[5.686196],[-7.507812],[-1.198106],[-9.508312],[7.738156],[-3.655796],[1.182296],[-5.648158],[3.444683],[9.989775],[-4.274119],[2.506836],[9.186072],[-6.697245],[3.920673],[-2.257196],[-2.748654],[-8.367309],[0.423037],[-8.687688],[7.344425],[0.315990],[-2.722980],[-9.626530],[1.519376],[7.201911],[6.330940],[9.073317],[-6.940923],[8.801301],[-8.111248],[8.159311],[-3.410140],[1.082203],[-3.698640],[-1.751586],[7.801046],[-9.291897],[-3.865791],[2.191337],[2.176204],[8.527997],[4.857899],[9.537172],[1.425877],[0.339730],[-8.137520],[-1.833119],[6.383616],[1.825688],[5.781709],[1.584454],[9.352540],[-7.941765],[-3.276168],[-2.339098],[-3.765782],[7.986136],[-2.689241],[7.916322],[1.775480],[0.979888],[5.501661],[3.858245],[-7.234189],[4.703837],[-5.644680],[-4.009470],[-1.351134],[9.651557],[-0.644103],[-5.469399],[-7.941651],[3.139159],[9.101584],[-8.826171],[6.232044],[-2.102442],[7.616605],[3.171210],[-7.716597],[9.669005],[9.745084],[0.399783],[-5.231253],[9.363082],[-9.491344],[4.505545],[0.114968],[2.987193],[1.314677],[4.198117],[-1.618668],[-8.731483],[1.311420],[1.481019],[-8.999798],[4.603704],[-1.683931],[5.149897],[4.875548],[2.263695],[7.703574],[-6.324792],[5.786042],[6.602068],[0.600081],[-3.570353],[-7.470776],[5.882153],[-6.774261],[-8.248654],[3.262712],[4.386213],[-5.756652],[-8.581695],[7.909570],[7.445566],[-2.301171],[2.775203],[4.040573],[2.691111],[0.846462],[-6.549459],[-4.916986],[-7.410369],[-6.404546],[2.193361],[-1.597884],[6.543170],[5.770045],[-6.245408],[-7.615091],[7.915987],[-4.980058],[-9.247576],[0.853585],[-7.318309],[0.351505],[8.718501],[4.439043],[3.705356],[-4.891691],[9.503952],[9.994798],[5.193177],[6.182584],[5.805161],[2.216888],[-3.249623],[3.375691],[9.340644],[-7.934335],[5.370322],[9.473104],[6.926828],[-5.335789],[-3.202376],[7.667327],[6.699213],[8.155244],[-8.893068],[7.523875],[-4.146081],[-0.223808],[-1.984374],[5.334436],[7.411017],[2.172926],[-2.257064],[0.913183],[6.317901],[-2.920128],[-5.263309],[-3.013862],[-9.073170],[-7.410472],[-3.242653],[-2.798696],[-8.320426],[3.542425],[-4.190821],[-6.614478],[5.065736],[-6.688342],[-1.254070],[8.586707],[-1.448199],[-4.790191],[-0.200790],[-9.682185],[-2.252838],[5.559976],[-3.748280],[3.626009],[-0.354186],[3.564137],[9.538626],[-6.556638],[-8.342957],[-4.127997],[-0.886943],[-8.335865],[8.338483],[0.321656],[8.978784],[-4.558952],[-0.863500],[-1.150911],[8.283339],[1.341720],[4.092306],[-8.913268],[1.430862],[8.266696],[-0.854535],[-0.313105],[2.313497],[4.225290],[1.031075],[-7.742577],[-7.339263],[-8.514796],[-1.037741],[-0.681097],[-1.625855],[-6.324571],[-2.223044],[9.398138],[9.838823],[3.600560],[-3.226475],[1.924748],[2.877130],[1.082592],[4.960442],[1.347471],[-6.920713],[2.474346],[7.905025],[2.947841],[4.443762],[4.788188],[-7.719483],[8.684337],[2.784919],[6.702281],[8.363313],[8.165782],[8.994893],[6.187996],[6.765380],[0.057717],[7.071476],[-7.546437],[-4.670584],[-5.978436],[1.728000],[9.597761],[-8.478831],[-1.747903],[-4.684446],[-9.346659],[-1.232161],[-0.896317],[-3.172382],[-0.025974],[-4.410442],[9.889606],[-0.960161],[-0.936434],[4.615012],[1.585997],[-9.700324],[7.258461],[7.669292],[-4.311732],[5.120101],[1.975758],[1.865927],[-2.700759],[-0.226460],[4.908519],[-7.013413],[-7.520420],[-6.307376],[5.093094]], dtype = "float64")#candidate|2443|(300, 1)|const|float64
call_2442 = func_1472_call(relay.reshape(const_2443.astype('float64'), [10, 6, 5]))
call_2444 = func_1472_call(relay.reshape(const_2443.astype('float64'), [10, 6, 5]))
func_1289_call = mod.get_global_var('func_1289')
func_1291_call = mutated_mod.get_global_var('func_1291')
call_2448 = relay.TupleGetItem(func_1289_call(), 0)
call_2449 = relay.TupleGetItem(func_1291_call(), 0)
func_1738_call = mod.get_global_var('func_1738')
func_1742_call = mutated_mod.get_global_var('func_1742')
var_2451 = relay.var("var_2451", dtype = "int8", shape = (1, 351))#candidate|2451|(1, 351)|var|int8
call_2450 = relay.TupleGetItem(func_1738_call(relay.reshape(call_2442.astype('float64'), [300,]), relay.reshape(var_2451.astype('int8'), [1, 351]), ), 1)
call_2452 = relay.TupleGetItem(func_1742_call(relay.reshape(call_2442.astype('float64'), [300,]), relay.reshape(var_2451.astype('int8'), [1, 351]), ), 1)
output = relay.Tuple([call_2430,call_2442,const_2443,call_2448,call_2450,var_2451,])
output2 = relay.Tuple([call_2431,call_2444,const_2443,call_2449,call_2452,var_2451,])
func_2455 = relay.Function([var_2451,], output)
mod['func_2455'] = func_2455
mod = relay.transform.InferType()(mod)
mutated_mod['func_2455'] = func_2455
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2456 = relay.var("var_2456", dtype = "int8", shape = (1, 351))#candidate|2456|(1, 351)|var|int8
func_2455_call = mutated_mod.get_global_var('func_2455')
call_2457 = func_2455_call(var_2456)
output = call_2457
func_2458 = relay.Function([var_2456], output)
mutated_mod['func_2458'] = func_2458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_2555 = func_365_call()
call_2556 = func_365_call()
func_1544_call = mod.get_global_var('func_1544')
func_1546_call = mutated_mod.get_global_var('func_1546')
call_2559 = relay.TupleGetItem(func_1544_call(), 1)
call_2560 = relay.TupleGetItem(func_1546_call(), 1)
output = relay.Tuple([call_2555,call_2559,])
output2 = relay.Tuple([call_2556,call_2560,])
func_2572 = relay.Function([], output)
mod['func_2572'] = func_2572
mod = relay.transform.InferType()(mod)
mutated_mod['func_2572'] = func_2572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mutated_mod.get_global_var('func_2572')
call_2573 = func_2572_call()
output = call_2573
func_2574 = relay.Function([], output)
mutated_mod['func_2574'] = func_2574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_730_call = mod.get_global_var('func_730')
func_731_call = mutated_mod.get_global_var('func_731')
call_2616 = relay.TupleGetItem(func_730_call(), 0)
call_2617 = relay.TupleGetItem(func_731_call(), 0)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_2645 = func_365_call()
call_2646 = func_365_call()
func_1223_call = mod.get_global_var('func_1223')
func_1224_call = mutated_mod.get_global_var('func_1224')
call_2658 = func_1223_call()
call_2659 = func_1223_call()
func_2184_call = mod.get_global_var('func_2184')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_2660 = func_2184_call()
call_2661 = func_2184_call()
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_2673 = relay.TupleGetItem(func_465_call(), 0)
call_2674 = relay.TupleGetItem(func_467_call(), 0)
output = relay.Tuple([call_2616,call_2645,call_2658,call_2660,call_2673,])
output2 = relay.Tuple([call_2617,call_2646,call_2659,call_2661,call_2674,])
func_2677 = relay.Function([], output)
mod['func_2677'] = func_2677
mod = relay.transform.InferType()(mod)
mutated_mod['func_2677'] = func_2677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2677_call = mutated_mod.get_global_var('func_2677')
call_2678 = func_2677_call()
output = call_2678
func_2679 = relay.Function([], output)
mutated_mod['func_2679'] = func_2679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_730_call = mod.get_global_var('func_730')
func_731_call = mutated_mod.get_global_var('func_731')
call_2690 = relay.TupleGetItem(func_730_call(), 0)
call_2691 = relay.TupleGetItem(func_731_call(), 0)
const_2694 = relay.const([[[3.391008,-8.626244,-2.939828,3.093048,-5.398148,-6.882179,-1.488257,-9.160156,-6.126948,5.967800,-4.297173,8.982698,-6.938504,-2.065770],[-1.410264,-0.282866,-5.236191,-4.076793,6.261101,-6.291745,3.799151,5.921033,6.850130,-2.313392,2.830364,-0.968206,5.974157,7.540593],[8.214244,-2.499040,4.995217,4.980662,6.364506,5.995501,-8.239781,7.958510,-3.109473,7.917691,-5.975336,5.728958,5.435839,3.559103],[-8.858736,1.408696,-9.006983,7.908626,-7.393549,-0.805497,-3.356818,3.292854,0.767722,3.508055,7.098063,1.660681,-1.525375,2.117181],[-0.475953,-3.184097,7.675193,4.772063,9.991879,9.005099,5.787056,-4.003994,9.740492,-9.141793,-2.718530,-9.598784,-0.991952,3.721983],[4.703389,7.228623,0.517068,-5.326881,9.102083,6.003831,-3.172537,-9.041509,-9.144275,5.135647,-9.632702,-9.885952,0.749579,-1.914526],[4.075556,6.758335,-4.121667,-6.658792,-2.441361,-9.958887,-2.919106,8.241448,7.215311,9.265427,-8.251333,4.996593,-7.853339,4.832076],[1.736852,-3.517688,5.540773,9.272310,-3.749289,8.883345,-6.095061,-0.871322,1.876566,3.600513,4.051592,-2.232745,4.874951,5.488557],[-3.951785,-1.916990,-1.452917,-2.830866,-6.775034,-5.276855,7.587488,2.714300,6.444336,3.097962,6.683313,6.838455,7.767774,-0.114339]],[[-4.126140,-7.004117,-5.160272,-8.842966,8.541378,-0.394802,-0.841986,-2.258719,0.300365,6.593752,3.561773,7.645300,1.255619,-5.965831],[6.045746,5.124456,-7.343357,-0.489793,-0.676970,1.494490,8.477992,2.667751,-8.957639,1.592183,-3.626367,0.335811,0.813799,-5.522901],[8.143409,4.190427,-9.336012,-0.755081,3.317988,1.318486,4.865399,0.614536,1.456230,-3.294861,7.247660,3.825625,-3.783393,3.299582],[0.525610,-3.933852,-0.060948,7.837022,3.084175,4.143185,-7.999941,-8.855058,-0.913149,-7.971760,2.553784,3.294471,3.649276,-6.768198],[6.769052,5.706898,3.975038,-0.730394,-3.094483,-6.651611,6.827165,-1.871462,7.445007,-3.225989,-1.329917,6.719813,9.062067,-4.466693],[9.251523,6.643006,4.049471,6.326384,-0.985970,-8.029527,-4.281851,-5.182984,3.395310,4.463948,-1.635512,-9.855873,4.508027,-1.168006],[-6.338536,9.467981,1.983594,7.406731,7.937943,8.058651,-5.075327,-2.315746,0.475654,-5.828528,9.637841,1.285689,5.877618,6.877057],[5.067197,-4.108527,-8.990928,4.904782,-6.893471,-0.229874,6.433956,2.486709,-0.788322,-9.196798,4.958387,-8.994740,6.983008,-0.414490],[1.475968,2.186867,1.037459,-8.253013,1.286728,5.588980,-4.458957,5.785711,2.628593,8.613204,7.909089,5.052454,4.955303,3.171448]],[[7.902279,0.217163,4.556595,9.974757,-9.885457,3.412873,8.858668,5.321456,-6.656516,-5.934758,-9.695862,5.308872,2.866714,-5.314085],[-2.148272,3.062464,8.771883,-1.212141,6.593304,7.320508,-0.236021,1.604095,4.121765,8.774719,-2.416867,3.611967,-4.835193,-1.355255],[-7.128852,-1.418511,-2.953990,-1.747749,-5.469048,6.417002,0.180437,-4.750115,9.273499,7.435835,-8.191464,-5.481749,-3.445842,4.782630],[3.511063,7.912842,-8.231165,-1.087346,6.437208,-5.970453,-9.325054,-8.496847,-4.729906,3.364667,-1.348706,-6.933805,0.063321,3.195809],[7.357743,-9.328207,-0.613073,-3.545334,4.987926,-2.691754,9.906894,7.197631,-0.767675,8.327472,-0.195310,-1.006728,-6.989051,2.955889],[7.278995,8.687530,-0.902951,8.378389,1.624295,9.929326,6.311659,-7.315305,3.140933,-7.019773,9.910794,-4.520400,-3.175444,-3.027098],[-2.157386,-5.122511,5.578756,-3.390356,-2.275366,-9.854641,5.042748,-6.370273,8.805590,1.504523,-4.910967,-5.620439,-8.291014,2.755864],[4.954760,3.075288,-1.341649,-1.533872,9.816484,1.068606,-3.933324,-7.010374,7.062739,-4.923965,1.010950,3.950363,5.343045,6.932749],[0.846366,-2.283271,-5.733177,-0.333575,-4.808104,-4.731350,7.057234,8.081520,-6.651119,0.557855,-9.048381,-1.451527,5.746885,-8.290350]],[[-9.577918,-5.182186,-4.382002,-6.811475,-8.560021,3.042824,0.738845,2.142437,2.350175,7.199525,-1.702840,-1.815388,-1.465678,-6.379924],[-9.178670,8.616580,-4.208381,-2.812582,-1.400018,4.955018,6.449583,6.547532,6.436053,9.376807,8.222521,-0.036122,8.090395,6.476954],[9.480754,-1.960473,-7.574837,-9.517269,8.621683,0.376218,-2.162822,7.617226,-5.294996,-9.789736,5.406114,-6.150114,-9.124119,-7.744468],[8.525301,-1.641819,8.502993,9.693514,-1.569789,-9.049931,-9.310797,2.594819,-7.367910,7.990644,-6.523497,-8.918316,3.079683,-2.164212],[3.749785,-0.814273,-6.245464,-8.404317,3.543149,5.633031,9.762845,5.023796,-2.317957,-1.783970,5.735687,7.089613,-3.144054,5.312511],[-6.260524,4.597556,-8.989356,6.011556,-8.873770,-0.502290,8.814967,2.842184,3.085285,-0.725064,-9.874309,9.117917,-2.582505,7.354724],[-6.213095,4.431977,-0.426716,7.622943,-6.377120,-7.103186,-3.023783,-8.093827,-4.629114,-5.387519,-1.683202,0.942846,-4.508856,0.647692],[5.360998,6.192591,7.835664,1.351972,5.188729,4.303506,8.515449,8.565509,-7.485172,5.949349,8.793307,1.264414,-3.432972,-0.165767],[5.835657,-0.349210,-9.849087,-6.917280,-6.638864,-5.864639,-7.628647,0.729465,2.486416,0.991720,-0.427858,-9.031911,4.827403,0.738739]],[[0.874689,-9.028501,7.056803,0.714892,-8.482597,-0.849167,2.120158,-5.928219,-2.424561,5.801563,-3.042720,6.952701,9.608502,1.305591],[3.270365,6.612403,-8.584749,3.228591,-0.268219,-6.656535,1.208737,8.712151,9.293317,-7.425269,7.442202,3.856639,6.819201,-9.135377],[-9.325676,5.445698,-6.842964,-6.527369,-2.593548,4.253489,4.565473,5.074441,-4.557554,7.448520,-4.544097,8.340613,-8.515233,-8.738608],[5.894205,-2.766183,-4.508425,-4.237101,-3.964186,0.455266,-8.313248,7.487404,-7.931936,-3.446986,3.726737,-5.515635,-1.122865,2.794336],[-8.744346,-2.764042,-0.874398,-7.219233,-7.518122,-3.891524,9.474660,4.864258,-6.013496,1.439219,9.654651,1.607487,-6.887749,-5.861617],[3.049066,3.230469,9.957992,3.503297,-2.070268,-6.552162,-4.111324,-5.579979,9.494358,-4.921377,-9.211526,-9.506003,4.135780,6.458054],[-7.740106,-0.203948,1.473645,9.299060,7.172191,9.795513,-4.109391,-3.903515,-0.368865,7.436203,-0.930133,5.298425,4.563264,-6.940009],[2.858144,-6.756784,-1.824588,9.900378,-0.344135,-1.617259,9.132684,-7.168848,-4.784798,4.295780,2.265486,-7.313604,-7.158785,-6.980480],[8.513597,-3.346843,-9.939520,-5.256340,-6.104145,6.527430,4.734755,-7.918531,5.332046,-8.742141,-1.064648,-8.031789,-7.869074,3.784606]],[[-2.816398,2.609551,9.868252,-4.810525,-7.549137,-6.445517,-5.874118,-2.113234,8.794821,-6.020320,3.455918,-9.793066,-7.798146,3.124403],[0.791845,1.683975,-9.649093,-5.470042,7.739314,-9.754068,1.157476,-9.476262,-3.291513,1.909057,6.179464,-1.670713,3.418894,-0.012267],[4.494460,-0.437567,3.838668,-1.415820,-7.013585,5.415678,1.843206,-1.608390,-9.831075,-1.758904,8.392556,-9.001589,6.468064,4.618884],[-8.949295,4.428260,5.702403,-5.346339,5.626273,-4.719612,8.316599,1.274234,9.640597,-1.793149,-4.056014,-2.763334,-8.384785,5.421391],[7.433879,-1.983091,-2.129967,0.535784,-9.071940,-0.771613,-0.967660,0.347966,-7.046892,-0.243681,-4.073225,1.153612,2.645006,-4.738671],[3.414031,-0.761266,-9.371290,-4.494761,-2.051054,-7.879002,8.720915,-8.025805,-4.605366,-9.034074,9.051057,-2.189467,5.249780,-0.606442],[-7.295892,-3.085104,-6.586723,-2.673868,-0.406635,-1.953551,7.220763,3.508918,6.600207,-5.144251,5.115832,6.668833,-5.335932,0.067775],[0.200711,-4.558210,-2.732106,7.262789,9.168514,-8.321747,-9.815305,-9.746519,3.506218,1.692210,-4.675588,-4.625266,-3.187423,-5.269478],[-8.486721,-8.988570,5.990082,2.914655,7.363155,0.017575,-1.416753,-4.829853,-5.825051,-3.256684,-7.601602,-3.378450,-5.773883,6.294116]],[[-0.597244,0.930715,8.483904,9.932201,-5.777842,-5.622302,6.990358,2.544540,8.833510,9.119980,-2.657919,-7.612726,3.113425,6.168588],[2.659724,-4.710499,-6.548861,-3.578636,0.850344,3.634807,-6.318485,0.937980,5.994303,-5.686106,7.960049,-0.377591,3.541173,-8.764275],[4.110195,-1.625687,-7.523835,0.236966,-6.175326,-7.289966,1.632583,-6.910352,-8.221293,4.052582,-9.145896,-6.657990,1.593065,6.422184],[6.395832,3.037941,-3.749302,-2.395189,-8.143585,5.256232,4.149589,-0.336922,1.676506,0.517845,3.044107,1.990395,-2.346548,4.671870],[-2.274980,-7.013980,-2.408908,3.888628,-2.228808,-6.716660,3.475884,9.923759,2.894595,9.709957,-8.492372,-4.626831,1.809310,7.920915],[-1.643957,-0.181869,-5.662256,-4.983921,-2.611804,4.155033,1.221656,-8.893384,6.435013,-1.260200,2.545756,-8.351797,-2.686857,6.409565],[-9.912729,2.771752,4.253905,-6.412265,-2.583794,7.220053,-8.354424,0.507585,-8.183384,-5.231922,-0.189044,-7.376117,-0.909440,8.679769],[-1.050711,-1.766253,-8.675150,0.725361,7.185065,0.255305,-2.767754,8.883873,4.290809,7.716739,-5.311000,2.086687,-8.269729,-6.383138],[-1.568432,5.857885,8.267598,-7.553570,7.559306,4.048857,3.997232,-4.028861,7.721453,-5.012406,2.609710,-7.579149,1.146384,-3.627252]],[[-4.075842,-3.195507,-8.940541,5.113882,8.937851,6.727496,5.631766,-7.315280,7.767611,-8.393478,-9.304130,7.264639,-9.114300,2.786142],[-7.461783,5.178427,-3.514328,3.218032,9.739674,-3.829395,-2.170064,7.749244,3.780359,-7.160731,5.821310,2.325286,2.698634,8.206146],[8.066513,7.005230,-5.841891,-6.896873,-1.945493,5.098489,-6.285729,7.640080,-6.784971,-6.795210,-1.942968,-5.702237,0.807558,3.603009],[2.332066,0.940432,1.848825,-7.091036,0.786070,-7.311079,-4.055057,-5.761245,-2.171427,-5.345748,-2.354307,-6.486341,9.953442,-5.730902],[-6.577651,-3.316485,-1.661736,-0.585144,-8.791864,0.705403,8.142441,-2.884737,-0.127629,-5.204790,-5.625387,0.105527,6.948894,4.684174],[-4.163680,-5.228390,2.946983,-0.065853,-2.089771,7.820264,4.351452,-4.642445,-2.976731,5.670712,3.258811,5.500956,-8.123057,4.761367],[-9.213571,-0.401895,-7.331822,-5.307081,3.867826,-5.290656,6.861197,4.478716,-7.649217,-2.299512,-5.354567,6.681148,6.715815,2.884634],[4.476764,-2.902963,9.864651,3.910242,4.445192,8.969941,-5.264338,-8.084433,0.741511,8.394015,7.145309,-0.791211,2.019460,-6.404104],[8.307963,-4.578366,-4.022836,-6.814495,6.405156,4.299443,5.835270,-1.060986,-0.250834,-9.197857,-0.925978,-6.300569,0.897781,2.388942]],[[-7.375653,2.497242,9.061619,2.190562,-3.146882,1.817658,4.604474,-9.773566,9.814085,-7.087410,8.073362,7.382356,-4.274995,-3.731878],[-1.474298,-3.154583,0.573672,-4.602284,3.383720,-1.137268,-8.189914,-7.070743,-0.828572,-9.994393,0.781555,-4.567396,3.077712,-3.247537],[5.883409,7.508816,-7.232619,-4.896482,-2.353792,-5.630206,-6.992048,3.588378,-3.230448,-3.573415,2.961410,-7.134225,-2.098802,5.170095],[-3.326077,0.624157,-0.158014,8.054601,6.129211,-3.693943,4.018971,2.568529,0.106433,-6.215494,-9.190641,5.381303,1.191816,-1.139314],[-6.034510,-5.281442,9.528412,-3.889478,-2.956711,-3.137924,6.087183,7.349558,6.025138,3.247790,-1.094434,-6.996740,-2.253138,-9.568315],[1.311110,7.426966,-7.605959,-4.117567,-1.126937,-6.075718,4.213283,-6.847174,3.758138,0.689472,-1.415457,-6.640969,-6.912805,-0.607449],[-7.737795,-7.353021,5.433441,1.084706,0.986232,-8.147913,-9.729298,5.602401,7.742401,-5.786134,1.377043,-3.923988,-5.714527,-4.482579],[8.774574,-3.923670,6.936849,-5.915910,-1.663036,7.466661,6.121827,1.188711,-5.316695,7.228379,-1.927232,-4.973503,8.058046,-2.770953],[2.538912,-9.849080,9.676965,-6.377744,-4.891819,7.062305,-1.548436,-2.934471,-2.955469,1.776348,-0.649145,9.205246,9.134112,6.111782]],[[-8.058889,-0.158389,-0.472191,-2.850057,8.111061,3.192465,6.883529,0.158549,2.722181,-8.385551,4.950803,-4.229970,-0.903390,4.691041],[4.611851,5.490528,-0.305685,-4.270790,-8.442032,-8.142676,6.612921,1.008563,-4.131032,6.470004,8.063459,-6.154364,8.851515,-8.848837],[-5.634776,0.101238,-4.383711,5.286399,0.391531,-0.323737,-7.012198,7.744940,-7.293326,2.796537,3.849305,-5.828059,-6.660884,-4.144303],[7.508715,2.807974,-5.483066,2.034890,7.732150,1.471220,-7.895712,6.422375,-4.502603,2.047493,5.588804,7.817166,5.856464,8.504959],[-5.628025,9.755218,1.471158,9.531922,-6.851143,-1.266988,1.988853,-3.614870,6.588214,0.275807,-7.928858,-8.628399,9.562939,0.759219],[2.738773,-0.631285,-4.120918,8.456625,-1.737014,7.351809,-6.895514,1.593120,5.119386,7.394791,3.802513,-9.429169,2.027566,8.906246],[-2.063003,9.026781,-5.914779,-0.012032,-5.984931,-2.930814,-0.522022,1.509042,6.420363,8.838911,-9.039411,-3.617917,9.204715,7.040345],[0.276313,1.518276,9.977863,-7.862879,-9.991005,-3.558416,-6.252683,1.503319,-7.008206,9.425702,2.640710,-8.775066,-9.994955,6.670255],[2.295022,-6.648067,-8.122050,9.772795,8.771589,7.574869,-9.405764,-5.008260,-7.697025,1.615251,-4.787418,-7.234632,7.757658,7.689735]]], dtype = "float32")#candidate|2694|(10, 9, 14)|const|float32
bop_2695 = relay.left_shift(call_2690.astype('int16'), relay.reshape(const_2694.astype('int16'), relay.shape_of(call_2690))) # shape=(10, 9, 14)
bop_2698 = relay.left_shift(call_2691.astype('int16'), relay.reshape(const_2694.astype('int16'), relay.shape_of(call_2691))) # shape=(10, 9, 14)
bop_2726 = relay.divide(call_2690.astype('float32'), relay.reshape(const_2694.astype('float32'), relay.shape_of(call_2690))) # shape=(10, 9, 14)
bop_2729 = relay.divide(call_2691.astype('float32'), relay.reshape(const_2694.astype('float32'), relay.shape_of(call_2691))) # shape=(10, 9, 14)
func_1472_call = mod.get_global_var('func_1472')
func_1475_call = mutated_mod.get_global_var('func_1475')
const_2732 = relay.const([3.493215,-3.600434,4.630845,5.181638,9.252821,3.512366,-8.772986,4.812101,1.876436,4.884559,-2.222350,-7.474821,9.294014,-1.711314,-2.663519,-5.526757,-6.864492,-6.127536,-9.264190,0.341856,-2.198142,-5.316531,8.494791,-6.985729,-4.478150,5.622051,-3.309089,1.826710,-6.555866,9.633123,2.568231,-9.410110,-3.041810,7.681925,-5.726381,-7.115737,5.231118,9.651618,-7.944079,-3.033091,6.632693,-6.804052,3.149395,0.251131,8.748988,4.876658,2.076335,-0.235307,-1.096488,-3.008774,-3.057540,7.060427,-5.453748,4.647922,-0.445223,8.801003,9.606759,8.128760,6.213358,-3.208729,7.883882,5.605063,8.163027,-2.926858,9.283300,-6.438774,4.038111,2.670309,-0.919358,2.887684,-5.349067,3.227735,-8.323078,3.030216,2.837990,-7.160035,9.079055,1.213513,4.748808,-1.282469,1.229096,-6.963404,-9.170889,-9.765457,-4.373150,3.090015,-7.138563,-7.559853,3.750290,-1.083602,8.684663,-4.004546,-1.126237,3.022283,7.088884,-5.407286,-2.028266,-0.651916,-6.837418,-3.975524,-5.213868,-1.766846,-7.804340,4.595973,-0.880669,-4.299269,-7.685909,-6.864079,3.961064,-2.745384,5.975491,5.122406,2.247054,-7.652805,-1.019608,3.008022,-7.812517,5.266551,-5.831991,-4.551380,-8.635354,0.950590,9.467742,1.656715,9.223650,-6.556063,-8.572967,8.613438,4.954361,6.190959,-2.981935,-9.850196,-3.461864,6.035563,-2.265110,3.315541,-9.306403,1.854386,-7.046005,-2.042107,-1.730587,-0.377753,-3.917105,-0.965172,2.325367,8.801187,-3.236030,-6.548029,6.454473,-3.699322,-6.449384,-4.823391,-5.478747,-8.803074,-1.789017,-9.096620,6.084383,7.393668,-1.955626,2.294177,-6.571602,2.180812,-5.071892,0.079051,0.688410,7.976447,-6.630940,7.454843,3.740070,2.657859,-9.046410,-1.180312,8.027915,-0.625417,-2.409214,5.654360,-7.263552,7.367434,4.720868,2.901820,-7.050881,-3.318259,-9.179249,4.570919,2.003022,-1.774450,4.015494,-9.302743,-0.059746,-8.094274,-0.032022,8.452960,3.577615,-5.698162,-0.341437,9.208436,-8.034126,0.472254,7.483666,2.171430,1.813467,5.971330,-0.219994,2.527663,-2.109539,4.758526,-2.064521,3.070126,-0.183743,-9.068966,3.497112,9.331447,8.303847,7.576553,-1.836524,1.392378,-5.471872,-3.676998,-6.268397,0.846990,4.054924,-9.549572,-0.376703,8.579266,4.348004,0.105663,-1.167657,-1.217835,5.099281,-1.770871,-1.897509,2.974747,-8.391558,-1.108566,-7.902677,9.285900,-3.356676,6.160515,-0.070129,0.084326,-0.141934,-6.959361,-7.708479,-9.194756,-6.702657,3.789971,-7.932746,9.525167,-8.698260,-9.871817,-6.030563,-3.757027,0.364251,3.080665,2.027737,8.218933,3.630316,-3.151683,-3.593884,0.750325,6.042471,-5.485579,6.823330,9.945894,0.314327,-2.592542,9.234608,-0.620464,-5.382169,-1.068424,0.354287,5.720651,-8.052216,-8.504889,-3.990326,6.537372,-2.037230,-3.508418,-2.444613,8.193047,3.033691,0.202198,-5.438470,1.506560,7.042872,-3.680569,3.191342,7.171366,4.321580,-6.856201,1.128106,-8.864064,1.739201,0.089527,-6.303768,9.279116,8.004616,-3.280040,4.879683,-3.971329], dtype = "float64")#candidate|2732|(300,)|const|float64
call_2731 = func_1472_call(relay.reshape(const_2732.astype('float64'), [10, 6, 5]))
call_2733 = func_1472_call(relay.reshape(const_2732.astype('float64'), [10, 6, 5]))
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_2741 = func_2428_call()
call_2742 = func_2428_call()
output = relay.Tuple([bop_2695,bop_2726,call_2731,const_2732,call_2741,])
output2 = relay.Tuple([bop_2698,bop_2729,call_2733,const_2732,call_2742,])
func_2750 = relay.Function([], output)
mod['func_2750'] = func_2750
mod = relay.transform.InferType()(mod)
output = func_2750()
func_2751 = relay.Function([], output)
mutated_mod['func_2751'] = func_2751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mod.get_global_var('func_1083')
func_1084_call = mutated_mod.get_global_var('func_1084')
call_2763 = relay.TupleGetItem(func_1083_call(), 1)
call_2764 = relay.TupleGetItem(func_1084_call(), 1)
func_610_call = mod.get_global_var('func_610')
func_613_call = mutated_mod.get_global_var('func_613')
var_2776 = relay.var("var_2776", dtype = "float64", shape = (175,))#candidate|2776|(175,)|var|float64
call_2775 = relay.TupleGetItem(func_610_call(relay.reshape(var_2776.astype('float64'), [5, 7, 5])), 1)
call_2777 = relay.TupleGetItem(func_613_call(relay.reshape(var_2776.astype('float64'), [5, 7, 5])), 1)
output = relay.Tuple([call_2763,call_2775,var_2776,])
output2 = relay.Tuple([call_2764,call_2777,var_2776,])
func_2785 = relay.Function([var_2776,], output)
mod['func_2785'] = func_2785
mod = relay.transform.InferType()(mod)
mutated_mod['func_2785'] = func_2785
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2786 = relay.var("var_2786", dtype = "float64", shape = (175,))#candidate|2786|(175,)|var|float64
func_2785_call = mutated_mod.get_global_var('func_2785')
call_2787 = func_2785_call(var_2786)
output = call_2787
func_2788 = relay.Function([var_2786], output)
mutated_mod['func_2788'] = func_2788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1631_call = mod.get_global_var('func_1631')
func_1632_call = mutated_mod.get_global_var('func_1632')
call_2792 = relay.TupleGetItem(func_1631_call(), 3)
call_2793 = relay.TupleGetItem(func_1632_call(), 3)
func_2054_call = mod.get_global_var('func_2054')
func_2055_call = mutated_mod.get_global_var('func_2055')
call_2802 = relay.TupleGetItem(func_2054_call(), 1)
call_2803 = relay.TupleGetItem(func_2055_call(), 1)
uop_2809 = relay.asin(call_2802.astype('float32')) # shape=(10, 9, 14)
uop_2811 = relay.asin(call_2803.astype('float32')) # shape=(10, 9, 14)
output = relay.Tuple([call_2792,uop_2809,])
output2 = relay.Tuple([call_2793,uop_2811,])
func_2815 = relay.Function([], output)
mod['func_2815'] = func_2815
mod = relay.transform.InferType()(mod)
mutated_mod['func_2815'] = func_2815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mutated_mod.get_global_var('func_2815')
call_2816 = func_2815_call()
output = call_2816
func_2817 = relay.Function([], output)
mutated_mod['func_2817'] = func_2817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2677_call = mod.get_global_var('func_2677')
func_2679_call = mutated_mod.get_global_var('func_2679')
call_2837 = relay.TupleGetItem(func_2677_call(), 3)
call_2838 = relay.TupleGetItem(func_2679_call(), 3)
output = call_2837
output2 = call_2838
func_2849 = relay.Function([], output)
mod['func_2849'] = func_2849
mod = relay.transform.InferType()(mod)
output = func_2849()
func_2850 = relay.Function([], output)
mutated_mod['func_2850'] = func_2850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_2868 = relay.TupleGetItem(func_465_call(), 0)
call_2869 = relay.TupleGetItem(func_467_call(), 0)
var_2887 = relay.var("var_2887", dtype = "float32", shape = (10, 9, 14))#candidate|2887|(10, 9, 14)|var|float32
bop_2888 = relay.minimum(call_2868.astype('int64'), relay.reshape(var_2887.astype('int64'), relay.shape_of(call_2868))) # shape=(10, 9, 14)
bop_2891 = relay.minimum(call_2869.astype('int64'), relay.reshape(var_2887.astype('int64'), relay.shape_of(call_2869))) # shape=(10, 9, 14)
output = relay.Tuple([bop_2888,])
output2 = relay.Tuple([bop_2891,])
func_2896 = relay.Function([var_2887,], output)
mod['func_2896'] = func_2896
mod = relay.transform.InferType()(mod)
var_2897 = relay.var("var_2897", dtype = "float32", shape = (10, 9, 14))#candidate|2897|(10, 9, 14)|var|float32
output = func_2896(var_2897)
func_2898 = relay.Function([var_2897], output)
mutated_mod['func_2898'] = func_2898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1687_call = mod.get_global_var('func_1687')
func_1688_call = mutated_mod.get_global_var('func_1688')
call_2908 = relay.TupleGetItem(func_1687_call(), 0)
call_2909 = relay.TupleGetItem(func_1688_call(), 0)
output = call_2908
output2 = call_2909
func_2915 = relay.Function([], output)
mod['func_2915'] = func_2915
mod = relay.transform.InferType()(mod)
mutated_mod['func_2915'] = func_2915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2915_call = mutated_mod.get_global_var('func_2915')
call_2916 = func_2915_call()
output = call_2916
func_2917 = relay.Function([], output)
mutated_mod['func_2917'] = func_2917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mod.get_global_var('func_1223')
func_1224_call = mutated_mod.get_global_var('func_1224')
call_2952 = func_1223_call()
call_2953 = func_1223_call()
var_2957 = relay.var("var_2957", dtype = "float64", shape = (10, 9, 14))#candidate|2957|(10, 9, 14)|var|float64
bop_2958 = relay.less(call_2952.astype('bool'), relay.reshape(var_2957.astype('bool'), relay.shape_of(call_2952))) # shape=(10, 9, 14)
bop_2961 = relay.less(call_2953.astype('bool'), relay.reshape(var_2957.astype('bool'), relay.shape_of(call_2953))) # shape=(10, 9, 14)
output = relay.Tuple([bop_2958,])
output2 = relay.Tuple([bop_2961,])
func_2963 = relay.Function([var_2957,], output)
mod['func_2963'] = func_2963
mod = relay.transform.InferType()(mod)
mutated_mod['func_2963'] = func_2963
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2964 = relay.var("var_2964", dtype = "float64", shape = (10, 9, 14))#candidate|2964|(10, 9, 14)|var|float64
func_2963_call = mutated_mod.get_global_var('func_2963')
call_2965 = func_2963_call(var_2964)
output = call_2965
func_2966 = relay.Function([var_2964], output)
mutated_mod['func_2966'] = func_2966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mod.get_global_var('func_1223')
func_1224_call = mutated_mod.get_global_var('func_1224')
call_2970 = func_1223_call()
call_2971 = func_1223_call()
output = call_2970
output2 = call_2971
func_2972 = relay.Function([], output)
mod['func_2972'] = func_2972
mod = relay.transform.InferType()(mod)
mutated_mod['func_2972'] = func_2972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2972_call = mutated_mod.get_global_var('func_2972')
call_2973 = func_2972_call()
output = call_2973
func_2974 = relay.Function([], output)
mutated_mod['func_2974'] = func_2974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2972_call = mod.get_global_var('func_2972')
func_2974_call = mutated_mod.get_global_var('func_2974')
call_2991 = func_2972_call()
call_2992 = func_2972_call()
output = call_2991
output2 = call_2992
func_3044 = relay.Function([], output)
mod['func_3044'] = func_3044
mod = relay.transform.InferType()(mod)
output = func_3044()
func_3045 = relay.Function([], output)
mutated_mod['func_3045'] = func_3045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2817_call = mutated_mod.get_global_var('func_2817')
call_3049 = relay.TupleGetItem(func_2815_call(), 0)
call_3050 = relay.TupleGetItem(func_2817_call(), 0)
output = relay.Tuple([call_3049,])
output2 = relay.Tuple([call_3050,])
func_3051 = relay.Function([], output)
mod['func_3051'] = func_3051
mod = relay.transform.InferType()(mod)
output = func_3051()
func_3052 = relay.Function([], output)
mutated_mod['func_3052'] = func_3052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3051_call = mod.get_global_var('func_3051')
func_3052_call = mutated_mod.get_global_var('func_3052')
call_3069 = relay.TupleGetItem(func_3051_call(), 0)
call_3070 = relay.TupleGetItem(func_3052_call(), 0)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_3106 = relay.TupleGetItem(func_465_call(), 1)
call_3107 = relay.TupleGetItem(func_467_call(), 1)
func_1631_call = mod.get_global_var('func_1631')
func_1632_call = mutated_mod.get_global_var('func_1632')
call_3109 = relay.TupleGetItem(func_1631_call(), 1)
call_3110 = relay.TupleGetItem(func_1632_call(), 1)
func_2404_call = mod.get_global_var('func_2404')
func_2407_call = mutated_mod.get_global_var('func_2407')
var_3115 = relay.var("var_3115", dtype = "float32", shape = (540,))#candidate|3115|(540,)|var|float32
call_3114 = relay.TupleGetItem(func_2404_call(relay.reshape(var_3115.astype('float32'), [12, 5, 9]), relay.reshape(call_3069.astype('float32'), [1260,]), ), 0)
call_3116 = relay.TupleGetItem(func_2407_call(relay.reshape(var_3115.astype('float32'), [12, 5, 9]), relay.reshape(call_3069.astype('float32'), [1260,]), ), 0)
func_2972_call = mod.get_global_var('func_2972')
func_2974_call = mutated_mod.get_global_var('func_2974')
call_3138 = func_2972_call()
call_3139 = func_2972_call()
bop_3155 = relay.power(call_3114.astype('float64'), relay.reshape(var_3115.astype('float64'), relay.shape_of(call_3114))) # shape=(12, 5, 9)
bop_3158 = relay.power(call_3116.astype('float64'), relay.reshape(var_3115.astype('float64'), relay.shape_of(call_3116))) # shape=(12, 5, 9)
func_610_call = mod.get_global_var('func_610')
func_613_call = mutated_mod.get_global_var('func_613')
const_3168 = relay.const([5.353717,5.090779,6.811231,-7.470638,-6.901130,-2.243246,7.473226,-2.835906,8.185498,6.458597,8.370685,-1.142798,1.693404,1.850973,-9.205356,-8.443040,-2.120941,-4.652199,2.193169,-4.126686,-1.887294,-4.115549,5.051246,6.518799,7.259117,-4.164027,-2.779786,-0.105809,-4.983391,-2.362626,8.586327,-4.166667,-5.307246,3.323573,-6.673895,7.699519,-3.882966,-5.477767,2.774967,3.766211,-7.557085,4.802435,-2.226830,-2.293647,-9.720532,-0.435403,7.705307,0.189427,1.176793,-4.433148,-2.324082,-1.937625,4.595416,1.033022,2.689144,-6.418305,-1.233997,-0.064512,2.204702,3.193665,3.518639,-9.193127,8.930087,5.669525,-5.866396,-3.199247,2.101505,-0.536181,2.069836,9.013151,-6.276120,-8.888549,-4.048722,5.596595,4.278923,7.124864,-7.755719,9.536419,0.231018,8.908702,-3.201985,7.772491,-5.259372,1.521722,1.335903,-2.542123,-9.151799,-6.740827,2.979408,-0.422606,8.608108,-2.120116,1.006831,7.445144,-0.902713,4.443815,-1.778757,-0.932265,-7.622058,-7.137264,8.709919,6.416493,0.919479,-3.827681,6.721183,5.114367,-3.478618,5.455730,3.660648,-2.873010,8.499193,9.686372,-0.394803,-8.656810,3.765336,-4.522371,-2.290202,-0.687461,-9.644419,-8.950458,9.485765,-5.562606,0.772443,-9.797994,-8.988310,-5.021811,-7.269262,6.890853,-1.761549,2.020585,-4.365296,-9.978482,4.600258,-4.408302,3.058612,8.593799,-6.182192,-5.260416,1.411580,-9.132211,6.939489,1.558739,-5.948221,4.956246,7.397544,-6.913554,-6.631492,-9.234698,5.219960,1.983042,0.437171,-2.962417,-6.546852,-4.536635,0.397047,1.637956,6.900519,-5.988844,3.499608,-1.704818,-1.412349,-2.081577,7.025111,-4.160342,2.798722,3.005685,-4.277221,-2.264062,-6.123870,3.027404,-5.908388,0.484705,1.774363,7.986357,0.030094], dtype = "float64")#candidate|3168|(175,)|const|float64
call_3167 = relay.TupleGetItem(func_610_call(relay.reshape(const_3168.astype('float64'), [5, 7, 5])), 1)
call_3169 = relay.TupleGetItem(func_613_call(relay.reshape(const_3168.astype('float64'), [5, 7, 5])), 1)
func_2022_call = mod.get_global_var('func_2022')
func_2024_call = mutated_mod.get_global_var('func_2024')
call_3187 = relay.TupleGetItem(func_2022_call(relay.reshape(call_3069.astype('float32'), [10, 9, 14])), 0)
call_3188 = relay.TupleGetItem(func_2024_call(relay.reshape(call_3069.astype('float32'), [10, 9, 14])), 0)
output = relay.Tuple([call_3069,call_3106,call_3109,call_3138,bop_3155,call_3167,const_3168,call_3187,])
output2 = relay.Tuple([call_3070,call_3107,call_3110,call_3139,bop_3158,call_3169,const_3168,call_3188,])
func_3189 = relay.Function([var_3115,], output)
mod['func_3189'] = func_3189
mod = relay.transform.InferType()(mod)
mutated_mod['func_3189'] = func_3189
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3190 = relay.var("var_3190", dtype = "float32", shape = (540,))#candidate|3190|(540,)|var|float32
func_3189_call = mutated_mod.get_global_var('func_3189')
call_3191 = func_3189_call(var_3190)
output = call_3191
func_3192 = relay.Function([var_3190], output)
mutated_mod['func_3192'] = func_3192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1083_call = mod.get_global_var('func_1083')
func_1084_call = mutated_mod.get_global_var('func_1084')
call_3240 = relay.TupleGetItem(func_1083_call(), 0)
call_3241 = relay.TupleGetItem(func_1084_call(), 0)
func_169_call = mod.get_global_var('func_169')
func_174_call = mutated_mod.get_global_var('func_174')
call_3253 = relay.TupleGetItem(func_169_call(relay.reshape(call_3240.astype('float32'), [10, 9, 14]), relay.reshape(call_3240.astype('float32'), [10, 9, 14]), relay.reshape(call_3240.astype('bool'), [10, 9, 14]), ), 1)
call_3254 = relay.TupleGetItem(func_174_call(relay.reshape(call_3240.astype('float32'), [10, 9, 14]), relay.reshape(call_3240.astype('float32'), [10, 9, 14]), relay.reshape(call_3240.astype('bool'), [10, 9, 14]), ), 1)
output = relay.Tuple([call_3240,call_3253,])
output2 = relay.Tuple([call_3241,call_3254,])
func_3279 = relay.Function([], output)
mod['func_3279'] = func_3279
mod = relay.transform.InferType()(mod)
output = func_3279()
func_3280 = relay.Function([], output)
mutated_mod['func_3280'] = func_3280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2849_call = mod.get_global_var('func_2849')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_3357 = func_2849_call()
call_3358 = func_2849_call()
output = call_3357
output2 = call_3358
func_3359 = relay.Function([], output)
mod['func_3359'] = func_3359
mod = relay.transform.InferType()(mod)
mutated_mod['func_3359'] = func_3359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3359_call = mutated_mod.get_global_var('func_3359')
call_3360 = func_3359_call()
output = call_3360
func_3361 = relay.Function([], output)
mutated_mod['func_3361'] = func_3361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3279_call = mod.get_global_var('func_3279')
func_3280_call = mutated_mod.get_global_var('func_3280')
call_3400 = relay.TupleGetItem(func_3279_call(), 0)
call_3401 = relay.TupleGetItem(func_3280_call(), 0)
output = call_3400
output2 = call_3401
func_3407 = relay.Function([], output)
mod['func_3407'] = func_3407
mod = relay.transform.InferType()(mod)
output = func_3407()
func_3408 = relay.Function([], output)
mutated_mod['func_3408'] = func_3408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_3429 = func_2428_call()
call_3430 = func_2428_call()
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_3441 = func_876_call()
call_3442 = func_876_call()
func_1331_call = mod.get_global_var('func_1331')
func_1334_call = mutated_mod.get_global_var('func_1334')
const_3451 = relay.const([7,-9,-1,-9,5,-1,-6,-5,7,2,5,8,4,-5,-3,6,-6,-9,1,-2,-5,5,8,-8,10,-10,-7,6,-6,-8,-9,-7,1,-2,3,-9,6,2,3,-1,-1,9,-9,9,8,-2,-4,-4,4,9,9,-8,1,-3,9,9,-4,7,-5,-7,-6,10,10,6,9,3,-5,-4,-10,-1,10,-8,8,8,-4,8,3,-1,-1,9,4,9,3,-4,-2,-2,4,-7,-9,-10,9,4,-6,-7,2,7,7,3,-9,1,-1,4,-4,2,7,8,-7,-1,5,-10,-3,-3,2,10,-3,5,-7,1,-1,7,-4,5,5,-6,4,-7,2,-9,6,-6,-4,2,1,3,8,-9,2,6,9,-8,-8,10,-7,-4,10,-9,-2,-6,-6,-4,-6,9,-6,7,-8,8,2,-8,1,-1,4,7,-2,-7,-1,-5,4,7,2,7,9,-8,7,1,9,-9,1,-9,9,1,8,7,1,-4,-7,5,-8,8,-10,-3,10,-2,-10,-4,-8,8,-5,8,8,9,2,-3,6,8,-2,-4,3,-3,-8,1], dtype = "uint64")#candidate|3451|(210,)|const|uint64
call_3450 = relay.TupleGetItem(func_1331_call(relay.reshape(const_3451.astype('uint64'), [10, 7, 3])), 1)
call_3452 = relay.TupleGetItem(func_1334_call(relay.reshape(const_3451.astype('uint64'), [10, 7, 3])), 1)
output = relay.Tuple([call_3429,call_3441,call_3450,const_3451,])
output2 = relay.Tuple([call_3430,call_3442,call_3452,const_3451,])
func_3461 = relay.Function([], output)
mod['func_3461'] = func_3461
mod = relay.transform.InferType()(mod)
mutated_mod['func_3461'] = func_3461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3461_call = mutated_mod.get_global_var('func_3461')
call_3462 = func_3461_call()
output = call_3462
func_3463 = relay.Function([], output)
mutated_mod['func_3463'] = func_3463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2203_call = mod.get_global_var('func_2203')
func_2205_call = mutated_mod.get_global_var('func_2205')
call_3478 = relay.TupleGetItem(func_2203_call(), 0)
call_3479 = relay.TupleGetItem(func_2205_call(), 0)
output = relay.Tuple([call_3478,])
output2 = relay.Tuple([call_3479,])
func_3489 = relay.Function([], output)
mod['func_3489'] = func_3489
mod = relay.transform.InferType()(mod)
output = func_3489()
func_3490 = relay.Function([], output)
mutated_mod['func_3490'] = func_3490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_876_call = mod.get_global_var('func_876')
func_878_call = mutated_mod.get_global_var('func_878')
call_3504 = func_876_call()
call_3505 = func_876_call()
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_3508 = relay.TupleGetItem(func_252_call(), 0)
call_3509 = relay.TupleGetItem(func_254_call(), 0)
func_2572_call = mod.get_global_var('func_2572')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_3514 = relay.TupleGetItem(func_2572_call(), 0)
call_3515 = relay.TupleGetItem(func_2574_call(), 0)
output = relay.Tuple([call_3504,call_3508,call_3514,])
output2 = relay.Tuple([call_3505,call_3509,call_3515,])
func_3520 = relay.Function([], output)
mod['func_3520'] = func_3520
mod = relay.transform.InferType()(mod)
output = func_3520()
func_3521 = relay.Function([], output)
mutated_mod['func_3521'] = func_3521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2849_call = mod.get_global_var('func_2849')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_3598 = func_2849_call()
call_3599 = func_2849_call()
var_3604 = relay.var("var_3604", dtype = "float32", shape = (12, 3, 8))#candidate|3604|(12, 3, 8)|var|float32
bop_3605 = relay.divide(call_3598.astype('float64'), relay.reshape(var_3604.astype('float64'), relay.shape_of(call_3598))) # shape=(12, 3, 8)
bop_3608 = relay.divide(call_3599.astype('float64'), relay.reshape(var_3604.astype('float64'), relay.shape_of(call_3599))) # shape=(12, 3, 8)
output = bop_3605
output2 = bop_3608
func_3613 = relay.Function([var_3604,], output)
mod['func_3613'] = func_3613
mod = relay.transform.InferType()(mod)
mutated_mod['func_3613'] = func_3613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3614 = relay.var("var_3614", dtype = "float32", shape = (12, 3, 8))#candidate|3614|(12, 3, 8)|var|float32
func_3613_call = mutated_mod.get_global_var('func_3613')
call_3615 = func_3613_call(var_3614)
output = call_3615
func_3616 = relay.Function([var_3614], output)
mutated_mod['func_3616'] = func_3616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_3629 = relay.TupleGetItem(func_465_call(), 1)
call_3630 = relay.TupleGetItem(func_467_call(), 1)
output = call_3629
output2 = call_3630
func_3635 = relay.Function([], output)
mod['func_3635'] = func_3635
mod = relay.transform.InferType()(mod)
mutated_mod['func_3635'] = func_3635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3635_call = mutated_mod.get_global_var('func_3635')
call_3636 = func_3635_call()
output = call_3636
func_3637 = relay.Function([], output)
mutated_mod['func_3637'] = func_3637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2817_call = mutated_mod.get_global_var('func_2817')
call_3705 = relay.TupleGetItem(func_2815_call(), 0)
call_3706 = relay.TupleGetItem(func_2817_call(), 0)
output = call_3705
output2 = call_3706
func_3715 = relay.Function([], output)
mod['func_3715'] = func_3715
mod = relay.transform.InferType()(mod)
output = func_3715()
func_3716 = relay.Function([], output)
mutated_mod['func_3716'] = func_3716
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3728 = relay.var("var_3728", dtype = "float64", shape = (2, 12, 10))#candidate|3728|(2, 12, 10)|var|float64
uop_3729 = relay.sin(var_3728.astype('float64')) # shape=(2, 12, 10)
func_513_call = mod.get_global_var('func_513')
func_516_call = mutated_mod.get_global_var('func_516')
const_3735 = relay.const(-10, dtype = "int8")#candidate|3735|()|const|int8
var_3736 = relay.var("var_3736", dtype = "int8", shape = (351, 1))#candidate|3736|(351, 1)|var|int8
call_3734 = func_513_call(relay.reshape(const_3735.astype('int8'), []), relay.reshape(var_3736.astype('int8'), [13, 9, 3]), )
call_3737 = func_513_call(relay.reshape(const_3735.astype('int8'), []), relay.reshape(var_3736.astype('int8'), [13, 9, 3]), )
func_2815_call = mod.get_global_var('func_2815')
func_2817_call = mutated_mod.get_global_var('func_2817')
call_3738 = relay.TupleGetItem(func_2815_call(), 1)
call_3739 = relay.TupleGetItem(func_2817_call(), 1)
output = relay.Tuple([uop_3729,call_3734,const_3735,var_3736,call_3738,])
output2 = relay.Tuple([uop_3729,call_3737,const_3735,var_3736,call_3739,])
func_3748 = relay.Function([var_3728,var_3736,], output)
mod['func_3748'] = func_3748
mod = relay.transform.InferType()(mod)
mutated_mod['func_3748'] = func_3748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3748_call = mutated_mod.get_global_var('func_3748')
var_3750 = relay.var("var_3750", dtype = "float64", shape = (2, 12, 10))#candidate|3750|(2, 12, 10)|var|float64
var_3751 = relay.var("var_3751", dtype = "int8", shape = (351, 1))#candidate|3751|(351, 1)|var|int8
call_3749 = func_3748_call(var_3750,var_3751,)
output = call_3749
func_3752 = relay.Function([var_3750,var_3751,], output)
mutated_mod['func_3752'] = func_3752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mod.get_global_var('func_2572')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_3812 = relay.TupleGetItem(func_2572_call(), 0)
call_3813 = relay.TupleGetItem(func_2574_call(), 0)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_3818 = relay.TupleGetItem(func_909_call(), 3)
call_3819 = relay.TupleGetItem(func_910_call(), 3)
func_3715_call = mod.get_global_var('func_3715')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_3824 = func_3715_call()
call_3825 = func_3715_call()
func_2963_call = mod.get_global_var('func_2963')
func_2966_call = mutated_mod.get_global_var('func_2966')
call_3840 = relay.TupleGetItem(func_2963_call(relay.reshape(call_3824.astype('float64'), [10, 9, 14])), 0)
call_3841 = relay.TupleGetItem(func_2966_call(relay.reshape(call_3824.astype('float64'), [10, 9, 14])), 0)
output = relay.Tuple([call_3812,call_3818,call_3824,call_3840,])
output2 = relay.Tuple([call_3813,call_3819,call_3825,call_3841,])
func_3848 = relay.Function([], output)
mod['func_3848'] = func_3848
mod = relay.transform.InferType()(mod)
mutated_mod['func_3848'] = func_3848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3848_call = mutated_mod.get_global_var('func_3848')
call_3849 = func_3848_call()
output = call_3849
func_3850 = relay.Function([], output)
mutated_mod['func_3850'] = func_3850
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3871 = relay.const([[[-7,5],[7,1],[-10,-10],[-7,-3],[3,-8]],[[-9,-2],[8,7],[-5,-3],[6,-6],[5,-3]],[[-10,-7],[-5,7],[-6,-9],[-10,9],[6,7]],[[1,-4],[9,1],[7,-8],[-6,6],[-5,9]],[[10,4],[8,-9],[7,6],[7,8],[7,-9]],[[-5,1],[-9,-3],[10,6],[10,1],[3,-4]]], dtype = "uint64")#candidate|3871|(6, 5, 2)|const|uint64
var_3872 = relay.var("var_3872", dtype = "uint64", shape = (6, 5, 2))#candidate|3872|(6, 5, 2)|var|uint64
bop_3873 = relay.less_equal(const_3871.astype('bool'), relay.reshape(var_3872.astype('bool'), relay.shape_of(const_3871))) # shape=(6, 5, 2)
func_1163_call = mod.get_global_var('func_1163')
func_1166_call = mutated_mod.get_global_var('func_1166')
var_3879 = relay.var("var_3879", dtype = "float64", shape = (1, 1260))#candidate|3879|(1, 1260)|var|float64
call_3878 = relay.TupleGetItem(func_1163_call(relay.reshape(var_3879.astype('float64'), [10, 9, 14])), 0)
call_3880 = relay.TupleGetItem(func_1166_call(relay.reshape(var_3879.astype('float64'), [10, 9, 14])), 0)
bop_3881 = relay.floor_divide(bop_3873.astype('float32'), relay.reshape(var_3872.astype('float32'), relay.shape_of(bop_3873))) # shape=(6, 5, 2)
uop_3886 = relay.sigmoid(var_3872.astype('float32')) # shape=(6, 5, 2)
output = relay.Tuple([call_3878,var_3879,bop_3881,uop_3886,])
output2 = relay.Tuple([call_3880,var_3879,bop_3881,uop_3886,])
func_3889 = relay.Function([var_3872,var_3879,], output)
mod['func_3889'] = func_3889
mod = relay.transform.InferType()(mod)
var_3890 = relay.var("var_3890", dtype = "uint64", shape = (6, 5, 2))#candidate|3890|(6, 5, 2)|var|uint64
var_3891 = relay.var("var_3891", dtype = "float64", shape = (1, 1260))#candidate|3891|(1, 1260)|var|float64
output = func_3889(var_3890,var_3891,)
func_3892 = relay.Function([var_3890,var_3891,], output)
mutated_mod['func_3892'] = func_3892
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3899 = relay.var("var_3899", dtype = "float32", shape = (13, 15, 6))#candidate|3899|(13, 15, 6)|var|float32
uop_3900 = relay.asin(var_3899.astype('float32')) # shape=(13, 15, 6)
var_3916 = relay.var("var_3916", dtype = "float32", shape = (13, 15, 6))#candidate|3916|(13, 15, 6)|var|float32
bop_3917 = relay.maximum(var_3899.astype('int32'), relay.reshape(var_3916.astype('int32'), relay.shape_of(var_3899))) # shape=(13, 15, 6)
output = relay.Tuple([uop_3900,bop_3917,])
output2 = relay.Tuple([uop_3900,bop_3917,])
func_3920 = relay.Function([var_3899,var_3916,], output)
mod['func_3920'] = func_3920
mod = relay.transform.InferType()(mod)
mutated_mod['func_3920'] = func_3920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3920_call = mutated_mod.get_global_var('func_3920')
var_3922 = relay.var("var_3922", dtype = "float32", shape = (13, 15, 6))#candidate|3922|(13, 15, 6)|var|float32
var_3923 = relay.var("var_3923", dtype = "float32", shape = (13, 15, 6))#candidate|3923|(13, 15, 6)|var|float32
call_3921 = func_3920_call(var_3922,var_3923,)
output = call_3921
func_3924 = relay.Function([var_3922,var_3923,], output)
mutated_mod['func_3924'] = func_3924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3520_call = mod.get_global_var('func_3520')
func_3521_call = mutated_mod.get_global_var('func_3521')
call_3944 = relay.TupleGetItem(func_3520_call(), 0)
call_3945 = relay.TupleGetItem(func_3521_call(), 0)
output = call_3944
output2 = call_3945
func_3977 = relay.Function([], output)
mod['func_3977'] = func_3977
mod = relay.transform.InferType()(mod)
mutated_mod['func_3977'] = func_3977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3977_call = mutated_mod.get_global_var('func_3977')
call_3978 = func_3977_call()
output = call_3978
func_3979 = relay.Function([], output)
mutated_mod['func_3979'] = func_3979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2972_call = mod.get_global_var('func_2972')
func_2974_call = mutated_mod.get_global_var('func_2974')
call_3999 = func_2972_call()
call_4000 = func_2972_call()
output = call_3999
output2 = call_4000
func_4030 = relay.Function([], output)
mod['func_4030'] = func_4030
mod = relay.transform.InferType()(mod)
mutated_mod['func_4030'] = func_4030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4030_call = mutated_mod.get_global_var('func_4030')
call_4031 = func_4030_call()
output = call_4031
func_4032 = relay.Function([], output)
mutated_mod['func_4032'] = func_4032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3044_call = mod.get_global_var('func_3044')
func_3045_call = mutated_mod.get_global_var('func_3045')
call_4043 = func_3044_call()
call_4044 = func_3044_call()
output = call_4043
output2 = call_4044
func_4054 = relay.Function([], output)
mod['func_4054'] = func_4054
mod = relay.transform.InferType()(mod)
output = func_4054()
func_4055 = relay.Function([], output)
mutated_mod['func_4055'] = func_4055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_4120 = relay.TupleGetItem(func_252_call(), 2)
call_4121 = relay.TupleGetItem(func_254_call(), 2)
output = call_4120
output2 = call_4121
func_4137 = relay.Function([], output)
mod['func_4137'] = func_4137
mod = relay.transform.InferType()(mod)
mutated_mod['func_4137'] = func_4137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4137_call = mutated_mod.get_global_var('func_4137')
call_4138 = func_4137_call()
output = call_4138
func_4139 = relay.Function([], output)
mutated_mod['func_4139'] = func_4139
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4147 = relay.const([[[4,3,-9,7,5,-7,-6,-6],[-10,-6,8,-2,7,-5,-6,8],[6,5,-10,-1,-4,3,-3,-8],[4,5,-10,-7,8,5,5,-5]],[[-7,-10,5,-3,10,-8,-5,-5],[10,2,-4,-8,3,8,7,10],[-4,-10,-2,7,-8,-6,-1,3],[10,3,4,-8,-5,6,-8,7]],[[-9,-10,-1,-6,9,-4,-10,2],[-2,-3,6,-3,8,4,-10,-7],[-9,3,-1,1,-10,10,9,1],[7,-8,-5,-6,4,8,-1,6]],[[-9,2,-7,-2,5,6,-4,-7],[-1,3,-10,9,-1,10,2,-3],[-5,3,-5,7,-6,8,-8,-10],[2,4,-4,-7,-4,8,3,8]],[[-6,9,7,3,-1,-3,6,9],[-1,-1,8,2,5,7,-9,7],[8,-9,6,-10,3,-5,9,10],[-6,6,8,-7,6,-2,-1,-10]],[[-7,-5,3,9,9,6,5,-9],[-6,7,1,-5,-8,-1,8,-9],[2,-9,9,10,9,7,1,-4],[-9,9,5,-6,-2,5,8,-6]],[[-7,-5,10,-4,1,-2,-7,9],[9,5,-3,10,-8,7,8,8],[8,-4,9,7,1,-4,8,-4],[3,-5,-2,4,-10,8,4,-7]],[[-1,1,1,2,5,-10,-9,-2],[-6,9,-1,-10,1,1,3,-8],[-9,4,6,9,4,-6,6,5],[4,3,-4,6,-8,5,-5,8]]], dtype = "int8")#candidate|4147|(8, 4, 8)|const|int8
const_4148 = relay.const([[[3,-6,-1,3,-6,-8,-1,8],[-5,-9,9,6,-1,-1,7,6],[5,10,-1,-8,10,-9,-9,4],[-1,-2,2,-8,-6,-7,-4,-3]],[[-5,4,6,4,-10,-6,2,-6],[7,-5,-6,4,-3,-7,6,-5],[4,8,3,-5,-4,5,-3,1],[9,-10,9,8,-7,-7,6,-3]],[[-3,-10,2,9,-8,-6,-5,2],[-2,-8,-8,-1,3,5,1,-10],[10,1,5,10,6,4,-2,5],[1,-3,2,-4,-3,2,9,-8]],[[-2,-1,-9,-2,-6,6,5,1],[5,-6,9,1,1,8,7,-8],[-5,8,9,-10,-8,-2,8,-2],[-7,-1,8,-10,5,-10,-4,-1]],[[-9,-4,9,-3,10,2,1,2],[-2,-4,-3,1,2,10,2,-4],[10,-9,-4,8,2,-6,3,10],[-1,6,-9,-3,10,5,-3,-3]],[[1,-4,8,2,1,10,-6,-9],[-5,2,-4,4,-8,-6,-2,-8],[4,-9,-3,2,-9,-7,-5,3],[-9,-3,-3,7,-8,4,5,-2]],[[-3,1,1,9,-6,-6,-1,10],[-7,-5,1,-2,8,-8,10,-1],[-10,9,6,3,4,-4,2,7],[8,-10,5,-8,7,-3,4,2]],[[-8,5,-10,-7,-2,9,4,3],[-7,1,-2,2,-4,8,1,-4],[-10,-3,9,-3,1,-5,8,-7],[9,-9,-6,10,-8,-10,8,-9]]], dtype = "int8")#candidate|4148|(8, 4, 8)|const|int8
bop_4149 = relay.minimum(const_4147.astype('int8'), relay.reshape(const_4148.astype('int8'), relay.shape_of(const_4147))) # shape=(8, 4, 8)
output = relay.Tuple([bop_4149,])
output2 = relay.Tuple([bop_4149,])
func_4157 = relay.Function([], output)
mod['func_4157'] = func_4157
mod = relay.transform.InferType()(mod)
output = func_4157()
func_4158 = relay.Function([], output)
mutated_mod['func_4158'] = func_4158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1687_call = mod.get_global_var('func_1687')
func_1688_call = mutated_mod.get_global_var('func_1688')
call_4182 = relay.TupleGetItem(func_1687_call(), 0)
call_4183 = relay.TupleGetItem(func_1688_call(), 0)
output = relay.Tuple([call_4182,])
output2 = relay.Tuple([call_4183,])
func_4184 = relay.Function([], output)
mod['func_4184'] = func_4184
mod = relay.transform.InferType()(mod)
mutated_mod['func_4184'] = func_4184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4184_call = mutated_mod.get_global_var('func_4184')
call_4185 = func_4184_call()
output = call_4185
func_4186 = relay.Function([], output)
mutated_mod['func_4186'] = func_4186
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4268 = relay.var("var_4268", dtype = "float64", shape = (15, 9, 1))#candidate|4268|(15, 9, 1)|var|float64
const_4269 = relay.const([[[5.177143,4.396433,2.276502,-3.303285,-8.585721,8.506977,-1.152295,-4.609706,-5.567034,-6.250609,4.637442],[1.722573,8.662824,9.435176,5.852275,-5.655198,-9.985467,5.929724,0.112935,1.025309,-1.021725,-4.204479],[-8.806810,3.395997,0.550619,-5.639452,8.964665,-3.334282,2.842266,6.913792,-8.382847,-4.587666,-8.976208],[-8.502561,7.677829,9.702307,2.584602,1.389602,-1.295227,-9.589662,-8.127570,3.930863,7.115093,-9.727109],[7.021955,3.628109,8.098822,0.508981,3.213397,-5.439402,1.635769,4.917857,3.343288,-0.038278,9.221449],[-7.229815,-4.286161,0.549135,7.118461,-6.981372,3.463724,-8.663392,2.326373,-9.192058,-5.728153,-8.862303],[7.116929,-4.242476,-8.791378,-6.477441,5.331710,6.638030,-2.776611,0.432377,2.188095,2.665625,0.084815],[3.882001,9.317845,-3.670561,-7.670834,1.184995,-4.133419,4.868314,9.600651,-9.243615,-3.206923,-9.557200],[-9.410604,-6.488158,6.288919,-4.138397,6.088438,-8.942330,-0.397690,-9.041527,0.795327,-3.187591,1.881982]],[[-9.209680,5.324964,-7.186247,-4.777720,2.503224,-5.972276,-0.487119,2.581539,4.397133,0.688513,1.260036],[-8.025138,-4.973383,9.616074,6.067212,-5.523122,2.983473,-1.062455,6.370332,-8.791920,2.485571,-0.511263],[1.170713,-0.686288,8.680533,-8.992384,8.708325,-4.365673,-8.687865,-5.309148,5.778431,4.422179,7.359682],[-1.635493,-7.607892,9.882978,1.027882,-6.406627,4.665898,7.876979,-4.850292,1.563329,-0.513428,5.098954],[2.145600,-7.170409,1.148845,-3.856782,8.201068,9.699504,8.204501,6.624318,7.176342,0.743202,8.343241],[1.442455,-8.737767,2.226099,-3.612017,1.869111,5.353165,-2.621820,4.724338,0.923612,5.374061,2.291673],[3.320952,-9.399760,-5.112850,3.118818,-8.356464,1.124042,4.752788,-1.427356,1.954021,7.057654,8.615388],[2.958556,-4.032889,-8.540639,-6.129397,7.517862,-9.949136,-2.510517,3.909317,-8.993769,-5.132390,1.942331],[9.414953,9.629807,7.654533,6.475998,8.987774,-4.231291,9.625494,1.243082,-9.543470,7.553475,-7.583076]],[[3.763731,7.946873,-1.885761,8.791647,5.466321,9.390584,4.919040,6.806304,2.936723,-1.169991,7.905178],[-3.746700,6.803757,5.104000,-2.004731,-5.812746,9.263972,6.859752,7.269858,7.105884,1.328303,9.619052],[-0.026183,1.872251,8.941393,1.536233,6.465029,-0.025189,-7.523642,9.181943,0.163609,-6.551156,3.599997],[-9.023662,-4.760384,9.820224,-7.957281,-5.512819,-6.016265,8.435388,5.763221,-1.893463,-9.271209,8.251290],[-9.106633,3.866019,-6.221493,-5.200362,-3.003191,-4.850388,9.734095,-7.112889,9.213060,-2.094652,9.067496],[7.109997,-0.030819,5.256892,-6.982400,0.689165,-6.885388,1.290152,-3.270168,-8.973606,-1.111059,5.387186],[9.234145,-6.513527,-7.163117,-4.123389,-3.414724,3.172131,7.162280,0.416749,4.484936,-4.240919,-1.817489],[9.028594,1.655074,8.085385,-9.609405,5.853009,-4.798575,-6.929166,-3.607996,-9.195954,3.828908,4.173768],[3.401442,-0.914116,8.433021,-6.735360,-3.029393,-7.797471,7.889905,-0.696022,-2.490186,3.476318,0.796408]],[[-3.929580,-9.872184,-6.766760,-3.325129,-4.548085,-1.387555,-1.470461,5.294540,8.801356,-7.009874,-0.983010],[9.632891,-6.709683,-8.710338,2.356036,3.584198,-8.071771,-2.467509,1.165708,-0.033135,-5.700445,4.681171],[9.796999,5.782485,-1.445019,-1.411207,-6.794752,6.485289,-7.474877,-1.544608,0.356400,9.671164,-9.004340],[-0.221676,-4.697577,0.803477,-4.400129,0.117053,-4.223138,-7.962939,6.253388,8.121460,6.155102,-6.858222],[-2.308459,0.884757,-7.499371,5.495904,-3.976240,2.363267,9.045119,-1.754570,8.846781,8.825449,-5.271714],[-5.409078,-0.902433,7.543650,3.483707,6.599441,3.765975,4.406230,2.586555,-2.043300,6.157986,-7.216750],[-5.620554,-2.825312,1.622097,9.877530,8.391812,1.512719,7.410275,5.866139,-4.634407,3.866737,2.906727],[9.168388,8.528596,2.101310,4.995746,9.461059,-1.712118,4.372310,4.357543,2.861892,9.814650,9.354859],[-4.016954,9.591368,0.760205,-3.694614,1.868420,-2.930221,6.954643,7.566512,6.362105,-5.486340,-0.232978]],[[3.579712,6.440342,2.730096,9.033880,2.559169,0.861627,-0.383881,4.981224,-6.720425,8.149516,-4.340613],[-8.175099,7.725392,-0.034941,0.496068,-9.996783,8.252070,1.346389,-2.986442,2.647927,-6.634911,-8.746802],[4.639305,3.736230,-1.046991,-3.695723,0.298278,2.734565,3.675647,2.760624,-2.609011,9.397640,5.557331],[-5.803418,-9.723105,0.765473,2.941715,3.580464,-9.921175,-6.022060,8.474151,7.143678,3.006471,-8.333993],[-5.870556,7.108070,2.294097,-2.366999,7.184592,-3.979421,-7.266381,1.808886,9.155108,3.297219,7.314291],[-4.140977,-6.013241,-2.632425,-5.386391,-6.984601,-1.417543,-6.372024,1.145129,-5.955302,1.046948,-3.516145],[-9.877252,2.128381,-8.722499,8.475178,-5.400723,0.224037,6.670346,-3.693672,-4.612076,3.653773,-1.667276],[-9.784130,-3.615465,6.326918,2.116808,-4.844692,4.485392,7.679365,-2.398786,9.096956,-9.481057,5.533252],[-1.711677,-0.434884,4.510973,8.485878,5.317366,3.745367,-0.397427,2.964021,-1.411202,-1.479071,-5.986298]],[[0.889812,-8.920290,5.482509,3.649262,1.768546,7.428486,-9.443327,0.084415,-2.158863,6.913756,-4.446756],[-5.434036,2.939180,3.447109,-9.080745,1.418699,-8.363828,2.628391,4.343852,2.658808,-0.908198,-8.687806],[6.157964,7.474533,-8.319534,0.354009,-4.748322,-6.049119,-8.271514,7.517926,9.886445,-4.302078,1.172269],[-3.661864,6.429594,6.014075,-5.835746,-0.099448,9.851832,9.693737,5.679400,-6.246689,0.112602,9.201680],[3.686143,-3.475756,-4.073966,-5.084447,-6.515904,-1.564528,-9.313063,-5.163607,4.367578,-3.547654,-1.323366],[-6.834811,-6.626134,7.934594,6.828850,7.838135,-4.727868,-8.081239,2.371591,-8.344716,2.507014,7.253715],[-8.790243,-0.967557,-4.310882,-6.392310,-9.485627,-4.268061,9.157288,-6.871556,4.727595,5.216746,-0.461207],[-7.925832,7.089902,9.425078,2.660274,-3.621908,-3.662306,4.106708,-0.959785,5.657349,-2.194260,4.968498],[-6.256396,-2.737746,-2.835503,1.095447,6.975103,-4.817562,-1.495559,4.832897,-9.694662,8.096779,-6.213575]],[[0.871927,-3.393416,-3.125717,1.338251,-3.725197,2.646491,8.669092,0.068212,-1.004004,-7.395551,5.625023],[0.521069,-1.486315,-1.005184,-2.457277,-9.117357,2.710877,4.717621,6.425486,-5.655820,-1.188138,-4.159104],[0.463308,-0.826606,4.382156,-5.930097,7.419256,4.471696,3.383044,9.035793,4.728965,2.217556,-8.137903],[-1.271554,7.205718,2.558086,-4.268645,7.963440,6.179514,-4.014866,-2.749936,7.849279,-8.213262,9.712293],[7.729260,1.191365,-0.177346,7.897363,7.950575,-9.101839,-0.058593,-3.324601,-1.888791,-2.228295,1.670218],[-8.280023,9.119465,7.808829,-5.030417,0.319510,5.816030,-1.510070,-5.330587,-5.901471,5.608590,-4.941875],[4.850411,7.661911,7.705602,6.988090,-9.742847,-0.772147,-5.119389,2.586898,5.578244,-4.673383,4.706092],[-7.616852,-3.533764,-7.807309,-3.698999,-3.086722,3.655242,7.278056,7.638928,-1.281952,-6.227326,-1.945142],[-9.879903,5.963454,-7.781957,6.918118,2.336372,1.672014,-7.507403,1.975932,7.858332,-7.324949,5.851781]],[[2.138872,0.495170,-8.613748,-4.003921,-9.223998,-7.420635,-5.032665,1.157600,9.516227,-4.990205,-3.282794],[-6.628271,9.645360,1.064118,-6.541777,0.237671,-5.626801,8.971502,-3.198635,0.390630,5.089306,-7.140699],[-0.839367,7.312137,-8.875211,6.989551,-3.987068,5.477454,9.326557,-8.612077,3.322904,9.843090,-3.118557],[5.532456,-0.700534,9.618767,-4.860807,-3.226374,6.052812,-4.273319,0.170299,-2.493207,5.969837,5.157787],[9.024237,6.299496,6.003538,-5.260865,7.537404,-1.319001,-7.145271,0.340344,2.534657,6.280340,4.466964],[6.235313,6.427457,0.473058,0.057225,6.283715,-1.092785,4.820773,0.912430,9.768056,2.532776,0.415015],[2.115248,6.441909,-1.943520,1.699485,-1.820940,-5.455550,-1.564228,9.710875,-4.388226,-0.702620,3.825885],[-2.247470,0.215693,4.364120,7.498152,-5.356244,-7.634340,0.953690,8.940407,-5.996999,1.661900,6.771656],[-4.630390,4.940503,-9.260574,5.633612,-9.012327,-3.899132,3.897584,-3.530764,-1.965397,9.237201,-7.641911]],[[9.296039,6.990709,-3.852393,-1.472529,4.789550,-2.830564,9.343023,-6.491129,-2.550622,-5.461200,1.119229],[-8.375271,-7.255036,-8.011408,3.997291,5.267176,-0.209608,5.273639,9.824903,2.744567,-3.506209,-8.514564],[-0.089242,1.796840,7.703843,8.512901,2.850496,-1.605750,0.427318,-0.045476,-6.780985,7.956021,-0.623083],[1.023066,9.870963,-1.275707,-3.825627,4.760501,-0.691459,6.305597,3.508504,-2.825385,-6.431372,-5.118586],[0.360614,2.535032,-7.591550,3.977783,6.894160,5.492490,2.691487,-2.742513,-5.571151,-9.757290,-5.580627],[-6.605299,-6.088725,8.848026,4.343381,-7.510249,-8.112123,-1.163479,4.164430,7.108176,-6.964500,2.852807],[9.661979,2.018863,9.617054,-5.942353,1.480162,1.911273,8.893436,6.455487,1.119775,6.898682,3.735426],[-0.258569,3.877721,1.026031,-1.444987,9.216188,-9.118320,1.206421,-7.567779,-4.403059,-0.073018,-4.811930],[-2.939741,1.407741,4.394675,8.245077,-0.430262,3.292765,4.293668,-8.225474,5.588716,9.084588,-7.729422]],[[-9.637197,-9.788460,4.264694,-4.863378,-1.593329,6.476193,-4.097967,8.646212,8.021505,-0.317156,5.709518],[6.685684,2.833720,-2.334180,-2.527784,-3.395312,9.739217,7.101279,0.369464,-0.980514,-4.307794,2.494340],[6.790318,-2.585274,7.728965,5.077837,7.023484,-1.389697,-6.390660,1.742112,6.890009,3.588003,9.817652],[7.214592,-6.109620,-9.943239,9.109257,-0.082635,-9.650792,0.021950,7.926590,1.274140,9.632088,0.131068],[-4.367082,8.560261,-7.402980,-5.313245,8.193243,1.557393,-7.952578,1.925910,2.742844,-1.465870,-7.826311],[9.747494,-6.073829,-3.722263,-0.402878,4.469529,5.202954,0.874977,5.732705,8.031787,4.848430,4.148478],[-8.418566,-7.165993,-6.089098,-7.393351,-2.074208,-3.151171,-7.442452,0.190615,-4.238084,9.903628,6.109035],[-4.998991,-0.324883,4.405781,-9.988813,3.198949,1.033910,-1.519010,-8.655411,4.578805,7.135239,-5.512469],[-0.055396,-9.828840,-5.786204,-2.873321,-7.319210,5.924038,-6.224744,5.713077,1.846304,-5.592000,-5.795140]],[[-9.307886,9.376938,3.902970,0.251345,-9.892385,4.102399,-7.202666,-8.988978,1.675077,9.319265,1.442468],[-4.530266,-7.813647,-6.987855,-4.005033,-8.706798,7.778002,-2.499819,-0.842965,-6.540017,-2.393417,0.543250],[-5.577220,1.429185,1.430206,-9.392312,8.268212,5.243812,-4.709489,-9.956053,-4.814836,2.829258,-9.164379],[-0.762030,8.484647,5.694792,5.794122,-4.993887,-5.816926,2.587144,0.724667,-5.994352,-5.534702,-3.100320],[1.007975,-0.011483,5.674540,-9.613800,7.113070,-4.432779,0.100447,-6.661912,5.864954,-0.975650,4.471272],[3.836253,2.830225,6.919520,0.713778,-7.867015,-3.852332,-3.113202,-9.346930,9.159233,0.725919,-8.038009],[2.635432,4.268939,-3.016631,-5.339574,-0.969837,-4.353365,5.942565,3.811707,7.042433,-5.220566,-9.931417],[-2.266878,3.098224,9.408577,2.511459,9.531391,-7.428392,1.426157,8.384502,-3.647877,1.789891,0.414289],[-1.453428,8.772926,3.000391,7.968626,-0.320304,-6.333467,9.592246,5.636888,-8.122148,4.813835,9.703213]],[[6.949345,-7.669733,-4.885941,-2.568461,1.938531,1.244348,-6.810095,-1.042621,-6.391926,7.206619,-2.624083],[-7.081812,-8.777778,-2.936763,-2.944477,-0.244445,-5.220715,1.459923,5.912119,9.986081,0.618849,7.309964],[3.026902,0.396565,0.368472,-5.650664,-1.178654,9.725319,2.617461,-6.198244,3.777098,4.194073,-1.452017],[1.514895,-3.046995,-6.493434,6.482714,-3.684400,8.154880,-6.589552,-1.790397,-2.264721,-8.988178,7.980304],[4.662480,9.584764,7.638878,6.829272,8.123456,8.650976,5.384875,0.070792,8.085642,3.406233,-4.072429],[2.737896,-8.912997,6.391412,9.202378,9.274685,-8.001804,-9.484448,3.275441,8.981467,-5.278456,4.019857],[-2.698471,-2.123771,-0.512360,-6.610486,5.758940,3.358536,5.873743,-9.893279,-0.125302,-5.079661,-6.616993],[-4.636647,-2.772061,9.681275,-0.625824,-0.843180,6.112674,-7.603911,-8.165506,-2.361940,5.261010,1.741544],[-8.257407,0.759666,7.840862,-1.039886,-8.835212,-5.327062,-5.166212,1.389189,-1.893267,-5.837902,-2.301838]],[[9.535889,5.402705,7.080810,9.735368,-7.445690,-0.196473,-6.634617,6.849874,-7.281699,5.859301,-8.110858],[-7.919714,-9.319327,7.550952,-7.460534,-5.728789,-0.444190,-9.404479,-4.644373,-4.514155,6.618130,-8.568078],[4.426532,-3.148891,-7.019919,-5.033561,-6.004073,-6.047078,5.628268,7.743147,-6.300874,4.697408,1.929891],[-7.879706,1.407456,-9.337056,4.436484,3.508942,-0.438084,-4.638599,6.434210,6.746789,4.002683,8.677034],[4.324072,1.031976,-8.243532,-8.294927,-2.853546,7.647856,-1.194397,-9.613277,-4.962732,-1.762936,-8.072998],[2.334948,9.349698,9.685123,3.322253,3.261523,0.083307,-6.181660,8.163048,7.206036,0.434255,4.571167],[1.320360,2.911817,5.848417,-0.546702,9.234192,-1.400842,4.128775,3.381656,-6.479191,4.907457,0.957075],[6.154371,5.338051,-0.947080,6.019632,-1.824170,-2.567534,-3.756340,8.766152,1.096894,5.639916,9.632268],[0.939582,6.107543,9.450782,3.327265,-1.025642,8.584130,6.931737,-1.991388,9.626224,8.867848,-4.798621]],[[-7.870665,2.017967,-8.866790,2.659072,5.735944,8.413237,-8.171521,2.279881,7.758425,-3.883215,1.847777],[9.485219,-4.574989,-5.741228,-5.476003,5.298108,-3.210210,-9.142833,7.068912,-6.934399,-6.571528,7.917084],[-5.268835,-2.592796,-1.538646,-2.705471,-0.506787,4.474613,4.399951,7.004045,0.626412,-4.203097,7.853337],[-4.588306,-4.521879,1.622802,-9.524321,6.864144,3.672210,8.216397,-6.405373,-0.422205,9.215858,0.972199],[3.920732,-3.141186,5.654571,3.400110,6.851949,-4.618523,-0.317329,-3.728171,-5.345464,-8.673855,5.983493],[-0.916376,8.721741,-3.848483,-5.494575,2.957637,-8.293535,-0.778227,-5.459532,-2.465283,-4.691300,1.830033],[-1.397822,8.730410,0.779326,1.983022,8.939292,-2.184618,-3.036075,1.550196,-1.927712,-2.366414,-2.712408],[4.093163,-5.939682,-5.913023,-1.655901,-7.273759,0.095590,5.440805,3.199906,4.400527,-0.461006,0.693167],[5.396047,-3.588311,-8.578010,-7.508572,0.566464,2.473320,-1.146279,-6.717246,-8.096685,6.564349,9.156870]],[[-4.104636,0.799252,1.832881,-7.873466,-7.045023,-4.438269,5.647942,-1.698347,2.358115,1.838438,0.994324],[5.003164,-0.677233,-0.072557,1.388570,3.887573,-7.649685,-3.956374,-5.239772,5.915618,-4.237991,6.487990],[-9.409791,9.282695,-3.806525,-7.896673,-4.674709,0.070882,7.954027,1.523713,6.914469,3.910334,5.923747],[-4.072680,-1.351381,4.743978,2.274881,-4.614208,-2.624563,5.184843,8.892180,-6.859200,0.654695,-9.653084],[-8.678257,-6.363417,-7.579362,5.535286,8.034625,-3.667619,0.518203,-0.650910,-8.274186,-2.931936,-8.760330],[0.154816,-1.192809,-2.110896,-3.684247,-5.645589,-4.629101,-4.726483,-9.903253,-0.176001,5.347129,0.430015],[-9.770127,9.518360,7.186093,5.174676,-4.152904,3.495402,5.758601,-5.189283,-9.195410,-5.478621,7.426373],[-6.766599,-5.636424,9.345418,3.264230,6.440686,-4.283313,-7.043256,-9.947647,-4.576077,7.492999,4.550759],[5.006483,-2.938779,6.221822,-7.589445,0.029201,-0.423974,3.427654,-2.879839,9.970665,4.243453,-7.925239]]], dtype = "float64")#candidate|4269|(15, 9, 11)|const|float64
bop_4270 = relay.equal(var_4268.astype('bool'), const_4269.astype('bool')) # shape=(15, 9, 11)
uop_4280 = relay.exp(var_4268.astype('float64')) # shape=(15, 9, 1)
func_569_call = mod.get_global_var('func_569')
func_571_call = mutated_mod.get_global_var('func_571')
const_4284 = relay.const([[-5.094545,9.784757,7.484101,0.995193,-7.974286,7.560651,-3.721373,2.797824,-3.853143,2.376860,5.030358,-1.390522,-3.383659,5.216904,4.743386,-3.350615,-1.618993,6.669811,-9.149945,5.928635,7.525696,-6.924669,0.469875,-0.535289,-5.067263,4.229055,7.909324,-0.866081,4.559557,-3.239571,2.600711,5.438012,-2.476048,6.418460,2.350051,-1.338204,6.742421,-6.796458,-4.858144,-9.615532,-9.387009,-5.693786,-3.628859,9.083959,-5.152414,-7.040490,0.847106,9.362983,-4.121900,-6.792526,8.385071,-2.798727,1.766020,7.707970,-1.478963,-4.360280,-0.275584,-8.186044,3.008738,-2.924752,-4.574967,5.078521,-4.152870,3.995088,8.703720,-9.876126,-2.061036,-0.662229,1.280635,5.835420,5.449951,-1.093420,-4.134362,-0.921630,5.199203,-6.956528,3.096278,6.282628,-4.913304,-0.350864,-7.507239,4.950930,-2.944302,-0.618802,6.540055,4.856373,-9.654702,-3.686787,-6.080003,-8.411771,-4.295300,3.358764,6.964901,6.482262,-5.132339,4.211377,8.246592,8.276661,-4.499494,4.567437,-1.054350,1.158198,6.936289,1.752030,-4.901480,4.807259,-9.641688,3.889016,4.457106,-8.168293,-0.934574,-3.587352,-2.609902,8.648054,6.990037,-8.940511,2.031312,-4.414900,-7.156546,9.849594,-9.565296,3.846557,4.483928,-2.158312,0.042354,-0.878578,-4.680285,3.105260,9.914124,-3.284886,-4.285381,-3.647103,-9.510543,-9.605694,-2.995555,3.951193,-4.392011,-6.982177,8.016760,-6.879126],[5.067580,0.415496,5.442579,-5.504549,3.619364,5.191919,8.197945,-6.118869,1.602004,-0.617597,-7.216982,-6.255674,-7.590846,-1.816623,2.196571,4.334405,-8.898692,-3.235423,9.873257,-0.891526,8.873431,-7.169187,6.372484,-6.982704,9.898945,-9.308481,1.574625,-3.477852,8.819025,2.086453,0.625785,5.220934,2.875118,7.553511,-0.186311,-5.926342,-5.363105,1.139829,0.035054,-3.379585,-6.020733,-6.887233,1.108362,-1.529451,0.018630,2.964341,-9.951980,-6.174602,-2.849094,-6.202577,1.387502,0.212851,-6.513961,6.342045,-9.095929,-8.892819,2.806086,-9.544664,-6.787875,0.087004,7.438162,-9.926896,-5.441373,7.725364,1.808053,8.195923,-9.206992,-4.668293,6.545983,-0.012241,7.334102,9.491658,9.269153,7.002873,-3.826567,-6.595090,6.751602,0.093868,1.405728,-6.479531,-0.447515,-0.209589,-3.342378,8.686408,-5.828080,-2.543877,0.959060,-7.489564,0.019763,-8.282035,8.368379,5.501002,1.267762,-0.381036,-3.212014,8.466981,-2.490321,6.183120,-6.990597,5.090464,5.569020,-5.134152,5.864307,7.351178,-4.584220,-0.085509,-3.100211,-0.206018,-5.030646,9.256152,-4.072105,5.860883,-8.738613,7.059863,-6.949916,5.136853,-9.061017,-1.077585,5.526988,3.276679,9.989544,7.020669,2.833337,6.646440,-3.700989,-6.826493,-2.544772,3.079735,8.676152,7.251025,9.691193,8.669059,4.190444,3.176279,5.466312,-9.538990,-4.555268,9.792058,-5.100714,3.515288],[8.200091,2.749974,-3.570974,-5.611032,5.330825,3.130463,-5.055612,8.232592,-5.593822,-6.695363,2.013548,-0.296376,-9.873256,6.280193,-0.199138,0.858565,9.495541,1.499153,-0.365750,8.707065,-5.898905,-3.931674,9.634193,-9.584076,0.600243,5.501939,4.961746,-1.733904,4.557934,-7.419312,1.009079,6.308465,-7.736833,-4.727481,-4.712956,2.999498,-0.008254,-8.083617,1.538636,1.869547,2.089647,1.201206,-9.925472,7.822185,8.681083,7.832255,5.943333,0.103665,-2.003484,-5.048422,8.548139,8.965952,-2.369982,7.868937,-5.369129,-2.225703,-0.771758,-6.255387,8.643258,-6.976334,-8.891509,8.180090,0.488203,2.548590,-7.754892,-7.694508,4.122956,1.727366,6.862847,0.587210,2.094237,-5.362633,8.052166,-6.656934,-6.738920,-6.660095,7.682699,-7.868653,-2.361059,-6.278816,-4.835243,3.989370,-4.564321,2.946196,0.132507,3.486151,-1.387709,-6.156264,-3.841146,-8.524383,-4.509509,3.428316,8.454820,-4.927830,-4.382560,-9.059045,0.132451,-4.426173,7.732253,-2.001993,5.298607,5.593095,0.141833,2.199644,1.856330,-5.208924,-1.977586,1.967119,7.998061,-7.483427,-0.236303,-7.766555,-8.858618,7.622142,-3.904170,-4.725861,8.107861,6.113179,-8.320780,-5.038894,1.440495,5.277104,2.979717,8.994705,-8.178204,-9.307293,-4.545051,-4.777690,3.837972,-5.450015,6.421897,2.897680,8.018884,3.582839,-8.568972,9.081126,-5.928034,8.453396,1.502700,1.509699],[-3.248555,-3.571027,-7.443872,5.039556,-6.906569,-9.601127,1.048314,-6.891857,-3.358202,-3.184222,9.975827,-7.770387,-8.594742,2.562528,-4.634086,7.306892,-0.304720,-9.896211,-7.266257,5.234836,9.778008,7.243772,2.235478,0.871392,9.241696,-5.955357,8.531612,8.222965,7.349223,1.702450,0.986787,-3.810821,-4.594692,-0.668099,7.923838,7.800150,7.109604,6.026932,-7.197054,3.223952,-9.045506,6.878129,-2.549312,5.416482,7.272875,-8.617705,7.019011,4.099795,9.447135,-2.554763,3.651458,7.658637,-1.209461,4.394199,-9.693461,1.850035,3.356999,-4.477929,6.423703,1.838755,8.460803,2.450251,-8.826892,-5.609866,-5.660697,-3.794748,1.616097,5.703044,-9.622988,-6.730521,4.784558,8.445602,-0.100022,-8.701304,6.511816,1.885220,5.554922,9.661227,3.939050,3.717740,1.287230,8.092365,-7.033023,-6.310772,5.554164,3.291092,-0.984834,4.991299,-8.660753,-9.337008,6.594775,-7.467579,-4.193171,6.946904,-4.664088,-8.648273,-6.556244,-5.961955,-3.939959,-7.807154,7.721900,-1.338360,-7.435900,2.008559,9.966427,6.164222,8.119670,-0.623506,9.901528,4.493560,-2.945550,9.733227,4.865065,6.007748,9.907898,9.916369,4.391020,-4.366371,-2.014545,6.884017,-5.232662,-4.210358,-7.303568,5.717447,-2.677780,6.524163,-9.848820,-5.320527,-0.052782,4.473050,0.588239,9.758573,-9.842439,-5.900755,7.402058,9.222016,-3.679435,4.537773,-6.882642,0.071973],[0.556935,4.548558,0.693519,8.716603,-0.416792,3.655360,8.859538,-7.885391,8.172213,-5.809076,-1.068080,-3.700450,-4.514729,-0.363311,-4.798905,1.357749,-5.425953,-1.105142,-5.577835,-0.148842,-1.452516,-8.952920,-7.278254,-3.730495,-2.106295,-8.406024,-0.459333,2.937695,-2.447225,8.941570,9.755034,-5.263026,7.840482,-1.021945,-7.453169,-0.685546,-8.830937,-1.278867,-9.182593,-3.734574,-2.775017,4.265316,6.554693,6.549422,-6.230652,5.859076,8.651705,-7.623436,-3.533998,0.928035,6.243244,8.516905,-9.962868,-7.759720,-8.965762,5.640224,5.122211,1.999481,-3.202423,-8.119942,4.783992,-2.155675,6.499132,-3.005739,6.933523,-5.921711,8.225542,0.537006,7.460329,-9.148665,-5.377054,-4.941247,5.796397,7.943913,-5.198322,-2.417506,6.261078,6.673920,8.735100,-9.524447,8.601974,0.472267,-3.236921,-1.664820,-6.624166,-0.882337,3.184044,-3.680965,-4.790531,-5.871398,9.910266,5.075395,2.868725,7.283366,-8.493495,-9.637456,-2.534338,-4.451688,-6.501012,9.379298,-9.906804,6.667772,-0.371063,-3.706796,1.305026,-7.868278,7.868719,4.063521,-1.014796,-3.530756,-7.368931,-0.742629,-3.556945,-2.828461,5.638538,-5.851513,2.988782,4.083620,6.538435,-0.321597,-5.498678,-3.008039,-4.318210,9.030905,-5.042553,3.695831,-6.783377,-3.243754,8.242403,1.882514,-0.273443,-1.091473,8.650800,3.477649,3.717629,-3.493083,-7.438493,9.654372,-5.672935,1.714869],[-9.923962,-9.976695,-8.043604,-7.230002,6.470204,7.547291,7.377871,9.709344,0.432455,6.479348,-0.919083,3.362899,-3.267924,-3.840056,0.185704,-7.672552,-7.999560,-2.832760,8.589856,-2.287629,-5.434214,-2.249267,6.515622,-0.839759,-9.077475,2.377038,7.867915,-5.402985,-2.139921,8.940063,-7.340302,0.645428,-1.988675,-3.037872,-2.036882,-0.605383,-1.418148,-7.982717,-5.484513,-9.223608,4.599585,3.136647,-8.336878,-7.638898,-0.551182,-9.381448,3.842801,-8.218967,0.043855,4.474922,6.996334,-6.027714,-3.488210,-9.350177,-1.754029,-0.275094,-9.222778,-1.118195,5.020377,3.891915,-3.978048,-7.327561,-2.839540,6.256090,0.161666,3.944736,-6.283300,-8.031133,0.431012,8.535545,-1.166425,6.438797,-3.646331,1.491983,-3.298807,0.059330,3.540886,7.077113,-4.801600,4.442951,0.038973,4.128930,5.761980,3.384456,-2.111554,-7.849613,-8.897672,9.715629,5.691905,-6.430376,-2.784256,3.400895,4.067173,8.173670,1.732338,-2.755849,7.064961,2.046259,7.174181,2.233731,0.489240,-4.574306,1.394284,-0.857707,8.100462,4.304884,9.610084,4.637865,5.723409,-6.765581,3.123273,8.066162,-2.059460,8.478480,5.552761,9.315279,-0.959592,-6.339949,-6.580611,7.685146,8.852800,0.690462,3.064543,-4.160546,5.651839,8.481670,2.895403,9.637706,8.707179,6.490345,-7.262339,-2.467811,2.033490,-3.489854,6.733508,6.489477,-8.436711,4.083483,2.897463,-9.185722],[7.739777,8.862006,0.784528,-1.788694,-4.127960,6.221361,3.907235,5.481862,2.987776,-3.974538,6.352863,1.039368,-8.722143,1.690272,-0.309477,-8.576050,-1.865841,-2.230187,-5.770047,-0.504562,5.018694,1.478683,1.463109,7.777300,7.053757,-3.410132,6.524054,-1.073814,-2.194224,0.401332,-5.355724,-6.408513,7.672167,-1.808359,-4.495696,-5.092563,-0.107990,-5.411736,0.158714,-1.684159,9.906232,7.478998,5.913315,-4.585796,-8.008313,-0.548167,5.858157,5.876107,-9.567707,-0.990354,-4.319696,-2.998666,7.623808,9.550041,-7.409838,4.550894,-0.580917,-7.478771,-3.674498,5.568937,-1.769225,1.064880,6.980861,-8.630427,-6.196297,-9.855633,-8.834957,-3.117570,7.008118,-1.089576,9.021576,5.498462,-3.149735,9.614455,-4.226423,4.198856,0.544332,-4.287473,8.923848,-5.887505,7.203309,0.153610,0.348128,2.501445,3.006609,-3.858284,2.625151,-6.512732,9.621843,8.855461,-5.547246,-1.903331,0.087134,-9.157835,1.031620,2.695008,3.615123,-7.019557,-6.373316,6.767598,8.548245,-2.253448,6.762552,3.040367,1.705371,-4.317736,1.208415,1.336197,4.251332,-2.418854,-6.064226,-3.173688,-8.507179,-3.224753,-0.382783,-1.331545,9.546253,2.343760,8.143277,4.018749,8.265184,-9.423088,-3.129803,7.043065,-6.727419,-6.019466,7.365095,-8.986755,-9.542725,-4.320554,8.758606,-0.797619,-8.115863,4.118289,-1.027124,-0.288783,1.133940,1.409948,-5.337057,1.243671],[-5.669212,4.287196,-2.846743,1.332542,-8.952107,-6.087802,-7.407561,-6.376418,-7.553159,-0.521959,-1.263780,-0.273873,5.987614,8.503775,-2.518944,-5.291741,-7.506037,5.152380,-7.336507,3.170178,-3.762124,-8.601204,7.131382,0.141177,-4.981956,-1.471054,-5.502419,-3.058061,-0.517115,3.248235,0.902146,9.216302,0.703754,-0.469255,6.687422,-4.065639,0.796236,-8.451517,8.223164,-0.219228,1.361547,-9.918668,8.980034,-3.000072,-2.590774,9.309139,8.479023,-8.096486,3.138302,-5.173182,-6.994558,-2.640750,4.085216,-8.739726,2.246133,7.877967,-3.649871,-0.147189,-5.824932,2.807205,4.440949,-0.667755,-4.226623,1.755317,-3.685154,-9.433284,7.779483,-3.869337,-4.923018,3.313535,-0.924464,-1.756147,3.880907,-2.597557,7.815291,-7.276940,-9.662785,-4.414742,0.223396,-7.677586,6.909414,4.193215,-6.602374,-2.717194,-6.430089,-2.980922,-0.911066,9.625358,7.253177,0.962817,-6.303364,3.765325,4.301249,3.344293,-8.600018,-9.326339,-4.019500,-4.815220,1.241482,8.765891,-5.411826,-8.989412,1.524099,-2.198268,-6.717183,0.529790,-6.155232,2.981457,-0.618798,-9.430718,5.525252,6.420927,-7.915175,-5.841448,-1.799937,-8.251863,9.237944,0.448022,-6.951366,2.896644,4.637091,3.642341,-8.189625,9.287600,4.689831,8.461624,-7.400098,2.680175,-6.331587,8.877973,5.538912,7.518354,-3.398389,5.798453,3.583724,5.060281,-1.584234,-2.858741,-1.519315,6.664613],[6.801410,-0.796849,6.306722,3.014530,1.962737,-5.039248,-5.238866,9.538255,-0.129643,8.287891,8.402925,9.887974,-3.174242,-8.812725,7.514622,-2.882259,-2.960809,9.837512,-9.721274,0.157303,8.622243,3.624777,-8.841984,-5.397696,5.238960,-3.060218,8.483047,-3.237550,7.724026,-1.442024,4.084151,8.337852,2.956786,0.068743,7.163362,5.190578,2.629356,-5.608204,4.937194,-3.925839,0.985257,2.819627,-8.059338,-8.750251,3.253934,5.141262,0.787245,-9.704290,7.905318,3.725646,5.494117,8.246034,5.257914,-3.563986,-6.762906,2.101322,9.294561,-8.527807,7.494581,8.773960,2.567376,9.408998,6.012184,7.793663,7.283656,-1.303576,5.779736,5.731812,5.710986,5.520793,5.283378,7.424447,-5.446125,-1.028902,-7.152262,-8.486333,-3.155803,9.437350,4.965563,-6.696229,5.805506,6.562540,-4.063910,5.447413,-3.318585,-5.443218,3.174990,-3.897264,0.207717,7.111869,-6.554386,-2.740248,6.659643,7.442930,-3.128718,-3.945811,-1.356929,7.952298,-6.897507,-9.881002,5.939658,-2.073092,6.466610,-5.844270,-6.643958,-5.672796,5.779391,6.462047,-0.744246,-4.225894,9.120188,-5.317145,-8.757839,-1.603762,-1.798384,-1.160990,5.353812,6.543047,1.054750,-0.334119,2.420117,4.079923,7.063541,-2.112110,0.287735,-1.774706,7.161250,-0.592889,-6.788266,-7.843190,7.288254,1.834689,-3.821321,9.601497,-7.822733,5.010464,9.835249,3.011349,5.982731,-3.544938]], dtype = "float64")#candidate|4284|(9, 140)|const|float64
call_4283 = relay.TupleGetItem(func_569_call(relay.reshape(const_4284.astype('float64'), [10, 9, 14])), 0)
call_4285 = relay.TupleGetItem(func_571_call(relay.reshape(const_4284.astype('float64'), [10, 9, 14])), 0)
output = relay.Tuple([bop_4270,uop_4280,call_4283,const_4284,])
output2 = relay.Tuple([bop_4270,uop_4280,call_4285,const_4284,])
func_4297 = relay.Function([var_4268,], output)
mod['func_4297'] = func_4297
mod = relay.transform.InferType()(mod)
var_4298 = relay.var("var_4298", dtype = "float64", shape = (15, 9, 1))#candidate|4298|(15, 9, 1)|var|float64
output = func_4297(var_4298)
func_4299 = relay.Function([var_4298], output)
mutated_mod['func_4299'] = func_4299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2972_call = mod.get_global_var('func_2972')
func_2974_call = mutated_mod.get_global_var('func_2974')
call_4333 = func_2972_call()
call_4334 = func_2972_call()
func_1414_call = mod.get_global_var('func_1414')
func_1417_call = mutated_mod.get_global_var('func_1417')
var_4342 = relay.var("var_4342", dtype = "int8", shape = (351,))#candidate|4342|(351,)|var|int8
call_4341 = relay.TupleGetItem(func_1414_call(relay.reshape(var_4342.astype('int8'), [351,])), 1)
call_4343 = relay.TupleGetItem(func_1417_call(relay.reshape(var_4342.astype('int8'), [351,])), 1)
uop_4355 = relay.asin(var_4342.astype('float32')) # shape=(351,)
output = relay.Tuple([call_4333,call_4341,uop_4355,])
output2 = relay.Tuple([call_4334,call_4343,uop_4355,])
func_4357 = relay.Function([var_4342,], output)
mod['func_4357'] = func_4357
mod = relay.transform.InferType()(mod)
var_4358 = relay.var("var_4358", dtype = "int8", shape = (351,))#candidate|4358|(351,)|var|int8
output = func_4357(var_4358)
func_4359 = relay.Function([var_4358], output)
mutated_mod['func_4359'] = func_4359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1631_call = mod.get_global_var('func_1631')
func_1632_call = mutated_mod.get_global_var('func_1632')
call_4388 = relay.TupleGetItem(func_1631_call(), 3)
call_4389 = relay.TupleGetItem(func_1632_call(), 3)
func_2677_call = mod.get_global_var('func_2677')
func_2679_call = mutated_mod.get_global_var('func_2679')
call_4397 = relay.TupleGetItem(func_2677_call(), 2)
call_4398 = relay.TupleGetItem(func_2679_call(), 2)
func_1544_call = mod.get_global_var('func_1544')
func_1546_call = mutated_mod.get_global_var('func_1546')
call_4412 = relay.TupleGetItem(func_1544_call(), 0)
call_4413 = relay.TupleGetItem(func_1546_call(), 0)
func_2972_call = mod.get_global_var('func_2972')
func_2974_call = mutated_mod.get_global_var('func_2974')
call_4419 = func_2972_call()
call_4420 = func_2972_call()
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_4446 = func_3977_call()
call_4447 = func_3977_call()
output = relay.Tuple([call_4388,call_4397,call_4412,call_4419,call_4446,])
output2 = relay.Tuple([call_4389,call_4398,call_4413,call_4420,call_4447,])
func_4451 = relay.Function([], output)
mod['func_4451'] = func_4451
mod = relay.transform.InferType()(mod)
output = func_4451()
func_4452 = relay.Function([], output)
mutated_mod['func_4452'] = func_4452
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4492 = relay.var("var_4492", dtype = "float64", shape = (12, 7, 11))#candidate|4492|(12, 7, 11)|var|float64
uop_4493 = relay.acos(var_4492.astype('float64')) # shape=(12, 7, 11)
uop_4508 = relay.acosh(var_4492.astype('float64')) # shape=(12, 7, 11)
bop_4525 = relay.add(var_4492.astype('float32'), relay.reshape(uop_4508.astype('float32'), relay.shape_of(var_4492))) # shape=(12, 7, 11)
bop_4530 = relay.divide(var_4492.astype('float32'), relay.reshape(bop_4525.astype('float32'), relay.shape_of(var_4492))) # shape=(12, 7, 11)
output = relay.Tuple([uop_4493,bop_4530,])
output2 = relay.Tuple([uop_4493,bop_4530,])
func_4540 = relay.Function([var_4492,], output)
mod['func_4540'] = func_4540
mod = relay.transform.InferType()(mod)
var_4541 = relay.var("var_4541", dtype = "float64", shape = (12, 7, 11))#candidate|4541|(12, 7, 11)|var|float64
output = func_4540(var_4541)
func_4542 = relay.Function([var_4541], output)
mutated_mod['func_4542'] = func_4542
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4572 = relay.var("var_4572", dtype = "float32", shape = (4, 6, 5))#candidate|4572|(4, 6, 5)|var|float32
uop_4573 = relay.sigmoid(var_4572.astype('float32')) # shape=(4, 6, 5)
output = uop_4573
output2 = uop_4573
func_4580 = relay.Function([var_4572,], output)
mod['func_4580'] = func_4580
mod = relay.transform.InferType()(mod)
var_4581 = relay.var("var_4581", dtype = "float32", shape = (4, 6, 5))#candidate|4581|(4, 6, 5)|var|float32
output = func_4580(var_4581)
func_4582 = relay.Function([var_4581], output)
mutated_mod['func_4582'] = func_4582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4184_call = mod.get_global_var('func_4184')
func_4186_call = mutated_mod.get_global_var('func_4186')
call_4653 = relay.TupleGetItem(func_4184_call(), 0)
call_4654 = relay.TupleGetItem(func_4186_call(), 0)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_4655 = func_365_call()
call_4656 = func_365_call()
output = relay.Tuple([call_4653,call_4655,])
output2 = relay.Tuple([call_4654,call_4656,])
func_4663 = relay.Function([], output)
mod['func_4663'] = func_4663
mod = relay.transform.InferType()(mod)
output = func_4663()
func_4664 = relay.Function([], output)
mutated_mod['func_4664'] = func_4664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mod.get_global_var('func_1223')
func_1224_call = mutated_mod.get_global_var('func_1224')
call_4711 = func_1223_call()
call_4712 = func_1223_call()
func_169_call = mod.get_global_var('func_169')
func_174_call = mutated_mod.get_global_var('func_174')
call_4719 = relay.TupleGetItem(func_169_call(relay.reshape(call_4711.astype('float32'), [10, 9, 14]), relay.reshape(call_4711.astype('float32'), [10, 9, 14]), relay.reshape(call_4711.astype('bool'), [10, 9, 14]), ), 1)
call_4720 = relay.TupleGetItem(func_174_call(relay.reshape(call_4711.astype('float32'), [10, 9, 14]), relay.reshape(call_4711.astype('float32'), [10, 9, 14]), relay.reshape(call_4711.astype('bool'), [10, 9, 14]), ), 1)
output = relay.Tuple([call_4711,call_4719,])
output2 = relay.Tuple([call_4712,call_4720,])
func_4728 = relay.Function([], output)
mod['func_4728'] = func_4728
mod = relay.transform.InferType()(mod)
mutated_mod['func_4728'] = func_4728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4728_call = mutated_mod.get_global_var('func_4728')
call_4729 = func_4728_call()
output = call_4729
func_4730 = relay.Function([], output)
mutated_mod['func_4730'] = func_4730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_4771 = relay.TupleGetItem(func_909_call(), 3)
call_4772 = relay.TupleGetItem(func_910_call(), 3)
output = relay.Tuple([call_4771,])
output2 = relay.Tuple([call_4772,])
func_4780 = relay.Function([], output)
mod['func_4780'] = func_4780
mod = relay.transform.InferType()(mod)
mutated_mod['func_4780'] = func_4780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4780_call = mutated_mod.get_global_var('func_4780')
call_4781 = func_4780_call()
output = call_4781
func_4782 = relay.Function([], output)
mutated_mod['func_4782'] = func_4782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_4783 = func_2356_call()
call_4784 = func_2356_call()
output = relay.Tuple([call_4783,])
output2 = relay.Tuple([call_4784,])
func_4792 = relay.Function([], output)
mod['func_4792'] = func_4792
mod = relay.transform.InferType()(mod)
output = func_4792()
func_4793 = relay.Function([], output)
mutated_mod['func_4793'] = func_4793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_254_call = mutated_mod.get_global_var('func_254')
call_4859 = relay.TupleGetItem(func_252_call(), 1)
call_4860 = relay.TupleGetItem(func_254_call(), 1)
func_2963_call = mod.get_global_var('func_2963')
func_2966_call = mutated_mod.get_global_var('func_2966')
call_4861 = relay.TupleGetItem(func_2963_call(relay.reshape(call_4859.astype('float64'), [10, 9, 14])), 0)
call_4862 = relay.TupleGetItem(func_2966_call(relay.reshape(call_4859.astype('float64'), [10, 9, 14])), 0)
func_4451_call = mod.get_global_var('func_4451')
func_4452_call = mutated_mod.get_global_var('func_4452')
call_4891 = relay.TupleGetItem(func_4451_call(), 4)
call_4892 = relay.TupleGetItem(func_4452_call(), 4)
output = relay.Tuple([call_4859,call_4861,call_4891,])
output2 = relay.Tuple([call_4860,call_4862,call_4892,])
func_4902 = relay.Function([], output)
mod['func_4902'] = func_4902
mod = relay.transform.InferType()(mod)
output = func_4902()
func_4903 = relay.Function([], output)
mutated_mod['func_4903'] = func_4903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4941 = relay.var("var_4941", dtype = "float32", shape = (9, 15))#candidate|4941|(9, 15)|var|float32
uop_4942 = relay.sinh(var_4941.astype('float32')) # shape=(9, 15)
output = uop_4942
output2 = uop_4942
func_4949 = relay.Function([var_4941,], output)
mod['func_4949'] = func_4949
mod = relay.transform.InferType()(mod)
mutated_mod['func_4949'] = func_4949
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4950 = relay.var("var_4950", dtype = "float32", shape = (9, 15))#candidate|4950|(9, 15)|var|float32
func_4949_call = mutated_mod.get_global_var('func_4949')
call_4951 = func_4949_call(var_4950)
output = call_4951
func_4952 = relay.Function([var_4950], output)
mutated_mod['func_4952'] = func_4952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2750_call = mod.get_global_var('func_2750')
func_2751_call = mutated_mod.get_global_var('func_2751')
call_4996 = relay.TupleGetItem(func_2750_call(), 2)
call_4997 = relay.TupleGetItem(func_2751_call(), 2)
var_5004 = relay.var("var_5004", dtype = "float64", shape = (10, 6, 5))#candidate|5004|(10, 6, 5)|var|float64
bop_5005 = relay.logical_xor(call_4996.astype('int8'), relay.reshape(var_5004.astype('int8'), relay.shape_of(call_4996))) # shape=(10, 6, 5)
bop_5008 = relay.logical_xor(call_4997.astype('int8'), relay.reshape(var_5004.astype('int8'), relay.shape_of(call_4997))) # shape=(10, 6, 5)
func_3489_call = mod.get_global_var('func_3489')
func_3490_call = mutated_mod.get_global_var('func_3490')
call_5009 = relay.TupleGetItem(func_3489_call(), 0)
call_5010 = relay.TupleGetItem(func_3490_call(), 0)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_5019 = relay.TupleGetItem(func_909_call(), 3)
call_5020 = relay.TupleGetItem(func_910_call(), 3)
var_5037 = relay.var("var_5037", dtype = "float32", shape = (10, 9, 14))#candidate|5037|(10, 9, 14)|var|float32
bop_5038 = relay.equal(call_5009.astype('bool'), relay.reshape(var_5037.astype('bool'), relay.shape_of(call_5009))) # shape=(10, 9, 14)
bop_5041 = relay.equal(call_5010.astype('bool'), relay.reshape(var_5037.astype('bool'), relay.shape_of(call_5010))) # shape=(10, 9, 14)
func_1331_call = mod.get_global_var('func_1331')
func_1334_call = mutated_mod.get_global_var('func_1334')
var_5048 = relay.var("var_5048", dtype = "uint64", shape = (210,))#candidate|5048|(210,)|var|uint64
call_5047 = relay.TupleGetItem(func_1331_call(relay.reshape(var_5048.astype('uint64'), [10, 7, 3])), 1)
call_5049 = relay.TupleGetItem(func_1334_call(relay.reshape(var_5048.astype('uint64'), [10, 7, 3])), 1)
func_1289_call = mod.get_global_var('func_1289')
func_1291_call = mutated_mod.get_global_var('func_1291')
call_5050 = relay.TupleGetItem(func_1289_call(), 1)
call_5051 = relay.TupleGetItem(func_1291_call(), 1)
var_5071 = relay.var("var_5071", dtype = "float32", shape = (4, 14, 10))#candidate|5071|(4, 14, 10)|var|float32
bop_5072 = relay.greater_equal(call_5019.astype('bool'), relay.reshape(var_5071.astype('bool'), relay.shape_of(call_5019))) # shape=(4, 14, 10)
bop_5075 = relay.greater_equal(call_5020.astype('bool'), relay.reshape(var_5071.astype('bool'), relay.shape_of(call_5020))) # shape=(4, 14, 10)
output = relay.Tuple([bop_5005,bop_5038,call_5047,var_5048,call_5050,bop_5072,])
output2 = relay.Tuple([bop_5008,bop_5041,call_5049,var_5048,call_5051,bop_5075,])
func_5082 = relay.Function([var_5004,var_5037,var_5048,var_5071,], output)
mod['func_5082'] = func_5082
mod = relay.transform.InferType()(mod)
mutated_mod['func_5082'] = func_5082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5082_call = mutated_mod.get_global_var('func_5082')
var_5084 = relay.var("var_5084", dtype = "float64", shape = (10, 6, 5))#candidate|5084|(10, 6, 5)|var|float64
var_5085 = relay.var("var_5085", dtype = "float32", shape = (10, 9, 14))#candidate|5085|(10, 9, 14)|var|float32
var_5086 = relay.var("var_5086", dtype = "uint64", shape = (210,))#candidate|5086|(210,)|var|uint64
var_5087 = relay.var("var_5087", dtype = "float32", shape = (4, 14, 10))#candidate|5087|(4, 14, 10)|var|float32
call_5083 = func_5082_call(var_5084,var_5085,var_5086,var_5087,)
output = call_5083
func_5088 = relay.Function([var_5084,var_5085,var_5086,var_5087,], output)
mutated_mod['func_5088'] = func_5088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4902_call = mod.get_global_var('func_4902')
func_4903_call = mutated_mod.get_global_var('func_4903')
call_5101 = relay.TupleGetItem(func_4902_call(), 1)
call_5102 = relay.TupleGetItem(func_4903_call(), 1)
output = call_5101
output2 = call_5102
func_5107 = relay.Function([], output)
mod['func_5107'] = func_5107
mod = relay.transform.InferType()(mod)
output = func_5107()
func_5108 = relay.Function([], output)
mutated_mod['func_5108'] = func_5108
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5146 = relay.const(True, dtype = "bool")#candidate|5146|()|const|bool
var_5147 = relay.var("var_5147", dtype = "bool", shape = (14, 7, 15))#candidate|5147|(14, 7, 15)|var|bool
bop_5148 = relay.logical_or(const_5146.astype('bool'), var_5147.astype('bool')) # shape=(14, 7, 15)
func_2104_call = mod.get_global_var('func_2104')
func_2106_call = mutated_mod.get_global_var('func_2106')
const_5152 = relay.const([[-9.732957,7.402775,-1.698384,0.125447,-3.696059,6.866088,4.562710,-8.984189,-3.245194,-3.804810,-9.010029,4.375526,-3.376446,1.852173,-3.553348,-3.923574],[0.139492,-4.448291,-6.918450,-0.234858,2.261946,-2.629442,-3.966698,-0.338387,3.174651,-5.745356,1.954651,-9.986548,-8.327627,-7.557615,5.502187,4.683418],[-9.321678,-5.757005,-7.829350,0.654220,-7.419335,-4.668054,-9.173981,0.723879,-7.701866,-5.345126,-7.103481,4.344827,-8.475909,5.110588,-9.832404,-4.763602],[-6.813839,2.289793,3.261355,-5.617780,-5.356196,-7.471761,5.563066,7.461024,0.466983,1.901562,-1.696958,-1.550624,7.083690,-5.935751,7.508595,-5.257136],[5.490792,-6.031409,4.903278,-5.182164,0.449347,-8.538365,4.146271,-3.352640,0.606423,-4.793976,-0.903682,-3.416446,-0.707101,-7.629006,2.339998,7.117725],[-9.694512,0.411835,-1.438642,-0.430808,5.780797,-4.809818,-3.865903,0.371216,8.957817,5.549869,2.075310,7.163432,-0.550484,5.212595,-0.323964,-0.093934],[-6.297636,-4.253980,9.502508,-8.449849,-4.253813,1.843688,-9.419045,-7.541143,-2.137919,4.833233,-4.947792,6.156340,-9.203337,-2.554404,3.402907,-7.998565],[8.172099,-1.085430,6.665281,2.885354,-3.883390,-2.616050,6.713773,-0.822902,-0.802033,2.530020,-4.093721,9.548397,9.500336,7.404900,-9.054499,-9.377863],[0.913409,-1.574475,-7.068544,-2.264028,2.470067,8.959403,8.169378,-5.182990,9.370185,-9.422385,8.585093,5.337066,-9.766353,1.615008,-5.578697,-7.959400],[2.737376,-9.878990,-8.606011,-4.600908,8.534078,-8.945371,9.567373,-8.879738,9.771492,-9.055446,-1.968312,9.779009,-5.454080,0.230147,8.165048,-3.278947],[-3.261783,-4.963834,3.413757,-0.459672,-4.238880,-9.112796,-9.887578,-0.010569,3.985290,-1.459598,-1.603192,-7.951902,-0.828655,5.509952,0.850692,-1.229186],[-6.852739,-1.100802,4.896283,-4.279912,-4.630859,0.626598,1.639132,-6.798662,-8.961852,-3.341986,-7.726890,-2.307140,-2.300844,-5.588594,6.196537,-5.103054],[5.365961,-3.702273,8.673351,-0.165531,8.631982,-2.408192,-4.382112,8.825443,4.014916,7.505919,8.830863,8.099988,-2.691085,0.283257,-5.026822,4.252438],[7.141573,0.112563,7.232271,-2.413918,7.287371,0.535593,9.041423,1.608263,3.172520,-6.386195,-5.397671,-9.730939,-5.994175,-9.291797,4.777846,-3.763293],[0.327420,-8.499288,-8.785707,9.771941,3.187718,4.411197,-2.273133,-9.167472,5.275972,-2.649607,-0.048864,-9.625739,-6.742101,7.219962,8.061798,-6.177992],[2.225945,6.808867,6.409136,-5.578418,3.983332,3.082011,-0.007975,6.855620,8.439162,9.352090,3.600861,-6.432259,-7.253814,7.122879,1.247422,9.917480]], dtype = "float32")#candidate|5152|(16, 16)|const|float32
call_5151 = relay.TupleGetItem(func_2104_call(relay.reshape(const_5152.astype('float32'), [16, 1, 16])), 0)
call_5153 = relay.TupleGetItem(func_2106_call(relay.reshape(const_5152.astype('float32'), [16, 1, 16])), 0)
bop_5156 = relay.bitwise_and(call_5151.astype('int32'), const_5146.astype('int32')) # shape=(16, 1, 16)
bop_5159 = relay.bitwise_and(call_5153.astype('int32'), const_5146.astype('int32')) # shape=(16, 1, 16)
uop_5163 = relay.tan(bop_5156.astype('float64')) # shape=(16, 1, 16)
uop_5165 = relay.tan(bop_5159.astype('float64')) # shape=(16, 1, 16)
bop_5173 = relay.greater_equal(const_5146.astype('bool'), uop_5163.astype('bool')) # shape=(16, 1, 16)
bop_5176 = relay.greater_equal(const_5146.astype('bool'), uop_5165.astype('bool')) # shape=(16, 1, 16)
output = relay.Tuple([bop_5148,const_5152,bop_5173,])
output2 = relay.Tuple([bop_5148,const_5152,bop_5176,])
func_5177 = relay.Function([var_5147,], output)
mod['func_5177'] = func_5177
mod = relay.transform.InferType()(mod)
mutated_mod['func_5177'] = func_5177
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5178 = relay.var("var_5178", dtype = "bool", shape = (14, 7, 15))#candidate|5178|(14, 7, 15)|var|bool
func_5177_call = mutated_mod.get_global_var('func_5177')
call_5179 = func_5177_call(var_5178)
output = call_5179
func_5180 = relay.Function([var_5178], output)
mutated_mod['func_5180'] = func_5180
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5211 = relay.var("var_5211", dtype = "float64", shape = (5, 12, 3))#candidate|5211|(5, 12, 3)|var|float64
uop_5212 = relay.erf(var_5211.astype('float64')) # shape=(5, 12, 3)
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_5215 = func_3977_call()
call_5216 = func_3977_call()
func_513_call = mod.get_global_var('func_513')
func_516_call = mutated_mod.get_global_var('func_516')
const_5229 = relay.const(3, dtype = "int8")#candidate|5229|()|const|int8
var_5230 = relay.var("var_5230", dtype = "int8", shape = (117, 3))#candidate|5230|(117, 3)|var|int8
call_5228 = func_513_call(relay.reshape(const_5229.astype('int8'), []), relay.reshape(var_5230.astype('int8'), [13, 9, 3]), )
call_5231 = func_513_call(relay.reshape(const_5229.astype('int8'), []), relay.reshape(var_5230.astype('int8'), [13, 9, 3]), )
uop_5238 = relay.acos(uop_5212.astype('float32')) # shape=(5, 12, 3)
func_1223_call = mod.get_global_var('func_1223')
func_1224_call = mutated_mod.get_global_var('func_1224')
call_5250 = func_1223_call()
call_5251 = func_1223_call()
output = relay.Tuple([call_5215,call_5228,const_5229,var_5230,uop_5238,call_5250,])
output2 = relay.Tuple([call_5216,call_5231,const_5229,var_5230,uop_5238,call_5251,])
func_5254 = relay.Function([var_5211,var_5230,], output)
mod['func_5254'] = func_5254
mod = relay.transform.InferType()(mod)
mutated_mod['func_5254'] = func_5254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5254_call = mutated_mod.get_global_var('func_5254')
var_5256 = relay.var("var_5256", dtype = "float64", shape = (5, 12, 3))#candidate|5256|(5, 12, 3)|var|float64
var_5257 = relay.var("var_5257", dtype = "int8", shape = (117, 3))#candidate|5257|(117, 3)|var|int8
call_5255 = func_5254_call(var_5256,var_5257,)
output = call_5255
func_5258 = relay.Function([var_5256,var_5257,], output)
mutated_mod['func_5258'] = func_5258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mod.get_global_var('func_465')
func_467_call = mutated_mod.get_global_var('func_467')
call_5260 = relay.TupleGetItem(func_465_call(), 1)
call_5261 = relay.TupleGetItem(func_467_call(), 1)
output = relay.Tuple([call_5260,])
output2 = relay.Tuple([call_5261,])
func_5285 = relay.Function([], output)
mod['func_5285'] = func_5285
mod = relay.transform.InferType()(mod)
output = func_5285()
func_5286 = relay.Function([], output)
mutated_mod['func_5286'] = func_5286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3359_call = mod.get_global_var('func_3359')
func_3361_call = mutated_mod.get_global_var('func_3361')
call_5289 = func_3359_call()
call_5290 = func_3359_call()
output = call_5289
output2 = call_5290
func_5301 = relay.Function([], output)
mod['func_5301'] = func_5301
mod = relay.transform.InferType()(mod)
mutated_mod['func_5301'] = func_5301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5301_call = mutated_mod.get_global_var('func_5301')
call_5302 = func_5301_call()
output = call_5302
func_5303 = relay.Function([], output)
mutated_mod['func_5303'] = func_5303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_5326 = func_2428_call()
call_5327 = func_2428_call()
output = call_5326
output2 = call_5327
func_5357 = relay.Function([], output)
mod['func_5357'] = func_5357
mod = relay.transform.InferType()(mod)
output = func_5357()
func_5358 = relay.Function([], output)
mutated_mod['func_5358'] = func_5358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4728_call = mod.get_global_var('func_4728')
func_4730_call = mutated_mod.get_global_var('func_4730')
call_5376 = relay.TupleGetItem(func_4728_call(), 0)
call_5377 = relay.TupleGetItem(func_4730_call(), 0)
output = call_5376
output2 = call_5377
func_5385 = relay.Function([], output)
mod['func_5385'] = func_5385
mod = relay.transform.InferType()(mod)
output = func_5385()
func_5386 = relay.Function([], output)
mutated_mod['func_5386'] = func_5386
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5396 = relay.var("var_5396", dtype = "float64", shape = (3, 5, 1))#candidate|5396|(3, 5, 1)|var|float64
uop_5397 = relay.tan(var_5396.astype('float64')) # shape=(3, 5, 1)
output = uop_5397
output2 = uop_5397
func_5399 = relay.Function([var_5396,], output)
mod['func_5399'] = func_5399
mod = relay.transform.InferType()(mod)
var_5400 = relay.var("var_5400", dtype = "float64", shape = (3, 5, 1))#candidate|5400|(3, 5, 1)|var|float64
output = func_5399(var_5400)
func_5401 = relay.Function([var_5400], output)
mutated_mod['func_5401'] = func_5401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2356_call = mod.get_global_var('func_2356')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_5432 = func_2356_call()
call_5433 = func_2356_call()
var_5465 = relay.var("var_5465", dtype = "float32", shape = (4, 14, 10))#candidate|5465|(4, 14, 10)|var|float32
bop_5466 = relay.add(call_5432.astype('int16'), relay.reshape(var_5465.astype('int16'), relay.shape_of(call_5432))) # shape=(4, 14, 10)
bop_5469 = relay.add(call_5433.astype('int16'), relay.reshape(var_5465.astype('int16'), relay.shape_of(call_5433))) # shape=(4, 14, 10)
output = relay.Tuple([bop_5466,])
output2 = relay.Tuple([bop_5469,])
func_5505 = relay.Function([var_5465,], output)
mod['func_5505'] = func_5505
mod = relay.transform.InferType()(mod)
var_5506 = relay.var("var_5506", dtype = "float32", shape = (4, 14, 10))#candidate|5506|(4, 14, 10)|var|float32
output = func_5505(var_5506)
func_5507 = relay.Function([var_5506], output)
mutated_mod['func_5507'] = func_5507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_5509 = func_3977_call()
call_5510 = func_3977_call()
output = call_5509
output2 = call_5510
func_5518 = relay.Function([], output)
mod['func_5518'] = func_5518
mod = relay.transform.InferType()(mod)
output = func_5518()
func_5519 = relay.Function([], output)
mutated_mod['func_5519'] = func_5519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4030_call = mod.get_global_var('func_4030')
func_4032_call = mutated_mod.get_global_var('func_4032')
call_5558 = func_4030_call()
call_5559 = func_4030_call()
output = relay.Tuple([call_5558,])
output2 = relay.Tuple([call_5559,])
func_5564 = relay.Function([], output)
mod['func_5564'] = func_5564
mod = relay.transform.InferType()(mod)
mutated_mod['func_5564'] = func_5564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5564_call = mutated_mod.get_global_var('func_5564')
call_5565 = func_5564_call()
output = call_5565
func_5566 = relay.Function([], output)
mutated_mod['func_5566'] = func_5566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3279_call = mod.get_global_var('func_3279')
func_3280_call = mutated_mod.get_global_var('func_3280')
call_5595 = relay.TupleGetItem(func_3279_call(), 1)
call_5596 = relay.TupleGetItem(func_3280_call(), 1)
func_1414_call = mod.get_global_var('func_1414')
func_1417_call = mutated_mod.get_global_var('func_1417')
var_5604 = relay.var("var_5604", dtype = "int8", shape = (351,))#candidate|5604|(351,)|var|int8
call_5603 = relay.TupleGetItem(func_1414_call(relay.reshape(var_5604.astype('int8'), [351,])), 3)
call_5605 = relay.TupleGetItem(func_1417_call(relay.reshape(var_5604.astype('int8'), [351,])), 3)
output = relay.Tuple([call_5595,call_5603,var_5604,])
output2 = relay.Tuple([call_5596,call_5605,var_5604,])
func_5614 = relay.Function([var_5604,], output)
mod['func_5614'] = func_5614
mod = relay.transform.InferType()(mod)
mutated_mod['func_5614'] = func_5614
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5615 = relay.var("var_5615", dtype = "int8", shape = (351,))#candidate|5615|(351,)|var|int8
func_5614_call = mutated_mod.get_global_var('func_5614')
call_5616 = func_5614_call(var_5615)
output = call_5616
func_5617 = relay.Function([var_5615], output)
mutated_mod['func_5617'] = func_5617
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5646 = relay.const([[[9,-7,8,-8,-3,8,-7,-9,-6,5,5],[-8,7,7,-3,-2,-8,-5,-6,-5,9,-3],[2,9,7,3,-8,-2,-6,-4,9,1,5]],[[-8,-8,10,-6,4,-4,-9,6,10,6,8],[-3,1,8,-1,-8,6,2,3,-10,10,-9],[3,-3,-1,7,9,2,1,-3,-5,-3,-7]],[[6,7,-9,9,5,3,-7,5,4,5,7],[7,10,1,4,10,-9,7,-5,-4,-8,-8],[-1,-10,-10,-10,3,-7,1,8,-5,7,-7]],[[-2,9,-3,-4,4,6,10,-1,3,10,-8],[-7,8,5,7,-8,-4,-8,-7,-6,10,7],[7,2,1,-7,3,-5,5,-4,2,3,2]],[[3,-6,10,-10,-5,4,-5,7,6,-8,-1],[-1,-7,-9,-10,-4,10,-1,-3,7,8,-3],[-6,8,2,-3,9,10,-6,6,1,7,7]],[[2,-9,-10,-10,-3,-5,10,-5,2,6,9],[10,8,-5,-3,-4,-4,3,1,9,2,3],[3,5,-1,7,5,-5,-1,7,-3,-8,-6]],[[-3,6,1,5,-2,-3,4,-9,5,-2,-6],[-1,6,6,2,-7,-8,-4,3,-4,-8,5],[2,4,-10,10,-9,1,-4,1,10,9,-5]],[[1,-2,6,-4,3,4,5,-8,-2,-3,-4],[1,-3,7,2,-6,-1,-8,2,5,5,-7],[-5,-3,-1,1,5,3,6,-3,2,-9,-10]],[[8,-6,9,4,4,-10,10,5,-7,5,2],[1,-8,-5,-6,4,8,8,-3,-3,6,6],[-5,7,-5,3,4,1,7,-10,2,8,6]],[[-7,-2,6,6,-4,-4,2,-3,-5,10,-8],[-5,-1,-2,6,7,-7,-8,7,-6,2,1],[-9,2,9,3,9,6,4,-9,4,-8,6]],[[-3,-9,-5,-10,6,1,5,-9,9,-6,-8],[-1,-5,-4,5,8,-7,8,7,-10,-7,-10],[-5,1,-7,-9,7,3,-4,-4,8,-10,6]],[[-1,-5,-7,-4,-3,8,-2,-10,1,10,9],[10,4,5,5,1,-6,6,9,2,8,-7],[-4,-1,4,6,5,9,4,-3,-9,6,3]],[[9,-4,3,1,-4,6,-10,7,8,-2,1],[-4,6,1,9,7,-3,10,-5,-7,-6,6],[-7,-9,-5,3,8,10,-9,7,-4,-7,-7]]], dtype = "uint32")#candidate|5646|(13, 3, 11)|const|uint32
var_5647 = relay.var("var_5647", dtype = "uint32", shape = (13, 3, 11))#candidate|5647|(13, 3, 11)|var|uint32
bop_5648 = relay.bitwise_xor(const_5646.astype('uint32'), relay.reshape(var_5647.astype('uint32'), relay.shape_of(const_5646))) # shape=(13, 3, 11)
output = bop_5648
output2 = bop_5648
func_5670 = relay.Function([var_5647,], output)
mod['func_5670'] = func_5670
mod = relay.transform.InferType()(mod)
mutated_mod['func_5670'] = func_5670
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5671 = relay.var("var_5671", dtype = "uint32", shape = (13, 3, 11))#candidate|5671|(13, 3, 11)|var|uint32
func_5670_call = mutated_mod.get_global_var('func_5670')
call_5672 = func_5670_call(var_5671)
output = call_5672
func_5673 = relay.Function([var_5671], output)
mutated_mod['func_5673'] = func_5673
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5681 = relay.const([[[10,8,8,-4,7,-7,3,-6,10,4,10,9,-3,3,-3,-3],[1,-6,3,-4,-9,-5,-4,5,-6,10,-7,3,1,-5,7,7],[1,-6,3,-7,10,5,2,8,1,3,8,-9,4,-3,-1,-8],[4,-1,2,9,1,-6,4,-8,-3,-2,-10,1,-6,-4,5,-1],[4,5,-1,7,-8,4,8,-8,6,-3,-2,10,-1,5,4,4],[-2,-5,-5,7,-5,7,5,-6,7,7,6,-9,2,4,2,6],[-6,8,-3,-5,8,-4,9,-3,-1,-6,-10,5,-9,-9,-6,-6],[8,-6,-1,-1,-4,9,7,8,4,7,10,-5,-9,-1,-1,-9],[-5,2,-5,2,-10,-3,-4,-6,-6,4,5,5,4,-10,5,4],[6,5,-8,1,9,-8,-4,3,9,3,7,-1,6,-5,-3,-10],[-6,-10,-1,6,-6,4,9,9,-5,6,-10,2,-8,-6,8,2],[2,-2,-5,-2,-1,1,4,-1,-2,-2,4,10,-10,5,-4,-6],[8,-9,4,-2,-8,8,10,-2,6,7,-7,-2,-1,9,-1,-2],[-2,-2,2,3,6,3,-1,-10,-8,-9,-2,-4,-5,10,7,-6]],[[1,-5,-1,-3,2,-3,-1,-1,8,6,10,-4,-2,-2,-6,-7],[-6,2,-1,-2,-10,-7,8,2,8,7,-9,-3,-7,9,3,10],[10,-5,-6,-5,4,9,-10,1,10,-5,10,9,5,1,-6,7],[5,-9,1,-9,-6,8,-9,5,6,8,2,-5,7,-2,7,3],[3,4,5,-10,10,-10,-6,10,-7,-10,-8,-5,-1,2,-8,1],[-6,-7,8,4,5,9,-1,7,-9,-6,-4,-6,9,4,-2,9],[1,8,3,-7,8,-4,-7,6,8,7,-4,-8,10,10,-8,-9],[-5,6,1,-10,9,9,-5,-4,-10,6,3,-8,-5,-4,-7,9],[1,2,9,4,-6,-4,9,-5,-8,-4,-6,-1,-9,3,9,10],[1,4,3,-8,3,1,1,-1,-8,9,7,6,-6,-2,5,6],[3,6,10,-7,9,4,-6,8,-2,-2,8,3,-9,10,6,-9],[-8,4,-10,-2,1,-6,3,-4,2,3,4,-3,-2,6,-9,-8],[-10,4,5,7,-3,6,-1,-2,8,3,3,6,9,7,9,-4],[10,-8,-5,3,-10,-6,3,3,5,-7,4,-6,-5,10,8,2]],[[-3,3,5,-9,-8,5,-5,5,4,10,5,-10,1,-6,-5,7],[9,9,-7,-9,3,8,-4,-10,7,6,-8,-4,-8,7,9,3],[-5,3,1,9,-10,4,4,-2,-3,-2,-7,-9,-7,10,10,7],[8,-7,6,4,7,-7,1,-9,-8,-7,-7,1,1,-3,7,-8],[2,5,-5,1,7,10,-9,-4,2,-3,-8,-7,8,-1,10,9],[7,9,2,-2,9,-9,-3,-7,-6,5,9,-4,2,9,9,3],[1,-7,-1,2,-3,10,5,2,-2,-7,1,-5,1,6,-3,3],[2,-6,9,6,-10,9,-6,9,9,10,-9,6,10,-7,2,6],[2,-10,-10,4,-3,-5,5,8,10,-8,4,9,6,6,8,6],[3,-2,10,-3,10,-1,-2,10,8,10,-2,5,-5,-9,-10,10],[9,-6,-7,-4,-7,-3,-6,10,1,-6,-7,2,-10,4,6,-5],[7,5,-10,-2,-4,5,-7,3,-5,2,10,5,-5,-1,-2,-5],[8,2,7,-7,8,-10,-9,3,-2,7,9,1,10,2,-10,2],[6,-8,-9,-3,-8,-1,6,10,-7,9,10,9,-3,1,-9,-3]],[[-8,-8,-7,1,-4,2,-6,-7,1,10,-5,1,-1,1,-7,5],[-7,-2,5,-10,8,8,-8,9,-8,-3,10,-1,10,3,8,5],[-4,-10,10,8,5,4,-3,-5,5,-6,-1,8,-10,-1,10,4],[2,-2,7,2,8,-5,10,3,-5,-10,5,10,-10,6,6,5],[7,10,-7,-3,-10,-7,-8,8,9,-4,8,4,4,10,-9,9],[2,9,4,8,2,-6,8,-6,4,5,-1,-9,-6,-8,-6,2],[-6,1,5,-6,7,-7,-8,3,-2,-3,7,9,-3,-2,-4,10],[7,4,1,9,3,-2,-1,-4,-5,-6,-1,8,4,4,4,1],[-5,5,4,3,-2,-10,-4,-5,-3,3,-8,7,-3,-1,7,10],[7,-8,-9,-10,-8,3,-7,2,9,-4,-8,-10,-2,-8,5,10],[1,-4,-9,-3,-7,10,5,3,-9,1,-8,6,2,-8,2,-8],[6,-5,-8,-5,-5,10,8,3,10,5,-7,-9,-7,-5,-7,-3],[-8,-9,7,1,8,1,5,-5,10,-7,1,5,5,6,-6,4],[-7,10,8,7,5,3,-4,6,-8,-10,-9,8,8,5,-5,9]],[[3,-8,-5,8,-3,-9,-1,2,10,-10,-10,2,-4,-3,5,1],[-5,10,5,9,2,6,7,-3,-9,-5,-1,6,-3,2,-3,5],[-3,-10,-6,8,-9,1,2,2,-7,10,-3,1,7,3,8,10],[4,2,8,-9,-4,-2,4,-8,10,-9,6,8,-5,5,-10,5],[-6,-5,-6,-3,5,-7,-1,10,-6,-6,-10,8,-5,7,10,9],[-10,10,9,8,-3,4,3,7,4,-2,8,-8,-2,10,8,8],[6,-5,3,10,10,2,-8,1,-2,4,2,7,-8,4,6,7],[-9,-6,6,10,8,7,1,-7,10,5,7,6,6,-3,-1,4],[-3,-6,-8,4,8,-1,-1,2,-2,-3,-8,4,10,-8,-10,-3],[-7,-3,-5,1,8,2,2,3,2,5,-7,-6,10,10,-8,-4],[-3,-10,-4,2,4,-3,10,4,-4,-2,10,7,-3,2,1,-6],[3,-1,-8,-10,8,1,-9,-2,6,5,-3,7,-1,-5,7,5],[9,8,10,2,-1,-8,7,-5,-5,8,3,1,-6,-6,-2,-4],[6,10,8,-6,2,1,-3,4,-7,3,10,5,2,1,-10,-5]],[[-5,-4,5,-3,-3,8,-1,3,5,-7,2,4,-3,8,-10,-2],[7,9,6,-1,-6,-5,3,4,-4,4,-5,9,-3,-3,-1,-9],[3,-10,-10,9,2,-5,-4,5,-2,-3,9,-6,1,5,-6,-10],[-2,1,-5,-2,-6,4,-7,-7,7,-5,4,-9,3,-8,-10,-10],[-1,8,3,5,-6,7,-7,2,4,10,-3,4,-5,-4,1,9],[7,9,7,7,-2,-9,-1,-3,-10,-5,-2,-8,-9,3,-8,-1],[-8,-3,4,-10,-4,-3,10,10,-9,-5,-3,-9,7,2,4,10],[-6,9,-3,-6,10,4,5,1,10,-8,-3,5,1,-7,5,-9],[10,-2,-8,2,10,-7,-1,-1,-6,-1,-6,-9,6,-1,3,3],[-7,6,5,-3,-5,2,-1,-4,1,-8,-4,5,-4,2,-6,1],[-1,-1,9,1,-8,-8,5,-6,9,-5,-2,4,9,-3,2,10],[-3,2,-7,-5,-8,-4,5,1,-5,-9,-9,10,1,-2,-9,8],[3,5,-5,-7,-3,7,-2,-2,-7,3,-3,5,-10,9,-9,-1],[-7,6,-7,4,-5,-8,9,5,2,-3,5,-1,7,4,6,-10]],[[-2,-4,1,-10,1,3,-9,-8,-10,-8,-1,10,10,3,9,-9],[-10,-1,3,7,-9,-3,-3,-1,-6,-8,9,-4,-1,-5,2,1],[-4,-5,6,-10,4,-5,-8,10,5,-10,3,3,3,-4,9,1],[2,2,-7,2,8,8,4,-10,3,3,-6,-2,4,5,5,-9],[-1,-6,-5,-10,6,9,-6,-8,8,7,-6,2,8,3,3,-2],[-3,3,-7,-1,10,2,8,5,1,-10,4,7,9,-7,2,-9],[8,-2,-4,7,-2,2,-10,6,10,8,-7,-5,-5,-1,2,3],[-3,-6,-8,2,3,-2,10,6,-3,5,-1,8,-5,-2,-10,-8],[10,9,8,-9,-5,5,8,-7,-8,-5,-5,5,-4,8,4,7],[1,-3,7,-9,3,-8,-9,-6,-7,8,-1,-3,-1,-9,10,-10],[-1,-9,5,1,-4,-10,3,-2,4,4,2,-2,-10,-10,8,1],[-3,8,-8,5,-7,7,-9,-2,-8,10,-6,2,5,6,2,-3],[-8,10,-1,2,-9,9,9,-3,-10,4,7,-3,8,8,-9,-2],[1,4,8,-1,4,-5,5,-9,-2,2,9,-4,7,4,2,-2]]], dtype = "uint64")#candidate|5681|(7, 14, 16)|const|uint64
const_5682 = relay.const([[[-5,-8,8,-5,9,7,-7,1,6,-9,-6,-10,-9,1,-7,7],[-1,-4,8,1,1,5,1,-9,7,-1,-4,-3,7,10,-10,-9],[3,1,-5,9,2,-3,-10,-9,2,-4,-10,-1,3,-4,10,4],[-7,3,9,7,7,-4,6,-6,3,7,8,-4,-7,2,2,-9],[2,2,-5,5,-2,-1,-10,7,8,9,-9,-5,-1,-6,-4,1],[-8,-9,1,6,-3,-2,-3,-8,-2,-7,10,-9,-2,4,-1,-1],[-8,-5,6,-4,8,2,4,2,-7,-9,2,9,-7,9,-10,9],[5,-8,-7,8,8,-7,-9,10,-10,4,1,8,-8,5,9,5],[10,-3,-8,10,-10,-10,-8,7,-3,1,-6,-1,-6,-4,2,7],[5,-9,-2,10,-8,2,-5,5,2,2,-5,-6,-9,5,10,-3],[3,-7,-1,-6,-9,6,-9,-2,6,-3,-8,3,-7,-9,10,1],[6,-10,-7,7,-7,2,3,-9,9,-4,-10,4,-5,6,9,-1],[-7,3,7,4,2,-2,-1,7,-4,6,-6,-3,7,8,-9,2],[-8,-4,2,9,-3,10,1,-3,-8,10,3,-7,-5,8,-2,1]],[[-3,6,-2,-1,7,6,-1,-4,-2,-5,8,-5,6,8,-4,-1],[4,4,4,1,-1,3,8,10,-2,4,8,-4,5,-2,10,7],[1,-2,-1,10,9,-1,-9,-8,-10,2,4,-2,-7,-9,10,-3],[-9,7,7,9,9,5,-5,-2,7,-2,-1,1,9,-6,-8,-9],[3,9,5,8,-10,-3,-7,-1,-10,-7,-7,10,-10,6,-7,-7],[3,2,3,-4,-2,9,4,6,-3,5,-3,8,3,-3,9,1],[-5,-1,-3,-1,-4,6,2,-1,7,7,-3,5,-10,-4,-8,2],[8,-2,-10,7,5,9,-7,2,-8,-6,-5,7,-9,4,-8,3],[-2,8,-7,-6,-10,10,7,1,-3,10,-8,-5,10,6,-8,5],[-1,-3,-9,1,-6,-7,4,-10,-5,-7,9,-1,1,-8,-6,8],[7,-8,-10,6,-1,-9,-2,-4,-9,-9,-10,7,10,10,-10,3],[-10,6,3,4,-6,1,-1,-5,3,-1,8,6,-5,2,-5,-5],[-8,-4,4,5,2,9,10,-8,-2,7,8,6,10,-3,4,9],[-8,3,5,-5,5,-2,8,7,8,-9,-7,-2,-2,-1,2,8]],[[-7,5,10,-8,-1,-1,8,-2,2,-5,-4,-6,-3,-3,-9,6],[-4,7,-10,-1,3,2,10,2,-5,2,5,8,-9,2,3,-5],[10,1,4,10,3,-1,-8,-6,-9,2,10,-1,-2,6,-2,2],[-2,-1,-6,6,-3,-4,-1,1,3,-3,3,2,10,1,-9,-3],[8,7,-4,-3,1,5,-2,-1,2,-5,-9,-10,-5,10,-4,4],[8,-5,-6,7,-8,7,-1,-2,-2,7,4,-2,-10,4,7,5],[-1,6,-9,-3,7,6,8,-2,4,4,9,-8,10,1,10,-1],[-6,-6,-3,-1,-1,-10,-4,-1,-2,-10,-5,-7,10,10,-6,1],[-1,-7,10,-5,-7,-1,-9,-1,9,1,-10,9,-10,2,-2,-10],[-1,-7,6,-3,-9,2,-7,9,2,2,-10,-2,7,-6,6,-4],[-2,-2,-5,9,-7,1,6,2,10,2,2,-10,-9,-10,2,-3],[-4,-3,10,-2,5,-1,-3,-10,4,3,-5,4,1,8,7,8],[-8,10,-2,-5,4,-9,10,10,-1,-1,-7,-2,-1,10,6,9],[8,4,-2,9,6,2,7,-1,6,7,-6,-2,9,-5,1,-9]],[[-5,-8,-1,-4,-5,4,-10,-2,-6,2,8,-1,7,2,-1,-6],[3,7,3,2,10,1,2,8,4,3,3,9,-9,-7,-3,1],[7,1,-9,-7,10,9,-1,3,7,7,8,-2,-8,-1,10,-6],[-10,-4,-1,-8,-8,4,-5,7,1,-4,4,7,-2,3,-10,8],[8,-1,-4,-10,7,2,-9,4,6,10,-3,-2,-5,1,-5,-5],[3,-4,4,-9,-7,5,-1,7,-8,-7,-4,-9,3,-4,9,5],[-5,8,2,4,-10,7,-7,-1,1,-7,-7,6,6,-2,9,-6],[-4,-8,4,8,-1,5,9,-5,4,-9,-10,-2,-5,9,2,10],[2,4,2,-9,-5,4,-2,6,3,-8,-10,-9,-5,-9,-6,2],[-1,-3,8,-9,-8,-9,-2,-6,-10,-9,-5,7,7,-8,7,2],[-6,-2,-8,-7,3,-5,-1,-1,-5,5,-7,1,-8,-8,9,-4],[6,9,-4,8,-2,-2,6,-8,-2,-3,5,4,1,8,-3,-4],[6,-10,-2,10,5,-1,-7,-2,-1,-9,-8,-10,8,-10,-10,-9],[10,1,-10,-7,4,4,6,2,10,4,8,-9,-1,7,-3,-8]],[[-6,4,9,-8,9,6,-9,-1,-2,1,8,-6,6,10,10,10],[-6,-1,-8,-10,5,10,-6,7,7,-8,5,-4,9,-8,-2,6],[-7,-5,-8,-9,2,-8,-2,6,10,-4,10,-6,4,8,6,-5],[3,-7,-2,-5,-8,3,-8,9,3,-5,-3,-1,-8,-4,5,7],[-7,10,-1,-6,-9,-8,7,7,1,2,6,3,-2,-8,6,4],[10,-5,-10,1,-1,6,-6,-10,6,3,5,6,4,-6,-7,-6],[-6,-9,3,6,7,-1,-5,-2,-3,3,-4,9,2,10,8,8],[8,-2,7,4,10,-9,-8,-7,5,-3,10,-6,-7,-2,4,-1],[-7,-3,3,-8,-5,-7,5,8,-6,8,-2,6,3,-6,-8,-9],[-2,-7,10,-5,10,9,-9,-7,5,9,-4,-7,-3,-3,-10,3],[-3,-4,-8,7,4,-5,-3,8,-2,5,1,10,-7,-4,5,8],[2,2,-4,7,-7,2,9,-7,-6,4,8,-1,8,1,-7,-3],[2,8,-6,-5,1,2,5,8,4,9,9,7,9,3,9,-6],[3,7,1,10,-9,-10,2,8,-4,-9,8,10,-6,-5,3,3]],[[3,3,4,-6,8,9,-5,-7,3,2,4,1,9,2,-5,-7],[-7,-4,6,5,-5,-5,1,-1,-9,-8,-9,2,2,1,1,8],[8,10,-4,-7,9,-1,-5,-7,-9,7,1,-7,5,4,6,5],[-6,8,-2,-8,7,3,4,-6,2,-3,3,10,10,4,-6,7],[-6,1,-10,-10,10,10,-3,9,10,-10,3,-2,4,6,5,-3],[8,8,4,-6,-1,-10,-3,-10,2,7,-2,10,-3,7,2,8],[3,-10,1,-3,2,-7,-2,-9,8,4,5,7,2,5,-3,6],[8,-3,3,3,9,2,8,-8,7,8,5,9,9,-1,-10,8],[-6,9,9,7,-4,9,-2,10,-8,1,-4,-3,8,-5,3,-6],[-6,-8,-7,-3,6,2,-9,-7,-3,-2,-1,-1,-9,5,2,2],[-6,-3,7,-5,7,1,2,-7,-6,-1,4,-6,-8,8,4,-10],[-2,5,-10,-2,-8,5,1,-2,-10,4,4,-8,2,-4,6,9],[8,9,2,5,6,-9,-3,-4,5,7,-9,-4,3,-9,4,8],[2,10,-1,-8,-8,-4,10,-3,9,6,7,2,8,10,1,-3]],[[-7,9,-1,-5,-3,-7,-10,-10,10,-8,4,8,1,-5,6,-7],[3,1,4,1,6,2,10,-2,8,9,9,-5,3,-5,9,4],[-8,6,-10,9,6,-9,-3,-7,2,-4,-3,-3,8,7,-10,9],[-7,-9,-3,2,-2,-6,-5,-8,10,10,-1,-10,-1,-6,8,-8],[-2,2,7,-5,-9,6,5,-3,-5,8,7,5,-5,-8,8,-9],[-3,6,-9,9,-1,3,8,-2,-10,9,10,-5,4,-9,-7,5],[-3,10,-1,1,-5,-1,-10,-7,3,8,-9,8,6,8,-10,-3],[-5,5,3,9,10,-2,2,3,-5,-9,-5,10,6,5,2,-9],[5,4,-9,8,2,10,-1,-1,5,1,-7,-1,10,1,8,-8],[3,2,4,9,-2,-1,-1,9,2,-6,-2,4,-5,-3,-4,-5],[-4,8,7,-5,-6,1,-9,-5,-2,-10,8,-6,10,7,2,-2],[8,-6,9,5,-8,-5,9,-9,-1,-3,4,1,1,-7,-9,-1],[1,4,-9,-5,7,3,10,-5,1,-9,9,9,9,5,7,6],[1,7,-1,6,-4,4,-3,4,-8,10,-2,-9,7,8,-8,-3]]], dtype = "uint64")#candidate|5682|(7, 14, 16)|const|uint64
bop_5683 = relay.greater(const_5681.astype('bool'), relay.reshape(const_5682.astype('bool'), relay.shape_of(const_5681))) # shape=(7, 14, 16)
const_5691 = relay.const([[[-8,1,-10,4,1,-7,-4,7,10,-1,8,2,-7,3,3,-5],[10,4,-6,9,6,-8,-10,4,-2,-6,-2,-10,5,8,-7,-8],[1,-6,-2,-8,-10,3,-1,10,3,-4,4,-3,-7,6,3,2],[6,3,-2,8,-7,-2,7,10,9,6,-5,-10,-7,-8,-10,6],[-8,-6,10,-4,5,3,-7,-6,8,10,9,8,6,-8,-8,-2],[3,-9,-2,-10,-9,2,10,4,8,-1,-4,2,-7,-8,-5,1],[8,3,-3,8,-9,-7,8,5,5,-4,-7,1,-9,6,7,5],[9,7,2,5,-8,8,-4,-4,1,8,-6,-1,-5,-2,6,2],[-5,9,-4,7,-7,-10,10,-1,-1,10,-7,-6,-7,9,-4,-9],[7,6,-2,-5,-8,1,-8,2,1,-1,-10,-3,5,-2,-2,-8],[9,-2,7,-2,-4,-6,5,-4,-7,-7,3,-7,1,-7,-8,-3],[1,2,7,-4,8,3,-7,2,-5,-2,-8,-5,6,-3,7,5],[-3,7,-10,-1,10,-2,3,10,2,6,-10,-10,-1,5,10,7],[9,-5,4,9,-10,-10,6,2,-3,-9,-9,3,3,9,10,-9]],[[1,-1,-10,8,3,4,9,7,-4,5,5,-5,-6,4,-2,8],[-6,6,-9,-5,-4,2,-7,-3,7,-4,8,1,-4,1,-7,-9],[7,-1,2,9,-7,9,-1,-6,-2,9,10,5,6,-1,-6,9],[6,8,-8,-3,-7,10,7,-4,-6,1,6,1,-4,6,1,-1],[-3,-4,-7,7,-1,4,1,-7,3,-3,3,-1,-6,-5,2,3],[-9,8,8,-2,10,-5,3,8,-7,5,4,-7,2,-7,-1,10],[9,-6,1,4,-3,2,10,-2,-2,-8,-2,5,8,8,4,9],[-6,-2,4,-10,-6,3,-4,-2,-1,-3,5,8,-1,5,6,9],[-1,-1,-9,-2,-5,1,-1,8,-5,-4,8,-6,-10,-2,-4,-10],[-6,-10,4,-9,10,-2,5,2,8,2,9,3,-10,-6,10,1],[-7,-10,-4,1,9,4,3,3,1,-5,5,10,5,-10,-1,10],[2,10,6,-10,7,10,10,-9,-1,9,-4,-9,-4,3,-10,5],[10,-7,-9,5,3,-5,-9,3,-1,-3,-1,4,-3,-3,10,4],[3,10,2,-7,-9,7,-9,7,3,6,4,3,7,-10,-4,-8]],[[-8,9,2,-5,2,-10,-4,-2,-6,-5,10,-10,4,3,6,6],[-10,4,-3,-2,4,-8,8,7,8,-8,10,5,-8,1,-10,10],[2,-1,-4,1,-6,8,9,-9,7,-5,-5,-8,-1,-7,-6,2],[-2,4,-7,-5,4,-8,-9,9,-4,3,-7,2,-4,10,7,-9],[-6,-4,9,-5,-3,5,-9,1,9,3,-7,-5,-6,-10,-6,4],[3,4,-7,5,1,5,-2,-5,10,-8,-5,-9,-7,-5,-9,6],[7,4,-10,-6,-8,-3,7,5,6,-6,8,1,6,10,-5,9],[-8,-5,-3,1,4,-4,-4,10,-2,-2,-2,6,8,-5,-4,-6],[7,-3,4,2,10,1,-4,-5,-5,-7,-9,-7,10,-2,4,1],[1,2,9,-5,9,-4,-5,9,7,9,10,-5,-7,7,6,5],[-3,5,2,-3,-8,-5,-8,-4,-10,-1,10,1,4,9,7,9],[10,1,6,4,-3,-6,3,7,5,-6,-5,-10,-6,-9,4,4],[-2,7,-1,1,-10,-8,-6,-6,5,4,8,1,5,-10,7,-3],[9,8,-1,-5,-3,1,7,8,1,6,-8,-5,8,-1,9,6]],[[6,-9,3,7,8,5,7,-9,-7,-8,-1,-9,-8,4,8,7],[-5,10,-2,-2,-5,6,-2,10,10,-8,1,-2,10,8,7,10],[10,8,5,2,10,-1,5,-4,9,7,-9,-9,-6,-5,-2,5],[-6,-4,6,2,6,-8,5,7,4,-4,-5,-2,-9,4,-5,-5],[-1,-2,7,-2,-7,3,2,4,3,9,-10,-7,-9,2,9,4],[6,-8,10,-5,8,-7,-9,-6,-8,10,-5,8,-9,7,8,7],[-7,-9,5,-2,-4,-3,9,-5,2,6,4,3,-4,1,-2,-8],[-7,4,10,5,4,-9,7,1,-3,9,10,-3,2,6,6,3],[-10,-3,4,6,-6,-2,-3,4,-9,-3,5,-3,2,1,3,9],[-10,6,10,1,-9,1,-7,7,-6,-6,6,7,9,6,-1,-7],[-7,6,-5,5,9,5,1,-3,2,-9,9,8,6,-1,-9,10],[3,5,-5,1,6,-10,-8,5,2,-10,-2,8,2,-6,10,-7],[4,-1,2,-2,8,7,-7,-7,8,10,6,7,9,-9,1,-2],[-7,3,4,10,-9,9,-9,7,-6,7,-6,3,8,-4,7,-6]],[[-8,-6,6,4,2,3,4,1,8,-5,4,10,8,-3,-2,3],[-7,2,-4,-9,4,2,-2,7,2,-6,9,-8,-2,4,-9,-5],[6,8,-6,8,8,7,2,-4,7,1,-6,3,-2,-3,3,-5],[-7,-9,-1,4,-7,-3,-6,-3,5,-1,5,-10,-2,-7,-4,6],[-7,-4,-3,10,-9,7,8,-2,-6,-7,-6,9,1,-5,-6,6],[-7,4,9,8,-6,7,8,10,-2,-6,-3,8,-9,-1,-3,10],[9,10,7,8,-4,9,4,-6,4,5,-5,3,8,-8,-1,1],[-4,8,10,7,2,-3,-5,3,1,9,2,9,-4,-1,7,4],[4,5,9,7,7,-6,-9,2,-8,7,10,10,-4,10,-2,5],[8,1,1,9,-7,8,3,-7,10,-10,9,6,-10,5,3,-9],[1,8,-7,-7,1,10,7,6,-1,-8,8,-4,-10,-2,10,-4],[3,-10,-9,3,-4,6,10,9,-8,-2,8,-5,-4,1,-8,4],[7,2,-2,-5,-7,10,-3,-9,-5,-9,4,3,-1,-3,-9,2],[10,1,-8,2,9,3,2,-5,2,2,-8,-5,1,-7,4,8]],[[1,7,8,-5,1,9,1,-10,5,-10,-9,1,-2,4,-8,-1],[2,10,-5,-4,-4,-10,6,7,-2,-6,3,-4,-6,2,-9,-4],[-9,10,1,2,9,-2,2,8,-8,6,2,6,-8,-3,-1,9],[-5,-4,5,2,8,10,-3,3,-5,-3,-10,-8,-9,-7,-9,-8],[5,1,-2,3,8,9,4,-3,2,7,-6,10,5,6,4,-10],[-8,7,3,9,5,-3,3,-5,5,-6,-6,-8,4,5,-8,6],[-6,-5,5,10,-3,7,2,-10,6,8,4,1,8,7,2,1],[6,-7,-9,1,4,7,-9,-1,-4,-7,4,6,7,-7,7,-7],[3,4,-2,5,2,-2,-10,-8,-3,-1,-4,-1,2,-9,6,-2],[1,3,2,1,-2,4,7,4,-8,9,6,2,7,-9,-9,-2],[-8,4,-4,1,-8,-6,9,-7,9,-9,-5,4,-4,5,-3,-2],[1,-8,-10,1,-6,-7,8,-1,9,3,1,-5,10,8,6,-4],[-7,4,-3,-9,1,-3,-9,10,-4,-1,-10,-4,6,-4,4,-1],[-10,2,9,2,5,-3,-10,2,5,3,-2,8,8,2,9,5]],[[-10,3,-6,1,10,8,6,6,-5,-9,-5,-9,-6,-5,6,-4],[-4,-8,-10,6,5,-2,5,-4,-6,-9,7,-3,1,-8,5,5],[-9,-2,4,-10,1,1,9,-6,6,5,-3,6,6,3,6,-1],[-3,-5,-10,-7,7,4,-1,3,6,-3,-8,-5,5,-6,-7,7],[9,-6,-6,-7,-1,3,3,-1,5,10,-5,10,4,-10,-2,-3],[-6,7,2,-9,6,6,7,8,5,9,-4,7,-6,3,3,-8],[-4,5,10,-10,-5,6,6,-5,-4,1,5,8,-7,9,6,1],[2,-8,7,1,-6,3,2,3,6,6,3,3,4,2,-9,9],[-8,-8,-3,-8,-7,-1,10,-7,-9,8,-6,4,4,9,8,9],[-5,10,5,8,-8,2,-4,-6,3,-9,-6,-10,-8,4,-9,1],[-9,3,-10,7,-10,9,8,-1,9,10,4,6,1,9,4,-3],[4,8,-6,3,3,-4,-7,-2,6,2,3,3,9,-5,5,-5],[-3,2,-5,7,-8,9,-5,-2,6,-10,-1,5,6,-2,-8,-9],[-7,10,7,9,8,1,-10,4,-6,-5,7,6,1,-4,4,-10]]], dtype = "uint64")#candidate|5691|(7, 14, 16)|const|uint64
bop_5692 = relay.multiply(const_5681.astype('uint32'), relay.reshape(const_5691.astype('uint32'), relay.shape_of(const_5681))) # shape=(7, 14, 16)
func_2896_call = mod.get_global_var('func_2896')
func_2898_call = mutated_mod.get_global_var('func_2898')
var_5701 = relay.var("var_5701", dtype = "float32", shape = (1260,))#candidate|5701|(1260,)|var|float32
call_5700 = relay.TupleGetItem(func_2896_call(relay.reshape(var_5701.astype('float32'), [10, 9, 14])), 0)
call_5702 = relay.TupleGetItem(func_2898_call(relay.reshape(var_5701.astype('float32'), [10, 9, 14])), 0)
output = relay.Tuple([bop_5683,bop_5692,call_5700,var_5701,])
output2 = relay.Tuple([bop_5683,bop_5692,call_5702,var_5701,])
func_5703 = relay.Function([var_5701,], output)
mod['func_5703'] = func_5703
mod = relay.transform.InferType()(mod)
var_5704 = relay.var("var_5704", dtype = "float32", shape = (1260,))#candidate|5704|(1260,)|var|float32
output = func_5703(var_5704)
func_5705 = relay.Function([var_5704], output)
mutated_mod['func_5705'] = func_5705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3848_call = mod.get_global_var('func_3848')
func_3850_call = mutated_mod.get_global_var('func_3850')
call_5798 = relay.TupleGetItem(func_3848_call(), 2)
call_5799 = relay.TupleGetItem(func_3850_call(), 2)
func_2203_call = mod.get_global_var('func_2203')
func_2205_call = mutated_mod.get_global_var('func_2205')
call_5801 = relay.TupleGetItem(func_2203_call(), 0)
call_5802 = relay.TupleGetItem(func_2205_call(), 0)
func_4540_call = mod.get_global_var('func_4540')
func_4542_call = mutated_mod.get_global_var('func_4542')
var_5804 = relay.var("var_5804", dtype = "float64", shape = (462, 2))#candidate|5804|(462, 2)|var|float64
call_5803 = relay.TupleGetItem(func_4540_call(relay.reshape(var_5804.astype('float64'), [12, 7, 11])), 0)
call_5805 = relay.TupleGetItem(func_4542_call(relay.reshape(var_5804.astype('float64'), [12, 7, 11])), 0)
func_4663_call = mod.get_global_var('func_4663')
func_4664_call = mutated_mod.get_global_var('func_4664')
call_5808 = relay.TupleGetItem(func_4663_call(), 0)
call_5809 = relay.TupleGetItem(func_4664_call(), 0)
func_2677_call = mod.get_global_var('func_2677')
func_2679_call = mutated_mod.get_global_var('func_2679')
call_5849 = relay.TupleGetItem(func_2677_call(), 0)
call_5850 = relay.TupleGetItem(func_2679_call(), 0)
uop_5855 = relay.sin(var_5804.astype('float32')) # shape=(462, 2)
uop_5858 = relay.log2(var_5804.astype('float64')) # shape=(462, 2)
func_2428_call = mod.get_global_var('func_2428')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_5861 = func_2428_call()
call_5862 = func_2428_call()
output = relay.Tuple([call_5798,call_5801,call_5803,call_5808,call_5849,uop_5855,uop_5858,call_5861,])
output2 = relay.Tuple([call_5799,call_5802,call_5805,call_5809,call_5850,uop_5855,uop_5858,call_5862,])
func_5873 = relay.Function([var_5804,], output)
mod['func_5873'] = func_5873
mod = relay.transform.InferType()(mod)
mutated_mod['func_5873'] = func_5873
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5874 = relay.var("var_5874", dtype = "float64", shape = (462, 2))#candidate|5874|(462, 2)|var|float64
func_5873_call = mutated_mod.get_global_var('func_5873')
call_5875 = func_5873_call(var_5874)
output = call_5875
func_5876 = relay.Function([var_5874], output)
mutated_mod['func_5876'] = func_5876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2915_call = mod.get_global_var('func_2915')
func_2917_call = mutated_mod.get_global_var('func_2917')
call_5894 = func_2915_call()
call_5895 = func_2915_call()
uop_5918 = relay.cosh(call_5894.astype('float32')) # shape=(10, 9, 14)
uop_5920 = relay.cosh(call_5895.astype('float32')) # shape=(10, 9, 14)
uop_5922 = relay.acosh(call_5894.astype('float64')) # shape=(10, 9, 14)
uop_5924 = relay.acosh(call_5895.astype('float64')) # shape=(10, 9, 14)
output = relay.Tuple([uop_5918,uop_5922,])
output2 = relay.Tuple([uop_5920,uop_5924,])
func_5934 = relay.Function([], output)
mod['func_5934'] = func_5934
mod = relay.transform.InferType()(mod)
output = func_5934()
func_5935 = relay.Function([], output)
mutated_mod['func_5935'] = func_5935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3635_call = mod.get_global_var('func_3635')
func_3637_call = mutated_mod.get_global_var('func_3637')
call_5949 = func_3635_call()
call_5950 = func_3635_call()
output = relay.Tuple([call_5949,])
output2 = relay.Tuple([call_5950,])
func_5954 = relay.Function([], output)
mod['func_5954'] = func_5954
mod = relay.transform.InferType()(mod)
mutated_mod['func_5954'] = func_5954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5954_call = mutated_mod.get_global_var('func_5954')
call_5955 = func_5954_call()
output = call_5955
func_5956 = relay.Function([], output)
mutated_mod['func_5956'] = func_5956
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5998 = relay.const([[[-4.685000,7.306429],[-6.495577,0.020454],[1.519586,-0.281333],[-9.682445,-3.972393],[8.735839,6.321920],[8.110518,-6.080864],[-6.592000,6.542786],[2.160449,-9.849236],[7.543724,3.545720],[5.739352,5.371034],[8.691558,-5.335179],[0.509430,-8.462083],[-5.938705,-8.826735],[5.389321,2.133364],[-0.247007,-1.417874]],[[-7.851673,7.414604],[-8.719325,5.892369],[7.298638,-0.933210],[5.218991,-8.974776],[5.477705,2.747035],[-6.497399,-2.881565],[-3.189299,8.910300],[-1.245442,-0.608887],[7.208674,-6.625029],[3.565440,1.249031],[7.015311,3.860554],[-4.766133,3.240424],[-9.516410,5.573342],[-9.894917,9.288543],[-4.395045,0.784861]],[[-8.766314,6.273931],[0.923118,-8.985150],[2.265555,2.268543],[2.356273,6.717688],[-5.460405,-7.568213],[9.948137,9.911112],[2.732134,7.883756],[8.998234,-1.713091],[-3.656249,4.810842],[-7.308748,-1.092563],[8.462329,-2.251475],[9.038801,-2.846471],[-6.170885,-3.386066],[0.140308,7.046299],[-6.952960,-5.984608]],[[5.744639,-7.254440],[-2.069253,1.937946],[1.166848,-2.376389],[9.176421,0.208006],[4.817472,-5.185429],[-2.388618,1.013428],[-0.709098,-2.385561],[1.119512,-9.384103],[-8.845861,3.966159],[9.533741,0.954517],[-6.092164,5.516239],[-1.160864,-5.432506],[1.139000,6.311033],[-8.216682,8.492825],[8.921442,0.798176]]], dtype = "float32")#candidate|5998|(4, 15, 2)|const|float32
uop_5999 = relay.exp(const_5998.astype('float32')) # shape=(4, 15, 2)
func_3715_call = mod.get_global_var('func_3715')
func_3716_call = mutated_mod.get_global_var('func_3716')
call_6009 = func_3715_call()
call_6010 = func_3715_call()
func_1289_call = mod.get_global_var('func_1289')
func_1291_call = mutated_mod.get_global_var('func_1291')
call_6015 = relay.TupleGetItem(func_1289_call(), 1)
call_6016 = relay.TupleGetItem(func_1291_call(), 1)
output = relay.Tuple([uop_5999,call_6009,call_6015,])
output2 = relay.Tuple([uop_5999,call_6010,call_6016,])
func_6047 = relay.Function([], output)
mod['func_6047'] = func_6047
mod = relay.transform.InferType()(mod)
mutated_mod['func_6047'] = func_6047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6047_call = mutated_mod.get_global_var('func_6047')
call_6048 = func_6047_call()
output = call_6048
func_6049 = relay.Function([], output)
mutated_mod['func_6049'] = func_6049
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6050 = relay.const([[[7.730750,-7.581825,-0.936641,-9.363080,-6.318705,-6.186631,8.201245,-7.778901,0.336745,-5.537094,9.769558,4.410147,-6.182518,8.630189,8.384280,-6.888016]],[[9.365870,2.990101,-6.163889,-7.225722,3.310885,6.725431,7.013608,3.537357,-6.232540,0.871896,-1.311517,2.380720,0.162991,-0.699623,4.362534,-7.305742]]], dtype = "float64")#candidate|6050|(2, 1, 16)|const|float64
uop_6051 = relay.erf(const_6050.astype('float64')) # shape=(2, 1, 16)
output = uop_6051
output2 = uop_6051
func_6059 = relay.Function([], output)
mod['func_6059'] = func_6059
mod = relay.transform.InferType()(mod)
output = func_6059()
func_6060 = relay.Function([], output)
mutated_mod['func_6060'] = func_6060
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6074 = relay.var("var_6074", dtype = "float64", shape = (14, 16))#candidate|6074|(14, 16)|var|float64
uop_6075 = relay.log2(var_6074.astype('float64')) # shape=(14, 16)
output = relay.Tuple([uop_6075,])
output2 = relay.Tuple([uop_6075,])
func_6077 = relay.Function([var_6074,], output)
mod['func_6077'] = func_6077
mod = relay.transform.InferType()(mod)
var_6078 = relay.var("var_6078", dtype = "float64", shape = (14, 16))#candidate|6078|(14, 16)|var|float64
output = func_6077(var_6078)
func_6079 = relay.Function([var_6078], output)
mutated_mod['func_6079'] = func_6079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1990_call = mod.get_global_var('func_1990')
func_1992_call = mutated_mod.get_global_var('func_1992')
call_6181 = relay.TupleGetItem(func_1990_call(), 0)
call_6182 = relay.TupleGetItem(func_1992_call(), 0)
func_1472_call = mod.get_global_var('func_1472')
func_1475_call = mutated_mod.get_global_var('func_1475')
const_6188 = relay.const([-9.034938,1.321915,-0.209148,-7.411746,2.595273,-1.816719,-0.885882,-8.793995,-4.753020,2.551537,7.500735,9.333326,6.897141,3.897366,1.528121,1.105872,2.273354,-1.650102,-7.259092,4.162184,-5.182405,3.831149,7.858371,8.854041,-1.753257,-3.621539,8.422331,-6.532478,6.193292,-7.903094,-6.488302,5.006550,-7.552489,-8.653714,-2.326072,-6.431550,3.212451,0.800726,5.254493,0.871745,2.883296,9.740559,8.158934,-3.761096,-3.695669,1.653071,-8.359639,-0.038088,-2.896869,5.857049,-3.118349,0.439702,0.973607,8.109485,-1.483646,9.106035,-4.476116,-2.059622,-0.967914,7.007831,3.029212,8.708540,2.896032,-8.006911,-5.001639,-1.381615,6.499866,5.548835,-6.183440,3.556170,1.418527,-8.138427,-2.656644,1.892647,0.212284,8.000432,8.581544,-8.077600,-5.969982,-1.350626,-6.689373,2.025261,6.233611,2.987432,2.741642,-8.853039,7.262376,0.152587,4.048564,-4.632558,8.771128,-2.493294,-2.386487,5.852929,0.917567,-6.462745,-4.943783,-6.539451,-1.707778,8.583347,-6.823131,-1.016196,-2.207496,6.230917,-5.588906,3.709641,6.295744,-1.011180,-3.872339,-0.270803,0.575760,-7.754280,5.045511,3.738524,-8.410782,6.794988,-4.121108,-7.716593,1.209642,3.263428,6.383148,8.688493,-3.988974,-0.740888,9.606982,-4.629985,7.867449,-6.627358,3.860484,-7.423940,-7.615088,3.315419,4.615563,-3.987791,7.690966,-6.430593,-4.442388,-8.384159,2.335786,0.282106,1.114438,-4.016233,-0.011807,1.744804,-8.442005,2.127827,-8.025109,-8.755556,-7.341400,-3.288523,-8.286758,-9.965165,2.085355,4.688873,-0.581299,0.088368,-1.862988,-5.408604,8.601736,7.363148,-0.662628,-0.680094,4.250947,-4.630899,4.242041,1.107000,-0.106753,-5.220620,-9.463019,-8.529071,1.307000,4.128227,5.718086,-5.154720,6.258178,0.736904,1.544855,-5.768793,-1.257264,-4.184231,-1.930403,7.200776,-6.268622,-9.926512,4.115322,6.732292,-1.047337,-4.566341,-8.508430,-9.485969,-7.582497,2.164060,-0.941342,-3.508838,8.836101,-5.137672,5.493071,-3.255777,-2.389761,-4.030007,5.635901,-2.073441,-4.133854,-9.269675,3.406251,7.346767,-2.755865,7.968543,-3.821883,0.109787,2.629875,2.278064,1.223729,-0.347549,-2.232985,7.193188,-0.684741,-5.454820,-8.152172,6.373368,8.337406,-0.774691,-8.103508,-8.777906,8.562482,-8.113242,-4.048076,4.929695,2.331965,6.480497,0.260217,2.151811,-7.871691,-4.402815,-9.097655,-7.171377,-1.230022,5.510637,4.327289,-9.011374,7.166454,9.236776,-0.227249,5.325884,-1.015669,-0.663975,2.626763,1.851790,3.709103,3.818236,8.348309,6.827906,-5.430379,-4.827219,6.922082,-2.522516,7.681399,-7.858352,7.487899,2.054934,-4.379953,7.337682,-6.634969,5.272561,-1.835240,0.017177,-1.654023,-0.664667,-1.491344,-2.158153,6.351638,-4.056939,-1.502992,-5.933377,1.728351,6.119386,6.764961,2.110012,0.067357,4.928001,4.737182,-5.535441,-4.540825,-7.883481,5.934404,-6.866272,-0.683660,-1.477269,9.323022,-0.355991,-1.058880,-7.740856,-3.789603,1.611611,-4.350586,8.162215,-7.524528,7.759895,-3.716743,9.800074], dtype = "float64")#candidate|6188|(300,)|const|float64
call_6187 = func_1472_call(relay.reshape(const_6188.astype('float64'), [10, 6, 5]))
call_6189 = func_1472_call(relay.reshape(const_6188.astype('float64'), [10, 6, 5]))
func_830_call = mod.get_global_var('func_830')
func_834_call = mutated_mod.get_global_var('func_834')
const_6193 = relay.const([7.542035,-0.112925,-5.447673,9.226046,1.200826,7.632704,-3.795760,-6.997356,8.871227,3.086879,7.624311,-1.929431,-7.282225,-0.309028,3.406122,-6.544763,0.306242,3.687828,-1.891042,0.642842,2.899687,5.672626,-0.472395,6.123780,-6.396437,-3.882203,1.781731,-1.256100,-8.408447,6.172565,-3.988060,-6.375639,6.432112,2.086210,-2.722672,8.180699,1.423715,2.652489,-3.782672,6.370646,7.643979,-5.821711,-7.260326,-1.204477,9.175818,-0.385460,-9.781408,0.340490,-6.098932,0.602716,2.132769,6.112839,5.418148,2.024535,1.006207,9.037237,-6.548404,1.823938,-0.121204,7.106214,9.453260,8.255829,-6.887636,5.446756,2.978443,-8.555993,1.823430,3.557660,-8.340773,-5.503232,1.661548,5.083726,-0.739221,-5.735848,-2.707796,-0.323159,0.416868,9.350140,5.655117,-6.440448,4.637683,2.024039,-5.593750,-3.769149,0.600231,-8.474973,-7.797272,-3.037947,-7.738308,5.156685,-6.917054,4.260547,8.871083,-6.803925,3.606959,5.590224,9.629171,-5.751214,2.189265,-9.989792,0.892565,2.028511,-3.843161,-2.434116,-4.365545,-1.026807,-2.379355,-8.904791,-4.836578,-7.179924,5.897689,1.933779,-6.760269,4.356298,-9.095332,8.324687,-8.258679,9.943550,-2.942468,-4.773002,6.254368,-2.318510,-7.784705,0.574638,5.190542,-1.703900,5.469022,3.119617,7.921996,4.757724,-7.410119,-5.750807], dtype = "float64")#candidate|6193|(132,)|const|float64
const_6194 = relay.const([2.276202,-6.701247,9.211998,-6.690272,3.403623,-8.474900,5.734001,8.418546,-1.904063,3.332122,4.357451,4.049133,3.449354,9.550584,5.606909,-9.975907,-0.699602,1.962152,5.924911,4.610330,6.426374,8.247930,-1.976979,6.791266,8.525697,6.896015,2.113135,1.307932,-2.944743,6.961355,-4.048715,-2.957163,-0.145670,-1.573035,-2.842369,-1.074739,2.110472,-9.976276,7.657652,8.170230,-1.743373,0.914498,1.502632,-4.721037,3.303366,-9.689473,-9.837460,-4.794864,-2.254173,-1.434907,-0.417007,7.323457,2.836186,-0.672728,3.387828,7.832567,-6.359522,-3.883882,1.896691,4.552834,-8.469702,-6.896985,-6.857679,-6.519810,3.035494,9.253096,4.568358,-8.084807,0.100514,6.940787,-5.062074,-6.342945,-2.377753,-2.059689,-9.500276,-6.602526,3.280279,7.467449,-4.890558,6.360022,-9.454779,5.552748,9.631819,-7.540687,-4.762820,5.096087,6.727445,1.120414,-2.203670,3.449384,8.641249,-8.573293,2.148408,3.588813,2.944531,6.043555,6.047789,7.246700,-6.215113,1.630630,-8.160806,7.119062,2.359863,0.690342,0.022109,-1.138175,-4.313647,8.979297,-2.192007,6.965483,2.412908,3.532033,-2.765137,1.773855,1.440323,5.056441,-4.245874,0.413284,-9.901931,2.766791,2.989488,-3.604314,-2.842440,3.864267,-8.733813,-8.056817], dtype = "float32")#candidate|6194|(126,)|const|float32
call_6192 = relay.TupleGetItem(func_830_call(relay.reshape(const_6193.astype('float64'), [2, 6, 11]), relay.reshape(const_6194.astype('float32'), [126,]), ), 3)
call_6195 = relay.TupleGetItem(func_834_call(relay.reshape(const_6193.astype('float64'), [2, 6, 11]), relay.reshape(const_6194.astype('float32'), [126,]), ), 3)
func_3407_call = mod.get_global_var('func_3407')
func_3408_call = mutated_mod.get_global_var('func_3408')
call_6201 = func_3407_call()
call_6202 = func_3407_call()
var_6220 = relay.var("var_6220", dtype = "float64", shape = (132,))#candidate|6220|(132,)|var|float64
bop_6221 = relay.multiply(const_6193.astype('uint16'), relay.reshape(var_6220.astype('uint16'), relay.shape_of(const_6193))) # shape=(132,)
bop_6226 = relay.subtract(const_6188.astype('float64'), relay.reshape(call_6187.astype('float64'), relay.shape_of(const_6188))) # shape=(300,)
bop_6229 = relay.subtract(const_6188.astype('float64'), relay.reshape(call_6189.astype('float64'), relay.shape_of(const_6188))) # shape=(300,)
uop_6235 = relay.sinh(bop_6226.astype('float64')) # shape=(300,)
uop_6237 = relay.sinh(bop_6229.astype('float64')) # shape=(300,)
uop_6242 = relay.tan(uop_6235.astype('float32')) # shape=(300,)
uop_6244 = relay.tan(uop_6237.astype('float32')) # shape=(300,)
output = relay.Tuple([call_6181,call_6192,const_6194,call_6201,bop_6221,uop_6242,])
output2 = relay.Tuple([call_6182,call_6195,const_6194,call_6202,bop_6221,uop_6244,])
func_6245 = relay.Function([var_6220,], output)
mod['func_6245'] = func_6245
mod = relay.transform.InferType()(mod)
var_6246 = relay.var("var_6246", dtype = "float64", shape = (132,))#candidate|6246|(132,)|var|float64
output = func_6245(var_6246)
func_6247 = relay.Function([var_6246], output)
mutated_mod['func_6247'] = func_6247
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6303 = relay.const([[[True,False,False,False,False,False,False,False,False,True,False,False],[False,True,False,False,False,True,True,False,True,False,False,True],[True,False,False,True,False,True,True,True,False,False,True,False],[False,True,True,False,True,True,False,True,False,True,True,False],[False,True,True,True,True,True,False,False,True,False,False,True],[False,True,False,False,True,True,False,True,True,True,False,False],[True,False,True,True,True,False,False,False,True,True,True,True],[False,False,True,True,False,True,False,False,True,False,False,False],[True,True,False,False,False,False,False,True,False,True,True,False]],[[False,True,False,True,False,True,False,False,True,False,True,False],[True,True,False,False,True,True,True,False,False,True,True,False],[True,True,False,True,True,True,True,True,False,True,False,False],[True,True,False,False,True,True,False,False,False,True,True,True],[False,False,True,False,True,False,False,False,False,False,True,True],[True,True,False,True,False,False,True,True,True,True,False,False],[False,False,True,False,True,False,True,True,False,True,True,True],[True,False,True,True,False,False,False,False,True,False,True,False],[True,True,True,False,False,True,True,True,False,False,True,True]],[[False,True,True,False,False,False,True,True,False,False,True,True],[False,True,True,False,False,False,False,True,True,True,True,False],[True,False,True,True,False,False,False,False,True,True,False,True],[False,True,True,False,True,False,True,False,True,False,False,True],[True,False,False,False,True,False,False,False,False,True,True,True],[False,False,True,True,True,False,True,True,True,False,False,True],[False,True,True,True,False,True,True,True,True,True,True,False],[True,False,True,False,True,False,True,True,False,False,True,False],[False,False,True,False,False,True,True,False,True,False,True,True]],[[True,False,False,False,False,True,False,True,True,True,True,True],[False,False,False,False,True,True,False,True,True,False,True,True],[True,False,True,False,False,True,True,True,True,True,True,True],[True,False,True,False,True,False,True,True,True,False,False,False],[True,False,True,True,False,True,False,False,True,False,False,False],[True,False,True,False,True,True,False,False,True,True,True,False],[True,False,False,False,False,False,False,False,False,False,True,True],[True,True,True,False,True,True,False,False,True,False,True,True],[True,True,True,False,False,False,False,True,True,False,False,True]],[[False,False,True,True,False,False,False,True,False,True,False,True],[False,False,False,False,False,True,True,True,False,False,True,False],[True,False,True,False,False,True,True,True,False,True,False,False],[True,False,False,True,True,False,True,True,False,True,True,True],[False,False,False,False,True,False,False,False,False,True,False,False],[True,True,True,True,False,True,True,False,True,True,True,False],[True,False,False,False,True,True,True,True,False,True,True,True],[True,True,True,True,True,True,False,False,False,True,True,True],[True,False,True,False,False,False,True,True,True,True,True,False]]], dtype = "bool")#candidate|6303|(5, 9, 12)|const|bool
const_6304 = relay.const([[[False,False,False,False,True,True,True,True,False,True,False,True],[True,False,False,False,True,True,True,True,False,False,True,False],[True,True,True,False,False,False,False,True,False,True,True,True],[False,False,False,True,True,False,False,False,False,False,True,True],[True,False,True,True,False,False,False,True,True,True,True,False],[True,False,True,True,True,False,True,True,False,True,False,False],[False,True,False,False,True,True,False,True,False,True,False,False],[True,False,False,True,False,True,True,True,True,False,True,False],[False,False,False,False,True,False,False,True,True,True,False,True]],[[False,False,False,False,True,False,True,False,True,True,True,True],[False,False,False,False,False,True,False,False,True,False,True,True],[True,True,False,False,False,False,True,True,False,True,True,True],[False,False,False,True,True,True,False,False,False,False,False,False],[False,False,True,True,True,False,False,False,True,True,False,False],[True,False,True,False,True,False,True,True,True,True,False,False],[True,False,False,True,True,False,True,True,True,False,False,False],[False,True,False,False,False,False,False,True,False,True,True,False],[True,True,True,False,False,False,True,True,False,True,False,True]],[[False,False,False,True,False,True,True,True,False,True,True,False],[True,True,True,False,False,True,False,True,False,True,False,False],[True,True,False,False,False,False,True,False,False,False,True,True],[True,False,False,True,True,True,True,True,False,False,True,False],[True,True,True,True,False,True,False,False,False,False,False,True],[False,True,True,True,True,True,False,False,True,False,True,True],[True,False,False,True,True,True,True,False,False,False,False,False],[False,False,False,False,False,False,True,False,False,True,True,True],[False,True,False,True,True,True,False,False,False,False,True,True]],[[True,False,True,True,True,True,False,True,True,False,True,True],[True,True,False,True,False,True,False,False,True,False,True,False],[False,False,True,False,False,False,True,False,True,False,True,False],[False,True,True,True,False,False,True,True,True,True,False,True],[False,False,True,True,True,True,False,True,True,True,True,True],[True,False,True,False,False,True,False,False,False,True,False,False],[False,True,True,True,False,True,True,False,False,False,False,True],[True,False,False,False,True,True,False,False,True,True,True,True],[False,True,False,True,True,False,True,True,True,True,False,True]],[[False,True,True,False,False,True,True,True,True,True,False,False],[False,False,True,True,True,False,True,False,True,True,True,False],[True,False,True,False,True,False,True,False,True,False,False,True],[False,False,True,True,True,True,False,False,True,True,True,False],[True,False,False,False,True,True,True,False,False,False,False,True],[False,True,True,False,False,False,True,False,False,False,True,True],[True,True,True,False,False,True,True,True,True,True,False,True],[True,True,True,True,True,False,False,False,True,False,False,True],[False,True,True,False,False,True,True,True,False,True,False,True]]], dtype = "bool")#candidate|6304|(5, 9, 12)|const|bool
bop_6305 = relay.logical_and(const_6303.astype('bool'), relay.reshape(const_6304.astype('bool'), relay.shape_of(const_6303))) # shape=(5, 9, 12)
bop_6314 = relay.bitwise_and(const_6303.astype('uint32'), relay.reshape(bop_6305.astype('uint32'), relay.shape_of(const_6303))) # shape=(5, 9, 12)
output = relay.Tuple([bop_6314,])
output2 = relay.Tuple([bop_6314,])
func_6329 = relay.Function([], output)
mod['func_6329'] = func_6329
mod = relay.transform.InferType()(mod)
output = func_6329()
func_6330 = relay.Function([], output)
mutated_mod['func_6330'] = func_6330
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6354 = relay.var("var_6354", dtype = "float32", shape = (13, 12, 8))#candidate|6354|(13, 12, 8)|var|float32
uop_6355 = relay.acosh(var_6354.astype('float32')) # shape=(13, 12, 8)
output = relay.Tuple([uop_6355,])
output2 = relay.Tuple([uop_6355,])
func_6357 = relay.Function([var_6354,], output)
mod['func_6357'] = func_6357
mod = relay.transform.InferType()(mod)
var_6358 = relay.var("var_6358", dtype = "float32", shape = (13, 12, 8))#candidate|6358|(13, 12, 8)|var|float32
output = func_6357(var_6358)
func_6359 = relay.Function([var_6358], output)
mutated_mod['func_6359'] = func_6359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5285_call = mod.get_global_var('func_5285')
func_5286_call = mutated_mod.get_global_var('func_5286')
call_6420 = relay.TupleGetItem(func_5285_call(), 0)
call_6421 = relay.TupleGetItem(func_5286_call(), 0)
output = relay.Tuple([call_6420,])
output2 = relay.Tuple([call_6421,])
func_6440 = relay.Function([], output)
mod['func_6440'] = func_6440
mod = relay.transform.InferType()(mod)
mutated_mod['func_6440'] = func_6440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6440_call = mutated_mod.get_global_var('func_6440')
call_6441 = func_6440_call()
output = call_6441
func_6442 = relay.Function([], output)
mutated_mod['func_6442'] = func_6442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_909_call = mod.get_global_var('func_909')
func_910_call = mutated_mod.get_global_var('func_910')
call_6466 = relay.TupleGetItem(func_909_call(), 0)
call_6467 = relay.TupleGetItem(func_910_call(), 0)
func_1223_call = mod.get_global_var('func_1223')
func_1224_call = mutated_mod.get_global_var('func_1224')
call_6477 = func_1223_call()
call_6478 = func_1223_call()
func_2572_call = mod.get_global_var('func_2572')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_6479 = relay.TupleGetItem(func_2572_call(), 0)
call_6480 = relay.TupleGetItem(func_2574_call(), 0)
output = relay.Tuple([call_6466,call_6477,call_6479,])
output2 = relay.Tuple([call_6467,call_6478,call_6480,])
func_6483 = relay.Function([], output)
mod['func_6483'] = func_6483
mod = relay.transform.InferType()(mod)
output = func_6483()
func_6484 = relay.Function([], output)
mutated_mod['func_6484'] = func_6484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5564_call = mod.get_global_var('func_5564')
func_5566_call = mutated_mod.get_global_var('func_5566')
call_6495 = relay.TupleGetItem(func_5564_call(), 0)
call_6496 = relay.TupleGetItem(func_5566_call(), 0)
func_1436_call = mod.get_global_var('func_1436')
func_1441_call = mutated_mod.get_global_var('func_1441')
const_6498 = relay.const([-0.846387,-8.638976,-5.317616,-6.385903,-5.685438,-9.931640,-7.130817,0.418510,-8.238740,1.037332,-7.431154,8.708943,-4.606588,0.797334,4.431259,4.220586,-2.924530,-4.044174,2.387369,8.586179,3.285990,-1.898141,-9.061991,-1.914222,6.596411,6.543818,3.216190,-4.859344,-2.064706,7.169908,-3.023518,1.982829,7.633689,9.669510,-9.432042,-3.023817,7.247738,9.098411,-4.994200,-9.464937,-5.238568,2.008401,6.331168,4.133883,1.013793,0.772278,1.923135,3.439212,-8.020529,-2.018176,6.514813,9.031082,5.834821,-1.936822,-9.972764,5.014673,8.366401,-9.445035,-8.155245,-4.261401,7.357312,-1.025040,0.884412,7.787690,-8.220509,-6.103157,-7.294935,-9.568097,1.152774,1.922523,-3.604546,-8.037628,-2.168472,-7.935548,-1.594582,-4.494497,-6.494011,-5.491433,-9.566014,-7.551845,7.674163,-9.025611,-6.435841,-9.591441,-6.862458,9.594469,-5.610999,-7.952814,-2.975623,-5.763479,0.254778,-5.520013,0.910395,7.267208,-7.240541,-4.889421,1.815851,1.336059,-9.338519,9.799625,-3.023475,0.855254,-1.143086,7.935525,-0.486885,8.962097,-6.610171,5.316173,-9.430728,-7.662332,-5.429657,9.884902,7.280937,9.809292,-7.238333,-1.192798,4.559109,0.190779,2.748092,6.769248,-2.628098,-1.466775,-8.253918,-3.802182,-3.877443,-3.193808,-0.723211,-1.371272,-1.804188,4.124279,-6.808578,5.809460,2.852298,6.290615,6.483045], dtype = "float64")#candidate|6498|(135,)|const|float64
var_6499 = relay.var("var_6499", dtype = "float64", shape = (2025,))#candidate|6499|(2025,)|var|float64
const_6500 = relay.const([1.823581,-6.387897,-7.260538,3.054334,-2.640154,-3.950298,-3.752009,-0.747392,9.603716,-7.382450,-7.830046,0.604947,-8.320666,5.768479,-8.403611,1.892438,0.957151,4.000650,-1.132002,-0.225563,2.979413,-3.406281,-7.894563,9.421568,-8.892321,-2.404064,-4.883577,8.479412,3.164820,-3.530971,3.356563,1.200978], dtype = "float32")#candidate|6500|(32,)|const|float32
call_6497 = relay.TupleGetItem(func_1436_call(relay.reshape(const_6498.astype('float64'), [1, 15, 9]), relay.reshape(var_6499.astype('float64'), [15, 15, 9]), relay.reshape(const_6500.astype('float32'), [32,]), ), 0)
call_6501 = relay.TupleGetItem(func_1441_call(relay.reshape(const_6498.astype('float64'), [1, 15, 9]), relay.reshape(var_6499.astype('float64'), [15, 15, 9]), relay.reshape(const_6500.astype('float32'), [32,]), ), 0)
uop_6505 = relay.acos(call_6497.astype('float64')) # shape=(15, 15, 9)
uop_6507 = relay.acos(call_6501.astype('float64')) # shape=(15, 15, 9)
output = relay.Tuple([call_6495,const_6498,var_6499,const_6500,uop_6505,])
output2 = relay.Tuple([call_6496,const_6498,var_6499,const_6500,uop_6507,])
func_6515 = relay.Function([var_6499,], output)
mod['func_6515'] = func_6515
mod = relay.transform.InferType()(mod)
var_6516 = relay.var("var_6516", dtype = "float64", shape = (2025,))#candidate|6516|(2025,)|var|float64
output = func_6515(var_6516)
func_6517 = relay.Function([var_6516], output)
mutated_mod['func_6517'] = func_6517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1990_call = mod.get_global_var('func_1990')
func_1992_call = mutated_mod.get_global_var('func_1992')
call_6519 = relay.TupleGetItem(func_1990_call(), 0)
call_6520 = relay.TupleGetItem(func_1992_call(), 0)
output = relay.Tuple([call_6519,])
output2 = relay.Tuple([call_6520,])
func_6527 = relay.Function([], output)
mod['func_6527'] = func_6527
mod = relay.transform.InferType()(mod)
mutated_mod['func_6527'] = func_6527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6527_call = mutated_mod.get_global_var('func_6527')
call_6528 = func_6527_call()
output = call_6528
func_6529 = relay.Function([], output)
mutated_mod['func_6529'] = func_6529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2677_call = mod.get_global_var('func_2677')
func_2679_call = mutated_mod.get_global_var('func_2679')
call_6655 = relay.TupleGetItem(func_2677_call(), 4)
call_6656 = relay.TupleGetItem(func_2679_call(), 4)
output = relay.Tuple([call_6655,])
output2 = relay.Tuple([call_6656,])
func_6661 = relay.Function([], output)
mod['func_6661'] = func_6661
mod = relay.transform.InferType()(mod)
mutated_mod['func_6661'] = func_6661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6661_call = mutated_mod.get_global_var('func_6661')
call_6662 = func_6661_call()
output = call_6662
func_6663 = relay.Function([], output)
mutated_mod['func_6663'] = func_6663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1951_call = mod.get_global_var('func_1951')
func_1952_call = mutated_mod.get_global_var('func_1952')
call_6700 = func_1951_call()
call_6701 = func_1951_call()
func_5285_call = mod.get_global_var('func_5285')
func_5286_call = mutated_mod.get_global_var('func_5286')
call_6717 = relay.TupleGetItem(func_5285_call(), 0)
call_6718 = relay.TupleGetItem(func_5286_call(), 0)
func_3977_call = mod.get_global_var('func_3977')
func_3979_call = mutated_mod.get_global_var('func_3979')
call_6723 = func_3977_call()
call_6724 = func_3977_call()
func_2963_call = mod.get_global_var('func_2963')
func_2966_call = mutated_mod.get_global_var('func_2966')
call_6742 = relay.TupleGetItem(func_2963_call(relay.reshape(call_6723.astype('float64'), [10, 9, 14])), 0)
call_6743 = relay.TupleGetItem(func_2966_call(relay.reshape(call_6723.astype('float64'), [10, 9, 14])), 0)
output = relay.Tuple([call_6700,call_6717,call_6723,call_6742,])
output2 = relay.Tuple([call_6701,call_6718,call_6724,call_6743,])
func_6769 = relay.Function([], output)
mod['func_6769'] = func_6769
mod = relay.transform.InferType()(mod)
output = func_6769()
func_6770 = relay.Function([], output)
mutated_mod['func_6770'] = func_6770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2203_call = mod.get_global_var('func_2203')
func_2205_call = mutated_mod.get_global_var('func_2205')
call_6783 = relay.TupleGetItem(func_2203_call(), 0)
call_6784 = relay.TupleGetItem(func_2205_call(), 0)
output = relay.Tuple([call_6783,])
output2 = relay.Tuple([call_6784,])
func_6787 = relay.Function([], output)
mod['func_6787'] = func_6787
mod = relay.transform.InferType()(mod)
mutated_mod['func_6787'] = func_6787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6787_call = mutated_mod.get_global_var('func_6787')
call_6788 = func_6787_call()
output = call_6788
func_6789 = relay.Function([], output)
mutated_mod['func_6789'] = func_6789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5357_call = mod.get_global_var('func_5357')
func_5358_call = mutated_mod.get_global_var('func_5358')
call_6911 = func_5357_call()
call_6912 = func_5357_call()
uop_6915 = relay.atan(call_6911.astype('float64')) # shape=(10, 9, 14)
uop_6917 = relay.atan(call_6912.astype('float64')) # shape=(10, 9, 14)
output = relay.Tuple([uop_6915,])
output2 = relay.Tuple([uop_6917,])
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
