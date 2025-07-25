import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_282 = relay.const([[[2.528685],[-8.459351],[2.426763]]], dtype = "float64")#candidate|282|(1, 3, 1)|const|float64
uop_283 = relay.acosh(const_282.astype('float64')) # shape=(1, 3, 1)
uop_288 = relay.sin(const_282.astype('float64')) # shape=(1, 3, 1)
bop_293 = relay.mod(const_282.astype('float32'), relay.reshape(uop_283.astype('float32'), relay.shape_of(const_282))) # shape=(1, 3, 1)
output = relay.Tuple([uop_288,bop_293,])
output2 = relay.Tuple([uop_288,bop_293,])
func_296 = relay.Function([], output)
mod['func_296'] = func_296
mod = relay.transform.InferType()(mod)
output = func_296()
func_297 = relay.Function([], output)
mutated_mod['func_297'] = func_297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_324 = relay.TupleGetItem(func_296_call(), 1)
call_325 = relay.TupleGetItem(func_297_call(), 1)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_339 = relay.TupleGetItem(func_296_call(), 0)
call_340 = relay.TupleGetItem(func_297_call(), 0)
output = relay.Tuple([call_324,call_339,])
output2 = relay.Tuple([call_325,call_340,])
func_344 = relay.Function([], output)
mod['func_344'] = func_344
mod = relay.transform.InferType()(mod)
output = func_344()
func_345 = relay.Function([], output)
mutated_mod['func_345'] = func_345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_370 = relay.TupleGetItem(func_296_call(), 0)
call_371 = relay.TupleGetItem(func_297_call(), 0)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_390 = relay.TupleGetItem(func_296_call(), 0)
call_391 = relay.TupleGetItem(func_297_call(), 0)
output = relay.Tuple([call_370,call_390,])
output2 = relay.Tuple([call_371,call_391,])
func_393 = relay.Function([], output)
mod['func_393'] = func_393
mod = relay.transform.InferType()(mod)
output = func_393()
func_394 = relay.Function([], output)
mutated_mod['func_394'] = func_394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_423 = relay.TupleGetItem(func_296_call(), 1)
call_424 = relay.TupleGetItem(func_297_call(), 1)
func_344_call = mod.get_global_var('func_344')
func_345_call = mutated_mod.get_global_var('func_345')
call_426 = relay.TupleGetItem(func_344_call(), 1)
call_427 = relay.TupleGetItem(func_345_call(), 1)
uop_432 = relay.asinh(call_426.astype('float32')) # shape=(1, 3, 1)
uop_434 = relay.asinh(call_427.astype('float32')) # shape=(1, 3, 1)
bop_452 = relay.add(uop_432.astype('uint64'), relay.reshape(call_426.astype('uint64'), relay.shape_of(uop_432))) # shape=(1, 3, 1)
bop_455 = relay.add(uop_434.astype('uint64'), relay.reshape(call_427.astype('uint64'), relay.shape_of(uop_434))) # shape=(1, 3, 1)
func_393_call = mod.get_global_var('func_393')
func_394_call = mutated_mod.get_global_var('func_394')
call_456 = relay.TupleGetItem(func_393_call(), 1)
call_457 = relay.TupleGetItem(func_394_call(), 1)
bop_458 = relay.not_equal(uop_432.astype('bool'), relay.reshape(call_426.astype('bool'), relay.shape_of(uop_432))) # shape=(1, 3, 1)
bop_461 = relay.not_equal(uop_434.astype('bool'), relay.reshape(call_427.astype('bool'), relay.shape_of(uop_434))) # shape=(1, 3, 1)
uop_463 = relay.sigmoid(call_423.astype('float64')) # shape=(1, 3, 1)
uop_465 = relay.sigmoid(call_424.astype('float64')) # shape=(1, 3, 1)
output = relay.Tuple([bop_452,call_456,bop_458,uop_463,])
output2 = relay.Tuple([bop_455,call_457,bop_461,uop_465,])
func_468 = relay.Function([], output)
mod['func_468'] = func_468
mod = relay.transform.InferType()(mod)
mutated_mod['func_468'] = func_468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_468_call = mutated_mod.get_global_var('func_468')
call_469 = func_468_call()
output = call_469
func_470 = relay.Function([], output)
mutated_mod['func_470'] = func_470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_502 = relay.TupleGetItem(func_468_call(), 0)
call_503 = relay.TupleGetItem(func_470_call(), 0)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_504 = relay.TupleGetItem(func_468_call(), 0)
call_505 = relay.TupleGetItem(func_470_call(), 0)
output = relay.Tuple([call_502,call_504,])
output2 = relay.Tuple([call_503,call_505,])
func_506 = relay.Function([], output)
mod['func_506'] = func_506
mod = relay.transform.InferType()(mod)
output = func_506()
func_507 = relay.Function([], output)
mutated_mod['func_507'] = func_507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_344_call = mod.get_global_var('func_344')
func_345_call = mutated_mod.get_global_var('func_345')
call_525 = relay.TupleGetItem(func_344_call(), 1)
call_526 = relay.TupleGetItem(func_345_call(), 1)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_534 = relay.TupleGetItem(func_296_call(), 0)
call_535 = relay.TupleGetItem(func_297_call(), 0)
output = relay.Tuple([call_525,call_534,])
output2 = relay.Tuple([call_526,call_535,])
func_541 = relay.Function([], output)
mod['func_541'] = func_541
mod = relay.transform.InferType()(mod)
output = func_541()
func_542 = relay.Function([], output)
mutated_mod['func_542'] = func_542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_556 = relay.TupleGetItem(func_506_call(), 1)
call_557 = relay.TupleGetItem(func_507_call(), 1)
func_393_call = mod.get_global_var('func_393')
func_394_call = mutated_mod.get_global_var('func_394')
call_566 = relay.TupleGetItem(func_393_call(), 0)
call_567 = relay.TupleGetItem(func_394_call(), 0)
output = relay.Tuple([call_556,call_566,])
output2 = relay.Tuple([call_557,call_567,])
func_585 = relay.Function([], output)
mod['func_585'] = func_585
mod = relay.transform.InferType()(mod)
mutated_mod['func_585'] = func_585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mutated_mod.get_global_var('func_585')
call_586 = func_585_call()
output = call_586
func_587 = relay.Function([], output)
mutated_mod['func_587'] = func_587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_602 = relay.TupleGetItem(func_296_call(), 0)
call_603 = relay.TupleGetItem(func_297_call(), 0)
output = relay.Tuple([call_602,])
output2 = relay.Tuple([call_603,])
func_604 = relay.Function([], output)
mod['func_604'] = func_604
mod = relay.transform.InferType()(mod)
output = func_604()
func_605 = relay.Function([], output)
mutated_mod['func_605'] = func_605
mutated_mod = relay.transform.InferType()(mutated_mod)
const_688 = relay.const([[[-7.346358,-9.997324,5.365241,9.707896,-0.138123,-4.127206,-3.500182,-8.818838,5.013713,-8.746115],[4.157027,-3.265680,-6.421932,-3.750347,5.209050,-3.562511,2.676587,0.011979,-1.059209,-6.224521],[8.118126,4.026755,-1.129440,-5.328723,-3.644913,-2.378436,7.886167,-6.746659,-2.189812,-9.713396],[3.296316,-7.370471,-2.955567,6.480273,-8.223395,0.661235,5.289818,7.640309,-1.652857,4.427925],[5.844582,-1.614609,1.568901,-1.556196,2.927327,7.836826,-4.395306,-7.480010,0.543991,3.005255],[3.866411,1.020962,-2.854327,-5.355556,-6.276681,7.887833,-3.026644,5.089279,0.154250,5.568334],[-4.645307,5.293437,-5.386333,0.732259,0.883286,2.188165,7.446455,5.021044,-5.474597,6.880129],[-6.727587,-5.013803,-1.946209,-0.126712,1.085034,9.562878,-6.353900,-7.036853,-2.913983,-0.753830],[5.203590,-3.591643,-2.359229,-0.294602,-1.382494,7.891362,-0.869615,5.549328,8.098899,-7.432289]],[[5.384513,0.151000,-1.877891,4.008953,4.843396,9.966479,3.519087,-3.685243,0.582858,-4.014194],[-5.366170,-8.966975,5.710645,2.987271,0.820063,-8.341807,6.455217,-1.357657,0.639689,-0.625459],[4.827430,9.603427,-8.701207,-5.899921,-1.447403,3.702771,1.849663,-4.753448,3.633880,6.188448],[7.695712,8.720255,7.877684,5.361080,7.324288,-1.746234,6.676201,-3.585463,5.917554,6.545715],[7.815112,-0.952353,2.827371,-8.337731,-6.788341,8.889434,7.485394,1.102629,6.001732,8.106017],[-6.168505,0.712110,-0.705815,9.349016,0.327211,7.640675,0.776456,5.610197,-8.692390,0.137299],[3.190424,9.229838,-0.577866,-1.087935,4.909737,-4.412328,9.399201,3.151324,6.699377,4.896992],[7.632024,-8.423465,-3.877539,5.724641,3.438639,9.922563,-2.892566,5.102739,1.166963,-1.871141],[6.219671,6.050531,-0.069914,-8.500126,6.677866,-0.011615,0.561986,-5.305427,-9.295875,-9.058260]],[[-6.328621,8.656836,-4.708873,7.546303,-9.960961,-2.560025,4.763938,-4.307738,-0.462869,7.691639],[-6.206767,9.159639,-2.293759,0.241872,7.759269,-2.082362,4.224286,-9.749739,-4.598448,-5.296794],[7.659973,3.583654,-4.527476,0.130812,-4.089102,-8.402082,-1.746912,-9.025448,5.934017,-1.926525],[-4.415425,3.959081,-7.602251,0.629378,2.650937,4.340044,8.167627,7.118291,-3.397381,-2.788899],[-6.239520,9.926369,-3.948810,9.081722,1.328349,3.978708,4.018174,7.533415,-7.550014,-8.435315],[-7.813716,9.363422,-4.984370,9.663894,7.523242,-4.503487,2.393806,-3.778343,2.125487,6.255659],[3.983645,-7.187440,4.221835,-4.338976,1.374046,-5.032193,-6.651391,1.853162,-3.948142,0.726089],[-5.838390,5.590423,2.057333,-1.518521,-0.844906,7.486836,-4.852371,-8.456913,-1.048278,6.766375],[1.267773,5.512337,7.786197,7.164747,-9.692340,4.358620,-5.402474,-8.534792,4.860607,-5.799595]],[[-2.631754,2.245051,-5.871517,2.120969,8.116287,-2.080053,-5.122399,-3.924984,-9.351023,0.195050],[3.293437,8.584221,-2.886104,5.723921,-0.075157,9.520129,-3.069380,5.679467,-2.542967,4.939035],[-7.006271,-6.714848,7.252185,-1.796359,-1.400447,-4.564097,9.145340,7.795708,8.395914,8.103995],[8.059030,0.604605,0.893513,-3.084915,7.456630,4.314473,6.722154,-5.428332,7.133932,-6.581966],[-2.512116,0.862611,-9.239369,3.971271,2.357498,-7.646961,1.193951,-2.735999,-9.124583,-0.870976],[-3.436781,6.694266,-1.701948,2.397876,1.520522,1.231669,-0.491695,4.129343,-8.510555,2.801683],[5.620581,-2.681453,9.964213,2.812452,0.682154,5.675074,-5.436308,1.871277,-6.816489,-6.582555],[-2.901087,5.075323,-0.485618,3.465231,-7.347251,-9.856697,-5.299868,-6.394004,-6.745552,-4.868915],[-1.457024,4.096332,-0.983748,9.847340,9.676198,-4.072107,3.450424,7.585753,-5.559527,-6.776743]],[[5.475529,-1.531199,8.883625,7.346060,1.427244,3.541470,9.870611,-2.325777,3.122947,-9.512590],[2.238174,-5.676781,-1.289566,-9.703150,2.805379,7.110963,9.531629,-7.545306,6.637654,-9.939306],[7.181623,-2.498431,3.677010,9.009421,-6.169711,6.815878,-1.555540,-4.031901,4.836053,-1.425290],[-4.039680,6.200439,4.171091,-9.674310,7.254998,2.186068,9.506389,4.886466,-1.325409,3.964219],[-6.676194,-6.229099,5.094507,-6.915336,5.137235,4.341155,-3.103427,-5.628276,-4.003959,-1.448218],[4.809856,3.537502,1.215383,3.389191,9.145866,-3.134649,-7.709349,-8.443478,-6.321167,-7.968804],[3.320598,5.729030,9.058464,-0.702200,-7.509425,8.473801,-4.003307,-9.655988,-4.605782,-3.481580],[2.026021,4.220786,3.008003,7.178544,-4.542549,-3.513941,0.669333,-4.071041,3.668424,-8.758291],[7.568050,9.812678,-9.780885,-4.947291,-8.165644,-8.787341,7.435313,8.629153,-1.007755,-5.687808]],[[-9.816636,-7.415478,-2.980758,-9.117417,0.146277,-5.200267,9.690334,3.565698,2.581960,-9.784711],[-6.871055,4.699484,-0.646550,-7.689487,2.424459,-6.974085,7.816642,0.889470,4.937594,1.357519],[7.405316,6.230501,-0.954930,-7.865829,-0.470080,7.551013,-9.237854,7.738359,7.661541,5.938757],[-2.617467,-3.241050,-5.602148,-1.910167,-6.820478,9.386539,0.124458,-8.804891,8.072840,3.240123],[9.574952,-4.076906,-4.754827,-2.158464,6.179879,-8.064009,7.921788,-2.690334,6.191010,3.407693],[-9.116760,5.541025,-6.128761,2.640896,-5.682043,3.436842,8.107219,9.723889,0.318537,5.412042],[9.628877,0.007397,3.933415,9.288384,-8.372668,-9.272460,0.410631,-4.743698,2.267538,5.226634],[-3.533458,8.249236,-7.032029,7.444464,-4.603835,-7.562571,6.557723,7.005599,4.521941,7.980473],[7.224564,1.934106,8.807336,-7.731106,0.165533,-8.274102,4.845937,-3.058500,0.351858,8.790837]],[[-8.795220,7.153721,7.517865,-6.677825,6.431627,-6.373163,6.194607,6.976715,5.250044,5.169906],[4.328134,7.328161,2.174891,-9.271246,0.842555,6.005625,-9.600667,2.627967,2.055716,-0.916898],[5.902170,3.956162,-7.802604,7.356370,4.598639,4.261557,3.711994,4.033632,-9.011776,7.212568],[6.783120,1.901987,5.724015,-7.877527,1.820184,-5.405572,9.645788,4.452380,-0.190996,-6.507675],[-1.701711,0.143105,-2.569567,-5.635914,-3.042434,-0.120782,-0.217522,2.938941,0.341753,-7.319123],[8.337056,4.611102,1.767344,-4.514435,-7.335780,1.111824,-4.554577,-6.957677,0.642244,6.295991],[-6.856421,4.776195,-6.802475,-8.543153,-0.359856,-2.334715,0.140266,4.651578,-2.535440,7.394059],[-3.534820,6.111174,2.645639,5.124372,4.265700,-8.508059,-2.969993,-4.916945,0.859673,-7.014196],[-4.038957,2.642793,8.963858,-4.720673,-9.741697,-6.644706,-5.668681,-2.362128,4.926551,-4.508292]],[[-0.328700,-0.625474,-4.453920,2.119926,7.911398,-5.868436,-7.493810,-2.369073,-2.943957,-0.201028],[-3.520343,7.605012,-0.928898,-6.347164,0.419552,-5.098511,4.210633,-2.527898,-7.441426,1.732757],[-7.303811,1.557664,5.306133,-6.516959,-3.200623,2.280895,4.114526,7.150293,-3.856600,0.347976],[-6.034560,3.330067,-9.910034,5.493066,-4.795437,-7.399810,-5.985172,9.898866,3.923077,2.889466],[-3.664990,-9.526188,6.945818,-1.171880,8.235661,9.824003,7.542899,-8.687335,3.052020,-5.894725],[-5.693297,-6.423705,-8.826180,9.527882,6.066840,0.055587,5.118213,5.357664,2.032161,-1.415271],[6.051475,-0.914305,-7.428940,-6.628458,7.761481,2.334540,1.270683,-6.385248,-7.526670,-3.368755],[5.666481,7.861925,6.506507,7.075158,-2.908922,-5.745869,-9.473154,2.687310,6.466658,-0.598679],[-3.317346,-1.002931,4.828995,-3.669891,-1.560518,5.543048,-9.333364,-6.496347,8.794219,1.154092]],[[0.155752,0.396946,-4.872953,7.002298,-2.891189,-4.317316,8.728444,-0.891088,-3.915563,-4.392146],[9.594110,-2.048934,9.071948,-3.942097,-4.257586,-3.347089,9.796454,6.009864,-6.057667,9.535458],[-3.775863,-4.324690,-1.637444,-2.554318,0.037688,-5.566236,-2.220784,-6.816717,6.011547,-1.113967],[-7.997626,-4.135544,-4.396591,-4.756625,-5.520191,0.343324,4.676156,-2.761700,0.339896,-2.278933],[-6.569535,2.182685,9.957645,-0.151262,-5.117339,8.834077,7.400247,-3.917665,0.115542,0.048375],[-7.802530,5.020566,-3.799439,-0.665955,-5.825858,-3.376952,6.430453,-6.160833,1.521680,4.273135],[3.002336,0.909357,-2.200972,3.104205,-6.223094,0.461704,7.412182,-3.243582,5.332431,8.374274],[-8.647246,-6.710016,-0.097138,-6.707464,2.076035,8.021244,-5.192642,8.086180,2.182412,3.176716],[7.507874,-9.039945,5.043866,-6.543855,1.093498,-5.793150,3.587660,3.091248,8.925140,-2.114803]],[[-3.853408,-8.423640,-9.099864,6.316941,-0.965473,8.017897,-7.697250,-1.675400,-7.749794,-5.463086],[9.373626,3.568609,8.912726,-5.958795,9.863089,0.840523,-8.953923,-5.480077,2.448105,-3.623501],[-0.178254,-6.247913,-1.835658,-1.784337,3.648482,-6.425507,-5.733162,-2.175974,5.907380,-9.227247],[5.419424,-0.914862,2.689401,-5.584314,-1.204795,-7.032971,-3.533111,3.787550,-3.801949,2.342698],[-2.250061,-8.950314,-2.376696,-2.632400,0.237398,-8.375469,-7.780190,-0.484007,0.906704,3.832363],[-1.668296,1.954098,-8.651827,1.435843,-4.965862,-3.236149,-0.702426,5.664743,2.607951,-9.768475],[1.604733,5.527342,6.898893,2.136053,-7.314087,5.183003,4.820261,9.785032,4.195234,-8.410819],[-4.192753,9.248415,4.860412,9.818047,-6.303080,4.495296,-8.675746,-1.531398,-6.279486,-4.756724],[-4.345989,5.671355,-2.558777,8.934284,8.863279,-7.627537,-5.683800,0.002684,-1.405006,0.696113]],[[-1.620868,-1.856334,2.524933,0.548487,4.755425,4.803951,4.028276,8.133988,5.089471,8.012359],[-5.049837,-5.192475,9.843228,-3.872106,-7.707554,2.767117,-6.041083,8.075157,-2.905148,4.829662],[1.524564,5.819835,-9.157043,-5.967332,6.236250,-9.124886,9.324940,-5.270448,-7.992743,5.532265],[-9.648911,-5.069415,-9.675543,2.079044,-9.327268,-1.147232,2.228027,-2.315794,-9.820955,7.886136],[-2.836666,3.493777,5.512434,4.205442,-1.851079,-3.792432,6.602245,3.451807,2.353416,-1.732825],[-7.507999,8.820704,-7.253823,5.380550,-7.484088,-4.340824,-5.302371,2.774080,6.812432,-8.993715],[2.572280,2.823553,4.498977,-2.216149,4.178907,-6.756989,-7.915387,5.394699,0.427799,0.279830],[2.614554,-0.659996,-4.558776,1.678576,-9.684352,4.426676,3.122600,-1.465292,-8.438973,0.802235],[6.719545,1.406723,2.144856,-7.287373,7.069716,-4.177025,6.994919,-6.672983,-3.252362,-6.944738]],[[8.140483,-7.658041,-3.738713,7.064787,-7.082071,-8.014338,-4.410053,1.000553,-0.136670,-7.821682],[3.275303,-0.061274,-0.771597,-4.386493,4.751567,1.131559,9.854439,5.379081,2.479712,-9.177547],[8.439927,8.138801,-2.464802,1.948421,7.184169,-2.348538,-2.111269,7.587914,0.922255,-2.199005],[-7.339117,-4.203782,0.025501,1.092209,-4.340826,-6.993072,-2.701067,-4.798827,-5.908420,8.674370],[2.299041,0.930117,4.581297,-5.274715,-6.865980,8.789812,5.687420,-0.952101,9.054646,8.409194],[7.362840,0.425348,3.440990,-8.818181,6.163389,5.641516,2.765937,-3.721735,-2.739109,-9.216196],[2.939901,0.630114,8.761445,-2.985593,-1.705780,-8.922604,8.912948,1.732456,9.647268,9.420927],[-3.578098,-9.623566,3.280616,-3.490349,9.948973,-9.991462,-1.647981,8.364517,-0.027144,-3.952951],[3.226923,-8.753239,-8.086413,-8.891084,-1.154576,-7.233966,-2.375260,-5.265270,4.747319,1.234133]],[[4.281297,-3.545718,-9.570096,7.170880,2.776859,1.870776,6.715528,5.502653,3.901492,3.481474],[2.583183,-7.977309,-5.727038,6.683183,9.322227,5.831989,0.352962,-0.827580,2.939675,-9.365800],[7.389000,-3.004901,3.230765,-7.477766,7.888394,-7.836329,1.674268,-2.327772,-1.717972,-8.744739],[5.998086,-2.059554,3.763730,-3.419778,6.466176,6.170813,-3.028117,9.496554,1.802530,-7.615799],[3.911788,-7.233368,-8.230674,9.326149,-2.405326,-0.217234,8.455069,-7.975864,-0.807256,2.344949],[5.149758,-7.644117,-8.645827,-9.275760,-2.392979,-6.711385,5.212252,-8.837617,-0.010015,-6.214428],[0.697820,-8.617171,-0.456998,9.401035,5.352542,-9.657192,0.842565,-1.384314,-1.533517,-0.464499],[1.349658,-8.473340,4.813429,-9.875364,-8.647508,-8.044791,-4.848472,-5.150062,-2.156319,1.164273],[0.243100,-8.660390,-5.192387,-4.371749,6.329765,8.915159,-1.100955,-6.185233,5.231669,9.879359]],[[4.131356,8.836083,-2.334212,-1.111223,-6.566286,-8.625604,0.789858,-8.546926,5.445912,-8.938524],[6.454986,1.476294,-5.250524,8.819246,3.027623,2.446218,5.477341,-7.920013,0.630443,-7.038150],[-9.682551,4.016994,2.147623,3.049163,-0.903830,-2.056258,-8.871711,0.495939,9.050081,-5.732494],[3.653126,1.746972,-8.522300,-8.259613,4.765325,3.481705,8.491826,3.331757,2.335141,8.363080],[6.783625,2.005598,-4.025522,-3.241870,-6.377644,-8.372890,-3.924748,-4.046424,1.045686,-7.946273],[3.860455,-0.384457,-2.127752,3.730561,-9.820155,-3.469722,-2.858901,5.717701,-1.813934,-2.090019],[-3.431215,3.210870,2.965726,-4.659784,-4.109806,6.899072,-2.498741,0.712005,4.603496,-3.455236],[0.625402,3.695491,0.776350,-6.023236,-1.828955,-2.915694,0.079911,-9.997420,5.240783,8.312967],[5.560622,5.472499,-6.104478,1.281574,0.057774,-5.414405,-0.170679,2.015357,-7.380128,6.305672]],[[-3.828391,-2.638505,7.960390,-8.148625,1.663880,4.034870,-1.523047,-7.939739,2.858728,3.290459],[-8.109512,8.066924,0.093248,-1.260912,9.599446,2.963083,5.188229,0.973137,-6.413056,7.151502],[-2.155580,-8.334313,1.691237,7.061423,-9.128329,8.217206,-6.239725,7.510166,8.812873,-1.950406],[-9.377625,6.514379,6.200573,-8.827918,-8.108977,1.671563,-2.448847,-8.048567,-2.725115,-1.111247],[-3.704580,1.699404,4.295533,-0.412214,-0.450871,9.154755,-0.073845,-4.041613,0.864098,0.778897],[-0.606178,-1.518568,1.476853,-1.948430,5.465032,-3.032910,7.190120,-7.209605,7.836696,9.079270],[5.251512,-6.126506,2.594003,4.638663,5.744823,8.138286,1.305760,3.411434,-9.472652,0.780072],[-1.841808,3.134445,6.133461,-8.876983,-5.270886,3.941404,-8.669934,-0.230593,-5.051117,6.694118],[-6.701820,-0.828877,-8.131593,-8.378013,5.127394,-5.940726,-6.588561,9.926479,-9.275017,-1.299624]]], dtype = "float64")#candidate|688|(15, 9, 10)|const|float64
var_689 = relay.var("var_689", dtype = "float64", shape = (15, 9, 10))#candidate|689|(15, 9, 10)|var|float64
bop_690 = relay.mod(const_688.astype('float64'), relay.reshape(var_689.astype('float64'), relay.shape_of(const_688))) # shape=(15, 9, 10)
func_604_call = mod.get_global_var('func_604')
func_605_call = mutated_mod.get_global_var('func_605')
call_695 = relay.TupleGetItem(func_604_call(), 0)
call_696 = relay.TupleGetItem(func_605_call(), 0)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_704 = relay.TupleGetItem(func_296_call(), 1)
call_705 = relay.TupleGetItem(func_297_call(), 1)
output = relay.Tuple([bop_690,call_695,call_704,])
output2 = relay.Tuple([bop_690,call_696,call_705,])
func_725 = relay.Function([var_689,], output)
mod['func_725'] = func_725
mod = relay.transform.InferType()(mod)
mutated_mod['func_725'] = func_725
mutated_mod = relay.transform.InferType()(mutated_mod)
var_726 = relay.var("var_726", dtype = "float64", shape = (15, 9, 10))#candidate|726|(15, 9, 10)|var|float64
func_725_call = mutated_mod.get_global_var('func_725')
call_727 = func_725_call(var_726)
output = call_727
func_728 = relay.Function([var_726], output)
mutated_mod['func_728'] = func_728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_587_call = mutated_mod.get_global_var('func_587')
call_773 = relay.TupleGetItem(func_585_call(), 0)
call_774 = relay.TupleGetItem(func_587_call(), 0)
output = relay.Tuple([call_773,])
output2 = relay.Tuple([call_774,])
func_780 = relay.Function([], output)
mod['func_780'] = func_780
mod = relay.transform.InferType()(mod)
output = func_780()
func_781 = relay.Function([], output)
mutated_mod['func_781'] = func_781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_394_call = mutated_mod.get_global_var('func_394')
call_833 = relay.TupleGetItem(func_393_call(), 0)
call_834 = relay.TupleGetItem(func_394_call(), 0)
output = relay.Tuple([call_833,])
output2 = relay.Tuple([call_834,])
func_840 = relay.Function([], output)
mod['func_840'] = func_840
mod = relay.transform.InferType()(mod)
mutated_mod['func_840'] = func_840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_840_call = mutated_mod.get_global_var('func_840')
call_841 = func_840_call()
output = call_841
func_842 = relay.Function([], output)
mutated_mod['func_842'] = func_842
mutated_mod = relay.transform.InferType()(mutated_mod)
const_859 = relay.const([[[10,-4,-2,3,-2,9,3,-3,-8],[-5,-6,-8,7,4,-9,3,-4,-10],[-10,2,-9,9,5,-6,-9,-3,-3],[-2,6,10,4,7,-4,6,-1,5],[-1,1,-8,-10,8,-4,4,-1,9],[-6,-9,-10,-1,7,5,1,8,-4],[10,3,-7,9,10,-4,5,1,4],[-7,10,-6,-5,2,10,10,-10,-8],[-8,10,8,7,3,-7,1,-9,-7]],[[-7,1,-8,5,-9,-10,4,3,-6],[-6,-6,2,6,-7,-4,10,-7,-1],[2,-4,5,-9,2,2,6,-2,9],[-4,-7,1,-5,3,2,8,3,8],[-4,6,-10,5,-8,-6,2,3,-3],[3,5,-2,1,4,2,2,8,5],[8,-4,8,7,-4,-1,7,6,1],[1,-10,8,5,-1,9,1,-5,-8],[-6,2,5,6,-9,-4,-4,4,7]],[[7,3,-7,1,4,4,8,-4,10],[6,-3,-2,-7,9,-8,5,-2,-3],[-5,-8,10,-8,2,9,-3,-1,1],[-1,-8,4,-1,-3,-9,2,3,-2],[2,1,2,-9,6,1,-1,-10,7],[9,2,2,10,-5,4,4,-7,-3],[7,-6,-1,-2,1,3,3,7,4],[7,3,-5,-1,-4,-5,9,-8,5],[-2,-2,-9,3,7,-7,7,-4,-10]],[[-7,9,-1,-10,-8,-3,-8,10,-10],[-4,-2,2,1,5,-2,-4,8,-2],[-8,7,-1,-9,-9,-8,9,-1,3],[2,7,-9,4,7,7,-1,2,-2],[-2,1,-3,10,10,-5,-7,5,4],[-10,-7,10,-8,10,-1,-4,-3,-4],[-3,10,-6,-4,-2,6,5,4,-4],[-6,5,2,-8,1,-1,-10,9,-10],[5,-7,-5,2,-10,-3,-9,7,-7]],[[-4,-7,-8,9,-7,-10,-3,-10,-3],[-3,8,9,6,-10,-6,5,-4,6],[-3,2,3,-6,8,-7,5,-3,-1],[-4,-4,3,-3,-9,-1,1,-10,-5],[-4,1,8,-2,-8,-6,9,8,-4],[3,-9,6,-7,-3,9,-2,-8,-6],[1,-1,-5,9,-9,-9,-10,-2,-7],[9,7,-3,-10,1,9,8,5,10],[8,-6,-8,10,9,7,2,10,-7]],[[-6,-9,7,-2,6,4,-9,-5,7],[-2,-1,9,-7,-3,-10,9,7,3],[-3,-1,-4,9,5,-8,9,-1,1],[10,3,-4,-4,-1,10,-9,8,-6],[-2,6,8,4,-4,-10,7,10,3],[-4,-6,10,-10,-10,6,1,-2,-7],[-8,10,6,-4,7,-4,7,-7,-7],[-8,-5,-3,6,-1,10,-1,-9,-2],[-10,-1,-2,9,-4,-2,-5,-8,-9]],[[-1,7,-5,2,-5,6,9,6,5],[2,5,10,9,-8,-6,-7,3,-3],[-1,4,-5,5,-10,-1,-7,9,-2],[-1,-6,5,-5,-3,6,-9,-10,-3],[7,8,-9,10,-5,-9,-10,8,-9],[-2,-7,5,10,10,-8,4,3,1],[-2,-7,2,1,-6,1,-2,-2,-7],[-4,-2,6,1,3,9,-5,9,-7],[-8,4,-7,-9,-10,-10,7,-4,10]]], dtype = "uint8")#candidate|859|(7, 9, 9)|const|uint8
const_860 = relay.const([[[-1,3,-8,-10,-8,6,9,-2,4],[2,-8,-4,2,-7,10,-10,-4,-9],[-3,-1,-1,-10,3,-5,-2,2,-1],[4,-6,6,9,-1,10,5,8,-6],[-5,1,8,6,5,10,4,1,-7],[10,-4,-10,8,10,3,6,2,-7],[-5,2,1,-8,-8,-7,-8,2,5],[-8,9,-2,8,2,5,-2,-2,-2],[6,10,-1,-10,3,2,-4,-4,10]],[[5,3,-10,7,-1,-6,-6,5,8],[-4,-6,8,8,10,-7,7,10,1],[10,-10,9,-6,-10,-10,6,5,-2],[9,9,1,2,9,-9,2,10,-10],[9,3,-6,6,-8,3,-5,1,4],[9,-9,-9,-9,-8,4,8,-4,3],[-6,2,-1,8,-9,-2,-9,10,9],[6,2,-9,-2,8,-9,-7,-1,3],[-4,-1,-7,8,4,-6,9,5,8]],[[8,2,-7,8,-10,-5,-4,-3,3],[-6,8,1,4,-7,-3,-2,6,-6],[9,-9,4,1,2,-1,-3,-8,-6],[6,10,9,-8,-2,-7,9,2,-4],[-3,-2,-8,-2,1,-6,8,9,5],[9,8,-10,-2,2,9,10,-10,9],[-9,-3,-10,7,10,5,-5,9,-10],[10,-7,5,8,-10,-2,-8,-1,-1],[-9,10,-6,3,1,-5,-10,-10,7]],[[5,-3,-4,7,7,-3,10,7,-1],[4,4,-7,-6,-6,-6,-4,-8,9],[5,2,-3,-8,-6,4,10,3,-3],[5,-9,-8,1,7,2,-1,-1,8],[-7,8,3,-5,10,-7,8,4,2],[-4,5,-2,7,-5,6,2,-10,-1],[2,6,-3,5,-6,1,-1,10,-6],[5,8,2,3,-9,6,-4,7,-10],[-4,4,-4,-5,-9,4,-9,-1,-1]],[[1,8,-5,-2,-3,-10,9,-8,3],[7,-10,4,4,-3,10,-7,-7,3],[-7,2,5,-5,-7,7,-6,7,3],[-7,5,-9,5,-6,-10,4,-5,9],[10,4,6,5,-8,-5,-4,-7,4],[1,-1,-2,7,8,4,-2,1,10],[-1,-7,-7,-9,7,-9,-1,2,9],[-3,-10,10,10,8,10,-9,3,8],[-8,-3,3,8,4,8,-4,2,3]],[[9,4,7,5,2,1,10,-9,6],[4,-7,-4,4,7,-1,7,-6,-9],[-4,-8,-2,8,-10,-4,-10,8,7],[-4,9,6,-2,2,-6,10,5,8],[-8,-9,3,3,-4,-3,-5,1,-6],[4,1,-5,-6,9,-4,-1,1,-3],[5,-10,-8,-9,9,5,-10,3,-6],[10,-3,3,4,-2,-4,-1,-10,10],[-5,-3,1,-10,-8,2,-1,-5,-9]],[[-6,4,10,-2,9,-4,-3,7,5],[-3,-1,-10,-4,5,-7,-10,9,-10],[2,-2,7,-9,6,4,4,-8,10],[-7,-9,6,9,9,-9,-9,-3,3],[8,8,-6,7,4,6,-3,10,7],[10,-3,-6,-9,7,-5,-10,10,10],[2,7,-5,10,8,-2,8,-3,-10],[-5,-3,9,-1,-2,8,-9,9,8],[1,-4,10,5,5,-8,4,-3,6]]], dtype = "uint8")#candidate|860|(7, 9, 9)|const|uint8
bop_861 = relay.right_shift(const_859.astype('uint8'), relay.reshape(const_860.astype('uint8'), relay.shape_of(const_859))) # shape=(7, 9, 9)
func_604_call = mod.get_global_var('func_604')
func_605_call = mutated_mod.get_global_var('func_605')
call_871 = relay.TupleGetItem(func_604_call(), 0)
call_872 = relay.TupleGetItem(func_605_call(), 0)
uop_881 = relay.sqrt(const_860.astype('float64')) # shape=(7, 9, 9)
func_541_call = mod.get_global_var('func_541')
func_542_call = mutated_mod.get_global_var('func_542')
call_883 = relay.TupleGetItem(func_541_call(), 0)
call_884 = relay.TupleGetItem(func_542_call(), 0)
output = relay.Tuple([bop_861,call_871,uop_881,call_883,])
output2 = relay.Tuple([bop_861,call_872,uop_881,call_884,])
func_890 = relay.Function([], output)
mod['func_890'] = func_890
mod = relay.transform.InferType()(mod)
output = func_890()
func_891 = relay.Function([], output)
mutated_mod['func_891'] = func_891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_394_call = mutated_mod.get_global_var('func_394')
call_913 = relay.TupleGetItem(func_393_call(), 1)
call_914 = relay.TupleGetItem(func_394_call(), 1)
output = relay.Tuple([call_913,])
output2 = relay.Tuple([call_914,])
func_917 = relay.Function([], output)
mod['func_917'] = func_917
mod = relay.transform.InferType()(mod)
mutated_mod['func_917'] = func_917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_917_call = mutated_mod.get_global_var('func_917')
call_918 = func_917_call()
output = call_918
func_919 = relay.Function([], output)
mutated_mod['func_919'] = func_919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_982 = relay.TupleGetItem(func_506_call(), 0)
call_983 = relay.TupleGetItem(func_507_call(), 0)
output = call_982
output2 = call_983
func_984 = relay.Function([], output)
mod['func_984'] = func_984
mod = relay.transform.InferType()(mod)
mutated_mod['func_984'] = func_984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_984_call = mutated_mod.get_global_var('func_984')
call_985 = func_984_call()
output = call_985
func_986 = relay.Function([], output)
mutated_mod['func_986'] = func_986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_989 = func_984_call()
call_990 = func_984_call()
uop_998 = relay.exp(call_989.astype('float32')) # shape=(1, 3, 1)
uop_1000 = relay.exp(call_990.astype('float32')) # shape=(1, 3, 1)
bop_1005 = relay.floor_divide(uop_998.astype('float32'), relay.reshape(call_989.astype('float32'), relay.shape_of(uop_998))) # shape=(1, 3, 1)
bop_1008 = relay.floor_divide(uop_1000.astype('float32'), relay.reshape(call_990.astype('float32'), relay.shape_of(uop_1000))) # shape=(1, 3, 1)
output = bop_1005
output2 = bop_1008
func_1014 = relay.Function([], output)
mod['func_1014'] = func_1014
mod = relay.transform.InferType()(mod)
mutated_mod['func_1014'] = func_1014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1014_call = mutated_mod.get_global_var('func_1014')
call_1015 = func_1014_call()
output = call_1015
func_1016 = relay.Function([], output)
mutated_mod['func_1016'] = func_1016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_541_call = mod.get_global_var('func_541')
func_542_call = mutated_mod.get_global_var('func_542')
call_1025 = relay.TupleGetItem(func_541_call(), 0)
call_1026 = relay.TupleGetItem(func_542_call(), 0)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_1045 = relay.TupleGetItem(func_468_call(), 2)
call_1046 = relay.TupleGetItem(func_470_call(), 2)
func_1014_call = mod.get_global_var('func_1014')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_1055 = func_1014_call()
call_1056 = func_1014_call()
output = relay.Tuple([call_1025,call_1045,call_1055,])
output2 = relay.Tuple([call_1026,call_1046,call_1056,])
func_1061 = relay.Function([], output)
mod['func_1061'] = func_1061
mod = relay.transform.InferType()(mod)
output = func_1061()
func_1062 = relay.Function([], output)
mutated_mod['func_1062'] = func_1062
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1073 = relay.const([[[7,7,-9,5,-4,-1,-7,-9,-5],[-6,-4,4,4,-8,-2,-8,-9,6],[9,4,-8,-8,-10,-5,-9,-7,-1],[-8,9,-3,-8,-10,7,-3,-9,-2],[3,-2,-8,-7,2,-7,-5,8,-10],[4,2,-5,2,-7,-6,-8,8,4],[-8,10,-7,3,-3,-7,-3,-3,9],[-6,-5,-1,-10,3,-10,-4,10,-10],[-5,8,-5,-3,7,5,-3,6,4],[10,-8,-3,-10,7,-3,4,2,-5],[8,-7,-3,3,-5,-3,-6,-4,4],[3,4,-3,-8,4,2,7,9,-6],[-8,6,8,4,-2,10,-4,1,4],[-7,-4,10,-2,5,1,-4,4,4]],[[-1,8,5,-9,-5,-8,-6,-1,8],[6,10,-1,-5,-2,7,1,-4,-1],[-10,-9,3,-6,-4,9,2,-2,-7],[5,-10,-2,-3,-6,3,8,-8,-10],[8,-9,-5,-6,6,-7,-3,-6,1],[3,-3,3,-4,1,9,4,9,10],[4,9,6,-4,10,5,9,5,6],[-8,-8,4,-2,5,-2,3,2,7],[-8,8,-2,-9,-10,-1,-4,-7,-7],[10,-9,-1,9,-10,-6,7,-9,-3],[-8,10,-9,-2,-9,5,-2,-7,7],[4,2,7,1,1,10,9,-6,-6],[1,8,-9,-9,-8,-1,-4,1,7],[1,3,-7,6,1,-6,-1,-4,-8]],[[1,-3,-4,4,-9,2,-4,-3,-7],[-9,6,-8,-8,-9,7,-7,-7,-9],[-7,8,7,-2,-5,9,-7,4,8],[-8,-1,1,8,-8,8,-5,8,3],[-3,8,1,-9,-6,6,7,2,-2],[-5,1,-5,-9,-6,-4,-4,-3,5],[2,4,9,3,5,5,10,-10,-3],[10,7,-1,-2,-10,-9,-10,-10,-10],[6,6,-3,-1,-9,2,9,-6,-7],[-7,-3,-5,-1,5,9,10,-3,9],[5,6,2,-10,3,7,-2,-10,-1],[-9,-2,-4,4,-8,-10,10,8,3],[-8,-1,8,1,-2,5,8,6,10],[2,-3,10,7,3,8,5,9,-6]]], dtype = "int32")#candidate|1073|(3, 14, 9)|const|int32
var_1074 = relay.var("var_1074", dtype = "int32", shape = (3, 14, 9))#candidate|1074|(3, 14, 9)|var|int32
bop_1075 = relay.equal(const_1073.astype('bool'), relay.reshape(var_1074.astype('bool'), relay.shape_of(const_1073))) # shape=(3, 14, 9)
output = bop_1075
output2 = bop_1075
func_1080 = relay.Function([var_1074,], output)
mod['func_1080'] = func_1080
mod = relay.transform.InferType()(mod)
var_1081 = relay.var("var_1081", dtype = "int32", shape = (3, 14, 9))#candidate|1081|(3, 14, 9)|var|int32
output = func_1080(var_1081)
func_1082 = relay.Function([var_1081], output)
mutated_mod['func_1082'] = func_1082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_890_call = mod.get_global_var('func_890')
func_891_call = mutated_mod.get_global_var('func_891')
call_1156 = relay.TupleGetItem(func_890_call(), 3)
call_1157 = relay.TupleGetItem(func_891_call(), 3)
output = call_1156
output2 = call_1157
func_1170 = relay.Function([], output)
mod['func_1170'] = func_1170
mod = relay.transform.InferType()(mod)
output = func_1170()
func_1171 = relay.Function([], output)
mutated_mod['func_1171'] = func_1171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1014_call = mod.get_global_var('func_1014')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_1193 = func_1014_call()
call_1194 = func_1014_call()
var_1214 = relay.var("var_1214", dtype = "float32", shape = (16, 3, 1))#candidate|1214|(16, 3, 1)|var|float32
bop_1215 = relay.bitwise_xor(call_1193.astype('int32'), var_1214.astype('int32')) # shape=(16, 3, 1)
bop_1218 = relay.bitwise_xor(call_1194.astype('int32'), var_1214.astype('int32')) # shape=(16, 3, 1)
func_917_call = mod.get_global_var('func_917')
func_919_call = mutated_mod.get_global_var('func_919')
call_1225 = relay.TupleGetItem(func_917_call(), 0)
call_1226 = relay.TupleGetItem(func_919_call(), 0)
output = relay.Tuple([bop_1215,call_1225,])
output2 = relay.Tuple([bop_1218,call_1226,])
func_1227 = relay.Function([var_1214,], output)
mod['func_1227'] = func_1227
mod = relay.transform.InferType()(mod)
var_1228 = relay.var("var_1228", dtype = "float32", shape = (16, 3, 1))#candidate|1228|(16, 3, 1)|var|float32
output = func_1227(var_1228)
func_1229 = relay.Function([var_1228], output)
mutated_mod['func_1229'] = func_1229
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1239 = relay.var("var_1239", dtype = "float32", shape = (10, 8, 13))#candidate|1239|(10, 8, 13)|var|float32
uop_1240 = relay.asin(var_1239.astype('float32')) # shape=(10, 8, 13)
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_1247 = func_984_call()
call_1248 = func_984_call()
var_1253 = relay.var("var_1253", dtype = "uint64", shape = (9, 3, 13))#candidate|1253|(9, 3, 13)|var|uint64
bop_1254 = relay.minimum(call_1247.astype('float32'), var_1253.astype('float32')) # shape=(9, 3, 13)
bop_1257 = relay.minimum(call_1248.astype('float32'), var_1253.astype('float32')) # shape=(9, 3, 13)
func_604_call = mod.get_global_var('func_604')
func_605_call = mutated_mod.get_global_var('func_605')
call_1258 = relay.TupleGetItem(func_604_call(), 0)
call_1259 = relay.TupleGetItem(func_605_call(), 0)
var_1261 = relay.var("var_1261", dtype = "float32", shape = (9, 3, 13))#candidate|1261|(9, 3, 13)|var|float32
bop_1262 = relay.bitwise_or(bop_1254.astype('uint8'), relay.reshape(var_1261.astype('uint8'), relay.shape_of(bop_1254))) # shape=(9, 3, 13)
bop_1265 = relay.bitwise_or(bop_1257.astype('uint8'), relay.reshape(var_1261.astype('uint8'), relay.shape_of(bop_1257))) # shape=(9, 3, 13)
func_585_call = mod.get_global_var('func_585')
func_587_call = mutated_mod.get_global_var('func_587')
call_1278 = relay.TupleGetItem(func_585_call(), 1)
call_1279 = relay.TupleGetItem(func_587_call(), 1)
bop_1282 = relay.equal(uop_1240.astype('bool'), relay.reshape(var_1239.astype('bool'), relay.shape_of(uop_1240))) # shape=(10, 8, 13)
uop_1298 = relay.sin(bop_1262.astype('float32')) # shape=(9, 3, 13)
uop_1300 = relay.sin(bop_1265.astype('float32')) # shape=(9, 3, 13)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_1313 = relay.TupleGetItem(func_296_call(), 1)
call_1314 = relay.TupleGetItem(func_297_call(), 1)
func_1227_call = mod.get_global_var('func_1227')
func_1229_call = mutated_mod.get_global_var('func_1229')
const_1316 = relay.const([5.391898,0.519013,3.162209,-2.104792,1.215131,0.987627,-0.887985,-6.452967,2.362409,-0.888920,1.408082,-3.267712,-7.062914,-9.828481,-2.085296,-5.810175,-3.334476,-3.363843,-2.124677,0.821439,-8.703699,-6.913208,8.569590,-4.962543,-1.226684,-0.657136,-6.427631,4.015168,-4.515648,-3.478816,-1.409153,-7.747863,-4.402743,-7.520700,9.628292,-6.768405,2.002657,-3.415347,8.505904,5.182965,-6.091905,-9.344685,7.378096,2.063097,8.290680,-4.337835,-6.526462,8.415645], dtype = "float32")#candidate|1316|(48,)|const|float32
call_1315 = relay.TupleGetItem(func_1227_call(relay.reshape(const_1316.astype('float32'), [16, 3, 1])), 0)
call_1317 = relay.TupleGetItem(func_1229_call(relay.reshape(const_1316.astype('float32'), [16, 3, 1])), 0)
func_585_call = mod.get_global_var('func_585')
func_587_call = mutated_mod.get_global_var('func_587')
call_1319 = relay.TupleGetItem(func_585_call(), 0)
call_1320 = relay.TupleGetItem(func_587_call(), 0)
output = relay.Tuple([call_1258,call_1278,bop_1282,uop_1298,call_1313,call_1315,const_1316,call_1319,])
output2 = relay.Tuple([call_1259,call_1279,bop_1282,uop_1300,call_1314,call_1317,const_1316,call_1320,])
func_1321 = relay.Function([var_1239,var_1253,var_1261,], output)
mod['func_1321'] = func_1321
mod = relay.transform.InferType()(mod)
mutated_mod['func_1321'] = func_1321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mutated_mod.get_global_var('func_1321')
var_1323 = relay.var("var_1323", dtype = "float32", shape = (10, 8, 13))#candidate|1323|(10, 8, 13)|var|float32
var_1324 = relay.var("var_1324", dtype = "uint64", shape = (9, 3, 13))#candidate|1324|(9, 3, 13)|var|uint64
var_1325 = relay.var("var_1325", dtype = "float32", shape = (9, 3, 13))#candidate|1325|(9, 3, 13)|var|float32
call_1322 = func_1321_call(var_1323,var_1324,var_1325,)
output = call_1322
func_1326 = relay.Function([var_1323,var_1324,var_1325,], output)
mutated_mod['func_1326'] = func_1326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_1402 = relay.TupleGetItem(func_296_call(), 0)
call_1403 = relay.TupleGetItem(func_297_call(), 0)
output = call_1402
output2 = call_1403
func_1404 = relay.Function([], output)
mod['func_1404'] = func_1404
mod = relay.transform.InferType()(mod)
mutated_mod['func_1404'] = func_1404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1404_call = mutated_mod.get_global_var('func_1404')
call_1405 = func_1404_call()
output = call_1405
func_1406 = relay.Function([], output)
mutated_mod['func_1406'] = func_1406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_587_call = mutated_mod.get_global_var('func_587')
call_1418 = relay.TupleGetItem(func_585_call(), 0)
call_1419 = relay.TupleGetItem(func_587_call(), 0)
uop_1425 = relay.acos(call_1418.astype('float32')) # shape=(1, 3, 1)
uop_1427 = relay.acos(call_1419.astype('float32')) # shape=(1, 3, 1)
bop_1429 = relay.logical_or(uop_1425.astype('bool'), relay.reshape(call_1418.astype('bool'), relay.shape_of(uop_1425))) # shape=(1, 3, 1)
bop_1432 = relay.logical_or(uop_1427.astype('bool'), relay.reshape(call_1419.astype('bool'), relay.shape_of(uop_1427))) # shape=(1, 3, 1)
uop_1443 = relay.log(bop_1429.astype('float32')) # shape=(1, 3, 1)
uop_1445 = relay.log(bop_1432.astype('float32')) # shape=(1, 3, 1)
bop_1446 = relay.multiply(uop_1443.astype('int8'), relay.reshape(call_1418.astype('int8'), relay.shape_of(uop_1443))) # shape=(1, 3, 1)
bop_1449 = relay.multiply(uop_1445.astype('int8'), relay.reshape(call_1419.astype('int8'), relay.shape_of(uop_1445))) # shape=(1, 3, 1)
bop_1453 = relay.greater_equal(call_1418.astype('bool'), relay.reshape(uop_1425.astype('bool'), relay.shape_of(call_1418))) # shape=(1, 3, 1)
bop_1456 = relay.greater_equal(call_1419.astype('bool'), relay.reshape(uop_1427.astype('bool'), relay.shape_of(call_1419))) # shape=(1, 3, 1)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_1463 = relay.TupleGetItem(func_468_call(), 0)
call_1464 = relay.TupleGetItem(func_470_call(), 0)
bop_1468 = relay.less(bop_1446.astype('bool'), relay.reshape(uop_1443.astype('bool'), relay.shape_of(bop_1446))) # shape=(1, 3, 1)
bop_1471 = relay.less(bop_1449.astype('bool'), relay.reshape(uop_1445.astype('bool'), relay.shape_of(bop_1449))) # shape=(1, 3, 1)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_1477 = relay.TupleGetItem(func_506_call(), 1)
call_1478 = relay.TupleGetItem(func_507_call(), 1)
output = relay.Tuple([bop_1453,call_1463,bop_1468,call_1477,])
output2 = relay.Tuple([bop_1456,call_1464,bop_1471,call_1478,])
func_1483 = relay.Function([], output)
mod['func_1483'] = func_1483
mod = relay.transform.InferType()(mod)
mutated_mod['func_1483'] = func_1483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mutated_mod.get_global_var('func_1483')
call_1484 = func_1483_call()
output = call_1484
func_1485 = relay.Function([], output)
mutated_mod['func_1485'] = func_1485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_1519 = relay.TupleGetItem(func_506_call(), 0)
call_1520 = relay.TupleGetItem(func_507_call(), 0)
var_1526 = relay.var("var_1526", dtype = "uint64", shape = (1, 3, 12))#candidate|1526|(1, 3, 12)|var|uint64
bop_1527 = relay.minimum(call_1519.astype('uint16'), var_1526.astype('uint16')) # shape=(1, 3, 12)
bop_1530 = relay.minimum(call_1520.astype('uint16'), var_1526.astype('uint16')) # shape=(1, 3, 12)
func_917_call = mod.get_global_var('func_917')
func_919_call = mutated_mod.get_global_var('func_919')
call_1535 = relay.TupleGetItem(func_917_call(), 0)
call_1536 = relay.TupleGetItem(func_919_call(), 0)
output = relay.Tuple([bop_1527,call_1535,])
output2 = relay.Tuple([bop_1530,call_1536,])
func_1544 = relay.Function([var_1526,], output)
mod['func_1544'] = func_1544
mod = relay.transform.InferType()(mod)
var_1545 = relay.var("var_1545", dtype = "uint64", shape = (1, 3, 12))#candidate|1545|(1, 3, 12)|var|uint64
output = func_1544(var_1545)
func_1546 = relay.Function([var_1545], output)
mutated_mod['func_1546'] = func_1546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_890_call = mod.get_global_var('func_890')
func_891_call = mutated_mod.get_global_var('func_891')
call_1745 = relay.TupleGetItem(func_890_call(), 0)
call_1746 = relay.TupleGetItem(func_891_call(), 0)
func_1404_call = mod.get_global_var('func_1404')
func_1406_call = mutated_mod.get_global_var('func_1406')
call_1750 = func_1404_call()
call_1751 = func_1404_call()
output = relay.Tuple([call_1745,call_1750,])
output2 = relay.Tuple([call_1746,call_1751,])
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
var_1767 = relay.var("var_1767", dtype = "float64", shape = ())#candidate|1767|()|var|float64
const_1768 = relay.const([[[3.963952,7.797583,-4.078398,-7.465516,-0.029176,-4.782192,3.892070,-7.712862,3.427507,-9.093461,-9.199595,-7.898100,-2.282833,-2.954484],[6.418651,9.704080,1.747475,-3.947395,8.856375,-3.784089,5.460793,-1.646958,2.867438,9.679920,-5.788596,-0.575165,-4.362519,0.456149],[2.551489,-3.594875,-0.887943,-6.926333,-2.021738,7.208395,7.498925,2.774892,-6.919996,8.483766,-7.466311,-9.571467,5.550070,-3.099964],[6.253312,-6.420750,4.995603,6.235437,-2.889385,2.189682,-9.689672,-8.517505,-4.717167,-6.670850,1.349733,-2.083005,7.233839,-3.893605],[-8.110744,-4.971088,7.088369,-9.110224,0.899793,-2.009295,1.065297,-5.988111,-2.662772,7.479867,6.616005,9.499891,-8.662760,-1.960540],[-9.021171,-1.020665,9.491826,-1.928841,1.583131,1.609960,-8.473224,-7.739192,7.185351,3.227299,6.308948,-5.200527,-8.934071,-4.467225],[-4.849262,-8.469818,3.470066,6.951792,-4.100328,7.722220,-5.931349,-4.764664,-8.578684,5.130760,-6.981685,8.006612,8.639856,-0.858495],[4.654645,-1.064175,0.642145,-6.564105,1.800206,-6.007004,5.877255,5.925171,-8.127634,-5.678880,-7.611308,1.596367,-3.433898,4.874824],[-8.310450,-2.869282,-2.650007,6.535611,2.514084,-8.140436,9.844471,-6.170200,7.934797,5.084435,-2.606155,-7.345023,6.097345,0.633200],[4.243744,2.199864,-2.771839,0.735175,8.452975,-1.364873,1.118899,8.054869,8.155339,6.505608,-7.950389,7.871556,1.327294,4.844085]],[[4.626429,-2.912131,9.115930,-0.736180,2.311179,-7.036957,1.076147,-9.418006,-3.745361,6.793986,1.138070,-6.552985,1.510405,-1.010303],[6.577021,0.106760,-4.480962,4.074796,-3.682385,9.041647,-7.371735,-1.350459,2.360471,-1.717486,-5.622805,6.954316,-9.109725,8.946165],[3.695481,-4.304591,-2.681474,0.767842,-2.582752,-1.841876,9.882006,-0.586580,-7.189932,5.643902,4.143376,3.566299,4.142091,-6.926126],[-2.476307,-4.180707,0.687581,-0.066255,-4.927986,9.863018,6.340661,2.084171,2.084526,-2.140943,-6.823178,5.033522,8.788465,-5.322997],[-1.824550,-8.211281,-1.210712,-4.236382,-5.460335,3.196843,6.404258,9.314963,5.738183,4.855159,-8.566467,-9.557163,1.624495,9.058951],[-3.764332,6.177236,-7.857658,4.818416,-6.638118,-6.141026,-0.652679,-0.644539,-1.828163,-7.600851,-0.492381,8.717278,7.152333,-8.099638],[1.410052,5.160260,7.411506,-3.980696,6.792785,-6.806133,-8.120649,-3.176701,4.885557,-1.222397,-2.593307,7.016889,-3.482205,9.364275],[-7.701110,-4.055847,4.884068,8.106100,-0.011856,-3.386677,7.345995,-0.837769,-0.553892,-5.258684,8.110691,2.229836,-5.028893,-2.845085],[0.419568,-3.497334,3.459887,-5.093357,0.915224,7.675576,8.145779,9.302800,6.137324,-8.166519,-4.181217,5.478801,9.379246,6.289725],[8.382148,-6.797836,6.734276,-8.593444,1.311412,-0.157834,-0.079642,7.743863,8.328687,-8.011876,-2.191439,-7.185536,4.422132,-0.231607]],[[6.883657,-1.116933,5.932576,0.350527,-1.899871,-1.182398,-2.233916,-6.509847,-8.951395,0.292032,-8.421972,-0.205508,-4.176054,2.663575],[-9.142955,5.106717,7.741216,-2.786435,-2.922679,2.970196,2.897101,1.578511,-7.600463,-5.605466,2.725307,0.435264,2.571401,-5.786408],[-4.708460,-0.770763,8.936840,-3.972255,9.230646,2.752340,7.829326,-8.784554,-8.624708,-7.578425,7.162057,-6.595653,-6.468956,-7.749242],[7.053010,-4.892236,-8.768381,8.987482,-1.903937,-1.187160,-7.095752,4.452113,9.686304,5.638770,0.350108,-0.712190,-3.682376,3.859745],[-5.250364,7.017365,-9.160536,-9.535572,-3.285116,-1.588064,5.681786,-6.547998,5.531765,6.475073,-1.928210,-8.989958,7.009963,-7.130716],[2.129269,-4.765107,-9.186623,-5.583328,0.748256,4.705423,-0.848299,-8.425956,0.815281,1.197927,7.278107,7.829731,7.029769,2.481758],[-7.421034,2.560429,-8.344916,-2.928038,3.587433,0.077331,8.956166,-9.154538,9.222075,7.904643,9.133873,4.217317,-3.749598,-2.726604],[-4.549795,-8.118548,-5.279675,6.142063,6.779984,0.910371,-3.469528,-0.954239,8.145419,3.352834,4.643535,9.554935,6.490761,5.109124],[8.364762,-4.617569,-7.851411,7.591247,-7.961570,1.743265,-4.841075,-9.596418,8.488399,-1.130441,2.850800,8.745073,-5.131248,0.517845],[4.481699,6.082445,3.424757,1.200350,-9.008028,-8.386128,5.575521,1.945212,-6.850146,-2.534438,-5.743922,-5.271323,-5.197842,-2.638580]],[[7.581902,-6.714326,4.752943,9.155737,8.474364,-0.218789,8.564210,-0.028281,-8.106494,-1.034182,3.891758,-5.058451,4.956369,1.831349],[0.666462,9.352050,-8.202095,7.968748,9.981660,-2.981588,7.379132,9.440865,6.338896,4.510722,5.238827,-2.966647,-9.061413,-2.890122],[5.848804,5.999458,8.108132,6.818742,9.307360,7.600333,-8.011593,3.164191,-1.382452,-2.132759,2.672605,8.752055,-9.443442,2.130493],[5.696263,-6.535006,-5.960944,1.570619,-8.875613,3.926654,5.837015,7.048027,-3.269037,-2.656763,5.197638,-8.910939,-4.535519,8.414733],[8.725097,-7.021204,-2.796950,4.104105,-1.895881,-0.829641,-2.190188,-2.386188,5.419075,8.636593,3.540807,-6.726855,-9.719404,8.896029],[4.978947,6.534187,1.738180,5.107832,0.509685,-8.298307,5.879064,-0.680279,-8.558197,1.088216,-9.109448,7.873852,-2.018299,-9.984469],[-7.853425,-8.854052,-7.895357,-1.909311,7.026730,8.492898,7.684307,-8.638287,5.594636,-6.380940,-0.712957,7.036946,-8.323068,-7.214638],[-6.148179,9.815737,-7.625801,-7.385094,-4.902049,-9.936798,-4.315836,-5.877188,-5.639229,-2.872554,7.306070,5.664411,5.462637,8.230677],[-3.321166,-1.931390,-6.866507,6.576039,2.594843,-1.846536,0.395211,0.045569,-4.651011,0.536187,1.476002,-7.031471,-3.931635,-2.616216],[-2.799355,9.410488,6.454350,-1.858834,9.490541,-6.359552,9.200039,-2.410986,2.001793,3.370620,0.382688,-7.677466,-7.249081,-1.124007]],[[2.247445,-9.729404,-7.315480,-3.042103,-9.101366,7.240703,-2.489106,-9.067368,-1.806446,-2.846893,7.413998,-1.629110,-7.191090,1.100672],[8.888363,2.840599,-1.423696,5.224799,7.081189,-6.871688,-4.373697,-7.621541,3.871373,-3.707411,6.803056,9.797582,-5.224033,-6.494233],[4.798060,-6.481652,0.950842,5.104831,0.982957,-2.712097,-1.667921,-8.700725,-0.627811,4.648740,-8.498094,-2.650759,9.142875,-0.171586],[5.424888,-3.752715,-0.418599,7.650059,2.948938,4.816699,6.139923,5.203318,-3.159023,-0.173743,-7.237473,-7.058871,-7.551078,3.765976],[-9.171509,8.084238,-5.863953,-4.102108,-2.270290,-5.877979,-0.263591,1.217678,8.366129,4.023684,-8.064316,-5.018640,-9.785165,1.812390],[8.776612,-5.183445,-9.202063,9.263593,7.302952,9.946627,-9.325299,2.573813,8.484797,-9.942055,-9.746434,-2.120866,-7.419773,7.407454],[9.432018,5.922238,0.407714,0.282008,4.014904,-1.158900,-7.273671,3.669194,9.367503,-9.468168,0.825258,6.829356,-9.619965,-1.949109],[2.710064,1.028037,5.887012,8.957333,-4.825992,-6.421959,-8.948724,4.204966,2.112820,6.369740,2.661158,8.450384,-5.907786,-9.350567],[7.690283,2.133544,8.589070,4.888388,0.081520,8.722994,3.974136,-8.627441,1.635279,5.887830,-5.196389,7.966121,-2.098994,-3.430589],[-4.815031,8.376433,7.682810,-9.573851,-5.011898,4.486767,-6.221197,2.853768,4.231373,8.964816,9.286793,9.273721,7.655236,-6.385386]],[[2.240686,0.952929,0.932824,9.770052,0.222840,5.474120,-9.924372,-5.075863,-0.210016,-3.165172,1.843038,-7.038981,-2.676508,-4.387382],[-3.855595,6.716446,6.264364,8.397830,-0.747957,0.073551,-2.647125,3.339045,-2.530133,-7.049941,6.242306,-4.201178,-2.892251,-7.397718],[-2.258301,3.720997,2.219070,-8.351800,7.309160,5.720016,9.296368,2.768749,-6.041417,-3.286900,-2.552233,3.686717,6.360654,-5.855457],[-4.904952,6.218389,7.150465,5.106646,7.501298,6.084475,-8.154908,-0.948360,-2.808016,7.255080,-6.606698,1.551674,-9.909278,3.610454],[-6.367114,-1.894112,-1.472064,3.307746,-0.771221,-4.882295,-2.272087,-9.601582,-8.537575,-5.899446,-4.126681,6.607834,3.256424,-7.256488],[0.927892,-0.804319,2.198746,-3.401674,-0.421058,-6.912943,8.028461,-6.861284,-1.786966,-2.031827,-1.113441,9.139150,-0.407075,9.104397],[1.992942,-7.593355,3.429044,-9.490086,7.705527,-6.845779,-1.290233,-4.193279,7.525186,-9.189331,5.157613,6.525909,7.799746,-0.564929],[7.276047,-9.091674,6.002562,-0.655550,8.101661,-9.181464,8.361837,-5.472016,2.121956,5.820789,4.558642,-6.312559,-4.851643,-5.102108],[7.594248,-1.849521,0.745377,2.878007,3.089743,1.541760,0.562666,6.812089,3.485099,-7.562505,-6.710309,5.436993,1.067497,-3.478343],[1.852728,-5.605494,4.188411,-4.368456,8.610644,-9.618150,0.916450,0.924860,9.771779,6.852639,-1.003120,9.731245,-8.828582,-4.750646]],[[-3.811795,6.426611,-1.841873,-9.617017,-1.944585,-1.895159,0.082954,-7.415930,-3.645578,4.976810,-4.362560,-2.447354,-1.180574,4.138863],[2.346801,3.484889,-5.065366,1.274515,-6.141413,8.697341,-7.542445,-0.602594,-3.827509,-4.565099,-4.813721,-7.928359,2.809300,6.934851],[-5.120442,-2.187869,-5.083148,0.348155,-9.352461,2.687468,1.355188,-2.689158,-2.057171,3.357467,1.586255,-3.465748,7.554193,6.882704],[6.319526,-3.060807,1.383320,1.720397,-2.999118,8.241569,-2.535102,6.940469,7.310635,3.868093,-1.695364,-6.260023,4.237294,3.745582],[8.946957,1.708506,5.153266,-1.590025,-4.926457,0.354452,-3.014143,8.580405,2.760399,-5.383066,-9.527700,8.448896,-0.029274,3.154396],[-1.262986,-0.923678,6.297666,-8.143022,-0.319158,4.583711,9.961501,5.907990,7.231074,-7.067389,-1.895482,1.318812,-7.574697,7.189562],[-0.140472,-1.002556,-7.187117,-6.755893,-4.445496,-5.203100,8.870597,9.284019,-2.975140,1.487960,-4.897388,4.425569,-1.906615,2.942847],[5.553300,-0.218023,4.595889,-6.258778,4.750854,2.346078,4.386251,-3.597975,-3.493385,4.172954,4.185326,-5.576353,-1.573704,-6.643165],[6.736452,-6.482882,-9.724949,-5.296555,8.905211,2.924198,-2.424938,6.674378,5.578284,-8.644292,3.051561,-1.041237,-9.317799,-7.194389],[-9.652430,-2.322319,6.707469,-1.770162,0.957167,1.206761,0.397459,4.603245,-7.713338,-3.715966,8.446455,6.447142,-7.055727,0.040190]],[[-9.207649,-4.297245,-0.099724,-0.277325,5.172747,9.112996,-5.279089,2.925332,-6.228000,7.898633,8.999281,-5.132137,-0.554682,-6.140583],[6.579054,-0.876949,7.427156,2.391688,0.983450,3.550515,-7.634427,3.108930,-6.119825,2.133816,4.739810,9.808829,-6.039860,9.751928],[9.892845,9.638496,9.121247,-9.916397,-7.006099,-5.418234,-1.856450,-0.737683,4.432090,5.193595,5.056570,-7.619652,0.011321,7.780497],[3.708740,-3.618185,-7.943428,1.329929,3.188569,8.641705,1.702155,9.164814,5.379414,6.484421,1.497774,-4.229946,4.649592,-4.040254],[-4.248651,-4.267390,-3.496295,-1.187588,-4.482927,1.715357,-2.508634,-2.101975,-8.049965,8.029204,1.831543,-0.285360,2.242636,2.245449],[8.076055,3.275227,-3.597486,6.424797,-3.078977,8.882883,-6.255135,2.396560,9.377416,-3.508246,0.319819,-7.262927,-3.685801,-7.706452],[7.483947,-6.768360,4.155037,5.317049,5.779153,-2.349575,-3.127664,9.408412,-0.047472,3.820018,-9.907094,-5.777995,0.986769,-7.321723],[8.089942,0.485277,0.135665,-0.490363,6.938681,-1.193170,-5.904849,1.691069,-4.304606,6.664360,2.382154,0.010140,9.960618,3.567086],[-5.545811,-9.403636,-0.321574,-8.006987,-3.504568,-2.459527,-0.998876,-6.950473,-4.082513,-5.260843,-8.125548,3.893889,-0.759623,8.310227],[-0.870146,7.605275,4.511912,5.441666,5.949299,5.181901,-9.181052,-8.387005,-7.595821,7.860900,-0.373830,9.030714,-4.294812,-3.187005]],[[9.270667,-1.795843,-2.988792,-1.453530,4.219768,-8.818439,-3.387941,-5.988067,9.321746,7.397942,-2.804885,-8.976393,-0.454511,8.560988],[0.963199,-1.860853,-4.555241,-6.318491,-1.167773,-6.498684,-9.622880,-0.170914,-6.076377,6.239470,0.983147,4.747994,-4.147133,-5.731919],[3.590893,9.240977,4.309754,-1.364882,-8.705416,4.031323,3.673678,-9.845961,-6.896332,-8.955806,-6.301646,-0.362756,1.730702,3.327330],[-7.777203,-9.734701,7.666182,-5.903938,3.405387,-0.320767,7.989826,-7.253258,1.353203,3.951384,-6.474887,-7.457182,5.862885,-4.631438],[-6.072023,-8.005700,-8.850547,1.496146,-5.764938,-4.995640,-3.343942,4.335779,-2.909082,-1.433450,6.825313,8.450735,-0.431217,-6.051179],[8.972231,-9.596157,-8.715356,-0.362897,7.000438,-6.685412,8.158477,-9.926907,-1.417882,0.987312,6.385623,-7.663584,4.269072,-0.919478],[-7.369659,-6.835146,-4.159481,8.624708,1.038208,3.501772,7.412164,7.852901,-4.136512,-6.488994,7.927165,-2.520124,-0.100406,2.758603],[-2.832655,1.083261,-9.163730,-6.456367,-9.055959,6.898212,8.571755,-7.989818,1.323972,8.896727,7.045652,-9.366588,-9.444626,-8.035700],[6.800635,-0.023504,5.016795,-4.976860,9.089751,-9.390689,8.981627,-2.025819,-9.480034,3.720488,-1.428708,-5.546399,9.905093,-0.920109],[5.259959,-6.362791,9.326283,-2.904656,-8.193067,-9.925037,-8.110918,3.948221,3.988985,-6.353847,-6.849066,1.823682,9.587999,6.220576]],[[-9.035701,-1.452540,-5.951148,-2.784053,5.059871,-1.370324,-4.547913,-5.232792,-5.387168,-8.355561,2.216732,8.326918,-0.276349,-6.563225],[-5.246523,-7.718999,7.057082,-5.357699,7.529467,0.481691,-3.414164,-7.879277,0.733788,9.484945,-8.323722,9.144220,-2.011681,-3.221216],[0.510844,-7.629673,-3.664243,-1.408445,6.180137,8.494998,1.718012,-0.418625,-2.591187,-9.339487,4.271055,4.363619,3.324090,4.783554],[-6.859949,2.730861,-9.607743,8.423295,-2.450947,-1.490646,5.199886,8.660702,5.018152,-3.498088,-5.755213,9.927246,-2.986776,-4.172126],[5.034914,5.336356,9.477319,8.656167,1.288449,-9.958817,-3.946964,0.242584,-1.225792,-3.910406,-3.996340,6.479194,-2.114172,-1.106814],[-6.654487,-3.425995,-2.440712,1.402092,-6.327022,8.565554,6.634335,-9.346685,9.375491,0.809870,-8.661377,8.774291,-6.464930,7.674580],[9.002343,4.201532,-5.228357,1.166525,-6.739372,-5.909445,7.849337,-8.095108,2.109329,-8.737053,-7.031454,-7.236162,1.774040,-0.709901],[7.739168,-1.158285,8.529691,-3.626474,-6.941322,0.683299,-1.058166,7.690856,5.345205,-1.207942,-7.705736,1.570687,8.609599,2.545345],[7.940784,-4.344365,-6.471818,6.565127,2.507989,3.912118,9.955567,-3.851287,2.806145,8.242051,3.284506,9.529593,-7.889474,-3.355714],[7.554523,9.930303,9.924393,2.706510,-2.123020,-2.803133,-7.268747,4.238823,-8.504483,6.014752,-0.551157,-2.299646,-3.567191,4.553009]]], dtype = "float64")#candidate|1768|(10, 10, 14)|const|float64
bop_1769 = relay.mod(var_1767.astype('float64'), const_1768.astype('float64')) # shape=(10, 10, 14)
output = relay.Tuple([bop_1769,])
output2 = relay.Tuple([bop_1769,])
func_1779 = relay.Function([var_1767,], output)
mod['func_1779'] = func_1779
mod = relay.transform.InferType()(mod)
var_1780 = relay.var("var_1780", dtype = "float64", shape = ())#candidate|1780|()|var|float64
output = func_1779(var_1780)
func_1781 = relay.Function([var_1780], output)
mutated_mod['func_1781'] = func_1781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_541_call = mod.get_global_var('func_541')
func_542_call = mutated_mod.get_global_var('func_542')
call_1849 = relay.TupleGetItem(func_541_call(), 0)
call_1850 = relay.TupleGetItem(func_542_call(), 0)
func_917_call = mod.get_global_var('func_917')
func_919_call = mutated_mod.get_global_var('func_919')
call_1863 = relay.TupleGetItem(func_917_call(), 0)
call_1864 = relay.TupleGetItem(func_919_call(), 0)
output = relay.Tuple([call_1849,call_1863,])
output2 = relay.Tuple([call_1850,call_1864,])
func_1867 = relay.Function([], output)
mod['func_1867'] = func_1867
mod = relay.transform.InferType()(mod)
mutated_mod['func_1867'] = func_1867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1867_call = mutated_mod.get_global_var('func_1867')
call_1868 = func_1867_call()
output = call_1868
func_1869 = relay.Function([], output)
mutated_mod['func_1869'] = func_1869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_1929 = relay.TupleGetItem(func_296_call(), 1)
call_1930 = relay.TupleGetItem(func_297_call(), 1)
output = call_1929
output2 = call_1930
func_1940 = relay.Function([], output)
mod['func_1940'] = func_1940
mod = relay.transform.InferType()(mod)
mutated_mod['func_1940'] = func_1940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mutated_mod.get_global_var('func_1940')
call_1941 = func_1940_call()
output = call_1941
func_1942 = relay.Function([], output)
mutated_mod['func_1942'] = func_1942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_344_call = mod.get_global_var('func_344')
func_345_call = mutated_mod.get_global_var('func_345')
call_1962 = relay.TupleGetItem(func_344_call(), 1)
call_1963 = relay.TupleGetItem(func_345_call(), 1)
output = relay.Tuple([call_1962,])
output2 = relay.Tuple([call_1963,])
func_1980 = relay.Function([], output)
mod['func_1980'] = func_1980
mod = relay.transform.InferType()(mod)
mutated_mod['func_1980'] = func_1980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1980_call = mutated_mod.get_global_var('func_1980')
call_1981 = func_1980_call()
output = call_1981
func_1982 = relay.Function([], output)
mutated_mod['func_1982'] = func_1982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1061_call = mod.get_global_var('func_1061')
func_1062_call = mutated_mod.get_global_var('func_1062')
call_2013 = relay.TupleGetItem(func_1061_call(), 2)
call_2014 = relay.TupleGetItem(func_1062_call(), 2)
var_2019 = relay.var("var_2019", dtype = "float32", shape = (3, 3, 2))#candidate|2019|(3, 3, 2)|var|float32
bop_2020 = relay.greater(call_2013.astype('bool'), var_2019.astype('bool')) # shape=(3, 3, 2)
bop_2023 = relay.greater(call_2014.astype('bool'), var_2019.astype('bool')) # shape=(3, 3, 2)
uop_2024 = relay.atanh(bop_2020.astype('float32')) # shape=(3, 3, 2)
uop_2026 = relay.atanh(bop_2023.astype('float32')) # shape=(3, 3, 2)
func_890_call = mod.get_global_var('func_890')
func_891_call = mutated_mod.get_global_var('func_891')
call_2033 = relay.TupleGetItem(func_890_call(), 2)
call_2034 = relay.TupleGetItem(func_891_call(), 2)
func_585_call = mod.get_global_var('func_585')
func_587_call = mutated_mod.get_global_var('func_587')
call_2040 = relay.TupleGetItem(func_585_call(), 1)
call_2041 = relay.TupleGetItem(func_587_call(), 1)
output = relay.Tuple([uop_2024,call_2033,call_2040,])
output2 = relay.Tuple([uop_2026,call_2034,call_2041,])
func_2054 = relay.Function([var_2019,], output)
mod['func_2054'] = func_2054
mod = relay.transform.InferType()(mod)
var_2055 = relay.var("var_2055", dtype = "float32", shape = (3, 3, 2))#candidate|2055|(3, 3, 2)|var|float32
output = func_2054(var_2055)
func_2056 = relay.Function([var_2055], output)
mutated_mod['func_2056'] = func_2056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_394_call = mutated_mod.get_global_var('func_394')
call_2058 = relay.TupleGetItem(func_393_call(), 1)
call_2059 = relay.TupleGetItem(func_394_call(), 1)
func_1762_call = mod.get_global_var('func_1762')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_2062 = relay.TupleGetItem(func_1762_call(), 1)
call_2063 = relay.TupleGetItem(func_1764_call(), 1)
output = relay.Tuple([call_2058,call_2062,])
output2 = relay.Tuple([call_2059,call_2063,])
func_2077 = relay.Function([], output)
mod['func_2077'] = func_2077
mod = relay.transform.InferType()(mod)
output = func_2077()
func_2078 = relay.Function([], output)
mutated_mod['func_2078'] = func_2078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_2111 = relay.TupleGetItem(func_296_call(), 1)
call_2112 = relay.TupleGetItem(func_297_call(), 1)
output = call_2111
output2 = call_2112
func_2124 = relay.Function([], output)
mod['func_2124'] = func_2124
mod = relay.transform.InferType()(mod)
mutated_mod['func_2124'] = func_2124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2124_call = mutated_mod.get_global_var('func_2124')
call_2125 = func_2124_call()
output = call_2125
func_2126 = relay.Function([], output)
mutated_mod['func_2126'] = func_2126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_344_call = mod.get_global_var('func_344')
func_345_call = mutated_mod.get_global_var('func_345')
call_2140 = relay.TupleGetItem(func_344_call(), 0)
call_2141 = relay.TupleGetItem(func_345_call(), 0)
output = relay.Tuple([call_2140,])
output2 = relay.Tuple([call_2141,])
func_2142 = relay.Function([], output)
mod['func_2142'] = func_2142
mod = relay.transform.InferType()(mod)
output = func_2142()
func_2143 = relay.Function([], output)
mutated_mod['func_2143'] = func_2143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2077_call = mod.get_global_var('func_2077')
func_2078_call = mutated_mod.get_global_var('func_2078')
call_2158 = relay.TupleGetItem(func_2077_call(), 1)
call_2159 = relay.TupleGetItem(func_2078_call(), 1)
output = call_2158
output2 = call_2159
func_2161 = relay.Function([], output)
mod['func_2161'] = func_2161
mod = relay.transform.InferType()(mod)
mutated_mod['func_2161'] = func_2161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2161_call = mutated_mod.get_global_var('func_2161')
call_2162 = func_2161_call()
output = call_2162
func_2163 = relay.Function([], output)
mutated_mod['func_2163'] = func_2163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_840_call = mod.get_global_var('func_840')
func_842_call = mutated_mod.get_global_var('func_842')
call_2180 = relay.TupleGetItem(func_840_call(), 0)
call_2181 = relay.TupleGetItem(func_842_call(), 0)
output = relay.Tuple([call_2180,])
output2 = relay.Tuple([call_2181,])
func_2218 = relay.Function([], output)
mod['func_2218'] = func_2218
mod = relay.transform.InferType()(mod)
mutated_mod['func_2218'] = func_2218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2218_call = mutated_mod.get_global_var('func_2218')
call_2219 = func_2218_call()
output = call_2219
func_2220 = relay.Function([], output)
mutated_mod['func_2220'] = func_2220
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2249 = relay.var("var_2249", dtype = "bool", shape = (9, 12, 12))#candidate|2249|(9, 12, 12)|var|bool
const_2250 = relay.const([[[True,True,True,False,False,True,False,True,False,True,False,False],[False,True,True,False,True,True,False,True,False,False,False,False],[True,False,False,False,True,False,True,False,True,False,False,False],[True,False,True,True,False,True,True,False,True,False,False,False],[True,True,True,False,True,False,False,True,False,False,True,True],[False,False,True,True,False,False,True,True,False,True,False,False],[False,True,False,True,True,True,True,True,False,True,True,True],[True,True,False,True,True,False,False,True,False,True,False,True],[True,False,False,False,True,True,False,True,False,True,True,False],[False,False,True,False,True,False,True,False,True,False,True,False],[False,True,True,False,True,True,True,False,True,False,False,False],[True,True,False,True,False,True,True,False,True,False,False,True]],[[False,True,True,True,True,True,True,True,False,False,False,True],[False,True,False,True,True,False,False,False,True,False,False,True],[True,True,True,False,False,True,True,False,True,True,False,False],[False,True,False,False,False,False,False,False,True,False,True,True],[False,True,True,False,True,True,True,False,True,True,True,True],[False,False,True,True,True,True,False,True,True,False,False,True],[False,False,True,True,False,False,False,False,False,False,False,True],[True,False,False,False,True,True,True,True,True,True,True,True],[False,True,False,True,True,False,False,True,False,True,False,False],[False,True,True,False,True,True,True,False,True,True,True,False],[False,False,False,False,True,True,True,False,False,True,True,True],[False,False,False,False,True,False,True,True,True,False,True,False]],[[True,True,True,True,False,False,True,True,False,True,True,False],[False,False,False,False,True,True,True,True,True,True,False,True],[False,True,False,True,True,False,False,False,True,True,True,True],[True,True,False,True,False,True,True,True,True,True,True,True],[True,True,False,False,False,False,True,False,True,False,False,False],[False,False,True,True,True,False,False,False,True,True,True,False],[False,True,True,False,False,False,True,True,True,True,False,False],[False,True,False,True,True,False,False,True,False,True,False,True],[True,True,True,True,False,True,True,False,False,False,False,False],[False,True,False,False,True,False,False,True,True,False,False,True],[True,False,False,True,True,True,True,True,False,False,False,False],[True,True,False,True,True,True,False,True,False,False,True,True]],[[False,True,False,True,False,True,False,True,True,True,False,True],[False,True,False,False,False,False,False,True,True,False,True,False],[True,True,True,False,True,True,True,True,False,False,False,False],[True,True,True,False,False,False,True,False,True,True,False,True],[True,False,True,False,False,False,False,False,True,False,False,False],[True,True,True,True,True,True,False,False,False,True,True,False],[True,False,False,True,False,False,False,True,False,True,False,True],[True,False,True,False,False,True,False,True,False,True,True,False],[True,True,False,True,False,True,False,False,False,False,True,False],[True,True,True,True,True,True,False,False,False,True,True,False],[False,True,False,True,True,True,True,False,False,True,True,False],[True,True,False,True,False,True,True,True,True,False,False,False]],[[False,True,False,False,False,True,False,True,True,False,False,False],[True,True,False,True,False,True,False,True,True,False,False,True],[False,True,False,True,False,False,True,False,True,True,False,False],[True,False,True,False,True,True,False,False,False,False,False,False],[True,False,False,False,False,False,True,False,False,True,True,False],[False,False,False,True,False,False,True,True,False,False,True,True],[True,True,False,True,True,False,False,False,False,False,True,False],[False,False,True,False,False,False,False,False,True,False,True,True],[False,True,False,True,True,True,False,True,False,False,False,True],[False,False,True,False,False,False,True,True,True,False,True,True],[False,False,True,True,False,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True]],[[False,True,False,True,True,False,False,True,False,True,True,False],[False,True,True,True,False,True,False,True,False,False,True,True],[True,True,False,False,True,False,True,False,True,False,True,False],[False,False,False,False,True,True,False,True,False,False,True,False],[True,True,False,True,False,True,False,True,False,True,True,False],[True,False,False,True,False,True,True,False,True,True,False,True],[False,True,False,True,True,True,True,False,True,True,False,True],[False,False,False,True,True,True,True,True,True,True,False,False],[False,True,False,False,True,True,True,True,False,True,False,True],[True,False,True,False,True,True,True,False,False,True,True,True],[False,False,False,True,True,False,True,True,False,False,True,True],[True,False,False,True,False,True,False,True,True,True,True,False]],[[True,False,False,True,True,True,False,True,True,True,False,False],[True,False,False,True,False,True,False,True,False,True,False,False],[False,False,True,True,True,False,True,False,False,False,True,True],[True,False,False,True,True,False,True,False,False,True,False,False],[True,False,True,True,True,True,True,True,True,False,False,True],[False,False,True,False,False,True,True,True,True,True,False,False],[True,False,False,False,True,False,False,False,True,False,True,False],[True,False,False,True,False,False,False,False,False,True,False,False],[False,True,False,True,False,False,True,False,False,False,False,False],[False,False,False,True,False,False,False,False,False,False,True,True],[False,True,True,True,False,False,True,True,True,True,False,False],[False,False,False,False,False,False,False,False,False,True,False,True]],[[True,False,True,True,False,False,False,False,True,False,True,True],[False,True,False,True,False,True,True,False,True,True,True,True],[True,True,True,False,False,True,True,True,True,False,True,True],[False,True,False,True,True,True,False,True,False,True,True,True],[False,False,True,True,False,False,False,True,False,True,True,False],[True,False,False,False,False,True,False,False,False,False,True,False],[True,False,True,False,True,False,True,True,True,False,False,True],[True,False,False,True,True,False,True,False,False,True,True,True],[False,True,True,True,True,True,True,False,True,False,False,False],[True,True,True,False,False,True,True,True,True,True,False,False],[True,True,True,False,True,False,True,True,True,False,False,False],[True,True,False,False,False,True,False,True,False,True,True,False]],[[False,False,True,True,True,True,False,True,True,True,True,False],[True,False,True,False,False,False,False,False,True,False,False,True],[True,True,False,False,False,True,False,True,True,False,False,True],[True,False,False,False,True,True,False,False,True,False,False,True],[False,False,True,True,True,False,True,False,True,True,False,True],[True,True,False,False,True,True,True,False,True,True,True,True],[False,True,True,True,True,False,True,True,False,False,True,True],[False,False,False,True,True,False,True,False,True,True,True,False],[False,False,True,False,False,False,True,False,True,False,False,True],[False,True,False,True,True,True,False,False,True,False,True,True],[True,False,True,False,False,False,True,False,True,False,False,True],[False,True,True,True,False,True,False,False,False,True,True,False]]], dtype = "bool")#candidate|2250|(9, 12, 12)|const|bool
bop_2251 = relay.logical_or(var_2249.astype('bool'), relay.reshape(const_2250.astype('bool'), relay.shape_of(var_2249))) # shape=(9, 12, 12)
bop_2254 = relay.add(bop_2251.astype('uint32'), relay.reshape(const_2250.astype('uint32'), relay.shape_of(bop_2251))) # shape=(9, 12, 12)
var_2258 = relay.var("var_2258", dtype = "bool", shape = (9, 12, 12))#candidate|2258|(9, 12, 12)|var|bool
bop_2259 = relay.equal(bop_2251.astype('bool'), relay.reshape(var_2258.astype('bool'), relay.shape_of(bop_2251))) # shape=(9, 12, 12)
uop_2267 = relay.cosh(var_2249.astype('float64')) # shape=(9, 12, 12)
output = relay.Tuple([bop_2254,bop_2259,uop_2267,])
output2 = relay.Tuple([bop_2254,bop_2259,uop_2267,])
func_2274 = relay.Function([var_2249,var_2258,], output)
mod['func_2274'] = func_2274
mod = relay.transform.InferType()(mod)
mutated_mod['func_2274'] = func_2274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2274_call = mutated_mod.get_global_var('func_2274')
var_2276 = relay.var("var_2276", dtype = "bool", shape = (9, 12, 12))#candidate|2276|(9, 12, 12)|var|bool
var_2277 = relay.var("var_2277", dtype = "bool", shape = (9, 12, 12))#candidate|2277|(9, 12, 12)|var|bool
call_2275 = func_2274_call(var_2276,var_2277,)
output = call_2275
func_2278 = relay.Function([var_2276,var_2277,], output)
mutated_mod['func_2278'] = func_2278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1014_call = mod.get_global_var('func_1014')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_2353 = func_1014_call()
call_2354 = func_1014_call()
output = relay.Tuple([call_2353,])
output2 = relay.Tuple([call_2354,])
func_2359 = relay.Function([], output)
mod['func_2359'] = func_2359
mod = relay.transform.InferType()(mod)
output = func_2359()
func_2360 = relay.Function([], output)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_2387 = func_1940_call()
call_2388 = func_1940_call()
output = call_2387
output2 = call_2388
func_2395 = relay.Function([], output)
mod['func_2395'] = func_2395
mod = relay.transform.InferType()(mod)
output = func_2395()
func_2396 = relay.Function([], output)
mutated_mod['func_2396'] = func_2396
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2416 = relay.var("var_2416", dtype = "float32", shape = (11, 7, 6))#candidate|2416|(11, 7, 6)|var|float32
uop_2417 = relay.atanh(var_2416.astype('float32')) # shape=(11, 7, 6)
func_1762_call = mod.get_global_var('func_1762')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_2420 = relay.TupleGetItem(func_1762_call(), 0)
call_2421 = relay.TupleGetItem(func_1764_call(), 0)
func_1061_call = mod.get_global_var('func_1061')
func_1062_call = mutated_mod.get_global_var('func_1062')
call_2454 = relay.TupleGetItem(func_1061_call(), 0)
call_2455 = relay.TupleGetItem(func_1062_call(), 0)
bop_2464 = relay.greater(uop_2417.astype('bool'), relay.reshape(var_2416.astype('bool'), relay.shape_of(uop_2417))) # shape=(11, 7, 6)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_2468 = relay.TupleGetItem(func_2359_call(), 0)
call_2469 = relay.TupleGetItem(func_2360_call(), 0)
output = relay.Tuple([call_2420,call_2454,bop_2464,call_2468,])
output2 = relay.Tuple([call_2421,call_2455,bop_2464,call_2469,])
func_2472 = relay.Function([var_2416,], output)
mod['func_2472'] = func_2472
mod = relay.transform.InferType()(mod)
mutated_mod['func_2472'] = func_2472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2473 = relay.var("var_2473", dtype = "float32", shape = (11, 7, 6))#candidate|2473|(11, 7, 6)|var|float32
func_2472_call = mutated_mod.get_global_var('func_2472')
call_2474 = func_2472_call(var_2473)
output = call_2474
func_2475 = relay.Function([var_2473], output)
mutated_mod['func_2475'] = func_2475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2395_call = mod.get_global_var('func_2395')
func_2396_call = mutated_mod.get_global_var('func_2396')
call_2488 = func_2395_call()
call_2489 = func_2395_call()
func_2218_call = mod.get_global_var('func_2218')
func_2220_call = mutated_mod.get_global_var('func_2220')
call_2496 = relay.TupleGetItem(func_2218_call(), 0)
call_2497 = relay.TupleGetItem(func_2220_call(), 0)
bop_2507 = relay.subtract(call_2496.astype('uint8'), relay.reshape(call_2488.astype('uint8'), relay.shape_of(call_2496))) # shape=(1, 3, 1)
bop_2510 = relay.subtract(call_2497.astype('uint8'), relay.reshape(call_2489.astype('uint8'), relay.shape_of(call_2497))) # shape=(1, 3, 1)
bop_2511 = relay.less_equal(bop_2507.astype('bool'), relay.reshape(call_2496.astype('bool'), relay.shape_of(bop_2507))) # shape=(1, 3, 1)
bop_2514 = relay.less_equal(bop_2510.astype('bool'), relay.reshape(call_2497.astype('bool'), relay.shape_of(bop_2510))) # shape=(1, 3, 1)
output = relay.Tuple([bop_2511,])
output2 = relay.Tuple([bop_2514,])
func_2515 = relay.Function([], output)
mod['func_2515'] = func_2515
mod = relay.transform.InferType()(mod)
mutated_mod['func_2515'] = func_2515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2515_call = mutated_mod.get_global_var('func_2515')
call_2516 = func_2515_call()
output = call_2516
func_2517 = relay.Function([], output)
mutated_mod['func_2517'] = func_2517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_604_call = mod.get_global_var('func_604')
func_605_call = mutated_mod.get_global_var('func_605')
call_2594 = relay.TupleGetItem(func_604_call(), 0)
call_2595 = relay.TupleGetItem(func_605_call(), 0)
output = call_2594
output2 = call_2595
func_2603 = relay.Function([], output)
mod['func_2603'] = func_2603
mod = relay.transform.InferType()(mod)
mutated_mod['func_2603'] = func_2603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2603_call = mutated_mod.get_global_var('func_2603')
call_2604 = func_2603_call()
output = call_2604
func_2605 = relay.Function([], output)
mutated_mod['func_2605'] = func_2605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_890_call = mod.get_global_var('func_890')
func_891_call = mutated_mod.get_global_var('func_891')
call_2630 = relay.TupleGetItem(func_890_call(), 1)
call_2631 = relay.TupleGetItem(func_891_call(), 1)
var_2651 = relay.var("var_2651", dtype = "float64", shape = (15, 3, 10))#candidate|2651|(15, 3, 10)|var|float64
bop_2652 = relay.not_equal(call_2630.astype('bool'), var_2651.astype('bool')) # shape=(15, 3, 10)
bop_2655 = relay.not_equal(call_2631.astype('bool'), var_2651.astype('bool')) # shape=(15, 3, 10)
output = relay.Tuple([bop_2652,])
output2 = relay.Tuple([bop_2655,])
func_2663 = relay.Function([var_2651,], output)
mod['func_2663'] = func_2663
mod = relay.transform.InferType()(mod)
var_2664 = relay.var("var_2664", dtype = "float64", shape = (15, 3, 10))#candidate|2664|(15, 3, 10)|var|float64
output = func_2663(var_2664)
func_2665 = relay.Function([var_2664], output)
mutated_mod['func_2665'] = func_2665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_2715 = relay.TupleGetItem(func_506_call(), 0)
call_2716 = relay.TupleGetItem(func_507_call(), 0)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_2717 = func_1940_call()
call_2718 = func_1940_call()
output = relay.Tuple([call_2715,call_2717,])
output2 = relay.Tuple([call_2716,call_2718,])
func_2726 = relay.Function([], output)
mod['func_2726'] = func_2726
mod = relay.transform.InferType()(mod)
output = func_2726()
func_2727 = relay.Function([], output)
mutated_mod['func_2727'] = func_2727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2124_call = mod.get_global_var('func_2124')
func_2126_call = mutated_mod.get_global_var('func_2126')
call_2744 = func_2124_call()
call_2745 = func_2124_call()
output = call_2744
output2 = call_2745
func_2746 = relay.Function([], output)
mod['func_2746'] = func_2746
mod = relay.transform.InferType()(mod)
mutated_mod['func_2746'] = func_2746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2746_call = mutated_mod.get_global_var('func_2746')
call_2747 = func_2746_call()
output = call_2747
func_2748 = relay.Function([], output)
mutated_mod['func_2748'] = func_2748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_917_call = mod.get_global_var('func_917')
func_919_call = mutated_mod.get_global_var('func_919')
call_2762 = relay.TupleGetItem(func_917_call(), 0)
call_2763 = relay.TupleGetItem(func_919_call(), 0)
func_1762_call = mod.get_global_var('func_1762')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_2770 = relay.TupleGetItem(func_1762_call(), 1)
call_2771 = relay.TupleGetItem(func_1764_call(), 1)
output = relay.Tuple([call_2762,call_2770,])
output2 = relay.Tuple([call_2763,call_2771,])
func_2776 = relay.Function([], output)
mod['func_2776'] = func_2776
mod = relay.transform.InferType()(mod)
output = func_2776()
func_2777 = relay.Function([], output)
mutated_mod['func_2777'] = func_2777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1061_call = mod.get_global_var('func_1061')
func_1062_call = mutated_mod.get_global_var('func_1062')
call_2799 = relay.TupleGetItem(func_1061_call(), 2)
call_2800 = relay.TupleGetItem(func_1062_call(), 2)
output = relay.Tuple([call_2799,])
output2 = relay.Tuple([call_2800,])
func_2813 = relay.Function([], output)
mod['func_2813'] = func_2813
mod = relay.transform.InferType()(mod)
output = func_2813()
func_2814 = relay.Function([], output)
mutated_mod['func_2814'] = func_2814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2776_call = mod.get_global_var('func_2776')
func_2777_call = mutated_mod.get_global_var('func_2777')
call_2853 = relay.TupleGetItem(func_2776_call(), 1)
call_2854 = relay.TupleGetItem(func_2777_call(), 1)
var_2879 = relay.var("var_2879", dtype = "float64", shape = (10, 3, 12))#candidate|2879|(10, 3, 12)|var|float64
bop_2880 = relay.add(call_2853.astype('uint32'), var_2879.astype('uint32')) # shape=(10, 3, 12)
bop_2883 = relay.add(call_2854.astype('uint32'), var_2879.astype('uint32')) # shape=(10, 3, 12)
var_2899 = relay.var("var_2899", dtype = "uint32", shape = (10, 3, 12))#candidate|2899|(10, 3, 12)|var|uint32
bop_2900 = relay.logical_and(bop_2880.astype('bool'), relay.reshape(var_2899.astype('bool'), relay.shape_of(bop_2880))) # shape=(10, 3, 12)
bop_2903 = relay.logical_and(bop_2883.astype('bool'), relay.reshape(var_2899.astype('bool'), relay.shape_of(bop_2883))) # shape=(10, 3, 12)
var_2910 = relay.var("var_2910", dtype = "uint32", shape = (10, 3, 12))#candidate|2910|(10, 3, 12)|var|uint32
bop_2911 = relay.maximum(bop_2880.astype('int32'), relay.reshape(var_2910.astype('int32'), relay.shape_of(bop_2880))) # shape=(10, 3, 12)
bop_2914 = relay.maximum(bop_2883.astype('int32'), relay.reshape(var_2910.astype('int32'), relay.shape_of(bop_2883))) # shape=(10, 3, 12)
func_2218_call = mod.get_global_var('func_2218')
func_2220_call = mutated_mod.get_global_var('func_2220')
call_2915 = relay.TupleGetItem(func_2218_call(), 0)
call_2916 = relay.TupleGetItem(func_2220_call(), 0)
output = relay.Tuple([bop_2900,bop_2911,call_2915,])
output2 = relay.Tuple([bop_2903,bop_2914,call_2916,])
func_2920 = relay.Function([var_2879,var_2899,var_2910,], output)
mod['func_2920'] = func_2920
mod = relay.transform.InferType()(mod)
mutated_mod['func_2920'] = func_2920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2920_call = mutated_mod.get_global_var('func_2920')
var_2922 = relay.var("var_2922", dtype = "float64", shape = (10, 3, 12))#candidate|2922|(10, 3, 12)|var|float64
var_2923 = relay.var("var_2923", dtype = "uint32", shape = (10, 3, 12))#candidate|2923|(10, 3, 12)|var|uint32
var_2924 = relay.var("var_2924", dtype = "uint32", shape = (10, 3, 12))#candidate|2924|(10, 3, 12)|var|uint32
call_2921 = func_2920_call(var_2922,var_2923,var_2924,)
output = call_2921
func_2925 = relay.Function([var_2922,var_2923,var_2924,], output)
mutated_mod['func_2925'] = func_2925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_3014 = relay.TupleGetItem(func_296_call(), 0)
call_3015 = relay.TupleGetItem(func_297_call(), 0)
uop_3020 = relay.sqrt(call_3014.astype('float32')) # shape=(1, 3, 1)
uop_3022 = relay.sqrt(call_3015.astype('float32')) # shape=(1, 3, 1)
bop_3026 = relay.left_shift(call_3014.astype('int16'), relay.reshape(uop_3020.astype('int16'), relay.shape_of(call_3014))) # shape=(1, 3, 1)
bop_3029 = relay.left_shift(call_3015.astype('int16'), relay.reshape(uop_3022.astype('int16'), relay.shape_of(call_3015))) # shape=(1, 3, 1)
bop_3049 = relay.bitwise_or(bop_3026.astype('uint8'), relay.reshape(call_3014.astype('uint8'), relay.shape_of(bop_3026))) # shape=(1, 3, 1)
bop_3052 = relay.bitwise_or(bop_3029.astype('uint8'), relay.reshape(call_3015.astype('uint8'), relay.shape_of(bop_3029))) # shape=(1, 3, 1)
output = bop_3049
output2 = bop_3052
func_3053 = relay.Function([], output)
mod['func_3053'] = func_3053
mod = relay.transform.InferType()(mod)
mutated_mod['func_3053'] = func_3053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3053_call = mutated_mod.get_global_var('func_3053')
call_3054 = func_3053_call()
output = call_3054
func_3055 = relay.Function([], output)
mutated_mod['func_3055'] = func_3055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1014_call = mod.get_global_var('func_1014')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_3200 = func_1014_call()
call_3201 = func_1014_call()
func_1779_call = mod.get_global_var('func_1779')
func_1781_call = mutated_mod.get_global_var('func_1781')
var_3213 = relay.var("var_3213", dtype = "float64", shape = ())#candidate|3213|()|var|float64
call_3212 = relay.TupleGetItem(func_1779_call(relay.reshape(var_3213.astype('float64'), [])), 0)
call_3214 = relay.TupleGetItem(func_1781_call(relay.reshape(var_3213.astype('float64'), [])), 0)
bop_3217 = relay.power(var_3213.astype('float32'), call_3200.astype('float32')) # shape=(1, 3, 1)
bop_3220 = relay.power(var_3213.astype('float32'), call_3201.astype('float32')) # shape=(1, 3, 1)
output = relay.Tuple([call_3212,bop_3217,])
output2 = relay.Tuple([call_3214,bop_3220,])
func_3223 = relay.Function([var_3213,], output)
mod['func_3223'] = func_3223
mod = relay.transform.InferType()(mod)
mutated_mod['func_3223'] = func_3223
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3224 = relay.var("var_3224", dtype = "float64", shape = ())#candidate|3224|()|var|float64
func_3223_call = mutated_mod.get_global_var('func_3223')
call_3225 = func_3223_call(var_3224)
output = call_3225
func_3226 = relay.Function([var_3224], output)
mutated_mod['func_3226'] = func_3226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2077_call = mod.get_global_var('func_2077')
func_2078_call = mutated_mod.get_global_var('func_2078')
call_3228 = relay.TupleGetItem(func_2077_call(), 0)
call_3229 = relay.TupleGetItem(func_2078_call(), 0)
var_3234 = relay.var("var_3234", dtype = "float64", shape = (14, 3, 8))#candidate|3234|(14, 3, 8)|var|float64
bop_3235 = relay.greater(call_3228.astype('bool'), var_3234.astype('bool')) # shape=(14, 3, 8)
bop_3238 = relay.greater(call_3229.astype('bool'), var_3234.astype('bool')) # shape=(14, 3, 8)
const_3243 = relay.const([[[4.213880,-2.764533,-4.524620,6.808914,-5.304801,-9.396998,-2.547422,-8.808590],[-7.618887,5.959089,-9.333628,4.219585,-6.701428,4.204515,7.744838,1.453522],[-5.574708,-1.582701,-4.009068,-5.850315,-3.616144,-3.980296,-0.423018,9.417088]],[[9.033898,-3.139830,0.407864,0.456055,0.372402,8.343836,6.942712,-4.661593],[-0.826202,9.885811,-8.402055,-7.029770,-6.476152,5.626458,3.680802,6.110007],[3.089850,-0.720025,1.209995,2.856099,-9.823611,5.102293,1.467248,5.900065]],[[9.212898,-0.077616,3.347474,-4.372019,6.502331,-5.748501,-3.288456,5.117866],[0.870210,9.829009,-5.473444,-7.147567,6.192350,-3.836393,4.869276,-6.067072],[-0.216249,-3.224260,1.175922,7.997097,-2.723141,5.656075,4.278530,9.878308]],[[-6.039344,0.749473,0.452074,2.074828,-4.640638,6.126644,-1.667648,-1.764133],[0.005208,-6.014018,3.466586,8.798001,5.430022,0.742760,-3.432031,-2.359582],[3.175425,5.223386,8.939366,5.090853,-3.392906,7.639320,-5.879263,-4.584112]],[[-3.715997,4.645737,-2.844039,9.803511,2.472419,6.241255,6.793754,1.642263],[7.825547,3.814474,8.185207,-0.767057,-0.239044,-5.722272,8.598266,-8.432128],[3.931157,-2.342344,-1.396534,-7.218655,-1.337870,0.573382,9.419738,-5.890784]],[[7.522237,3.637671,-9.049895,3.038023,4.468388,9.905851,-3.676813,-3.950266],[3.454759,1.807769,-6.321925,-4.167018,7.321801,2.207505,-1.871337,-0.738018],[1.609957,-7.505374,3.488646,-0.583509,-3.483406,-7.787420,7.527289,-5.833554]],[[8.515967,7.069225,8.117176,-3.712291,4.259191,5.106623,7.878852,-6.980289],[4.513285,-7.518580,-5.336176,1.261623,-4.207940,6.125838,-3.966396,4.509820],[0.332621,-0.458740,-3.365038,-7.315277,-7.242963,1.399845,3.122348,-8.806128]],[[-6.772877,6.063238,-5.343857,3.035876,-5.814522,-4.627083,5.047599,-0.492944],[-5.122065,6.841103,8.430737,6.589052,-6.471328,0.414583,-2.713007,-3.375055],[-5.727696,5.772655,0.235716,-4.472550,5.245891,-6.744675,-8.537668,9.080624]],[[5.559617,3.257012,-6.674709,-1.991258,9.913529,-4.149655,-1.545730,-7.405488],[8.466117,0.576269,6.996399,-2.524020,-4.091409,0.233342,-6.862804,-4.005261],[4.515761,-7.221991,-5.474219,-8.516324,1.237767,4.156887,-4.759074,-9.452235]],[[3.289965,-5.800575,0.932999,6.281253,9.447026,-1.332425,7.915603,-4.387290],[-9.333182,2.003898,1.342355,-3.859518,-5.594714,-3.491511,-1.796031,-9.823704],[-6.610152,-3.034773,-8.958071,-4.675686,-1.459779,9.339195,1.790399,-3.808865]],[[-7.290401,-4.753097,-3.654414,-7.956169,-7.465154,0.917426,-0.922805,-9.438494],[-7.364799,-7.468436,-9.214207,-3.364149,-8.820115,-9.005282,7.497912,4.521796],[-0.983205,-0.190686,4.297728,-0.312835,6.785445,-4.671245,5.576826,1.061516]],[[5.054599,-0.805841,-2.519975,-4.367905,-9.582022,-9.701240,2.872764,-4.206688],[4.883237,-1.432956,5.050837,-5.996359,-9.607588,-3.616961,2.467176,3.339198],[-6.399427,-1.178249,8.037037,0.214916,0.699204,2.412672,9.417252,1.547871]],[[-4.540564,0.437939,-2.725681,5.568202,-4.889575,-8.774623,7.864820,-4.987891],[-0.433710,-5.309242,0.909883,1.262789,0.099005,-9.528118,-8.706962,5.393707],[4.158747,9.468743,-3.555237,3.047609,-8.646028,-8.670121,2.952812,6.488191]],[[6.647965,8.302770,9.438915,7.588408,-7.744008,-7.088670,7.663170,1.328282],[-5.666955,-4.623395,7.354509,-7.513090,-9.397131,9.566023,3.316202,4.863722],[-0.797520,-8.824794,9.898230,-6.799180,1.366560,7.496309,-7.331353,4.118107]]], dtype = "float64")#candidate|3243|(14, 3, 8)|const|float64
bop_3244 = relay.not_equal(var_3234.astype('bool'), relay.reshape(const_3243.astype('bool'), relay.shape_of(var_3234))) # shape=(14, 3, 8)
output = relay.Tuple([bop_3235,bop_3244,])
output2 = relay.Tuple([bop_3238,bop_3244,])
func_3247 = relay.Function([var_3234,], output)
mod['func_3247'] = func_3247
mod = relay.transform.InferType()(mod)
mutated_mod['func_3247'] = func_3247
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3248 = relay.var("var_3248", dtype = "float64", shape = (14, 3, 8))#candidate|3248|(14, 3, 8)|var|float64
func_3247_call = mutated_mod.get_global_var('func_3247')
call_3249 = func_3247_call(var_3248)
output = call_3249
func_3250 = relay.Function([var_3248], output)
mutated_mod['func_3250'] = func_3250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mod.get_global_var('func_1170')
func_1171_call = mutated_mod.get_global_var('func_1171')
call_3284 = func_1170_call()
call_3285 = func_1170_call()
func_2054_call = mod.get_global_var('func_2054')
func_2056_call = mutated_mod.get_global_var('func_2056')
var_3293 = relay.var("var_3293", dtype = "float32", shape = (18,))#candidate|3293|(18,)|var|float32
call_3292 = relay.TupleGetItem(func_2054_call(relay.reshape(var_3293.astype('float32'), [3, 3, 2])), 2)
call_3294 = relay.TupleGetItem(func_2056_call(relay.reshape(var_3293.astype('float32'), [3, 3, 2])), 2)
func_541_call = mod.get_global_var('func_541')
func_542_call = mutated_mod.get_global_var('func_542')
call_3297 = relay.TupleGetItem(func_541_call(), 0)
call_3298 = relay.TupleGetItem(func_542_call(), 0)
output = relay.Tuple([call_3284,call_3292,var_3293,call_3297,])
output2 = relay.Tuple([call_3285,call_3294,var_3293,call_3298,])
func_3300 = relay.Function([var_3293,], output)
mod['func_3300'] = func_3300
mod = relay.transform.InferType()(mod)
var_3301 = relay.var("var_3301", dtype = "float32", shape = (18,))#candidate|3301|(18,)|var|float32
output = func_3300(var_3301)
func_3302 = relay.Function([var_3301], output)
mutated_mod['func_3302'] = func_3302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_394_call = mutated_mod.get_global_var('func_394')
call_3309 = relay.TupleGetItem(func_393_call(), 0)
call_3310 = relay.TupleGetItem(func_394_call(), 0)
func_2077_call = mod.get_global_var('func_2077')
func_2078_call = mutated_mod.get_global_var('func_2078')
call_3311 = relay.TupleGetItem(func_2077_call(), 1)
call_3312 = relay.TupleGetItem(func_2078_call(), 1)
func_3223_call = mod.get_global_var('func_3223')
func_3226_call = mutated_mod.get_global_var('func_3226')
const_3330 = relay.const(-7.985231, dtype = "float64")#candidate|3330|()|const|float64
call_3329 = relay.TupleGetItem(func_3223_call(relay.reshape(const_3330.astype('float64'), [])), 1)
call_3331 = relay.TupleGetItem(func_3226_call(relay.reshape(const_3330.astype('float64'), [])), 1)
bop_3336 = relay.greater(call_3309.astype('bool'), relay.reshape(call_3311.astype('bool'), relay.shape_of(call_3309))) # shape=(1, 3, 1)
bop_3339 = relay.greater(call_3310.astype('bool'), relay.reshape(call_3312.astype('bool'), relay.shape_of(call_3310))) # shape=(1, 3, 1)
func_1014_call = mod.get_global_var('func_1014')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_3340 = func_1014_call()
call_3341 = func_1014_call()
func_604_call = mod.get_global_var('func_604')
func_605_call = mutated_mod.get_global_var('func_605')
call_3353 = relay.TupleGetItem(func_604_call(), 0)
call_3354 = relay.TupleGetItem(func_605_call(), 0)
func_780_call = mod.get_global_var('func_780')
func_781_call = mutated_mod.get_global_var('func_781')
call_3371 = relay.TupleGetItem(func_780_call(), 0)
call_3372 = relay.TupleGetItem(func_781_call(), 0)
output = relay.Tuple([call_3329,const_3330,bop_3336,call_3340,call_3353,call_3371,])
output2 = relay.Tuple([call_3331,const_3330,bop_3339,call_3341,call_3354,call_3372,])
func_3384 = relay.Function([], output)
mod['func_3384'] = func_3384
mod = relay.transform.InferType()(mod)
mutated_mod['func_3384'] = func_3384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3384_call = mutated_mod.get_global_var('func_3384')
call_3385 = func_3384_call()
output = call_3385
func_3386 = relay.Function([], output)
mutated_mod['func_3386'] = func_3386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1867_call = mod.get_global_var('func_1867')
func_1869_call = mutated_mod.get_global_var('func_1869')
call_3467 = relay.TupleGetItem(func_1867_call(), 0)
call_3468 = relay.TupleGetItem(func_1869_call(), 0)
output = relay.Tuple([call_3467,])
output2 = relay.Tuple([call_3468,])
func_3473 = relay.Function([], output)
mod['func_3473'] = func_3473
mod = relay.transform.InferType()(mod)
mutated_mod['func_3473'] = func_3473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3473_call = mutated_mod.get_global_var('func_3473')
call_3474 = func_3473_call()
output = call_3474
func_3475 = relay.Function([], output)
mutated_mod['func_3475'] = func_3475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3484 = relay.var("var_3484", dtype = "float32", shape = (6, 2, 3))#candidate|3484|(6, 2, 3)|var|float32
uop_3485 = relay.cosh(var_3484.astype('float32')) # shape=(6, 2, 3)
func_2515_call = mod.get_global_var('func_2515')
func_2517_call = mutated_mod.get_global_var('func_2517')
call_3502 = relay.TupleGetItem(func_2515_call(), 0)
call_3503 = relay.TupleGetItem(func_2517_call(), 0)
func_3300_call = mod.get_global_var('func_3300')
func_3302_call = mutated_mod.get_global_var('func_3302')
var_3505 = relay.var("var_3505", dtype = "float32", shape = (1, 18))#candidate|3505|(1, 18)|var|float32
call_3504 = relay.TupleGetItem(func_3300_call(relay.reshape(var_3505.astype('float32'), [18,])), 1)
call_3506 = relay.TupleGetItem(func_3302_call(relay.reshape(var_3505.astype('float32'), [18,])), 1)
output = relay.Tuple([uop_3485,call_3502,call_3504,var_3505,])
output2 = relay.Tuple([uop_3485,call_3503,call_3506,var_3505,])
func_3509 = relay.Function([var_3484,var_3505,], output)
mod['func_3509'] = func_3509
mod = relay.transform.InferType()(mod)
mutated_mod['func_3509'] = func_3509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3509_call = mutated_mod.get_global_var('func_3509')
var_3511 = relay.var("var_3511", dtype = "float32", shape = (6, 2, 3))#candidate|3511|(6, 2, 3)|var|float32
var_3512 = relay.var("var_3512", dtype = "float32", shape = (1, 18))#candidate|3512|(1, 18)|var|float32
call_3510 = func_3509_call(var_3511,var_3512,)
output = call_3510
func_3513 = relay.Function([var_3511,var_3512,], output)
mutated_mod['func_3513'] = func_3513
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3532 = relay.var("var_3532", dtype = "float64", shape = (16, 11, 8))#candidate|3532|(16, 11, 8)|var|float64
uop_3533 = relay.atanh(var_3532.astype('float64')) # shape=(16, 11, 8)
uop_3542 = relay.sinh(var_3532.astype('float32')) # shape=(16, 11, 8)
output = relay.Tuple([uop_3533,uop_3542,])
output2 = relay.Tuple([uop_3533,uop_3542,])
func_3550 = relay.Function([var_3532,], output)
mod['func_3550'] = func_3550
mod = relay.transform.InferType()(mod)
mutated_mod['func_3550'] = func_3550
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3551 = relay.var("var_3551", dtype = "float64", shape = (16, 11, 8))#candidate|3551|(16, 11, 8)|var|float64
func_3550_call = mutated_mod.get_global_var('func_3550')
call_3552 = func_3550_call(var_3551)
output = call_3552
func_3553 = relay.Function([var_3551], output)
mutated_mod['func_3553'] = func_3553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_3566 = relay.TupleGetItem(func_296_call(), 1)
call_3567 = relay.TupleGetItem(func_297_call(), 1)
output = call_3566
output2 = call_3567
func_3570 = relay.Function([], output)
mod['func_3570'] = func_3570
mod = relay.transform.InferType()(mod)
mutated_mod['func_3570'] = func_3570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3570_call = mutated_mod.get_global_var('func_3570')
call_3571 = func_3570_call()
output = call_3571
func_3572 = relay.Function([], output)
mutated_mod['func_3572'] = func_3572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_3599 = func_984_call()
call_3600 = func_984_call()
func_1867_call = mod.get_global_var('func_1867')
func_1869_call = mutated_mod.get_global_var('func_1869')
call_3619 = relay.TupleGetItem(func_1867_call(), 1)
call_3620 = relay.TupleGetItem(func_1869_call(), 1)
bop_3623 = relay.logical_and(call_3619.astype('bool'), relay.reshape(call_3599.astype('bool'), relay.shape_of(call_3619))) # shape=(1, 3, 1)
bop_3626 = relay.logical_and(call_3620.astype('bool'), relay.reshape(call_3600.astype('bool'), relay.shape_of(call_3620))) # shape=(1, 3, 1)
func_2395_call = mod.get_global_var('func_2395')
func_2396_call = mutated_mod.get_global_var('func_2396')
call_3630 = func_2395_call()
call_3631 = func_2395_call()
func_604_call = mod.get_global_var('func_604')
func_605_call = mutated_mod.get_global_var('func_605')
call_3650 = relay.TupleGetItem(func_604_call(), 0)
call_3651 = relay.TupleGetItem(func_605_call(), 0)
var_3663 = relay.var("var_3663", dtype = "uint64", shape = (8, 3, 8))#candidate|3663|(8, 3, 8)|var|uint64
bop_3664 = relay.floor_divide(call_3599.astype('float32'), var_3663.astype('float32')) # shape=(8, 3, 8)
bop_3667 = relay.floor_divide(call_3600.astype('float32'), var_3663.astype('float32')) # shape=(8, 3, 8)
func_3550_call = mod.get_global_var('func_3550')
func_3553_call = mutated_mod.get_global_var('func_3553')
var_3678 = relay.var("var_3678", dtype = "float64", shape = (1408,))#candidate|3678|(1408,)|var|float64
call_3677 = relay.TupleGetItem(func_3550_call(relay.reshape(var_3678.astype('float64'), [16, 11, 8])), 0)
call_3679 = relay.TupleGetItem(func_3553_call(relay.reshape(var_3678.astype('float64'), [16, 11, 8])), 0)
output = relay.Tuple([bop_3623,call_3630,call_3650,bop_3664,call_3677,var_3678,])
output2 = relay.Tuple([bop_3626,call_3631,call_3651,bop_3667,call_3679,var_3678,])
func_3684 = relay.Function([var_3663,var_3678,], output)
mod['func_3684'] = func_3684
mod = relay.transform.InferType()(mod)
mutated_mod['func_3684'] = func_3684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3684_call = mutated_mod.get_global_var('func_3684')
var_3686 = relay.var("var_3686", dtype = "uint64", shape = (8, 3, 8))#candidate|3686|(8, 3, 8)|var|uint64
var_3687 = relay.var("var_3687", dtype = "float64", shape = (1408,))#candidate|3687|(1408,)|var|float64
call_3685 = func_3684_call(var_3686,var_3687,)
output = call_3685
func_3688 = relay.Function([var_3686,var_3687,], output)
mutated_mod['func_3688'] = func_3688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_3801 = relay.TupleGetItem(func_296_call(), 0)
call_3802 = relay.TupleGetItem(func_297_call(), 0)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_3803 = relay.TupleGetItem(func_296_call(), 0)
call_3804 = relay.TupleGetItem(func_297_call(), 0)
output = relay.Tuple([call_3801,call_3803,])
output2 = relay.Tuple([call_3802,call_3804,])
func_3814 = relay.Function([], output)
mod['func_3814'] = func_3814
mod = relay.transform.InferType()(mod)
output = func_3814()
func_3815 = relay.Function([], output)
mutated_mod['func_3815'] = func_3815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2395_call = mod.get_global_var('func_2395')
func_2396_call = mutated_mod.get_global_var('func_2396')
call_3845 = func_2395_call()
call_3846 = func_2395_call()
func_2603_call = mod.get_global_var('func_2603')
func_2605_call = mutated_mod.get_global_var('func_2605')
call_3847 = func_2603_call()
call_3848 = func_2603_call()
func_3223_call = mod.get_global_var('func_3223')
func_3226_call = mutated_mod.get_global_var('func_3226')
const_3851 = relay.const(1.480019, dtype = "float64")#candidate|3851|()|const|float64
call_3850 = relay.TupleGetItem(func_3223_call(relay.reshape(const_3851.astype('float64'), [])), 0)
call_3852 = relay.TupleGetItem(func_3226_call(relay.reshape(const_3851.astype('float64'), [])), 0)
uop_3860 = relay.log10(call_3847.astype('float32')) # shape=(1, 3, 1)
uop_3862 = relay.log10(call_3848.astype('float32')) # shape=(1, 3, 1)
func_1321_call = mod.get_global_var('func_1321')
func_1326_call = mutated_mod.get_global_var('func_1326')
var_3869 = relay.var("var_3869", dtype = "float32", shape = (1040,))#candidate|3869|(1040,)|var|float32
var_3870 = relay.var("var_3870", dtype = "uint64", shape = (351,))#candidate|3870|(351,)|var|uint64
call_3868 = relay.TupleGetItem(func_1321_call(relay.reshape(var_3869.astype('float32'), [10, 8, 13]), relay.reshape(var_3870.astype('uint64'), [9, 3, 13]), relay.reshape(var_3870.astype('float32'), [9, 3, 13]), ), 3)
call_3871 = relay.TupleGetItem(func_1326_call(relay.reshape(var_3869.astype('float32'), [10, 8, 13]), relay.reshape(var_3870.astype('uint64'), [9, 3, 13]), relay.reshape(var_3870.astype('float32'), [9, 3, 13]), ), 3)
bop_3877 = relay.greater(uop_3860.astype('bool'), call_3868.astype('bool')) # shape=(9, 3, 13)
bop_3880 = relay.greater(uop_3862.astype('bool'), call_3871.astype('bool')) # shape=(9, 3, 13)
func_3473_call = mod.get_global_var('func_3473')
func_3475_call = mutated_mod.get_global_var('func_3475')
call_3882 = relay.TupleGetItem(func_3473_call(), 0)
call_3883 = relay.TupleGetItem(func_3475_call(), 0)
output = relay.Tuple([call_3845,call_3850,const_3851,var_3869,var_3870,bop_3877,call_3882,])
output2 = relay.Tuple([call_3846,call_3852,const_3851,var_3869,var_3870,bop_3880,call_3883,])
func_3887 = relay.Function([var_3869,var_3870,], output)
mod['func_3887'] = func_3887
mod = relay.transform.InferType()(mod)
var_3888 = relay.var("var_3888", dtype = "float32", shape = (1040,))#candidate|3888|(1040,)|var|float32
var_3889 = relay.var("var_3889", dtype = "uint64", shape = (351,))#candidate|3889|(351,)|var|uint64
output = func_3887(var_3888,var_3889,)
func_3890 = relay.Function([var_3888,var_3889,], output)
mutated_mod['func_3890'] = func_3890
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3892 = relay.const([[[-3],[8],[-5],[-1],[-1],[-4],[-6],[-2],[7],[-1],[-5]],[[-8],[-4],[5],[10],[-2],[8],[-2],[10],[-3],[10],[8]],[[6],[-8],[6],[-9],[4],[9],[8],[7],[-1],[-1],[-8]],[[3],[8],[-3],[-3],[-6],[-2],[4],[-4],[10],[-2],[5]],[[6],[-10],[-1],[-7],[5],[9],[6],[-2],[4],[8],[2]],[[4],[6],[-1],[5],[-8],[8],[-10],[-8],[9],[7],[-7]],[[-1],[-3],[-4],[-1],[-4],[-10],[10],[-9],[-9],[-8],[5]],[[-7],[-6],[-8],[-4],[7],[-1],[2],[-3],[4],[9],[8]],[[-7],[-8],[3],[5],[-5],[3],[-7],[-4],[6],[-8],[-2]],[[-4],[3],[-4],[2],[-4],[10],[5],[-8],[-5],[3],[4]],[[-1],[-2],[-10],[5],[9],[8],[-9],[-4],[6],[-2],[-10]],[[10],[-9],[2],[-3],[1],[5],[-2],[-4],[-6],[8],[2]],[[-6],[-10],[6],[9],[-1],[3],[5],[4],[-2],[-3],[-10]],[[1],[-2],[4],[-2],[-9],[7],[-3],[3],[9],[2],[-8]]], dtype = "uint8")#candidate|3892|(14, 11, 1)|const|uint8
var_3893 = relay.var("var_3893", dtype = "uint8", shape = (14, 11, 1))#candidate|3893|(14, 11, 1)|var|uint8
bop_3894 = relay.greater_equal(const_3892.astype('bool'), relay.reshape(var_3893.astype('bool'), relay.shape_of(const_3892))) # shape=(14, 11, 1)
uop_3900 = relay.erf(const_3892.astype('float64')) # shape=(14, 11, 1)
output = relay.Tuple([bop_3894,uop_3900,])
output2 = relay.Tuple([bop_3894,uop_3900,])
func_3903 = relay.Function([var_3893,], output)
mod['func_3903'] = func_3903
mod = relay.transform.InferType()(mod)
var_3904 = relay.var("var_3904", dtype = "uint8", shape = (14, 11, 1))#candidate|3904|(14, 11, 1)|var|uint8
output = func_3903(var_3904)
func_3905 = relay.Function([var_3904], output)
mutated_mod['func_3905'] = func_3905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2746_call = mod.get_global_var('func_2746')
func_2748_call = mutated_mod.get_global_var('func_2748')
call_3968 = func_2746_call()
call_3969 = func_2746_call()
output = call_3968
output2 = call_3969
func_3975 = relay.Function([], output)
mod['func_3975'] = func_3975
mod = relay.transform.InferType()(mod)
output = func_3975()
func_3976 = relay.Function([], output)
mutated_mod['func_3976'] = func_3976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2726_call = mod.get_global_var('func_2726')
func_2727_call = mutated_mod.get_global_var('func_2727')
call_4025 = relay.TupleGetItem(func_2726_call(), 0)
call_4026 = relay.TupleGetItem(func_2727_call(), 0)
output = relay.Tuple([call_4025,])
output2 = relay.Tuple([call_4026,])
func_4049 = relay.Function([], output)
mod['func_4049'] = func_4049
mod = relay.transform.InferType()(mod)
output = func_4049()
func_4050 = relay.Function([], output)
mutated_mod['func_4050'] = func_4050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_890_call = mod.get_global_var('func_890')
func_891_call = mutated_mod.get_global_var('func_891')
call_4172 = relay.TupleGetItem(func_890_call(), 0)
call_4173 = relay.TupleGetItem(func_891_call(), 0)
output = relay.Tuple([call_4172,])
output2 = relay.Tuple([call_4173,])
func_4197 = relay.Function([], output)
mod['func_4197'] = func_4197
mod = relay.transform.InferType()(mod)
mutated_mod['func_4197'] = func_4197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4197_call = mutated_mod.get_global_var('func_4197')
call_4198 = func_4197_call()
output = call_4198
func_4199 = relay.Function([], output)
mutated_mod['func_4199'] = func_4199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_585_call = mod.get_global_var('func_585')
func_587_call = mutated_mod.get_global_var('func_587')
call_4200 = relay.TupleGetItem(func_585_call(), 1)
call_4201 = relay.TupleGetItem(func_587_call(), 1)
output = call_4200
output2 = call_4201
func_4204 = relay.Function([], output)
mod['func_4204'] = func_4204
mod = relay.transform.InferType()(mod)
output = func_4204()
func_4205 = relay.Function([], output)
mutated_mod['func_4205'] = func_4205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_4209 = func_984_call()
call_4210 = func_984_call()
func_2142_call = mod.get_global_var('func_2142')
func_2143_call = mutated_mod.get_global_var('func_2143')
call_4230 = relay.TupleGetItem(func_2142_call(), 0)
call_4231 = relay.TupleGetItem(func_2143_call(), 0)
output = relay.Tuple([call_4209,call_4230,])
output2 = relay.Tuple([call_4210,call_4231,])
func_4255 = relay.Function([], output)
mod['func_4255'] = func_4255
mod = relay.transform.InferType()(mod)
mutated_mod['func_4255'] = func_4255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4255_call = mutated_mod.get_global_var('func_4255')
call_4256 = func_4255_call()
output = call_4256
func_4257 = relay.Function([], output)
mutated_mod['func_4257'] = func_4257
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4266 = relay.const([[[-3,-6,-3,7,-5,-1,8,-2,-4,-2,-6],[-7,-10,5,-3,1,9,-10,-8,-6,-1,1],[9,-4,10,4,-8,10,5,8,-8,-4,6],[1,-1,8,2,-3,-5,-5,-2,2,9,10],[7,-2,6,-4,-9,6,-10,4,-4,-4,-4],[5,-10,-6,8,5,-5,-2,4,-3,9,-5]],[[-6,2,5,-10,-6,3,-3,-7,8,-6,-8],[1,-4,-4,-6,1,-7,-3,-10,-9,7,4],[-4,10,-2,2,7,-3,10,4,-8,9,10],[8,-2,-6,-3,-10,1,9,-10,-3,-8,8],[6,5,8,7,-5,-8,4,-7,-4,3,1],[-9,5,-6,10,3,7,-8,-4,-3,-2,6]],[[-2,-2,-4,-2,-9,3,-2,-6,-4,-8,9],[-6,-5,-9,-7,-4,10,5,-2,-8,-7,4],[-10,4,1,5,-2,-2,9,3,-8,4,6],[3,-8,9,-2,7,-5,-7,4,6,-4,-2],[-2,6,-5,-10,-10,7,4,3,8,7,2],[-10,8,4,-4,3,-1,-6,9,-5,8,9]],[[9,7,4,3,-10,4,-8,-7,5,8,9],[2,9,9,3,-1,-1,-4,-4,5,-9,-1],[-9,9,8,-10,3,-5,3,-10,-5,1,-1],[5,9,9,-8,6,9,-1,-5,4,-5,10],[4,-4,-3,6,-9,9,-8,-7,9,6,-1],[2,10,-5,4,2,-7,8,-3,-4,-3,2]],[[3,2,5,9,6,3,9,10,-1,-3,1],[8,6,-8,-7,4,2,-4,-5,2,-4,7],[2,7,2,-2,3,-6,-6,-10,5,-4,10],[-3,-9,-6,9,-8,-1,-4,9,5,-10,3],[-7,8,8,10,-10,-5,-7,5,4,-9,-10],[-9,1,-1,7,8,8,6,9,-4,-9,9]],[[-1,6,-8,4,7,7,9,10,3,-10,3],[-6,3,1,-10,10,3,-9,-10,-8,-6,7],[-4,-9,-5,7,6,2,3,1,-4,-5,8],[7,-6,-5,4,8,-8,-7,8,3,-9,-1],[-6,8,-5,6,-8,1,2,8,7,5,5],[-10,-8,-4,6,9,-10,-4,1,-10,7,-3]],[[-9,-6,-7,4,5,-2,5,-1,-5,-6,9],[-2,2,-7,5,-9,-1,1,-7,9,-8,-6],[8,7,10,-10,5,-9,-4,-7,8,-3,4],[6,-10,-5,5,5,-9,-9,-6,-9,-9,-8],[-7,-3,-5,-2,2,-8,3,5,5,1,10],[4,-7,7,-3,2,-3,3,-3,5,-4,-10]],[[-8,-5,4,-8,6,-2,-7,2,7,-8,-8],[6,-5,-9,-6,6,-5,-5,-6,3,5,8],[6,9,-5,4,7,7,1,-1,-6,-8,-7],[-9,-8,-7,-2,4,-7,1,-2,-5,5,3],[7,-2,10,-5,-5,-9,9,-7,-3,8,5],[-1,-6,-8,-8,6,4,8,8,-8,-8,-7]],[[3,9,-4,-5,8,-10,2,-3,8,6,7],[-5,-9,-9,9,5,9,-9,3,-4,2,3],[-1,-4,8,-2,-6,-10,-9,4,-5,4,-3],[7,-9,-6,4,-4,-8,5,-10,10,3,3],[-1,1,-5,9,8,-5,8,7,-1,-8,-1],[4,9,9,8,-5,-8,4,-1,-3,-1,-5]],[[8,-1,-3,7,-2,-7,-8,3,8,-4,6],[2,-3,6,3,-10,-3,9,10,4,-10,-2],[-5,4,-5,-10,6,-8,-6,2,-6,-2,5],[-7,-9,6,-1,-8,5,2,2,-1,-5,-9],[1,-2,-6,-6,-6,-6,7,4,2,4,8],[5,7,8,5,5,-7,-3,-9,-3,-5,10]]], dtype = "uint16")#candidate|4266|(10, 6, 11)|const|uint16
const_4267 = relay.const([[[5,-6,-3,7,1,6,-3,1,-4,-7,-10],[10,-4,-3,3,8,9,6,-9,10,9,5],[-6,-1,3,-1,-10,10,-5,8,6,-8,2],[-9,-9,10,-8,9,1,6,-1,-6,10,-2],[-10,3,-6,3,6,-8,2,2,-5,3,2],[-10,8,3,4,3,4,10,-10,10,4,9]],[[-8,-5,4,6,9,9,4,7,7,-1,-9],[-3,-5,-5,10,6,-4,10,-3,4,-4,3],[-6,7,-2,4,-1,-2,-1,7,10,-1,8],[-4,10,3,2,-4,-6,-2,9,-4,5,9],[3,-7,-1,1,10,8,-5,3,-9,-8,8],[-7,-7,9,7,6,-4,-6,1,-2,-5,2]],[[5,1,-2,3,8,9,1,7,-6,9,-8],[-2,-4,-2,9,1,9,2,-1,-3,4,-6],[10,2,-8,3,-8,7,-3,3,4,10,5],[7,4,7,-2,3,-8,-7,8,2,-8,9],[9,5,-7,-7,6,10,-3,-10,-2,8,-7],[-8,-4,-2,1,-6,-7,-4,-6,9,-6,-4]],[[10,4,6,-3,7,-10,2,-5,-5,-3,-2],[7,9,-9,-8,2,6,9,-9,3,-6,9],[6,2,7,-4,-4,6,-10,6,8,4,-5],[-6,-9,-4,-3,-4,-9,10,4,4,6,9],[6,2,5,-10,2,9,-4,-6,-6,-5,9],[-10,9,10,5,-1,-5,5,-10,-2,-10,6]],[[2,10,-4,-2,10,5,7,5,3,2,-1],[-9,3,-5,-2,8,3,-3,-3,-10,-10,-2],[-8,-8,-3,2,9,-6,5,-7,10,-3,3],[10,5,-9,-2,-2,10,-3,2,8,7,4],[-3,10,-6,8,1,3,9,10,5,-4,-2],[7,-2,-5,-8,2,-10,7,-5,5,-7,3]],[[2,-9,-5,-3,2,1,4,-7,-3,-6,-9],[-10,9,4,6,4,-3,9,8,5,2,7],[1,10,1,8,-8,8,-6,7,-2,-1,4],[4,-2,3,6,9,4,-1,5,6,-2,5],[7,-1,1,-3,-2,10,-8,7,2,9,-5],[-10,-2,6,-1,1,10,-6,-5,-9,-7,-10]],[[-1,9,3,1,10,10,8,-7,6,-8,9],[-9,-4,-1,5,-6,-10,-2,-2,-3,-4,6],[7,-2,1,-9,-5,-7,7,10,1,10,2],[6,-3,-8,-10,-1,-6,-9,-5,9,9,7],[-6,-9,4,10,-1,1,3,-3,2,1,-6],[-6,1,1,3,-5,6,8,5,-7,4,2]],[[-5,-2,8,-8,-4,-7,4,-4,-5,-8,6],[10,-3,8,5,5,-5,-1,-8,9,-3,-6],[4,4,2,-8,-7,8,7,7,5,4,-9],[-5,3,-1,-10,-5,-9,-2,2,-9,-10,1],[6,1,-10,-3,3,-7,2,5,5,4,3],[-8,8,6,-6,-9,-4,6,-9,-2,7,-9]],[[7,10,-5,7,2,5,-3,-2,-7,-3,-3],[-3,-8,-3,4,3,-5,3,-9,10,-8,-5],[-5,3,-10,-10,-5,-5,10,9,9,5,-5],[8,3,-7,-2,-3,9,-6,4,2,-9,-4],[5,4,7,10,10,-8,-5,-5,7,-3,-3],[5,-6,-9,-4,-5,8,2,9,-7,-1,3]],[[10,-4,-5,5,-9,7,9,-2,1,-1,7],[4,7,-8,-6,4,-8,-7,7,-2,4,2],[5,6,3,7,-3,9,-10,-8,-5,-6,-5],[5,3,-8,7,10,-6,-10,-4,-1,5,6],[-5,6,1,5,3,7,9,4,-7,-8,1],[-6,-4,-3,-6,-8,7,5,6,-1,-1,-6]]], dtype = "uint16")#candidate|4267|(10, 6, 11)|const|uint16
bop_4268 = relay.greater(const_4266.astype('bool'), relay.reshape(const_4267.astype('bool'), relay.shape_of(const_4266))) # shape=(10, 6, 11)
uop_4273 = relay.log10(bop_4268.astype('float64')) # shape=(10, 6, 11)
func_2395_call = mod.get_global_var('func_2395')
func_2396_call = mutated_mod.get_global_var('func_2396')
call_4275 = func_2395_call()
call_4276 = func_2395_call()
func_2603_call = mod.get_global_var('func_2603')
func_2605_call = mutated_mod.get_global_var('func_2605')
call_4277 = func_2603_call()
call_4278 = func_2603_call()
output = relay.Tuple([uop_4273,call_4275,call_4277,])
output2 = relay.Tuple([uop_4273,call_4276,call_4278,])
func_4284 = relay.Function([], output)
mod['func_4284'] = func_4284
mod = relay.transform.InferType()(mod)
mutated_mod['func_4284'] = func_4284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4284_call = mutated_mod.get_global_var('func_4284')
call_4285 = func_4284_call()
output = call_4285
func_4286 = relay.Function([], output)
mutated_mod['func_4286'] = func_4286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4197_call = mod.get_global_var('func_4197')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_4329 = relay.TupleGetItem(func_4197_call(), 0)
call_4330 = relay.TupleGetItem(func_4199_call(), 0)
output = call_4329
output2 = call_4330
func_4335 = relay.Function([], output)
mod['func_4335'] = func_4335
mod = relay.transform.InferType()(mod)
output = func_4335()
func_4336 = relay.Function([], output)
mutated_mod['func_4336'] = func_4336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2218_call = mod.get_global_var('func_2218')
func_2220_call = mutated_mod.get_global_var('func_2220')
call_4404 = relay.TupleGetItem(func_2218_call(), 0)
call_4405 = relay.TupleGetItem(func_2220_call(), 0)
output = call_4404
output2 = call_4405
func_4417 = relay.Function([], output)
mod['func_4417'] = func_4417
mod = relay.transform.InferType()(mod)
mutated_mod['func_4417'] = func_4417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4417_call = mutated_mod.get_global_var('func_4417')
call_4418 = func_4417_call()
output = call_4418
func_4419 = relay.Function([], output)
mutated_mod['func_4419'] = func_4419
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4442 = relay.const([[[10,2,6,6,5,-3,-5,-9,-9,-6,1],[-4,3,-3,-5,-4,4,-10,2,-6,-2,-1],[1,-6,1,7,7,7,7,6,4,-6,-6],[9,-10,4,5,-9,-3,9,6,6,-9,3],[2,-7,9,-5,8,2,-8,-2,-10,-9,7],[-7,-4,-6,9,-9,1,9,9,-5,-5,-7],[-3,-6,-1,6,-5,-10,-9,3,8,-8,10]],[[-8,-1,-6,-2,-1,-3,8,4,-1,-8,-9],[7,-4,6,5,1,-4,8,1,4,-3,-9],[-8,-4,1,10,-8,1,-4,-7,-2,-2,-3],[6,-10,-3,7,5,-4,-4,10,4,1,-3],[-4,-1,9,3,-6,7,1,-1,4,2,5],[-3,-10,-5,4,-5,6,-5,1,-10,-8,5],[7,-6,9,8,-5,-9,8,5,9,10,-8]],[[-4,-4,-6,-1,2,6,-8,-9,1,7,-9],[3,9,-6,9,4,2,8,-10,10,7,-9],[1,3,-2,-1,9,8,5,-7,-7,8,8],[-9,6,-8,5,10,-7,-9,7,-9,3,-4],[-1,-3,-1,10,-8,6,8,9,-3,-1,-3],[-9,-2,7,-8,-4,-2,-9,-1,-2,10,2],[-4,-3,-9,-7,-9,-5,7,-6,4,5,-8]],[[-9,-7,-9,9,-7,2,9,-6,-6,-5,6],[2,8,-4,2,-1,-3,3,3,3,6,10],[9,-4,-3,-5,-2,10,4,6,6,-6,4],[-10,3,7,-9,5,-6,-4,-9,-7,7,-2],[1,-7,-3,-7,4,6,-1,7,1,-9,-2],[-6,-3,3,-10,2,-2,2,2,4,7,5],[2,-9,7,-2,10,-1,8,-4,8,-4,5]],[[-6,5,4,10,1,5,-7,-9,-1,-4,3],[-6,-4,1,5,-2,-2,2,1,7,-4,-4],[-5,7,-2,-8,-4,-10,-1,4,8,8,5],[9,-2,7,-1,4,-2,1,3,-8,6,-5],[2,2,7,1,-9,-9,-9,4,7,-5,2],[-4,-7,-2,-2,-9,-6,6,2,7,-10,-2],[-3,8,-6,-1,-8,3,-9,8,4,8,2]],[[-5,-1,-6,1,9,-6,-3,9,3,1,3],[-3,-1,-10,-8,3,7,-8,-5,2,-2,-3],[1,1,1,9,1,-7,-10,-1,1,4,8],[-2,-2,8,-1,10,-5,5,10,4,-10,4],[-9,-10,9,-8,-7,-9,-3,4,-8,-7,3],[10,9,-7,-4,9,-7,4,1,2,-10,-9],[-8,8,-5,-10,8,6,-4,6,-5,1,-4]],[[-8,7,-4,-1,-10,4,-6,3,-9,-5,-8],[-7,7,1,-4,5,9,3,6,6,4,4],[-1,5,-7,7,7,2,-8,4,-6,-5,8],[8,-4,2,4,-10,-2,-7,7,-2,7,-10],[7,-6,-2,7,1,-6,10,6,5,-1,3],[3,1,4,-1,1,-8,-10,2,-2,3,-9],[-7,10,-1,6,8,-5,5,5,6,2,6]],[[6,-9,10,-6,6,-4,-5,7,10,-1,4],[-6,1,-6,-6,5,10,-10,-8,7,-2,-2],[7,-6,-7,-4,2,2,2,6,-2,-1,9],[-1,2,2,-3,8,-6,-9,-3,5,-2,9],[-9,-5,-10,-3,10,5,-6,-5,-3,-8,-1],[-3,-7,2,-9,7,-7,-9,9,-3,8,10],[-5,10,9,-7,5,5,-10,5,-9,7,3]],[[3,6,2,6,-7,-8,-8,-6,-9,7,-5],[2,-8,10,-7,9,-8,9,-10,-3,-7,7],[10,-2,-4,-5,-10,7,-8,-3,-4,6,-1],[10,-10,-2,6,2,-3,-4,-7,-6,-6,5],[1,-8,2,7,-6,7,-9,-3,-8,-10,-3],[-6,3,-7,6,-2,2,4,-1,9,7,7],[5,-3,-7,4,7,-2,3,-1,1,-7,-5]],[[-7,1,6,-10,-4,-5,9,-9,-3,2,-1],[3,3,-7,-7,3,-9,-7,-2,9,5,-4],[5,-7,2,-2,-4,4,10,-2,-4,-2,9],[9,8,9,10,-8,-9,-3,-4,-5,-3,8],[10,2,-4,8,-4,5,5,-7,-1,9,-2],[2,-9,-6,6,6,3,2,2,1,7,10],[-3,-6,-2,4,-9,-9,3,-1,-9,-7,-6]],[[-10,-8,-4,8,-6,1,-7,7,6,-10,-4],[-8,4,-3,10,9,-6,2,2,4,-2,10],[-7,-1,-2,-5,3,-3,-3,-7,4,4,5],[-1,-7,-6,1,8,-4,-8,9,-5,1,1],[-4,8,6,-1,-1,9,7,-8,-3,6,-7],[-4,-2,-1,8,-8,2,-4,9,9,-8,-9],[-4,-5,3,-4,8,9,8,-2,3,3,-5]],[[4,-2,5,3,-5,10,6,1,-6,-10,8],[6,-8,-9,6,8,7,5,8,-7,7,-10],[3,-2,10,-5,-2,6,3,1,-9,-1,6],[2,4,-6,-7,3,-10,10,-1,-6,-9,4],[-10,-1,-3,7,8,5,7,4,-8,7,-4],[-7,3,9,-8,3,-8,-6,9,-10,3,9],[-7,-5,10,2,-8,-8,-2,4,-9,-9,3]]], dtype = "int64")#candidate|4442|(12, 7, 11)|const|int64
var_4443 = relay.var("var_4443", dtype = "int64", shape = (12, 7, 11))#candidate|4443|(12, 7, 11)|var|int64
bop_4444 = relay.multiply(const_4442.astype('int64'), relay.reshape(var_4443.astype('int64'), relay.shape_of(const_4442))) # shape=(12, 7, 11)
output = relay.Tuple([bop_4444,])
output2 = relay.Tuple([bop_4444,])
func_4450 = relay.Function([var_4443,], output)
mod['func_4450'] = func_4450
mod = relay.transform.InferType()(mod)
mutated_mod['func_4450'] = func_4450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4451 = relay.var("var_4451", dtype = "int64", shape = (12, 7, 11))#candidate|4451|(12, 7, 11)|var|int64
func_4450_call = mutated_mod.get_global_var('func_4450')
call_4452 = func_4450_call(var_4451)
output = call_4452
func_4453 = relay.Function([var_4451], output)
mutated_mod['func_4453'] = func_4453
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4465 = relay.const([[[9,5,10,8,-7,-10,6,2,5,4,-3,4],[3,5,-2,-9,7,-6,9,2,1,-6,-5,-6],[-2,-4,5,8,-9,-4,-8,-1,-7,1,5,4],[5,-2,-8,9,-9,4,-10,1,-5,-10,8,-9],[-10,-10,6,-10,-6,9,1,6,2,-5,2,4],[1,-10,5,5,-10,2,-1,-6,7,2,7,9],[10,4,1,1,1,-2,-1,-6,2,-8,2,-1],[-1,-8,-1,-10,2,4,3,5,7,2,4,2],[4,10,-5,-5,-6,-7,-2,9,-2,-7,-6,-8],[-2,2,8,4,3,-10,-7,-7,9,-1,2,5],[10,-10,6,9,10,-4,3,-10,5,5,4,6],[-5,-4,-4,-2,3,-1,1,7,-1,-8,10,-3]],[[6,9,-9,5,10,2,2,-8,-7,6,-1,7],[-5,-6,-3,-1,8,-2,5,-2,9,-8,-9,6],[7,6,-6,-10,8,-9,7,-3,-2,-2,2,-1],[-8,-10,7,-5,-9,-2,3,-7,10,-5,7,-9],[-1,-5,5,-2,7,1,1,10,-6,6,-6,2],[10,-10,5,6,-2,-9,-5,9,-4,-7,4,-6],[2,2,6,4,5,-2,7,6,-9,6,5,-7],[4,5,-3,-10,4,5,-10,-7,4,3,9,1],[-4,3,10,10,4,-4,8,-4,-8,6,7,-2],[5,4,-5,-4,-4,10,-5,-10,6,7,-7,-10],[-7,2,-10,-7,-10,-10,8,5,9,7,-6,4],[-10,7,2,-2,-2,5,9,-6,6,3,10,-7]],[[-3,-4,1,10,10,9,-5,-3,5,10,1,-2],[-1,-3,3,1,-4,5,-2,-7,4,-4,-8,7],[-4,-7,2,4,-4,-6,6,-5,2,-6,-6,-9],[-10,9,-2,3,-1,3,-2,9,-3,-5,2,-7],[-9,-1,7,-5,-2,7,1,10,-4,7,9,2],[-3,-10,6,-9,2,9,-9,6,-9,5,-7,-3],[-7,7,-8,-9,7,-6,-9,-7,7,10,-10,-7],[-1,10,7,-9,4,2,6,-3,-1,5,5,10],[-9,10,-7,10,-9,-6,-2,3,-2,9,8,-10],[-10,8,-8,-9,-9,6,-6,-3,-7,-3,5,-6],[-3,-4,7,-10,10,4,8,-5,-2,4,9,5],[8,4,6,-10,-5,1,-10,-8,-1,-8,-6,10]],[[4,-8,-9,9,-4,1,-5,10,7,1,-2,-8],[1,-6,9,-7,-7,-5,1,-6,-7,5,-9,-1],[6,-6,2,3,-9,2,-4,10,7,10,9,1],[4,-7,10,-1,-1,7,2,7,-1,-1,10,-8],[7,3,5,-2,-1,-4,-1,9,6,5,8,-9],[-1,-5,2,-7,1,-4,5,5,-7,9,8,9],[-8,1,-4,-6,-1,-7,-2,1,-6,10,-1,7],[6,5,6,7,8,-9,-8,-9,-5,3,3,-1],[-9,2,7,-9,7,-8,-9,8,-3,-2,-3,-4],[-9,8,-3,5,-9,3,6,9,-9,8,-2,-5],[-5,-7,-10,-7,-8,-5,3,2,-4,-7,10,-4],[3,-6,10,1,10,2,-9,-9,5,9,-3,-9]],[[9,-9,-4,-5,-7,-3,4,-10,1,4,-2,-10],[-8,-4,-3,10,-1,-10,-2,-3,8,3,9,8],[-7,2,7,8,-1,8,5,8,5,-2,-3,-3],[10,-4,-3,-9,-5,4,2,-9,4,9,-3,7],[2,-4,-4,-7,7,3,6,-2,4,-2,6,9],[7,3,-4,-8,10,3,-1,10,6,7,7,10],[3,-6,-3,1,5,-2,6,5,-3,2,3,-1],[-7,-8,6,-6,9,-10,-8,-4,6,-2,-7,-8],[7,6,4,-6,6,5,-1,-2,2,-7,-2,-3],[-9,1,-2,-8,-9,-7,-2,3,-7,1,-7,10],[-3,-2,-8,-5,8,2,-5,8,-7,-8,-10,-8],[-7,-6,-1,6,5,-1,2,1,2,-1,6,-10]],[[6,1,-8,4,-9,2,9,4,-7,-7,10,1],[1,-8,1,9,7,3,2,-1,-8,-9,-4,-10],[-7,-1,5,7,-4,-5,3,4,6,3,7,-9],[10,1,-10,-4,10,-1,9,-10,-3,10,9,-5],[-3,4,-6,-4,-10,8,-8,6,2,-2,7,4],[9,7,-9,-4,3,-4,-1,-5,5,-1,-8,2],[6,10,8,-3,-9,-4,5,5,-5,8,7,-7],[7,-9,6,-6,5,-4,-2,-7,-9,1,8,3],[5,9,5,6,5,8,7,4,9,-5,6,4],[-3,-1,-1,6,8,-9,3,-4,1,2,5,1],[3,-5,-8,-6,3,3,4,1,-5,6,8,-6],[3,8,-3,1,5,-3,-4,5,8,3,-7,5]],[[-7,-10,10,-5,-6,-10,1,3,7,8,-6,-1],[1,8,10,-8,4,-3,5,-7,10,10,-9,7],[10,7,10,-4,-2,7,-4,1,4,-4,10,10],[9,1,-2,1,-6,1,8,5,6,2,-10,9],[6,2,5,6,-3,-9,5,-8,10,-5,3,-10],[3,-10,-6,-6,2,-6,4,-10,-7,2,1,-3],[7,1,9,10,3,6,9,-10,3,-10,10,-2],[1,10,-1,-4,10,-10,-5,10,10,-9,-9,-4],[7,-9,-5,3,-4,7,6,6,5,5,-8,-1],[-3,9,-9,4,6,10,-4,-7,-8,6,4,-1],[1,2,-3,8,-1,-9,8,6,-9,-5,-1,-3],[-7,-4,2,1,-3,1,-3,-1,-5,-5,-8,-9]],[[9,-1,-8,-1,3,5,3,9,6,2,-10,-6],[-7,-10,-3,-1,-4,-3,7,5,-1,7,6,-2],[7,-4,8,4,10,-10,2,5,2,-8,2,-8],[6,1,-1,-6,8,9,-1,-1,6,6,-3,-6],[9,-5,-9,-5,10,9,-10,2,-7,6,-4,1],[-8,-2,7,7,1,-6,7,-5,9,8,1,9],[-1,-5,2,6,2,3,5,-5,4,-9,3,5],[8,-5,-5,6,-9,-2,-9,-5,8,2,9,-4],[-9,1,-6,7,-2,-4,7,3,-3,9,5,6],[-1,9,-8,-3,5,-2,-2,7,-9,1,1,2],[-8,7,-4,-9,3,-4,-10,-9,-3,-5,10,-1],[5,7,-5,-9,1,-8,-10,1,-2,4,4,-8]],[[4,3,7,5,3,7,10,-3,-3,7,6,7],[-2,2,4,-4,3,-4,-9,-4,8,2,-7,-10],[-4,4,-4,-9,-1,2,-1,4,4,-6,-7,-5],[10,-5,-2,9,-2,5,-3,-4,-5,2,5,-10],[5,9,-6,7,4,5,6,4,-7,8,5,-8],[8,-6,5,-9,-4,2,-7,-8,-10,-8,6,-8],[1,7,-6,6,-5,7,10,10,-6,-6,1,3],[8,10,1,9,4,8,10,-5,8,-5,-10,6],[7,-9,7,-10,3,-9,9,-8,3,-4,4,8],[-3,-2,-7,-9,2,5,-1,-4,-6,-3,-10,-10],[1,-6,5,-6,-6,-1,7,-9,1,-8,-10,9],[5,3,-2,-8,6,7,7,-2,-2,-8,-5,9]]], dtype = "int64")#candidate|4465|(9, 12, 12)|const|int64
var_4466 = relay.var("var_4466", dtype = "int64", shape = (9, 12, 12))#candidate|4466|(9, 12, 12)|var|int64
bop_4467 = relay.bitwise_or(const_4465.astype('int64'), relay.reshape(var_4466.astype('int64'), relay.shape_of(const_4465))) # shape=(9, 12, 12)
output = relay.Tuple([bop_4467,])
output2 = relay.Tuple([bop_4467,])
func_4478 = relay.Function([var_4466,], output)
mod['func_4478'] = func_4478
mod = relay.transform.InferType()(mod)
var_4479 = relay.var("var_4479", dtype = "int64", shape = (9, 12, 12))#candidate|4479|(9, 12, 12)|var|int64
output = func_4478(var_4479)
func_4480 = relay.Function([var_4479], output)
mutated_mod['func_4480'] = func_4480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_394_call = mutated_mod.get_global_var('func_394')
call_4482 = relay.TupleGetItem(func_393_call(), 1)
call_4483 = relay.TupleGetItem(func_394_call(), 1)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_4495 = relay.TupleGetItem(func_296_call(), 1)
call_4496 = relay.TupleGetItem(func_297_call(), 1)
output = relay.Tuple([call_4482,call_4495,])
output2 = relay.Tuple([call_4483,call_4496,])
func_4502 = relay.Function([], output)
mod['func_4502'] = func_4502
mod = relay.transform.InferType()(mod)
output = func_4502()
func_4503 = relay.Function([], output)
mutated_mod['func_4503'] = func_4503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_4512 = relay.TupleGetItem(func_506_call(), 0)
call_4513 = relay.TupleGetItem(func_507_call(), 0)
output = relay.Tuple([call_4512,])
output2 = relay.Tuple([call_4513,])
func_4523 = relay.Function([], output)
mod['func_4523'] = func_4523
mod = relay.transform.InferType()(mod)
output = func_4523()
func_4524 = relay.Function([], output)
mutated_mod['func_4524'] = func_4524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1014_call = mod.get_global_var('func_1014')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_4531 = func_1014_call()
call_4532 = func_1014_call()
func_2746_call = mod.get_global_var('func_2746')
func_2748_call = mutated_mod.get_global_var('func_2748')
call_4535 = func_2746_call()
call_4536 = func_2746_call()
output = relay.Tuple([call_4531,call_4535,])
output2 = relay.Tuple([call_4532,call_4536,])
func_4539 = relay.Function([], output)
mod['func_4539'] = func_4539
mod = relay.transform.InferType()(mod)
output = func_4539()
func_4540 = relay.Function([], output)
mutated_mod['func_4540'] = func_4540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1980_call = mod.get_global_var('func_1980')
func_1982_call = mutated_mod.get_global_var('func_1982')
call_4572 = relay.TupleGetItem(func_1980_call(), 0)
call_4573 = relay.TupleGetItem(func_1982_call(), 0)
var_4586 = relay.var("var_4586", dtype = "float64", shape = (2, 3, 7))#candidate|4586|(2, 3, 7)|var|float64
bop_4587 = relay.left_shift(call_4572.astype('int64'), var_4586.astype('int64')) # shape=(2, 3, 7)
bop_4590 = relay.left_shift(call_4573.astype('int64'), var_4586.astype('int64')) # shape=(2, 3, 7)
func_725_call = mod.get_global_var('func_725')
func_728_call = mutated_mod.get_global_var('func_728')
var_4604 = relay.var("var_4604", dtype = "float64", shape = (1350,))#candidate|4604|(1350,)|var|float64
call_4603 = relay.TupleGetItem(func_725_call(relay.reshape(var_4604.astype('float64'), [15, 9, 10])), 2)
call_4605 = relay.TupleGetItem(func_728_call(relay.reshape(var_4604.astype('float64'), [15, 9, 10])), 2)
uop_4606 = relay.sin(var_4604.astype('float32')) # shape=(1350,)
func_725_call = mod.get_global_var('func_725')
func_728_call = mutated_mod.get_global_var('func_728')
call_4608 = relay.TupleGetItem(func_725_call(relay.reshape(var_4604.astype('float64'), [15, 9, 10])), 2)
call_4609 = relay.TupleGetItem(func_728_call(relay.reshape(var_4604.astype('float64'), [15, 9, 10])), 2)
func_4450_call = mod.get_global_var('func_4450')
func_4453_call = mutated_mod.get_global_var('func_4453')
const_4618 = relay.const([-2,-10,-1,-2,10,-6,-9,-5,2,-7,5,8,9,-2,-5,-8,1,10,9,-9,-9,5,3,-7,3,6,10,-10,7,8,4,1,-8,-7,4,-5,10,3,9,-8,1,-2,5,-10,1,4,-5,-9,7,-7,2,4,-3,-3,6,-7,-5,-10,1,3,-7,9,4,-5,6,10,8,-9,-2,5,6,-6,3,3,5,5,-5,-6,-4,1,-4,5,-6,3,9,-5,2,-5,-7,-8,-6,-6,9,1,-4,-1,-5,10,-3,9,-3,-4,-6,-9,-9,5,1,-6,5,4,-2,-8,3,6,3,7,-10,10,-2,-10,7,6,-9,2,2,3,-3,10,-1,4,-4,9,-2,1,-9,4,-6,-7,5,-9,5,10,3,4,8,7,8,5,6,-5,7,-2,-2,-10,-8,3,-10,-3,-4,-8,-4,-2,10,4,5,2,9,-9,-3,-7,7,-6,4,2,6,-8,-5,-5,-10,-5,-8,-1,9,7,8,-6,-5,-3,-2,5,-5,2,-3,-8,-6,2,-8,-3,4,2,4,-8,-10,8,-6,-4,5,-4,3,-3,-7,-4,-1,-3,-5,-8,2,-1,-9,-6,9,-7,-4,-5,4,-7,-5,5,6,-3,-2,-3,9,7,-1,2,-5,-6,-1,-7,1,6,-2,3,9,-2,-7,7,9,3,-1,3,5,4,-2,-10,4,8,9,6,7,10,5,1,3,5,10,-7,-7,10,-1,-2,-10,-1,-2,-6,-6,-5,4,-4,-4,3,7,9,-3,5,3,9,8,10,-10,10,-3,-7,-5,-7,10,-2,-10,-2,2,-6,-3,-8,-8,2,7,4,-9,8,-1,-2,5,-9,5,-9,-7,3,4,2,10,-8,7,8,2,-9,-2,-8,-5,3,8,-8,-9,-6,10,4,3,-8,3,-8,3,10,10,-2,4,-6,9,7,3,-10,-5,-7,-8,1,-3,6,8,-9,3,3,7,8,-3,6,2,1,2,-8,-2,-2,9,1,4,-4,-3,4,8,8,9,-5,9,10,5,2,8,4,-1,-5,-5,4,7,10,10,-5,1,9,10,-3,-7,2,-10,1,9,8,4,-4,10,6,-1,6,-5,-3,-4,7,5,7,6,-9,-5,-1,-9,-1,10,-6,2,-4,-8,-1,-3,-8,-10,4,-2,-8,-9,5,5,-8,5,5,-9,4,6,-4,4,9,-4,9,-5,-4,-8,-6,-6,8,-10,1,-4,7,-10,8,10,9,10,1,-5,-4,5,-7,-4,-4,-10,4,-10,3,-3,-6,-10,-8,-1,8,5,10,-1,2,-2,10,1,-7,6,-1,-2,-3,-1,5,-1,1,-4,-7,-6,10,5,-1,5,-9,9,-1,8,3,4,-3,-10,2,-3,-1,-10,-10,-1,3,-10,-9,2,-10,-4,10,-1,-5,-7,-9,8,1,8,-4,2,-7,10,1,-7,-2,4,-9,5,9,2,2,5,9,7,-4,-1,-1,-6,2,-3,-4,-8,-1,-8,-5,-8,2,10,-7,-5,8,-2,6,3,-1,4,-3,-10,-5,7,-1,-7,-6,-4,-6,4,4,2,3,-10,2,-4,6,9,4,-3,9,-8,9,-10,1,-6,9,5,-3,-10,8,-10,-10,10,-5,9,-3,10,10,-4,5,6,-9,-8,7,-7,-2,1,-6,-5,4,-6,10,-6,8,-3,-1,7,-1,2,2,1,8,5,-3,-6,4,-3,-10,7,8,-10,-9,8,-1,6,-10,7,-10,-4,3,-1,2,1,2,9,-6,-6,-8,-2,5,-10,6,-4,10,-3,-8,9,-8,-3,6,10,-2,6,-3,7,-8,-2,6,3,6,10,10,-5,8,9,-9,-8,5,1,4,-5,-8,-7,5,-2,-5,6,-2,4,-8,-5,-1,-9,7,-4,9,3,8,-4,9,-3,-8,2,9,-1,-10,-3,-9,9,2,7,5,-9,-10,-6,-10,-7,-10,-10,6,6,-10,-9,1,7,3,5,3,-1,-8,4,-5,-6,-10,4,10,4,-8,8,-2,3,10,5,3,-8,2,8,-3,-4,3,-10,9,4,8,-9,9,-8,-9,2,-1,-2,2,-4,-6,-9,8,5,-5,7,1,6,5,8,-8,-5,-1,-6,8,-10,-10,-7,-8,8,-9,7,-8,-1,8,8,-2,-7,-9,-5,-4,-3,-4,3,-1,5,5,-2,-6,7,-4,2,-7,6,3,-4,8,3,8,-6,-8,-10,7,-7,7,-7,-8,-5,-9,2,-6,-10,6,8,1,4,7,2,8,-6,-3,5,3,6,-5,-5,7,-7,1,6,1,1,1,-1,5,3,-10,7,10,-7,-4,-6,-10,-3,-10,4,6,-9,-1,8,-10,1,-1,3,-6,6,3,-10,-7,-5,-9,-10,4,-3,-2,10,4,-1,-4,4,-7,7,-4,-4,-7,8,5,2,-9,-4,-8,2,6,4,-8,-9,1,-6,2,-6,8,-6,3,-2,-2,1,1,-9,7,-8,-4], dtype = "int64")#candidate|4618|(924,)|const|int64
call_4617 = relay.TupleGetItem(func_4450_call(relay.reshape(const_4618.astype('int64'), [12, 7, 11])), 0)
call_4619 = relay.TupleGetItem(func_4453_call(relay.reshape(const_4618.astype('int64'), [12, 7, 11])), 0)
output = relay.Tuple([bop_4587,call_4603,uop_4606,call_4608,call_4617,const_4618,])
output2 = relay.Tuple([bop_4590,call_4605,uop_4606,call_4609,call_4619,const_4618,])
func_4635 = relay.Function([var_4586,var_4604,], output)
mod['func_4635'] = func_4635
mod = relay.transform.InferType()(mod)
mutated_mod['func_4635'] = func_4635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4635_call = mutated_mod.get_global_var('func_4635')
var_4637 = relay.var("var_4637", dtype = "float64", shape = (2, 3, 7))#candidate|4637|(2, 3, 7)|var|float64
var_4638 = relay.var("var_4638", dtype = "float64", shape = (1350,))#candidate|4638|(1350,)|var|float64
call_4636 = func_4635_call(var_4637,var_4638,)
output = call_4636
func_4639 = relay.Function([var_4637,var_4638,], output)
mutated_mod['func_4639'] = func_4639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2161_call = mod.get_global_var('func_2161')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_4658 = func_2161_call()
call_4659 = func_2161_call()
output = relay.Tuple([call_4658,])
output2 = relay.Tuple([call_4659,])
func_4663 = relay.Function([], output)
mod['func_4663'] = func_4663
mod = relay.transform.InferType()(mod)
output = func_4663()
func_4664 = relay.Function([], output)
mutated_mod['func_4664'] = func_4664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1980_call = mod.get_global_var('func_1980')
func_1982_call = mutated_mod.get_global_var('func_1982')
call_4703 = relay.TupleGetItem(func_1980_call(), 0)
call_4704 = relay.TupleGetItem(func_1982_call(), 0)
output = relay.Tuple([call_4703,])
output2 = relay.Tuple([call_4704,])
func_4709 = relay.Function([], output)
mod['func_4709'] = func_4709
mod = relay.transform.InferType()(mod)
mutated_mod['func_4709'] = func_4709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4709_call = mutated_mod.get_global_var('func_4709')
call_4710 = func_4709_call()
output = call_4710
func_4711 = relay.Function([], output)
mutated_mod['func_4711'] = func_4711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_4792 = relay.TupleGetItem(func_506_call(), 0)
call_4793 = relay.TupleGetItem(func_507_call(), 0)
uop_4807 = relay.asin(call_4792.astype('float64')) # shape=(1, 3, 1)
uop_4809 = relay.asin(call_4793.astype('float64')) # shape=(1, 3, 1)
uop_4823 = relay.atanh(call_4792.astype('float64')) # shape=(1, 3, 1)
uop_4825 = relay.atanh(call_4793.astype('float64')) # shape=(1, 3, 1)
output = relay.Tuple([uop_4807,uop_4823,])
output2 = relay.Tuple([uop_4809,uop_4825,])
func_4842 = relay.Function([], output)
mod['func_4842'] = func_4842
mod = relay.transform.InferType()(mod)
output = func_4842()
func_4843 = relay.Function([], output)
mutated_mod['func_4843'] = func_4843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1014_call = mod.get_global_var('func_1014')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_4875 = func_1014_call()
call_4876 = func_1014_call()
var_4886 = relay.var("var_4886", dtype = "float32", shape = (14, 3, 16))#candidate|4886|(14, 3, 16)|var|float32
bop_4887 = relay.right_shift(call_4875.astype('int32'), var_4886.astype('int32')) # shape=(14, 3, 16)
bop_4890 = relay.right_shift(call_4876.astype('int32'), var_4886.astype('int32')) # shape=(14, 3, 16)
func_4709_call = mod.get_global_var('func_4709')
func_4711_call = mutated_mod.get_global_var('func_4711')
call_4891 = relay.TupleGetItem(func_4709_call(), 0)
call_4892 = relay.TupleGetItem(func_4711_call(), 0)
output = relay.Tuple([bop_4887,call_4891,])
output2 = relay.Tuple([bop_4890,call_4892,])
func_4893 = relay.Function([var_4886,], output)
mod['func_4893'] = func_4893
mod = relay.transform.InferType()(mod)
var_4894 = relay.var("var_4894", dtype = "float32", shape = (14, 3, 16))#candidate|4894|(14, 3, 16)|var|float32
output = func_4893(var_4894)
func_4895 = relay.Function([var_4894], output)
mutated_mod['func_4895'] = func_4895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4842_call = mod.get_global_var('func_4842')
func_4843_call = mutated_mod.get_global_var('func_4843')
call_4905 = relay.TupleGetItem(func_4842_call(), 0)
call_4906 = relay.TupleGetItem(func_4843_call(), 0)
output = relay.Tuple([call_4905,])
output2 = relay.Tuple([call_4906,])
func_4918 = relay.Function([], output)
mod['func_4918'] = func_4918
mod = relay.transform.InferType()(mod)
output = func_4918()
func_4919 = relay.Function([], output)
mutated_mod['func_4919'] = func_4919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_5000 = func_984_call()
call_5001 = func_984_call()
func_4197_call = mod.get_global_var('func_4197')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_5008 = relay.TupleGetItem(func_4197_call(), 0)
call_5009 = relay.TupleGetItem(func_4199_call(), 0)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_5030 = relay.TupleGetItem(func_468_call(), 3)
call_5031 = relay.TupleGetItem(func_470_call(), 3)
func_4478_call = mod.get_global_var('func_4478')
func_4480_call = mutated_mod.get_global_var('func_4480')
const_5035 = relay.const([2,5,1,-4,-8,-6,9,2,6,3,6,-6,4,-2,-9,-1,10,-4,-2,8,3,-6,1,-10,-4,4,4,2,5,-10,4,5,9,-7,-10,-5,-6,-7,-1,-5,-8,2,-10,-4,8,-9,-7,-6,-6,1,5,-10,5,9,2,10,2,4,8,-7,1,-9,-2,7,8,-5,4,-6,-1,-6,1,-5,-7,7,6,-2,-1,7,5,-1,-2,10,10,-6,2,-5,5,8,-8,7,-8,-1,9,-10,2,1,-8,1,-6,-2,-6,-1,-7,-2,3,-1,10,10,9,-8,-3,-6,-8,2,3,-2,1,1,4,4,-5,-10,6,6,2,-6,-3,-8,9,-4,-4,-1,-10,2,8,-1,3,-9,1,-2,-1,8,1,4,-5,-2,5,-5,-8,8,5,10,-1,6,-8,5,-9,5,8,-1,10,-4,-9,-9,-8,-6,8,-10,6,-1,4,-4,-8,4,10,10,9,2,-5,-8,10,5,-9,-7,10,-9,-3,-9,4,6,7,2,4,-7,-7,-3,8,-2,-4,1,-6,-8,5,-9,-1,5,-5,-5,10,-9,8,3,9,-2,-6,-6,-5,-1,-4,-3,7,2,-4,-10,-2,3,-2,-3,-4,3,9,-4,6,9,10,-2,10,1,-4,8,2,3,10,5,2,-7,9,-7,9,-6,10,7,3,-3,1,-2,-5,-8,-2,10,-3,7,10,-9,-2,9,-3,1,6,-5,-7,9,4,8,10,-2,-7,-7,2,8,-2,-7,3,3,4,-6,6,3,-5,-8,3,10,-8,6,2,6,-1,9,1,-3,1,-5,7,9,-3,6,4,3,-2,1,-5,8,-10,-9,-2,-7,2,-9,2,-2,2,8,-4,9,-1,2,7,-9,-8,9,1,-2,-8,3,-1,-2,2,1,10,-4,10,9,5,-6,6,-4,3,-1,8,-10,10,-2,-1,-10,4,-4,-9,4,10,-10,7,-7,-1,1,4,-10,1,-9,-6,-7,-3,5,-5,8,8,4,-2,-6,-9,4,-6,10,-6,-2,-5,3,2,-2,6,10,5,-7,-7,10,10,1,-6,-3,-9,-5,6,6,5,-2,-5,-2,10,-7,-4,3,9,-10,-7,7,10,4,-9,3,-6,4,-9,2,-10,6,-4,-8,7,7,-10,1,6,5,6,1,5,3,-4,5,2,9,-2,-8,-4,-2,9,4,9,-3,7,6,1,-8,-4,10,4,-3,-6,-5,6,-7,-3,2,-10,8,1,1,-3,7,-2,3,-8,-2,7,-7,7,2,4,-3,-1,6,-6,3,6,9,9,-3,10,1,3,4,1,1,10,-10,6,2,-2,3,7,7,-4,4,8,-1,5,-2,-1,-2,8,1,-7,-7,-10,-1,10,6,2,8,-7,-2,6,1,-8,10,4,-1,-6,3,7,-6,4,3,-4,-6,3,5,2,9,-6,6,-10,-2,5,6,-9,-1,6,9,-6,-1,2,10,-10,2,8,8,6,6,-3,-3,7,-7,7,-3,10,-4,7,-4,1,-5,-5,8,-10,1,9,8,-8,-10,-1,-10,4,3,5,10,-5,-6,-5,2,-9,1,-8,5,-5,3,-8,7,8,-7,9,-1,-2,7,-1,3,1,-9,4,-7,1,-5,4,2,3,-4,-7,-9,4,-8,-4,-9,6,5,4,-9,9,-5,-7,4,-6,-4,-5,-4,10,8,-5,-8,6,1,3,-4,-5,7,6,3,2,-9,-4,-8,6,-8,-4,2,-10,-10,6,-7,-5,-6,-8,6,-8,-6,9,7,-1,-6,1,-5,-2,4,-10,-10,7,-7,5,-4,-8,7,6,3,-9,10,-7,-1,-9,1,-7,-6,7,1,9,-8,8,4,-9,1,6,-8,-6,5,3,9,-7,4,10,-9,-5,-8,2,6,9,-9,-1,-9,3,4,-8,-6,8,10,-7,9,-5,4,-8,-7,10,-1,3,7,4,4,4,8,9,-2,-6,-8,-5,-8,-3,-2,-3,3,5,-1,-1,2,4,7,-7,-10,9,5,10,-9,-8,-7,3,6,10,-6,4,-8,5,2,6,6,7,1,5,-10,10,6,7,-1,9,2,3,-2,9,2,-5,3,4,-1,6,3,-1,1,-1,7,-10,-5,-2,3,10,-7,8,9,7,-10,-3,1,4,-2,-6,4,1,-9,8,-2,-9,-5,2,8,6,-2,-5,-5,-7,-3,-7,7,8,-10,-1,-5,3,9,6,7,-9,2,-4,-10,-3,3,10,7,9,-4,-10,-1,9,-2,-9,-8,10,10,-7,6,-5,-10,-1,3,-6,8,-6,-1,-1,1,-2,8,-8,-7,-1,5,-9,1,3,10,2,5,9,2,-1,-9,9,6,-8,-2,-3,6,-3,-4,2,-4,-3,10,-7,1,-5,-4,8,4,2,-6,5,10,9,-2,9,-3,9,4,8,-5,-6,7,-8,1,-9,4,8,-9,8,-6,-1,9,4,5,9,-5,8,2,-5,5,-1,-7,3,-6,9,-9,-2,-8,4,-10,-3,9,-7,7,-3,5,1,10,7,-6,9,5,-6,8,8,2,-3,3,1,1,10,5,-7,5,3,2,-7,-3,-2,10,1,9,2,-3,2,6,-1,3,-9,3,10,-6,-2,7,-10,-4,-10,4,-7,-6,8,-10,2,-6,-2,5,-4,-8,-7,-2,3,-9,-1,4,7,-6,1,-5,-1,-5,2,4,10,4,-6,-6,4,-1,-8,2,4,-2,6,-9,-8,10,6,-8,6,4,2,-9,7,1,7,-3,-5,-8,-4,-8,3,4,1,-4,8,7,9,-4,7,2,-3,7,-1,9,-3,-8,4,-6,6,10,-9,1,4,-4,5,7,2,3,10,-9,-8,9,-8,5,-6,-5,-3,-5,-4,-9,5,-4,-3,-2,-1,-6,-5,1,2,7,-2,-5,1,-3,8,-5,-2,-2,7,8,5,9,8,5,-7,-8,-7,5,2,6,-1,-3,-9,8,8,-6,-7,-3,4,-7,-2,-9,7,-8,1,8,-4,-5,-5,9,-8,-6,-1,-1,9,-7,2,-8,1,9,2,5,8,7,2,7,-4,-6,4,-9,5,1,-3,8,9,-5,3,-4,-10,4,-8,6,8,6,-9,-4,-2,-4,6,-8,-7,5,-5,-3,-10,8,2,2,6,-1,-3,-1,-9,-2,5,1,5,4,-5,-2,3,-4,6,4,-4,-8,9,-3,-2,-5,-5,9,-4,-7,-9,5,2,7,-5,-1,6,-5,-7,-3,-5,8,-9,-1,1,4,-10,-1,10,10,1,-6,1,1,-2,-8,5,9,4,-6,10,2,1,-2,-1,8,-6,-8,6,6,4,-6,-10,2,7,-9,-10,-6,-4,1,3,-9,6,9,-7,-1,-8,1,-2,-4,-10,5,-3,10,9,5,3,-4,-3,10,-7,4,-5,-5,-5,7,3,-5,1,6,-9,6,6,10,3,1,10,-5,-10,4,-9,-3,1,9], dtype = "int64")#candidate|5035|(1296,)|const|int64
call_5034 = relay.TupleGetItem(func_4478_call(relay.reshape(const_5035.astype('int64'), [9, 12, 12])), 0)
call_5036 = relay.TupleGetItem(func_4480_call(relay.reshape(const_5035.astype('int64'), [9, 12, 12])), 0)
uop_5040 = relay.cos(call_5000.astype('float64')) # shape=(1, 3, 1)
uop_5042 = relay.cos(call_5001.astype('float64')) # shape=(1, 3, 1)
func_1779_call = mod.get_global_var('func_1779')
func_1781_call = mutated_mod.get_global_var('func_1781')
const_5055 = relay.const(-9.647654, dtype = "float64")#candidate|5055|()|const|float64
call_5054 = relay.TupleGetItem(func_1779_call(relay.reshape(const_5055.astype('float64'), [])), 0)
call_5056 = relay.TupleGetItem(func_1781_call(relay.reshape(const_5055.astype('float64'), [])), 0)
func_3887_call = mod.get_global_var('func_3887')
func_3890_call = mutated_mod.get_global_var('func_3890')
var_5058 = relay.var("var_5058", dtype = "float32", shape = (1040,))#candidate|5058|(1040,)|var|float32
const_5059 = relay.const([-2,-3,7,-5,-2,8,-3,5,10,-5,9,-7,-2,6,-9,-5,7,9,3,9,-1,3,1,-1,1,8,-7,-2,3,3,2,3,10,-7,6,-10,-4,10,-2,-6,6,-4,-10,3,6,-5,6,10,-2,8,-3,-4,3,2,-6,10,-4,-6,-1,-10,-5,-5,-5,-6,2,-4,4,1,3,-3,-2,10,7,2,4,-5,7,9,-5,-8,3,-1,1,6,-5,-4,4,-5,-1,-9,7,2,-1,7,-8,-2,-8,-7,7,2,2,9,9,5,10,-4,7,2,-9,-6,5,-5,5,3,-5,1,10,-1,5,10,-1,4,-2,-8,9,-5,3,9,-2,-9,-5,4,4,8,-3,-7,-5,-4,9,-6,-5,-3,1,-10,2,1,10,7,-1,3,3,8,-3,3,-4,2,-9,2,9,-2,9,-2,-9,5,4,-1,10,-5,4,6,-8,-9,-7,7,-3,7,-4,-3,8,10,7,-8,-3,-9,2,4,8,-5,4,-9,10,-9,6,7,1,5,1,3,6,-10,1,-6,-7,2,-4,-6,-8,1,10,-10,-5,7,8,-9,-5,-3,-1,3,-2,9,7,-10,-2,-1,-9,1,5,10,-1,-8,-6,-1,9,-4,1,7,-9,-3,10,-5,-4,-2,6,10,1,-4,-8,3,-8,-8,-2,-7,6,4,-3,-6,7,3,2,-1,-3,9,9,-9,-2,-10,-4,7,-4,-5,-10,-3,10,10,-3,-4,-7,8,-6,-7,-3,-1,1,-6,-9,-3,3,7,5,-5,10,3,-2,-5,7,5,8,-5,-5,7,4,-4,7,-2,1,-9,7,-10,4,-5,7,8,-9,-8,6,10,-5,-10,-8,-5,10,-9,7,-3,-5,1,-2,1,4,6,3,3,-10,2,-5,-6,10,-9,-5,1,5,-5,-3,-10,6,-8,-2,8,-3,-10,5], dtype = "uint64")#candidate|5059|(351,)|const|uint64
call_5057 = relay.TupleGetItem(func_3887_call(relay.reshape(var_5058.astype('float32'), [1040,]), relay.reshape(const_5059.astype('uint64'), [351,]), ), 4)
call_5060 = relay.TupleGetItem(func_3890_call(relay.reshape(var_5058.astype('float32'), [1040,]), relay.reshape(const_5059.astype('uint64'), [351,]), ), 4)
func_4450_call = mod.get_global_var('func_4450')
func_4453_call = mutated_mod.get_global_var('func_4453')
const_5068 = relay.const([-1,7,7,2,1,-4,-5,1,-6,9,-9,7,7,6,-6,6,-7,7,-8,-5,-5,8,-7,1,9,-3,1,4,2,3,-10,-5,-2,2,-3,9,-4,-9,7,-6,2,-7,-9,-10,1,-9,2,10,8,6,-7,-1,-3,3,10,8,-1,4,-8,-1,6,9,-3,4,9,3,6,-10,-4,-10,-4,-6,-5,-5,5,-1,-5,10,9,9,7,-5,-6,3,8,6,-6,-7,5,6,-9,2,7,-9,-10,-6,10,10,-6,8,10,8,-8,-7,-8,-4,9,-8,-10,5,-5,6,2,-3,-1,-4,7,-5,6,10,4,-10,10,9,7,9,-7,-9,-1,9,3,2,-5,7,-10,5,2,7,5,3,2,-4,-9,9,-5,-1,-2,-10,-2,6,7,4,-9,3,-8,4,10,-10,2,8,-6,8,4,4,-9,7,-4,-5,-3,4,7,-3,9,8,3,-1,-9,-6,8,-10,-2,3,8,-8,-8,-6,2,6,3,3,1,4,2,4,9,7,9,-7,9,1,8,4,7,1,3,-5,-7,-6,-8,-1,2,-10,9,1,-5,-5,10,-4,7,-6,-1,-7,-7,-9,3,3,9,10,1,6,-6,8,8,2,7,-8,-8,-9,7,-1,10,-8,7,7,-1,-3,-3,2,5,9,-1,-10,-1,7,7,-10,2,-5,8,-7,6,6,3,1,2,-9,8,-6,-10,-8,-9,-5,-10,9,4,-9,-8,-10,-2,8,-2,9,-8,-8,5,7,-6,-6,5,-4,-3,-1,-7,9,-5,-5,4,8,8,10,4,7,2,-8,-1,7,-7,-3,1,-6,-9,-7,7,-4,-1,-6,4,9,-9,2,-9,-3,7,-3,-8,-9,3,1,-9,-3,-3,-9,6,-2,5,6,3,2,-5,-10,-7,-3,5,10,-1,6,4,1,-3,5,-9,2,10,3,1,2,4,-8,-9,3,-1,-6,-4,3,1,5,-8,-3,-3,6,8,1,1,-1,8,-4,2,-2,-8,8,-4,1,-2,-10,9,-8,-4,-10,-8,9,4,-5,-3,7,-3,-3,7,-8,-8,-3,-6,5,8,7,6,-4,-7,-9,5,2,-8,-2,8,-4,-10,-3,-6,6,-2,1,-7,10,-3,6,2,3,-4,-5,-9,-9,5,-5,8,6,4,-2,2,7,-9,-3,-5,-3,5,1,8,-3,4,4,9,4,9,4,-5,9,6,-9,10,1,-1,-1,4,1,-4,-10,7,6,-9,7,3,-2,-8,1,-2,-7,-5,-9,2,7,-7,1,-2,-9,-9,-6,2,3,-8,10,-9,10,-5,4,-1,5,9,-1,3,1,6,-6,7,8,6,-7,7,10,8,-1,-9,8,-4,-1,1,-9,-1,-5,4,8,-5,8,4,-4,-4,-1,3,2,-10,-4,-5,8,-10,8,8,8,1,-5,-4,7,-6,-2,10,6,-7,1,-5,-9,1,1,-3,3,2,9,7,-5,-4,1,1,4,-8,-1,1,10,-7,-1,7,-6,-10,-7,1,-9,9,1,-7,-9,9,10,1,-3,-8,-1,-8,5,2,-6,-2,-7,5,2,-2,-7,-10,-2,4,1,10,8,-1,-6,5,-5,7,9,-2,3,9,-7,-6,3,-4,3,-8,-2,4,-3,3,7,2,1,-4,-9,4,-5,5,-2,2,-3,-6,9,-6,-10,-10,9,2,7,-4,-2,-2,-3,-3,-6,-10,-5,-3,-8,-7,-7,7,3,6,7,6,-2,-4,-5,-10,2,-9,6,-1,2,3,9,5,-9,-3,3,-6,8,-10,9,-4,-9,7,-7,-10,-10,-8,4,2,6,-10,3,-4,7,7,-5,6,4,-9,-4,9,3,3,-1,-1,-8,-6,10,-5,-5,1,-3,-3,-2,9,-3,-10,-6,-6,-9,5,-1,-10,2,-5,10,-6,7,-2,-4,-5,-1,-5,-7,7,-9,3,5,10,3,-6,-5,5,-4,1,8,-4,8,-8,-2,2,7,-3,1,10,3,4,-10,2,-6,1,8,4,7,-2,7,2,9,6,3,3,-4,5,-8,8,-1,-1,-4,-4,9,2,10,-7,1,7,1,-9,-9,-7,-3,-10,-3,1,5,8,1,-9,-4,-8,-2,-9,6,-6,-4,1,-7,2,-1,-9,10,2,9,-4,10,8,-8,-4,6,-1,-4,-10,3,-3,8,-5,-9,-4,10,1,-10,1,9,6,7,8,8,-4,-3,-7,9,1,-9,-6,1,-1,8,10,-9,-5,-4,8,10,-4,9,3,-5,5,9,5,1,-2,-7,-8,-1,-5,-5,-8,6,-9,-7,-2,7,6,-1,6,6,2,-10,-2,-3,-7,-1,-3,-9,2,5,8,-3,9,-5,7,5,-5,-2,-8,-5,3,-10,-10,1,4,-8,-9,7,7,3,3,7,-4,6,-6,-5,-6,-7,5,-10,5,1,1,2,-10,-5,-4,9,-1,-8,-6,6,-9,10,-3,2,8,-2], dtype = "int64")#candidate|5068|(924,)|const|int64
call_5067 = relay.TupleGetItem(func_4450_call(relay.reshape(const_5068.astype('int64'), [12, 7, 11])), 0)
call_5069 = relay.TupleGetItem(func_4453_call(relay.reshape(const_5068.astype('int64'), [12, 7, 11])), 0)
func_917_call = mod.get_global_var('func_917')
func_919_call = mutated_mod.get_global_var('func_919')
call_5072 = relay.TupleGetItem(func_917_call(), 0)
call_5073 = relay.TupleGetItem(func_919_call(), 0)
output = relay.Tuple([call_5008,call_5030,call_5034,const_5035,uop_5040,call_5054,const_5055,call_5057,var_5058,const_5059,call_5067,const_5068,call_5072,])
output2 = relay.Tuple([call_5009,call_5031,call_5036,const_5035,uop_5042,call_5056,const_5055,call_5060,var_5058,const_5059,call_5069,const_5068,call_5073,])
func_5093 = relay.Function([var_5058,], output)
mod['func_5093'] = func_5093
mod = relay.transform.InferType()(mod)
var_5094 = relay.var("var_5094", dtype = "float32", shape = (1040,))#candidate|5094|(1040,)|var|float32
output = func_5093(var_5094)
func_5095 = relay.Function([var_5094], output)
mutated_mod['func_5095'] = func_5095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_5208 = func_4335_call()
call_5209 = func_4335_call()
uop_5211 = relay.exp(call_5208.astype('float32')) # shape=(7, 9, 9)
uop_5213 = relay.exp(call_5209.astype('float32')) # shape=(7, 9, 9)
func_2726_call = mod.get_global_var('func_2726')
func_2727_call = mutated_mod.get_global_var('func_2727')
call_5216 = relay.TupleGetItem(func_2726_call(), 0)
call_5217 = relay.TupleGetItem(func_2727_call(), 0)
func_2142_call = mod.get_global_var('func_2142')
func_2143_call = mutated_mod.get_global_var('func_2143')
call_5218 = relay.TupleGetItem(func_2142_call(), 0)
call_5219 = relay.TupleGetItem(func_2143_call(), 0)
uop_5229 = relay.sinh(call_5218.astype('float32')) # shape=(1, 3, 1)
uop_5231 = relay.sinh(call_5219.astype('float32')) # shape=(1, 3, 1)
uop_5234 = relay.tan(uop_5211.astype('float32')) # shape=(7, 9, 9)
uop_5236 = relay.tan(uop_5213.astype('float32')) # shape=(7, 9, 9)
func_4284_call = mod.get_global_var('func_4284')
func_4286_call = mutated_mod.get_global_var('func_4286')
call_5241 = relay.TupleGetItem(func_4284_call(), 2)
call_5242 = relay.TupleGetItem(func_4286_call(), 2)
output = relay.Tuple([call_5216,uop_5229,uop_5234,call_5241,])
output2 = relay.Tuple([call_5217,uop_5231,uop_5236,call_5242,])
func_5244 = relay.Function([], output)
mod['func_5244'] = func_5244
mod = relay.transform.InferType()(mod)
mutated_mod['func_5244'] = func_5244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5244_call = mutated_mod.get_global_var('func_5244')
call_5245 = func_5244_call()
output = call_5245
func_5246 = relay.Function([], output)
mutated_mod['func_5246'] = func_5246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4842_call = mod.get_global_var('func_4842')
func_4843_call = mutated_mod.get_global_var('func_4843')
call_5271 = relay.TupleGetItem(func_4842_call(), 0)
call_5272 = relay.TupleGetItem(func_4843_call(), 0)
func_4709_call = mod.get_global_var('func_4709')
func_4711_call = mutated_mod.get_global_var('func_4711')
call_5280 = relay.TupleGetItem(func_4709_call(), 0)
call_5281 = relay.TupleGetItem(func_4711_call(), 0)
uop_5309 = relay.atan(call_5280.astype('float32')) # shape=(1, 3, 1)
uop_5311 = relay.atan(call_5281.astype('float32')) # shape=(1, 3, 1)
var_5315 = relay.var("var_5315", dtype = "float64", shape = (16, 3, 7))#candidate|5315|(16, 3, 7)|var|float64
bop_5316 = relay.bitwise_or(call_5271.astype('int16'), var_5315.astype('int16')) # shape=(16, 3, 7)
bop_5319 = relay.bitwise_or(call_5272.astype('int16'), var_5315.astype('int16')) # shape=(16, 3, 7)
output = relay.Tuple([uop_5309,bop_5316,])
output2 = relay.Tuple([uop_5311,bop_5319,])
func_5320 = relay.Function([var_5315,], output)
mod['func_5320'] = func_5320
mod = relay.transform.InferType()(mod)
mutated_mod['func_5320'] = func_5320
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5321 = relay.var("var_5321", dtype = "float64", shape = (16, 3, 7))#candidate|5321|(16, 3, 7)|var|float64
func_5320_call = mutated_mod.get_global_var('func_5320')
call_5322 = func_5320_call(var_5321)
output = call_5322
func_5323 = relay.Function([var_5321], output)
mutated_mod['func_5323'] = func_5323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2218_call = mod.get_global_var('func_2218')
func_2220_call = mutated_mod.get_global_var('func_2220')
call_5334 = relay.TupleGetItem(func_2218_call(), 0)
call_5335 = relay.TupleGetItem(func_2220_call(), 0)
output = relay.Tuple([call_5334,])
output2 = relay.Tuple([call_5335,])
func_5348 = relay.Function([], output)
mod['func_5348'] = func_5348
mod = relay.transform.InferType()(mod)
mutated_mod['func_5348'] = func_5348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5348_call = mutated_mod.get_global_var('func_5348')
call_5349 = func_5348_call()
output = call_5349
func_5350 = relay.Function([], output)
mutated_mod['func_5350'] = func_5350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_5362 = func_984_call()
call_5363 = func_984_call()
func_3300_call = mod.get_global_var('func_3300')
func_3302_call = mutated_mod.get_global_var('func_3302')
var_5374 = relay.var("var_5374", dtype = "float32", shape = (18,))#candidate|5374|(18,)|var|float32
call_5373 = relay.TupleGetItem(func_3300_call(relay.reshape(var_5374.astype('float32'), [18,])), 3)
call_5375 = relay.TupleGetItem(func_3302_call(relay.reshape(var_5374.astype('float32'), [18,])), 3)
output = relay.Tuple([call_5362,call_5373,var_5374,])
output2 = relay.Tuple([call_5363,call_5375,var_5374,])
func_5383 = relay.Function([var_5374,], output)
mod['func_5383'] = func_5383
mod = relay.transform.InferType()(mod)
var_5384 = relay.var("var_5384", dtype = "float32", shape = (18,))#candidate|5384|(18,)|var|float32
output = func_5383(var_5384)
func_5385 = relay.Function([var_5384], output)
mutated_mod['func_5385'] = func_5385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_890_call = mod.get_global_var('func_890')
func_891_call = mutated_mod.get_global_var('func_891')
call_5398 = relay.TupleGetItem(func_890_call(), 3)
call_5399 = relay.TupleGetItem(func_891_call(), 3)
output = relay.Tuple([call_5398,])
output2 = relay.Tuple([call_5399,])
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
var_5408 = relay.var("var_5408", dtype = "float64", shape = (1, 8, 15))#candidate|5408|(1, 8, 15)|var|float64
uop_5409 = relay.cosh(var_5408.astype('float64')) # shape=(1, 8, 15)
bop_5411 = relay.bitwise_or(var_5408.astype('uint8'), relay.reshape(uop_5409.astype('uint8'), relay.shape_of(var_5408))) # shape=(1, 8, 15)
uop_5418 = relay.sqrt(var_5408.astype('float64')) # shape=(1, 8, 15)
func_1867_call = mod.get_global_var('func_1867')
func_1869_call = mutated_mod.get_global_var('func_1869')
call_5428 = relay.TupleGetItem(func_1867_call(), 1)
call_5429 = relay.TupleGetItem(func_1869_call(), 1)
output = relay.Tuple([bop_5411,uop_5418,call_5428,])
output2 = relay.Tuple([bop_5411,uop_5418,call_5429,])
func_5434 = relay.Function([var_5408,], output)
mod['func_5434'] = func_5434
mod = relay.transform.InferType()(mod)
var_5435 = relay.var("var_5435", dtype = "float64", shape = (1, 8, 15))#candidate|5435|(1, 8, 15)|var|float64
output = func_5434(var_5435)
func_5436 = relay.Function([var_5435], output)
mutated_mod['func_5436'] = func_5436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_5482 = relay.TupleGetItem(func_2813_call(), 0)
call_5483 = relay.TupleGetItem(func_2814_call(), 0)
var_5537 = relay.var("var_5537", dtype = "float32", shape = (16, 3, 12))#candidate|5537|(16, 3, 12)|var|float32
bop_5538 = relay.bitwise_xor(call_5482.astype('int64'), var_5537.astype('int64')) # shape=(16, 3, 12)
bop_5541 = relay.bitwise_xor(call_5483.astype('int64'), var_5537.astype('int64')) # shape=(16, 3, 12)
func_1080_call = mod.get_global_var('func_1080')
func_1082_call = mutated_mod.get_global_var('func_1082')
var_5570 = relay.var("var_5570", dtype = "int32", shape = (378,))#candidate|5570|(378,)|var|int32
call_5569 = func_1080_call(relay.reshape(var_5570.astype('int32'), [3, 14, 9]))
call_5571 = func_1080_call(relay.reshape(var_5570.astype('int32'), [3, 14, 9]))
output = relay.Tuple([bop_5538,call_5569,var_5570,])
output2 = relay.Tuple([bop_5541,call_5571,var_5570,])
func_5580 = relay.Function([var_5537,var_5570,], output)
mod['func_5580'] = func_5580
mod = relay.transform.InferType()(mod)
var_5581 = relay.var("var_5581", dtype = "float32", shape = (16, 3, 12))#candidate|5581|(16, 3, 12)|var|float32
var_5582 = relay.var("var_5582", dtype = "int32", shape = (378,))#candidate|5582|(378,)|var|int32
output = func_5580(var_5581,var_5582,)
func_5583 = relay.Function([var_5581,var_5582,], output)
mutated_mod['func_5583'] = func_5583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1404_call = mod.get_global_var('func_1404')
func_1406_call = mutated_mod.get_global_var('func_1406')
call_5626 = func_1404_call()
call_5627 = func_1404_call()
output = call_5626
output2 = call_5627
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
func_2161_call = mod.get_global_var('func_2161')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_5844 = func_2161_call()
call_5845 = func_2161_call()
func_541_call = mod.get_global_var('func_541')
func_542_call = mutated_mod.get_global_var('func_542')
call_5848 = relay.TupleGetItem(func_541_call(), 0)
call_5849 = relay.TupleGetItem(func_542_call(), 0)
func_5631_call = mod.get_global_var('func_5631')
func_5633_call = mutated_mod.get_global_var('func_5633')
call_5852 = func_5631_call()
call_5853 = func_5631_call()
func_5631_call = mod.get_global_var('func_5631')
func_5633_call = mutated_mod.get_global_var('func_5633')
call_5855 = func_5631_call()
call_5856 = func_5631_call()
func_3223_call = mod.get_global_var('func_3223')
func_3226_call = mutated_mod.get_global_var('func_3226')
const_5863 = relay.const(8.404279, dtype = "float64")#candidate|5863|()|const|float64
call_5862 = relay.TupleGetItem(func_3223_call(relay.reshape(const_5863.astype('float64'), [])), 1)
call_5864 = relay.TupleGetItem(func_3226_call(relay.reshape(const_5863.astype('float64'), [])), 1)
bop_5865 = relay.logical_xor(call_5862.astype('int64'), relay.reshape(call_5852.astype('int64'), relay.shape_of(call_5862))) # shape=(1, 3, 1)
bop_5868 = relay.logical_xor(call_5864.astype('int64'), relay.reshape(call_5853.astype('int64'), relay.shape_of(call_5864))) # shape=(1, 3, 1)
func_1779_call = mod.get_global_var('func_1779')
func_1781_call = mutated_mod.get_global_var('func_1781')
call_5872 = relay.TupleGetItem(func_1779_call(relay.reshape(const_5863.astype('float64'), [])), 0)
call_5873 = relay.TupleGetItem(func_1781_call(relay.reshape(const_5863.astype('float64'), [])), 0)
output = relay.Tuple([call_5844,call_5848,call_5855,const_5863,bop_5865,call_5872,])
output2 = relay.Tuple([call_5845,call_5849,call_5856,const_5863,bop_5868,call_5873,])
func_5874 = relay.Function([], output)
mod['func_5874'] = func_5874
mod = relay.transform.InferType()(mod)
mutated_mod['func_5874'] = func_5874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5874_call = mutated_mod.get_global_var('func_5874')
call_5875 = func_5874_call()
output = call_5875
func_5876 = relay.Function([], output)
mutated_mod['func_5876'] = func_5876
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5877 = relay.var("var_5877", dtype = "float64", shape = (1, 14, 1))#candidate|5877|(1, 14, 1)|var|float64
var_5878 = relay.var("var_5878", dtype = "float64", shape = (12, 14, 11))#candidate|5878|(12, 14, 11)|var|float64
bop_5879 = relay.add(var_5877.astype('float64'), var_5878.astype('float64')) # shape=(12, 14, 11)
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_5884 = func_984_call()
call_5885 = func_984_call()
output = relay.Tuple([bop_5879,call_5884,])
output2 = relay.Tuple([bop_5879,call_5885,])
func_5888 = relay.Function([var_5877,var_5878,], output)
mod['func_5888'] = func_5888
mod = relay.transform.InferType()(mod)
mutated_mod['func_5888'] = func_5888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5888_call = mutated_mod.get_global_var('func_5888')
var_5890 = relay.var("var_5890", dtype = "float64", shape = (1, 14, 1))#candidate|5890|(1, 14, 1)|var|float64
var_5891 = relay.var("var_5891", dtype = "float64", shape = (12, 14, 11))#candidate|5891|(12, 14, 11)|var|float64
call_5889 = func_5888_call(var_5890,var_5891,)
output = call_5889
func_5892 = relay.Function([var_5890,var_5891,], output)
mutated_mod['func_5892'] = func_5892
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5970 = relay.var("var_5970", dtype = "float64", shape = (14, 2, 10))#candidate|5970|(14, 2, 10)|var|float64
uop_5971 = relay.erf(var_5970.astype('float64')) # shape=(14, 2, 10)
output = uop_5971
output2 = uop_5971
func_5974 = relay.Function([var_5970,], output)
mod['func_5974'] = func_5974
mod = relay.transform.InferType()(mod)
var_5975 = relay.var("var_5975", dtype = "float64", shape = (14, 2, 10))#candidate|5975|(14, 2, 10)|var|float64
output = func_5974(var_5975)
func_5976 = relay.Function([var_5975], output)
mutated_mod['func_5976'] = func_5976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1170_call = mod.get_global_var('func_1170')
func_1171_call = mutated_mod.get_global_var('func_1171')
call_6001 = func_1170_call()
call_6002 = func_1170_call()
var_6009 = relay.var("var_6009", dtype = "float64", shape = (16, 3, 6))#candidate|6009|(16, 3, 6)|var|float64
bop_6010 = relay.bitwise_xor(call_6001.astype('uint8'), var_6009.astype('uint8')) # shape=(16, 3, 6)
bop_6013 = relay.bitwise_xor(call_6002.astype('uint8'), var_6009.astype('uint8')) # shape=(16, 3, 6)
func_5244_call = mod.get_global_var('func_5244')
func_5246_call = mutated_mod.get_global_var('func_5246')
call_6017 = relay.TupleGetItem(func_5244_call(), 0)
call_6018 = relay.TupleGetItem(func_5246_call(), 0)
bop_6020 = relay.minimum(bop_6010.astype('int32'), call_6001.astype('int32')) # shape=(16, 3, 6)
bop_6023 = relay.minimum(bop_6013.astype('int32'), call_6002.astype('int32')) # shape=(16, 3, 6)
func_4539_call = mod.get_global_var('func_4539')
func_4540_call = mutated_mod.get_global_var('func_4540')
call_6024 = relay.TupleGetItem(func_4539_call(), 1)
call_6025 = relay.TupleGetItem(func_4540_call(), 1)
func_3473_call = mod.get_global_var('func_3473')
func_3475_call = mutated_mod.get_global_var('func_3475')
call_6030 = relay.TupleGetItem(func_3473_call(), 0)
call_6031 = relay.TupleGetItem(func_3475_call(), 0)
bop_6035 = relay.right_shift(call_6024.astype('int8'), bop_6020.astype('int8')) # shape=(16, 3, 6)
bop_6038 = relay.right_shift(call_6025.astype('int8'), bop_6023.astype('int8')) # shape=(16, 3, 6)
func_4478_call = mod.get_global_var('func_4478')
func_4480_call = mutated_mod.get_global_var('func_4480')
const_6040 = relay.const([-1,-5,3,2,-8,8,7,-5,5,-1,5,-3,7,-8,-7,-4,-6,-1,-1,-1,-3,-5,5,9,5,-8,-5,1,-6,-8,-2,1,-3,10,-7,-3,10,-3,1,-8,3,5,6,1,4,4,4,-7,10,-1,10,7,3,6,1,10,-9,-5,-2,-6,-6,6,6,6,-3,-2,2,-3,-1,-1,-3,8,8,9,-2,10,-5,-9,-2,-6,-2,5,10,-1,7,5,4,5,9,-4,9,8,-2,5,-1,-8,3,-9,1,6,-3,-1,-4,-9,-8,-3,-8,-1,5,-4,-8,1,6,-4,1,7,9,-1,2,-8,-4,9,10,-2,-5,5,-9,-3,-6,3,7,1,8,10,1,-4,7,-9,-3,-5,-9,2,-5,-4,3,8,9,-7,1,-9,-5,1,6,10,1,8,6,-10,6,-3,3,-9,3,9,3,-8,1,-2,-9,6,8,2,3,-8,-7,-6,-4,-3,2,3,-10,-6,2,7,10,3,-7,-3,-6,9,-2,4,-1,7,8,1,-2,-10,4,-6,-3,4,4,2,8,3,-8,10,-5,5,6,5,4,2,5,4,-7,-9,6,10,5,-8,2,2,-4,5,2,7,5,6,7,7,-6,4,-10,-8,8,7,3,-9,6,-6,-4,-6,4,9,10,5,4,8,4,8,1,1,-5,-8,6,9,8,-9,5,-4,-3,1,-10,3,4,-5,-7,8,9,-2,1,-5,7,3,-3,9,6,5,-10,8,-10,-8,9,8,1,5,1,2,5,2,-2,5,-2,4,1,-5,-4,7,-8,-3,4,4,7,5,-1,1,-9,-1,-1,10,-6,-2,-7,-6,-5,-5,-9,6,5,10,-10,1,-9,10,-7,1,-5,-4,3,9,-2,-9,-5,7,-8,-8,-9,-10,1,-8,2,2,2,2,-9,-5,9,-10,-1,-6,7,9,-5,4,-1,-6,2,2,5,3,-7,5,-2,-10,-3,2,-2,-5,4,-5,-2,9,3,1,-7,4,-1,-10,3,8,8,-5,2,9,1,-2,9,8,5,9,-4,-6,9,9,-5,9,8,-6,-6,-8,-1,10,4,-9,7,-8,1,7,-9,-2,-5,10,5,-4,10,-7,-2,10,-5,4,-7,7,6,7,-2,2,2,-3,-7,-9,10,-10,5,10,-7,5,7,-3,6,10,1,-9,3,1,10,-9,-7,3,-8,-3,-5,10,-8,7,-3,6,-9,6,-7,-4,-6,-5,3,-5,1,8,6,-10,-3,10,5,9,-1,6,3,-4,2,-3,9,7,-8,8,3,8,-4,-1,6,-3,-8,-6,-8,1,2,-6,-6,1,-8,-9,6,6,-8,8,-8,3,-1,-8,-9,-10,6,4,-9,-7,-3,-7,-6,8,1,-9,9,6,1,9,-4,3,-5,4,-1,2,-9,-4,1,8,1,10,1,2,-1,-4,-9,4,5,9,-1,1,-9,5,-8,-1,-2,9,-8,-7,-1,1,7,6,-5,9,8,-6,-8,7,5,5,9,-3,4,-6,-9,6,4,2,-9,-7,-3,-3,3,-7,8,-6,-5,-5,-8,-5,-8,7,-3,3,-9,6,-1,-3,9,-5,-3,5,1,-8,-3,-8,-3,4,1,5,-6,-2,-2,-5,6,-9,2,-6,5,2,8,-8,-2,-7,8,10,5,-4,6,7,9,10,9,4,9,-2,3,-8,-2,7,8,-5,1,1,1,1,3,3,7,-8,1,-5,-9,1,-9,1,-8,-2,8,-8,1,-10,3,8,9,8,5,-6,6,4,-8,5,-1,-6,-2,9,6,-10,5,8,-4,-5,8,3,-1,-1,2,-4,5,-4,-4,10,6,-8,-10,4,3,-4,3,6,4,4,7,1,-7,9,-9,5,1,-4,-2,-6,10,-5,-7,6,2,7,7,1,2,9,-3,5,-8,4,9,-2,-9,-1,-1,8,-6,-3,3,-9,8,-6,-2,4,4,-7,-7,2,-9,-2,10,4,-5,3,2,4,-1,10,3,-1,-3,10,1,-8,6,9,-10,-4,-1,-4,8,-3,-8,10,9,10,4,-4,3,5,1,-5,-8,-7,-5,-2,-7,-4,9,10,-9,-2,2,8,-7,5,9,-1,1,8,9,3,-4,-2,-10,3,-5,-2,10,-2,-3,8,-9,10,7,7,7,-3,-4,-6,-9,4,5,-9,-6,-3,-8,-2,10,-6,-10,-4,-3,-10,1,-1,-6,-4,-1,-5,4,5,-8,8,8,6,8,-9,-6,10,-6,10,8,-4,-7,-7,6,4,8,4,7,-8,-10,8,5,-7,-10,4,1,6,-6,10,4,5,-7,10,9,-10,4,-8,7,1,-2,-3,2,2,4,-9,7,2,5,9,1,-6,7,-5,7,2,-10,2,-6,-1,8,9,-6,-1,-5,8,8,-1,5,-1,-2,2,8,6,-10,-4,-7,-6,-6,-5,-7,-6,-6,-4,-5,-3,-8,8,1,-1,1,1,-10,2,-6,-8,-1,-8,3,5,-6,6,-5,1,-10,-7,10,10,7,-8,8,-3,-2,5,-2,-5,9,4,8,2,-8,9,-8,-9,-1,-9,-3,-10,-5,2,5,6,9,-10,5,-4,-10,2,2,-5,8,-5,-6,8,10,-9,-7,9,-6,4,-10,6,-3,-9,2,9,-6,3,-7,-3,10,2,-8,-7,1,-8,2,-2,-4,10,-3,-6,-1,-2,9,-7,-7,10,1,2,1,-4,5,7,-7,5,-6,-10,1,7,-7,-1,-5,-4,10,-8,-7,3,-8,-3,-7,-4,1,-2,-6,-4,-5,-9,-8,9,-8,-9,1,9,4,4,-2,6,4,6,7,5,5,-4,-7,-10,-2,-4,-1,-2,-4,-6,-5,-10,10,-9,5,3,-9,2,-2,3,-1,4,-9,-9,-3,1,-9,8,-8,10,-2,5,10,7,2,-5,-6,-7,5,2,-10,5,6,9,-2,-7,-2,6,-10,3,3,-4,-6,8,6,-9,-2,6,-10,2,-3,-6,9,-8,-3,2,-10,-6,9,8,-1,2,3,-1,-2,-3,-2,-2,9,2,3,-9,-2,9,-7,7,-6,-3,-4,10,-7,-2,1,2,4,-3,7,7,-7,3,5,-3,-8,10,3,9,-2,-1,-3,-5,6,-3,2,-4,-8,4,-4,4,7,3,3,-2,-3,10,-5,-2,-4,5,4,-6,4,-8,1,2,8,-8,9,8,4,-7,-2,1,5,4,5,6,2,-10,5,-10,9,-6,9,-10,9,-3,10,6,10,-7,-10,4,6,-4,6,-6,2,-3,3,4,-3,-4,1,-8,-10,3,9,-1,-1,-6,8,4,-1,9,-10,-7,-9,6,2,10,3,1,1,5,-8,-1,-10,-4,-1,6,-7,-6,5,-6,-8,-9,10,-10,-6,4,-5,-8,-1,-5,-7,-4,7,1,-2,9,3,-10,1,-3,7,1,-6,7,1,-10,5,3,3,-4,-2,6,4,-8,8,-2], dtype = "int64")#candidate|6040|(1296,)|const|int64
call_6039 = relay.TupleGetItem(func_4478_call(relay.reshape(const_6040.astype('int64'), [9, 12, 12])), 0)
call_6041 = relay.TupleGetItem(func_4480_call(relay.reshape(const_6040.astype('int64'), [9, 12, 12])), 0)
var_6042 = relay.var("var_6042", dtype = "int8", shape = (16, 3, 6))#candidate|6042|(16, 3, 6)|var|int8
bop_6043 = relay.floor_mod(bop_6035.astype('float32'), relay.reshape(var_6042.astype('float32'), relay.shape_of(bop_6035))) # shape=(16, 3, 6)
bop_6046 = relay.floor_mod(bop_6038.astype('float32'), relay.reshape(var_6042.astype('float32'), relay.shape_of(bop_6038))) # shape=(16, 3, 6)
func_2515_call = mod.get_global_var('func_2515')
func_2517_call = mutated_mod.get_global_var('func_2517')
call_6048 = relay.TupleGetItem(func_2515_call(), 0)
call_6049 = relay.TupleGetItem(func_2517_call(), 0)
bop_6051 = relay.minimum(call_6048.astype('uint32'), const_6040.astype('uint32')) # shape=(1, 3, 1296)
bop_6054 = relay.minimum(call_6049.astype('uint32'), const_6040.astype('uint32')) # shape=(1, 3, 1296)
var_6055 = relay.var("var_6055", dtype = "float64", shape = (16, 3, 15))#candidate|6055|(16, 3, 15)|var|float64
bop_6056 = relay.power(call_6030.astype('float32'), var_6055.astype('float32')) # shape=(16, 3, 15)
bop_6059 = relay.power(call_6031.astype('float32'), var_6055.astype('float32')) # shape=(16, 3, 15)
uop_6063 = relay.log10(bop_6051.astype('float64')) # shape=(1, 3, 1296)
uop_6065 = relay.log10(bop_6054.astype('float64')) # shape=(1, 3, 1296)
output = relay.Tuple([call_6017,call_6039,bop_6043,bop_6056,uop_6063,])
output2 = relay.Tuple([call_6018,call_6041,bop_6046,bop_6059,uop_6065,])
func_6091 = relay.Function([var_6009,var_6042,var_6055,], output)
mod['func_6091'] = func_6091
mod = relay.transform.InferType()(mod)
mutated_mod['func_6091'] = func_6091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6091_call = mutated_mod.get_global_var('func_6091')
var_6093 = relay.var("var_6093", dtype = "float64", shape = (16, 3, 6))#candidate|6093|(16, 3, 6)|var|float64
var_6094 = relay.var("var_6094", dtype = "int8", shape = (16, 3, 6))#candidate|6094|(16, 3, 6)|var|int8
var_6095 = relay.var("var_6095", dtype = "float64", shape = (16, 3, 15))#candidate|6095|(16, 3, 15)|var|float64
call_6092 = func_6091_call(var_6093,var_6094,var_6095,)
output = call_6092
func_6096 = relay.Function([var_6093,var_6094,var_6095,], output)
mutated_mod['func_6096'] = func_6096
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6100 = relay.const([[[1,7,9,3,-5,7,5,1,-4,-10,-10,-4,-3,6,7,6],[-1,-6,-8,-8,-5,9,2,-6,4,9,8,-6,8,-9,-5,-5],[-7,-7,-1,2,-2,6,10,4,5,-7,-7,-4,-7,10,-9,8],[-9,2,4,5,-4,1,2,-9,9,2,9,10,8,-9,8,-2],[4,6,8,3,-4,-6,-10,-5,-3,6,10,9,8,4,5,3],[-10,7,-10,-9,-7,-3,2,-7,-5,-6,-8,5,-2,4,-5,-7],[5,2,-6,-2,-6,9,4,-10,8,-6,-10,4,1,1,6,2],[4,7,-3,-3,5,-6,6,8,3,-2,-6,-8,4,-7,-7,-2],[-3,1,9,6,5,-10,9,7,-1,-6,3,8,-3,-8,3,1]],[[8,-1,-7,-10,6,-3,8,-8,9,8,8,-1,-10,-1,-8,7],[6,4,3,-4,-6,6,7,2,10,7,-7,-10,7,8,-6,5],[2,-3,-5,-6,4,-4,-9,-8,-8,6,-5,-10,10,10,-4,-5],[-6,1,-5,-4,-2,3,-5,-8,-8,-10,-3,-5,-10,-6,-2,9],[9,-1,1,-7,-4,-2,-3,-5,9,2,-6,2,4,10,-10,5],[-1,6,-4,4,-3,-8,-1,7,-8,9,-8,2,10,9,3,1],[-2,7,-10,-3,-9,1,-6,7,9,-10,8,10,-3,10,-5,-9],[8,1,7,2,7,-4,-4,-6,7,-2,7,-3,-3,4,3,-2],[-9,8,-9,2,6,10,6,-4,4,-10,-8,-1,7,6,1,1]],[[-3,8,9,-9,-7,-6,-6,10,6,1,2,-2,9,8,-6,-2],[6,-10,-1,4,7,-4,2,-3,1,-10,-5,-1,2,4,6,8],[7,1,-6,-7,4,-8,-5,-5,-4,-9,-9,3,8,9,3,-10],[-7,10,5,-8,1,7,6,10,7,1,10,9,-1,-5,-8,-7],[-3,8,-6,-7,2,-1,-6,-10,-2,10,5,3,-8,4,-1,-8],[-10,4,-3,-3,7,-7,6,-7,-8,-2,4,1,-2,-7,6,1],[4,-1,6,-3,-7,5,8,2,9,-9,9,-7,4,6,-1,-7],[-2,-3,-2,3,-7,-5,-2,-10,-2,6,-10,-2,6,8,7,-6],[4,9,-6,-7,5,-9,-10,-8,10,2,4,8,-4,-1,10,1]],[[-5,-9,-5,5,10,-6,2,3,-7,-4,10,5,6,6,1,9],[-10,-8,-7,-4,6,-9,6,-10,8,-6,-6,4,-4,8,-8,5],[9,2,8,-5,7,-5,-8,6,1,-6,-10,8,1,-1,-7,6],[10,2,-3,2,-2,3,-4,-6,10,1,-2,-3,-7,9,-1,-7],[-2,-10,-7,9,1,-9,-10,7,9,-9,7,4,-8,-7,10,3],[5,9,6,-1,-9,-2,-7,10,-9,7,-2,-9,5,-3,-1,7],[10,8,-5,2,9,-6,5,2,-6,9,9,-10,5,9,10,2],[3,5,-8,3,-3,4,2,1,5,6,7,10,9,-7,-3,-10],[-10,-4,4,-6,4,-4,-3,6,2,-4,10,-10,-1,-10,8,3]],[[-5,-8,4,-7,-3,-9,-5,-6,7,-7,-4,-7,-5,-1,9,3],[-3,-4,-5,7,9,6,-1,2,-2,4,-7,1,10,-7,8,-2],[2,-7,-4,-5,-10,-8,3,8,8,-1,5,-6,-6,3,-4,-6],[-10,3,9,8,1,10,-5,-9,-2,-9,-4,3,10,5,-2,2],[4,-7,-5,2,-10,-10,-3,-1,9,4,-5,-5,-5,-2,-1,-9],[10,-8,1,-1,-4,-10,-9,-4,1,4,-6,-2,7,-10,-8,5],[-4,-5,3,-6,8,-4,6,-7,-7,-4,8,-6,2,5,-4,10],[-3,1,-2,3,-4,6,6,-9,-4,7,-1,-9,8,2,4,8],[-6,1,9,-7,2,4,-9,-2,6,-5,2,-9,-7,2,3,-7]],[[10,-5,4,1,5,4,10,7,5,2,-5,8,2,-1,10,1],[6,1,10,-5,-9,1,5,5,1,9,-8,7,-7,-2,8,10],[-1,-5,-3,8,-9,1,-6,-6,-2,4,-2,-10,1,7,-9,-5],[-6,-3,-1,2,7,-6,8,3,-6,1,-8,-8,-7,10,2,6],[6,-8,8,8,3,-2,7,2,2,1,8,-1,-4,9,-6,5],[-4,-2,-5,2,6,9,-9,7,8,-1,9,9,3,-1,-7,-3],[-3,5,-5,6,-1,5,7,9,-9,-2,-2,-4,-3,6,-1,-10],[3,-2,2,-2,-4,1,8,-1,-2,-5,-3,1,-4,-3,7,-1],[9,-1,-3,4,-1,-3,8,-3,-6,-7,9,-5,7,8,-3,6]],[[-2,5,-1,7,5,-8,3,-3,2,-7,2,-4,2,-4,-2,-9],[5,-2,-2,-8,-8,-7,-10,7,2,4,6,2,-1,2,-5,8],[4,10,-10,10,5,-8,-8,6,10,6,10,-3,6,-4,8,-3],[-3,-6,-1,10,4,10,2,-3,-8,8,9,-10,-1,-6,-6,9],[3,-4,-2,10,-2,-7,8,9,-1,3,2,-4,8,10,-10,7],[4,6,8,1,6,-8,-10,-10,6,2,9,-1,-6,4,1,7],[-3,-1,-1,-2,-10,3,7,-2,9,3,10,8,6,-9,-3,2],[1,8,-6,1,3,10,7,7,6,7,-5,-1,7,7,8,8],[3,-3,10,-8,6,-7,8,1,3,1,3,8,-3,1,-4,-3]]], dtype = "int64")#candidate|6100|(7, 9, 16)|const|int64
const_6101 = relay.const([[[5,-8,-7,5,-8,-2,-8,4,-8,-9,1,-3,1,2,7,9],[-8,-10,-7,-8,-4,5,-7,9,1,4,-9,-9,-10,-2,-10,1],[-5,-4,-8,9,-3,5,-5,-5,6,10,-8,-8,1,5,10,-1],[9,-9,-8,-8,-5,10,1,8,-7,-5,-1,-3,-2,4,-6,-10],[10,1,-10,-8,-4,-4,-6,-2,-5,9,-9,-8,3,-4,-9,-4],[-4,9,-4,8,9,-2,-8,-9,-9,-1,-3,1,3,4,10,4],[-3,-9,-2,-6,10,-6,-10,3,5,10,-3,1,6,9,-5,1],[6,6,8,-8,10,9,1,1,-4,-4,-2,2,-2,6,-3,-9],[9,-8,-9,-7,4,-9,6,1,-1,-6,1,10,8,-3,5,2]],[[9,-10,8,-5,3,-7,2,-8,4,5,-1,-9,3,4,5,-9],[-5,1,8,8,-10,2,-5,-6,-6,4,-7,8,8,7,7,-8],[-7,-10,6,8,-2,-9,-3,-8,5,-6,-9,-2,8,2,5,10],[10,-1,-7,-6,1,8,10,1,-9,10,3,7,-1,-9,-9,-2],[-8,-9,2,-5,-9,-7,8,4,6,7,6,-5,3,7,2,4],[4,6,-9,1,4,8,-5,-1,-8,2,-6,-3,10,2,-3,5],[-8,-3,2,6,1,9,-6,-9,-3,-8,-10,8,5,4,-4,3],[-10,10,2,1,10,1,2,-10,-3,-6,1,2,3,4,-5,-3],[5,10,-9,-1,10,-5,-2,-1,-3,-5,-10,10,3,1,1,4]],[[7,-5,4,7,10,8,7,6,-6,-2,-9,10,-6,-1,-6,5],[10,2,-8,8,1,9,-7,5,5,2,2,8,-4,9,6,3],[-5,-10,6,-10,-5,-4,-3,10,10,4,1,-2,-10,4,4,-2],[4,4,1,8,5,2,5,-10,1,9,-5,-8,-3,-3,-2,7],[-8,-6,7,6,-8,-3,-8,7,6,-3,6,-8,-6,7,-7,-1],[-5,5,-3,-5,-1,3,1,1,6,8,7,-3,6,-10,4,9],[10,-3,-7,5,9,7,8,7,4,-9,1,4,2,4,5,7],[-9,10,1,6,-3,-1,-3,-8,6,-7,-9,-6,-5,9,4,-7],[6,-1,-5,6,1,1,-6,8,6,8,-8,-8,-5,-5,1,-5]],[[3,4,2,6,-7,-7,7,6,-3,-1,-9,4,-4,-6,-2,3],[-7,-3,-7,4,9,-9,-7,2,-9,10,1,-5,-2,-3,-2,-10],[-1,7,2,-4,-3,7,-7,-9,-3,-4,3,-1,-10,9,-9,10],[2,10,1,4,6,-3,2,9,10,-10,-5,-10,-5,7,-10,8],[4,-5,-1,-8,-2,-1,-2,-10,6,-7,-10,3,6,1,-9,-5],[6,-10,10,-7,-7,-7,-1,-3,-4,5,5,-1,-10,-6,-3,1],[-2,-10,9,7,6,-6,8,3,8,-7,-5,-6,1,3,-5,-5],[7,1,1,-3,9,-5,9,-10,3,1,-8,-5,1,4,6,4],[3,1,-3,-2,-2,-1,2,-7,1,-6,-7,7,-3,-3,-10,-2]],[[2,6,8,8,-4,2,-2,-2,-8,-3,1,2,-3,-1,-2,4],[8,9,-8,7,-6,8,9,3,8,4,-8,-3,3,-3,-9,-9],[7,-7,5,-6,5,2,-4,3,3,-3,-4,-1,2,-4,-9,10],[-10,-2,2,-7,2,1,6,-9,-1,-7,1,-4,10,-4,10,8],[2,9,7,-9,7,4,5,-10,8,-5,-5,-1,-8,5,-8,10],[-2,4,-6,8,-4,-5,-8,7,-2,4,-3,4,10,9,-4,-8],[9,6,6,7,8,10,6,-1,-2,-8,10,4,5,9,-2,6],[8,7,9,3,7,-3,-3,-3,-1,-7,7,2,5,-1,-8,-10],[-2,2,2,-9,1,4,-6,8,-10,-10,-8,-8,4,2,6,-8]],[[-1,-10,-6,-4,8,-10,4,4,4,-2,-6,5,-10,2,3,4],[8,8,2,-2,7,7,-9,5,4,-8,-8,10,2,-3,2,8],[3,6,8,-8,-10,-6,7,-4,9,-3,5,-2,-5,-1,-4,9],[-6,5,-10,1,-7,1,-8,-4,5,3,-1,6,-2,5,7,-3],[6,9,10,-8,-6,-10,-3,3,-4,-9,-1,-2,-3,1,2,5],[4,6,5,-1,-4,-7,-9,-5,7,9,9,3,10,-2,-7,-10],[4,-5,1,-1,-8,10,-7,10,6,-1,1,-7,-7,-3,7,-7],[1,-9,7,7,-8,-3,-1,8,2,-4,-5,-6,-9,9,4,6],[-8,-6,-5,-10,-10,-8,8,8,-7,-7,-3,-7,1,8,-3,-1]],[[-9,4,9,-9,-9,-10,4,8,-2,6,-7,-8,2,-6,-8,4],[3,5,3,1,-2,-8,-10,-10,3,-8,2,1,-1,6,3,9],[9,-7,8,2,-8,-8,1,3,-7,-6,-6,-2,-3,8,-8,1],[-1,-8,6,-10,-4,-3,10,9,-6,6,-2,-10,-5,-3,5,2],[4,-4,-2,3,7,-3,3,-4,-8,2,7,9,10,8,-7,9],[10,10,-2,-10,-2,-5,6,1,-8,-6,-4,-10,6,-10,-6,-4],[6,10,10,6,4,4,-1,-4,9,7,-6,10,4,-6,-8,-9],[-8,-2,-9,-10,-2,-3,-1,-5,8,4,8,5,-3,-2,-3,5],[10,-10,10,1,4,6,-10,4,2,1,1,3,9,4,8,3]]], dtype = "int64")#candidate|6101|(7, 9, 16)|const|int64
bop_6102 = relay.add(const_6100.astype('int64'), relay.reshape(const_6101.astype('int64'), relay.shape_of(const_6100))) # shape=(7, 9, 16)
output = bop_6102
output2 = bop_6102
func_6127 = relay.Function([], output)
mod['func_6127'] = func_6127
mod = relay.transform.InferType()(mod)
output = func_6127()
func_6128 = relay.Function([], output)
mutated_mod['func_6128'] = func_6128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5244_call = mod.get_global_var('func_5244')
func_5246_call = mutated_mod.get_global_var('func_5246')
call_6144 = relay.TupleGetItem(func_5244_call(), 0)
call_6145 = relay.TupleGetItem(func_5246_call(), 0)
func_5093_call = mod.get_global_var('func_5093')
func_5095_call = mutated_mod.get_global_var('func_5095')
var_6160 = relay.var("var_6160", dtype = "float32", shape = (1040,))#candidate|6160|(1040,)|var|float32
call_6159 = relay.TupleGetItem(func_5093_call(relay.reshape(var_6160.astype('float32'), [1040,])), 10)
call_6161 = relay.TupleGetItem(func_5095_call(relay.reshape(var_6160.astype('float32'), [1040,])), 10)
output = relay.Tuple([call_6144,call_6159,var_6160,])
output2 = relay.Tuple([call_6145,call_6161,var_6160,])
func_6162 = relay.Function([var_6160,], output)
mod['func_6162'] = func_6162
mod = relay.transform.InferType()(mod)
var_6163 = relay.var("var_6163", dtype = "float32", shape = (1040,))#candidate|6163|(1040,)|var|float32
output = func_6162(var_6163)
func_6164 = relay.Function([var_6163], output)
mutated_mod['func_6164'] = func_6164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_6192 = func_1940_call()
call_6193 = func_1940_call()
func_4417_call = mod.get_global_var('func_4417')
func_4419_call = mutated_mod.get_global_var('func_4419')
call_6194 = func_4417_call()
call_6195 = func_4417_call()
output = relay.Tuple([call_6192,call_6194,])
output2 = relay.Tuple([call_6193,call_6195,])
func_6210 = relay.Function([], output)
mod['func_6210'] = func_6210
mod = relay.transform.InferType()(mod)
mutated_mod['func_6210'] = func_6210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6210_call = mutated_mod.get_global_var('func_6210')
call_6211 = func_6210_call()
output = call_6211
func_6212 = relay.Function([], output)
mutated_mod['func_6212'] = func_6212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_394_call = mutated_mod.get_global_var('func_394')
call_6241 = relay.TupleGetItem(func_393_call(), 1)
call_6242 = relay.TupleGetItem(func_394_call(), 1)
func_2161_call = mod.get_global_var('func_2161')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_6245 = func_2161_call()
call_6246 = func_2161_call()
output = relay.Tuple([call_6241,call_6245,])
output2 = relay.Tuple([call_6242,call_6246,])
func_6265 = relay.Function([], output)
mod['func_6265'] = func_6265
mod = relay.transform.InferType()(mod)
mutated_mod['func_6265'] = func_6265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6265_call = mutated_mod.get_global_var('func_6265')
call_6266 = func_6265_call()
output = call_6266
func_6267 = relay.Function([], output)
mutated_mod['func_6267'] = func_6267
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6294 = relay.var("var_6294", dtype = "float64", shape = (3, 1, 13))#candidate|6294|(3, 1, 13)|var|float64
const_6295 = relay.const([[[-2.407240,-8.959706,5.426084,-0.206280,3.972732,0.988305,-5.860527,-6.757509,-3.752771,-8.432835,0.854771,9.103430,9.871589]],[[-1.509754,-1.890508,-3.208368,8.780984,-8.303910,-5.244473,8.448039,-4.833844,-4.024812,-0.189586,-0.479719,9.902797,-8.129249]],[[3.263141,6.998792,1.451967,7.660345,1.943969,-5.454571,-2.950959,-0.053016,3.596699,-0.107186,-3.162987,-4.510868,1.856067]]], dtype = "float64")#candidate|6295|(3, 1, 13)|const|float64
bop_6296 = relay.maximum(var_6294.astype('float64'), relay.reshape(const_6295.astype('float64'), relay.shape_of(var_6294))) # shape=(3, 1, 13)
func_4709_call = mod.get_global_var('func_4709')
func_4711_call = mutated_mod.get_global_var('func_4711')
call_6311 = relay.TupleGetItem(func_4709_call(), 0)
call_6312 = relay.TupleGetItem(func_4711_call(), 0)
func_6091_call = mod.get_global_var('func_6091')
func_6096_call = mutated_mod.get_global_var('func_6096')
var_6315 = relay.var("var_6315", dtype = "float64", shape = (288,))#candidate|6315|(288,)|var|float64
const_6316 = relay.const([4.426869,-2.501161,3.564344,-7.851289,-5.569324,4.842904,9.265825,6.579363,1.722053,-4.485722,-2.737946,-0.912533,3.961826,5.518667,3.608965,3.116062,-0.451797,-8.354814,4.389136,-2.357388,3.533694,0.722894,0.064583,2.127023,3.533399,1.325043,-7.292496,0.610312,-8.829532,-6.276231,3.610254,-5.008346,0.045840,3.236129,3.310234,5.406701,8.686740,4.414670,3.032643,7.799730,-4.999981,-7.183750,-2.258032,2.678991,-7.545119,-3.705798,6.075447,1.498830,5.583002,0.693620,1.641319,-6.235493,1.346486,8.919043,-2.506601,-8.210818,-3.406383,4.170312,-9.600994,8.968846,-8.370085,2.418491,-0.302742,3.328061,4.698813,-2.161532,8.933320,-9.713242,-2.370538,9.181222,-1.411894,2.860955,-3.890687,-5.347033,5.671508,-4.610202,8.508392,-6.073632,-5.789999,-7.961853,-3.607946,-8.247007,5.463376,8.632476,4.846385,-2.181335,-6.269787,-5.980437,-5.114688,7.295719,-4.577816,5.027447,2.573787,3.458077,3.769898,-5.325223,-3.884750,1.794042,3.728898,3.501254,2.497953,-9.009149,5.444223,7.319395,5.920968,-1.121928,-3.699369,-5.452150,5.395729,5.374245,2.912211,-1.657600,7.824005,1.016552,-2.749012,7.985580,-3.691820,0.287466,-5.144424,2.008720,-9.561752,3.749392,3.618830,-5.084598,8.528856,-1.081101,7.401412,-8.281048,-7.221803,8.825645,-1.652705,9.135568,6.889056,-5.086422,0.724757,8.694555,5.761536,-9.934253,-1.011305,1.675425,-8.172756,-9.444289,6.380419,-5.592618,-9.110408,-7.777374,-2.501208,3.668893,0.419967,5.130696,4.836798,-9.012721,1.572059,-3.719072,1.961515,9.588054,3.236673,-5.331617,-4.371178,-2.944430,-6.897476,9.213413,-7.955933,-9.655909,5.368983,-3.189667,2.985884,1.446221,1.414088,-3.155039,-4.465683,8.074391,-6.855850,-7.277622,-8.914786,9.605723,5.343846,-5.663650,-7.763772,6.369598,-0.502018,-9.760981,-9.510028,8.510333,9.832035,9.422863,9.441452,5.948516,-2.826021,3.572863,5.654019,9.586216,5.721045,-7.467908,5.962687,3.331314,-9.710899,0.410584,-4.913959,-0.851990,-8.917592,7.810826,-4.598977,9.380833,-4.450783,-2.570649,-5.697578,-4.564261,1.798516,5.579827,3.459776,-2.594031,-0.274994,-8.120274,-4.412488,4.525438,-4.476490,6.032708,5.932071,9.166783,5.941439,4.747985,-9.089241,9.844076,5.041521,-3.543305,-2.602620,-5.124195,-0.875910,0.723788,6.256575,0.251997,1.658930,4.858811,-4.718620,-0.878041,-4.403173,4.340167,9.359454,-4.547321,8.183230,5.417160,3.874612,-5.697739,1.855988,9.568752,-2.570456,-6.269818,5.952428,7.322066,8.617627,7.324865,9.665042,-0.352725,5.070916,8.526144,0.084028,-1.635729,-0.627650,-4.065233,-4.577502,0.792504,-2.981753,-3.069419,8.058496,3.510796,1.928841,-1.871117,4.646550,-4.852765,5.942558,6.209836,-4.293342,9.924630,0.273755,-2.639238,1.369056,-0.397792,-7.159879,8.354996,-6.340523,-8.812856,5.936077,5.649528,0.509426,-7.756151,5.661795,7.470017,8.166596,9.934143,-5.507052,9.486217,2.286023,4.788105,-2.355866,8.723296,-7.738124,3.779948,-3.666619,-7.339119,-0.627639,-3.505685,7.022519,0.540114,-3.322772,2.011430,6.979444,5.608452,-3.985355,-9.955687,6.396603,-7.004339,9.610750,-9.329311,-5.338142,9.864652,7.067230,-2.015867,1.176459,0.271279,-5.449772,-2.423016,7.947380,-6.779765,-3.174304,0.518789,-2.564232,7.343685,6.752972,2.249349,6.151437,-2.037643,-3.037821,4.510588,-1.929292,-5.636467,9.290818,-8.758444,-3.810287,-4.109214,6.083758,-9.416229,4.006312,6.970440,5.554235,-2.868736,5.564564,1.932541,-7.453285,4.771794,-2.663895,1.704872,-6.592373,-7.802980,1.977082,-1.766027,-6.546911,-1.259007,-0.624009,-8.797703,9.001921,-5.778777,3.910928,-3.941797,-7.848871,7.327070,7.198494,-4.727688,-6.163486,-6.896620,-3.511860,9.770371,-6.205314,-5.610562,5.267224,-9.893900,-3.412936,-3.880249,9.018546,5.616400,-7.796557,-8.887788,2.887320,-9.130422,4.771448,8.458291,1.076238,1.797751,9.258805,-6.438114,-6.889242,9.733273,-6.618393,8.793059,-9.366641,8.503411,7.658708,5.621099,2.581906,-9.956453,-6.548554,-8.541123,-5.719958,9.988844,4.097168,8.996541,7.113669,-9.893469,-4.617872,3.235249,-9.681425,1.458801,-1.634764,6.516589,-7.892040,-3.128905,8.162924,-2.259668,-8.026876,5.197088,-0.695868,-9.389634,3.620081,4.731477,-1.502504,5.533960,3.428194,-8.086770,6.252455,5.381026,2.203185,-9.346571,-0.551562,7.046188,1.438800,1.054382,0.305153,5.877771,-6.261278,-1.165564,0.302325,-1.871832,-4.920507,-1.133955,-4.887702,-3.521997,6.851433,-3.694859,3.398808,1.193846,6.884005,-6.551459,-8.578285,6.212818,-6.673652,9.670282,9.127622,1.390599,-4.943590,3.359379,0.695351,-2.076891,9.835010,8.869421,-2.353827,1.061175,5.410734,-6.228908,4.711962,-7.663413,9.462325,1.346371,4.233675,6.585082,-3.604176,-6.761834,-6.073777,-7.673143,-3.885690,-7.353738,-8.578603,-6.858239,-1.612084,1.573581,-6.153747,2.163820,1.411544,8.832623,7.225623,-1.432185,5.458492,-0.172389,-2.802451,3.334655,-1.314093,0.477466,9.950245,-8.808243,3.908637,9.936096,4.596768,1.740434,7.015058,-9.362900,8.519630,-5.911535,9.674400,-1.286307,-1.639161,-0.021047,-2.431264,7.514403,8.892492,2.826039,-2.026960,4.618941,6.202845,-4.161046,6.179227,-2.375696,-2.751086,8.487802,5.311939,9.434596,-9.523217,-8.757671,9.288406,-0.903255,7.750404,9.281632,3.047235,8.906723,-7.194025,4.279888,-8.507193,-2.145026,6.926131,5.502650,-5.661954,-2.185510,-4.856163,2.526333,-1.615029,1.046908,6.155325,5.617250,3.784871,1.473905,2.732181,4.503835,-2.100663,-3.721286,4.741317,-0.664106,-9.555750,-9.468637,5.261614,-4.333734,-4.701250,4.434082,1.868198,-8.559701,-7.916921,-5.053407,-7.576280,6.380804,0.843374,-2.522601,3.950485,-3.609039,3.701520,5.834480,-2.156430,8.592325,0.234796,-2.254813,4.697328,6.890386,3.843501,1.141796,0.299197,-0.771933,-8.878883,6.782525,-6.174287,5.296964,3.158341,-9.006913,3.459049,-0.485929,2.791364,9.298794,6.381650,-2.342173,-5.372188,-5.954099,-8.807086,-2.129420,-7.587786,8.093344,-7.651527,-6.644441,6.463861,9.691166,-0.952374,2.527935,5.141850,5.191224,7.967864,1.166671,9.902644,0.014230,-6.511006,9.113626,3.446990,8.852689,6.375854,8.011867,1.343115,0.032914,-3.731635,1.724360,1.534177,-7.131233,-1.876667,-7.272342,-9.401689,1.658026,-8.006186,9.866735,1.979634,0.067565,-5.803116,3.207322,0.773341,-4.405101,8.846445,4.625484,-3.081413,6.439351,8.831589,-2.888146,2.416524,9.658437,-8.986183,-0.540625,6.624693,9.496657,-5.430730,9.104891,2.761601,-6.152536,5.956751,-6.984801,5.287765,-7.105655,0.420808,-0.491396,5.499525,-9.596374,-0.899658,3.740686,-3.994853,-5.606751,-5.841641,9.623333,5.390268,-1.980086,8.569493,-7.495973,5.091361,-7.842217,8.607124,7.124176,-7.569954,2.605620,-6.419255,-0.542790,2.568347,-0.288595,9.582728,3.304436,5.769302,8.758669,-0.968002,2.780960,2.405650,8.243751,1.982869,8.934176,-0.250886,-6.106285,9.272126,-6.707252,3.113457,-7.519938,-7.613151,3.859068,-8.198097,-9.570056,-5.075525,-9.349172,1.030459,7.930496,-4.867130,-6.381778,0.875655,-2.655709,-1.257858,3.113198,6.303078,-7.848512,6.609008,0.126594,-1.861729,6.184130,5.302893,-5.681019,8.941630,5.037569], dtype = "float64")#candidate|6316|(720,)|const|float64
call_6314 = relay.TupleGetItem(func_6091_call(relay.reshape(var_6315.astype('float64'), [16, 3, 6]), relay.reshape(var_6315.astype('int8'), [16, 3, 6]), relay.reshape(const_6316.astype('float64'), [16, 3, 15]), ), 2)
call_6317 = relay.TupleGetItem(func_6096_call(relay.reshape(var_6315.astype('float64'), [16, 3, 6]), relay.reshape(var_6315.astype('int8'), [16, 3, 6]), relay.reshape(const_6316.astype('float64'), [16, 3, 15]), ), 2)
output = relay.Tuple([bop_6296,call_6311,call_6314,var_6315,const_6316,])
output2 = relay.Tuple([bop_6296,call_6312,call_6317,var_6315,const_6316,])
func_6337 = relay.Function([var_6294,var_6315,], output)
mod['func_6337'] = func_6337
mod = relay.transform.InferType()(mod)
mutated_mod['func_6337'] = func_6337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6337_call = mutated_mod.get_global_var('func_6337')
var_6339 = relay.var("var_6339", dtype = "float64", shape = (3, 1, 13))#candidate|6339|(3, 1, 13)|var|float64
var_6340 = relay.var("var_6340", dtype = "float64", shape = (288,))#candidate|6340|(288,)|var|float64
call_6338 = func_6337_call(var_6339,var_6340,)
output = call_6338
func_6341 = relay.Function([var_6339,var_6340,], output)
mutated_mod['func_6341'] = func_6341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2218_call = mod.get_global_var('func_2218')
func_2220_call = mutated_mod.get_global_var('func_2220')
call_6348 = relay.TupleGetItem(func_2218_call(), 0)
call_6349 = relay.TupleGetItem(func_2220_call(), 0)
output = call_6348
output2 = call_6349
func_6377 = relay.Function([], output)
mod['func_6377'] = func_6377
mod = relay.transform.InferType()(mod)
mutated_mod['func_6377'] = func_6377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6377_call = mutated_mod.get_global_var('func_6377')
call_6378 = func_6377_call()
output = call_6378
func_6379 = relay.Function([], output)
mutated_mod['func_6379'] = func_6379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1404_call = mod.get_global_var('func_1404')
func_1406_call = mutated_mod.get_global_var('func_1406')
call_6380 = func_1404_call()
call_6381 = func_1404_call()
func_4523_call = mod.get_global_var('func_4523')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_6386 = relay.TupleGetItem(func_4523_call(), 0)
call_6387 = relay.TupleGetItem(func_4524_call(), 0)
output = relay.Tuple([call_6380,call_6386,])
output2 = relay.Tuple([call_6381,call_6387,])
func_6388 = relay.Function([], output)
mod['func_6388'] = func_6388
mod = relay.transform.InferType()(mod)
output = func_6388()
func_6389 = relay.Function([], output)
mutated_mod['func_6389'] = func_6389
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6390 = relay.const([[[-7.995182],[6.538849],[-6.080230],[8.646813],[-4.946616],[4.956476],[1.117648],[-4.932661],[0.891734],[6.421789],[0.276239],[-8.494765],[-1.551459]],[[-0.424288],[2.526616],[4.236021],[-3.079768],[-7.937581],[-7.692019],[-3.123987],[-4.205223],[6.530841],[-3.656165],[2.761512],[-4.121403],[-6.851415]],[[4.527246],[4.087046],[-7.125121],[5.693725],[3.549882],[3.119732],[2.856470],[-5.263186],[-3.147584],[-9.100264],[9.672978],[-8.753132],[-8.410209]],[[5.902496],[-5.952996],[-7.074389],[-1.170756],[-9.911331],[4.630329],[-8.737125],[-7.690137],[6.142627],[-6.836740],[-0.604635],[-1.891476],[2.698710]],[[-4.358600],[8.619132],[-0.141207],[8.434989],[-1.519447],[-1.930149],[7.859232],[-3.891204],[-5.632795],[0.370463],[-1.188965],[-1.837428],[-9.148064]],[[7.886624],[-2.881438],[-8.550251],[1.304225],[0.622755],[6.919302],[-0.857727],[-9.481113],[-3.059070],[1.235178],[5.801881],[-5.969081],[7.423793]],[[1.050420],[7.086073],[-2.624893],[-1.198909],[2.794907],[4.825828],[9.432171],[-7.373137],[8.984773],[-0.030901],[7.909062],[3.964671],[6.191562]],[[-8.839944],[2.570426],[3.920908],[-1.316217],[-0.061064],[7.963001],[2.318762],[-1.635312],[7.693620],[4.305092],[-6.753834],[8.572823],[-6.348548]],[[0.596395],[0.632720],[-2.821655],[-0.165276],[8.739136],[-7.988417],[-2.422957],[-6.302516],[-4.912633],[4.441708],[-3.574113],[-5.586460],[-1.735036]],[[-9.097938],[4.647142],[0.206261],[-5.017898],[-5.579021],[-2.520807],[-8.929530],[-2.269421],[2.706970],[-2.346798],[-3.847738],[2.432893],[8.750705]],[[2.137386],[6.694080],[-0.607693],[1.884212],[4.787127],[-1.494704],[9.326896],[-3.439995],[-8.896435],[-9.302105],[-6.941681],[6.429421],[0.098872]],[[1.850501],[0.676142],[3.904466],[-8.561236],[1.306369],[-3.465849],[-5.431854],[7.402491],[-4.082897],[9.198959],[-9.271628],[7.504312],[-3.755400]]], dtype = "float64")#candidate|6390|(12, 13, 1)|const|float64
var_6391 = relay.var("var_6391", dtype = "float64", shape = (12, 13, 9))#candidate|6391|(12, 13, 9)|var|float64
bop_6392 = relay.mod(const_6390.astype('float64'), var_6391.astype('float64')) # shape=(12, 13, 9)
func_2776_call = mod.get_global_var('func_2776')
func_2777_call = mutated_mod.get_global_var('func_2777')
call_6401 = relay.TupleGetItem(func_2776_call(), 1)
call_6402 = relay.TupleGetItem(func_2777_call(), 1)
output = relay.Tuple([bop_6392,call_6401,])
output2 = relay.Tuple([bop_6392,call_6402,])
func_6403 = relay.Function([var_6391,], output)
mod['func_6403'] = func_6403
mod = relay.transform.InferType()(mod)
var_6404 = relay.var("var_6404", dtype = "float64", shape = (12, 13, 9))#candidate|6404|(12, 13, 9)|var|float64
output = func_6403(var_6404)
func_6405 = relay.Function([var_6404], output)
mutated_mod['func_6405'] = func_6405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2124_call = mod.get_global_var('func_2124')
func_2126_call = mutated_mod.get_global_var('func_2126')
call_6413 = func_2124_call()
call_6414 = func_2124_call()
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_6416 = relay.TupleGetItem(func_296_call(), 0)
call_6417 = relay.TupleGetItem(func_297_call(), 0)
func_3814_call = mod.get_global_var('func_3814')
func_3815_call = mutated_mod.get_global_var('func_3815')
call_6421 = relay.TupleGetItem(func_3814_call(), 1)
call_6422 = relay.TupleGetItem(func_3815_call(), 1)
uop_6423 = relay.erf(call_6416.astype('float64')) # shape=(1, 3, 1)
uop_6425 = relay.erf(call_6417.astype('float64')) # shape=(1, 3, 1)
output = relay.Tuple([call_6413,call_6421,uop_6423,])
output2 = relay.Tuple([call_6414,call_6422,uop_6425,])
func_6426 = relay.Function([], output)
mod['func_6426'] = func_6426
mod = relay.transform.InferType()(mod)
output = func_6426()
func_6427 = relay.Function([], output)
mutated_mod['func_6427'] = func_6427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mod.get_global_var('func_1483')
func_1485_call = mutated_mod.get_global_var('func_1485')
call_6456 = relay.TupleGetItem(func_1483_call(), 3)
call_6457 = relay.TupleGetItem(func_1485_call(), 3)
output = call_6456
output2 = call_6457
func_6464 = relay.Function([], output)
mod['func_6464'] = func_6464
mod = relay.transform.InferType()(mod)
mutated_mod['func_6464'] = func_6464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6464_call = mutated_mod.get_global_var('func_6464')
call_6465 = func_6464_call()
output = call_6465
func_6466 = relay.Function([], output)
mutated_mod['func_6466'] = func_6466
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6504 = relay.var("var_6504", dtype = "float64", shape = (5, 9, 1))#candidate|6504|(5, 9, 1)|var|float64
uop_6505 = relay.log(var_6504.astype('float64')) # shape=(5, 9, 1)
func_4502_call = mod.get_global_var('func_4502')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_6510 = relay.TupleGetItem(func_4502_call(), 1)
call_6511 = relay.TupleGetItem(func_4503_call(), 1)
func_3053_call = mod.get_global_var('func_3053')
func_3055_call = mutated_mod.get_global_var('func_3055')
call_6528 = func_3053_call()
call_6529 = func_3053_call()
output = relay.Tuple([uop_6505,call_6510,call_6528,])
output2 = relay.Tuple([uop_6505,call_6511,call_6529,])
func_6552 = relay.Function([var_6504,], output)
mod['func_6552'] = func_6552
mod = relay.transform.InferType()(mod)
mutated_mod['func_6552'] = func_6552
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6553 = relay.var("var_6553", dtype = "float64", shape = (5, 9, 1))#candidate|6553|(5, 9, 1)|var|float64
func_6552_call = mutated_mod.get_global_var('func_6552')
call_6554 = func_6552_call(var_6553)
output = call_6554
func_6555 = relay.Function([var_6553], output)
mutated_mod['func_6555'] = func_6555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3384_call = mod.get_global_var('func_3384')
func_3386_call = mutated_mod.get_global_var('func_3386')
call_6594 = relay.TupleGetItem(func_3384_call(), 1)
call_6595 = relay.TupleGetItem(func_3386_call(), 1)
output = call_6594
output2 = call_6595
func_6616 = relay.Function([], output)
mod['func_6616'] = func_6616
mod = relay.transform.InferType()(mod)
mutated_mod['func_6616'] = func_6616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6616_call = mutated_mod.get_global_var('func_6616')
call_6617 = func_6616_call()
output = call_6617
func_6618 = relay.Function([], output)
mutated_mod['func_6618'] = func_6618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_6669 = relay.TupleGetItem(func_2359_call(), 0)
call_6670 = relay.TupleGetItem(func_2360_call(), 0)
var_6679 = relay.var("var_6679", dtype = "float32", shape = (6, 3, 8))#candidate|6679|(6, 3, 8)|var|float32
bop_6680 = relay.power(call_6669.astype('float64'), var_6679.astype('float64')) # shape=(6, 3, 8)
bop_6683 = relay.power(call_6670.astype('float64'), var_6679.astype('float64')) # shape=(6, 3, 8)
output = relay.Tuple([bop_6680,])
output2 = relay.Tuple([bop_6683,])
func_6684 = relay.Function([var_6679,], output)
mod['func_6684'] = func_6684
mod = relay.transform.InferType()(mod)
var_6685 = relay.var("var_6685", dtype = "float32", shape = (6, 3, 8))#candidate|6685|(6, 3, 8)|var|float32
output = func_6684(var_6685)
func_6686 = relay.Function([var_6685], output)
mutated_mod['func_6686'] = func_6686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4918_call = mod.get_global_var('func_4918')
func_4919_call = mutated_mod.get_global_var('func_4919')
call_6714 = relay.TupleGetItem(func_4918_call(), 0)
call_6715 = relay.TupleGetItem(func_4919_call(), 0)
output = call_6714
output2 = call_6715
func_6719 = relay.Function([], output)
mod['func_6719'] = func_6719
mod = relay.transform.InferType()(mod)
mutated_mod['func_6719'] = func_6719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6719_call = mutated_mod.get_global_var('func_6719')
call_6720 = func_6719_call()
output = call_6720
func_6721 = relay.Function([], output)
mutated_mod['func_6721'] = func_6721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3570_call = mod.get_global_var('func_3570')
func_3572_call = mutated_mod.get_global_var('func_3572')
call_6722 = func_3570_call()
call_6723 = func_3570_call()
func_5631_call = mod.get_global_var('func_5631')
func_5633_call = mutated_mod.get_global_var('func_5633')
call_6724 = func_5631_call()
call_6725 = func_5631_call()
func_1061_call = mod.get_global_var('func_1061')
func_1062_call = mutated_mod.get_global_var('func_1062')
call_6733 = relay.TupleGetItem(func_1061_call(), 1)
call_6734 = relay.TupleGetItem(func_1062_call(), 1)
func_6377_call = mod.get_global_var('func_6377')
func_6379_call = mutated_mod.get_global_var('func_6379')
call_6738 = func_6377_call()
call_6739 = func_6377_call()
func_4523_call = mod.get_global_var('func_4523')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_6755 = relay.TupleGetItem(func_4523_call(), 0)
call_6756 = relay.TupleGetItem(func_4524_call(), 0)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_6762 = relay.TupleGetItem(func_2813_call(), 0)
call_6763 = relay.TupleGetItem(func_2814_call(), 0)
output = relay.Tuple([call_6722,call_6724,call_6733,call_6738,call_6755,call_6762,])
output2 = relay.Tuple([call_6723,call_6725,call_6734,call_6739,call_6756,call_6763,])
func_6765 = relay.Function([], output)
mod['func_6765'] = func_6765
mod = relay.transform.InferType()(mod)
output = func_6765()
func_6766 = relay.Function([], output)
mutated_mod['func_6766'] = func_6766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3570_call = mod.get_global_var('func_3570')
func_3572_call = mutated_mod.get_global_var('func_3572')
call_6809 = func_3570_call()
call_6810 = func_3570_call()
var_6820 = relay.var("var_6820", dtype = "float32", shape = (15, 3, 3))#candidate|6820|(15, 3, 3)|var|float32
bop_6821 = relay.not_equal(call_6809.astype('bool'), var_6820.astype('bool')) # shape=(15, 3, 3)
bop_6824 = relay.not_equal(call_6810.astype('bool'), var_6820.astype('bool')) # shape=(15, 3, 3)
bop_6832 = relay.greater_equal(bop_6821.astype('bool'), call_6809.astype('bool')) # shape=(15, 3, 3)
bop_6835 = relay.greater_equal(bop_6824.astype('bool'), call_6810.astype('bool')) # shape=(15, 3, 3)
output = bop_6832
output2 = bop_6835
func_6841 = relay.Function([var_6820,], output)
mod['func_6841'] = func_6841
mod = relay.transform.InferType()(mod)
var_6842 = relay.var("var_6842", dtype = "float32", shape = (15, 3, 3))#candidate|6842|(15, 3, 3)|var|float32
output = func_6841(var_6842)
func_6843 = relay.Function([var_6842], output)
mutated_mod['func_6843'] = func_6843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_840_call = mod.get_global_var('func_840')
func_842_call = mutated_mod.get_global_var('func_842')
call_6902 = relay.TupleGetItem(func_840_call(), 0)
call_6903 = relay.TupleGetItem(func_842_call(), 0)
output = call_6902
output2 = call_6903
func_6907 = relay.Function([], output)
mod['func_6907'] = func_6907
mod = relay.transform.InferType()(mod)
output = func_6907()
func_6908 = relay.Function([], output)
mutated_mod['func_6908'] = func_6908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_604_call = mod.get_global_var('func_604')
func_605_call = mutated_mod.get_global_var('func_605')
call_6998 = relay.TupleGetItem(func_604_call(), 0)
call_6999 = relay.TupleGetItem(func_605_call(), 0)
func_4635_call = mod.get_global_var('func_4635')
func_4639_call = mutated_mod.get_global_var('func_4639')
var_7007 = relay.var("var_7007", dtype = "float64", shape = (42,))#candidate|7007|(42,)|var|float64
var_7008 = relay.var("var_7008", dtype = "float64", shape = (1350,))#candidate|7008|(1350,)|var|float64
call_7006 = relay.TupleGetItem(func_4635_call(relay.reshape(var_7007.astype('float64'), [2, 3, 7]), relay.reshape(var_7008.astype('float64'), [1350,]), ), 5)
call_7009 = relay.TupleGetItem(func_4639_call(relay.reshape(var_7007.astype('float64'), [2, 3, 7]), relay.reshape(var_7008.astype('float64'), [1350,]), ), 5)
output = relay.Tuple([call_6998,call_7006,var_7007,var_7008,])
output2 = relay.Tuple([call_6999,call_7009,var_7007,var_7008,])
func_7011 = relay.Function([var_7007,var_7008,], output)
mod['func_7011'] = func_7011
mod = relay.transform.InferType()(mod)
mutated_mod['func_7011'] = func_7011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7011_call = mutated_mod.get_global_var('func_7011')
var_7013 = relay.var("var_7013", dtype = "float64", shape = (42,))#candidate|7013|(42,)|var|float64
var_7014 = relay.var("var_7014", dtype = "float64", shape = (1350,))#candidate|7014|(1350,)|var|float64
call_7012 = func_7011_call(var_7013,var_7014,)
output = call_7012
func_7015 = relay.Function([var_7013,var_7014,], output)
mutated_mod['func_7015'] = func_7015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1014_call = mod.get_global_var('func_1014')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_7053 = func_1014_call()
call_7054 = func_1014_call()
func_4478_call = mod.get_global_var('func_4478')
func_4480_call = mutated_mod.get_global_var('func_4480')
var_7082 = relay.var("var_7082", dtype = "int64", shape = (1296,))#candidate|7082|(1296,)|var|int64
call_7081 = relay.TupleGetItem(func_4478_call(relay.reshape(var_7082.astype('int64'), [9, 12, 12])), 0)
call_7083 = relay.TupleGetItem(func_4480_call(relay.reshape(var_7082.astype('int64'), [9, 12, 12])), 0)
func_2054_call = mod.get_global_var('func_2054')
func_2056_call = mutated_mod.get_global_var('func_2056')
const_7092 = relay.const([-0.286145,-3.390237,-5.831198,-0.597369,-8.196539,2.691042,-4.409637,-1.143640,2.933836,-8.417854,7.385804,0.350892,-7.691321,-9.053925,0.475506,6.305960,-2.879791,3.401052], dtype = "float32")#candidate|7092|(18,)|const|float32
call_7091 = relay.TupleGetItem(func_2054_call(relay.reshape(const_7092.astype('float32'), [3, 3, 2])), 2)
call_7093 = relay.TupleGetItem(func_2056_call(relay.reshape(const_7092.astype('float32'), [3, 3, 2])), 2)
func_6403_call = mod.get_global_var('func_6403')
func_6405_call = mutated_mod.get_global_var('func_6405')
const_7100 = relay.const([[-5.897462],[-7.210921],[7.650792],[1.425210],[0.452506],[-0.691603],[8.670957],[2.740580],[5.764706],[2.998552],[9.832656],[-8.805244],[-1.931632],[4.753029],[-5.693401],[7.271403],[3.761751],[5.101752],[9.883548],[0.265620],[0.827397],[4.835000],[8.557751],[4.075474],[9.584092],[4.260134],[2.992651],[9.716669],[-8.686251],[-8.879170],[5.358520],[9.559403],[1.457764],[3.826376],[7.875097],[3.067833],[-5.294330],[2.850590],[5.502671],[-4.563551],[2.607856],[-6.779622],[-7.836064],[0.612104],[-0.016961],[0.860975],[3.763780],[-6.433610],[-4.367031],[-7.144397],[-8.471862],[-2.210547],[-8.355068],[-1.992233],[-5.117385],[-7.787078],[-5.178907],[-9.857619],[8.262818],[3.495994],[9.327338],[3.514387],[3.437127],[4.699178],[7.159199],[-3.590504],[-4.421326],[-6.342670],[-1.105697],[-3.045273],[9.714745],[4.086490],[8.062697],[-6.517933],[0.478109],[-7.635796],[1.457872],[6.328458],[3.503295],[-3.874502],[-9.787378],[-6.747493],[6.496958],[-9.195818],[1.752721],[3.854633],[2.085644],[4.779436],[-4.891255],[6.203634],[3.901581],[4.346143],[1.578131],[-7.526865],[4.024655],[3.454158],[8.214335],[-4.892375],[-4.773512],[-6.656928],[-0.324035],[6.148482],[-5.091400],[-4.039286],[-6.332814],[-5.047251],[-8.387280],[-4.312428],[7.015092],[-5.969485],[6.848251],[-7.292713],[-3.896797],[-8.768769],[3.644889],[-6.022492],[-0.107032],[-5.654968],[-5.740515],[2.432125],[-5.178612],[4.090595],[0.235510],[4.597769],[-4.497973],[-9.713180],[4.400958],[-3.113720],[9.141252],[4.606239],[9.372513],[-8.598736],[4.152981],[0.220569],[-8.525190],[-3.366870],[-4.748183],[4.432255],[-7.189742],[-1.220760],[-6.759701],[-5.478635],[-1.902401],[5.076691],[8.730271],[-6.653476],[3.523660],[-5.663238],[8.813414],[-3.866616],[3.654684],[3.626721],[-9.899979],[0.072303],[4.541153],[3.195950],[-4.533793],[5.228482],[-3.005703],[8.393401],[6.075754],[1.183217],[-3.009750],[8.014608],[6.578248],[5.843278],[0.774541],[-5.156598],[7.859376],[-1.089189],[-3.121326],[8.188569],[5.657463],[3.996971],[9.511186],[-3.108697],[-3.060508],[9.132206],[5.553068],[4.822792],[1.529831],[2.861745],[0.214361],[-6.163018],[-5.495375],[0.697788],[1.398017],[8.718568],[3.936534],[-4.185021],[5.895176],[-3.708017],[-8.486750],[7.801500],[-1.355474],[-4.071429],[4.742826],[-0.837911],[-5.615087],[-2.604382],[5.010339],[4.523734],[-1.040691],[-2.097619],[5.324659],[-5.809096],[7.762999],[-8.898741],[6.700636],[3.503582],[-4.805321],[6.038456],[-6.913081],[-8.033711],[-2.059833],[8.537403],[-5.704915],[-1.857461],[2.445077],[3.886400],[-3.945765],[-5.606101],[-9.160502],[8.906859],[-7.841481],[5.884219],[7.193579],[-8.675834],[9.407896],[-5.456413],[1.068543],[7.332197],[-3.505869],[-8.979561],[-6.987067],[-0.662857],[-5.733067],[-9.255495],[7.089143],[-0.032338],[5.058465],[9.962377],[-6.357130],[-5.873582],[-1.681291],[9.154371],[-0.041684],[-8.162316],[3.758662],[-1.142505],[-5.720845],[-0.935909],[3.915570],[0.198139],[-8.705895],[-3.205027],[6.605663],[-2.434595],[-3.748389],[5.512261],[2.331991],[-0.178517],[-6.391481],[-9.822853],[-1.957542],[0.805382],[5.990975],[7.515326],[8.114789],[-2.382042],[-4.030169],[6.978930],[-0.617741],[0.873182],[-5.212324],[5.627408],[4.759255],[7.899184],[-0.615026],[7.228158],[-3.924997],[6.447945],[-0.855960],[8.547372],[4.275805],[-6.644176],[-7.552205],[-3.043871],[1.006449],[2.115161],[-7.883470],[-6.296259],[9.417495],[8.665139],[7.415948],[-6.748089],[-2.162090],[-8.050737],[-8.379156],[-1.586577],[9.180500],[0.007615],[-0.346046],[-2.980400],[8.245212],[6.712860],[-0.311560],[4.981068],[3.834974],[-3.756152],[-7.225826],[-6.415919],[-5.349452],[6.726979],[-4.455677],[4.876764],[-4.806121],[-2.689549],[-5.169109],[7.156526],[-0.043249],[2.445835],[-2.036596],[-8.781078],[-5.187571],[-0.041685],[1.327846],[0.927233],[9.072014],[-8.308877],[-6.995037],[2.843292],[-0.123428],[4.375641],[-5.610328],[-6.228344],[4.397355],[-7.444295],[8.866162],[4.987728],[0.900799],[-7.867337],[-8.543642],[-0.215031],[-0.132555],[-6.597348],[-6.764089],[-9.834851],[8.279551],[0.394346],[-0.394585],[-3.370648],[-8.415567],[7.835639],[-9.739886],[1.411878],[-3.908613],[-0.027608],[9.328681],[9.553668],[-1.437390],[-6.154234],[6.514186],[1.867956],[-9.357656],[6.015900],[7.344037],[-4.162535],[-8.741594],[1.517286],[-3.164583],[-2.306197],[-2.211443],[9.303832],[5.748286],[6.702231],[-3.082043],[9.087993],[-0.740467],[-3.328911],[3.972474],[3.953836],[-3.146409],[-2.129359],[8.202763],[7.989759],[-3.579124],[5.569179],[-4.614277],[-4.503635],[9.946940],[9.002976],[4.573988],[7.802163],[-4.375286],[-1.571722],[3.992857],[-4.817819],[2.144965],[-2.900691],[-0.366533],[-1.468602],[6.262579],[0.986360],[2.854764],[-1.559658],[1.684856],[-1.780889],[-8.502815],[3.455582],[-8.269504],[-6.000938],[2.960713],[8.895357],[-1.467071],[-0.335820],[7.647604],[4.826369],[-2.742652],[-3.935358],[6.547125],[-0.594152],[2.541462],[4.047006],[-5.617214],[-4.048070],[5.841217],[5.229934],[9.703479],[1.849859],[-6.818718],[-4.242298],[5.507719],[8.101673],[-6.844514],[3.100491],[-9.803090],[-4.624322],[-9.795484],[2.828599],[-4.348088],[0.248189],[-6.783616],[0.158274],[6.052774],[7.784093],[-5.701445],[1.658933],[-1.408846],[9.563882],[5.465902],[-0.858887],[-4.951564],[5.265278],[-2.358782],[8.924282],[-5.874504],[-5.947248],[0.909466],[-3.532206],[4.156392],[6.899462],[2.124731],[4.577358],[1.050931],[-9.188003],[4.771834],[-2.600277],[2.255203],[-3.025124],[-7.625908],[3.792536],[7.013691],[7.281013],[1.852786],[6.693412],[-5.004412],[-8.275478],[-4.906114],[1.764695],[-7.637079],[-0.365203],[-5.615621],[6.869823],[-2.300118],[6.274016],[9.054695],[1.288182],[3.902833],[-0.881552],[-6.342688],[4.387309],[-4.222747],[-0.218559],[4.920585],[-8.578652],[1.385574],[8.048332],[6.141420],[0.409735],[-1.468842],[-2.057770],[6.582580],[-5.886129],[-1.572530],[2.767754],[8.365810],[2.708657],[-8.811168],[-7.457346],[0.542039],[6.130648],[0.156715],[-8.940030],[5.144079],[-0.624525],[7.644118],[-6.844886],[-2.794188],[6.176005],[5.667014],[5.617627],[6.827274],[-9.119994],[-3.502734],[1.118931],[0.148169],[-5.030956],[4.690844],[5.168669],[-8.403519],[-5.892533],[-2.588702],[2.936305],[-6.951961],[9.243876],[5.898371],[-6.318101],[-2.485316],[7.273549],[4.086280],[-4.118530],[4.578537],[5.608752],[-2.549701],[-6.679980],[-7.591984],[-3.770015],[5.150213],[4.482257],[-2.510805],[9.415175],[8.260868],[-8.421765],[-6.796371],[-3.108622],[-3.417789],[-1.512687],[7.492555],[-0.566171],[-5.734661],[-4.836593],[8.633803],[2.040339],[-1.541899],[-0.922708],[1.446116],[9.209609],[1.283023],[-4.251043],[4.984911],[4.671137],[-4.436061],[3.193277],[9.170961],[4.541320],[-0.849184],[-3.915834],[-3.046139],[-4.894181],[-4.276069],[0.047189],[-5.494982],[-9.189179],[-8.050269],[6.067632],[2.596633],[0.580286],[-4.717350],[4.704183],[-8.115367],[3.228272],[2.445742],[-5.078915],[1.847384],[-4.534574],[-2.272886],[-1.948519],[-1.947776],[-4.157859],[7.089028],[-0.915737],[5.242081],[-6.875701],[3.530333],[0.361863],[-7.155372],[-0.180255],[3.879566],[6.852614],[-5.358318],[-0.662234],[7.976248],[4.654472],[-7.688290],[-5.586452],[-2.752515],[-9.447951],[-7.710547],[0.371902],[5.763756],[2.524993],[-9.782532],[2.666767],[3.053770],[-4.206227],[-1.584255],[-5.101501],[5.905064],[-0.500033],[1.788429],[-6.489569],[9.823116],[3.461873],[0.085944],[7.856816],[-7.684444],[2.804978],[7.917039],[-4.437549],[1.251824],[-3.766517],[1.044013],[-0.734475],[-9.700424],[-4.396338],[1.999832],[2.311291],[-3.762582],[7.830619],[-6.041373],[-7.273135],[5.712592],[6.932842],[-6.375497],[1.210953],[-9.697727],[7.201780],[-4.193309],[3.248469],[-0.126562],[4.861962],[-5.813757],[3.414169],[1.066234],[-4.461133],[9.262018],[-3.277554],[-1.996376],[0.380360],[2.882153],[6.523769],[-2.117407],[-3.919076],[-4.533643],[-8.491013],[1.806205],[-7.972721],[-1.416051],[-4.414817],[-9.150448],[9.009635],[8.622726],[8.937581],[7.207153],[-9.156363],[2.297239],[7.154571],[4.643309],[8.223227],[2.739802],[-6.808560],[0.442105],[-8.650390],[-0.630086],[6.422423],[3.865737],[7.010340],[8.182118],[3.693061],[4.367368],[7.885422],[6.795130],[2.876230],[-3.789700],[-3.636086],[-7.984204],[9.395951],[3.146321],[2.455103],[-3.256727],[1.954957],[-2.801416],[8.671121],[6.414467],[-9.344979],[-8.901256],[4.668977],[-7.109241],[-7.949387],[6.947704],[-9.014042],[-5.746359],[8.031107],[8.680891],[1.784703],[-1.526577],[-1.803664],[7.942562],[-3.388711],[-0.539140],[-1.341314],[-9.147166],[-0.129596],[-6.526028],[-8.772970],[7.557494],[3.826152],[-8.953922],[0.112287],[9.489177],[5.249397],[1.725659],[-4.236224],[1.637138],[4.975114],[-5.059661],[5.150380],[-0.844642],[7.738081],[-1.470115],[-0.540081],[1.475773],[4.610124],[6.241295],[3.279592],[-4.169601],[-0.833020],[-3.457446],[-1.508005],[3.833644],[7.172095],[8.114781],[-3.959255],[-8.321060],[-0.375502],[1.836520],[-8.126232],[-3.217109],[-3.305407],[3.810052],[6.677909],[2.638552],[2.607429],[-8.338159],[6.698901],[-1.993381],[0.784074],[0.130188],[0.244438],[-0.778762],[9.443969],[-4.676313],[-3.126573],[4.572540],[-5.759526],[-4.159336],[-8.075657],[1.438528],[-9.917912],[-5.256465],[6.658403],[-0.907101],[-1.606004],[3.847175],[-7.777314],[-8.272167],[2.278340],[0.443122],[7.085572],[6.715226],[4.765843],[5.416575],[1.109524],[-0.768989],[0.530140],[8.633540],[2.152057],[5.331533],[-2.987595],[8.282704],[-8.160914],[-0.810076],[-3.694982],[3.216372],[-1.967738],[-5.471542],[4.560576],[-7.691875],[-2.320390],[-6.910964],[4.133540],[1.672433],[3.010895],[-0.533120],[4.702785],[-1.049959],[5.482036],[7.813338],[9.963838],[-2.890380],[0.813405],[7.642312],[-2.871694],[6.686844],[-1.200903],[-6.334279],[-7.275754],[-2.902051],[2.180362],[4.071652],[-3.157729],[-3.235748],[-6.632294],[-0.504444],[9.316591],[9.219254],[9.974325],[0.409010],[-5.786428],[-6.850667],[-7.032596],[-7.322421],[-4.197218],[-7.568487],[-0.827211],[-0.899515],[-6.684520],[-7.239259],[0.842596],[-4.029989],[8.110433],[0.571009],[-8.766875],[7.543110],[-5.595618],[-3.724027],[-6.549511],[0.765148],[2.779764],[-9.439735],[4.850711],[0.106596],[-5.920594],[-0.720578],[-4.451385],[-8.928599],[-5.986976],[-4.868500],[-7.002979],[-5.509007],[1.634419],[4.258826],[8.113873],[4.343906],[-9.372257],[-6.371725],[-2.228212],[2.916414],[-2.504754],[-8.425507],[-6.186611],[-5.893041],[6.454684],[-9.918905],[-3.522602],[-2.751366],[1.007748],[-5.926156],[-9.873706],[0.936453],[5.488821],[-6.843998],[4.198501],[-5.343081],[7.563852],[-9.366822],[7.130819],[-0.255157],[4.208114],[-8.585341],[7.512826],[-2.798885],[-8.509247],[-2.492439],[-9.283472],[-4.636107],[3.867231],[9.074113],[-6.009596],[-7.586387],[8.907775],[-0.507003],[-5.311706],[9.409100],[6.361435],[2.337661],[-4.938852],[0.588956],[-3.647940],[2.205905],[4.515176],[3.605901],[-4.800714],[-4.547510],[-3.282092],[-1.607942],[5.321540],[7.629709],[5.159923],[-5.082851],[-3.988086],[-7.335037],[2.865950],[-3.123879],[9.613119],[-1.197856],[0.101040],[9.876898],[-7.754975],[-6.584062],[8.655556],[-8.237949],[6.055457],[-0.567154],[-8.966365],[8.888867],[-8.096081],[8.355159],[8.120718],[-4.266946],[5.789541],[-1.286821],[-7.831275],[-4.219292],[4.805947],[6.233060],[3.485540],[1.416050],[6.086235],[-6.822779],[-9.585501],[8.668491],[5.086469],[-9.358637],[-5.766282],[3.923770],[0.762068],[-4.010878],[7.900285],[3.333302],[8.716560],[5.111979],[-1.040066],[-0.174933],[-9.903249],[-3.381104],[-7.138217],[-9.497353],[-7.447857],[9.491770],[2.619839],[1.200269],[-2.414418],[-0.884635],[-8.483366],[-6.800644],[-1.652995],[0.045011],[-6.801838],[2.615824],[-0.825428],[-4.761413],[3.114500],[-9.134717],[9.749355],[-5.814319],[-1.386494],[-6.535193],[6.385347],[-9.445879],[-3.949180],[9.012008],[5.104368],[8.846872],[-3.263454],[-7.053516],[-3.682344],[-2.297825],[4.221132],[-2.485805],[-3.468908],[1.200256],[-3.574530],[0.816850],[-3.218131],[6.531799],[-4.809979],[-2.896965],[4.418115],[6.383913],[-1.278638],[-7.566825],[-6.006638],[-4.724526],[7.372663],[2.936571],[6.681562],[-7.687606],[-7.836989],[6.136798],[-5.053044],[8.876945],[9.231543],[-3.422106],[0.198102],[6.458070],[9.647590],[1.822311],[-6.844028],[-4.658472],[-0.851990],[8.400339],[-4.305557],[6.492095],[2.094885],[-1.473096],[6.179558],[-1.690705],[8.807782],[-6.368887],[-8.993938],[-9.985289],[5.540424],[-9.383960],[1.704227],[-8.272340],[-0.386712],[7.086420],[2.843395],[4.642951],[6.053825],[-6.552879],[1.552473],[7.439537],[8.267153],[5.678299],[2.400614],[-8.599051],[7.482100],[-7.830969],[5.732416],[-3.854944],[-2.674310],[-7.267401],[-2.991122],[-1.541034],[4.029701],[1.888331],[2.272123],[0.530508],[-7.038486],[4.233239],[-4.203541],[-5.550242],[-4.996606],[-5.673297],[4.165312],[9.960373],[-3.347863],[-4.582136],[9.138850],[-8.144021],[9.212425],[9.243647],[2.893365],[-3.767272],[2.748053],[5.218256],[3.447203],[-9.061894],[1.397348],[0.354325],[7.702988],[-8.967655],[-7.974912],[2.498749],[-0.245177],[2.301666],[5.780063],[-6.676549],[3.912979],[-0.950356],[-9.648284],[6.240323],[2.448994],[5.084441],[-0.818548],[-7.109632],[1.512076],[-9.672786],[1.962103],[3.331649],[4.875934],[3.991040],[5.281638],[8.148261],[-2.261291],[-0.086373],[-4.405021],[-3.338247],[3.620006],[-9.487433],[-6.098446],[3.787974],[9.300241],[-4.508927],[6.616871],[-5.371767],[-9.272640],[1.570018],[-2.948182],[-9.468767],[-1.404781],[5.824192],[-3.848822],[6.847128],[-1.863644],[-9.286461],[-2.561029],[-4.654839],[6.504463],[-8.910385],[9.294727],[7.539267],[-0.225033],[4.032333],[-1.180233],[-9.634527],[-6.270077],[5.698782],[6.611275],[-7.169045],[-3.715929],[0.378597],[2.421211],[-4.136121],[-0.250019],[0.702867],[-4.172929],[7.526042],[-6.586324],[0.813159],[-9.727399],[1.988009],[4.161267],[-0.044682],[1.666012],[-4.332951],[8.822878],[-2.028088],[-3.800432],[2.538261],[2.623229],[-3.406963],[6.789805],[3.376307],[-3.198457],[-3.734547],[-9.771857],[-6.175234],[-2.494119],[-2.411482],[9.611390],[9.457439],[-2.596656],[4.712755],[7.970912],[1.325078],[-5.539180],[-9.492221],[2.242982],[7.234146],[-1.482969],[2.076227],[9.815026],[-3.623872],[-8.018075],[-0.375277],[-9.420185],[-5.553688],[3.920980],[1.657236],[-5.915930],[-8.006970],[-5.580947],[-0.301799],[-3.475261],[6.437407],[-7.578097],[4.631845],[-1.220048],[5.860355],[-6.628201],[7.039584],[-5.119650],[-3.526929],[5.727856],[-1.793437],[-7.128300],[-0.627565],[4.861140],[3.163333],[-8.753873],[-6.471258],[5.033533],[6.160968],[7.669194],[-6.042715],[-2.864687],[-8.150593],[8.675984],[-5.226172],[-7.966180],[-0.714741],[0.799433],[4.098950],[1.853136],[-6.579649],[-0.571038],[-6.083746],[-2.015250],[2.400413],[8.479934],[-2.564062],[5.226329],[-6.488219],[0.562274],[-5.939526],[6.418525],[-9.235087],[8.281100],[7.873216],[-1.144503],[2.738345],[-3.971046],[-2.429495],[4.035165],[-9.218485],[2.895306],[-1.519330],[-5.716650],[2.497071],[5.364334],[1.509138],[-6.039213],[-6.572310],[-4.922606],[4.343662],[4.500488],[3.350859],[-0.746208],[6.429863],[1.717293],[-5.774997],[-7.355708],[-3.157089],[2.881927],[-3.208707],[8.398017],[4.499634],[4.715559],[7.741646],[0.671397],[7.803466],[5.739257],[-2.324921],[-0.563899],[0.145856],[-5.352416],[2.630906],[-5.962279],[3.782446],[8.026785],[5.605023],[7.386184],[4.349142],[-3.416048],[-6.997178],[1.159151],[-4.694226],[-4.274604],[-8.388767],[-0.314634],[0.542770],[-6.173292],[3.704591],[-1.554884],[-0.605799],[-4.393724],[-6.041159],[4.547744],[0.276846],[-1.424285],[6.930336],[2.245823],[4.399580],[1.837651],[-8.301465],[2.386080],[-0.826700],[-9.421269],[4.525351],[-1.969838],[1.955037],[0.864845],[-9.554455],[8.639002],[-6.134344],[-4.896002],[0.488412],[7.818966],[0.039572],[-3.087641],[6.513959],[9.940222],[8.714553],[7.308267],[-8.605951],[5.127518],[8.729039],[0.307398],[4.663823],[8.197220],[4.736605],[4.057625],[4.370146],[0.054913],[0.866866],[-2.337158],[8.878717],[-3.420426],[-9.094543],[2.089130],[6.689866],[-9.397617],[2.265067],[9.881909],[-5.757323],[-7.267717],[-5.180841],[-4.012123],[6.111958],[-7.656927],[0.160167],[9.481635],[5.641989],[-4.936247],[8.185824],[-1.522418],[-3.228876],[4.121326],[5.694657],[-6.684933],[4.438447],[8.631371],[-2.746205],[8.817982],[3.122322],[5.135281],[0.283639],[6.946508],[-5.341565],[-6.644202]], dtype = "float64")#candidate|7100|(1404, 1)|const|float64
call_7099 = relay.TupleGetItem(func_6403_call(relay.reshape(const_7100.astype('float64'), [12, 13, 9])), 0)
call_7101 = relay.TupleGetItem(func_6405_call(relay.reshape(const_7100.astype('float64'), [12, 13, 9])), 0)
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_7102 = func_4335_call()
call_7103 = func_4335_call()
bop_7104 = relay.maximum(const_7100.astype('uint16'), relay.reshape(call_7099.astype('uint16'), relay.shape_of(const_7100))) # shape=(1404, 1)
bop_7107 = relay.maximum(const_7100.astype('uint16'), relay.reshape(call_7101.astype('uint16'), relay.shape_of(const_7100))) # shape=(1404, 1)
output = relay.Tuple([call_7053,call_7081,var_7082,call_7091,const_7092,call_7102,bop_7104,])
output2 = relay.Tuple([call_7054,call_7083,var_7082,call_7093,const_7092,call_7103,bop_7107,])
func_7117 = relay.Function([var_7082,], output)
mod['func_7117'] = func_7117
mod = relay.transform.InferType()(mod)
mutated_mod['func_7117'] = func_7117
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7118 = relay.var("var_7118", dtype = "int64", shape = (1296,))#candidate|7118|(1296,)|var|int64
func_7117_call = mutated_mod.get_global_var('func_7117')
call_7119 = func_7117_call(var_7118)
output = call_7119
func_7120 = relay.Function([var_7118], output)
mutated_mod['func_7120'] = func_7120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3384_call = mod.get_global_var('func_3384')
func_3386_call = mutated_mod.get_global_var('func_3386')
call_7143 = relay.TupleGetItem(func_3384_call(), 4)
call_7144 = relay.TupleGetItem(func_3386_call(), 4)
output = relay.Tuple([call_7143,])
output2 = relay.Tuple([call_7144,])
func_7162 = relay.Function([], output)
mod['func_7162'] = func_7162
mod = relay.transform.InferType()(mod)
output = func_7162()
func_7163 = relay.Function([], output)
mutated_mod['func_7163'] = func_7163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_7238 = relay.TupleGetItem(func_506_call(), 0)
call_7239 = relay.TupleGetItem(func_507_call(), 0)
func_6388_call = mod.get_global_var('func_6388')
func_6389_call = mutated_mod.get_global_var('func_6389')
call_7249 = relay.TupleGetItem(func_6388_call(), 1)
call_7250 = relay.TupleGetItem(func_6389_call(), 1)
var_7261 = relay.var("var_7261", dtype = "uint64", shape = (16, 3, 9))#candidate|7261|(16, 3, 9)|var|uint64
bop_7262 = relay.bitwise_and(call_7238.astype('int16'), var_7261.astype('int16')) # shape=(16, 3, 9)
bop_7265 = relay.bitwise_and(call_7239.astype('int16'), var_7261.astype('int16')) # shape=(16, 3, 9)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_7275 = relay.TupleGetItem(func_468_call(), 2)
call_7276 = relay.TupleGetItem(func_470_call(), 2)
func_5434_call = mod.get_global_var('func_5434')
func_5436_call = mutated_mod.get_global_var('func_5436')
const_7286 = relay.const([[1.978547,-2.344042,5.373280,-3.303688,-5.030496,-4.875107,-3.317155,-1.275854,3.877688,-0.185765,-8.405188,-2.404442,4.045140,-8.995621,-1.673991,1.563591,-8.109523,2.098344,3.267750,7.317015,3.921013,6.719542,2.950395,-4.251979,-2.978888,4.748267,-9.578393,-8.026969,0.622313,8.531428,-5.266845,3.738841,-2.278402,-8.239763,-8.257539,-8.920032,9.967280,2.359569,3.587314,3.483924],[-1.105981,-1.949996,-3.633993,-0.671244,-5.526739,-6.145485,-5.721881,9.147156,-5.288965,1.401215,6.308386,-3.972160,4.184008,1.154081,5.580804,-7.562452,5.220404,-7.666060,-0.177840,7.819250,9.644399,5.071581,-6.492396,-9.877211,-3.225547,2.950735,0.623694,8.560429,-4.906069,-6.161563,9.177615,1.198455,2.371175,7.500606,3.559056,-7.195649,-5.985034,-5.047809,-2.028091,3.605763],[-5.418404,-3.210880,-8.751095,-7.384148,-3.806774,-9.199902,-2.052500,-9.954973,-2.461704,0.438826,8.805399,-4.370422,3.623273,-8.086540,1.606948,-1.641568,-6.806304,-3.513810,-3.450490,5.906658,4.649233,0.499364,-7.404219,4.006404,4.681234,-6.528838,6.321219,-3.679952,0.656357,-1.359924,-4.260256,3.302174,-1.983617,2.987815,-7.624423,7.998591,-7.099105,4.921118,9.572429,8.139277]], dtype = "float64")#candidate|7286|(3, 40)|const|float64
call_7285 = relay.TupleGetItem(func_5434_call(relay.reshape(const_7286.astype('float64'), [1, 8, 15])), 1)
call_7287 = relay.TupleGetItem(func_5436_call(relay.reshape(const_7286.astype('float64'), [1, 8, 15])), 1)
output = relay.Tuple([call_7249,bop_7262,call_7275,call_7285,const_7286,])
output2 = relay.Tuple([call_7250,bop_7265,call_7276,call_7287,const_7286,])
func_7297 = relay.Function([var_7261,], output)
mod['func_7297'] = func_7297
mod = relay.transform.InferType()(mod)
var_7298 = relay.var("var_7298", dtype = "uint64", shape = (16, 3, 9))#candidate|7298|(16, 3, 9)|var|uint64
output = func_7297(var_7298)
func_7299 = relay.Function([var_7298], output)
mutated_mod['func_7299'] = func_7299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4523_call = mod.get_global_var('func_4523')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_7343 = relay.TupleGetItem(func_4523_call(), 0)
call_7344 = relay.TupleGetItem(func_4524_call(), 0)
output = relay.Tuple([call_7343,])
output2 = relay.Tuple([call_7344,])
func_7345 = relay.Function([], output)
mod['func_7345'] = func_7345
mod = relay.transform.InferType()(mod)
output = func_7345()
func_7346 = relay.Function([], output)
mutated_mod['func_7346'] = func_7346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1404_call = mod.get_global_var('func_1404')
func_1406_call = mutated_mod.get_global_var('func_1406')
call_7447 = func_1404_call()
call_7448 = func_1404_call()
output = relay.Tuple([call_7447,])
output2 = relay.Tuple([call_7448,])
func_7466 = relay.Function([], output)
mod['func_7466'] = func_7466
mod = relay.transform.InferType()(mod)
output = func_7466()
func_7467 = relay.Function([], output)
mutated_mod['func_7467'] = func_7467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_7501 = relay.TupleGetItem(func_468_call(), 0)
call_7502 = relay.TupleGetItem(func_470_call(), 0)
func_4417_call = mod.get_global_var('func_4417')
func_4419_call = mutated_mod.get_global_var('func_4419')
call_7507 = func_4417_call()
call_7508 = func_4417_call()
output = relay.Tuple([call_7501,call_7507,])
output2 = relay.Tuple([call_7502,call_7508,])
func_7513 = relay.Function([], output)
mod['func_7513'] = func_7513
mod = relay.transform.InferType()(mod)
mutated_mod['func_7513'] = func_7513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7513_call = mutated_mod.get_global_var('func_7513')
call_7514 = func_7513_call()
output = call_7514
func_7515 = relay.Function([], output)
mutated_mod['func_7515'] = func_7515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_296_call = mod.get_global_var('func_296')
func_297_call = mutated_mod.get_global_var('func_297')
call_7585 = relay.TupleGetItem(func_296_call(), 0)
call_7586 = relay.TupleGetItem(func_297_call(), 0)
output = call_7585
output2 = call_7586
func_7592 = relay.Function([], output)
mod['func_7592'] = func_7592
mod = relay.transform.InferType()(mod)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7592_call = mutated_mod.get_global_var('func_7592')
call_7593 = func_7592_call()
output = call_7593
func_7594 = relay.Function([], output)
mutated_mod['func_7594'] = func_7594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1483_call = mod.get_global_var('func_1483')
func_1485_call = mutated_mod.get_global_var('func_1485')
call_7609 = relay.TupleGetItem(func_1483_call(), 3)
call_7610 = relay.TupleGetItem(func_1485_call(), 3)
output = relay.Tuple([call_7609,])
output2 = relay.Tuple([call_7610,])
func_7612 = relay.Function([], output)
mod['func_7612'] = func_7612
mod = relay.transform.InferType()(mod)
mutated_mod['func_7612'] = func_7612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7612_call = mutated_mod.get_global_var('func_7612')
call_7613 = func_7612_call()
output = call_7613
func_7614 = relay.Function([], output)
mutated_mod['func_7614'] = func_7614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_7634 = relay.TupleGetItem(func_506_call(), 1)
call_7635 = relay.TupleGetItem(func_507_call(), 1)
output = call_7634
output2 = call_7635
func_7657 = relay.Function([], output)
mod['func_7657'] = func_7657
mod = relay.transform.InferType()(mod)
mutated_mod['func_7657'] = func_7657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7657_call = mutated_mod.get_global_var('func_7657')
call_7658 = func_7657_call()
output = call_7658
func_7659 = relay.Function([], output)
mutated_mod['func_7659'] = func_7659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1762_call = mod.get_global_var('func_1762')
func_1764_call = mutated_mod.get_global_var('func_1764')
call_7728 = relay.TupleGetItem(func_1762_call(), 0)
call_7729 = relay.TupleGetItem(func_1764_call(), 0)
const_7733 = relay.const([[[-10,-3,-10,10,-6,6,-2,-2,1],[-1,5,-8,10,-1,-2,-6,2,1],[10,5,10,-1,-4,-5,10,6,3],[-4,-3,3,-8,10,-10,5,4,-3],[9,1,1,-10,3,10,2,-8,-9],[-2,1,10,-3,-9,-2,3,10,-7],[-1,4,3,-9,-6,-9,9,-5,-3],[10,-7,-7,3,4,-6,-4,8,-1],[10,5,9,4,-7,-8,1,10,-9]],[[10,-7,-5,5,-9,5,-3,2,-2],[4,-10,-2,-3,6,-4,-8,-5,9],[7,-9,-5,8,9,6,10,-7,10],[9,-4,-7,-8,-1,10,-4,3,5],[8,-6,3,8,3,-4,-5,-6,-7],[-5,10,9,7,-8,5,-6,9,9],[5,5,-3,3,-3,-8,4,5,-1],[-3,-6,-7,-6,-5,7,7,3,2],[-3,5,3,-6,7,10,-6,6,-6]],[[4,-8,-1,4,8,9,3,-4,10],[2,-6,-7,-8,-1,-6,7,-3,2],[-9,9,4,-9,4,5,-1,-9,-9],[5,-1,2,-5,1,6,-9,10,6],[10,8,7,5,4,6,2,1,-8],[-1,3,-1,5,-8,2,6,-7,5],[2,3,5,9,3,-9,2,5,3],[-8,8,5,10,-1,8,1,5,7],[-5,5,6,-8,7,-6,9,-1,10]],[[6,-7,-6,-2,-8,1,7,10,2],[10,-4,3,-7,4,9,4,-3,-4],[-10,6,-3,1,-4,4,7,-6,-10],[3,-1,-5,-2,-6,2,5,-6,7],[-1,3,-9,1,-10,-1,6,-8,-10],[9,-4,10,-7,-7,10,-4,2,4],[6,-9,2,9,-3,-7,1,-8,1],[10,-5,-2,-9,-5,6,4,5,-8],[-5,-7,3,-3,9,7,1,9,4]],[[-10,8,6,5,5,5,-6,-8,9],[6,6,-5,-7,-10,-4,-8,7,-10],[-9,3,6,5,8,-7,-7,-3,10],[7,6,-6,4,-5,-9,4,-1,-1],[-6,-10,-4,-3,2,5,6,1,-9],[-2,-10,-4,3,6,8,2,-6,8],[1,-10,-9,-5,4,7,-3,-6,6],[-2,1,-3,-5,-3,-9,-10,4,1],[2,-8,-2,-2,4,7,-2,-8,-7]],[[2,-8,-5,-9,7,-5,-9,-6,5],[-2,4,7,-5,-10,-1,-4,1,1],[-8,10,-4,-6,4,-9,-2,10,-6],[-9,7,4,8,-5,9,-6,-4,4],[3,-2,4,10,2,-3,-6,-3,-2],[2,-6,-1,-1,-4,5,-5,-10,7],[-8,-9,6,1,2,6,-1,-6,-5],[4,5,-5,7,-9,6,-10,-7,-7],[1,-7,-3,9,-5,-3,-3,8,-4]],[[-8,-4,-8,7,7,7,6,-3,10],[-10,-10,-5,5,9,-8,8,-3,-5],[3,9,3,-3,3,-2,9,-4,-6],[1,1,-5,-2,4,-5,6,-8,-5],[2,-10,1,-10,5,-9,-4,-10,-10],[-3,10,-8,4,-1,3,-5,-6,-2],[8,-9,-7,-2,1,-8,-1,-3,-6],[-5,7,7,4,6,7,-6,1,8],[4,-9,-3,5,-7,4,1,6,-5]]], dtype = "uint8")#candidate|7733|(7, 9, 9)|const|uint8
bop_7734 = relay.maximum(call_7728.astype('float32'), relay.reshape(const_7733.astype('float32'), relay.shape_of(call_7728))) # shape=(7, 9, 9)
bop_7737 = relay.maximum(call_7729.astype('float32'), relay.reshape(const_7733.astype('float32'), relay.shape_of(call_7729))) # shape=(7, 9, 9)
bop_7744 = relay.logical_or(call_7728.astype('bool'), relay.reshape(const_7733.astype('bool'), relay.shape_of(call_7728))) # shape=(7, 9, 9)
bop_7747 = relay.logical_or(call_7729.astype('bool'), relay.reshape(const_7733.astype('bool'), relay.shape_of(call_7729))) # shape=(7, 9, 9)
bop_7751 = relay.not_equal(call_7728.astype('bool'), relay.reshape(bop_7734.astype('bool'), relay.shape_of(call_7728))) # shape=(7, 9, 9)
bop_7754 = relay.not_equal(call_7729.astype('bool'), relay.reshape(bop_7737.astype('bool'), relay.shape_of(call_7729))) # shape=(7, 9, 9)
uop_7777 = relay.log(bop_7751.astype('float64')) # shape=(7, 9, 9)
uop_7779 = relay.log(bop_7754.astype('float64')) # shape=(7, 9, 9)
output = relay.Tuple([bop_7744,uop_7777,])
output2 = relay.Tuple([bop_7747,uop_7779,])
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
