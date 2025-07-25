import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_35 = relay.var("var_35", dtype = "float32", shape = ())#candidate|35|()|var|float32
var_36 = relay.var("var_36", dtype = "float32", shape = (7, 10, 5))#candidate|36|(7, 10, 5)|var|float32
bop_37 = relay.mod(var_35.astype('float32'), var_36.astype('float32')) # shape=(7, 10, 5)
output = bop_37
output2 = bop_37
func_49 = relay.Function([var_35,var_36,], output)
mod['func_49'] = func_49
mod = relay.transform.InferType()(mod)
mutated_mod['func_49'] = func_49
mutated_mod = relay.transform.InferType()(mutated_mod)
func_49_call = mutated_mod.get_global_var('func_49')
var_51 = relay.var("var_51", dtype = "float32", shape = ())#candidate|51|()|var|float32
var_52 = relay.var("var_52", dtype = "float32", shape = (7, 10, 5))#candidate|52|(7, 10, 5)|var|float32
call_50 = func_49_call(var_51,var_52,)
output = call_50
func_53 = relay.Function([var_51,var_52,], output)
mutated_mod['func_53'] = func_53
mutated_mod = relay.transform.InferType()(mutated_mod)
var_229 = relay.var("var_229", dtype = "uint64", shape = (13, 3, 10))#candidate|229|(13, 3, 10)|var|uint64
const_230 = relay.const([[[2,-1,5,7,-7,8,2,-10,8,-7],[5,10,6,-9,4,-6,-3,5,-1,10],[5,-9,-7,-4,-6,8,2,1,1,9]],[[-1,4,-2,-2,3,-10,-3,5,-10,5],[-2,7,2,-4,-8,-10,7,-3,-5,3],[-10,-6,4,2,-2,9,-9,-8,6,6]],[[4,-5,10,-2,-4,2,-10,8,2,9],[9,8,6,-1,-7,-8,-2,3,-10,8],[-2,9,-1,-9,9,6,7,5,1,6]],[[4,-10,5,-10,-10,9,1,7,5,6],[1,-1,8,-2,2,9,-1,4,-2,-3],[5,6,9,9,-7,-7,6,9,-4,7]],[[10,-3,4,-9,2,-1,-1,4,-10,6],[-7,-8,-3,-9,9,-2,-1,-9,10,1],[9,10,1,-2,4,-8,10,-6,-6,-9]],[[-10,-3,-6,5,-2,10,10,-1,-4,2],[10,-1,-8,5,-1,-7,7,-1,4,-1],[-4,-8,-2,5,-4,6,-7,-8,3,8]],[[-10,-4,-7,-2,-2,-9,-3,-3,8,3],[-5,9,7,8,3,-5,-1,9,-5,-10],[3,5,6,5,8,-7,-8,-6,4,-6]],[[-9,9,9,9,1,2,9,-2,-7,-1],[2,9,-6,4,8,4,-10,-9,-1,2],[6,-5,-1,-1,3,-3,-4,6,9,10]],[[9,-7,9,9,-2,3,5,4,5,6],[1,-3,-2,-5,-9,8,-10,-1,1,-8],[-1,3,-9,3,6,3,9,-4,-5,1]],[[3,3,6,-2,-4,-2,-1,8,-3,5],[-10,-9,-4,-9,-2,-4,2,10,-1,-7],[-5,7,-5,8,-8,9,3,7,3,-6]],[[-6,1,8,-10,-6,-6,-7,8,10,1],[-1,7,10,-1,10,7,-10,6,10,8],[2,-6,7,-10,-10,-6,-3,4,9,-6]],[[5,-6,2,2,9,-9,-4,-1,-10,9],[-4,-2,-9,10,-6,-8,-2,5,-8,7],[8,10,2,2,-2,6,5,-1,-6,6]],[[-9,-2,-1,-6,-3,8,-10,3,10,6],[6,6,-9,8,9,-9,8,-9,8,10],[8,-5,8,2,3,10,9,-1,-4,-6]]], dtype = "uint64")#candidate|230|(13, 3, 10)|const|uint64
bop_231 = relay.logical_xor(var_229.astype('uint64'), relay.reshape(const_230.astype('uint64'), relay.shape_of(var_229))) # shape=(13, 3, 10)
output = relay.Tuple([bop_231,])
output2 = relay.Tuple([bop_231,])
func_239 = relay.Function([var_229,], output)
mod['func_239'] = func_239
mod = relay.transform.InferType()(mod)
mutated_mod['func_239'] = func_239
mutated_mod = relay.transform.InferType()(mutated_mod)
var_240 = relay.var("var_240", dtype = "uint64", shape = (13, 3, 10))#candidate|240|(13, 3, 10)|var|uint64
func_239_call = mutated_mod.get_global_var('func_239')
call_241 = func_239_call(var_240)
output = call_241
func_242 = relay.Function([var_240], output)
mutated_mod['func_242'] = func_242
mutated_mod = relay.transform.InferType()(mutated_mod)
const_325 = relay.const([[[3.522857,-2.755528,-8.421383,-0.841525],[6.936618,-4.525644,-3.934292,-1.211027],[-7.347948,5.835414,1.941892,-2.376874],[7.893366,7.210150,-1.960973,8.430751],[-5.783113,-2.680413,1.346034,6.858186],[2.211421,-7.351277,4.996571,-6.484791],[0.601900,7.140483,0.523201,3.401422],[9.000978,4.874571,-0.625397,-8.025222],[-9.543535,9.311248,8.296616,-5.629286],[-9.871313,-2.156219,-5.990804,8.843956],[-6.107741,-9.550615,0.996640,-1.222317],[5.393620,-7.335450,-0.085934,-4.142050],[-1.110549,2.887686,-0.167561,-0.774615],[-0.298297,0.926230,1.980129,-3.985393],[7.294621,-7.856312,1.644133,-3.421618]],[[-9.272645,-7.306719,6.739693,7.203449],[-5.851858,4.738861,-0.238801,-4.301397],[-1.237833,4.198615,-0.012784,6.383812],[2.630641,-2.344846,-8.467454,0.593107],[-5.615749,4.469976,-3.999000,0.411930],[7.473339,5.966049,-0.459081,-8.639020],[9.975426,9.296228,-6.065988,-3.110089],[-6.812035,-2.627343,8.004526,5.863048],[4.870710,7.184996,6.532247,-5.677674],[8.409165,-5.874943,5.726966,-7.815023],[3.436204,1.392410,-5.076732,6.773527],[-5.551007,1.921306,4.023284,6.675561],[8.197010,-7.439943,9.631527,-8.123107],[-3.644020,3.067954,6.248525,6.692083],[9.307385,-3.163973,-3.583930,-7.592076]],[[5.021647,-4.723679,-5.534859,8.089551],[-2.326531,-5.529154,2.071006,-0.023282],[3.750607,9.721702,6.971332,2.494433],[8.592858,-5.857129,6.066341,3.749390],[-9.256685,6.674421,0.331041,-2.659760],[-9.480004,-3.608657,6.468924,-8.270679],[-9.623956,-5.924514,-0.048102,-7.404741],[0.339237,3.319885,6.897356,-7.142585],[-0.298459,-8.473656,-6.624470,4.039110],[2.695273,-7.468666,-5.374536,1.811386],[0.473982,-1.497931,-5.035555,5.217967],[7.222460,-9.776083,9.058275,-7.968289],[6.654929,-5.530596,1.417659,-2.882563],[8.624295,-7.649998,3.945929,-6.192744],[5.207049,-2.684673,3.909117,4.487516]],[[-1.419303,6.951600,-2.943940,1.976521],[-9.638402,-9.366371,2.919012,-8.104281],[3.291347,-3.165027,-8.030050,0.108379],[2.631798,7.455307,-2.061630,9.808928],[2.202162,-3.570851,-7.965678,5.625597],[2.422592,2.660462,-7.690964,0.138184],[-3.180261,4.140239,-3.737953,-5.924621],[-4.239643,-3.468122,-8.771163,-3.286858],[-9.111542,-3.846705,-7.177119,5.632937],[7.122223,0.198669,-3.556583,6.712372],[-4.957023,-5.928371,-2.878874,1.924854],[-2.073190,4.502062,8.864586,-4.425492],[-9.941487,7.383688,-4.482570,8.052287],[8.869767,-3.860403,0.171552,-5.893979],[-8.563118,9.509330,7.792179,4.731347]],[[-0.076553,-7.438493,-0.864517,-1.757366],[6.600560,-2.674307,-1.508464,3.844008],[-2.345555,-8.384716,-8.561600,8.205944],[3.281638,3.711740,5.571306,-6.008804],[6.893841,-8.845806,-4.042645,-9.745742],[-4.731957,3.823208,-0.686620,-5.592685],[-0.348674,2.531449,4.737775,1.296809],[1.140317,3.614288,-4.875814,-2.129978],[-3.710900,8.525989,2.535110,5.177702],[-3.400582,4.696571,2.268368,5.004982],[-6.037445,-2.826773,-8.500189,-4.605030],[-0.685920,-0.472483,0.419698,-1.739309],[4.081958,-4.277766,-5.583642,-0.642508],[7.975479,5.073186,1.086801,-4.766785],[6.156829,4.930760,4.165555,9.091637]],[[4.078446,-2.145705,4.845969,2.514247],[-4.784895,5.710312,0.159470,-7.932398],[8.262571,4.696420,-3.225162,-9.082978],[4.291241,6.713496,4.892502,-8.942316],[3.995611,-6.855425,-1.929632,6.424311],[1.399176,9.328142,7.684771,3.744455],[1.451345,0.872154,6.736082,-0.734535],[-2.061190,1.704475,-8.699910,-5.001769],[-2.083590,-1.619140,-4.024572,4.839931],[2.490712,-0.545771,-1.030361,9.365660],[6.187433,-1.120980,5.546442,6.402813],[-9.101650,1.740470,-1.177058,-6.556088],[-7.106168,6.871135,4.485976,8.769747],[1.991192,7.758035,2.798347,-2.024744],[8.340156,4.069913,6.984516,-0.897391]],[[5.450100,-0.301062,-7.546888,-0.468612],[-6.942303,4.786603,8.592008,-7.300922],[4.274789,-5.010273,-2.486980,1.506100],[0.100278,-6.892708,4.743387,8.390703],[5.094239,-3.225469,-4.300094,-1.069602],[4.061489,-2.749487,-1.498146,4.245728],[-4.997137,8.418581,-2.862151,2.162663],[3.355584,-6.513283,-0.251964,-0.236233],[-7.718736,7.718420,7.683394,8.750112],[-3.489582,5.034284,-3.630576,-4.624882],[7.753963,3.021667,-9.171788,1.637285],[3.171819,-8.364395,8.934345,6.643544],[0.451588,1.197826,-0.707032,8.383661],[-1.729709,-7.829784,-2.473709,-6.230396],[-1.892266,9.756835,-5.213721,-0.161781]],[[8.116548,8.381613,3.696674,-8.202417],[-2.666548,-6.094198,-8.740276,1.342323],[-2.031891,6.785145,-7.777779,-1.572119],[4.255119,2.995669,1.868161,9.841276],[-7.150010,7.478706,8.535819,-3.444724],[0.417769,2.772590,4.268295,5.644888],[-8.087851,-9.696258,-9.748309,1.559904],[-0.265797,7.564374,-6.496927,-5.054773],[7.820145,0.351112,6.251275,-3.459951],[-0.409979,-4.568242,-1.755529,7.259226],[-6.171141,9.849911,5.937095,0.586539],[4.204521,9.573011,1.692002,-5.689391],[6.663806,-9.784579,-0.218338,-8.016028],[-1.728351,-5.057240,-0.768593,3.102563],[7.987032,0.595081,4.991450,-9.156955]],[[5.619169,-4.187339,-3.075778,3.603183],[-2.812560,-2.763237,2.913401,1.133353],[-9.593209,-4.155010,-3.129601,5.126956],[9.794095,-4.745056,8.729748,9.812930],[-5.613857,-2.513966,7.165482,-6.155821],[6.961565,-9.903933,3.890043,-2.455862],[8.397271,-0.222827,-8.172270,2.780445],[-2.868919,-0.800594,-1.855961,-2.824213],[8.140275,8.033256,7.576469,7.469762],[1.127845,5.032850,4.951765,-9.102446],[-3.285478,-0.403120,-0.091514,-6.251521],[3.890255,5.430703,0.197300,-7.751542],[-6.796279,9.980152,-8.234931,-7.700736],[-4.861373,-4.133303,2.469876,-9.296285],[-3.970053,-6.388256,-5.516543,8.556590]]], dtype = "float64")#candidate|325|(9, 15, 4)|const|float64
uop_326 = relay.sigmoid(const_325.astype('float64')) # shape=(9, 15, 4)
output = uop_326
output2 = uop_326
func_328 = relay.Function([], output)
mod['func_328'] = func_328
mod = relay.transform.InferType()(mod)
mutated_mod['func_328'] = func_328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mutated_mod.get_global_var('func_328')
call_329 = func_328_call()
output = call_329
func_330 = relay.Function([], output)
mutated_mod['func_330'] = func_330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_341 = func_328_call()
call_342 = func_328_call()
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_344 = func_328_call()
call_345 = func_328_call()
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_355 = func_328_call()
call_356 = func_328_call()
output = relay.Tuple([call_341,call_344,call_355,])
output2 = relay.Tuple([call_342,call_345,call_356,])
func_357 = relay.Function([], output)
mod['func_357'] = func_357
mod = relay.transform.InferType()(mod)
output = func_357()
func_358 = relay.Function([], output)
mutated_mod['func_358'] = func_358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_374 = relay.TupleGetItem(func_357_call(), 0)
call_375 = relay.TupleGetItem(func_358_call(), 0)
output = call_374
output2 = call_375
func_384 = relay.Function([], output)
mod['func_384'] = func_384
mod = relay.transform.InferType()(mod)
mutated_mod['func_384'] = func_384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mutated_mod.get_global_var('func_384')
call_385 = func_384_call()
output = call_385
func_386 = relay.Function([], output)
mutated_mod['func_386'] = func_386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_422 = relay.TupleGetItem(func_357_call(), 2)
call_423 = relay.TupleGetItem(func_358_call(), 2)
output = call_422
output2 = call_423
func_427 = relay.Function([], output)
mod['func_427'] = func_427
mod = relay.transform.InferType()(mod)
mutated_mod['func_427'] = func_427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_427_call = mutated_mod.get_global_var('func_427')
call_428 = func_427_call()
output = call_428
func_429 = relay.Function([], output)
mutated_mod['func_429'] = func_429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_445 = func_384_call()
call_446 = func_384_call()
output = call_445
output2 = call_446
func_449 = relay.Function([], output)
mod['func_449'] = func_449
mod = relay.transform.InferType()(mod)
mutated_mod['func_449'] = func_449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mutated_mod.get_global_var('func_449')
call_450 = func_449_call()
output = call_450
func_451 = relay.Function([], output)
mutated_mod['func_451'] = func_451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_475 = relay.TupleGetItem(func_357_call(), 1)
call_476 = relay.TupleGetItem(func_358_call(), 1)
const_481 = relay.const([[[-2.035775,-7.529785,-3.420230,6.381801],[2.957105,-8.522906,0.733477,6.026077],[-5.210663,1.879889,-2.388465,-0.663131],[-9.696114,-5.273555,0.564026,-0.724481],[5.969774,-8.293776,9.727781,9.496136],[-3.891098,3.422301,-9.315724,3.259333],[-8.206269,9.832706,2.120430,-5.918875],[-0.209193,-9.424153,-9.909362,4.155798],[-7.355518,-9.486675,7.929631,-1.555290],[7.399018,-1.861798,-5.055276,-2.530851],[-1.673470,-1.590945,6.838047,8.391608],[9.490871,7.491286,-2.224759,-3.280018],[-8.395712,-0.685364,-1.678841,5.357750],[-9.287157,9.572675,-7.115558,-9.870717],[-6.247777,-6.569400,8.849451,5.378840]],[[2.837435,-8.160382,7.801555,-1.173225],[0.210293,-6.922048,3.239118,5.301331],[7.623256,5.366521,-3.577878,-4.870000],[-9.662833,-5.456036,-3.125880,-8.352139],[-3.222506,-4.146850,2.546285,4.506833],[9.531304,-3.764412,-1.225745,2.209548],[8.536898,8.356122,-1.018756,-6.824345],[-2.661677,-6.501589,-5.979527,-3.438044],[3.622353,-6.582638,-6.538434,-9.868701],[5.257848,-6.757563,-0.698624,3.979754],[-2.058689,-5.999227,-5.814250,0.685467],[4.903304,-8.655746,3.276235,3.998384],[0.205923,2.871585,6.926304,5.765042],[2.340727,-3.963554,9.852088,2.407450],[-2.508725,-4.678091,-5.995581,5.869174]],[[7.491639,6.454128,5.099582,-5.520934],[-5.393493,-1.713727,4.744435,5.558699],[3.664030,-0.445744,3.924260,0.310465],[0.327728,3.891221,8.893858,-4.878001],[-1.637725,6.960134,-5.939403,-5.532550],[-5.819848,-5.355919,-1.194270,-7.330714],[-5.148761,7.400664,-0.532444,3.574151],[-1.934355,8.121746,-1.043625,6.681677],[5.681303,-6.373978,-6.990805,-9.165919],[3.864817,-7.032018,-2.182277,7.100296],[4.259052,8.176231,2.338933,-6.773339],[6.351490,-3.889714,6.141761,-5.745034],[-5.502509,-0.113173,0.083015,4.825761],[9.857009,-4.330641,-2.751054,-0.540706],[-5.503762,9.089144,6.302598,-0.140029]],[[0.735701,-2.272183,-4.747085,4.996978],[2.357697,7.525649,8.831997,4.657198],[-5.712771,-4.975798,0.120030,-8.854682],[-8.389422,-6.961332,4.385981,-3.469880],[8.052031,9.993771,7.271215,-6.494774],[-0.093978,7.514860,0.683359,9.887200],[6.070659,-9.702229,-9.085208,-4.136098],[8.300331,-6.007088,3.605990,1.768470],[9.761742,-1.438972,-2.456248,5.745825],[-8.994711,-9.061679,7.307988,2.630896],[6.764688,-0.464999,1.167847,4.924954],[2.453133,7.560231,-3.488061,5.843734],[-8.006990,5.015491,-2.435066,6.913576],[2.475109,-3.486848,6.200017,2.995999],[-2.359278,4.206948,0.424372,-3.542566]],[[-9.902734,0.316466,-0.928090,4.031616],[2.817630,1.569154,6.819897,-3.940639],[-9.664302,-6.771211,9.241231,0.677030],[5.823194,8.093768,2.752197,1.930679],[8.965203,-7.008921,3.714559,-0.172897],[-7.017054,-3.290693,8.140848,4.160894],[-2.628294,6.862430,7.494582,7.806873],[0.521009,9.812951,-8.412581,3.841722],[-4.427332,8.759298,6.521673,-4.284373],[-6.589253,2.570599,3.895344,4.957932],[-4.347907,6.409390,6.578727,-1.740053],[4.186928,4.285458,-2.163914,-4.817180],[2.414175,-3.273373,4.062235,-8.018036],[-4.532093,4.954104,-6.847068,8.891793],[-9.284223,0.600053,1.316872,-0.765573]],[[4.754451,-1.733980,-1.274796,-8.757566],[-2.399736,-8.019216,3.998289,7.726624],[8.573505,-2.541478,-5.813837,-2.200925],[-1.190141,-0.558020,-0.827483,3.663166],[2.359751,0.329286,-8.361638,9.688859],[5.374391,-1.239769,-8.202163,-7.224579],[0.353279,-6.032644,-9.309479,-7.001128],[-2.222845,-5.281269,4.091254,-9.302584],[3.464769,4.131043,-8.220824,-5.021060],[-3.126737,-1.159884,0.950003,-3.509271],[2.917515,-7.304178,-1.594539,5.276805],[8.673992,4.511839,1.943064,1.230415],[0.379221,-3.777177,8.453811,5.426452],[8.100937,8.225610,-0.489296,8.938261],[-1.985464,8.942786,-9.996877,7.308275]],[[-0.082123,8.013068,-7.677525,-4.677660],[3.883150,4.572418,-9.475235,-1.308986],[9.923256,-5.156037,-9.771751,1.493079],[0.073295,2.791084,2.249328,8.351830],[7.645227,8.694443,-9.163014,3.146264],[-1.855624,-5.608358,-4.168206,2.764663],[-9.250189,5.739368,0.243124,3.422288],[-6.169410,8.336780,3.366659,1.700710],[4.726736,4.314367,7.311218,0.212500],[1.971058,-8.250759,-7.291523,0.563450],[2.671233,6.234414,-2.557426,6.999523],[8.326886,-4.317494,8.224491,2.994926],[2.677340,-8.147414,-0.155798,-4.333486],[-8.350148,0.544099,-7.272957,2.482052],[7.461012,7.945560,-1.319921,-9.577999]],[[0.720473,-3.693246,1.506506,2.243409],[-4.717104,6.563316,4.799024,7.700651],[-1.599467,-7.942485,8.272975,-4.545120],[9.515820,-1.067864,-8.594457,6.899068],[-7.810756,-6.537904,-7.815936,-4.365784],[-5.094804,4.377879,6.481992,7.283843],[3.576058,8.409878,7.987824,1.283913],[2.370651,-1.885892,4.622412,6.082746],[-9.595577,1.126712,5.791294,9.480247],[7.168855,5.579450,9.017363,-4.112043],[-2.292207,-7.667167,8.119940,-6.621660],[2.414091,-6.650608,1.389854,-4.788870],[2.047269,-3.740375,1.639412,-2.276013],[-0.428502,-4.581318,-6.113695,-6.902053],[-6.056872,2.374836,-8.148235,-1.515233]],[[-4.945495,-6.557595,-0.289298,2.357056],[-0.365331,-6.891862,-1.536431,-0.480044],[-1.147067,-9.688140,1.267780,7.311391],[4.129540,0.413319,4.829933,-0.746231],[-1.142898,2.648027,3.696003,5.833825],[-0.833190,-7.981796,-3.273558,3.163451],[0.974588,-0.412860,-2.935497,-7.811516],[-9.270960,3.670077,1.179237,0.635906],[5.060642,-0.112370,-4.918770,-4.022571],[2.167046,6.269609,-9.863760,-2.712906],[-8.042381,-2.639905,-3.412834,0.274818],[5.693284,-3.784455,-3.181977,-5.225307],[-7.867141,-0.477046,-8.575219,0.390540],[6.281045,-6.093544,8.434310,5.668664],[9.658750,-3.655316,-2.064856,-8.482283]]], dtype = "float64")#candidate|481|(9, 15, 4)|const|float64
bop_482 = relay.bitwise_xor(call_475.astype('uint64'), relay.reshape(const_481.astype('uint64'), relay.shape_of(call_475))) # shape=(9, 15, 4)
bop_485 = relay.bitwise_xor(call_476.astype('uint64'), relay.reshape(const_481.astype('uint64'), relay.shape_of(call_476))) # shape=(9, 15, 4)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_489 = func_328_call()
call_490 = func_328_call()
output = relay.Tuple([bop_482,call_489,])
output2 = relay.Tuple([bop_485,call_490,])
func_496 = relay.Function([], output)
mod['func_496'] = func_496
mod = relay.transform.InferType()(mod)
mutated_mod['func_496'] = func_496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mutated_mod.get_global_var('func_496')
call_497 = func_496_call()
output = call_497
func_498 = relay.Function([], output)
mutated_mod['func_498'] = func_498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_427_call = mod.get_global_var('func_427')
func_429_call = mutated_mod.get_global_var('func_429')
call_519 = func_427_call()
call_520 = func_427_call()
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_522 = func_328_call()
call_523 = func_328_call()
output = relay.Tuple([call_519,call_522,])
output2 = relay.Tuple([call_520,call_523,])
func_531 = relay.Function([], output)
mod['func_531'] = func_531
mod = relay.transform.InferType()(mod)
mutated_mod['func_531'] = func_531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_531_call = mutated_mod.get_global_var('func_531')
call_532 = func_531_call()
output = call_532
func_533 = relay.Function([], output)
mutated_mod['func_533'] = func_533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_580 = relay.TupleGetItem(func_357_call(), 0)
call_581 = relay.TupleGetItem(func_358_call(), 0)
func_49_call = mod.get_global_var('func_49')
func_53_call = mutated_mod.get_global_var('func_53')
var_583 = relay.var("var_583", dtype = "float32", shape = ())#candidate|583|()|var|float32
var_584 = relay.var("var_584", dtype = "float32", shape = (350,))#candidate|584|(350,)|var|float32
call_582 = func_49_call(relay.reshape(var_583.astype('float32'), []), relay.reshape(var_584.astype('float32'), [7, 10, 5]), )
call_585 = func_49_call(relay.reshape(var_583.astype('float32'), []), relay.reshape(var_584.astype('float32'), [7, 10, 5]), )
var_586 = relay.var("var_586", dtype = "float32", shape = (350,))#candidate|586|(350,)|var|float32
bop_587 = relay.left_shift(var_584.astype('int32'), relay.reshape(var_586.astype('int32'), relay.shape_of(var_584))) # shape=(350,)
uop_594 = relay.sinh(bop_587.astype('float32')) # shape=(350,)
output = relay.Tuple([call_580,call_582,var_583,uop_594,])
output2 = relay.Tuple([call_581,call_585,var_583,uop_594,])
func_598 = relay.Function([var_583,var_584,var_586,], output)
mod['func_598'] = func_598
mod = relay.transform.InferType()(mod)
var_599 = relay.var("var_599", dtype = "float32", shape = ())#candidate|599|()|var|float32
var_600 = relay.var("var_600", dtype = "float32", shape = (350,))#candidate|600|(350,)|var|float32
var_601 = relay.var("var_601", dtype = "float32", shape = (350,))#candidate|601|(350,)|var|float32
output = func_598(var_599,var_600,var_601,)
func_602 = relay.Function([var_599,var_600,var_601,], output)
mutated_mod['func_602'] = func_602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_642 = func_449_call()
call_643 = func_449_call()
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_644 = func_328_call()
call_645 = func_328_call()
output = relay.Tuple([call_642,call_644,])
output2 = relay.Tuple([call_643,call_645,])
func_661 = relay.Function([], output)
mod['func_661'] = func_661
mod = relay.transform.InferType()(mod)
mutated_mod['func_661'] = func_661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_661_call = mutated_mod.get_global_var('func_661')
call_662 = func_661_call()
output = call_662
func_663 = relay.Function([], output)
mutated_mod['func_663'] = func_663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_531_call = mod.get_global_var('func_531')
func_533_call = mutated_mod.get_global_var('func_533')
call_671 = relay.TupleGetItem(func_531_call(), 0)
call_672 = relay.TupleGetItem(func_533_call(), 0)
uop_677 = relay.acos(call_671.astype('float32')) # shape=(9, 15, 4)
uop_679 = relay.acos(call_672.astype('float32')) # shape=(9, 15, 4)
bop_684 = relay.floor_mod(uop_677.astype('float64'), relay.reshape(call_671.astype('float64'), relay.shape_of(uop_677))) # shape=(9, 15, 4)
bop_687 = relay.floor_mod(uop_679.astype('float64'), relay.reshape(call_672.astype('float64'), relay.shape_of(uop_679))) # shape=(9, 15, 4)
func_239_call = mod.get_global_var('func_239')
func_242_call = mutated_mod.get_global_var('func_242')
var_689 = relay.var("var_689", dtype = "uint64", shape = (390,))#candidate|689|(390,)|var|uint64
call_688 = relay.TupleGetItem(func_239_call(relay.reshape(var_689.astype('uint64'), [13, 3, 10])), 0)
call_690 = relay.TupleGetItem(func_242_call(relay.reshape(var_689.astype('uint64'), [13, 3, 10])), 0)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_694 = func_384_call()
call_695 = func_384_call()
output = relay.Tuple([bop_684,call_688,var_689,call_694,])
output2 = relay.Tuple([bop_687,call_690,var_689,call_695,])
func_708 = relay.Function([var_689,], output)
mod['func_708'] = func_708
mod = relay.transform.InferType()(mod)
mutated_mod['func_708'] = func_708
mutated_mod = relay.transform.InferType()(mutated_mod)
var_709 = relay.var("var_709", dtype = "uint64", shape = (390,))#candidate|709|(390,)|var|uint64
func_708_call = mutated_mod.get_global_var('func_708')
call_710 = func_708_call(var_709)
output = call_710
func_711 = relay.Function([var_709], output)
mutated_mod['func_711'] = func_711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_713 = relay.TupleGetItem(func_357_call(), 1)
call_714 = relay.TupleGetItem(func_358_call(), 1)
output = relay.Tuple([call_713,])
output2 = relay.Tuple([call_714,])
func_717 = relay.Function([], output)
mod['func_717'] = func_717
mod = relay.transform.InferType()(mod)
output = func_717()
func_718 = relay.Function([], output)
mutated_mod['func_718'] = func_718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_722 = relay.TupleGetItem(func_357_call(), 0)
call_723 = relay.TupleGetItem(func_358_call(), 0)
func_598_call = mod.get_global_var('func_598')
func_602_call = mutated_mod.get_global_var('func_602')
const_734 = relay.const(3.314044, dtype = "float32")#candidate|734|()|const|float32
var_735 = relay.var("var_735", dtype = "float32", shape = (350,))#candidate|735|(350,)|var|float32
call_733 = relay.TupleGetItem(func_598_call(relay.reshape(const_734.astype('float32'), []), relay.reshape(var_735.astype('float32'), [350,]), relay.reshape(var_735.astype('float32'), [350,]), ), 2)
call_736 = relay.TupleGetItem(func_602_call(relay.reshape(const_734.astype('float32'), []), relay.reshape(var_735.astype('float32'), [350,]), relay.reshape(var_735.astype('float32'), [350,]), ), 2)
bop_747 = relay.greater_equal(const_734.astype('bool'), var_735.astype('bool')) # shape=(350,)
output = relay.Tuple([call_722,call_733,bop_747,])
output2 = relay.Tuple([call_723,call_736,bop_747,])
func_750 = relay.Function([var_735,], output)
mod['func_750'] = func_750
mod = relay.transform.InferType()(mod)
var_751 = relay.var("var_751", dtype = "float32", shape = (350,))#candidate|751|(350,)|var|float32
output = func_750(var_751)
func_752 = relay.Function([var_751], output)
mutated_mod['func_752'] = func_752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_786 = func_328_call()
call_787 = func_328_call()
uop_790 = relay.erf(call_786.astype('float64')) # shape=(9, 15, 4)
uop_792 = relay.erf(call_787.astype('float64')) # shape=(9, 15, 4)
output = relay.Tuple([uop_790,])
output2 = relay.Tuple([uop_792,])
func_793 = relay.Function([], output)
mod['func_793'] = func_793
mod = relay.transform.InferType()(mod)
mutated_mod['func_793'] = func_793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_793_call = mutated_mod.get_global_var('func_793')
call_794 = func_793_call()
output = call_794
func_795 = relay.Function([], output)
mutated_mod['func_795'] = func_795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_835 = relay.var("var_835", dtype = "float64", shape = (16, 3))#candidate|835|(16, 3)|var|float64
uop_836 = relay.sigmoid(var_835.astype('float64')) # shape=(16, 3)
output = uop_836
output2 = uop_836
func_849 = relay.Function([var_835,], output)
mod['func_849'] = func_849
mod = relay.transform.InferType()(mod)
mutated_mod['func_849'] = func_849
mutated_mod = relay.transform.InferType()(mutated_mod)
var_850 = relay.var("var_850", dtype = "float64", shape = (16, 3))#candidate|850|(16, 3)|var|float64
func_849_call = mutated_mod.get_global_var('func_849')
call_851 = func_849_call(var_850)
output = call_851
func_852 = relay.Function([var_850], output)
mutated_mod['func_852'] = func_852
mutated_mod = relay.transform.InferType()(mutated_mod)
var_918 = relay.var("var_918", dtype = "float64", shape = (16, 14, 4))#candidate|918|(16, 14, 4)|var|float64
var_919 = relay.var("var_919", dtype = "float64", shape = (16, 14, 4))#candidate|919|(16, 14, 4)|var|float64
bop_920 = relay.divide(var_918.astype('float64'), relay.reshape(var_919.astype('float64'), relay.shape_of(var_918))) # shape=(16, 14, 4)
bop_952 = relay.not_equal(bop_920.astype('bool'), relay.reshape(var_919.astype('bool'), relay.shape_of(bop_920))) # shape=(16, 14, 4)
func_427_call = mod.get_global_var('func_427')
func_429_call = mutated_mod.get_global_var('func_429')
call_972 = func_427_call()
call_973 = func_427_call()
output = relay.Tuple([bop_952,call_972,])
output2 = relay.Tuple([bop_952,call_973,])
func_994 = relay.Function([var_918,var_919,], output)
mod['func_994'] = func_994
mod = relay.transform.InferType()(mod)
var_995 = relay.var("var_995", dtype = "float64", shape = (16, 14, 4))#candidate|995|(16, 14, 4)|var|float64
var_996 = relay.var("var_996", dtype = "float64", shape = (16, 14, 4))#candidate|996|(16, 14, 4)|var|float64
output = func_994(var_995,var_996,)
func_997 = relay.Function([var_995,var_996,], output)
mutated_mod['func_997'] = func_997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_717_call = mod.get_global_var('func_717')
func_718_call = mutated_mod.get_global_var('func_718')
call_1026 = relay.TupleGetItem(func_717_call(), 0)
call_1027 = relay.TupleGetItem(func_718_call(), 0)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_1033 = relay.TupleGetItem(func_496_call(), 0)
call_1034 = relay.TupleGetItem(func_498_call(), 0)
uop_1044 = relay.sqrt(call_1026.astype('float32')) # shape=(9, 15, 4)
uop_1046 = relay.sqrt(call_1027.astype('float32')) # shape=(9, 15, 4)
func_708_call = mod.get_global_var('func_708')
func_711_call = mutated_mod.get_global_var('func_711')
var_1051 = relay.var("var_1051", dtype = "uint64", shape = (390,))#candidate|1051|(390,)|var|uint64
call_1050 = relay.TupleGetItem(func_708_call(relay.reshape(var_1051.astype('uint64'), [390,])), 1)
call_1052 = relay.TupleGetItem(func_711_call(relay.reshape(var_1051.astype('uint64'), [390,])), 1)
output = relay.Tuple([call_1033,uop_1044,call_1050,var_1051,])
output2 = relay.Tuple([call_1034,uop_1046,call_1052,var_1051,])
func_1064 = relay.Function([var_1051,], output)
mod['func_1064'] = func_1064
mod = relay.transform.InferType()(mod)
var_1065 = relay.var("var_1065", dtype = "uint64", shape = (390,))#candidate|1065|(390,)|var|uint64
output = func_1064(var_1065)
func_1066 = relay.Function([var_1065], output)
mutated_mod['func_1066'] = func_1066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_1070 = func_449_call()
call_1071 = func_449_call()
output = relay.Tuple([call_1070,])
output2 = relay.Tuple([call_1071,])
func_1072 = relay.Function([], output)
mod['func_1072'] = func_1072
mod = relay.transform.InferType()(mod)
output = func_1072()
func_1073 = relay.Function([], output)
mutated_mod['func_1073'] = func_1073
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1087 = relay.var("var_1087", dtype = "int16", shape = (1, 5, 12))#candidate|1087|(1, 5, 12)|var|int16
var_1088 = relay.var("var_1088", dtype = "int16", shape = (10, 5, 12))#candidate|1088|(10, 5, 12)|var|int16
bop_1089 = relay.multiply(var_1087.astype('int16'), var_1088.astype('int16')) # shape=(10, 5, 12)
func_531_call = mod.get_global_var('func_531')
func_533_call = mutated_mod.get_global_var('func_533')
call_1092 = relay.TupleGetItem(func_531_call(), 1)
call_1093 = relay.TupleGetItem(func_533_call(), 1)
func_750_call = mod.get_global_var('func_750')
func_752_call = mutated_mod.get_global_var('func_752')
const_1098 = relay.const([7.251440,3.057935,-2.166705,-7.767158,4.963587,2.168472,-7.932796,4.914616,-8.084479,3.799793,-2.259627,2.603343,4.331923,-8.226330,3.517827,3.547125,-8.725267,8.823060,2.232818,8.220375,-6.161449,-6.471635,5.530752,-2.728292,-9.264348,-6.149314,0.244097,-2.594830,9.739535,6.859581,5.364517,6.657252,2.960243,1.120511,5.599516,-2.067650,2.537790,-6.241394,-0.215474,-1.321911,-5.593869,9.656563,-6.966262,-1.310583,-1.841893,6.945813,9.751827,2.260500,0.376667,7.308032,-1.541029,-8.601360,4.621328,-5.249117,6.856368,-3.776420,6.370443,7.286996,3.306113,2.923479,0.150977,-8.899723,-9.580848,6.024894,-2.977061,-0.662881,-6.795351,-8.701025,5.897221,2.799220,1.820438,-8.571888,-4.798060,-9.615968,1.344952,1.921196,-4.292939,7.582269,-7.919280,-7.599739,-2.184819,1.969256,8.430826,-7.215120,-3.714585,8.966236,1.026649,0.981262,6.517731,6.083068,9.466961,3.056580,-0.495972,-8.948012,-8.688091,7.501851,5.736635,2.153204,-6.684862,6.440131,-7.226895,-3.588385,-8.391205,4.119909,-4.443430,8.272347,2.451487,3.194517,5.478710,-6.454343,5.706787,-4.191561,-7.137415,3.011719,3.239812,-0.067778,-0.186793,4.390217,-2.238750,-1.897643,-3.206810,-6.334626,2.369075,4.810997,-3.593103,-3.840304,-2.059028,-4.345828,-8.612662,0.118804,4.064647,3.837850,7.987347,-6.392789,0.899294,-8.194327,-7.297234,-5.518580,-0.930688,0.308203,8.747397,-9.479406,-6.501325,3.974156,3.587167,0.746814,-5.793921,-5.728081,4.777296,9.659880,3.984720,-2.730421,-8.858541,1.018600,8.561947,6.293938,-9.124154,-0.639449,5.731256,-0.577405,-0.576571,5.730404,-7.821792,-4.431027,-3.854130,3.894201,4.954175,-8.900083,-9.613432,5.116090,-1.418779,-6.724973,-9.986191,4.170245,-7.341540,-7.044438,3.101463,3.403778,5.261959,-0.360053,8.020341,-6.763543,5.981840,8.201440,-6.484154,9.067130,8.636012,-2.122082,-5.787631,2.736391,5.532713,-9.511234,4.518829,-8.836710,1.749033,4.994453,-2.756527,-4.145764,-0.448975,6.262383,-7.191966,4.894350,3.453058,4.604500,4.481319,-1.801391,9.607609,-1.111005,6.180219,6.528229,2.569505,0.300864,-3.062451,1.978373,6.472436,-9.720859,-1.128714,-4.661599,2.925027,8.923777,-8.494722,8.179638,-4.602121,8.262570,-0.128055,8.320552,6.733211,-8.523106,-5.587079,-9.654040,-9.334108,8.107864,-9.459718,-6.450446,2.822677,-8.283639,-3.543327,1.588086,7.974613,-1.840865,-6.342189,1.466000,-2.239878,9.787079,-4.050343,8.568304,-2.713503,3.819679,-4.523155,-9.932954,4.285923,9.996902,-8.397758,0.243420,3.249569,-3.206282,5.973927,3.076572,5.545102,-7.451016,-2.434714,-3.645325,-7.796515,6.814132,-9.212538,-7.490726,6.741659,8.781256,8.467438,0.199840,-2.752558,-6.476173,-5.850921,5.140439,-2.124438,7.077023,1.200525,-0.514340,3.670268,-7.018139,6.219933,7.742552,1.561352,9.539469,1.039543,7.609919,-8.259033,5.203000,-6.290258,-5.244627,-0.917176,8.727990,3.442882,9.553819,-0.332560,-8.293899,7.949374,-0.045711,-4.274892,1.366782,-8.814593,6.354267,-5.026522,3.798504,-2.102213,7.103050,6.521006,-5.182450,-2.832050,7.615461,-6.020760,4.229146,-7.362706,-2.029827,3.093884,-4.681645,-2.138508,-5.162017,2.134721,4.977450,3.508154,-2.646099,-3.909594,7.730307,1.537741,5.606406,5.448477,9.430225,-1.125939,-7.023767,7.319598,8.034002,5.731436,-0.174105,-3.220255,-1.863852,-6.773137,-0.064777,3.656462,-6.126996,3.119339,-7.118806,-2.367733,-9.418642,2.580394,-5.712399,9.309981,2.397928,1.851888,6.172789], dtype = "float32")#candidate|1098|(350,)|const|float32
call_1097 = relay.TupleGetItem(func_750_call(relay.reshape(const_1098.astype('float32'), [350,])), 2)
call_1099 = relay.TupleGetItem(func_752_call(relay.reshape(const_1098.astype('float32'), [350,])), 2)
func_708_call = mod.get_global_var('func_708')
func_711_call = mutated_mod.get_global_var('func_711')
const_1102 = relay.const([7,-9,-3,-1,-3,-2,-4,5,-8,-6,-6,-7,-8,-3,6,-2,-5,9,7,-10,-9,-3,-7,-1,-7,10,-9,6,-9,-6,-9,8,-9,-6,7,1,2,-8,-2,4,7,-5,-2,-4,10,-6,8,6,10,-6,-8,2,-10,-9,-1,-4,-8,5,-1,-10,8,-9,9,6,7,-6,-10,7,1,4,8,10,-6,7,-5,8,3,2,5,1,1,-7,8,-10,-9,-10,-2,-4,-7,-8,7,10,5,2,-9,10,-2,10,2,-10,-6,-7,-1,9,-1,4,2,10,5,7,-6,-5,-5,-10,-7,-7,1,1,8,-1,6,-9,-9,-8,-10,8,2,-6,-8,-8,-9,8,-3,-3,9,-10,-9,-3,-5,-1,-6,2,-2,-8,7,7,-1,5,2,-2,1,-5,-10,-9,9,-9,10,-2,-10,-5,4,-2,-5,-8,-4,-9,2,-5,2,9,-5,4,-2,10,-7,-10,6,-8,8,9,6,-8,2,3,9,-5,2,2,6,-5,-8,5,-4,5,9,-7,2,5,9,7,-2,6,2,6,-1,-2,-4,3,10,-4,-3,-3,-6,-8,8,5,-8,4,3,9,-2,5,9,-6,7,9,-10,-5,-3,-1,8,3,-1,7,10,7,6,8,9,6,5,-4,-8,-3,-1,3,4,-7,-4,8,10,-6,5,-4,7,10,3,-8,4,1,-6,5,2,-5,-8,-2,8,5,-9,10,8,9,6,2,1,-5,8,8,-4,8,-6,10,-8,7,-5,5,-9,-3,-6,-4,10,3,-9,-10,4,5,-8,-3,-2,-6,-7,8,-7,-10,-8,9,6,-6,3,-10,-5,6,-9,-2,9,-8,8,2,-9,-10,1,-6,1,1,-9,-10,5,-10,5,7,-7,-10,-3,10,-7,10,10,-4,-10,-5,-6,-5,-1,9,-4,-9,3,6,2,-7,-6,8,3,-7,6,1,-8,-7,1,4,4,6,3,-3,-8,7,-9,2,-6,4,2,8,-4,-9,-10,-10,-6,-4,-8,7,1,-2,8,2,-4,6,6,3,8,4], dtype = "uint64")#candidate|1102|(390,)|const|uint64
call_1101 = relay.TupleGetItem(func_708_call(relay.reshape(const_1102.astype('uint64'), [390,])), 3)
call_1103 = relay.TupleGetItem(func_711_call(relay.reshape(const_1102.astype('uint64'), [390,])), 3)
func_793_call = mod.get_global_var('func_793')
func_795_call = mutated_mod.get_global_var('func_795')
call_1110 = relay.TupleGetItem(func_793_call(), 0)
call_1111 = relay.TupleGetItem(func_795_call(), 0)
output = relay.Tuple([bop_1089,call_1092,call_1097,const_1098,call_1101,const_1102,call_1110,])
output2 = relay.Tuple([bop_1089,call_1093,call_1099,const_1098,call_1103,const_1102,call_1111,])
func_1114 = relay.Function([var_1087,var_1088,], output)
mod['func_1114'] = func_1114
mod = relay.transform.InferType()(mod)
mutated_mod['func_1114'] = func_1114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1114_call = mutated_mod.get_global_var('func_1114')
var_1116 = relay.var("var_1116", dtype = "int16", shape = (1, 5, 12))#candidate|1116|(1, 5, 12)|var|int16
var_1117 = relay.var("var_1117", dtype = "int16", shape = (10, 5, 12))#candidate|1117|(10, 5, 12)|var|int16
call_1115 = func_1114_call(var_1116,var_1117,)
output = call_1115
func_1118 = relay.Function([var_1116,var_1117,], output)
mutated_mod['func_1118'] = func_1118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_793_call = mod.get_global_var('func_793')
func_795_call = mutated_mod.get_global_var('func_795')
call_1120 = relay.TupleGetItem(func_793_call(), 0)
call_1121 = relay.TupleGetItem(func_795_call(), 0)
func_793_call = mod.get_global_var('func_793')
func_795_call = mutated_mod.get_global_var('func_795')
call_1130 = relay.TupleGetItem(func_793_call(), 0)
call_1131 = relay.TupleGetItem(func_795_call(), 0)
uop_1135 = relay.sinh(call_1130.astype('float64')) # shape=(9, 15, 4)
uop_1137 = relay.sinh(call_1131.astype('float64')) # shape=(9, 15, 4)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_1138 = func_384_call()
call_1139 = func_384_call()
output = relay.Tuple([call_1120,uop_1135,call_1138,])
output2 = relay.Tuple([call_1121,uop_1137,call_1139,])
func_1147 = relay.Function([], output)
mod['func_1147'] = func_1147
mod = relay.transform.InferType()(mod)
mutated_mod['func_1147'] = func_1147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1147_call = mutated_mod.get_global_var('func_1147')
call_1148 = func_1147_call()
output = call_1148
func_1149 = relay.Function([], output)
mutated_mod['func_1149'] = func_1149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_1152 = relay.TupleGetItem(func_357_call(), 1)
call_1153 = relay.TupleGetItem(func_358_call(), 1)
output = relay.Tuple([call_1152,])
output2 = relay.Tuple([call_1153,])
func_1166 = relay.Function([], output)
mod['func_1166'] = func_1166
mod = relay.transform.InferType()(mod)
output = func_1166()
func_1167 = relay.Function([], output)
mutated_mod['func_1167'] = func_1167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_1175 = func_384_call()
call_1176 = func_384_call()
func_717_call = mod.get_global_var('func_717')
func_718_call = mutated_mod.get_global_var('func_718')
call_1187 = relay.TupleGetItem(func_717_call(), 0)
call_1188 = relay.TupleGetItem(func_718_call(), 0)
output = relay.Tuple([call_1175,call_1187,])
output2 = relay.Tuple([call_1176,call_1188,])
func_1197 = relay.Function([], output)
mod['func_1197'] = func_1197
mod = relay.transform.InferType()(mod)
mutated_mod['func_1197'] = func_1197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1197_call = mutated_mod.get_global_var('func_1197')
call_1198 = func_1197_call()
output = call_1198
func_1199 = relay.Function([], output)
mutated_mod['func_1199'] = func_1199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1166_call = mod.get_global_var('func_1166')
func_1167_call = mutated_mod.get_global_var('func_1167')
call_1279 = relay.TupleGetItem(func_1166_call(), 0)
call_1280 = relay.TupleGetItem(func_1167_call(), 0)
func_531_call = mod.get_global_var('func_531')
func_533_call = mutated_mod.get_global_var('func_533')
call_1293 = relay.TupleGetItem(func_531_call(), 1)
call_1294 = relay.TupleGetItem(func_533_call(), 1)
output = relay.Tuple([call_1279,call_1293,])
output2 = relay.Tuple([call_1280,call_1294,])
func_1298 = relay.Function([], output)
mod['func_1298'] = func_1298
mod = relay.transform.InferType()(mod)
mutated_mod['func_1298'] = func_1298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1298_call = mutated_mod.get_global_var('func_1298')
call_1299 = func_1298_call()
output = call_1299
func_1300 = relay.Function([], output)
mutated_mod['func_1300'] = func_1300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_1343 = relay.TupleGetItem(func_496_call(), 0)
call_1344 = relay.TupleGetItem(func_498_call(), 0)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_1345 = func_328_call()
call_1346 = func_328_call()
const_1355 = relay.const([[[5,-5,-8,2],[-8,7,9,-9],[4,2,-10,4],[-2,6,3,9],[-3,-6,-7,-10],[-3,-7,6,7],[-7,-2,4,4],[-3,2,-10,3],[-5,-6,-1,-9],[3,9,3,9],[-5,-6,-1,6],[1,-9,9,6],[-2,8,9,10],[-3,-9,-4,-4],[-1,9,3,3]],[[5,4,-3,8],[5,1,-1,-5],[-9,-1,-5,2],[-7,8,-6,3],[5,7,-10,-5],[1,8,-6,-8],[-7,8,6,-8],[10,-1,10,-10],[-1,-3,2,-7],[-6,6,-8,-9],[-5,-7,-8,4],[-4,6,10,9],[3,-4,1,-9],[-8,1,1,-1],[8,9,-4,3]],[[9,3,5,3],[-3,-4,-10,-3],[8,-4,-5,-5],[-2,8,9,-7],[-3,8,-10,8],[7,10,-3,-8],[9,9,-7,-9],[-1,7,10,-8],[4,-3,-6,10],[2,-3,-4,-7],[-2,-7,3,8],[-2,-3,2,-7],[9,1,-10,-9],[2,9,-4,7],[3,5,-1,-7]],[[1,-7,-5,-7],[4,-10,-10,9],[2,6,-4,-3],[8,-10,-2,-3],[-9,6,-5,-8],[5,-5,6,7],[-2,5,-7,-1],[-6,-5,8,-1],[-8,-2,-4,-2],[-10,-1,3,-6],[10,-10,-10,3],[2,4,6,10],[4,7,-6,-6],[7,3,-5,4],[-10,6,7,-6]],[[9,-2,7,9],[6,1,4,-8],[-5,1,-8,9],[3,-8,5,1],[3,-7,5,-2],[-1,-5,-10,-5],[4,5,3,1],[-7,6,4,6],[-1,8,10,-9],[4,-3,8,9],[6,-3,-8,-4],[-3,9,-8,-5],[-9,-4,-4,9],[8,-4,3,-8],[7,-5,4,-2]],[[-10,6,-7,6],[3,-8,-5,-7],[-2,-1,2,2],[-9,-6,8,1],[10,-7,-8,6],[5,8,-2,4],[4,7,-3,9],[5,6,-5,3],[-6,-4,-5,4],[6,-1,9,-10],[-3,10,5,-9],[-7,6,-3,7],[3,-4,4,10],[1,8,-9,2],[-7,-7,4,-5]],[[-10,-2,3,-4],[1,-5,-5,-4],[-6,-6,-1,4],[-3,-2,-6,9],[-9,-1,-10,-9],[1,7,8,-4],[-6,-9,1,6],[-4,-2,-5,-8],[-3,7,6,-6],[7,-4,-7,-9],[-9,1,-2,3],[-5,-10,-7,5],[9,-3,5,3],[5,8,8,-4],[-6,6,-9,-5]],[[7,5,4,-3],[-1,10,-8,-9],[-2,4,6,6],[2,-3,-2,-5],[4,2,1,4],[6,7,7,-8],[7,-9,-9,-7],[7,-1,-8,10],[10,3,9,-3],[-1,10,8,-7],[1,8,-10,-10],[6,-8,2,8],[1,-3,-7,7],[7,-6,-7,-10],[2,8,-4,1]],[[-2,4,-8,-5],[-4,-1,-5,10],[6,-6,10,1],[3,-4,-8,9],[-3,-3,7,-9],[-6,-3,9,-2],[-9,7,-4,3],[-8,8,-1,3],[10,-6,3,10],[-6,-10,-8,9],[3,-9,6,8],[-9,7,1,-4],[7,-2,5,-10],[6,-5,4,-2],[-4,6,2,-4]]], dtype = "uint64")#candidate|1355|(9, 15, 4)|const|uint64
bop_1356 = relay.maximum(call_1343.astype('uint8'), relay.reshape(const_1355.astype('uint8'), relay.shape_of(call_1343))) # shape=(9, 15, 4)
bop_1359 = relay.maximum(call_1344.astype('uint8'), relay.reshape(const_1355.astype('uint8'), relay.shape_of(call_1344))) # shape=(9, 15, 4)
bop_1373 = relay.right_shift(call_1345.astype('int64'), relay.reshape(const_1355.astype('int64'), relay.shape_of(call_1345))) # shape=(9, 15, 4)
bop_1376 = relay.right_shift(call_1346.astype('int64'), relay.reshape(const_1355.astype('int64'), relay.shape_of(call_1346))) # shape=(9, 15, 4)
var_1384 = relay.var("var_1384", dtype = "uint64", shape = (9, 15, 4))#candidate|1384|(9, 15, 4)|var|uint64
bop_1385 = relay.subtract(call_1343.astype('int32'), relay.reshape(var_1384.astype('int32'), relay.shape_of(call_1343))) # shape=(9, 15, 4)
bop_1388 = relay.subtract(call_1344.astype('int32'), relay.reshape(var_1384.astype('int32'), relay.shape_of(call_1344))) # shape=(9, 15, 4)
func_849_call = mod.get_global_var('func_849')
func_852_call = mutated_mod.get_global_var('func_852')
var_1391 = relay.var("var_1391", dtype = "float64", shape = (48,))#candidate|1391|(48,)|var|float64
call_1390 = func_849_call(relay.reshape(var_1391.astype('float64'), [16, 3]))
call_1392 = func_849_call(relay.reshape(var_1391.astype('float64'), [16, 3]))
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_1398 = func_384_call()
call_1399 = func_384_call()
output = relay.Tuple([bop_1356,bop_1373,bop_1385,call_1390,var_1391,call_1398,])
output2 = relay.Tuple([bop_1359,bop_1376,bop_1388,call_1392,var_1391,call_1399,])
func_1403 = relay.Function([var_1384,var_1391,], output)
mod['func_1403'] = func_1403
mod = relay.transform.InferType()(mod)
mutated_mod['func_1403'] = func_1403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1403_call = mutated_mod.get_global_var('func_1403')
var_1405 = relay.var("var_1405", dtype = "uint64", shape = (9, 15, 4))#candidate|1405|(9, 15, 4)|var|uint64
var_1406 = relay.var("var_1406", dtype = "float64", shape = (48,))#candidate|1406|(48,)|var|float64
call_1404 = func_1403_call(var_1405,var_1406,)
output = call_1404
func_1407 = relay.Function([var_1405,var_1406,], output)
mutated_mod['func_1407'] = func_1407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1166_call = mod.get_global_var('func_1166')
func_1167_call = mutated_mod.get_global_var('func_1167')
call_1427 = relay.TupleGetItem(func_1166_call(), 0)
call_1428 = relay.TupleGetItem(func_1167_call(), 0)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_1431 = func_384_call()
call_1432 = func_384_call()
output = relay.Tuple([call_1427,call_1431,])
output2 = relay.Tuple([call_1428,call_1432,])
func_1433 = relay.Function([], output)
mod['func_1433'] = func_1433
mod = relay.transform.InferType()(mod)
output = func_1433()
func_1434 = relay.Function([], output)
mutated_mod['func_1434'] = func_1434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_1465 = func_384_call()
call_1466 = func_384_call()
uop_1469 = relay.exp(call_1465.astype('float32')) # shape=(9, 15, 4)
uop_1471 = relay.exp(call_1466.astype('float32')) # shape=(9, 15, 4)
uop_1474 = relay.log(uop_1469.astype('float64')) # shape=(9, 15, 4)
uop_1476 = relay.log(uop_1471.astype('float64')) # shape=(9, 15, 4)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_1480 = func_384_call()
call_1481 = func_384_call()
output = relay.Tuple([uop_1474,call_1480,])
output2 = relay.Tuple([uop_1476,call_1481,])
func_1490 = relay.Function([], output)
mod['func_1490'] = func_1490
mod = relay.transform.InferType()(mod)
output = func_1490()
func_1491 = relay.Function([], output)
mutated_mod['func_1491'] = func_1491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_1522 = func_328_call()
call_1523 = func_328_call()
var_1524 = relay.var("var_1524", dtype = "float64", shape = (9, 15, 4))#candidate|1524|(9, 15, 4)|var|float64
bop_1525 = relay.multiply(call_1522.astype('uint64'), relay.reshape(var_1524.astype('uint64'), relay.shape_of(call_1522))) # shape=(9, 15, 4)
bop_1528 = relay.multiply(call_1523.astype('uint64'), relay.reshape(var_1524.astype('uint64'), relay.shape_of(call_1523))) # shape=(9, 15, 4)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_1530 = func_449_call()
call_1531 = func_449_call()
output = relay.Tuple([bop_1525,call_1530,])
output2 = relay.Tuple([bop_1528,call_1531,])
func_1532 = relay.Function([var_1524,], output)
mod['func_1532'] = func_1532
mod = relay.transform.InferType()(mod)
mutated_mod['func_1532'] = func_1532
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1533 = relay.var("var_1533", dtype = "float64", shape = (9, 15, 4))#candidate|1533|(9, 15, 4)|var|float64
func_1532_call = mutated_mod.get_global_var('func_1532')
call_1534 = func_1532_call(var_1533)
output = call_1534
func_1535 = relay.Function([var_1533], output)
mutated_mod['func_1535'] = func_1535
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1570 = relay.const([[[-2.299262,9.706481,0.581848,8.848326],[-5.882748,0.968314,-7.097929,-2.402328],[9.168162,9.413773,-7.639034,-1.013163],[9.212038,-6.338687,-6.946004,0.844428],[3.985874,-3.641565,-3.722141,0.036808],[1.374471,5.238389,-9.539112,5.329582],[6.770051,8.135321,-5.304232,-7.314295],[-0.263545,4.131582,6.652263,8.109668],[6.372982,4.827714,2.047529,3.379545]],[[2.986480,3.422213,-1.543257,6.430316],[6.001638,4.880872,5.975434,-6.398544],[4.309258,-0.974365,-1.592458,0.946678],[-3.330602,7.257347,2.991957,-1.964815],[-4.652504,2.964998,-3.334501,-6.591392],[0.875985,-2.583380,-9.973843,-1.290383],[-8.541988,-6.079151,7.489614,0.743421],[-4.894976,3.387513,6.120709,-1.668522],[6.920128,-8.833408,-6.224744,-9.713411]],[[9.443616,-2.839187,3.175723,5.925288],[-3.281080,-9.759614,0.470541,8.885550],[5.575943,1.555642,-7.588915,-6.870749],[2.918149,-6.629807,0.061192,-4.663388],[3.774213,-3.920542,5.563458,-0.426973],[7.549441,4.640059,-7.165399,-3.812956],[-2.878063,-5.649163,0.277474,-3.888263],[-7.415958,9.889389,4.747244,-2.783745],[-4.702498,6.630615,-4.160963,7.092197]],[[7.457328,-2.157027,4.820094,0.887201],[-5.911031,1.513824,-7.471281,7.343699],[-9.363405,-2.846361,-8.944859,-6.371567],[-2.655543,-9.435624,1.825490,-4.467657],[1.280121,4.204800,-1.194687,-5.892620],[-0.922101,-9.001089,0.879594,0.635480],[-2.656292,-7.443587,-8.511526,-5.493121],[-5.588693,4.532230,-0.064151,-1.322913],[-2.490372,2.534515,-1.403826,-6.646375]],[[0.876676,0.397189,-4.332037,-0.472444],[8.500282,7.658128,3.257589,-5.516971],[-2.316409,6.407429,2.497594,-3.209803],[2.606913,-4.857947,2.731697,6.235951],[-1.482025,-1.282483,1.488702,4.629477],[9.389954,8.966299,-1.488314,-9.576492],[0.035323,-4.086543,-7.296462,3.436629],[-9.237513,7.412067,-3.805655,-5.085112],[-3.598596,4.433973,7.405166,-1.866126]],[[4.139313,3.883180,9.479153,-4.037392],[4.116208,9.674097,-4.052049,-1.451744],[0.026758,-8.631313,-9.208987,-2.298526],[5.198906,-1.749053,-4.408585,7.747945],[-0.671048,-2.540236,1.707778,9.210343],[8.809582,-4.852850,3.468462,-5.052643],[-3.082887,-8.735065,5.639482,0.173043],[-8.746987,3.556184,-2.589962,-8.295110],[7.114715,-8.330995,5.526285,3.764578]],[[3.287077,-8.310660,-1.071272,9.109294],[-3.998342,8.586761,-7.741538,-8.618504],[9.230054,1.253604,8.615999,-0.362042],[-3.673324,2.726882,-9.679074,-5.278894],[-9.342188,-6.686733,3.200138,5.260056],[8.190599,9.202257,-1.333470,-5.115264],[8.029802,0.078941,9.103663,8.114833],[5.143818,-5.803610,-9.275659,7.786915],[8.680130,7.912479,1.891596,-5.603225]],[[-8.873310,-9.617489,-8.124140,-1.170436],[-9.554054,-3.701264,2.003555,-8.496421],[-3.127796,4.244037,6.079395,4.782775],[-6.208819,-6.876235,2.320697,5.791773],[-2.479217,-8.973151,-1.335089,4.677657],[4.775439,2.546660,6.813141,3.948375],[-6.835987,-9.670155,6.086320,-4.858238],[4.830344,9.434507,-6.702232,-4.027648],[-4.279830,9.090107,1.206745,1.460575]],[[-6.638012,9.180642,-6.852169,9.194118],[1.210019,6.916174,9.915929,1.022810],[-3.058676,6.712119,3.912298,6.969570],[2.557368,-9.539173,0.904472,5.354491],[-7.023330,-7.315297,5.680553,1.890197],[8.771767,0.090833,6.784004,2.387861],[5.137420,-7.702943,-9.515425,-1.399371],[-5.611007,-9.653095,-7.757115,2.148707],[4.456300,-9.309179,8.353874,5.170630]],[[-1.938786,9.333402,7.691360,6.315864],[4.702123,6.489181,1.852517,5.094891],[8.321202,-4.387896,7.433084,-0.542768],[1.866166,2.183957,7.274280,8.245110],[6.289545,5.596540,-2.566784,9.993136],[-7.938463,1.447264,-7.371222,9.709886],[2.454810,-9.484536,1.245628,7.399893],[7.657222,5.099886,6.409767,-7.345312],[3.907029,-0.524975,-6.463317,6.812699]],[[-5.703271,-9.171274,-3.325813,-6.007236],[5.075342,-1.468284,-4.769899,1.408322],[0.455666,-5.265608,-5.101584,4.365525],[-1.282826,5.652348,-1.487079,0.323660],[2.245326,8.471653,9.620295,8.303046],[-5.718738,6.095450,1.819636,-8.659218],[4.946493,-7.368627,8.259897,9.504932],[9.388475,-3.846105,6.747240,-5.311708],[-9.632481,-7.039413,-3.542617,-0.240788]],[[-1.302906,0.513735,5.630485,-7.703090],[-2.421037,-5.796374,-2.413643,4.745373],[-4.400881,6.341707,8.430391,-9.525213],[-1.489577,2.487524,3.254459,4.388610],[0.467851,8.365671,1.131077,8.563155],[-4.697933,6.690685,5.180367,-6.632538],[1.499534,3.951876,-5.523053,-8.057611],[2.834319,9.036509,2.568700,-4.385558],[9.741837,3.104273,7.704636,-7.584362]]], dtype = "float32")#candidate|1570|(12, 9, 4)|const|float32
uop_1571 = relay.sigmoid(const_1570.astype('float32')) # shape=(12, 9, 4)
uop_1574 = relay.sinh(uop_1571.astype('float64')) # shape=(12, 9, 4)
output = uop_1574
output2 = uop_1574
func_1578 = relay.Function([], output)
mod['func_1578'] = func_1578
mod = relay.transform.InferType()(mod)
mutated_mod['func_1578'] = func_1578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1578_call = mutated_mod.get_global_var('func_1578')
call_1579 = func_1578_call()
output = call_1579
func_1580 = relay.Function([], output)
mutated_mod['func_1580'] = func_1580
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1593 = relay.var("var_1593", dtype = "uint8", shape = (15, 6, 7))#candidate|1593|(15, 6, 7)|var|uint8
var_1594 = relay.var("var_1594", dtype = "uint8", shape = (15, 6, 7))#candidate|1594|(15, 6, 7)|var|uint8
bop_1595 = relay.bitwise_xor(var_1593.astype('uint8'), relay.reshape(var_1594.astype('uint8'), relay.shape_of(var_1593))) # shape=(15, 6, 7)
output = relay.Tuple([bop_1595,])
output2 = relay.Tuple([bop_1595,])
func_1599 = relay.Function([var_1593,var_1594,], output)
mod['func_1599'] = func_1599
mod = relay.transform.InferType()(mod)
var_1600 = relay.var("var_1600", dtype = "uint8", shape = (15, 6, 7))#candidate|1600|(15, 6, 7)|var|uint8
var_1601 = relay.var("var_1601", dtype = "uint8", shape = (15, 6, 7))#candidate|1601|(15, 6, 7)|var|uint8
output = func_1599(var_1600,var_1601,)
func_1602 = relay.Function([var_1600,var_1601,], output)
mutated_mod['func_1602'] = func_1602
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1636 = relay.const([[[10,-10,-3,-7,7,-2,-10,9,10,10,-8,-6,7,5,4,-4],[1,-9,8,7,3,-6,-6,-5,-3,-2,-10,-1,-10,3,-8,-10]],[[10,-3,-9,-6,2,5,6,-6,-5,-10,-7,-1,1,-10,-10,-8],[-2,-1,-1,-3,-8,1,-8,-5,-7,5,-7,-10,-2,-5,-5,-5]],[[4,-7,-2,10,-1,-5,9,-10,-4,10,-3,10,-3,8,-8,4],[-8,8,3,1,8,3,-8,2,1,-3,-2,-2,8,2,4,9]],[[-9,1,5,-8,-9,-8,7,9,4,4,7,-3,-7,-2,-1,2],[-7,3,-6,5,-3,4,-5,-8,7,6,-8,-8,6,-6,10,-8]],[[-1,-1,2,-2,-8,-3,-9,5,4,7,-2,7,-4,6,8,-3],[5,-6,1,-1,6,4,-6,-1,-2,-2,-5,2,-3,3,2,-2]],[[1,3,-8,1,-10,-1,-7,7,-3,4,10,-7,-4,-4,-8,3],[-4,1,3,-8,-10,9,1,7,-5,-2,-8,-7,9,1,8,9]],[[2,-6,4,6,-4,3,3,1,-10,-4,-4,-1,4,2,-5,6],[9,-2,7,-8,5,6,1,5,-2,10,-1,9,-4,-7,-10,-8]],[[-4,-5,-10,-2,4,2,-7,9,-7,-5,3,-4,-5,-7,4,5],[8,9,-2,-5,-10,4,-4,-9,3,1,-10,-2,-6,1,8,5]],[[5,-6,-6,-7,-5,-6,-5,2,-10,3,-8,6,-6,1,2,-10],[2,6,-4,-6,4,-10,8,-9,8,10,-9,-9,3,8,10,4]]], dtype = "uint32")#candidate|1636|(9, 2, 16)|const|uint32
var_1637 = relay.var("var_1637", dtype = "uint32", shape = (9, 2, 16))#candidate|1637|(9, 2, 16)|var|uint32
bop_1638 = relay.greater(const_1636.astype('bool'), relay.reshape(var_1637.astype('bool'), relay.shape_of(const_1636))) # shape=(9, 2, 16)
output = bop_1638
output2 = bop_1638
func_1644 = relay.Function([var_1637,], output)
mod['func_1644'] = func_1644
mod = relay.transform.InferType()(mod)
mutated_mod['func_1644'] = func_1644
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1645 = relay.var("var_1645", dtype = "uint32", shape = (9, 2, 16))#candidate|1645|(9, 2, 16)|var|uint32
func_1644_call = mutated_mod.get_global_var('func_1644')
call_1646 = func_1644_call(var_1645)
output = call_1646
func_1647 = relay.Function([var_1645], output)
mutated_mod['func_1647'] = func_1647
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1694 = relay.var("var_1694", dtype = "float32", shape = (10, 2, 1))#candidate|1694|(10, 2, 1)|var|float32
const_1695 = relay.const([[[4.473026,-6.017712,-5.635999,-1.103617,6.143955,9.118362,-3.334216,2.370244,4.048566,3.846468,-5.881275,-9.197063,7.933765,4.943330,4.326603],[3.776918,9.625376,1.533718,7.996992,-6.613651,-6.146372,-7.470828,-4.660350,5.161720,4.798740,2.749112,2.275353,4.317650,4.716055,4.779218]],[[0.575570,0.953086,-1.677774,0.661493,-1.282696,6.901737,7.145329,8.934223,8.853695,5.928651,5.917593,-7.655959,-8.388402,-4.486309,-1.697099],[-0.873652,-3.349443,5.944804,-3.943904,-3.326047,-5.887299,9.696416,-1.131035,1.822112,-3.235649,-0.268062,-2.735168,-4.195592,7.831618,-4.860441]],[[-9.096970,2.684919,-2.790000,3.605277,8.467954,0.867816,0.891701,6.520672,-4.462633,4.052187,7.414377,-5.709052,2.385737,-6.510523,2.475346],[-4.151275,-6.604305,-8.663215,-9.143010,1.698099,-6.347756,-4.407907,-0.288793,6.619801,-7.033056,0.397191,-2.596456,3.371491,-1.888088,-3.114756]],[[-2.479256,4.924770,0.143463,8.751242,6.324663,7.126683,-1.755040,-1.419065,-8.168383,0.318874,-4.587440,-1.574969,-1.552000,-6.823545,-1.262907],[3.996728,-6.796633,1.855328,-3.125896,2.575265,3.604510,4.443501,-1.449885,-8.039808,6.103536,-9.897838,-3.667461,4.466267,-1.657816,1.284847]],[[-6.445705,-2.705721,3.918429,-5.777840,-7.290484,-7.345880,2.141253,6.093353,9.024715,-1.915573,5.589467,-1.252225,0.029745,9.027026,-3.535628],[-3.582237,7.809809,4.625996,-6.071690,-0.086620,4.652717,8.941556,5.934234,5.079463,-4.595948,7.018586,-4.748411,-4.127770,1.717196,6.071273]],[[-9.940887,6.168029,-9.394196,5.401770,-2.428459,-8.623207,-2.133929,-0.237835,-1.500713,-4.089798,4.439091,4.304336,7.968330,-2.786654,7.497439],[-0.787351,1.874729,6.155771,-1.947492,1.080855,-3.256902,5.295531,1.052427,-1.012966,4.915129,-8.917906,5.211544,-3.190779,3.957491,0.958400]],[[-8.485950,3.254217,8.976567,-7.988484,5.666727,5.287928,3.583290,-6.471137,-5.318509,-0.397734,8.300931,4.334688,-2.995288,8.139470,-5.397002],[-8.031593,3.982585,-9.740821,-5.427812,-5.526627,-4.480598,-7.730778,-3.684744,-7.845572,6.463018,-5.486070,-7.946710,8.963433,4.987946,-7.639001]],[[-5.173766,4.331999,-1.377674,-1.406463,-5.159953,-8.077267,-0.975530,-4.042001,0.432820,-9.261102,3.155951,8.293750,-1.143926,3.872921,-9.099511],[7.476874,-2.917777,-8.167067,-0.378409,-0.297864,8.790525,-9.265857,0.223285,2.600313,9.120860,9.891885,-2.978490,-1.039121,-3.275837,4.585326]],[[-1.567031,7.596927,7.935378,4.732010,-7.464714,-7.697495,7.119829,-5.232687,3.309886,7.371116,1.431582,4.224676,-2.973428,-1.911835,1.541823],[8.673616,-1.457963,4.660746,-5.624149,4.739927,-5.839404,-1.096229,-6.455709,-1.228861,-0.562981,4.976695,-6.454893,-5.656704,-1.686729,5.050734]],[[-5.672518,3.737600,4.904504,-4.667779,-9.440057,0.388554,8.129705,-5.663146,-9.774361,4.876789,-7.211989,-5.801923,6.918770,7.245378,0.465800],[-4.504122,5.506890,-7.242433,-7.723605,-7.660158,-8.901739,3.523234,-1.960827,-0.946270,-0.731151,2.035947,-3.512917,5.681591,-6.455933,3.029604]]], dtype = "float32")#candidate|1695|(10, 2, 15)|const|float32
bop_1696 = relay.floor_mod(var_1694.astype('float32'), const_1695.astype('float32')) # shape=(10, 2, 15)
func_1298_call = mod.get_global_var('func_1298')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_1710 = relay.TupleGetItem(func_1298_call(), 1)
call_1711 = relay.TupleGetItem(func_1300_call(), 1)
var_1723 = relay.var("var_1723", dtype = "float64", shape = (9, 15, 4))#candidate|1723|(9, 15, 4)|var|float64
bop_1724 = relay.bitwise_and(call_1710.astype('int8'), relay.reshape(var_1723.astype('int8'), relay.shape_of(call_1710))) # shape=(9, 15, 4)
bop_1727 = relay.bitwise_and(call_1711.astype('int8'), relay.reshape(var_1723.astype('int8'), relay.shape_of(call_1711))) # shape=(9, 15, 4)
func_1532_call = mod.get_global_var('func_1532')
func_1535_call = mutated_mod.get_global_var('func_1535')
call_1739 = relay.TupleGetItem(func_1532_call(relay.reshape(call_1710.astype('float64'), [9, 15, 4])), 1)
call_1740 = relay.TupleGetItem(func_1535_call(relay.reshape(call_1710.astype('float64'), [9, 15, 4])), 1)
uop_1772 = relay.tan(var_1694.astype('float64')) # shape=(10, 2, 1)
func_708_call = mod.get_global_var('func_708')
func_711_call = mutated_mod.get_global_var('func_711')
var_1776 = relay.var("var_1776", dtype = "uint64", shape = (65, 6))#candidate|1776|(65, 6)|var|uint64
call_1775 = relay.TupleGetItem(func_708_call(relay.reshape(var_1776.astype('uint64'), [390,])), 0)
call_1777 = relay.TupleGetItem(func_711_call(relay.reshape(var_1776.astype('uint64'), [390,])), 0)
uop_1781 = relay.asinh(uop_1772.astype('float64')) # shape=(10, 2, 1)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1788 = relay.TupleGetItem(func_1072_call(), 0)
call_1789 = relay.TupleGetItem(func_1073_call(), 0)
var_1792 = relay.var("var_1792", dtype = "float64", shape = (10, 2, 9))#candidate|1792|(10, 2, 9)|var|float64
bop_1793 = relay.less_equal(uop_1781.astype('bool'), var_1792.astype('bool')) # shape=(10, 2, 9)
output = relay.Tuple([bop_1696,bop_1724,call_1739,call_1775,var_1776,call_1788,bop_1793,])
output2 = relay.Tuple([bop_1696,bop_1727,call_1740,call_1777,var_1776,call_1789,bop_1793,])
func_1802 = relay.Function([var_1694,var_1723,var_1776,var_1792,], output)
mod['func_1802'] = func_1802
mod = relay.transform.InferType()(mod)
var_1803 = relay.var("var_1803", dtype = "float32", shape = (10, 2, 1))#candidate|1803|(10, 2, 1)|var|float32
var_1804 = relay.var("var_1804", dtype = "float64", shape = (9, 15, 4))#candidate|1804|(9, 15, 4)|var|float64
var_1805 = relay.var("var_1805", dtype = "uint64", shape = (65, 6))#candidate|1805|(65, 6)|var|uint64
var_1806 = relay.var("var_1806", dtype = "float64", shape = (10, 2, 9))#candidate|1806|(10, 2, 9)|var|float64
output = func_1802(var_1803,var_1804,var_1805,var_1806,)
func_1807 = relay.Function([var_1803,var_1804,var_1805,var_1806,], output)
mutated_mod['func_1807'] = func_1807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_1811 = func_384_call()
call_1812 = func_384_call()
func_708_call = mod.get_global_var('func_708')
func_711_call = mutated_mod.get_global_var('func_711')
const_1817 = relay.const([6,-4,-6,9,-7,-6,-9,9,1,4,-4,-1,2,5,2,2,3,-2,8,-7,-6,-7,7,-10,7,-8,10,6,-7,-10,4,-10,-1,-8,-2,5,9,2,9,6,-7,6,4,-1,-2,2,4,-5,-4,3,9,3,-9,5,8,5,6,5,3,10,7,-1,6,8,-10,-6,-9,6,8,8,-3,-3,4,8,4,-3,2,3,-2,7,-2,-1,-4,10,8,-7,-9,-9,-8,10,-5,-4,9,-4,-8,4,-4,4,-2,9,2,-3,6,-6,1,6,-1,2,8,2,6,10,1,-9,8,-2,-4,3,-9,4,-7,5,-1,-9,-4,8,6,-4,-4,7,1,-4,6,-4,-8,-6,-1,4,-1,-2,3,7,-8,6,3,5,5,-10,-9,-10,5,4,9,7,-3,3,8,5,10,-9,-5,7,-6,-2,3,3,-6,-3,7,4,-8,-5,-8,6,2,-1,2,6,4,4,-10,7,-6,-2,10,-4,-5,-9,-9,-1,10,9,-9,-1,-5,-2,4,10,8,4,9,10,-6,9,4,10,3,10,-6,-4,-8,5,-6,1,-8,3,2,3,4,7,3,4,5,-5,4,2,-8,3,4,9,10,1,-7,4,-6,9,-6,-3,-6,-4,2,2,4,5,3,10,-5,-7,-5,4,-2,9,6,1,-2,2,-10,5,2,-2,3,-8,4,1,-8,1,9,-10,-3,5,-3,-1,-3,-8,6,10,3,10,-7,7,7,7,-7,1,5,7,-4,2,-5,-2,10,2,4,-3,2,-6,7,5,2,5,-1,-7,1,2,-2,8,-6,7,10,-1,-1,3,2,-5,-3,4,-3,9,-2,9,-5,6,-5,3,5,10,-1,-4,-3,9,-9,10,-4,5,1,-8,9,10,-8,-1,-7,9,-6,-2,3,-4,4,4,6,4,3,6,7,-8,-10,-8,-2,2,-9,8,8,4,-8,10,10,-1,-9,5,-4,-2,3,-9,6,-6,10,7,-6,7,-1,-5,-4,-4,-5,8,-3,4,-10,-5,-8,3], dtype = "uint64")#candidate|1817|(390,)|const|uint64
call_1816 = relay.TupleGetItem(func_708_call(relay.reshape(const_1817.astype('uint64'), [390,])), 0)
call_1818 = relay.TupleGetItem(func_711_call(relay.reshape(const_1817.astype('uint64'), [390,])), 0)
output = relay.Tuple([call_1811,call_1816,const_1817,])
output2 = relay.Tuple([call_1812,call_1818,const_1817,])
func_1828 = relay.Function([], output)
mod['func_1828'] = func_1828
mod = relay.transform.InferType()(mod)
output = func_1828()
func_1829 = relay.Function([], output)
mutated_mod['func_1829'] = func_1829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_531_call = mod.get_global_var('func_531')
func_533_call = mutated_mod.get_global_var('func_533')
call_1833 = relay.TupleGetItem(func_531_call(), 0)
call_1834 = relay.TupleGetItem(func_533_call(), 0)
var_1839 = relay.var("var_1839", dtype = "float64", shape = (9, 15, 4))#candidate|1839|(9, 15, 4)|var|float64
bop_1840 = relay.not_equal(call_1833.astype('bool'), relay.reshape(var_1839.astype('bool'), relay.shape_of(call_1833))) # shape=(9, 15, 4)
bop_1843 = relay.not_equal(call_1834.astype('bool'), relay.reshape(var_1839.astype('bool'), relay.shape_of(call_1834))) # shape=(9, 15, 4)
bop_1844 = relay.power(bop_1840.astype('float64'), relay.reshape(var_1839.astype('float64'), relay.shape_of(bop_1840))) # shape=(9, 15, 4)
bop_1847 = relay.power(bop_1843.astype('float64'), relay.reshape(var_1839.astype('float64'), relay.shape_of(bop_1843))) # shape=(9, 15, 4)
func_717_call = mod.get_global_var('func_717')
func_718_call = mutated_mod.get_global_var('func_718')
call_1859 = relay.TupleGetItem(func_717_call(), 0)
call_1860 = relay.TupleGetItem(func_718_call(), 0)
output = relay.Tuple([bop_1844,call_1859,])
output2 = relay.Tuple([bop_1847,call_1860,])
func_1861 = relay.Function([var_1839,], output)
mod['func_1861'] = func_1861
mod = relay.transform.InferType()(mod)
var_1862 = relay.var("var_1862", dtype = "float64", shape = (9, 15, 4))#candidate|1862|(9, 15, 4)|var|float64
output = func_1861(var_1862)
func_1863 = relay.Function([var_1862], output)
mutated_mod['func_1863'] = func_1863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_1865 = func_384_call()
call_1866 = func_384_call()
output = relay.Tuple([call_1865,])
output2 = relay.Tuple([call_1866,])
func_1875 = relay.Function([], output)
mod['func_1875'] = func_1875
mod = relay.transform.InferType()(mod)
output = func_1875()
func_1876 = relay.Function([], output)
mutated_mod['func_1876'] = func_1876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_717_call = mod.get_global_var('func_717')
func_718_call = mutated_mod.get_global_var('func_718')
call_1900 = relay.TupleGetItem(func_717_call(), 0)
call_1901 = relay.TupleGetItem(func_718_call(), 0)
func_1490_call = mod.get_global_var('func_1490')
func_1491_call = mutated_mod.get_global_var('func_1491')
call_1914 = relay.TupleGetItem(func_1490_call(), 1)
call_1915 = relay.TupleGetItem(func_1491_call(), 1)
func_1599_call = mod.get_global_var('func_1599')
func_1602_call = mutated_mod.get_global_var('func_1602')
const_1922 = relay.const([9,8,-8,9,-3,5,6,6,6,1,7,-8,4,8,-4,-5,5,-1,4,-10,-8,-2,1,-2,-1,10,-3,-5,-2,3,9,1,3,-7,-1,-5,-2,-5,4,-1,-10,-1,1,-2,-10,-1,4,3,1,4,8,2,6,-2,-7,-3,4,-10,1,-10,-6,2,-10,-9,6,6,5,-4,7,1,-1,-1,-10,1,-2,4,9,-9,-10,3,-4,-10,9,9,-9,2,-5,-4,3,-8,-4,2,-8,-4,1,-6,6,-3,-1,-3,-1,10,-7,2,-2,4,3,-1,8,3,5,-4,7,-8,-10,-9,-3,8,5,-1,-10,-5,2,4,-5,1,8,1,-3,-4,-9,3,-1,-3,2,-5,10,3,-8,-1,-6,3,8,-9,-4,-3,5,-6,-10,7,4,2,4,5,6,6,-10,8,-4,10,-10,-2,10,3,8,2,2,7,1,9,-10,9,-4,10,4,6,3,-8,8,5,-3,-8,-10,2,-7,-9,6,8,5,-7,-8,-2,3,-7,5,-6,10,-5,1,4,-8,6,10,-5,-4,5,-7,4,-9,2,-5,-2,2,-7,-5,-10,3,9,2,10,4,9,-2,-3,5,3,-2,7,2,-9,-3,10,-7,-1,10,-6,-7,-10,-9,8,-6,6,-7,6,-6,-8,3,7,6,-10,9,5,-2,-5,-7,7,-5,3,-7,-5,3,-2,-1,8,-8,6,-6,-3,5,3,10,-5,-4,-1,9,-4,7,-1,-6,6,9,1,-4,-6,-2,-8,1,-9,4,-8,6,-5,1,-1,-5,2,2,1,-10,2,-8,-4,6,5,-3,-2,8,-2,-5,7,4,4,-3,-2,4,4,-6,10,-4,-5,2,8,7,1,4,2,5,6,2,2,-1,7,-7,-3,-4,9,-6,-9,6,-4,6,-10,3,3,-3,-1,-1,6,-7,-8,7,-8,4,-5,7,-3,-7,-6,-3,6,-1,-2,7,-2,-7,7,10,7,5,6,-3,-5,-6,-9,-7,4,-5,-2,-6,-9,5,-9,3,8,-7,-10,-7,-9,3,1,6,-9,4,5,6,-5,2,-5,-9,5,-9,-6,-7,9,-6,3,6,3,3,-9,6,7,7,4,-7,2,1,4,5,-1,4,3,6,-9,5,-6,-4,-10,-9,9,-1,-1,8,-2,9,-4,-7,-2,-2,-10,2,10,2,-1,2,4,10,6,5,3,-1,-8,3,-9,-2,3,-6,-2,-5,-9,10,10,1,9,6,-9,-10,-3,-8,9,-3,3,-7,10,-7,-9,-2,-8,9,-10,-1,9,-7,-6,9,4,8,-3,-4,9,2,10,-10,-1,-8,-1,-2,-2,-7,6,4,7,-9,10,-5,-5,-8,-5,5,-7,-6,4,1,1,-4,3,8,1,2,1,10,-4,-2,7,4,-2,2,-2,-6,2,-1,10,-5,-5,2,-4,-3,-9,9,4,-1,6,6,8,-3,2,5,1,2,-9,-3,7,3,-1,-3,6,1,9,9,7,-10,-4,-2,-7,3,1,8,2,-3,4,7,-1,-9,6,-8,10,4,2,-2,-4,-4,-3,-2,-6,9,10,7,4,2,5,-3,-7,-2,-6,-8,9,3,8,6,-10,-1,1,-4,3,-3,5,5,4,2,10,-8,4,1,-9,-4,-4,-1,-3,7,2,-4,7,-10,-7,-1,-2,7,2,-10,9], dtype = "uint8")#candidate|1922|(630,)|const|uint8
call_1921 = relay.TupleGetItem(func_1599_call(relay.reshape(const_1922.astype('uint8'), [15, 6, 7]), relay.reshape(const_1922.astype('uint8'), [15, 6, 7]), ), 0)
call_1923 = relay.TupleGetItem(func_1602_call(relay.reshape(const_1922.astype('uint8'), [15, 6, 7]), relay.reshape(const_1922.astype('uint8'), [15, 6, 7]), ), 0)
output = relay.Tuple([call_1900,call_1914,call_1921,const_1922,])
output2 = relay.Tuple([call_1901,call_1915,call_1923,const_1922,])
func_1931 = relay.Function([], output)
mod['func_1931'] = func_1931
mod = relay.transform.InferType()(mod)
mutated_mod['func_1931'] = func_1931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mutated_mod.get_global_var('func_1931')
call_1932 = func_1931_call()
output = call_1932
func_1933 = relay.Function([], output)
mutated_mod['func_1933'] = func_1933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_1937 = func_384_call()
call_1938 = func_384_call()
func_1532_call = mod.get_global_var('func_1532')
func_1535_call = mutated_mod.get_global_var('func_1535')
call_1950 = relay.TupleGetItem(func_1532_call(relay.reshape(call_1937.astype('float64'), [9, 15, 4])), 1)
call_1951 = relay.TupleGetItem(func_1535_call(relay.reshape(call_1937.astype('float64'), [9, 15, 4])), 1)
func_750_call = mod.get_global_var('func_750')
func_752_call = mutated_mod.get_global_var('func_752')
var_1964 = relay.var("var_1964", dtype = "float32", shape = (350,))#candidate|1964|(350,)|var|float32
call_1963 = relay.TupleGetItem(func_750_call(relay.reshape(var_1964.astype('float32'), [350,])), 2)
call_1965 = relay.TupleGetItem(func_752_call(relay.reshape(var_1964.astype('float32'), [350,])), 2)
var_1968 = relay.var("var_1968", dtype = "float32", shape = (350,))#candidate|1968|(350,)|var|float32
bop_1969 = relay.not_equal(var_1964.astype('bool'), relay.reshape(var_1968.astype('bool'), relay.shape_of(var_1964))) # shape=(350,)
func_849_call = mod.get_global_var('func_849')
func_852_call = mutated_mod.get_global_var('func_852')
const_1977 = relay.const([1.192125,-8.054967,1.054923,6.419971,-9.999795,-2.500484,2.478223,-6.092655,2.247863,0.901257,5.925665,-9.724918,-5.224800,9.416110,2.534563,3.817579,-9.817804,-7.621939,7.260227,-3.177279,6.809266,3.010695,6.110184,1.319035,1.945503,-4.429374,3.818515,-1.782462,4.926006,2.971605,7.892246,8.556976,-9.990545,3.874159,6.717123,0.190074,1.407141,1.472784,-0.818219,4.684390,8.809430,-5.454920,-4.538338,5.428052,3.135974,1.351168,3.826487,-2.024931], dtype = "float64")#candidate|1977|(48,)|const|float64
call_1976 = func_849_call(relay.reshape(const_1977.astype('float64'), [16, 3]))
call_1978 = func_849_call(relay.reshape(const_1977.astype('float64'), [16, 3]))
output = relay.Tuple([call_1937,call_1950,call_1963,bop_1969,call_1976,const_1977,])
output2 = relay.Tuple([call_1938,call_1951,call_1965,bop_1969,call_1978,const_1977,])
func_1984 = relay.Function([var_1964,var_1968,], output)
mod['func_1984'] = func_1984
mod = relay.transform.InferType()(mod)
var_1985 = relay.var("var_1985", dtype = "float32", shape = (350,))#candidate|1985|(350,)|var|float32
var_1986 = relay.var("var_1986", dtype = "float32", shape = (350,))#candidate|1986|(350,)|var|float32
output = func_1984(var_1985,var_1986,)
func_1987 = relay.Function([var_1985,var_1986,], output)
mutated_mod['func_1987'] = func_1987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1875_call = mod.get_global_var('func_1875')
func_1876_call = mutated_mod.get_global_var('func_1876')
call_2001 = relay.TupleGetItem(func_1875_call(), 0)
call_2002 = relay.TupleGetItem(func_1876_call(), 0)
func_1532_call = mod.get_global_var('func_1532')
func_1535_call = mutated_mod.get_global_var('func_1535')
call_2005 = relay.TupleGetItem(func_1532_call(relay.reshape(call_2001.astype('float64'), [9, 15, 4])), 1)
call_2006 = relay.TupleGetItem(func_1535_call(relay.reshape(call_2001.astype('float64'), [9, 15, 4])), 1)
output = relay.Tuple([call_2001,call_2005,])
output2 = relay.Tuple([call_2002,call_2006,])
func_2020 = relay.Function([], output)
mod['func_2020'] = func_2020
mod = relay.transform.InferType()(mod)
mutated_mod['func_2020'] = func_2020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2020_call = mutated_mod.get_global_var('func_2020')
call_2021 = func_2020_call()
output = call_2021
func_2022 = relay.Function([], output)
mutated_mod['func_2022'] = func_2022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_531_call = mod.get_global_var('func_531')
func_533_call = mutated_mod.get_global_var('func_533')
call_2063 = relay.TupleGetItem(func_531_call(), 0)
call_2064 = relay.TupleGetItem(func_533_call(), 0)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_2066 = relay.TupleGetItem(func_661_call(), 1)
call_2067 = relay.TupleGetItem(func_663_call(), 1)
output = relay.Tuple([call_2063,call_2066,])
output2 = relay.Tuple([call_2064,call_2067,])
func_2076 = relay.Function([], output)
mod['func_2076'] = func_2076
mod = relay.transform.InferType()(mod)
output = func_2076()
func_2077 = relay.Function([], output)
mutated_mod['func_2077'] = func_2077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_2127 = relay.TupleGetItem(func_1931_call(), 3)
call_2128 = relay.TupleGetItem(func_1933_call(), 3)
output = relay.Tuple([call_2127,])
output2 = relay.Tuple([call_2128,])
func_2129 = relay.Function([], output)
mod['func_2129'] = func_2129
mod = relay.transform.InferType()(mod)
mutated_mod['func_2129'] = func_2129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2129_call = mutated_mod.get_global_var('func_2129')
call_2130 = func_2129_call()
output = call_2130
func_2131 = relay.Function([], output)
mutated_mod['func_2131'] = func_2131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_2230 = func_328_call()
call_2231 = func_328_call()
output = call_2230
output2 = call_2231
func_2240 = relay.Function([], output)
mod['func_2240'] = func_2240
mod = relay.transform.InferType()(mod)
output = func_2240()
func_2241 = relay.Function([], output)
mutated_mod['func_2241'] = func_2241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_531_call = mod.get_global_var('func_531')
func_533_call = mutated_mod.get_global_var('func_533')
call_2260 = relay.TupleGetItem(func_531_call(), 1)
call_2261 = relay.TupleGetItem(func_533_call(), 1)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_2290 = func_328_call()
call_2291 = func_328_call()
output = relay.Tuple([call_2260,call_2290,])
output2 = relay.Tuple([call_2261,call_2291,])
func_2294 = relay.Function([], output)
mod['func_2294'] = func_2294
mod = relay.transform.InferType()(mod)
output = func_2294()
func_2295 = relay.Function([], output)
mutated_mod['func_2295'] = func_2295
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2332 = relay.const([[[5.447756,7.810534,8.135811,-0.920412,7.303801,-5.224334,1.765759,-7.674240,4.423647,-1.941760],[1.944532,1.758004,4.921402,-8.049835,9.520231,-6.615381,0.255062,8.385854,-8.720823,-9.729924],[8.993772,5.742544,4.881653,-4.278091,3.200983,1.105405,6.756981,1.984865,3.955568,-6.641112],[-1.776271,9.558152,-8.954016,-3.131449,-8.153107,1.687960,4.088442,-0.555187,-6.528637,5.329843],[-4.548257,-6.344863,-2.027499,-4.561692,-9.550063,-3.947742,8.912172,-9.435210,1.134250,7.406534],[5.548237,1.752599,6.723457,1.686086,-0.063113,1.362332,-9.617654,-9.411883,3.179114,-0.990837],[-0.115140,-7.975603,-2.242954,1.520999,6.813184,0.910121,7.376366,-7.956935,-3.944884,6.510015],[-4.609140,1.142778,-0.381922,6.971726,3.802228,0.695636,6.348612,7.374159,-9.146956,7.284980],[6.996941,-4.559425,4.739739,6.127943,8.209694,-8.148982,2.518943,-5.601567,6.816393,-9.991514],[4.618032,-0.516768,8.946191,-8.302964,8.350277,-4.602958,-2.924859,4.662015,2.298180,7.973225],[3.658049,-8.158358,-7.013636,2.759482,5.220997,-8.147512,5.322497,8.939628,-8.597028,6.259591],[5.930514,9.476433,-2.754127,2.823416,6.259394,-7.523686,-0.681546,-0.080544,1.643546,-3.393374],[6.217660,2.558152,-5.329811,2.813088,-4.535358,-6.607188,-9.284057,2.409252,-4.338080,-6.692157],[-4.172460,3.297225,-4.044872,0.617183,0.838107,-6.356688,-5.817157,1.083765,-0.390820,6.477001]],[[6.097016,-5.248104,0.151751,4.170475,-9.741083,-3.910386,-3.113124,1.951210,5.179617,7.336146],[-6.486750,8.169858,5.129129,3.228334,4.961358,2.766224,-4.772238,2.822673,1.180843,-5.563966],[-7.527243,-7.696667,-7.691361,1.010774,-1.480192,-4.521404,-9.947073,5.277702,-9.126122,3.102567],[-4.042851,9.771513,-1.731096,-4.591012,4.162663,5.832185,4.941768,-8.861414,3.619584,9.672637],[-0.118347,4.191739,6.470934,6.772384,8.280916,-2.837742,8.108453,4.909216,-9.720175,4.612721],[-8.472562,1.219262,4.276259,8.389135,-4.287397,-4.425901,-3.654340,4.909878,5.017842,8.459674],[-6.695498,-9.699681,3.901743,9.833056,6.723646,0.464380,-1.538729,-4.330344,9.353641,-4.022309],[-3.357424,-0.302638,-8.950107,6.120922,-5.042437,9.907625,-3.864303,-8.069532,4.539312,4.822964],[3.799023,-2.588797,4.339072,7.786080,-3.296679,-1.833935,-5.147432,3.452966,4.151666,-5.284088],[0.569786,-3.815046,2.832991,-9.416551,-3.491435,-9.022235,-2.711730,5.866483,4.441869,-5.919670],[5.554904,-6.954424,-4.584380,-1.499156,-0.705497,3.280479,-6.449174,6.072577,1.209170,-2.603095],[4.688348,0.454563,8.855270,-3.794579,3.273830,-0.161357,7.552637,-1.795792,-4.607169,1.695132],[-1.864844,3.126198,-9.557398,-7.189500,-5.098049,-5.478328,8.577261,4.264913,-9.552325,4.796574],[3.600160,-2.728066,3.658169,-0.627996,-2.455324,-1.696722,-5.303653,9.816862,3.749011,-0.611404]],[[1.192071,7.513457,-5.084358,9.382919,-1.583879,-4.386644,1.024637,4.836340,-0.779505,-4.564134],[5.591435,1.451389,-0.955149,0.209441,-8.821032,9.588938,-1.688587,2.189818,-7.049447,1.878394],[0.125094,-8.000669,0.997948,4.745610,6.780538,-9.046347,2.689683,-8.219484,-8.104696,5.920102],[-3.745477,-7.111555,0.514487,7.531467,4.178923,0.101886,3.194237,2.819443,8.138687,-4.773103],[-2.871301,9.141703,-0.488520,-5.792554,3.796097,2.525776,-7.361931,-9.664271,9.509351,3.737546],[7.907364,-9.312047,-7.823988,8.225875,-5.281090,-1.875499,-7.869020,-4.662768,-6.277092,9.410652],[-2.713896,1.863068,7.608479,7.887450,3.209594,9.918864,4.314945,5.927935,1.419669,6.607151],[-4.125166,-0.052897,6.085029,8.960509,4.039945,-8.912793,-2.353418,2.637156,1.604357,-3.330947],[7.340301,1.201195,4.855435,7.477660,2.680997,6.833856,-0.703003,-2.889485,-0.224087,1.417883],[8.651708,-6.209327,6.670698,2.762765,-9.377064,-6.157831,7.474119,-5.808604,-0.048211,5.466872],[-9.068085,-5.924151,-2.700693,-8.239995,-8.688718,0.365722,2.208524,6.740776,7.203701,-8.245163],[6.979844,8.836877,-9.760564,7.259078,0.990700,5.690401,7.708019,7.269872,-4.992830,9.298840],[1.904257,-5.099791,-1.372294,-1.793357,-1.729281,6.396198,1.268305,-1.096973,-0.823931,-2.057234],[-5.017147,6.872823,2.528311,-9.517983,-9.643065,7.614128,-9.914372,3.905327,3.263563,-2.507720]],[[-6.020413,3.711257,-1.129042,8.027582,-7.437455,1.487201,8.318127,-1.207961,3.482248,8.963807],[-5.244244,3.448079,-5.882312,7.083437,-6.640300,-1.665894,5.039683,-4.409542,6.713357,-8.997177],[-6.391197,2.114742,-1.975349,-9.791785,-5.789438,-3.358667,-3.074657,4.046122,-9.481245,4.457736],[-6.874632,2.313617,9.401310,6.674706,5.122918,-7.469814,4.251370,-3.386329,-9.594492,1.378427],[-5.133844,0.516952,-3.613984,9.575332,-4.056760,9.310474,-8.124088,-2.807431,7.822820,2.370007],[-2.030226,-7.388380,5.198073,3.708902,9.524675,-3.789929,-8.214181,6.593258,-6.303595,8.186511],[8.868231,0.906949,6.529950,2.002768,8.347611,-4.794128,7.931848,-6.174000,1.175647,-4.807167],[-9.860800,-7.488530,-2.011469,2.511575,-0.580337,1.853504,-8.600822,-8.347469,9.938761,-1.218968],[-3.961191,-7.545166,8.869296,-9.241381,-8.001861,1.854543,7.135278,-3.559326,4.710935,-3.584349],[-8.014056,9.101831,-7.474985,3.252052,-5.979521,-3.135089,-5.519771,-0.328459,8.970808,-9.939943],[1.473124,2.022130,4.617670,-4.908495,3.347437,-8.751976,0.232508,-8.061853,2.188980,1.803146],[0.752805,-6.339525,-9.668097,0.029116,5.170711,5.701040,-8.542618,1.835492,-8.489316,-3.132434],[-2.741607,-0.960038,4.965825,4.133580,-2.411456,-4.466337,5.444188,9.472359,0.104392,2.060980],[-4.268979,0.103978,5.680290,-2.897540,-7.063597,-5.512475,8.300781,-9.745768,9.109252,-2.798561]],[[-3.841159,-7.504563,3.969136,9.322400,-2.412946,-4.390791,-0.201896,1.945262,-5.364347,8.587465],[8.127897,-0.752945,-4.357074,8.085622,-0.605589,5.163319,-0.039974,-7.491082,9.953307,-6.760172],[1.875125,-9.075342,-4.124742,3.951673,8.794613,9.308887,-8.103873,-3.113398,1.850965,1.972474],[7.983752,-8.486754,-9.400218,8.311471,1.472187,4.700180,-0.973104,-6.712226,-5.318924,-8.075405],[-7.299217,-8.804329,8.958881,-8.313492,-5.754982,-7.929519,-5.223277,2.605714,-9.342085,8.658449],[-2.082698,-4.975791,-1.232789,1.432003,-2.485214,7.669386,3.705990,-7.861343,-6.246119,3.118413],[-4.605025,-3.390509,7.072814,0.715022,-6.081254,0.144715,3.628545,-8.090110,-6.875727,-3.423570],[6.607266,9.709630,5.120294,8.748514,-4.776874,-7.720184,-3.762070,-5.186931,-3.539276,8.104620],[-2.017875,1.629351,-4.792770,4.869061,6.301595,-4.156026,8.988791,-9.657027,6.008737,-1.694170],[-0.099095,-0.878466,9.568499,-5.768077,-6.764605,3.889516,-4.629765,-7.164900,-2.214032,6.258042],[-8.712279,-8.336117,-2.692659,-7.015218,-7.639243,1.480353,-5.780629,6.519956,-9.703480,5.689516],[-8.867714,1.228796,-2.748921,4.359910,-6.060261,-6.601762,-5.559437,-9.187649,5.841514,-4.519154],[-8.036373,2.636075,6.850029,-0.591011,-9.721107,-2.646952,-2.672873,-0.099998,-5.483598,1.680983],[-3.544273,7.203499,-8.280443,4.990189,-5.661482,1.703430,-7.214416,3.236705,-2.299041,8.673805]],[[-8.335631,6.172006,-1.092366,6.249397,8.553143,8.145398,-8.503614,2.171419,-4.026675,0.658239],[-3.337433,2.529639,5.324390,1.814579,1.993358,-2.146213,-9.115451,-8.889516,7.142151,9.489906],[9.000894,2.258757,0.038959,-3.599442,9.881165,7.572334,0.934319,-8.058234,5.937846,-7.154201],[3.169095,-0.039325,-4.549254,-3.149133,-3.818966,-7.446622,-9.624291,-5.040716,-5.142632,3.044494],[-0.193419,-9.060343,-5.439991,-1.952591,-8.605249,-5.116740,4.968424,0.953549,3.287575,-9.362843],[-5.677789,8.699496,-7.770016,-0.952989,9.631426,-3.680217,-0.311947,0.072239,-8.262990,2.033253],[-9.721158,-7.472273,-6.878001,2.706556,7.956693,-0.966051,-7.275629,-9.326039,9.208767,-4.191270],[-3.045215,-6.463204,8.363743,7.954982,6.573112,-8.233586,-7.491849,8.736782,-0.391742,4.907381],[-0.800748,5.909767,6.430128,4.069983,9.147280,4.937386,5.768426,-0.009833,5.775525,-5.185300],[-9.087831,-6.719833,0.129829,-9.819173,-2.239935,1.880514,7.016778,-3.690861,-0.905157,5.128447],[5.326343,5.974403,-9.374779,7.601927,-5.134268,-0.665443,-8.102056,6.412717,-4.285308,7.635214],[1.660846,-6.129284,-7.764217,-1.360782,-1.841262,-1.165964,-3.606391,-0.883856,5.084141,5.912863],[7.079374,2.893333,-9.556742,8.276294,-6.604987,-7.979952,2.976412,-5.879561,5.071691,-6.476855],[-1.452677,6.281680,0.891274,2.012090,2.204816,-3.291975,-6.105997,-3.260849,-4.727984,1.251267]],[[-0.745655,3.408486,-0.539742,7.700684,-2.882822,-8.729999,-1.033981,3.703067,4.763863,7.715035],[0.671897,-1.519656,7.094604,6.916591,-4.227953,-5.026456,-7.564779,2.134024,2.049034,-8.416382],[-0.714219,-8.513751,-9.471919,-6.538460,-0.381574,-6.016545,6.490259,0.649947,2.214001,2.749096],[9.767330,-9.660194,4.990938,7.173485,6.228813,-8.031057,-3.242098,-4.193279,-3.841552,-5.643995],[-8.231926,2.903513,7.194426,-1.438408,3.460787,6.774861,1.220016,-7.031172,3.849559,3.173216],[8.226937,-7.438911,-1.900491,-3.011593,-0.468029,8.560957,8.135061,-1.525562,1.274808,5.080827],[-2.610914,-2.049755,-4.614674,-7.887956,-5.490135,-9.600621,4.594229,5.628446,-2.347500,4.402309],[-9.830450,5.553192,9.456828,8.911388,6.882836,2.048322,9.107055,6.195683,-4.896901,8.959752],[-5.074433,-0.826729,-3.934167,8.725480,0.272626,4.696435,-3.661581,2.506438,5.200818,-4.593001],[4.806411,-4.073133,2.268326,-6.197841,-7.799524,-9.757687,-3.634733,-1.013693,-1.056119,9.878765],[-7.404217,-7.288140,7.372854,-2.893015,-8.094055,5.882322,-8.535757,-9.630695,-3.599954,8.382170],[-6.396790,5.659158,-8.343510,1.456592,7.106670,-0.186340,-0.661745,-3.065797,-1.897731,-7.650659],[-3.376935,-2.589753,9.119499,-0.952399,-4.163593,-3.552919,-1.566089,7.867448,-1.173900,8.760528],[9.574131,9.620035,-8.828701,0.885402,7.678695,8.399112,-5.817470,-2.882586,-3.208260,3.933825]],[[7.599981,6.612140,7.492244,-4.605855,-8.957029,6.637510,-5.221465,3.507314,9.090639,8.037601],[-7.555564,-9.142706,1.502215,-1.351690,8.835473,-3.430054,-4.631444,-6.049190,-3.015066,9.375595],[1.288212,-9.769196,3.402172,-1.799334,-8.495435,9.378180,6.069008,5.119902,4.821876,-3.601970],[7.633869,4.812552,8.380580,4.232044,-1.378918,-4.421283,-0.496766,7.453270,-4.917870,-9.956146],[-7.660389,6.000820,4.738926,-4.637230,-0.710993,7.443155,6.973166,7.957119,3.962504,-9.436200],[4.607249,4.193639,9.981979,-4.667599,-1.851934,-1.308217,-6.732645,-2.273885,8.542736,-1.168669],[-0.430842,7.825285,-4.539387,-9.309901,-5.751177,-5.267248,9.932883,1.495229,-5.458020,-1.352221],[-2.192084,0.245310,-5.656454,-8.663588,-8.917469,9.557166,-4.224933,-5.685254,-0.491746,-8.742403],[1.819675,-3.559053,-6.396630,7.119200,5.274111,-0.124960,3.073759,4.708912,4.546788,7.767978],[-7.357875,-2.250131,9.849936,-1.457418,5.109330,-8.572492,6.669180,4.850222,-0.980655,-9.779776],[-4.551962,7.460959,5.018210,8.097785,-3.811899,-3.741883,-0.737141,-6.983429,-0.517893,7.520605],[2.940623,-9.872943,-5.914670,1.656443,4.038645,1.885761,-6.644039,1.583287,3.846833,-5.405920],[9.554940,-9.875966,-7.225280,7.209974,3.119457,-7.218738,7.249636,2.993792,3.842365,-2.922620],[4.141675,-6.827222,2.634680,2.466905,3.904349,-8.225741,-2.752047,-2.640768,3.815728,5.733985]],[[-5.795628,-7.844487,8.974727,1.464711,-9.856755,7.718530,3.826153,4.902183,8.970756,0.597415],[-2.726103,1.405590,5.321884,2.630122,9.236450,0.155869,3.642787,8.121657,-7.760072,6.311859],[7.179329,-6.289820,-2.206469,8.745374,-4.734226,-1.281196,-3.182186,6.563357,7.713432,1.390128],[-3.859304,-1.834562,-9.735049,-1.417266,9.850031,4.434873,-2.565975,3.045849,7.647434,-4.779159],[-7.457386,-4.680305,-0.127548,-7.711229,6.060635,-1.535439,-4.803402,7.009144,8.726815,8.137351],[9.438169,1.842106,-4.985227,-8.897188,6.074318,8.588948,-8.435753,-8.645247,-0.656008,-5.304192],[-6.141012,7.246496,-1.714678,2.925356,-2.629941,-7.717768,6.429975,7.968227,-1.269332,1.369756],[-9.745902,5.684774,0.494413,6.288055,-8.189055,7.514816,-7.319307,-1.032384,7.238199,-4.948103],[-8.110989,7.609800,-3.428543,-3.252055,-8.064985,-9.184717,-4.545672,7.151331,-0.034151,8.039343],[2.181895,7.111668,4.857353,-3.501020,-8.838996,-2.671910,1.145248,-5.403724,-2.507386,-9.661059],[1.373881,3.388214,1.532963,1.503935,0.115368,-5.298379,1.591140,7.436182,5.385106,1.792111],[-7.182258,4.466532,5.136380,-6.345814,-1.553792,-1.808389,8.237773,6.400264,4.673805,-3.268804],[-9.601719,5.219862,4.042090,-4.380919,-9.790746,-4.240590,-8.035205,-8.667656,1.596956,8.383449],[2.020300,4.784108,-0.123086,2.754983,8.237272,-1.473559,0.345390,9.852754,-1.191807,3.555132]],[[7.192379,-7.847109,3.024447,6.058567,5.483769,-2.183567,7.927896,5.668749,3.040052,3.260809],[0.379515,-0.919471,6.641737,5.894355,7.762900,-4.215140,-3.136357,-7.739359,0.003188,-4.662118],[6.788206,5.584715,8.958764,-8.591169,-9.683928,6.554233,8.689335,-2.269673,-8.180963,3.024242],[-1.063030,-9.038224,-7.813956,7.090515,5.997309,-5.789777,-1.175358,8.442996,-2.738479,-3.002881],[9.236723,-0.070846,1.478376,7.681006,-2.347637,-9.141426,-4.186367,5.425739,8.686048,-1.208206],[2.090939,3.457111,-1.777262,3.888773,-2.865648,4.553423,8.387270,3.950615,-5.852200,-9.141633],[4.633047,-2.753260,-6.283177,-7.556212,-8.428343,-3.081323,5.359645,1.375873,-9.035768,-6.368835],[6.268552,-5.090847,-7.976236,8.756297,-8.111583,1.089657,-7.285825,0.235935,-1.831082,2.281651],[-4.505635,-5.309545,7.197909,9.858255,-4.610556,3.446809,-9.085547,-2.016279,0.933328,7.207236],[-0.010475,7.535830,-0.659629,1.576334,-5.841707,5.936960,-1.024697,-7.211960,-0.822087,1.392355],[9.973145,-5.073690,-1.157440,-5.523225,-4.566703,5.140565,7.505767,-7.061867,9.577210,-9.987712],[-9.689307,-0.731597,4.678386,-0.477388,-1.154819,-9.332170,-0.297403,1.565789,8.108812,-9.435228],[-4.565276,-8.607132,-9.870452,1.790912,-1.553636,2.383595,-8.839067,8.292380,-5.646203,3.158954],[1.808566,1.196261,-4.463845,-6.424119,-2.350644,4.044149,-0.156482,-8.147114,-1.869375,-0.601280]],[[9.809227,2.674745,9.137513,1.652293,6.369303,5.191946,-5.812488,-4.490901,2.585120,1.901247],[-5.409508,-2.974747,-9.875871,9.604784,8.740259,-9.138398,-4.065301,-5.312420,-4.326794,9.501227],[-7.078510,3.096373,5.842064,2.812105,-9.093659,6.489339,6.008777,-8.740396,-9.626855,8.509232],[0.749399,3.198978,4.573112,-7.652123,9.618097,6.797405,-3.343968,2.064952,0.289975,-6.143557],[4.192361,-5.301462,-4.743503,-6.564432,-6.200122,-0.433815,4.453377,3.456633,2.626755,5.066266],[-3.816312,-3.677749,6.175426,-1.266819,-5.481317,-4.470202,-1.128286,-1.305224,6.524191,-1.765479],[-7.987143,-6.982413,-1.736499,4.462133,7.842184,-7.724879,8.980996,-0.567784,-8.289721,7.892778],[6.158085,-0.164949,-8.579674,-4.556275,-3.979237,-8.796734,4.025316,-8.562082,-9.496836,3.311174],[-9.510932,1.611187,-5.346816,-2.898133,8.057366,2.289857,-6.225867,-0.590592,9.014660,-0.778509],[4.431508,-3.872460,3.700640,-4.491355,-4.814691,1.911099,-7.297677,3.837012,-9.104999,5.852779],[3.476369,2.129615,2.054620,5.653501,-3.346844,-4.889252,-0.304016,3.530786,6.997670,2.024060],[1.490439,0.908314,-5.210482,0.714976,-0.419868,-8.746982,8.864154,2.962498,5.182980,6.713075],[4.873302,-6.569301,8.376312,8.522790,6.644198,-1.375062,-4.105165,-7.506113,-0.662567,5.138579],[5.263763,9.939039,2.310830,1.246776,0.867692,8.154476,-2.459438,-6.112964,8.008340,-7.964887]]], dtype = "float64")#candidate|2332|(11, 14, 10)|const|float64
uop_2333 = relay.atan(const_2332.astype('float64')) # shape=(11, 14, 10)
uop_2341 = relay.log10(const_2332.astype('float64')) # shape=(11, 14, 10)
func_49_call = mod.get_global_var('func_49')
func_53_call = mutated_mod.get_global_var('func_53')
var_2347 = relay.var("var_2347", dtype = "float32", shape = ())#candidate|2347|()|var|float32
var_2348 = relay.var("var_2348", dtype = "float32", shape = (1, 350))#candidate|2348|(1, 350)|var|float32
call_2346 = func_49_call(relay.reshape(var_2347.astype('float32'), []), relay.reshape(var_2348.astype('float32'), [7, 10, 5]), )
call_2349 = func_49_call(relay.reshape(var_2347.astype('float32'), []), relay.reshape(var_2348.astype('float32'), [7, 10, 5]), )
output = relay.Tuple([uop_2333,uop_2341,call_2346,var_2347,var_2348,])
output2 = relay.Tuple([uop_2333,uop_2341,call_2349,var_2347,var_2348,])
func_2354 = relay.Function([var_2347,var_2348,], output)
mod['func_2354'] = func_2354
mod = relay.transform.InferType()(mod)
var_2355 = relay.var("var_2355", dtype = "float32", shape = ())#candidate|2355|()|var|float32
var_2356 = relay.var("var_2356", dtype = "float32", shape = (1, 350))#candidate|2356|(1, 350)|var|float32
output = func_2354(var_2355,var_2356,)
func_2357 = relay.Function([var_2355,var_2356,], output)
mutated_mod['func_2357'] = func_2357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_427_call = mod.get_global_var('func_427')
func_429_call = mutated_mod.get_global_var('func_429')
call_2393 = func_427_call()
call_2394 = func_427_call()
func_2076_call = mod.get_global_var('func_2076')
func_2077_call = mutated_mod.get_global_var('func_2077')
call_2403 = relay.TupleGetItem(func_2076_call(), 1)
call_2404 = relay.TupleGetItem(func_2077_call(), 1)
output = relay.Tuple([call_2393,call_2403,])
output2 = relay.Tuple([call_2394,call_2404,])
func_2405 = relay.Function([], output)
mod['func_2405'] = func_2405
mod = relay.transform.InferType()(mod)
output = func_2405()
func_2406 = relay.Function([], output)
mutated_mod['func_2406'] = func_2406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1828_call = mod.get_global_var('func_1828')
func_1829_call = mutated_mod.get_global_var('func_1829')
call_2410 = relay.TupleGetItem(func_1828_call(), 0)
call_2411 = relay.TupleGetItem(func_1829_call(), 0)
func_1197_call = mod.get_global_var('func_1197')
func_1199_call = mutated_mod.get_global_var('func_1199')
call_2439 = relay.TupleGetItem(func_1197_call(), 1)
call_2440 = relay.TupleGetItem(func_1199_call(), 1)
uop_2441 = relay.tan(call_2410.astype('float32')) # shape=(9, 15, 4)
uop_2443 = relay.tan(call_2411.astype('float32')) # shape=(9, 15, 4)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_2465 = func_384_call()
call_2466 = func_384_call()
output = relay.Tuple([call_2439,uop_2441,call_2465,])
output2 = relay.Tuple([call_2440,uop_2443,call_2466,])
func_2471 = relay.Function([], output)
mod['func_2471'] = func_2471
mod = relay.transform.InferType()(mod)
output = func_2471()
func_2472 = relay.Function([], output)
mutated_mod['func_2472'] = func_2472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_2501 = relay.TupleGetItem(func_496_call(), 0)
call_2502 = relay.TupleGetItem(func_498_call(), 0)
output = relay.Tuple([call_2501,])
output2 = relay.Tuple([call_2502,])
func_2509 = relay.Function([], output)
mod['func_2509'] = func_2509
mod = relay.transform.InferType()(mod)
mutated_mod['func_2509'] = func_2509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2509_call = mutated_mod.get_global_var('func_2509')
call_2510 = func_2509_call()
output = call_2510
func_2511 = relay.Function([], output)
mutated_mod['func_2511'] = func_2511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_2553 = func_328_call()
call_2554 = func_328_call()
output = relay.Tuple([call_2553,])
output2 = relay.Tuple([call_2554,])
func_2565 = relay.Function([], output)
mod['func_2565'] = func_2565
mod = relay.transform.InferType()(mod)
mutated_mod['func_2565'] = func_2565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2565_call = mutated_mod.get_global_var('func_2565')
call_2566 = func_2565_call()
output = call_2566
func_2567 = relay.Function([], output)
mutated_mod['func_2567'] = func_2567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_2568 = relay.TupleGetItem(func_1931_call(), 3)
call_2569 = relay.TupleGetItem(func_1933_call(), 3)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_2579 = relay.TupleGetItem(func_2294_call(), 1)
call_2580 = relay.TupleGetItem(func_2295_call(), 1)
func_2565_call = mod.get_global_var('func_2565')
func_2567_call = mutated_mod.get_global_var('func_2567')
call_2590 = relay.TupleGetItem(func_2565_call(), 0)
call_2591 = relay.TupleGetItem(func_2567_call(), 0)
output = relay.Tuple([call_2568,call_2579,call_2590,])
output2 = relay.Tuple([call_2569,call_2580,call_2591,])
func_2601 = relay.Function([], output)
mod['func_2601'] = func_2601
mod = relay.transform.InferType()(mod)
output = func_2601()
func_2602 = relay.Function([], output)
mutated_mod['func_2602'] = func_2602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2683 = relay.var("var_2683", dtype = "float64", shape = (4, 8, 14))#candidate|2683|(4, 8, 14)|var|float64
uop_2684 = relay.atan(var_2683.astype('float64')) # shape=(4, 8, 14)
bop_2693 = relay.subtract(uop_2684.astype('uint8'), relay.reshape(var_2683.astype('uint8'), relay.shape_of(uop_2684))) # shape=(4, 8, 14)
func_2129_call = mod.get_global_var('func_2129')
func_2131_call = mutated_mod.get_global_var('func_2131')
call_2698 = relay.TupleGetItem(func_2129_call(), 0)
call_2699 = relay.TupleGetItem(func_2131_call(), 0)
func_1147_call = mod.get_global_var('func_1147')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_2701 = relay.TupleGetItem(func_1147_call(), 2)
call_2702 = relay.TupleGetItem(func_1149_call(), 2)
bop_2704 = relay.power(uop_2684.astype('float32'), relay.reshape(bop_2693.astype('float32'), relay.shape_of(uop_2684))) # shape=(4, 8, 14)
bop_2712 = relay.mod(var_2683.astype('float32'), relay.reshape(uop_2684.astype('float32'), relay.shape_of(var_2683))) # shape=(4, 8, 14)
output = relay.Tuple([call_2698,call_2701,bop_2704,bop_2712,])
output2 = relay.Tuple([call_2699,call_2702,bop_2704,bop_2712,])
func_2719 = relay.Function([var_2683,], output)
mod['func_2719'] = func_2719
mod = relay.transform.InferType()(mod)
mutated_mod['func_2719'] = func_2719
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2720 = relay.var("var_2720", dtype = "float64", shape = (4, 8, 14))#candidate|2720|(4, 8, 14)|var|float64
func_2719_call = mutated_mod.get_global_var('func_2719')
call_2721 = func_2719_call(var_2720)
output = call_2721
func_2722 = relay.Function([var_2720], output)
mutated_mod['func_2722'] = func_2722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2509_call = mod.get_global_var('func_2509')
func_2511_call = mutated_mod.get_global_var('func_2511')
call_2748 = relay.TupleGetItem(func_2509_call(), 0)
call_2749 = relay.TupleGetItem(func_2511_call(), 0)
output = call_2748
output2 = call_2749
func_2771 = relay.Function([], output)
mod['func_2771'] = func_2771
mod = relay.transform.InferType()(mod)
mutated_mod['func_2771'] = func_2771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2771_call = mutated_mod.get_global_var('func_2771')
call_2772 = func_2771_call()
output = call_2772
func_2773 = relay.Function([], output)
mutated_mod['func_2773'] = func_2773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_2774 = func_328_call()
call_2775 = func_328_call()
output = relay.Tuple([call_2774,])
output2 = relay.Tuple([call_2775,])
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
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_2804 = func_384_call()
call_2805 = func_384_call()
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_2812 = relay.TupleGetItem(func_2776_call(), 0)
call_2813 = relay.TupleGetItem(func_2778_call(), 0)
bop_2814 = relay.logical_or(call_2812.astype('bool'), relay.reshape(call_2804.astype('bool'), relay.shape_of(call_2812))) # shape=(9, 15, 4)
bop_2817 = relay.logical_or(call_2813.astype('bool'), relay.reshape(call_2805.astype('bool'), relay.shape_of(call_2813))) # shape=(9, 15, 4)
output = bop_2814
output2 = bop_2817
func_2822 = relay.Function([], output)
mod['func_2822'] = func_2822
mod = relay.transform.InferType()(mod)
output = func_2822()
func_2823 = relay.Function([], output)
mutated_mod['func_2823'] = func_2823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_427_call = mod.get_global_var('func_427')
func_429_call = mutated_mod.get_global_var('func_429')
call_2837 = func_427_call()
call_2838 = func_427_call()
const_2840 = relay.const([[[3.491262,-9.568410,7.173005,-4.206239],[4.585074,-5.757887,5.495437,2.129897],[-6.967122,-9.661576,1.144529,-7.730577],[-2.842037,2.573051,-7.458099,-4.506264],[5.671529,-1.873721,-9.837127,3.776398],[-4.019519,-8.432552,-6.916811,-6.113563],[9.434813,-7.707219,7.852186,4.035506],[-1.363416,9.261611,3.490721,-7.485974],[-2.255582,7.643121,4.460819,-5.661289],[6.750076,0.571729,6.451084,-6.152633],[-2.280436,8.041889,7.978863,4.494199],[3.017822,1.682704,-5.437417,-3.675252],[-1.356890,0.745950,-0.393846,5.976328],[0.681483,5.274631,-1.249345,1.924591],[-0.601940,-7.193980,8.651484,6.367483]],[[-0.932815,-9.789520,-5.638784,1.874238],[-2.102307,-1.475979,-5.218687,-0.351923],[-5.931641,-4.594575,-7.391926,9.733251],[6.162828,-7.374583,0.601317,7.826176],[-1.610454,-4.785744,-1.372531,9.282500],[7.729691,1.280861,9.311866,9.349927],[4.478163,-4.542097,7.136226,8.630002],[5.297617,-5.312490,0.154254,-3.482944],[5.049280,0.492559,-9.789693,-4.347842],[-6.669832,-2.253152,-9.485988,-9.421611],[7.638725,3.788375,-2.323186,1.008249],[-6.511942,1.634601,-8.070032,-4.881610],[-8.547888,4.515192,-9.179326,-9.792139],[-7.384244,7.791305,-6.692543,-7.123347],[-1.467287,5.848960,-4.427232,9.097071]],[[-3.383883,2.406499,-5.712197,-2.749315],[9.358176,-1.043885,2.458462,-9.298386],[4.865773,-8.444245,8.470594,0.267134],[-1.083444,7.764087,-8.157836,-6.784931],[9.344285,5.790676,3.696509,-7.267507],[0.055931,-5.386003,-7.246259,-7.029859],[-6.437777,4.421752,-2.356137,-4.093197],[3.955751,8.378253,-4.911926,-7.234853],[2.091218,5.883635,6.491605,4.463952],[-2.786735,-1.012984,7.643609,-5.431303],[3.766773,0.145191,3.856267,2.894743],[2.993871,-0.307334,-4.117256,4.248797],[-7.452050,-6.051567,9.742927,-6.040636],[7.446231,-2.622304,-3.985588,5.621201],[-3.531520,4.079677,-4.671183,3.480727]],[[8.174525,7.003806,-2.437901,-9.787032],[0.495104,2.151341,-9.781540,8.613447],[-3.248650,-9.427344,-1.928918,-9.105382],[7.098291,-5.033231,-3.139736,7.940639],[4.407489,2.586996,-4.059930,-9.037592],[-1.019044,-0.249613,-0.621366,3.655217],[5.635903,3.969802,9.058559,-4.285176],[1.425571,-5.950007,-8.062187,3.089076],[-0.701371,-1.473990,-1.075076,-3.945533],[-6.382973,-7.534512,-6.325098,1.313325],[3.212279,-7.840078,-6.948342,8.386258],[1.238552,-5.848158,-7.907276,-0.020571],[-1.438730,2.444164,0.919108,-3.469172],[-5.694461,-2.798927,-0.043277,-0.956691],[-6.138542,-5.947448,6.152604,-7.695066]],[[7.553114,2.860757,4.681934,-2.949358],[-2.059765,-2.620020,6.700086,3.804027],[4.650965,4.107408,3.996272,-1.337478],[-8.426390,-9.318579,-0.193294,-4.251261],[1.577130,0.172311,5.005708,1.693911],[9.082218,-9.993143,-4.227216,-0.599813],[9.060108,2.541652,6.270452,2.603410],[-1.348578,-2.748470,-8.648732,-0.201752],[-6.509813,-1.682569,7.353407,2.013136],[-7.139583,9.064149,3.975861,-0.551926],[3.227598,1.619544,4.241629,-6.991614],[-5.206498,1.978870,-0.152979,8.876227],[8.617137,-9.879235,1.806419,-9.564803],[7.323405,-5.343127,7.573782,-9.512463],[-7.078947,-3.764178,-0.227587,2.499184]],[[7.177504,9.753482,-5.677522,-4.131612],[6.218535,-0.401229,-6.029284,-5.244399],[-1.285289,-0.365422,3.540903,6.976724],[-3.234211,-8.775197,-3.650393,6.481675],[-2.640908,2.293958,5.547350,-1.341815],[6.702101,8.201303,7.226396,6.805263],[-0.700517,-6.881566,-0.765594,8.414796],[7.144308,2.703883,0.809874,7.338890],[-3.928721,-7.483418,-5.121819,-3.385001],[3.293727,8.535451,7.313988,9.912204],[-1.266051,5.990483,7.637324,1.946006],[-1.581019,-2.460012,6.346797,2.500601],[2.452087,-0.079229,2.898440,5.607751],[-9.045341,7.128185,2.011777,-6.763177],[-3.078569,6.489347,-4.732373,-6.006750]],[[8.868148,9.671219,-2.908621,-9.224534],[-4.783389,2.334043,1.217686,1.358966],[3.587718,3.064102,9.590452,-4.718953],[-6.254969,7.494472,-9.069665,1.425534],[-2.063586,1.895185,-7.518941,-7.203066],[-7.498813,-8.321347,-9.649543,5.849127],[-8.532293,8.161968,-6.167186,-2.301783],[1.507484,-8.259953,9.653628,3.438039],[-6.730502,4.650363,5.468956,8.844773],[0.915845,9.949587,4.343143,-5.603706],[-3.098666,7.342256,6.962734,0.496352],[2.636390,4.334448,7.266133,0.345911],[6.714257,-7.163837,-9.363312,-0.411859],[5.723571,-4.089378,-8.152163,5.239207],[-4.722065,-0.768600,-5.094808,-4.158061]],[[5.809061,-1.317686,-6.515877,-5.707595],[-9.055922,-1.178417,-7.639223,4.513164],[6.646104,6.722665,-2.181146,-2.856250],[4.540025,-3.282773,-4.037089,-4.842459],[-4.322333,-4.712183,-3.575336,-2.447261],[-3.693812,0.346764,1.345470,-7.891911],[-6.401767,8.899618,-6.640921,4.207761],[-5.103762,8.835001,-9.726298,-4.771465],[7.318797,-1.151187,6.238398,-7.615443],[5.597085,-7.103193,-2.522632,2.083655],[-4.474232,5.453015,-3.109414,8.814621],[3.266091,0.114777,-8.494119,-1.569079],[6.143553,5.207680,-8.729468,-9.304799],[7.763493,-2.913065,3.481956,0.574688],[-2.363171,6.100142,2.504098,4.435439]],[[4.888850,9.621574,-9.128323,5.475503],[-5.982152,-6.213694,6.444929,-6.335332],[-1.215634,-1.994619,2.324284,4.297320],[4.043096,-2.739720,0.603767,8.582926],[0.944461,-4.045001,-8.513137,5.495749],[-2.337460,1.508895,-2.162905,2.188858],[3.786649,-2.026101,6.553640,-5.062626],[-8.159418,7.157641,0.794719,7.239455],[7.873631,-4.407804,9.700933,-6.328890],[-6.499472,5.469435,-1.029003,0.862508],[3.718142,-0.664110,1.136365,3.226457],[8.174730,-6.656337,8.497894,5.760932],[6.404248,-9.525252,4.764473,1.697668],[2.382505,-5.512044,3.045443,2.139354],[-5.002847,9.744624,-0.656225,1.556632]]], dtype = "float64")#candidate|2840|(9, 15, 4)|const|float64
bop_2841 = relay.minimum(call_2837.astype('uint16'), relay.reshape(const_2840.astype('uint16'), relay.shape_of(call_2837))) # shape=(9, 15, 4)
bop_2844 = relay.minimum(call_2838.astype('uint16'), relay.reshape(const_2840.astype('uint16'), relay.shape_of(call_2838))) # shape=(9, 15, 4)
uop_2849 = relay.sin(call_2837.astype('float64')) # shape=(9, 15, 4)
uop_2851 = relay.sin(call_2838.astype('float64')) # shape=(9, 15, 4)
uop_2862 = relay.cos(uop_2849.astype('float64')) # shape=(9, 15, 4)
uop_2864 = relay.cos(uop_2851.astype('float64')) # shape=(9, 15, 4)
output = relay.Tuple([bop_2841,uop_2862,])
output2 = relay.Tuple([bop_2844,uop_2864,])
func_2865 = relay.Function([], output)
mod['func_2865'] = func_2865
mod = relay.transform.InferType()(mod)
output = func_2865()
func_2866 = relay.Function([], output)
mutated_mod['func_2866'] = func_2866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2129_call = mod.get_global_var('func_2129')
func_2131_call = mutated_mod.get_global_var('func_2131')
call_2878 = relay.TupleGetItem(func_2129_call(), 0)
call_2879 = relay.TupleGetItem(func_2131_call(), 0)
func_2509_call = mod.get_global_var('func_2509')
func_2511_call = mutated_mod.get_global_var('func_2511')
call_2880 = relay.TupleGetItem(func_2509_call(), 0)
call_2881 = relay.TupleGetItem(func_2511_call(), 0)
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_2891 = relay.TupleGetItem(func_2776_call(), 0)
call_2892 = relay.TupleGetItem(func_2778_call(), 0)
uop_2894 = relay.acosh(call_2880.astype('float64')) # shape=(9, 15, 4)
uop_2896 = relay.acosh(call_2881.astype('float64')) # shape=(9, 15, 4)
func_1490_call = mod.get_global_var('func_1490')
func_1491_call = mutated_mod.get_global_var('func_1491')
call_2907 = relay.TupleGetItem(func_1490_call(), 0)
call_2908 = relay.TupleGetItem(func_1491_call(), 0)
func_708_call = mod.get_global_var('func_708')
func_711_call = mutated_mod.get_global_var('func_711')
const_2911 = relay.const([[5,-6],[-2,-6],[-1,-3],[-1,-1],[-5,2],[2,-1],[5,-2],[3,-4],[-9,9],[3,-10],[-6,-5],[9,-9],[9,-2],[1,4],[1,-1],[-1,3],[5,-1],[-9,1],[3,-4],[6,-7],[-5,7],[-2,2],[-8,-10],[-7,-1],[4,1],[5,1],[-1,-10],[-10,-3],[-6,1],[-3,1],[-5,2],[-3,4],[-5,3],[6,7],[2,-4],[4,7],[8,-10],[-2,-2],[-2,-9],[-5,4],[-6,1],[-4,-9],[6,9],[1,-4],[6,9],[4,5],[4,-3],[-6,1],[8,6],[-2,10],[-8,-10],[7,-7],[-7,-2],[-6,7],[2,-10],[-8,2],[7,-10],[3,-7],[-7,10],[-2,-8],[3,-9],[7,-10],[-7,9],[3,1],[-9,9],[9,3],[-6,1],[-9,-8],[-8,-3],[5,6],[-4,-7],[-6,9],[9,9],[5,-7],[4,8],[8,-8],[-2,-1],[-4,7],[2,7],[4,5],[-5,5],[-6,-10],[10,-6],[3,-5],[4,-10],[-3,-6],[-4,-2],[10,-2],[-4,4],[9,10],[1,10],[-9,9],[-8,-2],[9,-5],[3,-9],[-9,-10],[10,-10],[-10,-8],[6,7],[2,-9],[-4,-1],[-8,-3],[-6,-6],[5,-5],[-3,-4],[7,6],[-2,1],[6,4],[10,2],[-4,1],[-9,-4],[-6,-1],[-7,-2],[9,-10],[-8,4],[-10,3],[-6,9],[9,-1],[-8,3],[7,1],[-9,10],[8,10],[2,9],[6,1],[-6,-3],[10,-3],[10,-10],[-2,-3],[-3,-10],[5,-8],[-5,9],[10,5],[-10,-3],[2,-9],[-4,1],[2,-8],[1,10],[7,2],[-5,-5],[-3,-3],[7,-5],[3,-5],[-7,-2],[2,-5],[-7,8],[-3,8],[-3,4],[-1,1],[2,1],[2,-2],[-2,-7],[4,9],[9,7],[-10,-9],[-6,-1],[10,9],[9,-5],[5,9],[4,6],[-10,-1],[-4,8],[-3,-9],[9,-8],[-1,9],[6,-1],[3,-10],[6,5],[1,-4],[6,1],[8,-8],[1,6],[-2,3],[10,1],[-4,2],[-9,7],[-5,-6],[-10,8],[-6,-4],[2,-10],[4,-4],[-7,-10],[10,-10],[-9,8],[7,-4],[-1,-4],[-1,-6],[8,-9],[9,-9],[-10,5],[8,-8],[4,2],[-10,-8],[-1,7],[-3,-4],[9,5]], dtype = "uint64")#candidate|2911|(195, 2)|const|uint64
call_2910 = relay.TupleGetItem(func_708_call(relay.reshape(const_2911.astype('uint64'), [390,])), 3)
call_2912 = relay.TupleGetItem(func_711_call(relay.reshape(const_2911.astype('uint64'), [390,])), 3)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_2922 = func_328_call()
call_2923 = func_328_call()
output = relay.Tuple([call_2878,call_2891,uop_2894,call_2907,call_2910,const_2911,call_2922,])
output2 = relay.Tuple([call_2879,call_2892,uop_2896,call_2908,call_2912,const_2911,call_2923,])
func_2934 = relay.Function([], output)
mod['func_2934'] = func_2934
mod = relay.transform.InferType()(mod)
mutated_mod['func_2934'] = func_2934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2934_call = mutated_mod.get_global_var('func_2934')
call_2935 = func_2934_call()
output = call_2935
func_2936 = relay.Function([], output)
mutated_mod['func_2936'] = func_2936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_2994 = relay.TupleGetItem(func_357_call(), 2)
call_2995 = relay.TupleGetItem(func_358_call(), 2)
output = relay.Tuple([call_2994,])
output2 = relay.Tuple([call_2995,])
func_3000 = relay.Function([], output)
mod['func_3000'] = func_3000
mod = relay.transform.InferType()(mod)
mutated_mod['func_3000'] = func_3000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3000_call = mutated_mod.get_global_var('func_3000')
call_3001 = func_3000_call()
output = call_3001
func_3002 = relay.Function([], output)
mutated_mod['func_3002'] = func_3002
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3021 = relay.const([[[0.300550,-6.245579,-4.391186,5.581926,5.006816,-2.729053,-4.780524,-2.412361,1.879468,-0.118909,-0.534135,8.531619,-2.824427],[-2.430819,-9.166258,-1.308309,-8.393350,-3.768060,-0.848571,-0.822805,-0.720360,6.810947,2.975993,-8.540380,-0.553999,-1.298845],[5.593113,-3.341716,-4.557601,4.287692,2.415106,-5.990042,-7.230253,-0.112873,-7.107530,1.494705,4.201686,7.348865,-0.559037],[5.053066,-3.877753,3.197549,9.134899,5.348660,3.107771,-5.316760,3.703215,-4.647001,7.253016,-8.960777,4.933029,-4.762893],[6.755089,6.927097,8.968884,-8.610346,1.964313,1.272177,-0.261681,-3.195064,-5.201612,-0.461728,-4.094607,5.660133,4.762694],[7.060923,7.951946,5.931005,-9.431566,0.032058,8.307296,5.460647,8.816427,2.250277,-5.879709,6.342297,-7.653709,-4.496595],[1.108892,-8.284070,5.567648,9.664136,9.682878,8.268564,-2.963725,7.111170,9.422435,-4.274292,4.351720,-2.725752,0.686652]],[[-4.664363,2.913760,-9.560993,1.409743,7.197225,2.954015,9.038591,1.049716,-8.086848,3.885154,7.381235,-6.694025,-3.312939],[1.707065,2.705411,-4.867322,-0.410262,-3.921647,-9.015107,9.914542,3.821322,5.003230,0.852904,1.831845,-2.438556,2.048173],[4.984892,7.200687,4.873438,-0.554548,3.534216,3.711689,-0.340856,0.971658,3.939236,-1.609010,0.755036,3.400322,-4.633546],[-2.540334,-2.283540,-1.298496,1.593497,5.062889,-2.271826,-6.932379,-5.696938,0.128999,7.680264,-8.324764,8.654915,8.083717],[-5.845838,7.009898,-9.023622,5.861360,1.179882,-2.895204,6.811531,-9.930055,-6.112261,9.590159,-3.221203,8.712969,6.168026],[-9.478398,5.610902,1.599650,-7.241621,-6.177519,-4.455393,1.292810,-5.557812,1.907662,8.159990,3.856074,-0.345336,9.433977],[-9.849755,-4.164771,-2.411401,-1.781030,8.168322,1.150894,0.302957,-9.680671,2.191384,6.817302,0.170802,0.210699,-5.188152]],[[-0.011738,9.637206,0.667838,3.459691,-7.161805,-3.192771,6.238652,-4.744507,-2.894182,-3.883774,-0.449512,-9.102757,0.036916],[-2.297753,5.877029,-8.935578,2.468817,8.866995,6.999839,-9.436176,-3.402581,-0.444724,-0.694782,-1.767040,-9.114953,6.066671],[-5.857553,0.335455,-7.060578,-9.413213,-8.358706,3.577247,-0.114157,7.623236,6.759757,9.615489,-6.791099,9.795871,3.698276],[2.200549,4.312533,-5.764187,4.209760,3.075032,6.320105,5.979145,-4.988609,5.614161,4.149534,-6.899082,-2.066023,-6.164441],[-7.995030,-8.538129,8.375212,3.271953,-2.521867,-5.137654,8.574891,6.932049,0.951895,5.912682,-6.868450,-8.368544,4.304029],[-2.224829,0.469755,-1.735703,3.094069,3.793139,6.667196,4.583828,-1.577498,7.866656,2.930267,-5.749778,0.959239,9.973786],[-4.348709,9.804420,-6.658732,1.655934,-1.208608,0.239662,-5.056060,-3.645521,-0.667173,-4.993229,4.264338,-0.510199,-1.794575]]], dtype = "float32")#candidate|3021|(3, 7, 13)|const|float32
uop_3022 = relay.log2(const_3021.astype('float32')) # shape=(3, 7, 13)
output = uop_3022
output2 = uop_3022
func_3036 = relay.Function([], output)
mod['func_3036'] = func_3036
mod = relay.transform.InferType()(mod)
output = func_3036()
func_3037 = relay.Function([], output)
mutated_mod['func_3037'] = func_3037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_3050 = func_449_call()
call_3051 = func_449_call()
var_3057 = relay.var("var_3057", dtype = "float64", shape = (9, 15, 4))#candidate|3057|(9, 15, 4)|var|float64
bop_3058 = relay.greater_equal(call_3050.astype('bool'), relay.reshape(var_3057.astype('bool'), relay.shape_of(call_3050))) # shape=(9, 15, 4)
bop_3061 = relay.greater_equal(call_3051.astype('bool'), relay.reshape(var_3057.astype('bool'), relay.shape_of(call_3051))) # shape=(9, 15, 4)
func_1166_call = mod.get_global_var('func_1166')
func_1167_call = mutated_mod.get_global_var('func_1167')
call_3063 = relay.TupleGetItem(func_1166_call(), 0)
call_3064 = relay.TupleGetItem(func_1167_call(), 0)
uop_3067 = relay.asin(var_3057.astype('float32')) # shape=(9, 15, 4)
output = relay.Tuple([bop_3058,call_3063,uop_3067,])
output2 = relay.Tuple([bop_3061,call_3064,uop_3067,])
func_3070 = relay.Function([var_3057,], output)
mod['func_3070'] = func_3070
mod = relay.transform.InferType()(mod)
var_3071 = relay.var("var_3071", dtype = "float64", shape = (9, 15, 4))#candidate|3071|(9, 15, 4)|var|float64
output = func_3070(var_3071)
func_3072 = relay.Function([var_3071], output)
mutated_mod['func_3072'] = func_3072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_3085 = func_384_call()
call_3086 = func_384_call()
func_1433_call = mod.get_global_var('func_1433')
func_1434_call = mutated_mod.get_global_var('func_1434')
call_3092 = relay.TupleGetItem(func_1433_call(), 0)
call_3093 = relay.TupleGetItem(func_1434_call(), 0)
const_3107 = relay.const([[[0.963519,6.539880,6.924219,6.592865],[8.560083,7.423691,-7.941844,-8.300178],[-7.951398,-9.792828,8.188635,-5.777623],[-0.128752,3.622774,-3.883557,7.627466],[-1.548351,-1.120814,1.995069,-1.654620],[0.728096,-5.794532,3.278018,-0.282436],[-0.846199,-3.969083,0.361361,-3.370360],[3.569165,-9.499692,-9.933670,7.511341],[-4.605968,6.478183,1.434749,-5.593315],[3.905343,9.108824,6.989615,-9.664632],[-1.812331,-5.588429,6.960737,5.635884],[-7.856680,0.357223,9.120259,7.856561],[-5.878385,3.632619,-5.431163,-2.724500],[4.249232,1.774870,4.717778,-2.570948],[-1.236204,7.926297,7.354185,-2.340873]],[[-5.009462,-9.669158,1.351879,8.721589],[-6.656965,1.685270,-1.828276,8.550977],[3.106958,3.376767,-2.405446,-3.922285],[-0.847520,6.448519,-6.107076,9.431611],[8.137498,8.885053,-7.137178,-6.866487],[9.639841,6.259161,6.901137,3.139499],[4.355860,5.452366,-2.148213,1.345295],[4.596509,-4.739832,-8.340291,1.541671],[-7.799327,-5.295552,5.776669,7.685823],[6.486309,9.420047,1.999564,3.141711],[0.343620,3.071893,9.837697,-0.798716],[0.199801,-1.210636,-2.771819,1.766824],[-9.736806,2.293697,-3.234792,4.327360],[-8.497805,-3.034904,5.938583,-8.441361],[-9.819669,6.477225,-7.657622,-6.195078]],[[-4.567766,-1.698896,-9.887475,0.411151],[3.388318,5.071878,-5.266644,6.853790],[2.119094,-0.388109,-9.059543,9.234099],[-4.265982,-2.948008,-0.455712,-4.039355],[5.390627,5.715642,-2.083065,2.000971],[-5.960056,2.489069,5.009410,5.180269],[-1.113795,6.153669,-9.027415,5.994130],[6.799079,-3.905103,8.229489,5.473755],[5.395270,-6.017665,2.741336,3.729438],[-5.785002,-3.040953,-7.906352,-6.457521],[-2.414933,9.332192,-6.773892,4.694416],[-4.753412,3.165578,4.491788,-3.846977],[-2.871486,-4.170012,-5.319987,5.293528],[7.259138,-9.537708,3.203315,-8.147426],[9.416494,-7.017253,7.442613,5.041516]],[[6.893594,3.691358,0.302242,2.435123],[-1.595187,-7.184119,-9.662106,-5.423022],[5.869496,5.243054,0.930959,-4.703020],[0.662057,8.834470,4.113183,-5.039877],[9.801455,5.622868,0.423404,-2.343609],[-0.060418,2.114186,-8.408350,-0.524600],[-7.715789,-4.984365,-1.633080,-0.161791],[-0.110639,-1.989931,3.586310,-8.473184],[-3.383447,9.407516,2.432386,8.070409],[-5.076250,-2.790800,-0.823381,6.831402],[-4.147035,3.658336,-5.609857,-8.521624],[9.698484,-0.953374,1.963008,3.668777],[-3.897590,1.916226,6.894652,-0.830154],[9.613666,-2.194095,6.691236,3.266120],[-7.239030,-0.030107,-7.830558,7.185742]],[[8.401716,-1.085061,-9.641339,-4.416237],[4.864181,-4.766970,6.856153,-3.815305],[0.974100,-8.698855,-6.980113,-6.608414],[-5.847988,-4.078434,9.181354,-4.955265],[6.297601,6.251019,7.990379,5.787503],[-2.050929,8.235663,-9.322615,-3.331961],[-2.559012,-4.546359,-1.456530,9.098412],[-1.943402,-0.808978,3.170531,-5.569941],[7.017402,0.298724,-9.493609,1.331751],[-6.728009,-0.644426,2.814745,6.544569],[4.713468,-3.963974,-6.555174,9.928420],[6.174778,9.822221,-7.536361,-3.018500],[5.544299,-5.112956,-4.325384,-4.477398],[-2.082771,6.890233,-0.259335,-3.153686],[-1.190483,1.212392,-6.786326,7.820314]],[[-4.589747,5.499877,1.558347,0.916426],[4.746126,-8.477411,5.387147,-6.462456],[0.179796,0.165985,-3.882051,6.033638],[0.677048,-7.202364,6.841326,1.884133],[-5.999054,0.370433,-6.073559,-6.868520],[-7.254694,6.638897,-6.624428,-4.942508],[3.471814,4.856096,7.887688,3.528006],[3.577246,-1.548934,9.367538,3.959525],[-4.822636,9.310553,4.836770,-3.998317],[-8.107066,7.540571,-6.176642,-3.089255],[-3.231804,4.063650,0.969414,-3.176557],[-6.160150,7.259716,-1.092910,6.041900],[4.245256,-7.001657,1.103603,1.945189],[-8.678308,-1.308271,-3.861805,2.673892],[-9.512472,-7.090228,3.715136,-2.742405]],[[4.989611,8.208233,-7.538392,9.083733],[-6.077182,-3.335708,-3.704599,7.702482],[7.202019,7.461426,2.219125,-4.348327],[-1.622170,2.184580,9.056126,5.043782],[9.597304,-5.769920,-0.821173,-8.589379],[2.360293,-5.369017,-6.840132,1.159844],[5.135248,2.079629,8.577096,-0.448155],[-1.177671,4.289577,8.791092,-6.043806],[6.302855,7.199233,-7.920549,-3.809913],[-7.764372,-0.043280,5.178121,-0.448500],[-3.231203,4.399365,3.404945,5.372836],[3.754566,3.872634,-7.497154,4.907099],[7.524325,0.999871,-5.330335,3.529333],[-1.154967,4.696579,8.882699,-8.378159],[3.590201,3.141154,7.276829,-3.932761]],[[6.226447,7.984224,-5.520418,-3.989162],[3.029250,7.609257,2.187818,4.997975],[-7.610720,4.958729,-8.581164,-5.092655],[5.108110,5.986491,-1.732263,6.138090],[7.277741,4.693658,-1.570613,5.657729],[6.802174,3.487865,-2.962357,-3.896062],[-1.109694,-9.175596,5.131733,-9.221055],[1.211985,5.035166,-2.735367,7.590461],[-9.249604,9.073033,-8.960339,-8.402340],[0.397985,5.442517,-3.655927,2.139313],[6.461625,-4.795173,-2.147873,-4.969617],[-6.890005,6.068897,-4.935110,-9.461925],[-4.056209,4.173459,9.948175,-3.146549],[-0.750158,-2.502991,-0.274020,5.522498],[1.350952,-7.371564,-3.561866,7.729528]],[[7.407720,8.993025,-2.282326,-3.182443],[1.621071,4.549287,8.290683,-1.211269],[2.668195,4.953112,-3.120475,-1.089754],[-6.115885,1.306803,2.086605,9.198231],[6.118165,-2.876530,-7.616472,-8.659430],[3.093720,-1.503851,-4.565342,-8.806303],[6.786219,5.497308,-3.381407,-1.716480],[-1.484594,8.049528,-7.118259,-1.368802],[-6.348153,4.330521,9.661940,-4.558466],[-4.038378,-7.316520,3.894961,-5.008133],[-8.765266,-9.212862,9.593854,8.993613],[-2.726966,8.753545,0.123989,4.524711],[0.809474,-0.981245,-2.938374,7.076068],[-3.869539,1.359090,-7.702067,-3.197795],[3.605046,4.354905,7.008399,7.285217]]], dtype = "float64")#candidate|3107|(9, 15, 4)|const|float64
bop_3108 = relay.logical_xor(call_3085.astype('uint64'), relay.reshape(const_3107.astype('uint64'), relay.shape_of(call_3085))) # shape=(9, 15, 4)
bop_3111 = relay.logical_xor(call_3086.astype('uint64'), relay.reshape(const_3107.astype('uint64'), relay.shape_of(call_3086))) # shape=(9, 15, 4)
func_793_call = mod.get_global_var('func_793')
func_795_call = mutated_mod.get_global_var('func_795')
call_3115 = relay.TupleGetItem(func_793_call(), 0)
call_3116 = relay.TupleGetItem(func_795_call(), 0)
output = relay.Tuple([call_3092,bop_3108,call_3115,])
output2 = relay.Tuple([call_3093,bop_3111,call_3116,])
func_3121 = relay.Function([], output)
mod['func_3121'] = func_3121
mod = relay.transform.InferType()(mod)
mutated_mod['func_3121'] = func_3121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3121_call = mutated_mod.get_global_var('func_3121')
call_3122 = func_3121_call()
output = call_3122
func_3123 = relay.Function([], output)
mutated_mod['func_3123'] = func_3123
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3130 = relay.var("var_3130", dtype = "float32", shape = (14, 2, 12))#candidate|3130|(14, 2, 12)|var|float32
uop_3131 = relay.cos(var_3130.astype('float32')) # shape=(14, 2, 12)
uop_3141 = relay.rsqrt(uop_3131.astype('float64')) # shape=(14, 2, 12)
output = relay.Tuple([uop_3141,])
output2 = relay.Tuple([uop_3141,])
func_3154 = relay.Function([var_3130,], output)
mod['func_3154'] = func_3154
mod = relay.transform.InferType()(mod)
var_3155 = relay.var("var_3155", dtype = "float32", shape = (14, 2, 12))#candidate|3155|(14, 2, 12)|var|float32
output = func_3154(var_3155)
func_3156 = relay.Function([var_3155], output)
mutated_mod['func_3156'] = func_3156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2865_call = mod.get_global_var('func_2865')
func_2866_call = mutated_mod.get_global_var('func_2866')
call_3171 = relay.TupleGetItem(func_2865_call(), 1)
call_3172 = relay.TupleGetItem(func_2866_call(), 1)
func_384_call = mod.get_global_var('func_384')
func_386_call = mutated_mod.get_global_var('func_386')
call_3175 = func_384_call()
call_3176 = func_384_call()
output = relay.Tuple([call_3171,call_3175,])
output2 = relay.Tuple([call_3172,call_3176,])
func_3183 = relay.Function([], output)
mod['func_3183'] = func_3183
mod = relay.transform.InferType()(mod)
mutated_mod['func_3183'] = func_3183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mutated_mod.get_global_var('func_3183')
call_3184 = func_3183_call()
output = call_3184
func_3185 = relay.Function([], output)
mutated_mod['func_3185'] = func_3185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_3212 = relay.TupleGetItem(func_496_call(), 1)
call_3213 = relay.TupleGetItem(func_498_call(), 1)
output = relay.Tuple([call_3212,])
output2 = relay.Tuple([call_3213,])
func_3216 = relay.Function([], output)
mod['func_3216'] = func_3216
mod = relay.transform.InferType()(mod)
output = func_3216()
func_3217 = relay.Function([], output)
mutated_mod['func_3217'] = func_3217
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3225 = relay.const([[[-8,9,1],[-7,-3,-1],[4,-8,10],[-9,1,3],[-8,2,-7],[-7,6,-9],[3,-3,-4],[-9,-8,-5],[1,9,-7],[-7,-5,1],[2,9,4],[-6,1,-5],[-6,5,3]],[[2,4,-7],[4,-8,-3],[-3,6,4],[9,7,9],[-4,10,9],[-9,-9,-2],[6,8,-7],[2,5,-3],[10,-9,1],[-10,-3,6],[6,-4,-10],[3,4,-9],[-4,2,-1]],[[-8,-6,-7],[-7,6,9],[-3,-9,4],[-3,3,-8],[-10,-3,2],[9,4,-9],[4,8,-9],[4,-6,8],[10,4,-1],[-8,-5,-3],[-5,-6,-10],[10,2,-6],[6,2,-10]],[[-9,4,-6],[8,-5,-4],[-9,-3,-10],[2,8,5],[-5,-3,3],[9,-4,7],[-9,-3,-7],[5,8,1],[-10,5,6],[-2,-2,-10],[-8,9,4],[-3,5,9],[5,-10,-1]],[[-2,-3,-3],[-8,2,9],[9,10,1],[-7,7,10],[-4,10,-1],[-4,-6,-9],[-7,-3,1],[10,-9,-7],[6,-5,-6],[9,-2,-5],[-3,-6,-7],[7,6,-3],[-2,-6,-5]],[[1,8,2],[-3,-5,3],[-9,-8,-5],[-2,7,2],[4,4,5],[4,9,-4],[-6,-6,-1],[9,-5,-7],[-2,-3,-8],[10,9,1],[-3,1,-6],[7,-3,3],[1,-6,-10]],[[7,3,-10],[2,-4,-4],[-6,1,-1],[4,1,2],[-3,-7,-9],[3,9,-5],[6,9,-2],[-6,-1,6],[4,-1,-9],[-8,-6,-1],[-1,5,10],[-9,1,8],[-2,-10,9]],[[-7,7,-7],[-1,-9,9],[-5,2,-2],[-10,-9,-10],[2,1,-5],[9,-3,-9],[3,7,-8],[1,9,-1],[-8,-6,2],[5,-10,-8],[-7,8,-3],[2,9,-9],[-8,-10,6]],[[9,-4,10],[-3,-2,1],[7,-4,8],[1,5,-1],[-7,-7,-7],[-10,-8,3],[2,2,8],[-3,1,-1],[-7,1,2],[-8,-3,8],[1,-6,4],[-6,-5,10],[4,-10,1]],[[6,-4,1],[10,-7,-6],[3,-4,-4],[-10,7,-9],[-3,-2,-7],[-6,10,1],[8,-1,-6],[-1,-4,-10],[3,9,9],[7,-2,-5],[-2,2,-3],[-5,4,-5],[5,-9,-10]]], dtype = "uint16")#candidate|3225|(10, 13, 3)|const|uint16
var_3226 = relay.var("var_3226", dtype = "uint16", shape = (10, 13, 3))#candidate|3226|(10, 13, 3)|var|uint16
bop_3227 = relay.bitwise_xor(const_3225.astype('uint16'), relay.reshape(var_3226.astype('uint16'), relay.shape_of(const_3225))) # shape=(10, 13, 3)
uop_3230 = relay.exp(const_3225.astype('float64')) # shape=(10, 13, 3)
uop_3234 = relay.acos(uop_3230.astype('float64')) # shape=(10, 13, 3)
func_1114_call = mod.get_global_var('func_1114')
func_1118_call = mutated_mod.get_global_var('func_1118')
var_3244 = relay.var("var_3244", dtype = "int16", shape = (60,))#candidate|3244|(60,)|var|int16
var_3245 = relay.var("var_3245", dtype = "int16", shape = (12, 50))#candidate|3245|(12, 50)|var|int16
call_3243 = relay.TupleGetItem(func_1114_call(relay.reshape(var_3244.astype('int16'), [1, 5, 12]), relay.reshape(var_3245.astype('int16'), [10, 5, 12]), ), 4)
call_3246 = relay.TupleGetItem(func_1118_call(relay.reshape(var_3244.astype('int16'), [1, 5, 12]), relay.reshape(var_3245.astype('int16'), [10, 5, 12]), ), 4)
func_1802_call = mod.get_global_var('func_1802')
func_1807_call = mutated_mod.get_global_var('func_1807')
var_3260 = relay.var("var_3260", dtype = "float32", shape = (20,))#candidate|3260|(20,)|var|float32
const_3261 = relay.const([-2.434742,-7.281116,3.017562,-2.650405,-1.238609,5.364053,-9.854182,-8.629999,8.898430,-6.230677,7.917770,1.776538,5.713692,1.638279,6.614905,-0.189460,-3.528593,9.264535,-8.772919,-3.844462,-1.861816,6.096467,3.476791,-8.861956,5.939633,8.594319,4.489342,-8.776671,-7.551277,0.567202,-3.622101,1.912223,-8.144257,-4.213755,4.466170,1.933697,6.658085,-4.917201,3.503912,7.458067,-1.560997,1.747775,6.966184,-1.139221,7.373165,4.541149,-7.619406,-4.567094,-8.137119,6.787159,-8.037160,7.284383,5.564899,-4.280758,-0.648203,1.217425,-3.868036,-3.531661,-6.100221,-3.459191,-3.998211,-6.945948,-4.662661,-2.087315,2.811921,-4.974356,-2.031583,4.850412,-8.518053,-1.031954,-6.790297,4.465010,-7.528445,-9.111567,-6.047498,-9.848877,4.025323,3.965366,-6.428534,-3.632517,-0.053001,4.459478,-2.210233,-0.738353,-6.260166,1.021138,8.825511,-3.122196,-5.696741,-3.470023,6.184253,4.622305,2.967015,-5.029697,-2.417829,-2.690052,-5.749399,-6.319176,-4.399048,1.935526,1.812826,3.073280,6.177374,6.732564,5.460272,-1.617877,-5.552173,7.018126,2.642511,2.819902,-0.947842,-5.057697,4.041931,3.916736,2.119463,9.683672,0.856661,9.224797,-3.593966,-5.493551,4.571764,-6.281146,-0.295915,0.650863,4.468797,-8.209851,-3.803672,-8.520513,9.461203,-5.698178,-9.460373,6.553179,-0.954095,-6.368906,2.493894,-2.837411,-9.912488,1.316635,-5.868720,-8.966816,3.359598,9.106563,8.135568,-5.339513,4.739228,4.288397,-2.635841,5.819763,-5.096457,7.144266,-2.651807,-0.846831,-2.216918,-0.518121,-1.431221,-8.954638,0.116144,-7.543654,-8.711456,8.223614,4.239343,4.619631,5.077964,-2.292874,6.994983,-6.115841,-5.337897,-3.759203,-4.545477,7.452623,5.927183,-9.548105,-3.839309,9.856957,5.347183,-0.641683,4.854823,-0.021356,6.969535,-8.070777], dtype = "float64")#candidate|3261|(180,)|const|float64
call_3259 = relay.TupleGetItem(func_1802_call(relay.reshape(var_3260.astype('float32'), [10, 2, 1]), relay.reshape(call_3243.astype('float64'), [9, 15, 4]), relay.reshape(uop_3234.astype('uint64'), [65, 6]), relay.reshape(const_3261.astype('float64'), [10, 2, 9]), ), 6)
call_3262 = relay.TupleGetItem(func_1807_call(relay.reshape(var_3260.astype('float32'), [10, 2, 1]), relay.reshape(call_3243.astype('float64'), [9, 15, 4]), relay.reshape(uop_3234.astype('uint64'), [65, 6]), relay.reshape(const_3261.astype('float64'), [10, 2, 9]), ), 6)
output = relay.Tuple([bop_3227,uop_3234,call_3243,var_3244,var_3245,call_3259,var_3260,const_3261,])
output2 = relay.Tuple([bop_3227,uop_3234,call_3246,var_3244,var_3245,call_3262,var_3260,const_3261,])
func_3269 = relay.Function([var_3226,var_3244,var_3245,var_3260,], output)
mod['func_3269'] = func_3269
mod = relay.transform.InferType()(mod)
mutated_mod['func_3269'] = func_3269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3269_call = mutated_mod.get_global_var('func_3269')
var_3271 = relay.var("var_3271", dtype = "uint16", shape = (10, 13, 3))#candidate|3271|(10, 13, 3)|var|uint16
var_3272 = relay.var("var_3272", dtype = "int16", shape = (60,))#candidate|3272|(60,)|var|int16
var_3273 = relay.var("var_3273", dtype = "int16", shape = (12, 50))#candidate|3273|(12, 50)|var|int16
var_3274 = relay.var("var_3274", dtype = "float32", shape = (20,))#candidate|3274|(20,)|var|float32
call_3270 = func_3269_call(var_3271,var_3272,var_3273,var_3274,)
output = call_3270
func_3275 = relay.Function([var_3271,var_3272,var_3273,var_3274,], output)
mutated_mod['func_3275'] = func_3275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_3296 = relay.TupleGetItem(func_2601_call(), 1)
call_3297 = relay.TupleGetItem(func_2602_call(), 1)
func_1802_call = mod.get_global_var('func_1802')
func_1807_call = mutated_mod.get_global_var('func_1807')
const_3308 = relay.const([[8.307751,-9.656866,-3.378428,-0.439587,-3.502631,-4.411256,-4.669744,4.801790,-4.361617,6.590813,-4.473669,-3.292882,-4.360349,-3.766053,-1.315790,-8.534818,8.726874,-9.943210,-1.933431,-3.125200]], dtype = "float32")#candidate|3308|(1, 20)|const|float32
var_3309 = relay.var("var_3309", dtype = "uint64", shape = (390, 1))#candidate|3309|(390, 1)|var|uint64
const_3310 = relay.const([8.804111,3.051568,-8.411743,8.751323,-7.480557,-4.082026,-0.906972,3.041976,2.540907,6.740798,-4.671806,6.566792,2.872342,2.876503,6.232998,-6.551063,8.264432,-7.675709,3.989949,-8.849432,-7.027909,-5.766671,-7.715318,9.688891,3.330816,-0.354670,-8.452712,5.706785,5.300453,-2.500821,9.604840,-7.923412,0.597826,-0.473112,-1.321339,-0.396488,7.288272,8.145507,-1.927051,-6.594802,5.060003,-1.267512,-3.384645,7.994140,-2.163906,-0.191417,4.855492,-7.333260,0.744376,6.881974,-4.790521,-2.751396,-5.890319,3.045853,-3.558928,6.382389,-3.259594,0.930475,8.022353,0.083879,8.353304,3.754408,-8.949822,9.032713,0.745602,7.353577,-4.707961,4.903498,8.005188,6.922066,-0.330801,3.099544,-1.062481,5.916421,2.420242,-7.542219,-5.754672,5.184813,4.778537,1.157116,-5.404413,-8.064375,-4.687676,8.230822,-8.098004,-1.151404,9.599363,-5.513573,-0.477413,1.515340,-8.206022,-8.071044,-4.597723,4.200520,-0.567847,-8.372847,6.261526,6.121798,-8.680778,1.417451,-5.155611,-5.816664,9.694589,4.412784,-9.979456,5.083740,-7.699034,-9.592378,-5.370429,1.945896,-9.156481,3.652679,-8.544341,1.873849,7.661759,-1.992952,-2.531193,-6.358232,1.718748,-5.677085,-2.743518,-6.462421,3.713262,3.151705,-4.848552,7.188297,-3.327777,-7.906922,8.003142,-4.838592,-3.280362,-7.474003,1.204166,-8.291793,0.382207,-1.871764,-9.269022,-7.088619,0.767530,5.656983,-1.797539,-1.167044,0.245422,-7.452536,1.154894,-1.791287,2.947206,-0.530894,2.620407,1.542522,8.999988,-6.204987,-6.146585,-5.957251,5.132675,7.199329,-5.797075,-4.654096,-3.269202,-3.619880,5.490837,9.328217,-1.254962,5.500200,-4.380540,-0.272425,2.752484,8.812426,5.726948,9.994620,-3.055376,4.850825,5.036493,-4.852004,-8.709146,0.900778,0.882084,-9.734591,-3.499751,2.450062], dtype = "float64")#candidate|3310|(180,)|const|float64
call_3307 = relay.TupleGetItem(func_1802_call(relay.reshape(const_3308.astype('float32'), [10, 2, 1]), relay.reshape(call_3296.astype('float64'), [9, 15, 4]), relay.reshape(var_3309.astype('uint64'), [65, 6]), relay.reshape(const_3310.astype('float64'), [10, 2, 9]), ), 0)
call_3311 = relay.TupleGetItem(func_1807_call(relay.reshape(const_3308.astype('float32'), [10, 2, 1]), relay.reshape(call_3296.astype('float64'), [9, 15, 4]), relay.reshape(var_3309.astype('uint64'), [65, 6]), relay.reshape(const_3310.astype('float64'), [10, 2, 9]), ), 0)
var_3320 = relay.var("var_3320", dtype = "float64", shape = (9, 15, 4))#candidate|3320|(9, 15, 4)|var|float64
bop_3321 = relay.mod(call_3296.astype('float32'), relay.reshape(var_3320.astype('float32'), relay.shape_of(call_3296))) # shape=(9, 15, 4)
bop_3324 = relay.mod(call_3297.astype('float32'), relay.reshape(var_3320.astype('float32'), relay.shape_of(call_3297))) # shape=(9, 15, 4)
bop_3331 = relay.mod(const_3310.astype('float32'), var_3309.astype('float32')) # shape=(390, 180)
uop_3343 = relay.log2(bop_3321.astype('float32')) # shape=(9, 15, 4)
uop_3345 = relay.log2(bop_3324.astype('float32')) # shape=(9, 15, 4)
func_2509_call = mod.get_global_var('func_2509')
func_2511_call = mutated_mod.get_global_var('func_2511')
call_3351 = relay.TupleGetItem(func_2509_call(), 0)
call_3352 = relay.TupleGetItem(func_2511_call(), 0)
func_49_call = mod.get_global_var('func_49')
func_53_call = mutated_mod.get_global_var('func_53')
const_3354 = relay.const(6.388898, dtype = "float32")#candidate|3354|()|const|float32
const_3355 = relay.const([[-4.646572],[-6.435167],[-9.339576],[2.811808],[-6.592378],[-7.267081],[4.544155],[-7.123876],[0.710613],[-3.065333],[-7.395728],[1.109371],[-8.136700],[-9.032815],[5.328724],[-1.631936],[-9.959536],[-2.281652],[3.213255],[2.733433],[-7.703534],[-3.164038],[-9.182438],[9.842411],[-8.799538],[-1.029165],[3.389565],[-3.525089],[0.288856],[-4.337096],[8.646560],[-0.692411],[-7.523972],[-9.662073],[6.450346],[1.515947],[4.464531],[2.149620],[-1.995827],[6.354091],[-3.547064],[-3.896929],[-5.596447],[9.107429],[7.663092],[-0.354236],[-3.259926],[-0.330684],[8.130786],[-9.154628],[1.172797],[-6.907726],[4.169950],[-3.113756],[-3.008437],[-6.183497],[-5.408374],[-2.477852],[9.607268],[-9.740487],[4.799752],[2.583232],[9.426344],[-5.676045],[-1.579188],[5.639249],[6.225622],[-9.434721],[5.840144],[-3.037357],[4.499063],[6.724361],[3.059220],[-0.981114],[1.949493],[-3.536706],[4.418060],[3.857299],[9.477077],[9.024935],[-9.405656],[2.042491],[-1.740452],[6.290013],[3.300748],[9.841304],[-3.699457],[-3.035660],[-2.833056],[7.332391],[6.120025],[-1.429939],[7.411958],[1.614551],[-8.714348],[2.191840],[-9.953074],[-0.436235],[-5.715049],[-4.080292],[0.439291],[-5.131958],[-8.742088],[-3.318711],[6.950699],[4.246544],[4.211816],[5.660409],[4.588490],[8.146590],[9.411951],[-5.689567],[-0.066280],[-0.414827],[-4.753518],[-0.217965],[-7.550472],[-9.177060],[6.140631],[0.712003],[-9.389976],[7.675472],[3.927613],[-8.215297],[5.760410],[-1.452243],[-2.803697],[-2.128180],[8.429300],[-4.004892],[-0.646524],[8.162689],[4.008011],[0.028224],[-4.687038],[-6.933210],[5.158691],[-4.376710],[-0.225421],[1.883417],[3.085614],[2.717625],[0.894164],[-8.737182],[-6.931613],[-9.167741],[3.355702],[-3.422273],[3.663580],[4.939301],[-7.887208],[-7.473243],[8.195601],[-0.625078],[-4.300096],[0.857654],[4.628350],[7.403691],[2.985935],[1.106583],[-0.474354],[-9.262674],[-2.406236],[7.189147],[-4.650088],[8.068737],[-0.643530],[7.053426],[7.212512],[5.543583],[5.448749],[0.272700],[1.403331],[6.399281],[-5.585754],[4.131423],[9.997293],[-1.808814],[-4.813643],[2.555949],[-9.436126],[9.441656],[0.066583],[-9.423174],[1.968754],[-9.909681],[-6.531500],[5.594013],[-4.344035],[-0.617095],[-6.026947],[-6.314281],[0.595885],[3.552398],[-1.424796],[2.761798],[4.951958],[6.638652],[6.583559],[8.030131],[7.971438],[8.505304],[0.499707],[-6.124172],[-8.873757],[-5.980809],[-2.679906],[-4.130175],[9.633331],[3.080593],[-8.848331],[-7.332902],[7.818735],[-5.125921],[7.935938],[9.810314],[6.580919],[5.968901],[-5.082197],[8.812172],[-5.785668],[1.305412],[-5.377166],[7.676166],[9.504505],[2.432052],[3.887102],[1.665215],[7.263989],[0.903284],[-7.691152],[6.450877],[4.775169],[-8.918653],[-0.312070],[-7.381495],[-8.340749],[7.321276],[0.289423],[-5.185876],[5.937601],[9.676539],[-6.093055],[-6.263960],[-3.243608],[-0.413992],[-3.861049],[1.127580],[-0.147219],[8.627228],[1.456728],[-1.098557],[8.703726],[-4.733110],[-4.312922],[2.419649],[-4.387059],[-8.702443],[-7.278266],[-1.599282],[-1.082042],[8.401171],[-4.132695],[-3.840616],[-7.023665],[-1.589943],[-7.983781],[1.476730],[-0.190507],[-3.855440],[6.971129],[5.175258],[-5.950340],[-3.633598],[-1.902127],[-5.146267],[0.613441],[1.482863],[-7.151376],[9.940230],[-0.808792],[-5.149827],[-6.724853],[-5.331758],[9.601874],[6.259935],[3.756202],[-6.265507],[-7.766175],[-1.450001],[0.238188],[2.801741],[-1.767587],[-9.021318],[-1.295587],[4.365020],[2.724545],[4.606758],[-5.133226],[7.740356],[4.302857],[-2.959976],[5.174409],[-0.882954],[7.019607],[-3.139128],[4.340872],[4.175094],[-9.709593],[-0.470276],[6.624595],[9.404010],[5.498387],[-8.495299],[3.274811],[3.643371],[-9.482660],[6.470990],[-2.907278],[9.527664],[-4.292858],[-0.447056],[0.659826],[9.769547],[-2.774393],[0.051309],[7.651187],[-9.132581],[2.477957],[-4.466304],[-2.672890],[2.897821],[6.400625],[-3.354961],[9.630092],[1.287578],[9.774562],[3.383651],[-1.927557],[2.880220],[9.000750],[-2.842836],[5.923519],[0.943331],[-1.469242],[7.381350],[-1.744761],[0.608710],[8.261901],[4.317810]], dtype = "float32")#candidate|3355|(350, 1)|const|float32
call_3353 = func_49_call(relay.reshape(const_3354.astype('float32'), []), relay.reshape(const_3355.astype('float32'), [7, 10, 5]), )
call_3356 = func_49_call(relay.reshape(const_3354.astype('float32'), []), relay.reshape(const_3355.astype('float32'), [7, 10, 5]), )
uop_3358 = relay.rsqrt(uop_3343.astype('float32')) # shape=(9, 15, 4)
uop_3360 = relay.rsqrt(uop_3345.astype('float32')) # shape=(9, 15, 4)
output = relay.Tuple([call_3307,const_3308,bop_3331,call_3351,call_3353,const_3354,const_3355,uop_3358,])
output2 = relay.Tuple([call_3311,const_3308,bop_3331,call_3352,call_3356,const_3354,const_3355,uop_3360,])
func_3364 = relay.Function([var_3309,var_3320,], output)
mod['func_3364'] = func_3364
mod = relay.transform.InferType()(mod)
mutated_mod['func_3364'] = func_3364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3364_call = mutated_mod.get_global_var('func_3364')
var_3366 = relay.var("var_3366", dtype = "uint64", shape = (390, 1))#candidate|3366|(390, 1)|var|uint64
var_3367 = relay.var("var_3367", dtype = "float64", shape = (9, 15, 4))#candidate|3367|(9, 15, 4)|var|float64
call_3365 = func_3364_call(var_3366,var_3367,)
output = call_3365
func_3368 = relay.Function([var_3366,var_3367,], output)
mutated_mod['func_3368'] = func_3368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1147_call = mod.get_global_var('func_1147')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_3370 = relay.TupleGetItem(func_1147_call(), 2)
call_3371 = relay.TupleGetItem(func_1149_call(), 2)
output = relay.Tuple([call_3370,])
output2 = relay.Tuple([call_3371,])
func_3376 = relay.Function([], output)
mod['func_3376'] = func_3376
mod = relay.transform.InferType()(mod)
mutated_mod['func_3376'] = func_3376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3376_call = mutated_mod.get_global_var('func_3376')
call_3377 = func_3376_call()
output = call_3377
func_3378 = relay.Function([], output)
mutated_mod['func_3378'] = func_3378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2822_call = mod.get_global_var('func_2822')
func_2823_call = mutated_mod.get_global_var('func_2823')
call_3487 = func_2822_call()
call_3488 = func_2822_call()
output = call_3487
output2 = call_3488
func_3504 = relay.Function([], output)
mod['func_3504'] = func_3504
mod = relay.transform.InferType()(mod)
output = func_3504()
func_3505 = relay.Function([], output)
mutated_mod['func_3505'] = func_3505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1166_call = mod.get_global_var('func_1166')
func_1167_call = mutated_mod.get_global_var('func_1167')
call_3512 = relay.TupleGetItem(func_1166_call(), 0)
call_3513 = relay.TupleGetItem(func_1167_call(), 0)
output = relay.Tuple([call_3512,])
output2 = relay.Tuple([call_3513,])
func_3516 = relay.Function([], output)
mod['func_3516'] = func_3516
mod = relay.transform.InferType()(mod)
mutated_mod['func_3516'] = func_3516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3516_call = mutated_mod.get_global_var('func_3516')
call_3517 = func_3516_call()
output = call_3517
func_3518 = relay.Function([], output)
mutated_mod['func_3518'] = func_3518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_3523 = relay.TupleGetItem(func_661_call(), 0)
call_3524 = relay.TupleGetItem(func_663_call(), 0)
func_3364_call = mod.get_global_var('func_3364')
func_3368_call = mutated_mod.get_global_var('func_3368')
const_3542 = relay.const([[-7,-7],[9,10],[5,-8],[-4,9],[-1,6],[-2,7],[1,8],[6,-5],[5,1],[-7,5],[-4,-6],[10,-8],[-4,10],[-1,6],[3,-9],[-3,3],[4,5],[6,-5],[3,-3],[-9,-5],[-5,8],[4,-7],[-9,-7],[9,-2],[5,-6],[5,3],[3,2],[-5,6],[4,6],[-10,-4],[-9,3],[2,-3],[-1,7],[-10,-6],[6,-4],[7,-3],[-6,8],[3,-4],[4,4],[-3,10],[-8,1],[-7,1],[-9,8],[-7,-6],[1,-6],[7,-9],[-9,4],[10,7],[-2,5],[7,5],[-1,1],[-6,-10],[2,-1],[9,-7],[-5,-2],[6,-2],[-10,-8],[-3,3],[7,-3],[-3,-10],[-10,-4],[-5,9],[2,4],[1,-6],[2,-9],[6,10],[-8,-6],[7,-7],[-9,10],[-2,3],[-10,-1],[2,3],[-9,9],[-4,1],[-6,-4],[3,4],[10,7],[2,-5],[-6,3],[-4,-9],[1,-2],[-1,-7],[-8,-1],[-2,-4],[-6,-6],[10,1],[10,1],[2,-8],[-2,-8],[-3,-9],[7,3],[-5,-6],[7,-1],[3,-4],[-8,6],[-7,-5],[-7,1],[9,1],[1,7],[-1,1],[3,9],[-4,9],[-8,-3],[1,5],[10,-8],[-7,5],[4,-6],[-3,5],[8,3],[4,5],[-1,8],[-6,-2],[8,-5],[10,5],[-10,-9],[7,-10],[-5,-7],[9,3],[-10,-3],[-4,5],[6,7],[8,10],[-2,-2],[2,-3],[6,-7],[4,6],[3,-2],[-4,-8],[-7,-8],[6,2],[8,8],[7,-8],[3,-10],[7,1],[-7,6],[-2,-4],[1,3],[-10,7],[8,-8],[7,9],[-3,-7],[7,10],[-4,7],[-3,4],[-5,-3],[-1,-4],[8,-5],[-10,-4],[-5,3],[2,-8],[-2,-10],[-8,-10],[1,-7],[-6,3],[-3,-8],[5,5],[-5,-4],[2,1],[6,10],[8,-6],[-3,-3],[-6,-2],[7,3],[2,-3],[-6,3],[-6,-3],[-8,10],[-3,6],[1,-7],[-8,-5],[7,-10],[-6,5],[10,2],[-10,10],[-10,-5],[7,10],[-3,-5],[6,-9],[-10,1],[1,-9],[-3,9],[-8,3],[-9,2],[2,-8],[-1,-7],[4,1],[6,-9],[-9,10],[-9,-5],[-7,-6],[9,-4],[2,-5],[4,-1],[9,-2],[7,3]], dtype = "uint64")#candidate|3542|(195, 2)|const|uint64
call_3541 = relay.TupleGetItem(func_3364_call(relay.reshape(const_3542.astype('uint64'), [390, 1]), relay.reshape(call_3523.astype('float64'), [9, 15, 4]), ), 0)
call_3543 = relay.TupleGetItem(func_3368_call(relay.reshape(const_3542.astype('uint64'), [390, 1]), relay.reshape(call_3523.astype('float64'), [9, 15, 4]), ), 0)
output = relay.Tuple([call_3523,call_3541,const_3542,])
output2 = relay.Tuple([call_3524,call_3543,const_3542,])
func_3561 = relay.Function([], output)
mod['func_3561'] = func_3561
mod = relay.transform.InferType()(mod)
output = func_3561()
func_3562 = relay.Function([], output)
mutated_mod['func_3562'] = func_3562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_3563 = relay.TupleGetItem(func_357_call(), 0)
call_3564 = relay.TupleGetItem(func_358_call(), 0)
output = relay.Tuple([call_3563,])
output2 = relay.Tuple([call_3564,])
func_3566 = relay.Function([], output)
mod['func_3566'] = func_3566
mod = relay.transform.InferType()(mod)
mutated_mod['func_3566'] = func_3566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3566_call = mutated_mod.get_global_var('func_3566')
call_3567 = func_3566_call()
output = call_3567
func_3568 = relay.Function([], output)
mutated_mod['func_3568'] = func_3568
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3688 = relay.var("var_3688", dtype = "float32", shape = (4, 4, 13))#candidate|3688|(4, 4, 13)|var|float32
uop_3689 = relay.exp(var_3688.astype('float32')) # shape=(4, 4, 13)
func_2719_call = mod.get_global_var('func_2719')
func_2722_call = mutated_mod.get_global_var('func_2722')
var_3697 = relay.var("var_3697", dtype = "float64", shape = (224, 2))#candidate|3697|(224, 2)|var|float64
call_3696 = relay.TupleGetItem(func_2719_call(relay.reshape(var_3697.astype('float64'), [4, 8, 14])), 3)
call_3698 = relay.TupleGetItem(func_2722_call(relay.reshape(var_3697.astype('float64'), [4, 8, 14])), 3)
output = relay.Tuple([uop_3689,call_3696,var_3697,])
output2 = relay.Tuple([uop_3689,call_3698,var_3697,])
func_3699 = relay.Function([var_3688,var_3697,], output)
mod['func_3699'] = func_3699
mod = relay.transform.InferType()(mod)
var_3700 = relay.var("var_3700", dtype = "float32", shape = (4, 4, 13))#candidate|3700|(4, 4, 13)|var|float32
var_3701 = relay.var("var_3701", dtype = "float64", shape = (224, 2))#candidate|3701|(224, 2)|var|float64
output = func_3699(var_3700,var_3701,)
func_3702 = relay.Function([var_3700,var_3701,], output)
mutated_mod['func_3702'] = func_3702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1298_call = mod.get_global_var('func_1298')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_3744 = relay.TupleGetItem(func_1298_call(), 1)
call_3745 = relay.TupleGetItem(func_1300_call(), 1)
var_3769 = relay.var("var_3769", dtype = "float64", shape = (9, 15, 4))#candidate|3769|(9, 15, 4)|var|float64
bop_3770 = relay.greater(call_3744.astype('bool'), relay.reshape(var_3769.astype('bool'), relay.shape_of(call_3744))) # shape=(9, 15, 4)
bop_3773 = relay.greater(call_3745.astype('bool'), relay.reshape(var_3769.astype('bool'), relay.shape_of(call_3745))) # shape=(9, 15, 4)
output = bop_3770
output2 = bop_3773
func_3794 = relay.Function([var_3769,], output)
mod['func_3794'] = func_3794
mod = relay.transform.InferType()(mod)
var_3795 = relay.var("var_3795", dtype = "float64", shape = (9, 15, 4))#candidate|3795|(9, 15, 4)|var|float64
output = func_3794(var_3795)
func_3796 = relay.Function([var_3795], output)
mutated_mod['func_3796'] = func_3796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_3867 = relay.TupleGetItem(func_3183_call(), 0)
call_3868 = relay.TupleGetItem(func_3185_call(), 0)
var_3877 = relay.var("var_3877", dtype = "float64", shape = (9, 15, 4))#candidate|3877|(9, 15, 4)|var|float64
bop_3878 = relay.less(call_3867.astype('bool'), relay.reshape(var_3877.astype('bool'), relay.shape_of(call_3867))) # shape=(9, 15, 4)
bop_3881 = relay.less(call_3868.astype('bool'), relay.reshape(var_3877.astype('bool'), relay.shape_of(call_3868))) # shape=(9, 15, 4)
output = bop_3878
output2 = bop_3881
func_3883 = relay.Function([var_3877,], output)
mod['func_3883'] = func_3883
mod = relay.transform.InferType()(mod)
var_3884 = relay.var("var_3884", dtype = "float64", shape = (9, 15, 4))#candidate|3884|(9, 15, 4)|var|float64
output = func_3883(var_3884)
func_3885 = relay.Function([var_3884], output)
mutated_mod['func_3885'] = func_3885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1875_call = mod.get_global_var('func_1875')
func_1876_call = mutated_mod.get_global_var('func_1876')
call_3893 = relay.TupleGetItem(func_1875_call(), 0)
call_3894 = relay.TupleGetItem(func_1876_call(), 0)
uop_3900 = relay.atan(call_3893.astype('float32')) # shape=(9, 15, 4)
uop_3902 = relay.atan(call_3894.astype('float32')) # shape=(9, 15, 4)
output = relay.Tuple([uop_3900,])
output2 = relay.Tuple([uop_3902,])
func_3920 = relay.Function([], output)
mod['func_3920'] = func_3920
mod = relay.transform.InferType()(mod)
output = func_3920()
func_3921 = relay.Function([], output)
mutated_mod['func_3921'] = func_3921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_3926 = relay.TupleGetItem(func_2601_call(), 0)
call_3927 = relay.TupleGetItem(func_2602_call(), 0)
func_1644_call = mod.get_global_var('func_1644')
func_1647_call = mutated_mod.get_global_var('func_1647')
const_3929 = relay.const([[3,8,4,4,-2,7,1,-10,4,10,7,-8,-6,-9,-1,2,-2,-7,2,-6,-8,-6,3,-9,1,-8,3,5,8,-6,-4,-5,1,-5,-7,-7,6,-2,-1,-5,-2,3,2,7,-10,9,3,2,-7,-7,8,9,-1,-2,-4,5,3,-9,5,-2,-1,1,-6,8,-10,8,-2,1,-8,4,-3,5,-10,-10,2,-2,-3,-7,-7,-4,3,-2,-9,-6,9,8,-2,7,-1,7,-9,8,-3,2,-1,5,-8,-7,-2,-5,-5,-5,8,-9,9,2,-4,-1,-7,-6,-9,2,-8,6,4,-2,-4,5,9,1,-1,-7,5,-1,10,1,-8,7,-2,7,4,-4,-8,-10,-5,6,-4,-1,8,-1,1,8,-5,-5,-9,2,2,2,6,-9,-1,-9,6,3,-3,-2,8,-4,-6,7,-1,-9,-4,-5,10,-1,6,5,-9,-8,7,-9,-10,6,-1,-9,4,5,8,-8,3,9,-1,-3,-7,5,1,-6,6,-4,5,-9,-3,8,-6,10,-8,-1,5,1,5,3,1,-4,1,4,-5,-6,-9,2,1,-5,10,9,-9,5,-8,9,-10,-8,3,9,-7,8,9,1,1,2,3,-7,4,6,2,1,10,-3,1,3,-6,4,-1,9,3,1,3,-8,-10,6,2,6,-9,5,10,8,6,-5,-6,-9,4,-5,-8,3,-7,-1,-10,-1,5,-9,-3,-5,8,8,-2,5,6,4,-10,3,-8,6,-3,-7,4,-5,10,6,10,3]], dtype = "uint32")#candidate|3929|(1, 288)|const|uint32
call_3928 = func_1644_call(relay.reshape(const_3929.astype('uint32'), [9, 2, 16]))
call_3930 = func_1644_call(relay.reshape(const_3929.astype('uint32'), [9, 2, 16]))
output = relay.Tuple([call_3926,call_3928,const_3929,])
output2 = relay.Tuple([call_3927,call_3930,const_3929,])
func_3931 = relay.Function([], output)
mod['func_3931'] = func_3931
mod = relay.transform.InferType()(mod)
mutated_mod['func_3931'] = func_3931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3931_call = mutated_mod.get_global_var('func_3931')
call_3932 = func_3931_call()
output = call_3932
func_3933 = relay.Function([], output)
mutated_mod['func_3933'] = func_3933
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3942 = relay.var("var_3942", dtype = "float32", shape = (6, 4, 15))#candidate|3942|(6, 4, 15)|var|float32
uop_3943 = relay.erf(var_3942.astype('float32')) # shape=(6, 4, 15)
output = uop_3943
output2 = uop_3943
func_3963 = relay.Function([var_3942,], output)
mod['func_3963'] = func_3963
mod = relay.transform.InferType()(mod)
var_3964 = relay.var("var_3964", dtype = "float32", shape = (6, 4, 15))#candidate|3964|(6, 4, 15)|var|float32
output = func_3963(var_3964)
func_3965 = relay.Function([var_3964], output)
mutated_mod['func_3965'] = func_3965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3037_call = mutated_mod.get_global_var('func_3037')
call_3978 = func_3036_call()
call_3979 = func_3036_call()
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_3982 = relay.TupleGetItem(func_2776_call(), 0)
call_3983 = relay.TupleGetItem(func_2778_call(), 0)
var_3989 = relay.var("var_3989", dtype = "float32", shape = (3, 7, 13))#candidate|3989|(3, 7, 13)|var|float32
bop_3990 = relay.multiply(call_3978.astype('float32'), relay.reshape(var_3989.astype('float32'), relay.shape_of(call_3978))) # shape=(3, 7, 13)
bop_3993 = relay.multiply(call_3979.astype('float32'), relay.reshape(var_3989.astype('float32'), relay.shape_of(call_3979))) # shape=(3, 7, 13)
output = relay.Tuple([call_3982,bop_3990,])
output2 = relay.Tuple([call_3983,bop_3993,])
func_4009 = relay.Function([var_3989,], output)
mod['func_4009'] = func_4009
mod = relay.transform.InferType()(mod)
var_4010 = relay.var("var_4010", dtype = "float32", shape = (3, 7, 13))#candidate|4010|(3, 7, 13)|var|float32
output = func_4009(var_4010)
func_4011 = relay.Function([var_4010], output)
mutated_mod['func_4011'] = func_4011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_4035 = func_328_call()
call_4036 = func_328_call()
output = call_4035
output2 = call_4036
func_4049 = relay.Function([], output)
mod['func_4049'] = func_4049
mod = relay.transform.InferType()(mod)
mutated_mod['func_4049'] = func_4049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4049_call = mutated_mod.get_global_var('func_4049')
call_4050 = func_4049_call()
output = call_4050
func_4051 = relay.Function([], output)
mutated_mod['func_4051'] = func_4051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2565_call = mod.get_global_var('func_2565')
func_2567_call = mutated_mod.get_global_var('func_2567')
call_4052 = relay.TupleGetItem(func_2565_call(), 0)
call_4053 = relay.TupleGetItem(func_2567_call(), 0)
output = relay.Tuple([call_4052,])
output2 = relay.Tuple([call_4053,])
func_4058 = relay.Function([], output)
mod['func_4058'] = func_4058
mod = relay.transform.InferType()(mod)
mutated_mod['func_4058'] = func_4058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4058_call = mutated_mod.get_global_var('func_4058')
call_4059 = func_4058_call()
output = call_4059
func_4060 = relay.Function([], output)
mutated_mod['func_4060'] = func_4060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_4068 = relay.TupleGetItem(func_2294_call(), 1)
call_4069 = relay.TupleGetItem(func_2295_call(), 1)
func_3699_call = mod.get_global_var('func_3699')
func_3702_call = mutated_mod.get_global_var('func_3702')
const_4085 = relay.const([-8.282860,-0.832865,-1.215457,-9.507505,-1.467442,9.618375,4.768615,1.967745,-4.416877,5.199939,2.748502,-2.009297,-6.547978,-0.021516,-4.745850,-8.469075,-1.653489,-2.719433,-7.128237,-5.228101,-7.372957,5.829399,-4.525104,-0.131460,4.176790,9.899810,-0.208399,-7.271374,-9.232547,-6.649252,0.377819,5.379817,5.063292,8.915979,-2.334379,-2.596339,2.597225,-1.997715,2.133377,-9.029484,-5.566402,7.370557,3.195487,-2.934690,-2.345750,-4.494254,9.882177,-6.418653,0.552227,1.713314,3.469434,-8.084919,8.780132,-1.645269,-0.554524,0.071939,9.188166,8.593358,-3.755507,-8.983346,-7.084536,2.634943,-0.990288,-6.385092,8.933406,9.899191,1.809894,3.666865,2.743658,2.086963,-0.890238,-9.905776,6.032124,-5.937467,7.814887,7.259035,0.929631,-6.619396,-4.396798,-0.571123,-9.738227,-9.148611,5.121616,-6.074375,9.908003,-2.704632,-1.244820,0.089453,-0.540100,-5.883867,-2.020248,3.594655,-2.215549,0.675682,-8.457320,-8.909676,-1.105884,2.812918,-8.898422,-6.469367,9.297138,7.022221,3.390572,-2.834364,-5.856695,-7.694483,-6.763350,-0.176660,5.660554,6.906361,2.966728,-9.727498,-4.259151,-0.860614,5.675027,-6.724781,0.973653,-3.872488,6.270538,0.503560,2.808244,-5.154758,2.145483,-0.111572,4.691287,8.579629,2.934843,-3.249778,1.449078,-1.876286,8.171479,7.645286,-6.225126,2.075011,-6.694065,0.070993,-7.196072,4.889884,2.621871,-5.383940,8.359822,9.384865,4.077517,-2.160246,-7.556122,2.002384,-4.044043,5.318492,0.016512,-8.612734,5.838042,6.793176,7.282627,7.459233,3.914103,5.521569,3.000765,7.617503,-0.056245,2.687265,5.951387,-4.512792,-7.962744,-8.453684,9.585661,9.113721,8.244541,-2.693816,-7.406776,6.240357,-0.355216,-0.643736,8.774948,-4.535881,-7.398316,3.394350,6.413438,5.200348,4.327403,3.856545,-9.396335,2.109995,9.384925,-4.084202,9.856012,7.469788,4.820067,-7.332478,-8.686403,-5.452789,-9.432113,-2.560068,-9.487660,9.176478,3.832807,-0.124025,-8.354997,3.201631,1.319553,4.605574,8.684067,-7.474118,-4.515616,-2.642518,-9.571410,3.880282,-0.393535,-2.887958], dtype = "float32")#candidate|4085|(208,)|const|float32
const_4086 = relay.const([[-9.125824,-7.192453,-8.245934,-0.248530,-0.780708,1.613903,-8.981563,0.157408,-9.998796,3.284629,0.825214,7.472620,-3.533773,2.358831,0.470911,2.921957,-5.028825,-6.158800,-3.231536,-6.042514,-8.113083,5.689814,-9.258805,6.032363,-9.089572,-3.341696,-5.653575,7.067805,5.824156,3.477386,-3.375142,-6.443438,-7.086347,-7.385141,3.365684,-5.645085,-6.268895,-9.520714,-5.032709,5.403330,5.794222,-3.827423,5.663355,-8.356448,1.973744,9.192890,4.462182,-9.370569,-4.365767,-0.727347,-5.945137,-8.905692,-4.339065,0.594876,-7.051545,-5.914295],[-0.449699,-2.468007,-6.792233,-3.091002,-1.165468,-9.965049,-9.872019,-8.674357,4.551727,-1.648675,9.739003,-8.264716,-1.172093,-7.746388,-6.046056,-3.440604,-1.241863,-7.560510,9.721588,-0.876437,-5.207728,4.929915,9.568635,-4.521498,-0.981181,-3.211732,3.218726,-4.131043,-8.801134,-1.541151,1.752748,-2.234249,0.764648,-3.468392,5.503863,5.740655,2.112335,-8.236137,-0.735719,1.069515,-2.055966,-5.163030,-6.011545,7.963774,2.315842,5.010307,-7.124100,-7.832097,-5.376596,-9.019041,6.201109,-6.551762,3.033935,-6.388267,1.676525,-2.570760],[8.348139,8.237945,0.744944,3.164121,-9.232632,3.995267,-3.416452,1.427300,3.491673,-9.165561,1.244411,0.207621,-3.945596,-1.406514,-4.889839,1.024844,4.864415,5.811714,2.631355,0.958310,-5.775992,-8.772191,0.751641,8.001717,0.188598,5.245847,-8.205389,2.809922,-8.666090,-1.513893,2.389426,3.563295,-9.444286,5.563646,8.643083,-3.985795,-1.305025,-1.983720,-6.543725,-9.628044,5.683022,-7.959111,-3.136912,-9.939399,8.294095,9.926264,-8.068550,5.700513,-2.239454,-3.099195,3.345100,9.440944,6.061062,5.077032,2.247784,-5.122162],[-0.336942,4.465233,-6.340310,5.932873,-2.438205,-6.523869,9.603277,-5.439874,7.379697,0.870442,8.988934,-2.297084,-8.487536,-0.355532,9.436382,9.419202,4.730193,-0.266984,-2.357623,3.197755,9.785312,-1.511638,1.204061,-0.506921,3.739631,9.459863,-5.529283,-5.372776,-7.446458,-8.570722,0.445191,2.516396,-0.008658,-0.650455,2.745033,-0.424717,-0.582164,-5.120559,9.824090,-6.942916,-7.845662,5.842183,4.659899,-7.269730,-3.652458,4.004026,-1.866988,-0.614053,-8.274059,8.846140,-9.470963,-9.404572,-2.173998,-2.008598,0.146454,4.861385],[-8.701600,-2.006485,-8.308073,4.164752,-2.022964,-5.928080,4.916490,4.809257,8.074826,-5.443036,-4.103172,-1.509399,6.897171,-4.117754,4.612527,-5.728398,-1.396088,1.805094,3.515187,7.592777,7.988366,-9.980400,-7.204499,6.842843,5.276997,5.195865,-7.800570,-4.831866,-6.411747,1.775868,-7.190879,-0.132810,-0.310513,3.496061,-4.930578,6.599064,-6.844424,7.840316,-6.464944,0.927536,-9.031172,9.548853,-7.982146,-0.130401,6.987611,2.448020,2.535917,-9.275504,3.152756,-8.600809,5.030453,-7.663413,8.445998,-1.430651,-7.491550,3.922359],[0.849955,3.708066,4.306583,-3.024103,4.844613,-5.235383,7.584714,9.336241,1.106851,9.709726,3.531256,-0.533253,2.583215,-1.013761,-8.758340,-5.123402,0.949772,-5.652256,6.910535,5.691732,-9.995523,0.920130,-2.316402,-0.275550,-8.528542,-6.885835,3.331030,4.739782,-0.297605,-3.596074,7.970427,-0.397142,5.752116,5.223815,1.562477,5.498991,2.418039,-6.694044,8.744454,2.938226,-2.517201,-9.909064,-0.062114,-2.358451,3.698394,-7.966814,3.994542,5.126235,5.161054,1.804330,8.815668,-9.527687,5.211717,3.913716,7.932498,9.796433],[-4.323683,-6.966292,2.074435,1.826963,8.912501,3.561109,-9.189029,0.099556,-4.755884,6.500404,-0.329584,-4.579170,-4.333438,-6.003927,-3.249546,2.984280,8.681229,1.022836,-6.878760,-5.904252,-3.706013,-9.836633,-1.325200,-6.307540,-5.226091,4.801873,7.197731,-2.238073,2.620869,-0.764114,-3.718910,-7.500969,6.846987,-6.249902,1.255517,9.007251,0.199049,-5.157729,-1.235366,-8.481601,-5.430878,7.937648,0.246358,8.694028,-9.118960,-0.407238,8.434755,6.732461,-3.305108,-4.127152,-0.573065,-6.245639,8.420657,8.011709,6.413539,-5.416503],[2.587400,-0.170119,-1.565433,0.520778,0.586175,4.786343,7.597865,0.718656,4.653915,6.477296,5.665760,0.205123,-4.239395,-9.098250,-2.967722,-4.914638,-9.125674,-9.731137,-1.322067,-1.170533,6.563125,4.725348,-3.906571,-7.281858,-0.841435,9.674569,7.765730,3.566676,9.406469,-8.922769,-9.659106,-9.956059,6.074053,1.260855,-2.211281,9.088881,-0.605693,-4.170437,8.468852,-7.769284,-1.421752,1.153723,-5.087510,-3.819188,4.915448,5.410920,0.037486,-0.777053,-0.983791,-9.948793,7.396713,-9.931149,-0.943843,-8.377706,0.888707,-3.503944]], dtype = "float64")#candidate|4086|(8, 56)|const|float64
call_4084 = relay.TupleGetItem(func_3699_call(relay.reshape(const_4085.astype('float32'), [4, 4, 13]), relay.reshape(const_4086.astype('float64'), [224, 2]), ), 0)
call_4087 = relay.TupleGetItem(func_3702_call(relay.reshape(const_4085.astype('float32'), [4, 4, 13]), relay.reshape(const_4086.astype('float64'), [224, 2]), ), 0)
func_2565_call = mod.get_global_var('func_2565')
func_2567_call = mutated_mod.get_global_var('func_2567')
call_4090 = relay.TupleGetItem(func_2565_call(), 0)
call_4091 = relay.TupleGetItem(func_2567_call(), 0)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_4092 = relay.TupleGetItem(func_2601_call(), 1)
call_4093 = relay.TupleGetItem(func_2602_call(), 1)
func_1861_call = mod.get_global_var('func_1861')
func_1863_call = mutated_mod.get_global_var('func_1863')
call_4116 = relay.TupleGetItem(func_1861_call(relay.reshape(call_4092.astype('float64'), [9, 15, 4])), 0)
call_4117 = relay.TupleGetItem(func_1863_call(relay.reshape(call_4092.astype('float64'), [9, 15, 4])), 0)
func_3376_call = mod.get_global_var('func_3376')
func_3378_call = mutated_mod.get_global_var('func_3378')
call_4122 = relay.TupleGetItem(func_3376_call(), 0)
call_4123 = relay.TupleGetItem(func_3378_call(), 0)
func_1114_call = mod.get_global_var('func_1114')
func_1118_call = mutated_mod.get_global_var('func_1118')
const_4125 = relay.const([8,6,-5,-6,1,6,-2,-1,-8,-8,-2,-10,-4,10,-5,-2,10,-8,-1,9,6,3,-6,5,-7,-4,9,-5,-6,-7,-9,-5,7,7,-10,3,2,6,-10,3,-5,8,10,-10,-2,9,-6,-2,2,4,-6,9,-2,-7,9,2,6,9,5,2], dtype = "int16")#candidate|4125|(60,)|const|int16
var_4126 = relay.var("var_4126", dtype = "int16", shape = (600,))#candidate|4126|(600,)|var|int16
call_4124 = relay.TupleGetItem(func_1114_call(relay.reshape(const_4125.astype('int16'), [1, 5, 12]), relay.reshape(var_4126.astype('int16'), [10, 5, 12]), ), 2)
call_4127 = relay.TupleGetItem(func_1118_call(relay.reshape(const_4125.astype('int16'), [1, 5, 12]), relay.reshape(var_4126.astype('int16'), [10, 5, 12]), ), 2)
uop_4129 = relay.log(call_4124.astype('float64')) # shape=(350,)
uop_4131 = relay.log(call_4127.astype('float64')) # shape=(350,)
func_531_call = mod.get_global_var('func_531')
func_533_call = mutated_mod.get_global_var('func_533')
call_4139 = relay.TupleGetItem(func_531_call(), 0)
call_4140 = relay.TupleGetItem(func_533_call(), 0)
var_4141 = relay.var("var_4141", dtype = "float64", shape = (350,))#candidate|4141|(350,)|var|float64
bop_4142 = relay.minimum(uop_4129.astype('uint32'), relay.reshape(var_4141.astype('uint32'), relay.shape_of(uop_4129))) # shape=(350,)
bop_4145 = relay.minimum(uop_4131.astype('uint32'), relay.reshape(var_4141.astype('uint32'), relay.shape_of(uop_4131))) # shape=(350,)
uop_4151 = relay.sigmoid(uop_4129.astype('float32')) # shape=(350,)
uop_4153 = relay.sigmoid(uop_4131.astype('float32')) # shape=(350,)
output = relay.Tuple([call_4068,call_4084,const_4085,const_4086,call_4090,call_4092,call_4116,call_4122,const_4125,var_4126,call_4139,bop_4142,uop_4151,])
output2 = relay.Tuple([call_4069,call_4087,const_4085,const_4086,call_4091,call_4093,call_4117,call_4123,const_4125,var_4126,call_4140,bop_4145,uop_4153,])
func_4154 = relay.Function([var_4126,var_4141,], output)
mod['func_4154'] = func_4154
mod = relay.transform.InferType()(mod)
mutated_mod['func_4154'] = func_4154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mutated_mod.get_global_var('func_4154')
var_4156 = relay.var("var_4156", dtype = "int16", shape = (600,))#candidate|4156|(600,)|var|int16
var_4157 = relay.var("var_4157", dtype = "float64", shape = (350,))#candidate|4157|(350,)|var|float64
call_4155 = func_4154_call(var_4156,var_4157,)
output = call_4155
func_4158 = relay.Function([var_4156,var_4157,], output)
mutated_mod['func_4158'] = func_4158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1578_call = mod.get_global_var('func_1578')
func_1580_call = mutated_mod.get_global_var('func_1580')
call_4209 = func_1578_call()
call_4210 = func_1578_call()
uop_4214 = relay.erf(call_4209.astype('float32')) # shape=(12, 9, 4)
uop_4216 = relay.erf(call_4210.astype('float32')) # shape=(12, 9, 4)
func_1064_call = mod.get_global_var('func_1064')
func_1066_call = mutated_mod.get_global_var('func_1066')
var_4220 = relay.var("var_4220", dtype = "uint64", shape = (390,))#candidate|4220|(390,)|var|uint64
call_4219 = relay.TupleGetItem(func_1064_call(relay.reshape(var_4220.astype('uint64'), [390,])), 1)
call_4221 = relay.TupleGetItem(func_1066_call(relay.reshape(var_4220.astype('uint64'), [390,])), 1)
func_1166_call = mod.get_global_var('func_1166')
func_1167_call = mutated_mod.get_global_var('func_1167')
call_4222 = relay.TupleGetItem(func_1166_call(), 0)
call_4223 = relay.TupleGetItem(func_1167_call(), 0)
func_449_call = mod.get_global_var('func_449')
func_451_call = mutated_mod.get_global_var('func_451')
call_4231 = func_449_call()
call_4232 = func_449_call()
output = relay.Tuple([uop_4214,call_4219,var_4220,call_4222,call_4231,])
output2 = relay.Tuple([uop_4216,call_4221,var_4220,call_4223,call_4232,])
func_4246 = relay.Function([var_4220,], output)
mod['func_4246'] = func_4246
mod = relay.transform.InferType()(mod)
mutated_mod['func_4246'] = func_4246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4247 = relay.var("var_4247", dtype = "uint64", shape = (390,))#candidate|4247|(390,)|var|uint64
func_4246_call = mutated_mod.get_global_var('func_4246')
call_4248 = func_4246_call(var_4247)
output = call_4248
func_4249 = relay.Function([var_4247], output)
mutated_mod['func_4249'] = func_4249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1166_call = mod.get_global_var('func_1166')
func_1167_call = mutated_mod.get_global_var('func_1167')
call_4261 = relay.TupleGetItem(func_1166_call(), 0)
call_4262 = relay.TupleGetItem(func_1167_call(), 0)
func_3183_call = mod.get_global_var('func_3183')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_4270 = relay.TupleGetItem(func_3183_call(), 0)
call_4271 = relay.TupleGetItem(func_3185_call(), 0)
output = relay.Tuple([call_4261,call_4270,])
output2 = relay.Tuple([call_4262,call_4271,])
func_4282 = relay.Function([], output)
mod['func_4282'] = func_4282
mod = relay.transform.InferType()(mod)
output = func_4282()
func_4283 = relay.Function([], output)
mutated_mod['func_4283'] = func_4283
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4309 = relay.var("var_4309", dtype = "int32", shape = (10, 14, 7))#candidate|4309|(10, 14, 7)|var|int32
var_4310 = relay.var("var_4310", dtype = "int32", shape = (10, 14, 7))#candidate|4310|(10, 14, 7)|var|int32
bop_4311 = relay.less_equal(var_4309.astype('bool'), relay.reshape(var_4310.astype('bool'), relay.shape_of(var_4309))) # shape=(10, 14, 7)
bop_4320 = relay.maximum(var_4310.astype('float64'), relay.reshape(var_4309.astype('float64'), relay.shape_of(var_4310))) # shape=(10, 14, 7)
func_496_call = mod.get_global_var('func_496')
func_498_call = mutated_mod.get_global_var('func_498')
call_4324 = relay.TupleGetItem(func_496_call(), 0)
call_4325 = relay.TupleGetItem(func_498_call(), 0)
uop_4336 = relay.sqrt(bop_4320.astype('float64')) # shape=(10, 14, 7)
func_1197_call = mod.get_global_var('func_1197')
func_1199_call = mutated_mod.get_global_var('func_1199')
call_4339 = relay.TupleGetItem(func_1197_call(), 1)
call_4340 = relay.TupleGetItem(func_1199_call(), 1)
func_994_call = mod.get_global_var('func_994')
func_997_call = mutated_mod.get_global_var('func_997')
const_4354 = relay.const([-5.344530,8.381821,-6.475335,5.057851,-8.798457,6.237730,2.591154,-8.216387,-0.404139,-4.567062,-3.984196,3.106293,-1.807681,-1.323366,-1.275598,5.656799,-4.920534,-2.444524,9.173548,-3.560253,-0.895027,-8.344153,-1.622336,8.428324,8.717877,-0.163482,-9.396018,2.307536,-3.661257,-1.781343,-1.277964,8.276512,-6.654397,3.257805,5.589259,-1.644108,5.881693,8.795149,2.496901,-6.136272,-0.835954,4.806809,9.669182,9.430460,-4.055553,-4.572570,3.759880,7.059133,7.148508,8.697658,8.781987,2.378234,5.819533,-0.040145,7.381014,7.146691,2.399463,-5.858562,7.019488,-1.120359,-0.478230,-0.170431,-2.512545,6.410913,8.593523,-9.803186,-5.401664,7.657758,-5.261786,4.642379,1.591147,2.084306,5.911932,3.944463,8.108645,-2.034171,-6.545155,8.895180,1.520228,1.665291,3.102214,8.581152,6.294566,3.769619,-7.232433,4.145542,3.198886,-7.381465,-4.468567,-3.237768,3.099461,3.507056,4.369499,-7.089160,-9.656084,6.429081,0.749871,4.043643,-0.949053,-5.151291,6.761348,-2.904704,-3.196409,2.784427,-6.907482,-7.975018,3.629423,0.078445,-8.262662,5.482788,1.629165,-2.738786,9.126526,2.805991,1.936232,-2.605661,0.775227,8.430994,2.066724,7.826609,-3.758763,8.180585,6.164222,8.001030,-4.963628,-3.140704,4.682475,-8.133627,8.604022,-2.494727,8.411048,3.656407,6.847870,-8.897875,-3.582607,-0.893148,7.372818,-7.414278,6.523364,-7.631541,-6.304252,1.552670,7.722949,-9.592079,-1.708736,3.659739,7.242331,-4.526662,-1.801460,4.085741,-7.720046,2.684396,5.498347,2.552008,7.909460,-2.842375,-1.168643,-0.482209,6.359225,-8.482531,1.658946,5.882071,9.568524,-7.028814,-5.939500,-7.361940,2.413275,-0.984943,5.962830,9.115079,4.643561,-7.624755,-7.560863,0.115484,0.671372,7.376094,-3.088121,9.044883,-4.021102,5.386939,9.342342,-4.149564,0.588477,4.738503,-3.770559,-7.160814,-1.797735,0.535353,3.703397,-1.441492,7.056483,8.653528,-1.787875,7.491223,-1.246373,7.034940,-6.141628,3.346285,-0.636385,-4.136254,5.852465,-7.636871,7.622607,-4.778629,-3.731702,7.167680,-8.086304,8.689314,2.925511,-6.268904,4.215002,7.834270,0.232743,-0.740871,4.833119,-0.574087,6.300039,-5.343656,-4.679338,5.314484,0.269191,-1.119830,0.150980,-4.157776,-3.431877,7.022610,-0.477091,6.776079,9.955299,7.005184,-3.311918,7.263869,-2.622033,-4.342314,2.113879,3.818600,-2.545164,-5.920768,-1.121605,-4.160822,5.794080,-1.845722,-6.844856,7.985408,4.400786,-9.783781,-1.963705,9.103305,8.941797,-0.137625,1.346309,6.840256,0.339280,-6.345900,-2.500144,9.415769,-6.033857,8.941386,4.255779,-8.637052,7.692872,9.939747,-1.956884,-8.967635,-9.762572,-2.094816,9.013582,-7.502291,-9.284099,-9.013997,4.349812,-4.625895,4.054964,8.048147,7.654306,-2.781675,-4.059981,-6.013224,-2.592049,7.620885,8.123632,4.368775,8.626053,-6.663017,-3.598517,1.385141,-2.672151,2.237898,6.095506,-3.707368,-8.313740,-1.356585,-5.137129,0.088072,0.871055,-0.999549,4.129748,4.414066,0.002207,-8.507172,-7.823285,1.258289,6.272087,2.485309,5.792614,7.413182,-1.004437,7.615195,8.653330,6.564735,1.612788,8.870745,9.048957,1.728983,-7.750715,-8.940298,4.655693,4.295327,-0.786564,-6.710393,4.910762,1.330720,9.881796,-4.356953,-1.510533,4.441903,0.001167,-4.558297,-6.958921,9.306819,9.764574,2.538807,-8.551326,2.399534,1.312421,-7.832019,-0.054074,-6.022063,-1.766247,-0.988053,4.233902,-9.504275,-4.423772,8.773096,4.929933,-5.581106,6.879504,0.086184,-8.230253,-0.224915,-3.949195,-4.717040,5.895635,-5.525389,-2.715119,-5.456936,6.624316,-2.042934,4.568241,-8.948957,0.708826,5.424805,-8.779615,-2.239173,4.099554,9.247263,1.617994,-3.735164,-5.973691,4.919445,6.097472,-0.455931,-5.552766,6.651085,4.238512,-4.650209,-9.767321,8.797511,3.837771,2.609995,-0.467203,-5.711614,8.386265,-4.860734,-3.039623,-6.277419,7.227154,-3.344372,3.893517,4.207052,0.670875,8.221786,2.115233,-5.541109,-8.554213,-0.716223,-6.260746,7.370676,1.409168,-6.574437,2.744749,-1.804599,6.353833,-2.414789,-8.377389,3.175037,-5.927405,4.964867,3.362137,-0.242830,0.454190,3.594947,7.430661,1.656451,-8.549559,-1.770637,-1.411915,1.037022,3.232424,5.497981,4.879861,7.302821,5.201039,-7.872967,3.395933,2.455755,7.816079,-1.608705,5.914800,6.914493,3.298642,6.218304,-9.417264,-4.986948,-2.864269,6.500422,-1.355242,0.921174,6.605404,0.872712,-6.162181,-7.943164,6.567990,2.794362,-0.897699,-7.275705,-1.277341,-9.828470,-1.085102,0.278177,-3.782780,2.022178,1.421351,-5.933268,-7.692541,4.026117,-7.332933,-3.902032,9.106736,-0.827989,-4.294332,5.266515,-2.815587,-3.079900,-0.105291,-6.753297,-4.533434,-1.493749,-0.534935,8.991785,-6.711719,-5.465285,-6.617981,-8.915702,-4.876989,8.170527,1.764491,1.107063,-2.277489,4.486717,7.344249,0.707577,9.771308,-6.907122,9.441029,-6.389947,-8.897919,-8.289157,0.878701,-2.929015,-5.011824,-8.542094,6.799193,7.103450,9.683311,-0.552313,-5.962575,3.585843,7.777799,-0.511130,7.326582,-6.072436,0.102379,-8.200419,8.132894,-7.603966,-2.923051,-7.098292,-6.306988,-0.334093,-2.547406,3.074192,-9.595632,-9.233123,-3.364801,-4.779823,3.590605,8.428842,-5.896687,8.210973,0.748307,9.022613,-8.831958,2.496153,0.405342,5.178937,-3.374740,4.425650,9.604270,7.861644,-9.469041,0.567513,-4.949724,-9.343218,-8.701121,3.080146,9.348057,3.314232,-8.870173,-7.179410,-3.410495,1.004509,-9.867168,-3.451954,-4.322164,8.927850,8.045491,-2.205737,-9.856067,-7.972688,-9.727148,-1.563519,-8.987842,6.728306,-8.502401,2.062249,0.756544,8.277241,5.203365,1.875161,9.338641,-3.716225,8.882471,5.306642,1.315236,-6.389189,4.436112,9.508531,7.217844,-9.773486,-2.398521,-4.674340,-9.628306,-1.280638,9.988643,3.054720,-2.743356,-9.148603,-2.282503,7.379784,3.333506,9.679316,-6.758118,4.447333,9.965913,1.393317,6.499095,-4.870433,-7.759056,6.802829,-1.849069,-4.539999,-1.993202,0.641872,-6.934957,-7.564054,-8.716373,-7.070808,-6.059124,-7.458843,8.249617,7.854522,-3.728330,-9.387450,-2.750918,-7.784238,-3.987308,-9.229468,3.176666,0.498777,-4.596729,-7.891455,4.003128,-2.426978,-0.660646,-1.477114,-8.710184,-4.819689,7.334265,8.037250,-5.057391,-4.653790,0.867700,3.032410,-4.905696,-6.973126,-2.057149,-4.882133,-5.587637,6.827455,1.989792,-2.161267,8.341230,-3.192152,-0.032910,0.726927,-7.835405,8.327916,-3.710677,-3.374218,-3.044354,4.366857,4.271375,-4.710626,-3.957348,-6.050187,0.891913,-7.015974,9.618430,7.067480,-2.698937,-4.629565,3.269604,-6.973395,-7.994991,-2.792190,-1.850996,2.142964,8.347517,9.244394,5.828147,-0.186281,-7.797392,-5.124945,6.617575,4.799276,-6.065128,-8.668936,-5.729442,6.072323,-0.751253,1.867674,4.227549,-3.579856,-4.501411,1.890248,-9.276268,3.011673,-1.675600,-0.904548,9.550643,4.690859,-5.251638,5.870352,9.627658,5.154245,1.878952,-7.603113,-1.691935,6.954597,-0.262740,-4.907381,-3.767269,3.903763,8.150719,1.092384,-4.317101,-1.048413,-1.819489,6.244382,-8.123349,2.696082,4.170262,0.088663,8.745725,-3.869611,1.114258,-3.411929,-6.036638,-3.030037,8.248252,1.501132,-0.786670,-0.214970,7.773248,-7.452584,8.659642,4.301517,2.715162,-9.750797,-8.838482,-8.338270,3.105119,8.326867,4.735752,-7.679222,8.952244,-7.324181,4.484539,6.014580,-9.523763,6.206584,9.939823,-0.131902,7.059350,5.155475,4.369855,6.523996,-4.297992,3.471268,-0.014226,3.195904,9.468599,1.416099,-4.941129,3.185337,8.750779,-5.083977,-1.127158,3.290922,8.513559,1.442994,8.150783,-6.741028,8.850087,4.306385,4.169707,-1.513410,-9.164835,9.631428,-3.965138,3.488816,8.288648,-2.775980,-8.025576,3.774352,0.286752,-8.549486,9.829701,-9.417293,-0.671569,-4.896979,-9.224106,-0.392475,1.326087,-2.411462,1.808780,1.578183,5.317192,-9.915767,2.962474,-6.093145,-7.685009,0.026626,0.225507,-8.493478,7.176633,4.106537,9.358947,-3.948815,8.184936,-6.985216,-5.012178,-5.647726,-2.795829,3.029835,-8.889285,-7.086190,7.643770,0.957987,3.354209,-4.053274,-4.144320,1.180219,-6.509098,-7.355925,-2.653113,-7.737878,-5.073780,-6.558462,5.105503,0.903115,8.171213,-1.351216,3.323201,9.504649,3.050037,-6.502797,0.273750,-9.444026,3.482153,-9.239484,2.998147,2.389225,5.669478,-0.974637,0.858604,-1.798798,5.929394,2.252301,-7.414578,-5.017288,2.244874,-0.051041,-5.851350,-6.690276,6.463531,1.684478,5.745711,9.091135,-0.992514,7.038239,4.902563,6.390710,-4.940922,9.149174,6.560625,-9.824251,-4.555335,-2.421473,2.718549,7.959645,3.387583,-4.738481,7.438224,4.129339,3.859273,8.830075,-4.676249,-9.880196,-0.079260,-8.610888,9.711251,-7.866078,1.752339,-1.043022,0.881105,8.117769,-2.285971,8.005343,5.751081,6.159500,2.813642,4.915282,7.117451,-1.154949,-0.798478,-7.151496,4.198076,6.869510,9.475555,-6.551287,9.558341,1.247441,4.461498,4.055630,9.811775,6.824053,-6.429027,-3.234403,-9.828072,1.129591,9.272286,-4.923703,-9.022520,9.655414], dtype = "float64")#candidate|4354|(896,)|const|float64
call_4353 = relay.TupleGetItem(func_994_call(relay.reshape(const_4354.astype('float64'), [16, 14, 4]), relay.reshape(const_4354.astype('float64'), [16, 14, 4]), ), 0)
call_4355 = relay.TupleGetItem(func_997_call(relay.reshape(const_4354.astype('float64'), [16, 14, 4]), relay.reshape(const_4354.astype('float64'), [16, 14, 4]), ), 0)
uop_4362 = relay.sqrt(const_4354.astype('float64')) # shape=(896,)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_4372 = relay.TupleGetItem(func_2294_call(), 0)
call_4373 = relay.TupleGetItem(func_2295_call(), 0)
bop_4384 = relay.minimum(var_4309.astype('int64'), relay.reshape(bop_4320.astype('int64'), relay.shape_of(var_4309))) # shape=(10, 14, 7)
func_4058_call = mod.get_global_var('func_4058')
func_4060_call = mutated_mod.get_global_var('func_4060')
call_4397 = relay.TupleGetItem(func_4058_call(), 0)
call_4398 = relay.TupleGetItem(func_4060_call(), 0)
bop_4405 = relay.right_shift(uop_4336.astype('uint32'), relay.reshape(bop_4311.astype('uint32'), relay.shape_of(uop_4336))) # shape=(10, 14, 7)
uop_4421 = relay.log2(bop_4405.astype('float32')) # shape=(10, 14, 7)
var_4430 = relay.var("var_4430", dtype = "float64", shape = (10, 14, 7))#candidate|4430|(10, 14, 7)|var|float64
bop_4431 = relay.logical_and(uop_4336.astype('bool'), relay.reshape(var_4430.astype('bool'), relay.shape_of(uop_4336))) # shape=(10, 14, 7)
func_4282_call = mod.get_global_var('func_4282')
func_4283_call = mutated_mod.get_global_var('func_4283')
call_4434 = relay.TupleGetItem(func_4282_call(), 1)
call_4435 = relay.TupleGetItem(func_4283_call(), 1)
bop_4437 = relay.floor_divide(bop_4431.astype('float32'), relay.reshape(bop_4320.astype('float32'), relay.shape_of(bop_4431))) # shape=(10, 14, 7)
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_4442 = relay.TupleGetItem(func_357_call(), 1)
call_4443 = relay.TupleGetItem(func_358_call(), 1)
uop_4454 = relay.cosh(uop_4336.astype('float64')) # shape=(10, 14, 7)
var_4456 = relay.var("var_4456", dtype = "float64", shape = (10, 14, 7))#candidate|4456|(10, 14, 7)|var|float64
bop_4457 = relay.add(uop_4454.astype('uint8'), relay.reshape(var_4456.astype('uint8'), relay.shape_of(uop_4454))) # shape=(10, 14, 7)
output = relay.Tuple([call_4324,call_4339,call_4353,uop_4362,call_4372,bop_4384,call_4397,uop_4421,call_4434,bop_4437,call_4442,bop_4457,])
output2 = relay.Tuple([call_4325,call_4340,call_4355,uop_4362,call_4373,bop_4384,call_4398,uop_4421,call_4435,bop_4437,call_4443,bop_4457,])
func_4469 = relay.Function([var_4309,var_4310,var_4430,var_4456,], output)
mod['func_4469'] = func_4469
mod = relay.transform.InferType()(mod)
var_4470 = relay.var("var_4470", dtype = "int32", shape = (10, 14, 7))#candidate|4470|(10, 14, 7)|var|int32
var_4471 = relay.var("var_4471", dtype = "int32", shape = (10, 14, 7))#candidate|4471|(10, 14, 7)|var|int32
var_4472 = relay.var("var_4472", dtype = "float64", shape = (10, 14, 7))#candidate|4472|(10, 14, 7)|var|float64
var_4473 = relay.var("var_4473", dtype = "float64", shape = (10, 14, 7))#candidate|4473|(10, 14, 7)|var|float64
output = func_4469(var_4470,var_4471,var_4472,var_4473,)
func_4474 = relay.Function([var_4470,var_4471,var_4472,var_4473,], output)
mutated_mod['func_4474'] = func_4474
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4639 = relay.var("var_4639", dtype = "float32", shape = (14, 5, 4))#candidate|4639|(14, 5, 4)|var|float32
uop_4640 = relay.acosh(var_4639.astype('float32')) # shape=(14, 5, 4)
output = relay.Tuple([uop_4640,])
output2 = relay.Tuple([uop_4640,])
func_4651 = relay.Function([var_4639,], output)
mod['func_4651'] = func_4651
mod = relay.transform.InferType()(mod)
mutated_mod['func_4651'] = func_4651
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4652 = relay.var("var_4652", dtype = "float32", shape = (14, 5, 4))#candidate|4652|(14, 5, 4)|var|float32
func_4651_call = mutated_mod.get_global_var('func_4651')
call_4653 = func_4651_call(var_4652)
output = call_4653
func_4654 = relay.Function([var_4652], output)
mutated_mod['func_4654'] = func_4654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_4665 = func_328_call()
call_4666 = func_328_call()
func_357_call = mod.get_global_var('func_357')
func_358_call = mutated_mod.get_global_var('func_358')
call_4687 = relay.TupleGetItem(func_357_call(), 2)
call_4688 = relay.TupleGetItem(func_358_call(), 2)
func_2354_call = mod.get_global_var('func_2354')
func_2357_call = mutated_mod.get_global_var('func_2357')
var_4691 = relay.var("var_4691", dtype = "float32", shape = ())#candidate|4691|()|var|float32
var_4692 = relay.var("var_4692", dtype = "float32", shape = (350,))#candidate|4692|(350,)|var|float32
call_4690 = relay.TupleGetItem(func_2354_call(relay.reshape(var_4691.astype('float32'), []), relay.reshape(var_4692.astype('float32'), [1, 350]), ), 3)
call_4693 = relay.TupleGetItem(func_2357_call(relay.reshape(var_4691.astype('float32'), []), relay.reshape(var_4692.astype('float32'), [1, 350]), ), 3)
func_1802_call = mod.get_global_var('func_1802')
func_1807_call = mutated_mod.get_global_var('func_1807')
const_4702 = relay.const([-7.621849,5.132057,-5.457207,-4.384935,-0.340091,-9.700627,-3.841057,-6.397928,-7.281293,-7.097885,6.225450,3.747242,-4.384101,0.006358,8.464583,-1.077231,-8.797283,-5.303088,-8.175650,5.837274], dtype = "float32")#candidate|4702|(20,)|const|float32
var_4703 = relay.var("var_4703", dtype = "uint64", shape = (390,))#candidate|4703|(390,)|var|uint64
const_4704 = relay.const([-1.627418,-1.500761,9.447605,1.131456,-0.484372,6.024569,-4.844301,-8.332090,2.156846,9.076644,3.508742,-4.894081,8.662544,5.423555,5.552319,-3.934531,6.309536,3.626610,7.165630,-0.153927,-2.210644,9.747335,8.259802,0.815218,-4.902704,3.343756,9.855631,0.435253,8.833481,6.685126,-0.952901,-7.086104,-5.516798,2.350906,6.719996,0.924572,6.533676,-3.407535,-7.904878,9.449964,7.196185,5.498025,8.855631,9.369316,9.909060,8.487376,-9.688959,7.199886,-6.485194,-1.505825,-1.049958,0.859640,-6.526049,-7.874296,5.000071,-9.476747,4.976112,7.676328,-3.534057,9.547487,-7.208074,-1.326442,2.522518,5.395779,-0.255408,9.242852,-7.447580,-9.435930,-1.987211,9.898631,9.684104,-1.660657,0.073101,2.398193,-5.369515,2.112635,5.349167,0.321845,-6.252314,-4.514751,3.638858,8.766768,-8.675378,-8.914771,5.378992,-5.034124,7.255654,3.941542,3.840088,7.748558,9.012183,-3.734462,-0.201992,0.681771,-0.817762,4.780751,6.054073,6.716866,-2.048460,1.264085,-0.441999,-2.748858,-9.814186,-1.347782,-5.650845,-1.936788,3.269065,1.270136,-4.171763,-9.102724,-1.482783,-2.010664,-9.468009,-4.560165,-6.086451,-6.203380,6.343472,-8.491810,-9.540330,8.752944,-2.927188,0.940650,-6.807285,2.801773,1.004509,-5.982994,1.931773,-3.633409,-7.483075,0.762375,-2.932693,0.665978,-5.881367,4.104291,6.641902,-5.486750,-0.607989,6.688467,-1.030818,-9.371525,-4.594232,8.013982,8.850331,5.036301,-6.876122,-4.111668,9.398495,7.597153,-5.498570,-6.221226,5.419939,0.570887,-7.907832,4.948683,-7.384147,7.733000,-1.177883,-2.273448,-3.137276,7.636905,-2.207832,2.379035,-6.023334,-8.994699,9.502061,-5.148638,4.452572,2.950801,-6.339990,-5.279991,-7.636736,6.649361,-5.753222,-5.485595,0.447130,-4.382084,-5.786510,7.793355,-9.509447,0.795888], dtype = "float64")#candidate|4704|(180,)|const|float64
call_4701 = relay.TupleGetItem(func_1802_call(relay.reshape(const_4702.astype('float32'), [10, 2, 1]), relay.reshape(call_4665.astype('float64'), [9, 15, 4]), relay.reshape(var_4703.astype('uint64'), [65, 6]), relay.reshape(const_4704.astype('float64'), [10, 2, 9]), ), 0)
call_4705 = relay.TupleGetItem(func_1807_call(relay.reshape(const_4702.astype('float32'), [10, 2, 1]), relay.reshape(call_4665.astype('float64'), [9, 15, 4]), relay.reshape(var_4703.astype('uint64'), [65, 6]), relay.reshape(const_4704.astype('float64'), [10, 2, 9]), ), 0)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_4711 = relay.TupleGetItem(func_2601_call(), 1)
call_4712 = relay.TupleGetItem(func_2602_call(), 1)
output = relay.Tuple([call_4665,call_4687,call_4690,var_4691,var_4692,call_4701,const_4702,var_4703,const_4704,call_4711,])
output2 = relay.Tuple([call_4666,call_4688,call_4693,var_4691,var_4692,call_4705,const_4702,var_4703,const_4704,call_4712,])
func_4717 = relay.Function([var_4691,var_4692,var_4703,], output)
mod['func_4717'] = func_4717
mod = relay.transform.InferType()(mod)
var_4718 = relay.var("var_4718", dtype = "float32", shape = ())#candidate|4718|()|var|float32
var_4719 = relay.var("var_4719", dtype = "float32", shape = (350,))#candidate|4719|(350,)|var|float32
var_4720 = relay.var("var_4720", dtype = "uint64", shape = (390,))#candidate|4720|(390,)|var|uint64
output = func_4717(var_4718,var_4719,var_4720,)
func_4721 = relay.Function([var_4718,var_4719,var_4720,], output)
mutated_mod['func_4721'] = func_4721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4058_call = mod.get_global_var('func_4058')
func_4060_call = mutated_mod.get_global_var('func_4060')
call_4774 = relay.TupleGetItem(func_4058_call(), 0)
call_4775 = relay.TupleGetItem(func_4060_call(), 0)
func_3154_call = mod.get_global_var('func_3154')
func_3156_call = mutated_mod.get_global_var('func_3156')
const_4777 = relay.const([6.756103,3.136797,-0.445269,-3.087358,3.828012,4.964409,8.740145,-4.979255,-4.274367,4.421426,-7.608042,-8.415000,2.771473,9.803243,-3.380561,1.691794,-7.493095,-5.210800,9.374602,1.670166,5.059206,2.113209,-3.101651,-3.547112,-4.965208,1.406604,4.627744,-4.222387,-2.449929,0.254989,-5.300610,-2.166777,4.430207,4.386420,-1.733695,3.424395,-4.648431,-9.308029,-0.612873,7.182668,4.079232,4.063567,8.915915,2.488562,-3.336404,-4.306948,8.132208,1.399500,0.329636,3.789174,5.618724,2.792303,-1.690605,-4.450949,0.174399,0.644627,2.191884,2.276638,-9.748139,-9.031704,1.640687,0.012333,2.529532,2.001655,7.841676,-9.466853,-3.326588,-8.118092,-1.819325,9.725070,7.806597,-0.845267,-2.808577,6.523141,-7.638722,3.236391,-2.879921,4.715974,5.752437,-2.511629,0.352720,8.476284,-2.383332,-4.806032,0.532605,-9.000391,-4.945725,3.847568,-5.624317,6.769077,-0.003996,-6.048678,5.673954,-3.507798,4.399638,-9.891496,-0.668848,-7.820921,7.615229,4.906876,-3.219285,9.672226,-2.199726,3.910502,4.087973,8.928737,0.341022,-9.920915,1.702870,5.110938,8.182757,-1.422790,-1.655744,2.832772,7.075969,-8.492949,-0.546882,7.412799,-1.023639,-4.169977,5.638605,3.633884,6.039823,-7.394747,-9.749644,8.884610,5.693211,4.271666,-3.871830,3.073099,4.276709,-6.423064,-7.861665,-8.719418,-4.762566,-1.087657,5.123419,3.775864,-2.063874,3.316670,8.061000,-0.856722,-0.964343,-8.726632,-9.009533,6.049840,0.224942,-6.344309,2.237402,-5.247378,4.120624,0.546695,-2.333556,9.983345,-3.432303,-2.637953,-3.172219,-2.840446,-9.454411,4.791011,3.588484,1.788149,-3.578391,-8.552947,-8.057628,-2.123719,5.648439,-8.752085,-2.018413,-5.242319,8.843819,-7.656102,-0.671102,-8.331502,-8.241686,7.059362,-8.806389,-8.192824,-1.517620,-7.040689,-7.020345,-8.411340,4.674649,3.742718,8.220966,-9.381006,-2.302636,-3.029475,-2.688124,-0.355842,-7.897583,-4.206026,-7.721301,-9.050141,4.467772,1.734873,9.074304,5.260972,6.971589,-6.858966,3.066828,1.155057,4.556164,-8.251188,-5.321222,-8.398483,-3.462717,-0.009937,-2.389616,-6.268718,5.098869,2.193564,7.885512,4.205719,4.303097,9.596841,0.487639,4.897179,-8.899062,-5.599723,-4.452824,-3.789477,6.960077,9.616105,0.280721,7.823086,7.796144,5.784131,3.430525,7.774624,-6.260692,2.620196,4.518587,-3.179531,-6.319020,4.670779,-8.102148,-6.504197,-1.294969,8.754952,6.953728,-6.560045,6.977346,7.310368,3.869752,4.695750,-8.312176,4.554415,8.872277,8.663345,-1.006524,-9.395985,-3.946527,-9.052492,-7.851202,-6.523984,-4.340722,6.658784,-2.704921,-6.207406,6.119013,1.682263,5.780342,-1.322635,9.814644,-9.274059,-5.786473,-8.322887,7.568380,8.740841,-4.656730,5.163058,-5.815863,-6.113121,-1.259581,-5.229377,-1.716627,1.192351,-1.176433,2.452909,2.309287,1.702899,-2.328718,3.196609,-9.727052,-1.917810,-9.276490,0.345119,-7.744964,-1.214642,6.643842,-5.190798,-7.120583,5.562729,6.513190,-6.222824,-9.797188,-9.984528,3.846903,5.444502,-5.736148,-7.638060,6.336956,-7.051062,3.080122,-6.603539,7.359773,9.104106,-2.984953,8.917334,9.376443,5.614121,5.309726,-5.742952,3.841455,0.888737,0.210806,-4.495456,0.160171,-1.171642,4.690341,8.654675,-0.458609,0.617528,0.062088,-5.680755,-3.224168,6.671281,-9.633323,4.320459,8.836391,6.998736,-3.277574,8.328756,-0.235340,0.136687], dtype = "float32")#candidate|4777|(336,)|const|float32
call_4776 = relay.TupleGetItem(func_3154_call(relay.reshape(const_4777.astype('float32'), [14, 2, 12])), 0)
call_4778 = relay.TupleGetItem(func_3156_call(relay.reshape(const_4777.astype('float32'), [14, 2, 12])), 0)
output = relay.Tuple([call_4774,call_4776,const_4777,])
output2 = relay.Tuple([call_4775,call_4778,const_4777,])
func_4788 = relay.Function([], output)
mod['func_4788'] = func_4788
mod = relay.transform.InferType()(mod)
mutated_mod['func_4788'] = func_4788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4788_call = mutated_mod.get_global_var('func_4788')
call_4789 = func_4788_call()
output = call_4789
func_4790 = relay.Function([], output)
mutated_mod['func_4790'] = func_4790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3920_call = mod.get_global_var('func_3920')
func_3921_call = mutated_mod.get_global_var('func_3921')
call_4826 = relay.TupleGetItem(func_3920_call(), 0)
call_4827 = relay.TupleGetItem(func_3921_call(), 0)
func_3920_call = mod.get_global_var('func_3920')
func_3921_call = mutated_mod.get_global_var('func_3921')
call_4830 = relay.TupleGetItem(func_3920_call(), 0)
call_4831 = relay.TupleGetItem(func_3921_call(), 0)
output = relay.Tuple([call_4826,call_4830,])
output2 = relay.Tuple([call_4827,call_4831,])
func_4872 = relay.Function([], output)
mod['func_4872'] = func_4872
mod = relay.transform.InferType()(mod)
mutated_mod['func_4872'] = func_4872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4872_call = mutated_mod.get_global_var('func_4872')
call_4873 = func_4872_call()
output = call_4873
func_4874 = relay.Function([], output)
mutated_mod['func_4874'] = func_4874
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4938 = relay.var("var_4938", dtype = "float32", shape = (8, 11))#candidate|4938|(8, 11)|var|float32
uop_4939 = relay.sqrt(var_4938.astype('float32')) # shape=(8, 11)
output = relay.Tuple([uop_4939,])
output2 = relay.Tuple([uop_4939,])
func_4944 = relay.Function([var_4938,], output)
mod['func_4944'] = func_4944
mod = relay.transform.InferType()(mod)
mutated_mod['func_4944'] = func_4944
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4945 = relay.var("var_4945", dtype = "float32", shape = (8, 11))#candidate|4945|(8, 11)|var|float32
func_4944_call = mutated_mod.get_global_var('func_4944')
call_4946 = func_4944_call(var_4945)
output = call_4946
func_4947 = relay.Function([var_4945], output)
mutated_mod['func_4947'] = func_4947
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4952 = relay.var("var_4952", dtype = "float64", shape = (7, 3, 2))#candidate|4952|(7, 3, 2)|var|float64
uop_4953 = relay.erf(var_4952.astype('float64')) # shape=(7, 3, 2)
output = relay.Tuple([uop_4953,])
output2 = relay.Tuple([uop_4953,])
func_4958 = relay.Function([var_4952,], output)
mod['func_4958'] = func_4958
mod = relay.transform.InferType()(mod)
mutated_mod['func_4958'] = func_4958
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4959 = relay.var("var_4959", dtype = "float64", shape = (7, 3, 2))#candidate|4959|(7, 3, 2)|var|float64
func_4958_call = mutated_mod.get_global_var('func_4958')
call_4960 = func_4958_call(var_4959)
output = call_4960
func_4961 = relay.Function([var_4959], output)
mutated_mod['func_4961'] = func_4961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4872_call = mod.get_global_var('func_4872')
func_4874_call = mutated_mod.get_global_var('func_4874')
call_4979 = relay.TupleGetItem(func_4872_call(), 1)
call_4980 = relay.TupleGetItem(func_4874_call(), 1)
func_4944_call = mod.get_global_var('func_4944')
func_4947_call = mutated_mod.get_global_var('func_4947')
const_4986 = relay.const([-8.550348,-5.402284,-7.541025,4.802986,-3.546073,-1.885351,1.924629,6.088567,-8.519112,-9.519527,5.382759,7.624244,1.363585,1.656753,-2.648331,-3.435185,-8.575710,4.795776,1.307445,-2.198001,5.937847,-5.422587,4.492971,-3.437673,-7.709335,0.613534,-5.908004,4.027484,1.667578,-3.586380,6.201525,-0.208720,7.093641,-8.523540,-2.383622,-2.155344,3.505489,0.290203,-6.874695,1.842842,-4.887125,-2.969749,4.841399,-6.908863,-9.519059,-0.100624,0.216791,-3.045363,-8.010490,-9.418209,6.138854,-5.664094,8.666065,4.781036,6.041524,-7.970393,6.243405,-5.611611,-1.357560,9.964958,-9.648082,-1.034290,-9.448097,-9.720946,-7.017656,7.617090,-0.081210,-6.560276,8.873098,0.562161,-5.367295,5.499709,7.287294,-8.302027,-3.028102,-2.411836,2.405298,3.208467,8.783557,-7.409675,-5.452980,3.430359,-0.495168,-9.750735,2.176387,-4.286540,9.634103,6.594406], dtype = "float32")#candidate|4986|(88,)|const|float32
call_4985 = relay.TupleGetItem(func_4944_call(relay.reshape(const_4986.astype('float32'), [8, 11])), 0)
call_4987 = relay.TupleGetItem(func_4947_call(relay.reshape(const_4986.astype('float32'), [8, 11])), 0)
output = relay.Tuple([call_4979,call_4985,const_4986,])
output2 = relay.Tuple([call_4980,call_4987,const_4986,])
func_5000 = relay.Function([], output)
mod['func_5000'] = func_5000
mod = relay.transform.InferType()(mod)
output = func_5000()
func_5001 = relay.Function([], output)
mutated_mod['func_5001'] = func_5001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_531_call = mod.get_global_var('func_531')
func_533_call = mutated_mod.get_global_var('func_533')
call_5046 = relay.TupleGetItem(func_531_call(), 0)
call_5047 = relay.TupleGetItem(func_533_call(), 0)
output = relay.Tuple([call_5046,])
output2 = relay.Tuple([call_5047,])
func_5050 = relay.Function([], output)
mod['func_5050'] = func_5050
mod = relay.transform.InferType()(mod)
mutated_mod['func_5050'] = func_5050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5050_call = mutated_mod.get_global_var('func_5050')
call_5051 = func_5050_call()
output = call_5051
func_5052 = relay.Function([], output)
mutated_mod['func_5052'] = func_5052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_661_call = mod.get_global_var('func_661')
func_663_call = mutated_mod.get_global_var('func_663')
call_5069 = relay.TupleGetItem(func_661_call(), 0)
call_5070 = relay.TupleGetItem(func_663_call(), 0)
output = relay.Tuple([call_5069,])
output2 = relay.Tuple([call_5070,])
func_5085 = relay.Function([], output)
mod['func_5085'] = func_5085
mod = relay.transform.InferType()(mod)
mutated_mod['func_5085'] = func_5085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5085_call = mutated_mod.get_global_var('func_5085')
call_5086 = func_5085_call()
output = call_5086
func_5087 = relay.Function([], output)
mutated_mod['func_5087'] = func_5087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5050_call = mod.get_global_var('func_5050')
func_5052_call = mutated_mod.get_global_var('func_5052')
call_5194 = relay.TupleGetItem(func_5050_call(), 0)
call_5195 = relay.TupleGetItem(func_5052_call(), 0)
output = call_5194
output2 = call_5195
func_5197 = relay.Function([], output)
mod['func_5197'] = func_5197
mod = relay.transform.InferType()(mod)
mutated_mod['func_5197'] = func_5197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5197_call = mutated_mod.get_global_var('func_5197')
call_5198 = func_5197_call()
output = call_5198
func_5199 = relay.Function([], output)
mutated_mod['func_5199'] = func_5199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3516_call = mod.get_global_var('func_3516')
func_3518_call = mutated_mod.get_global_var('func_3518')
call_5203 = relay.TupleGetItem(func_3516_call(), 0)
call_5204 = relay.TupleGetItem(func_3518_call(), 0)
output = call_5203
output2 = call_5204
func_5231 = relay.Function([], output)
mod['func_5231'] = func_5231
mod = relay.transform.InferType()(mod)
output = func_5231()
func_5232 = relay.Function([], output)
mutated_mod['func_5232'] = func_5232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3920_call = mod.get_global_var('func_3920')
func_3921_call = mutated_mod.get_global_var('func_3921')
call_5245 = relay.TupleGetItem(func_3920_call(), 0)
call_5246 = relay.TupleGetItem(func_3921_call(), 0)
output = relay.Tuple([call_5245,])
output2 = relay.Tuple([call_5246,])
func_5249 = relay.Function([], output)
mod['func_5249'] = func_5249
mod = relay.transform.InferType()(mod)
mutated_mod['func_5249'] = func_5249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5249_call = mutated_mod.get_global_var('func_5249')
call_5250 = func_5249_call()
output = call_5250
func_5251 = relay.Function([], output)
mutated_mod['func_5251'] = func_5251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_5262 = relay.TupleGetItem(func_2294_call(), 0)
call_5263 = relay.TupleGetItem(func_2295_call(), 0)
output = relay.Tuple([call_5262,])
output2 = relay.Tuple([call_5263,])
func_5282 = relay.Function([], output)
mod['func_5282'] = func_5282
mod = relay.transform.InferType()(mod)
mutated_mod['func_5282'] = func_5282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5282_call = mutated_mod.get_global_var('func_5282')
call_5283 = func_5282_call()
output = call_5283
func_5284 = relay.Function([], output)
mutated_mod['func_5284'] = func_5284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3000_call = mod.get_global_var('func_3000')
func_3002_call = mutated_mod.get_global_var('func_3002')
call_5328 = relay.TupleGetItem(func_3000_call(), 0)
call_5329 = relay.TupleGetItem(func_3002_call(), 0)
output = call_5328
output2 = call_5329
func_5341 = relay.Function([], output)
mod['func_5341'] = func_5341
mod = relay.transform.InferType()(mod)
mutated_mod['func_5341'] = func_5341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5341_call = mutated_mod.get_global_var('func_5341')
call_5342 = func_5341_call()
output = call_5342
func_5343 = relay.Function([], output)
mutated_mod['func_5343'] = func_5343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_328_call = mod.get_global_var('func_328')
func_330_call = mutated_mod.get_global_var('func_330')
call_5390 = func_328_call()
call_5391 = func_328_call()
func_3883_call = mod.get_global_var('func_3883')
func_3885_call = mutated_mod.get_global_var('func_3885')
call_5395 = func_3883_call(relay.reshape(call_5390.astype('float64'), [9, 15, 4]))
call_5396 = func_3883_call(relay.reshape(call_5390.astype('float64'), [9, 15, 4]))
output = relay.Tuple([call_5390,call_5395,])
output2 = relay.Tuple([call_5391,call_5396,])
func_5397 = relay.Function([], output)
mod['func_5397'] = func_5397
mod = relay.transform.InferType()(mod)
mutated_mod['func_5397'] = func_5397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5397_call = mutated_mod.get_global_var('func_5397')
call_5398 = func_5397_call()
output = call_5398
func_5399 = relay.Function([], output)
mutated_mod['func_5399'] = func_5399
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5411 = relay.const([[[2.657770,1.159258,0.621537,-5.705187,-3.877620,-2.477473,-4.451002,-5.178810,3.674323,-2.425891,3.073671,9.830850],[-2.040641,-1.354516,2.806441,2.925937,-8.351615,-9.663113,-4.667560,-7.180948,1.131180,-0.937925,8.438440,-3.746011],[-0.536530,-4.793958,-4.761005,9.196043,4.571750,5.109211,9.652048,2.091661,6.101829,-0.336318,-9.507320,3.062032],[4.603129,-5.209904,-8.283822,2.028376,9.501083,-1.264697,-8.667323,0.575341,6.412850,-6.140698,3.550184,3.923031]],[[5.375927,-0.265545,-3.213667,-4.014624,0.510141,-2.114641,9.922031,-2.318214,3.455345,-5.968732,8.940767,-8.742950],[4.476507,5.361315,-4.581603,9.794120,-1.001738,-2.451413,4.198738,4.178932,9.464267,5.905632,5.114431,5.470869],[-6.067502,-0.937485,9.707406,1.761320,7.214186,-5.898102,9.768450,-4.467165,0.101644,-4.241278,0.656068,-1.333941],[-5.313172,1.227322,6.317301,-1.509350,6.549977,1.331722,0.868430,4.743677,-6.557772,7.873362,3.917552,5.834250]],[[-8.603722,-2.423910,6.148649,-4.668155,-0.669627,-8.582244,-8.012600,3.166843,4.581773,5.625288,8.414493,-8.054457],[-7.775665,8.974141,3.020631,-7.257098,3.468719,3.050229,2.476787,-0.152976,1.517168,-7.935033,8.727900,1.263716],[-8.528542,-6.841038,9.542658,1.065038,-2.867640,-6.064213,-2.523852,0.247613,2.357189,-0.206759,-2.267518,-1.835405],[1.896272,2.033410,-4.509694,-9.030833,0.393294,4.980446,0.133828,-8.937686,7.815634,8.471765,-8.700265,0.961330]],[[6.978267,-8.565349,-7.350422,9.234519,7.843446,4.294541,-7.733657,0.401098,-0.042607,-5.113686,4.879108,4.901552],[3.624885,-1.897364,4.398104,8.965699,-3.773575,-9.709667,-2.493395,-3.828842,-6.537704,-2.744270,9.855848,8.457699],[-9.620094,3.187428,-5.843056,-6.933977,0.374435,6.938142,4.461353,8.969130,1.449437,-6.207928,-8.510489,4.995424],[-8.019588,6.508084,6.513013,7.777849,-6.899412,-7.295927,2.973403,1.135172,5.576768,5.563385,0.516427,-6.227662]],[[-8.861414,8.321688,-1.455718,-5.382052,-8.043034,-1.859432,-5.041452,3.391982,2.214652,9.029788,-9.329945,6.028745],[-3.995803,-2.099391,-0.751023,-0.765362,-3.234546,7.753354,-5.880510,8.293905,8.867823,7.430743,-5.038808,-2.766603],[-4.767663,-9.974554,-9.959994,-5.504191,2.185789,5.676019,-9.345327,-5.343934,0.090590,6.191461,7.607847,-6.141894],[-9.013818,-3.055936,-0.584776,-4.137664,0.413169,4.823515,5.461319,-4.018533,8.500435,-9.779473,6.358511,-9.197646]],[[-0.790034,-3.006900,-5.070483,-8.143919,-3.360014,4.600965,1.584914,8.118590,2.059999,5.667048,0.600693,1.521139],[5.877848,-3.651575,-0.315889,7.579232,-4.941376,6.533218,-1.359600,2.057061,-0.272295,0.308958,4.182009,-8.663782],[7.003108,0.002543,1.157071,1.295717,-9.759577,8.044166,-9.550913,7.900718,6.166107,-5.109503,-4.902234,-9.566730],[-3.974624,-8.506730,3.380536,-3.567096,-0.862852,7.954397,-3.825241,-7.432430,-2.557623,-5.566476,-4.642162,2.331450]]], dtype = "float32")#candidate|5411|(6, 4, 12)|const|float32
uop_5412 = relay.log2(const_5411.astype('float32')) # shape=(6, 4, 12)
func_3699_call = mod.get_global_var('func_3699')
func_3702_call = mutated_mod.get_global_var('func_3702')
const_5415 = relay.const([2.908248,-3.910826,8.553691,3.514729,-7.360751,-1.119827,-5.095447,-3.772313,-4.024879,-8.397367,8.549594,3.874541,7.465699,-3.110091,6.547344,2.649113,-9.825644,-0.726447,8.539377,3.370885,-0.488901,-5.987851,-2.878072,8.289112,-4.244982,3.852190,-4.662409,2.585261,-5.787300,-4.374114,5.659308,-3.003880,2.826284,-0.063288,-3.907763,2.119301,4.433806,1.405600,-0.483364,6.898646,-1.309835,-1.665109,8.763352,0.619914,3.496015,0.486000,1.275462,-7.635765,7.417593,-6.602049,9.827630,-1.111544,6.978245,-7.147179,-3.024404,1.971259,1.328945,1.031015,5.610451,-7.351258,0.617456,8.257387,3.293299,0.922520,-8.820768,-1.374738,9.783819,7.547124,6.598574,-6.726986,2.172128,-2.260718,7.260383,6.702814,-0.177395,-1.341773,-7.535348,8.362653,8.446072,-3.935154,-0.389248,5.845807,7.843387,-1.394459,1.414487,-3.134858,-8.613811,7.132971,2.227696,-3.204069,-5.352760,4.805084,7.679912,-9.985758,6.156937,-9.613730,9.444318,-9.235030,-1.992071,1.333921,5.158291,-4.533649,9.603779,-6.271994,9.867200,-3.357996,4.925086,-3.829394,-1.168565,0.947391,1.455521,7.483611,-2.290248,5.702564,2.068400,-9.428316,-0.342134,-3.638269,-2.882747,-6.368949,-9.043205,5.996146,-1.416197,-4.643545,-5.846184,1.290577,5.045642,-8.283565,-3.149006,4.339766,5.935242,-9.802552,-8.358364,6.331301,1.753596,-4.504120,-5.468833,6.457444,0.699860,-6.713250,-4.713307,6.573448,-1.984137,4.725547,5.184384,-9.035524,-9.426188,5.469746,-8.173845,3.247332,-7.934010,7.834295,6.123460,-0.476958,-2.248225,-5.890571,-3.405132,-3.636741,3.324868,7.564897,-0.898523,3.745031,-3.976071,-8.986835,9.375940,7.555074,5.446508,6.048948,7.198226,-8.833286,-4.421888,-7.133456,-7.968568,6.933895,-0.254651,9.625168,5.324096,6.071932,7.600826,-0.156885,8.677233,-7.838336,-5.224354,5.113909,0.765970,8.748087,-0.292341,-3.492583,-6.069835,3.737495,-0.092376,-5.550395,2.014831,-9.311433,7.852849,-8.221749,-8.775204,0.817928,-7.307666,-7.425860,-2.786539,7.773098,-6.226582,-5.866950,1.643624,6.752077,-2.443525,6.563757], dtype = "float32")#candidate|5415|(208,)|const|float32
var_5416 = relay.var("var_5416", dtype = "float64", shape = (8, 56))#candidate|5416|(8, 56)|var|float64
call_5414 = relay.TupleGetItem(func_3699_call(relay.reshape(const_5415.astype('float32'), [4, 4, 13]), relay.reshape(var_5416.astype('float64'), [224, 2]), ), 0)
call_5417 = relay.TupleGetItem(func_3702_call(relay.reshape(const_5415.astype('float32'), [4, 4, 13]), relay.reshape(var_5416.astype('float64'), [224, 2]), ), 0)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_5419 = relay.TupleGetItem(func_2294_call(), 0)
call_5420 = relay.TupleGetItem(func_2295_call(), 0)
var_5421 = relay.var("var_5421", dtype = "float64", shape = (8, 56))#candidate|5421|(8, 56)|var|float64
bop_5422 = relay.add(var_5416.astype('uint8'), relay.reshape(var_5421.astype('uint8'), relay.shape_of(var_5416))) # shape=(8, 56)
output = relay.Tuple([uop_5412,call_5414,const_5415,call_5419,bop_5422,])
output2 = relay.Tuple([uop_5412,call_5417,const_5415,call_5420,bop_5422,])
func_5428 = relay.Function([var_5416,var_5421,], output)
mod['func_5428'] = func_5428
mod = relay.transform.InferType()(mod)
mutated_mod['func_5428'] = func_5428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5428_call = mutated_mod.get_global_var('func_5428')
var_5430 = relay.var("var_5430", dtype = "float64", shape = (8, 56))#candidate|5430|(8, 56)|var|float64
var_5431 = relay.var("var_5431", dtype = "float64", shape = (8, 56))#candidate|5431|(8, 56)|var|float64
call_5429 = func_5428_call(var_5430,var_5431,)
output = call_5429
func_5432 = relay.Function([var_5430,var_5431,], output)
mutated_mod['func_5432'] = func_5432
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5666 = relay.var("var_5666", dtype = "float64", shape = (12, 6, 1))#candidate|5666|(12, 6, 1)|var|float64
uop_5667 = relay.acos(var_5666.astype('float64')) # shape=(12, 6, 1)
bop_5671 = relay.bitwise_xor(uop_5667.astype('uint8'), relay.reshape(var_5666.astype('uint8'), relay.shape_of(uop_5667))) # shape=(12, 6, 1)
uop_5674 = relay.asin(var_5666.astype('float64')) # shape=(12, 6, 1)
uop_5676 = relay.atanh(var_5666.astype('float32')) # shape=(12, 6, 1)
bop_5685 = relay.minimum(var_5666.astype('int16'), relay.reshape(uop_5676.astype('int16'), relay.shape_of(var_5666))) # shape=(12, 6, 1)
func_1578_call = mod.get_global_var('func_1578')
func_1580_call = mutated_mod.get_global_var('func_1580')
call_5694 = func_1578_call()
call_5695 = func_1578_call()
bop_5704 = relay.floor_mod(uop_5674.astype('float32'), relay.reshape(var_5666.astype('float32'), relay.shape_of(uop_5674))) # shape=(12, 6, 1)
uop_5708 = relay.rsqrt(uop_5674.astype('float32')) # shape=(12, 6, 1)
bop_5717 = relay.logical_or(bop_5704.astype('bool'), relay.reshape(bop_5685.astype('bool'), relay.shape_of(bop_5704))) # shape=(12, 6, 1)
output = relay.Tuple([bop_5671,call_5694,uop_5708,bop_5717,])
output2 = relay.Tuple([bop_5671,call_5695,uop_5708,bop_5717,])
func_5742 = relay.Function([var_5666,], output)
mod['func_5742'] = func_5742
mod = relay.transform.InferType()(mod)
var_5743 = relay.var("var_5743", dtype = "float64", shape = (12, 6, 1))#candidate|5743|(12, 6, 1)|var|float64
output = func_5742(var_5743)
func_5744 = relay.Function([var_5743], output)
mutated_mod['func_5744'] = func_5744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2405_call = mod.get_global_var('func_2405')
func_2406_call = mutated_mod.get_global_var('func_2406')
call_5749 = relay.TupleGetItem(func_2405_call(), 1)
call_5750 = relay.TupleGetItem(func_2406_call(), 1)
output = relay.Tuple([call_5749,])
output2 = relay.Tuple([call_5750,])
func_5765 = relay.Function([], output)
mod['func_5765'] = func_5765
mod = relay.transform.InferType()(mod)
mutated_mod['func_5765'] = func_5765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5765_call = mutated_mod.get_global_var('func_5765')
call_5766 = func_5765_call()
output = call_5766
func_5767 = relay.Function([], output)
mutated_mod['func_5767'] = func_5767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4282_call = mod.get_global_var('func_4282')
func_4283_call = mutated_mod.get_global_var('func_4283')
call_5830 = relay.TupleGetItem(func_4282_call(), 1)
call_5831 = relay.TupleGetItem(func_4283_call(), 1)
func_5085_call = mod.get_global_var('func_5085')
func_5087_call = mutated_mod.get_global_var('func_5087')
call_5836 = relay.TupleGetItem(func_5085_call(), 0)
call_5837 = relay.TupleGetItem(func_5087_call(), 0)
bop_5841 = relay.divide(call_5836.astype('float32'), relay.reshape(call_5830.astype('float32'), relay.shape_of(call_5836))) # shape=(9, 15, 4)
bop_5844 = relay.divide(call_5837.astype('float32'), relay.reshape(call_5831.astype('float32'), relay.shape_of(call_5837))) # shape=(9, 15, 4)
func_1433_call = mod.get_global_var('func_1433')
func_1434_call = mutated_mod.get_global_var('func_1434')
call_5854 = relay.TupleGetItem(func_1433_call(), 1)
call_5855 = relay.TupleGetItem(func_1434_call(), 1)
func_2354_call = mod.get_global_var('func_2354')
func_2357_call = mutated_mod.get_global_var('func_2357')
var_5868 = relay.var("var_5868", dtype = "float32", shape = ())#candidate|5868|()|var|float32
const_5869 = relay.const([2.700845,-8.790830,-1.792579,-4.383082,-6.523405,-0.081795,3.402464,5.928849,0.478982,1.821345,-9.941249,-7.137472,3.390793,-2.778208,-2.592985,7.128807,-5.821207,7.659238,5.013636,1.216229,-2.024058,0.603454,7.729955,-3.808788,3.568612,3.727977,6.926031,-1.174239,-4.216706,2.025778,-9.824001,-6.832239,-9.321821,-6.405026,-5.185949,7.152413,0.894338,-3.234588,-7.105687,-9.989903,5.271067,1.479057,4.717669,4.847356,-9.480345,-0.792326,0.135495,0.083538,-9.439321,3.400902,6.853713,1.636551,-2.246189,5.453698,-2.279190,-9.663867,0.876456,0.343197,9.685201,-2.552689,2.360234,-7.581125,-9.687160,5.831861,4.232040,8.037186,9.745149,-1.765231,-3.747275,-8.072026,3.733558,-1.343937,-1.600619,0.112564,9.893334,0.177977,-7.694450,6.135446,0.977164,8.469956,-6.984684,6.793021,-8.840432,7.450739,3.952479,5.247064,-3.598493,7.814334,7.558006,-1.355268,7.825263,-6.519697,8.460409,-7.411808,-6.778393,-3.968538,-7.167297,-2.645315,6.654933,2.281583,-4.510739,8.557179,9.445202,2.075379,8.360054,0.262679,-2.563630,-4.443108,9.972162,-3.750181,-3.391365,-8.548849,2.484834,6.390772,-9.555739,4.872368,-8.922515,4.616314,-8.448731,-1.915168,-8.071051,-0.979497,7.099248,6.244039,2.184407,-9.018538,-2.685284,-2.019591,-3.891835,-1.916352,-7.219829,2.823258,-9.520456,-7.766272,3.179890,-5.546833,-6.521848,-3.931941,6.495516,8.223286,-6.996259,-5.079198,-4.699357,-3.288457,0.701126,-4.293590,-0.456990,-3.926048,-7.387694,1.442896,9.727301,-0.357251,-4.408001,-2.379726,-6.892507,-7.304386,5.591152,8.458304,1.054553,-5.682141,-4.917590,9.725969,-2.142283,1.081227,-4.350501,1.778447,-8.021948,-6.983651,-0.485698,-8.097410,-7.044521,6.258187,8.590659,1.559590,-9.027209,3.643970,-4.005461,-6.404478,-5.544968,-3.090805,-1.074158,8.448986,4.322872,-9.044029,-0.259201,-0.368169,9.964337,-7.159748,-0.883896,-5.882622,-5.056223,8.340915,-2.074275,1.484788,3.363991,5.428023,2.576685,-2.166041,-5.230688,8.753971,2.973867,4.405474,8.735739,3.703447,-2.561060,1.736537,-3.823343,2.588789,-5.796652,5.655073,-3.006830,6.542175,7.090626,-9.229747,-6.615968,-0.582792,8.079908,8.687861,-7.934950,-0.509281,-5.755487,2.723747,-9.013165,3.944200,1.747553,-7.978184,0.292154,-8.522508,5.028546,6.561179,-3.051766,6.067944,1.437945,-2.160613,-5.835679,-3.082919,-9.290189,8.872546,2.311747,8.472299,0.105700,-6.977811,-4.394988,-1.497729,-6.524775,3.124886,2.840520,-7.411543,7.992367,-1.852674,-6.084720,-1.081788,-3.124316,8.547504,-8.028077,9.066111,0.461471,3.470957,-2.745031,6.838902,9.195436,4.781084,-7.976184,5.820680,-0.826132,9.370929,3.670989,-4.933563,8.074971,9.737852,-7.175718,9.999185,-5.903854,7.230659,-2.119999,2.139198,-9.749750,4.083572,4.567913,-9.665032,-8.702396,-7.762590,-5.085023,-0.326127,-2.246308,2.295403,-7.279242,-0.561263,4.210049,4.083340,0.283129,0.698065,8.222351,-9.097008,-4.019208,-2.956827,-9.847996,-4.336993,2.583352,-1.283106,-3.605998,8.562532,-0.362995,6.966359,4.036487,-8.093632,-6.204210,-9.576706,-8.127529,-9.089370,-6.595776,5.164868,6.527989,5.806633,-5.319239,-5.101674,1.811764,0.587864,-1.527757,-9.367552,5.004624,-9.649036,-5.600342,5.703223,4.307925,0.267123,1.687160,-9.068910,-9.439207,7.891120,8.681217,7.454745,6.282132,-6.807786,-7.304570,-4.916750,2.195578,7.066715,0.512297,-5.819112,-4.393144,-9.745220,0.700784,-1.585185,-5.762986,-7.695944,9.175898,8.372985,5.654683,-2.223256], dtype = "float32")#candidate|5869|(350,)|const|float32
call_5867 = relay.TupleGetItem(func_2354_call(relay.reshape(var_5868.astype('float32'), []), relay.reshape(const_5869.astype('float32'), [1, 350]), ), 1)
call_5870 = relay.TupleGetItem(func_2357_call(relay.reshape(var_5868.astype('float32'), []), relay.reshape(const_5869.astype('float32'), [1, 350]), ), 1)
output = relay.Tuple([bop_5841,call_5854,call_5867,var_5868,const_5869,])
output2 = relay.Tuple([bop_5844,call_5855,call_5870,var_5868,const_5869,])
func_5879 = relay.Function([var_5868,], output)
mod['func_5879'] = func_5879
mod = relay.transform.InferType()(mod)
var_5880 = relay.var("var_5880", dtype = "float32", shape = ())#candidate|5880|()|var|float32
output = func_5879(var_5880)
func_5881 = relay.Function([var_5880], output)
mutated_mod['func_5881'] = func_5881
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5916 = relay.var("var_5916", dtype = "float64", shape = (4, 15, 4))#candidate|5916|(4, 15, 4)|var|float64
uop_5917 = relay.atan(var_5916.astype('float64')) # shape=(4, 15, 4)
output = relay.Tuple([uop_5917,])
output2 = relay.Tuple([uop_5917,])
func_5920 = relay.Function([var_5916,], output)
mod['func_5920'] = func_5920
mod = relay.transform.InferType()(mod)
var_5921 = relay.var("var_5921", dtype = "float64", shape = (4, 15, 4))#candidate|5921|(4, 15, 4)|var|float64
output = func_5920(var_5921)
func_5922 = relay.Function([var_5921], output)
mutated_mod['func_5922'] = func_5922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_531_call = mod.get_global_var('func_531')
func_533_call = mutated_mod.get_global_var('func_533')
call_5949 = relay.TupleGetItem(func_531_call(), 0)
call_5950 = relay.TupleGetItem(func_533_call(), 0)
func_3376_call = mod.get_global_var('func_3376')
func_3378_call = mutated_mod.get_global_var('func_3378')
call_5963 = relay.TupleGetItem(func_3376_call(), 0)
call_5964 = relay.TupleGetItem(func_3378_call(), 0)
func_2565_call = mod.get_global_var('func_2565')
func_2567_call = mutated_mod.get_global_var('func_2567')
call_5973 = relay.TupleGetItem(func_2565_call(), 0)
call_5974 = relay.TupleGetItem(func_2567_call(), 0)
output = relay.Tuple([call_5949,call_5963,call_5973,])
output2 = relay.Tuple([call_5950,call_5964,call_5974,])
func_5992 = relay.Function([], output)
mod['func_5992'] = func_5992
mod = relay.transform.InferType()(mod)
output = func_5992()
func_5993 = relay.Function([], output)
mutated_mod['func_5993'] = func_5993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2129_call = mod.get_global_var('func_2129')
func_2131_call = mutated_mod.get_global_var('func_2131')
call_6042 = relay.TupleGetItem(func_2129_call(), 0)
call_6043 = relay.TupleGetItem(func_2131_call(), 0)
uop_6067 = relay.rsqrt(call_6042.astype('float64')) # shape=(630,)
uop_6069 = relay.rsqrt(call_6043.astype('float64')) # shape=(630,)
output = uop_6067
output2 = uop_6069
func_6077 = relay.Function([], output)
mod['func_6077'] = func_6077
mod = relay.transform.InferType()(mod)
mutated_mod['func_6077'] = func_6077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6077_call = mutated_mod.get_global_var('func_6077')
call_6078 = func_6077_call()
output = call_6078
func_6079 = relay.Function([], output)
mutated_mod['func_6079'] = func_6079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1298_call = mod.get_global_var('func_1298')
func_1300_call = mutated_mod.get_global_var('func_1300')
call_6216 = relay.TupleGetItem(func_1298_call(), 1)
call_6217 = relay.TupleGetItem(func_1300_call(), 1)
func_3269_call = mod.get_global_var('func_3269')
func_3275_call = mutated_mod.get_global_var('func_3275')
var_6252 = relay.var("var_6252", dtype = "uint16", shape = (390,))#candidate|6252|(390,)|var|uint16
const_6253 = relay.const([-2,2,3,-1,-6,9,7,-10,-1,-9,9,-9,-9,-6,-4,4,2,-2,-2,5,-1,1,-10,-4,-4,-6,-8,-3,-8,5,-2,8,7,-10,-4,-8,1,-4,10,2,2,-9,2,5,-1,-4,3,8,3,-10,-6,3,-10,10,6,4,-9,8,4,-3], dtype = "int16")#candidate|6253|(60,)|const|int16
var_6254 = relay.var("var_6254", dtype = "int16", shape = (600,))#candidate|6254|(600,)|var|int16
const_6255 = relay.const([-6.215340,-1.074882,7.200277,-3.074114,-4.026281,-1.484237,0.109604,-0.640993,6.828718,1.625738,-2.589869,-9.613349,-1.107132,7.217263,4.510678,4.008547,-1.075173,-5.913362,-0.354316,-0.216230], dtype = "float32")#candidate|6255|(20,)|const|float32
call_6251 = relay.TupleGetItem(func_3269_call(relay.reshape(var_6252.astype('uint16'), [10, 13, 3]), relay.reshape(const_6253.astype('int16'), [60,]), relay.reshape(var_6254.astype('int16'), [12, 50]), relay.reshape(const_6255.astype('float32'), [20,]), ), 4)
call_6256 = relay.TupleGetItem(func_3275_call(relay.reshape(var_6252.astype('uint16'), [10, 13, 3]), relay.reshape(const_6253.astype('int16'), [60,]), relay.reshape(var_6254.astype('int16'), [12, 50]), relay.reshape(const_6255.astype('float32'), [20,]), ), 4)
func_5341_call = mod.get_global_var('func_5341')
func_5343_call = mutated_mod.get_global_var('func_5343')
call_6266 = func_5341_call()
call_6267 = func_5341_call()
output = relay.Tuple([call_6216,call_6251,var_6252,const_6253,var_6254,const_6255,call_6266,])
output2 = relay.Tuple([call_6217,call_6256,var_6252,const_6253,var_6254,const_6255,call_6267,])
func_6274 = relay.Function([var_6252,var_6254,], output)
mod['func_6274'] = func_6274
mod = relay.transform.InferType()(mod)
mutated_mod['func_6274'] = func_6274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6274_call = mutated_mod.get_global_var('func_6274')
var_6276 = relay.var("var_6276", dtype = "uint16", shape = (390,))#candidate|6276|(390,)|var|uint16
var_6277 = relay.var("var_6277", dtype = "int16", shape = (600,))#candidate|6277|(600,)|var|int16
call_6275 = func_6274_call(var_6276,var_6277,)
output = call_6275
func_6278 = relay.Function([var_6276,var_6277,], output)
mutated_mod['func_6278'] = func_6278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5397_call = mod.get_global_var('func_5397')
func_5399_call = mutated_mod.get_global_var('func_5399')
call_6288 = relay.TupleGetItem(func_5397_call(), 1)
call_6289 = relay.TupleGetItem(func_5399_call(), 1)
func_2601_call = mod.get_global_var('func_2601')
func_2602_call = mutated_mod.get_global_var('func_2602')
call_6323 = relay.TupleGetItem(func_2601_call(), 1)
call_6324 = relay.TupleGetItem(func_2602_call(), 1)
output = relay.Tuple([call_6288,call_6323,])
output2 = relay.Tuple([call_6289,call_6324,])
func_6327 = relay.Function([], output)
mod['func_6327'] = func_6327
mod = relay.transform.InferType()(mod)
output = func_6327()
func_6328 = relay.Function([], output)
mutated_mod['func_6328'] = func_6328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1578_call = mod.get_global_var('func_1578')
func_1580_call = mutated_mod.get_global_var('func_1580')
call_6381 = func_1578_call()
call_6382 = func_1578_call()
func_598_call = mod.get_global_var('func_598')
func_602_call = mutated_mod.get_global_var('func_602')
var_6409 = relay.var("var_6409", dtype = "float32", shape = ())#candidate|6409|()|var|float32
const_6410 = relay.const([-3.217524,-8.915944,-9.821358,3.579909,6.955978,-2.873762,-5.692658,-7.789018,1.422463,5.950106,-4.713028,5.952450,8.112890,-3.946079,4.204287,4.974673,-6.141854,-4.791157,6.329150,0.520369,3.868632,-6.686903,-4.746034,-9.865513,-0.970034,-8.167919,0.313543,9.485566,7.400915,6.015688,6.943724,8.289198,1.874784,-8.313186,0.024804,8.614890,-1.487956,-6.801690,0.661939,-7.603868,-3.115119,-9.716386,-8.057366,5.225692,3.419680,2.706984,5.268594,-4.184826,-8.355885,1.664941,-0.098454,-3.671249,-3.025346,-7.599811,7.637455,6.301510,0.917568,9.822016,5.357585,-1.082742,6.558803,6.009388,-3.569478,9.075974,4.234700,-7.329031,-0.772030,-7.326021,7.662415,-1.609333,3.634581,-6.935647,8.662250,7.925121,-2.254355,-0.383608,0.678745,-7.573491,6.748570,-8.671694,-4.220175,1.150430,4.497220,5.604675,-3.734861,2.185654,6.972008,-6.498240,9.724037,5.671507,0.108943,5.556741,-2.340020,-2.213367,-1.390188,-6.998174,8.016093,9.938765,8.836782,2.343474,-4.986155,9.005221,3.404068,-3.925439,3.066013,-7.640426,9.656168,8.446414,-0.903236,-7.498178,-3.728925,6.010195,-7.415101,-1.293631,-9.426548,0.928651,-2.575205,-1.608256,-4.181344,-7.405578,2.763548,0.796392,5.800616,-0.598605,-2.854100,-0.406843,9.093646,3.325966,-3.721771,0.505956,6.428539,2.576316,8.699405,0.366919,-5.276689,-0.717316,4.309408,7.757269,-4.072212,-7.290042,-0.609314,-1.467313,-2.335709,3.259762,3.290844,7.185860,5.458547,8.339012,2.469091,-8.178250,-9.964474,3.698863,-8.809012,-8.254255,-9.746093,-4.536781,5.078673,-3.088135,-3.194572,-0.037625,-6.953640,-9.554347,-0.745683,-9.101240,8.844256,-1.726996,2.100577,4.361754,-2.228363,9.046642,-1.691695,6.252210,-5.893553,5.680844,0.748852,-5.559365,-3.024922,9.659946,-0.415213,-8.681102,-0.020945,-0.717033,-5.810807,-9.875117,4.666003,3.684079,2.281519,-5.148618,-5.381615,-7.978296,8.489399,3.802557,1.478683,5.193172,-2.222966,8.605742,-0.192876,5.517174,4.992527,1.414971,8.187665,-8.208016,5.790546,-2.298716,4.675025,4.270593,3.607398,-8.415947,2.740065,0.466403,6.268577,-1.043558,-7.931520,-5.623357,4.305545,-3.427433,-0.905903,2.919160,3.111820,0.110732,-1.282128,-7.744361,0.558849,9.645266,-6.241413,-6.581919,7.777292,9.379809,-5.491191,-0.636496,9.654022,-5.046697,5.661420,7.250264,5.781892,0.093834,1.160400,-8.249215,-1.853333,6.022535,-3.621578,-1.877441,-6.826087,7.782936,5.511052,6.695754,-9.682663,-9.268414,0.924867,7.810998,-7.742871,3.488855,-9.984432,-4.528967,7.002912,4.794769,-9.152065,9.573503,5.697722,5.979831,-8.551475,8.343020,7.638356,8.713896,4.642081,1.887793,9.087746,2.834869,-5.949074,4.018233,8.923746,4.578504,-9.929551,-0.945112,2.859736,4.455908,-9.648185,9.328733,-7.916035,8.660286,0.672669,-6.098442,4.905366,-6.346912,8.655843,6.380561,-8.163866,-1.788564,9.856952,-7.291627,4.634307,6.852291,-9.279595,4.863969,3.861652,-0.392563,4.977140,8.837355,-3.159698,9.351717,6.924130,-5.297765,0.987335,6.470592,0.684634,-7.278661,1.925787,0.732865,-2.859515,-4.127428,4.108830,-9.182960,8.660851,5.051059,9.564523,-1.703402,4.915394,-3.325174,9.450972,9.721384,3.867453,1.739045,8.934672,-9.578674,8.583340,2.299834,8.431052,-7.767186,-2.896582,-6.676259,-9.105342,-4.726672,6.300792,-2.869829,-3.696131,1.591298,9.301134,-7.289858,6.198877,-8.619144,-7.794758,1.373246,7.057976,-5.932632,1.136934,4.997610,7.938172,0.416199,-7.114288,-2.557909], dtype = "float32")#candidate|6410|(350,)|const|float32
call_6408 = relay.TupleGetItem(func_598_call(relay.reshape(var_6409.astype('float32'), []), relay.reshape(const_6410.astype('float32'), [350,]), relay.reshape(const_6410.astype('float32'), [350,]), ), 1)
call_6411 = relay.TupleGetItem(func_602_call(relay.reshape(var_6409.astype('float32'), []), relay.reshape(const_6410.astype('float32'), [350,]), relay.reshape(const_6410.astype('float32'), [350,]), ), 1)
uop_6419 = relay.tan(call_6408.astype('float32')) # shape=(7, 10, 5)
uop_6421 = relay.tan(call_6411.astype('float32')) # shape=(7, 10, 5)
output = relay.Tuple([call_6381,var_6409,const_6410,uop_6419,])
output2 = relay.Tuple([call_6382,var_6409,const_6410,uop_6421,])
func_6429 = relay.Function([var_6409,], output)
mod['func_6429'] = func_6429
mod = relay.transform.InferType()(mod)
var_6430 = relay.var("var_6430", dtype = "float32", shape = ())#candidate|6430|()|var|float32
output = func_6429(var_6430)
func_6431 = relay.Function([var_6430], output)
mutated_mod['func_6431'] = func_6431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3561_call = mod.get_global_var('func_3561')
func_3562_call = mutated_mod.get_global_var('func_3562')
call_6433 = relay.TupleGetItem(func_3561_call(), 0)
call_6434 = relay.TupleGetItem(func_3562_call(), 0)
output = relay.Tuple([call_6433,])
output2 = relay.Tuple([call_6434,])
func_6440 = relay.Function([], output)
mod['func_6440'] = func_6440
mod = relay.transform.InferType()(mod)
output = func_6440()
func_6441 = relay.Function([], output)
mutated_mod['func_6441'] = func_6441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5231_call = mod.get_global_var('func_5231')
func_5232_call = mutated_mod.get_global_var('func_5232')
call_6452 = func_5231_call()
call_6453 = func_5231_call()
output = call_6452
output2 = call_6453
func_6461 = relay.Function([], output)
mod['func_6461'] = func_6461
mod = relay.transform.InferType()(mod)
mutated_mod['func_6461'] = func_6461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6461_call = mutated_mod.get_global_var('func_6461')
call_6462 = func_6461_call()
output = call_6462
func_6463 = relay.Function([], output)
mutated_mod['func_6463'] = func_6463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6461_call = mod.get_global_var('func_6461')
func_6463_call = mutated_mod.get_global_var('func_6463')
call_6473 = func_6461_call()
call_6474 = func_6461_call()
output = call_6473
output2 = call_6474
func_6475 = relay.Function([], output)
mod['func_6475'] = func_6475
mod = relay.transform.InferType()(mod)
output = func_6475()
func_6476 = relay.Function([], output)
mutated_mod['func_6476'] = func_6476
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6538 = relay.const([[[0.287179,-6.090080,6.775751,1.640624,-4.123881],[1.596162,8.523276,5.882192,3.019181,8.148763],[5.064618,4.325334,3.660439,6.924710,5.098999],[7.742135,0.382813,9.525718,6.830412,9.342874]],[[5.050548,-1.408138,8.519429,0.577741,3.697018],[3.508159,2.753612,9.118514,-7.536239,6.720222],[5.996651,-7.700974,-8.721545,4.112471,-3.404108],[0.087987,2.728181,6.406543,0.239202,0.537403]],[[6.913706,-9.470486,-8.360068,1.551623,-8.718801],[-2.121738,-1.838406,-5.762450,8.912448,-3.054561],[-6.238321,8.769705,3.467475,-3.472462,-5.633751],[9.706842,9.795708,-7.678272,-4.065969,-5.505385]],[[-2.650186,-5.009909,-9.517482,7.837976,7.565320],[5.240497,2.461266,4.032872,2.516800,5.914565],[-2.831348,9.331525,-0.613588,0.812139,-1.560262],[-2.768217,-7.309086,6.048603,6.835344,-7.867981]],[[-8.944998,4.178758,8.010850,-8.814006,-4.327339],[-1.629944,-2.292711,-9.113817,0.237257,8.423068],[-1.974731,-7.768536,6.844774,7.880888,-5.062577],[8.099277,9.628207,-7.856801,5.878892,-7.254955]],[[-4.390263,-9.761909,-3.511152,-2.110017,-1.058572],[9.357696,6.023825,-0.510818,7.762474,3.364114],[1.046740,-0.851277,3.962015,6.665195,2.764488],[9.134472,-7.404256,3.916114,-7.276210,-3.252235]],[[3.445886,6.983020,0.990519,0.381315,6.992654],[-6.087231,3.387137,-5.056838,5.389256,-6.128936],[8.965657,6.199498,6.132415,-9.966587,-3.946935],[9.364309,4.705293,-2.204192,-1.335534,3.650221]],[[-2.929322,-0.100438,0.287783,8.947472,6.885049],[5.497485,7.504411,-1.138630,2.900392,-8.013872],[-0.699230,-6.375227,6.908622,-4.534005,-5.197823],[3.851445,-9.521774,3.233101,-8.005427,-0.985733]],[[-6.189100,-7.016115,-3.070288,-3.095038,-3.308617],[9.048405,-5.484783,-7.276971,-8.113096,4.438549],[-2.413596,-8.224095,4.968950,-2.246601,-3.871770],[6.011843,1.905288,-5.347850,-8.843442,9.158443]],[[4.131958,8.930873,-2.613717,0.153328,8.053712],[-0.303812,-8.562706,-3.889678,-1.562835,9.777889],[0.598069,0.948963,3.233240,0.825517,-0.233079],[-0.951518,8.391763,-1.835164,2.620341,4.874253]],[[-9.762289,-9.550761,-9.381318,-3.380811,-7.092010],[1.565504,-8.587251,-6.262596,-4.063248,-8.374898],[-6.884674,-0.781386,-9.588262,-8.797240,8.433887],[-8.051218,5.971588,-3.848838,7.539254,-4.996293]],[[-3.639508,-3.130710,-4.529994,-9.808403,-5.163145],[7.541662,3.600716,-3.606683,-2.324674,8.447148],[-0.321322,-1.102371,1.805155,9.818085,7.560130],[-0.655686,8.377102,0.478586,1.985879,-0.984157]],[[-0.907750,-4.251091,-6.728198,0.210483,1.086646],[-7.491197,7.488184,7.823002,4.738588,7.530801],[-5.152063,-3.253608,-2.312955,0.986883,-7.899375],[4.914092,-4.771658,-4.857400,1.327166,6.954025]]], dtype = "float64")#candidate|6538|(13, 4, 5)|const|float64
uop_6539 = relay.asin(const_6538.astype('float64')) # shape=(13, 4, 5)
output = uop_6539
output2 = uop_6539
func_6543 = relay.Function([], output)
mod['func_6543'] = func_6543
mod = relay.transform.InferType()(mod)
output = func_6543()
func_6544 = relay.Function([], output)
mutated_mod['func_6544'] = func_6544
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6623 = relay.const(5, dtype = "int32")#candidate|6623|()|const|int32
var_6624 = relay.var("var_6624", dtype = "int32", shape = (15, 2, 16))#candidate|6624|(15, 2, 16)|var|int32
bop_6625 = relay.add(const_6623.astype('int32'), var_6624.astype('int32')) # shape=(15, 2, 16)
func_1166_call = mod.get_global_var('func_1166')
func_1167_call = mutated_mod.get_global_var('func_1167')
call_6629 = relay.TupleGetItem(func_1166_call(), 0)
call_6630 = relay.TupleGetItem(func_1167_call(), 0)
func_2129_call = mod.get_global_var('func_2129')
func_2131_call = mutated_mod.get_global_var('func_2131')
call_6638 = relay.TupleGetItem(func_2129_call(), 0)
call_6639 = relay.TupleGetItem(func_2131_call(), 0)
var_6654 = relay.var("var_6654", dtype = "float64", shape = (9, 15, 4))#candidate|6654|(9, 15, 4)|var|float64
bop_6655 = relay.logical_and(call_6629.astype('bool'), relay.reshape(var_6654.astype('bool'), relay.shape_of(call_6629))) # shape=(9, 15, 4)
bop_6658 = relay.logical_and(call_6630.astype('bool'), relay.reshape(var_6654.astype('bool'), relay.shape_of(call_6630))) # shape=(9, 15, 4)
output = relay.Tuple([bop_6625,call_6638,bop_6655,])
output2 = relay.Tuple([bop_6625,call_6639,bop_6658,])
F = relay.Function([var_6624,var_6654,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6624,var_6654,], output2)
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
