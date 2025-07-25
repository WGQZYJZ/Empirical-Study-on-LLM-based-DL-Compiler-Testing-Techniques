import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_46 = relay.const([[[-9.408817,7.849659,3.610031,2.607033,4.856320,-4.663201,-8.454981],[3.485823,3.632330,4.423333,-8.769190,-7.380060,7.706621,0.200721],[8.096973,5.999295,-4.356633,7.517697,9.861849,-6.574128,6.554837],[6.049527,9.264463,9.576135,6.496890,2.361242,-6.008392,-1.576358],[4.648150,-9.626488,-8.391504,-9.441828,-9.343534,5.827706,-5.838130],[-9.387267,-8.887368,-2.060772,5.200678,-3.373619,-7.060625,-4.442616],[6.331659,8.122510,-6.434904,-2.205803,8.113486,-1.188121,-3.138868],[6.568440,1.390610,-9.485980,-8.455039,4.964335,-1.351542,-2.991654],[-9.325031,6.623634,4.116545,-9.687907,4.013835,2.403749,2.638064],[-5.978077,6.854048,-1.617939,-0.130695,-4.469807,7.117618,-7.123061]],[[-2.815062,3.938064,0.728121,-5.724826,2.290863,4.783413,1.295897],[7.111892,-8.165708,5.308693,-0.909029,-7.475176,-3.272560,6.397883],[-4.823670,-9.578828,-6.122844,8.423078,-4.356900,-3.137738,-2.193189],[-0.287804,-3.169776,-2.870999,-5.101596,-1.212769,-1.010396,3.489810],[-6.677262,-8.903622,-1.726620,3.668662,-2.916607,-6.263333,-4.299848],[-1.506653,-4.751490,8.699247,2.558702,0.516458,2.318227,-1.938466],[-1.275686,-2.485544,-7.821783,-4.241693,0.910091,2.133397,-7.382195],[3.757291,-7.736308,-8.669006,-4.603072,-5.979857,4.429503,9.500199],[0.308398,-0.726748,4.659353,-7.304468,-1.470794,-5.988991,-3.232322],[5.994904,-8.980545,-8.521806,3.329248,0.322007,-1.930184,0.781279]],[[-5.014623,-2.633804,-7.033896,4.219414,7.113538,1.419349,-7.503657],[-0.137289,7.201770,-8.082392,-0.774135,-5.046673,6.690559,0.643740],[1.916719,0.327963,-2.729374,-7.491351,1.429154,-7.283637,5.124976],[-8.973552,-3.671782,6.482417,-5.432776,6.599233,-8.918443,-3.784654],[6.913735,2.352308,-0.538722,-2.684349,-2.850809,0.126097,6.504367],[-9.511631,4.649470,-9.062443,0.306116,8.952281,2.448202,-9.262875],[0.301655,0.063382,0.434378,3.942667,-8.259180,-4.608398,-8.716759],[-6.793461,0.239648,2.923270,0.383938,-6.674947,4.217917,-2.044643],[-5.263312,-9.325487,-3.965394,7.519708,-2.779909,0.159518,-0.215013],[9.862295,-6.314453,-9.909187,-9.012933,-2.093064,-9.763965,7.739433]],[[9.119073,-6.478049,-2.235589,6.951261,0.931221,-0.140395,1.569397],[-0.323472,3.137127,5.628914,2.489843,-3.749666,5.379044,3.476240],[4.993824,9.205607,-7.383107,7.667457,-4.963262,3.880002,1.879858],[1.395346,-4.699394,-6.287480,9.097166,5.533462,-2.391526,-7.719562],[-8.226718,7.175348,-6.854848,-7.008835,-2.072194,-2.456765,-0.606287],[-5.266701,6.637993,7.260424,0.897103,-3.975178,9.604253,9.821160],[3.725243,2.417177,0.778174,6.097304,2.714587,9.034263,1.629571],[-5.217172,6.026501,1.497790,-6.833462,-1.925567,2.332840,-9.719086],[-9.065483,-9.199317,3.960961,-6.374278,-3.132992,7.934207,3.788136],[1.020974,-4.069980,3.974220,3.666398,-4.037182,8.384645,7.035742]],[[3.519045,7.920864,-8.924233,3.983194,0.353136,-7.490016,-0.086793],[2.036874,-0.231413,-9.263814,-7.472200,6.813919,3.099100,6.851324],[-3.020444,2.786471,-1.345615,-9.965928,-2.897808,-3.824879,5.739646],[7.130998,-4.958612,5.059429,4.453907,0.812314,6.396407,1.933101],[5.443166,3.845837,-3.052165,9.657275,4.903414,5.584169,-4.865571],[3.584127,-6.236515,7.749373,2.106561,-4.429755,-9.394636,-8.787717],[-3.043697,-7.930088,-1.335843,5.253143,-8.964157,3.205563,-9.757132],[4.330132,6.978340,-2.319120,7.971635,-0.800274,3.205061,-1.898845],[7.156454,2.861687,-5.623202,0.352308,-6.230295,5.739281,5.977240],[-8.812821,5.715507,-8.034356,8.898594,1.560914,-1.681038,6.390460]],[[-5.476186,-3.637857,8.957075,5.734458,9.794202,-1.997515,4.091549],[0.362302,7.496093,9.868909,2.160064,4.389062,-1.821091,-2.857553],[-9.334978,-0.928122,7.317046,-6.996111,5.084646,-2.074012,-6.597078],[-9.019144,1.543502,8.666381,0.219639,1.330338,-6.428361,2.840593],[1.505174,-4.254656,-7.138072,-0.064584,3.831423,-0.214681,-5.586243],[8.139373,3.092596,5.505448,8.121834,4.263907,9.876011,-9.192673],[6.521833,-2.202418,0.923446,1.662700,-3.078314,0.809602,-2.854682],[-7.538539,-7.506205,-9.454826,8.307282,-6.789565,-2.398600,3.838464],[8.446787,5.064627,-8.999190,5.028992,-7.341346,6.843516,0.458418],[-7.676307,-6.846982,-8.530944,0.814173,-9.542273,-7.211997,1.076574]],[[9.239292,-9.623558,-7.875772,6.489075,-0.940879,-5.975124,9.802964],[9.354324,-5.867098,1.435704,-1.860471,-4.199810,-9.359360,-0.893557],[2.933161,5.768076,-4.118932,6.871502,6.819863,6.510119,-4.828005],[3.093685,2.597511,-0.780311,-4.405355,-2.809455,3.940233,-7.399647],[-7.965068,4.573770,7.786178,-4.916041,-9.576994,-1.050972,-8.035473],[6.970101,-4.807545,2.052440,7.358864,9.761291,1.284827,-7.666002],[-3.521030,-5.242966,5.619790,4.353692,-1.538035,4.226376,1.151239],[-3.426234,2.215639,-2.672323,-5.374547,-0.528227,4.812995,-4.539341],[9.871271,-2.722043,1.601409,-7.514886,-3.687158,6.984876,1.030647],[5.736691,8.754514,4.993513,-7.486323,-2.727659,8.812493,-0.380294]],[[-8.416805,3.556391,-7.581065,-3.433493,-1.503812,-7.526999,-4.769858],[6.267105,-3.990727,-3.252381,-7.669701,6.407152,-1.494209,-5.419328],[-1.820373,-4.468059,1.231189,-8.449271,8.883940,7.203458,-2.617738],[-4.352229,-7.915370,-3.953509,3.397166,-7.827420,-4.464259,-6.886032],[9.567298,-2.766825,5.903068,-8.121260,-0.479281,-9.266064,8.205403],[7.311026,-4.517522,-6.531912,0.079115,7.694946,-2.067709,7.136884],[5.500069,4.613032,-2.919921,-7.390437,-9.615595,-9.462779,-3.668911],[4.376921,-6.781033,5.353289,-6.921137,3.273805,-5.385104,-2.468066],[-8.073085,-9.288746,5.223987,-4.673120,3.722567,-9.346300,-8.462444],[4.112094,2.954382,-5.171188,1.638957,-7.014607,-2.531540,-8.203793]],[[3.380933,1.842703,-9.876914,6.677146,5.553938,7.941145,5.248697],[-6.493074,-0.203877,-3.681361,-6.306946,7.279987,-5.795570,-9.553412],[-2.246293,7.951546,1.520305,0.871945,-1.326608,-0.856723,6.317978],[3.440615,6.723695,-0.371453,3.359012,6.084004,1.057945,0.934186],[0.514939,-6.830336,-7.272189,7.191704,-8.221834,0.434938,9.817252],[-8.045672,9.171387,9.561217,-8.931655,-9.714936,-1.977470,7.167763],[6.795561,2.223974,-1.209418,-3.730304,-5.065061,7.900625,-9.620697],[8.385750,-4.377901,-1.382124,6.857154,-2.095703,5.971844,0.766695],[-1.844499,-1.942872,-9.729209,-3.413803,5.848659,8.376438,-5.825616],[2.905527,-4.648051,2.940382,-2.854035,-2.056084,4.958181,4.374873]],[[-5.544059,0.967918,-4.664842,-0.035772,1.259738,0.856905,7.059638],[-7.249237,3.280717,-7.906952,5.391470,-8.785705,-7.228584,7.783484],[7.211286,-2.735554,-7.219250,5.741660,5.733236,1.107085,-3.494406],[-1.435685,7.607670,-5.531607,-1.169023,-1.279192,-3.729033,8.790579],[-6.699110,-0.519682,-0.376305,2.100636,-2.631122,2.219154,-6.179131],[7.420385,9.911820,-9.315535,-0.636901,-9.240031,8.434504,-6.522773],[3.815882,-5.702438,1.709549,-3.861302,-8.642882,-2.320895,-4.755102],[-7.112540,-1.328540,3.343557,4.793152,-7.448840,-6.817697,-0.918753],[-1.232601,2.599917,8.100376,9.324191,5.237312,-1.853970,2.802958],[-4.130318,-0.916944,-2.000535,-4.566641,-8.448511,2.724713,-3.482451]],[[2.736918,3.369838,9.175310,-8.441791,0.815477,0.457903,5.499571],[-9.621542,-1.318124,-5.639898,3.729557,9.508559,-1.069424,-6.252354],[6.861522,-8.164907,0.837738,-8.301934,-0.405354,4.029789,-6.188408],[-6.083754,-6.320112,-6.827189,-5.347342,0.962647,0.453146,2.861316],[6.733941,8.329522,-4.781659,7.263180,6.464147,1.440198,-7.717769],[6.442072,0.471350,-2.030796,-9.147281,3.211574,0.759474,0.555533],[4.034635,3.028730,-3.641721,1.249865,-8.722885,-5.445783,-7.428061],[4.855112,4.607580,5.447043,3.760442,-6.501653,-8.603559,-2.828350],[5.105207,-5.394708,-2.256930,5.804053,-7.555037,-5.215086,5.942085],[7.249146,-3.437103,3.308756,7.690379,-2.128354,-3.317781,8.047818]],[[-2.367082,6.537836,4.953682,9.661523,6.722430,-7.970074,7.397093],[-6.223543,7.900780,6.108004,-2.112782,7.245582,4.260818,-0.171598],[6.380664,6.583797,3.052863,5.176891,-0.348254,7.994761,1.166545],[-4.677791,-2.298924,7.205798,-1.670975,5.639668,9.401067,-0.816240],[-1.331989,7.956574,-1.655413,-9.352577,7.090707,-6.064868,-0.760785],[7.520828,8.943188,-8.865017,-1.599739,-0.395373,-3.684437,1.884684],[-8.297774,1.952253,7.551371,-1.252960,3.313418,1.771956,-7.981479],[-8.998555,8.958622,-3.167260,6.578005,-7.345649,0.632045,-2.653825],[-3.828358,0.550361,-7.072950,-4.945493,5.558182,8.176088,2.665429],[7.525157,2.234818,-1.618519,3.521713,6.888494,0.017803,-2.611038]],[[-8.996516,7.586305,7.203653,-8.614674,5.743899,0.046100,7.717110],[7.930644,1.892605,2.853356,-8.935907,-1.505290,-2.188766,4.467054],[4.059282,-6.330925,-3.698800,5.398614,4.251554,4.840030,-4.618391],[6.690880,-2.177723,-3.023218,-8.653049,-9.921290,2.314445,-4.473228],[-0.733902,7.529376,-0.644056,-4.779098,1.423533,-0.760570,0.610709],[0.235680,-6.734566,8.158361,8.447432,-9.255958,5.837223,8.062277],[9.392442,5.960286,9.298120,-7.244455,-7.579181,-3.861945,-6.556782],[-9.120112,9.896099,7.926543,0.334395,-7.566981,-3.935507,-5.477588],[0.179424,-5.489244,0.586394,-7.203922,-0.471270,-2.271771,6.143805],[7.419150,4.876260,7.075542,8.362661,-7.086734,-6.796688,-4.223901]],[[-0.961227,-8.618346,-8.554772,-4.375969,-3.225476,-3.253321,1.558361],[-3.443838,1.046052,-4.544767,8.758957,1.731516,-5.677216,0.510805],[-2.770649,1.062777,-5.082635,-4.760195,-0.662762,8.864393,-7.127721],[-3.699797,-7.966485,-9.906011,-1.165837,7.413896,1.753743,-4.301708],[-5.675740,-3.041441,1.530604,5.161827,5.544629,-0.134429,7.906135],[2.117823,4.006833,7.763046,-5.211015,-7.418625,3.831846,-1.042745],[-2.742145,-4.214368,9.045692,-2.503009,3.917009,-1.372463,7.828425],[-7.051998,-4.096107,-8.407755,6.967621,-7.163036,-5.210203,-3.090685],[-2.481936,-1.258893,-7.238005,3.492110,3.700132,-3.131805,-3.526886],[1.281867,-0.631306,-7.865160,4.443461,-0.519800,-0.106919,-6.529908]]], dtype = "float64")#candidate|46|(14, 10, 7)|const|float64
uop_47 = relay.erf(const_46.astype('float64')) # shape=(14, 10, 7)
uop_64 = relay.sinh(uop_47.astype('float64')) # shape=(14, 10, 7)
output = relay.Tuple([uop_64,])
output2 = relay.Tuple([uop_64,])
func_75 = relay.Function([], output)
mod['func_75'] = func_75
mod = relay.transform.InferType()(mod)
output = func_75()
func_76 = relay.Function([], output)
mutated_mod['func_76'] = func_76
mutated_mod = relay.transform.InferType()(mutated_mod)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_93 = relay.TupleGetItem(func_75_call(), 0)
call_94 = relay.TupleGetItem(func_76_call(), 0)
uop_101 = relay.log10(call_93.astype('float32')) # shape=(14, 10, 7)
uop_103 = relay.log10(call_94.astype('float32')) # shape=(14, 10, 7)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_118 = relay.TupleGetItem(func_75_call(), 0)
call_119 = relay.TupleGetItem(func_76_call(), 0)
bop_130 = relay.power(call_118.astype('float64'), relay.reshape(call_93.astype('float64'), relay.shape_of(call_118))) # shape=(14, 10, 7)
bop_133 = relay.power(call_119.astype('float64'), relay.reshape(call_94.astype('float64'), relay.shape_of(call_119))) # shape=(14, 10, 7)
output = relay.Tuple([uop_101,bop_130,])
output2 = relay.Tuple([uop_103,bop_133,])
func_139 = relay.Function([], output)
mod['func_139'] = func_139
mod = relay.transform.InferType()(mod)
mutated_mod['func_139'] = func_139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mutated_mod.get_global_var('func_139')
call_140 = func_139_call()
output = call_140
func_141 = relay.Function([], output)
mutated_mod['func_141'] = func_141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_141_call = mutated_mod.get_global_var('func_141')
call_153 = relay.TupleGetItem(func_139_call(), 1)
call_154 = relay.TupleGetItem(func_141_call(), 1)
uop_160 = relay.exp(call_153.astype('float32')) # shape=(14, 10, 7)
uop_162 = relay.exp(call_154.astype('float32')) # shape=(14, 10, 7)
var_169 = relay.var("var_169", dtype = "float32", shape = (14, 10, 7))#candidate|169|(14, 10, 7)|var|float32
bop_170 = relay.floor_mod(uop_160.astype('float32'), relay.reshape(var_169.astype('float32'), relay.shape_of(uop_160))) # shape=(14, 10, 7)
bop_173 = relay.floor_mod(uop_162.astype('float32'), relay.reshape(var_169.astype('float32'), relay.shape_of(uop_162))) # shape=(14, 10, 7)
bop_174 = relay.logical_and(bop_170.astype('bool'), relay.reshape(uop_160.astype('bool'), relay.shape_of(bop_170))) # shape=(14, 10, 7)
bop_177 = relay.logical_and(bop_173.astype('bool'), relay.reshape(uop_162.astype('bool'), relay.shape_of(bop_173))) # shape=(14, 10, 7)
output = relay.Tuple([bop_174,])
output2 = relay.Tuple([bop_177,])
func_181 = relay.Function([var_169,], output)
mod['func_181'] = func_181
mod = relay.transform.InferType()(mod)
var_182 = relay.var("var_182", dtype = "float32", shape = (14, 10, 7))#candidate|182|(14, 10, 7)|var|float32
output = func_181(var_182)
func_183 = relay.Function([var_182], output)
mutated_mod['func_183'] = func_183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_209 = relay.TupleGetItem(func_75_call(), 0)
call_210 = relay.TupleGetItem(func_76_call(), 0)
uop_216 = relay.atanh(call_209.astype('float32')) # shape=(14, 10, 7)
uop_218 = relay.atanh(call_210.astype('float32')) # shape=(14, 10, 7)
output = relay.Tuple([uop_216,])
output2 = relay.Tuple([uop_218,])
func_223 = relay.Function([], output)
mod['func_223'] = func_223
mod = relay.transform.InferType()(mod)
output = func_223()
func_224 = relay.Function([], output)
mutated_mod['func_224'] = func_224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_233 = relay.TupleGetItem(func_223_call(), 0)
call_234 = relay.TupleGetItem(func_224_call(), 0)
uop_248 = relay.sqrt(call_233.astype('float64')) # shape=(14, 10, 7)
uop_250 = relay.sqrt(call_234.astype('float64')) # shape=(14, 10, 7)
output = relay.Tuple([uop_248,])
output2 = relay.Tuple([uop_250,])
func_252 = relay.Function([], output)
mod['func_252'] = func_252
mod = relay.transform.InferType()(mod)
output = func_252()
func_253 = relay.Function([], output)
mutated_mod['func_253'] = func_253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_298 = relay.TupleGetItem(func_75_call(), 0)
call_299 = relay.TupleGetItem(func_76_call(), 0)
func_181_call = mod.get_global_var('func_181')
func_183_call = mutated_mod.get_global_var('func_183')
call_308 = relay.TupleGetItem(func_181_call(relay.reshape(call_298.astype('float32'), [14, 10, 7])), 0)
call_309 = relay.TupleGetItem(func_183_call(relay.reshape(call_298.astype('float32'), [14, 10, 7])), 0)
output = relay.Tuple([call_298,call_308,])
output2 = relay.Tuple([call_299,call_309,])
func_311 = relay.Function([], output)
mod['func_311'] = func_311
mod = relay.transform.InferType()(mod)
mutated_mod['func_311'] = func_311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_311_call = mutated_mod.get_global_var('func_311')
call_312 = func_311_call()
output = call_312
func_313 = relay.Function([], output)
mutated_mod['func_313'] = func_313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_253_call = mutated_mod.get_global_var('func_253')
call_365 = relay.TupleGetItem(func_252_call(), 0)
call_366 = relay.TupleGetItem(func_253_call(), 0)
output = relay.Tuple([call_365,])
output2 = relay.Tuple([call_366,])
func_376 = relay.Function([], output)
mod['func_376'] = func_376
mod = relay.transform.InferType()(mod)
output = func_376()
func_377 = relay.Function([], output)
mutated_mod['func_377'] = func_377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_311_call = mod.get_global_var('func_311')
func_313_call = mutated_mod.get_global_var('func_313')
call_388 = relay.TupleGetItem(func_311_call(), 0)
call_389 = relay.TupleGetItem(func_313_call(), 0)
output = relay.Tuple([call_388,])
output2 = relay.Tuple([call_389,])
func_391 = relay.Function([], output)
mod['func_391'] = func_391
mod = relay.transform.InferType()(mod)
output = func_391()
func_392 = relay.Function([], output)
mutated_mod['func_392'] = func_392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_413 = relay.TupleGetItem(func_223_call(), 0)
call_414 = relay.TupleGetItem(func_224_call(), 0)
var_426 = relay.var("var_426", dtype = "float32", shape = (14, 10, 7))#candidate|426|(14, 10, 7)|var|float32
bop_427 = relay.not_equal(call_413.astype('bool'), relay.reshape(var_426.astype('bool'), relay.shape_of(call_413))) # shape=(14, 10, 7)
bop_430 = relay.not_equal(call_414.astype('bool'), relay.reshape(var_426.astype('bool'), relay.shape_of(call_414))) # shape=(14, 10, 7)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_434 = relay.TupleGetItem(func_391_call(), 0)
call_435 = relay.TupleGetItem(func_392_call(), 0)
uop_441 = relay.atan(call_413.astype('float64')) # shape=(14, 10, 7)
uop_443 = relay.atan(call_414.astype('float64')) # shape=(14, 10, 7)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_444 = relay.TupleGetItem(func_376_call(), 0)
call_445 = relay.TupleGetItem(func_377_call(), 0)
func_252_call = mod.get_global_var('func_252')
func_253_call = mutated_mod.get_global_var('func_253')
call_446 = relay.TupleGetItem(func_252_call(), 0)
call_447 = relay.TupleGetItem(func_253_call(), 0)
output = relay.Tuple([bop_427,call_434,uop_441,call_444,call_446,])
output2 = relay.Tuple([bop_430,call_435,uop_443,call_445,call_447,])
func_463 = relay.Function([var_426,], output)
mod['func_463'] = func_463
mod = relay.transform.InferType()(mod)
mutated_mod['func_463'] = func_463
mutated_mod = relay.transform.InferType()(mutated_mod)
var_464 = relay.var("var_464", dtype = "float32", shape = (14, 10, 7))#candidate|464|(14, 10, 7)|var|float32
func_463_call = mutated_mod.get_global_var('func_463')
call_465 = func_463_call(var_464)
output = call_465
func_466 = relay.Function([var_464], output)
mutated_mod['func_466'] = func_466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_253_call = mutated_mod.get_global_var('func_253')
call_468 = relay.TupleGetItem(func_252_call(), 0)
call_469 = relay.TupleGetItem(func_253_call(), 0)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_477 = relay.TupleGetItem(func_223_call(), 0)
call_478 = relay.TupleGetItem(func_224_call(), 0)
bop_491 = relay.equal(call_477.astype('bool'), relay.reshape(call_468.astype('bool'), relay.shape_of(call_477))) # shape=(14, 10, 7)
bop_494 = relay.equal(call_478.astype('bool'), relay.reshape(call_469.astype('bool'), relay.shape_of(call_478))) # shape=(14, 10, 7)
output = relay.Tuple([bop_491,])
output2 = relay.Tuple([bop_494,])
func_497 = relay.Function([], output)
mod['func_497'] = func_497
mod = relay.transform.InferType()(mod)
mutated_mod['func_497'] = func_497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_497_call = mutated_mod.get_global_var('func_497')
call_498 = func_497_call()
output = call_498
func_499 = relay.Function([], output)
mutated_mod['func_499'] = func_499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_542 = relay.TupleGetItem(func_75_call(), 0)
call_543 = relay.TupleGetItem(func_76_call(), 0)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_546 = relay.TupleGetItem(func_75_call(), 0)
call_547 = relay.TupleGetItem(func_76_call(), 0)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_564 = relay.TupleGetItem(func_223_call(), 0)
call_565 = relay.TupleGetItem(func_224_call(), 0)
output = relay.Tuple([call_542,call_546,call_564,])
output2 = relay.Tuple([call_543,call_547,call_565,])
func_568 = relay.Function([], output)
mod['func_568'] = func_568
mod = relay.transform.InferType()(mod)
mutated_mod['func_568'] = func_568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_568_call = mutated_mod.get_global_var('func_568')
call_569 = func_568_call()
output = call_569
func_570 = relay.Function([], output)
mutated_mod['func_570'] = func_570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_615 = relay.var("var_615", dtype = "int16", shape = (2, 14, 10))#candidate|615|(2, 14, 10)|var|int16
var_616 = relay.var("var_616", dtype = "int16", shape = (2, 14, 10))#candidate|616|(2, 14, 10)|var|int16
bop_617 = relay.subtract(var_615.astype('int16'), relay.reshape(var_616.astype('int16'), relay.shape_of(var_615))) # shape=(2, 14, 10)
output = bop_617
output2 = bop_617
func_621 = relay.Function([var_615,var_616,], output)
mod['func_621'] = func_621
mod = relay.transform.InferType()(mod)
var_622 = relay.var("var_622", dtype = "int16", shape = (2, 14, 10))#candidate|622|(2, 14, 10)|var|int16
var_623 = relay.var("var_623", dtype = "int16", shape = (2, 14, 10))#candidate|623|(2, 14, 10)|var|int16
output = func_621(var_622,var_623,)
func_624 = relay.Function([var_622,var_623,], output)
mutated_mod['func_624'] = func_624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_723 = relay.TupleGetItem(func_223_call(), 0)
call_724 = relay.TupleGetItem(func_224_call(), 0)
const_731 = relay.const([[[-6.083473,7.938246,6.394951,6.796154,-4.880708,-1.263084,-5.811638],[5.952399,6.609179,8.531460,-0.375581,7.957551,6.554210,8.992257],[5.126781,7.581767,-3.386008,8.616583,-8.167466,-6.361034,-4.922443],[-9.092042,-2.837149,-3.759866,2.817072,0.361647,-1.578572,-2.208007],[-8.028035,-4.174538,-2.127894,4.214944,-8.778951,-4.587951,-5.553646],[5.368839,5.851270,8.388140,4.684944,6.857067,2.346123,-7.664038],[3.479101,9.937968,-7.738402,-4.096508,3.957067,7.678652,-2.545414],[-7.387465,2.534458,1.581820,6.577818,-7.240952,8.701342,-7.197611],[-8.332887,-8.105959,0.064135,-0.912451,0.864852,-2.246938,-0.077608],[-9.196225,8.330759,9.093355,-0.093057,4.617176,-5.475874,-2.279305]],[[1.010739,-7.531517,-0.319556,-2.729552,2.664585,4.585206,8.121928],[5.037851,-1.669620,-0.676496,9.524741,-8.495528,-0.358044,7.276486],[2.780340,-5.129537,-6.319706,-0.799608,-8.696232,-5.498092,0.859305],[-4.278077,9.865504,6.742875,-7.502472,7.077693,9.317479,6.438014],[3.460536,-5.141096,5.099234,-3.974457,-0.897953,-3.932629,7.135855],[-7.009741,-6.737517,1.328633,-9.745994,1.320120,-3.893278,-4.740181],[-5.608145,8.789643,8.914961,-9.914873,0.472290,-1.763750,-0.836295],[-4.371594,-0.632129,-1.366453,2.605294,-4.681034,-6.494728,-9.716973],[0.553369,0.150838,0.165033,8.785425,-5.119252,1.835761,-0.522021],[6.007854,-4.006559,-1.944858,-6.424211,8.039411,-9.759850,-7.682273]],[[-0.424757,2.518258,0.253953,3.086106,-4.444489,0.020557,3.104501],[-7.759624,1.412303,-2.404254,7.964309,-4.510535,0.008219,1.790679],[7.503787,7.501932,2.240058,2.243467,7.368915,2.487136,-5.768848],[-0.263431,3.564102,9.186746,8.348746,-8.444578,8.809418,-1.740218],[-7.997326,-6.708430,6.185636,3.154219,4.230007,-1.164086,-5.793685],[-2.509179,-0.336690,-5.233906,6.502973,-9.255964,8.498617,4.630370],[3.802862,2.816543,6.251534,-3.408775,4.375102,5.253922,-0.909875],[8.898455,9.652497,5.307334,7.799373,8.152922,-4.894857,7.966623],[-0.385389,-5.283338,-4.929431,-7.562874,0.180640,3.491406,-9.373275],[4.346168,-6.707539,9.300135,-6.330622,6.999987,-1.633194,-7.778262]],[[3.282634,-4.698313,-3.537196,3.656476,3.582590,3.552460,-4.332328],[7.249942,5.523933,-1.921063,-2.050515,-2.432008,-5.360100,-0.898259],[-4.333608,4.197379,-4.542402,-6.791283,-5.358645,7.426399,8.858739],[9.875448,6.385237,-2.138339,6.064471,-3.530230,7.763016,4.390851],[1.731708,-2.171765,-3.632337,1.133057,-4.503705,-6.485255,8.593589],[-6.925192,-3.463028,8.411766,-4.365092,-2.074303,-6.814761,2.767347],[5.701137,7.602933,-9.870510,3.061444,-4.167941,2.430187,-0.009811],[4.768171,-7.135735,-2.123662,8.253110,-7.557808,3.616838,-6.309958],[-6.692410,7.581601,-0.788888,-1.568341,5.796625,7.260941,-8.458241],[-4.601547,-0.122359,-8.514310,2.267645,6.322585,-6.791115,-4.693581]],[[1.017328,1.395954,6.436901,3.681521,-6.735986,-6.447117,6.977241],[5.823201,0.908753,-4.148037,8.251423,-7.381067,2.241088,-9.185176],[1.752477,-8.464476,8.997696,-1.733769,-5.652386,-9.961251,5.351722],[-1.041094,-6.629891,-2.524911,9.805242,-8.325227,-8.072928,7.799643],[-1.360275,9.697757,6.487539,-5.726552,-1.756045,7.579923,4.553378],[1.465828,-1.175727,5.819643,5.473448,-8.865260,0.016302,4.575507],[1.874768,6.805747,-2.106026,-9.212324,-2.543041,-2.309400,2.983800],[-6.828890,9.907844,-5.815716,6.725861,6.012818,6.946011,-3.828383],[-3.876995,-8.351401,-9.082068,7.340874,6.881189,-7.474666,9.286833],[-2.767101,-6.743812,6.725036,-1.591818,-3.986018,6.975155,-0.766121]],[[6.930264,3.517076,-2.655066,-7.717353,-1.894063,-9.224353,3.115040],[8.214118,3.182848,4.365690,-9.429759,-7.943219,-8.754315,1.796726],[-5.541054,5.959630,-1.773398,8.484958,-5.341511,6.773873,8.412088],[-4.170205,0.677514,6.961427,0.944114,-7.090980,2.677458,-1.567819],[1.548138,-6.653915,1.361428,-8.781926,-7.367865,9.159035,0.087244],[4.438316,-5.595527,9.809944,-3.579111,-3.903642,2.399141,2.436155],[2.710903,6.003343,9.262880,-3.361231,4.000452,-0.958275,-0.992983],[-1.189390,0.001977,2.621516,-2.719178,5.747725,9.312925,-9.833855],[-1.636349,-1.879975,-3.855479,7.492029,9.042223,-0.968603,-1.064607],[-4.863765,-1.088454,-2.980667,1.288697,7.987541,-1.274487,-4.576064]],[[3.573600,-5.548599,-9.110796,4.339811,-2.479214,2.171203,2.945801],[-0.390243,-9.419302,-5.382589,-4.712384,-1.121189,-0.825180,4.259224],[-9.920971,1.321758,-0.145126,-8.785683,-3.307993,6.445728,-2.958493],[-8.139098,2.319406,5.270444,7.969168,-5.799051,-4.145447,7.064889],[8.379263,4.261941,-9.555868,3.428915,-7.771456,-0.814703,1.290126],[-2.683663,-3.697596,5.618994,3.500898,6.227992,2.446470,-9.427485],[4.798506,-3.364271,-2.412477,-0.819872,-1.561647,-2.914239,3.811579],[3.572277,-0.081378,-3.220907,-6.106444,-4.232885,-7.115525,6.455204],[-5.178920,5.164408,0.059747,-4.220731,5.888379,2.137254,-6.174405],[4.577737,-6.219237,-4.891465,-8.212961,5.605562,8.860671,-5.333309]],[[5.902414,6.948756,-2.418655,7.235079,-0.972283,8.415809,6.398462],[-6.075537,-4.468678,6.676007,-9.986584,-8.910402,2.051167,-0.278743],[8.557083,-2.406260,-1.029472,-3.801651,7.071505,-0.926471,8.172413],[0.524683,-2.043227,-3.510574,8.990238,7.241553,-0.954789,-3.574534],[0.782967,-6.849301,-1.267628,-5.149416,-1.942669,2.138543,-0.392412],[5.881917,4.557621,-5.338147,-4.773976,8.421535,4.471260,-5.822379],[-4.082294,6.610463,3.993452,-4.313840,-6.643879,-1.283916,-2.646685],[-4.197643,7.462726,-8.316335,5.708903,1.994851,-0.324428,2.004782],[3.279843,4.129726,0.653642,-9.408163,-2.102021,-3.495951,8.023404],[8.666352,-6.857122,-2.722282,2.856000,-0.352418,-3.539501,1.191537]],[[-9.505006,-1.423393,-2.211616,2.707976,-8.898683,-6.333785,6.758613],[2.465324,8.202943,-1.464910,2.062163,6.829046,3.864265,3.293779],[2.534175,-4.049588,1.681480,-6.384372,-9.075680,7.163083,4.399837],[8.775392,-9.924722,2.135244,4.181378,3.998827,-0.333972,-5.339845],[1.215679,9.106218,-7.868753,-6.298300,-6.938710,1.962262,6.471933],[4.425472,-0.180204,7.601330,-7.902687,-2.856789,-5.614342,-2.322740],[-2.862585,-6.200527,-9.148959,3.348437,-6.283750,-3.186633,-4.050343],[6.806560,1.276294,-9.874223,-7.747266,-8.335302,-6.263855,-8.458360],[1.767953,6.271111,6.077698,0.067461,-2.226380,-0.727505,-6.733175],[6.223257,-8.178218,-1.552323,-0.872149,7.858755,-3.743359,6.044078]],[[-0.206590,9.955021,-9.349649,-2.157689,9.706375,3.701437,-3.791070],[-7.442152,-7.479870,9.319001,-7.979977,-6.988964,-8.631577,2.290752],[-0.763557,3.705551,5.920937,-3.744847,7.623733,0.530948,-6.668255],[-0.661869,2.842958,3.032142,4.950002,-4.998616,2.360300,-2.233764],[1.287781,-5.944497,-7.356847,-5.055598,7.383072,4.739968,9.186987],[0.755780,0.849729,-6.597045,-7.346333,-2.481661,-7.168325,8.213448],[-7.403381,2.273454,-0.244857,7.485297,9.267648,-7.034208,-3.219693],[-7.736576,-5.225292,8.794834,9.497716,-5.557542,4.657136,3.727164],[-0.220305,1.394926,-2.093507,-4.634387,6.959190,4.308981,1.019581],[6.877185,3.483297,-4.226064,4.688588,7.212393,3.740584,-1.756691]],[[4.961857,8.908934,-3.354222,-2.234846,3.249252,0.138462,-3.863822],[-7.689742,-3.574664,0.248142,5.960870,-1.156461,2.706543,5.485654],[1.853156,8.909393,-3.324992,-1.918889,-0.799666,8.887324,4.335222],[-8.881439,-7.514097,-7.295305,-5.888097,-2.227076,6.100537,-2.534114],[4.791591,8.723566,8.948138,0.466171,1.793964,-1.849644,-6.138397],[-2.526607,6.089650,3.561285,0.323774,-2.113088,1.229656,0.995561],[7.965367,8.944922,5.151117,-3.214795,1.112514,-3.559850,5.961132],[-4.172970,7.751711,-0.868180,0.851162,-8.515461,2.323132,-5.112182],[6.319644,5.737246,1.710604,8.723566,6.337390,1.342342,4.727774],[-8.524978,2.480782,-3.338888,4.416154,6.352378,-5.137238,5.180200]],[[-7.079231,-6.799782,5.670776,1.219770,-7.457072,2.706959,-0.418543],[9.289486,2.526640,-9.177313,-1.934100,3.379781,5.019229,1.589532],[-3.248911,3.578860,-5.116078,-1.815512,6.918219,4.658145,1.590990],[-2.399891,5.049713,3.030906,6.004484,0.843530,8.699645,5.558544],[1.953819,-2.746927,3.313194,5.058663,-3.127487,9.183994,7.676801],[3.076166,0.296273,-7.174631,3.368165,1.811758,9.548277,3.520860],[7.785794,-6.648294,6.135600,-9.486044,-3.308244,-1.035192,-2.777977],[2.073916,-4.278397,-8.599572,-9.580997,2.625688,-2.817290,-8.554937],[1.707465,-3.658601,-8.697916,-9.381918,-3.770335,-7.879319,-1.139152],[8.178385,-4.056431,-7.243646,3.383460,-6.795277,7.092467,-0.300531]],[[6.579501,8.134418,-9.442423,8.854332,-1.193634,-9.460052,3.188696],[-7.658121,8.450481,-6.580653,-3.684514,0.957224,5.501285,0.321915],[5.776706,-4.375642,-5.466099,1.927596,-4.311754,1.277717,-7.817081],[1.728115,-0.138515,0.771129,3.838275,5.981848,-8.198974,1.995450],[-2.005361,-2.141057,-2.143326,-7.708703,8.008283,8.466376,7.627735],[-2.184054,-8.271016,2.474346,2.171739,5.970428,-3.845168,-3.962639],[5.031899,-9.083308,-9.481378,4.870890,9.611083,9.377253,4.259029],[-3.147322,3.775437,9.474428,-5.390078,-8.255268,1.228187,-8.899392],[-1.449245,0.027573,4.349064,-7.093847,-1.077780,-8.959226,7.056918],[-6.921429,1.930753,6.125780,-1.265385,-3.367004,6.808027,-0.819192]],[[-5.197019,-9.959486,-7.927742,-3.673230,1.024571,4.921980,-9.674596],[-0.668332,-2.000082,2.760318,5.565718,-3.853469,8.572491,1.921171],[-1.465345,4.373268,-2.226628,3.645977,0.307793,-6.122009,-9.434051],[4.895620,-1.572026,5.021455,-5.249239,-4.154187,4.975528,9.680102],[8.746199,-4.516573,0.527167,5.701387,2.039684,-4.994861,-0.279608],[-2.433369,-0.587105,-5.312114,1.871685,6.442682,-1.197579,0.702316],[5.323445,-2.108616,4.510934,-0.088558,-0.972268,1.913338,-7.781777],[1.331439,-9.513361,-4.180460,5.781077,5.720500,-7.337059,-1.224034],[-5.347271,-6.998146,1.661097,9.059777,2.162067,7.076338,6.291794],[-4.946185,-0.932085,-4.789916,1.402860,9.189584,4.374462,0.988931]]], dtype = "float32")#candidate|731|(14, 10, 7)|const|float32
bop_732 = relay.subtract(call_723.astype('int8'), relay.reshape(const_731.astype('int8'), relay.shape_of(call_723))) # shape=(14, 10, 7)
bop_735 = relay.subtract(call_724.astype('int8'), relay.reshape(const_731.astype('int8'), relay.shape_of(call_724))) # shape=(14, 10, 7)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_743 = relay.TupleGetItem(func_223_call(), 0)
call_744 = relay.TupleGetItem(func_224_call(), 0)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_752 = relay.TupleGetItem(func_391_call(), 0)
call_753 = relay.TupleGetItem(func_392_call(), 0)
output = relay.Tuple([bop_732,call_743,call_752,])
output2 = relay.Tuple([bop_735,call_744,call_753,])
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
func_311_call = mod.get_global_var('func_311')
func_313_call = mutated_mod.get_global_var('func_313')
call_795 = relay.TupleGetItem(func_311_call(), 0)
call_796 = relay.TupleGetItem(func_313_call(), 0)
func_311_call = mod.get_global_var('func_311')
func_313_call = mutated_mod.get_global_var('func_313')
call_800 = relay.TupleGetItem(func_311_call(), 1)
call_801 = relay.TupleGetItem(func_313_call(), 1)
uop_804 = relay.log(call_795.astype('float64')) # shape=(14, 10, 7)
uop_806 = relay.log(call_796.astype('float64')) # shape=(14, 10, 7)
func_252_call = mod.get_global_var('func_252')
func_253_call = mutated_mod.get_global_var('func_253')
call_811 = relay.TupleGetItem(func_252_call(), 0)
call_812 = relay.TupleGetItem(func_253_call(), 0)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_813 = relay.TupleGetItem(func_75_call(), 0)
call_814 = relay.TupleGetItem(func_76_call(), 0)
uop_829 = relay.asin(call_800.astype('float32')) # shape=(14, 10, 7)
uop_831 = relay.asin(call_801.astype('float32')) # shape=(14, 10, 7)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_833 = relay.TupleGetItem(func_376_call(), 0)
call_834 = relay.TupleGetItem(func_377_call(), 0)
uop_848 = relay.sigmoid(call_811.astype('float32')) # shape=(14, 10, 7)
uop_850 = relay.sigmoid(call_812.astype('float32')) # shape=(14, 10, 7)
uop_856 = relay.acos(uop_829.astype('float64')) # shape=(14, 10, 7)
uop_858 = relay.acos(uop_831.astype('float64')) # shape=(14, 10, 7)
output = relay.Tuple([uop_804,call_813,call_833,uop_848,uop_856,])
output2 = relay.Tuple([uop_806,call_814,call_834,uop_850,uop_858,])
func_859 = relay.Function([], output)
mod['func_859'] = func_859
mod = relay.transform.InferType()(mod)
output = func_859()
func_860 = relay.Function([], output)
mutated_mod['func_860'] = func_860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_881 = relay.var("var_881", dtype = "int8", shape = ())#candidate|881|()|var|int8
var_882 = relay.var("var_882", dtype = "int8", shape = (13, 12, 15))#candidate|882|(13, 12, 15)|var|int8
bop_883 = relay.left_shift(var_881.astype('int8'), var_882.astype('int8')) # shape=(13, 12, 15)
bop_886 = relay.greater_equal(var_881.astype('bool'), var_882.astype('bool')) # shape=(13, 12, 15)
output = relay.Tuple([bop_883,bop_886,])
output2 = relay.Tuple([bop_883,bop_886,])
func_894 = relay.Function([var_881,var_882,], output)
mod['func_894'] = func_894
mod = relay.transform.InferType()(mod)
var_895 = relay.var("var_895", dtype = "int8", shape = ())#candidate|895|()|var|int8
var_896 = relay.var("var_896", dtype = "int8", shape = (13, 12, 15))#candidate|896|(13, 12, 15)|var|int8
output = func_894(var_895,var_896,)
func_897 = relay.Function([var_895,var_896,], output)
mutated_mod['func_897'] = func_897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_253_call = mutated_mod.get_global_var('func_253')
call_930 = relay.TupleGetItem(func_252_call(), 0)
call_931 = relay.TupleGetItem(func_253_call(), 0)
output = call_930
output2 = call_931
func_947 = relay.Function([], output)
mod['func_947'] = func_947
mod = relay.transform.InferType()(mod)
mutated_mod['func_947'] = func_947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mutated_mod.get_global_var('func_947')
call_948 = func_947_call()
output = call_948
func_949 = relay.Function([], output)
mutated_mod['func_949'] = func_949
mutated_mod = relay.transform.InferType()(mutated_mod)
var_989 = relay.var("var_989", dtype = "int32", shape = (2, 16, 10))#candidate|989|(2, 16, 10)|var|int32
var_990 = relay.var("var_990", dtype = "int32", shape = (2, 16, 10))#candidate|990|(2, 16, 10)|var|int32
bop_991 = relay.bitwise_and(var_989.astype('int32'), relay.reshape(var_990.astype('int32'), relay.shape_of(var_989))) # shape=(2, 16, 10)
output = relay.Tuple([bop_991,])
output2 = relay.Tuple([bop_991,])
func_1008 = relay.Function([var_989,var_990,], output)
mod['func_1008'] = func_1008
mod = relay.transform.InferType()(mod)
mutated_mod['func_1008'] = func_1008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1008_call = mutated_mod.get_global_var('func_1008')
var_1010 = relay.var("var_1010", dtype = "int32", shape = (2, 16, 10))#candidate|1010|(2, 16, 10)|var|int32
var_1011 = relay.var("var_1011", dtype = "int32", shape = (2, 16, 10))#candidate|1011|(2, 16, 10)|var|int32
call_1009 = func_1008_call(var_1010,var_1011,)
output = call_1009
func_1012 = relay.Function([var_1010,var_1011,], output)
mutated_mod['func_1012'] = func_1012
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1080 = relay.var("var_1080", dtype = "float64", shape = ())#candidate|1080|()|var|float64
var_1081 = relay.var("var_1081", dtype = "float64", shape = (1, 16, 5))#candidate|1081|(1, 16, 5)|var|float64
bop_1082 = relay.maximum(var_1080.astype('float64'), var_1081.astype('float64')) # shape=(1, 16, 5)
output = bop_1082
output2 = bop_1082
func_1090 = relay.Function([var_1080,var_1081,], output)
mod['func_1090'] = func_1090
mod = relay.transform.InferType()(mod)
var_1091 = relay.var("var_1091", dtype = "float64", shape = ())#candidate|1091|()|var|float64
var_1092 = relay.var("var_1092", dtype = "float64", shape = (1, 16, 5))#candidate|1092|(1, 16, 5)|var|float64
output = func_1090(var_1091,var_1092,)
func_1093 = relay.Function([var_1091,var_1092,], output)
mutated_mod['func_1093'] = func_1093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_141_call = mutated_mod.get_global_var('func_141')
call_1099 = relay.TupleGetItem(func_139_call(), 0)
call_1100 = relay.TupleGetItem(func_141_call(), 0)
output = call_1099
output2 = call_1100
func_1103 = relay.Function([], output)
mod['func_1103'] = func_1103
mod = relay.transform.InferType()(mod)
output = func_1103()
func_1104 = relay.Function([], output)
mutated_mod['func_1104'] = func_1104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_1110 = relay.TupleGetItem(func_376_call(), 0)
call_1111 = relay.TupleGetItem(func_377_call(), 0)
output = relay.Tuple([call_1110,])
output2 = relay.Tuple([call_1111,])
func_1112 = relay.Function([], output)
mod['func_1112'] = func_1112
mod = relay.transform.InferType()(mod)
output = func_1112()
func_1113 = relay.Function([], output)
mutated_mod['func_1113'] = func_1113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_253_call = mutated_mod.get_global_var('func_253')
call_1194 = relay.TupleGetItem(func_252_call(), 0)
call_1195 = relay.TupleGetItem(func_253_call(), 0)
output = relay.Tuple([call_1194,])
output2 = relay.Tuple([call_1195,])
func_1200 = relay.Function([], output)
mod['func_1200'] = func_1200
mod = relay.transform.InferType()(mod)
output = func_1200()
func_1201 = relay.Function([], output)
mutated_mod['func_1201'] = func_1201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_1202 = relay.TupleGetItem(func_75_call(), 0)
call_1203 = relay.TupleGetItem(func_76_call(), 0)
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
call_1207 = relay.TupleGetItem(func_759_call(), 0)
call_1208 = relay.TupleGetItem(func_761_call(), 0)
func_621_call = mod.get_global_var('func_621')
func_624_call = mutated_mod.get_global_var('func_624')
const_1214 = relay.const([10,-3,3,3,10,-3,-5,-9,9,6,4,2,8,3,9,-8,6,-5,-7,-2,2,-4,-6,-8,8,-6,-3,-8,-6,-2,1,-3,3,5,8,7,-3,-9,-5,3,-10,-10,9,-5,-8,-9,8,5,-2,3,8,-8,-2,1,5,-3,-2,7,10,8,8,9,9,-7,-6,9,-2,-6,-7,2,-10,-4,-7,-6,2,6,-9,-5,-9,-9,5,-1,-8,-9,-6,4,5,8,10,10,-8,-1,-1,7,-1,7,8,-2,8,1,4,8,5,3,2,7,-2,-8,5,5,4,3,-1,-10,6,-3,-7,10,-8,5,-8,9,1,3,3,-5,9,10,-10,-10,-2,-9,-3,8,5,1,-8,-3,8,-6,-3,9,-8,5,1,-6,-8,1,7,-5,3,-6,-6,9,-5,4,-7,-4,-4,-2,-6,-8,-7,-8,-8,-7,-8,-1,9,10,-8,-6,9,-9,10,-10,2,-3,-6,-3,5,-5,-2,9,10,-7,-6,-3,-2,-8,4,9,5,-6,2,-7,-1,1,-1,-5,10,9,-5,-10,3,-1,7,4,3,-5,9,-3,-4,-2,-5,-8,-8,-2,9,2,-2,-10,7,1,4,-5,9,3,-2,-10,3,3,-5,4,7,-8,3,5,2,9,5,-8,4,8,8,5,4,-3,-1,2,5,4,-8,7,9,5,-2,8,6,-3,4,4,-4,-8,3,2,2,7,8,-1,4,3,-10,-1,7,-1,-2,10,1,2], dtype = "int16")#candidate|1214|(280,)|const|int16
call_1213 = func_621_call(relay.reshape(const_1214.astype('int16'), [2, 14, 10]), relay.reshape(const_1214.astype('int16'), [2, 14, 10]), )
call_1215 = func_621_call(relay.reshape(const_1214.astype('int16'), [2, 14, 10]), relay.reshape(const_1214.astype('int16'), [2, 14, 10]), )
output = relay.Tuple([call_1202,call_1207,call_1213,const_1214,])
output2 = relay.Tuple([call_1203,call_1208,call_1215,const_1214,])
func_1219 = relay.Function([], output)
mod['func_1219'] = func_1219
mod = relay.transform.InferType()(mod)
output = func_1219()
func_1220 = relay.Function([], output)
mutated_mod['func_1220'] = func_1220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_1249 = relay.TupleGetItem(func_223_call(), 0)
call_1250 = relay.TupleGetItem(func_224_call(), 0)
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
call_1251 = relay.TupleGetItem(func_463_call(relay.reshape(call_1249.astype('float32'), [14, 10, 7])), 2)
call_1252 = relay.TupleGetItem(func_466_call(relay.reshape(call_1249.astype('float32'), [14, 10, 7])), 2)
func_1200_call = mod.get_global_var('func_1200')
func_1201_call = mutated_mod.get_global_var('func_1201')
call_1253 = relay.TupleGetItem(func_1200_call(), 0)
call_1254 = relay.TupleGetItem(func_1201_call(), 0)
var_1255 = relay.var("var_1255", dtype = "float64", shape = (14, 10, 7))#candidate|1255|(14, 10, 7)|var|float64
bop_1256 = relay.logical_xor(call_1251.astype('int32'), relay.reshape(var_1255.astype('int32'), relay.shape_of(call_1251))) # shape=(14, 10, 7)
bop_1259 = relay.logical_xor(call_1252.astype('int32'), relay.reshape(var_1255.astype('int32'), relay.shape_of(call_1252))) # shape=(14, 10, 7)
func_1090_call = mod.get_global_var('func_1090')
func_1093_call = mutated_mod.get_global_var('func_1093')
const_1263 = relay.const(-6.115331, dtype = "float64")#candidate|1263|()|const|float64
var_1264 = relay.var("var_1264", dtype = "float64", shape = (80, 1))#candidate|1264|(80, 1)|var|float64
call_1262 = func_1090_call(relay.reshape(const_1263.astype('float64'), []), relay.reshape(var_1264.astype('float64'), [1, 16, 5]), )
call_1265 = func_1090_call(relay.reshape(const_1263.astype('float64'), []), relay.reshape(var_1264.astype('float64'), [1, 16, 5]), )
uop_1275 = relay.erf(call_1262.astype('float32')) # shape=(1, 16, 5)
uop_1277 = relay.erf(call_1265.astype('float32')) # shape=(1, 16, 5)
func_497_call = mod.get_global_var('func_497')
func_499_call = mutated_mod.get_global_var('func_499')
call_1290 = relay.TupleGetItem(func_497_call(), 0)
call_1291 = relay.TupleGetItem(func_499_call(), 0)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_1310 = relay.TupleGetItem(func_376_call(), 0)
call_1311 = relay.TupleGetItem(func_377_call(), 0)
output = relay.Tuple([call_1249,call_1253,bop_1256,const_1263,var_1264,uop_1275,call_1290,call_1310,])
output2 = relay.Tuple([call_1250,call_1254,bop_1259,const_1263,var_1264,uop_1277,call_1291,call_1311,])
func_1319 = relay.Function([var_1255,var_1264,], output)
mod['func_1319'] = func_1319
mod = relay.transform.InferType()(mod)
var_1320 = relay.var("var_1320", dtype = "float64", shape = (14, 10, 7))#candidate|1320|(14, 10, 7)|var|float64
var_1321 = relay.var("var_1321", dtype = "float64", shape = (80, 1))#candidate|1321|(80, 1)|var|float64
output = func_1319(var_1320,var_1321,)
func_1322 = relay.Function([var_1320,var_1321,], output)
mutated_mod['func_1322'] = func_1322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1200_call = mod.get_global_var('func_1200')
func_1201_call = mutated_mod.get_global_var('func_1201')
call_1335 = relay.TupleGetItem(func_1200_call(), 0)
call_1336 = relay.TupleGetItem(func_1201_call(), 0)
output = relay.Tuple([call_1335,])
output2 = relay.Tuple([call_1336,])
func_1338 = relay.Function([], output)
mod['func_1338'] = func_1338
mod = relay.transform.InferType()(mod)
output = func_1338()
func_1339 = relay.Function([], output)
mutated_mod['func_1339'] = func_1339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_1396 = relay.TupleGetItem(func_859_call(), 3)
call_1397 = relay.TupleGetItem(func_860_call(), 3)
output = relay.Tuple([call_1396,])
output2 = relay.Tuple([call_1397,])
func_1413 = relay.Function([], output)
mod['func_1413'] = func_1413
mod = relay.transform.InferType()(mod)
mutated_mod['func_1413'] = func_1413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1413_call = mutated_mod.get_global_var('func_1413')
call_1414 = func_1413_call()
output = call_1414
func_1415 = relay.Function([], output)
mutated_mod['func_1415'] = func_1415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_1416 = relay.TupleGetItem(func_391_call(), 0)
call_1417 = relay.TupleGetItem(func_392_call(), 0)
output = relay.Tuple([call_1416,])
output2 = relay.Tuple([call_1417,])
func_1422 = relay.Function([], output)
mod['func_1422'] = func_1422
mod = relay.transform.InferType()(mod)
output = func_1422()
func_1423 = relay.Function([], output)
mutated_mod['func_1423'] = func_1423
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1424 = relay.const([[[8.881027,7.290072,-4.681096,3.409757,2.577489,5.990291,-2.776215,2.723543,3.052512,-2.717401,-6.822692,-7.817245],[-6.436433,7.028025,1.898949,-7.396512,-6.932017,-1.716374,9.309459,-5.493614,-1.634733,1.210598,5.219159,9.489631],[8.736311,-0.873926,5.219697,-9.480174,-8.988546,-0.573421,-2.754722,-6.146542,1.716456,7.677799,0.954410,6.724980],[1.699066,-6.567038,6.171941,3.878039,0.524594,-4.495700,-6.892617,-1.133807,9.885358,-8.176012,6.535792,-5.629127],[1.966219,-9.834036,-6.224942,4.376690,-1.666723,-6.258095,1.779244,-0.465779,-6.496901,0.087289,3.336167,1.154378],[0.748546,-1.666387,-2.331485,7.515663,9.041996,-1.765545,9.819242,5.033840,-3.654839,9.155124,-1.413717,-0.822958],[-3.767310,1.172785,-6.530783,-5.857670,2.062858,-0.589433,-7.150942,2.767593,3.452385,7.242384,6.537521,1.710847],[-0.721281,-0.094693,-0.076635,0.557325,-5.676262,0.585234,0.779675,-5.604609,-7.121129,2.159682,-7.621702,-3.656160],[-6.665473,-8.611319,1.147075,6.928425,-4.930428,-2.195467,4.947980,-1.877439,-1.346714,-0.843105,2.887362,-4.339410],[4.471980,-0.642732,1.806283,-3.983491,-4.722758,9.639003,-5.317305,-9.659791,-0.442441,1.186786,-8.986620,-2.407089],[7.701735,0.340564,7.647297,3.279754,1.879699,0.209799,-7.767410,-5.759536,-9.210186,-8.798683,2.962065,-5.416363],[1.187123,4.946327,9.557041,5.749259,-5.786766,5.302601,-4.359759,-5.864185,7.936691,-5.255918,9.670658,-6.485134],[4.623840,-8.844619,4.019833,-9.656303,0.947108,4.827837,9.429458,5.960271,5.754797,-2.067093,6.511119,9.504124],[-0.954819,6.807250,-2.996856,5.226610,-9.933693,-6.417682,-2.701127,0.315400,-8.824936,-0.265699,6.127307,5.200486],[6.532999,-5.153389,2.017491,8.408906,-6.141445,1.267076,-9.718462,-0.840376,1.241753,0.844308,8.126346,5.140833],[5.815736,-5.733494,1.389544,2.652168,4.413072,-6.990418,7.616656,-0.604645,-0.331559,-5.656535,-9.240054,2.116174]],[[-0.126047,-9.717325,3.692526,1.386045,3.036893,2.817703,-2.721564,3.692616,2.725009,-5.907491,3.705353,-8.264318],[-6.838107,9.577003,2.052554,-0.909560,9.599222,8.884679,-9.808366,5.043173,-8.307128,9.814810,1.762038,-0.136978],[-5.935942,0.458797,0.518050,2.417555,-9.359656,9.705992,4.810605,0.717843,-8.041414,-7.992240,-7.401653,-6.832777],[-6.056397,8.300971,1.160206,-7.106171,-9.058792,9.663112,0.572336,6.194414,0.555581,5.625319,9.963037,6.020198],[-7.952862,-7.090210,2.836652,3.116961,-2.965846,3.692140,7.488354,4.492615,2.610934,5.664969,0.394938,7.425510],[0.635435,-7.192513,5.338641,-5.441150,1.237390,-5.461886,-7.608867,-4.130010,-2.878424,-4.078540,-7.653904,0.701779],[-5.655709,-6.523269,-3.014518,0.267583,0.928579,-6.554770,2.097364,-7.703401,3.803211,-8.955391,-4.899642,2.841011],[-1.018760,-4.154393,5.264903,9.497432,7.247849,-7.856191,4.318083,6.161174,0.376720,5.470767,9.761212,7.396567],[6.570974,-8.724950,-5.740579,-0.581283,3.998847,3.192192,5.164539,-8.787908,0.720835,-8.340140,-6.762889,7.838758],[3.106283,5.318261,-1.342956,3.303433,-4.526311,3.997701,5.039853,6.984008,4.536588,-3.255208,8.919166,3.339772],[3.310960,6.623017,1.797550,2.858825,-3.625358,9.777365,9.258179,-0.720848,-5.248867,-6.922582,1.586460,-4.256448],[5.996508,4.374595,-3.385065,6.274638,-3.876779,3.682693,6.117203,-4.057952,4.056825,-7.595387,0.735101,-4.888727],[-7.686825,9.418309,0.399295,-9.717418,-7.325239,6.281669,-1.349377,-1.992332,-1.483669,5.172986,-2.481513,7.668243],[3.907860,-0.647154,-6.439624,7.017632,-1.817683,-1.765501,-0.124257,-2.407048,8.673031,8.746114,-7.478044,-6.866700],[-0.206396,-5.919610,-9.683264,-4.393430,8.102416,-9.211020,-7.747302,-1.218326,-3.089549,-4.104254,-0.585515,-5.334750],[-9.670333,0.530886,1.147375,6.569052,8.972818,3.159763,8.982951,-8.014460,-7.815500,-0.249823,-4.352781,7.738404]],[[-5.679408,2.185073,-0.907105,-9.717360,-6.941737,4.764327,0.717947,6.811848,-1.263209,-5.222905,-9.237228,-9.448955],[7.504497,0.933014,-9.638601,9.568773,-6.300089,4.049381,-7.826466,-1.710329,6.415535,-6.890750,-9.002214,-2.032973],[-7.511551,0.812649,9.765879,-5.807986,-5.679038,-7.842126,-6.210708,5.091315,-7.364209,-6.491056,-3.268636,4.265076],[-1.439681,9.724435,9.870700,-9.199422,-1.962266,7.171400,7.175565,3.067673,2.161484,-2.863281,4.285982,4.930481],[-9.495174,-0.931628,-3.563683,9.336793,5.588453,4.372269,-6.520173,1.333550,2.436476,-0.547910,-7.704677,0.007904],[7.797283,3.047480,1.377896,-8.720956,-1.238199,5.911785,8.694077,-7.562029,3.628505,4.996101,0.837536,-6.930916],[6.947609,6.596231,-9.026391,-9.416698,4.872920,-3.197092,-4.891928,-0.957625,6.710798,2.094201,-0.988761,-3.605601],[6.405383,3.516607,-8.551847,-2.210048,-0.098413,5.748151,-4.813564,-2.181601,0.211085,-1.328717,-9.480761,5.948282],[-2.489400,-5.461324,-8.209140,-9.356969,-9.166070,-1.698261,-4.421315,6.708962,-7.999454,9.593513,-6.049444,-1.700004],[7.545963,7.388849,-4.961818,1.704281,2.527171,1.060993,-8.032291,0.035650,-3.392986,9.512296,-3.434312,8.810469],[8.856922,7.367488,2.851573,-8.111495,7.730188,-0.320685,-7.390772,-1.733481,6.097026,2.046616,-4.522905,-9.612418],[-4.838113,1.964554,-6.831274,8.813865,2.761413,2.525087,3.056925,7.459543,0.188229,-2.698565,-1.393441,3.816141],[-7.550920,4.493205,-3.176951,3.111219,-7.366975,0.780848,-0.335690,-9.087359,-1.242060,-7.176547,5.105763,-1.426414],[4.378779,-4.381484,6.848789,6.293038,-5.950994,-8.085931,-1.694256,6.552859,-1.057000,-2.875737,-6.025936,1.379412],[-5.707994,-6.455028,9.184116,9.446062,5.658623,-4.840938,5.574887,-9.945284,9.845750,-6.904750,3.111570,-5.383131],[4.329343,-3.000107,0.578844,-4.107861,1.397044,-3.814841,5.803416,8.639562,9.958358,7.011856,2.244191,0.024184]],[[8.376887,-6.141686,0.120200,-8.559680,3.870158,-5.753149,-8.985828,9.537218,5.890920,1.293555,9.948506,8.927204],[-9.947168,0.291844,2.654843,-3.126938,3.462595,6.993060,9.249048,6.267582,-8.465166,-9.384389,-4.700539,-3.857525],[8.144075,-1.363854,-0.028195,6.640980,-2.001907,-5.645373,4.121138,-4.817535,8.499108,-5.521177,-8.942274,-9.087401],[8.656932,0.382732,-9.899185,-9.405321,8.660861,-2.862470,-2.412824,4.030333,-2.515639,-2.649795,-8.502961,-4.886994],[-2.191017,0.589437,-5.523387,3.393683,-2.542893,7.489716,-4.445598,-7.062948,-4.100231,9.249292,-3.029998,-0.836326],[-2.698086,1.747809,5.685234,8.435505,-1.787365,-3.807170,-3.749409,-0.936924,0.379751,0.519509,3.336994,3.640175],[-2.793140,6.105810,0.672948,7.678041,-5.645726,2.942184,7.675506,-8.279341,6.427266,-1.833913,-9.064961,-8.304846],[0.158635,-7.447567,4.102351,-5.559033,-4.651941,-1.900298,6.779939,-9.174156,-4.439856,-1.357477,-4.669468,4.576133],[5.250720,3.516277,3.387813,0.805861,4.144588,7.334182,-6.653251,-0.308372,6.104056,-7.514818,-7.083359,3.435000],[-0.083310,-5.973634,-9.176681,-4.752357,-2.073082,1.237281,1.380760,-9.067549,-7.425598,2.637954,2.703895,-8.951150],[3.514515,-1.210523,7.283960,-8.322836,2.864266,-0.614959,0.683820,5.700509,-9.100430,0.881652,-5.622779,-7.272209],[9.827764,3.348767,8.793136,-4.200887,-3.601560,-3.142478,-1.355066,-7.187347,-1.844262,5.341428,4.961139,6.758851],[5.882473,-5.117658,-6.040053,8.900531,-5.983656,-0.574106,-3.661466,-8.898667,4.898995,-5.659736,-7.353667,9.941060],[9.797204,-6.139714,-5.175711,-7.757119,-5.307749,6.217466,6.438901,-9.696535,9.575261,8.398150,1.611406,-8.930626],[-8.550208,-9.374046,8.416311,0.136577,-9.668278,-0.840624,9.429044,4.205773,6.175068,-3.846228,6.957898,-1.410866],[-9.785361,-6.786867,-1.661226,-7.418220,2.998578,8.603995,7.926228,6.901022,-8.325394,-2.010447,-4.755998,0.617489]],[[-7.017270,-8.307578,-3.595413,-2.746478,-0.237407,6.197335,0.781457,5.944881,-8.364830,-2.505457,-3.273617,-0.420120],[1.029004,-5.637476,-2.389750,0.941279,-8.456951,-4.296808,-4.988097,2.020332,7.225517,3.514957,-3.971650,4.770444],[6.987192,-0.608687,2.463540,-5.045294,2.340119,-8.202681,-6.216881,-8.362062,4.138153,-1.582935,3.445392,-8.007942],[-0.291395,-5.401662,-0.831550,2.909849,7.935242,4.238285,-3.511587,9.843047,3.565254,3.200306,1.584680,-2.310953],[-9.113697,-4.411573,-5.636772,-6.781662,2.017678,3.678189,-4.690978,5.703449,2.426371,-2.045826,8.609768,3.149788],[4.734945,-7.826214,9.389870,0.637474,7.046726,4.364203,-0.161874,-3.240988,-6.737921,-4.250451,9.825255,-5.806013],[-8.644126,-0.223219,-1.488028,-9.254036,2.557145,-3.796281,6.426602,-1.315233,-4.556012,-5.199102,-1.034261,-7.212846],[2.411943,6.809383,-1.436587,1.786241,8.947985,-0.499759,4.666785,2.542850,-7.807143,5.107510,-9.416367,-3.063711],[-4.387491,6.416590,-9.469363,6.563890,-3.314230,-9.090642,4.222437,-9.844692,8.749572,-3.429588,0.094957,7.920710],[-9.082641,-4.769584,8.872676,1.128698,8.640605,-4.033690,-9.528232,0.460841,-3.639303,3.361654,6.056454,-6.875583],[4.305907,-1.981792,1.266586,-1.775671,-0.293318,-7.730328,4.813296,4.672578,-8.563646,-4.709146,-9.694758,-0.183968],[2.234533,-2.369619,1.591624,-2.229937,0.267595,3.204858,-4.922521,-8.454498,-5.690603,-8.814055,-7.276292,7.116311],[1.169488,3.857812,4.018905,9.807840,-0.974218,-9.817459,-1.515864,-1.151505,7.480964,-9.687202,2.468369,-8.896298],[6.091241,7.102273,3.387110,9.041646,9.104219,-8.285697,-9.418145,9.831071,4.855488,-5.548533,-5.042042,7.494260],[-7.498398,-2.116186,1.865540,-2.740462,4.001636,-0.813525,-1.238637,-4.881784,9.893398,-4.972308,-5.597128,-3.934241],[9.657971,6.711451,6.195748,9.558758,9.359896,7.385703,0.504683,0.611644,1.192382,1.670217,9.198051,4.632003]],[[-0.097860,-6.602183,-2.006206,-5.857072,0.764267,8.460495,-4.674044,3.287935,-4.838752,-0.077037,-5.036422,5.947754],[-3.117924,9.442079,-0.200036,-0.641860,-7.260091,9.815608,4.112722,7.059228,1.441572,0.747668,6.566419,2.390225],[8.262718,1.735042,-6.765864,9.201914,1.477761,-9.391268,-8.800069,-5.874127,-3.618338,5.129911,0.841534,-4.396277],[1.299173,2.363092,-4.093973,4.899194,-8.595347,1.486667,4.601447,0.786586,7.750576,-4.751812,-4.137451,5.293768],[-7.331629,-7.996070,5.041378,-2.915493,-0.136450,1.076675,4.348735,-7.429618,-0.822842,-1.699167,6.374151,-1.181104],[1.724014,-1.178016,-6.252685,-2.953020,-7.528737,-6.019722,-7.177370,-4.290001,-2.595747,8.071516,-3.777087,-3.762040],[-4.878812,-0.720594,-5.424659,-0.772122,2.086813,-4.612754,-2.931024,-1.514466,4.762427,-3.098172,-5.287523,6.455492],[2.880792,-4.264589,-7.747357,-1.549340,8.992380,-1.989837,7.584719,7.478926,1.563663,-0.694870,6.216474,-4.059794],[-5.822079,-3.133070,-3.612125,5.315618,-6.351526,7.284011,-8.316322,2.466861,9.709827,-3.417869,1.022515,3.178553],[1.887193,-6.636501,4.788658,9.064001,-2.484296,-8.219780,3.904769,-7.694560,4.371795,5.966293,3.448463,6.153406],[-3.602333,6.279560,1.589126,9.326644,1.431393,4.012501,-3.522302,-3.577614,-0.497640,4.351836,-0.602366,-8.844634],[-1.393213,-0.091197,-7.933791,-8.481519,0.146566,-7.804500,-3.295191,3.791089,-4.227224,-3.320642,7.755073,7.957786],[7.855022,-7.696265,-0.913519,5.196492,-1.702507,-4.035104,7.900343,6.048166,-0.055176,-0.107435,8.286749,-6.133139],[-4.162178,2.726501,9.010699,-0.645798,2.968711,9.656251,3.761088,-1.696466,-4.947031,-2.301452,2.282209,-9.302535],[-2.262315,8.428623,-6.173501,6.499455,-1.316117,-9.679226,9.601033,7.213342,5.349475,-7.323568,0.165461,-2.656746],[5.111291,-0.600388,8.640288,-6.087237,9.981504,4.029411,-1.690560,-7.794797,5.465102,-9.780442,7.620241,-4.086439]],[[-7.189414,8.498512,4.206283,3.433914,7.484731,-9.838617,-0.723432,-4.905073,-3.048049,5.165193,-9.804756,4.736054],[2.805106,-5.392795,4.903931,7.869184,4.535921,-4.413744,7.429059,4.039209,2.567562,7.884962,-7.488201,8.046989],[2.812167,6.006017,-7.676253,-8.762845,5.635970,3.692653,4.746514,-1.682018,3.190688,8.754457,2.569112,4.335707],[-1.970644,-3.227272,-2.833918,5.642090,7.693064,5.370892,-9.677618,9.836746,-4.735877,-9.700434,9.812517,-6.800988],[9.601435,5.542189,-2.707656,5.249824,4.542769,-9.166871,2.278881,-4.896124,-6.282021,3.460999,7.189795,-5.634472],[3.565374,3.344326,-9.334316,4.682622,8.177584,-2.712564,-0.169660,2.860704,6.854468,3.059294,9.122116,7.656077],[-9.532100,-8.810569,5.245211,6.500793,-9.080489,-1.719432,8.551714,-6.037878,-7.314869,-1.851836,7.058749,8.115053],[7.213935,8.897629,-1.119811,4.234091,9.721589,-6.803716,-1.110679,8.650609,-7.195396,9.955939,-3.125146,-1.009282],[-9.919299,3.608559,-9.341063,5.690020,0.921695,9.529317,9.229868,-6.861593,-4.786897,-4.249112,1.702028,8.139892],[4.229799,9.307405,1.151102,-7.639648,-1.582664,8.548277,-5.785846,0.575799,2.099933,3.261950,2.819034,-2.042496],[-9.491438,-5.303504,-4.818688,8.148450,5.889388,0.632174,1.510045,-9.542030,4.229477,-3.376148,-2.976228,-8.340980],[-1.592167,2.721915,1.454587,-6.275187,-6.418614,6.304737,-2.718341,-1.803817,2.074100,-1.358364,3.288278,2.224122],[-8.418692,8.257374,1.408290,0.275319,6.222545,6.185096,-5.474659,0.230088,-5.747959,6.561674,2.435259,-8.684014],[-4.809972,8.466539,-5.911769,-7.672733,5.719074,9.768744,7.675413,-8.617994,6.333518,-5.265404,5.190241,-1.132853],[-1.277168,0.029853,4.450568,5.845350,-8.504737,-2.131972,0.958657,-4.909034,-5.416544,7.012590,-9.886375,-6.973405],[1.112218,2.663296,-1.816295,-7.774762,5.005998,1.531718,-4.346900,-9.294511,5.751350,4.614760,-3.929332,1.902701]],[[7.831127,-0.813966,1.949779,-5.516625,5.176115,9.563752,9.597917,9.745755,5.696022,-9.698893,9.174244,7.404850],[8.724661,0.995067,-6.059118,-0.714811,9.033587,1.100625,6.660393,9.232310,6.621403,1.481359,-1.187827,3.003210],[9.373454,7.251621,3.131899,8.207055,6.871290,-5.410894,-9.447673,-7.367454,1.224741,-7.313335,2.335167,-0.311960],[-7.066263,9.711288,-2.683634,8.536538,-8.483567,-3.866604,0.784430,-7.605741,-7.923790,-8.631420,8.190509,-7.146134],[-4.182369,-2.845960,-4.021400,-2.833995,-8.101446,9.548532,-5.048903,-7.123228,-8.154026,-0.670531,-7.745800,-7.386301],[3.993290,7.899908,2.446495,-7.504478,-7.498281,9.625627,8.394491,-0.619624,-6.363022,-7.479006,-0.588047,3.500752],[1.578126,-4.727405,3.297314,-2.616921,9.456083,4.776405,0.675024,-6.882038,-4.406749,-8.330633,8.142261,2.634014],[-3.032095,-7.936996,-5.099408,6.251473,-8.928153,-6.429887,0.443007,-0.571080,-9.239135,1.695273,9.310461,-3.772483],[-3.681891,0.949381,3.636213,7.021886,-2.777111,-2.084742,9.592610,-7.437265,8.968813,0.944410,5.584389,7.748634],[-8.033536,1.048861,-0.648390,0.389769,-7.249434,-8.141422,-7.929590,-6.892098,5.431973,4.609481,-4.523398,-6.565696],[-9.120355,-8.503392,-1.016017,-0.814414,4.546732,-3.035559,4.463905,-4.751949,2.037701,7.535273,-6.449291,-9.229431],[-0.926726,-7.200915,-9.902569,-0.722509,9.182609,-1.885841,-4.702820,-9.131965,5.064966,2.945208,-6.136364,-1.718860],[-2.034406,6.441764,6.303375,-8.382803,-4.758216,3.215428,-6.674917,3.272358,-6.348652,6.936165,-9.394587,-5.146839],[-0.552803,-6.668737,6.294326,-1.291847,-5.074536,-7.482811,-9.852830,9.207378,-4.074525,1.056168,-7.022208,-4.474687],[-9.637593,2.049588,6.085401,-6.802739,1.813597,-8.182827,-6.101679,-6.556416,0.562545,-8.289797,-4.648617,-6.721328],[-4.249856,3.413510,-1.287596,-3.781693,7.686238,-1.087388,1.109908,-1.633613,3.010935,-4.817479,-2.235808,1.458531]],[[1.422083,2.305694,4.559615,-8.444948,1.086857,5.081373,5.071469,-4.734096,8.217766,2.966178,-3.119425,-8.182132],[9.300650,1.618157,6.679413,5.850754,-8.750875,-6.649830,-6.161654,-5.190938,-6.262381,0.632774,6.104018,-6.215771],[-7.186290,5.617363,-8.260481,4.738935,-1.598018,8.760227,5.179836,6.749966,1.397620,6.529393,-5.942821,6.643117],[9.944417,2.810132,-4.126616,-8.228757,4.381300,3.411105,6.653582,0.144675,2.013522,5.584631,3.877861,0.478129],[5.523384,-9.216423,-8.414908,-6.679617,0.317116,-4.189876,-7.072907,-9.740885,-0.232601,4.080268,-4.264859,-0.867677],[5.301594,-6.559270,-5.602001,6.270623,5.332090,9.845752,3.439103,3.924499,8.232476,-4.574119,-5.043280,-4.403597],[0.928854,-6.426156,-6.050838,5.531895,4.399770,1.907227,7.906479,9.380530,-0.898185,-4.156967,-7.399624,-4.456971],[1.749919,5.381473,-6.016871,3.178178,9.450277,6.146239,-6.977398,4.266084,0.175420,7.976129,6.948188,8.732324],[3.145929,5.392479,7.436151,-6.360543,8.229465,6.528879,7.935348,9.380193,-2.098766,-6.362609,9.567064,-5.169588],[-5.152081,-2.100489,-9.110960,-9.488991,2.136746,-7.092764,5.079327,-5.310998,-1.607938,-5.778852,-3.835924,2.433321],[5.844311,1.137114,3.653467,9.422065,1.597257,-3.848055,8.522653,4.405074,-9.350435,2.342817,-1.233726,-2.547992],[9.413256,-8.474250,-0.314288,2.854224,-6.537587,8.995044,-9.679408,8.873289,-9.800585,-1.809307,-0.937466,-1.521176],[4.796766,9.405442,0.486899,-2.707165,-8.114999,-3.634759,-3.834864,-0.419959,-9.814072,2.629646,-2.625601,-1.828718],[-2.792329,-1.770180,8.233787,1.982262,5.895487,-8.133300,6.259277,0.969940,-1.832476,-4.993436,1.647973,7.030100],[-7.915961,6.534932,3.678488,4.973747,-6.854620,8.710075,9.188198,-9.247945,3.556044,4.737550,0.714163,-5.994210],[5.381349,7.403891,-6.120408,-7.889286,9.956219,6.609816,-9.827995,-9.123867,3.960141,-2.435578,-4.222819,5.959028]],[[3.613740,-2.809923,6.401784,-9.506544,-9.627884,-0.199168,-8.106776,0.841316,-2.460162,6.442342,-3.108881,3.764881],[3.139980,-0.887812,-9.417582,7.739418,-4.752844,-1.507432,-7.265875,-6.054364,-1.102413,9.656585,-1.485053,-6.929727],[-4.827367,1.428399,8.543717,-1.093799,-4.554050,5.129032,-2.694643,-9.964921,-7.991664,-3.232452,-7.429909,4.826254],[8.621414,2.295128,-3.370826,-3.037195,9.310665,5.419947,-5.614833,6.324561,-3.663240,1.023538,6.724659,5.260932],[4.558182,2.509664,0.325366,-7.515180,7.745791,-9.022337,-4.273913,-4.190746,-1.577245,-7.597674,4.351445,7.029146],[-8.761542,-5.606790,-8.138903,-5.828539,-2.359511,8.377708,-7.817933,-8.738070,-6.476734,5.026533,-0.137557,-2.095364],[9.279145,4.562171,9.336250,-2.691478,-7.829658,0.703326,2.130069,-9.883825,2.268724,9.000530,6.665423,-7.301223],[-7.957020,-4.516030,1.792214,8.964330,-1.800502,-5.474217,2.596534,8.225921,8.702873,-3.630599,-3.954877,-0.120052],[8.822184,-0.059938,-1.966384,-4.514420,-1.603790,6.926248,8.079879,8.980120,6.598117,1.349137,-1.145810,-4.557603],[-4.844701,-2.401509,7.366886,-1.641133,-1.653664,-1.799987,2.302483,4.293658,4.073982,-7.313843,5.560119,-8.002136],[5.760861,2.526629,3.342561,4.576412,8.777092,-2.452868,8.856852,2.717321,3.770146,-7.187035,-4.814608,2.290519],[-7.528598,-3.079115,8.033898,-5.709409,6.048838,-9.779054,-5.642763,-0.576453,-1.072369,-4.412038,8.764843,1.324622],[9.883732,-1.614680,-6.948799,-2.288920,1.563848,-1.680957,4.937600,0.022306,4.769397,8.371883,5.663699,6.933950],[6.025891,5.746396,1.896149,1.313822,-3.217781,-7.873677,2.243008,1.783787,2.465964,3.479423,4.396139,1.573723],[9.955928,-1.560820,-3.737966,-2.949316,9.139912,1.024159,-9.896184,-1.314098,-7.188707,1.249992,8.438765,-0.272752],[8.552979,8.461776,-7.449525,8.453761,-6.113621,-1.814172,5.060958,-6.110978,1.292616,9.770524,-4.662204,-0.580358]],[[-3.377038,5.185827,0.543534,-2.231531,7.021835,7.865752,2.564924,8.960945,-4.107371,-8.104151,-6.877833,-6.190363],[-7.561931,-2.828261,7.501067,5.092297,-9.249818,1.302438,-8.494362,-0.020200,-2.901239,6.424680,-7.560117,0.682475],[2.229432,-1.513417,-0.371247,4.775895,-6.726789,7.175706,-7.301714,9.822216,1.777507,-5.296772,2.636921,-3.918012],[-8.725192,2.652947,-5.065330,6.778527,-8.182742,-5.720394,8.081927,-9.214871,0.016039,8.263881,-7.725247,-6.085058],[-3.655761,-5.603223,-9.395606,1.685049,-5.391735,2.129689,5.076083,-1.657596,8.727099,-2.863190,-4.647462,-0.899763],[-2.645502,-3.314889,2.475665,9.440651,0.146002,0.991960,-1.689292,3.202205,0.201401,0.398560,1.477743,-4.498612],[-9.662005,1.406453,7.145559,-2.785056,-6.521416,2.167337,-6.315886,3.050247,-0.173518,9.663409,3.551245,5.492410],[7.729463,8.168177,7.377301,4.228266,-4.369335,-2.388472,4.079810,7.385889,8.195373,1.134861,8.085050,-7.663182],[0.091177,-2.367798,-2.381959,8.323347,2.474677,-7.826554,-7.749233,-5.224744,3.957495,5.847924,-4.321276,-8.116456],[0.046642,8.533816,-2.317587,-6.466326,1.971890,-4.106201,-9.797730,7.783311,-4.977130,-3.065559,-7.542748,0.125561],[-6.934615,-8.457636,7.866555,-3.796133,-2.619224,-6.471143,4.877706,-7.318726,5.808558,-0.451550,-3.726328,0.537124],[-9.112262,0.681221,1.738038,-2.353971,6.860772,-7.223374,4.874339,2.129337,-4.514033,-8.129466,-8.320626,-4.579994],[7.474365,-1.470018,-3.334850,-8.646699,1.354962,8.061599,-7.757285,-7.914270,-5.814823,-7.490691,-9.695696,3.149162],[1.251377,-1.489006,-2.574604,-8.549374,-8.461092,1.215879,-2.327070,7.446582,-4.563610,-8.425560,-2.928552,-4.599853],[7.080148,-5.434151,6.843844,-2.793637,3.292212,-3.150494,2.738993,3.091416,4.520551,5.430617,-7.590786,-9.723651],[0.745816,3.071157,3.535217,2.454296,-4.614074,-7.556438,8.193905,5.419326,-9.873447,0.516005,-9.532011,0.325329]],[[3.570285,8.135873,2.312225,-8.976750,2.571619,-1.571423,-3.314840,3.933499,0.548253,-5.018160,4.927832,1.545787],[3.457090,3.665282,9.523105,-5.274247,8.830568,-3.652154,4.832474,-0.164510,-6.499445,3.866801,-1.707234,2.118529],[8.256019,-5.069987,0.187097,-7.933831,-1.861585,-5.356770,-8.021068,6.195646,7.462431,-1.887991,-1.023458,3.900317],[3.621415,6.044352,2.634114,5.776383,-9.224787,2.886716,0.356999,5.983977,-4.463550,4.270759,-2.639896,-2.308707],[-6.618372,-5.478574,0.029919,2.815956,-1.350362,-3.258393,6.290822,-2.107376,-9.160365,-0.290638,7.674942,8.822636],[7.420011,-4.331823,4.552759,8.955413,9.253892,7.346446,6.047442,2.454277,1.078001,-0.689350,1.229367,0.675978],[-0.189503,5.744505,3.073066,9.500163,8.074083,-0.756295,5.764849,-3.234056,0.159261,9.044210,-1.365083,-3.466643],[8.629011,4.928993,-3.935239,-7.802712,-4.401761,-7.121914,-7.586334,-9.409243,-0.815560,5.307434,3.575594,-8.553887],[0.695097,8.655997,7.635478,9.395932,-7.809390,0.953817,3.656719,-5.591171,-6.415511,7.145686,-2.408383,-8.423909],[-7.964759,-6.718087,-0.662519,-0.940157,3.678118,2.489041,-4.854773,0.904133,1.071144,3.216255,-9.474735,-1.022711],[-9.077460,3.370330,-7.214645,8.144527,7.843816,-1.765466,4.049139,0.739212,-1.568105,0.026275,-8.908019,-1.067053],[3.473078,-1.786613,0.213930,-6.036148,4.995054,-7.520760,-1.149412,-9.749495,-6.509468,0.184087,-0.505266,-3.811603],[8.580900,3.024526,-5.412715,-3.854814,9.434339,6.540267,5.246300,-5.437520,8.706236,-1.152160,6.186706,-3.378577],[2.508554,6.083620,-1.872307,7.080034,5.332821,1.990849,-3.766572,6.459410,4.899440,-3.197047,7.474622,8.447885],[1.568065,-5.292760,-9.402892,-1.535619,-2.413259,0.231641,6.979810,-4.794693,5.620683,-4.230363,7.341256,2.133956],[-5.356637,-5.055694,2.489225,4.312155,8.097114,9.112462,-1.094829,-9.672325,2.239698,8.415016,-5.786856,0.716952]]], dtype = "float32")#candidate|1424|(12, 16, 12)|const|float32
uop_1425 = relay.rsqrt(const_1424.astype('float32')) # shape=(12, 16, 12)
var_1439 = relay.var("var_1439", dtype = "float32", shape = (12, 16, 12))#candidate|1439|(12, 16, 12)|var|float32
bop_1440 = relay.power(const_1424.astype('float32'), relay.reshape(var_1439.astype('float32'), relay.shape_of(const_1424))) # shape=(12, 16, 12)
output = relay.Tuple([uop_1425,bop_1440,])
output2 = relay.Tuple([uop_1425,bop_1440,])
func_1451 = relay.Function([var_1439,], output)
mod['func_1451'] = func_1451
mod = relay.transform.InferType()(mod)
mutated_mod['func_1451'] = func_1451
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1452 = relay.var("var_1452", dtype = "float32", shape = (12, 16, 12))#candidate|1452|(12, 16, 12)|var|float32
func_1451_call = mutated_mod.get_global_var('func_1451')
call_1453 = func_1451_call(var_1452)
output = call_1453
func_1454 = relay.Function([var_1452], output)
mutated_mod['func_1454'] = func_1454
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1458 = relay.const([[[False,False,True,True,False,False,True,True,True,False,True,True,False,False,True],[False,False,False,False,False,True,False,False,True,True,False,True,True,False,True],[True,False,True,False,True,True,False,False,False,False,True,True,True,True,True],[True,True,False,True,True,False,False,True,True,False,True,True,True,False,True],[False,False,True,False,False,False,True,True,False,False,True,True,True,False,True],[True,True,False,True,True,False,True,True,True,False,True,False,True,False,True],[False,True,True,True,True,True,True,False,False,False,False,True,True,False,False],[False,True,True,True,False,False,True,True,False,False,False,True,True,True,False],[False,False,True,True,True,False,False,True,False,True,True,True,False,False,True],[False,True,False,False,False,False,False,True,True,False,True,True,False,False,True],[False,False,True,True,True,False,True,False,True,True,True,False,False,True,True]]], dtype = "bool")#candidate|1458|(1, 11, 15)|const|bool
var_1459 = relay.var("var_1459", dtype = "bool", shape = (2, 11, 15))#candidate|1459|(2, 11, 15)|var|bool
bop_1460 = relay.logical_and(const_1458.astype('bool'), var_1459.astype('bool')) # shape=(2, 11, 15)
uop_1471 = relay.acos(bop_1460.astype('float64')) # shape=(2, 11, 15)
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
var_1474 = relay.var("var_1474", dtype = "float32", shape = (980,))#candidate|1474|(980,)|var|float32
call_1473 = relay.TupleGetItem(func_463_call(relay.reshape(var_1474.astype('float32'), [14, 10, 7])), 0)
call_1475 = relay.TupleGetItem(func_466_call(relay.reshape(var_1474.astype('float32'), [14, 10, 7])), 0)
output = relay.Tuple([uop_1471,call_1473,var_1474,])
output2 = relay.Tuple([uop_1471,call_1475,var_1474,])
func_1483 = relay.Function([var_1459,var_1474,], output)
mod['func_1483'] = func_1483
mod = relay.transform.InferType()(mod)
mutated_mod['func_1483'] = func_1483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mutated_mod.get_global_var('func_1483')
var_1485 = relay.var("var_1485", dtype = "bool", shape = (2, 11, 15))#candidate|1485|(2, 11, 15)|var|bool
var_1486 = relay.var("var_1486", dtype = "float32", shape = (980,))#candidate|1486|(980,)|var|float32
call_1484 = func_1483_call(var_1485,var_1486,)
output = call_1484
func_1487 = relay.Function([var_1485,var_1486,], output)
mutated_mod['func_1487'] = func_1487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_1492 = relay.TupleGetItem(func_376_call(), 0)
call_1493 = relay.TupleGetItem(func_377_call(), 0)
func_1200_call = mod.get_global_var('func_1200')
func_1201_call = mutated_mod.get_global_var('func_1201')
call_1506 = relay.TupleGetItem(func_1200_call(), 0)
call_1507 = relay.TupleGetItem(func_1201_call(), 0)
output = relay.Tuple([call_1492,call_1506,])
output2 = relay.Tuple([call_1493,call_1507,])
func_1520 = relay.Function([], output)
mod['func_1520'] = func_1520
mod = relay.transform.InferType()(mod)
mutated_mod['func_1520'] = func_1520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1520_call = mutated_mod.get_global_var('func_1520')
call_1521 = func_1520_call()
output = call_1521
func_1522 = relay.Function([], output)
mutated_mod['func_1522'] = func_1522
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1557 = relay.var("var_1557", dtype = "uint16", shape = (16, 6, 11))#candidate|1557|(16, 6, 11)|var|uint16
var_1558 = relay.var("var_1558", dtype = "uint16", shape = (16, 6, 11))#candidate|1558|(16, 6, 11)|var|uint16
bop_1559 = relay.right_shift(var_1557.astype('uint16'), relay.reshape(var_1558.astype('uint16'), relay.shape_of(var_1557))) # shape=(16, 6, 11)
output = bop_1559
output2 = bop_1559
func_1571 = relay.Function([var_1557,var_1558,], output)
mod['func_1571'] = func_1571
mod = relay.transform.InferType()(mod)
mutated_mod['func_1571'] = func_1571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mutated_mod.get_global_var('func_1571')
var_1573 = relay.var("var_1573", dtype = "uint16", shape = (16, 6, 11))#candidate|1573|(16, 6, 11)|var|uint16
var_1574 = relay.var("var_1574", dtype = "uint16", shape = (16, 6, 11))#candidate|1574|(16, 6, 11)|var|uint16
call_1572 = func_1571_call(var_1573,var_1574,)
output = call_1572
func_1575 = relay.Function([var_1573,var_1574,], output)
mutated_mod['func_1575'] = func_1575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_1726 = relay.TupleGetItem(func_223_call(), 0)
call_1727 = relay.TupleGetItem(func_224_call(), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_1735 = relay.TupleGetItem(func_1112_call(), 0)
call_1736 = relay.TupleGetItem(func_1113_call(), 0)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
var_1739 = relay.var("var_1739", dtype = "float64", shape = (80,))#candidate|1739|(80,)|var|float64
call_1738 = relay.TupleGetItem(func_1319_call(relay.reshape(call_1735.astype('float64'), [14, 10, 7]), relay.reshape(var_1739.astype('float64'), [80, 1]), ), 2)
call_1740 = relay.TupleGetItem(func_1322_call(relay.reshape(call_1735.astype('float64'), [14, 10, 7]), relay.reshape(var_1739.astype('float64'), [80, 1]), ), 2)
func_1090_call = mod.get_global_var('func_1090')
func_1093_call = mutated_mod.get_global_var('func_1093')
var_1748 = relay.var("var_1748", dtype = "float64", shape = ())#candidate|1748|()|var|float64
call_1747 = func_1090_call(relay.reshape(var_1748.astype('float64'), []), relay.reshape(var_1739.astype('float64'), [1, 16, 5]), )
call_1749 = func_1090_call(relay.reshape(var_1748.astype('float64'), []), relay.reshape(var_1739.astype('float64'), [1, 16, 5]), )
bop_1751 = relay.floor_divide(var_1748.astype('float64'), call_1726.astype('float64')) # shape=(14, 10, 7)
bop_1754 = relay.floor_divide(var_1748.astype('float64'), call_1727.astype('float64')) # shape=(14, 10, 7)
output = relay.Tuple([call_1735,call_1738,var_1739,call_1747,bop_1751,])
output2 = relay.Tuple([call_1736,call_1740,var_1739,call_1749,bop_1754,])
func_1756 = relay.Function([var_1739,var_1748,], output)
mod['func_1756'] = func_1756
mod = relay.transform.InferType()(mod)
mutated_mod['func_1756'] = func_1756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1756_call = mutated_mod.get_global_var('func_1756')
var_1758 = relay.var("var_1758", dtype = "float64", shape = (80,))#candidate|1758|(80,)|var|float64
var_1759 = relay.var("var_1759", dtype = "float64", shape = ())#candidate|1759|()|var|float64
call_1757 = func_1756_call(var_1758,var_1759,)
output = call_1757
func_1760 = relay.Function([var_1758,var_1759,], output)
mutated_mod['func_1760'] = func_1760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1338_call = mod.get_global_var('func_1338')
func_1339_call = mutated_mod.get_global_var('func_1339')
call_1801 = relay.TupleGetItem(func_1338_call(), 0)
call_1802 = relay.TupleGetItem(func_1339_call(), 0)
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
call_1810 = relay.TupleGetItem(func_463_call(relay.reshape(call_1801.astype('float32'), [14, 10, 7])), 4)
call_1811 = relay.TupleGetItem(func_466_call(relay.reshape(call_1801.astype('float32'), [14, 10, 7])), 4)
output = relay.Tuple([call_1801,call_1810,])
output2 = relay.Tuple([call_1802,call_1811,])
func_1822 = relay.Function([], output)
mod['func_1822'] = func_1822
mod = relay.transform.InferType()(mod)
mutated_mod['func_1822'] = func_1822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1822_call = mutated_mod.get_global_var('func_1822')
call_1823 = func_1822_call()
output = call_1823
func_1824 = relay.Function([], output)
mutated_mod['func_1824'] = func_1824
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1842 = relay.const([[[6.679520,-9.236380,1.720378,-7.457737,-8.781809],[-7.210218,-6.258358,-9.667852,6.680832,0.211469]]], dtype = "float64")#candidate|1842|(1, 2, 5)|const|float64
uop_1843 = relay.erf(const_1842.astype('float64')) # shape=(1, 2, 5)
uop_1845 = relay.asinh(const_1842.astype('float32')) # shape=(1, 2, 5)
bop_1847 = relay.power(uop_1845.astype('float64'), relay.reshape(const_1842.astype('float64'), relay.shape_of(uop_1845))) # shape=(1, 2, 5)
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
const_1851 = relay.const([5.524285,0.963372,9.109967,8.068589,-7.429243,4.838002,0.511409,8.279425,-2.437730,-2.667789,-3.921805,4.008408,-1.387707,-8.586492,2.010981,-5.761734,-3.575705,0.652501,1.875415,7.185088,5.546724,-6.251240,0.306684,1.370443,-7.354027,-8.463052,-0.850010,6.844523,7.655064,-6.284485,7.106421,5.265914,4.446992,-2.220270,-0.319340,-4.497719,-6.573980,-2.340103,6.655666,-7.504407,8.537930,-1.793177,-9.939309,-6.614306,-9.720482,-2.537953,2.599900,2.797442,-6.323969,-6.165013,0.164462,6.860212,1.825114,1.723992,2.245469,-6.121135,-4.402657,-8.409038,-8.316693,-9.935667,0.815769,6.889355,5.057236,8.477375,-7.188539,-7.219615,5.258069,2.815972,1.481802,5.008541,-0.504606,2.784008,-2.437171,8.098200,-8.053299,1.723615,5.625719,1.695712,7.322041,-6.139528,-0.168564,-9.318984,-5.821099,-8.767617,-8.583924,-6.721884,7.218155,-1.361099,1.934748,2.754027,0.105984,-7.068156,7.561343,7.993072,-8.158898,-1.442269,-4.906621,-2.289652,-2.348742,-3.229021,-6.328855,-6.886857,-8.260010,-0.285969,-0.173678,-6.956219,-8.769532,-5.198830,-4.857297,3.527084,-8.003704,0.958725,-2.684881,2.218101,-0.249573,3.713567,3.644666,-7.057928,-9.451846,5.817596,-3.693869,1.746201,-4.343120,-1.535726,5.186939,-6.984766,7.959545,6.623084,3.382565,4.041235,-5.902139,2.910649,-7.443814,-0.632970,-3.911270,7.935703,9.668996,7.005187,3.201358,-0.990109,7.379663,-8.840068,-4.420865,-7.197537,-1.654911,9.727908,6.184201,-3.240151,-0.557563,-5.569793,9.414339,-4.480862,-1.299840,-5.228199,6.105944,7.210835,3.261647,-0.530968,5.114754,-1.414505,-7.563974,-6.963715,-6.572812,8.099072,5.260409,9.284315,1.368507,2.519943,8.313618,9.807070,-4.369916,-5.139882,-7.463704,2.551024,6.755317,-9.851477,2.853613,6.939067,2.148003,2.989619,9.982518,2.434268,-6.802721,-8.826042,4.633940,-6.713765,-9.305253,6.067254,1.135683,-1.649621,-2.359168,-2.821233,-4.567945,9.039956,-0.718164,-4.988824,7.891162,1.373360,8.670181,-5.205421,5.756921,-8.801589,7.341106,0.779508,5.271030,2.694331,-0.814634,2.664010,-8.852889,-8.632138,5.480013,-4.630715,9.469337,-2.921383,0.520707,8.477263,-8.678791,8.379203,8.041634,-4.886411,-7.228138,4.006721,-0.543665,5.155374,2.880397,5.058152,5.184457,-9.629563,7.051565,6.675408,0.322638,-1.351889,-4.725792,0.929242,-6.642858,-9.437817,6.471321,9.542187,1.758443,-6.403549,-4.678282,1.945559,3.097275,-6.952351,7.168494,-6.351482,-7.473591,-5.939717,-6.194905,8.179169,0.065353,1.008704,3.033635,-2.175648,-6.380222,2.632236,4.496437,-3.607980,-1.510529,7.515881,-3.453305,-2.394893,-4.785898,8.819357,-6.981809,8.435899,2.629479,3.426078,2.855124,4.483382,-7.159005,7.060719,7.857876,3.228469,-0.205016,9.456990,-4.218471,-2.767680,-1.453301,7.024975,-2.155797,1.366543,6.145164,-1.659333,-7.128247,-2.621020,-0.150598,-3.969102,5.527664,-4.455694,1.103653,-4.348384,5.496878,-1.036056,8.540157,7.159892,8.524568,9.288939,0.939647,3.128328,2.141788,-3.383601,1.060002,6.846843,-3.217537,6.935108,-4.332129,8.220032,-3.033937,8.037276,1.817858,5.076148,6.953097,-7.857142,-7.760028,4.699675,8.292714,2.347462,-6.642041,-3.309466,-7.539527,-4.017552,1.711357,5.246523,-4.709173,6.664973,9.960714,-0.366518,3.255893,1.373513,-3.292875,3.706703,-8.972553,0.675530,-7.699824,-1.942327,1.379274,0.800572,-4.081229,-7.732414,4.458802,0.536873,-5.978853,-2.878718,-4.451034,7.931650,-1.825779,-6.287741,9.432543,0.327375,6.598177,1.355237,2.783465,-7.150651,2.043386,-0.592451,-7.658613,3.854540,9.737121,3.889201,8.336158,-9.298842,9.076201,-3.670922,-2.349704,-9.071898,1.389376,-9.784477,-9.932075,0.254218,1.534357,4.316351,9.103139,-0.492717,-7.707304,-2.940622,-4.304936,5.893707,7.866447,7.275501,5.958038,-9.741650,0.236523,4.673875,5.426631,3.942506,-1.676396,-1.394386,9.995326,-8.716142,-9.216545,5.534757,-5.935046,5.767980,-2.135239,4.666680,-0.641818,6.892229,1.692113,-6.088497,2.326680,2.720167,-1.714053,5.584901,2.944432,5.515363,-4.356835,-6.575278,5.461308,-6.440765,-5.624427,4.374835,5.699665,-7.409030,-8.354799,5.984098,-5.404797,3.454926,5.468163,-9.995054,6.108561,-8.146753,-8.658033,-5.815600,-9.366008,-5.551141,-1.831727,-5.081014,-5.854769,-0.496805,6.098504,-6.902310,6.343521,-8.422939,-8.546646,4.739514,-6.394898,2.761670,-0.851608,-6.884762,-2.526570,-6.471636,-2.730373,7.246374,2.183143,5.595866,1.254849,6.384638,-4.025617,7.715523,-0.870194,-9.685666,7.979645,-1.463027,1.121947,-5.632861,1.833440,-8.137527,9.802299,-4.030816,-4.412313,2.683881,1.804078,-1.189887,-8.539962,-6.198255,-6.780523,1.874389,-4.547263,8.077297,-5.626951,6.305470,-3.666404,-6.906781,9.518200,7.682185,-6.286023,-1.424884,9.311568,2.096971,-2.998318,-8.468524,-2.756265,-1.290981,4.372828,-3.059535,-1.155068,1.430448,-6.453326,-7.761458,-0.250219,7.820523,9.846472,-6.407536,-7.320631,-8.676529,9.398572,6.765151,9.621541,-0.049748,4.311523,-5.067556,0.014637,9.746300,4.258755,9.194174,9.192886,6.717872,-8.060042,2.156481,6.540804,-6.529009,-6.296624,4.362396,5.393483,4.449321,-2.957367,-5.538862,8.410882,9.564936,-7.477608,3.669967,2.361636,-1.088864,-8.917458,-8.411359,6.855648,3.553822,-8.978404,4.833920,-6.569180,1.003742,1.308522,-7.759260,9.905298,9.729556,2.615350,2.446342,7.439137,-6.706269,6.561815,-0.860445,6.909260,-3.139952,-5.959531,-7.175095,-4.599623,2.254525,4.719577,3.540001,-6.201191,-7.643037,0.060885,-1.040444,9.382324,-3.168619,-0.964754,-3.271187,-5.677390,4.814413,-4.500298,-7.137907,1.003495,-7.438577,9.442186,9.794345,9.202421,1.687908,0.967662,8.133197,8.045028,8.518720,-2.901206,7.464182,8.061656,4.078159,-7.149098,-9.630365,-3.634802,2.060935,-5.652172,4.647523,-3.194598,-9.289744,-6.365360,5.634855,-1.803952,5.581391,-5.975924,9.998563,-1.592113,6.242448,-2.480841,-1.170294,1.623146,9.118590,2.311808,3.372320,8.575611,7.534527,1.026569,2.130518,-5.440183,0.936023,-4.895010,-9.591442,2.614555,3.600713,2.433429,-5.285409,6.412048,2.131077,-9.748880,5.719700,-2.884543,-9.298771,5.388823,8.718873,-8.139181,-6.955377,-0.430202,6.850364,-2.945550,3.083939,2.382479,-2.192583,7.503084,2.020059,-2.507547,-7.056457,1.178709,4.861005,-0.334690,-7.678237,5.899119,0.219022,8.263315,0.825328,-1.220438,-2.923519,3.589660,-0.299723,-9.392642,-2.038066,-5.820247,2.267644,7.564081,-8.212717,-6.342020,7.101828,8.492951,8.902465,0.167994,4.033289,6.359724,7.680309,-6.958825,-4.898813,6.831291,-9.140100,2.384467,-7.016434,-7.195729,-6.785413,9.929039,-2.430629,3.518821,-2.214796,-4.459695,-9.825380,2.794275,-8.352648,1.967412,-1.591348,-0.545902,7.035585,-0.785243,-4.808949,-9.575179,0.489015,-7.368289,4.914785,1.020739,9.089737,2.375624,-5.349684,3.608870,-9.881869,1.418018,-7.802819,8.094085,3.084862,8.315863,-6.399515,-1.257031,7.259229,9.564533,-8.425367,-2.357632,4.012791,5.428266,-5.315766,-7.871836,-4.686524,0.474729,1.278201,-8.499805,8.151587,8.684815,3.332195,7.737930,-8.823145,4.397780,-0.036523,-1.481716,7.768577,7.407009,6.305111,2.535782,4.357213,-7.976509,4.801323,8.561317,-7.491759,0.184688,-8.773824,-5.118920,0.606939,-2.410001,-0.021500,5.702540,-9.124352,6.656372,8.932817,3.713014,-3.333820,1.997507,-5.610341,-5.998053,0.365182,8.613220,-4.859728,0.500158,3.131639,0.459680,-0.438745,-5.092771,5.215974,-6.695264,-4.758988,3.540308,3.771996,-0.857904,3.220590,-6.175211,-6.333642,0.464535,-3.058704,0.544133,-2.703908,2.286921,9.003728,3.617792,0.633203,2.786673,-0.198146,-4.909974,-7.950859,2.607585,3.759932,-4.906507,9.023705,8.290190,-0.880947,-0.570107,3.614214,-1.167267,2.252272,-3.153271,4.646412,-5.435251,-4.779831,-6.522171,0.576215,9.262355,9.716283,9.092558,3.698718,-9.439024,2.464690,-0.511541,-5.883739,8.514272,-6.978768,9.724347,-2.465111,6.047970,-1.429003,5.529139,-1.757097,0.908266,-6.305671,-7.405357,1.665512,-3.872708,1.117150,7.260643,5.156976,3.031304,-6.408588,1.423127,-0.067400,-6.453737,-0.893121,7.416987,-9.234843,5.088026,7.146323,-0.052384,-0.201272,1.359853,8.318645,-1.921032,1.018804,-5.070970,-6.593248,-2.397894,2.889747,0.418224,-8.499819,-5.499270,7.274257,-5.013939,6.074276,6.624567,9.472717,-9.628033,-6.131906,7.464383,-4.816928,9.273998,4.883872,-8.050584,-8.009378,8.128580,-3.313863,7.142959,9.660034,-4.487950,-0.312262,-7.827423,-3.130808,-9.198741,2.128323,-0.053078,-7.968211,-6.869428,-5.760071,-1.377219,0.860766,1.813711,3.536267,0.143796,-1.717426,0.511401,-7.747633,-2.052154,-8.544557,4.957132,-4.823498,-5.552531,1.290081,0.597689,5.854379,7.813664,2.740476,-0.248887,9.849219,9.478970,9.851913,1.577916,-6.590495,-6.591333,-0.391824,3.335516,8.019805,1.761442,-3.460240,-9.224786,-2.346166,-3.480126,0.309668,-3.171339,5.598093,-4.830639,2.612048,-2.955498,-4.242980,-4.450452,-6.099429,3.071038,7.655696,-5.469890,4.800715,7.553096,-5.543867,6.476182,-8.578202,1.878319,8.161309,-8.303913,5.942816,4.369103,0.441035,-6.339167,7.940851,-7.488682,7.236578,-5.641721,1.165354,-6.009726,-4.790434,0.167371,-2.067291,-2.750372,4.077126,-8.079735,8.519252,-2.507562,9.390188,-2.987658,-0.009355,-0.143499,0.071351,0.830461,-6.031471,8.024000,8.839977,-6.068416,2.457650,-3.970194,2.238894,3.228709,-8.233012,-3.933549,-0.796986,-1.917166,6.201859,-2.031591,9.058694,0.864918,-8.798407,-1.514250,-6.088950,7.216222,2.061271,-9.045918,-9.783556,7.464068,6.251321,-3.297210,-4.881051,-2.146696,3.919151,7.076429,-6.504485,7.991717,0.667586,9.133898,-6.501797,4.589436,-2.781213,-6.045881,8.204151,1.930750,6.026341,-0.785114,-6.532194,5.860022,-5.773779], dtype = "float32")#candidate|1851|(980,)|const|float32
call_1850 = relay.TupleGetItem(func_463_call(relay.reshape(const_1851.astype('float32'), [14, 10, 7])), 4)
call_1852 = relay.TupleGetItem(func_466_call(relay.reshape(const_1851.astype('float32'), [14, 10, 7])), 4)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_1860 = func_947_call()
call_1861 = func_947_call()
bop_1871 = relay.bitwise_xor(const_1842.astype('uint32'), relay.reshape(uop_1845.astype('uint32'), relay.shape_of(const_1842))) # shape=(1, 2, 5)
bop_1875 = relay.bitwise_or(uop_1845.astype('int64'), relay.reshape(bop_1847.astype('int64'), relay.shape_of(uop_1845))) # shape=(1, 2, 5)
func_1483_call = mod.get_global_var('func_1483')
func_1487_call = mutated_mod.get_global_var('func_1487')
const_1881 = relay.const([True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,True,True,True,False,True,True,False,False,False,True], dtype = "bool")#candidate|1881|(330,)|const|bool
call_1880 = relay.TupleGetItem(func_1483_call(relay.reshape(const_1881.astype('bool'), [2, 11, 15]), relay.reshape(call_1850.astype('float32'), [980,]), ), 1)
call_1882 = relay.TupleGetItem(func_1487_call(relay.reshape(const_1881.astype('bool'), [2, 11, 15]), relay.reshape(call_1850.astype('float32'), [980,]), ), 1)
output = relay.Tuple([uop_1843,call_1850,const_1851,call_1860,bop_1871,bop_1875,call_1880,const_1881,])
output2 = relay.Tuple([uop_1843,call_1852,const_1851,call_1861,bop_1871,bop_1875,call_1882,const_1881,])
func_1888 = relay.Function([], output)
mod['func_1888'] = func_1888
mod = relay.transform.InferType()(mod)
mutated_mod['func_1888'] = func_1888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1888_call = mutated_mod.get_global_var('func_1888')
call_1889 = func_1888_call()
output = call_1889
func_1890 = relay.Function([], output)
mutated_mod['func_1890'] = func_1890
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1931 = relay.const([[[-8.796028,-1.674714,8.085276,3.874355,-2.744806,-9.039886,-4.221809,0.110160,6.830105,-2.713576,0.896169,9.824949,-9.504903,8.497517,-0.563357,-9.248279],[-5.638917,-4.650093,-7.099071,-2.429263,-2.069162,-5.134160,2.163264,-5.732095,2.197157,1.873940,5.853350,-3.313749,-8.886954,-0.305977,-0.622603,-1.627757],[9.380269,-2.259343,-8.772678,-1.872728,0.579500,-2.230605,3.405373,2.324926,2.461620,3.979478,6.966067,-7.816453,8.079166,-2.098425,8.863172,-7.738694],[-9.653019,-6.174299,7.292045,7.809111,-4.297391,6.641312,-9.662447,-8.548122,3.644881,-5.370489,2.561207,9.666319,2.390370,-3.862396,-1.468887,-8.594087],[-5.396823,1.489982,1.420895,-1.874326,-9.914343,3.996109,2.013910,2.459141,7.545191,6.756576,-0.427352,0.718863,6.074442,5.202270,-7.130679,-7.458019],[-5.039399,-8.448416,-0.502911,7.489428,1.356038,6.430713,-4.308487,0.454661,-0.597820,-4.683287,2.490481,-1.404850,-4.862032,-0.138554,6.256111,9.498674],[4.562316,-1.592156,-8.632675,-1.619897,-8.528037,-2.841573,-8.455790,5.246786,6.165360,-2.209688,1.546183,5.498560,-2.057001,7.924136,-7.111306,9.203805],[-9.869112,0.098168,-6.377722,-1.533420,9.204682,8.313965,6.451354,-2.687999,9.339225,2.375637,0.039642,-0.227461,9.709929,-5.501954,-1.927885,0.024355],[9.383379,9.581887,-2.323299,-7.822722,8.157536,-3.192814,-6.496718,9.167883,3.266774,6.711645,3.087041,-5.375256,9.722763,-0.983905,-6.972658,-9.392609],[-6.173203,3.640093,-4.870668,-8.420965,-5.631557,-3.758305,5.527428,-1.620701,-9.474344,4.636358,1.717443,-7.657890,-8.009170,-7.539725,-1.517042,-0.907218],[-4.776864,-1.754604,-8.842368,-3.789228,9.797692,3.302346,-0.751969,6.079833,3.317376,-3.293851,-6.457979,5.793324,1.047522,5.036329,3.089666,-1.465919],[-1.261036,-4.427033,3.314848,1.013233,1.130298,1.871105,-7.567770,-8.791110,-3.639263,-5.390390,-5.026544,4.908189,7.357309,4.544048,2.122316,-5.079351],[-2.194508,-3.401887,-2.993887,-5.540731,-2.072325,1.965678,-0.478290,7.646929,2.957453,5.724908,0.451577,2.503139,-6.453701,8.488384,5.849757,8.811097],[-9.477859,3.497525,8.655492,-7.821990,-8.250484,-3.486370,-2.816624,4.859553,3.010623,0.566170,0.496687,8.081656,8.961720,2.379290,-4.807709,4.531991],[-6.032715,3.302138,-9.726492,-3.887407,-5.706526,-8.879878,-9.220184,-2.171672,-0.978310,-3.823518,-6.440450,0.124269,8.108996,-3.065382,8.680284,-4.285551],[2.399584,7.760765,-3.404690,-4.498151,-0.522822,1.987195,-8.556684,-2.018903,3.376649,-8.656663,-6.737664,6.728338,5.030214,-1.119074,3.527048,-1.480492]],[[-4.726034,6.378728,8.056581,8.267459,-4.599067,-4.893890,-8.258299,9.555180,-5.413264,-3.076415,-1.717732,-2.090486,9.184684,-4.307071,9.464686,3.929576],[9.706545,-2.736876,-5.704399,-5.791463,-1.361145,5.624069,-5.739162,-6.864535,6.491170,4.265770,3.928035,5.892870,-1.536959,5.872619,-1.585101,-8.916648],[9.584084,6.528833,-1.333207,-8.977211,-1.681004,-9.855356,0.849004,8.124744,5.603810,-3.492611,-0.110176,6.633894,8.415515,7.206156,-6.061590,2.409095],[-0.868057,5.541491,3.527275,-4.075686,-7.863956,-4.890219,2.042536,-4.381610,-2.585453,9.569697,-5.074405,-7.214336,-7.082561,1.375829,8.886535,-7.402279],[1.351376,-2.577266,-4.324106,9.621701,6.548689,-6.021573,6.457112,7.478792,6.097460,6.193016,-7.486451,9.746453,1.370734,7.200603,-6.436122,-1.067972],[1.336163,-8.075569,1.803951,-0.948111,1.283336,-4.579481,1.962857,-3.902314,-3.488088,-0.297299,7.055717,5.691742,7.489842,9.774113,5.286664,6.244676],[7.238701,-3.678438,0.057232,9.967432,2.370301,-0.623085,-1.917932,2.162473,-8.901573,2.076437,4.493392,-6.926535,8.603636,-5.856006,7.716968,3.799804],[5.229456,-3.411095,4.679521,9.633457,6.989794,0.568311,9.830357,-1.262671,8.701397,5.653137,5.956668,6.556572,-5.562722,2.767234,0.343392,-8.345708],[-3.135576,-8.862684,-6.862409,-2.266395,8.750436,0.585843,-9.998709,-1.317276,5.087446,-7.580327,8.136063,4.256687,-9.294184,3.753924,-2.038777,-8.044351],[-5.017138,-9.277211,7.873813,-0.276508,-6.286631,6.635420,-9.786316,-6.198839,5.371507,-2.999199,-4.890180,-5.662520,-1.616606,6.423864,4.033693,3.539913],[-0.162297,4.379884,-3.111654,-3.078898,6.507315,7.491230,3.645902,-4.993384,-4.690895,2.644305,-3.930276,1.480731,8.362127,7.679901,7.586967,1.812787],[-0.621588,1.379115,-5.591492,-9.375128,6.233409,3.804122,2.548778,0.599788,-7.589255,3.363488,1.627427,2.362633,2.560592,1.473300,5.778019,-9.990019],[0.091836,-3.022494,5.332132,-3.658447,-0.018982,4.671337,1.469962,-3.061239,5.574975,-0.185991,-1.622304,9.314294,5.358175,-4.854943,8.068733,-9.795116],[-4.025495,9.391887,1.210083,-0.672651,9.227846,-8.407934,7.035898,0.296181,-5.891869,2.163780,3.527382,-1.849438,6.036579,-0.686046,8.877962,-3.916138],[1.044707,6.844568,2.833568,2.990178,0.908357,0.521095,-2.549571,3.338167,-9.567131,0.419130,3.940342,-5.011462,1.696818,-7.173226,-7.898325,-1.462583],[-2.379711,-8.319401,-1.311808,-9.385985,7.741106,-3.879349,-5.615064,-7.082276,-0.531632,5.285097,9.332792,-6.194749,-9.754939,7.282521,1.124123,-7.859423]],[[3.956986,9.216461,-2.685689,2.984719,8.033474,2.638603,1.014719,8.923320,-1.843950,-5.732565,-3.964684,-5.693693,8.828746,7.908748,5.316198,-2.976885],[8.508148,-4.402480,3.401271,9.716341,3.215189,8.090110,6.438346,-9.000368,5.753346,9.759922,-4.347811,-3.859802,-3.250605,-8.578699,7.557396,-2.182552],[3.049835,3.794594,0.478680,3.888853,7.723596,3.970662,6.031683,-3.912743,-7.951771,2.635294,8.307607,-0.571816,9.382645,-1.579575,1.157528,3.122037],[0.404766,-6.002763,-8.104622,-5.187956,-1.152966,-4.540125,9.744759,-1.226797,-7.189492,-6.828201,7.782062,7.842101,-8.915481,7.733302,1.565260,-1.444462],[9.437057,2.822558,-2.523331,-6.093122,9.370116,9.161392,8.333413,2.041112,9.297035,-5.827846,-3.613754,1.078186,2.059010,8.086895,-5.013468,9.166404],[-8.267785,3.873909,-4.846310,0.719718,-2.122155,8.480689,-0.133300,3.100155,-3.264859,-9.099893,-7.591056,7.236074,-9.621942,-7.456710,-0.459315,6.087857],[-2.793334,-3.681745,-8.118310,-8.243842,-4.703831,-1.828413,-7.811642,-9.188030,4.917928,-7.476424,-1.422673,2.286932,-2.114936,1.658237,-4.737581,6.575827],[2.587706,5.199357,2.779363,-5.111886,7.181141,-2.134035,9.026226,8.435292,8.213293,-9.560184,7.329177,-5.717012,6.908797,5.814107,-0.987979,-0.967129],[-7.172354,0.605780,7.128821,9.298476,5.133794,6.489763,-5.661458,0.067200,-9.737122,1.638753,-2.392379,6.872030,-7.315032,4.654498,4.459287,-3.902990],[1.564854,3.268384,-1.282861,-7.539957,-3.925144,-8.524075,-2.623419,-1.653693,0.679822,-9.238180,9.834426,6.694455,-5.547601,5.066534,-2.670200,9.188152],[7.713292,-7.514618,1.287091,3.747269,-9.401944,-5.191921,-8.257185,7.065408,8.764528,5.463394,0.007663,-7.724583,1.818405,9.642888,3.474302,7.979756],[7.738231,-1.588607,-2.906979,-2.793598,4.543008,8.777476,4.165130,2.084356,5.693462,-8.662351,6.530875,-1.840126,-6.612517,-3.194891,2.591868,-5.473116],[-1.515390,9.601330,5.543256,4.310224,0.579264,-7.174320,-4.306488,9.882495,-1.277799,-3.442625,-9.692301,-5.981279,8.496771,-2.245986,-0.203161,4.510929],[-4.652641,-3.702765,3.706243,-2.373503,-4.230149,9.500834,9.437179,-9.005244,-3.068199,1.052630,-7.241999,0.833100,9.142389,-8.951262,7.057734,-0.534846],[-6.490918,6.311741,-8.202201,-3.897921,-6.578570,7.149303,-6.760860,4.736787,7.271173,3.135736,-3.885467,3.930591,8.863783,4.782701,6.895224,-5.578076],[-3.493471,2.967812,3.521202,-8.320765,-9.563477,0.235490,5.896565,8.843414,-5.756478,-1.784639,-8.775288,-8.582032,1.161058,-1.128221,6.243649,5.787814]],[[-2.250594,-9.034474,-3.749142,8.172586,0.558717,-3.781827,3.041370,0.817698,-4.109662,-1.756524,6.861623,-9.440057,-0.063791,2.822700,5.304417,-0.815423],[-7.340928,-3.858549,9.231710,7.380403,-2.870829,3.999545,2.724519,0.841267,8.617224,-6.715554,-6.750436,9.241195,5.865918,-4.812413,2.038281,-1.382749],[-4.644354,6.802599,-6.743952,-5.095486,-5.492570,-4.941527,-5.538796,4.093599,5.531750,-1.575690,2.139877,6.218091,-1.329707,1.026103,-9.838091,7.707409],[-5.315081,-2.182458,3.158375,-0.435879,-2.594673,-2.317642,-8.432309,-7.278518,2.282951,-2.245175,5.529856,-4.782170,9.374003,5.831617,2.288187,-8.641212],[4.215411,2.470853,3.002208,-0.440121,-7.060955,-0.633696,0.653772,6.016542,6.940256,8.599043,1.211239,4.889622,4.341497,-9.052688,0.274485,5.804518],[8.521763,-2.081474,-2.636379,-7.796340,3.147064,5.069682,-5.802393,9.675762,-9.782710,-9.264771,-8.434477,6.994433,-6.145180,7.531616,-9.555764,5.698039],[3.905763,2.093070,-1.180085,-6.547615,-6.278472,-9.910606,-2.879724,0.026190,-2.058102,-3.664992,5.850718,6.702784,5.138447,6.430252,7.495671,5.983259],[-8.106659,-5.772175,0.130251,-7.337230,-9.652331,-3.983800,3.061878,-9.988373,3.417345,-9.465924,-1.962251,-9.185650,-0.538894,1.533501,-4.843219,-7.937611],[9.937282,-7.994870,-3.552413,7.102616,1.546178,6.270084,1.176228,1.467389,0.049437,0.087922,2.904092,1.299410,3.783783,7.628464,-3.647342,3.062767],[-1.460415,-0.752099,-9.966366,5.940207,2.033322,-2.356946,-9.349771,1.047226,-0.015895,3.836584,-9.943276,8.025391,-9.175466,-7.787014,8.786453,-2.153574],[2.845139,-1.623654,-4.399444,7.313274,-7.559007,-9.292526,7.738944,-8.673023,-4.230466,4.581261,0.409663,7.557064,7.922768,-1.592967,4.206476,-7.020054],[8.619686,-3.008624,4.765948,1.065049,-1.327392,-7.543501,5.322529,9.463705,2.961672,-1.740380,9.353192,-0.953323,0.263450,0.841542,1.976850,4.626048],[-8.982542,5.737145,-7.284103,-3.245115,-0.619890,-6.142739,6.986281,-8.917474,9.570643,0.129727,-6.423689,8.698235,-7.290915,-3.817528,9.458625,-0.855204],[8.082062,4.023775,-1.725318,-5.246368,-1.202950,-1.132301,-1.103930,-7.931948,-1.785494,1.027001,5.538950,-1.568103,3.077335,-4.656283,9.082373,1.618233],[-1.945607,-8.540506,-3.325763,3.094567,9.325669,-8.128754,-0.977312,7.356186,0.350920,2.297666,-7.189273,-2.616809,-6.245280,-4.026068,-2.846038,4.021211],[-3.161052,0.718630,-4.226656,1.917378,7.506379,-4.100330,8.459571,-7.243856,-6.740402,1.834607,0.396246,-3.794243,-8.696416,6.107623,-2.751650,0.244282]],[[-8.635631,7.136951,-1.564780,2.064447,6.155849,5.641981,6.443300,2.805003,-1.588944,-7.887531,-0.820174,9.091253,3.997803,3.840086,4.568866,-8.224701],[-3.856256,4.054417,5.090903,-6.499453,-0.815521,8.059822,2.981350,6.374221,2.706501,8.909591,-5.822909,9.523931,-9.086113,-8.400169,1.558108,5.023297],[-8.564012,-2.127070,3.171512,-2.894383,5.344773,-5.772060,-1.120924,-5.155895,0.842616,-6.695356,-8.139918,-0.686490,-8.377006,0.348933,3.345036,4.720166],[8.424520,5.942066,-4.926118,-4.198663,0.819208,-0.805289,-6.004689,-2.654669,1.038910,9.116634,-2.909950,-9.679631,-3.896555,-1.422740,-9.636615,-7.445891],[-5.224367,1.779321,9.483303,-7.547470,-9.311212,5.690047,2.990673,-9.859804,-7.714014,-9.382562,9.973281,2.828727,-2.537614,-4.289420,-8.333545,-3.756972],[-5.324367,8.658126,7.023808,0.756682,4.815879,-3.270752,-4.542958,7.485913,3.867530,5.761776,-6.096703,-3.610642,-5.518027,5.167670,5.649520,8.137297],[2.763481,-0.615668,-5.845246,-5.238990,-6.332024,-4.429045,-0.962797,5.940166,-8.919699,-4.443347,0.919190,4.471826,9.714183,-9.545017,8.457981,0.408479],[5.414877,8.625096,1.040255,6.639907,9.233642,-2.111083,9.653294,9.332643,-6.927623,-1.942539,-3.389339,9.469350,-1.316777,6.654886,-2.081498,4.203551],[-5.931303,8.787240,-3.062910,8.813633,4.212578,1.806308,3.380272,-5.397760,2.990379,6.750463,-4.711796,6.823562,7.604678,-7.497397,6.794320,5.765236],[0.288942,3.025839,2.177580,4.522734,-5.075497,8.941147,9.504171,7.341744,-4.652458,-7.200101,-6.164166,0.395397,-5.351392,0.237539,5.811935,0.107080],[1.991966,0.850126,5.387034,1.872762,9.059835,6.272493,-5.900878,8.775608,-1.427466,-2.524559,-9.986134,-0.477366,5.812967,-1.739622,-2.165191,6.573791],[8.177380,-5.520044,0.006748,-2.977150,-1.867365,9.544559,2.740982,5.500633,5.887041,-7.878401,0.399340,-4.885688,-0.553229,-5.918588,9.113626,-1.657085],[-6.935384,2.487555,8.675960,-6.469969,-0.632704,-0.701493,5.849149,5.916696,8.647627,-9.832213,-7.599260,-3.884657,6.146838,7.410011,-8.928744,8.384006],[-1.935090,1.226340,5.139819,4.614104,0.476790,9.215534,6.643763,7.546126,-5.080813,3.417062,6.868906,6.768028,-9.259935,2.634311,-8.982483,8.855102],[9.121353,-6.269602,9.198196,-1.806224,-4.450741,0.253186,-1.082036,-1.151830,-6.221488,4.745897,5.911910,-1.179009,8.619886,6.044205,3.024984,-7.554111],[7.729098,5.441245,-2.702044,3.005342,4.697677,-4.673455,-7.980967,-4.649577,0.154260,-9.951958,-0.603427,-1.463623,-0.157433,5.056847,5.025483,-4.793950]],[[7.225795,0.393738,-8.607341,-7.699551,7.759477,5.362816,4.572897,-3.163552,-5.090530,-0.649068,1.433128,-5.227924,-4.428763,5.834696,-5.836663,-2.853923],[1.977312,7.191425,-6.840257,5.010300,5.757936,2.293242,-8.364630,3.074968,-7.660994,8.699074,-4.346850,4.740812,-4.508513,-2.058812,8.210113,-9.864111],[-5.068694,-5.170513,6.429039,-7.201639,-3.127236,5.051481,7.228990,1.684185,-8.273456,-7.549320,3.697546,3.782119,-1.367573,-2.427368,-3.215209,8.728638],[-1.376009,-7.829160,1.572391,-9.239743,-7.611344,4.400549,-2.943385,-7.726245,1.437948,-2.547079,-0.396067,-6.554913,5.080363,-4.506201,7.422574,4.549764],[5.597086,2.665054,-3.167742,3.570050,-4.762410,9.708540,6.336478,7.111450,-5.038930,2.250268,-0.773508,0.120937,-9.605378,1.948392,2.358050,-1.004576],[-4.620236,-8.763139,9.625538,-8.588872,-5.057609,5.397573,4.303107,-8.629707,-4.715579,-0.712066,-3.864723,-4.946001,-2.016026,-9.001189,-2.892841,-4.672618],[2.249176,-2.674114,-4.813350,-3.178010,-9.400727,1.355465,-1.716463,2.749869,8.055337,9.004361,8.025647,6.254853,-0.471382,-7.260888,-6.404792,1.843053],[2.330113,-8.693185,-5.707602,-7.960174,-5.688983,-7.708552,3.685201,0.443902,-8.130254,-0.279044,9.267598,1.802624,-5.171239,-4.815342,-5.504531,-3.190885],[8.598277,-0.954111,7.467307,-0.774886,-7.836939,-7.540678,-7.670106,-2.948768,0.980847,5.397750,-2.492883,-5.770491,-0.548393,0.543362,-4.762466,-7.328328],[0.081942,-1.002105,4.886201,-5.402470,8.608070,1.420110,9.558010,-1.021611,1.453422,1.960842,-8.932887,-8.375706,-5.331668,-5.961152,7.794011,0.708978],[8.138261,3.869688,-1.214259,-4.547571,-9.690599,-9.765687,6.020631,-0.031293,-1.584766,6.552250,9.478388,8.878440,9.668397,2.422154,-9.501936,3.199126],[-5.987469,-2.380038,3.212600,-0.595632,-5.117437,6.408325,-8.081765,-3.758656,4.584585,8.302094,7.578636,-5.426280,-7.668276,1.988137,-4.709290,-9.816297],[8.955810,-9.996033,0.976451,4.424141,5.717444,-5.563986,-1.462343,-2.552108,-6.354874,2.768467,-0.061659,-4.283585,3.690728,6.881192,2.755817,-4.511882],[-9.574049,0.929774,8.132183,2.687748,5.576457,-1.550686,9.606651,6.297846,5.125086,6.297251,-7.595681,-2.123473,-0.948852,-5.250322,-6.896952,-3.058374],[6.108970,-4.967601,-6.129546,7.648628,4.042317,-1.783594,-9.007391,-1.618870,-3.758614,1.531447,-2.333009,-3.099792,6.624149,-5.298386,2.638509,-2.700945],[-2.855478,0.889932,-5.383269,-8.052975,4.721167,-0.191959,-3.208051,8.420067,2.655983,0.498784,-3.718235,-3.045146,-1.345236,3.303470,7.858044,-0.202322]],[[2.781209,7.094650,-5.085505,4.000076,-5.826384,4.042246,8.305488,6.749610,7.460837,-8.457210,-5.903130,5.145332,3.073267,-1.769323,-5.636960,-2.831946],[-0.667943,-5.229216,1.243492,-3.840090,6.441926,-3.205011,-3.603719,1.253520,-6.975074,-8.742654,-7.313964,-9.726525,-6.425284,6.275166,0.630030,-5.472537],[9.846427,3.165669,6.468692,-4.121334,8.120307,2.865039,-4.709438,-0.264938,-3.215759,4.868648,-0.821209,-6.214140,-2.243354,-3.298707,9.320101,5.754219],[7.759433,2.811700,5.515808,2.064359,-5.010493,-6.369330,-0.761695,5.906025,1.344587,1.114487,-8.382179,8.704262,9.926426,0.296787,-0.368474,4.544199],[0.302028,-4.755988,-9.895460,1.343104,-8.375975,9.722385,-4.982270,3.082344,1.491630,-9.439481,-2.728831,-6.673784,7.923166,-6.983083,0.492761,7.556889],[-2.088840,8.637050,8.972226,3.006383,-1.053886,-8.364684,-1.906935,5.870418,3.832692,5.714478,6.211915,9.804658,7.024843,-6.954932,-1.919982,9.255102],[-6.757280,6.266720,-5.963656,5.914590,-9.020272,5.149867,-2.263504,-9.439459,-5.300001,5.967988,-1.603924,-6.177646,0.736597,-9.750596,-9.745773,-7.055185],[-0.292931,9.134727,5.950715,5.306900,-3.357259,-0.149045,4.108528,-8.132534,-2.875294,1.195205,9.207072,7.002752,6.363252,-7.197414,6.180155,-6.678071],[-5.552676,-1.824365,-8.337754,1.901652,8.675101,6.586976,0.454419,-4.081169,-8.155263,-4.413325,-8.129538,-6.364082,3.944147,1.946783,1.661372,-4.801515],[4.514851,1.760570,-2.324994,2.603501,-8.703130,9.774607,-0.901542,-2.701271,3.369301,-2.693493,-6.440075,6.698634,7.530549,-9.208481,-2.145696,3.652881],[-4.275940,-6.826332,6.137505,-1.626277,-8.555259,6.021982,6.745877,3.870501,-9.894702,-4.986786,-3.318189,-0.619595,1.559270,8.995705,1.259573,5.213229],[7.477249,0.554173,0.914564,9.282911,5.363146,5.853200,-8.526894,7.152911,-4.768096,8.624062,-8.483960,8.800222,-1.080946,1.672258,5.146926,8.548220],[-3.726706,4.160112,-3.580129,-4.626822,-4.948600,4.600921,-5.547262,9.763318,-6.194515,-6.644099,4.297418,-5.436768,-6.327204,5.610330,0.365502,-0.446068],[3.079746,7.886047,-8.772108,9.545731,9.805126,8.728237,-7.672556,2.136924,9.491448,2.514366,5.877118,0.888973,8.769324,8.959755,0.737185,7.202408],[8.648755,3.255581,-4.039349,-5.472654,4.526676,7.073075,0.206588,-2.578382,-9.937488,2.975517,-1.220124,3.139788,1.519026,-7.439910,7.905634,-2.453567],[-3.274240,-8.058185,-3.235769,2.427567,9.505554,1.812304,3.343725,2.977658,7.142297,0.837347,6.317363,-7.577032,9.923569,-1.378919,-1.630425,6.823626]],[[-1.652117,3.713258,1.108399,-9.021398,4.051556,2.529514,0.886442,7.410205,9.635014,-5.836191,0.239515,1.601178,9.202550,3.294454,-7.282494,7.807300],[9.558487,-6.515995,1.232281,6.095512,-1.603935,6.383249,1.471826,6.014680,6.695442,-1.195233,-3.735601,4.742530,6.993966,7.442912,7.013874,-4.949080],[0.984497,9.966373,5.403183,6.978831,2.653754,8.710887,8.646829,3.550984,8.527447,-7.810064,-5.615712,7.826097,-2.783191,5.663988,8.889661,-2.886811],[-1.262379,1.884111,-3.340516,-7.401871,3.492886,4.615836,-7.426575,7.006444,-9.285358,1.088740,8.886627,-7.628256,7.955565,-6.214095,8.292520,7.876326],[-5.690936,1.339932,9.754993,3.163987,4.942254,-6.383753,1.369106,9.128387,6.714463,-7.060117,-9.168356,-0.860280,3.402798,-9.211009,-5.155318,-6.794991],[7.452422,9.406330,5.235300,8.780392,4.095865,-7.386995,-8.853464,-6.845929,-5.149409,-6.322515,4.147663,-8.547778,4.479405,1.004244,-3.535263,2.793478],[4.110048,8.955574,1.497940,-7.474403,-2.596448,3.744286,-2.583271,-7.408520,9.637338,7.631912,2.579075,3.410922,3.897323,-3.572344,-5.617852,6.587466],[3.142202,5.582432,0.760345,6.703567,-0.311160,-2.567298,6.420572,-9.513765,-9.769015,6.699926,1.166137,-1.801677,-5.095339,0.442925,-4.386637,-0.255422],[2.039847,-0.295944,7.175906,-4.590207,0.316363,3.683426,0.594704,5.384455,0.183968,7.373631,2.100920,9.534967,0.302597,-6.380715,2.607562,1.915412],[-0.672936,-1.472719,5.128241,-6.468373,1.951567,5.619887,8.937042,-7.530877,-3.444773,9.003520,-7.525323,9.659871,0.157117,5.022623,-2.180408,0.866048],[7.364980,0.494343,-9.080163,4.824757,2.193625,-9.813667,9.902624,8.476819,5.912911,4.389990,-1.550854,2.817146,-2.792473,-7.849223,2.292747,-4.335688],[2.291781,0.948632,2.350372,-2.997471,-9.594504,8.347514,4.828463,7.781891,5.989621,-0.735639,0.265797,-7.013385,4.687082,-8.887125,-8.430974,0.557601],[-7.271649,-7.531025,1.829954,-4.225377,8.313050,2.356111,7.677102,5.861010,5.865600,-5.563190,5.714334,-1.145062,4.918398,5.977257,2.396417,-1.723244],[-5.987289,6.410261,8.000093,2.679545,5.907473,7.798753,0.792152,-2.545890,7.811220,4.508487,1.835211,3.190301,-4.567023,-1.654256,2.947389,-5.053115],[4.138837,7.474332,1.538704,-2.073830,4.506381,9.596643,-8.596331,7.901368,-3.313894,1.313148,-9.780985,7.527871,6.322374,8.682484,-7.289539,-2.656331],[9.107531,-2.868386,-7.977807,-4.715010,-6.952354,-9.633970,1.457256,-8.963006,-7.029603,0.659349,-0.745879,-5.124502,-8.664189,-9.906574,4.031795,8.746928]]], dtype = "float32")#candidate|1931|(8, 16, 16)|const|float32
var_1932 = relay.var("var_1932", dtype = "float32", shape = (8, 16, 16))#candidate|1932|(8, 16, 16)|var|float32
bop_1933 = relay.floor_divide(const_1931.astype('float32'), relay.reshape(var_1932.astype('float32'), relay.shape_of(const_1931))) # shape=(8, 16, 16)
func_139_call = mod.get_global_var('func_139')
func_141_call = mutated_mod.get_global_var('func_141')
call_1945 = relay.TupleGetItem(func_139_call(), 0)
call_1946 = relay.TupleGetItem(func_141_call(), 0)
output = relay.Tuple([bop_1933,call_1945,])
output2 = relay.Tuple([bop_1933,call_1946,])
func_1950 = relay.Function([var_1932,], output)
mod['func_1950'] = func_1950
mod = relay.transform.InferType()(mod)
var_1951 = relay.var("var_1951", dtype = "float32", shape = (8, 16, 16))#candidate|1951|(8, 16, 16)|var|float32
output = func_1950(var_1951)
func_1952 = relay.Function([var_1951], output)
mutated_mod['func_1952'] = func_1952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_1956 = relay.TupleGetItem(func_391_call(), 0)
call_1957 = relay.TupleGetItem(func_392_call(), 0)
output = relay.Tuple([call_1956,])
output2 = relay.Tuple([call_1957,])
func_1958 = relay.Function([], output)
mod['func_1958'] = func_1958
mod = relay.transform.InferType()(mod)
mutated_mod['func_1958'] = func_1958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mutated_mod.get_global_var('func_1958')
call_1959 = func_1958_call()
output = call_1959
func_1960 = relay.Function([], output)
mutated_mod['func_1960'] = func_1960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_311_call = mod.get_global_var('func_311')
func_313_call = mutated_mod.get_global_var('func_313')
call_1961 = relay.TupleGetItem(func_311_call(), 1)
call_1962 = relay.TupleGetItem(func_313_call(), 1)
output = call_1961
output2 = call_1962
func_1979 = relay.Function([], output)
mod['func_1979'] = func_1979
mod = relay.transform.InferType()(mod)
mutated_mod['func_1979'] = func_1979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1979_call = mutated_mod.get_global_var('func_1979')
call_1980 = func_1979_call()
output = call_1980
func_1981 = relay.Function([], output)
mutated_mod['func_1981'] = func_1981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_1999 = relay.TupleGetItem(func_859_call(), 4)
call_2000 = relay.TupleGetItem(func_860_call(), 4)
func_1422_call = mod.get_global_var('func_1422')
func_1423_call = mutated_mod.get_global_var('func_1423')
call_2003 = relay.TupleGetItem(func_1422_call(), 0)
call_2004 = relay.TupleGetItem(func_1423_call(), 0)
output = relay.Tuple([call_1999,call_2003,])
output2 = relay.Tuple([call_2000,call_2004,])
func_2009 = relay.Function([], output)
mod['func_2009'] = func_2009
mod = relay.transform.InferType()(mod)
mutated_mod['func_2009'] = func_2009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mutated_mod.get_global_var('func_2009')
call_2010 = func_2009_call()
output = call_2010
func_2011 = relay.Function([], output)
mutated_mod['func_2011'] = func_2011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_2015 = relay.TupleGetItem(func_859_call(), 4)
call_2016 = relay.TupleGetItem(func_860_call(), 4)
func_1219_call = mod.get_global_var('func_1219')
func_1220_call = mutated_mod.get_global_var('func_1220')
call_2059 = relay.TupleGetItem(func_1219_call(), 1)
call_2060 = relay.TupleGetItem(func_1220_call(), 1)
func_1979_call = mod.get_global_var('func_1979')
func_1981_call = mutated_mod.get_global_var('func_1981')
call_2080 = func_1979_call()
call_2081 = func_1979_call()
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_2085 = relay.TupleGetItem(func_1958_call(), 0)
call_2086 = relay.TupleGetItem(func_1960_call(), 0)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_2101 = relay.TupleGetItem(func_376_call(), 0)
call_2102 = relay.TupleGetItem(func_377_call(), 0)
func_1200_call = mod.get_global_var('func_1200')
func_1201_call = mutated_mod.get_global_var('func_1201')
call_2104 = relay.TupleGetItem(func_1200_call(), 0)
call_2105 = relay.TupleGetItem(func_1201_call(), 0)
func_139_call = mod.get_global_var('func_139')
func_141_call = mutated_mod.get_global_var('func_141')
call_2106 = relay.TupleGetItem(func_139_call(), 0)
call_2107 = relay.TupleGetItem(func_141_call(), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_2111 = relay.TupleGetItem(func_1112_call(), 0)
call_2112 = relay.TupleGetItem(func_1113_call(), 0)
output = relay.Tuple([call_2015,call_2059,call_2080,call_2085,call_2101,call_2104,call_2106,call_2111,])
output2 = relay.Tuple([call_2016,call_2060,call_2081,call_2086,call_2102,call_2105,call_2107,call_2112,])
func_2121 = relay.Function([], output)
mod['func_2121'] = func_2121
mod = relay.transform.InferType()(mod)
mutated_mod['func_2121'] = func_2121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2121_call = mutated_mod.get_global_var('func_2121')
call_2122 = func_2121_call()
output = call_2122
func_2123 = relay.Function([], output)
mutated_mod['func_2123'] = func_2123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_2127 = relay.TupleGetItem(func_1958_call(), 0)
call_2128 = relay.TupleGetItem(func_1960_call(), 0)
func_1422_call = mod.get_global_var('func_1422')
func_1423_call = mutated_mod.get_global_var('func_1423')
call_2143 = relay.TupleGetItem(func_1422_call(), 0)
call_2144 = relay.TupleGetItem(func_1423_call(), 0)
func_568_call = mod.get_global_var('func_568')
func_570_call = mutated_mod.get_global_var('func_570')
call_2150 = relay.TupleGetItem(func_568_call(), 2)
call_2151 = relay.TupleGetItem(func_570_call(), 2)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
var_2162 = relay.var("var_2162", dtype = "float64", shape = (80,))#candidate|2162|(80,)|var|float64
call_2161 = relay.TupleGetItem(func_1319_call(relay.reshape(call_2127.astype('float64'), [14, 10, 7]), relay.reshape(var_2162.astype('float64'), [80, 1]), ), 5)
call_2163 = relay.TupleGetItem(func_1322_call(relay.reshape(call_2127.astype('float64'), [14, 10, 7]), relay.reshape(var_2162.astype('float64'), [80, 1]), ), 5)
func_1979_call = mod.get_global_var('func_1979')
func_1981_call = mutated_mod.get_global_var('func_1981')
call_2187 = func_1979_call()
call_2188 = func_1979_call()
output = relay.Tuple([call_2127,call_2143,call_2150,call_2161,var_2162,call_2187,])
output2 = relay.Tuple([call_2128,call_2144,call_2151,call_2163,var_2162,call_2188,])
func_2190 = relay.Function([var_2162,], output)
mod['func_2190'] = func_2190
mod = relay.transform.InferType()(mod)
mutated_mod['func_2190'] = func_2190
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2191 = relay.var("var_2191", dtype = "float64", shape = (80,))#candidate|2191|(80,)|var|float64
func_2190_call = mutated_mod.get_global_var('func_2190')
call_2192 = func_2190_call(var_2191)
output = call_2192
func_2193 = relay.Function([var_2191], output)
mutated_mod['func_2193'] = func_2193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1413_call = mod.get_global_var('func_1413')
func_1415_call = mutated_mod.get_global_var('func_1415')
call_2247 = relay.TupleGetItem(func_1413_call(), 0)
call_2248 = relay.TupleGetItem(func_1415_call(), 0)
output = call_2247
output2 = call_2248
func_2260 = relay.Function([], output)
mod['func_2260'] = func_2260
mod = relay.transform.InferType()(mod)
output = func_2260()
func_2261 = relay.Function([], output)
mutated_mod['func_2261'] = func_2261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_2305 = relay.TupleGetItem(func_1112_call(), 0)
call_2306 = relay.TupleGetItem(func_1113_call(), 0)
output = relay.Tuple([call_2305,])
output2 = relay.Tuple([call_2306,])
func_2326 = relay.Function([], output)
mod['func_2326'] = func_2326
mod = relay.transform.InferType()(mod)
output = func_2326()
func_2327 = relay.Function([], output)
mutated_mod['func_2327'] = func_2327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1520_call = mod.get_global_var('func_1520')
func_1522_call = mutated_mod.get_global_var('func_1522')
call_2374 = relay.TupleGetItem(func_1520_call(), 0)
call_2375 = relay.TupleGetItem(func_1522_call(), 0)
func_1756_call = mod.get_global_var('func_1756')
func_1760_call = mutated_mod.get_global_var('func_1760')
const_2385 = relay.const([[-7.911302,-4.961247,2.210126,-6.837286,2.476361,-8.426815,-1.201064,0.081357,2.283110,-5.107286,-2.786867,1.991091,5.875404,4.178216,-9.521442,-7.541414,2.145276,-1.975572,6.846398,-6.915446,-3.887833,-6.734544,3.702033,8.690240,9.404414,5.971241,-7.979907,-7.357624,1.547509,6.401059,-0.603344,8.784388,3.757867,-4.930957,-3.323543,0.143953,-2.986051,-6.295847,4.643728,-3.750771,2.035999,-0.202219,-6.378644,0.040568,-3.670497,0.785352,2.281270,-6.461096,6.416484,7.564370,-9.125608,-8.250678,-0.913185,-3.534131,-4.701891,-5.743963,-0.211502,-0.809550,8.666256,8.043745,-3.398363,-6.620418,8.461036,-0.911165,9.459179,-7.507883,1.830874,-1.535970,1.274115,5.828335,-1.829880,-5.013550,4.820510,9.851229,-0.936554,-2.486901,-9.056393,-8.562682,-0.226526,-4.233349]], dtype = "float64")#candidate|2385|(1, 80)|const|float64
var_2386 = relay.var("var_2386", dtype = "float64", shape = ())#candidate|2386|()|var|float64
call_2384 = relay.TupleGetItem(func_1756_call(relay.reshape(const_2385.astype('float64'), [80,]), relay.reshape(var_2386.astype('float64'), []), ), 4)
call_2387 = relay.TupleGetItem(func_1760_call(relay.reshape(const_2385.astype('float64'), [80,]), relay.reshape(var_2386.astype('float64'), []), ), 4)
func_139_call = mod.get_global_var('func_139')
func_141_call = mutated_mod.get_global_var('func_141')
call_2388 = relay.TupleGetItem(func_139_call(), 0)
call_2389 = relay.TupleGetItem(func_141_call(), 0)
func_1200_call = mod.get_global_var('func_1200')
func_1201_call = mutated_mod.get_global_var('func_1201')
call_2396 = relay.TupleGetItem(func_1200_call(), 0)
call_2397 = relay.TupleGetItem(func_1201_call(), 0)
uop_2398 = relay.acosh(const_2385.astype('float32')) # shape=(1, 80)
bop_2400 = relay.greater(uop_2398.astype('bool'), var_2386.astype('bool')) # shape=(1, 80)
output = relay.Tuple([call_2374,call_2384,call_2388,call_2396,bop_2400,])
output2 = relay.Tuple([call_2375,call_2387,call_2389,call_2397,bop_2400,])
func_2410 = relay.Function([var_2386,], output)
mod['func_2410'] = func_2410
mod = relay.transform.InferType()(mod)
mutated_mod['func_2410'] = func_2410
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2411 = relay.var("var_2411", dtype = "float64", shape = ())#candidate|2411|()|var|float64
func_2410_call = mutated_mod.get_global_var('func_2410')
call_2412 = func_2410_call(var_2411)
output = call_2412
func_2413 = relay.Function([var_2411], output)
mutated_mod['func_2413'] = func_2413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_2462 = relay.TupleGetItem(func_859_call(), 0)
call_2463 = relay.TupleGetItem(func_860_call(), 0)
output = call_2462
output2 = call_2463
func_2470 = relay.Function([], output)
mod['func_2470'] = func_2470
mod = relay.transform.InferType()(mod)
output = func_2470()
func_2471 = relay.Function([], output)
mutated_mod['func_2471'] = func_2471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1979_call = mod.get_global_var('func_1979')
func_1981_call = mutated_mod.get_global_var('func_1981')
call_2485 = func_1979_call()
call_2486 = func_1979_call()
output = call_2485
output2 = call_2486
func_2491 = relay.Function([], output)
mod['func_2491'] = func_2491
mod = relay.transform.InferType()(mod)
mutated_mod['func_2491'] = func_2491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2491_call = mutated_mod.get_global_var('func_2491')
call_2492 = func_2491_call()
output = call_2492
func_2493 = relay.Function([], output)
mutated_mod['func_2493'] = func_2493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1200_call = mod.get_global_var('func_1200')
func_1201_call = mutated_mod.get_global_var('func_1201')
call_2542 = relay.TupleGetItem(func_1200_call(), 0)
call_2543 = relay.TupleGetItem(func_1201_call(), 0)
func_1008_call = mod.get_global_var('func_1008')
func_1012_call = mutated_mod.get_global_var('func_1012')
const_2546 = relay.const([7,2,-2,-10,-4,7,10,-9,5,-8,-8,3,-2,10,-10,-5,-4,10,4,8,7,-9,-3,7,2,2,-10,6,5,-5,-1,-2,9,-1,-2,-10,6,-5,-2,7,-8,4,4,-1,-5,4,7,3,7,-9,-4,-5,-10,9,3,-4,7,-8,-7,9,-5,10,-10,8,-10,6,5,4,4,-7,-9,9,-10,-8,5,-9,-2,-4,5,-10,10,6,-9,-3,4,-1,1,-1,-8,8,-6,-6,7,1,-4,6,6,1,2,10,4,-1,3,5,-8,-7,-9,3,2,9,-6,4,-7,-9,9,-5,5,9,5,-1,7,9,8,-4,-9,-10,6,-7,9,1,5,10,-1,8,-2,-3,5,-5,-8,-5,1,-10,-9,1,-2,5,-10,7,-5,1,4,-6,-8,5,-9,-2,8,-7,-10,-7,3,-10,-9,6,2,1,1,-8,-8,6,-3,-8,-2,-10,-5,3,-8,-1,-9,-1,4,8,9,6,-9,5,-3,-3,-9,-7,9,-2,-4,4,-10,4,-6,3,10,-5,4,-1,2,-1,-8,-5,10,-5,-10,6,3,6,-4,-7,8,3,1,-8,9,-5,-10,3,-8,4,7,-10,2,2,-4,-2,8,-8,-9,-3,8,5,-8,9,7,6,3,-6,1,-3,-6,1,10,4,-8,8,-5,-5,1,1,-5,-6,2,-3,2,1,-3,-2,2,4,5,5,5,4,-1,-8,3,-5,7,-1,-6,-7,-5,-1,6,-6,-7,2,-10,-2,3,-7,3,3,-2,9,7,6,-6,8,2,3,-4,3,-3,-6,6,-5,7,-1,2,-6,5,-8,9,-2,-9,-2,2,-8,-2,-1,10,-7,4,8], dtype = "int32")#candidate|2546|(320,)|const|int32
call_2545 = relay.TupleGetItem(func_1008_call(relay.reshape(const_2546.astype('int32'), [2, 16, 10]), relay.reshape(const_2546.astype('int32'), [2, 16, 10]), ), 0)
call_2547 = relay.TupleGetItem(func_1012_call(relay.reshape(const_2546.astype('int32'), [2, 16, 10]), relay.reshape(const_2546.astype('int32'), [2, 16, 10]), ), 0)
const_2552 = relay.const([[[-5.764390,-8.658148,-1.088369,7.552557,-8.458933,2.737833,-1.719150],[-1.969004,4.144308,-1.467112,8.721543,-3.360918,6.880797,5.144867],[-1.139790,-8.730193,-5.428929,-6.522129,1.146491,-1.364472,1.945270],[-4.293599,-3.292715,5.234034,0.767861,-8.947617,0.862740,-8.257394],[9.647044,-7.877276,-3.488777,-6.774890,8.584745,-0.484693,-8.459989],[-1.754746,-3.762735,-0.117186,3.585634,-4.247701,9.930938,-5.856668],[6.256966,-2.116699,-6.028797,9.253088,7.202153,2.457990,-1.177608],[1.479599,-9.595998,-0.521408,-9.155372,1.858088,-2.809659,-0.048410],[-3.587745,-8.235231,-5.405030,-2.314762,4.799839,3.538924,7.547605],[-5.412385,-6.911591,9.086545,3.886745,4.726408,-8.209994,-3.203286]],[[-6.434200,-0.117071,1.724410,3.479230,3.969638,-4.667691,1.765893],[5.617229,-3.234862,-0.592604,3.629803,0.023042,9.382361,-1.602541],[0.081403,1.038955,-6.391272,9.091297,-2.799887,2.276651,-7.509825],[3.688836,1.772774,0.598604,-4.772978,3.446314,9.131104,-1.969282],[4.888087,-7.225741,8.261140,9.285851,2.038136,8.492055,5.595252],[-3.195864,-9.576483,2.216118,-9.393759,3.222600,-8.342443,3.061228],[4.689267,-8.117448,-7.047057,-3.363448,-2.696619,8.102707,-0.126709],[-4.995208,1.683297,9.121869,-1.444043,-3.396263,2.045474,0.261387],[-3.774623,7.895223,-8.123378,-5.173797,-1.984369,0.051685,-1.121760],[6.375207,8.019464,-7.369169,-1.289020,7.927229,-4.477741,9.956647]],[[6.536546,8.805836,1.496715,-8.204953,9.930453,8.470646,3.416184],[-1.646431,2.930338,-0.596307,1.399973,-2.584234,-8.762762,-4.372475],[2.250652,1.343767,-4.533003,-3.181537,1.475097,-4.810930,7.359693],[5.094145,-7.172817,8.216129,9.931444,-0.998234,-2.640108,-4.607363],[-2.040165,-8.388600,-3.286041,4.719823,-3.243545,1.241280,-7.919864],[-9.358678,3.260749,-1.994504,-2.244469,1.934693,4.373537,-7.882831],[-5.751990,-9.358239,-0.594747,-1.334204,-2.141899,0.331471,9.988396],[9.072213,-2.818633,-0.497843,0.936391,7.272659,-0.285174,5.134342],[2.772238,3.040196,-4.968936,-1.168600,-6.155221,6.682456,-9.948689],[-8.757222,6.896711,0.439559,0.228542,7.095984,-3.045883,-7.186291]],[[-2.853620,-7.562053,-8.858401,3.407667,-8.961334,0.036250,1.722537],[9.106622,3.496089,3.063569,6.358490,8.321859,-1.176018,2.220580],[9.084483,7.656009,3.824344,0.177694,-4.172106,-1.736339,5.809212],[3.736776,4.044111,-1.357145,-5.185597,2.744253,3.028509,3.142364],[-2.888222,-9.642570,-5.880210,0.344874,-6.585135,4.372472,0.496402],[6.953485,6.836892,4.694635,0.870383,-2.701929,-3.672187,-2.581522],[-5.963067,7.697077,-6.689220,-3.108539,-9.044021,1.744880,3.764131],[4.222515,-6.766447,0.320411,6.579263,-0.782882,-1.112372,2.766345],[2.459749,-6.219130,5.967153,-4.500142,-0.091403,-7.241779,-8.909120],[5.831564,1.170784,-2.973588,9.992794,4.811021,9.737864,5.957399]],[[-7.458760,-1.178722,-5.005089,7.972658,-4.337069,-6.551557,7.363230],[7.333608,-2.428150,4.861274,7.203626,5.651588,9.706774,-3.011765],[0.022721,-8.024761,-9.045097,6.582296,-6.481368,-9.657846,-4.932115],[4.015168,5.561037,1.216931,4.285054,5.282882,-0.822106,1.221515],[-5.070018,-9.246837,4.473406,1.461191,0.777508,0.873623,-8.912225],[0.978008,-9.963764,-3.426524,2.673903,2.491730,-2.395984,-4.869637],[3.877653,-8.153630,4.636402,0.060755,9.610261,-0.136408,0.671485],[-5.009445,1.951839,-0.400849,-0.796930,3.457205,-1.312706,-1.272369],[-5.790741,-2.165872,-4.140292,2.560981,4.174785,5.521310,9.805269],[-8.932307,7.954255,-7.055497,-3.408280,-0.130975,8.338850,-6.414424]],[[-9.882316,-8.367107,7.859120,-3.778437,2.583490,9.780330,8.625975],[-0.961393,-8.778996,0.228983,4.607716,-9.708529,7.872812,8.065733],[8.581115,-7.242563,-6.866996,-7.030952,5.891350,-3.318910,-2.543391],[-9.771673,-9.837506,-6.776091,4.659759,-5.456226,-0.806297,-8.674280],[7.429374,-0.865509,1.175073,-2.002108,-7.176010,-3.955075,7.900130],[-3.760723,-2.593996,1.002148,0.408439,-0.374150,-1.149375,-4.566342],[6.986906,-5.102334,-5.204709,6.683040,0.656520,7.847943,-2.576920],[-3.795430,-3.191492,6.563594,5.294322,7.844760,2.883095,6.924122],[-6.806109,-2.632052,-0.216329,-4.043149,9.099479,-3.564262,8.856638],[-8.499116,6.995523,-8.954069,-9.513870,1.558424,-8.783473,-7.314028]],[[-6.811283,9.341729,9.353221,-1.132481,-9.290434,-0.555867,5.065867],[9.987616,7.706494,-1.560492,-4.283617,-8.936427,9.213847,-7.443540],[0.428199,3.748585,-9.822761,-2.817485,-5.109101,2.947750,-8.221016],[-8.483432,-1.751554,-7.715861,-6.621077,1.912928,4.134422,0.919674],[6.498985,3.341057,-1.265279,-1.992023,9.574945,7.281987,5.669046],[3.993583,-6.926758,0.716123,3.219398,-3.290171,9.420913,-9.861447],[-4.444799,0.529645,1.184283,-4.686640,1.441290,-8.292551,1.463267],[-8.990375,-2.240140,-6.858764,6.310635,6.157522,-3.610073,-9.406330],[5.824199,-4.286420,-9.490049,3.974967,-7.651744,-9.722624,-6.634196],[0.195860,-2.534640,8.790690,0.048285,7.177471,2.713853,1.044875]],[[7.431955,1.153920,-9.199221,-6.428338,1.795818,-7.550459,8.531410],[1.497474,7.377135,2.421536,-0.539857,-1.487600,1.859813,5.691544],[-7.493582,-4.684087,-7.568255,7.747515,2.259852,-9.580060,2.567573],[4.896048,9.129463,5.366894,6.813673,-0.098418,7.108541,9.950644],[-4.096567,9.298852,3.171801,-7.033580,-1.873564,-7.638184,2.526717],[-3.735062,1.982394,1.938094,7.163381,1.767074,-5.047317,-8.444389],[-4.220154,-6.821630,-5.678547,9.417697,3.198565,-7.699817,9.854142],[9.734343,2.883989,-8.207041,1.405149,5.450447,-5.161952,3.786014],[-9.545374,-7.495483,7.430007,1.425384,-8.339568,1.096626,3.891880],[9.062117,-5.107377,1.447701,6.857838,-3.496371,-7.699375,6.832387]],[[-9.995215,8.777691,-3.170131,9.857714,-2.158744,-8.217630,-1.453498],[-9.818624,6.505340,-7.493262,-7.772540,8.238066,6.484959,6.542071],[0.859125,-4.116049,9.849706,-5.118466,8.245342,-1.119823,-1.514584],[2.373306,-9.040653,-8.513805,4.313215,-6.659503,2.304468,2.770889],[7.770912,-9.987079,7.343089,0.370745,-4.189612,4.637944,1.821590],[9.589126,-1.775551,-3.819974,-3.112275,-8.680325,-0.371357,9.205249],[-3.300449,-3.195509,4.159204,-2.628231,-0.526600,-3.234537,4.665057],[-7.345053,3.009269,-4.140253,-7.240980,-9.460452,-1.331318,9.345031],[3.472586,-7.621225,7.848872,-2.262021,6.257222,-6.570027,-0.974822],[-3.437027,-3.231630,-5.841273,-5.347647,1.417982,-5.223864,5.423294]],[[-5.054434,2.357000,9.479056,3.385491,-3.414534,-7.765504,-1.053879],[7.824728,2.383501,-7.043813,7.220453,3.116532,4.990832,-0.744012],[-5.304249,-7.757325,-9.120865,5.519508,9.482608,9.757794,-1.701639],[6.540808,-9.913834,5.953283,-7.052283,4.139408,-7.302394,7.722586],[2.497291,8.883156,8.783495,-2.040670,8.390374,-7.561341,-7.279006],[6.178325,8.054207,8.877697,6.189333,4.209950,-1.423540,8.691713],[1.430607,-3.646393,5.701670,-3.106467,-8.883041,-0.625833,-2.810525],[-9.910467,-6.791820,6.069768,6.963036,4.432877,0.189996,-1.590384],[4.050359,1.440512,9.412099,7.731318,7.011277,6.878611,-9.395500],[-4.891590,-0.281595,8.835229,-1.583728,-7.402255,8.511088,-3.293297]],[[-1.807283,-1.620846,7.933363,-4.136002,-6.780186,2.305719,-6.250762],[2.001994,-5.509446,2.093232,-5.743472,-7.857583,-9.090723,-5.779746],[-5.095816,-1.240940,-9.758006,4.394655,-1.034149,-0.319075,9.372991],[0.285170,-5.398569,5.179213,-7.112534,-1.294312,9.718868,0.804655],[5.121882,-2.954570,-9.921591,2.869683,9.186584,-0.729371,-4.610017],[-0.709443,-9.238814,6.932930,-3.264537,-3.856415,-3.020822,-4.545308],[9.614819,8.894862,9.712911,-1.480932,-5.464625,-1.937190,-4.482329],[-4.475183,4.207690,0.400729,-7.635393,5.364044,5.261641,7.553269],[-7.423464,7.721023,1.281770,-7.322551,-9.385287,-4.534342,-3.878472],[9.713111,-9.752911,-9.645434,-0.414625,3.069728,-8.438293,-6.062228]],[[-1.198493,4.754638,7.711427,-2.927350,8.044178,4.496461,-8.864886],[6.557981,4.679195,1.954268,-1.804454,1.541879,2.125742,9.786913],[3.798927,0.072855,2.988203,-3.754801,-2.302079,2.615803,-7.414604],[7.222257,-6.542611,0.581731,4.751422,1.484794,-5.331216,5.449762],[-1.146041,-1.502987,-9.336345,0.959895,-6.691363,-0.436563,8.764277],[3.326884,-5.614986,-6.926966,5.150558,-7.951857,-8.867425,-2.189928],[4.002843,1.346543,-7.948669,7.486820,7.144506,-8.871380,2.747863],[-0.820068,-8.096330,-9.273002,1.748321,8.046382,-0.860929,8.748043],[-6.998332,-3.636953,9.611847,7.297565,6.037910,-2.153686,9.511033],[-4.939206,6.616715,4.203423,-9.624382,7.729703,-1.551063,-7.372141]],[[-5.895564,-3.168079,9.509916,-2.019661,-4.659312,-5.408646,2.234921],[-5.894838,6.486655,9.683024,-7.385715,-0.063503,-2.937247,-8.392585],[7.532044,2.292190,-2.989356,-0.845485,-0.281630,5.591454,-9.112080],[-2.670539,-8.894606,-1.043840,-5.557381,7.583816,0.465954,6.964131],[1.536570,-1.006860,8.751611,-1.693817,9.849282,0.281422,-4.409709],[-5.112241,4.539596,-7.554689,-8.459206,9.131494,-1.529518,1.653610],[9.081672,4.870527,-0.922303,2.391974,4.296972,5.844258,-4.708643],[2.494526,1.373807,8.397769,-2.489954,1.122815,-9.300209,5.976581],[8.571083,-4.629120,-1.479562,4.972551,-6.599719,-4.362945,-5.704689],[-2.772804,-4.110055,1.623469,-8.779559,-9.721799,-6.112562,0.273918]],[[4.528000,5.897089,2.793140,4.781506,3.190507,-3.256627,2.007484],[-0.756433,-4.224442,-2.971613,-3.262964,3.159290,-6.933759,6.700740],[4.816187,9.385677,-5.525888,3.924362,4.205144,5.347064,2.432447],[-6.452406,-8.896674,-3.134827,9.625242,0.543587,7.814455,-6.217149],[1.067734,-4.011995,-3.571199,9.091699,7.161777,-6.498929,1.314461],[3.902480,1.034199,9.953194,-8.935798,3.456090,-3.373699,6.810744],[0.877389,4.715322,-8.052929,4.749059,3.480672,5.716842,5.865406],[4.052463,2.900062,3.230731,-0.026877,-6.393054,-8.605238,3.813416],[-4.355398,-6.901020,-2.087945,-5.209578,-8.509813,-1.568234,-6.891309],[-7.221010,9.042152,-5.819920,-3.837568,-0.030715,-5.045298,-3.403088]]], dtype = "float64")#candidate|2552|(14, 10, 7)|const|float64
bop_2553 = relay.greater_equal(call_2542.astype('bool'), relay.reshape(const_2552.astype('bool'), relay.shape_of(call_2542))) # shape=(14, 10, 7)
bop_2556 = relay.greater_equal(call_2543.astype('bool'), relay.reshape(const_2552.astype('bool'), relay.shape_of(call_2543))) # shape=(14, 10, 7)
output = relay.Tuple([call_2545,const_2546,bop_2553,])
output2 = relay.Tuple([call_2547,const_2546,bop_2556,])
func_2575 = relay.Function([], output)
mod['func_2575'] = func_2575
mod = relay.transform.InferType()(mod)
mutated_mod['func_2575'] = func_2575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2575_call = mutated_mod.get_global_var('func_2575')
call_2576 = func_2575_call()
output = call_2576
func_2577 = relay.Function([], output)
mutated_mod['func_2577'] = func_2577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1979_call = mod.get_global_var('func_1979')
func_1981_call = mutated_mod.get_global_var('func_1981')
call_2578 = func_1979_call()
call_2579 = func_1979_call()
output = relay.Tuple([call_2578,])
output2 = relay.Tuple([call_2579,])
func_2602 = relay.Function([], output)
mod['func_2602'] = func_2602
mod = relay.transform.InferType()(mod)
output = func_2602()
func_2603 = relay.Function([], output)
mutated_mod['func_2603'] = func_2603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_2614 = relay.TupleGetItem(func_859_call(), 4)
call_2615 = relay.TupleGetItem(func_860_call(), 4)
func_311_call = mod.get_global_var('func_311')
func_313_call = mutated_mod.get_global_var('func_313')
call_2616 = relay.TupleGetItem(func_311_call(), 1)
call_2617 = relay.TupleGetItem(func_313_call(), 1)
func_1103_call = mod.get_global_var('func_1103')
func_1104_call = mutated_mod.get_global_var('func_1104')
call_2638 = func_1103_call()
call_2639 = func_1103_call()
func_1219_call = mod.get_global_var('func_1219')
func_1220_call = mutated_mod.get_global_var('func_1220')
call_2645 = relay.TupleGetItem(func_1219_call(), 0)
call_2646 = relay.TupleGetItem(func_1220_call(), 0)
bop_2649 = relay.minimum(call_2616.astype('uint64'), relay.reshape(call_2645.astype('uint64'), relay.shape_of(call_2616))) # shape=(14, 10, 7)
bop_2652 = relay.minimum(call_2617.astype('uint64'), relay.reshape(call_2646.astype('uint64'), relay.shape_of(call_2617))) # shape=(14, 10, 7)
output = relay.Tuple([call_2614,call_2638,bop_2649,])
output2 = relay.Tuple([call_2615,call_2639,bop_2652,])
func_2653 = relay.Function([], output)
mod['func_2653'] = func_2653
mod = relay.transform.InferType()(mod)
mutated_mod['func_2653'] = func_2653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2653_call = mutated_mod.get_global_var('func_2653')
call_2654 = func_2653_call()
output = call_2654
func_2655 = relay.Function([], output)
mutated_mod['func_2655'] = func_2655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_2688 = relay.TupleGetItem(func_859_call(), 3)
call_2689 = relay.TupleGetItem(func_860_call(), 3)
var_2699 = relay.var("var_2699", dtype = "float32", shape = (14, 10, 7))#candidate|2699|(14, 10, 7)|var|float32
bop_2700 = relay.multiply(call_2688.astype('int64'), relay.reshape(var_2699.astype('int64'), relay.shape_of(call_2688))) # shape=(14, 10, 7)
bop_2703 = relay.multiply(call_2689.astype('int64'), relay.reshape(var_2699.astype('int64'), relay.shape_of(call_2689))) # shape=(14, 10, 7)
func_2326_call = mod.get_global_var('func_2326')
func_2327_call = mutated_mod.get_global_var('func_2327')
call_2707 = relay.TupleGetItem(func_2326_call(), 0)
call_2708 = relay.TupleGetItem(func_2327_call(), 0)
func_2260_call = mod.get_global_var('func_2260')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_2716 = func_2260_call()
call_2717 = func_2260_call()
func_2190_call = mod.get_global_var('func_2190')
func_2193_call = mutated_mod.get_global_var('func_2193')
var_2725 = relay.var("var_2725", dtype = "float64", shape = (80,))#candidate|2725|(80,)|var|float64
call_2724 = relay.TupleGetItem(func_2190_call(relay.reshape(var_2725.astype('float64'), [80,])), 1)
call_2726 = relay.TupleGetItem(func_2193_call(relay.reshape(var_2725.astype('float64'), [80,])), 1)
bop_2741 = relay.add(call_2724.astype('int32'), relay.reshape(call_2707.astype('int32'), relay.shape_of(call_2724))) # shape=(14, 10, 7)
bop_2744 = relay.add(call_2726.astype('int32'), relay.reshape(call_2708.astype('int32'), relay.shape_of(call_2726))) # shape=(14, 10, 7)
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_2746 = relay.TupleGetItem(func_1822_call(), 0)
call_2747 = relay.TupleGetItem(func_1824_call(), 0)
func_2575_call = mod.get_global_var('func_2575')
func_2577_call = mutated_mod.get_global_var('func_2577')
call_2760 = relay.TupleGetItem(func_2575_call(), 2)
call_2761 = relay.TupleGetItem(func_2577_call(), 2)
output = relay.Tuple([bop_2700,call_2716,var_2725,bop_2741,call_2746,call_2760,])
output2 = relay.Tuple([bop_2703,call_2717,var_2725,bop_2744,call_2747,call_2761,])
func_2765 = relay.Function([var_2699,var_2725,], output)
mod['func_2765'] = func_2765
mod = relay.transform.InferType()(mod)
mutated_mod['func_2765'] = func_2765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mutated_mod.get_global_var('func_2765')
var_2767 = relay.var("var_2767", dtype = "float32", shape = (14, 10, 7))#candidate|2767|(14, 10, 7)|var|float32
var_2768 = relay.var("var_2768", dtype = "float64", shape = (80,))#candidate|2768|(80,)|var|float64
call_2766 = func_2765_call(var_2767,var_2768,)
output = call_2766
func_2769 = relay.Function([var_2767,var_2768,], output)
mutated_mod['func_2769'] = func_2769
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2803 = relay.var("var_2803", dtype = "float64", shape = ())#candidate|2803|()|var|float64
var_2804 = relay.var("var_2804", dtype = "float64", shape = (13, 15, 16))#candidate|2804|(13, 15, 16)|var|float64
bop_2805 = relay.mod(var_2803.astype('float64'), var_2804.astype('float64')) # shape=(13, 15, 16)
output = relay.Tuple([bop_2805,])
output2 = relay.Tuple([bop_2805,])
func_2810 = relay.Function([var_2803,var_2804,], output)
mod['func_2810'] = func_2810
mod = relay.transform.InferType()(mod)
var_2811 = relay.var("var_2811", dtype = "float64", shape = ())#candidate|2811|()|var|float64
var_2812 = relay.var("var_2812", dtype = "float64", shape = (13, 15, 16))#candidate|2812|(13, 15, 16)|var|float64
output = func_2810(var_2811,var_2812,)
func_2813 = relay.Function([var_2811,var_2812,], output)
mutated_mod['func_2813'] = func_2813
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2815 = relay.const([[[-3.284805,0.527002,-6.795238,4.973537,4.889337,0.318790,-5.580648,-8.043157],[-2.565847,6.831024,-0.081665,-4.641310,0.264209,-7.778675,-7.839537,-4.317222],[8.881055,9.736948,9.432086,3.068227,7.486678,-2.005238,-1.800088,-5.162547],[-2.260689,-2.774695,8.253189,-7.568087,-8.163486,3.929653,-6.508179,3.610190],[4.512325,0.039953,7.352155,2.854262,-3.314883,9.603877,-0.634826,3.302151],[2.158946,-7.032176,9.960152,2.590316,8.943428,-2.394821,-0.240084,1.542941],[-1.564433,-7.659835,-9.185524,-6.296826,-3.260906,2.250990,8.488145,5.436271],[3.972020,-2.182157,-0.276386,-2.446693,-1.599273,3.890578,-9.830978,-6.294215],[-5.762384,9.641601,-6.229228,4.919730,3.127555,-7.405362,5.430863,1.081803],[0.624218,7.529972,-3.116458,0.629690,-6.421304,7.198887,-9.541269,-0.593459],[6.090701,8.307704,8.266206,-8.628491,0.670914,-5.964756,-2.353854,6.223285],[2.805777,-7.711828,-0.585117,-4.997568,-0.020631,-0.512236,1.145623,2.032772]],[[-2.514989,-6.233469,6.665635,-0.952419,6.135016,-3.667220,-8.374724,2.927924],[-1.435668,4.352814,-2.972951,-7.570775,-5.427381,8.530846,3.837680,-4.812330],[9.454545,5.211147,3.106275,4.342381,-9.696839,-9.671516,-2.342198,-0.831646],[9.570959,9.659000,8.703645,5.172941,-5.795770,0.985293,5.536571,2.258806],[1.055165,-0.604434,-6.458455,6.518389,1.736189,-6.384683,-0.796602,-6.635069],[-4.305791,2.653851,9.609398,3.225459,8.896542,3.320680,-3.691489,1.805234],[-3.585215,-7.456882,6.479999,6.171797,-2.133927,-9.554523,5.771953,-1.086231],[2.525531,7.816212,-1.370731,-6.820596,-5.792542,6.426742,3.244502,-8.747835],[-8.191075,-6.269272,-9.176559,-5.132191,5.585830,6.625429,9.786760,5.850639],[5.161243,-8.067373,1.208848,9.972039,-2.411097,9.795289,7.942003,9.997212],[-9.570726,-4.873069,-5.376624,6.918944,5.696578,-5.505853,1.897625,1.511081],[-2.573263,-5.454729,1.533332,0.687570,-1.578352,2.833274,-9.010215,2.588450]]], dtype = "float64")#candidate|2815|(2, 12, 8)|const|float64
var_2816 = relay.var("var_2816", dtype = "float64", shape = (2, 12, 8))#candidate|2816|(2, 12, 8)|var|float64
bop_2817 = relay.mod(const_2815.astype('float64'), relay.reshape(var_2816.astype('float64'), relay.shape_of(const_2815))) # shape=(2, 12, 8)
func_2575_call = mod.get_global_var('func_2575')
func_2577_call = mutated_mod.get_global_var('func_2577')
call_2821 = relay.TupleGetItem(func_2575_call(), 1)
call_2822 = relay.TupleGetItem(func_2577_call(), 1)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_2840 = relay.TupleGetItem(func_859_call(), 3)
call_2841 = relay.TupleGetItem(func_860_call(), 3)
uop_2843 = relay.erf(var_2816.astype('float32')) # shape=(2, 12, 8)
func_2765_call = mod.get_global_var('func_2765')
func_2769_call = mutated_mod.get_global_var('func_2769')
var_2848 = relay.var("var_2848", dtype = "float64", shape = (80,))#candidate|2848|(80,)|var|float64
call_2847 = relay.TupleGetItem(func_2765_call(relay.reshape(call_2840.astype('float32'), [14, 10, 7]), relay.reshape(var_2848.astype('float64'), [80,]), ), 0)
call_2849 = relay.TupleGetItem(func_2769_call(relay.reshape(call_2840.astype('float32'), [14, 10, 7]), relay.reshape(var_2848.astype('float64'), [80,]), ), 0)
output = relay.Tuple([bop_2817,call_2821,call_2840,uop_2843,call_2847,var_2848,])
output2 = relay.Tuple([bop_2817,call_2822,call_2841,uop_2843,call_2849,var_2848,])
func_2856 = relay.Function([var_2816,var_2848,], output)
mod['func_2856'] = func_2856
mod = relay.transform.InferType()(mod)
var_2857 = relay.var("var_2857", dtype = "float64", shape = (2, 12, 8))#candidate|2857|(2, 12, 8)|var|float64
var_2858 = relay.var("var_2858", dtype = "float64", shape = (80,))#candidate|2858|(80,)|var|float64
output = func_2856(var_2857,var_2858,)
func_2859 = relay.Function([var_2857,var_2858,], output)
mutated_mod['func_2859'] = func_2859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2470_call = mod.get_global_var('func_2470')
func_2471_call = mutated_mod.get_global_var('func_2471')
call_2913 = func_2470_call()
call_2914 = func_2470_call()
output = relay.Tuple([call_2913,])
output2 = relay.Tuple([call_2914,])
func_2918 = relay.Function([], output)
mod['func_2918'] = func_2918
mod = relay.transform.InferType()(mod)
output = func_2918()
func_2919 = relay.Function([], output)
mutated_mod['func_2919'] = func_2919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1219_call = mod.get_global_var('func_1219')
func_1220_call = mutated_mod.get_global_var('func_1220')
call_2938 = relay.TupleGetItem(func_1219_call(), 2)
call_2939 = relay.TupleGetItem(func_1220_call(), 2)
output = call_2938
output2 = call_2939
func_2949 = relay.Function([], output)
mod['func_2949'] = func_2949
mod = relay.transform.InferType()(mod)
mutated_mod['func_2949'] = func_2949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mutated_mod.get_global_var('func_2949')
call_2950 = func_2949_call()
output = call_2950
func_2951 = relay.Function([], output)
mutated_mod['func_2951'] = func_2951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1103_call = mod.get_global_var('func_1103')
func_1104_call = mutated_mod.get_global_var('func_1104')
call_2957 = func_1103_call()
call_2958 = func_1103_call()
output = relay.Tuple([call_2957,])
output2 = relay.Tuple([call_2958,])
func_2986 = relay.Function([], output)
mod['func_2986'] = func_2986
mod = relay.transform.InferType()(mod)
output = func_2986()
func_2987 = relay.Function([], output)
mutated_mod['func_2987'] = func_2987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_2991 = relay.TupleGetItem(func_2009_call(), 1)
call_2992 = relay.TupleGetItem(func_2011_call(), 1)
func_1422_call = mod.get_global_var('func_1422')
func_1423_call = mutated_mod.get_global_var('func_1423')
call_3017 = relay.TupleGetItem(func_1422_call(), 0)
call_3018 = relay.TupleGetItem(func_1423_call(), 0)
output = relay.Tuple([call_2991,call_3017,])
output2 = relay.Tuple([call_2992,call_3018,])
func_3028 = relay.Function([], output)
mod['func_3028'] = func_3028
mod = relay.transform.InferType()(mod)
mutated_mod['func_3028'] = func_3028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3028_call = mutated_mod.get_global_var('func_3028')
call_3029 = func_3028_call()
output = call_3029
func_3030 = relay.Function([], output)
mutated_mod['func_3030'] = func_3030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mod.get_global_var('func_2260')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_3052 = func_2260_call()
call_3053 = func_2260_call()
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_3058 = relay.TupleGetItem(func_1112_call(), 0)
call_3059 = relay.TupleGetItem(func_1113_call(), 0)
func_497_call = mod.get_global_var('func_497')
func_499_call = mutated_mod.get_global_var('func_499')
call_3062 = relay.TupleGetItem(func_497_call(), 0)
call_3063 = relay.TupleGetItem(func_499_call(), 0)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
const_3077 = relay.const([[9.734874],[8.411204],[7.519082],[-0.578612],[1.666075],[-2.193686],[-1.909923],[-5.350253],[7.210991],[6.069492],[5.999805],[-3.576800],[9.926683],[-8.294732],[-7.292866],[5.515360],[3.337213],[-2.785383],[4.718089],[7.990871],[-8.040504],[3.145567],[0.557147],[4.417591],[-9.788091],[1.810882],[0.019389],[-5.189375],[-4.428508],[-7.769863],[9.921075],[-6.301706],[-6.595937],[4.831334],[5.246958],[-5.188535],[-9.602357],[2.646117],[0.395682],[5.044578],[7.961414],[-9.484466],[-5.548120],[1.437696],[5.194659],[-6.402992],[4.308612],[5.516168],[0.836915],[-5.752359],[7.361873],[9.032489],[-2.311227],[-8.432018],[7.985768],[-4.824218],[-0.038888],[1.863237],[7.573478],[9.875936],[-6.088796],[4.129368],[7.894458],[7.586979],[2.108996],[1.179005],[-0.144390],[4.312908],[1.900566],[-5.189575],[7.462842],[8.543353],[2.572083],[-6.695015],[-2.260551],[4.316400],[9.192755],[-5.254329],[-8.690743],[-9.984179]], dtype = "float64")#candidate|3077|(80, 1)|const|float64
call_3076 = relay.TupleGetItem(func_1319_call(relay.reshape(call_3062.astype('float64'), [14, 10, 7]), relay.reshape(const_3077.astype('float64'), [80, 1]), ), 6)
call_3078 = relay.TupleGetItem(func_1322_call(relay.reshape(call_3062.astype('float64'), [14, 10, 7]), relay.reshape(const_3077.astype('float64'), [80, 1]), ), 6)
func_2810_call = mod.get_global_var('func_2810')
func_2813_call = mutated_mod.get_global_var('func_2813')
var_3095 = relay.var("var_3095", dtype = "float64", shape = ())#candidate|3095|()|var|float64
var_3096 = relay.var("var_3096", dtype = "float64", shape = (3120,))#candidate|3096|(3120,)|var|float64
call_3094 = relay.TupleGetItem(func_2810_call(relay.reshape(var_3095.astype('float64'), []), relay.reshape(var_3096.astype('float64'), [13, 15, 16]), ), 0)
call_3097 = relay.TupleGetItem(func_2813_call(relay.reshape(var_3095.astype('float64'), []), relay.reshape(var_3096.astype('float64'), [13, 15, 16]), ), 0)
output = relay.Tuple([call_3052,call_3058,call_3062,call_3076,const_3077,call_3094,var_3095,var_3096,])
output2 = relay.Tuple([call_3053,call_3059,call_3063,call_3078,const_3077,call_3097,var_3095,var_3096,])
func_3106 = relay.Function([var_3095,var_3096,], output)
mod['func_3106'] = func_3106
mod = relay.transform.InferType()(mod)
var_3107 = relay.var("var_3107", dtype = "float64", shape = ())#candidate|3107|()|var|float64
var_3108 = relay.var("var_3108", dtype = "float64", shape = (3120,))#candidate|3108|(3120,)|var|float64
output = func_3106(var_3107,var_3108,)
func_3109 = relay.Function([var_3107,var_3108,], output)
mutated_mod['func_3109'] = func_3109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1219_call = mod.get_global_var('func_1219')
func_1220_call = mutated_mod.get_global_var('func_1220')
call_3191 = relay.TupleGetItem(func_1219_call(), 2)
call_3192 = relay.TupleGetItem(func_1220_call(), 2)
output = call_3191
output2 = call_3192
func_3199 = relay.Function([], output)
mod['func_3199'] = func_3199
mod = relay.transform.InferType()(mod)
mutated_mod['func_3199'] = func_3199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3199_call = mutated_mod.get_global_var('func_3199')
call_3200 = func_3199_call()
output = call_3200
func_3201 = relay.Function([], output)
mutated_mod['func_3201'] = func_3201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3199_call = mod.get_global_var('func_3199')
func_3201_call = mutated_mod.get_global_var('func_3201')
call_3202 = func_3199_call()
call_3203 = func_3199_call()
func_1090_call = mod.get_global_var('func_1090')
func_1093_call = mutated_mod.get_global_var('func_1093')
var_3218 = relay.var("var_3218", dtype = "float64", shape = ())#candidate|3218|()|var|float64
const_3219 = relay.const([-2.636377,9.592452,5.322980,5.211936,4.820931,1.916597,-5.040567,-5.367221,4.978456,-8.248853,9.742393,9.401017,0.391936,-3.391078,-1.963149,-8.582730,-1.339718,-1.014140,3.547825,-6.498873,5.669423,0.335476,5.756179,9.442006,4.894863,-2.850225,-3.067660,-2.628229,5.891935,-5.693796,-5.383838,-7.392954,-9.692602,-9.833284,-7.110899,9.767698,-3.490210,-3.883540,-8.440535,-9.269159,9.289180,-3.385279,8.865623,3.671588,-8.895899,-6.223919,7.852117,3.921332,9.844716,4.394066,-2.136835,6.358736,-9.334631,-9.549695,4.243017,-2.719973,9.362114,-8.703826,1.722288,0.913199,7.046248,-8.055611,2.804644,0.014394,2.793623,-8.965924,1.228127,-0.753788,2.964009,-9.162930,-3.510325,-3.424688,5.610126,-6.641203,-3.174054,-4.082197,8.256467,-6.725759,-6.052584,7.838469], dtype = "float64")#candidate|3219|(80,)|const|float64
call_3217 = func_1090_call(relay.reshape(var_3218.astype('float64'), []), relay.reshape(const_3219.astype('float64'), [1, 16, 5]), )
call_3220 = func_1090_call(relay.reshape(var_3218.astype('float64'), []), relay.reshape(const_3219.astype('float64'), [1, 16, 5]), )
func_3199_call = mod.get_global_var('func_3199')
func_3201_call = mutated_mod.get_global_var('func_3201')
call_3224 = func_3199_call()
call_3225 = func_3199_call()
output = relay.Tuple([call_3202,call_3217,var_3218,const_3219,call_3224,])
output2 = relay.Tuple([call_3203,call_3220,var_3218,const_3219,call_3225,])
func_3226 = relay.Function([var_3218,], output)
mod['func_3226'] = func_3226
mod = relay.transform.InferType()(mod)
mutated_mod['func_3226'] = func_3226
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3227 = relay.var("var_3227", dtype = "float64", shape = ())#candidate|3227|()|var|float64
func_3226_call = mutated_mod.get_global_var('func_3226')
call_3228 = func_3226_call(var_3227)
output = call_3228
func_3229 = relay.Function([var_3227], output)
mutated_mod['func_3229'] = func_3229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_3259 = relay.TupleGetItem(func_2009_call(), 1)
call_3260 = relay.TupleGetItem(func_2011_call(), 1)
output = call_3259
output2 = call_3260
func_3264 = relay.Function([], output)
mod['func_3264'] = func_3264
mod = relay.transform.InferType()(mod)
mutated_mod['func_3264'] = func_3264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3264_call = mutated_mod.get_global_var('func_3264')
call_3265 = func_3264_call()
output = call_3265
func_3266 = relay.Function([], output)
mutated_mod['func_3266'] = func_3266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
call_3330 = relay.TupleGetItem(func_759_call(), 1)
call_3331 = relay.TupleGetItem(func_761_call(), 1)
func_2986_call = mod.get_global_var('func_2986')
func_2987_call = mutated_mod.get_global_var('func_2987')
call_3337 = relay.TupleGetItem(func_2986_call(), 0)
call_3338 = relay.TupleGetItem(func_2987_call(), 0)
output = relay.Tuple([call_3330,call_3337,])
output2 = relay.Tuple([call_3331,call_3338,])
func_3349 = relay.Function([], output)
mod['func_3349'] = func_3349
mod = relay.transform.InferType()(mod)
mutated_mod['func_3349'] = func_3349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3349_call = mutated_mod.get_global_var('func_3349')
call_3350 = func_3349_call()
output = call_3350
func_3351 = relay.Function([], output)
mutated_mod['func_3351'] = func_3351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_3402 = relay.TupleGetItem(func_223_call(), 0)
call_3403 = relay.TupleGetItem(func_224_call(), 0)
output = call_3402
output2 = call_3403
func_3404 = relay.Function([], output)
mod['func_3404'] = func_3404
mod = relay.transform.InferType()(mod)
mutated_mod['func_3404'] = func_3404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3404_call = mutated_mod.get_global_var('func_3404')
call_3405 = func_3404_call()
output = call_3405
func_3406 = relay.Function([], output)
mutated_mod['func_3406'] = func_3406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_3433 = relay.TupleGetItem(func_223_call(), 0)
call_3434 = relay.TupleGetItem(func_224_call(), 0)
output = relay.Tuple([call_3433,])
output2 = relay.Tuple([call_3434,])
func_3443 = relay.Function([], output)
mod['func_3443'] = func_3443
mod = relay.transform.InferType()(mod)
mutated_mod['func_3443'] = func_3443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3443_call = mutated_mod.get_global_var('func_3443')
call_3444 = func_3443_call()
output = call_3444
func_3445 = relay.Function([], output)
mutated_mod['func_3445'] = func_3445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1103_call = mod.get_global_var('func_1103')
func_1104_call = mutated_mod.get_global_var('func_1104')
call_3452 = func_1103_call()
call_3453 = func_1103_call()
output = call_3452
output2 = call_3453
func_3487 = relay.Function([], output)
mod['func_3487'] = func_3487
mod = relay.transform.InferType()(mod)
output = func_3487()
func_3488 = relay.Function([], output)
mutated_mod['func_3488'] = func_3488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2326_call = mod.get_global_var('func_2326')
func_2327_call = mutated_mod.get_global_var('func_2327')
call_3519 = relay.TupleGetItem(func_2326_call(), 0)
call_3520 = relay.TupleGetItem(func_2327_call(), 0)
func_2260_call = mod.get_global_var('func_2260')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_3528 = func_2260_call()
call_3529 = func_2260_call()
output = relay.Tuple([call_3519,call_3528,])
output2 = relay.Tuple([call_3520,call_3529,])
func_3544 = relay.Function([], output)
mod['func_3544'] = func_3544
mod = relay.transform.InferType()(mod)
mutated_mod['func_3544'] = func_3544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3544_call = mutated_mod.get_global_var('func_3544')
call_3545 = func_3544_call()
output = call_3545
func_3546 = relay.Function([], output)
mutated_mod['func_3546'] = func_3546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2986_call = mod.get_global_var('func_2986')
func_2987_call = mutated_mod.get_global_var('func_2987')
call_3589 = relay.TupleGetItem(func_2986_call(), 0)
call_3590 = relay.TupleGetItem(func_2987_call(), 0)
output = relay.Tuple([call_3589,])
output2 = relay.Tuple([call_3590,])
func_3593 = relay.Function([], output)
mod['func_3593'] = func_3593
mod = relay.transform.InferType()(mod)
mutated_mod['func_3593'] = func_3593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3593_call = mutated_mod.get_global_var('func_3593')
call_3594 = func_3593_call()
output = call_3594
func_3595 = relay.Function([], output)
mutated_mod['func_3595'] = func_3595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1200_call = mod.get_global_var('func_1200')
func_1201_call = mutated_mod.get_global_var('func_1201')
call_3613 = relay.TupleGetItem(func_1200_call(), 0)
call_3614 = relay.TupleGetItem(func_1201_call(), 0)
output = relay.Tuple([call_3613,])
output2 = relay.Tuple([call_3614,])
func_3642 = relay.Function([], output)
mod['func_3642'] = func_3642
mod = relay.transform.InferType()(mod)
output = func_3642()
func_3643 = relay.Function([], output)
mutated_mod['func_3643'] = func_3643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3349_call = mod.get_global_var('func_3349')
func_3351_call = mutated_mod.get_global_var('func_3351')
call_3667 = relay.TupleGetItem(func_3349_call(), 1)
call_3668 = relay.TupleGetItem(func_3351_call(), 1)
output = relay.Tuple([call_3667,])
output2 = relay.Tuple([call_3668,])
func_3674 = relay.Function([], output)
mod['func_3674'] = func_3674
mod = relay.transform.InferType()(mod)
mutated_mod['func_3674'] = func_3674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3674_call = mutated_mod.get_global_var('func_3674')
call_3675 = func_3674_call()
output = call_3675
func_3676 = relay.Function([], output)
mutated_mod['func_3676'] = func_3676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3700 = relay.var("var_3700", dtype = "float64", shape = (4, 14, 1))#candidate|3700|(4, 14, 1)|var|float64
uop_3701 = relay.log10(var_3700.astype('float64')) # shape=(4, 14, 1)
func_3226_call = mod.get_global_var('func_3226')
func_3229_call = mutated_mod.get_global_var('func_3229')
const_3708 = relay.const(1.391896, dtype = "float64")#candidate|3708|()|const|float64
call_3707 = relay.TupleGetItem(func_3226_call(relay.reshape(const_3708.astype('float64'), [])), 1)
call_3709 = relay.TupleGetItem(func_3229_call(relay.reshape(const_3708.astype('float64'), [])), 1)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_3713 = relay.TupleGetItem(func_859_call(), 2)
call_3714 = relay.TupleGetItem(func_860_call(), 2)
func_2121_call = mod.get_global_var('func_2121')
func_2123_call = mutated_mod.get_global_var('func_2123')
call_3715 = relay.TupleGetItem(func_2121_call(), 7)
call_3716 = relay.TupleGetItem(func_2123_call(), 7)
bop_3717 = relay.less_equal(uop_3701.astype('bool'), const_3708.astype('bool')) # shape=(4, 14, 1)
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
call_3726 = relay.TupleGetItem(func_463_call(relay.reshape(call_3715.astype('float32'), [14, 10, 7])), 1)
call_3727 = relay.TupleGetItem(func_466_call(relay.reshape(call_3715.astype('float32'), [14, 10, 7])), 1)
uop_3741 = relay.asin(bop_3717.astype('float32')) # shape=(4, 14, 1)
func_2190_call = mod.get_global_var('func_2190')
func_2193_call = mutated_mod.get_global_var('func_2193')
call_3747 = relay.TupleGetItem(func_2190_call(relay.reshape(call_3707.astype('float64'), [80,])), 3)
call_3748 = relay.TupleGetItem(func_2193_call(relay.reshape(call_3707.astype('float64'), [80,])), 3)
func_2986_call = mod.get_global_var('func_2986')
func_2987_call = mutated_mod.get_global_var('func_2987')
call_3755 = relay.TupleGetItem(func_2986_call(), 0)
call_3756 = relay.TupleGetItem(func_2987_call(), 0)
func_3106_call = mod.get_global_var('func_3106')
func_3109_call = mutated_mod.get_global_var('func_3109')
var_3770 = relay.var("var_3770", dtype = "float64", shape = (1, 3120))#candidate|3770|(1, 3120)|var|float64
call_3769 = relay.TupleGetItem(func_3106_call(relay.reshape(const_3708.astype('float64'), []), relay.reshape(var_3770.astype('float64'), [3120,]), ), 7)
call_3771 = relay.TupleGetItem(func_3109_call(relay.reshape(const_3708.astype('float64'), []), relay.reshape(var_3770.astype('float64'), [3120,]), ), 7)
uop_3773 = relay.sinh(uop_3701.astype('float32')) # shape=(4, 14, 1)
func_1483_call = mod.get_global_var('func_1483')
func_1487_call = mutated_mod.get_global_var('func_1487')
var_3776 = relay.var("var_3776", dtype = "bool", shape = (330,))#candidate|3776|(330,)|var|bool
call_3775 = relay.TupleGetItem(func_1483_call(relay.reshape(var_3776.astype('bool'), [2, 11, 15]), relay.reshape(call_3755.astype('float32'), [980,]), ), 0)
call_3777 = relay.TupleGetItem(func_1487_call(relay.reshape(var_3776.astype('bool'), [2, 11, 15]), relay.reshape(call_3755.astype('float32'), [980,]), ), 0)
bop_3782 = relay.minimum(uop_3773.astype('int64'), call_3769.astype('int64')) # shape=(4, 14, 3120)
bop_3785 = relay.minimum(uop_3773.astype('int64'), call_3771.astype('int64')) # shape=(4, 14, 3120)
var_3786 = relay.var("var_3786", dtype = "float32", shape = (4, 14, 9))#candidate|3786|(4, 14, 9)|var|float32
bop_3787 = relay.left_shift(uop_3741.astype('uint8'), var_3786.astype('uint8')) # shape=(4, 14, 9)
output = relay.Tuple([call_3707,call_3713,call_3715,call_3726,call_3747,call_3755,var_3770,call_3775,var_3776,bop_3782,bop_3787,])
output2 = relay.Tuple([call_3709,call_3714,call_3716,call_3727,call_3748,call_3756,var_3770,call_3777,var_3776,bop_3785,bop_3787,])
func_3796 = relay.Function([var_3700,var_3770,var_3776,var_3786,], output)
mod['func_3796'] = func_3796
mod = relay.transform.InferType()(mod)
var_3797 = relay.var("var_3797", dtype = "float64", shape = (4, 14, 1))#candidate|3797|(4, 14, 1)|var|float64
var_3798 = relay.var("var_3798", dtype = "float64", shape = (1, 3120))#candidate|3798|(1, 3120)|var|float64
var_3799 = relay.var("var_3799", dtype = "bool", shape = (330,))#candidate|3799|(330,)|var|bool
var_3800 = relay.var("var_3800", dtype = "float32", shape = (4, 14, 9))#candidate|3800|(4, 14, 9)|var|float32
output = func_3796(var_3797,var_3798,var_3799,var_3800,)
func_3801 = relay.Function([var_3797,var_3798,var_3799,var_3800,], output)
mutated_mod['func_3801'] = func_3801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3404_call = mod.get_global_var('func_3404')
func_3406_call = mutated_mod.get_global_var('func_3406')
call_3813 = func_3404_call()
call_3814 = func_3404_call()
output = call_3813
output2 = call_3814
func_3815 = relay.Function([], output)
mod['func_3815'] = func_3815
mod = relay.transform.InferType()(mod)
mutated_mod['func_3815'] = func_3815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3815_call = mutated_mod.get_global_var('func_3815')
call_3816 = func_3815_call()
output = call_3816
func_3817 = relay.Function([], output)
mutated_mod['func_3817'] = func_3817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_3865 = relay.TupleGetItem(func_75_call(), 0)
call_3866 = relay.TupleGetItem(func_76_call(), 0)
func_2918_call = mod.get_global_var('func_2918')
func_2919_call = mutated_mod.get_global_var('func_2919')
call_3876 = relay.TupleGetItem(func_2918_call(), 0)
call_3877 = relay.TupleGetItem(func_2919_call(), 0)
func_3404_call = mod.get_global_var('func_3404')
func_3406_call = mutated_mod.get_global_var('func_3406')
call_3878 = func_3404_call()
call_3879 = func_3404_call()
func_2986_call = mod.get_global_var('func_2986')
func_2987_call = mutated_mod.get_global_var('func_2987')
call_3883 = relay.TupleGetItem(func_2986_call(), 0)
call_3884 = relay.TupleGetItem(func_2987_call(), 0)
bop_3902 = relay.greater(call_3876.astype('bool'), relay.reshape(call_3878.astype('bool'), relay.shape_of(call_3876))) # shape=(14, 10, 7)
bop_3905 = relay.greater(call_3877.astype('bool'), relay.reshape(call_3879.astype('bool'), relay.shape_of(call_3877))) # shape=(14, 10, 7)
func_3487_call = mod.get_global_var('func_3487')
func_3488_call = mutated_mod.get_global_var('func_3488')
call_3910 = func_3487_call()
call_3911 = func_3487_call()
output = relay.Tuple([call_3865,call_3883,bop_3902,call_3910,])
output2 = relay.Tuple([call_3866,call_3884,bop_3905,call_3911,])
func_3917 = relay.Function([], output)
mod['func_3917'] = func_3917
mod = relay.transform.InferType()(mod)
output = func_3917()
func_3918 = relay.Function([], output)
mutated_mod['func_3918'] = func_3918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_3924 = relay.TupleGetItem(func_376_call(), 0)
call_3925 = relay.TupleGetItem(func_377_call(), 0)
func_2470_call = mod.get_global_var('func_2470')
func_2471_call = mutated_mod.get_global_var('func_2471')
call_3932 = func_2470_call()
call_3933 = func_2470_call()
func_3796_call = mod.get_global_var('func_3796')
func_3801_call = mutated_mod.get_global_var('func_3801')
var_3950 = relay.var("var_3950", dtype = "float64", shape = (56, 1))#candidate|3950|(56, 1)|var|float64
var_3951 = relay.var("var_3951", dtype = "float64", shape = (3120,))#candidate|3951|(3120,)|var|float64
const_3952 = relay.const([False,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False], dtype = "bool")#candidate|3952|(330,)|const|bool
var_3953 = relay.var("var_3953", dtype = "float32", shape = (504,))#candidate|3953|(504,)|var|float32
call_3949 = relay.TupleGetItem(func_3796_call(relay.reshape(var_3950.astype('float64'), [4, 14, 1]), relay.reshape(var_3951.astype('float64'), [1, 3120]), relay.reshape(const_3952.astype('bool'), [330,]), relay.reshape(var_3953.astype('float32'), [4, 14, 9]), ), 4)
call_3954 = relay.TupleGetItem(func_3801_call(relay.reshape(var_3950.astype('float64'), [4, 14, 1]), relay.reshape(var_3951.astype('float64'), [1, 3120]), relay.reshape(const_3952.astype('bool'), [330,]), relay.reshape(var_3953.astype('float32'), [4, 14, 9]), ), 4)
bop_3955 = relay.left_shift(const_3952.astype('int16'), var_3950.astype('int16')) # shape=(56, 330)
func_3917_call = mod.get_global_var('func_3917')
func_3918_call = mutated_mod.get_global_var('func_3918')
call_3963 = relay.TupleGetItem(func_3917_call(), 2)
call_3964 = relay.TupleGetItem(func_3918_call(), 2)
output = relay.Tuple([call_3924,call_3932,call_3949,var_3951,var_3953,bop_3955,call_3963,])
output2 = relay.Tuple([call_3925,call_3933,call_3954,var_3951,var_3953,bop_3955,call_3964,])
func_3987 = relay.Function([var_3950,var_3951,var_3953,], output)
mod['func_3987'] = func_3987
mod = relay.transform.InferType()(mod)
mutated_mod['func_3987'] = func_3987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3987_call = mutated_mod.get_global_var('func_3987')
var_3989 = relay.var("var_3989", dtype = "float64", shape = (56, 1))#candidate|3989|(56, 1)|var|float64
var_3990 = relay.var("var_3990", dtype = "float64", shape = (3120,))#candidate|3990|(3120,)|var|float64
var_3991 = relay.var("var_3991", dtype = "float32", shape = (504,))#candidate|3991|(504,)|var|float32
call_3988 = func_3987_call(var_3989,var_3990,var_3991,)
output = call_3988
func_3992 = relay.Function([var_3989,var_3990,var_3991,], output)
mutated_mod['func_3992'] = func_3992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1520_call = mod.get_global_var('func_1520')
func_1522_call = mutated_mod.get_global_var('func_1522')
call_4028 = relay.TupleGetItem(func_1520_call(), 1)
call_4029 = relay.TupleGetItem(func_1522_call(), 1)
const_4043 = relay.const([[[4.275185,6.168549,-7.772253,5.752090,-0.571223,-7.959297,-3.651777],[-2.140465,0.743691,-2.129718,-9.702894,-2.070155,7.563014,-7.560956],[3.995476,4.701207,1.909347,-7.473666,4.494011,-4.095211,-0.636222],[-5.376261,7.157796,-7.476152,2.123112,-1.468104,5.133554,3.479034],[-7.168600,-1.562560,0.889959,7.914813,-0.433450,-0.667441,2.976701],[7.714495,0.309630,-1.486038,0.419723,-1.141111,2.873554,-7.092979],[6.466048,9.630104,2.634638,-7.531803,-6.777115,8.997814,6.171299],[-2.601894,-5.312032,-5.058364,9.875361,-3.714183,1.445699,5.955523],[-4.807646,2.927704,2.765280,3.710801,3.368486,8.546374,0.349005],[-1.694657,1.802879,9.182158,5.106007,3.317618,-9.792360,9.141769]],[[-4.986455,6.838693,-5.236088,5.813148,7.694939,0.942073,-8.439395],[-3.478379,2.651095,-1.833311,8.130681,9.219574,6.853736,3.422037],[-6.368364,6.992773,7.132141,7.190077,-2.910864,4.769342,-3.048548],[-0.515934,-4.065985,-1.969115,7.204818,-2.046466,6.973351,1.089921],[-6.958993,-3.622585,9.253240,-1.857846,-8.417063,5.354714,-0.054489],[1.735504,3.362144,6.097669,-6.790685,7.536341,-7.136105,8.188852],[4.907151,-2.185410,8.054285,3.653643,-1.624450,-1.537184,7.416204],[3.254446,-4.079012,-3.209145,-8.174118,6.465816,-6.889212,7.263618],[-6.415335,-9.424082,9.856203,-7.942967,9.336467,-4.572666,4.471710],[4.189496,-8.308049,-9.854288,4.614815,-0.680966,-2.937561,-7.427073]],[[-4.786619,2.146580,-6.660265,7.594017,-7.569005,3.100633,6.474038],[8.521970,-9.957742,7.548710,-6.704657,3.174942,7.419048,8.685940],[-7.290063,-3.749663,4.612112,9.859605,2.984836,-7.524853,-7.928667],[5.674364,6.050230,-1.715716,5.029175,-1.787738,9.330698,7.269076],[4.382721,-7.967991,7.785777,-7.748617,-8.402620,-4.335187,-2.798563],[1.941908,-7.536421,-2.411268,-1.833941,4.536882,6.891327,9.039740],[-6.623119,3.371960,6.668681,9.388128,-0.020616,-6.481407,5.192549],[-6.611464,2.658233,4.634417,-8.121425,3.587489,-7.182788,9.433294],[-4.438819,6.259782,1.038350,-1.277102,-1.979281,3.358419,5.540815],[-7.531428,8.594525,5.311985,-9.212171,-1.915382,-6.727518,6.109886]],[[2.079803,-7.500505,7.761048,-1.092928,-5.036536,-7.176616,-0.540890],[4.335453,6.959568,-1.870451,-6.655026,2.761191,-4.616149,-6.424433],[8.360047,-8.932571,-0.844348,-2.784709,-4.150085,-3.774821,9.038856],[5.946722,5.815301,2.387400,-9.900733,7.970621,6.900325,-7.114495],[-2.839650,5.313574,-7.186016,-0.152837,-6.391327,4.733471,2.763518],[-6.323438,-5.504717,-4.546779,-9.860886,-7.369099,-4.498440,-4.773676],[-6.250856,0.691640,2.001083,-9.738980,-1.970304,-7.368784,3.177165],[2.214943,9.515940,0.890886,-6.372647,6.523304,3.106830,1.176609],[5.681009,-9.963564,-0.669367,5.880677,-4.978988,-1.091185,-8.836342],[3.126326,-1.405069,1.024970,-6.527357,5.377310,-9.753044,-9.882239]],[[-4.684908,6.302992,6.321738,1.169216,-7.576950,0.899155,-3.493417],[6.053468,-1.687536,-4.975698,-7.066292,-8.505756,-6.206599,1.418972],[0.738122,-0.084497,0.670863,4.473744,0.716964,7.682809,1.502484],[-3.211990,-0.049649,5.802351,0.777087,7.527225,2.633682,-7.833273],[8.884945,-6.370716,2.894526,-3.319533,7.627446,4.925135,-2.444028],[-0.700892,0.790364,4.043987,-0.201279,-9.489637,-0.327702,6.752339],[-5.966360,4.783676,3.135918,-6.293605,-0.507748,-8.181063,-0.841400],[5.480391,-1.301659,8.212155,-8.679968,7.587708,0.928081,-7.347802],[2.480509,1.736226,-5.183860,6.826727,-4.529617,-5.311651,-2.974527],[-2.288758,2.086427,4.129449,4.138232,5.577099,3.829784,8.771346]],[[1.730960,-3.064850,2.372903,-6.154962,-0.043028,-8.373541,5.885397],[1.791368,5.644756,-0.373397,9.101812,-4.984759,-8.098460,9.935381],[-4.471567,-1.409685,-1.992366,-0.975255,-4.058570,5.992631,-0.189801],[-3.692125,3.693774,5.763259,2.273510,7.250329,4.924806,-3.365005],[3.040264,2.883177,-3.688648,6.500892,-8.427475,-5.336459,-4.268431],[5.738946,6.818715,-9.768715,5.952004,3.475943,-1.768944,-6.476442],[-2.153188,2.535844,-4.369130,6.727620,5.744328,1.095651,-5.589935],[-5.830747,-2.057526,9.865820,8.780166,-8.356771,3.043632,-4.808608],[-4.890859,6.678605,2.424659,-6.911958,8.366554,-6.360761,3.314891],[-7.974167,4.440284,-1.654539,-1.214227,-4.408908,-3.036748,8.362221]],[[-4.689299,2.538505,-2.975012,-2.952594,0.689380,7.026636,-7.572189],[4.436280,1.793379,-9.760278,3.414166,-9.493418,-9.514548,1.652801],[5.642331,2.749400,-7.003626,-5.334775,1.090820,-9.131371,-0.720847],[-5.693462,0.881742,-5.396207,3.146064,-1.680974,5.737801,1.892210],[7.471608,-9.590013,3.714842,-1.954739,-2.773981,-2.647012,8.061340],[9.020282,-3.609125,8.776545,7.401477,-2.458289,-7.958272,9.773430],[-1.061665,7.327091,-5.061565,-8.340782,6.584488,1.102577,-0.092478],[-1.805772,2.302444,7.511645,2.173616,0.107538,-4.930452,7.309401],[-1.811023,-7.192347,7.855694,-7.069407,-9.408008,9.978729,-7.853014],[8.095669,-8.146657,-9.855515,9.965017,8.431545,-0.788295,-2.749450]],[[3.271208,1.616121,-2.776068,-1.338746,-0.541138,9.610555,1.276928],[-5.668192,-8.980411,-5.316080,7.023438,-5.194563,-0.010958,7.922228],[-4.637291,8.469212,-3.699100,-0.722335,4.317248,-5.287794,9.518413],[-4.289847,8.691261,-1.122456,-3.702611,-8.514748,-9.755163,4.410481],[1.822166,6.487308,-1.693857,9.867298,-3.116745,1.037612,-1.448065],[4.461296,-5.300757,-1.236916,-1.375179,7.178939,-2.608155,1.091930],[-8.468099,1.971248,5.971072,2.732879,-4.742715,-5.968161,-4.461131],[-0.249562,-9.079960,0.484144,6.853895,-2.500873,-5.586549,-0.210089],[0.952800,2.768812,-4.082200,0.408017,-9.912051,2.247285,7.527790],[7.718113,-2.369498,-2.805513,8.721441,3.592260,-4.014765,-0.465828]],[[9.796590,6.580666,-3.762695,-8.758809,3.127179,1.688228,-4.172279],[-7.719174,-1.144793,-7.229429,6.961621,7.293404,-9.756511,9.808397],[-7.939521,6.665764,3.052768,1.991471,-8.488306,-2.933604,9.067261],[8.247021,3.009856,-2.799549,1.404269,-3.565439,6.668529,9.169165],[-0.801222,-4.744269,-5.788587,-9.650867,-1.961209,-5.614332,3.731021],[0.359951,-5.717887,-3.310604,-9.435573,5.204313,0.048111,3.221999],[-9.712702,-2.977001,7.476649,9.111776,2.584259,6.790422,2.993380],[-9.989267,7.958597,-2.655846,-7.298861,6.673246,6.675440,-9.387141],[-8.243946,7.458584,-3.252903,8.618210,2.758425,6.526395,-3.180443],[-3.811332,-5.786601,-6.019721,-3.503628,1.966472,9.315383,-8.622444]],[[-8.277951,-7.834846,-9.800225,3.011581,9.309437,-7.990567,5.493403],[5.000879,4.683905,-1.771901,-6.381600,9.971166,1.162700,3.367118],[2.923477,6.214351,-5.424446,-6.995266,0.312794,7.857296,-3.450637],[4.027929,-8.087981,0.613893,1.262546,4.751902,-9.148514,-0.484707],[-6.722263,-2.065602,7.455497,3.588638,2.186792,-3.689864,4.361336],[-0.319672,-2.887079,2.902763,-1.794199,-6.291925,-0.264809,-8.223910],[-4.793898,-4.988555,-1.582058,-8.114849,-1.558635,-5.147930,3.246954],[6.008552,-4.517698,-7.392426,8.929544,5.092935,-6.625508,4.743319],[-1.305642,5.352498,4.828440,6.141214,-4.427796,0.162316,3.500351],[1.056868,5.647125,2.516523,-8.999706,-7.379172,3.741368,0.575152]],[[3.875147,6.383688,-6.922636,-3.307122,-4.278817,-6.953769,2.477668],[-4.444426,7.033977,7.530377,-4.224791,-4.759314,-4.957107,-2.201794],[8.731357,4.131520,1.974366,-0.356472,6.810023,5.120958,-1.514631],[-9.831930,3.617501,-4.803140,-6.068775,4.685229,-7.848442,2.534177],[-3.446805,-9.942795,-2.731192,-6.277133,-5.089531,0.419910,4.182279],[-8.156719,-0.999673,7.454071,5.356912,-4.040272,3.762650,-9.394827],[-8.838283,-4.072601,6.736191,-6.937302,-7.330692,4.524740,7.150335],[-8.206534,4.535989,-5.171240,-3.126675,-8.214177,8.156898,7.805017],[-2.593943,-3.900789,-4.559876,-8.362086,8.895207,3.698540,6.357443],[2.926693,9.589615,-8.072942,-2.936613,5.706009,-3.354458,-7.980681]],[[-9.694904,4.488946,4.067736,4.853409,-6.130211,9.061031,-5.830817],[-5.405006,-9.070477,-7.076801,0.913908,-8.033761,9.568876,-9.301624],[5.543682,2.990127,9.009908,8.157655,-3.897183,-8.255939,-5.962160],[7.867963,-7.622419,-2.597736,3.892669,-0.340599,4.878991,-2.638571],[-2.934419,6.696782,1.952745,-4.460110,4.726526,9.107721,-7.327873],[-8.351168,7.801958,-1.198778,2.279677,-8.640283,7.406885,-5.169230],[-0.512493,-6.263259,2.474493,-7.068945,-0.530206,6.313502,-1.274892],[-9.618009,-2.951437,2.268732,-3.815112,9.304605,7.286580,-4.136587],[8.774210,9.510796,8.264665,-1.197744,0.022792,2.675568,4.637565],[8.590057,0.442782,9.187787,9.105214,1.152656,-7.747986,8.539481]],[[4.075621,-2.824223,-2.544529,-4.725935,8.211443,9.759116,0.637771],[8.723542,7.719813,0.707523,-0.930026,9.102039,8.134411,6.217988],[6.640992,1.223679,-5.436011,7.666965,-9.471894,-2.660907,3.142980],[-2.324928,-7.083256,7.897355,3.510407,-9.674891,6.780249,3.024939],[-0.475382,-9.023641,4.893422,-3.731530,-6.817953,9.450390,7.104054],[-5.224654,8.585593,-0.048282,-7.375651,0.500259,-8.709837,2.708985],[4.601975,-7.462849,3.731323,-0.793406,0.740886,-4.658860,-9.633097],[-3.647240,7.726790,-7.717665,4.310325,-2.433707,1.660780,4.523302],[3.334741,2.106404,9.221159,0.161231,0.137464,-6.647008,-6.022678],[-4.636082,-1.851482,6.834725,1.042850,-2.742831,-5.339068,3.891496]],[[-5.088656,9.922049,3.215942,6.838564,-9.295671,-2.010694,-2.060096],[-7.886020,7.973320,9.501198,8.143986,-0.336084,7.079182,-6.714710],[0.279632,7.401633,-0.795470,-2.679351,6.186174,3.727848,-4.281089],[5.541488,-5.057466,8.357366,-5.978423,3.641975,4.975257,7.450846],[-1.110194,-8.650625,1.544549,3.060165,-1.515736,6.709373,8.439712],[-8.372711,-3.764078,-4.029556,0.966943,8.151933,9.179869,-5.148105],[-3.467448,5.404090,0.743312,-5.816811,1.572526,-5.377938,4.695432],[1.601868,-1.014744,-8.326390,-5.912998,2.136266,4.282752,2.875801],[2.983466,8.217479,3.985567,-7.389834,9.274668,4.909003,3.441094],[-1.054577,-4.735102,5.942685,5.964916,5.112778,2.644712,-4.206797]]], dtype = "float64")#candidate|4043|(14, 10, 7)|const|float64
bop_4044 = relay.mod(call_4028.astype('float64'), relay.reshape(const_4043.astype('float64'), relay.shape_of(call_4028))) # shape=(14, 10, 7)
bop_4047 = relay.mod(call_4029.astype('float64'), relay.reshape(const_4043.astype('float64'), relay.shape_of(call_4029))) # shape=(14, 10, 7)
output = relay.Tuple([bop_4044,])
output2 = relay.Tuple([bop_4047,])
func_4065 = relay.Function([], output)
mod['func_4065'] = func_4065
mod = relay.transform.InferType()(mod)
mutated_mod['func_4065'] = func_4065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4065_call = mutated_mod.get_global_var('func_4065')
call_4066 = func_4065_call()
output = call_4066
func_4067 = relay.Function([], output)
mutated_mod['func_4067'] = func_4067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_4107 = func_947_call()
call_4108 = func_947_call()
func_568_call = mod.get_global_var('func_568')
func_570_call = mutated_mod.get_global_var('func_570')
call_4109 = relay.TupleGetItem(func_568_call(), 1)
call_4110 = relay.TupleGetItem(func_570_call(), 1)
output = relay.Tuple([call_4107,call_4109,])
output2 = relay.Tuple([call_4108,call_4110,])
func_4119 = relay.Function([], output)
mod['func_4119'] = func_4119
mod = relay.transform.InferType()(mod)
output = func_4119()
func_4120 = relay.Function([], output)
mutated_mod['func_4120'] = func_4120
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4145 = relay.var("var_4145", dtype = "int64", shape = (16, 16, 11))#candidate|4145|(16, 16, 11)|var|int64
var_4146 = relay.var("var_4146", dtype = "int64", shape = (16, 16, 11))#candidate|4146|(16, 16, 11)|var|int64
bop_4147 = relay.add(var_4145.astype('int64'), relay.reshape(var_4146.astype('int64'), relay.shape_of(var_4145))) # shape=(16, 16, 11)
bop_4153 = relay.subtract(bop_4147.astype('int8'), relay.reshape(var_4145.astype('int8'), relay.shape_of(bop_4147))) # shape=(16, 16, 11)
bop_4164 = relay.greater_equal(bop_4153.astype('bool'), relay.reshape(bop_4147.astype('bool'), relay.shape_of(bop_4153))) # shape=(16, 16, 11)
uop_4172 = relay.sigmoid(bop_4164.astype('float64')) # shape=(16, 16, 11)
bop_4189 = relay.bitwise_and(uop_4172.astype('uint16'), relay.reshape(var_4146.astype('uint16'), relay.shape_of(uop_4172))) # shape=(16, 16, 11)
func_3226_call = mod.get_global_var('func_3226')
func_3229_call = mutated_mod.get_global_var('func_3229')
const_4194 = relay.const(-3.793267, dtype = "float64")#candidate|4194|()|const|float64
call_4193 = relay.TupleGetItem(func_3226_call(relay.reshape(const_4194.astype('float64'), [])), 0)
call_4195 = relay.TupleGetItem(func_3229_call(relay.reshape(const_4194.astype('float64'), [])), 0)
output = relay.Tuple([bop_4189,call_4193,const_4194,])
output2 = relay.Tuple([bop_4189,call_4195,const_4194,])
func_4198 = relay.Function([var_4145,var_4146,], output)
mod['func_4198'] = func_4198
mod = relay.transform.InferType()(mod)
var_4199 = relay.var("var_4199", dtype = "int64", shape = (16, 16, 11))#candidate|4199|(16, 16, 11)|var|int64
var_4200 = relay.var("var_4200", dtype = "int64", shape = (16, 16, 11))#candidate|4200|(16, 16, 11)|var|int64
output = func_4198(var_4199,var_4200,)
func_4201 = relay.Function([var_4199,var_4200,], output)
mutated_mod['func_4201'] = func_4201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2653_call = mod.get_global_var('func_2653')
func_2655_call = mutated_mod.get_global_var('func_2655')
call_4210 = relay.TupleGetItem(func_2653_call(), 2)
call_4211 = relay.TupleGetItem(func_2655_call(), 2)
func_2470_call = mod.get_global_var('func_2470')
func_2471_call = mutated_mod.get_global_var('func_2471')
call_4230 = func_2470_call()
call_4231 = func_2470_call()
output = relay.Tuple([call_4210,call_4230,])
output2 = relay.Tuple([call_4211,call_4231,])
func_4236 = relay.Function([], output)
mod['func_4236'] = func_4236
mod = relay.transform.InferType()(mod)
output = func_4236()
func_4237 = relay.Function([], output)
mutated_mod['func_4237'] = func_4237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1413_call = mod.get_global_var('func_1413')
func_1415_call = mutated_mod.get_global_var('func_1415')
call_4254 = relay.TupleGetItem(func_1413_call(), 0)
call_4255 = relay.TupleGetItem(func_1415_call(), 0)
output = call_4254
output2 = call_4255
func_4256 = relay.Function([], output)
mod['func_4256'] = func_4256
mod = relay.transform.InferType()(mod)
mutated_mod['func_4256'] = func_4256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4256_call = mutated_mod.get_global_var('func_4256')
call_4257 = func_4256_call()
output = call_4257
func_4258 = relay.Function([], output)
mutated_mod['func_4258'] = func_4258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_4270 = relay.TupleGetItem(func_376_call(), 0)
call_4271 = relay.TupleGetItem(func_377_call(), 0)
func_311_call = mod.get_global_var('func_311')
func_313_call = mutated_mod.get_global_var('func_313')
call_4294 = relay.TupleGetItem(func_311_call(), 1)
call_4295 = relay.TupleGetItem(func_313_call(), 1)
output = relay.Tuple([call_4270,call_4294,])
output2 = relay.Tuple([call_4271,call_4295,])
func_4306 = relay.Function([], output)
mod['func_4306'] = func_4306
mod = relay.transform.InferType()(mod)
output = func_4306()
func_4307 = relay.Function([], output)
mutated_mod['func_4307'] = func_4307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3264_call = mod.get_global_var('func_3264')
func_3266_call = mutated_mod.get_global_var('func_3266')
call_4348 = func_3264_call()
call_4349 = func_3264_call()
func_139_call = mod.get_global_var('func_139')
func_141_call = mutated_mod.get_global_var('func_141')
call_4359 = relay.TupleGetItem(func_139_call(), 0)
call_4360 = relay.TupleGetItem(func_141_call(), 0)
output = relay.Tuple([call_4348,call_4359,])
output2 = relay.Tuple([call_4349,call_4360,])
func_4372 = relay.Function([], output)
mod['func_4372'] = func_4372
mod = relay.transform.InferType()(mod)
output = func_4372()
func_4373 = relay.Function([], output)
mutated_mod['func_4373'] = func_4373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_139_call = mod.get_global_var('func_139')
func_141_call = mutated_mod.get_global_var('func_141')
call_4387 = relay.TupleGetItem(func_139_call(), 0)
call_4388 = relay.TupleGetItem(func_141_call(), 0)
func_3487_call = mod.get_global_var('func_3487')
func_3488_call = mutated_mod.get_global_var('func_3488')
call_4389 = func_3487_call()
call_4390 = func_3487_call()
func_3917_call = mod.get_global_var('func_3917')
func_3918_call = mutated_mod.get_global_var('func_3918')
call_4391 = relay.TupleGetItem(func_3917_call(), 1)
call_4392 = relay.TupleGetItem(func_3918_call(), 1)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_4403 = relay.TupleGetItem(func_376_call(), 0)
call_4404 = relay.TupleGetItem(func_377_call(), 0)
func_3199_call = mod.get_global_var('func_3199')
func_3201_call = mutated_mod.get_global_var('func_3201')
call_4407 = func_3199_call()
call_4408 = func_3199_call()
output = relay.Tuple([call_4387,call_4389,call_4391,call_4403,call_4407,])
output2 = relay.Tuple([call_4388,call_4390,call_4392,call_4404,call_4408,])
func_4413 = relay.Function([], output)
mod['func_4413'] = func_4413
mod = relay.transform.InferType()(mod)
mutated_mod['func_4413'] = func_4413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4413_call = mutated_mod.get_global_var('func_4413')
call_4414 = func_4413_call()
output = call_4414
func_4415 = relay.Function([], output)
mutated_mod['func_4415'] = func_4415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_253_call = mutated_mod.get_global_var('func_253')
call_4488 = relay.TupleGetItem(func_252_call(), 0)
call_4489 = relay.TupleGetItem(func_253_call(), 0)
func_2918_call = mod.get_global_var('func_2918')
func_2919_call = mutated_mod.get_global_var('func_2919')
call_4502 = relay.TupleGetItem(func_2918_call(), 0)
call_4503 = relay.TupleGetItem(func_2919_call(), 0)
output = relay.Tuple([call_4488,call_4502,])
output2 = relay.Tuple([call_4489,call_4503,])
func_4509 = relay.Function([], output)
mod['func_4509'] = func_4509
mod = relay.transform.InferType()(mod)
output = func_4509()
func_4510 = relay.Function([], output)
mutated_mod['func_4510'] = func_4510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2918_call = mod.get_global_var('func_2918')
func_2919_call = mutated_mod.get_global_var('func_2919')
call_4559 = relay.TupleGetItem(func_2918_call(), 0)
call_4560 = relay.TupleGetItem(func_2919_call(), 0)
func_2190_call = mod.get_global_var('func_2190')
func_2193_call = mutated_mod.get_global_var('func_2193')
const_4566 = relay.const([7.075789,-9.761352,-9.792429,2.247010,-4.209218,-0.694086,4.154574,-0.163758,1.392601,-1.732589,3.638569,-3.172288,-1.585648,2.476573,5.590053,7.663421,1.126800,-3.649766,-5.467870,-4.603616,-4.851875,-2.240370,8.700957,2.736148,-7.844713,-4.153716,8.339358,-0.199913,9.573292,2.147816,-7.391937,-8.608434,-9.002895,-9.918001,-9.182828,-0.546134,8.889432,-2.476655,6.457869,2.192754,6.169976,-2.756700,1.921043,-8.139028,-9.029008,4.538925,-7.510611,-7.537177,-0.019770,2.227563,-5.484255,8.650368,-7.028253,-6.200289,5.695480,-5.699094,3.335417,2.881185,7.907446,-0.182076,7.057396,-4.351259,7.653755,7.265421,7.343399,-0.032756,-6.219209,7.053844,8.316492,-7.355650,-7.604727,7.926621,6.006556,-2.564144,-4.089691,-8.690163,-5.332603,6.712161,-0.092733,-2.632825], dtype = "float64")#candidate|4566|(80,)|const|float64
call_4565 = relay.TupleGetItem(func_2190_call(relay.reshape(const_4566.astype('float64'), [80,])), 5)
call_4567 = relay.TupleGetItem(func_2193_call(relay.reshape(const_4566.astype('float64'), [80,])), 5)
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
call_4574 = relay.TupleGetItem(func_759_call(), 1)
call_4575 = relay.TupleGetItem(func_761_call(), 1)
output = relay.Tuple([call_4559,call_4565,const_4566,call_4574,])
output2 = relay.Tuple([call_4560,call_4567,const_4566,call_4575,])
func_4576 = relay.Function([], output)
mod['func_4576'] = func_4576
mod = relay.transform.InferType()(mod)
output = func_4576()
func_4577 = relay.Function([], output)
mutated_mod['func_4577'] = func_4577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4413_call = mod.get_global_var('func_4413')
func_4415_call = mutated_mod.get_global_var('func_4415')
call_4583 = relay.TupleGetItem(func_4413_call(), 1)
call_4584 = relay.TupleGetItem(func_4415_call(), 1)
output = call_4583
output2 = call_4584
func_4586 = relay.Function([], output)
mod['func_4586'] = func_4586
mod = relay.transform.InferType()(mod)
output = func_4586()
func_4587 = relay.Function([], output)
mutated_mod['func_4587'] = func_4587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_4623 = relay.TupleGetItem(func_1112_call(), 0)
call_4624 = relay.TupleGetItem(func_1113_call(), 0)
func_3815_call = mod.get_global_var('func_3815')
func_3817_call = mutated_mod.get_global_var('func_3817')
call_4632 = func_3815_call()
call_4633 = func_3815_call()
func_1338_call = mod.get_global_var('func_1338')
func_1339_call = mutated_mod.get_global_var('func_1339')
call_4654 = relay.TupleGetItem(func_1338_call(), 0)
call_4655 = relay.TupleGetItem(func_1339_call(), 0)
output = relay.Tuple([call_4623,call_4632,call_4654,])
output2 = relay.Tuple([call_4624,call_4633,call_4655,])
func_4659 = relay.Function([], output)
mod['func_4659'] = func_4659
mod = relay.transform.InferType()(mod)
output = func_4659()
func_4660 = relay.Function([], output)
mutated_mod['func_4660'] = func_4660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2326_call = mod.get_global_var('func_2326')
func_2327_call = mutated_mod.get_global_var('func_2327')
call_4697 = relay.TupleGetItem(func_2326_call(), 0)
call_4698 = relay.TupleGetItem(func_2327_call(), 0)
output = call_4697
output2 = call_4698
func_4700 = relay.Function([], output)
mod['func_4700'] = func_4700
mod = relay.transform.InferType()(mod)
mutated_mod['func_4700'] = func_4700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4700_call = mutated_mod.get_global_var('func_4700')
call_4701 = func_4700_call()
output = call_4701
func_4702 = relay.Function([], output)
mutated_mod['func_4702'] = func_4702
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4703 = relay.var("var_4703", dtype = "int32", shape = ())#candidate|4703|()|var|int32
var_4704 = relay.var("var_4704", dtype = "int32", shape = (3, 11, 2))#candidate|4704|(3, 11, 2)|var|int32
bop_4705 = relay.greater_equal(var_4703.astype('bool'), var_4704.astype('bool')) # shape=(3, 11, 2)
func_4413_call = mod.get_global_var('func_4413')
func_4415_call = mutated_mod.get_global_var('func_4415')
call_4709 = relay.TupleGetItem(func_4413_call(), 4)
call_4710 = relay.TupleGetItem(func_4415_call(), 4)
output = relay.Tuple([bop_4705,call_4709,])
output2 = relay.Tuple([bop_4705,call_4710,])
func_4711 = relay.Function([var_4703,var_4704,], output)
mod['func_4711'] = func_4711
mod = relay.transform.InferType()(mod)
mutated_mod['func_4711'] = func_4711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4711_call = mutated_mod.get_global_var('func_4711')
var_4713 = relay.var("var_4713", dtype = "int32", shape = ())#candidate|4713|()|var|int32
var_4714 = relay.var("var_4714", dtype = "int32", shape = (3, 11, 2))#candidate|4714|(3, 11, 2)|var|int32
call_4712 = func_4711_call(var_4713,var_4714,)
output = call_4712
func_4715 = relay.Function([var_4713,var_4714,], output)
mutated_mod['func_4715'] = func_4715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2986_call = mod.get_global_var('func_2986')
func_2987_call = mutated_mod.get_global_var('func_2987')
call_4748 = relay.TupleGetItem(func_2986_call(), 0)
call_4749 = relay.TupleGetItem(func_2987_call(), 0)
output = relay.Tuple([call_4748,])
output2 = relay.Tuple([call_4749,])
func_4751 = relay.Function([], output)
mod['func_4751'] = func_4751
mod = relay.transform.InferType()(mod)
mutated_mod['func_4751'] = func_4751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4751_call = mutated_mod.get_global_var('func_4751')
call_4752 = func_4751_call()
output = call_4752
func_4753 = relay.Function([], output)
mutated_mod['func_4753'] = func_4753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3404_call = mod.get_global_var('func_3404')
func_3406_call = mutated_mod.get_global_var('func_3406')
call_4801 = func_3404_call()
call_4802 = func_3404_call()
output = call_4801
output2 = call_4802
func_4819 = relay.Function([], output)
mod['func_4819'] = func_4819
mod = relay.transform.InferType()(mod)
output = func_4819()
func_4820 = relay.Function([], output)
mutated_mod['func_4820'] = func_4820
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4854 = relay.var("var_4854", dtype = "int64", shape = (3, 14, 9))#candidate|4854|(3, 14, 9)|var|int64
var_4855 = relay.var("var_4855", dtype = "int64", shape = (3, 14, 9))#candidate|4855|(3, 14, 9)|var|int64
bop_4856 = relay.logical_xor(var_4854.astype('int64'), relay.reshape(var_4855.astype('int64'), relay.shape_of(var_4854))) # shape=(3, 14, 9)
func_1888_call = mod.get_global_var('func_1888')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_4870 = relay.TupleGetItem(func_1888_call(), 1)
call_4871 = relay.TupleGetItem(func_1890_call(), 1)
func_4119_call = mod.get_global_var('func_4119')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_4890 = relay.TupleGetItem(func_4119_call(), 1)
call_4891 = relay.TupleGetItem(func_4120_call(), 1)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_4894 = relay.TupleGetItem(func_3642_call(), 0)
call_4895 = relay.TupleGetItem(func_3643_call(), 0)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
const_4902 = relay.const([9.471333,-3.206146,-5.158744,-0.547202,0.709639,1.635354,6.974213,6.630443,6.609350,0.863234,4.829137,5.097887,4.751182,-3.988531,9.290190,-0.075721,8.936889,-6.914515,3.965079,-4.891822,-7.308097,-7.768289,0.620054,-7.480966,9.746166,2.036308,-1.817712,-1.020672,2.973157,-0.190973,9.185354,2.504200,8.190151,1.934565,9.711801,-2.045999,3.991332,6.935001,-4.193662,6.050817,-3.926693,-8.941112,7.421219,-3.252919,4.069490,-1.370905,-3.730165,-7.259715,8.741247,-2.474160,5.917795,4.325530,8.697932,7.852501,-6.338474,9.238484,7.559752,3.418515,-5.867873,-6.562636,-4.837480,4.762722,-4.663754,9.594787,0.727614,-2.250934,-6.391226,3.854484,9.903733,6.275191,5.753466,-9.698684,-7.488526,4.689111,6.825385,-1.531619,-8.297954,-6.402692,0.408040,3.396433], dtype = "float64")#candidate|4902|(80,)|const|float64
call_4901 = relay.TupleGetItem(func_1319_call(relay.reshape(call_4890.astype('float64'), [14, 10, 7]), relay.reshape(const_4902.astype('float64'), [80, 1]), ), 2)
call_4903 = relay.TupleGetItem(func_1322_call(relay.reshape(call_4890.astype('float64'), [14, 10, 7]), relay.reshape(const_4902.astype('float64'), [80, 1]), ), 2)
output = relay.Tuple([bop_4856,call_4870,call_4890,call_4894,call_4901,const_4902,])
output2 = relay.Tuple([bop_4856,call_4871,call_4891,call_4895,call_4903,const_4902,])
func_4912 = relay.Function([var_4854,var_4855,], output)
mod['func_4912'] = func_4912
mod = relay.transform.InferType()(mod)
mutated_mod['func_4912'] = func_4912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4912_call = mutated_mod.get_global_var('func_4912')
var_4914 = relay.var("var_4914", dtype = "int64", shape = (3, 14, 9))#candidate|4914|(3, 14, 9)|var|int64
var_4915 = relay.var("var_4915", dtype = "int64", shape = (3, 14, 9))#candidate|4915|(3, 14, 9)|var|int64
call_4913 = func_4912_call(var_4914,var_4915,)
output = call_4913
func_4916 = relay.Function([var_4914,var_4915,], output)
mutated_mod['func_4916'] = func_4916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4576_call = mod.get_global_var('func_4576')
func_4577_call = mutated_mod.get_global_var('func_4577')
call_4923 = relay.TupleGetItem(func_4576_call(), 2)
call_4924 = relay.TupleGetItem(func_4577_call(), 2)
func_3674_call = mod.get_global_var('func_3674')
func_3676_call = mutated_mod.get_global_var('func_3676')
call_4950 = relay.TupleGetItem(func_3674_call(), 0)
call_4951 = relay.TupleGetItem(func_3676_call(), 0)
output = relay.Tuple([call_4923,call_4950,])
output2 = relay.Tuple([call_4924,call_4951,])
func_4989 = relay.Function([], output)
mod['func_4989'] = func_4989
mod = relay.transform.InferType()(mod)
mutated_mod['func_4989'] = func_4989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4989_call = mutated_mod.get_global_var('func_4989')
call_4990 = func_4989_call()
output = call_4990
func_4991 = relay.Function([], output)
mutated_mod['func_4991'] = func_4991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_4998 = relay.TupleGetItem(func_859_call(), 3)
call_4999 = relay.TupleGetItem(func_860_call(), 3)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_5004 = relay.TupleGetItem(func_1112_call(), 0)
call_5005 = relay.TupleGetItem(func_1113_call(), 0)
output = relay.Tuple([call_4998,call_5004,])
output2 = relay.Tuple([call_4999,call_5005,])
func_5013 = relay.Function([], output)
mod['func_5013'] = func_5013
mod = relay.transform.InferType()(mod)
mutated_mod['func_5013'] = func_5013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5013_call = mutated_mod.get_global_var('func_5013')
call_5014 = func_5013_call()
output = call_5014
func_5015 = relay.Function([], output)
mutated_mod['func_5015'] = func_5015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_5027 = relay.TupleGetItem(func_2009_call(), 0)
call_5028 = relay.TupleGetItem(func_2011_call(), 0)
output = call_5027
output2 = call_5028
func_5034 = relay.Function([], output)
mod['func_5034'] = func_5034
mod = relay.transform.InferType()(mod)
output = func_5034()
func_5035 = relay.Function([], output)
mutated_mod['func_5035'] = func_5035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4509_call = mod.get_global_var('func_4509')
func_4510_call = mutated_mod.get_global_var('func_4510')
call_5078 = relay.TupleGetItem(func_4509_call(), 1)
call_5079 = relay.TupleGetItem(func_4510_call(), 1)
output = call_5078
output2 = call_5079
func_5092 = relay.Function([], output)
mod['func_5092'] = func_5092
mod = relay.transform.InferType()(mod)
mutated_mod['func_5092'] = func_5092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mutated_mod.get_global_var('func_5092')
call_5093 = func_5092_call()
output = call_5093
func_5094 = relay.Function([], output)
mutated_mod['func_5094'] = func_5094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4119_call = mod.get_global_var('func_4119')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_5220 = relay.TupleGetItem(func_4119_call(), 1)
call_5221 = relay.TupleGetItem(func_4120_call(), 1)
func_3544_call = mod.get_global_var('func_3544')
func_3546_call = mutated_mod.get_global_var('func_3546')
call_5222 = relay.TupleGetItem(func_3544_call(), 1)
call_5223 = relay.TupleGetItem(func_3546_call(), 1)
func_621_call = mod.get_global_var('func_621')
func_624_call = mutated_mod.get_global_var('func_624')
const_5238 = relay.const([-9,2,-7,7,-10,-3,2,-6,-1,-2,9,-5,1,-9,-6,-2,9,5,10,3,4,-2,9,-7,-10,1,2,6,-7,6,1,10,-3,-5,-8,-2,-8,9,2,-10,-6,-4,7,4,4,9,7,5,-4,-2,1,-5,8,-6,1,-7,-7,7,-10,9,-8,-9,-6,6,7,2,-4,6,-4,-4,-8,-4,-3,-10,10,9,6,7,-2,-3,1,-8,-6,-8,-9,-5,-5,-4,10,1,3,-9,8,2,1,1,-3,-8,3,9,-8,9,-3,-2,-6,2,5,-2,-9,2,-2,-1,-2,-3,-3,-7,7,6,8,3,-1,7,6,8,4,5,-5,-10,-3,3,9,9,-7,-8,-3,1,5,1,-5,-7,10,-4,8,3,-1,9,8,6,5,10,-2,-3,9,8,-2,5,-7,-5,5,8,6,-5,-7,10,2,9,1,3,-5,-5,6,-7,1,9,1,3,5,4,9,-2,-3,7,3,5,-10,3,10,-10,3,6,-7,3,-7,3,-10,6,-8,-9,-4,-8,-5,-10,-4,-6,2,-1,1,2,-1,-5,-10,6,8,8,10,-6,-1,-7,-9,-2,-5,1,-6,-7,5,-8,4,2,9,-4,10,-1,-8,-7,-3,7,1,7,8,6,5,10,-10,-5,-6,8,-9,-8,1,-4,-4,2,9,-7,-3,-4,-9,-2,-9,-9,-6,-1,-8,-3,-6,-1,8,-10,-5,5,9,10,2,-6,9,-5,2,1,9,-7], dtype = "int16")#candidate|5238|(280,)|const|int16
call_5237 = func_621_call(relay.reshape(const_5238.astype('int16'), [2, 14, 10]), relay.reshape(const_5238.astype('int16'), [2, 14, 10]), )
call_5239 = func_621_call(relay.reshape(const_5238.astype('int16'), [2, 14, 10]), relay.reshape(const_5238.astype('int16'), [2, 14, 10]), )
bop_5250 = relay.left_shift(call_5220.astype('int8'), relay.reshape(call_5222.astype('int8'), relay.shape_of(call_5220))) # shape=(14, 10, 7)
bop_5253 = relay.left_shift(call_5221.astype('int8'), relay.reshape(call_5223.astype('int8'), relay.shape_of(call_5221))) # shape=(14, 10, 7)
output = relay.Tuple([call_5237,const_5238,bop_5250,])
output2 = relay.Tuple([call_5239,const_5238,bop_5253,])
func_5255 = relay.Function([], output)
mod['func_5255'] = func_5255
mod = relay.transform.InferType()(mod)
mutated_mod['func_5255'] = func_5255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5255_call = mutated_mod.get_global_var('func_5255')
call_5256 = func_5255_call()
output = call_5256
func_5257 = relay.Function([], output)
mutated_mod['func_5257'] = func_5257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3349_call = mod.get_global_var('func_3349')
func_3351_call = mutated_mod.get_global_var('func_3351')
call_5291 = relay.TupleGetItem(func_3349_call(), 0)
call_5292 = relay.TupleGetItem(func_3351_call(), 0)
func_3028_call = mod.get_global_var('func_3028')
func_3030_call = mutated_mod.get_global_var('func_3030')
call_5341 = relay.TupleGetItem(func_3028_call(), 1)
call_5342 = relay.TupleGetItem(func_3030_call(), 1)
output = relay.Tuple([call_5291,call_5341,])
output2 = relay.Tuple([call_5292,call_5342,])
func_5349 = relay.Function([], output)
mod['func_5349'] = func_5349
mod = relay.transform.InferType()(mod)
output = func_5349()
func_5350 = relay.Function([], output)
mutated_mod['func_5350'] = func_5350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1338_call = mod.get_global_var('func_1338')
func_1339_call = mutated_mod.get_global_var('func_1339')
call_5369 = relay.TupleGetItem(func_1338_call(), 0)
call_5370 = relay.TupleGetItem(func_1339_call(), 0)
output = call_5369
output2 = call_5370
func_5403 = relay.Function([], output)
mod['func_5403'] = func_5403
mod = relay.transform.InferType()(mod)
mutated_mod['func_5403'] = func_5403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5403_call = mutated_mod.get_global_var('func_5403')
call_5404 = func_5403_call()
output = call_5404
func_5405 = relay.Function([], output)
mutated_mod['func_5405'] = func_5405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5409 = relay.var("var_5409", dtype = "float32", shape = (11, 11, 14))#candidate|5409|(11, 11, 14)|var|float32
uop_5410 = relay.rsqrt(var_5409.astype('float32')) # shape=(11, 11, 14)
var_5418 = relay.var("var_5418", dtype = "float32", shape = (11, 11, 14))#candidate|5418|(11, 11, 14)|var|float32
bop_5419 = relay.bitwise_xor(uop_5410.astype('int16'), relay.reshape(var_5418.astype('int16'), relay.shape_of(uop_5410))) # shape=(11, 11, 14)
uop_5432 = relay.sqrt(uop_5410.astype('float32')) # shape=(11, 11, 14)
output = relay.Tuple([bop_5419,uop_5432,])
output2 = relay.Tuple([bop_5419,uop_5432,])
func_5435 = relay.Function([var_5409,var_5418,], output)
mod['func_5435'] = func_5435
mod = relay.transform.InferType()(mod)
mutated_mod['func_5435'] = func_5435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5435_call = mutated_mod.get_global_var('func_5435')
var_5437 = relay.var("var_5437", dtype = "float32", shape = (11, 11, 14))#candidate|5437|(11, 11, 14)|var|float32
var_5438 = relay.var("var_5438", dtype = "float32", shape = (11, 11, 14))#candidate|5438|(11, 11, 14)|var|float32
call_5436 = func_5435_call(var_5437,var_5438,)
output = call_5436
func_5439 = relay.Function([var_5437,var_5438,], output)
mutated_mod['func_5439'] = func_5439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1338_call = mod.get_global_var('func_1338')
func_1339_call = mutated_mod.get_global_var('func_1339')
call_5454 = relay.TupleGetItem(func_1338_call(), 0)
call_5455 = relay.TupleGetItem(func_1339_call(), 0)
output = relay.Tuple([call_5454,])
output2 = relay.Tuple([call_5455,])
func_5460 = relay.Function([], output)
mod['func_5460'] = func_5460
mod = relay.transform.InferType()(mod)
mutated_mod['func_5460'] = func_5460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5460_call = mutated_mod.get_global_var('func_5460')
call_5461 = func_5460_call()
output = call_5461
func_5462 = relay.Function([], output)
mutated_mod['func_5462'] = func_5462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1219_call = mod.get_global_var('func_1219')
func_1220_call = mutated_mod.get_global_var('func_1220')
call_5508 = relay.TupleGetItem(func_1219_call(), 2)
call_5509 = relay.TupleGetItem(func_1220_call(), 2)
output = call_5508
output2 = call_5509
func_5517 = relay.Function([], output)
mod['func_5517'] = func_5517
mod = relay.transform.InferType()(mod)
mutated_mod['func_5517'] = func_5517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5517_call = mutated_mod.get_global_var('func_5517')
call_5518 = func_5517_call()
output = call_5518
func_5519 = relay.Function([], output)
mutated_mod['func_5519'] = func_5519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2121_call = mod.get_global_var('func_2121')
func_2123_call = mutated_mod.get_global_var('func_2123')
call_5548 = relay.TupleGetItem(func_2121_call(), 3)
call_5549 = relay.TupleGetItem(func_2123_call(), 3)
output = relay.Tuple([call_5548,])
output2 = relay.Tuple([call_5549,])
func_5559 = relay.Function([], output)
mod['func_5559'] = func_5559
mod = relay.transform.InferType()(mod)
output = func_5559()
func_5560 = relay.Function([], output)
mutated_mod['func_5560'] = func_5560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_5561 = relay.TupleGetItem(func_75_call(), 0)
call_5562 = relay.TupleGetItem(func_76_call(), 0)
output = relay.Tuple([call_5561,])
output2 = relay.Tuple([call_5562,])
func_5566 = relay.Function([], output)
mod['func_5566'] = func_5566
mod = relay.transform.InferType()(mod)
output = func_5566()
func_5567 = relay.Function([], output)
mutated_mod['func_5567'] = func_5567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4509_call = mod.get_global_var('func_4509')
func_4510_call = mutated_mod.get_global_var('func_4510')
call_5629 = relay.TupleGetItem(func_4509_call(), 0)
call_5630 = relay.TupleGetItem(func_4510_call(), 0)
func_3349_call = mod.get_global_var('func_3349')
func_3351_call = mutated_mod.get_global_var('func_3351')
call_5666 = relay.TupleGetItem(func_3349_call(), 1)
call_5667 = relay.TupleGetItem(func_3351_call(), 1)
output = relay.Tuple([call_5629,call_5666,])
output2 = relay.Tuple([call_5630,call_5667,])
func_5671 = relay.Function([], output)
mod['func_5671'] = func_5671
mod = relay.transform.InferType()(mod)
mutated_mod['func_5671'] = func_5671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5671_call = mutated_mod.get_global_var('func_5671')
call_5672 = func_5671_call()
output = call_5672
func_5673 = relay.Function([], output)
mutated_mod['func_5673'] = func_5673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4119_call = mod.get_global_var('func_4119')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_5685 = relay.TupleGetItem(func_4119_call(), 1)
call_5686 = relay.TupleGetItem(func_4120_call(), 1)
output = relay.Tuple([call_5685,])
output2 = relay.Tuple([call_5686,])
func_5692 = relay.Function([], output)
mod['func_5692'] = func_5692
mod = relay.transform.InferType()(mod)
output = func_5692()
func_5693 = relay.Function([], output)
mutated_mod['func_5693'] = func_5693
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5697 = relay.var("var_5697", dtype = "uint32", shape = (7, 13, 3))#candidate|5697|(7, 13, 3)|var|uint32
var_5698 = relay.var("var_5698", dtype = "uint32", shape = (7, 13, 3))#candidate|5698|(7, 13, 3)|var|uint32
bop_5699 = relay.maximum(var_5697.astype('uint32'), relay.reshape(var_5698.astype('uint32'), relay.shape_of(var_5697))) # shape=(7, 13, 3)
func_894_call = mod.get_global_var('func_894')
func_897_call = mutated_mod.get_global_var('func_897')
const_5716 = relay.const(3, dtype = "int8")#candidate|5716|()|const|int8
var_5717 = relay.var("var_5717", dtype = "int8", shape = (2340,))#candidate|5717|(2340,)|var|int8
call_5715 = relay.TupleGetItem(func_894_call(relay.reshape(const_5716.astype('int8'), []), relay.reshape(var_5717.astype('int8'), [13, 12, 15]), ), 0)
call_5718 = relay.TupleGetItem(func_897_call(relay.reshape(const_5716.astype('int8'), []), relay.reshape(var_5717.astype('int8'), [13, 12, 15]), ), 0)
output = relay.Tuple([bop_5699,call_5715,const_5716,var_5717,])
output2 = relay.Tuple([bop_5699,call_5718,const_5716,var_5717,])
func_5725 = relay.Function([var_5697,var_5698,var_5717,], output)
mod['func_5725'] = func_5725
mod = relay.transform.InferType()(mod)
var_5726 = relay.var("var_5726", dtype = "uint32", shape = (7, 13, 3))#candidate|5726|(7, 13, 3)|var|uint32
var_5727 = relay.var("var_5727", dtype = "uint32", shape = (7, 13, 3))#candidate|5727|(7, 13, 3)|var|uint32
var_5728 = relay.var("var_5728", dtype = "int8", shape = (2340,))#candidate|5728|(2340,)|var|int8
output = func_5725(var_5726,var_5727,var_5728,)
func_5729 = relay.Function([var_5726,var_5727,var_5728,], output)
mutated_mod['func_5729'] = func_5729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5517_call = mod.get_global_var('func_5517')
func_5519_call = mutated_mod.get_global_var('func_5519')
call_5826 = func_5517_call()
call_5827 = func_5517_call()
output = call_5826
output2 = call_5827
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
func_3917_call = mod.get_global_var('func_3917')
func_3918_call = mutated_mod.get_global_var('func_3918')
call_5847 = relay.TupleGetItem(func_3917_call(), 2)
call_5848 = relay.TupleGetItem(func_3918_call(), 2)
func_4912_call = mod.get_global_var('func_4912')
func_4916_call = mutated_mod.get_global_var('func_4916')
const_5857 = relay.const([-8,-10,5,-9,-1,4,-6,-9,-8,3,1,-2,8,-3,-1,-1,-7,-7,-2,-7,5,-10,-8,-10,-7,10,10,-3,7,1,6,1,5,-4,-6,-2,4,-10,9,9,-2,4,-10,-10,2,-8,-3,2,9,-5,-8,-4,6,-7,5,-3,-6,8,-1,-4,10,-1,-3,5,10,-6,6,3,7,9,7,-10,-8,-10,7,-1,-7,3,7,3,7,-8,-1,-7,2,-10,-7,-3,-7,5,8,-2,-10,7,3,5,-1,-3,3,-9,-5,7,9,8,-2,1,-10,-6,-10,-8,-5,2,-5,8,-4,-6,-6,-2,2,3,2,-5,-9,-3,-4,-1,-5,4,-10,9,-9,-3,-7,-2,-5,-2,-8,-1,7,-5,4,-9,3,-8,-6,-6,-3,10,6,-8,8,9,-8,5,2,-6,8,-7,1,-3,-2,9,-10,5,2,6,-5,6,-5,9,-2,6,-10,-2,-8,-5,-6,6,-7,3,-6,9,-5,-3,7,8,6,-1,6,-9,-10,3,-1,5,1,7,-8,9,3,-4,5,-2,-5,-9,-6,-5,3,4,8,3,-7,9,9,1,-1,4,6,-8,9,-3,-6,-3,6,-4,-9,8,-7,1,6,-10,6,2,2,-2,7,-7,-4,1,-10,-6,2,-4,2,9,-9,4,4,9,6,-6,7,-8,-6,2,-6,6,4,-8,-7,-4,-5,4,-4,5,4,-5,-7,-3,3,-2,8,6,-9,-8,-1,-5,-1,-6,-1,5,4,-8,4,-7,-1,-8,6,8,-10,2,-1,10,5,4,-8,-3,8,5,-5,1,-1,2,2,-3,-8,-8,1,8,-5,-3,-1,7,-6,-3,7,6,2,-5,7,9,-4,-2,-4,-10,3,3,-10,5,-5,6,10,-9,-9,9,4,-9,6,1,4,-10,-7,-2,3,2,6,9,-1,10,-3,-3,-8,3,-8,5,-10,-10,10,-1,-9,-3,2,-3,-10,-2,-2,10,-9,-6,-9,-8,10,5,2,-6,-10,8,-1,-6], dtype = "int64")#candidate|5857|(378,)|const|int64
call_5856 = relay.TupleGetItem(func_4912_call(relay.reshape(const_5857.astype('int64'), [3, 14, 9]), relay.reshape(const_5857.astype('int64'), [3, 14, 9]), ), 0)
call_5858 = relay.TupleGetItem(func_4916_call(relay.reshape(const_5857.astype('int64'), [3, 14, 9]), relay.reshape(const_5857.astype('int64'), [3, 14, 9]), ), 0)
output = relay.Tuple([call_5847,call_5856,const_5857,])
output2 = relay.Tuple([call_5848,call_5858,const_5857,])
func_5859 = relay.Function([], output)
mod['func_5859'] = func_5859
mod = relay.transform.InferType()(mod)
output = func_5859()
func_5860 = relay.Function([], output)
mutated_mod['func_5860'] = func_5860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mod.get_global_var('func_2260')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_5889 = func_2260_call()
call_5890 = func_2260_call()
func_1979_call = mod.get_global_var('func_1979')
func_1981_call = mutated_mod.get_global_var('func_1981')
call_5918 = func_1979_call()
call_5919 = func_1979_call()
uop_5926 = relay.rsqrt(call_5918.astype('float32')) # shape=(14, 10, 7)
uop_5928 = relay.rsqrt(call_5919.astype('float32')) # shape=(14, 10, 7)
uop_5949 = relay.acosh(uop_5926.astype('float32')) # shape=(14, 10, 7)
uop_5951 = relay.acosh(uop_5928.astype('float32')) # shape=(14, 10, 7)
output = relay.Tuple([call_5889,uop_5949,])
output2 = relay.Tuple([call_5890,uop_5951,])
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
func_2949_call = mod.get_global_var('func_2949')
func_2951_call = mutated_mod.get_global_var('func_2951')
call_5960 = func_2949_call()
call_5961 = func_2949_call()
output = relay.Tuple([call_5960,])
output2 = relay.Tuple([call_5961,])
func_5976 = relay.Function([], output)
mod['func_5976'] = func_5976
mod = relay.transform.InferType()(mod)
mutated_mod['func_5976'] = func_5976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5976_call = mutated_mod.get_global_var('func_5976')
call_5977 = func_5976_call()
output = call_5977
func_5978 = relay.Function([], output)
mutated_mod['func_5978'] = func_5978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_252_call = mod.get_global_var('func_252')
func_253_call = mutated_mod.get_global_var('func_253')
call_6000 = relay.TupleGetItem(func_252_call(), 0)
call_6001 = relay.TupleGetItem(func_253_call(), 0)
output = call_6000
output2 = call_6001
func_6006 = relay.Function([], output)
mod['func_6006'] = func_6006
mod = relay.transform.InferType()(mod)
mutated_mod['func_6006'] = func_6006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6006_call = mutated_mod.get_global_var('func_6006')
call_6007 = func_6006_call()
output = call_6007
func_6008 = relay.Function([], output)
mutated_mod['func_6008'] = func_6008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_6039 = relay.TupleGetItem(func_376_call(), 0)
call_6040 = relay.TupleGetItem(func_377_call(), 0)
func_5435_call = mod.get_global_var('func_5435')
func_5439_call = mutated_mod.get_global_var('func_5439')
var_6042 = relay.var("var_6042", dtype = "float32", shape = (1, 1694))#candidate|6042|(1, 1694)|var|float32
call_6041 = relay.TupleGetItem(func_5435_call(relay.reshape(var_6042.astype('float32'), [11, 11, 14]), relay.reshape(var_6042.astype('float32'), [11, 11, 14]), ), 0)
call_6043 = relay.TupleGetItem(func_5439_call(relay.reshape(var_6042.astype('float32'), [11, 11, 14]), relay.reshape(var_6042.astype('float32'), [11, 11, 14]), ), 0)
var_6045 = relay.var("var_6045", dtype = "float32", shape = (2, 1694))#candidate|6045|(2, 1694)|var|float32
bop_6046 = relay.greater(var_6042.astype('bool'), var_6045.astype('bool')) # shape=(2, 1694)
func_1979_call = mod.get_global_var('func_1979')
func_1981_call = mutated_mod.get_global_var('func_1981')
call_6050 = func_1979_call()
call_6051 = func_1979_call()
func_181_call = mod.get_global_var('func_181')
func_183_call = mutated_mod.get_global_var('func_183')
call_6052 = relay.TupleGetItem(func_181_call(relay.reshape(call_6050.astype('float32'), [14, 10, 7])), 0)
call_6053 = relay.TupleGetItem(func_183_call(relay.reshape(call_6050.astype('float32'), [14, 10, 7])), 0)
output = relay.Tuple([call_6039,call_6041,bop_6046,call_6050,call_6052,])
output2 = relay.Tuple([call_6040,call_6043,bop_6046,call_6051,call_6053,])
func_6062 = relay.Function([var_6042,var_6045,], output)
mod['func_6062'] = func_6062
mod = relay.transform.InferType()(mod)
mutated_mod['func_6062'] = func_6062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6062_call = mutated_mod.get_global_var('func_6062')
var_6064 = relay.var("var_6064", dtype = "float32", shape = (1, 1694))#candidate|6064|(1, 1694)|var|float32
var_6065 = relay.var("var_6065", dtype = "float32", shape = (2, 1694))#candidate|6065|(2, 1694)|var|float32
call_6063 = func_6062_call(var_6064,var_6065,)
output = call_6063
func_6066 = relay.Function([var_6064,var_6065,], output)
mutated_mod['func_6066'] = func_6066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6006_call = mod.get_global_var('func_6006')
func_6008_call = mutated_mod.get_global_var('func_6008')
call_6091 = func_6006_call()
call_6092 = func_6006_call()
func_2949_call = mod.get_global_var('func_2949')
func_2951_call = mutated_mod.get_global_var('func_2951')
call_6105 = func_2949_call()
call_6106 = func_2949_call()
output = relay.Tuple([call_6091,call_6105,])
output2 = relay.Tuple([call_6092,call_6106,])
func_6107 = relay.Function([], output)
mod['func_6107'] = func_6107
mod = relay.transform.InferType()(mod)
mutated_mod['func_6107'] = func_6107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6107_call = mutated_mod.get_global_var('func_6107')
call_6108 = func_6107_call()
output = call_6108
func_6109 = relay.Function([], output)
mutated_mod['func_6109'] = func_6109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2986_call = mod.get_global_var('func_2986')
func_2987_call = mutated_mod.get_global_var('func_2987')
call_6121 = relay.TupleGetItem(func_2986_call(), 0)
call_6122 = relay.TupleGetItem(func_2987_call(), 0)
func_4413_call = mod.get_global_var('func_4413')
func_4415_call = mutated_mod.get_global_var('func_4415')
call_6126 = relay.TupleGetItem(func_4413_call(), 1)
call_6127 = relay.TupleGetItem(func_4415_call(), 1)
func_75_call = mod.get_global_var('func_75')
func_76_call = mutated_mod.get_global_var('func_76')
call_6159 = relay.TupleGetItem(func_75_call(), 0)
call_6160 = relay.TupleGetItem(func_76_call(), 0)
output = relay.Tuple([call_6121,call_6126,call_6159,])
output2 = relay.Tuple([call_6122,call_6127,call_6160,])
func_6162 = relay.Function([], output)
mod['func_6162'] = func_6162
mod = relay.transform.InferType()(mod)
mutated_mod['func_6162'] = func_6162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6162_call = mutated_mod.get_global_var('func_6162')
call_6163 = func_6162_call()
output = call_6163
func_6164 = relay.Function([], output)
mutated_mod['func_6164'] = func_6164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4576_call = mod.get_global_var('func_4576')
func_4577_call = mutated_mod.get_global_var('func_4577')
call_6174 = relay.TupleGetItem(func_4576_call(), 0)
call_6175 = relay.TupleGetItem(func_4577_call(), 0)
func_1451_call = mod.get_global_var('func_1451')
func_1454_call = mutated_mod.get_global_var('func_1454')
const_6177 = relay.const([[-0.521446,9.537139,1.229099,-1.995867,7.970821,-7.679224,-7.020978,5.439487,7.074260,-5.678634,9.729253,7.736638,-1.394900,4.453062,-7.446162,-4.453360,-7.612338,6.411560,-4.988302,-4.776130,9.644522,3.387039,-1.317467,1.465323,1.877618,-5.608643,5.892974,3.100305,-0.160728,4.517727,4.919554,6.930224,7.523057,1.842371,-9.634830,7.317620,-0.745450,7.994048,9.007103,-4.804618,6.522950,5.011859,1.364594,-2.706032,1.656844,-5.447847,-9.040891,-7.612460],[-7.785165,8.816256,3.024944,-1.400994,8.253957,-6.323432,4.265267,4.583552,8.758183,7.908249,1.037287,-7.422502,3.432496,6.159635,6.407279,6.255699,6.485830,-4.750973,5.232102,2.988638,2.580027,0.079014,-4.273369,5.788770,3.878514,-1.465742,-4.470560,5.451321,6.290525,3.818706,-1.181453,-5.020001,8.982493,-0.324758,-2.892265,4.351006,-9.550401,-5.274470,6.792063,-5.212892,-6.639165,-1.138076,-5.655241,5.389948,-1.458294,-0.812977,2.905589,5.848090],[1.889939,-7.725911,7.686785,7.597546,-3.025212,-6.803048,3.105301,0.157354,-0.538978,9.559687,0.710740,-3.552546,6.750053,6.750849,-9.258080,-2.916294,-0.845002,3.701118,-8.041738,9.463470,-3.942426,8.604908,7.837025,4.969516,-3.920155,-9.077356,8.245125,0.010394,0.249217,-8.119666,2.581311,3.802319,3.357159,7.030045,-4.433613,-3.027599,4.804571,-0.238725,-0.738987,-5.043311,-1.797369,7.957762,7.061964,8.012510,6.346956,-7.182215,-5.011534,-6.904503],[-4.408024,8.342138,7.670160,8.594286,0.995770,5.049844,-1.317661,-3.729005,-4.213568,-8.151085,9.288109,-4.520561,3.726163,9.515524,-4.633692,1.105657,-1.710664,6.924052,2.498358,-8.471871,8.820323,-3.905936,6.817810,-7.949230,-0.397763,9.918917,-0.723936,-7.377336,5.076173,5.871166,-5.131163,-4.787995,-5.404362,-0.482723,0.840266,-3.393676,-8.204998,-5.806498,-8.505971,4.667909,1.322615,-7.095682,-9.631484,-2.590171,-2.585085,8.722842,-5.099626,5.119912],[-4.028900,-0.749857,-9.173547,-1.191744,-9.175455,-2.128218,0.702616,2.492428,4.566866,6.943488,5.249528,5.005799,1.379986,-9.733572,-2.037947,-3.635091,6.743998,-0.573426,-8.294790,-3.737524,2.357657,6.090768,-5.872302,-6.017566,-6.758084,2.407948,4.913129,0.071118,5.028396,-8.289896,-4.179271,-0.515837,-3.990852,6.272493,7.013059,4.628449,5.220470,-8.640775,3.505025,7.536528,-5.238901,0.611513,8.345112,-5.200116,-6.737546,-4.797946,-1.349367,-2.351836],[-7.045256,4.621585,6.517491,-8.279585,0.371423,-2.518258,6.832299,-7.856327,-4.813196,0.884768,-3.696969,7.420848,3.173393,4.677716,-6.624244,-6.620064,-4.870017,6.167636,-4.526163,-9.610717,-6.718078,-2.239737,-6.010229,5.590780,5.814087,-4.211946,-9.988171,-7.879877,7.097480,4.482985,-0.685090,-6.694536,3.768769,-7.455693,-4.754616,5.540195,-3.586398,-1.151834,-0.508307,8.898547,3.007303,-1.105548,8.658242,3.511898,-8.053119,5.259136,-1.694987,0.601757],[5.493707,4.170927,-0.614683,-9.959827,-0.254632,1.495029,-2.423020,-4.005303,-5.900332,8.361203,-5.263665,9.110599,-6.152696,0.990120,-5.364526,-2.853666,-1.407767,4.698612,4.362985,4.493678,3.312050,-1.766011,-8.664022,5.894563,0.014212,-5.803023,6.259932,7.417101,-0.062400,-8.027937,8.735276,-6.022240,-9.236870,4.131191,0.385313,0.070260,0.603975,-6.845640,9.906721,7.874129,7.790885,-2.757963,8.601700,-5.954713,-8.137232,-2.432869,4.801394,1.786098],[3.805079,2.635760,-2.745877,7.131507,7.729590,6.219511,9.492574,7.083062,-4.899175,5.689239,8.072019,-2.799425,-4.271789,-4.181422,4.272665,7.576866,-3.359385,-7.825144,7.969723,-5.646504,3.860462,9.695440,-3.655009,7.118610,-8.638472,-2.577068,-0.130634,9.277548,-9.301551,9.501814,-6.779740,-6.557777,4.694383,6.609676,-7.527634,0.190094,4.735972,-7.494238,-9.749148,-4.675343,-5.961112,-4.299225,9.493061,1.861938,2.674123,-8.658042,7.401060,-6.005734],[7.633277,2.340485,-5.782839,7.209746,-1.604253,5.617018,-3.854093,5.954720,1.533402,7.158658,-7.724859,-5.661865,8.479872,3.180505,0.170491,-9.032642,8.103880,-7.536402,-8.373832,4.232121,3.745859,3.305802,-2.435742,-6.455784,1.686067,5.024152,-9.868321,5.100949,-0.176746,-5.491555,1.488831,-9.320680,-8.158100,-9.327280,-3.784261,5.796347,-3.518836,4.776869,-6.240048,-9.506805,-9.704596,2.717078,5.335280,-5.154195,8.019297,4.894052,3.304818,2.833343],[-5.309792,9.438113,2.344402,-5.947690,1.460156,-7.894709,1.466303,8.831823,-1.796329,-5.104485,-5.212486,7.714424,7.973116,-8.625288,-4.591175,3.400635,2.659344,-6.825226,6.598251,-9.998999,-5.518900,-0.061064,-2.568124,9.630715,-8.319006,-5.934410,9.496105,-2.848808,1.933855,0.572259,-7.098024,-9.278970,9.072938,-9.079531,-6.901011,-1.911064,-5.527001,-4.838669,-0.280177,8.223177,-2.902202,8.672916,-1.627294,-5.802933,-7.683249,4.758082,-4.351087,-9.977147],[-5.669042,3.468413,-4.545365,-1.669120,-4.225429,0.063522,-2.026828,-3.871694,-6.459899,-0.747088,8.888828,-0.574711,8.361142,3.543795,-9.376349,3.038450,-3.242418,1.522431,-6.045269,2.818007,-5.111200,-7.005174,-1.180947,7.130643,-6.165971,7.583567,4.572041,-7.394680,4.462350,-0.089812,2.205637,3.660904,-2.093791,-2.993243,-4.445385,-4.094965,-8.873358,7.372378,7.724339,-3.020792,9.077393,9.520800,5.432342,7.901809,4.547214,-3.454965,8.256579,8.315460],[-5.880031,5.333774,5.406406,-9.352000,-6.543981,-8.226618,-3.420540,5.921726,-0.634794,-7.943620,-5.488637,9.348676,-6.792049,2.723480,0.191289,9.206936,-1.938279,-6.040839,-0.323038,-8.121172,-0.069146,-4.808420,6.933802,-7.007916,4.436414,4.174027,-7.339728,6.126524,5.896870,5.456142,6.796823,-1.052674,9.952336,-0.107870,5.075488,-0.248682,7.571557,6.130711,-2.873063,4.007291,-9.217016,-4.291947,6.585923,9.144982,-7.539205,9.160384,-2.521875,9.748473],[-9.438814,5.408639,-0.237951,7.980187,9.023289,-5.547599,2.944095,0.483406,1.563347,-3.809740,9.988118,5.653320,-0.519590,-5.472648,-7.399985,-1.330595,2.357381,6.172974,7.926287,9.290904,3.147668,7.270551,1.549382,-4.223632,-8.114297,2.178014,2.868542,6.981655,6.190241,-8.298359,2.657123,-7.812827,-9.555442,5.558771,1.176486,-0.760114,-0.092361,9.188568,-6.172195,-2.349798,-4.135298,8.390801,-5.725648,-3.796676,-4.817492,-4.356006,7.663214,-3.622765],[-7.615903,-5.897560,-0.626243,-5.883107,-6.950517,8.166788,3.440870,7.370664,4.272694,9.332296,1.957879,-9.405857,-4.931417,4.330584,9.609104,-3.378719,6.476752,7.204664,7.351498,1.564251,3.472527,3.159258,-6.506189,2.706768,5.433792,-9.461691,-5.567902,-7.923042,8.096397,-0.151186,1.404262,-0.579379,6.976082,-7.786478,2.007198,-0.448077,-3.776700,0.182020,-4.035147,0.470459,-8.996608,-6.054027,-5.124910,7.250004,3.865018,-0.912634,-8.598420,2.573160],[5.652033,9.501448,8.737864,0.944002,3.688060,2.471133,6.776974,2.672408,-5.033727,-2.647320,-1.203739,-1.085241,-5.302143,-8.326745,6.582663,-9.652913,7.965532,5.266439,-1.385542,0.705953,3.605925,3.306671,8.742602,-2.164304,8.521136,-1.176346,8.059971,5.487466,0.737261,-7.725398,8.781947,2.958268,-9.750551,-0.704554,-4.043365,-1.539536,-8.545886,-9.446653,-6.024577,8.166336,-8.427815,8.834825,-4.267808,1.599643,-9.750174,-7.379308,-8.607930,8.099090],[-7.703019,2.707751,7.521552,-2.678779,-9.325275,4.543264,-4.196100,-8.337755,-2.907710,-9.743669,-9.249578,-4.927349,9.577088,-8.908379,3.197423,1.443256,5.585732,-9.472193,-5.037360,-3.263161,1.377677,-0.645817,-3.185659,-8.846844,-9.411517,1.769473,-8.358969,-1.879925,-6.008553,-2.934497,-6.385441,4.992712,-0.871855,-7.674088,6.333398,8.105659,-5.007829,-3.864458,-4.099473,5.538485,6.693215,1.220294,-3.458025,2.769326,8.524256,-5.815672,8.733197,2.058161],[7.780752,6.517126,4.653803,-5.597707,-2.265362,-0.182953,3.384627,7.061634,4.789072,4.894478,-0.998291,-9.905298,-4.443828,9.983714,4.673086,1.703179,-0.881754,2.922539,-1.577497,0.785346,-4.779211,7.748928,4.247490,-6.194529,-0.372743,5.062073,-0.823241,-9.719908,-9.040960,9.392307,-7.803349,8.195116,6.238213,-8.086208,-2.169713,-0.702099,-2.912287,-6.302854,-9.083689,-9.062387,-4.553531,-2.116340,2.259360,7.868581,-7.809047,4.742720,-0.301452,-3.588890],[8.890802,2.462020,-3.980988,-8.295837,6.591084,1.795145,4.182103,-0.040716,8.088074,8.990657,2.755651,-7.232253,8.844822,7.542580,-5.985054,3.648301,-2.387539,2.384447,-3.503873,1.650340,1.298050,5.222074,-7.359626,-3.480601,-3.310484,2.796937,5.567111,-7.275610,8.132127,-9.087786,4.472119,-6.798315,-6.841039,-3.544278,0.829534,-6.589171,-2.609964,-2.020322,-9.671531,-0.569975,-1.641535,-0.437858,-8.940819,-8.934891,-9.253934,4.791307,-3.843807,-2.516255],[-8.766612,3.789101,-9.807761,-8.360456,5.304831,-5.382135,8.625689,8.513920,-0.427819,5.747137,-7.541159,-9.350019,-2.885305,-6.192012,5.956595,8.867097,4.943719,-4.418945,5.712195,5.336818,2.150245,-2.389961,-6.421252,-0.202748,0.184066,5.879719,7.261881,6.049463,-4.670877,-9.968798,-8.672159,7.885768,-7.866597,9.257170,-3.520459,-4.278112,-8.569364,-8.132991,-6.905576,5.038842,3.871957,0.879571,6.840224,-3.184221,-3.959232,6.075110,2.251586,2.346698],[-3.288090,1.572119,7.014882,-8.450226,-0.912345,-4.935168,2.792249,-3.020140,8.102727,9.442175,-5.415173,-8.225672,-3.349709,6.817235,-8.038846,9.777161,-2.489854,2.609997,3.255065,6.040297,-7.805757,-5.795933,-2.134059,-6.376128,8.483273,-2.111410,-7.415831,-9.092124,-6.009038,-5.824160,-5.146668,-9.445002,-0.293051,-8.373269,7.322231,9.762575,-6.925104,-3.720313,-3.798086,-6.126485,-1.540859,-8.772531,5.840595,-5.251479,-8.019838,-9.339330,-7.986850,4.387686],[-3.624625,-5.105573,-1.653638,3.611056,-6.623810,8.417471,3.046924,-3.611519,-6.469803,-7.262443,9.613131,3.284321,5.525127,0.311969,-9.175091,-9.480163,-8.414754,2.802864,-1.479888,4.438193,-3.037761,6.542769,-1.700088,6.616171,-7.756490,-1.679854,-7.805202,-3.908437,5.297291,-2.112148,-7.367083,-3.037492,6.862608,9.879016,8.645572,-4.378495,9.683066,6.625142,9.841882,-4.121036,-1.928149,-6.029496,0.626239,-8.239062,-3.152691,-6.180706,9.900140,1.306587],[-0.005722,-7.032766,-6.235918,3.603044,-9.337086,3.219593,-6.214290,-3.217688,4.600568,8.035343,8.956068,8.139372,-0.459033,-9.473630,6.279695,1.553178,4.885680,0.102311,-6.672125,6.235264,5.535554,3.102560,9.609117,-4.820997,-6.591157,7.381582,1.503470,7.561719,-4.858297,1.585291,6.009847,-3.826050,-9.336054,-2.190955,-8.465549,4.873159,4.134993,1.789668,-9.168285,2.096861,-0.571378,-8.968817,8.241219,6.034840,-3.157331,1.761094,0.942072,-3.151226],[3.348075,5.320975,-9.244640,4.633274,6.525208,-0.800692,-3.332771,-2.250376,-8.773371,-0.545008,-7.303189,-4.242343,-4.076968,-2.231056,8.454435,7.114847,-1.052347,-6.525847,-8.286204,-1.620350,0.317062,4.114897,-5.679179,-0.905322,9.811174,-6.455157,-9.419322,-7.899372,2.169707,8.839838,9.755666,4.151898,1.589969,-8.557969,-4.869928,2.095103,-2.029826,4.695508,-8.087295,2.288276,7.541544,5.167345,-0.653828,-1.022477,-3.470703,-3.574028,0.976309,3.329593],[-6.583553,-3.901446,-8.036080,-2.457258,-6.900167,2.892173,3.005238,-4.097902,6.076539,-1.461885,9.551056,7.553005,-9.859589,3.853682,8.588286,-7.266217,1.409532,-0.518884,-6.997684,-5.270142,7.187317,3.280045,-4.695622,9.104335,4.417661,-4.540245,-9.732014,7.654294,6.669327,-7.265052,0.195650,-8.045685,7.066233,2.162577,6.971791,8.784830,4.258912,3.176483,-3.956496,5.098790,2.976098,6.754351,9.683484,-1.635189,6.990066,-8.285109,-5.534546,3.525927],[1.788726,0.507189,-3.156202,9.522820,-6.868164,-0.551441,2.782324,-7.401928,4.818228,8.875611,-0.760133,5.660159,-7.364742,8.450690,3.227530,4.949372,2.407227,9.313066,6.010636,8.904468,-3.664823,-9.345185,-3.277801,-4.520644,-6.258696,-1.051556,5.250110,4.170690,1.727401,-9.489026,7.769251,-4.842822,0.314367,3.738102,-0.440645,-1.662112,-8.827725,3.192379,7.773239,-3.468905,9.934919,0.205443,-2.311378,-5.313612,2.420132,-0.930711,-3.220546,9.666528],[7.114876,-5.890431,3.500667,-0.899638,-9.690309,-8.780657,9.352480,9.800159,-4.582785,5.728125,5.565860,-9.689643,9.222520,-1.755070,3.396908,9.332885,-0.988548,9.824603,-3.553721,9.231962,3.088822,-3.373161,-7.091101,9.857276,-5.669825,3.246468,-4.812722,-4.342456,7.763571,-9.019881,-4.857457,1.013092,5.495085,7.778400,-5.512694,-2.902987,-7.023040,-6.376857,6.266766,1.199063,-1.998265,6.507097,8.137713,-6.959228,-3.705814,1.014739,-9.396065,7.765479],[4.847648,0.388573,7.187203,7.303559,7.604232,-0.625834,3.740249,-6.835575,7.337617,4.463574,-8.877654,7.528320,-9.922287,3.361549,7.642500,-3.001248,9.333690,-4.046065,-7.824976,8.528936,1.806923,-1.060027,8.559312,-6.864861,-7.783413,0.815239,-7.292917,-9.663086,-6.278825,0.724957,-1.147718,-3.190462,-2.279313,9.585836,4.343541,-5.512566,-1.729174,0.136420,7.473061,-1.551488,1.945695,-7.024809,-2.149558,-4.571801,2.541526,-8.644615,-4.445708,6.453353],[7.325109,3.783330,4.270081,0.503165,-2.027747,-0.871386,0.010650,3.564417,-6.892025,-7.431691,-9.035828,7.981276,-3.759366,-3.166271,9.634656,8.489471,-0.280512,7.237672,-8.484734,0.272262,6.053843,4.662496,1.630478,-8.750466,-9.943979,-8.819949,3.490561,-7.516723,-6.848093,-0.122980,5.904335,-1.711704,-7.486047,9.241773,3.530790,7.252674,-4.446095,7.825920,-6.857913,-4.139266,-8.906214,5.817986,-4.420664,3.130736,-9.454005,-3.481564,-2.503638,3.209402],[-7.896275,9.181368,-4.099953,3.227409,6.471880,-2.631277,-2.951050,1.827434,3.659551,-8.009806,-8.640905,-6.069815,-8.993474,-5.465527,-6.569964,4.316321,7.337918,-3.204999,-2.962102,-9.669332,-0.210384,8.587482,1.745268,7.944685,9.265950,6.067988,0.834027,0.950827,-8.084789,-4.811097,1.338119,-8.767104,9.204843,-6.073692,-8.714874,1.420845,5.482271,1.507668,4.602271,-2.784012,-8.714633,5.566428,2.547733,1.933284,-7.721986,-4.556878,-2.473149,-3.664460],[3.577715,4.661860,-5.803365,-6.730359,1.806271,-5.465235,-8.601876,6.913928,-0.631298,3.555334,1.521907,-2.689133,-4.332220,-4.704194,1.116041,-5.586807,5.537221,-9.186098,9.130731,-9.811252,-4.429174,8.614781,8.609630,6.527371,6.717339,9.332776,-9.549095,9.053282,9.272136,2.159670,-4.816422,3.304708,9.218440,1.679770,1.931652,8.158730,3.040323,-6.572597,5.242626,-8.523314,-3.561299,-4.729196,3.952422,-5.974209,0.402088,5.572775,2.498113,1.744685],[-3.748494,0.801481,-9.655582,8.665223,-1.621882,-0.067221,-6.735738,-8.075509,2.635885,5.111357,-9.894903,6.643398,7.436387,-3.249822,5.642380,3.649690,-2.265965,9.403021,9.117573,-4.973872,9.684747,9.796245,-0.552419,-5.509666,-4.080180,-5.931925,7.251009,-6.976392,7.065841,-2.501994,8.725398,-7.768235,-4.648276,-7.182458,3.688976,8.968611,-2.558184,-5.583133,7.488369,-0.671933,-1.672423,-8.027407,-8.304136,-4.397196,7.266996,-5.044520,-7.560948,2.554346],[4.064918,-3.345787,-3.611133,4.635120,-2.866027,8.371015,-0.505717,-3.624139,0.195513,8.965478,3.064102,2.470318,-6.959100,6.528581,-2.442360,7.740402,5.953289,-0.813447,-8.334443,-5.818951,3.893769,-4.480338,1.942781,-0.953716,6.855407,-9.316206,0.763247,-7.763174,7.921881,-9.712730,-2.707412,9.191643,4.771113,6.957591,8.023866,1.795332,-4.314150,0.257743,-0.711383,-8.018114,8.966702,-2.117536,-2.781166,-5.604767,3.404269,9.932866,-0.117765,5.686088],[5.952794,1.408726,-8.694650,2.049274,-0.931191,-8.226019,8.430495,6.523860,2.684254,6.752638,-7.012409,5.219759,9.808275,1.184482,-4.005769,7.410103,1.337941,-0.870693,6.366674,-4.332158,-7.486433,-4.859348,1.165090,-1.952158,-4.016036,-8.997203,6.847716,-6.836757,4.969153,3.010482,-8.314565,1.277178,0.192617,9.943467,3.122477,6.982420,-7.758279,6.531386,7.867434,-2.066697,-3.289966,-9.584253,-4.649943,-8.089729,-1.333083,8.350759,-4.351365,-9.049218],[7.253170,8.360590,-5.967695,-7.242174,-2.444588,-7.271162,-1.887118,9.105637,-5.644607,-3.207937,-8.490279,-6.705826,-3.275471,6.243339,-3.483193,4.714085,9.805173,-6.207650,1.453938,-9.508371,7.038737,8.357680,7.048679,-9.439514,-6.340158,0.880692,7.591613,2.500059,8.954105,-3.664151,-2.960252,9.693573,-9.949403,1.232615,8.995493,-7.457135,1.903545,-9.020977,-0.068534,-2.170409,9.734134,-7.533412,8.339113,1.178066,-6.252093,-3.235376,1.490231,4.790087],[6.163162,8.885888,-6.158156,9.577711,6.874444,1.677542,-3.866126,-7.127936,6.478040,-0.214584,-1.466814,3.081661,-3.479707,6.730691,-7.677895,7.777157,-6.317454,-8.515297,-0.893773,-9.715809,0.026792,-1.351705,4.519541,1.395724,0.614792,3.618089,6.888304,-7.995371,-1.006698,8.223417,-0.822619,-9.550160,3.795640,-0.678658,0.908808,2.945386,-5.811995,-9.143274,-5.526766,-9.992718,-1.008464,6.898514,-0.334793,6.277549,-3.669551,7.021070,5.014931,3.410515],[-0.021845,2.897748,-6.987703,-8.251794,-9.352051,-1.873764,6.185843,-8.462416,-3.141722,8.904467,1.236087,9.819301,-8.515856,0.090224,-1.083492,-7.372722,-9.935897,-4.156114,5.878484,4.503326,-5.128963,-4.541292,-2.442578,2.648374,1.218065,7.967217,0.314492,-4.347686,-4.091484,2.290622,-2.806799,8.486344,3.021935,8.857720,1.942729,-3.708823,-8.346492,3.303258,3.187543,6.272682,1.834181,-8.563859,7.458176,-1.400513,-4.500789,-5.133958,-8.273989,9.616421],[-2.068115,-0.594223,7.961904,5.631558,3.785858,-2.699465,0.527727,7.628295,-5.874400,6.779555,-9.608951,5.079109,8.473672,3.196940,-6.277817,-9.049149,7.032018,-8.059327,6.071232,-4.106073,-5.195803,-7.425474,-7.840638,-5.372784,0.610828,-9.837237,-4.021664,-9.120569,-5.882601,0.371420,-6.427169,3.125829,-6.454773,-8.889022,7.970912,-9.030196,0.587594,8.941833,5.020714,-3.947503,0.094419,-5.194217,5.450782,3.244829,4.228655,-4.343080,-0.719662,8.319471],[0.166080,1.024090,6.540853,-5.783188,-8.693803,-9.313097,3.010050,-8.294658,-5.097059,-4.316949,2.773899,0.056534,-2.672629,-7.929698,3.371040,4.973339,4.259219,6.451205,2.216760,7.708177,1.285175,0.526049,-5.266140,1.412026,-8.634161,-1.865326,4.083831,-3.048760,3.721235,0.698657,5.454652,8.306780,1.949245,1.197475,-1.801948,-5.722751,-6.357071,4.891931,1.597549,4.454244,-0.865849,6.235506,0.597183,-2.049739,-5.709872,7.074255,-3.877698,-9.309247],[6.156705,-2.677214,-5.190528,1.333202,-8.750888,5.749157,5.370886,-2.511728,0.046319,-6.254995,9.911622,7.566198,-1.496430,3.098897,-7.572057,-8.087025,9.159858,4.481113,5.348556,5.875967,2.138003,7.931080,9.011414,4.790152,4.895637,-1.813550,-7.291326,-4.956941,-6.143057,8.588384,6.356766,7.303758,9.677104,-6.365629,2.663999,-1.698417,-0.448323,-8.885822,0.366872,-5.497625,4.954045,-3.739897,0.597803,-8.760594,-3.433150,-9.045109,4.826828,0.677909],[-8.761876,3.456370,3.350689,1.977801,4.633571,2.298773,9.401496,8.110512,-0.727289,-1.354479,-8.728700,-8.239836,-6.124961,-0.252936,-7.308218,-2.139969,0.972038,-1.888149,-8.600599,-8.941685,6.119534,-2.604554,-2.750268,4.309007,9.853700,-9.600794,-5.841650,1.271203,1.038469,-6.929727,4.901917,-5.683815,-2.189383,3.393313,-5.471002,-8.059510,2.538819,-3.503550,-9.315654,4.311772,3.009696,0.484522,-6.959260,4.085931,-2.759587,9.724710,-4.062243,-4.825710],[-0.192473,7.298687,-4.928161,4.458686,1.992064,9.379024,2.347192,6.515286,-2.051987,2.214531,5.161104,-1.014770,-7.300502,8.405487,3.847268,-5.085732,7.100344,5.991483,3.447115,-1.381701,-4.439788,9.969532,-9.677970,8.853376,5.539220,4.021267,0.465636,3.770733,2.744610,-8.567796,-2.284362,-8.303489,0.180525,6.436978,-6.158087,8.417209,9.378944,1.602256,5.694307,-2.296846,5.407541,-0.921433,6.113712,-3.876366,-6.095077,-0.605582,5.631035,7.536923],[-6.046487,-3.809197,-5.772592,7.547968,-1.230577,8.967134,9.187433,-1.587271,9.960868,4.207743,-4.676995,7.349110,8.704992,-7.522636,-6.714733,9.709305,-4.327023,-6.571195,8.622910,3.174163,-0.901292,7.482946,-3.439912,-4.384527,-4.244214,6.964568,7.553248,-9.647976,-8.890789,-5.133718,-7.332600,4.455007,1.780776,4.098407,8.306772,-4.157992,8.662159,-9.237616,2.126604,0.485093,-0.575506,3.736673,0.264103,-2.289870,-8.152190,-4.164950,-9.340871,6.256725],[2.658446,-0.561900,7.127864,-5.190709,1.199665,1.113078,9.728203,-4.925089,6.011686,-5.349291,0.954126,-8.607565,3.671544,-0.994959,-6.098535,7.508866,-8.742643,-0.122513,-2.229223,-9.407452,6.354190,-5.365546,-9.817579,2.157200,-7.004180,-3.752842,-1.014117,7.276199,-4.994333,-4.447422,-3.086068,-6.205213,8.186251,-1.092949,-0.262529,4.569880,-9.668517,-1.039679,8.002682,-2.573016,2.953301,1.240140,2.113100,6.088307,7.158093,-1.339473,5.478220,-7.461480],[-4.268633,-2.664452,-4.766758,-0.362562,-1.955567,0.157278,-2.395571,6.381478,6.355494,-9.961301,-9.014558,-7.109802,3.145602,0.237746,1.435446,1.007508,-8.974187,-9.247320,-9.114050,-1.929743,-9.023300,-9.086869,9.367033,-2.691597,-6.565536,-1.548530,0.179679,-4.879474,6.280733,7.942786,-0.339746,-2.684229,7.131133,9.585875,-2.890522,-4.246956,6.655489,4.156803,-4.313516,1.283039,-9.741592,5.224780,-3.410009,-6.191299,3.893576,9.684918,7.764452,0.105197],[-3.634658,-6.753410,-9.211951,7.702269,7.680439,-4.342380,3.054934,-9.428211,7.212387,3.906234,-0.451883,-6.245253,9.071692,1.796084,8.254449,0.477765,5.397942,-5.788708,-7.630156,3.102562,5.848123,-8.163235,-4.559835,-4.238783,-6.598449,4.521129,-6.051920,0.677724,1.076805,-7.727911,7.352495,0.192270,4.332425,-3.326353,3.820802,0.461400,4.450279,3.752568,-5.494739,-8.668939,6.717880,6.216251,7.036502,-9.201603,3.611898,4.109312,-7.120954,4.594603],[5.697772,-7.329605,-2.712845,3.331938,3.209453,6.716804,-8.980197,-4.436899,2.299959,4.391260,-7.265041,-7.206780,-5.670438,-4.135038,-4.439675,-1.857609,3.871892,-5.052727,-0.433392,-8.993654,9.160730,-6.810333,1.171378,2.056050,-8.663623,8.180649,-0.975058,0.667326,1.091245,-4.653046,2.716983,2.769132,5.955303,-0.716957,7.400459,4.841195,-4.746539,7.344894,-8.172737,3.194188,4.299989,-1.181555,-5.028620,0.721904,1.372398,9.741256,-5.763040,-9.092730],[-8.405659,-9.672791,4.918775,-8.238884,0.480908,9.762036,7.624515,-7.117901,1.939818,-5.336415,-3.897987,0.791802,1.406535,9.519438,-1.607083,0.714513,-2.845432,-9.674704,2.969499,-6.153954,-8.649699,0.557133,-2.665805,0.782348,-4.152485,8.058309,2.576050,-3.062338,2.876637,-1.711400,1.922862,-1.680767,1.417899,0.361279,-3.521484,9.205191,2.776771,-0.250935,3.332566,8.028236,1.440186,-0.916677,-7.702637,-0.014841,-4.315356,3.268360,-1.594518,-6.050597],[-1.617818,9.946323,7.017538,-6.508824,5.522736,-5.836879,-3.530051,-3.756214,-9.417425,-2.192940,5.151218,-6.294845,0.247069,-6.133253,2.008021,-5.749054,-1.776489,-5.959266,-6.800469,1.903265,7.245429,-1.702427,3.460214,-5.169186,-2.009409,-3.005995,6.586793,0.759764,-7.061156,-6.285820,-1.051628,-5.097568,-4.787200,-6.767935,3.349831,-2.502334,1.231042,-6.636424,1.980234,-1.909348,2.864963,-8.650214,7.331429,0.191681,1.121084,-1.374363,-2.314600,-1.560504]], dtype = "float32")#candidate|6177|(48, 48)|const|float32
call_6176 = relay.TupleGetItem(func_1451_call(relay.reshape(const_6177.astype('float32'), [12, 16, 12])), 0)
call_6178 = relay.TupleGetItem(func_1454_call(relay.reshape(const_6177.astype('float32'), [12, 16, 12])), 0)
uop_6185 = relay.erf(call_6176.astype('float64')) # shape=(12, 16, 12)
uop_6187 = relay.erf(call_6178.astype('float64')) # shape=(12, 16, 12)
uop_6196 = relay.sigmoid(const_6177.astype('float64')) # shape=(48, 48)
func_3443_call = mod.get_global_var('func_3443')
func_3445_call = mutated_mod.get_global_var('func_3445')
call_6203 = relay.TupleGetItem(func_3443_call(), 0)
call_6204 = relay.TupleGetItem(func_3445_call(), 0)
output = relay.Tuple([call_6174,uop_6185,uop_6196,call_6203,])
output2 = relay.Tuple([call_6175,uop_6187,uop_6196,call_6204,])
func_6207 = relay.Function([], output)
mod['func_6207'] = func_6207
mod = relay.transform.InferType()(mod)
output = func_6207()
func_6208 = relay.Function([], output)
mutated_mod['func_6208'] = func_6208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5566_call = mod.get_global_var('func_5566')
func_5567_call = mutated_mod.get_global_var('func_5567')
call_6227 = relay.TupleGetItem(func_5566_call(), 0)
call_6228 = relay.TupleGetItem(func_5567_call(), 0)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_6230 = func_947_call()
call_6231 = func_947_call()
func_4989_call = mod.get_global_var('func_4989')
func_4991_call = mutated_mod.get_global_var('func_4991')
call_6233 = relay.TupleGetItem(func_4989_call(), 0)
call_6234 = relay.TupleGetItem(func_4991_call(), 0)
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
call_6235 = relay.TupleGetItem(func_463_call(relay.reshape(call_6227.astype('float32'), [14, 10, 7])), 0)
call_6236 = relay.TupleGetItem(func_466_call(relay.reshape(call_6227.astype('float32'), [14, 10, 7])), 0)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_6250 = relay.TupleGetItem(func_223_call(), 0)
call_6251 = relay.TupleGetItem(func_224_call(), 0)
output = relay.Tuple([call_6227,call_6230,call_6233,call_6235,call_6250,])
output2 = relay.Tuple([call_6228,call_6231,call_6234,call_6236,call_6251,])
func_6260 = relay.Function([], output)
mod['func_6260'] = func_6260
mod = relay.transform.InferType()(mod)
mutated_mod['func_6260'] = func_6260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6260_call = mutated_mod.get_global_var('func_6260')
call_6261 = func_6260_call()
output = call_6261
func_6262 = relay.Function([], output)
mutated_mod['func_6262'] = func_6262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4236_call = mod.get_global_var('func_4236')
func_4237_call = mutated_mod.get_global_var('func_4237')
call_6303 = relay.TupleGetItem(func_4236_call(), 1)
call_6304 = relay.TupleGetItem(func_4237_call(), 1)
output = relay.Tuple([call_6303,])
output2 = relay.Tuple([call_6304,])
func_6313 = relay.Function([], output)
mod['func_6313'] = func_6313
mod = relay.transform.InferType()(mod)
output = func_6313()
func_6314 = relay.Function([], output)
mutated_mod['func_6314'] = func_6314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_6332 = func_947_call()
call_6333 = func_947_call()
func_6006_call = mod.get_global_var('func_6006')
func_6008_call = mutated_mod.get_global_var('func_6008')
call_6334 = func_6006_call()
call_6335 = func_6006_call()
output = relay.Tuple([call_6332,call_6334,])
output2 = relay.Tuple([call_6333,call_6335,])
func_6344 = relay.Function([], output)
mod['func_6344'] = func_6344
mod = relay.transform.InferType()(mod)
output = func_6344()
func_6345 = relay.Function([], output)
mutated_mod['func_6345'] = func_6345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_6353 = func_947_call()
call_6354 = func_947_call()
func_5034_call = mod.get_global_var('func_5034')
func_5035_call = mutated_mod.get_global_var('func_5035')
call_6363 = func_5034_call()
call_6364 = func_5034_call()
output = relay.Tuple([call_6353,call_6363,])
output2 = relay.Tuple([call_6354,call_6364,])
func_6373 = relay.Function([], output)
mod['func_6373'] = func_6373
mod = relay.transform.InferType()(mod)
mutated_mod['func_6373'] = func_6373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6373_call = mutated_mod.get_global_var('func_6373')
call_6374 = func_6373_call()
output = call_6374
func_6375 = relay.Function([], output)
mutated_mod['func_6375'] = func_6375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5013_call = mod.get_global_var('func_5013')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_6428 = relay.TupleGetItem(func_5013_call(), 1)
call_6429 = relay.TupleGetItem(func_5015_call(), 1)
output = call_6428
output2 = call_6429
func_6446 = relay.Function([], output)
mod['func_6446'] = func_6446
mod = relay.transform.InferType()(mod)
output = func_6446()
func_6447 = relay.Function([], output)
mutated_mod['func_6447'] = func_6447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4751_call = mod.get_global_var('func_4751')
func_4753_call = mutated_mod.get_global_var('func_4753')
call_6520 = relay.TupleGetItem(func_4751_call(), 0)
call_6521 = relay.TupleGetItem(func_4753_call(), 0)
output = call_6520
output2 = call_6521
func_6577 = relay.Function([], output)
mod['func_6577'] = func_6577
mod = relay.transform.InferType()(mod)
mutated_mod['func_6577'] = func_6577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6577_call = mutated_mod.get_global_var('func_6577')
call_6578 = func_6577_call()
output = call_6578
func_6579 = relay.Function([], output)
mutated_mod['func_6579'] = func_6579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1520_call = mod.get_global_var('func_1520')
func_1522_call = mutated_mod.get_global_var('func_1522')
call_6615 = relay.TupleGetItem(func_1520_call(), 0)
call_6616 = relay.TupleGetItem(func_1522_call(), 0)
func_3264_call = mod.get_global_var('func_3264')
func_3266_call = mutated_mod.get_global_var('func_3266')
call_6624 = func_3264_call()
call_6625 = func_3264_call()
output = relay.Tuple([call_6615,call_6624,])
output2 = relay.Tuple([call_6616,call_6625,])
func_6626 = relay.Function([], output)
mod['func_6626'] = func_6626
mod = relay.transform.InferType()(mod)
output = func_6626()
func_6627 = relay.Function([], output)
mutated_mod['func_6627'] = func_6627
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6666 = relay.var("var_6666", dtype = "float64", shape = (15, 10, 12))#candidate|6666|(15, 10, 12)|var|float64
uop_6667 = relay.erf(var_6666.astype('float64')) # shape=(15, 10, 12)
func_1103_call = mod.get_global_var('func_1103')
func_1104_call = mutated_mod.get_global_var('func_1104')
call_6671 = func_1103_call()
call_6672 = func_1103_call()
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_6682 = relay.TupleGetItem(func_1958_call(), 0)
call_6683 = relay.TupleGetItem(func_1960_call(), 0)
output = relay.Tuple([uop_6667,call_6671,call_6682,])
output2 = relay.Tuple([uop_6667,call_6672,call_6683,])
func_6686 = relay.Function([var_6666,], output)
mod['func_6686'] = func_6686
mod = relay.transform.InferType()(mod)
var_6687 = relay.var("var_6687", dtype = "float64", shape = (15, 10, 12))#candidate|6687|(15, 10, 12)|var|float64
output = func_6686(var_6687)
func_6688 = relay.Function([var_6687], output)
mutated_mod['func_6688'] = func_6688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6626_call = mod.get_global_var('func_6626')
func_6627_call = mutated_mod.get_global_var('func_6627')
call_6692 = relay.TupleGetItem(func_6626_call(), 0)
call_6693 = relay.TupleGetItem(func_6627_call(), 0)
output = relay.Tuple([call_6692,])
output2 = relay.Tuple([call_6693,])
func_6699 = relay.Function([], output)
mod['func_6699'] = func_6699
mod = relay.transform.InferType()(mod)
mutated_mod['func_6699'] = func_6699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6699_call = mutated_mod.get_global_var('func_6699')
call_6700 = func_6699_call()
output = call_6700
func_6701 = relay.Function([], output)
mutated_mod['func_6701'] = func_6701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3674_call = mod.get_global_var('func_3674')
func_3676_call = mutated_mod.get_global_var('func_3676')
call_6711 = relay.TupleGetItem(func_3674_call(), 0)
call_6712 = relay.TupleGetItem(func_3676_call(), 0)
func_5092_call = mod.get_global_var('func_5092')
func_5094_call = mutated_mod.get_global_var('func_5094')
call_6731 = func_5092_call()
call_6732 = func_5092_call()
func_6344_call = mod.get_global_var('func_6344')
func_6345_call = mutated_mod.get_global_var('func_6345')
call_6735 = relay.TupleGetItem(func_6344_call(), 0)
call_6736 = relay.TupleGetItem(func_6345_call(), 0)
output = relay.Tuple([call_6711,call_6731,call_6735,])
output2 = relay.Tuple([call_6712,call_6732,call_6736,])
func_6757 = relay.Function([], output)
mod['func_6757'] = func_6757
mod = relay.transform.InferType()(mod)
mutated_mod['func_6757'] = func_6757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6757_call = mutated_mod.get_global_var('func_6757')
call_6758 = func_6757_call()
output = call_6758
func_6759 = relay.Function([], output)
mutated_mod['func_6759'] = func_6759
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6794 = relay.const([[[5.120023,-4.261689,7.795104,7.729247,0.750560,-7.645660,9.226170,-9.061740,-5.556988,8.550438,-7.718898,-9.136673,-3.309251,3.220297,-6.685014],[-4.950776,9.996789,6.674168,-0.662743,8.109787,8.560310,-4.329543,9.736785,-8.544024,-8.619793,4.035111,3.643153,-2.423768,8.880993,7.234785],[5.377043,6.280302,6.039957,7.178148,3.216173,6.471926,-6.770676,0.200908,-8.892565,3.343024,8.866390,9.822033,-0.827377,2.343523,-1.699176],[5.838043,-0.813862,-9.211637,-4.829189,0.280948,2.639773,-8.993158,-4.322552,7.945061,3.678584,0.224982,5.620276,-0.748620,-5.142441,4.449278],[-8.884362,-7.043679,-6.219009,-4.732765,-0.408702,-6.718827,-0.046766,-4.515451,7.201678,-6.721359,-2.109136,1.996944,-7.432222,-1.611968,9.319632],[1.007424,-6.000079,-3.061604,6.387117,2.525104,-7.953200,0.234303,-5.258461,9.305782,1.081548,3.481728,7.041679,9.449551,-9.643035,6.895425],[2.556490,9.949931,-5.223431,-7.311380,2.016473,-3.992961,-5.828826,-4.765377,6.769664,-8.593603,7.541843,-9.401585,-3.137561,7.589013,2.863114],[7.269512,4.273007,8.204894,-4.946240,0.339782,1.279973,-7.947993,7.240254,5.212718,-5.488282,1.129171,9.242026,9.402240,2.272547,-8.926022],[2.979069,-2.637586,-8.636713,-6.813811,6.182801,-6.984131,8.092221,-1.258642,-4.117647,2.900037,7.886555,-2.199403,7.868695,4.843968,-6.034899]],[[1.209296,5.373717,4.139904,6.583168,-7.750867,5.090674,-6.960641,4.077065,-2.452557,-7.504979,3.587733,-7.063335,-6.592227,8.537578,4.511256],[3.556369,3.999568,-0.091526,-0.474658,-4.021167,-4.601182,-6.716222,5.070343,-8.723719,9.791238,9.578724,-2.909198,-8.103502,4.200296,-4.759467],[-6.710026,-7.570447,-2.242605,-1.245295,-7.986976,-6.773881,-3.074986,1.662897,-4.588568,8.428352,-3.503721,-5.316700,4.493727,0.451024,-9.042644],[4.781199,0.038846,-9.366280,-4.330264,5.497707,-8.431952,9.681126,-8.944962,-7.706484,-2.725725,-2.435982,-6.110414,-0.109646,2.399867,4.694140],[6.905575,-6.498581,-7.437140,2.098385,0.966308,9.517396,-6.015010,9.947213,-8.490706,7.233796,2.088371,4.348047,0.664870,0.166383,-5.249692],[-9.010453,9.372285,-1.732147,-6.733560,-0.281608,-6.690521,6.742235,7.277569,1.287013,-2.884116,-2.984826,-1.277104,8.387207,8.265805,0.461810],[2.822935,-3.150102,-8.966269,-6.294352,-2.619294,0.732495,0.349356,0.784465,7.179854,-1.724366,2.253245,0.481428,-6.635415,0.449644,-7.565022],[3.413774,1.987762,-3.125597,8.798282,-2.394955,-3.553940,-0.141112,-0.075062,-1.227904,9.150480,0.490099,1.383369,-7.899319,3.774690,-1.423814],[-3.130217,-2.884573,5.221732,-1.867314,8.387426,-6.531793,-5.244604,7.678481,-0.494823,-9.922604,-4.272824,-7.498445,-5.510894,-5.014366,7.647858]],[[6.684691,-6.601166,5.378276,9.266668,-4.465606,-7.727702,-6.366351,-6.429984,1.834143,7.972255,-2.043916,7.724917,2.952579,4.557070,7.835198],[-3.989001,1.004109,-8.090892,-6.232865,-6.496688,9.524637,3.213659,5.382448,1.895381,-3.936219,-9.441268,4.122415,-7.055379,4.333032,-6.993983],[-6.114652,-3.577186,9.344961,-0.690336,-6.011948,2.506000,6.319119,0.033635,-1.899063,4.238556,7.450460,2.518147,5.848578,0.767078,3.692404],[9.399751,5.872702,4.993711,3.830749,-3.835148,-3.632891,6.835754,1.618468,-9.098137,5.862532,-5.435713,6.756612,7.864705,5.757913,-4.413103],[-6.232545,-7.774617,9.224633,9.891852,8.902133,-2.028312,1.152581,2.057445,-2.603929,-7.377373,2.909593,-4.410341,-3.635846,3.906369,-2.750823],[-9.443153,-2.088939,-4.597852,1.592795,-8.609952,-1.730597,-2.954297,-9.075469,-9.373677,-6.097159,-7.591242,7.666935,-3.704370,9.485187,-3.879737],[5.351749,-7.998558,4.583493,9.259014,-0.598766,-3.195487,-6.101559,-1.093640,-4.208883,5.193026,0.614965,8.600546,-6.785175,-0.439824,4.941687],[-8.552971,-3.758490,-6.570444,4.343886,-2.606152,9.907062,-5.488857,0.900510,-3.375753,1.316758,-0.634733,-6.211771,-7.562843,-8.859043,-8.287231],[2.610473,-7.525022,8.754189,5.046452,7.901216,0.069266,-3.877030,-6.164887,-0.380609,-5.530767,7.021283,5.281770,-2.954810,-9.754495,-5.682719]],[[-7.140654,2.966006,8.598391,-9.842029,-9.227606,-1.974151,-9.221355,4.808810,7.196030,-1.335756,-3.796084,-7.401782,1.840164,5.993965,0.454011],[-2.388911,8.726592,2.355276,-1.144757,0.658276,8.230135,-2.182384,9.810804,-6.527407,-7.199050,-0.112462,-7.035546,-3.933426,5.809293,-4.826880],[1.536229,-6.557559,-9.220399,-2.498347,5.571183,3.238842,5.566118,0.654899,-0.469079,5.436516,-5.055638,5.512319,6.851142,-4.080095,9.733046],[8.628732,0.224083,9.705175,8.164226,-8.876306,9.403760,5.613354,-2.553759,2.338071,4.882811,4.041570,-4.003695,-7.952550,-4.723575,-5.447127],[4.175895,-4.582855,-6.047532,3.629221,2.090570,-3.400297,9.935459,-6.020495,-0.386839,-4.324118,-9.301212,9.322505,-1.526410,-3.988089,-8.923058],[-6.982097,1.791097,-5.649980,-5.114200,1.567560,-9.519537,6.764832,-9.492767,8.769480,5.330389,-7.567121,2.479759,4.770038,4.332790,-0.313098],[-6.828422,-3.740014,8.216625,1.389154,-8.265195,-4.484243,0.974988,-5.072497,3.829002,-4.801160,-5.275529,-6.185638,9.281312,7.789762,-4.207622],[-1.318903,2.830421,-1.515507,-0.096987,-4.487304,-4.067092,7.656978,-7.672314,8.582402,8.864191,6.525422,-7.448871,7.803948,9.651972,2.010256],[-0.798170,-7.819157,-7.995308,-7.703695,3.753770,5.464276,8.751352,3.824821,-6.706995,4.010395,-8.101112,3.999524,0.982152,-4.203638,-2.978604]],[[-0.100993,-2.033664,-7.812678,0.616158,1.156376,8.991143,-8.411529,3.693669,9.829301,7.042278,9.139083,4.192157,-9.505119,7.912138,8.296262],[-6.519262,-4.055405,-5.900813,3.710081,4.774577,-3.740548,2.039079,-8.522881,-9.461280,4.969102,-1.185576,-8.769575,8.862222,-3.643377,8.892447],[-2.023855,4.612759,-9.846384,3.724253,7.591360,-4.156264,-8.188768,3.133116,-5.313479,-2.705093,5.038733,-4.202596,-5.308522,-5.129286,-0.569167],[-6.317492,-2.377343,2.204068,2.216638,-7.035431,-2.817465,2.124853,1.237083,3.303518,-1.973883,0.460208,-4.096089,8.406531,3.823393,-7.215165],[-1.043311,0.629226,-2.114629,3.326000,5.495278,6.950629,6.381424,-7.967788,7.722611,-1.270602,2.181367,6.918298,-1.653511,-9.565197,-6.216861],[2.110631,4.570251,8.171567,-8.497099,-0.940175,7.239042,5.319112,-4.072560,5.727809,9.715617,7.049779,3.102978,-3.975264,-2.146015,9.860864],[0.547216,4.592430,2.654387,7.354442,0.872696,-1.538337,0.142933,3.828383,7.575740,0.327715,2.939435,-3.998700,4.326470,-5.722011,5.822466],[-3.446199,-5.885022,-5.961508,5.076913,6.428209,0.560803,5.561494,4.813767,-4.048308,3.911042,3.115118,-6.118606,9.824362,4.246835,5.641985],[3.785755,6.505002,5.456742,-1.979970,7.293744,-1.375346,9.812958,5.168260,-2.812323,0.625128,6.815527,-7.005329,-2.941193,2.062826,6.575367]],[[5.397689,5.993732,9.300930,-7.617488,9.909344,0.506588,-6.088985,8.151347,-4.851970,9.197698,8.406692,-1.297507,-3.112660,4.887624,-5.531175],[8.594047,9.965872,3.420694,9.759168,-3.330690,0.070979,-3.230172,-5.086714,-0.845248,-7.861455,2.054910,-5.106335,8.451411,-2.649917,1.796659],[-3.933824,-7.115423,8.045716,-5.196143,1.317386,9.384952,-7.294342,-4.420500,8.013228,1.268957,-4.096728,1.945427,7.963647,-5.094900,1.307371],[-7.845020,-3.161002,0.258690,-6.176193,-9.213108,4.463534,4.616343,-5.753027,-3.461151,-4.887265,7.877232,-5.980566,0.578095,1.411092,-6.331579],[9.104017,-4.706393,1.478430,2.201196,7.641959,-0.127143,5.026800,3.192076,4.120137,4.453667,0.030871,4.974800,0.036440,5.890606,-3.205768],[2.354497,2.798946,1.439712,-1.700578,-1.362850,-2.889960,-5.607809,-5.776305,0.878218,5.570201,0.629821,1.380870,7.965103,-3.755741,-4.238375],[-8.538461,-1.769638,6.717867,-8.531817,8.955467,-4.336501,5.738396,1.560324,-7.492498,-3.008252,-3.373754,-6.311965,-4.750793,-2.443839,9.323464],[0.277840,5.537350,1.815268,4.547106,-7.849888,-0.833434,-2.646387,5.873587,-2.379316,3.606766,1.250316,-3.149566,1.322994,3.627805,4.537410],[-6.291086,-4.636700,3.147696,4.941760,-5.044841,8.763915,-6.790613,-8.190568,2.275524,2.010182,4.825852,-4.213442,-9.390316,-8.863927,-4.017084]],[[-9.432739,-9.715542,-2.087727,-6.556981,-6.113655,2.231227,-4.243424,-2.813775,4.198285,4.736072,-3.883260,6.261995,-4.873521,-8.181639,-5.527515],[2.730415,-3.155262,0.463300,7.045062,-8.555834,-4.783495,5.818634,5.240888,-9.907749,6.743397,2.572390,-9.732752,0.504190,-9.493341,-6.490974],[-7.146345,-0.062650,0.284259,2.427623,3.340533,5.602179,0.545939,-1.549238,-7.793808,3.299353,-1.655035,5.289079,6.574726,-3.374559,-5.662454],[-8.226804,-1.717599,0.268300,0.552416,-8.370445,-5.451809,-9.358862,-4.397655,-0.102404,4.067411,-7.278794,-5.721197,7.317664,-2.526127,-2.035550],[-4.609523,2.893206,8.009867,-5.675756,1.386230,7.285715,-8.870448,5.726577,0.080853,0.182123,2.456704,-6.658810,7.506546,-0.848429,2.670235],[8.799337,9.672586,-8.536356,4.584883,6.910964,9.058988,5.631147,5.262324,-9.879316,-4.494499,0.506204,-9.786848,-4.038355,7.382575,5.906261],[9.552523,-3.084367,-7.812335,3.730284,-3.218132,-5.380698,7.073854,5.847162,3.557369,0.478920,-1.281884,8.246042,2.161135,-8.390010,-3.747122],[5.281017,-3.775951,0.391566,2.445294,0.837441,8.147926,3.974763,1.615959,8.302065,2.215847,-0.063574,-1.414354,-0.527808,0.675540,-0.115059],[-2.544105,0.758611,-2.084638,8.573925,8.323738,0.465346,0.718597,-2.486853,7.980979,8.142679,-9.579004,-1.624951,4.210649,-8.668346,-4.106408]],[[6.314615,1.341733,0.319450,2.595601,6.963117,2.789285,4.423435,3.452772,2.897239,-9.857059,5.192576,3.224801,6.534548,-9.663484,7.912873],[-5.465405,-7.760268,-3.339297,8.855560,-8.199403,-0.816872,5.933244,-2.384278,4.964804,-9.699229,-2.606084,2.591270,2.788432,6.506262,-4.836232],[-8.340406,9.679313,-9.537704,7.216829,8.439512,-9.762762,8.748346,6.204111,5.844236,-7.642382,-9.212127,2.663552,-3.725459,-9.025397,0.294917],[-5.863624,-6.105680,-6.867921,4.427611,-9.615867,5.671135,7.800114,3.317463,0.601768,5.359929,-0.373246,-0.198529,8.115861,-7.327472,-4.831269],[1.587169,-2.814028,-6.724432,-2.258872,-3.381945,-0.036377,-4.141624,-0.055910,1.301166,-8.061349,6.477106,-2.377587,-0.781183,-7.940704,-0.378129],[-1.544558,-1.540792,6.293619,3.203639,-0.517672,-7.117194,-6.679627,-0.439999,-6.196853,-9.816213,5.839506,6.452030,0.470228,8.181868,8.758220],[3.240153,7.788496,-5.108663,-3.930970,2.981665,3.072100,-5.826957,-0.201947,-3.249464,-2.526478,7.925284,3.533894,9.677772,-1.863384,-1.928167],[-4.065331,-0.624576,6.332894,-1.359007,-4.462815,6.238394,-8.064442,1.559834,-8.235049,3.037906,-7.521059,-9.779066,-8.502868,1.434020,6.977666],[-2.727982,9.127631,6.898872,5.167177,-1.266805,4.347873,5.964115,9.873852,-8.259630,-5.393487,-3.842849,-4.259267,-0.223176,0.951781,-9.132584]],[[-8.083269,-1.521772,1.620793,-3.415814,-9.358064,-5.125724,-6.998153,3.574791,0.037824,-9.106110,9.906107,-4.232039,3.232002,-3.456719,-6.880864],[0.404250,7.682858,-2.036044,-3.895862,1.250506,-9.472879,-9.925964,4.780814,-3.051510,-2.451776,2.656471,-9.174832,7.658833,-1.574855,-0.991096],[-8.151893,3.983050,1.418907,-2.981405,9.190597,-0.614243,-7.789158,-3.951456,-4.212066,-2.415668,8.091462,7.963749,0.157899,-0.722986,-1.944478],[1.083653,-8.290003,3.884210,-5.230483,7.058930,5.897718,3.880612,1.536236,-1.581934,4.502158,-0.247058,-9.660363,-4.319608,-0.192429,1.066764],[2.985288,-9.022157,-6.398033,0.248655,0.788532,-0.262346,7.291628,-0.707952,4.365249,-3.658653,8.101742,-0.179206,-7.901058,-6.142312,7.818321],[-9.725263,-8.999923,-3.037869,-9.917598,6.712312,4.849458,-9.103161,-2.555474,3.540759,2.281055,-2.502737,-2.182984,-4.478227,1.502944,4.477922],[1.286884,8.340044,-6.559013,-3.591335,8.273424,0.083346,2.545843,7.212810,-6.037903,9.282430,9.525437,9.462264,-8.418990,-1.232217,-6.904381],[-2.611018,7.294261,6.829123,-8.983956,-3.631892,8.558281,-9.731377,-7.403854,-3.118100,-3.605045,-1.881257,8.076309,7.915865,-6.287658,4.946814],[6.383023,-3.183056,4.271857,9.585616,2.542472,-0.572091,5.289231,5.511718,-3.565349,-7.797564,0.558177,-1.806536,-4.011043,4.194490,-4.749837]]], dtype = "float64")#candidate|6794|(9, 9, 15)|const|float64
const_6795 = relay.const([[[-7.005910,-3.035071,9.986680,2.755549,-3.532956,-2.904186,-9.624343,6.227603,9.245186,3.907391,-0.632244,-5.927431,0.067955,2.567113,-4.088756],[-9.558358,-7.590381,6.379395,-6.567270,-8.821079,-6.958259,-4.285902,-9.743399,4.737058,3.563325,3.295816,2.895384,0.399618,3.150375,-3.979907],[9.820879,-4.857392,7.665601,-6.086499,7.218440,-0.489435,3.005488,-0.706074,-8.420444,4.162282,4.868422,-6.766270,-4.247391,3.187332,-1.693733],[-8.407078,-9.251267,-4.709263,-5.930876,0.363502,9.082785,8.550478,-8.135330,4.010965,7.714086,9.247015,2.499449,3.790542,5.700437,3.784049],[-4.685220,9.990097,-6.217836,2.433644,-1.700283,-7.840027,-4.752453,-3.330993,-9.576443,-3.892262,6.865990,-1.502116,1.205802,-0.784975,-9.461302],[-1.556024,2.071643,-4.248265,3.195884,-7.837886,-9.239378,-0.829374,-5.040630,-8.740317,-0.328319,7.496396,-7.843873,-3.604812,0.924682,-2.735737],[-1.116629,9.399941,-7.487773,2.919872,1.408927,-9.396981,1.029745,-6.799286,5.869286,-9.905429,0.257405,9.057936,5.314256,9.342252,0.777803],[-4.049861,6.550928,3.861775,7.718620,4.759591,9.406100,0.429926,-2.619642,-9.836008,-0.639836,6.193926,-5.647679,1.283024,-6.199887,8.050351],[-7.008404,6.287739,9.694175,7.044340,-1.860847,0.002805,-6.572817,-4.958229,-4.013787,5.864867,3.006280,1.693318,0.194679,2.134645,1.727221]],[[8.271639,-5.504593,6.565076,-2.609644,2.577704,-9.546726,-8.755163,0.523244,4.661692,3.856719,-3.243664,-1.642301,5.604860,-9.762762,1.971948],[0.635754,8.853922,-2.085560,3.450190,9.915003,3.569822,1.459905,9.323131,-5.587511,-5.962993,6.811158,-3.888844,-9.700638,6.686964,-6.739699],[7.091929,-5.884635,2.110578,3.195126,0.849742,9.715369,-6.274039,-6.410871,1.522419,1.502414,-1.382183,-9.581207,-7.824217,-4.177732,3.171854],[-2.055843,-2.087405,2.522146,5.853765,-0.399287,-5.577093,1.412431,-4.494075,-0.582904,-4.023791,-2.470433,-2.239314,9.385636,6.438979,-5.779549],[-7.074824,1.356569,4.095352,6.983246,-9.182851,3.291910,1.825093,2.854442,-7.246857,-6.014262,4.274911,-3.156785,6.235652,-9.674552,1.369660],[-5.428474,-5.300406,8.201234,-4.644167,-1.745580,-6.797716,5.360753,8.550261,-1.916084,-9.554170,-2.979617,1.947421,2.940506,1.670597,1.974740],[2.771498,-8.373766,-1.240502,4.736344,-9.625576,6.362982,-8.197812,9.716125,7.569996,1.452314,-3.138813,-5.823525,-3.405640,-6.389090,9.982039],[7.614167,2.857302,-6.819928,0.179885,6.827140,-4.687733,-7.277010,7.019392,-6.252214,9.944517,9.515227,1.969499,7.414941,2.564755,4.705474],[-8.412178,7.518846,8.866178,7.478198,-4.913991,-4.433793,6.102675,9.846354,-8.684647,3.761599,7.259634,8.737355,-7.023895,8.418358,1.223873]],[[2.640331,6.971096,8.717801,-4.132002,5.879364,2.486175,7.860103,-6.287115,-0.228285,-4.180875,1.033028,-4.775705,8.479542,2.135726,-0.714252],[7.555311,-3.102533,7.167042,2.568716,-2.638884,-2.251787,4.938321,-2.180306,-0.909144,-7.512504,5.764138,-8.685136,5.281069,-5.802232,-0.485566],[5.899031,-5.643432,-0.764196,9.161257,-9.993754,-3.345920,-4.985909,-5.985808,-5.526839,4.722320,-3.881968,-4.734138,-9.983248,-0.766221,-1.870303],[7.638612,-8.127503,-7.760105,9.655460,7.302297,3.544924,-5.153617,2.473964,3.697242,8.025477,-0.220805,6.507896,2.270223,-5.837634,-4.162941],[-3.190813,-7.243308,-1.078823,-2.033843,6.495299,4.695273,9.650474,-1.781031,-0.938452,-2.030802,-8.428701,4.067262,9.576752,4.187828,-2.174123],[2.324647,5.084420,-5.983950,-2.252459,-3.064939,-9.721170,-1.893235,4.623882,-3.564243,-2.251944,-4.935467,1.979882,-0.999151,-2.769515,3.554754],[-9.729385,2.118977,-8.648884,3.928779,-1.779278,-7.208281,1.104612,7.795964,4.120110,-1.105209,-7.898429,-4.203710,3.258960,6.665758,-6.184047],[-3.549372,4.697014,2.538823,0.274172,-2.022452,-3.251935,-5.899827,0.295166,-5.063153,8.079242,4.440352,7.317283,-5.154975,-3.225367,-8.842803],[-2.376254,8.227356,2.284057,8.769688,1.274295,-9.349254,0.488135,6.575275,-0.778546,6.640742,2.354200,-1.688087,2.069416,1.021588,-2.024139]],[[-3.038862,-7.757083,-4.556646,-5.007639,0.107339,9.705516,4.058502,-9.707162,0.443745,5.220168,0.007208,9.377166,1.068370,-6.789711,6.236880],[6.212655,4.948258,5.332989,9.382927,3.896324,-2.379974,-0.335038,1.143578,-4.807841,-8.571354,-9.105813,-1.307073,6.093536,-7.482455,-0.550760],[-8.236349,3.126845,-6.729583,6.970989,6.680360,-6.320669,7.337934,6.507811,2.833359,9.748511,1.722790,7.043575,-1.073631,-0.568715,-2.013253],[-9.987528,-1.139134,-2.882497,-8.625536,-8.924588,4.989845,7.164551,8.358286,2.432689,5.323607,-8.360506,-2.365243,-8.209180,-5.406509,4.444736],[-1.848082,1.289742,-4.029918,2.624915,1.914573,-5.758922,-4.471680,2.310102,-0.867814,-9.758904,-1.565133,8.993499,3.513398,4.910538,-9.499388],[-6.862068,-5.981866,6.801895,-0.319184,8.506480,-9.969930,-6.988495,-6.494861,-8.164274,-2.839948,-8.288891,-2.735136,-7.266090,0.926749,6.380991],[-4.715033,-9.935369,-8.472288,3.944769,-0.950646,-4.297670,-9.926766,1.392812,5.546614,-8.328016,0.004082,-3.238775,-8.744072,5.157835,-7.516323],[7.539032,-8.875551,9.241925,8.081620,9.300262,8.827922,-1.596961,-4.916458,-5.781481,3.355768,-6.841681,3.511887,-9.803044,9.711891,-4.150253],[5.274523,-3.621905,2.605364,-0.322680,2.756893,2.093646,0.551560,-2.263992,3.398591,8.947359,8.437638,3.188992,-2.358364,-6.814730,3.575620]],[[0.874758,-2.408031,1.056331,3.004374,-9.883531,8.137535,-6.488319,2.775288,9.965207,9.054703,-6.496335,-1.598791,-6.823202,7.877582,-1.842005],[4.746430,3.568073,2.702084,9.842095,-9.955679,8.087344,6.226412,9.621761,7.320324,-5.389174,8.544312,3.381790,-5.076827,9.708211,9.166646],[6.004919,2.722885,-6.590558,0.570112,-5.581206,-8.752350,1.842769,5.983176,-1.480406,5.571084,3.491291,0.697853,-6.030662,-2.887146,-0.422144],[6.672337,-2.475134,-7.454592,-2.235919,6.621925,-5.560192,-6.372680,9.195870,-9.411530,-1.396647,-9.086666,-2.728771,2.035314,-5.641582,-0.301731],[6.480419,-6.369900,5.100126,-1.022510,-5.953516,-5.488522,6.661286,-6.227052,-4.937619,5.015888,4.641983,-0.212557,8.863857,-8.166696,-6.495138],[-3.093223,8.251692,8.811881,-7.106463,-9.646679,5.994648,4.555050,3.400046,-8.483566,-2.772376,3.216217,3.763141,1.482136,9.635306,-9.580818],[4.763009,4.932245,4.349766,0.545871,-1.057910,-8.142917,-7.739208,3.029156,-6.541179,2.300218,9.205974,-6.274677,-5.920139,4.197091,9.296588],[1.852942,5.276357,6.359765,-0.251582,-5.333034,-5.313022,-2.584495,-3.949301,9.107641,7.172890,4.169049,4.783725,-5.369341,0.167828,6.212386],[9.431680,6.594678,8.834919,-0.439460,4.008489,-6.895475,3.896248,-0.607140,-4.985549,-5.245189,-4.231852,-9.775004,1.909507,-2.116812,3.615150]],[[-2.968933,-6.622876,6.553107,-0.934805,3.288291,-9.795893,-5.156142,0.286998,5.816918,-7.482333,3.991531,4.014171,-5.660421,-2.959236,4.840643],[-3.304250,5.116770,-2.539978,-6.867487,-5.743909,-8.493507,3.831979,-5.623189,-0.070591,9.029840,-9.817658,2.242311,-9.918291,-4.643331,-8.793624],[-9.236615,2.887911,-4.006681,-7.603347,1.358999,-0.556099,0.248955,-0.496178,-4.635283,3.190603,1.772648,1.662832,6.589703,-0.982257,-9.585709],[-8.089760,5.018499,-3.156045,0.670208,-1.958353,1.916351,-3.558558,-2.191853,3.430369,2.333458,-2.361187,-8.435647,-8.038535,-5.121583,8.390431],[4.346590,3.171422,-4.174267,-3.932307,9.909056,-6.871742,-7.631391,3.670837,9.441712,1.086826,-4.048573,1.095524,3.324002,-9.050748,-6.970061],[1.597524,6.861981,-3.588024,-4.214914,6.474195,2.240750,5.008819,6.787541,-3.176145,2.475484,8.689983,-5.545084,-8.465084,-5.821924,4.951312],[-2.998469,0.234821,3.678042,9.702277,-4.227852,1.191396,-9.569243,2.298093,-3.222671,-5.848061,-2.043933,4.203156,-1.706706,-8.465599,-0.955921],[6.383554,-3.407998,1.466247,-9.419809,-0.622635,9.519234,-3.487714,-6.398812,2.235588,-7.881693,-6.460331,-1.056590,9.069870,4.471256,3.320827],[4.215646,-0.772725,1.235295,6.563430,3.982274,1.919993,-3.665313,-5.091858,8.103412,5.260380,-7.020450,-6.652078,4.164978,4.296558,-9.999730]],[[-8.667235,-6.605316,9.284828,-5.111773,5.285705,-3.719682,5.751616,3.938174,1.583871,3.372504,-8.128419,-1.695413,-7.107017,-6.428921,-6.483023],[3.626233,-2.653041,-4.191384,8.023692,-4.560187,-8.072859,3.205594,4.865948,9.800618,-6.667503,1.071026,-2.742932,0.823354,3.167509,4.873517],[-6.670481,5.959581,-8.110440,1.768471,-8.054762,-1.213190,-6.706495,-9.791569,-4.995045,6.518214,3.704629,8.873123,-5.386102,-5.999578,-7.845604],[-1.008581,-1.083724,3.701088,8.347483,7.680546,4.086310,-2.274875,9.603492,5.809130,-5.066826,-6.763618,-7.664302,-2.597113,6.967545,-1.855323],[-0.144357,-4.804289,-9.389199,0.734956,-5.445579,-1.666624,-4.900945,-8.754936,4.450946,-7.411195,-4.064030,2.294660,-8.096856,5.529792,3.010401],[-4.450045,-8.250723,-9.450679,-5.484776,-9.389633,-5.009804,-2.938105,6.788827,4.535314,0.373277,7.253367,-8.457938,-6.261750,-6.768205,-4.522633],[7.975508,8.521901,-6.216122,3.831064,9.154917,5.205140,-0.916877,-6.618493,-8.084578,-1.081592,3.305036,5.926048,4.918266,2.144891,-4.494098],[4.407147,-2.897272,5.413982,-6.956582,7.058304,6.030414,-5.524453,6.899325,6.812192,-0.296753,4.350453,9.874237,4.698381,-5.332812,-1.408497],[2.539373,-2.030169,-0.539896,-0.723509,-2.530390,-7.152925,-0.900831,4.779547,-7.482387,-7.867355,3.041522,-8.598740,-9.145074,4.710020,-2.932668]],[[9.231915,4.555894,5.313563,-4.053610,-6.137954,-0.185147,-3.925204,7.978013,-0.321395,-5.203521,-0.544241,-8.075570,0.105322,0.545707,6.005006],[-1.601581,0.668045,-7.082817,-8.529646,-7.575690,-9.091629,7.875861,1.178241,-2.195326,-0.241202,-3.924132,-4.323467,-7.165269,-9.793337,-1.181079],[4.530638,-6.368155,-0.243990,-8.772890,8.644036,-9.909642,4.945313,-9.131689,-0.862420,-4.998639,-4.846046,-4.815927,1.027476,-1.521872,-8.383029],[8.659235,5.659358,-1.847828,-5.429880,-1.978777,3.278743,8.078906,2.377605,1.334700,9.217739,-7.948392,5.997985,-0.186903,3.205543,-0.975380],[-2.534756,-4.589577,4.340690,7.327031,5.485375,-1.696873,-7.904154,3.090691,6.278266,-8.464129,-3.257620,-2.804962,4.330723,-4.556354,4.196460],[-2.380677,-2.227356,-2.047868,5.413355,0.158292,1.445183,4.670416,-2.003501,7.366474,5.753336,-0.212094,6.992109,1.444276,4.556610,8.972187],[-8.297625,-5.506867,-7.780637,9.106055,7.671077,-2.913383,-0.890413,-3.146020,-6.632964,-6.310382,0.706487,5.615021,-6.303967,1.416714,-5.635563],[-6.236046,-0.189361,4.451558,7.663472,-5.777866,-8.662850,-7.403445,-0.129703,2.908355,-7.576761,4.747632,-6.586518,-5.101380,1.641474,-4.497294],[7.160238,0.096385,-5.279904,-9.949990,8.068459,-8.829509,-7.965413,-4.245445,7.149004,7.648033,2.922543,-8.476471,-7.013156,-9.173371,-7.007506]],[[6.411376,-3.626533,-4.585591,-0.110291,-0.268704,9.914129,4.446145,2.376265,5.739127,8.032361,0.371653,6.185930,-7.976628,-9.439025,4.354853],[7.458241,-4.401104,8.096463,-8.247889,-3.551126,4.781939,8.402235,4.556523,-5.583716,-5.858399,7.054758,1.619930,5.670479,-9.177931,-5.063390],[-8.146879,9.853622,4.666886,0.412838,-9.489027,3.257371,-0.279332,-4.748522,3.335875,-9.190007,-6.650891,9.786481,-4.082171,5.945656,2.617461],[-1.080389,5.053472,-8.661373,5.222991,1.967719,6.466177,3.427373,3.972581,2.996426,6.376056,-5.764162,-4.187975,6.784419,-1.962511,2.608496],[-9.998117,-7.533453,9.982603,3.763050,-1.173636,-1.495085,3.921264,3.367901,8.890940,1.200020,-3.220706,-0.340140,-8.406931,4.989503,-5.078923],[-3.257819,3.276167,1.427399,9.200623,7.712491,8.282906,-4.872623,5.760421,9.179261,-1.803451,0.673430,9.913065,1.566928,1.854737,-0.939736],[-9.353401,6.272594,2.536857,-7.734715,6.391976,4.794291,-6.155743,9.998460,5.580131,-1.896651,5.364395,1.438728,-9.593077,-2.556343,1.007272],[1.819561,6.973522,3.235206,5.415284,-8.010438,3.182432,0.204571,5.394933,-4.925534,-2.807227,-0.579506,-6.405251,-4.491610,3.447744,9.382012],[4.680231,-5.783452,4.332417,-9.085325,9.674783,4.383904,-6.094918,-1.731565,0.358419,-8.958974,-3.316804,4.701584,-7.347507,3.048753,2.010090]]], dtype = "float64")#candidate|6795|(9, 9, 15)|const|float64
bop_6796 = relay.divide(const_6794.astype('float64'), relay.reshape(const_6795.astype('float64'), relay.shape_of(const_6794))) # shape=(9, 9, 15)
func_5435_call = mod.get_global_var('func_5435')
func_5439_call = mutated_mod.get_global_var('func_5439')
var_6800 = relay.var("var_6800", dtype = "float32", shape = (121, 14))#candidate|6800|(121, 14)|var|float32
call_6799 = relay.TupleGetItem(func_5435_call(relay.reshape(var_6800.astype('float32'), [11, 11, 14]), relay.reshape(var_6800.astype('float32'), [11, 11, 14]), ), 0)
call_6801 = relay.TupleGetItem(func_5439_call(relay.reshape(var_6800.astype('float32'), [11, 11, 14]), relay.reshape(var_6800.astype('float32'), [11, 11, 14]), ), 0)
func_5725_call = mod.get_global_var('func_5725')
func_5729_call = mutated_mod.get_global_var('func_5729')
const_6811 = relay.const([[-7,-4,5,4,5,6,4,5,4,7,3,7,6,-1,9,9,-4,-10,7,4,4],[7,5,6,-1,-5,6,2,-3,-6,8,-10,-10,-1,6,10,-7,-10,8,4,-10,4],[10,-8,6,-5,1,9,6,6,-7,-4,3,9,-9,-3,-1,-4,2,3,-8,-2,-6],[8,-1,7,-3,4,-4,-1,3,5,2,4,3,-2,10,8,7,9,10,-7,9,-1],[4,10,-6,3,4,2,9,-6,7,6,-10,3,-2,-5,2,6,9,-5,-10,-5,-8],[-2,10,-5,-4,1,5,-5,4,10,7,-4,-1,-3,7,-3,-4,1,5,-1,6,-2],[-7,10,7,9,-3,2,4,-4,3,8,-4,-1,7,-7,-5,-6,4,-4,-5,6,-8],[3,-4,-2,4,-4,1,7,-7,-10,3,-5,-3,9,3,-7,2,2,-7,-2,-6,-1],[-2,-2,-5,3,2,7,8,3,-1,-2,-10,-8,-1,-10,-7,-2,3,1,-10,-8,-2],[-6,-10,2,9,4,-10,-10,5,8,3,2,-5,4,7,6,6,2,2,7,9,5],[-8,-2,5,4,9,-5,-10,8,10,9,-9,-2,-4,-4,-2,4,-2,-10,4,6,-3],[8,10,1,1,6,10,10,-6,-6,-1,-8,-7,-1,-6,6,10,3,9,1,-3,-9],[4,-6,4,-1,-4,-8,-9,6,10,5,6,-1,1,7,9,-4,7,-7,3,4,9]], dtype = "uint32")#candidate|6811|(13, 21)|const|uint32
const_6812 = relay.const([5,-3,9,3,-3,-7,8,4,4,-3,6,-7,8,-2,4,5,-3,-6,-10,10,1,10,7,3,3,-4,-9,-2,6,-7,-3,-10,1,-1,-8,-6,10,8,-1,-9,-7,3,-6,3,9,2,2,-8,-1,-6,4,8,10,-9,7,7,-1,-1,5,10,-6,6,6,3,-7,-6,2,4,2,-7,3,4,-4,2,-9,-5,-5,-2,-7,8,-5,4,10,3,1,-10,4,8,-7,9,-3,10,5,6,-9,5,-9,-3,-5,1,-4,10,-3,8,-1,7,-9,-9,-2,-6,1,7,10,-9,6,-3,-10,-10,5,4,-3,9,1,8,-5,6,-6,6,-3,-3,6,9,10,9,-7,9,-6,-4,8,-8,-6,9,-7,10,-1,-9,6,2,-9,-1,-2,6,1,-4,-2,2,-7,2,7,4,-2,4,2,5,-7,-6,1,8,2,10,4,-3,-4,-7,-4,10,5,-7,-2,-6,1,7,-8,3,-6,-5,7,-1,1,-4,10,-5,8,10,4,-8,-2,6,-1,-9,4,-7,-1,1,-6,-1,9,-1,-7,8,9,-6,-2,-10,-5,-7,-4,-7,-5,-7,3,7,-3,8,1,1,1,-2,4,-3,-2,6,-7,1,3,-2,7,8,-10,-9,-4,1,-8,6,7,-8,4,-5,9,2,5,8,-5,-9,7,-8,-8,4,-3,9,4,9,3,8,1,4,3,-5,2,-5,-3,8,3,-9,-6,6,-8,-7,-2,-3,-4,8,-2,-8,-10,3,-8,-7,7,-9,6,3,2,-5,5,-7,8,8,2,-4,1,-6,-2,-1,-2,-4,-6,4,-6,-4,8,2,1,-4,6,-3,-9,7,3,10,8,6,10,-6,7,-9,-3,1,-1,-7,6,5,9,7,-9,9,-1,-5,-5,9,-3,8,-1,2,-5,10,-6,-7,6,1,10,-7,7,2,-5,3,-1,-5,-10,-6,-3,6,-1,8,-6,-5,1,7,-3,9,2,-5,-2,7,7,-7,-8,-2,6,8,-9,6,6,5,4,9,-5,-1,5,9,9,-2,10,8,2,-8,1,-10,-9,8,10,-9,2,-3,6,-10,-9,4,6,3,-9,10,5,9,-6,7,-2,2,6,10,-7,-9,-3,-4,-4,-9,-8,-5,1,-8,10,-3,-4,6,-10,4,-9,2,5,-2,-2,3,2,-6,-1,9,4,4,7,-9,-6,-4,7,8,-1,2,1,-7,3,-5,-10,6,6,-3,7,4,5,10,-4,-6,9,2,3,-3,3,-1,-2,-8,-6,-5,-2,-8,-7,-1,-9,7,6,5,9,6,-8,8,7,-2,6,5,6,-7,6,-5,-6,10,-4,-1,-5,-8,5,4,-3,-4,6,8,-7,-7,4,5,-6,10,-1,6,8,-10,-1,7,-1,-4,-2,-10,-9,1,9,-1,-2,7,-2,9,9,6,-4,-4,6,3,-10,9,8,-3,8,3,5,-3,-7,10,10,5,-1,-8,-7,-6,-3,-6,-9,-9,-3,8,6,-8,2,8,5,5,-10,-2,-5,4,7,9,1,4,-2,-3,-2,3,8,-7,5,-9,-4,-2,1,-4,-7,6,-3,-3,3,-7,-6,2,-2,-7,8,1,-8,10,2,10,1,9,-8,-10,6,-9,-8,8,-7,-6,-2,-8,4,10,4,-5,-9,8,5,-10,7,-5,10,6,10,-4,-3,-3,-2,10,4,-10,10,-10,-8,-7,-10,2,6,9,2,-8,-6,1,-3,-4,6,2,4,10,4,8,10,6,-8,3,8,6,-2,4,7,4,3,-9,10,8,-9,-2,6,8,-4,-7,-2,-8,7,-2,1,-10,-6,9,10,-1,-6,9,-10,-10,-6,7,-8,-6,9,1,-6,4,10,7,3,-9,3,-2,5,-9,7,-2,-3,3,-6,3,7,-3,1,9,10,-4,7,7,-8,-4,-4,-1,3,-2,10,1,3,4,-6,9,-2,10,-8,1,7,2,-10,-10,-9,-3,6,-6,-8,2,-3,1,-3,-5,1,-7,-1,-10,2,-5,-10,9,4,6,6,-7,10,-4,-8,4,-5,8,9,-7,5,3,-10,-5,8,6,3,10,-1,6,3,1,-2,4,-4,-6,2,-6,2,7,-5,1,-8,1,7,-1,9,10,10,5,-2,-2,-10,9,2,-1,10,-4,5,2,-5,4,-4,5,6,-7,-1,-5,9,-1,9,-9,4,-1,-3,10,-5,-1,-9,-2,-8,-7,10,-10,-5,4,-2,5,10,-6,-9,10,3,3,-10,10,4,5,-9,-6,5,-8,-3,-7,-3,6,3,5,7,-9,3,-3,5,2,4,-8,-6,-9,3,3,-1,7,-3,10,-10,-9,8,-9,-1,-9,-1,-7,7,-7,2,-8,9,6,8,3,7,-1,3,8,-3,10,-5,-10,-3,-5,-6,-9,-8,8,3,4,-1,-4,6,-10,-10,4,7,10,-2,-6,-7,5,2,-1,-5,6,1,2,-2,8,-3,9,-8,-2,3,-3,7,-6,-1,5,-2,-2,8,10,-6,-4,-5,-1,-10,-5,4,-3,-6,-7,6,3,-2,-10,-8,-2,1,3,7,-8,8,-1,-1,-3,-5,-2,-4,-8,-9,-9,-9,3,-9,7,-2,-4,-8,5,1,-6,10,-9,4,-1,6,-4,-2,-8,-5,6,9,10,-7,9,-4,-6,5,-9,5,-4,9,-9,-4,2,9,7,-10,-5,3,-4,-9,3,10,-4,9,7,7,1,-2,-1,10,8,4,-6,-9,5,-5,-3,10,9,5,-7,1,-4,-10,-3,-10,10,-4,4,-7,1,-7,6,-2,-7,10,-1,-2,3,9,-4,-4,-4,1,4,-7,1,-1,-3,1,-4,-4,1,10,-1,7,-8,8,-3,-2,-8,-4,-6,7,10,9,-8,-6,10,2,-5,-7,-3,-8,5,-3,-10,-3,10,4,-5,-1,-6,3,-5,9,5,4,10,-4,2,9,4,8,9,3,7,-8,-5,10,5,9,-5,10,4,2,3,10,1,-1,-2,-6,-10,-1,-3,-4,-2,10,7,5,-6,-9,-8,6,7,-10,4,7,10,1,-10,-6,2,-10,-8,10,1,4,-8,-9,-2,3,8,-1,9,4,9,-2,5,-9,8,-8,-9,-10,-7,-2,-1,4,-7,8,9,5,-1,10,-10,9,-8,-9,-1,6,10,-8,6,-10,9,9,9,7,-3,-4,-5,3,3,-4,10,4,-9,1,-4,-8,-9,2,-3,8,7,-8,-6,-8,2,-3,2,-2,-2,6,-6,-1,-1,4,4,-9,5,-3,-10,-2,-5,-5,-4,9,2,2,-2,-6,5,-9,2,-10,-9,8,8,-2,-4,-3,5,-4,9,-8,8,6,-2,4,4,10,9,-3,-7,1,3,2,5,-7,-2,7,-9,-5,7,6,5,5,4,-10,-4,-4,4,4,-10,4,-8,-3,-4,-7,-10,-6,-8,9,-10,5,-10,10,-3,-3,-7,-6,-8,9,9,-6,-8,-6,-3,8,-5,-9,2,-9,4,-7,-1,-6,-3,-2,1,-3,-10,5,5,-1,6,5,9,-2,-8,-4,3,-7,-4,-3,8,-6,-7,4,-4,-10,4,10,-9,-6,3,-5,9,7,10,-10,5,7,-7,-4,5,-5,9,-2,-10,-7,-8,1,4,-3,-5,-3,1,2,2,-2,10,-7,3,-9,-8,5,-1,-3,2,1,3,10,3,-3,-8,3,-2,-6,10,7,-2,-1,-9,-7,-4,-2,2,2,-4,2,10,9,-6,7,10,1,8,-4,10,-2,2,1,6,1,8,1,9,-10,-4,-8,-4,-6,-2,-1,-2,7,5,-7,-1,10,-2,-7,-2,5,-7,10,-3,-4,-9,-7,8,-6,-4,-3,-1,-4,5,-5,2,2,-4,-1,-1,2,-1,-10,7,-1,8,5,6,-4,5,-7,9,8,-4,-10,5,-6,5,3,-1,-2,-8,-10,-8,-5,-6,-2,2,8,-9,2,2,-8,3,6,8,6,-5,-10,3,-8,8,3,9,9,-2,2,8,-1,-3,-6,7,9,-10,-6,6,3,-5,-7,10,2,4,5,6,-4,7,2,-2,5,-1,7,7,1,-6,8,-2,-7,-6,10,-10,-1,-4,10,-5,10,-8,-3,-6,-10,-5,-8,1,-5,10,9,2,7,-4,-2,4,6,10,8,8,-8,-4,-9,-4,2,-4,3,2,1,-1,-6,6,6,5,-2,9,5,-10,10,1,-7,-4,2,-2,-1,-6,7,-1,10,4,9,3,9,-8,-7,-3,-5,-5,-1,8,10,-9,7,-8,5,10,7,6,7,7,3,8,-4,-5,-10,9,8,-8,7,4,2,-6,5,5,7,8,9,-10,-9,-10,-7,-2,6,-1,-10,6,7,8,-5,-8,4,-4,3,8,8,-2,8,1,-6,8,7,5,-6,-10,8,3,3,3,-1,10,10,4,8,3,-10,-1,2,3,-10,9,2,-10,-1,-2,5,-10,4,4,-1,-9,5,-10,-7,-7,7,-5,-9,-3,-7,1,-7,-8,6,4,-8,-10,10,-1,4,-3,3,-1,4,-1,1,4,2,8,3,-9,2,3,-1,10,-2,8,3,-6,-5,10,8,1,-6,-9,-10,10,-10,-5,-7,6,-10,-5,-6,-1,-7,-7,5,-6,-9,-9,-5,-1,2,-4,5,-10,-6,9,5,5,1,8,9,6,-1,7,4,1,-7,6,-8,-6,-3,-6,-5,4,-2,3,-8,-1,3,-7,9,-4,-4,6,-1,8,-7,4,-7,7,1,-3,8,8,-2,-10,-4,7,9,1,8,-3,4,-7,6,-10,-4,5,-5,-5,9,-9,-2,-10,2,10,-9,-4,-10,3,7,-2,4,-2,10,9,-3,-2,-7,-5,-2,-10,9,5,7,5,1,4,7,-8,5,8,-6,-4,-1,-3,-5,-7,8,-6,-1,-10,10,-10,4,-4,5,-7,-10,-5,10,-7,4,-1,-5,-9,8,9,-7,-3,-6,10,-8,-4,7,-1,-9,4,-10,6,-2,2,-8,5,9,-8,6,-8,-6,3,2,-4,2,-6,5,-10,1,-6,-2,-6,-1,-7,4,-9,6,6,8,10,-8,-4,8,-9,-7,-10,5,1,-10,-3,2,5,-6,7,-10,3,3,2,-3,-2,7,-1,-8,10,-1,-2,-5,-2,-7,4,-5,-7,8,4,2,4,-8,4,9,3,7,2,2,4,2,9,8,-10,7,10,9,-3,-10,4,2,-7,5,-2,3,8,-5,5,-5,2,8,-5,5,-6,6,-4,7,9,1,9,-9,-1,6,-10,10,4,3,5,-9,2,-10,4,-8,-9,4,4,7,-8,3,5,-1,3,10,1,-10,-5,-1,-10,-1,1,9,9,-3,2,-8,-1,-7,2,-4,-9,7,-5,-4,-7,-3,2,-4,-1,-9,-4,9,-5,-8,4,-9,-6,-6,5,5,-6,-2,4,9,-4,-8,5,-2,2,7,-3,8,5,2,5,-1,10,1,-9,9,9,2,3,-6,5,2,4,-9,5,6,-9,-4,2,2,4,-7,-9,10,-4,-8,4,8,1,4,9,9,-10,-8,6,4,-1,6,-9,-3,-3,-3,-2,-4,8,-2,-9,-6,4,1,-6,-2,7,9,4,-10,-5,-3,-2,2,4,-9,-5,-4,-3,-8,2,-7,8,5,-2,-9,8,3,-9,-1,7,6,7,10,4,10,-10,5,5,-9,6,3,10,-5,-9,1,-8,-9,-6,-6,8,6,-5,5,-2,-6,-2,2,4,-2,8,2,-2,-5,-1,9,-9,7,-8,3,-7,-8,-7,-3,-10,6,10,-5,1,1,1,1,-4,1,1,2,2,-8,-10,1,-8,7,-7,2,-10,-9,-2,-8,-1,8,2,9,-10,2,8,8,-10,-7,7,4,10,-8,-6,-9,-7,8,-9,-3,3,-8,1,-10,3,8,5,-9,7,-9,6,-7,-9,6,1,-8,7,9,2,-8,7,2,2,-10,1,-10,-9,1,2,-5,-9,1,-9,-3,-10,-3,-1,-10,8,-9,-9,-5,-8,6,6,-4,4,-10,-6,3,7,4,1,-10,5,-8,-10,3,-9,-7,10,-9,-9,-9,-3,-10,8,-8,-9,8,8,8,-8,6,-2,4,6,-8,4,1,-10,8,6,-7,-6,9,-2,2,2,9,2,-5,5,-7,-1,-6,9,10,-4,10,-3,-4,10,5,5,-5,7,9,-3,1,-3,6,-3,-7,1,-6,8,1,7,9,2,-3,2,-1,6,-1,-10,-3,1,-1,7,9,9,-5,-8,10,-6], dtype = "int8")#candidate|6812|(2340,)|const|int8
call_6810 = relay.TupleGetItem(func_5725_call(relay.reshape(const_6811.astype('uint32'), [7, 13, 3]), relay.reshape(const_6811.astype('uint32'), [7, 13, 3]), relay.reshape(const_6812.astype('int8'), [2340,]), ), 2)
call_6813 = relay.TupleGetItem(func_5729_call(relay.reshape(const_6811.astype('uint32'), [7, 13, 3]), relay.reshape(const_6811.astype('uint32'), [7, 13, 3]), relay.reshape(const_6812.astype('int8'), [2340,]), ), 2)
output = relay.Tuple([bop_6796,call_6799,var_6800,call_6810,const_6811,const_6812,])
output2 = relay.Tuple([bop_6796,call_6801,var_6800,call_6813,const_6811,const_6812,])
func_6820 = relay.Function([var_6800,], output)
mod['func_6820'] = func_6820
mod = relay.transform.InferType()(mod)
var_6821 = relay.var("var_6821", dtype = "float32", shape = (121, 14))#candidate|6821|(121, 14)|var|float32
output = func_6820(var_6821)
func_6822 = relay.Function([var_6821], output)
mutated_mod['func_6822'] = func_6822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5841_call = mod.get_global_var('func_5841')
func_5843_call = mutated_mod.get_global_var('func_5843')
call_6844 = func_5841_call()
call_6845 = func_5841_call()
uop_6847 = relay.asinh(call_6844.astype('float32')) # shape=(2, 14, 10)
uop_6849 = relay.asinh(call_6845.astype('float32')) # shape=(2, 14, 10)
func_1090_call = mod.get_global_var('func_1090')
func_1093_call = mutated_mod.get_global_var('func_1093')
const_6852 = relay.const(-9.963093, dtype = "float64")#candidate|6852|()|const|float64
var_6853 = relay.var("var_6853", dtype = "float64", shape = (2, 40))#candidate|6853|(2, 40)|var|float64
call_6851 = func_1090_call(relay.reshape(const_6852.astype('float64'), []), relay.reshape(var_6853.astype('float64'), [1, 16, 5]), )
call_6854 = func_1090_call(relay.reshape(const_6852.astype('float64'), []), relay.reshape(var_6853.astype('float64'), [1, 16, 5]), )
bop_6857 = relay.floor_mod(call_6851.astype('float64'), const_6852.astype('float64')) # shape=(1, 16, 5)
bop_6860 = relay.floor_mod(call_6854.astype('float64'), const_6852.astype('float64')) # shape=(1, 16, 5)
func_3917_call = mod.get_global_var('func_3917')
func_3918_call = mutated_mod.get_global_var('func_3918')
call_6868 = relay.TupleGetItem(func_3917_call(), 2)
call_6869 = relay.TupleGetItem(func_3918_call(), 2)
bop_6877 = relay.logical_or(uop_6847.astype('bool'), relay.reshape(call_6844.astype('bool'), relay.shape_of(uop_6847))) # shape=(2, 14, 10)
bop_6880 = relay.logical_or(uop_6849.astype('bool'), relay.reshape(call_6845.astype('bool'), relay.shape_of(uop_6849))) # shape=(2, 14, 10)
func_1413_call = mod.get_global_var('func_1413')
func_1415_call = mutated_mod.get_global_var('func_1415')
call_6889 = relay.TupleGetItem(func_1413_call(), 0)
call_6890 = relay.TupleGetItem(func_1415_call(), 0)
func_6207_call = mod.get_global_var('func_6207')
func_6208_call = mutated_mod.get_global_var('func_6208')
call_6912 = relay.TupleGetItem(func_6207_call(), 3)
call_6913 = relay.TupleGetItem(func_6208_call(), 3)
uop_6919 = relay.rsqrt(bop_6877.astype('float32')) # shape=(2, 14, 10)
uop_6921 = relay.rsqrt(bop_6880.astype('float32')) # shape=(2, 14, 10)
output = relay.Tuple([var_6853,bop_6857,call_6868,call_6889,call_6912,uop_6919,])
output2 = relay.Tuple([var_6853,bop_6860,call_6869,call_6890,call_6913,uop_6921,])
func_6924 = relay.Function([var_6853,], output)
mod['func_6924'] = func_6924
mod = relay.transform.InferType()(mod)
mutated_mod['func_6924'] = func_6924
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6925 = relay.var("var_6925", dtype = "float64", shape = (2, 40))#candidate|6925|(2, 40)|var|float64
func_6924_call = mutated_mod.get_global_var('func_6924')
call_6926 = func_6924_call(var_6925)
output = call_6926
func_6927 = relay.Function([var_6925], output)
mutated_mod['func_6927'] = func_6927
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6944 = relay.var("var_6944", dtype = "uint64", shape = (16, 14, 8))#candidate|6944|(16, 14, 8)|var|uint64
var_6945 = relay.var("var_6945", dtype = "uint64", shape = (16, 14, 8))#candidate|6945|(16, 14, 8)|var|uint64
bop_6946 = relay.bitwise_xor(var_6944.astype('uint64'), relay.reshape(var_6945.astype('uint64'), relay.shape_of(var_6944))) # shape=(16, 14, 8)
bop_6951 = relay.add(var_6945.astype('int64'), relay.reshape(bop_6946.astype('int64'), relay.shape_of(var_6945))) # shape=(16, 14, 8)
uop_6955 = relay.acos(var_6944.astype('float32')) # shape=(16, 14, 8)
func_4256_call = mod.get_global_var('func_4256')
func_4258_call = mutated_mod.get_global_var('func_4258')
call_6960 = func_4256_call()
call_6961 = func_4256_call()
uop_6975 = relay.asinh(var_6945.astype('float64')) # shape=(16, 14, 8)
func_4119_call = mod.get_global_var('func_4119')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_6980 = relay.TupleGetItem(func_4119_call(), 1)
call_6981 = relay.TupleGetItem(func_4120_call(), 1)
func_621_call = mod.get_global_var('func_621')
func_624_call = mutated_mod.get_global_var('func_624')
const_6995 = relay.const([[3,-2,4,-10,-7,8,-6,-2,9,9,-2,10,-5,-1,-10,-3,-9,-2,1,7,1,-8,6,-4,-9,-3,-8,-5,5,-1,5,9,-10,-8,5,9,-3,-4,8,3,9,-8,-2,-3,1,1,-7,-9,-1,8,-2,-3,3,-3,-5,8],[-6,-4,-1,3,-10,-5,5,4,3,-2,-10,-2,-4,3,5,5,10,-8,-8,-3,5,5,-4,-4,4,5,-2,-6,4,-6,-3,-10,10,-5,9,7,6,4,5,-8,-5,-3,-2,1,-8,-6,-8,3,-4,-6,-4,7,-9,1,-10,-2],[-4,1,-2,5,-9,-1,9,7,-2,-6,-8,-8,5,-10,8,9,-7,-9,5,10,-5,1,5,-7,10,3,8,6,1,-8,10,-1,8,-9,-6,-6,-10,-6,6,-1,-7,-8,-8,-6,-10,7,2,8,-10,4,6,8,1,-10,-7,5],[7,-9,-8,3,-1,-2,10,4,9,-7,-2,-2,1,9,-4,4,-2,10,1,-9,-6,5,3,8,-1,-6,2,-5,-1,-4,3,-8,-2,4,-2,6,-6,-3,-2,8,6,6,3,4,8,-10,-8,5,-7,-3,-3,-8,-2,5,-2,9],[10,-9,-9,-6,-2,9,5,2,-4,-2,6,4,-2,1,-4,5,6,-7,-8,-3,9,2,7,-7,-1,-7,-10,-4,-2,10,5,-1,9,7,1,10,3,4,-6,-10,2,3,-8,6,-1,-7,-2,-9,-6,-10,8,7,-2,9,3,-6]], dtype = "int16")#candidate|6995|(5, 56)|const|int16
call_6994 = func_621_call(relay.reshape(const_6995.astype('int16'), [2, 14, 10]), relay.reshape(const_6995.astype('int16'), [2, 14, 10]), )
call_6996 = func_621_call(relay.reshape(const_6995.astype('int16'), [2, 14, 10]), relay.reshape(const_6995.astype('int16'), [2, 14, 10]), )
output = relay.Tuple([bop_6951,uop_6955,call_6960,uop_6975,call_6980,call_6994,const_6995,])
output2 = relay.Tuple([bop_6951,uop_6955,call_6961,uop_6975,call_6981,call_6996,const_6995,])
func_6999 = relay.Function([var_6944,var_6945,], output)
mod['func_6999'] = func_6999
mod = relay.transform.InferType()(mod)
var_7000 = relay.var("var_7000", dtype = "uint64", shape = (16, 14, 8))#candidate|7000|(16, 14, 8)|var|uint64
var_7001 = relay.var("var_7001", dtype = "uint64", shape = (16, 14, 8))#candidate|7001|(16, 14, 8)|var|uint64
output = func_6999(var_7000,var_7001,)
func_7002 = relay.Function([var_7000,var_7001,], output)
mutated_mod['func_7002'] = func_7002
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7033 = relay.var("var_7033", dtype = "float64", shape = (5, 10, 15))#candidate|7033|(5, 10, 15)|var|float64
var_7034 = relay.var("var_7034", dtype = "float64", shape = (5, 10, 15))#candidate|7034|(5, 10, 15)|var|float64
bop_7035 = relay.mod(var_7033.astype('float64'), relay.reshape(var_7034.astype('float64'), relay.shape_of(var_7033))) # shape=(5, 10, 15)
func_252_call = mod.get_global_var('func_252')
func_253_call = mutated_mod.get_global_var('func_253')
call_7039 = relay.TupleGetItem(func_252_call(), 0)
call_7040 = relay.TupleGetItem(func_253_call(), 0)
bop_7066 = relay.add(var_7033.astype('uint16'), relay.reshape(var_7034.astype('uint16'), relay.shape_of(var_7033))) # shape=(5, 10, 15)
output = relay.Tuple([bop_7035,call_7039,bop_7066,])
output2 = relay.Tuple([bop_7035,call_7040,bop_7066,])
func_7069 = relay.Function([var_7033,var_7034,], output)
mod['func_7069'] = func_7069
mod = relay.transform.InferType()(mod)
var_7070 = relay.var("var_7070", dtype = "float64", shape = (5, 10, 15))#candidate|7070|(5, 10, 15)|var|float64
var_7071 = relay.var("var_7071", dtype = "float64", shape = (5, 10, 15))#candidate|7071|(5, 10, 15)|var|float64
output = func_7069(var_7070,var_7071,)
func_7072 = relay.Function([var_7070,var_7071,], output)
mutated_mod['func_7072'] = func_7072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_223_call = mod.get_global_var('func_223')
func_224_call = mutated_mod.get_global_var('func_224')
call_7142 = relay.TupleGetItem(func_223_call(), 0)
call_7143 = relay.TupleGetItem(func_224_call(), 0)
output = relay.Tuple([call_7142,])
output2 = relay.Tuple([call_7143,])
func_7150 = relay.Function([], output)
mod['func_7150'] = func_7150
mod = relay.transform.InferType()(mod)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7150_call = mutated_mod.get_global_var('func_7150')
call_7151 = func_7150_call()
output = call_7151
func_7152 = relay.Function([], output)
mutated_mod['func_7152'] = func_7152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1979_call = mod.get_global_var('func_1979')
func_1981_call = mutated_mod.get_global_var('func_1981')
call_7158 = func_1979_call()
call_7159 = func_1979_call()
output = relay.Tuple([call_7158,])
output2 = relay.Tuple([call_7159,])
func_7168 = relay.Function([], output)
mod['func_7168'] = func_7168
mod = relay.transform.InferType()(mod)
mutated_mod['func_7168'] = func_7168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7168_call = mutated_mod.get_global_var('func_7168')
call_7169 = func_7168_call()
output = call_7169
func_7170 = relay.Function([], output)
mutated_mod['func_7170'] = func_7170
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7184 = relay.var("var_7184", dtype = "uint32", shape = (8, 15, 15))#candidate|7184|(8, 15, 15)|var|uint32
var_7185 = relay.var("var_7185", dtype = "uint32", shape = (8, 15, 15))#candidate|7185|(8, 15, 15)|var|uint32
bop_7186 = relay.bitwise_or(var_7184.astype('uint32'), relay.reshape(var_7185.astype('uint32'), relay.shape_of(var_7184))) # shape=(8, 15, 15)
func_1979_call = mod.get_global_var('func_1979')
func_1981_call = mutated_mod.get_global_var('func_1981')
call_7199 = func_1979_call()
call_7200 = func_1979_call()
func_3226_call = mod.get_global_var('func_3226')
func_3229_call = mutated_mod.get_global_var('func_3229')
var_7256 = relay.var("var_7256", dtype = "float64", shape = ())#candidate|7256|()|var|float64
call_7255 = relay.TupleGetItem(func_3226_call(relay.reshape(var_7256.astype('float64'), [])), 3)
call_7257 = relay.TupleGetItem(func_3229_call(relay.reshape(var_7256.astype('float64'), [])), 3)
output = relay.Tuple([bop_7186,call_7199,call_7255,var_7256,])
output2 = relay.Tuple([bop_7186,call_7200,call_7257,var_7256,])
func_7259 = relay.Function([var_7184,var_7185,var_7256,], output)
mod['func_7259'] = func_7259
mod = relay.transform.InferType()(mod)
mutated_mod['func_7259'] = func_7259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7259_call = mutated_mod.get_global_var('func_7259')
var_7261 = relay.var("var_7261", dtype = "uint32", shape = (8, 15, 15))#candidate|7261|(8, 15, 15)|var|uint32
var_7262 = relay.var("var_7262", dtype = "uint32", shape = (8, 15, 15))#candidate|7262|(8, 15, 15)|var|uint32
var_7263 = relay.var("var_7263", dtype = "float64", shape = ())#candidate|7263|()|var|float64
call_7260 = func_7259_call(var_7261,var_7262,var_7263,)
output = call_7260
func_7264 = relay.Function([var_7261,var_7262,var_7263,], output)
mutated_mod['func_7264'] = func_7264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4119_call = mod.get_global_var('func_4119')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_7275 = relay.TupleGetItem(func_4119_call(), 0)
call_7276 = relay.TupleGetItem(func_4120_call(), 0)
func_4119_call = mod.get_global_var('func_4119')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_7291 = relay.TupleGetItem(func_4119_call(), 0)
call_7292 = relay.TupleGetItem(func_4120_call(), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_7312 = relay.TupleGetItem(func_1112_call(), 0)
call_7313 = relay.TupleGetItem(func_1113_call(), 0)
func_497_call = mod.get_global_var('func_497')
func_499_call = mutated_mod.get_global_var('func_499')
call_7324 = relay.TupleGetItem(func_497_call(), 0)
call_7325 = relay.TupleGetItem(func_499_call(), 0)
func_7168_call = mod.get_global_var('func_7168')
func_7170_call = mutated_mod.get_global_var('func_7170')
call_7333 = relay.TupleGetItem(func_7168_call(), 0)
call_7334 = relay.TupleGetItem(func_7170_call(), 0)
output = relay.Tuple([call_7275,call_7291,call_7312,call_7324,call_7333,])
output2 = relay.Tuple([call_7276,call_7292,call_7313,call_7325,call_7334,])
func_7340 = relay.Function([], output)
mod['func_7340'] = func_7340
mod = relay.transform.InferType()(mod)
mutated_mod['func_7340'] = func_7340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7340_call = mutated_mod.get_global_var('func_7340')
call_7341 = func_7340_call()
output = call_7341
func_7342 = relay.Function([], output)
mutated_mod['func_7342'] = func_7342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
call_7355 = relay.TupleGetItem(func_759_call(), 1)
call_7356 = relay.TupleGetItem(func_761_call(), 1)
output = relay.Tuple([call_7355,])
output2 = relay.Tuple([call_7356,])
func_7360 = relay.Function([], output)
mod['func_7360'] = func_7360
mod = relay.transform.InferType()(mod)
mutated_mod['func_7360'] = func_7360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7360_call = mutated_mod.get_global_var('func_7360')
call_7361 = func_7360_call()
output = call_7361
func_7362 = relay.Function([], output)
mutated_mod['func_7362'] = func_7362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1822_call = mod.get_global_var('func_1822')
func_1824_call = mutated_mod.get_global_var('func_1824')
call_7434 = relay.TupleGetItem(func_1822_call(), 1)
call_7435 = relay.TupleGetItem(func_1824_call(), 1)
func_7069_call = mod.get_global_var('func_7069')
func_7072_call = mutated_mod.get_global_var('func_7072')
var_7443 = relay.var("var_7443", dtype = "float64", shape = (750,))#candidate|7443|(750,)|var|float64
call_7442 = relay.TupleGetItem(func_7069_call(relay.reshape(var_7443.astype('float64'), [5, 10, 15]), relay.reshape(var_7443.astype('float64'), [5, 10, 15]), ), 0)
call_7444 = relay.TupleGetItem(func_7072_call(relay.reshape(var_7443.astype('float64'), [5, 10, 15]), relay.reshape(var_7443.astype('float64'), [5, 10, 15]), ), 0)
func_376_call = mod.get_global_var('func_376')
func_377_call = mutated_mod.get_global_var('func_377')
call_7448 = relay.TupleGetItem(func_376_call(), 0)
call_7449 = relay.TupleGetItem(func_377_call(), 0)
output = relay.Tuple([call_7434,call_7442,var_7443,call_7448,])
output2 = relay.Tuple([call_7435,call_7444,var_7443,call_7449,])
func_7450 = relay.Function([var_7443,], output)
mod['func_7450'] = func_7450
mod = relay.transform.InferType()(mod)
mutated_mod['func_7450'] = func_7450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7451 = relay.var("var_7451", dtype = "float64", shape = (750,))#candidate|7451|(750,)|var|float64
func_7450_call = mutated_mod.get_global_var('func_7450')
call_7452 = func_7450_call(var_7451)
output = call_7452
func_7453 = relay.Function([var_7451], output)
mutated_mod['func_7453'] = func_7453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5460_call = mod.get_global_var('func_5460')
func_5462_call = mutated_mod.get_global_var('func_5462')
call_7500 = relay.TupleGetItem(func_5460_call(), 0)
call_7501 = relay.TupleGetItem(func_5462_call(), 0)
func_1200_call = mod.get_global_var('func_1200')
func_1201_call = mutated_mod.get_global_var('func_1201')
call_7504 = relay.TupleGetItem(func_1200_call(), 0)
call_7505 = relay.TupleGetItem(func_1201_call(), 0)
func_4065_call = mod.get_global_var('func_4065')
func_4067_call = mutated_mod.get_global_var('func_4067')
call_7508 = relay.TupleGetItem(func_4065_call(), 0)
call_7509 = relay.TupleGetItem(func_4067_call(), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_7512 = relay.TupleGetItem(func_1112_call(), 0)
call_7513 = relay.TupleGetItem(func_1113_call(), 0)
output = relay.Tuple([call_7500,call_7504,call_7508,call_7512,])
output2 = relay.Tuple([call_7501,call_7505,call_7509,call_7513,])
func_7526 = relay.Function([], output)
mod['func_7526'] = func_7526
mod = relay.transform.InferType()(mod)
output = func_7526()
func_7527 = relay.Function([], output)
mutated_mod['func_7527'] = func_7527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5859_call = mod.get_global_var('func_5859')
func_5860_call = mutated_mod.get_global_var('func_5860')
call_7528 = relay.TupleGetItem(func_5859_call(), 1)
call_7529 = relay.TupleGetItem(func_5860_call(), 1)
output = call_7528
output2 = call_7529
func_7538 = relay.Function([], output)
mod['func_7538'] = func_7538
mod = relay.transform.InferType()(mod)
output = func_7538()
func_7539 = relay.Function([], output)
mutated_mod['func_7539'] = func_7539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6107_call = mod.get_global_var('func_6107')
func_6109_call = mutated_mod.get_global_var('func_6109')
call_7595 = relay.TupleGetItem(func_6107_call(), 1)
call_7596 = relay.TupleGetItem(func_6109_call(), 1)
func_7450_call = mod.get_global_var('func_7450')
func_7453_call = mutated_mod.get_global_var('func_7453')
const_7605 = relay.const([[-5.810380,-9.638903,8.086146,4.065395,3.746756,3.345555,8.045447,8.003785,8.507160,-6.456862,-6.331325,-8.786590,-3.649639,-1.274423,-5.509580],[1.130172,3.295289,1.293014,8.389367,-5.472973,-7.348368,-4.054323,-3.596078,2.946586,-0.092487,-7.151494,5.192868,-0.794264,-2.186610,-7.826170],[7.490118,-0.286020,6.661272,-0.822703,-8.824032,-4.162460,-3.482465,-9.315670,-4.994331,-1.674572,8.489327,8.515433,-2.679539,-1.969652,9.258792],[8.530058,0.949360,0.858502,0.620700,9.136667,4.591356,-2.109681,-0.231708,-8.704891,-4.496934,6.463125,5.199470,-1.899669,5.574940,5.807532],[-6.446714,7.296776,-9.352669,-5.664941,-3.254117,2.707273,4.868085,7.548313,-6.514365,3.213688,1.797325,-3.871084,8.067922,-7.205825,-4.726785],[3.392102,-8.035165,-9.924525,-0.087104,1.143863,-7.328735,-6.101647,-5.555959,5.354259,7.545720,-1.587821,-9.212656,4.105310,4.999425,-4.451460],[3.113565,-2.829559,-7.394123,-6.612103,-4.217546,-2.336802,-0.648957,-3.943031,-0.332777,2.051051,-3.573862,-5.070947,5.160690,9.526208,6.163779],[-8.186807,2.987451,7.981280,1.922469,-9.490580,0.655146,-9.210321,6.427170,-7.700190,-2.394201,6.345710,3.272395,1.785433,-3.570244,-1.476608],[-5.861675,-7.700390,9.958473,-3.186386,-1.415324,-0.800025,8.473838,8.477954,-9.743285,-7.968600,-8.974202,9.434936,-2.607876,-0.829421,6.310277],[-0.933540,3.852666,-7.351447,-1.309409,8.241696,4.745972,-2.496858,-1.056441,-7.792488,-8.351793,0.546315,-1.632832,-8.960231,-3.946880,7.054147],[3.124482,2.673982,4.369484,-5.116409,-9.250925,-0.620265,0.417319,-1.761052,-6.052753,-8.875174,-3.277893,6.701352,0.631029,1.791082,-1.678546],[8.653395,-0.625506,-1.848191,-1.284946,-0.281441,-9.001752,1.389413,1.653828,3.789290,-4.097621,-1.433880,-7.214841,5.964509,-6.889280,3.513188],[-3.410410,-5.636619,7.420876,-3.272338,4.060059,1.277827,4.390585,-1.573980,-7.119008,-2.208391,3.666581,3.955394,5.753450,8.497358,9.000852],[-0.769285,-0.771646,2.690927,-1.884512,3.491873,-3.367948,8.881192,2.785094,-2.356798,-9.528943,-5.222694,-4.109976,5.892685,1.019062,6.273405],[3.114741,-4.770587,-1.544294,5.651963,5.936242,7.118935,3.370704,9.723939,-6.308097,7.551222,-6.908595,-4.963954,3.234979,-0.159469,4.514598],[-8.774429,-5.690714,-6.911398,-5.204223,7.664399,-5.596805,7.583649,2.787950,0.107730,-3.921506,-8.055988,-5.366059,6.613574,-3.138763,-9.935011],[4.590171,-9.591608,2.832092,9.138896,4.266280,5.559388,5.571154,6.060473,2.576766,-9.584609,3.065766,1.914948,3.318722,-8.101707,-4.547221],[1.270616,2.953453,3.924380,-9.005783,-6.872666,7.645802,-3.549308,-1.337719,-3.116623,-1.565076,4.663163,8.439220,7.476355,-3.920203,4.887772],[5.644891,-1.919565,-2.456056,5.960026,-5.233022,-8.300751,-3.249479,-1.586818,9.777848,-3.840676,5.513764,8.835698,-6.481318,-4.969465,-7.126014],[-7.204784,-6.668921,-2.128174,-5.266919,-3.291661,0.905239,0.935928,3.911881,-3.924116,-4.825542,-4.313612,8.921725,-3.733767,-0.124906,-6.548388],[-4.729388,-5.854029,7.449926,-5.855482,8.422072,4.009748,6.462375,-1.729526,-3.488795,2.922512,0.567243,7.672058,-4.421351,5.946026,-2.219788],[1.995235,-3.441172,3.925288,9.923697,9.553970,-6.746393,9.296794,1.438805,-2.865181,6.984103,-6.220715,1.111476,4.935096,-9.869464,9.780527],[-4.138840,9.207780,-9.416551,-5.364658,-5.072425,-6.858928,-7.686337,2.586420,4.230907,-1.647242,3.997632,-8.481454,-1.038730,-7.142711,-3.831517],[1.921234,6.070805,7.039926,4.177755,8.904238,0.628463,9.787453,7.919944,-8.167757,-5.236249,9.022157,4.823718,7.340061,1.673896,-3.094225],[3.248698,-0.425325,5.220571,-7.056659,-1.853115,-3.524990,-7.002586,2.315705,-0.554129,-5.339495,-4.490371,4.687079,3.972375,5.884581,-5.820268],[-7.499700,5.400685,-9.513589,-0.276703,-8.039553,-5.622147,3.918407,-5.492575,3.701147,-0.253594,8.320588,1.312314,-4.305749,6.692375,-9.117759],[-3.744775,7.453935,8.933065,-3.741319,0.715202,-1.838408,7.021348,-5.115173,8.223755,0.574998,8.250973,-2.737690,4.950527,-4.103492,5.110009],[-5.305477,6.905384,5.951527,-1.406719,0.163175,-4.574748,9.595973,4.533103,8.253995,5.612283,-2.577212,-0.809557,-3.093979,4.809956,-2.427507],[1.001744,-6.237254,8.138418,3.603771,4.535491,9.248022,2.623006,-9.331601,-9.992886,2.481927,-4.189227,-2.795950,-7.395431,-5.962997,1.903436],[-1.827170,8.736605,-7.749731,0.119114,-5.636561,-8.299533,-9.917480,2.976631,-0.721929,8.117966,1.913968,7.709902,-6.849876,-1.290599,2.960366],[8.986225,-8.380326,1.449321,3.098944,0.238358,3.642480,7.572234,2.722341,-6.663385,-7.724834,0.672208,2.134354,-6.558539,-7.692957,-0.172682],[-4.864274,-3.760594,0.161490,9.267932,-7.879306,-8.644724,-5.706499,8.258890,-4.313147,1.002262,4.006329,2.611623,0.502513,-9.465893,-6.465366],[-5.083164,2.773607,-8.955449,-7.198678,0.944516,-3.350641,-2.588158,-4.944455,-3.766568,-9.951473,7.027291,-4.703942,-0.520725,-3.058315,6.655255],[-2.770498,-1.993570,-9.236206,-3.257409,-9.877787,1.462463,4.104998,-5.943926,-8.665638,8.582183,-6.036795,-5.171069,2.131931,9.219617,-1.764425],[-7.449935,-9.126126,-8.667603,4.029047,9.708213,-2.112100,-7.784830,-5.372154,8.649588,5.617680,4.262683,-5.340074,-2.229899,5.112715,0.044049],[7.536167,-8.346761,-2.693742,-6.948747,7.266622,-3.849400,9.609496,4.986157,2.491203,-4.295792,1.200417,-0.786818,5.118972,7.605952,-6.743562],[-2.145006,8.890238,4.019733,8.691084,4.611734,4.321335,1.829956,5.257488,8.057335,5.417152,1.149536,2.518616,-4.696283,1.571321,9.380442],[7.481561,7.280868,-8.431152,-3.796597,-1.400533,-6.945150,9.409719,-6.949963,5.010374,1.307897,4.876311,8.893964,6.419122,-6.158614,-1.656129],[-4.133812,3.737066,-2.556759,7.684673,-6.936404,-2.960397,9.015885,-2.022158,-1.829361,6.896193,-7.852648,8.590828,-4.500272,-4.544649,0.344278],[-6.991231,-7.623070,0.544161,-8.057826,9.949173,-1.801404,8.979848,-7.127913,-5.044188,7.710274,-5.205224,-6.013464,-1.594096,-5.821260,0.992016],[9.099917,-7.519254,-4.809819,-8.153163,-7.332544,1.969974,9.403084,-2.512646,-0.945871,1.245927,9.424740,3.680965,1.979113,-5.319693,-2.717848],[2.437223,6.660270,7.311751,5.498980,-8.380532,-5.593648,-7.005327,8.687490,8.462050,4.208665,6.466218,-8.162061,5.246061,-1.233801,-2.268437],[5.170426,-3.960821,6.694540,-4.994580,3.745998,-6.020163,-0.154382,-5.076654,0.728529,5.948761,-6.036255,6.872705,-4.135234,-8.269487,-5.720303],[9.429789,-0.613758,1.947486,-1.910377,-1.842338,-9.225165,5.953548,6.300947,-7.811257,9.047844,-3.402353,9.549406,-3.615436,-8.283657,-2.831349],[1.492013,-2.721346,-7.650216,8.064737,-1.821251,-3.380838,-4.981945,3.908871,3.437893,7.570785,-8.491766,-4.404164,0.259605,4.680978,9.910078],[1.400071,3.912732,-3.061637,4.878962,-0.238732,2.839552,-4.502669,-6.072417,-9.518223,-9.725333,-5.107622,2.839200,-3.938099,-4.213929,-2.728784],[3.753309,-9.429926,7.573819,-4.701307,4.897332,-8.950120,-8.938165,-2.642794,4.902292,-7.592400,-3.745472,-1.773129,-9.301264,3.187856,-1.222775],[-7.218184,2.560380,-9.882517,-0.837594,4.727704,-2.125824,-7.221040,-4.531811,4.524251,9.267728,7.656073,5.111036,0.058422,-1.718181,-4.883316],[-2.675488,3.399112,5.341887,2.966657,-8.613351,3.766825,-9.902593,7.434569,9.295396,-8.813245,4.755029,-7.736972,3.095567,-9.371767,-5.807673],[-6.622871,2.696441,-0.989224,-1.232439,-5.753390,-2.828041,0.061245,-5.430626,-6.062912,9.709603,-9.196317,-8.881649,8.835520,5.514235,-4.730498]], dtype = "float64")#candidate|7605|(50, 15)|const|float64
call_7604 = relay.TupleGetItem(func_7450_call(relay.reshape(const_7605.astype('float64'), [750,])), 0)
call_7606 = relay.TupleGetItem(func_7453_call(relay.reshape(const_7605.astype('float64'), [750,])), 0)
var_7610 = relay.var("var_7610", dtype = "int16", shape = (2, 14, 10))#candidate|7610|(2, 14, 10)|var|int16
bop_7611 = relay.divide(call_7595.astype('float32'), relay.reshape(var_7610.astype('float32'), relay.shape_of(call_7595))) # shape=(2, 14, 10)
bop_7614 = relay.divide(call_7596.astype('float32'), relay.reshape(var_7610.astype('float32'), relay.shape_of(call_7596))) # shape=(2, 14, 10)
func_1979_call = mod.get_global_var('func_1979')
func_1981_call = mutated_mod.get_global_var('func_1981')
call_7620 = func_1979_call()
call_7621 = func_1979_call()
output = relay.Tuple([call_7604,const_7605,bop_7611,call_7620,])
output2 = relay.Tuple([call_7606,const_7605,bop_7614,call_7621,])
func_7638 = relay.Function([var_7610,], output)
mod['func_7638'] = func_7638
mod = relay.transform.InferType()(mod)
var_7639 = relay.var("var_7639", dtype = "int16", shape = (2, 14, 10))#candidate|7639|(2, 14, 10)|var|int16
output = func_7638(var_7639)
func_7640 = relay.Function([var_7639], output)
mutated_mod['func_7640'] = func_7640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_7645 = relay.TupleGetItem(func_1958_call(), 0)
call_7646 = relay.TupleGetItem(func_1960_call(), 0)
func_5692_call = mod.get_global_var('func_5692')
func_5693_call = mutated_mod.get_global_var('func_5693')
call_7649 = relay.TupleGetItem(func_5692_call(), 0)
call_7650 = relay.TupleGetItem(func_5693_call(), 0)
output = relay.Tuple([call_7645,call_7649,])
output2 = relay.Tuple([call_7646,call_7650,])
func_7659 = relay.Function([], output)
mod['func_7659'] = func_7659
mod = relay.transform.InferType()(mod)
output = func_7659()
func_7660 = relay.Function([], output)
mutated_mod['func_7660'] = func_7660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_568_call = mod.get_global_var('func_568')
func_570_call = mutated_mod.get_global_var('func_570')
call_7710 = relay.TupleGetItem(func_568_call(), 2)
call_7711 = relay.TupleGetItem(func_570_call(), 2)
func_2602_call = mod.get_global_var('func_2602')
func_2603_call = mutated_mod.get_global_var('func_2603')
call_7737 = relay.TupleGetItem(func_2602_call(), 0)
call_7738 = relay.TupleGetItem(func_2603_call(), 0)
func_1451_call = mod.get_global_var('func_1451')
func_1454_call = mutated_mod.get_global_var('func_1454')
var_7755 = relay.var("var_7755", dtype = "float32", shape = (576, 4))#candidate|7755|(576, 4)|var|float32
call_7754 = relay.TupleGetItem(func_1451_call(relay.reshape(var_7755.astype('float32'), [12, 16, 12])), 1)
call_7756 = relay.TupleGetItem(func_1454_call(relay.reshape(var_7755.astype('float32'), [12, 16, 12])), 1)
func_7150_call = mod.get_global_var('func_7150')
func_7152_call = mutated_mod.get_global_var('func_7152')
call_7760 = relay.TupleGetItem(func_7150_call(), 0)
call_7761 = relay.TupleGetItem(func_7152_call(), 0)
uop_7772 = relay.sigmoid(call_7754.astype('float32')) # shape=(12, 16, 12)
uop_7774 = relay.sigmoid(call_7756.astype('float32')) # shape=(12, 16, 12)
func_2121_call = mod.get_global_var('func_2121')
func_2123_call = mutated_mod.get_global_var('func_2123')
call_7797 = relay.TupleGetItem(func_2121_call(), 3)
call_7798 = relay.TupleGetItem(func_2123_call(), 3)
var_7800 = relay.var("var_7800", dtype = "float32", shape = (12, 16, 12))#candidate|7800|(12, 16, 12)|var|float32
bop_7801 = relay.left_shift(uop_7772.astype('int32'), relay.reshape(var_7800.astype('int32'), relay.shape_of(uop_7772))) # shape=(12, 16, 12)
bop_7804 = relay.left_shift(uop_7774.astype('int32'), relay.reshape(var_7800.astype('int32'), relay.shape_of(uop_7774))) # shape=(12, 16, 12)
uop_7807 = relay.acosh(call_7754.astype('float64')) # shape=(12, 16, 12)
uop_7809 = relay.acosh(call_7756.astype('float64')) # shape=(12, 16, 12)
output = relay.Tuple([call_7710,call_7737,var_7755,call_7760,call_7797,bop_7801,uop_7807,])
output2 = relay.Tuple([call_7711,call_7738,var_7755,call_7761,call_7798,bop_7804,uop_7809,])
func_7814 = relay.Function([var_7755,var_7800,], output)
mod['func_7814'] = func_7814
mod = relay.transform.InferType()(mod)
mutated_mod['func_7814'] = func_7814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7814_call = mutated_mod.get_global_var('func_7814')
var_7816 = relay.var("var_7816", dtype = "float32", shape = (576, 4))#candidate|7816|(576, 4)|var|float32
var_7817 = relay.var("var_7817", dtype = "float32", shape = (12, 16, 12))#candidate|7817|(12, 16, 12)|var|float32
call_7815 = func_7814_call(var_7816,var_7817,)
output = call_7815
func_7818 = relay.Function([var_7816,var_7817,], output)
mutated_mod['func_7818'] = func_7818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4819_call = mod.get_global_var('func_4819')
func_4820_call = mutated_mod.get_global_var('func_4820')
call_7826 = func_4819_call()
call_7827 = func_4819_call()
output = relay.Tuple([call_7826,])
output2 = relay.Tuple([call_7827,])
func_7828 = relay.Function([], output)
mod['func_7828'] = func_7828
mod = relay.transform.InferType()(mod)
mutated_mod['func_7828'] = func_7828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7828_call = mutated_mod.get_global_var('func_7828')
call_7829 = func_7828_call()
output = call_7829
func_7830 = relay.Function([], output)
mutated_mod['func_7830'] = func_7830
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7851 = relay.var("var_7851", dtype = "int64", shape = (7, 8, 4))#candidate|7851|(7, 8, 4)|var|int64
const_7852 = relay.const([[[10,-3,-5,-9],[2,-7,-2,2],[5,5,-7,3],[-4,6,9,-1],[-5,-1,9,-1],[7,7,1,1],[5,5,10,-8],[8,8,1,10]],[[6,-10,3,-4],[-1,10,-4,2],[-10,-9,-5,-7],[-4,-2,-4,1],[-6,-3,-2,1],[-9,7,-5,3],[6,-6,-1,-5],[7,10,-2,9]],[[3,6,10,1],[2,3,9,-1],[-9,5,1,7],[-7,-7,-9,6],[-10,-9,2,10],[-8,-1,10,-1],[10,-9,7,-9],[4,-3,4,-6]],[[2,7,-5,-9],[-1,-1,2,-1],[9,-5,5,-3],[2,3,5,-2],[-3,2,7,3],[2,2,8,-8],[3,-5,7,-9],[-4,-7,-10,-8]],[[10,-2,-3,-9],[-1,-1,-4,5],[-2,6,-10,10],[-7,-3,-6,3],[2,4,-10,-10],[-4,9,-8,5],[-7,-1,8,-1],[8,6,-6,3]],[[4,-1,2,5],[-10,6,-1,10],[-4,6,-4,-10],[2,10,3,-6],[-1,-1,-8,-1],[-5,10,9,-3],[-3,-6,-6,1],[10,-6,5,10]],[[-8,-10,-1,7],[-9,-1,7,1],[3,-8,2,8],[3,7,-5,5],[-9,-10,-10,-8],[3,7,-3,1],[6,6,-9,1],[10,1,4,9]]], dtype = "int64")#candidate|7852|(7, 8, 4)|const|int64
bop_7853 = relay.not_equal(var_7851.astype('bool'), relay.reshape(const_7852.astype('bool'), relay.shape_of(var_7851))) # shape=(7, 8, 4)
func_2602_call = mod.get_global_var('func_2602')
func_2603_call = mutated_mod.get_global_var('func_2603')
call_7861 = relay.TupleGetItem(func_2602_call(), 0)
call_7862 = relay.TupleGetItem(func_2603_call(), 0)
uop_7867 = relay.log2(bop_7853.astype('float64')) # shape=(7, 8, 4)
uop_7872 = relay.log(uop_7867.astype('float32')) # shape=(7, 8, 4)
func_5435_call = mod.get_global_var('func_5435')
func_5439_call = mutated_mod.get_global_var('func_5439')
const_7890 = relay.const([-8.675711,7.052957,-5.377280,-5.244279,6.343159,3.539944,0.310304,6.702266,7.066265,-1.754067,5.633288,6.111548,5.760891,9.325976,0.133108,7.905710,-7.155750,7.231363,-5.918511,5.520446,9.325575,-1.321473,-7.696077,-7.117023,7.935094,5.697923,9.411480,-9.745448,3.340512,6.408037,-7.663440,6.911238,0.889493,7.015208,-9.074085,9.322273,3.633332,-0.280763,9.482416,6.746958,8.479716,7.797057,-2.815783,4.675564,-7.091454,-7.601058,6.135858,1.471583,-8.262009,5.803326,8.655032,-6.572763,-5.749438,8.492968,-4.094349,-1.061073,3.246606,-0.671003,6.678756,6.771254,-2.207658,3.458819,3.429782,-7.570499,6.517178,-0.356149,-3.541870,-4.064630,2.540502,-7.749153,-2.487247,2.371119,1.739346,3.465454,8.743497,-4.159622,8.821198,-4.288213,-1.828089,-5.020363,-7.714578,3.910990,-9.842660,6.022559,3.189495,8.998178,-4.238757,2.239674,-4.242526,3.074907,3.161379,9.544852,8.074990,-3.639783,-2.939658,4.895196,9.935806,0.480848,-3.279614,-8.552974,-3.347211,-2.043841,-1.378929,-1.145597,-4.626881,5.842295,1.161506,-8.872430,-3.321240,4.301624,-7.418948,9.522130,3.807327,5.015899,5.291288,1.710956,7.370967,-8.129922,1.684663,-4.011618,-3.394791,3.366716,-8.123483,-4.778532,-5.237274,7.288118,4.816425,3.722312,5.217755,-8.487517,-6.850406,-4.817326,1.863360,9.641756,-4.016557,2.590996,1.711291,-0.430920,-2.232712,-3.734788,-0.115450,9.208488,-6.218090,-9.808535,1.329995,-8.765196,-1.512469,7.348175,-7.390882,-8.025105,-0.062818,6.821417,1.791864,7.013318,3.213400,-1.762714,9.196846,4.642387,-5.818329,9.033756,-9.404392,3.645756,9.463310,4.100887,-8.880823,-0.508212,5.488280,-5.141694,2.824374,-8.145869,-0.512199,1.836890,6.803958,9.025453,-5.283929,2.625508,3.083859,-6.782831,-0.855328,-8.784707,8.145293,8.857685,-0.716335,4.933278,-3.210623,-4.427274,6.047206,-9.681800,-6.811128,-0.333754,7.818034,-8.116826,5.435629,4.836430,-2.844360,-5.797617,-5.121649,-2.451878,5.515466,-5.959724,4.256108,-7.792434,-9.170137,0.812510,1.904724,-2.619263,-3.820992,1.946741,5.301351,8.926403,-8.590801,3.122273,7.780301,4.438126,-1.782495,-5.060750,9.345485,-9.722537,-6.790228,-1.610993,7.046067,-9.682999,0.108637,5.051701,-4.885809,-1.185949,-1.400144,5.738490,5.877634,4.167410,-9.150150,-9.865476,-1.394697,-9.573146,-7.448012,-3.564740,8.571759,6.091648,-1.395816,6.858722,0.547570,5.548966,8.027027,-1.768847,-8.041726,-1.723795,2.203360,-5.506599,7.253409,-6.623532,3.344503,-7.324586,5.105097,-2.989532,-4.083755,-9.996478,3.435107,-3.862940,-9.673969,-2.784964,-0.455909,-6.872315,0.178710,1.034986,9.441938,-3.476174,3.175392,8.086536,0.643829,-3.998359,9.436964,6.473855,8.733486,0.215301,-1.061292,-5.932032,6.042219,2.163592,4.303271,1.045233,-8.007184,2.991801,-3.974954,5.084818,-5.600335,-1.781050,-2.371940,8.715421,3.153416,-2.372239,-0.549832,-5.351071,7.722002,-6.862297,-3.191222,6.001784,1.537685,-2.699948,4.057070,0.975478,-9.777123,4.914096,-9.447894,-3.918191,9.839118,4.640625,1.467198,5.986695,4.666397,1.575996,-0.519636,3.616709,6.351948,5.365266,2.896638,8.744289,-5.661354,-8.997334,8.425786,-0.510333,8.837985,-7.314440,2.364557,8.109184,2.487159,8.337345,5.175969,5.740699,-3.234671,1.543190,-5.527811,1.636256,3.638313,6.701621,-7.038635,-8.471728,2.595848,-0.118887,-5.186186,-3.087277,-2.652731,4.651636,-3.026452,4.753570,-2.032146,-9.191867,1.007882,7.425975,8.795892,6.055542,0.849275,-7.353684,-9.322304,1.523943,-5.205560,-0.233726,5.524578,5.008000,-8.509355,1.573053,3.576796,8.897032,5.301607,-3.640866,7.237036,2.432942,2.019771,-4.572393,-7.668674,-9.231356,6.786898,-1.880352,6.692518,-7.377968,-0.827633,-5.578923,1.525250,-8.233238,-9.645135,6.697561,-0.159908,-3.921962,-4.437340,1.784456,5.412055,-0.678237,-9.247133,7.163005,-1.993905,1.340944,8.001565,-4.910997,-9.289940,-5.642059,7.649660,-1.961385,-7.543776,2.662078,8.808603,1.391143,9.426120,2.213514,-6.938464,5.171240,-4.659248,4.802500,-3.410240,-4.976211,-5.256286,7.601988,6.560999,5.981372,2.451343,-0.516569,7.161059,2.580567,3.905224,-7.829779,5.081626,-5.793059,1.138259,-0.043026,-3.865734,-9.857706,8.422348,-8.578960,1.311313,-1.984939,3.785012,-8.580323,-1.869294,1.441142,-1.944780,-4.321651,0.573610,-3.941102,-3.155994,-8.243995,1.812266,-2.564364,-9.862433,7.621808,-0.688276,-7.336613,1.357072,0.006792,-6.860430,9.547429,-9.275982,5.472516,4.857386,-7.529226,-4.820886,-0.002428,6.556498,-7.564547,6.852990,-4.733435,5.901603,3.339238,8.795703,-9.700975,3.991197,-1.767629,8.673571,5.339744,0.286380,9.111947,-0.989810,-0.911729,-2.628562,-6.163077,-3.630656,4.361272,4.324454,-9.306769,8.566296,7.007553,7.448395,1.022358,4.307520,3.986992,-8.694421,-9.192506,-1.489494,2.355833,2.617543,-1.982051,-5.447369,4.023152,8.632000,-1.517892,-2.488249,0.020857,0.973213,4.133740,-6.292686,-6.160378,0.463526,5.126277,4.747067,-7.783121,-6.563197,-5.450297,-1.971961,6.870392,-8.414225,9.605366,8.573694,-8.746276,9.096489,4.885648,-2.251550,-4.512985,-8.860811,3.747530,-1.717299,-3.466424,-6.862027,0.087373,-8.543330,-7.891982,-5.427154,8.181499,7.121879,0.380250,3.129656,-6.627599,-6.374782,6.487224,-4.640489,-4.262056,-0.743943,-7.480075,7.612712,-2.935724,-8.556635,-9.377864,-8.757528,-7.885456,6.424524,-8.029874,-7.489678,-9.772745,4.244510,3.316071,-3.091180,0.083922,-4.501158,-0.438827,7.329803,3.378238,0.365637,3.852903,0.381401,7.333593,7.602865,-9.487348,-7.095387,-3.980619,-6.791022,-4.185425,8.916317,-6.783080,6.423584,7.673616,3.567308,-0.280700,9.691879,-3.891385,7.798061,5.020719,6.512039,-5.422064,1.162274,4.436409,-6.282325,-4.833959,0.499109,1.742712,0.855558,-7.504807,4.365491,-3.639811,-9.885068,0.170650,-6.878736,-0.433924,-7.148279,-0.934416,2.190802,-4.019544,3.061272,9.176010,7.442323,2.331285,6.445410,9.389547,-8.014414,2.529348,-8.649404,-6.310277,-1.880386,-0.545744,2.949630,-4.578045,-6.321522,-0.601246,0.595162,9.744361,-6.807408,-3.544299,-1.996699,-9.516576,4.470189,6.521333,-9.131387,-5.849400,-4.218275,-6.598366,1.534133,-4.887177,8.765272,4.976431,-1.509143,6.947070,9.703544,-3.798296,5.457168,-9.914535,9.799479,-6.059751,1.133609,-6.372535,9.010837,0.062917,7.104080,-9.957027,-7.153319,4.468884,-9.596848,2.066216,-3.528269,8.998769,-8.471898,-0.193229,1.490040,-2.458209,-6.294398,-5.643002,6.467594,-7.078615,5.581285,3.367917,4.571811,-5.551195,5.679202,5.845652,-8.414754,2.618162,2.961857,-1.897569,-4.220613,2.138531,8.163893,-9.369759,-2.288855,2.588439,4.628002,4.290644,0.481167,8.232534,-0.766720,1.597697,7.515208,6.003456,-6.353303,-7.906776,-8.216818,6.548429,7.394182,-0.176108,0.434325,-6.321559,-7.004308,5.117385,1.165522,-2.375725,2.419006,-1.404139,-8.291065,3.097747,5.672470,5.328252,-5.473316,6.708772,-5.955538,1.669404,5.184026,7.964804,8.456799,-3.330777,3.047627,-0.882215,-7.224961,2.989933,4.571798,0.185991,-3.251654,-9.417819,-1.160763,6.937331,-6.823102,-9.117420,-1.598844,6.274396,-5.765498,-8.929662,9.241822,-0.852959,-9.521999,-0.885447,7.287904,-5.268155,0.814483,-0.737308,7.153882,-8.445936,-0.843157,7.584840,-2.317634,-2.146821,-1.377177,-2.203501,-3.271438,7.518830,8.843216,-5.348606,-2.475731,-1.516667,0.123180,0.375655,-6.111392,-0.958626,-5.104331,8.207239,3.471676,0.133982,4.830227,3.717898,-5.583749,-9.360069,-4.914314,-5.435043,1.564635,-4.279580,6.170269,3.100050,-5.658650,-8.256576,-6.210101,7.156409,-4.471332,1.924002,0.602111,1.967071,-3.951717,8.667037,-6.391052,1.725200,-8.108249,-6.897763,9.071019,-9.694118,-3.695141,-0.117798,-8.272506,-4.093322,-7.023858,-1.114096,-4.094512,6.408316,4.459427,8.309721,6.785633,-9.878184,5.915922,8.595377,-1.813410,-3.171344,2.434723,8.938303,-5.963477,-0.348497,-7.042535,-8.090682,-9.247323,2.554212,-6.585114,6.143700,9.765100,-7.206330,-2.956517,5.627804,0.221505,0.245803,-7.237625,-5.730984,-4.243149,5.511196,-0.830178,2.464626,2.160513,-5.256654,-9.261843,6.010952,4.573095,-7.864509,-8.324474,8.112281,1.205096,-9.183083,1.586993,-6.420035,1.321041,-5.800968,-6.773578,-2.595176,-9.329997,5.725613,-7.070070,-1.285263,-2.142899,3.687563,-2.007385,-3.432545,-5.242068,4.164436,-9.946252,3.967070,5.878961,8.818976,-9.244696,-0.429249,-7.695704,4.749539,-8.231119,1.514428,-8.950544,6.765397,9.937268,-6.599212,-8.583832,2.636378,9.164805,-3.171665,3.514488,-5.952688,5.577883,-5.342948,6.369444,-3.359786,-1.815295,-3.878893,4.507503,5.865644,-0.712357,-6.463393,-0.448384,2.762079,-9.762384,-3.098064,7.662534,8.709116,6.131022,-8.948701,0.950772,6.603776,-4.752640,-6.547071,2.045838,-4.922113,1.738092,9.220469,2.247637,-5.321809,-1.234927,1.134192,0.937808,1.308375,-4.107993,3.936315,-5.728790,3.063695,2.847096,-1.972616,-3.129378,-9.425756,3.500176,8.456882,-4.275076,9.800752,-0.624603,-1.017346,2.124972,1.374285,4.507916,-5.773505,3.276630,8.286995,4.987865,4.101158,-2.067094,-3.250153,0.390174,-5.678513,6.560339,1.932042,-0.326132,7.242862,4.105361,-9.630347,-4.102908,-3.277322,-4.913169,-0.177314,-6.541793,3.894038,0.985858,-1.711401,9.781404,-9.164347,-7.672087,4.157341,6.084865,0.430105,0.109028,7.477594,-9.970220,8.004791,0.058249,-0.297007,4.980013,6.596706,3.993288,-1.405912,-9.375669,5.302436,-6.481657,-3.448555,-6.043641,-0.303576,7.122311,9.429670,9.559597,-9.592174,-6.277926,-1.960470,3.581070,-8.084629,-1.471914,8.990406,4.860601,6.926589,0.348869,9.993411,6.839743,4.443796,9.594119,-9.672412,6.420474,-3.050320,-9.943223,-4.209449,-8.173825,-0.146770,3.554235,4.660220,2.816187,-0.731038,-4.758360,-5.376073,7.445932,-8.928955,-2.629314,5.406515,-6.464228,8.072882,1.279843,-3.965928,-5.352726,-2.022218,-2.761062,-3.451451,-4.020914,0.915335,-9.291555,4.599191,1.891427,-5.533588,-5.955248,-9.174027,2.534380,6.447712,8.535342,-3.212473,2.898186,9.750486,1.618763,0.149619,-7.569329,-4.178966,-6.772200,-9.000685,-7.100741,5.498138,-4.541599,4.700807,1.953153,-9.198589,-5.532663,-4.911591,7.771051,8.071044,0.919963,6.752706,9.996029,-5.145931,7.885040,-7.617575,0.358391,-0.382278,4.800715,-6.213431,0.984655,0.993703,8.342839,2.279208,8.673133,7.414390,6.093361,-6.137959,4.088679,-0.755777,2.200329,-9.584959,-0.933524,-0.726714,-8.556909,-9.305973,-5.727875,4.471855,6.039207,-6.736079,8.332433,2.594655,-5.387843,-5.529128,-0.641257,-7.567922,8.501331,-0.672329,-8.312496,6.496924,4.159388,-8.206589,6.414449,-8.641054,-2.117666,6.919357,-4.620944,-3.408765,-0.873316,-5.485396,3.552293,-3.025927,0.213530,-4.109256,1.463099,-1.778689,9.020179,-8.288763,-2.727792,6.787270,-8.848440,1.771836,1.090451,4.913165,-6.104525,-1.129673,3.255942,-1.230437,6.051122,-9.911315,-4.237956,-4.807910,3.173615,-5.813898,8.169825,-0.063350,-6.557999,-1.666558,6.409797,6.024720,-3.568505,5.635624,-8.883148,-5.254437,-7.442905,-7.104726,-2.503407,-3.826297,-3.434076,4.141946,-9.075822,5.620873,2.174826,-8.643742,2.661520,-9.970873,2.093716,9.350179,6.931250,2.596465,-7.459513,-7.641828,-8.370014,-7.848194,4.173142,-4.145171,4.289477,-6.878837,-9.214398,0.872957,-1.021845,6.771102,4.229038,7.547327,-4.701620,-0.409095,5.189711,9.385460,3.783187,-9.345734,-3.724650,-1.039115,-0.267665,-4.969376,8.456483,-4.002001,-8.961414,5.150450,2.048571,-9.808249,-2.600611,-6.837814,-7.535700,8.884954,-9.713350,-0.155523,8.247635,-2.641088,-9.567174,-1.784126,4.242463,7.228238,-6.946581,0.715391,-3.287989,9.812865,6.850909,-9.159007,-5.467808,7.948046,1.079576,7.106798,7.800936,-8.076602,-3.882204,8.657835,9.791854,2.631230,-1.440390,5.061396,7.373756,8.594312,5.158375,-4.233811,0.165312,-3.832901,1.923064,8.861937,1.333526,-6.269915,-4.618544,2.457543,7.825097,3.695158,-5.873611,-1.880024,-0.211868,-1.671537,4.681857,5.132940,-0.319617,9.322240,4.706905,-4.486993,-5.052898,-4.318357,6.174012,-5.548877,0.458303,-1.238226,6.604721,2.785397,-8.658675,8.391746,-1.018591,-6.485793,-5.512845,-4.619904,2.133497,-9.271672,-8.870349,-5.239683,4.384269,-7.431006,3.607691,-9.313392,9.783587,-2.661803,7.438711,2.642216,-5.006388,-6.487393,2.949485,-6.715401,-7.543224,-1.662832,6.398239,-6.573496,3.455218,5.955090,9.496689,1.399791,3.819507,-1.464214,9.063411,-0.067863,2.926880,-1.022676,-4.625633,1.460918,-6.168750,8.906265,1.664338,-8.089755,-5.206204,7.465782,4.145620,-7.025283,-9.338099,3.799151,-6.881766,9.041358,-5.308213,-2.635285,-5.219894,7.030780,2.954924,-2.458702,-7.097543,2.294025,3.156585,-2.992788,-2.570151,2.224471,8.768738,-9.211793,2.049818,-4.854249,-9.133412,-2.298359,-7.015616,1.113931,-3.001970,-7.177902,-3.105974,7.130240,-9.048252,-0.861086,-1.045700,3.394199,-0.528210,5.030465,9.131333,7.331559,-7.876489,-4.377672,-9.591368,-5.200097,-1.335239,5.119984,-6.092536,-9.725642,5.566788,4.288314,-4.532890,9.638135,8.166428,-7.754401,-7.848040,-4.992527,0.641103,-7.145141,-2.905084,-8.004566,0.163574,1.848551,-4.132815,3.926662,-3.662044,3.009928,8.895910,8.493584,3.511290,-4.848568,7.249342,-3.556551,9.459592,-6.799859,2.356209,-2.354230,1.180764,5.572763,5.700806,0.426428,5.638659,4.160585,2.858375,4.703050,-6.187922,2.293786,-0.521512,0.140121,-4.363705,2.432156,-7.777379,-6.478142,3.033029,-2.234485,-9.904939,-9.716386,-0.243350,0.854022,-2.748396,1.638599,-8.833562,5.234422,-5.660115,-8.259584,-3.434896,8.571206,-3.298077,-3.143751,2.500081,-9.693583,-9.622767,2.923179,-7.230272,2.505102,-8.900859,-2.380166,2.806961,8.824725,-8.939394,-9.391624,-9.808710,5.158619,0.831549,-5.383909,-8.337388,9.894330,-8.522239,-4.327516,2.793234,1.759083,-6.324591,-7.335347,3.940344,9.362860,6.819664,4.712298,6.802892,-9.460132,-6.797001,9.645708,-7.457302,-8.264547,-9.293635,8.265014,-2.920737,5.157642,-3.443808,-8.185843,7.832395,8.133017,5.594563,-2.515851,-0.520632,5.935456,-7.501250,5.607327,9.306172,3.922233,-8.089215,2.600952,5.756461,8.385871,-8.025558,-7.867725,-6.121152,4.317718,-9.540570,-6.267933,-7.293411,3.956913,0.342381,8.946471,-5.830687,-1.455915,-1.588107,1.195458,-1.696659,8.387562,-0.908002,-2.967610,-0.647428,-5.078574,-1.972013,3.135253,4.479534,9.917028,5.735443,1.183575,1.475720,4.938199,-2.771995,2.599986,3.115770,6.827119,-1.534733,-1.112775,9.246659,3.619957,-5.167063,2.348592,-1.219148,-7.104139,5.210228,0.132840,2.138824,-5.264317,-4.240218,-3.673854,2.975764,8.031849,6.048775,-1.019050,5.834331,-9.875723,-3.216133,9.195131,-0.381201,-9.027863,8.848034,-1.547286,-9.628624,-8.521467,9.122785,6.762099,3.687844,-4.254270,-3.464378,3.701320,4.958723,0.550206,1.713843,-1.493437,-0.894747,-3.831463,-4.583941,-5.981689,6.467228,0.974017,9.052222,4.796983,-0.263075,-6.168231,-4.701352,-6.182572,9.674385,2.424768,-2.423932,6.062188,7.006257,-8.141483,-4.513275,-3.361350,-6.542352,-8.406348,-1.998442,-4.677290,-8.792466,-8.839100,-0.687102,-9.272668,-3.636956,1.038282,0.013579,-0.759439,-0.791628,-6.670291,0.498633,-7.727489,6.242477,-8.558715,3.289786,-4.995265,5.887885,-8.546319,1.274475,3.863808,2.116151,-2.796490,7.134906,4.171684,5.837734,1.673841,-1.312389,-9.227011,-0.968267,-3.454899,3.694900,1.605872,7.075991,6.688645,-1.009135,-2.182681,0.223838,-0.760347,1.197313,-0.355536,-2.359977,-9.754139,7.524951,-0.909684,8.516708,4.020398,6.583173,6.507664,4.791894,0.286232,4.541870,6.816011,-8.840990,-6.144454,8.220961,-2.638155,-4.248537,-3.276743,-5.969458,9.423956,6.168645,-9.155712,-9.669374,5.233364,-2.213328,0.804707,9.779214,-1.041234,0.107381,6.198024,3.330791,-4.100254,-0.174983,-0.883785,0.586911,-5.158930,-1.696268,9.181506,-1.321229,-8.451575,0.364808,7.122913,-1.621347,-3.124285,-7.124071,-0.864403,9.408021,1.059217,-9.280777,-6.416473,4.427506,-0.737749,-6.552927,-8.285310,9.983772,1.286645,0.647757,2.890798,4.929444,9.885398,7.073809,0.098317,-9.091429,3.569212,-7.102342,-1.581615,-2.330091,-4.365666,-4.241638,-7.851489,5.152818,-1.038752,-2.820462,3.050584,8.813301,8.240371,-1.679954,1.027960,4.549394,4.924484,0.089981,7.497377,9.916431,-7.147920,1.608088,2.934787,-3.037320,6.156928,5.645167,-2.241987,3.104000,8.251795,4.818228,-4.097403,3.866054,-4.082461,5.299825,6.995826,4.566827,-0.800589,-8.685372,-7.622698,4.755203,2.370902,-6.434116,6.708243,1.145318,6.908172,7.219147,7.298145,-2.453399,3.347076,0.489185,-7.703577,-9.638029,3.888967,-2.881698,-2.281904,1.583219,-2.649480,7.370434,1.837221,-8.507513,3.616008,-4.306140,2.025368,6.285094,-0.734560,5.333519,3.730787,2.835140,-5.720236,-0.329960,3.201412,-0.557186,5.514876,4.067948,-9.971615,-5.904854,-4.492674], dtype = "float32")#candidate|7890|(1694,)|const|float32
call_7889 = relay.TupleGetItem(func_5435_call(relay.reshape(const_7890.astype('float32'), [11, 11, 14]), relay.reshape(const_7890.astype('float32'), [11, 11, 14]), ), 0)
call_7891 = relay.TupleGetItem(func_5439_call(relay.reshape(const_7890.astype('float32'), [11, 11, 14]), relay.reshape(const_7890.astype('float32'), [11, 11, 14]), ), 0)
func_5255_call = mod.get_global_var('func_5255')
func_5257_call = mutated_mod.get_global_var('func_5257')
call_7902 = relay.TupleGetItem(func_5255_call(), 0)
call_7903 = relay.TupleGetItem(func_5257_call(), 0)
output = relay.Tuple([call_7861,uop_7872,call_7889,const_7890,call_7902,])
output2 = relay.Tuple([call_7862,uop_7872,call_7891,const_7890,call_7903,])
func_7911 = relay.Function([var_7851,], output)
mod['func_7911'] = func_7911
mod = relay.transform.InferType()(mod)
var_7912 = relay.var("var_7912", dtype = "int64", shape = (7, 8, 4))#candidate|7912|(7, 8, 4)|var|int64
output = func_7911(var_7912)
func_7913 = relay.Function([var_7912], output)
mutated_mod['func_7913'] = func_7913
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7958 = relay.var("var_7958", dtype = "bool", shape = (13, 4, 1))#candidate|7958|(13, 4, 1)|var|bool
var_7959 = relay.var("var_7959", dtype = "bool", shape = (13, 4, 11))#candidate|7959|(13, 4, 11)|var|bool
bop_7960 = relay.logical_and(var_7958.astype('bool'), var_7959.astype('bool')) # shape=(13, 4, 11)
func_6699_call = mod.get_global_var('func_6699')
func_6701_call = mutated_mod.get_global_var('func_6701')
call_7973 = relay.TupleGetItem(func_6699_call(), 0)
call_7974 = relay.TupleGetItem(func_6701_call(), 0)
func_1571_call = mod.get_global_var('func_1571')
func_1575_call = mutated_mod.get_global_var('func_1575')
var_7977 = relay.var("var_7977", dtype = "uint16", shape = (1056,))#candidate|7977|(1056,)|var|uint16
call_7976 = func_1571_call(relay.reshape(var_7977.astype('uint16'), [16, 6, 11]), relay.reshape(var_7977.astype('uint16'), [16, 6, 11]), )
call_7978 = func_1571_call(relay.reshape(var_7977.astype('uint16'), [16, 6, 11]), relay.reshape(var_7977.astype('uint16'), [16, 6, 11]), )
func_5841_call = mod.get_global_var('func_5841')
func_5843_call = mutated_mod.get_global_var('func_5843')
call_7982 = func_5841_call()
call_7983 = func_5841_call()
output = relay.Tuple([bop_7960,call_7973,call_7976,var_7977,call_7982,])
output2 = relay.Tuple([bop_7960,call_7974,call_7978,var_7977,call_7983,])
func_7993 = relay.Function([var_7958,var_7959,var_7977,], output)
mod['func_7993'] = func_7993
mod = relay.transform.InferType()(mod)
mutated_mod['func_7993'] = func_7993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7993_call = mutated_mod.get_global_var('func_7993')
var_7995 = relay.var("var_7995", dtype = "bool", shape = (13, 4, 1))#candidate|7995|(13, 4, 1)|var|bool
var_7996 = relay.var("var_7996", dtype = "bool", shape = (13, 4, 11))#candidate|7996|(13, 4, 11)|var|bool
var_7997 = relay.var("var_7997", dtype = "uint16", shape = (1056,))#candidate|7997|(1056,)|var|uint16
call_7994 = func_7993_call(var_7995,var_7996,var_7997,)
output = call_7994
func_7998 = relay.Function([var_7995,var_7996,var_7997,], output)
mutated_mod['func_7998'] = func_7998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6757_call = mod.get_global_var('func_6757')
func_6759_call = mutated_mod.get_global_var('func_6759')
call_8000 = relay.TupleGetItem(func_6757_call(), 2)
call_8001 = relay.TupleGetItem(func_6759_call(), 2)
output = call_8000
output2 = call_8001
func_8008 = relay.Function([], output)
mod['func_8008'] = func_8008
mod = relay.transform.InferType()(mod)
mutated_mod['func_8008'] = func_8008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8008_call = mutated_mod.get_global_var('func_8008')
call_8009 = func_8008_call()
output = call_8009
func_8010 = relay.Function([], output)
mutated_mod['func_8010'] = func_8010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3593_call = mod.get_global_var('func_3593')
func_3595_call = mutated_mod.get_global_var('func_3595')
call_8052 = relay.TupleGetItem(func_3593_call(), 0)
call_8053 = relay.TupleGetItem(func_3595_call(), 0)
output = relay.Tuple([call_8052,])
output2 = relay.Tuple([call_8053,])
func_8066 = relay.Function([], output)
mod['func_8066'] = func_8066
mod = relay.transform.InferType()(mod)
mutated_mod['func_8066'] = func_8066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8066_call = mutated_mod.get_global_var('func_8066')
call_8067 = func_8066_call()
output = call_8067
func_8068 = relay.Function([], output)
mutated_mod['func_8068'] = func_8068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_8071 = relay.TupleGetItem(func_1112_call(), 0)
call_8072 = relay.TupleGetItem(func_1113_call(), 0)
output = relay.Tuple([call_8071,])
output2 = relay.Tuple([call_8072,])
func_8073 = relay.Function([], output)
mod['func_8073'] = func_8073
mod = relay.transform.InferType()(mod)
mutated_mod['func_8073'] = func_8073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8073_call = mutated_mod.get_global_var('func_8073')
call_8074 = func_8073_call()
output = call_8074
func_8075 = relay.Function([], output)
mutated_mod['func_8075'] = func_8075
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8093 = relay.var("var_8093", dtype = "uint64", shape = (1, 8, 9))#candidate|8093|(1, 8, 9)|var|uint64
var_8094 = relay.var("var_8094", dtype = "uint64", shape = (3, 8, 9))#candidate|8094|(3, 8, 9)|var|uint64
bop_8095 = relay.maximum(var_8093.astype('uint64'), var_8094.astype('uint64')) # shape=(3, 8, 9)
output = bop_8095
output2 = bop_8095
func_8103 = relay.Function([var_8093,var_8094,], output)
mod['func_8103'] = func_8103
mod = relay.transform.InferType()(mod)
var_8104 = relay.var("var_8104", dtype = "uint64", shape = (1, 8, 9))#candidate|8104|(1, 8, 9)|var|uint64
var_8105 = relay.var("var_8105", dtype = "uint64", shape = (3, 8, 9))#candidate|8105|(3, 8, 9)|var|uint64
output = func_8103(var_8104,var_8105,)
func_8106 = relay.Function([var_8104,var_8105,], output)
mutated_mod['func_8106'] = func_8106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3487_call = mod.get_global_var('func_3487')
func_3488_call = mutated_mod.get_global_var('func_3488')
call_8131 = func_3487_call()
call_8132 = func_3487_call()
output = call_8131
output2 = call_8132
func_8133 = relay.Function([], output)
mod['func_8133'] = func_8133
mod = relay.transform.InferType()(mod)
mutated_mod['func_8133'] = func_8133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8133_call = mutated_mod.get_global_var('func_8133')
call_8134 = func_8133_call()
output = call_8134
func_8135 = relay.Function([], output)
mutated_mod['func_8135'] = func_8135
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8139 = relay.const([[[False,False,False,False,True,True,True,False,False,True,False,False,False,True,False,True],[True,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True],[False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True],[False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False],[True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True],[False,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False],[False,False,False,True,False,True,True,True,True,True,False,False,True,True,False,True],[True,False,False,False,False,False,False,False,True,True,False,True,False,True,True,False],[True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True],[False,True,True,False,True,False,True,False,True,True,False,True,False,True,False,False],[True,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True],[True,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False],[True,False,True,False,False,False,True,True,True,True,False,False,True,True,True,True],[False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True],[False,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True]],[[False,True,False,False,True,False,True,False,True,True,False,True,False,False,False,False],[True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True],[True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False],[False,True,True,True,False,False,True,False,True,False,False,False,False,False,True,True],[True,False,False,True,False,False,True,False,True,True,False,True,False,True,True,True],[False,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True],[False,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True],[True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False],[True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False],[False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True],[True,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True],[True,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False],[True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False],[True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,True],[False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,True]],[[False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,False],[True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False],[False,True,True,True,False,False,False,True,False,False,False,False,False,True,False,True],[True,False,True,False,True,True,False,False,False,True,False,False,True,True,False,True],[False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False],[True,False,False,False,True,True,False,True,False,False,True,True,True,True,True,True],[True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,True],[True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,False],[False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False],[False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False],[False,False,True,False,False,False,False,True,True,True,False,False,True,False,False,False],[True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,True],[True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,False],[False,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False],[True,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False]],[[False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False],[True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False],[False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,True],[False,True,True,True,False,True,True,True,False,True,True,False,False,False,False,False],[True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False],[True,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True],[False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False],[True,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False],[False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False],[False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,False],[True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True],[False,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True],[True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True],[False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True],[False,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True]],[[False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False],[False,True,False,True,True,True,False,True,True,False,False,False,True,True,True,True],[False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False],[True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False],[False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False],[False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True],[False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True],[True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False],[False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,False],[False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True],[False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True],[False,False,True,True,False,True,True,False,True,False,False,True,True,True,False,True],[True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False],[False,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False],[True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True]],[[False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False],[False,True,False,False,False,True,True,True,False,False,True,False,False,True,True,False],[False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False],[True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True],[False,True,False,True,False,True,True,False,True,False,True,True,False,False,True,True],[False,True,False,True,True,True,True,True,True,False,True,False,True,True,False,False],[True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True],[True,False,True,False,False,False,True,True,False,False,False,False,True,False,False,False],[False,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True],[False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False],[True,False,False,False,True,False,True,True,True,False,False,True,False,True,False,False],[False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True],[False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True],[False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False],[True,False,False,True,False,True,True,True,True,True,False,False,False,True,False,True]]], dtype = "bool")#candidate|8139|(6, 15, 16)|const|bool
const_8140 = relay.const([[[True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False],[True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False],[False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,True],[False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True],[True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True],[False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False],[False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,False],[True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,False],[True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False],[False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False],[False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,False],[False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False],[False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False],[False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True],[True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False]],[[True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False],[False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True],[True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False],[True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False],[False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False],[True,False,True,True,True,False,True,False,False,False,False,True,False,False,True,False],[True,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True],[True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False],[True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False],[False,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False],[True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False],[True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False],[False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True],[False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False],[False,False,True,False,False,True,True,False,True,False,False,True,True,False,False,True]],[[True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,True],[True,False,True,False,True,False,False,False,False,False,True,True,False,True,False,True],[False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True],[True,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False],[False,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False],[False,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False],[True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False],[False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False],[True,True,True,True,True,False,True,False,False,True,True,False,False,False,False,True],[True,True,False,True,False,True,True,False,False,False,False,False,False,False,False,True],[True,True,False,True,False,True,True,False,False,False,False,True,False,False,False,False],[True,False,True,True,True,False,True,True,True,True,True,True,False,False,True,True],[True,True,False,True,True,False,True,True,False,True,False,True,True,False,True,True],[False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True],[False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False]],[[False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,True],[False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,True],[False,True,True,True,True,False,True,True,True,True,True,True,False,False,False,True],[True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,False],[False,True,True,True,False,True,False,True,False,True,False,True,True,True,False,False],[False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False],[True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False],[True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False],[False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True],[True,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False],[True,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False],[False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False],[False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False],[False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True],[True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False]],[[True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False],[True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False],[False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True],[False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,True],[False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False],[False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False],[False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False],[True,False,True,True,False,False,True,False,False,True,True,True,True,True,True,True],[True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False],[True,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False],[False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True],[True,True,True,False,False,True,False,True,True,False,False,True,False,True,True,False],[True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True],[False,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True],[False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True]],[[True,True,False,True,False,False,True,False,False,False,True,False,True,False,True,True],[False,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True],[True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,True],[True,True,True,False,True,True,True,True,False,False,False,False,False,True,False,False],[True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False],[False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False],[True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True],[True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True],[False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True],[False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,True],[False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False],[False,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True],[True,True,False,False,True,True,True,False,True,True,False,True,True,False,True,False],[True,False,True,True,False,False,False,False,False,False,True,True,False,True,False,True],[False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False]]], dtype = "bool")#candidate|8140|(6, 15, 16)|const|bool
bop_8141 = relay.logical_or(const_8139.astype('bool'), relay.reshape(const_8140.astype('bool'), relay.shape_of(const_8139))) # shape=(6, 15, 16)
output = relay.Tuple([bop_8141,])
output2 = relay.Tuple([bop_8141,])
func_8149 = relay.Function([], output)
mod['func_8149'] = func_8149
mod = relay.transform.InferType()(mod)
output = func_8149()
func_8150 = relay.Function([], output)
mutated_mod['func_8150'] = func_8150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3199_call = mod.get_global_var('func_3199')
func_3201_call = mutated_mod.get_global_var('func_3201')
call_8271 = func_3199_call()
call_8272 = func_3199_call()
output = relay.Tuple([call_8271,])
output2 = relay.Tuple([call_8272,])
func_8278 = relay.Function([], output)
mod['func_8278'] = func_8278
mod = relay.transform.InferType()(mod)
output = func_8278()
func_8279 = relay.Function([], output)
mutated_mod['func_8279'] = func_8279
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8345 = relay.var("var_8345", dtype = "float64", shape = (10, 2, 10))#candidate|8345|(10, 2, 10)|var|float64
uop_8346 = relay.sqrt(var_8345.astype('float64')) # shape=(10, 2, 10)
output = relay.Tuple([uop_8346,])
output2 = relay.Tuple([uop_8346,])
func_8355 = relay.Function([var_8345,], output)
mod['func_8355'] = func_8355
mod = relay.transform.InferType()(mod)
mutated_mod['func_8355'] = func_8355
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8356 = relay.var("var_8356", dtype = "float64", shape = (10, 2, 10))#candidate|8356|(10, 2, 10)|var|float64
func_8355_call = mutated_mod.get_global_var('func_8355')
call_8357 = func_8355_call(var_8356)
output = call_8357
func_8358 = relay.Function([var_8356], output)
mutated_mod['func_8358'] = func_8358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7360_call = mod.get_global_var('func_7360')
func_7362_call = mutated_mod.get_global_var('func_7362')
call_8509 = relay.TupleGetItem(func_7360_call(), 0)
call_8510 = relay.TupleGetItem(func_7362_call(), 0)
func_1950_call = mod.get_global_var('func_1950')
func_1952_call = mutated_mod.get_global_var('func_1952')
var_8522 = relay.var("var_8522", dtype = "float32", shape = (2048,))#candidate|8522|(2048,)|var|float32
call_8521 = relay.TupleGetItem(func_1950_call(relay.reshape(var_8522.astype('float32'), [8, 16, 16])), 0)
call_8523 = relay.TupleGetItem(func_1952_call(relay.reshape(var_8522.astype('float32'), [8, 16, 16])), 0)
output = relay.Tuple([call_8509,call_8521,var_8522,])
output2 = relay.Tuple([call_8510,call_8523,var_8522,])
func_8534 = relay.Function([var_8522,], output)
mod['func_8534'] = func_8534
mod = relay.transform.InferType()(mod)
var_8535 = relay.var("var_8535", dtype = "float32", shape = (2048,))#candidate|8535|(2048,)|var|float32
output = func_8534(var_8535)
func_8536 = relay.Function([var_8535], output)
mutated_mod['func_8536'] = func_8536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2986_call = mod.get_global_var('func_2986')
func_2987_call = mutated_mod.get_global_var('func_2987')
call_8544 = relay.TupleGetItem(func_2986_call(), 0)
call_8545 = relay.TupleGetItem(func_2987_call(), 0)
func_4576_call = mod.get_global_var('func_4576')
func_4577_call = mutated_mod.get_global_var('func_4577')
call_8547 = relay.TupleGetItem(func_4576_call(), 3)
call_8548 = relay.TupleGetItem(func_4577_call(), 3)
output = relay.Tuple([call_8544,call_8547,])
output2 = relay.Tuple([call_8545,call_8548,])
func_8552 = relay.Function([], output)
mod['func_8552'] = func_8552
mod = relay.transform.InferType()(mod)
output = func_8552()
func_8553 = relay.Function([], output)
mutated_mod['func_8553'] = func_8553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5349_call = mod.get_global_var('func_5349')
func_5350_call = mutated_mod.get_global_var('func_5350')
call_8564 = relay.TupleGetItem(func_5349_call(), 0)
call_8565 = relay.TupleGetItem(func_5350_call(), 0)
output = call_8564
output2 = call_8565
func_8566 = relay.Function([], output)
mod['func_8566'] = func_8566
mod = relay.transform.InferType()(mod)
output = func_8566()
func_8567 = relay.Function([], output)
mutated_mod['func_8567'] = func_8567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4819_call = mod.get_global_var('func_4819')
func_4820_call = mutated_mod.get_global_var('func_4820')
call_8581 = func_4819_call()
call_8582 = func_4819_call()
output = relay.Tuple([call_8581,])
output2 = relay.Tuple([call_8582,])
func_8601 = relay.Function([], output)
mod['func_8601'] = func_8601
mod = relay.transform.InferType()(mod)
mutated_mod['func_8601'] = func_8601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8601_call = mutated_mod.get_global_var('func_8601')
call_8602 = func_8601_call()
output = call_8602
func_8603 = relay.Function([], output)
mutated_mod['func_8603'] = func_8603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7340_call = mod.get_global_var('func_7340')
func_7342_call = mutated_mod.get_global_var('func_7342')
call_8604 = relay.TupleGetItem(func_7340_call(), 4)
call_8605 = relay.TupleGetItem(func_7342_call(), 4)
func_139_call = mod.get_global_var('func_139')
func_141_call = mutated_mod.get_global_var('func_141')
call_8613 = relay.TupleGetItem(func_139_call(), 0)
call_8614 = relay.TupleGetItem(func_141_call(), 0)
func_6686_call = mod.get_global_var('func_6686')
func_6688_call = mutated_mod.get_global_var('func_6688')
const_8616 = relay.const([[1.931768,-6.684652,-7.355421,-4.429954,0.574945,-0.079806,4.612575,-7.272431,-2.644649,-1.801562,7.814391,-6.348287,5.510670,5.043517,4.190291,5.835003,-2.875770,-8.162000,-1.117155,6.325316,-6.345220,6.207236,4.972660,3.788615,6.422280,1.344905,8.277053,-2.971464,7.046934,-8.026706,2.897309,-3.982031,8.584258,4.298918,9.140561,-6.100638,-9.018226,3.078290,9.042498,5.657147,0.627090,-1.205552,-0.371882,3.612247,-8.199536,-4.783507,8.839932,-3.769884,1.510064,-5.907811,-2.107784,1.820945,7.158001,-2.464130,8.385127,2.925138,5.920125,2.301846,1.455806,9.698145,9.733443,2.611474,-9.232543,3.227972,2.226621,0.847722,-0.664312,-9.473451,4.140448,6.799575,-7.097429,2.263952,-1.278009,-1.676153,4.769714,5.723234,6.797360,-3.030610,-0.832032,-0.671588,3.237765,-5.609362,-7.957633,3.122818,5.062308,-0.807279,-4.392966,7.818215,2.882433,-2.098207,-1.561935,7.990388,-7.322619,4.907026,6.008840,6.150622,8.389563,0.703575,-0.260316,-5.424641],[3.692458,-4.948603,-5.279299,-2.173665,9.027992,1.540243,-4.098531,3.948860,-6.846671,-4.591854,-8.206315,-9.170703,2.632588,8.044650,3.328738,7.515307,4.851442,-7.333181,-4.431525,3.120720,5.656773,6.198139,2.620082,-0.183248,2.054133,8.043857,-7.623266,-1.154995,4.259741,-1.574314,8.689021,4.894225,6.379543,-5.004801,-0.542633,2.512841,-3.899845,-0.799746,8.484132,1.443843,0.785568,6.673413,0.143520,2.147763,2.003944,2.224912,4.039474,6.625642,-1.736835,-4.832156,6.388415,-8.081819,-1.278086,5.915410,9.205282,4.090719,-5.933889,3.050624,-5.416264,-5.123672,-1.604144,-3.769941,0.124933,-2.424687,4.208848,-2.482627,-0.567219,3.498549,2.859796,-4.138876,5.999563,4.075388,-5.866472,2.911095,5.211582,4.633482,0.128617,-8.626833,6.195403,-0.490545,9.390633,-9.416597,4.296665,3.991850,-7.487361,-4.746390,5.222614,2.973764,-9.759576,-0.931271,4.594396,4.969506,4.595557,8.168507,-5.472480,0.990754,-2.115749,5.090518,5.239122,7.180468],[-4.938515,-9.172151,0.510827,-2.961054,-0.558810,-4.570793,-2.083489,0.223178,6.131315,-5.687805,-1.234707,9.859944,4.861289,1.015562,9.994175,8.557348,-6.893182,7.957275,0.504821,1.387602,-4.413273,9.687848,6.435406,-3.260784,5.469558,-2.007147,7.225363,5.836953,-1.397196,1.269826,5.243312,6.702607,-0.992650,7.635071,-4.786160,-9.869923,-0.560468,4.354024,-1.812416,-8.703113,4.456073,9.334946,2.100301,7.028689,3.893657,4.859365,1.923549,-4.568738,-4.758287,-1.510194,-0.151498,0.471800,-4.662816,-6.721431,4.948810,7.115076,5.087927,7.413016,7.221524,-3.983508,6.051829,6.133026,8.175315,9.126907,2.623646,-4.810799,-1.624907,5.438440,9.871459,7.875584,-5.889417,6.824265,4.874364,-8.918018,1.584236,-5.903397,6.749960,-7.994743,1.749597,-4.900187,4.143204,7.522003,-9.024106,-6.377673,-7.498595,-1.545172,-8.922953,4.576612,-8.831178,-8.401634,-5.064241,1.210562,-6.152743,-9.522812,9.448123,7.725766,-6.745587,-2.417178,9.082508,-8.461905],[-6.779694,-3.390526,-4.188395,-3.058225,-1.873953,-5.122783,1.197529,-4.508470,9.960383,-1.780881,7.932821,7.477891,-7.773728,-1.241218,2.094767,7.663617,-4.336797,-3.987088,9.477053,1.345282,-7.661243,9.237424,5.474849,3.734216,-6.347948,8.712755,7.597029,6.690417,-1.294808,6.261206,-4.953194,7.018927,9.824439,8.964119,3.973091,-2.759376,2.158113,0.684488,1.662153,9.007078,-5.068281,6.351097,-3.259639,2.082966,-1.893521,-2.950041,-2.877664,8.419183,1.940335,-4.744483,-5.482978,-6.076541,-8.841032,-0.885635,4.507991,-5.860614,7.732440,5.841311,-7.068774,-5.580946,-3.424314,-9.860214,6.368294,-5.482861,-9.550479,9.066509,1.820644,-4.498124,0.490064,9.489296,2.738518,0.115331,5.036490,-2.486766,4.719431,-1.071787,6.125964,-7.634299,1.881766,2.898715,-7.992942,-4.718927,8.433964,1.770639,0.966383,2.358384,-8.967234,0.434188,9.030599,-0.804557,8.601824,-4.495798,0.730741,6.129493,7.181527,-7.115537,8.504423,4.343106,-1.254182,6.414761],[1.910213,-2.271008,4.159358,0.822384,2.394928,-1.659027,7.784898,0.207022,0.351886,3.842532,6.906422,-6.338205,-4.522631,8.132776,7.901265,-7.143278,2.554603,-8.143181,5.992821,-0.612846,0.529741,2.065257,4.845404,7.993475,2.009271,-7.170210,3.776789,0.889456,-8.813744,-5.455374,5.431252,5.692822,8.462254,-7.104989,4.912123,1.842248,1.960000,9.011558,2.773293,7.523281,4.350640,5.126659,7.123277,-0.280361,-4.256802,3.471151,-5.827817,-9.635730,-2.196126,-0.790591,3.100816,0.250860,-2.794759,-6.394816,1.435743,-3.279022,5.373275,7.056794,-1.902877,-2.442015,-6.963577,-2.188368,-2.957139,-7.585029,4.806874,1.607141,-0.564732,2.309450,8.237443,-7.818768,-9.770668,-2.860711,6.217578,-4.456773,9.972870,-2.837041,-1.076220,-2.336613,0.089513,8.884197,3.078143,-9.995423,0.453884,-0.110962,8.846862,-1.526551,4.905822,6.923845,-5.064914,-1.390119,-0.406442,-7.621141,-2.465538,-7.077970,7.294238,-7.847332,-2.212673,2.792960,0.519461,-6.075825],[-6.022240,-9.091097,1.314820,-9.846097,2.398001,-4.443391,9.869275,-3.588571,4.565773,-9.426554,-7.035274,-8.933636,7.549216,8.893452,5.014222,8.811843,-5.030930,-9.020972,3.236710,9.776874,3.358686,-3.916889,-8.794665,-3.533234,3.534065,3.116844,-6.114960,-6.568618,8.317215,-5.497234,-8.917648,-3.684817,5.580040,-6.734552,-7.224939,9.428623,8.321185,-9.703402,-9.037577,-0.949373,8.359446,1.629304,8.101174,2.184666,2.534514,5.278475,6.342961,-4.005410,-7.331466,9.087617,8.382073,1.895552,6.964059,-3.264419,-8.323994,1.501463,-7.350257,4.118525,6.599667,-4.960760,-9.237458,-9.072270,-9.954627,-3.018188,9.813395,4.143458,-9.542126,-0.668516,-5.992038,7.681880,1.140966,1.121143,-6.255170,0.092739,1.125322,-9.553899,6.460997,-7.637298,-5.620760,2.569267,-4.922526,-6.590608,1.318872,-0.342794,7.718832,-3.365041,0.148330,4.384698,9.078846,6.050583,-4.283306,-8.748978,-3.543451,2.882761,-5.217511,-9.795939,0.531833,9.253954,5.599500,0.189355],[-8.063108,7.804260,1.013481,3.933058,9.268627,1.442093,-1.109025,-9.935032,-4.335893,1.014402,-1.500224,-6.017855,-1.154974,-8.219834,7.002365,5.376007,4.517107,3.832659,6.275961,4.481625,8.486963,-9.584472,4.952439,-2.953844,7.820202,-2.319248,-6.886132,6.234829,-6.785828,-6.688227,0.863328,2.767375,8.987909,8.994583,8.805828,9.991520,-8.707652,6.204148,-6.185201,6.273805,0.688604,0.286242,-0.865660,0.873155,-1.278526,2.435738,9.589951,5.433936,6.471939,5.052489,7.184300,-5.647086,-4.903037,0.505895,5.824911,-9.350785,-9.102238,-2.227551,6.546477,-7.936937,-5.644807,0.475455,-6.217860,-4.236938,-3.834330,6.693275,-2.900641,4.451201,2.578653,-2.104675,7.034714,4.048941,-3.668822,4.768442,3.972784,-3.630130,9.960289,3.447328,-6.168842,1.754379,7.602173,-8.094158,-5.261270,7.322017,3.686882,5.058319,-4.941603,-6.448987,-7.034598,-5.391336,4.765369,0.661123,4.571068,0.046328,-4.427569,-3.422453,7.492470,-4.082097,-1.007617,7.608448],[8.894976,-6.412604,9.341070,-7.665142,-2.109805,-8.589563,9.565519,-6.513760,-5.887129,-5.765470,1.965577,9.449231,-8.671060,-6.419662,0.657308,-3.324130,-9.922880,-0.533739,6.184631,-0.493320,-2.499080,-0.293567,-6.246988,-1.587495,-0.987428,-8.358723,0.168108,-6.196145,3.014136,-8.624567,-1.377776,6.109150,2.878794,-8.353049,-8.604029,7.818075,2.104556,6.787851,-6.452285,0.275246,-9.086326,-5.440522,5.249766,4.341955,-3.351365,9.405557,-2.171918,1.587624,-2.229786,2.482952,-8.398650,8.265827,-8.949447,-3.513564,-8.823824,0.293812,2.216059,-4.970113,-5.175472,0.388675,9.687839,3.431522,0.006912,-1.200308,-3.468929,-3.794866,-6.414069,8.189107,-3.019939,0.930653,1.435641,-3.442644,5.222641,9.046438,-8.492707,-7.020432,9.780453,-4.519340,-9.005049,-1.607387,-3.019276,-9.541302,9.223992,9.603374,7.506761,-1.357098,7.830115,8.134532,-7.359591,-5.010331,4.042412,-1.845678,-5.278430,0.504345,6.960465,4.171476,-9.225662,-8.940347,0.292500,-1.875314],[6.006317,9.017118,5.337198,7.183725,0.708035,-6.004338,-7.232782,8.291275,8.818730,3.939053,9.691645,-9.422937,-6.643762,8.652190,-8.323610,-8.102507,-5.555158,-5.819679,-4.454194,5.085395,1.997623,-6.356258,1.777721,-0.295630,-6.633858,2.778586,4.882821,-9.756851,3.828095,5.583502,0.111734,8.271718,-1.146879,3.754338,4.989675,-1.489850,-8.088481,-6.529716,2.570896,9.247037,-1.872758,3.291237,-3.281598,-4.530286,8.890161,-8.351366,5.500102,-3.347795,9.191842,6.799542,2.725244,-0.143400,-8.160079,1.513752,3.992763,-5.440577,2.735320,5.552145,2.142976,5.789025,-9.858718,7.489359,1.908865,0.481945,6.404655,9.063248,-8.940104,-2.341678,-9.708792,-0.468190,-7.092059,-7.610999,-9.347910,-6.663145,4.831343,-8.521165,1.625887,9.756668,-9.809386,6.965392,8.392628,-4.200319,-0.201712,8.435096,-5.193748,3.927361,-9.187219,-7.172870,3.765223,-9.979185,4.927984,-7.493396,-2.737724,8.947543,-6.053972,-9.153381,-2.381484,-1.970161,4.755878,1.350365],[0.265448,2.673840,-3.772929,3.529064,-9.144119,-7.202060,-2.995828,-3.292389,7.587852,5.647949,-9.293916,0.991589,-9.239317,-8.760285,6.138521,8.666180,-0.131279,-7.993351,7.395425,-3.815064,8.375414,1.936940,-4.658908,-0.161687,5.952655,6.072600,2.281528,-0.089699,-4.092863,-8.698435,6.610040,8.175155,-8.753787,-0.561530,6.483097,3.873606,-4.049818,-9.892014,-5.175152,-8.831661,8.400453,5.828644,-2.724673,-4.919261,-1.179024,4.493842,0.543058,3.210919,-8.887952,5.906840,4.397212,5.432036,0.683754,-1.231584,-0.614330,7.280134,-2.544950,4.658235,3.496794,-1.986930,-1.039783,5.800071,-9.557391,0.066989,-5.604891,-3.427317,8.623380,2.472844,9.959107,-6.357507,-7.178265,2.815252,-8.113233,-4.534825,7.337298,-2.381557,-2.011555,1.828854,-5.079763,7.064803,6.876749,-6.231674,2.573585,6.008013,1.654043,2.529924,1.383009,1.299269,8.696082,8.061846,-3.051343,-2.496253,0.375391,1.089625,-5.877144,2.796126,-7.754797,-9.045623,4.012202,-1.479611],[6.365544,5.698969,5.162647,-3.214260,-7.957906,7.314845,3.469071,0.458253,7.809205,6.447385,4.203444,5.815445,-4.480754,-5.636976,6.811052,7.174138,-6.949179,6.196836,8.108551,-1.683939,-1.100920,-6.042464,2.380892,-7.279052,-0.439049,-0.756799,-6.842702,5.510761,2.050537,1.510966,-2.720261,9.336293,8.998162,-8.747050,-2.181752,-3.467372,-6.137115,9.865609,-4.507748,-2.412329,6.041162,-9.399275,-3.373836,-0.208012,9.844964,-8.057978,-8.962845,-1.751738,6.752528,-7.794949,7.779713,-8.478033,8.658432,3.228699,5.206556,-8.895121,-5.929062,9.600626,-1.252373,-7.830430,0.560562,-4.863401,-6.197377,9.682038,3.648718,-9.765154,-6.671804,8.200382,-5.206246,1.858387,-0.286150,-7.741818,-7.907349,-1.895662,3.454771,6.050740,6.262629,8.777089,-9.251423,8.766381,-6.788934,2.155444,-3.067575,0.084224,1.106036,1.515314,-6.547814,1.330795,0.926418,-0.246862,-3.049072,2.959799,3.035773,-5.734525,3.114932,5.557359,4.648365,-7.801136,6.046362,-6.216492],[-2.475103,3.644896,6.154763,6.950337,-5.822508,0.024158,8.104673,-1.503873,7.066817,2.770554,3.188789,7.953962,7.250788,-2.157521,7.737940,6.237158,-7.140899,-9.786251,9.269178,-6.906076,5.922347,4.630124,-7.381253,9.048720,-4.021070,-6.370838,-8.266467,-1.877024,5.193233,-3.071710,9.433883,-0.492880,-8.172666,5.054710,4.502386,9.493428,3.853157,5.327038,2.210066,-1.333911,7.472334,9.254104,-1.845852,5.561196,-8.763283,-8.838145,-8.812399,-0.058087,6.695198,-7.611017,4.312292,-9.518831,-2.791372,5.706437,-6.048236,4.976725,-3.198472,1.737632,-6.715783,5.969863,0.088195,-9.893382,-7.477035,-1.544084,-4.121704,-8.809331,1.199337,2.863963,8.639232,8.163932,-6.735848,7.755897,3.902831,4.289224,-7.730199,-9.936930,-3.060768,7.455279,7.464807,-2.581609,-1.439636,-0.519906,1.590174,-5.092465,-8.633789,9.190687,-6.236595,4.963749,4.153059,-0.725114,0.620981,2.860652,4.251826,2.595906,1.391185,1.241703,-5.024026,3.318274,8.355718,-2.282837],[2.142781,-6.367944,1.944303,4.030350,-2.925385,-4.868311,-1.775535,4.289199,-3.671140,2.610218,-2.095827,4.825622,-9.673120,6.633060,-4.417294,5.871974,2.422205,-9.109824,4.753163,9.182151,0.345310,-9.596742,-5.485421,9.970427,-7.516583,-4.101126,0.611048,0.865608,-4.928929,3.876565,7.468618,-7.648577,-0.064532,0.616919,-9.757535,0.128272,-8.581820,8.461866,8.791518,9.384712,6.081291,6.331063,5.955274,-4.896430,1.222372,5.052337,-4.967699,0.093450,-0.033444,9.444555,9.139931,-1.332787,-7.745449,-9.193282,-6.697035,7.284347,8.609264,1.431065,9.951223,-0.644998,8.603209,2.002770,5.205191,0.362889,7.381671,-1.195462,3.867957,-2.669065,0.787254,-1.151205,-0.870846,7.479943,-7.327514,8.785091,9.202655,-9.926553,7.598539,-9.360273,-3.268936,-1.399853,-0.219474,-1.413434,9.297791,2.921538,-3.734763,-5.257421,7.072034,-1.743636,-5.105072,-2.713519,-8.025504,8.293710,-0.268604,-3.216366,5.417914,6.892245,-1.776917,3.210148,-5.026165,-8.601180],[-7.378231,-5.225156,-9.785578,8.783260,-8.214804,-7.800007,-0.059633,-1.629183,-9.581917,5.990784,1.312961,7.888658,3.506928,3.325817,-3.028527,-1.987130,-8.577367,-4.005837,6.849592,-4.890947,5.442133,-5.639312,-0.225692,4.893949,-1.226650,-1.133373,3.036035,0.160339,-2.684987,-5.675147,-3.710103,-1.672998,5.473522,9.167220,-7.622141,-0.134166,3.689034,-7.766627,0.140365,-4.260090,-5.646756,8.887862,-4.831349,-8.646427,9.216330,1.099449,5.523574,9.769513,5.001900,-1.286638,-7.593089,9.344155,7.919979,2.984390,1.637940,-7.835783,-3.737963,6.508804,-0.969563,1.407783,4.636487,8.029425,-0.453562,2.513385,-7.076737,-8.645753,2.014865,-4.784545,1.191848,4.091768,9.642625,-9.129733,-6.769427,-5.629772,-9.479458,-9.101905,9.501244,-2.922107,-7.502567,7.416557,8.769060,3.390847,4.432943,-5.904691,1.862834,-9.467216,1.258502,-6.303941,-4.988613,4.648308,3.229426,-9.783394,9.978999,-4.418676,9.948920,-1.416099,5.083411,0.589249,4.288391,5.898888],[8.514319,2.509051,8.883396,-7.164593,5.957952,-9.467550,-6.277421,4.762166,3.651895,8.711189,1.808123,-6.373679,-9.519928,6.722573,0.906425,-9.591952,-3.906624,8.783144,-0.348794,-1.048204,3.487056,-8.795548,6.289086,-2.622806,4.641630,5.101878,9.520362,-7.082340,3.497689,-1.064724,-8.450030,-3.206941,-1.302529,-8.227267,8.219518,-1.988488,9.876894,-8.293480,-6.534109,-6.336997,0.779976,-4.560104,1.042628,-9.943227,1.338089,3.137817,1.700448,-4.961894,3.357814,-8.271426,9.317901,-4.780442,6.348069,-4.625016,0.618986,-4.668377,-3.181465,7.998614,6.333138,0.937536,-8.719996,-1.311676,-2.301336,-1.224901,-1.553319,-1.622247,0.219970,-4.963826,-2.536550,0.129011,4.530836,-8.702470,-4.340785,8.760142,1.732397,-2.952505,2.140624,0.502009,-0.102349,-8.360828,7.514844,-3.929291,1.778925,4.732734,9.615766,6.338001,-8.841479,7.326452,0.894928,-7.735829,1.382781,7.464134,-6.085550,-9.064988,-7.631918,8.019930,8.174591,-4.524680,-0.903249,-7.672616],[-9.519884,7.919596,3.507181,-5.939717,6.529709,7.190319,2.298808,-0.370094,-5.403311,-0.899624,3.452692,-6.704526,-3.809189,9.415096,-5.053239,-2.879766,8.265893,-0.944370,-5.127409,6.046759,8.195909,-0.015971,7.682448,-5.895229,1.668210,-6.825885,-2.358640,-4.424237,-0.594251,-9.909827,3.035657,4.325048,-4.361436,-1.611059,-4.688614,-4.275056,-1.613257,8.394580,7.961368,7.768457,-9.176370,6.068990,-3.129093,3.670246,2.929204,-9.837140,1.185639,8.499644,5.446454,-2.896806,-4.121650,4.064293,-6.361195,-7.060753,6.237468,-2.176569,-1.504327,-7.704818,1.078523,2.119939,2.174596,-7.534291,7.721836,-0.821727,4.427748,9.649181,-0.561649,-7.059369,0.599341,-1.203763,7.059934,-9.718760,5.289817,-2.008736,8.093969,5.836820,7.770391,7.333230,-3.748477,2.528641,-8.350590,2.993225,-4.337903,8.543679,-8.114968,-6.302899,2.203691,2.651088,7.185932,8.106888,5.067188,-2.351462,-0.651399,-0.961426,3.154252,-8.547867,-4.995593,-4.542393,-2.596308,-2.520730],[-1.613366,-9.975087,4.508145,-5.461358,4.989299,8.881958,-0.090850,-2.077810,7.799224,5.574530,-8.670844,4.453799,0.394487,3.122724,5.612430,9.797911,-8.109886,4.861783,1.251928,6.232736,-4.412655,-9.266721,-1.879376,6.082863,5.094063,-5.733305,2.411411,-5.384123,-9.352365,-2.164961,3.313395,5.366864,0.871299,7.966089,-8.294331,0.139998,-5.485772,5.657720,-6.298189,-7.230222,-1.702393,-8.864316,-7.821166,-5.867822,-0.854233,0.940196,-3.478402,-9.336196,8.970587,1.212116,-5.626314,-4.508994,-3.891818,6.640185,0.839118,-0.956717,-3.019003,0.818938,4.858143,9.774931,-2.311014,5.813718,1.381185,-5.455308,9.318560,-3.506517,-5.225856,-7.501019,5.223629,-7.337948,-7.752989,-0.327641,7.261046,8.726780,8.643290,-6.714032,8.321124,0.813492,4.103004,-9.736624,3.569530,-6.054137,6.829832,-5.436489,-8.116978,4.547695,6.963530,-3.106456,2.608822,6.884154,-2.930044,-7.024071,1.120108,5.479218,4.766722,2.724507,-4.444668,3.226876,5.697851,-5.297682],[-4.992225,-3.905421,3.463608,-2.630144,-3.621480,-4.739808,3.956299,8.970068,-2.877039,-3.984090,-2.251202,-2.211358,8.242743,-7.015883,9.287098,8.095217,9.735198,0.374475,-1.785445,5.833417,5.131533,8.141193,2.335065,4.733971,1.861673,5.851479,5.903820,4.482856,5.470988,6.925348,-3.049064,-6.198914,-6.603824,4.449066,2.783747,-1.259678,-2.776670,-7.992074,-5.092608,8.542797,7.650248,6.975153,-7.208843,6.881542,-3.484874,-0.970195,9.468258,-9.407556,-8.711813,-5.986738,3.056779,-9.420803,3.852717,8.086844,-3.553295,7.120806,3.111562,-7.387159,7.704053,-2.061239,9.356834,6.176574,0.414022,-0.330380,1.122248,-1.776268,9.841972,-2.644607,9.775212,-5.400050,-9.481107,1.130048,-9.754899,8.372093,3.153661,-6.940297,-7.145665,-5.440591,3.613495,9.876911,4.371134,0.346331,-0.193545,0.641770,8.327740,5.176207,-7.984375,-7.587479,-0.130973,-3.612829,3.098897,-1.258680,-5.399162,1.804004,-8.321270,-0.029989,-0.954174,-8.429748,3.120296,-4.519096]], dtype = "float64")#candidate|8616|(18, 100)|const|float64
call_8615 = relay.TupleGetItem(func_6686_call(relay.reshape(const_8616.astype('float64'), [15, 10, 12])), 0)
call_8617 = relay.TupleGetItem(func_6688_call(relay.reshape(const_8616.astype('float64'), [15, 10, 12])), 0)
func_2949_call = mod.get_global_var('func_2949')
func_2951_call = mutated_mod.get_global_var('func_2951')
call_8619 = func_2949_call()
call_8620 = func_2949_call()
func_2410_call = mod.get_global_var('func_2410')
func_2413_call = mutated_mod.get_global_var('func_2413')
const_8629 = relay.const(5.122266, dtype = "float64")#candidate|8629|()|const|float64
call_8628 = relay.TupleGetItem(func_2410_call(relay.reshape(const_8629.astype('float64'), [])), 1)
call_8630 = relay.TupleGetItem(func_2413_call(relay.reshape(const_8629.astype('float64'), [])), 1)
uop_8637 = relay.log10(call_8619.astype('float32')) # shape=(2, 14, 10)
uop_8639 = relay.log10(call_8620.astype('float32')) # shape=(2, 14, 10)
output = relay.Tuple([call_8604,call_8613,call_8615,const_8616,call_8628,const_8629,uop_8637,])
output2 = relay.Tuple([call_8605,call_8614,call_8617,const_8616,call_8630,const_8629,uop_8639,])
func_8654 = relay.Function([], output)
mod['func_8654'] = func_8654
mod = relay.transform.InferType()(mod)
mutated_mod['func_8654'] = func_8654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8654_call = mutated_mod.get_global_var('func_8654')
call_8655 = func_8654_call()
output = call_8655
func_8656 = relay.Function([], output)
mutated_mod['func_8656'] = func_8656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8678 = relay.var("var_8678", dtype = "int8", shape = (1, 11, 10))#candidate|8678|(1, 11, 10)|var|int8
var_8679 = relay.var("var_8679", dtype = "int8", shape = (4, 11, 10))#candidate|8679|(4, 11, 10)|var|int8
bop_8680 = relay.minimum(var_8678.astype('int8'), var_8679.astype('int8')) # shape=(4, 11, 10)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
const_8695 = relay.const([3.149193,-0.697711,-0.122679,8.482817,2.722120,4.357158,-2.632838,0.659009,-4.937200,3.692025,-2.168121,0.982481,-6.789971,-5.414156,-2.045674,-0.363055,-3.120173,9.710140,0.908745,-4.255039,-4.303076,5.651260,2.400720,-4.125477,-0.846100,-9.835891,3.820726,-3.620522,-3.089209,3.893812,-7.763743,6.009885,-7.654176,5.041752,7.621934,7.982205,6.482350,-8.566619,8.342841,-4.462973,4.058979,-4.413533,-4.000139,-2.756640,0.101731,6.905712,-3.046940,-3.685449,1.704934,-6.616810,-4.395484,-6.876423,-5.053023,-0.730623,4.004106,-2.979910,0.981969,6.040898,9.071534,0.374539,0.577246,-1.236929,5.204579,1.285138,-0.616151,6.395601,8.774249,9.749887,-7.544007,1.970428,-8.788511,-0.411386,-4.445716,-4.696680,-3.902496,7.387099,-9.714050,8.710642,-1.736341,5.039810,-5.217111,7.835950,-5.072209,8.498699,-1.223180,4.058993,-8.694766,1.135618,4.685236,8.797235,0.518058,-7.583791,-5.608790,6.199956,-9.695660,-8.469462,9.458037,-4.149762,-3.542846,-9.277935,-2.122686,3.217712,-1.571121,0.766753,-2.366648,6.167368,8.254512,-0.098445,1.024996,6.738779,-2.505580,-0.214095,7.660683,7.779947,-7.286959,2.627690,3.026873,-5.556543,1.717012,-0.901428,-9.240880,6.295648,6.664735,8.153467,0.276011,-8.559759,-0.858849,6.972692,5.712846,0.588793,-0.983265,-2.383998,-2.662134,2.028167,-3.901573,4.181616,2.218413,9.293324,-4.516624,4.443931,2.457446,8.411691,-0.483541,7.249246,-6.832313,-6.941854,4.575350,-1.533637,0.453392,1.149498,3.929762,-6.145462,2.933814,4.036820,-1.202832,4.754894,-9.722373,-5.984905,1.144375,-2.797694,-5.992186,2.520090,7.946164,8.795395,6.662177,4.164342,-8.861531,-2.677301,2.514862,9.408133,-3.343022,6.317012,-8.282862,-2.645882,3.759038,4.626747,8.193417,-0.080076,-3.012191,4.401042,-4.793734,9.882719,-4.306766,0.964487,3.357696,0.421520,8.800019,8.019395,-3.705476,-9.162267,-9.894701,-5.780787,-2.401980,7.136731,-2.462941,-6.432822,9.217058,1.168774,2.063917,7.527315,-5.849516,8.322028,8.512866,7.882721,-6.203213,9.810664,0.767087,-1.013143,-9.151483,-4.836826,-6.412263,-3.877673,-3.158506,6.143451,-0.629724,7.129936,7.456645,-1.398649,1.753339,1.282991,5.969157,-1.241587,-8.642043,-0.198014,-8.468003,9.158932,-9.037206,-9.057463,-7.858323,-1.789701,-4.473886,6.381449,-5.463058,-9.411345,9.973559,6.823761,1.382467,5.644763,-0.028980,-7.817406,-4.968403,3.399261,4.887046,-8.525384,6.774255,-8.798374,-8.930575,-2.178233,-4.372908,-0.596483,-5.705770,-1.270439,9.683911,9.111070,-2.407552,8.497565,8.913771,6.550194,-4.455721,-3.522496,-1.586761,-1.359826,-0.361071,-6.600487,6.925276,-0.531984,-3.239605,0.248723,-8.977721,-2.010070,2.399418,-3.794694,-6.934897,3.271637,7.529627,9.647282,2.699280,-5.922230,-9.865547,-9.374816,8.213036,9.074172,8.717318,8.281312,8.743894,-4.987252,7.411329,7.104378,-7.365967,4.315694,7.081257,-1.061988,-8.299333,-4.675377,9.971437,-4.714465,-1.488232,-1.080144,4.751789,2.207282,5.240378,5.831161,-9.181975,0.274705,5.371745,-7.157769,5.436174,0.626738,4.539714,-5.926372,-3.015573,0.251064,-4.660396,2.811957,-6.804940,-7.298817,-8.125793,-9.630386,-3.109910,-3.061658,-4.613509,-9.418749,3.113306,3.140572,-6.942107,5.261823,5.049964,2.029725,-1.464606,9.583830,3.266677,6.151701,5.182039,0.168529,2.754824,3.088166,-9.798373,6.976170,-3.873889,5.675503,-4.645092,7.253165,0.293534,8.407251,3.664349,-0.311973,-5.525184,0.384720,-9.376244,5.562679,-5.415382,9.838281,9.787695,-1.203041,-6.029827,-3.630487,-3.284943,-8.686936,-6.403190,2.657772,-6.869042,-1.159356,5.777526,-2.030688,-5.536524,9.596881,-8.718601,-7.067975,8.105177,4.164121,-4.687443,-0.504132,-4.592045,-8.619478,-6.723989,-9.103441,-9.570883,0.179091,-7.123373,1.214576,-9.073762,7.348105,6.180374,-1.484511,-4.586417,-8.878935,4.960253,8.949670,5.103907,-8.217109,-4.459323,-2.662092,3.189810,-5.050095,8.538109,2.387456,4.287816,0.040304,-3.916619,0.317509,0.483476,7.625303,8.470309,-7.953461,-3.516069,-7.555041,-0.595684,5.160628,9.307938,1.998146,1.193423,-9.333928,-5.811216,-6.764127,4.733719,7.581631,8.775873,0.012908,-4.361747,-4.464610,-9.041517,0.218995,4.222703,-5.893045,-9.342232,-9.707601,-0.930172,-6.558742,-8.922342,5.384451,7.867117,-5.486088,5.763007,1.674665,-5.070228,7.470699,-6.715118,2.683852,1.842319,-5.640133,6.174365,-1.907716,2.484923,-3.186099,6.251817,1.891878,9.549381,9.686633,5.534808,-5.510231,-8.084184,-1.601169,-8.019136,7.371757,-9.200463,6.158510,-0.892980,2.860547,6.979934,3.296613,-3.070160,4.134351,-0.308871,-3.875281,3.705176,5.491098,-3.371946,-0.764858,7.810930,1.716009,-7.867775,-6.174866,-9.614022,-4.723700,6.954203,-3.949136,8.443988,9.063633,-0.054452,5.109427,-3.586159,-2.151706,2.179684,2.752606,-4.317522,-6.457993,-5.117659,2.550870,-8.384879,-4.343201,4.851957,2.416942,-0.796504,-8.482604,9.253089,-5.289755,7.581424,-7.621445,7.000251,0.841486,-2.157901,-8.003472,-1.784641,5.878080,-6.001692,3.197809,-0.389677,-4.038725,7.993091,-6.112527,-6.294459,6.014689,6.969056,-3.819659,3.635243,-8.279208,1.284418,-1.687985,-7.767634,0.308179,6.663295,-9.734834,8.363124,-3.534179,4.446560,7.271144,5.191665,0.965703,7.200977,-4.957782,-6.704645,-1.924783,3.227416,5.620145,0.320990,-7.687164,7.676712,-1.504517,6.000898,-9.073514,3.411768,7.466030,-8.716840,7.503457,-6.770470,-9.929768,-6.709203,2.489900,-9.490164,7.305369,4.545654,-0.650984,-7.967452,7.843486,-1.228144,4.345291,-5.838375,-2.902242,5.925406,-4.607920,6.807402,-5.147600,4.678461,-3.710093,5.580751,3.835098,2.024376,7.940436,1.114253,-3.614243,-0.086244,1.825441,-6.225253,9.478732,-5.173297,2.003206,6.311629,4.018506,3.781213,-8.986907,-3.447029,9.710480,5.188978,0.108573,-6.771377,-1.275917,7.497319,2.808181,-8.076087,-5.153388,-5.603509,-3.744956,6.958030,-1.071389,1.918580,9.865244,9.834863,-7.833604,-8.224947,5.414809,9.808708,3.814800,6.810561,-3.116074,-8.764376,-7.790596,-6.991700,-4.383242,9.462414,2.630737,5.851754,-9.813923,6.459129,1.736096,-4.180113,-1.479240,0.431329,3.939974,-3.283519,-8.720975,-8.474177,0.589927,6.103880,-1.250128,4.183365,-7.837457,5.995062,9.626638,2.116393,-3.778436,6.464559,8.935210,-5.474318,3.638318,-3.444104,4.576261,6.137164,8.990038,-1.340721,8.085143,2.006702,-5.188919,-6.081544,-1.366759,8.787727,2.332534,3.136377,1.820619,1.040728,3.543782,-0.443993,-6.330617,9.081044,-1.256307,-9.941184,2.574879,6.971349,-4.403344,4.450714,1.421818,2.029407,3.080631,2.618304,-7.373779,-3.395901,-9.221712,8.580405,-8.846182,9.846387,-6.986505,-8.258806,8.172204,-1.049710,8.063928,-3.777357,-4.663204,4.744130,2.639517,-8.695910,-3.524295,8.765857,9.043661,6.296450,3.664798,-8.299401,-0.660929,-5.010530,1.512200,3.279536,-8.750997,6.922653,4.648020,0.332356,-4.432884,8.516047,-1.532506,0.795628,2.627484,0.043884,8.322900,-8.461849,-3.061604,-5.402828,0.821537,-7.250050,1.018656,-4.010555,-8.225519,3.362377,1.943249,6.470273,3.760500,6.556773,-7.279411,-8.090253,5.231302,9.414593,1.249285,2.834839,-6.108889,-7.370181,5.851729,-1.212033,-8.178232,-4.972635,-4.565010,6.151898,5.823996,-5.110551,4.397353,9.486581,-6.044446,-0.908791,-0.919526,-7.606573,0.084830,3.167977,-6.596408,7.100241,5.497499,-1.647868,9.290674,-9.496099,8.495717,-2.911417,7.405501,4.286397,4.556186,8.304831,3.624419,-4.547947,-4.887147,6.597236,7.731744,-8.608843,6.254633,8.024030,-1.660036,1.674112,-0.359801,6.452473,6.628270,4.793278,-1.225189,0.111711,2.834353,1.483148,2.276428,-7.364641,2.394263,2.863924,8.555320,1.278317,-0.564201,8.401131,9.754929,-7.289540,7.927014,0.215315,-7.614310,9.647842,-0.150901,-2.184052,-7.130391,-4.637387,1.450047,-1.122633,-4.529879,-9.584854,-0.809666,-6.213515,-6.841865,-8.080404,-7.723181,-2.034985,-4.373672,-3.327475,-7.824510,-6.394393,6.321056,-5.379111,0.837359,-3.351410,-8.804347,-2.964496,-8.411013,-8.850036,-6.041172,3.931361,-4.068408,8.475121,3.613812,4.737284,-2.392123,-2.593199,1.639634,-3.119116,7.201328,-7.318019,-3.519595,-8.228126,4.309905,8.101020,-9.539868,1.596505,-6.917985,4.559038,-2.694305,6.552561,5.508387,4.596677,-0.497933,3.474749,-3.853012,-5.815756,-5.820732,9.368909,5.692666,0.232305,9.300614,3.156722,-1.406614,-5.958796,3.218820,7.464875,2.946427,0.742698,5.362790,-0.914186,2.622337,-0.821505,3.393186,8.261667,-2.394506,-0.342122,9.389786,-7.390557,1.537756,4.513326,-9.505059,1.136181,2.021113,-4.069212,9.056772,-7.670101,2.362302,-3.321161,-0.409070,9.285552,9.649899,8.018425,7.267876,-7.622721,-6.509585,-2.318331,-5.484482,-5.189072,-4.562566,-5.746486,5.868696,-9.759598,0.726284,-2.823083,9.222989,3.879668,5.597057,9.506213,-7.246424,3.774730,8.324618,4.672458,4.147212,0.879775,-4.923509,0.645154,-9.168696,-5.243092,4.590398,-4.497651,0.518600,6.587500,-7.420273,6.383372,-6.263284,0.938932,-6.486140,9.797979,-2.985032,-1.274036,6.055054,5.763470,1.091022,1.419223,-7.885125,2.960908,6.145800,-1.159672,-1.851431,-3.324240,6.702981,-3.656829,9.258452,7.586711,7.647724,-2.250268,-5.050603,-6.059926,-0.564031,-9.238935,6.448695,-3.745743,-2.844914,-9.666270,-4.377092,6.553979,-5.213577,-0.854472,0.404203,-6.471141,1.349664,8.484624,-9.536091,1.187766,-3.523750,6.948859,-5.927904,-0.998297,-6.532643,5.038046,-0.825068,-9.052978,-1.317244,-3.994991,2.924268,-7.424639,4.991060,-5.574287,-6.583808,-2.747064,4.628194,-0.865191,1.932749,-3.407314,-2.021170,7.149762,-2.911955,6.508009,-7.614442,-3.064093,-6.728667,-8.266055,8.325712,0.417637,-5.078922,-1.170771,1.837875,6.442606,9.451478,4.811170,6.187814], dtype = "float64")#candidate|8695|(980,)|const|float64
var_8696 = relay.var("var_8696", dtype = "float64", shape = (40, 2))#candidate|8696|(40, 2)|var|float64
call_8694 = relay.TupleGetItem(func_1319_call(relay.reshape(const_8695.astype('float64'), [14, 10, 7]), relay.reshape(var_8696.astype('float64'), [80, 1]), ), 0)
call_8697 = relay.TupleGetItem(func_1322_call(relay.reshape(const_8695.astype('float64'), [14, 10, 7]), relay.reshape(var_8696.astype('float64'), [80, 1]), ), 0)
bop_8704 = relay.add(var_8679.astype('uint16'), relay.reshape(bop_8680.astype('uint16'), relay.shape_of(var_8679))) # shape=(4, 11, 10)
bop_8713 = relay.multiply(bop_8704.astype('int32'), relay.reshape(bop_8680.astype('int32'), relay.shape_of(bop_8704))) # shape=(4, 11, 10)
output = relay.Tuple([call_8694,const_8695,var_8696,bop_8713,])
output2 = relay.Tuple([call_8697,const_8695,var_8696,bop_8713,])
func_8717 = relay.Function([var_8678,var_8679,var_8696,], output)
mod['func_8717'] = func_8717
mod = relay.transform.InferType()(mod)
mutated_mod['func_8717'] = func_8717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8717_call = mutated_mod.get_global_var('func_8717')
var_8719 = relay.var("var_8719", dtype = "int8", shape = (1, 11, 10))#candidate|8719|(1, 11, 10)|var|int8
var_8720 = relay.var("var_8720", dtype = "int8", shape = (4, 11, 10))#candidate|8720|(4, 11, 10)|var|int8
var_8721 = relay.var("var_8721", dtype = "float64", shape = (40, 2))#candidate|8721|(40, 2)|var|float64
call_8718 = func_8717_call(var_8719,var_8720,var_8721,)
output = call_8718
func_8722 = relay.Function([var_8719,var_8720,var_8721,], output)
mutated_mod['func_8722'] = func_8722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_8724 = relay.TupleGetItem(func_2009_call(), 0)
call_8725 = relay.TupleGetItem(func_2011_call(), 0)
func_4586_call = mod.get_global_var('func_4586')
func_4587_call = mutated_mod.get_global_var('func_4587')
call_8734 = func_4586_call()
call_8735 = func_4586_call()
output = relay.Tuple([call_8724,call_8734,])
output2 = relay.Tuple([call_8725,call_8735,])
func_8741 = relay.Function([], output)
mod['func_8741'] = func_8741
mod = relay.transform.InferType()(mod)
mutated_mod['func_8741'] = func_8741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8741_call = mutated_mod.get_global_var('func_8741')
call_8742 = func_8741_call()
output = call_8742
func_8743 = relay.Function([], output)
mutated_mod['func_8743'] = func_8743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1200_call = mod.get_global_var('func_1200')
func_1201_call = mutated_mod.get_global_var('func_1201')
call_8762 = relay.TupleGetItem(func_1200_call(), 0)
call_8763 = relay.TupleGetItem(func_1201_call(), 0)
output = call_8762
output2 = call_8763
func_8779 = relay.Function([], output)
mod['func_8779'] = func_8779
mod = relay.transform.InferType()(mod)
output = func_8779()
func_8780 = relay.Function([], output)
mutated_mod['func_8780'] = func_8780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4659_call = mod.get_global_var('func_4659')
func_4660_call = mutated_mod.get_global_var('func_4660')
call_8814 = relay.TupleGetItem(func_4659_call(), 0)
call_8815 = relay.TupleGetItem(func_4660_call(), 0)
output = relay.Tuple([call_8814,])
output2 = relay.Tuple([call_8815,])
func_8816 = relay.Function([], output)
mod['func_8816'] = func_8816
mod = relay.transform.InferType()(mod)
mutated_mod['func_8816'] = func_8816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8816_call = mutated_mod.get_global_var('func_8816')
call_8817 = func_8816_call()
output = call_8817
func_8818 = relay.Function([], output)
mutated_mod['func_8818'] = func_8818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_8870 = func_947_call()
call_8871 = func_947_call()
output = relay.Tuple([call_8870,])
output2 = relay.Tuple([call_8871,])
func_8883 = relay.Function([], output)
mod['func_8883'] = func_8883
mod = relay.transform.InferType()(mod)
mutated_mod['func_8883'] = func_8883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8883_call = mutated_mod.get_global_var('func_8883')
call_8884 = func_8883_call()
output = call_8884
func_8885 = relay.Function([], output)
mutated_mod['func_8885'] = func_8885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7360_call = mod.get_global_var('func_7360')
func_7362_call = mutated_mod.get_global_var('func_7362')
call_8911 = relay.TupleGetItem(func_7360_call(), 0)
call_8912 = relay.TupleGetItem(func_7362_call(), 0)
output = call_8911
output2 = call_8912
func_8927 = relay.Function([], output)
mod['func_8927'] = func_8927
mod = relay.transform.InferType()(mod)
output = func_8927()
func_8928 = relay.Function([], output)
mutated_mod['func_8928'] = func_8928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8654_call = mod.get_global_var('func_8654')
func_8656_call = mutated_mod.get_global_var('func_8656')
call_8952 = relay.TupleGetItem(func_8654_call(), 5)
call_8953 = relay.TupleGetItem(func_8656_call(), 5)
func_2653_call = mod.get_global_var('func_2653')
func_2655_call = mutated_mod.get_global_var('func_2655')
call_8954 = relay.TupleGetItem(func_2653_call(), 2)
call_8955 = relay.TupleGetItem(func_2655_call(), 2)
func_5954_call = mod.get_global_var('func_5954')
func_5956_call = mutated_mod.get_global_var('func_5956')
call_8956 = relay.TupleGetItem(func_5954_call(), 0)
call_8957 = relay.TupleGetItem(func_5956_call(), 0)
output = relay.Tuple([call_8952,call_8954,call_8956,])
output2 = relay.Tuple([call_8953,call_8955,call_8957,])
func_8962 = relay.Function([], output)
mod['func_8962'] = func_8962
mod = relay.transform.InferType()(mod)
output = func_8962()
func_8963 = relay.Function([], output)
mutated_mod['func_8963'] = func_8963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7150_call = mod.get_global_var('func_7150')
func_7152_call = mutated_mod.get_global_var('func_7152')
call_8982 = relay.TupleGetItem(func_7150_call(), 0)
call_8983 = relay.TupleGetItem(func_7152_call(), 0)
func_4236_call = mod.get_global_var('func_4236')
func_4237_call = mutated_mod.get_global_var('func_4237')
call_8988 = relay.TupleGetItem(func_4236_call(), 1)
call_8989 = relay.TupleGetItem(func_4237_call(), 1)
output = relay.Tuple([call_8982,call_8988,])
output2 = relay.Tuple([call_8983,call_8989,])
func_8991 = relay.Function([], output)
mod['func_8991'] = func_8991
mod = relay.transform.InferType()(mod)
mutated_mod['func_8991'] = func_8991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8991_call = mutated_mod.get_global_var('func_8991')
call_8992 = func_8991_call()
output = call_8992
func_8993 = relay.Function([], output)
mutated_mod['func_8993'] = func_8993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6313_call = mod.get_global_var('func_6313')
func_6314_call = mutated_mod.get_global_var('func_6314')
call_9032 = relay.TupleGetItem(func_6313_call(), 0)
call_9033 = relay.TupleGetItem(func_6314_call(), 0)
output = call_9032
output2 = call_9033
func_9036 = relay.Function([], output)
mod['func_9036'] = func_9036
mod = relay.transform.InferType()(mod)
output = func_9036()
func_9037 = relay.Function([], output)
mutated_mod['func_9037'] = func_9037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5460_call = mod.get_global_var('func_5460')
func_5462_call = mutated_mod.get_global_var('func_5462')
call_9211 = relay.TupleGetItem(func_5460_call(), 0)
call_9212 = relay.TupleGetItem(func_5462_call(), 0)
func_181_call = mod.get_global_var('func_181')
func_183_call = mutated_mod.get_global_var('func_183')
call_9216 = relay.TupleGetItem(func_181_call(relay.reshape(call_9211.astype('float32'), [14, 10, 7])), 0)
call_9217 = relay.TupleGetItem(func_183_call(relay.reshape(call_9211.astype('float32'), [14, 10, 7])), 0)
output = relay.Tuple([call_9211,call_9216,])
output2 = relay.Tuple([call_9212,call_9217,])
func_9221 = relay.Function([], output)
mod['func_9221'] = func_9221
mod = relay.transform.InferType()(mod)
output = func_9221()
func_9222 = relay.Function([], output)
mutated_mod['func_9222'] = func_9222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6207_call = mod.get_global_var('func_6207')
func_6208_call = mutated_mod.get_global_var('func_6208')
call_9228 = relay.TupleGetItem(func_6207_call(), 2)
call_9229 = relay.TupleGetItem(func_6208_call(), 2)
output = call_9228
output2 = call_9229
func_9249 = relay.Function([], output)
mod['func_9249'] = func_9249
mod = relay.transform.InferType()(mod)
mutated_mod['func_9249'] = func_9249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9249_call = mutated_mod.get_global_var('func_9249')
call_9250 = func_9249_call()
output = call_9250
func_9251 = relay.Function([], output)
mutated_mod['func_9251'] = func_9251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_9252 = relay.TupleGetItem(func_1112_call(), 0)
call_9253 = relay.TupleGetItem(func_1113_call(), 0)
output = relay.Tuple([call_9252,])
output2 = relay.Tuple([call_9253,])
func_9254 = relay.Function([], output)
mod['func_9254'] = func_9254
mod = relay.transform.InferType()(mod)
mutated_mod['func_9254'] = func_9254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9254_call = mutated_mod.get_global_var('func_9254')
call_9255 = func_9254_call()
output = call_9255
func_9256 = relay.Function([], output)
mutated_mod['func_9256'] = func_9256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3674_call = mod.get_global_var('func_3674')
func_3676_call = mutated_mod.get_global_var('func_3676')
call_9291 = relay.TupleGetItem(func_3674_call(), 0)
call_9292 = relay.TupleGetItem(func_3676_call(), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1113_call = mutated_mod.get_global_var('func_1113')
call_9295 = relay.TupleGetItem(func_1112_call(), 0)
call_9296 = relay.TupleGetItem(func_1113_call(), 0)
output = relay.Tuple([call_9291,call_9295,])
output2 = relay.Tuple([call_9292,call_9296,])
func_9300 = relay.Function([], output)
mod['func_9300'] = func_9300
mod = relay.transform.InferType()(mod)
mutated_mod['func_9300'] = func_9300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9300_call = mutated_mod.get_global_var('func_9300')
call_9301 = func_9300_call()
output = call_9301
func_9302 = relay.Function([], output)
mutated_mod['func_9302'] = func_9302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2653_call = mod.get_global_var('func_2653')
func_2655_call = mutated_mod.get_global_var('func_2655')
call_9327 = relay.TupleGetItem(func_2653_call(), 2)
call_9328 = relay.TupleGetItem(func_2655_call(), 2)
func_3987_call = mod.get_global_var('func_3987')
func_3992_call = mutated_mod.get_global_var('func_3992')
var_9330 = relay.var("var_9330", dtype = "float64", shape = (56,))#candidate|9330|(56,)|var|float64
const_9331 = relay.const([-6.641874,-9.119134,-2.735253,-1.685166,5.888572,3.595465,-7.552556,4.396713,-6.994622,9.045581,-1.968615,6.785827,-0.815285,-7.863794,0.299601,9.690454,-6.895422,9.144307,-7.885281,-1.773188,-2.797828,-9.793656,-4.786302,4.341641,5.281698,-7.506124,-0.848785,-1.836893,6.623532,-2.748066,-8.898116,5.048637,-7.604014,2.797559,-5.289410,-8.925327,8.270325,1.250115,-2.502782,-3.364749,-4.273516,2.882689,-9.923921,5.614895,8.473800,-7.338219,0.006413,-2.363660,6.100072,-8.710739,8.226825,-9.787338,2.931111,-9.282838,-3.753286,4.850032,6.256812,-0.078382,6.999615,3.679808,0.698747,-5.766692,1.092405,-2.252469,-3.787102,8.260667,2.013929,4.578417,3.932927,-6.675119,-4.055337,-1.578753,8.766171,-7.892515,8.096557,5.687436,0.520108,8.864844,-5.529918,9.931486,6.592383,-1.569745,7.838121,2.019163,7.004454,-0.739838,-8.913649,7.714229,7.719341,-4.735787,3.694152,-2.347021,4.116414,-8.551312,5.846232,-9.810655,-2.648350,-6.757106,-9.192068,-8.556224,3.257980,-9.118658,-2.378363,8.727290,6.248591,-7.698411,8.585485,5.574595,-6.670007,-2.656532,-9.815627,-5.828572,6.639343,-6.406801,3.576839,9.610474,9.355344,-6.982227,2.932341,-7.264820,9.637129,-1.008538,8.877798,3.269526,9.736172,0.676180,-1.692926,-3.344761,-5.435920,-9.208761,3.106917,8.840744,3.890903,-5.913087,4.246507,5.456010,1.459082,-2.593834,2.919682,6.380536,9.813243,-7.751666,-7.976087,-4.016061,5.125933,-2.471441,-9.981776,-3.058782,9.281887,4.763361,1.016611,8.788863,-9.941793,6.323280,2.259489,-0.830151,3.761728,3.521156,7.535500,2.208889,-5.101429,1.423104,7.638698,-5.214238,4.201476,1.711715,-2.224345,4.986395,-1.278776,-4.287212,0.752815,2.931398,-2.261642,2.537263,-5.234656,-8.938662,-5.546671,2.662121,9.338267,8.019223,5.806043,1.574194,0.070267,-6.008730,8.559602,-2.454318,5.485191,-9.724414,-9.682740,0.919624,-7.636020,5.905650,-7.620548,-1.193788,-3.581543,-2.191800,-5.499472,3.422656,-5.746429,-0.912831,-7.409419,4.552339,-3.805409,2.769554,8.551040,6.960114,8.921461,-4.563313,2.478094,1.611348,-9.826261,-4.405915,-0.993230,1.553688,0.913419,-3.347988,-6.379203,-8.907444,6.221334,2.254855,-0.569757,-5.922663,4.923662,9.233654,1.468155,-6.754031,-5.332025,2.070595,-6.241314,-8.366810,-5.445898,0.402195,-2.071291,0.532597,-7.362272,-1.887895,1.201074,-8.048572,4.771886,1.037481,-1.729485,6.593698,-6.143522,9.496117,3.691959,9.396450,8.750233,-2.513140,-4.265751,6.574241,-0.989139,8.801336,3.289708,-9.233790,-9.124796,4.174258,3.041960,2.724841,9.976668,-6.413472,-4.891519,-9.781317,-3.357948,3.074460,-2.188006,0.069893,-2.983366,-3.488438,-8.888379,0.982175,6.733387,-1.484466,3.155818,-8.570116,-5.771394,4.697215,-5.618894,-2.401358,-1.939351,9.231190,2.814250,5.387537,-9.134603,0.708931,-8.900044,0.096154,3.428344,-2.033734,1.659863,-9.832702,2.123612,4.274444,4.811578,-0.771180,7.075052,0.387544,6.259857,9.792822,-7.877215,-3.893198,9.601262,-5.232390,3.653576,2.353046,-8.824219,2.507661,1.116955,8.294729,-3.181957,-7.933704,-5.686350,-2.439022,-7.495124,7.339480,-4.631463,9.847054,0.787393,3.466400,-5.651197,9.968801,-2.950868,-2.074032,0.191189,-2.654144,0.437098,-4.627021,-9.970583,6.828250,-1.984103,-9.189647,0.005931,-7.649897,5.848816,6.606829,-9.667281,-5.284561,8.274358,-2.173020,8.606616,4.480204,8.983305,-0.797023,-2.653226,-3.503958,-6.892588,-8.971341,-0.441805,-8.858329,-3.711896,0.131469,-8.129792,1.801612,-2.982385,6.060546,-3.887703,-2.890349,-0.409350,-8.655105,7.745924,1.678446,8.457466,1.098196,-0.530833,6.640768,2.733032,4.824325,9.472046,-6.590000,-2.957038,1.127957,-6.512987,-6.153150,-4.186510,7.934503,4.215874,0.017708,-0.258608,-1.028167,-2.551133,7.922951,-7.316515,5.492371,4.675993,4.676606,9.889281,8.875661,-4.378413,-6.470373,-5.931817,-5.945594,-4.014797,-0.655559,-2.007245,3.907112,-4.654695,1.888417,3.834065,-9.420776,-2.747640,-1.237567,-5.970290,7.948887,3.094358,0.712994,4.825830,7.715464,8.709401,8.890130,-0.960876,-6.365397,6.055471,3.879690,1.564107,-8.229008,1.218623,7.193261,-7.468631,3.911915,6.551303,2.561549,-4.473739,-3.977415,-2.892528,-2.283775,1.242384,8.974838,-1.052436,9.551261,6.741880,6.081802,2.979674,-2.408524,7.487551,4.543034,5.969373,1.968590,-1.949610,2.223635,2.916424,1.881895,5.017869,-0.470989,-3.216391,0.974945,6.456429,-5.859718,6.651048,-3.048906,-7.014168,1.242398,-2.576211,-3.529461,1.716251,6.338652,9.368902,7.459081,4.489942,-3.473452,6.683432,0.951623,-6.095155,5.856456,4.068500,-0.442830,-8.063374,4.036579,-5.675776,8.920231,2.300264,0.686424,0.930386,6.658313,-1.369511,-3.911570,6.010514,-2.835076,-4.384339,-4.358815,9.663834,6.088597,-1.798428,-0.101690,-3.938370,-0.338749,-0.481368,-2.025271,-1.280045,-6.828457,7.144786,2.913475,4.713994,-0.817708,3.213263,5.287167,0.031033,-7.105951,7.286162,4.543219,-6.386370,0.100158,2.405325,7.481448,-3.788317,-2.618154,-0.960881,-6.733060,7.428472,7.922465,0.438336,2.109179,-3.937660,2.938453,-7.595002,1.643433,-0.204348,1.520470,5.434058,-7.085118,-1.050022,4.544338,-4.063528,-4.581032,6.747204,-1.080597,-9.698364,2.141038,-9.106229,-6.997800,8.807842,0.993453,0.327442,2.999944,1.815485,-6.756297,-9.973957,1.034354,0.749284,-3.836233,1.942716,-0.752420,-5.153078,-4.698162,-7.528617,7.547897,1.969166,8.875860,3.055786,3.119792,-0.671620,5.511516,1.350982,3.548650,-7.212430,6.812322,0.457634,-2.987069,-4.455298,-5.215494,6.959408,-4.397546,-2.379581,8.109426,3.635220,3.924110,-0.286906,-4.450367,1.164945,4.154632,-0.971549,7.834733,-5.526696,1.425609,6.695582,7.732593,-4.640342,5.638033,5.597680,-5.844786,9.816937,9.477128,-5.123782,1.190282,6.222971,-3.880531,-9.819440,9.738598,8.595746,8.839591,-3.504266,4.694882,-8.233717,-8.456479,-9.661982,-3.916728,-7.927716,1.251519,-7.456891,-8.111713,3.380880,0.326179,-0.186981,-0.576112,7.457089,-0.295633,-1.197008,-3.001115,-8.865367,0.934325,-3.639675,-8.038810,3.351012,7.363973,4.330120,9.576820,-9.105763,-6.870873,-4.478232,-8.905290,-0.634103,5.271347,0.412628,1.733460,-5.696835,-0.545606,1.465209,7.618859,-6.401737,-6.399055,-6.193432,1.778377,-0.379451,-9.610581,-0.029298,-7.575713,4.595931,-9.040193,-2.734199,8.862534,-4.177914,0.167201,-3.049164,-5.546288,8.411169,-1.184611,-9.894632,7.457613,0.549937,8.124376,-6.565566,-4.006775,-3.232194,-3.043223,6.991246,7.393934,6.990841,3.646115,-5.816783,2.117940,-9.900311,7.873308,6.436848,5.814768,-2.858844,-8.329938,-6.773921,6.308068,7.867424,3.225215,8.005196,-1.554609,4.905460,-6.456197,5.494589,-2.164308,-5.591882,4.816950,-0.435695,-2.318466,5.513315,6.440759,-2.990346,-1.839711,1.331748,-0.960336,5.983632,9.766292,-8.514581,-6.469195,1.639145,1.007106,-1.741168,2.523209,2.059533,-6.536726,6.400255,-6.087859,-6.814657,0.229305,7.913001,-1.995977,2.211305,7.667295,9.925731,2.774309,-4.310571,-5.447112,6.911430,6.596770,-8.330564,-6.032271,-6.633186,9.250585,7.628183,-2.377028,-2.712358,8.248478,-7.895303,8.984524,-9.264110,4.834406,3.592763,-5.608707,2.469097,9.270276,5.490771,7.332693,-6.453006,-6.997289,-0.393647,-6.823571,3.508078,-9.782002,4.808924,6.244414,-0.033282,-7.507177,0.078819,8.318724,6.333754,-1.564593,-5.215389,-9.963386,-4.755934,-5.368672,9.379892,6.562509,0.710873,-1.683956,0.215970,-1.898203,-0.229984,6.393610,4.281431,1.888525,5.898846,1.328300,7.618041,-0.086187,-0.284402,-8.462207,-0.840518,-6.019720,1.815330,-5.809049,6.608024,7.771916,8.283892,3.610254,6.296023,5.048146,-1.127181,-0.395846,-5.394444,8.048134,8.637349,-4.614718,5.821066,2.516904,-9.455809,8.520286,8.918247,7.833202,2.824882,4.179052,0.429022,8.638525,-4.389184,-6.579321,-0.867699,6.646462,0.934509,8.025992,4.547888,-2.383050,-8.256927,8.637074,-9.673838,5.313677,2.416300,-9.494521,3.499240,-4.748823,0.274958,8.615620,-1.156832,7.164393,-4.220331,-3.471520,-7.606819,0.670696,-9.074603,-5.912028,-5.786379,-6.286516,-2.720869,-0.291591,-5.767354,2.723161,9.486624,3.778039,-8.833362,-4.865637,-5.221679,-3.698876,2.159881,8.284976,-5.448375,-7.152322,6.351381,-2.663979,8.035888,-9.271380,9.556810,8.680349,-2.343223,-2.924752,8.252481,7.716411,9.397025,-8.472184,-2.257655,-8.273562,4.315454,8.866032,9.919514,7.075648,-4.783777,-4.143352,7.852055,2.556377,-4.083441,-8.775942,-0.544014,5.195999,0.564920,-5.239777,-1.166632,-2.090528,1.422309,-2.279552,7.645539,9.279711,3.055228,2.385286,4.423595,-7.394438,-5.952419,1.464520,9.329443,-9.669812,7.791607,-0.470890,8.121718,4.744047,-9.026150,5.290110,8.741092,2.122716,-2.631475,-0.446484,1.458059,-2.489481,7.205086,-6.923509,-0.737421,-6.916953,1.163117,4.724332,4.454062,9.023537,8.059511,-0.133403,3.127001,0.611419,-4.129443,6.633659,6.616508,-7.948507,-2.095064,0.556476,5.245667,-1.258032,-5.688302,-6.635536,-9.075264,3.424450,-2.282679,6.286529,9.116844,-5.325381,-1.315995,-9.408331,7.439203,-3.626200,3.771055,-3.158304,6.471789,-5.946551,5.201734,-7.416050,-0.288211,6.200103,3.129325,7.553600,9.902069,-3.864613,1.324014,4.067039,7.460752,-7.468390,4.822507,-4.991965,6.768783,-4.802291,9.100373,9.493631,-2.249902,-7.570557,5.220017,0.135707,1.522436,-8.315729,-9.921896,0.532209,6.019865,-4.091082,1.580580,-5.322581,3.204649,6.773873,4.556383,2.816471,4.324127,8.259152,0.849830,5.447316,-9.430159,9.782549,-7.378094,8.687913,5.341222,-1.392968,-5.444670,8.763845,-7.608250,-1.288159,6.864166,4.877015,7.783116,3.642390,7.176988,-6.905540,-8.019305,-4.563327,-5.992985,0.661775,-5.786115,-8.336685,-4.464110,-4.949778,-6.874498,-8.541001,-9.492039,-5.748840,-7.856788,-8.031178,4.394201,9.685503,0.578100,-3.374946,3.372386,8.449805,7.121943,-8.115565,3.432343,-6.570212,5.225154,-8.843466,0.662987,-0.662262,-4.829566,6.695372,3.206830,-3.390933,4.755873,-0.965305,-2.994945,-7.765371,-2.448445,2.671344,3.177998,6.310481,-6.809193,3.879307,9.536601,1.066439,-2.668263,8.626425,7.349265,-6.930446,-7.695646,-1.580936,-0.874681,-9.120338,6.930208,8.360051,-9.947805,-3.851381,-9.546272,-8.012074,9.114379,1.579062,-7.863364,6.632499,-5.363180,-4.152066,-9.038289,3.484838,6.868352,3.723618,0.781586,-9.395646,-4.097667,-2.328104,-5.405605,-1.374610,-2.419983,9.526426,-1.525560,0.144719,5.301434,8.513703,-4.069944,-2.798431,-5.526499,-7.061466,-3.387714,0.817181,8.831510,9.386516,-1.776630,4.763244,-3.088037,-3.193654,2.804650,4.229229,9.175023,0.035389,-5.222256,-5.291893,6.609110,-9.757142,1.676675,-0.061193,-8.225434,-4.232549,9.920304,1.467153,-8.295674,-0.634262,5.832288,-0.462550,-0.813270,-7.603081,-9.362400,-3.482212,-7.406746,1.385182,-4.340941,-4.831826,-8.140965,-9.649876,3.048597,6.508451,0.459819,0.957596,2.694493,9.419458,0.692315,-3.101215,-6.212679,-3.105529,-1.447673,-9.909918,5.630877,3.145658,0.820194,-5.246205,0.987857,3.323166,5.930799,-5.351218,-4.308539,7.826015,9.615697,8.713646,-9.831255,-0.803671,-4.905245,5.091689,-1.056489,3.617005,-2.575874,-9.328206,2.577938,-1.264265,-4.455609,1.247115,7.978171,5.809252,6.690669,-3.259449,-6.777499,-1.048787,-0.343613,-5.101065,-5.718266,-6.506509,4.319890,-2.333972,-8.844940,-6.285775,5.307622,-8.017462,-4.550745,-2.401510,-9.385191,2.238573,5.871086,0.266913,5.159185,-3.232370,8.073674,4.282841,9.570118,5.387313,-2.853572,0.681083,-2.182916,-6.632602,4.938162,-9.569919,-7.946728,-5.640855,3.207929,9.824181,0.954261,-7.350363,-8.124931,-4.387652,3.330201,-2.631315,8.848492,-8.854337,9.817510,-2.762288,9.903190,-4.524256,-9.409299,8.078022,5.751025,-0.075676,3.040473,9.759320,-5.468448,4.876789,-1.377465,-9.810018,3.256861,7.736490,9.047717,1.095773,-3.543651,-6.325982,-8.127526,-2.393084,-7.280281,0.178998,3.803018,-9.747989,-5.897077,6.293483,4.713249,-4.805856,-4.737337,3.594065,3.714967,-1.427065,-3.938137,-8.412665,2.772825,-4.788924,3.033953,4.409026,4.275570,1.130499,8.638970,-1.272872,-1.527325,-9.528083,-7.312210,-8.166438,-5.634552,3.584769,-5.172458,-4.937055,-2.916011,4.296387,-9.963676,-1.102960,-1.614337,6.693218,-6.595523,-9.045886,-2.976432,-6.146158,-3.379014,-3.175706,7.730599,-4.098003,2.412410,5.697074,5.782196,1.004894,7.852517,4.258837,6.939572,-6.815882,-5.356095,-8.714749,5.140897,4.663692,-8.963123,-4.780163,8.497133,5.716342,0.522835,-1.107974,4.727303,-2.524303,3.421685,9.233671,-6.168599,7.439047,-4.303100,1.790945,-8.466198,-4.538410,-0.034806,-4.743391,1.088936,-2.912815,3.968003,4.887937,9.486042,3.563736,-0.189425,9.923600,-9.414712,8.368940,2.226387,-1.453930,-5.904358,-3.658086,-6.081262,-0.158827,-6.456279,-5.058013,-5.661019,-4.564887,-2.170566,-2.848184,-2.419621,6.054955,-2.285713,-0.366501,-5.842241,9.476922,5.557737,5.273372,4.550866,4.542574,0.819375,2.771906,8.584103,7.957673,4.233519,-5.844685,1.308937,4.144485,5.749051,0.850660,-3.918970,-3.154371,-4.783596,2.992282,4.365235,2.558358,0.351252,-8.707536,6.496538,-9.074941,-9.860759,-1.602899,-1.141202,8.466400,7.299165,0.508874,-2.617802,8.160588,-5.394445,-4.978514,3.940453,-8.528986,-3.421651,-9.783600,-6.510950,-0.813060,5.151362,-2.142468,-8.718150,6.299569,6.100317,-7.126882,-5.282887,-0.367686,-4.838224,4.552135,8.478925,-6.124778,-6.548728,3.679101,9.070342,5.433323,-0.870161,3.075378,-4.822694,6.618758,3.098561,1.746706,6.353492,-1.334401,-7.037269,-4.065730,6.610546,6.058963,3.068863,-1.903969,-0.585710,9.249774,-3.796947,-3.382024,-0.643245,-3.831299,0.193115,4.018443,4.370759,-1.576112,7.919873,1.357883,-5.690728,3.760714,3.633494,-1.288375,4.265934,3.710625,-6.378750,-6.085211,7.690643,6.928106,-9.214877,3.095943,-2.184351,0.500032,-1.416463,1.270372,6.253282,-7.631831,-0.826758,1.814787,9.349670,0.686364,-6.933393,-7.959323,-1.678961,-2.731214,-9.559238,9.095276,2.784439,1.230887,2.991048,-5.674856,0.443354,-6.164769,-4.516693,0.271745,-4.632710,1.751884,5.158099,-9.848055,7.728939,-3.676553,-6.842125,4.003627,2.715113,-4.405143,1.496299,6.594874,5.757525,-5.152146,7.533400,9.059827,6.951359,-1.519819,-1.267624,-1.777399,6.088435,-6.237937,-4.932462,-7.265300,-9.068038,0.787359,1.718381,-4.145305,-6.960073,-9.547516,-3.128864,7.458479,5.642699,-1.835931,-0.606437,0.459639,-6.251148,6.271356,2.183957,-4.224215,-9.823471,3.496780,-1.015399,3.353760,9.710490,4.190044,0.666372,1.699999,-6.737162,0.029802,-5.464609,6.027190,-0.190292,-7.354789,-8.302847,3.927675,-7.094733,-9.272835,-8.843549,4.220854,-8.809931,1.348686,7.488077,-1.341449,3.197250,-6.342240,-8.622511,-0.133128,-3.983795,2.520350,1.308675,-2.680863,2.257510,-6.815647,-5.601120,0.117349,-9.696292,-9.078967,4.183733,-3.493205,-6.201286,4.269499,-6.122933,9.697606,-3.160223,1.601138,0.250517,0.579202,-5.618712,-0.648658,3.032287,6.285295,9.712769,8.393243,-0.568233,3.016588,-3.068110,-9.857801,-8.500918,4.713756,-5.036312,-1.154636,-3.741404,-5.863325,4.307919,4.287958,0.138506,0.359557,8.586836,0.052067,-8.793623,-4.909820,4.393015,7.915556,7.517324,-5.831108,8.321180,5.639852,-6.868522,-0.434067,1.605748,-2.407177,8.110086,1.621136,-6.763749,-1.376918,4.449317,6.531882,6.423532,-6.107222,-5.896709,-0.254394,5.136856,4.218163,-7.970884,1.619859,-2.599239,-3.972259,5.447870,-8.048326,-0.902490,-6.623350,7.951705,2.863473,-7.486241,6.561546,-2.960536,-8.930813,-7.722564,-6.902576,-0.755154,-3.001963,7.773464,-5.072818,-7.275776,4.666472,4.213024,-0.574769,8.143233,-7.134383,0.081868,-1.603309,5.992079,5.215270,1.088285,-1.198332,8.723058,-4.534640,5.742430,-1.581534,3.947714,9.457165,8.229240,0.806720,7.147084,7.510865,-4.392097,-5.860685,-5.001176,2.405694,5.070524,4.840250,-7.163815,-7.455504,-5.397402,6.581605,-4.851837,7.740533,-2.472044,-0.743126,-6.561202,-9.351032,-6.854387,-9.830333,-4.350878,-0.537712,-2.010683,-0.890383,6.522584,-2.439166,2.389139,6.182697,-0.774822,-9.072054,1.363735,-5.763214,-6.123619,-4.906099,-2.773985,6.353963,-0.419668,-0.178638,-0.806137,1.178354,1.878761,1.394921,3.046901,-9.518430,1.864371,-4.965873,-1.662517,-2.363413,1.197466,6.992155,-3.659633,-1.043741,-6.842733,1.726293,-9.935131,-1.542035,-7.923953,-4.755949,-5.946347,-9.331463,2.799358,-0.571953,7.440834,-5.066793,-5.577010,-7.593996,4.614821,6.507162,-3.736550,-8.221108,-6.141485,-9.276398,-8.100068,-9.971680,-2.827197,3.646704,-1.104535,9.774847,-8.688112,-1.236155,7.214195,9.546026,-5.000903,-4.232723,9.673786,8.996440,0.139019,3.550320,-6.449194,-7.493435,-5.791856,2.217516,6.312279,-1.333230,-8.337876,-0.262842,-7.054224,-2.835340,2.774804,3.104975,4.319785,-0.123762,-7.903890,9.362855,1.876918,6.943861,9.758170,-5.413976,3.773130,-4.536434,-5.926649,9.003133,3.793203,1.081588,-5.090176,0.787482,0.519988,-0.926003,3.767783,-4.234864,5.390542,-2.561732,-9.211481,-0.146712,-2.270436,-6.151364,8.037854,2.536299,9.282338,2.307673,4.629634,-6.679162,-5.759737,-5.036364,-4.036299,0.597227,0.766022,-9.074194,-6.320880,9.527260,9.040906,7.057340,-7.184356,9.841568,8.772293,8.011730,-9.600709,0.558240,5.599138,-6.570089,4.846258,6.477721,-5.434649,-7.712316,-6.438415,9.179266,8.818124,1.187156,4.655090,-8.950785,7.474767,0.635109,1.769765,8.839229,-2.498556,-2.130332,1.632351,-4.360984,8.444826,-1.437870,8.836604,4.292660,3.593092,-0.117906,-9.899552,3.734318,-8.354430,5.424225,-4.434229,-6.095836,-1.081070,-3.430101,0.271690,9.131857,6.331744,-5.978550,6.733459,-5.900677,-4.683201,9.396889,2.875642,4.288387,9.150095,7.471185,1.697869,9.876237,-8.976683,3.570744,-5.655466,-7.926672,-2.306847,-8.254430,-9.647914,-2.290619,4.445305,8.703782,0.421449,0.058979,5.460752,-0.039703,-1.216270,6.243771,1.065067,-2.385499,4.475497,3.541715,-5.718460,-8.482612,-7.732898,2.956819,-1.851246,-5.113360,0.037848,0.493320,-1.572915,4.986195,6.272361,1.762664,9.380284,-9.255219,-4.634600,9.835355,-7.288213,-2.514016,-3.922219,-1.400410,-4.500635,-6.404125,-9.967356,3.670679,1.163541,-2.410889,5.705755,8.596164,9.018812,8.536328,-7.164841,-7.658948,-8.098873,2.462780,0.355035,-3.632288,2.888589,9.813956,-2.037834,-5.749069,-3.727386,-8.727654,4.650382,-9.952727,7.633979,-3.789667,-3.611418,-5.766866,7.605113,-4.335945,-2.311223,0.641095,5.964589,1.539066,2.912727,-1.608046,-4.509400,6.168053,-3.563639,4.767632,1.010613,6.800825,-1.802485,1.149052,-0.068575,-7.759446,-4.418447,-1.878692,6.638708,1.760490,3.995394,-4.826801,-9.629048,1.100534,8.361389,-9.332109,7.916248,8.556544,-5.998807,5.607585,-0.276599,9.809924,6.490110,-5.782234,1.715567,5.890733,9.497241,8.369443,1.911325,5.530894,9.512212,-5.402858,8.168696,-6.733060,-6.469119,-6.557170,-5.996360,0.784007,2.016680,-0.417908,2.543974,-6.231091,1.716029,-1.237061,-0.175983,8.731288,1.421295,-7.478230,2.910397,-5.964589,8.600733,-4.205695,-6.074293,1.486088,-0.618973,1.880756,-7.263881,-1.148167,6.314648,-1.966883,-6.455223,5.698135,6.913717,8.192003,-6.135301,-4.011266,-0.105415,5.271514,-2.874555,1.953433,-4.312366,-4.143776,-4.261368,-5.418237,0.306603,2.807755,8.727092,-3.921083,5.387024,3.011874,3.926044,0.544440,9.350476,0.354940,7.794233,-4.536506,2.699208,-9.986347,9.571356,3.451958,-1.212548,8.103309,7.975162,-7.030108,7.006661,-9.402859,-2.788921,-7.618765,4.737982,1.810510,-7.812493,-5.747363,7.235499,2.148810,-5.016690,1.590523,-1.709022,-8.397923,-4.299089,-3.717032,-3.530009,0.111263,-2.797272,-3.488553,3.564509,-9.496789,8.794099,1.680501,-2.872623,-0.233452,9.248256,9.701444,-9.066461,6.352899,-1.964343,-3.943891,-6.013181,4.295551,5.634339,-0.811156,-5.901475,7.793861,-0.560755,-5.847577,8.375190,8.292373,-1.443565,-1.536793,-8.132478,-2.720926,2.764875,7.363719,-8.515885,-2.228130,1.335643,-1.410416,-6.490592,1.855313,-7.935328,6.781324,-3.364567,-4.816319,0.739138,9.535074,-0.482875,-5.136895,-9.841027,6.748747,2.859723,4.266432,6.748489,-2.194749,5.316863,-5.266999,3.281434,8.776440,-4.630198,-7.823366,2.566431,7.789887,6.695518,8.926168,8.308777,-7.197186,0.949257,2.358741,7.276843,-5.838045,-5.039679,-8.547125,-4.210690,7.329823,7.074348,-8.460256,-2.848442,-0.736155,9.476816,7.382139,5.471905,7.248098,5.299257,7.303824,-3.727561,3.492850,-9.265055,-6.021086,-0.977965,7.677878,-4.759544,-6.877418,8.328348,-4.233423,-2.105765,4.607827,-2.033190,-4.511522,-6.875548,-5.385309,5.231323,0.364472,-7.756594,-2.981094,2.550007,-6.799375,0.170096,-4.024671,-0.127298,-5.205661,9.988550,-2.362835,-3.978027,5.417717,-6.174451,-3.263746,-4.597915,4.336170,8.094165,0.283512,7.799195,-0.901370,-7.994090,5.593379,-0.397531,4.575568,9.466558,5.488497,6.383088,-0.617164,-9.576389,9.343021,-6.086921,4.267991,7.767869,3.057192,4.793934,9.397034,-2.939230,-9.683810,-9.440027,-2.655547,9.956046,-5.957772,3.979591,-4.559693,2.154334,-6.518611,-9.226627,9.655798,-0.328089,-4.698692,9.039826,3.766366,-4.323831,-5.949873,1.885927,-6.748376,-8.494834,0.064925,-3.251352,7.720985,-3.505921,5.978571,-9.470133,-9.054064,9.778992,-7.533215,-2.184486,5.599156,4.664971,-2.992465,-4.641715,9.451303,7.487454,-7.687275,-4.750307,5.031294,8.409352,1.726854,9.059739,-9.498679,-9.164814,5.313780,-1.281028,6.392567,-5.604451,9.298004,-5.078670,1.560383,8.373865,3.165446,-7.941524,-0.272997,-9.980431,9.840246,7.925791,-3.357280,-3.331115,0.336267,-9.390479,-5.452739,-4.233772,-6.241347,-2.938121,-0.906844,1.491364,3.292926,-7.785985,-2.631597,0.704915,-4.148324,3.569368,-2.919862,2.992445,3.329288,-7.172293,-6.874548,7.269626,8.317708,3.243769,9.273392,-5.183858,-7.692449,4.640697,8.477407,-3.208551,1.366379,-4.031587,6.205450,6.290969,-2.410442,-2.935239,-9.440780,1.215480,2.918824,3.708142,6.538756,7.117962,-4.081519,-0.798949,6.117840,-1.456652,8.300285,-8.379358,-0.589979,3.260546,9.497281,7.478887,1.748316,7.582536,6.404008,1.110349,-9.758503,-1.093097,1.136954,-9.859787,6.186068,-5.754771,-2.124668,3.402309,-5.465115,2.581057,-4.080622,-3.045267,6.790713,-2.101191,-2.687065,0.723254,-0.724844,-4.611938,1.152918,-9.877226,2.611870,4.387249,6.777628,-2.896227,5.041689,5.007192,-8.467401,4.295649,-8.674479,0.999972,3.368587,5.526460,-8.560167,-0.545197,8.636022,1.434374,1.901610,-6.534313,9.528908,-2.517592,-3.863652,0.592351,5.454058,-2.017905,-3.786198,7.015587,-1.929661,-8.596768,-2.405488,-5.911176,5.175650,-5.010344,-9.986645,-5.778001,1.624597,-7.835894,-1.412256,-1.752737,-4.895639,5.522598,-5.439789,3.787006,-8.660072,-3.055616,-1.676543,-9.619388,-8.415611,-1.812343,1.706365,-5.972195,4.878434,-9.773420,-7.971460,-4.889240,8.593532,-2.792172,-1.018451,-9.412850,1.182199,4.030997,-0.460891,6.742659,-7.895090,2.645792,-1.953702,-0.067127,5.124343,-4.471444,9.952399,-9.124324,-4.552067,8.155260,-7.149996,5.845951,-5.498040,5.601406,-3.769687,3.701180,-4.976966,-4.883459,-3.253929,1.328720,3.075444,-6.178982,-8.177102,4.787999,0.896527,7.449612,4.799484,0.785651,5.991641,-7.111830,3.372008,-7.389889,-0.791296,9.654288,7.374966,-5.324937,-4.574867,3.516470,-7.922887,9.799470,9.609027,6.612787,-2.245261,-2.230303,-0.894913,8.272717,-8.618997,9.522744,3.366063,-6.860077,5.316208,8.727548,9.700207,-2.665167,-9.420611,9.366071,-2.023579,-6.996925,4.226697,-1.703517,1.207034,0.162337,4.973459,-9.781059,7.549759,5.328899,-4.481153,-0.279200,-1.749694,4.703601,4.609459,-8.708972,6.563237,-3.249386,-0.687882,-9.283925,-6.194835,1.074618,9.231321,-8.540952,-6.173838,5.095032,2.835418,-7.010582,9.619424,-5.836451,-5.922558,-6.538399,7.802509,-0.767598,-0.112726,3.495833,2.927084,-8.432357,-2.405026,4.867930,8.473147,1.682953,4.863415,-9.724620,3.802784,5.369106,3.060560,-7.233758,-5.440966,-1.090879,3.718575,6.630700,6.510009,4.153593,9.322741,-1.284979,-8.699030,7.078990,-0.720883,-5.869976,-4.687758,9.132116,1.713891,-2.029991,0.708012,-5.531279,-4.458041,7.302494,-7.337412,6.408139,3.084439,-3.325247,-2.216280,3.602528,7.554502,-4.101487,6.153172,6.662073,4.129417,-3.316940,7.981967,-2.962747,4.673301,5.985288,-4.309776,1.464175,-9.796543,1.869330,3.976155,6.597153,-6.556192,-6.723132,-2.988148,6.770965,5.923068,-6.296846,-2.683162,-9.915008,-1.013190,9.210484,-8.193526,-7.933210,-6.588900,5.178174,8.167263,-8.949266,7.456388,7.538957,2.521266,7.951933,1.124745,7.045817,-6.132239,8.130395,7.636884,-1.562965,1.610348,-9.406744,-9.341736,6.219785,6.401596,-6.529596,-6.053534,-9.837063,-3.721504,-9.501094,3.539309,1.871879,9.028544,-2.829798,-6.274997,-9.320051,8.387946,2.432612,1.102484,2.080338,5.710252,3.528404,-0.722639,4.105827,7.587389,-3.805702,6.251613,0.541929,-2.736509,9.395422,-7.676499,-4.101384,-7.257914,9.935495,-8.623620,-6.072438,-4.546357,4.035943,4.092131,1.132796,-3.409409,1.675960,-6.024102,-2.206313,-1.842413,7.635101,4.842056,9.674302,3.867897,1.612672,7.213447,1.235626,3.191451,-4.318540,2.354315,-3.429887,5.498442,3.482019,-7.386437,-5.251531,1.260557,3.936840,5.096799,2.855115,0.786185,-3.837455,-3.857497,6.388949,-9.884147,9.396239,2.044047,9.021957,4.649356,-9.235635,-5.627495,2.456308,-0.244689,2.378263,8.968011,3.870220,1.361363,6.650078,5.698117,-5.615822,5.724086,-9.144959,0.557047,1.450351,-9.408833,-1.263073,7.697841,5.597922,-5.165505,1.366496,3.153574,-7.022873,7.368883,-4.588457,-1.737885,-8.038071,-1.514754,0.793943,1.056035,6.281714,-4.827257,-6.136934,2.536027,-5.149787,-3.602309,0.218299,-7.273487,6.645505,5.490556,-3.790180,-2.907636,2.746354,1.341823,-2.511877,-2.621053,0.216457,5.804844,-0.632114,4.459311,-9.415969,-1.572866,1.805110,3.186686,-1.744777,-1.358528,1.802961,-0.572188,-9.976183,7.793892,-2.433027,-6.984648,-8.906858,2.944789,-7.456243,7.250288,2.272096,-0.383545,-1.011729,5.643925,-0.366442,-7.147333,-8.718849,8.612916,-0.025246,7.871342,-5.410824,-7.602465,7.470231,5.259346,-0.303669,-7.260652,-9.713397,-0.482158,-6.854185,-0.551805,-6.015365,-7.013882,7.754094,0.686876,-6.861070,-6.359772,-7.365643,-8.116656,-0.771546,3.966536,-0.517421,-0.970407,-3.324499,-4.889549,-9.011307,9.958368,3.475859,8.046898,9.531756,-1.610906,0.261720,-1.324054,-3.253117,4.957787,-0.373542,6.893124,-9.040721,-5.149416,3.106861,-4.741916,1.616694,-4.752844,4.155450,8.822805,-7.752419,5.686074,-5.644549,2.354158,-3.587829,0.550001,6.646413,0.763230,9.059563,-5.783458,-9.377898,-3.894086,-3.582137,-7.498161,7.956613,7.524486,-9.305243,2.551034,-7.628788,5.249753,-0.792001,-5.853534,1.375503,9.475735,5.494373,1.929346,-6.231353,1.996797,-8.920091,0.137425,3.194627,5.250539,9.231819,-3.034479,6.787747,-5.915501,-6.700098,5.182046,-7.311464,-7.235262,-6.322724,-2.622399,-0.365181,-6.934133,9.689021,-8.354481,-9.500356,-5.696804,-2.080903,1.222535,-6.634518,7.458115,-1.741271,5.866173,-0.031326,-2.528925,9.474775,7.640704,-0.685925,5.115602,3.407519,-5.221870,9.483924,7.554813,6.193600,-9.783363,-4.561399,1.006936,-8.190700,-0.191516,-3.889317,-6.265891,7.389503,3.322908,5.847210,8.411561,-8.574342,-8.557475,0.954401,-6.511677,-3.285040,-6.036423,-7.214058,-0.456604,-2.987445,6.847299,3.999103,4.771121,-4.412139,5.893212,7.120346,-0.256646,-9.093014,8.045273,0.390374,8.261949,-2.672968,-6.233786,7.070374,-9.208395,3.282869,-5.203541,4.134830,4.437310,7.369263,1.481224,-2.672495,-2.285318,-1.715777,-8.695132,0.796716,0.532367,9.399875,9.492404,-5.684308,9.842596,3.280174,0.737827,5.795697,-0.725860,9.986210,6.034233,-6.313830,-8.635610,0.962861,-0.756747,-5.837958,7.318347,6.269708,-3.527683,-1.631312,-3.659671,-4.068289,-0.261614,-3.611438,-2.837900,-9.213873,7.720872,4.588004,0.511986,-2.343753,-9.175704,2.123849,9.121549,-8.728575,6.533680,2.061802,-2.676223,4.210348,4.294263,-6.047738,2.043340,4.005270,8.542465,-9.597029,4.540387,-2.493706,-0.146428,6.042548,-2.083663,8.986527,-8.913545,9.215213,-3.050861,2.896858,9.702414,1.139942,-7.553040,9.150743,-5.637945,-8.955401,6.052906,9.226768,6.428706,2.044823,-3.830404,9.294361,8.633211,6.396421,1.507023,4.851035,-5.110259,1.791003,8.859956,-3.960831,-5.652940,0.348077,6.854825,6.626064,-1.336389,7.749770,-0.220634,7.726596,3.339853,1.918611,-5.708751,6.802060,-9.173692,2.448126,-3.040376,3.931231,4.444714,-4.207426,1.114806,7.177342,-1.533464,-6.634910,0.756264,-1.724684,-1.836457,6.818321,-9.803114,-1.105147,9.267235,-9.997076,1.833974,-2.668251,-0.005543,-6.788842,8.859251,0.531054,-6.453306,-0.516964,-3.218990,-6.216214,-1.774272,6.045807,2.919461,1.128436,7.844607,-4.465952,1.637297,4.450435,9.306104,6.198147,3.894576,-2.776667,-6.700732,1.744898,4.213649,-7.367616,0.252800,-0.205695,9.843774,8.423351,0.728588,2.486942,6.516023,-1.617860,-1.202917,6.332804,4.558187,5.215309,-0.145934,-1.173583,5.748988,5.083503,-5.249531,3.291946,-4.104679,-9.305714,-1.129232,-5.241891,1.873098,-1.202006,6.226568,7.286190,8.392369,-2.675643,-2.750303,3.466043,9.494824,-6.131301,-7.905499,8.244718,9.857185,-9.667289,-5.374877,6.611219,6.036097,3.394014,4.458643,9.566377,-6.277372,-8.734506,-7.874136,-0.659228,-1.077885,2.422261,-0.248630,8.752966,5.984200,8.832584,4.240296,2.565294,-2.270418,3.410966,8.431288,-9.141668,-1.435477,-1.651935,-4.326258,2.677177,-3.846877,5.002797,0.344345,-2.992798,-3.313592,-4.230769,-8.260146,-7.851003,5.609500,-0.911418,8.842496,-7.091984,5.818302,-8.133512,1.563443,-0.946336,1.266693,-5.216079,1.201365,3.805127,-1.201198,1.595259,9.585045,4.413495,0.738611,6.198985,-6.903832,-0.967498,0.847033,2.899332,-1.450336,-1.799805,3.175115,7.199033,9.479412,-7.434873,-1.729711,-8.154638,8.629243,-8.469168,6.920802,3.977944,4.952263,8.308019,3.106362,9.486768,-1.779098,1.163422,-8.258227,-8.250773,3.764669,4.760702,-7.134071,2.011926,4.558481,-0.865250,6.990112,-3.093421,-1.884109,6.007858,-9.931323,4.026367,-4.190732,-7.760655,0.536028,-3.007701,1.454576,5.553773,7.005754,-4.123031,-1.995730,1.143306,-8.825648,3.377414,0.922020,-0.095383,2.625370,4.520436,-2.496892,8.472339,-9.252033,-2.610348,7.571751,-5.570439,-1.430172,-9.765139,5.191401,7.962231,8.196355,-9.282884,3.359703,9.837604,6.956705,0.846057,-8.135748,5.025607,-9.652622,4.162061,3.081042,2.989866,-5.434553,4.426710,5.691239,6.545061,9.517092,-7.151012,6.269714,4.636081,-1.465856,-6.945961,7.116146,7.209987,-6.391852,-9.294501,-5.405309,0.944777,7.921323,7.145825,4.611723,4.387925,-4.741271,-9.994875,6.098738,-1.331652,-7.241476,3.096491,6.560050,7.519674,5.388251,4.019191,5.991930,-9.453671,1.597300,-6.951696,-8.121892,1.171337,6.059495,-9.031119,-1.332070,-7.379164,-2.950937,-7.044912,-5.462494], dtype = "float64")#candidate|9331|(3120,)|const|float64
const_9332 = relay.const([-8.553477,5.293703,4.164432,-3.180014,-6.417549,-4.897517,1.229336,3.918467,-9.051371,1.310851,-7.888337,-0.713053,1.001269,-0.736345,-3.444224,6.456722,4.612438,1.810410,-3.102668,-1.015044,1.542452,-0.165993,-3.992203,-9.366935,4.131893,5.386959,5.504785,9.075269,-0.560819,0.042994,0.150994,3.022742,-4.708125,-9.463754,-5.410087,9.682107,7.987312,4.857246,1.907887,-1.907455,4.088043,-4.170912,-2.724545,9.010677,4.204295,0.408774,2.544837,1.290182,-1.706322,-8.835572,-3.035807,-4.234393,-2.577067,2.637870,8.525109,-4.869802,9.533081,-2.011554,-8.823753,9.813395,-3.012037,8.482975,3.307193,2.917832,-0.858842,3.291204,6.937252,-2.395706,0.467255,4.246299,1.942627,5.625899,-7.948713,-3.447795,8.780933,3.093134,8.057330,3.760982,2.683487,-6.859991,7.503723,5.066055,7.683326,-6.538654,0.057045,2.158958,0.049701,-3.267458,-2.103246,3.991014,-3.520944,-4.929045,0.924312,-2.298465,-5.389365,-0.212759,-0.118452,5.770323,7.546598,-2.054795,0.364616,5.002400,-2.324991,0.026857,7.545403,-9.960826,4.286384,7.878751,7.767220,1.495597,-8.804186,0.888503,3.499978,-6.402253,-2.339105,-4.245083,-2.336567,-6.727895,4.991339,-0.096086,-0.421931,-0.150375,6.150494,-4.095258,9.818543,-1.883449,8.981838,4.347424,-2.464074,0.740752,-6.007836,8.316937,-3.089146,-4.987503,5.081511,-0.090371,4.924131,5.963904,-9.501959,6.650969,4.105365,7.535160,0.335814,-7.793869,-4.225947,-4.597070,2.811619,2.436339,-2.435279,4.251657,-6.088976,0.183731,-0.913792,-4.771003,7.965786,-4.873983,-8.280851,9.216253,-9.625820,4.773065,-8.386091,-8.759430,2.838646,3.082800,3.157478,1.662611,-6.801460,3.584205,2.533902,4.615756,-3.734264,-9.067421,7.388164,-6.194710,2.566891,-9.945937,-5.934774,0.195112,-8.959620,9.060548,9.596230,-0.620393,0.326209,-6.281930,0.396486,8.662903,0.743040,-6.424410,-7.920402,1.032503,3.677565,7.133546,-2.936430,5.033564,8.498146,-1.662570,-9.947611,-8.929176,-9.635873,-8.843733,-1.840298,3.198318,1.361766,-0.703035,4.897042,9.297688,5.117095,-3.870597,5.116445,-4.598216,-9.608918,0.308178,0.278704,-1.507266,-0.572394,-9.635681,5.195057,3.157782,9.936034,-0.958388,1.475320,5.140335,-2.934460,-8.827486,-4.182821,-4.833522,6.684170,8.150091,8.387543,-2.497526,-5.520070,-9.679459,3.972796,8.303606,8.819631,2.931423,0.841373,6.365107,-4.170460,-7.333943,-9.644172,8.724520,-4.474884,7.791748,-3.089939,-0.307587,-5.802538,-6.850164,-7.641566,-6.660062,1.614845,-6.845090,7.357699,-5.452024,6.919628,-3.539166,2.289740,6.537978,-0.287196,9.900869,-6.544456,0.457726,-4.015525,-6.331444,1.546145,-0.017660,-0.517635,-3.097588,-3.411003,9.381240,3.077454,-9.628630,6.887671,-2.817645,-5.388348,7.582445,0.087069,6.178663,-0.730949,-2.170545,-1.584564,8.942190,7.801417,-2.174738,-7.854906,9.462573,9.404069,4.221315,9.728408,-4.940606,1.588443,9.262158,7.908602,7.194881,-7.511752,1.827017,-8.920315,-3.093400,-8.189027,-8.724183,-8.600586,-5.170688,4.477141,6.685630,-2.821132,-1.995529,0.618851,-0.279537,-4.223827,-2.744546,-9.177869,6.827734,-2.642039,-9.242160,7.085186,-9.703005,7.033969,5.100971,-6.970407,0.709270,0.879936,-0.313801,5.476563,8.661657,-9.299559,3.725661,3.502156,-9.031150,-2.609727,9.610133,7.664262,6.423210,-2.480822,6.846165,5.577506,1.523566,-3.212513,0.191619,7.701430,2.421487,0.474327,-3.289146,2.522055,-1.561685,7.982272,8.122466,5.414534,8.336020,-6.286156,-7.020699,-1.853392,-7.387429,-7.422423,-7.609427,-5.087669,0.139411,-4.376410,-4.850133,-5.503335,2.238452,-3.352936,-0.996144,-3.743098,-9.269088,-7.275798,-6.652495,-6.628519,1.114115,3.398376,-3.929771,0.075462,4.088713,5.333094,-4.528809,-5.961090,-1.060778,-7.694811,3.656788,-1.973064,7.215839,-3.198083,5.179182,-7.789215,4.664942,4.557108,7.699301,-6.095294,-0.340036,3.377700,4.797269,9.277523,-8.607543,9.086482,-8.385069,1.596157,-5.541921,8.484111,2.423583,7.223181,3.512266,-7.445726,8.388731,8.977143,0.633598,-2.665405,7.464050,-0.176998,-7.062592,2.436920,6.425419,-5.753428,-2.298023,-7.273233,-0.774328,5.857804,-9.562863,-8.847719,-4.807737,1.690320,-4.521691,-1.013450,7.987382,-3.198285,-6.764716,-3.267708,-1.579064,-0.430852,3.264286,-0.786864,-4.306949,0.941981,-7.450170,-8.768790,-6.197764,-5.021194,-6.524290,-4.242074,0.703416,3.587194,-2.914711,2.636149,-5.467070,6.523721,-1.938145,4.669828,1.453259,3.229548,9.052007,-7.950371,-5.413990,-9.046317,-3.779647,-6.516329,9.496932,4.248774,-2.609467,9.277953,-5.192380,-9.274126,-8.822748,2.273141,-9.299930,6.541242,2.474166,5.177485,-1.778505,-6.781375,-8.984945,-3.285018,-3.897357,3.277998,3.065170,1.278025,-9.383206,-2.185171,-3.709980,-3.528257,6.581531,-4.170951,-8.864324,-0.101318,9.322352,7.475302,4.380743,-8.259717,1.531684,-6.841228,-3.415003,6.573726,6.901443,1.988242,7.155925,5.991145,-8.786193,9.047002,9.784702,7.079887,-4.510039,3.087781,2.399191,2.972012,9.775702,0.040002,-9.937421], dtype = "float32")#candidate|9332|(504,)|const|float32
call_9329 = relay.TupleGetItem(func_3987_call(relay.reshape(var_9330.astype('float64'), [56, 1]), relay.reshape(const_9331.astype('float64'), [3120,]), relay.reshape(const_9332.astype('float32'), [504,]), ), 1)
call_9333 = relay.TupleGetItem(func_3992_call(relay.reshape(var_9330.astype('float64'), [56, 1]), relay.reshape(const_9331.astype('float64'), [3120,]), relay.reshape(const_9332.astype('float32'), [504,]), ), 1)
func_4659_call = mod.get_global_var('func_4659')
func_4660_call = mutated_mod.get_global_var('func_4660')
call_9344 = relay.TupleGetItem(func_4659_call(), 0)
call_9345 = relay.TupleGetItem(func_4660_call(), 0)
output = relay.Tuple([call_9327,call_9329,var_9330,const_9331,const_9332,call_9344,])
output2 = relay.Tuple([call_9328,call_9333,var_9330,const_9331,const_9332,call_9345,])
func_9364 = relay.Function([var_9330,], output)
mod['func_9364'] = func_9364
mod = relay.transform.InferType()(mod)
var_9365 = relay.var("var_9365", dtype = "float64", shape = (56,))#candidate|9365|(56,)|var|float64
output = func_9364(var_9365)
func_9366 = relay.Function([var_9365], output)
mutated_mod['func_9366'] = func_9366
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9441 = relay.const([[[-3.979454,-9.664044,-3.603360,-4.197416,-8.962685,6.221358,8.354997,-0.255583,1.587861,-6.088978,-5.628455,2.935763,-0.021287,2.509618,-2.634810,-5.937997],[6.619510,-8.202546,-5.872505,-4.316877,-8.309388,-2.982359,2.077442,3.671786,-0.847554,-1.391703,-9.538374,6.350446,6.265260,1.182283,-1.815798,-1.420751],[-7.496698,4.893224,-1.382732,8.022994,3.668279,-7.437210,5.554813,5.956351,9.667838,-9.902193,9.245000,1.715530,-4.970570,2.273145,-7.968990,-2.070866],[-8.087555,-8.963160,-3.429233,3.959362,5.759692,-9.090683,0.957201,-0.641616,4.115113,-0.960022,3.632784,4.702018,-2.816398,-1.448488,7.126592,7.278169],[-3.141692,-2.565448,-9.110625,-5.426651,0.804405,-5.302384,-5.679434,7.980942,2.582322,-7.009492,8.066677,-3.118639,-1.518410,1.940916,1.916517,1.304532],[-2.531662,-5.349632,2.881715,-4.106739,3.730263,6.581430,-4.479130,-6.661562,-6.475807,-9.943668,-9.813348,6.841018,4.349586,-1.895394,-7.026094,-0.892281],[1.794752,3.191735,8.502013,7.990868,-4.889563,-1.903898,-8.405242,-4.626012,9.817436,-6.930120,4.928241,2.825437,-6.138981,5.068669,3.687248,6.086000],[7.999770,-3.809324,9.967853,6.835071,-6.563268,-2.724573,-3.080167,-2.800443,4.935544,-8.625002,-7.746958,9.104092,3.674544,7.451022,-1.132167,-8.757072],[4.681325,-7.190136,-8.594705,-5.180238,7.304160,6.242927,6.841363,1.513127,6.128117,1.688703,3.024444,-0.401478,-8.043427,-5.430612,2.476170,-3.643157],[4.701649,3.085389,-2.111658,-1.250927,-9.699283,-4.097112,6.742044,-2.321963,1.491568,4.514849,-7.052311,4.767594,7.717781,3.947203,-4.234858,-2.349103],[-3.697493,-1.675635,9.626245,-2.096672,-3.532297,-0.670075,-9.931149,-1.316934,-9.172073,2.180833,-4.760831,9.242283,-1.488752,-0.960917,-5.751408,-5.851868],[-5.615952,-5.149478,8.772701,2.499844,0.935674,-8.377981,-7.636133,9.513997,-9.835478,5.197537,5.348144,-0.529403,2.173468,0.105479,1.154650,-6.961021],[-4.314799,-3.933815,1.767432,4.802012,1.715128,-7.569633,5.159018,-4.689450,-1.958329,-8.671292,8.736558,5.935567,7.941316,-7.568038,-5.608415,-0.338193],[9.140690,9.575906,-7.655300,2.296412,-8.215921,3.893607,0.708837,2.131318,9.673657,-8.493889,-4.795558,2.960389,-7.557944,7.401393,-0.583187,9.020524],[-7.034714,-8.738783,2.332246,-0.801729,8.146247,7.006608,8.704546,1.403471,-6.080503,7.089585,2.411208,-6.013007,2.019017,7.365332,1.331940,8.695829]],[[3.916549,-2.630883,-9.029160,-5.008271,-2.645268,-3.633488,-9.426703,-8.510576,4.216581,7.985885,-5.024585,-5.098789,6.634950,2.589617,-7.413045,-0.985127],[-9.402651,2.987914,6.211558,9.574954,0.780985,-4.424957,8.631974,4.611712,-5.303994,6.905897,-6.106842,-6.856603,8.299779,0.885733,1.090723,0.886285],[-4.931314,-5.277767,-9.418028,-1.338285,1.093871,4.692845,9.679457,-7.649337,-0.210843,6.495686,8.148880,-8.418784,5.174643,8.839901,-1.196758,2.938896],[1.553820,-6.144238,7.653713,3.620244,4.375528,5.697699,6.381699,0.868648,0.823822,5.294551,-3.427383,-7.157706,1.317672,-3.594280,-6.775147,-2.060892],[2.042020,-1.489552,6.441288,-0.368212,-7.248530,-2.502048,2.175667,0.755268,-5.416321,6.945977,3.090074,-0.185099,6.959702,-9.730183,-0.174172,5.628349],[4.159786,-9.335954,-3.562358,-4.757434,-5.766389,-4.996838,-9.604887,1.314577,-0.441743,6.646016,-4.396121,-0.154582,0.781899,3.881012,-8.436937,6.380806],[-0.518113,-9.194390,-4.155996,-1.313942,7.093591,-8.145896,-3.253315,-4.193918,1.103178,-8.191960,-5.300074,2.938486,1.505567,2.108638,-5.211376,-1.357098],[7.681576,9.887086,3.931889,-9.789999,-5.069774,-6.383339,-7.390000,-6.903115,-7.726470,9.670905,2.753849,-2.681818,-4.631459,-4.307945,8.067005,1.683372],[-4.868940,-1.828356,-0.795241,-8.829015,-8.564644,-8.565014,-4.236952,-2.690331,1.218018,4.590600,-1.575633,-8.684412,8.031759,9.193321,9.344097,8.732637],[8.444314,4.299130,4.143186,9.230646,-0.832372,-6.800162,-6.129138,2.611327,8.835993,-9.893578,3.505087,-8.335829,-2.746936,7.642373,-9.370175,7.149073],[-7.473039,-6.631317,-9.478035,0.712586,1.774821,0.365709,-3.993526,3.559990,0.010477,-3.147068,-6.917267,-2.573997,-4.013983,-7.706225,-3.380950,7.202668],[-6.078315,-1.405583,7.043487,5.250689,-4.596757,-4.828041,-9.025559,-4.489150,9.423261,-8.471095,4.376735,-3.591705,-2.579781,-1.428060,-0.151170,3.029929],[9.936952,-7.353405,-7.558640,1.665246,-7.459582,0.251283,-9.587154,7.859888,-5.895346,7.740112,-4.101351,-2.820576,6.721759,6.026779,-6.451697,-7.787007],[9.353872,-6.626314,9.981510,-6.916013,2.376613,-8.377275,8.009694,6.253080,0.144756,1.570245,0.617877,-9.103003,-5.955799,-1.270385,-5.768254,0.484086],[9.629494,1.297228,8.310529,7.094386,-4.190389,-4.709140,5.267991,5.137606,9.095423,-9.234283,-3.857385,1.326162,-4.343283,1.507714,-9.461082,-0.620362]]], dtype = "float32")#candidate|9441|(2, 15, 16)|const|float32
uop_9442 = relay.log2(const_9441.astype('float32')) # shape=(2, 15, 16)
output = relay.Tuple([uop_9442,])
output2 = relay.Tuple([uop_9442,])
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
	relay.transform.ToBasicBlockNormalForm(),
	relay.transform.FuseOps(3),
	relay.transform.DefuseOps(),
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
