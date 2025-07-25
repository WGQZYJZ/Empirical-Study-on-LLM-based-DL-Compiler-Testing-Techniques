import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_117 = relay.var("var_117", dtype = "float64", shape = (4, 12, 8))#candidate|117|(4, 12, 8)|var|float64
var_118 = relay.var("var_118", dtype = "float64", shape = (4, 12, 8))#candidate|118|(4, 12, 8)|var|float64
bop_119 = relay.less(var_117.astype('bool'), relay.reshape(var_118.astype('bool'), relay.shape_of(var_117))) # shape=(4, 12, 8)
output = bop_119
output2 = bop_119
func_152 = relay.Function([var_117,var_118,], output)
mod['func_152'] = func_152
mod = relay.transform.InferType()(mod)
mutated_mod['func_152'] = func_152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_152_call = mutated_mod.get_global_var('func_152')
var_154 = relay.var("var_154", dtype = "float64", shape = (4, 12, 8))#candidate|154|(4, 12, 8)|var|float64
var_155 = relay.var("var_155", dtype = "float64", shape = (4, 12, 8))#candidate|155|(4, 12, 8)|var|float64
call_153 = func_152_call(var_154,var_155,)
output = call_153
func_156 = relay.Function([var_154,var_155,], output)
mutated_mod['func_156'] = func_156
mutated_mod = relay.transform.InferType()(mutated_mod)
const_435 = relay.const([[[4.575742,5.542004,-4.064054,-0.101045,5.279542,-9.951886,-3.794190],[5.427450,2.192481,9.341942,9.903397,7.102916,9.123904,-4.059768],[9.415941,7.643626,7.621125,-1.395353,3.901122,-4.042472,8.454822],[7.666912,-9.921254,-8.758837,3.276925,-1.788085,6.725846,7.469284],[-0.166550,-5.178337,7.404172,9.917418,-5.222968,-5.007633,-6.403611],[1.021513,2.602477,9.948699,1.339098,0.474808,7.335478,2.569000],[-4.746144,9.138023,-8.020781,-8.542912,-5.946884,-0.962871,3.797450],[-7.684260,-9.742909,-5.434934,-9.698754,2.782728,1.441262,-5.493468],[-4.977887,-4.384881,-5.042369,-5.013736,3.109311,-2.505650,-5.981547],[-0.244040,1.618117,8.932419,-3.485037,5.786484,4.655081,4.856213],[5.493865,-3.707262,1.017998,-5.958113,-1.472840,1.718762,-6.657144],[8.363896,-5.061702,-2.021038,-6.993700,6.115949,3.129226,6.307470],[-8.939962,-2.662612,-3.349821,2.178712,7.049216,0.450561,-9.683435],[4.104310,-5.388006,3.143651,-1.825002,-9.162269,6.529665,-0.846340],[-3.682414,-0.437742,-6.785397,3.289579,3.840579,-2.014742,-2.476380]],[[-6.367779,-8.241520,2.782451,4.012590,-1.843172,9.030092,-6.522916],[-8.324525,1.387560,4.053874,9.869940,-3.616992,-8.951614,-5.943335],[-8.616915,0.859877,8.114824,-4.721965,-7.674463,-2.852863,-8.234768],[-7.273275,-0.409193,2.508689,1.367722,5.157098,-4.903963,6.307808],[0.789516,3.934346,4.033670,9.728254,0.788297,0.967309,3.600866],[-0.797498,6.153505,-9.814452,1.695638,-2.730361,-1.021248,-3.603027],[3.155398,-2.026633,7.957555,8.698653,-8.514901,2.520083,-4.533133],[4.778705,-0.265491,2.795895,-0.111831,-6.954441,4.585764,1.887839],[-8.219771,-2.611335,2.561317,7.470726,4.715879,3.120755,9.008532],[9.105795,-8.442862,8.454538,-3.746407,-3.058516,-6.919289,-6.364416],[8.769323,-2.692725,0.851564,-0.811308,4.764376,8.619764,-9.323836],[-0.117834,-2.815527,9.621021,-6.943778,9.315208,-9.226581,-0.338601],[-3.688007,-8.183951,-6.542700,-8.269646,-7.499333,-7.982230,-3.026438],[-7.786995,5.696661,-4.359202,-3.551595,-5.898505,-4.928837,8.199835],[0.908976,5.027988,-2.125568,-7.531514,-1.965150,7.586109,2.093286]],[[-3.474307,2.458153,-9.412824,6.337808,-7.404135,-1.697822,7.250572],[8.506921,0.309830,-7.558261,-0.493542,9.373920,2.761501,1.571117],[-0.916532,-4.877885,-3.185397,2.069979,-2.423445,5.759184,-8.153510],[3.607308,-6.639674,-9.870256,-2.534311,0.774108,1.063195,9.474165],[-5.705378,3.101673,0.577791,-7.518498,-4.601941,-0.955141,-4.592004],[9.958131,6.572845,-8.335491,4.257355,-7.574234,1.443896,8.851292],[-5.560267,4.130944,1.561595,4.206865,2.967321,4.951153,5.771854],[-7.847926,6.689994,-7.269254,1.614705,5.211626,5.664584,-3.762787],[3.943241,1.528518,-6.427232,-7.125316,-8.805989,-4.779211,4.230601],[8.618369,7.033988,7.907536,9.783573,4.133514,-4.130315,-4.488752],[-3.729428,7.502324,-2.990979,9.272053,0.634129,-0.476656,0.060566],[4.406287,-2.773129,8.084254,0.468296,3.581191,-3.453086,0.982257],[9.941078,-5.682455,-6.764108,6.238628,0.291874,1.656463,-4.676175],[-1.887079,-4.219990,6.918436,-8.059652,-9.171765,7.529853,-5.517632],[-4.776155,-4.981801,0.497023,-4.696336,-9.586518,-0.254970,-4.343576]]], dtype = "float32")#candidate|435|(3, 15, 7)|const|float32
uop_436 = relay.sin(const_435.astype('float32')) # shape=(3, 15, 7)
func_152_call = mod.get_global_var('func_152')
func_156_call = mutated_mod.get_global_var('func_156')
const_445 = relay.const([7.561081,-8.102110,5.853657,4.390030,1.244919,-7.285855,3.170973,3.597974,-8.593500,-3.720579,-5.633487,9.855397,9.754661,0.206783,-9.371091,9.661156,-4.976246,-7.701039,0.722032,9.010181,6.390648,-7.071705,2.313558,0.812954,5.938795,-3.654629,3.768895,2.526434,-2.419809,7.326988,2.660965,-5.020187,-8.849137,4.119347,-5.949212,-6.877522,-9.735972,-3.928559,2.356347,1.434195,8.779299,-7.990426,5.220165,6.944297,-6.196711,4.862164,-9.675427,9.884489,-3.419492,-8.077528,3.132055,-4.392374,6.124811,4.436543,-5.632831,5.564948,-8.492010,-2.118471,-6.292823,3.799052,-7.163418,-8.717474,6.288488,-3.642845,-2.807941,-7.899477,5.258446,0.478311,-5.604910,8.462868,2.703290,-6.162762,-0.681505,-5.164008,2.856255,5.534133,-9.718487,-9.258741,5.191992,2.868717,4.423036,8.135369,-0.757044,6.104633,1.400406,3.876639,-3.682481,1.830489,2.680301,2.899668,2.524505,-8.252497,-9.230702,0.653675,8.207461,2.409938,3.349504,-3.478214,7.461533,-8.378402,-2.012626,5.745943,0.071852,-4.261998,-5.069958,7.419781,-1.787340,9.288166,-1.244879,9.481529,7.576551,-0.034387,2.297706,-6.403946,6.622251,-8.860706,2.728608,-2.794064,-9.320842,4.986240,-4.876967,-3.714757,-2.799582,6.135447,7.012841,7.734776,1.770576,2.091485,-2.538095,2.891924,-8.348495,6.078665,5.794468,-9.882786,-1.539208,3.979562,3.210765,-9.834397,0.402058,-6.183548,-6.737148,-7.257091,-7.745707,-8.982472,8.844836,-2.377203,8.732368,6.753718,5.473639,-4.061675,8.950770,-9.190096,-0.123967,9.442775,-9.248665,-0.691515,1.356312,-6.036960,-7.914679,-8.767078,-1.973824,0.455304,-7.906446,-9.891686,-7.563241,-1.432733,-9.233650,-4.638903,2.099171,2.303692,-2.510434,-1.321333,-5.439504,0.866132,3.266628,-4.979842,-4.455547,-2.786904,7.322177,-5.704833,1.583427,5.651400,4.298265,-3.550506,7.833175,-9.437102,1.981824,3.227932,2.164952,-6.518728,-6.412430,-4.027094,-7.786042,-7.270647,9.700196,-9.029912,7.119173,1.789105,4.863824,5.977009,8.391527,-0.493798,-6.508583,-9.785716,-7.623918,-9.386904,0.911264,8.055785,5.789612,2.852302,-0.711214,-9.002361,-9.541186,-0.768571,2.124120,-8.703381,8.022693,-2.096030,8.406813,5.980858,2.008903,-8.108108,-5.213406,8.311031,3.155337,0.903704,-5.185590,1.073733,9.719717,-1.300573,7.330697,0.689462,-3.220085,-1.807567,-6.416904,2.021633,-7.848279,-4.435741,-2.365009,-3.026768,7.644634,2.204677,6.920855,-4.040658,8.668581,-8.129932,0.897116,2.547732,1.486067,8.171847,-1.787041,5.052635,3.890231,5.103799,0.690525,2.704368,4.534813,-6.914483,-4.360889,5.372207,-3.622174,-6.316369,6.332282,6.130607,-4.764456,-7.728310,8.824716,3.149042,-0.919795,-6.662675,-5.246795,-1.780322,6.471103,2.109185,1.463908,8.147094,-4.738903,7.842648,9.043629,-2.471189,-5.025624,-0.335033,-8.333458,-2.205022,4.756771,8.829459,-0.471539,4.418800,-4.034974,8.066138,-0.050017,9.110500,9.363722,-3.900989,0.495703,-7.570921,-9.892050,-1.509552,-7.161365,2.330006,2.832263,1.525208,-1.288589,0.218315,9.275288,-4.792178,8.193864,-6.922036,-5.473487,-2.605712,4.508190,3.501084,8.255635,3.277191,-7.997443,9.604367,6.615507,-4.563167,-7.793645,-6.977316,-3.115109,0.149584,1.519988,-6.302054,-9.692718,1.820578,5.621746,4.208386,-7.299136,-8.169570,5.341177,0.600919,9.660514,-4.108313,1.902927,1.497234,8.914141,-9.932945,9.722022,3.043455,7.799816,8.777249,4.224723,8.140856,8.306370,2.572937,-2.121850,4.224374,-4.014002,8.662314,0.432571,3.511870,8.905872,2.937418,0.135264,-3.887402,8.503696,0.323553,4.834475,8.012945,0.360446,9.780390,4.484053,7.679930,8.777276,5.484127,3.345287,5.097437,-7.618403,8.853814,2.709136,-2.567471,-5.951396,-2.171962,0.295582,-7.738462,-7.675544,-1.156045,1.721240,6.843695,-4.289387,7.598067,0.376265,-2.604414], dtype = "float64")#candidate|445|(384,)|const|float64
call_444 = func_152_call(relay.reshape(const_445.astype('float64'), [4, 12, 8]), relay.reshape(const_445.astype('float64'), [4, 12, 8]), )
call_446 = func_152_call(relay.reshape(const_445.astype('float64'), [4, 12, 8]), relay.reshape(const_445.astype('float64'), [4, 12, 8]), )
output = relay.Tuple([uop_436,call_444,const_445,])
output2 = relay.Tuple([uop_436,call_446,const_445,])
func_448 = relay.Function([], output)
mod['func_448'] = func_448
mod = relay.transform.InferType()(mod)
mutated_mod['func_448'] = func_448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mutated_mod.get_global_var('func_448')
call_449 = func_448_call()
output = call_449
func_450 = relay.Function([], output)
mutated_mod['func_450'] = func_450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_457 = relay.TupleGetItem(func_448_call(), 0)
call_458 = relay.TupleGetItem(func_450_call(), 0)
output = relay.Tuple([call_457,])
output2 = relay.Tuple([call_458,])
func_477 = relay.Function([], output)
mod['func_477'] = func_477
mod = relay.transform.InferType()(mod)
mutated_mod['func_477'] = func_477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mutated_mod.get_global_var('func_477')
call_478 = func_477_call()
output = call_478
func_479 = relay.Function([], output)
mutated_mod['func_479'] = func_479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_480 = relay.TupleGetItem(func_477_call(), 0)
call_481 = relay.TupleGetItem(func_479_call(), 0)
output = relay.Tuple([call_480,])
output2 = relay.Tuple([call_481,])
func_526 = relay.Function([], output)
mod['func_526'] = func_526
mod = relay.transform.InferType()(mod)
output = func_526()
func_527 = relay.Function([], output)
mutated_mod['func_527'] = func_527
mutated_mod = relay.transform.InferType()(mutated_mod)
const_537 = relay.const(-3, dtype = "int64")#candidate|537|()|const|int64
var_538 = relay.var("var_538", dtype = "int64", shape = (4, 12, 4))#candidate|538|(4, 12, 4)|var|int64
bop_539 = relay.maximum(const_537.astype('int64'), var_538.astype('int64')) # shape=(4, 12, 4)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_544 = relay.TupleGetItem(func_526_call(), 0)
call_545 = relay.TupleGetItem(func_527_call(), 0)
output = relay.Tuple([bop_539,call_544,])
output2 = relay.Tuple([bop_539,call_545,])
func_555 = relay.Function([var_538,], output)
mod['func_555'] = func_555
mod = relay.transform.InferType()(mod)
mutated_mod['func_555'] = func_555
mutated_mod = relay.transform.InferType()(mutated_mod)
var_556 = relay.var("var_556", dtype = "int64", shape = (4, 12, 4))#candidate|556|(4, 12, 4)|var|int64
func_555_call = mutated_mod.get_global_var('func_555')
call_557 = func_555_call(var_556)
output = call_557
func_558 = relay.Function([var_556], output)
mutated_mod['func_558'] = func_558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_560 = relay.TupleGetItem(func_477_call(), 0)
call_561 = relay.TupleGetItem(func_479_call(), 0)
func_152_call = mod.get_global_var('func_152')
func_156_call = mutated_mod.get_global_var('func_156')
const_563 = relay.const([[-3.476630,1.194319,2.015361,-3.763931,-5.398245,-5.617531,3.160151,4.162913,-5.836399,-9.816157,-2.982942,6.555956,-2.947766,5.990575,-5.058831,-6.861617,-4.545133,-5.583865,9.625850,7.824103,2.823162,-1.394133,-7.618360,-7.590347,9.932351,1.707681,8.493222,-8.715617,-9.828280,-0.558924,3.693530,8.582271,9.178132,7.941511,5.512023,-2.431370,2.780466,3.115481,-0.927138,-2.288164,-2.847491,-6.267013,-3.931994,9.187974,-4.695080,2.250547,7.411695,-7.104193,1.886901,6.021450,-3.221497,7.311015,-6.292576,9.946589,-0.065058,-9.481529,-3.967301,-0.185893,-9.535644,8.556225,-5.659476,-2.886251,1.682835,-0.647406,-5.675791,0.633994,5.538915,-6.496862,9.456358,4.347022,1.564096,9.517353,-2.035285,8.638739,9.697000,7.293681,9.376184,3.380613,-2.384730,2.598668,4.790661,-2.165275,3.618552,-2.847343,-9.757700,3.646931,-4.159196,6.841124,-3.988283,3.001939,0.963349,8.452580,-2.566227,-8.493603,-5.700348,9.009122,-7.854062,6.778157,3.197786,6.807268,6.371033,6.980342,7.596016,-1.647832,2.667341,1.644007,-7.558901,-5.389150,-9.317340,-9.636781,-7.793704,-6.629055,7.256648,6.460894,-4.334529,-2.093348,9.107317,2.638196,3.050322,-8.907798,0.028485,3.407341,6.611826,-2.239346,-8.300442,-5.198423,-1.785835,-4.929231,-8.863350,-4.079511,-7.609084,-7.366652,1.832071,-2.862775,1.834330,1.281403,-2.656828,8.265319,-6.330327,9.176422,-0.313116,-8.644942,6.705894,-3.477084,-4.256169,-0.225120,1.226326,-4.056248,-5.840804,4.524464,9.958699,-1.877011,-3.288275,6.848848,3.569050,2.565540,0.064725,-4.756190,-6.113337,-9.876917,-5.072316,9.504045,-6.278621,-4.908478,-4.546216,-6.381395,-7.394568,-8.284484,-9.673281,-5.568757,-0.844970,9.802062,9.504228,-9.352450,-2.953355,-3.810305,3.265768,5.720885,0.503100,-9.532235,7.862343,1.116769,3.114758,-6.119833,-8.030402,2.769094,9.538732,-8.338556,2.961784,-2.609796,4.658157,-1.907020],[0.858786,-7.652763,2.331233,-2.501373,-4.767620,-1.351647,2.167419,7.018539,7.598860,9.671721,-7.968438,9.396914,-8.109054,4.838087,-3.565329,6.133370,4.197942,-9.101822,-4.811607,-6.430196,2.079429,7.240990,1.105260,-7.393316,0.168771,0.169358,2.100046,6.877348,0.855816,3.806086,-9.043225,3.322403,0.506049,-4.760706,-2.946016,-6.493712,-3.967367,2.860707,-2.710931,-4.612612,3.634950,0.837592,5.845274,-1.440042,-6.017584,-2.069424,-8.367384,-4.348611,-2.207562,-1.755801,9.562774,-9.105037,-4.442293,-7.895755,5.009375,-5.499974,-0.542592,1.311333,3.360637,-7.510098,2.748115,-3.561354,-0.369095,3.545661,-3.452767,-3.124777,-5.846483,9.897248,-8.627622,-5.980037,-8.596251,-4.767038,-8.586335,-8.313071,9.602306,8.649110,-7.736272,6.685042,6.801896,0.841134,-5.450943,6.304160,-0.298024,4.785290,-4.492090,-6.068111,-9.404644,-7.226961,-7.074468,-2.720102,8.587949,-1.945355,-5.964558,7.140802,6.430469,3.659422,-7.806053,-0.288248,2.453710,9.734061,8.118014,-9.361978,-5.502853,9.960274,-9.103862,-6.737137,9.443637,7.984671,-0.325022,5.776028,7.838245,9.624144,-6.330999,-5.074422,8.214743,9.893859,2.829185,9.434671,-3.352844,-4.903563,-9.838499,8.920098,8.985158,1.891541,2.781933,9.044752,6.128959,-8.017521,5.951747,1.023199,-0.368615,9.082699,6.444870,9.058253,4.336402,-3.366382,-0.241536,-4.583048,-4.883003,-7.258525,-7.907057,-3.315244,-5.868421,2.077921,6.073231,0.705676,-6.512909,4.855131,5.315786,3.154397,-1.406299,-1.119275,3.743938,-3.971693,1.068431,4.192488,1.336228,3.042983,-6.284140,8.834938,-1.529113,3.352377,6.186148,-9.060952,1.511730,-4.725307,7.410406,9.545882,9.533847,-4.809762,-2.059155,-0.487296,9.659422,1.079074,1.458251,4.826021,7.713817,-5.743920,4.442615,9.821254,-6.402477,-7.317595,1.478206,3.806447,4.020725,2.524117,9.537601,5.424825,0.178841,0.708511,5.305782,-2.347478]], dtype = "float64")#candidate|563|(2, 192)|const|float64
call_562 = func_152_call(relay.reshape(const_563.astype('float64'), [4, 12, 8]), relay.reshape(const_563.astype('float64'), [4, 12, 8]), )
call_564 = func_152_call(relay.reshape(const_563.astype('float64'), [4, 12, 8]), relay.reshape(const_563.astype('float64'), [4, 12, 8]), )
func_152_call = mod.get_global_var('func_152')
func_156_call = mutated_mod.get_global_var('func_156')
call_567 = func_152_call(relay.reshape(call_562.astype('float64'), [4, 12, 8]), relay.reshape(call_562.astype('float64'), [4, 12, 8]), )
call_568 = func_152_call(relay.reshape(call_562.astype('float64'), [4, 12, 8]), relay.reshape(call_562.astype('float64'), [4, 12, 8]), )
output = relay.Tuple([call_560,call_562,const_563,call_567,])
output2 = relay.Tuple([call_561,call_564,const_563,call_568,])
func_578 = relay.Function([], output)
mod['func_578'] = func_578
mod = relay.transform.InferType()(mod)
output = func_578()
func_579 = relay.Function([], output)
mutated_mod['func_579'] = func_579
mutated_mod = relay.transform.InferType()(mutated_mod)
const_603 = relay.const(4, dtype = "uint64")#candidate|603|()|const|uint64
var_604 = relay.var("var_604", dtype = "uint64", shape = (8, 4, 1))#candidate|604|(8, 4, 1)|var|uint64
bop_605 = relay.bitwise_or(const_603.astype('uint64'), var_604.astype('uint64')) # shape=(8, 4, 1)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_626 = relay.TupleGetItem(func_448_call(), 1)
call_627 = relay.TupleGetItem(func_450_call(), 1)
output = relay.Tuple([bop_605,call_626,])
output2 = relay.Tuple([bop_605,call_627,])
func_629 = relay.Function([var_604,], output)
mod['func_629'] = func_629
mod = relay.transform.InferType()(mod)
mutated_mod['func_629'] = func_629
mutated_mod = relay.transform.InferType()(mutated_mod)
var_630 = relay.var("var_630", dtype = "uint64", shape = (8, 4, 1))#candidate|630|(8, 4, 1)|var|uint64
func_629_call = mutated_mod.get_global_var('func_629')
call_631 = func_629_call(var_630)
output = call_631
func_632 = relay.Function([var_630], output)
mutated_mod['func_632'] = func_632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_702 = relay.TupleGetItem(func_477_call(), 0)
call_703 = relay.TupleGetItem(func_479_call(), 0)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_717 = relay.TupleGetItem(func_448_call(), 1)
call_718 = relay.TupleGetItem(func_450_call(), 1)
func_578_call = mod.get_global_var('func_578')
func_579_call = mutated_mod.get_global_var('func_579')
call_731 = relay.TupleGetItem(func_578_call(), 1)
call_732 = relay.TupleGetItem(func_579_call(), 1)
var_734 = relay.var("var_734", dtype = "bool", shape = (4, 12, 8))#candidate|734|(4, 12, 8)|var|bool
bop_735 = relay.minimum(call_731.astype('uint8'), relay.reshape(var_734.astype('uint8'), relay.shape_of(call_731))) # shape=(4, 12, 8)
bop_738 = relay.minimum(call_732.astype('uint8'), relay.reshape(var_734.astype('uint8'), relay.shape_of(call_732))) # shape=(4, 12, 8)
func_152_call = mod.get_global_var('func_152')
func_156_call = mutated_mod.get_global_var('func_156')
call_764 = func_152_call(relay.reshape(call_717.astype('float64'), [4, 12, 8]), relay.reshape(var_734.astype('float64'), [4, 12, 8]), )
call_765 = func_152_call(relay.reshape(call_717.astype('float64'), [4, 12, 8]), relay.reshape(var_734.astype('float64'), [4, 12, 8]), )
output = relay.Tuple([call_702,call_717,bop_735,call_764,])
output2 = relay.Tuple([call_703,call_718,bop_738,call_765,])
func_780 = relay.Function([var_734,], output)
mod['func_780'] = func_780
mod = relay.transform.InferType()(mod)
mutated_mod['func_780'] = func_780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_781 = relay.var("var_781", dtype = "bool", shape = (4, 12, 8))#candidate|781|(4, 12, 8)|var|bool
func_780_call = mutated_mod.get_global_var('func_780')
call_782 = func_780_call(var_781)
output = call_782
func_783 = relay.Function([var_781], output)
mutated_mod['func_783'] = func_783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_578_call = mod.get_global_var('func_578')
func_579_call = mutated_mod.get_global_var('func_579')
call_834 = relay.TupleGetItem(func_578_call(), 2)
call_835 = relay.TupleGetItem(func_579_call(), 2)
output = relay.Tuple([call_834,])
output2 = relay.Tuple([call_835,])
func_838 = relay.Function([], output)
mod['func_838'] = func_838
mod = relay.transform.InferType()(mod)
output = func_838()
func_839 = relay.Function([], output)
mutated_mod['func_839'] = func_839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_875 = relay.TupleGetItem(func_448_call(), 1)
call_876 = relay.TupleGetItem(func_450_call(), 1)
uop_880 = relay.erf(call_875.astype('float64')) # shape=(4, 12, 8)
uop_882 = relay.erf(call_876.astype('float64')) # shape=(4, 12, 8)
output = uop_880
output2 = uop_882
func_884 = relay.Function([], output)
mod['func_884'] = func_884
mod = relay.transform.InferType()(mod)
output = func_884()
func_885 = relay.Function([], output)
mutated_mod['func_885'] = func_885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_838_call = mod.get_global_var('func_838')
func_839_call = mutated_mod.get_global_var('func_839')
call_945 = relay.TupleGetItem(func_838_call(), 0)
call_946 = relay.TupleGetItem(func_839_call(), 0)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_952 = relay.TupleGetItem(func_477_call(), 0)
call_953 = relay.TupleGetItem(func_479_call(), 0)
func_629_call = mod.get_global_var('func_629')
func_632_call = mutated_mod.get_global_var('func_632')
const_963 = relay.const([-8,-2,-10,4,-3,3,-7,-8,-2,3,4,-7,1,7,6,-10,6,-5,-4,10,-6,-9,-9,-9,9,-3,5,9,9,3,3,2], dtype = "uint64")#candidate|963|(32,)|const|uint64
call_962 = relay.TupleGetItem(func_629_call(relay.reshape(const_963.astype('uint64'), [8, 4, 1])), 1)
call_964 = relay.TupleGetItem(func_632_call(relay.reshape(const_963.astype('uint64'), [8, 4, 1])), 1)
bop_967 = relay.add(call_945.astype('int64'), relay.reshape(call_962.astype('int64'), relay.shape_of(call_945))) # shape=(2, 192)
bop_970 = relay.add(call_946.astype('int64'), relay.reshape(call_964.astype('int64'), relay.shape_of(call_946))) # shape=(2, 192)
func_780_call = mod.get_global_var('func_780')
func_783_call = mutated_mod.get_global_var('func_783')
call_971 = relay.TupleGetItem(func_780_call(relay.reshape(call_962.astype('bool'), [4, 12, 8])), 2)
call_972 = relay.TupleGetItem(func_783_call(relay.reshape(call_962.astype('bool'), [4, 12, 8])), 2)
output = relay.Tuple([call_952,const_963,bop_967,call_971,])
output2 = relay.Tuple([call_953,const_963,bop_970,call_972,])
func_973 = relay.Function([], output)
mod['func_973'] = func_973
mod = relay.transform.InferType()(mod)
mutated_mod['func_973'] = func_973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_973_call = mutated_mod.get_global_var('func_973')
call_974 = func_973_call()
output = call_974
func_975 = relay.Function([], output)
mutated_mod['func_975'] = func_975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_992 = relay.TupleGetItem(func_526_call(), 0)
call_993 = relay.TupleGetItem(func_527_call(), 0)
var_997 = relay.var("var_997", dtype = "float32", shape = (3, 15, 7))#candidate|997|(3, 15, 7)|var|float32
bop_998 = relay.subtract(call_992.astype('float64'), relay.reshape(var_997.astype('float64'), relay.shape_of(call_992))) # shape=(3, 15, 7)
bop_1001 = relay.subtract(call_993.astype('float64'), relay.reshape(var_997.astype('float64'), relay.shape_of(call_993))) # shape=(3, 15, 7)
output = bop_998
output2 = bop_1001
func_1016 = relay.Function([var_997,], output)
mod['func_1016'] = func_1016
mod = relay.transform.InferType()(mod)
var_1017 = relay.var("var_1017", dtype = "float32", shape = (3, 15, 7))#candidate|1017|(3, 15, 7)|var|float32
output = func_1016(var_1017)
func_1018 = relay.Function([var_1017], output)
mutated_mod['func_1018'] = func_1018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_884_call = mod.get_global_var('func_884')
func_885_call = mutated_mod.get_global_var('func_885')
call_1023 = func_884_call()
call_1024 = func_884_call()
uop_1027 = relay.log(call_1023.astype('float32')) # shape=(4, 12, 8)
uop_1029 = relay.log(call_1024.astype('float32')) # shape=(4, 12, 8)
output = relay.Tuple([uop_1027,])
output2 = relay.Tuple([uop_1029,])
func_1030 = relay.Function([], output)
mod['func_1030'] = func_1030
mod = relay.transform.InferType()(mod)
output = func_1030()
func_1031 = relay.Function([], output)
mutated_mod['func_1031'] = func_1031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_973_call = mod.get_global_var('func_973')
func_975_call = mutated_mod.get_global_var('func_975')
call_1035 = relay.TupleGetItem(func_973_call(), 0)
call_1036 = relay.TupleGetItem(func_975_call(), 0)
output = call_1035
output2 = call_1036
func_1048 = relay.Function([], output)
mod['func_1048'] = func_1048
mod = relay.transform.InferType()(mod)
output = func_1048()
func_1049 = relay.Function([], output)
mutated_mod['func_1049'] = func_1049
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1105 = relay.const([[[9.378330,-2.212968,4.771426],[-3.453830,-7.234853,8.444598]],[[8.403784,1.099878,-8.293367],[-8.270192,-3.873801,3.422561]],[[-5.829904,8.578053,-7.052898],[-9.244169,1.393440,-2.506864]],[[-8.466385,8.088697,-1.320808],[5.877858,-0.714461,-8.037733]],[[-8.750200,4.732326,0.481965],[-8.926683,-7.995638,3.348615]],[[-4.247630,-7.570393,-3.183965],[-6.302253,8.622802,5.305271]],[[-2.626923,6.704215,1.699374],[-4.495792,-9.119087,-7.913570]],[[-2.052914,7.726027,7.729580],[8.667912,-1.003517,7.159026]],[[4.876802,2.796183,4.070323],[-0.427565,4.967809,-4.208586]],[[9.950941,1.713109,-4.967101],[-6.176469,-5.478851,6.844666]],[[-4.447168,2.637070,9.090200],[-2.236235,-1.666798,4.694663]],[[-0.760557,-4.086239,-9.906259],[2.291497,8.054187,9.006509]],[[-2.554136,-9.757073,-6.526667],[-7.361044,8.640431,5.860188]],[[6.056685,2.822072,-6.594653],[8.272044,-9.597023,-0.301712]]], dtype = "float32")#candidate|1105|(14, 2, 3)|const|float32
var_1106 = relay.var("var_1106", dtype = "float32", shape = (14, 2, 3))#candidate|1106|(14, 2, 3)|var|float32
bop_1107 = relay.greater(const_1105.astype('bool'), relay.reshape(var_1106.astype('bool'), relay.shape_of(const_1105))) # shape=(14, 2, 3)
uop_1118 = relay.acos(bop_1107.astype('float64')) # shape=(14, 2, 3)
output = uop_1118
output2 = uop_1118
func_1132 = relay.Function([var_1106,], output)
mod['func_1132'] = func_1132
mod = relay.transform.InferType()(mod)
mutated_mod['func_1132'] = func_1132
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1133 = relay.var("var_1133", dtype = "float32", shape = (14, 2, 3))#candidate|1133|(14, 2, 3)|var|float32
func_1132_call = mutated_mod.get_global_var('func_1132')
call_1134 = func_1132_call(var_1133)
output = call_1134
func_1135 = relay.Function([var_1133], output)
mutated_mod['func_1135'] = func_1135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_1155 = relay.TupleGetItem(func_448_call(), 0)
call_1156 = relay.TupleGetItem(func_450_call(), 0)
uop_1174 = relay.tan(call_1155.astype('float64')) # shape=(3, 15, 7)
uop_1176 = relay.tan(call_1156.astype('float64')) # shape=(3, 15, 7)
func_973_call = mod.get_global_var('func_973')
func_975_call = mutated_mod.get_global_var('func_975')
call_1179 = relay.TupleGetItem(func_973_call(), 2)
call_1180 = relay.TupleGetItem(func_975_call(), 2)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_1189 = relay.TupleGetItem(func_477_call(), 0)
call_1190 = relay.TupleGetItem(func_479_call(), 0)
func_1132_call = mod.get_global_var('func_1132')
func_1135_call = mutated_mod.get_global_var('func_1135')
var_1205 = relay.var("var_1205", dtype = "float32", shape = (84,))#candidate|1205|(84,)|var|float32
call_1204 = func_1132_call(relay.reshape(var_1205.astype('float32'), [14, 2, 3]))
call_1206 = func_1132_call(relay.reshape(var_1205.astype('float32'), [14, 2, 3]))
output = relay.Tuple([uop_1174,call_1179,call_1189,call_1204,var_1205,])
output2 = relay.Tuple([uop_1176,call_1180,call_1190,call_1206,var_1205,])
func_1209 = relay.Function([var_1205,], output)
mod['func_1209'] = func_1209
mod = relay.transform.InferType()(mod)
var_1210 = relay.var("var_1210", dtype = "float32", shape = (84,))#candidate|1210|(84,)|var|float32
output = func_1209(var_1210)
func_1211 = relay.Function([var_1210], output)
mutated_mod['func_1211'] = func_1211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_838_call = mod.get_global_var('func_838')
func_839_call = mutated_mod.get_global_var('func_839')
call_1213 = relay.TupleGetItem(func_838_call(), 0)
call_1214 = relay.TupleGetItem(func_839_call(), 0)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_1216 = relay.TupleGetItem(func_477_call(), 0)
call_1217 = relay.TupleGetItem(func_479_call(), 0)
output = relay.Tuple([call_1213,call_1216,])
output2 = relay.Tuple([call_1214,call_1217,])
func_1223 = relay.Function([], output)
mod['func_1223'] = func_1223
mod = relay.transform.InferType()(mod)
mutated_mod['func_1223'] = func_1223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mutated_mod.get_global_var('func_1223')
call_1224 = func_1223_call()
output = call_1224
func_1225 = relay.Function([], output)
mutated_mod['func_1225'] = func_1225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_1226 = relay.TupleGetItem(func_477_call(), 0)
call_1227 = relay.TupleGetItem(func_479_call(), 0)
const_1234 = relay.const([[[1.055416,-1.036810,-4.620669,2.508116,6.128744,-2.541122,0.637125],[-7.844439,-4.030609,-0.891209,-5.345287,-3.346501,9.627123,3.888797],[-7.958290,-7.710602,0.528698,6.033200,0.217335,0.407841,-1.511916],[1.914192,1.843482,-2.340550,-3.088864,-9.097008,4.356764,-7.660211],[0.627121,5.256336,-9.772403,4.553398,-8.133165,-1.323951,0.079268],[-9.436488,5.540945,1.286556,9.046063,-8.969920,-6.855410,-6.473663],[1.144319,-7.658366,6.452231,-0.655505,1.881447,6.348776,-1.897055],[3.074541,3.229004,4.932562,5.264780,-7.263491,0.315880,-7.297301],[8.263263,1.604723,4.697160,1.757569,3.389363,6.438467,3.096196],[-6.244341,-8.498957,0.959166,-9.649730,-0.155402,0.105288,-3.315552],[5.030060,-1.946632,-1.815810,8.959340,7.706455,-9.516920,-2.655132],[0.351702,-6.760820,-3.764029,3.156621,3.052404,-4.721425,8.223500],[-5.165290,-0.696823,-0.795927,-2.919317,-4.301782,8.858158,-5.327085],[-0.280208,5.762626,-6.299659,-1.813948,-2.498903,-6.998093,1.394126],[0.388182,-0.057842,-5.163804,9.163748,2.344688,0.447315,6.896343]],[[7.902954,-8.433352,-2.027244,0.758333,-9.767997,8.790481,7.124369],[-8.428701,4.405964,5.345188,7.120709,-8.455161,-9.058885,-3.181055],[-9.578340,-4.270663,1.495074,1.055591,-7.128103,-3.551362,-8.762730],[4.317092,9.394182,-5.378822,8.925141,-8.015019,-0.436883,5.987347],[-7.680288,-6.251849,8.464431,-9.731106,-6.801212,0.416555,-5.012270],[0.413751,0.560831,-7.516952,-0.253234,1.809567,-4.488805,-6.395274],[1.471744,9.207173,3.707880,-8.331012,4.516607,4.057387,-7.035385],[-1.937444,-6.718954,-7.536231,9.328016,-6.437911,4.285489,8.081814],[0.820894,-5.627473,-4.429434,-3.161517,-2.711029,-6.186310,0.814456],[0.284991,-9.549434,-5.698389,7.354564,7.792879,4.727655,-8.046911],[2.116037,-2.004060,0.720241,6.415414,-4.114846,2.691777,-4.046867],[-6.793348,6.389298,-5.394558,-5.681624,-4.969624,7.526799,-2.875621],[4.163740,7.359640,-4.760520,9.159379,6.728345,4.123772,-1.010526],[-1.929513,0.615110,-3.518934,-0.732241,-8.215414,0.315397,-6.523948],[-0.976598,6.690220,4.401482,4.817131,-2.677368,6.180339,9.241149]],[[9.097323,4.584256,4.127898,5.864705,7.994112,-6.211550,-6.547536],[-6.419904,-8.066611,8.160133,-0.139492,-1.077632,-3.046201,-2.620380],[-8.874539,8.116600,1.248959,6.684192,9.160794,-7.431545,-9.662176],[-8.276673,-8.689673,8.821451,-9.425367,-4.002278,0.623681,-4.489626],[1.611113,6.187863,-8.424493,0.189341,6.395888,-6.632671,2.743291],[6.153673,5.700834,-8.568226,-9.803943,-0.333245,-8.756472,1.705677],[-6.518072,-1.832758,-5.254038,1.778203,-6.688513,-5.495452,-0.058077],[-6.241085,7.757625,5.132033,1.598829,-3.207557,-0.240149,-8.076378],[3.868011,-0.974466,4.285361,0.425581,0.018926,2.429953,-0.677119],[9.433664,-7.207878,-7.182622,-8.360013,5.728588,-2.471879,7.643327],[-3.175115,7.411187,-4.259171,6.194427,-5.840372,1.865857,-6.199843],[1.099047,5.316682,6.937274,-6.655701,2.126807,0.563286,9.749652],[1.608200,-5.430926,-7.826164,6.262363,-6.774883,1.071628,-1.416219],[-0.977446,0.714722,4.137261,-9.005298,-1.929815,-5.951151,5.114552],[-5.967665,7.588416,-0.182872,-2.351864,-4.433019,4.212456,-5.701442]]], dtype = "float32")#candidate|1234|(3, 15, 7)|const|float32
bop_1235 = relay.not_equal(call_1226.astype('bool'), relay.reshape(const_1234.astype('bool'), relay.shape_of(call_1226))) # shape=(3, 15, 7)
bop_1238 = relay.not_equal(call_1227.astype('bool'), relay.reshape(const_1234.astype('bool'), relay.shape_of(call_1227))) # shape=(3, 15, 7)
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
const_1250 = relay.const([1.625570,-1.165360,-0.204713,5.953902,9.886882,-3.918174,4.892522,0.372236,-2.117330,-4.159888,1.213711,-7.778733,-4.817104,2.601681,8.456840,1.029990,2.076432,-8.922857,-1.337041,1.824322,-0.638166,6.504016,3.930370,-1.452624,2.178196,-8.132135,-4.764700,0.195186,-0.521988,-3.197724,-9.409780,-7.657018,-6.635193,3.988155,8.423579,-9.875635,1.673121,9.134173,7.959177,-0.357746,-7.956959,3.009328,0.373072,-3.722258,2.951277,2.720621,-3.889444,4.862991,-5.362544,4.448313,9.810189,-2.349602,8.033518,2.456754,3.337045,4.069427,0.538217,6.463901,-9.684550,-8.281298,-5.298588,7.966778,-8.197773,7.854951,-3.990572,-2.114295,1.891398,-5.277413,-9.381694,5.415136,3.044849,7.379495,5.193746,4.937484,-7.331466,3.969983,4.945753,3.223178,8.427789,-3.456315,-2.096832,-7.778691,3.982571,-0.252683], dtype = "float32")#candidate|1250|(84,)|const|float32
call_1249 = relay.TupleGetItem(func_1209_call(relay.reshape(const_1250.astype('float32'), [84,])), 2)
call_1251 = relay.TupleGetItem(func_1211_call(relay.reshape(const_1250.astype('float32'), [84,])), 2)
uop_1263 = relay.rsqrt(bop_1235.astype('float32')) # shape=(3, 15, 7)
uop_1265 = relay.rsqrt(bop_1238.astype('float32')) # shape=(3, 15, 7)
func_555_call = mod.get_global_var('func_555')
func_558_call = mutated_mod.get_global_var('func_558')
var_1276 = relay.var("var_1276", dtype = "int64", shape = (192,))#candidate|1276|(192,)|var|int64
call_1275 = relay.TupleGetItem(func_555_call(relay.reshape(var_1276.astype('int64'), [4, 12, 4])), 0)
call_1277 = relay.TupleGetItem(func_558_call(relay.reshape(var_1276.astype('int64'), [4, 12, 4])), 0)
output = relay.Tuple([call_1249,const_1250,uop_1263,call_1275,var_1276,])
output2 = relay.Tuple([call_1251,const_1250,uop_1265,call_1277,var_1276,])
func_1279 = relay.Function([var_1276,], output)
mod['func_1279'] = func_1279
mod = relay.transform.InferType()(mod)
var_1280 = relay.var("var_1280", dtype = "int64", shape = (192,))#candidate|1280|(192,)|var|int64
output = func_1279(var_1280)
func_1281 = relay.Function([var_1280], output)
mutated_mod['func_1281'] = func_1281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1285 = relay.TupleGetItem(func_1030_call(), 0)
call_1286 = relay.TupleGetItem(func_1031_call(), 0)
output = relay.Tuple([call_1285,])
output2 = relay.Tuple([call_1286,])
func_1294 = relay.Function([], output)
mod['func_1294'] = func_1294
mod = relay.transform.InferType()(mod)
output = func_1294()
func_1295 = relay.Function([], output)
mutated_mod['func_1295'] = func_1295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1294_call = mod.get_global_var('func_1294')
func_1295_call = mutated_mod.get_global_var('func_1295')
call_1296 = relay.TupleGetItem(func_1294_call(), 0)
call_1297 = relay.TupleGetItem(func_1295_call(), 0)
func_1223_call = mod.get_global_var('func_1223')
func_1225_call = mutated_mod.get_global_var('func_1225')
call_1313 = relay.TupleGetItem(func_1223_call(), 1)
call_1314 = relay.TupleGetItem(func_1225_call(), 1)
func_884_call = mod.get_global_var('func_884')
func_885_call = mutated_mod.get_global_var('func_885')
call_1316 = func_884_call()
call_1317 = func_884_call()
func_1279_call = mod.get_global_var('func_1279')
func_1281_call = mutated_mod.get_global_var('func_1281')
var_1335 = relay.var("var_1335", dtype = "int64", shape = (1, 192))#candidate|1335|(1, 192)|var|int64
call_1334 = relay.TupleGetItem(func_1279_call(relay.reshape(var_1335.astype('int64'), [192,])), 0)
call_1336 = relay.TupleGetItem(func_1281_call(relay.reshape(var_1335.astype('int64'), [192,])), 0)
output = relay.Tuple([call_1296,call_1313,call_1316,call_1334,var_1335,])
output2 = relay.Tuple([call_1297,call_1314,call_1317,call_1336,var_1335,])
func_1348 = relay.Function([var_1335,], output)
mod['func_1348'] = func_1348
mod = relay.transform.InferType()(mod)
mutated_mod['func_1348'] = func_1348
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1349 = relay.var("var_1349", dtype = "int64", shape = (1, 192))#candidate|1349|(1, 192)|var|int64
func_1348_call = mutated_mod.get_global_var('func_1348')
call_1350 = func_1348_call(var_1349)
output = call_1350
func_1351 = relay.Function([var_1349], output)
mutated_mod['func_1351'] = func_1351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1368 = relay.TupleGetItem(func_1030_call(), 0)
call_1369 = relay.TupleGetItem(func_1031_call(), 0)
uop_1370 = relay.atanh(call_1368.astype('float64')) # shape=(4, 12, 8)
uop_1372 = relay.atanh(call_1369.astype('float64')) # shape=(4, 12, 8)
output = relay.Tuple([uop_1370,])
output2 = relay.Tuple([uop_1372,])
func_1377 = relay.Function([], output)
mod['func_1377'] = func_1377
mod = relay.transform.InferType()(mod)
mutated_mod['func_1377'] = func_1377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1377_call = mutated_mod.get_global_var('func_1377')
call_1378 = func_1377_call()
output = call_1378
func_1379 = relay.Function([], output)
mutated_mod['func_1379'] = func_1379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mod.get_global_var('func_1223')
func_1225_call = mutated_mod.get_global_var('func_1225')
call_1420 = relay.TupleGetItem(func_1223_call(), 1)
call_1421 = relay.TupleGetItem(func_1225_call(), 1)
output = relay.Tuple([call_1420,])
output2 = relay.Tuple([call_1421,])
func_1433 = relay.Function([], output)
mod['func_1433'] = func_1433
mod = relay.transform.InferType()(mod)
mutated_mod['func_1433'] = func_1433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1433_call = mutated_mod.get_global_var('func_1433')
call_1434 = func_1433_call()
output = call_1434
func_1435 = relay.Function([], output)
mutated_mod['func_1435'] = func_1435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_578_call = mod.get_global_var('func_578')
func_579_call = mutated_mod.get_global_var('func_579')
call_1438 = relay.TupleGetItem(func_578_call(), 0)
call_1439 = relay.TupleGetItem(func_579_call(), 0)
output = relay.Tuple([call_1438,])
output2 = relay.Tuple([call_1439,])
func_1443 = relay.Function([], output)
mod['func_1443'] = func_1443
mod = relay.transform.InferType()(mod)
output = func_1443()
func_1444 = relay.Function([], output)
mutated_mod['func_1444'] = func_1444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1048_call = mod.get_global_var('func_1048')
func_1049_call = mutated_mod.get_global_var('func_1049')
call_1447 = func_1048_call()
call_1448 = func_1048_call()
var_1449 = relay.var("var_1449", dtype = "float32", shape = (3, 15, 7))#candidate|1449|(3, 15, 7)|var|float32
bop_1450 = relay.greater(call_1447.astype('bool'), relay.reshape(var_1449.astype('bool'), relay.shape_of(call_1447))) # shape=(3, 15, 7)
bop_1453 = relay.greater(call_1448.astype('bool'), relay.reshape(var_1449.astype('bool'), relay.shape_of(call_1448))) # shape=(3, 15, 7)
func_555_call = mod.get_global_var('func_555')
func_558_call = mutated_mod.get_global_var('func_558')
const_1456 = relay.const([7,-2,4,-10,10,-3,-2,8,-2,3,-6,-9,-6,7,3,10,-3,-4,2,5,1,8,2,1,-9,-7,5,-5,8,-3,-9,3,-7,8,-3,1,10,9,-7,6,-7,2,-9,-10,-6,-10,-6,-8,1,2,8,10,-5,10,1,8,8,-9,7,-4,2,10,8,-3,-4,5,-10,-10,5,-7,-5,-4,6,-10,5,-6,7,-9,3,-5,6,-9,-6,1,8,-8,6,-5,-7,7,-8,-3,10,3,-1,-10,-10,-5,-7,-8,8,-1,-9,-9,1,2,-9,-6,4,-2,-8,4,-1,-4,7,7,-7,-2,-3,5,-6,-5,2,6,1,-1,-10,6,-5,-2,-2,10,5,8,-2,6,-1,-5,-2,-9,8,-3,6,-2,10,5,-10,3,-8,7,-5,-10,-2,9,7,-9,9,-7,-3,-6,-10,-7,8,10,-3,8,10,4,4,-7,3,-7,-10,-7,-3,6,-6,6,2,-9,-2,3,-4,3,-2,8,8,10,-2,-1,-2,8], dtype = "int64")#candidate|1456|(192,)|const|int64
call_1455 = relay.TupleGetItem(func_555_call(relay.reshape(const_1456.astype('int64'), [4, 12, 4])), 1)
call_1457 = relay.TupleGetItem(func_558_call(relay.reshape(const_1456.astype('int64'), [4, 12, 4])), 1)
output = relay.Tuple([bop_1450,call_1455,const_1456,])
output2 = relay.Tuple([bop_1453,call_1457,const_1456,])
func_1467 = relay.Function([var_1449,], output)
mod['func_1467'] = func_1467
mod = relay.transform.InferType()(mod)
mutated_mod['func_1467'] = func_1467
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1468 = relay.var("var_1468", dtype = "float32", shape = (3, 15, 7))#candidate|1468|(3, 15, 7)|var|float32
func_1467_call = mutated_mod.get_global_var('func_1467')
call_1469 = func_1467_call(var_1468)
output = call_1469
func_1470 = relay.Function([var_1468], output)
mutated_mod['func_1470'] = func_1470
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1498 = relay.const([[[0.046519,0.454111,1.747245,7.032499,-0.002039],[6.993695,-2.297347,-5.691583,-1.789180,0.046202],[1.050266,7.972278,-3.679183,-5.412281,-2.079271],[2.437219,-6.133723,1.582774,-2.872505,7.557697],[3.830304,1.374024,0.572389,-8.980374,-9.123437],[-8.764228,-5.069526,1.757120,-7.095459,-7.119356],[9.320499,-2.650637,7.308440,7.997375,-1.710235],[-3.596082,3.805974,8.722119,5.697709,-3.861202],[3.336746,-7.734205,-8.007623,0.893565,2.996250],[-2.989871,7.267043,5.042346,-5.584212,-6.663277],[6.314057,-2.617603,6.724166,8.722020,-2.137297],[-3.996419,-2.928094,4.663437,-9.854790,-6.551600],[-2.143544,-6.038265,1.974724,-4.012395,-0.152891],[1.239056,-9.309924,-9.950341,1.236597,-4.797808],[-1.403847,-0.076438,8.210418,7.368840,-4.408102]],[[-7.129663,-2.860198,-0.230735,-5.124549,0.931382],[-7.077715,-7.663528,8.624592,-1.889713,-8.576349],[-2.127025,1.413934,4.501775,-3.165536,-5.888182],[-7.241972,3.248677,1.365851,6.469927,4.885629],[-7.699597,5.531964,-4.693692,8.173258,5.251509],[4.378633,-0.478077,-9.083522,-3.779403,4.935178],[8.401276,6.512616,-9.990683,9.012222,-6.001674],[2.749513,-7.940026,2.606403,4.819907,0.120496],[-3.799550,-6.645854,0.454035,-7.389771,5.927083],[-9.585635,-7.618649,1.894216,-2.787583,-1.005476],[0.174865,2.484054,-0.421667,-7.539181,8.946560],[-7.256392,3.719921,2.493384,-1.266253,-9.717161],[0.333515,-4.487682,-4.234573,-0.503856,-0.677853],[3.187622,-4.537051,4.560976,1.042147,-2.966036],[3.822203,-7.273636,8.522068,3.880186,0.656796]],[[7.489045,-8.787970,-6.581017,-2.799263,7.978008],[1.090224,-0.321439,8.676501,-0.824470,-8.432776],[-0.178536,-7.930736,-3.287319,-4.841000,4.178154],[6.881187,-0.353573,-4.303236,-4.683552,8.206857],[-0.731763,-3.239190,1.678253,-1.280429,-5.203099],[-8.897322,5.528662,7.076786,6.417717,4.491994],[3.074696,4.285740,3.510966,6.905252,-3.169220],[2.219082,6.445037,-4.501052,-5.640756,8.577776],[9.844007,4.344100,-5.301977,-8.870390,-5.786082],[-0.711472,-1.343322,6.089410,3.135635,5.973051],[8.469748,-8.614446,-4.336374,6.136385,-9.088795],[7.597526,0.827424,-7.229678,7.615505,4.821020],[-9.523735,7.486989,2.712594,-5.328354,3.570535],[1.073549,8.754440,-3.770475,-1.698187,-0.631970],[-7.055097,-8.485815,-5.419770,2.551430,8.363533]],[[5.225307,-0.745496,-1.866482,1.017310,-1.789514],[-4.847058,2.974363,-3.674246,5.409421,-3.388537],[9.423762,2.800838,-2.290775,-1.464725,1.382372],[-0.398734,6.680388,1.026403,-6.881011,5.591165],[-6.403534,-1.940628,5.757236,1.054734,4.200948],[-9.424553,-4.554033,-3.287094,9.470131,-4.221455],[-9.199847,4.430293,0.277629,8.787603,2.885031],[-4.546500,-4.434182,9.580723,0.261601,-5.645841],[-1.860061,5.771136,-5.432331,7.844779,-3.233252],[-4.493619,-5.487372,5.383602,7.627989,-7.942927],[0.012097,-2.050255,8.710201,8.054062,-3.114615],[-0.135091,-1.306465,9.657039,0.237458,-9.868414],[-2.996849,6.962447,-9.913596,-4.512957,1.868557],[-3.196325,4.928000,3.457848,-4.737429,-6.735783],[-1.000147,-9.193556,-9.908734,-6.890544,-7.370505]],[[-1.738116,7.450294,-8.254049,-3.363166,7.030656],[1.890973,-9.258743,-7.993244,0.339180,-8.459251],[3.772813,-9.890781,4.635371,0.842319,8.824054],[-2.318950,-2.243983,5.387896,4.842880,4.349556],[5.959472,-4.667357,-4.989728,2.390935,0.607445],[8.301980,4.446822,-1.129785,-3.512272,-1.365441],[-3.171058,5.124299,-2.235245,7.622314,-4.658633],[4.159790,4.145016,5.783982,-9.154683,7.849711],[-1.343500,2.997559,2.730114,-5.050529,4.954278],[7.918334,4.364887,0.181579,0.862606,1.698719],[1.231847,7.511378,-1.360076,-2.544247,-7.990457],[0.959583,-7.951481,-0.740056,-9.486173,-0.283275],[9.522900,9.901149,-3.141922,-4.838830,0.657809],[-5.447262,-2.559515,0.989863,-8.008738,-8.391147],[-7.965179,-8.702364,-8.030450,-3.723893,9.065357]],[[-9.585973,-1.821061,-4.647907,-2.003537,-5.276580],[-1.517728,8.636574,-4.932927,-2.653458,-4.196929],[8.038102,-1.854898,-8.978871,-0.469231,7.224980],[2.205855,-5.133729,-3.635210,-4.202537,-8.776673],[-4.811068,4.686149,9.330959,0.957135,5.988925],[-3.661345,-3.030420,-6.522858,3.843374,0.629043],[-0.817840,1.454857,-5.723566,1.205403,-9.918171],[3.316212,5.678837,-3.864181,-2.280768,-4.635173],[-3.493195,0.377000,8.546009,8.474493,-4.851279],[5.764207,7.313178,-4.711472,-6.451615,-8.805246],[0.454411,-4.412690,8.166476,6.820405,-6.561428],[3.691533,7.978392,1.021556,-6.289132,6.169663],[1.872468,6.875944,8.474341,-8.476077,-4.234789],[8.537097,-7.619005,-7.456359,-0.516262,2.548985],[8.174016,2.793859,5.168306,5.889198,8.400441]],[[2.040509,4.990877,8.166555,-3.956042,0.952654],[4.092581,-6.655883,-0.284456,8.605821,-7.653519],[1.823639,4.584111,-7.756270,3.497798,-2.464695],[9.078431,6.060096,-6.398585,2.774190,-3.268736],[1.813682,0.436658,5.566926,-6.035728,4.486692],[6.946681,-3.243607,5.148516,-2.190565,-2.900312],[-3.972885,-2.428530,9.478436,-3.520814,8.383246],[6.792094,-0.958762,-5.980063,-8.125004,-7.466471],[4.333045,-8.303512,-1.637853,4.076766,-2.300907],[0.885932,7.760363,-2.509069,3.923650,8.260517],[9.342709,1.268713,-2.339027,1.697212,0.907983],[-6.421751,7.410199,-4.011940,-2.094438,-8.108594],[-5.198069,5.345388,8.778217,-5.760056,1.751471],[0.770227,-7.022701,-9.896218,-3.244401,3.924924],[-2.888789,2.177017,-5.424461,5.392245,2.551255]],[[6.313637,-9.340542,8.044295,-7.420919,-1.510105],[5.469942,-3.854514,-2.162459,-1.384773,-4.908395],[-2.053168,6.231934,-0.553843,-8.283235,6.507623],[-1.461551,5.865102,5.642013,-9.811552,-4.525025],[4.619793,6.590500,2.338330,2.001557,-0.161182],[0.483635,-5.165734,-6.345744,-7.328009,-6.763683],[-1.482631,-7.346288,2.838607,-5.038482,5.427396],[-6.637215,9.131441,-2.416664,-0.390795,-1.090352],[8.437699,5.752639,8.460452,-8.307105,-0.955509],[2.900546,9.231062,-7.814540,8.443346,2.007409],[6.253508,-3.982400,9.010418,3.518773,-4.897890],[-0.120465,3.318730,1.926301,-8.479901,-9.306599],[-4.945271,5.387986,5.104920,1.572937,3.760957],[6.391981,-6.877367,5.922619,-0.582928,7.702114],[-6.198583,-6.393859,-4.786394,-1.474204,-4.470739]]], dtype = "float32")#candidate|1498|(8, 15, 5)|const|float32
uop_1499 = relay.cosh(const_1498.astype('float32')) # shape=(8, 15, 5)
output = relay.Tuple([uop_1499,])
output2 = relay.Tuple([uop_1499,])
func_1509 = relay.Function([], output)
mod['func_1509'] = func_1509
mod = relay.transform.InferType()(mod)
output = func_1509()
func_1510 = relay.Function([], output)
mutated_mod['func_1510'] = func_1510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_1519 = relay.TupleGetItem(func_448_call(), 2)
call_1520 = relay.TupleGetItem(func_450_call(), 2)
output = call_1519
output2 = call_1520
func_1527 = relay.Function([], output)
mod['func_1527'] = func_1527
mod = relay.transform.InferType()(mod)
mutated_mod['func_1527'] = func_1527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1527_call = mutated_mod.get_global_var('func_1527')
call_1528 = func_1527_call()
output = call_1528
func_1529 = relay.Function([], output)
mutated_mod['func_1529'] = func_1529
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1536 = relay.var("var_1536", dtype = "int64", shape = (3, 3, 8))#candidate|1536|(3, 3, 8)|var|int64
var_1537 = relay.var("var_1537", dtype = "int64", shape = (3, 3, 8))#candidate|1537|(3, 3, 8)|var|int64
bop_1538 = relay.maximum(var_1536.astype('int64'), relay.reshape(var_1537.astype('int64'), relay.shape_of(var_1536))) # shape=(3, 3, 8)
output = bop_1538
output2 = bop_1538
func_1546 = relay.Function([var_1536,var_1537,], output)
mod['func_1546'] = func_1546
mod = relay.transform.InferType()(mod)
mutated_mod['func_1546'] = func_1546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1546_call = mutated_mod.get_global_var('func_1546')
var_1548 = relay.var("var_1548", dtype = "int64", shape = (3, 3, 8))#candidate|1548|(3, 3, 8)|var|int64
var_1549 = relay.var("var_1549", dtype = "int64", shape = (3, 3, 8))#candidate|1549|(3, 3, 8)|var|int64
call_1547 = func_1546_call(var_1548,var_1549,)
output = call_1547
func_1550 = relay.Function([var_1548,var_1549,], output)
mutated_mod['func_1550'] = func_1550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1708 = relay.TupleGetItem(func_1030_call(), 0)
call_1709 = relay.TupleGetItem(func_1031_call(), 0)
uop_1712 = relay.tan(call_1708.astype('float32')) # shape=(4, 12, 8)
uop_1714 = relay.tan(call_1709.astype('float32')) # shape=(4, 12, 8)
func_1279_call = mod.get_global_var('func_1279')
func_1281_call = mutated_mod.get_global_var('func_1281')
var_1730 = relay.var("var_1730", dtype = "int64", shape = (192,))#candidate|1730|(192,)|var|int64
call_1729 = relay.TupleGetItem(func_1279_call(relay.reshape(var_1730.astype('int64'), [192,])), 3)
call_1731 = relay.TupleGetItem(func_1281_call(relay.reshape(var_1730.astype('int64'), [192,])), 3)
bop_1736 = relay.bitwise_or(uop_1712.astype('uint8'), relay.reshape(call_1708.astype('uint8'), relay.shape_of(uop_1712))) # shape=(4, 12, 8)
bop_1739 = relay.bitwise_or(uop_1714.astype('uint8'), relay.reshape(call_1709.astype('uint8'), relay.shape_of(uop_1714))) # shape=(4, 12, 8)
output = relay.Tuple([call_1729,var_1730,bop_1736,])
output2 = relay.Tuple([call_1731,var_1730,bop_1739,])
func_1760 = relay.Function([var_1730,], output)
mod['func_1760'] = func_1760
mod = relay.transform.InferType()(mod)
mutated_mod['func_1760'] = func_1760
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1761 = relay.var("var_1761", dtype = "int64", shape = (192,))#candidate|1761|(192,)|var|int64
func_1760_call = mutated_mod.get_global_var('func_1760')
call_1762 = func_1760_call(var_1761)
output = call_1762
func_1763 = relay.Function([var_1761], output)
mutated_mod['func_1763'] = func_1763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_884_call = mod.get_global_var('func_884')
func_885_call = mutated_mod.get_global_var('func_885')
call_1765 = func_884_call()
call_1766 = func_884_call()
output = relay.Tuple([call_1765,])
output2 = relay.Tuple([call_1766,])
func_1771 = relay.Function([], output)
mod['func_1771'] = func_1771
mod = relay.transform.InferType()(mod)
mutated_mod['func_1771'] = func_1771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1771_call = mutated_mod.get_global_var('func_1771')
call_1772 = func_1771_call()
output = call_1772
func_1773 = relay.Function([], output)
mutated_mod['func_1773'] = func_1773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mod.get_global_var('func_1223')
func_1225_call = mutated_mod.get_global_var('func_1225')
call_1805 = relay.TupleGetItem(func_1223_call(), 1)
call_1806 = relay.TupleGetItem(func_1225_call(), 1)
output = call_1805
output2 = call_1806
func_1812 = relay.Function([], output)
mod['func_1812'] = func_1812
mod = relay.transform.InferType()(mod)
output = func_1812()
func_1813 = relay.Function([], output)
mutated_mod['func_1813'] = func_1813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1509_call = mod.get_global_var('func_1509')
func_1510_call = mutated_mod.get_global_var('func_1510')
call_1814 = relay.TupleGetItem(func_1509_call(), 0)
call_1815 = relay.TupleGetItem(func_1510_call(), 0)
output = call_1814
output2 = call_1815
func_1829 = relay.Function([], output)
mod['func_1829'] = func_1829
mod = relay.transform.InferType()(mod)
mutated_mod['func_1829'] = func_1829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1829_call = mutated_mod.get_global_var('func_1829')
call_1830 = func_1829_call()
output = call_1830
func_1831 = relay.Function([], output)
mutated_mod['func_1831'] = func_1831
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1860 = relay.var("var_1860", dtype = "uint8", shape = (4, 3, 13))#candidate|1860|(4, 3, 13)|var|uint8
var_1861 = relay.var("var_1861", dtype = "uint8", shape = (4, 3, 13))#candidate|1861|(4, 3, 13)|var|uint8
bop_1862 = relay.right_shift(var_1860.astype('uint8'), relay.reshape(var_1861.astype('uint8'), relay.shape_of(var_1860))) # shape=(4, 3, 13)
output = relay.Tuple([bop_1862,])
output2 = relay.Tuple([bop_1862,])
func_1880 = relay.Function([var_1860,var_1861,], output)
mod['func_1880'] = func_1880
mod = relay.transform.InferType()(mod)
var_1881 = relay.var("var_1881", dtype = "uint8", shape = (4, 3, 13))#candidate|1881|(4, 3, 13)|var|uint8
var_1882 = relay.var("var_1882", dtype = "uint8", shape = (4, 3, 13))#candidate|1882|(4, 3, 13)|var|uint8
output = func_1880(var_1881,var_1882,)
func_1883 = relay.Function([var_1881,var_1882,], output)
mutated_mod['func_1883'] = func_1883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1443_call = mod.get_global_var('func_1443')
func_1444_call = mutated_mod.get_global_var('func_1444')
call_1945 = relay.TupleGetItem(func_1443_call(), 0)
call_1946 = relay.TupleGetItem(func_1444_call(), 0)
output = relay.Tuple([call_1945,])
output2 = relay.Tuple([call_1946,])
func_1958 = relay.Function([], output)
mod['func_1958'] = func_1958
mod = relay.transform.InferType()(mod)
output = func_1958()
func_1959 = relay.Function([], output)
mutated_mod['func_1959'] = func_1959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_838_call = mod.get_global_var('func_838')
func_839_call = mutated_mod.get_global_var('func_839')
call_2010 = relay.TupleGetItem(func_838_call(), 0)
call_2011 = relay.TupleGetItem(func_839_call(), 0)
func_1348_call = mod.get_global_var('func_1348')
func_1351_call = mutated_mod.get_global_var('func_1351')
const_2015 = relay.const([-4,10,-9,-7,2,8,9,-10,9,-10,-4,8,8,10,-6,1,-3,9,9,8,2,-1,-4,-7,10,-7,2,-8,3,-10,-2,-6,-6,-8,3,-8,-4,7,-1,2,-4,8,4,6,-4,6,-9,-5,-9,10,1,-8,7,2,2,1,-2,-9,5,-6,4,-6,-6,6,4,-9,1,9,-3,-8,-4,10,-6,-4,6,9,-2,3,-4,3,-2,-2,-10,-3,-1,-9,-7,-2,-9,5,4,7,1,-4,-6,4,9,-5,6,-1,8,-1,-8,2,-9,5,3,9,-2,8,8,-8,-7,-6,-10,9,9,-4,6,8,-3,9,7,-9,-9,-6,10,-5,-8,1,10,-7,3,-9,9,2,-10,-9,7,5,4,6,-7,2,-4,5,-2,-4,-6,-4,10,-9,7,9,-6,1,-6,-8,9,-2,3,-6,10,2,5,-4,-1,9,-3,-1,3,-2,2,3,8,-2,-3,-5,-10,-10,2,2,-9,1,-7,2,8,-8,2,10,7,10], dtype = "int64")#candidate|2015|(192,)|const|int64
call_2014 = relay.TupleGetItem(func_1348_call(relay.reshape(const_2015.astype('int64'), [1, 192])), 3)
call_2016 = relay.TupleGetItem(func_1351_call(relay.reshape(const_2015.astype('int64'), [1, 192])), 3)
uop_2020 = relay.log2(call_2014.astype('float32')) # shape=(3, 15, 7)
uop_2022 = relay.log2(call_2016.astype('float32')) # shape=(3, 15, 7)
func_1509_call = mod.get_global_var('func_1509')
func_1510_call = mutated_mod.get_global_var('func_1510')
call_2027 = relay.TupleGetItem(func_1509_call(), 0)
call_2028 = relay.TupleGetItem(func_1510_call(), 0)
output = relay.Tuple([call_2010,const_2015,uop_2020,call_2027,])
output2 = relay.Tuple([call_2011,const_2015,uop_2022,call_2028,])
func_2032 = relay.Function([], output)
mod['func_2032'] = func_2032
mod = relay.transform.InferType()(mod)
mutated_mod['func_2032'] = func_2032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2032_call = mutated_mod.get_global_var('func_2032')
call_2033 = func_2032_call()
output = call_2033
func_2034 = relay.Function([], output)
mutated_mod['func_2034'] = func_2034
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2054 = relay.var("var_2054", dtype = "float64", shape = (3, 4, 2))#candidate|2054|(3, 4, 2)|var|float64
var_2055 = relay.var("var_2055", dtype = "float64", shape = (3, 4, 2))#candidate|2055|(3, 4, 2)|var|float64
bop_2056 = relay.greater(var_2054.astype('bool'), relay.reshape(var_2055.astype('bool'), relay.shape_of(var_2054))) # shape=(3, 4, 2)
func_1377_call = mod.get_global_var('func_1377')
func_1379_call = mutated_mod.get_global_var('func_1379')
call_2064 = relay.TupleGetItem(func_1377_call(), 0)
call_2065 = relay.TupleGetItem(func_1379_call(), 0)
output = relay.Tuple([bop_2056,call_2064,])
output2 = relay.Tuple([bop_2056,call_2065,])
func_2066 = relay.Function([var_2054,var_2055,], output)
mod['func_2066'] = func_2066
mod = relay.transform.InferType()(mod)
mutated_mod['func_2066'] = func_2066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2066_call = mutated_mod.get_global_var('func_2066')
var_2068 = relay.var("var_2068", dtype = "float64", shape = (3, 4, 2))#candidate|2068|(3, 4, 2)|var|float64
var_2069 = relay.var("var_2069", dtype = "float64", shape = (3, 4, 2))#candidate|2069|(3, 4, 2)|var|float64
call_2067 = func_2066_call(var_2068,var_2069,)
output = call_2067
func_2070 = relay.Function([var_2068,var_2069,], output)
mutated_mod['func_2070'] = func_2070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_2084 = relay.TupleGetItem(func_526_call(), 0)
call_2085 = relay.TupleGetItem(func_527_call(), 0)
output = relay.Tuple([call_2084,])
output2 = relay.Tuple([call_2085,])
func_2111 = relay.Function([], output)
mod['func_2111'] = func_2111
mod = relay.transform.InferType()(mod)
output = func_2111()
func_2112 = relay.Function([], output)
mutated_mod['func_2112'] = func_2112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_2121 = relay.TupleGetItem(func_526_call(), 0)
call_2122 = relay.TupleGetItem(func_527_call(), 0)
func_1433_call = mod.get_global_var('func_1433')
func_1435_call = mutated_mod.get_global_var('func_1435')
call_2127 = relay.TupleGetItem(func_1433_call(), 0)
call_2128 = relay.TupleGetItem(func_1435_call(), 0)
output = relay.Tuple([call_2121,call_2127,])
output2 = relay.Tuple([call_2122,call_2128,])
func_2129 = relay.Function([], output)
mod['func_2129'] = func_2129
mod = relay.transform.InferType()(mod)
output = func_2129()
func_2130 = relay.Function([], output)
mutated_mod['func_2130'] = func_2130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_2138 = relay.TupleGetItem(func_1030_call(), 0)
call_2139 = relay.TupleGetItem(func_1031_call(), 0)
output = relay.Tuple([call_2138,])
output2 = relay.Tuple([call_2139,])
func_2141 = relay.Function([], output)
mod['func_2141'] = func_2141
mod = relay.transform.InferType()(mod)
output = func_2141()
func_2142 = relay.Function([], output)
mutated_mod['func_2142'] = func_2142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_2145 = relay.TupleGetItem(func_448_call(), 1)
call_2146 = relay.TupleGetItem(func_450_call(), 1)
func_973_call = mod.get_global_var('func_973')
func_975_call = mutated_mod.get_global_var('func_975')
call_2147 = relay.TupleGetItem(func_973_call(), 0)
call_2148 = relay.TupleGetItem(func_975_call(), 0)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_2170 = relay.TupleGetItem(func_448_call(), 2)
call_2171 = relay.TupleGetItem(func_450_call(), 2)
output = relay.Tuple([call_2145,call_2147,call_2170,])
output2 = relay.Tuple([call_2146,call_2148,call_2171,])
func_2179 = relay.Function([], output)
mod['func_2179'] = func_2179
mod = relay.transform.InferType()(mod)
output = func_2179()
func_2180 = relay.Function([], output)
mutated_mod['func_2180'] = func_2180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1433_call = mod.get_global_var('func_1433')
func_1435_call = mutated_mod.get_global_var('func_1435')
call_2239 = relay.TupleGetItem(func_1433_call(), 0)
call_2240 = relay.TupleGetItem(func_1435_call(), 0)
func_1348_call = mod.get_global_var('func_1348')
func_1351_call = mutated_mod.get_global_var('func_1351')
var_2267 = relay.var("var_2267", dtype = "int64", shape = (192,))#candidate|2267|(192,)|var|int64
call_2266 = relay.TupleGetItem(func_1348_call(relay.reshape(var_2267.astype('int64'), [1, 192])), 1)
call_2268 = relay.TupleGetItem(func_1351_call(relay.reshape(var_2267.astype('int64'), [1, 192])), 1)
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
var_2275 = relay.var("var_2275", dtype = "float32", shape = (84,))#candidate|2275|(84,)|var|float32
call_2274 = relay.TupleGetItem(func_1209_call(relay.reshape(var_2275.astype('float32'), [84,])), 4)
call_2276 = relay.TupleGetItem(func_1211_call(relay.reshape(var_2275.astype('float32'), [84,])), 4)
func_2129_call = mod.get_global_var('func_2129')
func_2130_call = mutated_mod.get_global_var('func_2130')
call_2295 = relay.TupleGetItem(func_2129_call(), 1)
call_2296 = relay.TupleGetItem(func_2130_call(), 1)
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_2308 = relay.TupleGetItem(func_1030_call(), 0)
call_2309 = relay.TupleGetItem(func_1031_call(), 0)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_2316 = func_1016_call(relay.reshape(call_2295.astype('float32'), [3, 15, 7]))
call_2317 = func_1016_call(relay.reshape(call_2295.astype('float32'), [3, 15, 7]))
func_1812_call = mod.get_global_var('func_1812')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_2319 = func_1812_call()
call_2320 = func_1812_call()
func_1279_call = mod.get_global_var('func_1279')
func_1281_call = mutated_mod.get_global_var('func_1281')
call_2327 = relay.TupleGetItem(func_1279_call(relay.reshape(var_2267.astype('int64'), [192,])), 0)
call_2328 = relay.TupleGetItem(func_1281_call(relay.reshape(var_2267.astype('int64'), [192,])), 0)
func_1771_call = mod.get_global_var('func_1771')
func_1773_call = mutated_mod.get_global_var('func_1773')
call_2335 = relay.TupleGetItem(func_1771_call(), 0)
call_2336 = relay.TupleGetItem(func_1773_call(), 0)
func_1294_call = mod.get_global_var('func_1294')
func_1295_call = mutated_mod.get_global_var('func_1295')
call_2337 = relay.TupleGetItem(func_1294_call(), 0)
call_2338 = relay.TupleGetItem(func_1295_call(), 0)
bop_2351 = relay.add(call_2335.astype('int32'), relay.reshape(call_2308.astype('int32'), relay.shape_of(call_2335))) # shape=(4, 12, 8)
bop_2354 = relay.add(call_2336.astype('int32'), relay.reshape(call_2309.astype('int32'), relay.shape_of(call_2336))) # shape=(4, 12, 8)
output = relay.Tuple([call_2239,call_2266,var_2267,call_2274,var_2275,call_2295,call_2316,call_2319,call_2327,call_2337,bop_2351,])
output2 = relay.Tuple([call_2240,call_2268,var_2267,call_2276,var_2275,call_2296,call_2317,call_2320,call_2328,call_2338,bop_2354,])
func_2357 = relay.Function([var_2267,var_2275,], output)
mod['func_2357'] = func_2357
mod = relay.transform.InferType()(mod)
mutated_mod['func_2357'] = func_2357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2357_call = mutated_mod.get_global_var('func_2357')
var_2359 = relay.var("var_2359", dtype = "int64", shape = (192,))#candidate|2359|(192,)|var|int64
var_2360 = relay.var("var_2360", dtype = "float32", shape = (84,))#candidate|2360|(84,)|var|float32
call_2358 = func_2357_call(var_2359,var_2360,)
output = call_2358
func_2361 = relay.Function([var_2359,var_2360,], output)
mutated_mod['func_2361'] = func_2361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mod.get_global_var('func_1223')
func_1225_call = mutated_mod.get_global_var('func_1225')
call_2384 = relay.TupleGetItem(func_1223_call(), 1)
call_2385 = relay.TupleGetItem(func_1225_call(), 1)
uop_2386 = relay.atan(call_2384.astype('float64')) # shape=(3, 15, 7)
uop_2388 = relay.atan(call_2385.astype('float64')) # shape=(3, 15, 7)
output = relay.Tuple([uop_2386,])
output2 = relay.Tuple([uop_2388,])
func_2390 = relay.Function([], output)
mod['func_2390'] = func_2390
mod = relay.transform.InferType()(mod)
mutated_mod['func_2390'] = func_2390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2390_call = mutated_mod.get_global_var('func_2390')
call_2391 = func_2390_call()
output = call_2391
func_2392 = relay.Function([], output)
mutated_mod['func_2392'] = func_2392
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2396 = relay.var("var_2396", dtype = "int64", shape = (14, 6, 2))#candidate|2396|(14, 6, 2)|var|int64
var_2397 = relay.var("var_2397", dtype = "int64", shape = (14, 6, 2))#candidate|2397|(14, 6, 2)|var|int64
bop_2398 = relay.equal(var_2396.astype('bool'), relay.reshape(var_2397.astype('bool'), relay.shape_of(var_2396))) # shape=(14, 6, 2)
func_1443_call = mod.get_global_var('func_1443')
func_1444_call = mutated_mod.get_global_var('func_1444')
call_2407 = relay.TupleGetItem(func_1443_call(), 0)
call_2408 = relay.TupleGetItem(func_1444_call(), 0)
func_555_call = mod.get_global_var('func_555')
func_558_call = mutated_mod.get_global_var('func_558')
var_2413 = relay.var("var_2413", dtype = "int64", shape = (192,))#candidate|2413|(192,)|var|int64
call_2412 = relay.TupleGetItem(func_555_call(relay.reshape(var_2413.astype('int64'), [4, 12, 4])), 0)
call_2414 = relay.TupleGetItem(func_558_call(relay.reshape(var_2413.astype('int64'), [4, 12, 4])), 0)
var_2428 = relay.var("var_2428", dtype = "int64", shape = (4, 12, 4))#candidate|2428|(4, 12, 4)|var|int64
bop_2429 = relay.divide(call_2412.astype('float64'), relay.reshape(var_2428.astype('float64'), relay.shape_of(call_2412))) # shape=(4, 12, 4)
bop_2432 = relay.divide(call_2414.astype('float64'), relay.reshape(var_2428.astype('float64'), relay.shape_of(call_2414))) # shape=(4, 12, 4)
output = relay.Tuple([bop_2398,call_2407,var_2413,bop_2429,])
output2 = relay.Tuple([bop_2398,call_2408,var_2413,bop_2432,])
func_2437 = relay.Function([var_2396,var_2397,var_2413,var_2428,], output)
mod['func_2437'] = func_2437
mod = relay.transform.InferType()(mod)
mutated_mod['func_2437'] = func_2437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2437_call = mutated_mod.get_global_var('func_2437')
var_2439 = relay.var("var_2439", dtype = "int64", shape = (14, 6, 2))#candidate|2439|(14, 6, 2)|var|int64
var_2440 = relay.var("var_2440", dtype = "int64", shape = (14, 6, 2))#candidate|2440|(14, 6, 2)|var|int64
var_2441 = relay.var("var_2441", dtype = "int64", shape = (192,))#candidate|2441|(192,)|var|int64
var_2442 = relay.var("var_2442", dtype = "int64", shape = (4, 12, 4))#candidate|2442|(4, 12, 4)|var|int64
call_2438 = func_2437_call(var_2439,var_2440,var_2441,var_2442,)
output = call_2438
func_2443 = relay.Function([var_2439,var_2440,var_2441,var_2442,], output)
mutated_mod['func_2443'] = func_2443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_973_call = mod.get_global_var('func_973')
func_975_call = mutated_mod.get_global_var('func_975')
call_2457 = relay.TupleGetItem(func_973_call(), 0)
call_2458 = relay.TupleGetItem(func_975_call(), 0)
output = call_2457
output2 = call_2458
func_2486 = relay.Function([], output)
mod['func_2486'] = func_2486
mod = relay.transform.InferType()(mod)
mutated_mod['func_2486'] = func_2486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2486_call = mutated_mod.get_global_var('func_2486')
call_2487 = func_2486_call()
output = call_2487
func_2488 = relay.Function([], output)
mutated_mod['func_2488'] = func_2488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_838_call = mod.get_global_var('func_838')
func_839_call = mutated_mod.get_global_var('func_839')
call_2544 = relay.TupleGetItem(func_838_call(), 0)
call_2545 = relay.TupleGetItem(func_839_call(), 0)
func_1348_call = mod.get_global_var('func_1348')
func_1351_call = mutated_mod.get_global_var('func_1351')
var_2548 = relay.var("var_2548", dtype = "int64", shape = (192,))#candidate|2548|(192,)|var|int64
call_2547 = relay.TupleGetItem(func_1348_call(relay.reshape(var_2548.astype('int64'), [1, 192])), 4)
call_2549 = relay.TupleGetItem(func_1351_call(relay.reshape(var_2548.astype('int64'), [1, 192])), 4)
func_555_call = mod.get_global_var('func_555')
func_558_call = mutated_mod.get_global_var('func_558')
call_2560 = relay.TupleGetItem(func_555_call(relay.reshape(call_2547.astype('int64'), [4, 12, 4])), 0)
call_2561 = relay.TupleGetItem(func_558_call(relay.reshape(call_2547.astype('int64'), [4, 12, 4])), 0)
output = relay.Tuple([call_2544,call_2547,var_2548,call_2560,])
output2 = relay.Tuple([call_2545,call_2549,var_2548,call_2561,])
func_2564 = relay.Function([var_2548,], output)
mod['func_2564'] = func_2564
mod = relay.transform.InferType()(mod)
mutated_mod['func_2564'] = func_2564
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2565 = relay.var("var_2565", dtype = "int64", shape = (192,))#candidate|2565|(192,)|var|int64
func_2564_call = mutated_mod.get_global_var('func_2564')
call_2566 = func_2564_call(var_2565)
output = call_2566
func_2567 = relay.Function([var_2565], output)
mutated_mod['func_2567'] = func_2567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2179_call = mod.get_global_var('func_2179')
func_2180_call = mutated_mod.get_global_var('func_2180')
call_2571 = relay.TupleGetItem(func_2179_call(), 1)
call_2572 = relay.TupleGetItem(func_2180_call(), 1)
func_1348_call = mod.get_global_var('func_1348')
func_1351_call = mutated_mod.get_global_var('func_1351')
var_2574 = relay.var("var_2574", dtype = "int64", shape = (192,))#candidate|2574|(192,)|var|int64
call_2573 = relay.TupleGetItem(func_1348_call(relay.reshape(var_2574.astype('int64'), [1, 192])), 2)
call_2575 = relay.TupleGetItem(func_1351_call(relay.reshape(var_2574.astype('int64'), [1, 192])), 2)
output = relay.Tuple([call_2571,call_2573,var_2574,])
output2 = relay.Tuple([call_2572,call_2575,var_2574,])
func_2581 = relay.Function([var_2574,], output)
mod['func_2581'] = func_2581
mod = relay.transform.InferType()(mod)
var_2582 = relay.var("var_2582", dtype = "int64", shape = (192,))#candidate|2582|(192,)|var|int64
output = func_2581(var_2582)
func_2583 = relay.Function([var_2582], output)
mutated_mod['func_2583'] = func_2583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_973_call = mod.get_global_var('func_973')
func_975_call = mutated_mod.get_global_var('func_975')
call_2617 = relay.TupleGetItem(func_973_call(), 1)
call_2618 = relay.TupleGetItem(func_975_call(), 1)
func_1880_call = mod.get_global_var('func_1880')
func_1883_call = mutated_mod.get_global_var('func_1883')
var_2620 = relay.var("var_2620", dtype = "uint8", shape = (156,))#candidate|2620|(156,)|var|uint8
call_2619 = relay.TupleGetItem(func_1880_call(relay.reshape(var_2620.astype('uint8'), [4, 3, 13]), relay.reshape(var_2620.astype('uint8'), [4, 3, 13]), ), 0)
call_2621 = relay.TupleGetItem(func_1883_call(relay.reshape(var_2620.astype('uint8'), [4, 3, 13]), relay.reshape(var_2620.astype('uint8'), [4, 3, 13]), ), 0)
func_629_call = mod.get_global_var('func_629')
func_632_call = mutated_mod.get_global_var('func_632')
call_2628 = relay.TupleGetItem(func_629_call(relay.reshape(call_2617.astype('uint64'), [8, 4, 1])), 1)
call_2629 = relay.TupleGetItem(func_632_call(relay.reshape(call_2617.astype('uint64'), [8, 4, 1])), 1)
output = relay.Tuple([call_2617,call_2619,var_2620,call_2628,])
output2 = relay.Tuple([call_2618,call_2621,var_2620,call_2629,])
func_2639 = relay.Function([var_2620,], output)
mod['func_2639'] = func_2639
mod = relay.transform.InferType()(mod)
mutated_mod['func_2639'] = func_2639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2640 = relay.var("var_2640", dtype = "uint8", shape = (156,))#candidate|2640|(156,)|var|uint8
func_2639_call = mutated_mod.get_global_var('func_2639')
call_2641 = func_2639_call(var_2640)
output = call_2641
func_2642 = relay.Function([var_2640], output)
mutated_mod['func_2642'] = func_2642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_2652 = relay.TupleGetItem(func_1030_call(), 0)
call_2653 = relay.TupleGetItem(func_1031_call(), 0)
const_2657 = relay.const([[[-6.893092,5.776274,6.668265,5.362344,-0.716305,5.551039,4.019328,2.967156],[4.622171,3.096229,4.265449,-0.197234,-1.478279,0.006382,-1.502991,0.104903],[-3.181730,-7.972774,-7.650030,-8.409698,-6.635631,-2.101144,-6.707048,6.769506],[-9.439025,-9.551166,8.484987,-5.397171,7.055883,-3.707220,-1.409078,-6.678135],[-1.174656,-6.945089,-4.062022,6.616428,-0.668061,2.925613,-5.424212,-1.501326],[2.648764,-4.567027,-7.236683,-4.288755,-0.808509,1.028805,-5.291603,-6.680623],[-0.421361,2.539657,6.599507,3.972881,1.601885,-2.864636,-9.857498,-7.918426],[2.968608,-1.778475,0.913513,-5.698047,6.850708,-5.420131,6.663095,-0.552690],[8.026287,7.702103,6.549376,-1.638725,8.011488,-6.711101,-8.925807,9.240254],[3.144262,8.030237,-3.549463,4.685108,4.561397,7.516589,-2.406756,-5.315240],[-1.276704,-0.615180,5.694718,-5.117020,-6.938299,-8.256222,7.556591,-4.181211],[7.422569,1.573017,9.963589,6.704456,-6.088849,-0.455124,-9.882618,-6.592273]],[[-0.918886,-5.298410,6.851564,-1.950852,8.971314,-4.852805,-8.304459,-8.478888],[-5.286309,7.353026,-2.750441,-6.840668,8.191477,4.531730,-8.072608,-4.885003],[-6.601901,-1.421464,0.740890,0.262987,5.274962,1.138414,8.112603,3.346187],[9.996977,1.393501,6.801615,-3.021143,-0.466516,-5.632727,2.852273,7.469553],[-9.274414,-4.286031,-6.149472,-4.254378,3.902564,8.598738,0.976372,3.211106],[3.075713,-8.178644,-0.037650,-6.103125,-0.774028,2.167498,3.087428,-8.200362],[-4.099404,-7.768718,-7.947105,-0.058722,-4.611585,-2.673010,-6.941342,6.608477],[5.152961,-9.254240,-7.950503,-1.466772,-1.207544,9.097123,1.924514,3.670230],[-3.111828,-5.585091,-1.783488,-4.690627,0.010910,9.802351,-9.566421,7.254543],[-2.390911,-9.231835,-0.482282,-9.430913,-2.166890,7.645053,4.720489,-2.497811],[-4.949292,-0.443828,9.713414,2.681452,-2.253257,9.718918,3.452471,-6.744005],[-9.123922,2.683840,3.802699,3.814336,4.174064,9.145869,2.094389,-5.619161]],[[5.750854,3.660305,7.749896,4.869647,2.518748,9.604984,5.252019,-8.746752],[-4.978587,8.202560,2.329225,1.047427,9.186584,4.267395,-2.624503,-6.957060],[0.897850,6.738152,-8.108132,-1.207112,2.979815,8.795196,7.205833,-5.045042],[1.455147,3.488984,4.738753,5.929939,-2.982953,3.442189,-3.539540,-3.178384],[9.129491,-3.300146,-0.577751,3.447814,-1.499328,-1.553016,7.839772,6.868082],[-5.271886,8.090293,-4.507311,-8.370482,-9.769044,7.107527,4.020112,-3.644820],[6.617214,5.999350,7.150507,2.184156,9.846452,0.189113,5.278804,6.959954],[6.998820,0.385839,1.862020,-3.081320,3.922472,-7.946360,2.188314,-3.906722],[4.564624,-3.700533,-5.101946,7.693491,-7.365845,-2.264670,4.628546,2.356670],[4.155080,-1.807604,2.126214,-9.461454,7.802952,0.262103,7.475064,9.132690],[9.721487,5.520949,-9.082835,2.539879,6.525195,-5.718748,5.691557,9.199702],[-6.518917,4.092916,0.997417,-9.201000,-9.775582,0.555283,3.728133,4.233375]],[[8.939767,6.016359,8.900104,-8.685551,-6.224923,3.766571,-0.494847,-4.995418],[0.883810,-3.564991,2.642653,2.329516,1.444639,6.560040,6.512923,8.273232],[0.878697,-1.291000,-3.208174,2.006355,2.098596,-5.294552,-6.055230,-0.017725],[8.002111,-7.764908,-9.823232,-0.665948,-8.385906,-7.051441,-7.159442,-3.585015],[-7.768157,-9.861482,5.988987,-4.102744,9.586652,7.546148,8.811538,7.844459],[-9.105354,-1.325419,9.509295,-0.793634,-1.745144,0.277890,8.173089,0.378556],[3.429913,-7.789199,3.108608,0.645825,6.969163,-8.700839,2.601691,3.429046],[4.523674,-8.153248,4.852977,4.931093,7.390511,-0.429883,-5.615606,0.758879],[-7.027266,2.415963,-7.580358,-9.389691,9.276348,-3.179904,-6.798216,-4.573798],[8.593808,-3.798286,-6.209806,9.594533,-5.789444,-8.864504,0.815186,-0.639599],[4.872508,8.632533,8.908745,7.237920,2.537641,3.204447,-7.080607,7.229457],[-5.645332,-1.501062,5.228007,-6.788457,9.312345,7.774912,-1.383693,-0.638882]]], dtype = "float32")#candidate|2657|(4, 12, 8)|const|float32
bop_2658 = relay.equal(call_2652.astype('bool'), relay.reshape(const_2657.astype('bool'), relay.shape_of(call_2652))) # shape=(4, 12, 8)
bop_2661 = relay.equal(call_2653.astype('bool'), relay.reshape(const_2657.astype('bool'), relay.shape_of(call_2653))) # shape=(4, 12, 8)
bop_2670 = relay.not_equal(const_2657.astype('bool'), relay.reshape(call_2652.astype('bool'), relay.shape_of(const_2657))) # shape=(4, 12, 8)
bop_2673 = relay.not_equal(const_2657.astype('bool'), relay.reshape(call_2653.astype('bool'), relay.shape_of(const_2657))) # shape=(4, 12, 8)
func_629_call = mod.get_global_var('func_629')
func_632_call = mutated_mod.get_global_var('func_632')
const_2677 = relay.const([6,-8,-6,-7,-4,9,1,5,3,-7,-6,2,1,8,-6,-6,8,7,10,-10,1,8,-7,-2,-2,-7,-1,10,-4,-6,5,3], dtype = "uint64")#candidate|2677|(32,)|const|uint64
call_2676 = relay.TupleGetItem(func_629_call(relay.reshape(const_2677.astype('uint64'), [8, 4, 1])), 1)
call_2678 = relay.TupleGetItem(func_632_call(relay.reshape(const_2677.astype('uint64'), [8, 4, 1])), 1)
var_2679 = relay.var("var_2679", dtype = "float32", shape = (4, 12, 8))#candidate|2679|(4, 12, 8)|var|float32
bop_2680 = relay.floor_divide(const_2657.astype('float64'), relay.reshape(var_2679.astype('float64'), relay.shape_of(const_2657))) # shape=(4, 12, 8)
output = relay.Tuple([bop_2658,bop_2670,call_2676,const_2677,bop_2680,])
output2 = relay.Tuple([bop_2661,bop_2673,call_2678,const_2677,bop_2680,])
func_2686 = relay.Function([var_2679,], output)
mod['func_2686'] = func_2686
mod = relay.transform.InferType()(mod)
mutated_mod['func_2686'] = func_2686
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2687 = relay.var("var_2687", dtype = "float32", shape = (4, 12, 8))#candidate|2687|(4, 12, 8)|var|float32
func_2686_call = mutated_mod.get_global_var('func_2686')
call_2688 = func_2686_call(var_2687)
output = call_2688
func_2689 = relay.Function([var_2687], output)
mutated_mod['func_2689'] = func_2689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_838_call = mod.get_global_var('func_838')
func_839_call = mutated_mod.get_global_var('func_839')
call_2738 = relay.TupleGetItem(func_838_call(), 0)
call_2739 = relay.TupleGetItem(func_839_call(), 0)
func_1294_call = mod.get_global_var('func_1294')
func_1295_call = mutated_mod.get_global_var('func_1295')
call_2751 = relay.TupleGetItem(func_1294_call(), 0)
call_2752 = relay.TupleGetItem(func_1295_call(), 0)
output = relay.Tuple([call_2738,call_2751,])
output2 = relay.Tuple([call_2739,call_2752,])
func_2753 = relay.Function([], output)
mod['func_2753'] = func_2753
mod = relay.transform.InferType()(mod)
mutated_mod['func_2753'] = func_2753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2753_call = mutated_mod.get_global_var('func_2753')
call_2754 = func_2753_call()
output = call_2754
func_2755 = relay.Function([], output)
mutated_mod['func_2755'] = func_2755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_448_call = mod.get_global_var('func_448')
func_450_call = mutated_mod.get_global_var('func_450')
call_2756 = relay.TupleGetItem(func_448_call(), 2)
call_2757 = relay.TupleGetItem(func_450_call(), 2)
func_2141_call = mod.get_global_var('func_2141')
func_2142_call = mutated_mod.get_global_var('func_2142')
call_2784 = relay.TupleGetItem(func_2141_call(), 0)
call_2785 = relay.TupleGetItem(func_2142_call(), 0)
output = relay.Tuple([call_2756,call_2784,])
output2 = relay.Tuple([call_2757,call_2785,])
func_2797 = relay.Function([], output)
mod['func_2797'] = func_2797
mod = relay.transform.InferType()(mod)
mutated_mod['func_2797'] = func_2797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2797_call = mutated_mod.get_global_var('func_2797')
call_2798 = func_2797_call()
output = call_2798
func_2799 = relay.Function([], output)
mutated_mod['func_2799'] = func_2799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_2811 = relay.TupleGetItem(func_526_call(), 0)
call_2812 = relay.TupleGetItem(func_527_call(), 0)
output = relay.Tuple([call_2811,])
output2 = relay.Tuple([call_2812,])
func_2826 = relay.Function([], output)
mod['func_2826'] = func_2826
mod = relay.transform.InferType()(mod)
mutated_mod['func_2826'] = func_2826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2826_call = mutated_mod.get_global_var('func_2826')
call_2827 = func_2826_call()
output = call_2827
func_2828 = relay.Function([], output)
mutated_mod['func_2828'] = func_2828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2866 = relay.var("var_2866", dtype = "uint32", shape = (7, 1, 10))#candidate|2866|(7, 1, 10)|var|uint32
var_2867 = relay.var("var_2867", dtype = "uint32", shape = (7, 16, 10))#candidate|2867|(7, 16, 10)|var|uint32
bop_2868 = relay.less_equal(var_2866.astype('bool'), var_2867.astype('bool')) # shape=(7, 16, 10)
func_1509_call = mod.get_global_var('func_1509')
func_1510_call = mutated_mod.get_global_var('func_1510')
call_2876 = relay.TupleGetItem(func_1509_call(), 0)
call_2877 = relay.TupleGetItem(func_1510_call(), 0)
uop_2894 = relay.erf(call_2876.astype('float64')) # shape=(8, 15, 5)
uop_2896 = relay.erf(call_2877.astype('float64')) # shape=(8, 15, 5)
func_2639_call = mod.get_global_var('func_2639')
func_2642_call = mutated_mod.get_global_var('func_2642')
const_2905 = relay.const([1,4,-9,-6,5,8,9,-5,9,3,8,2,-3,-5,3,7,7,-9,-10,-1,-3,10,10,10,-3,-7,8,6,-8,-2,6,8,-5,-2,-10,-1,1,-6,9,10,8,10,1,-9,1,-2,5,2,5,-4,-8,-1,-6,-10,2,6,9,7,-4,-1,-10,-3,2,-2,1,5,2,-6,2,3,8,-5,-7,-1,1,-7,-4,3,-8,-7,2,6,-8,2,2,6,-9,1,5,7,1,-4,-4,2,-1,-1,-9,-7,-1,6,8,-5,5,1,5,6,3,2,-9,9,1,5,7,8,-2,-1,-10,-7,2,5,-9,-3,2,-10,-10,-3,9,5,-9,-3,-1,3,-3,-6,-2,2,3,2,3,-8,-10,-7,6,-4,7,8,-4,-9,3,9,8,7,-9,9,-10,6], dtype = "uint8")#candidate|2905|(156,)|const|uint8
call_2904 = relay.TupleGetItem(func_2639_call(relay.reshape(const_2905.astype('uint8'), [156,])), 0)
call_2906 = relay.TupleGetItem(func_2642_call(relay.reshape(const_2905.astype('uint8'), [156,])), 0)
uop_2913 = relay.log2(var_2867.astype('float32')) # shape=(7, 16, 10)
func_2753_call = mod.get_global_var('func_2753')
func_2755_call = mutated_mod.get_global_var('func_2755')
call_2919 = relay.TupleGetItem(func_2753_call(), 1)
call_2920 = relay.TupleGetItem(func_2755_call(), 1)
output = relay.Tuple([bop_2868,uop_2894,call_2904,const_2905,uop_2913,call_2919,])
output2 = relay.Tuple([bop_2868,uop_2896,call_2906,const_2905,uop_2913,call_2920,])
func_2925 = relay.Function([var_2866,var_2867,], output)
mod['func_2925'] = func_2925
mod = relay.transform.InferType()(mod)
mutated_mod['func_2925'] = func_2925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2925_call = mutated_mod.get_global_var('func_2925')
var_2927 = relay.var("var_2927", dtype = "uint32", shape = (7, 1, 10))#candidate|2927|(7, 1, 10)|var|uint32
var_2928 = relay.var("var_2928", dtype = "uint32", shape = (7, 16, 10))#candidate|2928|(7, 16, 10)|var|uint32
call_2926 = func_2925_call(var_2927,var_2928,)
output = call_2926
func_2929 = relay.Function([var_2927,var_2928,], output)
mutated_mod['func_2929'] = func_2929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_3000 = relay.TupleGetItem(func_477_call(), 0)
call_3001 = relay.TupleGetItem(func_479_call(), 0)
func_1223_call = mod.get_global_var('func_1223')
func_1225_call = mutated_mod.get_global_var('func_1225')
call_3002 = relay.TupleGetItem(func_1223_call(), 1)
call_3003 = relay.TupleGetItem(func_1225_call(), 1)
func_1294_call = mod.get_global_var('func_1294')
func_1295_call = mutated_mod.get_global_var('func_1295')
call_3016 = relay.TupleGetItem(func_1294_call(), 0)
call_3017 = relay.TupleGetItem(func_1295_call(), 0)
output = relay.Tuple([call_3000,call_3002,call_3016,])
output2 = relay.Tuple([call_3001,call_3003,call_3017,])
func_3019 = relay.Function([], output)
mod['func_3019'] = func_3019
mod = relay.transform.InferType()(mod)
output = func_3019()
func_3020 = relay.Function([], output)
mutated_mod['func_3020'] = func_3020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3104 = relay.var("var_3104", dtype = "float32", shape = (8, 10, 8))#candidate|3104|(8, 10, 8)|var|float32
uop_3105 = relay.sqrt(var_3104.astype('float32')) # shape=(8, 10, 8)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
var_3125 = relay.var("var_3125", dtype = "float32", shape = (315,))#candidate|3125|(315,)|var|float32
call_3124 = func_1016_call(relay.reshape(var_3125.astype('float32'), [3, 15, 7]))
call_3126 = func_1016_call(relay.reshape(var_3125.astype('float32'), [3, 15, 7]))
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
var_3128 = relay.var("var_3128", dtype = "float32", shape = (84,))#candidate|3128|(84,)|var|float32
call_3127 = relay.TupleGetItem(func_1209_call(relay.reshape(var_3128.astype('float32'), [84,])), 2)
call_3129 = relay.TupleGetItem(func_1211_call(relay.reshape(var_3128.astype('float32'), [84,])), 2)
uop_3148 = relay.cosh(uop_3105.astype('float32')) # shape=(8, 10, 8)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_3162 = relay.TupleGetItem(func_526_call(), 0)
call_3163 = relay.TupleGetItem(func_527_call(), 0)
func_1812_call = mod.get_global_var('func_1812')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_3168 = func_1812_call()
call_3169 = func_1812_call()
output = relay.Tuple([call_3124,var_3125,call_3127,var_3128,uop_3148,call_3162,call_3168,])
output2 = relay.Tuple([call_3126,var_3125,call_3129,var_3128,uop_3148,call_3163,call_3169,])
func_3170 = relay.Function([var_3104,var_3125,var_3128,], output)
mod['func_3170'] = func_3170
mod = relay.transform.InferType()(mod)
mutated_mod['func_3170'] = func_3170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3170_call = mutated_mod.get_global_var('func_3170')
var_3172 = relay.var("var_3172", dtype = "float32", shape = (8, 10, 8))#candidate|3172|(8, 10, 8)|var|float32
var_3173 = relay.var("var_3173", dtype = "float32", shape = (315,))#candidate|3173|(315,)|var|float32
var_3174 = relay.var("var_3174", dtype = "float32", shape = (84,))#candidate|3174|(84,)|var|float32
call_3171 = func_3170_call(var_3172,var_3173,var_3174,)
output = call_3171
func_3175 = relay.Function([var_3172,var_3173,var_3174,], output)
mutated_mod['func_3175'] = func_3175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mod.get_global_var('func_1223')
func_1225_call = mutated_mod.get_global_var('func_1225')
call_3199 = relay.TupleGetItem(func_1223_call(), 0)
call_3200 = relay.TupleGetItem(func_1225_call(), 0)
var_3203 = relay.var("var_3203", dtype = "float64", shape = (2, 192))#candidate|3203|(2, 192)|var|float64
bop_3204 = relay.multiply(call_3199.astype('float32'), relay.reshape(var_3203.astype('float32'), relay.shape_of(call_3199))) # shape=(2, 192)
bop_3207 = relay.multiply(call_3200.astype('float32'), relay.reshape(var_3203.astype('float32'), relay.shape_of(call_3200))) # shape=(2, 192)
uop_3214 = relay.log10(bop_3204.astype('float64')) # shape=(2, 192)
uop_3216 = relay.log10(bop_3207.astype('float64')) # shape=(2, 192)
uop_3223 = relay.exp(call_3199.astype('float64')) # shape=(2, 192)
uop_3225 = relay.exp(call_3200.astype('float64')) # shape=(2, 192)
func_1433_call = mod.get_global_var('func_1433')
func_1435_call = mutated_mod.get_global_var('func_1435')
call_3232 = relay.TupleGetItem(func_1433_call(), 0)
call_3233 = relay.TupleGetItem(func_1435_call(), 0)
func_780_call = mod.get_global_var('func_780')
func_783_call = mutated_mod.get_global_var('func_783')
call_3238 = relay.TupleGetItem(func_780_call(relay.reshape(bop_3204.astype('bool'), [4, 12, 8])), 2)
call_3239 = relay.TupleGetItem(func_783_call(relay.reshape(bop_3204.astype('bool'), [4, 12, 8])), 2)
const_3243 = relay.const([[7.203263,3.320490,-2.086281,-3.939867,-5.286352,-6.062431,8.396675,4.607744,-8.466452,-7.746990,-1.043373,4.150210,-5.693807,-4.465637,2.785889,-9.093599,1.107043,6.228215,8.309891,-2.115464,4.116618,-9.596657,0.460591,-9.324208,6.360377,-3.682736,-5.970348,4.633326,3.117543,-2.732934,7.059117,3.645199,-0.332299,-3.286396,9.117915,-3.951553,0.026113,8.658127,-6.463213,9.254268,-8.454279,9.989144,7.534655,-1.754095,4.263085,3.803869,0.652856,4.243295,-7.007117,3.387482,-7.003804,-3.006325,9.805386,-2.140292,5.529403,3.035749,-9.837829,4.748463,-9.295951,-4.321333,-3.335122,-1.486494,3.713563,7.762646,-7.798253,5.414283,-5.717001,-7.318653,4.869264,4.001068,-8.329178,-1.660872,-7.295100,8.320950,5.505358,-1.156474,0.775332,-4.800673,-8.262169,-0.037050,-8.700061,-3.064863,-4.053443,-4.007989,7.269462,-7.538821,4.330043,-5.239970,-3.063225,-8.491744,-0.842786,4.300859,3.100862,-9.403032,-6.069888,-3.769551,-1.182314,3.885327,-1.818542,-4.625016,-6.593325,0.649049,7.392382,8.745528,1.193500,-6.533812,-7.728214,-8.285167,8.300334,0.391394,2.012024,-7.289555,-8.796207,-4.619038,-6.610913,0.883851,-0.911046,-5.647527,-4.825210,7.889483,4.793467,1.282481,-3.706168,4.543568,-6.913126,6.051822,4.816965,9.649968,7.432720,-9.560816,-0.452025,-6.040358,-8.774457,3.445024,-4.447108,5.113346,-4.860073,1.848719,-3.930449,-0.999942,-5.602692,-8.784626,5.764358,2.699062,-8.028510,-5.103211,3.055557,6.310068,4.958231,7.643987,2.880330,3.524044,8.987346,-6.381465,-9.244634,4.748245,-7.939409,-8.652119,9.337322,2.955891,8.329002,1.520155,-8.380015,-2.514895,5.879863,-6.545162,-8.498757,-3.604921,-1.486379,1.496632,6.772920,9.375057,8.794052,6.910043,-3.693809,-0.794303,7.940968,-5.243121,-3.807989,6.605287,-1.403945,-4.522992,-0.734482,8.729011,-2.836094,1.345951,3.044045,8.258177,-9.380857,8.637968,5.680919,-3.882066],[6.269035,2.476817,4.131486,6.196510,-5.206326,4.550720,-2.687673,7.918926,1.047384,-8.067681,-9.898119,1.966344,8.269800,2.850531,-8.786209,7.415922,-4.158636,2.951070,1.485491,-7.973573,2.537366,-5.616218,-6.539395,-8.266788,-9.674532,-7.135867,-8.801279,6.466236,-9.784773,6.249141,-1.056941,7.924035,1.302518,0.349285,1.410834,-5.636985,0.447573,4.450457,-7.613385,4.101061,-3.731244,5.481548,-7.361347,-5.458938,2.819432,5.027548,-5.604473,5.644483,-6.482841,0.358915,-5.015976,-8.072856,-9.023994,3.331518,7.497153,-4.697035,-5.091102,-5.912497,-1.281713,9.335755,-1.039231,-7.643997,8.340867,-3.934398,-8.772448,-4.655480,8.441397,-2.417884,-2.475758,5.500357,-4.416581,5.733290,0.533555,4.952987,4.519740,-2.794460,-2.140845,-7.128615,-6.780942,3.916502,-7.588875,6.037077,-4.082927,-8.648587,7.219477,-5.419676,8.300491,-8.443895,7.225694,-8.184751,-6.683205,7.094888,4.736872,6.651457,-1.578365,-4.353366,-9.990020,1.111058,8.210446,1.842600,4.702939,9.369872,4.556691,0.897091,4.614808,1.466151,-0.251414,-5.509011,6.701871,1.920261,-7.321621,-8.191452,9.737966,6.268620,4.315427,0.253895,-9.523307,7.129049,-3.628501,2.991363,9.641753,-7.547903,9.955160,4.350688,-6.572151,-7.223091,2.983473,1.815211,-7.070860,1.507814,5.962323,-4.990590,8.055009,3.523563,8.651515,-1.292614,-4.905786,-8.431731,2.793030,-5.628740,6.412421,2.091408,9.649799,4.144909,0.004548,-2.031304,-2.848305,5.207914,-9.337613,2.157522,1.464650,-4.247199,-9.331657,8.070036,0.313794,8.120573,-0.751782,5.389143,0.147324,-8.400420,4.535201,7.522287,8.651522,-7.902604,-7.332335,9.644120,3.889265,6.176645,5.197737,2.346138,-0.893732,5.018329,8.466514,-3.895505,8.516215,-5.866413,1.617187,-5.865267,-3.118212,0.348954,9.396549,-4.533765,-1.432121,-1.890771,-6.134232,-2.309469,0.749333,9.921476,-5.520124,5.567982,-5.145616,9.294674]], dtype = "float64")#candidate|3243|(2, 192)|const|float64
bop_3244 = relay.greater_equal(uop_3223.astype('bool'), relay.reshape(const_3243.astype('bool'), relay.shape_of(uop_3223))) # shape=(2, 192)
bop_3247 = relay.greater_equal(uop_3225.astype('bool'), relay.reshape(const_3243.astype('bool'), relay.shape_of(uop_3225))) # shape=(2, 192)
uop_3258 = relay.acos(var_3203.astype('float32')) # shape=(2, 192)
output = relay.Tuple([uop_3214,call_3232,call_3238,bop_3244,uop_3258,])
output2 = relay.Tuple([uop_3216,call_3233,call_3239,bop_3247,uop_3258,])
func_3262 = relay.Function([var_3203,], output)
mod['func_3262'] = func_3262
mod = relay.transform.InferType()(mod)
var_3263 = relay.var("var_3263", dtype = "float64", shape = (2, 192))#candidate|3263|(2, 192)|var|float64
output = func_3262(var_3263)
func_3264 = relay.Function([var_3263], output)
mutated_mod['func_3264'] = func_3264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_578_call = mod.get_global_var('func_578')
func_579_call = mutated_mod.get_global_var('func_579')
call_3269 = relay.TupleGetItem(func_578_call(), 1)
call_3270 = relay.TupleGetItem(func_579_call(), 1)
output = call_3269
output2 = call_3270
func_3275 = relay.Function([], output)
mod['func_3275'] = func_3275
mod = relay.transform.InferType()(mod)
output = func_3275()
func_3276 = relay.Function([], output)
mutated_mod['func_3276'] = func_3276
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3379 = relay.var("var_3379", dtype = "float64", shape = ())#candidate|3379|()|var|float64
const_3380 = relay.const([[[7.955770,-2.861347,8.238825,-8.430572],[2.500260,-1.402671,-3.476938,-8.079730],[-6.191904,6.236502,-0.489705,9.346455],[-4.154067,-3.210701,3.682695,9.190120],[3.105192,1.540535,-7.743496,1.786498],[6.447603,4.241251,1.792406,4.467322],[-6.005283,3.029690,6.584825,-9.541678],[-0.854928,-9.053000,-5.752418,5.018506]],[[-4.269260,-3.918739,-4.782623,-7.385961],[8.286548,6.125476,1.605558,-0.881699],[1.401846,7.733446,9.585163,-4.665182],[-4.347526,2.398174,-9.749446,-9.611250],[0.638558,5.141768,-6.937256,2.909074],[-1.098153,-7.492193,-0.403095,2.448525],[-2.791667,-3.720552,-5.050905,-2.724658],[6.013580,-7.019300,-5.567824,-1.385387]],[[8.459548,1.983337,-5.283650,-3.934263],[-4.985229,-7.601791,2.983631,-4.161543],[-0.095314,4.180028,-0.238264,7.700147],[2.872950,1.461775,-8.550282,3.471666],[-2.725024,-3.838342,-3.275667,4.293896],[5.231864,5.393160,2.351978,9.199102],[-8.242602,-1.742827,-9.785249,-2.914494],[0.122193,9.704087,-1.179139,-5.844728]],[[0.224709,1.341480,9.229197,-3.521562],[-6.125501,9.396871,-7.080059,-8.645490],[-1.232463,3.464803,-8.852422,-5.112705],[1.983826,-7.342085,8.569382,-3.765987],[0.706796,-8.137400,-1.658944,8.894533],[-0.009089,-8.222272,4.854231,5.209833],[-1.033902,-5.766856,-3.890432,-9.273421],[-0.250320,3.440235,1.359261,2.668404]],[[7.771661,1.601309,-2.636862,9.998581],[-6.518286,2.911489,-0.075477,9.854055],[6.571455,5.054757,-8.324700,-2.743202],[-5.973986,-5.529218,7.562260,-9.000991],[9.705628,9.001664,6.455462,-0.755078],[-5.241375,8.637549,-8.866644,9.267033],[0.600530,-7.312973,3.041061,-0.032900],[-1.273810,0.256033,-8.083763,2.181534]],[[-5.025670,-4.663758,8.103234,4.392993],[-4.765387,-1.889679,7.572464,2.355842],[-4.612968,-2.349251,-0.116715,-7.647664],[-8.021130,-5.616036,2.490141,-7.221754],[-4.388402,5.431100,-2.088970,-0.956502],[-2.159210,0.821428,-7.956343,-1.577885],[-0.197466,-7.741785,3.992427,-4.814896],[3.823111,5.621630,-9.555912,-3.751915]],[[-7.866761,-6.034944,-7.958620,8.316009],[7.616042,-0.044045,8.878250,-6.657047],[2.489360,-0.441391,6.909584,-8.444392],[-5.697864,-5.422177,-8.169629,7.162895],[-0.598488,6.409748,-3.935818,0.803058],[7.695016,-6.710257,-7.318971,5.818450],[5.912780,0.159616,-1.410494,1.005049],[9.625184,0.973585,-3.695203,-3.687257]],[[-3.899152,1.849883,-4.265209,-1.390387],[-2.367239,2.742030,4.734067,6.801360],[-5.929802,-2.086828,-0.508641,0.934470],[5.173948,3.727006,-3.807335,-5.012355],[5.785512,0.380830,7.648959,-9.651334],[-2.159068,-5.064252,-7.385916,5.257696],[-6.725492,3.748005,5.968531,-2.474947],[1.743408,5.702486,4.661032,-3.108312]],[[8.752485,6.760562,0.756454,3.678347],[4.210227,0.313428,0.543756,-2.903698],[-7.164320,-5.102161,2.977370,-5.064924],[8.025261,-8.164220,-9.346244,2.507502],[-0.996826,-1.644163,-4.164067,-1.817248],[3.185992,0.079999,-9.789135,2.372582],[0.970151,-3.500791,-4.582707,7.346645],[-0.716633,4.189141,-2.860249,7.316569]],[[7.638372,-1.048413,1.364803,7.003294],[7.566420,6.623209,-2.936643,-4.513623],[-9.718801,-3.171484,-5.773929,-4.237905],[2.333157,2.747135,6.774777,5.109354],[-4.988566,-7.392594,-1.698639,-9.394541],[4.851212,0.310466,-7.678815,8.138865],[-6.682390,-4.917300,-2.872684,-5.557814],[-2.979624,6.172803,-6.180205,-1.136647]],[[1.021791,-8.061857,-8.078051,6.871612],[-0.679660,1.866778,-9.659687,7.315834],[4.845131,9.410617,2.334035,2.201094],[2.912985,0.135199,7.263009,-8.442652],[-7.679626,-1.345140,-7.959025,-6.510397],[-1.783343,6.083550,9.275569,-0.687645],[-4.086071,-9.136178,1.927652,6.457791],[-1.658557,-0.526917,-1.167644,-2.344870]]], dtype = "float64")#candidate|3380|(11, 8, 4)|const|float64
bop_3381 = relay.mod(var_3379.astype('float64'), const_3380.astype('float64')) # shape=(11, 8, 4)
func_1546_call = mod.get_global_var('func_1546')
func_1550_call = mutated_mod.get_global_var('func_1550')
const_3391 = relay.const([-10,3,-5,-2,-5,1,7,-5,5,-1,8,10,-7,-8,-7,-8,-7,6,9,-4,6,10,-5,10,-3,-2,1,4,8,-10,1,3,-1,2,1,-8,-1,-10,-7,10,-3,9,-6,-9,-9,9,-9,7,-5,1,5,3,-10,-6,-5,-5,9,-10,10,-9,-2,-6,5,10,2,-4,-3,-5,-9,-7,7,3], dtype = "int64")#candidate|3391|(72,)|const|int64
call_3390 = func_1546_call(relay.reshape(const_3391.astype('int64'), [3, 3, 8]), relay.reshape(const_3391.astype('int64'), [3, 3, 8]), )
call_3392 = func_1546_call(relay.reshape(const_3391.astype('int64'), [3, 3, 8]), relay.reshape(const_3391.astype('int64'), [3, 3, 8]), )
output = relay.Tuple([bop_3381,call_3390,const_3391,])
output2 = relay.Tuple([bop_3381,call_3392,const_3391,])
func_3393 = relay.Function([var_3379,], output)
mod['func_3393'] = func_3393
mod = relay.transform.InferType()(mod)
mutated_mod['func_3393'] = func_3393
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3394 = relay.var("var_3394", dtype = "float64", shape = ())#candidate|3394|()|var|float64
func_3393_call = mutated_mod.get_global_var('func_3393')
call_3395 = func_3393_call(var_3394)
output = call_3395
func_3396 = relay.Function([var_3394], output)
mutated_mod['func_3396'] = func_3396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2390_call = mod.get_global_var('func_2390')
func_2392_call = mutated_mod.get_global_var('func_2392')
call_3487 = relay.TupleGetItem(func_2390_call(), 0)
call_3488 = relay.TupleGetItem(func_2392_call(), 0)
output = relay.Tuple([call_3487,])
output2 = relay.Tuple([call_3488,])
func_3493 = relay.Function([], output)
mod['func_3493'] = func_3493
mod = relay.transform.InferType()(mod)
output = func_3493()
func_3494 = relay.Function([], output)
mutated_mod['func_3494'] = func_3494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1048_call = mod.get_global_var('func_1048')
func_1049_call = mutated_mod.get_global_var('func_1049')
call_3495 = func_1048_call()
call_3496 = func_1048_call()
var_3499 = relay.var("var_3499", dtype = "float32", shape = (3, 15, 7))#candidate|3499|(3, 15, 7)|var|float32
bop_3500 = relay.equal(call_3495.astype('bool'), relay.reshape(var_3499.astype('bool'), relay.shape_of(call_3495))) # shape=(3, 15, 7)
bop_3503 = relay.equal(call_3496.astype('bool'), relay.reshape(var_3499.astype('bool'), relay.shape_of(call_3496))) # shape=(3, 15, 7)
func_780_call = mod.get_global_var('func_780')
func_783_call = mutated_mod.get_global_var('func_783')
var_3516 = relay.var("var_3516", dtype = "bool", shape = (384,))#candidate|3516|(384,)|var|bool
call_3515 = relay.TupleGetItem(func_780_call(relay.reshape(var_3516.astype('bool'), [4, 12, 8])), 2)
call_3517 = relay.TupleGetItem(func_783_call(relay.reshape(var_3516.astype('bool'), [4, 12, 8])), 2)
output = relay.Tuple([bop_3500,call_3515,var_3516,])
output2 = relay.Tuple([bop_3503,call_3517,var_3516,])
func_3536 = relay.Function([var_3499,var_3516,], output)
mod['func_3536'] = func_3536
mod = relay.transform.InferType()(mod)
var_3537 = relay.var("var_3537", dtype = "float32", shape = (3, 15, 7))#candidate|3537|(3, 15, 7)|var|float32
var_3538 = relay.var("var_3538", dtype = "bool", shape = (384,))#candidate|3538|(384,)|var|bool
output = func_3536(var_3537,var_3538,)
func_3539 = relay.Function([var_3537,var_3538,], output)
mutated_mod['func_3539'] = func_3539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3547 = relay.var("var_3547", dtype = "float32", shape = (4, 14, 1))#candidate|3547|(4, 14, 1)|var|float32
uop_3548 = relay.sqrt(var_3547.astype('float32')) # shape=(4, 14, 1)
var_3557 = relay.var("var_3557", dtype = "float32", shape = (4, 14, 16))#candidate|3557|(4, 14, 16)|var|float32
bop_3558 = relay.greater(uop_3548.astype('bool'), var_3557.astype('bool')) # shape=(4, 14, 16)
func_629_call = mod.get_global_var('func_629')
func_632_call = mutated_mod.get_global_var('func_632')
var_3575 = relay.var("var_3575", dtype = "uint64", shape = (32,))#candidate|3575|(32,)|var|uint64
call_3574 = relay.TupleGetItem(func_629_call(relay.reshape(var_3575.astype('uint64'), [8, 4, 1])), 0)
call_3576 = relay.TupleGetItem(func_632_call(relay.reshape(var_3575.astype('uint64'), [8, 4, 1])), 0)
output = relay.Tuple([bop_3558,call_3574,var_3575,])
output2 = relay.Tuple([bop_3558,call_3576,var_3575,])
func_3583 = relay.Function([var_3547,var_3557,var_3575,], output)
mod['func_3583'] = func_3583
mod = relay.transform.InferType()(mod)
var_3584 = relay.var("var_3584", dtype = "float32", shape = (4, 14, 1))#candidate|3584|(4, 14, 1)|var|float32
var_3585 = relay.var("var_3585", dtype = "float32", shape = (4, 14, 16))#candidate|3585|(4, 14, 16)|var|float32
var_3586 = relay.var("var_3586", dtype = "uint64", shape = (32,))#candidate|3586|(32,)|var|uint64
output = func_3583(var_3584,var_3585,var_3586,)
func_3587 = relay.Function([var_3584,var_3585,var_3586,], output)
mutated_mod['func_3587'] = func_3587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_973_call = mod.get_global_var('func_973')
func_975_call = mutated_mod.get_global_var('func_975')
call_3597 = relay.TupleGetItem(func_973_call(), 3)
call_3598 = relay.TupleGetItem(func_975_call(), 3)
var_3605 = relay.var("var_3605", dtype = "uint8", shape = (4, 12, 8))#candidate|3605|(4, 12, 8)|var|uint8
bop_3606 = relay.bitwise_xor(call_3597.astype('uint64'), relay.reshape(var_3605.astype('uint64'), relay.shape_of(call_3597))) # shape=(4, 12, 8)
bop_3609 = relay.bitwise_xor(call_3598.astype('uint64'), relay.reshape(var_3605.astype('uint64'), relay.shape_of(call_3598))) # shape=(4, 12, 8)
output = bop_3606
output2 = bop_3609
func_3610 = relay.Function([var_3605,], output)
mod['func_3610'] = func_3610
mod = relay.transform.InferType()(mod)
var_3611 = relay.var("var_3611", dtype = "uint8", shape = (4, 12, 8))#candidate|3611|(4, 12, 8)|var|uint8
output = func_3610(var_3611)
func_3612 = relay.Function([var_3611], output)
mutated_mod['func_3612'] = func_3612
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3639 = relay.const([[[-4.748846,-5.679436,-6.864929,-7.884927,-1.969763,1.587208,-2.978049,-2.369531,1.802055,4.821663,9.164282,-8.316942,8.220330,8.757839,-5.589585],[7.678528,-6.551518,-7.980139,0.321703,9.069680,-0.260813,-2.335124,-1.580468,-6.039708,8.386541,-5.448657,-1.538088,9.937751,1.468441,-3.893370],[4.315027,-4.216098,-4.570650,-8.288952,8.822754,4.613663,2.935036,-5.468783,2.286845,0.157586,-5.621986,6.878818,9.189327,5.287115,-6.254548],[-7.765825,1.328420,4.993452,4.570841,1.363986,-2.564918,-5.732795,-8.742461,0.140065,-5.998181,5.636600,-9.249535,9.452959,0.466252,-2.531709],[-6.379645,-3.391107,-3.820964,7.526989,7.341054,-1.435295,-6.918110,0.855937,-9.267965,-7.376812,-2.460433,6.934608,-5.803650,-1.810674,6.638154],[3.667579,0.660762,8.285674,-6.992406,2.865282,8.305558,6.776965,-1.160345,5.887274,0.135472,5.569397,5.085222,-8.210523,5.515603,4.539126],[-9.973203,3.608056,-6.746602,8.100497,5.904955,4.024248,-7.414878,-4.533259,4.583303,4.438592,1.831179,-2.047004,-7.017854,2.032118,0.950294],[-5.023143,2.306751,7.493015,3.925568,-7.575901,1.724786,5.603789,-8.717798,3.616497,4.580795,-2.358712,7.545201,3.537695,-7.678893,-7.388802],[-2.636844,8.041299,-0.074416,4.764441,3.511169,-0.713604,1.355431,-9.176439,-4.135496,-3.501144,2.472990,-2.175716,1.991111,-7.238060,-0.110390],[-9.427433,6.933915,8.460557,-5.713108,1.902693,-3.017939,2.429393,-4.073835,-3.813443,0.870882,-6.876646,8.406298,2.845125,4.940808,-3.102738],[-0.033221,-1.446113,-0.651150,1.623304,-2.467460,-1.493937,7.518332,2.168111,-1.392822,-7.024850,-7.224350,-6.828176,1.123389,-8.424777,9.250682]],[[5.571793,3.957518,7.847880,3.659509,5.573581,-9.304383,-3.810890,5.517145,9.412906,9.812029,7.493543,-6.921109,-6.723506,2.541057,-6.178902],[1.046325,1.069839,1.675608,0.075982,7.008117,3.686015,-8.624676,6.923975,9.862044,6.156418,-5.016878,-3.409709,-6.950419,0.016368,1.969678],[-3.223602,9.709588,-3.760349,6.209338,8.386365,-7.116433,-5.860251,-1.558592,-8.579514,-4.532291,3.999207,-9.581346,1.964461,-7.329730,-7.332738],[5.212458,-0.412210,-6.452051,9.027675,-1.141652,2.042040,6.687718,-2.812391,7.689934,3.444680,-3.481842,2.548625,-7.181241,-0.698985,7.391297],[5.584480,7.310870,6.158412,-7.592739,8.520522,3.240983,7.192215,-8.027098,-3.063178,-2.308917,3.417300,-9.299402,1.775228,-2.524624,3.052732],[-0.159630,-6.947180,3.504324,-6.249970,-2.056688,-8.016590,-7.699586,3.310382,2.424348,-8.387108,4.359016,4.142966,-9.749036,9.402837,-3.785798],[-5.141579,3.257192,-5.156968,-1.608470,-7.458136,6.660200,-4.030887,-1.831385,-7.588485,-0.464495,3.400080,5.682734,1.679905,6.238963,-9.177114],[-0.192750,-6.398873,4.507973,-2.123878,8.660120,-8.422415,8.015635,-7.688744,-7.364005,-6.914670,-3.624629,2.652605,-9.816152,2.959316,7.444408],[3.451362,5.890853,0.125424,-5.694293,-5.770294,-4.523267,-1.893847,-4.831521,5.512900,-1.441545,6.543769,1.563681,-1.904918,9.831495,2.315901],[2.031281,-5.831231,-5.249985,4.168226,2.690120,5.132179,-3.925458,-5.262022,-6.663014,-2.603994,9.636270,1.385391,-7.549688,-1.663611,-0.451717],[-6.827583,-1.550348,-3.948951,-3.938512,1.344652,6.888370,4.373618,3.394188,-6.158525,3.240888,-5.330908,-4.515949,4.607118,0.996147,7.538279]],[[1.744478,0.535417,-6.198472,-5.248550,1.839435,4.696459,-1.513708,-6.807302,-9.423011,-7.008172,3.387368,-6.187860,-1.764594,-2.034662,9.843281],[8.503734,5.449145,-6.591617,-5.965415,-1.116192,-5.507220,1.047685,-5.096429,-7.291064,-8.586624,-2.792268,0.021701,-6.434024,-4.860022,3.365717],[-4.206299,-3.684423,5.727370,0.413185,-3.603563,9.331012,5.355245,5.345065,7.580831,-1.915358,-5.097402,6.543644,9.913743,-6.751693,4.981998],[9.888241,-1.183128,2.059757,-2.126719,-8.643607,1.698932,-9.460355,-0.006860,-8.069067,4.778469,1.214367,-2.357524,-1.565479,-3.544088,8.073949],[-1.131037,7.172440,9.390517,4.913765,-0.690956,-0.847755,5.281911,-2.116003,-6.608291,9.082799,-6.465709,-2.580061,-5.966803,-0.107260,2.476955],[-7.450765,7.189681,-0.769543,-9.347439,-0.461061,0.916202,-9.992667,9.315764,-8.756696,-8.656489,-4.817187,8.353238,2.793249,5.994273,-5.632613],[3.833933,-3.531224,6.452256,8.041649,-5.813913,-4.941069,-0.572654,7.270621,2.374595,-3.153619,5.890220,-7.157502,5.495035,-2.617864,-2.061027],[1.803950,8.361269,-3.964892,-5.417331,5.837714,1.221218,6.078272,-4.601837,-3.782115,-3.943304,2.630221,2.105290,-1.871376,1.606285,2.164103],[-6.620229,-4.229970,-3.217198,-8.389636,-0.560716,-9.443735,3.243849,-2.911587,-4.578484,3.026929,0.995020,-5.206875,9.930889,7.682996,-7.487535],[-8.412619,1.654692,-6.082825,8.176400,-4.272898,-5.001942,9.265233,-9.818884,-2.737397,-4.588778,-8.204675,-2.425075,-6.034016,8.276745,1.047396],[-3.848946,-4.989258,-8.153719,-0.742633,7.073274,1.157893,0.975035,6.880943,-2.698831,-7.364106,-6.034509,-3.949222,9.061062,-4.500870,-5.108316]],[[-5.659921,9.764860,-7.945988,-2.376609,4.302908,-8.931723,8.121654,6.534451,4.444955,-5.609179,8.478230,-1.573891,-9.213894,-1.368552,6.110560],[-0.847115,-3.780823,-7.419983,3.139586,4.704349,0.970600,5.622521,3.306249,9.647516,2.562237,-4.249574,-9.322603,-9.659907,-7.115816,3.368413],[-0.190235,-7.886316,0.880851,0.142337,5.465086,3.176291,-1.156084,8.746523,-9.871403,1.401473,9.313976,-2.509655,-5.485149,-3.055252,8.864805],[-4.410955,1.097129,-6.896620,-3.321227,4.276719,-9.381403,-2.535067,7.675184,-2.798796,-3.153716,8.647843,0.469085,-5.049100,1.522239,7.963760],[-6.952744,-5.103889,-0.716494,7.234579,-2.625612,-8.790795,8.864695,-8.240414,-8.985166,-3.095151,-0.104039,-5.729208,0.705627,4.151664,5.644185],[-8.101831,2.857524,5.630551,1.257037,-6.455494,3.552921,4.479489,3.798824,-8.691089,-4.209158,-8.381829,-8.760156,0.892093,2.436798,-7.264000],[7.523457,7.135681,7.415948,-0.733336,2.858771,8.114943,8.424228,3.708561,-1.349982,-2.445305,7.386607,0.569000,-9.039156,1.501438,9.141850],[-4.678464,-2.779426,0.985766,2.427828,2.106866,-2.666385,6.403143,9.732948,-7.436347,-6.523667,-0.159767,-3.286892,-0.536454,-8.929066,-4.837138],[3.420231,-3.064675,-7.243266,-1.267868,5.002717,-5.093611,-2.025309,8.787653,0.805380,0.296742,0.283140,5.905606,4.599316,-7.749563,7.589517],[9.249967,8.858276,2.486861,-4.396756,2.100137,8.311755,6.457805,-6.936461,4.389102,2.561190,3.358022,-6.968262,-6.298249,-4.107358,-8.208075],[7.194588,4.414504,5.211047,2.446120,-5.685109,-4.815173,-6.026304,6.721066,-4.408716,-4.266882,7.974502,-7.481005,-8.252686,0.493436,5.954705]],[[1.940991,2.550881,-4.732526,6.135375,-3.985844,-9.856245,6.648347,9.375561,1.449393,5.482839,3.563214,-1.134157,-7.556677,-8.204748,4.749163],[3.864445,-3.375750,9.980790,-0.633321,-4.860624,-6.089168,6.872954,-9.803308,-8.621648,-3.820467,4.122998,-1.437728,-5.423894,0.230170,-1.656084],[-8.394116,4.088274,8.367643,3.539319,3.073348,-0.697214,3.646268,2.173301,-1.383132,0.404788,4.259375,-5.891397,-1.450772,-4.229930,7.389252],[7.748426,1.273837,6.774457,3.404109,-1.362032,-3.584499,1.739003,-1.005100,9.029691,-9.794435,1.678717,-3.853142,-8.358517,-8.298334,-3.298109],[3.257998,-7.044379,-9.079477,8.855520,-6.799253,-9.553830,2.477021,-2.453183,-6.429523,-8.001536,6.043191,-2.546777,-3.535569,-0.387770,7.709185],[-3.730297,-1.563755,5.874688,-3.601584,8.098568,-3.439149,-0.875259,8.456870,4.184671,-5.671818,-8.612688,-1.170638,7.830113,0.817051,1.069458],[-6.273342,-5.082292,-2.910547,3.632549,-3.852063,-8.060075,-6.876311,-2.316290,5.239347,5.264392,-7.625132,5.390525,-7.434751,5.644037,6.931541],[5.984486,-5.836538,-5.297724,8.754463,-7.814381,-4.331118,2.444081,5.845601,-8.384303,4.281179,-6.482123,-7.305653,-0.085692,8.629039,-7.207292],[1.107486,-3.583747,4.853894,-0.504584,9.061318,7.759394,6.213423,-8.007322,-9.593038,-5.907953,3.367826,9.898036,-6.732099,-4.435324,0.581392],[-3.564636,-5.754261,9.688969,-1.204828,7.554540,-0.083672,7.185111,9.268043,-1.305321,9.069642,5.331812,9.912507,-5.264009,1.828443,7.838606],[0.536613,3.860370,0.555206,-5.233973,-4.803011,9.129756,-9.299654,7.924960,-2.772583,7.850875,-2.339603,-8.537915,-5.013678,1.812492,-3.223909]],[[-9.539956,3.945436,7.481543,-9.034907,-4.779921,2.259363,0.235087,-8.078766,1.224027,-2.220595,-7.152312,-5.063660,7.812943,5.266627,-1.323657],[5.034225,-2.546408,-9.168794,5.242214,8.005686,5.005380,3.468355,-5.067956,5.007787,5.182040,-6.601398,-3.922638,-3.055667,8.659211,7.908483],[9.016808,5.418581,3.408473,-4.980007,-8.524671,-5.256418,-2.247929,9.472384,7.750772,3.670062,-2.292558,7.675508,-0.533098,-6.955092,9.040992],[9.807347,1.765216,-4.432082,-0.182130,5.602321,-4.956590,-7.048219,-0.069985,1.839655,5.360972,-2.697134,5.961539,-3.379915,5.473673,5.615243],[-6.851148,-4.465428,2.371671,-7.633075,1.436567,8.653919,3.207733,-4.818014,4.945749,-9.114901,-1.475567,-9.116129,-8.548365,7.017781,-0.889475],[-4.229047,1.886606,-4.415809,-8.662148,-5.399376,-8.123803,1.810367,-1.354976,2.949917,-3.209672,-0.882434,-6.164739,-2.130071,3.892053,8.438143],[-6.936818,4.365618,-3.830470,3.170186,-0.091891,-8.553757,0.871602,9.084435,3.449556,1.248514,-4.792885,9.870306,-9.327712,4.757115,0.573493],[9.944157,-1.242656,-4.505368,-9.793058,6.003050,6.165284,-0.533688,-7.020525,-3.021547,-4.553414,6.839729,0.733914,-9.093117,-3.545758,-7.164360],[-0.992625,4.248637,-5.602203,2.408254,5.714605,6.945758,-0.759311,8.036645,6.753880,-2.854618,3.289190,-0.747471,-2.232963,2.296743,-6.640188],[5.141264,7.912651,-8.985613,-3.728774,5.207439,-7.549692,-5.266358,-2.028028,6.811085,-8.576283,6.490957,2.967396,-9.881925,-6.224531,-0.373428],[0.325172,3.186049,0.482503,-5.022123,8.083212,7.011353,4.109603,-9.860915,-0.863557,5.754958,-7.609508,-4.326210,3.114333,6.088701,-2.455075]],[[-7.933727,1.061496,1.039064,4.050836,-1.302221,1.554293,6.225582,-5.926890,-6.511756,3.486567,0.047996,-9.304332,-2.491560,-4.949860,-8.310422],[4.917399,5.295468,-6.981513,4.972033,-2.178197,9.133095,-4.870751,-5.601989,-3.237606,4.386215,2.706178,6.592091,-5.081142,6.694475,-9.145139],[-3.083370,-0.833069,-1.623017,-3.452535,0.400959,-9.047821,-0.927608,6.195739,6.374599,2.442863,5.409128,2.381448,-6.725628,-7.071001,-4.407900],[1.540326,0.700103,-8.341627,8.959973,1.988254,-4.712704,6.486667,-8.486245,2.525959,-6.581338,-6.532083,9.516034,3.571706,-8.220316,3.385324],[-2.180327,5.082116,1.845844,2.389101,-4.646619,4.712576,-4.280628,8.435000,4.168073,-1.687725,4.656843,9.990280,-8.159713,-8.482470,4.820564],[-9.871727,6.526921,4.081779,5.563366,5.412228,7.687164,-7.870349,3.255459,3.446923,0.675898,-8.381068,-5.335279,4.917481,-6.984055,6.007596],[-4.842867,5.630138,1.772478,-0.279996,-4.559403,-2.443938,-9.494125,4.027014,-4.920077,-6.317981,3.672798,-0.346751,-3.191575,-5.560544,-3.648209],[-1.483076,2.931523,-0.527449,-5.386575,-0.986537,-5.602638,0.677597,3.617864,-3.797569,1.351724,5.697540,8.973364,-3.704385,-2.843597,0.252360],[7.214537,6.158101,6.567549,2.803575,-9.950717,-0.941904,5.626228,6.805510,7.117109,-1.790590,-5.857007,5.160939,-1.619667,7.843860,-7.775871],[2.472527,3.542147,4.391185,-4.044511,-3.288843,-4.917008,2.058999,-6.238637,-3.279703,-8.919811,-0.303809,7.234980,-0.268655,-6.032605,-5.050661],[-4.536092,-3.528715,-7.785212,4.480590,-3.018390,9.126998,-3.308671,-0.033783,2.991232,-2.315695,-8.402469,-6.190031,-0.237130,1.578555,-0.457070]]], dtype = "float64")#candidate|3639|(7, 11, 15)|const|float64
var_3640 = relay.var("var_3640", dtype = "float64", shape = (7, 11, 15))#candidate|3640|(7, 11, 15)|var|float64
bop_3641 = relay.power(const_3639.astype('float64'), relay.reshape(var_3640.astype('float64'), relay.shape_of(const_3639))) # shape=(7, 11, 15)
output = relay.Tuple([bop_3641,])
output2 = relay.Tuple([bop_3641,])
func_3645 = relay.Function([var_3640,], output)
mod['func_3645'] = func_3645
mod = relay.transform.InferType()(mod)
mutated_mod['func_3645'] = func_3645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3646 = relay.var("var_3646", dtype = "float64", shape = (7, 11, 15))#candidate|3646|(7, 11, 15)|var|float64
func_3645_call = mutated_mod.get_global_var('func_3645')
call_3647 = func_3645_call(var_3646)
output = call_3647
func_3648 = relay.Function([var_3646], output)
mutated_mod['func_3648'] = func_3648
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3674 = relay.var("var_3674", dtype = "float32", shape = (10, 16, 14))#candidate|3674|(10, 16, 14)|var|float32
var_3675 = relay.var("var_3675", dtype = "float32", shape = (10, 16, 14))#candidate|3675|(10, 16, 14)|var|float32
bop_3676 = relay.power(var_3674.astype('float32'), relay.reshape(var_3675.astype('float32'), relay.shape_of(var_3674))) # shape=(10, 16, 14)
func_1294_call = mod.get_global_var('func_1294')
func_1295_call = mutated_mod.get_global_var('func_1295')
call_3683 = relay.TupleGetItem(func_1294_call(), 0)
call_3684 = relay.TupleGetItem(func_1295_call(), 0)
func_2581_call = mod.get_global_var('func_2581')
func_2583_call = mutated_mod.get_global_var('func_2583')
var_3686 = relay.var("var_3686", dtype = "int64", shape = (192,))#candidate|3686|(192,)|var|int64
call_3685 = relay.TupleGetItem(func_2581_call(relay.reshape(var_3686.astype('int64'), [192,])), 1)
call_3687 = relay.TupleGetItem(func_2583_call(relay.reshape(var_3686.astype('int64'), [192,])), 1)
output = relay.Tuple([bop_3676,call_3683,call_3685,var_3686,])
output2 = relay.Tuple([bop_3676,call_3684,call_3687,var_3686,])
func_3693 = relay.Function([var_3674,var_3675,var_3686,], output)
mod['func_3693'] = func_3693
mod = relay.transform.InferType()(mod)
mutated_mod['func_3693'] = func_3693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3693_call = mutated_mod.get_global_var('func_3693')
var_3695 = relay.var("var_3695", dtype = "float32", shape = (10, 16, 14))#candidate|3695|(10, 16, 14)|var|float32
var_3696 = relay.var("var_3696", dtype = "float32", shape = (10, 16, 14))#candidate|3696|(10, 16, 14)|var|float32
var_3697 = relay.var("var_3697", dtype = "int64", shape = (192,))#candidate|3697|(192,)|var|int64
call_3694 = func_3693_call(var_3695,var_3696,var_3697,)
output = call_3694
func_3698 = relay.Function([var_3695,var_3696,var_3697,], output)
mutated_mod['func_3698'] = func_3698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2826_call = mod.get_global_var('func_2826')
func_2828_call = mutated_mod.get_global_var('func_2828')
call_3737 = relay.TupleGetItem(func_2826_call(), 0)
call_3738 = relay.TupleGetItem(func_2828_call(), 0)
func_1829_call = mod.get_global_var('func_1829')
func_1831_call = mutated_mod.get_global_var('func_1831')
call_3744 = func_1829_call()
call_3745 = func_1829_call()
output = relay.Tuple([call_3737,call_3744,])
output2 = relay.Tuple([call_3738,call_3745,])
func_3758 = relay.Function([], output)
mod['func_3758'] = func_3758
mod = relay.transform.InferType()(mod)
output = func_3758()
func_3759 = relay.Function([], output)
mutated_mod['func_3759'] = func_3759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3758_call = mod.get_global_var('func_3758')
func_3759_call = mutated_mod.get_global_var('func_3759')
call_3762 = relay.TupleGetItem(func_3758_call(), 1)
call_3763 = relay.TupleGetItem(func_3759_call(), 1)
output = call_3762
output2 = call_3763
func_3768 = relay.Function([], output)
mod['func_3768'] = func_3768
mod = relay.transform.InferType()(mod)
output = func_3768()
func_3769 = relay.Function([], output)
mutated_mod['func_3769'] = func_3769
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3774 = relay.const([[[-4.444769,5.584867,-1.186551,4.610232],[-1.829058,2.241329,5.718947,6.498490],[1.062587,-7.294892,-8.356736,-3.862139],[-9.891029,-1.242200,2.799849,-0.946470],[7.405383,2.267791,6.537062,8.632957],[-9.648924,0.710025,-3.914877,5.897848],[7.518340,-4.425739,-8.181354,0.918469],[1.883660,8.636502,-8.433245,-4.958429],[2.160243,6.443488,5.331916,-3.941083],[2.543181,6.187048,-3.901328,0.671144],[-3.037173,3.186919,-1.332205,1.350904],[-0.273654,0.575773,-8.454185,8.745470]],[[8.256429,0.335888,1.821325,7.451326],[7.785575,-8.319182,0.800035,9.624667],[3.260901,-4.873381,-3.257118,7.130432],[-9.509094,6.973705,4.590658,-1.268833],[3.661445,9.726446,-8.268945,-7.282188],[5.526375,2.572315,-9.726073,3.894672],[-8.016192,-4.378396,9.028424,4.079961],[-8.350084,2.393556,1.078255,-7.829633],[4.824268,2.925230,-5.656423,0.294930],[-9.338156,-0.132724,-7.686899,-7.609966],[6.253103,8.274879,3.687962,-4.473136],[0.698700,3.387657,-5.731387,7.112251]],[[6.976249,8.487208,-0.855061,6.917878],[1.339432,-6.474309,2.544685,-5.616116],[3.237521,-3.995718,7.859742,-5.308073],[-7.638557,7.636951,5.218562,-4.622375],[-1.576535,4.540391,-7.792774,3.794524],[-8.585765,8.822186,5.569954,6.650592],[8.049663,6.962660,-2.742906,3.017810],[6.786260,7.876321,-5.907821,3.825801],[7.152941,3.592012,1.230298,-3.784289],[-4.867392,-3.737600,2.793169,-3.648981],[8.576053,3.929418,6.694328,-5.541108],[-2.966892,-1.642273,1.000882,6.648936]],[[-7.797898,-4.556037,0.332753,9.323262],[0.937473,7.529645,9.842930,6.102638],[2.098196,2.656274,-6.366976,1.104721],[2.424846,1.912256,7.321160,-9.255303],[7.113615,-2.252223,4.169423,1.818624],[9.366376,3.020810,-2.266486,4.108315],[-1.889302,4.588928,-5.397335,8.145006],[-7.954647,-0.572844,6.802655,4.969720],[4.758348,5.632657,0.667023,9.804554],[-7.607796,-8.704924,-0.705956,-7.449122],[-1.149177,9.330522,8.019610,-4.943201],[4.391594,8.654209,0.648617,1.432346]],[[-4.428066,8.238263,0.275076,-8.789666],[-7.316782,6.001356,-6.721613,4.103508],[0.417900,7.219644,3.622543,-3.480061],[-6.516652,9.818664,-5.133635,1.497740],[7.264729,-7.141802,5.264156,-7.367582],[3.095870,-6.393101,-6.226718,-4.865834],[-9.282150,-2.859455,-0.739098,-6.250961],[-3.202280,-1.850122,0.976379,-5.808721],[5.572813,1.100193,2.177709,-4.378268],[1.964309,0.404824,-0.522739,0.733569],[9.793866,-1.340448,-1.265868,3.671840],[-7.233101,8.577514,5.413963,-3.504816]],[[7.097370,7.508009,-4.114010,4.732699],[3.832915,8.143320,5.026509,-8.219261],[-9.714094,-8.677834,-5.121238,6.897407],[0.762208,-6.970109,-2.719458,3.084777],[-8.497236,5.269183,-7.042237,8.169762],[2.970046,8.413611,0.422477,1.359916],[-2.070341,3.319109,7.476191,7.036361],[7.423886,5.469467,9.021933,9.171415],[-8.885141,-7.744744,-3.479958,-7.418297],[-1.434632,-2.419890,3.163725,7.007817],[0.135371,-4.519502,4.687552,5.072327],[8.096893,3.214604,-8.425661,0.678006]],[[4.722942,8.029181,4.219476,2.457443],[-9.233109,6.842979,6.487179,2.825300],[3.928508,-2.162575,-7.937533,-8.910930],[-4.126053,-3.082504,-5.364156,7.892281],[4.732928,9.745780,-5.396137,-8.627125],[-9.768689,0.741567,-5.802590,-4.489008],[-5.830265,-2.801152,2.895651,4.825453],[-3.362519,-7.710908,5.445570,-2.132332],[-9.939361,6.546616,-7.182124,4.813841],[7.164768,1.537777,-1.376920,-7.044636],[-1.537547,9.494181,8.123049,8.394859],[-9.253005,-2.139975,-6.170836,-4.664397]],[[1.010633,1.805788,7.526353,-7.867846],[0.607414,-7.284857,-0.040175,5.925178],[7.574017,-8.237115,2.038875,8.160775],[9.440712,2.345306,-5.165853,-0.016660],[1.822988,-8.639278,0.539558,6.693988],[-1.375404,-8.196759,-6.169065,7.270056],[-3.277842,-1.467250,4.167122,1.789145],[-6.971216,-6.084625,-9.773745,-2.574620],[4.774683,-9.362463,7.977325,4.874303],[3.909344,-8.486773,1.268397,2.946707],[8.402983,4.623682,9.462700,6.648136],[0.478848,1.729164,6.691574,6.784264]],[[-5.279431,9.419677,-0.782058,6.094068],[-5.074952,6.176849,5.756428,7.530384],[8.636836,8.351400,6.935443,-4.019629],[0.618846,-2.964302,0.618646,6.609665],[0.653336,3.710763,6.758628,1.338668],[8.851488,-9.852119,5.525080,5.957824],[-0.371080,-5.102977,-6.331589,3.934310],[-6.565423,-1.741065,7.424165,2.148078],[-9.958616,-1.417034,6.206725,4.748414],[9.610330,0.015952,4.819139,4.117310],[5.342857,5.394525,-4.800670,9.922488],[-3.604016,-5.231269,7.337577,-6.916086]],[[-0.032234,-9.402031,-7.919807,-7.430041],[7.857444,-9.697355,8.561337,-8.804345],[9.193488,-2.955211,-7.794072,-2.049831],[4.233065,8.443141,-4.490658,-4.060581],[-7.918791,-4.689050,-4.256969,-4.099500],[-0.665738,-4.361445,-6.335670,6.915260],[-8.583965,8.995673,5.561554,7.503734],[-0.227182,-3.962464,-7.366934,-4.868592],[6.469309,2.887837,4.486063,4.473551],[-2.366417,8.455282,-9.497127,6.330787],[-6.185438,-7.604875,-4.304284,-2.355630],[-0.132276,-1.769371,3.989335,0.272623]],[[7.501097,-0.514476,6.507815,6.868011],[4.874114,-2.488348,8.834248,-4.104862],[1.996758,6.322891,-0.141079,-7.584664],[-2.777299,2.830502,9.632975,-4.021006],[8.726864,-6.016314,-6.913814,6.215982],[-1.270355,-0.284634,6.192344,-9.735427],[4.949149,-3.078541,2.064717,-0.404824],[4.271213,-3.776236,-1.761896,-9.133422],[0.418975,-3.693758,-9.705362,-7.049201],[-5.389463,-9.340020,2.052709,-0.761396],[-0.047397,5.939915,3.875977,-3.035731],[2.854425,-9.123108,6.297331,-1.944613]],[[4.975482,1.474480,-6.100821,-4.529292],[-0.066264,-4.713773,6.901494,-5.566526],[1.611511,-0.828244,0.968198,-3.706216],[7.599293,-2.952254,6.506051,5.694154],[-8.791353,-0.443612,-7.277478,8.128883],[3.587798,7.940867,-7.367360,-0.128095],[3.500806,-3.853590,5.223170,1.272540],[5.870252,-3.505304,-8.033494,6.185270],[-3.672799,2.795899,3.016220,0.324277],[-3.970804,4.229139,-7.761852,7.856019],[-7.848272,-7.179114,-3.856335,-6.778954],[4.708702,-8.558400,4.133022,-4.284681]],[[3.000478,-4.248676,-1.463352,1.449966],[-9.325309,2.038339,-2.411127,-9.079290],[8.324901,5.634586,5.628280,3.297132],[-3.159900,-6.759321,-8.206166,5.885346],[5.868203,-8.464389,7.961704,-5.629212],[-7.354430,-4.097618,-0.987283,-0.106007],[9.339902,7.611233,4.858595,8.276974],[-1.829706,6.879013,4.983279,-3.386859],[7.659882,-8.473337,-5.579732,-5.213934],[8.723782,-3.922314,-4.749121,6.342404],[-1.405838,-5.852053,2.013639,6.727940],[9.279684,-5.697991,5.145503,8.293646]],[[1.637301,8.881077,6.393371,2.359254],[-1.585579,-4.764671,-8.313148,-1.928377],[0.521175,-0.203732,-9.421536,-4.609605],[6.687318,-6.053971,-4.537497,1.050159],[-1.320770,7.253954,-2.007586,-8.119345],[-0.751744,3.348099,-9.680615,8.844132],[-2.693107,-5.411552,3.543377,1.809490],[-7.967237,8.963917,0.069060,-1.439685],[6.261743,7.288632,-9.658442,-8.230439],[2.423486,4.127704,5.206069,5.493433],[1.413557,4.547975,-5.173636,9.039361],[-9.749830,7.725998,0.571607,1.811835]],[[-7.755051,-7.616970,-7.814066,8.482079],[2.552748,4.548862,-0.667912,-2.311585],[2.802450,-1.271337,-0.878429,-3.838318],[4.496934,2.936126,3.516946,1.836465],[3.738013,7.206410,6.950196,1.302944],[9.200787,6.402414,6.508159,5.784175],[0.647882,0.293160,0.655485,3.474510],[0.491606,5.666343,0.819475,-6.386419],[7.988829,1.478050,8.967090,5.383964],[8.839712,-7.329865,-2.494632,0.332125],[2.625079,-0.528465,-6.411304,3.453512],[-7.218561,1.487087,-2.609537,-6.947745]]], dtype = "float64")#candidate|3774|(15, 12, 4)|const|float64
uop_3775 = relay.acosh(const_3774.astype('float64')) # shape=(15, 12, 4)
func_1509_call = mod.get_global_var('func_1509')
func_1510_call = mutated_mod.get_global_var('func_1510')
call_3779 = relay.TupleGetItem(func_1509_call(), 0)
call_3780 = relay.TupleGetItem(func_1510_call(), 0)
output = relay.Tuple([uop_3775,call_3779,])
output2 = relay.Tuple([uop_3775,call_3780,])
func_3787 = relay.Function([], output)
mod['func_3787'] = func_3787
mod = relay.transform.InferType()(mod)
mutated_mod['func_3787'] = func_3787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3787_call = mutated_mod.get_global_var('func_3787')
call_3788 = func_3787_call()
output = call_3788
func_3789 = relay.Function([], output)
mutated_mod['func_3789'] = func_3789
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3817 = relay.var("var_3817", dtype = "float64", shape = (3, 1, 5))#candidate|3817|(3, 1, 5)|var|float64
var_3818 = relay.var("var_3818", dtype = "float64", shape = (3, 6, 5))#candidate|3818|(3, 6, 5)|var|float64
bop_3819 = relay.floor_divide(var_3817.astype('float64'), var_3818.astype('float64')) # shape=(3, 6, 5)
output = bop_3819
output2 = bop_3819
func_3824 = relay.Function([var_3817,var_3818,], output)
mod['func_3824'] = func_3824
mod = relay.transform.InferType()(mod)
mutated_mod['func_3824'] = func_3824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3824_call = mutated_mod.get_global_var('func_3824')
var_3826 = relay.var("var_3826", dtype = "float64", shape = (3, 1, 5))#candidate|3826|(3, 1, 5)|var|float64
var_3827 = relay.var("var_3827", dtype = "float64", shape = (3, 6, 5))#candidate|3827|(3, 6, 5)|var|float64
call_3825 = func_3824_call(var_3826,var_3827,)
output = call_3825
func_3828 = relay.Function([var_3826,var_3827,], output)
mutated_mod['func_3828'] = func_3828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3275_call = mod.get_global_var('func_3275')
func_3276_call = mutated_mod.get_global_var('func_3276')
call_3971 = func_3275_call()
call_3972 = func_3275_call()
output = call_3971
output2 = call_3972
func_3973 = relay.Function([], output)
mod['func_3973'] = func_3973
mod = relay.transform.InferType()(mod)
mutated_mod['func_3973'] = func_3973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3973_call = mutated_mod.get_global_var('func_3973')
call_3974 = func_3973_call()
output = call_3974
func_3975 = relay.Function([], output)
mutated_mod['func_3975'] = func_3975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3768_call = mod.get_global_var('func_3768')
func_3769_call = mutated_mod.get_global_var('func_3769')
call_3989 = func_3768_call()
call_3990 = func_3768_call()
func_3610_call = mod.get_global_var('func_3610')
func_3612_call = mutated_mod.get_global_var('func_3612')
const_4002 = relay.const([[-3,-9,9,-4,-8,-3,-8,3,2,7,4,-7,3,-5,-1,7,6,-4,1,3,10,2,-6,-9,-2,-6,2,-3,-7,10,-5,-2,4,-6,-4,4,3,-4,-3,-1,9,-1,-1,8,3,5,-6,9,-3,-6,-3,2,8,-9,1,4,-7,3,-9,3,-2,10,-7,9,-5,8,-5,6,-8,-2,4,1,3,9,-8,4,3,7,2,-10,10,4,8,-7,-4,-9,9,2,-7,-5,-3,4,-10,4,6,-10,-1,2,-6,-8,-9,1,-9,1,-1,-1,-5,8,6,9,7,-10,6,8,10,4,-4,-1,-7,-9,9,5,-4,1,-7,6,2,10,8,1,3,1,-10,10,-5,8,-10,-1,-5,6,5,-6,8,6,-4,-5,-10,-6,-9,8,7,9,8,-2,2,-5,-8,3,-8,1,4,3,-2,-6,5,-4,-1,-10,5,-2,-7,-4,-9,-10,-8,1,7,-7,2,10,7,-2,9,7,-3,10,5,7,-5,-3,10,-4,-9,-7,-4,10,3,10,-3,5,-6,-8,-3,7,5,-8,3,3,-4,-2,-7,10,4,1,8,5,-3,5,1,-3,-1,1,-6,7,-5,6,1,2,-7,5,1,9,5,1,3,2,8,9,8,-1,3,6,7,-1,3,10,-4,-7,1,6,-3,-10,-2,4,-3,4,6,3,-10,-6,8,4,-4,-2,-10,-3,-7,-5,-1,10,7,3,-3,-5,-9,-5,-8,1,-3,-9,3,7,6,-8,4,3,1,-3,2,-9,-8,10,-5,-7,5,-1,-9,-8,-4,-2,-4,8,-2,-10,-10,7,-5,-3,9,-9,8,-5,-2,-4,1,5,-10,1,-5,-8,1,-2,-4,9,6,2,-9,3,-9,-10,-2,6,-9,7,9,8,3,-8,-6,2,4,8,-2,9,-7,-4,3,4,-8,-5,-4,-8,-4,6,5,3,-4,7,3,7,-4,-10,10,8,-5,-6,-5,-6,5,10,-9,-9,4,-9,1,-9,-7,-3,-3,7,-1,6,7,6]], dtype = "uint8")#candidate|4002|(1, 384)|const|uint8
call_4001 = func_3610_call(relay.reshape(const_4002.astype('uint8'), [4, 12, 8]))
call_4003 = func_3610_call(relay.reshape(const_4002.astype('uint8'), [4, 12, 8]))
output = relay.Tuple([call_3989,call_4001,const_4002,])
output2 = relay.Tuple([call_3990,call_4003,const_4002,])
func_4005 = relay.Function([], output)
mod['func_4005'] = func_4005
mod = relay.transform.InferType()(mod)
mutated_mod['func_4005'] = func_4005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4005_call = mutated_mod.get_global_var('func_4005')
call_4006 = func_4005_call()
output = call_4006
func_4007 = relay.Function([], output)
mutated_mod['func_4007'] = func_4007
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4038 = relay.const([[[6,-3,-3,-10,-5,-2,5],[-1,-7,-8,-9,-6,10,9],[-4,9,4,-9,-1,5,10],[-7,9,7,-2,-3,-2,4],[-4,5,7,7,5,10,7],[-4,-3,9,6,7,1,-9],[-6,8,-5,-9,-4,-6,2],[-5,-3,3,9,-7,-10,-2],[-4,-5,-3,-2,5,-1,-8],[7,6,7,2,-7,-4,3],[1,-4,-6,5,1,8,-1],[-4,-9,-6,-5,-4,7,-8],[-6,-4,8,-9,-6,-4,4],[-2,2,-1,-8,-3,4,-10],[9,-1,-8,-1,2,1,-6],[6,8,4,-7,-10,-4,8]],[[4,-8,-7,-7,3,-3,8],[6,10,4,3,9,-3,-4],[4,6,1,1,4,-5,8],[5,-2,9,-2,-2,-3,4],[10,4,10,-3,7,-1,6],[1,3,-9,6,9,-5,4],[1,-3,-3,-6,8,-6,-7],[-7,2,-4,-3,-2,-5,8],[3,5,7,5,-4,3,-2],[8,-5,-2,-2,-3,-1,5],[-9,5,2,-6,-7,-10,-3],[2,3,7,-2,6,5,-10],[-6,2,7,-7,-7,-9,3],[-3,2,2,-5,5,5,-3],[1,-9,-8,4,8,4,2],[10,-3,-2,10,10,10,-5]],[[7,7,1,4,-7,-5,-10],[2,2,-9,-7,-10,2,2],[-7,1,3,9,4,-5,4],[5,1,-7,-9,10,5,3],[-1,-3,10,-10,10,10,7],[-4,-7,6,-6,5,-9,-3],[4,-4,-1,-1,1,-7,-5],[6,2,2,8,-9,10,4],[-8,6,3,7,8,-6,-1],[9,-9,7,-4,-3,6,-9],[-8,8,9,8,-3,-5,-2],[8,-3,-1,-4,4,-7,2],[-8,2,5,-2,1,6,4],[2,4,1,-1,-10,1,2],[-10,1,-7,-6,10,-5,-7],[-4,-4,-6,10,-8,10,-3]],[[3,-6,2,-2,10,-1,5],[1,9,-2,-6,5,-6,5],[10,-6,7,-5,9,8,-7],[-10,-7,6,-10,10,9,-10],[-6,-10,6,1,-7,-4,6],[-6,3,9,8,-5,-6,-2],[10,-9,-10,-5,6,-2,4],[9,-10,-5,10,-2,-9,-7],[-1,9,3,-8,-10,1,-8],[-9,1,-2,-3,-5,-1,3],[3,7,9,7,-8,6,7],[2,-2,-10,8,-5,1,6],[-6,-3,9,7,10,1,-9],[5,-6,-3,-9,5,-5,10],[10,-9,5,9,6,3,8],[-5,2,-2,9,1,10,-7]],[[6,-2,-3,3,5,-5,8],[8,-1,2,10,-6,-3,9],[10,-8,-3,-3,3,8,9],[-10,9,-2,8,-8,2,-9],[10,8,-4,-8,-9,5,8],[2,5,6,-10,8,6,8],[7,-3,-7,-9,-9,10,-8],[2,8,-5,7,-9,-2,7],[-1,8,-6,7,3,-4,2],[10,9,-6,-7,-10,-6,3],[3,8,9,-4,-6,-6,-8],[1,6,-10,5,-4,8,-1],[2,-2,6,-1,-5,-9,7],[-10,-8,4,2,3,-9,4],[-10,2,10,8,-4,-10,3],[10,5,-6,-10,-10,-2,4]],[[9,-9,-2,2,-6,10,7],[-1,-9,4,-10,10,-1,-4],[3,-4,-5,-3,3,1,-6],[-1,10,5,10,5,10,-2],[6,-3,4,-3,-10,6,-4],[5,7,-2,6,6,7,-10],[7,-9,7,-3,-9,10,5],[-5,2,-8,5,-5,5,9],[-3,10,-10,-2,-1,8,3],[7,3,-6,1,-3,4,-9],[9,3,-6,1,-4,-5,-10],[-2,10,-3,-3,-7,5,-3],[9,-7,8,10,3,-4,-6],[1,-1,-1,4,3,2,-4],[-3,5,-6,10,-2,-2,4],[3,4,-6,-7,-3,10,2]],[[7,1,2,-1,8,-4,4],[5,-1,-7,-2,-9,1,-4],[9,3,2,5,-9,2,-10],[6,-4,1,1,2,3,4],[3,-5,4,8,3,9,2],[9,-10,3,8,-1,3,2],[-5,4,-6,10,-8,-5,-6],[4,6,7,8,9,-7,5],[-4,-8,5,6,-2,1,-9],[-2,9,-10,-7,10,-10,-3],[1,-6,5,1,5,-1,-8],[-6,9,1,-4,-4,9,-8],[4,5,-9,8,5,6,-1],[-9,-1,5,5,-7,-8,-1],[4,-7,3,6,10,-10,7],[7,4,6,-10,-5,-6,5]],[[-3,10,-8,-10,8,-4,9],[-3,1,4,-5,3,1,2],[2,3,4,5,-2,-4,8],[-7,4,-3,2,-2,-8,-2],[-5,-10,2,2,-7,-7,-1],[-9,2,6,-8,3,-8,8],[-2,-7,-7,-3,8,-4,-4],[6,-3,-4,1,-1,1,-10],[10,3,10,-8,4,-5,-1],[-9,-1,10,-10,-9,4,-9],[-5,-4,-6,-7,-6,3,-10],[-6,7,-4,2,2,-8,-2],[-4,-7,-9,6,-7,-4,-1],[7,-9,-10,8,-7,-10,2],[-2,2,5,-7,-10,2,9],[2,-6,9,2,4,-7,-2]]], dtype = "uint32")#candidate|4038|(8, 16, 7)|const|uint32
const_4039 = relay.const([[[4,2,8,-5,-7,-8,-1],[10,-9,7,9,10,-6,7],[2,5,1,-5,5,8,1],[4,4,-2,-2,-2,4,10],[3,-5,3,10,-7,6,6],[-5,-1,-9,-10,-10,1,-3],[4,-4,-3,1,-10,1,-7],[-9,-1,2,-3,9,-3,6],[-2,10,2,-2,-4,10,-5],[1,-8,-7,-7,10,-9,1],[-9,7,-8,9,10,5,-6],[7,-8,5,1,4,2,-5],[-5,2,-5,-7,-5,-3,10],[6,6,9,-2,-9,-6,-10],[-7,9,1,-5,-2,9,9],[-10,-3,4,2,3,-6,8]],[[3,2,10,1,-3,-10,-7],[2,-5,4,1,-5,-9,-8],[1,9,-3,-4,-2,-6,9],[2,7,3,-8,-7,-3,1],[-3,9,6,-7,-10,-2,6],[-9,-6,-3,7,-4,-3,4],[-7,7,4,1,-5,9,-9],[-10,-2,2,-4,-10,10,-5],[-9,8,4,4,-3,-9,5],[-6,10,-9,-6,10,-5,10],[8,-10,-4,1,-6,-5,-1],[-7,-4,-1,10,-9,-1,6],[-3,3,2,8,-2,4,-5],[-4,5,3,8,-6,-3,5],[-5,-2,-7,-10,6,3,-9],[5,7,-10,-3,-2,6,9]],[[2,-5,-7,5,-10,3,3],[6,-4,-5,10,-1,-8,-6],[-10,6,-1,9,8,9,9],[3,-7,-3,10,2,-3,5],[-6,8,5,10,-6,3,-4],[-9,-4,8,-5,-4,1,5],[9,-7,-10,-2,10,-1,4],[-8,8,-3,4,-8,2,-2],[-8,-9,8,5,-1,-4,-1],[-7,1,-3,-5,-3,-8,5],[-3,-7,7,-9,1,4,-10],[-3,7,6,-7,7,5,-10],[1,7,4,4,-7,8,-6],[10,-3,9,-4,8,-3,-3],[6,-3,1,-10,3,8,-6],[10,1,2,-4,3,-5,9]],[[-5,8,10,-8,-3,-7,2],[-8,4,-4,7,-8,-6,-9],[10,-1,-2,8,-4,4,7],[-6,7,-9,4,-7,-1,2],[-5,-2,-8,-2,4,4,-8],[-7,-10,-4,-9,-9,10,3],[-10,-1,-5,2,6,8,3],[9,-2,6,9,10,-5,-10],[6,6,-10,3,-10,3,-8],[-5,4,-4,-8,8,-10,-5],[9,10,1,-3,5,-8,-10],[8,-1,1,-6,-2,5,4],[-10,10,6,-5,8,-8,6],[7,-7,6,-9,-5,-1,-1],[-9,-2,6,10,-6,9,-5],[-6,-2,-8,7,9,2,10]],[[3,2,8,2,-9,-8,-7],[8,3,-2,-8,-4,-6,-10],[-8,-2,4,4,-9,10,9],[3,-2,-8,5,-9,-2,-10],[7,5,-2,8,-2,-10,9],[10,-5,-3,-2,-3,3,-1],[-5,1,1,-9,6,9,-10],[-10,-10,-6,-1,-5,10,-3],[-7,7,-5,4,-8,-9,10],[2,-10,8,1,6,-3,-9],[8,-7,6,7,-6,-7,5],[7,-7,-5,1,8,7,6],[-4,4,-4,-9,7,-2,-8],[-7,9,8,5,3,-7,6],[3,-6,6,1,1,2,5],[-2,5,7,7,7,1,6]],[[1,3,-5,-2,-9,2,-4],[-9,-10,-3,-4,8,8,-1],[-5,10,-2,-9,2,-9,8],[-2,-8,1,-5,3,-7,-9],[6,5,-1,-9,-7,-10,-2],[1,-2,2,5,-10,-10,-10],[-5,1,10,-5,10,-4,4],[6,-4,-6,2,-8,3,-7],[-2,9,7,9,5,-10,9],[2,9,9,-6,10,3,7],[6,9,3,5,8,-7,9],[-8,3,-10,-7,-4,4,-3],[9,-2,-5,3,7,-8,-2],[-7,-6,7,-6,-10,6,8],[-7,6,2,-3,9,7,-3],[-10,-1,4,-4,7,-10,3]],[[-10,-5,-3,-4,-10,-1,2],[4,2,8,1,-1,5,-4],[-4,10,-7,2,7,-2,3],[-6,1,8,-4,-7,8,-1],[-7,-5,-10,-6,9,5,-3],[3,-10,9,-8,5,3,8],[-1,4,2,10,6,8,-3],[3,10,2,-6,-3,7,-8],[-3,4,3,-3,-9,8,-10],[-3,9,-1,-4,1,3,6],[-6,-2,9,3,4,-1,-1],[-10,-3,-4,-9,-3,7,2],[-10,1,3,4,-9,-5,5],[6,3,6,9,10,6,-10],[7,-4,2,-4,-1,6,9],[3,-7,9,4,-10,7,10]],[[3,-6,-6,1,10,-3,-6],[-10,-10,9,1,1,-5,-10],[-1,8,4,8,6,8,-5],[-6,-9,5,9,-9,4,-8],[1,3,-2,-9,5,-8,7],[7,-8,10,-9,-9,9,-1],[-9,1,-8,-3,-5,9,-2],[-1,3,-8,2,8,-4,-2],[-4,7,-1,-3,-5,1,1],[-10,-5,1,-2,8,-10,7],[-3,1,9,1,8,-9,10],[-5,-8,-7,7,-2,8,2],[8,4,-6,9,2,-5,1],[5,4,6,6,-8,1,1],[1,9,-3,-1,7,4,7],[2,-5,-1,1,-4,1,10]]], dtype = "uint32")#candidate|4039|(8, 16, 7)|const|uint32
bop_4040 = relay.logical_xor(const_4038.astype('uint32'), relay.reshape(const_4039.astype('uint32'), relay.shape_of(const_4038))) # shape=(8, 16, 7)
func_3768_call = mod.get_global_var('func_3768')
func_3769_call = mutated_mod.get_global_var('func_3769')
call_4049 = func_3768_call()
call_4050 = func_3768_call()
func_2826_call = mod.get_global_var('func_2826')
func_2828_call = mutated_mod.get_global_var('func_2828')
call_4055 = relay.TupleGetItem(func_2826_call(), 0)
call_4056 = relay.TupleGetItem(func_2828_call(), 0)
func_3536_call = mod.get_global_var('func_3536')
func_3539_call = mutated_mod.get_global_var('func_3539')
var_4058 = relay.var("var_4058", dtype = "bool", shape = (384,))#candidate|4058|(384,)|var|bool
call_4057 = relay.TupleGetItem(func_3536_call(relay.reshape(call_4055.astype('float32'), [3, 15, 7]), relay.reshape(var_4058.astype('bool'), [384,]), ), 2)
call_4059 = relay.TupleGetItem(func_3539_call(relay.reshape(call_4055.astype('float32'), [3, 15, 7]), relay.reshape(var_4058.astype('bool'), [384,]), ), 2)
output = relay.Tuple([bop_4040,call_4049,call_4055,call_4057,var_4058,])
output2 = relay.Tuple([bop_4040,call_4050,call_4056,call_4059,var_4058,])
func_4060 = relay.Function([var_4058,], output)
mod['func_4060'] = func_4060
mod = relay.transform.InferType()(mod)
var_4061 = relay.var("var_4061", dtype = "bool", shape = (384,))#candidate|4061|(384,)|var|bool
output = func_4060(var_4061)
func_4062 = relay.Function([var_4061], output)
mutated_mod['func_4062'] = func_4062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_4089 = relay.TupleGetItem(func_1030_call(), 0)
call_4090 = relay.TupleGetItem(func_1031_call(), 0)
func_2437_call = mod.get_global_var('func_2437')
func_2443_call = mutated_mod.get_global_var('func_2443')
var_4103 = relay.var("var_4103", dtype = "int64", shape = (168,))#candidate|4103|(168,)|var|int64
const_4104 = relay.const([-9,-5,-2,9,1,9,6,-6,-5,4,-3,7,-8,-4,4,-2,4,1,4,9,7,-1,4,-7,10,3,4,9,-1,-7,-10,7,6,-1,9,8,-8,8,6,-10,-9,-2,-5,4,-3,2,-10,9,-8,-8,2,4,5,-1,9,9,-4,-10,-9,-6,5,-6,-6,1,-5,2,7,7,-8,-4,10,5,-2,3,-7,-4,9,-7,4,1,-9,9,9,-9,-6,3,4,-8,-1,8,3,2,3,-7,9,8,-10,-5,7,-5,-7,-7,-4,-7,-9,5,-8,-4,-6,10,10,5,-7,9,4,-6,-2,-2,-9,3,6,2,3,-7,-8,4,4,-7,10,8,-2,5,-7,-4,9,-6,5,1,3,-9,-6,8,4,5,-3,-10,-5,-1,-3,1,-2,7,5,5,7,-7,-7,-2,-10,5,-10,-8,-9,9,4,5,7,3,-1,7,2,-10,-9,-10,-1,-10,-1,4,-9,-1,3,1,8,-9,2,-7,-10,-5,-1,-7,1,1], dtype = "int64")#candidate|4104|(192,)|const|int64
call_4102 = relay.TupleGetItem(func_2437_call(relay.reshape(var_4103.astype('int64'), [14, 6, 2]), relay.reshape(var_4103.astype('int64'), [14, 6, 2]), relay.reshape(const_4104.astype('int64'), [192,]), relay.reshape(const_4104.astype('int64'), [4, 12, 4]), ), 3)
call_4105 = relay.TupleGetItem(func_2443_call(relay.reshape(var_4103.astype('int64'), [14, 6, 2]), relay.reshape(var_4103.astype('int64'), [14, 6, 2]), relay.reshape(const_4104.astype('int64'), [192,]), relay.reshape(const_4104.astype('int64'), [4, 12, 4]), ), 3)
output = relay.Tuple([call_4089,call_4102,var_4103,const_4104,])
output2 = relay.Tuple([call_4090,call_4105,var_4103,const_4104,])
func_4106 = relay.Function([var_4103,], output)
mod['func_4106'] = func_4106
mod = relay.transform.InferType()(mod)
mutated_mod['func_4106'] = func_4106
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4107 = relay.var("var_4107", dtype = "int64", shape = (168,))#candidate|4107|(168,)|var|int64
func_4106_call = mutated_mod.get_global_var('func_4106')
call_4108 = func_4106_call(var_4107)
output = call_4108
func_4109 = relay.Function([var_4107], output)
mutated_mod['func_4109'] = func_4109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_4120 = relay.TupleGetItem(func_526_call(), 0)
call_4121 = relay.TupleGetItem(func_527_call(), 0)
output = relay.Tuple([call_4120,])
output2 = relay.Tuple([call_4121,])
func_4122 = relay.Function([], output)
mod['func_4122'] = func_4122
mod = relay.transform.InferType()(mod)
output = func_4122()
func_4123 = relay.Function([], output)
mutated_mod['func_4123'] = func_4123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_4133 = relay.TupleGetItem(func_477_call(), 0)
call_4134 = relay.TupleGetItem(func_479_call(), 0)
func_2486_call = mod.get_global_var('func_2486')
func_2488_call = mutated_mod.get_global_var('func_2488')
call_4138 = func_2486_call()
call_4139 = func_2486_call()
output = relay.Tuple([call_4133,call_4138,])
output2 = relay.Tuple([call_4134,call_4139,])
func_4140 = relay.Function([], output)
mod['func_4140'] = func_4140
mod = relay.transform.InferType()(mod)
output = func_4140()
func_4141 = relay.Function([], output)
mutated_mod['func_4141'] = func_4141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4122_call = mod.get_global_var('func_4122')
func_4123_call = mutated_mod.get_global_var('func_4123')
call_4154 = relay.TupleGetItem(func_4122_call(), 0)
call_4155 = relay.TupleGetItem(func_4123_call(), 0)
output = relay.Tuple([call_4154,])
output2 = relay.Tuple([call_4155,])
func_4159 = relay.Function([], output)
mod['func_4159'] = func_4159
mod = relay.transform.InferType()(mod)
output = func_4159()
func_4160 = relay.Function([], output)
mutated_mod['func_4160'] = func_4160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mod.get_global_var('func_1958')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_4163 = relay.TupleGetItem(func_1958_call(), 0)
call_4164 = relay.TupleGetItem(func_1959_call(), 0)
func_2437_call = mod.get_global_var('func_2437')
func_2443_call = mutated_mod.get_global_var('func_2443')
var_4174 = relay.var("var_4174", dtype = "int64", shape = (168,))#candidate|4174|(168,)|var|int64
const_4175 = relay.const([[8,8,-10,5],[-3,-3,-10,5],[-2,-3,9,-2],[3,-2,5,1],[5,-3,6,-7],[2,6,-2,1],[7,4,-5,-10],[-4,1,-6,3],[4,8,-3,-8],[4,6,4,-2],[3,-7,-4,-1],[9,6,-4,7],[-4,-5,10,1],[-7,10,6,4],[-9,10,-10,-10],[2,-4,-6,4],[6,6,-5,9],[-5,5,4,3],[-2,7,-3,-9],[-4,3,6,9],[-9,9,5,7],[-9,-3,4,6],[-8,-6,-1,-8],[-9,-6,-8,-6],[-1,2,3,6],[-4,6,-7,-5],[-7,-8,7,-5],[6,-1,6,1],[10,-5,-3,-6],[-2,-6,-5,3],[-2,-2,8,-5],[-7,-7,2,2],[1,7,-8,10],[5,8,7,-4],[4,-7,-1,5],[7,-5,-1,-2],[-6,-8,-2,-6],[-6,-7,-6,3],[-4,2,-3,5],[10,8,9,-8],[9,-9,6,-5],[10,7,-2,-7],[1,4,-6,-1],[-1,2,8,-4],[5,5,-9,-4],[-4,-4,-1,7],[-10,-3,1,7],[-4,-3,10,-1]], dtype = "int64")#candidate|4175|(48, 4)|const|int64
call_4173 = relay.TupleGetItem(func_2437_call(relay.reshape(var_4174.astype('int64'), [14, 6, 2]), relay.reshape(var_4174.astype('int64'), [14, 6, 2]), relay.reshape(const_4175.astype('int64'), [192,]), relay.reshape(const_4175.astype('int64'), [4, 12, 4]), ), 0)
call_4176 = relay.TupleGetItem(func_2443_call(relay.reshape(var_4174.astype('int64'), [14, 6, 2]), relay.reshape(var_4174.astype('int64'), [14, 6, 2]), relay.reshape(const_4175.astype('int64'), [192,]), relay.reshape(const_4175.astype('int64'), [4, 12, 4]), ), 0)
func_3275_call = mod.get_global_var('func_3275')
func_3276_call = mutated_mod.get_global_var('func_3276')
call_4186 = func_3275_call()
call_4187 = func_3275_call()
func_4159_call = mod.get_global_var('func_4159')
func_4160_call = mutated_mod.get_global_var('func_4160')
call_4191 = relay.TupleGetItem(func_4159_call(), 0)
call_4192 = relay.TupleGetItem(func_4160_call(), 0)
output = relay.Tuple([call_4163,call_4173,var_4174,const_4175,call_4186,call_4191,])
output2 = relay.Tuple([call_4164,call_4176,var_4174,const_4175,call_4187,call_4192,])
func_4195 = relay.Function([var_4174,], output)
mod['func_4195'] = func_4195
mod = relay.transform.InferType()(mod)
var_4196 = relay.var("var_4196", dtype = "int64", shape = (168,))#candidate|4196|(168,)|var|int64
output = func_4195(var_4196)
func_4197 = relay.Function([var_4196], output)
mutated_mod['func_4197'] = func_4197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3275_call = mod.get_global_var('func_3275')
func_3276_call = mutated_mod.get_global_var('func_3276')
call_4201 = func_3275_call()
call_4202 = func_3275_call()
output = call_4201
output2 = call_4202
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
func_4159_call = mod.get_global_var('func_4159')
func_4160_call = mutated_mod.get_global_var('func_4160')
call_4265 = relay.TupleGetItem(func_4159_call(), 0)
call_4266 = relay.TupleGetItem(func_4160_call(), 0)
func_884_call = mod.get_global_var('func_884')
func_885_call = mutated_mod.get_global_var('func_885')
call_4278 = func_884_call()
call_4279 = func_884_call()
output = relay.Tuple([call_4265,call_4278,])
output2 = relay.Tuple([call_4266,call_4279,])
func_4280 = relay.Function([], output)
mod['func_4280'] = func_4280
mod = relay.transform.InferType()(mod)
mutated_mod['func_4280'] = func_4280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4280_call = mutated_mod.get_global_var('func_4280')
call_4281 = func_4280_call()
output = call_4281
func_4282 = relay.Function([], output)
mutated_mod['func_4282'] = func_4282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1433_call = mod.get_global_var('func_1433')
func_1435_call = mutated_mod.get_global_var('func_1435')
call_4289 = relay.TupleGetItem(func_1433_call(), 0)
call_4290 = relay.TupleGetItem(func_1435_call(), 0)
uop_4301 = relay.log(call_4289.astype('float64')) # shape=(3, 15, 7)
uop_4303 = relay.log(call_4290.astype('float64')) # shape=(3, 15, 7)
func_2032_call = mod.get_global_var('func_2032')
func_2034_call = mutated_mod.get_global_var('func_2034')
call_4306 = relay.TupleGetItem(func_2032_call(), 3)
call_4307 = relay.TupleGetItem(func_2034_call(), 3)
func_3493_call = mod.get_global_var('func_3493')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_4320 = relay.TupleGetItem(func_3493_call(), 0)
call_4321 = relay.TupleGetItem(func_3494_call(), 0)
output = relay.Tuple([uop_4301,call_4306,call_4320,])
output2 = relay.Tuple([uop_4303,call_4307,call_4321,])
func_4345 = relay.Function([], output)
mod['func_4345'] = func_4345
mod = relay.transform.InferType()(mod)
output = func_4345()
func_4346 = relay.Function([], output)
mutated_mod['func_4346'] = func_4346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1433_call = mod.get_global_var('func_1433')
func_1435_call = mutated_mod.get_global_var('func_1435')
call_4372 = relay.TupleGetItem(func_1433_call(), 0)
call_4373 = relay.TupleGetItem(func_1435_call(), 0)
func_973_call = mod.get_global_var('func_973')
func_975_call = mutated_mod.get_global_var('func_975')
call_4411 = relay.TupleGetItem(func_973_call(), 1)
call_4412 = relay.TupleGetItem(func_975_call(), 1)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_4428 = func_1016_call(relay.reshape(call_4372.astype('float32'), [3, 15, 7]))
call_4429 = func_1016_call(relay.reshape(call_4372.astype('float32'), [3, 15, 7]))
uop_4432 = relay.erf(call_4372.astype('float32')) # shape=(3, 15, 7)
uop_4434 = relay.erf(call_4373.astype('float32')) # shape=(3, 15, 7)
output = relay.Tuple([call_4411,call_4428,uop_4432,])
output2 = relay.Tuple([call_4412,call_4429,uop_4434,])
func_4442 = relay.Function([], output)
mod['func_4442'] = func_4442
mod = relay.transform.InferType()(mod)
output = func_4442()
func_4443 = relay.Function([], output)
mutated_mod['func_4443'] = func_4443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_4487 = relay.TupleGetItem(func_477_call(), 0)
call_4488 = relay.TupleGetItem(func_479_call(), 0)
output = relay.Tuple([call_4487,])
output2 = relay.Tuple([call_4488,])
func_4514 = relay.Function([], output)
mod['func_4514'] = func_4514
mod = relay.transform.InferType()(mod)
mutated_mod['func_4514'] = func_4514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4514_call = mutated_mod.get_global_var('func_4514')
call_4515 = func_4514_call()
output = call_4515
func_4516 = relay.Function([], output)
mutated_mod['func_4516'] = func_4516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mod.get_global_var('func_1958')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_4538 = relay.TupleGetItem(func_1958_call(), 0)
call_4539 = relay.TupleGetItem(func_1959_call(), 0)
output = relay.Tuple([call_4538,])
output2 = relay.Tuple([call_4539,])
func_4548 = relay.Function([], output)
mod['func_4548'] = func_4548
mod = relay.transform.InferType()(mod)
output = func_4548()
func_4549 = relay.Function([], output)
mutated_mod['func_4549'] = func_4549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4345_call = mod.get_global_var('func_4345')
func_4346_call = mutated_mod.get_global_var('func_4346')
call_4569 = relay.TupleGetItem(func_4345_call(), 0)
call_4570 = relay.TupleGetItem(func_4346_call(), 0)
output = call_4569
output2 = call_4570
func_4628 = relay.Function([], output)
mod['func_4628'] = func_4628
mod = relay.transform.InferType()(mod)
output = func_4628()
func_4629 = relay.Function([], output)
mutated_mod['func_4629'] = func_4629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4548_call = mod.get_global_var('func_4548')
func_4549_call = mutated_mod.get_global_var('func_4549')
call_4647 = relay.TupleGetItem(func_4548_call(), 0)
call_4648 = relay.TupleGetItem(func_4549_call(), 0)
output = call_4647
output2 = call_4648
func_4696 = relay.Function([], output)
mod['func_4696'] = func_4696
mod = relay.transform.InferType()(mod)
output = func_4696()
func_4697 = relay.Function([], output)
mutated_mod['func_4697'] = func_4697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3758_call = mod.get_global_var('func_3758')
func_3759_call = mutated_mod.get_global_var('func_3759')
call_4752 = relay.TupleGetItem(func_3758_call(), 1)
call_4753 = relay.TupleGetItem(func_3759_call(), 1)
var_4767 = relay.var("var_4767", dtype = "float32", shape = (8, 15, 5))#candidate|4767|(8, 15, 5)|var|float32
bop_4768 = relay.maximum(call_4752.astype('uint16'), relay.reshape(var_4767.astype('uint16'), relay.shape_of(call_4752))) # shape=(8, 15, 5)
bop_4771 = relay.maximum(call_4753.astype('uint16'), relay.reshape(var_4767.astype('uint16'), relay.shape_of(call_4753))) # shape=(8, 15, 5)
func_3583_call = mod.get_global_var('func_3583')
func_3587_call = mutated_mod.get_global_var('func_3587')
var_4778 = relay.var("var_4778", dtype = "float32", shape = (56,))#candidate|4778|(56,)|var|float32
const_4779 = relay.const([0.423981,-1.550710,4.713011,9.263895,-0.857094,6.462514,-1.933155,3.924482,-6.996751,-1.503464,4.413721,3.127495,-5.860408,1.724066,-9.157396,-8.186136,-9.013818,2.993445,4.374939,-2.135861,-1.162804,5.347146,6.275378,5.460202,-8.388009,1.245177,6.309877,6.680702,4.507557,9.700153,3.440487,5.800086,8.338584,-6.478966,-3.057667,-6.215256,-7.454796,7.675097,-2.683312,9.085662,-1.395476,-4.698608,0.360924,0.445596,0.459146,-5.998463,-5.391174,-1.511620,3.779247,-9.220680,2.861312,-4.797250,-7.696848,6.005675,-6.701312,4.835484,1.850436,-0.259575,5.120549,0.869429,3.976617,-1.435258,2.589254,2.524389,8.194308,-9.271092,-7.610286,-4.051656,-6.980781,7.631789,-1.544338,0.723307,8.330403,-1.520029,3.737795,2.886575,-3.699982,-9.525093,-6.948644,-3.599980,4.101874,-3.940659,2.572416,9.020611,-9.763758,0.915441,8.457140,-1.603362,-0.337638,-3.773287,-4.634834,-3.002243,2.363587,-7.218279,-1.509819,0.957405,-8.691748,9.020723,-7.779914,3.125170,-0.495591,8.190549,-4.070496,-0.567976,-5.426766,-2.457031,-1.363075,9.723747,-2.171628,5.748890,-2.859082,-8.530435,-3.357818,6.169553,-1.135010,0.650741,9.015036,4.820566,-0.195752,-2.530435,-4.807639,8.408329,-5.775796,-4.282793,-8.241966,6.576923,-0.142148,5.292958,-3.452393,7.176332,-2.543423,0.669096,3.391050,5.531438,-2.035994,-4.818326,-3.618604,8.631249,8.845197,3.980364,7.482103,-6.746675,7.788747,-1.858529,-8.420316,-0.006608,-8.161934,-5.237423,-7.748934,9.636608,-5.483226,9.491797,8.836434,0.789021,-8.474304,-6.892252,2.101690,7.308883,2.060047,-1.919444,0.567307,-8.308170,-1.899928,9.717151,-6.667792,1.938496,8.482128,5.623848,9.242951,6.943504,-7.831058,6.574752,-9.401852,-2.595346,-3.701134,-7.563014,2.161004,3.074613,8.519321,4.787234,0.310127,-9.889503,8.514237,0.953369,-0.739554,6.476696,8.945242,5.542259,4.453288,8.633077,-8.252679,-6.555600,-6.031905,-3.904224,-7.085802,9.296055,-4.472830,-4.768753,6.963443,8.453791,-7.330635,-4.617390,6.908559,-7.439424,5.218939,2.898352,2.018687,-0.714331,4.675835,1.472465,-5.539679,-5.501446,3.477442,-3.942040,-8.436352,-5.461310,-1.494235,-5.936976,-6.498051,7.316859,-2.342057,-1.339888,-4.901179,3.765042,8.030941,5.010625,9.404864,-0.498715,3.298391,-8.059588,-5.185384,-4.022607,4.144919,1.577545,3.581206,-7.551729,1.829037,5.273884,3.946142,7.590942,-1.042948,-9.147034,-7.484833,-3.175527,3.970850,-6.335397,0.866412,8.632975,3.454031,9.487685,5.744480,0.029031,-3.550262,-9.553105,6.893575,-9.907088,-5.934839,-0.254116,8.791676,-6.898907,7.462971,5.425292,-7.410047,1.270423,8.877177,-0.593200,-2.326308,2.556776,2.725251,-9.521521,7.150046,-0.525153,7.776256,8.184868,2.200041,-8.824165,-0.831737,5.909121,-3.294622,-9.368539,1.332472,-4.740163,-6.789384,-1.396790,5.434911,0.892140,0.641166,-4.538898,-9.435262,-6.051171,-4.797389,-8.426094,-6.053123,4.313729,-5.182563,-4.612333,-6.505790,-1.552312,-5.437233,-3.135903,0.674046,-8.294211,7.673818,-8.547773,-1.162792,5.771615,6.680038,1.507445,-4.934259,-7.771482,5.812635,-1.013750,0.067885,-4.705231,-8.265310,8.657177,-0.587157,-2.987150,-7.187625,2.764053,0.929140,1.398316,-3.127985,-0.165327,3.322171,-3.869127,2.555110,0.608814,5.384240,-2.370382,-5.513904,0.090293,-5.128612,5.521762,-9.781177,7.770575,9.118755,-7.511801,-1.620372,-5.947547,3.328168,-6.265275,-1.499347,7.897118,9.628050,9.121728,8.206608,0.645357,-9.832441,7.784658,9.355792,7.765735,7.077049,7.758142,-8.803817,-4.476559,-1.132058,5.120557,-4.431701,-5.108848,-8.871524,8.288369,-5.372198,6.064841,6.716829,-1.103643,-5.770780,-5.591074,7.736410,9.477090,1.142739,-1.939801,-9.999423,-5.992868,-2.553548,-1.157416,-4.929255,2.240321,-0.012086,-7.610594,9.435546,1.034261,-7.759170,3.308034,9.982278,7.089660,-1.782978,-6.492381,7.507574,3.466201,8.300756,9.715559,-7.737455,-3.493343,6.495273,-4.989010,9.714635,-4.368374,6.563398,-4.610794,-9.107215,-9.710428,8.305519,1.965645,9.615201,-7.394919,8.623886,8.609444,-2.111925,-8.330647,-2.196676,-9.803395,-8.884545,2.981263,3.748042,-8.231482,1.615425,-0.445660,0.804528,-9.695313,4.209778,8.270650,-5.401063,-9.795970,8.236560,-1.462074,7.059219,0.575069,-8.500590,-7.864695,-4.486786,2.287391,5.705944,-5.920303,-1.928148,4.011264,-7.952604,-8.219274,9.918640,3.405468,1.818373,-7.073171,9.851146,3.962837,-8.326333,6.149525,-3.694031,1.462312,-5.831698,1.966973,-3.491888,-9.441248,8.493839,2.542603,2.397732,2.695478,-5.383222,-7.298245,-8.255328,7.183448,6.595179,8.680817,-5.789537,4.765031,0.860380,2.668162,2.257836,-6.262823,-4.974976,-5.621202,-1.903450,-3.988120,0.677817,-3.865055,-0.428294,6.194281,-9.879545,-6.742048,2.473496,-0.247294,-8.789865,-9.173840,4.246286,-6.583877,-2.062020,-8.666317,1.556129,0.564226,0.917848,-2.840380,-1.008705,4.999259,-1.974013,7.876989,0.279495,-6.920230,3.805671,6.665636,1.730412,-5.879152,-0.145655,7.429458,4.603210,1.925147,-2.893445,2.341957,9.770493,-9.197864,-9.971299,7.259288,7.105264,9.723611,-9.747454,1.851927,-5.361880,0.101447,-0.907692,-0.737512,0.481831,-3.114778,6.288959,-5.136708,-0.445963,0.295725,-2.897776,-0.942341,-3.340616,-6.464518,3.547898,7.503675,2.624593,-4.853033,3.991028,-4.814394,-5.942894,-3.260163,-1.925487,-7.379991,6.145500,2.792304,-1.883351,3.602701,4.569034,8.105386,-1.396850,-0.609848,3.044905,7.063757,-4.944517,-2.104729,3.014065,-3.799157,9.417592,-7.640993,-6.023274,8.052009,-3.068255,-6.675295,-4.590212,-7.099005,-9.742361,2.409187,4.095909,-2.376363,-9.119570,3.901411,7.224515,1.152567,-5.371189,-2.116212,1.372240,-6.225217,-5.149717,0.655730,-5.534417,0.510171,-0.011582,2.620311,-0.932253,0.703354,-1.012570,-5.612084,0.497867,-4.849246,3.681793,-6.171392,-2.287198,-3.253218,5.577814,-9.567071,5.895923,-5.821856,-6.987146,-1.756253,9.327436,2.112328,-2.170114,-8.731794,5.930969,1.043635,1.578348,0.554046,-7.393657,-2.420243,4.267460,-1.543706,9.808656,-2.190895,-9.092202,-3.173287,1.591906,5.180784,3.197088,1.361689,-4.507311,2.615146,-0.866187,-7.188891,8.617551,0.924087,3.588959,7.499927,-9.271178,-3.540725,-7.331820,7.933983,-0.937200,6.144234,-4.807137,-1.072560,-5.611114,-0.263382,-6.673675,2.962418,9.894726,-0.411439,-9.280693,2.458971,3.875351,1.996816,-4.733345,3.236750,8.717107,-8.049692,1.965225,2.292488,5.306278,9.780688,-2.318144,3.407343,5.086617,-7.738074,6.072979,-9.919154,7.073556,7.325534,-8.736514,-7.101069,8.529138,1.435553,1.966415,-2.020180,-3.336044,-1.974277,3.458487,2.089812,1.391171,-0.807746,2.855854,0.305273,4.687861,9.485420,-1.732846,3.015937,-6.410380,-6.233955,8.515190,-6.979314,-0.643515,-7.968652,-2.931537,-8.376285,7.187182,9.982963,-1.327631,7.377030,6.687797,1.381608,-6.766531,6.283838,-9.864105,-0.824828,6.819472,1.821126,8.320471,9.130833,9.380869,5.275429,-5.831165,-9.173485,-3.107660,-1.037181,-7.652895,1.822533,9.024609,5.698357,-3.919000,0.911065,1.601638,-3.645498,5.348047,-7.010763,8.207096,0.655615,-2.443771,-3.319164,-2.676869,-6.394386,1.496794,6.114388,6.368029,-4.081213,5.106615,4.254061,-6.366894,2.745675,3.761768,2.518042,-3.121075,-6.883736,-4.730946,7.955069,-3.464578,7.307894,6.243685,-3.936946,1.357316,-8.504642,-1.812991,5.699736,1.776805,-5.825255,6.092162,-7.503668,5.308885,-4.806776,2.181029,-1.817294,-3.671189,0.232280,-5.262114,-1.383559,-8.247214,-3.008653,-0.837047,-1.890719,9.471976,-5.073166,-2.950858,-8.689010,3.147222,9.698772,-0.991677,-2.578385,3.051008,-2.869868,7.344438,3.070704,6.056889,1.285102,-8.842484,-7.499799,-2.789992,-6.454480,8.767180,-8.276175,9.552508,4.527445,0.109221,-8.365506,-1.854366,5.937126,4.925819,8.392399,-0.191264,-8.896033,-5.965588,-6.854576,7.152232,2.142903,5.374117,-0.847978,6.071012,-1.067050,2.821944,0.601520,2.841024,-1.233873,-5.483334,-1.594532,-5.593943,0.793178,8.440476,0.787672,-0.331133,3.300637,2.834711,-7.274916,6.686224,3.820543,-4.702601,-4.593192,5.207184,-5.318419,4.240287,9.746144,-0.076867,-6.561726,-0.671945,-6.448138,7.982718,7.483778,3.355883,9.843994,-6.241544,-6.639425,-4.193651,6.743143,2.791340,1.742286,-7.132186,-2.541684,8.067746,-0.462741,-8.442646,-3.564708,-0.564380,-4.292231,6.254982,-9.729565,9.169868,-1.912469,-2.106039,3.175221,-2.487086,-7.843194,4.947980,6.123995,9.699018,2.542812,-5.289535,6.051636,2.245284,6.459095,-9.238653,-5.387838,-8.049589,1.717608,-1.909050,-2.079801,3.079272,5.459877,3.399455,4.535676,-7.383359,-9.972950,-2.428421,2.945698,-0.116497,-1.791775,0.725306,-7.856356,-2.703521,-2.539844,-3.153854,5.074538,0.940712,7.421304,2.686077,7.231800,8.442147,-7.358248,-0.630540,0.046419,-6.947081,7.227716,-3.816540,6.262036,6.814280,-1.847811,-9.149014,8.085535,-1.746414,-2.075069,4.516206,-3.697577], dtype = "float32")#candidate|4779|(896,)|const|float32
var_4780 = relay.var("var_4780", dtype = "uint64", shape = (2, 16))#candidate|4780|(2, 16)|var|uint64
call_4777 = relay.TupleGetItem(func_3583_call(relay.reshape(var_4778.astype('float32'), [4, 14, 1]), relay.reshape(const_4779.astype('float32'), [4, 14, 16]), relay.reshape(var_4780.astype('uint64'), [32,]), ), 0)
call_4781 = relay.TupleGetItem(func_3587_call(relay.reshape(var_4778.astype('float32'), [4, 14, 1]), relay.reshape(const_4779.astype('float32'), [4, 14, 16]), relay.reshape(var_4780.astype('uint64'), [32,]), ), 0)
const_4782 = relay.const([3.974503,-2.967909,0.811101,7.078561,-6.470851,-2.803010,1.542689,-1.673269,4.499950,2.519844,4.301742,9.264811,9.889560,-9.469777,0.570707,-4.374478,8.336095,4.365741,6.798420,6.480273,5.765324,-7.330649,-7.369833,-8.093374,-7.867691,-8.666265,-4.091243,3.384097,0.902609,-3.847980,-5.839112,6.534110,0.841161,-8.646182,-7.849898,1.349604,2.902651,-7.883946,-8.822748,0.540250,3.496973,-2.549014,5.464796,6.110382,7.559447,1.945224,-7.512484,-9.931567,4.387557,-8.736020,-7.649941,3.269879,-7.321811,1.953400,-8.392176,6.704006], dtype = "float32")#candidate|4782|(56,)|const|float32
bop_4783 = relay.not_equal(var_4778.astype('bool'), relay.reshape(const_4782.astype('bool'), relay.shape_of(var_4778))) # shape=(56,)
output = relay.Tuple([bop_4768,call_4777,const_4779,var_4780,bop_4783,])
output2 = relay.Tuple([bop_4771,call_4781,const_4779,var_4780,bop_4783,])
func_4795 = relay.Function([var_4767,var_4778,var_4780,], output)
mod['func_4795'] = func_4795
mod = relay.transform.InferType()(mod)
var_4796 = relay.var("var_4796", dtype = "float32", shape = (8, 15, 5))#candidate|4796|(8, 15, 5)|var|float32
var_4797 = relay.var("var_4797", dtype = "float32", shape = (56,))#candidate|4797|(56,)|var|float32
var_4798 = relay.var("var_4798", dtype = "uint64", shape = (2, 16))#candidate|4798|(2, 16)|var|uint64
output = func_4795(var_4796,var_4797,var_4798,)
func_4799 = relay.Function([var_4796,var_4797,var_4798,], output)
mutated_mod['func_4799'] = func_4799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4696_call = mod.get_global_var('func_4696')
func_4697_call = mutated_mod.get_global_var('func_4697')
call_4824 = func_4696_call()
call_4825 = func_4696_call()
var_4852 = relay.var("var_4852", dtype = "float32", shape = (3, 15, 7))#candidate|4852|(3, 15, 7)|var|float32
bop_4853 = relay.left_shift(call_4824.astype('uint64'), relay.reshape(var_4852.astype('uint64'), relay.shape_of(call_4824))) # shape=(3, 15, 7)
bop_4856 = relay.left_shift(call_4825.astype('uint64'), relay.reshape(var_4852.astype('uint64'), relay.shape_of(call_4825))) # shape=(3, 15, 7)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_4885 = relay.TupleGetItem(func_526_call(), 0)
call_4886 = relay.TupleGetItem(func_527_call(), 0)
output = relay.Tuple([bop_4853,call_4885,])
output2 = relay.Tuple([bop_4856,call_4886,])
func_4890 = relay.Function([var_4852,], output)
mod['func_4890'] = func_4890
mod = relay.transform.InferType()(mod)
var_4891 = relay.var("var_4891", dtype = "float32", shape = (3, 15, 7))#candidate|4891|(3, 15, 7)|var|float32
output = func_4890(var_4891)
func_4892 = relay.Function([var_4891], output)
mutated_mod['func_4892'] = func_4892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_4971 = relay.TupleGetItem(func_1030_call(), 0)
call_4972 = relay.TupleGetItem(func_1031_call(), 0)
uop_4984 = relay.rsqrt(call_4971.astype('float32')) # shape=(4, 12, 8)
uop_4986 = relay.rsqrt(call_4972.astype('float32')) # shape=(4, 12, 8)
bop_4992 = relay.greater(uop_4984.astype('bool'), relay.reshape(call_4971.astype('bool'), relay.shape_of(uop_4984))) # shape=(4, 12, 8)
bop_4995 = relay.greater(uop_4986.astype('bool'), relay.reshape(call_4972.astype('bool'), relay.shape_of(uop_4986))) # shape=(4, 12, 8)
func_3393_call = mod.get_global_var('func_3393')
func_3396_call = mutated_mod.get_global_var('func_3396')
var_5003 = relay.var("var_5003", dtype = "float64", shape = ())#candidate|5003|()|var|float64
call_5002 = relay.TupleGetItem(func_3393_call(relay.reshape(var_5003.astype('float64'), [])), 2)
call_5004 = relay.TupleGetItem(func_3396_call(relay.reshape(var_5003.astype('float64'), [])), 2)
func_4122_call = mod.get_global_var('func_4122')
func_4123_call = mutated_mod.get_global_var('func_4123')
call_5006 = relay.TupleGetItem(func_4122_call(), 0)
call_5007 = relay.TupleGetItem(func_4123_call(), 0)
func_2581_call = mod.get_global_var('func_2581')
func_2583_call = mutated_mod.get_global_var('func_2583')
var_5010 = relay.var("var_5010", dtype = "int64", shape = (192,))#candidate|5010|(192,)|var|int64
call_5009 = relay.TupleGetItem(func_2581_call(relay.reshape(var_5010.astype('int64'), [192,])), 0)
call_5011 = relay.TupleGetItem(func_2583_call(relay.reshape(var_5010.astype('int64'), [192,])), 0)
func_2686_call = mod.get_global_var('func_2686')
func_2689_call = mutated_mod.get_global_var('func_2689')
call_5012 = relay.TupleGetItem(func_2686_call(relay.reshape(uop_4984.astype('float32'), [4, 12, 8])), 3)
call_5013 = relay.TupleGetItem(func_2689_call(relay.reshape(uop_4984.astype('float32'), [4, 12, 8])), 3)
func_1467_call = mod.get_global_var('func_1467')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_5035 = relay.TupleGetItem(func_1467_call(relay.reshape(call_5009.astype('float32'), [3, 15, 7])), 1)
call_5036 = relay.TupleGetItem(func_1470_call(relay.reshape(call_5009.astype('float32'), [3, 15, 7])), 1)
output = relay.Tuple([bop_4992,call_5002,var_5003,call_5006,call_5009,var_5010,call_5012,call_5035,])
output2 = relay.Tuple([bop_4995,call_5004,var_5003,call_5007,call_5011,var_5010,call_5013,call_5036,])
func_5058 = relay.Function([var_5003,var_5010,], output)
mod['func_5058'] = func_5058
mod = relay.transform.InferType()(mod)
mutated_mod['func_5058'] = func_5058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5058_call = mutated_mod.get_global_var('func_5058')
var_5060 = relay.var("var_5060", dtype = "float64", shape = ())#candidate|5060|()|var|float64
var_5061 = relay.var("var_5061", dtype = "int64", shape = (192,))#candidate|5061|(192,)|var|int64
call_5059 = func_5058_call(var_5060,var_5061,)
output = call_5059
func_5062 = relay.Function([var_5060,var_5061,], output)
mutated_mod['func_5062'] = func_5062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3973_call = mod.get_global_var('func_3973')
func_3975_call = mutated_mod.get_global_var('func_3975')
call_5086 = func_3973_call()
call_5087 = func_3973_call()
var_5090 = relay.var("var_5090", dtype = "bool", shape = (4, 12, 8))#candidate|5090|(4, 12, 8)|var|bool
bop_5091 = relay.right_shift(call_5086.astype('uint32'), relay.reshape(var_5090.astype('uint32'), relay.shape_of(call_5086))) # shape=(4, 12, 8)
bop_5094 = relay.right_shift(call_5087.astype('uint32'), relay.reshape(var_5090.astype('uint32'), relay.shape_of(call_5087))) # shape=(4, 12, 8)
output = bop_5091
output2 = bop_5094
func_5101 = relay.Function([var_5090,], output)
mod['func_5101'] = func_5101
mod = relay.transform.InferType()(mod)
mutated_mod['func_5101'] = func_5101
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5102 = relay.var("var_5102", dtype = "bool", shape = (4, 12, 8))#candidate|5102|(4, 12, 8)|var|bool
func_5101_call = mutated_mod.get_global_var('func_5101')
call_5103 = func_5101_call(var_5102)
output = call_5103
func_5104 = relay.Function([var_5102], output)
mutated_mod['func_5104'] = func_5104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1527_call = mod.get_global_var('func_1527')
func_1529_call = mutated_mod.get_global_var('func_1529')
call_5115 = func_1527_call()
call_5116 = func_1527_call()
func_2797_call = mod.get_global_var('func_2797')
func_2799_call = mutated_mod.get_global_var('func_2799')
call_5142 = relay.TupleGetItem(func_2797_call(), 0)
call_5143 = relay.TupleGetItem(func_2799_call(), 0)
output = relay.Tuple([call_5115,call_5142,])
output2 = relay.Tuple([call_5116,call_5143,])
func_5162 = relay.Function([], output)
mod['func_5162'] = func_5162
mod = relay.transform.InferType()(mod)
output = func_5162()
func_5163 = relay.Function([], output)
mutated_mod['func_5163'] = func_5163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1223_call = mod.get_global_var('func_1223')
func_1225_call = mutated_mod.get_global_var('func_1225')
call_5176 = relay.TupleGetItem(func_1223_call(), 1)
call_5177 = relay.TupleGetItem(func_1225_call(), 1)
output = call_5176
output2 = call_5177
func_5185 = relay.Function([], output)
mod['func_5185'] = func_5185
mod = relay.transform.InferType()(mod)
output = func_5185()
func_5186 = relay.Function([], output)
mutated_mod['func_5186'] = func_5186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3493_call = mod.get_global_var('func_3493')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_5187 = relay.TupleGetItem(func_3493_call(), 0)
call_5188 = relay.TupleGetItem(func_3494_call(), 0)
uop_5219 = relay.exp(call_5187.astype('float32')) # shape=(3, 15, 7)
uop_5221 = relay.exp(call_5188.astype('float32')) # shape=(3, 15, 7)
output = uop_5219
output2 = uop_5221
func_5224 = relay.Function([], output)
mod['func_5224'] = func_5224
mod = relay.transform.InferType()(mod)
output = func_5224()
func_5225 = relay.Function([], output)
mutated_mod['func_5225'] = func_5225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2179_call = mod.get_global_var('func_2179')
func_2180_call = mutated_mod.get_global_var('func_2180')
call_5234 = relay.TupleGetItem(func_2179_call(), 2)
call_5235 = relay.TupleGetItem(func_2180_call(), 2)
output = call_5234
output2 = call_5235
func_5261 = relay.Function([], output)
mod['func_5261'] = func_5261
mod = relay.transform.InferType()(mod)
output = func_5261()
func_5262 = relay.Function([], output)
mutated_mod['func_5262'] = func_5262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2129_call = mod.get_global_var('func_2129')
func_2130_call = mutated_mod.get_global_var('func_2130')
call_5308 = relay.TupleGetItem(func_2129_call(), 1)
call_5309 = relay.TupleGetItem(func_2130_call(), 1)
func_4628_call = mod.get_global_var('func_4628')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_5314 = func_4628_call()
call_5315 = func_4628_call()
output = relay.Tuple([call_5308,call_5314,])
output2 = relay.Tuple([call_5309,call_5315,])
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
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_5342 = relay.TupleGetItem(func_1030_call(), 0)
call_5343 = relay.TupleGetItem(func_1031_call(), 0)
output = call_5342
output2 = call_5343
func_5359 = relay.Function([], output)
mod['func_5359'] = func_5359
mod = relay.transform.InferType()(mod)
output = func_5359()
func_5360 = relay.Function([], output)
mutated_mod['func_5360'] = func_5360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mod.get_global_var('func_4208')
func_4210_call = mutated_mod.get_global_var('func_4210')
call_5375 = func_4208_call()
call_5376 = func_4208_call()
output = relay.Tuple([call_5375,])
output2 = relay.Tuple([call_5376,])
func_5392 = relay.Function([], output)
mod['func_5392'] = func_5392
mod = relay.transform.InferType()(mod)
output = func_5392()
func_5393 = relay.Function([], output)
mutated_mod['func_5393'] = func_5393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2826_call = mod.get_global_var('func_2826')
func_2828_call = mutated_mod.get_global_var('func_2828')
call_5397 = relay.TupleGetItem(func_2826_call(), 0)
call_5398 = relay.TupleGetItem(func_2828_call(), 0)
func_5321_call = mod.get_global_var('func_5321')
func_5323_call = mutated_mod.get_global_var('func_5323')
call_5409 = relay.TupleGetItem(func_5321_call(), 0)
call_5410 = relay.TupleGetItem(func_5323_call(), 0)
output = relay.Tuple([call_5397,call_5409,])
output2 = relay.Tuple([call_5398,call_5410,])
func_5411 = relay.Function([], output)
mod['func_5411'] = func_5411
mod = relay.transform.InferType()(mod)
mutated_mod['func_5411'] = func_5411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5411_call = mutated_mod.get_global_var('func_5411')
call_5412 = func_5411_call()
output = call_5412
func_5413 = relay.Function([], output)
mutated_mod['func_5413'] = func_5413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2179_call = mod.get_global_var('func_2179')
func_2180_call = mutated_mod.get_global_var('func_2180')
call_5414 = relay.TupleGetItem(func_2179_call(), 2)
call_5415 = relay.TupleGetItem(func_2180_call(), 2)
func_1771_call = mod.get_global_var('func_1771')
func_1773_call = mutated_mod.get_global_var('func_1773')
call_5417 = relay.TupleGetItem(func_1771_call(), 0)
call_5418 = relay.TupleGetItem(func_1773_call(), 0)
func_3645_call = mod.get_global_var('func_3645')
func_3648_call = mutated_mod.get_global_var('func_3648')
var_5422 = relay.var("var_5422", dtype = "float64", shape = (1155,))#candidate|5422|(1155,)|var|float64
call_5421 = relay.TupleGetItem(func_3645_call(relay.reshape(var_5422.astype('float64'), [7, 11, 15])), 0)
call_5423 = relay.TupleGetItem(func_3648_call(relay.reshape(var_5422.astype('float64'), [7, 11, 15])), 0)
func_3768_call = mod.get_global_var('func_3768')
func_3769_call = mutated_mod.get_global_var('func_3769')
call_5428 = func_3768_call()
call_5429 = func_3768_call()
uop_5448 = relay.sin(call_5428.astype('float64')) # shape=(8, 15, 5)
uop_5450 = relay.sin(call_5429.astype('float64')) # shape=(8, 15, 5)
output = relay.Tuple([call_5414,call_5417,call_5421,var_5422,uop_5448,])
output2 = relay.Tuple([call_5415,call_5418,call_5423,var_5422,uop_5450,])
func_5457 = relay.Function([var_5422,], output)
mod['func_5457'] = func_5457
mod = relay.transform.InferType()(mod)
mutated_mod['func_5457'] = func_5457
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5458 = relay.var("var_5458", dtype = "float64", shape = (1155,))#candidate|5458|(1155,)|var|float64
func_5457_call = mutated_mod.get_global_var('func_5457')
call_5459 = func_5457_call(var_5458)
output = call_5459
func_5460 = relay.Function([var_5458], output)
mutated_mod['func_5460'] = func_5460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1030_call = mod.get_global_var('func_1030')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_5474 = relay.TupleGetItem(func_1030_call(), 0)
call_5475 = relay.TupleGetItem(func_1031_call(), 0)
output = call_5474
output2 = call_5475
func_5521 = relay.Function([], output)
mod['func_5521'] = func_5521
mod = relay.transform.InferType()(mod)
output = func_5521()
func_5522 = relay.Function([], output)
mutated_mod['func_5522'] = func_5522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4005_call = mod.get_global_var('func_4005')
func_4007_call = mutated_mod.get_global_var('func_4007')
call_5566 = relay.TupleGetItem(func_4005_call(), 0)
call_5567 = relay.TupleGetItem(func_4007_call(), 0)
func_555_call = mod.get_global_var('func_555')
func_558_call = mutated_mod.get_global_var('func_558')
const_5576 = relay.const([6,6,7,-4,-1,5,2,-2,-2,6,-2,5,-2,-10,8,-10,3,2,-8,-1,7,-9,-4,5,-1,3,-2,1,7,10,7,8,7,-10,-8,-6,-10,3,7,1,-9,-1,-3,6,6,-5,-7,2,5,-1,-6,-10,-3,10,9,7,-6,-10,3,-10,3,1,-10,-5,7,-10,4,-9,10,-6,1,-8,4,-9,-3,5,4,-5,-8,-1,-6,-8,-10,-7,6,-9,9,-5,5,-1,3,-4,3,-3,-10,8,5,6,2,-6,-1,5,-4,4,-4,-10,4,-4,-3,-9,-1,-9,-6,-2,2,-7,4,-2,4,-10,2,3,-3,-2,4,-9,10,-9,-5,-5,8,-10,7,1,-10,8,-10,-8,8,9,-1,4,8,-10,-6,-2,10,-7,5,-6,8,7,-5,-10,2,4,10,7,-1,3,-3,-2,-6,-7,8,4,-9,3,-5,-6,4,10,-8,-2,-5,8,9,-10,10,3,-3,1,9,6,9,-1,-2,9,-10,-10,-7,5], dtype = "int64")#candidate|5576|(192,)|const|int64
call_5575 = relay.TupleGetItem(func_555_call(relay.reshape(const_5576.astype('int64'), [4, 12, 4])), 0)
call_5577 = relay.TupleGetItem(func_558_call(relay.reshape(const_5576.astype('int64'), [4, 12, 4])), 0)
func_629_call = mod.get_global_var('func_629')
func_632_call = mutated_mod.get_global_var('func_632')
const_5582 = relay.const([10,5,6,1,6,-1,10,8,10,-4,-8,1,6,-9,8,-9,7,-2,9,-9,7,-9,-5,-2,-10,9,-5,-8,-4,-7,8,-3], dtype = "uint64")#candidate|5582|(32,)|const|uint64
call_5581 = relay.TupleGetItem(func_629_call(relay.reshape(const_5582.astype('uint64'), [8, 4, 1])), 1)
call_5583 = relay.TupleGetItem(func_632_call(relay.reshape(const_5582.astype('uint64'), [8, 4, 1])), 1)
func_3758_call = mod.get_global_var('func_3758')
func_3759_call = mutated_mod.get_global_var('func_3759')
call_5600 = relay.TupleGetItem(func_3758_call(), 0)
call_5601 = relay.TupleGetItem(func_3759_call(), 0)
output = relay.Tuple([call_5566,call_5575,const_5576,call_5581,const_5582,call_5600,])
output2 = relay.Tuple([call_5567,call_5577,const_5576,call_5583,const_5582,call_5601,])
func_5602 = relay.Function([], output)
mod['func_5602'] = func_5602
mod = relay.transform.InferType()(mod)
mutated_mod['func_5602'] = func_5602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5602_call = mutated_mod.get_global_var('func_5602')
call_5603 = func_5602_call()
output = call_5603
func_5604 = relay.Function([], output)
mutated_mod['func_5604'] = func_5604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1527_call = mod.get_global_var('func_1527')
func_1529_call = mutated_mod.get_global_var('func_1529')
call_5645 = func_1527_call()
call_5646 = func_1527_call()
func_3583_call = mod.get_global_var('func_3583')
func_3587_call = mutated_mod.get_global_var('func_3587')
const_5655 = relay.const([-5.676906,7.109339,-5.519048,5.620657,-8.087236,-5.932878,9.498651,2.284724,3.135440,-3.177844,7.815121,-1.042098,-2.713584,-6.044520,4.776367,-2.798117,1.316609,2.806728,-1.572410,-2.830030,-4.240558,0.220573,-9.024234,-7.379507,0.415233,1.044200,-7.157854,5.867996,9.827442,-1.345846,-0.776884,-0.142224,9.121143,5.146661,0.180907,-2.524234,-7.432913,9.260636,-8.859376,5.812843,9.994238,-1.081741,-7.413519,-9.264503,1.768256,-5.961679,8.949524,3.037458,-0.182271,-7.846937,5.814965,5.153085,-1.384372,-7.536109,9.740609,6.510177], dtype = "float32")#candidate|5655|(56,)|const|float32
var_5656 = relay.var("var_5656", dtype = "float32", shape = (2, 448))#candidate|5656|(2, 448)|var|float32
var_5657 = relay.var("var_5657", dtype = "uint64", shape = (32,))#candidate|5657|(32,)|var|uint64
call_5654 = relay.TupleGetItem(func_3583_call(relay.reshape(const_5655.astype('float32'), [4, 14, 1]), relay.reshape(var_5656.astype('float32'), [4, 14, 16]), relay.reshape(var_5657.astype('uint64'), [32,]), ), 1)
call_5658 = relay.TupleGetItem(func_3587_call(relay.reshape(const_5655.astype('float32'), [4, 14, 1]), relay.reshape(var_5656.astype('float32'), [4, 14, 16]), relay.reshape(var_5657.astype('uint64'), [32,]), ), 1)
func_1348_call = mod.get_global_var('func_1348')
func_1351_call = mutated_mod.get_global_var('func_1351')
var_5669 = relay.var("var_5669", dtype = "int64", shape = (192,))#candidate|5669|(192,)|var|int64
call_5668 = relay.TupleGetItem(func_1348_call(relay.reshape(var_5669.astype('int64'), [1, 192])), 0)
call_5670 = relay.TupleGetItem(func_1351_call(relay.reshape(var_5669.astype('int64'), [1, 192])), 0)
output = relay.Tuple([call_5645,call_5654,const_5655,var_5656,var_5657,call_5668,var_5669,])
output2 = relay.Tuple([call_5646,call_5658,const_5655,var_5656,var_5657,call_5670,var_5669,])
func_5671 = relay.Function([var_5656,var_5657,var_5669,], output)
mod['func_5671'] = func_5671
mod = relay.transform.InferType()(mod)
var_5672 = relay.var("var_5672", dtype = "float32", shape = (2, 448))#candidate|5672|(2, 448)|var|float32
var_5673 = relay.var("var_5673", dtype = "uint64", shape = (32,))#candidate|5673|(32,)|var|uint64
var_5674 = relay.var("var_5674", dtype = "int64", shape = (192,))#candidate|5674|(192,)|var|int64
output = func_5671(var_5672,var_5673,var_5674,)
func_5675 = relay.Function([var_5672,var_5673,var_5674,], output)
mutated_mod['func_5675'] = func_5675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4442_call = mod.get_global_var('func_4442')
func_4443_call = mutated_mod.get_global_var('func_4443')
call_5743 = relay.TupleGetItem(func_4442_call(), 1)
call_5744 = relay.TupleGetItem(func_4443_call(), 1)
output = relay.Tuple([call_5743,])
output2 = relay.Tuple([call_5744,])
func_5760 = relay.Function([], output)
mod['func_5760'] = func_5760
mod = relay.transform.InferType()(mod)
mutated_mod['func_5760'] = func_5760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5760_call = mutated_mod.get_global_var('func_5760')
call_5761 = func_5760_call()
output = call_5761
func_5762 = relay.Function([], output)
mutated_mod['func_5762'] = func_5762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3758_call = mod.get_global_var('func_3758')
func_3759_call = mutated_mod.get_global_var('func_3759')
call_5808 = relay.TupleGetItem(func_3758_call(), 1)
call_5809 = relay.TupleGetItem(func_3759_call(), 1)
func_1016_call = mod.get_global_var('func_1016')
func_1018_call = mutated_mod.get_global_var('func_1018')
var_5812 = relay.var("var_5812", dtype = "float32", shape = (315,))#candidate|5812|(315,)|var|float32
call_5811 = func_1016_call(relay.reshape(var_5812.astype('float32'), [3, 15, 7]))
call_5813 = func_1016_call(relay.reshape(var_5812.astype('float32'), [3, 15, 7]))
output = relay.Tuple([call_5808,call_5811,var_5812,])
output2 = relay.Tuple([call_5809,call_5813,var_5812,])
func_5821 = relay.Function([var_5812,], output)
mod['func_5821'] = func_5821
mod = relay.transform.InferType()(mod)
mutated_mod['func_5821'] = func_5821
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5822 = relay.var("var_5822", dtype = "float32", shape = (315,))#candidate|5822|(315,)|var|float32
func_5821_call = mutated_mod.get_global_var('func_5821')
call_5823 = func_5821_call(var_5822)
output = call_5823
func_5824 = relay.Function([var_5822], output)
mutated_mod['func_5824'] = func_5824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5521_call = mod.get_global_var('func_5521')
func_5522_call = mutated_mod.get_global_var('func_5522')
call_5828 = func_5521_call()
call_5829 = func_5521_call()
output = call_5828
output2 = call_5829
func_5830 = relay.Function([], output)
mod['func_5830'] = func_5830
mod = relay.transform.InferType()(mod)
mutated_mod['func_5830'] = func_5830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5830_call = mutated_mod.get_global_var('func_5830')
call_5831 = func_5830_call()
output = call_5831
func_5832 = relay.Function([], output)
mutated_mod['func_5832'] = func_5832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5224_call = mod.get_global_var('func_5224')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_5848 = func_5224_call()
call_5849 = func_5224_call()
output = relay.Tuple([call_5848,])
output2 = relay.Tuple([call_5849,])
func_5850 = relay.Function([], output)
mod['func_5850'] = func_5850
mod = relay.transform.InferType()(mod)
output = func_5850()
func_5851 = relay.Function([], output)
mutated_mod['func_5851'] = func_5851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3275_call = mod.get_global_var('func_3275')
func_3276_call = mutated_mod.get_global_var('func_3276')
call_5855 = func_3275_call()
call_5856 = func_3275_call()
func_1467_call = mod.get_global_var('func_1467')
func_1470_call = mutated_mod.get_global_var('func_1470')
var_5863 = relay.var("var_5863", dtype = "float32", shape = (315,))#candidate|5863|(315,)|var|float32
call_5862 = relay.TupleGetItem(func_1467_call(relay.reshape(var_5863.astype('float32'), [3, 15, 7])), 2)
call_5864 = relay.TupleGetItem(func_1470_call(relay.reshape(var_5863.astype('float32'), [3, 15, 7])), 2)
func_2032_call = mod.get_global_var('func_2032')
func_2034_call = mutated_mod.get_global_var('func_2034')
call_5869 = relay.TupleGetItem(func_2032_call(), 1)
call_5870 = relay.TupleGetItem(func_2034_call(), 1)
func_3973_call = mod.get_global_var('func_3973')
func_3975_call = mutated_mod.get_global_var('func_3975')
call_5887 = func_3973_call()
call_5888 = func_3973_call()
output = relay.Tuple([call_5855,call_5862,var_5863,call_5869,call_5887,])
output2 = relay.Tuple([call_5856,call_5864,var_5863,call_5870,call_5888,])
func_5904 = relay.Function([var_5863,], output)
mod['func_5904'] = func_5904
mod = relay.transform.InferType()(mod)
var_5905 = relay.var("var_5905", dtype = "float32", shape = (315,))#candidate|5905|(315,)|var|float32
output = func_5904(var_5905)
func_5906 = relay.Function([var_5905], output)
mutated_mod['func_5906'] = func_5906
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5983 = relay.var("var_5983", dtype = "bool", shape = ())#candidate|5983|()|var|bool
var_5984 = relay.var("var_5984", dtype = "bool", shape = (1, 2, 15))#candidate|5984|(1, 2, 15)|var|bool
bop_5985 = relay.logical_and(var_5983.astype('bool'), var_5984.astype('bool')) # shape=(1, 2, 15)
output = bop_5985
output2 = bop_5985
func_5989 = relay.Function([var_5983,var_5984,], output)
mod['func_5989'] = func_5989
mod = relay.transform.InferType()(mod)
var_5990 = relay.var("var_5990", dtype = "bool", shape = ())#candidate|5990|()|var|bool
var_5991 = relay.var("var_5991", dtype = "bool", shape = (1, 2, 15))#candidate|5991|(1, 2, 15)|var|bool
output = func_5989(var_5990,var_5991,)
func_5992 = relay.Function([var_5990,var_5991,], output)
mutated_mod['func_5992'] = func_5992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4122_call = mod.get_global_var('func_4122')
func_4123_call = mutated_mod.get_global_var('func_4123')
call_6015 = relay.TupleGetItem(func_4122_call(), 0)
call_6016 = relay.TupleGetItem(func_4123_call(), 0)
func_3493_call = mod.get_global_var('func_3493')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_6042 = relay.TupleGetItem(func_3493_call(), 0)
call_6043 = relay.TupleGetItem(func_3494_call(), 0)
output = relay.Tuple([call_6015,call_6042,])
output2 = relay.Tuple([call_6016,call_6043,])
func_6048 = relay.Function([], output)
mod['func_6048'] = func_6048
mod = relay.transform.InferType()(mod)
mutated_mod['func_6048'] = func_6048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6048_call = mutated_mod.get_global_var('func_6048')
call_6049 = func_6048_call()
output = call_6049
func_6050 = relay.Function([], output)
mutated_mod['func_6050'] = func_6050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5411_call = mod.get_global_var('func_5411')
func_5413_call = mutated_mod.get_global_var('func_5413')
call_6113 = relay.TupleGetItem(func_5411_call(), 0)
call_6114 = relay.TupleGetItem(func_5413_call(), 0)
func_3275_call = mod.get_global_var('func_3275')
func_3276_call = mutated_mod.get_global_var('func_3276')
call_6115 = func_3275_call()
call_6116 = func_3275_call()
output = relay.Tuple([call_6113,call_6115,])
output2 = relay.Tuple([call_6114,call_6116,])
func_6145 = relay.Function([], output)
mod['func_6145'] = func_6145
mod = relay.transform.InferType()(mod)
output = func_6145()
func_6146 = relay.Function([], output)
mutated_mod['func_6146'] = func_6146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1812_call = mod.get_global_var('func_1812')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_6157 = func_1812_call()
call_6158 = func_1812_call()
output = relay.Tuple([call_6157,])
output2 = relay.Tuple([call_6158,])
func_6159 = relay.Function([], output)
mod['func_6159'] = func_6159
mod = relay.transform.InferType()(mod)
output = func_6159()
func_6160 = relay.Function([], output)
mutated_mod['func_6160'] = func_6160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5359_call = mod.get_global_var('func_5359')
func_5360_call = mutated_mod.get_global_var('func_5360')
call_6178 = func_5359_call()
call_6179 = func_5359_call()
uop_6201 = relay.sqrt(call_6178.astype('float32')) # shape=(4, 12, 8)
uop_6203 = relay.sqrt(call_6179.astype('float32')) # shape=(4, 12, 8)
func_1348_call = mod.get_global_var('func_1348')
func_1351_call = mutated_mod.get_global_var('func_1351')
const_6207 = relay.const([[9,-8,3,1,-5,-1,7,7,-5,-6,4,-5,-8,-5,-6,10,-4,-10,-10,-5,9,-9,-6,-8,9,-9,6,5,2,-2,-6,-4,1,-7,2,-7,2,9,10,8,1,-4,3,3,-1,2,9,10],[-1,-10,-1,-5,-3,-2,10,-4,-5,-10,-8,-4,9,-6,3,8,-5,6,-7,10,5,-3,-9,-6,5,-5,-10,-10,6,-5,4,-4,4,-6,10,9,5,10,10,2,-3,-6,7,-2,-6,3,-10,8],[4,-5,9,10,7,-9,8,-2,-8,6,6,8,4,-1,-6,-10,-4,-7,-8,-6,8,4,9,-9,-6,-2,-2,6,4,2,-8,-10,-7,7,7,2,1,1,2,8,-6,4,-3,-2,10,6,-6,2],[5,-9,-3,8,-7,-5,-1,-8,-3,5,-3,-2,-10,-10,-5,10,-2,-4,9,10,-3,6,-5,-2,-7,4,-3,2,5,2,6,1,2,-4,5,9,-8,1,9,2,10,7,-4,-9,-3,-8,4,9]], dtype = "int64")#candidate|6207|(4, 48)|const|int64
call_6206 = relay.TupleGetItem(func_1348_call(relay.reshape(const_6207.astype('int64'), [1, 192])), 2)
call_6208 = relay.TupleGetItem(func_1351_call(relay.reshape(const_6207.astype('int64'), [1, 192])), 2)
output = relay.Tuple([uop_6201,call_6206,const_6207,])
output2 = relay.Tuple([uop_6203,call_6208,const_6207,])
func_6222 = relay.Function([], output)
mod['func_6222'] = func_6222
mod = relay.transform.InferType()(mod)
output = func_6222()
func_6223 = relay.Function([], output)
mutated_mod['func_6223'] = func_6223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2486_call = mod.get_global_var('func_2486')
func_2488_call = mutated_mod.get_global_var('func_2488')
call_6289 = func_2486_call()
call_6290 = func_2486_call()
func_1812_call = mod.get_global_var('func_1812')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_6293 = func_1812_call()
call_6294 = func_1812_call()
output = relay.Tuple([call_6289,call_6293,])
output2 = relay.Tuple([call_6290,call_6294,])
func_6302 = relay.Function([], output)
mod['func_6302'] = func_6302
mod = relay.transform.InferType()(mod)
output = func_6302()
func_6303 = relay.Function([], output)
mutated_mod['func_6303'] = func_6303
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6371 = relay.var("var_6371", dtype = "float64", shape = (11, 2, 13))#candidate|6371|(11, 2, 13)|var|float64
uop_6372 = relay.erf(var_6371.astype('float64')) # shape=(11, 2, 13)
uop_6374 = relay.log(var_6371.astype('float32')) # shape=(11, 2, 13)
func_6222_call = mod.get_global_var('func_6222')
func_6223_call = mutated_mod.get_global_var('func_6223')
call_6378 = relay.TupleGetItem(func_6222_call(), 0)
call_6379 = relay.TupleGetItem(func_6223_call(), 0)
output = relay.Tuple([uop_6372,uop_6374,call_6378,])
output2 = relay.Tuple([uop_6372,uop_6374,call_6379,])
func_6422 = relay.Function([var_6371,], output)
mod['func_6422'] = func_6422
mod = relay.transform.InferType()(mod)
mutated_mod['func_6422'] = func_6422
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6423 = relay.var("var_6423", dtype = "float64", shape = (11, 2, 13))#candidate|6423|(11, 2, 13)|var|float64
func_6422_call = mutated_mod.get_global_var('func_6422')
call_6424 = func_6422_call(var_6423)
output = call_6424
func_6425 = relay.Function([var_6423], output)
mutated_mod['func_6425'] = func_6425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_527_call = mutated_mod.get_global_var('func_527')
call_6458 = relay.TupleGetItem(func_526_call(), 0)
call_6459 = relay.TupleGetItem(func_527_call(), 0)
func_838_call = mod.get_global_var('func_838')
func_839_call = mutated_mod.get_global_var('func_839')
call_6476 = relay.TupleGetItem(func_838_call(), 0)
call_6477 = relay.TupleGetItem(func_839_call(), 0)
uop_6478 = relay.asinh(call_6476.astype('float32')) # shape=(2, 192)
uop_6480 = relay.asinh(call_6477.astype('float32')) # shape=(2, 192)
const_6510 = relay.const([[9.064224,-7.967914,-4.201579,-2.999859,-6.178816,-3.115604,1.877021,-0.450918,-7.028909,-1.299617,2.352687,-4.263846,-0.693858,4.118541,-5.449652,5.952895,-1.968561,4.999352,-3.792748,0.174514,-2.887806,3.074845,-4.003368,-5.098513,-3.612315,-1.311060,-8.968742,9.512611,1.467841,1.478853,0.790131,9.314471,-4.613315,-9.482587,-8.871681,3.922063,7.893191,2.844752,9.924524,2.042579,-8.973974,6.125946,-8.568248,-1.075731,5.786676,-2.965510,-3.690988,-4.985616,-4.955533,7.643591,-3.946043,2.525603,1.850651,-9.506214,-2.698383,-1.217883,1.306968,4.157378,-4.636617,3.169532,1.528002,-1.204968,1.872069,-2.242200,-8.156359,8.297239,-1.067449,-1.389129,0.052636,-9.284345,-2.113331,-4.621734,-3.689600,-1.854318,3.789063,4.868272,4.525618,1.159817,-8.783494,-2.708063,8.495976,-5.883094,-8.252391,-5.959518,1.104316,1.228027,5.294797,8.466079,0.116716,8.901987,8.786291,3.826966,-3.714941,4.773376,-6.112575,1.496154,5.149485,5.288940,5.264315,9.549340,9.907178,-4.446720,4.723763,-2.207140,5.984700,3.561706,-9.509988,9.122570,1.639510,-3.449099,-0.936128,-3.139920,6.314999,5.125054,5.430336,8.446120,8.984983,3.862127,4.440085,6.366810,3.130911,1.194935,6.348820,6.549821,6.499379,-4.219729,1.671563,-0.132264,5.687991,2.499052,-6.808640,1.289744,8.324596,-0.746171,-2.969367,0.832603,1.443298,-5.332063,-6.125404,0.722114,1.348273,0.495152,-6.242938,3.284098,-8.089648,-0.916571,0.811576,-8.452745,8.524836,3.567968,4.238029,3.379327,2.192223,3.179379,6.129907,0.921695,3.274922,-7.118912,-5.537886,2.911840,-3.168945,-8.662449,4.103639,-0.131288,3.487030,-5.957483,0.080603,5.109944,9.982485,-6.233476,-0.326669,5.013818,-2.611873,7.575783,3.128646,1.595256,3.902221,0.141317,7.282196,5.883050,1.535509,5.487573,4.385855,4.339538,9.989005,-1.341033,-4.470672,3.229444,2.766645,7.364642,2.354084,-4.481540],[-6.767819,3.271088,-7.080870,0.796514,0.855234,-0.536745,5.412345,1.634286,6.006813,-4.855234,-5.361022,-1.834312,6.066258,-1.690627,7.690232,1.460884,4.827781,7.835820,4.465712,4.616497,3.047012,2.024966,-4.515671,1.804578,-9.102519,1.744720,-3.761886,-0.005367,3.972865,-1.787548,-3.909040,5.335574,1.864164,3.877719,6.606343,1.910266,-4.448334,5.602954,9.863343,-7.214414,9.466470,-6.440263,6.627948,2.244556,-0.816476,4.628347,7.526486,-7.570417,7.701081,5.593105,-2.264154,6.277412,1.224210,0.029347,-9.227475,3.959992,7.399547,1.314638,-7.363746,-3.118295,-8.567825,2.444821,-5.475893,-2.886837,3.869502,-1.484686,-5.396442,-2.033461,-3.400760,0.279643,9.976250,-7.179204,-5.335937,-0.107183,-8.124473,6.749648,-9.780335,-3.034974,-7.661173,2.879516,-9.179324,-5.207510,2.757566,2.009009,-8.506863,-7.665225,6.190225,4.498810,-7.988346,-6.013192,-7.134870,-2.537333,6.967834,4.395480,1.309580,0.023161,-0.765491,4.502673,4.248965,4.988538,3.055681,6.413402,1.585227,-3.853597,-7.832211,-8.937929,9.230041,-1.043403,-9.268328,-3.072529,-7.301440,7.027771,4.487179,-3.586058,9.061193,0.085672,-6.135830,9.315037,4.756346,6.705458,0.366375,-4.568926,-1.683241,7.285454,-1.910940,5.345127,1.567547,8.868814,3.981892,0.376930,2.653990,9.456602,-2.692040,1.233078,-5.179673,5.036404,6.222607,-0.633657,-2.408056,-5.685799,-7.845470,5.021278,-0.592571,-7.903982,6.870708,2.730974,-7.344386,-2.390258,5.785900,-5.729524,-8.722723,1.629229,2.788497,-2.979874,1.241690,-6.059742,-2.314049,-6.750915,-4.576718,-0.820692,-3.986385,1.035860,-2.016082,0.184167,8.295409,8.786118,-4.690810,7.438959,1.742542,5.519900,-7.035285,-3.662782,-7.051490,-6.038326,3.964342,-7.167945,-2.129886,2.348835,0.366705,-1.839173,-2.719000,-4.147464,7.018759,8.579718,9.783058,5.631434,-7.167807,-9.249223,-3.846376,-3.450658,3.971107,-5.259965]], dtype = "float64")#candidate|6510|(2, 192)|const|float64
bop_6511 = relay.power(call_6476.astype('float64'), relay.reshape(const_6510.astype('float64'), relay.shape_of(call_6476))) # shape=(2, 192)
bop_6514 = relay.power(call_6477.astype('float64'), relay.reshape(const_6510.astype('float64'), relay.shape_of(call_6477))) # shape=(2, 192)
uop_6517 = relay.atanh(call_6476.astype('float32')) # shape=(2, 192)
uop_6519 = relay.atanh(call_6477.astype('float32')) # shape=(2, 192)
const_6524 = relay.const([[-5.289141,0.957149,-9.415162,4.231428,2.966986,-8.980961,3.319897,-9.905652,-6.706124,8.869778,2.963894,1.743047,7.172094,-2.927225,2.174878,4.638498,-6.801693,7.888933,0.093281,7.230321,2.904419,-9.214205,-7.471465,3.710423,-3.621708,-9.375088,-3.174372,0.843911,7.515057,5.213501,2.892048,-8.708685,3.744636,2.124317,6.308287,6.586097,-5.677722,2.190751,9.341213,8.844571,1.856542,1.720183,-9.755285,-3.885677,-2.647085,-7.987200,-4.972776,0.427839,-5.705811,-3.123634,-1.805719,-1.977568,7.940453,9.221362,6.010661,-7.625150,-1.624429,-8.313527,-6.995064,-6.259158,-1.699382,0.688092,-5.422860,-8.103898,4.067062,-2.707784,2.131445,-8.801978,-7.646391,9.653441,8.293357,8.776744,0.215741,-3.039302,-5.299602,-0.025969,2.202935,2.764565,6.487465,9.337521,-1.036419,-0.291568,-7.385803,3.376493,-6.738239,-2.027232,-9.161510,7.572294,4.416023,-3.048189,-7.627226,-4.646135,-6.028245,1.497972,-0.567275,-3.232964,-4.491225,-1.469613,3.174880,-5.625134,-3.191710,2.708792,-1.339206,-7.552721,-6.164048,4.781081,4.194387,2.623688,5.501426,7.631380,5.047670,-8.101437,-6.194149,-2.347306,-9.648480,4.617793,-9.218936,-7.666404,0.354064,-9.311449,5.705023,7.444142,-5.915278,-1.771086,9.633129,2.926752,5.290888,0.271572,-6.246445,7.563770,-2.146833,7.739917,-2.216002,0.060400,-8.812872,7.149700,9.166441,-3.410457,6.994902,7.882293,3.941512,9.420100,-0.096548,-2.112207,1.260197,-6.828008,8.088253,-6.629642,9.433084,7.476325,4.438725,3.167261,5.900179,-9.100606,-2.451693,-6.693569,-1.414842,-0.378705,-3.929755,9.626399,-4.337214,6.486992,6.489069,2.185202,2.922830,-4.090899,-3.437987,3.202427,-5.202911,-8.631858,4.192826,-1.452629,1.204642,-1.881439,3.699285,6.792280,6.548339,0.860305,-0.211988,6.777550,-8.365799,-7.137176,3.561617,-6.317074,-6.205451,-2.035033,6.982950,0.319131,0.182572,-6.583685,-4.280884,2.427062],[-1.012746,-0.661402,3.542566,-7.799896,-0.733183,-4.971566,-1.821555,3.075940,-7.347670,-7.330808,-8.944957,-8.897637,-6.518575,-8.919364,-6.652427,-4.667738,4.633424,1.345297,6.095217,-8.483986,-8.461023,9.717810,4.821367,6.302677,5.157364,-4.900246,-9.188119,0.457021,3.557634,6.358219,6.776090,5.807743,-2.605178,-6.837862,-3.067265,4.339783,7.078955,-5.452264,0.311753,-5.441673,1.083271,-3.185664,9.562301,-0.619558,-6.837398,-3.132454,-5.076167,-8.930498,-9.703540,-6.046755,1.282780,-0.416642,-7.645593,7.086924,-3.844219,-5.653723,-2.860947,2.575068,9.636064,2.266851,0.720112,2.292501,3.440611,7.927361,-9.283293,-0.882959,6.790969,4.510019,9.247758,-0.999311,-9.071786,-3.285710,8.272058,5.460826,2.221017,-4.023242,-0.713290,-3.722891,1.341734,-4.963584,1.290942,1.272817,9.572766,2.919029,-4.649975,-8.229920,-3.720433,0.585426,0.023882,-3.182782,7.004866,7.605437,4.155697,2.017060,8.326443,-8.938684,1.620500,-8.901176,-3.068376,5.954296,9.554401,-8.862779,-1.098627,6.168247,-0.207139,2.365833,4.748417,1.994260,-2.665191,7.291154,-9.686534,9.769178,-3.334708,-7.805075,9.029895,8.164523,-6.923130,-9.558933,6.164830,-2.495341,-7.370540,-6.786613,-9.620384,-0.841850,-9.369275,5.950931,2.117550,-1.796451,-3.430457,1.279802,5.730295,-1.827314,-1.527103,-9.530535,-2.506712,8.935441,-9.172751,-0.255056,8.606039,-5.496314,4.012571,4.641251,-3.454527,-5.722934,-5.529480,-7.171604,-1.112863,6.920157,5.206506,-7.808297,-4.956660,-1.565797,4.112295,-2.758210,8.221451,7.641316,-7.774470,-6.123931,-5.516875,2.987832,-4.682958,-4.894098,-9.411142,8.349756,-7.300627,1.480419,9.077452,3.258913,4.251271,9.364871,-3.002573,2.166297,7.708911,1.577844,-3.451683,6.087039,-3.279925,2.648180,9.099562,5.786022,-5.719239,3.744013,-2.659126,0.809119,-3.773777,8.294537,4.879059,3.933211,-8.229490,-8.965729,9.674020,1.559062]], dtype = "float32")#candidate|6524|(2, 192)|const|float32
bop_6525 = relay.floor_divide(uop_6517.astype('float64'), relay.reshape(const_6524.astype('float64'), relay.shape_of(uop_6517))) # shape=(2, 192)
bop_6528 = relay.floor_divide(uop_6519.astype('float64'), relay.reshape(const_6524.astype('float64'), relay.shape_of(uop_6519))) # shape=(2, 192)
output = relay.Tuple([call_6458,uop_6478,bop_6511,bop_6525,])
output2 = relay.Tuple([call_6459,uop_6480,bop_6514,bop_6528,])
func_6537 = relay.Function([], output)
mod['func_6537'] = func_6537
mod = relay.transform.InferType()(mod)
output = func_6537()
func_6538 = relay.Function([], output)
mutated_mod['func_6538'] = func_6538
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6546 = relay.const([[[-3,-3,-4,-5,-4,3,6,3,4,-7,7],[8,9,-6,4,-10,-10,9,9,4,6,9],[1,-6,-1,-7,-8,-8,6,3,3,-6,-8],[8,-2,3,2,-10,6,-9,8,7,-4,-7]],[[9,10,-5,5,-3,3,7,-3,-9,-5,8],[4,-1,6,-4,-6,2,4,-4,1,2,-3],[1,10,-9,-5,-9,5,-9,-7,-1,-7,9],[-10,-10,10,-4,-3,-1,5,9,8,-10,-10]],[[-3,4,-10,-9,-4,-9,10,6,-2,-1,3],[-2,-5,-10,3,-5,-7,-2,-2,5,10,10],[-3,3,7,-10,-9,3,-5,10,3,6,-6],[6,-7,-4,4,6,4,5,-5,-2,-9,10]],[[-5,2,8,9,-4,2,5,10,-3,7,10],[-7,-6,9,3,9,-2,8,-7,-3,-10,-6],[-4,6,-7,-5,6,-9,-10,-8,-10,2,8],[-3,5,-9,5,-1,4,-6,-10,-5,10,9]],[[-6,6,-5,-9,6,-9,-10,-5,-6,3,4],[10,-8,-10,-10,-2,-9,-4,5,-9,-9,-4],[-9,-5,-7,-2,8,7,-8,6,-10,-6,-7],[3,-6,-6,1,4,-9,4,7,-7,9,-1]],[[-4,4,-7,1,1,-7,4,-1,-3,4,4],[-8,-3,4,-10,8,-1,-8,-3,2,2,-10],[-5,3,6,10,7,-8,4,4,-6,9,-5],[6,5,1,-9,6,-1,-4,10,6,-3,-10]],[[6,-2,-8,-2,6,-10,-7,-10,3,-2,7],[-1,3,4,4,4,10,4,5,-1,-3,-3],[2,-9,-9,9,-9,3,-10,10,3,-3,10],[-10,-5,-7,2,1,3,-10,10,-8,-2,3]],[[-8,-5,6,3,-7,-2,-2,3,9,9,-3],[-4,-8,4,-3,-1,1,-1,8,-5,-5,-9],[6,-10,-3,10,-7,1,-7,5,-3,1,4],[2,-4,-9,4,7,-8,-8,5,9,10,-7]],[[-4,-9,1,-10,3,-7,9,-7,1,-2,10],[-4,-5,1,4,6,-2,-4,6,6,-5,6],[10,-6,9,2,7,-6,-10,2,5,-3,-3],[-8,2,-10,-10,1,-2,-10,5,10,-9,-6]],[[3,4,-6,-3,-5,-9,8,4,-8,5,-1],[10,-7,10,7,9,-6,8,-2,-2,-3,-2],[2,6,-2,-9,5,1,-10,-2,-8,6,3],[-5,-4,-2,8,7,-1,-2,-3,-5,2,2]],[[4,-8,-2,6,10,-2,6,1,-9,6,3],[-2,8,-7,-3,2,-3,-2,9,-2,-9,3],[-10,1,-5,1,6,-6,-3,7,-2,-5,-3],[9,5,1,8,9,-10,-1,-1,5,-10,-6]],[[-2,10,5,-8,-2,-10,-10,1,5,-10,-2],[10,-5,-3,-3,-7,3,10,1,-6,-5,-10],[-9,5,-2,-9,-5,-10,-3,3,-3,5,-8],[-5,5,1,-10,-6,-3,3,5,-2,10,-1]]], dtype = "int8")#candidate|6546|(12, 4, 11)|const|int8
var_6547 = relay.var("var_6547", dtype = "int8", shape = (12, 4, 11))#candidate|6547|(12, 4, 11)|var|int8
bop_6548 = relay.not_equal(const_6546.astype('bool'), relay.reshape(var_6547.astype('bool'), relay.shape_of(const_6546))) # shape=(12, 4, 11)
func_4060_call = mod.get_global_var('func_4060')
func_4062_call = mutated_mod.get_global_var('func_4062')
var_6556 = relay.var("var_6556", dtype = "bool", shape = (384,))#candidate|6556|(384,)|var|bool
call_6555 = relay.TupleGetItem(func_4060_call(relay.reshape(var_6556.astype('bool'), [384,])), 3)
call_6557 = relay.TupleGetItem(func_4062_call(relay.reshape(var_6556.astype('bool'), [384,])), 3)
output = relay.Tuple([bop_6548,call_6555,var_6556,])
output2 = relay.Tuple([bop_6548,call_6557,var_6556,])
func_6573 = relay.Function([var_6547,var_6556,], output)
mod['func_6573'] = func_6573
mod = relay.transform.InferType()(mod)
var_6574 = relay.var("var_6574", dtype = "int8", shape = (12, 4, 11))#candidate|6574|(12, 4, 11)|var|int8
var_6575 = relay.var("var_6575", dtype = "bool", shape = (384,))#candidate|6575|(384,)|var|bool
output = func_6573(var_6574,var_6575,)
func_6576 = relay.Function([var_6574,var_6575,], output)
mutated_mod['func_6576'] = func_6576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5392_call = mod.get_global_var('func_5392')
func_5393_call = mutated_mod.get_global_var('func_5393')
call_6578 = relay.TupleGetItem(func_5392_call(), 0)
call_6579 = relay.TupleGetItem(func_5393_call(), 0)
output = call_6578
output2 = call_6579
func_6589 = relay.Function([], output)
mod['func_6589'] = func_6589
mod = relay.transform.InferType()(mod)
output = func_6589()
func_6590 = relay.Function([], output)
mutated_mod['func_6590'] = func_6590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mod.get_global_var('func_477')
func_479_call = mutated_mod.get_global_var('func_479')
call_6605 = relay.TupleGetItem(func_477_call(), 0)
call_6606 = relay.TupleGetItem(func_479_call(), 0)
output = call_6605
output2 = call_6606
func_6623 = relay.Function([], output)
mod['func_6623'] = func_6623
mod = relay.transform.InferType()(mod)
output = func_6623()
func_6624 = relay.Function([], output)
mutated_mod['func_6624'] = func_6624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5185_call = mod.get_global_var('func_5185')
func_5186_call = mutated_mod.get_global_var('func_5186')
call_6808 = func_5185_call()
call_6809 = func_5185_call()
func_4005_call = mod.get_global_var('func_4005')
func_4007_call = mutated_mod.get_global_var('func_4007')
call_6820 = relay.TupleGetItem(func_4005_call(), 1)
call_6821 = relay.TupleGetItem(func_4007_call(), 1)
output = relay.Tuple([call_6808,call_6820,])
output2 = relay.Tuple([call_6809,call_6821,])
func_6837 = relay.Function([], output)
mod['func_6837'] = func_6837
mod = relay.transform.InferType()(mod)
output = func_6837()
func_6838 = relay.Function([], output)
mutated_mod['func_6838'] = func_6838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1812_call = mod.get_global_var('func_1812')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_6866 = func_1812_call()
call_6867 = func_1812_call()
func_3973_call = mod.get_global_var('func_3973')
func_3975_call = mutated_mod.get_global_var('func_3975')
call_6886 = func_3973_call()
call_6887 = func_3973_call()
output = relay.Tuple([call_6866,call_6886,])
output2 = relay.Tuple([call_6867,call_6887,])
func_6889 = relay.Function([], output)
mod['func_6889'] = func_6889
mod = relay.transform.InferType()(mod)
output = func_6889()
func_6890 = relay.Function([], output)
mutated_mod['func_6890'] = func_6890
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6907 = relay.var("var_6907", dtype = "uint32", shape = (8, 2, 13))#candidate|6907|(8, 2, 13)|var|uint32
var_6908 = relay.var("var_6908", dtype = "uint32", shape = (8, 2, 13))#candidate|6908|(8, 2, 13)|var|uint32
bop_6909 = relay.right_shift(var_6907.astype('uint32'), relay.reshape(var_6908.astype('uint32'), relay.shape_of(var_6907))) # shape=(8, 2, 13)
output = relay.Tuple([bop_6909,])
output2 = relay.Tuple([bop_6909,])
func_6946 = relay.Function([var_6907,var_6908,], output)
mod['func_6946'] = func_6946
mod = relay.transform.InferType()(mod)
mutated_mod['func_6946'] = func_6946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6946_call = mutated_mod.get_global_var('func_6946')
var_6948 = relay.var("var_6948", dtype = "uint32", shape = (8, 2, 13))#candidate|6948|(8, 2, 13)|var|uint32
var_6949 = relay.var("var_6949", dtype = "uint32", shape = (8, 2, 13))#candidate|6949|(8, 2, 13)|var|uint32
call_6947 = func_6946_call(var_6948,var_6949,)
output = call_6947
func_6950 = relay.Function([var_6948,var_6949,], output)
mutated_mod['func_6950'] = func_6950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1377_call = mod.get_global_var('func_1377')
func_1379_call = mutated_mod.get_global_var('func_1379')
call_6964 = relay.TupleGetItem(func_1377_call(), 0)
call_6965 = relay.TupleGetItem(func_1379_call(), 0)
output = relay.Tuple([call_6964,])
output2 = relay.Tuple([call_6965,])
func_6968 = relay.Function([], output)
mod['func_6968'] = func_6968
mod = relay.transform.InferType()(mod)
output = func_6968()
func_6969 = relay.Function([], output)
mutated_mod['func_6969'] = func_6969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1527_call = mod.get_global_var('func_1527')
func_1529_call = mutated_mod.get_global_var('func_1529')
call_7005 = func_1527_call()
call_7006 = func_1527_call()
output = relay.Tuple([call_7005,])
output2 = relay.Tuple([call_7006,])
func_7015 = relay.Function([], output)
mod['func_7015'] = func_7015
mod = relay.transform.InferType()(mod)
output = func_7015()
func_7016 = relay.Function([], output)
mutated_mod['func_7016'] = func_7016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6159_call = mod.get_global_var('func_6159')
func_6160_call = mutated_mod.get_global_var('func_6160')
call_7074 = relay.TupleGetItem(func_6159_call(), 0)
call_7075 = relay.TupleGetItem(func_6160_call(), 0)
output = call_7074
output2 = call_7075
func_7078 = relay.Function([], output)
mod['func_7078'] = func_7078
mod = relay.transform.InferType()(mod)
output = func_7078()
func_7079 = relay.Function([], output)
mutated_mod['func_7079'] = func_7079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1443_call = mod.get_global_var('func_1443')
func_1444_call = mutated_mod.get_global_var('func_1444')
call_7176 = relay.TupleGetItem(func_1443_call(), 0)
call_7177 = relay.TupleGetItem(func_1444_call(), 0)
func_4005_call = mod.get_global_var('func_4005')
func_4007_call = mutated_mod.get_global_var('func_4007')
call_7182 = relay.TupleGetItem(func_4005_call(), 2)
call_7183 = relay.TupleGetItem(func_4007_call(), 2)
func_7015_call = mod.get_global_var('func_7015')
func_7016_call = mutated_mod.get_global_var('func_7016')
call_7189 = relay.TupleGetItem(func_7015_call(), 0)
call_7190 = relay.TupleGetItem(func_7016_call(), 0)
output = relay.Tuple([call_7176,call_7182,call_7189,])
output2 = relay.Tuple([call_7177,call_7183,call_7190,])
func_7191 = relay.Function([], output)
mod['func_7191'] = func_7191
mod = relay.transform.InferType()(mod)
mutated_mod['func_7191'] = func_7191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7191_call = mutated_mod.get_global_var('func_7191')
call_7192 = func_7191_call()
output = call_7192
func_7193 = relay.Function([], output)
mutated_mod['func_7193'] = func_7193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_884_call = mod.get_global_var('func_884')
func_885_call = mutated_mod.get_global_var('func_885')
call_7223 = func_884_call()
call_7224 = func_884_call()
func_152_call = mod.get_global_var('func_152')
func_156_call = mutated_mod.get_global_var('func_156')
call_7230 = func_152_call(relay.reshape(call_7223.astype('float64'), [4, 12, 8]), relay.reshape(call_7223.astype('float64'), [4, 12, 8]), )
call_7231 = func_152_call(relay.reshape(call_7223.astype('float64'), [4, 12, 8]), relay.reshape(call_7223.astype('float64'), [4, 12, 8]), )
func_1546_call = mod.get_global_var('func_1546')
func_1550_call = mutated_mod.get_global_var('func_1550')
const_7252 = relay.const([-10,5,-4,5,3,10,8,10,-10,-1,-5,-1,5,-10,-8,5,-7,-5,7,6,7,4,4,1,-4,8,-5,8,-4,6,-9,-9,3,7,4,-8,1,-8,5,-10,4,-10,-8,-10,1,6,8,6,1,-1,-9,8,2,-5,-9,-6,7,-3,-6,-9,10,-5,-1,10,-4,-9,-2,3,4,1,-4,-6], dtype = "int64")#candidate|7252|(72,)|const|int64
call_7251 = func_1546_call(relay.reshape(const_7252.astype('int64'), [3, 3, 8]), relay.reshape(const_7252.astype('int64'), [3, 3, 8]), )
call_7253 = func_1546_call(relay.reshape(const_7252.astype('int64'), [3, 3, 8]), relay.reshape(const_7252.astype('int64'), [3, 3, 8]), )
bop_7262 = relay.floor_divide(call_7251.astype('float64'), relay.reshape(const_7252.astype('float64'), relay.shape_of(call_7251))) # shape=(3, 3, 8)
bop_7265 = relay.floor_divide(call_7253.astype('float64'), relay.reshape(const_7252.astype('float64'), relay.shape_of(call_7253))) # shape=(3, 3, 8)
func_5821_call = mod.get_global_var('func_5821')
func_5824_call = mutated_mod.get_global_var('func_5824')
const_7269 = relay.const([[8.172954,-9.102062,-3.428536],[8.715454,4.474148,6.014073],[-9.882782,-7.924597,6.094205],[-8.140185,5.769736,-9.775490],[1.833934,-2.904605,-3.283207],[3.618675,-5.029441,3.150805],[4.605805,7.331540,7.636703],[9.520478,9.516631,-8.362818],[6.613208,9.871035,-6.327375],[-5.325637,6.820306,4.950550],[6.162459,5.879511,-7.561886],[-7.095804,4.185931,-5.503958],[5.918808,-9.621053,-2.927232],[3.058135,1.368661,-3.841757],[-2.828483,-7.701902,6.798957],[5.921225,-5.919925,6.721478],[-7.720280,-9.728772,1.380580],[-3.825044,2.356897,0.067022],[0.660573,7.759997,-1.350400],[-8.329580,2.877600,-5.918946],[-5.157066,3.965639,4.497892],[-5.533609,-0.310750,7.481030],[6.357769,-5.189840,4.148642],[-6.368589,8.136786,6.786585],[-2.681189,-9.762459,-1.492215],[-1.133657,9.882379,0.650976],[-0.535526,-6.167146,5.001879],[8.044384,2.680413,5.676468],[6.024311,7.983446,2.363817],[-3.037814,-8.309274,3.951465],[-3.308687,2.550420,0.820865],[-3.538810,-0.785224,1.530162],[-0.218174,8.158129,-3.346351],[-2.829039,-7.099255,-6.977730],[1.328929,4.783741,-5.686513],[-7.158331,1.471341,-0.431263],[7.718884,-4.045954,5.473221],[0.924590,-0.022739,4.430353],[0.923846,4.705792,5.306838],[7.313988,-1.477184,-2.937204],[-4.126697,0.130079,-7.425729],[-1.556027,-3.381538,-9.342963],[-8.390335,-6.242496,-9.402313],[-2.348674,4.145112,1.329133],[8.125707,9.814365,-9.752779],[-9.669472,8.730591,-7.776208],[9.597538,2.573008,8.210215],[7.545786,4.945118,5.491911],[0.165426,9.334624,4.331602],[5.677808,3.333697,-1.591330],[-4.708838,-4.093970,4.927776],[-6.026437,-3.060465,-6.107348],[1.456827,7.853412,4.247673],[-6.047342,-2.808795,-9.264049],[-2.384346,5.125190,-5.559716],[2.819828,-8.753565,-6.451000],[-9.239916,8.116537,-2.570463],[4.385429,4.792331,-9.436917],[7.772543,-4.594935,-9.502362],[3.135977,-4.665569,1.242931],[-4.121639,-3.623614,-5.047441],[-7.601480,0.785375,5.310085],[-5.826212,6.477262,-0.944964],[-8.770938,-3.337195,9.469281],[9.521588,1.073053,8.630827],[8.555309,-2.763668,8.789888],[-9.449292,0.377102,5.328755],[-9.786803,8.364845,5.122611],[5.351148,1.371853,-2.824360],[2.040804,4.528881,-5.243487],[7.072937,5.746311,1.188955],[-0.648398,-0.598609,3.464950],[6.552333,1.933202,1.625374],[-0.445883,7.091966,-1.068204],[-0.517559,9.301623,-9.937168],[4.044511,1.895244,8.531038],[2.510577,6.702560,-1.456121],[6.641829,-1.266436,-3.545129],[4.542352,-5.583587,7.154325],[4.988282,-5.388346,1.292972],[-1.913789,-1.891674,5.328920],[-6.771350,-2.595854,0.111835],[-8.290340,-5.309274,8.442121],[-9.782735,9.584127,9.003961],[1.262828,-8.925463,-6.558794],[-1.380695,-7.032090,-8.065066],[5.395872,-3.052696,-2.170481],[-7.855420,-9.123874,7.809878],[0.306415,5.748350,9.640529],[9.341791,1.731990,-0.088509],[-4.983374,-0.952431,-4.798153],[-3.868635,4.922097,9.442217],[-8.458753,-6.379909,-7.432000],[6.485816,3.641351,-8.559428],[4.175359,0.594496,3.182205],[-9.326108,-8.911859,4.157433],[-9.820002,-8.393057,-0.262695],[5.720288,2.811782,-9.388410],[-1.374443,-9.183376,-5.882215],[-0.399780,-6.505031,-6.708049],[0.002969,1.995140,7.951601],[-4.906564,5.765831,2.022482],[-2.697061,-2.527132,-7.226871],[1.249041,-1.525873,-9.877951],[-3.673489,4.619360,-3.508137]], dtype = "float32")#candidate|7269|(105, 3)|const|float32
call_7268 = relay.TupleGetItem(func_5821_call(relay.reshape(const_7269.astype('float32'), [315,])), 1)
call_7270 = relay.TupleGetItem(func_5824_call(relay.reshape(const_7269.astype('float32'), [315,])), 1)
uop_7271 = relay.cosh(const_7269.astype('float32')) # shape=(105, 3)
func_2753_call = mod.get_global_var('func_2753')
func_2755_call = mutated_mod.get_global_var('func_2755')
call_7274 = relay.TupleGetItem(func_2753_call(), 1)
call_7275 = relay.TupleGetItem(func_2755_call(), 1)
uop_7279 = relay.rsqrt(uop_7271.astype('float64')) # shape=(105, 3)
uop_7283 = relay.atanh(uop_7279.astype('float64')) # shape=(105, 3)
func_3787_call = mod.get_global_var('func_3787')
func_3789_call = mutated_mod.get_global_var('func_3789')
call_7293 = relay.TupleGetItem(func_3787_call(), 0)
call_7294 = relay.TupleGetItem(func_3789_call(), 0)
output = relay.Tuple([call_7223,call_7230,bop_7262,call_7268,call_7274,uop_7283,call_7293,])
output2 = relay.Tuple([call_7224,call_7231,bop_7265,call_7270,call_7275,uop_7283,call_7294,])
func_7301 = relay.Function([], output)
mod['func_7301'] = func_7301
mod = relay.transform.InferType()(mod)
mutated_mod['func_7301'] = func_7301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7301_call = mutated_mod.get_global_var('func_7301')
call_7302 = func_7301_call()
output = call_7302
func_7303 = relay.Function([], output)
mutated_mod['func_7303'] = func_7303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5760_call = mod.get_global_var('func_5760')
func_5762_call = mutated_mod.get_global_var('func_5762')
call_7358 = relay.TupleGetItem(func_5760_call(), 0)
call_7359 = relay.TupleGetItem(func_5762_call(), 0)
func_2486_call = mod.get_global_var('func_2486')
func_2488_call = mutated_mod.get_global_var('func_2488')
call_7363 = func_2486_call()
call_7364 = func_2486_call()
output = relay.Tuple([call_7358,call_7363,])
output2 = relay.Tuple([call_7359,call_7364,])
func_7365 = relay.Function([], output)
mod['func_7365'] = func_7365
mod = relay.transform.InferType()(mod)
output = func_7365()
func_7366 = relay.Function([], output)
mutated_mod['func_7366'] = func_7366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3973_call = mod.get_global_var('func_3973')
func_3975_call = mutated_mod.get_global_var('func_3975')
call_7461 = func_3973_call()
call_7462 = func_3973_call()
func_5521_call = mod.get_global_var('func_5521')
func_5522_call = mutated_mod.get_global_var('func_5522')
call_7466 = func_5521_call()
call_7467 = func_5521_call()
output = relay.Tuple([call_7461,call_7466,])
output2 = relay.Tuple([call_7462,call_7467,])
func_7479 = relay.Function([], output)
mod['func_7479'] = func_7479
mod = relay.transform.InferType()(mod)
mutated_mod['func_7479'] = func_7479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7479_call = mutated_mod.get_global_var('func_7479')
call_7480 = func_7479_call()
output = call_7480
func_7481 = relay.Function([], output)
mutated_mod['func_7481'] = func_7481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_838_call = mod.get_global_var('func_838')
func_839_call = mutated_mod.get_global_var('func_839')
call_7482 = relay.TupleGetItem(func_838_call(), 0)
call_7483 = relay.TupleGetItem(func_839_call(), 0)
func_5602_call = mod.get_global_var('func_5602')
func_5604_call = mutated_mod.get_global_var('func_5604')
call_7486 = relay.TupleGetItem(func_5602_call(), 4)
call_7487 = relay.TupleGetItem(func_5604_call(), 4)
func_4005_call = mod.get_global_var('func_4005')
func_4007_call = mutated_mod.get_global_var('func_4007')
call_7493 = relay.TupleGetItem(func_4005_call(), 0)
call_7494 = relay.TupleGetItem(func_4007_call(), 0)
output = relay.Tuple([call_7482,call_7486,call_7493,])
output2 = relay.Tuple([call_7483,call_7487,call_7494,])
func_7498 = relay.Function([], output)
mod['func_7498'] = func_7498
mod = relay.transform.InferType()(mod)
output = func_7498()
func_7499 = relay.Function([], output)
mutated_mod['func_7499'] = func_7499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_578_call = mod.get_global_var('func_578')
func_579_call = mutated_mod.get_global_var('func_579')
call_7541 = relay.TupleGetItem(func_578_call(), 3)
call_7542 = relay.TupleGetItem(func_579_call(), 3)
func_5321_call = mod.get_global_var('func_5321')
func_5323_call = mutated_mod.get_global_var('func_5323')
call_7543 = relay.TupleGetItem(func_5321_call(), 0)
call_7544 = relay.TupleGetItem(func_5323_call(), 0)
output = relay.Tuple([call_7541,call_7543,])
output2 = relay.Tuple([call_7542,call_7544,])
func_7551 = relay.Function([], output)
mod['func_7551'] = func_7551
mod = relay.transform.InferType()(mod)
output = func_7551()
func_7552 = relay.Function([], output)
mutated_mod['func_7552'] = func_7552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_578_call = mod.get_global_var('func_578')
func_579_call = mutated_mod.get_global_var('func_579')
call_7560 = relay.TupleGetItem(func_578_call(), 0)
call_7561 = relay.TupleGetItem(func_579_call(), 0)
func_5989_call = mod.get_global_var('func_5989')
func_5992_call = mutated_mod.get_global_var('func_5992')
var_7589 = relay.var("var_7589", dtype = "bool", shape = ())#candidate|7589|()|var|bool
const_7590 = relay.const([[True,False,False,False,False,True],[True,False,False,False,True,False],[False,True,False,False,True,True],[True,True,False,False,False,True],[False,True,False,True,True,False]], dtype = "bool")#candidate|7590|(5, 6)|const|bool
call_7588 = func_5989_call(relay.reshape(var_7589.astype('bool'), []), relay.reshape(const_7590.astype('bool'), [1, 2, 15]), )
call_7591 = func_5989_call(relay.reshape(var_7589.astype('bool'), []), relay.reshape(const_7590.astype('bool'), [1, 2, 15]), )
func_6889_call = mod.get_global_var('func_6889')
func_6890_call = mutated_mod.get_global_var('func_6890')
call_7597 = relay.TupleGetItem(func_6889_call(), 0)
call_7598 = relay.TupleGetItem(func_6890_call(), 0)
output = relay.Tuple([call_7560,call_7588,var_7589,const_7590,call_7597,])
output2 = relay.Tuple([call_7561,call_7591,var_7589,const_7590,call_7598,])
func_7609 = relay.Function([var_7589,], output)
mod['func_7609'] = func_7609
mod = relay.transform.InferType()(mod)
mutated_mod['func_7609'] = func_7609
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7610 = relay.var("var_7610", dtype = "bool", shape = ())#candidate|7610|()|var|bool
func_7609_call = mutated_mod.get_global_var('func_7609')
call_7611 = func_7609_call(var_7610)
output = call_7611
func_7612 = relay.Function([var_7610], output)
mutated_mod['func_7612'] = func_7612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2390_call = mod.get_global_var('func_2390')
func_2392_call = mutated_mod.get_global_var('func_2392')
call_7643 = relay.TupleGetItem(func_2390_call(), 0)
call_7644 = relay.TupleGetItem(func_2392_call(), 0)
output = relay.Tuple([call_7643,])
output2 = relay.Tuple([call_7644,])
func_7669 = relay.Function([], output)
mod['func_7669'] = func_7669
mod = relay.transform.InferType()(mod)
mutated_mod['func_7669'] = func_7669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7669_call = mutated_mod.get_global_var('func_7669')
call_7670 = func_7669_call()
output = call_7670
func_7671 = relay.Function([], output)
mutated_mod['func_7671'] = func_7671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5411_call = mod.get_global_var('func_5411')
func_5413_call = mutated_mod.get_global_var('func_5413')
call_7711 = relay.TupleGetItem(func_5411_call(), 0)
call_7712 = relay.TupleGetItem(func_5413_call(), 0)
output = relay.Tuple([call_7711,])
output2 = relay.Tuple([call_7712,])
func_7719 = relay.Function([], output)
mod['func_7719'] = func_7719
mod = relay.transform.InferType()(mod)
output = func_7719()
func_7720 = relay.Function([], output)
mutated_mod['func_7720'] = func_7720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7719_call = mod.get_global_var('func_7719')
func_7720_call = mutated_mod.get_global_var('func_7720')
call_7727 = relay.TupleGetItem(func_7719_call(), 0)
call_7728 = relay.TupleGetItem(func_7720_call(), 0)
output = call_7727
output2 = call_7728
func_7751 = relay.Function([], output)
mod['func_7751'] = func_7751
mod = relay.transform.InferType()(mod)
output = func_7751()
func_7752 = relay.Function([], output)
mutated_mod['func_7752'] = func_7752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2179_call = mod.get_global_var('func_2179')
func_2180_call = mutated_mod.get_global_var('func_2180')
call_7778 = relay.TupleGetItem(func_2179_call(), 2)
call_7779 = relay.TupleGetItem(func_2180_call(), 2)
func_7479_call = mod.get_global_var('func_7479')
func_7481_call = mutated_mod.get_global_var('func_7481')
call_7811 = relay.TupleGetItem(func_7479_call(), 1)
call_7812 = relay.TupleGetItem(func_7481_call(), 1)
output = relay.Tuple([call_7778,call_7811,])
output2 = relay.Tuple([call_7779,call_7812,])
func_7817 = relay.Function([], output)
mod['func_7817'] = func_7817
mod = relay.transform.InferType()(mod)
mutated_mod['func_7817'] = func_7817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7817_call = mutated_mod.get_global_var('func_7817')
call_7818 = func_7817_call()
output = call_7818
func_7819 = relay.Function([], output)
mutated_mod['func_7819'] = func_7819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6145_call = mod.get_global_var('func_6145')
func_6146_call = mutated_mod.get_global_var('func_6146')
call_7885 = relay.TupleGetItem(func_6145_call(), 1)
call_7886 = relay.TupleGetItem(func_6146_call(), 1)
output = call_7885
output2 = call_7886
func_7890 = relay.Function([], output)
mod['func_7890'] = func_7890
mod = relay.transform.InferType()(mod)
output = func_7890()
func_7891 = relay.Function([], output)
mutated_mod['func_7891'] = func_7891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3019_call = mod.get_global_var('func_3019')
func_3020_call = mutated_mod.get_global_var('func_3020')
call_7894 = relay.TupleGetItem(func_3019_call(), 0)
call_7895 = relay.TupleGetItem(func_3020_call(), 0)
func_2032_call = mod.get_global_var('func_2032')
func_2034_call = mutated_mod.get_global_var('func_2034')
call_7904 = relay.TupleGetItem(func_2032_call(), 0)
call_7905 = relay.TupleGetItem(func_2034_call(), 0)
var_7910 = relay.var("var_7910", dtype = "float64", shape = (2, 192))#candidate|7910|(2, 192)|var|float64
bop_7911 = relay.equal(call_7904.astype('bool'), relay.reshape(var_7910.astype('bool'), relay.shape_of(call_7904))) # shape=(2, 192)
bop_7914 = relay.equal(call_7905.astype('bool'), relay.reshape(var_7910.astype('bool'), relay.shape_of(call_7905))) # shape=(2, 192)
output = relay.Tuple([call_7894,bop_7911,])
output2 = relay.Tuple([call_7895,bop_7914,])
func_7920 = relay.Function([var_7910,], output)
mod['func_7920'] = func_7920
mod = relay.transform.InferType()(mod)
mutated_mod['func_7920'] = func_7920
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7921 = relay.var("var_7921", dtype = "float64", shape = (2, 192))#candidate|7921|(2, 192)|var|float64
func_7920_call = mutated_mod.get_global_var('func_7920')
call_7922 = func_7920_call(var_7921)
output = call_7922
func_7923 = relay.Function([var_7921], output)
mutated_mod['func_7923'] = func_7923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5321_call = mod.get_global_var('func_5321')
func_5323_call = mutated_mod.get_global_var('func_5323')
call_7941 = relay.TupleGetItem(func_5321_call(), 1)
call_7942 = relay.TupleGetItem(func_5323_call(), 1)
func_1132_call = mod.get_global_var('func_1132')
func_1135_call = mutated_mod.get_global_var('func_1135')
const_7966 = relay.const([8.269690,-1.931902,2.301560,-0.971571,0.797410,5.651755,-1.949048,-8.725267,-3.590634,-0.158168,0.091942,3.929967,-7.238083,6.499760,-7.767716,2.397147,-4.020800,0.846115,7.200522,9.616738,4.218834,4.350054,-7.503112,-0.615829,6.272793,6.353651,-6.522384,-1.701090,-4.569758,3.764112,1.164673,-0.135949,-8.974492,4.651094,0.945074,-2.413405,-3.802015,-2.282813,8.437460,3.024987,4.593231,-5.457527,-9.925759,2.589284,-0.215991,6.505636,5.215786,0.745078,2.188492,3.466426,-3.243591,-4.610696,-2.941585,9.365806,9.113969,-9.907002,-4.025226,-8.926550,1.016517,7.034345,-6.969587,1.803305,-0.949910,-1.258229,-6.400767,-9.857700,3.291761,6.018173,-7.977082,-9.818926,0.682966,-6.798362,9.481864,-2.277399,-8.377301,-8.772198,-5.702892,-0.888336,-2.513723,9.881920,4.124618,8.768117,-2.592427,-1.829192], dtype = "float32")#candidate|7966|(84,)|const|float32
call_7965 = func_1132_call(relay.reshape(const_7966.astype('float32'), [14, 2, 3]))
call_7967 = func_1132_call(relay.reshape(const_7966.astype('float32'), [14, 2, 3]))
func_5521_call = mod.get_global_var('func_5521')
func_5522_call = mutated_mod.get_global_var('func_5522')
call_7970 = func_5521_call()
call_7971 = func_5521_call()
func_2390_call = mod.get_global_var('func_2390')
func_2392_call = mutated_mod.get_global_var('func_2392')
call_7972 = relay.TupleGetItem(func_2390_call(), 0)
call_7973 = relay.TupleGetItem(func_2392_call(), 0)
func_3758_call = mod.get_global_var('func_3758')
func_3759_call = mutated_mod.get_global_var('func_3759')
call_7979 = relay.TupleGetItem(func_3758_call(), 0)
call_7980 = relay.TupleGetItem(func_3759_call(), 0)
bop_7985 = relay.divide(call_7941.astype('float32'), relay.reshape(call_7979.astype('float32'), relay.shape_of(call_7941))) # shape=(3, 15, 7)
bop_7988 = relay.divide(call_7942.astype('float32'), relay.reshape(call_7980.astype('float32'), relay.shape_of(call_7942))) # shape=(3, 15, 7)
func_7301_call = mod.get_global_var('func_7301')
func_7303_call = mutated_mod.get_global_var('func_7303')
call_7991 = relay.TupleGetItem(func_7301_call(), 2)
call_7992 = relay.TupleGetItem(func_7303_call(), 2)
func_5904_call = mod.get_global_var('func_5904')
func_5906_call = mutated_mod.get_global_var('func_5906')
call_8043 = relay.TupleGetItem(func_5904_call(relay.reshape(call_7941.astype('float32'), [315,])), 2)
call_8044 = relay.TupleGetItem(func_5906_call(relay.reshape(call_7941.astype('float32'), [315,])), 2)
output = relay.Tuple([call_7965,const_7966,call_7970,call_7972,bop_7985,call_7991,call_8043,])
output2 = relay.Tuple([call_7967,const_7966,call_7971,call_7973,bop_7988,call_7992,call_8044,])
func_8057 = relay.Function([], output)
mod['func_8057'] = func_8057
mod = relay.transform.InferType()(mod)
mutated_mod['func_8057'] = func_8057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8057_call = mutated_mod.get_global_var('func_8057')
call_8058 = func_8057_call()
output = call_8058
func_8059 = relay.Function([], output)
mutated_mod['func_8059'] = func_8059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5185_call = mod.get_global_var('func_5185')
func_5186_call = mutated_mod.get_global_var('func_5186')
call_8060 = func_5185_call()
call_8061 = func_5185_call()
output = call_8060
output2 = call_8061
func_8065 = relay.Function([], output)
mod['func_8065'] = func_8065
mod = relay.transform.InferType()(mod)
mutated_mod['func_8065'] = func_8065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8065_call = mutated_mod.get_global_var('func_8065')
call_8066 = func_8065_call()
output = call_8066
func_8067 = relay.Function([], output)
mutated_mod['func_8067'] = func_8067
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8085 = relay.const([[[3.310145,-6.061959,-5.094529,-7.993195,-3.226155,8.065706,-1.282380,5.582890,-9.989965,6.161417,-6.453960,-2.463170,5.131253,-0.787504,-0.635884,-3.073365],[-7.622369,1.665869,2.643232,-3.136828,7.764455,2.469316,-1.407743,-5.100314,-6.921004,-7.129135,3.906985,5.733753,8.425536,-1.311247,8.857755,3.002220],[6.798211,-0.138727,7.515855,-5.525545,3.059763,-7.380777,-3.819804,-1.746234,3.045412,-6.474603,8.617751,4.145744,9.476180,9.335322,9.828980,-1.297055],[9.379587,0.618782,5.591725,9.012632,3.276709,1.375387,-2.082041,-6.320790,-3.381008,-4.572996,9.227019,-9.318322,3.526065,1.044831,6.718236,8.858745],[3.241268,9.122744,-4.954297,4.313238,-7.735480,-4.282695,-3.773494,-7.650938,7.452229,-2.679677,0.286522,2.096207,-1.254037,0.298558,-5.822968,-3.087532],[4.333917,-3.431728,-4.069319,5.251954,-7.005303,5.928360,-4.551008,-3.995908,-7.291600,-7.605597,2.775675,-1.670360,6.183187,3.410828,-0.590925,7.806943],[3.883162,-6.245212,5.612537,5.191873,8.384604,-9.281833,-6.941656,0.583389,3.737347,-5.866012,2.564642,3.914542,-5.014051,-8.857747,-3.313865,-3.448034],[1.092734,-8.614134,-4.430692,4.296198,-4.090418,-3.897943,-5.211554,-2.527046,2.945706,-2.720168,1.423962,8.364392,3.310824,3.016186,1.670780,1.267857],[-3.769005,7.289707,6.131746,-8.323863,-2.758927,4.673404,-4.149225,1.247704,-4.071402,-0.005042,7.933484,-5.699092,6.265414,-9.230749,3.025275,0.224637],[6.968104,0.402070,0.458950,2.545387,-9.736913,-3.465109,-4.585156,-3.817988,-0.365255,-7.358451,8.489027,-9.817871,-1.884625,4.625057,-0.821783,0.031843],[-9.298409,1.035475,-7.303297,3.845165,6.900162,6.616973,4.547626,-9.376450,-7.407904,5.313014,8.679861,-2.345085,5.109301,-8.560423,9.288284,3.413861],[-1.767251,1.810647,4.700916,6.654772,3.955023,-6.116638,-5.984698,-1.013255,-2.269889,-3.298214,6.802386,4.483308,5.348378,-6.134883,-9.704631,-8.925739],[-2.035761,0.960125,-6.876968,-1.509594,-2.804583,9.366512,-0.211389,7.288026,7.173400,-4.653652,3.315024,8.761274,0.619484,7.266948,-0.133959,-0.207095]],[[7.371012,-1.977705,-3.047923,7.854968,-4.884468,-6.325586,-6.056884,1.456822,3.668877,-4.388516,8.642977,3.883129,-8.273243,-1.602979,-0.500402,9.449705],[5.123184,-1.417584,2.837464,-5.289487,-1.070730,-7.305690,-6.582203,-3.681796,5.248903,-4.324941,0.654827,-1.570129,-2.377087,-8.613349,6.942938,6.594708],[5.411419,7.350670,4.799515,-9.842530,-7.904154,3.152018,-9.795186,-0.398802,-8.290665,0.325927,7.251965,1.912896,-1.562511,-7.411658,-0.779545,-9.346211],[3.092161,-0.381454,0.451260,-1.721210,5.210631,4.261449,-1.859959,6.152534,-1.460121,-0.465737,-8.535755,-1.128440,9.514183,9.973888,-9.870770,6.334143],[5.602949,-9.023827,5.083134,-2.152283,-8.544980,-7.220843,0.890488,-0.134208,-8.010572,7.124301,-4.150329,-9.130973,6.453192,5.108855,5.352545,4.880601],[-6.993394,-7.882017,1.893795,-3.079077,-0.991108,-4.824766,6.574920,6.024019,5.887796,-5.418555,-7.097424,6.001613,-6.393241,0.807548,3.429376,-6.225268],[4.950159,3.595129,0.156250,-8.839652,7.629743,-8.109958,1.439521,-5.521940,-4.607543,0.803743,3.362927,-1.737007,8.768605,-2.422147,0.650342,8.729622],[3.291808,6.261889,-6.941023,-4.443304,-8.452942,-2.724271,-1.772490,-3.627346,-5.210927,-1.765982,-7.214841,0.608680,-8.287238,-8.922899,8.784868,-2.908058],[4.869961,8.743929,-7.104560,4.385574,-3.560862,-7.488678,-3.477227,-2.016569,-4.495546,8.774605,8.224949,2.342032,-8.803381,1.596157,8.360573,-8.705512],[1.489961,-2.735496,7.328347,-4.141054,-4.755273,-1.494984,2.065954,5.275973,1.186808,-0.401614,3.124869,7.747037,-6.956791,8.438706,-2.953212,-0.540587],[-8.813858,1.504087,-5.931565,2.076336,3.896748,3.001618,-5.174785,-6.827107,8.127260,9.416666,-2.930129,-2.122436,8.766134,-8.460017,5.630942,-9.828755],[-3.212802,1.840845,7.365671,0.298514,6.479904,-5.324796,4.324859,1.936568,7.951675,8.894447,0.186436,-1.275549,-9.407267,8.414419,8.338707,0.082021],[2.952874,-3.263644,0.192261,8.358768,9.192905,0.566603,6.129762,4.593815,1.863894,-1.012386,5.776219,7.270936,-0.493885,7.435622,-7.054747,4.255150]],[[-0.432140,8.061758,6.800947,-5.410209,-0.939155,3.052062,-0.320109,-1.284848,7.967329,8.241771,-6.200727,-9.626678,9.271836,-9.273456,-9.911230,7.244900],[-2.139203,9.846474,-1.449230,-5.329952,5.637128,-9.961071,-3.098021,8.521117,8.845272,-4.689312,7.365116,-9.632929,9.075050,9.106546,-4.585509,-5.460819],[7.582746,-7.217051,3.508891,-7.638833,-2.195619,-5.643839,1.452058,5.725355,-2.095009,-6.166306,-5.315827,-0.350711,-3.614689,-2.471891,6.930982,2.490722],[-3.795788,-4.730732,-5.302040,-2.272643,0.151366,9.416817,-1.099986,6.533918,5.639384,-5.449194,9.276013,5.040491,-1.743046,-4.467011,-5.085848,-7.917326],[-2.514645,-2.189946,9.249331,1.495686,8.261384,-1.658428,2.493786,3.982490,7.650312,0.901328,-6.496923,-9.168702,-4.154471,-0.209916,-4.916915,8.159650],[6.408127,4.542388,-6.331847,9.025501,-4.558264,5.166183,-4.651833,-2.360949,-8.271976,-3.857732,-9.966068,-5.914946,2.156872,3.633768,7.320300,-4.333624],[-2.795646,-7.840244,6.356385,-6.099985,5.806611,4.502200,-6.265247,1.397357,1.321248,-6.942731,2.543219,-1.274133,5.717036,-0.589374,-4.699719,-5.018138],[1.949762,9.050010,-0.890555,-6.219131,9.050766,3.456085,6.100691,5.786628,-6.022499,-0.927722,-2.996470,1.605758,-0.242717,-7.789112,-8.473288,8.125421],[8.779072,-9.933138,-2.661317,9.841847,5.099267,-3.356403,-8.977157,2.413142,2.095777,-0.879369,6.850404,5.272589,7.404448,-0.528379,-4.551106,4.587251],[8.752685,-8.140542,-9.569389,1.841539,-3.253448,-7.698997,2.860725,-6.056697,2.737567,-4.829037,-0.832778,-2.993968,-4.219324,9.384387,-9.397392,-3.229459],[9.826500,-0.652195,8.949199,2.067910,2.369720,-3.998659,7.327678,0.191027,3.000285,1.245131,5.542731,1.391645,8.844650,2.874550,-5.056128,4.444530],[-3.433930,4.515893,1.626047,8.073510,1.399682,-9.914139,-6.217499,0.249417,8.093163,0.666338,3.988039,-2.244558,-4.280426,-7.232504,-9.478657,-3.779332],[3.645469,-6.362986,-8.067145,4.890049,4.217797,-0.138403,8.132685,9.748029,0.149278,-1.012060,3.149011,9.193059,-4.415655,-2.626715,4.339906,4.382548]],[[6.881129,0.439276,5.353181,8.113091,-2.758659,2.391538,5.062496,1.911324,7.739983,7.370011,-3.154055,-9.082885,5.457073,4.094022,9.290193,4.879088],[-7.004586,-5.673377,-8.135701,-6.723517,-7.718010,-3.845717,-7.859006,-3.231532,5.476702,6.770049,-9.207302,-2.031226,-4.684521,-7.125460,-9.710376,-9.625220],[-3.967136,3.684999,-0.626167,-7.499088,0.253831,7.502056,-0.432587,5.485510,4.714117,6.993135,4.214371,5.317971,-4.214426,0.904071,-3.407125,4.975735],[3.087886,0.344424,5.439144,-1.327941,-8.867748,-4.508283,1.923599,6.779698,-7.516116,-9.316676,-0.569081,-8.357417,3.491413,-6.789812,9.952363,-8.720396],[-3.629237,9.852784,5.651025,-4.389196,8.343360,-2.396313,-8.551777,0.476665,1.556492,-6.954036,-1.711569,-2.237359,2.655178,3.142848,-7.813348,6.611663],[6.052430,-6.373347,-0.396003,-2.895310,-0.655285,-4.920637,-0.635231,8.408508,8.135434,-2.495153,-7.508272,1.700400,0.136173,6.032861,-6.574467,-6.971364],[8.668517,4.163049,5.460530,1.210450,-9.105460,-6.367284,3.458965,-3.419868,-3.022161,-0.707108,2.047822,-6.866716,-4.331063,0.617899,-7.398426,-4.487067],[-9.091572,9.104803,-2.827383,3.631335,-1.007076,5.475061,-1.993610,-0.140569,-5.539284,4.365448,-2.054799,-2.668154,5.449925,1.030199,7.556541,7.136849],[7.883893,4.483315,2.415409,1.856450,7.746413,-3.873194,-9.407978,-2.746553,4.296493,1.923650,4.216413,0.511139,9.003236,-4.423189,-0.816680,-1.116886],[-7.114643,8.814617,0.746554,0.204934,-3.490948,-5.841699,-5.106335,6.529584,-3.522358,0.490656,0.569497,8.421365,8.352172,6.913459,5.135557,-7.260048],[-6.145925,-4.366004,-7.812292,-9.323032,2.415449,6.978332,5.322219,1.635867,1.462962,4.584865,8.923898,5.018329,-5.698609,3.563685,0.541021,8.890703],[2.263530,6.253207,9.569268,-5.807527,-2.459595,-0.644932,4.350052,4.348524,-1.120360,8.877405,9.659223,-5.271533,3.124878,-3.070315,8.856013,-6.986773],[9.881780,-7.611220,6.442055,0.754273,5.110575,1.430753,0.826678,8.686435,5.135459,-5.761081,-9.087758,-1.429363,-6.797105,-9.003613,-0.273608,-5.008012]],[[-2.589586,-1.917424,-2.967475,3.441825,4.472074,-1.633882,6.520755,-2.349128,-0.574604,-4.681760,-8.311470,-2.644611,5.901131,-0.581503,-4.403484,5.906899],[-3.689117,-3.453652,7.061626,-6.535431,0.555096,3.326648,-4.956250,0.651743,-7.559949,2.321655,4.435435,9.228773,-5.563961,-9.568006,3.966592,8.397514],[-5.373862,-2.993263,3.796026,-9.873763,6.792528,-0.013392,-1.843385,-0.391091,9.219495,1.115246,2.953642,2.087483,-0.393021,-6.775814,0.374631,9.245923],[-4.309638,6.841048,-2.844315,-5.118228,1.547577,-7.428250,-8.417662,7.237557,-3.312547,-4.629189,2.231305,-1.539938,-2.524697,1.828071,-6.532958,2.716713],[-7.662025,2.839890,-5.351884,-8.758283,-9.408020,7.652850,0.395090,-0.429116,3.490004,-7.698197,-3.127055,8.108020,2.075810,-9.677828,4.997430,-6.815191],[-3.781717,7.603335,1.397103,-5.486908,-0.991704,2.157362,-9.570339,0.252751,-2.822221,2.638982,-1.894137,4.546118,2.828488,-4.825911,7.344372,1.638813],[-0.551789,5.986432,-5.340402,6.280537,9.590978,9.361355,-4.891420,-9.411492,-8.794385,3.963267,-2.353588,-4.223479,-0.474482,-4.720716,-5.948083,8.531619],[-2.262248,-2.912462,-1.646898,8.224119,-8.232890,-6.284292,-5.219927,-2.934954,-8.870667,2.067833,-8.409769,-7.595807,-7.442798,8.595579,-9.438239,6.185787],[0.864134,-6.427125,8.387014,0.532571,-3.217219,-6.604331,-0.647301,1.359190,-2.744971,7.026717,-9.058964,6.077935,3.145183,1.784688,9.486483,-0.598999],[4.574979,5.336407,8.426675,-8.737256,-4.549999,-6.746089,0.244583,9.563135,-3.801447,4.585944,-4.946392,-3.882467,6.218512,-7.844859,-6.744050,5.304599],[8.135483,3.901530,6.600458,-1.867116,-5.400944,2.689465,-6.832395,-9.585744,4.297792,5.915155,-8.593248,7.459976,-8.056083,4.366520,6.179472,-0.146300],[3.317608,5.371676,6.962261,-9.846915,-8.019915,-0.019019,-5.301163,0.396368,-4.054602,4.864464,-9.176573,-7.989500,-6.774039,-7.533853,-0.043286,-0.348726],[-9.565927,-0.541808,9.455533,4.545849,-8.620593,-5.376197,-0.744272,4.601396,2.379578,-4.674341,9.755195,-3.422567,-4.918249,9.268431,2.304897,-6.073269]],[[6.550047,5.718870,9.552649,-7.724000,-6.017206,-8.015289,7.956017,1.744236,-7.381453,-2.383188,-2.172804,-2.704565,7.291690,0.451925,8.608312,-9.030856],[5.114581,-1.950289,5.546848,-8.383861,7.091053,-8.199715,-1.792607,6.929733,5.943094,2.403308,-7.453022,-8.831415,5.341019,-1.107453,4.090051,-1.933500],[7.542571,5.095414,4.366203,-5.956282,-4.850236,0.942973,9.072568,-4.424774,1.486722,-8.799280,4.567829,1.436154,9.267353,2.276945,1.821810,0.324317],[-7.640351,6.653380,-2.636176,4.475620,-4.656125,-2.803551,1.033340,3.483919,-5.944357,4.452557,-6.979956,-6.129674,-2.042818,9.564350,8.883365,-6.838812],[0.940130,-3.387547,-2.325726,3.059023,-1.698022,-8.836624,-5.958235,-8.202773,0.818193,-2.962289,9.011835,9.440043,-7.046452,9.887501,3.604657,-6.969089],[8.316429,6.530465,-5.640470,-8.090423,-3.113720,-1.391009,-9.616557,9.269007,-9.079302,-4.029253,-4.548576,-9.824988,-4.995831,8.175239,9.572043,-1.519241],[-6.195765,-1.556534,-7.156443,7.583692,0.862800,5.425712,2.540435,-3.762919,-5.070951,8.872777,-5.218142,-6.596886,6.113906,0.420505,5.918107,5.700915],[2.802764,-8.868617,-8.936610,-9.863541,1.152876,-6.339177,-3.468927,7.932560,9.616359,7.636110,-5.553035,-4.419145,4.230059,-6.619107,2.696054,-1.334381],[-8.552964,6.712497,5.840753,-5.077946,2.532197,4.037995,0.790761,4.331116,0.769426,3.309122,-3.137439,9.619918,5.219822,-2.868805,5.128304,8.772901],[8.576708,-7.644757,-4.340545,4.752350,0.532123,4.647254,9.422992,2.865230,5.690586,-0.988431,-2.302819,-2.596928,-4.401764,4.380356,1.059898,2.308323],[2.576328,3.275369,-7.694553,0.549632,0.416619,4.235842,5.264068,7.814468,1.468281,-5.116330,9.706210,6.716064,8.936767,9.857244,0.746874,9.719942],[1.253503,-6.226949,-3.989117,3.252361,-3.796789,-2.981249,-2.758959,-0.413765,-3.815231,8.952283,1.619478,0.518155,1.786358,-4.246216,0.112121,5.236454],[-7.340448,-7.602175,-5.348110,4.126910,-7.298192,-1.997080,0.873224,-3.264629,-1.899285,-6.858015,-8.487472,-2.470052,-5.042278,-0.384749,8.949591,-9.753259]]], dtype = "float64")#candidate|8085|(6, 13, 16)|const|float64
uop_8086 = relay.acosh(const_8085.astype('float64')) # shape=(6, 13, 16)
bop_8088 = relay.multiply(const_8085.astype('int8'), relay.reshape(uop_8086.astype('int8'), relay.shape_of(const_8085))) # shape=(6, 13, 16)
func_5224_call = mod.get_global_var('func_5224')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_8094 = func_5224_call()
call_8095 = func_5224_call()
func_2032_call = mod.get_global_var('func_2032')
func_2034_call = mutated_mod.get_global_var('func_2034')
call_8100 = relay.TupleGetItem(func_2032_call(), 1)
call_8101 = relay.TupleGetItem(func_2034_call(), 1)
output = relay.Tuple([bop_8088,call_8094,call_8100,])
output2 = relay.Tuple([bop_8088,call_8095,call_8101,])
func_8103 = relay.Function([], output)
mod['func_8103'] = func_8103
mod = relay.transform.InferType()(mod)
mutated_mod['func_8103'] = func_8103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8103_call = mutated_mod.get_global_var('func_8103')
call_8104 = func_8103_call()
output = call_8104
func_8105 = relay.Function([], output)
mutated_mod['func_8105'] = func_8105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7751_call = mod.get_global_var('func_7751')
func_7752_call = mutated_mod.get_global_var('func_7752')
call_8174 = func_7751_call()
call_8175 = func_7751_call()
output = call_8174
output2 = call_8175
func_8179 = relay.Function([], output)
mod['func_8179'] = func_8179
mod = relay.transform.InferType()(mod)
output = func_8179()
func_8180 = relay.Function([], output)
mutated_mod['func_8180'] = func_8180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mod.get_global_var('func_4208')
func_4210_call = mutated_mod.get_global_var('func_4210')
call_8181 = func_4208_call()
call_8182 = func_4208_call()
var_8183 = relay.var("var_8183", dtype = "bool", shape = (4, 12, 8))#candidate|8183|(4, 12, 8)|var|bool
bop_8184 = relay.bitwise_and(call_8181.astype('uint32'), relay.reshape(var_8183.astype('uint32'), relay.shape_of(call_8181))) # shape=(4, 12, 8)
bop_8187 = relay.bitwise_and(call_8182.astype('uint32'), relay.reshape(var_8183.astype('uint32'), relay.shape_of(call_8182))) # shape=(4, 12, 8)
output = relay.Tuple([bop_8184,])
output2 = relay.Tuple([bop_8187,])
func_8188 = relay.Function([var_8183,], output)
mod['func_8188'] = func_8188
mod = relay.transform.InferType()(mod)
mutated_mod['func_8188'] = func_8188
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8189 = relay.var("var_8189", dtype = "bool", shape = (4, 12, 8))#candidate|8189|(4, 12, 8)|var|bool
func_8188_call = mutated_mod.get_global_var('func_8188')
call_8190 = func_8188_call(var_8189)
output = call_8190
func_8191 = relay.Function([var_8189], output)
mutated_mod['func_8191'] = func_8191
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8213 = relay.const(-6.410210, dtype = "float32")#candidate|8213|()|const|float32
var_8214 = relay.var("var_8214", dtype = "float32", shape = (14, 13, 6))#candidate|8214|(14, 13, 6)|var|float32
bop_8215 = relay.floor_divide(const_8213.astype('float32'), var_8214.astype('float32')) # shape=(14, 13, 6)
func_6222_call = mod.get_global_var('func_6222')
func_6223_call = mutated_mod.get_global_var('func_6223')
call_8235 = relay.TupleGetItem(func_6222_call(), 2)
call_8236 = relay.TupleGetItem(func_6223_call(), 2)
uop_8246 = relay.erf(call_8235.astype('float64')) # shape=(4, 48)
uop_8248 = relay.erf(call_8236.astype('float64')) # shape=(4, 48)
uop_8253 = relay.exp(bop_8215.astype('float32')) # shape=(14, 13, 6)
func_5185_call = mod.get_global_var('func_5185')
func_5186_call = mutated_mod.get_global_var('func_5186')
call_8258 = func_5185_call()
call_8259 = func_5185_call()
uop_8269 = relay.log10(var_8214.astype('float32')) # shape=(14, 13, 6)
uop_8271 = relay.atan(uop_8246.astype('float64')) # shape=(4, 48)
uop_8273 = relay.atan(uop_8248.astype('float64')) # shape=(4, 48)
var_8274 = relay.var("var_8274", dtype = "float64", shape = (4, 48))#candidate|8274|(4, 48)|var|float64
bop_8275 = relay.minimum(uop_8271.astype('float32'), relay.reshape(var_8274.astype('float32'), relay.shape_of(uop_8271))) # shape=(4, 48)
bop_8278 = relay.minimum(uop_8273.astype('float32'), relay.reshape(var_8274.astype('float32'), relay.shape_of(uop_8273))) # shape=(4, 48)
func_2826_call = mod.get_global_var('func_2826')
func_2828_call = mutated_mod.get_global_var('func_2828')
call_8284 = relay.TupleGetItem(func_2826_call(), 0)
call_8285 = relay.TupleGetItem(func_2828_call(), 0)
bop_8293 = relay.logical_and(uop_8246.astype('bool'), relay.reshape(bop_8275.astype('bool'), relay.shape_of(uop_8246))) # shape=(4, 48)
bop_8296 = relay.logical_and(uop_8248.astype('bool'), relay.reshape(bop_8278.astype('bool'), relay.shape_of(uop_8248))) # shape=(4, 48)
bop_8300 = relay.mod(uop_8246.astype('float64'), relay.reshape(bop_8293.astype('float64'), relay.shape_of(uop_8246))) # shape=(4, 48)
bop_8303 = relay.mod(uop_8248.astype('float64'), relay.reshape(bop_8296.astype('float64'), relay.shape_of(uop_8248))) # shape=(4, 48)
output = relay.Tuple([uop_8253,call_8258,uop_8269,call_8284,bop_8300,])
output2 = relay.Tuple([uop_8253,call_8259,uop_8269,call_8285,bop_8303,])
func_8316 = relay.Function([var_8214,var_8274,], output)
mod['func_8316'] = func_8316
mod = relay.transform.InferType()(mod)
var_8317 = relay.var("var_8317", dtype = "float32", shape = (14, 13, 6))#candidate|8317|(14, 13, 6)|var|float32
var_8318 = relay.var("var_8318", dtype = "float64", shape = (4, 48))#candidate|8318|(4, 48)|var|float64
output = func_8316(var_8317,var_8318,)
func_8319 = relay.Function([var_8317,var_8318,], output)
mutated_mod['func_8319'] = func_8319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5162_call = mod.get_global_var('func_5162')
func_5163_call = mutated_mod.get_global_var('func_5163')
call_8346 = relay.TupleGetItem(func_5162_call(), 0)
call_8347 = relay.TupleGetItem(func_5163_call(), 0)
func_973_call = mod.get_global_var('func_973')
func_975_call = mutated_mod.get_global_var('func_975')
call_8362 = relay.TupleGetItem(func_973_call(), 3)
call_8363 = relay.TupleGetItem(func_975_call(), 3)
uop_8368 = relay.acosh(call_8362.astype('float64')) # shape=(4, 12, 8)
uop_8370 = relay.acosh(call_8363.astype('float64')) # shape=(4, 12, 8)
func_4106_call = mod.get_global_var('func_4106')
func_4109_call = mutated_mod.get_global_var('func_4109')
var_8393 = relay.var("var_8393", dtype = "int64", shape = (168,))#candidate|8393|(168,)|var|int64
call_8392 = relay.TupleGetItem(func_4106_call(relay.reshape(var_8393.astype('int64'), [168,])), 3)
call_8394 = relay.TupleGetItem(func_4109_call(relay.reshape(var_8393.astype('int64'), [168,])), 3)
uop_8419 = relay.asin(uop_8368.astype('float32')) # shape=(4, 12, 8)
uop_8421 = relay.asin(uop_8370.astype('float32')) # shape=(4, 12, 8)
func_1760_call = mod.get_global_var('func_1760')
func_1763_call = mutated_mod.get_global_var('func_1763')
call_8455 = relay.TupleGetItem(func_1760_call(relay.reshape(call_8392.astype('int64'), [192,])), 2)
call_8456 = relay.TupleGetItem(func_1763_call(relay.reshape(call_8392.astype('int64'), [192,])), 2)
func_6946_call = mod.get_global_var('func_6946')
func_6950_call = mutated_mod.get_global_var('func_6950')
var_8461 = relay.var("var_8461", dtype = "uint32", shape = (52, 4))#candidate|8461|(52, 4)|var|uint32
call_8460 = relay.TupleGetItem(func_6946_call(relay.reshape(var_8461.astype('uint32'), [8, 2, 13]), relay.reshape(var_8461.astype('uint32'), [8, 2, 13]), ), 0)
call_8462 = relay.TupleGetItem(func_6950_call(relay.reshape(var_8461.astype('uint32'), [8, 2, 13]), relay.reshape(var_8461.astype('uint32'), [8, 2, 13]), ), 0)
output = relay.Tuple([call_8346,call_8392,var_8393,uop_8419,call_8455,call_8460,var_8461,])
output2 = relay.Tuple([call_8347,call_8394,var_8393,uop_8421,call_8456,call_8462,var_8461,])
func_8463 = relay.Function([var_8393,var_8461,], output)
mod['func_8463'] = func_8463
mod = relay.transform.InferType()(mod)
mutated_mod['func_8463'] = func_8463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8463_call = mutated_mod.get_global_var('func_8463')
var_8465 = relay.var("var_8465", dtype = "int64", shape = (168,))#candidate|8465|(168,)|var|int64
var_8466 = relay.var("var_8466", dtype = "uint32", shape = (52, 4))#candidate|8466|(52, 4)|var|uint32
call_8464 = func_8463_call(var_8465,var_8466,)
output = call_8464
func_8467 = relay.Function([var_8465,var_8466,], output)
mutated_mod['func_8467'] = func_8467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7301_call = mod.get_global_var('func_7301')
func_7303_call = mutated_mod.get_global_var('func_7303')
call_8493 = relay.TupleGetItem(func_7301_call(), 5)
call_8494 = relay.TupleGetItem(func_7303_call(), 5)
uop_8506 = relay.asin(call_8493.astype('float32')) # shape=(105, 3)
uop_8508 = relay.asin(call_8494.astype('float32')) # shape=(105, 3)
bop_8515 = relay.greater_equal(uop_8506.astype('bool'), relay.reshape(call_8493.astype('bool'), relay.shape_of(uop_8506))) # shape=(105, 3)
bop_8518 = relay.greater_equal(uop_8508.astype('bool'), relay.reshape(call_8494.astype('bool'), relay.shape_of(uop_8508))) # shape=(105, 3)
uop_8520 = relay.log2(bop_8515.astype('float64')) # shape=(105, 3)
uop_8522 = relay.log2(bop_8518.astype('float64')) # shape=(105, 3)
bop_8525 = relay.mod(uop_8520.astype('float32'), relay.reshape(uop_8506.astype('float32'), relay.shape_of(uop_8520))) # shape=(105, 3)
bop_8528 = relay.mod(uop_8522.astype('float32'), relay.reshape(uop_8508.astype('float32'), relay.shape_of(uop_8522))) # shape=(105, 3)
func_5671_call = mod.get_global_var('func_5671')
func_5675_call = mutated_mod.get_global_var('func_5675')
var_8530 = relay.var("var_8530", dtype = "float32", shape = (56, 16))#candidate|8530|(56, 16)|var|float32
const_8531 = relay.const([-7,4,6,10,-7,-1,8,5,4,4,7,6,10,-1,10,-2,2,9,-2,-10,-10,9,-6,7,-2,-2,2,-2,-9,-3,-8,7], dtype = "uint64")#candidate|8531|(32,)|const|uint64
const_8532 = relay.const([-10,7,-3,10,-6,-8,6,3,6,-7,10,-3,6,9,3,-1,8,-10,-4,5,-7,-2,1,-3,1,-9,-6,5,4,-7,-8,2,4,-7,4,-8,-4,-6,-6,-6,-8,9,7,-8,-1,-10,1,5,3,6,5,-10,4,8,2,-8,-10,6,4,10,7,4,-1,-7,-2,-4,7,-8,10,5,-9,-4,-2,6,-2,-1,6,1,4,-4,1,3,-3,-2,-6,-3,-10,6,7,7,-8,-2,-6,4,1,6,7,1,-2,-1,10,7,-2,3,7,-9,-8,3,-4,-4,4,-6,-1,9,9,-6,-3,-10,-8,-4,-1,-1,-6,5,-1,4,10,4,-8,-9,-2,-8,7,-2,9,1,-9,-2,-9,4,7,5,9,-3,4,-3,-6,-3,-9,10,-1,9,-3,6,10,-2,-7,6,-6,-2,-10,7,6,-3,-7,2,-1,-1,-3,-8,6,-10,5,-8,7,-1,6,7,10,-8,10,-8,-2,9,3,-8,5,1,-8,-1,2,3], dtype = "int64")#candidate|8532|(192,)|const|int64
call_8529 = relay.TupleGetItem(func_5671_call(relay.reshape(var_8530.astype('float32'), [2, 448]), relay.reshape(const_8531.astype('uint64'), [32,]), relay.reshape(const_8532.astype('int64'), [192,]), ), 1)
call_8533 = relay.TupleGetItem(func_5675_call(relay.reshape(var_8530.astype('float32'), [2, 448]), relay.reshape(const_8531.astype('uint64'), [32,]), relay.reshape(const_8532.astype('int64'), [192,]), ), 1)
func_4442_call = mod.get_global_var('func_4442')
func_4443_call = mutated_mod.get_global_var('func_4443')
call_8535 = relay.TupleGetItem(func_4442_call(), 0)
call_8536 = relay.TupleGetItem(func_4443_call(), 0)
const_8539 = relay.const([[9.410287,3.170915,7.656956],[-6.992429,-2.257271,8.446455],[8.583687,0.141707,-5.809783],[-9.293300,8.324960,9.103183],[-6.473172,-7.382786,7.455178],[4.746593,6.452306,-4.496065],[-2.165814,-6.337935,-7.102705],[3.143818,-9.109125,3.489214],[1.956582,6.045345,-2.048498],[-0.315031,1.846117,-5.637457],[-2.213340,5.012059,-7.644494],[5.783996,8.704816,2.660609],[1.053213,3.171545,0.287320],[-3.515734,-3.783516,9.352908],[-3.547907,-7.755054,2.196113],[-8.998003,-6.271545,5.458762],[6.508794,5.761920,-2.969773],[-8.471966,-1.713275,8.648901],[-9.700592,-7.617302,6.823968],[9.247087,0.258088,8.719106],[-3.395165,9.984353,-3.495636],[2.931277,0.710365,-5.964890],[3.158326,2.035766,-9.935210],[6.501008,1.966025,-7.534581],[-8.509301,-1.044219,8.304766],[-3.990305,-0.730358,-2.733112],[-6.636075,-3.158158,-9.400713],[3.996586,-5.087567,9.748402],[3.082668,0.334091,-1.959571],[-0.748098,-1.149858,4.271821],[-8.833459,6.818962,4.896843],[0.253554,-0.566394,1.434371],[-5.907891,-1.259289,2.009475],[-6.347113,9.481685,0.144289],[9.958574,-8.070236,2.974755],[4.743237,4.540963,-0.912347],[-5.703744,-1.234928,2.203674],[5.554719,-9.681791,-5.853177],[-4.821786,-1.289363,6.045680],[5.152986,1.401954,-6.998800],[2.238909,9.570770,-7.612088],[4.395971,3.537358,9.187805],[6.887644,0.356071,2.138551],[-9.632636,-1.216603,3.935704],[-1.892000,-8.580474,-3.126118],[-7.789816,-5.216950,-2.360245],[2.827403,0.499559,7.347997],[-3.879670,8.889302,-8.922753],[4.808334,-5.633852,0.840984],[8.293981,8.745109,-6.326685],[-5.537831,1.035233,-7.487876],[-1.218029,-1.072860,-7.757611],[-1.417305,-9.399393,-7.246058],[-2.309090,6.193883,2.194004],[-0.585447,0.134365,-3.921570],[9.985927,-2.844194,5.243540],[-0.014279,5.395195,6.364906],[-7.384930,-1.092163,-5.796219],[0.381692,-0.389670,8.138473],[-8.784354,6.787860,1.330883],[8.995479,-5.508698,-3.182960],[-4.672339,8.923190,9.604094],[6.813510,1.812116,-1.079021],[9.213438,-8.359797,8.584609],[9.733216,-6.906237,3.227055],[2.267884,-4.720691,-0.323408],[8.333207,-6.019143,-1.768436],[-7.451662,9.537380,1.175505],[4.369559,-5.682827,5.856761],[8.037073,4.688312,2.028736],[-4.906812,7.105749,-4.751926],[2.770293,-7.606067,0.894424],[2.254156,-3.182420,6.119705],[-3.762817,-9.016795,-0.947659],[-6.116617,9.305145,6.551287],[-9.235017,3.140349,3.810609],[-3.276102,1.484843,-7.473151],[0.461437,-1.644919,-9.942000],[-4.720182,-0.035892,0.595008],[-5.227040,3.683131,5.782292],[-1.836692,-1.437013,3.647037],[1.524609,-1.346562,-9.828772],[2.971824,-7.236239,-1.374082],[4.418699,1.900754,9.632793],[7.625173,0.789686,6.466914],[4.132801,-1.672076,6.679593],[1.231094,1.026404,-9.421373],[-9.246545,-3.687823,4.576906],[-6.594342,9.010717,3.166382],[-2.380481,-5.102920,3.667217],[7.615814,4.707568,-6.614601],[5.230486,5.544694,8.390413],[0.867229,-5.225691,-6.503948],[-4.910140,-2.916903,-5.974821],[-9.392880,-7.224318,-5.208343],[4.283829,1.104989,-5.562234],[3.271249,1.062500,-3.285248],[-1.332228,9.025887,9.486535],[5.312695,-8.876294,9.958464],[4.510236,6.247747,-3.585072],[3.290851,3.966218,-6.151290],[-5.435621,-3.665669,6.434643],[-6.316390,-1.644514,-8.365594],[1.236860,1.679151,9.666084],[-2.622738,-1.959932,4.625692]], dtype = "float64")#candidate|8539|(105, 3)|const|float64
bop_8540 = relay.equal(uop_8520.astype('bool'), relay.reshape(const_8539.astype('bool'), relay.shape_of(uop_8520))) # shape=(105, 3)
bop_8543 = relay.equal(uop_8522.astype('bool'), relay.reshape(const_8539.astype('bool'), relay.shape_of(uop_8522))) # shape=(105, 3)
bop_8545 = relay.less(uop_8506.astype('bool'), relay.reshape(bop_8515.astype('bool'), relay.shape_of(uop_8506))) # shape=(105, 3)
bop_8548 = relay.less(uop_8508.astype('bool'), relay.reshape(bop_8518.astype('bool'), relay.shape_of(uop_8508))) # shape=(105, 3)
uop_8549 = relay.asinh(bop_8525.astype('float64')) # shape=(105, 3)
uop_8551 = relay.asinh(bop_8528.astype('float64')) # shape=(105, 3)
bop_8571 = relay.maximum(bop_8525.astype('float64'), relay.reshape(bop_8540.astype('float64'), relay.shape_of(bop_8525))) # shape=(105, 3)
bop_8574 = relay.maximum(bop_8528.astype('float64'), relay.reshape(bop_8543.astype('float64'), relay.shape_of(bop_8528))) # shape=(105, 3)
func_555_call = mod.get_global_var('func_555')
func_558_call = mutated_mod.get_global_var('func_558')
call_8578 = relay.TupleGetItem(func_555_call(relay.reshape(const_8532.astype('int64'), [4, 12, 4])), 1)
call_8579 = relay.TupleGetItem(func_558_call(relay.reshape(const_8532.astype('int64'), [4, 12, 4])), 1)
func_7498_call = mod.get_global_var('func_7498')
func_7499_call = mutated_mod.get_global_var('func_7499')
call_8582 = relay.TupleGetItem(func_7498_call(), 1)
call_8583 = relay.TupleGetItem(func_7499_call(), 1)
uop_8589 = relay.sigmoid(uop_8549.astype('float64')) # shape=(105, 3)
uop_8591 = relay.sigmoid(uop_8551.astype('float64')) # shape=(105, 3)
bop_8594 = relay.greater(uop_8589.astype('bool'), relay.reshape(bop_8525.astype('bool'), relay.shape_of(uop_8589))) # shape=(105, 3)
bop_8597 = relay.greater(uop_8591.astype('bool'), relay.reshape(bop_8528.astype('bool'), relay.shape_of(uop_8591))) # shape=(105, 3)
bop_8604 = relay.not_equal(bop_8545.astype('bool'), relay.reshape(bop_8525.astype('bool'), relay.shape_of(bop_8545))) # shape=(105, 3)
bop_8607 = relay.not_equal(bop_8548.astype('bool'), relay.reshape(bop_8528.astype('bool'), relay.shape_of(bop_8548))) # shape=(105, 3)
output = relay.Tuple([call_8529,var_8530,const_8531,const_8532,call_8535,bop_8571,call_8578,call_8582,bop_8594,bop_8604,])
output2 = relay.Tuple([call_8533,var_8530,const_8531,const_8532,call_8536,bop_8574,call_8579,call_8583,bop_8597,bop_8607,])
F = relay.Function([var_8530,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8530,], output2)
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
