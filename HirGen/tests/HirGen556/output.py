import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_63 = relay.var("var_63", dtype = "uint8", shape = (8, 13, 4))#candidate|63|(8, 13, 4)|var|uint8
var_64 = relay.var("var_64", dtype = "uint8", shape = (8, 13, 4))#candidate|64|(8, 13, 4)|var|uint8
bop_65 = relay.multiply(var_63.astype('uint8'), relay.reshape(var_64.astype('uint8'), relay.shape_of(var_63))) # shape=(8, 13, 4)
output = bop_65
output2 = bop_65
func_77 = relay.Function([var_63,var_64,], output)
mod['func_77'] = func_77
mod = relay.transform.InferType()(mod)
mutated_mod['func_77'] = func_77
mutated_mod = relay.transform.InferType()(mutated_mod)
func_77_call = mutated_mod.get_global_var('func_77')
var_79 = relay.var("var_79", dtype = "uint8", shape = (8, 13, 4))#candidate|79|(8, 13, 4)|var|uint8
var_80 = relay.var("var_80", dtype = "uint8", shape = (8, 13, 4))#candidate|80|(8, 13, 4)|var|uint8
call_78 = func_77_call(var_79,var_80,)
output = call_78
func_81 = relay.Function([var_79,var_80,], output)
mutated_mod['func_81'] = func_81
mutated_mod = relay.transform.InferType()(mutated_mod)
var_118 = relay.var("var_118", dtype = "float64", shape = (12, 5, 8))#candidate|118|(12, 5, 8)|var|float64
var_119 = relay.var("var_119", dtype = "float64", shape = (12, 5, 8))#candidate|119|(12, 5, 8)|var|float64
bop_120 = relay.mod(var_118.astype('float64'), relay.reshape(var_119.astype('float64'), relay.shape_of(var_118))) # shape=(12, 5, 8)
output = relay.Tuple([bop_120,])
output2 = relay.Tuple([bop_120,])
func_133 = relay.Function([var_118,var_119,], output)
mod['func_133'] = func_133
mod = relay.transform.InferType()(mod)
var_134 = relay.var("var_134", dtype = "float64", shape = (12, 5, 8))#candidate|134|(12, 5, 8)|var|float64
var_135 = relay.var("var_135", dtype = "float64", shape = (12, 5, 8))#candidate|135|(12, 5, 8)|var|float64
output = func_133(var_134,var_135,)
func_136 = relay.Function([var_134,var_135,], output)
mutated_mod['func_136'] = func_136
mutated_mod = relay.transform.InferType()(mutated_mod)
const_308 = relay.const([[[-7.794307,8.194399,6.400473,8.429950,2.966348,-0.844938,7.838750],[-2.808391,3.812002,-4.540065,2.844861,4.841077,-0.986670,-2.068549]],[[-2.991725,-4.146869,-4.628978,-5.863699,6.602540,-5.768753,-5.379762],[-2.903075,8.261583,1.773448,7.491009,-1.513979,-2.351160,-7.368693]],[[9.104319,7.922207,7.741458,-8.521905,2.023108,6.372812,-9.713120],[9.711204,-6.140080,8.842234,-8.439599,-9.366113,-9.171578,-4.026822]],[[-6.056427,-2.499948,9.942696,4.322496,7.125299,-1.535649,6.879356],[-8.997280,0.250628,-8.802256,2.561013,1.063972,9.098097,-5.836026]],[[-7.673102,-5.122796,0.277410,-3.156908,-4.590280,6.032030,0.335923],[-9.935867,0.435309,8.234393,-5.208581,-1.694733,1.499196,5.367982]],[[-3.065510,-3.712652,-4.163713,8.583663,4.890908,-2.201964,-7.039886],[-7.899028,9.333697,-2.975731,2.080753,-1.700602,6.298643,1.224374]],[[-1.260314,0.136772,-3.752106,-7.202216,8.950074,9.411622,5.766075],[-0.669068,8.699388,-8.045547,-6.386743,-9.118649,-6.795471,0.435242]],[[2.951040,-3.696703,-7.157781,-5.541475,4.675188,7.509549,1.300046],[-8.807644,3.620180,-2.086856,4.021044,5.230840,5.299943,1.930449]],[[-4.522899,9.417568,1.820149,-3.124213,-5.726547,9.917436,5.004265],[-8.238973,4.222703,5.435988,2.231936,6.070480,-8.939367,-7.647025]],[[-2.337887,2.746333,1.083246,1.752470,-9.904763,-2.117360,-8.197220],[4.477217,-4.319746,-6.929209,-1.938546,-3.190006,2.178338,-7.112587]],[[5.971277,2.804848,-1.025103,-4.634914,-4.461938,-8.169286,2.299587],[6.021916,-5.204732,4.159892,-3.949165,-7.832645,-8.129165,-8.347238]],[[9.260103,1.741173,-4.311810,-1.755373,-4.493437,-6.461311,-4.274339],[5.228965,2.058242,-7.938081,3.501421,-6.944376,6.379422,-8.806893]]], dtype = "float32")#candidate|308|(12, 2, 7)|const|float32
uop_309 = relay.log10(const_308.astype('float32')) # shape=(12, 2, 7)
output = uop_309
output2 = uop_309
func_318 = relay.Function([], output)
mod['func_318'] = func_318
mod = relay.transform.InferType()(mod)
mutated_mod['func_318'] = func_318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mutated_mod.get_global_var('func_318')
call_319 = func_318_call()
output = call_319
func_320 = relay.Function([], output)
mutated_mod['func_320'] = func_320
mutated_mod = relay.transform.InferType()(mutated_mod)
const_336 = relay.const([[[-7.735181,-1.294075,4.646279,1.030736,-2.685839,-1.515336,-8.225994,-3.324968,0.869950,1.526588,2.707323,4.398360,1.293625],[2.695577,9.770012,-6.220899,0.542530,5.622735,1.689763,9.130881,0.130514,-1.618561,8.911907,8.711162,4.325597,-0.745148],[-3.383019,-0.251335,9.659122,-0.288948,8.559305,-4.509015,-8.699771,9.330463,-1.567411,2.732255,-7.055883,-2.301251,-2.017361],[9.289125,-5.825526,1.605975,6.861841,-0.314915,4.863206,1.921568,-4.446502,-5.104866,-7.046213,-9.036114,-9.085067,-8.540077],[-0.393376,-9.781332,-9.022617,-5.066580,3.549859,8.534302,-9.131641,-6.948887,-0.269227,-0.522483,3.740336,6.029045,-8.502478],[0.455164,5.174032,-4.329539,-1.909664,1.028642,-0.481873,4.081546,9.981999,-2.099422,-2.710624,2.413930,9.826755,5.096534],[-4.025875,-9.603539,6.511626,-6.275120,8.946932,-2.656841,7.293978,-8.754286,0.081433,-6.870365,-1.931616,-4.688831,2.734967],[6.788446,3.659565,4.311808,-0.287471,5.109597,3.696350,-8.280870,-1.308007,-6.293436,-5.965614,7.050180,-9.314383,-7.351261],[-8.679255,-2.836971,8.835675,-0.409724,-1.766267,-8.302262,7.769716,-6.077456,4.577244,5.460840,3.993899,-3.218407,-3.316230],[-2.441930,8.059675,2.977903,1.313458,8.116916,-6.188339,-0.663084,9.201712,0.197247,-2.518119,-1.390939,-4.598671,1.151994]],[[9.782253,-5.132733,7.299952,4.340905,7.911600,-2.657435,-3.442185,2.475996,-4.134410,3.838473,1.532758,-8.576113,0.148263],[2.959180,4.512606,3.924113,-2.291225,-6.107043,-7.187616,-4.709059,7.455831,8.555392,-2.204938,-3.628182,-9.755114,2.792258],[-2.178946,1.349031,-7.725195,5.972497,5.815491,-9.254580,-5.365641,8.837558,-2.748640,0.944877,-2.398945,4.648406,5.418684],[2.804499,-5.053749,0.187252,4.644938,-8.360971,-3.248770,1.080137,-1.457756,3.817509,-2.798078,-0.805880,0.381849,-1.024653],[-1.839789,-2.362740,2.644569,4.321909,-2.427044,-3.682970,7.638434,5.176296,1.051852,7.670561,6.784313,-7.319922,1.780120],[-6.522438,-8.137588,-9.780344,2.217788,9.675342,3.342170,-6.396800,8.758184,6.508917,7.649533,-4.282342,5.499928,-1.975019],[3.974647,-4.729832,9.836927,4.642254,-4.059369,-9.477891,-4.541747,-6.779275,-9.931524,-8.807742,-7.980066,-0.447113,-4.120364],[-7.093877,-1.627485,-6.430318,7.581730,-0.778365,-3.147167,2.749302,-6.601743,-9.814424,1.755722,-2.004593,7.767628,5.551205],[-0.288136,7.736681,5.859456,-8.327137,-5.637455,6.672695,2.826828,4.085682,6.826291,-1.196165,-1.359845,-0.808120,-6.363167],[-1.939024,0.589304,9.327989,0.892705,0.971865,-4.192813,3.736526,-0.200007,-2.170624,-4.805786,3.130274,-0.265615,1.773947]],[[-9.620823,-2.251881,-1.017137,-4.680266,6.688219,7.126743,-4.733512,7.447109,-0.100121,-7.320379,4.432195,4.727158,-2.072721],[7.456827,-6.214933,5.095844,-1.244993,2.735620,-6.677413,4.967104,1.439105,3.898575,0.785722,-6.084853,5.570417,-6.524433],[-6.756845,-1.463617,3.012750,1.479119,5.052543,-8.942907,4.549612,-5.265664,-7.447401,8.942506,8.845141,1.881034,0.846075],[-9.943424,-0.080954,9.676304,-0.843939,8.672805,2.193643,-5.846355,-8.283459,-7.294430,-7.662085,4.814738,-3.946106,6.870205],[1.481771,-4.881892,-3.259828,4.350195,-6.488939,2.828370,7.371808,-8.819070,-6.468281,2.902170,4.794630,-7.024879,-8.830447],[-5.461336,-6.295902,-0.891829,3.338228,-6.319647,-2.029434,-3.031907,-2.541273,9.750189,8.786513,-2.689918,-2.080559,-1.256771],[0.449872,-5.931272,-3.672425,9.653248,-3.447017,0.462555,-8.523407,2.411452,1.133207,6.198895,-3.593720,8.287851,-4.543116],[8.409112,1.788757,9.550057,-2.761685,9.262369,-0.668897,8.415975,-4.972491,-6.748563,-6.066089,8.092023,-8.022840,1.997490],[-4.920560,-4.577156,-7.850800,1.741927,8.197974,-1.229460,-2.456684,-0.561937,-5.757361,8.433169,-2.259792,-3.870107,-8.040563],[3.157461,-2.466634,8.484786,0.400950,-1.565635,9.177947,-7.840082,-0.189523,-2.557123,-9.105404,7.614710,-9.934205,4.783235]],[[9.673535,0.819539,-4.711931,-1.872476,1.459860,1.794928,9.489093,-4.997306,4.368792,5.348409,2.211056,8.628792,-3.291294],[6.150221,2.311206,-6.665414,-7.511397,-0.340392,-1.733845,0.146526,-8.507154,-6.858132,-8.815920,-5.681327,7.819702,0.609940],[4.954161,-7.139963,-9.419750,-3.846259,4.684892,-8.852722,-8.371174,-7.747622,7.030259,-8.957197,-1.905760,2.424098,9.362003],[-5.489306,5.705258,-0.873283,-4.968027,-4.616527,-9.762897,6.802373,1.223839,0.592400,-3.780177,-5.825286,3.153983,-0.400384],[-4.541240,6.131254,2.489310,-3.638360,0.072140,-6.914759,-8.302106,-4.039342,5.390591,-5.162564,9.798257,5.058943,2.272205],[8.169540,-6.773543,-9.353287,6.837824,7.263734,5.898583,6.291552,-6.422256,9.915097,9.625334,9.237907,5.397693,1.712408],[1.994484,-9.031755,0.341556,4.378068,2.792378,-4.507030,4.344326,-1.094845,2.947281,-1.267880,0.313033,-0.299008,6.202222],[1.616108,0.563456,-9.320040,7.930132,2.438753,-1.158398,5.615054,-9.258687,1.554180,7.838924,5.391119,0.502088,-3.242775],[7.923181,5.897009,-9.550456,1.696096,-8.650759,-0.394943,-5.942989,-6.246737,-6.013539,2.042280,0.277722,9.964139,-9.443622],[5.452923,-7.878503,-2.211188,5.138661,-7.725640,-9.987630,5.040109,4.162665,9.086629,-1.522571,5.134667,5.195937,4.040647]],[[3.213798,9.988150,6.994377,3.752969,-3.470839,1.549271,-4.835159,5.428647,8.746509,8.279016,-5.590807,6.069094,-4.298648],[4.307531,8.240444,-6.163341,3.438215,-3.617447,-5.045732,-7.057418,0.108472,-4.076487,-0.815278,-7.937444,3.018401,-6.162990],[-4.920005,-6.870069,-1.626457,-5.577302,-5.809394,-0.925432,-9.322030,2.204029,9.482489,2.868322,5.046652,-1.458882,4.549412],[-9.669453,-1.987120,-3.637569,-7.373027,7.916343,8.891347,-8.571786,-7.690322,6.019770,4.474330,2.384202,7.579529,6.704770],[7.073435,-2.165268,-0.756111,2.534076,2.896344,-4.526492,-4.621909,7.096789,9.863606,7.720775,-7.562926,3.457945,1.087727],[-0.184669,6.985512,-5.266222,9.076872,-8.276186,2.400126,-1.437623,0.863627,-4.358921,-2.035601,1.429275,3.893655,3.496371],[-9.918157,0.502490,-8.339672,-1.608750,5.193806,-3.939885,4.837419,-3.157095,-7.835066,4.581689,7.694266,1.642427,0.261856],[-5.090806,2.338209,3.406191,-3.308133,-2.980971,-8.201281,-3.579429,0.906289,4.054294,4.519641,0.632200,-1.576435,-5.024365],[-4.042889,-4.502773,-6.681459,-4.772506,-5.006618,9.508454,-5.023984,6.262422,-7.079306,-0.609117,-5.123926,-1.264791,1.736885],[0.119155,9.384887,-8.779913,2.193120,6.018759,7.880316,-6.820908,8.545166,-9.830269,7.149109,7.668692,8.194511,8.792967]],[[2.595029,-6.710777,7.946522,-9.213940,6.239851,-4.706363,2.820618,-9.641175,9.977346,5.886384,0.121206,-9.352633,9.341615],[-5.687257,7.462792,6.676349,-2.189033,3.841695,0.719294,-9.744097,-1.975524,-5.172731,-0.692645,-3.148157,3.657834,9.579893],[3.395293,9.893550,6.229282,-3.942814,1.417524,1.381644,4.363833,6.007676,-2.569189,9.583521,-6.729941,4.342075,-0.278361],[-3.729505,8.887040,-5.835044,1.886807,4.349811,-3.596915,2.635796,9.163748,9.224823,8.722527,-1.472230,-0.078671,3.319354],[0.931125,2.091533,-1.488124,6.965825,9.518262,3.948752,4.803437,3.815485,-6.022702,7.877310,3.062186,-9.041089,2.084743],[9.095222,-0.215384,-2.333424,0.872258,7.139465,0.996739,8.085815,4.642567,1.064894,2.283984,-9.977396,1.000075,-4.093090],[-9.258131,7.676637,6.677698,7.295994,9.988068,4.179839,6.665820,4.802607,0.523139,-1.552935,0.208595,7.935066,-8.000556],[-2.134313,8.996533,0.619747,2.424311,5.681218,2.101922,-4.050244,-2.824317,7.011089,-0.176660,-3.381283,8.336429,-7.207970],[-3.558560,4.169577,7.263810,-2.380944,-7.697280,-1.600582,-8.003665,-9.687993,-0.781907,5.269690,-6.119107,6.572421,7.183353],[-6.243568,-3.288924,3.688842,-6.004434,0.695144,-1.553911,-7.931822,2.778773,-2.140237,-8.213494,3.071093,0.973205,0.630431]],[[8.986780,-1.786412,-6.639148,9.508027,-2.279501,8.384430,-1.341126,-8.088355,-9.768474,5.436110,-4.055129,-3.863141,4.295384],[9.347304,-6.906684,-5.232887,7.148879,-6.161356,-8.278903,-3.353079,-7.818857,8.079155,8.790916,9.328478,9.374805,4.165180],[-7.504195,-1.643666,-3.102592,-5.953819,2.838334,-7.305704,2.716679,-9.026999,1.522544,-0.333799,3.191515,-4.459967,-3.394779],[-8.313564,-9.913987,6.925512,8.105440,-1.314345,4.999078,-0.255174,-5.837474,-9.513446,5.535883,2.142202,3.904147,-4.716814],[6.383341,7.504358,-4.715685,4.386431,-6.315137,6.700749,0.605143,1.568015,-7.095788,5.604144,-3.534927,2.442963,-2.050607],[-6.619541,-4.948121,-1.889695,5.298953,8.980911,-8.189062,5.985678,4.302455,-7.926443,-2.886609,-6.811062,-6.408383,9.630398],[9.689748,-9.643934,7.729847,8.653561,-8.486955,-3.116710,-3.824906,3.905405,-3.935223,1.950287,-0.022858,-5.996482,8.472477],[0.400359,-9.701613,-0.919132,7.390315,-6.238949,-1.597855,9.018513,5.016936,-2.684695,1.985756,-6.438972,-4.311998,-4.683443],[-6.057977,-9.858581,5.000414,4.920882,-1.552193,9.451440,-8.839838,0.224850,1.900878,6.895288,-5.353187,-0.292844,-5.400208],[6.920946,-8.334541,8.725012,1.929666,-5.905997,6.697199,-5.256017,-5.084242,-0.397556,0.782991,6.851754,-1.454719,-0.360373]],[[-5.318077,-7.314762,2.258369,-6.410943,0.963589,-8.428425,1.930565,7.533504,-3.364863,-7.404439,9.286651,-2.430376,-1.638388],[-8.476681,-7.206291,9.215471,5.218477,5.012994,-4.319076,5.872609,5.482930,-2.656599,-0.573965,-1.825360,9.146589,4.942117],[4.993951,-4.974548,0.678816,-9.837345,2.867301,7.656134,6.969058,0.390684,-5.646894,-0.862946,8.615583,-5.723072,-5.815737],[-5.028635,9.636928,9.888460,5.959125,8.231106,-8.687286,1.948110,9.468282,-7.511528,4.293530,-0.162801,-0.551354,-7.450293],[3.431675,-7.950777,3.132509,-1.410396,-8.715000,8.532529,8.574406,9.188559,-9.314091,3.179990,5.843146,-1.821842,4.047232],[-9.520137,3.704902,8.326114,8.495498,3.683097,8.750729,1.709399,9.217145,1.234558,5.036029,-6.480842,4.821916,-7.780779],[1.212907,-4.309055,7.766260,0.836569,1.906425,-5.744357,-0.118800,1.825886,0.638194,9.337169,8.308171,4.501290,9.422096],[-6.019848,8.091683,7.773146,9.485488,3.712220,-9.261947,-0.459901,-1.641393,-1.010228,-9.255655,-4.748924,7.650329,-2.737249],[-7.742329,7.276366,0.670787,3.898752,-2.418380,4.193780,-3.098646,1.496254,5.087520,-1.777779,-4.229398,-9.186599,-9.392728],[-7.334763,1.083208,-2.675726,-9.278647,7.188798,9.698719,-1.372101,-3.549832,8.545925,-0.676883,7.364805,-4.798107,7.297439]]], dtype = "float32")#candidate|336|(8, 10, 13)|const|float32
uop_337 = relay.cosh(const_336.astype('float32')) # shape=(8, 10, 13)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_340 = func_318_call()
call_341 = func_318_call()
uop_344 = relay.sin(uop_337.astype('float64')) # shape=(8, 10, 13)
output = relay.Tuple([call_340,uop_344,])
output2 = relay.Tuple([call_341,uop_344,])
func_348 = relay.Function([], output)
mod['func_348'] = func_348
mod = relay.transform.InferType()(mod)
output = func_348()
func_349 = relay.Function([], output)
mutated_mod['func_349'] = func_349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_350 = func_318_call()
call_351 = func_318_call()
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_352 = relay.TupleGetItem(func_348_call(), 0)
call_353 = relay.TupleGetItem(func_349_call(), 0)
func_133_call = mod.get_global_var('func_133')
func_136_call = mutated_mod.get_global_var('func_136')
var_356 = relay.var("var_356", dtype = "float64", shape = (480,))#candidate|356|(480,)|var|float64
call_355 = relay.TupleGetItem(func_133_call(relay.reshape(var_356.astype('float64'), [12, 5, 8]), relay.reshape(var_356.astype('float64'), [12, 5, 8]), ), 0)
call_357 = relay.TupleGetItem(func_136_call(relay.reshape(var_356.astype('float64'), [12, 5, 8]), relay.reshape(var_356.astype('float64'), [12, 5, 8]), ), 0)
output = relay.Tuple([call_350,call_352,call_355,var_356,])
output2 = relay.Tuple([call_351,call_353,call_357,var_356,])
func_358 = relay.Function([var_356,], output)
mod['func_358'] = func_358
mod = relay.transform.InferType()(mod)
mutated_mod['func_358'] = func_358
mutated_mod = relay.transform.InferType()(mutated_mod)
var_359 = relay.var("var_359", dtype = "float64", shape = (480,))#candidate|359|(480,)|var|float64
func_358_call = mutated_mod.get_global_var('func_358')
call_360 = func_358_call(var_359)
output = call_360
func_361 = relay.Function([var_359], output)
mutated_mod['func_361'] = func_361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_391 = func_318_call()
call_392 = func_318_call()
var_398 = relay.var("var_398", dtype = "float32", shape = (12, 2, 7))#candidate|398|(12, 2, 7)|var|float32
bop_399 = relay.power(call_391.astype('float32'), relay.reshape(var_398.astype('float32'), relay.shape_of(call_391))) # shape=(12, 2, 7)
bop_402 = relay.power(call_392.astype('float32'), relay.reshape(var_398.astype('float32'), relay.shape_of(call_392))) # shape=(12, 2, 7)
uop_406 = relay.cos(call_391.astype('float32')) # shape=(12, 2, 7)
uop_408 = relay.cos(call_392.astype('float32')) # shape=(12, 2, 7)
func_77_call = mod.get_global_var('func_77')
func_81_call = mutated_mod.get_global_var('func_81')
var_410 = relay.var("var_410", dtype = "uint8", shape = (416,))#candidate|410|(416,)|var|uint8
call_409 = func_77_call(relay.reshape(var_410.astype('uint8'), [8, 13, 4]), relay.reshape(var_410.astype('uint8'), [8, 13, 4]), )
call_411 = func_77_call(relay.reshape(var_410.astype('uint8'), [8, 13, 4]), relay.reshape(var_410.astype('uint8'), [8, 13, 4]), )
uop_419 = relay.atan(var_410.astype('float64')) # shape=(416,)
bop_447 = relay.floor_mod(uop_406.astype('float32'), relay.reshape(var_398.astype('float32'), relay.shape_of(uop_406))) # shape=(12, 2, 7)
bop_450 = relay.floor_mod(uop_408.astype('float32'), relay.reshape(var_398.astype('float32'), relay.shape_of(uop_408))) # shape=(12, 2, 7)
bop_455 = relay.less_equal(call_409.astype('bool'), relay.reshape(uop_419.astype('bool'), relay.shape_of(call_409))) # shape=(8, 13, 4)
bop_458 = relay.less_equal(call_411.astype('bool'), relay.reshape(uop_419.astype('bool'), relay.shape_of(call_411))) # shape=(8, 13, 4)
func_133_call = mod.get_global_var('func_133')
func_136_call = mutated_mod.get_global_var('func_136')
const_460 = relay.const([-7.240301,-5.981198,4.707958,6.973245,8.472349,-2.728094,4.455628,6.239428,0.254493,4.172078,-0.401176,9.967744,1.478970,-2.800663,5.664479,-1.667982,8.759942,0.436948,-1.333770,-5.268381,3.024171,4.520344,-1.054285,8.618536,8.133254,-9.507484,-4.905274,8.524215,2.428214,6.728891,-9.457854,-9.650645,-8.518667,1.728021,-1.996446,-9.328011,-0.802578,2.705009,-8.656496,8.746266,9.937621,-6.891385,4.246262,-4.988963,5.968596,-6.533672,7.882494,-2.740433,-6.224514,-8.360040,1.486699,-8.035366,-6.972874,-7.136447,-9.560966,-3.942052,6.205322,-5.105075,-6.373780,2.054803,-0.382104,-2.321463,-0.779779,9.460310,-2.673610,-9.114544,1.658754,6.224749,-2.274290,-3.040512,2.037603,-6.072086,9.650276,-3.267974,4.939507,-4.388580,1.187352,6.989706,3.558814,-0.541963,-0.050745,4.746348,3.659059,-7.075454,2.856188,0.818054,2.223147,0.091379,-6.817958,3.362625,-2.990378,3.235545,-2.093315,2.595138,7.176275,8.155209,-6.579292,5.379895,4.102325,5.210179,9.483070,-5.062566,5.882245,9.350969,0.114613,3.125168,-3.509950,7.258801,-8.589416,-0.772214,-4.980841,9.623683,2.013460,-9.691600,-3.742730,6.554136,-1.891415,9.799405,0.344556,5.940425,1.107148,-7.556063,9.481134,-1.269679,1.804203,-0.739626,-6.890446,-0.827102,-5.370536,-4.151845,6.146500,-5.262687,5.642113,9.469089,8.966818,1.052053,8.534015,-9.425247,9.632959,-9.525497,-7.672733,-2.115819,4.221796,-2.552424,-2.670786,-4.436720,-7.159111,3.843222,-1.983225,-4.389397,-1.109152,-5.371062,-1.304796,-9.840020,6.125225,-2.150225,8.140902,-8.187892,0.507216,1.962409,-8.674623,5.309368,-2.002881,-1.601188,2.426612,-7.692095,4.603249,-3.957423,-0.390414,2.317352,3.324574,3.522029,0.606873,1.238765,-5.132367,-8.620434,5.318652,4.392292,-7.759718,-9.261578,-9.857975,6.875684,-0.051523,3.082952,2.686609,-9.882817,-9.250416,7.199251,-7.228578,1.706282,9.684232,5.943290,3.290640,3.025067,-0.261934,-1.030605,-2.558342,-0.489633,0.777889,3.227270,4.613617,2.787637,9.906855,6.372736,-3.200750,-6.891211,-1.542744,-8.912162,-2.436317,3.146871,9.239073,-8.027451,-9.825128,-8.414999,-9.857379,-8.636144,-3.994212,-7.310825,-1.780514,0.829507,-8.030089,5.378227,4.742345,-2.681850,6.327427,-0.167295,1.331101,-9.829100,-9.944643,0.739755,9.287111,-6.968269,-8.936233,0.942758,-1.675389,7.389356,3.473969,0.318667,-9.691703,-5.436506,7.799658,-5.779255,1.806306,-5.203227,-1.921172,8.646472,4.268552,2.873984,-5.572253,5.050871,2.847427,8.924675,2.020686,1.243945,-6.071099,4.743065,-1.399242,5.130490,-3.900393,8.236553,8.896327,-6.651403,-2.315758,-3.537711,4.558874,2.823106,-7.646641,9.575189,4.094705,8.654789,-9.942795,-7.254805,7.147278,3.520735,2.274675,-8.002785,1.284504,-9.859207,-9.621927,-4.486366,-5.903989,-6.315524,-3.291774,-3.453896,-6.737125,8.560954,-7.543257,3.123868,8.096309,9.977492,-1.238305,-6.977425,6.559962,8.695774,1.543655,7.431135,-1.251060,6.756928,7.840142,-2.632713,4.934602,-9.642417,2.656758,5.232735,-5.994234,-0.597227,-5.831701,-4.996558,4.742343,8.854891,9.059195,-0.955380,-3.343863,-7.529972,8.348577,6.500776,2.096048,-0.039632,-6.511638,7.471241,-7.538625,6.490086,-5.251200,-0.279676,0.593491,4.728104,-6.132467,-1.395794,5.182058,-2.767880,-0.589530,3.275463,-9.289497,-2.853027,-6.568647,3.589052,9.132891,3.527738,5.362123,0.470213,-3.023031,7.249378,-9.050779,5.956764,1.804063,-8.880155,-1.457120,2.157057,5.084443,6.028167,4.258699,0.951660,8.632696,4.872088,-5.881377,7.573801,1.726085,-1.504125,0.544860,0.861663,5.212426,-6.571942,2.182966,-9.683104,8.778193,-9.831319,7.977882,-8.457431,1.606015,6.598136,-0.292177,-5.625461,6.530217,-4.901155,-7.638592,6.350971,6.201871,2.258322,0.813516,-0.703014,8.181370,-9.871119,-5.586789,8.066541,-4.586414,5.756515,-3.966000,-8.518059,-5.668014,-3.582851,-0.648648,2.012463,3.188194,-5.748345,-8.293952,3.066440,-8.113501,-2.713755,-2.091402,-5.256151,-6.310281,-1.141669,9.638321,3.438032,5.216969,-2.628462,8.085996,9.527371,4.652760,-8.374877,-1.344773,5.359978,2.324115,8.500981,-5.253808,-6.402745,-2.383269,4.051830,3.595852,5.173940,-9.677460,-6.849582,3.102990,-1.109899,6.959022,5.038255,-2.462571,-8.745843,-6.770966,-4.664347,8.571216,-3.152863,3.090184,9.429627,-0.447228,1.344090,7.365150,-6.357030,5.817746,4.999520,3.874811,3.299797,5.232888,6.754501,3.568620,-8.557286,-0.993409,-0.548598,-9.086600,-3.564739,5.274908,3.658170,4.745720,9.559855,-8.632160,-9.567397,3.088743,-0.864474,2.341363,1.287049,3.456767,-6.496164,-5.819195,3.661395,-7.581923,5.158042,3.901152,-0.913490,-1.001913,5.026212,-1.900993,7.454403,7.515243,1.078885,6.472133,-3.053832,-0.620017,0.828243,0.358147,-1.815056], dtype = "float64")#candidate|460|(480,)|const|float64
call_459 = relay.TupleGetItem(func_133_call(relay.reshape(const_460.astype('float64'), [12, 5, 8]), relay.reshape(const_460.astype('float64'), [12, 5, 8]), ), 0)
call_461 = relay.TupleGetItem(func_136_call(relay.reshape(const_460.astype('float64'), [12, 5, 8]), relay.reshape(const_460.astype('float64'), [12, 5, 8]), ), 0)
func_358_call = mod.get_global_var('func_358')
func_361_call = mutated_mod.get_global_var('func_361')
call_462 = relay.TupleGetItem(func_358_call(relay.reshape(call_459.astype('float64'), [480,])), 2)
call_463 = relay.TupleGetItem(func_361_call(relay.reshape(call_459.astype('float64'), [480,])), 2)
output = relay.Tuple([bop_399,bop_447,bop_455,call_459,const_460,call_462,])
output2 = relay.Tuple([bop_402,bop_450,bop_458,call_461,const_460,call_463,])
func_478 = relay.Function([var_398,var_410,], output)
mod['func_478'] = func_478
mod = relay.transform.InferType()(mod)
var_479 = relay.var("var_479", dtype = "float32", shape = (12, 2, 7))#candidate|479|(12, 2, 7)|var|float32
var_480 = relay.var("var_480", dtype = "uint8", shape = (416,))#candidate|480|(416,)|var|uint8
output = func_478(var_479,var_480,)
func_481 = relay.Function([var_479,var_480,], output)
mutated_mod['func_481'] = func_481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_483 = relay.var("var_483", dtype = "float32", shape = (16, 16, 1))#candidate|483|(16, 16, 1)|var|float32
uop_484 = relay.sigmoid(var_483.astype('float32')) # shape=(16, 16, 1)
bop_486 = relay.minimum(uop_484.astype('uint8'), relay.reshape(var_483.astype('uint8'), relay.shape_of(uop_484))) # shape=(16, 16, 1)
uop_498 = relay.acos(bop_486.astype('float32')) # shape=(16, 16, 1)
bop_510 = relay.equal(uop_498.astype('bool'), relay.reshape(uop_484.astype('bool'), relay.shape_of(uop_498))) # shape=(16, 16, 1)
output = bop_510
output2 = bop_510
func_517 = relay.Function([var_483,], output)
mod['func_517'] = func_517
mod = relay.transform.InferType()(mod)
mutated_mod['func_517'] = func_517
mutated_mod = relay.transform.InferType()(mutated_mod)
var_518 = relay.var("var_518", dtype = "float32", shape = (16, 16, 1))#candidate|518|(16, 16, 1)|var|float32
func_517_call = mutated_mod.get_global_var('func_517')
call_519 = func_517_call(var_518)
output = call_519
func_520 = relay.Function([var_518], output)
mutated_mod['func_520'] = func_520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_573 = func_318_call()
call_574 = func_318_call()
func_478_call = mod.get_global_var('func_478')
func_481_call = mutated_mod.get_global_var('func_481')
var_576 = relay.var("var_576", dtype = "uint8", shape = (1, 416))#candidate|576|(1, 416)|var|uint8
call_575 = relay.TupleGetItem(func_478_call(relay.reshape(call_573.astype('float32'), [12, 2, 7]), relay.reshape(var_576.astype('uint8'), [416,]), ), 5)
call_577 = relay.TupleGetItem(func_481_call(relay.reshape(call_573.astype('float32'), [12, 2, 7]), relay.reshape(var_576.astype('uint8'), [416,]), ), 5)
var_578 = relay.var("var_578", dtype = "uint8", shape = (11, 416))#candidate|578|(11, 416)|var|uint8
bop_579 = relay.logical_and(var_576.astype('bool'), var_578.astype('bool')) # shape=(11, 416)
const_587 = relay.const([[True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True],[False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True],[True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,True],[True,False,True,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True],[False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,False,True,True,True],[False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False],[True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,True,False,False,False],[True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False],[False,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False],[True,True,False,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True],[False,True,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,False,True,True,True,True,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True]], dtype = "bool")#candidate|587|(11, 416)|const|bool
bop_588 = relay.bitwise_xor(bop_579.astype('int8'), relay.reshape(const_587.astype('int8'), relay.shape_of(bop_579))) # shape=(11, 416)
func_517_call = mod.get_global_var('func_517')
func_520_call = mutated_mod.get_global_var('func_520')
var_593 = relay.var("var_593", dtype = "float32", shape = (128, 2))#candidate|593|(128, 2)|var|float32
call_592 = func_517_call(relay.reshape(var_593.astype('float32'), [16, 16, 1]))
call_594 = func_517_call(relay.reshape(var_593.astype('float32'), [16, 16, 1]))
func_133_call = mod.get_global_var('func_133')
func_136_call = mutated_mod.get_global_var('func_136')
call_595 = relay.TupleGetItem(func_133_call(relay.reshape(call_575.astype('float64'), [12, 5, 8]), relay.reshape(call_575.astype('float64'), [12, 5, 8]), ), 0)
call_596 = relay.TupleGetItem(func_136_call(relay.reshape(call_575.astype('float64'), [12, 5, 8]), relay.reshape(call_575.astype('float64'), [12, 5, 8]), ), 0)
uop_604 = relay.acos(var_576.astype('float64')) # shape=(1, 416)
func_517_call = mod.get_global_var('func_517')
func_520_call = mutated_mod.get_global_var('func_520')
call_606 = func_517_call(relay.reshape(var_593.astype('float32'), [16, 16, 1]))
call_607 = func_517_call(relay.reshape(var_593.astype('float32'), [16, 16, 1]))
output = relay.Tuple([call_573,call_575,bop_588,call_592,var_593,call_595,uop_604,call_606,])
output2 = relay.Tuple([call_574,call_577,bop_588,call_594,var_593,call_596,uop_604,call_607,])
func_609 = relay.Function([var_576,var_578,var_593,], output)
mod['func_609'] = func_609
mod = relay.transform.InferType()(mod)
mutated_mod['func_609'] = func_609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mutated_mod.get_global_var('func_609')
var_611 = relay.var("var_611", dtype = "uint8", shape = (1, 416))#candidate|611|(1, 416)|var|uint8
var_612 = relay.var("var_612", dtype = "uint8", shape = (11, 416))#candidate|612|(11, 416)|var|uint8
var_613 = relay.var("var_613", dtype = "float32", shape = (128, 2))#candidate|613|(128, 2)|var|float32
call_610 = func_609_call(var_611,var_612,var_613,)
output = call_610
func_614 = relay.Function([var_611,var_612,var_613,], output)
mutated_mod['func_614'] = func_614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_658 = func_318_call()
call_659 = func_318_call()
func_517_call = mod.get_global_var('func_517')
func_520_call = mutated_mod.get_global_var('func_520')
var_665 = relay.var("var_665", dtype = "float32", shape = (256,))#candidate|665|(256,)|var|float32
call_664 = func_517_call(relay.reshape(var_665.astype('float32'), [16, 16, 1]))
call_666 = func_517_call(relay.reshape(var_665.astype('float32'), [16, 16, 1]))
output = relay.Tuple([call_658,call_664,var_665,])
output2 = relay.Tuple([call_659,call_666,var_665,])
func_667 = relay.Function([var_665,], output)
mod['func_667'] = func_667
mod = relay.transform.InferType()(mod)
mutated_mod['func_667'] = func_667
mutated_mod = relay.transform.InferType()(mutated_mod)
var_668 = relay.var("var_668", dtype = "float32", shape = (256,))#candidate|668|(256,)|var|float32
func_667_call = mutated_mod.get_global_var('func_667')
call_669 = func_667_call(var_668)
output = call_669
func_670 = relay.Function([var_668], output)
mutated_mod['func_670'] = func_670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_699 = func_318_call()
call_700 = func_318_call()
uop_726 = relay.sinh(call_699.astype('float32')) # shape=(12, 2, 7)
uop_728 = relay.sinh(call_700.astype('float32')) # shape=(12, 2, 7)
uop_749 = relay.erf(uop_726.astype('float64')) # shape=(12, 2, 7)
uop_751 = relay.erf(uop_728.astype('float64')) # shape=(12, 2, 7)
uop_758 = relay.exp(uop_749.astype('float32')) # shape=(12, 2, 7)
uop_760 = relay.exp(uop_751.astype('float32')) # shape=(12, 2, 7)
func_77_call = mod.get_global_var('func_77')
func_81_call = mutated_mod.get_global_var('func_81')
const_779 = relay.const([4,2,1,1,-2,10,-2,2,10,1,-4,-7,8,-6,-3,-3,6,-9,7,-4,-6,-1,-7,-6,-6,6,1,-8,7,-3,-6,9,4,-8,-10,10,-9,4,3,-4,6,10,3,-6,10,5,8,10,6,2,10,-1,2,-8,7,5,-4,-3,-3,-9,8,10,10,9,6,1,3,9,-9,-4,3,-10,-4,-3,-1,9,8,5,-9,-5,6,-5,10,-8,-2,-5,-10,1,-9,-1,9,-10,-1,-7,1,-5,10,8,5,8,10,2,2,4,-8,-2,6,5,10,6,-6,10,3,7,-6,5,10,-6,1,-4,6,5,9,-9,-2,2,-8,-7,10,8,8,-2,1,3,-1,-10,-2,-10,6,1,6,7,6,6,-7,4,10,-6,-5,2,5,-2,8,9,3,2,-5,-5,3,7,-10,5,-6,-10,7,6,5,-8,-9,-4,1,2,-5,7,8,5,-4,7,-1,-2,10,-2,-3,5,9,4,5,6,-3,-7,-8,1,5,3,-7,-4,-2,-10,-9,8,-6,10,8,-1,-10,2,-1,1,2,-1,10,4,4,-6,2,-2,8,-10,-7,-7,-9,4,-3,5,-10,4,4,9,-3,8,3,-4,2,-7,-4,8,7,-5,-9,-8,9,-7,10,-10,5,8,7,-8,5,10,2,-5,9,9,-4,-5,1,-5,-9,3,2,1,3,-10,5,-8,-7,-5,-4,-2,-3,1,-10,4,3,5,-1,7,-6,-2,9,9,6,-10,-10,9,1,9,8,3,1,9,4,5,4,-4,-9,9,-7,-6,-3,-10,6,-8,-3,6,-8,-7,10,6,-1,-7,1,6,6,3,-8,6,4,-6,6,2,-6,8,-1,10,-5,2,6,4,-3,-3,-1,3,-6,4,-3,-6,7,7,-8,-2,7,-9,-4,-4,9,8,-8,-7,1,4,2,-5,4,7,-10,-7,2,9,-8,-5,-10,-6,1,3,-9,-8,-9,-7,6,6,-4,-4,-8,4,-3,2,-9,2,-6,-6,1,3,8,4,-8,1,-5,10,-5,9,3,-3,-2,4,1,-2,-3,-4,-8,4,-9,8,9,7,-2,6,-10,8,6,-9,-2,-9,7,-8], dtype = "uint8")#candidate|779|(416,)|const|uint8
call_778 = func_77_call(relay.reshape(const_779.astype('uint8'), [8, 13, 4]), relay.reshape(const_779.astype('uint8'), [8, 13, 4]), )
call_780 = func_77_call(relay.reshape(const_779.astype('uint8'), [8, 13, 4]), relay.reshape(const_779.astype('uint8'), [8, 13, 4]), )
output = relay.Tuple([uop_758,call_778,const_779,])
output2 = relay.Tuple([uop_760,call_780,const_779,])
func_782 = relay.Function([], output)
mod['func_782'] = func_782
mod = relay.transform.InferType()(mod)
output = func_782()
func_783 = relay.Function([], output)
mutated_mod['func_783'] = func_783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_794 = relay.TupleGetItem(func_782_call(), 1)
call_795 = relay.TupleGetItem(func_783_call(), 1)
output = relay.Tuple([call_794,])
output2 = relay.Tuple([call_795,])
func_800 = relay.Function([], output)
mod['func_800'] = func_800
mod = relay.transform.InferType()(mod)
output = func_800()
func_801 = relay.Function([], output)
mutated_mod['func_801'] = func_801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_800_call = mod.get_global_var('func_800')
func_801_call = mutated_mod.get_global_var('func_801')
call_929 = relay.TupleGetItem(func_800_call(), 0)
call_930 = relay.TupleGetItem(func_801_call(), 0)
uop_944 = relay.exp(call_929.astype('float64')) # shape=(8, 13, 4)
uop_946 = relay.exp(call_930.astype('float64')) # shape=(8, 13, 4)
func_358_call = mod.get_global_var('func_358')
func_361_call = mutated_mod.get_global_var('func_361')
var_958 = relay.var("var_958", dtype = "float64", shape = (1, 480))#candidate|958|(1, 480)|var|float64
call_957 = relay.TupleGetItem(func_358_call(relay.reshape(var_958.astype('float64'), [480,])), 3)
call_959 = relay.TupleGetItem(func_361_call(relay.reshape(var_958.astype('float64'), [480,])), 3)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_975 = relay.TupleGetItem(func_782_call(), 0)
call_976 = relay.TupleGetItem(func_783_call(), 0)
uop_982 = relay.log(uop_944.astype('float32')) # shape=(8, 13, 4)
uop_984 = relay.log(uop_946.astype('float32')) # shape=(8, 13, 4)
var_986 = relay.var("var_986", dtype = "float32", shape = (8, 13, 4))#candidate|986|(8, 13, 4)|var|float32
bop_987 = relay.subtract(uop_982.astype('int32'), relay.reshape(var_986.astype('int32'), relay.shape_of(uop_982))) # shape=(8, 13, 4)
bop_990 = relay.subtract(uop_984.astype('int32'), relay.reshape(var_986.astype('int32'), relay.shape_of(uop_984))) # shape=(8, 13, 4)
output = relay.Tuple([call_957,var_958,call_975,bop_987,])
output2 = relay.Tuple([call_959,var_958,call_976,bop_990,])
func_1001 = relay.Function([var_958,var_986,], output)
mod['func_1001'] = func_1001
mod = relay.transform.InferType()(mod)
var_1002 = relay.var("var_1002", dtype = "float64", shape = (1, 480))#candidate|1002|(1, 480)|var|float64
var_1003 = relay.var("var_1003", dtype = "float32", shape = (8, 13, 4))#candidate|1003|(8, 13, 4)|var|float32
output = func_1001(var_1002,var_1003,)
func_1004 = relay.Function([var_1002,var_1003,], output)
mutated_mod['func_1004'] = func_1004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_1026 = func_318_call()
call_1027 = func_318_call()
output = relay.Tuple([call_1026,])
output2 = relay.Tuple([call_1027,])
func_1029 = relay.Function([], output)
mod['func_1029'] = func_1029
mod = relay.transform.InferType()(mod)
mutated_mod['func_1029'] = func_1029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mutated_mod.get_global_var('func_1029')
call_1030 = func_1029_call()
output = call_1030
func_1031 = relay.Function([], output)
mutated_mod['func_1031'] = func_1031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_1048 = relay.TupleGetItem(func_348_call(), 0)
call_1049 = relay.TupleGetItem(func_349_call(), 0)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_1050 = relay.TupleGetItem(func_348_call(), 0)
call_1051 = relay.TupleGetItem(func_349_call(), 0)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1054 = relay.TupleGetItem(func_1029_call(), 0)
call_1055 = relay.TupleGetItem(func_1031_call(), 0)
output = relay.Tuple([call_1048,call_1050,call_1054,])
output2 = relay.Tuple([call_1049,call_1051,call_1055,])
func_1075 = relay.Function([], output)
mod['func_1075'] = func_1075
mod = relay.transform.InferType()(mod)
output = func_1075()
func_1076 = relay.Function([], output)
mutated_mod['func_1076'] = func_1076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1090 = relay.TupleGetItem(func_1029_call(), 0)
call_1091 = relay.TupleGetItem(func_1031_call(), 0)
uop_1100 = relay.sin(call_1090.astype('float64')) # shape=(12, 2, 7)
uop_1102 = relay.sin(call_1091.astype('float64')) # shape=(12, 2, 7)
func_667_call = mod.get_global_var('func_667')
func_670_call = mutated_mod.get_global_var('func_670')
var_1104 = relay.var("var_1104", dtype = "float32", shape = (4, 64))#candidate|1104|(4, 64)|var|float32
call_1103 = relay.TupleGetItem(func_667_call(relay.reshape(var_1104.astype('float32'), [256,])), 1)
call_1105 = relay.TupleGetItem(func_670_call(relay.reshape(var_1104.astype('float32'), [256,])), 1)
uop_1109 = relay.rsqrt(var_1104.astype('float64')) # shape=(4, 64)
output = relay.Tuple([uop_1100,call_1103,uop_1109,])
output2 = relay.Tuple([uop_1102,call_1105,uop_1109,])
func_1114 = relay.Function([var_1104,], output)
mod['func_1114'] = func_1114
mod = relay.transform.InferType()(mod)
mutated_mod['func_1114'] = func_1114
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1115 = relay.var("var_1115", dtype = "float32", shape = (4, 64))#candidate|1115|(4, 64)|var|float32
func_1114_call = mutated_mod.get_global_var('func_1114')
call_1116 = func_1114_call(var_1115)
output = call_1116
func_1117 = relay.Function([var_1115], output)
mutated_mod['func_1117'] = func_1117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_1127 = relay.TupleGetItem(func_348_call(), 0)
call_1128 = relay.TupleGetItem(func_349_call(), 0)
output = call_1127
output2 = call_1128
func_1131 = relay.Function([], output)
mod['func_1131'] = func_1131
mod = relay.transform.InferType()(mod)
mutated_mod['func_1131'] = func_1131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1131_call = mutated_mod.get_global_var('func_1131')
call_1132 = func_1131_call()
output = call_1132
func_1133 = relay.Function([], output)
mutated_mod['func_1133'] = func_1133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_1187 = relay.TupleGetItem(func_1075_call(), 2)
call_1188 = relay.TupleGetItem(func_1076_call(), 2)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_1191 = relay.TupleGetItem(func_348_call(), 1)
call_1192 = relay.TupleGetItem(func_349_call(), 1)
func_1001_call = mod.get_global_var('func_1001')
func_1004_call = mutated_mod.get_global_var('func_1004')
var_1194 = relay.var("var_1194", dtype = "float64", shape = (120, 4))#candidate|1194|(120, 4)|var|float64
var_1195 = relay.var("var_1195", dtype = "float32", shape = (416,))#candidate|1195|(416,)|var|float32
call_1193 = relay.TupleGetItem(func_1001_call(relay.reshape(var_1194.astype('float64'), [1, 480]), relay.reshape(var_1195.astype('float32'), [8, 13, 4]), ), 2)
call_1196 = relay.TupleGetItem(func_1004_call(relay.reshape(var_1194.astype('float64'), [1, 480]), relay.reshape(var_1195.astype('float32'), [8, 13, 4]), ), 2)
output = relay.Tuple([call_1187,call_1191,call_1193,var_1194,var_1195,])
output2 = relay.Tuple([call_1188,call_1192,call_1196,var_1194,var_1195,])
func_1211 = relay.Function([var_1194,var_1195,], output)
mod['func_1211'] = func_1211
mod = relay.transform.InferType()(mod)
mutated_mod['func_1211'] = func_1211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1211_call = mutated_mod.get_global_var('func_1211')
var_1213 = relay.var("var_1213", dtype = "float64", shape = (120, 4))#candidate|1213|(120, 4)|var|float64
var_1214 = relay.var("var_1214", dtype = "float32", shape = (416,))#candidate|1214|(416,)|var|float32
call_1212 = func_1211_call(var_1213,var_1214,)
output = call_1212
func_1215 = relay.Function([var_1213,var_1214,], output)
mutated_mod['func_1215'] = func_1215
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1245 = relay.var("var_1245", dtype = "uint64", shape = (15, 8, 12))#candidate|1245|(15, 8, 12)|var|uint64
var_1246 = relay.var("var_1246", dtype = "uint64", shape = (15, 8, 12))#candidate|1246|(15, 8, 12)|var|uint64
bop_1247 = relay.bitwise_xor(var_1245.astype('uint64'), relay.reshape(var_1246.astype('uint64'), relay.shape_of(var_1245))) # shape=(15, 8, 12)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_1285 = relay.TupleGetItem(func_782_call(), 1)
call_1286 = relay.TupleGetItem(func_783_call(), 1)
output = relay.Tuple([bop_1247,call_1285,])
output2 = relay.Tuple([bop_1247,call_1286,])
func_1325 = relay.Function([var_1245,var_1246,], output)
mod['func_1325'] = func_1325
mod = relay.transform.InferType()(mod)
mutated_mod['func_1325'] = func_1325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1325_call = mutated_mod.get_global_var('func_1325')
var_1327 = relay.var("var_1327", dtype = "uint64", shape = (15, 8, 12))#candidate|1327|(15, 8, 12)|var|uint64
var_1328 = relay.var("var_1328", dtype = "uint64", shape = (15, 8, 12))#candidate|1328|(15, 8, 12)|var|uint64
call_1326 = func_1325_call(var_1327,var_1328,)
output = call_1326
func_1329 = relay.Function([var_1327,var_1328,], output)
mutated_mod['func_1329'] = func_1329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_1379 = relay.TupleGetItem(func_1075_call(), 0)
call_1380 = relay.TupleGetItem(func_1076_call(), 0)
output = call_1379
output2 = call_1380
func_1381 = relay.Function([], output)
mod['func_1381'] = func_1381
mod = relay.transform.InferType()(mod)
mutated_mod['func_1381'] = func_1381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1381_call = mutated_mod.get_global_var('func_1381')
call_1382 = func_1381_call()
output = call_1382
func_1383 = relay.Function([], output)
mutated_mod['func_1383'] = func_1383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_800_call = mod.get_global_var('func_800')
func_801_call = mutated_mod.get_global_var('func_801')
call_1399 = relay.TupleGetItem(func_800_call(), 0)
call_1400 = relay.TupleGetItem(func_801_call(), 0)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_1401 = relay.TupleGetItem(func_782_call(), 0)
call_1402 = relay.TupleGetItem(func_783_call(), 0)
const_1415 = relay.const([[[5,8,-6,1],[8,5,-5,6],[4,-10,10,-8],[-4,8,5,5],[-9,-4,-5,-8],[8,-5,-6,8],[-2,-10,-4,-1],[3,6,-5,-10],[5,9,10,5],[1,-3,-10,-7],[-1,7,9,-2],[9,-2,8,-7],[5,-4,-3,3]],[[10,-1,8,3],[8,3,-9,-10],[4,3,2,-6],[7,-2,-1,-4],[-2,1,6,-1],[5,-2,10,5],[3,-7,-9,4],[5,6,-2,6],[9,5,-1,-10],[10,-3,3,6],[7,9,-10,-1],[10,2,-2,-7],[8,-6,10,-7]],[[7,3,-9,4],[-6,-1,-7,-1],[2,10,-4,6],[-10,-2,8,3],[3,-3,-6,-10],[9,9,6,4],[3,-3,-10,-2],[-1,3,6,-3],[1,-3,3,9],[5,-10,8,-8],[-8,2,9,-10],[-8,8,-10,-5],[8,-10,-1,5]],[[-9,-6,8,9],[-4,6,5,-4],[3,-9,4,4],[1,-3,4,-8],[-2,7,-8,-8],[7,10,3,5],[7,-7,-7,4],[-6,2,-6,1],[7,-10,6,9],[-3,3,2,-10],[-1,1,1,-6],[2,-4,-10,-6],[5,-2,-3,4]],[[2,2,5,-5],[2,-4,1,7],[-2,4,10,-9],[-8,-5,3,-7],[-7,1,4,10],[-1,-6,-8,8],[5,-10,-1,-1],[-1,10,-8,-1],[9,-8,-5,6],[5,-8,4,-1],[-5,-8,-1,7],[-5,-5,5,7],[7,6,4,-8]],[[3,-9,2,-10],[10,-5,-6,2],[1,-6,5,-2],[-9,-4,10,3],[8,2,4,8],[9,7,-8,-9],[-8,7,6,-4],[8,1,2,3],[8,9,-7,-7],[10,4,-5,-7],[5,4,3,-10],[8,1,5,-9],[7,-6,6,-3]],[[-7,6,-9,5],[-9,5,9,-3],[7,8,-7,-5],[-8,1,4,4],[-2,-3,5,4],[7,6,-5,4],[4,-3,10,7],[1,-3,3,-6],[8,-7,9,7],[-1,3,-5,-7],[10,1,-2,-7],[-8,9,8,8],[7,8,-7,2]],[[-1,3,2,6],[1,-2,-6,7],[-1,-5,2,-4],[-9,6,9,-3],[3,-6,-5,6],[8,1,1,7],[-4,3,-6,-8],[-3,-2,-2,-3],[-10,-1,1,-2],[-9,4,5,-4],[-6,7,-5,-8],[9,1,2,8],[4,6,9,6]]], dtype = "uint8")#candidate|1415|(8, 13, 4)|const|uint8
bop_1416 = relay.logical_and(call_1399.astype('bool'), relay.reshape(const_1415.astype('bool'), relay.shape_of(call_1399))) # shape=(8, 13, 4)
bop_1419 = relay.logical_and(call_1400.astype('bool'), relay.reshape(const_1415.astype('bool'), relay.shape_of(call_1400))) # shape=(8, 13, 4)
func_1131_call = mod.get_global_var('func_1131')
func_1133_call = mutated_mod.get_global_var('func_1133')
call_1420 = func_1131_call()
call_1421 = func_1131_call()
output = relay.Tuple([call_1401,bop_1416,call_1420,])
output2 = relay.Tuple([call_1402,bop_1419,call_1421,])
func_1426 = relay.Function([], output)
mod['func_1426'] = func_1426
mod = relay.transform.InferType()(mod)
mutated_mod['func_1426'] = func_1426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mutated_mod.get_global_var('func_1426')
call_1427 = func_1426_call()
output = call_1427
func_1428 = relay.Function([], output)
mutated_mod['func_1428'] = func_1428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1429 = relay.TupleGetItem(func_1029_call(), 0)
call_1430 = relay.TupleGetItem(func_1031_call(), 0)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_1443 = func_318_call()
call_1444 = func_318_call()
func_609_call = mod.get_global_var('func_609')
func_614_call = mutated_mod.get_global_var('func_614')
var_1451 = relay.var("var_1451", dtype = "uint8", shape = (416,))#candidate|1451|(416,)|var|uint8
const_1452 = relay.const([7,-10,-2,-4,-7,1,-1,3,-1,7,-3,5,-6,7,6,-3,-3,7,-5,6,-5,-3,-3,-8,-7,6,-8,3,-4,1,-2,2,9,-3,-2,6,3,-4,8,-1,-10,3,7,-1,-6,-10,-9,4,-4,2,-5,1,-10,6,-8,-10,-5,-6,1,-5,2,-5,-10,10,-7,7,-1,-10,7,8,5,4,1,4,9,-8,5,-3,4,10,-6,-3,-7,-7,-3,10,10,-7,3,-4,-1,5,-8,2,2,3,-8,2,-3,10,3,-3,-5,6,2,-2,2,10,6,2,-5,-3,-5,-10,3,4,1,8,8,4,4,4,3,-6,7,4,-6,6,-3,10,8,1,1,-7,-5,-8,7,5,-7,9,-2,9,2,-9,-4,1,3,3,-5,-3,-3,9,5,2,-6,10,-5,-4,-6,2,-2,-2,-6,8,-7,-10,-4,-10,3,-4,4,7,-5,-6,5,-1,-2,-3,1,-8,4,9,-8,-8,-3,-2,-8,-4,-3,6,-10,-7,1,9,-3,2,-8,5,10,-9,-6,9,1,9,-6,3,1,8,-10,-5,7,-10,8,1,9,-4,2,-8,-9,-8,-1,2,-1,-5,-1,-3,10,3,9,10,5,-2,7,9,-9,10,-8,-2,-5,9,9,-4,5,1,-5,-1,-4,7,-5,7,5,-3,-10,-1,4,-10,-2,-4,-4,-1,7,-9,-7,2,7,3,5,-7,3,-9,-8,1,-5,-8,-1,10,-3,7,-7,9,8,-6,-1,9,2,10,9,1,6,7,-10,-5,5,-2,-3,-8,4,6,-6,-9,5,8,1,-1,1,-6,4,4,5,4,7,-1,-6,6,1,2,-5,1,-2,-2,-10,-3,-10,-4,5,3,9,-4,-2,-7,-8,-1,1,-6,6,-5,-6,1,-9,1,2,-5,9,-6,-2,5,3,-10,10,7,-5,10,-5,7,5,-8,-3,8,4,4,8,-3,-5,-5,-10,9,-7,9,2,-7,-6,-6,10,3,-1,-10,-8,1,-6,8,-1,3,10,1,8,2,5,-2,-3,8,4,2,1,-5,2,-4,2,4,-7,-7,4,-8,-7,-1,5,-4,-7,1,2,4,-1,8,6,-7,-6,10,2,-9,10,9,9,-6,-2,6,-3,1,-9,-9,-2,9,-1,-7,9,-3,-6,-4,-8,3,9,5,10,-6,-6,5,3,5,7,8,10,4,-4,2,1,3,3,-2,5,-3,6,8,-5,1,4,7,1,-9,4,-8,-7,6,10,-4,-9,5,-6,-3,5,-3,5,5,5,-2,7,5,10,3,-1,-4,-5,-6,-3,4,-4,7,8,5,7,-2,7,6,1,9,8,2,4,6,6,-3,6,-10,-3,-10,4,3,-1,1,10,-2,3,4,2,5,2,8,10,-6,7,-3,8,-4,-7,-1,-5,9,-8,5,5,-8,8,6,-8,-2,8,5,3,7,2,-9,2,5,1,10,8,4,7,-5,-2,-7,-2,8,-10,7,2,1,6,-4,5,-4,5,10,-9,5,2,4,4,3,-5,-8,-8,1,-2,-10,2,-10,1,-8,-7,-2,5,-6,7,3,-10,9,9,-2,8,9,-6,-8,1,7,-1,8,6,6,-3,-5,1,1,-7,-2,2,6,10,-7,2,-10,5,-10,2,-6,7,6,-9,-10,9,-1,3,1,1,-4,-1,5,-2,9,-1,9,-8,7,-3,2,-9,4,-10,5,2,6,6,9,8,-4,-5,-8,9,10,4,-5,-7,-5,4,2,-3,-9,-10,9,-8,-9,-7,6,2,-9,10,-9,2,3,6,-4,-4,10,-3,3,3,4,9,-7,8,7,-1,-2,-10,1,-2,7,-5,-3,-5,10,8,-1,8,8,-5,3,-9,8,-1,7,1,-3,-2,-7,-3,-6,-4,8,4,-7,8,4,-4,9,3,-1,2,5,10,-1,-10,4,4,8,-5,-7,-5,-10,-7,-6,-5,-7,1,-10,-3,-4,6,8,7,7,1,6,-7,4,-7,4,-7,10,-10,-1,-9,-7,10,-6,1,10,9,7,2,10,4,-3,5,-1,2,-10,-6,10,2,2,9,-5,-5,4,6,9,8,-4,-5,-9,-6,10,6,7,-5,-1,-10,5,-1,-5,5,-8,5,-7,7,-9,-5,-7,8,8,3,-10,-8,-8,-5,5,-6,2,-2,-2,-5,4,-10,10,4,-3,-9,-10,7,-5,3,-2,-2,-10,5,5,-5,-9,-1,4,9,4,2,5,4,-4,10,5,2,6,1,7,-2,2,-9,9,-6,8,-9,-9,-4,1,1,-4,3,-2,3,10,-8,-9,9,-7,-10,-4,7,-3,8,-5,-2,-4,2,9,5,-1,10,-2,-7,-3,-5,8,-10,-4,-7,-9,-9,1,-1,7,10,1,-7,10,-3,10,9,1,-9,2,-4,-2,-6,-2,-5,-2,-6,-6,7,4,-8,7,2,-9,-3,-6,1,-9,3,3,2,-5,-8,1,7,-5,-4,4,-2,-7,-3,-3,-1,3,-8,3,2,10,9,5,-1,-2,-5,-10,-9,-4,-2,-9,1,-8,-8,3,-1,2,-6,-7,-9,3,3,-1,-2,7,1,-8,7,5,9,7,-1,-9,6,-8,-4,9,6,-2,-4,-2,-2,-1,-6,-4,4,-4,-10,6,6,-3,4,-10,3,-9,-10,3,-3,2,-3,-6,-10,4,1,8,-5,-10,4,-9,1,-1,1,4,10,-3,2,2,10,-4,7,10,2,10,1,2,-9,2,8,-6,-10,3,-10,6,2,-1,-1,-10,-3,10,2,-4,4,3,-2,2,9,7,-4,-9,4,-7,1,9,-8,5,-2,2,-7,-8,3,-4,-9,10,-4,10,-9,3,4,5,5,-3,3,1,-8,10,2,4,4,5,-4,-6,-1,4,-4,-7,-1,4,-6,3,-7,-7,-6,10,-6,-8,9,-3,6,6,-6,-7,-5,-10,-7,9,5,-10,-7,-1,-7,-3,-6,9,-4,1,9,-9,-10,-7,2,-8,-2,-8,-3,3,-9,-6,-3,-6,-9,-10,-5,-5,10,2,10,8,10,-4,-8,-5,-5,1,-8,-6,-4,-7,7,-3,-6,8,-5,-1,-4,-2,-1,-9,-7,-6,-9,-2,-1,5,-1,-3,-3,6,-9,7,-1,6,-3,8,-9,-5,-9,3,-5,7,7,6,3,2,-8,-5,-5,9,-8,-9,3,7,-2,1,-9,7,10,-9,-5,5,7,10,-3,-3,-8,-9,-8,-5,7,10,-6,-3,8,9,3,5,-6,-6,-6,1,3,8,-6,-4,1,-10,-8,-5,-7,10,-2,3,-3,-6,-10,-4,-9,-6,5,2,1,5,7,8,8,-7,6,-6,-1,-6,3,5,2,9,-1,-3,2,-6,2,4,-3,-8,-1,5,-1,4,-3,-6,-10,2,7,-8,7,-10,5,9,-5,6,-5,7,-6,-8,9,5,10,-3,-7,7,-2,-3,3,6,10,3,2,1,-2,-6,4,10,-1,4,5,-1,10,-7,-7,10,-4,-5,2,6,-7,-5,-6,-7,-2,-4,-4,-6,-9,7,4,7,10,-6,-10,-6,-5,-7,8,7,-7,-6,5,5,-5,-2,-10,8,-1,-2,-5,7,1,-10,-10,-10,-7,1,-10,-6,9,-3,6,-6,-6,-7,9,2,8,1,-10,-8,-9,2,3,4,7,10,-1,-10,7,9,-9,-5,4,6,1,2,1,9,2,-6,3,2,-6,-10,-10,-8,9,-8,3,6,6,-2,-3,-10,8,-6,6,4,2,5,-4,-3,-8,5,-4,3,-10,10,-8,8,8,7,-4,8,-7,-8,-3,2,-1,-3,8,9,-9,-1,1,2,-5,-5,-10,-3,-5,-7,-1,10,-8,10,-8,-3,-10,-5,4,-10,8,6,-8,6,9,2,4,3,-6,7,-2,3,5,-10,-7,9,-6,3,3,9,-5,-3,4,1,7,-4,-8,-10,4,5,-10,7,7,-4,-1,4,4,5,1,8,5,6,10,8,6,5,8,-6,2,-7,2,1,9,2,3,10,3,-3,4,6,7,-7,-3,-7,-2,-10,-8,-10,6,-10,3,8,8,10,-3,1,8,-2,-3,-8,7,-9,6,1,3,-4,1,-4,-3,2,-1,-5,-3,1,-10,-2,6,10,-3,5,-4,2,-1,8,-3,10,-3,4,-6,3,4,10,7,2,-5,-5,8,-6,-6,-4,5,2,3,-8,-2,2,6,-8,6,-4,8,1,7,-8,-2,-1,-8,-6,8,9,-5,-6,7,-6,3,-3,9,9,-1,-10,-1,3,3,-2,5,9,-4,-3,-8,-3,8,3,2,-5,1,8,-8,3,2,10,-7,-7,5,-4,-6,-7,-5,-6,-4,-9,-8,-9,8,8,7,5,-9,7,-2,-1,7,5,-8,-6,3,7,2,8,8,-2,-5,9,1,10,-6,-2,-6,-3,-9,7,6,-5,-10,2,10,2,-1,9,-8,5,-9,7,7,2,-2,-10,-2,9,-10,9,5,7,-4,-9,-5,-6,-3,-10,4,-6,8,5,3,-4,-4,-6,4,-4,10,-3,-8,-7,-4,1,8,4,-7,8,2,-4,-4,-3,4,9,9,-6,2,9,-2,-6,10,-6,9,-7,-5,5,-3,-10,-6,-10,-2,3,2,4,10,4,-9,7,6,7,6,3,-10,8,-3,-10,-7,-10,5,-2,-3,-7,7,-8,-9,-4,-7,-6,-9,3,-3,6,-6,-8,2,5,6,-8,7,8,1,3,-3,4,-3,4,10,3,-8,-8,-1,-8,5,4,1,8,-7,1,9,-2,2,8,7,9,-4,-8,10,-6,1,8,3,6,-8,10,2,-2,7,8,5,1,-6,4,4,-2,-9,9,-10,-2,1,10,5,8,3,-7,-5,8,7,7,4,-8,-4,5,-3,-4,10,-8,5,-8,-1,-9,-3,-6,-2,4,4,9,1,2,4,10,10,-10,1,-7,2,7,-4,-6,7,2,-1,9,-6,8,7,-3,-4,-3,-10,-9,6,-8,10,9,-3,9,2,8,7,8,-3,-2,-6,4,-5,8,1,-4,-1,6,-3,-2,1,5,-7,5,-5,-1,-1,-7,-9,8,5,9,-4,-2,10,-2,-5,2,-1,3,3,9,8,8,2,-7,7,-5,-1,-8,2,-3,-6,-10,-3,2,-7,-9,8,-4,5,-9,7,3,-10,8,-10,8,9,4,-1,7,-7,4,-6,-6,-8,-3,-9,-3,-1,9,-6,-7,5,7,8,-3,-2,2,5,-9,5,10,-10,2,-5,-3,8,-8,-3,-10,-8,-10,9,-8,-2,-9,-9,-2,3,-2,-5,-9,-7,9,-1,3,-1,2,6,6,7,6,4,6,-4,-6,-3,5,4,-2,-10,-6,9,-10,-10,-3,-2,2,1,-5,-4,5,8,9,-3,-6,-7,5,-2,1,3,-8,6,-5,8,1,3,-1,-5,2,3,-2,-2,-8,-6,-6,-6,-6,-6,7,-10,-6,-6,3,-9,-1,5,-7,-2,1,6,7,-4,4,3,-4,2,8,-8,9,-8,-2,-4,7,-5,-6,-8,5,-7,1,-2,4,4,-2,-7,-10,3,-5,10,-5,-4,6,-3,5,-9,1,-3,5,-9,10,10,-10,-3,-10,-8,-9,-7,6,7,-1,8,-10,-6,-8,2,10,9,6,4,-6,2,-7,-2,10,-4,8,2,-5,-2,3,3,7,3,6,9,2,-9,2,-3,3,-3,1,10,4,-9,6,-2,5,-8,5,-5,1,-5,7,3,-7,-2,2,4,-4,4,-4,4,-2,-10,-2,-3,1,3,-7,-10,5,-3,-6,4,10,1,-6,3,7,-4,-8,-1,-4,7,-5,8,-10,8,7,-3,1,1,9,5,9,7,6,-8,-6,-4,1,10,2,-5,-1,-8,-6,-2,-4,3,8,-1,-9,7,-4,-6,-4,8,4,8,6,10,4,-5,10,-2,-9,5,1,-5,6,2,8,9,-3,-9,-3,-1,2,-7,-5,3,3,-5,-1,-1,-2,8,-3,3,-3,9,3,5,5,8,-3,5,10,-10,10,7,-4,-3,-1,7,1,10,-5,7,-8,-9,9,-5,-3,7,8,-5,-10,-1,7,5,-5,9,-9,-7,5,-8,-9,-1,-9,6,-4,-10,-1,5,3,3,-4,-6,-3,2,1,2,6,-4,4,2,3,4,7,10,-9,7,-9,10,10,-10,3,-2,-5,-6,8,-9,-2,-3,-2,10,-9,-9,-10,8,1,10,8,-5,-10,-2,-10,9,3,2,6,9,9,-4,4,-10,10,3,3,2,10,4,-4,2,5,-3,8,-8,7,-7,-4,10,-6,-1,-2,4,7,-1,-9,8,-9,-8,-2,-3,8,2,4,5,4,10,-1,7,10,-10,-3,6,-1,6,-1,-4,6,9,7,-1,-2,-6,-5,10,3,8,-10,5,-9,9,-1,-6,-9,8,-1,-7,-9,-5,-8,-2,6,-4,-4,-2,-1,10,-3,10,3,8,-8,-8,-9,-3,-7,7,-5,-4,1,10,6,-7,-8,9,-4,7,3,1,8,1,7,1,-1,10,10,6,-2,4,-10,3,-1,8,-6,8,-10,-1,6,-10,-8,9,-10,5,9,-6,-4,5,-9,-1,-9,-3,9,6,6,2,-6,-4,-9,-10,10,-7,5,2,-4,-3,4,-10,9,-8,-3,1,-3,-8,5,1,6,-10,2,6,-4,7,-6,1,-6,-10,-1,-8,7,-9,6,6,9,-2,7,-5,9,-1,10,10,-2,4,-1,-10,-8,9,-10,-7,-2,-8,-9,1,4,4,-3,9,-5,1,-3,4,-3,-7,-1,-9,-5,1,-9,-1,4,6,-10,-5,6,-2,-10,-4,3,-3,8,-7,-1,5,3,-3,-5,-6,-6,1,8,4,-10,-10,-10,5,-7,10,-3,7,5,2,-1,-5,9,10,7,-5,2,10,-10,-1,1,4,8,-9,1,3,2,-10,3,-8,4,9,-1,-10,-8,-8,2,-1,3,-5,5,-6,-5,-8,6,1,3,6,1,-5,-6,-5,6,1,10,-2,4,-10,4,-1,5,-8,4,-2,-1,1,1,8,-6,7,-6,8,8,-1,7,-1,-4,1,-7,2,-2,-7,-10,2,-7,1,9,3,7,-10,-8,7,1,1,-2,8,-5,-9,-2,-3,2,-10,3,-8,9,-5,10,8,-9,-9,-1,3,2,5,2,2,-3,-5,-8,-7,3,-2,1,4,9,8,-2,8,-4,-7,10,-10,-4,9,10,-6,5,7,10,-5,7,-10,6,-3,8,7,-1,-3,2,6,-6,-6,-2,9,4,-10,-7,10,-8,-4,-4,6,-7,-2,-1,-2,1,-7,1,-5,-10,-6,5,2,8,2,8,9,9,6,-2,-6,-8,-5,9,-6,5,7,7,-3,-5,10,3,9,-3,-9,-5,7,7,4,2,-8,1,4,5,6,-2,-3,6,-6,-9,3,1,-9,9,-8,-5,-5,2,-6,-9,-8,9,-6,5,3,1,10,-5,2,-4,5,7,-6,1,5,-6,-3,-6,1,2,-5,-1,5,-4,10,-9,7,-6,4,-7,-9,4,10,-2,-1,-9,9,1,-6,3,3,10,8,3,5,-5,-4,8,-8,7,7,6,-5,-2,-2,-8,8,6,-6,-10,-10,-5,3,-2,-4,-10,6,6,3,-4,-4,-3,-2,8,10,9,2,-6,-9,-6,7,5,4,-7,-9,3,3,6,4,3,2,6,8,-9,-10,2,-10,3,8,2,-10,3,-2,-9,2,10,4,8,-8,8,1,-9,7,-7,-1,4,-6,5,7,4,-5,-3,-2,10,-9,2,-8,-1,3,2,8,5,5,4,3,-1,-4,-7,7,-8,6,6,-9,1,-6,-5,-8,-10,10,5,2,2,-2,2,-8,8,10,-10,-3,-2,1,-5,10,2,-1,-3,-4,-1,-6,8,5,8,9,6,-6,-1,6,7,-3,-5,-7,9,5,-8,3,5,-9,3,10,8,-8,6,-4,1,4,-2,-6,2,1,4,-5,3,-3,-4,8,10,2,1,9,-3,-9,5,8,-9,-7,-4,-4,-8,5,-2,5,-10,-10,-3,2,1,3,-9,3,-1,-10,7,-3,-3,-9,3,8,9,4,-6,-7,10,-5,2,-6,10,-9,-4,-2,-5,3,-4,-1,9,-4,2,2,-1,2,4,-8,5,-1,-2,-5,3,4,7,10,-1,-10,6,-6,8,-2,-3,7,8,7,1,8,8,-3,7,2,8,10,4,10,-1,4,-1,-4,-7,2,2,3,-1,-8,10,6,-2,1,-2,9,1,9,-2,-4,5,8,3,-1,8,3,-9,-5,5,10,4,1,1,-9,5,4,9,-1,-3,-9,2,-6,-10,6,4,-3,3,6,-3,9,-10,2,-6,4,-5,-10,-4,2,7,9,1,-2,5,-2,-4,-8,5,4,3,1,-10,7,-5,-5,-6,-6,8,3,5,-2,6,5,-10,-3,6,10,-4,7,-5,-4,1,-8,-7,2,6,-4,6,6,-8,-10,2,2,7,5,-4,-3,-10,-3,1,10,-1,-4,4,4,8,8,-2,-5,-10,2,-1,10,-3,-10,-10,6,7,-10,-9,-2,-8,8,-9,-10,-5,-4,5,-10,8,-7,-10,-4,4,-7,8,-3,-8,-8,-3,-7,-9,7,-4,6,-8,-2,7,-5,-10,5,2,6,-8,8,-3,2,-7,-7,7,-4,-8,3,-4,6,1,-6,1,2,6,-3,-6,-10,5,5,-3,-10,9,6,-4,-9,-8,-7,-5,-2,-2,10,1,2,-1,1,7,-7,-5,-8,-9,-3,2,-8,2,9,-7,1,-1,6,-7,8,-8,-10,9,-1,5,-7,-5,-5,7,8,-3,1,-1,7,-4,4,3,-3,2,-3,8,-5,7,10,1,7,7,9,-5,-8,5,-8,-3,-1,5,-1,3,7,-5,-1,5,2,6,-1,-10,-7,-10,3,6,-8,5,-7,7,-6,1,9,-7,-7,4,3,9,-1,5,-10,-8,-5,10,-1,5,9,9,1,1,-9,8,-3,10,-3,7,-7,6,10,-3,2,10,-4,-9,3,3,-7,1,-9,3,7,9,-7,-5,8,-5,8,2,-4,-6,-3,8,1,7,4,4,-9,5,-6,2,2,6,5,-1,1,6,6,3,5,9,-1,9,4,6,8,-5,5,10,1,9,-9,-7,8,4,1,1,4,2,7,7,-7,-8,6,-4,-9,1,7,3,-2,-9,10,-7,-1,2,8,-3,-4,9,9,8,-6,6,-9,-9,7,5,7,4,10,3,-7,-5,7,10,-7,4,9,7,2,-10,3,8,7,7,8,-7,8,6,6,-1,-4,4,-6,3,8,-7,-9,2,-7,-7,-1,-7,-6,4,1,-3,-4,-10,10,10,-7,1,-4,-3,-6,-5,5,-5,7,3,9,-2,-4,3,6,-4,-10,10,-1,-4,-3,3,-3,1,2,-7,-1,-3,-3,-1,-10,1,-3,4,4,-1,9,9,4,1,5,6,8,2,-6,10,1,5,-4,8,-1,9,4,-9,7,6,-7,-1,-4,6,-8,-7,10,1,-5,4,-7,-3,8,-9,3,10,-8,6,-3,-3,9,-10,-1,2,9,1,8,6,5,4,1,-7,2,2,-6,-6,4,-3,-6,-3,3,-2,-8,-9,-4,-1,7,-5,-3,-6,-3,-3,10,-3,5,3,10,10,-4,10,-6,-4,-1,3,9,3,6,8,-4,-2,9,-8,9,-8,1,-10,1,9,6,-7,3,-6,8,5,-4,-2,10,-3,-9,1,-1,6,-8,5,9,8,2,1,7,3,-2,-6,6,-1,-2,-7,-7,6,-10,-1,3,-10,-1,-4,-8,-10,1,-3,5,1,8,2,-3,-3,7,9,-3,-4,2,3,-6,-8,-10,3,-5,-5,-4,-10,-3,-9,9,2,-9,-6,-6,-10,-3,1,-9,1,3,-9,-2,4,-6,-6,3,6,-6,-2,1,-7,10,10,-6,-5,6,8,7,-3,-6,-5,-9,-8,3,-9,4,3,-6,5,-3,-3,-6,-8,2,5,2,-7,-3,8,-7,-4,-3,-6,1,2,-4,4,-7,-3,4,9,10,-9,-2,-10,-3,1,1,-4,-9,-6,-3,-2,-5,-9,7,-6,-3,9,-1,-4,5,-10,-3,9,-1,4,7,4,5,2,-9,-8,-3,-6,7,-1,-5,9,7,1,-4,2,5,5,9,-1,-6,-1,-5,7,8,4,-1,3,-10,-4,1,6,-3,-7,8,1,6,-5,8,5,-10,-9,-2,6,1,4,9,-10,-3,-5,5,-7,5,-4,-5,-8,9,-5,4,-3,-3,-6,9,5,3,4,-5,10,4,2,4,4,9,-4,-1,7,4,-6,-9,4,10,-7,1,-4,3,4,-8,-1,-8,-2,-4,2,-2,2,1,1,-5,6,-8,-3,-6,6,-5,-1,-6,3,1,9,-6,-5,8,-8,-4,1,3,-3,-10,3,8,2,8,-5,3,-2,-6,7,3,-8,-10,-9,2,-1,2,10,9,-5,7,8,3,-8,9,4,-1,-8,-5,3,10,-10,10,-2,1,-8,7,-8,-5,1,4,-5,2,-3,10,-4,9,-1,-5,-10,10,7,-3,8,-3,-4,-6,1,10,-3,-9,-1,3,9,-4,-6,-10,-10,10,-3,-6,-10,-3,10,-5,6,-2,-4,10,4,-6,-8,5,-9,7,8,8,8,10,-7,-5,-1,-9,-3,-2,-2,-7,-5,2,7,-6,5,-4,-7,2,-1,4,-3,9,-3,3,9,8,4,2,9,8,-3,-8,-7,2,-7,-10,-3,-10,-9,-10,5,-6,7,-2,-5,-10,-3,7,-9,7,-7,-10,-7,-5,-3,7,-4,-9,-1,7,1,2,-6,-3,-2,-2,-9,-9,3,3,2,6,-2,-9,5,-7,-5,-10,2,5,8,-2,2,-5,7,2,7,7,2,2,-4,-4,2,8,-1,-7,-4,8,-10,4,-9,9,6,-7,2,6,8,4,7,-3,7,-9,-9,-9,-8,-8,-9,4,5,-4,1,-2,3,9,8,-10,10,-7,6,9,1,2,-6,-5,-8,-7,-2,-7,5,-7,-6,1,8,-6,-6,-8,-2,-6,7,-9,-4,-3,5,3,4,4,-1,-7,-3,-3,7,7,-4,-10,-6,-7,3,-9,9,-8,-4,-2,-7,3,-1,-10,-2,10,8,6,-6,6,-2,-6,7,-4,6,5,5,3,6,6,8,3,-3,4,3,-9,-5,6,10,-4,-7,10,-6,-10,6,-10,10,-4,4,2,-6,-2,5,4,9,-10,6,10,4,-4,-6,9,-8,8,-9,-9,9,-9,-1,-8,10,1,-1,-7,1,-7,8,2,9,9,-8,6,-2,-4,7,-7,3,2,-7,10,4,4,5,7,-5,3,-7,-3,-1,1,-10,-4,4,-6,9,-10,3,-5,1,-2,8,-10,-4,3,-1,-5,1,-3,-7,10,4,9,6,-6,5,3,-5,10,7,5,8,-10,-9,-5,-1,2,-7,-5,-4,1,-2,5,-9,-5,8,6,-9,-4,9,-5,-6,-8,-10,7,-7,-7,7,4,-7,-4,-8,3,-7,6,-8,-8,9,-1,-10,-5,1,6,4,-1,9,-7,6,-6,9,-10,-4,3,-6,-2,-5,3,-9,-1,9,3,9,-6,-2,-9,8,-7,-10,4,7,4,3,7,8,-4,-1,-6,-8,7,-7,-10,8,7,-10,-5,9,10,-7,-5,-6,-2,7,-7,-2,-7,-3,-6,-6,10,-4,-2,6,-4,-8,10,9,3,1,10,-6,-4,6,1,-5,-8,8,1,-4,9,-7,8,-10,-9,-10,-6,-8,5,-2,-5,-7,-5,3,-1,4,-10,8,4,-8,-10,-4,7,9,-3,10,10,-1,4,-3,-2,6,10,2,3,9,-2,-2,-2,-3,-3,-4,-2,-10,-10,3,1,-6,3,-5,9,2,4,10,-6,-2,8,4,3,-6,6,-5,-1,8,-10,-4,8,10,-7,-9,-5,-4,8,-3,-1,-4,-2,-5,-1,-1,-7,-7,9,6,-10,-1,-7,10,-10,-8,1,7,2,-6,-7,1,-2,-9,-8,6,-2,-4,1,-4,-6,1,4,-3,-2,-7,-6,10,-9,-8,6,8,1,6,-8,3,5,-3,4,5,-5,-2,5,10,5,-4,1,10,5,-4,-8,-7,2,4,-6,-1,-3,3,-7,3,-10,-4,6,3,-7,6,-5,-10,5,-3,1,3,7,4,-8,7,-4,8,-2,-3,9,8,-2,-1,10,-9,7,9,-7,-9], dtype = "uint8")#candidate|1452|(4576,)|const|uint8
const_1453 = relay.const([-5.797647,-0.862084,-0.515944,-7.714198,6.805704,1.145428,1.679894,0.103728,0.545548,-0.832777,2.684123,-6.195826,-1.472497,2.520132,6.412061,-9.250758,-9.602258,2.449757,-0.887277,0.182230,-3.596042,0.807932,3.521930,-0.220527,4.223860,-0.652597,2.476589,-9.072281,0.303406,-2.282173,-8.810868,1.428974,0.977139,-8.228764,-6.344594,9.197981,-5.673245,-2.239618,-9.565133,-4.450479,0.255231,-1.475324,-2.303789,0.894205,-4.092200,-9.229303,-2.958072,-2.837249,-8.716041,-2.112895,-3.491055,-4.449255,-3.810766,-3.223114,2.762083,-6.639106,2.079555,-2.268859,8.538159,-7.138813,9.073492,4.039235,-6.529187,0.144870,-7.327007,7.673990,-7.250501,5.995966,-1.078659,2.709356,2.089090,9.202073,-8.938870,-1.820141,5.571364,-4.661942,3.771102,-7.941834,3.650090,6.909026,8.703694,-4.119091,-5.538801,-9.736302,9.522556,-6.461918,-5.334384,-7.063293,4.909288,-7.331866,4.400932,9.309969,-6.831175,-7.249416,-1.258655,4.059040,-3.724945,2.943911,-6.062951,7.811116,6.146087,-8.080632,8.976988,-1.053350,0.397896,7.341793,0.219622,0.955359,2.474337,6.966655,2.422173,5.623265,-6.909445,-9.305830,8.343261,3.150328,-1.700796,-6.890013,-1.377924,-1.127546,9.773243,-6.808112,7.754951,5.994348,3.739329,-7.059516,1.782345,-6.865161,-4.827236,-2.186648,-9.927464,-6.629004,8.390828,1.122401,4.715110,3.761262,0.684566,-9.034437,-6.490144,3.774181,-8.200006,-9.240551,-5.989764,-2.853888,-9.948007,-0.858968,-5.157886,9.701820,1.894292,4.906932,-9.299157,3.703386,-6.190448,-9.939010,9.472334,-6.828204,3.075255,-4.369252,1.979363,-3.083776,0.238225,-2.652675,0.684134,-6.762996,-5.385780,-1.352535,-3.893745,4.711060,6.812149,4.724086,2.364849,-8.878883,0.173163,-2.248144,7.439927,-1.394624,3.805335,-3.491525,-8.507415,6.479797,-5.031656,4.182231,-7.617742,5.200695,6.855769,-7.243949,-6.464162,5.670376,4.189342,-4.649272,7.603952,-8.502399,-7.777777,3.099230,1.144812,0.386709,-0.756509,-0.686719,9.292773,-9.975132,0.513621,-3.150698,-1.008395,0.193128,6.325996,-3.275688,-7.296725,-0.596080,-6.332991,2.276630,-2.879226,4.516010,3.665350,7.161803,-4.389640,7.635738,9.205580,7.438485,-5.179279,6.466162,8.199600,-1.421334,-1.325886,-2.146647,-6.162359,-6.514397,-4.000764,-8.150525,-7.623454,4.902165,7.552457,-7.535281,-3.685456,-8.316539,-0.639655,-2.271971,-8.251572,7.144529,5.424490,2.950026,8.321999,3.976481,7.498679,8.019295,3.934330,-0.638776,-2.985566,4.740317,2.348589,8.951956,-1.696898,2.213361,-5.771215,3.978015,-2.400838,0.985099], dtype = "float32")#candidate|1453|(256,)|const|float32
call_1450 = relay.TupleGetItem(func_609_call(relay.reshape(var_1451.astype('uint8'), [1, 416]), relay.reshape(const_1452.astype('uint8'), [11, 416]), relay.reshape(const_1453.astype('float32'), [128, 2]), ), 6)
call_1454 = relay.TupleGetItem(func_614_call(relay.reshape(var_1451.astype('uint8'), [1, 416]), relay.reshape(const_1452.astype('uint8'), [11, 416]), relay.reshape(const_1453.astype('float32'), [128, 2]), ), 6)
uop_1461 = relay.cosh(const_1452.astype('float32')) # shape=(4576,)
const_1464 = relay.const([2.884775,1.014283,6.009905,-7.494981,-2.090407,-1.489633,0.244908,7.105365,-6.971153,4.533143,8.677836,6.697995,-2.788056,6.615702,3.212740,-1.645956,-6.693614,2.337673,-8.307908,-3.142580,5.210188,9.126441,-3.746012,4.320795,4.627137,9.330532,-1.816969,0.011948,-1.137476,-0.155671,-5.270019,6.368927,9.132578,-7.774304,-4.219797,-2.106823,-0.720819,-1.883760,-3.711299,3.724876,2.602355,9.394787,-3.428504,-2.442423,0.438135,-3.947937,5.295269,0.462843,-1.978626,6.934516,-2.422020,4.322010,2.202507,7.402407,7.506640,7.693450,4.918114,8.373019,3.192450,-2.230948,-9.317029,-8.839684,-8.363641,-4.286846,-1.168998,-1.718398,9.259464,0.326897,3.470844,3.481531,3.323002,9.873940,6.235687,-5.097405,3.926172,4.095780,-6.496193,4.637888,4.984591,2.722353,7.756768,-3.324008,6.586929,4.365263,-0.652007,-8.690591,3.967106,-2.261845,-9.869259,-0.386888,-6.550022,5.244252,5.544622,6.500462,6.157094,-5.174834,-2.565827,0.229308,-6.824723,7.975922,8.818832,9.638203,2.337775,4.343829,-9.047299,0.555655,-1.645303,8.290891,-0.103123,-7.388653,-7.542899,-9.088331,-1.920266,-7.598882,0.156251,6.928544,9.634183,8.188223,9.079310,-3.396309,-4.123608,-5.142305,0.545775,6.254708,-6.947612,2.155125,-6.747814,-4.475771,4.146433,-8.183027,-8.174160,-6.142976,-2.129892,-8.930474,-8.350033,0.733660,3.991100,8.287402,-5.028512,-2.922843,8.305032,9.030456,8.132228,-7.282308,-4.122558,5.659778,-3.632812,9.818907,-8.204027,-3.629338,-3.282901,0.572472,6.053959,-2.042216,2.109308,0.879861,-0.555769,9.102563,-0.422723,7.597626,-5.570076,2.474159,-6.417766,6.463454,-3.149834,2.793376,7.900559,-6.926638,-2.671730,-9.997075,2.498172,-4.480992,-6.818466,-3.612946,3.292246,-9.074031,-5.319936,-1.530134,-4.701707,5.263361,-2.796247,6.051574,-9.280466,-6.611668,7.209479,-2.061395,-8.464434,-8.768911,-0.738412,3.824777,-9.086571,2.939926,7.864678,5.399538,3.014446,3.386182,-8.965944,-9.862146,-6.046055,3.397431,7.523581,5.549146,-5.149539,6.025046,-7.252373,-3.417042,-8.748395,7.203859,3.328049,3.681118,-8.263071,-1.301062,6.512964,6.920985,-0.366445,3.188036,-1.578431,1.644387,3.939701,-0.855122,-7.173023,-2.512998,-8.695253,-6.822303,7.689305,5.565274,-7.647986,-7.457418,-6.161124,-3.309250,-1.877233,-6.620349,-6.638562,6.251489,-7.394090,5.450042,-0.798547,5.209475,6.229673,-4.928602,7.979465,-4.021482,-1.402666,-8.429457,-8.718095,5.426684,-8.218739,-6.045164,4.950441,-3.992660,0.896422,-5.184361,-4.133901,-2.025130,-0.295738,-6.683556,-3.499044,4.354419,4.578406,9.773837,-4.560169,-2.855735,2.253957,7.776991,-6.996512,-6.366747,1.948033,5.723769,2.643934,-1.923462,-8.481143,2.327568,0.449569,1.932479,-2.235057,3.369267,4.496704,-7.585599,-2.173250,-7.502321,6.856316,-6.975286,6.274020,-9.126457,5.925548,-0.129810,8.042771,1.948773,7.857993,2.494672,9.084396,-7.544430,-5.249380,8.640513,0.297612,8.420652,2.762816,4.613941,9.042756,1.235455,-4.856596,5.007440,3.578830,5.195180,0.113217,4.542522,1.985391,-6.516019,-3.206049,-1.219499,0.984582,-1.645479,3.184908,3.918483,-0.471347,8.592228,4.986439,-1.212889,7.682842,4.372936,1.067436,-8.644935,-0.111012,-7.877159,-2.084863,-5.374484,8.843754,-3.332800,9.972092,0.742781,-9.672630,-6.443481,9.982251,9.946459,-7.371685,-0.494403,2.406128,-5.446626,8.361256,-2.755223,0.760955,7.622461,0.546177,2.819135,0.570988,-8.548479,-9.893258,7.768663,-1.566114,-7.199885,6.498562,-0.193880,0.827758,9.230077,2.437284,8.400271,-4.713033,0.238022,-1.834571,-0.449306,-4.355628,-5.932308,-6.033487,-5.187019,-4.024614,0.506174,7.358930,-9.496929,6.482474,1.752600,1.298654,6.438321,9.671323,1.109091,-4.188020,-3.817809,9.083019,1.814393,-0.472135,-2.347487,-0.074305,4.433122,5.699103,2.969262,2.610425,2.049309,2.634818,-5.164070,-2.339649,-6.119392,-6.459439,6.173505,1.061361,6.015567,-9.316623,-6.217402,4.342994,5.603990,9.995709,4.382111,9.567518,0.540493,-5.683478,-5.726763,-2.416525,7.658101,7.265881,-8.809431,2.155826,-3.151360,1.723433,-5.917184,-3.317835,6.307161,-2.022590,-1.508010,4.493866,-3.579286,-0.373281,-6.534859,-5.715844,7.761962,-8.015150,-4.476723,1.571623,-0.793234,-4.554112,3.906268,-6.689272,-6.207146,-8.551124,-8.167372,7.654105,8.958522,5.104519,-6.226768,3.330602,5.602135,8.922417,7.069176,1.391874,0.687910,-6.723462,-2.457899,4.336926,-8.499652,-3.241992,6.802086,1.883245,5.590113,5.202169,-9.729748,7.605737,-6.497823,-1.490366,9.652961,9.144135,8.872949,4.000837,-5.439368,-1.627880,-8.740907,-7.370855,-7.718469,-8.798392,-2.197198,3.434582,-7.829228,9.772416,9.836932,-4.206387,6.180193,2.612405,-1.290600,-4.251734,3.920526,6.900781,6.087145,-9.069287,7.708725,2.001813,-4.086343,9.195626,9.695796,3.607587,-7.749340,4.488080,-1.740508,-0.516769,-2.330964,3.639268,1.995995,2.401215,-5.012034,0.964973,4.164220,-2.609517,2.092841,-3.249011,-7.515855,-3.244237,-5.808790,-8.029591,-4.474280,0.589153,9.760543,8.808954,3.819977,-6.697297,-9.632284,9.451826,-8.461929,2.951041,2.744779,0.455912,1.710501,-5.393032,7.718416,-7.946450,6.094729,-3.798524,4.549744,-3.361487,2.683655,-2.077529,-0.784212,9.249637,7.120863,-0.780800,-1.167305,-7.099899,9.729295,3.437658,4.421997,8.736637,8.002359,-5.702780,0.027859,9.087709,1.759886,-1.915854,-8.574395,-0.388583,-9.449571,-3.449125,-3.342945,-6.979174,-6.043919,4.248723,-3.233259,-4.521464,-2.364878,-9.346012,4.176685,-9.374680,9.585676,-5.836701,-6.148011,-9.317731,-0.135849,-9.433278,3.745057,-9.077313,-0.222580,-1.709226,-1.956775,8.904512,3.955350,-6.228567,7.463803,3.633624,1.833251,-8.289714,-7.566431,-0.979486,-0.886072,-1.537531,-3.953918,6.925171,-7.870495,6.481509,-9.753377,5.231882,-6.351618,0.642043,8.990154,-4.967094,-6.406517,-6.528008,0.864692,0.108251,3.539194,-1.822555,2.540739,0.122332,1.149155,-1.210205,9.414462,0.501355,-1.079079,6.195190,4.733989,-9.645864,0.942126,-0.792771,-0.813782,-5.268749,2.689333,4.310868,-1.479491,-7.332652,8.763991,8.240519,8.885490,-6.121124,9.176302,6.660540,3.382405,1.770924,-7.941866,-1.378292,4.429782,6.443537,6.270361,4.673175,0.516436,6.530869,6.257375,3.817347,5.630070,-2.730501,3.452599,9.413872,0.045579,5.103658,-3.586151,-0.661863,-2.424830,9.708700,-9.007335,4.815336,-7.935901,-5.254088,-2.609524,-8.193323,0.366271,-4.079326,-6.992856,-2.751143,-5.764824,-3.004774,5.130771,4.348316,-9.278295,3.776112,2.036527,-6.400063,0.293686,5.591164,-9.732128,8.354354,-3.695555,-9.406746,0.532305,0.429655,2.908693,-3.957654,-3.605878,-2.691478,-3.393659,-4.287676,5.761675,-0.895577,1.503718,-4.335357,7.901995,-8.843678,2.605562,8.384133,6.979601,7.862311,-8.138657,9.417589,4.846586,2.032100,7.153934,8.194584,-6.760656,3.565654,-2.619328,3.119050,1.113264,1.263003,-0.919756,2.152247,6.937424,-6.396074,-3.507357,5.447159,-6.925621,-1.381421,-0.354010,-8.358513,6.774584,-8.519785,1.821818,0.306310,5.662209,3.375883,6.035225,7.233756,7.433830,-4.870482,9.901007,6.332593,-7.288080,6.948860,-9.083208,9.349984,9.324344,5.679470,6.680125,7.331802,3.974604,4.550274,6.465706,-2.389447,-3.036868,0.110745,-7.607427,8.724883,-6.931373,9.905604,-6.568963,-8.624671,-1.330293,-2.954686,-5.331850,5.904788,8.786918,3.213979,7.710511,5.555459,-6.385854,-1.223098,-0.683116,-6.265325,-5.267991,7.854636,-5.767082,4.890126,5.694842,3.761900,9.693019,1.539683,3.182148,-1.848840,-3.573173,-9.629740,-8.019507,5.024810,6.088129,8.557901,0.019271,-5.266515,-3.904072,4.564036,-3.870688,8.352543,3.944267,-2.525623,8.099296,0.316872,-9.081209,5.514579,-2.452317,2.475153,-3.976039,-4.707787,0.573565,6.617696,-1.487586,4.534432,9.052202,-6.565504,-4.341466,5.774787,1.865541,3.202817,7.846244,-7.828841,-5.476971,8.275542,-2.109590,-1.410097,-7.467725,3.610624,-5.230646,9.723321,-2.213376,-0.828299,-3.019235,-2.675146,3.797224,-2.980866,-6.333372,-3.420919,-7.041812,2.478826,8.482754,0.429745,-2.755469,-2.716284,1.489667,-2.956829,-9.884372,-3.962662,5.986281,-7.208458,5.348498,9.174117,-9.086481,-9.831095,9.814569,8.284784,4.377128,-8.030422,-9.372733,5.207136,9.621186,5.858347,-7.822316,-4.374347,-7.611769,-7.458940,6.112305,-7.251200,-7.895989,3.981433,-3.991755,-4.381083,9.651092,6.690897,-1.200598,4.632664,3.140076,4.501039,8.744035,0.381529,-3.554863,7.138339,8.059729,5.265006,-5.517558,7.029250,-8.738069,-9.265469,-4.355065,0.772690,-1.607494,-6.447205,4.761158,-6.017620,-8.653224,-0.772167,3.465395,-3.893601,8.213002,-5.780681,-1.833005,6.515475,-1.195935,-5.604560,2.706072,4.996181,4.386288,3.233743,7.905250,0.458146,6.317097,-5.825814,9.375416,5.887446,9.385242,-8.684016,1.422239,-8.788390,3.620144,9.998971,-3.731506,2.554038,-1.703741,-4.617119,-7.837999,1.192202,2.733882,-5.820906,5.418966,-8.088298,-6.441086,-1.224236,-6.412224,4.706622,-1.267837,-1.277606,5.518543,-1.101229,5.447199,9.106718,-0.996343,8.954853,-1.040649,-3.629268,-3.649524,-4.258156,8.390235,-7.808017,1.162041,1.479630,-8.112154,-8.649327,7.080528,-3.995881,4.786962,-3.797948,-3.697495,-9.365757,-6.720760,-6.482468,7.696973,8.914609,-0.456094,-2.720168,4.699218,6.794837,8.403377,5.674624,-1.626589,3.428887,4.941198,3.793656,-3.814684,-8.165003,-3.218337,9.900138,-1.513928,-2.606867,-8.164370,-2.851590,-6.716675,-8.079008,-2.095248,9.124432,6.898503,-2.089619,-0.783041,-9.627061,3.400058,4.777680,-2.648195,0.740682,3.925813,1.752470,-8.743856,9.525083,2.155967,7.806619,3.227630,-8.901714,6.008363,2.128216,-7.042858,-3.632494,6.744727,0.266255,-9.152891,-4.817939,-9.479463,-8.476020,2.070652,8.071343,5.453052,-7.624023,8.099081,1.719012,-6.732919,0.400065,-2.832205,-3.242396,0.298182,6.321075,2.578632,-4.526162,3.675619,-2.974955,-4.874726,5.050277,-5.015018,7.855059,-6.519529,9.039139,1.452896,4.960173,-8.887816,6.871900,0.694625,-4.294524,-3.287891,-5.265830,8.461504,4.538742,7.050640,2.317902,-3.039293,6.638806,9.461662,3.083573,0.791129,-7.412767,4.780978,-8.239009,8.312314,3.919160,1.882307,0.575666,-1.498039,-0.947831,-4.971112,-6.393715,-4.259556,7.532683,-6.837897,2.125430,-7.103108,6.990368,3.512703,-9.892093,-8.575700,4.655660,-3.054653,-7.473776,4.759790,-0.177935,-2.263057,-6.739678,-3.348173,-3.074628,6.522290,1.308701,-6.819944,4.745452,-9.701708,-0.432463,2.746539,-0.681727,-1.358212,-6.475182,9.769363,1.409602,3.380866,3.106676,-3.240006,-4.251959,0.130072,4.999515,5.005043,1.088005,-5.108251,-0.433545,2.237816,4.479815,-9.483315,1.308320,-3.390626,3.134391,5.586153,-1.771177,9.021795,2.566788,-1.501228,-2.251065,7.473187,4.552088,2.596949,9.499037,-6.551782,-0.532970,-7.188551,-3.106247,7.188235,1.761844,-4.155591,-3.911156,-8.505458,-0.767008,-7.335620,-4.873908,5.448707,4.414914,-2.772756,4.136677,-3.415303,5.790564,-5.149925,9.450977,3.793176,-2.123355,-2.810483,3.665446,-7.417754,7.767494,-5.502515,-1.219038,2.131647,-2.729074,-4.187840,-3.050993,-2.724256,7.255209,-2.311769,-8.028915,1.063978,7.740916,9.855884,2.304571,3.470888,-7.488379,-6.421085,3.438401,-4.691522,5.027817,4.187614,3.978694,5.446027,-0.258666,-4.296748,-7.093246,2.147647,3.673712,-4.917486,-6.644900,-8.429377,-5.053590,7.922744,-4.638580,4.745304,-5.857720,-7.226061,-2.062960,3.183496,7.205122,2.109494,7.744327,1.047137,6.808814,2.431507,3.181422,-7.522349,7.714624,7.956000,-8.524315,6.717597,-2.711093,-4.645404,-0.880745,4.730884,4.546894,9.730051,-2.043271,-5.368165,-6.970573,6.039892,5.911951,8.622843,-2.248974,-2.234685,-2.896438,4.930776,5.964127,1.518225,6.226518,6.734175,-7.567967,-9.560294,-4.842024,-6.085603,-2.355806,-1.199182,-9.798270,-5.322896,2.642305,0.117115,2.936843,-0.065032,-7.385807,-7.059248,-2.158440,1.148233,-9.497095,6.030783,-2.860623,0.819811,-7.854231,-3.880174,-6.311678,2.699934,1.487677,1.726813,5.490253,-9.710180,0.930722,-5.545408,-4.588603,-8.760482,0.813433,3.197936,-4.608468,-3.739661,4.551967,7.551191,-9.193470,8.906036,4.947877,-3.834380,-8.980924,-7.308415,1.901658,8.248560,-1.977060,-6.405856,-7.790418,5.734515,-3.992244,0.109132,-1.278154,7.511435,2.478853,7.875853,6.155757,8.323785,-7.014786,-1.978834,-0.960229,8.755365,8.327253,-8.762931,-5.174625,-5.605002,-8.235487,-8.305069,-3.264448,2.713669,-5.483467,-0.045109,-5.673640,7.960824,-3.138305,-8.799052,3.992364,8.542357,4.958687,-4.601412,-3.255918,-4.934482,-4.303192,8.111794,1.314676,-8.509507,8.453349,8.195793,7.411881,-4.936602,-0.970148,-0.196003,1.526920,9.806982,-8.485504,-4.949757,-5.021052,8.344120,6.551992,-2.062822,7.671868,-4.306104,0.698882,-8.019909,-6.259851,-6.698620,9.269111,-8.194260,6.401798,9.268025,-5.673858,-5.695077,-9.120356,9.898212,-0.628133,-3.413079,7.976798,5.626111,8.035402,4.348314,-2.004565,-6.685226,-0.531317,-3.226920,-3.837764,1.897018,5.217163,-5.495084,3.832071,1.179191,8.286793,8.942954,-3.388344,1.316886,-7.522497,1.451120,9.508903,-4.321437,9.960965,0.279473,-2.687363,-1.357182,-5.269640,-0.391826,-1.637845,0.770896,0.063334,-0.301747,6.124731,9.776161,-7.833262,1.251650,6.412651,-3.000337,-3.763376,-7.733564,-4.590092,4.580176,5.101592,3.678241,7.423970,8.318649,9.454243,9.550914,-7.260951,8.473111,8.606661,-4.370047,-1.765101,6.687150,-5.398757,-4.476090,-2.793675,0.181014,3.505706,-8.029609,6.465180,9.636960,9.402791,-3.250285,-3.350532,5.391928,-0.566117,-8.735937,-5.633045,7.274558,9.472290,9.948552,2.690948,-9.223429,8.609917,-1.711550,-6.554453,-1.016454,-1.278242,0.152934,-0.122321,-0.863262,-1.685758,1.073175,9.701240,5.366671,-7.571669,-3.193774,1.668692,-5.047775,6.512771,-7.194532,5.252606,-9.020096,1.249143,-6.371185,-6.067483,-0.600806,7.542241,7.126580,-7.575570,0.266172,4.767871,4.178021,-6.974666,-9.007755,-2.756202,-6.373505,3.657619,5.960374,-8.553020,-6.455971,-3.081267,-9.228801,-4.328022,-8.200445,-1.296781,-6.838069,-1.380898,7.147970,6.376444,-2.375901,-3.805404,6.963457,0.741208,-2.423588,-3.826342,-2.683277,1.095024,-1.112382,-7.137297,-9.716488,3.360317,1.124875,-5.665929,-3.176245,-3.925986,8.380347,9.985144,-6.414166,3.823027,6.966872,6.229862,5.151717,-8.301492,-7.896896,-6.089077,8.663589,6.351957,8.972883,8.506181,-8.812850,8.418271,-6.184196,-4.914127,2.707482,2.034137,-5.697028,9.544042,8.212792,6.642636,-6.754574,1.869152,5.611446,-5.163725,-7.033518,8.591169,2.563192,0.935920,2.511352,-0.652612,8.901853,9.127188,-6.768327,5.300991,-8.181555,-8.588883,4.010163,4.386362,-3.640925,5.300725,6.274169,8.892053,6.942804,8.170242,2.783852,-7.126560,9.165235,-0.625513,-6.284540,-4.621693,-4.944574,6.088059,-2.435795,1.819331,1.969002,9.139082,1.150668,4.599304,1.989567,8.683739,0.249334,-9.020650,-6.961037,-2.618232,-7.345353,6.208086,0.839037,-5.263758,6.205716,8.269372,4.806047,-9.197300,6.202138,6.974630,-5.041296,1.966606,-0.168305,-8.809652,-9.365862,4.809385,3.058434,-4.583562,-4.156863,-5.768292,-8.170875,-6.037252,3.183480,-2.937831,-1.109128,3.661274,-8.333756,-8.567898,-0.485580,6.781189,-4.127371,-6.572371,-0.009045,-7.733405,2.753491,-4.879380,-5.619055,7.230782,6.834035,4.224550,-8.149136,-9.488151,9.090013,5.509148,-2.571003,5.232079,-9.516430,-0.838445,-5.299444,9.347162,-0.465219,2.796031,-2.331467,-6.239992,-4.078050,8.848293,-9.269744,0.769041,7.186295,-0.741451,-5.209832,-0.832710,4.793433,8.167246,1.330018,2.346540,-7.814015,7.420030,-0.282865,3.273849,0.707494,9.772163,-9.726436,5.842543,9.486208,3.814636,6.426061,-1.392544,3.156955,-0.754633,-5.858851,-2.866921,-6.593791,5.301298,8.281844,3.117270,-0.285146,-1.310343,-7.223307,-1.499511,0.601214,8.476352,6.074526,4.098755,4.963678,6.270739,-0.575988,-0.804353,8.532556,3.833618,-2.717447,5.834813,1.411917,-2.116324,-2.388370,2.394230,-3.515142,-5.977886,4.107522,-3.082163,-4.606539,-0.055299,5.653460,1.172527,1.100628,5.404737,-0.443136,-5.029260,0.987977,9.016183,4.641397,4.164144,8.200794,8.106201,-1.073360,7.471150,9.057620,9.210686,-0.934820,-7.688543,6.579576,-7.177878,-4.431278,4.333392,2.523959,1.884220,0.301076,-8.844395,6.712886,2.089658,-6.037447,-2.245193,5.554816,-0.042793,-0.866114,2.572187,5.466511,3.293284,-5.322128,7.930040,8.862916,-5.024389,3.050864,2.751208,-0.850734,-1.270922,0.202233,-6.700500,-6.579404,2.745368,5.707214,-7.188651,-6.578058,6.855960,-0.346860,-3.108690,6.337192,2.732016,3.212212,9.889822,3.060489,-9.416725,-9.036139,8.732237,-1.090263,-6.045107,9.237218,-8.257046,-4.538744,-4.880694,-3.793488,7.819689,9.069276,-9.529856,8.209133,-4.499226,-3.653501,-3.457525,-3.848308,6.726130,-3.160924,-0.389590,8.396529,6.277714,-2.769721,-0.480840,-4.837154,6.141742,-3.206368,-1.998143,5.882080,5.485058,-9.994874,2.673648,7.828258,1.115745,-6.291073,-9.287917,-4.096279,2.574080,3.794400,5.348012,4.014417,-2.295717,-3.368218,-2.507084,2.530500,5.670116,4.805262,-4.430342,-7.793787,-6.042018,-6.336124,-1.934649,-9.215866,2.801083,8.052913,1.527547,4.068614,2.795320,-9.664076,-6.904226,8.683670,0.021070,-2.104666,2.484057,4.435548,0.158212,-6.839237,-7.028055,5.970734,4.919682,-1.694726,-9.989262,-4.604110,-5.745295,6.474665,-4.385406,-7.035677,2.143448,-8.756429,1.331953,-0.704484,1.397854,-8.780460,9.027294,3.610134,1.755456,1.445638,-2.526977,3.453650,-4.712395,9.448124,9.987844,6.973679,-2.292743,7.874088,2.800435,-7.541582,9.502975,6.191950,-1.470014,2.495844,-0.651571,0.871109,-5.489846,8.640479,1.703922,7.550920,7.661351,2.087262,-3.044264,1.728537,-4.459607,-9.041811,3.422416,-0.645244,7.665448,8.475565,-2.938919,-7.565713,7.777651,-0.817986,-4.998857,4.845939,-8.077625,2.008083,9.772852,-7.974340,-5.747325,8.729963,-1.827373,1.114494,8.403063,-0.967008,-1.113055,-9.803235,-8.092828,-7.074754,3.993704,-0.800748,5.585598,-4.487189,7.858152,-2.622980,-8.755495,1.734928,-7.554254,-4.796492,1.170129,7.384263,0.156752,0.484509,-5.626487,-9.283139,0.044672,4.518303,-0.825012,5.011305,4.188420,2.027689,-8.123460,-0.286651,7.546767,-8.982645,5.425274,-4.507378,-8.256210,5.703472,-0.690326,-2.798329,-4.615953,-7.366399,2.204692,-7.630947,1.852656,-1.076966,-4.605836,-4.146026,1.318671,-0.427693,1.338949,0.213558,-3.278643,-7.544218,-1.738811,-7.686914,2.650547,8.811709,1.224695,5.143356,9.308049,-5.120331,-8.518313,-0.222663,4.161561,2.714720,9.086268,-6.097467,5.477447,-9.022818,3.718755,-9.801505,4.280675,-1.463911,-5.010174,-2.787590,1.477380,6.174208,4.037875,-4.500178,3.325336,5.156285,-4.278596,-5.701236,9.994384,-9.883025,-3.109025,7.399290,-8.879491,-7.897533,4.393255,5.282178,9.962155,-0.813716,-5.905040,6.849182,-3.477315,-3.540000,9.282642,-5.893884,-0.831560,6.686688,-6.116979,-1.895851,-8.976879,9.081724,4.103039,5.760634,4.751057,-6.152500,-7.308407,2.795995,-3.874096,2.153443,8.235217,-0.253584,-4.427873,-3.462012,-1.268703,-3.317915,7.698141,-6.037817,-8.220439,5.039332,-8.089539,2.115147,3.669787,4.113539,-4.970892,5.806979,4.702067,3.422362,-5.981527,-9.913706,0.981887,9.572209,-5.974289,2.056065,4.027479,-3.337691,-0.147893,-6.119234,3.715253,-4.475314,9.337023,8.397471,5.200485,-0.532801,-3.270571,7.822339,3.803069,-9.666363,-9.675760,-0.226254,-2.401412,5.552703,-9.262432,-8.930866,-1.882163,-7.183941,2.008080,-4.734944,-7.721122,-3.211405,3.622572,-5.471989,-7.354346,-5.474258,7.163266,2.300465,0.098402,-5.688552,-7.660522,7.994761,9.054767,-8.713983,7.786162,-9.223361,-8.702173,-7.338794,-2.192340,-4.518283,2.126738,8.344682,-8.579619,-4.498948,-1.726252,6.597829,-5.107542,4.501966,-1.600105,-9.417561,-6.399275,-9.360365,5.642978,-5.387114,2.190799,-6.337800,7.158578,3.584930,-4.246736,0.116436,4.970346,-5.410748,-7.761039,0.646351,5.134678,-4.615426,-0.334073,-1.003199,-9.434779,6.211910,-9.051387,-4.542972,-4.326230,1.899138,-7.250009,9.395786,3.118265,3.485410,8.538633,8.365935,-4.180272,-7.903218,-9.262796,-5.471133,5.164119,-7.470402,5.165018,1.213784,9.691184,7.659614,2.208081,2.214234,-6.568117,-8.654515,9.694690,-0.720426,-7.950129,9.657603,-0.647470,4.862965,8.317486,5.547024,-8.697223,-6.114736,1.108918,8.012294,-2.931811,5.710308,1.184333,-2.131716,2.794472,-8.078021,8.255189,-7.642411,7.554834,6.965792,-5.878283,-6.996837,5.694181,-4.799501,-6.919423,-0.252725,-5.346071,5.088760,7.549728,-7.729368,-6.475463,-7.650939,-7.157992,1.639335,-7.183210,0.339826,3.827597,-7.200198,-6.583976,8.359860,-2.978512,-4.400891,-5.850074,1.131276,1.766339,-6.599133,-2.791419,-1.509141,-1.750605,4.670569,-7.141461,4.824849,-2.275667,6.293960,-8.614596,0.089317,-8.651662,4.021791,3.163112,-4.394296,-5.696658,-8.297207,-7.425744,-4.066616,3.220653,0.702530,-6.816446,5.570940,-5.959357,0.990564,-9.265307,-8.168000,-7.038740,5.803627,-2.575577,0.621047,-2.434447,4.551903,-8.234994,5.501132,4.106855,3.552888,1.518757,-8.349451,5.931186,-9.955772,-6.129287,-1.582857,-2.636184,-9.968398,-3.170810,-7.466996,-1.040022,1.506241,1.912679,-6.439826,2.289064,-1.016401,-1.927325,1.140481,-1.427633,4.160666,-2.075667,-7.112677,0.985530,6.299881,-3.310811,0.337685,3.293763,8.217861,1.174694,-7.234004,0.012474,-3.589688,0.769221,-7.414802,3.530225,5.248219,7.571079,7.804085,-4.940250,-3.723530,-7.892996,1.168919,-0.341383,-6.540864,-1.374970,8.708883,6.066647,-1.550914,4.650657,-7.011794,-9.780829,-3.529383,5.652753,5.397699,-9.430814,-4.224060,0.403918,-7.183917,-5.415137,7.427287,4.075793,6.071548,-8.662902,-2.397650,-9.577800,1.747905,-5.768299,-4.388701,9.833716,2.548484,-7.234426,-0.476131,-2.806988,9.196155,8.565207,5.962797,0.085289,7.962806,-8.183062,8.083003,-0.946706,-6.462858,-5.578891,2.593272,-3.470984,1.692372,-3.909924,-9.578700,9.649973,-2.453448,-8.275351,1.459671,-7.116914,-8.397624,-3.557600,3.077379,-1.584690,8.882858,-0.503851,-5.201187,-3.160495,8.896875,4.229336,9.037664,-6.188392,1.120793,5.196334,-9.013576,0.420496,7.058181,6.209990,-0.562469,-9.657458,-2.445669,-4.620355,7.035675,5.187604,-6.467541,-6.001064,8.806966,4.258748,6.782330,4.291921,-2.967056,-9.368692,8.461140,-6.929440,7.520788,1.987141,8.819512,-8.940498,-0.510568,-3.535712,-6.161374,-7.220456,8.993353,-9.002090,8.542367,-4.991256,-6.661959,4.639773,-1.681966,-2.337550,-5.208751,-8.360354,3.895581,-1.315958,-8.904207,-1.633660,4.355909,-0.033964,-8.628357,4.155933,-0.768783,4.372061,9.311620,-6.630441,-8.718360,1.232951,6.478827,2.340605,5.848667,-3.745869,-7.239269,-0.519487,-9.161217,-0.884731,-2.824244,-4.969702,8.703818,2.552054,-0.439371,9.269196,-5.591356,0.490389,-0.859982,4.452868,-8.039424,4.888190,-6.274154,-0.299703,-3.809661,-7.643523,-3.184317,5.442641,-9.042849,-4.424161,5.025295,-4.882124,6.097734,8.903059,-4.315371,5.348832,-4.500362,3.280361,-6.103840,9.513381,-9.261923,7.940643,-5.484162,-2.371773,-6.773818,7.243103,-3.939142,7.421639,8.819844,1.398594,1.431330,-9.008911,4.500608,0.497323,5.901535,-0.198239,-8.189638,8.093101,9.545009,0.913706,-8.315864,5.145781,-0.752117,-2.606242,7.712043,9.235008,-6.192538,-5.815751,4.423302,-8.073788,6.556961,-1.976506,-8.028377,-2.615222,-1.761148,5.374140,3.237491,9.651917,-3.672972,1.963571,-7.966550,-7.692397,8.848345,-5.248527,-5.575952,7.080675,-8.093878,4.748878,2.280014,-4.177108,-5.037870,7.697219,-6.306200,1.257110,-0.322751,-3.502281,-8.557179,-5.470029,8.518336,-4.071024,0.307013,7.938667,-0.631874,-3.001333,8.303690,7.906202,6.856728,7.386538,0.465673,-8.183345,3.376827,-0.357548,5.916142,2.786362,-0.485920,7.686849,-6.103691,0.509540,4.874190,-8.953642,-8.234840,-6.317032,-0.612466,3.842960,7.236348,-5.434203,-1.553819,-2.850317,8.758222,-4.784643,3.424736,7.795486,0.647494,-3.500448,-8.675928,9.326699,-0.646858,-8.600049,7.437013,2.185453,0.268840,5.807448,-6.439070,-0.540413,-8.363151,0.213047,-1.296979,9.230270,3.946090,-6.106785,-7.462660,-6.575814,-4.893015,-7.817457,-5.220026,-1.518699,5.275716,6.677790,0.463008,8.892278,1.135227,3.791525,7.337479,3.705141,4.087575,-8.480349,7.582224,-3.718638,-3.797175,8.370515,-2.619496,-0.624596,2.576153,-5.278061,1.831390,-6.545094,-0.354902,-2.018024,-1.654331,1.523471,-3.798253,-9.145120,-2.209210,9.641536,5.650597,-6.427294,-9.670578,3.129436,-3.170873,-8.841492,4.369119,-2.252801,-5.249680,3.549890,-1.361312,-2.477932,-4.047947,-0.543898,-2.166212,6.546624,-8.833312,7.859471,6.135619,5.974651,-7.144380,6.294845,-1.228495,-6.620912,0.820984,-2.561779,-9.660236,-9.560538,7.598703,1.566069,-9.264829,6.400614,-7.429790,1.248642,1.485533,-3.058873,-5.184899,7.983077,5.477721,6.229651,1.555205,2.869687,0.722114,-3.626545,-7.542568,-3.013500,9.953892,-2.667621,-4.905627,1.640907,-0.030846,-1.025247,6.863534,5.398857,9.203979,6.855475,-9.167139,-2.844733,-9.037378,-7.554831,-1.642378,4.140244,-6.567213,-0.196242,0.620932,-6.130957,4.794504,-8.407627,-4.596578,6.460631,5.647190,-4.960754,1.912650,0.878996,-2.999633,5.084549,-4.927337,-5.707912,-7.101281,1.749319,-6.837385,6.653454,-2.209467,-9.289832,7.870015,-4.672806,4.890637,5.902809,6.292745,-9.432232,-8.820050,5.681071,3.158923,-9.209991,-1.936184,5.389477,7.843309,-1.347819,2.763394,5.153801,-9.955908,0.137648,-1.533729,4.639629,7.224799,7.986372,5.692748,-6.651479,-6.747258,-5.020393,-9.158315,7.879906,-3.864605,-2.891138,6.711480,-3.692185,6.688088,7.662489,-8.062528,-8.497904,-3.509137,-0.353476,-6.819128,-3.667145,1.977730,7.702851,9.830354,4.225237,-2.419271,1.295759,1.851404,9.751996,0.553973,6.380675,6.155628,8.565970,4.577818,0.031811,-2.609798,0.305532,-2.634033,5.060220,9.584850,9.391872,-5.274459,5.698366,7.688856,8.262546,8.242196,-6.238702,-1.591813,3.587956,4.121971,5.708990,-0.687124,9.085429,2.280499,-0.109410,-5.144778,-1.180459,-9.688149,-7.787056,-6.116896,-3.682976,-9.339369,0.688724,-1.751794,6.365622,9.649594,3.890426,0.839268,3.166695,-3.121959,2.687807,5.775110,6.517617,-1.292692,4.322407,8.679269,-3.332957,6.872544,-2.747660,-1.591974,5.656905,-0.743530,-2.791382,-1.165244,-5.540255,9.222800,2.898278,0.744312,0.183025,-6.796642,4.545612,-7.292458,-1.855818,2.319016,-4.124811,-6.386807,8.341996,-5.156744,-4.876940,6.416301,4.154503,-6.979603,-0.498610,-2.171385,0.486021,-0.119502,-3.132148,4.897199,-2.163946,-5.176069,-0.072282,7.668468,0.410338,3.265015,-4.636038,4.063904,-7.888389,-3.734459,2.745726,-6.476510,7.393481,4.977991,9.395879,-0.207852,3.227468,-5.890264,2.324740,-4.401114,-6.526337,-2.308975,-7.847572,-0.702991,-9.058955,7.003495,7.294098,-7.098866,3.892401,2.214448,-7.913720,-0.235894,-1.972288,-2.132526,-3.200528,-3.951782,-6.978811,8.859943,-8.174434,9.072524,-1.029127,0.999616,-6.462600,3.058890,7.229284,2.997008,-8.344785,-1.432960,-5.037945,9.039291,5.955519,8.883699,-3.713375,-9.344693,2.521571,6.405320,5.419732,8.717614,2.022026,8.450839,1.857078,-7.031021,-4.424254,-2.162969,2.891382,-8.797431,-9.338315,3.826739,-9.796364,8.229362,5.492560,-8.373339,0.298280,2.825173,-4.701029,-9.973387,7.574123,5.952706,3.786198,-6.488318,1.260467,5.757295,0.233588,0.044188,-5.580414,4.529845,9.640991,-6.392011,5.921558,9.812894,-2.747489,-5.641922,2.422631,-2.460718,1.520115,0.031371,4.173621,-1.182580,1.320242,-5.642881,0.438227,-3.260320,1.869414,9.868880,-1.143153,-4.362339,-6.794052,-0.308920,6.478618,-3.350220,0.991117,6.776708,-8.570320,6.059514,7.683562,-4.560033,7.883867,-9.293356,4.706574,-8.620648,-9.504147,8.203671,9.112251,-9.914638,-8.163090,7.598832,0.097693,-1.362908,3.393783,0.931697,5.626241,4.582521,-8.558968,-8.123855,4.406217,2.288358,3.450158,0.198991,-5.396870,9.670559,-1.676789,6.776710,-1.673616,-9.991502,1.137362,-6.984436,4.439248,-3.366949,3.113091,2.026976,3.131440,0.545115,9.561247,1.040191,-2.398301,-6.228360,8.365555,-3.709933,1.657650,3.969302,3.090553,-8.730730,8.366143,-2.278070,7.181944,-3.910246,9.286595,3.502729,-6.242394,-8.341574,-8.243334,1.851235,-8.801240,0.807260,-7.014269,9.335011,-5.478995,-7.379110,-9.178435,2.168425,8.831954,-7.485128,9.221991,9.762891,-0.103516,-5.339560,5.567087,-2.720380,-4.532579,1.965774,9.324740,-9.506201,-7.290390,8.676393,7.222355,-5.833292,-1.027662,5.078002,4.517754,8.679164,7.801456,-0.027434,-3.236712,-9.006613,-4.462806,6.628187,-2.307351,3.666373,6.960312,8.021310,0.132237,3.272207,-0.716629,6.545704,6.812420,6.904195,1.969296,5.464168,2.890027,-4.397525,-1.440009,4.646099,0.394174,3.532941,6.668578,0.854211,1.874605,1.009491,-9.968822,3.688028,9.881834,-2.265764,-5.815292,-8.488866,5.713094,2.723010,9.457935,3.622209,9.456163,3.134855,8.955979,-7.055841,1.589296,9.352587,-4.296433,1.399357,1.013210,-9.572813,-4.215767,1.884824,6.865503,1.097347,7.028871,0.739388,2.218495,-3.593505,-3.525507,6.539671,-7.847571,3.930383,1.758067,-7.962050,-1.008525,-7.560341,-7.463448,-7.071128,-2.807408,-1.473458,-6.248810,9.511115,-3.899342,8.352924,-1.329710,-8.905218,8.393909,5.972068,-0.351680,1.687289,2.020553,3.083265,-4.632510,0.596783,7.431992,-1.408418,-2.823664,-6.547051,4.903717,9.971984,-1.059979,-3.006290,0.764014,6.698140,-9.147149,-1.967002,-9.598206,0.782624,4.490071,-8.894960,-2.627705,5.364450,-5.065993,9.135281,4.477885,2.048012,-5.811097,5.525840,5.047747,4.816022,3.806080,6.133946,-3.367106,-2.775151,-9.754389,-2.971201,-7.270131,5.440000,2.100664,-9.492425,5.740183,4.151047,-2.111468,6.081602,2.418226,7.376925,-7.495051,-4.014352,3.301084,-6.297558,1.291030,-2.718636,-7.641146,-4.067838,-1.573875,-5.643152,-2.038212,6.300775,-0.952394,6.145425,1.982885,0.199256,2.491976,-8.042625,-8.505587,-1.428314,-0.340363,0.155268,-4.029779,-9.799431,1.707734,-2.620465,-1.960540,-0.669857,-1.864372,-9.757874,-6.597682,0.445991,-5.631920,-7.495137,6.190860,-6.661422,0.230214,-7.861234,-7.160221,-4.400017,-7.979031,7.293516,-2.652012,5.164300,4.397428,-8.488475,0.530163,-3.122483,-0.961056,1.880458,1.652757,8.299676,9.775602,6.967437,-7.320297,4.398555,-9.673902,-7.932770,-9.277590,-9.584807,6.342171,9.426908,-5.448906,-6.342620,-5.986695,-4.047936,-3.070026,-1.841263,-7.002682,3.606358,2.337358,1.143087,3.230216,-5.749184,3.464695,-5.427035,-7.669144,-4.652793,6.408187,3.339812,-0.628670,8.318850,1.295431,-3.993310,3.628022,-6.104638,4.551526,7.128992,0.722587,-5.092965,-7.277096,-9.895887,7.248111,1.522837,5.921860,-1.530609,8.551063,-3.972240,-1.360369,-0.120130,-9.066894,-0.901740,-8.206508,6.395529,-3.407304,-9.278777,-7.379059,5.370293,8.831592,-6.485053,5.055521,-8.179382,-5.138319,6.380099,-9.234625,2.149693,-2.616525,-5.528476,7.157793,1.638943,9.229820,-9.369058,-4.096352,1.254709,-0.919303,-0.812530,5.104750,-5.214673,-4.431532,-4.893169,4.186534,9.814132,3.158045,-0.337528,7.138336,-2.945367,-3.131769,-1.885831,-4.672737,-8.121302,3.536073,-2.429215,-1.592838,9.555708,-2.711033,3.414386,1.900976,-1.944499,-0.740501,0.758734,-2.554519,-8.189536,-2.488246,2.839431,0.277773,7.982182,-7.604404,4.764966,8.416013,6.083600,-3.953860,4.887247,-2.366034,-5.452445,1.182121,-1.291265,-7.498101,-5.924138,-1.610341,6.845774,7.996714,-0.172217,7.110438,-5.797528,-7.911353,-7.022008,-1.865445,-2.906484,3.564979,7.429159,-6.029367,-5.564901,0.869983,5.991599,-3.707709,0.497845,-4.560955,-3.731960,5.940870,-8.503356,-8.295045,-9.596132,-3.982093,4.114844,7.388573,-4.456487,0.490481,-8.236911,0.198350,-4.483808,9.799451,-2.862115,7.898787,3.071547,2.458862,6.965518,-9.494917,8.643093,-3.791018,0.363849,2.446962,-7.504344,-4.962695,1.288269,-4.983689,-9.191576,3.397192,1.719014,1.737678,2.128315,-8.465826,-6.451673,-5.891331,-0.276650,9.891689,5.440013,5.501443,4.060539,-6.470392,-5.199670,-8.692231,-8.580354,2.458941,-7.723483,-6.057643,3.574495,-7.811098,-7.505597,5.074537,-6.138804,-3.729196,-6.762305,6.849512,5.064841,-8.911064,-3.688249,-8.559972,2.924528,5.077879,-9.622166,6.617016,-4.103036,-2.089448,3.160207,0.171502,-3.325440,6.446790,-2.446523,-9.212987,-1.000414,7.056431,6.598104,-4.101518,4.492089,-0.234060,1.974482,6.058787,-6.165800,-2.166720,-3.417567,5.899455,9.206223,4.535994,6.363210,-9.110139,-3.094658,-0.870449,1.471192,-1.239462,-0.154039,0.213807,9.382981,-1.513493,-9.463644,3.108569,-4.382732,3.060617,3.482215,0.531792,-7.592310,-7.574400,3.749259,-3.501314,1.727281,8.561997,7.074923,-8.815849,-4.337902,-1.746505,5.228936,4.577463,-1.601894,-1.981928,7.651873,-9.227496,2.162295,-0.685863,-6.525359,9.519808,-1.064052,7.077103,3.930180,-2.178088,-4.976339,-3.574843,-7.669049,-1.583266,-6.779912,-8.834860,-5.035236,7.951917,9.570537,6.467172,-9.491989,-4.720435,0.031959,4.961371,9.058456,-3.973070,-9.341257,4.037085,-6.386388,-2.376861,-0.355171,-0.945102,9.139046,-0.079980,-1.762916,-4.503387,2.346643,8.994286,5.450749,6.659345,-3.882219,-2.358155,5.177772,7.535609,4.332555,-4.071463,-4.678111,7.543041,5.715262,-5.758293,4.793708,-9.278221,3.933151,6.621174,-9.640848,8.090335,2.307513,-1.654741,-7.409990,-8.657442,9.697753,7.837680,-2.052085,1.668939,2.091222,3.132566,2.951579,9.977120,8.337574,7.785416,8.981576,-0.141619,-7.101774,5.331808,-4.455099,0.615228,5.803636,9.165313,0.370680,4.774899,-4.906353,5.867845,-6.550323,2.370072,5.954492,-7.106614,7.143499,4.917401,7.551848,-8.289613,4.223621,4.857445,8.877486,-1.834430,4.824467,8.499420,-3.604285,3.257801,9.673693,-6.295655,2.871257,0.562729,9.978874,7.874156,-7.538321,-0.453464,1.665552,-0.551784,-9.992225,4.841328,-6.642637,5.913660,3.726020,1.533428,2.912587,4.278525,-9.322816,-8.605912,-0.342651,-7.590412,9.373070,-6.938731,-9.807536,4.061133,2.471931,4.973152,8.382794,-6.526071,6.771172,9.378313,1.025728,-9.405629,-2.464131,6.800723,-4.173829,8.013899,-5.190887,-4.426159,-5.156963,4.839836,-0.737900,6.827793,9.641340,-9.823881,4.399892,-2.639937,-9.805149,9.582326,3.858003,6.823032,-0.649631,0.331160,-6.042850,-1.249873,-3.929539,-0.008508,-2.080659,-2.272935,6.946401,-3.125813,4.389824,6.607330,8.423416,-0.224989,1.115069,-2.392260,-4.696300,-0.611128,0.041733,1.978968,-5.877729,-3.606760,7.049246,7.430956,5.441885,0.674040,-7.760636,2.204080,2.797898,-7.493751,0.467760,9.598705,-6.028858,0.082290,-7.720336,6.578698,-4.954310,6.259227,8.450926,3.817074,-4.796044,0.923999,7.044406,4.040918,-3.043148,-1.228686,-1.429584,0.619166,1.273216,1.990878,7.639987,8.013813,-4.194721,7.924226,0.388554,4.443280,4.014534,-3.562680,5.644393,-7.084740,1.489926,5.580596,-1.798789,-3.428003,1.244072,2.974186,4.532016,8.272993,0.378415,9.928093,7.489385,-4.074052,1.484214,0.518092,-4.813057,-3.588423,-5.986992,-2.668233,-4.464072,2.602879,-2.703467,-1.760376,1.086922,1.624183,-3.028088,4.427576,2.622826,-8.534823,-7.457848,4.310392,6.059618,-7.660100,-0.840024,-8.563190,1.848328,-9.447299,-7.180456,0.880469,-8.204412,-0.018648,6.648330,-0.314829,-9.607971,5.106601,7.930001,7.441440,-8.085188,-8.828297,-0.392641,7.451207,-6.350162,0.332505,-1.928298,-2.200366,-0.632173,3.510140,-7.007033,-2.025933,5.479051,9.566407,9.442367,6.929802,-9.066598,-2.433560,6.590550,0.067778,7.962365,-5.624368,5.097172,3.441715,-3.402208,-4.658459,-1.135327,4.216814,-5.221744,-6.982303,6.030815,-8.178421,-9.234633,3.776463,-7.743425,7.902600,5.158036,-8.315380,9.788239,-2.924361,-3.121953,-8.886414,-2.281276,-8.321860,1.473738,-2.860140,5.779292,-8.786516,2.270533,0.354016,-4.800707,9.237612,-1.276368,3.531409,3.961481,2.140427,-7.437156,0.243829,2.024599,5.493868,-0.472674,-5.135436,-3.162227,1.360094,-8.135098,-8.628591,-6.814706,-1.316094,7.064016,-5.657147,-0.650857,-1.964504,4.400318,2.948228,-0.935558,9.377604,-4.048984,-0.904068,0.951522,-6.439907,-3.302922,-5.831858,-4.691128,4.107798,-9.154627,3.650278,-2.694826,7.039856,3.645925,-7.246410,-6.070752,-4.173787,9.065490,0.554681,3.876132,-3.779728,-4.904913,-3.328782,-1.087926,-7.974204,5.436734,3.732980,-8.885281,0.172814,9.979325,8.435823,-4.976604,-6.904876,-9.926225,-4.153917,8.417046,9.288896,3.975722,-5.332745,6.591072,4.712505,-2.246021,-4.337431,5.999241,-2.023031,-8.731820,-3.290751,-2.679853,-5.665659,7.791640,-6.830048,-0.585562,-0.116396,3.869807,7.261706,-6.391228,4.180357,2.860291,5.503732,2.364111,8.086532,9.095686,-3.128908,-0.783480,-2.831783,5.929817,-7.715807,-3.978348,-6.696676,2.891957,-7.162629,-0.273685,8.967680,-8.970747,-2.725041,-4.418748,7.229180,-6.034490,4.332928,-1.903278,-6.231420,-9.304878,6.255481,0.618270,-1.424865,1.030464,-0.125573,-3.976459,8.586330,-8.608456,7.296154,5.452354,-1.595370,-5.442268,-0.561655,6.366192,9.915161,6.941288,-9.509311,-5.292320,-4.049278,-4.229546,2.187924,-2.666083,1.847430,-1.884407,6.950678,6.184475,4.956394,-4.693356,-2.511301,-3.816229,9.687577,1.498047,9.575799,7.527860,8.694578,-7.555655,-9.709449,-8.298798,-3.409375,-2.835335,-3.569538,9.215794,-0.697707,-3.006878,-3.970708,-2.637864,-0.327617,4.800220,5.432694,0.299316,-5.440413,2.421773,-9.704951,-5.740413,-0.114124,0.732792,-5.837272,3.842446,-4.797414,-7.446645,-0.833741,-6.349826,-4.989179,-8.893813,-9.959543,-6.366028,-4.968963,-2.822334,8.890335,2.262812,4.000296,4.805146,7.404831,-6.014284,-1.632726,-9.051088,9.584719,1.713363,4.085732,0.209302,-3.134875,-4.023745,8.658446,6.340406,-6.136025,9.695622,1.667318,2.786933,8.033324,-6.099641,-8.513346,-6.251027,-1.889132,2.123259,-3.345797,9.064413,9.028301,3.627819,-0.759383,7.812486,5.471608,7.685532,4.466108,6.454009,-6.287285,-8.169157,6.413419,5.416579,3.510374,5.173167,6.640562,-4.045494,-0.763394,-4.598150,-6.214372,8.540388,-5.584290,7.017238,-2.732205,-0.476580,-5.304738,7.178722,8.940631,1.132806,-9.394039,-6.702471,-4.705822,-5.665394,-6.995852,3.458366,-8.785373,-6.689755,6.455328,1.603074,2.532402,1.054140,-2.535231,0.842371,1.951859,-5.112924,5.440352,3.669087,3.982435,-5.678905,-2.882508,3.615808,5.832905,0.736931,0.968217,-8.891231,-5.254000,-9.422440,-9.497475,5.045885,2.371902,5.052012,-7.804822,-0.636207,-6.991158,-4.067083,-0.991556,-0.554680,6.779857,6.991983,-1.000143,1.984518,6.669860,9.816437,1.199736,0.618802,5.717647,7.141491,7.824609,7.863751,6.685509,8.236688,6.902708,5.192148,7.116714,9.033560,-4.380493,3.446965,2.511098,2.483496,0.845242,1.260344,-8.056578,-9.710723,-3.901650,0.261339,5.868314,2.423862,-9.800035,-1.707301,2.979612,8.353166,-7.188557,0.024415,-1.869080,0.895236,1.856762,-7.651553,1.740339,-1.395452,-1.381422,5.229642,-8.773002,2.809556,2.812635,-3.577389,3.387074,-9.263152,-1.521385,5.796857,3.006321,-5.204085,0.068568,-5.339700,-5.764780,-1.830536,-6.332080,-1.091772,3.275055,-6.385614,9.099243,4.825329,-7.562198,1.882075,-5.618097,7.638626,8.267983,-3.002282,-4.233064,5.143158,4.306524,-4.371606,-5.267420,-6.543844,-0.876964,-5.408565,-6.912532,-4.236099,-9.361981,9.139898,9.684463,-7.958152,3.715281,3.152070,9.770625,-1.256606,4.220381,-8.019396,3.446737,5.625478,0.550820,-6.003944,2.714431,6.060847,-0.125319,-7.727844,5.307623,-6.228753,-1.737781,7.710724,-0.069355,-2.501049,-6.331129,8.511688,-9.676261,4.096239,3.248119,5.227657,-7.218020,-3.476736,1.041449,-4.805652,9.209233,3.238237,4.224859,7.497121,-8.366719,0.420712,-9.305622,9.476486,9.448476,2.817367,-6.284289,6.309223,1.287054,7.575159,3.603241,3.976142,-9.503919,-8.835553,5.688810,4.268098,6.874087,-3.947990,-9.668821,-9.186583,-7.984807,-0.960362,-1.208118,-6.561048,7.678091,1.002446,3.729547,6.272309,1.572066,2.503971,1.227274,3.544137,9.287382,-5.512231,6.596362,7.320824,-2.331220,-9.338671,-3.863971,-8.751216,-7.032752,-8.978418,8.246018,5.528242,5.174270,1.924281,0.103559,7.316779,8.176026,-2.156339,4.375294,-4.144544,1.564778,-4.549367,3.054358,5.697762,-5.845110,-1.957213,9.147155,7.323680,-8.079090,3.435216,3.263668,9.054423,4.910341,2.082904,9.930673,-5.113051,-3.885268,-8.863488,-0.088074,0.749480,7.752298,-7.149364,4.407785,9.383904,-1.320761,3.348268,-7.414348,-7.618937,8.736196,-1.176517,-9.592855,7.342254,0.633962,-7.148192,-9.238028,7.620309,0.381419,-7.266531,5.758189,3.783396,3.094972,0.020697,4.047432,6.594139,7.983444,8.240925,-5.747701,-6.198902,7.633539,1.190089,-0.241370,5.094168,-7.867105,-7.695732,-9.933286,-0.176236,-1.765619,7.859332,2.597435,-7.094450,-1.010647,-4.407679,9.189075,-7.909092,-0.955278,-4.173224,-8.301839,-7.315956,8.723724,-6.686386,-9.641553,6.518988,-8.229989,-3.192623,8.133100,-5.724432,5.310721,4.441298,9.806681,8.455924,3.998868,-9.034041,7.472747,3.705636,0.536238,-9.566270,-1.141626,7.145952,-7.424517,-3.187168,-1.628849,2.875290,-3.713224,-5.237094,4.888366,9.137392,0.782807,-5.711911,-3.510893,-1.605634,-3.857908,-2.435614,-0.306473,0.271811,3.429661,1.653631,3.715697,3.533921,2.686491,1.691009,5.796507,9.252946,5.946785,-3.747121,6.023727,0.030099,5.961336,-2.967214,1.154352,2.437131,-6.841625,4.943369,4.918795,1.538479,-6.682445,7.004623,1.960300,3.536746,8.724071,-4.762425,-5.161920,-9.313988,8.427520,1.297201,-2.274033,-6.783947,9.647031,-3.684794,-3.211037,2.052293,8.807229,5.938466,-6.043400,1.102989,-3.224374,-3.469968,7.656152,-4.813796,-7.288683,-5.533552,-5.533892,2.986392,-3.732153,5.432829,3.808048,4.572491,1.372840,8.957973,0.175106,3.824484,-2.490660,-8.330445,-6.370646,2.623357,4.231521,-3.189864,-1.659175,4.257552,9.256345,3.529509,-3.995385,6.030734,5.045067,0.459672,2.299554,-9.173274,-7.929377,-7.237179,-2.494086,9.881224,6.700698,3.515109,3.554984,-8.739482,0.932392,6.001184,-1.405560,-7.963481,7.116225,8.450886,-3.487393,3.988194,-4.242293,-7.496113,7.425155,-4.922540,5.926130,-7.673302,5.775648,5.892266,-7.275083,-5.725169,-0.388063,3.736319,-3.308998,-3.631167,-9.477862,0.546590,7.143644,6.302081,-6.246412,7.497508,-6.949745,-4.873133,-6.982197,-7.872119,9.802935,-0.869876,8.630335,8.794941,-7.872008,9.017755,1.221006,4.310441,-8.797187,2.398588,5.227998,-1.801768,-2.779769,4.096302,-4.036575,-9.710727,-2.948970,4.627094,-3.729560,9.201108,0.941489,8.233004,9.974483,4.557385,-2.085164,-0.704237,-9.548514,8.020648,-7.452005,6.970326,-7.190108,-1.932217,-8.617115,0.394154,-3.098780,9.071055,7.484163,4.896602,-9.432792,-5.394270,0.584147,-3.202389,5.462775,0.353163,-7.427265,-5.695199,-4.910626,3.609148,4.609161,1.065787,7.515620,9.883450,2.872590,0.524041,4.329756,-7.890003,3.640041,-7.741280,-5.120392,-1.328641,5.133821,-3.184998,7.197246,-8.976287,-3.423099,-0.931709,5.362165,-3.471478,-5.699681,-7.384097,2.399793,9.972695,1.890605,6.077873,5.440071,-7.786314,-9.347044,-2.148483,-8.211037,-5.294104,-8.065030,-6.306915,-2.411085,-6.764736,-4.690403,1.609743,-6.434016,-1.119052,-4.320179,4.546350,0.059976,-2.494817,-4.278918,3.176116,-0.014615,0.457572,2.742354,-0.460509,-6.955327,-5.999498,0.532100,-8.130426,-8.418136,4.696889,-1.993682,-8.749686,-1.107908,-1.639764,8.117103,2.941537,2.536234,-2.949321,-0.511082,3.103815,-6.232996,6.649230,9.411133,7.277740,2.540821,-1.217923,5.206919,4.327828,-4.759081,5.116826,-8.306256,8.323332,5.228803,-9.077598,-1.019885,0.336042,8.111449,-1.370833,-4.589606,5.591606,-3.604272,-3.091039,-5.641013,1.186284,5.734471,9.095747,9.576955,3.072267,-4.327943,-4.953058,5.775944,5.354738,-3.241971,1.511809,4.803361,-1.519575,3.103705,-3.577076,0.909758,-2.369766,-6.852670,-1.412980,-3.657899,-6.238724,0.422494,1.784383,-3.452129,2.990013,-8.095244,-2.843931,5.419483,0.338196,8.344071,4.350954,0.861834,7.254612,5.274340,7.463245,8.855430,-8.976218,-3.313021,-5.405347,1.418315,0.728176,-2.764944,3.497965,9.696550,-3.030088,-1.286288,9.148010,1.606763,3.261008,-5.413195,-7.065778,1.798768,-6.259124,-6.056328,-7.200222,-3.992027,9.404600,4.177800,9.211076,1.217503,7.608729,3.009219,5.570006,9.123178,9.584834,8.443130,-8.331620,-7.244927,-9.026641,1.161536,-6.312542,5.650662,-6.789529,4.447141,5.668497,-3.660327,-9.042948,0.942044,-9.617771,7.571465,-9.324416,-3.109721,6.488682,6.029115,5.859495,-8.928100,-6.576030,-9.748500,8.792025,-9.951973,-8.656927,6.799503,-8.256238,4.831061,-3.300020,-9.692158,3.380614,2.492602,-9.178547,9.619460,7.286186,5.959407,8.893234,-6.982212,2.828557,7.610928,8.539980,8.537373,8.642981,1.128269,7.290014,-0.554597,-0.962050,1.639372,-0.374719,-4.330073,-9.240623,2.476387,8.533295,-5.279438,9.734785,9.854753,4.262006,-3.054068,8.431617,-0.236668,-5.314139,0.069237,-1.755332,8.476960,4.574874,-2.906398,3.757617,7.488468,0.391790,-3.289841,3.162524,-2.248868,-1.291691,2.891134,-6.663865,-0.837682,-8.037992,5.473033,-7.117106,5.474744,-8.737414,9.776077,-4.665697,5.838611,0.930739,-9.435286,4.358036,9.662774,7.048572,9.978182,-8.772951,-0.365507,9.307347,9.429736,-7.294754,-2.114337,-2.560262,2.644268,-3.679013,-4.500730,-6.977794,9.289507,5.802608,5.801171,6.585814,-5.006620,-1.375131,1.179849,-0.861856], dtype = "float32")#candidate|1464|(4576,)|const|float32
bop_1465 = relay.less_equal(uop_1461.astype('bool'), relay.reshape(const_1464.astype('bool'), relay.shape_of(uop_1461))) # shape=(4576,)
bop_1472 = relay.right_shift(uop_1461.astype('int16'), relay.reshape(bop_1465.astype('int16'), relay.shape_of(uop_1461))) # shape=(4576,)
bop_1479 = relay.equal(uop_1461.astype('bool'), relay.reshape(const_1452.astype('bool'), relay.shape_of(uop_1461))) # shape=(4576,)
output = relay.Tuple([call_1429,call_1443,call_1450,var_1451,const_1453,bop_1472,bop_1479,])
output2 = relay.Tuple([call_1430,call_1444,call_1454,var_1451,const_1453,bop_1472,bop_1479,])
func_1482 = relay.Function([var_1451,], output)
mod['func_1482'] = func_1482
mod = relay.transform.InferType()(mod)
var_1483 = relay.var("var_1483", dtype = "uint8", shape = (416,))#candidate|1483|(416,)|var|uint8
output = func_1482(var_1483)
func_1484 = relay.Function([var_1483], output)
mutated_mod['func_1484'] = func_1484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1504 = relay.TupleGetItem(func_1029_call(), 0)
call_1505 = relay.TupleGetItem(func_1031_call(), 0)
output = relay.Tuple([call_1504,])
output2 = relay.Tuple([call_1505,])
func_1553 = relay.Function([], output)
mod['func_1553'] = func_1553
mod = relay.transform.InferType()(mod)
output = func_1553()
func_1554 = relay.Function([], output)
mutated_mod['func_1554'] = func_1554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_1591 = relay.TupleGetItem(func_782_call(), 2)
call_1592 = relay.TupleGetItem(func_783_call(), 2)
func_1325_call = mod.get_global_var('func_1325')
func_1329_call = mutated_mod.get_global_var('func_1329')
const_1595 = relay.const([-7,8,-4,-7,7,-7,-1,9,10,1,2,6,2,7,-6,-6,1,-8,-6,-1,-10,-3,-5,4,8,7,-1,3,-7,-7,-5,5,-8,-1,9,-7,-2,2,3,-3,5,-3,4,-8,-4,-3,10,5,10,-2,1,10,10,-1,9,-5,3,-9,-2,8,-3,-7,7,-3,-9,8,6,3,9,10,7,2,-3,-7,-1,-3,5,9,3,3,-9,-3,-8,-5,-8,6,-2,5,3,-2,-8,9,4,-9,2,-8,2,9,8,10,-1,-3,-7,10,-2,-4,-5,8,-1,-6,-7,-5,8,1,-8,-1,-7,3,5,-4,4,-9,-1,10,-4,-4,-5,-1,2,8,-3,8,5,6,3,-9,9,9,7,-1,-8,-1,5,7,-4,-5,5,-8,5,10,-5,-8,-9,4,6,4,-2,8,-8,5,9,-2,-5,5,-4,9,-6,-4,2,8,3,4,10,3,9,2,7,-4,-4,-2,6,10,8,4,1,-10,5,-10,-9,2,10,-8,8,9,3,-2,5,-8,7,-7,-5,5,-4,-6,7,-1,-4,1,-2,-3,4,-3,-9,-5,4,-5,10,10,4,-7,6,7,8,1,10,7,1,-6,3,-7,3,8,3,-7,4,7,1,-9,1,1,3,-7,7,3,5,7,-3,3,-2,2,-4,7,4,-6,-5,-10,4,1,3,3,7,7,-6,-5,-5,-6,9,-6,-1,-9,9,5,9,7,3,9,2,7,10,-6,-10,-6,8,-3,4,3,3,9,5,3,9,-5,10,9,-5,-7,-9,-5,2,-6,-2,-4,-9,7,2,-2,-4,10,-1,3,5,-3,2,-3,-6,3,-8,-4,-1,-10,1,-1,-9,8,-3,-5,3,-5,6,9,7,-1,-10,-1,-6,-5,-3,3,-9,-3,3,3,6,1,7,7,4,8,-4,7,2,-8,-10,8,-1,-4,-8,10,-4,-7,9,-7,-3,8,-6,7,7,-2,6,6,8,2,6,2,-1,3,5,4,4,5,-7,7,-10,10,-8,5,-8,-4,9,6,-4,-1,-10,-7,4,-4,8,4,-10,-6,-3,-6,10,-5,5,8,-10,-8,-1,-5,-1,-8,2,-9,-10,-3,-7,-4,-9,5,-8,-3,1,1,10,-1,-6,-2,-2,-3,7,5,-6,-3,6,1,1,6,-9,6,-10,-2,5,-5,6,-9,-5,-9,3,-8,-3,5,-4,8,8,3,-8,-4,-9,-9,-8,-10,-5,8,2,-9,6,9,-6,5,10,2,3,10,-7,-8,9,2,6,4,-5,-5,8,4,2,10,7,7,-7,3,5,-3,-9,10,4,-5,8,1,-5,-2,4,6,-3,1,-1,-6,-8,-1,-1,-4,7,-5,1,-1,-10,-3,4,-6,-4,6,3,-2,-10,-10,5,7,7,-5,5,7,8,10,1,8,2,9,-6,6,5,7,2,-2,-4,-7,4,8,6,-5,-3,10,-8,3,-1,2,-7,-8,2,9,-8,9,-2,5,5,3,-2,5,4,-6,7,3,-8,4,-10,8,-1,9,5,1,1,-8,-9,-6,3,9,1,-5,-10,7,-1,-7,5,8,-7,10,5,4,-2,-6,-2,4,-5,-10,-7,-7,5,3,-10,-10,9,9,-7,-7,-3,4,8,-9,-7,1,8,-2,-4,5,-7,-4,-2,-10,6,-7,-2,2,-9,6,2,9,5,-6,-8,4,-3,-2,1,-3,-3,4,1,7,9,-5,-1,2,8,7,-9,1,-9,-7,9,5,-10,7,-7,9,-10,-8,9,-6,-9,4,2,-8,-10,-1,-4,-9,7,4,-2,1,-9,10,-10,6,-9,-5,-6,4,-1,5,3,-10,9,4,10,3,4,-9,2,-4,-10,4,6,-1,4,2,9,-8,7,2,-9,9,2,8,7,-5,-2,2,8,3,-9,-7,-9,9,-9,5,7,1,-2,-3,2,-6,8,2,-9,-8,-2,-9,2,-8,8,-10,7,-2,2,-8,3,1,-1,-7,-10,1,2,4,5,-6,5,-5,7,1,-3,8,-2,9,-1,-4,-3,-4,4,-8,10,-1,10,-5,-5,8,7,6,-4,3,-1,-8,-5,-9,10,7,1,-5,5,-8,8,10,4,5,1,5,8,-8,8,1,5,8,-7,7,-6,-2,-2,2,-8,-6,-8,3,-4,8,-6,-10,8,-7,4,6,-8,6,1,-8,4,8,-4,-7,-9,2,7,-8,-1,-9,8,5,-6,-8,9,-5,-9,-5,3,-5,1,10,9,-3,3,-7,9,-7,-5,9,-2,-6,-7,-5,-5,5,-8,-1,2,-9,-6,-6,-2,-10,-9,-10,-5,-3,7,5,8,5,-6,5,2,5,-2,-5,-5,3,5,-8,-10,-7,8,-9,3,-2,-2,-6,-1,-4,-1,9,-5,-3,-6,3,1,2,-1,6,7,-2,5,5,9,10,10,8,-2,6,-4,-3,-10,-4,8,-6,6,-3,-5,6,8,4,5,-3,-6,6,-1,-5,-4,3,-9,-6,-6,7,-9,-5,-8,7,2,-2,-1,8,-7,-3,4,-2,3,-7,9,10,6,5,4,-9,9,7,-8,-2,-2,8,8,-6,-10,-2,4,4,-9,3,-10,4,-4,1,-7,-8,7,2,6,8,10,4,4,-3,-9,-8,9,-10,2,6,6,8,-8,1,-10,-9,-1,-6,2,-9,8,-2,7,1,-7,9,-8,7,9,1,6,-10,4,-3,-5,-1,-10,-1,7,8,-10,-7,6,-6,1,2,7,8,10,-2,-4,10,-6,-2,-5,-6,7,-3,7,-8,7,10,4,7,-9,-8,10,6,-1,8,7,10,7,-9,-3,5,-6,3,-2,5,9,-4,-1,6,9,7,8,-1,1,9,4,-3,10,-4,6,6,1,6,-10,-4,-6,4,8,-7,5,2,-2,4,9,-4,5,2,-10,10,1,-9,-4,-1,10,1,5,-7,-8,-9,-8,4,3,-1,-2,-2,-4,-2,-6,3,2,-3,9,6,-4,-4,7,6,-2,4,-8,1,-7,-2,-5,-3,1,5,-8,9,5,-4,1,-4,-7,-1,3,8,-4,-7,5,5,5,-8,-9,5,-10,8,-9,6,-9,2,8,5,10,10,-1,-3,-5,9,10,9,1,3,10,-7,-8,-2,-8,-8,-9,6,-5,6,4,5,-9,5,-2,1,10,10,6,-4,-8,-7,-3,7,-3,-8,-8,10,7,-7,-4,2,8,-1,3,1,10,-8,-10,-10,10,10,3,7,-7,-3,-5,-6,7,7,5,-3,7,-7,-8,10,9,10,-1,-3,1,9,1,1,5,7,-10,-4,-4,4,9,2,3,9,-8,4,8,-9,1,6,10,3,-6,6,9,3,-1,6,-8,-2,9,8,-9,6,-7,-3,6,6,2,-1,2,-9,-1,-9,-3,-3,-6,2,8,-3,-2,3,-2,-1,2,7,8,-7,4,5,-8,2,1,-7,-3,5,9,-3,-8,-7,-8,4,-2,-4,6,4,10,-8,-9,2,-9,7,-7,-9,7,-7,2,-1,-2,-1,-6,4,2,-9,-9,2,9,6,-10,-5,2,-1,3,9,9,-4,6,3,10,-8,4,-8,9,-3,8,-5,-7,-5,10,-6,3,-6,-5,-8,2,3,3,-10,-5,1,-8,4,-5,-8,2,-6,3,5,-2,1,8,-9,-7,-5,-10,4,3,7,-6,4,10,-4,-3,-1,1,-8,-7,-1,-6,5,-3,7,-8,5,-1,3,-1,4,-5,1,-6,6,-8,8,-3,3,3,-3,6,6,-9,1,-7,5,10,9,-7,-1,-3,-2,-1,4,4,-6,5,10,-4,-3,-5,-2,-4,-1,5,-9,-1,7,-5,8,8,2], dtype = "uint64")#candidate|1595|(1440,)|const|uint64
call_1594 = relay.TupleGetItem(func_1325_call(relay.reshape(const_1595.astype('uint64'), [15, 8, 12]), relay.reshape(const_1595.astype('uint64'), [15, 8, 12]), ), 0)
call_1596 = relay.TupleGetItem(func_1329_call(relay.reshape(const_1595.astype('uint64'), [15, 8, 12]), relay.reshape(const_1595.astype('uint64'), [15, 8, 12]), ), 0)
output = relay.Tuple([call_1591,call_1594,const_1595,])
output2 = relay.Tuple([call_1592,call_1596,const_1595,])
func_1612 = relay.Function([], output)
mod['func_1612'] = func_1612
mod = relay.transform.InferType()(mod)
output = func_1612()
func_1613 = relay.Function([], output)
mutated_mod['func_1613'] = func_1613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1626 = relay.TupleGetItem(func_1029_call(), 0)
call_1627 = relay.TupleGetItem(func_1031_call(), 0)
output = call_1626
output2 = call_1627
func_1658 = relay.Function([], output)
mod['func_1658'] = func_1658
mod = relay.transform.InferType()(mod)
output = func_1658()
func_1659 = relay.Function([], output)
mutated_mod['func_1659'] = func_1659
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1668 = relay.var("var_1668", dtype = "uint32", shape = ())#candidate|1668|()|var|uint32
var_1669 = relay.var("var_1669", dtype = "uint32", shape = (1, 4, 9))#candidate|1669|(1, 4, 9)|var|uint32
bop_1670 = relay.add(var_1668.astype('uint32'), var_1669.astype('uint32')) # shape=(1, 4, 9)
bop_1673 = relay.floor_mod(bop_1670.astype('float32'), relay.reshape(var_1669.astype('float32'), relay.shape_of(bop_1670))) # shape=(1, 4, 9)
bop_1679 = relay.mod(bop_1673.astype('float32'), relay.reshape(var_1669.astype('float32'), relay.shape_of(bop_1673))) # shape=(1, 4, 9)
func_1381_call = mod.get_global_var('func_1381')
func_1383_call = mutated_mod.get_global_var('func_1383')
call_1687 = func_1381_call()
call_1688 = func_1381_call()
func_1001_call = mod.get_global_var('func_1001')
func_1004_call = mutated_mod.get_global_var('func_1004')
const_1694 = relay.const([[1.927078,8.357108,8.939574,-4.693690,1.122079,7.893543,-1.842924,-2.683744,-8.121747,-1.702502,-2.100400,8.036114,-1.319501,6.148087,-4.170378,-1.109080,8.835890,-7.394429,-7.723157,-8.205251,3.290529,-9.739160,3.304415,-2.110008,-9.938599,7.946633,6.187266,1.031915,4.010693,-0.845765,2.876290,7.751472,-1.146158,0.295219,-7.345780,-9.849894,3.162279,-6.635388,4.411462,-5.379536,9.088248,0.735921,0.669063,-6.989279,7.090020,-3.453788,2.759600,-9.120043,7.708941,-7.493930,8.017370,6.533950,2.045953,8.880624,-4.745699,4.735782,8.493549,-2.270868,4.900251,-2.520866,-5.688602,1.573170,-5.531824,2.470998,4.871452,-9.013910,0.214837,-2.887922,3.470797,5.145479,6.216964,3.964680,6.725316,3.463582,-9.520826,-0.809037,-3.447754,-8.854989,2.325370,-9.510683,-6.798729,6.791514,-6.758225,-9.324111,-5.093617,8.087990,-2.442137,-7.696188,5.327226,-7.316357,5.311957,-9.381857,-4.527762,9.039844,-1.240461,8.970873,-9.750078,-3.261817,-3.295281,-0.213920,6.005102,-1.563434,-0.218906,9.593823,7.938843,2.920775,-6.561696,-2.095243,-8.669144,-9.763540,-3.445427,7.511018,6.822913,9.231155,9.978245,-2.144947,-2.713119,-8.637411,8.361622,-2.414529],[-6.720665,-7.460391,0.291635,9.338184,-5.896785,-7.799427,5.875054,4.826339,-7.533804,-4.192133,-9.976831,-7.112844,-9.849951,5.543572,-2.544403,-6.637298,7.285133,-1.631570,7.041948,-5.238197,9.246013,-4.906046,9.968978,6.624381,9.180864,6.747932,-4.155323,-4.924557,-6.979729,7.212636,1.885050,5.402111,-9.949217,6.708717,-9.487208,5.031797,-6.286715,-3.074452,1.155289,5.945683,-9.653800,-8.024967,-7.423804,7.670029,-7.443703,-3.433422,-3.742814,-1.849099,4.524255,-8.410599,6.928847,9.171392,-4.464571,9.354488,-0.394143,-7.661744,7.352052,4.445569,0.624561,7.670541,3.886276,5.039052,9.390713,-8.865802,4.224156,-1.351544,-8.595201,-0.587227,-7.535967,-8.014682,5.161889,4.536213,2.313816,-7.379594,1.520014,-2.465731,9.872644,-1.832961,5.670623,3.908612,8.750228,-8.386557,-5.217427,-0.662757,-5.834339,0.942936,4.692937,7.514889,8.083398,3.699178,6.219803,-4.599056,2.488447,6.698093,8.799636,3.073920,9.312052,7.556867,9.980665,-3.381929,-5.758813,3.765880,-6.883457,6.845723,-9.135888,-4.875668,-8.455793,1.228896,9.012321,8.072418,7.838141,3.357100,-9.574387,-4.551169,1.061528,1.753076,-7.940118,1.536034,3.283352,1.374725],[-8.084199,5.972503,-9.546666,-0.224604,-5.028338,-7.287195,2.088126,-5.759573,-6.137746,0.265786,4.275864,-5.936791,6.592017,-3.152126,-4.287440,-7.867981,3.029259,4.067181,-8.219927,3.350705,5.270706,5.986311,9.570205,-0.635922,-6.040150,8.953175,7.499621,-2.134032,-8.561666,0.498561,-2.785442,3.863297,-8.549520,2.841669,-2.514750,4.915579,-4.662786,-5.806782,-5.863164,-6.512960,-8.974931,-7.484052,9.360823,-1.194143,5.047075,-1.285992,-0.291473,1.099623,-9.077268,6.438095,0.581817,3.797316,5.086630,1.063348,-6.062318,0.912185,-7.121047,-5.418637,-2.780869,6.162948,1.968919,8.685997,2.494292,-6.286494,2.567405,-7.301834,-6.680358,-5.340111,-6.445086,5.103591,1.737298,1.293190,-7.474387,7.612367,2.280659,-9.118465,-5.456758,-0.055136,-2.787523,-4.125272,-3.888611,-8.385807,-4.431933,2.360781,-8.731696,4.377783,3.700362,2.660036,8.596234,-0.233338,8.815388,9.796905,-3.451034,8.789740,-0.524258,-9.725062,8.300907,7.651819,4.385602,-3.795732,2.584499,-9.697121,-5.478797,-0.903498,-3.799715,-8.309649,6.234443,-0.626407,9.619704,-4.907703,7.763829,6.297268,7.162861,-0.399900,5.185158,-3.680055,-9.856271,4.888201,3.149063,-2.618939],[-3.863884,8.950071,-2.288159,3.801805,-3.095454,4.757544,-8.601708,-6.537447,4.914322,-2.749235,5.674299,3.659520,8.400178,-0.708000,-0.740702,9.071567,-5.015135,-3.217678,-1.447261,-3.196096,9.008045,-8.218981,-7.071588,1.697398,5.402324,-9.311105,7.427139,-0.670155,-5.858033,3.009398,-5.997492,2.178605,0.681188,7.485253,4.385234,-7.371860,-1.932553,-4.472216,2.162062,-4.272346,-9.551112,2.433334,4.894816,-2.302550,6.004997,-3.374774,-5.902602,-5.293295,-6.020274,1.412629,2.203959,-5.221715,-0.802356,7.506484,2.233553,-1.830929,-8.303808,6.120561,-2.257696,-7.034003,9.500866,3.576944,-9.773372,8.414504,8.376639,9.553004,8.708753,-1.703522,-7.715364,6.939067,-0.217284,9.754581,-7.912983,-9.020691,4.510997,-3.553213,0.792824,-0.174803,8.688984,-6.965467,6.986628,2.052723,-4.254884,-5.084663,8.998810,-1.449376,-5.254746,6.487611,-6.405417,5.146875,-8.396770,-4.890083,7.753437,3.509815,-0.533831,6.895843,3.687468,-1.236410,3.976060,9.648450,5.952285,-2.382131,4.292574,-9.445784,5.979882,1.559086,9.626231,0.886758,4.693194,5.821815,3.865325,3.428211,8.181111,-8.706465,-4.327965,-0.462176,9.292812,6.244663,-0.595476,-3.566455]], dtype = "float64")#candidate|1694|(4, 120)|const|float64
const_1695 = relay.const([8.381322,5.942345,3.900274,-2.603783,-2.825534,-7.474175,-3.042736,-6.318037,-3.708204,-3.824461,4.870367,-3.273842,9.287811,7.564191,7.414618,5.563814,9.780528,2.602570,1.498349,0.223932,0.931767,7.644174,-3.644781,-5.916800,-2.125854,-2.266453,6.115737,8.114445,6.129858,7.485533,5.406853,9.913539,-1.476463,-6.383563,6.333545,3.499353,5.403329,-9.884079,-7.547221,-7.260648,9.017312,-1.820132,2.663000,7.950437,-2.880597,8.792688,1.432937,-6.862772,9.071338,1.032731,0.155985,6.946116,0.495995,-4.006285,5.489141,9.522234,-1.039832,8.709265,4.473230,-7.642186,6.207758,-6.173590,7.943417,-1.526790,5.048644,2.260653,-4.214554,5.044617,-1.414451,6.935027,-0.438282,-6.089295,-4.798751,-1.904732,-1.964274,0.498250,1.185747,-3.373688,1.057376,2.344191,-3.859463,2.510403,-4.025820,-0.045988,-6.850510,-5.946408,-7.358396,1.932291,-2.379609,9.399643,4.552314,-9.321248,-0.274451,3.013156,-3.971005,-6.155407,9.108213,6.683297,-4.591110,-8.282124,-4.373341,1.169876,1.174135,5.780005,-7.479338,-9.059848,-5.669867,-6.740156,3.629031,-1.747360,3.439263,-8.824072,-9.752737,-8.651913,4.642085,5.083800,2.595830,1.798640,-7.444229,-7.856344,5.809236,-8.472062,8.510663,-3.605744,-5.104725,-6.863452,3.602021,-4.696572,5.424207,-7.924922,1.407814,-2.448541,-0.461236,0.624819,-3.457978,6.451071,-2.421398,1.944746,4.425469,-4.613738,-4.946897,4.444804,3.531994,9.901237,-4.440800,8.025946,-9.111554,-4.925411,9.687388,8.908328,8.003981,3.418069,-2.914782,4.174085,-8.419995,0.621106,4.819444,-6.011917,-3.867809,0.986672,7.130133,-5.234240,-0.309971,-4.523591,-8.252470,8.840342,0.629001,5.443648,-6.008772,0.217915,-1.400146,9.493364,1.535873,-4.695020,-8.665963,-4.790480,-7.852657,3.980948,5.415551,0.916959,7.387917,2.034265,0.460452,-3.715416,4.129088,4.734190,-4.568892,9.736039,-0.667424,3.147208,7.208701,4.384647,-8.060614,-4.033095,-3.681225,5.833494,3.262966,-5.144749,4.686346,-3.980915,-2.814372,-6.831842,-6.986627,-9.920313,8.942380,3.179254,0.922855,-2.476493,2.676035,5.675473,-0.107470,6.729475,7.247424,5.171241,-9.466313,-3.693833,1.133416,3.960625,-5.779066,-2.330386,0.993150,3.018056,-5.906194,-3.794970,-0.594328,-7.240104,-5.981537,-7.681916,6.760458,-0.865290,2.975097,4.272033,4.646470,1.721543,-3.374863,2.241795,2.161030,0.397122,7.548712,-4.046020,0.387000,-1.641799,-0.826017,-7.102459,-9.591875,-9.555202,6.383296,-5.776822,-2.174197,-3.164565,-9.142981,9.614622,-8.392245,8.947004,-6.479365,-5.169011,-5.553278,-6.632570,8.068189,4.461349,3.163598,-5.299596,6.581564,-9.497338,-3.542206,-4.016188,-8.239838,-3.053214,-1.550634,-9.286050,6.843389,7.901295,-8.834001,1.693811,-5.140809,8.814008,-2.132090,-3.750778,7.553807,5.692339,2.669193,-5.952387,8.909459,7.470404,-9.789864,1.293559,-7.808556,-3.343610,-0.800884,-5.406114,-6.394900,-5.646079,7.135003,-0.777018,4.856191,-3.666031,4.418795,6.634255,-3.801609,9.178713,-6.663203,-7.703269,0.791333,2.590941,-1.188424,-1.605180,-3.202897,5.011204,2.440443,-6.963762,-0.815471,1.898400,1.955165,-2.865569,7.519053,-7.916839,-8.436449,-0.022679,2.870615,0.518494,-6.359239,-8.497662,1.746558,-0.105337,3.336518,8.201471,-0.965771,-3.626017,3.429263,9.101776,-5.994240,7.286683,-5.728080,-3.907636,3.714273,-9.603246,5.295805,-9.321994,-3.970849,0.841149,2.106214,9.249090,0.173895,0.266740,0.255108,-8.237221,9.039421,-3.646509,6.155413,2.296396,2.138858,-9.048307,3.096011,6.050349,-6.347399,4.404541,7.385479,6.637715,-8.673505,-9.390497,7.424304,1.711338,-7.254876,-4.481056,-0.928613,-2.561504,2.822380,-5.759002,-8.139764,6.622473,-9.238247,-2.903471,4.003892,0.691568,1.306571,6.770619,-2.023729,8.256461,0.209899,-6.584305,5.152735,0.971808,-3.540350,2.583671,5.285076,2.267723,-2.878296,0.215933,4.495994,1.409534,-4.937010,2.494875,-7.399751,0.072504,-3.178541,0.254130,2.024977,9.807831,8.316612,-6.096217,1.117956,-0.511043,4.657274,6.768373,-4.705657,0.134298,-8.579019,1.159797,3.877444,-1.056508,6.152133,-5.380429,-3.426107,-8.799593,-2.781637,-1.222512], dtype = "float32")#candidate|1695|(416,)|const|float32
call_1693 = relay.TupleGetItem(func_1001_call(relay.reshape(const_1694.astype('float64'), [1, 480]), relay.reshape(const_1695.astype('float32'), [8, 13, 4]), ), 2)
call_1696 = relay.TupleGetItem(func_1004_call(relay.reshape(const_1694.astype('float64'), [1, 480]), relay.reshape(const_1695.astype('float32'), [8, 13, 4]), ), 2)
output = relay.Tuple([bop_1679,call_1687,call_1693,const_1694,const_1695,])
output2 = relay.Tuple([bop_1679,call_1688,call_1696,const_1694,const_1695,])
func_1702 = relay.Function([var_1668,var_1669,], output)
mod['func_1702'] = func_1702
mod = relay.transform.InferType()(mod)
var_1703 = relay.var("var_1703", dtype = "uint32", shape = ())#candidate|1703|()|var|uint32
var_1704 = relay.var("var_1704", dtype = "uint32", shape = (1, 4, 9))#candidate|1704|(1, 4, 9)|var|uint32
output = func_1702(var_1703,var_1704,)
func_1705 = relay.Function([var_1703,var_1704,], output)
mutated_mod['func_1705'] = func_1705
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1821 = relay.const([[[0.709530,-0.794682,-2.016074,3.104749,3.484258,-1.202550,6.908808],[4.180734,-9.730329,4.017745,-0.548966,-1.294537,-4.621802,9.810444],[8.422170,7.059437,2.401300,2.674963,-5.557127,-3.572471,5.989681],[5.423987,6.882130,-8.112469,3.562992,-1.962022,4.026758,-3.976903],[-6.888484,-2.020403,-8.040911,3.284396,7.033050,9.222461,2.762358]],[[1.370516,1.734328,5.526069,4.599673,-3.747335,5.279853,4.280046],[-8.421795,-2.224777,1.825327,-1.147391,-5.430112,9.203644,-8.513092],[-0.110865,3.779490,-3.558295,-8.840195,1.039500,1.218788,-7.281130],[-6.798181,-5.246142,7.468239,7.697028,4.608332,-1.192428,8.300708],[5.888997,7.071823,2.325138,-3.103634,3.300681,3.537145,-1.895248]],[[-0.394892,1.302815,-8.816862,3.584286,-9.637906,-0.757434,-5.341712],[-7.925408,0.834788,4.638603,2.800055,9.843629,-8.907718,-2.448154],[8.132816,3.812897,5.944348,-9.491134,-5.913422,7.723576,-7.623575],[-0.634523,-0.238101,3.431014,-5.726074,-4.962086,6.645421,0.685129],[-5.111178,-1.706588,4.726676,-4.584172,-3.928648,-0.875903,-3.780160]],[[-5.816644,-5.488189,-6.790972,5.339905,-7.833612,-0.885766,9.993956],[-0.582526,-1.080066,-1.566241,-1.745501,-4.292839,-9.389352,9.964230],[1.149127,-5.289288,-2.670628,-3.413777,7.240257,-1.265196,7.564978],[4.137104,6.668693,-9.621509,-6.498440,-4.955101,-6.641384,0.292248],[4.651551,4.736369,2.636146,-3.121885,-3.479068,-2.339919,-5.747609]],[[6.186127,7.303520,-4.692650,-4.597031,-4.839424,8.287669,2.354156],[0.612457,-5.499311,4.784683,0.439743,7.292096,2.317004,-8.903652],[-7.376583,-9.319419,7.734438,-2.652480,-7.936365,-5.451459,1.278893],[9.584623,4.816308,-1.373452,-7.540988,1.039127,-5.880179,5.148001],[2.917643,5.303946,9.304681,6.461192,6.787297,-3.253071,5.195235]],[[7.268444,1.393358,2.341476,1.907411,-8.043925,-6.045532,-7.645094],[3.342245,-6.818046,5.088468,-4.598058,0.686337,1.814454,8.497468],[9.121982,-9.588169,5.717931,6.997414,-5.546987,-6.897965,-3.165145],[3.552089,7.145007,3.643848,9.546074,8.441085,1.556645,2.419615],[-5.430241,-4.738542,7.462072,-0.465043,-3.456155,-8.429889,-6.401240]],[[-4.732408,7.648595,7.212685,-8.861849,-9.769060,-7.319426,7.107550],[-7.855614,-2.056068,1.259867,-1.102577,-8.836056,0.526549,2.102323],[7.071151,8.360355,-2.587328,5.776009,3.883086,-5.794674,1.739294],[-8.223387,-8.596004,-6.371329,8.335439,-1.800333,-0.808823,-4.676044],[3.830426,0.655978,5.509297,-1.700846,4.871703,-5.119131,6.764146]],[[-7.153655,2.974994,5.129816,-0.650034,-3.101282,5.064457,7.279702],[0.004063,-4.698081,2.690725,-9.920178,-2.437545,6.200143,-6.279185],[-1.434116,-3.097100,6.529778,3.917610,-5.236776,-1.613817,4.893494],[7.335787,6.133966,-0.662714,9.149427,-5.801402,0.749247,3.993783],[-7.547059,-4.044307,7.376307,-1.985848,-6.651035,-6.627645,2.316184]],[[2.560073,-7.474237,3.063252,-9.120362,7.857163,-2.849722,6.744038],[-9.052417,-2.786772,-1.531915,-1.144002,5.710428,-6.305484,-3.987328],[-7.864820,9.966678,7.028923,-8.232564,-8.082178,-5.967144,7.773082],[8.924897,-7.517949,7.958978,-2.717917,1.718619,5.446050,9.896751],[-8.540083,-2.965025,1.500814,6.084721,-1.056632,-9.832353,-8.006594]],[[-6.609635,6.597580,-7.098295,-9.251320,-6.497134,7.369899,1.797450],[-9.139421,8.962299,-4.055059,-1.412474,6.384799,-9.436004,4.229560],[-2.998804,-1.734247,6.996549,-2.223341,9.144702,9.566839,-3.255840],[-1.953497,-5.741386,-7.322481,7.533301,2.862248,7.962312,6.898456],[-5.847795,-1.023527,-7.601230,-5.804311,-7.897071,6.650679,1.192187]],[[5.364939,-0.882093,7.564885,-8.796810,-4.038086,-6.082237,4.176970],[-4.414395,-8.237152,-1.167615,-5.278898,2.069822,-1.026862,7.509247],[5.975044,0.861709,-1.668639,-1.070224,-9.514177,-6.580447,5.493645],[-7.721908,-5.530748,2.482918,-1.770442,0.717093,3.620890,6.315023],[-0.188564,1.785596,9.369496,-1.357418,-0.848694,4.293212,5.758877]],[[1.554189,-6.520719,-4.725004,8.641163,7.367059,1.421424,-8.640971],[5.227743,-5.205628,-6.941490,-3.364156,-5.211510,-4.043762,1.063042],[5.847826,1.406808,3.178658,9.452306,-1.011798,-2.426881,-5.592031],[-6.087361,-3.175408,-8.790041,7.187525,-1.839268,-1.344831,-6.988219],[-9.359791,-0.311421,-8.483867,-7.506350,6.498519,4.883642,-7.598072]]], dtype = "float32")#candidate|1821|(12, 5, 7)|const|float32
uop_1822 = relay.log(const_1821.astype('float32')) # shape=(12, 5, 7)
uop_1829 = relay.atanh(const_1821.astype('float32')) # shape=(12, 5, 7)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_1831 = func_318_call()
call_1832 = func_318_call()
output = relay.Tuple([uop_1822,uop_1829,call_1831,])
output2 = relay.Tuple([uop_1822,uop_1829,call_1832,])
func_1837 = relay.Function([], output)
mod['func_1837'] = func_1837
mod = relay.transform.InferType()(mod)
output = func_1837()
func_1838 = relay.Function([], output)
mutated_mod['func_1838'] = func_1838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_800_call = mod.get_global_var('func_800')
func_801_call = mutated_mod.get_global_var('func_801')
call_1855 = relay.TupleGetItem(func_800_call(), 0)
call_1856 = relay.TupleGetItem(func_801_call(), 0)
uop_1865 = relay.sigmoid(call_1855.astype('float64')) # shape=(8, 13, 4)
uop_1867 = relay.sigmoid(call_1856.astype('float64')) # shape=(8, 13, 4)
func_667_call = mod.get_global_var('func_667')
func_670_call = mutated_mod.get_global_var('func_670')
const_1870 = relay.const([[-4.332491,-9.144411,8.012664,5.806081,3.031606,8.165079,-3.283681,-8.048455,-9.143151,-4.852667,-0.641238,7.690400,7.821132,-6.901550,0.614784,-6.558458],[5.189627,-2.955905,6.494955,5.875663,-8.046378,9.222490,-0.741357,8.262888,3.176057,5.926013,7.993697,-0.394139,7.630754,-5.412108,-1.986689,7.077084],[3.905848,2.872948,6.155911,-3.394847,0.839679,4.544083,3.833944,-0.099050,-7.863774,8.230308,-9.314767,-6.145385,-3.350569,9.585002,-8.350499,-5.218279],[-0.567063,-7.955537,-0.976989,8.624846,8.589209,-5.923005,8.762495,8.895234,-5.440472,-6.079418,-3.077701,2.949662,3.832356,-9.773346,7.816573,-1.600567],[-6.506847,5.445181,0.074316,-4.105340,8.506767,0.633608,0.923175,-0.101602,7.132117,-5.493779,-1.719953,-0.050209,-3.671975,4.643914,-6.749620,0.752711],[-9.663757,2.895217,8.619058,-3.756750,-8.599306,-5.194073,-5.663766,-9.039396,7.201917,-2.105941,-5.504358,2.849336,2.059902,-9.428137,-9.661958,-9.737620],[-9.622967,-5.634765,9.558888,9.948854,2.479907,7.351929,-5.511205,2.727605,-0.514426,5.243156,0.814358,-4.479076,1.245608,-4.677411,-8.317704,3.235587],[-5.859945,0.550559,-6.491065,-2.599777,-8.725591,-6.125672,0.721745,-3.941835,6.622720,-2.367290,-4.547131,9.548170,4.761898,-7.952722,-1.693405,-0.492969],[2.415990,-0.565673,-8.526856,1.417372,-3.551198,-0.912290,-9.665333,0.835314,-2.737994,-2.791555,-4.915056,1.989771,1.456316,-8.015282,1.966200,-3.240058],[-1.078445,-0.385623,0.255371,2.748202,7.881184,6.042494,-3.107883,4.539282,-6.687776,3.843090,4.586363,-4.622676,-2.985591,-5.906542,-4.956444,0.142473],[0.635741,6.969963,7.036816,-6.536499,-1.976008,-7.428071,8.321684,-6.692886,4.052706,-9.559488,-4.558592,1.519132,0.523793,-5.704592,0.794162,-4.376339],[9.068156,3.898913,-7.715094,-0.962934,-4.756134,1.464345,-7.152897,1.732535,-9.766647,8.183093,6.429745,4.544247,-3.078866,-5.356357,5.972299,8.399742],[-0.338975,-4.820547,-2.661898,-1.305169,5.655320,-7.798333,7.868499,-4.378393,-9.332340,-4.138680,-6.185870,-3.832994,1.574319,-3.230457,-8.398624,9.554066],[4.141479,8.637838,-2.248670,-5.958519,-3.680168,-0.586305,-3.642258,7.511871,-3.619564,-2.504993,0.642129,3.064474,5.308237,-2.999681,0.556370,5.667370],[7.343772,5.648179,-6.795850,0.340530,-5.332925,-1.436727,-1.774565,7.012350,1.996851,-4.705982,5.359012,7.452709,2.055350,-9.852735,6.712439,4.238885],[-1.663434,4.631093,-0.534564,9.987666,-8.034721,-2.172513,6.877343,2.317980,2.896052,-4.824615,7.191959,-7.540009,6.583572,-1.681613,-4.147269,6.504317]], dtype = "float32")#candidate|1870|(16, 16)|const|float32
call_1869 = relay.TupleGetItem(func_667_call(relay.reshape(const_1870.astype('float32'), [256,])), 2)
call_1871 = relay.TupleGetItem(func_670_call(relay.reshape(const_1870.astype('float32'), [256,])), 2)
func_1381_call = mod.get_global_var('func_1381')
func_1383_call = mutated_mod.get_global_var('func_1383')
call_1873 = func_1381_call()
call_1874 = func_1381_call()
bop_1885 = relay.logical_xor(uop_1865.astype('uint64'), relay.reshape(call_1855.astype('uint64'), relay.shape_of(uop_1865))) # shape=(8, 13, 4)
bop_1888 = relay.logical_xor(uop_1867.astype('uint64'), relay.reshape(call_1856.astype('uint64'), relay.shape_of(uop_1867))) # shape=(8, 13, 4)
func_1482_call = mod.get_global_var('func_1482')
func_1484_call = mutated_mod.get_global_var('func_1484')
call_1894 = relay.TupleGetItem(func_1482_call(relay.reshape(call_1855.astype('uint8'), [416,])), 0)
call_1895 = relay.TupleGetItem(func_1484_call(relay.reshape(call_1855.astype('uint8'), [416,])), 0)
func_77_call = mod.get_global_var('func_77')
func_81_call = mutated_mod.get_global_var('func_81')
call_1905 = func_77_call(relay.reshape(uop_1865.astype('uint8'), [8, 13, 4]), relay.reshape(uop_1865.astype('uint8'), [8, 13, 4]), )
call_1906 = func_77_call(relay.reshape(uop_1865.astype('uint8'), [8, 13, 4]), relay.reshape(uop_1865.astype('uint8'), [8, 13, 4]), )
output = relay.Tuple([call_1869,const_1870,call_1873,bop_1885,call_1894,call_1905,])
output2 = relay.Tuple([call_1871,const_1870,call_1874,bop_1888,call_1895,call_1906,])
func_1911 = relay.Function([], output)
mod['func_1911'] = func_1911
mod = relay.transform.InferType()(mod)
output = func_1911()
func_1912 = relay.Function([], output)
mutated_mod['func_1912'] = func_1912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1612_call = mod.get_global_var('func_1612')
func_1613_call = mutated_mod.get_global_var('func_1613')
call_1941 = relay.TupleGetItem(func_1612_call(), 1)
call_1942 = relay.TupleGetItem(func_1613_call(), 1)
output = call_1941
output2 = call_1942
func_1943 = relay.Function([], output)
mod['func_1943'] = func_1943
mod = relay.transform.InferType()(mod)
mutated_mod['func_1943'] = func_1943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1943_call = mutated_mod.get_global_var('func_1943')
call_1944 = func_1943_call()
output = call_1944
func_1945 = relay.Function([], output)
mutated_mod['func_1945'] = func_1945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1911_call = mod.get_global_var('func_1911')
func_1912_call = mutated_mod.get_global_var('func_1912')
call_1971 = relay.TupleGetItem(func_1911_call(), 0)
call_1972 = relay.TupleGetItem(func_1912_call(), 0)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_1980 = func_318_call()
call_1981 = func_318_call()
func_1325_call = mod.get_global_var('func_1325')
func_1329_call = mutated_mod.get_global_var('func_1329')
var_1983 = relay.var("var_1983", dtype = "uint64", shape = (1440,))#candidate|1983|(1440,)|var|uint64
call_1982 = relay.TupleGetItem(func_1325_call(relay.reshape(var_1983.astype('uint64'), [15, 8, 12]), relay.reshape(var_1983.astype('uint64'), [15, 8, 12]), ), 0)
call_1984 = relay.TupleGetItem(func_1329_call(relay.reshape(var_1983.astype('uint64'), [15, 8, 12]), relay.reshape(var_1983.astype('uint64'), [15, 8, 12]), ), 0)
output = relay.Tuple([call_1971,call_1980,call_1982,var_1983,])
output2 = relay.Tuple([call_1972,call_1981,call_1984,var_1983,])
func_1989 = relay.Function([var_1983,], output)
mod['func_1989'] = func_1989
mod = relay.transform.InferType()(mod)
var_1990 = relay.var("var_1990", dtype = "uint64", shape = (1440,))#candidate|1990|(1440,)|var|uint64
output = func_1989(var_1990)
func_1991 = relay.Function([var_1990], output)
mutated_mod['func_1991'] = func_1991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1993 = relay.TupleGetItem(func_1029_call(), 0)
call_1994 = relay.TupleGetItem(func_1031_call(), 0)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_1995 = relay.TupleGetItem(func_1075_call(), 2)
call_1996 = relay.TupleGetItem(func_1076_call(), 2)
output = relay.Tuple([call_1993,call_1995,])
output2 = relay.Tuple([call_1994,call_1996,])
func_2011 = relay.Function([], output)
mod['func_2011'] = func_2011
mod = relay.transform.InferType()(mod)
mutated_mod['func_2011'] = func_2011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2011_call = mutated_mod.get_global_var('func_2011')
call_2012 = func_2011_call()
output = call_2012
func_2013 = relay.Function([], output)
mutated_mod['func_2013'] = func_2013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1943_call = mod.get_global_var('func_1943')
func_1945_call = mutated_mod.get_global_var('func_1945')
call_2030 = func_1943_call()
call_2031 = func_1943_call()
func_1612_call = mod.get_global_var('func_1612')
func_1613_call = mutated_mod.get_global_var('func_1613')
call_2052 = relay.TupleGetItem(func_1612_call(), 0)
call_2053 = relay.TupleGetItem(func_1613_call(), 0)
func_1211_call = mod.get_global_var('func_1211')
func_1215_call = mutated_mod.get_global_var('func_1215')
const_2065 = relay.const([3.662443,-1.436035,4.343513,-1.305273,9.380189,-1.098679,-7.249522,9.109172,1.092480,-6.420459,-8.353082,-4.519976,2.850055,-1.069428,-3.523532,-6.668482,-0.997464,-3.171384,-9.389716,2.284723,4.750935,-1.226626,-6.024174,2.930575,-0.465332,7.183487,-7.791651,-1.389983,-9.192448,-9.444355,-3.798837,-0.463484,8.359553,-7.017894,6.464890,5.354491,2.720374,-2.131300,3.466390,5.245181,4.696834,2.455792,-3.133810,-8.483357,-2.472691,-8.529069,3.066146,-6.913043,9.318259,-3.366974,-9.618489,5.783117,2.840236,-0.785251,2.318949,-2.415375,-6.065361,-8.287784,8.747317,5.763752,-1.383580,-2.827187,-0.184149,-9.783816,7.872037,-7.347596,0.271902,-9.551554,-6.583638,1.249054,-0.034727,-7.983585,9.606482,-6.569897,6.645055,3.737753,2.646611,7.128898,-4.237092,0.285104,-5.192767,3.818168,-8.636817,7.218002,-6.597554,-0.574257,-9.038830,-3.526132,-9.204774,2.426736,-2.322371,7.835236,-7.843252,-5.812563,-2.820578,0.263766,9.855470,-8.974629,-9.557040,-5.451560,6.431721,0.117333,-1.546906,2.253757,-0.142774,-0.739504,6.084420,-8.210842,7.975357,-4.690966,3.445178,-0.794610,5.606910,-3.279949,-0.600726,-6.719036,3.878464,-6.913517,4.476752,-3.833209,-1.505312,8.183255,-6.881729,9.061883,-8.474125,-3.737897,9.172673,-6.918688,7.912168,-4.156864,-6.840524,4.477102,4.031823,0.469645,-5.589833,-4.540342,-4.122111,-4.858513,-0.156758,-5.669494,-0.968885,-2.482702,-3.718630,-7.142282,8.020406,2.142899,7.950049,3.119203,-2.565187,-0.361265,8.637076,2.766433,-0.050905,-8.496131,-4.868429,2.144410,0.026842,-2.687392,-8.169977,-6.457061,-7.017945,4.997316,-8.216648,-2.932798,1.915108,4.032350,2.048326,1.123420,6.066919,-7.342875,-5.218567,-4.146489,5.344321,4.549634,3.217153,5.348192,-1.560501,4.136268,-2.096781,3.350407,-0.647462,-4.959661,-3.314384,0.889587,7.306307,6.540744,9.826488,-6.807887,-3.335857,0.339813,2.647323,4.479852,4.142605,-4.771952,-8.175870,-5.258873,4.299471,7.006198,-1.493720,9.986306,-5.297218,4.173191,-0.511619,4.257563,-8.029670,-5.218893,8.149316,3.838555,-2.156535,-3.751008,9.822377,-8.116029,3.512020,-8.686325,-9.113314,-5.032683,-5.206237,8.635109,2.261498,-3.567710,7.485880,2.641395,-1.235236,2.497628,-7.880975,-6.469671,-9.097996,-1.751047,-0.678832,4.921020,-8.891640,8.810823,-6.155051,2.168881,4.243492,2.064875,-4.255935,-9.633056,7.848320,-7.919374,3.758087,9.539221,6.142298,-4.350181,1.565358,-5.157118,1.584292,-2.018806,-4.376942,9.982852,7.843139,-8.012009,8.630531,0.357709,5.017002,-5.026121,-8.738806,-4.892076,-8.315540,8.371195,7.108676,1.622102,4.750823,-6.245713,-4.190402,-3.635431,-4.065682,4.484790,6.587503,-0.727982,-3.240157,3.126990,-8.248202,-5.710991,-1.097549,-7.883393,-3.169816,-2.501990,-5.001631,3.476553,-9.661601,-0.840520,6.806440,-2.392010,-8.265187,4.231009,-0.542423,4.586943,-2.054504,9.122885,3.950520,-8.955394,5.802743,-1.768159,7.505441,-3.389887,4.020608,-9.267374,2.948573,2.830783,5.687633,-6.471800,0.871081,5.427894,-7.499612,5.909420,-1.619841,7.423693,-8.429915,7.896050,9.158697,-9.325188,8.199250,3.618079,3.677797,-7.926123,6.492390,-6.988842,8.721901,4.480526,-2.247413,5.286784,-9.700450,1.906753,-8.373019,6.048019,-3.428423,-8.063964,-8.790140,-4.244250,-5.743615,4.842933,-6.110118,3.877310,8.897426,4.938895,2.265318,-7.067001,8.962685,-5.670850,5.178479,5.349692,8.256607,1.176802,-4.496316,-1.083706,-4.273125,-5.166679,6.201513,-1.352949,-6.260154,9.179430,5.211505,-8.148572,5.372272,-6.718763,-0.595477,-4.933579,-1.731397,6.587798,-4.263787,9.697526,5.738162,1.090072,6.234350,8.143844,7.529644,3.680148,6.656769,6.128707,8.049485,2.234809,2.316081,3.098015,8.409074,-9.116597,-5.539555,-5.137932,-7.894069,3.737213,-4.940945,3.586072,9.623681,-6.073958,-4.259656,9.073978,5.349547,8.678339,-5.416292,-0.406564,-7.803566,6.383933,8.794033,-6.094048,9.845189,3.373824,9.055319,6.322640,-2.313301,6.717637,7.128087,-6.166135,7.516043,-0.807127,-1.105350,3.205300,8.358146,-0.460731,-6.378737,-1.180558,-9.108122,6.482480,7.910872,-5.683862,-6.506324,-6.809759,-6.199842,6.507834,0.796511,7.699975,-2.733803,-2.919198,-3.759862,-1.580319,8.651974,-8.543211,9.270597,0.514885,7.709291,-7.854839,3.162063,9.105566,8.922929,5.474130,-3.244030,-4.719929,0.179803,1.358314,4.694618,5.788900,-6.889571,-7.379492,1.749768,-4.728726,2.015901,3.444458,-7.222851,-5.022511,2.018383,-6.033807,0.430101,-6.640613,8.296451,-8.753819,-4.522253,4.778284,5.365052,-3.541919,-9.329283,9.565440,3.102514,-7.167312,-4.915493,3.225033,9.948648,3.914869,-3.513861,4.489650,3.894175,3.468824,1.401074,0.306242,-1.426729,-9.479081,-6.808002,2.674226,-2.955928,9.813541,-7.179499,-0.252523], dtype = "float64")#candidate|2065|(480,)|const|float64
call_2064 = relay.TupleGetItem(func_1211_call(relay.reshape(const_2065.astype('float64'), [120, 4]), relay.reshape(call_2052.astype('float32'), [416,]), ), 4)
call_2066 = relay.TupleGetItem(func_1215_call(relay.reshape(const_2065.astype('float64'), [120, 4]), relay.reshape(call_2052.astype('float32'), [416,]), ), 4)
output = relay.Tuple([call_2030,call_2052,call_2064,const_2065,])
output2 = relay.Tuple([call_2031,call_2053,call_2066,const_2065,])
func_2082 = relay.Function([], output)
mod['func_2082'] = func_2082
mod = relay.transform.InferType()(mod)
output = func_2082()
func_2083 = relay.Function([], output)
mutated_mod['func_2083'] = func_2083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_2106 = relay.TupleGetItem(func_1075_call(), 2)
call_2107 = relay.TupleGetItem(func_1076_call(), 2)
func_1482_call = mod.get_global_var('func_1482')
func_1484_call = mutated_mod.get_global_var('func_1484')
const_2119 = relay.const([[-8,-8,-7,7,3,7,-10,-6,-1,-3,8,1,-2,10,4,3,-8,-10,-8,-2,-8,3,-10,-6,-7,-1,-10,-10,1,-8,-5,6,3,-10,-10,2,-1,-7,-5,1,-4,6,5,6,8,-8,6,4,-9,-10,7,8,-8,-9,9,-4,4,-9,-10,4,9,-8,-5,6,-9,4,10,-5,8,3,6,2,-1,-7,-6,-6,-5,1,7,6,4,1,2,4,10,7,7,5,10,7,-5,2,7,9,-9,-1,5,-6,-6,6,8,-1,7,-2],[-8,-5,-4,-10,-8,-7,4,-9,10,5,-4,3,6,-8,9,-10,-1,-1,-1,7,2,6,4,2,-9,-9,7,8,5,8,7,3,2,4,5,-3,-7,-2,4,-4,-2,-9,-4,-6,-2,3,2,-9,9,8,-5,2,9,5,-9,-8,2,2,4,-7,2,-8,-5,9,-8,-10,9,7,8,-3,10,10,9,-10,-1,9,-4,-8,-4,4,5,5,8,3,-3,-2,8,-5,-3,-1,-1,-10,7,-5,-6,-3,7,-6,-1,8,7,-6,-2,-3],[-7,1,-5,4,-8,5,2,-6,5,1,-3,1,-10,5,10,-9,10,-7,-1,-9,2,3,-9,2,-3,3,3,-5,10,5,8,9,3,5,8,3,5,5,-6,-9,3,6,5,-1,3,-5,9,1,1,-6,-7,1,4,7,7,1,-9,6,-10,6,-2,-6,-4,-2,2,-4,-8,2,-2,-4,-6,-9,-3,6,-9,-9,-3,3,-2,2,5,-3,-2,-5,-6,5,5,5,-8,-3,3,-9,9,-4,7,4,-6,4,-4,4,9,1,3,6],[-7,10,3,8,3,10,10,1,1,-5,6,4,-1,3,-3,7,8,-1,9,2,1,-2,-5,8,10,-2,3,6,-3,7,-8,5,4,-6,5,-6,9,7,3,-2,9,3,-2,-7,8,10,-10,3,-2,8,-8,-2,-4,-4,6,-2,-2,6,-4,8,7,-1,4,3,-4,3,-7,2,6,10,2,5,-7,-7,-6,-6,-2,1,2,3,-5,9,-1,-3,6,7,5,3,6,6,4,4,8,3,-9,7,5,4,-8,-3,8,4,5,-7]], dtype = "uint8")#candidate|2119|(4, 104)|const|uint8
call_2118 = relay.TupleGetItem(func_1482_call(relay.reshape(const_2119.astype('uint8'), [416,])), 4)
call_2120 = relay.TupleGetItem(func_1484_call(relay.reshape(const_2119.astype('uint8'), [416,])), 4)
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
const_2126 = relay.const([[10],[2],[3],[-8],[1],[-9],[-7],[-4],[2],[9],[3],[-8],[1],[10],[10],[4],[7],[10],[7],[-8],[-4],[-5],[7],[-3],[3],[-4],[9],[3],[-4],[5],[-8],[-3],[-4],[6],[5],[-4],[-1],[1],[8],[7],[-7],[8],[-3],[-7],[7],[-2],[-1],[-1],[-2],[-10],[2],[-7],[3],[-3],[3],[2],[10],[-7],[4],[-3],[-5],[7],[2],[5],[-6],[-10],[-1],[3],[6],[-4],[-7],[10],[-8],[-2],[2],[-3],[-10],[5],[10],[-7],[-6],[-7],[5],[-10],[-8],[-1],[-3],[-2],[-7],[-5],[-10],[6],[-1],[-4],[-2],[9],[8],[-7],[-6],[4],[-3],[8],[-6],[-9],[5],[-4],[4],[-6],[2],[8],[-1],[-3],[3],[-1],[-9],[4],[2],[10],[-2],[-2],[4],[-1],[3],[-5],[-7],[10],[2],[-6],[5],[7],[-4],[8],[4],[-3],[6],[3],[-9],[-10],[4],[-1],[2],[9],[-7],[10],[-2],[-8],[7],[2],[3],[-8],[-3],[8],[-7],[-6],[6],[2],[-9],[2],[5],[9],[-9],[4],[4],[-7],[-5],[5],[8],[-10],[4],[4],[5],[7],[-6],[-1],[-1],[8],[9],[7],[-2],[-10],[1],[-5],[-3],[-2],[2],[8],[-3],[-9],[-6],[-9],[3],[8],[-9],[-5],[1],[-8],[-5],[9],[-7],[-6],[8],[-4],[2],[9],[-6],[-6],[4],[-10],[9],[4],[3],[10],[4],[-5],[-2],[-7],[8],[1],[-7],[-8],[7],[-1],[-8],[-5],[-6],[-6],[-10],[8],[-6],[4],[5],[-8],[5],[1],[-10],[-6],[-2],[7],[9],[6],[-1],[-6],[-7],[-7],[-7],[-4],[-6],[-3],[2],[4],[4],[-8],[-6],[6],[-8],[-1],[-3],[2],[-1],[-6],[3],[9],[2],[10],[-8],[7],[-4],[-10],[-3],[6],[-9],[2],[3],[-3],[-6],[3],[8],[-7],[-3],[-6],[1],[5],[-10],[6],[1],[5],[-8],[-3],[3],[-7],[6],[-6],[-9],[-9],[-2],[-5],[10],[-8],[7],[4],[-5],[-10],[-7],[6],[-1],[-7],[-3],[5],[8],[6],[1],[-4],[-3],[1],[-8],[8],[5],[-8],[10],[-2],[-9],[10],[-4],[3],[1],[3],[-1],[10],[9],[4],[8],[3],[-7],[-8],[9],[10],[1],[-1],[6],[-8],[-5],[8],[-9],[-2],[2],[8],[-5],[5],[-5],[2],[3],[3],[3],[10],[10],[-8],[-10],[-3],[-9],[-7],[-10],[-2],[7],[-8],[2],[-6],[2],[-10],[5],[-4],[-7],[-2],[-3],[6],[-1],[-2],[8],[-7],[-3],[5],[4],[10],[-3],[1],[-8],[3],[-1],[4],[1],[3],[-3],[-4],[-9],[5],[-5],[-5],[4],[-5],[6],[4],[-2],[1],[3],[7],[-7],[7],[-5],[2],[1],[6],[-10],[7],[8],[2],[9],[-8],[-5],[6],[8],[6],[-4],[-5],[6],[-3],[-7],[-7],[9],[2],[5],[9],[-1],[8],[-10],[6],[10],[3],[-6],[2],[-8],[-1],[1],[-1],[-9],[8],[-6],[-9],[-6],[5],[-3],[-3],[-2],[4],[-7],[-10],[-1],[-9],[6],[-3],[-4],[10],[-7],[-8],[-7],[-10],[3],[-1],[2],[-3],[-4],[-5],[3],[-7],[5],[-3],[-10],[2],[3],[2],[-5],[2],[10],[5],[3],[-2],[-2],[-1],[-10],[-3],[6],[-5],[-10],[-4],[6],[-6],[-10],[1],[2],[-3],[-3],[-1],[9],[-9],[8],[-3],[7],[-3],[-2],[-1],[-4],[-1],[5],[-6],[7],[3],[4],[4],[-6],[10],[2],[-10],[-1],[5],[3],[6],[-5],[4],[9],[9],[1],[6],[6],[9],[-1],[-5],[4],[2],[-10],[1],[-7],[1],[-3],[3],[8],[8],[4],[5],[1],[9],[4],[-5],[-9],[4],[-5],[3],[9],[3],[-2],[4],[8],[9],[5],[9],[7],[8],[-2],[-10],[1],[2],[-8],[-6],[-2],[8],[5],[2],[-5],[3],[-5],[6],[2],[3],[-8],[-9],[-6],[2],[8],[10],[-9],[2],[2],[7],[-4],[-7],[-5],[-1],[6],[3],[1],[-2],[-2],[1],[-4],[-10],[3],[9],[5],[-5],[6],[-8],[-7],[-10],[-4],[-9],[-6],[2],[-5],[8],[7],[-4],[-9],[8],[-7],[-2],[6],[-4],[8],[-6],[-6],[9],[-3],[-9],[-7],[-10],[6],[-7],[-7],[8],[-7],[-8],[10],[-6],[5],[-3],[6],[-4],[5],[1],[-2],[-8],[-7],[3],[9],[9],[-2],[1],[-9],[10],[-10],[7],[-7],[6],[4],[-5],[8],[-5],[8],[8],[-7],[-5],[4],[-1],[-4],[6],[-4],[-1],[4],[4],[-7],[-2],[-4],[-10],[3],[2],[-7],[-1],[5],[-3],[-2],[7],[4],[8],[7],[3],[3],[-9],[-2],[-1],[-10],[-9],[2],[-7],[1],[-7],[3],[-1],[-2],[-4],[-1],[3],[4],[-10],[2],[3],[4],[9],[1],[4],[8],[-5],[5],[-9],[-4],[-8],[-1],[8],[-4],[4],[-2],[7],[1],[6],[4],[4],[-1],[-4],[-6],[5],[-7],[5],[-5],[-7],[-3],[-4],[10],[-5],[-7],[-4],[8],[4],[6],[6],[-2],[-2],[-6],[-9],[9],[-8],[7],[-9],[3],[-9],[-2],[-3],[9],[-2],[5],[9],[-10],[6],[-7],[7],[-9],[6],[8],[2],[-9],[6],[-3],[6],[6],[9],[7],[-9],[-10],[-5],[10],[-10],[-10],[4],[4],[-1],[-8],[-6],[6],[5],[9],[5],[3],[-3],[1],[-9],[-9],[-1],[-9],[-6],[4],[6],[4],[4],[-4],[-2],[-2],[-7],[3],[9],[7],[4],[-1],[4],[9],[-1],[-9],[4],[10],[3],[-7],[-5],[4],[-6],[-1],[10],[7],[3],[-8],[-7],[8],[1],[-6],[-3],[4],[-8],[-3],[-10],[4],[-5],[-4],[-2],[-8],[8],[3],[4],[-3],[1],[3],[-6],[1],[8],[7],[-4],[-7],[-8],[3],[-10],[7],[8],[3],[-3],[8],[-8],[9],[-8],[7],[8],[-5],[9],[-1],[-10],[8],[-5],[10],[-7],[7],[1],[-6],[-8],[4],[7],[3],[7],[8],[-1],[4],[-1],[-3],[-7],[4],[-10],[-4],[10],[-2],[4],[6],[7],[-9],[-9],[-2],[-5],[-2],[-9],[5],[-2],[10],[1],[2],[3],[-8],[2],[-2],[-5],[-5],[9],[-7],[-8],[-1],[5],[-4],[4],[-8],[-9],[4],[6],[1],[-10],[-9],[6],[-1],[3],[-7],[6],[7],[3],[-8],[-7],[-2],[9],[-8],[-2],[5],[2],[6],[7],[-2],[5],[3],[-7],[-3],[-4],[-7],[-7],[7],[7],[-3],[4],[10],[3],[3],[3],[-2],[3],[10],[-10],[10],[3],[-6],[8],[-8],[-9],[-5],[-2],[-7],[3],[5],[-5],[4],[4],[10],[6],[9],[7],[2],[7],[10],[3],[-8],[-2],[-10],[-7],[9],[-1],[10],[9],[-1],[-9],[-4],[4],[-2],[6],[-10],[9],[3],[-3],[6],[-7],[-9],[-10],[-8],[-10],[3],[9],[-6],[3],[-7],[-3],[-9],[-3],[6],[5],[-5],[7],[-5],[-5],[-7],[1],[-6],[9],[-3],[-1],[-3],[-7],[7],[-5],[5],[4],[-4],[-6],[-7],[1],[-5],[6],[-1],[5],[-7],[-6],[1],[1],[3],[-2],[5],[10],[7],[10],[6],[10],[4],[-5],[8],[10],[-6],[-8],[-2],[-8],[6],[-7],[6],[-2],[-5],[6],[6],[5],[1],[4],[3],[7],[-4],[8],[-3],[-1],[6],[9],[7],[-6],[-6],[4],[-8],[1],[-2],[-9],[10],[-4],[-10],[-10],[-1],[-1],[1],[1],[-3],[-10],[9],[10],[-4],[9],[7],[1],[-3],[-2],[9],[5],[5],[7],[5],[-5],[4],[7],[9],[3],[8],[1],[9],[3],[-7],[4],[-8],[-6],[-4],[-10],[10],[9],[-9],[9],[4],[3],[-5],[9],[6],[-5],[-10],[-1],[-9],[-3],[9],[-4],[-9],[4],[9],[-7],[-9],[-7],[7],[-8],[2],[8],[-6],[8],[5],[10],[5],[4],[7],[1],[3],[-1],[10],[-7],[-5],[-10],[10],[-7],[-4],[-4],[8],[-2],[8],[-6],[-3],[-2],[-7],[-1],[10],[4],[6],[-2],[-9],[-5],[-6],[1],[-10],[9],[-8],[-4],[-4],[-1],[9],[7],[-1],[7],[-2],[-4],[-10],[3],[7],[-1],[8],[7],[-7],[-1],[9],[-9],[4],[-10],[-7],[-2],[7],[-10],[-6],[-4],[9],[-10],[-7],[7],[9],[-4],[-1],[-9],[-1],[2],[7],[4],[2],[1],[-9],[1],[-4],[6],[-9],[5],[2],[6],[-4],[-6],[3],[2],[-4],[4],[-2],[-3],[1],[8],[-6],[-7],[7],[3],[-3],[1],[-4],[-2],[-7],[-9],[-1],[-8],[-9],[4],[7],[-5],[6],[8],[-8],[-3],[9],[-8],[-2],[-2],[-7],[3],[-3],[2],[2],[-3],[-8],[1],[-2],[7],[7],[-1],[-3],[1],[-1],[8],[5],[5],[10],[1],[-3],[-10],[5],[-5],[8],[7],[10],[-4],[-8],[2],[-2],[-9],[-2],[7],[4],[-6],[4],[-8],[-5],[6],[-2],[3],[-2],[9],[-3],[-1],[-1],[-2],[-7],[-5],[-6],[-9],[-4],[9],[-9],[7],[7],[-5],[6],[-1],[5],[4],[4],[-7],[4],[3],[-2],[10],[9],[-9],[4],[2],[-5],[-2],[-1],[10],[5],[-9],[7],[-4],[-9],[-2],[-1],[-1],[4],[9],[-6],[-1],[7],[10],[6],[-3],[-3],[2],[2],[2],[2],[4],[-6],[4],[-5],[-10],[-5],[1],[-6],[-2],[-2],[-5],[-1],[6],[4],[-5],[-2],[2],[4],[-10],[10],[-1],[10],[-10],[7],[-9],[1],[6],[3],[-5],[10],[5],[-9],[-9],[-2],[5],[10],[-8],[-1],[9],[2],[-7],[-3],[5],[4],[5],[10],[-5],[-7],[-5],[5],[1],[-5],[6],[-1],[4],[-2],[-6],[-3],[-3],[1],[-1],[7],[9]], dtype = "uint64")#candidate|2126|(1440, 1)|const|uint64
call_2125 = relay.TupleGetItem(func_1989_call(relay.reshape(const_2126.astype('uint64'), [1440,])), 2)
call_2127 = relay.TupleGetItem(func_1991_call(relay.reshape(const_2126.astype('uint64'), [1440,])), 2)
func_1612_call = mod.get_global_var('func_1612')
func_1613_call = mutated_mod.get_global_var('func_1613')
call_2139 = relay.TupleGetItem(func_1612_call(), 1)
call_2140 = relay.TupleGetItem(func_1613_call(), 1)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_2147 = relay.TupleGetItem(func_1426_call(), 2)
call_2148 = relay.TupleGetItem(func_1428_call(), 2)
const_2150 = relay.const([[7,10,5,5,6,10,5,-7,3,-9,-7,-4,-2,-9,5,-3,-5,-4,-2,8,-10,-9,6,-7,-10,-6,7,-1,-5,6,-10,-2,-1,-5,5,10,2,4,3,-6,8,-10,-2,-3,-3,-6,-7,8,-7,10,-6,9,8,-5,5,-6,5,-7,8,5,1,4,2,-6,5,-10,4,9,1,5,-9,-8,-8,1,-6,-7,8,5,-3,8,4,-9,7,2,-5,-3,-7,-7,5,1,4,8,-1,-3,-1,4,-9,6,2,4,-5,4,-10,-7],[10,-6,-7,-8,5,-5,-2,-4,4,5,-7,5,-7,-4,-9,2,8,-6,2,3,5,8,1,-6,-1,2,1,-2,8,5,-4,9,-5,-6,6,6,1,9,-5,6,-8,-8,6,7,-3,-3,1,10,4,-3,-9,-4,-7,2,-7,-10,7,-4,-7,8,5,-10,3,2,-7,-10,8,-9,-8,-6,1,10,5,2,-6,5,-4,-10,6,4,1,-2,-9,-5,-3,-4,9,2,-9,-10,-7,-8,10,5,2,-1,-3,-5,3,-1,-10,-1,-10,-7],[-7,2,1,-2,10,9,7,8,-3,4,10,4,-2,-1,6,-9,-4,-7,-3,-8,-4,-6,8,-1,-6,1,-2,-5,10,5,5,-10,-5,4,6,2,2,3,3,-5,10,-4,-10,7,9,7,5,1,-6,9,-10,4,-2,-3,10,5,-5,4,-2,-7,-4,2,-4,1,-1,-4,3,4,2,2,7,-5,10,8,-2,-2,-9,-6,-9,-5,-9,-3,4,10,5,1,3,4,7,3,7,6,10,-1,10,1,-4,4,2,-5,7,-10,-3,-4],[-8,-10,2,3,1,-5,1,-2,10,2,-1,-8,-6,-1,-3,-9,-1,8,-6,-9,6,-10,8,9,-10,-8,1,-9,4,-5,-2,10,3,1,10,10,2,10,-4,7,-1,4,3,-8,-3,8,7,-1,7,-4,9,-10,6,2,8,-5,-8,-2,2,10,2,3,5,2,5,8,9,-9,-7,-4,-10,-5,-8,1,-6,7,8,-9,-3,6,6,6,-1,10,-5,4,-5,-6,-7,-5,8,3,2,-3,-3,-7,-5,6,-7,6,5,7,-1,3]], dtype = "uint8")#candidate|2150|(4, 104)|const|uint8
bop_2151 = relay.less(const_2119.astype('bool'), relay.reshape(const_2150.astype('bool'), relay.shape_of(const_2119))) # shape=(4, 104)
output = relay.Tuple([call_2106,call_2118,call_2125,const_2126,call_2139,call_2147,bop_2151,])
output2 = relay.Tuple([call_2107,call_2120,call_2127,const_2126,call_2140,call_2148,bop_2151,])
func_2163 = relay.Function([], output)
mod['func_2163'] = func_2163
mod = relay.transform.InferType()(mod)
output = func_2163()
func_2164 = relay.Function([], output)
mutated_mod['func_2164'] = func_2164
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2181 = relay.var("var_2181", dtype = "float64", shape = (8, 6, 15))#candidate|2181|(8, 6, 15)|var|float64
uop_2182 = relay.cos(var_2181.astype('float64')) # shape=(8, 6, 15)
func_2082_call = mod.get_global_var('func_2082')
func_2083_call = mutated_mod.get_global_var('func_2083')
call_2184 = relay.TupleGetItem(func_2082_call(), 2)
call_2185 = relay.TupleGetItem(func_2083_call(), 2)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_2189 = relay.TupleGetItem(func_1075_call(), 1)
call_2190 = relay.TupleGetItem(func_1076_call(), 1)
output = relay.Tuple([uop_2182,call_2184,call_2189,])
output2 = relay.Tuple([uop_2182,call_2185,call_2190,])
func_2193 = relay.Function([var_2181,], output)
mod['func_2193'] = func_2193
mod = relay.transform.InferType()(mod)
var_2194 = relay.var("var_2194", dtype = "float64", shape = (8, 6, 15))#candidate|2194|(8, 6, 15)|var|float64
output = func_2193(var_2194)
func_2195 = relay.Function([var_2194], output)
mutated_mod['func_2195'] = func_2195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1131_call = mod.get_global_var('func_1131')
func_1133_call = mutated_mod.get_global_var('func_1133')
call_2201 = func_1131_call()
call_2202 = func_1131_call()
func_1612_call = mod.get_global_var('func_1612')
func_1613_call = mutated_mod.get_global_var('func_1613')
call_2203 = relay.TupleGetItem(func_1612_call(), 2)
call_2204 = relay.TupleGetItem(func_1613_call(), 2)
func_609_call = mod.get_global_var('func_609')
func_614_call = mutated_mod.get_global_var('func_614')
var_2232 = relay.var("var_2232", dtype = "uint8", shape = (416,))#candidate|2232|(416,)|var|uint8
var_2233 = relay.var("var_2233", dtype = "uint8", shape = (4576,))#candidate|2233|(4576,)|var|uint8
const_2234 = relay.const([-7.680183,1.183382,-3.659997,2.930011,4.546604,5.972605,-1.146730,2.132324,-0.657970,-5.784565,-2.734475,-1.549843,4.105264,5.969442,9.610983,-6.372867,2.085389,-7.779466,-0.170910,5.999699,5.702711,9.632448,-5.634046,-1.709779,-7.032893,9.538570,8.929559,2.521698,2.721269,-8.900024,-9.486126,-9.022271,-3.202964,-1.766489,7.049033,6.654143,-1.610253,-1.406633,3.238099,0.650098,3.549357,-8.262093,-1.575259,-1.114237,-6.123300,-4.600464,8.550028,1.163257,3.209990,-7.943583,4.361858,1.547840,-6.693005,-3.189723,-8.141177,7.354940,7.477436,0.871920,3.487043,3.851852,-5.920677,8.395303,2.208968,4.150546,-0.344540,9.889117,6.255377,8.915461,-9.956151,5.549977,-1.255224,2.596937,-0.210895,5.179246,-5.196898,-5.087292,4.701649,-6.772031,-0.272402,0.165656,8.207704,-1.039067,-4.375870,-3.983964,8.894673,4.821603,2.826906,7.337991,1.603291,0.466590,-5.395728,-4.740169,3.889401,-4.996438,3.762003,-0.432321,-4.700925,1.642113,7.480094,9.193679,-4.289238,-5.473693,5.558939,9.732728,-9.188163,-3.198304,-1.058819,-1.690634,7.135165,5.796243,5.369012,2.045941,-1.404678,-8.855377,1.604537,8.871976,-8.030555,8.134953,9.205892,1.863669,6.099452,-4.938612,-0.737693,-9.976563,3.059216,-9.421963,6.546975,-2.561018,1.181869,3.632390,2.377439,-0.932088,-1.345849,7.700174,-2.590887,-6.018167,3.428615,-4.844298,7.260091,1.733546,-3.711533,9.421394,-3.412502,-5.175819,-9.210687,-3.093464,-5.034787,-0.592906,-4.293246,-8.686039,-4.515015,-7.631756,-6.372394,3.748106,3.252998,-1.491493,8.525623,-8.257985,-8.803883,6.287152,-8.163631,-3.598313,-8.064867,-6.361157,-2.788637,2.679846,9.549897,-5.003824,-9.920704,5.756354,3.550214,-1.487714,-6.981479,-4.998547,7.617236,2.791119,5.546528,-9.605279,-3.936790,-2.728105,8.479185,3.892380,8.297886,-5.383321,-3.491194,-1.543446,-1.518716,-3.091065,6.478294,1.127599,-8.233110,-6.101340,-2.966937,7.857452,2.851638,7.751395,1.350555,6.308220,0.186255,1.626669,-9.114003,6.133163,-0.194028,4.308531,-9.583217,-3.078563,4.732861,-3.492067,7.191493,9.351036,0.100528,4.921668,8.136427,3.078111,3.516947,-5.411286,-0.810782,-3.602604,6.096652,-4.776323,-8.589016,-3.789823,-6.712530,0.870401,-6.149758,-8.028454,0.411904,5.690795,1.695445,8.271259,1.519961,-3.605779,2.957645,-3.077663,-4.449792,-1.464448,9.794855,-0.246499,3.038791,4.591910,-1.438887,4.000922,3.764381,8.143061,-7.806899,4.403862,-2.591096,7.323416,-9.512937,5.389678,0.271431,6.325899,-2.795353,-9.880057,4.772417,-3.552508], dtype = "float32")#candidate|2234|(256,)|const|float32
call_2231 = relay.TupleGetItem(func_609_call(relay.reshape(var_2232.astype('uint8'), [1, 416]), relay.reshape(var_2233.astype('uint8'), [11, 416]), relay.reshape(const_2234.astype('float32'), [128, 2]), ), 4)
call_2235 = relay.TupleGetItem(func_614_call(relay.reshape(var_2232.astype('uint8'), [1, 416]), relay.reshape(var_2233.astype('uint8'), [11, 416]), relay.reshape(const_2234.astype('float32'), [128, 2]), ), 4)
func_1553_call = mod.get_global_var('func_1553')
func_1554_call = mutated_mod.get_global_var('func_1554')
call_2241 = relay.TupleGetItem(func_1553_call(), 0)
call_2242 = relay.TupleGetItem(func_1554_call(), 0)
uop_2243 = relay.acosh(call_2231.astype('float64')) # shape=(128, 2)
uop_2245 = relay.acosh(call_2235.astype('float64')) # shape=(128, 2)
const_2249 = relay.const([[-1.698368,-7.839120],[-5.970825,3.936684],[2.283324,-7.515428],[-1.539974,-1.253075],[3.497617,-8.480323],[-9.795640,-7.834236],[-0.535921,7.736087],[-8.694267,1.776083],[1.786398,-3.583930],[2.557177,3.105451],[-2.237378,0.857281],[9.835037,-5.406252],[-0.312194,2.958145],[1.075036,-2.883835],[6.315514,9.324225],[-2.535383,-0.938825],[-8.466290,-9.229023],[-5.607165,-7.703223],[1.332015,-2.155871],[3.548458,7.872520],[5.517807,3.045825],[-1.692368,5.313688],[2.001998,9.492064],[4.573517,6.388658],[-8.335367,9.410020],[-5.812500,-3.610365],[9.877440,-0.207025],[1.467381,1.510973],[3.424733,9.298552],[-3.877002,9.246155],[2.602464,-5.189140],[-5.654920,8.827877],[4.097190,-2.242727],[-9.242491,3.659021],[4.578967,0.900878],[3.642960,8.555797],[5.170546,-3.725929],[8.501548,6.199998],[-1.992425,-4.671214],[-9.816519,-7.807867],[-8.804388,5.371463],[5.468766,3.229169],[-0.673417,0.920016],[1.153628,-6.325837],[4.200942,-9.168693],[-9.434428,-3.775525],[2.896628,-5.902417],[-2.141693,5.594815],[4.870347,6.057072],[9.188464,7.491289],[4.991638,2.273879],[9.967025,1.874727],[-6.787898,-3.569192],[-6.948460,-6.601630],[2.105142,7.036461],[5.591420,-3.726791],[4.103933,1.932186],[-5.999703,-3.765766],[8.449095,-8.580233],[-2.291411,2.358891],[-1.757631,0.658558],[-4.370100,-6.118064],[-1.324168,9.155983],[2.014686,-3.202542],[-4.084350,4.217197],[-6.176366,-1.843869],[-3.083050,3.359750],[4.505628,7.795228],[-6.466869,-5.810254],[-8.233485,-9.430522],[-7.338531,-1.214127],[3.835002,-8.240471],[-7.201352,9.105064],[4.604695,-2.995099],[-5.650686,-7.155288],[7.567433,3.107344],[6.917305,-4.272792],[4.718541,-6.531692],[2.221022,2.982878],[-7.730841,-8.157858],[5.693326,4.573559],[3.679736,-5.623503],[5.217252,3.386248],[8.065188,-2.595692],[-5.406454,-4.952740],[5.006169,4.308147],[-3.004606,-3.462291],[-7.990569,4.353446],[-2.834570,6.045207],[9.391790,8.036971],[-6.568463,9.651802],[-3.001929,-4.930735],[-8.738242,-4.841705],[-0.805438,-6.416986],[-7.207119,0.268531],[5.895532,-5.917337],[5.175743,-3.386100],[-2.439157,-6.712438],[-4.080957,-0.514804],[7.053092,-6.834648],[5.567482,-4.151810],[-4.304500,-1.107354],[4.486238,-2.023028],[0.783662,-0.624149],[-5.790888,9.659742],[-9.045214,7.797963],[0.707910,4.040700],[2.803059,-9.909855],[-3.594465,-1.949301],[-1.692722,5.279300],[-8.257886,-5.569515],[9.117720,-7.086940],[2.948881,-0.125115],[0.320466,1.542140],[5.854256,-7.063558],[-0.510704,6.277324],[7.299768,4.685985],[2.134980,3.574321],[-5.679092,8.455695],[-6.835760,2.609507],[2.666648,6.787681],[-0.827198,3.596085],[-4.771127,-6.530857],[-6.441842,6.117337],[3.847296,7.480717],[-4.324755,-0.828050],[5.506046,-8.249400],[4.034112,1.751982]], dtype = "float64")#candidate|2249|(128, 2)|const|float64
bop_2250 = relay.logical_or(uop_2243.astype('bool'), relay.reshape(const_2249.astype('bool'), relay.shape_of(uop_2243))) # shape=(128, 2)
bop_2253 = relay.logical_or(uop_2245.astype('bool'), relay.reshape(const_2249.astype('bool'), relay.shape_of(uop_2245))) # shape=(128, 2)
output = relay.Tuple([call_2201,call_2203,var_2232,var_2233,const_2234,call_2241,bop_2250,])
output2 = relay.Tuple([call_2202,call_2204,var_2232,var_2233,const_2234,call_2242,bop_2253,])
func_2254 = relay.Function([var_2232,var_2233,], output)
mod['func_2254'] = func_2254
mod = relay.transform.InferType()(mod)
mutated_mod['func_2254'] = func_2254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2254_call = mutated_mod.get_global_var('func_2254')
var_2256 = relay.var("var_2256", dtype = "uint8", shape = (416,))#candidate|2256|(416,)|var|uint8
var_2257 = relay.var("var_2257", dtype = "uint8", shape = (4576,))#candidate|2257|(4576,)|var|uint8
call_2255 = func_2254_call(var_2256,var_2257,)
output = call_2255
func_2258 = relay.Function([var_2256,var_2257,], output)
mutated_mod['func_2258'] = func_2258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2011_call = mod.get_global_var('func_2011')
func_2013_call = mutated_mod.get_global_var('func_2013')
call_2333 = relay.TupleGetItem(func_2011_call(), 1)
call_2334 = relay.TupleGetItem(func_2013_call(), 1)
func_133_call = mod.get_global_var('func_133')
func_136_call = mutated_mod.get_global_var('func_136')
const_2339 = relay.const([[-6.567603,4.184514,-7.687385,-2.318223],[-3.707292,6.933380,8.597542,-6.482130],[2.300193,5.157156,5.958888,9.305465],[-7.775910,-8.807868,5.223980,-1.840803],[-6.726554,-1.379773,-5.406675,8.227867],[2.341766,8.582696,3.652205,3.052366],[8.713023,-5.373306,-9.337110,5.474720],[-0.201746,9.354257,-3.682610,3.166709],[0.810997,-3.617674,-4.721661,-4.809453],[-9.262084,-8.072889,7.143488,3.693305],[-2.709705,0.290939,7.434796,6.502552],[-4.775952,6.948294,-1.951815,8.046629],[-1.495970,2.941336,-4.615395,8.230136],[-8.156236,-0.489622,4.283032,-9.914675],[0.503974,-6.719985,7.575934,-9.856672],[-5.628225,-8.435833,-6.303213,-0.055521],[6.967617,8.662512,2.010147,7.411486],[-8.843418,-4.829022,9.514875,8.812468],[-3.948235,5.464325,7.479128,-5.337669],[3.740622,-6.861836,-9.194682,-8.602643],[8.758073,8.286940,-1.772180,-9.478875],[-1.947174,-5.395428,2.228777,-0.470039],[5.608105,2.042780,3.949218,-4.049582],[0.679738,-0.752890,0.707696,4.010872],[-7.969356,-1.941071,4.836410,4.194074],[6.634692,8.838810,0.893452,-6.799988],[9.845700,4.474272,1.662875,8.200729],[6.621058,6.026229,3.214621,4.584248],[1.746785,-3.688794,-5.528479,1.416021],[-0.680553,-9.964402,-3.317468,-1.679978],[6.930040,8.375619,-2.804308,2.068488],[-0.102639,-9.234313,3.229682,-7.396538],[5.943770,-2.130247,-8.148807,5.551457],[-9.462982,0.142268,4.436462,9.930666],[4.524815,4.184788,5.686989,0.399343],[8.215773,8.217674,9.085405,-2.805456],[8.621127,-2.023430,-8.406616,-3.985606],[-4.872714,4.465898,4.645539,-1.199119],[9.521864,-0.584706,-0.612774,7.986716],[-2.733535,-9.214037,-3.796682,-1.315802],[9.674649,7.534834,3.496084,2.121690],[5.621724,8.940855,4.999301,-1.787453],[4.210868,2.022971,-0.005021,-3.926222],[-2.720967,9.271312,9.864646,-6.947981],[-5.321927,-6.848281,7.648221,8.848512],[-9.372578,3.522070,-7.472478,5.906197],[1.681024,6.720633,8.634185,-5.530849],[0.419398,-9.952999,1.845131,9.318971],[-7.322066,4.843222,6.538804,0.224529],[9.170737,0.578599,-9.893692,-0.234968],[-9.393932,4.706846,0.084050,0.921076],[0.055875,0.339596,-9.239578,3.455150],[-3.526118,-3.051493,1.535032,1.323589],[-5.245614,3.904359,6.161387,-4.557573],[7.189983,0.506897,7.941943,4.862600],[-9.017255,-2.098174,-8.368581,-2.162755],[-5.028076,-4.948436,-9.362299,6.790092],[0.144018,4.569241,-0.201521,-8.631810],[3.791900,-2.982293,-1.488229,-1.893121],[-7.573156,4.802408,-3.624731,1.704068],[-0.513974,-7.798276,1.023088,2.588186],[-9.733746,-8.465622,9.508837,2.840080],[-6.062935,7.418111,0.100953,-5.653590],[-5.500484,-1.038285,5.736752,-3.082339],[-5.564120,-8.435238,-0.595948,-6.827239],[-6.401432,2.053681,1.408306,-6.615084],[-4.397373,-7.330369,1.164466,5.709300],[-9.554666,-4.654854,2.817434,4.911612],[-8.994416,5.688886,0.402280,4.015912],[-2.151425,2.830819,4.889147,-7.500516],[-4.351439,-2.272109,0.150792,4.114315],[6.751479,3.986472,-3.483320,-3.606598],[-3.798113,0.150641,8.829498,9.738430],[6.610560,9.881519,-9.511756,-7.285882],[-6.462370,2.110774,-3.409277,3.993917],[-0.995148,-1.782679,9.356832,8.919178],[9.903250,-9.491598,-7.519937,-8.805378],[-5.573852,-0.727079,8.059035,4.167918],[5.655906,3.958096,-5.616746,-3.057232],[9.837071,8.477461,1.146668,-4.353036],[-4.928095,-2.129177,-9.837223,-8.628793],[-1.197815,-5.601315,-0.359432,-9.008146],[-4.138207,6.146522,-1.161625,3.402932],[6.134603,0.577309,-7.808390,3.822237],[-2.811442,8.871873,-5.224150,5.985431],[-6.379550,5.395240,-8.046609,2.634440],[6.074467,3.282605,-1.446866,-9.180864],[2.480880,-9.782819,1.787315,-8.980915],[1.860417,6.808115,-8.733558,4.705094],[-5.384197,7.514417,-9.065530,6.256874],[7.640123,4.074437,0.578682,8.999544],[7.941328,-0.754101,5.537928,-9.481324],[-5.737463,2.438980,8.934517,-9.913086],[1.960811,-1.855055,-5.297198,7.215351],[-7.976597,9.978624,-8.999475,-1.019944],[-0.252381,8.535630,-0.361508,0.706815],[2.661207,4.740234,1.989591,-9.719377],[4.682956,-0.121727,-8.532169,6.553806],[-1.822147,-2.008061,-4.449218,9.009865],[-7.610570,-7.189846,-2.406286,2.066111],[-9.576465,-2.092837,-9.567969,-0.892071],[9.930087,4.226179,1.001924,-9.286482],[3.375213,-5.189819,-8.304208,6.154933],[-6.565642,4.770177,7.256814,-2.417666],[7.038980,8.487509,1.692110,6.430925],[-6.485168,-0.057925,0.237165,2.669218],[-2.767949,-5.721177,3.219546,4.885321],[-6.429372,4.332955,4.782237,2.953215],[-2.733514,1.147414,5.212803,3.303487],[3.992539,0.927080,-0.983507,-2.332342],[-7.890742,3.817388,-2.705472,-0.870425],[7.781365,-5.181994,8.595882,4.671607],[-1.626185,-3.782208,9.630040,9.310462],[9.598152,-5.650972,4.152714,-8.870758],[7.630174,-7.841981,-8.896344,-1.871220],[-6.659427,5.600463,6.375299,7.856737],[6.934978,0.319262,1.918379,4.975749],[0.361679,7.964041,-6.985072,-8.459858],[5.389326,5.648521,9.506165,-3.145498],[-7.300589,-9.909190,-6.731773,1.553769]], dtype = "float64")#candidate|2339|(120, 4)|const|float64
call_2338 = relay.TupleGetItem(func_133_call(relay.reshape(const_2339.astype('float64'), [12, 5, 8]), relay.reshape(const_2339.astype('float64'), [12, 5, 8]), ), 0)
call_2340 = relay.TupleGetItem(func_136_call(relay.reshape(const_2339.astype('float64'), [12, 5, 8]), relay.reshape(const_2339.astype('float64'), [12, 5, 8]), ), 0)
output = relay.Tuple([call_2333,call_2338,const_2339,])
output2 = relay.Tuple([call_2334,call_2340,const_2339,])
func_2348 = relay.Function([], output)
mod['func_2348'] = func_2348
mod = relay.transform.InferType()(mod)
output = func_2348()
func_2349 = relay.Function([], output)
mutated_mod['func_2349'] = func_2349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_2358 = relay.TupleGetItem(func_348_call(), 0)
call_2359 = relay.TupleGetItem(func_349_call(), 0)
func_2254_call = mod.get_global_var('func_2254')
func_2258_call = mutated_mod.get_global_var('func_2258')
var_2379 = relay.var("var_2379", dtype = "uint8", shape = (416,))#candidate|2379|(416,)|var|uint8
const_2380 = relay.const([[-2],[-8],[2],[3],[9],[6],[7],[-5],[-6],[7],[-4],[-1],[-4],[-4],[7],[-7],[-7],[-9],[5],[5],[-9],[8],[-10],[10],[-2],[7],[-3],[-2],[9],[7],[6],[-6],[-1],[3],[6],[1],[-8],[1],[2],[4],[-10],[1],[-9],[-10],[3],[-6],[-3],[1],[7],[9],[-4],[1],[9],[-8],[3],[6],[-2],[7],[-2],[-2],[4],[3],[2],[1],[-9],[-5],[9],[5],[-7],[-1],[-6],[6],[-6],[1],[-1],[4],[-5],[-3],[2],[-8],[-2],[-6],[-8],[1],[5],[-10],[10],[8],[2],[-3],[-4],[-8],[-3],[-4],[3],[-10],[7],[-10],[-8],[-2],[4],[1],[-9],[-8],[-8],[-4],[8],[-1],[-1],[8],[9],[2],[5],[-10],[-2],[5],[6],[2],[4],[-8],[10],[7],[4],[-9],[-5],[10],[6],[-9],[-2],[3],[3],[4],[3],[-9],[-5],[-3],[1],[-3],[10],[-9],[-2],[8],[-8],[8],[-5],[-8],[8],[-10],[-7],[1],[-7],[6],[-6],[10],[-4],[10],[7],[1],[-2],[9],[-1],[-8],[10],[-1],[-6],[-8],[-7],[-1],[-7],[9],[-10],[-5],[-7],[-4],[7],[-8],[10],[-7],[-3],[-7],[3],[4],[-4],[-2],[-5],[-2],[2],[-4],[8],[-7],[1],[5],[-9],[-2],[-3],[1],[-8],[5],[-9],[-5],[-2],[3],[-8],[2],[-5],[3],[2],[7],[-10],[-4],[-2],[10],[-2],[-6],[-6],[7],[-9],[1],[-7],[1],[1],[8],[-2],[7],[-8],[7],[-7],[-1],[-4],[2],[-7],[-9],[9],[-2],[-2],[-6],[9],[-8],[-3],[-2],[-5],[-10],[-8],[3],[-8],[-5],[2],[-1],[-3],[-7],[8],[-9],[9],[7],[-2],[2],[2],[2],[-3],[-3],[10],[5],[-1],[2],[9],[-10],[-3],[3],[6],[-6],[3],[-10],[8],[-4],[-6],[1],[6],[-7],[2],[10],[9],[10],[8],[-7],[-5],[7],[-1],[-2],[6],[1],[2],[8],[-9],[4],[4],[-5],[-3],[8],[8],[8],[-8],[-3],[9],[-9],[1],[8],[3],[-3],[3],[-4],[-3],[-2],[5],[10],[5],[9],[2],[-4],[7],[-7],[-3],[-2],[-3],[9],[-4],[2],[3],[4],[4],[-1],[1],[-2],[-2],[-5],[10],[-7],[-8],[-1],[6],[4],[-2],[-5],[-10],[3],[4],[-1],[-4],[9],[1],[-6],[5],[4],[-4],[4],[-5],[-10],[-5],[-2],[-6],[7],[8],[5],[4],[9],[8],[-6],[1],[-6],[-5],[7],[-9],[8],[3],[-8],[-4],[-9],[4],[-6],[7],[-4],[1],[8],[10],[-10],[-4],[-6],[5],[-6],[-4],[7],[9],[2],[-9],[-2],[2],[-1],[-5],[-6],[5],[-1],[-3],[2],[1],[-6],[10],[4],[-9],[-3],[-5],[-5],[2],[-3],[-7],[2],[-4],[-10],[2],[-7],[-8],[9],[-6],[5],[9],[4],[-4],[2],[-6],[-3],[-3],[4],[-1],[-8],[-6],[5],[10],[10],[-7],[3],[-7],[-4],[5],[7],[3],[6],[-6],[-5],[5],[-10],[-2],[3],[-9],[8],[-1],[3],[-8],[-9],[5],[6],[-5],[-3],[-3],[9],[-4],[8],[-4],[-8],[7],[-8],[-8],[6],[-10],[-1],[-10],[-2],[-9],[7],[-3],[-1],[5],[-5],[-2],[9],[-10],[8],[2],[4],[-1],[-8],[9],[-6],[-2],[2],[9],[-4],[-3],[-3],[-9],[-2],[1],[-7],[-6],[-6],[3],[5],[-3],[2],[-6],[-1],[-8],[-1],[-2],[-3],[7],[2],[-7],[-5],[-9],[9],[-5],[3],[7],[-3],[2],[10],[-9],[-10],[-3],[3],[-10],[10],[-5],[2],[5],[3],[-8],[-10],[-6],[10],[9],[7],[-10],[10],[-1],[7],[-10],[-1],[-1],[-7],[6],[10],[10],[1],[-3],[3],[2],[1],[-6],[7],[-1],[-9],[1],[-6],[-4],[-3],[-6],[-4],[-1],[10],[7],[-7],[3],[3],[8],[-9],[6],[2],[9],[-4],[-2],[3],[7],[2],[-4],[3],[8],[-10],[-9],[-2],[-5],[-8],[8],[-10],[7],[-10],[-8],[4],[-10],[-5],[-1],[-6],[10],[1],[3],[8],[6],[-8],[-5],[3],[-2],[-8],[-6],[8],[-1],[10],[1],[2],[-4],[-3],[-8],[-4],[9],[3],[2],[-6],[9],[-9],[-6],[-2],[-7],[-10],[10],[2],[-5],[-2],[5],[9],[10],[8],[8],[-10],[-7],[3],[-3],[-2],[-7],[1],[-2],[-1],[7],[2],[-9],[-8],[3],[-3],[-1],[9],[10],[-1],[6],[7],[8],[3],[2],[-9],[-9],[-3],[-9],[7],[8],[-2],[-3],[-6],[2],[-7],[-3],[-4],[-2],[-2],[-2],[3],[1],[-10],[-8],[4],[-9],[6],[-7],[6],[-10],[-10],[7],[7],[-2],[4],[-10],[-7],[-3],[-3],[6],[-9],[-4],[-8],[5],[-2],[6],[1],[7],[-1],[-7],[-7],[1],[9],[-1],[-7],[10],[1],[-10],[8],[-2],[2],[4],[1],[1],[2],[-8],[4],[3],[5],[6],[10],[-1],[3],[-1],[-7],[-1],[2],[6],[7],[-7],[5],[10],[-5],[5],[-8],[6],[-8],[-10],[-8],[-1],[-5],[-6],[6],[-10],[9],[-5],[-3],[8],[-1],[-9],[-5],[-6],[2],[5],[6],[-5],[-6],[8],[4],[8],[7],[10],[10],[7],[-2],[-10],[-1],[-1],[10],[-3],[1],[7],[-8],[1],[5],[5],[-5],[-10],[-6],[8],[-3],[-4],[-3],[-7],[10],[1],[-7],[-1],[5],[7],[1],[2],[9],[-3],[-10],[3],[-9],[10],[-4],[7],[7],[7],[8],[9],[10],[-5],[-9],[9],[10],[-3],[2],[4],[4],[3],[2],[-4],[-10],[3],[9],[-3],[-9],[9],[5],[6],[-1],[4],[6],[5],[3],[-8],[10],[6],[-4],[-9],[-2],[-1],[-1],[8],[10],[9],[-4],[5],[4],[-2],[7],[-4],[3],[-8],[8],[10],[-2],[-2],[1],[8],[6],[1],[4],[-2],[5],[5],[-5],[1],[-6],[4],[8],[5],[-3],[4],[-9],[-5],[4],[6],[1],[4],[3],[10],[-8],[-5],[9],[10],[1],[1],[2],[-8],[-10],[5],[9],[9],[1],[-8],[3],[-2],[6],[-5],[7],[6],[1],[-4],[3],[-6],[-4],[-4],[-2],[5],[-6],[-10],[10],[10],[-1],[2],[-4],[-8],[6],[-10],[3],[-1],[-4],[-2],[-9],[2],[1],[-6],[3],[-8],[3],[-2],[10],[2],[3],[6],[-9],[-5],[-1],[-1],[-7],[6],[4],[10],[10],[-2],[7],[1],[-6],[-5],[6],[-5],[8],[8],[-8],[-2],[2],[2],[9],[-3],[-7],[3],[-1],[-3],[-7],[7],[2],[8],[3],[-1],[-7],[-5],[-10],[6],[8],[-10],[6],[-1],[8],[-5],[-4],[8],[-6],[6],[-6],[-10],[10],[1],[2],[-9],[9],[-7],[5],[-6],[-4],[7],[5],[4],[4],[1],[-8],[3],[6],[-8],[-3],[1],[8],[-1],[-6],[5],[-7],[-7],[-8],[4],[-2],[-1],[7],[8],[8],[-4],[-5],[-7],[2],[8],[-2],[-7],[-3],[-1],[-5],[2],[1],[-8],[7],[-2],[2],[-10],[-2],[9],[-4],[2],[-8],[-6],[3],[-4],[2],[6],[9],[-2],[9],[-3],[-9],[-7],[-9],[-4],[3],[-8],[-7],[6],[2],[10],[3],[-9],[-1],[-1],[2],[-1],[-7],[1],[7],[9],[-3],[5],[-3],[-2],[8],[-1],[8],[-5],[3],[-9],[-10],[-8],[-3],[2],[-6],[1],[8],[-9],[-6],[6],[-3],[-7],[10],[-1],[-10],[8],[3],[4],[4],[-5],[7],[-8],[-2],[5],[-8],[-4],[-9],[1],[4],[2],[2],[-3],[-3],[10],[-5],[10],[3],[-6],[-6],[4],[2],[-4],[-10],[-2],[-7],[-8],[2],[4],[10],[-7],[-3],[4],[4],[2],[1],[-4],[6],[5],[3],[10],[-2],[10],[2],[3],[2],[-7],[-6],[10],[3],[10],[1],[-6],[-3],[3],[-2],[7],[3],[-10],[-1],[-9],[5],[-5],[-8],[-3],[-10],[4],[8],[-10],[-5],[-7],[8],[-1],[-9],[-10],[-7],[3],[-6],[5],[5],[7],[-10],[1],[-5],[8],[-4],[6],[-7],[4],[1],[-6],[2],[10],[-8],[-4],[-4],[2],[-1],[3],[2],[5],[4],[-9],[-10],[9],[-7],[-10],[4],[9],[-7],[-7],[-3],[5],[2],[10],[-9],[1],[8],[-6],[-2],[-10],[8],[10],[-9],[6],[-3],[7],[1],[-7],[-1],[-8],[-2],[6],[6],[-8],[5],[-7],[-9],[-6],[7],[6],[-4],[5],[-6],[10],[-9],[-10],[5],[3],[-7],[10],[-1],[6],[-8],[-8],[-4],[-7],[7],[4],[4],[3],[-2],[6],[-10],[-9],[-10],[-9],[-9],[-10],[-7],[4],[-1],[8],[2],[-3],[7],[10],[2],[7],[7],[-1],[6],[-7],[-4],[4],[5],[3],[-10],[6],[-6],[-8],[9],[-2],[-6],[-5],[4],[7],[5],[-7],[-2],[10],[-10],[5],[-5],[-1],[4],[-4],[7],[-5],[5],[-3],[3],[1],[7],[7],[-10],[9],[2],[-9],[9],[-10],[7],[-7],[9],[7],[-10],[-3],[10],[1],[1],[-9],[6],[10],[-3],[9],[-8],[4],[-4],[-2],[-1],[-9],[9],[5],[5],[9],[3],[6],[5],[9],[4],[8],[6],[9],[-5],[5],[2],[-8],[-5],[10],[-9],[7],[-6],[-3],[-10],[9],[-10],[-7],[-2],[-8],[-9],[-2],[6],[-2],[3],[4],[-3],[-5],[-3],[-2],[-3],[-8],[9],[-9],[4],[-6],[10],[-6],[10],[-1],[9],[6],[-6],[3],[-1],[4],[-5],[7],[8],[6],[5],[6],[2],[4],[-9],[-4],[10],[-10],[-10],[8],[7],[5],[4],[9],[2],[-7],[7],[-2],[5],[-10],[3],[-3],[-3],[1],[-8],[-5],[1],[-9],[6],[1],[1],[-4],[-3],[-9],[4],[-5],[5],[-2],[-2],[2],[-4],[-5],[10],[3],[1],[-3],[2],[-5],[4],[5],[5],[-7],[-7],[1],[-3],[-9],[3],[-1],[-9],[-9],[8],[3],[7],[-7],[3],[-9],[10],[-1],[4],[-6],[8],[-4],[-1],[-3],[1],[1],[2],[-1],[3],[10],[-8],[4],[-4],[4],[-8],[6],[10],[-4],[7],[1],[9],[-5],[-7],[10],[4],[4],[8],[9],[3],[-9],[-8],[7],[-5],[8],[10],[7],[-1],[-10],[1],[-6],[9],[-7],[10],[-8],[-3],[-3],[2],[-8],[-3],[-8],[-4],[-10],[-9],[3],[10],[5],[1],[-6],[-9],[-3],[-9],[-1],[8],[-9],[-6],[4],[2],[-6],[6],[-3],[9],[6],[1],[1],[4],[10],[2],[-6],[3],[-1],[-2],[8],[9],[-9],[3],[9],[-9],[4],[-7],[-7],[10],[-6],[-3],[3],[10],[4],[7],[10],[-7],[-10],[8],[-4],[6],[-6],[-4],[-6],[2],[-7],[6],[2],[1],[10],[9],[-5],[8],[9],[-7],[-4],[3],[-6],[4],[-9],[3],[3],[5],[-5],[-1],[-8],[6],[1],[1],[3],[-4],[-10],[6],[-2],[-9],[-7],[9],[2],[-7],[-2],[-6],[1],[6],[-10],[-1],[-2],[8],[10],[10],[-6],[-4],[-9],[-5],[9],[-2],[10],[-3],[-9],[-4],[-3],[-2],[10],[9],[-5],[3],[-7],[-6],[-2],[-9],[-3],[-1],[-8],[6],[3],[-6],[5],[-5],[7],[-4],[-4],[4],[5],[-8],[-1],[9],[-8],[8],[7],[3],[2],[-8],[9],[-1],[-7],[1],[-3],[3],[-6],[-7],[7],[-2],[-6],[-1],[2],[3],[-5],[-10],[-2],[5],[5],[3],[2],[8],[-6],[-7],[-10],[-8],[-9],[9],[2],[7],[1],[-4],[-8],[6],[-6],[3],[-4],[7],[3],[3],[-5],[10],[-7],[-5],[-9],[8],[10],[4],[-2],[1],[-9],[5],[-5],[-5],[8],[-4],[6],[-7],[4],[-4],[4],[4],[-4],[10],[-1],[4],[-7],[-5],[-1],[3],[-8],[-2],[-10],[1],[-1],[-7],[-7],[-7],[-1],[8],[1],[-4],[-1],[1],[1],[3],[10],[8],[-4],[-5],[2],[-10],[-5],[1],[-3],[8],[1],[4],[-2],[7],[-10],[5],[-8],[1],[-1],[-9],[-8],[-1],[3],[9],[-1],[1],[10],[5],[10],[-7],[2],[10],[6],[4],[-8],[10],[9],[1],[5],[1],[8],[7],[7],[1],[-4],[10],[2],[-8],[3],[-4],[4],[-1],[7],[-6],[-9],[-8],[10],[4],[-9],[-7],[-3],[1],[-8],[2],[2],[6],[-1],[-10],[6],[-1],[-2],[3],[-4],[9],[2],[-6],[-4],[-10],[7],[-8],[9],[-4],[1],[-1],[9],[-4],[-10],[-7],[4],[8],[4],[2],[-3],[4],[2],[1],[-6],[-4],[-1],[5],[-8],[5],[8],[4],[7],[-9],[-8],[-1],[-1],[4],[-7],[-7],[-2],[-1],[7],[-4],[-5],[-4],[-10],[6],[-2],[8],[-5],[-2],[-2],[-2],[-1],[-1],[1],[5],[7],[4],[8],[-6],[6],[-6],[6],[8],[-3],[-10],[7],[5],[2],[-3],[7],[2],[7],[8],[3],[4],[6],[8],[3],[5],[-8],[-10],[-6],[7],[10],[-10],[7],[-3],[-7],[-10],[6],[2],[5],[6],[-7],[6],[6],[4],[-3],[-10],[10],[2],[-10],[-2],[9],[-7],[-9],[7],[-10],[3],[-5],[-7],[-5],[5],[-2],[10],[2],[9],[-10],[-9],[4],[-2],[-7],[-6],[5],[8],[-8],[-3],[6],[10],[-10],[1],[-6],[-6],[-1],[3],[-2],[-8],[-7],[8],[2],[2],[-1],[-5],[-2],[6],[-7],[5],[-7],[-10],[-5],[4],[10],[-6],[4],[9],[-10],[-8],[-5],[-7],[-7],[-8],[-9],[-8],[2],[-5],[-10],[4],[-10],[-9],[4],[4],[8],[-6],[-6],[9],[-7],[-8],[9],[-3],[5],[-8],[8],[7],[2],[-6],[-5],[-2],[-2],[-5],[3],[-4],[10],[-9],[9],[10],[3],[-8],[-1],[8],[-2],[-10],[5],[-9],[2],[7],[-9],[-8],[-2],[-10],[2],[-4],[-9],[3],[-9],[3],[-7],[8],[7],[-3],[3],[-4],[1],[-3],[-2],[6],[4],[-8],[-4],[3],[6],[-5],[-9],[7],[10],[4],[-9],[6],[-4],[-5],[-2],[10],[-10],[-9],[1],[-8],[-7],[10],[-3],[3],[8],[-7],[-8],[9],[9],[-8],[-4],[7],[9],[8],[7],[7],[-8],[2],[-5],[-7],[2],[1],[4],[-2],[3],[-6],[-10],[-1],[-10],[-1],[5],[-10],[6],[-6],[-9],[-5],[4],[1],[-4],[-3],[-2],[-4],[-5],[-3],[3],[1],[-1],[-3],[-5],[9],[10],[2],[-10],[4],[-5],[10],[9],[2],[-8],[8],[-9],[3],[9],[7],[5],[-5],[10],[2],[2],[3],[-4],[-9],[-7],[-6],[5],[6],[10],[2],[-5],[3],[-6],[8],[-8],[5],[6],[-9],[1],[3],[6],[10],[-5],[5],[-8],[-5],[7],[7],[-6],[9],[-5],[4],[-2],[-2],[-9],[-8],[-8],[6],[9],[-9],[10],[1],[1],[1],[3],[3],[-6],[-9],[-8],[-1],[8],[3],[10],[-9],[3],[-5],[1],[-10],[-4],[-4],[-5],[-4],[2],[9],[-6],[8],[-10],[10],[-10],[-6],[-7],[6],[8],[4],[9],[10],[-3],[-4],[8],[6],[4],[8],[4],[-1],[-10],[-7],[-9],[-7],[-9],[9],[-7],[1],[-3],[-4],[6],[7],[-5],[-3],[6],[3],[-2],[-3],[3],[8],[-8],[-9],[5],[-6],[5],[-1],[1],[3],[4],[3],[10],[6],[-6],[3],[-8],[3],[-9],[3],[-4],[-4],[9],[2],[-3],[6],[-2],[9],[-6],[-6],[-5],[-4],[-1],[1],[1],[3],[2],[-6],[3],[1],[-4],[-5],[-7],[-8],[3],[-5],[-4],[-1],[6],[-4],[5],[2],[-5],[10],[-6],[-5],[-9],[7],[-9],[9],[3],[-10],[3],[-2],[5],[-7],[5],[10],[10],[9],[-1],[8],[-5],[6],[-4],[-5],[8],[-3],[-1],[1],[-3],[8],[10],[8],[-6],[-9],[1],[6],[4],[1],[-6],[-6],[6],[-7],[-6],[-10],[-9],[-7],[-6],[10],[-3],[-8],[-6],[-2],[8],[-2],[-4],[1],[8],[4],[6],[-3],[4],[-3],[-4],[-2],[-4],[1],[7],[-2],[-1],[-1],[3],[-2],[8],[6],[-1],[9],[6],[6],[7],[-7],[10],[-10],[-3],[4],[-9],[6],[7],[-6],[5],[-8],[-9],[-4],[1],[5],[7],[6],[9],[-6],[2],[-6],[-5],[4],[4],[6],[10],[-8],[1],[5],[9],[9],[-1],[-5],[2],[-5],[-1],[5],[7],[5],[-9],[-1],[-5],[1],[-10],[-9],[6],[6],[2],[10],[-1],[8],[9],[-8],[-5],[8],[-6],[-5],[7],[-8],[-10],[-5],[-6],[6],[2],[-3],[4],[-5],[-7],[9],[-7],[-5],[5],[5],[-4],[8],[-1],[-4],[6],[6],[7],[-1],[1],[4],[-10],[-9],[10],[-2],[-4],[9],[-2],[-5],[2],[2],[7],[-5],[7],[5],[-1],[-7],[2],[8],[4],[6],[-6],[7],[2],[3],[-9],[-3],[2],[3],[2],[-9],[-9],[-4],[6],[10],[3],[-5],[1],[-7],[4],[-8],[-4],[3],[8],[5],[-6],[-3],[-3],[-5],[-10],[-7],[2],[-9],[6],[7],[-7],[-4],[7],[7],[5],[-5],[6],[-7],[6],[8],[-6],[-6],[8],[3],[-5],[-3],[7],[-3],[7],[10],[-2],[3],[7],[-1],[-2],[9],[-3],[-8],[2],[5],[2],[-8],[-7],[1],[-3],[-6],[-10],[-4],[-8],[7],[3],[10],[3],[-7],[7],[-10],[9],[-8],[-3],[10],[2],[10],[4],[-6],[-9],[4],[1],[8],[-2],[-8],[-6],[-10],[8],[-3],[8],[6],[9],[1],[-8],[-10],[4],[-10],[10],[10],[4],[2],[6],[-7],[1],[7],[3],[-1],[-7],[-10],[3],[-5],[3],[-3],[-5],[6],[-1],[-1],[2],[5],[-8],[-5],[8],[-7],[-8],[2],[-6],[8],[4],[2],[-6],[-9],[9],[-6],[-8],[4],[-5],[-8],[5],[-8],[10],[-6],[-8],[-8],[8],[2],[-10],[-1],[-8],[8],[9],[-1],[3],[5],[-3],[-2],[-4],[-3],[-5],[-5],[-9],[-6],[-5],[-8],[5],[-1],[9],[7],[1],[1],[7],[-1],[4],[-1],[3],[1],[-2],[-2],[4],[-2],[-5],[-1],[4],[8],[2],[-1],[5],[-9],[-4],[-7],[8],[-10],[2],[7],[-10],[-5],[1],[1],[6],[3],[1],[8],[-4],[4],[-1],[6],[6],[10],[-7],[-6],[-10],[-4],[-6],[8],[-6],[-3],[-5],[-2],[10],[-8],[6],[10],[9],[2],[1],[-5],[-6],[1],[3],[8],[-10],[-6],[-2],[5],[-4],[-2],[-8],[-2],[6],[-5],[1],[-7],[-6],[-3],[-10],[10],[-9],[-7],[7],[-4],[-5],[-3],[1],[-10],[-3],[-4],[-2],[3],[9],[-8],[-4],[9],[9],[6],[-7],[10],[5],[3],[-1],[2],[5],[-8],[7],[4],[5],[5],[4],[-3],[-1],[8],[-7],[8],[-2],[-9],[3],[8],[-9],[6],[8],[-2],[-3],[2],[-4],[-10],[-6],[-4],[9],[-7],[4],[-5],[-1],[-6],[1],[-6],[3],[-2],[6],[6],[3],[-6],[-6],[-1],[4],[-5],[8],[-7],[7],[9],[5],[-7],[-3],[7],[-6],[-1],[6],[-7],[-10],[7],[-10],[2],[4],[-7],[5],[9],[1],[-10],[-8],[2],[-7],[3],[2],[8],[-10],[-6],[7],[10],[-9],[4],[-3],[6],[2],[8],[3],[2],[-5],[-3],[-6],[-9],[-8],[-9],[-4],[8],[-6],[-9],[-9],[4],[-3],[9],[-2],[-5],[-7],[4],[-1],[-2],[-7],[-4],[9],[-8],[6],[7],[4],[-5],[6],[2],[7],[5],[-6],[-1],[-3],[6],[3],[-2],[-1],[1],[-8],[3],[2],[1],[-3],[5],[10],[6],[-10],[-3],[-10],[-4],[-8],[-9],[-7],[-6],[-1],[-8],[-6],[10],[-2],[1],[-9],[-8],[-6],[4],[9],[-2],[4],[-5],[4],[-7],[8],[-7],[-6],[6],[-5],[2],[6],[3],[-2],[-9],[-2],[-7],[4],[7],[-1],[10],[-10],[6],[5],[-6],[10],[4],[-7],[-1],[1],[9],[3],[-2],[-7],[-3],[-3],[-10],[2],[-3],[-9],[-9],[6],[-9],[8],[3],[10],[-5],[-9],[9],[7],[-4],[7],[-5],[9],[7],[-6],[1],[10],[8],[-9],[-9],[4],[-1],[-2],[9],[-2],[-10],[-7],[9],[-5],[-6],[-3],[-5],[-4],[-2],[6],[2],[-7],[1],[5],[7],[-2],[-8],[3],[5],[-4],[-9],[5],[-1],[-8],[3],[-4],[4],[-8],[-1],[6],[10],[-4],[-7],[6],[3],[2],[-8],[-9],[-7],[1],[3],[-5],[-9],[3],[-5],[7],[-6],[-4],[7],[6],[1],[-3],[4],[-7],[1],[3],[7],[2],[-10],[-5],[3],[-2],[4],[4],[7],[1],[-8],[6],[-10],[-5],[3],[6],[7],[-6],[-2],[-3],[5],[-8],[1],[-10],[1],[-6],[-8],[3],[7],[9],[-7],[10],[3],[-10],[-8],[-2],[6],[2],[1],[8],[3],[-3],[8],[1],[5],[5],[-6],[-5],[-10],[-6],[7],[1],[-5],[3],[-5],[9],[6],[-1],[9],[10],[-3],[-5],[10],[10],[6],[8],[1],[9],[2],[-5],[4],[7],[6],[-4],[1],[9],[9],[-4],[6],[8],[-9],[5],[8],[9],[7],[-9],[8],[1],[-3],[10],[-7],[9],[-5],[-4],[9],[4],[8],[10],[-5],[-8],[-3],[-3],[10],[-4],[9],[8],[-3],[1],[-3],[10],[8],[-2],[5],[-4],[2],[-5],[6],[5],[-2],[-10],[3],[8],[-8],[7],[-5],[-3],[-2],[9],[10],[-10],[-5],[7],[-2],[7],[3],[6],[7],[3],[4],[-7],[6],[-2],[-7],[-6],[6],[9],[-10],[3],[1],[6],[9],[-10],[-8],[2],[-3],[-1],[-8],[-9],[-5],[4],[-10],[3],[1],[2],[5],[-4],[9],[-1],[-6],[-9],[3],[-10],[-2],[-8],[4],[8],[-4],[4],[6],[5],[-3],[8],[-4],[-1],[3],[3],[-9],[-6],[2],[9],[5],[9],[-8],[-5],[10],[-8],[1],[-7],[4],[-7],[-7],[4],[3],[-6],[-4],[-10],[2],[-10],[-6],[-9],[-5],[9],[2],[2],[1],[6],[2],[-3],[-9],[-10],[6],[4],[3],[2],[-9],[6],[-7],[-3],[-1],[6],[6],[2],[-1],[-3],[-6],[3],[-6],[9],[3],[9],[-2],[7],[3],[8],[-4],[-8],[8],[8],[-4],[10],[-3],[9],[-4],[-9],[2],[8],[-6],[-3],[4],[3],[-10],[8],[-10],[7],[-7],[-2],[-4],[2],[-3],[-2],[10],[1],[6],[6],[-9],[-7],[9],[-7],[2],[-3],[-3],[-9],[-7],[-4],[1],[-9],[7],[-10],[-8],[-4],[-5],[-6],[-8],[5],[6],[-1],[2],[7],[-1],[4],[-6],[-7],[-3],[-7],[-5],[-7],[-2],[7],[5],[2],[-10],[4],[2],[-5],[-10],[-7],[2],[-1],[-2],[5],[7],[-10],[-5],[1],[-10],[5],[5],[-6],[-9],[-10],[-10],[7],[-4],[6],[-7],[3],[-4],[-5],[9],[1],[8],[-1],[-5],[9],[-6],[3],[7],[-7],[-8],[-7],[5],[-9],[5],[8],[-1],[-5],[-4],[1],[3],[-3],[1],[6],[-8],[9],[7],[1],[7],[1],[-5],[8],[-9],[-4],[-9],[-2],[6],[-1],[1],[-5],[2],[5],[3],[3],[7],[4],[2],[-5],[-4],[4],[3],[-6],[-1],[-6],[-8],[-3],[8],[-2],[-7],[2],[9],[-5],[7],[4],[8],[-7],[-3],[-2],[3],[1],[2],[2],[6],[-10],[8],[-5],[8],[-10],[10],[8],[-1],[1],[-7],[-10],[-2],[2],[7],[-5],[-7],[-5],[8],[2],[10],[1],[-3],[1],[4],[-7],[4],[1],[-8],[-1],[6],[-7],[-10],[-6],[2],[4],[-9],[5],[-6],[3],[8],[-10],[9],[10],[4],[-4],[9],[1],[-6],[8],[6],[-4],[-9],[-4],[-5],[2],[9],[8],[3],[5],[1],[-8],[-3],[-2],[10],[6],[3],[9],[-9],[6],[4],[-9],[-2],[-2],[5],[4],[9],[8],[3],[-10],[1],[-6],[-8],[-6],[-2],[2],[4],[10],[8],[-3],[-9],[1],[-9],[9],[-9],[4],[7],[-2],[-9],[-3],[-5],[-6],[6],[-7],[5],[-7],[6],[-4],[7],[8],[4],[-3],[6],[-5],[8],[-3],[-3],[-3],[4],[-5],[-9],[5],[10],[-4],[-5],[-10],[8],[10],[-1],[-6],[-5],[1],[9],[-8],[6],[-4],[-6],[4],[-2],[-1],[-1],[-6],[4],[-3],[-4],[-5],[10],[-8],[-2],[6],[10],[2],[-10],[-1],[5],[9],[-5],[-6],[-2],[-6],[-8],[7],[7],[-8],[4],[6],[3],[1],[6],[-8],[-6],[-8],[-2],[9],[-1],[-2],[6],[-6],[-5],[-3],[-10],[2],[-8],[-1],[-6],[5],[5],[-2],[6],[-3],[-8],[6],[4],[-8],[-8],[-7],[-9],[4],[-3],[2],[-3],[1],[10],[3],[5],[-3],[-10],[-9],[-4],[-3],[-10],[-3],[-9],[-6],[3],[2],[-5],[-1],[4],[-1],[1],[4],[-4],[6],[-1],[-10],[-9],[-2],[1],[1],[-8],[-9],[-3],[9],[6],[8],[5],[-9],[-6],[9],[-3],[-2],[4],[-1],[4],[9],[4],[-6],[-8],[-6],[-5],[2],[-8],[-9],[7],[6],[6],[2],[-2],[7],[6],[9],[-5],[7],[-7],[8],[9],[10],[-10],[-6],[6],[6],[-1],[-6],[-3],[10],[-10],[-9],[1],[-8],[1],[10],[5],[-9],[-10],[1],[8],[10],[8],[-2],[-8],[10],[1],[-2],[-7],[1],[-6],[8],[-1],[-6],[4],[7],[-7],[-3],[4],[5],[8],[-9],[-7],[1],[1],[2],[5],[1],[-10],[6],[-6],[-8],[-9],[-9],[-6],[4],[-2],[-5],[6],[-4],[2],[-6],[-9],[10],[6],[5],[-9],[7],[4],[3],[-2],[8],[-2],[4],[-10],[6],[-6],[8],[1],[-5],[6],[-1],[3],[-2],[-3],[8],[2],[9],[8],[-3],[-4],[2],[-3],[-5],[10],[3],[8],[-10],[-1],[-7],[-7],[-10],[-1],[-2],[-4],[1],[4],[-8],[-6],[5],[-1],[-2],[2],[1],[4],[8],[4],[-10],[-8],[-6],[-9],[-10],[2],[4],[-1],[4],[5],[2],[-7],[1],[-10],[3],[-8],[9],[-7],[-10],[-3],[1],[-8],[-3],[-4],[-10],[2],[8],[-4],[3],[9],[-8],[-10],[5],[-3],[6],[-5],[1],[-4],[10],[-1],[6],[-4],[-5],[5],[-2],[3],[-3],[10],[-2],[5],[9],[7],[-3],[4],[8],[6],[9],[8],[6],[-1],[8],[-2],[-8],[-3],[5],[10],[-7],[-6],[7],[-4],[7],[9],[-7],[9],[10],[4],[5],[3],[10],[4],[3],[3],[-1],[8],[1],[3],[9],[-4],[-6],[-2],[5],[6],[-3],[1],[-4],[-3],[9],[5],[-5],[5],[7],[5],[-9],[2],[2],[-4],[9],[-4],[1],[-8],[-2],[-2],[-6],[-8],[1],[8],[5],[-4],[10],[10],[10],[-10],[-7],[5],[-2],[3],[-3],[5],[-1],[10],[-10],[8],[2],[8],[9],[-6],[5],[10],[-10],[10],[-8],[-6],[-5],[2],[-3],[7],[-1],[-7],[-6],[4],[4],[-6],[6],[10],[1],[-10],[2],[-1],[6],[-2],[8],[-4],[-4],[-1],[-7],[-8],[7],[-1],[10],[-2],[1],[1],[7],[-10],[-7],[-4],[2],[3],[1],[8],[3],[1],[10],[4],[3],[-10],[-8],[-10],[6],[10],[4],[10],[3],[4],[9],[4],[-10],[1],[-4],[9],[-1],[-4],[3],[-5],[-5],[4],[-2],[7],[-8],[-1],[-5],[-9],[9],[4],[-5],[3],[-5],[8],[-2],[-6],[-2],[8],[3],[-1],[-6],[-7],[9],[-7],[-8],[-2],[-5],[2],[3],[-7],[4],[3],[2],[-10],[-7],[-5],[3],[-6],[-10],[1],[-4],[-2],[9],[9],[3],[-10],[-9],[-1],[-4],[-5],[9],[-6],[4],[5],[4],[3],[-8],[-7],[8],[-10],[3],[-5],[2],[-3],[-6],[9],[-10],[10],[-6],[-1],[2],[6],[-10],[6],[2],[8],[5],[-10],[-3],[5],[-3],[7],[-9],[1],[-3],[-4],[6],[-4],[7],[-6],[-5],[4],[10],[-8],[9],[2],[-6],[-7],[-7],[10],[9],[-4],[8],[-5],[5],[3],[8],[3],[3],[10],[-3],[-4],[-5],[-7],[7],[2],[-5],[-5],[2],[9],[-1],[-1],[-2],[-6],[-4],[-9],[-3],[9],[1],[-10],[-3],[-8],[-7],[-1],[-5],[8],[3],[-5],[-2],[1],[9],[6],[-10],[2],[8],[4],[2],[-2],[-5],[8],[3],[5],[5],[-10],[3],[4],[1],[8],[4],[-7],[-9],[6],[2],[-10],[10],[8],[4],[-9],[5],[8],[3],[4],[4],[7],[9],[2],[4],[-9],[7],[3],[7],[-3],[5],[2],[5],[10],[5],[-4],[-3],[7],[-7],[-9],[-9],[5],[-8],[-7],[10],[-8],[4],[-6],[3],[7],[-9],[7],[3],[5],[-4],[-1],[5],[-1],[6],[9],[-8],[2],[-10],[-10],[-4],[1],[9],[-5],[-3],[-2],[-7],[2],[-9],[-4],[-2],[3],[-2],[1],[1],[3],[10],[9],[1],[2],[6],[-10],[9],[4],[6],[-4],[-3],[-8],[10],[-6],[-3],[-6],[-4],[-4],[1],[-8],[-2],[-2],[4],[-10],[6],[-7],[-3],[-5],[-6],[-5],[10],[2],[8],[-9],[-2],[8],[9],[6],[5],[-2],[-3],[1],[5],[10],[5],[-10],[7],[-8],[-8],[6],[6],[-5],[-5],[6],[10],[-3],[10],[9],[-8],[-7],[-4],[-9],[-9],[-8],[4],[6],[-1],[2],[-3],[-5],[8],[-5],[2],[4],[-3],[-4],[-9],[8],[9],[-4],[3],[2],[-10],[-7],[5],[-5],[-10],[1],[-6],[-3],[-7],[-8],[1],[4],[-3],[3],[-8],[-7],[9],[3],[-7],[-7],[3],[-10],[-5],[10],[9],[8],[-3],[10],[-3],[-1],[7],[-1],[-5],[2],[-5],[1],[-7],[6],[4],[-3],[3],[5],[-6],[-1],[7],[9],[-3],[4],[-7],[2],[-3],[1],[-3],[-3],[-5],[4],[-10],[4],[-3],[6],[-1],[7],[7],[4],[6],[-7],[8],[-1],[7],[2],[10],[9],[-4],[-5],[-8],[-8],[-6],[-2],[4],[9],[1],[-1],[4],[-2],[7],[2],[-9],[-7],[-4],[9],[-3],[-2],[1],[6],[-2],[-7],[10],[2],[1],[-6],[7],[6],[-1],[-8],[-5],[-8],[5],[9],[-5],[-3],[-9],[2],[10],[5],[9],[2],[9],[3],[-10],[6],[7],[6],[-5],[-9],[-2],[-9],[-3],[-2],[6],[-8],[7],[10],[-9],[8],[3],[7],[-10],[-3],[-9],[-7],[-5],[4],[9],[2],[-3],[10],[-2],[8],[3],[-3],[1],[-8],[4],[-6],[-4],[-6],[9],[-8],[5],[-4],[2],[-8],[4],[10],[-5],[-6],[2],[7],[-7],[-8],[8],[-1],[-3],[-7],[-1],[-7],[-5],[-1],[-3],[6],[1],[-4],[8],[-10],[-4],[10],[-4],[9],[2],[-6],[-7],[5],[-7],[10],[-7],[-8],[10],[3],[3],[7],[-4],[1],[7],[-5],[-8],[-9],[-1],[-6],[3],[10],[4],[-8],[2],[-6],[-7],[-6],[9],[-10],[7],[-5],[-4],[9],[-3],[8],[3],[-5],[8],[3],[7],[6],[-4],[6],[10],[-10],[-1],[2],[-1],[3],[-6],[-9]], dtype = "uint8")#candidate|2380|(4576, 1)|const|uint8
call_2378 = relay.TupleGetItem(func_2254_call(relay.reshape(var_2379.astype('uint8'), [416,]), relay.reshape(const_2380.astype('uint8'), [4576,]), ), 5)
call_2381 = relay.TupleGetItem(func_2258_call(relay.reshape(var_2379.astype('uint8'), [416,]), relay.reshape(const_2380.astype('uint8'), [4576,]), ), 5)
output = relay.Tuple([call_2358,call_2378,var_2379,const_2380,])
output2 = relay.Tuple([call_2359,call_2381,var_2379,const_2380,])
func_2390 = relay.Function([var_2379,], output)
mod['func_2390'] = func_2390
mod = relay.transform.InferType()(mod)
var_2391 = relay.var("var_2391", dtype = "uint8", shape = (416,))#candidate|2391|(416,)|var|uint8
output = func_2390(var_2391)
func_2392 = relay.Function([var_2391], output)
mutated_mod['func_2392'] = func_2392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_2444 = relay.TupleGetItem(func_348_call(), 0)
call_2445 = relay.TupleGetItem(func_349_call(), 0)
output = relay.Tuple([call_2444,])
output2 = relay.Tuple([call_2445,])
func_2454 = relay.Function([], output)
mod['func_2454'] = func_2454
mod = relay.transform.InferType()(mod)
mutated_mod['func_2454'] = func_2454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2454_call = mutated_mod.get_global_var('func_2454')
call_2455 = func_2454_call()
output = call_2455
func_2456 = relay.Function([], output)
mutated_mod['func_2456'] = func_2456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2348_call = mod.get_global_var('func_2348')
func_2349_call = mutated_mod.get_global_var('func_2349')
call_2493 = relay.TupleGetItem(func_2348_call(), 0)
call_2494 = relay.TupleGetItem(func_2349_call(), 0)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_2497 = relay.TupleGetItem(func_1426_call(), 1)
call_2498 = relay.TupleGetItem(func_1428_call(), 1)
func_2011_call = mod.get_global_var('func_2011')
func_2013_call = mutated_mod.get_global_var('func_2013')
call_2523 = relay.TupleGetItem(func_2011_call(), 1)
call_2524 = relay.TupleGetItem(func_2013_call(), 1)
var_2536 = relay.var("var_2536", dtype = "bool", shape = (8, 13, 4))#candidate|2536|(8, 13, 4)|var|bool
bop_2537 = relay.equal(call_2497.astype('bool'), relay.reshape(var_2536.astype('bool'), relay.shape_of(call_2497))) # shape=(8, 13, 4)
bop_2540 = relay.equal(call_2498.astype('bool'), relay.reshape(var_2536.astype('bool'), relay.shape_of(call_2498))) # shape=(8, 13, 4)
output = relay.Tuple([call_2493,call_2523,bop_2537,])
output2 = relay.Tuple([call_2494,call_2524,bop_2540,])
func_2552 = relay.Function([var_2536,], output)
mod['func_2552'] = func_2552
mod = relay.transform.InferType()(mod)
mutated_mod['func_2552'] = func_2552
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2553 = relay.var("var_2553", dtype = "bool", shape = (8, 13, 4))#candidate|2553|(8, 13, 4)|var|bool
func_2552_call = mutated_mod.get_global_var('func_2552')
call_2554 = func_2552_call(var_2553)
output = call_2554
func_2555 = relay.Function([var_2553], output)
mutated_mod['func_2555'] = func_2555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_2560 = relay.TupleGetItem(func_2454_call(), 0)
call_2561 = relay.TupleGetItem(func_2456_call(), 0)
output = call_2560
output2 = call_2561
func_2562 = relay.Function([], output)
mod['func_2562'] = func_2562
mod = relay.transform.InferType()(mod)
output = func_2562()
func_2563 = relay.Function([], output)
mutated_mod['func_2563'] = func_2563
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2588 = relay.var("var_2588", dtype = "float32", shape = (1, 16, 14))#candidate|2588|(1, 16, 14)|var|float32
uop_2589 = relay.asin(var_2588.astype('float32')) # shape=(1, 16, 14)
uop_2594 = relay.tan(var_2588.astype('float64')) # shape=(1, 16, 14)
output = relay.Tuple([uop_2589,uop_2594,])
output2 = relay.Tuple([uop_2589,uop_2594,])
func_2602 = relay.Function([var_2588,], output)
mod['func_2602'] = func_2602
mod = relay.transform.InferType()(mod)
mutated_mod['func_2602'] = func_2602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2603 = relay.var("var_2603", dtype = "float32", shape = (1, 16, 14))#candidate|2603|(1, 16, 14)|var|float32
func_2602_call = mutated_mod.get_global_var('func_2602')
call_2604 = func_2602_call(var_2603)
output = call_2604
func_2605 = relay.Function([var_2603], output)
mutated_mod['func_2605'] = func_2605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_800_call = mod.get_global_var('func_800')
func_801_call = mutated_mod.get_global_var('func_801')
call_2621 = relay.TupleGetItem(func_800_call(), 0)
call_2622 = relay.TupleGetItem(func_801_call(), 0)
output = call_2621
output2 = call_2622
func_2623 = relay.Function([], output)
mod['func_2623'] = func_2623
mod = relay.transform.InferType()(mod)
mutated_mod['func_2623'] = func_2623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2623_call = mutated_mod.get_global_var('func_2623')
call_2624 = func_2623_call()
output = call_2624
func_2625 = relay.Function([], output)
mutated_mod['func_2625'] = func_2625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2623_call = mod.get_global_var('func_2623')
func_2625_call = mutated_mod.get_global_var('func_2625')
call_2662 = func_2623_call()
call_2663 = func_2623_call()
func_1325_call = mod.get_global_var('func_1325')
func_1329_call = mutated_mod.get_global_var('func_1329')
const_2689 = relay.const([-9,1,3,3,2,6,10,-9,-3,-4,-8,9,-2,-5,4,6,-5,9,6,-7,9,2,-7,6,2,9,6,8,-3,-10,2,-10,-5,-2,2,9,5,3,-10,1,10,6,8,-3,-6,9,3,3,-8,-6,6,-4,-7,-10,7,-3,-1,-2,-10,1,-9,3,8,9,1,-8,3,8,8,-8,-1,-1,-9,-3,-7,-6,5,-10,5,8,-5,7,-8,-7,-4,3,-8,-2,-5,-8,9,9,-5,-6,-8,-8,-3,-8,-9,9,-2,1,-7,6,7,-4,-8,-2,-4,3,5,5,-6,2,10,9,6,-9,-4,-4,-9,-1,5,-1,-2,-1,6,6,8,7,1,-9,9,-9,5,8,-2,-2,-10,6,-7,-10,2,7,6,-10,-2,-4,-7,6,4,5,-10,-5,-9,-4,-9,-3,2,4,4,3,-3,8,9,9,5,1,2,-10,10,-9,-8,-1,2,6,-9,3,9,-1,3,-2,-5,-8,3,-8,-1,10,-1,10,6,3,-9,7,-6,-4,8,1,-1,10,6,4,7,9,-7,-5,-6,-10,3,-3,-6,1,-5,9,1,9,-9,7,1,8,-2,2,-1,3,10,4,4,-1,-8,-4,-2,-8,-10,-9,-10,8,1,-2,-10,6,-2,5,-10,5,-9,-8,-6,1,3,6,10,7,-3,4,7,-5,-4,5,9,9,2,8,-6,-1,-3,-4,10,2,2,7,8,10,-2,-4,-6,-8,2,4,5,9,-4,-10,-4,-8,-8,8,6,-8,3,-1,4,-9,5,6,-1,-9,8,9,-2,10,1,8,8,-8,-7,-1,-10,9,4,-7,-2,9,-6,2,3,-1,-4,4,4,-2,-10,-4,-5,-8,-10,-3,-3,-2,1,8,10,10,8,-5,-5,5,-3,-6,4,7,-8,8,-3,10,-6,1,10,1,5,-10,4,8,6,6,-9,-6,3,8,-6,-3,-1,-8,8,-8,-5,5,-4,1,-8,-10,1,-4,9,4,4,-8,2,5,5,-4,10,4,-2,-3,-1,5,-8,6,-3,-3,-8,2,-6,1,-10,4,4,-5,-2,-5,1,6,-1,9,5,-10,2,4,-9,-1,-9,9,6,10,-2,2,-6,-5,1,10,-5,-8,2,-6,8,-2,-6,-10,6,-10,-6,-6,-1,9,4,-9,-10,7,-2,5,-4,-6,-9,-3,-8,-5,-7,7,1,-1,5,-5,10,7,7,-9,10,-1,4,5,-7,8,-1,-4,-3,9,-7,-5,6,-7,5,-6,-3,-7,1,1,-2,3,-8,-8,-4,-10,-1,5,8,-2,10,-1,5,2,-10,5,3,-7,-7,-3,2,-1,2,-2,-10,5,-4,-4,4,6,-10,6,-1,6,10,10,-7,-6,-6,9,-5,-9,3,-6,1,3,-5,7,-3,-7,-6,-6,-7,-2,-1,1,7,2,3,-9,2,-8,-2,-4,-9,8,7,8,6,-6,-1,10,-7,10,-2,8,10,2,10,6,4,-7,-10,4,-7,1,-5,7,-5,6,3,-3,8,4,-9,1,4,6,-3,10,-9,7,3,-10,1,8,-7,-9,-6,7,3,1,-6,-1,-7,8,-1,-4,10,-7,-7,7,5,1,10,9,5,-3,8,9,-7,5,-3,4,-10,-4,-5,-3,8,-4,-3,2,-6,9,10,-1,-7,5,-5,1,10,-4,-8,-7,-4,-7,-5,-7,5,-5,7,10,-4,2,-3,-5,-10,-8,-10,9,8,-3,6,-4,-9,5,-8,-8,1,-2,-2,-9,-7,-3,4,1,7,-4,5,5,8,-7,-7,9,-4,-4,9,3,2,5,7,7,9,10,-9,5,4,-4,-9,-1,-3,1,10,-7,9,8,7,3,-7,1,7,3,-10,-4,-7,3,-2,1,-10,4,-2,9,-10,-7,-5,-2,6,4,2,6,3,-1,-4,6,-3,-5,-5,-6,7,5,-4,4,4,-6,6,-6,-1,-1,-7,1,7,7,-8,-10,-6,7,-2,8,9,-2,7,-1,3,7,10,2,-4,1,9,7,8,5,-6,-6,8,7,6,-6,-3,10,1,-1,10,6,-5,7,8,-3,-5,-9,-9,-2,6,3,-1,1,5,-6,5,-8,-7,-4,-7,9,-8,-8,-5,-3,8,-10,-8,-2,4,10,2,-8,3,5,-8,5,-3,4,-3,10,-2,-2,-3,3,-4,7,-3,6,8,7,6,-4,6,8,5,-1,-10,7,-7,1,5,9,6,3,9,-1,-3,7,-5,9,4,-6,2,8,-4,-3,8,9,9,7,4,-4,-3,8,-5,7,-4,-4,8,8,-10,3,4,3,5,-3,7,8,10,9,1,-7,-1,-3,-2,1,3,3,7,3,7,1,-7,6,-4,-5,3,2,-4,4,-8,-1,10,-8,-9,1,9,1,-2,3,6,-3,-3,-4,1,-4,-5,-10,8,-4,-9,4,10,3,-6,9,6,10,8,8,-2,-8,7,1,-6,-6,-1,-2,-8,2,3,6,5,9,-8,3,-9,-6,-7,-4,4,-7,-10,6,5,-4,1,-8,-3,-2,-5,-2,3,3,-7,-2,-8,-5,-9,-8,1,5,-9,-2,1,3,6,2,-5,9,5,4,2,2,2,-10,-10,-9,-7,9,-5,-7,10,-10,6,9,-3,-5,-4,-10,4,3,2,-3,3,8,6,8,-7,-3,10,-6,-6,-9,5,9,7,3,4,-10,-8,6,6,-2,-4,7,8,8,4,6,-7,9,7,-5,8,1,-4,1,-2,-2,-7,-2,-2,-1,-8,-6,-2,-8,8,1,7,-3,-8,2,7,-10,-2,-1,3,-9,-7,-3,-9,-7,4,-3,9,-3,-2,10,-8,-4,-3,5,7,4,-8,-4,-9,3,8,-6,4,5,-4,-5,-5,3,6,-1,-1,-10,3,-7,4,6,10,10,-1,1,-1,-10,-7,-4,10,-9,-2,1,10,8,1,-7,-7,-6,5,-4,4,-5,-6,8,-8,-8,-4,8,8,-10,-1,10,8,-6,3,-1,3,-10,9,-6,4,7,-4,4,2,-1,-4,1,-8,7,7,10,6,-1,-9,1,-3,-3,-5,9,2,-10,-4,10,-8,-3,5,-6,-3,-7,6,-6,-6,5,6,7,-5,-4,-8,1,1,10,5,-8,-5,-1,-3,-9,5,-10,-8,-7,-6,2,-7,-1,-6,6,-8,-2,-9,3,1,3,-6,5,2,8,6,5,4,-2,8,4,2,9,10,-5,6,6,-1,-7,-4,-4,-9,-4,4,3,-3,9,2,9,2,2,-4,-9,9,9,-10,-4,3,-2,-3,10,-4,5,7,-8,10,6,-10,8,-8,1,-1,9,-2,-2,7,-4,10,-7,-3,-5,-8,-4,3,-6,-10,-3,3,-8,4,-3,-9,4,-4,6,9,-10,-2,5,-8,-10,-9,1,6,8,-9,-3,-8,10,1,9,7,6,4,7,-2,2,2,5,3,8,-6,2,1,6,-8,-1,-6,6,-10,-4,2,6,-9,1,-8,-6,1,8,10,5,3,-2,-5,-1,-3,-1,-10,10,10,3,-10,2,-7,-5,-6,-4,6,-8,-6,10,-3,-6,-8,4,6,5,6,-1,-8,9,-7,-5,-1,-8,3,6,-6,10,-9,-1,-10,2,4,1,10,-7,5,3,-4,-10,-6,-4,-1,8,7,-4,6,4,-9,-1,5,5,-10,3,-9,5,-3,10,1,1,-7,-8,-1,2,-7,9,1,-1,4,8,-9,9,-10,-6,-8,3,-4,-8,-1,-6,-3,2,1,-6,-7,6,-7,-10,5,2,-6,1,-3,-6,-9,-5,-9,8,-10,3,-3,3,-6,-9,-10,-6,-3,6,-8,-2,-7,1,4,6,-8,-1,-7,-10,-9,6], dtype = "uint64")#candidate|2689|(1440,)|const|uint64
call_2688 = relay.TupleGetItem(func_1325_call(relay.reshape(const_2689.astype('uint64'), [15, 8, 12]), relay.reshape(const_2689.astype('uint64'), [15, 8, 12]), ), 0)
call_2690 = relay.TupleGetItem(func_1329_call(relay.reshape(const_2689.astype('uint64'), [15, 8, 12]), relay.reshape(const_2689.astype('uint64'), [15, 8, 12]), ), 0)
output = relay.Tuple([call_2662,call_2688,const_2689,])
output2 = relay.Tuple([call_2663,call_2690,const_2689,])
func_2696 = relay.Function([], output)
mod['func_2696'] = func_2696
mod = relay.transform.InferType()(mod)
mutated_mod['func_2696'] = func_2696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2696_call = mutated_mod.get_global_var('func_2696')
call_2697 = func_2696_call()
output = call_2697
func_2698 = relay.Function([], output)
mutated_mod['func_2698'] = func_2698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1381_call = mod.get_global_var('func_1381')
func_1383_call = mutated_mod.get_global_var('func_1383')
call_2757 = func_1381_call()
call_2758 = func_1381_call()
output = call_2757
output2 = call_2758
func_2759 = relay.Function([], output)
mod['func_2759'] = func_2759
mod = relay.transform.InferType()(mod)
mutated_mod['func_2759'] = func_2759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2759_call = mutated_mod.get_global_var('func_2759')
call_2760 = func_2759_call()
output = call_2760
func_2761 = relay.Function([], output)
mutated_mod['func_2761'] = func_2761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_2789 = relay.TupleGetItem(func_1075_call(), 2)
call_2790 = relay.TupleGetItem(func_1076_call(), 2)
output = call_2789
output2 = call_2790
func_2797 = relay.Function([], output)
mod['func_2797'] = func_2797
mod = relay.transform.InferType()(mod)
output = func_2797()
func_2798 = relay.Function([], output)
mutated_mod['func_2798'] = func_2798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_2879 = relay.TupleGetItem(func_1426_call(), 1)
call_2880 = relay.TupleGetItem(func_1428_call(), 1)
var_2885 = relay.var("var_2885", dtype = "bool", shape = (8, 13, 4))#candidate|2885|(8, 13, 4)|var|bool
bop_2886 = relay.bitwise_and(call_2879.astype('uint32'), relay.reshape(var_2885.astype('uint32'), relay.shape_of(call_2879))) # shape=(8, 13, 4)
bop_2889 = relay.bitwise_and(call_2880.astype('uint32'), relay.reshape(var_2885.astype('uint32'), relay.shape_of(call_2880))) # shape=(8, 13, 4)
bop_2891 = relay.not_equal(call_2879.astype('bool'), relay.reshape(bop_2886.astype('bool'), relay.shape_of(call_2879))) # shape=(8, 13, 4)
bop_2894 = relay.not_equal(call_2880.astype('bool'), relay.reshape(bop_2889.astype('bool'), relay.shape_of(call_2880))) # shape=(8, 13, 4)
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
var_2905 = relay.var("var_2905", dtype = "uint64", shape = (1440,))#candidate|2905|(1440,)|var|uint64
call_2904 = relay.TupleGetItem(func_1989_call(relay.reshape(var_2905.astype('uint64'), [1440,])), 1)
call_2906 = relay.TupleGetItem(func_1991_call(relay.reshape(var_2905.astype('uint64'), [1440,])), 1)
func_2602_call = mod.get_global_var('func_2602')
func_2605_call = mutated_mod.get_global_var('func_2605')
const_2911 = relay.const([[3.474631,8.312022,1.661917,9.772635,-9.355887,5.199355,-9.040360,-4.446787,-5.919473,-7.498392,-9.988173,-5.727612,4.535861,-5.126718,9.174927,-8.551579,2.080614,-7.736716,4.757103,3.053355,-5.370388,-2.607107,8.893650,2.944677,-9.412373,-0.161632,5.355608,0.273654,-3.821439,-2.456756,6.322930,4.099767,-5.022939,3.102583,5.828440,3.245606,8.220453,-1.567637,-8.257043,-2.284045,4.196246,-1.500087,0.052507,4.748618,8.255461,-0.878255,4.311000,4.623607,6.533851,2.695069,7.313812,2.817518,8.617293,-2.169891,0.688667,-1.199610,8.940602,7.233055,-0.797920,-3.186797,-5.729240,-6.678201,-2.534338,0.976683,-6.402182,-6.054503,-1.963565,-0.021989,-3.465772,5.702412,4.548454,-2.352041,-8.011482,-6.425972,9.825059,-0.436056,9.917574,0.267366,3.958893,9.444768,1.976656,2.357604,6.094922,6.921972,-4.517437,-3.222927,9.224236,-0.109454,-9.817552,-7.808250,-9.671241,-1.749141,-1.608057,2.270109,-3.284020,7.685079,6.019966,1.599068,0.886705,-4.910682,-5.269972,2.096937,7.292297,7.042570,-5.724924,6.026628,1.475381,-8.901707,4.442755,6.773316,9.899520,-2.456114,1.044063,1.090632,-4.534821,7.458838,-4.551230,-5.343006,-4.973541,-0.541249,-1.234548,2.699669,0.102593,0.114845,-1.813994,-1.904321,6.929316,-8.452010,9.970083,7.242900,5.191156,-7.656671,-7.946794,9.619464,-5.436113,2.867738,-5.880733,-6.610876,1.316912,-5.704824,-7.720678,7.878428,0.725557,0.222840,8.464624,4.501310,3.101521,6.751838,-3.720492,-6.704002,-0.177045,2.267966,0.285269,-5.271691,1.340194,-6.494466,1.629876,-2.909121,7.834828,0.721532,-4.107537,3.143481,-8.804995,7.380599,0.101523,-6.210761,-7.054303,-3.591380,0.761433,-9.854479,-8.296479,6.794685,-3.082176,-9.149190,4.620441,-0.813039,-1.004379,7.579453,-6.368464,-0.537911,-8.865166,7.496658,-4.062076,-1.922423,-3.644097,1.433643,0.527701,0.350048,-3.679193,7.013810,1.682753,8.859816,1.571273,0.270418,-0.186425,-2.326548,-6.428290,3.149534,7.423516,-7.042998,-3.292593,-6.289900,-6.179686,7.823560,-8.955697,-1.728157,-9.228671,4.124440,-6.442264,-3.650357,-8.162144,-2.889670,-2.222549,-2.686419,0.379271,-2.264284,-8.554961,-3.519984,-3.538419,8.289978,-1.459627,-6.220944,7.433245,9.025554]], dtype = "float32")#candidate|2911|(1, 224)|const|float32
call_2910 = relay.TupleGetItem(func_2602_call(relay.reshape(const_2911.astype('float32'), [1, 16, 14])), 0)
call_2912 = relay.TupleGetItem(func_2605_call(relay.reshape(const_2911.astype('float32'), [1, 16, 14])), 0)
output = relay.Tuple([bop_2891,call_2904,var_2905,call_2910,const_2911,])
output2 = relay.Tuple([bop_2894,call_2906,var_2905,call_2912,const_2911,])
func_2934 = relay.Function([var_2885,var_2905,], output)
mod['func_2934'] = func_2934
mod = relay.transform.InferType()(mod)
var_2935 = relay.var("var_2935", dtype = "bool", shape = (8, 13, 4))#candidate|2935|(8, 13, 4)|var|bool
var_2936 = relay.var("var_2936", dtype = "uint64", shape = (1440,))#candidate|2936|(1440,)|var|uint64
output = func_2934(var_2935,var_2936,)
func_2937 = relay.Function([var_2935,var_2936,], output)
mutated_mod['func_2937'] = func_2937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1943_call = mod.get_global_var('func_1943')
func_1945_call = mutated_mod.get_global_var('func_1945')
call_2941 = func_1943_call()
call_2942 = func_1943_call()
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_2947 = relay.TupleGetItem(func_1075_call(), 1)
call_2948 = relay.TupleGetItem(func_1076_call(), 1)
output = relay.Tuple([call_2941,call_2947,])
output2 = relay.Tuple([call_2942,call_2948,])
func_2988 = relay.Function([], output)
mod['func_2988'] = func_2988
mod = relay.transform.InferType()(mod)
mutated_mod['func_2988'] = func_2988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2988_call = mutated_mod.get_global_var('func_2988')
call_2989 = func_2988_call()
output = call_2989
func_2990 = relay.Function([], output)
mutated_mod['func_2990'] = func_2990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2348_call = mod.get_global_var('func_2348')
func_2349_call = mutated_mod.get_global_var('func_2349')
call_3006 = relay.TupleGetItem(func_2348_call(), 2)
call_3007 = relay.TupleGetItem(func_2349_call(), 2)
var_3019 = relay.var("var_3019", dtype = "float64", shape = (120, 4))#candidate|3019|(120, 4)|var|float64
bop_3020 = relay.logical_or(call_3006.astype('bool'), relay.reshape(var_3019.astype('bool'), relay.shape_of(call_3006))) # shape=(120, 4)
bop_3023 = relay.logical_or(call_3007.astype('bool'), relay.reshape(var_3019.astype('bool'), relay.shape_of(call_3007))) # shape=(120, 4)
func_667_call = mod.get_global_var('func_667')
func_670_call = mutated_mod.get_global_var('func_670')
const_3026 = relay.const([-7.126406,2.870185,2.240693,9.394617,-5.760503,2.045847,3.298176,-0.070348,9.888089,7.003687,-7.576885,-4.605619,-3.017106,-1.123067,-6.337580,-4.825362,-3.805428,8.215918,-5.245519,0.019807,9.603131,-0.797484,-5.095214,3.790861,-1.223540,0.533657,-0.873653,-6.838476,7.202398,-2.020426,-5.116467,-8.669811,-9.413620,-4.440952,-5.105258,-4.882692,-0.467201,-7.459921,4.396419,-7.456438,-2.874759,5.941253,-5.147456,4.203767,-7.499293,3.710971,-3.372759,2.766051,6.008978,9.617665,7.201470,5.098226,4.826945,6.994596,6.319572,-8.734467,9.021072,-3.073816,4.306565,6.500320,4.618813,-6.911511,-7.256205,-3.631913,9.573749,0.438898,5.761671,-5.365054,-9.758598,-2.500303,0.952096,2.976700,-5.065480,-9.726452,4.179729,6.006507,-0.151187,5.747655,7.255287,-2.990431,9.382142,9.409733,-8.383707,6.407959,5.111081,-0.697755,-3.146872,4.913213,1.414208,-4.859933,3.384802,3.896437,7.075862,-7.978712,9.976633,8.330054,-6.223079,0.933570,-2.487240,7.894787,-1.422322,3.463220,2.098216,1.462483,-3.104648,-1.387023,3.586204,-8.118707,-9.527179,1.780689,3.615579,-3.414737,-8.124274,9.419027,0.105194,-1.310594,-9.233676,-2.529153,1.751598,9.699444,-2.881083,4.944545,0.700389,-8.556953,7.550700,8.322156,6.608006,-4.960488,-8.626943,-9.831941,1.688329,8.207476,-5.893977,7.855770,-9.149983,-4.128393,-8.885541,-1.636759,1.376048,0.338766,3.656424,6.257935,1.525425,-9.548446,5.058438,6.538011,1.367090,1.416221,-8.720166,7.358560,3.732434,3.991111,-8.899749,7.658598,2.498877,-1.970695,-4.336886,1.473126,5.178136,5.411354,-3.667114,2.137296,4.222780,-2.251075,-5.749094,-4.676097,6.019633,0.707327,-3.147461,0.282769,-6.824067,-2.198099,3.501753,-8.048502,0.652696,-8.290073,-6.145263,3.214544,-4.832481,9.992184,-2.154745,-4.463039,-2.639603,7.922638,-3.705079,-5.401390,-6.582899,3.161331,-6.172514,-2.737887,7.872291,8.379794,6.483871,-6.449930,-3.357911,-7.088752,2.925980,-5.671529,-3.863571,-7.031116,-7.469425,6.649499,9.012186,2.318657,-0.404281,4.657032,-0.957111,4.564688,-2.067907,2.840447,-4.952125,9.457372,-4.213255,3.442908,4.286462,3.608142,-3.156073,-0.680399,-4.672107,0.453416,6.335095,-6.217312,4.558306,9.011864,1.572565,8.077174,-8.965125,-1.521952,-6.588263,-2.489287,2.677214,-2.343433,-1.707784,-9.040068,-6.904291,-5.927699,-9.955747,9.000957,-1.048873,0.050961,6.298581,3.540154,9.662203,-6.723470,5.196593,6.154599,-4.306256,-9.007308,-8.260643,5.301899,-5.804685,1.811280,6.585554,9.787749,7.839625,5.325252], dtype = "float32")#candidate|3026|(256,)|const|float32
call_3025 = relay.TupleGetItem(func_667_call(relay.reshape(const_3026.astype('float32'), [256,])), 2)
call_3027 = relay.TupleGetItem(func_670_call(relay.reshape(const_3026.astype('float32'), [256,])), 2)
bop_3034 = relay.equal(var_3019.astype('bool'), relay.reshape(call_3006.astype('bool'), relay.shape_of(var_3019))) # shape=(120, 4)
bop_3037 = relay.equal(var_3019.astype('bool'), relay.reshape(call_3007.astype('bool'), relay.shape_of(var_3019))) # shape=(120, 4)
func_2696_call = mod.get_global_var('func_2696')
func_2698_call = mutated_mod.get_global_var('func_2698')
call_3044 = relay.TupleGetItem(func_2696_call(), 2)
call_3045 = relay.TupleGetItem(func_2698_call(), 2)
func_2163_call = mod.get_global_var('func_2163')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_3047 = relay.TupleGetItem(func_2163_call(), 5)
call_3048 = relay.TupleGetItem(func_2164_call(), 5)
func_1837_call = mod.get_global_var('func_1837')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_3056 = relay.TupleGetItem(func_1837_call(), 2)
call_3057 = relay.TupleGetItem(func_1838_call(), 2)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_3064 = relay.TupleGetItem(func_2454_call(), 0)
call_3065 = relay.TupleGetItem(func_2456_call(), 0)
uop_3085 = relay.acos(bop_3034.astype('float64')) # shape=(120, 4)
uop_3087 = relay.acos(bop_3037.astype('float64')) # shape=(120, 4)
output = relay.Tuple([bop_3020,call_3025,const_3026,call_3044,call_3047,call_3056,call_3064,uop_3085,])
output2 = relay.Tuple([bop_3023,call_3027,const_3026,call_3045,call_3048,call_3057,call_3065,uop_3087,])
func_3090 = relay.Function([var_3019,], output)
mod['func_3090'] = func_3090
mod = relay.transform.InferType()(mod)
mutated_mod['func_3090'] = func_3090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3091 = relay.var("var_3091", dtype = "float64", shape = (120, 4))#candidate|3091|(120, 4)|var|float64
func_3090_call = mutated_mod.get_global_var('func_3090')
call_3092 = func_3090_call(var_3091)
output = call_3092
func_3093 = relay.Function([var_3091], output)
mutated_mod['func_3093'] = func_3093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1131_call = mod.get_global_var('func_1131')
func_1133_call = mutated_mod.get_global_var('func_1133')
call_3098 = func_1131_call()
call_3099 = func_1131_call()
output = call_3098
output2 = call_3099
func_3108 = relay.Function([], output)
mod['func_3108'] = func_3108
mod = relay.transform.InferType()(mod)
output = func_3108()
func_3109 = relay.Function([], output)
mutated_mod['func_3109'] = func_3109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_3131 = relay.TupleGetItem(func_1426_call(), 0)
call_3132 = relay.TupleGetItem(func_1428_call(), 0)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_3138 = relay.TupleGetItem(func_782_call(), 2)
call_3139 = relay.TupleGetItem(func_783_call(), 2)
output = relay.Tuple([call_3131,call_3138,])
output2 = relay.Tuple([call_3132,call_3139,])
func_3154 = relay.Function([], output)
mod['func_3154'] = func_3154
mod = relay.transform.InferType()(mod)
mutated_mod['func_3154'] = func_3154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3154_call = mutated_mod.get_global_var('func_3154')
call_3155 = func_3154_call()
output = call_3155
func_3156 = relay.Function([], output)
mutated_mod['func_3156'] = func_3156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_3209 = relay.TupleGetItem(func_1075_call(), 0)
call_3210 = relay.TupleGetItem(func_1076_call(), 0)
output = call_3209
output2 = call_3210
func_3226 = relay.Function([], output)
mod['func_3226'] = func_3226
mod = relay.transform.InferType()(mod)
output = func_3226()
func_3227 = relay.Function([], output)
mutated_mod['func_3227'] = func_3227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1658_call = mod.get_global_var('func_1658')
func_1659_call = mutated_mod.get_global_var('func_1659')
call_3233 = func_1658_call()
call_3234 = func_1658_call()
func_2348_call = mod.get_global_var('func_2348')
func_2349_call = mutated_mod.get_global_var('func_2349')
call_3235 = relay.TupleGetItem(func_2348_call(), 0)
call_3236 = relay.TupleGetItem(func_2349_call(), 0)
output = relay.Tuple([call_3233,call_3235,])
output2 = relay.Tuple([call_3234,call_3236,])
func_3240 = relay.Function([], output)
mod['func_3240'] = func_3240
mod = relay.transform.InferType()(mod)
mutated_mod['func_3240'] = func_3240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3240_call = mutated_mod.get_global_var('func_3240')
call_3241 = func_3240_call()
output = call_3241
func_3242 = relay.Function([], output)
mutated_mod['func_3242'] = func_3242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_3259 = relay.TupleGetItem(func_1029_call(), 0)
call_3260 = relay.TupleGetItem(func_1031_call(), 0)
output = relay.Tuple([call_3259,])
output2 = relay.Tuple([call_3260,])
func_3293 = relay.Function([], output)
mod['func_3293'] = func_3293
mod = relay.transform.InferType()(mod)
output = func_3293()
func_3294 = relay.Function([], output)
mutated_mod['func_3294'] = func_3294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1837_call = mod.get_global_var('func_1837')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_3317 = relay.TupleGetItem(func_1837_call(), 2)
call_3318 = relay.TupleGetItem(func_1838_call(), 2)
output = call_3317
output2 = call_3318
func_3325 = relay.Function([], output)
mod['func_3325'] = func_3325
mod = relay.transform.InferType()(mod)
output = func_3325()
func_3326 = relay.Function([], output)
mutated_mod['func_3326'] = func_3326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2082_call = mod.get_global_var('func_2082')
func_2083_call = mutated_mod.get_global_var('func_2083')
call_3329 = relay.TupleGetItem(func_2082_call(), 0)
call_3330 = relay.TupleGetItem(func_2083_call(), 0)
var_3336 = relay.var("var_3336", dtype = "uint64", shape = (15, 8, 12))#candidate|3336|(15, 8, 12)|var|uint64
bop_3337 = relay.logical_or(call_3329.astype('bool'), relay.reshape(var_3336.astype('bool'), relay.shape_of(call_3329))) # shape=(15, 8, 12)
bop_3340 = relay.logical_or(call_3330.astype('bool'), relay.reshape(var_3336.astype('bool'), relay.shape_of(call_3330))) # shape=(15, 8, 12)
output = relay.Tuple([bop_3337,])
output2 = relay.Tuple([bop_3340,])
func_3347 = relay.Function([var_3336,], output)
mod['func_3347'] = func_3347
mod = relay.transform.InferType()(mod)
var_3348 = relay.var("var_3348", dtype = "uint64", shape = (15, 8, 12))#candidate|3348|(15, 8, 12)|var|uint64
output = func_3347(var_3348)
func_3349 = relay.Function([var_3348], output)
mutated_mod['func_3349'] = func_3349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_3388 = relay.TupleGetItem(func_782_call(), 1)
call_3389 = relay.TupleGetItem(func_783_call(), 1)
output = call_3388
output2 = call_3389
func_3390 = relay.Function([], output)
mod['func_3390'] = func_3390
mod = relay.transform.InferType()(mod)
mutated_mod['func_3390'] = func_3390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3390_call = mutated_mod.get_global_var('func_3390')
call_3391 = func_3390_call()
output = call_3391
func_3392 = relay.Function([], output)
mutated_mod['func_3392'] = func_3392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3325_call = mod.get_global_var('func_3325')
func_3326_call = mutated_mod.get_global_var('func_3326')
call_3453 = func_3325_call()
call_3454 = func_3325_call()
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_3500 = func_2562_call()
call_3501 = func_2562_call()
output = relay.Tuple([call_3453,call_3500,])
output2 = relay.Tuple([call_3454,call_3501,])
func_3515 = relay.Function([], output)
mod['func_3515'] = func_3515
mod = relay.transform.InferType()(mod)
output = func_3515()
func_3516 = relay.Function([], output)
mutated_mod['func_3516'] = func_3516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3293_call = mod.get_global_var('func_3293')
func_3294_call = mutated_mod.get_global_var('func_3294')
call_3527 = relay.TupleGetItem(func_3293_call(), 0)
call_3528 = relay.TupleGetItem(func_3294_call(), 0)
output = call_3527
output2 = call_3528
func_3539 = relay.Function([], output)
mod['func_3539'] = func_3539
mod = relay.transform.InferType()(mod)
output = func_3539()
func_3540 = relay.Function([], output)
mutated_mod['func_3540'] = func_3540
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3584 = relay.var("var_3584", dtype = "int16", shape = ())#candidate|3584|()|var|int16
var_3585 = relay.var("var_3585", dtype = "int16", shape = (16, 6, 13))#candidate|3585|(16, 6, 13)|var|int16
bop_3586 = relay.greater_equal(var_3584.astype('bool'), var_3585.astype('bool')) # shape=(16, 6, 13)
func_1131_call = mod.get_global_var('func_1131')
func_1133_call = mutated_mod.get_global_var('func_1133')
call_3594 = func_1131_call()
call_3595 = func_1131_call()
output = relay.Tuple([bop_3586,call_3594,])
output2 = relay.Tuple([bop_3586,call_3595,])
func_3598 = relay.Function([var_3584,var_3585,], output)
mod['func_3598'] = func_3598
mod = relay.transform.InferType()(mod)
var_3599 = relay.var("var_3599", dtype = "int16", shape = ())#candidate|3599|()|var|int16
var_3600 = relay.var("var_3600", dtype = "int16", shape = (16, 6, 13))#candidate|3600|(16, 6, 13)|var|int16
output = func_3598(var_3599,var_3600,)
func_3601 = relay.Function([var_3599,var_3600,], output)
mutated_mod['func_3601'] = func_3601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2797_call = mod.get_global_var('func_2797')
func_2798_call = mutated_mod.get_global_var('func_2798')
call_3696 = func_2797_call()
call_3697 = func_2797_call()
output = relay.Tuple([call_3696,])
output2 = relay.Tuple([call_3697,])
func_3709 = relay.Function([], output)
mod['func_3709'] = func_3709
mod = relay.transform.InferType()(mod)
output = func_3709()
func_3710 = relay.Function([], output)
mutated_mod['func_3710'] = func_3710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1943_call = mod.get_global_var('func_1943')
func_1945_call = mutated_mod.get_global_var('func_1945')
call_3789 = func_1943_call()
call_3790 = func_1943_call()
func_2696_call = mod.get_global_var('func_2696')
func_2698_call = mutated_mod.get_global_var('func_2698')
call_3818 = relay.TupleGetItem(func_2696_call(), 0)
call_3819 = relay.TupleGetItem(func_2698_call(), 0)
func_800_call = mod.get_global_var('func_800')
func_801_call = mutated_mod.get_global_var('func_801')
call_3847 = relay.TupleGetItem(func_800_call(), 0)
call_3848 = relay.TupleGetItem(func_801_call(), 0)
func_2254_call = mod.get_global_var('func_2254')
func_2258_call = mutated_mod.get_global_var('func_2258')
const_3852 = relay.const([5,-4,-5,-7,5,6,-8,-7,1,-7,8,7,2,10,-3,9,-5,2,-9,-8,6,2,-2,10,-8,2,-3,-1,-9,7,10,-1,1,4,4,-4,5,-6,-2,2,7,7,1,3,1,-3,5,7,-7,6,2,-4,6,3,8,8,-7,5,5,9,7,-8,-8,-10,5,-8,8,5,4,3,-5,-9,-8,-2,2,8,5,-4,10,-10,4,1,10,7,5,-7,-1,-3,-1,-1,-8,2,6,8,2,10,-6,7,8,-1,1,3,6,-2,-1,-10,5,-2,-10,6,8,5,10,9,5,3,10,10,2,-3,-7,3,6,3,-6,7,9,-8,-3,7,7,-4,7,-2,-7,5,-9,8,-4,1,-1,5,-10,9,10,-3,-9,5,-2,5,2,-7,-8,6,5,-5,-8,8,-3,-5,-6,-1,5,1,3,-1,7,5,1,9,-3,-4,-5,10,1,3,4,-2,-10,-8,-10,9,7,3,7,5,6,-10,-4,-9,6,2,-5,-8,-9,9,7,7,2,-3,-1,9,-8,8,-9,-6,-6,6,-7,6,3,5,3,-4,-9,-4,-7,-8,1,-8,-3,-7,7,10,-8,-9,-4,-10,6,10,3,8,6,-7,-1,9,-9,3,-2,9,-1,-10,3,-2,6,-4,5,-10,-7,-7,-10,-2,-5,-7,10,-6,4,-8,5,-4,1,1,10,-6,-6,7,3,9,6,4,1,9,-5,-2,6,-3,-4,4,6,2,4,10,-9,-5,6,-1,9,-4,-6,7,2,10,4,1,3,-2,3,6,10,6,-1,4,-8,6,-3,-5,-3,-3,6,-5,-9,8,8,7,5,5,-2,-8,7,4,9,5,4,-8,-3,-1,-1,-8,3,8,-9,-4,4,-1,7,1,5,-7,5,3,-10,2,-3,2,-6,-2,7,-5,-1,2,-2,-4,-10,-7,-10,-6,-5,4,9,-4,10,9,3,10,10,1,-6,10,10,2,-8,-2,7,10,6,2,-1,5,4,-9,-7,8,-9,-1,6,1,-2,-8,1,-6,4,-2,10,1,3,10,-2,3,-7,-10,-8,8,4,-10,5,-1,-5,-6,-10,-8,-8,-5,9,2,2,10,3,-1,-5,9,8,-3,-2,-9,5,-7,8,-3,-10,2,7,4,-9,6,-8,7,4,1,6,-2,9,-6,-3,-1,-6,-7,-4,-4,5,-8,4,1,5,5,3,-4,9,7,-1,-5,3,1,-2,-2,-2,2,-6,-3,6,-4,-7,3,-10,-8,-1,9,6,3,2,6,6,1,2,4,-4,-9,7,-9,-2,-10,-1,-9,9,-6,7,-7,10,6,-2,2,-9,6,-4,-4,1,3,3,10,6,-2,-8,6,5,-1,-10,-2,7,6,-3,10,-4,-6,7,-6,-2,3,-7,7,1,-10,1,2,10,-9,-8,-6,4,-9,10,1,4,-9,5,3,-3,8,5,-2,-8,7,-2,8,7,-6,-3,-8,-2,-7,2,-4,-5,9,-10,4,-3,-6,5,2,1,8,6,-2,10,7,1,9,4,5,-10,-4,9,-10,3,-6,-2,10,-8,-10,4,-4,-1,-3,10,8,7,1,-1,-2,-4,1,-3,-8,5,-3,7,4,-8,-2,-4,-8,-4,9,-1,2,-9,3,-5,-5,9,9,-5,6,9,4,10,-4,-1,10,4,-7,-6,-7,1,3,-1,-8,7,-4,3,2,9,8,9,-4,-1,-7,1,-7,-5,-4,5,5,-9,-8,8,-8,8,-9,-5,1,5,-2,-2,-1,-1,5,9,8,10,10,8,7,3,2,-10,-3,-10,1,6,-9,5,3,-8,3,8,8,-1,-1,-2,2,5,4,10,7,5,3,2,7,-8,9,-4,-4,-1,-9,10,-4,-9,-10,4,-7,5,-3,7,-8,10,2,2,9,1,-8,-1,5,9,-3,5,3,1,7,-4,4,10,-8,-10,-10,4,1,8,-9,3,1,-1,6,-10,9,-7,10,9,-4,4,1,9,7,-9,-6,8,8,2,1,-8,8,5,5,-5,-4,-2,-8,8,2,-2,10,6,9,-6,1,-5,1,4,-4,6,7,3,-1,-9,-8,1,-10,10,6,2,-1,-4,-8,8,-9,-10,-2,-10,-5,6,-1,-3,-4,10,2,9,10,-4,4,-10,6,-7,-4,1,-7,3,4,9,-3,-9,-3,-6,2,3,4,8,5,8,6,7,6,3,7,9,-1,5,-9,-10,1,-8,7,4,-5,9,2,7,7,-8,-2,-4,-5,8,10,-4,1,5,-10,-10,-3,-6,-7,1,-3,-10,-5,-7,-3,-6,-4,5,4,3,-1,1,-4,-9,10,-6,-10,-7,1,7,10,9,6,9,-6,-8,-9,-2,-5,-5,2,9,8,-9,1,-4,-1,-7,9,-1,-2,1,-5,4,4,5,9,-8,-10,-5,-2,6,-4,-2,-10,-5,9,4,10,4,-7,2,4,4,-8,7,-10,3,7,-4,-8,1,-8,3,-5,4,9,10,9,-7,5,-4,8,-8,5,-2,-4,4,8,-9,-6,4,2,-9,10,-5,2,1,-9,7,-4,8,-3,-9,10,3,3,-3,3,-6,-10,1,10,-5,4,2,-2,7,5,-4,6,-2,7,5,-9,-7,2,2,2,1,-9,4,-5,5,-9,-6,-10,-5,6,-1,1,-6,7,-2,-3,-5,-6,-4,-1,3,-1,4,-7,-8,-9,10,8,2,1,-2,-7,-9,-7,-7,3,8,-7,3,1,9,-2,-9,-2,-4,5,9,5,6,-10,-2,-3,7,5,5,3,6,-2,6,6,-7,9,2,4,8,2,-7,10,-6,3,-1,-7,4,1,-3,1,7,-8,6,6,-5,3,3,5,-10,-3,7,-9,-9,-10,-7,-2,2,3,1,-1,-8,-10,10,2,-6,-3,5,5,-2,6,-7,-6,-10,7,6,10,2,7,-5,-4,-4,-7,8,-4,-6,-2,1,-2,-6,-4,6,-8,-4,-2,4,2,-4,-8,1,-5,-4,-10,6,8,2,4,-6,8,-7,-8,10,-10,1,9,2,8,4,3,-1,-1,2,1,-10,-5,3,8,3,6,-6,5,10,3,3,-3,6,-9,9,-6,3,6,5,7,-1,-4,-9,-4,6,2,-5,6,-9,10,9,9,-7,5,-8,-4,5,-6,10,-5,9,-6,2,-6,10,-1,3,-8,4,6,6,-10,9,9,-6,-6,2,9,-7,-9,2,4,9,-6,5,-4,2,-6,-10,2,9,-2,1,7,8,-3,-5,8,10,8,7,-10,7,-10,9,4,-10,-9,10,9,1,10,2,1,-3,-9,2,-9,-5,8,1,-2,-10,3,8,-10,7,-6,-8,-1,7,-1,-9,-7,-9,8,7,-4,10,7,-1,-6,6,7,10,-7,8,-3,-10,9,7,1,7,1,3,5,6,4,5,8,-9,-10,6,-2,-6,-4,-10,7,10,-7,9,-1,-5,-8,6,6,4,-10,3,-5,-7,-2,-5,6,-8,-2,-7,3,-6,2,7,-5,6,-9,9,8,4,3,-10,7,-2,-6,-2,10,-7,9,-2,5,10,-9,-10,5,8,5,6,7,-3,-8,-3,2,-3,-4,-5,-5,4,6,-4,8,-8,1,7,4,4,-6,10,-4,8,10,-8,-8,10,6,2,5,9,4,5,-9,-9,3,-2,4,9,-3,10,1,5,3,3,9,-3,1,2,6,-4,5,-10,-6,-5,-5,-10,5,4,-3,6,-9,7,-9,-10,10,-8,10,4,-4,-4,-3,3,-10,-6,4,-4,-2,-4,10,10,10,5,-5,-7,-9,7,-7,-2,9,-9,1,-7,6,6,9,-6,-5,10,-3,8,-2,-5,-9,-6,-4,-3,-2,-10,4,-4,3,4,4,-7,-3,-8,3,-5,-10,-1,8,1,-4,10,-8,-3,-6,-8,-10,-7,3,-9,-9,-7,5,-5,-3,5,-9,7,1,8,-6,-10,-3,-9,-2,-3,3,10,-9,1,1,-9,-2,8,6,-3,-4,9,7,4,-8,-10,6,-9,7,6,7,-8,2,4,-2,8,-7,-3,-7,-6,5,-6,-10,-7,6,-2,-9,-3,8,8,-2,6,-5,6,8,-9,-9,-4,-9,-3,4,-7,10,5,5,6,4,-9,-10,3,6,-9,-6,-4,-3,9,6,2,3,-2,5,-8,-9,-7,9,-9,3,-1,-2,-3,6,4,-5,-6,6,-9,-7,7,1,6,-6,-8,-2,8,-6,9,-3,3,-9,-8,-8,-5,1,2,-10,3,-5,4,10,3,5,7,7,5,1,-1,8,8,2,1,-10,7,-5,-5,5,10,-2,-7,9,4,-7,2,5,-7,10,6,-4,7,3,4,-2,7,1,4,10,-9,5,4,-1,-6,3,-1,4,-6,-2,5,5,1,-8,6,-4,-6,-8,10,3,10,-7,-3,-3,-8,-1,10,-4,4,7,-1,8,-2,8,-8,10,-5,3,8,8,10,8,9,-2,-6,-4,-1,-4,1,-5,-1,8,-1,-7,-6,6,6,7,-8,8,-7,-10,-7,1,6,-8,2,4,-7,-4,-8,1,4,1,7,5,4,-4,2,10,1,5,-1,7,-2,5,1,5,-5,9,-8,8,10,4,7,-9,9,2,-5,-2,-1,-8,-4,-10,-9,-1,-3,-10,10,6,5,6,9,6,6,-10,2,1,-1,4,-2,-1,-3,10,3,3,-9,-4,6,2,-5,-10,10,-4,2,5,1,9,-4,-9,4,7,-10,2,10,-7,8,-1,-7,-1,10,-5,1,9,4,6,-10,1,-3,-6,-9,-7,8,-5,-2,-8,-4,5,8,5,-2,7,-4,-3,-3,2,-4,9,7,-9,-2,-1,-1,-6,-10,8,-1,-7,-7,-6,1,-2,-8,-7,9,-4,-6,-9,-3,3,-5,-9,-9,-5,-9,7,-8,-5,2,-1,-1,-1,-2,-1,5,-10,8,-1,6,-1,7,-6,-7,-3,-4,-9,9,-9,2,8,7,-10,-9,-10,-6,-1,1,10,-6,-8,-7,-5,-10,-7,-8,10,3,10,2,7,3,3,-5,3,-7,-2,-9,-9,5,1,-3,9,-2,7,9,4,-4,-7,3,10,2,-2,-1,9,-9,9,1,7,5,7,-10,7,1,2,-3,-2,6,-5,7,5,6,7,2,-1,9,-10,-3,6,-10,-6,1,-9,3,6,-9,5,4,3,7,-2,3,9,10,8,2,-4,-5,1,-8,8,-7,3,7,7,1,10,3,10,3,-5,5,1,2,-7,-9,10,-10,-7,-10,-10,-6,-6,10,-2,5,9,5,-9,-1,1,-5,-8,-3,-1,1,-3,2,4,5,-6,-1,2,6,-7,10,-9,-7,10,-1,-5,4,9,-9,-9,-1,7,-3,-10,-10,8,-4,-7,-3,5,1,8,7,-3,-2,-3,9,-5,-8,-1,-3,-10,-5,2,-5,-2,6,-2,-7,1,7,-4,-3,1,5,2,3,9,-9,8,9,-10,9,-9,-5,8,4,2,-3,1,-9,8,-4,-1,-9,9,-8,2,-1,6,1,1,5,5,6,-6,8,6,2,-9,8,-6,8,-2,8,6,3,5,1,-8,5,-2,9,-6,-9,1,-4,-2,4,3,3,1,7,3,-3,4,4,-10,-6,-3,1,10,10,8,-7,8,-10,-5,-5,4,-9,8,6,8,4,9,-5,1,-3,1,-7,10,-10,-6,-1,-4,1,-6,10,1,5,-7,10,-6,-6,1,-10,3,-3,-4,1,7,-10,1,6,3,-1,-2,10,-4,-8,2,-5,7,-5,-6,-1,-8,-7,2,-10,-5,-5,4,6,10,2,-10,-8,-6,-10,-7,5,-1,-2,-6,-5,-5,-7,-6,4,4,9,-2,-3,-7,-1,1,2,8,6,-6,6,-3,-10,-5,4,-10,-5,7,-3,8,-3,-9,2,8,-3,1,8,2,1,-2,-5,6,-7,8,1,1,5,-6,-9,-7,9,-4,9,4,-1,5,-1,8,5,-5,1,10,-9,-3,1,3,-7,8,2,8,-10,-9,-5,6,-4,8,-8,9,7,8,-3,9,-7,-8,10,-2,8,-9,10,-6,-8,-8,-3,6,1,7,4,-6,2,9,9,-2,3,-1,-9,-7,-1,5,-2,-5,6,8,7,-10,7,1,-1,4,-6,-8,2,-2,-8,9,10,6,-6,-6,8,2,-5,1,9,1,10,10,5,-9,1,-5,-3,-6,5,2,10,-1,10,-3,9,2,-5,3,4,-3,1,-7,10,3,-7,-3,10,2,-5,-7,-2,6,-1,5,3,2,7,8,3,7,6,-7,-1,6,-7,-2,2,-4,7,10,-1,-5,2,-8,-5,-6,-4,-7,5,2,-6,1,-4,-5,-6,2,9,-6,1,9,10,8,10,8,1,-9,8,-7,5,-5,8,10,7,10,1,-3,-5,-4,6,-2,6,4,-1,6,2,9,-1,7,7,5,5,1,-8,-4,-1,-1,-10,-10,-7,-9,8,-1,8,-8,-5,5,10,9,4,-2,4,1,10,4,-8,6,-10,-6,5,5,6,10,-7,1,6,6,9,-3,9,-8,-10,-4,3,1,3,-8,6,-4,-10,-6,-10,-6,10,-2,9,-7,-4,9,2,-5,-6,3,-2,-6,-3,1,-5,-4,8,-5,6,4,-4,7,-5,-10,-7,4,1,4,-10,-7,1,9,7,-6,7,-3,5,8,6,2,2,-7,-3,9,5,10,7,-7,5,-9,7,7,6,3,-3,7,8,2,-6,-7,-7,9,8,2,3,-8,-5,-2,8,5,10,-9,-6,2,-2,-3,7,4,-1,-9,-8,-3,-1,4,-10,-5,10,1,-6,10,-3,6,-6,-5,7,-1,4,7,-9,-9,9,3,7,-7,-6,-1,-9,-1,9,4,-4,2,9,3,2,8,5,3,5,5,7,2,-6,3,-1,-3,1,10,7,-7,5,-10,-9,2,-5,9,6,-9,4,-8,-10,9,8,-1,-5,2,8,-2,-9,2,5,5,3,-4,8,6,-6,-1,-6,-7,-1,-5,-5,7,-5,-5,10,-2,7,-4,1,-5,4,-9,-6,-3,9,7,5,5,3,-2,3,-8,1,5,9,-9,6,3,-8,1,2,-9,-4,-9,-8,9,-5,4,-8,-10,-1,-10,-8,-10,-9,4,-1,-10,-9,1,10,-1,-9,-2,3,6,2,-10,-8,9,-1,9,-5,-8,-10,4,-1,6,1,6,2,10,9,8,-2,7,9,-9,6,1,-6,-5,-1,6,-9,-7,-6,8,-9,-5,3,-6,7,-7,3,-7,4,-6,3,8,-6,-6,4,-10,-8,3,4,-4,-5,3,8,6,2,-8,6,6,10,8,5,6,2,7,-1,8,1,-5,-1,-2,7,-7,-7,-6,-6,3,-2,-7,10,-2,-4,-10,-4,-5,-10,-10,-8,-9,-2,3,9,1,5,-8,1,-8,2,7,5,-3,-10,1,9,-2,4,3,9,5,-2,-1,-2,-8,-8,-2,-9,-9,9,-5,-9,1,2,7,8,7,6,4,8,-4,-7,1,-3,-2,-2,1,4,5,10,9,-7,-9,-4,-10,-3,9,3,3,-2,-8,-2,6,-5,-3,-4,-10,-7,-3,-1,3,7,1,4,6,9,-10,3,10,-8,10,5,4,-10,-5,10,-5,2,7,-2,-3,4,-3,-1,6,5,-3,7,-4,-4,10,-9,-9,2,8,-8,6,-6,1,-1,-7,5,9,-7,1,-6,-5,5,-7,-9,-1,-5,1,6,-9,10,-7,7,-7,1,-8,-8,-1,7,9,2,-5,9,-8,-9,-3,-6,4,-8,-10,8,5,2,-8,-3,-5,9,2,7,4,-9,-6,9,10,10,6,9,1,-7,-8,-8,-5,-6,-6,9,10,-10,4,-4,-9,-4,2,8,5,-4,8,-8,10,2,-7,-9,2,1,1,10,-2,6,-10,-9,10,7,-7,10,9,7,-4,2,6,-2,3,-8,8,8,8,2,3,5,6,-7,-7,10,-1,-5,-10,-5,-9,-7,-6,-9,-4,-4,2,-5,5,3,6,-1,-10,3,5,2,-2,-5,3,5,-4,-4,-8,-5,1,-3,3,-6,-4,10,9,-5,10,9,3,3,-3,-4,-4,-4,-6,3,-2,-10,-10,-6,-2,-9,-1,8,-4,-1,-5,-10,1,5,-10,7,-9,-8,7,9,-5,4,9,-9,-2,-2,3,-6,-5,-4,-3,-4,-5,-3,-6,-4,3,8,1,-4,8,-9,-9,7,-8,-8,-1,-3,-5,-1,-1,4,4,-5,-9,-5,7,10,-1,-10,10,-9,-10,-7,9,8,2,3,5,-10,-6,-3,-1,9,-2,10,-4,-10,1,1,-5,9,2,3,9,4,-10,-6,-10,2,1,1,-1,2,-8,2,-2,3,3,3,-1,7,4,4,-8,7,8,-7,-10,-9,-1,-4,-3,9,2,10,-9,-5,-8,-10,-5,6,-4,2,-3,2,3,-7,2,-2,9,10,-7,-4,5,-1,-8,4,1,6,9,8,-6,6,-2,-4,8,-1,-8,10,-9,-4,10,-1,-5,5,-6,4,7,-2,8,-9,10,1,-7,1,-6,4,-4,6,-3,1,-3,3,-5,-8,3,-9,-9,2,5,-3,10,-6,-2,4,-5,-7,2,-8,-7,1,-4,-4,3,1,9,9,-9,6,9,-9,8,5,-7,8,9,-5,-10,-6,-5,2,-8,7,-8,-1,4,-3,5,2,-3,6,-10,5,-2,-4,9,-4,9,-6,-4,-3,-8,-1,-8,-7,-5,-3,5,-6,10,-5,6,-5,9,-1,10,-3,2,-3,9,1,4,9,-3,-10,3,-9,-3,7,6,8,1,6,5,6,-3,6,-3,9,-9,7,4,-4,-10,10,-6,4,10,-3,-1,-9,-5,2,-1,2,-1,2,6,-2,-5,-4,3,-10,-10,-7,1,-7,-10,-6,3,-9,-8,-10,4,-1,-6,-2,5,-3,-3,9,-4,-2,-9,-5,6,-7,-4,-9,10,-1,-6,-7,-3,7,-1,-1,5,1,-2,6,-10,-4,-1,7,6,-10,-1,5,-9,9,1,5,3,-1,2,-5,-10,1,4,3,-5,2,1,-9,2,-8,-8,-10,-1,-6,-6,-7,9,-10,-5,-3,-7,8,2,8,-3,-6,1,10,5,-5,6,-1,-10,-6,-7,7,5,2,1,1,6,5,-5,1,2,5,10,2,9,4,8,10,7,1,1,3,1,-7,6,8,-6,7,9,5,-9,1,-2,-1,2,10,5,-3,3,5,-1,-7,-6,-2,-6,-2,-6,2,-6,1,-4,3,4,8,-9,-7,5,-7,10,5,-4,1,-2,2,-6,7,-3,1,-10,5,1,-10,-5,9,-4,-3,3,-2,7,-4,6,4,4,7,4,3,-1,4,-2,3,-9,-6,-8,-1,2,-7,9,-8,-7,-6,4,-8,4,2,7,2,10,2,8,-5,9,1,-3,10,3,-3,-9,3,-3,9,-10,7,1,-10,-3,1,6,9,-10,-1,8,3,5,9,3,-9,1,3,-3,2,7,-7,5,4,8,-10,1,2,-1,5,10,-7,8,-6,-4,-9,4,-5,4,6,-7,8,2,-6,-10,-7,3,-5,3,-3,10,9,10,4,-7,7,1,-2,5,7,6,-10,-7,1,-6,8,-8,1,5,5,-6,-6,8,-1,7,-10,2,-4,-5,-9,-1,7,8,-7,-3,-6,5,-7,9,7,4,9,-9,4,-9,-5,4,8,-1,-6,9,5,-4,-8,10,1,7,1,4,-10,-10,1,-8,-7,-8,-5,-7,-3,-3,-7,8,-1,9,-1,-9,6,-3,-5,-10,1,-7,4,-5,6,8,4,-1,-1,7,3,-2,-7,-10,7,5,7,-2,-6,6,8,-5,-9,7,9,3,-2,-3,-9,9,2,-4,6,7,-3,-5,-6,3,-9,5,-4,9,3,-5,4,8,10,4,6,-7,4,-1,-4,-6,-5,-10,9,-7,1,5,-7,-1,3,-2,-7,-1,1,-1,-8,-8,10,-4,-9,-1,6,-6,-9,10,4,-4,-1,2,-8,-8,2,9,-6,-10,7,-5,-9,6,10,3,-5,5,-3,9,3,-8,-5,-6,-2,-8,-10,-2,6,9,1,9,3,4,-4,7,-2,2,-4,10,5,-4,3,-3,3,4,-8,-4,1,-6,2,-2,-10,4,3,9,4,-4,-1,-5,-1,-2,3,9,-5,9,-8,-4,5,2,5,-7,-5,7,8,-2,-2,9,10,9,4,-5,-9,3,-10,-2,-6,-4,-10,9,-5,-8,-5,4,6,3,3,4,-6,6,2,10,8,9,5,7,-8,6,-3,-1,4,-1,-9,-9,-4,2,6,5,6,-4,-3,10,6,-5,8,10,-9,9,7,-4,4,10,7,-5,-1,-3,-10,8,-3,-6,10,-3,6,4,1,-4,-5,6,-10,-5,10,7,-3,5,-7,-4,-7,-3,-10,-6,-6,-7,-5,-3,4,7,-5,1,9,-3,10,-5,-6,-10,7,7,-8,-6,-7,-1,-4,2,-5,7,-2,-2,10,9,-6,-2,7,-6,-6,-10,-1,4,9,5,1,-8,6,5,-7,-2,3,4,3,-7,-4,2,7,-1,1,10,9,7,8,-1,-8,6,7,3,1,9,-6,1,6,-10,7,3,8,3,-5,10,7,5,9,-6,-10,8,-7,-1,-10,-3,1,-4,7,-6,2,-4,-6,-5,-8,7,-7,6,-3,-6,-8,-9,7,9,-9,-6,4,3,10,-5,8,-8,7,8,1,-3,5,7,3,5,10,6,3,4,-7,4,2,-2,-8,-9,6,-5,5,-2,7,-2,-9,2,8,-7,-6,-2,-5,-7,5,-1,1,-2,9,5,-3,6,7,-6,-8,2,2,-4,8,-9,9,-4,7,7,1,-3,-10,6,8,4,3,-10,10,3,7,-3,-3,9,4,-5,9,-9,8,8,-7,2,8,4,-7,-8,-10,-1,7,-4,-7,5,-8,4,-10,-4,5,-7,-9,1,-10,10,-9,5,-2,-8,-8,2,-7,-2,9,4,-1,6,-1,-7,7,3,10,-3,-6,9,4,-2,10,-2,1,4,6,-3,1,10,-7,6,-2,8,-2,4,10,8,9,10,5,-1,4,-2,3,-2,6,8,9,-7,-4,-6,6,-6,-6,-4,-10,4,10,8,-7,-4,10,-10,-9,-7,-8,1,9,-9,-2,7,-10,6,6,-3,-6,-7,-2,-7,-6,6,-9,7,4,2,9,-10,10,-8,1,1,-2,-6,-7,-5,-7,-4,10,6,-7,2,8,6,-7,8,8,5,-8,-4,4,-8,2,7,3,-8,2,10,-9,1,1,-1,-9,-2,-7,-3,-8,2,-1,4,4,8,-9,9,-5,3,10,-6,10,7,6,10,9,4,5,-7,7,7,4,-3,6,4,9,6,-9,1,-1,7,-5,1,8,-8,-3,-10,-1,-5,-10,3,-10,1,2,-5,2,-4,-3,-6,-2,8,1,4,3,-9,8,-4,-2,8,-10,-8,4,-9,6,-10,2,-8,5,5,1,3,-7,-10,6,5,-8,8,3,-9,-5,-1,-4,-9,1,9,7,3,-10,3,10,2,10,-10,-9,6,-7,-10,6,-1,5,-10,3,6,-8,-1,-8,-6,3,3,-4,-8,6,3,-9,-6,6,7,-9,3,2,6,7,10,6,3,-4,3,9,9,-2,-2,-3,10,-2,1,-6,-5,9,-6,1,-6,-10,-5,5,-9,-1,7,-2,7,-9,7,7,10,-9,2,-6,5,7,7,3,1,8,7,-3,1,5,7,2,-8,6,1,8,9,5,9,1,4,-6,-9,-7,10,10,4,9,-3,3,6,-1,7,1,5,-6,3,-10,-10,7,-9,-1,1,6,-2,9,10,-5,5,5,-9,-9,-2,9,3,3,-2,-6,2,-6,-3,-4,-4,-2,-4,1,7,-6,-6,-2,-10,5,-9,5,-5,8,8,4,1,-1,4,-8,1,-9,-10,7,6,-4,-3,8,1,-9,-8,-1,9,-5,5,6,-1,2,-6,3,-3,8,-5,-5,10,5,6,-10,9,2,1,1,-2,3,-4,-1,3,-2,-4,7,2,6,2,-5,-3,7,4,8,-1,-4,-9,-1,-4,3,9,-6,5,-8,-9,-8,-1,-6,2,-1,-7,9,1,8,-10,-5,-4,1,2,6,4,4,8,-2,-6,-5,-9,-8,-4,-8,-9,7,-4,3,-8,9,-3,-9,5,-3,-6,5,-5,-6,1,-5,-6], dtype = "uint8")#candidate|3852|(4576,)|const|uint8
call_3851 = relay.TupleGetItem(func_2254_call(relay.reshape(call_3847.astype('uint8'), [416,]), relay.reshape(const_3852.astype('uint8'), [4576,]), ), 0)
call_3853 = relay.TupleGetItem(func_2258_call(relay.reshape(call_3847.astype('uint8'), [416,]), relay.reshape(const_3852.astype('uint8'), [4576,]), ), 0)
output = relay.Tuple([call_3789,call_3818,call_3847,call_3851,const_3852,])
output2 = relay.Tuple([call_3790,call_3819,call_3848,call_3853,const_3852,])
func_3855 = relay.Function([], output)
mod['func_3855'] = func_3855
mod = relay.transform.InferType()(mod)
output = func_3855()
func_3856 = relay.Function([], output)
mutated_mod['func_3856'] = func_3856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3226_call = mod.get_global_var('func_3226')
func_3227_call = mutated_mod.get_global_var('func_3227')
call_3870 = func_3226_call()
call_3871 = func_3226_call()
func_1911_call = mod.get_global_var('func_1911')
func_1912_call = mutated_mod.get_global_var('func_1912')
call_3881 = relay.TupleGetItem(func_1911_call(), 4)
call_3882 = relay.TupleGetItem(func_1912_call(), 4)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_3901 = relay.TupleGetItem(func_782_call(), 1)
call_3902 = relay.TupleGetItem(func_783_call(), 1)
output = relay.Tuple([call_3870,call_3881,call_3901,])
output2 = relay.Tuple([call_3871,call_3882,call_3902,])
func_3905 = relay.Function([], output)
mod['func_3905'] = func_3905
mod = relay.transform.InferType()(mod)
output = func_3905()
func_3906 = relay.Function([], output)
mutated_mod['func_3906'] = func_3906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3515_call = mod.get_global_var('func_3515')
func_3516_call = mutated_mod.get_global_var('func_3516')
call_3961 = relay.TupleGetItem(func_3515_call(), 0)
call_3962 = relay.TupleGetItem(func_3516_call(), 0)
output = relay.Tuple([call_3961,])
output2 = relay.Tuple([call_3962,])
func_3968 = relay.Function([], output)
mod['func_3968'] = func_3968
mod = relay.transform.InferType()(mod)
mutated_mod['func_3968'] = func_3968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3968_call = mutated_mod.get_global_var('func_3968')
call_3969 = func_3968_call()
output = call_3969
func_3970 = relay.Function([], output)
mutated_mod['func_3970'] = func_3970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_3977 = relay.TupleGetItem(func_1426_call(), 2)
call_3978 = relay.TupleGetItem(func_1428_call(), 2)
output = call_3977
output2 = call_3978
func_3984 = relay.Function([], output)
mod['func_3984'] = func_3984
mod = relay.transform.InferType()(mod)
output = func_3984()
func_3985 = relay.Function([], output)
mutated_mod['func_3985'] = func_3985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3240_call = mod.get_global_var('func_3240')
func_3242_call = mutated_mod.get_global_var('func_3242')
call_4035 = relay.TupleGetItem(func_3240_call(), 0)
call_4036 = relay.TupleGetItem(func_3242_call(), 0)
output = call_4035
output2 = call_4036
func_4048 = relay.Function([], output)
mod['func_4048'] = func_4048
mod = relay.transform.InferType()(mod)
output = func_4048()
func_4049 = relay.Function([], output)
mutated_mod['func_4049'] = func_4049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_4061 = func_318_call()
call_4062 = func_318_call()
func_3390_call = mod.get_global_var('func_3390')
func_3392_call = mutated_mod.get_global_var('func_3392')
call_4066 = func_3390_call()
call_4067 = func_3390_call()
output = relay.Tuple([call_4061,call_4066,])
output2 = relay.Tuple([call_4062,call_4067,])
func_4079 = relay.Function([], output)
mod['func_4079'] = func_4079
mod = relay.transform.InferType()(mod)
output = func_4079()
func_4080 = relay.Function([], output)
mutated_mod['func_4080'] = func_4080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3855_call = mod.get_global_var('func_3855')
func_3856_call = mutated_mod.get_global_var('func_3856')
call_4114 = relay.TupleGetItem(func_3855_call(), 2)
call_4115 = relay.TupleGetItem(func_3856_call(), 2)
func_2254_call = mod.get_global_var('func_2254')
func_2258_call = mutated_mod.get_global_var('func_2258')
const_4124 = relay.const([-1,4,1,-7,9,-2,8,-7,3,4,9,-2,1,2,-9,-9,-7,2,-9,6,6,2,-3,2,-4,3,2,-8,9,-7,2,1,-9,9,1,-9,-1,-8,1,-2,8,8,1,3,5,8,-7,9,1,5,3,-8,4,-1,-10,8,8,-8,-2,-9,-2,-6,-8,-5,5,3,-4,4,-9,-1,-10,6,6,5,2,5,-2,3,8,-9,7,-2,-2,-9,3,-9,8,1,7,2,-1,-7,9,-3,7,-1,3,-7,10,-6,-5,-8,-10,7,-4,-1,7,9,8,-3,3,9,-9,-1,-2,4,3,10,-10,3,5,10,-1,-8,-1,4,-6,2,-1,4,1,1,-1,-7,8,-6,5,-7,-5,7,-7,-1,-8,-8,-7,4,-4,2,-8,6,-1,10,-6,-4,3,8,4,5,-2,1,-7,7,-10,7,-8,-5,-3,4,-6,-2,-2,9,10,8,-8,1,-3,-9,5,-4,-6,1,6,9,-6,10,-1,-5,-4,-1,3,-10,-10,1,2,10,4,9,9,-1,1,4,-10,-1,4,-7,-5,3,-5,-3,-2,6,6,-6,-3,1,-8,-6,-8,3,10,-6,6,-4,-6,7,-2,3,-8,5,8,7,-5,-4,-9,-2,4,6,9,-10,-7,-10,8,6,-4,7,-9,8,7,-4,9,-5,-5,-5,-3,7,10,10,3,-3,-9,9,-5,9,-8,-8,10,-2,-8,-7,-9,-2,6,-6,8,-5,10,-4,-10,-8,-7,-7,-4,9,-3,-3,-5,-1,7,-9,7,-1,-8,3,-7,8,9,-8,-4,5,7,2,-2,-2,-2,-1,5,-7,6,-10,-5,4,6,7,1,1,-9,-10,10,10,-3,3,3,-10,4,-2,10,2,-10,-10,-2,-10,6,2,4,-7,2,-4,2,4,5,4,3,-3,-7,-7,4,10,9,-5,3,-9,-2,10,8,9,-3,9,8,-1,7,-4,7,-4,-5,9,-8,4,5,3,9,5,4,-8,-9,7,-8,10,6,-2,-10,-10,-1,-8,8,10,-3,1,-2,-10,-9,7,-8,1,-1,-7,-3,-1,1,3,-3,9,9,-3,-9,1,2,3,7,5,8,10,7,8,-3,7,7,1,-6,-6,-1,-10,7,2,1,3,-7,1,-4,-4,-3,2,9,-5,-2,-9,-9,4,4,1,3,-5,9,-6,4,-10,3,6,-7,-6,-1,2,3,6,-3,-5,3,7,-5,-4,3,7,-8,-7,-1,6,5,1,-5,9,6,-4,-5,10,6,-8,-8,6,-7,10,3,9,-3,9,-9,-6,4,5,-3,-9,1,-9,-4,6,7,7,-2,-9,9,3,-8,-5,10,-2,-7,3,8,-10,6,-4,-1,-2,-7,8,-1,-4,-1,-1,-8,-6,-2,6,1,-4,9,-10,9,3,-3,2,5,2,4,9,-6,1,-3,10,1,1,-2,-10,2,-6,6,10,-5,-9,6,5,4,10,2,-1,5,-3,-4,-5,10,-3,1,-10,-6,9,7,-5,-1,8,6,6,-5,6,6,8,-7,2,4,6,1,3,-1,-8,-5,6,10,-3,-3,-4,4,-2,-5,-9,-4,-9,2,2,-2,8,9,-1,5,3,6,-6,-3,1,3,-5,5,-2,9,4,8,-1,5,-7,-7,-10,-10,-3,-7,1,4,-8,1,8,6,9,4,-1,3,3,10,3,2,-5,10,-10,9,3,-8,7,-5,-9,10,1,-2,3,8,2,-2,8,2,-6,5,-2,-4,-10,9,1,-3,-3,5,-7,-2,2,7,-7,9,9,-7,-1,-1,-2,-4,10,-5,2,-6,2,7,5,-7,2,-8,-2,-3,-7,-5,5,-2,-7,-5,-7,-8,-1,5,1,-8,8,4,-2,4,-1,8,10,-8,-9,8,4,-6,-2,-2,-3,-6,6,-2,6,10,8,-1,10,-7,-2,4,2,-4,-3,9,-5,-8,4,-1,-7,-6,-1,-5,-8,-9,-9,8,-4,-8,-9,2,2,6,9,6,10,-3,1,-1,10,1,4,-1,-4,-7,7,-6,9,-7,-9,8,-7,10,9,-8,1,10,-3,-6,-1,-9,-4,9,6,4,1,5,-3,7,-8,10,-6,-7,-1,-5,7,3,8,-5,-8,-10,-10,-6,-1,4,-7,1,7,4,2,-2,-5,10,-7,-10,5,5,-8,-10,-3,10,-1,7,6,7,3,7,-4,-5,-4,-7,6,6,-2,-5,-3,7,4,3,7,10,-9,10,-7,-8,10,2,9,10,-6,-8,-9,-2,-3,5,-5,8,5,1,2,3,-7,8,4,-9,2,-9,6,-4,-8,-7,-5,1,6,1,3,8,8,-8,-3,-5,6,-5,-7,3,7,2,-8,3,-7,10,8,-2,5,1,6,-4,-7,-9,8,-2,4,9,7,4,6,-3,-3,3,4,-7,-7,7,1,-10,7,-6,-8,-3,-8,-8,-10,-9,6,2,-5,2,-3,7,4,3,-1,-2,-3,-3,-1,-5,4,5,-7,1,7,3,-10,-4,-8,-6,5,8,-3,8,6,7,1,-9,1,10,3,10,6,8,10,-4,1,2,5,-8,-5,-10,-8,-5,-10,7,-2,5,-10,1,4,-4,9,9,-7,-4,3,-1,4,-10,-2,-6,-5,-2,3,-6,1,3,9,6,10,-2,-6,6,8,-4,6,-7,-2,-7,-6,-3,-6,-9,-10,-2,-4,7,-7,2,10,8,-8,6,-7,7,7,-10,-8,-9,3,3,6,-9,-5,-10,9,-1,-4,8,-2,-5,-5,-6,-4,-3,6,6,6,-7,-8,-5,5,-5,7,-2,-6,-1,-2,4,-2,2,-3,-10,-6,1,3,1,6,-9,-9,1,10,6,7,-9,-9,6,1,-2,-2,9,10,3,7,-6,-7,-2,9,8,-8,-6,9,-8,8,5,4,7,-5,-10,4,-9,-5,7,-8,1,-3,-2,8,3,9,-6,-2,-7,-5,9,4,-10,6,-2,-4,10,-9,2,-2,3,-2,6,-4,-1,1,8,-6,4,-8,6,-1,-1,-9,-8,-9,4,-10,5,5,-10,-4,2,7,-3,4,8,8,-6,4,9,4,7,6,-7,8,7,-8,-5,9,-9,-9,-10,6,-5,-9,6,-10,5,-6,6,2,7,6,-2,-10,-10,9,6,-4,-8,5,-6,8,10,-4,10,-4,3,-9,-7,-9,7,-6,5,-4,-5,-8,6,2,2,4,1,8,-10,-2,-5,-3,-9,7,-1,7,-10,4,-3,-1,2,8,7,-9,1,3,2,-10,7,7,8,1,-2,-3,-1,1,-2,-9,5,6,-9,3,9,6,-1,-3,10,-7,10,7,-6,5,7,9,-1,-7,-7,6,6,-1,7,-7,7,7,-6,7,5,2,-7,6,-7,2,5,-10,-2,-1,-3,3,-4,5,7,2,7,5,-6,-4,4,-8,6,4,-9,4,-1,1,-9,5,-10,9,-2,3,-5,-4,-5,-2,10,-8,8,10,10,7,8,7,-1,-9,-3,5,-9,1,-9,6,8,8,-5,7,10,5,8,-7,-10,-3,9,3,5,4,6,5,4,-9,-4,2,-10,1,1,-6,4,-6,-7,1,-2,10,-6,9,2,7,-4,-7,8,-2,-6,1,-10,-5,5,-1,-2,6,-7,6,-3,-3,-3,-3,10,9,-4,8,-7,-10,-10,1,3,-1,-2,-10,-1,-4,-5,7,-2,3,-7,1,5,-8,6,10,7,-2,8,6,6,6,-8,-9,9,10,5,2,7,-7,-1,4,8,-9,-7,8,6,5,6,8,-5,3,-2,-10,-5,1,5,4,-1,-2,7,-2,-3,-10,-10,-4,7,-7,-2,-9,5,3,-7,-3,-9,5,-4,-10,3,-6,8,-9,7,5,2,-6,-4,-7,7,7,7,-5,-10,-8,5,-7,-3,-10,-4,-10,7,-3,7,1,-2,-4,-2,-9,-4,-7,-10,3,-3,-4,10,-5,-1,9,10,4,8,-10,6,5,6,-8,8,-10,8,10,-9,4,-3,8,1,-7,1,-1,9,-5,-8,1,-8,-9,-6,-2,-3,-5,-7,2,-6,-1,6,-1,8,10,-3,-3,6,7,10,9,8,-10,8,7,8,-2,-9,-1,-1,4,4,6,1,3,7,-3,-9,-1,4,2,3,-8,7,9,10,5,-3,5,-6,-5,4,9,-10,10,-6,8,6,-4,-5,4,-8,-1,-2,5,9,-3,8,4,-10,-6,7,-10,7,-8,8,-10,-1,-7,9,10,-4,9,-5,-3,-7,5,-10,5,-10,-4,4,-5,4,9,8,3,4,-5,7,6,-7,-8,-8,8,7,-6,-5,8,-7,-5,6,-8,-2,-1,-2,-10,8,10,10,-3,8,-10,2,-2,-4,-3,-5,-3,3,5,-1,-6,5,-6,-4,4,10,-6,-1,-3,-7,5,7,-10,-4,-10,10,-5,-2,1,-1,9,-8,-6,-5,-4,-5,-4,-9,-7,-9,-7,2,5,-2,-1,9,4,7,6,9,4,-7,8,-5,8,-1,5,6,9,-4,8,-10,-3,-4,-9,-7,7,-3,1,-2,-4,-5,-8,8,-6,8,8,-8,-7,7,5,2,7,1,-5,-8,-7,7,1,-3,-10,3,-10,-8,-3,-4,-9,2,-2,-6,5,-6,-7,8,-10,7,3,-9,-2,2,2,-6,4,6,9,5,-8,-6,5,4,-8,-9,-2,-6,3,-4,5,5,7,7,5,-2,2,7,4,7,4,-5,-4,3,-10,-2,6,-6,1,9,-5,9,8,9,7,8,-1,8,-5,-3,-9,-1,4,-7,3,1,6,-9,5,-8,3,-4,8,-2,-6,-9,-1,1,10,-2,-4,2,2,6,-7,-2,2,-7,-9,-5,-3,1,3,-3,1,-7,-8,-7,-10,8,9,10,-5,2,-5,2,-9,3,-6,-6,-2,2,-2,10,1,-9,-7,2,7,9,-8,9,-5,-3,1,-8,4,2,-10,-8,-10,1,-8,-1,-4,-7,3,-4,-10,-9,-6,-3,8,6,8,9,3,-5,-3,-7,9,3,-10,10,4,3,8,-10,-3,-4,-10,-1,5,3,-4,-4,4,5,-4,6,-2,-6,6,9,-2,-10,-8,-5,-9,-10,1,-6,-3,1,-3,3,-5,-8,-7,-10,-1,-3,-3,1,-9,5,-7,4,-9,5,-3,7,-9,9,-3,-7,1,-3,-6,-6,-5,4,-9,2,-7,-10,-5,-8,-6,-2,-8,-3,-7,-1,9,10,8,8,6,7,-4,2,6,6,9,-10,7,5,-8,-8,4,4,4,1,-9,3,-3,-7,-7,2,-10,-2,-8,10,-3,-4,8,1,10,-2,-10,6,-10,-4,-5,4,1,-2,-4,4,3,-8,-7,-3,-3,-10,9,-6,-9,7,-9,9,8,-8,6,-10,3,9,7,1,-6,2,-6,-4,9,9,4,-9,-9,-3,-2,-5,-2,-4,-4,-10,-5,6,1,6,-5,9,1,10,-6,9,7,-2,6,-8,3,1,-10,-9,10,10,-8,-3,-6,1,7,9,-1,2,7,10,-10,7,-9,-9,-2,4,-8,9,9,6,-1,1,6,-1,-7,-6,-1,7,9,-1,-4,1,2,-8,1,9,10,3,-5,-2,5,-9,1,8,-1,1,4,9,-1,6,-10,-3,5,8,-10,2,6,-4,7,-7,3,-4,-1,10,10,3,1,2,-1,7,9,-9,-1,4,-6,-4,10,-3,-3,-4,-9,2,-2,-7,5,4,-3,2,5,2,8,10,6,-10,8,-1,-8,8,-9,3,-9,9,10,-6,7,8,-3,-5,4,9,7,1,-5,7,4,-10,-7,-6,2,3,7,-7,10,3,-5,-5,2,-10,-3,-3,-7,3,-3,2,-9,7,4,10,5,-7,-6,7,-6,-5,3,9,2,-5,-1,10,-10,7,2,10,-1,-2,-9,4,-5,8,8,8,-1,5,-10,9,-4,5,-4,-7,-2,-1,-7,8,-4,10,6,-2,-2,9,5,-1,-6,7,1,-4,-3,6,10,2,2,5,-9,-7,7,-3,3,1,4,9,2,-10,10,4,2,3,-5,4,-7,-7,6,-7,7,10,6,7,-7,-2,5,-7,2,-10,8,5,6,2,-3,3,-6,1,4,-9,-7,10,-9,-8,6,-1,2,2,7,10,-10,10,-7,8,-3,4,10,-3,-8,-1,6,9,-8,-6,4,5,-8,-1,-9,6,-8,3,4,-8,-4,-7,10,10,8,3,3,-5,4,-8,7,-5,6,-2,2,3,8,8,-7,-8,-4,6,-8,8,6,-4,-10,7,-5,-6,-10,4,-10,-8,9,-3,-6,10,-9,5,-6,10,8,-4,8,-1,-9,-6,7,8,-1,-1,-10,-10,-1,8,-4,5,-6,6,-7,10,-1,-6,2,4,-5,-8,-8,-5,5,-8,2,2,10,-1,2,6,-10,2,8,-3,3,-9,-4,-9,10,8,9,-1,8,10,5,-5,-8,-7,5,9,-5,-6,-5,-8,2,-8,-7,-2,10,5,5,10,-7,10,-7,9,-9,1,-9,2,4,-4,8,-4,-7,-4,8,-8,1,6,-8,1,9,-5,10,2,7,5,-2,-4,9,-9,-1,4,4,-1,-7,2,-2,-6,4,6,-4,5,-9,2,6,-5,-10,-9,10,-9,-2,-3,-9,7,-7,-3,4,-4,8,3,9,10,-8,4,-9,-5,5,5,6,-5,7,-3,-7,-5,5,8,-7,-3,-7,1,1,7,5,-10,-6,-4,-5,5,6,-9,-8,-6,5,-10,-6,10,-8,-3,-9,-1,-8,-7,6,8,-9,-4,6,-4,7,5,4,1,2,-2,-5,-5,2,9,-1,-9,-6,1,-2,4,8,5,5,-3,-9,8,-2,10,-3,9,8,6,2,5,-10,-5,8,-10,7,-8,10,4,-8,-5,5,-5,-3,-6,-6,-1,10,7,-10,-1,-4,-5,6,8,6,-3,9,-4,10,-9,1,-5,8,8,-2,-4,7,-3,-1,-7,4,9,-9,-6,-3,7,5,-4,5,10,3,6,-5,3,7,4,1,5,-8,-8,5,4,9,-4,2,-4,8,-4,-8,-1,-8,-6,-2,-8,-1,-9,4,-6,-3,-9,-4,9,2,7,2,-5,-6,-9,2,-9,8,9,3,-6,6,1,-6,-4,-6,8,-10,8,6,6,-7,-10,5,6,5,-4,5,10,8,2,2,9,3,-2,5,8,3,6,7,5,3,-2,-7,-2,4,-6,-3,2,4,-6,2,-2,2,-2,-1,-3,-6,-5,-7,7,-2,-10,10,3,-6,5,-5,-4,5,7,4,-10,-5,5,-1,-5,-7,-8,-9,-3,1,4,4,-2,3,-7,-9,9,-2,-6,-9,8,8,-3,10,-1,-3,-9,-2,-10,-10,3,-5,-3,-9,2,2,3,9,-6,-3,1,1,-5,-9,-9,3,8,8,-5,-2,4,10,-3,-5,-9,5,4,-8,-10,-7,7,3,-8,-9,-8,1,-5,1,-1,5,5,-9,-6,10,-5,-5,5,-2,-8,7,1,8,-10,-2,-7,10,-6,1,-6,-10,-7,5,-4,6,-7,-10,10,4,8,10,4,-7,7,-6,8,3,-2,9,5,-10,10,-1,-9,-10,-1,-2,2,-7,9,1,-9,5,3,7,-1,10,-8,-2,6,-4,4,-3,-9,-5,-4,-6,-3,4,6,3,10,-9,-2,5,-4,-4,7,7,8,4,10,-4,-2,-8,10,8,-5,-6,9,-7,-2,-3,10,5,-2,1,9,-5,-4,9,-4,-1,5,8,-3,-7,9,2,-2,7,-5,5,4,5,5,-1,1,10,3,10,-4,-9,-8,2,9,3,-10,6,-10,-3,6,-4,5,-5,-3,-2,-3,-1,3,1,5,-4,4,-10,-2,9,-6,-5,8,-9,4,-9,-4,7,4,-9,-2,5,-4,10,7,-4,-6,-3,-10,7,-6,2,-7,-9,-7,-1,3,4,-10,-3,-4,9,9,-6,6,4,2,-4,-5,1,3,-10,1,-2,-8,9,6,-4,9,4,5,-7,-4,-7,6,-10,1,5,-5,2,-4,9,-8,4,5,5,6,7,5,-8,4,-9,-1,9,-3,-1,-4,8,-3,3,10,10,-2,-5,-2,7,4,-1,2,1,10,2,-4,6,-3,-7,-7,-1,3,5,1,-1,7,10,-9,5,-4,-3,-7,6,-8,-3,10,-3,1,10,7,7,-3,-5,7,-2,-7,7,-4,4,-8,8,-2,-4,-6,-5,6,-10,8,-1,-5,3,-8,6,5,-5,-10,2,-3,-4,-3,-5,-2,9,-10,2,5,-9,-8,-6,-6,8,5,7,10,-6,-2,-1,-6,4,-3,3,-2,3,-7,4,4,-9,-4,7,-10,7,6,8,-10,-9,-9,-5,7,4,10,9,-10,1,5,-9,2,8,-4,9,-1,1,3,2,3,-3,-3,-7,1,8,7,-2,1,-5,8,-1,2,-8,7,4,7,-2,-2,-3,6,-10,9,2,-5,7,10,-2,-9,7,2,7,-1,-10,-10,5,-4,-1,-10,-3,9,-8,-7,1,-1,-3,2,-2,10,5,5,-6,-6,2,-9,2,-2,-6,1,4,-8,6,-6,2,-8,-6,6,2,10,-1,-8,8,3,8,5,-7,8,4,10,9,-2,3,-6,3,10,6,5,5,-2,-4,-4,10,2,5,10,2,-9,-2,-1,-3,-7,8,-5,-3,-5,-3,-8,10,-7,-4,8,-10,2,-2,-5,5,-3,7,7,4,7,-2,10,-4,6,5,3,-3,-5,1,9,5,10,-2,2,-10,5,1,-3,-4,3,5,5,3,4,-2,-10,6,9,-9,-8,-7,9,10,-2,-3,6,-1,7,-10,5,-3,-9,7,9,-6,-4,-9,10,5,8,7,7,4,1,4,-6,-3,5,10,7,-10,8,4,-1,-9,8,-2,5,10,9,-2,-10,-7,-6,-9,-2,1,-10,-9,-5,-7,-6,9,-4,7,-4,8,3,-1,4,-9,-10,-10,7,-9,-8,5,-7,7,-5,7,-1,-3,2,-3,-5,5,-3,4,-4,4,3,-8,-6,-4,-9,-2,7,7,9,-6,-2,-10,7,7,-8,5,-10,2,10,-9,-8,-1,6,4,8,2,4,5,7,-5,4,-6,5,-2,-5,-3,-2,10,10,7,-6,8,-2,-3,6,2,8,-4,-8,-7,7,-8,2,-1,1,-2,7,-7,2,8,8,10,9,-10,-2,2,6,-10,-7,3,-9,5,5,-6,3,-9,-5,-8,4,-3,-6,-8,4,-3,1,9,2,-9,-7,8,-1,5,-5,-4,3,-7,-2,-1,3,7,1,5,9,2,8,-8,-6,-9,-5,2,-10,-7,4,-1,4,-2,-4,-10,-10,9,-2,-9,1,3,-10,-4,-6,5,10,8,5,-3,-6,2,-5,3,9,8,-1,5,-6,4,-1,3,-6,-9,8,10,3,9,4,-5,-8,-2,-6,2,8,-5,6,2,8,3,-1,1,4,4,-3,-10,4,2,2,3,4,9,-5,-4,-2,8,-1,-9,-8,-4,2,4,9,-5,3,-9,5,7,-8,-2,9,4,-8,4,4,8,3,1,1,-10,-3,1,8,-7,-10,-7,-8,6,5,-3,-9,4,-7,3,2,-2,4,-4,-3,9,9,-10,-8,-2,-10,2,8,-3,-5,-10,-2,4,8,-10,-9,2,-6,3,-3,-9,-2,4,8,-2,4,10,6,3,1,3,-2,-8,-9,4,-7,-5,-3,6,6,4,4,9,-9,-4,-8,2,3,-10,-10,6,-7,-4,-2,2,2,2,-4,-6,3,-5,6,-1,-7,3,5,-5,-2,5,-1,4,4,9,-6,1,4,10,-5,-1,2,-10,-5,1,5,-3,-2,-2,-4,-6,-10,10,5,6,-1,-2,2,1,-8,5,10,-2,7,-1,-8,1,-4,-10,1,8,-4,6,-2,-3,1,6,6,-6,-3,-3,-3,-7,-5,7,4,9,-6,3,-4,-10,4,6,5,2,8,9,10,-10,4,1,3,-7,5,-6,-6,-1,2,2,-1,5,2,1,-9,-6,-6,-10,-7,7,7,-8,-10,5,8,1,-4,9,2,7,-8,-6,-10,-5,-3,8,4,5,6,-7,-9,-6,-7,-10,-2,2,-10,6,5,10,4,10,-5,-3,8,5,-10,-2,-5,-6,9,-7,-4,-10,4,9,-7,7,5,-3,2,10,-1,7,-5,1,10,-3,-10,-7,5,4,4,-6,-1,-10,8,-5,2,-3,6,1,3,-2,10,-9,5,9,-5,6,3,-9,6,8,-7,-7,6,-8,-3,-1,-10,-8,-2,-4,-9,2,-6,2,6,-10,-10,3,4,-4,4,9,-4,8,-1,2,3,-3,5,-1,-3,4,-7,-1,8,7,1,-7,3,2,8,-6,-7,9,4,5,-10,-3,7,9,1,9,-4,-6,2,10,1,-2,-7,-4,-3,-8,-9,-2,-7,2,-7,-10,5,-5,-4,-6,3,5,1,10,-8,6,3,4,7,8,4,4,-3,-6,-7,4,-2,-1,8,-4,-2,-6,8,-5,-3,-10,2,-10,-6,4,1,-5,-8,-4,8,5,-10,-2,-10,-5,1,-3,1,8,10,-3,1,-3,-2,7,7,-9,4,7,-10,10,8,-2,9,-8,-3,9,7,-5,9,1,6,2,3,8,2,5,-3,2,-1,10,-1,10,-9,1,8,3,-1,-6,6,8,-1,-1,1,6,-4,-6,3,5,2,1,7,4,1,-2,3,7,6,6,-1,-1,-9,10,-4,6,-10,-6,3,6,-9,4,-2,-5,1,6,-4,-7,-6,4,3,-6,9,3,-3,9,-7,5,6,-6,3,-8,-10,9,3,6,7,2,-7,9,4,-3,1,-8,9,-3,-9,9,-8,-5,-6,-1,-4,-9,8,10,-6,-2,-2,3,6,6,-8,5,5,-7,1,-4,-10,4,10,1,7,-4,-4,2,4,-7,3,8,-2,-3,-4,-7,-1,-4,5,9,-9,-2,-2,4,4,-10,-3,-9,5,5,-8,-6,5,9,7,3,9,-10,-4,6,-6,-7,5,4,-5,-1,-3,-1,1,8,6,-6,9,-7,-10,10,-9,5,-10,-6,-7,-7,8,-9,-8,6,8,-10,-8,9,9,-6,-6,-4,9,1,-1,-8,-8,7,-4,7,-9,-9,3,-6,9,3,-2,-10,-1,9,-1,10,-4,3,-3,1,9,-8,-10,-7,6,-2,8,-1,5,10,9,-5,-10,4,-1,5,5,-6,-10,3,4,-6,9,1,1,8,-3,6,1,9,3,6,9,-2,-5,-7,-2,1,-4,3,-6,-5,4,-4,-1,1,-7,1,-8,-7,2,4,-8,-3,-7,-8,-7,-2,4,10,-9,9,-9,-3,7,-2,3,1,8,2,10,8,4,-2,8,-6,-4,-6,-7,-10,1,3,9,-5,-10,4,-8,-1,4,1,-7,2,1,-4,7,3,7,1,-4,3,-3,5,-1,2,-2,-9,9,10,-9,6,-10,3,-9,-5,1,4,-5,5,-7,-1,-1,8,2,-8,2,-7,7,10,-6,-6,3,3,10,5,-7,6,9,-6,2,9,9,6,8,1,-1,1,6,-3,3,6,6,-8,10,5,-9,5,2,4,-7,2,-2,3,10,-6,6,3,-8,7,2,-7,8,-8,3,-8,7,-10,6,6,-9,-7,6,9,8,1,9,2,2,-6,4,-7,6,9,-1,8,-1,7,4,1,-1,5,-2,7,-6,9,9,-2,-5,6,8,-8,-8,8,10,-5,4,10,6,-8,-10,-4,-4,3,9,-5,-3,8,7,-5,-5,-9,10,-3,-9,-3,-1,-10,-5,-6,4,1,-4,9,5,2,4,-7,3,3,4,-4,2,1,9,-2,-9,-10,-2,-6,-5,-4,-2,-5,4,8,5,4,6,-5,-3,9,9,-4,-2,-5,3,-8,-4,-9,-3,6,-8,5,6,-10,6,8,1,-6,6,-10,5,-3,2,-5,8,-5,2,2,-10,6,4,-5,9,9,-5,4,8,-6,7,7,7,-4,2,6,10,9,-7,10,6,-1,8,-10,3,7,1,7,-4,6,7,-9,5,1,-2,8,-10,-2,2,-5,2,-7,5,-1,-5,6,-1,6,-3,-8,8,7,-4,-6,-1,-3,10,5,4,-6,-3,8,5,1,-3,-5,6,-8,-8,-9,3,1,-2,1,-10,-4,9,-10,7,4,-2,-8,-10,-9,1,7,-9,-1,3,-8,1,10,3,-8,-1,10,-1,4,-7,10,-10,-5,-5,2,8,-3,-4,-1,-4,9], dtype = "uint8")#candidate|4124|(4576,)|const|uint8
call_4123 = relay.TupleGetItem(func_2254_call(relay.reshape(call_4114.astype('uint8'), [416,]), relay.reshape(const_4124.astype('uint8'), [4576,]), ), 5)
call_4125 = relay.TupleGetItem(func_2258_call(relay.reshape(call_4114.astype('uint8'), [416,]), relay.reshape(const_4124.astype('uint8'), [4576,]), ), 5)
uop_4128 = relay.log10(call_4114.astype('float32')) # shape=(8, 13, 4)
uop_4130 = relay.log10(call_4115.astype('float32')) # shape=(8, 13, 4)
output = relay.Tuple([call_4123,const_4124,uop_4128,])
output2 = relay.Tuple([call_4125,const_4124,uop_4130,])
func_4134 = relay.Function([], output)
mod['func_4134'] = func_4134
mod = relay.transform.InferType()(mod)
mutated_mod['func_4134'] = func_4134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4134_call = mutated_mod.get_global_var('func_4134')
call_4135 = func_4134_call()
output = call_4135
func_4136 = relay.Function([], output)
mutated_mod['func_4136'] = func_4136
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4150 = relay.const([[[2.561907,-9.304845,-3.661199,7.526442,-5.389636],[-3.672021,-8.950238,3.253024,-4.689295,-1.601060],[-3.476337,-5.532527,0.337809,0.333640,-4.338613],[-8.371309,0.534286,4.510189,-5.689991,9.110373],[-5.062068,-7.396464,7.993623,-1.228746,-1.648672],[9.064539,-5.924404,-2.418171,8.880964,-4.244073],[9.411612,-6.965900,2.316730,-6.518651,-8.518012],[-2.744268,-1.934688,-8.339489,-4.335989,5.435595],[1.305068,0.170204,-7.597838,9.734177,-4.734314]],[[5.641123,-1.793452,-4.592499,6.303539,2.812334],[-2.049615,6.391044,-1.727790,8.602396,-0.588290],[1.463468,0.066366,2.462481,9.181169,6.639119],[-1.954538,4.090500,-1.500415,2.045934,-3.092752],[-7.021039,-2.990249,5.358341,5.015523,-7.193665],[6.990729,5.136280,-7.479881,-4.019303,4.037697],[7.411008,-5.697517,-4.880979,0.289056,5.303121],[-6.670434,-4.597513,0.650482,7.308464,-4.535518],[-4.742905,-5.751798,-7.105674,1.049165,-5.794996]],[[5.579058,-8.254293,-6.757213,-8.138329,-4.325589],[0.873410,7.013172,-5.607436,-7.895362,9.086635],[0.345854,-6.307658,2.624788,-4.836821,-3.459799],[5.660484,2.510161,7.754500,-9.974948,5.544847],[3.291916,4.126958,-2.204187,3.812497,-1.481651],[-0.610351,9.994379,3.626655,6.242493,1.738356],[-5.907571,6.297936,-1.754912,0.278043,2.931904],[-7.052852,4.651665,1.714298,0.679608,-3.196640],[-9.731033,2.176548,-7.950365,-5.382490,-2.568436]],[[3.248712,2.951028,-7.150664,3.532671,-5.449553],[-0.104756,-2.173146,6.973901,-6.707028,-7.032685],[-3.432792,2.577168,-5.065589,-9.322745,5.831711],[-9.240227,3.289537,-5.720068,-8.065915,7.085711],[-0.175588,9.471957,3.140403,-1.795752,1.040146],[2.571860,6.829387,0.475416,-6.054929,3.675860],[-0.730125,-7.735953,9.150275,-4.662677,-5.660071],[-9.757907,5.770172,6.325546,-3.067704,-3.468934],[0.642995,7.069036,-7.642516,-1.549638,-5.695022]],[[9.008394,-5.328688,-1.161080,-3.886700,4.915675],[-4.717780,8.228494,0.539157,4.208045,-4.845718],[1.232929,3.447439,7.395130,4.624513,-3.067315],[1.852200,-2.683680,6.833168,4.172338,9.307193],[-5.234321,-3.266358,-9.688184,4.222896,-2.667201],[5.832876,0.946396,-1.289248,0.173778,-7.686752],[-9.103984,1.931078,5.391447,3.676948,-5.625427],[2.526750,7.068541,-4.436235,6.727335,6.475365],[1.889979,2.456304,3.827656,4.272361,2.108648]],[[-5.380149,6.757499,0.854953,-4.588525,6.037822],[1.705313,7.059789,0.808680,-2.901772,5.280788],[-7.007122,7.540957,8.137629,0.536256,7.041901],[2.247135,-2.344087,2.689154,3.221325,2.298461],[-9.412308,-0.141447,8.470566,7.195360,-0.873197],[1.102092,9.810204,8.540831,5.100257,-0.241744],[2.840794,-0.881932,-1.763764,0.605654,2.173828],[8.168694,-5.134088,3.212564,2.059928,4.386366],[-7.955475,-1.483744,8.950552,-9.451927,-1.529472]],[[1.165243,-3.972292,-0.771962,7.021731,5.112212],[-9.031777,-0.316532,-3.250808,-6.317512,-8.718721],[9.342818,-7.964859,4.203638,9.882779,-3.414231],[-0.423569,-3.250652,2.747864,9.708006,-8.571676],[3.368330,2.103997,6.401188,2.875916,4.315589],[-6.981276,-0.436562,-7.104201,-5.949699,-7.295328],[-9.738774,7.728124,6.909910,6.804355,7.750293],[8.430755,-4.378935,1.189586,-1.888503,7.259537],[-1.294594,1.038683,-1.078810,-6.988633,6.932225]],[[5.538345,2.331743,-5.560747,6.285307,-6.192255],[-9.130974,0.236958,-8.104907,-6.792787,3.118802],[4.020318,3.314411,7.902578,-5.265225,3.733983],[-6.968597,3.682456,6.515584,-4.120109,8.718627],[1.129014,8.544678,-7.049271,8.295204,-9.381709],[-4.008519,4.676439,-8.242063,0.753650,-9.831666],[5.902820,8.830431,9.009839,-8.947936,2.889137],[-7.333147,9.299970,3.537515,3.291747,0.621195],[-8.125600,4.242925,9.799851,-9.012294,2.187487]],[[8.519156,0.569119,6.744319,6.051277,-7.684539],[-2.672188,-6.583538,-4.248527,8.841161,-6.213379],[-3.097351,7.183616,-3.698726,5.262400,1.603737],[-7.809890,1.126447,-6.957041,-8.388559,7.347856],[-7.021404,1.051868,8.863327,5.660688,5.840280],[1.146718,-3.579694,-3.897137,-2.044212,7.710139],[-6.009173,-1.142579,8.285233,-6.670695,1.213736],[-3.003298,2.965738,-8.710870,-6.752304,-4.353456],[2.822992,1.182442,-1.552767,6.965062,5.723690]],[[-8.373394,-4.523500,-4.478595,1.030356,6.316963],[-8.900068,0.875264,1.425536,-7.438797,8.971818],[5.943241,4.721020,-6.461066,-0.754799,-6.660084],[-2.016363,3.845479,8.860695,-6.827666,1.221668],[0.649654,0.241166,5.820594,-4.685345,-0.753519],[-5.577416,4.047933,-6.721160,1.483466,1.703763],[5.234719,5.400033,-8.054282,-3.502402,4.141218],[-4.500136,1.179839,1.379458,-4.279677,-4.973684],[2.029146,-5.241142,-2.347255,-7.378889,-0.661063]],[[4.808426,9.209228,-6.113031,-3.846500,-9.158812],[-0.132237,-5.155643,1.298455,1.880095,-4.439747],[-8.680717,-8.371404,-7.741138,-4.574261,5.457098],[-4.183659,-6.698087,0.559811,7.031707,6.971277],[6.205389,-5.219038,2.324939,-3.353642,1.593685],[-2.973271,-5.060471,-7.652185,-4.776497,-8.809458],[9.700751,-9.083595,-9.255049,1.510970,1.636021],[-8.787897,-0.751600,4.149932,-6.407412,-1.947343],[-4.479714,8.147751,-1.021494,6.732580,-8.446923]],[[-9.323168,-9.497047,5.374439,-6.321911,-1.962205],[1.376434,-3.654807,9.691007,5.195142,6.258388],[2.781155,8.400839,7.423848,-5.684361,-8.239034],[-3.063555,6.998483,9.703859,0.448379,8.314506],[-4.071779,-5.651817,-1.845566,-5.887455,4.189099],[-5.003281,7.834016,-5.820969,1.068476,7.124083],[0.464306,-7.573315,-1.637914,-9.164058,6.930180],[4.372710,-4.123178,-1.502632,0.369699,6.064273],[8.836944,8.456099,3.148826,7.452105,-1.974060]],[[-1.434181,-8.869615,-3.249597,-4.878421,-3.738192],[-8.278683,8.193721,-4.636204,-3.436589,-4.331217],[-3.357964,0.302554,-0.293672,8.508818,2.994000],[-7.672825,-7.131235,-1.940256,1.959865,7.120837],[-2.308768,7.450720,-9.559491,1.530064,3.110102],[-7.654468,8.009398,1.855280,-0.218810,6.097326],[4.273164,4.746125,-4.176320,-3.884602,1.572596],[-3.781770,-5.345317,3.869268,9.647638,4.622871],[1.302456,-7.114955,0.059126,-6.945912,4.479776]]], dtype = "float32")#candidate|4150|(13, 9, 5)|const|float32
var_4151 = relay.var("var_4151", dtype = "float32", shape = (13, 9, 5))#candidate|4151|(13, 9, 5)|var|float32
bop_4152 = relay.floor_mod(const_4150.astype('float32'), relay.reshape(var_4151.astype('float32'), relay.shape_of(const_4150))) # shape=(13, 9, 5)
func_2988_call = mod.get_global_var('func_2988')
func_2990_call = mutated_mod.get_global_var('func_2990')
call_4168 = relay.TupleGetItem(func_2988_call(), 1)
call_4169 = relay.TupleGetItem(func_2990_call(), 1)
output = relay.Tuple([bop_4152,call_4168,])
output2 = relay.Tuple([bop_4152,call_4169,])
func_4173 = relay.Function([var_4151,], output)
mod['func_4173'] = func_4173
mod = relay.transform.InferType()(mod)
mutated_mod['func_4173'] = func_4173
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4174 = relay.var("var_4174", dtype = "float32", shape = (13, 9, 5))#candidate|4174|(13, 9, 5)|var|float32
func_4173_call = mutated_mod.get_global_var('func_4173')
call_4175 = func_4173_call(var_4174)
output = call_4175
func_4176 = relay.Function([var_4174], output)
mutated_mod['func_4176'] = func_4176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4220 = relay.var("var_4220", dtype = "int64", shape = (7, 5, 9))#candidate|4220|(7, 5, 9)|var|int64
const_4221 = relay.const([[[-3,-7,-7,1,-7,-4,-9,-2,2],[8,5,3,-8,-6,-1,2,-5,4],[8,-3,-10,-2,8,9,-3,8,-4],[4,7,10,-2,3,3,-1,-3,-4],[5,-3,1,5,-2,2,3,10,7]],[[-10,-2,8,2,-6,8,-7,7,6],[-5,-4,5,3,-1,9,-2,-6,-4],[2,6,1,8,-6,2,-3,-2,-2],[-2,-4,9,-10,4,9,-4,6,-7],[-5,8,9,3,7,-10,4,-5,6]],[[4,8,4,8,8,-10,-2,1,-4],[10,-6,-5,-5,2,-7,-7,-4,1],[-2,-8,2,9,-10,-5,-5,-4,-1],[9,5,-5,10,3,7,-4,2,3],[-9,-1,-5,5,-1,-2,5,-8,3]],[[-5,5,6,4,3,1,4,-10,-9],[1,-4,-3,5,-8,-2,-6,5,-7],[-5,3,8,6,4,-7,9,-8,-10],[-9,-9,-6,7,8,-3,-5,9,-8],[9,-1,10,-7,5,3,-6,-8,9]],[[-8,6,-10,-4,-7,2,9,9,-6],[7,-9,-1,-8,7,6,2,4,-3],[-8,1,7,3,5,-6,-3,6,-5],[-6,-6,1,-9,-7,2,1,-6,-7],[6,-10,4,-3,9,10,-6,9,9]],[[5,2,3,1,-3,-4,9,10,2],[5,10,-5,-10,-9,5,10,6,-4],[-5,10,-2,-10,-6,-10,4,-4,-9],[-7,1,1,-3,-6,2,-7,4,9],[-4,7,-7,10,2,8,-4,2,2]],[[-9,-2,-4,-6,-5,8,8,-1,2],[2,1,-6,5,5,-5,-1,-4,1],[9,-8,-2,8,-6,7,-1,2,4],[3,7,-7,9,-9,2,8,9,-8],[2,-3,7,8,8,9,9,-1,4]]], dtype = "int64")#candidate|4221|(7, 5, 9)|const|int64
bop_4222 = relay.greater_equal(var_4220.astype('bool'), relay.reshape(const_4221.astype('bool'), relay.shape_of(var_4220))) # shape=(7, 5, 9)
bop_4226 = relay.not_equal(bop_4222.astype('bool'), relay.reshape(const_4221.astype('bool'), relay.shape_of(bop_4222))) # shape=(7, 5, 9)
func_1131_call = mod.get_global_var('func_1131')
func_1133_call = mutated_mod.get_global_var('func_1133')
call_4234 = func_1131_call()
call_4235 = func_1131_call()
uop_4242 = relay.acos(const_4221.astype('float64')) # shape=(7, 5, 9)
output = relay.Tuple([bop_4226,call_4234,uop_4242,])
output2 = relay.Tuple([bop_4226,call_4235,uop_4242,])
func_4246 = relay.Function([var_4220,], output)
mod['func_4246'] = func_4246
mod = relay.transform.InferType()(mod)
var_4247 = relay.var("var_4247", dtype = "int64", shape = (7, 5, 9))#candidate|4247|(7, 5, 9)|var|int64
output = func_4246(var_4247)
func_4248 = relay.Function([var_4247], output)
mutated_mod['func_4248'] = func_4248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2988_call = mod.get_global_var('func_2988')
func_2990_call = mutated_mod.get_global_var('func_2990')
call_4250 = relay.TupleGetItem(func_2988_call(), 1)
call_4251 = relay.TupleGetItem(func_2990_call(), 1)
output = call_4250
output2 = call_4251
func_4253 = relay.Function([], output)
mod['func_4253'] = func_4253
mod = relay.transform.InferType()(mod)
mutated_mod['func_4253'] = func_4253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4253_call = mutated_mod.get_global_var('func_4253')
call_4254 = func_4253_call()
output = call_4254
func_4255 = relay.Function([], output)
mutated_mod['func_4255'] = func_4255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_4316 = relay.TupleGetItem(func_1075_call(), 0)
call_4317 = relay.TupleGetItem(func_1076_call(), 0)
func_3390_call = mod.get_global_var('func_3390')
func_3392_call = mutated_mod.get_global_var('func_3392')
call_4318 = func_3390_call()
call_4319 = func_3390_call()
output = relay.Tuple([call_4316,call_4318,])
output2 = relay.Tuple([call_4317,call_4319,])
func_4331 = relay.Function([], output)
mod['func_4331'] = func_4331
mod = relay.transform.InferType()(mod)
output = func_4331()
func_4332 = relay.Function([], output)
mutated_mod['func_4332'] = func_4332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3226_call = mod.get_global_var('func_3226')
func_3227_call = mutated_mod.get_global_var('func_3227')
call_4407 = func_3226_call()
call_4408 = func_3226_call()
func_2602_call = mod.get_global_var('func_2602')
func_2605_call = mutated_mod.get_global_var('func_2605')
const_4419 = relay.const([7.331655,8.841103,8.136185,2.419976,-3.306802,-6.096708,3.888029,8.101593,-2.713225,-3.478351,-8.528853,-5.971003,-5.342286,1.682010,2.000452,3.287451,-4.141529,1.934656,8.462216,-7.873761,7.321978,-9.972413,-8.685997,7.359180,0.057720,2.374338,0.024687,-6.962395,-8.043744,2.437739,9.352656,-9.787424,0.032980,-9.234689,7.705018,4.522353,5.280870,0.073558,9.336063,-6.104947,-0.564930,-2.385641,4.561431,-5.442995,-8.938124,1.275219,-2.595407,7.431502,4.833607,8.236505,7.182544,1.098055,-3.057401,-6.277636,-0.852248,1.591604,5.830848,-5.516932,-7.088237,-6.257526,2.148340,9.534424,1.243102,7.162749,-0.586887,0.228359,3.678579,-8.325167,-0.257649,8.768869,-9.486205,4.694939,-8.686306,-2.238514,-8.891454,9.490178,9.828764,-6.243603,-4.856398,6.111429,-5.218720,-0.599354,-0.967765,0.549329,8.314389,2.469726,2.686077,6.303487,-3.614496,1.626389,-3.205301,-4.770253,6.943551,2.415512,2.149161,-0.163903,2.171996,2.397382,4.155557,-5.837333,-4.367362,-3.334057,9.385090,2.330639,-2.065942,-0.852684,-3.991261,-3.273521,8.603994,8.953121,-3.494028,-1.266999,-9.236926,1.287396,7.798206,-8.437027,3.869487,2.475931,9.695797,7.422184,1.813305,-9.522487,-1.768683,4.684279,-3.289011,-2.951450,-6.915576,1.457532,7.625600,8.334474,-1.647066,-3.340764,-2.784774,-2.844682,-4.688054,6.612228,-7.172582,5.929890,-6.673415,-9.878108,1.005698,-3.078629,-7.356683,-8.821398,-1.594914,-9.934448,-1.143138,9.356972,-6.055113,-8.790042,3.475024,3.147659,2.323415,-9.958426,4.676708,8.515943,-0.145787,1.689847,1.705397,-8.662605,4.560351,-6.581886,6.939268,-4.085376,-2.163322,-0.912510,2.601783,2.200145,2.058466,-9.048662,-2.845061,3.855880,8.027889,4.079683,9.315212,8.151464,-8.471990,-8.734904,6.245895,-5.099401,6.595066,7.751252,-5.864008,1.513424,-8.791735,-8.276484,8.999993,0.819894,-7.820112,2.845237,-1.446643,-8.559999,5.346987,-0.943001,-0.694181,-1.371113,-3.463882,-2.207252,-0.653841,-1.326448,7.562619,0.454814,-3.983336,-1.785626,-4.447329,-4.141263,-5.799699,2.107628,6.271382,-6.562945,-8.287919,1.208662,-9.822647,0.617287,-7.884797,4.261657,7.270007,-7.566140,-3.499236,-7.431189,4.535725,6.217790,-6.018013,1.831420], dtype = "float32")#candidate|4419|(224,)|const|float32
call_4418 = relay.TupleGetItem(func_2602_call(relay.reshape(const_4419.astype('float32'), [1, 16, 14])), 0)
call_4420 = relay.TupleGetItem(func_2605_call(relay.reshape(const_4419.astype('float32'), [1, 16, 14])), 0)
output = relay.Tuple([call_4407,call_4418,const_4419,])
output2 = relay.Tuple([call_4408,call_4420,const_4419,])
func_4426 = relay.Function([], output)
mod['func_4426'] = func_4426
mod = relay.transform.InferType()(mod)
output = func_4426()
func_4427 = relay.Function([], output)
mutated_mod['func_4427'] = func_4427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3226_call = mod.get_global_var('func_3226')
func_3227_call = mutated_mod.get_global_var('func_3227')
call_4445 = func_3226_call()
call_4446 = func_3226_call()
output = relay.Tuple([call_4445,])
output2 = relay.Tuple([call_4446,])
func_4456 = relay.Function([], output)
mod['func_4456'] = func_4456
mod = relay.transform.InferType()(mod)
mutated_mod['func_4456'] = func_4456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4456_call = mutated_mod.get_global_var('func_4456')
call_4457 = func_4456_call()
output = call_4457
func_4458 = relay.Function([], output)
mutated_mod['func_4458'] = func_4458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2082_call = mod.get_global_var('func_2082')
func_2083_call = mutated_mod.get_global_var('func_2083')
call_4563 = relay.TupleGetItem(func_2082_call(), 0)
call_4564 = relay.TupleGetItem(func_2083_call(), 0)
func_4253_call = mod.get_global_var('func_4253')
func_4255_call = mutated_mod.get_global_var('func_4255')
call_4571 = func_4253_call()
call_4572 = func_4253_call()
output = relay.Tuple([call_4563,call_4571,])
output2 = relay.Tuple([call_4564,call_4572,])
func_4574 = relay.Function([], output)
mod['func_4574'] = func_4574
mod = relay.transform.InferType()(mod)
output = func_4574()
func_4575 = relay.Function([], output)
mutated_mod['func_4575'] = func_4575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4253_call = mod.get_global_var('func_4253')
func_4255_call = mutated_mod.get_global_var('func_4255')
call_4616 = func_4253_call()
call_4617 = func_4253_call()
output = call_4616
output2 = call_4617
func_4631 = relay.Function([], output)
mod['func_4631'] = func_4631
mod = relay.transform.InferType()(mod)
output = func_4631()
func_4632 = relay.Function([], output)
mutated_mod['func_4632'] = func_4632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_4683 = relay.TupleGetItem(func_348_call(), 1)
call_4684 = relay.TupleGetItem(func_349_call(), 1)
uop_4698 = relay.acos(call_4683.astype('float64')) # shape=(8, 10, 13)
uop_4700 = relay.acos(call_4684.astype('float64')) # shape=(8, 10, 13)
bop_4704 = relay.bitwise_or(uop_4698.astype('uint32'), relay.reshape(call_4683.astype('uint32'), relay.shape_of(uop_4698))) # shape=(8, 10, 13)
bop_4707 = relay.bitwise_or(uop_4700.astype('uint32'), relay.reshape(call_4684.astype('uint32'), relay.shape_of(uop_4700))) # shape=(8, 10, 13)
output = bop_4704
output2 = bop_4707
func_4717 = relay.Function([], output)
mod['func_4717'] = func_4717
mod = relay.transform.InferType()(mod)
output = func_4717()
func_4718 = relay.Function([], output)
mutated_mod['func_4718'] = func_4718
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4724 = relay.var("var_4724", dtype = "float64", shape = (13, 11, 5))#candidate|4724|(13, 11, 5)|var|float64
uop_4725 = relay.asinh(var_4724.astype('float64')) # shape=(13, 11, 5)
func_4631_call = mod.get_global_var('func_4631')
func_4632_call = mutated_mod.get_global_var('func_4632')
call_4750 = func_4631_call()
call_4751 = func_4631_call()
output = relay.Tuple([uop_4725,call_4750,])
output2 = relay.Tuple([uop_4725,call_4751,])
func_4772 = relay.Function([var_4724,], output)
mod['func_4772'] = func_4772
mod = relay.transform.InferType()(mod)
mutated_mod['func_4772'] = func_4772
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4773 = relay.var("var_4773", dtype = "float64", shape = (13, 11, 5))#candidate|4773|(13, 11, 5)|var|float64
func_4772_call = mutated_mod.get_global_var('func_4772')
call_4774 = func_4772_call(var_4773)
output = call_4774
func_4775 = relay.Function([var_4773], output)
mutated_mod['func_4775'] = func_4775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3515_call = mod.get_global_var('func_3515')
func_3516_call = mutated_mod.get_global_var('func_3516')
call_4813 = relay.TupleGetItem(func_3515_call(), 1)
call_4814 = relay.TupleGetItem(func_3516_call(), 1)
var_4823 = relay.var("var_4823", dtype = "float32", shape = (12, 2, 7))#candidate|4823|(12, 2, 7)|var|float32
bop_4824 = relay.equal(call_4813.astype('bool'), relay.reshape(var_4823.astype('bool'), relay.shape_of(call_4813))) # shape=(12, 2, 7)
bop_4827 = relay.equal(call_4814.astype('bool'), relay.reshape(var_4823.astype('bool'), relay.shape_of(call_4814))) # shape=(12, 2, 7)
func_3108_call = mod.get_global_var('func_3108')
func_3109_call = mutated_mod.get_global_var('func_3109')
call_4831 = func_3108_call()
call_4832 = func_3108_call()
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
const_4839 = relay.const([-10,6,4,9,-9,7,-10,4,-2,5,9,10,4,-9,4,1,-6,-2,-10,6,-7,3,-5,-7,-10,-9,-6,10,9,-3,3,7,-1,-4,9,10,-10,3,-10,4,-5,-10,-2,-10,-2,-1,9,8,8,-8,-9,1,1,-7,-6,-2,-4,1,5,-4,-6,-3,7,-2,-1,-10,-9,10,-6,-3,-7,-5,-9,8,8,2,1,9,-7,2,1,8,4,-2,-6,5,1,-6,-6,6,-6,-10,-6,-4,-9,-2,-8,-2,10,-3,10,2,9,4,2,-3,-8,7,1,-10,-8,1,-5,-8,-9,-3,-10,2,3,-9,6,5,-3,2,6,4,-2,-1,8,-4,-10,-9,2,-4,-7,-1,-4,-9,-1,-1,-10,-10,-10,3,-10,-6,-4,5,-8,2,-1,-10,-1,2,-9,8,7,-6,-1,-4,6,3,5,-7,-6,-8,-3,-4,9,-8,-8,-2,8,-2,6,10,-6,-1,1,-5,8,6,4,-8,5,-3,-4,-9,-2,-1,-7,-10,6,-7,9,5,-7,-9,-2,-6,-4,-1,-4,3,1,6,-7,-4,-10,-1,3,6,-9,-1,-3,8,-5,-6,-9,-7,-4,-10,-3,-5,3,2,4,-6,-5,3,-1,5,-2,-5,1,1,8,6,6,-4,7,-7,-6,-1,-9,2,7,-7,10,2,-5,9,-6,5,-6,3,7,-2,4,-5,-2,-4,-6,-10,5,10,-4,-5,3,2,-1,1,-6,10,-10,2,3,3,-7,6,4,3,-4,-10,-10,-4,-1,8,10,7,6,4,-5,9,-9,-5,-2,2,-9,-4,-7,10,5,-5,-8,7,-2,-3,5,1,8,6,6,-7,2,-4,10,-9,3,-2,-6,5,9,5,10,9,-1,10,-4,-2,10,5,3,-7,-8,7,5,2,-10,9,10,-1,-2,8,-10,2,10,2,-3,-8,-5,5,-9,-7,3,-2,-3,-3,4,10,-6,5,-2,-9,-5,6,-4,-3,9,5,-3,4,-7,-10,-10,4,3,-4,-6,9,-10,1,-7,8,-2,7,-9,1,10,7,-2,-8,2,-9,2,10,-5,7,-5,10,-9,5,10,6,-9,-1,-5,7,8,-6,6,-6,8,4,10,5,1,-9,-7,-2,-7,-9,-2,2,2,2,-5,-8,-2,8,-6,-3,-2,9,-5,-8,-4,5,-1,5,4,-1,8,1,2,3,-10,-5,7,2,7,-6,-6,8,-9,-3,2,3,-3,-1,-4,3,9,8,5,1,3,4,10,9,5,-4,5,-7,2,7,2,-3,9,-8,5,-6,-9,-6,-2,-8,-8,-4,-8,3,-8,-7,2,1,3,-6,1,5,-4,-8,-7,-1,-7,-7,-5,6,-3,-6,-4,6,8,-4,-6,8,-1,4,1,2,-10,6,1,3,-8,9,-5,9,-7,-2,-1,10,-5,1,-10,7,-2,-9,6,9,10,5,-10,-9,-7,-7,9,2,4,3,4,7,-4,1,8,-3,-7,-4,-5,4,-3,-10,-10,8,6,7,-3,10,-1,-7,-10,-7,-1,3,-5,-7,8,3,-2,10,-4,9,-1,5,9,-1,4,-7,-3,10,7,-8,-9,-3,-4,8,-9,-7,8,-2,-4,10,-5,3,-9,-5,2,-1,4,1,-4,6,-10,6,5,-6,3,4,-3,5,2,8,3,7,1,3,-1,-1,-4,-8,6,-7,-10,-8,-10,4,-5,7,2,-5,-4,-8,-9,-5,-7,1,8,4,-9,-2,-7,10,-1,-10,-3,-5,3,-1,4,5,-10,7,-4,-8,5,-1,-8,-4,8,-1,-7,9,10,2,7,-7,4,6,7,1,4,4,-3,-9,4,-3,6,3,-1,2,-4,4,3,8,-2,1,10,-7,6,1,8,3,5,10,2,-1,-10,-6,5,-4,2,-2,-3,-3,-5,-8,-10,6,8,-1,-9,7,-7,6,-7,-8,6,-1,-9,7,-9,-6,8,4,10,-8,-8,-10,-8,-9,-7,-5,-7,1,9,1,-4,8,-10,10,8,1,-3,-4,-7,7,10,-8,-8,-2,-6,-4,-9,-2,5,-9,2,-2,10,7,9,-3,5,5,-10,-10,-1,7,-7,8,-3,-8,8,-7,5,10,-7,2,-4,-7,3,1,2,-3,4,-2,10,-9,1,1,-1,2,3,2,-9,2,-4,6,-8,4,10,-1,7,3,8,-6,4,-7,-1,4,7,4,8,9,6,-8,-1,-1,8,6,7,-5,9,-7,2,-10,7,10,3,1,-3,8,-9,2,-4,-3,2,1,1,-4,1,-2,8,-6,-1,2,8,-10,10,6,2,-4,-9,-8,5,5,-5,-6,1,6,9,-10,8,5,1,2,3,10,1,4,9,9,10,-9,-7,5,-2,6,4,-10,5,10,9,9,7,5,-5,-10,-2,-6,-5,-7,-7,-9,-4,-7,2,-6,7,-1,7,10,2,6,10,-1,2,-2,-10,-1,-1,-5,6,-5,5,7,4,5,-9,8,-3,-4,8,6,-8,-6,5,-3,-1,4,-6,9,8,6,4,-7,-6,4,1,-5,6,10,-1,4,1,1,9,-1,-5,-6,-2,8,6,-3,-1,-5,-10,-10,-6,-4,-2,-8,4,-8,6,-7,-7,-8,6,-9,2,4,9,-2,6,-5,10,9,-3,-4,-3,9,8,4,-1,-9,-8,-4,4,-3,-1,-9,2,-8,5,5,-4,7,-4,-4,-5,-7,-7,-10,-6,-1,1,-9,-8,-7,-8,10,-7,-4,1,5,2,-10,2,9,-5,2,-2,9,9,-4,10,-8,4,-9,1,-10,-5,-1,-2,-4,3,-3,8,-5,-9,3,5,-8,3,-2,1,-7,-4,-5,1,5,5,8,-1,-10,2,-10,5,5,-5,-4,3,-5,2,-5,-7,-6,8,8,7,-10,9,7,9,-4,1,3,1,-2,7,-5,-6,9,-7,3,-2,4,-2,7,-4,-6,-1,10,-6,-5,8,9,3,7,-4,-3,-5,2,-7,-9,-2,-8,5,-2,-8,5,-9,9,-2,-3,9,5,-4,-1,7,-3,-8,-9,7,-5,-10,-1,5,-2,-8,-5,2,1,10,6,6,4,8,-9,9,-10,-6,-10,10,-10,-9,-5,9,-9,-10,4,-6,-1,4,-9,-4,1,-9,3,-5,8,-9,8,-9,-7,-2,6,-1,-2,7,-7,-2,2,-1,3,-5,-1,3,2,-6,10,10,-8,1,6,-3,10,3,-9,5,2,4,-6,-5,-7,-7,-1,-3,6,8,3,-6,7,2,-4,1,-9,-3,1,1,-1,7,5,-2,3,2,-1,8,8,7,7,1,-4,8,2,-5,10,-8,1,6,10,-1,-6,1,9,7,-8,1,-3,-7,-10,2,4,5,-8,3,-8,-10,-5,10,1,-9,8,-8,9,-9,-8,1,9,-1,-6,8,1,10,-9,10,-10,8,9,10,-1,-10,-10,-3,8,7,-8,-10,2,-5,-10,2,3,9,-6,-3,10,8,-4,-8,-6,-6,9,-5,6,4,6,8,-6,3,-10,2,8,9,-2,-4,-1,5,6,4,2,8,4,9,-6,3,-9,-5,7,-10,-8,-9,5,-2,-6,5,-4,7,-10,9,7,2,-9,4,9,-4,8,-10,9,-6,-10,-2,5,-6,4,-10,9,8,1,5,5,8,5,10,2,9,-6,-8,-8,5,2,-4,1,1,5,-1,7,6,9,-8,-2,5,-5,1,9,-7,5,-2,-5,-6,10,3,-9,1,-6,1,5,-8,-10,6,-6,2,6,6,6,-4,-1,6,-5,-8,-6,-9,-4,1,-5,-5,2,10,1,1,-10,-8,9,3,-8,5,9,-7,10,-8,9,-7,3,8,5,-5,-2,8,-4,-7,1], dtype = "uint64")#candidate|4839|(1440,)|const|uint64
call_4838 = relay.TupleGetItem(func_1989_call(relay.reshape(const_4839.astype('uint64'), [1440,])), 1)
call_4840 = relay.TupleGetItem(func_1991_call(relay.reshape(const_4839.astype('uint64'), [1440,])), 1)
func_2623_call = mod.get_global_var('func_2623')
func_2625_call = mutated_mod.get_global_var('func_2625')
call_4841 = func_2623_call()
call_4842 = func_2623_call()
output = relay.Tuple([bop_4824,call_4831,call_4838,const_4839,call_4841,])
output2 = relay.Tuple([bop_4827,call_4832,call_4840,const_4839,call_4842,])
func_4855 = relay.Function([var_4823,], output)
mod['func_4855'] = func_4855
mod = relay.transform.InferType()(mod)
var_4856 = relay.var("var_4856", dtype = "float32", shape = (12, 2, 7))#candidate|4856|(12, 2, 7)|var|float32
output = func_4855(var_4856)
func_4857 = relay.Function([var_4856], output)
mutated_mod['func_4857'] = func_4857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4631_call = mod.get_global_var('func_4631')
func_4632_call = mutated_mod.get_global_var('func_4632')
call_4909 = func_4631_call()
call_4910 = func_4631_call()
output = call_4909
output2 = call_4910
func_4917 = relay.Function([], output)
mod['func_4917'] = func_4917
mod = relay.transform.InferType()(mod)
output = func_4917()
func_4918 = relay.Function([], output)
mutated_mod['func_4918'] = func_4918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2988_call = mod.get_global_var('func_2988')
func_2990_call = mutated_mod.get_global_var('func_2990')
call_4960 = relay.TupleGetItem(func_2988_call(), 1)
call_4961 = relay.TupleGetItem(func_2990_call(), 1)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_4963 = relay.TupleGetItem(func_1426_call(), 2)
call_4964 = relay.TupleGetItem(func_1428_call(), 2)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_4966 = func_318_call()
call_4967 = func_318_call()
output = relay.Tuple([call_4960,call_4963,call_4966,])
output2 = relay.Tuple([call_4961,call_4964,call_4967,])
func_4994 = relay.Function([], output)
mod['func_4994'] = func_4994
mod = relay.transform.InferType()(mod)
output = func_4994()
func_4995 = relay.Function([], output)
mutated_mod['func_4995'] = func_4995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3984_call = mod.get_global_var('func_3984')
func_3985_call = mutated_mod.get_global_var('func_3985')
call_5037 = func_3984_call()
call_5038 = func_3984_call()
output = call_5037
output2 = call_5038
func_5040 = relay.Function([], output)
mod['func_5040'] = func_5040
mod = relay.transform.InferType()(mod)
mutated_mod['func_5040'] = func_5040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5040_call = mutated_mod.get_global_var('func_5040')
call_5041 = func_5040_call()
output = call_5041
func_5042 = relay.Function([], output)
mutated_mod['func_5042'] = func_5042
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5050 = relay.var("var_5050", dtype = "int32", shape = (3, 4, 7))#candidate|5050|(3, 4, 7)|var|int32
var_5051 = relay.var("var_5051", dtype = "int32", shape = (3, 4, 7))#candidate|5051|(3, 4, 7)|var|int32
bop_5052 = relay.multiply(var_5050.astype('int32'), relay.reshape(var_5051.astype('int32'), relay.shape_of(var_5050))) # shape=(3, 4, 7)
func_4253_call = mod.get_global_var('func_4253')
func_4255_call = mutated_mod.get_global_var('func_4255')
call_5058 = func_4253_call()
call_5059 = func_4253_call()
bop_5061 = relay.power(var_5050.astype('float32'), relay.reshape(var_5051.astype('float32'), relay.shape_of(var_5050))) # shape=(3, 4, 7)
output = relay.Tuple([bop_5052,call_5058,bop_5061,])
output2 = relay.Tuple([bop_5052,call_5059,bop_5061,])
func_5065 = relay.Function([var_5050,var_5051,], output)
mod['func_5065'] = func_5065
mod = relay.transform.InferType()(mod)
var_5066 = relay.var("var_5066", dtype = "int32", shape = (3, 4, 7))#candidate|5066|(3, 4, 7)|var|int32
var_5067 = relay.var("var_5067", dtype = "int32", shape = (3, 4, 7))#candidate|5067|(3, 4, 7)|var|int32
output = func_5065(var_5066,var_5067,)
func_5068 = relay.Function([var_5066,var_5067,], output)
mutated_mod['func_5068'] = func_5068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3108_call = mod.get_global_var('func_3108')
func_3109_call = mutated_mod.get_global_var('func_3109')
call_5132 = func_3108_call()
call_5133 = func_3108_call()
output = relay.Tuple([call_5132,])
output2 = relay.Tuple([call_5133,])
func_5135 = relay.Function([], output)
mod['func_5135'] = func_5135
mod = relay.transform.InferType()(mod)
mutated_mod['func_5135'] = func_5135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5135_call = mutated_mod.get_global_var('func_5135')
call_5136 = func_5135_call()
output = call_5136
func_5137 = relay.Function([], output)
mutated_mod['func_5137'] = func_5137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4134_call = mod.get_global_var('func_4134')
func_4136_call = mutated_mod.get_global_var('func_4136')
call_5198 = relay.TupleGetItem(func_4134_call(), 0)
call_5199 = relay.TupleGetItem(func_4136_call(), 0)
output = relay.Tuple([call_5198,])
output2 = relay.Tuple([call_5199,])
func_5204 = relay.Function([], output)
mod['func_5204'] = func_5204
mod = relay.transform.InferType()(mod)
output = func_5204()
func_5205 = relay.Function([], output)
mutated_mod['func_5205'] = func_5205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2623_call = mod.get_global_var('func_2623')
func_2625_call = mutated_mod.get_global_var('func_2625')
call_5245 = func_2623_call()
call_5246 = func_2623_call()
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_5253 = relay.TupleGetItem(func_2454_call(), 0)
call_5254 = relay.TupleGetItem(func_2456_call(), 0)
output = relay.Tuple([call_5245,call_5253,])
output2 = relay.Tuple([call_5246,call_5254,])
func_5270 = relay.Function([], output)
mod['func_5270'] = func_5270
mod = relay.transform.InferType()(mod)
mutated_mod['func_5270'] = func_5270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5270_call = mutated_mod.get_global_var('func_5270')
call_5271 = func_5270_call()
output = call_5271
func_5272 = relay.Function([], output)
mutated_mod['func_5272'] = func_5272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4134_call = mod.get_global_var('func_4134')
func_4136_call = mutated_mod.get_global_var('func_4136')
call_5379 = relay.TupleGetItem(func_4134_call(), 2)
call_5380 = relay.TupleGetItem(func_4136_call(), 2)
output = relay.Tuple([call_5379,])
output2 = relay.Tuple([call_5380,])
func_5391 = relay.Function([], output)
mod['func_5391'] = func_5391
mod = relay.transform.InferType()(mod)
output = func_5391()
func_5392 = relay.Function([], output)
mutated_mod['func_5392'] = func_5392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4917_call = mod.get_global_var('func_4917')
func_4918_call = mutated_mod.get_global_var('func_4918')
call_5428 = func_4917_call()
call_5429 = func_4917_call()
var_5436 = relay.var("var_5436", dtype = "float32", shape = (12, 2, 7))#candidate|5436|(12, 2, 7)|var|float32
bop_5437 = relay.less(call_5428.astype('bool'), relay.reshape(var_5436.astype('bool'), relay.shape_of(call_5428))) # shape=(12, 2, 7)
bop_5440 = relay.less(call_5429.astype('bool'), relay.reshape(var_5436.astype('bool'), relay.shape_of(call_5429))) # shape=(12, 2, 7)
func_3598_call = mod.get_global_var('func_3598')
func_3601_call = mutated_mod.get_global_var('func_3601')
var_5443 = relay.var("var_5443", dtype = "int16", shape = ())#candidate|5443|()|var|int16
var_5444 = relay.var("var_5444", dtype = "int16", shape = (1248,))#candidate|5444|(1248,)|var|int16
call_5442 = relay.TupleGetItem(func_3598_call(relay.reshape(var_5443.astype('int16'), []), relay.reshape(var_5444.astype('int16'), [16, 6, 13]), ), 0)
call_5445 = relay.TupleGetItem(func_3601_call(relay.reshape(var_5443.astype('int16'), []), relay.reshape(var_5444.astype('int16'), [16, 6, 13]), ), 0)
func_1001_call = mod.get_global_var('func_1001')
func_1004_call = mutated_mod.get_global_var('func_1004')
var_5448 = relay.var("var_5448", dtype = "float64", shape = (480,))#candidate|5448|(480,)|var|float64
const_5449 = relay.const([-5.192381,4.726241,8.520361,-5.368426,-9.192464,1.756605,6.626365,6.721751,0.235194,7.387331,-2.177123,0.478715,5.610907,-8.132571,7.535961,-2.067026,3.548555,-7.892511,-9.686470,1.230438,0.218604,-8.811020,-9.201219,-3.908691,-0.938856,-8.835685,-0.349128,5.123343,0.983985,-5.228360,8.307399,6.511392,1.403748,4.370110,-9.171387,-6.784125,-1.140652,6.497414,-0.069065,-8.217480,1.240201,7.086788,3.115885,7.967157,9.965220,2.483094,-0.844974,3.375316,-1.770475,5.549811,-4.955072,2.276520,-1.525664,6.576183,-2.783139,0.809686,-4.833968,6.662879,-1.367448,9.940125,-5.588169,-3.644612,1.471245,-0.148403,-5.150999,-6.830837,2.868988,5.234156,-4.348944,0.455721,6.609421,-2.451144,9.731129,1.053889,-3.590725,5.337219,3.733005,-4.689212,-6.527980,9.690869,-8.900751,5.804899,1.528928,-9.066080,5.979138,-7.095550,-9.314025,1.525052,-7.166223,7.685563,9.878131,8.757644,-9.293990,5.199190,9.080523,-3.616733,-7.498243,0.180400,-4.259743,-8.292517,9.814794,-9.066726,7.681841,-7.660268,-0.119778,7.040298,-0.697350,3.459390,-6.781855,0.825068,7.388031,2.051074,7.095991,3.319692,-9.757273,-0.280511,-0.498671,-6.128062,-4.297917,5.685829,-9.491481,-5.226535,4.865785,-2.351128,-0.782909,5.744558,7.898226,6.294079,-1.501450,-3.913899,-2.354419,-9.141164,-2.543388,1.336733,1.631175,4.083728,7.195020,0.243391,0.028955,-8.173725,1.655041,0.538384,-1.833622,-3.103669,6.702140,-7.931653,4.753001,-6.689255,8.828170,-2.971745,-8.421517,-9.721093,6.610879,9.639392,3.847130,-1.416273,4.176467,7.506048,-3.776563,-4.539706,9.742576,-3.629316,-0.408700,-8.297962,-4.916960,-4.677956,-3.332272,-5.556456,-4.749893,4.898319,0.672911,7.478245,4.610520,-1.043316,-3.017672,-8.267452,0.909613,-1.068587,2.365390,6.582152,4.288373,9.636314,0.330677,0.433651,9.342367,3.887228,-5.603878,3.682987,-6.500744,3.229189,4.437450,-5.804403,-1.061479,-3.079904,3.734848,3.970369,7.112016,-9.887314,-3.328035,7.494337,-8.911133,-3.254289,4.226354,5.413119,-9.054084,-8.349776,-3.196174,-9.527693,2.326312,-4.622742,2.884783,5.636874,-0.719669,2.323078,7.472230,-6.907821,5.677233,-8.102114,3.801383,-1.653237,-4.165140,1.645726,2.358941,-7.147354,-8.096826,1.354934,-6.150459,-4.741936,6.997161,-0.098752,-2.516062,-7.530369,1.508785,-8.830560,-5.590114,-5.339514,3.521585,8.442390,-7.780010,7.982295,9.771721,-0.748396,4.494060,-7.014191,-6.686960,7.587635,-5.267581,-8.331412,-5.447504,-1.396355,-9.853964,-0.348417,-9.650835,-8.033060,3.973721,1.142379,5.369973,-6.921295,-1.695063,5.228970,9.784905,-9.173355,-9.954187,-1.311205,4.478207,-6.876008,3.382024,-4.048735,-8.082390,-8.970448,-0.596466,-1.239256,7.502944,1.579430,-7.002446,-8.813290,4.335577,3.021002,-2.131525,7.814146,-0.303579,2.422062,-1.029593,7.224282,-1.025352,-6.733476,2.991729,-4.805589,4.853927,-2.104895,-1.730363,-1.511871,0.409287,-4.850207,1.411567,-3.580901,3.380860,9.575993,9.832988,-4.571990,8.448824,-1.855323,-2.250065,9.257463,-8.638408,0.766599,7.080443,0.032751,6.458436,-8.535227,6.969039,-1.001840,-3.157505,-5.510793,-4.418343,9.663881,2.715109,-8.732751,6.908437,9.909544,7.759617,-5.989238,-6.082818,-2.673625,0.900088,-8.241638,6.751665,3.125291,0.365879,6.421160,5.190095,5.236197,-2.182077,-1.463646,9.351979,-5.642941,-4.852030,9.162988,-1.018427,-6.295170,-7.336316,-2.186505,7.493098,9.441210,8.247077,-9.986360,-1.784622,4.018573,8.492809,-7.242507,6.415118,4.416529,3.778213,1.734294,-9.586728,-7.025976,-3.602275,-7.016304,-3.591371,-1.382980,-1.553280,-4.842119,-6.918093,-7.713211,1.592201,9.797875,6.589892,-6.434080,8.160147,-8.119265,5.384548,4.408011,7.582027,2.496341,1.012695,3.212505,-2.156890,-6.604640,8.075208,-5.310971,9.743498,8.090161,2.220831,-6.315785,7.416584,-7.207006,5.318106,5.577775,-2.077242,-5.374010,-5.031998,6.379794,-5.233777,-4.714392,-9.956435,-6.358540,-1.173847,-5.281007,-5.089892,-1.074542,7.328753,-2.738439,-8.562545,8.457589,0.842900,0.619007,8.266849,-7.313716,-5.847641,6.108715,-2.459498,5.747351,-5.961229,-6.637509,-3.088249,-4.446808], dtype = "float32")#candidate|5449|(416,)|const|float32
call_5447 = relay.TupleGetItem(func_1001_call(relay.reshape(var_5448.astype('float64'), [1, 480]), relay.reshape(const_5449.astype('float32'), [8, 13, 4]), ), 2)
call_5450 = relay.TupleGetItem(func_1004_call(relay.reshape(var_5448.astype('float64'), [1, 480]), relay.reshape(const_5449.astype('float32'), [8, 13, 4]), ), 2)
func_517_call = mod.get_global_var('func_517')
func_520_call = mutated_mod.get_global_var('func_520')
var_5458 = relay.var("var_5458", dtype = "float32", shape = (4, 64))#candidate|5458|(4, 64)|var|float32
call_5457 = func_517_call(relay.reshape(var_5458.astype('float32'), [16, 16, 1]))
call_5459 = func_517_call(relay.reshape(var_5458.astype('float32'), [16, 16, 1]))
output = relay.Tuple([bop_5437,call_5442,var_5443,var_5444,call_5447,var_5448,const_5449,call_5457,var_5458,])
output2 = relay.Tuple([bop_5440,call_5445,var_5443,var_5444,call_5450,var_5448,const_5449,call_5459,var_5458,])
func_5479 = relay.Function([var_5436,var_5443,var_5444,var_5448,var_5458,], output)
mod['func_5479'] = func_5479
mod = relay.transform.InferType()(mod)
mutated_mod['func_5479'] = func_5479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5479_call = mutated_mod.get_global_var('func_5479')
var_5481 = relay.var("var_5481", dtype = "float32", shape = (12, 2, 7))#candidate|5481|(12, 2, 7)|var|float32
var_5482 = relay.var("var_5482", dtype = "int16", shape = ())#candidate|5482|()|var|int16
var_5483 = relay.var("var_5483", dtype = "int16", shape = (1248,))#candidate|5483|(1248,)|var|int16
var_5484 = relay.var("var_5484", dtype = "float64", shape = (480,))#candidate|5484|(480,)|var|float64
var_5485 = relay.var("var_5485", dtype = "float32", shape = (4, 64))#candidate|5485|(4, 64)|var|float32
call_5480 = func_5479_call(var_5481,var_5482,var_5483,var_5484,var_5485,)
output = call_5480
func_5486 = relay.Function([var_5481,var_5482,var_5483,var_5484,var_5485,], output)
mutated_mod['func_5486'] = func_5486
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5494 = relay.var("var_5494", dtype = "uint8", shape = (3, 5, 5))#candidate|5494|(3, 5, 5)|var|uint8
var_5495 = relay.var("var_5495", dtype = "uint8", shape = (3, 5, 5))#candidate|5495|(3, 5, 5)|var|uint8
bop_5496 = relay.subtract(var_5494.astype('uint8'), relay.reshape(var_5495.astype('uint8'), relay.shape_of(var_5494))) # shape=(3, 5, 5)
output = bop_5496
output2 = bop_5496
func_5501 = relay.Function([var_5494,var_5495,], output)
mod['func_5501'] = func_5501
mod = relay.transform.InferType()(mod)
var_5502 = relay.var("var_5502", dtype = "uint8", shape = (3, 5, 5))#candidate|5502|(3, 5, 5)|var|uint8
var_5503 = relay.var("var_5503", dtype = "uint8", shape = (3, 5, 5))#candidate|5503|(3, 5, 5)|var|uint8
output = func_5501(var_5502,var_5503,)
func_5504 = relay.Function([var_5502,var_5503,], output)
mutated_mod['func_5504'] = func_5504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5204_call = mod.get_global_var('func_5204')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_5515 = relay.TupleGetItem(func_5204_call(), 0)
call_5516 = relay.TupleGetItem(func_5205_call(), 0)
var_5544 = relay.var("var_5544", dtype = "float32", shape = (12, 2, 7))#candidate|5544|(12, 2, 7)|var|float32
bop_5545 = relay.bitwise_and(call_5515.astype('int64'), relay.reshape(var_5544.astype('int64'), relay.shape_of(call_5515))) # shape=(12, 2, 7)
bop_5548 = relay.bitwise_and(call_5516.astype('int64'), relay.reshape(var_5544.astype('int64'), relay.shape_of(call_5516))) # shape=(12, 2, 7)
func_1837_call = mod.get_global_var('func_1837')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_5582 = relay.TupleGetItem(func_1837_call(), 0)
call_5583 = relay.TupleGetItem(func_1838_call(), 0)
func_1612_call = mod.get_global_var('func_1612')
func_1613_call = mutated_mod.get_global_var('func_1613')
call_5590 = relay.TupleGetItem(func_1612_call(), 0)
call_5591 = relay.TupleGetItem(func_1613_call(), 0)
func_4717_call = mod.get_global_var('func_4717')
func_4718_call = mutated_mod.get_global_var('func_4718')
call_5592 = func_4717_call()
call_5593 = func_4717_call()
var_5595 = relay.var("var_5595", dtype = "float32", shape = (12, 2, 7))#candidate|5595|(12, 2, 7)|var|float32
bop_5596 = relay.left_shift(call_5515.astype('int8'), relay.reshape(var_5595.astype('int8'), relay.shape_of(call_5515))) # shape=(12, 2, 7)
bop_5599 = relay.left_shift(call_5516.astype('int8'), relay.reshape(var_5595.astype('int8'), relay.shape_of(call_5516))) # shape=(12, 2, 7)
output = relay.Tuple([bop_5545,call_5582,call_5590,call_5592,bop_5596,])
output2 = relay.Tuple([bop_5548,call_5583,call_5591,call_5593,bop_5599,])
func_5616 = relay.Function([var_5544,var_5595,], output)
mod['func_5616'] = func_5616
mod = relay.transform.InferType()(mod)
mutated_mod['func_5616'] = func_5616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5616_call = mutated_mod.get_global_var('func_5616')
var_5618 = relay.var("var_5618", dtype = "float32", shape = (12, 2, 7))#candidate|5618|(12, 2, 7)|var|float32
var_5619 = relay.var("var_5619", dtype = "float32", shape = (12, 2, 7))#candidate|5619|(12, 2, 7)|var|float32
call_5617 = func_5616_call(var_5618,var_5619,)
output = call_5617
func_5620 = relay.Function([var_5618,var_5619,], output)
mutated_mod['func_5620'] = func_5620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4917_call = mod.get_global_var('func_4917')
func_4918_call = mutated_mod.get_global_var('func_4918')
call_5624 = func_4917_call()
call_5625 = func_4917_call()
output = call_5624
output2 = call_5625
func_5631 = relay.Function([], output)
mod['func_5631'] = func_5631
mod = relay.transform.InferType()(mod)
mutated_mod['func_5631'] = func_5631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5631_call = mutated_mod.get_global_var('func_5631')
call_5632 = func_5631_call()
output = call_5632
func_5633 = relay.Function([], output)
mutated_mod['func_5633'] = func_5633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5631_call = mod.get_global_var('func_5631')
func_5633_call = mutated_mod.get_global_var('func_5633')
call_5710 = func_5631_call()
call_5711 = func_5631_call()
const_5717 = relay.const([[[8.596552,6.125669,4.068997,-5.044815,3.561655,-2.695464,-6.797801],[4.350561,-2.447873,-4.817276,-2.113550,-7.579371,-0.319035,-9.703770]],[[4.898527,-2.177478,0.915471,-6.598746,-9.914578,8.097817,9.427232],[-4.756941,-7.503928,-5.094460,-3.406674,7.943258,-3.239144,-8.598014]],[[-4.607416,8.069914,-4.519309,-7.940953,0.784758,1.617505,8.798658],[8.016230,-5.987786,1.500987,6.128711,0.853797,-7.228112,9.141909]],[[-2.638062,1.180270,-5.930530,-0.175027,0.982954,-0.377404,5.842563],[-2.062070,-5.087004,1.672102,1.861398,8.586800,-6.105581,2.520656]],[[1.219082,-3.786542,-3.347554,-7.344668,-1.867853,1.325137,-4.358964],[-5.174083,7.631158,-7.469428,-6.443227,0.777812,-0.734729,5.343132]],[[5.878628,-2.125965,6.135971,5.244037,-9.692288,-8.972850,-6.203826],[-7.498499,8.006148,2.117126,5.010817,-3.022060,4.491128,-2.575492]],[[8.195710,4.660694,-9.570843,6.744545,-1.963706,0.490150,4.341403],[2.708094,0.263786,-2.442719,-0.418360,-3.967181,0.599407,1.041328]],[[-0.455761,3.666743,4.063153,-1.302033,-2.658204,6.463792,-2.612985],[6.159048,-8.114279,-2.994776,6.626419,-2.895460,-7.050367,0.325211]],[[-9.298958,-0.726636,-5.068937,-0.958711,-6.520745,2.285847,-1.046287],[0.562074,4.611359,-7.652138,0.731744,-4.097508,5.283324,-2.272286]],[[6.945343,-5.035586,0.967713,-9.166431,-2.567401,4.020828,3.541087],[6.801263,-3.652291,6.166162,7.125520,1.227805,-8.302429,8.773980]],[[1.447130,8.672308,-4.813695,-0.411940,-2.811417,5.582710,3.924305],[-3.921015,-3.543669,-0.193429,-7.201547,-6.372456,-3.484851,1.478142]],[[8.519874,-2.168364,-9.502168,7.049961,7.135063,-5.179008,-4.741799],[-8.290108,4.589122,7.996527,-8.745236,-8.372604,8.448317,8.716807]]], dtype = "float32")#candidate|5717|(12, 2, 7)|const|float32
bop_5718 = relay.logical_or(call_5710.astype('bool'), relay.reshape(const_5717.astype('bool'), relay.shape_of(call_5710))) # shape=(12, 2, 7)
bop_5721 = relay.logical_or(call_5711.astype('bool'), relay.reshape(const_5717.astype('bool'), relay.shape_of(call_5711))) # shape=(12, 2, 7)
output = bop_5718
output2 = bop_5721
func_5722 = relay.Function([], output)
mod['func_5722'] = func_5722
mod = relay.transform.InferType()(mod)
output = func_5722()
func_5723 = relay.Function([], output)
mutated_mod['func_5723'] = func_5723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2011_call = mod.get_global_var('func_2011')
func_2013_call = mutated_mod.get_global_var('func_2013')
call_5747 = relay.TupleGetItem(func_2011_call(), 1)
call_5748 = relay.TupleGetItem(func_2013_call(), 1)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_5751 = relay.TupleGetItem(func_782_call(), 2)
call_5752 = relay.TupleGetItem(func_783_call(), 2)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_5764 = relay.TupleGetItem(func_348_call(), 0)
call_5765 = relay.TupleGetItem(func_349_call(), 0)
output = relay.Tuple([call_5747,call_5751,call_5764,])
output2 = relay.Tuple([call_5748,call_5752,call_5765,])
func_5800 = relay.Function([], output)
mod['func_5800'] = func_5800
mod = relay.transform.InferType()(mod)
mutated_mod['func_5800'] = func_5800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5800_call = mutated_mod.get_global_var('func_5800')
call_5801 = func_5800_call()
output = call_5801
func_5802 = relay.Function([], output)
mutated_mod['func_5802'] = func_5802
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5814 = relay.var("var_5814", dtype = "float32", shape = (16, 5, 16))#candidate|5814|(16, 5, 16)|var|float32
uop_5815 = relay.atanh(var_5814.astype('float32')) # shape=(16, 5, 16)
output = relay.Tuple([uop_5815,])
output2 = relay.Tuple([uop_5815,])
func_5822 = relay.Function([var_5814,], output)
mod['func_5822'] = func_5822
mod = relay.transform.InferType()(mod)
mutated_mod['func_5822'] = func_5822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5823 = relay.var("var_5823", dtype = "float32", shape = (16, 5, 16))#candidate|5823|(16, 5, 16)|var|float32
func_5822_call = mutated_mod.get_global_var('func_5822')
call_5824 = func_5822_call(var_5823)
output = call_5824
func_5825 = relay.Function([var_5823], output)
mutated_mod['func_5825'] = func_5825
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5878 = relay.var("var_5878", dtype = "int32", shape = (1, 14, 2))#candidate|5878|(1, 14, 2)|var|int32
var_5879 = relay.var("var_5879", dtype = "int32", shape = (16, 14, 2))#candidate|5879|(16, 14, 2)|var|int32
bop_5880 = relay.bitwise_xor(var_5878.astype('int32'), var_5879.astype('int32')) # shape=(16, 14, 2)
uop_5887 = relay.cos(var_5878.astype('float32')) # shape=(1, 14, 2)
func_77_call = mod.get_global_var('func_77')
func_81_call = mutated_mod.get_global_var('func_81')
const_5893 = relay.const([[-8,-3,10,-2,9,-5,-9,8,7,-10,2,3,5,2,3,1,4,-6,5,3,1,8,-5,6,8,6,7,9,-7,10,-9,-1,-5,7,6,-6,8,-9,-2,4,10,7,9,3,-9,6,-4,-10,6,10,9,-1],[2,9,-4,2,-3,1,-9,8,7,-5,-2,1,6,2,-1,-2,2,5,-8,-9,-7,5,-7,3,8,7,5,-8,1,-6,-10,5,4,7,8,3,8,-3,-10,9,6,-7,-5,-4,4,1,10,7,6,6,-2,1],[-4,7,3,-1,1,4,5,-4,-9,5,1,-5,-10,2,7,-3,10,-6,-3,5,-7,2,6,2,-3,5,1,-2,9,2,-1,-9,-3,5,-2,-4,7,2,3,9,1,9,-3,10,7,10,-6,-9,1,-7,-6,3],[-6,-9,7,5,1,7,-7,8,2,3,4,-9,8,10,-8,9,6,-4,-3,10,-5,8,5,-7,1,-4,-2,3,-10,5,-6,1,10,4,4,-9,-10,-2,-2,-3,-9,-9,-10,2,-5,-8,-1,2,4,-7,7,-9],[1,-3,10,-8,-3,-9,-1,-4,10,-7,3,-2,-3,-5,-5,1,-6,10,10,-5,5,5,7,-2,3,5,7,3,6,-4,4,6,-8,4,-4,-9,2,-5,-5,-5,-4,-4,-8,3,-5,-5,-10,7,-9,6,-1,-2],[-2,4,-2,6,7,-9,5,1,8,-8,-8,6,7,1,-10,-3,-8,10,3,-7,5,7,7,1,5,4,4,1,4,1,2,4,8,1,-9,-4,-2,4,1,5,-5,-7,8,2,1,6,7,5,-4,-9,-5,-7],[5,8,-9,10,-1,4,-9,1,-10,-5,-7,-4,-9,5,-7,-2,-6,-8,5,-6,7,6,-6,5,-2,-5,-9,1,4,-1,-8,3,5,-6,9,5,-4,1,-7,-10,-5,9,5,-3,6,10,-8,8,4,4,-8,9],[-9,5,-5,5,9,-3,4,3,-9,-3,-6,10,7,-1,-4,-10,-1,9,10,-5,9,-5,-3,4,1,-10,-2,-7,6,-5,-10,-3,10,6,-9,-2,8,-3,8,-4,-9,-6,-5,-10,-10,-1,-10,1,6,1,-8,-4]], dtype = "uint8")#candidate|5893|(8, 52)|const|uint8
call_5892 = func_77_call(relay.reshape(const_5893.astype('uint8'), [8, 13, 4]), relay.reshape(const_5893.astype('uint8'), [8, 13, 4]), )
call_5894 = func_77_call(relay.reshape(const_5893.astype('uint8'), [8, 13, 4]), relay.reshape(const_5893.astype('uint8'), [8, 13, 4]), )
uop_5901 = relay.log10(var_5879.astype('float64')) # shape=(16, 14, 2)
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
const_5906 = relay.const([[-1,-8,-1,-6,2,-8,1,2,4,-4,5,10,-8,5,-2,-5,-7,-1,-5,-5,-1,9,-2,-2,10,-5,6,9,2,5,10,8,6,-6,-6,-10,-5,-1,-10,3,-8,5,6,7,1,-3,-3,-8,10,-2,6,-5,10,8,-10,-2,-3,-4,2,-6,-3,-3,10,7,-5,8,10,-2,9,10,3,8,10,5,-1,-6,2,5,3,1,3,-9,3,1,1,1,-5,2,-1,9,1,-8,-7,2,7,7,-3,2,8,-7,-7,5,-7,9,-5,10,8,-9,-5,6,-6,-1,-9,-6,6,-6,-2,-7,9,7,-8,1,6,-10,1,-2,-1,6,4,7,-5,-5,3,6,-7,7,7,-1,8,-6,9,5,-9,-10],[-3,4,-9,5,-10,3,1,5,9,-4,9,-5,-6,-10,1,1,-6,-2,-4,6,-7,5,10,7,-8,-6,9,-7,2,-1,9,7,-6,10,-5,8,-5,9,1,-7,-6,-7,-6,1,2,-1,5,6,-6,-3,-1,2,-4,-3,8,5,5,-9,4,9,6,-7,-7,-2,9,3,-8,6,-7,-6,-1,8,-3,-6,-1,-5,4,-5,6,3,5,-5,-2,-5,-2,-3,4,-6,10,-3,7,-5,-9,2,-10,-1,3,-7,9,-4,-5,-3,-8,-5,2,-9,-4,-10,7,-10,-8,-3,1,6,4,-10,-6,-9,3,-5,9,-4,10,-10,7,-5,5,10,10,3,-5,-6,-7,7,6,-4,6,2,3,5,3,7,-10,1],[4,-5,-8,-1,-5,-6,-2,7,-10,6,-10,5,2,1,-10,3,8,-2,8,-3,4,3,-2,4,9,5,-10,5,2,-6,-8,-4,-5,-3,10,6,-7,-7,-7,-1,2,8,-8,-6,8,-3,-8,-1,5,-8,1,-8,10,7,8,-8,6,4,8,6,-9,2,-8,-2,8,10,3,8,-5,3,-5,-6,6,6,-10,-1,3,-8,-8,-4,10,8,1,-7,2,-2,2,9,7,-1,10,-6,7,4,4,-6,1,10,-1,-10,10,2,-1,-7,8,7,-3,-3,-9,-10,4,-9,-1,8,-7,-4,4,8,-9,-6,-4,7,6,-10,6,7,-5,4,7,-5,-4,-1,7,4,4,-4,-4,8,10,4,7,5,-10,-5],[3,-3,-10,-5,-6,6,-10,-10,1,4,-5,9,-4,1,1,2,7,3,2,8,-9,-7,5,5,5,-9,-10,4,1,9,-3,-8,-8,8,10,-7,-10,-10,-4,-9,6,3,6,-1,3,1,-1,-4,1,-1,10,2,4,3,8,-1,1,10,9,4,-1,6,5,3,4,9,-3,3,2,7,7,-2,-10,-6,4,-3,-7,9,10,10,-7,7,-7,-9,-6,8,-4,2,5,-5,1,5,6,2,9,10,-10,-8,-7,5,-3,7,-5,3,10,-8,5,-1,-1,-7,-6,8,5,-2,-5,8,-1,-7,-5,-6,-10,9,2,-6,-4,3,1,-7,-9,9,-7,-4,-3,7,-1,4,-9,-7,-5,-6,-10,-9,10,7],[5,3,-4,-2,-8,-4,4,-2,-3,6,4,6,-10,-4,3,2,-7,1,4,8,-4,2,-4,-3,-3,-6,-2,2,-9,4,8,-1,-5,-8,-8,8,3,-2,-4,4,5,-6,-2,10,-7,-5,-2,-1,1,-5,-10,-2,5,-9,-10,-6,-3,-3,3,8,10,4,-10,-1,6,9,-9,8,5,-2,-10,-10,-5,10,6,7,-1,-8,-7,9,4,-1,9,8,-7,-8,1,2,1,-3,1,-5,-4,-3,-1,-6,10,-10,9,2,-8,-4,8,-4,-9,-10,-8,5,7,3,-10,-4,8,-1,2,2,-6,9,-4,7,-10,4,-9,10,-6,-5,-3,1,5,-8,-9,-4,-7,-1,6,4,4,-3,-8,-10,-7,-5,5,2],[9,-4,-10,-5,1,-10,3,-2,6,9,-10,10,-5,-6,2,8,-7,2,-1,8,3,3,-4,5,2,-3,5,8,10,-8,-3,4,9,1,4,-5,9,-5,3,-2,5,7,-1,-2,2,-3,-6,-9,4,-8,9,-7,3,3,3,-3,5,2,9,-8,4,8,-10,-7,-6,5,10,6,-6,-1,6,-1,6,-6,-5,-3,-6,9,7,2,-2,-9,-1,-8,-3,7,-3,-10,-2,-1,9,-6,-5,10,-2,5,9,8,8,8,5,1,-6,6,-7,6,2,-10,-10,1,5,8,10,6,4,-9,1,-6,3,6,-10,6,8,-1,10,-2,7,-1,-8,5,2,2,8,-2,-1,-10,5,-2,-4,3,4,9,5,-10],[-8,6,1,-3,5,1,-8,-6,-9,-5,-3,6,-4,-1,-4,4,6,-2,-10,-7,2,1,-8,-2,7,-9,6,10,-10,-10,1,-6,8,3,3,-2,-7,5,-2,-4,4,1,-1,-1,1,-7,9,-9,-1,4,-4,1,9,-9,-2,-4,-10,-8,8,-2,-3,3,-4,9,-5,-1,7,-2,-7,1,-8,8,2,7,-5,10,9,10,-6,-9,1,-1,2,-9,6,10,5,-2,-4,-4,9,7,-7,-3,7,5,-2,6,-2,4,-5,4,2,4,4,-5,3,-2,8,-5,-7,-2,-9,-2,-3,10,1,-5,-9,-9,8,5,5,-4,-5,9,-9,1,-9,-10,-1,10,4,5,6,-4,7,8,1,6,-10,7,3,-9],[3,7,-10,6,-2,-5,8,-5,-3,8,4,9,6,-5,-4,-5,4,10,7,-5,-10,9,2,-2,8,6,-1,-8,-2,10,-9,-4,-5,6,2,-2,6,10,-9,2,2,1,-4,4,4,-2,9,8,10,-7,-7,-9,-2,10,3,1,1,-1,-3,-1,-9,9,-8,-9,1,5,6,-5,-2,2,-7,1,4,-3,6,-5,-8,10,-1,8,-6,-4,-6,-1,-3,2,-5,-10,-4,8,-10,5,-7,-3,4,4,4,-2,-6,7,-7,1,-5,-3,-5,-8,-5,-2,8,5,-9,-3,7,-3,10,2,10,-1,6,3,6,8,-6,8,-8,-5,-9,9,-8,1,-2,-7,-8,-9,-2,-8,6,4,6,6,-2,-10,3,-1],[2,9,4,-6,4,-7,-8,5,-2,-7,-10,4,-6,-6,-6,10,-6,-9,4,-3,1,-5,6,4,-10,6,-4,3,-7,-10,6,8,-10,-4,-4,-5,8,7,-1,-4,2,2,-10,-7,-3,-9,-9,-5,-6,5,8,7,9,2,5,-2,5,2,-6,2,5,2,-8,3,6,4,-8,-9,-4,-7,-8,3,-1,-9,-5,-10,-2,-4,-9,-4,7,-8,10,-9,10,-3,-5,2,-3,-6,-1,9,-9,6,2,-3,-10,3,8,-2,10,-9,-4,-4,1,5,4,-7,-9,-1,3,-1,2,-2,-7,-3,10,5,-4,-2,7,-8,1,4,-8,-2,-8,5,8,4,-2,6,8,7,-8,-8,-6,8,2,9,8,3,6,-7],[7,-4,8,-2,-1,8,-10,6,3,-3,-7,-6,-6,4,9,8,3,-7,-4,-7,10,4,-4,-5,-6,3,-5,-2,-8,-2,-8,-2,-6,1,-8,3,-6,9,9,8,-4,-3,-7,-9,9,-1,6,7,-4,10,-7,-3,1,-4,6,8,-2,-1,5,-6,-3,-1,-2,-1,-9,2,5,8,5,-8,3,-3,6,3,-3,-6,-6,5,7,6,-6,-1,-2,-7,-2,-10,-1,-9,-6,-8,1,-7,-5,7,-10,-10,-1,-9,2,4,1,7,6,10,-10,2,4,-10,-6,3,-10,-4,3,-8,9,7,5,-3,1,4,4,3,-7,-9,8,1,-4,-2,8,10,-1,9,-2,-8,8,2,-8,-1,8,10,-1,-7,-5,10]], dtype = "uint64")#candidate|5906|(10, 144)|const|uint64
call_5905 = relay.TupleGetItem(func_3347_call(relay.reshape(const_5906.astype('uint64'), [15, 8, 12])), 0)
call_5907 = relay.TupleGetItem(func_3349_call(relay.reshape(const_5906.astype('uint64'), [15, 8, 12])), 0)
output = relay.Tuple([bop_5880,uop_5887,call_5892,const_5893,uop_5901,call_5905,const_5906,])
output2 = relay.Tuple([bop_5880,uop_5887,call_5894,const_5893,uop_5901,call_5907,const_5906,])
func_5908 = relay.Function([var_5878,var_5879,], output)
mod['func_5908'] = func_5908
mod = relay.transform.InferType()(mod)
mutated_mod['func_5908'] = func_5908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5908_call = mutated_mod.get_global_var('func_5908')
var_5910 = relay.var("var_5910", dtype = "int32", shape = (1, 14, 2))#candidate|5910|(1, 14, 2)|var|int32
var_5911 = relay.var("var_5911", dtype = "int32", shape = (16, 14, 2))#candidate|5911|(16, 14, 2)|var|int32
call_5909 = func_5908_call(var_5910,var_5911,)
output = call_5909
func_5912 = relay.Function([var_5910,var_5911,], output)
mutated_mod['func_5912'] = func_5912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3515_call = mod.get_global_var('func_3515')
func_3516_call = mutated_mod.get_global_var('func_3516')
call_5934 = relay.TupleGetItem(func_3515_call(), 1)
call_5935 = relay.TupleGetItem(func_3516_call(), 1)
output = relay.Tuple([call_5934,])
output2 = relay.Tuple([call_5935,])
func_5957 = relay.Function([], output)
mod['func_5957'] = func_5957
mod = relay.transform.InferType()(mod)
mutated_mod['func_5957'] = func_5957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5957_call = mutated_mod.get_global_var('func_5957')
call_5958 = func_5957_call()
output = call_5958
func_5959 = relay.Function([], output)
mutated_mod['func_5959'] = func_5959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5204_call = mod.get_global_var('func_5204')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_6016 = relay.TupleGetItem(func_5204_call(), 0)
call_6017 = relay.TupleGetItem(func_5205_call(), 0)
func_2797_call = mod.get_global_var('func_2797')
func_2798_call = mutated_mod.get_global_var('func_2798')
call_6022 = func_2797_call()
call_6023 = func_2797_call()
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_6031 = relay.TupleGetItem(func_1426_call(), 2)
call_6032 = relay.TupleGetItem(func_1428_call(), 2)
output = relay.Tuple([call_6016,call_6022,call_6031,])
output2 = relay.Tuple([call_6017,call_6023,call_6032,])
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
func_2011_call = mod.get_global_var('func_2011')
func_2013_call = mutated_mod.get_global_var('func_2013')
call_6062 = relay.TupleGetItem(func_2011_call(), 1)
call_6063 = relay.TupleGetItem(func_2013_call(), 1)
func_2696_call = mod.get_global_var('func_2696')
func_2698_call = mutated_mod.get_global_var('func_2698')
call_6074 = relay.TupleGetItem(func_2696_call(), 0)
call_6075 = relay.TupleGetItem(func_2698_call(), 0)
func_2163_call = mod.get_global_var('func_2163')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_6088 = relay.TupleGetItem(func_2163_call(), 1)
call_6089 = relay.TupleGetItem(func_2164_call(), 1)
var_6094 = relay.var("var_6094", dtype = "float32", shape = (12, 2, 7))#candidate|6094|(12, 2, 7)|var|float32
bop_6095 = relay.subtract(call_6062.astype('float32'), relay.reshape(var_6094.astype('float32'), relay.shape_of(call_6062))) # shape=(12, 2, 7)
bop_6098 = relay.subtract(call_6063.astype('float32'), relay.reshape(var_6094.astype('float32'), relay.shape_of(call_6063))) # shape=(12, 2, 7)
output = relay.Tuple([call_6074,call_6088,bop_6095,])
output2 = relay.Tuple([call_6075,call_6089,bop_6098,])
func_6126 = relay.Function([var_6094,], output)
mod['func_6126'] = func_6126
mod = relay.transform.InferType()(mod)
mutated_mod['func_6126'] = func_6126
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6127 = relay.var("var_6127", dtype = "float32", shape = (12, 2, 7))#candidate|6127|(12, 2, 7)|var|float32
func_6126_call = mutated_mod.get_global_var('func_6126')
call_6128 = func_6126_call(var_6127)
output = call_6128
func_6129 = relay.Function([var_6127], output)
mutated_mod['func_6129'] = func_6129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5270_call = mod.get_global_var('func_5270')
func_5272_call = mutated_mod.get_global_var('func_5272')
call_6264 = relay.TupleGetItem(func_5270_call(), 0)
call_6265 = relay.TupleGetItem(func_5272_call(), 0)
func_318_call = mod.get_global_var('func_318')
func_320_call = mutated_mod.get_global_var('func_320')
call_6279 = func_318_call()
call_6280 = func_318_call()
output = relay.Tuple([call_6264,call_6279,])
output2 = relay.Tuple([call_6265,call_6280,])
func_6299 = relay.Function([], output)
mod['func_6299'] = func_6299
mod = relay.transform.InferType()(mod)
output = func_6299()
func_6300 = relay.Function([], output)
mutated_mod['func_6300'] = func_6300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3984_call = mod.get_global_var('func_3984')
func_3985_call = mutated_mod.get_global_var('func_3985')
call_6327 = func_3984_call()
call_6328 = func_3984_call()
func_1325_call = mod.get_global_var('func_1325')
func_1329_call = mutated_mod.get_global_var('func_1329')
const_6330 = relay.const([[5,-1],[-2,-2],[8,5],[6,7],[6,2],[-6,4],[-8,10],[-4,1],[2,-4],[-5,-7],[6,-2],[10,2],[3,-3],[-2,6],[-5,2],[-5,-9],[-5,3],[1,4],[-10,10],[6,-7],[-5,-9],[-7,-6],[9,2],[-1,3],[5,-9],[-4,4],[9,-5],[5,5],[2,6],[9,2],[10,-4],[-8,-10],[-2,1],[-9,-3],[10,-7],[-10,4],[10,-1],[-2,7],[-10,4],[9,-1],[10,-9],[7,-1],[-10,2],[5,-1],[-4,2],[-9,9],[-3,5],[8,2],[-8,-10],[3,-1],[-2,-10],[-7,-1],[-5,-10],[-3,4],[-3,-7],[5,-2],[10,-7],[3,-3],[-1,3],[-8,-10],[7,-7],[-10,-8],[10,-5],[-7,-7],[6,10],[-1,6],[10,9],[-4,-8],[10,3],[8,2],[-9,2],[-3,2],[10,1],[-7,-3],[-8,2],[3,3],[7,1],[9,3],[10,1],[4,-3],[7,8],[-2,-8],[3,-2],[-10,-10],[-3,4],[4,-8],[-3,-8],[-4,3],[-6,3],[10,-8],[-3,-1],[-5,2],[2,8],[3,2],[6,-3],[10,2],[-7,-4],[10,1],[-2,6],[1,-7],[-4,-1],[-4,-3],[3,-1],[-3,1],[-1,6],[8,-5],[-10,-10],[-9,-8],[-6,7],[1,10],[-7,-1],[7,-8],[-8,2],[-4,6],[7,8],[7,-10],[4,2],[-9,-1],[3,-5],[-5,-9],[-1,-9],[-7,2],[-5,2],[6,-6],[1,-6],[-10,7],[1,4],[-6,1],[3,4],[-6,-5],[-7,-4],[1,3],[-6,2],[-8,-9],[-10,-6],[-7,8],[6,-3],[-10,-3],[7,10],[-7,-10],[2,1],[3,-10],[5,1],[-5,-4],[-3,-3],[-5,-10],[6,-10],[10,8],[-4,-3],[-8,-9],[-3,5],[-1,8],[7,-7],[-2,5],[-4,2],[7,-8],[-8,-7],[6,-9],[8,6],[6,5],[7,-6],[-10,8],[-7,10],[10,-6],[-10,7],[1,-4],[2,2],[4,-1],[-1,2],[9,-7],[-2,-4],[-6,-3],[5,2],[-5,-7],[-6,7],[6,3],[-9,1],[4,-6],[-7,-1],[1,1],[3,2],[-2,7],[7,8],[-3,3],[5,-10],[3,7],[8,-5],[1,5],[-1,-4],[-5,1],[-6,-5],[1,1],[-3,-6],[10,-6],[-1,-7],[9,10],[8,-3],[4,7],[4,-1],[2,-10],[4,9],[9,-2],[8,-7],[-9,5],[1,-2],[-3,-7],[1,-1],[-1,-7],[-6,10],[-4,8],[-10,-9],[1,10],[-1,7],[1,10],[-3,8],[1,-8],[4,2],[10,9],[4,3],[-1,7],[7,-7],[-9,4],[-9,5],[-8,7],[-3,-9],[1,-7],[6,-10],[2,1],[3,-10],[9,6],[4,10],[-6,-1],[7,4],[-8,3],[-10,2],[-2,3],[-3,2],[7,-9],[-1,3],[5,-8],[6,10],[-2,9],[-8,6],[-6,-7],[-4,-2],[-9,1],[10,-7],[8,9],[7,9],[6,3],[-10,6],[-10,8],[4,-4],[-3,-10],[9,-1],[-1,2],[-2,9],[-8,2],[3,-8],[10,8],[8,-6],[-7,5],[4,-2],[8,4],[4,8],[6,-1],[-9,-2],[7,-5],[-2,-5],[7,-4],[5,9],[1,-3],[-7,-6],[-2,-1],[-8,-2],[-5,-7],[7,-5],[-3,9],[-8,-1],[-10,-3],[-9,1],[7,-4],[7,7],[2,8],[-5,6],[-3,-6],[-1,-7],[5,-9],[8,-6],[4,-10],[-4,4],[1,5],[-4,-6],[6,-7],[10,8],[-5,-10],[9,-9],[-5,-7],[-4,-7],[2,2],[5,-2],[-9,7],[-4,-7],[-4,-1],[4,-7],[9,-2],[-4,9],[-2,-1],[-9,7],[-3,-9],[9,-5],[6,5],[9,1],[-7,-2],[-1,-8],[-4,-10],[-3,2],[9,-4],[-9,1],[-6,5],[2,3],[8,-2],[-8,2],[9,-4],[-8,10],[-8,-6],[-3,4],[5,7],[7,7],[-7,6],[7,-5],[1,9],[-6,5],[-3,-2],[-9,-8],[-8,-2],[-6,2],[-7,-9],[6,3],[7,-5],[10,6],[-4,-2],[7,-7],[-6,9],[7,-7],[8,1],[4,-3],[5,-4],[1,-10],[8,-8],[-1,-9],[-6,-1],[8,9],[6,3],[-3,10],[6,3],[-4,2],[5,9],[7,-5],[6,5],[-3,-1],[-4,8],[-1,-5],[2,2],[-3,10],[-4,-5],[6,-3],[-5,-6],[1,-5],[2,-2],[2,7],[5,2],[6,7],[-2,3],[2,2],[-2,-4],[-6,10],[2,8],[-9,-2],[6,4],[7,-2],[-2,8],[-8,-1],[-1,-7],[-4,6],[1,4],[10,-6],[-1,8],[10,8],[4,-7],[-8,-7],[3,-5],[-1,7],[-6,-3],[8,-3],[-8,6],[1,-1],[1,1],[6,8],[2,-10],[-6,-6],[-9,-7],[8,7],[-10,-5],[8,10],[-4,9],[-1,-3],[10,-7],[-2,9],[1,10],[7,-5],[-10,-2],[6,8],[-4,-4],[-1,9],[2,-10],[-8,8],[6,-1],[5,3],[-8,-6],[8,-6],[8,-7],[-9,-4],[2,-7],[-4,4],[-5,4],[2,-7],[-4,-5],[-6,3],[3,5],[-8,-6],[5,-3],[-10,-1],[-1,-5],[4,-3],[5,-1],[1,5],[5,7],[-10,-4],[-6,-4],[-1,9],[1,4],[8,-6],[-5,1],[10,-9],[5,8],[7,-10],[6,-9],[-10,10],[-4,9],[-10,-2],[1,-1],[9,-5],[4,-2],[5,5],[-8,10],[-3,-1],[3,-9],[-4,-9],[6,5],[-8,2],[4,-4],[-7,-2],[-1,3],[3,3],[4,10],[-2,-3],[9,-6],[8,10],[3,3],[-2,7],[7,9],[3,-5],[-1,7],[6,-6],[9,3],[-1,1],[6,5],[9,1],[-1,-4],[-10,5],[6,9],[-3,-8],[-6,-2],[-3,-10],[-9,8],[7,5],[-8,6],[10,3],[3,-9],[-4,1],[-7,6],[7,2],[1,5],[-7,-9],[1,-7],[7,8],[-10,10],[-3,6],[3,-3],[-8,-8],[5,6],[-6,-1],[10,-8],[5,-1],[-3,3],[-10,-10],[-10,3],[10,-6],[7,-8],[-9,-9],[-4,8],[-5,8],[-7,-5],[-9,2],[-10,9],[8,-4],[9,9],[-9,-7],[-7,6],[-3,1],[-5,-1],[-3,-6],[-9,10],[2,4],[6,-7],[4,-1],[8,-3],[10,-5],[10,1],[-8,-6],[-4,4],[-2,5],[-2,4],[8,-6],[-3,-1],[5,-9],[-9,-10],[-9,-4],[5,-9],[8,7],[-8,-7],[8,-5],[6,-5],[-2,-8],[5,10],[6,-7],[3,8],[-1,3],[-7,8],[-6,6],[10,5],[-4,-5],[-2,-4],[-8,-1],[-6,4],[5,-9],[-2,6],[1,-1],[3,-3],[8,-7],[2,3],[2,-4],[-5,8],[-8,10],[3,7],[2,-4],[-4,2],[-4,4],[-2,-7],[1,5],[-10,5],[7,9],[5,-3],[-3,-10],[4,9],[-4,-6],[-2,-1],[6,10],[-6,-7],[2,4],[-1,-4],[1,-1],[9,3],[-3,-10],[-5,7],[-8,9],[-1,8],[2,1],[-6,-8],[-1,2],[-9,1],[-7,8],[-3,-3],[-3,6],[1,-7],[5,-6],[5,8],[3,5],[-8,-3],[-9,-6],[5,5],[6,-1],[-5,-1],[10,-9],[-3,10],[10,5],[4,-2],[-10,-7],[-10,2],[4,-4],[-6,7],[-4,1],[-7,1],[-8,5],[6,-7],[6,1],[8,3],[-1,-3],[3,10],[-8,3],[4,3],[2,-6],[-5,-5],[6,-8],[-3,8],[-9,-8],[-1,-8],[-1,-6],[-4,-9],[-9,5],[7,-3],[-9,-9],[2,-4],[-10,-1],[-5,2],[9,1],[1,10],[-4,-1],[4,-3],[-5,-3],[10,7],[-4,-1],[-9,-4],[-4,-2],[4,2],[4,6],[9,2],[2,2],[5,-1],[2,-7],[-6,-9],[-6,5],[2,8],[3,5],[3,-8],[3,6],[3,-8],[-1,4],[-7,-10],[-4,5],[-4,-2],[-8,1],[-4,-8],[-10,6],[2,-6],[10,10],[3,-2],[-5,-2],[9,8],[-3,-1],[-7,-4],[3,-8],[-4,10],[6,-1],[2,-7],[8,7],[-5,9],[1,5],[-8,5],[-6,8],[9,4],[-8,6],[6,-8],[-7,6],[-8,-10],[-4,7],[3,-3],[4,1],[-9,-1],[-7,8],[2,-2],[9,-1],[-2,5],[7,7],[-1,10],[-4,-1],[5,-2],[6,-8],[8,-7],[9,-5],[8,-6],[-2,-4],[-5,-10],[-7,-2],[2,-5],[-7,-9],[4,-3],[2,1],[-8,5],[-1,-4],[-7,-3],[-7,7],[2,8],[-6,4],[10,10],[-5,-4],[-1,4],[-9,-6],[5,1]], dtype = "uint64")#candidate|6330|(720, 2)|const|uint64
call_6329 = relay.TupleGetItem(func_1325_call(relay.reshape(const_6330.astype('uint64'), [15, 8, 12]), relay.reshape(const_6330.astype('uint64'), [15, 8, 12]), ), 1)
call_6331 = relay.TupleGetItem(func_1329_call(relay.reshape(const_6330.astype('uint64'), [15, 8, 12]), relay.reshape(const_6330.astype('uint64'), [15, 8, 12]), ), 1)
func_1131_call = mod.get_global_var('func_1131')
func_1133_call = mutated_mod.get_global_var('func_1133')
call_6337 = func_1131_call()
call_6338 = func_1131_call()
func_4331_call = mod.get_global_var('func_4331')
func_4332_call = mutated_mod.get_global_var('func_4332')
call_6350 = relay.TupleGetItem(func_4331_call(), 1)
call_6351 = relay.TupleGetItem(func_4332_call(), 1)
uop_6352 = relay.sinh(call_6329.astype('float64')) # shape=(8, 13, 4)
uop_6354 = relay.sinh(call_6331.astype('float64')) # shape=(8, 13, 4)
func_5270_call = mod.get_global_var('func_5270')
func_5272_call = mutated_mod.get_global_var('func_5272')
call_6360 = relay.TupleGetItem(func_5270_call(), 0)
call_6361 = relay.TupleGetItem(func_5272_call(), 0)
func_2163_call = mod.get_global_var('func_2163')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_6377 = relay.TupleGetItem(func_2163_call(), 4)
call_6378 = relay.TupleGetItem(func_2164_call(), 4)
uop_6383 = relay.cos(uop_6352.astype('float64')) # shape=(8, 13, 4)
uop_6385 = relay.cos(uop_6354.astype('float64')) # shape=(8, 13, 4)
func_1989_call = mod.get_global_var('func_1989')
func_1991_call = mutated_mod.get_global_var('func_1991')
call_6393 = relay.TupleGetItem(func_1989_call(relay.reshape(const_6330.astype('uint64'), [1440,])), 3)
call_6394 = relay.TupleGetItem(func_1991_call(relay.reshape(const_6330.astype('uint64'), [1440,])), 3)
func_1114_call = mod.get_global_var('func_1114')
func_1117_call = mutated_mod.get_global_var('func_1117')
var_6403 = relay.var("var_6403", dtype = "float32", shape = (256,))#candidate|6403|(256,)|var|float32
call_6402 = relay.TupleGetItem(func_1114_call(relay.reshape(var_6403.astype('float32'), [4, 64])), 1)
call_6404 = relay.TupleGetItem(func_1117_call(relay.reshape(var_6403.astype('float32'), [4, 64])), 1)
func_2193_call = mod.get_global_var('func_2193')
func_2195_call = mutated_mod.get_global_var('func_2195')
var_6424 = relay.var("var_6424", dtype = "float64", shape = (1, 720))#candidate|6424|(1, 720)|var|float64
call_6423 = relay.TupleGetItem(func_2193_call(relay.reshape(var_6424.astype('float64'), [8, 6, 15])), 2)
call_6425 = relay.TupleGetItem(func_2195_call(relay.reshape(var_6424.astype('float64'), [8, 6, 15])), 2)
output = relay.Tuple([call_6327,const_6330,call_6337,call_6350,call_6360,call_6377,uop_6383,call_6393,call_6402,var_6403,call_6423,var_6424,])
output2 = relay.Tuple([call_6328,const_6330,call_6338,call_6351,call_6361,call_6378,uop_6385,call_6394,call_6404,var_6403,call_6425,var_6424,])
func_6426 = relay.Function([var_6403,var_6424,], output)
mod['func_6426'] = func_6426
mod = relay.transform.InferType()(mod)
var_6427 = relay.var("var_6427", dtype = "float32", shape = (256,))#candidate|6427|(256,)|var|float32
var_6428 = relay.var("var_6428", dtype = "float64", shape = (1, 720))#candidate|6428|(1, 720)|var|float64
output = func_6426(var_6427,var_6428,)
func_6429 = relay.Function([var_6427,var_6428,], output)
mutated_mod['func_6429'] = func_6429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1943_call = mod.get_global_var('func_1943')
func_1945_call = mutated_mod.get_global_var('func_1945')
call_6444 = func_1943_call()
call_6445 = func_1943_call()
output = relay.Tuple([call_6444,])
output2 = relay.Tuple([call_6445,])
func_6449 = relay.Function([], output)
mod['func_6449'] = func_6449
mod = relay.transform.InferType()(mod)
output = func_6449()
func_6450 = relay.Function([], output)
mutated_mod['func_6450'] = func_6450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2348_call = mod.get_global_var('func_2348')
func_2349_call = mutated_mod.get_global_var('func_2349')
call_6542 = relay.TupleGetItem(func_2348_call(), 0)
call_6543 = relay.TupleGetItem(func_2349_call(), 0)
var_6556 = relay.var("var_6556", dtype = "float32", shape = (12, 2, 7))#candidate|6556|(12, 2, 7)|var|float32
bop_6557 = relay.floor_divide(call_6542.astype('float64'), relay.reshape(var_6556.astype('float64'), relay.shape_of(call_6542))) # shape=(12, 2, 7)
bop_6560 = relay.floor_divide(call_6543.astype('float64'), relay.reshape(var_6556.astype('float64'), relay.shape_of(call_6543))) # shape=(12, 2, 7)
output = relay.Tuple([bop_6557,])
output2 = relay.Tuple([bop_6560,])
func_6565 = relay.Function([var_6556,], output)
mod['func_6565'] = func_6565
mod = relay.transform.InferType()(mod)
mutated_mod['func_6565'] = func_6565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6566 = relay.var("var_6566", dtype = "float32", shape = (12, 2, 7))#candidate|6566|(12, 2, 7)|var|float32
func_6565_call = mutated_mod.get_global_var('func_6565')
call_6567 = func_6565_call(var_6566)
output = call_6567
func_6568 = relay.Function([var_6566], output)
mutated_mod['func_6568'] = func_6568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2348_call = mod.get_global_var('func_2348')
func_2349_call = mutated_mod.get_global_var('func_2349')
call_6600 = relay.TupleGetItem(func_2348_call(), 1)
call_6601 = relay.TupleGetItem(func_2349_call(), 1)
uop_6604 = relay.sinh(call_6600.astype('float64')) # shape=(12, 5, 8)
uop_6606 = relay.sinh(call_6601.astype('float64')) # shape=(12, 5, 8)
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
var_6613 = relay.var("var_6613", dtype = "uint64", shape = (1440,))#candidate|6613|(1440,)|var|uint64
call_6612 = relay.TupleGetItem(func_3347_call(relay.reshape(var_6613.astype('uint64'), [15, 8, 12])), 0)
call_6614 = relay.TupleGetItem(func_3349_call(relay.reshape(var_6613.astype('uint64'), [15, 8, 12])), 0)
func_2988_call = mod.get_global_var('func_2988')
func_2990_call = mutated_mod.get_global_var('func_2990')
call_6621 = relay.TupleGetItem(func_2988_call(), 1)
call_6622 = relay.TupleGetItem(func_2990_call(), 1)
output = relay.Tuple([uop_6604,call_6612,var_6613,call_6621,])
output2 = relay.Tuple([uop_6606,call_6614,var_6613,call_6622,])
func_6624 = relay.Function([var_6613,], output)
mod['func_6624'] = func_6624
mod = relay.transform.InferType()(mod)
mutated_mod['func_6624'] = func_6624
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6625 = relay.var("var_6625", dtype = "uint64", shape = (1440,))#candidate|6625|(1440,)|var|uint64
func_6624_call = mutated_mod.get_global_var('func_6624')
call_6626 = func_6624_call(var_6625)
output = call_6626
func_6627 = relay.Function([var_6625], output)
mutated_mod['func_6627'] = func_6627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5391_call = mod.get_global_var('func_5391')
func_5392_call = mutated_mod.get_global_var('func_5392')
call_6727 = relay.TupleGetItem(func_5391_call(), 0)
call_6728 = relay.TupleGetItem(func_5392_call(), 0)
uop_6731 = relay.atanh(call_6727.astype('float64')) # shape=(8, 13, 4)
uop_6733 = relay.atanh(call_6728.astype('float64')) # shape=(8, 13, 4)
output = uop_6731
output2 = uop_6733
func_6736 = relay.Function([], output)
mod['func_6736'] = func_6736
mod = relay.transform.InferType()(mod)
output = func_6736()
func_6737 = relay.Function([], output)
mutated_mod['func_6737'] = func_6737
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6752 = relay.var("var_6752", dtype = "uint32", shape = (2, 4, 15))#candidate|6752|(2, 4, 15)|var|uint32
var_6753 = relay.var("var_6753", dtype = "uint32", shape = (2, 4, 15))#candidate|6753|(2, 4, 15)|var|uint32
bop_6754 = relay.equal(var_6752.astype('bool'), relay.reshape(var_6753.astype('bool'), relay.shape_of(var_6752))) # shape=(2, 4, 15)
output = bop_6754
output2 = bop_6754
func_6765 = relay.Function([var_6752,var_6753,], output)
mod['func_6765'] = func_6765
mod = relay.transform.InferType()(mod)
var_6766 = relay.var("var_6766", dtype = "uint32", shape = (2, 4, 15))#candidate|6766|(2, 4, 15)|var|uint32
var_6767 = relay.var("var_6767", dtype = "uint32", shape = (2, 4, 15))#candidate|6767|(2, 4, 15)|var|uint32
output = func_6765(var_6766,var_6767,)
func_6768 = relay.Function([var_6766,var_6767,], output)
mutated_mod['func_6768'] = func_6768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_6800 = relay.TupleGetItem(func_348_call(), 1)
call_6801 = relay.TupleGetItem(func_349_call(), 1)
const_6807 = relay.const([[[2.055011,0.027113,-8.430945,0.465257,-8.490402,1.923988,-6.597539,-8.348741,-0.017058,1.963142,6.196225,0.017349,-3.667974],[7.454377,1.068928,3.615517,4.276171,-6.113734,0.770381,-5.518321,4.418858,-1.895042,2.434480,-2.636512,-0.022323,4.335875],[-2.143585,-6.440759,3.432357,-5.696894,-7.400741,7.940886,3.483607,9.140577,5.007029,-7.592274,-7.951595,-2.842382,4.817973],[7.830397,-7.973873,7.444849,-2.300132,-1.356305,8.724951,-8.955837,-7.190811,4.927752,0.980019,7.578097,2.224123,2.868871],[-7.552973,4.892988,4.973326,-0.497073,-2.416447,-1.408630,7.357213,-9.113010,9.737220,-0.288357,-3.571161,3.507389,-0.733447],[6.749302,6.363008,4.146239,-8.200132,1.787803,-5.188438,-2.140185,-9.891979,4.395606,4.651132,-4.125959,-5.487654,-7.569152],[7.378105,-9.132079,-8.929385,6.205866,7.731118,-7.202836,2.401469,2.641222,1.834226,-3.404538,-5.422913,8.375035,1.520422],[-5.895372,-4.527675,8.865282,8.570977,9.300838,5.032204,4.947219,-1.585860,-1.628040,1.724884,8.406225,0.592675,-0.973655],[0.662072,9.800232,-0.886817,-4.740199,9.002460,-5.512370,9.725246,-8.799290,-5.848587,9.465115,1.417826,-3.368465,3.108118],[7.263873,-0.126250,-2.508950,0.757233,-7.913779,-5.927811,-8.277240,-8.761438,-7.967342,0.904583,-3.680739,-9.589096,-0.599650]],[[-9.441287,-2.360613,-3.562709,-7.226080,-6.142994,-6.261871,3.034789,9.430117,7.726812,3.009632,-9.300208,4.836681,-9.258076],[0.586478,-0.159618,4.293926,-2.716179,-1.363095,2.977012,3.349644,-6.491819,-1.921117,6.791236,7.926460,1.414571,-3.199623],[-1.176083,2.845075,-1.357572,1.989191,-9.418673,1.823633,-5.854661,5.411782,-2.601835,0.846382,-6.323294,-9.170214,5.884132],[-0.220793,-7.349245,-7.022692,8.278978,-0.091287,-1.321626,-3.779130,-3.656381,-2.646395,0.708051,-1.933837,-9.534637,-5.641161],[7.049345,-2.501099,-4.049137,-9.798117,-7.412721,1.593500,-7.153918,6.138226,1.696571,-2.671680,1.064685,9.824380,-5.302206],[-3.179275,4.454892,-3.615920,-9.937576,-2.118055,4.667952,9.346282,5.546284,0.784387,-7.152089,9.020152,-4.683945,0.467731],[-2.624865,3.362837,6.358211,5.339629,-8.193223,9.748773,2.049340,-5.597802,-9.022055,-4.556180,-0.235356,-2.957760,-6.969973],[5.810727,9.225749,-2.671183,4.400586,-3.869788,8.129431,1.267246,3.445340,-5.883349,-7.200569,-4.649681,2.718136,5.208658],[-5.458398,-2.930119,9.238154,-2.778544,3.265279,-1.949859,-7.810148,3.122879,-7.141156,7.866720,9.086186,-7.625420,-1.816966],[2.244627,9.044790,-0.560665,-2.467411,-6.226528,-1.016329,-0.306688,2.173591,-4.705147,0.599211,-0.492823,-3.531802,-3.709867]],[[9.841266,-8.888281,8.701690,4.256520,-5.630556,-8.640229,6.360239,-8.936323,7.659610,9.070942,4.658585,-0.013850,2.267951],[-3.671150,2.917158,9.070453,-3.628215,-2.591220,9.513427,-2.810239,5.673336,-8.663795,-7.829077,-6.117144,0.403283,-7.486778],[0.884503,-4.819739,7.068575,8.031122,2.941042,-7.256434,-3.609020,1.223522,-6.575843,8.404950,-1.257189,-9.744445,-2.833964],[8.423746,-5.102843,-7.208183,-1.546660,-2.796295,1.504883,-2.010082,3.362338,-3.240066,-0.301563,5.721238,-1.938063,-3.432594],[1.018347,8.192000,-1.747507,8.740273,-2.559044,-2.835404,-8.563719,8.493867,-3.636143,-2.986425,-0.210566,6.261056,-4.115144],[6.864528,5.691374,-1.281590,5.462178,-5.136264,-5.593775,-5.470970,6.116746,9.701275,-7.265097,-7.561007,1.933632,-8.416385],[1.706979,-7.647209,-4.133867,-2.679226,3.842614,-7.200192,-1.561876,-1.437556,1.947710,-3.043570,-9.247926,-2.765904,-0.716450],[9.755859,-7.820744,3.840168,-7.565848,1.502618,5.333854,-9.754244,-1.856815,2.387220,-1.664942,9.736215,0.534379,-8.915933],[-6.226795,-8.397374,8.141642,-7.014600,3.862007,-9.926125,6.204492,-7.418519,8.814557,8.414389,-3.507569,4.172198,9.625435],[-3.914621,-2.589307,-6.495854,1.672247,8.827665,-9.130055,-0.985926,0.318161,6.879138,7.073600,1.390436,4.242774,-2.416915]],[[-7.843253,-4.119521,8.785142,-9.547456,3.343636,-2.070347,2.795280,-1.051719,2.534118,6.513799,2.858248,8.980898,-1.915336],[2.445632,0.522562,0.051231,7.415804,5.820297,-2.044337,-1.778757,-0.703263,2.992744,-4.120192,-6.025090,-1.940266,-0.544935],[-2.907559,-8.684935,7.408192,-8.539652,-0.592683,-6.904991,3.683752,-8.508734,8.067497,-3.349395,6.514175,1.562957,2.212274],[5.440397,2.188709,2.706121,0.844989,-5.756908,7.467355,2.998092,4.002637,-7.204575,-6.095106,-0.685555,7.354369,4.686053],[-0.866290,3.458146,-1.180975,-2.549338,-9.165002,-1.871185,0.148813,-1.232409,8.907945,-4.821051,2.380427,-5.764257,2.357332],[1.376367,7.873235,0.541956,0.521345,0.313971,3.166989,2.657599,4.284926,7.857528,9.162324,7.742573,-3.981867,0.770757],[-0.840904,4.599584,-8.444214,8.417707,8.798825,-8.302583,4.458151,9.607684,6.804600,-6.301751,-0.248802,0.315013,-3.384889],[-2.514484,3.029878,-9.079301,5.553533,6.466803,1.059653,5.979720,-2.264599,9.340781,0.362628,-1.932477,-2.067463,4.536577],[2.856215,-6.961441,-2.479892,-1.825728,-0.006956,2.446136,-8.526076,9.870128,4.752553,-2.260328,-4.874870,8.619826,-1.363006],[-4.435672,0.395299,3.416972,3.033451,-2.787674,2.701665,2.307131,5.553787,1.407790,9.133209,5.147094,-1.218978,-7.193352]],[[-3.931000,-2.783387,-6.569936,7.599087,5.907549,-8.563421,-1.282690,-4.450417,3.371728,3.674476,-0.228957,-3.315522,5.463486],[0.185465,9.204876,6.342613,1.305550,5.889191,-4.042302,7.588553,9.932693,-3.697708,-1.869130,1.824805,-7.383601,5.518361],[-1.764510,5.923964,5.900933,5.273167,-9.291544,-9.423556,-7.579440,9.408672,-3.900497,-6.220478,-6.286161,3.993524,1.202139],[-6.912414,0.276564,2.069761,4.253960,-6.885948,1.490435,-7.263129,-1.650385,3.402060,-2.772912,7.467868,-0.648092,-3.303649],[7.484088,2.919198,6.477956,-5.726216,4.336068,-6.388648,-4.567099,-1.338473,-2.595671,-2.283479,5.089736,4.791555,-2.889673],[0.247993,1.909000,-1.414852,8.730026,0.210312,4.035210,-1.682690,9.914887,-6.929174,8.537426,0.699633,5.705378,-2.140534],[-2.238105,-9.429283,-3.439512,0.371968,7.252509,-8.406797,1.919238,7.150928,-0.039074,-7.212992,-3.227401,3.614623,1.843476],[8.997319,-6.919339,0.008418,-9.856318,-0.270433,1.533136,-0.912872,1.592934,-8.898902,-1.733563,9.798871,3.844741,2.595158],[-4.577080,5.858961,2.982254,-7.963753,-2.250975,-3.768650,5.165389,6.058934,-7.420800,-8.789575,8.504129,2.168296,-4.301643],[-6.908152,-3.666203,-8.125256,-9.681524,-2.227851,-2.119511,-6.450347,-7.351750,6.605997,6.795054,7.824856,-7.991489,9.026820]],[[-8.982386,-9.957149,4.085099,-5.806116,-1.770883,1.216332,-5.656688,-1.202094,-6.586653,4.197383,-2.348721,2.451757,9.515628],[9.194141,-7.917733,4.176433,5.530956,0.003262,-3.788672,-6.456711,-2.079484,-0.491946,0.792566,-7.016027,7.908647,8.993759],[-3.597419,9.737395,1.488662,-5.654391,4.688669,-7.734408,7.525918,0.749773,0.641328,-3.554211,3.610447,-7.251260,1.663866],[7.932671,-4.308657,-2.875911,2.101952,-8.757793,1.191023,-4.729564,0.713087,8.482848,-3.373724,-0.239142,3.902500,-6.506458],[3.074816,6.439673,5.847394,6.603321,2.451573,-6.215439,4.472419,6.961391,4.082569,1.201968,-6.895082,7.463033,-7.555178],[-8.681435,-4.137913,-8.003522,6.864745,2.899497,-1.963004,-9.661635,-6.523214,-0.659201,-2.774396,-0.292778,9.517112,-1.174669],[5.740398,9.268355,9.579017,1.329335,-5.056037,-6.510637,2.585381,-3.252180,-0.764812,-6.068789,1.258624,3.531629,-8.234479],[-8.872071,6.505817,-3.633636,-0.526326,-3.635902,0.969709,-7.434987,-1.072675,-1.501658,-3.525129,3.481858,9.684451,3.163877],[8.853052,-0.021864,1.276636,8.678031,4.573962,1.020810,6.285649,-5.474953,0.327266,-5.940241,7.896560,7.408385,4.840784],[-9.467462,-3.572514,-1.209015,-2.101604,-1.588498,3.661736,8.804841,3.476044,-3.380000,-5.558372,6.754574,3.760295,9.065554]],[[-6.772400,-4.461872,-1.337441,1.196409,6.647011,-6.119651,-3.726588,5.624448,-6.559581,6.395186,9.214918,4.283372,-9.880499],[8.935484,-4.098902,-2.176116,1.977751,5.279424,0.803884,7.508294,-9.722666,6.768852,-7.142286,-4.583977,6.026941,-7.704379],[4.235131,-0.443539,-4.956533,-1.919805,2.542414,-4.186431,9.218161,-2.351332,-0.423991,9.283752,7.210877,7.489454,9.771672],[-4.394502,1.034016,2.231559,-5.195534,-0.440990,3.448506,-3.205696,5.493346,-7.725043,-4.622735,-2.887475,-4.187973,6.103504],[-3.573509,8.143231,-3.500379,-4.945759,-3.842897,-4.629327,4.709570,2.736743,4.963743,3.889638,-1.718462,-7.272315,-3.629592],[8.380000,-4.833756,-7.330511,-9.319650,2.582516,-3.940475,-4.116496,1.727168,6.773729,-4.401880,-6.963621,-3.477640,-6.108969],[2.281020,3.435387,0.339871,-5.045986,2.842179,-3.720149,-4.587364,-7.715271,2.886544,3.775554,-3.617838,-5.332096,8.792385],[-4.911257,-6.059114,2.374241,1.100156,-2.109549,5.031404,8.757779,7.947783,-6.266107,9.627887,-1.743152,-6.608076,2.433996],[2.481655,9.551485,-7.400555,-2.249900,-7.809989,-4.537576,5.290093,5.330724,9.601706,4.907482,-7.644038,-0.762909,0.582145],[6.071771,-8.256151,-3.802373,-7.660654,6.216017,5.245458,6.329344,8.074503,-0.167868,-1.684444,7.429306,-9.588260,7.011842]],[[4.588610,-4.139144,-4.397399,-9.766248,-7.612972,-3.046678,-1.565521,-5.001141,-6.406066,8.737872,7.242089,-3.219813,1.561292],[-2.856535,-0.249606,2.210044,9.590241,-2.695782,7.610785,4.933792,2.134555,-3.825881,8.144198,-3.293794,-2.517332,1.473809],[1.762869,-9.538866,1.477527,-3.410257,-2.982116,5.389042,1.615675,8.280950,-1.491571,-3.034430,3.629759,1.733455,0.497699],[-9.690580,-5.151233,-2.795941,9.993807,-3.517179,0.571013,-8.461628,-4.856737,9.333633,-1.357757,-2.072883,9.237693,-7.289621],[5.670594,8.265311,3.714119,2.492457,6.153478,1.993142,-4.609144,-6.860476,-2.720096,6.991678,-7.987714,-4.915577,0.590035],[-5.537196,-0.581254,3.605576,-6.060473,-2.820002,-7.430130,4.236881,0.658539,-0.117731,0.934862,9.600900,-5.805309,-0.109119],[-2.753848,4.108703,-6.601465,-2.051732,-9.369090,-9.959651,4.663005,9.949050,-5.434322,6.741250,8.767706,2.322924,-3.404069],[2.198885,1.071953,-2.653804,-4.330728,-1.188301,2.085264,0.271599,-4.663960,-0.583386,3.150921,-6.630778,6.022045,5.691021],[3.286718,4.036711,-7.754031,-3.498698,-0.387068,1.143942,-0.888155,4.659205,-2.583234,-9.224823,5.782980,-5.923318,-4.291415],[-9.645628,4.878225,-3.138604,9.372411,-6.464266,-3.938870,0.297706,6.278707,-5.152556,-0.784843,5.454873,-4.690683,-3.652196]]], dtype = "float64")#candidate|6807|(8, 10, 13)|const|float64
bop_6808 = relay.not_equal(call_6800.astype('bool'), relay.reshape(const_6807.astype('bool'), relay.shape_of(call_6800))) # shape=(8, 10, 13)
bop_6811 = relay.not_equal(call_6801.astype('bool'), relay.reshape(const_6807.astype('bool'), relay.shape_of(call_6801))) # shape=(8, 10, 13)
uop_6813 = relay.sqrt(const_6807.astype('float32')) # shape=(8, 10, 13)
func_4855_call = mod.get_global_var('func_4855')
func_4857_call = mutated_mod.get_global_var('func_4857')
var_6828 = relay.var("var_6828", dtype = "float32", shape = (168,))#candidate|6828|(168,)|var|float32
call_6827 = relay.TupleGetItem(func_4855_call(relay.reshape(var_6828.astype('float32'), [12, 2, 7])), 0)
call_6829 = relay.TupleGetItem(func_4857_call(relay.reshape(var_6828.astype('float32'), [12, 2, 7])), 0)
func_5631_call = mod.get_global_var('func_5631')
func_5633_call = mutated_mod.get_global_var('func_5633')
call_6831 = func_5631_call()
call_6832 = func_5631_call()
func_4253_call = mod.get_global_var('func_4253')
func_4255_call = mutated_mod.get_global_var('func_4255')
call_6840 = func_4253_call()
call_6841 = func_4253_call()
output = relay.Tuple([bop_6808,uop_6813,call_6827,var_6828,call_6831,call_6840,])
output2 = relay.Tuple([bop_6811,uop_6813,call_6829,var_6828,call_6832,call_6841,])
func_6847 = relay.Function([var_6828,], output)
mod['func_6847'] = func_6847
mod = relay.transform.InferType()(mod)
mutated_mod['func_6847'] = func_6847
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6848 = relay.var("var_6848", dtype = "float32", shape = (168,))#candidate|6848|(168,)|var|float32
func_6847_call = mutated_mod.get_global_var('func_6847')
call_6849 = func_6847_call(var_6848)
output = call_6849
func_6850 = relay.Function([var_6848], output)
mutated_mod['func_6850'] = func_6850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2696_call = mod.get_global_var('func_2696')
func_2698_call = mutated_mod.get_global_var('func_2698')
call_6862 = relay.TupleGetItem(func_2696_call(), 2)
call_6863 = relay.TupleGetItem(func_2698_call(), 2)
func_3390_call = mod.get_global_var('func_3390')
func_3392_call = mutated_mod.get_global_var('func_3392')
call_6866 = func_3390_call()
call_6867 = func_3390_call()
func_2348_call = mod.get_global_var('func_2348')
func_2349_call = mutated_mod.get_global_var('func_2349')
call_6903 = relay.TupleGetItem(func_2348_call(), 0)
call_6904 = relay.TupleGetItem(func_2349_call(), 0)
func_6847_call = mod.get_global_var('func_6847')
func_6850_call = mutated_mod.get_global_var('func_6850')
call_6918 = relay.TupleGetItem(func_6847_call(relay.reshape(call_6903.astype('float32'), [168,])), 2)
call_6919 = relay.TupleGetItem(func_6850_call(relay.reshape(call_6903.astype('float32'), [168,])), 2)
output = relay.Tuple([call_6862,call_6866,call_6903,call_6918,])
output2 = relay.Tuple([call_6863,call_6867,call_6904,call_6919,])
func_6920 = relay.Function([], output)
mod['func_6920'] = func_6920
mod = relay.transform.InferType()(mod)
mutated_mod['func_6920'] = func_6920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6920_call = mutated_mod.get_global_var('func_6920')
call_6921 = func_6920_call()
output = call_6921
func_6922 = relay.Function([], output)
mutated_mod['func_6922'] = func_6922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5722_call = mod.get_global_var('func_5722')
func_5723_call = mutated_mod.get_global_var('func_5723')
call_6970 = func_5722_call()
call_6971 = func_5722_call()
output = call_6970
output2 = call_6971
func_6999 = relay.Function([], output)
mod['func_6999'] = func_6999
mod = relay.transform.InferType()(mod)
output = func_6999()
func_7000 = relay.Function([], output)
mutated_mod['func_7000'] = func_7000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3709_call = mod.get_global_var('func_3709')
func_3710_call = mutated_mod.get_global_var('func_3710')
call_7015 = relay.TupleGetItem(func_3709_call(), 0)
call_7016 = relay.TupleGetItem(func_3710_call(), 0)
output = relay.Tuple([call_7015,])
output2 = relay.Tuple([call_7016,])
func_7036 = relay.Function([], output)
mod['func_7036'] = func_7036
mod = relay.transform.InferType()(mod)
mutated_mod['func_7036'] = func_7036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7036_call = mutated_mod.get_global_var('func_7036')
call_7037 = func_7036_call()
output = call_7037
func_7038 = relay.Function([], output)
mutated_mod['func_7038'] = func_7038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5957_call = mod.get_global_var('func_5957')
func_5959_call = mutated_mod.get_global_var('func_5959')
call_7088 = relay.TupleGetItem(func_5957_call(), 0)
call_7089 = relay.TupleGetItem(func_5959_call(), 0)
output = call_7088
output2 = call_7089
func_7109 = relay.Function([], output)
mod['func_7109'] = func_7109
mod = relay.transform.InferType()(mod)
mutated_mod['func_7109'] = func_7109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7109_call = mutated_mod.get_global_var('func_7109')
call_7110 = func_7109_call()
output = call_7110
func_7111 = relay.Function([], output)
mutated_mod['func_7111'] = func_7111
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7159 = relay.var("var_7159", dtype = "float64", shape = (9, 14, 11))#candidate|7159|(9, 14, 11)|var|float64
uop_7160 = relay.cosh(var_7159.astype('float64')) # shape=(9, 14, 11)
output = relay.Tuple([uop_7160,])
output2 = relay.Tuple([uop_7160,])
func_7162 = relay.Function([var_7159,], output)
mod['func_7162'] = func_7162
mod = relay.transform.InferType()(mod)
mutated_mod['func_7162'] = func_7162
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7163 = relay.var("var_7163", dtype = "float64", shape = (9, 14, 11))#candidate|7163|(9, 14, 11)|var|float64
func_7162_call = mutated_mod.get_global_var('func_7162')
call_7164 = func_7162_call(var_7163)
output = call_7164
func_7165 = relay.Function([var_7163], output)
mutated_mod['func_7165'] = func_7165
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7248 = relay.var("var_7248", dtype = "float32", shape = (1, 16, 12))#candidate|7248|(1, 16, 12)|var|float32
uop_7249 = relay.cos(var_7248.astype('float32')) # shape=(1, 16, 12)
func_4173_call = mod.get_global_var('func_4173')
func_4176_call = mutated_mod.get_global_var('func_4176')
var_7265 = relay.var("var_7265", dtype = "float32", shape = (585,))#candidate|7265|(585,)|var|float32
call_7264 = relay.TupleGetItem(func_4173_call(relay.reshape(var_7265.astype('float32'), [13, 9, 5])), 1)
call_7266 = relay.TupleGetItem(func_4176_call(relay.reshape(var_7265.astype('float32'), [13, 9, 5])), 1)
output = relay.Tuple([uop_7249,call_7264,var_7265,])
output2 = relay.Tuple([uop_7249,call_7266,var_7265,])
func_7267 = relay.Function([var_7248,var_7265,], output)
mod['func_7267'] = func_7267
mod = relay.transform.InferType()(mod)
var_7268 = relay.var("var_7268", dtype = "float32", shape = (1, 16, 12))#candidate|7268|(1, 16, 12)|var|float32
var_7269 = relay.var("var_7269", dtype = "float32", shape = (585,))#candidate|7269|(585,)|var|float32
output = func_7267(var_7268,var_7269,)
func_7270 = relay.Function([var_7268,var_7269,], output)
mutated_mod['func_7270'] = func_7270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5800_call = mod.get_global_var('func_5800')
func_5802_call = mutated_mod.get_global_var('func_5802')
call_7272 = relay.TupleGetItem(func_5800_call(), 2)
call_7273 = relay.TupleGetItem(func_5802_call(), 2)
output = call_7272
output2 = call_7273
func_7288 = relay.Function([], output)
mod['func_7288'] = func_7288
mod = relay.transform.InferType()(mod)
output = func_7288()
func_7289 = relay.Function([], output)
mutated_mod['func_7289'] = func_7289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3108_call = mod.get_global_var('func_3108')
func_3109_call = mutated_mod.get_global_var('func_3109')
call_7317 = func_3108_call()
call_7318 = func_3108_call()
output = call_7317
output2 = call_7318
func_7341 = relay.Function([], output)
mod['func_7341'] = func_7341
mod = relay.transform.InferType()(mod)
mutated_mod['func_7341'] = func_7341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7341_call = mutated_mod.get_global_var('func_7341')
call_7342 = func_7341_call()
output = call_7342
func_7343 = relay.Function([], output)
mutated_mod['func_7343'] = func_7343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_7409 = relay.TupleGetItem(func_1426_call(), 2)
call_7410 = relay.TupleGetItem(func_1428_call(), 2)
output = call_7409
output2 = call_7410
func_7433 = relay.Function([], output)
mod['func_7433'] = func_7433
mod = relay.transform.InferType()(mod)
output = func_7433()
func_7434 = relay.Function([], output)
mutated_mod['func_7434'] = func_7434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3855_call = mod.get_global_var('func_3855')
func_3856_call = mutated_mod.get_global_var('func_3856')
call_7435 = relay.TupleGetItem(func_3855_call(), 2)
call_7436 = relay.TupleGetItem(func_3856_call(), 2)
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
var_7438 = relay.var("var_7438", dtype = "uint64", shape = (1440,))#candidate|7438|(1440,)|var|uint64
call_7437 = relay.TupleGetItem(func_3347_call(relay.reshape(var_7438.astype('uint64'), [15, 8, 12])), 0)
call_7439 = relay.TupleGetItem(func_3349_call(relay.reshape(var_7438.astype('uint64'), [15, 8, 12])), 0)
uop_7440 = relay.acosh(var_7438.astype('float64')) # shape=(1440,)
output = relay.Tuple([call_7435,call_7437,uop_7440,])
output2 = relay.Tuple([call_7436,call_7439,uop_7440,])
func_7446 = relay.Function([var_7438,], output)
mod['func_7446'] = func_7446
mod = relay.transform.InferType()(mod)
mutated_mod['func_7446'] = func_7446
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7447 = relay.var("var_7447", dtype = "uint64", shape = (1440,))#candidate|7447|(1440,)|var|uint64
func_7446_call = mutated_mod.get_global_var('func_7446')
call_7448 = func_7446_call(var_7447)
output = call_7448
func_7449 = relay.Function([var_7447], output)
mutated_mod['func_7449'] = func_7449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5204_call = mod.get_global_var('func_5204')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_7508 = relay.TupleGetItem(func_5204_call(), 0)
call_7509 = relay.TupleGetItem(func_5205_call(), 0)
func_5391_call = mod.get_global_var('func_5391')
func_5392_call = mutated_mod.get_global_var('func_5392')
call_7512 = relay.TupleGetItem(func_5391_call(), 0)
call_7513 = relay.TupleGetItem(func_5392_call(), 0)
const_7522 = relay.const([[[7.875585,9.271282,-4.450306,2.887338],[-1.573931,0.965978,-7.776712,0.356836],[-2.940881,-5.831032,5.543876,-5.953174],[6.102552,8.131180,-3.186933,8.617839],[-0.536643,0.040449,8.113295,3.535478],[5.114103,-9.500436,0.375015,-2.608816],[-4.469985,6.663740,0.698169,0.664187],[1.429865,-5.245363,-3.833572,8.805419],[9.058722,9.951672,1.854584,-7.458810],[1.807117,-7.583640,-3.993383,-0.738765],[9.693486,-2.491788,8.836563,-1.175794],[-6.890496,4.881077,-3.680392,7.571098],[4.921175,-0.300156,-4.171628,-0.375586]],[[4.502849,-3.670006,3.871220,5.652264],[1.919052,7.001508,5.911162,2.087482],[7.964115,-7.299470,8.788896,2.874109],[6.076747,6.296667,-1.941533,9.501057],[4.227016,5.711446,5.808753,4.294288],[4.537998,0.050659,-4.681773,-3.248946],[0.170951,9.629289,5.580430,-9.797246],[3.820520,-0.081622,7.248037,3.456948],[8.603371,9.493024,2.133789,5.958941],[0.943122,-2.621374,2.847054,1.085649],[8.622669,5.467427,3.966034,2.958090],[-4.898744,-4.860931,-3.701826,-7.240450],[0.949107,-9.230957,-3.745668,2.381288]],[[-0.735656,-2.587629,-4.783323,0.422802],[-6.191863,-7.592207,-2.394441,-8.458011],[4.489315,-4.700461,3.958590,-7.228823],[-7.535569,8.086511,-1.849007,-3.261250],[-7.427405,9.865940,6.841330,9.891741],[1.656040,5.699110,9.297906,-4.348231],[2.697765,-6.239537,0.140242,2.571783],[5.572151,6.402013,1.020214,9.226538],[-4.477953,-2.779524,4.584153,5.890370],[-6.963401,-9.541314,9.304991,-9.099740],[6.755425,5.005927,8.655368,-5.505937],[1.024983,3.472464,2.156297,9.319851],[8.712362,3.665580,1.284019,9.493140]],[[-6.017740,4.550441,1.148028,-6.902322],[7.677602,1.845146,-2.713385,6.346267],[0.597261,-7.730127,7.589385,-4.204312],[4.511998,3.688258,4.839662,-4.473072],[-4.525421,1.820095,-2.220659,-3.330855],[8.174347,-3.764440,0.871245,8.294313],[-2.325668,-9.322649,7.716206,-8.196361],[-4.404140,8.803219,5.542168,9.259892],[-6.132349,7.988030,-6.869694,-2.834015],[6.783990,0.228490,-9.127478,-6.343079],[-1.751009,4.935991,7.031666,8.405759],[9.201414,3.607297,-9.435722,2.473717],[6.700276,0.765678,-9.948139,8.640979]],[[0.209771,8.653700,-3.249995,-6.731827],[-7.522877,-7.624714,-7.228723,3.741875],[1.774939,-9.369070,-3.863876,-4.898593],[-7.607626,2.217472,5.501740,-2.365336],[-8.660901,-7.400066,8.541523,1.380201],[-1.494174,-2.171962,1.579048,6.054355],[-5.622264,6.785022,3.795673,5.219052],[8.259065,-1.117090,3.480193,4.690049],[-1.955498,-7.897700,4.069460,3.443845],[-4.491086,-8.356837,-9.102709,-8.917003],[1.689050,9.863020,6.940436,-4.717767],[1.117202,6.369047,7.134117,-3.397550],[-9.994815,-5.106731,3.360566,-1.895799]],[[0.895490,6.533596,-8.090852,-7.216267],[5.153019,-0.014104,-8.427565,-6.284258],[7.136288,0.748322,-9.781210,0.630414],[-3.058051,-2.395751,2.007645,0.740386],[6.873455,-0.854598,-0.123179,6.917264],[-0.820428,-7.421260,-9.263673,8.206057],[-0.395017,0.222283,-8.672389,-7.527178],[-0.468451,-8.458201,5.878785,-5.303603],[4.710193,-5.258034,5.446073,7.422344],[6.693090,2.744726,-7.854319,6.648623],[8.305688,-1.611646,0.606762,-8.202857],[1.321141,-6.422131,8.303035,-4.025533],[4.156945,-7.850266,-0.851371,2.150432]],[[-5.852821,-6.009880,1.251066,5.974888],[-6.961751,-5.959024,-1.425395,3.165469],[-0.587976,-4.114920,-5.321168,-4.444285],[0.985386,-5.840735,-5.914655,0.654267],[-5.855909,-1.892289,-1.241797,-9.658728],[5.033243,-6.955894,-2.197690,4.862813],[5.250150,-0.071307,-5.880669,-7.236577],[1.421162,-6.534952,-9.687732,-8.953788],[6.396398,-3.608790,5.596211,-8.620064],[4.850586,-1.372709,-0.158235,-7.668138],[-5.826457,0.289487,2.346345,-7.208892],[-6.207251,0.121398,0.083795,-5.447442],[-2.549989,-5.431292,2.001608,-6.128082]],[[7.471929,-4.617370,-5.088922,-5.425646],[5.035647,-1.884522,0.891410,-2.973760],[2.003777,-6.488837,8.848816,6.109337],[8.319791,1.733711,-3.011225,1.065944],[1.311813,4.029387,3.347613,-2.298462],[1.024741,5.312641,7.564341,-5.300179],[7.122825,2.140068,4.738526,-1.151817],[-5.783725,-8.870786,5.106432,8.141696],[9.674088,6.482184,-5.603064,-9.177250],[-2.511034,-2.978016,6.111275,-7.782565],[6.648933,3.798168,-3.722607,8.792389],[-0.550347,3.093405,6.807826,-9.792882],[8.195945,0.257098,0.633847,9.078506]]], dtype = "float32")#candidate|7522|(8, 13, 4)|const|float32
bop_7523 = relay.maximum(call_7512.astype('uint8'), relay.reshape(const_7522.astype('uint8'), relay.shape_of(call_7512))) # shape=(8, 13, 4)
bop_7526 = relay.maximum(call_7513.astype('uint8'), relay.reshape(const_7522.astype('uint8'), relay.shape_of(call_7513))) # shape=(8, 13, 4)
func_6736_call = mod.get_global_var('func_6736')
func_6737_call = mutated_mod.get_global_var('func_6737')
call_7530 = func_6736_call()
call_7531 = func_6736_call()
func_3325_call = mod.get_global_var('func_3325')
func_3326_call = mutated_mod.get_global_var('func_3326')
call_7542 = func_3325_call()
call_7543 = func_3325_call()
bop_7552 = relay.mod(call_7530.astype('float64'), relay.reshape(call_7512.astype('float64'), relay.shape_of(call_7530))) # shape=(8, 13, 4)
bop_7555 = relay.mod(call_7531.astype('float64'), relay.reshape(call_7513.astype('float64'), relay.shape_of(call_7531))) # shape=(8, 13, 4)
func_7036_call = mod.get_global_var('func_7036')
func_7038_call = mutated_mod.get_global_var('func_7038')
call_7556 = relay.TupleGetItem(func_7036_call(), 0)
call_7557 = relay.TupleGetItem(func_7038_call(), 0)
func_1837_call = mod.get_global_var('func_1837')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_7564 = relay.TupleGetItem(func_1837_call(), 2)
call_7565 = relay.TupleGetItem(func_1838_call(), 2)
output = relay.Tuple([call_7508,bop_7523,call_7542,bop_7552,call_7556,call_7564,])
output2 = relay.Tuple([call_7509,bop_7526,call_7543,bop_7555,call_7557,call_7565,])
func_7570 = relay.Function([], output)
mod['func_7570'] = func_7570
mod = relay.transform.InferType()(mod)
mutated_mod['func_7570'] = func_7570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7570_call = mutated_mod.get_global_var('func_7570')
call_7571 = func_7570_call()
output = call_7571
func_7572 = relay.Function([], output)
mutated_mod['func_7572'] = func_7572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2623_call = mod.get_global_var('func_2623')
func_2625_call = mutated_mod.get_global_var('func_2625')
call_7601 = func_2623_call()
call_7602 = func_2623_call()
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_7603 = relay.TupleGetItem(func_348_call(), 1)
call_7604 = relay.TupleGetItem(func_349_call(), 1)
const_7606 = relay.const([[[4,-7,-6,4],[-4,-9,6,-7],[-4,5,7,10],[7,1,-3,-9],[2,1,-4,-8],[-6,5,6,-1],[8,-10,-7,-9],[6,6,-6,-8],[4,6,6,6],[-4,-6,-6,-1],[-2,-7,1,7],[-5,1,-9,-10],[10,-1,-2,10]],[[10,6,-4,10],[8,-7,3,-8],[-9,2,8,3],[9,-4,-2,7],[-10,-10,10,10],[-7,-8,-3,1],[-7,-1,4,-3],[-9,6,-3,5],[-7,-10,5,8],[-1,10,-5,7],[3,-9,2,-4],[10,4,2,-1],[-4,-8,10,-9]],[[-2,-4,-2,-1],[9,-6,3,-3],[9,-8,-7,-1],[-9,8,-7,-2],[-9,-8,-7,8],[10,-8,3,7],[7,10,-6,4],[2,-7,-10,7],[-7,-10,5,-2],[-1,9,-2,-3],[-6,4,6,9],[2,6,-7,1],[8,-8,-9,-10]],[[-3,-4,9,-3],[-2,7,6,7],[-2,-10,-6,2],[-2,8,3,6],[1,8,-7,3],[9,-9,-3,-3],[-9,-5,3,8],[-8,-1,-8,-6],[6,7,8,-5],[9,3,10,9],[8,4,-1,-9],[3,-1,-6,10],[-2,5,6,-6]],[[6,6,-3,7],[1,3,8,-3],[1,-3,-1,-8],[7,-1,-7,-7],[6,1,2,-3],[3,-5,7,3],[-1,6,7,-5],[1,-9,-4,-1],[4,2,-2,-9],[10,-6,-3,8],[5,-8,-9,-9],[10,7,6,6],[10,8,-4,6]],[[4,-2,9,2],[5,-6,-2,3],[3,-6,9,-1],[-2,2,-7,-10],[8,-7,-4,-3],[-7,-1,4,-1],[-7,-7,8,7],[10,-6,6,7],[7,-1,3,10],[-2,10,-7,4],[7,10,1,7],[-7,-8,8,6],[-9,8,2,-3]],[[9,2,-4,9],[8,-9,9,2],[-1,-8,6,-8],[-5,-7,2,-1],[3,6,10,1],[7,8,-9,1],[-9,-1,-4,-9],[3,6,-8,-8],[-10,10,-2,-9],[2,4,-6,-1],[3,-9,1,6],[6,1,10,-4],[-8,2,9,8]],[[7,-5,4,-7],[8,-5,-5,-4],[4,-4,-7,-5],[-7,4,8,-7],[3,-7,6,5],[1,-4,3,-7],[5,9,2,-6],[1,-2,3,4],[-9,-4,-7,2],[1,4,6,-10],[5,-3,-5,7],[-1,7,-8,2],[1,6,-7,6]]], dtype = "uint8")#candidate|7606|(8, 13, 4)|const|uint8
bop_7607 = relay.divide(call_7601.astype('float32'), relay.reshape(const_7606.astype('float32'), relay.shape_of(call_7601))) # shape=(8, 13, 4)
bop_7610 = relay.divide(call_7602.astype('float32'), relay.reshape(const_7606.astype('float32'), relay.shape_of(call_7602))) # shape=(8, 13, 4)
output = relay.Tuple([call_7603,bop_7607,])
output2 = relay.Tuple([call_7604,bop_7610,])
func_7645 = relay.Function([], output)
mod['func_7645'] = func_7645
mod = relay.transform.InferType()(mod)
output = func_7645()
func_7646 = relay.Function([], output)
mutated_mod['func_7646'] = func_7646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_348_call = mod.get_global_var('func_348')
func_349_call = mutated_mod.get_global_var('func_349')
call_7664 = relay.TupleGetItem(func_348_call(), 1)
call_7665 = relay.TupleGetItem(func_349_call(), 1)
output = call_7664
output2 = call_7665
func_7672 = relay.Function([], output)
mod['func_7672'] = func_7672
mod = relay.transform.InferType()(mod)
output = func_7672()
func_7673 = relay.Function([], output)
mutated_mod['func_7673'] = func_7673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1553_call = mod.get_global_var('func_1553')
func_1554_call = mutated_mod.get_global_var('func_1554')
call_7707 = relay.TupleGetItem(func_1553_call(), 0)
call_7708 = relay.TupleGetItem(func_1554_call(), 0)
func_3226_call = mod.get_global_var('func_3226')
func_3227_call = mutated_mod.get_global_var('func_3227')
call_7713 = func_3226_call()
call_7714 = func_3226_call()
func_1325_call = mod.get_global_var('func_1325')
func_1329_call = mutated_mod.get_global_var('func_1329')
var_7719 = relay.var("var_7719", dtype = "uint64", shape = (1440,))#candidate|7719|(1440,)|var|uint64
call_7718 = relay.TupleGetItem(func_1325_call(relay.reshape(var_7719.astype('uint64'), [15, 8, 12]), relay.reshape(var_7719.astype('uint64'), [15, 8, 12]), ), 1)
call_7720 = relay.TupleGetItem(func_1329_call(relay.reshape(var_7719.astype('uint64'), [15, 8, 12]), relay.reshape(var_7719.astype('uint64'), [15, 8, 12]), ), 1)
func_7288_call = mod.get_global_var('func_7288')
func_7289_call = mutated_mod.get_global_var('func_7289')
call_7735 = func_7288_call()
call_7736 = func_7288_call()
func_4631_call = mod.get_global_var('func_4631')
func_4632_call = mutated_mod.get_global_var('func_4632')
call_7744 = func_4631_call()
call_7745 = func_4631_call()
func_1211_call = mod.get_global_var('func_1211')
func_1215_call = mutated_mod.get_global_var('func_1215')
const_7755 = relay.const([[5.815538,5.867947,-0.801433,-8.809999,4.909363,-9.236145,-4.459231,-2.468665,-0.799411,3.866831,9.750840,9.442851,6.116414,-1.942513,-5.713300,9.765241,-9.554822,5.556341,-9.642306,-0.366343,9.373583,3.171373,6.692980,5.931061,-8.971834,-7.025126,-8.747671,9.272665,8.924292,9.800549,-6.410167,9.065273,8.631900,-8.977975,-3.242309,6.782088,7.787750,-4.256098,-9.594115,-6.824570,-1.930234,4.570663,-7.483502,-5.909234,-3.065485,-6.695503,-3.166809,-7.165814,-9.021577,6.827773,3.767308,-9.677675,3.625422,7.220010,-4.659185,-1.992583,7.211224,9.379221,6.373030,3.703340],[8.875075,-2.064926,1.774497,6.698943,9.762398,7.303731,-6.605350,-8.368019,-1.517610,1.865662,0.623948,6.167256,7.752800,5.806891,-0.935410,4.773270,-4.949222,5.053771,-7.463460,5.869109,8.539796,-2.986997,-4.584047,-8.182555,-4.910415,-3.333267,0.377428,-7.795026,-6.558932,8.619832,-9.230696,7.002468,2.418077,2.719445,3.357789,4.951344,5.275934,-0.303430,-4.381627,-0.393305,8.004318,7.271651,-3.912316,0.987539,0.343679,0.843030,5.108474,-4.682788,7.721310,-7.161051,-8.787770,3.748633,1.807431,6.801751,-3.032219,7.182110,-9.828652,6.236903,-6.827655,-4.290995],[4.494504,-4.207573,-5.947888,6.241910,-6.577414,-1.924689,-3.748335,-6.665880,-0.464285,2.024819,5.591608,-0.098572,8.416162,-8.370516,-0.116924,8.679853,-5.863202,6.774093,-6.173347,-4.834963,-7.858800,7.503589,-4.866649,6.852222,-1.378203,-6.936906,6.816113,5.316219,-6.827082,-1.225278,-7.560597,-4.409495,5.294954,1.354742,4.282555,-7.488126,4.109219,-5.980175,9.292769,-0.750954,-3.814822,4.426707,1.031995,7.591423,-3.100536,-9.003648,4.046178,1.500021,-2.428632,9.602286,-3.792572,-3.491272,0.368218,-0.022549,-2.670643,-1.266017,7.817948,-8.255709,8.413231,-2.855328],[4.463041,-7.557952,4.964644,-5.422814,5.331132,2.550473,6.530622,7.548624,-4.353412,-2.370771,-1.964882,-1.567143,-9.873462,-8.113675,-9.799155,-1.260398,8.955889,-9.346511,-6.941737,6.667271,-2.614916,-9.247235,-8.541530,3.397845,1.370202,6.521778,-5.071982,5.530083,-0.468561,-4.897210,-9.266437,-8.738438,-3.209961,-1.247347,7.911967,-2.943005,7.050472,-5.030452,-3.086600,-6.752813,6.300204,1.662421,1.982457,-4.737313,-7.738021,-3.571993,8.320952,-6.145766,-7.391189,6.618805,-5.715578,0.154310,-6.997269,8.865833,1.808111,-5.947047,7.997939,4.507871,-4.467123,-4.370682],[-9.584669,1.053208,-6.235374,8.720328,-4.930124,-2.266483,-9.205645,-7.145128,9.265698,9.937839,-3.537930,0.687447,9.259365,-7.129535,8.419325,-3.065464,-7.456909,4.825095,-5.919889,1.556506,7.113238,7.844506,8.569087,-4.459154,-4.424574,-5.457708,0.733736,-2.900081,-8.711903,-5.409327,-9.049701,1.646097,-4.008087,5.770341,-1.492169,-4.953376,-4.677429,9.470735,5.989125,5.791401,-8.475810,-5.005836,9.091447,-1.082459,-2.986272,8.422842,-1.168844,2.851144,-9.481846,0.789495,4.851405,-6.326598,3.862393,0.217400,-7.896833,-7.331146,-8.038878,-9.217982,-6.441599,5.078253],[-3.984076,4.124326,-4.138878,4.072173,8.117796,3.342468,-7.692620,-2.752077,6.964839,4.337104,-8.617416,-8.750234,-0.687426,9.694909,-9.743055,8.328210,4.294782,4.903042,0.085372,-2.255477,9.279900,3.487039,-3.093066,9.905263,-3.397716,1.908113,9.999149,5.428730,-1.347556,-9.727102,-3.461992,2.531052,-3.169694,3.166853,-7.304462,-4.960405,2.434600,1.359657,1.557724,1.185756,4.713019,4.741799,2.734538,0.794380,2.709411,-0.466875,9.340130,7.617959,-8.345911,-2.332937,7.884770,-7.641703,-2.309861,-3.955284,-6.858600,1.541299,-1.431088,-8.235580,-6.253246,4.383531],[5.429419,6.198492,-9.523523,-8.707863,1.325079,9.906052,5.530330,8.874485,9.367265,-3.963613,7.922988,-3.019364,-3.971523,2.009685,-6.351807,-1.062289,-9.812377,-0.823499,-9.480400,5.731073,0.237957,-4.857189,-1.201118,4.556198,6.265901,-1.428749,7.773630,-5.366483,0.421254,-9.360759,1.934144,-1.071828,-5.270487,-2.327063,4.664764,-7.495427,-3.495082,-7.589210,-8.881321,-3.922214,5.142341,7.010036,1.317364,-5.401691,9.478356,-0.293002,9.933188,2.502078,-6.224196,-5.016454,0.713172,-6.618468,-7.997122,6.651950,-2.401399,-0.004851,-5.184455,7.584938,-6.278157,-6.108354],[-6.211909,-7.394612,9.554383,-3.959526,1.653372,-4.720118,6.800523,-6.491005,2.487795,2.345192,5.394036,7.125003,8.811958,-8.596147,-4.309436,3.833533,9.683833,-0.275526,3.506346,-6.367296,2.887444,-5.340639,-5.471797,-7.306406,-6.775432,9.487289,-7.837093,6.999225,4.209187,8.760447,-0.144009,4.910285,-4.742504,0.429771,-2.520255,-4.365891,-7.807689,-0.507796,5.230626,-7.921464,-6.530658,0.019577,-9.536588,-3.000718,-0.736932,3.753889,0.215496,3.163248,-4.520954,3.911667,-2.606008,-5.107638,-4.155786,7.945879,-4.689691,1.391153,-2.368066,5.285995,7.699130,-9.866460]], dtype = "float64")#candidate|7755|(8, 60)|const|float64
call_7754 = relay.TupleGetItem(func_1211_call(relay.reshape(const_7755.astype('float64'), [120, 4]), relay.reshape(call_7718.astype('float32'), [416,]), ), 1)
call_7756 = relay.TupleGetItem(func_1215_call(relay.reshape(const_7755.astype('float64'), [120, 4]), relay.reshape(call_7718.astype('float32'), [416,]), ), 1)
func_2193_call = mod.get_global_var('func_2193')
func_2195_call = mutated_mod.get_global_var('func_2195')
var_7761 = relay.var("var_7761", dtype = "float64", shape = (720,))#candidate|7761|(720,)|var|float64
call_7760 = relay.TupleGetItem(func_2193_call(relay.reshape(var_7761.astype('float64'), [8, 6, 15])), 1)
call_7762 = relay.TupleGetItem(func_2195_call(relay.reshape(var_7761.astype('float64'), [8, 6, 15])), 1)
func_7162_call = mod.get_global_var('func_7162')
func_7165_call = mutated_mod.get_global_var('func_7165')
const_7770 = relay.const([9.425322,1.433772,1.700222,0.995296,-6.921849,-3.001431,-7.276884,-9.637933,-1.016076,5.942769,-4.256820,6.515333,4.505225,4.243024,-5.643903,-2.044904,-0.872996,6.971116,2.353438,-0.530675,-0.990484,-1.050666,-3.270802,-4.867534,-8.456768,-0.824351,8.177887,-6.700555,2.984067,6.559610,5.892446,3.339143,7.401866,2.874540,2.156623,-4.715286,-8.055009,5.043984,1.488016,-7.702745,3.720390,-2.425021,-8.957480,7.647600,6.312319,9.535540,-9.841754,-9.594040,5.043550,-1.082106,7.265309,4.577832,-3.514572,0.948105,-6.035828,1.151833,-3.375027,-5.296159,-0.477523,5.465418,-6.667415,-9.587599,3.441314,-2.583243,-3.577511,-7.487175,8.387261,-1.327145,-0.783206,2.696687,0.630288,-5.761382,-1.345924,-9.518744,-2.076475,-6.891419,-1.232570,4.823772,-8.175002,-6.776015,-7.951662,-8.606858,-5.104599,9.361600,-2.445651,8.330945,1.915822,-3.612730,-8.010136,-2.079975,-2.274801,7.154252,7.783344,-8.019361,-4.205251,7.335380,8.875702,-9.586691,-4.456798,-7.026914,-1.178755,-2.583637,2.916763,-2.875688,3.389945,-5.745346,4.237905,-8.413908,-0.441838,-7.164895,2.271864,-6.513452,-5.388778,1.661568,-9.942117,8.304109,6.260217,5.723074,-4.689788,7.022987,-6.592872,3.675293,5.239233,6.149419,4.963266,8.071114,1.480219,5.956936,-6.032621,-9.194893,0.418249,-1.405389,4.446691,0.620729,8.040442,3.940504,9.203881,7.329500,-1.585206,-0.913242,8.748217,-6.936376,7.629933,-2.622688,-5.311339,3.016491,-5.089228,8.526061,7.658498,-8.671523,0.178181,-0.594062,-8.740841,4.017546,-0.870519,-7.782007,6.733947,-8.626022,3.730343,8.684228,2.508748,2.131520,-0.495265,0.796793,1.491754,-6.018474,1.361509,7.550290,-2.133050,-4.149226,0.385218,-0.058907,-8.580177,0.296937,9.275637,1.802526,8.611182,9.209218,4.317160,1.280237,-9.345153,1.102537,7.863581,1.196837,-6.390286,-8.435585,9.748168,-4.295524,-2.367175,1.453389,-9.675573,-1.924509,7.618259,3.605432,0.111978,3.841110,-7.204792,4.108269,-7.659566,-5.604685,3.992287,-6.758476,2.692761,-0.664204,-2.345194,-7.957918,-5.365661,3.911542,-5.093387,4.691626,2.572292,0.367896,8.460109,6.884164,4.431833,-9.817222,7.325338,6.955647,-9.254725,-7.761300,5.414812,3.590901,6.599203,6.554421,-6.866014,0.085926,-6.359742,8.995534,-7.420086,2.436276,-7.744302,-9.344089,-8.219295,9.728495,5.575064,3.531830,-5.027600,-4.708485,6.727541,7.887737,-2.104735,-3.872232,7.854398,4.417034,-6.953983,4.599441,-5.983053,-5.297333,-0.024885,6.328284,2.465770,-6.596770,-9.317733,-4.554211,7.057167,1.908321,-5.819053,-6.668258,5.627391,3.010794,-3.245641,6.601561,-9.037892,3.342978,8.872444,-0.445436,0.701940,-9.471087,-8.705203,-3.590901,-2.489627,9.192075,0.180130,-0.861584,3.658124,-5.990926,-5.043112,5.036081,-5.527807,5.656695,0.550525,-1.859881,4.037970,-5.318113,4.768465,9.522453,-3.995487,4.416639,-6.426919,1.931817,2.777317,2.234251,0.341888,4.616270,9.009709,9.538218,-0.084068,5.913542,-7.654446,8.401807,-7.555629,2.292726,-5.866997,-0.836735,-0.682010,-2.072747,-5.212633,5.209083,-5.291291,8.490307,-1.482277,7.050932,-0.520067,-9.352611,-4.048725,5.988822,-4.902807,-5.757187,0.840274,6.102066,-9.350950,1.467007,4.699411,-5.249187,6.055569,6.319645,-7.455727,6.574108,8.831372,9.247530,7.156087,5.090379,5.734510,-6.206358,-2.510347,-3.732247,-5.178526,0.587451,-6.270218,6.798973,2.950213,9.817566,9.797074,7.650423,-8.335882,1.437288,9.694831,5.516736,-7.258714,1.280119,0.696502,1.316649,6.397062,1.354934,-7.063846,-2.328478,7.704440,5.763886,-2.662614,-5.967693,8.961849,-1.559983,-8.871537,5.194974,-1.908519,7.421286,-3.682547,7.198253,-9.914680,1.005438,2.087432,-2.022876,-5.579063,-8.830134,-3.268408,7.458246,-7.423318,-8.164187,-1.155819,4.558794,-0.278043,-2.441292,5.829235,4.758439,1.259912,-3.957632,-4.478150,1.783831,-8.165129,0.846312,-4.056653,-3.758823,-8.147961,4.689805,-4.239106,0.310328,-4.300998,8.538021,4.052626,4.448537,2.465409,-5.520808,-7.007375,-4.423761,5.142418,-2.825369,6.627292,-7.130783,1.980743,-1.036745,-5.972834,8.855368,5.635426,-7.895297,1.694261,4.838798,3.399075,-1.785519,-7.994672,-2.687153,-7.336816,3.694346,2.398350,6.225468,-5.234657,-6.607503,-4.369753,4.885028,-1.182812,-3.115935,3.042296,-9.907058,4.397288,-1.848345,-1.154080,3.745515,5.894067,-4.740899,-9.090580,-7.311542,7.852710,3.639164,-6.982948,7.031169,-7.844020,-6.015245,-4.911301,-7.926217,8.279360,7.060118,2.868336,-0.945141,7.166909,4.812485,-8.980350,-6.600302,-3.579242,4.877115,-3.540648,2.150942,9.802902,-0.974324,9.053991,4.442271,-7.913276,-6.260792,-1.662464,-4.231983,8.016261,4.975803,5.095958,3.251406,-5.196708,-1.435037,8.919348,7.821096,3.951961,-3.109085,1.734888,7.840386,-8.060386,6.872690,-3.826286,8.646237,-9.652696,-9.740064,-5.915176,6.657507,-6.885476,-4.447820,-0.541342,-8.598466,3.800555,-9.335892,5.307592,-5.640627,9.795761,-3.244391,-6.925155,6.949627,-6.611545,-4.593216,5.061033,3.600466,-7.399687,0.720385,-7.397619,-0.498838,0.122246,-0.877220,3.736617,-1.576368,-7.569478,-2.720807,-6.874810,8.069204,5.197111,-0.518245,-5.954033,4.368082,3.617818,1.498123,-5.528254,1.531725,-0.880300,-1.389943,2.450189,-0.116928,7.820647,-7.094253,-9.127879,0.131309,3.501245,-0.253344,3.882513,-4.661536,-7.376084,-6.264352,-0.549184,-4.197385,7.402461,-6.593471,-5.145596,0.400321,6.592933,9.478213,4.651995,-4.996282,-9.125093,-0.461120,-0.208490,-4.959808,-2.243163,1.906490,8.154429,0.839362,0.036633,4.595065,-2.688925,5.458888,-3.037735,5.116102,5.736460,-1.953881,-7.252341,-6.083320,-9.402615,-4.308096,2.098379,8.661411,1.116840,-1.831310,-0.007170,-9.638349,-9.297077,-8.288687,4.207810,-1.383903,9.722855,-5.011157,-5.119668,-1.014670,-8.135001,6.249372,1.650175,-4.409064,-3.596223,2.980218,-4.045561,5.173726,0.873862,3.779430,-5.754092,-0.395707,-1.571973,9.763059,2.533010,5.976031,-6.207501,0.539084,1.892335,0.866703,-8.884225,-0.989558,-5.497014,4.217547,-0.535418,-4.294421,1.459081,-3.167859,-7.446464,-6.651716,-5.118488,5.223311,-6.030712,-2.711343,-1.205394,8.444726,-9.221835,9.442911,-3.559901,-4.176780,2.295117,4.139290,3.103842,-0.118767,5.237017,8.145497,4.095401,6.514386,-9.175403,6.063031,2.128761,6.988188,7.692351,-0.085947,-4.994253,-7.927467,-3.927983,-4.533705,8.365024,8.277889,4.200359,-1.824658,8.061920,-5.132359,3.183784,-8.449850,7.678959,-5.726093,-0.700610,-9.869399,-4.231545,-3.769424,-8.283363,-8.891228,3.706492,-7.875670,8.061740,4.675925,-9.527081,-4.493541,-7.013690,-9.230231,-8.860922,-2.956602,-2.670945,9.117904,5.010815,4.730763,-0.335976,0.432239,8.814692,-2.205179,7.801590,9.442533,-3.789621,2.125343,-3.763768,-4.546754,6.155210,6.955648,1.920363,-5.019786,-2.189729,-9.880135,8.540664,-6.361393,1.577309,2.841164,2.487931,9.716816,-8.808379,-6.870960,-8.253136,-9.999935,1.522867,8.145326,-8.707050,7.822952,6.572115,-4.076789,3.354404,5.207762,9.090105,2.819136,9.672714,-5.280929,-7.000557,-1.123808,5.292421,-3.016194,-3.585637,1.446863,7.217786,6.479075,-9.479014,2.135492,5.377543,6.132053,-0.428141,0.863221,9.435094,1.702694,-1.159077,-7.337602,-3.435602,-5.508036,8.756941,-8.193307,-4.145394,7.476843,2.406376,-2.095859,-5.914627,2.367842,5.477478,-9.932397,3.309157,-7.077456,-2.854185,4.660471,1.265786,0.165056,-4.312047,6.113024,-5.575063,4.888756,4.088675,-9.112854,8.250238,-3.456744,-9.493945,0.209330,6.568787,7.739262,6.965632,-9.317367,-8.863338,9.396728,4.576753,0.336694,5.110744,0.459562,-5.600628,-0.920752,-8.113757,-2.312307,-6.131509,-8.975234,4.881911,7.047101,-1.254046,1.924280,9.808482,3.935797,7.183647,-7.022477,-1.021718,-6.680089,7.288806,-1.055736,6.642648,-7.995092,8.647582,2.500247,-9.326710,4.599545,8.183186,2.390147,6.133809,0.752530,4.242796,4.633543,-5.431000,4.487918,0.527806,7.461934,-0.394221,-7.109493,-3.650046,1.138504,-1.825556,4.254087,0.728600,-9.270597,-6.434382,-5.850823,-3.692467,0.347294,9.347927,-4.815175,-1.764533,4.819244,-9.088105,-5.836193,-4.904898,9.382965,-7.513634,-5.320351,-8.691820,-9.163658,-6.235965,-9.171547,5.976268,8.607795,-9.294360,7.869108,5.091064,-8.826361,-2.426742,-2.591866,-8.806790,0.735781,7.796339,-2.218368,-9.172545,-1.341714,6.653467,5.782526,-7.008916,7.231318,6.134586,5.991121,-6.085143,-6.718386,5.377330,5.756383,-2.173095,-7.039905,-8.540798,6.883625,-9.605798,6.357545,7.518160,-7.209058,-9.075489,-1.856654,-3.235367,-6.038438,4.912846,1.290393,-5.231928,-6.571393,9.243462,-4.574820,-6.890062,-7.199888,7.914951,-4.633523,7.507377,-6.678196,3.976499,8.871814,-5.852627,-2.032459,-0.964190,-5.565924,-7.023805,4.893083,-4.000368,6.304636,-9.283497,8.699964,8.292732,-5.705917,-4.404199,-2.082299,2.808172,3.890731,-0.282368,-1.220324,6.427915,3.111767,0.545293,8.398157,-3.057345,-8.389569,-9.003312,-6.609588,-3.000691,-0.843427,8.842765,-3.144154,-5.264842,-5.376163,2.118395,8.341622,-5.126827,-5.225375,-4.650568,5.501078,-2.555085,3.397350,5.469446,-2.009530,-8.490913,-1.209395,-1.972151,-2.919863,-4.745812,0.277737,9.934347,-9.608370,1.214420,-8.212017,-1.675042,-1.386428,1.509034,1.917595,6.175298,-9.872374,5.631897,2.891779,1.148690,-4.622107,-6.437499,8.184104,2.668250,0.376395,-8.478529,-4.033597,5.050876,1.889986,-6.723295,6.685799,9.093469,9.254735,-2.749376,-9.743362,-0.416546,7.859429,-6.959326,8.384156,-1.952683,-8.270175,-9.987208,2.121212,4.812452,-6.999273,-5.079271,6.427023,-7.698751,-6.528419,7.118599,-2.107406,5.246164,-1.506708,9.960094,0.397344,7.842581,-4.091883,-9.000603,1.508450,8.671273,3.652338,-7.966289,1.465524,3.269598,0.953148,-5.501044,7.264188,-5.036988,6.263115,3.794334,4.927515,-0.592040,-5.275687,-8.007700,-2.096603,7.409423,7.592636,-8.620767,-7.347091,-0.127070,-6.308219,-0.861821,-8.144753,4.968882,-4.151401,2.911125,5.891088,1.124683,-8.822581,-4.504810,8.998503,1.876922,3.015318,2.715555,5.006052,2.157369,-7.424642,8.474811,-2.008569,-9.956068,2.272021,7.962462,8.245321,-0.184894,-9.716900,-9.650197,7.718826,-2.694672,8.586257,-4.757548,2.849278,-6.747788,4.486347,-0.588954,6.833184,-6.688463,-2.090291,5.026754,7.571116,-2.897880,-1.201151,8.085582,-8.026409,-4.234543,-9.071871,-0.857024,1.138308,4.733599,7.388824,-1.065516,2.562609,8.754687,-8.173676,4.602466,2.136622,3.135991,9.744865,1.973760,-0.754191,1.854233,-1.652449,-6.867434,7.121814,4.728607,-1.087541,3.637584,-4.190703,6.822031,2.899035,-1.423148,-3.402791,2.031716,8.179648,4.870061,-8.525219,-3.339177,0.535323,-3.941526,-5.171776,1.721394,-9.780062,-3.518529,9.927321,5.603985,0.411358,7.040511,-8.276079,0.354920,4.878567,4.483775,7.087375,7.840866,5.415716,8.271732,3.842415,-0.651121,1.933580,-8.170403,-3.004332,-1.306772,-8.811595,-9.145353,-6.475437,-6.572085,-5.133638,1.002444,2.117912,-7.291482,0.823243,-0.545568,-9.715773,-7.142295,-3.059264,3.383827,-6.945116,-3.986813,0.737171,4.614611,-6.770166,-0.857592,-6.881766,-2.501248,-0.402669,-7.679439,5.683916,-0.777731,4.267005,8.427204,7.715033,-6.931712,-8.158082,-5.733944,9.835341,0.836467,9.749465,3.821339,-5.050130,7.968884,-9.282221,-5.628764,0.256020,-0.889306,1.318484,-4.951718,-0.507350,-9.230779,4.909267,-6.855804,2.527709,-8.163543,6.116538,-2.296959,9.979805,-3.236775,8.604731,2.920546,2.726357,5.012602,-2.555173,-7.913331,-2.033560,5.964998,4.881306,2.260137,-5.089351,-9.247529,7.217728,0.117704,-1.809366,-0.071835,-2.136397,-8.562098,6.316442,-1.862256,6.031040,-0.973218,9.143610,6.697657,-1.063783,2.759940,-1.543015,-0.274441,-8.922161,6.662569,-8.570038,-2.109603,9.081508,-7.832258,-0.768781,-8.769262,6.180422,-3.003351,8.523849,-4.318198,-5.980619,-8.967819,7.446363,-1.361760,-7.986844,-4.002606,4.774296,4.639110,-7.519427,-1.216258,-1.755434,-9.571296,3.865312,-0.066736,4.694240,-5.307611,6.376849,-2.796561,-7.740666,-7.428040,-4.982085,5.797441,-2.992600,2.935985,-7.308084,0.631747,-4.888729,4.587355,-1.214206,-2.725274,-5.458759,9.214795,0.958717,-8.799158,-1.637371,-2.123929,9.489829,5.983668,-8.544398,-5.745185,-9.157550,5.225382,-3.581756,-6.358189,2.650788,-1.285615,-6.208728,0.988843,1.345183,6.755759,-7.330822,5.302617,9.571119,6.269993,9.877345,-9.966564,-2.303830,-1.118700,-4.202736,0.384934,-1.786634,1.144588,-4.690872,-6.483917,-0.009424,6.882481,-4.944348,3.442209,6.353834,7.913201,-4.159787,-5.733607,-7.284757,3.472261,-9.835164,-5.827179,-8.043723,5.727408,-0.546061,0.466835,5.743030,1.602464,8.959404,3.176571,-8.906986,5.189219,-6.365535,4.668613,-0.368052,-9.579838,8.288914,7.392231,-8.269891,-0.375711,5.687541,-0.306909,8.382825,-0.974727,-8.366070,1.393209,-5.799552,1.299332,5.569080,8.250479,-6.432168,-3.307322,-0.654981,9.412328,-8.670808,0.278640,5.460416,-1.247305,-5.899920,6.319704,-3.855880,1.283298,4.391304,0.744822,0.789692,4.724471,-4.777573,4.955533,9.677638,-4.480880,9.336598,7.780857,1.736486,9.482698,-0.420633,-3.317687,0.385324,-7.500872,-5.180946,7.676053,-5.156047,8.340068,-7.076953,-7.286147,-6.972763,1.227336,-6.120365,-7.840912,-3.773072,4.359111,9.950971,2.329403,5.743211,6.132876,-3.525511,5.479593,8.378915,0.213417,-8.409214,-0.669273,-9.952187,-2.797252,-2.661411,-8.762086,-1.010081,-6.619286,2.804642,-5.836035,3.286908,0.515187,0.379020,-4.106669,1.131117,-6.505663,4.619766,-1.241857,7.039209,2.455635,-0.927597,-1.043287,9.263235,-7.517222,5.842847,-3.869903,-2.221948,-6.039160,-9.852313,0.585372,-4.967738,2.599978,-3.831248,-6.857233,-6.057817,6.064425,5.741151,7.133200,-2.748313,-4.205667,8.441547,-5.394496,-2.522285,0.088748,-4.151358], dtype = "float64")#candidate|7770|(1386,)|const|float64
call_7769 = relay.TupleGetItem(func_7162_call(relay.reshape(const_7770.astype('float64'), [9, 14, 11])), 0)
call_7771 = relay.TupleGetItem(func_7165_call(relay.reshape(const_7770.astype('float64'), [9, 14, 11])), 0)
output = relay.Tuple([call_7707,call_7713,call_7718,var_7719,call_7735,call_7744,call_7754,const_7755,call_7760,var_7761,call_7769,const_7770,])
output2 = relay.Tuple([call_7708,call_7714,call_7720,var_7719,call_7736,call_7745,call_7756,const_7755,call_7762,var_7761,call_7771,const_7770,])
func_7773 = relay.Function([var_7719,var_7761,], output)
mod['func_7773'] = func_7773
mod = relay.transform.InferType()(mod)
var_7774 = relay.var("var_7774", dtype = "uint64", shape = (1440,))#candidate|7774|(1440,)|var|uint64
var_7775 = relay.var("var_7775", dtype = "float64", shape = (720,))#candidate|7775|(720,)|var|float64
output = func_7773(var_7774,var_7775,)
func_7776 = relay.Function([var_7774,var_7775,], output)
mutated_mod['func_7776'] = func_7776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5204_call = mod.get_global_var('func_5204')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_7801 = relay.TupleGetItem(func_5204_call(), 0)
call_7802 = relay.TupleGetItem(func_5205_call(), 0)
output = call_7801
output2 = call_7802
func_7824 = relay.Function([], output)
mod['func_7824'] = func_7824
mod = relay.transform.InferType()(mod)
output = func_7824()
func_7825 = relay.Function([], output)
mutated_mod['func_7825'] = func_7825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3226_call = mod.get_global_var('func_3226')
func_3227_call = mutated_mod.get_global_var('func_3227')
call_7866 = func_3226_call()
call_7867 = func_3226_call()
func_3855_call = mod.get_global_var('func_3855')
func_3856_call = mutated_mod.get_global_var('func_3856')
call_7877 = relay.TupleGetItem(func_3855_call(), 2)
call_7878 = relay.TupleGetItem(func_3856_call(), 2)
uop_7880 = relay.erf(call_7877.astype('float32')) # shape=(8, 13, 4)
uop_7882 = relay.erf(call_7878.astype('float32')) # shape=(8, 13, 4)
func_609_call = mod.get_global_var('func_609')
func_614_call = mutated_mod.get_global_var('func_614')
var_7890 = relay.var("var_7890", dtype = "uint8", shape = (4576,))#candidate|7890|(4576,)|var|uint8
const_7891 = relay.const([7.773115,-5.947462,-8.387466,-3.067966,-5.497304,6.440848,5.275540,2.899329,8.897056,-7.743061,7.902447,5.797273,5.817079,-7.893081,-5.623916,2.091507,-9.468503,9.651320,0.801032,-8.789538,6.116744,-9.761201,-5.245201,-5.669853,-8.494629,1.021256,0.616155,2.105490,1.416192,8.306686,-6.049966,5.755660,-8.675711,7.646836,-3.984126,3.297579,4.397973,-1.947591,8.031540,-4.903774,5.779758,1.422390,-8.490118,0.920361,2.281982,5.166665,-1.239948,-7.874119,-2.361877,-3.645351,0.456438,-5.150695,0.322375,-4.540103,1.068452,-8.473829,0.939324,-5.939388,-0.732261,3.729986,-6.990946,-1.080084,2.501843,-2.443119,-9.716081,-1.176823,-3.243179,8.557769,5.915892,0.858880,-1.186503,1.913155,4.023363,4.531613,9.500774,4.752839,5.175461,-8.389381,-0.207438,-9.599412,3.264684,-9.684861,-4.006822,-3.253626,-8.305310,-3.059342,9.862748,-7.345565,8.651813,6.122809,-5.350820,4.936878,-8.755786,-4.527554,-6.529025,9.486710,2.297424,4.122888,8.807477,6.859527,6.799678,-9.030683,1.437837,-5.886809,-4.534933,2.203050,-5.858939,5.959450,1.641058,-8.478392,-7.249803,1.118780,2.829689,6.471582,-4.097006,-4.624176,6.252727,5.637544,5.018802,8.696090,5.235796,-6.192867,3.587960,-1.765298,0.633058,-8.867630,-8.744852,0.442299,1.126914,4.242165,0.637852,0.765762,-2.779323,7.762492,-9.870250,-5.442070,-4.531483,-8.930245,-9.977694,-9.571013,6.563541,2.256284,-5.590050,5.411085,-2.966316,-7.625394,9.346710,-6.180293,-5.905160,2.478570,-1.072130,-6.982562,3.236741,0.299927,4.871653,7.991336,-6.890949,-9.265101,-0.644149,-9.489207,-9.577682,-1.853405,1.134691,-6.943315,6.196207,-4.194845,0.479667,-0.708240,6.585498,-4.983404,0.099996,2.813222,-5.841893,-6.797229,-7.273705,0.388613,8.733700,-4.152116,-9.636682,-0.462986,-5.625575,-3.930876,9.770916,-1.352178,-7.990508,4.694515,6.201303,1.421879,0.171403,-4.688240,5.857529,-7.800077,3.750390,8.349740,5.733618,5.772777,-4.473418,5.358211,-3.762921,7.419615,-9.726714,-5.208842,4.777007,-7.297884,-3.999500,-6.732384,-4.315430,-9.859441,9.584475,-7.558858,-2.428415,3.972269,9.138761,-2.141303,-5.966944,-4.074702,7.589727,-6.912311,-9.485082,2.222852,8.751191,-0.125973,-1.365487,-3.071785,-9.047833,7.161570,-8.766167,-3.054106,1.163467,-1.496011,-0.072222,2.539349,6.098323,-8.541249,-2.263877,-1.223421,-3.855567,5.448889,-2.309197,-6.330783,-8.337736,1.011444,-2.663752,-5.820713,-8.887631,-1.558768,0.907735,-6.707931,5.668823,2.319750,-4.021080,-2.930571,-1.118601,-4.308970,3.716285,-7.938386], dtype = "float32")#candidate|7891|(256,)|const|float32
call_7889 = relay.TupleGetItem(func_609_call(relay.reshape(uop_7880.astype('uint8'), [1, 416]), relay.reshape(var_7890.astype('uint8'), [11, 416]), relay.reshape(const_7891.astype('float32'), [128, 2]), ), 7)
call_7892 = relay.TupleGetItem(func_614_call(relay.reshape(uop_7880.astype('uint8'), [1, 416]), relay.reshape(var_7890.astype('uint8'), [11, 416]), relay.reshape(const_7891.astype('float32'), [128, 2]), ), 7)
func_4717_call = mod.get_global_var('func_4717')
func_4718_call = mutated_mod.get_global_var('func_4718')
call_7943 = func_4717_call()
call_7944 = func_4717_call()
output = relay.Tuple([call_7866,uop_7880,call_7889,var_7890,const_7891,call_7943,])
output2 = relay.Tuple([call_7867,uop_7882,call_7892,var_7890,const_7891,call_7944,])
func_7952 = relay.Function([var_7890,], output)
mod['func_7952'] = func_7952
mod = relay.transform.InferType()(mod)
var_7953 = relay.var("var_7953", dtype = "uint8", shape = (4576,))#candidate|7953|(4576,)|var|uint8
output = func_7952(var_7953)
func_7954 = relay.Function([var_7953], output)
mutated_mod['func_7954'] = func_7954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4426_call = mod.get_global_var('func_4426')
func_4427_call = mutated_mod.get_global_var('func_4427')
call_7979 = relay.TupleGetItem(func_4426_call(), 2)
call_7980 = relay.TupleGetItem(func_4427_call(), 2)
func_4173_call = mod.get_global_var('func_4173')
func_4176_call = mutated_mod.get_global_var('func_4176')
var_7987 = relay.var("var_7987", dtype = "float32", shape = (585,))#candidate|7987|(585,)|var|float32
call_7986 = relay.TupleGetItem(func_4173_call(relay.reshape(var_7987.astype('float32'), [13, 9, 5])), 0)
call_7988 = relay.TupleGetItem(func_4176_call(relay.reshape(var_7987.astype('float32'), [13, 9, 5])), 0)
output = relay.Tuple([call_7979,call_7986,var_7987,])
output2 = relay.Tuple([call_7980,call_7988,var_7987,])
func_7989 = relay.Function([var_7987,], output)
mod['func_7989'] = func_7989
mod = relay.transform.InferType()(mod)
mutated_mod['func_7989'] = func_7989
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7990 = relay.var("var_7990", dtype = "float32", shape = (585,))#candidate|7990|(585,)|var|float32
func_7989_call = mutated_mod.get_global_var('func_7989')
call_7991 = func_7989_call(var_7990)
output = call_7991
func_7992 = relay.Function([var_7990], output)
mutated_mod['func_7992'] = func_7992
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8030 = relay.var("var_8030", dtype = "float32", shape = (3, 12, 14))#candidate|8030|(3, 12, 14)|var|float32
uop_8031 = relay.asin(var_8030.astype('float32')) # shape=(3, 12, 14)
bop_8036 = relay.power(uop_8031.astype('float32'), relay.reshape(var_8030.astype('float32'), relay.shape_of(uop_8031))) # shape=(3, 12, 14)
func_2163_call = mod.get_global_var('func_2163')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_8039 = relay.TupleGetItem(func_2163_call(), 3)
call_8040 = relay.TupleGetItem(func_2164_call(), 3)
output = relay.Tuple([bop_8036,call_8039,])
output2 = relay.Tuple([bop_8036,call_8040,])
func_8044 = relay.Function([var_8030,], output)
mod['func_8044'] = func_8044
mod = relay.transform.InferType()(mod)
mutated_mod['func_8044'] = func_8044
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8045 = relay.var("var_8045", dtype = "float32", shape = (3, 12, 14))#candidate|8045|(3, 12, 14)|var|float32
func_8044_call = mutated_mod.get_global_var('func_8044')
call_8046 = func_8044_call(var_8045)
output = call_8046
func_8047 = relay.Function([var_8045], output)
mutated_mod['func_8047'] = func_8047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5135_call = mod.get_global_var('func_5135')
func_5137_call = mutated_mod.get_global_var('func_5137')
call_8084 = relay.TupleGetItem(func_5135_call(), 0)
call_8085 = relay.TupleGetItem(func_5137_call(), 0)
output = call_8084
output2 = call_8085
func_8110 = relay.Function([], output)
mod['func_8110'] = func_8110
mod = relay.transform.InferType()(mod)
mutated_mod['func_8110'] = func_8110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8110_call = mutated_mod.get_global_var('func_8110')
call_8111 = func_8110_call()
output = call_8111
func_8112 = relay.Function([], output)
mutated_mod['func_8112'] = func_8112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3154_call = mod.get_global_var('func_3154')
func_3156_call = mutated_mod.get_global_var('func_3156')
call_8171 = relay.TupleGetItem(func_3154_call(), 0)
call_8172 = relay.TupleGetItem(func_3156_call(), 0)
func_1837_call = mod.get_global_var('func_1837')
func_1838_call = mutated_mod.get_global_var('func_1838')
call_8175 = relay.TupleGetItem(func_1837_call(), 2)
call_8176 = relay.TupleGetItem(func_1838_call(), 2)
output = relay.Tuple([call_8171,call_8175,])
output2 = relay.Tuple([call_8172,call_8176,])
func_8178 = relay.Function([], output)
mod['func_8178'] = func_8178
mod = relay.transform.InferType()(mod)
output = func_8178()
func_8179 = relay.Function([], output)
mutated_mod['func_8179'] = func_8179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3390_call = mod.get_global_var('func_3390')
func_3392_call = mutated_mod.get_global_var('func_3392')
call_8199 = func_3390_call()
call_8200 = func_3390_call()
func_7672_call = mod.get_global_var('func_7672')
func_7673_call = mutated_mod.get_global_var('func_7673')
call_8210 = func_7672_call()
call_8211 = func_7672_call()
output = relay.Tuple([call_8199,call_8210,])
output2 = relay.Tuple([call_8200,call_8211,])
func_8220 = relay.Function([], output)
mod['func_8220'] = func_8220
mod = relay.transform.InferType()(mod)
mutated_mod['func_8220'] = func_8220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8220_call = mutated_mod.get_global_var('func_8220')
call_8221 = func_8220_call()
output = call_8221
func_8222 = relay.Function([], output)
mutated_mod['func_8222'] = func_8222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5040_call = mod.get_global_var('func_5040')
func_5042_call = mutated_mod.get_global_var('func_5042')
call_8238 = func_5040_call()
call_8239 = func_5040_call()
output = call_8238
output2 = call_8239
func_8246 = relay.Function([], output)
mod['func_8246'] = func_8246
mod = relay.transform.InferType()(mod)
mutated_mod['func_8246'] = func_8246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8246_call = mutated_mod.get_global_var('func_8246')
call_8247 = func_8246_call()
output = call_8247
func_8248 = relay.Function([], output)
mutated_mod['func_8248'] = func_8248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5957_call = mod.get_global_var('func_5957')
func_5959_call = mutated_mod.get_global_var('func_5959')
call_8254 = relay.TupleGetItem(func_5957_call(), 0)
call_8255 = relay.TupleGetItem(func_5959_call(), 0)
output = relay.Tuple([call_8254,])
output2 = relay.Tuple([call_8255,])
func_8256 = relay.Function([], output)
mod['func_8256'] = func_8256
mod = relay.transform.InferType()(mod)
mutated_mod['func_8256'] = func_8256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8256_call = mutated_mod.get_global_var('func_8256')
call_8257 = func_8256_call()
output = call_8257
func_8258 = relay.Function([], output)
mutated_mod['func_8258'] = func_8258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1943_call = mod.get_global_var('func_1943')
func_1945_call = mutated_mod.get_global_var('func_1945')
call_8262 = func_1943_call()
call_8263 = func_1943_call()
output = call_8262
output2 = call_8263
func_8280 = relay.Function([], output)
mod['func_8280'] = func_8280
mod = relay.transform.InferType()(mod)
output = func_8280()
func_8281 = relay.Function([], output)
mutated_mod['func_8281'] = func_8281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6299_call = mod.get_global_var('func_6299')
func_6300_call = mutated_mod.get_global_var('func_6300')
call_8292 = relay.TupleGetItem(func_6299_call(), 1)
call_8293 = relay.TupleGetItem(func_6300_call(), 1)
output = relay.Tuple([call_8292,])
output2 = relay.Tuple([call_8293,])
func_8296 = relay.Function([], output)
mod['func_8296'] = func_8296
mod = relay.transform.InferType()(mod)
mutated_mod['func_8296'] = func_8296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8296_call = mutated_mod.get_global_var('func_8296')
call_8297 = func_8296_call()
output = call_8297
func_8298 = relay.Function([], output)
mutated_mod['func_8298'] = func_8298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7433_call = mod.get_global_var('func_7433')
func_7434_call = mutated_mod.get_global_var('func_7434')
call_8340 = func_7433_call()
call_8341 = func_7433_call()
output = call_8340
output2 = call_8341
func_8362 = relay.Function([], output)
mod['func_8362'] = func_8362
mod = relay.transform.InferType()(mod)
output = func_8362()
func_8363 = relay.Function([], output)
mutated_mod['func_8363'] = func_8363
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8366 = relay.var("var_8366", dtype = "float64", shape = (16, 3, 6))#candidate|8366|(16, 3, 6)|var|float64
var_8367 = relay.var("var_8367", dtype = "float64", shape = (16, 3, 6))#candidate|8367|(16, 3, 6)|var|float64
bop_8368 = relay.not_equal(var_8366.astype('bool'), relay.reshape(var_8367.astype('bool'), relay.shape_of(var_8366))) # shape=(16, 3, 6)
bop_8375 = relay.greater(var_8366.astype('bool'), relay.reshape(bop_8368.astype('bool'), relay.shape_of(var_8366))) # shape=(16, 3, 6)
output = bop_8375
output2 = bop_8375
func_8381 = relay.Function([var_8366,var_8367,], output)
mod['func_8381'] = func_8381
mod = relay.transform.InferType()(mod)
mutated_mod['func_8381'] = func_8381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8381_call = mutated_mod.get_global_var('func_8381')
var_8383 = relay.var("var_8383", dtype = "float64", shape = (16, 3, 6))#candidate|8383|(16, 3, 6)|var|float64
var_8384 = relay.var("var_8384", dtype = "float64", shape = (16, 3, 6))#candidate|8384|(16, 3, 6)|var|float64
call_8382 = func_8381_call(var_8383,var_8384,)
output = call_8382
func_8385 = relay.Function([var_8383,var_8384,], output)
mutated_mod['func_8385'] = func_8385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2011_call = mod.get_global_var('func_2011')
func_2013_call = mutated_mod.get_global_var('func_2013')
call_8423 = relay.TupleGetItem(func_2011_call(), 1)
call_8424 = relay.TupleGetItem(func_2013_call(), 1)
output = relay.Tuple([call_8423,])
output2 = relay.Tuple([call_8424,])
func_8428 = relay.Function([], output)
mod['func_8428'] = func_8428
mod = relay.transform.InferType()(mod)
output = func_8428()
func_8429 = relay.Function([], output)
mutated_mod['func_8429'] = func_8429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3293_call = mod.get_global_var('func_3293')
func_3294_call = mutated_mod.get_global_var('func_3294')
call_8466 = relay.TupleGetItem(func_3293_call(), 0)
call_8467 = relay.TupleGetItem(func_3294_call(), 0)
func_4134_call = mod.get_global_var('func_4134')
func_4136_call = mutated_mod.get_global_var('func_4136')
call_8468 = relay.TupleGetItem(func_4134_call(), 2)
call_8469 = relay.TupleGetItem(func_4136_call(), 2)
func_8362_call = mod.get_global_var('func_8362')
func_8363_call = mutated_mod.get_global_var('func_8363')
call_8492 = func_8362_call()
call_8493 = func_8362_call()
uop_8495 = relay.acosh(call_8468.astype('float32')) # shape=(8, 13, 4)
uop_8497 = relay.acosh(call_8469.astype('float32')) # shape=(8, 13, 4)
var_8501 = relay.var("var_8501", dtype = "float32", shape = (8, 13, 4))#candidate|8501|(8, 13, 4)|var|float32
bop_8502 = relay.add(call_8468.astype('uint32'), relay.reshape(var_8501.astype('uint32'), relay.shape_of(call_8468))) # shape=(8, 13, 4)
bop_8505 = relay.add(call_8469.astype('uint32'), relay.reshape(var_8501.astype('uint32'), relay.shape_of(call_8469))) # shape=(8, 13, 4)
output = relay.Tuple([call_8466,call_8492,uop_8495,bop_8502,])
output2 = relay.Tuple([call_8467,call_8493,uop_8497,bop_8505,])
func_8514 = relay.Function([var_8501,], output)
mod['func_8514'] = func_8514
mod = relay.transform.InferType()(mod)
mutated_mod['func_8514'] = func_8514
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8515 = relay.var("var_8515", dtype = "float32", shape = (8, 13, 4))#candidate|8515|(8, 13, 4)|var|float32
func_8514_call = mutated_mod.get_global_var('func_8514')
call_8516 = func_8514_call(var_8515)
output = call_8516
func_8517 = relay.Function([var_8515], output)
mutated_mod['func_8517'] = func_8517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3984_call = mod.get_global_var('func_3984')
func_3985_call = mutated_mod.get_global_var('func_3985')
call_8519 = func_3984_call()
call_8520 = func_3984_call()
output = call_8519
output2 = call_8520
func_8521 = relay.Function([], output)
mod['func_8521'] = func_8521
mod = relay.transform.InferType()(mod)
output = func_8521()
func_8522 = relay.Function([], output)
mutated_mod['func_8522'] = func_8522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8178_call = mod.get_global_var('func_8178')
func_8179_call = mutated_mod.get_global_var('func_8179')
call_8549 = relay.TupleGetItem(func_8178_call(), 0)
call_8550 = relay.TupleGetItem(func_8179_call(), 0)
uop_8556 = relay.atanh(call_8549.astype('float32')) # shape=(12, 2, 7)
uop_8558 = relay.atanh(call_8550.astype('float32')) # shape=(12, 2, 7)
func_3984_call = mod.get_global_var('func_3984')
func_3985_call = mutated_mod.get_global_var('func_3985')
call_8580 = func_3984_call()
call_8581 = func_3984_call()
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_8586 = relay.TupleGetItem(func_782_call(), 0)
call_8587 = relay.TupleGetItem(func_783_call(), 0)
output = relay.Tuple([uop_8556,call_8580,call_8586,])
output2 = relay.Tuple([uop_8558,call_8581,call_8587,])
func_8606 = relay.Function([], output)
mod['func_8606'] = func_8606
mod = relay.transform.InferType()(mod)
output = func_8606()
func_8607 = relay.Function([], output)
mutated_mod['func_8607'] = func_8607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7036_call = mod.get_global_var('func_7036')
func_7038_call = mutated_mod.get_global_var('func_7038')
call_8656 = relay.TupleGetItem(func_7036_call(), 0)
call_8657 = relay.TupleGetItem(func_7038_call(), 0)
func_4079_call = mod.get_global_var('func_4079')
func_4080_call = mutated_mod.get_global_var('func_4080')
call_8662 = relay.TupleGetItem(func_4079_call(), 0)
call_8663 = relay.TupleGetItem(func_4080_call(), 0)
func_5479_call = mod.get_global_var('func_5479')
func_5486_call = mutated_mod.get_global_var('func_5486')
const_8671 = relay.const(-3, dtype = "int16")#candidate|8671|()|const|int16
var_8672 = relay.var("var_8672", dtype = "int16", shape = (4, 312))#candidate|8672|(4, 312)|var|int16
var_8673 = relay.var("var_8673", dtype = "float64", shape = (480,))#candidate|8673|(480,)|var|float64
const_8674 = relay.const([-0.966579,-9.503376,-0.883637,1.085591,-6.847411,6.917801,2.196192,-2.097728,-4.807163,-9.828776,8.201973,-7.000679,1.286664,3.291351,9.605590,6.127091,-5.389829,-6.356947,-4.439509,-0.147681,0.884766,-5.317686,-5.923554,-1.584506,7.618914,6.244936,-5.038805,-7.202292,3.191399,-3.800388,3.539664,-5.287096,-1.129405,-7.684601,-1.641454,2.008050,-6.214604,-6.661201,-7.380670,-7.266974,0.887795,9.028773,2.099849,4.409083,5.234558,6.185658,1.687672,3.093293,-2.547266,-8.686102,-1.396619,-7.310963,4.087934,9.658586,5.770863,-8.593450,8.812073,3.985917,3.084218,-1.523761,-9.260063,2.257104,9.727845,6.273993,-3.210116,6.615521,9.183745,-9.823623,-8.774534,8.002298,0.599896,1.994061,5.245558,2.754786,7.812582,9.745142,4.856262,-1.530278,7.976151,-5.413010,7.153692,-9.737141,0.934602,-0.361250,-8.615912,8.785313,2.323664,0.683444,9.496541,3.003419,-0.756004,0.610876,-3.661673,-4.596213,5.485348,9.189467,-2.785600,-9.211513,-6.995028,-5.129048,-4.576054,-1.617179,-0.388414,-6.981028,-2.754151,-6.568780,-3.695365,-2.569372,1.736036,0.551821,3.272014,-7.664002,-2.273517,1.083925,4.874745,-9.365623,-5.063086,9.072559,-1.272670,-1.051625,2.700387,4.600315,-1.971847,-0.343956,-7.129710,4.001164,0.899468,-0.932015,-2.419742,-3.576611,1.729175,0.528403,-8.544442,-7.494799,-6.345865,2.574559,4.731640,3.997375,5.577345,-8.714006,5.933277,0.166264,4.575348,4.232647,-2.774279,6.895600,-7.913498,2.090690,7.988426,7.447760,-4.630352,7.280281,0.688214,-2.876802,1.318715,-7.109205,-4.664683,4.932486,0.710276,3.119710,-5.697398,7.181007,3.539690,5.449949,-3.193702,-3.754877,-2.494383,4.048469,-1.875240,-4.045888,-6.502964,8.609245,-5.739310,-1.452984,9.450293,6.763337,-7.702536,-1.715687,6.884705,-2.714259,-4.010961,6.367583,-5.697741,-4.298292,-9.405229,-1.484736,9.554407,2.384827,-2.631182,-1.977552,7.970349,-0.864465,-1.097054,4.936111,-1.904740,-3.817210,-9.062769,9.514468,-8.494772,4.180603,-3.630115,6.623536,7.035505,-8.425445,-2.861017,6.206910,-0.351037,2.863571,-0.904800,6.888634,-9.130198,1.055247,4.883467,6.062684,-5.075472,-6.817151,5.506166,1.787036,-7.994584,-3.747165,-8.827020,-8.715055,1.597027,3.630027,-8.593940,0.841146,-3.145548,1.766798,1.714770,5.573313,8.021391,7.461528,9.466565,-7.430347,-0.480206,-6.373651,-0.707129,5.966020,-5.927293,-7.017543,8.247803,1.729709,-6.321416,1.415960,-3.500076,-7.835929,-0.565460,-0.009843,-1.348352,1.361308,7.663219,5.979323,-6.897833,-7.252369,5.969622,0.775407], dtype = "float32")#candidate|8674|(256,)|const|float32
call_8670 = relay.TupleGetItem(func_5479_call(relay.reshape(call_8662.astype('float32'), [12, 2, 7]), relay.reshape(const_8671.astype('int16'), []), relay.reshape(var_8672.astype('int16'), [1248,]), relay.reshape(var_8673.astype('float64'), [480,]), relay.reshape(const_8674.astype('float32'), [4, 64]), ), 8)
call_8675 = relay.TupleGetItem(func_5486_call(relay.reshape(call_8662.astype('float32'), [12, 2, 7]), relay.reshape(const_8671.astype('int16'), []), relay.reshape(var_8672.astype('int16'), [1248,]), relay.reshape(var_8673.astype('float64'), [480,]), relay.reshape(const_8674.astype('float32'), [4, 64]), ), 8)
func_7570_call = mod.get_global_var('func_7570')
func_7572_call = mutated_mod.get_global_var('func_7572')
call_8677 = relay.TupleGetItem(func_7570_call(), 3)
call_8678 = relay.TupleGetItem(func_7572_call(), 3)
uop_8696 = relay.asinh(call_8670.astype('float64')) # shape=(4, 64)
uop_8698 = relay.asinh(call_8675.astype('float64')) # shape=(4, 64)
uop_8703 = relay.log(call_8670.astype('float64')) # shape=(4, 64)
uop_8705 = relay.log(call_8675.astype('float64')) # shape=(4, 64)
func_2163_call = mod.get_global_var('func_2163')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_8710 = relay.TupleGetItem(func_2163_call(), 2)
call_8711 = relay.TupleGetItem(func_2164_call(), 2)
var_8725 = relay.var("var_8725", dtype = "float64", shape = (4, 64))#candidate|8725|(4, 64)|var|float64
bop_8726 = relay.less_equal(uop_8696.astype('bool'), relay.reshape(var_8725.astype('bool'), relay.shape_of(uop_8696))) # shape=(4, 64)
bop_8729 = relay.less_equal(uop_8698.astype('bool'), relay.reshape(var_8725.astype('bool'), relay.shape_of(uop_8698))) # shape=(4, 64)
output = relay.Tuple([call_8656,call_8662,const_8671,var_8672,var_8673,const_8674,call_8677,uop_8703,call_8710,bop_8726,])
output2 = relay.Tuple([call_8657,call_8663,const_8671,var_8672,var_8673,const_8674,call_8678,uop_8705,call_8711,bop_8729,])
func_8751 = relay.Function([var_8672,var_8673,var_8725,], output)
mod['func_8751'] = func_8751
mod = relay.transform.InferType()(mod)
var_8752 = relay.var("var_8752", dtype = "int16", shape = (4, 312))#candidate|8752|(4, 312)|var|int16
var_8753 = relay.var("var_8753", dtype = "float64", shape = (480,))#candidate|8753|(480,)|var|float64
var_8754 = relay.var("var_8754", dtype = "float64", shape = (4, 64))#candidate|8754|(4, 64)|var|float64
output = func_8751(var_8752,var_8753,var_8754,)
func_8755 = relay.Function([var_8752,var_8753,var_8754,], output)
mutated_mod['func_8755'] = func_8755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4253_call = mod.get_global_var('func_4253')
func_4255_call = mutated_mod.get_global_var('func_4255')
call_8760 = func_4253_call()
call_8761 = func_4253_call()
output = relay.Tuple([call_8760,])
output2 = relay.Tuple([call_8761,])
func_8772 = relay.Function([], output)
mod['func_8772'] = func_8772
mod = relay.transform.InferType()(mod)
output = func_8772()
func_8773 = relay.Function([], output)
mutated_mod['func_8773'] = func_8773
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8814 = relay.var("var_8814", dtype = "float64", shape = (16, 11, 4))#candidate|8814|(16, 11, 4)|var|float64
var_8815 = relay.var("var_8815", dtype = "float64", shape = (16, 11, 4))#candidate|8815|(16, 11, 4)|var|float64
bop_8816 = relay.minimum(var_8814.astype('float64'), relay.reshape(var_8815.astype('float64'), relay.shape_of(var_8814))) # shape=(16, 11, 4)
func_358_call = mod.get_global_var('func_358')
func_361_call = mutated_mod.get_global_var('func_361')
const_8820 = relay.const([0.640220,-0.556398,-0.485205,3.869729,-7.159186,3.675263,5.812604,-7.309707,-6.769717,2.088920,2.375644,-3.258484,3.316907,-8.508345,-6.549556,-1.104649,4.045858,-1.089088,-0.400617,1.320825,-8.110372,7.621171,-2.343754,0.872494,-2.083405,-0.593430,8.966344,9.491188,0.419009,-6.076492,4.304664,4.208800,7.892387,-9.386438,8.476923,-4.557933,-4.450474,-2.040598,0.867757,3.992703,-2.672684,2.486555,-4.670739,-8.247285,-9.965190,0.222400,9.108940,5.901221,-7.224484,7.075132,0.640289,8.537471,2.743801,-1.818066,-9.666357,-7.826291,1.414110,-5.067200,-4.164725,-2.786125,0.159977,-6.012650,-7.767375,2.366762,1.180581,3.408179,-2.631343,-7.139954,-2.786424,6.389328,-4.269323,7.451732,5.829811,6.244312,-6.783734,9.064558,1.224134,-7.781256,2.364986,-4.213728,-4.112776,5.896579,5.664245,-6.582259,-0.314903,-2.255681,8.559505,-6.246373,4.845067,-8.075916,3.488714,-1.739769,8.331862,7.461052,-2.905053,9.336726,7.451795,-4.867237,-4.826926,-9.850541,-0.125565,4.655934,-6.887474,-2.302410,7.760437,6.055373,-8.871840,6.807487,-9.067476,-1.892460,4.030227,-6.751399,-9.746619,5.891550,2.882093,7.500800,-3.863825,-4.328441,2.405887,-7.910615,0.406300,6.537213,3.402965,-1.619157,4.669095,8.466892,-0.986689,7.485621,-6.672552,-5.967071,-8.099983,2.650955,-8.606992,4.012315,-7.901657,2.368896,6.658452,-0.872325,6.380059,7.984047,7.740657,3.908352,-8.467149,3.196881,5.060785,-1.609588,3.750202,-6.775807,4.676833,7.919096,-5.617839,-5.278519,-5.503603,-2.846323,7.586900,-4.617922,-6.542790,-6.129477,3.180561,1.326578,7.134024,-8.695946,1.691641,8.194100,3.338793,5.910798,2.126430,9.074612,-3.431838,0.803671,1.870006,-1.493556,-9.392084,-7.140602,-6.135011,-0.207736,-2.452452,5.931059,-0.956150,-0.191811,6.545915,9.844253,7.417597,-6.308301,-9.277003,4.564849,-0.651237,-6.717150,5.092873,-7.760937,-9.995692,2.640441,2.789083,4.636412,4.323103,7.239933,1.603443,2.227624,-0.994060,-3.843317,-4.322998,-5.871751,6.146584,7.788166,-3.274354,0.156295,-6.315194,3.262003,0.347599,3.785434,-7.351348,0.702729,9.558152,1.907977,4.538479,6.205926,0.609319,-7.257015,-6.577853,9.376869,2.285168,6.258243,-6.992658,5.181537,0.710172,-2.669791,-6.986140,5.370446,4.415785,7.142971,-5.729670,-4.052553,-9.845143,6.765682,-6.580397,2.893266,3.715846,7.822336,5.503821,2.811008,-5.807784,4.149685,6.253173,-3.340867,5.384657,3.697342,-4.763546,5.687210,-0.827027,7.389191,-7.452120,-3.810205,-1.754320,8.117667,1.501336,-5.044999,-2.165043,-1.808126,8.422092,-5.015409,-0.153989,-0.568331,5.644327,5.504503,-5.319155,-5.533814,-3.438427,-8.359167,3.622502,-6.596484,-0.568277,-0.134317,-6.306634,8.840260,0.683572,-0.704132,6.864957,5.589022,1.457538,8.674940,3.902432,-7.064086,-0.177651,-1.636172,-6.745674,-0.413926,-4.913593,8.839288,4.626935,-3.535367,1.579267,-2.721419,8.303827,1.550858,6.617181,8.403584,2.258148,-7.463440,-7.309474,4.219104,9.122490,-0.948657,-3.718354,4.386400,-5.998734,-4.630297,-4.433161,-7.781935,-2.828802,-5.519030,-6.496643,4.302166,2.283768,-1.318476,-3.048573,-8.449797,4.403163,6.889917,5.038018,-8.477800,-7.743215,0.815453,1.733421,9.039463,2.726445,1.239597,8.212322,0.622572,-3.740252,-0.419058,4.863600,7.545239,0.681169,-5.022614,9.626675,-5.051402,-0.466520,-4.012585,-0.866977,3.925436,-1.834818,6.022719,1.336405,-0.305122,-3.650714,4.305850,-6.755738,7.700666,0.539232,-9.762235,-7.913902,5.470111,-0.046818,-5.723028,0.357506,-3.718213,3.994138,6.771431,7.007744,-9.188200,-3.652643,4.987451,-7.903211,4.505362,5.843824,-1.058218,-3.143926,-4.747791,-1.812404,4.465896,-7.665060,1.071395,-3.737801,6.421111,-7.407405,4.220987,4.646213,5.485164,7.102329,6.228832,-7.760864,-9.204708,4.305482,7.045118,-7.334777,0.851124,9.412909,-9.564953,2.923183,8.702398,0.597137,5.376922,0.090832,9.356049,4.019723,0.077915,-1.683967,-3.796037,-6.219246,5.903178,2.426168,-6.515072,4.562571,-6.730736,-3.609979,1.323051,-9.605695,-5.569931,2.187852,8.593474,-8.294103,1.237933,-0.451611,5.025196,4.872204,5.673312,1.647579,0.144869,-6.988382,-9.569335,3.991278,0.045505,-0.056382,-8.314894,6.903024,-9.161209,-8.373380,-2.583003,7.066370,-8.693058,7.566826,0.333944,4.469686,3.129594,-4.032285,-4.582732,5.007777,-8.506912,9.475995,-0.066165,-6.687211,-5.168047,-5.896457,9.331132,-3.274386,-2.975978,-3.804001,4.389745,8.473910,8.433194,-0.545862,9.855233,4.199211,6.693631,-6.172468,4.460173,-4.697865,-6.029548,3.814866,-5.404291,5.206800,6.807208,3.526069,2.678891,1.646649,-4.168716,-8.903545,-5.345310,4.158328,-8.147988,9.370355,-0.956467,9.380206,-1.201243,1.706173,1.067087,1.857199,-7.357703,9.142651,0.429067], dtype = "float64")#candidate|8820|(480,)|const|float64
call_8819 = relay.TupleGetItem(func_358_call(relay.reshape(const_8820.astype('float64'), [480,])), 3)
call_8821 = relay.TupleGetItem(func_361_call(relay.reshape(const_8820.astype('float64'), [480,])), 3)
func_8521_call = mod.get_global_var('func_8521')
func_8522_call = mutated_mod.get_global_var('func_8522')
call_8822 = func_8521_call()
call_8823 = func_8521_call()
func_5040_call = mod.get_global_var('func_5040')
func_5042_call = mutated_mod.get_global_var('func_5042')
call_8824 = func_5040_call()
call_8825 = func_5040_call()
const_8853 = relay.const([[[-4.649422,-9.435450,5.330414,0.505793],[7.464658,-9.722538,-4.802065,-9.587707],[-0.198590,-1.857863,-7.554510,-4.327087],[1.653009,-4.239642,2.244373,7.182369],[-8.897079,7.946255,-6.392480,-2.128494],[7.634945,2.378696,5.124475,-8.432601],[8.417206,-6.575293,6.030306,2.175318],[4.102294,-0.643723,4.870541,-7.187464],[3.778724,-2.535932,-4.277719,-4.772110],[6.165885,3.470275,4.719335,-7.009953],[3.415582,-1.921724,4.773516,7.025475]],[[-5.646293,-9.413837,-2.557387,7.394040],[-9.130918,7.223824,-8.968517,-5.085545],[4.007057,-4.973887,-9.734817,-4.921557],[3.884144,-8.104334,-6.616744,2.571468],[3.186606,-9.700235,7.551213,-6.433060],[6.603832,-6.932545,6.431826,3.126555],[8.156814,8.525583,3.585629,6.062660],[1.358868,4.764847,0.633319,-0.454591],[-4.245986,-6.587714,-6.389767,-9.845852],[6.170823,8.165607,9.737367,0.906813],[-5.146824,-1.130779,-6.811619,-0.032976]],[[-3.186196,5.699808,6.501790,-7.480614],[6.673167,4.047435,7.206440,9.452877],[-8.946243,4.220179,-1.363871,-8.040883],[-3.938741,-4.031216,-7.184367,-0.370662],[-5.559494,7.950937,4.423137,-6.639768],[-1.647221,-3.476427,8.869557,-7.483151],[-0.044619,6.409470,2.524933,9.813431],[2.933916,-2.650717,-0.143880,-3.183330],[3.530696,-3.583363,1.815237,4.865733],[-4.521078,-0.685472,8.125403,-9.919274],[-5.856220,-8.627611,3.700376,5.250592]],[[2.154986,8.817788,-1.716599,4.482257],[1.084536,-9.958957,-0.022584,-7.819670],[7.858675,-9.512372,-5.594702,-6.344913],[-7.088119,-9.385058,-0.010182,-7.862658],[5.912050,-7.791497,3.650695,1.752376],[5.038153,-3.046215,4.408715,5.608148],[3.380194,-4.370432,-0.145132,-8.811954],[4.998686,-7.554567,6.735513,-6.124065],[-2.866020,-0.836026,-4.072818,-1.584928],[-4.322395,0.914881,-3.442943,-5.939828],[-1.141235,2.818569,-2.723387,6.169715]],[[-4.074266,5.523503,4.767061,-7.705309],[-5.763293,1.559230,0.728657,2.589832],[-5.867828,3.291845,2.112132,-0.983923],[-4.757369,-4.807750,-8.556782,1.458323],[6.976818,-2.063896,-2.992709,3.010469],[9.102780,9.670337,-5.282081,-4.197791],[1.538427,8.938028,-9.954156,-3.598538],[9.870800,3.892704,-6.891978,-3.331630],[9.121877,-9.539379,-1.742435,1.909484],[7.045638,-5.241688,1.218345,-4.340558],[-2.633889,8.159193,-3.612668,-8.140041]],[[-3.177374,3.853740,-3.178949,-5.638785],[-3.574983,2.618104,-0.799684,-4.829709],[9.151849,-2.192603,-1.431915,7.149441],[-2.130499,3.034843,-6.782572,2.470620],[7.788718,4.266966,-5.285363,4.401754],[8.995005,9.105681,9.553612,1.295461],[-2.610145,0.547672,-3.566838,-8.325907],[7.051604,3.939479,2.291011,-3.512060],[2.429736,-1.834619,-3.538494,-5.529975],[-1.068806,6.203217,-9.580084,-1.618408],[-5.690370,4.255868,-3.880256,-1.491430]],[[7.193310,4.350340,-1.608692,7.226779],[5.790711,0.823538,2.171086,6.538558],[-0.395141,-0.762283,8.276297,4.457806],[-0.435947,3.339688,-3.347686,9.070758],[3.421118,-5.189217,-4.169486,-5.840178],[7.830732,8.809212,3.641030,-0.893861],[-7.900728,-0.770516,1.501965,0.095323],[-2.970344,-6.501311,-5.453175,-7.105616],[-8.356015,1.702772,-8.690852,1.525819],[-8.799795,1.976961,4.431801,3.702011],[-2.179659,-8.055798,8.377507,6.149269]],[[-5.025705,1.674272,2.839342,-5.895735],[-5.108346,6.941934,6.508351,5.541966],[0.738079,-8.188297,-6.333996,-9.191705],[1.820519,4.174247,9.041419,9.977003],[-2.710624,-9.323264,-0.881750,-8.282864],[3.254619,-2.849990,-5.681896,-5.444616],[-4.519691,-1.332520,-0.920167,2.547790],[3.132371,-4.743615,9.540396,-9.892209],[-3.496480,-3.596505,-5.958788,-7.297462],[-3.655038,-4.570015,-3.443120,-0.950060],[5.285017,1.428980,-8.379231,-0.098293]],[[5.341686,-6.277503,-5.920806,4.517473],[0.158688,3.959743,-4.324193,5.550171],[-5.160536,4.473412,-5.830294,1.710810],[-8.746711,8.643328,6.948949,8.388662],[1.583591,-4.813042,-8.915279,-5.443492],[7.755758,0.292304,8.600919,-5.056320],[6.657513,-8.532717,0.624037,3.247720],[2.710548,-2.525915,-4.887784,1.298170],[9.069784,7.114622,0.769493,-7.615489],[-6.948228,-1.004086,-8.045134,8.730829],[-6.805103,-4.648436,-4.711261,-0.018634]],[[-6.770408,-3.050183,-5.371634,-5.434329],[9.229760,3.970575,-4.412566,4.689353],[-5.475162,-9.712953,-7.042563,-4.843996],[-8.495141,7.214957,-3.047055,-7.452984],[-8.831382,-4.051933,-9.688717,8.730119],[-1.753107,3.358430,-4.454772,4.125726],[-9.524621,0.673263,-8.249528,-8.942624],[-1.606490,5.536787,4.228651,-0.739077],[-9.867884,-2.155633,9.997657,5.986810],[-6.880859,-8.323873,4.921738,8.431659],[-8.293596,3.696033,-9.307280,3.836654]],[[2.387033,-3.351534,-0.473115,-1.271131],[9.716108,6.707222,-3.157319,-6.192062],[6.465163,5.182081,2.313885,6.015410],[-6.678501,-2.314677,-9.001984,0.217215],[-5.843569,-1.585193,-8.939704,2.170105],[4.051481,4.367170,5.887463,-9.954165],[-1.123505,-9.800422,4.755552,8.410955],[-1.744191,-4.466232,1.433713,-5.398641],[4.418376,-5.161015,4.925315,5.267018],[0.661915,9.309159,8.851667,0.026493],[6.094390,5.464024,4.986194,-7.950254]],[[-6.011425,-1.900669,6.153897,0.064688],[8.026760,-4.419368,3.249896,6.836026],[-9.727192,-4.065090,7.689124,-4.976564],[3.667837,5.420398,-6.380182,-8.337411],[-5.572272,5.442045,8.490598,1.244424],[-2.045034,5.599371,4.056789,-7.153960],[1.399011,6.728891,7.918209,-4.044627],[1.385432,2.876134,7.790289,-1.524802],[2.169463,4.787395,-5.690564,9.481413],[5.342335,4.259838,-8.573667,-2.497474],[-1.075830,-4.464223,5.509778,-0.239486]],[[-9.208475,3.498379,5.932902,4.499817],[2.133787,5.224349,4.044821,-6.297979],[2.576406,-7.301622,-0.859389,-3.661489],[-3.934181,-8.742276,4.239819,8.544030],[-0.429933,1.505295,-3.972642,-8.162414],[-4.727989,-7.544144,5.674718,-3.084346],[-3.150298,-0.354857,1.328564,6.345799],[6.485429,-3.385510,-0.951941,-5.541502],[-9.267826,-6.693566,-7.982718,-8.767616],[-4.925998,0.456796,3.267000,-3.495585],[-5.237009,-5.645442,8.588376,4.630761]],[[5.154736,5.870670,3.449123,5.319337],[-0.831757,3.959722,-4.377194,4.377131],[-7.642118,-1.918826,-7.126877,6.279250],[6.236004,-0.399564,7.253293,0.753668],[8.335727,-8.412431,-3.652630,-4.925624],[9.947508,-0.672824,6.810331,-0.690273],[-2.276623,-8.087906,0.641235,7.790922],[8.173766,-6.605796,0.608119,-4.834863],[-2.926655,-3.267320,-6.190988,4.952467],[-0.028534,5.745652,5.375068,5.834361],[4.738068,-8.659004,3.937550,5.676147]],[[-6.462873,8.809465,-6.958023,-2.246001],[-0.921090,4.370094,-4.910285,-9.703798],[-2.226325,-5.142141,3.978597,7.602217],[8.307431,6.428818,1.984517,-9.850934],[-2.534800,-0.342641,6.068538,-8.043023],[8.878685,-6.992955,-1.684784,-8.833887],[-6.664331,3.954881,-3.892291,-4.472506],[-5.830696,-7.482313,5.602309,8.615821],[-9.429798,-4.327602,4.578187,3.083203],[-5.677389,-1.218631,-7.260693,-0.850726],[7.683597,-8.160075,-9.981028,-5.193511]],[[-0.881466,3.868591,3.499515,-8.286650],[-5.288662,0.430559,7.568530,-9.653459],[-4.575596,-9.242798,3.198492,1.965310],[-9.478046,-0.150911,2.645876,-6.875250],[9.969736,7.806178,-7.132925,-5.429936],[-5.076624,-5.851105,-3.474732,8.132354],[3.033154,6.103734,-8.692262,-7.437833],[-6.155584,-4.722068,9.166932,2.860836],[-3.253665,2.547320,-5.724053,4.532389],[2.016774,-3.651476,-9.093554,-2.049240],[-4.030603,-5.437764,-8.745828,7.384163]]], dtype = "float64")#candidate|8853|(16, 11, 4)|const|float64
bop_8854 = relay.floor_mod(var_8814.astype('float32'), relay.reshape(const_8853.astype('float32'), relay.shape_of(var_8814))) # shape=(16, 11, 4)
output = relay.Tuple([bop_8816,call_8819,const_8820,call_8822,call_8824,bop_8854,])
output2 = relay.Tuple([bop_8816,call_8821,const_8820,call_8823,call_8825,bop_8854,])
F = relay.Function([var_8814,var_8815,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8814,var_8815,], output2)
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
