import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_121 = relay.const([[[6.298736,-1.471506,-4.832591,-1.914907,-1.012667,9.305502,3.909543,1.411449],[5.243777,-5.457024,-7.720795,-5.165105,-4.343823,-1.176065,7.053941,2.503438],[3.797428,-6.245851,6.582729,3.791820,-4.384681,-7.701876,3.240711,2.856081],[-9.626176,2.434079,6.212792,6.578614,2.102476,-9.934715,-5.489807,-0.398910],[7.771922,2.165923,1.650412,-7.533712,9.210748,0.395305,-3.598987,5.915516],[-7.149295,2.191993,6.564119,9.050821,-5.743424,7.248615,-6.389887,-6.570556],[-5.978471,-1.966248,-0.176150,4.506948,0.685680,7.722719,-6.892173,-3.948895],[8.429293,-0.666390,4.514959,3.849533,1.771243,-0.573445,-7.759357,2.614004],[-9.390049,6.510548,-5.916317,-9.882712,6.780124,5.534384,8.479419,9.005450],[7.366441,0.292570,6.375127,-3.291180,8.087643,-5.037236,9.900354,-2.666764],[-1.443289,-5.961400,-4.942862,-5.698800,-5.480009,4.553376,-6.964602,-0.422933]],[[-3.606725,-5.509375,4.403243,-7.830360,2.757889,-3.786751,-8.113205,-5.815923],[-2.547116,7.809394,7.132251,1.802344,4.413050,3.236366,2.944653,2.900983],[5.660158,0.197806,-6.115326,0.046136,9.373745,-6.727471,-0.518035,-2.604449],[-6.023382,-0.773731,5.030560,2.736772,-8.388264,-8.174399,7.821448,-8.729797],[4.218951,7.324122,4.288490,7.842994,-8.944815,7.903118,-4.168669,-9.823722],[8.314855,6.459342,-8.682666,-1.502443,9.107361,-1.909998,-5.097529,-1.659261],[-3.037944,-8.887831,-8.250486,-3.465677,4.168942,-4.600637,3.235109,-4.806819],[6.577991,-3.241007,2.450937,-2.979143,4.623741,0.908663,9.808865,-5.780556],[5.242989,-6.256095,-9.169941,-9.989938,-1.116534,-3.709776,1.789337,-2.742932],[-1.443294,-5.937973,8.906770,-2.700723,6.941195,8.614116,4.514722,8.364817],[-9.758199,8.659435,-8.702078,-3.798265,-3.906710,5.789416,-9.879420,-1.887248]],[[-9.150904,-2.996761,5.192611,-6.997348,-8.735200,-7.101717,3.462295,-9.171699],[8.662816,0.066791,8.763983,-7.328214,-6.159576,-1.260419,1.290893,2.975565],[2.941912,-3.845089,-0.218711,-7.657159,-9.427518,6.026866,-1.243821,5.659592],[2.959560,9.166589,-3.952910,-0.827502,5.092955,2.818309,7.124860,-0.507244],[-0.957135,1.179131,-1.411274,5.671150,-9.966894,-8.689134,-1.583298,-9.693373],[-9.287156,6.712542,0.730937,5.299312,-9.577737,-5.317662,2.215723,-0.991058],[5.628462,4.686593,5.496063,-0.341799,1.287644,-5.730144,-8.265976,3.239963],[6.318856,5.772986,-5.787927,7.921064,-4.634170,-4.241197,2.773177,9.826590],[-5.843498,-1.973085,-1.135426,-5.799671,4.527776,6.133153,9.258672,4.309826],[5.247980,-5.993380,1.944440,-2.380390,8.036994,-4.523363,-2.755774,3.145106],[-7.724139,-8.329329,-2.923573,-8.975415,-4.660278,5.730001,-1.268676,-2.639522]],[[5.617143,7.989499,-2.838708,-8.490360,-6.582438,-5.180637,9.216917,0.155980],[1.211519,-7.482704,-4.107936,-2.780288,-6.293220,0.538957,-9.124499,5.924675],[-3.852940,-4.798488,-8.243442,-5.395229,3.541932,6.802489,-1.723667,-3.882752],[8.858256,2.324142,7.337392,-0.766816,9.011744,-0.698495,1.671604,4.475766],[-2.445141,-2.697981,8.657249,8.298466,-6.150713,2.843093,-5.373461,-5.078305],[-0.725714,2.327694,0.419861,9.815598,1.318456,-4.750201,8.545966,-2.603314],[-6.830009,8.768562,1.368891,-8.903600,1.876123,-1.845646,-7.248714,0.852541],[-2.761048,-5.299771,-8.909627,-3.141769,-8.039165,-7.485193,1.476101,7.731725],[-2.706288,2.316614,-3.108044,4.807010,6.738619,7.737884,-4.062836,-8.781756],[0.160104,6.372403,-0.660523,-2.012108,-8.309261,4.910305,4.568906,8.550191],[7.328938,-4.314146,4.340876,0.470239,1.542044,-8.545222,-3.468296,3.697206]],[[9.088901,2.446900,-2.459749,-2.534041,8.507453,-2.678153,4.733062,-9.651610],[-5.480680,-5.938029,-9.657963,-5.983257,-7.896957,8.605746,1.876917,-9.687594],[3.628251,7.924881,5.626209,6.452813,3.372937,-5.092119,0.730942,8.244555],[4.729426,2.656917,8.183703,1.365939,-8.076517,-6.052018,1.083846,2.628890],[2.650200,5.225998,-1.390098,1.309559,-8.249283,-4.472522,-4.988537,-1.485768],[5.015060,5.546186,9.880409,-5.792927,1.209777,-0.535799,-5.595020,-9.557367],[-2.509626,-8.747289,-8.675561,-5.509196,1.349742,-2.817691,-0.713037,4.622078],[4.674252,-4.606962,-0.461415,-7.520357,-4.323476,-6.194980,-7.965950,-3.668710],[-3.712218,-7.280977,-0.221425,-6.360380,8.584788,2.428970,2.084998,-1.154046],[2.412847,2.618770,7.837590,3.458787,-5.140519,-2.569431,-1.470909,9.864575],[-8.068697,0.856829,-2.078152,-3.013503,1.469237,9.865954,7.256264,1.114469]],[[7.809954,-7.935243,-4.745009,-9.010932,4.564484,-5.119266,7.683615,2.580649],[2.799325,-8.511316,-3.156246,9.017298,-5.028681,-6.862180,-2.613119,-0.036675],[-3.931609,5.948799,-8.942381,-4.500201,-7.336481,-1.946213,-5.652918,9.475745],[-8.140123,-3.607117,9.925612,-4.297676,-3.436388,2.361277,-9.933249,-6.765506],[-2.854800,-0.165164,7.110727,-4.030005,7.307370,0.454087,-8.585811,0.205587],[-7.234925,5.657673,5.256987,1.080070,-1.337137,7.932645,-1.188014,-0.672347],[3.997038,-3.401535,3.966527,-3.883750,5.142880,-7.980836,4.856423,-9.348840],[4.473246,2.351696,-3.790606,7.910364,0.741348,4.179698,-1.248318,-9.040172],[-9.868887,3.380610,8.456450,-9.041387,7.135840,7.320215,-7.562726,7.085829],[7.193122,3.352185,7.356962,5.439659,3.688958,2.687806,-2.656168,6.424184],[-2.540140,-3.665059,-5.483625,-6.675510,3.220527,-1.133039,4.503641,-7.288112]],[[-7.625145,-0.162146,-1.160918,-7.056144,6.672193,1.901958,9.349738,-0.876806],[6.858704,-0.387095,-7.754969,-2.115215,-4.189778,1.744583,-2.341453,-8.988404],[3.071421,-2.357702,-8.519370,7.641872,-9.581646,7.304676,7.624391,7.159277],[-5.239907,1.192083,-2.489809,0.278857,-5.828006,5.056981,-5.752420,-4.378470],[-1.510110,7.019583,3.459160,-1.571057,7.287955,-6.340549,-7.877139,-3.978659],[5.293412,3.045774,9.816734,-7.189339,9.090746,-1.708346,4.920161,-9.634816],[0.744135,6.269179,-2.801461,6.814616,9.054593,7.327604,5.886895,6.867385],[3.678382,9.987602,5.615685,-4.419122,7.312582,-1.557405,6.690231,-5.780330],[-8.085221,-3.900198,-1.053794,-2.794328,8.281106,7.859574,3.127461,1.642014],[1.382736,6.390304,-8.853565,1.841287,-5.311270,-7.272764,-6.409382,6.575876],[-6.755877,-2.638619,3.949897,1.349319,-2.957120,3.042632,3.248547,-9.586608]],[[9.785533,0.282072,5.205659,0.128396,-5.711914,-2.024641,5.471955,3.529459],[0.687087,-7.736658,-6.174438,0.429850,-9.045123,4.477735,4.650190,-2.558258],[1.987006,-8.016455,-3.057927,1.619761,1.433296,-7.815377,9.425531,2.422519],[0.702300,1.197866,2.135319,-9.740709,1.810789,6.461872,6.891897,-3.136125],[3.242234,5.992042,-6.575347,-8.448561,-7.711060,-5.381377,-2.689200,-4.447650],[6.076601,0.613336,-6.613146,-4.614285,0.149690,-3.354211,8.866500,-0.551022],[9.242067,7.656937,-1.232791,-9.049840,-7.677647,-5.017300,-5.808907,-9.691720],[-5.820496,-3.016406,0.225678,-8.561806,-4.317606,1.478266,9.118083,-0.279907],[1.187630,1.392235,7.699466,4.429582,-5.632242,-0.660824,-2.192210,3.617241],[-3.690021,-7.859424,-2.940298,9.061473,3.677873,4.714804,-9.737694,-9.355318],[6.587094,3.306818,1.909686,-6.230013,-7.316099,-8.035347,8.767419,0.253265]],[[4.395943,7.638003,-1.348786,-5.595462,6.351505,7.476440,7.878075,3.467591],[3.495993,8.294351,8.457420,-8.212392,-4.960441,7.315864,-2.747928,9.501658],[-9.253128,-7.292038,8.353747,-3.071239,-4.487996,-2.778172,5.416427,-4.188954],[-1.568795,8.989534,0.841556,8.850969,-7.949170,4.629143,7.197521,-2.104432],[5.895227,5.098177,9.035917,5.974845,4.177649,8.955279,1.166303,7.425084],[3.873303,-8.101984,-4.404162,-1.360901,-2.831187,-6.464185,9.685772,8.972064],[6.800685,5.830143,-0.333203,-3.194494,2.222951,1.025800,8.189770,-1.936480],[0.339958,5.356579,4.404686,9.046684,0.970853,3.124191,-0.910518,0.394129],[0.615017,0.178599,4.659514,6.668577,4.960344,5.637902,0.844169,-4.507662],[-5.651342,5.158128,1.995476,0.111175,-5.727029,1.897195,3.907624,-5.002477],[-4.242068,7.927392,2.184315,-6.386421,6.319386,6.214760,8.881709,5.330021]],[[0.897065,5.806046,3.099816,0.597953,-6.447737,1.005723,4.521242,-8.239856],[1.307404,5.385128,2.352088,0.195689,5.456232,7.728961,-0.629056,9.477929],[5.742606,8.352449,5.819620,-5.076534,5.610931,-4.316266,2.167306,-0.788120],[-4.859270,5.392751,3.266660,-2.362284,2.778162,-3.896662,-0.472322,9.254569],[-4.102187,8.252827,0.222564,7.771362,4.991394,7.568243,8.950633,2.834209],[6.934879,0.167773,1.792703,-9.469941,8.223403,9.170332,-0.673477,-5.519090],[0.125382,-9.966349,8.378057,1.057303,2.165906,-9.443050,5.169829,-5.990421],[-1.215361,4.721135,2.637380,4.198705,-8.538580,8.702009,8.254946,-6.462205],[3.308717,-7.109156,-1.420604,0.347664,-2.851839,-9.310816,5.674748,5.973063],[-7.155433,0.092110,-3.269304,2.772957,3.588255,8.385672,-1.147394,2.506914],[-2.145934,-3.710873,-0.798002,8.307086,2.134437,-5.317927,-9.493670,8.737501]]], dtype = "float32")#candidate|121|(10, 11, 8)|const|float32
uop_122 = relay.log2(const_121.astype('float32')) # shape=(10, 11, 8)
output = uop_122
output2 = uop_122
func_139 = relay.Function([], output)
mod['func_139'] = func_139
mod = relay.transform.InferType()(mod)
output = func_139()
func_140 = relay.Function([], output)
mutated_mod['func_140'] = func_140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_172 = func_139_call()
call_173 = func_139_call()
output = call_172
output2 = call_173
func_176 = relay.Function([], output)
mod['func_176'] = func_176
mod = relay.transform.InferType()(mod)
mutated_mod['func_176'] = func_176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_176_call = mutated_mod.get_global_var('func_176')
call_177 = func_176_call()
output = call_177
func_178 = relay.Function([], output)
mutated_mod['func_178'] = func_178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_190 = func_139_call()
call_191 = func_139_call()
output = relay.Tuple([call_190,])
output2 = relay.Tuple([call_191,])
func_207 = relay.Function([], output)
mod['func_207'] = func_207
mod = relay.transform.InferType()(mod)
mutated_mod['func_207'] = func_207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_207_call = mutated_mod.get_global_var('func_207')
call_208 = func_207_call()
output = call_208
func_209 = relay.Function([], output)
mutated_mod['func_209'] = func_209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_176_call = mod.get_global_var('func_176')
func_178_call = mutated_mod.get_global_var('func_178')
call_225 = func_176_call()
call_226 = func_176_call()
output = call_225
output2 = call_226
func_234 = relay.Function([], output)
mod['func_234'] = func_234
mod = relay.transform.InferType()(mod)
mutated_mod['func_234'] = func_234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_234_call = mutated_mod.get_global_var('func_234')
call_235 = func_234_call()
output = call_235
func_236 = relay.Function([], output)
mutated_mod['func_236'] = func_236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_207_call = mod.get_global_var('func_207')
func_209_call = mutated_mod.get_global_var('func_209')
call_243 = relay.TupleGetItem(func_207_call(), 0)
call_244 = relay.TupleGetItem(func_209_call(), 0)
func_207_call = mod.get_global_var('func_207')
func_209_call = mutated_mod.get_global_var('func_209')
call_299 = relay.TupleGetItem(func_207_call(), 0)
call_300 = relay.TupleGetItem(func_209_call(), 0)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_304 = func_139_call()
call_305 = func_139_call()
output = relay.Tuple([call_243,call_299,call_304,])
output2 = relay.Tuple([call_244,call_300,call_305,])
func_312 = relay.Function([], output)
mod['func_312'] = func_312
mod = relay.transform.InferType()(mod)
mutated_mod['func_312'] = func_312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_312_call = mutated_mod.get_global_var('func_312')
call_313 = func_312_call()
output = call_313
func_314 = relay.Function([], output)
mutated_mod['func_314'] = func_314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
call_380 = relay.TupleGetItem(func_312_call(), 1)
call_381 = relay.TupleGetItem(func_314_call(), 1)
output = call_380
output2 = call_381
func_389 = relay.Function([], output)
mod['func_389'] = func_389
mod = relay.transform.InferType()(mod)
mutated_mod['func_389'] = func_389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_389_call = mutated_mod.get_global_var('func_389')
call_390 = func_389_call()
output = call_390
func_391 = relay.Function([], output)
mutated_mod['func_391'] = func_391
mutated_mod = relay.transform.InferType()(mutated_mod)
var_450 = relay.var("var_450", dtype = "float64", shape = (11, 3, 14))#candidate|450|(11, 3, 14)|var|float64
uop_451 = relay.tan(var_450.astype('float64')) # shape=(11, 3, 14)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_454 = func_139_call()
call_455 = func_139_call()
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
call_466 = relay.TupleGetItem(func_312_call(), 1)
call_467 = relay.TupleGetItem(func_314_call(), 1)
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
call_468 = relay.TupleGetItem(func_312_call(), 2)
call_469 = relay.TupleGetItem(func_314_call(), 2)
func_176_call = mod.get_global_var('func_176')
func_178_call = mutated_mod.get_global_var('func_178')
call_477 = func_176_call()
call_478 = func_176_call()
output = relay.Tuple([uop_451,call_454,call_466,call_468,call_477,])
output2 = relay.Tuple([uop_451,call_455,call_467,call_469,call_478,])
func_480 = relay.Function([var_450,], output)
mod['func_480'] = func_480
mod = relay.transform.InferType()(mod)
mutated_mod['func_480'] = func_480
mutated_mod = relay.transform.InferType()(mutated_mod)
var_481 = relay.var("var_481", dtype = "float64", shape = (11, 3, 14))#candidate|481|(11, 3, 14)|var|float64
func_480_call = mutated_mod.get_global_var('func_480')
call_482 = func_480_call(var_481)
output = call_482
func_483 = relay.Function([var_481], output)
mutated_mod['func_483'] = func_483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_207_call = mod.get_global_var('func_207')
func_209_call = mutated_mod.get_global_var('func_209')
call_547 = relay.TupleGetItem(func_207_call(), 0)
call_548 = relay.TupleGetItem(func_209_call(), 0)
uop_555 = relay.tan(call_547.astype('float32')) # shape=(10, 11, 8)
uop_557 = relay.tan(call_548.astype('float32')) # shape=(10, 11, 8)
output = relay.Tuple([uop_555,])
output2 = relay.Tuple([uop_557,])
func_563 = relay.Function([], output)
mod['func_563'] = func_563
mod = relay.transform.InferType()(mod)
mutated_mod['func_563'] = func_563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_563_call = mutated_mod.get_global_var('func_563')
call_564 = func_563_call()
output = call_564
func_565 = relay.Function([], output)
mutated_mod['func_565'] = func_565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_234_call = mod.get_global_var('func_234')
func_236_call = mutated_mod.get_global_var('func_236')
call_615 = func_234_call()
call_616 = func_234_call()
func_176_call = mod.get_global_var('func_176')
func_178_call = mutated_mod.get_global_var('func_178')
call_622 = func_176_call()
call_623 = func_176_call()
var_656 = relay.var("var_656", dtype = "float32", shape = (10, 11, 8))#candidate|656|(10, 11, 8)|var|float32
bop_657 = relay.equal(call_615.astype('bool'), relay.reshape(var_656.astype('bool'), relay.shape_of(call_615))) # shape=(10, 11, 8)
bop_660 = relay.equal(call_616.astype('bool'), relay.reshape(var_656.astype('bool'), relay.shape_of(call_616))) # shape=(10, 11, 8)
output = relay.Tuple([call_622,bop_657,])
output2 = relay.Tuple([call_623,bop_660,])
func_682 = relay.Function([var_656,], output)
mod['func_682'] = func_682
mod = relay.transform.InferType()(mod)
var_683 = relay.var("var_683", dtype = "float32", shape = (10, 11, 8))#candidate|683|(10, 11, 8)|var|float32
output = func_682(var_683)
func_684 = relay.Function([var_683], output)
mutated_mod['func_684'] = func_684
mutated_mod = relay.transform.InferType()(mutated_mod)
var_700 = relay.var("var_700", dtype = "float32", shape = (8, 8, 15))#candidate|700|(8, 8, 15)|var|float32
uop_701 = relay.sinh(var_700.astype('float32')) # shape=(8, 8, 15)
uop_705 = relay.log2(uop_701.astype('float64')) # shape=(8, 8, 15)
bop_712 = relay.greater(uop_701.astype('bool'), relay.reshape(uop_705.astype('bool'), relay.shape_of(uop_701))) # shape=(8, 8, 15)
func_480_call = mod.get_global_var('func_480')
func_483_call = mutated_mod.get_global_var('func_483')
const_719 = relay.const([-4.082051,9.417061,0.552308,-6.629193,-4.733186,-4.876567,0.473213,3.357884,9.334050,8.359252,8.682044,0.770199,-1.611141,9.976757,6.516208,-6.639711,0.514915,6.476529,9.592035,3.475193,4.573198,-4.414465,-0.156935,0.578330,5.565315,-7.600226,6.006560,8.983148,4.193387,6.674771,8.013256,-6.746449,2.866352,6.512604,-0.837393,-3.306641,-0.263332,-8.338304,7.900869,-2.404107,-5.285865,6.482701,-5.853113,0.237246,5.718508,6.534531,-5.265382,5.660050,9.048142,-1.756012,9.611431,1.807633,-3.545533,2.650919,-2.239830,-6.850580,-9.101579,-8.880263,-5.325976,-1.973643,5.723118,-0.512069,-7.236425,2.149473,-9.961401,0.463756,2.283085,0.064334,-6.074039,5.854627,-8.831029,3.938676,4.163660,8.681001,-6.986022,7.058286,8.508964,3.352853,-1.324560,-8.585968,6.365117,-4.632109,-1.478597,-2.011665,-8.136264,1.943780,7.768595,1.119104,9.249111,-8.715277,3.113915,6.198799,4.064481,-3.770248,9.362194,-9.248852,-8.852865,0.604028,-1.679101,8.377872,2.126231,8.794344,2.249669,2.953449,5.787449,-7.138083,-9.555195,-8.010942,2.607651,8.274514,4.455072,6.122171,-3.756810,-3.369588,-5.937242,-4.432304,1.581289,-5.137733,-3.817426,1.921590,1.906198,-1.584848,5.782809,0.602401,6.099510,2.476864,-1.007944,-1.448809,-2.626281,2.603836,-1.987891,-2.311922,6.797079,3.879669,8.757955,5.652319,-2.706908,-5.816544,-3.492939,-1.572358,-1.530188,-3.113832,-6.727164,3.242261,-5.114832,4.096848,-6.216710,-2.696210,-3.615241,-7.694579,-0.641610,-0.922346,2.773137,-6.425259,-7.204574,-5.287714,-1.992439,1.410822,0.957139,2.464423,2.508623,5.229705,4.524660,9.595052,5.695266,9.917328,-1.823216,-4.675576,-3.916721,8.936830,-1.311573,3.092621,4.289210,7.663452,0.351448,-8.439760,-3.967202,4.053101,0.052021,9.358495,-4.644034,-8.046575,3.863356,-9.204807,6.038783,-4.329229,8.164918,-0.729217,0.544899,-0.754248,9.804222,5.782492,-2.886779,2.797818,-2.994168,-4.543609,8.126936,4.439029,8.355007,-4.651496,9.341692,-5.976481,-0.185715,5.694882,4.360852,-4.722065,-0.350700,-3.220640,-1.559976,-9.876711,-6.226864,9.417787,3.070680,-8.842859,6.918045,0.837090,-5.801140,9.107984,2.145541,-2.154178,-1.117185,4.677146,-3.392749,3.232550,4.966492,4.981412,-1.939614,3.516105,1.757978,5.402038,-0.894960,-9.475081,-8.700609,1.296418,-2.790045,-0.135168,-5.757795,-3.609798,8.817302,-0.535592,9.895202,6.245992,-9.327302,-7.417654,-3.696875,-1.047259,-6.439985,2.302633,2.075810,-1.859562,-4.206830,-4.338686,-3.509955,-5.647650,0.941301,-1.059055,-4.444709,-4.557758,-3.240800,6.118213,-6.177221,8.651274,-5.450944,-8.757691,1.413916,6.450807,9.971198,9.849914,-7.848344,-8.056871,-3.984444,4.173469,-1.586168,8.360958,-0.660848,8.399051,2.030282,0.785397,-3.716692,3.339293,1.045055,9.813399,-3.161728,-8.442136,-0.429857,-4.748753,-7.537339,-8.772090,-9.032196,6.876316,-5.608634,9.099950,-2.461424,3.835787,-5.712374,-0.250863,4.839590,6.028994,-3.246960,5.454166,-3.705761,3.576591,5.196623,1.665475,-2.801132,-7.899995,7.390361,-5.042597,-6.549529,-0.084807,-6.535852,-8.162200,9.442790,2.652730,-3.451030,-0.500196,6.960494,3.838026,9.656500,-1.125614,3.781900,-7.308942,-8.797896,-5.716363,-3.787032,-1.093570,-6.955539,5.404489,-3.466146,8.233060,8.645813,4.694786,-5.387855,0.910509,5.636219,2.435311,-1.196500,0.069673,-8.720363,4.093058,5.667390,7.886751,2.731094,3.771109,6.147322,-6.303057,-3.141847,7.540327,-8.537941,9.406254,-2.523948,-1.545154,-3.606297,-6.332965,-1.988528,-8.493857,3.919852,9.335353,-7.373416,-7.326253,8.103736,-5.041448,-4.201934,-3.965981,-9.585739,-8.512680,-3.759137,4.351542,-6.231977,9.167523,6.000901,-7.789453,2.082842,4.296187,-6.658267,-3.842738,-5.367558,-9.097212,-6.539670,7.574854,-4.661633,-7.772911,1.950236,7.145353,7.033252,-4.105486,-7.744528,9.342329,-1.293116,5.582194,-6.583606,-2.016625,-2.136914,5.537907,-7.525253,3.221978,-6.885421,8.656600,6.303467,1.209934,-9.638071,-6.067930,0.225241,-7.246602,-6.038387,-2.373681,7.096802,-6.578098,7.681478,7.203013,-4.486022,-5.705218,-6.071588,-1.518130,3.343606,-9.924720,2.037087,-8.910165,-4.581003,-4.255342,4.421892,9.233062,-0.150003,-1.452487,7.288835,5.849708,3.966481,-4.381685,8.630056,7.523695,-7.293709,-1.013651,-0.218110,-3.818807,-4.533823,-7.477611,-2.192612,-9.561162,9.026206,-5.689988,-1.766214,-9.924905,-7.620537,9.716338,-8.868150,-9.464318,-4.214961,-4.961467,1.436534,6.859191,-1.486062,4.162237,3.483844,9.037453,8.051435,3.455080,0.087031,6.071278,-9.062009,7.093353,2.842208,-6.298595], dtype = "float64")#candidate|719|(462,)|const|float64
call_718 = relay.TupleGetItem(func_480_call(relay.reshape(const_719.astype('float64'), [11, 3, 14])), 1)
call_720 = relay.TupleGetItem(func_483_call(relay.reshape(const_719.astype('float64'), [11, 3, 14])), 1)
output = relay.Tuple([bop_712,call_718,const_719,])
output2 = relay.Tuple([bop_712,call_720,const_719,])
func_726 = relay.Function([var_700,], output)
mod['func_726'] = func_726
mod = relay.transform.InferType()(mod)
mutated_mod['func_726'] = func_726
mutated_mod = relay.transform.InferType()(mutated_mod)
var_727 = relay.var("var_727", dtype = "float32", shape = (8, 8, 15))#candidate|727|(8, 8, 15)|var|float32
func_726_call = mutated_mod.get_global_var('func_726')
call_728 = func_726_call(var_727)
output = call_728
func_729 = relay.Function([var_727], output)
mutated_mod['func_729'] = func_729
mutated_mod = relay.transform.InferType()(mutated_mod)
const_752 = relay.const([[[2,5,-4,-6,4,6],[2,-9,6,1,3,9],[-7,-10,-8,9,10,6],[4,2,1,10,-6,4],[-8,-2,-6,-9,-8,4],[-1,-7,-8,6,5,9],[-10,1,-9,5,-1,8],[-2,2,8,-5,8,10],[5,7,-8,7,-7,-1],[3,-2,5,-2,7,-6]],[[-2,3,-2,-8,-9,-8],[3,-4,-6,-7,-10,-5],[-10,-3,-3,-1,-1,4],[7,2,-9,2,8,2],[-10,-4,9,7,-6,-6],[1,-1,2,-8,9,5],[-10,8,3,-3,1,3],[-7,-9,1,10,-5,-6],[8,5,4,3,-7,4],[-5,2,4,-7,-6,-2]],[[4,-10,-6,-5,10,2],[-2,-8,10,-10,8,-2],[-7,-5,-7,-1,10,-1],[10,3,-8,6,1,-8],[5,-3,-9,-9,-4,-9],[-1,4,-6,2,-1,-7],[-7,8,6,-9,5,6],[-9,-2,9,-3,-4,6],[2,-5,10,-1,-5,-6],[-6,-10,7,4,-2,8]],[[-8,2,10,1,5,-4],[-7,3,-3,-1,-4,-9],[-10,6,9,-3,-4,10],[-4,-7,-8,3,5,9],[7,-8,-4,9,-10,-6],[-6,8,4,6,-1,-5],[4,-6,8,-1,-5,3],[6,3,-6,4,8,3],[-10,-7,4,9,2,10],[-9,4,-8,7,-8,9]],[[-1,-7,7,-8,3,-7],[7,-6,9,10,5,-6],[-10,8,-3,-1,3,1],[10,-6,-5,9,-7,3],[-8,-6,7,-9,-4,5],[7,-4,-6,10,-6,-8],[-7,3,1,-2,6,-6],[-9,-2,-4,-2,6,1],[1,-9,-8,-8,-5,1],[-6,7,-10,-7,-5,-3]],[[7,-10,-1,5,4,9],[-1,9,9,-2,-4,6],[-9,4,-3,7,-2,3],[9,5,1,3,2,-8],[3,-5,8,-2,6,4],[-3,-9,7,-8,7,-8],[-7,10,5,2,9,-7],[-9,-7,5,4,2,4],[-5,-8,4,-3,-10,-10],[-3,5,10,-1,2,-5]],[[9,6,-5,3,-1,-4],[-8,7,8,-5,2,2],[-3,-10,-9,2,6,-1],[8,-1,-4,7,-10,2],[-2,10,6,-5,-5,3],[-1,3,-5,-8,-8,-4],[-4,8,5,-3,-8,10],[-6,-4,1,-8,4,-2],[8,2,3,-10,-6,10],[-10,-10,-7,-2,-7,-6]],[[4,3,-5,-5,-8,-9],[-2,7,-9,1,1,6],[4,-3,-4,9,2,6],[-10,-2,-9,-9,-2,-10],[5,-8,5,-8,-4,9],[-1,8,2,-3,-4,-3],[6,3,-10,8,-8,-6],[2,3,-5,6,3,-9],[5,-9,9,-1,6,4],[10,-3,-8,-3,-3,6]],[[9,3,-5,8,8,-10],[-9,-1,-6,-3,7,-5],[5,5,4,-7,3,-6],[-4,-10,-4,-9,-9,8],[-7,2,-6,-9,4,-10],[-5,-3,9,-9,-6,7],[-7,-2,9,4,2,-10],[-4,1,10,8,2,-4],[-3,-4,-1,-8,7,7],[-10,2,8,10,10,1]],[[7,-7,-3,10,5,-2],[4,5,9,-9,-4,1],[-2,5,6,-4,-7,2],[4,-3,-5,-3,6,2],[1,-4,-2,-6,-10,8],[7,9,-5,-4,-2,-7],[-4,5,8,5,9,-4],[-6,5,1,10,-7,2],[9,-2,2,9,10,6],[-1,9,2,-1,4,-4]],[[9,-5,-6,-2,-2,7],[4,2,10,-1,-2,-1],[6,5,-7,-6,-5,-7],[-7,-8,-3,-5,-9,-8],[6,1,2,2,-5,-7],[-6,-3,2,-3,-6,10],[-6,-6,-1,-3,6,4],[-8,-3,5,-5,2,3],[-7,5,-7,-5,-9,7],[5,-8,6,6,-2,6]],[[8,-8,1,-6,-10,-2],[-5,2,-5,-5,-3,-1],[9,-4,6,-8,-3,-7],[-10,1,-2,-10,9,3],[3,6,5,6,3,-4],[-1,-5,1,-9,3,-4],[4,-5,6,-8,-8,-4],[2,-6,9,5,-4,-4],[-2,-9,-2,1,-5,-8],[-4,9,-3,-4,2,-7]],[[2,10,-2,-3,5,9],[-5,3,9,-10,-10,-7],[-9,-5,1,-3,-5,8],[-7,-4,-5,2,-5,9],[-8,9,5,2,-6,-6],[-2,9,1,-7,-2,-3],[-3,-6,-9,4,-1,9],[6,-1,-8,-9,-7,-8],[-10,9,5,1,-6,-8],[-10,-4,5,1,5,-6]],[[-1,3,-5,-8,-7,9],[8,4,6,9,-6,9],[8,-5,-3,8,-5,-4],[4,-7,1,-7,-5,3],[2,-9,6,-2,-7,-7],[-9,4,8,4,2,-4],[-7,-1,1,6,-5,6],[3,6,-6,-2,-10,8],[-6,9,-4,-2,4,-7],[-5,-10,8,-2,3,-10]]], dtype = "int32")#candidate|752|(14, 10, 6)|const|int32
var_753 = relay.var("var_753", dtype = "int32", shape = (14, 10, 6))#candidate|753|(14, 10, 6)|var|int32
bop_754 = relay.maximum(const_752.astype('int32'), relay.reshape(var_753.astype('int32'), relay.shape_of(const_752))) # shape=(14, 10, 6)
func_563_call = mod.get_global_var('func_563')
func_565_call = mutated_mod.get_global_var('func_565')
call_764 = relay.TupleGetItem(func_563_call(), 0)
call_765 = relay.TupleGetItem(func_565_call(), 0)
var_774 = relay.var("var_774", dtype = "float32", shape = (10, 11, 8))#candidate|774|(10, 11, 8)|var|float32
bop_775 = relay.divide(call_764.astype('float64'), relay.reshape(var_774.astype('float64'), relay.shape_of(call_764))) # shape=(10, 11, 8)
bop_778 = relay.divide(call_765.astype('float64'), relay.reshape(var_774.astype('float64'), relay.shape_of(call_765))) # shape=(10, 11, 8)
output = relay.Tuple([bop_754,bop_775,])
output2 = relay.Tuple([bop_754,bop_778,])
func_781 = relay.Function([var_753,var_774,], output)
mod['func_781'] = func_781
mod = relay.transform.InferType()(mod)
mutated_mod['func_781'] = func_781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_781_call = mutated_mod.get_global_var('func_781')
var_783 = relay.var("var_783", dtype = "int32", shape = (14, 10, 6))#candidate|783|(14, 10, 6)|var|int32
var_784 = relay.var("var_784", dtype = "float32", shape = (10, 11, 8))#candidate|784|(10, 11, 8)|var|float32
call_782 = func_781_call(var_783,var_784,)
output = call_782
func_785 = relay.Function([var_783,var_784,], output)
mutated_mod['func_785'] = func_785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_840 = func_139_call()
call_841 = func_139_call()
output = call_840
output2 = call_841
func_844 = relay.Function([], output)
mod['func_844'] = func_844
mod = relay.transform.InferType()(mod)
output = func_844()
func_845 = relay.Function([], output)
mutated_mod['func_845'] = func_845
mutated_mod = relay.transform.InferType()(mutated_mod)
var_852 = relay.var("var_852", dtype = "bool", shape = (2, 15, 14))#candidate|852|(2, 15, 14)|var|bool
const_853 = relay.const([[[False,True,True,True,False,False,False,True,True,False,True,False,True,False],[True,False,True,True,True,False,False,False,True,False,False,False,True,False],[True,False,True,False,True,False,True,True,False,True,False,True,False,True],[True,True,True,False,True,True,True,False,True,True,False,False,True,False],[False,False,True,False,True,False,False,False,False,True,False,False,True,False],[True,True,False,False,False,True,False,True,False,True,True,False,False,True],[False,False,False,True,False,True,True,True,True,True,False,True,False,False],[True,True,False,False,False,False,False,False,False,False,True,False,True,False],[False,True,False,True,True,False,False,False,True,True,True,False,False,True],[True,False,True,False,False,False,False,False,False,False,True,False,False,False],[True,True,True,True,False,True,False,False,True,False,False,False,True,True],[False,True,True,True,False,False,True,False,False,True,False,True,True,True],[True,True,False,False,False,True,False,False,False,False,False,True,True,False],[True,False,False,True,False,True,False,False,True,True,False,False,False,False],[True,True,False,False,False,False,True,False,True,True,False,True,True,True]],[[False,False,True,True,True,True,False,True,False,False,True,False,True,True],[False,True,True,True,False,True,True,False,True,False,False,False,True,False],[True,True,True,True,True,True,False,False,False,False,True,True,False,False],[True,True,True,True,False,True,False,False,False,True,False,False,False,False],[False,True,True,False,False,False,True,False,True,False,False,False,False,False],[True,True,False,False,False,False,True,True,True,True,True,True,False,False],[True,False,False,False,False,True,False,False,False,True,False,True,True,True],[True,False,True,False,True,True,False,True,True,True,False,False,False,False],[False,True,False,True,True,False,True,True,False,True,False,False,True,False],[True,False,True,True,False,False,True,True,False,False,True,True,True,True],[False,False,True,False,True,True,True,False,False,True,False,False,False,False],[False,True,False,True,False,False,False,False,False,False,False,False,False,True],[False,True,False,False,True,False,False,False,True,True,True,True,False,True],[True,True,True,True,False,True,True,False,True,True,True,False,True,True],[False,True,False,False,True,False,False,False,False,False,True,False,False,False]]], dtype = "bool")#candidate|853|(2, 15, 14)|const|bool
bop_854 = relay.logical_or(var_852.astype('bool'), relay.reshape(const_853.astype('bool'), relay.shape_of(var_852))) # shape=(2, 15, 14)
uop_859 = relay.asinh(bop_854.astype('float32')) # shape=(2, 15, 14)
func_234_call = mod.get_global_var('func_234')
func_236_call = mutated_mod.get_global_var('func_236')
call_864 = func_234_call()
call_865 = func_234_call()
func_480_call = mod.get_global_var('func_480')
func_483_call = mutated_mod.get_global_var('func_483')
var_881 = relay.var("var_881", dtype = "float64", shape = (462, 1))#candidate|881|(462, 1)|var|float64
call_880 = relay.TupleGetItem(func_480_call(relay.reshape(var_881.astype('float64'), [11, 3, 14])), 4)
call_882 = relay.TupleGetItem(func_483_call(relay.reshape(var_881.astype('float64'), [11, 3, 14])), 4)
func_563_call = mod.get_global_var('func_563')
func_565_call = mutated_mod.get_global_var('func_565')
call_883 = relay.TupleGetItem(func_563_call(), 0)
call_884 = relay.TupleGetItem(func_565_call(), 0)
uop_888 = relay.cos(uop_859.astype('float32')) # shape=(2, 15, 14)
uop_896 = relay.log2(uop_888.astype('float32')) # shape=(2, 15, 14)
bop_901 = relay.floor_mod(uop_896.astype('float64'), relay.reshape(bop_854.astype('float64'), relay.shape_of(uop_896))) # shape=(2, 15, 14)
output = relay.Tuple([call_864,call_880,var_881,call_883,bop_901,])
output2 = relay.Tuple([call_865,call_882,var_881,call_884,bop_901,])
func_904 = relay.Function([var_852,var_881,], output)
mod['func_904'] = func_904
mod = relay.transform.InferType()(mod)
mutated_mod['func_904'] = func_904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_904_call = mutated_mod.get_global_var('func_904')
var_906 = relay.var("var_906", dtype = "bool", shape = (2, 15, 14))#candidate|906|(2, 15, 14)|var|bool
var_907 = relay.var("var_907", dtype = "float64", shape = (462, 1))#candidate|907|(462, 1)|var|float64
call_905 = func_904_call(var_906,var_907,)
output = call_905
func_908 = relay.Function([var_906,var_907,], output)
mutated_mod['func_908'] = func_908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_844_call = mod.get_global_var('func_844')
func_845_call = mutated_mod.get_global_var('func_845')
call_915 = func_844_call()
call_916 = func_844_call()
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
call_921 = relay.TupleGetItem(func_312_call(), 1)
call_922 = relay.TupleGetItem(func_314_call(), 1)
output = relay.Tuple([call_915,call_921,])
output2 = relay.Tuple([call_916,call_922,])
func_928 = relay.Function([], output)
mod['func_928'] = func_928
mod = relay.transform.InferType()(mod)
mutated_mod['func_928'] = func_928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mutated_mod.get_global_var('func_928')
call_929 = func_928_call()
output = call_929
func_930 = relay.Function([], output)
mutated_mod['func_930'] = func_930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_176_call = mod.get_global_var('func_176')
func_178_call = mutated_mod.get_global_var('func_178')
call_980 = func_176_call()
call_981 = func_176_call()
var_987 = relay.var("var_987", dtype = "float32", shape = (10, 11, 8))#candidate|987|(10, 11, 8)|var|float32
bop_988 = relay.less(call_980.astype('bool'), relay.reshape(var_987.astype('bool'), relay.shape_of(call_980))) # shape=(10, 11, 8)
bop_991 = relay.less(call_981.astype('bool'), relay.reshape(var_987.astype('bool'), relay.shape_of(call_981))) # shape=(10, 11, 8)
bop_994 = relay.not_equal(var_987.astype('bool'), relay.reshape(call_980.astype('bool'), relay.shape_of(var_987))) # shape=(10, 11, 8)
bop_997 = relay.not_equal(var_987.astype('bool'), relay.reshape(call_981.astype('bool'), relay.shape_of(var_987))) # shape=(10, 11, 8)
output = relay.Tuple([bop_988,bop_994,])
output2 = relay.Tuple([bop_991,bop_997,])
func_998 = relay.Function([var_987,], output)
mod['func_998'] = func_998
mod = relay.transform.InferType()(mod)
mutated_mod['func_998'] = func_998
mutated_mod = relay.transform.InferType()(mutated_mod)
var_999 = relay.var("var_999", dtype = "float32", shape = (10, 11, 8))#candidate|999|(10, 11, 8)|var|float32
func_998_call = mutated_mod.get_global_var('func_998')
call_1000 = func_998_call(var_999)
output = call_1000
func_1001 = relay.Function([var_999], output)
mutated_mod['func_1001'] = func_1001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_1016 = relay.TupleGetItem(func_928_call(), 1)
call_1017 = relay.TupleGetItem(func_930_call(), 1)
output = call_1016
output2 = call_1017
func_1021 = relay.Function([], output)
mod['func_1021'] = func_1021
mod = relay.transform.InferType()(mod)
output = func_1021()
func_1022 = relay.Function([], output)
mutated_mod['func_1022'] = func_1022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mod.get_global_var('func_1021')
func_1022_call = mutated_mod.get_global_var('func_1022')
call_1029 = func_1021_call()
call_1030 = func_1021_call()
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
call_1059 = relay.TupleGetItem(func_312_call(), 0)
call_1060 = relay.TupleGetItem(func_314_call(), 0)
bop_1073 = relay.greater_equal(call_1029.astype('bool'), relay.reshape(call_1059.astype('bool'), relay.shape_of(call_1029))) # shape=(10, 11, 8)
bop_1076 = relay.greater_equal(call_1030.astype('bool'), relay.reshape(call_1060.astype('bool'), relay.shape_of(call_1030))) # shape=(10, 11, 8)
output = relay.Tuple([bop_1073,])
output2 = relay.Tuple([bop_1076,])
func_1084 = relay.Function([], output)
mod['func_1084'] = func_1084
mod = relay.transform.InferType()(mod)
output = func_1084()
func_1085 = relay.Function([], output)
mutated_mod['func_1085'] = func_1085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_176_call = mod.get_global_var('func_176')
func_178_call = mutated_mod.get_global_var('func_178')
call_1098 = func_176_call()
call_1099 = func_176_call()
output = relay.Tuple([call_1098,])
output2 = relay.Tuple([call_1099,])
func_1104 = relay.Function([], output)
mod['func_1104'] = func_1104
mod = relay.transform.InferType()(mod)
output = func_1104()
func_1105 = relay.Function([], output)
mutated_mod['func_1105'] = func_1105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_389_call = mod.get_global_var('func_389')
func_391_call = mutated_mod.get_global_var('func_391')
call_1116 = func_389_call()
call_1117 = func_389_call()
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_1129 = relay.TupleGetItem(func_1104_call(), 0)
call_1130 = relay.TupleGetItem(func_1105_call(), 0)
output = relay.Tuple([call_1116,call_1129,])
output2 = relay.Tuple([call_1117,call_1130,])
func_1134 = relay.Function([], output)
mod['func_1134'] = func_1134
mod = relay.transform.InferType()(mod)
mutated_mod['func_1134'] = func_1134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1134_call = mutated_mod.get_global_var('func_1134')
call_1135 = func_1134_call()
output = call_1135
func_1136 = relay.Function([], output)
mutated_mod['func_1136'] = func_1136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
call_1139 = relay.TupleGetItem(func_312_call(), 1)
call_1140 = relay.TupleGetItem(func_314_call(), 1)
output = call_1139
output2 = call_1140
func_1152 = relay.Function([], output)
mod['func_1152'] = func_1152
mod = relay.transform.InferType()(mod)
mutated_mod['func_1152'] = func_1152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1152_call = mutated_mod.get_global_var('func_1152')
call_1153 = func_1152_call()
output = call_1153
func_1154 = relay.Function([], output)
mutated_mod['func_1154'] = func_1154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_389_call = mod.get_global_var('func_389')
func_391_call = mutated_mod.get_global_var('func_391')
call_1194 = func_389_call()
call_1195 = func_389_call()
uop_1200 = relay.acos(call_1194.astype('float64')) # shape=(10, 11, 8)
uop_1202 = relay.acos(call_1195.astype('float64')) # shape=(10, 11, 8)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_1204 = relay.TupleGetItem(func_928_call(), 1)
call_1205 = relay.TupleGetItem(func_930_call(), 1)
uop_1206 = relay.log(uop_1200.astype('float64')) # shape=(10, 11, 8)
uop_1208 = relay.log(uop_1202.astype('float64')) # shape=(10, 11, 8)
output = relay.Tuple([call_1204,uop_1206,])
output2 = relay.Tuple([call_1205,uop_1208,])
func_1209 = relay.Function([], output)
mod['func_1209'] = func_1209
mod = relay.transform.InferType()(mod)
mutated_mod['func_1209'] = func_1209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1209_call = mutated_mod.get_global_var('func_1209')
call_1210 = func_1209_call()
output = call_1210
func_1211 = relay.Function([], output)
mutated_mod['func_1211'] = func_1211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1134_call = mod.get_global_var('func_1134')
func_1136_call = mutated_mod.get_global_var('func_1136')
call_1273 = relay.TupleGetItem(func_1134_call(), 1)
call_1274 = relay.TupleGetItem(func_1136_call(), 1)
output = relay.Tuple([call_1273,])
output2 = relay.Tuple([call_1274,])
func_1292 = relay.Function([], output)
mod['func_1292'] = func_1292
mod = relay.transform.InferType()(mod)
mutated_mod['func_1292'] = func_1292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1292_call = mutated_mod.get_global_var('func_1292')
call_1293 = func_1292_call()
output = call_1293
func_1294 = relay.Function([], output)
mutated_mod['func_1294'] = func_1294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mod.get_global_var('func_1021')
func_1022_call = mutated_mod.get_global_var('func_1022')
call_1354 = func_1021_call()
call_1355 = func_1021_call()
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_1371 = relay.TupleGetItem(func_1084_call(), 0)
call_1372 = relay.TupleGetItem(func_1085_call(), 0)
uop_1373 = relay.cos(call_1371.astype('float32')) # shape=(10, 11, 8)
uop_1375 = relay.cos(call_1372.astype('float32')) # shape=(10, 11, 8)
output = relay.Tuple([call_1354,uop_1373,])
output2 = relay.Tuple([call_1355,uop_1375,])
func_1382 = relay.Function([], output)
mod['func_1382'] = func_1382
mod = relay.transform.InferType()(mod)
mutated_mod['func_1382'] = func_1382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1382_call = mutated_mod.get_global_var('func_1382')
call_1383 = func_1382_call()
output = call_1383
func_1384 = relay.Function([], output)
mutated_mod['func_1384'] = func_1384
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1415 = relay.var("var_1415", dtype = "float64", shape = (13, 8, 3))#candidate|1415|(13, 8, 3)|var|float64
uop_1416 = relay.tan(var_1415.astype('float64')) # shape=(13, 8, 3)
func_904_call = mod.get_global_var('func_904')
func_908_call = mutated_mod.get_global_var('func_908')
var_1419 = relay.var("var_1419", dtype = "bool", shape = (10, 42))#candidate|1419|(10, 42)|var|bool
const_1420 = relay.const([3.944789,3.331679,-1.236796,-0.720220,5.435352,-3.146876,0.081863,0.474046,-5.783976,5.906122,-8.260327,-8.900744,7.225797,-6.337740,-2.910593,7.714944,-3.554201,0.707899,-6.091750,8.633514,3.659200,3.298981,9.270773,4.222837,9.382361,3.034490,-8.910888,-7.647128,0.696214,-4.593425,-5.192640,5.744310,2.976135,1.245245,-3.174276,0.206244,-5.096868,-4.841310,3.148866,-5.149085,-4.999361,3.085463,5.981821,0.874307,-4.067631,-4.017377,5.394212,7.463803,2.585339,-4.916458,0.250314,4.782415,1.814806,9.657455,0.101543,9.943772,7.356696,-0.700382,-6.981825,6.277817,-5.283163,5.559968,8.266827,-7.067085,7.228010,-2.894515,-4.243764,6.710627,-7.424724,-8.787302,-9.482014,7.534279,-9.041486,-5.838617,7.938984,5.942562,8.628073,-5.035996,9.092888,3.162086,9.669380,-2.421901,-9.376748,9.357054,-5.612590,-7.932108,7.450625,8.864625,-7.948107,-5.113878,5.048081,7.166557,-7.094651,-3.338436,-7.751819,2.545114,9.045480,1.953208,4.699609,-9.714805,-8.902000,-8.252833,0.337284,-1.420897,2.739719,0.103380,-4.361965,5.715114,-1.839621,5.187661,-6.747157,6.835311,-9.691105,0.313138,6.409479,7.028393,-3.686865,-0.643576,2.307574,2.247461,4.333127,-5.385369,1.592784,3.425187,5.431829,-5.468816,2.453187,1.684297,-6.319167,2.703631,1.642530,-3.718247,-5.488019,0.964392,2.393837,-9.776433,3.535639,-1.471395,-8.211421,9.042048,-9.566066,3.467561,5.836002,1.051491,7.583588,8.334540,-0.944125,6.096614,-6.655562,-7.855077,9.108098,0.794848,1.671813,-4.536644,5.124633,4.568921,2.066439,3.516617,-5.450797,2.609438,7.169795,-3.520788,-4.008870,-3.392728,-1.325627,-7.155930,1.682017,-8.480604,2.974785,-2.499646,-4.606993,9.498921,6.574154,-5.794274,7.403429,8.231259,0.128767,-5.417251,2.914756,-8.228848,-9.755027,-9.159136,-9.028581,-1.122771,9.680910,-0.098981,3.438283,7.782787,-5.349050,-0.420849,0.251428,-4.029105,9.468391,-9.804428,2.834413,-0.622125,8.041742,3.409092,5.721400,-9.844512,4.437942,0.793233,-5.706101,4.876234,-3.402413,-0.801037,1.240933,-3.622720,-6.828856,-4.405221,-1.370656,1.249903,1.417764,8.281171,-4.745843,7.028071,3.128306,-2.978376,7.733905,-5.298073,3.972937,-9.163304,-9.941514,0.095668,4.966122,-0.894536,-7.550700,-2.104278,3.929295,2.059707,7.975448,9.829200,1.084600,-5.578257,3.341469,-0.855500,7.322854,7.590803,-9.508569,-9.590893,-2.513580,2.729347,-2.511886,-7.291143,7.774964,-0.628253,-8.219088,9.387214,7.890628,2.944738,5.117131,-2.830468,-4.759116,-7.984498,-4.795986,-1.855611,0.115252,-5.928771,5.177036,1.753404,-8.505134,5.889319,7.986744,-0.770778,-8.833843,5.640541,4.331928,5.209363,-7.581806,-0.472924,-2.850230,9.885804,-3.083380,-4.609141,4.076220,4.249237,2.310819,-7.841097,5.643238,2.268840,-6.074064,8.622475,-9.052752,9.546509,-2.221612,-6.698764,7.402594,9.672394,5.797609,0.013026,3.742492,-7.890287,-6.615756,-5.023227,5.554698,4.998229,-6.015442,5.807987,4.744588,0.643688,0.917050,7.475269,-4.675761,-7.240300,-4.743764,-8.113190,-9.767296,-8.778130,4.610388,1.767156,-7.414964,8.496507,8.850252,-1.176008,3.219907,4.907661,5.122161,5.498749,1.199431,9.410955,-4.408288,3.832993,-5.314283,9.483720,-6.685542,-0.135426,3.790828,-0.697500,-6.423721,-1.103025,-3.335843,-5.945331,-1.745939,9.743905,-7.072623,5.893654,-7.617863,0.888060,-5.707090,2.545674,4.033170,7.739901,2.572190,-3.674474,-7.650778,2.901522,-2.010254,-8.288871,-8.998980,-8.631972,-1.502332,8.177822,-6.079021,2.421303,2.059123,-5.164747,-9.792896,0.008292,6.425172,-3.664854,-1.824323,-8.016227,0.039260,6.710430,0.557909,-3.790625,1.943657,-8.460843,2.756734,-1.730375,-2.236757,7.647206,3.761630,-3.225220,-7.133767,-2.888738,2.036881,2.848727,-3.798523,-7.574836,-3.363428,1.917037,-4.909639,-2.083098,-7.301112,-4.144789,3.704455,4.677796,-2.822067,5.522139,-3.545222,-4.121069,-0.539823,1.343998,-7.946174,-9.465344,-8.996164,2.665700,-0.982839,-3.014461,-3.047809,0.383150,6.213294,-7.933045,0.211948,-9.230719,-9.528472,1.539701,6.708192,6.397673,-1.794262,-4.771872,8.078079,4.228133,2.423052,-1.972934,-5.013452,6.284320,9.115572,6.545200,3.578468,-9.850864,-9.135438,9.895610,-7.049483,-1.456168,-9.899510,-4.837893,-7.743620,4.249241,7.730523,6.854439,-9.984824,2.711370,6.940544,-1.087819,9.858252,-4.178233,-5.258879,4.783546,-5.283041,6.570591,-5.433936,-4.823362,2.691411,0.298422,-9.748773,-7.451382,2.928346,-6.110830,-0.459172,-2.714972,6.861045,-1.446913,-2.881325,7.467094,9.541806,1.961113,-4.580842,-5.744628,-3.577177,-8.057123], dtype = "float64")#candidate|1420|(462,)|const|float64
call_1418 = relay.TupleGetItem(func_904_call(relay.reshape(var_1419.astype('bool'), [2, 15, 14]), relay.reshape(const_1420.astype('float64'), [462, 1]), ), 2)
call_1421 = relay.TupleGetItem(func_908_call(relay.reshape(var_1419.astype('bool'), [2, 15, 14]), relay.reshape(const_1420.astype('float64'), [462, 1]), ), 2)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_1435 = func_139_call()
call_1436 = func_139_call()
func_1292_call = mod.get_global_var('func_1292')
func_1294_call = mutated_mod.get_global_var('func_1294')
call_1445 = relay.TupleGetItem(func_1292_call(), 0)
call_1446 = relay.TupleGetItem(func_1294_call(), 0)
func_234_call = mod.get_global_var('func_234')
func_236_call = mutated_mod.get_global_var('func_236')
call_1449 = func_234_call()
call_1450 = func_234_call()
func_1134_call = mod.get_global_var('func_1134')
func_1136_call = mutated_mod.get_global_var('func_1136')
call_1452 = relay.TupleGetItem(func_1134_call(), 1)
call_1453 = relay.TupleGetItem(func_1136_call(), 1)
output = relay.Tuple([uop_1416,call_1418,var_1419,const_1420,call_1435,call_1445,call_1449,call_1452,])
output2 = relay.Tuple([uop_1416,call_1421,var_1419,const_1420,call_1436,call_1446,call_1450,call_1453,])
func_1454 = relay.Function([var_1415,var_1419,], output)
mod['func_1454'] = func_1454
mod = relay.transform.InferType()(mod)
mutated_mod['func_1454'] = func_1454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mutated_mod.get_global_var('func_1454')
var_1456 = relay.var("var_1456", dtype = "float64", shape = (13, 8, 3))#candidate|1456|(13, 8, 3)|var|float64
var_1457 = relay.var("var_1457", dtype = "bool", shape = (10, 42))#candidate|1457|(10, 42)|var|bool
call_1455 = func_1454_call(var_1456,var_1457,)
output = call_1455
func_1458 = relay.Function([var_1456,var_1457,], output)
mutated_mod['func_1458'] = func_1458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_1541 = func_139_call()
call_1542 = func_139_call()
output = call_1541
output2 = call_1542
func_1545 = relay.Function([], output)
mod['func_1545'] = func_1545
mod = relay.transform.InferType()(mod)
mutated_mod['func_1545'] = func_1545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1545_call = mutated_mod.get_global_var('func_1545')
call_1546 = func_1545_call()
output = call_1546
func_1547 = relay.Function([], output)
mutated_mod['func_1547'] = func_1547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
call_1559 = func_1152_call()
call_1560 = func_1152_call()
func_1292_call = mod.get_global_var('func_1292')
func_1294_call = mutated_mod.get_global_var('func_1294')
call_1561 = relay.TupleGetItem(func_1292_call(), 0)
call_1562 = relay.TupleGetItem(func_1294_call(), 0)
const_1564 = relay.const([[[0.646703,-6.935603,-4.642828,-9.296700,3.032320,-0.746478,6.558693,-0.023717],[-7.258866,6.881920,-6.236973,-0.871124,-7.735404,0.947713,3.406948,2.114728],[-0.769227,-2.011977,9.655715,-2.227059,4.502050,-2.411417,-8.387612,-9.243743],[9.547268,3.825646,9.674648,-1.075653,-5.636389,-7.372084,-0.631011,-4.202142],[1.342267,-9.400535,-0.474482,1.314320,1.348196,-8.770879,-2.288120,0.551623],[6.265904,2.427312,-7.408779,-4.649742,3.976441,-4.789899,-5.396975,-2.727260],[-5.350353,-7.675696,-1.370327,-4.388068,9.922884,5.071766,1.268746,5.992922],[-7.504486,-9.354736,-6.500289,3.697095,7.926647,-8.559414,0.864563,9.526915],[6.169939,-4.873727,8.437500,9.203139,9.659982,-9.482407,7.126822,0.905918],[-0.287709,1.727799,-4.409612,-5.333535,-3.323890,6.994191,2.866197,2.339802],[2.587626,-7.064374,6.484904,7.985288,6.352451,4.459416,-0.567820,-1.641621]],[[-7.606131,8.616071,-7.477407,-2.432887,-1.789563,-6.742036,-8.447587,-6.709194],[4.303303,-4.689140,8.339294,-4.610799,2.485864,9.122219,-4.865557,-8.158346],[1.521924,-3.867053,2.342272,0.475807,-4.179031,-6.790607,7.895158,-3.966837],[0.899466,4.197049,2.606691,3.353401,-8.119687,-9.697110,-1.831152,6.453901],[-0.288090,-4.160019,9.874886,-1.278290,6.641304,-7.636524,5.518776,-6.479175],[-3.079240,0.630870,5.298669,-8.169435,-7.860677,-6.909169,-2.598537,-6.268635],[2.520561,-4.854704,-9.982979,8.116208,7.405230,5.161248,-5.575531,-8.312211],[8.867745,-2.393390,-9.852431,-0.569645,3.031248,-8.677970,3.516115,8.920675],[2.025372,3.931436,-4.954567,7.112757,-7.338529,-7.941184,-2.092165,4.784186],[1.009743,-5.843730,1.224281,-7.601783,-1.031961,-8.509604,9.185266,-7.582824],[6.777573,0.097974,-6.565836,-4.923971,6.997005,-9.853542,7.574123,4.371630]],[[4.234757,-5.921610,4.842179,-3.205906,6.591123,3.152030,-0.833095,9.499924],[2.255877,9.750931,-5.668375,-3.470956,-3.197930,1.291249,7.274527,-7.044405],[0.536231,7.342608,3.599529,-4.958504,-3.911615,-1.545592,7.913014,-4.509359],[-1.732285,3.497607,5.925399,-9.441289,-7.246121,7.415780,-3.696895,-7.734838],[2.347709,-7.620814,8.978088,9.267275,-6.895125,-5.803454,-9.052145,-8.667438],[-2.217149,1.877922,-6.424264,-6.770280,2.182508,-7.881274,5.586036,5.980742],[-0.447729,-3.000208,-4.988602,4.726949,5.701413,6.077489,-3.252244,-5.747568],[8.445414,2.532813,5.571970,-5.033283,5.621762,-2.006271,8.234596,1.069317],[-4.790571,-0.875330,-1.401526,1.964279,0.246048,7.570508,1.130464,7.888630],[8.545880,-4.714721,-5.224322,6.925239,7.767749,-6.846421,-4.733222,-5.940081],[0.910285,0.598360,-8.884312,3.882989,1.724552,6.818321,-1.212553,4.814082]],[[1.759041,-1.212134,-1.772044,-6.666585,-6.718365,0.124556,-7.103437,7.312732],[-8.307295,2.827239,9.390866,-6.056024,7.464261,1.210590,-7.871705,0.263524],[-2.590693,5.478552,-9.923038,-7.150467,5.700073,0.157301,4.317050,8.012792],[7.112281,-8.015920,-0.371373,-5.795468,5.748271,1.012299,-2.347562,0.181558],[9.742307,-5.892894,-6.516786,-3.939246,-7.400326,-1.139146,-9.976127,4.385585],[-0.452926,-3.988159,-9.937730,5.692566,9.943866,-3.376507,6.008898,-7.418728],[-9.068510,-5.309728,-5.113278,-5.747536,-7.346058,-1.315048,7.968608,6.274177],[-6.180504,-3.327001,-4.090844,-8.788982,-0.013254,4.252319,-2.726164,-8.983642],[-4.777595,-3.136198,6.832654,7.146296,2.003810,-4.472544,7.606926,-2.140079],[-4.289681,9.526649,-8.643150,-4.852470,-1.415408,8.327047,4.389270,8.465678],[-4.441060,-5.142832,1.434139,-5.144073,-3.313351,9.587868,-4.810819,4.945486]],[[-2.675445,7.228896,-7.641751,5.748984,2.343076,2.770919,4.341757,5.077788],[-8.552110,0.358703,9.580950,-1.649765,1.965987,-3.015395,-0.713792,-5.841800],[-2.482295,9.550153,9.817964,4.137527,5.921268,4.691888,4.037990,2.261161],[4.468071,2.726682,-4.191108,-5.066961,5.213294,0.616763,-1.374120,-3.268776],[7.629876,9.905021,4.213663,9.651058,0.722158,7.392669,3.441870,0.096241],[5.340370,-3.683412,-0.510541,4.201384,3.241279,6.744508,-1.573863,-4.427732],[-3.081622,-0.734401,-3.824526,-7.519479,4.584399,-3.519768,-4.589363,8.868339],[8.719172,1.162690,-0.133299,6.515064,8.814839,9.786019,9.719308,8.575401],[7.564713,2.615714,-2.293732,7.017260,8.347242,-3.669203,3.106687,8.180540],[5.198239,7.115579,-4.878052,0.120013,7.165251,8.937041,-0.588537,-1.104100],[6.811232,2.184925,-0.743684,0.236000,4.645624,8.165980,3.703268,6.705219]],[[-4.666287,-6.445696,6.518611,-5.908967,-3.803172,0.422566,7.605546,-4.383192],[7.892942,-6.399415,-6.969680,2.214849,1.658091,3.805274,-3.805656,-8.029917],[2.443135,9.141727,-3.731462,3.305128,6.180667,-7.596988,8.598916,7.940434],[-0.254451,-2.859973,5.100038,-1.787280,-3.471490,2.029748,-3.389415,3.578234],[-1.004436,6.606276,2.059309,1.816199,1.777357,6.882873,-5.030715,-1.413563],[-0.721873,-1.464433,-4.583960,-1.880279,-2.148542,7.592134,7.552581,-0.550372],[5.606215,9.637578,-1.057722,-5.886658,-0.995828,-4.616463,-5.325603,4.162405],[6.048160,0.681486,2.255094,0.321756,9.716802,-5.930339,3.405004,9.868617],[-3.854268,0.576790,4.157841,0.065056,6.471691,0.419687,-4.809741,-6.191572],[-6.339041,8.030540,-3.006826,0.465652,-9.810175,-7.180085,-0.781364,-3.824164],[-0.735179,2.012881,5.771601,1.078982,0.042610,1.377095,-5.985401,6.869425]],[[6.370393,-3.374644,1.700338,3.436647,5.822230,-8.264290,8.788946,7.340916],[-1.356369,-0.088360,0.692164,8.885351,-6.733582,-0.875104,-1.754520,2.226496],[-2.490088,9.949319,2.508208,3.690394,8.648165,-6.289874,7.554883,-9.334537],[-6.222178,2.779686,6.065268,-2.438547,6.313895,-9.604521,9.835245,9.865655],[8.806842,3.057928,-7.577557,4.596166,-8.256103,-7.673738,8.137727,-7.127174],[7.787884,2.230813,-7.616220,-1.833981,-1.224917,3.422401,-9.182385,-0.363357],[-3.494744,-0.694615,-2.635495,-8.568007,1.721881,-4.496457,0.630636,8.319449],[9.759942,3.872655,-2.748340,9.525690,-9.643246,-9.571478,-0.455030,-7.534676],[1.565471,1.369150,7.996755,-6.618114,-2.099014,1.361054,8.304457,1.844165],[-7.031837,-7.517745,-6.624884,1.464594,2.632866,-4.522516,-9.121044,-9.650872],[0.656893,-9.219507,1.885356,-2.737300,8.955223,8.994336,-3.225821,0.332895]],[[-1.139774,9.145508,-2.399324,2.794265,4.670748,4.702702,0.870466,4.694967],[4.274951,7.348914,-0.442924,-7.156746,2.196740,5.257617,-0.182878,-2.761161],[-6.678488,-9.328769,1.585388,-5.024706,1.162434,-1.558641,3.542608,2.126912],[8.382072,7.571089,-7.013109,-4.161263,-9.562866,2.343242,-8.161661,0.102835],[-2.893480,1.087876,7.288578,-4.615869,1.350626,9.914069,-8.121580,7.188051],[9.103212,1.012950,8.242258,-4.928164,5.807429,-2.234754,0.457325,1.572539],[7.295125,7.421250,-2.462046,8.365730,7.778889,3.249372,-3.947949,8.182007],[2.013878,8.850588,-5.962936,-9.617405,-0.994605,-2.429689,-0.991600,4.217949],[-8.155570,9.532468,-0.799047,4.685578,7.566786,9.578259,4.197964,-6.864612],[4.632194,4.296098,5.588691,-9.088627,8.421669,4.522943,-2.506943,3.501400],[-0.135989,9.426828,-8.179797,-0.525692,6.081846,9.628773,-0.479800,-3.862523]],[[5.124750,-3.233538,7.022801,-5.105683,8.810970,1.535789,-9.587808,-7.293423],[8.093410,7.585971,-6.429057,5.805765,4.474142,2.118336,-7.059687,-1.839426],[8.848960,-5.200706,4.595045,5.850337,4.484140,-2.352720,-7.198273,-0.734608],[-5.734476,7.637062,5.290284,2.199909,3.871710,-2.291429,-6.318446,6.455483],[0.968626,-4.023695,5.013570,8.864151,-4.820257,-1.337338,8.071279,-6.697157],[0.562130,-8.379674,5.201949,5.182075,-9.662506,-5.302719,-1.583609,9.618501],[-8.014414,-3.490692,2.032923,-2.128384,3.324456,-7.803497,8.411650,3.324094],[-7.769532,2.578636,1.825905,-7.016432,-9.359672,-9.823431,9.364475,0.513218],[8.450275,9.325497,2.409177,3.195637,-8.659779,8.816473,-8.325833,-5.704461],[8.302251,-3.178045,0.091732,-7.015508,-0.455189,-4.359579,-2.798798,9.966078],[-0.416030,5.693215,-7.514087,-1.968560,-4.676791,-4.554127,-2.276695,-8.781701]],[[-5.563088,-7.209430,6.736590,3.421482,8.708194,3.653476,7.636015,-4.474105],[1.997058,-5.403257,-1.375630,8.187574,-7.028630,4.216146,-0.624031,-1.037557],[4.857626,-1.180385,-0.589549,-7.001493,-0.573529,0.720115,-2.818770,8.927466],[7.967972,0.894225,-3.545797,9.822103,-3.467453,-6.065065,-7.898667,5.203301],[2.962046,-1.428586,4.189890,-9.361104,0.564226,-6.499794,5.371638,0.526643],[1.796338,-3.316746,7.328456,-6.875939,-2.508882,1.251978,-5.564811,-9.631145],[-0.154606,8.295685,9.889499,1.825928,5.866506,-2.222634,4.093811,-2.867259],[-8.874094,4.317437,-2.243156,5.397160,-0.396150,3.207100,7.641305,-6.504682],[-3.839186,-9.400968,6.736673,-4.414947,9.762101,0.920289,3.009507,2.131487],[-2.784764,5.993929,-3.555387,-6.842260,1.843893,9.887474,0.367850,4.018133],[8.909781,-6.592969,1.845115,-8.324062,1.868857,-8.806094,2.409800,3.817544]]], dtype = "float32")#candidate|1564|(10, 11, 8)|const|float32
bop_1565 = relay.add(call_1561.astype('uint64'), relay.reshape(const_1564.astype('uint64'), relay.shape_of(call_1561))) # shape=(10, 11, 8)
bop_1568 = relay.add(call_1562.astype('uint64'), relay.reshape(const_1564.astype('uint64'), relay.shape_of(call_1562))) # shape=(10, 11, 8)
output = relay.Tuple([call_1559,bop_1565,])
output2 = relay.Tuple([call_1560,bop_1568,])
func_1572 = relay.Function([], output)
mod['func_1572'] = func_1572
mod = relay.transform.InferType()(mod)
mutated_mod['func_1572'] = func_1572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1572_call = mutated_mod.get_global_var('func_1572')
call_1573 = func_1572_call()
output = call_1573
func_1574 = relay.Function([], output)
mutated_mod['func_1574'] = func_1574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_844_call = mod.get_global_var('func_844')
func_845_call = mutated_mod.get_global_var('func_845')
call_1609 = func_844_call()
call_1610 = func_844_call()
var_1612 = relay.var("var_1612", dtype = "float32", shape = (10, 11, 8))#candidate|1612|(10, 11, 8)|var|float32
bop_1613 = relay.logical_xor(call_1609.astype('int16'), relay.reshape(var_1612.astype('int16'), relay.shape_of(call_1609))) # shape=(10, 11, 8)
bop_1616 = relay.logical_xor(call_1610.astype('int16'), relay.reshape(var_1612.astype('int16'), relay.shape_of(call_1610))) # shape=(10, 11, 8)
func_1545_call = mod.get_global_var('func_1545')
func_1547_call = mutated_mod.get_global_var('func_1547')
call_1620 = func_1545_call()
call_1621 = func_1545_call()
output = relay.Tuple([bop_1613,call_1620,])
output2 = relay.Tuple([bop_1616,call_1621,])
func_1648 = relay.Function([var_1612,], output)
mod['func_1648'] = func_1648
mod = relay.transform.InferType()(mod)
mutated_mod['func_1648'] = func_1648
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1649 = relay.var("var_1649", dtype = "float32", shape = (10, 11, 8))#candidate|1649|(10, 11, 8)|var|float32
func_1648_call = mutated_mod.get_global_var('func_1648')
call_1650 = func_1648_call(var_1649)
output = call_1650
func_1651 = relay.Function([var_1649], output)
mutated_mod['func_1651'] = func_1651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_563_call = mod.get_global_var('func_563')
func_565_call = mutated_mod.get_global_var('func_565')
call_1730 = relay.TupleGetItem(func_563_call(), 0)
call_1731 = relay.TupleGetItem(func_565_call(), 0)
output = call_1730
output2 = call_1731
func_1762 = relay.Function([], output)
mod['func_1762'] = func_1762
mod = relay.transform.InferType()(mod)
mutated_mod['func_1762'] = func_1762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1762_call = mutated_mod.get_global_var('func_1762')
call_1763 = func_1762_call()
output = call_1763
func_1764 = relay.Function([], output)
mutated_mod['func_1764'] = func_1764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_563_call = mod.get_global_var('func_563')
func_565_call = mutated_mod.get_global_var('func_565')
call_1811 = relay.TupleGetItem(func_563_call(), 0)
call_1812 = relay.TupleGetItem(func_565_call(), 0)
func_844_call = mod.get_global_var('func_844')
func_845_call = mutated_mod.get_global_var('func_845')
call_1826 = func_844_call()
call_1827 = func_844_call()
bop_1840 = relay.bitwise_or(call_1826.astype('uint64'), relay.reshape(call_1811.astype('uint64'), relay.shape_of(call_1826))) # shape=(10, 11, 8)
bop_1843 = relay.bitwise_or(call_1827.astype('uint64'), relay.reshape(call_1812.astype('uint64'), relay.shape_of(call_1827))) # shape=(10, 11, 8)
output = relay.Tuple([bop_1840,])
output2 = relay.Tuple([bop_1843,])
func_1847 = relay.Function([], output)
mod['func_1847'] = func_1847
mod = relay.transform.InferType()(mod)
mutated_mod['func_1847'] = func_1847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1847_call = mutated_mod.get_global_var('func_1847')
call_1848 = func_1847_call()
output = call_1848
func_1849 = relay.Function([], output)
mutated_mod['func_1849'] = func_1849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1572_call = mod.get_global_var('func_1572')
func_1574_call = mutated_mod.get_global_var('func_1574')
call_1852 = relay.TupleGetItem(func_1572_call(), 0)
call_1853 = relay.TupleGetItem(func_1574_call(), 0)
output = call_1852
output2 = call_1853
func_1854 = relay.Function([], output)
mod['func_1854'] = func_1854
mod = relay.transform.InferType()(mod)
mutated_mod['func_1854'] = func_1854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1854_call = mutated_mod.get_global_var('func_1854')
call_1855 = func_1854_call()
output = call_1855
func_1856 = relay.Function([], output)
mutated_mod['func_1856'] = func_1856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_563_call = mod.get_global_var('func_563')
func_565_call = mutated_mod.get_global_var('func_565')
call_1864 = relay.TupleGetItem(func_563_call(), 0)
call_1865 = relay.TupleGetItem(func_565_call(), 0)
uop_1879 = relay.sin(call_1864.astype('float64')) # shape=(10, 11, 8)
uop_1881 = relay.sin(call_1865.astype('float64')) # shape=(10, 11, 8)
func_904_call = mod.get_global_var('func_904')
func_908_call = mutated_mod.get_global_var('func_908')
var_1892 = relay.var("var_1892", dtype = "bool", shape = (420,))#candidate|1892|(420,)|var|bool
var_1893 = relay.var("var_1893", dtype = "float64", shape = (462,))#candidate|1893|(462,)|var|float64
call_1891 = relay.TupleGetItem(func_904_call(relay.reshape(var_1892.astype('bool'), [2, 15, 14]), relay.reshape(var_1893.astype('float64'), [462, 1]), ), 4)
call_1894 = relay.TupleGetItem(func_908_call(relay.reshape(var_1892.astype('bool'), [2, 15, 14]), relay.reshape(var_1893.astype('float64'), [462, 1]), ), 4)
func_844_call = mod.get_global_var('func_844')
func_845_call = mutated_mod.get_global_var('func_845')
call_1905 = func_844_call()
call_1906 = func_844_call()
output = relay.Tuple([uop_1879,call_1891,var_1892,var_1893,call_1905,])
output2 = relay.Tuple([uop_1881,call_1894,var_1892,var_1893,call_1906,])
func_1910 = relay.Function([var_1892,var_1893,], output)
mod['func_1910'] = func_1910
mod = relay.transform.InferType()(mod)
var_1911 = relay.var("var_1911", dtype = "bool", shape = (420,))#candidate|1911|(420,)|var|bool
var_1912 = relay.var("var_1912", dtype = "float64", shape = (462,))#candidate|1912|(462,)|var|float64
output = func_1910(var_1911,var_1912,)
func_1913 = relay.Function([var_1911,var_1912,], output)
mutated_mod['func_1913'] = func_1913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_234_call = mod.get_global_var('func_234')
func_236_call = mutated_mod.get_global_var('func_236')
call_1920 = func_234_call()
call_1921 = func_234_call()
func_1454_call = mod.get_global_var('func_1454')
func_1458_call = mutated_mod.get_global_var('func_1458')
const_1943 = relay.const([9.641198,5.705415,8.840186,5.339897,7.154026,-0.024580,4.742168,1.860157,2.712289,-3.992118,-0.956454,7.935732,-0.637386,-9.445978,-5.950461,-6.335133,3.817981,-7.378227,8.493729,-1.683717,-1.001670,6.123347,-3.719562,5.855792,-9.698053,-3.581982,-5.076676,3.074463,-9.244054,-4.504807,0.879052,5.599258,-0.829575,3.587574,0.667354,8.387785,-8.497877,5.457813,8.691510,-9.602577,-1.799624,4.367221,5.576038,-5.819668,-5.776239,-9.397845,9.718462,-6.739165,8.127430,-4.653626,9.984489,-1.254513,-3.688498,-3.222472,4.259630,6.998787,0.097579,-7.971894,-9.382125,0.042611,-7.409764,-3.670169,5.055195,9.512168,-1.799740,7.423797,4.793320,4.351550,0.648703,-7.285534,-1.405096,-0.807879,-6.093170,-2.013268,8.387183,1.711519,-4.669103,-0.062124,7.593876,-8.240620,4.322423,5.581605,-9.910735,-5.170499,4.501902,-7.692182,8.110976,2.322729,9.457713,-5.081723,5.229296,-8.436289,5.169974,9.928643,5.472643,-6.584034,3.120492,9.677482,-3.188960,5.405317,-5.128791,2.923624,3.370967,1.666874,5.944048,4.138337,-5.732987,-0.775237,-5.091140,-4.306447,6.519097,-1.067926,-6.857488,-9.754383,-4.810910,-3.909047,2.491115,-1.603380,9.574464,-3.664874,9.991539,8.746847,7.945699,0.238228,-9.030052,4.336586,-5.849703,-3.036559,-6.327091,4.223149,1.040859,9.240336,5.738380,4.588926,-1.847706,7.935974,8.612571,2.636180,-2.925803,8.343728,-1.726888,5.966606,-2.211959,2.436401,-8.914768,3.642557,2.394518,8.939079,-6.841231,0.947151,-7.145568,-7.004465,9.719586,-8.891446,-2.648854,-7.953106,9.306486,6.712931,-2.434390,-7.664826,3.323126,-4.659518,-2.414158,-9.049237,-7.141330,3.240760,-1.255619,-9.438223,4.166140,-3.788672,-3.957581,-4.690233,-3.775849,-0.789363,7.835119,2.310942,-5.725723,2.629163,0.074236,-2.475608,7.599118,-9.741392,3.011464,5.539318,-3.697304,1.396476,5.211701,-8.747975,1.855533,-6.630883,3.095370,-1.194967,1.326337,-9.076814,9.525164,-9.498620,4.907939,-1.280450,1.223733,1.036956,4.615405,6.138010,6.163636,-7.392496,-6.771781,6.813520,8.758203,2.100295,5.337001,9.984748,-4.534968,6.546846,9.426259,6.855777,8.855482,-3.895823,5.541352,0.508523,7.399985,7.080150,-5.216681,1.365652,-3.077200,-8.313844,-6.479770,-6.899525,8.552644,-5.964613,-3.150723,-0.204201,6.205246,-1.215747,-0.701354,2.382222,-4.514195,4.766997,8.255895,-2.525583,2.413424,4.287984,-9.848749,4.874373,9.713203,-5.523548,1.002220,2.180025,7.693015,1.792184,-4.377378,0.400356,9.229174,7.822553,1.443407,2.684491,4.070413,2.960003,-1.389399,1.404096,-6.554920,6.825049,-2.480249,-7.952171,1.331068,9.204681,-9.008893,-3.739698,9.008426,-6.601690,0.217776,-6.001335,-7.878690,-0.361051,-8.329614,-8.415881,-7.291980,-6.144947,8.449962,-7.483203,-8.959572,-0.665569,7.178174,-7.602664,-6.282736,9.030249,-8.268064,-5.586824,3.356524,-1.703108,1.050159,4.557611,-3.731387,-2.756016,-7.256753,-9.006845,6.372534,-1.040289,5.144594,7.516414,0.403624,7.335892,-7.245926,5.776515,3.763870,8.217071,-4.932861,-2.661702,-3.835875,-6.236666,9.249712,7.225333,3.605567,4.815752], dtype = "float64")#candidate|1943|(312,)|const|float64
const_1944 = relay.const([True,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True], dtype = "bool")#candidate|1944|(420,)|const|bool
call_1942 = relay.TupleGetItem(func_1454_call(relay.reshape(const_1943.astype('float64'), [13, 8, 3]), relay.reshape(const_1944.astype('bool'), [10, 42]), ), 4)
call_1945 = relay.TupleGetItem(func_1458_call(relay.reshape(const_1943.astype('float64'), [13, 8, 3]), relay.reshape(const_1944.astype('bool'), [10, 42]), ), 4)
output = relay.Tuple([call_1920,call_1942,const_1943,const_1944,])
output2 = relay.Tuple([call_1921,call_1945,const_1943,const_1944,])
func_1951 = relay.Function([], output)
mod['func_1951'] = func_1951
mod = relay.transform.InferType()(mod)
mutated_mod['func_1951'] = func_1951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1951_call = mutated_mod.get_global_var('func_1951')
call_1952 = func_1951_call()
output = call_1952
func_1953 = relay.Function([], output)
mutated_mod['func_1953'] = func_1953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1847_call = mod.get_global_var('func_1847')
func_1849_call = mutated_mod.get_global_var('func_1849')
call_1999 = relay.TupleGetItem(func_1847_call(), 0)
call_2000 = relay.TupleGetItem(func_1849_call(), 0)
output = relay.Tuple([call_1999,])
output2 = relay.Tuple([call_2000,])
func_2004 = relay.Function([], output)
mod['func_2004'] = func_2004
mod = relay.transform.InferType()(mod)
mutated_mod['func_2004'] = func_2004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2004_call = mutated_mod.get_global_var('func_2004')
call_2005 = func_2004_call()
output = call_2005
func_2006 = relay.Function([], output)
mutated_mod['func_2006'] = func_2006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_563_call = mod.get_global_var('func_563')
func_565_call = mutated_mod.get_global_var('func_565')
call_2007 = relay.TupleGetItem(func_563_call(), 0)
call_2008 = relay.TupleGetItem(func_565_call(), 0)
func_844_call = mod.get_global_var('func_844')
func_845_call = mutated_mod.get_global_var('func_845')
call_2026 = func_844_call()
call_2027 = func_844_call()
var_2035 = relay.var("var_2035", dtype = "float32", shape = (10, 11, 8))#candidate|2035|(10, 11, 8)|var|float32
bop_2036 = relay.bitwise_and(call_2026.astype('int32'), relay.reshape(var_2035.astype('int32'), relay.shape_of(call_2026))) # shape=(10, 11, 8)
bop_2039 = relay.bitwise_and(call_2027.astype('int32'), relay.reshape(var_2035.astype('int32'), relay.shape_of(call_2027))) # shape=(10, 11, 8)
uop_2043 = relay.asinh(bop_2036.astype('float32')) # shape=(10, 11, 8)
uop_2045 = relay.asinh(bop_2039.astype('float32')) # shape=(10, 11, 8)
func_1648_call = mod.get_global_var('func_1648')
func_1651_call = mutated_mod.get_global_var('func_1651')
call_2058 = relay.TupleGetItem(func_1648_call(relay.reshape(var_2035.astype('float32'), [10, 11, 8])), 1)
call_2059 = relay.TupleGetItem(func_1651_call(relay.reshape(var_2035.astype('float32'), [10, 11, 8])), 1)
func_2004_call = mod.get_global_var('func_2004')
func_2006_call = mutated_mod.get_global_var('func_2006')
call_2093 = relay.TupleGetItem(func_2004_call(), 0)
call_2094 = relay.TupleGetItem(func_2006_call(), 0)
func_1572_call = mod.get_global_var('func_1572')
func_1574_call = mutated_mod.get_global_var('func_1574')
call_2098 = relay.TupleGetItem(func_1572_call(), 0)
call_2099 = relay.TupleGetItem(func_1574_call(), 0)
output = relay.Tuple([call_2007,uop_2043,call_2058,call_2093,call_2098,])
output2 = relay.Tuple([call_2008,uop_2045,call_2059,call_2094,call_2099,])
func_2118 = relay.Function([var_2035,], output)
mod['func_2118'] = func_2118
mod = relay.transform.InferType()(mod)
mutated_mod['func_2118'] = func_2118
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2119 = relay.var("var_2119", dtype = "float32", shape = (10, 11, 8))#candidate|2119|(10, 11, 8)|var|float32
func_2118_call = mutated_mod.get_global_var('func_2118')
call_2120 = func_2118_call(var_2119)
output = call_2120
func_2121 = relay.Function([var_2119], output)
mutated_mod['func_2121'] = func_2121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
call_2150 = func_1152_call()
call_2151 = func_1152_call()
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_2176 = func_139_call()
call_2177 = func_139_call()
output = relay.Tuple([call_2150,call_2176,])
output2 = relay.Tuple([call_2151,call_2177,])
func_2179 = relay.Function([], output)
mod['func_2179'] = func_2179
mod = relay.transform.InferType()(mod)
mutated_mod['func_2179'] = func_2179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2179_call = mutated_mod.get_global_var('func_2179')
call_2180 = func_2179_call()
output = call_2180
func_2181 = relay.Function([], output)
mutated_mod['func_2181'] = func_2181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_389_call = mod.get_global_var('func_389')
func_391_call = mutated_mod.get_global_var('func_391')
call_2226 = func_389_call()
call_2227 = func_389_call()
output = relay.Tuple([call_2226,])
output2 = relay.Tuple([call_2227,])
func_2249 = relay.Function([], output)
mod['func_2249'] = func_2249
mod = relay.transform.InferType()(mod)
mutated_mod['func_2249'] = func_2249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2249_call = mutated_mod.get_global_var('func_2249')
call_2250 = func_2249_call()
output = call_2250
func_2251 = relay.Function([], output)
mutated_mod['func_2251'] = func_2251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1382_call = mod.get_global_var('func_1382')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_2252 = relay.TupleGetItem(func_1382_call(), 0)
call_2253 = relay.TupleGetItem(func_1384_call(), 0)
output = call_2252
output2 = call_2253
func_2294 = relay.Function([], output)
mod['func_2294'] = func_2294
mod = relay.transform.InferType()(mod)
output = func_2294()
func_2295 = relay.Function([], output)
mutated_mod['func_2295'] = func_2295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2296 = relay.var("var_2296", dtype = "float64", shape = (4, 15, 4))#candidate|2296|(4, 15, 4)|var|float64
uop_2297 = relay.log(var_2296.astype('float64')) # shape=(4, 15, 4)
var_2306 = relay.var("var_2306", dtype = "float64", shape = (4, 15, 4))#candidate|2306|(4, 15, 4)|var|float64
bop_2307 = relay.maximum(uop_2297.astype('uint32'), relay.reshape(var_2306.astype('uint32'), relay.shape_of(uop_2297))) # shape=(4, 15, 4)
func_1951_call = mod.get_global_var('func_1951')
func_1953_call = mutated_mod.get_global_var('func_1953')
call_2316 = relay.TupleGetItem(func_1951_call(), 0)
call_2317 = relay.TupleGetItem(func_1953_call(), 0)
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
call_2319 = relay.TupleGetItem(func_312_call(), 1)
call_2320 = relay.TupleGetItem(func_314_call(), 1)
func_1572_call = mod.get_global_var('func_1572')
func_1574_call = mutated_mod.get_global_var('func_1574')
call_2330 = relay.TupleGetItem(func_1572_call(), 0)
call_2331 = relay.TupleGetItem(func_1574_call(), 0)
func_1572_call = mod.get_global_var('func_1572')
func_1574_call = mutated_mod.get_global_var('func_1574')
call_2333 = relay.TupleGetItem(func_1572_call(), 1)
call_2334 = relay.TupleGetItem(func_1574_call(), 1)
uop_2338 = relay.erf(uop_2297.astype('float32')) # shape=(4, 15, 4)
func_234_call = mod.get_global_var('func_234')
func_236_call = mutated_mod.get_global_var('func_236')
call_2350 = func_234_call()
call_2351 = func_234_call()
output = relay.Tuple([bop_2307,call_2316,call_2319,call_2330,call_2333,uop_2338,call_2350,])
output2 = relay.Tuple([bop_2307,call_2317,call_2320,call_2331,call_2334,uop_2338,call_2351,])
func_2360 = relay.Function([var_2296,var_2306,], output)
mod['func_2360'] = func_2360
mod = relay.transform.InferType()(mod)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2360_call = mutated_mod.get_global_var('func_2360')
var_2362 = relay.var("var_2362", dtype = "float64", shape = (4, 15, 4))#candidate|2362|(4, 15, 4)|var|float64
var_2363 = relay.var("var_2363", dtype = "float64", shape = (4, 15, 4))#candidate|2363|(4, 15, 4)|var|float64
call_2361 = func_2360_call(var_2362,var_2363,)
output = call_2361
func_2364 = relay.Function([var_2362,var_2363,], output)
mutated_mod['func_2364'] = func_2364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2249_call = mod.get_global_var('func_2249')
func_2251_call = mutated_mod.get_global_var('func_2251')
call_2430 = relay.TupleGetItem(func_2249_call(), 0)
call_2431 = relay.TupleGetItem(func_2251_call(), 0)
output = call_2430
output2 = call_2431
func_2433 = relay.Function([], output)
mod['func_2433'] = func_2433
mod = relay.transform.InferType()(mod)
output = func_2433()
func_2434 = relay.Function([], output)
mutated_mod['func_2434'] = func_2434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2249_call = mod.get_global_var('func_2249')
func_2251_call = mutated_mod.get_global_var('func_2251')
call_2437 = relay.TupleGetItem(func_2249_call(), 0)
call_2438 = relay.TupleGetItem(func_2251_call(), 0)
func_1847_call = mod.get_global_var('func_1847')
func_1849_call = mutated_mod.get_global_var('func_1849')
call_2448 = relay.TupleGetItem(func_1847_call(), 0)
call_2449 = relay.TupleGetItem(func_1849_call(), 0)
func_2118_call = mod.get_global_var('func_2118')
func_2121_call = mutated_mod.get_global_var('func_2121')
call_2467 = relay.TupleGetItem(func_2118_call(relay.reshape(call_2448.astype('float32'), [10, 11, 8])), 1)
call_2468 = relay.TupleGetItem(func_2121_call(relay.reshape(call_2448.astype('float32'), [10, 11, 8])), 1)
output = relay.Tuple([call_2437,call_2448,call_2467,])
output2 = relay.Tuple([call_2438,call_2449,call_2468,])
func_2482 = relay.Function([], output)
mod['func_2482'] = func_2482
mod = relay.transform.InferType()(mod)
mutated_mod['func_2482'] = func_2482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2482_call = mutated_mod.get_global_var('func_2482')
call_2483 = func_2482_call()
output = call_2483
func_2484 = relay.Function([], output)
mutated_mod['func_2484'] = func_2484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_2507 = relay.TupleGetItem(func_1104_call(), 0)
call_2508 = relay.TupleGetItem(func_1105_call(), 0)
func_2118_call = mod.get_global_var('func_2118')
func_2121_call = mutated_mod.get_global_var('func_2121')
call_2521 = relay.TupleGetItem(func_2118_call(relay.reshape(call_2507.astype('float32'), [10, 11, 8])), 0)
call_2522 = relay.TupleGetItem(func_2121_call(relay.reshape(call_2507.astype('float32'), [10, 11, 8])), 0)
output = relay.Tuple([call_2507,call_2521,])
output2 = relay.Tuple([call_2508,call_2522,])
func_2539 = relay.Function([], output)
mod['func_2539'] = func_2539
mod = relay.transform.InferType()(mod)
output = func_2539()
func_2540 = relay.Function([], output)
mutated_mod['func_2540'] = func_2540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
call_2553 = relay.TupleGetItem(func_312_call(), 0)
call_2554 = relay.TupleGetItem(func_314_call(), 0)
func_1762_call = mod.get_global_var('func_1762')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_2555 = func_1762_call()
call_2556 = func_1762_call()
output = relay.Tuple([call_2553,call_2555,])
output2 = relay.Tuple([call_2554,call_2556,])
func_2568 = relay.Function([], output)
mod['func_2568'] = func_2568
mod = relay.transform.InferType()(mod)
mutated_mod['func_2568'] = func_2568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2568_call = mutated_mod.get_global_var('func_2568')
call_2569 = func_2568_call()
output = call_2569
func_2570 = relay.Function([], output)
mutated_mod['func_2570'] = func_2570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2571 = relay.var("var_2571", dtype = "float32", shape = (2, 4, 12))#candidate|2571|(2, 4, 12)|var|float32
uop_2572 = relay.log2(var_2571.astype('float32')) # shape=(2, 4, 12)
func_1951_call = mod.get_global_var('func_1951')
func_1953_call = mutated_mod.get_global_var('func_1953')
call_2592 = relay.TupleGetItem(func_1951_call(), 3)
call_2593 = relay.TupleGetItem(func_1953_call(), 3)
uop_2610 = relay.sqrt(var_2571.astype('float32')) # shape=(2, 4, 12)
output = relay.Tuple([uop_2572,call_2592,uop_2610,])
output2 = relay.Tuple([uop_2572,call_2593,uop_2610,])
func_2613 = relay.Function([var_2571,], output)
mod['func_2613'] = func_2613
mod = relay.transform.InferType()(mod)
var_2614 = relay.var("var_2614", dtype = "float32", shape = (2, 4, 12))#candidate|2614|(2, 4, 12)|var|float32
output = func_2613(var_2614)
func_2615 = relay.Function([var_2614], output)
mutated_mod['func_2615'] = func_2615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1847_call = mod.get_global_var('func_1847')
func_1849_call = mutated_mod.get_global_var('func_1849')
call_2620 = relay.TupleGetItem(func_1847_call(), 0)
call_2621 = relay.TupleGetItem(func_1849_call(), 0)
func_1572_call = mod.get_global_var('func_1572')
func_1574_call = mutated_mod.get_global_var('func_1574')
call_2623 = relay.TupleGetItem(func_1572_call(), 1)
call_2624 = relay.TupleGetItem(func_1574_call(), 1)
func_2179_call = mod.get_global_var('func_2179')
func_2181_call = mutated_mod.get_global_var('func_2181')
call_2630 = relay.TupleGetItem(func_2179_call(), 1)
call_2631 = relay.TupleGetItem(func_2181_call(), 1)
output = relay.Tuple([call_2620,call_2623,call_2630,])
output2 = relay.Tuple([call_2621,call_2624,call_2631,])
func_2636 = relay.Function([], output)
mod['func_2636'] = func_2636
mod = relay.transform.InferType()(mod)
mutated_mod['func_2636'] = func_2636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2636_call = mutated_mod.get_global_var('func_2636')
call_2637 = func_2636_call()
output = call_2637
func_2638 = relay.Function([], output)
mutated_mod['func_2638'] = func_2638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mod.get_global_var('func_1021')
func_1022_call = mutated_mod.get_global_var('func_1022')
call_2641 = func_1021_call()
call_2642 = func_1021_call()
uop_2646 = relay.asin(call_2641.astype('float32')) # shape=(10, 11, 8)
uop_2648 = relay.asin(call_2642.astype('float32')) # shape=(10, 11, 8)
uop_2651 = relay.atan(uop_2646.astype('float32')) # shape=(10, 11, 8)
uop_2653 = relay.atan(uop_2648.astype('float32')) # shape=(10, 11, 8)
output = uop_2651
output2 = uop_2653
func_2655 = relay.Function([], output)
mod['func_2655'] = func_2655
mod = relay.transform.InferType()(mod)
mutated_mod['func_2655'] = func_2655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2655_call = mutated_mod.get_global_var('func_2655')
call_2656 = func_2655_call()
output = call_2656
func_2657 = relay.Function([], output)
mutated_mod['func_2657'] = func_2657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2179_call = mod.get_global_var('func_2179')
func_2181_call = mutated_mod.get_global_var('func_2181')
call_2676 = relay.TupleGetItem(func_2179_call(), 1)
call_2677 = relay.TupleGetItem(func_2181_call(), 1)
output = relay.Tuple([call_2676,])
output2 = relay.Tuple([call_2677,])
func_2684 = relay.Function([], output)
mod['func_2684'] = func_2684
mod = relay.transform.InferType()(mod)
mutated_mod['func_2684'] = func_2684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2684_call = mutated_mod.get_global_var('func_2684')
call_2685 = func_2684_call()
output = call_2685
func_2686 = relay.Function([], output)
mutated_mod['func_2686'] = func_2686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_2841 = func_139_call()
call_2842 = func_139_call()
output = relay.Tuple([call_2841,])
output2 = relay.Tuple([call_2842,])
func_2854 = relay.Function([], output)
mod['func_2854'] = func_2854
mod = relay.transform.InferType()(mod)
mutated_mod['func_2854'] = func_2854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2854_call = mutated_mod.get_global_var('func_2854')
call_2855 = func_2854_call()
output = call_2855
func_2856 = relay.Function([], output)
mutated_mod['func_2856'] = func_2856
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2892 = relay.const([[[5.594260,9.450460,-0.500686,2.549099,-8.966116,3.700072,-4.980945,-1.932414,-2.315645,6.145528,6.705404,-8.122538],[-9.650844,-8.935709,-2.276970,5.583380,-8.443896,0.457965,7.429240,7.131364,-3.534234,-6.403892,5.668209,-0.996185],[1.810134,0.666832,-8.616397,-1.826436,6.688757,5.899438,8.170120,-7.767314,-2.137955,-8.328083,-9.771299,9.331031],[-2.604430,8.751558,3.276363,9.606426,-2.765958,0.063438,0.072233,1.187454,6.962970,-4.627256,-2.431925,-5.083982],[5.752201,-4.477755,-0.693914,-9.557705,3.435188,5.112909,3.735463,-1.280478,6.514848,-2.211149,9.070613,-2.117821],[5.172862,7.113469,5.453257,-8.033910,-0.508354,-5.848244,-5.879154,-1.784562,-6.875943,-8.901978,-9.196973,9.079800],[3.490362,-5.305091,-9.609511,8.114213,-4.761545,0.434914,-1.087855,-3.317023,-9.086850,-2.991481,9.109266,-0.040774],[-1.141086,5.231558,9.534173,-3.144927,0.917444,-0.115574,7.995020,4.956023,-9.159322,6.543093,-9.418378,-3.684301],[-8.048603,6.673222,1.894424,-6.260031,9.378667,-8.215038,-9.343474,8.221658,-0.283440,7.341858,9.798456,4.001690]],[[5.134520,-6.944153,-1.290672,-6.971386,5.432292,-5.577570,-5.903205,-2.198155,-6.579416,-9.024234,-0.434467,-1.351754],[0.268963,-3.106493,-2.826213,4.553560,7.843759,3.646753,-7.045967,-6.221498,-8.315085,-2.277309,8.338393,-5.600892],[4.697261,1.177815,-0.960178,-9.614575,0.422814,-2.015949,-0.581136,-2.367673,1.039653,2.953097,2.061746,-2.857422],[-5.700361,-1.344734,1.915814,-1.436420,-0.497775,-0.901997,3.335176,-5.977465,-4.526034,4.025023,-8.998214,-6.273213],[5.504339,7.668572,4.280626,-8.626505,-2.907971,-6.890108,3.477242,5.814008,-1.413787,-4.887758,-2.608330,-6.514418],[3.221468,-8.995566,2.399845,-0.092016,-6.841623,-4.228328,0.324870,-2.772476,6.693092,0.254666,1.248249,-3.280809],[5.467512,9.804740,-0.357832,-7.780304,9.029658,2.293180,2.673256,-6.354799,-4.361744,0.055313,4.760657,0.377009],[-0.493218,-2.357547,5.318375,5.530373,5.316391,3.136552,0.701665,-5.496544,-1.362340,8.733743,1.081393,2.106496],[-3.235648,0.201181,-2.343074,6.157728,9.694595,-2.206048,-2.285344,5.930332,4.475918,6.200685,-6.939712,4.344111]],[[-0.328390,-4.551718,-7.787526,3.108460,2.567371,5.861543,4.657653,-7.752618,-9.073780,-5.106879,8.523562,-8.031996],[-1.768957,4.797077,1.256901,2.730024,8.647736,5.097267,8.536634,7.277287,9.159763,5.290874,3.875055,-1.049688],[-5.695142,-7.990387,-6.119687,-8.606480,9.239544,-9.166300,2.085619,-8.641898,7.117525,-5.955043,-6.484214,2.909383],[-4.924662,-3.387132,2.234380,8.427590,0.264098,0.738111,6.042375,-5.001459,8.833642,2.252869,-6.345198,0.778924],[-6.118440,7.359005,5.804045,-3.068375,0.679861,8.729209,6.490735,-9.706853,1.491831,9.734523,-4.967545,6.802743],[-4.422176,-5.282866,-7.472811,-3.674341,2.825310,5.940019,0.180702,1.039645,-2.877876,4.181938,1.868129,8.872513],[0.141972,7.278032,-2.056617,1.816383,-2.424600,-1.943781,9.722572,4.909385,-4.044143,-8.035062,-1.736237,-3.770164],[-3.398875,5.387398,5.007367,-9.736611,8.312940,-3.363696,-2.711668,-4.659945,7.818699,7.527299,9.084071,-9.515425],[4.186717,9.676294,-2.559693,1.653523,0.879873,-7.020386,8.903348,0.118966,7.090864,-2.809011,3.431590,-9.440564]],[[9.677583,-5.099824,-9.115385,-7.066863,7.092125,6.535195,5.831615,-1.923840,2.837783,-0.530486,-3.777575,3.167413],[5.190103,5.041912,-0.849058,-2.578484,-7.103756,4.598902,6.477843,-6.884057,7.929559,-4.737425,-1.955995,-8.344185],[1.413204,-6.685153,-7.752413,7.212781,-5.555449,8.218053,-4.168005,-6.735004,-1.267386,1.653014,-1.268882,-8.780599],[-6.627673,-1.237891,3.134905,-2.666163,8.137367,-5.979431,1.839187,-5.254994,1.998089,-9.476922,2.834273,-3.483119],[-0.101306,1.691646,9.034702,2.300931,-3.654366,9.819153,-9.130415,-3.687177,-9.903385,2.371793,7.090565,6.397371],[8.964192,-8.481601,2.954668,-3.516382,2.983065,-5.139291,5.980284,-4.872829,9.490379,-9.907307,5.455453,-7.415113],[1.109675,1.479552,8.241476,7.685290,2.355398,3.815043,-5.406512,-0.477609,1.514518,3.896040,-8.014852,-8.123838],[1.528776,1.807014,0.542280,-1.374146,-2.516773,0.805439,6.635412,-6.880559,5.353571,7.873792,-9.695692,6.031182],[-3.716982,-6.148769,-1.543710,-8.925918,0.968701,-4.796989,1.878278,-8.962325,8.753147,2.805694,-3.351107,9.604294]],[[0.116915,-6.641698,-2.947614,9.968236,-6.994028,-3.339546,-1.784342,-8.316563,-6.315468,8.943109,4.312120,0.734578],[2.990804,5.574622,3.339117,4.384260,6.709685,-6.398431,7.843383,-7.773799,8.166916,-4.994431,-8.727152,-4.478289],[-6.830105,-2.133624,0.309040,-6.807411,4.528490,-6.134080,-2.468888,1.621243,1.319699,7.237436,-1.405348,-4.904221],[-9.916793,2.289891,9.317246,-6.262177,6.148756,-9.684344,-8.292122,-2.863895,-4.884112,-9.636284,-1.867628,1.119279],[2.476131,1.157373,-9.635519,-9.986557,-5.626640,8.047235,0.128458,4.057101,3.316955,9.349714,-7.810799,7.122387],[-1.712933,9.390992,7.461890,3.407399,-6.568584,-3.091048,-8.456002,3.081101,4.872378,9.763014,-7.946521,6.802638],[-4.450147,-6.255007,-5.017271,5.746387,6.608759,-5.503681,2.601904,-6.796269,-7.163331,8.984140,0.021672,4.863696],[5.971230,0.209456,-1.926574,4.099206,6.930169,4.832642,8.900597,-1.452240,-8.440393,-6.489056,-9.037759,1.197032],[2.438790,-1.892678,4.630454,0.980959,-9.081429,5.315765,-1.460298,9.164470,-5.740443,7.926666,2.031401,-9.497618]],[[-9.232538,-9.757731,2.489210,9.096594,-4.461872,1.115062,-9.344668,-2.409876,9.353261,1.942474,8.768358,9.921280],[9.330066,6.421009,9.942298,-9.466227,-4.450561,-4.071548,-0.176538,0.982158,1.002821,4.178378,5.792647,-9.299297],[9.223654,-9.956928,-5.080681,-2.918547,4.743387,3.423845,1.175453,-2.346059,-5.496014,-3.175807,0.038673,5.859354],[-7.986704,-5.572760,-7.425975,4.848932,-3.182909,-2.684324,5.102396,-9.033510,1.605275,1.057309,-2.369992,-7.106119],[0.490993,6.664679,-6.728291,1.381374,1.991240,1.030871,1.012637,5.231730,-8.283415,-1.258121,-7.922028,-8.930367],[-4.503954,5.333651,-1.861324,9.148207,-4.201332,-1.784077,1.615120,3.519175,0.923382,2.973152,9.222341,-3.983671],[-9.346895,-5.566620,3.022446,-4.778599,-6.264250,-3.956062,-2.243134,-8.193592,5.780092,7.924209,1.804148,8.897154],[9.042161,1.427143,-1.839804,7.593855,-6.724019,8.586791,-7.443042,-7.253603,0.191923,6.044940,-5.060010,-0.677754],[-7.665017,9.644256,2.974582,-1.148599,4.504653,7.031233,1.354100,-0.494586,-8.932456,-7.266627,-4.796468,-7.296579]],[[6.437699,3.961476,0.836023,6.604655,6.966818,9.683832,-8.165813,-4.540578,7.287066,2.217400,-3.207241,6.175953],[4.681738,2.369918,-6.549690,-7.854978,-5.501514,0.540220,0.676625,4.396544,2.373260,2.922212,6.711173,6.654836],[-9.029655,0.133088,4.290192,0.428493,-1.837385,-3.453266,-6.503222,3.133106,-9.256271,6.828858,1.430520,-3.467046],[8.824937,-3.100376,7.826262,-9.657941,-2.908384,-2.676534,-6.499999,5.947253,3.287027,8.991747,-4.839520,-7.777946],[2.007995,-3.569994,-0.906879,-4.278877,6.559896,-4.091927,-9.670204,-5.264602,3.151560,-5.827450,-8.300751,-3.148195],[6.605303,-8.740171,-5.691645,-6.910689,-1.304759,7.773242,-7.800889,-9.575235,-6.605739,-0.752298,9.792960,-7.518700],[-7.476212,-2.990473,-0.445004,-9.400010,-0.353562,7.322885,2.285237,3.034920,-4.635202,-5.747092,-8.032171,-3.744760],[-6.359785,7.822424,4.460277,-6.365750,1.088583,7.577786,8.278032,8.020776,-1.403485,8.118266,4.054856,5.576265],[0.112759,-9.401249,-1.753705,-0.280596,5.466922,7.637828,1.696781,-4.882395,-7.485953,-3.028791,6.858489,-0.954018]],[[-4.863358,8.519857,-8.252969,-5.805274,2.799415,0.391360,7.886631,-2.098177,1.620612,-2.609409,1.230478,4.001486],[-5.358599,5.335628,-5.410565,6.300588,8.715060,-4.867116,2.950067,8.115999,8.277398,-5.627677,2.292076,7.825260],[-4.917010,9.086134,7.899056,-1.426394,8.301917,6.079430,0.008454,-3.063125,-7.599703,-3.549266,8.874977,-9.721608],[-9.731040,-4.008155,0.825707,-1.895668,6.310018,3.570630,8.557221,-2.157023,0.275516,-8.113209,-2.205418,-4.692908],[1.334902,-1.830181,-8.988550,4.807312,6.524255,-3.813718,5.222882,1.474219,7.462400,0.586113,-2.475715,9.821025],[-8.524532,-3.697940,-0.815416,9.985791,2.486400,2.293308,-8.095371,-2.372551,-7.272094,-5.508983,0.804360,-2.467906],[-7.598439,9.921121,9.182127,-0.089229,-3.950007,-0.540825,5.201673,-7.241802,9.034004,3.187443,-2.766222,8.584924],[-9.732558,5.689383,1.000197,-6.142712,7.319079,-1.568879,-1.370096,-2.575867,0.662438,-4.109006,-1.884353,5.463600],[-0.455578,1.397033,-8.080739,0.002353,-5.161116,1.666716,-9.093632,8.726524,4.686910,-6.954364,5.576923,9.688164]],[[4.080585,1.089173,-2.932661,2.254979,6.512707,-7.590215,8.587515,2.451321,-9.086130,-8.871602,-8.808531,-1.927181],[2.798845,-8.892489,-6.918652,-6.977917,4.365905,1.288206,-0.683263,-6.347712,-7.980277,-1.996793,-1.416265,7.189559],[-7.766056,4.653127,-0.851173,-5.658961,-4.066999,-5.038857,-1.721826,-8.486002,-9.613904,-3.265282,-0.339982,6.765098],[7.617049,-2.602701,5.293758,-2.416711,4.970427,-8.561688,3.639179,-5.622252,8.476803,-1.165797,2.555796,9.274127],[3.746221,-2.301074,-6.071544,-2.485735,5.559025,7.467592,-8.565670,-1.342531,8.223067,5.236100,-6.459148,-5.003757],[-0.124290,9.710068,1.333405,-3.272122,-4.594078,-7.542990,-5.952815,-7.598336,-5.775314,-8.530583,2.935697,-8.125383],[5.743398,-0.673097,6.055460,-7.020608,4.141162,3.874509,-3.155840,5.893688,7.433186,-3.805272,-5.833125,0.894246],[-8.631258,-9.364937,7.020530,6.928588,-1.551859,-4.465383,-9.830725,-5.220037,-1.497340,6.528743,6.139990,-0.793187],[-4.643258,-7.939529,3.185646,1.352833,6.543331,-2.156135,4.289599,6.372811,3.425452,9.887049,-5.397978,1.280997]],[[-5.618981,-6.865941,-0.075705,-9.292288,8.634375,1.729664,-7.855861,-4.852323,-5.675766,-3.263447,-7.347663,-3.585158],[1.533419,-0.298712,0.104944,0.464161,-1.724679,6.456959,-4.660477,7.321976,-3.199432,-7.012246,-0.450972,-9.104002],[4.962989,-9.943309,-2.547881,7.064836,-7.426222,-0.436989,-5.166329,6.289568,1.397310,1.731473,-6.987994,0.071022],[4.386895,-4.680968,-4.196667,3.347464,1.569323,-3.542074,-0.946238,-9.581023,3.910419,-2.548759,-6.516174,-3.170307],[-1.741092,8.016696,-0.615141,5.953477,-9.897088,8.102645,-5.347144,2.193109,-0.554937,9.876930,3.505148,-2.354631],[-2.298297,-7.119246,-1.322108,-6.507069,-5.602910,-9.431990,-3.985521,7.813546,8.081854,-2.486345,0.202957,4.938276],[0.446648,-7.527723,-5.464695,6.659623,3.101291,2.246599,-7.266592,-7.277143,0.789280,6.117758,-1.537048,8.186798],[-6.802228,6.292882,5.215485,6.517402,8.015520,1.085915,-3.172348,3.256094,8.942478,-4.157691,-6.584381,-5.100191],[3.273285,-9.565515,-7.611985,7.239356,5.285505,-8.728962,9.829704,6.048021,9.435817,3.253819,8.933386,3.078612]],[[7.498576,-2.692926,-9.243047,-5.508940,-4.277102,1.665776,-0.160991,3.150954,2.422908,-8.318626,-7.975329,-7.889059],[-0.509193,6.948370,-6.865317,-6.789138,-5.947854,9.934005,-3.551752,-8.274723,-5.903454,2.057450,-2.883208,-4.865113],[7.762191,9.878683,-1.088167,0.384602,5.858051,-2.896182,-3.665946,0.052639,0.138363,6.171911,-0.443178,6.006220],[-1.198540,7.988183,3.688500,-9.399539,-4.111703,-6.294375,5.487823,-1.743176,0.728088,-3.011746,8.969175,-6.422544],[1.166216,-3.215072,-7.369952,-7.562412,9.360719,2.355886,-4.314993,1.076683,4.784405,4.021294,5.607461,6.728891],[8.604248,-0.081997,-1.958325,2.954167,6.543465,4.830262,5.164220,-7.006830,-8.241395,-5.988125,8.845082,0.085571],[4.345975,-7.092914,-6.118843,4.446518,8.319776,8.748224,1.724803,3.275482,-5.778291,-5.000796,3.121229,-5.055777],[-6.998331,-1.672759,-8.471376,2.401354,-3.495017,5.180705,2.850760,-7.500152,-7.503486,-4.624404,2.064290,-5.359561],[3.694498,1.651083,2.780318,-9.228330,-7.363399,-3.478284,-9.405533,3.863677,1.586234,-3.043130,0.917520,9.336533]],[[-8.711518,2.697712,-3.127282,0.109940,-7.215404,-9.002879,6.657463,-4.597260,5.290221,-4.380276,-1.809094,-5.696972],[-4.823284,-0.747252,-3.642838,-3.475145,-0.495500,-1.993135,0.197773,-3.127807,-3.728285,-6.981233,2.839601,-1.290175],[1.725728,-5.004370,-8.646985,8.605098,9.532804,-6.316049,8.639471,-3.590721,8.115327,-9.823296,0.721084,-9.893153],[0.157731,3.923545,8.581948,0.786764,-3.968801,-9.357314,8.394470,-7.252235,-3.700574,-8.507560,7.042115,9.221967],[5.260941,4.331087,-7.656798,-1.374541,-8.744317,-2.515847,3.681012,-3.255167,6.155773,-6.842471,-8.056751,-9.273134],[-8.931524,6.880794,0.138468,-1.238159,-9.054426,5.364537,0.974000,0.564056,2.980532,-4.982362,9.160599,7.685489],[1.653613,1.843223,-9.434537,-8.277430,-5.212239,-0.310928,-5.200742,-2.000952,-0.769534,3.315251,-0.828597,-2.615756],[-3.779297,-0.621604,3.380229,0.241471,-8.986080,5.260698,-1.595520,5.714606,0.028718,-2.850531,-8.137938,-5.008535],[3.273820,-5.134925,-1.204962,9.157904,7.388361,6.839287,7.144040,-8.065175,5.403812,-2.568328,8.961303,4.399526]],[[3.568277,2.285967,-9.641009,0.150307,6.446119,4.771122,-5.414786,2.527355,8.384298,-1.803372,1.462566,-3.453948],[-3.451256,-4.801884,-4.336380,-4.089422,8.772093,7.267508,-0.555129,6.177773,-8.205823,4.958709,-5.481069,9.114723],[6.650870,-6.804350,-2.884665,-8.267102,-4.907105,-7.372573,-3.980755,-3.708421,-7.496492,0.921048,-2.504281,0.347926],[-2.249779,9.240646,3.870118,-7.511370,7.977322,0.815470,3.326272,-9.957751,-3.636324,-6.854539,-8.942627,-4.901373],[-6.305134,4.642785,5.601221,9.475810,0.458324,-1.201336,7.798550,-1.857358,5.396184,-8.125959,3.695289,-0.299071],[-5.466769,-1.164574,-4.333499,7.110069,-4.533642,9.613081,8.575372,0.858989,-1.676001,6.551241,-3.992477,-1.463797],[1.567368,-5.650344,0.116170,-0.229480,5.176581,-6.539080,-3.049540,-2.009110,-1.794321,-2.105194,0.736508,2.954243],[1.740390,5.795188,-7.195092,2.590634,9.033600,-2.142403,9.804075,-2.651631,1.777143,-1.160129,-3.239849,-5.821080],[-8.660880,7.283220,0.047686,4.874599,3.735014,-7.040868,-1.743087,-4.567177,-1.600727,8.325324,8.017683,-9.079429]],[[-2.848510,-7.176265,-9.030330,-4.874162,2.619704,-4.429148,-3.763492,8.535023,-3.490704,8.784067,-4.040069,-9.202766],[-5.357361,-5.057636,9.964260,-3.272873,0.938230,7.417015,4.117609,-3.571105,5.692354,2.862404,0.812716,6.786528],[5.801719,-3.073189,-4.664682,-9.396629,-9.679735,0.761520,8.531707,-7.719848,-7.447236,-6.953204,6.215782,3.275516],[4.698261,-3.564023,0.272997,4.458908,-6.745414,-8.213596,-5.432541,9.733908,5.084030,4.590497,-7.749018,1.208170],[8.693441,-2.944271,1.980921,5.024240,6.578191,7.506265,4.666348,5.076763,-8.584617,1.143794,-9.824452,-8.087552],[3.859103,-7.736801,7.771737,-8.433352,-8.727182,8.876084,-3.572193,-3.244810,-7.322090,5.369477,-5.083208,0.688754],[-7.522959,-4.613053,1.522687,4.406735,-0.362632,-4.216755,7.703937,-9.394965,7.047209,8.901966,-4.685226,2.923254],[4.414272,-1.965193,8.472886,0.230790,-9.696333,-1.120606,-2.740499,-8.665535,-7.617595,-2.291910,-9.122391,5.835110],[-3.926870,6.893286,-3.024717,3.807460,4.353835,-7.567554,9.186894,6.568094,6.982527,8.746647,2.533859,-3.150266]]], dtype = "float64")#candidate|2892|(14, 9, 12)|const|float64
uop_2893 = relay.log(const_2892.astype('float64')) # shape=(14, 9, 12)
func_1648_call = mod.get_global_var('func_1648')
func_1651_call = mutated_mod.get_global_var('func_1651')
var_2900 = relay.var("var_2900", dtype = "float32", shape = (880,))#candidate|2900|(880,)|var|float32
call_2899 = relay.TupleGetItem(func_1648_call(relay.reshape(var_2900.astype('float32'), [10, 11, 8])), 0)
call_2901 = relay.TupleGetItem(func_1651_call(relay.reshape(var_2900.astype('float32'), [10, 11, 8])), 0)
func_2684_call = mod.get_global_var('func_2684')
func_2686_call = mutated_mod.get_global_var('func_2686')
call_2903 = relay.TupleGetItem(func_2684_call(), 0)
call_2904 = relay.TupleGetItem(func_2686_call(), 0)
output = relay.Tuple([uop_2893,call_2899,var_2900,call_2903,])
output2 = relay.Tuple([uop_2893,call_2901,var_2900,call_2904,])
func_2913 = relay.Function([var_2900,], output)
mod['func_2913'] = func_2913
mod = relay.transform.InferType()(mod)
mutated_mod['func_2913'] = func_2913
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2914 = relay.var("var_2914", dtype = "float32", shape = (880,))#candidate|2914|(880,)|var|float32
func_2913_call = mutated_mod.get_global_var('func_2913')
call_2915 = func_2913_call(var_2914)
output = call_2915
func_2916 = relay.Function([var_2914], output)
mutated_mod['func_2916'] = func_2916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_563_call = mod.get_global_var('func_563')
func_565_call = mutated_mod.get_global_var('func_565')
call_2935 = relay.TupleGetItem(func_563_call(), 0)
call_2936 = relay.TupleGetItem(func_565_call(), 0)
func_2568_call = mod.get_global_var('func_2568')
func_2570_call = mutated_mod.get_global_var('func_2570')
call_2937 = relay.TupleGetItem(func_2568_call(), 1)
call_2938 = relay.TupleGetItem(func_2570_call(), 1)
output = relay.Tuple([call_2935,call_2937,])
output2 = relay.Tuple([call_2936,call_2938,])
func_2945 = relay.Function([], output)
mod['func_2945'] = func_2945
mod = relay.transform.InferType()(mod)
mutated_mod['func_2945'] = func_2945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2945_call = mutated_mod.get_global_var('func_2945')
call_2946 = func_2945_call()
output = call_2946
func_2947 = relay.Function([], output)
mutated_mod['func_2947'] = func_2947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1847_call = mod.get_global_var('func_1847')
func_1849_call = mutated_mod.get_global_var('func_1849')
call_2965 = relay.TupleGetItem(func_1847_call(), 0)
call_2966 = relay.TupleGetItem(func_1849_call(), 0)
var_2977 = relay.var("var_2977", dtype = "uint64", shape = (10, 11, 8))#candidate|2977|(10, 11, 8)|var|uint64
bop_2978 = relay.greater(call_2965.astype('bool'), relay.reshape(var_2977.astype('bool'), relay.shape_of(call_2965))) # shape=(10, 11, 8)
bop_2981 = relay.greater(call_2966.astype('bool'), relay.reshape(var_2977.astype('bool'), relay.shape_of(call_2966))) # shape=(10, 11, 8)
output = bop_2978
output2 = bop_2981
func_3002 = relay.Function([var_2977,], output)
mod['func_3002'] = func_3002
mod = relay.transform.InferType()(mod)
var_3003 = relay.var("var_3003", dtype = "uint64", shape = (10, 11, 8))#candidate|3003|(10, 11, 8)|var|uint64
output = func_3002(var_3003)
func_3004 = relay.Function([var_3003], output)
mutated_mod['func_3004'] = func_3004
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3036 = relay.var("var_3036", dtype = "int16", shape = (10, 1, 12))#candidate|3036|(10, 1, 12)|var|int16
var_3037 = relay.var("var_3037", dtype = "int16", shape = (10, 4, 12))#candidate|3037|(10, 4, 12)|var|int16
bop_3038 = relay.minimum(var_3036.astype('int16'), var_3037.astype('int16')) # shape=(10, 4, 12)
func_1572_call = mod.get_global_var('func_1572')
func_1574_call = mutated_mod.get_global_var('func_1574')
call_3042 = relay.TupleGetItem(func_1572_call(), 0)
call_3043 = relay.TupleGetItem(func_1574_call(), 0)
func_2945_call = mod.get_global_var('func_2945')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_3048 = relay.TupleGetItem(func_2945_call(), 1)
call_3049 = relay.TupleGetItem(func_2947_call(), 1)
uop_3056 = relay.asin(var_3037.astype('float32')) # shape=(10, 4, 12)
output = relay.Tuple([bop_3038,call_3042,call_3048,uop_3056,])
output2 = relay.Tuple([bop_3038,call_3043,call_3049,uop_3056,])
func_3058 = relay.Function([var_3036,var_3037,], output)
mod['func_3058'] = func_3058
mod = relay.transform.InferType()(mod)
mutated_mod['func_3058'] = func_3058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3058_call = mutated_mod.get_global_var('func_3058')
var_3060 = relay.var("var_3060", dtype = "int16", shape = (10, 1, 12))#candidate|3060|(10, 1, 12)|var|int16
var_3061 = relay.var("var_3061", dtype = "int16", shape = (10, 4, 12))#candidate|3061|(10, 4, 12)|var|int16
call_3059 = func_3058_call(var_3060,var_3061,)
output = call_3059
func_3062 = relay.Function([var_3060,var_3061,], output)
mutated_mod['func_3062'] = func_3062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1854_call = mod.get_global_var('func_1854')
func_1856_call = mutated_mod.get_global_var('func_1856')
call_3064 = func_1854_call()
call_3065 = func_1854_call()
func_998_call = mod.get_global_var('func_998')
func_1001_call = mutated_mod.get_global_var('func_1001')
call_3068 = relay.TupleGetItem(func_998_call(relay.reshape(call_3064.astype('float32'), [10, 11, 8])), 1)
call_3069 = relay.TupleGetItem(func_1001_call(relay.reshape(call_3064.astype('float32'), [10, 11, 8])), 1)
output = relay.Tuple([call_3064,call_3068,])
output2 = relay.Tuple([call_3065,call_3069,])
func_3085 = relay.Function([], output)
mod['func_3085'] = func_3085
mod = relay.transform.InferType()(mod)
output = func_3085()
func_3086 = relay.Function([], output)
mutated_mod['func_3086'] = func_3086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_563_call = mod.get_global_var('func_563')
func_565_call = mutated_mod.get_global_var('func_565')
call_3087 = relay.TupleGetItem(func_563_call(), 0)
call_3088 = relay.TupleGetItem(func_565_call(), 0)
output = call_3087
output2 = call_3088
func_3091 = relay.Function([], output)
mod['func_3091'] = func_3091
mod = relay.transform.InferType()(mod)
output = func_3091()
func_3092 = relay.Function([], output)
mutated_mod['func_3092'] = func_3092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2684_call = mod.get_global_var('func_2684')
func_2686_call = mutated_mod.get_global_var('func_2686')
call_3134 = relay.TupleGetItem(func_2684_call(), 0)
call_3135 = relay.TupleGetItem(func_2686_call(), 0)
var_3140 = relay.var("var_3140", dtype = "float32", shape = (10, 11, 8))#candidate|3140|(10, 11, 8)|var|float32
bop_3141 = relay.bitwise_xor(call_3134.astype('int64'), relay.reshape(var_3140.astype('int64'), relay.shape_of(call_3134))) # shape=(10, 11, 8)
bop_3144 = relay.bitwise_xor(call_3135.astype('int64'), relay.reshape(var_3140.astype('int64'), relay.shape_of(call_3135))) # shape=(10, 11, 8)
output = relay.Tuple([bop_3141,])
output2 = relay.Tuple([bop_3144,])
func_3153 = relay.Function([var_3140,], output)
mod['func_3153'] = func_3153
mod = relay.transform.InferType()(mod)
mutated_mod['func_3153'] = func_3153
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3154 = relay.var("var_3154", dtype = "float32", shape = (10, 11, 8))#candidate|3154|(10, 11, 8)|var|float32
func_3153_call = mutated_mod.get_global_var('func_3153')
call_3155 = func_3153_call(var_3154)
output = call_3155
func_3156 = relay.Function([var_3154], output)
mutated_mod['func_3156'] = func_3156
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3171 = relay.var("var_3171", dtype = "float32", shape = (12, 9, 10))#candidate|3171|(12, 9, 10)|var|float32
var_3172 = relay.var("var_3172", dtype = "float32", shape = (12, 9, 10))#candidate|3172|(12, 9, 10)|var|float32
bop_3173 = relay.divide(var_3171.astype('float32'), relay.reshape(var_3172.astype('float32'), relay.shape_of(var_3171))) # shape=(12, 9, 10)
func_726_call = mod.get_global_var('func_726')
func_729_call = mutated_mod.get_global_var('func_729')
var_3187 = relay.var("var_3187", dtype = "float32", shape = (960,))#candidate|3187|(960,)|var|float32
call_3186 = relay.TupleGetItem(func_726_call(relay.reshape(var_3187.astype('float32'), [8, 8, 15])), 1)
call_3188 = relay.TupleGetItem(func_729_call(relay.reshape(var_3187.astype('float32'), [8, 8, 15])), 1)
func_2655_call = mod.get_global_var('func_2655')
func_2657_call = mutated_mod.get_global_var('func_2657')
call_3190 = func_2655_call()
call_3191 = func_2655_call()
func_2482_call = mod.get_global_var('func_2482')
func_2484_call = mutated_mod.get_global_var('func_2484')
call_3196 = relay.TupleGetItem(func_2482_call(), 2)
call_3197 = relay.TupleGetItem(func_2484_call(), 2)
func_2118_call = mod.get_global_var('func_2118')
func_2121_call = mutated_mod.get_global_var('func_2121')
call_3198 = relay.TupleGetItem(func_2118_call(relay.reshape(call_3196.astype('float32'), [10, 11, 8])), 0)
call_3199 = relay.TupleGetItem(func_2121_call(relay.reshape(call_3196.astype('float32'), [10, 11, 8])), 0)
output = relay.Tuple([bop_3173,call_3186,var_3187,call_3190,call_3196,call_3198,])
output2 = relay.Tuple([bop_3173,call_3188,var_3187,call_3191,call_3197,call_3199,])
func_3207 = relay.Function([var_3171,var_3172,var_3187,], output)
mod['func_3207'] = func_3207
mod = relay.transform.InferType()(mod)
var_3208 = relay.var("var_3208", dtype = "float32", shape = (12, 9, 10))#candidate|3208|(12, 9, 10)|var|float32
var_3209 = relay.var("var_3209", dtype = "float32", shape = (12, 9, 10))#candidate|3209|(12, 9, 10)|var|float32
var_3210 = relay.var("var_3210", dtype = "float32", shape = (960,))#candidate|3210|(960,)|var|float32
output = func_3207(var_3208,var_3209,var_3210,)
func_3211 = relay.Function([var_3208,var_3209,var_3210,], output)
mutated_mod['func_3211'] = func_3211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_3236 = relay.TupleGetItem(func_928_call(), 1)
call_3237 = relay.TupleGetItem(func_930_call(), 1)
output = call_3236
output2 = call_3237
func_3261 = relay.Function([], output)
mod['func_3261'] = func_3261
mod = relay.transform.InferType()(mod)
mutated_mod['func_3261'] = func_3261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3261_call = mutated_mod.get_global_var('func_3261')
call_3262 = func_3261_call()
output = call_3262
func_3263 = relay.Function([], output)
mutated_mod['func_3263'] = func_3263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1382_call = mod.get_global_var('func_1382')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_3270 = relay.TupleGetItem(func_1382_call(), 0)
call_3271 = relay.TupleGetItem(func_1384_call(), 0)
output = relay.Tuple([call_3270,])
output2 = relay.Tuple([call_3271,])
func_3281 = relay.Function([], output)
mod['func_3281'] = func_3281
mod = relay.transform.InferType()(mod)
mutated_mod['func_3281'] = func_3281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3281_call = mutated_mod.get_global_var('func_3281')
call_3282 = func_3281_call()
output = call_3282
func_3283 = relay.Function([], output)
mutated_mod['func_3283'] = func_3283
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3341 = relay.var("var_3341", dtype = "float32", shape = (15, 11, 12))#candidate|3341|(15, 11, 12)|var|float32
uop_3342 = relay.sigmoid(var_3341.astype('float32')) # shape=(15, 11, 12)
func_781_call = mod.get_global_var('func_781')
func_785_call = mutated_mod.get_global_var('func_785')
const_3386 = relay.const([[9,3,-4,1,-4,-9,2,5,-8,-9,5,7,10,5],[-8,-10,-2,-2,-1,-8,5,4,-5,-1,7,6,-6,9],[-2,4,5,4,-8,-4,3,-4,7,-6,-10,-5,-6,10],[1,10,6,-3,9,-10,8,-7,-6,-7,-2,7,-9,10],[-3,-1,-10,10,-4,-8,-2,3,-2,1,5,5,3,1],[6,9,-10,6,1,9,-8,-10,7,10,-6,-9,1,10],[10,7,-1,-5,-9,2,-6,-5,9,-7,-3,-6,-10,-1],[3,-6,-1,8,1,4,6,-10,-8,-9,2,-3,-2,3],[-8,-2,6,-3,-1,10,6,-2,9,-5,8,-5,-7,-7],[-9,-1,-7,-7,1,9,-1,-5,-2,-7,10,-7,7,1],[2,5,8,-8,8,-7,5,4,4,3,8,-6,-6,-9],[7,-7,7,8,-7,-2,4,-8,5,5,3,7,9,-2],[-6,-6,-2,-2,6,-6,-8,9,-10,-1,7,6,5,1],[-7,-9,-7,-8,1,-8,1,7,4,3,1,9,-1,9],[-10,-2,-7,-4,7,1,-3,2,-7,-7,-6,-7,4,8],[2,-3,-10,-1,-5,1,-8,-9,-3,7,3,3,2,-6],[-5,-4,-4,9,-10,-2,7,7,6,-6,-9,1,5,-1],[3,5,-4,4,6,1,-6,-2,-6,8,-5,3,5,5],[-7,9,6,7,-5,-7,8,8,2,-7,-9,10,-9,-9],[6,-4,-2,2,-9,5,4,6,1,6,-3,2,9,-7],[7,-3,-2,6,10,-2,-1,-2,1,8,3,7,-8,10],[-3,6,-5,-4,5,-2,10,-3,-5,7,-6,-9,-9,-5],[-5,4,3,1,8,6,-3,-8,6,-5,10,-6,7,5],[2,-2,-4,9,8,-5,3,-2,2,1,-5,9,-8,-4],[-8,10,-7,-9,1,-10,7,-7,-7,-7,1,8,-6,-3],[-10,1,4,-2,-4,-3,8,-5,-9,5,3,6,2,2],[-3,-4,10,2,5,-6,-4,7,2,-7,6,8,4,7],[-10,-3,4,7,-3,9,-5,-10,-5,3,8,-10,-1,-8],[-4,10,4,8,-3,3,6,-5,-8,-9,1,-2,-1,-7],[-3,-7,10,5,-3,3,10,1,9,-6,-10,-3,9,1],[-10,-2,3,-1,9,6,-9,-7,4,-4,5,-3,-6,-5],[2,5,-4,6,-8,-10,-3,6,-5,2,2,-6,5,-1],[4,6,-4,7,-7,7,9,2,-4,-5,-1,2,-2,-10],[8,10,7,-7,4,-1,6,-8,-5,-7,9,2,1,-5],[2,2,5,1,7,-5,3,-3,3,-4,-2,-1,-4,-2],[9,-8,3,3,3,1,4,-10,-9,-6,6,3,10,8],[-7,9,-8,-8,-8,-8,-5,-8,3,5,-2,-6,-10,8],[-5,6,-9,-9,-1,-7,-6,-9,-3,9,4,2,7,-6],[-9,9,-1,9,1,6,-4,2,-9,2,-5,-2,7,8],[-1,10,-9,5,5,9,-1,7,-9,7,9,1,-2,-6],[-4,4,-9,7,-7,-9,8,8,4,-5,6,2,-3,1],[6,8,-2,-9,-9,10,-1,-8,-6,6,-4,4,5,7],[-8,7,8,6,-8,-10,1,2,-8,9,-9,-5,-10,-4],[4,4,2,8,5,-9,-10,1,-8,3,5,1,1,-6],[-2,3,-4,7,-8,-7,10,-5,4,2,-9,1,9,8],[5,-8,-8,4,-9,9,8,10,1,-6,3,10,-3,8],[10,-1,-1,5,-1,3,-2,5,10,7,3,8,-3,8],[7,7,3,6,6,-5,-10,5,3,-3,-7,4,-6,-8],[3,3,3,9,8,1,-7,-9,7,9,5,-2,-4,4],[1,7,9,3,-1,-7,-10,-3,5,1,7,1,-4,6],[-9,8,-4,3,-6,-5,-1,-4,-1,5,10,-7,10,10],[-10,3,-9,-1,-5,-8,3,8,6,-6,-10,2,-10,6],[8,5,-4,-9,-9,-8,7,7,-9,-5,-8,9,-3,-7],[-9,-3,1,-7,6,6,6,-2,-1,-4,-6,3,-1,2],[-5,-7,2,-3,9,5,-6,1,-8,7,-3,-8,-2,-3],[-7,-7,3,-9,5,7,-2,9,7,3,4,5,-3,-8],[-7,-5,7,-7,5,5,-9,-6,-9,2,9,-1,5,2],[-10,2,3,-10,-9,-1,6,-8,10,-8,1,5,3,-2],[-2,8,-5,7,-6,-10,-7,-1,7,-8,3,4,-5,-3],[4,1,-10,-8,-7,-4,-6,-2,-5,6,2,7,-1,9]], dtype = "int32")#candidate|3386|(60, 14)|const|int32
const_3387 = relay.const([[-0.488674,-3.986406,-5.813268,6.635963,3.740115,-3.597045,-5.200031,-2.483270,-0.788602,9.922745,2.779134,-5.248399,-8.587538,-3.654284,6.534304,-6.516201,0.966539,-3.184172,0.197022,3.306151,-4.707331,8.449283,3.499572,-1.412336,2.768978,-5.630058,-0.955299,3.189515,-9.080729,6.804294,3.320310,-2.668658,-0.228181,-5.233859,-1.279210,-7.653892,9.300261,1.900799,8.309987,7.012932,7.140389,-0.484080,-8.823955,4.264055,7.450305,-4.508789,-1.870222,1.363328,4.387670,-8.825370,-3.907480,-6.692686,-8.717029,-9.276737,3.571435,-6.188338,-9.339144,2.298140,-8.995862,0.264398,6.993240,-6.374672,-4.564993,0.134820,-3.398267,3.061102,-7.472363,-1.266436,3.908925,6.236634,-0.596353,-2.436379,-8.349815,6.656851,-7.216500,-2.052714,-1.360015,9.037497,8.597974,2.652579,-1.237697,-9.319601,-8.913394,8.283265,2.821760,0.409219,-6.948710,-3.412115,1.132156,7.094203,1.246328,6.754548,6.327351,-7.512745,9.706204,-5.645049,9.913635,8.588863,9.305987,2.253857,3.704322,2.784013,-8.284051,-1.069527,7.877717,1.126773,9.190790,6.684264,6.600454,0.641148],[4.440359,-1.864805,-8.502555,-1.141910,-4.073730,7.790558,-0.314923,8.888567,-8.339407,-5.739180,-4.398804,-7.311352,0.980587,-6.578185,-6.764205,8.347366,9.651718,-0.674608,7.395917,4.133641,-8.741028,6.855307,7.834100,-5.308467,-5.720144,-0.388895,-0.821910,1.043905,-2.818778,1.969118,8.965526,-5.607311,-5.647104,4.955044,1.483352,-3.173504,5.250032,6.568783,-8.436655,-0.454165,-8.005160,7.357517,-6.618123,-5.613389,-8.040328,9.736432,9.956603,-5.151693,-6.174790,2.479110,4.447696,8.528507,-0.890453,3.599309,-3.868909,1.476052,-3.169846,-2.966311,7.535597,8.328212,-1.191614,-3.325315,-0.207615,6.507612,-2.766984,0.582148,-7.188792,-1.001206,1.300736,-0.163105,4.554264,-9.434671,-1.838329,-8.308471,-6.562023,-5.127512,-4.413159,-1.238378,7.674885,9.976688,-9.504475,5.891487,-6.543816,8.057542,-8.822927,9.702624,-0.698312,1.638615,-6.928561,-4.365374,-5.397993,6.471586,5.655607,5.667063,-0.792847,-3.138631,1.907629,3.581320,2.237845,4.861446,-2.779800,-5.459459,1.152780,-2.450676,1.803848,-9.443603,8.872276,6.499079,1.324114,5.283610],[1.853912,-1.641343,-8.827404,-8.321305,1.067939,0.606334,4.660141,-1.696817,8.354466,-8.125587,6.356987,-5.518284,0.719838,-5.155143,4.164718,-5.594467,5.147940,2.526366,-8.599750,-9.544990,-9.444485,-1.978133,6.463619,-2.797330,6.353985,2.782587,2.601606,0.302408,7.559083,3.997913,8.850192,-0.093948,-3.166684,-8.402589,7.458009,-1.790824,-1.462715,8.850447,9.201148,9.358747,3.443491,-4.283031,-9.736805,5.963121,2.071536,-7.845317,-6.933691,7.309140,0.608574,0.231250,-1.056239,-7.563814,-3.283282,-2.980043,6.486947,-2.308898,8.272640,7.733572,-5.807918,1.205058,5.884660,3.200047,-0.740261,-0.548713,-7.044445,0.135626,-9.182524,-2.361045,3.958616,-2.036967,-8.113473,1.301042,9.214408,7.722012,3.856281,1.465560,2.949040,-6.157240,-7.155478,3.003717,1.392172,1.924470,-9.469652,-6.714485,2.732211,-5.347474,-8.421543,9.156290,-9.897658,8.140407,5.484070,-5.014418,1.662295,0.039671,2.009760,4.482506,1.170724,-6.757770,-3.014140,8.862962,-4.984510,1.855212,-6.808513,-6.298024,6.277513,-8.045070,2.996888,9.890602,-1.036468,-3.762311],[4.448656,-5.457729,-8.916658,-9.909275,3.073468,-6.029381,4.501912,-2.033945,-8.800391,-6.041183,0.491285,1.724255,0.019924,4.266593,0.913917,-8.552082,2.013744,1.719536,6.169035,-5.665652,3.479587,-4.670754,-0.953701,-6.342456,-0.662429,3.694002,-8.349004,-0.004983,9.077041,7.075584,0.374112,-0.323174,-7.060902,-9.766557,0.025692,-4.296751,-7.963936,-8.045854,-8.574172,7.621062,1.686685,-2.860082,1.729052,-2.378789,-6.477224,0.491455,0.852203,1.295413,7.089975,5.154824,-1.072492,-3.098095,5.916890,-8.663935,8.111294,-1.378926,-2.619187,-6.193576,3.413500,-5.538157,-9.528041,1.763623,5.488364,8.906950,-5.005018,-2.567416,2.537505,5.796877,6.304377,-4.926524,-6.289204,0.578389,9.116582,-3.644773,-2.581755,-5.743538,0.842407,-0.139926,-4.450731,8.500391,3.573611,-8.565815,-8.739338,0.782494,7.239411,7.033879,-5.225574,-4.661335,-2.985893,-4.200441,4.762461,-2.302236,-5.273706,-5.637434,-1.937672,1.361680,4.118716,-1.397850,-8.242318,9.055680,2.934526,4.268042,0.780637,5.546651,-7.746694,0.228673,1.039054,-2.638681,-9.795933,-5.062090],[0.476181,-2.180511,2.273570,-6.954781,-8.296040,4.679556,-8.431634,2.704688,-1.256417,-3.585222,-1.246876,5.943464,7.202073,9.765408,-4.569350,-7.747770,-6.049036,-2.259788,-1.914541,2.029416,-6.123344,-6.898581,2.417967,-1.531141,2.188159,-8.742347,-4.953333,2.646832,-2.890584,-7.343488,-3.286772,-2.693401,0.900489,3.800444,0.725656,4.164896,5.848542,6.847639,4.076977,0.968170,-9.197218,7.839305,4.983199,-8.758734,0.191576,-9.963938,5.292789,-5.622634,8.225649,-7.935061,-1.779743,-3.953898,-0.057969,-5.456431,1.908332,-0.593266,-5.405047,7.149475,-9.202838,2.361404,-4.558681,2.527030,-1.564968,-2.483965,3.828445,-4.575383,-6.806631,-5.940447,-8.029086,7.445064,-3.174014,9.214481,8.625988,-5.244453,-8.470431,7.572223,3.380208,0.474808,0.128823,9.798543,-1.801645,-8.910520,-7.819098,6.581477,-6.064357,-6.509026,-5.458644,8.737505,-9.968502,0.387665,3.099643,3.647975,-2.801836,-3.387442,3.781696,-3.835169,1.911415,-1.641784,4.481325,9.576263,-0.330341,-1.314443,8.738411,-3.775936,5.900513,2.746548,4.365596,8.819289,5.857542,5.050285],[4.914933,-3.634066,-3.551242,-3.089354,0.326623,6.500297,-0.496494,-7.717297,5.259294,1.089998,2.720096,6.114192,-5.286136,-4.506401,-7.588277,-7.908344,6.447358,0.866917,5.327687,-1.295825,5.250468,4.673270,5.256024,6.717894,-8.317321,-2.312982,3.597104,-0.799395,-9.073258,1.694419,-5.854800,5.601887,2.803020,-8.104579,-1.786150,6.294041,-1.479554,4.076012,-3.301780,2.020898,-1.204807,-2.522868,9.399210,6.911010,5.400354,5.886206,-8.504827,-7.865607,2.211276,-3.015622,9.443468,6.553279,-6.115786,7.121704,3.157321,-0.689430,-5.450592,-0.163022,9.063130,-5.417859,-1.196214,3.879811,-6.784377,-8.060768,-4.938614,5.792819,-8.746000,8.724219,-4.607070,-5.270148,2.912598,7.887918,3.626734,-9.859692,6.183225,-6.511754,-8.827041,-6.431998,3.331654,-3.176966,7.478545,1.344706,-7.237954,6.019099,1.230404,-1.903589,-2.814121,9.439777,3.930216,-3.842091,-9.840513,9.714972,-9.709158,1.974404,-5.191280,9.219321,9.132529,-2.144216,-0.871071,-2.359515,0.433163,-8.007482,-5.980157,4.254083,7.853952,-5.941513,-3.543676,-3.044949,7.145016,-2.270851],[7.226863,-7.484297,-2.461586,-9.799602,-2.613237,0.533110,-2.496595,7.251510,5.583529,-0.953960,-5.844215,-4.151296,-3.211375,-4.920426,-9.790218,-4.324155,-2.926938,-2.374422,4.988630,9.618889,-8.676019,3.422840,9.394087,3.401685,2.645407,5.551402,0.911456,4.523692,6.709119,2.374346,-2.743889,2.147491,-8.226954,-6.900463,3.708588,8.667553,-5.741810,-8.668276,8.250277,-9.654665,2.369070,5.781442,9.601535,3.742193,-7.849951,-8.608902,-8.032007,7.771483,6.909239,-8.594896,-7.317491,-6.914298,-2.376393,-4.585116,0.189455,-6.171751,-9.875754,9.893702,-6.922226,-2.392658,4.148485,-2.452358,7.069923,6.673667,0.483832,2.018571,0.560510,-9.651148,-1.054661,-5.898218,7.746381,-5.811531,-8.662570,3.648736,-2.425788,0.753950,-6.852749,4.185738,2.587054,-3.924217,-2.108316,-2.074308,-7.938195,8.800276,7.679350,-5.873860,7.295401,9.122587,-4.125892,-6.080281,-9.490914,-4.137634,2.677750,-2.786435,-8.568795,8.092658,-2.826865,0.462637,-5.095310,1.447150,-2.797826,-4.309966,3.745353,9.189579,-5.429932,-1.055314,5.156372,1.943789,2.752364,3.096470],[8.615446,-7.753686,3.768192,-8.087240,2.990708,6.495544,3.478740,0.790112,7.427192,-9.566703,-3.579621,0.665774,9.092479,9.109639,-8.406766,8.985370,7.131920,-9.263213,0.573646,6.118515,-9.218449,-4.717148,-5.656853,-4.563986,-6.708670,-9.722670,-6.675252,-9.756252,-7.314243,-5.171132,-9.453233,-8.410715,1.099672,-2.464384,4.671802,8.372157,7.480928,6.714695,8.492874,9.680510,-0.001488,8.588956,0.197704,4.197722,8.871920,0.526346,2.237441,8.535899,-1.182285,5.889252,5.493861,8.880128,-2.793461,0.849360,9.725047,6.615513,-2.498969,-6.714514,-4.080273,9.823690,2.052169,2.978051,8.766823,7.524143,2.705196,6.248014,-3.657039,6.467252,-6.841240,-0.403961,4.126311,8.495277,-0.483651,-8.580772,5.414569,-2.738005,-7.511136,8.347038,3.783502,6.709950,3.027578,2.165656,4.554748,-4.446135,9.774954,6.854439,-6.699668,-9.411794,-4.400644,9.926700,4.016496,-5.993178,-3.252388,2.191583,4.002260,-1.941277,0.992377,-9.961244,-6.492495,-6.246910,4.409425,-5.348140,6.695151,6.266060,8.773439,0.019116,-3.496584,-3.393135,-6.349948,-9.636610]], dtype = "float32")#candidate|3387|(8, 110)|const|float32
call_3385 = relay.TupleGetItem(func_781_call(relay.reshape(const_3386.astype('int32'), [14, 10, 6]), relay.reshape(const_3387.astype('float32'), [10, 11, 8]), ), 1)
call_3388 = relay.TupleGetItem(func_785_call(relay.reshape(const_3386.astype('int32'), [14, 10, 6]), relay.reshape(const_3387.astype('float32'), [10, 11, 8]), ), 1)
output = relay.Tuple([uop_3342,call_3385,const_3386,const_3387,])
output2 = relay.Tuple([uop_3342,call_3388,const_3386,const_3387,])
func_3395 = relay.Function([var_3341,], output)
mod['func_3395'] = func_3395
mod = relay.transform.InferType()(mod)
mutated_mod['func_3395'] = func_3395
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3396 = relay.var("var_3396", dtype = "float32", shape = (15, 11, 12))#candidate|3396|(15, 11, 12)|var|float32
func_3395_call = mutated_mod.get_global_var('func_3395')
call_3397 = func_3395_call(var_3396)
output = call_3397
func_3398 = relay.Function([var_3396], output)
mutated_mod['func_3398'] = func_3398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_207_call = mod.get_global_var('func_207')
func_209_call = mutated_mod.get_global_var('func_209')
call_3406 = relay.TupleGetItem(func_207_call(), 0)
call_3407 = relay.TupleGetItem(func_209_call(), 0)
output = relay.Tuple([call_3406,])
output2 = relay.Tuple([call_3407,])
func_3437 = relay.Function([], output)
mod['func_3437'] = func_3437
mod = relay.transform.InferType()(mod)
output = func_3437()
func_3438 = relay.Function([], output)
mutated_mod['func_3438'] = func_3438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3468 = relay.var("var_3468", dtype = "int32", shape = (4, 15, 14))#candidate|3468|(4, 15, 14)|var|int32
var_3469 = relay.var("var_3469", dtype = "int32", shape = (4, 15, 14))#candidate|3469|(4, 15, 14)|var|int32
bop_3470 = relay.logical_xor(var_3468.astype('int32'), relay.reshape(var_3469.astype('int32'), relay.shape_of(var_3468))) # shape=(4, 15, 14)
output = bop_3470
output2 = bop_3470
func_3473 = relay.Function([var_3468,var_3469,], output)
mod['func_3473'] = func_3473
mod = relay.transform.InferType()(mod)
mutated_mod['func_3473'] = func_3473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3473_call = mutated_mod.get_global_var('func_3473')
var_3475 = relay.var("var_3475", dtype = "int32", shape = (4, 15, 14))#candidate|3475|(4, 15, 14)|var|int32
var_3476 = relay.var("var_3476", dtype = "int32", shape = (4, 15, 14))#candidate|3476|(4, 15, 14)|var|int32
call_3474 = func_3473_call(var_3475,var_3476,)
output = call_3474
func_3477 = relay.Function([var_3475,var_3476,], output)
mutated_mod['func_3477'] = func_3477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_563_call = mod.get_global_var('func_563')
func_565_call = mutated_mod.get_global_var('func_565')
call_3530 = relay.TupleGetItem(func_563_call(), 0)
call_3531 = relay.TupleGetItem(func_565_call(), 0)
func_207_call = mod.get_global_var('func_207')
func_209_call = mutated_mod.get_global_var('func_209')
call_3548 = relay.TupleGetItem(func_207_call(), 0)
call_3549 = relay.TupleGetItem(func_209_call(), 0)
func_2539_call = mod.get_global_var('func_2539')
func_2540_call = mutated_mod.get_global_var('func_2540')
call_3577 = relay.TupleGetItem(func_2539_call(), 0)
call_3578 = relay.TupleGetItem(func_2540_call(), 0)
func_3437_call = mod.get_global_var('func_3437')
func_3438_call = mutated_mod.get_global_var('func_3438')
call_3586 = relay.TupleGetItem(func_3437_call(), 0)
call_3587 = relay.TupleGetItem(func_3438_call(), 0)
output = relay.Tuple([call_3530,call_3548,call_3577,call_3586,])
output2 = relay.Tuple([call_3531,call_3549,call_3578,call_3587,])
func_3591 = relay.Function([], output)
mod['func_3591'] = func_3591
mod = relay.transform.InferType()(mod)
mutated_mod['func_3591'] = func_3591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3591_call = mutated_mod.get_global_var('func_3591')
call_3592 = func_3591_call()
output = call_3592
func_3593 = relay.Function([], output)
mutated_mod['func_3593'] = func_3593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_234_call = mod.get_global_var('func_234')
func_236_call = mutated_mod.get_global_var('func_236')
call_3607 = func_234_call()
call_3608 = func_234_call()
func_2179_call = mod.get_global_var('func_2179')
func_2181_call = mutated_mod.get_global_var('func_2181')
call_3621 = relay.TupleGetItem(func_2179_call(), 1)
call_3622 = relay.TupleGetItem(func_2181_call(), 1)
output = relay.Tuple([call_3607,call_3621,])
output2 = relay.Tuple([call_3608,call_3622,])
func_3638 = relay.Function([], output)
mod['func_3638'] = func_3638
mod = relay.transform.InferType()(mod)
output = func_3638()
func_3639 = relay.Function([], output)
mutated_mod['func_3639'] = func_3639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_3677 = relay.TupleGetItem(func_1104_call(), 0)
call_3678 = relay.TupleGetItem(func_1105_call(), 0)
func_2945_call = mod.get_global_var('func_2945')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_3681 = relay.TupleGetItem(func_2945_call(), 1)
call_3682 = relay.TupleGetItem(func_2947_call(), 1)
output = relay.Tuple([call_3677,call_3681,])
output2 = relay.Tuple([call_3678,call_3682,])
func_3685 = relay.Function([], output)
mod['func_3685'] = func_3685
mod = relay.transform.InferType()(mod)
output = func_3685()
func_3686 = relay.Function([], output)
mutated_mod['func_3686'] = func_3686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1292_call = mod.get_global_var('func_1292')
func_1294_call = mutated_mod.get_global_var('func_1294')
call_3719 = relay.TupleGetItem(func_1292_call(), 0)
call_3720 = relay.TupleGetItem(func_1294_call(), 0)
output = relay.Tuple([call_3719,])
output2 = relay.Tuple([call_3720,])
func_3761 = relay.Function([], output)
mod['func_3761'] = func_3761
mod = relay.transform.InferType()(mod)
output = func_3761()
func_3762 = relay.Function([], output)
mutated_mod['func_3762'] = func_3762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2945_call = mod.get_global_var('func_2945')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_3902 = relay.TupleGetItem(func_2945_call(), 0)
call_3903 = relay.TupleGetItem(func_2947_call(), 0)
output = call_3902
output2 = call_3903
func_3923 = relay.Function([], output)
mod['func_3923'] = func_3923
mod = relay.transform.InferType()(mod)
mutated_mod['func_3923'] = func_3923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3923_call = mutated_mod.get_global_var('func_3923')
call_3924 = func_3923_call()
output = call_3924
func_3925 = relay.Function([], output)
mutated_mod['func_3925'] = func_3925
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3965 = relay.var("var_3965", dtype = "int16", shape = (4, 15, 6))#candidate|3965|(4, 15, 6)|var|int16
const_3966 = relay.const([[[-10,-2,6,-4,5,-6],[2,-6,10,-9,-7,9],[10,-4,-6,7,-5,-5],[-8,-9,6,8,9,-7],[8,-3,-8,10,2,3],[10,-6,-8,-6,-1,-9],[-4,5,1,-4,9,-3],[-10,6,-6,3,-6,-10],[1,1,5,-9,7,4],[-7,6,-8,2,3,-1],[5,-6,3,7,4,-6],[-10,-9,10,-4,2,10],[10,-7,7,1,-1,5],[2,10,10,8,2,6],[1,-8,9,-4,-1,1]],[[10,-2,-8,9,-6,10],[6,7,-5,1,-2,-2],[8,-1,8,8,3,-1],[4,-3,-8,8,10,1],[8,-3,10,3,-9,8],[10,5,4,6,-5,-10],[-1,8,-4,7,2,4],[3,-1,-6,2,-5,-9],[3,8,-4,5,-9,-9],[4,6,-3,-8,-10,1],[-8,-1,-9,3,-6,4],[-3,5,3,-8,-9,-1],[-7,-1,7,-2,-6,-1],[1,-9,-9,7,3,6],[8,-1,8,-9,2,-9]],[[-5,-6,-4,-6,-3,4],[-1,3,-2,9,1,-7],[3,-2,-10,-4,4,6],[8,-4,8,-2,8,-2],[-2,-2,-1,4,7,-9],[-8,1,-2,3,10,1],[-7,6,8,-8,9,7],[-9,5,6,-4,-4,10],[4,8,-3,2,3,5],[-8,-4,-1,10,-2,7],[-7,-4,-7,-9,-8,-3],[-7,8,4,3,-4,-2],[8,6,-5,7,5,-4],[-6,1,3,2,2,-2],[-5,10,-2,6,-4,-1]],[[9,-2,-1,-7,3,-10],[4,8,4,-2,-5,-10],[-7,-8,-1,10,8,4],[-2,6,-9,-2,10,10],[-8,-5,-7,9,-1,4],[7,-4,10,4,-9,5],[-9,-2,7,-5,4,-9],[2,6,-6,-7,-6,7],[9,8,-6,-5,-10,-3],[10,-3,7,7,9,-5],[4,9,5,8,9,-1],[8,9,-4,6,-10,8],[10,-9,9,-5,9,2],[10,-5,5,4,-3,-1],[7,1,-6,-7,4,-7]]], dtype = "int16")#candidate|3966|(4, 15, 6)|const|int16
bop_3967 = relay.less(var_3965.astype('bool'), relay.reshape(const_3966.astype('bool'), relay.shape_of(var_3965))) # shape=(4, 15, 6)
output = relay.Tuple([bop_3967,])
output2 = relay.Tuple([bop_3967,])
func_3991 = relay.Function([var_3965,], output)
mod['func_3991'] = func_3991
mod = relay.transform.InferType()(mod)
var_3992 = relay.var("var_3992", dtype = "int16", shape = (4, 15, 6))#candidate|3992|(4, 15, 6)|var|int16
output = func_3991(var_3992)
func_3993 = relay.Function([var_3992], output)
mutated_mod['func_3993'] = func_3993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3638_call = mod.get_global_var('func_3638')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_4018 = relay.TupleGetItem(func_3638_call(), 0)
call_4019 = relay.TupleGetItem(func_3639_call(), 0)
output = relay.Tuple([call_4018,])
output2 = relay.Tuple([call_4019,])
func_4022 = relay.Function([], output)
mod['func_4022'] = func_4022
mod = relay.transform.InferType()(mod)
output = func_4022()
func_4023 = relay.Function([], output)
mutated_mod['func_4023'] = func_4023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_234_call = mod.get_global_var('func_234')
func_236_call = mutated_mod.get_global_var('func_236')
call_4043 = func_234_call()
call_4044 = func_234_call()
output = call_4043
output2 = call_4044
func_4063 = relay.Function([], output)
mod['func_4063'] = func_4063
mod = relay.transform.InferType()(mod)
mutated_mod['func_4063'] = func_4063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4063_call = mutated_mod.get_global_var('func_4063')
call_4064 = func_4063_call()
output = call_4064
func_4065 = relay.Function([], output)
mutated_mod['func_4065'] = func_4065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2655_call = mod.get_global_var('func_2655')
func_2657_call = mutated_mod.get_global_var('func_2657')
call_4068 = func_2655_call()
call_4069 = func_2655_call()
func_2568_call = mod.get_global_var('func_2568')
func_2570_call = mutated_mod.get_global_var('func_2570')
call_4091 = relay.TupleGetItem(func_2568_call(), 1)
call_4092 = relay.TupleGetItem(func_2570_call(), 1)
output = relay.Tuple([call_4068,call_4091,])
output2 = relay.Tuple([call_4069,call_4092,])
func_4093 = relay.Function([], output)
mod['func_4093'] = func_4093
mod = relay.transform.InferType()(mod)
output = func_4093()
func_4094 = relay.Function([], output)
mutated_mod['func_4094'] = func_4094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2655_call = mod.get_global_var('func_2655')
func_2657_call = mutated_mod.get_global_var('func_2657')
call_4137 = func_2655_call()
call_4138 = func_2655_call()
func_2613_call = mod.get_global_var('func_2613')
func_2615_call = mutated_mod.get_global_var('func_2615')
var_4164 = relay.var("var_4164", dtype = "float32", shape = (96,))#candidate|4164|(96,)|var|float32
call_4163 = relay.TupleGetItem(func_2613_call(relay.reshape(var_4164.astype('float32'), [2, 4, 12])), 1)
call_4165 = relay.TupleGetItem(func_2615_call(relay.reshape(var_4164.astype('float32'), [2, 4, 12])), 1)
func_3437_call = mod.get_global_var('func_3437')
func_3438_call = mutated_mod.get_global_var('func_3438')
call_4168 = relay.TupleGetItem(func_3437_call(), 0)
call_4169 = relay.TupleGetItem(func_3438_call(), 0)
func_4022_call = mod.get_global_var('func_4022')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_4187 = relay.TupleGetItem(func_4022_call(), 0)
call_4188 = relay.TupleGetItem(func_4023_call(), 0)
output = relay.Tuple([call_4137,call_4163,var_4164,call_4168,call_4187,])
output2 = relay.Tuple([call_4138,call_4165,var_4164,call_4169,call_4188,])
func_4189 = relay.Function([var_4164,], output)
mod['func_4189'] = func_4189
mod = relay.transform.InferType()(mod)
mutated_mod['func_4189'] = func_4189
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4190 = relay.var("var_4190", dtype = "float32", shape = (96,))#candidate|4190|(96,)|var|float32
func_4189_call = mutated_mod.get_global_var('func_4189')
call_4191 = func_4189_call(var_4190)
output = call_4191
func_4192 = relay.Function([var_4190], output)
mutated_mod['func_4192'] = func_4192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3086_call = mutated_mod.get_global_var('func_3086')
call_4204 = relay.TupleGetItem(func_3085_call(), 1)
call_4205 = relay.TupleGetItem(func_3086_call(), 1)
output = call_4204
output2 = call_4205
func_4210 = relay.Function([], output)
mod['func_4210'] = func_4210
mod = relay.transform.InferType()(mod)
output = func_4210()
func_4211 = relay.Function([], output)
mutated_mod['func_4211'] = func_4211
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4217 = relay.var("var_4217", dtype = "float32", shape = (11, 7, 13))#candidate|4217|(11, 7, 13)|var|float32
const_4218 = relay.const([[[-0.525255,1.517204,-3.801019,3.578032,-7.291877,9.405669,7.532439,-1.864953,-1.132117,-2.679474,-4.612907,1.422645,6.960427],[-7.623974,-0.419192,-8.391180,-0.075655,9.063444,0.808397,-4.576149,5.851504,-2.523614,2.627043,-2.012171,-3.831208,-4.881302],[-5.258320,-6.836822,-9.364481,-7.682130,9.873152,-7.827946,-8.744750,-4.445479,-1.560851,5.824004,-6.842083,-9.608205,-1.581531],[2.192335,0.357093,3.161610,6.974554,1.060085,-0.142591,-4.062680,-1.388165,9.829496,2.125249,-0.609950,-5.013257,0.106203],[-1.187063,0.582266,-4.795768,9.520764,-9.969123,1.393129,-8.798129,-1.275863,-3.638781,-1.747172,2.102598,8.673077,8.755082],[-8.350077,8.772601,-1.779011,3.205139,-0.749746,-8.830099,3.126388,-7.744893,-4.006737,9.424518,5.183692,-7.036499,-7.885018],[0.710399,-9.813791,-3.796098,2.887528,-8.172468,0.995225,6.756175,-0.963573,8.564392,-1.565762,-6.620654,-0.089295,4.623078]],[[-0.978322,-7.716794,6.561974,-9.142813,-8.467248,-2.928423,2.710845,-8.608842,-5.927233,-4.529419,3.387256,-6.594199,-0.701932],[0.667467,-8.422244,-8.961339,-3.966005,-3.272436,1.785637,8.831752,1.224320,7.746815,-1.477555,0.831515,3.816023,4.182296],[4.911543,-6.023229,1.533461,-7.717256,1.978894,-1.066233,2.339071,3.557242,3.543787,2.092483,6.446823,9.183063,-3.213898],[-2.519598,8.791035,-3.000320,-3.400455,-0.756919,-6.060814,9.635664,9.917547,1.486291,-2.804889,5.339573,9.947777,-2.559379],[9.430772,3.573242,-4.002087,4.591480,0.713605,-2.645586,9.142580,9.426712,-5.479869,6.572538,-4.677328,-6.414687,5.688838],[5.574124,-0.681988,6.553822,6.027311,8.317376,6.272044,3.344377,4.507817,-6.090254,-0.437061,-0.416991,-2.542757,3.247808],[8.606157,-8.671233,0.129595,2.954350,9.850004,-2.763761,6.208225,6.218466,-9.121378,-4.274716,-1.939231,-4.718296,-3.758969]],[[3.403794,-6.729482,-5.283040,7.419522,5.196535,-7.959236,-7.834725,7.511781,-1.267441,8.320141,2.769670,3.757431,8.838321],[-7.537900,-5.652033,-8.007904,-1.314206,-6.340716,-5.920872,5.556380,5.221127,1.130432,4.088083,-1.817936,3.552562,9.705607],[0.091737,-5.427390,8.252723,6.369354,-4.771835,6.852637,-0.973240,4.727624,9.507635,-0.692386,-7.972540,0.046551,7.466457],[9.974243,6.752311,6.950295,2.778337,6.847220,5.063046,5.183340,-3.627427,-9.981936,-0.683960,-0.064087,-0.266498,-5.062636],[-0.873597,-4.472730,8.433706,-9.763983,7.430079,-2.985724,-1.491326,6.861129,-1.635992,1.250382,9.831950,5.006988,9.243747],[-2.307792,8.409795,-8.307662,-5.312672,6.631732,-5.299196,-7.422392,2.096100,6.876093,-4.449588,9.155650,6.747303,3.995890],[-3.634470,-6.068227,-3.213455,2.557966,-6.582959,3.185927,3.647279,-4.984657,3.742373,4.054589,2.096422,-9.630196,3.227527]],[[-6.787833,-4.481285,3.306749,1.345643,-3.478313,-5.390898,9.315858,6.035224,2.596544,6.738561,-4.980874,-5.212701,9.678196],[-5.067116,6.812460,-1.196157,-2.628729,-7.459443,6.341350,-1.312777,8.118415,-7.299945,9.719449,-6.291186,-3.376168,-6.841572],[-6.555872,-0.180371,7.964342,7.991477,-6.382915,-5.025917,-1.229855,-2.387239,-1.199171,8.728391,-9.657182,-6.055846,4.900943],[-0.120359,-2.757386,-7.772875,-5.909620,4.893758,-7.807947,-4.152507,-5.147083,1.869277,6.260720,-6.380692,-2.601769,-8.526225],[5.240602,-3.461310,9.751295,-4.377950,-6.262602,-8.155218,4.540202,-3.671051,-2.564309,-0.166132,5.576575,0.896529,-3.309749],[8.639176,5.943340,5.456526,-5.056701,2.885582,-5.486577,-6.701019,-3.597809,6.141268,-9.750414,8.899526,8.595926,0.024724],[-8.028627,7.218842,-8.750051,5.288880,-1.057780,7.747226,9.958776,-6.386063,-6.901296,-7.027670,8.629546,3.493912,2.104361]],[[-0.295681,-3.234962,7.940342,-2.277279,8.451111,9.982553,-6.733435,1.984206,6.483938,-7.713402,1.938127,-7.647458,-5.730606],[2.216456,2.592886,-4.159303,4.686253,9.596474,6.876800,-1.751472,-6.634899,-4.499641,6.436593,-5.479966,-7.906224,4.297573],[-8.992889,9.629337,0.167843,-9.064948,8.046433,6.988042,3.220874,9.075088,-8.985537,-3.690262,-9.577614,-7.898167,-2.607980],[-9.969047,9.796337,-7.229898,3.046304,-9.336465,3.399795,0.119195,-5.314924,9.721890,4.331364,-2.635600,-0.879055,-4.922475],[5.706506,5.248306,-2.195966,-8.975597,4.265305,3.639628,-3.345191,1.159302,-9.366327,-4.309877,0.254645,-3.821982,6.972959],[4.036123,9.880555,-1.009553,-3.787304,1.256912,8.591710,-8.827264,-9.151366,6.002837,-6.078807,-6.220795,3.966752,7.979561],[1.895040,9.423610,-4.819283,-7.894619,-3.437593,4.129615,-1.785007,8.600973,-1.825629,-5.773506,8.822808,-8.825217,0.522292]],[[-4.864752,7.456075,9.878524,-4.324101,3.304392,3.282749,-1.780404,-5.067781,-9.161256,-2.966117,-0.339963,-8.348805,-1.948272],[-9.987613,5.999577,3.905613,-8.014580,5.740412,7.015381,-4.054073,-0.704486,9.443685,-2.239216,-5.007844,-5.213037,-3.891504],[-7.874362,-0.771514,4.106934,5.128340,-1.925023,-9.568633,2.827613,-9.704426,7.469661,-2.583509,4.272927,0.935269,4.995150],[-2.314767,-7.688157,5.991491,3.513166,6.175624,-7.798387,7.393271,-2.335613,-5.028241,1.174804,-2.216820,2.477749,1.480014],[-0.828349,-0.268206,-6.982062,-2.694358,-2.423199,5.459441,0.161006,-5.121859,4.824045,-5.457369,5.396469,-8.900357,2.745936],[-1.460223,1.520810,0.431224,-9.813741,3.481973,8.252504,3.449432,6.516223,9.959740,-0.128948,8.802769,-0.838489,3.214668],[-0.262590,-8.907483,-7.660324,-5.063950,-9.664199,-8.598996,-2.169336,-1.988809,7.435908,8.823798,-9.054062,2.060752,-3.481538]],[[7.508544,-9.398670,-1.292356,-1.411019,-8.747776,6.629137,-4.287169,6.758691,-8.764679,-8.966613,4.642836,5.068344,5.162409],[4.373762,-9.775028,2.910008,-7.591077,-4.045708,-1.764971,-3.730142,8.814359,6.954134,8.981334,-1.227700,-4.691331,-4.270990],[-8.901930,-6.272590,-1.404139,-6.457595,0.547416,-9.873951,3.109401,3.746176,8.160438,7.821039,5.934556,-7.600738,5.551043],[8.866099,8.737423,9.452781,9.454552,0.289699,8.175371,-6.508846,1.672152,2.630260,2.158044,-1.580088,-4.200129,3.259427],[1.897457,-0.480883,0.234270,-3.879048,-0.359075,-6.594336,-5.607095,8.340833,-0.599780,-6.762333,-8.521461,-6.304078,-1.729012],[-0.088443,-3.483087,7.940065,5.082527,-4.477254,6.633227,7.325654,-2.628812,2.308371,-5.374822,9.450155,-7.621091,-9.414623],[5.018569,-9.920261,-4.374455,-2.391041,-3.423637,-3.883365,4.274294,-4.480699,6.052091,-7.523065,-7.169773,-3.059879,-1.212363]],[[4.806517,-7.032752,6.861871,-6.006212,2.988827,-5.879079,-0.243704,6.544515,-4.536069,4.092158,2.828431,6.036107,9.075001],[6.220975,-7.845271,6.035440,-6.675198,9.594870,8.484640,3.743978,-8.808800,-3.558210,2.027718,6.151165,-1.368063,-9.898731],[-0.701561,-7.964423,5.658016,9.492218,2.230335,0.763211,-6.613176,-4.125204,0.152409,9.132286,1.414429,-7.173186,9.124591],[3.114624,-2.752357,-8.816072,6.201832,-2.636835,-2.817175,-4.641658,-5.418567,-6.885508,-4.670030,-5.930068,-2.672042,-3.778824],[4.343102,-2.094339,-8.480055,5.134146,-2.811867,7.374828,-6.479241,-2.884789,-6.019026,-8.132060,5.589334,2.588177,9.609690],[5.574578,9.183545,-1.173186,-6.969668,-5.885764,-3.018666,4.694536,2.648874,-6.359189,7.878477,-8.061931,1.455206,-0.480780],[2.654927,-7.566988,-9.468076,5.518556,1.468735,-9.910126,-1.137909,0.060425,-5.633148,2.090774,5.379569,9.744027,3.497802]],[[-5.940651,5.584931,1.103365,2.088416,4.938860,7.328667,7.181699,-1.742958,-5.500460,-3.783554,2.628980,-3.231240,-8.446074],[-2.102272,-8.635351,-4.979407,-8.092568,-2.323035,-7.735727,-9.959937,5.292000,-1.571175,-5.606779,-7.317175,-4.561451,-4.677510],[-0.585719,-8.286083,6.640473,-8.146978,-2.954428,-0.841829,-9.004992,-6.126016,-5.320117,8.163040,-7.492895,6.607642,-4.490448],[1.021449,-0.321004,2.592467,0.848887,-4.653420,-6.957041,-7.124431,3.456698,-3.635775,6.355288,-8.485419,0.665846,1.309087],[-5.297190,-3.312759,4.244706,5.082218,-1.145768,-6.691346,-6.459807,-7.526815,5.883231,-7.034532,7.741189,7.338798,8.512977],[6.620708,3.186019,4.233807,2.749621,-2.654351,6.608065,-8.651863,-3.699499,2.222650,4.446592,-5.060760,8.450368,1.583808],[1.097123,1.584056,9.640297,4.447165,-3.268362,-5.459355,-3.581785,-5.317255,-0.059910,3.930450,0.830984,3.757805,-3.829269]],[[4.836521,-9.357227,8.097612,5.625747,9.522717,3.978732,4.616495,9.396500,3.502127,8.759999,1.458195,-2.682646,-9.353804],[-1.741417,2.863437,8.581892,-6.746550,6.630403,5.574405,-9.149803,9.909666,3.202750,1.857349,-1.475513,7.365332,-9.739667],[5.354445,3.338915,-9.546054,-0.834427,8.925622,3.225167,3.435917,1.108487,8.248606,1.374430,3.333803,-0.971433,4.160537],[1.476582,-9.921022,-2.877525,-8.605100,1.027441,2.665592,-6.259300,-9.989341,-0.174530,6.600302,-3.601938,3.525572,8.125176],[2.740055,-3.280710,7.145754,1.704189,0.632788,3.970147,7.186033,1.348023,-7.671867,5.026125,6.662276,2.993571,7.429356],[2.551657,9.644308,7.755478,-2.411570,-3.489186,1.227249,1.811080,0.641702,6.369328,-7.142786,4.150278,-9.721044,9.124680],[-4.338702,-6.784264,-2.491469,-5.426301,4.230346,-7.291882,8.171557,4.787427,-6.090255,-3.011147,0.879417,7.280894,-5.506676]],[[7.916454,3.922391,-5.846230,9.438693,-4.842125,-8.865465,1.282832,-9.219788,-9.073079,-2.834093,0.952331,-7.906291,-9.119572],[3.165541,8.706789,-6.555249,-4.780838,7.495854,6.511656,-3.926658,5.481557,7.382701,-5.298495,-8.754241,6.984982,-8.415935],[-1.687616,-1.557461,-5.885638,-5.651814,5.875330,-8.243330,-5.376629,-3.928064,-3.273546,1.947158,-0.327895,4.968554,4.301702],[4.159649,-5.115017,1.596047,-6.077670,-5.050643,0.052859,8.425492,2.633752,-6.473271,4.211847,-0.839243,2.098028,1.618115],[-5.297789,-7.993206,7.429057,-9.175853,9.024732,-5.240885,-4.252312,6.103727,3.027422,-4.773128,-6.438256,-5.960218,-4.846732],[-7.772550,3.385656,0.993682,-8.165839,9.991894,4.252564,4.914490,2.339315,-2.833056,-8.309402,0.204133,-3.865898,7.372036],[-1.074147,3.499413,-8.876421,0.068780,9.787791,7.320483,-0.096795,8.179048,-3.105414,2.535158,-9.981141,7.833794,1.885212]]], dtype = "float32")#candidate|4218|(11, 7, 13)|const|float32
bop_4219 = relay.power(var_4217.astype('float32'), relay.reshape(const_4218.astype('float32'), relay.shape_of(var_4217))) # shape=(11, 7, 13)
output = relay.Tuple([bop_4219,])
output2 = relay.Tuple([bop_4219,])
func_4231 = relay.Function([var_4217,], output)
mod['func_4231'] = func_4231
mod = relay.transform.InferType()(mod)
mutated_mod['func_4231'] = func_4231
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4232 = relay.var("var_4232", dtype = "float32", shape = (11, 7, 13))#candidate|4232|(11, 7, 13)|var|float32
func_4231_call = mutated_mod.get_global_var('func_4231')
call_4233 = func_4231_call(var_4232)
output = call_4233
func_4234 = relay.Function([var_4232], output)
mutated_mod['func_4234'] = func_4234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3086_call = mutated_mod.get_global_var('func_3086')
call_4238 = relay.TupleGetItem(func_3085_call(), 0)
call_4239 = relay.TupleGetItem(func_3086_call(), 0)
output = relay.Tuple([call_4238,])
output2 = relay.Tuple([call_4239,])
func_4273 = relay.Function([], output)
mod['func_4273'] = func_4273
mod = relay.transform.InferType()(mod)
mutated_mod['func_4273'] = func_4273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4273_call = mutated_mod.get_global_var('func_4273')
call_4274 = func_4273_call()
output = call_4274
func_4275 = relay.Function([], output)
mutated_mod['func_4275'] = func_4275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1134_call = mod.get_global_var('func_1134')
func_1136_call = mutated_mod.get_global_var('func_1136')
call_4306 = relay.TupleGetItem(func_1134_call(), 0)
call_4307 = relay.TupleGetItem(func_1136_call(), 0)
func_234_call = mod.get_global_var('func_234')
func_236_call = mutated_mod.get_global_var('func_236')
call_4315 = func_234_call()
call_4316 = func_234_call()
func_139_call = mod.get_global_var('func_139')
func_140_call = mutated_mod.get_global_var('func_140')
call_4359 = func_139_call()
call_4360 = func_139_call()
func_480_call = mod.get_global_var('func_480')
func_483_call = mutated_mod.get_global_var('func_483')
var_4377 = relay.var("var_4377", dtype = "float64", shape = (462,))#candidate|4377|(462,)|var|float64
call_4376 = relay.TupleGetItem(func_480_call(relay.reshape(var_4377.astype('float64'), [11, 3, 14])), 0)
call_4378 = relay.TupleGetItem(func_483_call(relay.reshape(var_4377.astype('float64'), [11, 3, 14])), 0)
func_2945_call = mod.get_global_var('func_2945')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_4403 = relay.TupleGetItem(func_2945_call(), 0)
call_4404 = relay.TupleGetItem(func_2947_call(), 0)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_4409 = func_2294_call()
call_4410 = func_2294_call()
output = relay.Tuple([call_4306,call_4315,call_4359,call_4376,var_4377,call_4403,call_4409,])
output2 = relay.Tuple([call_4307,call_4316,call_4360,call_4378,var_4377,call_4404,call_4410,])
func_4415 = relay.Function([var_4377,], output)
mod['func_4415'] = func_4415
mod = relay.transform.InferType()(mod)
var_4416 = relay.var("var_4416", dtype = "float64", shape = (462,))#candidate|4416|(462,)|var|float64
output = func_4415(var_4416)
func_4417 = relay.Function([var_4416], output)
mutated_mod['func_4417'] = func_4417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1104_call = mod.get_global_var('func_1104')
func_1105_call = mutated_mod.get_global_var('func_1105')
call_4502 = relay.TupleGetItem(func_1104_call(), 0)
call_4503 = relay.TupleGetItem(func_1105_call(), 0)
func_3207_call = mod.get_global_var('func_3207')
func_3211_call = mutated_mod.get_global_var('func_3211')
const_4508 = relay.const([[1.658564,-4.582379,2.314274,-8.327626,-2.058893,4.838895,-7.624445,-2.035676,-9.723325,-1.220811,7.670803,7.632231,-8.267143,4.208810,-4.284185,-3.351627,-8.311264,-3.098697,4.291951,-4.066428,-4.616825,7.793170,-5.177699,1.615959,4.910204,-2.203313,4.166198,5.154331,-4.025403,-8.146455,-9.780753,-0.062538,7.148166,7.394429,-3.823775,1.477867,6.414698,1.612669,-3.071549,-7.539199,1.610377,1.834426,-2.190606,-3.761840,1.381041,0.989830,9.961303,-5.628997,-6.827690,-0.539993,-6.115305,-2.370137,-7.258339,3.724532,-5.794258,-6.417552,-4.844810,-9.699363,-8.641597,5.678294,2.765133,-6.139126,7.703665,-4.777539,-3.743048,-6.820441,-9.175265,-6.869685,-5.917106,2.239244,0.037591,-7.056985,9.868385,-9.959622,-6.823180,0.435897,-7.928388,-7.512111,3.323258,-2.265621,0.809644,-4.632590,7.241353,-8.390701,-9.307428,-3.355138,2.661991,-0.689458,8.136808,0.627775,-4.845801,4.120421,-3.258806,-0.387119,-5.643505,8.718101,2.030879,7.224795,-9.920727,5.183241,-1.788979,-5.474169,-6.450072,-7.950090,4.674908,6.830940,9.786132,-3.282743,3.822037,7.256760,6.138500,9.914235,-9.212864,9.779404,1.085980,9.183168,-9.943045,6.068220,-0.654797,-5.092100,4.880455,-0.500180,6.212072,-9.946008,7.727684,-2.451606,-1.745518,-4.297033,0.318551,2.646129,-2.531617,-3.128085,-6.230567,3.068468,9.884246,-6.237930,-1.831979,9.235726,-2.548414,-1.138915,5.910905,-3.734472,-5.567372,-2.272785,8.380095,-4.237632,7.854163,-5.076891,9.684413,-5.244098,-8.543217,7.874855,4.979817,-2.748196,3.266993,-5.160851,5.414238,-5.711503,4.724889,7.356222,6.923522,-0.163475,-9.645748,-6.622818,-4.652560,1.543696,-8.193149,3.764450,3.774352,2.177817,-0.984945,-6.727528,-4.792354,-9.749981,4.861704,-1.835018,7.756785,9.911030,-1.784679,6.301361,8.371232,4.476846,-4.729294,5.432170,-6.772873,-4.906382,-0.946212,-6.492079,7.074261,-9.200416,3.889654,8.348042,3.172880,-3.833401,3.395760,5.616717,-8.687955,-9.783585,6.283638,6.405477,-2.696448,9.910741,-0.348977,9.349306,-7.328064,-8.500144,3.884944,-7.050218,5.839439,-5.529030,2.672357,3.296726,-0.403480,-2.155991,9.178023,9.552595,2.791695,1.560017,-4.003373,7.639658,-2.978758,-8.690424,-1.193460,1.827617,-8.099774,-8.411369,6.123651,2.697717,5.291754,1.475330,2.190211,-6.403879,4.037943,-1.084758,-0.042965,-1.716055,-6.453916,-2.815485,-1.252795,-7.369222,4.282294,-2.550307,-2.303995,-1.742028,8.762092,-5.970273,-5.804782,2.710528,-5.861658,-6.345061,6.122898,-3.405363,3.998642,-1.304437,-8.128620,-5.455277,9.042873,-1.429445,1.610700,5.449350,-8.100891,1.197468,-0.674994,2.159607,1.631797,-8.443005,-7.429790,-6.966198,9.184832,4.086233,9.650836,-3.358328,-9.134341,-9.672897,7.684289,-9.384534,4.742248,3.309776,-7.428537,5.527984,-8.940747,0.196872,-6.711411,-6.477278,-9.358809,0.990403,-6.652590,9.965534,-4.163702,-4.849752,8.678848,9.478542,-7.151709,7.283919,3.140025,-3.192212,-5.446745,3.054099,4.237589,-0.190982,8.485845,3.268888,5.450299,1.688515,-2.761203,-0.789512,-5.964672,1.081556,-0.250837,-4.779101,6.551896,8.912651,-9.468442,-9.816597,-2.931832,3.089439,-7.460647,8.843755,7.474072,9.866868,-8.908309,-4.380459,9.224497,-6.689517,-5.694862,-6.849623,9.357303,1.569000,-3.670797,-2.588453,-2.614536,-1.319245,-4.588583,2.464524,-0.502951,-8.676392,-6.030320,-1.185654,-2.531255,4.049103,5.761469,-6.053850,0.434013,-0.072222,5.843231,-3.176659,-2.783657,-8.082955,9.958713,0.357426,-7.236792,-9.436699,-1.200890,-7.242271,6.252906,2.612827,6.824633,-6.864309,0.498745,-9.243362],[6.038476,-9.697326,-8.405633,-5.409501,-3.924821,3.035357,6.225577,8.926523,-9.177307,-4.324324,9.630195,-1.717154,7.147044,4.297725,8.798357,6.210887,8.968683,7.894768,-1.252805,3.164160,0.567969,3.084024,-8.411961,-6.516106,9.989358,9.214929,-4.041869,4.888006,-0.349245,-9.600630,3.821016,-1.730446,6.034941,-9.388229,4.620237,5.437845,-1.126434,-5.621007,3.977236,-7.479544,5.075962,-9.495627,1.042948,-8.191552,-9.361548,-4.676131,-0.777989,-2.471626,-8.436899,-9.691799,-8.403809,-7.369394,-8.743989,-8.379638,9.931257,-8.749457,-6.534750,-2.385234,3.541880,5.891527,5.896705,1.522499,-1.369238,8.874919,-7.514664,-9.582094,0.426673,7.071281,2.809816,-9.235235,-5.765177,-6.208480,1.335784,8.722465,7.288173,-5.848096,-0.347780,-2.667484,-3.329217,6.055522,8.772870,1.307162,-3.091512,9.326642,-0.263656,-5.444642,-5.359367,5.517681,1.994712,-9.096076,7.575286,0.711541,-7.870702,-4.975775,1.040623,2.213175,-2.538330,-9.446782,-8.255040,-5.778986,9.682592,8.774191,9.467983,9.753708,8.710604,9.795855,-0.016564,-5.885265,4.125839,9.819183,-0.134262,6.196484,-2.641519,6.340189,8.151712,3.300480,-9.117734,6.119155,-3.706212,-0.805726,-1.189675,-0.858451,-4.178416,-9.688381,-7.025608,0.024570,-9.920858,7.151385,-5.861378,6.173730,-4.614574,-9.618195,-0.183177,1.375193,-4.428368,-8.630254,2.748856,6.346144,-1.102188,2.092488,-9.615868,2.885265,-3.935990,4.234381,-8.703022,-3.591323,7.680135,4.936902,-8.737056,-4.699376,6.035227,-9.870242,-3.933799,-2.333609,9.281727,7.551457,-1.739380,-2.630870,1.844578,1.337389,2.325376,-7.763646,-9.083692,-8.502187,-7.789297,4.178184,7.629224,7.952099,-2.866527,-0.415683,7.576823,1.456973,5.372486,-0.462421,8.054708,-2.553134,-3.047820,6.322507,-5.807063,1.176394,3.569674,-9.597020,-2.741599,-9.115134,-5.894961,-1.120022,-6.557012,3.860532,-8.337156,-1.567682,-2.558609,-4.541372,4.137858,3.607704,2.403702,5.278104,-3.972688,1.013607,3.361101,7.747404,6.386677,5.778300,7.484953,2.025691,7.298293,9.113406,-6.721380,-6.268331,5.948146,8.962955,-9.669863,9.186994,1.519726,-8.026731,-1.727885,-2.374931,1.944906,6.160070,-6.852447,-2.116811,-0.182322,6.185218,6.607922,6.257954,-5.779775,5.290779,6.211121,3.953668,-0.859285,9.594565,7.422139,-8.146951,0.277741,8.053720,-1.228587,9.823789,0.116538,1.108501,-4.403344,4.321882,2.642078,-7.914456,-0.487260,3.054323,0.972665,8.048406,-4.321866,8.063834,-6.671315,-3.041436,5.199924,9.159987,-6.167351,9.296874,4.804016,3.928542,-8.811097,7.268684,3.063241,3.466306,8.474018,1.899262,-0.438321,-8.454798,8.634373,8.147309,-9.953295,7.515556,3.591558,-5.662372,-1.983172,6.330071,4.826128,1.238966,-4.269023,5.291497,6.310048,6.759555,6.126485,-0.556866,-1.177438,1.217151,5.623451,-4.211313,-6.497568,0.667081,-8.481820,4.065282,-2.882612,5.746734,4.992191,-7.874141,6.414092,-2.345706,9.279539,-4.662328,-2.160487,7.889459,-9.851650,-5.764571,-1.753495,4.029014,-6.015657,-0.552672,3.653932,5.688551,-7.578555,-2.599524,-2.035478,-0.192037,2.169120,4.231816,5.033431,0.849517,-2.947131,-6.231948,-7.196126,-6.868696,-1.227525,6.471606,-3.658498,-7.252300,-7.163951,-6.521573,7.505409,3.221531,2.098193,-4.750892,1.274171,0.712849,2.453263,-1.220445,3.164270,-4.314539,9.725237,-3.963230,8.459812,-4.895831,4.823469,-8.393485,4.709909,4.186635,-6.903073,8.277174,-8.744912,-1.975233,-5.348509,1.943570,2.669703,3.877829,0.624231,-9.707567,-7.648467,-7.080253,9.235038,-3.762163,-8.984695,-5.064432,9.513325,-2.569384],[-2.503290,6.159830,8.937880,-0.947170,5.489636,7.014176,1.691127,1.623230,-2.738621,4.503329,-5.457662,0.467091,-4.839920,5.006315,5.864441,4.017667,-5.378303,0.786401,5.928133,-3.271019,8.062173,2.451475,5.468903,1.101523,-5.724991,-5.885527,-9.188714,-0.318504,0.925104,6.563778,4.103017,-4.685882,8.789194,-4.670488,3.887572,8.625740,-0.413289,-0.288104,3.988058,-8.875026,-1.800925,-3.837113,-2.740889,5.901678,1.112440,-6.936998,1.923782,-0.384466,-9.367927,3.388024,-3.950707,5.708414,5.829343,-6.290833,2.584564,7.047715,2.460547,-0.093006,-5.779058,4.745618,-4.673049,-4.889015,-9.987327,2.768544,4.725186,3.446792,7.176878,1.216334,-8.807608,-9.794488,-5.240021,4.474992,5.777872,0.700505,-5.128445,4.809156,-1.207878,-8.221117,2.236213,-7.830968,4.003526,-3.117174,-2.359606,6.501830,9.044026,-1.854210,9.515376,-8.772941,9.927217,-4.044216,-2.413745,2.500736,-1.086309,-9.554273,1.444434,-5.534794,-8.891195,5.692164,-9.063906,8.373681,-5.919840,6.890036,4.665788,5.005586,6.048061,-0.445281,4.254269,6.368705,-1.712073,0.686099,-0.122182,-3.806933,-9.071645,4.932717,-9.187491,6.742760,-2.106395,4.827482,-9.188498,-7.606731,-1.899631,4.794651,-0.020577,6.489517,-3.666842,-1.678683,7.634553,8.598582,0.329478,-3.723903,3.205330,-5.040046,3.795870,-6.556881,-5.905040,8.959833,7.433615,1.923977,9.408654,-8.889401,1.903170,-8.861786,1.495657,1.825536,-9.022997,8.346545,1.151971,1.588269,4.551109,-6.780891,9.044466,-0.047557,-9.916637,-2.998029,4.228803,-2.972654,-3.912619,8.585659,-0.174750,-4.747283,-3.201709,9.457805,2.897752,-5.127472,-3.390386,0.814388,8.032194,-7.070556,2.436108,6.668274,-9.453079,0.555387,3.299021,-2.787386,3.669627,-9.228707,-0.278741,1.774408,8.078034,-1.648430,-5.109470,0.167403,-2.028806,-5.886568,-8.772268,-4.119294,8.463535,8.060817,-3.910646,-2.959686,-3.271566,4.938570,-5.525309,0.273703,9.037516,8.787159,4.815239,6.939855,0.454103,3.611345,5.343254,-4.640102,8.907321,3.220669,2.461590,-8.852820,7.517214,6.996970,-0.071796,0.643488,-8.928038,-9.135030,7.169992,1.961870,3.323006,-7.525219,-5.360229,1.320828,7.262999,4.559707,-7.102154,-4.283407,-2.914282,-3.938437,-6.735316,-5.201972,-8.229074,-4.725744,-7.491242,-8.787563,-5.213432,-5.365991,3.723884,5.430549,8.808159,-5.196904,-3.101771,6.202249,-4.932513,7.658229,7.126751,2.527934,-8.029126,8.375265,-8.082591,-3.331152,-0.062472,2.934776,-0.053062,-4.136157,-2.235217,-4.276597,-7.424217,6.065476,2.487170,4.068137,-5.187874,-9.211212,4.010456,7.547623,-0.007834,-1.917094,-0.484310,-5.353420,-8.883118,-1.473649,3.724528,0.362629,-4.768796,-0.137693,-6.411782,-7.821015,3.515867,4.601806,-1.602807,-9.471225,2.644899,-3.348370,-4.635958,-4.612876,2.463941,4.138867,4.414039,-1.343004,7.625163,1.678441,3.010907,-1.569374,9.944314,6.338679,-1.245049,-8.484310,-0.067923,-4.467901,4.628025,-9.072659,0.993685,-0.421578,-0.967779,4.029813,5.494720,4.417507,-0.729073,1.062186,-2.398845,-0.887230,-6.301523,-4.727804,8.131364,-6.442438,3.837240,2.163343,-8.660505,-6.936305,9.688147,0.315911,-7.045928,5.171944,-0.723069,-8.247097,9.659104,-6.107673,3.535888,-5.607638,3.404883,-9.171940,7.658346,0.845162,2.740043,9.478453,7.890887,3.418985,8.377551,6.645569,-8.185040,-7.757321,-7.029110,7.717156,5.961092,-6.376703,-8.776679,-9.121390,-2.671691,-0.168704,2.067042,-1.351950,-5.871011,-9.634020,-3.259006,6.284822,-9.556402,-5.694267,-1.370132,-4.623892,-6.528875,-5.177875,7.743938,-1.281632,7.279250,6.273486]], dtype = "float32")#candidate|4508|(3, 360)|const|float32
const_4509 = relay.const([[9.072213,6.063546,-9.241721,-5.794164,2.832435,5.052172,7.409906,3.893528,-6.356569,8.710159,-4.245887,-6.768203,-6.825084,3.216951,1.890331,-7.309272,3.251607,-5.394853,4.849785,7.179841,-9.680975,-0.930187,-2.887643,-6.550875,-0.859274,-4.854131,8.174793,6.472674,7.396531,-5.859302,1.321647,3.601277,-1.054717,6.663167,1.661110,-1.175420,6.096172,4.737134,-3.700289,-4.662858,4.783353,5.256112,8.602533,8.329939,1.561037,6.226467,-6.483562,-6.045388,4.056853,-4.408955,-0.344724,-5.330592,-3.290426,6.987665,2.823444,3.165679,8.681524,7.372562,6.705428,4.226780,-0.563996,-3.389400,6.866759,2.353447,-3.301033,5.653337,0.297730,-3.489593,-6.626984,-6.795804,2.364240,-9.017794,7.630621,9.638790,-9.862137,8.163009,1.485466,3.369882,-0.729393,8.842524,8.634167,4.654159,-7.917316,-5.414608,-8.314998,6.831009,-3.332905,-8.552415,7.328873,-1.266763,-0.731402,1.178773,5.922893,-1.774122,2.187025,-4.930225],[7.467102,1.835097,2.036312,-3.259085,9.735441,5.779570,0.889005,2.068477,5.073852,8.456935,2.894799,-3.145039,6.733109,2.677460,-4.984473,7.773214,9.797491,-2.579914,-1.105375,-5.174915,-7.988638,2.078244,6.108121,-1.988700,0.323139,-7.321989,-2.171188,3.052862,-1.778244,5.749816,0.392193,-7.347500,1.859159,6.453119,7.843370,4.676928,-3.051319,6.505741,8.971574,-4.730760,1.351099,-1.324403,8.323549,-3.956514,-9.818670,6.109596,-0.993082,-8.745205,-4.998815,-3.978959,-4.454246,2.443237,-5.647544,-5.003889,-7.882345,-0.652200,-3.847143,-5.317706,9.208285,1.701372,-1.974266,4.748585,-2.139221,-2.721343,2.769324,-3.250939,7.783499,-7.977959,-8.031456,8.960451,-0.690856,7.400287,-4.216773,-7.378736,-5.257278,0.067821,-6.483440,6.990792,0.587457,3.842460,-7.415310,-0.930820,7.599092,-2.785614,0.483004,3.555709,9.817455,-0.252204,-7.528109,2.501484,-6.348726,5.068001,8.053862,3.524719,-8.263889,-5.855367],[-9.063967,-8.612955,4.183947,-8.339600,5.168624,-8.952973,-9.714524,-7.295695,-8.579649,8.450573,8.647472,0.528424,9.912688,1.464314,-9.075051,8.419089,-6.449316,-1.467559,-5.428776,-4.567426,-4.784396,-4.108027,-3.123357,7.956331,8.909026,9.728460,9.802069,8.169596,-4.743296,9.164830,-0.368860,0.852292,-2.629118,7.276441,-7.135667,-7.449983,-1.944787,3.448741,-7.426546,7.683188,8.143831,-8.496511,-3.948885,-3.848971,-4.660044,8.417175,-5.452654,0.468092,-3.146599,9.621498,-2.183739,-0.335356,-0.005817,3.523270,-6.510907,-2.365406,-7.134271,7.149320,3.245521,1.785985,1.199774,-7.981226,0.824843,-4.580021,-8.490634,0.100825,-6.161740,-8.120386,5.458245,5.222274,-6.191508,-0.885245,-0.394714,0.381507,2.342722,0.939857,4.767888,-8.175102,3.729771,2.789481,-0.418270,-3.500578,-1.436685,4.830514,7.991983,5.875677,3.570778,-5.664356,0.390743,1.746260,-1.106655,2.029098,-7.805080,-3.104440,3.724117,-7.958470],[-4.831845,-7.227784,5.508106,8.258244,-7.281286,-0.148661,-3.846410,0.805731,7.980259,-2.227086,0.218973,6.256448,1.412328,8.827454,3.164737,-5.158305,-3.636203,-2.701052,-3.153737,-1.971179,6.165208,-7.186154,1.610261,8.882543,-9.304502,-5.936880,-3.764728,-3.040593,-6.123443,-4.395978,2.358556,0.572604,5.380354,5.210175,8.479401,-7.617115,-0.589142,-4.702800,-8.050909,-2.356105,4.953487,-7.324639,4.499605,5.045773,-7.898715,2.003359,-6.890470,3.916292,9.992054,-1.817552,0.167283,4.763138,0.058875,8.667060,2.951807,7.839909,8.994228,-6.307452,-1.382947,-7.255129,2.013516,-4.420793,-0.503309,5.399386,-9.842696,2.954025,-2.020872,9.866833,-4.735198,2.722193,9.801650,0.049626,-5.164980,2.642139,0.290489,6.332560,1.347998,6.427330,-2.199581,5.316913,-6.913457,-1.254324,3.161410,-3.162457,-5.387588,-4.229189,-5.833997,-6.524432,7.524425,2.722590,2.096739,-1.241569,-8.806642,2.583240,-7.629998,1.611665],[5.119339,-0.936038,-9.553595,-5.157687,-6.116481,-2.515015,-5.235133,-8.248733,-4.120528,5.079759,-8.741771,-9.464234,4.657729,7.895630,9.360796,-4.827732,-2.050772,3.978499,0.662201,-7.293691,-6.567447,0.391637,9.554329,8.986922,2.692934,-3.101704,-1.528505,2.801918,-9.139922,3.023465,0.789398,-1.745645,-0.568089,-6.332277,5.263816,-6.482641,9.126193,0.790357,3.659193,-7.514516,9.492993,-0.210409,-0.099287,8.781633,1.077837,-1.741630,-3.019083,-9.039834,-1.271382,-8.473884,8.922231,-1.717587,-1.300241,-9.065214,-6.452521,0.279113,3.361088,5.606194,9.428198,-4.009682,5.000446,6.858373,3.202043,7.378445,7.941104,1.103780,-5.800551,1.564834,3.784822,-2.487848,7.318220,7.226687,8.371440,-9.344689,7.696827,6.795876,3.380051,-7.459069,8.592969,-9.619356,-5.381886,3.701081,6.398497,2.811285,-1.355557,-8.084710,3.744546,-6.106326,-1.308862,6.750762,5.698031,2.366604,-9.621540,7.119653,0.449099,-7.511678],[-1.196209,-2.451956,-3.175876,-7.041947,5.660120,-5.757627,2.500399,9.524145,3.781329,7.633406,-7.693445,4.724935,7.255751,-2.356437,1.807891,-5.656327,-3.811277,1.945731,-5.468862,-8.185461,0.600797,2.368338,8.616234,-6.174128,2.042322,-5.551827,-8.101571,-1.937583,-6.452812,-7.106817,2.871715,1.321904,9.035522,0.924331,9.736845,4.552873,-4.431890,7.946814,-2.493484,2.844767,0.512048,0.679045,5.231559,4.786204,-5.621673,7.690449,-6.092317,3.915961,-8.607540,-5.270259,-3.051344,-6.240118,-7.514765,1.832438,0.022699,-4.584657,-5.908593,7.484124,-7.424449,6.127692,-0.843676,-8.736321,-2.781480,6.534962,-8.683572,-3.292822,5.282539,-2.239366,-5.297908,-7.578319,-5.177042,-8.351824,-6.874595,-2.290283,5.891758,2.889326,8.544904,-5.403933,-8.756130,-7.048948,0.972022,7.364380,1.896602,-1.281377,9.696685,1.132064,-1.158468,-0.788483,5.770548,7.654347,8.561565,5.739338,-3.767316,-1.820162,0.160002,-1.371915],[0.037080,9.832837,6.164356,-9.616070,1.609815,-7.659752,5.785511,-9.897606,7.015022,6.169444,0.904294,9.259341,7.932770,-2.541742,-2.896327,8.106439,-6.695731,-7.799784,2.657681,3.395112,4.196652,-2.876986,-2.937994,4.987634,-7.447112,-4.577937,9.785376,1.433247,2.839697,4.657228,-5.466756,0.354103,-0.655059,-8.968071,-7.842454,-6.371189,4.752238,6.319015,2.617763,-2.899418,8.502743,7.742642,-6.094960,1.311277,-9.419911,-7.778630,-9.444628,-2.157806,9.594439,-1.479057,-1.806405,4.198340,7.320345,7.211688,-7.728838,-5.834163,0.891188,-8.116053,-7.897990,3.643597,2.568498,-4.884756,-8.550373,-8.713810,4.655883,2.363815,5.383318,-2.896314,4.414917,0.006768,4.518925,-7.288727,-9.504348,-8.547782,-8.302727,4.405581,3.206114,9.407895,-2.499412,-6.894947,-3.526655,0.536004,-9.181317,-8.363488,-6.600946,7.095023,0.929179,-5.291109,6.673650,2.662136,-7.540260,7.119211,-3.863088,6.271717,-7.611486,-9.008482],[-4.188763,-1.666667,8.360309,-3.235338,-5.462904,1.094951,5.067932,1.227836,3.470304,9.766459,-4.844619,7.284143,3.057896,1.750181,-8.888697,4.682144,-3.488067,-2.931566,-3.271294,4.058827,-0.530297,2.316636,-5.550793,-2.951195,8.114383,4.026674,-5.293501,-8.993092,-0.487222,7.576575,9.502353,5.998907,-5.143432,-3.426772,-3.560834,-1.772781,-3.663918,8.794520,-8.336820,-6.895743,8.733117,5.542270,0.555729,6.476876,-3.934238,-0.808520,9.689082,8.522180,7.135317,4.351904,6.769109,1.687065,6.390095,-3.094991,-4.115994,2.225392,-2.608879,-7.172372,-3.755345,8.394805,-3.500688,-6.899402,1.656840,-8.547205,4.567338,6.044694,0.621675,7.765214,7.911774,-2.391195,-4.117393,6.179565,8.934350,-2.399516,2.033294,-4.216040,-2.493557,-4.954271,-9.873662,-9.914803,-1.853063,-6.677712,-6.961480,-2.013161,2.171921,-7.411034,-0.267490,-7.981409,5.915960,0.126129,3.568329,-7.281645,-4.491708,6.450949,0.221741,3.256327],[1.764209,6.903583,1.145166,0.684063,9.843956,-3.171538,1.934073,1.894320,-9.357117,-6.652504,-0.536361,5.611392,1.772371,9.826774,-3.922579,-5.576762,-3.914838,-9.413667,6.310028,-9.915922,8.692738,-8.834576,7.161731,5.770777,-7.357797,8.668166,-2.255778,1.222428,-7.168979,5.729912,9.642404,-9.205175,0.513974,3.017733,5.456043,8.254111,9.694768,2.682773,3.039762,-1.260838,-9.962911,-8.672113,-3.339038,-3.596511,-4.604505,8.650496,3.521718,1.035348,-6.927126,8.117922,-6.769049,-5.802996,-5.096001,3.498302,-0.742668,0.659684,5.508462,-2.529091,-6.686610,-0.165710,-6.440924,-2.195970,-2.866705,-4.286548,6.495236,-0.958689,0.699680,8.980242,-9.731326,6.072579,-6.477894,-7.240984,3.855776,8.431161,9.331174,-3.960555,6.846601,-2.513338,0.618851,3.129948,-9.326717,-8.235640,-4.747378,-4.637720,-9.282659,-3.322075,-5.555716,8.788216,3.832854,4.240715,-8.608579,-1.004154,7.157712,1.462701,6.179901,7.961513],[-2.115973,5.579382,0.590244,-6.489148,-0.227463,-2.887593,9.079279,-1.236878,-4.473171,4.712187,5.093901,-9.401069,-1.477584,5.024914,-7.650978,-1.406027,4.252488,-6.340201,1.626033,-7.666230,5.294902,-7.351894,-5.091128,4.959795,7.743907,-1.673271,-1.484506,0.563783,-7.919627,-6.614623,3.844240,-4.180562,3.480596,5.578140,7.940558,-9.362943,-0.039193,7.229263,0.423527,6.391014,4.351687,6.114173,-9.344726,2.974212,-8.131520,-0.566419,-1.104555,-0.308530,4.942876,-2.892074,9.709467,5.059614,4.525185,1.633992,9.606600,9.798515,-7.439523,-6.338360,4.761590,1.640234,7.073369,7.793039,-4.861361,1.570088,5.151104,-0.130984,-7.251335,-0.212817,-0.544658,-1.239586,-8.236434,3.036397,9.954497,-0.940337,2.972978,-3.405809,4.911303,-8.832874,9.236941,3.032999,1.584457,1.403043,8.057195,3.668353,2.929014,0.564197,-0.503214,-5.905686,-1.099013,-9.952133,2.469065,-5.019128,3.984557,-9.549357,3.805468,5.412703]], dtype = "float32")#candidate|4509|(10, 96)|const|float32
call_4507 = relay.TupleGetItem(func_3207_call(relay.reshape(const_4508.astype('float32'), [12, 9, 10]), relay.reshape(const_4508.astype('float32'), [12, 9, 10]), relay.reshape(const_4509.astype('float32'), [960,]), ), 4)
call_4510 = relay.TupleGetItem(func_3211_call(relay.reshape(const_4508.astype('float32'), [12, 9, 10]), relay.reshape(const_4508.astype('float32'), [12, 9, 10]), relay.reshape(const_4509.astype('float32'), [960,]), ), 4)
uop_4513 = relay.log(const_4509.astype('float32')) # shape=(10, 96)
func_998_call = mod.get_global_var('func_998')
func_1001_call = mutated_mod.get_global_var('func_1001')
call_4520 = relay.TupleGetItem(func_998_call(relay.reshape(call_4502.astype('float32'), [10, 11, 8])), 1)
call_4521 = relay.TupleGetItem(func_1001_call(relay.reshape(call_4502.astype('float32'), [10, 11, 8])), 1)
output = relay.Tuple([call_4502,call_4507,const_4508,uop_4513,call_4520,])
output2 = relay.Tuple([call_4503,call_4510,const_4508,uop_4513,call_4521,])
func_4524 = relay.Function([], output)
mod['func_4524'] = func_4524
mod = relay.transform.InferType()(mod)
output = func_4524()
func_4525 = relay.Function([], output)
mutated_mod['func_4525'] = func_4525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
call_4557 = func_1152_call()
call_4558 = func_1152_call()
output = relay.Tuple([call_4557,])
output2 = relay.Tuple([call_4558,])
func_4559 = relay.Function([], output)
mod['func_4559'] = func_4559
mod = relay.transform.InferType()(mod)
output = func_4559()
func_4560 = relay.Function([], output)
mutated_mod['func_4560'] = func_4560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3638_call = mod.get_global_var('func_3638')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_4561 = relay.TupleGetItem(func_3638_call(), 0)
call_4562 = relay.TupleGetItem(func_3639_call(), 0)
func_3085_call = mod.get_global_var('func_3085')
func_3086_call = mutated_mod.get_global_var('func_3086')
call_4582 = relay.TupleGetItem(func_3085_call(), 1)
call_4583 = relay.TupleGetItem(func_3086_call(), 1)
output = relay.Tuple([call_4561,call_4582,])
output2 = relay.Tuple([call_4562,call_4583,])
func_4588 = relay.Function([], output)
mod['func_4588'] = func_4588
mod = relay.transform.InferType()(mod)
output = func_4588()
func_4589 = relay.Function([], output)
mutated_mod['func_4589'] = func_4589
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4590 = relay.var("var_4590", dtype = "uint32", shape = (4, 2, 3))#candidate|4590|(4, 2, 3)|var|uint32
const_4591 = relay.const([[[-6,4,-2],[6,8,-9]],[[-5,8,-8],[-7,-10,5]],[[-4,-6,-2],[-2,7,-4]],[[2,9,1],[8,-6,-10]]], dtype = "uint32")#candidate|4591|(4, 2, 3)|const|uint32
bop_4592 = relay.maximum(var_4590.astype('uint32'), relay.reshape(const_4591.astype('uint32'), relay.shape_of(var_4590))) # shape=(4, 2, 3)
output = relay.Tuple([bop_4592,])
output2 = relay.Tuple([bop_4592,])
func_4608 = relay.Function([var_4590,], output)
mod['func_4608'] = func_4608
mod = relay.transform.InferType()(mod)
var_4609 = relay.var("var_4609", dtype = "uint32", shape = (4, 2, 3))#candidate|4609|(4, 2, 3)|var|uint32
output = func_4608(var_4609)
func_4610 = relay.Function([var_4609], output)
mutated_mod['func_4610'] = func_4610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3281_call = mod.get_global_var('func_3281')
func_3283_call = mutated_mod.get_global_var('func_3283')
call_4645 = relay.TupleGetItem(func_3281_call(), 0)
call_4646 = relay.TupleGetItem(func_3283_call(), 0)
func_1454_call = mod.get_global_var('func_1454')
func_1458_call = mutated_mod.get_global_var('func_1458')
const_4651 = relay.const([[-9.133673,-2.399245,-7.278799,-6.237491],[8.824546,-9.495343,9.436841,-5.086759],[3.422414,-9.994832,-0.510138,9.432584],[3.264111,4.847790,6.828164,7.877112],[-2.143971,5.089214,-4.440490,7.425034],[9.710803,1.512852,-7.399213,-2.553337],[-9.114848,4.239476,4.006633,0.963078],[-7.558867,8.949356,7.633195,9.624517],[-0.092901,-8.155943,-4.297196,-5.333423],[3.085092,-9.734944,9.804795,-3.179548],[-5.015637,1.219301,-5.469984,-3.784655],[0.487444,-1.926274,-6.242113,-2.065747],[6.247509,-4.001079,-5.010946,1.647366],[-2.559954,1.325512,-7.002294,9.548346],[-8.330152,7.331568,-8.340467,2.839469],[5.556841,-0.440803,2.178212,-7.112660],[1.724952,-9.541793,9.986243,-8.926826],[9.049996,-1.286818,3.743646,-9.396900],[-1.480765,-4.485990,-5.312691,-4.459443],[-4.516079,3.652366,2.019696,-7.558963],[-3.769549,1.193088,-1.032917,-9.478832],[7.202999,7.219458,-1.739921,-3.545591],[7.227699,7.264365,-3.934754,2.712065],[-4.394144,-8.328420,-4.694628,0.342066],[7.289204,6.733411,-7.298477,-2.529752],[-1.452313,-1.683409,5.491451,4.252737],[4.861945,-2.641153,-9.477650,-4.878670],[2.136549,-4.874620,7.605166,-8.759272],[-3.916095,-5.927942,2.700471,1.341611],[2.615086,9.610987,-0.956369,8.579573],[8.129273,-7.825244,-1.956833,4.827289],[4.613366,2.058957,9.231603,-3.865992],[6.160622,-3.918012,5.754930,-4.377261],[2.974707,2.932921,-5.098512,5.972590],[3.278082,6.257437,9.350028,0.815602],[6.311089,0.659475,-9.442531,-2.170743],[9.644567,2.234110,-2.569216,4.728244],[0.491606,-9.113306,8.177134,1.988947],[3.783045,-5.853071,8.689832,4.424593],[0.999877,8.406114,-6.009877,9.624246],[-6.743085,-4.480496,3.051147,-6.728364],[2.039113,-8.097040,6.421570,6.979346],[5.404736,4.071199,2.241635,6.004634],[1.786689,-9.862555,-4.385360,4.618040],[-3.488648,-5.813183,9.392242,-8.022593],[6.260576,-0.776085,7.092663,0.127743],[1.894010,5.513532,8.661163,4.602848],[-3.908641,3.736769,-8.662621,3.326488],[-7.546682,-7.892463,6.045812,-7.757886],[7.978442,7.302600,-8.465063,0.891407],[2.859862,-8.415028,2.204388,3.795967],[-8.668264,3.994046,-7.737917,7.204875],[-9.918874,-4.813508,2.103287,-2.059082],[1.935381,0.849332,-2.016582,-4.625471],[4.315284,-2.073198,-6.219134,-6.225732],[-2.862938,3.419502,9.060535,-6.114349],[-0.528048,3.685298,3.339726,4.580262],[3.274155,9.806139,8.087359,1.073783],[-5.609095,-9.580840,4.917556,4.955042],[-8.506257,-5.125717,-2.043538,7.288237],[-6.288060,-1.967401,-5.648521,-5.451158],[-9.400301,5.191193,0.540548,-2.958568],[-8.442230,9.952237,-9.499933,-9.181004],[9.445788,-5.919188,1.820082,2.293225],[-9.371307,7.479456,8.390970,-8.971460],[2.145980,1.438965,-8.220896,7.117189],[-0.215195,-5.110992,9.161413,5.649455],[-3.306308,-4.944186,2.133038,1.756420],[2.146588,-0.256550,-5.710188,-7.840793],[-2.066307,0.958233,-1.727562,-5.675183],[2.274238,3.035739,1.043496,9.753817],[-8.723843,3.452001,6.999103,5.968592],[1.534502,8.213673,-8.839670,-5.717215],[-6.160534,4.736314,-2.177584,4.239833],[-0.847158,-1.032039,-9.306582,4.510036],[-7.712736,-5.051583,5.797418,-0.783897],[-4.569202,2.656399,-6.782041,5.105425],[0.274303,8.560104,-5.050049,2.664281]], dtype = "float64")#candidate|4651|(78, 4)|const|float64
const_4652 = relay.const([[True,True],[True,True],[False,True],[False,True],[False,False],[False,True],[True,True],[False,False],[False,True],[False,False],[False,False],[True,True],[False,True],[False,False],[True,False],[True,False],[True,False],[True,True],[True,True],[False,False],[True,False],[True,False],[False,True],[False,False],[False,True],[False,True],[True,True],[False,False],[False,False],[False,True],[False,True],[True,False],[True,False],[True,True],[True,False],[True,False],[False,False],[True,False],[True,True],[True,True],[False,True],[False,False],[True,False],[False,True],[True,False],[True,True],[False,False],[True,True],[True,True],[False,False],[True,True],[True,True],[True,False],[False,False],[True,True],[False,False],[False,False],[False,True],[True,False],[True,False],[False,False],[True,False],[False,True],[False,True],[False,False],[False,True],[False,True],[False,True],[True,False],[False,False],[True,False],[False,False],[False,False],[True,True],[False,False],[True,True],[False,True],[True,True],[False,True],[False,False],[False,False],[True,False],[True,True],[True,False],[False,True],[True,True],[True,True],[True,False],[False,True],[True,False],[True,True],[True,False],[False,True],[True,False],[False,True],[False,False],[False,True],[False,True],[False,False],[False,False],[True,True],[False,True],[False,True],[True,False],[False,False],[True,False],[True,False],[False,True],[True,True],[True,False],[False,True],[False,False],[False,True],[False,True],[True,False],[True,False],[True,True],[True,True],[True,False],[False,True],[True,True],[True,False],[True,True],[False,True],[False,True],[True,True],[True,True],[True,True],[False,True],[False,True],[True,False],[False,False],[True,True],[False,False],[False,False],[False,True],[True,True],[True,False],[True,True],[True,True],[True,False],[False,False],[False,False],[True,False],[True,False],[False,True],[False,False],[True,True],[True,True],[False,True],[True,False],[False,False],[True,False],[True,False],[True,False],[False,False],[True,False],[False,True],[False,False],[True,False],[False,True],[True,False],[True,False],[True,True],[False,True],[False,True],[True,True],[False,True],[True,True],[True,False],[True,True],[True,False],[False,True],[True,False],[True,True],[False,True],[False,True],[True,False],[False,True],[True,False],[False,True],[True,False],[False,True],[True,True],[False,False],[False,False],[False,True],[False,False],[False,False],[False,False],[True,True],[True,True],[False,True],[True,False],[False,False],[False,False],[False,False],[False,False],[True,True],[False,False],[False,False],[False,False],[True,False],[False,True],[False,False],[True,True],[True,True],[True,False],[False,False],[False,False]], dtype = "bool")#candidate|4652|(210, 2)|const|bool
call_4650 = relay.TupleGetItem(func_1454_call(relay.reshape(const_4651.astype('float64'), [13, 8, 3]), relay.reshape(const_4652.astype('bool'), [10, 42]), ), 5)
call_4653 = relay.TupleGetItem(func_1458_call(relay.reshape(const_4651.astype('float64'), [13, 8, 3]), relay.reshape(const_4652.astype('bool'), [10, 42]), ), 5)
output = relay.Tuple([call_4645,call_4650,const_4651,const_4652,])
output2 = relay.Tuple([call_4646,call_4653,const_4651,const_4652,])
func_4654 = relay.Function([], output)
mod['func_4654'] = func_4654
mod = relay.transform.InferType()(mod)
output = func_4654()
func_4655 = relay.Function([], output)
mutated_mod['func_4655'] = func_4655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3685_call = mod.get_global_var('func_3685')
func_3686_call = mutated_mod.get_global_var('func_3686')
call_4700 = relay.TupleGetItem(func_3685_call(), 1)
call_4701 = relay.TupleGetItem(func_3686_call(), 1)
func_2636_call = mod.get_global_var('func_2636')
func_2638_call = mutated_mod.get_global_var('func_2638')
call_4703 = relay.TupleGetItem(func_2636_call(), 2)
call_4704 = relay.TupleGetItem(func_2638_call(), 2)
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
call_4710 = relay.TupleGetItem(func_312_call(), 2)
call_4711 = relay.TupleGetItem(func_314_call(), 2)
func_2482_call = mod.get_global_var('func_2482')
func_2484_call = mutated_mod.get_global_var('func_2484')
call_4713 = relay.TupleGetItem(func_2482_call(), 0)
call_4714 = relay.TupleGetItem(func_2484_call(), 0)
func_207_call = mod.get_global_var('func_207')
func_209_call = mutated_mod.get_global_var('func_209')
call_4717 = relay.TupleGetItem(func_207_call(), 0)
call_4718 = relay.TupleGetItem(func_209_call(), 0)
output = relay.Tuple([call_4700,call_4703,call_4710,call_4713,call_4717,])
output2 = relay.Tuple([call_4701,call_4704,call_4711,call_4714,call_4718,])
func_4719 = relay.Function([], output)
mod['func_4719'] = func_4719
mod = relay.transform.InferType()(mod)
output = func_4719()
func_4720 = relay.Function([], output)
mutated_mod['func_4720'] = func_4720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1762_call = mod.get_global_var('func_1762')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_4847 = func_1762_call()
call_4848 = func_1762_call()
func_4559_call = mod.get_global_var('func_4559')
func_4560_call = mutated_mod.get_global_var('func_4560')
call_4853 = relay.TupleGetItem(func_4559_call(), 0)
call_4854 = relay.TupleGetItem(func_4560_call(), 0)
output = relay.Tuple([call_4847,call_4853,])
output2 = relay.Tuple([call_4848,call_4854,])
func_4867 = relay.Function([], output)
mod['func_4867'] = func_4867
mod = relay.transform.InferType()(mod)
mutated_mod['func_4867'] = func_4867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4867_call = mutated_mod.get_global_var('func_4867')
call_4868 = func_4867_call()
output = call_4868
func_4869 = relay.Function([], output)
mutated_mod['func_4869'] = func_4869
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4870 = relay.const([[[-5,-1,4],[1,-2,3],[5,7,-10]],[[-7,-4,-10],[1,9,1],[3,-1,-3]],[[2,10,4],[-5,-3,5],[1,-2,2]],[[-9,5,9],[3,2,-6],[8,-6,-10]],[[-6,-1,9],[2,7,8],[-5,4,-6]],[[6,5,-1],[2,7,-2],[10,5,-4]],[[-5,-6,-2],[4,3,9],[-1,7,4]],[[4,-9,-4],[9,-6,-5],[-1,-9,-5]],[[-3,-8,6],[-4,-2,-2],[-8,2,9]]], dtype = "uint64")#candidate|4870|(9, 3, 3)|const|uint64
var_4871 = relay.var("var_4871", dtype = "uint64", shape = (9, 3, 3))#candidate|4871|(9, 3, 3)|var|uint64
bop_4872 = relay.less(const_4870.astype('bool'), relay.reshape(var_4871.astype('bool'), relay.shape_of(const_4870))) # shape=(9, 3, 3)
var_4875 = relay.var("var_4875", dtype = "uint64", shape = (9, 3, 3))#candidate|4875|(9, 3, 3)|var|uint64
bop_4876 = relay.floor_mod(var_4871.astype('float32'), relay.reshape(var_4875.astype('float32'), relay.shape_of(var_4871))) # shape=(9, 3, 3)
func_4189_call = mod.get_global_var('func_4189')
func_4192_call = mutated_mod.get_global_var('func_4192')
var_4915 = relay.var("var_4915", dtype = "float32", shape = (96,))#candidate|4915|(96,)|var|float32
call_4914 = relay.TupleGetItem(func_4189_call(relay.reshape(var_4915.astype('float32'), [96,])), 0)
call_4916 = relay.TupleGetItem(func_4192_call(relay.reshape(var_4915.astype('float32'), [96,])), 0)
output = relay.Tuple([bop_4872,bop_4876,call_4914,var_4915,])
output2 = relay.Tuple([bop_4872,bop_4876,call_4916,var_4915,])
func_4928 = relay.Function([var_4871,var_4875,var_4915,], output)
mod['func_4928'] = func_4928
mod = relay.transform.InferType()(mod)
var_4929 = relay.var("var_4929", dtype = "uint64", shape = (9, 3, 3))#candidate|4929|(9, 3, 3)|var|uint64
var_4930 = relay.var("var_4930", dtype = "uint64", shape = (9, 3, 3))#candidate|4930|(9, 3, 3)|var|uint64
var_4931 = relay.var("var_4931", dtype = "float32", shape = (96,))#candidate|4931|(96,)|var|float32
output = func_4928(var_4929,var_4930,var_4931,)
func_4932 = relay.Function([var_4929,var_4930,var_4931,], output)
mutated_mod['func_4932'] = func_4932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1545_call = mod.get_global_var('func_1545')
func_1547_call = mutated_mod.get_global_var('func_1547')
call_4957 = func_1545_call()
call_4958 = func_1545_call()
func_3091_call = mod.get_global_var('func_3091')
func_3092_call = mutated_mod.get_global_var('func_3092')
call_4962 = func_3091_call()
call_4963 = func_3091_call()
output = relay.Tuple([call_4957,call_4962,])
output2 = relay.Tuple([call_4958,call_4963,])
func_4968 = relay.Function([], output)
mod['func_4968'] = func_4968
mod = relay.transform.InferType()(mod)
output = func_4968()
func_4969 = relay.Function([], output)
mutated_mod['func_4969'] = func_4969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4022_call = mod.get_global_var('func_4022')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_5011 = relay.TupleGetItem(func_4022_call(), 0)
call_5012 = relay.TupleGetItem(func_4023_call(), 0)
output = relay.Tuple([call_5011,])
output2 = relay.Tuple([call_5012,])
func_5027 = relay.Function([], output)
mod['func_5027'] = func_5027
mod = relay.transform.InferType()(mod)
mutated_mod['func_5027'] = func_5027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5027_call = mutated_mod.get_global_var('func_5027')
call_5028 = func_5027_call()
output = call_5028
func_5029 = relay.Function([], output)
mutated_mod['func_5029'] = func_5029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2636_call = mod.get_global_var('func_2636')
func_2638_call = mutated_mod.get_global_var('func_2638')
call_5047 = relay.TupleGetItem(func_2636_call(), 1)
call_5048 = relay.TupleGetItem(func_2638_call(), 1)
output = relay.Tuple([call_5047,])
output2 = relay.Tuple([call_5048,])
func_5057 = relay.Function([], output)
mod['func_5057'] = func_5057
mod = relay.transform.InferType()(mod)
output = func_5057()
func_5058 = relay.Function([], output)
mutated_mod['func_5058'] = func_5058
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5086 = relay.var("var_5086", dtype = "float32", shape = (13, 6, 12))#candidate|5086|(13, 6, 12)|var|float32
uop_5087 = relay.log10(var_5086.astype('float32')) # shape=(13, 6, 12)
uop_5091 = relay.rsqrt(uop_5087.astype('float64')) # shape=(13, 6, 12)
output = uop_5091
output2 = uop_5091
func_5094 = relay.Function([var_5086,], output)
mod['func_5094'] = func_5094
mod = relay.transform.InferType()(mod)
var_5095 = relay.var("var_5095", dtype = "float32", shape = (13, 6, 12))#candidate|5095|(13, 6, 12)|var|float32
output = func_5094(var_5095)
func_5096 = relay.Function([var_5095], output)
mutated_mod['func_5096'] = func_5096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_5129 = relay.TupleGetItem(func_928_call(), 0)
call_5130 = relay.TupleGetItem(func_930_call(), 0)
func_4928_call = mod.get_global_var('func_4928')
func_4932_call = mutated_mod.get_global_var('func_4932')
var_5140 = relay.var("var_5140", dtype = "uint64", shape = (81,))#candidate|5140|(81,)|var|uint64
var_5141 = relay.var("var_5141", dtype = "float32", shape = (96,))#candidate|5141|(96,)|var|float32
call_5139 = relay.TupleGetItem(func_4928_call(relay.reshape(var_5140.astype('uint64'), [9, 3, 3]), relay.reshape(var_5140.astype('uint64'), [9, 3, 3]), relay.reshape(var_5141.astype('float32'), [96,]), ), 1)
call_5142 = relay.TupleGetItem(func_4932_call(relay.reshape(var_5140.astype('uint64'), [9, 3, 3]), relay.reshape(var_5140.astype('uint64'), [9, 3, 3]), relay.reshape(var_5141.astype('float32'), [96,]), ), 1)
func_4231_call = mod.get_global_var('func_4231')
func_4234_call = mutated_mod.get_global_var('func_4234')
var_5155 = relay.var("var_5155", dtype = "float32", shape = (1001, 1))#candidate|5155|(1001, 1)|var|float32
call_5154 = relay.TupleGetItem(func_4231_call(relay.reshape(var_5155.astype('float32'), [11, 7, 13])), 0)
call_5156 = relay.TupleGetItem(func_4234_call(relay.reshape(var_5155.astype('float32'), [11, 7, 13])), 0)
bop_5157 = relay.equal(call_5154.astype('bool'), relay.reshape(var_5155.astype('bool'), relay.shape_of(call_5154))) # shape=(11, 7, 13)
bop_5160 = relay.equal(call_5156.astype('bool'), relay.reshape(var_5155.astype('bool'), relay.shape_of(call_5156))) # shape=(11, 7, 13)
bop_5164 = relay.bitwise_xor(var_5141.astype('int32'), var_5155.astype('int32')) # shape=(1001, 96)
func_3002_call = mod.get_global_var('func_3002')
func_3004_call = mutated_mod.get_global_var('func_3004')
call_5168 = func_3002_call(relay.reshape(call_5129.astype('uint64'), [10, 11, 8]))
call_5169 = func_3002_call(relay.reshape(call_5129.astype('uint64'), [10, 11, 8]))
uop_5178 = relay.acosh(var_5140.astype('float32')) # shape=(81,)
var_5180 = relay.var("var_5180", dtype = "float32", shape = (81,))#candidate|5180|(81,)|var|float32
bop_5181 = relay.floor_divide(uop_5178.astype('float32'), relay.reshape(var_5180.astype('float32'), relay.shape_of(uop_5178))) # shape=(81,)
uop_5191 = relay.erf(uop_5178.astype('float32')) # shape=(81,)
output = relay.Tuple([call_5129,call_5139,bop_5157,bop_5164,call_5168,bop_5181,uop_5191,])
output2 = relay.Tuple([call_5130,call_5142,bop_5160,bop_5164,call_5169,bop_5181,uop_5191,])
func_5197 = relay.Function([var_5140,var_5141,var_5155,var_5180,], output)
mod['func_5197'] = func_5197
mod = relay.transform.InferType()(mod)
var_5198 = relay.var("var_5198", dtype = "uint64", shape = (81,))#candidate|5198|(81,)|var|uint64
var_5199 = relay.var("var_5199", dtype = "float32", shape = (96,))#candidate|5199|(96,)|var|float32
var_5200 = relay.var("var_5200", dtype = "float32", shape = (1001, 1))#candidate|5200|(1001, 1)|var|float32
var_5201 = relay.var("var_5201", dtype = "float32", shape = (81,))#candidate|5201|(81,)|var|float32
output = func_5197(var_5198,var_5199,var_5200,var_5201,)
func_5202 = relay.Function([var_5198,var_5199,var_5200,var_5201,], output)
mutated_mod['func_5202'] = func_5202
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5210 = relay.var("var_5210", dtype = "float32", shape = (1, 10, 15))#candidate|5210|(1, 10, 15)|var|float32
uop_5211 = relay.sin(var_5210.astype('float32')) # shape=(1, 10, 15)
bop_5216 = relay.greater_equal(var_5210.astype('bool'), relay.reshape(uop_5211.astype('bool'), relay.shape_of(var_5210))) # shape=(1, 10, 15)
uop_5219 = relay.atanh(uop_5211.astype('float32')) # shape=(1, 10, 15)
var_5223 = relay.var("var_5223", dtype = "bool", shape = (10, 10, 15))#candidate|5223|(10, 10, 15)|var|bool
bop_5224 = relay.power(bop_5216.astype('float64'), var_5223.astype('float64')) # shape=(10, 10, 15)
output = relay.Tuple([uop_5219,bop_5224,])
output2 = relay.Tuple([uop_5219,bop_5224,])
func_5238 = relay.Function([var_5210,var_5223,], output)
mod['func_5238'] = func_5238
mod = relay.transform.InferType()(mod)
mutated_mod['func_5238'] = func_5238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5238_call = mutated_mod.get_global_var('func_5238')
var_5240 = relay.var("var_5240", dtype = "float32", shape = (1, 10, 15))#candidate|5240|(1, 10, 15)|var|float32
var_5241 = relay.var("var_5241", dtype = "bool", shape = (10, 10, 15))#candidate|5241|(10, 10, 15)|var|bool
call_5239 = func_5238_call(var_5240,var_5241,)
output = call_5239
func_5242 = relay.Function([var_5240,var_5241,], output)
mutated_mod['func_5242'] = func_5242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2655_call = mod.get_global_var('func_2655')
func_2657_call = mutated_mod.get_global_var('func_2657')
call_5288 = func_2655_call()
call_5289 = func_2655_call()
output = relay.Tuple([call_5288,])
output2 = relay.Tuple([call_5289,])
func_5290 = relay.Function([], output)
mod['func_5290'] = func_5290
mod = relay.transform.InferType()(mod)
mutated_mod['func_5290'] = func_5290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5290_call = mutated_mod.get_global_var('func_5290')
call_5291 = func_5290_call()
output = call_5291
func_5292 = relay.Function([], output)
mutated_mod['func_5292'] = func_5292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
call_5298 = func_1152_call()
call_5299 = func_1152_call()
output = relay.Tuple([call_5298,])
output2 = relay.Tuple([call_5299,])
func_5321 = relay.Function([], output)
mod['func_5321'] = func_5321
mod = relay.transform.InferType()(mod)
mutated_mod['func_5321'] = func_5321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5321_call = mutated_mod.get_global_var('func_5321')
call_5322 = func_5321_call()
output = call_5322
func_5323 = relay.Function([], output)
mutated_mod['func_5323'] = func_5323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5321_call = mod.get_global_var('func_5321')
func_5323_call = mutated_mod.get_global_var('func_5323')
call_5337 = relay.TupleGetItem(func_5321_call(), 0)
call_5338 = relay.TupleGetItem(func_5323_call(), 0)
output = relay.Tuple([call_5337,])
output2 = relay.Tuple([call_5338,])
func_5343 = relay.Function([], output)
mod['func_5343'] = func_5343
mod = relay.transform.InferType()(mod)
mutated_mod['func_5343'] = func_5343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mutated_mod.get_global_var('func_5343')
call_5344 = func_5343_call()
output = call_5344
func_5345 = relay.Function([], output)
mutated_mod['func_5345'] = func_5345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mod.get_global_var('func_1021')
func_1022_call = mutated_mod.get_global_var('func_1022')
call_5361 = func_1021_call()
call_5362 = func_1021_call()
uop_5393 = relay.sqrt(call_5361.astype('float64')) # shape=(10, 11, 8)
uop_5395 = relay.sqrt(call_5362.astype('float64')) # shape=(10, 11, 8)
func_1021_call = mod.get_global_var('func_1021')
func_1022_call = mutated_mod.get_global_var('func_1022')
call_5408 = func_1021_call()
call_5409 = func_1021_call()
func_480_call = mod.get_global_var('func_480')
func_483_call = mutated_mod.get_global_var('func_483')
const_5414 = relay.const([-5.987184,2.423067,7.602114,-6.373031,-2.337509,7.585097,5.606954,7.725240,-9.617106,-5.784706,-4.323888,6.414464,4.264068,2.284488,6.196812,4.337609,-8.486429,3.166593,6.676829,9.456351,-4.924522,4.863728,-0.030441,-0.093656,-8.479267,8.672653,-1.622504,-0.233661,-8.030204,-2.939155,4.468448,4.095002,-8.124616,4.676809,0.693398,4.158195,9.702349,3.961236,1.899203,-1.803173,9.010904,-0.285270,1.860906,2.514429,-1.304115,3.746560,1.538067,-6.177206,-8.290177,4.495119,-7.410246,2.314462,-8.132421,9.087613,-2.905595,8.482857,9.636970,-6.427924,-6.263203,7.513157,0.433982,-6.044661,8.100956,2.639013,-7.764819,1.098832,2.761552,-3.612556,-9.534580,-3.377123,1.295458,-0.552817,3.259784,7.779968,-6.044291,7.594416,-1.269447,-1.708220,-0.091606,3.821307,-0.729542,1.794762,3.431298,6.754617,4.937537,8.013975,9.418485,-1.544548,-8.942577,-0.355990,-4.790377,-6.576342,9.739741,-7.489428,-4.807336,-2.137479,2.653855,3.375895,6.259109,-4.988609,-1.160077,-3.059804,8.887480,-0.051080,-4.556927,-4.027759,-1.958971,1.982696,1.935096,5.420957,2.734587,-2.112043,8.685620,-0.425551,0.027188,-3.598958,-6.236609,5.484273,2.220178,9.508738,5.541876,-8.454534,-4.474232,6.769319,2.738716,-0.037377,1.112580,1.809529,-3.081004,4.880420,-9.960021,8.451082,-9.000967,-6.574346,-5.042566,-1.958176,1.858745,-3.640635,-1.685329,1.475533,-0.069985,0.898877,4.106009,7.154032,-4.137557,1.430775,-7.917823,5.607625,3.118940,-7.547145,9.795650,9.704768,5.971745,-9.436485,-9.445760,9.219592,9.026724,-5.179329,-1.087410,-6.628235,-4.811062,8.481010,-0.059244,-1.094979,9.069631,-6.271701,0.718556,9.926411,4.217216,-9.173813,-3.096526,-5.386872,-2.767073,-5.297169,-3.571922,3.689149,-9.930265,8.287441,9.432736,-4.986965,-3.240003,7.056397,6.291577,-1.959941,0.864279,-6.171736,9.605951,0.567970,6.252981,-3.508474,6.764961,-4.382804,-5.618021,-2.792522,0.732438,-5.642814,1.825164,7.359260,4.546355,3.761255,5.987350,-9.609304,3.330485,-7.621778,3.665049,-5.709888,8.766272,-7.939201,3.433502,3.820150,1.462285,-7.507647,-3.537607,9.978800,-3.833305,-3.677672,-9.431482,-2.606979,-3.050531,-8.159831,6.826976,-8.360573,-2.170419,-9.627910,-6.615131,-7.912483,-0.345055,-1.053993,8.198618,-1.502664,9.317599,1.756282,3.915750,6.505597,-5.489230,0.751456,-4.911617,-3.349132,-3.347162,-1.820687,3.446075,-0.039757,-6.774579,-7.936400,3.150685,0.749473,0.142916,-1.435681,-2.755673,-4.002185,-4.354950,-0.259412,-8.783263,3.319297,7.203424,6.763625,-7.024676,-4.213365,-0.311873,-7.229754,3.907258,-7.214690,-7.052408,1.821745,-2.322897,-6.649969,8.473801,-8.627328,8.341197,-1.456955,7.785116,9.344907,-5.691145,-9.800708,-1.476673,-4.088309,-5.477081,-5.643371,3.860315,1.396878,-4.006290,-3.444274,-9.999935,5.346761,-1.048084,8.826322,8.826305,-1.839536,-6.638487,-5.977155,4.887552,9.991646,-4.478986,2.638936,4.811826,9.696240,-7.736252,-7.278173,-2.275029,-7.633692,6.650446,1.878765,9.137444,-4.038897,-9.932910,-9.144402,2.036395,-4.908883,-6.390141,-5.008324,-7.252220,4.580734,2.004284,-7.883104,3.659136,0.256118,-9.605946,2.899299,-2.038191,5.543463,-3.389930,-5.106502,2.365379,6.499607,-9.493378,-8.697316,-7.627711,2.368463,2.136713,3.154228,8.926895,7.684987,6.018969,5.622453,2.473443,4.763559,-4.457400,3.900604,-3.184247,8.203213,-9.356632,1.140280,0.801703,9.907896,-5.022153,2.711934,3.736063,6.725898,8.563045,-9.817989,-9.685833,0.290059,1.517628,-8.075647,8.329192,1.638042,0.548938,-1.381869,6.895097,3.812156,5.716747,0.200691,-9.851023,3.236337,9.345082,-1.689427,1.603824,0.956078,-7.790966,-2.828153,9.203181,-1.901434,6.207244,-5.096839,-9.876051,-2.171724,-8.837031,-5.938876,9.198976,8.554001,6.026294,-6.768232,2.164172,7.408561,0.770608,2.842519,8.304089,-6.118646,5.254011,-0.553556,-8.249150,3.232804,-1.946902,9.351699,8.695791,1.231935,-1.195254,-2.654657,9.856644,-4.113341,3.372684,0.900997,3.503962,1.672961,-0.852725,-1.175008,3.043382,-9.359626,6.959269,3.756215,-2.599237,9.721917,-4.620235,-9.687664,8.533572,-2.921258,-7.473166,-7.954039,2.335500,-2.102148,2.716931,6.007575,-6.649597,-6.969675,8.640409,6.748985,-4.130340,3.539787,-6.600697,-1.499830,-1.722069,-9.773731,3.815433,-8.052756,0.650474,-2.046267,0.512180,2.907816,0.569050,7.137035,5.505389,-2.477539,2.698541,-8.004115,1.002587,5.738176,9.226032,1.330092,-8.996595,-7.824011,-5.113736,-8.392986,-4.437357,-8.935293,-0.960915,-6.182284,-2.285135,1.352197,-8.891418,2.511176,8.690031,2.388171], dtype = "float64")#candidate|5414|(462,)|const|float64
call_5413 = relay.TupleGetItem(func_480_call(relay.reshape(const_5414.astype('float64'), [11, 3, 14])), 0)
call_5415 = relay.TupleGetItem(func_483_call(relay.reshape(const_5414.astype('float64'), [11, 3, 14])), 0)
output = relay.Tuple([uop_5393,call_5408,call_5413,const_5414,])
output2 = relay.Tuple([uop_5395,call_5409,call_5415,const_5414,])
func_5426 = relay.Function([], output)
mod['func_5426'] = func_5426
mod = relay.transform.InferType()(mod)
mutated_mod['func_5426'] = func_5426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5426_call = mutated_mod.get_global_var('func_5426')
call_5427 = func_5426_call()
output = call_5427
func_5428 = relay.Function([], output)
mutated_mod['func_5428'] = func_5428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5446 = relay.var("var_5446", dtype = "float32", shape = (16, 7, 15))#candidate|5446|(16, 7, 15)|var|float32
uop_5447 = relay.acosh(var_5446.astype('float32')) # shape=(16, 7, 15)
output = relay.Tuple([uop_5447,])
output2 = relay.Tuple([uop_5447,])
func_5465 = relay.Function([var_5446,], output)
mod['func_5465'] = func_5465
mod = relay.transform.InferType()(mod)
mutated_mod['func_5465'] = func_5465
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5466 = relay.var("var_5466", dtype = "float32", shape = (16, 7, 15))#candidate|5466|(16, 7, 15)|var|float32
func_5465_call = mutated_mod.get_global_var('func_5465')
call_5467 = func_5465_call(var_5466)
output = call_5467
func_5468 = relay.Function([var_5466], output)
mutated_mod['func_5468'] = func_5468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4867_call = mod.get_global_var('func_4867')
func_4869_call = mutated_mod.get_global_var('func_4869')
call_5510 = relay.TupleGetItem(func_4867_call(), 1)
call_5511 = relay.TupleGetItem(func_4869_call(), 1)
func_4093_call = mod.get_global_var('func_4093')
func_4094_call = mutated_mod.get_global_var('func_4094')
call_5526 = relay.TupleGetItem(func_4093_call(), 1)
call_5527 = relay.TupleGetItem(func_4094_call(), 1)
func_1134_call = mod.get_global_var('func_1134')
func_1136_call = mutated_mod.get_global_var('func_1136')
call_5530 = relay.TupleGetItem(func_1134_call(), 1)
call_5531 = relay.TupleGetItem(func_1136_call(), 1)
var_5558 = relay.var("var_5558", dtype = "float32", shape = (10, 11, 8))#candidate|5558|(10, 11, 8)|var|float32
bop_5559 = relay.minimum(call_5526.astype('float32'), relay.reshape(var_5558.astype('float32'), relay.shape_of(call_5526))) # shape=(10, 11, 8)
bop_5562 = relay.minimum(call_5527.astype('float32'), relay.reshape(var_5558.astype('float32'), relay.shape_of(call_5527))) # shape=(10, 11, 8)
output = relay.Tuple([call_5510,call_5530,bop_5559,])
output2 = relay.Tuple([call_5511,call_5531,bop_5562,])
func_5565 = relay.Function([var_5558,], output)
mod['func_5565'] = func_5565
mod = relay.transform.InferType()(mod)
mutated_mod['func_5565'] = func_5565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5566 = relay.var("var_5566", dtype = "float32", shape = (10, 11, 8))#candidate|5566|(10, 11, 8)|var|float32
func_5565_call = mutated_mod.get_global_var('func_5565')
call_5567 = func_5565_call(var_5566)
output = call_5567
func_5568 = relay.Function([var_5566], output)
mutated_mod['func_5568'] = func_5568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4022_call = mod.get_global_var('func_4022')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_5573 = relay.TupleGetItem(func_4022_call(), 0)
call_5574 = relay.TupleGetItem(func_4023_call(), 0)
output = relay.Tuple([call_5573,])
output2 = relay.Tuple([call_5574,])
func_5575 = relay.Function([], output)
mod['func_5575'] = func_5575
mod = relay.transform.InferType()(mod)
mutated_mod['func_5575'] = func_5575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5575_call = mutated_mod.get_global_var('func_5575')
call_5576 = func_5575_call()
output = call_5576
func_5577 = relay.Function([], output)
mutated_mod['func_5577'] = func_5577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5321_call = mod.get_global_var('func_5321')
func_5323_call = mutated_mod.get_global_var('func_5323')
call_5615 = relay.TupleGetItem(func_5321_call(), 0)
call_5616 = relay.TupleGetItem(func_5323_call(), 0)
output = call_5615
output2 = call_5616
func_5617 = relay.Function([], output)
mod['func_5617'] = func_5617
mod = relay.transform.InferType()(mod)
output = func_5617()
func_5618 = relay.Function([], output)
mutated_mod['func_5618'] = func_5618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_5630 = func_2294_call()
call_5631 = func_2294_call()
output = relay.Tuple([call_5630,])
output2 = relay.Tuple([call_5631,])
func_5639 = relay.Function([], output)
mod['func_5639'] = func_5639
mod = relay.transform.InferType()(mod)
output = func_5639()
func_5640 = relay.Function([], output)
mutated_mod['func_5640'] = func_5640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4559_call = mod.get_global_var('func_4559')
func_4560_call = mutated_mod.get_global_var('func_4560')
call_5674 = relay.TupleGetItem(func_4559_call(), 0)
call_5675 = relay.TupleGetItem(func_4560_call(), 0)
output = relay.Tuple([call_5674,])
output2 = relay.Tuple([call_5675,])
func_5679 = relay.Function([], output)
mod['func_5679'] = func_5679
mod = relay.transform.InferType()(mod)
output = func_5679()
func_5680 = relay.Function([], output)
mutated_mod['func_5680'] = func_5680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3638_call = mod.get_global_var('func_3638')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_5692 = relay.TupleGetItem(func_3638_call(), 0)
call_5693 = relay.TupleGetItem(func_3639_call(), 0)
func_1648_call = mod.get_global_var('func_1648')
func_1651_call = mutated_mod.get_global_var('func_1651')
call_5694 = relay.TupleGetItem(func_1648_call(relay.reshape(call_5692.astype('float32'), [10, 11, 8])), 0)
call_5695 = relay.TupleGetItem(func_1651_call(relay.reshape(call_5692.astype('float32'), [10, 11, 8])), 0)
output = relay.Tuple([call_5692,call_5694,])
output2 = relay.Tuple([call_5693,call_5695,])
func_5705 = relay.Function([], output)
mod['func_5705'] = func_5705
mod = relay.transform.InferType()(mod)
mutated_mod['func_5705'] = func_5705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5705_call = mutated_mod.get_global_var('func_5705')
call_5706 = func_5705_call()
output = call_5706
func_5707 = relay.Function([], output)
mutated_mod['func_5707'] = func_5707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1572_call = mod.get_global_var('func_1572')
func_1574_call = mutated_mod.get_global_var('func_1574')
call_5708 = relay.TupleGetItem(func_1572_call(), 0)
call_5709 = relay.TupleGetItem(func_1574_call(), 0)
output = call_5708
output2 = call_5709
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
const_5740 = relay.const([[[4,-2,-1,9,-9,5,-10,-5,4,9,7,7],[-5,4,-9,-5,8,-6,-2,5,1,-7,-2,1],[4,-7,-7,-2,-7,2,7,-2,5,-3,4,6],[9,-6,8,8,9,-5,-2,-9,-5,4,8,-8],[6,10,1,-3,1,-1,9,3,5,-4,-4,5],[-4,5,6,7,-5,2,-4,8,8,-6,-1,3]],[[-6,-4,-10,2,-1,-9,8,-1,-2,-3,-9,4],[2,-4,-9,-10,6,5,-6,-1,4,4,-6,7],[9,6,10,-7,2,-7,8,5,-3,9,9,-6],[2,5,6,-7,3,-5,5,-7,-3,7,-2,-7],[-7,4,-8,9,10,-7,-9,3,10,-6,2,-2],[-6,8,3,2,-2,6,-5,-10,-8,-5,-3,-8]],[[8,6,7,-7,-8,10,-10,1,-9,2,1,-2],[10,5,-6,6,7,4,-1,7,-5,1,1,5],[-9,7,2,-9,5,-8,9,4,8,-9,8,8],[-5,9,1,8,-3,-1,4,-9,-4,-9,3,-10],[-3,9,7,5,6,-9,-9,10,4,9,1,-7],[7,9,-1,-2,-8,-8,-8,-6,-8,-3,2,9]],[[3,3,7,9,8,-5,-7,-5,-6,7,-5,-10],[7,-10,-7,4,6,-3,7,-9,2,-8,-1,-3],[6,-2,-4,-6,6,-8,4,2,-9,-4,-1,-5],[-7,3,4,6,7,-2,10,9,-1,-8,1,6],[-7,8,3,2,-4,7,-2,-9,1,-9,7,-9],[-7,5,7,7,10,-3,-9,-5,3,-5,7,5]],[[5,-10,-3,3,6,-7,-7,-8,-2,-4,-9,5],[10,-6,-4,-6,-4,-3,5,-9,4,-3,-2,10],[3,4,2,3,-1,-9,-9,-6,-3,-4,-5,-9],[-6,-9,-5,-2,-4,2,8,-8,-4,8,3,-10],[2,-5,4,-7,-8,1,-7,6,9,-9,-3,10],[3,-3,-1,-3,7,-2,-1,3,5,-5,-7,6]],[[-8,7,-2,-9,4,-3,6,-7,-1,-6,-10,-2],[-3,9,-7,-9,10,6,-2,8,6,-10,5,-7],[-8,1,-2,-3,1,6,-9,-2,-9,-2,3,7],[-9,-4,-4,-5,2,2,-10,-8,9,10,8,-6],[10,10,-5,-5,-3,3,9,-2,5,-6,9,5],[-7,5,-8,-2,8,-4,-8,9,7,9,-1,9]],[[-4,-8,-7,8,-1,9,3,-8,5,4,-10,-5],[9,2,-4,4,4,-9,-9,6,2,-7,-1,4],[6,7,4,-2,-5,-1,-5,-7,8,-1,6,9],[7,1,-3,-1,-6,7,-2,3,5,-8,-10,1],[-4,-9,2,-8,-3,6,-5,-5,9,1,2,3],[-9,-8,-10,10,-3,-4,-4,5,-3,-3,2,-9]],[[1,4,-5,1,-8,6,-9,-1,5,7,-10,-9],[3,-9,-2,-6,2,8,-7,-3,9,-2,-6,-9],[8,2,-8,9,3,-8,10,-9,4,-10,-6,5],[-4,4,-7,3,-10,-3,6,-2,2,5,4,4],[1,6,-7,-1,-7,3,9,-9,-2,7,-6,10],[-1,-2,9,10,10,-7,8,-1,2,-8,1,10]],[[-2,3,8,-10,8,-1,-9,-7,8,7,-2,10],[2,7,-7,-7,3,-1,-3,1,4,-8,-4,2],[-9,-9,-9,6,-9,7,9,-7,3,-5,-8,8],[8,-4,1,6,9,10,6,-1,9,3,1,-2],[1,-1,-4,2,2,-6,-4,-2,8,2,10,-1],[1,-6,-7,7,6,6,4,3,3,-9,-2,3]],[[5,-3,9,5,-7,2,-1,-1,-6,8,4,6],[-3,-8,7,4,-7,8,-3,5,4,-6,-8,-2],[4,4,5,9,4,4,1,3,7,3,2,9],[-9,1,-4,2,6,9,-4,9,8,-9,-1,4],[-4,7,-6,4,-5,-3,-9,-6,10,6,4,4],[-9,8,7,-10,-10,9,-5,-3,9,9,2,-4]],[[-1,-8,6,-6,7,6,7,-7,5,6,10,-10],[7,6,7,2,2,2,2,-4,-3,4,-8,-8],[8,3,-3,-6,4,-10,4,10,9,-4,1,1],[10,-3,-6,-3,5,2,-1,-8,2,8,7,-4],[10,-9,-7,5,6,8,-9,6,-9,1,9,-6],[7,-9,-4,3,10,-4,-4,4,7,2,5,1]],[[6,-5,-3,-6,-7,-7,7,-4,1,3,9,5],[-3,5,5,-3,9,-6,1,3,8,-10,9,3],[3,7,-5,-1,9,8,3,-5,-1,5,4,1],[-9,8,-4,7,-8,3,-9,4,2,2,-3,-8],[-9,-8,2,-6,10,-8,-4,6,-1,7,-5,8],[1,3,-6,-2,-5,-7,-10,7,-6,4,9,-3]],[[-9,8,9,1,5,-8,6,-5,8,9,4,6],[10,9,-2,-10,1,4,6,-2,1,4,-7,2],[1,-3,-9,3,1,-9,-4,-3,-8,5,-4,7],[-6,-7,-9,10,2,3,2,-9,9,7,8,8],[-7,-4,-1,-8,-1,2,6,8,-5,7,8,-2],[5,-10,-9,3,-1,-9,-7,1,-4,7,-5,5]],[[-7,-7,8,4,1,8,-2,10,-7,6,-7,-9],[-10,-10,3,-2,10,7,-3,3,5,-5,-2,10],[3,-3,-3,-3,1,7,-1,-4,10,-8,2,-6],[3,-6,8,4,4,-4,-10,-9,10,-4,-4,-1],[10,9,9,1,-9,-6,-4,8,8,4,-9,-8],[10,-10,-8,3,8,-2,-7,8,-1,-5,-7,-3]],[[-7,2,2,4,1,10,-3,-9,-3,8,3,10],[-2,-9,1,1,-8,3,4,4,9,7,7,3],[-7,1,-8,-6,-7,-7,-4,6,5,2,5,5],[9,8,-7,5,-1,-6,9,-9,-4,7,-9,9],[-2,-1,8,3,-7,-3,-1,10,7,10,9,-6],[-6,-2,6,8,4,-7,7,-10,-2,-1,-3,4]]], dtype = "int64")#candidate|5740|(15, 6, 12)|const|int64
const_5741 = relay.const([[[-5,9,5,10,6,-6,-3,2,2,-9,-4,5],[-4,-8,-1,-6,-7,-2,-10,-2,8,-3,-2,-6],[8,7,-10,-8,1,-3,-6,1,-5,8,7,10],[-7,-8,-8,3,-10,10,5,6,-5,-10,-7,-6],[4,-8,1,6,-2,9,1,-8,4,-2,-7,7],[-5,-4,-10,7,-4,6,-4,5,9,6,6,2]],[[3,1,2,3,-8,2,-9,3,5,-9,2,-2],[8,2,3,5,9,9,7,1,-1,3,-3,1],[4,4,6,8,6,-9,5,9,2,-5,10,-2],[8,-10,2,8,3,-3,-2,4,-10,-8,-7,-8],[5,-5,9,7,-5,-8,-8,2,-2,10,-5,-1],[7,9,-6,-2,10,7,9,7,-1,-2,5,8]],[[-10,-9,-5,9,10,8,6,-9,9,6,-2,-3],[-9,-9,8,2,-8,-2,-1,-4,10,-9,2,-3],[-5,-1,3,9,-9,-6,6,7,-9,6,10,1],[2,8,-9,4,-1,1,1,4,8,8,-8,-9],[-4,6,-5,-7,8,-10,6,3,3,9,-5,5],[-5,-9,-10,1,-3,9,6,4,1,3,2,-7]],[[1,6,-1,1,-5,-10,-9,8,-7,-10,5,7],[10,5,7,6,10,-5,-4,-8,7,4,10,-7],[-9,10,-3,-1,-10,-6,10,4,-3,-2,7,3],[-9,-1,-9,6,5,3,6,2,2,-2,7,4],[-6,6,8,9,-6,-6,1,4,-1,-6,1,-2],[6,-7,9,5,-8,1,10,-3,4,-3,3,-1]],[[-4,-1,6,10,-5,-9,8,2,-4,-10,-6,-3],[2,3,5,10,-4,-6,4,4,-3,-6,6,-7],[-2,5,9,6,3,-9,-7,8,9,4,10,-5],[-3,-5,10,1,8,9,1,-3,7,3,-10,-7],[-4,4,-1,8,9,-4,5,8,1,-3,5,7],[5,-7,-10,5,7,8,6,1,1,-4,-1,10]],[[-2,-4,-6,-8,-2,7,1,-8,1,6,3,-5],[-5,9,-3,-9,1,-1,-8,-9,6,-6,9,-5],[9,-10,-1,7,3,-5,6,-3,-1,5,5,-2],[1,8,-2,-2,6,-3,6,4,-5,-8,-5,7],[3,-5,-7,9,-5,-10,2,5,-4,5,-8,9],[-8,-6,6,-8,7,-9,-10,-2,7,-9,-4,7]],[[5,-7,-10,8,-3,-2,-10,-2,-6,3,1,-9],[9,-7,4,-2,5,4,8,-7,8,2,2,7],[6,3,7,-8,-2,1,1,7,-3,-3,-2,-3],[-2,8,-2,-3,7,6,10,10,8,-7,5,5],[2,-10,-2,5,-2,9,8,-10,10,6,-1,1],[10,-8,-2,4,5,-10,-8,1,8,4,4,8]],[[4,-3,2,4,-1,-8,7,1,-5,1,6,7],[-1,-7,-7,-10,-10,-5,8,6,-2,-4,-6,5],[6,7,5,5,5,3,-8,2,-8,2,-6,7],[3,-1,6,10,-9,5,1,3,3,-7,-1,-1],[-7,6,1,3,5,-5,-9,5,4,-5,-4,-2],[-6,-10,-1,7,5,-1,-7,2,-10,4,-4,9]],[[-1,-6,3,-3,-8,-6,-3,-6,6,-5,-4,4],[-8,5,-7,1,-9,2,6,10,8,2,9,-2],[-5,-8,7,-5,8,6,-4,-3,5,-6,-3,-4],[4,-6,4,-10,6,10,-1,8,-4,-7,3,-1],[7,1,6,5,-1,-3,-1,-4,2,-2,-8,2],[-5,10,9,8,1,-10,-3,6,-5,9,-3,-5]],[[-4,8,7,3,1,2,5,7,-7,2,3,-6],[-9,6,-7,-7,-8,-2,-8,-7,-8,-10,6,8],[6,7,-10,-10,9,10,-7,-6,3,7,5,-2],[-2,-4,10,6,-4,5,-8,-2,1,5,-9,10],[-1,5,3,-8,8,5,-6,5,-6,5,-5,2],[-10,-3,-10,-3,2,-6,5,-3,-6,2,1,-3]],[[8,-2,-8,1,1,-7,7,-1,-9,-5,1,-9],[6,10,-1,-6,-4,3,3,9,8,-7,7,-5],[7,3,9,6,5,5,-10,6,9,5,5,-6],[-10,-9,2,-3,5,-6,8,-2,-9,-1,-9,-4],[-10,10,3,-2,10,-9,-7,-1,8,9,-1,-1],[1,1,2,-8,-4,-10,4,-1,-3,-7,3,-5]],[[5,-9,6,-7,3,-6,-3,7,-3,-8,1,3],[10,-4,-10,-5,2,1,3,6,-8,-1,7,2],[-9,8,10,1,3,-4,-6,-10,-1,8,-9,-10],[-7,9,2,-3,-10,8,6,9,-9,-4,1,5],[3,8,8,-10,-10,8,-10,3,-3,1,4,-1],[-4,8,-9,7,-6,5,-2,6,7,6,-6,7]],[[-1,1,10,-8,6,-8,-7,-6,-10,5,-9,-4],[9,-4,-8,-4,-1,4,-8,-6,6,-9,10,8],[-6,2,7,2,5,-9,-6,3,2,1,-10,2],[2,1,-7,-4,3,10,1,4,-9,8,-9,-5],[8,9,-4,6,-4,-9,-7,8,8,-7,-2,-6],[5,-8,-7,-3,10,3,-7,-9,-7,4,1,3]],[[9,-10,-1,4,10,-10,5,-2,-9,7,5,9],[-4,7,6,-7,-9,8,1,8,1,8,3,-1],[6,-8,-5,4,-1,-5,8,2,8,9,-1,3],[-5,10,-3,-8,-10,-10,5,-4,-5,-1,-2,-2],[4,-2,-8,-9,-5,1,-3,-7,-7,-7,10,-7],[2,-10,3,-7,-3,4,-3,4,-3,6,-4,-8]],[[-9,-3,6,-6,10,-5,7,-1,-10,-4,7,10],[5,-5,-8,-1,-10,8,6,6,-9,10,2,8],[4,2,-4,-1,-10,-9,1,-7,-6,-7,-2,-10],[-4,9,-10,6,3,-5,-2,-5,5,3,5,7],[9,-6,6,2,-4,4,9,10,-9,8,-1,6],[-6,2,-10,-3,-10,10,2,-6,2,-2,9,3]]], dtype = "int64")#candidate|5741|(15, 6, 12)|const|int64
bop_5742 = relay.equal(const_5740.astype('bool'), relay.reshape(const_5741.astype('bool'), relay.shape_of(const_5740))) # shape=(15, 6, 12)
func_5057_call = mod.get_global_var('func_5057')
func_5058_call = mutated_mod.get_global_var('func_5058')
call_5747 = relay.TupleGetItem(func_5057_call(), 0)
call_5748 = relay.TupleGetItem(func_5058_call(), 0)
uop_5751 = relay.log10(call_5747.astype('float32')) # shape=(10, 11, 8)
uop_5753 = relay.log10(call_5748.astype('float32')) # shape=(10, 11, 8)
output = relay.Tuple([bop_5742,uop_5751,])
output2 = relay.Tuple([bop_5742,uop_5753,])
func_5770 = relay.Function([], output)
mod['func_5770'] = func_5770
mod = relay.transform.InferType()(mod)
output = func_5770()
func_5771 = relay.Function([], output)
mutated_mod['func_5771'] = func_5771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_207_call = mod.get_global_var('func_207')
func_209_call = mutated_mod.get_global_var('func_209')
call_5780 = relay.TupleGetItem(func_207_call(), 0)
call_5781 = relay.TupleGetItem(func_209_call(), 0)
func_2004_call = mod.get_global_var('func_2004')
func_2006_call = mutated_mod.get_global_var('func_2006')
call_5791 = relay.TupleGetItem(func_2004_call(), 0)
call_5792 = relay.TupleGetItem(func_2006_call(), 0)
func_3638_call = mod.get_global_var('func_3638')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_5812 = relay.TupleGetItem(func_3638_call(), 1)
call_5813 = relay.TupleGetItem(func_3639_call(), 1)
func_1854_call = mod.get_global_var('func_1854')
func_1856_call = mutated_mod.get_global_var('func_1856')
call_5827 = func_1854_call()
call_5828 = func_1854_call()
output = relay.Tuple([call_5780,call_5791,call_5812,call_5827,])
output2 = relay.Tuple([call_5781,call_5792,call_5813,call_5828,])
func_5833 = relay.Function([], output)
mod['func_5833'] = func_5833
mod = relay.transform.InferType()(mod)
output = func_5833()
func_5834 = relay.Function([], output)
mutated_mod['func_5834'] = func_5834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2568_call = mod.get_global_var('func_2568')
func_2570_call = mutated_mod.get_global_var('func_2570')
call_5853 = relay.TupleGetItem(func_2568_call(), 0)
call_5854 = relay.TupleGetItem(func_2570_call(), 0)
output = call_5853
output2 = call_5854
func_5874 = relay.Function([], output)
mod['func_5874'] = func_5874
mod = relay.transform.InferType()(mod)
output = func_5874()
func_5875 = relay.Function([], output)
mutated_mod['func_5875'] = func_5875
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5897 = relay.var("var_5897", dtype = "float64", shape = (5, 13, 12))#candidate|5897|(5, 13, 12)|var|float64
uop_5898 = relay.sqrt(var_5897.astype('float64')) # shape=(5, 13, 12)
uop_5902 = relay.exp(uop_5898.astype('float32')) # shape=(5, 13, 12)
func_5094_call = mod.get_global_var('func_5094')
func_5096_call = mutated_mod.get_global_var('func_5096')
var_5914 = relay.var("var_5914", dtype = "float32", shape = (936,))#candidate|5914|(936,)|var|float32
call_5913 = func_5094_call(relay.reshape(var_5914.astype('float32'), [13, 6, 12]))
call_5915 = func_5094_call(relay.reshape(var_5914.astype('float32'), [13, 6, 12]))
output = relay.Tuple([uop_5902,call_5913,var_5914,])
output2 = relay.Tuple([uop_5902,call_5915,var_5914,])
func_5939 = relay.Function([var_5897,var_5914,], output)
mod['func_5939'] = func_5939
mod = relay.transform.InferType()(mod)
var_5940 = relay.var("var_5940", dtype = "float64", shape = (5, 13, 12))#candidate|5940|(5, 13, 12)|var|float64
var_5941 = relay.var("var_5941", dtype = "float32", shape = (936,))#candidate|5941|(936,)|var|float32
output = func_5939(var_5940,var_5941,)
func_5942 = relay.Function([var_5940,var_5941,], output)
mutated_mod['func_5942'] = func_5942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2945_call = mod.get_global_var('func_2945')
func_2947_call = mutated_mod.get_global_var('func_2947')
call_5947 = relay.TupleGetItem(func_2945_call(), 0)
call_5948 = relay.TupleGetItem(func_2947_call(), 0)
func_5426_call = mod.get_global_var('func_5426')
func_5428_call = mutated_mod.get_global_var('func_5428')
call_5951 = relay.TupleGetItem(func_5426_call(), 3)
call_5952 = relay.TupleGetItem(func_5428_call(), 3)
output = relay.Tuple([call_5947,call_5951,])
output2 = relay.Tuple([call_5948,call_5952,])
func_6022 = relay.Function([], output)
mod['func_6022'] = func_6022
mod = relay.transform.InferType()(mod)
output = func_6022()
func_6023 = relay.Function([], output)
mutated_mod['func_6023'] = func_6023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4559_call = mod.get_global_var('func_4559')
func_4560_call = mutated_mod.get_global_var('func_4560')
call_6032 = relay.TupleGetItem(func_4559_call(), 0)
call_6033 = relay.TupleGetItem(func_4560_call(), 0)
func_3761_call = mod.get_global_var('func_3761')
func_3762_call = mutated_mod.get_global_var('func_3762')
call_6047 = relay.TupleGetItem(func_3761_call(), 0)
call_6048 = relay.TupleGetItem(func_3762_call(), 0)
output = relay.Tuple([call_6032,call_6047,])
output2 = relay.Tuple([call_6033,call_6048,])
func_6072 = relay.Function([], output)
mod['func_6072'] = func_6072
mod = relay.transform.InferType()(mod)
output = func_6072()
func_6073 = relay.Function([], output)
mutated_mod['func_6073'] = func_6073
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6101 = relay.var("var_6101", dtype = "float32", shape = (7, 8, 1))#candidate|6101|(7, 8, 1)|var|float32
uop_6102 = relay.erf(var_6101.astype('float32')) # shape=(7, 8, 1)
output = relay.Tuple([uop_6102,])
output2 = relay.Tuple([uop_6102,])
func_6108 = relay.Function([var_6101,], output)
mod['func_6108'] = func_6108
mod = relay.transform.InferType()(mod)
mutated_mod['func_6108'] = func_6108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6109 = relay.var("var_6109", dtype = "float32", shape = (7, 8, 1))#candidate|6109|(7, 8, 1)|var|float32
func_6108_call = mutated_mod.get_global_var('func_6108')
call_6110 = func_6108_call(var_6109)
output = call_6110
func_6111 = relay.Function([var_6109], output)
mutated_mod['func_6111'] = func_6111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_6113 = relay.TupleGetItem(func_928_call(), 1)
call_6114 = relay.TupleGetItem(func_930_call(), 1)
output = call_6113
output2 = call_6114
func_6115 = relay.Function([], output)
mod['func_6115'] = func_6115
mod = relay.transform.InferType()(mod)
mutated_mod['func_6115'] = func_6115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6115_call = mutated_mod.get_global_var('func_6115')
call_6116 = func_6115_call()
output = call_6116
func_6117 = relay.Function([], output)
mutated_mod['func_6117'] = func_6117
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6121 = relay.var("var_6121", dtype = "int8", shape = (13, 4, 14))#candidate|6121|(13, 4, 14)|var|int8
var_6122 = relay.var("var_6122", dtype = "int8", shape = (13, 4, 14))#candidate|6122|(13, 4, 14)|var|int8
bop_6123 = relay.less_equal(var_6121.astype('bool'), relay.reshape(var_6122.astype('bool'), relay.shape_of(var_6121))) # shape=(13, 4, 14)
output = bop_6123
output2 = bop_6123
func_6134 = relay.Function([var_6121,var_6122,], output)
mod['func_6134'] = func_6134
mod = relay.transform.InferType()(mod)
var_6135 = relay.var("var_6135", dtype = "int8", shape = (13, 4, 14))#candidate|6135|(13, 4, 14)|var|int8
var_6136 = relay.var("var_6136", dtype = "int8", shape = (13, 4, 14))#candidate|6136|(13, 4, 14)|var|int8
output = func_6134(var_6135,var_6136,)
func_6137 = relay.Function([var_6135,var_6136,], output)
mutated_mod['func_6137'] = func_6137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1854_call = mod.get_global_var('func_1854')
func_1856_call = mutated_mod.get_global_var('func_1856')
call_6142 = func_1854_call()
call_6143 = func_1854_call()
func_2249_call = mod.get_global_var('func_2249')
func_2251_call = mutated_mod.get_global_var('func_2251')
call_6144 = relay.TupleGetItem(func_2249_call(), 0)
call_6145 = relay.TupleGetItem(func_2251_call(), 0)
func_2118_call = mod.get_global_var('func_2118')
func_2121_call = mutated_mod.get_global_var('func_2121')
call_6146 = relay.TupleGetItem(func_2118_call(relay.reshape(call_6144.astype('float32'), [10, 11, 8])), 1)
call_6147 = relay.TupleGetItem(func_2121_call(relay.reshape(call_6144.astype('float32'), [10, 11, 8])), 1)
output = relay.Tuple([call_6142,call_6144,call_6146,])
output2 = relay.Tuple([call_6143,call_6145,call_6147,])
func_6158 = relay.Function([], output)
mod['func_6158'] = func_6158
mod = relay.transform.InferType()(mod)
output = func_6158()
func_6159 = relay.Function([], output)
mutated_mod['func_6159'] = func_6159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4063_call = mod.get_global_var('func_4063')
func_4065_call = mutated_mod.get_global_var('func_4065')
call_6160 = func_4063_call()
call_6161 = func_4063_call()
func_3395_call = mod.get_global_var('func_3395')
func_3398_call = mutated_mod.get_global_var('func_3398')
var_6176 = relay.var("var_6176", dtype = "float32", shape = (1980,))#candidate|6176|(1980,)|var|float32
call_6175 = relay.TupleGetItem(func_3395_call(relay.reshape(var_6176.astype('float32'), [15, 11, 12])), 3)
call_6177 = relay.TupleGetItem(func_3398_call(relay.reshape(var_6176.astype('float32'), [15, 11, 12])), 3)
func_5426_call = mod.get_global_var('func_5426')
func_5428_call = mutated_mod.get_global_var('func_5428')
call_6180 = relay.TupleGetItem(func_5426_call(), 2)
call_6181 = relay.TupleGetItem(func_5428_call(), 2)
output = relay.Tuple([call_6160,call_6175,var_6176,call_6180,])
output2 = relay.Tuple([call_6161,call_6177,var_6176,call_6181,])
func_6188 = relay.Function([var_6176,], output)
mod['func_6188'] = func_6188
mod = relay.transform.InferType()(mod)
mutated_mod['func_6188'] = func_6188
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6189 = relay.var("var_6189", dtype = "float32", shape = (1980,))#candidate|6189|(1980,)|var|float32
func_6188_call = mutated_mod.get_global_var('func_6188')
call_6190 = func_6188_call(var_6189)
output = call_6190
func_6191 = relay.Function([var_6189], output)
mutated_mod['func_6191'] = func_6191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5617_call = mod.get_global_var('func_5617')
func_5618_call = mutated_mod.get_global_var('func_5618')
call_6250 = func_5617_call()
call_6251 = func_5617_call()
func_5465_call = mod.get_global_var('func_5465')
func_5468_call = mutated_mod.get_global_var('func_5468')
var_6269 = relay.var("var_6269", dtype = "float32", shape = (1680,))#candidate|6269|(1680,)|var|float32
call_6268 = relay.TupleGetItem(func_5465_call(relay.reshape(var_6269.astype('float32'), [16, 7, 15])), 0)
call_6270 = relay.TupleGetItem(func_5468_call(relay.reshape(var_6269.astype('float32'), [16, 7, 15])), 0)
func_1910_call = mod.get_global_var('func_1910')
func_1913_call = mutated_mod.get_global_var('func_1913')
const_6276 = relay.const([[True,True],[True,True],[False,False],[True,True],[True,False],[False,True],[True,False],[False,True],[True,False],[False,True],[False,True],[True,False],[False,False],[False,True],[False,True],[True,True],[True,False],[False,True],[True,False],[False,False],[False,True],[True,True],[True,True],[False,True],[True,True],[False,False],[False,True],[False,True],[True,False],[False,True],[True,False],[True,False],[False,True],[True,True],[True,False],[False,True],[True,True],[False,False],[True,True],[True,False],[False,False],[False,False],[True,False],[True,True],[False,False],[False,False],[False,True],[False,False],[True,False],[False,False],[False,False],[False,True],[True,False],[True,False],[True,True],[True,True],[True,True],[False,False],[False,True],[True,False],[True,False],[False,True],[True,True],[False,False],[True,False],[True,True],[False,True],[False,True],[True,True],[False,True],[False,True],[False,True],[False,False],[False,False],[False,True],[True,True],[True,True],[True,True],[False,True],[True,True],[True,False],[False,True],[True,False],[False,True],[False,False],[False,False],[True,False],[False,False],[True,False],[False,True],[True,True],[False,True],[True,True],[False,True],[False,True],[True,True],[False,True],[False,True],[False,True],[False,False],[True,False],[False,True],[True,False],[True,False],[False,True],[True,False],[True,True],[True,False],[True,True],[True,True],[False,False],[True,False],[False,True],[False,False],[False,False],[False,False],[True,False],[True,False],[True,False],[False,True],[True,True],[True,False],[False,False],[False,True],[True,False],[True,False],[False,False],[False,False],[True,False],[False,False],[True,False],[False,False],[True,True],[False,False],[True,False],[True,False],[True,True],[True,True],[True,True],[True,True],[True,False],[True,False],[False,True],[False,True],[False,True],[True,True],[True,True],[True,False],[False,True],[False,True],[True,False],[False,False],[True,True],[True,False],[False,False],[True,False],[False,False],[False,False],[False,False],[False,False],[True,True],[True,True],[True,False],[True,True],[True,False],[True,False],[False,True],[False,True],[False,True],[True,False],[False,True],[False,False],[True,False],[True,True],[True,True],[True,False],[False,False],[True,True],[False,True],[True,True],[True,False],[True,True],[True,True],[False,True],[True,True],[True,True],[False,False],[True,False],[False,False],[True,True],[True,True],[False,False],[True,True],[True,False],[False,False],[True,True],[False,True],[False,True],[False,False],[False,True],[False,False],[False,False],[False,False],[False,False],[False,False],[False,False],[True,False],[False,False],[True,True],[False,False]], dtype = "bool")#candidate|6276|(210, 2)|const|bool
const_6277 = relay.const([-5.340157,2.580715,-6.197914,5.538462,4.304939,-8.730697,3.163552,1.556338,-9.521902,2.874462,2.699309,-8.386995,-7.060328,2.230897,-7.625592,-2.270526,-7.063374,9.837589,-4.424496,-0.464121,7.323807,9.892426,-3.936538,6.439585,-8.939663,3.596688,-5.974360,-1.058283,8.258188,-0.949631,-2.500751,2.283384,3.598338,3.865988,6.644936,5.412222,1.177793,3.350176,9.213333,-4.028800,-7.026814,-6.099924,3.127192,4.539001,-3.205666,3.153877,-9.328191,5.011071,6.623253,-0.877521,-7.480054,9.337757,-9.387064,9.233461,2.461206,6.460285,-3.067576,-3.532830,4.558372,-3.198222,-9.407539,-8.838210,-9.364495,-4.474453,5.027582,-6.855766,-7.452806,4.329469,2.532393,-9.226715,-7.644147,-5.134555,3.156976,-3.617993,-7.665727,8.366186,-0.764678,3.852746,8.903896,-9.681986,-6.270619,4.373680,-2.176797,-9.008716,5.400454,-9.771210,-3.800174,-2.607542,-2.373979,-3.781011,-5.650627,5.931794,-3.016849,7.106850,-3.089060,-2.227755,6.396166,9.095752,-5.361763,3.079570,-1.524978,8.772936,-0.554689,6.447590,-5.343342,0.158175,9.951814,-6.244660,7.832869,0.458717,2.315430,5.607174,6.059268,5.080894,-1.078718,-0.908289,-1.409820,4.637928,6.378415,2.856404,7.501522,-0.752510,5.137113,-9.405303,7.970790,-2.940245,3.427994,5.340110,-9.668492,-3.409555,9.036138,-9.813822,-6.702998,-6.610933,-0.070445,7.101664,-9.133385,-5.499416,-3.242523,-2.327250,-5.077884,5.467703,-2.798173,8.305225,9.669513,2.630228,-9.039114,-7.199379,-0.827998,-8.697548,0.984877,-8.576840,-6.913999,7.358253,6.935881,-3.248326,1.669845,1.419787,-2.754360,-5.591196,-9.698327,-0.005272,2.249506,4.539724,3.609570,-5.821341,6.300963,-5.465892,6.070846,0.645821,7.184444,1.941997,4.372634,3.537318,3.844698,0.170797,3.116498,-4.568938,-7.599215,-4.398966,2.928585,-8.941210,9.255036,-1.853552,9.228882,7.970886,5.924342,3.329648,7.608369,-5.259618,-9.596391,-2.296539,4.544910,7.350145,-4.000952,9.697149,-6.534813,4.226722,-2.552525,3.513056,6.030319,4.458685,0.461040,2.474380,7.605335,3.497251,2.120416,7.759095,-0.842323,-3.862852,3.670273,-9.357414,-1.734632,0.857023,-9.678883,-8.540926,-0.284588,-5.770127,-5.717351,-3.744424,-3.683155,7.679257,-1.311551,-9.479743,7.277701,9.129281,1.742091,0.689640,2.389488,-0.087980,9.522510,8.237010,-4.733934,4.926327,8.403213,-4.215544,6.947380,6.615121,7.655171,-2.104663,4.351302,2.705913,0.975718,-5.213554,8.422093,-4.731559,0.107449,-3.979830,-5.480430,-1.725089,-8.457213,5.346095,-0.566512,4.554215,-5.722946,9.242308,5.026410,-3.704697,1.756057,-1.817561,-6.176085,4.395086,-4.225969,6.658941,5.796514,8.830037,9.638590,0.584091,8.794558,9.616816,-4.070349,9.841367,0.814711,-5.854867,-9.749285,2.398466,-2.058961,-1.869016,6.748908,0.154992,6.200751,-9.897598,0.186945,3.332249,-6.650455,-0.371623,7.455650,-3.481618,-3.563398,2.225359,7.712181,8.022959,4.782770,5.441184,6.362991,0.107373,0.323750,6.079400,5.965036,0.393140,1.287750,-3.605612,-3.624614,6.110686,6.314660,6.391734,-2.406763,-1.252043,2.652320,-5.592925,-0.077011,6.770917,6.651239,-7.825075,2.738708,-4.179392,-8.250320,8.554501,8.295108,7.536543,6.351252,-3.668809,2.121394,5.698880,-9.307882,0.528843,3.944129,-7.511308,-0.721870,0.504468,-3.677179,-6.109293,-7.856524,6.324575,0.143591,0.191367,-9.038925,-0.603505,-4.228062,-2.539175,9.382399,-8.701420,-5.404714,1.729719,0.685054,3.054219,-4.179287,-5.121631,9.972621,-2.164542,-8.924699,-9.176239,8.199764,-6.307665,-9.309754,-8.020658,9.851858,6.774961,8.763128,-0.120141,2.436675,0.433126,3.980218,9.840620,1.828518,7.102567,4.012583,-7.684684,-3.674624,-8.721886,1.815668,-1.942514,4.058536,1.165796,-3.607979,-0.354038,4.025438,1.072332,6.893381,3.371660,4.845724,7.961905,-2.328661,7.876638,-4.074784,-7.360888,7.903562,-5.357718,-8.351441,3.382149,0.969437,-3.645063,1.262362,-3.117662,-1.457070,-0.507190,-6.114638,-9.760017,6.378708,-0.782257,-0.917805,-9.030955,5.788699,-3.823618,-2.401834,5.596405,7.843044,-3.354869,7.737022,-4.212802,-2.993849,5.940631,-6.563075,-7.795946,-7.153173,9.664832,3.842721,-1.816113,1.558974,-8.378931,-5.929326,0.754765,6.634673,4.887178,-1.410793,9.736612,-4.747738,-7.778300,-8.528949,-3.637233,5.191239,7.798887,0.310099,0.866547,5.563018,-1.091233,9.666615,3.948776,2.378463,-0.887799,-8.840774,7.380558,-2.892316,6.221269,-5.881955,3.425540,-5.015759,-5.282435,-8.410960,-8.970747,0.311464,-6.235270,-3.085763,1.897141,-9.737637,-5.489897,2.635757,7.400535,2.768000,7.928064,-5.626271,2.050668], dtype = "float64")#candidate|6277|(462,)|const|float64
call_6275 = relay.TupleGetItem(func_1910_call(relay.reshape(const_6276.astype('bool'), [420,]), relay.reshape(const_6277.astype('float64'), [462,]), ), 3)
call_6278 = relay.TupleGetItem(func_1913_call(relay.reshape(const_6276.astype('bool'), [420,]), relay.reshape(const_6277.astype('float64'), [462,]), ), 3)
func_4231_call = mod.get_global_var('func_4231')
func_4234_call = mutated_mod.get_global_var('func_4234')
var_6288 = relay.var("var_6288", dtype = "float32", shape = (1001,))#candidate|6288|(1001,)|var|float32
call_6287 = relay.TupleGetItem(func_4231_call(relay.reshape(var_6288.astype('float32'), [11, 7, 13])), 0)
call_6289 = relay.TupleGetItem(func_4234_call(relay.reshape(var_6288.astype('float32'), [11, 7, 13])), 0)
func_1572_call = mod.get_global_var('func_1572')
func_1574_call = mutated_mod.get_global_var('func_1574')
call_6295 = relay.TupleGetItem(func_1572_call(), 0)
call_6296 = relay.TupleGetItem(func_1574_call(), 0)
func_5639_call = mod.get_global_var('func_5639')
func_5640_call = mutated_mod.get_global_var('func_5640')
call_6303 = relay.TupleGetItem(func_5639_call(), 0)
call_6304 = relay.TupleGetItem(func_5640_call(), 0)
func_4210_call = mod.get_global_var('func_4210')
func_4211_call = mutated_mod.get_global_var('func_4211')
call_6318 = func_4210_call()
call_6319 = func_4210_call()
output = relay.Tuple([call_6250,call_6268,var_6269,call_6275,const_6276,const_6277,call_6287,var_6288,call_6295,call_6303,call_6318,])
output2 = relay.Tuple([call_6251,call_6270,var_6269,call_6278,const_6276,const_6277,call_6289,var_6288,call_6296,call_6304,call_6319,])
func_6324 = relay.Function([var_6269,var_6288,], output)
mod['func_6324'] = func_6324
mod = relay.transform.InferType()(mod)
mutated_mod['func_6324'] = func_6324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6324_call = mutated_mod.get_global_var('func_6324')
var_6326 = relay.var("var_6326", dtype = "float32", shape = (1680,))#candidate|6326|(1680,)|var|float32
var_6327 = relay.var("var_6327", dtype = "float32", shape = (1001,))#candidate|6327|(1001,)|var|float32
call_6325 = func_6324_call(var_6326,var_6327,)
output = call_6325
func_6328 = relay.Function([var_6326,var_6327,], output)
mutated_mod['func_6328'] = func_6328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4093_call = mod.get_global_var('func_4093')
func_4094_call = mutated_mod.get_global_var('func_4094')
call_6330 = relay.TupleGetItem(func_4093_call(), 1)
call_6331 = relay.TupleGetItem(func_4094_call(), 1)
func_3685_call = mod.get_global_var('func_3685')
func_3686_call = mutated_mod.get_global_var('func_3686')
call_6341 = relay.TupleGetItem(func_3685_call(), 0)
call_6342 = relay.TupleGetItem(func_3686_call(), 0)
func_4719_call = mod.get_global_var('func_4719')
func_4720_call = mutated_mod.get_global_var('func_4720')
call_6345 = relay.TupleGetItem(func_4719_call(), 0)
call_6346 = relay.TupleGetItem(func_4720_call(), 0)
output = relay.Tuple([call_6330,call_6341,call_6345,])
output2 = relay.Tuple([call_6331,call_6342,call_6346,])
func_6351 = relay.Function([], output)
mod['func_6351'] = func_6351
mod = relay.transform.InferType()(mod)
mutated_mod['func_6351'] = func_6351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6351_call = mutated_mod.get_global_var('func_6351')
call_6352 = func_6351_call()
output = call_6352
func_6353 = relay.Function([], output)
mutated_mod['func_6353'] = func_6353
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6382 = relay.var("var_6382", dtype = "uint64", shape = (9, 15, 3))#candidate|6382|(9, 15, 3)|var|uint64
var_6383 = relay.var("var_6383", dtype = "uint64", shape = (9, 15, 3))#candidate|6383|(9, 15, 3)|var|uint64
bop_6384 = relay.less(var_6382.astype('bool'), relay.reshape(var_6383.astype('bool'), relay.shape_of(var_6382))) # shape=(9, 15, 3)
output = bop_6384
output2 = bop_6384
func_6389 = relay.Function([var_6382,var_6383,], output)
mod['func_6389'] = func_6389
mod = relay.transform.InferType()(mod)
var_6390 = relay.var("var_6390", dtype = "uint64", shape = (9, 15, 3))#candidate|6390|(9, 15, 3)|var|uint64
var_6391 = relay.var("var_6391", dtype = "uint64", shape = (9, 15, 3))#candidate|6391|(9, 15, 3)|var|uint64
output = func_6389(var_6390,var_6391,)
func_6392 = relay.Function([var_6390,var_6391,], output)
mutated_mod['func_6392'] = func_6392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3685_call = mod.get_global_var('func_3685')
func_3686_call = mutated_mod.get_global_var('func_3686')
call_6443 = relay.TupleGetItem(func_3685_call(), 0)
call_6444 = relay.TupleGetItem(func_3686_call(), 0)
output = relay.Tuple([call_6443,])
output2 = relay.Tuple([call_6444,])
func_6446 = relay.Function([], output)
mod['func_6446'] = func_6446
mod = relay.transform.InferType()(mod)
output = func_6446()
func_6447 = relay.Function([], output)
mutated_mod['func_6447'] = func_6447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2539_call = mod.get_global_var('func_2539')
func_2540_call = mutated_mod.get_global_var('func_2540')
call_6456 = relay.TupleGetItem(func_2539_call(), 1)
call_6457 = relay.TupleGetItem(func_2540_call(), 1)
output = call_6456
output2 = call_6457
func_6492 = relay.Function([], output)
mod['func_6492'] = func_6492
mod = relay.transform.InferType()(mod)
mutated_mod['func_6492'] = func_6492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6492_call = mutated_mod.get_global_var('func_6492')
call_6493 = func_6492_call()
output = call_6493
func_6494 = relay.Function([], output)
mutated_mod['func_6494'] = func_6494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4093_call = mod.get_global_var('func_4093')
func_4094_call = mutated_mod.get_global_var('func_4094')
call_6500 = relay.TupleGetItem(func_4093_call(), 0)
call_6501 = relay.TupleGetItem(func_4094_call(), 0)
func_3923_call = mod.get_global_var('func_3923')
func_3925_call = mutated_mod.get_global_var('func_3925')
call_6502 = func_3923_call()
call_6503 = func_3923_call()
output = relay.Tuple([call_6500,call_6502,])
output2 = relay.Tuple([call_6501,call_6503,])
func_6505 = relay.Function([], output)
mod['func_6505'] = func_6505
mod = relay.transform.InferType()(mod)
mutated_mod['func_6505'] = func_6505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6505_call = mutated_mod.get_global_var('func_6505')
call_6506 = func_6505_call()
output = call_6506
func_6507 = relay.Function([], output)
mutated_mod['func_6507'] = func_6507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4654_call = mod.get_global_var('func_4654')
func_4655_call = mutated_mod.get_global_var('func_4655')
call_6559 = relay.TupleGetItem(func_4654_call(), 2)
call_6560 = relay.TupleGetItem(func_4655_call(), 2)
output = relay.Tuple([call_6559,])
output2 = relay.Tuple([call_6560,])
func_6561 = relay.Function([], output)
mod['func_6561'] = func_6561
mod = relay.transform.InferType()(mod)
output = func_6561()
func_6562 = relay.Function([], output)
mutated_mod['func_6562'] = func_6562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4559_call = mod.get_global_var('func_4559')
func_4560_call = mutated_mod.get_global_var('func_4560')
call_6571 = relay.TupleGetItem(func_4559_call(), 0)
call_6572 = relay.TupleGetItem(func_4560_call(), 0)
output = relay.Tuple([call_6571,])
output2 = relay.Tuple([call_6572,])
func_6573 = relay.Function([], output)
mod['func_6573'] = func_6573
mod = relay.transform.InferType()(mod)
output = func_6573()
func_6574 = relay.Function([], output)
mutated_mod['func_6574'] = func_6574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6561_call = mod.get_global_var('func_6561')
func_6562_call = mutated_mod.get_global_var('func_6562')
call_6685 = relay.TupleGetItem(func_6561_call(), 0)
call_6686 = relay.TupleGetItem(func_6562_call(), 0)
func_2913_call = mod.get_global_var('func_2913')
func_2916_call = mutated_mod.get_global_var('func_2916')
var_6692 = relay.var("var_6692", dtype = "float32", shape = (8, 110))#candidate|6692|(8, 110)|var|float32
call_6691 = relay.TupleGetItem(func_2913_call(relay.reshape(var_6692.astype('float32'), [880,])), 1)
call_6693 = relay.TupleGetItem(func_2916_call(relay.reshape(var_6692.astype('float32'), [880,])), 1)
func_2004_call = mod.get_global_var('func_2004')
func_2006_call = mutated_mod.get_global_var('func_2006')
call_6694 = relay.TupleGetItem(func_2004_call(), 0)
call_6695 = relay.TupleGetItem(func_2006_call(), 0)
func_2684_call = mod.get_global_var('func_2684')
func_2686_call = mutated_mod.get_global_var('func_2686')
call_6697 = relay.TupleGetItem(func_2684_call(), 0)
call_6698 = relay.TupleGetItem(func_2686_call(), 0)
func_781_call = mod.get_global_var('func_781')
func_785_call = mutated_mod.get_global_var('func_785')
var_6702 = relay.var("var_6702", dtype = "int32", shape = (840,))#candidate|6702|(840,)|var|int32
call_6701 = relay.TupleGetItem(func_781_call(relay.reshape(var_6702.astype('int32'), [14, 10, 6]), relay.reshape(var_6692.astype('float32'), [10, 11, 8]), ), 1)
call_6703 = relay.TupleGetItem(func_785_call(relay.reshape(var_6702.astype('int32'), [14, 10, 6]), relay.reshape(var_6692.astype('float32'), [10, 11, 8]), ), 1)
func_3085_call = mod.get_global_var('func_3085')
func_3086_call = mutated_mod.get_global_var('func_3086')
call_6717 = relay.TupleGetItem(func_3085_call(), 0)
call_6718 = relay.TupleGetItem(func_3086_call(), 0)
func_2482_call = mod.get_global_var('func_2482')
func_2484_call = mutated_mod.get_global_var('func_2484')
call_6720 = relay.TupleGetItem(func_2482_call(), 0)
call_6721 = relay.TupleGetItem(func_2484_call(), 0)
uop_6722 = relay.exp(call_6685.astype('float64')) # shape=(78, 4)
uop_6724 = relay.exp(call_6686.astype('float64')) # shape=(78, 4)
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_6725 = relay.TupleGetItem(func_1084_call(), 0)
call_6726 = relay.TupleGetItem(func_1085_call(), 0)
uop_6752 = relay.tan(uop_6722.astype('float64')) # shape=(78, 4)
uop_6754 = relay.tan(uop_6724.astype('float64')) # shape=(78, 4)
func_4654_call = mod.get_global_var('func_4654')
func_4655_call = mutated_mod.get_global_var('func_4655')
call_6771 = relay.TupleGetItem(func_4654_call(), 2)
call_6772 = relay.TupleGetItem(func_4655_call(), 2)
var_6776 = relay.var("var_6776", dtype = "float64", shape = (78, 4))#candidate|6776|(78, 4)|var|float64
bop_6777 = relay.bitwise_and(uop_6752.astype('uint32'), relay.reshape(var_6776.astype('uint32'), relay.shape_of(uop_6752))) # shape=(78, 4)
bop_6780 = relay.bitwise_and(uop_6754.astype('uint32'), relay.reshape(var_6776.astype('uint32'), relay.shape_of(uop_6754))) # shape=(78, 4)
bop_6783 = relay.logical_xor(uop_6752.astype('int32'), relay.reshape(uop_6722.astype('int32'), relay.shape_of(uop_6752))) # shape=(78, 4)
bop_6786 = relay.logical_xor(uop_6754.astype('int32'), relay.reshape(uop_6724.astype('int32'), relay.shape_of(uop_6754))) # shape=(78, 4)
bop_6788 = relay.less_equal(uop_6752.astype('bool'), relay.reshape(call_6771.astype('bool'), relay.shape_of(uop_6752))) # shape=(78, 4)
bop_6791 = relay.less_equal(uop_6754.astype('bool'), relay.reshape(call_6772.astype('bool'), relay.shape_of(uop_6754))) # shape=(78, 4)
func_904_call = mod.get_global_var('func_904')
func_908_call = mutated_mod.get_global_var('func_908')
const_6793 = relay.const([[False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,True],[False,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False],[False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True],[True,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False],[True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True],[False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True],[True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True],[False,True,True,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False],[False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True],[True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False]], dtype = "bool")#candidate|6793|(10, 42)|const|bool
var_6794 = relay.var("var_6794", dtype = "float64", shape = (462,))#candidate|6794|(462,)|var|float64
call_6792 = relay.TupleGetItem(func_904_call(relay.reshape(const_6793.astype('bool'), [2, 15, 14]), relay.reshape(var_6794.astype('float64'), [462, 1]), ), 4)
call_6795 = relay.TupleGetItem(func_908_call(relay.reshape(const_6793.astype('bool'), [2, 15, 14]), relay.reshape(var_6794.astype('float64'), [462, 1]), ), 4)
uop_6802 = relay.log2(uop_6722.astype('float32')) # shape=(78, 4)
uop_6804 = relay.log2(uop_6724.astype('float32')) # shape=(78, 4)
var_6806 = relay.var("var_6806", dtype = "int32", shape = (78, 4))#candidate|6806|(78, 4)|var|int32
bop_6807 = relay.maximum(bop_6783.astype('int16'), relay.reshape(var_6806.astype('int16'), relay.shape_of(bop_6783))) # shape=(78, 4)
bop_6810 = relay.maximum(bop_6786.astype('int16'), relay.reshape(var_6806.astype('int16'), relay.shape_of(bop_6786))) # shape=(78, 4)
output = relay.Tuple([call_6691,var_6692,call_6694,call_6697,call_6701,var_6702,call_6717,call_6720,call_6725,bop_6777,bop_6788,call_6792,const_6793,var_6794,uop_6802,bop_6807,])
output2 = relay.Tuple([call_6693,var_6692,call_6695,call_6698,call_6703,var_6702,call_6718,call_6721,call_6726,bop_6780,bop_6791,call_6795,const_6793,var_6794,uop_6804,bop_6810,])
func_6812 = relay.Function([var_6692,var_6702,var_6776,var_6794,var_6806,], output)
mod['func_6812'] = func_6812
mod = relay.transform.InferType()(mod)
mutated_mod['func_6812'] = func_6812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mutated_mod.get_global_var('func_6812')
var_6814 = relay.var("var_6814", dtype = "float32", shape = (8, 110))#candidate|6814|(8, 110)|var|float32
var_6815 = relay.var("var_6815", dtype = "int32", shape = (840,))#candidate|6815|(840,)|var|int32
var_6816 = relay.var("var_6816", dtype = "float64", shape = (78, 4))#candidate|6816|(78, 4)|var|float64
var_6817 = relay.var("var_6817", dtype = "float64", shape = (462,))#candidate|6817|(462,)|var|float64
var_6818 = relay.var("var_6818", dtype = "int32", shape = (78, 4))#candidate|6818|(78, 4)|var|int32
call_6813 = func_6812_call(var_6814,var_6815,var_6816,var_6817,var_6818,)
output = call_6813
func_6819 = relay.Function([var_6814,var_6815,var_6816,var_6817,var_6818,], output)
mutated_mod['func_6819'] = func_6819
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6857 = relay.var("var_6857", dtype = "float32", shape = ())#candidate|6857|()|var|float32
var_6858 = relay.var("var_6858", dtype = "float32", shape = (6, 2, 5))#candidate|6858|(6, 2, 5)|var|float32
bop_6859 = relay.power(var_6857.astype('float32'), var_6858.astype('float32')) # shape=(6, 2, 5)
func_2613_call = mod.get_global_var('func_2613')
func_2615_call = mutated_mod.get_global_var('func_2615')
var_6865 = relay.var("var_6865", dtype = "float32", shape = (96,))#candidate|6865|(96,)|var|float32
call_6864 = relay.TupleGetItem(func_2613_call(relay.reshape(var_6865.astype('float32'), [2, 4, 12])), 1)
call_6866 = relay.TupleGetItem(func_2615_call(relay.reshape(var_6865.astype('float32'), [2, 4, 12])), 1)
output = relay.Tuple([bop_6859,call_6864,var_6865,])
output2 = relay.Tuple([bop_6859,call_6866,var_6865,])
func_6867 = relay.Function([var_6857,var_6858,var_6865,], output)
mod['func_6867'] = func_6867
mod = relay.transform.InferType()(mod)
var_6868 = relay.var("var_6868", dtype = "float32", shape = ())#candidate|6868|()|var|float32
var_6869 = relay.var("var_6869", dtype = "float32", shape = (6, 2, 5))#candidate|6869|(6, 2, 5)|var|float32
var_6870 = relay.var("var_6870", dtype = "float32", shape = (96,))#candidate|6870|(96,)|var|float32
output = func_6867(var_6868,var_6869,var_6870,)
func_6871 = relay.Function([var_6868,var_6869,var_6870,], output)
mutated_mod['func_6871'] = func_6871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6888 = relay.var("var_6888", dtype = "float64", shape = (10, 13, 8))#candidate|6888|(10, 13, 8)|var|float64
uop_6889 = relay.log(var_6888.astype('float64')) # shape=(10, 13, 8)
func_6158_call = mod.get_global_var('func_6158')
func_6159_call = mutated_mod.get_global_var('func_6159')
call_6903 = relay.TupleGetItem(func_6158_call(), 1)
call_6904 = relay.TupleGetItem(func_6159_call(), 1)
var_6914 = relay.var("var_6914", dtype = "float64", shape = (10, 13, 8))#candidate|6914|(10, 13, 8)|var|float64
bop_6915 = relay.less_equal(var_6888.astype('bool'), relay.reshape(var_6914.astype('bool'), relay.shape_of(var_6888))) # shape=(10, 13, 8)
bop_6920 = relay.bitwise_and(uop_6889.astype('uint64'), relay.reshape(var_6914.astype('uint64'), relay.shape_of(uop_6889))) # shape=(10, 13, 8)
bop_6927 = relay.subtract(uop_6889.astype('int32'), relay.reshape(bop_6915.astype('int32'), relay.shape_of(uop_6889))) # shape=(10, 13, 8)
bop_6930 = relay.floor_divide(uop_6889.astype('float64'), relay.reshape(bop_6927.astype('float64'), relay.shape_of(uop_6889))) # shape=(10, 13, 8)
uop_6940 = relay.sinh(bop_6930.astype('float32')) # shape=(10, 13, 8)
output = relay.Tuple([call_6903,bop_6920,uop_6940,])
output2 = relay.Tuple([call_6904,bop_6920,uop_6940,])
func_6956 = relay.Function([var_6888,var_6914,], output)
mod['func_6956'] = func_6956
mod = relay.transform.InferType()(mod)
mutated_mod['func_6956'] = func_6956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6956_call = mutated_mod.get_global_var('func_6956')
var_6958 = relay.var("var_6958", dtype = "float64", shape = (10, 13, 8))#candidate|6958|(10, 13, 8)|var|float64
var_6959 = relay.var("var_6959", dtype = "float64", shape = (10, 13, 8))#candidate|6959|(10, 13, 8)|var|float64
call_6957 = func_6956_call(var_6958,var_6959,)
output = call_6957
func_6960 = relay.Function([var_6958,var_6959,], output)
mutated_mod['func_6960'] = func_6960
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6986 = relay.var("var_6986", dtype = "uint64", shape = ())#candidate|6986|()|var|uint64
var_6987 = relay.var("var_6987", dtype = "uint64", shape = (10, 14, 14))#candidate|6987|(10, 14, 14)|var|uint64
bop_6988 = relay.less(var_6986.astype('bool'), var_6987.astype('bool')) # shape=(10, 14, 14)
bop_7011 = relay.greater_equal(bop_6988.astype('bool'), relay.reshape(var_6987.astype('bool'), relay.shape_of(bop_6988))) # shape=(10, 14, 14)
func_6812_call = mod.get_global_var('func_6812')
func_6819_call = mutated_mod.get_global_var('func_6819')
const_7017 = relay.const([-4.851926,0.664389,2.750335,-7.683674,4.895527,2.434401,8.548387,4.607732,-4.024993,-6.303589,1.383450,-9.413873,7.563659,-1.990070,-8.979985,-2.291624,-6.357185,-7.846869,8.556696,-5.063815,2.280720,-9.228958,-1.967727,-0.756583,0.678876,-0.220642,-1.234599,-0.150263,5.983979,6.631275,-8.916757,-4.111990,1.658828,7.428495,3.599058,9.514314,3.151185,-6.545077,-1.611448,-7.265273,5.157052,-2.018407,9.500535,6.775725,0.106198,9.078095,7.451434,-6.680696,-7.492575,4.309402,-9.080934,0.210580,-5.975009,2.263745,-5.135714,-9.135835,-8.448928,-7.238548,9.119632,-3.512787,-7.311268,1.240820,-6.255453,-9.289741,5.082233,-8.756179,4.182262,4.568198,7.938148,-4.234774,-1.401882,0.630106,5.971522,-6.752713,-3.827607,4.855277,-6.068169,-3.131850,8.319999,-0.172192,-1.284037,-5.004853,-7.505556,-8.989140,-5.250855,5.215831,2.281599,7.775214,-2.843248,-2.600770,1.643209,0.168555,-0.086061,-3.121371,1.539214,-3.123861,1.439560,8.122806,-8.346113,-5.491766,-6.967981,5.516966,-8.330341,-0.614255,-6.100294,2.786083,-4.134082,-4.813512,-9.770551,-7.493619,2.425183,-3.483092,8.067148,-9.928356,6.233154,-5.332840,-4.407189,5.999884,3.274324,-5.828631,-3.250333,9.494562,-6.054822,9.511405,-7.860261,-4.806557,-2.612800,-2.318524,-3.462776,8.705166,0.917961,2.307883,1.232675,2.199420,-5.374454,2.025867,9.782214,-1.263543,-1.082080,2.999479,3.696919,-8.271827,-7.862244,-7.405687,1.409519,-4.317724,0.659425,-5.429078,-5.859816,7.021546,7.934298,-5.842236,5.388642,9.594211,-8.098081,-4.001563,-5.929714,-5.783283,-4.353286,-7.208103,-8.702520,-9.824603,-3.621174,8.234322,-5.130871,-3.297225,4.406044,8.684764,4.449431,-8.744885,0.183178,8.778774,7.932709,-4.111947,-1.406036,1.928041,2.281042,6.240154,-0.993109,-2.835907,7.803474,3.352625,9.568652,-8.139482,9.018851,6.626578,0.095053,-9.573035,-0.636343,-3.848128,7.610250,3.138517,-7.601688,6.872041,6.400662,3.271991,-6.076095,1.550263,2.418658,-3.947556,-0.636005,9.188906,-5.413828,-5.051055,-7.827037,-2.741635,-3.815981,-9.234965,-8.485008,-8.723804,-3.249206,-1.694210,-9.103214,-2.553001,2.562027,-5.368232,-3.030859,-0.214679,3.644038,9.495786,4.751405,-6.037923,-9.826421,-4.880606,-9.941157,-1.449765,1.310226,9.355079,3.775040,0.353147,-2.701295,-7.323603,-5.624264,3.398903,-8.348908,5.068957,-6.177707,0.345904,5.096659,8.142190,-9.898908,-1.020136,0.430069,7.029620,6.307309,1.206859,-0.381320,9.357248,-5.266850,8.964736,4.864613,4.102676,-0.206514,-0.033117,-4.062041,4.902975,-8.866057,-8.650937,4.999068,-1.421842,3.462554,-2.368868,4.991160,-6.348682,-7.806717,-8.885012,-5.076356,-9.593284,3.929562,-0.533075,-2.166522,-7.285249,9.022517,-0.282669,9.860410,-9.777648,9.920906,-0.883532,-0.324488,-7.081036,-5.995909,-9.684746,-1.870202,4.768530,-3.097205,-2.508552,4.736894,9.436294,2.530214,0.526992,-9.662919,8.129501,-0.886603,-8.790369,-8.695128,-6.654294,-3.276030,-4.153275,4.824003,-7.153217,5.897458,-4.883039,6.390150,-2.911090,-0.612674,4.233311,5.079936,-8.333336,3.348954,-5.490898,7.817826,-2.135479,0.065625,5.333974,1.502025,-1.075260,-7.275824,5.082028,-7.944988,-5.816178,-0.653263,5.177579,0.327639,2.690888,0.237783,-5.009640,-6.606027,-0.703598,8.360344,-1.673900,8.134879,-3.160972,-1.382371,9.086101,2.691646,5.262831,-9.639797,9.344177,-0.356599,-9.466684,-7.689221,-7.596144,8.989607,-9.781006,-6.301371,5.845164,-4.087955,8.110625,-5.806619,6.840456,9.072671,9.854388,-7.801752,2.986831,7.061814,-8.045618,-6.720571,9.276722,0.228471,9.114368,-2.723634,7.059128,-0.255074,2.399669,1.893773,-8.132357,1.446293,-6.671094,-9.462421,-5.749426,2.134003,8.802978,-2.323834,-9.131847,-5.602444,9.877031,-8.338814,6.901869,-2.477851,4.504134,-9.228603,-8.912564,5.470681,5.115890,-2.096288,-2.416817,-0.577537,2.496731,-3.958800,-3.653693,3.603472,6.371102,-9.611606,-3.446559,-7.640810,-2.665219,2.220919,-3.059455,-6.435717,-4.207255,-9.807542,-7.865364,-1.332495,6.252625,0.728957,-4.361840,7.802592,6.661825,-7.044019,-7.917058,0.077097,8.883818,5.734290,-3.312742,3.085349,-2.015062,8.057013,-1.491907,0.200761,-2.172548,5.886446,3.226905,-3.185127,-1.707533,7.570446,8.471180,-1.601187,5.066483,0.893109,5.467485,5.987764,-3.778911,-1.783123,-0.254563,-2.040464,6.727449,2.551949,-9.960271,1.027097,1.120427,-2.983478,3.164798,4.104209,-3.800472,-2.345301,-4.724714,-6.180031,-1.533631,5.774877,-9.080052,4.051336,-7.022004,-5.303551,0.953485,4.480426,-7.956002,9.640981,-1.337509,2.178172,1.988653,-3.101317,1.452409,-6.994146,-6.322752,-7.015169,6.364685,-6.823290,0.453630,2.482586,-7.809772,2.581221,-9.140786,-4.446373,2.958289,9.024886,-7.249382,-7.590169,-2.327931,7.373969,9.666852,8.142367,-6.232875,-7.321655,5.316313,-6.842699,-8.350474,-1.298318,-3.618654,-1.810759,-1.274222,5.028721,6.712906,-1.897513,-8.922583,-7.439142,-6.819352,5.490013,6.052946,-8.167384,0.207141,-9.803227,-7.240501,-9.759046,-2.559081,-1.507902,-0.510222,9.526189,-1.947437,-1.293107,5.125398,-0.509069,-0.504782,-3.321691,9.802453,-1.995081,9.679521,-7.663404,-0.481722,5.888990,2.211540,5.394994,0.509357,-8.858988,0.072534,-6.471462,2.646667,-7.874997,-8.813204,-2.673447,6.022694,-2.622983,1.582358,-4.413257,3.765977,-6.952958,9.697225,6.939848,-1.036125,-9.818037,-1.804311,0.530059,7.980359,2.266869,-7.884234,7.436108,7.700423,1.763288,6.018378,-1.383782,5.856687,3.232517,-2.531338,9.237102,-8.488777,-7.424243,-8.732783,7.881811,8.394005,-5.362942,-2.289818,6.006749,3.789148,-0.902486,-2.682209,-5.247761,-4.752603,4.008680,-9.949229,8.916305,-1.637669,6.973057,1.034464,2.346672,8.194884,5.724595,0.790705,5.348631,4.663722,1.156788,-2.631484,5.197889,-1.598616,-6.449177,0.359303,7.271499,1.163743,-2.002524,6.355525,-8.334261,5.013192,-9.519105,-2.629297,-6.807455,-6.783340,-9.193359,9.920694,9.955467,-0.804437,-8.725163,4.360344,9.157072,-2.858487,-5.477538,0.635642,-8.049868,-8.207445,-2.033373,3.915421,-5.222443,-6.759889,-0.742762,-0.184674,8.124702,8.792310,-2.999722,-2.416015,-6.713917,6.436788,-8.547444,0.927871,-0.884768,-9.166723,-7.574847,8.220365,2.830725,9.621606,3.346585,1.622988,-0.904546,-6.196587,1.228291,8.491058,9.189694,-1.128437,3.109642,-3.965233,3.552907,-0.503789,-5.857380,-6.168701,-0.904581,-7.654868,7.149762,-1.771491,-8.036014,-3.385729,9.777432,1.814639,7.113879,2.145403,7.635582,-7.285640,-6.533553,2.745419,-8.347278,-2.225290,7.741024,-0.081366,-7.807295,7.191743,5.012098,-9.140545,6.286433,9.815712,-9.110132,5.098880,-2.206642,-5.486433,7.320857,-4.301454,-0.379234,-0.244359,1.756310,-1.131441,3.081130,-9.455891,-1.415680,-4.321573,3.279205,-7.567577,-3.205645,4.443396,7.197465,6.518089,7.938015,-1.092638,-6.429364,-0.214074,3.145228,7.653848,-0.350692,4.252188,-6.768070,-4.204209,6.007506,1.219145,-9.289021,-1.754481,0.991914,-4.889331,7.547189,-2.773444,5.838836,1.884796,9.339485,-0.319167,8.278480,-9.489918,6.372556,6.725137,4.978003,-5.185364,3.153957,8.044404,-6.503721,-0.847056,-7.843034,3.820874,5.535148,-7.826562,6.070759,-4.447766,-0.195963,-6.624178,5.125075,-0.201737,0.088514,-9.827951,-1.563658,7.159474,-0.963521,-3.691226,-9.884660,-8.465647,7.589250,-0.870437,9.314975,8.935454,-2.906277,1.334440,8.120388,-9.501455,-3.484397,3.111331,9.477183,7.442316,-7.895221,-3.493630,5.315451,-8.607940,-4.218852,1.566798,0.143270,3.225628,7.555024,4.539851,7.815844,0.733165,5.519713,-6.223033,8.159316,-0.637379,2.976451,-5.029461,9.140437,1.822242,3.397593,-8.864057,8.100732,-0.527851,-6.257331,9.369978,-1.984574,-4.936322,-8.778316,-6.367022,-9.391164,3.559724,8.281516,9.189633,2.164898,-5.633932,5.324382,8.961339,3.484688,6.486274,-2.848509,6.053485,9.182466,-9.807661,-3.860855,6.187763,4.132967,-6.199328,-5.526246,4.503547,6.188595,8.724002,-1.557355,8.597560,-2.236438,-0.193829,-1.884813,9.440017,3.135312,5.018780,-3.155891,-2.373543,2.817381,9.712058,-1.026146,0.191022,-5.976803,4.230796,-3.865678,-5.690538,3.099740,0.991249,-5.832347,-2.160595,-4.024230,4.339654,-5.891407,-1.631648,8.049604,-3.634360,-0.422313,6.697013,-0.936685,-5.256588,0.653605,2.979162,7.798582,-1.585066,-2.839382,2.397962,-8.360077,6.140560,-0.015783,8.322624,3.603677,-4.320307,9.203295,5.442067,-3.703700,-8.711864,-8.894708,-5.431479,-7.907704,-5.495864,0.784738,2.789426,-7.138658,3.959821,-9.511293,-0.577920,-4.600235,-2.913606,-5.429729,3.224830,6.706527,9.412263,1.509912,2.818199,-0.587812,-8.206092,4.525527,-7.875033,9.288028,-7.155301,-0.457394,7.956629,7.295089,-2.786737,4.674836,-8.226699,-7.051353,2.431928,-6.680496,4.694011], dtype = "float32")#candidate|7017|(880,)|const|float32
var_7018 = relay.var("var_7018", dtype = "int32", shape = (420, 2))#candidate|7018|(420, 2)|var|int32
const_7019 = relay.const([[6.013586,7.137957,-7.769037,-6.503838,2.277836,-0.810891,-7.351529,-6.225092,-9.321386,-3.794463,3.954557,-9.691730,8.613676,8.826436,-7.754713,-9.084034,-0.724660,-6.167371,5.989376,-6.146536,-4.118438,-2.259668,-1.232039,4.534029,9.158076,5.135969,-6.827610,-8.399400,-5.995060,-6.726005,-8.126858,-4.187894,-2.500415,-3.719129,2.884018,6.225020,1.598843,4.961043,-4.116400,8.825314,-9.258378,-8.113198,-2.980683,-8.019351,7.478717,2.865573,1.882334,-6.083614,9.545585,1.396887,2.096630,-3.993692,1.864620,7.997634,-2.462351,6.704236,2.877130,3.298739,-6.926326,-6.055531,-1.793732,1.855560,8.842259,-5.627792,-9.839334,-0.385774,-7.158066,0.732370,-8.797697,0.368271,5.905920,3.317145,-2.693693,-2.394628,-2.893378,-1.913129,8.243740,-4.953959,1.276131,2.961954,-3.491679,-6.717662,-5.544500,-8.866356,-7.413230,4.674716,-5.735479,-1.855739,8.366602,6.999807,-0.569111,3.535027,-8.198164,-7.278634,-7.326003,8.254128,9.531880,6.561239,0.267611,-2.896917,7.766070,1.826281,-3.813571,-5.985299,7.070141,5.305292,-6.594020,0.550341,-7.654746,-3.316754,4.288036,-1.543203,9.520297,-2.402391,4.000751,-3.835456,-5.782499,8.679692,-6.009969,-9.941747,6.338091,6.331457,-3.610298,-2.607293,-5.706852,3.717183,4.565113,9.996774,3.477157,1.564674,-2.056586,6.514299,-2.586226,-5.243151,1.104260,-9.800032,-5.804843,-4.280525,-3.801609,-6.126316,4.469628,-5.575558,9.750581,-6.622336,6.077950,1.722047,2.174870,-5.112666,1.549962,-8.605588,9.655242,-0.137070,-1.225855,4.926836,9.244970,-3.580846,0.035935,9.701440,-4.909460,-9.221876,-1.638341,9.871187,-6.138523,4.128014,-6.259137,-7.853401,-8.334594,-0.842198,9.391031,3.633956,6.313487,-6.902667,-9.387274,0.915009,7.179879,-4.952058,8.914223,5.462470,3.320236,-7.702247,2.097850,6.606700,3.506420,-0.020285,7.913977,2.645569,8.735247,-8.010609,-2.491272,-5.778839,7.192469,4.600905,5.971161,-8.700967,3.862583,-2.441821,-4.588195,-9.281510,8.644907,-4.736996,-9.547361,9.963389,1.672510,3.764001,7.539321,5.496857,-7.009307,-6.109788,-2.482311,-3.281425,8.725171,-2.485387,-2.505176,7.643127,0.602467,3.729554,3.308398,-4.039547,-2.024615,-9.646467,9.376211,-4.616421,-1.208816,6.258945,1.666919,-6.023192,7.926857,-9.331052,1.616607,9.729358,-1.090900,-2.488813,-6.432006,-8.724875,-3.310468,-3.333387,8.250608,9.008487,5.112083,-9.388810,-4.940801,2.773637,8.318686,-6.819179,1.152793,9.176030,-6.999656,-0.080271,-2.172409,1.881233,7.557178,9.992597,-4.208915,5.497253,0.801446,-7.497282,-7.583014,2.641096,-3.168362,7.829563,-1.428309,9.913735,-7.925880,1.557026,-8.531858,-2.054047,-0.971461,-5.051181,-2.160294,7.403200,8.816794,-5.630828,6.152545,7.415082,2.512847,-5.349336,-7.684382,-9.209769,6.552366,7.503725,-0.761948,1.946430,8.427546,4.983896,3.185636,-8.459235,-0.342463,2.331376,-5.663357,5.305088,4.590684,7.913472,0.653300,-9.801793,5.320002,1.991035,5.749503,3.041247,-8.345470,6.293817,6.413125,1.390789,-1.389056,0.121800,0.816220,-6.689256,-4.195929,-4.636488,2.488047,-4.418870,1.186114,-9.718662]], dtype = "float64")#candidate|7019|(1, 312)|const|float64
const_7020 = relay.const([-5.853950,8.514575,-9.196754,8.650980,7.927012,-0.095656,-2.792338,2.845285,-5.983048,-2.391111,8.114462,9.923368,-2.539840,6.061264,8.785597,-4.630902,2.416825,6.051578,-7.677753,-4.374833,7.923647,-4.713554,3.406071,2.551726,-3.585462,3.858419,-8.025588,-1.956710,-5.421531,-6.501513,-3.048664,6.931295,8.725490,-6.979067,-8.171191,8.050389,4.671635,3.439102,-2.600828,-7.052788,-5.305569,-0.008239,-3.519311,-3.441336,-9.011781,-0.194339,9.334580,3.257540,-1.621457,-9.284650,-8.766399,1.674741,9.437767,6.567971,1.184769,-3.107362,7.566389,-0.378395,3.256769,0.662916,-5.569258,9.855043,2.047741,-0.408329,-0.391318,-7.160204,-5.716637,-3.239507,-5.094287,2.424996,6.025694,-6.294717,-6.635481,6.008279,7.197826,-7.722239,-5.829724,7.684792,-7.690170,-8.083209,-7.821207,6.178994,-9.114410,-7.198950,9.834783,-9.905843,-8.720779,-7.436195,6.104395,-7.068644,-8.928547,-7.782864,-9.822832,-4.022609,4.613251,2.790793,-5.170388,1.592154,-7.624405,2.954131,2.416071,6.179521,-5.173495,3.451115,9.073690,-1.645172,-9.599727,-6.077618,-9.187754,7.507023,5.319358,9.848235,7.866726,-7.693621,8.106109,-4.382939,2.546781,-8.693387,8.684184,-6.431467,0.054951,-9.792911,1.964912,4.272897,8.282611,-5.329920,9.211918,-3.737846,-1.496938,4.663618,7.038140,-3.564343,4.552053,-4.100207,-5.722616,6.577737,-1.120261,7.693356,-9.836385,8.321479,2.237977,8.500228,-6.417727,-5.725671,-5.512175,-0.470484,9.310847,0.573244,2.259292,3.727092,-1.330809,9.024532,-1.514009,-3.666322,6.197358,-8.300562,6.344699,-6.820507,-0.265512,-1.782349,-4.466394,-0.051624,-8.541505,-8.549004,5.573762,6.326205,-8.806280,-9.142801,-8.783174,6.191125,9.555557,-1.112228,4.936948,-8.689194,5.576227,2.035310,0.428131,7.961348,1.663242,8.734312,4.946548,-0.967298,3.680100,-3.965285,1.731069,-6.447013,-3.373093,-5.127575,5.106461,2.487446,6.862463,-1.564770,-9.682918,-4.203725,9.488650,-2.791556,6.066037,-6.503611,-8.854474,-4.129849,-4.033318,-8.184767,9.313332,8.140999,0.945097,-8.927398,6.846540,6.086625,-8.474721,5.041324,2.367942,4.628603,-3.889712,0.841224,-6.160788,-0.671965,-9.139017,4.887256,6.427706,-0.862855,9.414254,-8.012938,5.709883,-9.896841,8.306573,4.236007,-4.130879,2.767762,-3.837081,4.904615,-1.972080,-2.300311,-5.463780,7.572726,-6.627259,-4.996787,-9.562789,-0.693976,-4.450204,5.245583,-2.740931,-6.706505,1.965371,0.833397,-9.971873,1.407235,-5.960524,-6.754638,1.878969,2.186860,1.310644,-3.744224,-9.106999,-5.696212,6.889325,-4.240414,-6.434297,-5.638411,6.554161,-8.855389,-9.778010,-9.995198,8.757495,2.352038,-6.479177,-1.688689,-9.994458,2.156666,4.756512,2.438510,-2.085606,-4.047180,-6.501350,-4.136482,-1.630707,-0.394263,-4.325074,9.471411,5.790324,0.947067,0.724754,4.820339,-3.531892,-7.895878,-9.807553,-3.338143,-5.426988,-8.997166,-6.219711,-3.178837,8.117466,5.253954,4.209201,1.898803,-0.751234,2.773093,-9.397769,6.716375,0.512218,-3.581301,-9.533217,-4.278111,6.703394,2.716700,-4.482754,-9.257151,-7.420982,2.121304,-3.915023,-2.241031,3.921497,4.082625,8.510068,-5.752980,-5.429325,-2.509457,-3.598760,4.710982,5.041442,3.529472,-5.982180,8.272230,1.894048,9.739560,3.542697,-4.342147,6.441431,-5.935598,7.592208,5.566160,4.288488,-5.675451,7.899575,5.095155,-4.599085,-4.067637,-0.674172,-2.033411,-6.381989,-3.037181,0.504468,9.440043,-3.787657,7.432683,-0.380930,1.291452,7.938453,1.280275,-1.010733,8.115035,8.019455,4.404456,-8.106210,-7.549213,9.977995,-9.426405,2.915222,7.099742,-3.367872,8.283154,-8.004679,-4.429420,-0.590880,-7.302115,7.241192,-2.697881,0.580485,-1.669607,1.929632,-6.160490,2.594486,2.844624,-2.621187,-6.533584,-2.383046,-2.825519,1.126372,-1.909547,-5.827319,-4.450536,-8.544093,4.225264,-5.926765,3.931241,-3.588792,9.535877,7.784483,-8.958410,4.205156,-7.477182,2.387640,-9.023644,0.721517,-0.179641,9.554088,8.833338,4.086398,6.787296,0.111665,6.541411,1.279816,8.160873,-5.882726,-7.138836,3.935480,1.304888,3.091006,2.082933,-9.506339,1.171216,-3.171574,7.554224,4.159010,6.925008,-8.048297,-5.388759,4.103227,-5.989810,2.938768,-9.040224,3.619250,4.381479,2.213978,6.702686,4.410914,-6.054528,-4.783912,3.079367,-7.228074,-7.598952,-8.122972,-5.221808,-9.426671,6.549965,-4.320870,-2.323245,9.509587,-8.105560,-3.766200,-1.197023,-4.021908,4.828321,-7.120464,-2.940167,-0.638257,9.670871,5.447195,-6.525811,-8.843811,-8.827002,6.393509,-1.781479,-3.048609,-8.227453,1.387915,-9.846247,2.595973,-2.847129,7.749697,-6.386491,3.632698,-5.349986], dtype = "float64")#candidate|7020|(462,)|const|float64
call_7016 = relay.TupleGetItem(func_6812_call(relay.reshape(const_7017.astype('float32'), [8, 110]), relay.reshape(var_7018.astype('int32'), [840,]), relay.reshape(const_7019.astype('float64'), [78, 4]), relay.reshape(const_7020.astype('float64'), [462,]), relay.reshape(const_7019.astype('int32'), [78, 4]), ), 14)
call_7021 = relay.TupleGetItem(func_6819_call(relay.reshape(const_7017.astype('float32'), [8, 110]), relay.reshape(var_7018.astype('int32'), [840,]), relay.reshape(const_7019.astype('float64'), [78, 4]), relay.reshape(const_7020.astype('float64'), [462,]), relay.reshape(const_7019.astype('int32'), [78, 4]), ), 14)
uop_7023 = relay.acosh(var_6987.astype('float64')) # shape=(10, 14, 14)
output = relay.Tuple([bop_7011,call_7016,const_7017,var_7018,const_7019,const_7020,uop_7023,])
output2 = relay.Tuple([bop_7011,call_7021,const_7017,var_7018,const_7019,const_7020,uop_7023,])
func_7026 = relay.Function([var_6986,var_6987,var_7018,], output)
mod['func_7026'] = func_7026
mod = relay.transform.InferType()(mod)
mutated_mod['func_7026'] = func_7026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7026_call = mutated_mod.get_global_var('func_7026')
var_7028 = relay.var("var_7028", dtype = "uint64", shape = ())#candidate|7028|()|var|uint64
var_7029 = relay.var("var_7029", dtype = "uint64", shape = (10, 14, 14))#candidate|7029|(10, 14, 14)|var|uint64
var_7030 = relay.var("var_7030", dtype = "int32", shape = (420, 2))#candidate|7030|(420, 2)|var|int32
call_7027 = func_7026_call(var_7028,var_7029,var_7030,)
output = call_7027
func_7031 = relay.Function([var_7028,var_7029,var_7030,], output)
mutated_mod['func_7031'] = func_7031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5833_call = mod.get_global_var('func_5833')
func_5834_call = mutated_mod.get_global_var('func_5834')
call_7044 = relay.TupleGetItem(func_5833_call(), 2)
call_7045 = relay.TupleGetItem(func_5834_call(), 2)
output = relay.Tuple([call_7044,])
output2 = relay.Tuple([call_7045,])
func_7080 = relay.Function([], output)
mod['func_7080'] = func_7080
mod = relay.transform.InferType()(mod)
mutated_mod['func_7080'] = func_7080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7080_call = mutated_mod.get_global_var('func_7080')
call_7081 = func_7080_call()
output = call_7081
func_7082 = relay.Function([], output)
mutated_mod['func_7082'] = func_7082
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7086 = relay.var("var_7086", dtype = "float32", shape = ())#candidate|7086|()|var|float32
const_7087 = relay.const([[[-1.668572,-6.200021,3.776991,-5.913987,-5.538299,5.630417],[2.300296,6.802466,2.013418,-4.860800,6.148624,-4.579683],[-8.573642,3.706665,4.533890,3.615937,-9.347995,-7.213078]],[[-2.973699,-0.347897,-3.380873,-0.739461,5.085335,7.972821],[-4.811012,3.149069,-2.479362,-1.751854,-2.584994,8.735648],[-2.150904,7.134913,9.843250,-6.138525,-4.226210,-6.730856]],[[-8.965977,4.619519,-9.140285,5.988566,-3.861642,-1.734731],[-5.199418,8.212328,8.012315,-5.102761,5.722205,-4.623560],[1.720680,-4.087582,9.114506,-5.757469,1.275849,4.271758]],[[-1.726022,8.078057,-4.509887,2.384873,-5.620273,6.084642],[-7.682329,8.836085,9.509802,-2.839204,8.730459,-5.524315],[8.135302,-7.679635,-6.787371,-0.929547,-7.216032,2.946571]],[[-5.699461,8.899518,-3.049345,-6.720065,-4.603618,-5.194756],[9.651085,7.514812,-7.561616,9.719620,-7.619253,-9.702028],[7.911550,-7.883058,-3.790581,-1.863863,-2.962131,3.265072]],[[-1.244023,5.397069,-8.732458,-6.028412,-3.599224,-5.540993],[-4.606220,-2.781229,8.438602,5.312889,-4.582504,3.582557],[-1.378749,0.540024,4.000335,0.813618,-4.290987,9.149846]]], dtype = "float32")#candidate|7087|(6, 3, 6)|const|float32
bop_7088 = relay.subtract(var_7086.astype('float32'), const_7087.astype('float32')) # shape=(6, 3, 6)
output = relay.Tuple([bop_7088,])
output2 = relay.Tuple([bop_7088,])
func_7095 = relay.Function([var_7086,], output)
mod['func_7095'] = func_7095
mod = relay.transform.InferType()(mod)
mutated_mod['func_7095'] = func_7095
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7096 = relay.var("var_7096", dtype = "float32", shape = ())#candidate|7096|()|var|float32
func_7095_call = mutated_mod.get_global_var('func_7095')
call_7097 = func_7095_call(var_7096)
output = call_7097
func_7098 = relay.Function([var_7096], output)
mutated_mod['func_7098'] = func_7098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3437_call = mod.get_global_var('func_3437')
func_3438_call = mutated_mod.get_global_var('func_3438')
call_7136 = relay.TupleGetItem(func_3437_call(), 0)
call_7137 = relay.TupleGetItem(func_3438_call(), 0)
func_2854_call = mod.get_global_var('func_2854')
func_2856_call = mutated_mod.get_global_var('func_2856')
call_7138 = relay.TupleGetItem(func_2854_call(), 0)
call_7139 = relay.TupleGetItem(func_2856_call(), 0)
func_7026_call = mod.get_global_var('func_7026')
func_7031_call = mutated_mod.get_global_var('func_7031')
var_7141 = relay.var("var_7141", dtype = "uint64", shape = ())#candidate|7141|()|var|uint64
const_7142 = relay.const([-2,-9,-2,-3,-9,7,1,-10,6,9,-4,10,7,-2,-4,3,1,-8,-8,3,2,-7,-7,-9,-1,-4,3,10,7,6,6,-9,1,9,8,7,1,-4,1,3,4,-6,1,-6,-7,-2,-2,-9,6,-4,-1,6,-5,2,6,9,-3,6,10,-4,6,1,7,-3,-7,1,8,-9,8,10,-7,3,-3,-3,4,-9,3,10,-9,5,2,3,3,-2,5,6,-10,-9,-9,5,2,-4,5,7,7,-9,7,-8,7,-3,3,-4,8,7,8,1,-7,4,-10,-3,2,5,-5,10,-4,-4,-2,-9,2,2,-9,9,-9,-5,6,6,-1,9,-4,10,4,5,10,10,2,-3,4,-5,7,-2,2,-2,8,1,-2,10,-4,-6,10,8,6,3,3,3,-1,-2,-4,6,-8,4,7,-8,2,5,7,-4,-5,5,8,-6,4,10,4,9,-2,-2,8,9,-1,2,10,-3,6,4,5,-10,10,6,-5,-4,8,5,-3,6,3,-3,5,-9,-3,4,5,-8,4,-6,9,-6,-5,4,9,5,-9,4,-6,6,8,-9,2,7,-3,6,5,8,-5,2,-4,6,5,9,7,-1,5,-9,9,-4,-10,-4,-2,-7,-5,-3,-3,-2,2,-2,-7,7,4,9,-1,8,3,8,-4,-4,-3,-10,9,7,-3,2,1,-2,-5,-10,5,-8,2,8,1,7,-1,10,-8,1,5,1,-3,3,-5,-4,3,-3,-10,-2,-2,-6,-7,3,5,-7,1,8,-3,2,6,-2,-2,5,-3,4,6,-8,-6,8,-9,2,5,4,1,-7,3,-5,4,6,6,5,-8,7,-8,-5,-2,-6,9,6,-5,-6,-4,-3,2,8,-7,-2,-7,-1,5,-1,7,3,-5,-5,-2,9,3,-4,1,-2,6,5,2,10,4,-4,9,6,-6,6,-5,6,9,2,4,8,10,5,9,-9,9,5,-1,-1,3,7,-4,-5,-2,1,-5,-10,-2,4,2,-8,7,6,4,4,-7,-7,-1,4,-3,3,-5,10,-8,1,-10,-1,-2,-4,6,-8,-7,6,1,-5,-6,-2,-9,-8,-1,-9,10,7,-8,-10,8,-9,-3,5,6,8,-6,1,-5,6,-2,6,-4,-3,5,-7,9,8,-3,-6,2,-9,2,-8,2,2,9,-5,-10,-5,2,-8,10,-5,-8,1,4,-10,1,3,2,-7,-5,3,-3,-2,2,7,5,-4,2,-7,-5,-3,5,-10,-3,-7,1,4,10,-8,8,-4,-5,8,-4,-4,-1,5,-2,2,-6,-4,1,-1,-5,-5,4,6,8,9,-10,-2,9,-9,-4,6,2,-9,9,-7,-10,-9,-2,4,-10,3,-7,3,2,-6,-2,8,-6,8,6,-2,-8,1,-8,1,9,10,-8,-3,-2,1,-3,8,6,7,-1,-10,-1,-8,-7,7,-2,-3,7,-5,5,4,4,7,10,-4,2,8,5,10,-5,-8,-3,1,7,10,-1,9,-8,5,-2,-9,-3,8,4,-1,-7,8,-2,-2,5,2,-8,-9,-9,6,-3,6,1,7,-3,4,9,-2,1,1,-7,1,-4,-4,5,2,3,6,-1,-9,1,-4,7,1,-9,-5,-5,-4,7,10,7,1,-2,-6,-2,-9,8,3,-1,-5,-9,7,-5,1,-8,-5,4,7,-5,-3,5,9,-7,-3,1,7,6,-1,6,6,-4,-8,-7,6,-5,-8,-1,8,-3,6,-8,-3,-8,7,6,-7,4,-1,-10,2,8,-10,1,8,-8,10,-7,10,7,9,-1,-6,-2,6,5,-1,-2,-5,8,8,6,-2,1,10,1,1,-6,9,-5,-3,-4,7,-3,10,-6,9,-8,-6,-5,7,6,8,-7,3,3,-6,10,3,-6,7,3,3,-7,10,-7,-7,-5,6,-3,7,5,-3,9,-10,-10,6,-1,7,-9,-1,4,-1,5,4,-6,-4,-4,-10,4,7,-5,1,3,-7,5,-1,5,9,-7,8,1,8,10,10,8,-1,-10,10,-10,-8,-4,-5,8,7,-4,1,-8,5,-7,-5,2,-7,-8,-8,5,-5,-2,5,2,-5,10,6,-7,7,5,10,-8,2,5,6,5,-8,-10,6,7,-10,9,5,6,9,-4,1,-7,9,4,-1,-5,-5,-4,-8,-4,7,6,-9,-4,8,-7,-3,3,-8,5,7,10,6,-4,-4,7,-2,-3,-7,-9,-8,-5,3,-1,4,-10,-8,2,-4,-10,-7,-2,-10,-9,-4,4,-9,3,7,-2,-1,-4,5,-5,-4,-1,-4,1,-8,4,3,3,9,3,-1,-10,9,3,2,7,7,-1,1,-8,4,-10,-2,-8,-1,8,6,-4,4,1,5,3,5,2,6,4,2,7,-9,4,6,1,9,-6,-3,8,4,2,5,-7,4,3,9,1,-6,9,-6,-1,6,-10,6,-8,1,-2,-4,9,4,7,3,1,-2,9,-1,-6,10,9,-6,-8,7,-3,-1,-10,-4,10,4,7,2,-5,-10,3,7,-8,8,-9,-6,-7,-5,-3,5,-8,-5,-4,-3,-1,2,-3,-3,-1,4,8,-2,-6,10,-8,3,4,3,2,-1,-8,-6,-1,1,1,-9,7,2,8,3,8,4,-1,-4,-2,7,-5,3,3,7,1,-5,-9,2,-10,5,-2,-2,5,-7,8,-1,8,-8,-9,-6,-2,9,-7,-7,9,-7,-1,3,4,7,5,-8,1,3,-2,10,-10,-3,3,4,-4,-2,-9,-2,-4,-8,6,-1,1,-5,-3,-4,6,-7,-9,-1,-1,7,8,4,10,-1,7,1,6,-10,-3,-1,2,-5,1,4,-9,-4,2,-8,-10,-9,1,-5,-8,-7,9,-7,5,2,10,-8,8,-5,-9,-5,2,-6,-5,-3,3,-1,5,3,-2,6,2,-2,-5,3,1,-5,-3,7,1,9,9,8,10,4,8,-5,-5,5,3,5,7,9,10,-7,6,-7,-6,9,-6,-7,4,-9,8,-10,-1,6,-5,-7,1,-8,-10,3,9,3,4,2,-3,-8,6,-1,-5,6,-2,-6,6,1,8,5,6,3,-9,10,7,-2,-6,-9,-10,10,7,-4,-10,1,6,5,4,-4,2,-5,-1,-3,10,9,-6,-1,-7,-8,-9,-6,6,9,-7,3,6,-10,4,6,-5,1,6,-6,6,-1,-6,-2,-6,10,-3,-5,-2,-5,-8,8,6,7,-3,4,-1,-6,1,7,2,-3,2,-3,-6,-1,-9,-10,-10,6,1,3,-4,9,1,-3,3,8,-5,-2,-1,-7,-9,7,3,-3,3,6,-8,-3,1,2,3,1,-2,10,3,-4,-2,4,-4,10,4,7,3,3,-7,7,-4,7,-1,-9,-4,-1,-2,2,3,-3,1,10,-1,5,-7,-5,1,7,9,-8,-7,-9,-3,6,4,2,-1,-9,-5,-8,7,3,5,1,6,-7,6,3,-9,-5,8,8,2,-10,2,-7,-1,-8,-10,10,-8,-8,-5,4,-8,6,-8,5,-4,5,1,4,4,-8,-2,-2,-5,5,-1,-3,9,7,6,5,5,3,-6,9,2,6,-6,-2,-9,3,5,-9,7,-10,-5,10,-9,-7,-3,-4,-4,9,-9,2,-6,-7,3,5,-9,-3,-4,-6,8,-5,-10,8,-3,3,-5,-9,-10,-6,-2,2,-8,8,8,2,-7,-8,9,-2,-10,2,10,10,10,4,7,-3,-9,-6,7,4,6,-3,-8,5,2,5,3,-3,-1,2,10,-2,8,-7,-5,-9,3,-6,-8,8,10,-1,1,3,10,-10,3,-3,-2,-8,-1,8,10,2,-4,-10,-6,-5,-7,-8,6,-9,-4,1,-3,2,7,-8,5,7,-2,4,-9,2,-9,-5,10,5,-6,-9,7,-3,-5,-3,10,-2,8,10,-8,7,5,-4,8,1,10,-5,5,-3,-10,5,-6,-4,-4,4,-7,1,1,-10,-7,-4,-5,3,-8,4,-3,-8,5,-3,-6,-3,6,-6,-7,7,-1,10,10,8,10,-4,9,1,-3,3,9,-2,-7,-3,9,10,-9,-6,2,6,3,6,-3,-6,-9,-8,4,-5,-10,-7,6,-9,-8,5,8,-3,-5,-3,-3,-7,-7,-5,4,-3,-8,-3,10,3,-6,7,2,-5,8,-5,4,-7,6,-3,4,5,10,8,10,9,10,2,-7,-8,4,8,-7,10,-9,-4,-10,-4,-4,2,2,4,7,-5,-4,9,-8,5,-4,-1,-9,-5,-1,-1,1,-1,-3,6,-2,4,6,3,10,1,4,-8,-4,-3,-4,-2,-6,-10,9,-8,-7,-8,-6,6,2,2,9,10,-5,-8,7,-3,-4,-1,9,5,-4,10,5,-5,-5,-2,1,10,5,4,-10,5,10,-5,9,-8,5,2,5,-7,-6,-7,-9,4,4,5,5,-6,-8,-7,-2,-10,2,-7,9,7,2,-4,-8,-6,4,-6,3,-7,4,-10,8,5,1,-5,7,6,6,10,-8,-8,-8,-3,-8,-6,6,-1,5,4,-10,-6,3,-4,-2,6,-1,-4,1,-3,-10,1,4,-10,-10,5,-5,6,-5,-8,-9,8,-9,10,-10,8,4,5,5,-7,2,-4,-6,-7,-5,7,1,3,-8,1,7,-7,3,1,9,-3,-1,-2,-9,8,-7,-5,2,10,2,9,5,2,-8,-5,10,-2,5,10,2,-6,-6,-7,3,-10,1,6,-5,-3,1,4,6,-6,9,-2,5,9,-3,2,6,-10,-3,-2,-5,3,-4,1,2,-8,-3,-1,-2,-2,7,-10,-7,-9,-7,9,7,-9,-9,-9,-8,-4,-1,3,-5,8,-10,4,-7,10,-3,5,10,-1,6,4,8,9,10,3,-9,-7,7,10,4,9,6,-9,2,7,-9,4,-8,-9,4,-2,-2,6,10,-7,-4,4,-2,8,3,2,8,-1,6,3,-1,5,-5,5,4,10,8,-10,6,-4,5,3,9,-10,-4,-7,9,10,-4,1,-7,-8,6,-7,5,-3,5,-4,10,1,8,-10,-1,-2,7,3,-6,-1,8,-5,9,-5,-4,1,4,9,-10,-10,-9,-6,-6,2,-9,-4,-1,1,-9,-4,-5,8,-5,-3,5,-5,-6,1,-9,5,6,-4,10,-4,-2,-3,-1,8,5,-2,3,-5,8,2,-10,5,6,-2,-7,-5,-5,5,9,-4,5,5,3,6,9,-1,4,-5,-9,9,3,4], dtype = "uint64")#candidate|7142|(1960,)|const|uint64
var_7143 = relay.var("var_7143", dtype = "int32", shape = (840,))#candidate|7143|(840,)|var|int32
call_7140 = relay.TupleGetItem(func_7026_call(relay.reshape(var_7141.astype('uint64'), []), relay.reshape(const_7142.astype('uint64'), [10, 14, 14]), relay.reshape(var_7143.astype('int32'), [420, 2]), ), 1)
call_7144 = relay.TupleGetItem(func_7031_call(relay.reshape(var_7141.astype('uint64'), []), relay.reshape(const_7142.astype('uint64'), [10, 14, 14]), relay.reshape(var_7143.astype('int32'), [420, 2]), ), 1)
output = relay.Tuple([call_7136,call_7138,call_7140,var_7141,const_7142,var_7143,])
output2 = relay.Tuple([call_7137,call_7139,call_7144,var_7141,const_7142,var_7143,])
func_7148 = relay.Function([var_7141,var_7143,], output)
mod['func_7148'] = func_7148
mod = relay.transform.InferType()(mod)
var_7149 = relay.var("var_7149", dtype = "uint64", shape = ())#candidate|7149|()|var|uint64
var_7150 = relay.var("var_7150", dtype = "int32", shape = (840,))#candidate|7150|(840,)|var|int32
output = func_7148(var_7149,var_7150,)
func_7151 = relay.Function([var_7149,var_7150,], output)
mutated_mod['func_7151'] = func_7151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3437_call = mod.get_global_var('func_3437')
func_3438_call = mutated_mod.get_global_var('func_3438')
call_7209 = relay.TupleGetItem(func_3437_call(), 0)
call_7210 = relay.TupleGetItem(func_3438_call(), 0)
output = relay.Tuple([call_7209,])
output2 = relay.Tuple([call_7210,])
func_7226 = relay.Function([], output)
mod['func_7226'] = func_7226
mod = relay.transform.InferType()(mod)
mutated_mod['func_7226'] = func_7226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7226_call = mutated_mod.get_global_var('func_7226')
call_7227 = func_7226_call()
output = call_7227
func_7228 = relay.Function([], output)
mutated_mod['func_7228'] = func_7228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4588_call = mod.get_global_var('func_4588')
func_4589_call = mutated_mod.get_global_var('func_4589')
call_7364 = relay.TupleGetItem(func_4588_call(), 0)
call_7365 = relay.TupleGetItem(func_4589_call(), 0)
output = relay.Tuple([call_7364,])
output2 = relay.Tuple([call_7365,])
func_7378 = relay.Function([], output)
mod['func_7378'] = func_7378
mod = relay.transform.InferType()(mod)
mutated_mod['func_7378'] = func_7378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7378_call = mutated_mod.get_global_var('func_7378')
call_7379 = func_7378_call()
output = call_7379
func_7380 = relay.Function([], output)
mutated_mod['func_7380'] = func_7380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6505_call = mod.get_global_var('func_6505')
func_6507_call = mutated_mod.get_global_var('func_6507')
call_7402 = relay.TupleGetItem(func_6505_call(), 1)
call_7403 = relay.TupleGetItem(func_6507_call(), 1)
output = relay.Tuple([call_7402,])
output2 = relay.Tuple([call_7403,])
func_7407 = relay.Function([], output)
mod['func_7407'] = func_7407
mod = relay.transform.InferType()(mod)
mutated_mod['func_7407'] = func_7407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7407_call = mutated_mod.get_global_var('func_7407')
call_7408 = func_7407_call()
output = call_7408
func_7409 = relay.Function([], output)
mutated_mod['func_7409'] = func_7409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4654_call = mod.get_global_var('func_4654')
func_4655_call = mutated_mod.get_global_var('func_4655')
call_7423 = relay.TupleGetItem(func_4654_call(), 1)
call_7424 = relay.TupleGetItem(func_4655_call(), 1)
output = relay.Tuple([call_7423,])
output2 = relay.Tuple([call_7424,])
func_7433 = relay.Function([], output)
mod['func_7433'] = func_7433
mod = relay.transform.InferType()(mod)
output = func_7433()
func_7434 = relay.Function([], output)
mutated_mod['func_7434'] = func_7434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3437_call = mod.get_global_var('func_3437')
func_3438_call = mutated_mod.get_global_var('func_3438')
call_7445 = relay.TupleGetItem(func_3437_call(), 0)
call_7446 = relay.TupleGetItem(func_3438_call(), 0)
output = call_7445
output2 = call_7446
func_7447 = relay.Function([], output)
mod['func_7447'] = func_7447
mod = relay.transform.InferType()(mod)
output = func_7447()
func_7448 = relay.Function([], output)
mutated_mod['func_7448'] = func_7448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_7478 = relay.TupleGetItem(func_928_call(), 1)
call_7479 = relay.TupleGetItem(func_930_call(), 1)
output = call_7478
output2 = call_7479
func_7485 = relay.Function([], output)
mod['func_7485'] = func_7485
mod = relay.transform.InferType()(mod)
output = func_7485()
func_7486 = relay.Function([], output)
mutated_mod['func_7486'] = func_7486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7407_call = mod.get_global_var('func_7407')
func_7409_call = mutated_mod.get_global_var('func_7409')
call_7523 = relay.TupleGetItem(func_7407_call(), 0)
call_7524 = relay.TupleGetItem(func_7409_call(), 0)
output = call_7523
output2 = call_7524
func_7529 = relay.Function([], output)
mod['func_7529'] = func_7529
mod = relay.transform.InferType()(mod)
mutated_mod['func_7529'] = func_7529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7529_call = mutated_mod.get_global_var('func_7529')
call_7530 = func_7529_call()
output = call_7530
func_7531 = relay.Function([], output)
mutated_mod['func_7531'] = func_7531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1762_call = mod.get_global_var('func_1762')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_7630 = func_1762_call()
call_7631 = func_1762_call()
output = call_7630
output2 = call_7631
func_7635 = relay.Function([], output)
mod['func_7635'] = func_7635
mod = relay.transform.InferType()(mod)
mutated_mod['func_7635'] = func_7635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7635_call = mutated_mod.get_global_var('func_7635')
call_7636 = func_7635_call()
output = call_7636
func_7637 = relay.Function([], output)
mutated_mod['func_7637'] = func_7637
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7689 = relay.var("var_7689", dtype = "int64", shape = (14, 12, 2))#candidate|7689|(14, 12, 2)|var|int64
var_7690 = relay.var("var_7690", dtype = "int64", shape = (14, 12, 2))#candidate|7690|(14, 12, 2)|var|int64
bop_7691 = relay.greater(var_7689.astype('bool'), relay.reshape(var_7690.astype('bool'), relay.shape_of(var_7689))) # shape=(14, 12, 2)
output = bop_7691
output2 = bop_7691
func_7698 = relay.Function([var_7689,var_7690,], output)
mod['func_7698'] = func_7698
mod = relay.transform.InferType()(mod)
var_7699 = relay.var("var_7699", dtype = "int64", shape = (14, 12, 2))#candidate|7699|(14, 12, 2)|var|int64
var_7700 = relay.var("var_7700", dtype = "int64", shape = (14, 12, 2))#candidate|7700|(14, 12, 2)|var|int64
output = func_7698(var_7699,var_7700,)
func_7701 = relay.Function([var_7699,var_7700,], output)
mutated_mod['func_7701'] = func_7701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5874_call = mod.get_global_var('func_5874')
func_5875_call = mutated_mod.get_global_var('func_5875')
call_7730 = func_5874_call()
call_7731 = func_5874_call()
output = relay.Tuple([call_7730,])
output2 = relay.Tuple([call_7731,])
func_7732 = relay.Function([], output)
mod['func_7732'] = func_7732
mod = relay.transform.InferType()(mod)
mutated_mod['func_7732'] = func_7732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7732_call = mutated_mod.get_global_var('func_7732')
call_7733 = func_7732_call()
output = call_7733
func_7734 = relay.Function([], output)
mutated_mod['func_7734'] = func_7734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4022_call = mod.get_global_var('func_4022')
func_4023_call = mutated_mod.get_global_var('func_4023')
call_7735 = relay.TupleGetItem(func_4022_call(), 0)
call_7736 = relay.TupleGetItem(func_4023_call(), 0)
output = relay.Tuple([call_7735,])
output2 = relay.Tuple([call_7736,])
func_7737 = relay.Function([], output)
mod['func_7737'] = func_7737
mod = relay.transform.InferType()(mod)
mutated_mod['func_7737'] = func_7737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7737_call = mutated_mod.get_global_var('func_7737')
call_7738 = func_7737_call()
output = call_7738
func_7739 = relay.Function([], output)
mutated_mod['func_7739'] = func_7739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_234_call = mod.get_global_var('func_234')
func_236_call = mutated_mod.get_global_var('func_236')
call_7750 = func_234_call()
call_7751 = func_234_call()
output = relay.Tuple([call_7750,])
output2 = relay.Tuple([call_7751,])
func_7754 = relay.Function([], output)
mod['func_7754'] = func_7754
mod = relay.transform.InferType()(mod)
mutated_mod['func_7754'] = func_7754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7754_call = mutated_mod.get_global_var('func_7754')
call_7755 = func_7754_call()
output = call_7755
func_7756 = relay.Function([], output)
mutated_mod['func_7756'] = func_7756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1292_call = mod.get_global_var('func_1292')
func_1294_call = mutated_mod.get_global_var('func_1294')
call_7762 = relay.TupleGetItem(func_1292_call(), 0)
call_7763 = relay.TupleGetItem(func_1294_call(), 0)
func_2684_call = mod.get_global_var('func_2684')
func_2686_call = mutated_mod.get_global_var('func_2686')
call_7767 = relay.TupleGetItem(func_2684_call(), 0)
call_7768 = relay.TupleGetItem(func_2686_call(), 0)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_7773 = func_2294_call()
call_7774 = func_2294_call()
output = relay.Tuple([call_7762,call_7767,call_7773,])
output2 = relay.Tuple([call_7763,call_7768,call_7774,])
func_7789 = relay.Function([], output)
mod['func_7789'] = func_7789
mod = relay.transform.InferType()(mod)
output = func_7789()
func_7790 = relay.Function([], output)
mutated_mod['func_7790'] = func_7790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2004_call = mod.get_global_var('func_2004')
func_2006_call = mutated_mod.get_global_var('func_2006')
call_7810 = relay.TupleGetItem(func_2004_call(), 0)
call_7811 = relay.TupleGetItem(func_2006_call(), 0)
output = relay.Tuple([call_7810,])
output2 = relay.Tuple([call_7811,])
func_7819 = relay.Function([], output)
mod['func_7819'] = func_7819
mod = relay.transform.InferType()(mod)
output = func_7819()
func_7820 = relay.Function([], output)
mutated_mod['func_7820'] = func_7820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4719_call = mod.get_global_var('func_4719')
func_4720_call = mutated_mod.get_global_var('func_4720')
call_7825 = relay.TupleGetItem(func_4719_call(), 2)
call_7826 = relay.TupleGetItem(func_4720_call(), 2)
func_3437_call = mod.get_global_var('func_3437')
func_3438_call = mutated_mod.get_global_var('func_3438')
call_7854 = relay.TupleGetItem(func_3437_call(), 0)
call_7855 = relay.TupleGetItem(func_3438_call(), 0)
output = relay.Tuple([call_7825,call_7854,])
output2 = relay.Tuple([call_7826,call_7855,])
func_7856 = relay.Function([], output)
mod['func_7856'] = func_7856
mod = relay.transform.InferType()(mod)
mutated_mod['func_7856'] = func_7856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7856_call = mutated_mod.get_global_var('func_7856')
call_7857 = func_7856_call()
output = call_7857
func_7858 = relay.Function([], output)
mutated_mod['func_7858'] = func_7858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7732_call = mod.get_global_var('func_7732')
func_7734_call = mutated_mod.get_global_var('func_7734')
call_7869 = relay.TupleGetItem(func_7732_call(), 0)
call_7870 = relay.TupleGetItem(func_7734_call(), 0)
func_7819_call = mod.get_global_var('func_7819')
func_7820_call = mutated_mod.get_global_var('func_7820')
call_7875 = relay.TupleGetItem(func_7819_call(), 0)
call_7876 = relay.TupleGetItem(func_7820_call(), 0)
func_207_call = mod.get_global_var('func_207')
func_209_call = mutated_mod.get_global_var('func_209')
call_7912 = relay.TupleGetItem(func_207_call(), 0)
call_7913 = relay.TupleGetItem(func_209_call(), 0)
output = relay.Tuple([call_7869,call_7875,call_7912,])
output2 = relay.Tuple([call_7870,call_7876,call_7913,])
func_7914 = relay.Function([], output)
mod['func_7914'] = func_7914
mod = relay.transform.InferType()(mod)
output = func_7914()
func_7915 = relay.Function([], output)
mutated_mod['func_7915'] = func_7915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1545_call = mod.get_global_var('func_1545')
func_1547_call = mutated_mod.get_global_var('func_1547')
call_7942 = func_1545_call()
call_7943 = func_1545_call()
func_6188_call = mod.get_global_var('func_6188')
func_6191_call = mutated_mod.get_global_var('func_6191')
var_7951 = relay.var("var_7951", dtype = "float32", shape = (990, 2))#candidate|7951|(990, 2)|var|float32
call_7950 = relay.TupleGetItem(func_6188_call(relay.reshape(var_7951.astype('float32'), [1980,])), 3)
call_7952 = relay.TupleGetItem(func_6191_call(relay.reshape(var_7951.astype('float32'), [1980,])), 3)
output = relay.Tuple([call_7942,call_7950,var_7951,])
output2 = relay.Tuple([call_7943,call_7952,var_7951,])
func_7961 = relay.Function([var_7951,], output)
mod['func_7961'] = func_7961
mod = relay.transform.InferType()(mod)
mutated_mod['func_7961'] = func_7961
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7962 = relay.var("var_7962", dtype = "float32", shape = (990, 2))#candidate|7962|(990, 2)|var|float32
func_7961_call = mutated_mod.get_global_var('func_7961')
call_7963 = func_7961_call(var_7962)
output = call_7963
func_7964 = relay.Function([var_7962], output)
mutated_mod['func_7964'] = func_7964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5705_call = mod.get_global_var('func_5705')
func_5707_call = mutated_mod.get_global_var('func_5707')
call_7969 = relay.TupleGetItem(func_5705_call(), 1)
call_7970 = relay.TupleGetItem(func_5707_call(), 1)
func_2636_call = mod.get_global_var('func_2636')
func_2638_call = mutated_mod.get_global_var('func_2638')
call_8009 = relay.TupleGetItem(func_2636_call(), 1)
call_8010 = relay.TupleGetItem(func_2638_call(), 1)
output = relay.Tuple([call_7969,call_8009,])
output2 = relay.Tuple([call_7970,call_8010,])
func_8016 = relay.Function([], output)
mod['func_8016'] = func_8016
mod = relay.transform.InferType()(mod)
mutated_mod['func_8016'] = func_8016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8017 = func_8016_call()
output = call_8017
func_8018 = relay.Function([], output)
mutated_mod['func_8018'] = func_8018
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8021 = relay.var("var_8021", dtype = "float64", shape = (11, 3, 15))#candidate|8021|(11, 3, 15)|var|float64
var_8022 = relay.var("var_8022", dtype = "float64", shape = (11, 3, 15))#candidate|8022|(11, 3, 15)|var|float64
bop_8023 = relay.floor_mod(var_8021.astype('float64'), relay.reshape(var_8022.astype('float64'), relay.shape_of(var_8021))) # shape=(11, 3, 15)
uop_8039 = relay.asin(var_8022.astype('float32')) # shape=(11, 3, 15)
func_7856_call = mod.get_global_var('func_7856')
func_7858_call = mutated_mod.get_global_var('func_7858')
call_8041 = relay.TupleGetItem(func_7856_call(), 0)
call_8042 = relay.TupleGetItem(func_7858_call(), 0)
var_8045 = relay.var("var_8045", dtype = "float64", shape = (11, 3, 15))#candidate|8045|(11, 3, 15)|var|float64
bop_8046 = relay.mod(var_8021.astype('float32'), relay.reshape(var_8045.astype('float32'), relay.shape_of(var_8021))) # shape=(11, 3, 15)
var_8049 = relay.var("var_8049", dtype = "float64", shape = (11, 3, 15))#candidate|8049|(11, 3, 15)|var|float64
bop_8050 = relay.less(var_8022.astype('bool'), relay.reshape(var_8049.astype('bool'), relay.shape_of(var_8022))) # shape=(11, 3, 15)
output = relay.Tuple([bop_8023,uop_8039,call_8041,bop_8046,bop_8050,])
output2 = relay.Tuple([bop_8023,uop_8039,call_8042,bop_8046,bop_8050,])
func_8055 = relay.Function([var_8021,var_8022,var_8045,var_8049,], output)
mod['func_8055'] = func_8055
mod = relay.transform.InferType()(mod)
mutated_mod['func_8055'] = func_8055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8055_call = mutated_mod.get_global_var('func_8055')
var_8057 = relay.var("var_8057", dtype = "float64", shape = (11, 3, 15))#candidate|8057|(11, 3, 15)|var|float64
var_8058 = relay.var("var_8058", dtype = "float64", shape = (11, 3, 15))#candidate|8058|(11, 3, 15)|var|float64
var_8059 = relay.var("var_8059", dtype = "float64", shape = (11, 3, 15))#candidate|8059|(11, 3, 15)|var|float64
var_8060 = relay.var("var_8060", dtype = "float64", shape = (11, 3, 15))#candidate|8060|(11, 3, 15)|var|float64
call_8056 = func_8055_call(var_8057,var_8058,var_8059,var_8060,)
output = call_8056
func_8061 = relay.Function([var_8057,var_8058,var_8059,var_8060,], output)
mutated_mod['func_8061'] = func_8061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7407_call = mod.get_global_var('func_7407')
func_7409_call = mutated_mod.get_global_var('func_7409')
call_8068 = relay.TupleGetItem(func_7407_call(), 0)
call_8069 = relay.TupleGetItem(func_7409_call(), 0)
func_3091_call = mod.get_global_var('func_3091')
func_3092_call = mutated_mod.get_global_var('func_3092')
call_8087 = func_3091_call()
call_8088 = func_3091_call()
func_4210_call = mod.get_global_var('func_4210')
func_4211_call = mutated_mod.get_global_var('func_4211')
call_8097 = func_4210_call()
call_8098 = func_4210_call()
output = relay.Tuple([call_8068,call_8087,call_8097,])
output2 = relay.Tuple([call_8069,call_8088,call_8098,])
func_8109 = relay.Function([], output)
mod['func_8109'] = func_8109
mod = relay.transform.InferType()(mod)
output = func_8109()
func_8110 = relay.Function([], output)
mutated_mod['func_8110'] = func_8110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3923_call = mod.get_global_var('func_3923')
func_3925_call = mutated_mod.get_global_var('func_3925')
call_8177 = func_3923_call()
call_8178 = func_3923_call()
func_6115_call = mod.get_global_var('func_6115')
func_6117_call = mutated_mod.get_global_var('func_6117')
call_8231 = func_6115_call()
call_8232 = func_6115_call()
output = relay.Tuple([call_8177,call_8231,])
output2 = relay.Tuple([call_8178,call_8232,])
func_8247 = relay.Function([], output)
mod['func_8247'] = func_8247
mod = relay.transform.InferType()(mod)
output = func_8247()
func_8248 = relay.Function([], output)
mutated_mod['func_8248'] = func_8248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2636_call = mod.get_global_var('func_2636')
func_2638_call = mutated_mod.get_global_var('func_2638')
call_8304 = relay.TupleGetItem(func_2636_call(), 0)
call_8305 = relay.TupleGetItem(func_2638_call(), 0)
func_4928_call = mod.get_global_var('func_4928')
func_4932_call = mutated_mod.get_global_var('func_4932')
const_8330 = relay.const([[-2,-6,-3,-7,6,9,4,4,-8],[2,9,-6,-3,8,10,6,3,10],[-10,4,-5,-4,2,8,8,7,-10],[-8,9,-10,10,-1,-8,8,8,-4],[4,-1,5,-6,9,-2,-6,4,8],[4,-10,10,8,5,-9,10,-4,-10],[2,2,9,2,4,-3,-8,10,-4],[5,8,7,-7,-3,-9,2,8,1],[-7,3,9,-6,4,6,-8,-9,8]], dtype = "uint64")#candidate|8330|(9, 9)|const|uint64
var_8331 = relay.var("var_8331", dtype = "float32", shape = (16, 6))#candidate|8331|(16, 6)|var|float32
call_8329 = relay.TupleGetItem(func_4928_call(relay.reshape(const_8330.astype('uint64'), [9, 3, 3]), relay.reshape(const_8330.astype('uint64'), [9, 3, 3]), relay.reshape(var_8331.astype('float32'), [96,]), ), 1)
call_8332 = relay.TupleGetItem(func_4932_call(relay.reshape(const_8330.astype('uint64'), [9, 3, 3]), relay.reshape(const_8330.astype('uint64'), [9, 3, 3]), relay.reshape(var_8331.astype('float32'), [96,]), ), 1)
func_3281_call = mod.get_global_var('func_3281')
func_3283_call = mutated_mod.get_global_var('func_3283')
call_8350 = relay.TupleGetItem(func_3281_call(), 0)
call_8351 = relay.TupleGetItem(func_3283_call(), 0)
func_2433_call = mod.get_global_var('func_2433')
func_2434_call = mutated_mod.get_global_var('func_2434')
call_8356 = func_2433_call()
call_8357 = func_2433_call()
func_5197_call = mod.get_global_var('func_5197')
func_5202_call = mutated_mod.get_global_var('func_5202')
var_8363 = relay.var("var_8363", dtype = "float32", shape = (1001,))#candidate|8363|(1001,)|var|float32
call_8362 = relay.TupleGetItem(func_5197_call(relay.reshape(const_8330.astype('uint64'), [81,]), relay.reshape(var_8331.astype('float32'), [96,]), relay.reshape(var_8363.astype('float32'), [1001, 1]), relay.reshape(call_8329.astype('float32'), [81,]), ), 0)
call_8364 = relay.TupleGetItem(func_5202_call(relay.reshape(const_8330.astype('uint64'), [81,]), relay.reshape(var_8331.astype('float32'), [96,]), relay.reshape(var_8363.astype('float32'), [1001, 1]), relay.reshape(call_8329.astype('float32'), [81,]), ), 0)
func_1084_call = mod.get_global_var('func_1084')
func_1085_call = mutated_mod.get_global_var('func_1085')
call_8365 = relay.TupleGetItem(func_1084_call(), 0)
call_8366 = relay.TupleGetItem(func_1085_call(), 0)
output = relay.Tuple([call_8304,call_8329,const_8330,var_8331,call_8350,call_8356,call_8362,var_8363,call_8365,])
output2 = relay.Tuple([call_8305,call_8332,const_8330,var_8331,call_8351,call_8357,call_8364,var_8363,call_8366,])
func_8376 = relay.Function([var_8331,var_8363,], output)
mod['func_8376'] = func_8376
mod = relay.transform.InferType()(mod)
var_8377 = relay.var("var_8377", dtype = "float32", shape = (16, 6))#candidate|8377|(16, 6)|var|float32
var_8378 = relay.var("var_8378", dtype = "float32", shape = (1001,))#candidate|8378|(1001,)|var|float32
output = func_8376(var_8377,var_8378,)
func_8379 = relay.Function([var_8377,var_8378,], output)
mutated_mod['func_8379'] = func_8379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2655_call = mod.get_global_var('func_2655')
func_2657_call = mutated_mod.get_global_var('func_2657')
call_8467 = func_2655_call()
call_8468 = func_2655_call()
func_6022_call = mod.get_global_var('func_6022')
func_6023_call = mutated_mod.get_global_var('func_6023')
call_8478 = relay.TupleGetItem(func_6022_call(), 1)
call_8479 = relay.TupleGetItem(func_6023_call(), 1)
func_6072_call = mod.get_global_var('func_6072')
func_6073_call = mutated_mod.get_global_var('func_6073')
call_8483 = relay.TupleGetItem(func_6072_call(), 0)
call_8484 = relay.TupleGetItem(func_6073_call(), 0)
func_4928_call = mod.get_global_var('func_4928')
func_4932_call = mutated_mod.get_global_var('func_4932')
var_8487 = relay.var("var_8487", dtype = "uint64", shape = (81,))#candidate|8487|(81,)|var|uint64
const_8488 = relay.const([0.014435,3.946194,9.424726,-4.775419,-1.882113,-0.804266,2.643560,6.615171,-5.994405,-3.594618,-4.062782,3.551736,2.987488,-1.602998,-1.198037,-7.072679,-9.553588,3.763649,1.899326,-9.347573,-2.991501,-6.452898,1.497574,-7.466158,8.735952,-9.374399,2.844554,3.917133,6.426910,3.233506,1.399479,8.440339,-1.373730,-7.998574,-4.976572,4.729596,6.202497,1.238325,-6.390204,5.748086,-7.266118,4.093961,7.843189,-1.067668,6.973563,-1.015401,-5.276730,-7.217661,-0.145054,-8.165807,0.790059,3.909632,7.847376,1.760225,-1.861240,-7.085689,2.612423,-7.883671,-0.022678,6.102953,5.617569,7.952469,8.545152,-0.478510,-1.391983,-4.253684,-3.647024,-5.324707,-9.567132,4.080461,-4.459508,6.665709,-9.497951,7.754587,9.800281,-3.274400,-6.036174,-5.994298,6.617893,-0.637046,7.618782,3.475938,-7.362834,2.725338,9.600442,-0.700675,-7.856268,8.162427,8.842097,-0.792330,0.837075,7.991252,-5.398638,0.779536,-4.216549,5.078557], dtype = "float32")#candidate|8488|(96,)|const|float32
call_8486 = relay.TupleGetItem(func_4928_call(relay.reshape(var_8487.astype('uint64'), [9, 3, 3]), relay.reshape(var_8487.astype('uint64'), [9, 3, 3]), relay.reshape(const_8488.astype('float32'), [96,]), ), 1)
call_8489 = relay.TupleGetItem(func_4932_call(relay.reshape(var_8487.astype('uint64'), [9, 3, 3]), relay.reshape(var_8487.astype('uint64'), [9, 3, 3]), relay.reshape(const_8488.astype('float32'), [96,]), ), 1)
func_176_call = mod.get_global_var('func_176')
func_178_call = mutated_mod.get_global_var('func_178')
call_8490 = func_176_call()
call_8491 = func_176_call()
output = relay.Tuple([call_8467,call_8478,call_8483,call_8486,var_8487,const_8488,call_8490,])
output2 = relay.Tuple([call_8468,call_8479,call_8484,call_8489,var_8487,const_8488,call_8491,])
func_8511 = relay.Function([var_8487,], output)
mod['func_8511'] = func_8511
mod = relay.transform.InferType()(mod)
mutated_mod['func_8511'] = func_8511
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8512 = relay.var("var_8512", dtype = "uint64", shape = (81,))#candidate|8512|(81,)|var|uint64
func_8511_call = mutated_mod.get_global_var('func_8511')
call_8513 = func_8511_call(var_8512)
output = call_8513
func_8514 = relay.Function([var_8512], output)
mutated_mod['func_8514'] = func_8514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2482_call = mod.get_global_var('func_2482')
func_2484_call = mutated_mod.get_global_var('func_2484')
call_8556 = relay.TupleGetItem(func_2482_call(), 0)
call_8557 = relay.TupleGetItem(func_2484_call(), 0)
func_3923_call = mod.get_global_var('func_3923')
func_3925_call = mutated_mod.get_global_var('func_3925')
call_8571 = func_3923_call()
call_8572 = func_3923_call()
func_1951_call = mod.get_global_var('func_1951')
func_1953_call = mutated_mod.get_global_var('func_1953')
call_8598 = relay.TupleGetItem(func_1951_call(), 0)
call_8599 = relay.TupleGetItem(func_1953_call(), 0)
func_4415_call = mod.get_global_var('func_4415')
func_4417_call = mutated_mod.get_global_var('func_4417')
var_8616 = relay.var("var_8616", dtype = "float64", shape = (462, 1))#candidate|8616|(462, 1)|var|float64
call_8615 = relay.TupleGetItem(func_4415_call(relay.reshape(var_8616.astype('float64'), [462,])), 3)
call_8617 = relay.TupleGetItem(func_4417_call(relay.reshape(var_8616.astype('float64'), [462,])), 3)
var_8625 = relay.var("var_8625", dtype = "float64", shape = (462, 9))#candidate|8625|(462, 9)|var|float64
bop_8626 = relay.logical_and(var_8616.astype('bool'), var_8625.astype('bool')) # shape=(462, 9)
output = relay.Tuple([call_8556,call_8571,call_8598,call_8615,bop_8626,])
output2 = relay.Tuple([call_8557,call_8572,call_8599,call_8617,bop_8626,])
func_8636 = relay.Function([var_8616,var_8625,], output)
mod['func_8636'] = func_8636
mod = relay.transform.InferType()(mod)
var_8637 = relay.var("var_8637", dtype = "float64", shape = (462, 1))#candidate|8637|(462, 1)|var|float64
var_8638 = relay.var("var_8638", dtype = "float64", shape = (462, 9))#candidate|8638|(462, 9)|var|float64
output = func_8636(var_8637,var_8638,)
func_8639 = relay.Function([var_8637,var_8638,], output)
mutated_mod['func_8639'] = func_8639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3638_call = mod.get_global_var('func_3638')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_8767 = relay.TupleGetItem(func_3638_call(), 0)
call_8768 = relay.TupleGetItem(func_3639_call(), 0)
func_6573_call = mod.get_global_var('func_6573')
func_6574_call = mutated_mod.get_global_var('func_6574')
call_8778 = relay.TupleGetItem(func_6573_call(), 0)
call_8779 = relay.TupleGetItem(func_6574_call(), 0)
output = relay.Tuple([call_8767,call_8778,])
output2 = relay.Tuple([call_8768,call_8779,])
func_8783 = relay.Function([], output)
mod['func_8783'] = func_8783
mod = relay.transform.InferType()(mod)
mutated_mod['func_8783'] = func_8783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8783_call = mutated_mod.get_global_var('func_8783')
call_8784 = func_8783_call()
output = call_8784
func_8785 = relay.Function([], output)
mutated_mod['func_8785'] = func_8785
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8786 = relay.var("var_8786", dtype = "float32", shape = (2, 3, 13))#candidate|8786|(2, 3, 13)|var|float32
uop_8787 = relay.log(var_8786.astype('float32')) # shape=(2, 3, 13)
output = relay.Tuple([uop_8787,])
output2 = relay.Tuple([uop_8787,])
func_8792 = relay.Function([var_8786,], output)
mod['func_8792'] = func_8792
mod = relay.transform.InferType()(mod)
var_8793 = relay.var("var_8793", dtype = "float32", shape = (2, 3, 13))#candidate|8793|(2, 3, 13)|var|float32
output = func_8792(var_8793)
func_8794 = relay.Function([var_8793], output)
mutated_mod['func_8794'] = func_8794
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8812 = relay.var("var_8812", dtype = "float64", shape = (2, 8, 3))#candidate|8812|(2, 8, 3)|var|float64
uop_8813 = relay.sin(var_8812.astype('float64')) # shape=(2, 8, 3)
bop_8818 = relay.less(uop_8813.astype('bool'), relay.reshape(var_8812.astype('bool'), relay.shape_of(uop_8813))) # shape=(2, 8, 3)
var_8827 = relay.var("var_8827", dtype = "float64", shape = (2, 8, 3))#candidate|8827|(2, 8, 3)|var|float64
bop_8828 = relay.greater(uop_8813.astype('bool'), relay.reshape(var_8827.astype('bool'), relay.shape_of(uop_8813))) # shape=(2, 8, 3)
uop_8833 = relay.cos(var_8812.astype('float32')) # shape=(2, 8, 3)
bop_8836 = relay.multiply(bop_8818.astype('uint64'), relay.reshape(uop_8813.astype('uint64'), relay.shape_of(bop_8818))) # shape=(2, 8, 3)
func_7378_call = mod.get_global_var('func_7378')
func_7380_call = mutated_mod.get_global_var('func_7380')
call_8850 = relay.TupleGetItem(func_7378_call(), 0)
call_8851 = relay.TupleGetItem(func_7380_call(), 0)
func_1648_call = mod.get_global_var('func_1648')
func_1651_call = mutated_mod.get_global_var('func_1651')
call_8878 = relay.TupleGetItem(func_1648_call(relay.reshape(call_8850.astype('float32'), [10, 11, 8])), 1)
call_8879 = relay.TupleGetItem(func_1651_call(relay.reshape(call_8850.astype('float32'), [10, 11, 8])), 1)
func_1910_call = mod.get_global_var('func_1910')
func_1913_call = mutated_mod.get_global_var('func_1913')
var_8890 = relay.var("var_8890", dtype = "bool", shape = (10, 42))#candidate|8890|(10, 42)|var|bool
var_8891 = relay.var("var_8891", dtype = "float64", shape = (462,))#candidate|8891|(462,)|var|float64
call_8889 = relay.TupleGetItem(func_1910_call(relay.reshape(var_8890.astype('bool'), [420,]), relay.reshape(var_8891.astype('float64'), [462,]), ), 4)
call_8892 = relay.TupleGetItem(func_1913_call(relay.reshape(var_8890.astype('bool'), [420,]), relay.reshape(var_8891.astype('float64'), [462,]), ), 4)
bop_8906 = relay.less_equal(uop_8813.astype('bool'), relay.reshape(var_8827.astype('bool'), relay.shape_of(uop_8813))) # shape=(2, 8, 3)
output = relay.Tuple([bop_8828,uop_8833,bop_8836,call_8850,call_8878,call_8889,var_8890,var_8891,bop_8906,])
output2 = relay.Tuple([bop_8828,uop_8833,bop_8836,call_8851,call_8879,call_8892,var_8890,var_8891,bop_8906,])
F = relay.Function([var_8812,var_8827,var_8890,var_8891,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8812,var_8827,var_8890,var_8891,], output2)
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
