import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_420 = relay.var("var_420", dtype = "float32", shape = (4, 8, 2))#candidate|420|(4, 8, 2)|var|float32
var_421 = relay.var("var_421", dtype = "float32", shape = (4, 8, 2))#candidate|421|(4, 8, 2)|var|float32
bop_422 = relay.greater_equal(var_420.astype('bool'), relay.reshape(var_421.astype('bool'), relay.shape_of(var_420))) # shape=(4, 8, 2)
output = bop_422
output2 = bop_422
func_427 = relay.Function([var_420,var_421,], output)
mod['func_427'] = func_427
mod = relay.transform.InferType()(mod)
var_428 = relay.var("var_428", dtype = "float32", shape = (4, 8, 2))#candidate|428|(4, 8, 2)|var|float32
var_429 = relay.var("var_429", dtype = "float32", shape = (4, 8, 2))#candidate|429|(4, 8, 2)|var|float32
output = func_427(var_428,var_429,)
func_430 = relay.Function([var_428,var_429,], output)
mutated_mod['func_430'] = func_430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_452 = relay.var("var_452", dtype = "float32", shape = (11, 1, 3))#candidate|452|(11, 1, 3)|var|float32
var_453 = relay.var("var_453", dtype = "float32", shape = (11, 16, 3))#candidate|453|(11, 16, 3)|var|float32
bop_454 = relay.divide(var_452.astype('float32'), var_453.astype('float32')) # shape=(11, 16, 3)
output = relay.Tuple([bop_454,])
output2 = relay.Tuple([bop_454,])
func_458 = relay.Function([var_452,var_453,], output)
mod['func_458'] = func_458
mod = relay.transform.InferType()(mod)
mutated_mod['func_458'] = func_458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_458_call = mutated_mod.get_global_var('func_458')
var_460 = relay.var("var_460", dtype = "float32", shape = (11, 1, 3))#candidate|460|(11, 1, 3)|var|float32
var_461 = relay.var("var_461", dtype = "float32", shape = (11, 16, 3))#candidate|461|(11, 16, 3)|var|float32
call_459 = func_458_call(var_460,var_461,)
output = call_459
func_462 = relay.Function([var_460,var_461,], output)
mutated_mod['func_462'] = func_462
mutated_mod = relay.transform.InferType()(mutated_mod)
const_475 = relay.const([[[0.938200,8.508950,9.695315,-2.713517,-4.943022,5.631812,-0.429654,4.728413],[-0.775041,-8.546795,-2.000798,7.634453,-0.543241,-2.167412,-0.715017,2.790815],[-1.144771,-6.166223,-8.935283,-5.285213,6.371332,-2.288957,-3.023388,-2.605618],[9.371819,4.214801,-1.510991,4.009190,-6.771690,1.746348,9.645264,-9.653409],[5.541476,-0.787082,-7.174852,2.273271,-2.735911,0.830111,8.246289,8.386835],[-7.563348,-8.182366,-9.017167,-4.482781,5.553410,1.963783,-5.914410,-9.276803],[-1.723765,9.201939,7.570263,8.327716,1.344593,9.606287,-1.468141,5.258833],[0.964450,3.340303,-9.397599,-2.858992,9.549846,-9.362494,7.414499,-6.362446]]], dtype = "float64")#candidate|475|(1, 8, 8)|const|float64
uop_476 = relay.asinh(const_475.astype('float64')) # shape=(1, 8, 8)
uop_486 = relay.rsqrt(const_475.astype('float64')) # shape=(1, 8, 8)
bop_494 = relay.subtract(uop_486.astype('int16'), relay.reshape(uop_476.astype('int16'), relay.shape_of(uop_486))) # shape=(1, 8, 8)
func_458_call = mod.get_global_var('func_458')
func_462_call = mutated_mod.get_global_var('func_462')
const_499 = relay.const([-0.107532,5.718564,5.597091,7.739544,-8.548754,0.866707,-0.954342,8.838754,-6.314101,-6.582781,5.841060,-6.319784,-3.905750,-7.423594,4.527593,-6.363620,-7.757656,7.419384,0.809689,8.978062,9.416959,6.050539,0.444010,-9.624401,-3.063442,7.112906,0.939308,4.049852,-6.565734,5.118715,2.778563,2.458539,7.077194], dtype = "float32")#candidate|499|(33,)|const|float32
const_500 = relay.const([-9.178563,8.036486,0.706180,3.491568,1.926595,-5.075936,4.554150,-1.040831,5.988510,-4.378164,-1.632270,5.139041,5.773068,-6.086133,5.498891,-4.530938,5.268464,1.242259,-0.878901,-7.292213,7.005864,9.077761,-0.395362,3.518678,-0.948472,5.029923,8.310913,-7.796664,8.906318,-1.383843,7.916819,1.661018,-7.707690,3.100940,1.405319,-0.669624,-9.572620,8.761094,4.540146,-5.443907,-9.237720,3.936546,-4.136287,-5.785132,-8.101292,-1.908510,5.530360,-9.309075,4.055182,3.452113,-7.673149,4.232202,9.404165,8.471200,5.190095,-5.623415,1.346991,-8.514310,7.792803,-3.875205,1.443451,0.673947,-6.870819,-2.498429,0.702184,-1.648453,-0.341139,-5.102401,-9.107778,-4.872806,-1.743958,7.353074,-0.656008,7.531156,-4.162880,-5.510692,3.579330,5.622731,1.090787,0.237454,9.084028,-6.749525,1.109564,0.663448,5.431398,1.293897,-1.534399,4.409588,-2.917143,-8.270504,-8.524114,-5.858017,1.758361,1.312892,-8.939913,4.866481,-4.604884,1.603164,7.117304,3.973672,-1.944134,-2.436007,1.959172,-3.423145,-5.862285,5.488734,1.311963,-0.600813,7.701993,0.805825,-5.972025,9.449943,5.187315,-2.544675,9.323790,3.917415,7.306220,-3.425106,7.032503,-7.149736,1.822173,2.710987,-8.014091,0.739090,6.644536,9.895483,-0.358898,1.888614,9.518497,-6.502909,5.994278,-9.442220,7.862741,-5.081751,2.200698,-3.967739,-7.624598,1.530809,-4.535790,-8.045693,-4.419184,0.035484,-1.807279,-1.105711,1.218959,-5.899318,-1.425213,3.609827,2.685593,-6.151874,-7.283304,6.947704,-5.371237,4.208970,-4.833489,0.617162,8.200987,2.476814,2.052149,6.702321,-7.796811,6.314311,3.502496,-8.095230,-1.428939,6.605131,4.880096,7.065244,-9.021714,-4.898603,-2.082005,9.787936,2.514957,9.907872,-9.284868,8.131424,-8.955754,5.393512,1.681960,-7.883606,-2.019872,-0.196997,1.545417,-0.498604,8.192922,-6.856492,-6.812827,2.385060,-4.606248,-8.727329,-2.937804,7.758215,-2.194478,-7.480547,-6.650028,-2.601893,-2.254302,-7.916266,-9.644203,6.071912,-5.838854,-6.450868,5.061993,-4.369622,-9.307011,-4.283813,-6.706451,-3.538157,-5.765941,-5.052063,3.539316,-6.307024,7.466023,6.690681,3.918171,6.160076,-3.289036,-4.084914,-0.568036,8.082288,1.669395,3.997356,0.905305,-2.982953,-8.366034,-3.910455,2.776400,5.107608,-6.885225,7.914920,-0.789855,3.983195,-2.033541,-3.301195,-0.231351,2.102076,-4.756385,0.211375,-4.862416,2.792755,-3.195587,9.324600,-5.023912,-2.459607,1.692324,-8.544407,8.995451,1.758679,1.065233,-0.999601,9.355555,9.429336,-7.717781,-8.807479,1.153879,1.118440,7.583374,1.413792,0.459844,-2.586734,1.021999,-8.091475,-1.838664,-0.002022,-0.205183,7.948890,1.907801,2.473723,4.495825,-9.736877,7.203351,-0.350524,-4.639826,5.164821,-1.135852,6.858919,-1.056039,-3.137543,7.255001,2.615457,7.875850,6.501402,6.762298,-3.925136,-5.220905,4.225349,-1.380401,5.036651,-1.098271,-4.718778,-7.202224,-2.087124,-2.726208,-8.129632,-8.393887,0.546320,-0.939234,-3.279859,9.466150,3.731853,0.178660,8.983299,-8.647647,9.010420,0.857359,5.582373,2.629033,8.899273,-0.567332,9.955258,9.723552,-6.877526,7.080796,0.344601,2.519781,3.277539,-1.778078,-3.688783,1.732199,6.645875,-5.484839,-4.309341,-9.474604,4.622404,9.959002,5.646992,8.570962,9.794911,-6.307737,8.869331,6.149651,4.449724,8.217560,-5.582344,1.862132,-2.832834,0.423422,3.044891,-5.777488,-5.806142,9.021373,-0.154629,-5.377727,9.218737,-2.467489,-8.212322,1.458810,5.410566,-2.778194,5.784165,4.378228,8.225924,3.277999,5.307129,5.944372,7.199924,7.615987,1.658164,2.401497,1.577269,4.573806,3.071169,8.090981,7.426314,8.505223,2.703281,-0.045522,7.758994,1.637569,0.362120,-8.753314,9.872129,-5.732129,9.314395,2.796917,-9.395059,4.780113,-4.228221,-3.524795,-2.314419,-8.742417,1.685438,-3.203143,-5.233120,9.306126,-0.762558,2.957142,7.251556,-1.261558,6.676679,3.162074,-2.267810,-4.988142,7.016548,-6.011282,-8.139174,6.702062,-8.146747,-8.420238,7.551042,-1.266630,3.672773,7.674873,-1.032012,-8.473360,-2.145174,8.863477,-6.936238,8.096008,-6.132769,4.528911,-8.182643,-9.339834,-6.801335,-0.782891,-5.190527,7.684517,-0.925356,8.583562,-9.498780,-0.803492,8.381823,4.944246,9.263227,-4.097153,-1.059782,-9.134189,-3.122878,8.908919,9.264553,2.972715,1.581595,-8.162880,0.619386,-8.621099,0.745319,-2.837350,-6.240424,-2.242683,-6.036970,5.675936,-5.246541,-8.109592,8.782640,4.206929,7.057124,-6.637704,6.787816,-0.516771,-7.128479,-7.925626,5.124369,6.954901,-5.167434,-4.396420,-8.190992,5.982192,3.321940,4.833234,-0.226005,-6.066073,8.419918,-9.862666,8.118341,-5.152716,6.095390,0.227570,4.461826,-8.332162,-2.563859,3.561218,-1.039103,4.970372,-8.997036,-6.543797,2.778589,-4.643717,-6.769520,1.735763,3.646048,7.990735,-8.801290,4.354812,8.312328,2.808132,-6.464192,-2.555681,9.380128,2.302252,1.367981,-6.265853,-6.488018,4.505019,0.898257,-9.456173,-7.269286,8.461682,-8.526768,8.628984,-0.901263,2.766484,2.938661,-7.071862,4.867681,-8.425837,1.597910,5.064020,3.740888,-4.563087,3.600615,6.938982,7.458004,-8.461293,0.009743,3.342055,-6.260217,2.500008,8.223355,-4.526755,3.131933,4.124326,-2.714529,-2.886046,2.816149,-8.312521,1.197705,1.599612,5.937793], dtype = "float32")#candidate|500|(528,)|const|float32
call_498 = relay.TupleGetItem(func_458_call(relay.reshape(const_499.astype('float32'), [11, 1, 3]), relay.reshape(const_500.astype('float32'), [11, 16, 3]), ), 0)
call_501 = relay.TupleGetItem(func_462_call(relay.reshape(const_499.astype('float32'), [11, 1, 3]), relay.reshape(const_500.astype('float32'), [11, 16, 3]), ), 0)
output = relay.Tuple([bop_494,call_498,const_499,const_500,])
output2 = relay.Tuple([bop_494,call_501,const_499,const_500,])
func_503 = relay.Function([], output)
mod['func_503'] = func_503
mod = relay.transform.InferType()(mod)
output = func_503()
func_504 = relay.Function([], output)
mutated_mod['func_504'] = func_504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_503_call = mod.get_global_var('func_503')
func_504_call = mutated_mod.get_global_var('func_504')
call_526 = relay.TupleGetItem(func_503_call(), 2)
call_527 = relay.TupleGetItem(func_504_call(), 2)
uop_537 = relay.atanh(call_526.astype('float64')) # shape=(33,)
uop_539 = relay.atanh(call_527.astype('float64')) # shape=(33,)
output = uop_537
output2 = uop_539
func_542 = relay.Function([], output)
mod['func_542'] = func_542
mod = relay.transform.InferType()(mod)
mutated_mod['func_542'] = func_542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mutated_mod.get_global_var('func_542')
call_543 = func_542_call()
output = call_543
func_544 = relay.Function([], output)
mutated_mod['func_544'] = func_544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_503_call = mod.get_global_var('func_503')
func_504_call = mutated_mod.get_global_var('func_504')
call_558 = relay.TupleGetItem(func_503_call(), 2)
call_559 = relay.TupleGetItem(func_504_call(), 2)
func_458_call = mod.get_global_var('func_458')
func_462_call = mutated_mod.get_global_var('func_462')
const_561 = relay.const([9.495997,3.530981,-0.221425,9.555056,7.169032,-7.574799,-2.901829,-1.186116,-3.149821,3.038259,-6.695052,-2.501319,8.070253,8.255810,5.451417,-5.479250,-7.636175,2.911000,0.413934,-0.907472,7.703261,-8.914548,5.954331,-4.877007,-6.740570,6.986242,1.335638,5.667189,4.292815,8.991071,-6.926580,-2.099056,0.272426,8.420698,-9.593833,5.804498,-1.820882,9.636534,-3.482102,4.085215,7.280174,-7.091055,-3.872296,4.124571,-6.850137,8.374948,-6.275141,-2.717252,6.826915,3.150851,9.103345,9.814807,-7.597031,9.011014,-3.285250,-4.236075,3.265073,-3.075999,-8.542771,0.285139,-9.085421,5.540193,-5.693815,-6.396706,8.870942,5.124721,-9.730577,-0.311459,8.986682,-5.987586,-3.022339,9.956848,6.527836,-7.178131,4.648484,-8.339895,-7.241629,5.863726,9.086135,-1.666529,9.544666,9.367342,-4.791683,-3.127328,6.251804,-8.968694,7.120980,3.175441,1.348281,-9.073034,-2.778279,7.782562,-3.433406,1.713277,-4.336122,-6.583139,-1.471654,-7.643358,3.618277,-0.232303,7.996159,1.267848,5.051181,5.286303,-5.052910,9.822865,-3.420742,0.817851,9.854971,0.871717,-2.292035,6.369222,7.737269,7.541529,7.726409,-7.667590,-0.884098,1.951555,-2.889952,3.285086,0.342499,6.278931,9.482810,-9.861887,-5.530287,-9.320861,-3.732442,5.187146,3.295628,-9.181436,-2.782576,2.109368,-1.183519,-1.110713,3.687918,2.751424,3.285475,3.790317,4.621162,0.042458,9.467483,-7.466753,-5.794755,6.094766,1.897528,-8.783063,-9.476245,-7.971405,-0.958583,-8.284247,-1.695299,-1.668995,-1.433034,-6.023715,-4.312907,4.061148,-1.343973,3.713059,7.156142,-7.778297,-2.358698,1.609631,5.284818,-1.392021,-0.061724,5.368896,-5.287486,-0.447686,7.386499,3.191142,9.778839,1.109891,-7.673287,-7.925359,-9.623251,-0.193024,9.445896,8.335713,-3.686080,-9.050638,-1.986756,7.227259,-3.970254,-8.224538,0.991148,1.416869,-9.495986,-1.841410,3.941439,1.343772,9.800526,-3.961501,8.032208,5.520181,8.448999,-4.174316,-9.450401,6.275729,-5.508998,-7.921266,7.734872,-6.965419,4.985016,-7.137501,1.755870,-9.055817,-2.703746,5.231037,-0.783092,6.802594,-0.949101,-5.576123,2.158796,0.294122,0.320190,1.548912,8.344574,-9.215971,-5.187830,9.432078,-8.467917,8.111796,8.031595,-7.665087,5.219044,7.466702,-3.907684,-3.679608,1.818823,2.538319,-1.468274,7.561779,-0.786461,-0.625463,9.251914,-4.477142,9.666356,-3.518687,-6.555805,-7.715256,-7.723350,3.685351,1.433742,-1.603102,-6.385271,0.988799,0.747458,-6.579754,4.017748,-8.154274,0.159774,-5.854102,-3.716705,5.360679,-3.274917,3.701384,8.214276,4.014618,-1.196210,-9.442668,5.754609,4.033328,-3.973535,-4.495800,-9.855445,-1.214165,1.786422,-9.036300,2.582749,-4.554024,-4.534080,-0.006861,-3.495406,-8.857481,-4.816639,3.747000,7.937547,-9.596173,1.298639,2.026008,0.621355,2.523821,-4.390811,1.902402,7.938248,6.607029,2.082907,6.610495,4.625875,-5.160579,-3.923820,7.981430,2.702695,-6.947982,-0.573149,-2.930395,9.814139,-4.448056,-5.268825,-2.723468,5.233235,9.667022,0.579935,3.676172,-7.791345,-3.638006,6.941642,-5.752078,9.473794,2.150376,-3.817826,-1.171882,1.384455,-2.749453,-8.739990,7.756124,-3.840160,-1.464905,-8.433114,9.007936,8.064902,0.919215,8.452324,6.031247,-7.539465,6.552668,7.915009,9.903479,-2.842579,-7.507186,-5.758811,2.405700,-2.578264,-6.215252,1.624665,3.887580,-7.219943,9.824757,0.430776,-4.828546,-4.601038,-5.229893,0.385059,-3.946103,2.025701,-4.287965,0.703528,4.966399,6.735257,-9.991550,1.374945,-8.896131,-0.597368,0.924554,-5.110986,-3.391877,6.920653,-1.365997,-3.322705,7.147731,9.035118,5.707192,6.339749,-2.988200,-0.926208,1.456815,1.673578,9.784835,5.987219,0.951648,1.865057,-6.039898,-5.929791,0.220282,-6.966606,4.304428,8.111791,-6.117099,3.209284,6.954681,2.734582,1.325923,-3.359842,-3.365027,3.942970,-9.651559,5.983217,-5.905890,2.244949,-5.182065,-4.773539,-2.153339,-2.727623,-9.176628,2.472990,-8.157151,-4.747370,6.830832,-1.610624,-5.443874,0.984847,-5.004065,-7.093311,5.266686,2.502742,4.416530,5.944728,1.004052,-5.774920,3.048468,1.836315,-1.144399,6.585527,1.618467,7.750789,1.824206,-8.495208,-2.297172,-8.530312,-2.381108,0.912642,6.968143,7.741593,5.892346,-7.635181,-1.778373,-7.492305,6.354134,-1.310579,2.418047,3.459652,0.605422,2.756079,-7.029553,5.477460,0.042677,-0.320252,9.465958,6.421653,5.603027,3.505439,4.823311,-8.547697,8.246865,0.599168,-7.460572,1.372104,-2.376730,9.071582,9.970398,-6.257319,-9.896420,0.966520,-0.683891,-5.250922,3.759696,4.723590,3.016863,8.795600,8.549658,8.070336,0.049809,0.736093,3.232796,-4.827396,4.129729,3.915001,8.936666,2.810917,6.836276,8.460476,4.293721,-3.998439,-9.161492,3.952160,-4.527485,-0.226608,7.847537,-1.581445,-2.592871,4.995248,2.027185,4.943764,-3.821384,-4.409144,-2.379036,-5.703267,4.693080,-1.761679,-3.650045,5.376307,1.063668,9.817630,2.029726,6.101619,-7.664698,9.214360,-8.189228,0.451934,1.301929,-3.541317,8.073188,7.590141,0.795601,0.145108,9.408626,0.713310,-8.988214,2.559210,-3.107409,4.778235,-2.464000,-9.896660,-0.148163,7.873120,9.587946,2.423928,-9.904582,0.706087,0.767117,7.879422,7.145522,1.671834,0.507679,3.793578,0.262504,8.427862,0.267520], dtype = "float32")#candidate|561|(528,)|const|float32
call_560 = relay.TupleGetItem(func_458_call(relay.reshape(call_558.astype('float32'), [11, 1, 3]), relay.reshape(const_561.astype('float32'), [11, 16, 3]), ), 0)
call_562 = relay.TupleGetItem(func_462_call(relay.reshape(call_558.astype('float32'), [11, 1, 3]), relay.reshape(const_561.astype('float32'), [11, 16, 3]), ), 0)
output = relay.Tuple([call_558,call_560,const_561,])
output2 = relay.Tuple([call_559,call_562,const_561,])
func_602 = relay.Function([], output)
mod['func_602'] = func_602
mod = relay.transform.InferType()(mod)
mutated_mod['func_602'] = func_602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_602_call = mutated_mod.get_global_var('func_602')
call_603 = func_602_call()
output = call_603
func_604 = relay.Function([], output)
mutated_mod['func_604'] = func_604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
call_619 = relay.TupleGetItem(func_602_call(), 2)
call_620 = relay.TupleGetItem(func_604_call(), 2)
output = call_619
output2 = call_620
func_669 = relay.Function([], output)
mod['func_669'] = func_669
mod = relay.transform.InferType()(mod)
output = func_669()
func_670 = relay.Function([], output)
mutated_mod['func_670'] = func_670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_669_call = mod.get_global_var('func_669')
func_670_call = mutated_mod.get_global_var('func_670')
call_710 = func_669_call()
call_711 = func_669_call()
output = call_710
output2 = call_711
func_752 = relay.Function([], output)
mod['func_752'] = func_752
mod = relay.transform.InferType()(mod)
mutated_mod['func_752'] = func_752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_752_call = mutated_mod.get_global_var('func_752')
call_753 = func_752_call()
output = call_753
func_754 = relay.Function([], output)
mutated_mod['func_754'] = func_754
mutated_mod = relay.transform.InferType()(mutated_mod)
var_768 = relay.var("var_768", dtype = "uint8", shape = (5, 13, 5))#candidate|768|(5, 13, 5)|var|uint8
var_769 = relay.var("var_769", dtype = "uint8", shape = (5, 13, 5))#candidate|769|(5, 13, 5)|var|uint8
bop_770 = relay.less(var_768.astype('bool'), relay.reshape(var_769.astype('bool'), relay.shape_of(var_768))) # shape=(5, 13, 5)
output = relay.Tuple([bop_770,])
output2 = relay.Tuple([bop_770,])
func_774 = relay.Function([var_768,var_769,], output)
mod['func_774'] = func_774
mod = relay.transform.InferType()(mod)
mutated_mod['func_774'] = func_774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_774_call = mutated_mod.get_global_var('func_774')
var_776 = relay.var("var_776", dtype = "uint8", shape = (5, 13, 5))#candidate|776|(5, 13, 5)|var|uint8
var_777 = relay.var("var_777", dtype = "uint8", shape = (5, 13, 5))#candidate|777|(5, 13, 5)|var|uint8
call_775 = func_774_call(var_776,var_777,)
output = call_775
func_778 = relay.Function([var_776,var_777,], output)
mutated_mod['func_778'] = func_778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mod.get_global_var('func_542')
func_544_call = mutated_mod.get_global_var('func_544')
call_780 = func_542_call()
call_781 = func_542_call()
output = relay.Tuple([call_780,])
output2 = relay.Tuple([call_781,])
func_782 = relay.Function([], output)
mod['func_782'] = func_782
mod = relay.transform.InferType()(mod)
mutated_mod['func_782'] = func_782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mutated_mod.get_global_var('func_782')
call_783 = func_782_call()
output = call_783
func_784 = relay.Function([], output)
mutated_mod['func_784'] = func_784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_803 = relay.TupleGetItem(func_782_call(), 0)
call_804 = relay.TupleGetItem(func_784_call(), 0)
var_819 = relay.var("var_819", dtype = "float64", shape = (33,))#candidate|819|(33,)|var|float64
bop_820 = relay.not_equal(call_803.astype('bool'), relay.reshape(var_819.astype('bool'), relay.shape_of(call_803))) # shape=(33,)
bop_823 = relay.not_equal(call_804.astype('bool'), relay.reshape(var_819.astype('bool'), relay.shape_of(call_804))) # shape=(33,)
output = bop_820
output2 = bop_823
func_824 = relay.Function([var_819,], output)
mod['func_824'] = func_824
mod = relay.transform.InferType()(mod)
var_825 = relay.var("var_825", dtype = "float64", shape = (33,))#candidate|825|(33,)|var|float64
output = func_824(var_825)
func_826 = relay.Function([var_825], output)
mutated_mod['func_826'] = func_826
mutated_mod = relay.transform.InferType()(mutated_mod)
var_879 = relay.var("var_879", dtype = "float32", shape = (10, 14, 12))#candidate|879|(10, 14, 12)|var|float32
uop_880 = relay.sigmoid(var_879.astype('float32')) # shape=(10, 14, 12)
uop_890 = relay.log2(uop_880.astype('float64')) # shape=(10, 14, 12)
output = relay.Tuple([uop_890,])
output2 = relay.Tuple([uop_890,])
func_898 = relay.Function([var_879,], output)
mod['func_898'] = func_898
mod = relay.transform.InferType()(mod)
mutated_mod['func_898'] = func_898
mutated_mod = relay.transform.InferType()(mutated_mod)
var_899 = relay.var("var_899", dtype = "float32", shape = (10, 14, 12))#candidate|899|(10, 14, 12)|var|float32
func_898_call = mutated_mod.get_global_var('func_898')
call_900 = func_898_call(var_899)
output = call_900
func_901 = relay.Function([var_899], output)
mutated_mod['func_901'] = func_901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_752_call = mod.get_global_var('func_752')
func_754_call = mutated_mod.get_global_var('func_754')
call_951 = func_752_call()
call_952 = func_752_call()
func_458_call = mod.get_global_var('func_458')
func_462_call = mutated_mod.get_global_var('func_462')
const_959 = relay.const([1.805684,-3.000468,7.245589,-1.023084,-5.178181,8.114058,0.879533,-7.931903,-7.087411,-5.500241,-9.118451,1.064276,-8.013909,5.745403,-1.223413,-3.607148,5.173540,6.552117,-6.655349,3.165766,-9.486240,5.136799,-0.072522,-9.459342,-1.201987,-1.794186,-8.825318,-6.941670,-9.861692,2.502585,-8.039432,0.589509,-6.829970], dtype = "float32")#candidate|959|(33,)|const|float32
call_958 = relay.TupleGetItem(func_458_call(relay.reshape(const_959.astype('float32'), [11, 1, 3]), relay.reshape(call_951.astype('float32'), [11, 16, 3]), ), 0)
call_960 = relay.TupleGetItem(func_462_call(relay.reshape(const_959.astype('float32'), [11, 1, 3]), relay.reshape(call_951.astype('float32'), [11, 16, 3]), ), 0)
output = relay.Tuple([call_951,call_958,const_959,])
output2 = relay.Tuple([call_952,call_960,const_959,])
func_970 = relay.Function([], output)
mod['func_970'] = func_970
mod = relay.transform.InferType()(mod)
mutated_mod['func_970'] = func_970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mutated_mod.get_global_var('func_970')
call_971 = func_970_call()
output = call_971
func_972 = relay.Function([], output)
mutated_mod['func_972'] = func_972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_1025 = relay.TupleGetItem(func_782_call(), 0)
call_1026 = relay.TupleGetItem(func_784_call(), 0)
uop_1039 = relay.rsqrt(call_1025.astype('float32')) # shape=(33,)
uop_1041 = relay.rsqrt(call_1026.astype('float32')) # shape=(33,)
uop_1042 = relay.log10(uop_1039.astype('float32')) # shape=(33,)
uop_1044 = relay.log10(uop_1041.astype('float32')) # shape=(33,)
uop_1048 = relay.sin(uop_1039.astype('float64')) # shape=(33,)
uop_1050 = relay.sin(uop_1041.astype('float64')) # shape=(33,)
output = relay.Tuple([uop_1042,uop_1048,])
output2 = relay.Tuple([uop_1044,uop_1050,])
func_1052 = relay.Function([], output)
mod['func_1052'] = func_1052
mod = relay.transform.InferType()(mod)
mutated_mod['func_1052'] = func_1052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1052_call = mutated_mod.get_global_var('func_1052')
call_1053 = func_1052_call()
output = call_1053
func_1054 = relay.Function([], output)
mutated_mod['func_1054'] = func_1054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
call_1066 = relay.TupleGetItem(func_602_call(), 2)
call_1067 = relay.TupleGetItem(func_604_call(), 2)
output = call_1066
output2 = call_1067
func_1074 = relay.Function([], output)
mod['func_1074'] = func_1074
mod = relay.transform.InferType()(mod)
output = func_1074()
func_1075 = relay.Function([], output)
mutated_mod['func_1075'] = func_1075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mod.get_global_var('func_542')
func_544_call = mutated_mod.get_global_var('func_544')
call_1081 = func_542_call()
call_1082 = func_542_call()
uop_1100 = relay.sigmoid(call_1081.astype('float64')) # shape=(33,)
uop_1102 = relay.sigmoid(call_1082.astype('float64')) # shape=(33,)
func_1052_call = mod.get_global_var('func_1052')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_1103 = relay.TupleGetItem(func_1052_call(), 0)
call_1104 = relay.TupleGetItem(func_1054_call(), 0)
func_774_call = mod.get_global_var('func_774')
func_778_call = mutated_mod.get_global_var('func_778')
var_1111 = relay.var("var_1111", dtype = "uint8", shape = (325,))#candidate|1111|(325,)|var|uint8
call_1110 = relay.TupleGetItem(func_774_call(relay.reshape(var_1111.astype('uint8'), [5, 13, 5]), relay.reshape(var_1111.astype('uint8'), [5, 13, 5]), ), 0)
call_1112 = relay.TupleGetItem(func_778_call(relay.reshape(var_1111.astype('uint8'), [5, 13, 5]), relay.reshape(var_1111.astype('uint8'), [5, 13, 5]), ), 0)
output = relay.Tuple([uop_1100,call_1103,call_1110,var_1111,])
output2 = relay.Tuple([uop_1102,call_1104,call_1112,var_1111,])
func_1113 = relay.Function([var_1111,], output)
mod['func_1113'] = func_1113
mod = relay.transform.InferType()(mod)
var_1114 = relay.var("var_1114", dtype = "uint8", shape = (325,))#candidate|1114|(325,)|var|uint8
output = func_1113(var_1114)
func_1115 = relay.Function([var_1114], output)
mutated_mod['func_1115'] = func_1115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_1117 = relay.TupleGetItem(func_970_call(), 1)
call_1118 = relay.TupleGetItem(func_972_call(), 1)
uop_1120 = relay.asinh(call_1117.astype('float32')) # shape=(11, 16, 3)
uop_1122 = relay.asinh(call_1118.astype('float32')) # shape=(11, 16, 3)
output = relay.Tuple([uop_1120,])
output2 = relay.Tuple([uop_1122,])
func_1132 = relay.Function([], output)
mod['func_1132'] = func_1132
mod = relay.transform.InferType()(mod)
mutated_mod['func_1132'] = func_1132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1132_call = mutated_mod.get_global_var('func_1132')
call_1133 = func_1132_call()
output = call_1133
func_1134 = relay.Function([], output)
mutated_mod['func_1134'] = func_1134
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1147 = relay.var("var_1147", dtype = "float64", shape = (16, 15, 11))#candidate|1147|(16, 15, 11)|var|float64
uop_1148 = relay.sin(var_1147.astype('float64')) # shape=(16, 15, 11)
func_824_call = mod.get_global_var('func_824')
func_826_call = mutated_mod.get_global_var('func_826')
const_1153 = relay.const([[-1.326419,4.255083,-6.923674,-4.175177,-2.530595,5.455121,3.400127,2.703358,-8.711927,4.715901,1.154307,9.774090,5.277547,1.956056,8.895372,1.512165,-4.960659,-0.793359,-5.825284,-8.397191,-3.603177,-3.390690,-0.071284,-8.428403,7.230108,1.719122,-0.522597,-9.363272,-7.210395,0.340565,5.553840,9.755601,9.084647]], dtype = "float64")#candidate|1153|(1, 33)|const|float64
call_1152 = func_824_call(relay.reshape(const_1153.astype('float64'), [33,]))
call_1154 = func_824_call(relay.reshape(const_1153.astype('float64'), [33,]))
output = relay.Tuple([uop_1148,call_1152,const_1153,])
output2 = relay.Tuple([uop_1148,call_1154,const_1153,])
func_1157 = relay.Function([var_1147,], output)
mod['func_1157'] = func_1157
mod = relay.transform.InferType()(mod)
mutated_mod['func_1157'] = func_1157
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1158 = relay.var("var_1158", dtype = "float64", shape = (16, 15, 11))#candidate|1158|(16, 15, 11)|var|float64
func_1157_call = mutated_mod.get_global_var('func_1157')
call_1159 = func_1157_call(var_1158)
output = call_1159
func_1160 = relay.Function([var_1158], output)
mutated_mod['func_1160'] = func_1160
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1180 = relay.var("var_1180", dtype = "float32", shape = (3, 10, 6))#candidate|1180|(3, 10, 6)|var|float32
uop_1181 = relay.acos(var_1180.astype('float32')) # shape=(3, 10, 6)
output = uop_1181
output2 = uop_1181
func_1206 = relay.Function([var_1180,], output)
mod['func_1206'] = func_1206
mod = relay.transform.InferType()(mod)
var_1207 = relay.var("var_1207", dtype = "float32", shape = (3, 10, 6))#candidate|1207|(3, 10, 6)|var|float32
output = func_1206(var_1207)
func_1208 = relay.Function([var_1207], output)
mutated_mod['func_1208'] = func_1208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_1217 = relay.TupleGetItem(func_970_call(), 1)
call_1218 = relay.TupleGetItem(func_972_call(), 1)
var_1219 = relay.var("var_1219", dtype = "float32", shape = (11, 16, 3))#candidate|1219|(11, 16, 3)|var|float32
bop_1220 = relay.maximum(call_1217.astype('float64'), relay.reshape(var_1219.astype('float64'), relay.shape_of(call_1217))) # shape=(11, 16, 3)
bop_1223 = relay.maximum(call_1218.astype('float64'), relay.reshape(var_1219.astype('float64'), relay.shape_of(call_1218))) # shape=(11, 16, 3)
func_669_call = mod.get_global_var('func_669')
func_670_call = mutated_mod.get_global_var('func_670')
call_1229 = func_669_call()
call_1230 = func_669_call()
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
call_1235 = relay.TupleGetItem(func_602_call(), 2)
call_1236 = relay.TupleGetItem(func_604_call(), 2)
output = relay.Tuple([bop_1220,call_1229,call_1235,])
output2 = relay.Tuple([bop_1223,call_1230,call_1236,])
func_1237 = relay.Function([var_1219,], output)
mod['func_1237'] = func_1237
mod = relay.transform.InferType()(mod)
var_1238 = relay.var("var_1238", dtype = "float32", shape = (11, 16, 3))#candidate|1238|(11, 16, 3)|var|float32
output = func_1237(var_1238)
func_1239 = relay.Function([var_1238], output)
mutated_mod['func_1239'] = func_1239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_752_call = mod.get_global_var('func_752')
func_754_call = mutated_mod.get_global_var('func_754')
call_1268 = func_752_call()
call_1269 = func_752_call()
output = relay.Tuple([call_1268,])
output2 = relay.Tuple([call_1269,])
func_1270 = relay.Function([], output)
mod['func_1270'] = func_1270
mod = relay.transform.InferType()(mod)
mutated_mod['func_1270'] = func_1270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1270_call = mutated_mod.get_global_var('func_1270')
call_1271 = func_1270_call()
output = call_1271
func_1272 = relay.Function([], output)
mutated_mod['func_1272'] = func_1272
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1308 = relay.var("var_1308", dtype = "uint64", shape = (7, 7, 9))#candidate|1308|(7, 7, 9)|var|uint64
var_1309 = relay.var("var_1309", dtype = "uint64", shape = (7, 7, 9))#candidate|1309|(7, 7, 9)|var|uint64
bop_1310 = relay.bitwise_and(var_1308.astype('uint64'), relay.reshape(var_1309.astype('uint64'), relay.shape_of(var_1308))) # shape=(7, 7, 9)
func_898_call = mod.get_global_var('func_898')
func_901_call = mutated_mod.get_global_var('func_901')
var_1327 = relay.var("var_1327", dtype = "float32", shape = (840, 2))#candidate|1327|(840, 2)|var|float32
call_1326 = relay.TupleGetItem(func_898_call(relay.reshape(var_1327.astype('float32'), [10, 14, 12])), 0)
call_1328 = relay.TupleGetItem(func_901_call(relay.reshape(var_1327.astype('float32'), [10, 14, 12])), 0)
output = relay.Tuple([bop_1310,call_1326,var_1327,])
output2 = relay.Tuple([bop_1310,call_1328,var_1327,])
func_1330 = relay.Function([var_1308,var_1309,var_1327,], output)
mod['func_1330'] = func_1330
mod = relay.transform.InferType()(mod)
var_1331 = relay.var("var_1331", dtype = "uint64", shape = (7, 7, 9))#candidate|1331|(7, 7, 9)|var|uint64
var_1332 = relay.var("var_1332", dtype = "uint64", shape = (7, 7, 9))#candidate|1332|(7, 7, 9)|var|uint64
var_1333 = relay.var("var_1333", dtype = "float32", shape = (840, 2))#candidate|1333|(840, 2)|var|float32
output = func_1330(var_1331,var_1332,var_1333,)
func_1334 = relay.Function([var_1331,var_1332,var_1333,], output)
mutated_mod['func_1334'] = func_1334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_752_call = mod.get_global_var('func_752')
func_754_call = mutated_mod.get_global_var('func_754')
call_1356 = func_752_call()
call_1357 = func_752_call()
output = call_1356
output2 = call_1357
func_1359 = relay.Function([], output)
mod['func_1359'] = func_1359
mod = relay.transform.InferType()(mod)
output = func_1359()
func_1360 = relay.Function([], output)
mutated_mod['func_1360'] = func_1360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_1411 = relay.TupleGetItem(func_970_call(), 0)
call_1412 = relay.TupleGetItem(func_972_call(), 0)
output = relay.Tuple([call_1411,])
output2 = relay.Tuple([call_1412,])
func_1419 = relay.Function([], output)
mod['func_1419'] = func_1419
mod = relay.transform.InferType()(mod)
output = func_1419()
func_1420 = relay.Function([], output)
mutated_mod['func_1420'] = func_1420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1359_call = mod.get_global_var('func_1359')
func_1360_call = mutated_mod.get_global_var('func_1360')
call_1427 = func_1359_call()
call_1428 = func_1359_call()
func_1419_call = mod.get_global_var('func_1419')
func_1420_call = mutated_mod.get_global_var('func_1420')
call_1443 = relay.TupleGetItem(func_1419_call(), 0)
call_1444 = relay.TupleGetItem(func_1420_call(), 0)
func_1330_call = mod.get_global_var('func_1330')
func_1334_call = mutated_mod.get_global_var('func_1334')
const_1448 = relay.const([[1,-7,-1,3,8,-6,-8,7,-3,-1,8,1,-2,-10,2,-2,-7,9,9,8,4,4,-4,-4,-7,-3,8,4,6,7,-3,10,8,-8,3,-4,9,-9,-10,-1,5,-4,8,4,-10,-4,2,3,-3,-8,-8,-1,10,-1,10,-7,-5,-9,7,-7,-6,1,2],[9,4,2,-10,8,-3,-2,10,10,-2,-8,-6,-7,-5,2,2,-5,-1,-10,-9,2,-9,7,-4,5,-7,5,8,-8,10,-10,-3,1,-1,-4,-9,-4,-9,-8,-7,-8,-5,-10,5,-6,7,-9,1,4,-3,2,-3,10,7,-4,2,1,-5,2,8,-8,4,-5],[9,6,-6,-4,7,10,6,8,-7,7,9,-3,7,-4,-9,7,8,10,6,-2,9,-6,-7,-3,7,-8,9,-5,-3,9,-6,9,-10,8,4,8,4,-6,-2,7,9,6,-7,4,8,3,10,9,-3,-5,-9,-8,-6,-5,-5,8,10,-2,4,8,-1,-7,-4],[-10,-3,4,7,4,8,4,4,9,-5,-2,9,1,2,1,-6,1,-4,-1,8,-6,7,-4,-9,4,4,-3,5,-2,-3,2,-2,9,9,8,-7,6,2,4,10,7,5,8,-5,-8,-3,-8,-3,-2,-8,10,5,-1,5,-2,5,-1,-3,-2,-9,-9,-9,7],[5,-4,2,-10,9,5,9,1,9,6,-2,10,-1,6,-5,1,4,5,-9,-2,6,-6,-5,3,-10,-7,9,6,6,9,-6,-3,8,-4,-1,-9,6,-6,-2,-6,-9,-7,-10,-8,6,8,-10,2,-9,6,5,-8,9,-1,-2,3,1,10,4,10,7,-2,8],[-4,-2,-6,-4,-7,10,-5,-8,6,10,-1,-3,-6,8,7,4,5,-2,3,7,10,-8,2,5,5,1,2,6,6,6,2,-3,-5,9,-2,8,4,6,3,-3,7,-4,-9,6,6,7,3,-6,6,6,2,9,-1,-3,6,-1,-9,1,9,1,9,-5,9],[-1,-9,-4,-1,8,-6,6,-6,-5,4,-2,5,-10,3,-7,9,9,4,-8,6,9,-8,4,-2,10,8,10,-7,-8,-6,-5,2,2,9,3,7,-7,-6,2,3,5,3,-5,-6,1,7,-6,1,-6,-7,6,-2,-2,8,-8,3,2,-3,-8,-9,2,6,4]], dtype = "uint64")#candidate|1448|(7, 63)|const|uint64
var_1449 = relay.var("var_1449", dtype = "float32", shape = (1, 1680))#candidate|1449|(1, 1680)|var|float32
call_1447 = relay.TupleGetItem(func_1330_call(relay.reshape(const_1448.astype('uint64'), [7, 7, 9]), relay.reshape(const_1448.astype('uint64'), [7, 7, 9]), relay.reshape(var_1449.astype('float32'), [840, 2]), ), 0)
call_1450 = relay.TupleGetItem(func_1334_call(relay.reshape(const_1448.astype('uint64'), [7, 7, 9]), relay.reshape(const_1448.astype('uint64'), [7, 7, 9]), relay.reshape(var_1449.astype('float32'), [840, 2]), ), 0)
func_669_call = mod.get_global_var('func_669')
func_670_call = mutated_mod.get_global_var('func_670')
call_1451 = func_669_call()
call_1452 = func_669_call()
var_1461 = relay.var("var_1461", dtype = "float32", shape = (6, 1680))#candidate|1461|(6, 1680)|var|float32
bop_1462 = relay.divide(var_1449.astype('float32'), var_1461.astype('float32')) # shape=(6, 1680)
func_1359_call = mod.get_global_var('func_1359')
func_1360_call = mutated_mod.get_global_var('func_1360')
call_1465 = func_1359_call()
call_1466 = func_1359_call()
func_1419_call = mod.get_global_var('func_1419')
func_1420_call = mutated_mod.get_global_var('func_1420')
call_1471 = relay.TupleGetItem(func_1419_call(), 0)
call_1472 = relay.TupleGetItem(func_1420_call(), 0)
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
call_1480 = relay.TupleGetItem(func_602_call(), 1)
call_1481 = relay.TupleGetItem(func_604_call(), 1)
output = relay.Tuple([call_1427,call_1443,call_1447,const_1448,call_1451,bop_1462,call_1465,call_1471,call_1480,])
output2 = relay.Tuple([call_1428,call_1444,call_1450,const_1448,call_1452,bop_1462,call_1466,call_1472,call_1481,])
func_1486 = relay.Function([var_1449,var_1461,], output)
mod['func_1486'] = func_1486
mod = relay.transform.InferType()(mod)
var_1487 = relay.var("var_1487", dtype = "float32", shape = (1, 1680))#candidate|1487|(1, 1680)|var|float32
var_1488 = relay.var("var_1488", dtype = "float32", shape = (6, 1680))#candidate|1488|(6, 1680)|var|float32
output = func_1486(var_1487,var_1488,)
func_1489 = relay.Function([var_1487,var_1488,], output)
mutated_mod['func_1489'] = func_1489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1132_call = mod.get_global_var('func_1132')
func_1134_call = mutated_mod.get_global_var('func_1134')
call_1530 = relay.TupleGetItem(func_1132_call(), 0)
call_1531 = relay.TupleGetItem(func_1134_call(), 0)
func_898_call = mod.get_global_var('func_898')
func_901_call = mutated_mod.get_global_var('func_901')
const_1539 = relay.const([3.564250,-7.063779,-4.746469,-6.004997,-4.661857,-9.956688,-4.236964,5.751749,5.737809,2.165587,4.119223,0.153597,8.687726,6.351606,-4.281224,8.266068,-4.298365,-9.918009,1.027760,-5.342847,-4.521438,7.254666,3.795666,8.073463,-8.949708,2.636266,4.144958,2.592002,-7.110039,-3.922947,8.068032,-4.585213,7.593071,-9.665534,9.180263,-8.923345,4.255644,7.428040,-4.349719,-8.685409,0.027738,1.236980,-9.633379,3.349003,2.507351,9.038933,-5.055194,-2.654883,1.689436,-3.316769,5.117530,-0.232120,-7.231778,6.832154,-4.676715,4.128184,4.760768,7.053541,6.370734,3.597856,-7.423453,7.084215,-9.979609,-3.690139,8.418502,4.888323,-2.894583,1.478583,0.816197,1.885853,-2.542187,5.284703,8.799895,-2.721077,-5.622278,4.278624,-7.108088,9.845223,8.148893,-0.975434,-2.343646,0.635420,5.374423,2.835987,-8.710751,7.869749,4.119956,-6.668498,6.540916,-8.317372,-8.846757,-9.903168,-4.530190,-8.505460,8.386891,-8.470087,-4.329644,-8.120192,7.460502,-2.042549,6.505474,-1.722827,-8.133819,8.572101,0.211384,6.989617,-4.374500,3.346890,2.356821,-4.148005,-0.233577,-9.118904,-4.312129,8.183195,-6.116876,1.189598,2.262355,4.543900,4.371936,0.843724,-5.491723,-1.560533,-7.254468,6.721019,6.260517,-6.850057,9.088882,-1.244242,-2.114818,7.539715,6.431793,-8.657108,-2.535500,7.659062,-6.293707,1.817620,4.191477,4.508999,9.075601,-9.602609,-2.329309,-2.584830,8.137407,-8.634736,-9.599652,7.008298,-8.444012,-5.368127,0.208808,-9.078941,-5.265837,-1.791681,-4.997514,7.212488,-2.796239,-2.366211,8.324541,-8.537733,-6.351232,-2.285799,-5.918686,-5.599290,8.312336,-0.879577,-8.752092,-9.020986,-1.611545,2.291220,6.172307,-0.454929,-0.163137,-1.589327,0.226067,-1.358982,5.229147,7.612190,-7.247179,7.421937,-6.466040,-1.076602,-5.137725,-8.225898,7.180690,1.580562,-3.001019,8.196101,4.644898,-3.119270,-4.002535,-9.913029,5.628633,-1.148111,8.150325,7.055998,1.517371,8.918226,5.790826,-1.337095,6.515852,6.239449,1.174858,-2.967583,-7.096738,6.581087,2.989012,9.321959,6.080346,1.565521,9.568659,8.244368,-3.590349,-8.833441,-6.308488,7.398548,0.397909,0.143215,8.731108,8.490674,0.286281,-0.080412,-5.295124,6.800952,4.093543,-2.280313,-0.890998,7.764673,-6.586252,-0.929340,-7.095573,-1.085940,-6.651600,-7.466396,4.326218,2.369764,0.211301,-5.651092,3.890682,0.881066,-8.864729,9.981073,0.369035,7.659453,5.058144,-8.673819,4.890442,1.927499,6.475710,7.041743,6.893021,5.490344,4.929587,-8.017480,6.862005,0.286102,1.688017,-5.690866,-3.441876,7.552040,1.003861,8.574379,-0.807981,-1.177318,8.509661,2.212882,5.470244,3.017869,-1.888032,0.062816,0.856530,5.609167,-1.917146,-7.828471,9.412650,-9.715205,0.920180,-4.059855,-4.583996,4.351783,-0.030519,-7.706267,2.946621,-7.597394,4.772896,-1.452074,7.855199,6.212089,5.435582,-8.876122,7.878216,-2.924531,-2.234427,8.499445,3.471896,-6.094483,8.954236,5.959713,-2.970995,-6.016333,-2.249004,7.875223,-2.508837,4.071789,-5.305018,-7.312696,-9.233069,-5.653936,2.996434,4.169445,7.788687,1.425572,-6.752549,4.244978,-9.198094,-5.098416,-4.323325,-3.199788,-2.610165,8.699681,5.134372,7.351241,-9.487214,7.989197,8.142411,-0.904562,-5.818640,1.703280,3.968336,-9.781974,-2.744372,-4.750745,-5.104990,2.667026,-8.636817,4.718018,-6.798819,2.207959,-1.025581,1.166865,4.506183,-8.408479,1.938225,-7.334908,0.824283,-1.391365,0.208726,-9.335979,-0.539162,-2.892745,-6.247259,-5.064446,-1.279660,3.954797,-6.392467,-1.680646,4.856913,-9.423590,-1.168642,0.430031,6.138338,3.632815,-0.615181,-6.320878,0.492558,2.342726,-8.007006,1.987732,9.672335,4.916985,4.880346,4.875168,4.466243,8.327642,-1.982382,1.712748,-6.784558,-9.411119,-1.016899,6.246630,5.323325,-6.308754,1.838069,3.395982,-3.426715,-4.875133,-3.094134,-3.281597,6.232649,-7.045272,-1.444963,9.039344,-1.267691,4.028102,-4.569732,7.716573,7.972474,1.580159,2.980233,2.833281,-7.107503,6.489707,1.391925,-9.606370,9.312180,-7.339468,-3.785965,-2.578999,5.186068,7.865440,8.474834,-7.858716,-3.553840,7.193803,-8.917925,-2.668981,-9.583471,3.615065,9.197127,4.341408,-6.854310,0.711536,1.665138,-6.534552,4.095701,1.677143,-8.547456,-5.216586,6.009295,-4.033809,-5.217139,-4.495204,-7.874272,0.312484,7.606769,-4.980811,-7.944187,-9.180328,6.737869,7.040597,2.429190,5.369844,-2.902972,-1.175953,5.714658,0.106222,8.955700,5.848009,1.291720,-0.669068,0.353502,1.957893,-3.525823,3.537905,-9.790941,-6.013672,3.558666,7.204999,7.177489,-5.509409,-6.294706,3.342486,1.007548,3.117801,8.352961,-0.009453,-8.542871,-3.760281,9.811519,-7.459595,-1.138758,6.211320,7.648339,7.157106,2.195001,0.390940,6.113262,7.770207,9.468038,-1.366348,-1.793111,7.090583,-8.380448,6.013082,-2.905286,9.491086,3.741484,-5.374186,9.756009,5.051678,7.178904,-7.872789,6.668811,-9.396636,-1.860075,3.616325,2.176774,5.609358,0.180269,7.543056,-1.260383,-0.833524,-2.250001,-1.279870,0.024505,-3.258777,7.816575,4.619037,-2.617308,9.274679,-7.056243,-4.203181,-2.739652,6.136211,-4.132296,6.488517,0.836001,-8.676097,-2.677196,0.084537,2.417686,1.093868,-8.269313,2.445362,-0.310224,1.122488,-9.374823,-3.749877,2.390696,-2.417649,-1.620276,8.849469,4.268984,7.167329,-5.728973,7.071430,-5.370190,-4.386087,-1.721579,-9.919143,6.611058,6.119619,2.317883,-7.432184,-0.446654,-0.422848,-7.598030,-6.967586,-1.260767,1.850821,4.333291,-3.295658,1.873809,-1.762753,-8.716500,-8.663946,4.346866,8.139529,4.392887,3.283593,-8.688639,3.064113,5.632570,8.611523,5.510663,7.766598,4.989040,9.679689,-1.094107,-4.181063,-9.875658,-6.315027,2.309623,-2.417711,2.793734,-1.616915,6.062609,-9.592357,5.531074,-6.095956,5.319712,4.725957,4.677094,1.221410,5.131959,0.722429,5.756034,9.188294,8.161284,7.958579,7.725093,5.589328,2.036956,-7.971445,0.551316,-9.421035,-6.264198,7.713460,-6.595950,3.120801,1.376761,9.745865,7.354196,4.228933,-1.560087,7.296030,-4.159966,-6.847396,3.386605,-1.889750,-9.968795,1.280830,3.424564,-1.201726,1.849010,1.619487,-1.355368,8.744458,3.156374,3.702400,-3.293000,7.780089,9.116897,-1.733114,-0.262361,4.221077,7.105055,1.610720,9.405255,-8.268726,-9.413441,8.126198,-9.243622,-3.813212,6.751744,1.040845,-9.915209,-7.721691,9.940304,-9.986272,-0.080275,-1.547970,-4.134558,-3.662854,3.675086,1.313289,-4.204062,5.834877,9.657171,-7.258543,4.073960,-9.615525,-8.381503,1.394612,-6.910957,-9.175826,6.504023,-9.100855,-3.098637,3.137181,-3.819014,1.406652,-9.410080,6.424384,-9.072813,-2.862102,-0.081152,-8.229040,-8.615157,-8.924369,6.304030,1.285122,2.797102,3.186406,-4.392792,4.668541,0.826531,5.223653,1.045823,8.673442,-8.124582,4.615219,9.184347,0.764719,6.163963,-9.899206,-9.834033,9.672951,6.907962,-1.171207,-3.122513,-3.950915,-1.032123,7.946687,5.467765,-9.700219,-7.425531,-8.080718,1.953760,9.918369,5.871655,0.530801,4.632096,1.177180,9.374018,-8.886522,2.039416,1.182959,-1.886114,-7.244110,-6.855702,2.747661,-4.902203,-2.299801,-5.451778,7.020980,8.073683,4.651750,6.336112,1.087367,-2.373023,-0.956314,0.229391,-7.884015,-1.690379,1.006268,0.226492,-6.681421,-4.078851,2.098653,-0.719270,-8.596323,4.458663,5.689902,-2.053744,-7.196154,-8.585940,-3.597442,-9.266858,-1.166646,0.428092,4.983612,-5.119402,3.858545,-3.454047,1.262302,9.455606,-5.337143,-4.479125,7.608702,3.609292,3.872889,0.881951,1.688054,-5.056040,-8.767333,6.262151,-0.364236,2.709890,-0.665131,-7.972600,1.428461,7.280065,4.328243,0.675733,-9.340686,-4.780981,-9.059866,2.860593,6.699428,0.328567,-4.603637,-6.672641,9.414573,-9.428271,0.216932,9.394827,-4.276594,8.173846,-1.654825,-4.215042,3.934532,4.714983,-3.423930,0.743253,-2.488258,-9.908336,2.097791,-5.871867,-3.334340,-4.894681,0.300503,-2.799689,-5.878495,3.650158,-4.880321,7.323049,-3.614141,-5.073570,4.778787,6.420075,-8.557682,-1.350798,-4.917432,-4.947436,7.864788,-3.981119,0.539278,-0.248133,-7.424073,-4.135492,-2.626063,-6.697217,-2.570338,4.712869,-1.559459,-4.525377,-9.068757,-4.526046,4.827547,-8.055595,2.261044,6.507819,9.562695,-6.902702,-0.814634,9.116721,-4.229846,3.923940,-5.044430,7.952787,8.966642,7.825390,-3.695318,-8.168790,1.102613,1.604067,-0.689221,5.646126,-4.283729,7.932305,-5.897698,1.478599,8.493746,-5.502754,-0.695575,-8.325727,6.850481,8.955045,-6.987106,0.360226,-7.007605,-4.552924,6.821947,1.426583,-8.056779,-2.409697,0.613674,2.919032,7.931027,-1.825406,3.080846,6.864374,-8.737259,5.773855,9.368993,-3.199548,7.945368,-1.244862,-2.020388,-1.663645,-6.255490,-3.858682,3.661259,-3.908302,4.962716,-5.156067,-9.145415,6.248573,-2.897676,2.855411,2.411244,-1.313662,-8.267847,3.309562,-3.829869,4.134094,3.919308,-6.878543,-2.802264,8.924453,5.317046,-4.102042,3.994174,-4.253456,-3.431952,8.547506,-8.520418,-3.772181,-6.530581,8.231193,-6.439154,-9.905577,-4.355358,-4.507992,5.511513,-4.683016,0.521330,-7.258927,-7.333891,-6.743557,-8.527810,-3.652071,9.893980,-7.109280,1.272208,-2.587849,-7.515752,0.524991,5.219419,9.661153,5.042642,7.902885,5.271280,7.894514,5.734597,-1.330517,-6.379240,-5.350863,-6.051338,0.814795,-5.467020,1.692576,-3.943778,-4.046256,-3.362027,8.330854,1.703632,-0.387222,-6.675552,5.404638,3.448090,-9.819125,-3.844984,-3.835279,4.336998,-5.088662,5.232791,-4.560301,-3.677794,-6.005325,5.916385,-5.157325,-0.570873,2.769322,0.389551,-9.567253,-2.949951,-0.934978,7.017073,0.087623,-6.115412,8.665468,1.540064,-9.871114,-7.983757,-7.778847,-9.966929,-1.745976,4.483015,2.789698,-3.104393,-3.888937,-2.401513,-3.976964,0.521802,-6.337471,7.018690,8.467047,-3.078519,9.653317,-4.956369,-5.670084,-3.389801,-7.688569,-7.459044,-4.176955,5.202255,7.437329,7.886301,-6.909798,-3.442816,8.649045,-2.446894,-5.985507,-7.731789,0.833166,-4.733901,2.776485,-5.723053,-1.350833,2.187779,-4.585318,0.307659,9.842870,0.468346,8.562025,-2.259505,3.938899,-8.100725,2.009761,5.350195,5.287019,-2.681168,0.795660,-9.904548,9.399866,-9.523523,4.448289,-8.538472,4.212090,-2.005146,9.704336,0.224323,7.766334,-1.712398,-1.706373,8.975551,1.358292,-7.113790,-7.955537,0.325690,-7.816227,8.671214,0.963127,-7.409803,1.230852,-0.567755,-6.606973,-3.927252,6.015587,-4.189986,-0.872525,1.089193,-8.779055,-7.557831,3.430097,-0.939246,-2.518471,8.047974,8.101042,-5.454673,-6.478149,1.807393,-7.720804,-3.494512,4.272089,0.641191,-0.894680,5.878923,-8.002897,1.542489,6.907147,6.062155,-1.856243,-5.944001,2.169485,-7.988803,0.371179,-6.736486,0.279631,9.553134,2.878684,6.595623,3.722976,-5.647019,-1.770179,2.756774,-8.087939,8.920171,0.991293,-0.715938,-0.951555,-0.335153,6.336822,6.526941,4.163407,3.990657,3.557845,-1.853778,8.556038,-1.693465,3.664740,-5.159625,0.848670,-4.452437,7.352011,0.899443,1.294064,2.352080,-9.389080,-1.286420,9.143793,-4.571479,-8.406572,6.900952,-7.709199,6.510583,-2.217122,2.609057,-9.558223,-4.822330,-6.589846,2.396341,-6.916972,-7.097001,-2.646289,-1.549760,-3.300169,-0.527755,-5.103669,3.171027,-8.682545,-5.701838,-5.677565,-5.361312,2.049909,-8.788253,-3.873109,1.906165,-5.307048,6.392396,-4.511280,-9.454892,-2.703303,5.810547,-7.854845,6.682223,-0.298715,0.755554,1.964594,9.379628,9.032171,7.919614,6.458799,-3.140882,-3.526566,-9.776083,4.473877,-9.925385,-5.528867,-9.247629,-2.248610,5.639818,9.760123,3.021460,-6.645512,1.390167,-4.458563,0.192493,-3.056319,1.077341,2.400103,7.202937,-9.295026,-8.792229,-9.702997,9.520103,9.812427,3.564338,-6.454299,2.202112,9.863430,-3.412553,8.869858,9.599667,9.653266,5.055027,3.771309,5.894914,-4.434628,-4.835003,4.746776,1.387198,-4.444911,5.723972,1.436792,7.223397,-4.946169,-8.958603,6.131833,5.317878,-6.706408,8.204646,9.154481,3.458399,-9.520731,-0.003683,5.434785,-8.237297,-3.360886,-8.781959,3.851259,-6.600513,7.447900,6.661355,0.678441,9.709544,9.554154,5.332267,-0.914489,-0.962105,-7.537372,-9.334349,-4.619621,1.471383,-6.953038,-7.225150,6.420299,6.474953,9.036292,7.555372,9.947598,-6.880052,6.626170,-6.726162,-2.081824,-4.272328,8.293045,7.679355,-0.602459,7.607100,-8.471501,-8.945369,-0.074377,0.065638,-3.621319,-9.405113,9.740806,3.504898,-3.317300,-8.792902,-8.034769,2.361918,2.859821,-0.703362,4.923711,6.355765,6.636267,6.381194,1.764864,-4.500394,3.898900,-3.651264,5.946738,7.998093,9.559842,9.498352,1.797873,7.510413,1.900069,-0.172937,6.131507,-0.136192,6.656422,8.963850,-0.524553,-7.876641,-4.358123,6.480066,-5.586740,-8.840549,-4.435979,-4.853695,-2.986170,2.115926,7.102400,9.336133,3.424628,5.166603,5.555083,0.062866,-5.088300,-8.631952,-6.430849,3.353291,-3.184674,-9.653827,1.549535,-1.871691,5.848848,1.357225,3.770195,0.101615,-8.412649,0.920454,8.876369,-8.471344,3.787799,9.413953,-9.970708,-7.929495,-1.336308,5.192299,8.301036,7.131767,8.672369,9.925359,6.285058,7.516714,-4.789326,-9.135792,-6.794625,7.160413,4.409612,8.773021,9.509405,-8.466602,0.168488,1.202123,-9.081780,8.911374,4.574036,-1.607422,3.101733,3.030575,5.502502,-4.709625,-5.118446,2.365809,-4.469975,2.978104,-0.926598,0.719408,3.319717,7.049523,1.236788,-7.130504,2.146164,-9.508895,-2.808528,-7.775436,7.350381,0.670118,1.517821,9.432123,-7.276604,3.081636,-0.262326,-8.052186,-5.809965,9.187205,-2.404321,-1.320142,1.667204,-6.709117,-7.974157,7.032477,5.003286,2.198374,2.825055,-6.216449,4.434049,-2.993967,-1.671813,-7.683735,-4.872433,3.366716,7.659108,8.575673,-6.059991,-0.423430,-1.490724,-3.477740,3.564697,-5.088699,-4.837147,-4.264950,5.778032,2.919716,1.595401,-7.957585,-6.074227,-2.254568,3.231220,-6.717953,6.432361,5.953398,-5.489872,-1.976480,7.316159,-9.953660,4.702437,-8.504339,9.569998,6.726343,7.829031,5.781694,9.307755,0.456072,9.192400,-3.943457,-4.720211,-6.239393,8.305516,-8.696221,-2.853485,-7.028567,7.010444,-5.179510,-5.377373,6.357289,9.122684,5.287233,-9.744930,5.030251,-0.022002,4.385218,5.132719,3.688956,-0.033818,-6.467594,-6.249590,-5.870059,2.127337,8.403665,-8.900876,1.898034,0.523700,-1.962009,0.545317,4.634640,6.150292,-4.985167,-4.139721,7.075857,-9.037809,2.253450,-2.096174,-7.795060,-7.840659,-0.562543,7.167345,-2.760407,-1.559484,-1.244769,4.795046,-3.101123,-2.133024,4.407695,-5.598774,3.363618,-4.907755,-3.424753,7.527461,-0.445831,-0.156596,-9.735371,-7.176794,-9.278835,-9.342636,-5.411050,-8.256745,-7.101758,-9.139232,7.037129,9.782198,8.560353,-3.059527,-5.813596,-4.956657,9.649151,6.410148,-5.860018,5.273613,9.167776,-8.707204,1.131433,-9.314603,0.305047,4.497735,0.852938,-2.577003,2.586762,-2.335999,-1.308632,-3.450470,5.490862,4.036290,-6.741407,-4.238574,-3.208310,6.070264,8.460156,-3.643529,-3.801383,-9.238897,-0.674428,-8.699073,1.932991,2.776741,-9.184114,1.737858,-0.796610,8.418910,6.437887,-3.642390,-4.313012,6.168131,4.755394,8.189619,-2.142739,3.923424,-0.499972,-6.078022,8.695341,1.825482,6.773302,0.502503,3.616021,-8.357376,8.771840,1.854701,5.720988,1.687694,-1.352200,-2.413544,-0.727078,7.277929,-8.781816,-0.890876,7.129741,8.167120,7.433509,-6.876410,4.354655,1.300253,4.010064,9.682656,-8.410323,4.135398,8.517705,2.408630,-9.367112,-5.377608,-6.306449,-5.807198,-3.376267,-6.091828,-7.071805,-0.729845,-1.702214,-4.824093,-1.211940,-0.489295,0.048276,0.658362,9.222720,-6.659658,2.667678,-6.093409,-8.412002,-7.882159,-7.527779,-2.043580,0.900215,0.259463,-6.826446,-9.763699,4.602332,4.051199,-5.004109,0.555329,4.851902,6.028477,-8.552675,-0.148904,-4.225738,6.874623,-7.777915,-4.792782,-7.361355,1.966219,8.141481,-6.100378,-3.542469,5.958958,-7.710331,-1.400199,6.909523,5.997295,-2.992128,-6.782548,-3.909843,6.741801,9.847696,-6.503352,7.020143,-2.846143,6.021006,2.277309,3.411735,7.772465,8.987156,3.787590,4.896049,-0.452160,9.071478,0.560458,-4.159781,-8.830918,-3.724649,-9.329512,-5.596528,-0.307028,0.216468,7.498733,0.205274,-2.057328,-4.612060,8.024825,-1.428152,0.824936,-6.363293,6.668489,-2.291304,-3.016405,5.387516,-8.002963,9.928078,8.757156,5.560206,6.609686,7.910519,0.533310,-2.720348,-2.594692,3.339714,-3.051410,-0.821302,-1.129665,7.274505,8.022391,1.639357,-0.617054,-1.673436,9.718422,-3.179442,-2.602206,2.391066,0.884232,-5.703052,-4.443282,-9.918674,2.135399,0.994849,6.526312,-0.039775,3.268387,-4.820049,4.688833,1.286576,-4.408540,4.516732,-5.561839,3.380311,-8.985344,6.521820,0.032525,3.818507,-8.496948,-5.152972,5.927509,-4.787649,2.594124,-0.522166,6.112592,1.734356,2.779443,8.231363,9.714586,-3.359154], dtype = "float32")#candidate|1539|(1680,)|const|float32
call_1538 = relay.TupleGetItem(func_898_call(relay.reshape(const_1539.astype('float32'), [10, 14, 12])), 0)
call_1540 = relay.TupleGetItem(func_901_call(relay.reshape(const_1539.astype('float32'), [10, 14, 12])), 0)
output = relay.Tuple([call_1530,call_1538,const_1539,])
output2 = relay.Tuple([call_1531,call_1540,const_1539,])
func_1541 = relay.Function([], output)
mod['func_1541'] = func_1541
mod = relay.transform.InferType()(mod)
mutated_mod['func_1541'] = func_1541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1541_call = mutated_mod.get_global_var('func_1541')
call_1542 = func_1541_call()
output = call_1542
func_1543 = relay.Function([], output)
mutated_mod['func_1543'] = func_1543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_1549 = relay.TupleGetItem(func_782_call(), 0)
call_1550 = relay.TupleGetItem(func_784_call(), 0)
const_1562 = relay.const([1.434051,1.225600,4.939023,6.329111,-7.020986,2.776089,-5.666361,8.854423,9.636029,4.276422,7.540399,3.433667,7.049106,0.328153,7.636329,-3.395489,-8.470551,-1.629713,-9.844530,7.960729,-0.678479,2.640653,8.212908,3.640809,-6.575279,9.212004,6.739671,-9.026752,9.778902,6.993461,-2.064499,5.653477,-5.052253], dtype = "float64")#candidate|1562|(33,)|const|float64
bop_1563 = relay.maximum(call_1549.astype('int8'), relay.reshape(const_1562.astype('int8'), relay.shape_of(call_1549))) # shape=(33,)
bop_1566 = relay.maximum(call_1550.astype('int8'), relay.reshape(const_1562.astype('int8'), relay.shape_of(call_1550))) # shape=(33,)
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
call_1591 = relay.TupleGetItem(func_602_call(), 1)
call_1592 = relay.TupleGetItem(func_604_call(), 1)
func_1157_call = mod.get_global_var('func_1157')
func_1160_call = mutated_mod.get_global_var('func_1160')
var_1601 = relay.var("var_1601", dtype = "float64", shape = (2640,))#candidate|1601|(2640,)|var|float64
call_1600 = relay.TupleGetItem(func_1157_call(relay.reshape(var_1601.astype('float64'), [16, 15, 11])), 0)
call_1602 = relay.TupleGetItem(func_1160_call(relay.reshape(var_1601.astype('float64'), [16, 15, 11])), 0)
func_1113_call = mod.get_global_var('func_1113')
func_1115_call = mutated_mod.get_global_var('func_1115')
var_1615 = relay.var("var_1615", dtype = "uint8", shape = (325,))#candidate|1615|(325,)|var|uint8
call_1614 = relay.TupleGetItem(func_1113_call(relay.reshape(var_1615.astype('uint8'), [325,])), 0)
call_1616 = relay.TupleGetItem(func_1115_call(relay.reshape(var_1615.astype('uint8'), [325,])), 0)
func_1237_call = mod.get_global_var('func_1237')
func_1239_call = mutated_mod.get_global_var('func_1239')
call_1637 = relay.TupleGetItem(func_1237_call(relay.reshape(call_1591.astype('float32'), [11, 16, 3])), 2)
call_1638 = relay.TupleGetItem(func_1239_call(relay.reshape(call_1591.astype('float32'), [11, 16, 3])), 2)
output = relay.Tuple([bop_1563,call_1591,call_1600,var_1601,call_1614,var_1615,call_1637,])
output2 = relay.Tuple([bop_1566,call_1592,call_1602,var_1601,call_1616,var_1615,call_1638,])
func_1645 = relay.Function([var_1601,var_1615,], output)
mod['func_1645'] = func_1645
mod = relay.transform.InferType()(mod)
var_1646 = relay.var("var_1646", dtype = "float64", shape = (2640,))#candidate|1646|(2640,)|var|float64
var_1647 = relay.var("var_1647", dtype = "uint8", shape = (325,))#candidate|1647|(325,)|var|uint8
output = func_1645(var_1646,var_1647,)
func_1648 = relay.Function([var_1646,var_1647,], output)
mutated_mod['func_1648'] = func_1648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_1694 = relay.TupleGetItem(func_782_call(), 0)
call_1695 = relay.TupleGetItem(func_784_call(), 0)
output = call_1694
output2 = call_1695
func_1704 = relay.Function([], output)
mod['func_1704'] = func_1704
mod = relay.transform.InferType()(mod)
mutated_mod['func_1704'] = func_1704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mutated_mod.get_global_var('func_1704')
call_1705 = func_1704_call()
output = call_1705
func_1706 = relay.Function([], output)
mutated_mod['func_1706'] = func_1706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1706_call = mutated_mod.get_global_var('func_1706')
call_1749 = func_1704_call()
call_1750 = func_1704_call()
var_1770 = relay.var("var_1770", dtype = "float64", shape = (33,))#candidate|1770|(33,)|var|float64
bop_1771 = relay.bitwise_and(call_1749.astype('int16'), relay.reshape(var_1770.astype('int16'), relay.shape_of(call_1749))) # shape=(33,)
bop_1774 = relay.bitwise_and(call_1750.astype('int16'), relay.reshape(var_1770.astype('int16'), relay.shape_of(call_1750))) # shape=(33,)
output = relay.Tuple([bop_1771,])
output2 = relay.Tuple([bop_1774,])
func_1816 = relay.Function([var_1770,], output)
mod['func_1816'] = func_1816
mod = relay.transform.InferType()(mod)
var_1817 = relay.var("var_1817", dtype = "float64", shape = (33,))#candidate|1817|(33,)|var|float64
output = func_1816(var_1817)
func_1818 = relay.Function([var_1817], output)
mutated_mod['func_1818'] = func_1818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1359_call = mod.get_global_var('func_1359')
func_1360_call = mutated_mod.get_global_var('func_1360')
call_1825 = func_1359_call()
call_1826 = func_1359_call()
func_1645_call = mod.get_global_var('func_1645')
func_1648_call = mutated_mod.get_global_var('func_1648')
var_1849 = relay.var("var_1849", dtype = "float64", shape = (2640,))#candidate|1849|(2640,)|var|float64
const_1850 = relay.const([7,8,-1,10,-3,6,3,-5,2,8,-1,-7,-1,-7,-2,-5,-4,-4,1,1,-8,-5,7,-1,3,-3,2,-3,5,-2,-4,6,1,5,6,8,-4,-5,5,4,-5,-4,-10,-8,9,-2,10,-3,9,-4,5,-9,7,2,9,-9,2,1,-10,-7,-2,4,-8,-2,-6,-2,-6,-9,-4,-4,4,7,-9,-8,-1,10,3,-5,2,9,-2,8,-1,-3,-6,8,-2,-8,7,-10,10,-4,-7,-5,6,8,5,10,-2,1,-9,10,5,-2,1,-1,-3,5,3,10,3,1,-3,6,-3,-3,-7,6,10,-4,-2,-3,9,-7,-9,-4,-5,2,6,-3,-8,-1,-1,7,-7,-6,6,-3,9,-1,-7,1,-10,9,-3,-4,1,6,-4,-5,5,-9,-3,8,-2,-8,-4,10,4,-1,-4,-9,-4,-8,9,-1,-7,5,-3,-1,4,4,10,5,5,-10,2,-3,4,5,7,8,-6,-5,10,4,5,3,1,-7,5,-5,-9,-3,2,-8,6,4,-3,-1,-4,6,-2,-5,8,-1,-1,9,-5,-5,-10,5,-1,8,-7,-4,5,-10,-2,9,-9,2,-7,2,-3,10,-7,1,-5,1,-9,4,-6,10,1,9,-2,-2,2,-2,8,-8,8,-5,10,6,1,-5,6,7,7,-7,-7,-1,-2,3,6,7,5,-6,5,4,1,5,7,5,7,4,-3,-2,9,-7,1,10,3,8,-7,4,-4,-7,10,-6,6,-1,-6,-7,2,-1,-5,6,-6,-6,1,-2,10,7,-1,-6,-4,9,-2,4,-8,5,-5,-9,-9,3,-6,6,-4,5,5,-4,10,8,8,6,-8,-9,-5,-5,5,4,-5], dtype = "uint8")#candidate|1850|(325,)|const|uint8
call_1848 = relay.TupleGetItem(func_1645_call(relay.reshape(var_1849.astype('float64'), [2640,]), relay.reshape(const_1850.astype('uint8'), [325,]), ), 5)
call_1851 = relay.TupleGetItem(func_1648_call(relay.reshape(var_1849.astype('float64'), [2640,]), relay.reshape(const_1850.astype('uint8'), [325,]), ), 5)
output = relay.Tuple([call_1825,call_1848,var_1849,const_1850,])
output2 = relay.Tuple([call_1826,call_1851,var_1849,const_1850,])
func_1880 = relay.Function([var_1849,], output)
mod['func_1880'] = func_1880
mod = relay.transform.InferType()(mod)
mutated_mod['func_1880'] = func_1880
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1881 = relay.var("var_1881", dtype = "float64", shape = (2640,))#candidate|1881|(2640,)|var|float64
func_1880_call = mutated_mod.get_global_var('func_1880')
call_1882 = func_1880_call(var_1881)
output = call_1882
func_1883 = relay.Function([var_1881], output)
mutated_mod['func_1883'] = func_1883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_752_call = mod.get_global_var('func_752')
func_754_call = mutated_mod.get_global_var('func_754')
call_1910 = func_752_call()
call_1911 = func_752_call()
output = call_1910
output2 = call_1911
func_1912 = relay.Function([], output)
mod['func_1912'] = func_1912
mod = relay.transform.InferType()(mod)
mutated_mod['func_1912'] = func_1912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1912_call = mutated_mod.get_global_var('func_1912')
call_1913 = func_1912_call()
output = call_1913
func_1914 = relay.Function([], output)
mutated_mod['func_1914'] = func_1914
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1917 = relay.var("var_1917", dtype = "float32", shape = (4, 5, 11))#candidate|1917|(4, 5, 11)|var|float32
uop_1918 = relay.sinh(var_1917.astype('float32')) # shape=(4, 5, 11)
func_1704_call = mod.get_global_var('func_1704')
func_1706_call = mutated_mod.get_global_var('func_1706')
call_1920 = func_1704_call()
call_1921 = func_1704_call()
func_1132_call = mod.get_global_var('func_1132')
func_1134_call = mutated_mod.get_global_var('func_1134')
call_1933 = relay.TupleGetItem(func_1132_call(), 0)
call_1934 = relay.TupleGetItem(func_1134_call(), 0)
uop_1944 = relay.acos(uop_1918.astype('float64')) # shape=(4, 5, 11)
output = relay.Tuple([call_1920,call_1933,uop_1944,])
output2 = relay.Tuple([call_1921,call_1934,uop_1944,])
func_1949 = relay.Function([var_1917,], output)
mod['func_1949'] = func_1949
mod = relay.transform.InferType()(mod)
var_1950 = relay.var("var_1950", dtype = "float32", shape = (4, 5, 11))#candidate|1950|(4, 5, 11)|var|float32
output = func_1949(var_1950)
func_1951 = relay.Function([var_1950], output)
mutated_mod['func_1951'] = func_1951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_1987 = func_1912_call()
call_1988 = func_1912_call()
output = relay.Tuple([call_1987,])
output2 = relay.Tuple([call_1988,])
func_1999 = relay.Function([], output)
mod['func_1999'] = func_1999
mod = relay.transform.InferType()(mod)
output = func_1999()
func_2000 = relay.Function([], output)
mutated_mod['func_2000'] = func_2000
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2004 = relay.var("var_2004", dtype = "uint64", shape = (8, 10, 2))#candidate|2004|(8, 10, 2)|var|uint64
var_2005 = relay.var("var_2005", dtype = "uint64", shape = (8, 10, 2))#candidate|2005|(8, 10, 2)|var|uint64
bop_2006 = relay.right_shift(var_2004.astype('uint64'), relay.reshape(var_2005.astype('uint64'), relay.shape_of(var_2004))) # shape=(8, 10, 2)
output = bop_2006
output2 = bop_2006
func_2014 = relay.Function([var_2004,var_2005,], output)
mod['func_2014'] = func_2014
mod = relay.transform.InferType()(mod)
mutated_mod['func_2014'] = func_2014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2014_call = mutated_mod.get_global_var('func_2014')
var_2016 = relay.var("var_2016", dtype = "uint64", shape = (8, 10, 2))#candidate|2016|(8, 10, 2)|var|uint64
var_2017 = relay.var("var_2017", dtype = "uint64", shape = (8, 10, 2))#candidate|2017|(8, 10, 2)|var|uint64
call_2015 = func_2014_call(var_2016,var_2017,)
output = call_2015
func_2018 = relay.Function([var_2016,var_2017,], output)
mutated_mod['func_2018'] = func_2018
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2057 = relay.var("var_2057", dtype = "float32", shape = (7, 7, 2))#candidate|2057|(7, 7, 2)|var|float32
uop_2058 = relay.acosh(var_2057.astype('float32')) # shape=(7, 7, 2)
func_458_call = mod.get_global_var('func_458')
func_462_call = mutated_mod.get_global_var('func_462')
var_2061 = relay.var("var_2061", dtype = "float32", shape = (33,))#candidate|2061|(33,)|var|float32
const_2062 = relay.const([-6.425799,8.806680,9.866842,-2.610610,3.364956,4.237769,-0.415762,9.201993,-0.252982,3.976695,-6.398249,7.650746,-6.050489,6.379021,-7.870442,1.897328,-0.975580,-3.149470,-8.265988,-7.902754,-4.623451,9.464259,-7.141445,6.590249,6.015597,1.729486,-1.780505,-5.209162,2.111656,-1.926419,5.720760,-1.685798,-7.961651,2.621072,-8.601083,-9.081329,-7.336782,3.593832,9.766757,1.031803,-4.124252,-3.025825,-8.542428,9.312015,-5.875715,9.126615,5.424696,3.618712,-9.615576,-3.797065,7.887043,2.979622,-3.103543,-9.087955,-1.736621,0.807185,6.242690,9.693179,-4.691480,3.282113,-8.504471,-6.830916,9.799589,4.980841,0.601691,-1.092454,-6.397724,-7.289688,-5.349198,-4.755985,-7.522925,5.828518,-1.612486,5.901887,6.554481,2.982729,-1.954174,9.907064,-4.431603,6.665914,-6.273340,-5.518143,-9.022559,-6.540496,4.177842,8.057199,-3.699779,4.443205,6.561642,9.429815,-0.030257,-1.667557,2.503974,-5.689027,-7.692669,6.798473,6.485320,4.012648,-9.703315,-9.423755,4.976052,2.767542,3.742689,-0.526235,-9.927933,2.305423,-0.922982,0.851243,-1.722763,6.172858,0.205574,1.329738,-9.988215,-0.576007,-6.267733,7.271759,-6.579570,4.779243,3.541068,-5.446248,-2.374404,-7.892045,7.848040,-7.112607,9.860813,-4.401794,-4.482812,7.129181,0.841696,9.801476,6.332505,0.800140,9.526139,1.664941,-1.576192,-0.305792,4.712860,3.249795,-6.824903,-2.359911,-9.426296,4.568753,9.714610,8.186758,-6.905959,-2.820595,4.640571,-6.984700,6.912458,-2.932578,6.172423,-8.911993,0.097001,-2.939798,2.036269,-5.425441,8.984032,-4.381720,-1.465065,4.277409,-9.444449,-4.427365,7.966000,-4.030241,-4.318534,-6.876893,-9.246414,3.139148,8.440224,8.160546,-4.239405,-1.749056,9.271315,-8.680597,-9.590071,6.931946,-1.171291,6.192026,-3.494121,-8.070086,-1.128232,-7.243303,8.932461,-6.535622,1.049884,9.476983,8.147838,-3.838524,-2.508345,5.444393,-9.493532,2.397488,-4.256733,0.372241,-5.292300,-7.032002,-8.999462,2.628599,-6.700595,-8.427744,-0.350386,1.249264,3.554782,-8.447652,4.195621,7.523474,-4.072621,-6.931619,3.096299,8.033868,4.174794,-4.495557,2.914268,9.904466,0.832119,6.819995,0.557115,-5.274225,-2.640533,-3.483585,-9.844045,-0.471111,-6.014356,2.913107,-3.457959,6.447307,-3.812378,7.937891,-5.559296,4.938382,7.990977,3.474425,-6.865383,2.820968,-9.714939,-3.268550,5.913014,-9.405663,1.332471,9.490857,-5.413394,2.612910,-7.288827,-6.766860,8.233681,3.659943,7.055393,8.077880,-1.822780,-8.487311,-9.826775,3.091948,9.984153,8.137963,4.853681,-6.110083,9.468589,9.200054,0.856347,-6.754954,0.490813,6.717599,-5.114538,-2.463594,9.534132,-0.129293,6.332895,-4.041665,3.248322,9.679306,-4.908580,-7.182874,9.421181,-1.342118,-9.987562,4.039064,-9.774810,-1.755180,7.904126,8.268250,6.381842,-8.359748,8.145132,-3.230060,-3.442954,1.534201,9.959704,2.361244,3.051989,2.982119,-3.724380,-4.237655,3.519736,-0.017346,8.341732,-1.837834,1.070952,-1.235598,3.428575,3.329086,-9.333888,-4.140262,-6.991483,0.118477,2.533919,4.931687,8.396968,-3.827715,-0.473219,-1.500717,-5.258771,9.321222,4.190351,-4.456043,-0.437956,3.274607,7.595370,-0.518395,3.170664,9.402558,1.821046,-6.727220,-4.404747,0.474610,7.846167,2.750204,-5.998480,4.020456,-5.198738,-6.928207,9.281569,6.757904,-3.323720,9.321468,1.856062,-6.970853,3.710608,-2.240607,-4.310745,9.399197,1.005316,1.550135,6.404730,9.966061,4.223169,-0.755215,4.556653,6.993813,2.603548,8.334189,2.879923,0.422250,3.072795,1.917002,-6.961208,1.095968,5.132422,6.537078,-2.774828,-6.980463,8.973399,-9.145203,-6.293872,-9.101730,-5.752966,0.347025,6.023867,0.969169,-7.254813,-6.914264,2.633824,-2.174934,8.935820,6.622171,-0.277698,3.885040,-0.909152,4.764780,9.159554,-3.316003,7.352161,2.910599,7.218439,5.327169,9.949677,-8.707004,-2.018475,0.223609,-8.005656,2.102361,-6.725848,-9.550346,-9.564165,-2.188603,8.454366,-0.712489,-2.925071,-9.329185,-1.497631,1.602308,4.891073,-5.723029,-0.523132,5.495729,-8.017689,4.068810,1.947950,6.624478,8.494597,1.178582,-5.105722,-6.521441,-2.850276,-8.162964,-0.946136,-2.337012,1.587774,8.476515,5.266650,4.278354,8.261068,-7.612788,-3.992599,0.509603,1.937827,0.043881,-3.450415,-7.760741,-4.119751,0.438446,-4.230432,-9.930773,-9.261831,0.241756,6.097527,7.028640,-1.297034,2.470601,6.412819,-9.057359,-6.573226,-9.243116,1.007750,0.843539,-0.656127,3.204259,-0.425114,-3.948239,8.905979,-6.209283,-9.413326,-2.744981,-7.288362,-4.742759,-0.490064,-7.262623,-9.557700,3.883699,-5.861448,9.558894,1.203613,1.090710,-3.062227,-3.401518,-1.702150,-2.478212,-4.794586,8.093707,8.185538,-9.279305,-0.769043,-6.642651,2.627350,1.193282,-5.759758,-8.869316,6.492587,2.035148,-8.606783,2.294747,4.275722,8.370449,-2.734642,-2.471955,-5.156259,8.453758,3.572371,0.019016,4.245062,-9.886937,6.331503,6.004196,1.925404,3.094288,-1.066973,-6.302145,-7.661515,1.293346,-7.293645,-7.169610,-2.146487,4.021158,4.250721,5.376619,5.238755,-5.473020,-2.306679,7.876571,8.049032,5.316808,-3.655260,0.628765,-9.274601,2.611712,-9.482009,0.833507,-7.610096,-4.017605,-9.068449,-5.858306,-5.537875,-3.915445,4.450507,-3.849024,-4.137823,-4.625315,3.739917,-3.124376], dtype = "float32")#candidate|2062|(528,)|const|float32
call_2060 = relay.TupleGetItem(func_458_call(relay.reshape(var_2061.astype('float32'), [11, 1, 3]), relay.reshape(const_2062.astype('float32'), [11, 16, 3]), ), 0)
call_2063 = relay.TupleGetItem(func_462_call(relay.reshape(var_2061.astype('float32'), [11, 1, 3]), relay.reshape(const_2062.astype('float32'), [11, 16, 3]), ), 0)
func_1645_call = mod.get_global_var('func_1645')
func_1648_call = mutated_mod.get_global_var('func_1648')
var_2070 = relay.var("var_2070", dtype = "float64", shape = (12, 220))#candidate|2070|(12, 220)|var|float64
const_2071 = relay.const([[-3],[9],[10],[7],[-4],[-10],[2],[-6],[5],[-7],[-6],[-2],[9],[-1],[2],[-3],[8],[-4],[-1],[2],[5],[-2],[10],[-2],[-10],[10],[8],[-7],[9],[-3],[1],[7],[-10],[-10],[3],[-10],[-6],[3],[-10],[2],[4],[6],[-3],[-10],[-4],[3],[-2],[7],[-3],[-5],[-10],[3],[9],[1],[3],[-1],[-7],[-10],[1],[3],[2],[1],[6],[8],[-4],[6],[-9],[-10],[-6],[-8],[-8],[5],[-4],[-6],[-4],[2],[-4],[-2],[10],[2],[4],[-10],[6],[9],[-2],[-1],[6],[4],[3],[-6],[-8],[5],[-3],[4],[6],[9],[-1],[-2],[8],[-9],[8],[1],[-7],[5],[6],[9],[10],[-7],[10],[8],[5],[-5],[-6],[-5],[8],[-9],[5],[-2],[6],[4],[-9],[-7],[4],[3],[5],[-1],[1],[-1],[3],[-3],[2],[-1],[3],[-1],[3],[2],[-6],[-2],[-5],[6],[8],[-2],[-3],[8],[-9],[-1],[5],[7],[-7],[7],[-4],[3],[-8],[-2],[-2],[2],[-6],[-1],[-7],[7],[9],[8],[9],[-2],[-4],[6],[5],[-9],[4],[7],[2],[8],[-6],[-6],[-5],[9],[-8],[10],[2],[4],[8],[-7],[-9],[10],[-10],[1],[-6],[9],[-7],[5],[8],[8],[2],[-3],[-7],[-4],[9],[1],[-6],[3],[-8],[7],[3],[-8],[-8],[2],[8],[4],[-7],[4],[-6],[-10],[10],[2],[4],[3],[2],[-10],[3],[-7],[8],[9],[-9],[-5],[1],[-2],[-10],[1],[6],[7],[9],[-6],[7],[7],[-1],[-4],[-4],[-6],[-7],[-1],[4],[5],[-8],[5],[8],[-5],[-9],[9],[4],[-9],[10],[5],[-8],[9],[4],[4],[-3],[-2],[-3],[-6],[9],[1],[2],[-8],[-8],[3],[-10],[-2],[-9],[-6],[10],[9],[-8],[6],[-9],[4],[4],[6],[7],[-2],[2],[-1],[-4],[-3],[-3],[-4],[-8],[8],[-5],[7],[7],[-2],[9],[8],[-3],[-1],[8],[9],[6],[-4],[8],[3],[2],[-2],[-8],[-3],[-4],[-9],[-4],[-1],[7],[-3],[-5],[-6],[-2],[-1],[10],[-8],[7],[-3],[3],[-1],[10],[10],[-5]], dtype = "uint8")#candidate|2071|(325, 1)|const|uint8
call_2069 = relay.TupleGetItem(func_1645_call(relay.reshape(var_2070.astype('float64'), [2640,]), relay.reshape(const_2071.astype('uint8'), [325,]), ), 0)
call_2072 = relay.TupleGetItem(func_1648_call(relay.reshape(var_2070.astype('float64'), [2640,]), relay.reshape(const_2071.astype('uint8'), [325,]), ), 0)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_2073 = relay.TupleGetItem(func_970_call(), 0)
call_2074 = relay.TupleGetItem(func_972_call(), 0)
output = relay.Tuple([uop_2058,call_2060,var_2061,const_2062,call_2069,var_2070,const_2071,call_2073,])
output2 = relay.Tuple([uop_2058,call_2063,var_2061,const_2062,call_2072,var_2070,const_2071,call_2074,])
func_2075 = relay.Function([var_2057,var_2061,var_2070,], output)
mod['func_2075'] = func_2075
mod = relay.transform.InferType()(mod)
mutated_mod['func_2075'] = func_2075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2075_call = mutated_mod.get_global_var('func_2075')
var_2077 = relay.var("var_2077", dtype = "float32", shape = (7, 7, 2))#candidate|2077|(7, 7, 2)|var|float32
var_2078 = relay.var("var_2078", dtype = "float32", shape = (33,))#candidate|2078|(33,)|var|float32
var_2079 = relay.var("var_2079", dtype = "float64", shape = (12, 220))#candidate|2079|(12, 220)|var|float64
call_2076 = func_2075_call(var_2077,var_2078,var_2079,)
output = call_2076
func_2080 = relay.Function([var_2077,var_2078,var_2079,], output)
mutated_mod['func_2080'] = func_2080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1132_call = mod.get_global_var('func_1132')
func_1134_call = mutated_mod.get_global_var('func_1134')
call_2125 = relay.TupleGetItem(func_1132_call(), 0)
call_2126 = relay.TupleGetItem(func_1134_call(), 0)
func_1359_call = mod.get_global_var('func_1359')
func_1360_call = mutated_mod.get_global_var('func_1360')
call_2128 = func_1359_call()
call_2129 = func_1359_call()
output = relay.Tuple([call_2125,call_2128,])
output2 = relay.Tuple([call_2126,call_2129,])
func_2131 = relay.Function([], output)
mod['func_2131'] = func_2131
mod = relay.transform.InferType()(mod)
mutated_mod['func_2131'] = func_2131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mutated_mod.get_global_var('func_2131')
call_2132 = func_2131_call()
output = call_2132
func_2133 = relay.Function([], output)
mutated_mod['func_2133'] = func_2133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1706_call = mutated_mod.get_global_var('func_1706')
call_2249 = func_1704_call()
call_2250 = func_1704_call()
func_898_call = mod.get_global_var('func_898')
func_901_call = mutated_mod.get_global_var('func_901')
const_2257 = relay.const([-9.696592,5.312232,3.530774,8.269491,-3.581773,-7.759230,-2.226539,0.842757,3.221773,-3.321795,-3.921583,-6.421450,-4.465827,3.177861,-1.938730,-1.158397,9.566352,-1.211801,-6.497676,-3.401621,1.855037,-8.976522,-2.507719,6.312528,-1.601445,-3.575231,-3.509100,-1.876816,4.312826,-1.018147,1.384025,-4.571830,3.701061,5.755511,-3.675829,-4.247816,-5.150846,-4.152526,-7.882320,4.934093,0.309867,9.812676,-4.423298,-9.621538,7.828888,3.892566,6.503919,7.783671,3.206508,-4.048662,-6.910740,5.702374,-2.614587,5.627233,1.996160,1.640518,-4.853746,-0.111622,-3.296186,6.592937,-9.063797,-9.500966,-7.621775,-4.176223,6.301249,-6.586036,1.001263,-9.127148,6.509453,-9.612909,-3.763282,5.788833,-6.679087,-8.625246,-3.835789,-4.821729,-2.282381,-3.879141,-7.765321,-2.565903,-5.281215,1.151854,9.011776,2.063105,-0.562021,7.989031,9.660896,0.657967,1.581178,8.889262,5.840433,-2.342225,-9.968030,5.892606,2.631883,-0.875694,-1.545491,1.039741,-4.662723,-3.778105,-5.729272,2.701979,-6.836524,8.168119,-6.229865,8.527568,-2.127226,-0.200804,-6.581792,6.244299,8.319632,7.160496,0.392229,9.888081,9.134969,-8.539813,-4.765504,-1.871032,7.867592,-6.561711,-5.964026,3.881541,7.551841,8.058789,6.106340,4.404664,9.633322,-3.655932,8.899634,-7.975063,6.882126,-6.925612,-6.940599,-6.798441,-8.404099,-2.968927,-2.108409,7.247595,3.626131,-1.500635,3.726611,8.266288,-7.324466,5.008398,-1.218146,9.380659,5.780713,2.327663,-3.234784,6.576799,-5.486115,3.523944,6.115037,-5.448964,5.748890,-4.312882,-1.058524,7.936738,7.545804,-9.071275,-9.936505,-1.092742,9.344552,-5.160505,8.386488,-0.189768,9.640242,6.467726,-7.857088,5.882983,-8.948734,-5.825924,4.663049,7.271831,-4.752471,-8.989268,0.229015,-6.077608,-7.396048,-0.847161,-5.257995,9.903973,-8.564633,3.478888,-7.730808,4.827828,-5.069510,6.830741,8.721664,-3.159448,-1.469627,2.481699,6.093553,-9.884776,-6.291621,-2.906895,1.291071,-7.073685,-0.158769,-0.704722,-9.493009,5.886067,5.406002,-2.574641,8.596239,1.833020,-5.700314,-0.968700,-7.017505,0.828394,9.862678,-1.777994,-5.651149,5.238250,-7.175499,5.580763,2.026571,8.240351,-9.405887,5.453963,-3.981823,3.138631,8.707957,6.062764,0.256860,-9.163855,-0.354139,9.524427,2.059510,3.015275,8.125609,-4.590223,2.723326,1.705662,-6.226861,4.754685,3.412095,3.400728,-5.659911,9.352622,5.071313,0.331284,-1.598579,-1.488196,2.692796,0.568511,3.584455,5.008610,2.482255,-5.418807,1.622573,-7.077409,-8.836371,-1.559113,-6.321459,-5.979604,4.028774,0.971275,8.010612,-0.655885,3.392478,4.269198,4.789675,9.099824,4.936034,-3.510273,-8.309992,-4.505192,-1.125787,2.522183,-8.457567,3.672143,8.521262,5.564178,-1.865046,1.195792,6.833382,-5.097011,1.714240,6.882213,2.551606,-2.270556,-1.690572,3.017542,4.296170,-3.072425,-8.116939,4.996374,-7.392333,-1.517551,-6.189856,5.749360,-2.461932,1.046823,8.306641,4.504836,-0.517652,-0.101143,-1.826462,-8.864509,4.432722,3.604669,-7.320293,2.137223,1.648339,3.599902,-4.200145,8.749315,5.957759,-2.356955,1.312623,5.912638,2.263838,-6.834449,8.851949,4.148484,7.665987,5.646062,-4.692669,8.453309,-4.695871,4.259638,9.584684,-5.202262,5.039392,6.319945,-0.498523,2.747300,2.759629,8.454484,-6.994859,9.330255,1.670087,9.244041,1.079367,6.710197,4.840699,-6.866806,4.210992,9.141790,-2.688795,3.908011,-9.878917,-0.803860,-1.693409,-2.876522,8.547382,7.924159,-6.076769,-9.476344,0.780034,-5.939171,-2.633201,2.521537,9.644321,3.753402,8.479719,-8.355367,0.596253,1.345294,-1.608637,-0.312276,9.444948,-9.529812,-0.650131,-3.893395,-2.282782,-4.488481,6.679674,-2.743841,8.899410,-5.199146,-0.062538,-6.824347,-2.121135,1.598756,9.579322,-5.616082,5.903835,7.357975,1.220929,5.808556,-1.292455,-3.257277,0.165139,-1.179474,-4.375462,-7.334919,2.592152,-6.361285,-8.267917,-5.734820,3.632866,4.994407,0.900372,-4.283087,-0.530187,-3.103888,-6.095059,-2.025024,3.109337,-9.105492,-0.599625,-5.785372,4.820875,9.252001,-9.637845,5.680869,-0.591656,7.014593,5.713380,-8.005687,6.969261,-6.837603,9.697547,-4.151234,3.640521,2.244214,5.007003,7.991847,-3.561879,-5.309934,-7.055590,8.035679,-6.478047,-3.777228,-2.175797,0.714159,2.835556,9.393628,5.410913,4.112022,-2.160297,-2.981016,-0.322193,-5.561237,-0.669932,-2.464343,4.730142,2.617177,-0.113288,0.635043,-3.789692,-3.356308,9.817067,-3.948434,0.786823,7.522594,-9.332525,2.534193,-8.096278,-2.463287,3.606790,8.899234,-9.445825,-0.626444,9.924450,3.800942,7.989555,4.023827,-7.297178,6.867268,-7.244155,1.465254,-6.175728,4.454148,9.827258,3.012177,-4.251227,1.635896,0.564349,9.057990,3.321008,-3.947486,4.841144,7.348440,0.627189,3.769071,-3.135511,8.350166,-1.901605,9.582574,-5.766423,-4.096575,7.616558,9.026482,5.301175,1.945790,1.218697,6.891588,-7.716457,-9.846175,5.223475,3.909663,0.535100,-9.213201,5.141878,9.129535,-6.548869,5.965855,2.136252,-0.073221,5.089189,3.796478,1.894782,7.523885,-1.636584,-6.381569,-2.872669,3.788100,-0.498156,1.551104,2.556143,1.079311,-9.936066,6.100935,4.843777,-7.530828,-1.799367,8.743775,8.367256,7.696267,9.420642,6.266497,3.899937,1.593114,1.523097,7.962806,3.687025,-8.685219,5.835356,5.539459,-7.113439,-9.461906,9.659994,-3.995551,-7.082368,-6.796283,4.959313,1.924318,-0.559585,-8.491006,4.532133,-8.589787,-2.075792,-7.196087,8.342853,-7.127956,-5.872836,-9.760472,2.045030,-0.036262,-8.237061,1.966412,-4.570573,-3.930197,5.445260,-1.108020,-2.112644,3.438696,-6.034522,6.969337,0.727517,6.168524,-2.608487,7.816205,-6.031941,2.666798,8.730895,4.262792,-1.735686,-1.126198,-6.126514,-5.237486,-2.222296,-0.097108,-7.835449,-6.147300,1.264857,0.976569,2.944906,1.825554,-7.462324,-8.015841,9.079376,3.089869,7.783887,7.504290,8.873419,-1.389351,1.486100,-2.004431,-7.368264,5.734615,-7.480002,1.547056,-6.206349,3.388844,-7.512912,-6.897235,2.531065,6.924821,5.048925,0.721508,-6.859534,-0.345449,-7.957566,5.952593,6.801923,-6.660266,8.217122,0.625497,6.574328,-7.104146,-9.729243,0.369018,5.291240,-6.016007,-5.141279,1.942132,-1.232602,-3.913579,-9.758827,9.740184,3.053689,3.100970,-3.925723,-0.257863,3.609091,6.520638,5.403301,-0.209923,5.948743,5.652792,-4.292445,-2.875456,3.131146,4.275450,3.238920,7.244835,-6.469374,5.736407,-1.429382,-5.324219,3.227099,4.682099,9.172897,7.362751,7.514821,-2.998649,7.644831,-1.045877,6.792344,-8.813614,-3.882561,6.861109,-2.704844,2.920391,-6.232718,-7.558557,0.867025,-7.883431,1.006060,3.545830,0.457537,-6.535474,0.366605,7.658391,-4.633851,0.857592,2.104537,-7.464485,3.184761,-9.711775,6.418349,3.321346,7.320238,4.594364,2.348519,1.772655,-7.271700,1.855754,-1.921481,6.222271,-9.815372,5.093805,3.413039,1.530298,-0.716984,6.388686,4.252105,-9.053418,-0.119361,4.272127,0.572154,-6.753061,7.737651,2.162701,-7.231369,-7.406526,6.825768,2.670979,7.266743,4.536645,-3.992752,-1.769445,-1.526796,-4.362810,-7.973564,-4.341352,-7.799625,-9.503163,7.501023,4.648836,-4.269300,-2.933447,-2.071243,-2.865946,1.586396,9.613766,-9.901117,0.003584,-0.888531,-4.058025,9.562984,-7.075358,4.054858,7.381991,-9.006256,4.066244,5.037646,-6.499305,4.559636,3.387259,2.368584,-2.898324,-1.274085,-9.660328,-6.740258,-9.688464,3.659142,1.155785,7.371886,4.508903,-5.305570,-9.253147,6.697877,3.272912,5.828782,0.567489,7.829675,1.466682,1.491562,-0.518309,-9.966660,3.949703,-1.509366,-6.123098,-0.697961,6.510145,-1.151759,-1.412161,2.707157,-1.939851,-0.726769,2.072379,-8.682603,-7.942015,-1.258913,1.586652,4.011422,-9.050713,0.160091,5.465808,1.348913,-7.204013,-3.344649,2.775946,-4.083411,-1.980325,6.721836,-3.737298,-1.790883,4.803265,-3.487847,7.037015,9.837654,1.031371,7.948436,-3.669584,3.754282,-9.194829,4.896766,8.281776,-6.853798,2.321492,2.239451,6.839359,-7.866941,-9.235182,0.608102,-5.425390,-7.281885,5.611243,-2.764343,-1.110773,8.549450,5.039734,-0.944573,-0.167997,-1.358487,-7.121786,-0.477343,-8.022529,-1.352063,1.238305,-8.665485,-7.873594,6.087990,-4.220388,-0.450971,0.012631,-5.760677,-3.031119,-4.582676,5.826857,-1.832117,-8.446198,3.904314,0.815280,-6.611999,0.976249,-5.060560,9.140190,1.147630,8.144648,-6.348391,2.614941,6.680673,5.362447,3.414029,0.220911,-8.550238,-8.078491,-5.656352,1.671162,-0.808598,4.030694,-8.526526,-8.639310,1.756625,1.676068,-2.358004,-2.707826,2.707480,5.631287,-8.735567,-5.052078,0.667007,-9.814659,7.132455,-0.137899,-2.929003,-4.820460,-1.317196,-3.535291,3.452507,0.488229,0.727507,8.020704,7.798194,3.802023,1.121177,-2.548597,-4.032296,-0.379804,-0.520220,6.029937,6.097948,5.179327,-7.276466,8.143750,-2.590677,6.386750,-6.925641,-7.041345,-0.200285,4.126962,6.538997,-1.983323,-3.358295,0.356992,2.535488,5.795345,5.497361,-6.831767,-4.412386,4.275911,-8.384448,-4.484257,9.241289,-3.993003,-4.416223,-7.576843,9.252517,7.230688,4.159774,-9.526671,1.808961,6.453801,-1.158948,-2.273612,4.663583,2.021489,4.902664,-3.452169,-2.494882,-3.196051,-3.755084,5.427538,1.035915,7.776698,7.641298,4.394503,6.212381,5.047022,-5.272272,5.911094,1.495566,4.440763,-9.625498,-3.764011,-8.629369,-5.212510,7.273727,-1.260131,-2.020834,3.575031,0.906475,0.440704,-6.321906,-5.795351,-7.881807,-9.697086,9.430099,-1.159421,-2.131466,-3.078726,0.114706,0.066434,-4.834530,2.303033,-8.808069,3.316782,4.898447,-3.504975,2.420173,-5.006885,-9.376113,-2.143725,-2.646525,-4.375082,0.732497,7.348066,4.132192,7.806635,-3.738167,-4.419553,1.278541,-5.751568,-0.546216,-7.911858,-7.733641,-0.884408,-5.684187,-5.695974,8.648679,3.933179,6.218210,-8.271876,9.618314,4.597019,-8.910863,-4.524798,2.287814,3.935357,-3.786921,2.972535,-1.725092,0.696266,-5.029253,-1.216566,-0.969852,-7.418736,-3.099938,-1.980759,-7.059624,-1.013503,-9.717310,2.554672,0.278526,0.585366,-2.670378,-8.936968,-6.175737,1.145443,6.345071,5.593722,4.330332,-4.038843,-4.020255,-2.231967,-0.930222,3.848729,9.838202,-8.958068,3.693797,-1.727178,-1.065291,1.533781,5.517606,-4.994422,-5.839336,-2.734946,1.310356,3.655932,-5.164044,2.429960,-6.900347,1.985560,8.242787,7.145887,8.946978,-8.542817,-1.147504,3.284782,7.295473,9.575884,9.696165,4.400538,-3.949015,-9.675895,-2.861402,7.675187,-5.499766,5.324829,-7.627643,8.721693,-5.723106,9.472015,0.037050,-6.721776,-4.656906,-3.860251,-6.339305,7.850364,-6.972039,9.577460,6.229086,-8.450548,8.230324,6.840385,-4.365104,4.369575,-1.919349,4.061586,9.949372,-4.028653,1.065018,2.415171,9.460864,-3.191197,-0.044171,-7.638858,-6.911622,-1.797275,-2.468372,2.182248,-2.889640,-5.626662,-0.447158,-1.135998,7.896400,1.195195,0.235249,-2.710480,8.462248,-9.198606,-3.836145,1.090217,2.020667,-6.449498,2.238435,-5.190880,1.136177,5.596615,5.725326,3.293308,-4.146170,7.746168,-6.123701,-6.959017,2.715286,1.450811,-4.776697,-3.202788,-5.323429,4.121396,6.328912,7.233155,-0.689271,-4.315112,-5.841261,8.226570,-2.072751,-9.100666,-3.897294,3.946838,-5.180139,-9.264893,2.806117,-4.708364,4.352916,-4.730175,-6.556804,7.393036,-3.415138,-6.195660,-5.300405,6.240864,-6.297808,1.536839,8.021193,-3.297057,2.914677,-3.874059,-0.114848,4.779289,-6.569651,-6.633178,4.784720,-6.230201,5.260672,0.413594,-8.525493,-1.563959,-6.243460,4.063028,-2.443576,9.063308,-5.017773,0.372823,8.486134,1.246144,-1.158885,-0.449360,8.453490,6.146584,0.181084,-8.337429,7.736399,-1.937050,-0.634057,9.082163,-7.830131,1.319601,-5.025732,5.882351,7.968618,-8.723917,-9.421408,9.756191,5.840589,-1.979338,5.715106,-6.606440,2.349759,0.924758,-4.154643,0.146727,3.302468,-5.870033,1.556266,0.364410,-8.994076,-4.708300,-3.431000,-1.048241,-8.794593,-5.485055,-9.637304,-4.624685,-3.952481,7.813149,1.861376,6.843265,6.853859,-1.324456,2.511276,1.802516,6.658631,-7.772975,-0.825022,3.293336,0.170151,-1.546457,-8.129278,8.489095,-5.703394,-4.025388,2.301417,9.054213,2.592352,7.344579,3.539274,-7.857783,-0.955166,1.439000,3.901975,4.449584,-8.415011,-8.365479,4.314097,2.892361,8.376359,7.978838,5.060068,9.508761,-1.691471,8.919809,-4.711611,4.060988,-1.434383,0.878478,9.228601,-3.053680,-1.476350,0.900266,2.109503,-8.153872,-0.545655,1.403925,-6.767203,-8.075187,-9.340503,-6.351468,1.267442,4.562013,-3.521038,7.927791,-3.807136,-0.520189,3.137844,-5.696638,-2.444302,4.541078,-5.601988,4.587373,4.177548,3.434669,4.260103,-6.111946,9.874692,7.646006,-5.769261,-0.902088,-1.901873,-5.293192,-3.300484,-9.601229,0.360469,0.791542,7.164306,-4.732486,-5.218304,-8.434961,8.046534,-5.725303,-9.543238,0.022221,-3.966986,0.287343,-6.713987,-0.413616,-1.770528,3.097103,-8.678288,9.056198,7.823844,0.133777,-4.093396,-5.232521,-0.785090,-6.077706,-8.879888,-0.857111,2.688844,5.670863,2.137760,-0.133445,9.162782,5.466699,-6.069672,4.169273,-8.506243,5.113902,-2.170240,-8.121149,-1.346309,9.211793,-5.370634,-7.828266,-1.959528,1.254199,8.837970,2.010286,-9.287604,3.327033,-6.359923,-5.333514,6.478846,4.287407,7.182303,-2.251891,-0.436683,-0.200082,4.530622,2.097946,9.629825,2.857670,-5.116754,5.530037,8.243471,-2.698254,7.758618,-7.616966,-4.704489,-8.485697,-3.882244,-0.521825,-5.010738,8.153037,9.088622,0.290196,-7.717885,8.562826,-9.957069,3.270558,4.412813,6.951577,-5.416362,2.820176,0.011820,9.133938,2.568043,-2.179302,-2.232102,4.600041,-4.188615,-2.708305,-4.364911,-8.890554,-4.300302,-8.502528,7.391644,-7.229496,-3.964413,-0.852917,6.050075,5.387141,4.258954,0.608359,8.962842,9.509033,8.501812,-8.327751,-0.543093,-5.932724,-6.258881,-1.697322,-1.454913,-9.661959,7.985277,-4.117822,-7.293037,6.727770,-9.397972,8.852759,6.526627,2.586309,7.827554,-1.841984,-7.141812,-0.313758,-4.093608,-9.575343,-1.433269,1.451003,-3.297339,-9.236219,3.274201,-1.999545,-6.806640,0.536419,1.022975,8.286146,6.654312,-4.468369,-4.192557,-5.977543,3.753393,-8.908815,3.810240,5.895410,6.795697,-2.257376,9.961424,-8.153066,8.595703,-1.645638,7.653631,9.816293,9.138617,-3.638152,-4.687900,-7.678881,-1.099885,3.391966,-5.042025,3.031822,7.174579,-0.770317,-9.570193,-9.982381,9.606330,-8.050758,-0.484845,9.182044,5.465600,-4.453719,-0.774696,-3.921397,2.832679,3.414482,-7.521846,4.180014,-5.574884,5.442310,4.873583,-3.490514,-7.827593,3.831463,-0.345456,-1.136940,-5.903027,-8.007558,-5.701807,3.551507,-0.712796,5.486131,8.035256,-2.377374,9.858253,8.631340,-2.929458,2.815587,-3.082920,1.681132,6.490352,4.823967,-9.677936,-1.173549,-8.197688,-5.401284,-3.085098,9.188033,3.844033,-3.795523,0.155198,8.865951,0.252796,-3.832338,9.118696,6.990835,-7.465423,-2.836451,-5.075196,7.490318,8.739983,7.127304,6.461481,7.814696,0.154530,6.787914,0.216074,-4.048830,0.612537,7.015842,-6.341131,4.538461,3.006356,-6.957430,3.692872,-8.367516,9.097888,-7.090131,-0.124631,3.361234,8.568333,6.418776,6.232030,-0.699336,-1.376419,9.563903,-7.779649,0.048772,1.174352,4.945717,5.310670,9.092576,4.611393,-7.562503,7.074422,0.355776,-8.868551,-3.974152,-8.502244,2.479641,-7.439192,-9.023020,6.065225,-9.269326,6.859741,4.007255,0.915612,0.861742,1.758733,-1.837062,-5.808220,0.987359,-5.110588,-2.386433,-5.503568,-3.536776,1.472098,7.153063,-7.785594,3.665111,6.089550,3.567762,6.900470,-1.853390,-7.579832,6.832909,-9.314684,1.136958,-8.653132,-0.567849,3.026668,9.473981,7.398742,-0.827322,-0.338321,4.365227,-5.377619,-3.750985,2.400018,-5.767410,-7.688080,-4.095063,0.972506,3.174552,-5.231015,-6.273745,-9.282340,-0.025441,3.938849,-0.212102,-8.856173,3.264091,-4.516715,-6.352971,-8.394741,7.723253,-8.023082,-3.302171,7.265956,-4.257710,1.904771,-0.161789,-1.954990,6.909121,3.919393,-4.573645,2.190384,-9.132640,5.057054,4.214904,-7.611353,-7.966824,9.061288,-1.687888,0.662408,-5.093531,4.821282,-2.358800,8.228978,8.372370,6.047465,-9.305263,-9.897917,-0.855664,1.537080,1.316871,-3.590355,-2.159043,-4.844038,2.004117,8.090320,-7.842184,-8.546529,2.465218,-9.917171,-3.648496,-6.909386,-7.207994,5.479324,-2.304959,6.040550,-1.435997,-7.429380,1.133129,0.084215,-7.738335,-5.627055,-2.231836,1.258803,-8.285376,-4.448959,-5.748651,2.928944,2.326883,6.736294,5.988768,-6.210062,6.179005,-5.376187,3.719331,5.899611,3.963198,7.099586,-8.179302,3.905181,-2.247000,0.709022,-1.464323,-4.720466,8.252206,8.051113,-5.225441,5.859846,-5.892864,-7.187945,8.939016,7.366554,2.685560,-1.752414,-2.022363,-9.194160,-1.997476,2.421343,-1.041142,-9.727284,9.754886,-4.666903,8.736159,1.116389,0.457230,-5.977312,4.518994], dtype = "float32")#candidate|2257|(1680,)|const|float32
call_2256 = relay.TupleGetItem(func_898_call(relay.reshape(const_2257.astype('float32'), [10, 14, 12])), 0)
call_2258 = relay.TupleGetItem(func_901_call(relay.reshape(const_2257.astype('float32'), [10, 14, 12])), 0)
func_1999_call = mod.get_global_var('func_1999')
func_2000_call = mutated_mod.get_global_var('func_2000')
call_2273 = relay.TupleGetItem(func_1999_call(), 0)
call_2274 = relay.TupleGetItem(func_2000_call(), 0)
output = relay.Tuple([call_2249,call_2256,const_2257,call_2273,])
output2 = relay.Tuple([call_2250,call_2258,const_2257,call_2274,])
func_2277 = relay.Function([], output)
mod['func_2277'] = func_2277
mod = relay.transform.InferType()(mod)
mutated_mod['func_2277'] = func_2277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2277_call = mutated_mod.get_global_var('func_2277')
call_2278 = func_2277_call()
output = call_2278
func_2279 = relay.Function([], output)
mutated_mod['func_2279'] = func_2279
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2367 = relay.var("var_2367", dtype = "float64", shape = (1, 8, 5))#candidate|2367|(1, 8, 5)|var|float64
var_2368 = relay.var("var_2368", dtype = "float64", shape = (9, 8, 5))#candidate|2368|(9, 8, 5)|var|float64
bop_2369 = relay.divide(var_2367.astype('float64'), var_2368.astype('float64')) # shape=(9, 8, 5)
output = relay.Tuple([bop_2369,])
output2 = relay.Tuple([bop_2369,])
func_2373 = relay.Function([var_2367,var_2368,], output)
mod['func_2373'] = func_2373
mod = relay.transform.InferType()(mod)
mutated_mod['func_2373'] = func_2373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2373_call = mutated_mod.get_global_var('func_2373')
var_2375 = relay.var("var_2375", dtype = "float64", shape = (1, 8, 5))#candidate|2375|(1, 8, 5)|var|float64
var_2376 = relay.var("var_2376", dtype = "float64", shape = (9, 8, 5))#candidate|2376|(9, 8, 5)|var|float64
call_2374 = func_2373_call(var_2375,var_2376,)
output = call_2374
func_2377 = relay.Function([var_2375,var_2376,], output)
mutated_mod['func_2377'] = func_2377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1419_call = mod.get_global_var('func_1419')
func_1420_call = mutated_mod.get_global_var('func_1420')
call_2454 = relay.TupleGetItem(func_1419_call(), 0)
call_2455 = relay.TupleGetItem(func_1420_call(), 0)
output = relay.Tuple([call_2454,])
output2 = relay.Tuple([call_2455,])
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
func_2131_call = mod.get_global_var('func_2131')
func_2133_call = mutated_mod.get_global_var('func_2133')
call_2477 = relay.TupleGetItem(func_2131_call(), 0)
call_2478 = relay.TupleGetItem(func_2133_call(), 0)
output = call_2477
output2 = call_2478
func_2483 = relay.Function([], output)
mod['func_2483'] = func_2483
mod = relay.transform.InferType()(mod)
output = func_2483()
func_2484 = relay.Function([], output)
mutated_mod['func_2484'] = func_2484
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2485 = relay.var("var_2485", dtype = "float64", shape = (11, 8, 4))#candidate|2485|(11, 8, 4)|var|float64
uop_2486 = relay.atan(var_2485.astype('float64')) # shape=(11, 8, 4)
output = uop_2486
output2 = uop_2486
func_2490 = relay.Function([var_2485,], output)
mod['func_2490'] = func_2490
mod = relay.transform.InferType()(mod)
var_2491 = relay.var("var_2491", dtype = "float64", shape = (11, 8, 4))#candidate|2491|(11, 8, 4)|var|float64
output = func_2490(var_2491)
func_2492 = relay.Function([var_2491], output)
mutated_mod['func_2492'] = func_2492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mod.get_global_var('func_2131')
func_2133_call = mutated_mod.get_global_var('func_2133')
call_2546 = relay.TupleGetItem(func_2131_call(), 1)
call_2547 = relay.TupleGetItem(func_2133_call(), 1)
func_1704_call = mod.get_global_var('func_1704')
func_1706_call = mutated_mod.get_global_var('func_1706')
call_2554 = func_1704_call()
call_2555 = func_1704_call()
output = relay.Tuple([call_2546,call_2554,])
output2 = relay.Tuple([call_2547,call_2555,])
func_2556 = relay.Function([], output)
mod['func_2556'] = func_2556
mod = relay.transform.InferType()(mod)
output = func_2556()
func_2557 = relay.Function([], output)
mutated_mod['func_2557'] = func_2557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2277_call = mod.get_global_var('func_2277')
func_2279_call = mutated_mod.get_global_var('func_2279')
call_2567 = relay.TupleGetItem(func_2277_call(), 2)
call_2568 = relay.TupleGetItem(func_2279_call(), 2)
output = relay.Tuple([call_2567,])
output2 = relay.Tuple([call_2568,])
func_2569 = relay.Function([], output)
mod['func_2569'] = func_2569
mod = relay.transform.InferType()(mod)
output = func_2569()
func_2570 = relay.Function([], output)
mutated_mod['func_2570'] = func_2570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2662 = relay.var("var_2662", dtype = "uint8", shape = (5, 11, 15))#candidate|2662|(5, 11, 15)|var|uint8
const_2663 = relay.const([[[-7,8,5,-7,-8,-10,1,3,-10,-4,9,8,6,5,-5],[1,-4,-10,-6,10,1,-6,-9,-8,-10,-5,-8,-7,10,-4],[-7,-7,-3,-1,-5,5,-10,-8,-2,8,-1,-10,-8,3,-9],[3,3,6,-10,-7,8,10,-4,9,-7,5,1,-4,2,-9],[6,6,3,-5,1,-7,-5,8,-5,5,-3,-9,6,5,3],[-9,-5,10,1,2,-9,-2,6,-6,-5,5,9,-4,1,3],[3,-5,-10,-8,-4,4,9,-10,6,-10,-4,10,-10,10,-4],[-5,8,-5,9,-1,4,-6,1,-10,1,7,4,3,-2,5],[-8,2,4,-4,1,-6,3,7,-10,-3,4,10,-9,-2,-4],[8,-9,7,8,-6,1,3,6,1,7,-8,-8,-1,-9,-10],[1,-6,10,6,9,6,-6,5,9,9,-10,8,-3,-6,3]],[[-7,6,7,-9,2,8,5,7,7,5,-3,-3,4,-10,-8],[6,9,1,8,10,-5,9,2,1,3,5,3,-7,-4,7],[1,-9,7,-8,-9,8,7,-7,5,-8,4,-2,-3,-3,-5],[-1,6,-7,-2,-10,3,7,5,-9,-2,7,-4,4,-8,-4],[-7,-1,5,-8,5,7,5,-8,-8,3,5,7,-10,7,-7],[-3,6,-9,-4,-7,4,6,10,2,-2,9,4,7,6,-2],[-2,9,-10,8,-5,10,-1,-1,-2,-10,-9,-2,-8,8,2],[8,6,-4,6,-10,-7,2,-9,-10,9,5,-2,2,-7,-3],[-4,-3,-8,9,-8,-7,-9,4,4,-7,7,-1,-1,10,-7],[5,6,2,-6,10,-9,-1,-7,-4,-1,2,-7,9,-9,-3],[4,6,9,-5,-10,-9,3,-5,4,-9,-4,-5,5,-8,4]],[[9,-1,-7,-4,3,7,-2,1,9,1,-2,-9,6,2,-8],[-5,-4,3,-7,4,-2,-4,-1,4,-2,-8,-7,-3,2,-7],[4,9,-10,-9,-9,7,-6,-6,7,9,-4,-6,-5,-6,-4],[9,-6,-6,-1,3,2,3,-10,6,-10,7,-3,5,-1,7],[5,-5,-4,-7,-10,5,10,-9,-7,-10,-2,-9,9,3,6],[-5,-5,1,-1,-2,-1,-2,-5,3,-8,10,-9,4,-4,8],[-6,8,5,-1,-10,-7,2,-1,-2,8,9,-1,9,-10,4],[-1,-1,4,-8,2,9,-8,1,-7,-8,-5,5,9,3,4],[-5,2,4,4,2,-2,9,2,-1,-5,4,-6,-7,-10,2],[2,9,-5,-1,-8,9,5,-10,-8,-6,8,2,-10,8,-3],[-5,10,-8,-8,-6,-1,-4,10,5,-5,-10,10,6,5,1]],[[-4,1,-10,-9,-8,-5,-9,-7,-5,7,-1,2,3,3,-9],[3,9,-5,5,-9,8,-1,-5,6,-1,9,-3,7,-6,-1],[-5,10,10,-4,1,9,-7,6,1,1,8,3,-10,7,-1],[3,-7,-1,-8,4,-10,9,-3,1,-1,-5,-4,-2,1,10],[-2,-9,6,5,-8,-5,4,-8,-1,3,3,10,-8,-10,4],[2,-5,-4,-2,-8,10,9,-7,10,-7,-7,1,-6,4,10],[9,3,-3,-8,-5,-5,8,-8,-2,3,1,10,9,-3,-5],[10,-2,-10,9,-10,-2,1,1,-7,8,-4,9,-3,3,3],[8,2,10,9,-9,6,-3,3,6,7,-9,-5,7,1,5],[-6,1,4,-9,1,-1,-9,-3,10,-4,3,10,-4,-5,4],[10,2,-9,3,1,-8,-8,-9,-1,10,8,9,-9,-2,1]],[[-2,-6,-2,-3,5,-6,6,-9,-7,-6,4,-10,9,-9,6],[6,10,-4,-9,9,1,-4,-1,4,1,-9,-1,1,10,10],[1,4,10,-6,-3,10,10,10,6,1,3,6,9,-5,-7],[-5,-3,-2,6,-1,-2,-4,-6,4,-10,1,7,9,-5,8],[-3,2,3,10,-1,10,-3,-6,9,-3,8,-4,3,4,-2],[-2,5,-1,-8,-8,4,-4,10,-6,-1,2,4,6,-1,-5],[-3,6,-1,-4,9,-9,8,10,3,-1,-4,4,8,5,-2],[-10,9,1,-4,8,7,-6,1,6,-1,-6,9,3,2,5],[-10,9,3,-9,6,-2,-7,1,2,9,4,8,-7,-1,1],[-5,2,-10,5,-4,9,8,-2,-1,6,-10,5,-4,-1,5],[10,4,-5,9,-6,-3,-8,-10,-9,9,-10,6,8,-2,-4]]], dtype = "uint8")#candidate|2663|(5, 11, 15)|const|uint8
bop_2664 = relay.maximum(var_2662.astype('uint8'), relay.reshape(const_2663.astype('uint8'), relay.shape_of(var_2662))) # shape=(5, 11, 15)
output = bop_2664
output2 = bop_2664
func_2667 = relay.Function([var_2662,], output)
mod['func_2667'] = func_2667
mod = relay.transform.InferType()(mod)
var_2668 = relay.var("var_2668", dtype = "uint8", shape = (5, 11, 15))#candidate|2668|(5, 11, 15)|var|uint8
output = func_2667(var_2668)
func_2669 = relay.Function([var_2668], output)
mutated_mod['func_2669'] = func_2669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_2683 = func_1912_call()
call_2684 = func_1912_call()
func_1704_call = mod.get_global_var('func_1704')
func_1706_call = mutated_mod.get_global_var('func_1706')
call_2696 = func_1704_call()
call_2697 = func_1704_call()
func_1074_call = mod.get_global_var('func_1074')
func_1075_call = mutated_mod.get_global_var('func_1075')
call_2703 = func_1074_call()
call_2704 = func_1074_call()
func_2556_call = mod.get_global_var('func_2556')
func_2557_call = mutated_mod.get_global_var('func_2557')
call_2737 = relay.TupleGetItem(func_2556_call(), 1)
call_2738 = relay.TupleGetItem(func_2557_call(), 1)
func_1157_call = mod.get_global_var('func_1157')
func_1160_call = mutated_mod.get_global_var('func_1160')
const_2753 = relay.const([-0.430383,-0.758583,-0.959423,8.265140,-1.953598,9.173383,9.328887,-2.086847,5.775413,4.029324,7.809222,2.027798,9.198258,-3.423577,7.700921,5.398471,2.594959,2.497879,2.575060,7.346373,-9.618020,4.475741,-9.218796,-9.361673,7.855120,-3.194246,-3.579068,-4.316708,5.241642,5.816158,-7.295292,-7.224630,-5.418141,-6.340888,-1.348056,2.755164,-2.598895,-6.084713,-7.241436,9.462871,-8.908374,-9.679731,2.861468,-7.901143,4.147563,7.581487,-9.485735,-6.089465,3.391133,8.664847,-6.423125,-0.802406,4.673487,3.197709,7.136723,3.011150,2.138785,4.799115,8.668598,2.268336,6.851305,-9.010117,-3.785575,-8.234534,7.492455,8.423284,-3.433962,0.234928,-5.146228,5.480060,5.686033,8.459051,6.718237,8.910709,3.322117,6.508710,-0.534641,-1.430889,-8.728330,-9.068952,-2.527481,4.667646,-7.890556,6.746329,-0.651005,-5.762148,5.620531,-6.737126,-8.327835,7.367362,-5.627259,-3.265082,7.571584,3.387640,6.169509,1.511238,0.413847,-2.647402,7.641838,-8.559278,5.503876,5.612805,-6.057494,5.388320,-0.326698,-8.956891,7.098674,6.374535,-7.486881,6.554680,-0.834858,2.418226,0.537022,8.560067,7.096007,-5.269565,4.207340,-5.061196,6.219253,-1.806545,-3.602259,-8.843708,-9.874133,-3.655059,-9.633877,-1.069029,1.093738,-3.231827,-7.456437,7.881666,3.779792,-5.511850,-2.538527,4.284578,-0.503279,8.190321,-9.717323,-8.328756,4.171939,6.247643,-0.244354,-9.832972,-3.156739,7.693193,6.129993,-0.463133,-7.152700,1.547456,0.982608,7.445095,-1.089570,4.031441,-6.906350,3.257874,-2.743756,-2.361697,5.699196,-5.787208,9.267205,-0.323562,3.812597,-8.823268,6.489536,-4.170481,-2.023949,-7.266868,-3.259171,1.291852,5.893799,-0.774563,-7.229467,9.803704,2.745820,8.071767,2.680659,6.747593,-5.072209,-5.984306,7.265822,7.589185,-4.130934,3.032312,6.000110,-2.043975,5.576147,-3.736188,1.258862,7.564650,-5.624031,9.704119,-7.103995,-8.450702,-2.506715,-0.168910,2.538424,4.863063,9.386996,-0.987942,-0.016953,-8.791111,8.909209,6.126867,-8.715951,9.584869,1.628844,-8.745563,-4.435841,-2.964077,3.532324,-8.918541,-9.000095,6.784789,-1.490979,-1.295074,-8.880379,2.003833,-9.389046,-4.463690,5.612379,7.022854,-8.638946,5.514316,-4.934837,-4.675631,-6.351678,-4.173614,-3.341484,5.530839,6.931133,2.976659,-5.105760,2.956174,3.141556,8.578353,0.224912,2.791050,-7.486948,-6.065537,5.559365,-9.210328,-6.822480,-0.604526,-0.115284,4.200785,-0.435483,8.088757,0.209422,0.655176,-7.799202,-5.840007,1.600222,-8.144235,-8.659981,-2.030658,0.101201,8.818925,0.333643,-0.954610,5.633594,5.574124,2.991961,-1.381502,6.495792,9.754520,-3.676624,9.657294,-3.756178,3.480456,8.744181,-2.892551,2.023341,-0.892031,4.234278,-2.086260,-2.489750,-1.506416,7.358782,9.389619,-0.168338,-4.779589,-4.064817,-7.966025,9.252810,7.589383,3.938988,8.611424,6.611973,6.148606,8.410542,-1.102854,3.458684,6.623591,0.067893,2.332523,0.308846,4.155840,-5.265888,-2.498308,0.284306,-8.593708,4.893437,0.693897,1.686750,-3.990959,5.897991,-4.349202,0.157755,4.587707,-6.542167,0.900921,-6.866778,6.484420,-3.664997,6.936149,6.925037,0.064893,5.927036,-1.798709,9.390896,9.078456,7.579673,-9.088756,4.017899,3.786699,-9.671718,-5.043754,5.297524,0.096344,0.924660,-1.623448,-1.524496,-5.349135,-8.909331,-1.135619,5.627251,-7.137601,-3.633901,7.184886,-8.352383,8.937632,5.559035,-1.290262,-1.709502,9.444058,-8.999650,-0.813842,8.623697,-4.559247,0.204187,3.336747,4.141983,1.531346,-2.248683,3.831420,-4.569485,-8.164154,-0.915680,-5.115473,-2.140586,4.681875,2.757855,-2.049548,-6.578608,5.232987,2.078506,-4.116461,-0.130435,-6.886038,-7.915932,-1.023229,6.908502,9.747275,3.338345,-0.151319,3.609942,-4.388668,1.697128,5.775193,0.181535,-8.968877,4.639329,4.012785,-8.309885,3.418464,-4.317381,4.609936,-0.430696,9.480494,0.167199,2.659974,1.002332,8.765801,-0.802784,-4.403224,8.422463,1.994916,1.693005,9.109903,-0.342541,3.083641,-1.061235,-2.419277,7.542501,-4.402262,6.641599,3.082408,2.743736,-5.991802,7.361778,3.192079,9.194487,6.052306,-8.613903,-1.991739,2.392417,0.539557,8.105305,-8.539299,1.990033,4.083181,3.229293,-7.251452,4.914171,-9.725907,0.745239,-7.304601,-3.987692,-7.677502,-6.812973,-6.087334,-7.407744,6.460001,0.043690,-8.216591,-0.555028,-5.272825,-9.267963,-6.634773,0.578273,-7.306450,-7.662608,4.582346,-9.655028,1.020455,-9.093132,9.444851,0.503110,-4.469435,-0.063812,-0.104424,-2.186919,-1.232394,0.241335,2.605878,-1.465191,7.836928,-9.460644,4.650446,-4.007700,3.253788,-5.260956,7.083995,2.641531,5.408193,-4.774306,-5.911709,-2.649635,5.800699,8.521165,-6.607588,-0.450028,-1.453898,-9.896564,-9.535405,4.943284,5.695975,-1.340493,1.274024,5.902154,7.548556,-4.805112,-2.889273,5.341046,-2.111847,-1.740773,-0.717836,5.154635,0.168575,-3.270399,-8.795805,9.133385,-9.328698,3.374555,0.449346,-3.514621,-0.588333,-6.301442,5.117221,1.102729,-5.933337,-9.744409,-6.998302,-3.739458,1.150965,6.465794,-6.102113,2.548437,-0.191202,-2.875130,5.029778,6.066621,-0.168963,3.974567,3.643157,8.174358,-9.604786,-1.627294,6.520893,4.289239,4.684160,3.282063,5.509582,-9.298592,5.970404,-3.901250,1.070173,-8.209970,1.197296,0.807975,-7.711669,0.037853,-1.439149,-7.703894,-0.745850,-2.976584,-6.776835,3.300480,3.420045,-1.429882,-4.422700,3.123925,-8.667701,7.185924,0.915160,-2.554809,-2.226186,0.890140,4.641261,-6.972528,8.557165,4.920520,-4.808857,8.166445,5.058153,-3.073860,-4.723316,1.129142,-6.761389,3.319774,-2.802771,3.099698,3.002957,2.327215,-5.371636,-2.580849,9.224918,-3.595155,-2.593758,6.253094,1.659297,6.161645,1.986874,-0.412546,-9.011103,-8.467724,6.309199,7.724113,-1.175098,9.765983,-5.605450,-2.271625,2.651945,-1.638731,-5.320073,6.868824,8.622496,-9.558604,-2.993423,-2.546631,-3.383214,8.661039,3.699576,-7.812128,7.837513,-5.602349,3.018900,4.068096,2.540563,-5.253706,1.146087,4.152173,-0.532281,-6.520081,-3.525437,2.784679,8.313476,-6.848974,0.399702,-5.403096,-4.122519,4.627422,3.157015,3.749803,-8.538290,-6.081234,0.445053,-5.506962,5.613077,-6.311143,-2.018729,-9.253086,-0.872080,-7.052515,3.739579,7.742704,9.186324,1.709363,9.398156,-5.966057,-8.558802,-6.830642,-5.031599,-5.594333,4.110660,-5.612467,-7.121259,5.820258,5.425426,4.714735,-3.604162,3.841909,7.763823,-2.335639,6.896353,-8.221233,8.418818,8.300246,4.524613,-2.434040,4.109640,-0.650458,0.932953,-4.103262,6.561534,-1.887381,-4.393301,-9.910765,-5.409404,0.748623,4.661575,-7.181741,-5.092653,-0.769597,7.776242,-5.586113,3.603162,-9.748586,-7.161852,-7.918862,-9.809963,8.923966,-2.752149,-3.342785,-2.029203,-4.681322,2.151810,-9.514494,-5.617256,-7.766289,6.069265,-7.805217,2.880667,-3.548234,-9.060686,-9.194015,2.730397,7.921166,2.629984,-3.622605,1.401355,2.015808,7.102427,-1.159164,-6.879242,8.860305,9.028597,7.674489,6.125797,-9.486927,-3.190614,-1.030118,-5.268757,1.800635,-6.843540,1.006120,-1.263639,-2.009802,2.485167,6.132276,3.402464,5.439111,4.272746,-0.989777,-0.182365,-4.940467,0.656812,-1.948951,-6.711341,4.840469,-0.871309,4.690183,5.060570,-1.714156,-4.779727,-9.557858,3.137282,0.134739,-1.273891,5.892511,-1.559524,5.250283,-9.561026,-6.347579,9.455126,2.446841,-7.137152,-3.685459,0.522895,-6.981245,9.436787,0.767868,4.056687,9.861849,-9.712364,-0.857569,-8.530011,-8.819682,-3.775816,5.538249,-7.128587,0.162198,1.531861,-3.714083,-6.874228,0.341898,-2.839934,-4.870961,4.037818,2.404703,-8.486154,-8.100293,-9.664628,-0.254802,5.242243,-5.609018,-5.884809,7.982925,-1.578869,-1.139169,-3.954254,-3.166256,9.270060,-7.592041,-5.972941,-7.527292,-8.562121,3.299477,-4.254886,0.403943,5.981529,0.441544,1.199162,-8.416398,3.579116,-1.360550,-4.026358,-9.596081,-8.266780,-0.420283,-0.233353,2.801282,3.079276,4.667858,-0.039325,-7.460772,6.189438,-8.901878,-9.763160,-7.665547,6.617381,7.840239,4.341755,9.345367,2.657436,-8.534277,0.023647,-7.783922,-4.464910,-0.962893,-9.428092,-1.795967,-2.566977,-1.142775,7.836697,-3.618477,4.576649,-1.552473,2.308424,-0.033086,6.071387,1.139329,1.270448,-8.171206,2.128941,-5.347415,1.534779,7.023354,5.007275,-2.142159,-5.948151,-4.864175,-7.163319,-0.377661,-2.908979,-9.121752,7.616933,-1.632806,5.511037,-3.456965,9.877721,-8.778047,-6.782660,2.593972,3.580239,-8.617235,-3.809250,-9.499410,-3.787841,8.454522,9.059541,-6.905494,9.365287,3.616921,7.545413,6.154016,1.434058,4.954998,-4.877576,5.941054,-4.562083,0.287935,-2.369946,-9.311922,5.281668,-4.002350,7.340858,4.078571,6.376596,-5.287796,8.007338,-5.413213,2.066021,-2.244093,-9.773282,-5.181688,9.063958,1.700523,2.242045,-9.998449,3.637103,1.144455,-9.786382,4.912490,-5.243046,-8.732195,-3.340222,-7.259778,3.523239,8.901343,-5.436387,-5.018176,6.809549,-9.277548,2.415820,1.419412,8.672027,-6.727854,-3.354096,2.810613,9.882414,-2.330911,-3.368836,4.510042,3.151613,2.251338,-7.883211,0.995126,-4.058618,-4.649252,9.260072,-7.565587,3.564202,-7.683261,7.117335,-3.347764,5.976262,-2.288857,0.300027,2.485797,-2.691608,-9.001144,5.075159,-8.871514,4.786315,4.319311,4.566151,6.752371,-1.829280,-8.781319,-0.587685,-4.351688,2.386434,4.870734,6.300841,5.335993,-8.224463,-0.522864,0.819421,3.113133,-6.562759,3.941787,-0.411865,-2.888267,-7.342079,-5.893861,4.511508,0.225390,5.079841,6.502801,0.435501,-0.742637,-5.223946,4.812961,-5.944970,8.333303,-9.135547,-1.472137,3.673653,4.041222,6.936631,-2.786256,3.544256,4.349057,1.293858,4.031573,8.500596,-9.028155,-8.227547,1.368010,-1.934414,5.689436,-1.657791,2.000922,-8.613324,0.112998,5.171569,-9.985307,8.239732,5.989077,-5.857811,-1.580398,2.906715,-6.933642,-9.466859,-4.166348,-6.539245,1.162031,7.210008,-8.033220,-2.108527,2.143986,-2.605763,-8.833128,8.397168,-0.669304,-7.302604,2.909111,0.277560,6.322139,7.155333,-1.968466,-9.532192,-2.356802,-0.295763,7.485800,7.218024,-4.840359,4.218597,6.383446,1.666539,-3.497355,-5.704826,7.724405,0.038628,-4.322751,-6.847370,-2.125100,-0.204132,-2.137178,-2.220875,0.592680,-1.329054,2.821819,-5.026205,-8.832621,-9.769723,8.530611,-1.807997,-7.691499,-4.339537,-4.160740,3.015694,6.184249,-5.530672,-9.351429,4.764289,-5.720313,-4.397455,1.330397,-6.205267,-9.924972,3.229665,-3.296845,-2.360088,5.231306,4.708949,3.028977,3.703213,-2.472561,-0.940595,-9.630123,8.767362,5.456609,-6.531882,-9.932406,-4.875540,4.623217,2.844335,5.896364,-7.060073,-9.016005,-6.882710,-5.874412,-9.925590,5.744186,1.442468,-8.227530,-0.770541,-6.851746,2.484019,-3.496835,9.103634,7.941197,9.066670,-9.787538,8.309718,3.844270,-7.596191,9.892679,-4.201000,2.843701,-4.133400,-1.011978,1.514349,7.194949,-2.411630,-6.908202,6.254404,-0.990691,-9.119010,-7.452221,4.628588,-3.962358,8.950340,-4.976620,-7.319889,-4.682273,1.953848,-8.421046,5.102663,6.981455,1.791853,-2.521702,0.657033,3.870477,0.595806,-2.472647,0.283793,3.655086,-9.493227,-4.103458,5.251601,-3.219172,-4.010325,-9.949647,-4.547649,1.862125,1.468643,5.639813,-3.327511,0.864850,-6.981615,-7.397760,-8.108921,7.187239,2.883226,8.736911,-3.040221,0.720822,-4.119437,-8.221425,-5.140575,-8.178357,0.963080,-2.067577,-9.038748,-7.666713,4.203663,-2.046388,-3.808545,6.778494,-2.399546,-5.915795,-6.423577,0.517884,7.393894,6.212837,0.761475,-1.582809,7.675906,-6.364327,-1.906703,0.713457,9.924751,6.480654,2.371712,1.284584,9.525202,-4.563995,7.774823,9.294295,1.904274,-2.469401,-6.181780,-7.740836,-3.048438,-8.078143,8.915035,-8.711463,5.343588,-6.936743,-9.343265,-3.432886,0.003654,1.594213,-6.448249,-0.964313,-1.932860,-5.932704,9.059289,-4.986150,5.048469,-6.173623,-4.272336,3.352313,-1.461693,-2.288625,2.950580,-1.924939,9.395610,-3.041724,-3.642677,-7.777634,1.026390,-6.656973,4.263529,-7.641386,1.050634,8.687806,-1.340182,1.716833,-6.605109,4.442556,6.138750,-5.029879,-6.563939,-7.885961,7.707985,3.976063,-4.425225,7.296882,-4.822046,-9.678306,-6.457486,-6.911696,8.782887,9.688131,0.613459,7.323069,9.312469,-4.322194,-7.404101,-1.513220,8.496025,8.002454,2.681789,2.868729,-2.872692,7.544387,0.407179,5.239157,-9.160009,-8.707029,-0.600069,-1.850433,7.515332,0.658784,7.936154,-7.014070,2.872200,-7.106972,-4.610508,-3.217724,-9.388262,-0.927633,6.453129,-5.791376,-0.305328,-8.342769,-3.000650,-2.945732,4.753550,-1.846320,-1.526293,0.597512,-5.494879,-5.694307,8.376962,4.877424,7.729526,2.023122,-1.027831,-0.500799,-0.351783,9.471265,4.340120,-4.837373,7.003425,6.362992,0.902925,5.421186,7.411409,8.008427,-9.720702,-2.440324,-1.533793,7.402723,5.995613,6.356334,-2.269337,-5.469997,3.494302,-0.130691,1.147799,-7.775734,-3.123715,-7.735101,3.594620,-4.521525,2.424561,4.789754,-5.815670,-9.944589,-6.344303,9.266558,-2.915432,-2.563760,-6.970720,-6.499940,0.779632,2.616258,-8.201958,5.375484,2.253839,6.363363,-8.373586,-8.804297,9.882132,-6.067374,-9.315965,-5.722795,4.939509,-3.531675,3.514250,-5.487666,0.691983,-4.101148,7.278411,-0.610435,3.805642,4.764544,-1.482445,-3.578158,-5.071224,-2.098181,-4.740997,4.462715,3.562651,-6.307167,-0.165203,1.355704,-6.022424,4.752382,6.008783,-7.345615,-5.821079,-3.764360,4.511504,-1.292935,3.558630,-6.394812,-3.072253,-6.342450,-4.190383,-0.887014,7.839760,-8.988392,-4.933668,5.730572,6.592950,-0.012432,-4.050200,6.171333,-5.813619,4.070015,-4.506068,9.696341,-0.269093,-8.334423,-6.945449,9.159081,5.175931,5.509070,-6.166283,5.924797,-7.927053,6.021359,4.895488,-9.313014,-7.132065,5.980107,-2.616786,1.982251,-6.936631,1.167852,6.513984,-0.010046,-5.843097,-1.576629,8.296979,6.597634,7.692158,-4.162490,5.062162,-1.980509,-0.051101,-0.647328,6.653106,0.184700,1.571632,-5.940585,-4.729646,2.901627,3.939386,4.411081,-6.800225,-5.651478,6.301279,-7.589311,-6.655884,-3.074616,-6.650886,3.376735,4.849939,-7.032839,0.802244,3.716891,5.589533,-5.293035,-6.240684,4.228773,-0.900687,-2.029639,-6.253033,-1.767460,-7.064799,-2.095342,9.900007,-0.140667,-3.824886,-2.303303,3.454975,4.053427,-0.875235,4.264972,6.899427,0.688756,2.901973,8.270295,-8.914123,-4.397932,5.375216,-7.427630,-6.502909,9.461653,9.212861,-6.938653,8.196612,5.670438,7.193236,-5.773521,-3.134229,9.386124,0.077683,4.404248,-7.738317,-9.108605,-2.636696,5.097558,0.793368,-8.055693,-5.371711,-3.924150,-8.720934,1.543496,-1.634904,8.816840,-0.516853,-8.300131,3.608371,4.919499,5.075591,8.377431,-2.709676,-3.537409,2.366375,-7.187367,7.499771,5.097587,8.485939,-3.094805,-9.033822,-5.145738,-2.022462,1.454477,-9.122955,1.340915,-8.197092,-9.860381,1.096204,6.274778,4.613506,-8.516899,-9.302969,-6.886136,3.628411,2.473042,-1.332078,-4.901888,0.301146,5.829404,-6.425581,6.113504,4.136760,-1.980534,7.971336,-8.670443,2.834075,2.362191,-6.321912,6.514797,-9.421013,-9.124062,-5.789654,9.596687,-3.283045,-0.237603,-9.379127,7.502125,9.032190,-1.448389,5.869659,6.154575,-6.201975,-7.799898,-6.355103,-6.734988,6.811503,-2.880126,5.217046,6.916308,-7.481431,-0.030554,3.858350,-8.835441,4.828687,4.978381,6.692528,-7.379525,-2.348060,9.315259,-2.676199,7.768892,-3.094575,-6.867345,-0.098720,4.691520,3.810833,8.081678,2.401912,5.422281,-7.539494,-3.557384,5.815957,1.045193,4.794818,-0.401554,-2.820058,2.313885,7.494281,-3.170357,4.116167,-3.740067,-3.799088,-6.179305,-9.506264,-4.038034,-6.855026,-6.423176,3.763053,6.420025,-6.291652,5.223102,-3.398924,3.446289,-6.377504,5.022823,9.586612,-4.089873,5.236444,-2.373417,-4.140432,-5.600850,1.890519,-2.888391,7.684885,7.174866,8.397739,-0.526997,-4.856144,-3.712825,-4.291989,-4.437869,3.048573,4.875279,6.892924,-3.494040,-4.491096,1.377043,-8.342725,5.839572,5.677839,2.247954,2.711547,-4.218315,-9.205479,-2.896376,-7.072375,-0.242890,4.700771,-1.053540,3.182233,-8.938717,-0.653313,0.289168,7.582315,-1.651993,-4.108119,2.938547,4.869900,8.912593,-2.892052,-3.334274,-6.640931,3.920430,-5.462578,6.919966,-9.037821,-3.895637,4.214744,2.515019,-1.682551,4.143564,-1.669768,-5.100913,3.245968,9.118360,5.602061,-7.590892,-6.883200,2.887135,-4.105414,6.883117,-2.236360,7.944179,5.634252,-1.130500,-9.261803,-5.933390,-6.267506,-9.550205,-8.221493,-9.177513,-2.392259,-4.533596,-9.751945,4.101905,-7.700579,0.726755,-9.377771,-2.505532,-0.603052,5.086228,-2.247449,7.421956,-1.579518,-7.057841,4.672256,-2.251269,-1.227143,-3.384259,-0.749919,1.076639,-1.499760,7.639648,7.454715,7.951354,-7.276975,-7.453278,-9.708159,-9.473835,1.494130,-5.385652,8.535860,-2.580536,4.930497,-8.229969,2.014023,-3.909448,-8.410967,-6.713752,3.336841,8.953872,9.443196,-1.286575,0.200649,-7.065657,-7.165239,7.863345,-8.466787,7.890807,9.606747,1.262165,0.419398,-5.244647,-9.285272,0.362263,-0.018500,7.309976,-5.882345,-1.813673,-5.497132,-3.961214,0.399401,-5.403447,-6.233013,3.807951,8.500826,-8.989117,-3.808565,6.135710,3.139442,-2.229054,9.617672,7.993783,2.263586,-8.887027,9.740170,-2.980351,-0.715904,-2.144178,-9.450828,-5.307753,-3.934351,-2.779066,-6.943901,5.093453,-2.766641,8.746172,-3.414416,8.266297,-1.834558,1.586662,5.340259,-6.525402,2.973721,-5.601140,-9.083519,5.420759,7.035122,4.352489,5.661053,4.853879,-0.113041,-4.295069,-9.949079,8.105236,4.949947,-3.013540,-1.980012,-1.376076,3.639296,-1.218424,-0.172396,-2.510555,2.502606,2.150587,0.355242,4.246497,0.476158,-6.143391,3.261480,1.301420,-2.027525,7.247990,-3.270685,-0.269414,-7.575424,-8.058140,5.064054,-5.036649,-2.518148,7.063808,0.962176,-1.683650,-0.295242,-0.573717,-5.050279,-9.711978,0.171119,2.622053,-2.572815,1.712898,-5.035969,2.335631,-6.460636,8.135223,4.186026,-8.480645,0.144261,0.229487,2.759559,1.105916,4.440049,0.557673,-7.872382,1.431766,-0.262866,3.537539,-3.499118,-7.359501,6.483456,9.080867,9.863202,2.973644,-6.689837,-9.860035,-3.809743,9.334594,-3.062660,-8.949358,-1.875166,6.964615,-5.636991,7.447664,1.422707,2.015439,3.328547,7.693064,4.858335,9.210365,2.806543,6.644150,-4.697823,-2.940539,8.068608,0.463924,-9.061279,1.561796,3.319810,5.040194,-1.957412,9.209842,8.308312,-9.148764,9.738656,3.445170,-4.402064,-3.275349,3.144160,8.206413,2.976317,-5.928024,8.754286,-5.965829,3.752270,5.636226,7.746227,5.065782,1.413005,0.018339,-7.361279,5.864454,8.659954,0.313620,-1.847727,-4.119502,8.045564,2.942616,-8.267466,3.198005,5.007278,3.417964,-7.063056,-0.082534,3.196147,-6.564319,-4.758916,-7.094076,-2.155488,-7.683979,-4.582386,-6.436071,-7.408668,-4.318024,-7.875315,-4.340750,-1.584183,-3.081428,-4.937477,-9.240726,-8.019401,3.523678,-4.162941,-8.707941,2.087963,-4.247582,0.608277,1.283685,-1.332737,-4.621280,-0.286075,9.870907,7.865676,2.439194,-3.526889,3.893712,-5.906131,1.312945,-7.388527,7.809200,-1.226724,2.191693,1.404512,5.939346,-7.538755,-3.780931,-5.086245,4.177598,1.821592,-9.298870,-5.881293,-4.194961,-3.173488,3.284916,0.338225,9.685981,-4.447873,-3.609526,6.368084,-2.105601,1.394467,-3.314812,-6.445403,2.837818,-3.249751,6.606705,3.396589,-5.168324,1.213142,-9.119478,-8.011438,-8.179070,-2.950435,-5.377744,1.310378,7.851560,6.695882,-2.458851,8.952400,5.537823,6.083256,-9.497194,-4.258772,6.411273,5.459757,5.314654,7.815964,-5.882755,-0.166291,3.332165,8.857914,-4.725274,0.206375,-3.198065,5.068967,-6.875609,-8.878849,0.374675,2.438543,-3.309947,8.179633,6.312789,-4.383581,-9.168813,-3.422378,-8.302453,6.556638,3.676084,8.719946,5.319631,6.322532,-0.515425,2.651823,7.948818,-4.164069,1.292475,4.240900,-6.189949,-0.501690,-0.612914,-7.540887,4.981442,1.810261,-1.168727,-8.477968,1.345208,-3.583524,-6.068183,-1.340799,-3.806717,3.683624,-9.506646,-1.052621,-9.066723,0.951709,-8.030433,5.480447,7.174395,-6.409969,-4.333128,-6.898701,-4.158662,5.574803,-9.833963,-4.897219,-8.892211,-1.025736,-3.949114,6.202539,7.813679,2.571819,-5.191868,9.969963,-8.180419,-2.664025,0.662004,-7.238279,8.390577,-1.341631,9.060599,-8.753816,-0.695307,-2.200146,-0.920636,-9.054939,9.324369,6.964924,-1.620642,6.544584,-5.017538,8.107061,-1.673119,5.614241,9.647652,7.370479,5.719968,-5.742169,-0.356860,-8.934056,-9.655284,8.516175,0.621009,-1.633687,6.269455,-5.129905,9.426239,7.372244,3.801716,0.631084,-5.694942,-9.273110,-5.299580,-3.776013,4.724377,6.983351,7.015227,6.395606,2.738265,-5.499743,-4.644763,-5.985114,3.091616,6.992915,7.478997,3.259480,-3.349748,4.461368,8.229860,1.771784,-4.048498,-4.795456,4.358296,-5.138664,8.427664,-7.842303,9.285791,1.750992,-9.098113,-6.020620,3.899781,-3.718379,8.448707,1.467316,7.734853,2.708504,1.218261,8.183364,-1.533132,-8.251359,-0.402698,7.783337,0.865643,-9.197661,0.952523,0.402762,6.529724,-9.532735,6.133136,5.349755,6.801611,7.997428,-5.189356,9.232718,-9.329420,6.979584,-6.329986,1.846046,0.858987,-6.481645,-1.268151,-1.648247,8.416189,-9.734071,-1.307142,7.464334,-2.682201,-5.047516,5.575123,0.539925,8.409711,-9.505029,8.667647,-9.051993,-0.964656,-3.542460,-5.037375,-4.838219,1.044793,2.681176,-0.787344,4.069136,5.157076,0.781686,-0.071577,-1.072595,6.839102,0.824675,-5.778507,-8.404379,-7.160235,7.173156,1.464314,-5.522391,-0.492940,-9.445942,-8.113918,-6.544612,0.599130,-2.897772,-7.215009,-1.907156,-3.698529,5.062971,1.551939,9.154733,-8.301019,-6.037471,-2.451989,-7.421203,-8.324587,2.064459,7.114923,-2.628930,2.433355,-6.898748,-1.159871,-0.803918,-9.900965,1.683221,6.757379,-4.740355,-3.713817,3.784068,8.667654,1.722032,-3.963203,2.921450,-3.641769,-4.806596,-4.812967,-6.209500,8.611181,0.801955,-7.009695,5.020275,6.454680,0.935241,5.681492,-5.613262,-1.823958,-3.942448,-6.008496,-9.351407,-1.971188,9.898542,4.569410,7.235632,-7.145629,8.159228,3.973122,-2.366913,-4.641877,-5.072391,-0.726902,-9.651673,2.403669,5.042464,-1.195250,-2.830952,-4.224886,-3.176821,3.090882,5.554736,-6.709796,-0.992044,8.997293,9.340423,-3.556893,2.445788,-4.432832,-1.614858,0.488803,-4.099939,7.390197,-4.491246,-6.781088,-3.011981,-5.910359,4.110866,-5.973257,-3.851647,-2.651545,0.993591,-2.643411,5.206551,-4.110873,-3.751113,9.583126,-0.538412,6.363392,-1.382446,3.456332,-8.774927,-1.677035,-0.354240,5.896696,6.336032,-1.621410,6.896757,7.129039,-5.266865,-9.027248,8.376148,2.495221,-2.760514,-8.991543,-7.406424,2.998346,6.578253,-2.792985,-8.605301,0.711523,2.318576,-6.715408,-6.004344,5.127729,-6.210935,9.434158,6.667960,3.673829,1.216006,-9.421336,6.120524,-0.983606,-1.578182,-1.189784,7.646839,-2.944127,-2.270077,9.439928,-5.842652,7.610324,-8.299447,8.184604,1.853059,4.363101,-6.386457,-8.686545,-4.798980,0.876235,1.789430,6.373487,9.202507,8.450916,2.931345,-3.899927,4.904949,-7.617126,-9.064244,9.325138,-2.497200,-9.043051,-5.085499,-6.087641,-9.336070,3.563860,0.388742,-2.137156,-3.234304,-5.734550,-4.741529,-4.105303,-0.249532,1.110550,-8.514482,-5.545689,5.590527,9.427451,9.405529,-7.875695,3.340943,6.949149,2.689073,0.999677,9.286987,4.007853,-6.683964,0.066998,-1.955942,1.417632,6.687312,7.120585,8.822850,3.062973,-7.410043,-4.075089,2.118576,-3.308028,5.499812,5.472380,-5.178528,-6.842458,-5.779276,7.507144,-8.044305,9.112154,9.578396,-8.267177,7.927545,8.598646,-8.800735,-4.962099,-7.192369,-2.598237,-4.235393,-2.398505,-0.581510,-9.371255,5.855165,1.757876,-3.852944,6.177969,3.922352,-0.439403,9.681472,-9.163547,5.024004,-4.246326,1.072567,5.409367,-9.496025,-1.359275,-0.472113,4.034832,7.099547,0.322347,1.189587,4.102525,7.608656,4.372533,3.766203,-1.932941,-7.915943,-0.318007,0.676169,-4.717279,-2.601480,-0.044842,5.655899,-7.441317,-8.588289,-0.873822,-4.278624,-3.426438,-8.802285,0.274727,8.811325,-6.473492,-5.044587,8.067310,3.566446,6.407039,9.847764,-4.815689,5.370285,6.184454,1.741180,2.498870,5.662115,2.271715,6.628053,9.162455,-7.390519,9.497252,6.778811,-2.256885,-4.117838,-8.653741,8.126072,-6.769541,2.020627,-2.064079,8.238877,-9.615503,6.597549,-9.413025,-0.362687,0.580372,-8.851724,8.358369,0.170128,-6.071721,3.217721,5.720011,3.026949,4.422710,4.154369,9.781069,0.498602,8.051357,5.994830,-1.617183,-5.975897,-0.951303,-2.215043,-7.907013,4.524738,7.526314,6.667930,6.257772,-8.042693,1.513347,-6.114531,-4.871908,-7.112394,-5.206979,-2.636433,-0.091580,-3.548221,2.429206,-0.380312,8.418752,-9.946256,3.312801,7.897964,-4.168267,0.250185,-2.305007,7.791655,-7.869120,-3.088769,9.205449,3.581395,1.520569,4.175250,-2.526302,-5.954602,4.378207,-9.825445,-6.925809,-8.413462,8.399536,-1.759466,4.600931,-7.815493,-0.736912,0.752207,4.352217,8.695873,-5.475421,6.516736,-5.772214,-1.547309,-1.248353,-2.291814,2.048169,-6.159091,7.427107,-7.205370,-3.704054,-3.524992,6.540110,-3.612717,-6.608357,-1.358612,-2.477431,5.399139,3.342178,9.500143,-6.540802,9.759367,-3.095965,-3.106901,-3.129191,-4.751372,3.748400,9.960262,-8.898283,-3.159494,6.934334,-4.031757,-6.398282,4.393036,4.870760,-0.048999,-4.639837,0.922457,1.712659,-6.771802,-0.043112,-0.583507,4.144128,7.243087,1.833283,-3.876215,-5.745082,7.505723,-6.059538,-4.394682,7.135738,2.909587,-8.863710,-4.790312,-5.590934,-5.632845,5.739600,9.545084,-9.502307,5.013949,-6.016961,5.667830,-8.394574,1.172629,3.355495,-5.363349,-9.600936,-0.794223,1.125878,-3.018191,-7.047652,-1.319979,6.268882,-5.904005,-3.805114,-9.977085,-0.970973,6.859381,-4.988087,0.209286,4.125089,-4.305067,-3.984001,-5.410342,9.225605,5.113677,4.399285,0.561111,3.133160,4.344568,6.780830,-1.994952,7.699658,-5.844066,2.957430,4.023967,-4.640665,-5.939931,-1.188508,-8.417920,-5.916137,4.796150,4.791938,-1.177875,0.642926,6.566148,2.697636,-5.533806,1.124547,-5.182237,-0.152556,0.039719,6.196590,0.769042,7.792162,7.598513,-9.540338,9.088550,-0.316988,-9.100454,6.969455,-2.608076,-1.743787,9.905928,-6.941086,-1.809479,6.942723,8.314131,6.721525,0.452645,-3.217198,-0.964804,2.810389,-1.745960,-7.083566,4.687307,-6.272565,-1.911277,-7.192479,5.162937,-2.883060,-5.033338,6.529506,-0.818817,-0.548606,5.214505,4.510140,6.112773,-3.357639,-8.079709], dtype = "float64")#candidate|2753|(2640,)|const|float64
call_2752 = relay.TupleGetItem(func_1157_call(relay.reshape(const_2753.astype('float64'), [16, 15, 11])), 0)
call_2754 = relay.TupleGetItem(func_1160_call(relay.reshape(const_2753.astype('float64'), [16, 15, 11])), 0)
output = relay.Tuple([call_2683,call_2696,call_2703,call_2737,call_2752,const_2753,])
output2 = relay.Tuple([call_2684,call_2697,call_2704,call_2738,call_2754,const_2753,])
func_2768 = relay.Function([], output)
mod['func_2768'] = func_2768
mod = relay.transform.InferType()(mod)
output = func_2768()
func_2769 = relay.Function([], output)
mutated_mod['func_2769'] = func_2769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_2811 = relay.TupleGetItem(func_970_call(), 2)
call_2812 = relay.TupleGetItem(func_972_call(), 2)
func_1486_call = mod.get_global_var('func_1486')
func_1489_call = mutated_mod.get_global_var('func_1489')
const_2816 = relay.const([4.099953,-6.793087,-4.165157,-3.450785,-3.958048,9.826515,-2.522531,6.249396,-6.911957,8.922843,-4.089856,6.986513,9.563451,0.145567,-4.181128,9.442552,6.646332,-1.550006,1.167431,-8.303332,7.721049,-4.684296,5.472145,-0.057002,0.521792,4.959362,-6.539328,-7.236937,-8.451219,-4.279741,9.190445,-1.783665,2.135675,1.164150,5.388662,-5.125224,2.599840,-6.508709,0.183892,-7.959396,-5.338977,-5.232268,-5.351609,-5.975265,7.893973,7.367941,3.107830,7.540613,9.101335,0.400711,7.985762,9.326559,-9.459846,9.107898,2.337086,0.100190,8.748481,-8.564936,-1.518805,-7.354622,4.674751,1.175347,1.071787,-2.230376,6.704609,9.703461,7.254780,6.997405,-1.292043,1.261959,2.846349,3.418109,5.301030,-8.266791,1.739630,5.448266,2.275898,4.690641,6.599962,9.977786,8.324793,8.475224,8.704369,8.277321,1.551661,7.203007,5.028055,7.491277,-9.306763,-9.950462,-9.442005,1.569485,-2.060238,-6.667577,-0.707213,-6.496658,-1.815633,-0.609580,1.816829,6.243555,0.367160,7.529797,-1.053365,3.988210,-2.843791,-4.526508,0.829937,-6.855508,-4.696743,2.993130,-1.909606,-0.271839,-0.717325,1.011121,-8.938325,-6.781998,2.648750,-3.195146,5.985604,8.754503,-3.757807,-0.251146,5.657448,1.119950,-8.165511,-4.376429,1.681576,2.094235,8.403609,1.137994,-2.863849,3.416795,3.752104,0.837298,3.118826,-8.018482,-6.866949,9.950719,-4.976838,0.213017,-2.332126,0.125038,-1.059780,0.151709,1.892041,-5.471435,-4.918728,-6.752240,7.952748,-1.019944,-7.107543,-4.452500,-5.937478,-4.586637,6.463403,4.710681,8.290273,8.327599,4.402009,9.996257,5.927632,-1.240741,-8.829303,2.127572,-1.246927,-7.247746,-6.050951,4.991641,1.003314,1.112480,5.203336,-1.448617,-7.771073,1.436729,-0.500588,-0.897605,-8.572613,0.022015,6.182433,-8.624670,3.984579,-9.392471,-4.691254,-7.311358,6.353796,-9.053742,-6.239166,1.596935,-0.713112,-8.446590,-7.168716,-6.960483,-6.564569,0.116016,-1.430735,7.061011,-9.671426,4.323391,-8.667526,-9.029801,-4.634175,-9.435006,0.081598,9.095702,-9.477312,-7.666654,-1.986866,2.840987,3.933156,2.810816,7.094168,7.791237,-1.907639,-1.725052,-4.343143,5.741133,7.882539,4.666595,1.307488,-4.309539,-3.365027,-8.738686,1.023575,5.523370,-2.122975,-4.224162,-2.839171,-6.984334,-4.932647,0.393518,8.478273,2.371118,-3.203655,-5.093876,9.725786,-1.275957,2.526709,1.407567,-1.186005,5.473998,2.501179,-8.486741,8.037668,-3.973599,4.872946,-8.801810,-8.774720,7.548643,-5.752107,9.735269,-7.339024,-9.702053,-4.060795,-4.461906,-6.288553,-5.452268,8.802189,7.457875,0.268961,3.214783,1.575869,2.822211,0.804830,5.828023,-9.492614,-3.667521,-4.549251,2.050263,-6.676855,6.368837,5.755389,-9.660721,8.542134,-8.082276,0.012084,5.456269,5.411570,9.184368,-8.073624,9.717843,0.043491,9.373591,-6.694595,-6.074741,0.609689,3.793594,5.615114,2.054930,-0.365949,3.232336,4.993452,-6.629715,-4.957098,-3.885247,-2.138264,1.673146,8.106498,2.437192,4.127471,-7.895335,-9.263701,-5.442512,9.661123,-8.515267,9.215101,0.289463,-4.151136,3.765344,0.729844,6.799800,7.135646,5.516392,-8.871797,-9.535782,8.576334,-8.575087,2.430187,0.001893,-2.764393,-0.954614,-4.372813,2.334852,4.520358,8.928064,-6.928140,0.521035,0.347753,-7.773749,3.179854,-5.306431,6.074137,-0.958629,2.438854,9.244000,5.596962,8.133665,0.641552,5.139879,6.858435,-0.271684,6.986839,-6.447992,-4.806617,-3.555633,8.425600,-0.796228,7.349606,8.267265,2.990211,9.164007,-4.970387,-6.307851,5.765407,5.239601,-3.342705,-9.534969,0.008754,-2.507259,5.399786,4.873867,5.073426,9.315214,8.445752,9.470561,7.662376,5.572693,4.292089,2.636375,7.626920,-1.622436,-4.918239,-1.557440,9.766581,-5.356076,4.771450,8.258388,7.246139,-8.596932,-3.986707,7.057526,-2.965897,4.660294,-6.545974,-3.932110,7.643641,6.569836,6.392901,8.929026,9.023680,3.880167,-0.271673,7.843288,7.639123,-3.706489,-8.697882,0.396517,-3.642704,-5.964460,8.685605,5.359046,5.490821,0.752450,-8.714231,2.312348,-9.053011,-9.777201,-2.675946,-2.762093,2.829135,6.318114,7.707201,-6.192141,0.327526,-4.158595,3.364368,-5.517739,3.945393,9.659930,-9.179245,5.440292,5.987721,8.522480,1.461595,0.940645,-8.123701,-7.532516,9.028491,-0.847159,-8.158114,-4.524520,-3.679063,-5.212236,-0.984070,8.707253,9.924122,5.752747,-1.260897,-6.452449,-2.136756,1.707460,-7.963469,-8.537702,-7.938356,-0.756059,-2.120926,1.278168,8.640989,-5.239874,1.269324,5.551720,-7.456535,-4.912404,4.569107,-0.586771,-3.862830,9.152239,-6.651877,6.992190,-6.981974,8.912208,-3.965781,0.705633,-8.896462,4.232417,2.434259,-1.019935,0.986917,-5.989667,7.634871,-3.244345,-3.136698,-9.328736,-8.611565,-4.253737,-5.648059,8.527954,-9.871165,-3.012156,-6.333933,-4.541434,-7.748845,1.906506,8.224469,0.504516,-8.644256,8.562101,5.133264,5.561531,2.778189,-4.845339,0.320258,-6.607408,-5.115340,4.269138,-6.697715,-1.166839,-1.065692,-7.289253,5.055924,4.933755,7.488728,8.521059,-7.745060,-8.258769,-8.870853,5.736072,-8.333782,9.409237,4.619494,3.704594,-5.650764,-8.498401,8.592692,8.173471,-0.299549,6.470597,2.016553,-9.429900,9.717623,0.871669,3.045216,-0.966384,-0.402139,-3.189132,-3.432051,8.772767,9.105815,3.868450,-1.496469,-3.468782,1.441007,-3.451578,-5.777991,6.012668,-1.361281,5.090572,4.661680,9.477875,1.555997,6.092755,-5.707375,-0.040143,1.346590,-7.734693,-8.439044,-4.386108,-3.212116,-8.357326,-9.415803,6.064566,-9.560812,-2.118580,-8.270121,2.109276,-6.408388,0.057196,7.753619,-1.294547,2.571984,-5.152535,8.203970,-4.020445,-4.446383,-5.657941,-7.786949,7.947559,-5.598203,-3.399731,0.682194,-4.640351,7.937187,-6.816268,-8.832299,9.997330,-4.871469,4.527760,-2.859697,9.053528,3.462211,7.520959,0.724637,-1.759366,7.061335,-0.475509,3.160088,-8.410953,-4.210185,8.283156,9.412730,8.350667,4.722175,-4.995151,-4.276496,-5.460665,0.126886,2.349026,-0.094252,4.324829,-0.331641,-4.509231,-5.787672,-5.864979,-3.320002,6.311071,-0.838677,9.673190,-2.331043,-0.811924,0.751816,-5.076087,-0.592311,-4.747810,3.583071,-6.258139,1.416573,8.021296,0.677116,9.757443,-9.668730,-6.541775,9.650860,-1.290691,7.113960,-5.029870,8.969279,8.125527,-9.175780,-7.306372,6.376038,4.241720,7.380675,7.002766,7.657543,-6.708679,1.254166,-1.746203,-7.094967,-7.698888,0.705890,3.824097,2.470086,1.490255,-7.056303,-8.975581,-4.064617,-8.062431,-6.169572,8.458432,-6.322457,5.741019,-8.872920,-5.215848,-9.734513,-9.992507,9.667078,-6.033370,-6.883326,-4.098553,8.339879,9.057165,4.051489,-4.102543,3.136152,0.218158,3.133432,0.269989,-1.173333,6.189650,6.257297,3.036692,5.563293,0.494718,2.585258,-5.544511,-1.370448,-1.869091,4.587892,-1.478246,-2.469702,3.109985,-1.355454,4.478818,-3.025529,-8.628862,-5.373194,8.950015,3.568568,-8.134177,-9.269768,-3.597360,-3.402874,-0.697908,5.002470,-0.686412,-6.895912,6.174242,-2.535536,-8.939687,4.762479,-8.626463,-6.669683,8.373063,6.631667,-2.721152,-9.909073,-9.226552,7.026904,3.959018,2.250402,6.032586,9.957074,7.492381,5.850272,-2.591258,-8.099766,8.766735,-9.833158,-7.621944,-3.125965,-6.468227,0.051930,6.058596,2.235878,2.918010,-9.326559,0.262521,-1.608758,6.924424,-1.548508,-2.912863,9.411844,2.261333,8.550393,3.914923,-6.699818,-1.317693,-7.532447,-6.226969,-7.931703,8.955475,-3.423731,-0.207981,3.836465,6.747007,-4.128015,-6.214633,4.601839,8.947062,4.955659,-1.859355,-5.199578,-0.726481,-2.351224,2.907770,-8.124502,1.388001,5.852065,8.676488,8.632011,-6.809432,2.862779,8.341380,-2.790233,7.057025,5.303896,0.039136,-6.326971,5.535875,-9.069395,-2.206520,6.141460,-3.808878,9.217855,6.316845,-9.460731,-9.850224,-3.175199,-6.114398,4.839060,-6.138651,8.500875,-7.322868,8.675387,-4.349305,-2.643922,5.741810,-6.050635,-7.969372,8.738961,-9.751334,9.530105,6.295766,4.125615,-1.177266,2.660965,0.433072,-6.652952,3.825752,8.321612,-0.734828,-3.414703,8.469657,9.831273,-0.404940,5.134103,-0.386998,-8.711107,-4.998544,4.711885,-0.120099,-8.719288,0.190610,3.516900,-4.212816,-5.910119,3.000827,-6.715233,7.525048,-6.901199,7.709189,-6.241159,6.836926,3.893232,-9.690629,-5.697355,-5.897766,0.630538,-3.745746,-0.781639,2.089176,5.289907,0.395524,-7.020619,6.100068,-6.622918,-2.298021,-1.412797,6.809606,-4.402328,-3.481041,-3.260533,8.664955,-9.191683,8.189098,-1.520755,3.011606,9.973302,-7.662524,0.824059,-4.991975,-4.113143,-6.332915,-6.476602,-3.320030,-3.665273,-9.726359,6.463452,-2.940510,2.748545,-8.330215,-3.897264,4.468439,-4.834772,8.236701,0.529514,-1.175470,6.378026,-8.592441,-7.039000,-0.795187,8.275335,-3.375554,-3.802653,-9.924641,-0.033128,1.933004,-0.210749,-1.926462,-2.888738,-5.518385,8.108592,8.698320,9.505720,2.770663,0.673213,-4.113495,-1.899177,6.674773,0.493073,-8.505880,3.848462,9.861477,-5.755981,-4.231213,1.815846,-3.958020,9.434174,1.580142,4.285211,4.513605,-0.462275,3.622145,-0.028426,8.005893,-7.334713,9.720727,-0.891146,4.642318,-1.629623,2.320377,-4.022699,-3.379805,-4.397628,-7.350232,-5.750395,-3.481445,-6.398175,5.493787,-5.682040,-0.887458,-2.126803,-1.278630,-7.672389,3.170923,-0.438544,4.062598,-6.324693,-6.560881,9.248409,-8.494524,-4.046319,3.963626,-8.671415,2.154988,7.807260,9.661422,5.632016,-0.754062,7.731935,-0.026950,4.654101,-9.700645,-4.950206,-9.089157,-0.189320,8.797701,2.140170,1.429545,-7.472923,-3.713183,-8.786784,5.055146,-1.081282,-4.052068,-2.202740,1.747544,-0.724335,0.837545,-2.413940,-5.025366,3.285496,-4.678317,-8.207341,-5.896586,-0.103256,7.989666,0.211980,7.544868,-4.559309,1.632140,-1.950909,-6.600925,4.717747,5.429649,2.991200,-1.359011,-2.880498,0.402172,-9.295257,5.895563,1.231672,2.894129,2.981386,-2.168374,-5.301086,-3.864028,-0.688109,1.667574,2.398901,6.664289,3.504579,2.983163,-2.803401,-6.450714,-1.935150,-8.382995,-1.840008,-7.329722,-4.414096,-9.045979,0.853835,5.637659,5.204042,0.103754,-3.894038,-9.090993,-1.685336,9.312485,-6.856594,9.448982,6.551002,-7.724942,0.072439,1.500826,8.613977,2.158999,8.367219,-4.702265,4.764975,4.020995,1.972117,9.819359,3.796430,-7.096216,4.251156,-6.285452,7.735821,-3.194237,-4.932194,-2.149291,3.027899,-1.616188,0.845465,-1.580790,-7.689889,-7.221990,7.197126,0.817030,-7.193523,-8.746653,8.512985,-1.090871,-0.607709,2.311445,-8.138154,-0.881773,6.190925,-0.030185,-8.632247,-9.134633,-4.187878,-1.898170,-8.866544,-9.283846,8.761441,-6.726552,-3.747028,-8.949185,-1.136795,4.099161,5.116499,-1.127859,-3.307599,0.269560,4.960111,5.008677,-5.789764,5.620649,6.902849,3.207669,7.893889,4.656738,-9.802364,-8.024591,5.163446,-8.472969,3.789304,-0.743174,1.510875,-2.416539,6.119089,6.360126,1.788802,-0.703713,-7.373045,-0.612846,-3.172358,9.125104,3.938998,3.272556,0.500103,5.978654,-4.950718,-9.414199,-1.991838,0.498198,-2.148843,2.624473,8.477358,-8.393798,-9.505598,8.553359,-1.305514,8.663555,-2.924758,6.042831,-7.193968,0.210690,-8.031229,3.599207,-8.888788,-5.934650,7.266490,4.362931,9.370145,-3.991808,-7.293892,-1.805140,4.920700,-0.809537,-2.916287,4.139387,-2.612553,-2.919441,2.717036,1.026363,-1.863621,-5.336186,-9.381958,-6.805700,-2.401600,4.511203,6.135931,1.201939,4.704101,-6.943838,6.770299,5.613708,-1.286656,-9.159233,3.919522,-1.425032,0.169642,7.052432,-8.349833,-7.187367,-3.586592,5.660920,2.424688,-5.478710,-7.951986,0.129585,1.670956,5.663343,-8.954725,2.672761,-8.877538,7.659296,-2.361668,8.506325,-5.148065,0.767345,5.938674,-3.243210,-5.080533,2.097547,-4.374050,-0.675025,3.117563,1.322285,-6.674686,7.068949,-4.667874,-9.113637,5.498113,1.674381,7.236817,1.087116,5.126019,-0.110104,-6.032821,-0.303597,-1.149835,-1.592996,5.557151,4.409958,-4.150547,-2.515880,0.907358,-7.320088,-2.813876,-9.531253,-5.037705,-6.020379,-7.651590,6.799135,-7.610046,4.326329,4.076374,7.528879,7.939618,-4.123752,9.588548,0.765882,6.024028,-2.058721,8.934640,-9.317168,-2.414520,-3.289927,9.492456,8.086875,9.088440,-2.151567,9.153791,2.614362,-3.736568,-1.883030,-6.874058,-1.281287,5.051832,4.214978,3.781949,8.348576,-5.480520,-3.581145,7.580510,-5.509749,-5.045732,8.234699,-9.546216,5.599329,-4.454852,-2.984510,9.944627,7.456405,6.408133,9.497409,-5.969173,-6.487776,-9.116753,-5.035881,0.978047,7.867978,9.770774,0.934724,0.115616,-2.856282,-9.926423,6.567454,0.270290,7.670745,9.452200,4.834134,6.683730,2.331203,5.998973,6.947426,-4.255521,-3.234192,-1.924204,6.473619,-8.162140,2.715302,-2.957050,-4.673723,4.786685,5.910011,7.452866,-6.522066,-5.439874,-5.196191,3.857603,-4.471643,-8.368514,5.107314,-3.814098,0.069566,-0.851387,-5.723971,3.937068,-8.559162,-6.413822,5.385683,8.930611,-4.359378,7.057382,3.350029,-4.625760,-3.048528,-7.902111,8.092855,-8.585953,-0.770697,-2.128925,-0.594752,3.628686,-8.238432,-1.034470,9.358580,-7.222391,4.394917,5.183378,-2.530850,5.841552,-4.795483,0.325437,-5.772865,-2.505139,-1.222748,0.105018,-9.270048,-7.548605,-5.871022,3.435661,-8.494135,2.917519,6.299787,-7.880309,0.709360,3.809075,5.035071,9.488155,-4.697876,-3.860028,-9.778691,7.838573,7.754920,-0.271846,-2.454940,4.360339,7.557764,9.490201,5.973240,-9.036798,5.565847,1.613949,-1.925212,-6.824847,-8.334975,-2.383542,3.153157,-1.038185,5.995108,-7.656599,-3.897151,-0.605751,2.688904,-9.604820,1.647279,8.865388,-2.924845,7.803496,3.645169,-9.678334,1.800447,8.940645,-3.779756,7.084014,-1.245918,-3.151415,4.012521,-2.618378,-5.620461,-8.832773,4.705514,-4.659538,-3.365515,0.601289,1.220836,8.524002,-7.108749,3.503429,-3.239908,-8.067692,3.177375,6.292883,6.792899,3.156563,9.900827,6.883700,3.718068,-8.823092,8.417675,4.140446,5.130513,3.001108,6.186785,5.802436,9.741984,-7.049772,-7.007904,-2.802014,1.280395,0.624665,6.638345,-9.069061,-4.278655,-7.648659,-4.523207,-1.080670,-8.934033,2.554329,0.541217,-2.175320,-4.005194,1.032196,-7.788378,-5.462838,7.186427,-4.807161,-7.321620,0.607486,-2.423316,-0.933171,7.762491,-9.735032,3.144796,-2.463152,-6.965583,7.098420,9.323855,3.910401,-4.528751,-8.058007,5.393841,-7.641312,7.371657,-6.303264,2.084538,-4.663782,-2.013945,2.831432,-5.046381,-7.057516,-3.039943,9.213907,-5.671413,6.564862,-9.450126,-5.704435,7.758234,9.978797,-5.381658,-3.537063,-4.736484,-4.968978,6.112918,-6.592535,3.533415,9.328567,5.076945,-3.433764,9.088605,-1.920836,0.955040,-2.143927,-4.774168,3.026513,7.990246,-8.232502,-7.814970,-9.638040,-9.745456,7.022447,9.559339,4.649532,0.102558,-7.251455,-7.729423,-3.664705,9.120902,-4.610449,-9.992519,-6.177377,1.288496,0.880510,-1.626654,4.142080,5.309267,-5.868931,6.960487,4.745617,1.763794,-8.537196,-9.109837,2.396683,4.290709,0.197567,0.468424,9.321609,0.847234,-2.935601,3.599170,-8.473932,-2.228517,1.314240,3.193731,-8.413983,1.631032,-2.670205,0.548354,9.662238,9.025580,-8.388746,3.024529,4.861087,8.729165,-6.970248,3.965037,9.813619,4.964490,-1.927836,6.997024,-2.800008,9.264160,-8.309101,-1.340168,8.085492,2.685240,1.510302,6.197016,1.612594,-3.438444,5.126982,-6.202061,-6.447232,-1.688021,-9.179434,4.736143,-4.440217,5.562204,-2.888914,-1.773735,3.509672,1.344558,-9.754990,8.077411,5.659034,1.298927,-3.923424,6.720520,-9.038889,7.434715,3.287952,6.615347,0.867507,4.450952,-2.069739,2.517412,9.742414,-5.394878,0.008004,5.103360,-3.016754,-5.108078,-1.229816,8.176155,7.014047,-8.490406,2.983307,-2.549149,-4.090805,-2.975666,5.842705,6.592477,1.625720,7.142081,0.085384,8.641772,1.950944,-4.290422,-0.829804,-8.834425,-5.427357,-3.598141,-8.217563,-2.060689,-3.555792,-5.715524,-4.913253,-6.982356,3.794037,6.061521,-4.953067,-7.179969,-4.467902,-3.044348,-9.923306,-3.696028,6.904976,7.077126,2.278527,-9.502535,-1.985472,5.267339,-8.097635,-7.234074,8.379236,4.214189,7.301979,-6.889786,-1.087557,-7.283307,0.446851,-6.840522,5.168674,0.203183,6.786542,2.451318,-4.265593,6.499296,-0.529674,-0.151889,0.188158,-5.610661,-7.493333,-0.728769,7.922496,6.181358,1.885997,9.893354,8.659477,5.822343,-8.474768,6.759041,4.794286,-2.752297,-0.758269,-9.082304,-9.226782,-9.076489,3.776986,8.090288,4.031971,5.363152,-9.935145,-8.254585,5.756859,9.426819,-7.708954,-7.131544,0.002585,9.966995,-2.926669,6.786021,-0.742762,8.118081,-3.104241,-0.648694,1.790125,-9.438192,-1.146237,-8.521771,-5.706278,-0.845118,-7.441377,-1.730581,6.013959,4.446136,8.581120,-7.917566,0.705310,1.160047,-2.376289,3.815133,-2.159094,-5.574788,-4.694619,-7.585052,-3.881585,4.709888,-8.005261,-1.359088,-0.217424,5.974332,-3.565984,6.651588,6.540234,1.249303], dtype = "float32")#candidate|2816|(1680,)|const|float32
const_2817 = relay.const([-5.467696,-9.722978,-6.074358,6.582638,6.913472,4.795357,-7.312643,9.037712,-1.342368,9.616853,-1.500811,-1.378164,1.917702,-4.468550,-0.445631,-7.283149,6.094773,-5.652545,-9.492657,-5.189424,-7.051936,9.646170,9.120856,3.133039,7.588766,-3.319353,-2.603641,9.102052,-2.662482,-9.634975,1.081475,7.995802,2.142459,6.397212,1.040164,-8.017946,8.288193,-5.067372,-9.361941,-6.171263,-0.452424,-3.867629,0.793783,1.448538,9.517420,8.375591,-6.646930,5.408077,-6.907471,3.945902,-3.759265,5.593370,7.697990,-3.506654,-7.232540,0.743071,6.767694,9.628098,6.355342,-4.000740,-3.778347,-4.363803,-2.362458,-9.753803,-7.660265,-7.010356,4.643873,-6.920290,4.478928,4.866845,-8.334431,0.014529,-0.884918,-9.294215,8.685763,-0.275053,-4.889953,-7.273750,-5.515359,2.027007,0.741363,5.105946,-0.614507,1.192141,-5.112442,8.736415,-9.183774,-9.767495,4.342315,-7.182413,4.753803,-8.682863,1.351129,-7.528012,5.186084,-4.262485,4.362698,-0.020053,-7.424109,0.315028,-2.068789,7.201918,0.331705,2.702531,-0.213439,9.962133,-8.356859,-0.513234,9.612682,1.659439,-3.188704,8.177295,7.762637,8.179944,4.687670,-5.879770,6.692283,-2.066064,7.144133,3.932869,-9.603408,8.404707,-6.809469,-4.385884,-2.526899,2.747900,-1.032910,-1.675463,-9.496112,1.175537,-3.776796,4.111165,2.652528,4.078029,7.631680,-3.556643,2.811572,-7.149525,8.750473,6.069497,-8.356013,0.803958,8.852539,-4.811090,3.801147,-7.325963,6.399349,-8.089978,4.456354,3.671029,-8.744786,-8.588325,7.679182,-3.148125,-9.299874,-3.604351,-8.962368,8.712421,8.888669,0.188410,3.601524,-8.649181,9.399851,6.574839,-2.495744,9.927102,-0.186742,9.792212,-5.548328,1.361172,0.967225,6.151657,3.891694,-5.571124,-2.004806,6.983947,7.100221,-4.062915,-2.173365,7.761662,-0.267782,-7.342377,9.658522,-2.736447,9.116020,-1.796963,6.552407,-7.208378,-6.992922,0.629574,-2.074187,-6.413948,-8.839985,-4.574555,-2.807467,-2.110641,-7.534292,2.894218,-9.907960,6.434212,8.544030,-4.312958,6.342246,9.361525,1.744834,-1.957337,-9.632200,2.600046,5.026637,3.773429,-7.164184,-8.946197,-5.534109,-4.247590,8.616777,-1.858151,5.100882,0.329518,4.429970,-1.173665,4.969817,-7.542301,9.458123,-5.711154,0.976966,-5.812589,9.774158,-0.126353,-1.117257,-3.910296,-0.102685,0.074321,-6.932519,-6.963633,0.829505,-0.697587,1.019492,-7.512376,0.037323,2.202955,4.510208,-7.023086,-7.764344,-2.709808,7.429607,-4.789424,-2.384691,7.133788,-4.997964,-5.599044,-5.465953,-7.195348,-4.757360,-7.067923,-9.777985,-8.885079,3.114239,-6.603440,-6.738532,-6.055582,-6.929093,3.147504,-6.434728,4.876046,4.132532,2.121273,-5.030546,0.405251,-8.623246,-7.555080,-7.467162,-5.363735,4.722372,1.819113,-6.832101,0.122917,7.839111,3.591279,9.396500,-2.092168,-7.711558,-3.870725,-2.910194,7.513521,8.509988,9.664155,8.496343,5.872760,-8.673982,-8.767652,1.973436,8.126604,-4.897163,-1.339891,1.066437,-4.921894,-8.100211,2.104798,0.331810,-7.427377,-6.002650,-0.800818,1.229072,1.634899,-9.132844,-2.030264,0.773707,-6.976438,-0.620100,-3.600304,-2.325092,-6.448295,0.675021,9.333260,-9.737912,-0.865587,0.831182,-4.596401,-1.216016,-9.107534,3.416183,-9.207663,4.099036,3.639784,-5.823819,9.323694,-6.313759,5.105345,1.769790,-0.370489,-9.640026,1.294239,2.340654,7.727958,4.866457,1.133543,-3.196333,6.723264,-3.369160,-2.983851,-3.136446,0.221035,7.549098,2.766766,1.952506,-4.850349,-8.094659,2.625884,-5.425056,9.795425,1.347438,-0.927137,2.046633,2.585514,-5.471377,-5.940547,3.089315,-8.213991,-2.531530,-2.168763,3.266560,-1.525201,-1.403912,-7.037107,-4.506255,-4.014936,-8.570391,3.839211,-3.879740,1.240554,-7.048952,-4.567369,-3.699643,-6.257592,-0.367074,-3.441748,-1.182847,1.669157,4.279638,7.847704,8.605080,3.186235,-4.108226,1.558224,9.048092,-8.984705,-2.846913,1.842517,0.172359,-6.120266,-1.489442,3.408109,0.278143,4.320919,-1.602659,-5.866022,-8.410029,6.475507,-9.997998,-5.704028,-4.500175,-1.234866,2.957287,4.449374,3.422780,-6.108022,-1.231676,-9.989162,-3.887319,-5.425972,-6.377937,-8.700343,-1.906097,-6.352842,0.609624,-5.462766,4.664105,-9.711922,6.746010,4.215966,7.141551,-9.542625,7.253050,4.786347,4.008899,0.725336,-0.091443,-0.207843,7.649794,-3.293986,1.712051,-4.584700,6.006625,4.277231,-3.712029,0.432067,-4.563497,-1.446583,6.419456,4.638537,3.961930,-7.301399,9.104046,7.021915,3.568184,4.821769,-1.232520,5.830545,-4.161849,-0.783834,4.252611,7.899649,-1.199031,-0.898652,5.554549,-4.123132,-8.444658,6.130697,4.324410,-1.292961,-8.559094,-5.192024,-2.663414,-4.260529,-7.650968,4.157442,-2.356266,-4.559454,-8.807051,-3.241856,-2.145976,5.796807,-2.099990,-4.410882,5.724978,-4.065711,-9.945602,-7.859813,8.881313,-5.904189,-1.870500,2.297575,-5.309824,7.534916,-9.087981,-4.370439,-1.989191,6.275246,-8.466560,-0.613690,0.217741,8.486159,4.509514,-7.715469,-8.794308,5.555216,-7.782694,-6.161757,-7.115552,-6.449066,8.466610,1.844100,-5.424215,-9.550835,4.890805,-5.581832,-4.890425,-5.744719,0.273954,-7.435963,2.095761,-9.895942,-7.631089,-5.547728,-4.650221,-1.586229,-8.064623,9.575446,-6.171669,6.447993,9.222944,-3.816136,-7.641274,1.502063,5.774212,6.630572,5.459638,0.790438,-7.227050,-2.315701,-1.498603,9.719337,4.771800,0.490703,-3.103385,1.221335,-6.443759,3.141173,-0.674507,-2.391618,-0.203225,2.842867,-2.460438,-1.931917,-2.409307,5.112150,1.435222,2.254807,-5.332806,-9.378638,-8.508104,-2.298627,-7.481646,3.236079,-0.307406,-5.279760,7.416828,6.312556,-1.527954,3.061858,-4.087463,0.215425,5.580309,-3.701259,8.680026,-3.166691,-1.552327,-6.350723,9.681310,-7.365148,-1.577813,-8.123859,-2.242453,1.209573,3.747954,6.991324,8.038001,0.798807,-6.246330,-7.795758,2.851372,4.954613,6.893945,-0.048181,8.963465,1.171085,9.131298,3.208128,0.567003,8.514432,9.589121,-1.639701,0.453720,5.811735,-0.805189,-6.975769,2.253433,1.670655,7.381494,2.782080,-8.534361,-0.091691,-0.772263,7.044694,-8.687869,1.087570,-2.767170,5.042278,5.867797,4.101812,-1.893617,5.505966,0.675711,0.189146,-5.528119,3.347725,0.862245,1.066674,6.071821,1.412044,4.789573,-8.049680,-9.834753,1.344360,-3.908050,5.854882,-4.972387,-2.660061,-4.398215,8.053352,-8.742273,8.906392,-4.262406,-9.988887,-5.197363,-2.974763,-4.925303,3.404101,-2.325577,-2.023572,9.976079,3.668373,2.559714,2.114116,5.512265,-7.794464,4.993697,6.159070,-7.333020,8.829242,1.613594,-1.319590,-4.787955,6.022698,1.249771,-9.554269,5.506543,-0.089836,5.724131,-0.749912,-7.231475,3.014119,2.928381,-8.536075,-5.040699,-9.799032,9.109125,1.202354,-3.685609,-2.689676,-9.068154,-5.981273,-4.021539,-4.802961,-5.527445,8.919547,-8.061086,-4.022580,0.243031,2.478292,-7.165953,-8.501959,1.243034,-4.944624,-0.520902,0.323361,1.952271,-7.866255,-4.581141,1.546997,-2.482490,-8.910251,2.880620,-9.541365,0.991390,-3.096757,9.450944,7.965880,-2.862259,-4.113979,-8.684259,-2.857342,3.501226,5.863158,8.593684,-5.735499,8.707224,-8.774480,1.749670,-2.317244,8.811768,-3.726807,1.565391,8.992567,6.108328,-2.513605,9.211018,8.311254,6.872310,-4.908457,-1.179874,-8.898982,4.060093,-0.900985,4.990771,9.458975,-7.991392,9.678084,1.426448,3.334562,-2.900911,-6.444266,-4.466598,-8.975489,9.117523,9.680681,3.572638,6.576831,-1.102452,3.688883,-2.888992,-0.531770,6.055571,-3.601248,-9.512159,1.821846,2.845305,-2.288495,-1.088352,-2.898979,-0.734577,9.569869,6.470466,-3.316219,-9.307792,-0.073141,9.207864,0.050517,-5.764867,2.975692,-1.213260,-5.375848,1.218307,4.579971,3.684832,6.802540,4.624663,-8.685635,1.989922,8.584000,-8.348877,2.526895,-8.275059,-9.891051,-5.051331,-7.287955,7.474634,5.801444,3.944139,-8.127983,-0.873625,-9.950632,-7.962746,-3.164100,-7.459269,6.345780,5.731589,-9.571092,-5.143222,5.814760,-5.824811,2.790636,-0.294465,-4.524192,9.253021,-8.315165,-5.868903,-1.088032,8.085498,4.998136,-5.767207,4.230295,2.458375,8.027872,-6.029577,-6.248841,-0.014421,-4.855371,-8.483457,6.278788,4.936036,1.869548,-6.138689,-2.515570,4.120180,5.033142,9.100663,4.098027,-2.716510,-3.086285,1.197228,-0.833449,-7.337831,-6.337673,2.135454,-4.978340,-8.766347,4.016165,4.707512,-6.765913,6.537844,-2.219336,-6.469224,6.913141,2.011020,-6.026062,-8.645072,-1.868231,8.044882,-1.200410,-7.390552,-4.884849,-5.436602,-2.041207,1.248494,-0.556501,-2.815393,7.695379,5.001842,-5.853040,-6.914359,6.264423,7.911065,6.311205,7.923336,5.447451,5.253299,-8.995371,0.875749,0.905259,8.982261,3.134913,7.800006,6.562704,9.231615,7.568128,-0.624464,4.143654,-0.963150,-9.301989,-8.245144,-2.795031,8.288460,9.250468,3.874770,-4.086522,0.526554,-1.408956,-9.407227,3.975772,3.096203,-8.509844,1.057359,3.381479,-8.386276,0.483089,-6.379549,-9.040866,-8.633590,-2.948761,2.687721,3.004645,6.464944,2.612216,4.417274,3.061028,0.309270,-6.607958,2.983613,-8.407455,5.118368,-0.616933,0.335738,-6.880456,8.287433,8.990383,1.007472,6.720110,1.550751,-6.280471,8.637811,1.958593,8.966981,5.209185,-1.674635,1.323712,-1.393075,6.293983,-4.982365,5.420406,-5.495599,-2.622228,4.643942,-7.484644,-1.637605,5.723626,6.376259,-7.226766,-6.761966,2.335716,-6.754578,4.093308,6.989866,-8.198577,-3.475035,4.868547,0.723820,-9.521173,2.971196,5.891660,7.975149,6.530438,3.321984,-1.901373,1.614028,-9.237266,-5.435855,-5.822026,-4.638138,2.499161,5.943462,-0.796755,5.844823,0.612146,4.890684,-9.014486,-7.432254,4.022735,-1.670405,6.199191,-5.047365,3.196997,7.798666,-1.429390,-2.191910,-5.656597,-8.610916,-9.720613,1.686559,-9.222801,-9.456297,-3.076981,-1.272456,4.261309,0.889834,-4.036336,-6.489569,-4.708153,-2.187898,-5.688653,-5.562127,-7.081062,4.089124,-6.369979,-1.974504,6.297403,-3.520503,7.560519,-9.852480,3.471497,-3.790236,3.533064,1.140047,-9.569263,-9.773510,-6.017862,-5.551368,4.948531,-1.374296,-1.913346,-1.938785,2.696389,8.496725,6.023549,1.920695,6.802046,-2.877078,8.247257,-3.599881,8.945045,-2.969375,-6.813798,-9.905273,-6.704655,0.456328,-1.695959,-8.090781,-2.695280,-0.959664,3.277403,-1.374744,3.752430,0.397897,-2.869568,9.760323,-9.118213,-7.371613,-2.259999,-3.425371,7.200920,2.323418,4.568194,1.551258,-5.534551,8.567964,-8.427473,-9.404157,4.313156,-1.361550,-5.916586,3.799310,8.974168,7.342282,7.976192,-8.595186,4.653210,-3.197602,2.002917,4.827473,8.885042,-6.142362,-8.842510,-3.868754,-8.025307,-0.631496,-5.304694,-4.304044,3.993023,2.747575,4.228434,8.153208,6.987365,-4.654596,6.108918,-1.198477,-0.861671,-9.029493,-2.932412,-8.893097,9.745993,2.841600,6.750087,5.061626,3.470360,2.919465,-9.759276,6.588832,-1.717916,9.945083,8.982879,-8.914019,-6.950820,9.831546,4.719569,0.316210,-0.953607,-3.219870,-8.146108,-8.906254,-6.373165,9.716973,-9.185268,4.958966,-7.048770,-1.021710,-5.614561,3.001430,-5.805693,4.248665,7.696213,-6.705724,2.272366,1.477308,6.087083,6.063030,4.778105,-0.481202,-0.722588,-5.561084,-1.636708,-9.012463,2.907573,9.282793,-4.130024,-1.539943,-5.161363,5.666229,7.381983,5.570827,-7.797624,3.681721,1.571249,6.184762,9.978668,-5.918183,6.744591,-6.265647,7.781821,-9.923945,4.418741,7.978540,5.465273,8.012006,2.273240,7.487853,-3.531278,9.052466,4.924439,9.503599,-7.431530,-6.318236,-7.706837,-0.377340,5.037082,-7.842972,2.485722,-8.184162,-6.899040,-2.728461,-4.098583,-7.302906,-5.708734,4.792320,-6.559386,-7.165907,-0.992671,-1.188183,0.747888,-3.684123,7.625027,6.292836,-9.836152,-3.850353,-8.778084,-6.573111,-7.449511,7.903176,-1.685127,-0.702014,7.617623,7.980788,-8.715248,-1.464788,2.668570,-0.714690,2.076404,7.002490,3.158419,0.028929,-8.113528,-3.512542,-6.214406,9.780629,-8.047262,2.814532,-7.933817,-8.267486,2.841687,4.171240,7.528830,4.980072,2.027791,3.618866,-0.279036,-4.198057,-7.389210,-1.138594,-8.173408,-2.126824,4.982447,-9.515041,-0.170991,-0.622016,-1.097054,-1.946388,8.998806,-3.234276,1.579990,5.604578,-9.813895,-4.198246,0.815476,1.373037,8.636178,-0.046204,-9.875595,-0.065946,2.655667,-2.156740,-8.888251,-3.316209,-2.573129,0.726189,-1.109353,-6.693106,-8.477498,3.777228,3.420595,-4.434357,-3.693623,1.952906,5.999395,-7.169142,6.620951,-7.923136,9.102845,6.712904,-4.513482,6.647396,-0.844334,2.636712,5.535407,-3.275077,-9.937892,4.283925,0.966366,6.483075,-6.870877,-0.505889,-4.964355,-9.982185,8.353836,5.520982,-4.795996,-1.030097,-5.933501,3.506099,-9.255874,-1.577285,-8.484586,-3.979503,2.443965,6.498806,9.535499,5.159654,-8.025772,7.928645,1.395132,6.620923,-7.868258,-0.602803,-9.661085,-4.735251,0.234892,8.609824,-4.739358,-6.929906,3.034376,3.638642,8.048025,-1.098998,-8.634550,6.585706,-2.696249,0.256907,-9.901531,-5.011238,-4.330101,1.012638,5.763263,4.949962,-4.594429,1.917325,9.134599,-6.547103,1.064408,9.871073,3.674765,-5.903506,4.434210,-2.681144,5.216104,-4.435515,7.786694,-7.645685,-6.956057,-5.113299,2.317372,-6.061286,-9.022015,2.267682,7.723893,-0.256131,9.186108,0.012697,-9.385773,-2.437042,-3.495887,1.893501,-3.702321,-8.325956,-8.512839,-9.816102,9.758931,-4.601661,3.884610,8.189099,-0.779032,6.384578,-9.787254,0.201212,-6.389637,4.470909,-3.013041,-4.038928,-4.066395,-3.235153,1.066794,-1.346074,6.405803,9.998158,-5.611458,-2.862250,-5.408252,-7.261268,-4.127944,3.237917,6.102998,8.093799,-3.385266,-2.356123,-2.296367,7.708097,9.483027,-7.443671,-5.471804,-4.884698,3.256289,-2.138657,-5.337762,-0.872144,-4.200734,-6.026803,-7.047151,6.007284,3.166647,9.954553,-6.530411,-7.842768,-6.102898,2.328392,-2.123404,4.463993,-0.061506,1.135852,-8.126673,6.654948,1.412240,-5.992406,1.859055,-1.652486,-4.348389,-0.935476,-5.043649,-3.863147,-9.189454,-5.571786,3.591011,-4.864344,9.363280,5.626969,1.666908,-6.103501,-1.481072,8.238930,-5.178177,-2.402303,2.370524,-9.039952,5.015026,9.079506,-5.420460,-4.149382,3.363111,6.913829,-6.580973,3.245962,2.082983,3.691074,-9.472080,3.964868,-4.455557,5.520891,-0.615888,-3.927100,0.156662,9.678769,1.423651,8.337588,-2.662703,0.454920,7.472929,9.700008,-2.380995,-5.172001,7.467805,8.579279,-1.300230,2.577935,-3.868010,-9.352933,5.895524,0.129408,-1.784595,-6.512976,3.798388,7.597306,-8.674114,8.350317,9.940918,4.980247,8.267990,8.378308,-0.086329,1.066516,-0.379025,-7.985479,7.348877,-5.065325,-5.157219,3.377069,-2.294733,6.169425,7.890056,5.156990,-5.783830,6.093842,5.826752,7.075800,1.720494,0.008248,0.474642,-9.151784,6.097598,-0.429881,0.162316,-9.566467,-2.044465,-4.775414,-0.866984,5.220516,-6.870455,4.929282,1.541469,2.594045,2.488013,-2.148220,-2.031173,9.522436,2.473495,-9.999626,8.431973,-5.793967,-7.583459,7.896888,-8.140411,8.859617,7.662752,-7.894537,-7.199499,-9.783902,-1.261923,-3.507379,4.441254,3.466614,0.434342,5.573966,-4.305534,-0.855329,-8.800760,8.610341,-4.686823,3.813671,9.272792,-8.868604,-6.437309,1.881367,0.130172,7.785935,-4.131507,9.627322,-0.621418,-9.990776,-8.746181,3.094594,3.570333,8.111984,-1.916831,2.919666,3.688681,2.746588,-0.042765,-0.998848,-8.518569,-5.180911,-6.717747,-1.086258,-9.654318,6.230972,2.324279,5.938268,-3.677071,0.372930,-3.275427,-5.552551,-9.318152,0.844368,9.915651,1.936785,9.089576,-8.411966,1.066103,4.572633,7.215128,0.167868,4.242388,8.835996,3.400712,-6.622258,-9.125942,8.159269,-3.866261,7.823332,0.674975,0.063967,0.351778,-7.330543,-7.756648,-2.423700,3.196230,2.808808,7.926769,-5.377593,7.382736,-3.757369,0.232922,-8.977756,-4.990114,3.732496,-5.943136,-4.396670,-4.858246,8.260472,-6.545071,5.825199,0.760890,4.033336,5.206263,5.759860,-3.810567,-4.868927,-3.582281,-0.369401,6.533455,-3.524649,-0.877384,7.078928,0.418468,-9.737636,-8.077468,5.582297,-9.104417,-1.828604,-6.181134,-2.398104,5.531056,6.471708,0.293873,-2.797784,8.604695,4.443637,-2.080940,5.608282,7.373386,2.855316,5.325161,5.979958,7.790795,1.430052,4.502840,2.844515,2.830695,-9.665786,-5.040255,9.756590,8.460947,9.770268,1.182004,-7.854912,-8.146508,-3.558665,-6.814154,6.530602,-2.131919,-3.987466,-1.172233,-4.597332,-9.679920,7.406748,-8.512992,-2.938788,8.097517,5.470118,-2.876134,5.382945,4.065421,-8.902567,0.484688,-0.062668,3.841641,7.413819,-7.438186,2.634408,7.344327,6.014612,0.963966,3.563088,4.683561,3.844012,-8.744608,9.714953,-8.274969,-8.230433,0.548253,8.764172,4.706890,0.901992,0.464370,-0.935402,3.289518,-1.055157,9.232347,1.197084,-0.684543,5.302572,9.904339,-9.903840,-7.996698,2.745101,4.365658,-7.434438,0.148405,-4.782160,-9.431489,7.434876,-1.723840,-9.493644,-5.273011,2.569225,-1.499573,5.741624,5.357996,-0.308394,-5.288030,0.581185,-6.529914,-6.012378,1.619486,-3.871875,2.145054,9.670860,9.873733,-4.542528,1.098712,-7.005658,-6.121159,1.106543,-6.104868,5.031855,4.554135,-8.001123,0.148990,-5.324841,-4.705732,-9.266302,-5.119434,4.832118,-0.715390,7.294863,6.681623,7.847623,-5.262627,0.719339,-0.891608,2.968597,-5.984329,-1.654122,0.422938,-2.595640,8.242793,9.864872,8.683342,-3.275643,-2.279299,6.363478,9.962265,7.470587,-8.620778,-6.105428,-9.872678,-1.841054,-1.449425,-8.771170,0.629017,0.591916,9.609860,9.298214,5.300173,-4.642681,6.162240,-7.139910,0.176621,-0.920393,-1.372918,-2.762859,0.692733,2.702800,0.493863,7.966132,3.068251,-6.280047,5.725702,0.810991,1.027549,6.778943,6.024205,8.942520,5.138781,-3.261273,8.693310,-4.222759,-1.879120,-3.864212,6.650517,-7.987611,-0.082892,-1.323632,-0.913759,-2.369885,4.829858,4.012772,9.789051,1.202517,-6.427890,7.629695,2.760590,-7.925582,7.502166,7.136759,-9.037369,1.194828,-1.758539,7.347166,5.277379,-4.218897,7.627457,-4.991614,1.793724,6.033869,6.692872,5.802339,6.162271,-7.678575,-8.843798,6.189052,-1.199610,2.622170,-0.665649,3.981012,-4.224499,9.998346,5.064385,6.953978,9.782092,4.636307,8.797209,7.407067,-3.375463,7.607691,-7.852489,-7.000089,-9.082075,3.676504,-2.966310,-8.694433,6.112763,-6.911688,5.948678,7.394895,-8.090894,-7.455307,4.315975,-8.982497,2.117259,-3.618535,8.938915,-4.832176,-4.843179,-8.637841,8.450044,8.555121,-3.047663,8.503015,5.022624,6.260520,1.117737,1.715426,9.938965,2.522149,-6.687259,-5.758868,-4.033252,4.413079,9.219948,5.445327,-1.696661,4.292818,-8.359540,1.848141,5.541461,5.216407,-3.302590,9.561076,5.125065,-9.577497,-6.879433,9.712157,-1.566632,8.548739,-2.208387,-7.892855,3.871620,-1.107707,-3.317390,-2.426089,-8.485549,8.900874,-9.811781,-2.935680,8.602615,8.314612,-5.565523,-1.342969,0.617673,-7.251026,-9.642612,3.871898,-5.388259,1.879043,2.662918,-4.242063,7.150711,-2.917918,-8.898315,3.883308,8.854987,5.464991,2.261094,-2.250821,1.110890,2.353949,1.659638,7.671379,-2.818100,5.827269,-9.258170,8.900909,1.572018,-9.482658,-9.500995,3.967802,-0.562318,8.178667,-6.943064,4.907705,-6.662473,0.734192,9.566752,6.066154,2.682280,8.335160,-8.822018,3.227358,-8.873913,9.312146,-6.923072,-6.099750,5.375219,-2.572446,-6.203744,9.456373,-2.668398,-9.044257,-1.830855,8.484972,-9.053058,7.377523,5.116759,-1.865626,-7.013401,8.843573,-0.661163,-4.374120,2.459376,0.189289,-8.797442,5.580916,5.053471,-7.865895,1.497264,3.320340,-6.292696,0.064771,-9.196485,0.910468,9.005042,3.045530,-2.508861,-2.320646,-9.628551,3.973160,-8.759200,-8.724102,9.195655,2.202899,-2.676588,-2.519510,-6.206554,8.198469,-9.433221,5.392402,5.486423,5.044926,-8.212387,1.602959,-9.228441,5.110450,7.638894,-9.731080,-2.609186,-8.800080,1.000549,8.463022,-2.544420,-2.590923,9.637978,-5.799041,-9.658958,8.464432,6.201374,7.849650,7.852027,3.659568,-4.083645,9.550432,6.311290,-7.140651,2.815541,-5.406166,-1.471950,-6.697477,6.613762,-2.881062,-8.522462,-8.224242,-2.378625,6.366412,9.217197,5.211860,8.840984,-1.113592,-2.062446,6.413085,7.305327,6.494227,-1.682130,0.903417,-7.199087,6.847927,4.678167,3.092506,7.795000,-7.937830,5.209848,5.753374,-6.530912,6.545774,-0.247748,-8.692406,9.733027,2.495701,0.325939,7.445875,-3.302880,0.917741,-3.120779,1.523352,5.774107,-6.497183,3.871121,5.558381,-3.877950,-3.296845,5.610330,-0.873527,-3.905455,-8.904564,-6.364318,-0.277955,-9.278070,4.199404,-3.197390,6.080874,-2.797243,-2.679554,8.084406,0.676473,-1.297412,-5.083615,8.074738,-0.138839,-0.264649,0.944960,-1.097056,1.939590,7.512222,-8.554888,8.756002,-7.064310,8.917204,-2.681657,-9.224721,-7.196656,9.555682,5.189993,4.755874,3.369845,-4.442108,9.538223,-1.478220,-8.954105,8.272107,4.860564,-9.472738,-2.613009,-5.786380,-6.737537,-3.469426,1.033947,1.039419,-8.812687,2.341015,-7.803059,3.846163,-9.840428,-4.019060,0.649255,0.016207,-5.758781,-9.817755,-9.386279,7.140761,-6.880374,6.826802,-0.950388,-5.634467,-9.729063,-6.991096,4.277780,-8.990142,1.558624,-2.507851,-8.155830,2.975453,3.799129,8.228721,-5.863610,-4.553071,-5.342313,-5.397238,-0.248355,-4.929510,-8.531732,9.442792,-0.758439,-0.139535,-4.518107,-6.836997,-1.811181,-6.746801,-8.590062,1.924777,-4.338853,0.393143,-0.681770,4.012883,-8.856428,3.277138,-4.060650,-9.986226,-2.972415,-7.690908,-6.258972,4.983325,-2.171919,-6.793320,9.637412,4.510902,-8.479671,-1.787587,9.542955,7.579448,0.937033,-1.060329,-8.550180,-3.894706,8.512953,2.455524,-8.118903,0.396575,-6.939442,1.012734,2.185532,-8.257516,6.619619,-4.966295,-2.255345,-1.390413,-8.856138,-5.713823,7.589773,0.224497,4.126203,-8.719855,3.123309,6.719447,-3.676145,5.266380,8.611946,9.531209,7.233179,2.866026,6.730288,8.326210,4.124906,-0.539198,6.828273,4.092158,7.616403,-1.083308,2.625400,-0.599861,-8.197026,-6.726413,2.953712,-4.951968,9.785794,8.712133,4.098865,4.195431,-9.321945,3.628855,6.575357,-8.365864,6.687621,-7.269754,-4.613940,-5.379404,-7.484045,6.449401,-0.708681,-0.980402,4.030391,-2.187482,0.300254,4.637287,-8.319551,9.413732,-5.359244,-2.697777,-5.743563,-7.545838,0.993174,5.559504,3.178241,-3.686798,-8.918587,-4.236998,-1.652132,-7.522907,-5.745686,8.862946,-3.607933,-9.507666,-8.347705,-9.791318,9.593157,-5.197599,1.505388,7.732996,-6.971324,-7.938866,-3.680411,-8.948992,-1.946294,-7.634932,4.636820,0.545060,-5.155455,-5.854017,-9.303287,1.347834,3.194066,-1.460423,5.487980,-4.342440,5.488152,-9.446741,4.733772,-1.644780,4.124116,-8.210129,-0.386509,7.749048,2.675991,-1.456646,-8.271392,-7.631607,5.182581,2.502920,-5.122663,-8.148429,-2.868162,1.233479,7.291285,1.896346,4.786666,9.271465,8.538045,-5.173120,-8.738128,-9.066229,9.991588,0.882408,-1.963660,7.220380,-1.377729,-0.771489,6.148498,-0.932819,-2.483695,6.749734,6.181490,7.116487,3.235425,8.145901,-0.446471,8.339372,-9.127273,-0.852717,2.871483,6.441683,4.457811,-6.462782,-8.597759,-1.505983,0.186112,-4.834851,-2.226605,8.536744,7.173473,-5.042185,8.334763,7.334586,-5.309297,-4.274640,-0.108171,4.475919,5.435775,-9.983326,-3.415617,-5.858263,-6.974026,-6.265122,3.060904,4.857828,-4.316536,-4.775814,0.944685,-0.786053,-3.192619,5.767453,-1.167471,-2.148663,-2.407347,0.766300,4.532312,-0.700757,-5.679052,3.602986,1.394345,0.757962,-0.001777,6.025951,9.465973,5.219249,-2.361959,-7.703231,2.965956,-5.883142,7.297526,-1.492696,-5.394222,6.768609,4.904195,-0.698288,4.419469,-8.756798,4.332709,1.407215,9.908582,-7.283760,3.621414,2.076242,-1.288022,-8.842324,9.689585,-0.410816,-9.750680,6.910156,-9.650891,-7.217566,8.959754,7.970107,-1.269178,0.806563,5.251536,4.662016,2.902564,3.965966,-2.964191,5.237225,-8.822928,3.126230,3.205701,-4.596860,-1.249661,9.471479,-3.181805,9.370270,1.369471,-3.996957,-3.081884,2.157104,-4.625236,9.100460,9.585271,0.478758,6.937822,-5.776976,2.987055,-1.263410,3.827800,8.208818,7.627684,-8.663974,4.545742,7.630598,-4.670552,7.290009,-3.269234,1.673714,-6.944454,2.552177,-7.500505,-9.988174,9.735061,8.416076,8.503904,-0.934499,4.441185,6.248977,3.642066,3.197160,-0.438091,8.971722,0.796683,-9.949668,3.437097,2.992806,9.641152,1.027736,6.565690,1.070778,8.363770,5.924882,-7.099762,0.676308,6.134039,3.923787,-9.737470,-3.743901,4.618031,8.569193,4.769305,-0.311129,-8.678527,8.534072,8.444272,-4.159100,-0.747815,0.783268,4.507258,-6.142517,0.456266,-4.018243,-3.626484,-6.483480,9.711130,-4.012517,-8.465798,9.440681,-5.492413,-0.344519,3.083046,-3.455135,-6.477234,-4.868696,1.449617,1.281411,-1.154710,-8.782950,-3.515345,-7.499993,-3.306887,-5.274558,-9.970420,1.071244,-6.482927,-8.255711,6.038371,2.084498,-3.342216,6.376493,1.107608,0.520591,-1.770530,-9.546967,-3.151172,-3.029223,-8.456938,3.041089,-8.569055,6.043150,3.011108,-5.740817,1.720455,-0.253006,1.150380,8.977845,-6.894649,-0.126518,-0.405998,-5.290076,8.970428,9.930680,4.297991,-6.094778,4.363608,3.545918,4.228707,7.429123,4.812920,0.528846,3.919169,7.597929,9.865081,-5.902720,8.979392,-8.874745,4.681350,-7.362056,-4.855833,-6.186612,-0.013894,-9.771389,7.621353,-7.502873,-3.222949,4.339286,-8.427158,4.545894,-6.559938,4.562172,-4.879713,5.423947,2.466085,6.924823,-6.554730,-1.495587,5.909660,7.154517,-3.575993,0.472764,3.896131,3.108682,-6.717272,6.913620,-2.274646,-1.231761,-9.301875,9.335214,1.433881,4.641896,-8.956806,-1.689382,2.696175,6.441269,-2.087717,-5.818193,5.157811,1.165542,-9.630961,3.212630,-2.643544,-8.828566,2.929756,-5.877750,-6.306791,-3.677760,2.430815,-4.316057,-9.935554,7.224498,-8.662305,-5.728974,3.418113,9.183303,-4.970939,-4.994106,-7.285757,3.634014,-7.003917,-0.177533,-8.475832,-5.382410,-1.090368,-0.077887,-9.435606,2.587808,5.350853,-4.158948,0.437270,-7.854585,-9.841301,-8.015315,1.571801,-9.487433,-7.080298,-0.794435,-7.882964,-7.879814,3.385113,0.082757,-3.123575,2.149865,7.287826,-5.381372,3.987831,-3.069220,-5.623280,6.970056,1.603108,1.086019,-8.703083,-0.233687,-9.942558,9.980826,1.392453,0.264374,8.090618,9.296413,6.074091,-7.234692,-0.981038,-6.539480,5.314017,1.816350,-7.388245,-6.499461,-0.484849,6.760020,-0.387795,6.189910,4.901395,5.744403,1.060648,7.942258,0.339955,1.679089,3.909919,-5.524537,0.527756,2.151318,-9.934831,9.304595,-6.000271,-7.384831,9.603999,-2.623089,-9.318017,-7.698145,-8.938067,-2.380189,3.922533,8.813996,-0.861004,0.146616,0.971879,1.383747,7.017289,3.513750,4.614099,-0.193566,4.850242,0.948179,-8.438335,8.120742,-4.551236,-7.672375,4.223282,-2.109455,6.272823,-5.760678,-1.491313,2.086079,-8.198351,0.454383,-2.756482,-3.943425,-2.671761,1.365283,8.235994,8.942857,3.965911,2.943861,5.247890,-4.288039,-1.118767,-9.906505,-3.913383,-7.692523,-1.153389,-1.744126,3.765181,-6.976624,-3.282741,-2.136451,-2.528573,6.002529,-1.539370,-6.232670,-7.039460,-9.396515,5.576495,1.630849,-1.524849,-0.569754,0.829657,4.583026,-5.369419,-8.451321,-6.918285,-4.680603,-7.292272,-2.496334,2.809423,8.394101,4.404444,-3.304557,-8.178466,-2.167782,0.778063,8.797894,4.194287,8.305832,-1.713611,-7.913538,-5.219790,9.640923,2.225630,8.015309,-3.330917,-1.089312,9.804890,1.616506,6.741383,-7.726385,-1.110818,2.727571,0.261715,1.742676,7.770010,-5.653877,2.612205,-6.032521,4.999277,6.433841,-4.496894,2.573763,-8.253095,2.409552,-1.338485,-7.633871,4.656745,-0.866931,-2.076872,-2.225425,6.593445,3.949369,-7.484189,3.526438,-4.394200,-4.887300,8.332744,-1.086419,-9.192084,6.300178,3.756485,5.255420,7.725690,9.021058,-5.361881,8.323141,-6.073121,-4.299897,0.075996,-1.906194,-1.995614,-2.036278,-0.313716,7.715849,5.872954,7.030169,-1.050916,7.462859,-0.872664,6.696485,6.737517,7.636634,2.948329,-9.970627,6.655783,-4.205805,2.214090,8.275453,1.330950,-6.758374,5.208821,-5.554786,3.521363,-0.748007,-0.727457,-3.434503,-9.315545,-6.472385,1.149435,-7.617608,4.103372,-7.732231,-7.245458,3.332761,-8.001415,-4.505197,3.293538,6.953670,-4.222323,4.065486,2.234740,-2.630152,9.246878,2.260932,-0.948250,4.878533,7.152444,-3.868418,-6.699689,3.541692,-4.259036,-2.393038,-7.341135,-6.639133,5.762128,-4.381131,8.680732,9.074256,1.863507,7.472254,-8.257441,9.076749,-3.302361,9.392084,4.672112,5.120507,-6.909953,-2.360568,9.475206,-2.667986,-5.502459,4.512024,8.579819,-5.987510,6.767717,-3.563870,-8.613227,0.599933,-4.911188,1.237433,-8.860978,9.190869,7.684064,4.755471,-4.836896,9.602230,-6.126645,-4.351334,6.662895,-2.604878,-5.738643,1.679685,0.971649,6.170879,8.605571,4.716794,6.926704,4.079239,-6.721495,8.944935,-9.301611,8.465570,9.616188,-9.125350,-3.014620,5.885907,-0.329965,-5.277580,-1.053110,4.785045,-3.311666,5.764528,4.859646,-3.930576,3.010694,-5.403724,1.491309,6.353087,0.053475,4.255112,-4.670118,-5.147668,4.997112,-1.357008,-5.267768,-4.557501,3.431671,-8.502340,-0.807141,-3.049591,-4.566857,9.560203,1.805494,-7.692951,-0.679273,-8.609681,-0.998958,9.512635,0.292657,8.300907,6.705993,3.235807,0.678746,0.342173,-8.889212,-1.240351,-6.939374,-7.301605,-0.928806,-0.992356,2.891081,1.249220,3.595998,8.696058,9.029348,-1.634974,-9.231264,1.603430,5.131423,8.636449,-0.166268,-1.076252,3.009046,-8.324495,1.940596,5.659534,-4.573197,3.233431,4.729526,-3.264675,6.091059,-7.616648,-8.440841,-6.656709,-9.327220,-7.947018,5.900269,-7.037972,8.729334,-7.717914,4.252365,5.857723,-2.014672,-4.404277,-9.541794,-9.859083,9.754417,1.874530,-1.293029,-8.724069,-8.849127,-5.866911,4.172002,-4.367180,5.647838,-1.733526,-0.570441,-3.938351,-6.730231,4.559981,-7.777199,-7.762745,-6.801989,2.414583,5.568705,2.791590,-9.137745,7.588570,-0.915339,3.869618,-2.639019,3.361042,6.012401,-9.352515,-1.858771,-9.304867,8.089987,-0.541962,2.662440,3.743601,2.433626,-4.049618,-7.476267,-5.021925,3.834076,-2.477962,0.313748,7.788044,-2.289785,-6.698089,9.396095,0.946181,7.791821,-3.164261,6.546651,-7.937145,-1.547467,7.401595,-2.123387,-8.015213,3.942631,-4.696397,-1.716416,4.965991,3.994885,8.948765,1.670860,8.247534,-6.011612,1.690203,1.766070,3.758562,-9.423788,-4.871650,-3.900101,-5.985729,-5.005936,-8.988893,-1.083338,0.260454,9.334494,-4.961715,7.912713,4.298442,6.549903,9.353470,-4.778058,5.492585,6.672838,-6.158350,-7.189635,6.352132,2.906407,5.257140,-7.437347,3.755971,7.826862,-7.708657,8.276973,-0.308957,-7.681152,-5.460420,-7.487416,6.952501,5.196100,5.551426,-3.298719,-1.594694,-6.376586,-9.267264,-1.747240,-0.215984,6.555821,-8.712347,3.853112,-7.201578,8.744031,-3.551495,-6.480725,3.135492,0.199828,4.092553,-5.590917,7.903965,8.470375,8.990304,0.506101,2.305787,-8.114643,-0.711415,-3.700212,0.411629,7.916958,-8.034104,2.299146,4.637337,-1.937958,-3.562196,3.569514,-2.377974,9.347212,-7.629772,2.144493,-2.933743,-3.382854,4.423863,2.033570,-5.394917,0.418945,-4.529840,-1.622811,9.611936,-7.548690,4.713163,-7.893643,-6.063004,8.616692,-9.554842,-7.719528,-9.239227,3.132842,7.897442,-3.331624,7.681830,-7.577946,-1.474333,-9.210743,-4.761862,-2.503529,-0.429459,5.378936,-9.008648,8.529995,7.776637,3.802115,-1.506881,-9.482840,8.412204,1.953625,-0.510803,-0.796742,3.710074,-5.442780,5.878141,7.309395,3.040877,-7.115908,-7.283113,6.311193,9.448103,1.784978,1.743595,-2.686876,0.357308,-1.796853,5.547503,-9.413640,8.946192,-2.031814,3.406186,-4.531163,-6.864054,4.692525,-9.280187,7.378278,5.175025,-9.234592,-8.447576,-8.827227,-4.529641,3.129344,3.854437,-9.425455,-1.742145,-6.292958,6.146596,5.560394,3.065214,-1.348529,0.256489,-8.600634,-7.737003,3.671684,4.092574,-4.689738,-4.404926,5.770966,-5.808569,-2.522792,3.398024,-6.203344,0.342322,-1.097336,-4.055772,9.016396,-5.750490,8.586412,-9.935789,5.097129,-8.522470,9.208336,2.849304,-5.184315,9.323124,4.641281,2.154368,9.232426,2.915666,-9.479864,-4.974928,2.619101,8.268318,8.762558,9.925101,0.863619,1.646454,1.637195,9.608382,-0.603935,-9.251633,1.454749,6.880206,3.025478,8.754210,5.794132,2.913055,-1.057040,1.385988,-3.432543,5.867504,-6.404087,-3.652647,0.058620,9.166477,-9.797034,4.174124,-8.935248,-2.770736,8.891986,7.447325,9.846131,4.868494,2.389587,-9.122501,-6.272638,2.092389,-6.668904,-7.015931,9.362457,0.002925,2.056623,-2.795944,2.812654,5.688563,-6.231724,8.540551,1.001635,0.846688,7.403699,-8.310153,7.639805,-5.244087,-2.624400,-4.716883,2.486034,8.545013,-5.087836,-2.455416,9.854336,8.886189,-8.337165,7.977452,8.018224,-9.855077,-1.480044,-7.784088,-5.034549,7.560222,8.698379,-6.616658,1.785134,-1.573923,1.858236,-2.831991,-3.353991,-9.395907,-5.651328,1.990558,0.941348,1.484575,-1.748691,4.544083,-0.623516,0.661410,-3.414250,-9.377229,-0.049506,-3.056491,0.216801,-4.673179,-2.514059,-0.111782,-7.319864,-2.438349,2.266504,-7.642928,-2.315653,-0.617489,-9.811781,-8.433515,-7.193940,8.671259,4.825583,-1.996842,-8.851545,8.634619,-8.625050,0.542740,6.860836,-6.549498,2.480526,-7.839999,-4.631886,3.066042,7.295188,-4.693918,-8.770479,-3.111760,8.271786,7.372946,7.961340,-6.441577,-4.895517,-3.116901,7.695475,1.663815,8.303249,-3.108512,-7.236228,4.536297,-3.671637,4.293241,4.934764,-8.121569,8.208414,-7.248521,-6.432616,-6.500989,-5.613214,-4.977053,2.417901,9.869084,-4.429276,-5.619340,8.886553,-2.176568,3.467739,-8.921152,9.568866,2.768828,-0.496355,6.984381,-7.917857,-1.044208,-2.030771,2.696543,-3.180111,0.202690,-9.148816,6.680713,8.474187,5.266715,-3.484784,6.179473,7.145136,-7.431706,-7.453000,-8.179290,2.216512,5.937403,-6.270133,1.538797,2.349454,4.522715,-5.108897,6.848902,-5.986347,8.672327,0.700900,-6.414250,1.657307,-1.311026,-1.119352,8.872190,5.856492,2.068433,2.036612,-3.605059,4.727032,-3.953919,4.026238,2.621167,9.865943,-5.816967,6.813969,2.044541,9.750864,-6.911076,-8.588802,6.458164,4.191875,0.638650,4.585500,3.285158,9.459390,-1.266749,-0.624996,-2.926685,-0.713056,-6.515684,3.434108,2.554345,1.797720,-1.006955,8.305373,-1.070616,9.488095,6.783143,7.941037,3.129300,-2.376094,8.705225,-1.919308,-3.641094,-9.853146,-6.311293,-0.381839,-5.006165,-7.384944,-4.432438,-3.664497,-3.570957,-0.030921,-9.114700,-8.811510,6.337255,-0.244433,9.502194,-3.458821,6.077780,-2.501197,5.879597,6.915527,5.589067,-0.181488,0.734093,-3.120296,-8.795282,7.956156,-9.309518,2.383090,0.079153,1.822995,-6.564664,-5.132106,-0.153644,0.841575,-6.360961,-7.426958,-2.327812,5.521530,6.160119,7.377774,-6.423099,6.205238,7.344603,-6.862400,-4.331285,9.196018,-6.838652,-5.657401,9.440362,-5.526965,6.263607,6.062068,8.786168,2.673861,-0.021967,2.544208,-4.265235,7.291785,4.443548,-4.116297,5.819357,-8.643688,9.550137,5.058196,-5.050207,-4.366268,-4.647644,-5.231407,-2.860245,-1.701766,-6.385708,-2.737076,-5.130274,-9.809424,0.405927,3.610314,9.192879,-7.516284,4.083483,5.096380,3.393336,4.293224,5.258044,-4.711162,7.200437,-1.338767,-5.414249,-4.637672,-5.463944,-4.149872,3.404335,9.946407,7.241976,-0.442360,3.659348,-5.365099,0.313791,-8.675549,7.641907,6.983536,3.519959,4.562408,-8.581312,2.167065,-0.660240,-8.778863,8.646308,-4.114488,-7.141831,6.752963,-0.272237,-8.571827,5.300474,-8.427940,0.318449,-2.197547,1.153237,-0.689584,3.064914,3.776502,9.634987,-4.647372,4.543710,6.907383,2.301945,5.183317,0.935235,6.308020,-2.268145,7.550939,8.689366,-2.423916,1.208778,-4.152360,-1.420276,6.101932,-5.682702,2.047413,-7.354769,2.027917,6.579131,-8.316455,-7.953032,-7.798845,4.286357,9.948680,7.572358,-0.077077,-2.142119,3.465484,-8.893936,9.532368,-4.996390,-4.259448,7.886912,-8.974221,-4.447866,1.971955,0.306336,4.198695,-6.422048,4.348019,-3.634801,-3.001526,0.574606,-3.636546,-8.928523,-0.880544,-5.805303,-0.626222,-2.233727,-4.479822,5.941530,0.132780,7.386074,3.445734,9.702718,8.997703,-8.538546,8.440405,-4.923640,2.764177,8.618375,1.536833,-6.555350,5.281915,9.959496,3.309227,-0.026073,6.345915,7.346854,6.242540,0.545510,8.016664,-6.967487,9.526457,-3.300415,-4.819751,-7.770576,0.659185,8.722662,8.811198,-7.047305,5.799745,-9.942429,3.990755,9.335838,-9.663210,6.397974,4.334861,-8.186650,-9.017560,2.341817,-3.441887,2.298534,4.430237,9.068325,5.654298,6.663676,-4.682459,9.130129,-0.478393,-1.340616,2.927909,-6.973159,2.829524,-9.695348,0.410024,-3.959365,3.735739,5.365551,-4.100669,-1.602679,-5.666346,-2.706472,1.847541,-1.791170,9.836673,-7.940161,7.534284,7.884634,-0.289878,-9.346700,5.953119,4.737671,-5.761298,6.806554,2.148407,-8.350399,-6.674058,-2.701308,-9.981141,7.946736,9.514056,9.227681,-2.515450,-4.305547,-9.928984,-0.591400,7.915081,-8.505840,-9.779580,5.155357,7.709354,4.573204,-9.200575,9.782690,2.898672,-3.989563,6.603546,7.140843,-8.114142,-6.333418,-9.893354,4.831243,-2.154806,-7.301926,9.341239,1.322266,1.364804,-3.282766,-6.536757,2.315935,-6.851230,4.276029,0.521785,3.186312,-8.885962,-3.805894,-7.947005,-7.391097,5.365257,9.005582,-2.151927,-1.291897,-5.885611,-3.656592,-5.021195,-8.973768,5.859736,-5.325465,-8.864650,0.880762,5.320839,4.291663,1.003317,7.923949,-1.371754,0.035611,4.936535,9.753026,3.664184,-5.548465,2.332142,-2.912140,-7.018560,3.450347,5.717568,9.003699,-0.543305,-5.545073,1.617858,-3.857005,0.755485,-5.795728,2.693195,-5.434476,4.514209,2.184148,6.342370,-4.938534,-5.028868,-3.612719,-0.390979,5.061612,-2.771155,-7.147550,6.331458,-7.840196,-5.321041,0.146456,-0.850726,-2.580572,-7.284971,-3.353638,-8.823598,-3.541329,-7.530139,-6.325667,-0.353203,5.235144,2.825906,-4.170760,-7.576556,4.809190,-2.642544,3.396784,-3.829874,-9.443670,1.960217,-3.362111,0.482943,-0.427887,9.744092,-6.493727,-4.338050,0.532119,9.646083,-0.554407,-6.633464,5.107987,-6.615416,1.946275,-0.943962,-8.436682,-8.589519,8.099408,5.506351,1.539845,-0.369131,-5.984207,8.475100,6.726951,-0.307181,-8.755855,5.594998,1.052541,-8.587014,0.057504,-6.389848,-3.152330,-7.918136,2.402212,-7.059095,8.311015,-5.485458,5.784459,9.453203,8.648450,6.683562,-3.131841,6.570398,-6.052824,-3.696025,-9.999644,1.245544,7.770782,4.011127,8.716789,1.627324,-6.677613,6.250039,2.862039,-4.146775,-8.734343,-3.687784,7.270219,-8.527224,-8.183896,3.005616,5.020775,7.391015,-8.743620,4.786730,-9.122501,-8.874349,7.851968,4.878975,-9.738282,4.637503,7.204394,2.601935,8.195072,-9.879594,-9.085902,-1.175496,9.759528,-2.681176,-5.465695,4.471850,-1.729958,-4.261663,0.484584,-1.506436,7.301226,-4.861744,-1.108228,1.906749,1.264113,1.919005,0.193106,-0.329928,2.789509,7.623185,-3.978144,4.393652,-1.640646,-4.433240,6.772802,-1.920010,-2.076948,1.314265,-6.859771,-0.034019,-1.213501,-8.533827,-9.631716,-3.378993,2.796347,8.812567,8.903818,4.773423,-8.530046,3.892377,-9.482661,7.661380,8.442883,9.836851,8.227262,0.603674,5.098104,-1.462003,-7.287765,-1.183932,-5.834199,-5.265676,-9.572522,6.873015,2.506712,-0.808632,-3.526302,8.092964,-4.526004,-7.953096,-4.226696,8.632930,9.133074,2.495220,3.293348,6.787321,-5.637188,2.500659,2.598066,2.504195,1.755263,3.333755,7.056247,1.286772,8.235999,-7.973513,-9.333215,-9.344754,9.913415,0.833131,8.569465,-1.643149,-4.239264,-1.941594,-5.034944,6.929196,3.800399,-7.115227,9.502935,-8.589636,8.036063,-1.783298,-5.986061,6.335246,4.833129,-5.429639,8.040733,-9.108408,-5.586949,-3.949259,-4.063315,8.402996,-4.849617,7.419897,6.447920,-0.546353,-5.666750,-8.410911,3.272321,-8.304499,5.849876,4.932066,6.395203,-7.537553,-7.632698,-9.173343,-9.590138,-8.948715,9.372634,-7.442891,9.260721,9.751585,-0.642043,3.465332,1.722956,-3.253137,-1.616048,-9.564050,8.066332,-2.127868,4.797677,-6.212580,-2.202194,-9.162083,-1.989717,-1.216676,5.229356,1.001662,-7.173841,-7.162868,-8.597947,-4.795783,-3.988757,-0.681305,2.111110,-6.345454,-9.873004,6.430610,1.483130,-5.234051,-7.222558,-3.606439,9.577905,4.685372,-1.964861,5.636732,-9.658544,7.370975,-4.810130,-3.347694,-3.964287,-9.675693,-3.477174,8.659113,1.819981,2.676565,2.603829,-6.939903,-5.720906,-3.492929,2.252445,3.253785,6.281524,-5.564511,0.833685,4.177470,2.840147,-3.596685,9.757208,-4.496898,6.726651,4.877553,4.777732,7.165308,2.626812,-6.155571,-8.965107,8.426417,-7.505276,3.625399,-9.019772,-6.747039,0.664279,5.022115,-3.253875,9.885035,-2.290417,-2.049895,-5.040358,1.803828,3.742679,-2.357620,8.256518,2.459049,-7.089518,5.154402,-1.531014,-0.714334,-2.925709,-7.000748,8.525355,2.620252,-4.426614,4.913222,3.422232,7.741827,-8.679672,-8.421742,5.276792,-8.837926,4.775746,-9.122167,7.943710,5.347563,2.855845,-6.904859,9.269915,-9.318826,-0.474604,6.845140,-7.659341,-2.038326,-7.322301,-2.324372,5.010686,5.660219,8.339328,-2.770009,7.362594,-8.439409,3.849090,5.530769,-4.375859,9.966267,-4.412618,3.332835,8.402730,5.324390,-3.980540,3.480738,-3.072623,-4.016655,-2.312983,-2.791655,-2.096294,-8.881206,-9.007807,8.951812,8.882925,0.064615,7.470990,-2.456844,-1.542755,-9.236435,-9.783576,-6.374126,6.808961,-1.059538,3.568810,0.672840,0.608339,-8.878056,9.492973,9.569520,-3.063222,-9.003793,4.677310,-5.453566,7.514623,-8.062557,-5.330737,-2.746976,-1.669189,7.763290,-6.045265,4.258614,2.516295,8.285457,3.364513,0.799203,1.000548,5.851540,4.948404,-8.562330,8.581804,-0.005369,-6.009341,3.601592,6.284273,-0.255085,9.103896,4.358299,8.466221,5.364955,3.888702,-3.055217,0.858070,2.073069,1.405881,5.143604,8.283759,-5.036827,-9.095070,-6.528952,1.261103,3.654024,-0.916091,3.975840,0.507155,7.505508,9.283968,6.948200,7.933812,9.269122,6.084490,5.469886,-6.953176,-7.588087,0.689938,-3.917671,5.035492,7.697938,3.885271,-0.741994,-2.512184,3.138029,0.038175,-2.179858,-6.031828,-0.564039,-5.295506,-1.918027,9.879948,7.664333,8.703457,5.245344,-6.376265,-6.168395,1.611857,-9.024534,-4.436914,-8.871798,0.390231,2.216833,-2.193323,2.084290,9.338074,-4.887991,-7.390971,-7.447104,3.731886,-1.132386,-9.932035,7.046086,0.639508,3.688586,-6.805480,-0.261009,-0.303512,0.476022,9.382608,4.582379,-2.889134,6.014040,-8.208233,-8.953793,-3.827470,2.372808,6.736804,-0.133688,-6.754731,3.822540,1.596403,-2.771226,1.357896,0.457220,-7.451460,2.866547,-6.775896,2.136531,-6.457927,-6.225709,4.770848,-6.869494,8.275048,1.135814,-6.587507,-1.752463,-6.655670,-1.553238,-3.787567,-0.659256,-1.566682,6.112441,4.045486,5.018746,-3.818399,-9.806827,6.212961,-0.577867,3.295516,7.051243,-6.523574,-5.690715,-6.037723,-4.317645,-2.234354,-9.663380,5.652634,1.915445,-9.861584,-5.620259,-9.028593,-0.204143,3.438947,-3.386554,5.294143,0.530909,2.038873,-1.691118,-4.935384,-9.137399,-2.071861,7.056217,-9.871137,-3.066015,-1.514320,7.331199,4.075875,-0.252500,9.810999,8.961529,-3.833723,-0.196906,-8.277366,-1.159845,-5.577095,6.423415,5.807463,-9.797652,9.157903,-1.733914,3.866375,9.586673,-6.600898,-1.243528,-1.235242,-2.370779,-3.352532,1.551564,8.127373,6.480410,-3.659758,-8.535370,2.970318,-8.492187,8.196482,-5.017911,-3.704937,8.892106,-5.240297,-5.907801,-3.143332,3.598044,-4.633297,2.081170,-9.844354,5.077074,-4.167867,-7.544740,-1.479255,-9.697822,-8.113935,-1.864871,-0.639094,5.371512,7.705470,-3.506244,-1.350726,-9.344166,-3.092463,-5.544131,-7.457641,1.390426,-5.999589,3.932416,-6.623472,-3.350137,-8.172200,-3.233672,6.304307,5.996488,2.286753,-7.913640,-5.479600,-7.441492,-5.778113,9.016315,-7.924926,4.928414,7.992896,4.440652,2.097842,-9.536931,9.118738,-2.232870,-3.182064,7.803517,4.274477,3.065797,8.155587,-5.044224,-5.422257,-3.805747,6.396094,4.584750,-8.075736,-1.484153,1.233032,-4.526194,4.638836,2.551861,-5.736331,-2.302812,-0.183375,9.154331,7.420322,9.020018,-0.301183,4.017856,-4.616588,-7.318322,8.360106,-2.490731,9.404275,5.046267,0.703902,-7.096811,-5.980255,-9.512062,-2.764717,-5.974369,8.050663,9.523267,3.771873,2.483546,-6.171232,3.458071,9.986668,-6.036707,-0.363029,4.375616,-1.646650,6.240805,-7.418469,1.733270,-1.787937,7.751972,7.386803,8.046664,8.914263,-6.952667,-4.102760,3.800620,2.210705,-3.978799,-0.440921,-2.466075,3.317637,8.407414,8.155840,-9.012555,-9.290072,9.904548,-7.379561,-2.528739,-1.397904,4.128754,-1.507598,-3.723310,-5.341010,5.174986,-4.923535,5.596852,-3.316163,-4.123085,3.309942,7.422846,-5.921109,-0.524120,2.618937,-3.821107,3.963238,-8.727930,-0.188610,-0.579151,8.584561,0.341967,2.217899,1.503106,6.421639,4.201494,-9.303684,-7.850146,0.193842,3.365662,-8.544369,-0.664073,-0.118692,5.088447,2.093120,9.313977,-4.397913,3.143827,-3.639320,0.575088,-8.358536,-4.393525,2.320788,6.995402,7.041631,5.503883,-2.764781,-7.941207,-9.338105,1.189787,1.963922,-6.174536,-9.755108,6.158273,-3.175387,-7.311539,6.294694,8.356471,-4.800996,7.285742,3.430023,5.498747,6.620107,-0.214098,9.283091,6.926917,3.033712,-9.213663,3.454010,-1.283358,-5.594853,-6.614162,7.858049,-9.167359,-5.097288,-5.494614,-5.412026,2.376522,1.601001,7.285170,-1.588931,5.171280,-1.315739,9.299657,1.908366,7.627448,-3.739343,9.674661,1.249587,2.750473,1.329858,-7.355957,5.029818,0.969287,1.801175,-1.624000,-2.422247,6.621568,9.287681,-2.027991,-7.436202,2.720907,-9.237868,7.859634,-6.261667,2.174123,-7.906104,-4.179308,-1.513504,-9.853343,-5.924827,9.207649,-1.496439,-0.301729,7.277986,-3.125955,-9.494144,-3.825242,-1.481980,1.288292,4.017030,-3.289466,-1.434708,7.248646,2.686948,-1.335379,-8.100995,-3.115759,7.741297,7.945135,2.563297,-0.792696,7.775451,-1.099429,-1.905114,-0.838085,0.815731,2.895993,6.545493,-8.324068,-6.741317,3.453182,-1.736243,2.034000,-4.101916,-4.209968,-1.714430,3.201808,3.921448,0.463070,9.915728,5.660146,8.512258,-2.930107,-5.209294,5.505017,-1.243697,6.261441,-3.344131,-1.660175,2.268872,-2.653364,1.252280,9.507114,-1.328912,4.271069,6.583085,-4.245330,9.116661,0.347986,9.939932,3.217632,4.448827,-8.749292,6.828440,-9.417597,4.295323,3.844565,1.887165,3.392592,9.962756,8.533196,-2.422699,3.593318,3.359008,8.270543,4.281470,-3.805548,0.938004,-7.987310,1.292543,-6.546499,-8.500759,4.287138,-9.305538,1.178618,3.424627,-7.026487,-3.021075,-1.515673,6.209828,-8.440079,-5.506745,6.042529,5.282447,-5.203336,8.368974,2.824804,-7.269829,8.106959,8.885845,9.171370,5.045370,-3.531195,7.554215,2.633992,-6.279562,-3.878202,-3.450120,5.276605,0.055205,-8.749789,-8.781718,-7.685835,3.241562,5.374057,-0.520910,8.669993,2.443306,2.197741,-6.494044,8.046865,-4.872985,6.634708,6.463751,-2.175104,0.817638,2.469805,-7.567644,-1.849222,4.495018,0.910402,-8.414239,-7.350992,-5.561013,1.730501,-3.910995,-7.226514,-3.878621,-5.087888,-1.295154,-3.205749,7.118101,4.889130,-1.746990,4.243093,0.595064,7.232113,-3.797996,6.864626,-3.128541,7.365804,5.643329,3.444868,-6.396119,-0.596251,0.026329,-2.182074,-9.341562,-9.656626,7.770139,7.870828,-6.017999,6.152042,-3.043118,-5.653590,5.935016,4.712835,8.543697,-0.441087,-7.700004,-7.394901,0.358331,4.715452,-9.135209,-8.679929,8.824573,-5.096815,4.159853,-7.297332,5.071887,-8.279744,9.722669,7.023253,-1.726296,-9.724051,-1.373324,-1.841615,7.911501,-1.401563,-6.508251,4.999307,-4.672448,5.608506,1.448326,2.100024,-9.522591,2.392720,4.444096,-0.334042,-6.768493,8.078681,3.593919,0.397977,7.343580,-8.563114,-7.726738,5.297259,-8.929014,-3.835309,1.897938,-1.500416,6.593604,6.520629,-9.727038,6.657732,-6.779169,-4.164649,-6.056937,-1.909822,7.485191,1.662527,-5.828332,-4.377004,-4.773785,2.300514,-3.492150,6.824254,7.263593,-5.665362,3.877679,2.248262,-8.179346,3.272147,8.391391,-4.917650,6.735921,-7.153449,7.797846,-3.042868,-4.211757,0.430825,6.619802,-5.753756,2.312465,-4.898910,-6.858678,-9.751368,9.723379,-0.108445,5.446537,0.416486,-0.667836,-7.280239,-1.686135,6.229125,-6.785950,1.671470,-8.929834,9.571297,6.820368,-6.108291,4.886841,-5.704338,-8.590852,9.890635,-3.318184,-3.568851,-4.780703,-7.204267,5.604915,7.098046,-2.431639,5.163745,0.276063,-2.840543,7.543217,-3.000991,4.307518,7.474035,6.369911,2.070995,-6.240400,6.886416,-1.574365,6.239775,3.424952,-0.947252,-8.454753,-7.299910,-6.317848,-6.193035,2.782352,-1.935372,0.890785,8.514317,-2.216006,-3.646508,-8.166110,6.597647,6.775235,4.922895,-8.441999,-0.783491,7.210178,-9.165433,2.537307,5.388119,3.965331,8.688272,-2.904182,-6.040089,2.533316,2.862411,-3.751263,6.973084,3.977129,-7.390165,-8.743574,-7.861874,-6.945819,9.951907,6.794797,-9.855507,-5.458596,-0.080394,-8.872883,7.514273,2.016859,-4.270609,8.112446,-7.882860,-2.817809,-3.576651,1.774407,-1.571824,9.748816,-3.375567,1.675243,-6.510074,-0.065804,-2.304016,6.658225,8.463767,-7.349814,-0.358267,1.987495,-9.588782,3.888272,-0.285633,-6.923578,-8.019494,-3.291398,-9.587575,-7.456471,5.929014,6.845398,5.814774,6.412509,-1.240386,-0.804787,9.906189,8.144352,2.564937,0.105958,9.874538,7.986165,4.573116,-5.345168,6.868240,-8.668038,-4.711294,-4.818943,-9.095747,-5.649041,2.095621,0.160587,-3.064795,-7.886612,-4.569240,4.664820,7.332675,1.708242,-1.739887,0.818058,-0.866722,-3.754262,9.221509,2.732528,-3.272176,-9.015771,-8.126842,-3.335689,-7.067667,3.120857,-8.287059,2.908416,0.836023,7.485133,-8.591947,0.801325,-2.243572,9.423430,-8.083249,-0.704746,-9.344526,-4.317548,-0.853001,1.932126,9.959351,9.542675,2.831075,-5.707782,-9.269706,-4.071370,-7.937049,6.707168,7.140278,-0.924536,6.438956,-0.958475,-0.175535,9.316347,-2.049482,4.897966,6.698236,7.193633,5.071273,2.907178,7.298884,6.369429,7.426915,0.545060,3.874280,-0.932703,-2.319568,4.656358,2.615731,0.311331,0.804470,1.557697,-3.634582,-1.208892,-3.782916,2.878545,7.988971,8.026511,2.308366,-9.162259,2.789744,-0.277531,2.653165,-2.054690,-2.582456,-8.440952,-2.156099,-2.826612,4.342372,4.749724,-0.357711,5.014638,4.479674,-1.946430,8.247237,2.857094,0.087050,-5.020993,9.669800,0.018468,1.830069,-0.982943,3.944670,-9.903516,6.767247,3.423706,-4.941030,7.915128,7.715369,-0.841691,-1.739663,7.049868,5.952323,0.988969,-6.088304,-9.682848,-5.583087,-4.018244,7.602228,-1.299524,-0.078776,-8.878766,3.789637,-5.877951,7.566715,4.405258,-6.467098,4.956772,2.366143,0.502374,5.420265,5.017561,-6.323301,-6.221684,-3.924926,-3.454320,-3.234289,2.245616,-9.584748,-0.344133,-6.159545,-0.060591,2.099769,2.789637,-8.899405,-4.344858,-2.521772,9.106765,1.649834,1.319391,2.692399,-0.772223,-1.671051,1.168848,0.675244,3.474982,3.412361,1.019027,8.514238,6.184220,2.345226,-1.216353,2.913471,-0.617046,4.716276,-5.543516,7.557125,-4.577177,-7.207106,-9.443481,1.997826,-3.055500,2.732432,3.783589,-4.646253,-6.751690,3.297131,9.939849,6.535605,2.743316,1.435502,2.255677,8.141619,3.286269,2.195717,5.177903,1.919436,0.796072,8.567293,6.080861,-5.397635,1.854944,-0.606633,-4.958639,-4.788986,-4.278932,-8.860027,-3.735134,8.091980,5.471701,-9.177296,-9.843056,-1.231629,-8.919011,-0.675833,3.054530,-6.988761,-5.023742,-1.927898,-4.584916,6.676288,-3.577070,-0.904136,8.256463,-3.226760,-2.077187,9.543722,-8.081628,-8.296491,-3.479719,8.847530,9.795754,-5.971862,-9.024665,0.864100,-6.442779,-0.613142,-7.897814,3.867963,-3.212346,-1.850406,-1.546416,2.680541,-1.386373,-2.520516,6.844257,-4.883777,5.130656,-6.203458,2.312321,-5.908358,-5.639379,1.839790,5.623907,-9.287322,-1.386761,-2.404947,3.667372,-3.699168,7.085387,-1.913749,-4.206844,-0.849376,9.631779,8.923446,-3.143667,-5.393354,-5.418583,3.961728,8.845146,-4.837475,-6.594979,-2.496414,-0.544671,2.101595,4.209470,-4.584273,8.000288,7.698187,-7.755917,1.009507,-0.119779,3.841041,2.637474,-8.624934,2.932998,6.642961,4.619370,9.248008,-7.675772,-3.784582,-0.596215,7.984874,5.903000,-2.270290,3.545683,-1.699151,-8.921671,4.210630,-1.078163,-9.318716,-7.492162,4.098990,6.361389,8.490719,-1.658433,-0.435824,1.250992,-8.222004,-9.841379,-6.185518,-3.942581,-3.362387,-0.546815,4.373057,3.147691,-4.904567,0.214422,-1.785921,-0.425404,-8.004501,4.146475,5.842090,-3.308131,3.255914,3.892913,-8.434319,-1.439232,-9.196380,-0.657700,7.817937,8.363405,3.463500,6.934508,8.035116,-6.819988,-2.073281,-5.727832,-3.318689,5.831219,-0.159393,4.307039,4.932337,4.335371,-6.749619,3.003457,9.329002,-6.519402,0.187323,-3.328172,4.311705,-5.149476,-9.311128,-1.956624,3.941555,-1.346869,-8.329965,-2.408422,3.599558,8.870925,-6.884394,9.349594,2.071425,-7.212158,-4.883142,7.367003,3.730808,4.367355,4.841055,-3.577016,-9.796239,-9.875820,-0.427241,-8.481858,-7.039421,-7.822035,-2.700600,-9.026162,2.104298,-0.545466,-4.775025,6.850347,0.218460,2.769859,-0.522159,2.454003,9.039274,8.684291,-2.238492,0.226545,4.766242,9.707622,-8.470986,8.007082,6.864442,2.546081,-0.319530,8.939738,0.041396,-8.879268,6.678558,-7.884704,2.965950,-0.761714,6.233937,-3.188165,2.801114,-7.498776,5.952830,4.229858,0.493270,-9.175883,-7.557769,3.940878,1.416692,0.301940,8.288388,3.903320,-4.322266,4.730082,5.636261,-5.845158,1.851903,-6.784087,9.307103,0.397129,-2.713110,-6.966025,-2.748115,6.304162,5.003307,-3.928877,-6.185070,6.677142,1.884445,3.994849,-6.146357,-2.105630,-8.866702,-1.293088,-9.577088,9.117465,-6.625169,4.087372,9.498872,-6.108837,-4.628985,-8.135337,-5.746545,2.487819,-0.335052,-9.895900,-5.471519,-0.899145,-2.941456,-8.258838,5.539571,3.040179,8.695630,-2.526681,0.611489,5.288424,2.854185,4.784400,4.782645,2.095329,4.140462,-5.056810,-6.440421,-0.391483,-4.673971,-4.674793,-5.766762,7.635265,-7.942867,1.703676,-2.662825,5.207617,-3.846474,3.728573,3.531428,2.282396,-3.345831,2.154527,-3.871037,7.391407,-3.953210,-8.104824,-0.288858,4.421547,0.743011,-3.020072,7.317441,9.219303,-9.479206,-3.971867,-2.217810,-1.775046,7.613442,8.303231,-6.457417,-0.425999,-5.452082,3.898346,-4.060893,-4.045101,0.905171,4.425113,-6.485816,-9.971301,8.149833,1.149758,-5.292041,0.718951,6.941658,-7.244282,0.779566,-8.697165,8.583168,-6.081723,-7.118518,-2.506680,-9.948019,1.284898,-4.475295,8.579017,-4.274350,9.552234,1.668931,-4.951046,-6.318063,-7.665012,-8.721270,4.919768,-9.239913,2.893808,-2.324204,4.180617,-2.354379,-0.725688,-4.234164,-9.058866,-1.865896,-6.230495,-7.352172,-5.590742,0.823824,5.350751,1.506590,8.620991,-0.695252,8.962920,-8.419031,1.052961,1.515552,-1.379062,-0.691052,-2.221918,-2.373177,-9.988520,1.300110,6.920040,9.222318,-6.263960,-2.051182,-3.592813,4.462118,9.451039,-1.898618,-3.505106,-3.857295,-9.918132,7.047263,6.741567,1.722925,5.222871,-9.451965,6.452899,6.100047,1.083215,1.577633,-6.274978,8.949050,1.401746,2.310338,2.788033,-4.417657,-3.183728,-9.769986,6.979085,2.023990,-8.954499,-5.165521,8.167630,-6.807351,4.729506,-9.965213,-3.366575,1.507521,-4.927810,0.037842,5.032118,9.511687,8.877156,5.408511,4.824443,3.882025,1.444549,1.590677,5.164142,4.828840,4.095897,3.002429,0.340604,1.272418,2.958609,5.378697,-5.370111,-4.081314,-4.799159,6.422459,-2.489329,9.994900,-3.758639,-6.928593,-0.004678,-4.272300,5.521973,0.919961,-6.061247,-3.824525,7.816541,-5.241420,-6.101740,-1.402746,9.312904,-2.667419,-9.195183,4.722421,-9.928862,3.365275,4.085621,7.795372,6.043797,0.943737,0.746034,3.233811,4.136178,3.718857,-5.823368,-2.568840,8.355807,1.740181,-0.088170,-9.370143,-4.114455,-1.511734,2.759099,-0.845729,-9.292048,-9.996005,-8.760216,9.509203,-7.858189,5.642501,-0.656933,-7.191353,9.954495,6.157356,-1.004853,-3.297863,6.339442,-7.725813,-5.567299,4.216958,-8.422655,5.853876,5.969628,-5.255042,3.621553,-1.685812,1.139479,3.773435,-3.652322,-4.000963,-6.443175,9.447690,5.573766,-8.029892,7.104650,9.401428,0.915555,-6.700899,5.997540,-3.551331,-3.605648,-7.296384,7.606088,-6.850299,-2.878113,-2.100172,-1.125667,6.388522,0.929309,1.901083,0.601773,-7.394210,8.969722,-7.682723,6.324704,9.905415,3.150029,2.911145,9.727742,9.613072,1.176309,-4.058853,0.686251,4.488650,7.889250,0.295666,0.503573,-7.210371,-1.553142,3.416856,5.889067,-2.330897,-7.495265,-7.945919,2.743383,-5.157549,9.947291,-0.839131,-6.368069,-6.744913,2.218202,-6.791205,2.985602,9.380019,7.027488,-7.959010,-2.289448,-9.276514,-0.910095,-3.912556,-4.418034,-4.490684,-6.245214,-8.477593,7.015292,-2.059809,5.631968,5.534822,3.131801,-6.455374,-8.885134,-4.665980,5.713164,7.515000,7.962568,-7.662707,-7.417839,8.398112,6.773260,4.659934,-5.523213,4.383227,9.378975,5.263461,-1.460271,7.392745,-9.234018,4.363349,-6.610322,1.600791,-6.486107,9.636955,6.904925,7.993513,9.090532,5.554337,0.939883,4.455261,4.088219,6.009911,-9.233363,-6.981944,-3.984513,4.521525,8.671988,-7.096374,-3.094598,-9.744360,9.234569,-0.098013,0.843375,-0.368022,2.943409,9.026844,-5.790800,-8.848055,6.488133,5.499382,-5.379450,5.145837,-2.652943,3.649236,3.004750,-3.112718,-7.654374,6.895869,-1.607180,-9.064143,4.509275,-1.098940,-6.186833,4.960613,-6.215867,-4.096406,3.542742,-0.171712,6.590302,-8.142792,2.099155,7.374782,4.110507,1.535503,8.628333,6.885593,0.515518,-3.603313,-4.805654,-5.394795,8.668528,5.720931,-3.739605,-1.142580,-1.883450,-4.011512,7.240775,9.100317,0.568184,-0.724238,-7.027130,7.925674,0.777859,9.340487,8.767419,-0.383311,-7.804877,7.201186,0.641803,0.552326,-1.975408,-0.137449,4.285386,8.698682,-5.275896,4.762303,3.035177,0.239525,3.295224,1.317055,-9.893222,2.372119,5.556860,3.238222,-4.272830,-1.259304,-2.437341,-3.088626,-7.017804,-5.197387,8.459924,0.556270,6.956696,2.128429,-4.233544,1.538476,4.809711,2.725273,-9.097432,9.593374,6.302987,7.385432,-8.228421,-0.803029,2.768377,-9.912192,-2.543508,-1.003997,-1.909680,-3.996317,-5.754881,1.646374,-9.090658,-1.392495,4.531831,7.842451,-0.814509,-3.850900,-8.550553,2.521589,-2.686196,-8.579320,-4.434796,-6.647069,0.625318,5.366416,-2.484332,4.334468,0.345342,8.500188,8.859160,-8.192643,-0.283956,6.497207,8.589648,-1.188804,-4.569758,-7.656760,4.965073,5.950158,-5.847597,-3.399491,3.466690,2.090982,-2.573580,2.669287,-4.085722,4.143959,-0.772997,8.274385,7.401383,1.926533,7.461455,-4.941585,-2.383747,4.032451,-5.315406,-7.243535,9.282753,0.896768,-8.348689,4.712220,-6.961689,2.982320,6.933005,-6.724393,2.685309,-0.197032,9.051035,4.477096,-7.440707,-8.576194,2.536000,-1.535658,8.648304,-5.451418,-7.200616,-8.038097,-4.906895,-9.366424,-0.394887,-1.555023,-8.667633,-9.286885,-2.226029,-7.758440,-9.754037,3.326442,1.207998,-3.213284,9.755792,-5.640874,6.524585,-0.482322,8.086902,1.146058,0.624237,4.469935,9.226662,-8.870431,3.173446,-6.814020,8.034285,3.284145,-9.049422,0.666410,-9.209118,6.958993,-3.600024,6.585284,-9.950397,-1.028638,1.021787,-2.275526,0.525658,-3.293714,4.477494,2.359804,-9.001005,1.070547,-3.191684,5.612691,-6.852483,-0.415388,-6.916378,-5.986442,5.381168,9.765856,-7.004563,4.893542,-5.977141,6.676822,-4.924180,-7.554625,6.244654,9.563170,4.341859,8.618839,-1.293533,-4.538943,5.845584,5.027701,4.920616,9.129682,-5.115902,-7.821065,-8.905499,-9.278250,-9.660286,-2.669709,-1.516008,4.352466,-2.906399,-9.714511,2.676240,6.891987,8.311566,4.850356,2.431879,8.925400,1.886353,-5.312971,5.138355,-0.748813,-2.870306,8.038750,2.652103,-0.560787,6.181288,-3.739322,2.436807,-3.858913,-9.665893,-7.024673,-9.152573,-8.662639,1.953491,-9.209458,7.438342,-6.638377,9.063593,2.612384,-8.264844,-8.117813,-7.198329,-7.382044,-4.724203,-9.664760,-4.014428,1.967941,-4.563642,-1.160604,-8.496082,-7.409053,-1.866815,9.596603,1.455825,-2.974843,-2.974277,9.934664,7.881732,0.517386,-8.877862,-6.442789,-3.799107,-3.189913,1.680475,-9.583685,9.473965,-2.753510,5.488838,3.497228,-6.950891,-2.645623,-3.316536,0.209362,-2.163656,8.784249,-9.369632,6.003483,6.566565,-5.285774,2.603865,8.145923,1.450266,-6.275690,2.033540,4.940853,2.513486,9.550038,-3.525609,2.358057,3.966015,7.698344,-7.705052,-2.739007,-0.541198,2.346087,9.848312,-8.865959,-0.412960,8.250150,-1.426719,7.901654,-5.958858,6.075341,3.528490,3.145163,-7.810958,-0.665077,-9.268305,-6.485976,4.707531,-7.238881,-3.083773,-2.402017,4.743813,7.455638,-9.515622,4.531854,9.027758,3.338498,9.097367,8.514666,-0.042448,-1.948815,-5.206752,8.586422,-3.786876,-3.042885,5.900697,9.433191,-5.499222,-8.515109,8.886966,0.183600,3.833909,3.901765,-0.536746,-2.363584,0.349041,7.515458,4.228389,2.870622,-4.612933,8.630788,-9.067382,-5.412723,8.912883,-2.109010,-0.100803,6.585444,-0.843727,-8.666977,0.004929,7.214699,4.126459,-1.228552,-1.584569,0.295874,6.515902,-5.194862,0.549826,-0.152013,0.461158,-0.624457,-2.298742,8.975727,-4.685026,9.331990,-6.526124,-4.978564,2.334570,2.466899,5.850839,-0.291721,1.933039,-4.666617,5.905829,0.140822,8.775094,-9.760085,4.867687,0.005153,1.252494,5.608911,8.695861,-0.917175,-4.934525,-7.210845,-8.423635,-7.656225,5.597182,-9.997109,0.170593,-7.230025,2.278671,-8.014290,-6.475373,5.456215,4.374824,-2.632425,-0.812956,7.365782,-4.655163,-1.339225,2.512135,-7.523305,-1.350367,4.084571,-8.835035,-1.402311,8.271470,-9.726649,-4.464031,6.628979,-0.359085,4.851115,-0.092251,6.427807,-8.173445,6.913347,-7.692329,0.144489,0.693325,-0.843578,-2.028867,6.841877,9.502378,5.103770,2.997275,8.276871,-2.934359,6.407429,-8.472591,7.900533,-6.751053,-5.307630,-6.218784,3.798890,-0.934829,4.240300,4.580760,-8.112917,-5.239415,-9.958426,9.507151,8.716048,-5.644294,-2.866047,1.689629,-6.670586,7.641618,-4.624922,-9.279796,7.135144,0.241578,6.149463,3.914437,-1.301142,3.530713,-5.729737,-0.629972,1.665664,-9.496769,3.497880,2.591759,3.824871,-1.542793,6.558962,-8.363296,-0.006060,2.079200,-4.888721,1.437327,9.673821,0.242599,2.565156,3.687150,6.177318,2.577465,-6.478914,-1.940907,9.111618,7.339061,2.659377,4.007288,-9.352040,8.625284,0.696838,1.261419,5.550410,-0.578608,-5.253590,9.805820,0.231668,2.130193,-4.512433,-6.373810,-2.404650,-4.987302,0.018428,3.609351,-7.096637,-2.984471,-0.935710,-4.655416,-0.427534,-9.619922,0.610181,-4.156586,-3.389733,-6.583891,1.987485,-6.478868,-8.759531,5.869748,-3.167761,7.593531,5.798566,5.792296,2.199836,-0.075827,-8.573214,3.625184,-3.152302,3.678849,7.458965,5.396120,-8.755991,-0.243827,-9.132907,-4.191482,5.558205,-4.697399,6.124284,-4.293996,3.981013,-4.137304,7.753262,2.845350,-5.911650,6.135568,-1.648641,-2.667003,-8.171059,-6.853347,9.287886,-4.570265,-0.735481,4.728159,-1.012365,0.727465,-2.326612,4.579520,7.615980,-8.136995,6.496353,9.871021,-1.219598,-3.742547,-3.332548,-5.643656,7.414523,-6.666624,4.988406,4.550949,8.297718,6.335087,8.394809,-6.439946,-5.063217,-2.777553,-9.109710,2.040369,9.317718,0.471722,-2.861681,9.176910,-3.743073,-4.579688,-7.870697,8.370571,-0.567435,1.813861,-8.841274,-4.832486,-0.131503,-3.542871,-0.840686,-8.817718,-6.851472,8.140788,5.031237,-0.041559,6.704910,3.204001,3.417627,5.357718,6.500231,8.880788,-4.615904,-4.590358,-1.069438,1.143806,5.485631,-8.977383,-6.207559,-5.221946,3.503340,1.223133,6.133004,-4.559871,-6.873950,-7.925292,-4.809390,1.067900,0.849128,-1.150777,-6.336651,-3.378807,2.767411,1.834944,4.168334,4.758861,2.364989,0.543098,2.436441,2.222525,4.642641,2.240860,2.048497,4.893768,3.916486,-9.171310,6.290990,3.094300,4.386737,-5.004902,-5.209123,1.604325,9.224861,1.708056,-9.696821,-9.325624,-2.115894,-3.200760,-2.074274,7.587115,1.755738,0.227334,-5.992212,0.160810,-7.577610,-4.969902,5.642676,-1.942524,-7.893767,1.358806,-4.865191,1.865298,0.520879,-3.119381,8.058206,0.712772,0.688939,2.642086,7.130619,2.460067,1.785963,6.430691,-2.410124,2.086576,1.073865,4.694975,-2.282313,-9.338458,-6.872367,3.575623,-8.453464,-8.467750,6.643043,-7.233033,-0.074198,-3.040430,0.161783,-1.921164,8.428079,0.263753,-2.228058,-6.394850,1.859002,5.036243,6.064837,0.149167,4.590803,2.044912,9.543617,-4.147838,-6.606750,0.834290,-9.495422,6.900554,0.751132,-7.570373,8.841593,-4.980398,3.361422,1.163051,-3.648454,5.252914,-2.357267,0.778153,-3.384218,-7.572384,-1.444734,-4.018329,1.576404,1.836849,-5.600084,8.663954,-4.442912,-0.408752,0.515765,3.915996,-6.903025,7.402505,4.722598,9.968203,-9.175003,-4.483161,9.680394,6.603910,-3.063089,-3.930639,-3.690650,2.926448,9.735648,5.545854,1.700816,4.220540,9.176526,-7.036397,9.498191,-3.351333,6.140716,-8.548654,3.131919,-8.581654,-6.869104,1.574664,-8.218892,-9.447352,-1.455696,-0.160981,-9.098632,-0.306603,-9.163337,-1.269434,-3.149911,-9.643058,-7.501607,-4.407825,-6.544440,9.441480,6.089077,-0.176290,8.142333,-2.783187,-7.299507,8.023773,-4.688126,-8.726664,6.245260,-2.263873,9.812031,0.651466,5.691165,5.268871,-8.254406,9.710821,9.089252,3.381565,-1.668545,7.480067,-8.559898,1.829852,-7.261407,-1.433584,-5.762509,0.817157,9.698095,1.974718,-6.568639,-2.994130,-6.738699,1.131957,8.648006,-5.669990,-1.315374,-6.113208,8.997361,0.926261,2.804591,2.923405,-3.422948,8.055592,6.771224,-5.243945,-8.939733,2.982906,-7.516913,-8.657968,4.893811,0.699237,-2.870106,2.179364,7.443002,7.371102,-7.646138,6.030362,4.731434,-9.046460,5.989383,0.363047,6.283187,-4.804221,9.655079,-1.251788,-6.479420,-8.874603,1.651540,-3.973304,-4.604999,-7.699232,-6.413635,2.891771,-1.679325,-1.173625,-9.800188,4.688057,-5.510812,-7.777366,4.847036,4.671842,-1.210047,-8.485676,6.288633,5.074844,3.205349,-2.524197,2.938090,2.511994,9.297856,6.035800,0.598692,2.113812,3.009747,8.300678,-1.461963,-0.769980,-7.898868,9.613484,3.437847,3.072019,-6.628952,-4.576013,7.432094,8.492542,8.861606,7.072145,-3.836837,6.314241,-7.359197,-4.245276,6.688732,3.156522,5.481655,2.662162,2.980263,0.451423,-0.092905,0.869928,-8.971964,-3.748994,-0.958835,-9.718435,-0.241892,-9.989172,1.734949,-1.647285,9.284871,-4.849992,-1.954296,1.698121,4.020587,6.762236,-1.082641,5.405721,4.666679,-5.522863,9.635029,-7.233396,-0.911127,-5.464380,7.840974,-6.791712,0.018047,-1.663423,-6.725211,3.359236,-5.500503,9.750771,-8.394917,9.262655,-5.506800,6.119094,6.729582,-9.221486,-7.466697,9.739551,7.395759,-8.595054,-1.570116,-4.010802,-2.755217,-8.659248,-7.992350,5.034925,9.440131,-5.515343,-4.331566,5.582660,-0.688536,-7.882178,4.517720,-2.372219,3.972832,6.766729,1.208933,1.550163,8.611951,3.166779,6.872515,-4.209243,1.636880,7.036277,-4.216713,5.093500,-2.258369,9.427051,9.807654,-5.867830,-3.055335,2.992642,0.423071,0.087022,-2.780298,-5.242150,5.605924,-2.611869,0.293920,3.304232,1.262832,-6.785217,-7.265584,9.464637,-8.428517,-0.242539,3.844910,-1.984797,-3.837764,6.081404,-9.144914,1.778429,8.296091,7.343742,7.842342,-7.357703,1.884692,-3.730919,4.433155,-3.792674,6.451661,-2.647156,-6.184777,7.513962,5.491370,4.830355,-1.065709,0.413115,3.367356,-1.167880,3.290926,7.804291,-3.932119,-8.734559,1.350365,0.610863,-2.963675,3.108958,-8.431081,1.445472,6.715612,-1.297834,1.397476,9.280635,-6.825331,1.187820,5.536301,-0.770938,-7.654375,6.604264,9.521458,-6.498530,-2.188670,-3.764189,-2.055809,-5.266832,9.529171,4.651245,8.687541,1.644050,3.496667,6.085064,0.078528,-3.124091,6.072735,8.587962,-3.167482,-8.294605,9.330218,2.224213,-4.571642,7.381381,-5.339649,0.993612,-7.868367,8.452810,1.668975,-8.344592,7.803589,5.869804,-7.671750,6.827978,-2.683405,6.163973,9.046141,-3.084376,1.709811,4.101892,-3.901056,9.251414,5.028912,-0.732125,2.121330,7.439641,0.410969,6.231023,3.838676,-2.153894,-4.671991,2.504783,6.933349,-2.111806,7.302096,-8.715364,-7.568990,-9.050475,5.790190,-4.898714,1.591762,3.599706,-2.024769,-3.250399,0.476649,-6.888992,0.120457,5.576514,0.298990,1.106847,7.265006,-2.566070,5.053298,7.089363,-6.157228,8.851200,1.675557,-9.331393,-5.365290,9.898572,-3.432882,3.631153,7.271971,-7.013265,-3.920428,-3.543385,9.779105,4.832755,3.260215,9.673276,5.436835,-6.925695,9.503384,-8.939003,7.558390,-1.232004,4.576970,6.779378,-7.424970,9.065060,3.638430,0.998284,0.948087,8.387392,4.097867,-8.135830,-3.113731,-4.796562,5.931235,5.691845,-1.031309,-9.682073,1.469880,3.749096,6.461592,8.916803,-7.603459,-9.130341,2.762023,-6.040824,-5.788703,3.238721,4.527707,4.150544,7.782121,-6.337121,-1.523743,2.973415,-3.648126,6.423767,-7.153725,6.728825,0.359169,-5.060203,5.669705,-7.777854,9.074433,-3.025988,0.265909,0.169493,-5.808734,-1.278978,1.884785,8.690078,-4.390648,3.356553,3.083661,7.443328,-3.618720,4.836526,5.819479,-9.418118,-1.497083,1.567887,-5.723522,-8.481918,-4.639096,8.111699,-2.915296,-3.421943,3.576067,9.048973,-6.234971,-9.091218,-7.066142,-7.965801,9.342222,-7.298188,-9.794472,4.990778,2.024460,8.427535,-1.336367,4.505559,7.876220,-2.902328,8.626025,6.424837,-1.515032,2.094806,-6.121052,-9.435732,-6.256674,3.723597,8.769537,4.709405,-7.510160,-8.064190,5.221873,3.529534,3.441728,0.703673,-8.266838,-0.872394,-2.816680,2.546756,-5.188646,-2.958047,0.836418,4.647618,-2.139958,4.981805,0.510894,-3.294085,9.054564,-7.678656,9.203918,1.289906,-1.912072,-0.264415,1.575613,5.138113,-6.890581,-1.409300,5.635219,-8.998408,-7.589868,-1.425474,9.402656,-8.964229,2.772997,-6.580012,4.599098,-8.419484,7.257225,-4.858305,-5.599581,-1.151984,-6.083141,-6.465933,-1.059546,7.991675,-2.664715,7.085671,-0.997879,-2.876669,-7.250168,-9.595171,0.936759,7.682383,-6.138308,4.738315,-4.153850,0.475372,1.372398,-3.430657,-7.405470,-4.591271,-7.326233,-5.730288,-2.111134,-5.458342,3.255662,-7.657318,7.474016,-9.318792,0.283864,-5.280478,7.216574,-2.889933,-5.254957,3.701120,6.937966,2.901283,9.985227,-3.780712,0.374112,-5.088597,-1.397592,7.338797,-4.840953,2.336742,5.002689,2.918286,1.833444,2.376540,9.835919,-9.073721,4.212297,-1.611361,5.944140,-9.543307,1.568536,-1.700066,6.984593,1.676508,8.386753,0.829179,-8.884088,7.905473,4.327438,9.716247,7.497389,2.358727,-6.860725,8.072352,-0.055297,-8.715261,-3.411502,8.160547,-2.509611,-7.808092,3.332648,-2.858701,-4.899023,8.696436,4.990699,-1.921677,-9.345475,3.130450,9.385003,3.416107,-4.894763,0.552383,-5.935835,-0.233505,3.988522,-3.945470,-1.241462,8.865771,-1.940141,-8.230356,2.228110,9.570086,-5.548168,-2.457997,1.408002,-2.304250,2.922797,3.466180,-1.557158,-6.985032,-7.376585,9.553381,-3.568115,5.244883,0.787099,-1.779829,1.885378,6.751143,-5.699930,2.219815,9.311357,8.089846,-7.953750,-5.935671,-4.916799,-5.188837,0.339573,8.894298,-4.347032,-9.315071,6.237834,2.922466,-1.632642,-1.044917,-7.579137,2.423155,9.260991,2.028589,0.844240,4.391311,-0.303234,-4.494749,1.394544,6.414717,-2.621020,1.537470,-7.050784,-4.576195,1.884647,0.738650,1.413468,5.999761,9.950310,-2.763519,-7.610138,-4.005802,9.356294,-1.518318,8.340696,0.070726,-6.187611,0.259011,9.182191,4.066969,-3.711577,-8.010371,9.979721,4.926408,-5.139651,2.411802,0.607381,-2.200071,-1.721722,7.330069,-7.475878,-6.862526,9.662635,-6.727804,0.383760,-5.415813,-3.484499,9.065427,-6.053934,8.103521,-2.694631,-6.523986,-8.509711,5.397031,5.392140,-0.130831,6.894875,-3.196652,-3.837801,1.024727,1.315620,-0.949740,-8.408887,6.412468,-8.204537,-8.744822,-4.242256,-8.148888,1.746749,7.178558,-9.801170,-2.949025,-0.242570,-2.584020,3.409984,4.084338,1.026462,6.597446,2.325627,2.494735,9.997095,8.252732,-0.198491,-9.275559,2.914113,-0.609317,-8.344296,7.715259,-3.126341,2.444491,2.681162,-2.145545,-0.991181,-5.177432,-6.402234,2.212701,9.790445,6.444410,-0.650230,5.489759,-5.684402,6.568168,0.522979,6.180529,2.286291,6.279749,3.441709,6.740462,6.357190,-5.211609,4.116386,9.459670,-2.847007,-5.228620,1.541332,-8.974373,-1.653619,-9.708182,-3.132141,2.250247,-5.655586,-4.802800,-7.792790,-6.072216,1.189601,9.872377,-9.649404,-8.579589,-7.522290,-0.694651,-6.868497,2.910479,-2.310899,-8.538834,1.513350,-1.106774,5.078930,-4.901471,4.099824,9.403634,3.907428,3.135613,-4.320478,-9.335169,0.016964,-6.181355,2.056710,-4.806712,1.175134,-0.215320,-7.950992,-8.221364,8.597735,8.673449,3.916975,2.707948,6.298459,9.533592,-5.118341,-6.275670,-8.462145,-4.904906,-8.321836,3.327656,8.488935,1.760577,1.193013,1.950582,-0.369227,7.515691,-1.860431,-5.625374,8.012751,9.422508,2.135104,8.259596,-3.469281,5.292675,-5.930641,-4.709486,-5.706346,1.210341,9.571903,-1.149131,4.463461,-6.339010,-0.303129,-4.191770,-7.032391,-8.641077,8.212474,2.847978,4.308840,9.899351,3.412592,1.683292,7.147007,2.760939,-2.451402,-9.138784,9.034931,7.918823,8.572735,-0.060071,1.200853,3.815156,-9.895106,-2.179554,1.070361,-4.030485,3.974210,-5.823735,-7.288899,3.452930,3.922602,5.560595,-7.767813,-2.151761,-8.771125,9.903709,7.017053,-1.586551,8.166280,4.832243,-2.903055,-7.094634,-3.688394,-8.545944,-7.693360,4.408759,6.147405,1.852990,1.699032,5.007605,-6.754310,1.792330,2.664788,2.950223,-8.773846,4.853057,-0.604229,-9.404846,-3.271790,-4.419820,-2.789769,-4.156131,-9.241350,-8.159857,-4.624928,7.255075,-0.486475,-5.899598,-3.832766,7.799880,7.016811,-8.630029,-3.903181,-4.112124,8.838583,2.695010,-0.938549,-5.028002,7.782213,-4.039387,-5.740208,-3.366119,-0.850595,8.728201,1.646937,0.918559,3.425289,-7.348923,-0.497234,7.540222,0.456656,5.119585,-5.479072,-8.805902,-5.341499,5.904456,-7.270448,-3.332750,7.158162,-0.865414,-9.357093,7.700791,3.485290,7.988787,-9.446935,2.195328,7.220138,4.971894,-5.881958,-2.207115,-1.373736,-1.327709,2.993943,3.554017,-9.309926,7.373701,5.399172,-1.274634,8.763943,-9.342769,-7.060603,7.588901,-5.669962,-2.007093,7.840439,-3.053970,-6.070067,-3.656241,6.244296,-3.251435,5.787176,-8.227277,-3.182814,1.551243,-5.870156,3.107370,-3.993865,-9.030821,0.148233,3.141086,5.641219,-2.662287,-0.059569,-8.037256,-9.035369,7.796467,-8.334868,-1.385162,4.600174,-8.752776,3.414241,-9.582021,9.844615,2.609726,4.057085,8.516020,-8.104365,9.848906,-3.977733,-8.663894,-1.546695,8.835965,0.014991,-6.604080,5.258757,-8.158747,-3.277524,-8.416960,2.975289,1.057840,1.645592,-4.523620,-0.488768,-4.461399,7.094222,-2.141846,2.344625,-7.921089,8.428489,7.996958,-4.748735,-2.721444,-3.026193,-4.418426,-8.613685,4.765566,-7.489364,7.755967,7.852229,8.157785,-9.760940,-5.792019,7.254741,-3.108166,2.301396,-2.740737,7.606251,2.240274,2.506082,9.348923,1.489204,4.440274,-5.078680,-7.316344,9.777371,-0.082333,2.413288,0.195299,-7.428013,-1.494131,5.478325,5.492508,1.463998,-2.772482,-6.572776,-0.789036,-4.579157,7.044419,-5.030709,-9.278253,8.076758,9.921103,-0.549025,-2.095402,-7.927466,-8.484061,7.403859,-1.526005,-5.040268,6.452390,-0.453059,-3.795737,-2.030708,-4.676318,-6.185080,-9.141237,5.433839,-8.890246,-6.395952,-2.222213,2.979650,-4.687358,-8.823079,8.678161,0.824685,8.785455,-5.234134,1.948678,5.096761,0.951656,-1.083062,-0.647559,9.535425,1.468749,0.445819,-8.808827,5.266687,8.384228,2.763329,-6.821826,0.868425,9.400409,-9.977279,-7.291257,-7.578937,4.694045,0.992387,-8.059452,-1.202834,-8.441308,-3.361949,5.090764,4.052101,1.009368,2.750059,-0.468237,-7.752834,8.475183,-0.250934,-2.987876,3.197093,4.517343,7.659870,-9.749945,-1.706605,4.161996,2.479006,-0.581848,4.579869,-9.586424,7.290943,-9.739485,-2.955738,-8.086079,5.099325,2.255211,-1.013506,-2.745589,-9.720181,-2.121227,4.070101,6.078803,-5.187281,-5.883203,-6.296583,-6.298762,5.557816,3.420622,-1.003902,-9.257823,-3.010809,1.129537,-3.419486,1.399241,-8.637645,9.094479,2.307321,-6.820331,-8.063311,-2.200999,0.805436,0.952968,6.234228,-2.149829,-8.126129,5.755912,-8.086790,-0.391491,-2.933231,-3.195399,9.861214,8.608727,-0.924458,-9.891428,-2.097548,9.168965,5.932010,-7.927311,1.225115,3.040554,0.784794,5.269328,5.412491,-7.536158,4.231463,-1.725466,0.346336,1.576347,0.768827,-0.264014,-0.354681,-2.500391,-6.270446,-5.148519,4.516683,-2.698744,0.571511,2.052989,6.260938,-1.780626,-1.760379,8.336807,-1.299857,6.680525,-1.804237,0.148038,-0.645814,-0.225937,-0.631338,-2.434489,-8.468700,-3.812010,-0.953370,-9.811247,-6.290046,-0.704553,7.260347,-8.270119,0.135151,-6.258119,6.601959,-7.776693,6.907038,0.015893,-9.080088,9.496432,-4.402595,-2.824781,4.685363,-1.264464,8.035066,-8.422645,-8.291629,3.017715,0.803424,2.311436,6.404920,-5.073167,-2.644298,5.524411,8.275315,-2.962748,-8.705915,0.285628,8.768023,7.581027,-4.496675,-3.826291,-2.166480,-7.239542,4.695040,6.502274,-4.775045,7.261179,7.277709,0.505205,6.979670,-2.393535,-6.473543,-9.505583,4.525353,-0.133496,6.676852,-0.584832,-6.824711,2.524025,-3.697980,1.013140,-8.574621,5.519259,9.494690,4.164232,-5.315209,-7.784496,2.612345,0.487463,5.752801,-4.684284,-6.806202,-8.989505,-8.981942,-2.533430,-5.795508,6.406074,-9.594011,-6.805508,3.541129,-2.386707,8.543145,-4.888118,4.138789,0.899291,3.791612,-6.722497,-1.217132,9.985193,-7.199352,4.343902,6.707056,-5.247113,-7.511458,0.980571,-5.606481,9.619754,-9.979747,-7.035990,8.918738,-7.638837,6.395714,-0.062590,-4.542519,-4.256908,3.081552,7.126056,-5.135603,-9.205221,8.734106,-6.173419,-1.495305,9.924988,5.045981,-0.259726,-7.177237,-6.478917,2.251820,5.569664,-2.425573,9.704965,-2.488990,-7.287602,-2.627965,2.844084,-3.723311,1.485281,2.856062,1.264277,-5.656219,-7.624346,5.120929,-2.313015,7.833344,-5.608197,-5.192520,-3.274957,-0.324860,5.814638,0.828416,-5.659694,1.200443,-0.125991,4.223272,9.943947,-2.970818,-0.504617,-6.352797,-8.748969,-2.510133,8.618840,-2.619434,0.836262,-3.841961,8.270737,1.223162,4.916680,3.355114,-7.792153,-8.010338,-0.107357,3.458563,-6.381953,-0.185046,2.803781,8.481899,1.329817,-6.528187,-0.524582,4.889563,5.640548,-4.498413,0.912215,-9.718729,-8.833973,-0.509810,2.243176,9.240312,2.988917,9.958831,-7.958440,-0.385184,-8.622135,1.814738,4.081081,2.752897,7.139091,-5.987700,3.920429,-0.152158,3.134611,1.527442,-5.812584,-5.424438,-8.052973,3.177158,-8.987164,-8.296285,-3.487769,7.074233,-2.814776,-2.883819,-0.199008,8.559784,-7.908856,9.589183,-9.911785,-4.796575,1.669979,-5.496229,-6.125353,3.535181,6.265097,-3.945786,5.617007,-9.531329,-1.970827,2.165030,3.342925,-2.424460,7.392272,2.292572,-4.002234,-4.774446,-0.600432,6.378188,-6.529621,6.068842,-3.095247,-3.518124,1.867093,-9.911432,8.449835,8.277061,-9.566584,-0.474856,8.240744,6.194908,-0.848910,-4.619822,-8.883811,0.042721,-3.305510,6.928682,-9.602546,-6.042837,-9.542738,6.954800,-4.813760,-3.864569,5.617507,-4.712031,-8.061889,-3.894513,-9.768267,6.299212,3.789521,5.696221,7.095362,-6.383168,-5.362242,9.505645,1.187709,4.641625,2.957058,-4.303438,-3.853516,-6.291869,-4.467818,0.912544,4.174258,-3.446868,-0.474176,-9.468453,-2.680986,7.681127,7.615927,8.766587,-2.662429,-5.926316,-9.119808,-4.402050,-8.556719,5.613976,9.148049,0.827547,7.101243,1.754622,3.086071,0.848408,2.993121,1.748973,1.105519,9.229692,8.060785,-1.144208,2.315764,-7.039726,6.463923,-4.232315,5.982442,7.197138,8.806956,-2.199851,-6.160479,-7.478939,-9.444669,-6.647723,-5.355570,0.892519,0.326180,1.270801,-4.880594,-9.041744,8.712984,3.778036,-9.245933,3.342803,0.611443,5.853511,2.065974,7.260463,4.842506,-7.300468,-3.016625,6.874026,0.604262,-3.756678,-3.898898,1.968682,8.827528,-5.874759,4.483825,-3.057459,1.911418,-8.834119,8.449903,1.743369,8.367234,3.273705,0.559761,0.241676,9.882095,6.736884,2.162453,-3.018218,0.346241,-3.883419,-1.401062,8.887003,-3.288076,2.776006,-8.101792,-5.369967,-0.794316,6.901486,-6.496355,-0.138074,-0.735948,-1.413721,-8.204678,-7.002174,1.825029,-4.649540,5.942434,-4.785715,2.171633,-8.534096,-5.934909,9.842165,-8.374503,-4.153643,2.176921,-3.138999,-1.063595,6.325639,1.969086,-1.563760,9.946058,3.153978,2.896723,-9.190756,4.160144,-1.380207,-3.051630,-5.584919,-0.080494,3.975292,0.947787,6.008367,-9.693013,-7.421309,-9.712233,7.416592,1.017753,7.121047,-2.834046,4.611496,-3.853374,9.696049,3.530575,2.919209,-7.358807,7.668652,-3.226079,-9.086022,-3.542916,3.112343,5.945490,-1.691021,7.912683,4.246002,3.930247,3.048807,-2.487865,-8.237275,-2.153831,5.004457,3.644221,-2.522466,1.542679,-6.300627,6.236381,1.937653,-0.954733,1.659786,6.916781,2.202878,3.747193,-4.270772,3.725848,9.508558,-4.691733,9.243624,0.134653,1.517318,-3.951629,-7.663044,7.819549,-1.110522,2.016074,6.077772,1.256309,-9.782461,6.559243,-9.441684,7.891125,-7.962771,3.463040,2.185364,8.781862,1.236043,8.247350,2.036348,6.806011,-2.150021,5.143668,8.539574,3.542008,1.179669,-2.754814,6.230934,7.541270,1.312036,7.784355,-5.853730,-3.105199,-2.695249,5.477586,-9.717649,-4.021739,-4.612288,1.381114,-1.331646,4.069565,9.895116,8.145502,4.257225,5.525146,8.029471,-9.908106,1.644303,-0.349110,-6.952419,-4.649051,-4.285066,4.570734,-5.900270,2.036373,4.604879,3.331714,-1.990366,-9.462357,5.395166,4.602013,-0.499334,-0.910986,-6.796828,-1.420854,1.143248,5.926450,0.998555,-8.027910,7.740418,-4.680427,-4.563346,-2.101820,-5.577099,-2.418835,-4.480753,7.765373,2.262745,-1.608514,-6.956822,-5.384988,4.038493,5.292196,2.569955,6.709017,1.740650,5.233678,9.153772,6.296398,-8.559323,4.355869,2.500171,-7.640390,9.864866,-0.559148,7.051017,5.991054,-6.262938,7.923646,-2.509591,1.679567,-8.370585,3.441814,-0.287794,4.896316,-8.019408,0.371642,1.071007,5.055229,-3.117170,-8.597738,-6.166317,6.350095,0.992890,-5.112354,4.370308,7.977020,9.388123,6.454664,2.168669,-9.397638,2.887387,0.057826,3.184972,7.564947,-5.738314,4.624357,4.547323,-5.681472,6.951416,-5.710641,-7.241937,-9.403323,-7.462865,4.867775,8.547496,-4.276775,3.193587,8.729192,-5.406522,-8.978895,1.265181,5.718138,-2.070874,8.833076,9.718036,-7.760572,0.686105,3.677434,-7.885763,-7.538643,-6.098475,5.841167,-9.424956,3.416854,1.060751,-1.619387,2.011163,-6.331996,9.266299,-7.242440,1.464593,-6.743900,5.915759,1.393001,-8.889946,6.378634,-3.489105,-1.708527,-4.394526,0.692077,5.131663,-5.975148,7.422526,2.078158,-5.241368,0.611974,-0.225259,-7.170942,9.459559,-3.128727,3.694580,6.976380,-9.462400,5.362889,9.407423,-4.200354,-7.704563,9.546328,0.134197,-3.985713,-2.759710,-5.982102,9.048998,1.952696,-6.183917,-3.576124,2.681896,0.688849,6.503853,-8.888842,0.675185,5.450493,2.912731,4.016935,0.820213,-8.461146,-9.193449,8.731565,-8.094265,-7.224560,-2.997886,-7.519877,-1.675258,6.570762,-0.430040,-5.976106,-1.024122,0.217678,6.090783,0.268254,-6.233270,-1.241946,-8.491625,-6.327634,-2.949516,1.198989,2.304478,0.861269,9.309874,7.913635,-8.894298,2.445604,-9.636812,1.676752,8.850141,-2.971674,-6.910400,-3.683926,-1.166500,9.322133,-6.934480,4.000884,0.812031,8.671270,5.472835,-9.201954,4.835369,2.568110,7.933456,4.775605,6.796486,-9.695392,-7.696754,-4.016488,-6.274725,-9.901483,-5.623252,-2.405528,-3.798340,-8.112863,7.799184,3.076437,-6.759098,-6.111373,1.066814,-1.470775,8.245574,5.564508,-6.721339,3.274698,1.439283,4.654826,1.074435,3.491513,3.191557,-3.585096,6.378067,4.650191,-2.639771,7.972174,5.615600,-9.521081,-0.214817,5.919445,7.251358,8.451899,-6.341789,-8.070232,7.594631,9.222851,3.432984,3.273833,3.207760,-1.517194,-4.152599,-0.774918,6.791887,-9.261631,-6.787483,-6.388475,-7.672227,-4.490723,-3.088952,0.295823,1.209161,2.982906,-6.466978,6.764512,3.371833,3.002444,4.346480,-0.383078,-6.114198,-4.719427,-9.547683,-0.681437,8.800278,3.462532,9.208780,6.607483,3.929512,2.928190,2.324975,1.514065,-2.876614,-8.419174,-8.739002,-4.733997,3.445915,4.229762,-0.375684,9.860163,5.068478,7.067367,3.910056,3.113643,3.704862,-5.707569,5.954467,-2.411817,-1.481517,5.724806,6.262584,8.834036,-4.503945,-0.001491,-1.076579,-7.913644,-8.803660,-7.420843,-9.557050,-9.943164,-9.234114,-8.710690,-7.134255,1.892241,8.508071,-2.170346,-9.301373,-6.201572,-6.698433,9.382434,-5.616913,-6.042972,-8.667467,-0.529921,-3.381342,-8.105034,5.521936,-4.021329,4.989574,-9.819455,-5.977918,2.973594,-7.120622,-0.508071,-3.125542,9.891247,6.981447,4.298509,-7.203111,2.772123,-7.664081,9.170399,-9.693360,-9.090685,6.432990,1.383940,4.152791,-1.626205,-1.729348,-3.807140,0.218900,7.762138,-3.630309,-9.545390,-1.450638,6.175462,2.973824,-7.975066,5.251705,-9.771934,0.772703,-9.038724,-1.317479,-9.127271,2.512363,-2.404444,-6.162743,-8.765097,-3.399757,0.997221,-6.984806,-8.578247,9.484492,0.304156,3.483251,7.043535,4.683200,9.119096,-9.845193,-9.081576,-3.561834,-3.464393,-3.188207,2.004979,9.431064,6.877181,-2.121240,-1.666080,-2.197582,-1.760960,5.032624,-6.804249,1.442911,-4.696204,0.660080,-3.037762,7.850274,-2.776430,8.181823,8.879701,-0.520224,-4.444167,-4.724844,-7.711764,-8.398655,-6.090240,-8.863244,9.168816,-3.957814,-0.516128,-3.933083,4.238667,4.747024,-1.400973,-9.339231,-5.264160,-6.910454,1.195341,8.052004,-8.433096,-8.425651,6.130532,8.925456,-8.671431,-8.841158,-9.156282,1.684574,7.048612,7.852616,1.305789,5.998827,1.822040,-1.355894,-2.111808,-6.140541,-9.844433,5.683961,-4.522169,-7.158833,-1.120947,3.715744,5.658938,-5.930479,7.808499,-8.602165,3.411780,-7.859360,-6.286315,7.563334,-5.370042,6.658436,-9.206022,-7.440364,7.648599,-4.005056,-5.209140,-1.560998,-6.290724,-8.302667,8.534248,9.420233,-7.159092,5.600024,-6.512606,4.354347,-6.829431,3.510772,3.292676,9.447189,-1.143276,-2.457729,9.031746,8.519710,1.148586,-4.746531,-2.379920,-4.478340,2.506411,7.882213,-9.170783,9.823204,3.556794,-3.542363,-0.197674,-4.627702,9.767107,4.311036,6.647970,-3.472579,-4.025272,8.942056,-4.485736,1.620255,8.308593,-8.865719,1.114183,8.424033,-3.584729,7.648008,2.403283,-6.719973,-6.857943,-2.027472,-2.844399,0.019319,8.465198,6.514754,-9.044042,7.945019,-4.474495,4.698800,8.008213,-7.324895,-3.579936,0.697515,1.072630,-3.170218,4.590659,-5.680347,-6.951477,0.127470,-1.966727,6.555084,0.398944,8.281136,-2.744682,-0.289297,9.829637,-7.057551,-0.680109,0.309329,7.816429,-0.282702,-0.460300,-3.812883,-7.450774,-9.825490,-4.264411,7.596292,2.310614,1.940607,0.181257,4.225490,3.077761,2.459722,8.774304,2.541011,-5.781404,-0.502607,-8.209964,3.206746,-0.043999,-1.536128,-6.592425,-4.113504,-9.747025,1.777982,5.716799,-1.197523,-6.667909,3.029329,-6.498572,-8.435668,-0.380646,-4.625695,1.305353,7.038154,0.063313,4.369337,0.652331,8.188491,2.669739,9.664296,-0.700082,3.347769,6.317832,-2.495687,-9.855717,3.919122,2.030910,9.787755,8.475534,-5.110883,-2.777096,-0.126280,-8.720567,9.215021,3.050648,-0.595950,-8.163766,-9.747412,-8.560735,-3.474028,-3.524508,8.836543,4.794508,-6.542557,6.630311,6.394714,-8.317483,1.689475,-9.551599,6.565725,-6.019552,7.329046,9.206248,-3.918605,-2.327456,-1.565094,-6.625202,6.073064,8.476421,5.733095,-3.100844,-6.098323,-2.317919,6.486363,0.233978,-6.439155,8.742363,-0.095301,-2.545273,-9.682342,8.363226,9.190418,7.108136,4.231813,-3.583112,8.192817,-3.692911,-9.262787,-5.024256,6.742383,-7.992530,9.025528,6.886598,-5.926951,-8.481867,-7.860097,-7.276076,-6.699370,-7.716342,-2.222963,-5.907246,-0.568825,0.840892,3.733673,-4.581883,6.160515,5.152193,-5.012556,8.168094,-3.386519,-4.883904,0.459340,-9.567286,-8.680805,-7.157533,6.932181,-7.047897,5.919070,-1.358267,8.585803,7.181363,4.033581,0.455390,1.894033,0.409514,7.686248,-2.154032,-7.813796,-7.439244,-9.164801,3.104129,9.422576,3.781440,1.139605,0.311080,-7.094642,-1.243405,0.653574,-3.966078,-9.503698,-0.077258,8.878455,-5.246786,9.550877,-2.624890,2.004731,-7.307057,9.515160,8.668887,4.459143,-6.714053,6.603922,-3.428565,-7.640227,7.369805,-7.817775,-1.601407,3.716996,7.950649,5.533055,-0.181021,5.684004,9.816213,-8.253436,7.846962,-7.983734,7.537582,-9.930269,-1.822678,-9.899646,1.649152,-9.959244,-2.452446,9.706637,-1.431252,7.598774,6.862103,2.170230,-4.657266,-5.139318,-5.074815,9.098120,-2.146495,6.075350,-7.862313,9.239490,-2.012577,-6.498900,2.513472,-0.729112,-8.356966,-4.435940,-8.604621,1.188770,4.175258,-7.124801,-9.222431,4.429117,-6.483191,3.170645,2.529248,-9.118158,-7.898923,-4.848387,-8.812998,-0.471180,8.334370,6.833801,-9.598949,-7.176128,-9.979236,3.898644,-1.317813,5.987961,4.285575,1.380496,2.474989,-4.086773,-8.502060,4.801635,5.335298,-4.140691,-9.459076,-5.467426,-0.030805,-7.129624,-0.598396,3.748812,2.214108,5.086451,8.238013,7.370822,-6.863335,6.773192,-2.567775,-5.653638,-0.442089,-7.379899,-0.531687,9.335502,2.668616,4.239877,-2.260993,-9.638162,6.919190,-6.549949,9.930783,-7.452819,-3.378556,-4.335261,-7.669395,-0.280594,2.131043,-5.699931,-7.927130,-2.786103,1.257846,9.681432,-8.977863,8.698075,1.027612,2.088448,8.756460,-3.637904,5.863951,4.758570,7.768949,-1.567406,-6.058819,-3.653034,-9.407676,8.597927,-6.113623,9.203520,-9.409772,7.575337,2.621226,-6.530272,-2.593081,-5.872535,-9.796822,3.097433,4.489598,-6.262155,-7.209182,-2.454774,-4.626834,5.766239,-2.134333,2.035070,4.339937,-1.875852,0.110506,-2.315213,-1.693034,2.316733,-8.140351,-5.595908,-2.089757,6.954271,-9.260192,-4.266642,4.535522,2.874818,-0.839167,1.532657,6.276668,-2.403160,-3.621374,-8.860490,8.988023,2.844806,7.826371,-7.035803,0.742994,-6.596018,9.677141,-4.889976,-4.235537,4.932913,-3.233813,2.287965,-1.680220,7.026039,-7.759316,4.593509,0.213308,3.299317,0.517806,1.979033,1.131085,-0.508715,-1.922102,-0.818681,-1.780174,2.667958,-7.305672,8.057410,5.132791,8.170878,-4.900872,2.967673,-3.920081,-6.817441,-0.503740,-4.271891,-1.457251,2.177501,4.153156,9.577346,1.268847,-6.503576,4.996697,-5.719546,-9.627936,-9.985491,3.549298,1.042177,-9.813582,1.384853,6.765027,2.816555,-7.045724,-1.945622,-0.311124,1.218948,-0.562762,1.160796,1.283734,-5.233360,6.197747,5.873733,7.944496,-3.853886,-2.217347,-3.551254,3.853125,9.233607,-9.997515,6.977255,-2.271437,-7.711585,4.737139,-1.844778,-0.331079,-4.373129,-2.400771,-7.538572,-3.257858,5.892171,-8.897188,-3.202481,7.733907,9.637968,1.111029,-8.841857,6.601339,7.856334,-5.567689,-1.384044,-1.786320,1.708750,-5.011596,-0.342426,-5.219769,3.293724,-2.533621,5.205387,-2.612472,7.535469,1.990965,0.660413,3.813254,0.855021,-3.317241,-3.394712,3.014102,5.880567,6.112102,-6.288440,-2.672673,-5.611053,-4.653920,-5.699101,-0.471276,-1.327765,-7.013803,-9.432713,-6.730095,5.217885,1.623813,-0.879163,3.017086,-0.282838,9.077218,8.354084,1.489808,-3.282870,8.170662,-8.363963,1.791000,3.060070,-1.851019,2.459766,-0.569863,7.855188,-3.420928,-4.858358,-6.658957,-7.991206,6.602161,1.986241,1.319139,-4.072871,-3.394846,-6.672603,-6.399014,4.018669,3.784655,3.493365,-2.053538,-8.045555,-8.880133,-8.158513,2.523222,5.649065,-4.524308,3.065955,-7.696247,-6.629023,-2.041916,-9.466432,5.143477,1.823945,-1.668531,-6.628857,-8.601817,5.160915,1.140909,5.740469,-5.713445,0.410587,1.336814,-1.332923,7.733830,-3.500763,6.540231,-2.492288,8.629297,-7.566577,-5.796229,-5.680381,8.039102,-4.328313,1.413175,0.107008,-2.471544,2.326589,-2.224363,0.501241,-8.013451,9.678898,9.529319,-7.226530,-5.905580,-6.197586,5.289617,2.598948,3.397919,0.785553,0.935044,-7.709288,-1.034306,5.664256,-5.566013,-4.444196,-5.283333,-3.159881,2.325085,-3.895665,3.069400,-9.014377,3.644648,1.936334,3.568273,-5.112949,-0.891046,-2.973800,-9.905822,2.274865,7.842223,5.904412,0.622917,9.323113,1.662960,-9.791518,-9.702874,4.101886,-0.279187,-0.297354,-7.812001,-3.947861,-5.116227,7.302881,-9.810219,2.620153,-9.123490,-4.947611,-2.038160,-4.212073,4.493648,8.602039,3.560891,-7.623763,4.392894,-6.299242,2.887096,-6.648191,9.997488,-1.852746,-6.599316,5.981581,-0.992774,8.262780,0.159544,-2.932395,-0.729287,0.258605,6.944257,-4.564615,-9.972841,-9.998894,8.430505,9.894390,-3.962921,5.154455,9.991744,1.390514,-7.617288,1.008116,-4.948038,-8.728702,0.748510,-8.311992,9.224287,5.826761,3.627424,0.561416,4.409141,-5.415599,-5.436710,-4.011887,-6.684689,-9.128490,-8.835162,6.662485,8.840715,-3.204312,9.768376,3.874434,3.544919,-5.331821,-2.057445,4.416275,0.792359,4.502386,7.810721,1.718493,6.739800,-4.165059,4.727315,-7.419590,-5.370098,8.130507,-0.212273,-7.517365,-3.357888,-9.579891,8.122338,-7.029629,7.920030,-7.637598,1.407872,2.473299,6.577965,5.790121,9.579408,-5.039667,-2.182000,7.142887,-6.782637,-7.709881,-1.763825,-0.411687,-2.843630,-0.347792,-1.011546,1.956648,0.263162,7.698121,-8.521123,3.506246,-6.243962,0.396244,-1.103511,8.516410,6.852494,4.718662,3.679791,8.716225,-8.004529,3.609898,-4.359562,-0.577348,8.596175,3.021739,-2.394378,6.375607,-1.653106,6.322693,5.380584,3.152545,-9.967692,3.095996,-9.691788,-3.469206,-5.716956,-6.766699,-1.422885,-7.185044,-5.530092,6.919841,9.748834,5.102196,-0.239018,-7.656881,-0.291301,-1.062566,-3.284805,-0.280733,-6.611813,8.264498,-2.199481,9.564887,-2.884019,3.978868,5.803357,-7.008783,9.689945,-7.797731,-1.697164,-4.039145,2.480824,-6.781828,-1.852499,-5.568643,3.311159,3.239475,8.605380,-5.217426,1.699175,-7.802260,-3.942836,8.659136,5.825981,3.031243,-8.586975,-1.341674,-8.924931,0.819039,8.315571,4.257408,1.576082,-2.908841,-1.514009,-7.247975,-7.175360,-6.552162,9.741986,6.144669,-6.539372,7.365494,-2.318863,-5.155947,-7.748759,9.440993,8.498033,-1.519367,8.745954,-6.158993,5.805232,5.737133,0.304249,-4.332091,8.960830,1.254347,8.147082,-2.144467,-6.347320,-9.665688,-0.914004,-5.124498,6.830321,-4.180616,-1.433337,-5.952886,-9.418490,7.666572,8.855488,-2.592341,5.114772,-7.014461,-4.359342,-6.419045,9.635088,1.063310,-9.102500,-7.130595,-7.389325,3.419619,6.966964,-2.552695,1.231189,0.310448,-5.997188,-2.178709,-8.769211,-4.070049,9.494661,5.628828,4.294883,8.176847,6.091156,1.936451,-0.119562,-0.614196,-9.045790,6.400015,-6.468620,3.817660,6.488377,8.138934,-4.277598,-3.064995,-3.852669,5.962457,9.680716,-2.852102,-1.165310,-6.094684,-2.613185,-6.912378,-8.498263,-3.653315,-1.672984,7.265145,9.672152,0.146000,-5.608641,-0.616075,-8.442008,-7.624567,-5.324865,-2.548907,8.352477,7.109863,2.012926,-5.828309,-2.030140,-2.517740,-7.798207,-6.529168,-8.850736,-0.985798,9.917748,-5.445809,-5.376888,5.887147,0.884147,9.616930,9.229793,-7.435937,-5.817559,-2.103339,9.875085,7.763964,-9.204065,-8.274771,-5.170723,8.415145,3.323548,0.115807,-6.725376,-7.220686,-9.043830,-8.986652,-7.456862,-9.499439,-9.821913,2.437742,6.683598,6.248146,-6.090547,3.667990,-5.318735,6.899545,-2.178439,7.803457,7.426080,-7.829619,0.041974,9.406933,7.439299,-8.615512,-1.325121,3.437090,9.000292,4.329311,-2.455125,-4.282891,3.033583,-4.664805,-3.024532,5.673539,4.186658,2.473580,-4.930696,7.106348,-1.528007,3.983197,5.124899,-3.098313,-5.990331,9.809791,-7.947164,2.965229,5.352180,5.861087,-4.168828,4.650529,-6.531281,-3.190939,-6.425417,-3.758780,-9.284686,0.111604,6.382084,-7.135160,-2.152238,-7.835103,8.392560,-0.741150,-5.790500,-7.873314,-8.790442,-4.749469,-2.238494,-1.806042,-0.448022,9.736197,-5.482739,5.105829,-6.302479,3.592485,8.503189,-5.298836,-5.543675,5.259144,-0.499796,6.883206,6.196684,-4.102057,-8.825020,-1.017479,2.776296,7.584346,1.813034,7.356325,-7.169705,-6.157918,5.103367,-5.534337,0.411621,-1.342555,0.412803,0.241926,9.458722,-9.624362,-6.215579,7.180967,-6.190409,6.867574,7.939559,-4.970847,-6.438509,4.313272,3.154697,6.562320,4.880475,-0.036552,9.775999,5.706852,7.593903,-0.910406,9.697158,-9.819996,5.816298,8.026116,-4.542178,-7.512234,-4.004806,-1.267275,-0.512723,-5.975522,2.520029,-8.986275,-1.278840,-4.801059,-1.997566,3.300070,-0.453428,9.117969,-3.940928,-1.395522,-6.656245,8.816535,-0.060213,-7.418709,7.017964,-5.178238,-1.858715,5.244679,-8.200082,-3.742810,-9.510559,-5.217384,4.700083,-2.757328,-1.199717,9.176201,-9.579058,4.630392,-4.243281,5.552951,5.571880,8.191328,-7.117958,-6.221565,-3.453777,5.639265,4.617342,7.460710,-7.808889,-6.603202,-5.564612,7.434307,-6.248965,8.149127,3.544159,-0.892097,-0.816955,-4.190472,-1.318796,7.634169,9.196846,0.289554,9.529970,-3.049315,4.380349,-6.557161,-7.944582,-3.177102,3.066212,9.889479,-9.725435,8.637154,9.478623,8.403623,-2.133796,-4.575666,-9.497871,-7.827030,-3.658907,5.896130,5.756158,8.465516,0.072385,-9.266601,5.227730,5.722077,4.868450,-7.469131,-3.667746,-5.881703,7.786828,7.879382,2.803955,0.878000,-7.331956,7.251527,-3.474746,3.538511,-6.083092,-7.664922,7.924495,2.194091,-0.136753,-0.532451,5.635212,-5.532185,7.490060,-8.361349,1.621132,8.828172,-2.449338,-2.968254,9.957527,3.157463,7.346655,-5.818760,9.299662,-2.783233,0.168114,5.746191,5.114588,2.523131,5.634832,7.719970,4.901615,-6.078921,9.120051,1.299974,-8.564727,-9.711194,-0.524100,-4.672255,-9.323764,-5.800788,2.178859,6.330495,6.349854,-3.358708,-9.229901,3.048898,-1.113619,-5.832414,-1.910159,-9.510837,-5.381648,2.810236,3.480025,-5.597301,-3.322193,-8.919437,-9.482443,-5.107188,-3.089484,-5.389739,1.131940,7.031324,3.428543,0.330322,9.689625,-6.261508,1.260965,-6.744144,-6.797280,-9.220331,5.778411,-5.580922,-9.880040,6.549353,3.055645,-7.886264,-8.437275,-8.404810,6.624376,9.229952,-7.372829,-4.067364,0.142408,-1.074885,7.884541,-9.048561,2.157119,3.210682,-6.828583,7.114687,-2.622720,-8.313610,0.321354,3.902140,-4.084396,6.062082,-2.453556,-7.302286,-3.575283,6.891659,-1.391282,0.108114,7.525168,9.336392,6.176331,1.708466,-8.861396,-5.636992,7.257156,-6.350388,0.829855,-2.404990,5.751549,1.736587,5.529859,-9.549485,2.763343,-9.557653,-0.370578,-7.845901,-9.052617,4.209974,6.248930,-1.748102,3.907620,-1.858844,-4.314711,4.238175,-9.317834,2.537818,4.595647,7.503430,6.550106,4.164238,5.326100,-5.546856,-3.177590,9.876032,8.957726,-2.528467,-5.709387,3.093856,9.359044,4.267841,-6.010079,4.271717,-5.731940,-6.084094,-0.472198,7.544535,3.329939,2.612537,7.404615,8.006062,-9.309472,-9.689886,-5.334332,8.306884,-7.660021,5.601133,-8.326248,-9.438288,9.317123,-2.498002,8.284344,-4.605435,7.193879,-7.970950,-7.369479,-2.446595,4.565178,0.030009,-0.287156,1.267637,3.184132,3.542339,6.812258,-4.408601,-4.516876,8.544995,-2.603461,-0.017269,2.110414,4.147786,-4.948063,1.877089,-2.093341,-6.280412,4.373559,3.093539,-3.507887,-3.995928,-7.099696,9.773953,-0.349202,-7.126516,-1.377252,-8.974521,3.541975,0.465336,4.475239,3.738490,1.998511,5.723486,8.105145,-5.627039,2.112829,-8.119913,9.515237,8.606405,-5.537444,8.132626,-3.906576,-2.201571,8.382358,-2.416276,-0.762209,-4.409213,2.290591,0.278260,-7.661426,-3.926606,-8.453646,7.700565,-8.557813,9.802478,4.205837,7.632174,1.895733,2.827477,5.670180,4.228048,-9.243756,-7.452410,6.427115,-5.338762,5.055303,-5.843691,4.063337,1.538494,-0.506725,-5.886426,7.809642,0.966745,-9.463493,1.508518,-2.141604,6.821800,-5.081138,-1.230320,4.592011,8.805853,-1.674769,0.449718,-2.541581,6.277126,7.731546,-3.502724,-5.951709,3.843654,-7.905321,-4.875497,-3.141496,9.692630,8.574535,-2.990590,2.234100,4.087468,9.732464,1.289169,-8.126325,-5.229203,6.728701,-6.158310,5.891626,-5.325216,6.108020,-5.769910,-3.093532,-5.885479,-1.625864,2.638983,7.857354,8.329954,2.813453,-1.426826,8.430871,5.667921,9.499348,-0.962073,-9.877501,-9.428452,-0.629139,7.441311,5.577431,-7.652229,-0.498151,5.172512,4.762719,9.667021,2.459454,-2.744728,-4.025688,8.177896,4.339549,-2.173405,-5.407150,4.420056,-5.914433,-6.952107,6.379086,4.201131,-0.346165,2.225724,5.408503,-1.364732,-1.410721,8.184803,-6.893349,-8.272644,5.245465,8.396675,0.562869,-1.953385,0.793189,1.197493,7.585363,5.012439,6.261068,2.812694,2.989925,-0.068466,-1.690308,-8.712043,-5.069078,0.507570,-4.961236,-8.977346,6.424949,3.432675,0.841652,1.734427,0.894071,-4.668859,3.023379,6.765812,5.450681,-0.296999,9.772799,-6.648764,9.606856,1.647143,8.253851,-4.924909,-4.463908,5.956353,-3.074482,6.786115,5.274297,4.658002,4.869736,2.515595,-0.379601,8.633218,1.434771,9.483218,2.404813,-4.213645,-5.976190,3.997803,-2.203766], dtype = "float32")#candidate|2817|(10080,)|const|float32
call_2815 = relay.TupleGetItem(func_1486_call(relay.reshape(const_2816.astype('float32'), [1, 1680]), relay.reshape(const_2817.astype('float32'), [6, 1680]), ), 5)
call_2818 = relay.TupleGetItem(func_1489_call(relay.reshape(const_2816.astype('float32'), [1, 1680]), relay.reshape(const_2817.astype('float32'), [6, 1680]), ), 5)
output = relay.Tuple([call_2811,call_2815,const_2816,const_2817,])
output2 = relay.Tuple([call_2812,call_2818,const_2816,const_2817,])
func_2824 = relay.Function([], output)
mod['func_2824'] = func_2824
mod = relay.transform.InferType()(mod)
output = func_2824()
func_2825 = relay.Function([], output)
mutated_mod['func_2825'] = func_2825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1999_call = mod.get_global_var('func_1999')
func_2000_call = mutated_mod.get_global_var('func_2000')
call_2833 = relay.TupleGetItem(func_1999_call(), 0)
call_2834 = relay.TupleGetItem(func_2000_call(), 0)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_2844 = relay.TupleGetItem(func_782_call(), 0)
call_2845 = relay.TupleGetItem(func_784_call(), 0)
func_1541_call = mod.get_global_var('func_1541')
func_1543_call = mutated_mod.get_global_var('func_1543')
call_2864 = relay.TupleGetItem(func_1541_call(), 1)
call_2865 = relay.TupleGetItem(func_1543_call(), 1)
uop_2871 = relay.log(call_2864.astype('float64')) # shape=(10, 14, 12)
uop_2873 = relay.log(call_2865.astype('float64')) # shape=(10, 14, 12)
output = relay.Tuple([call_2833,call_2844,uop_2871,])
output2 = relay.Tuple([call_2834,call_2845,uop_2873,])
func_2888 = relay.Function([], output)
mod['func_2888'] = func_2888
mod = relay.transform.InferType()(mod)
output = func_2888()
func_2889 = relay.Function([], output)
mutated_mod['func_2889'] = func_2889
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2892 = relay.var("var_2892", dtype = "int64", shape = (4, 2, 15))#candidate|2892|(4, 2, 15)|var|int64
const_2893 = relay.const([[[8,9,-4,-3,1,-5,-8,1,-2,8,-3,4,10,4,-2],[6,-3,-5,7,7,-1,8,9,-9,-10,1,-8,7,-3,-4]],[[9,6,-4,-3,9,10,-2,1,10,10,-9,-1,6,-4,10],[7,-9,-3,1,5,6,2,-4,7,5,1,-2,10,2,-8]],[[-2,-4,-7,-4,-5,-10,2,8,5,9,-7,-3,-5,-7,-4],[1,-10,-5,-4,-7,7,9,-9,7,-4,-5,7,8,-8,-10]],[[9,-8,-6,8,-3,-10,-4,2,-6,9,-3,1,-10,-1,5],[1,-3,-5,-4,-1,-9,9,-10,7,8,-7,8,-1,8,-9]]], dtype = "int64")#candidate|2893|(4, 2, 15)|const|int64
bop_2894 = relay.not_equal(var_2892.astype('bool'), relay.reshape(const_2893.astype('bool'), relay.shape_of(var_2892))) # shape=(4, 2, 15)
output = bop_2894
output2 = bop_2894
func_2897 = relay.Function([var_2892,], output)
mod['func_2897'] = func_2897
mod = relay.transform.InferType()(mod)
mutated_mod['func_2897'] = func_2897
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2898 = relay.var("var_2898", dtype = "int64", shape = (4, 2, 15))#candidate|2898|(4, 2, 15)|var|int64
func_2897_call = mutated_mod.get_global_var('func_2897')
call_2899 = func_2897_call(var_2898)
output = call_2899
func_2900 = relay.Function([var_2898], output)
mutated_mod['func_2900'] = func_2900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_503_call = mod.get_global_var('func_503')
func_504_call = mutated_mod.get_global_var('func_504')
call_2987 = relay.TupleGetItem(func_503_call(), 2)
call_2988 = relay.TupleGetItem(func_504_call(), 2)
const_2992 = relay.const([2.286292,-1.120053,-3.244055,-2.035333,8.178154,1.345899,-8.005345,-3.265948,-4.022457,-6.983622,-4.369183,-1.799987,-5.983411,-4.464936,-8.808184,7.022232,8.342740,-8.048261,3.061611,-0.216392,-9.838795,8.316742,2.326201,-3.891673,4.616034,-9.351198,-5.533449,9.197680,-5.900744,-2.505999,-9.540235,-0.225739,6.652043], dtype = "float32")#candidate|2992|(33,)|const|float32
bop_2993 = relay.less(call_2987.astype('bool'), relay.reshape(const_2992.astype('bool'), relay.shape_of(call_2987))) # shape=(33,)
bop_2996 = relay.less(call_2988.astype('bool'), relay.reshape(const_2992.astype('bool'), relay.shape_of(call_2988))) # shape=(33,)
func_669_call = mod.get_global_var('func_669')
func_670_call = mutated_mod.get_global_var('func_670')
call_2998 = func_669_call()
call_2999 = func_669_call()
func_1816_call = mod.get_global_var('func_1816')
func_1818_call = mutated_mod.get_global_var('func_1818')
call_3000 = relay.TupleGetItem(func_1816_call(relay.reshape(bop_2993.astype('float64'), [33,])), 0)
call_3001 = relay.TupleGetItem(func_1818_call(relay.reshape(bop_2993.astype('float64'), [33,])), 0)
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
call_3002 = relay.TupleGetItem(func_602_call(), 0)
call_3003 = relay.TupleGetItem(func_604_call(), 0)
bop_3004 = relay.less_equal(bop_2993.astype('bool'), relay.reshape(call_2987.astype('bool'), relay.shape_of(bop_2993))) # shape=(33,)
bop_3007 = relay.less_equal(bop_2996.astype('bool'), relay.reshape(call_2988.astype('bool'), relay.shape_of(bop_2996))) # shape=(33,)
output = relay.Tuple([call_2998,call_3000,call_3002,bop_3004,])
output2 = relay.Tuple([call_2999,call_3001,call_3003,bop_3007,])
func_3024 = relay.Function([], output)
mod['func_3024'] = func_3024
mod = relay.transform.InferType()(mod)
output = func_3024()
func_3025 = relay.Function([], output)
mutated_mod['func_3025'] = func_3025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
call_3068 = relay.TupleGetItem(func_602_call(), 1)
call_3069 = relay.TupleGetItem(func_604_call(), 1)
func_1999_call = mod.get_global_var('func_1999')
func_2000_call = mutated_mod.get_global_var('func_2000')
call_3090 = relay.TupleGetItem(func_1999_call(), 0)
call_3091 = relay.TupleGetItem(func_2000_call(), 0)
output = relay.Tuple([call_3068,call_3090,])
output2 = relay.Tuple([call_3069,call_3091,])
func_3101 = relay.Function([], output)
mod['func_3101'] = func_3101
mod = relay.transform.InferType()(mod)
mutated_mod['func_3101'] = func_3101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3101_call = mutated_mod.get_global_var('func_3101')
call_3102 = func_3101_call()
output = call_3102
func_3103 = relay.Function([], output)
mutated_mod['func_3103'] = func_3103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_3104 = relay.TupleGetItem(func_3024_call(), 0)
call_3105 = relay.TupleGetItem(func_3025_call(), 0)
output = relay.Tuple([call_3104,])
output2 = relay.Tuple([call_3105,])
func_3111 = relay.Function([], output)
mod['func_3111'] = func_3111
mod = relay.transform.InferType()(mod)
output = func_3111()
func_3112 = relay.Function([], output)
mutated_mod['func_3112'] = func_3112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
call_3132 = relay.TupleGetItem(func_602_call(), 0)
call_3133 = relay.TupleGetItem(func_604_call(), 0)
func_3111_call = mod.get_global_var('func_3111')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_3147 = relay.TupleGetItem(func_3111_call(), 0)
call_3148 = relay.TupleGetItem(func_3112_call(), 0)
func_898_call = mod.get_global_var('func_898')
func_901_call = mutated_mod.get_global_var('func_901')
const_3164 = relay.const([-1.672266,2.909147,9.918102,2.765482,5.740247,5.954120,-4.526173,0.797399,1.390865,-7.718996,6.116306,8.709544,0.944492,8.193571,-6.415587,-0.430423,-3.723213,-6.974426,-2.694121,-8.360011,8.868822,-2.080383,-7.274064,-9.925504,-1.096814,7.678057,3.242381,8.648519,4.471276,8.551808,4.387520,-5.642689,8.306395,-8.126448,-1.524878,-7.858514,-7.555930,-6.913405,-1.405275,-1.557598,4.236922,-2.133738,7.077164,8.922097,-4.091945,-2.915313,-5.319883,-9.740759,0.400110,1.369988,3.236437,5.966324,-9.874152,-4.706507,0.984126,-1.648902,-3.593718,8.623706,-9.452001,7.221009,-4.680117,-9.387824,-5.700375,-8.800836,1.861331,-9.727059,7.720113,-5.317722,8.539822,1.118959,-6.152214,0.216757,-7.648669,-4.118246,5.977917,-4.794499,4.110039,-4.370485,5.515588,8.819240,8.296330,4.220689,-5.262842,-9.526030,-9.778776,-7.951658,6.349079,5.882390,-8.102950,-8.117431,8.639757,0.936870,-1.811519,7.597026,3.509825,-3.869238,-0.329164,1.697188,-7.369722,-1.024082,4.368053,2.275176,-6.035184,9.579416,-2.593508,-7.815620,-0.895963,-9.839627,3.641827,-5.317381,-2.119003,1.516278,-8.257900,1.880232,1.740976,1.456701,-5.392279,7.275832,8.465213,-7.329572,3.835596,-7.857347,-0.021193,-8.786204,-1.250320,-7.614790,7.967705,0.811995,7.731256,-7.277637,-7.764468,9.731202,-5.711455,6.987856,3.594879,9.977940,-3.962570,-1.794216,-4.130518,-1.875262,5.769085,-8.611279,7.423010,-2.270337,-5.751141,0.119498,-7.136621,-6.924123,1.865695,6.816253,6.456322,5.463778,-4.137133,-0.312908,-7.337602,5.122296,-6.469488,1.989752,8.166117,-6.148938,-9.809338,-2.067580,-8.873519,-3.897211,-6.774732,9.938117,-0.514195,0.601132,-7.132313,-4.777792,-9.453702,3.950597,5.216735,-2.241514,-2.035319,-4.685497,-2.227926,-1.218801,0.681305,9.283603,-8.609517,1.489505,5.516555,3.308204,4.600531,5.346391,9.808937,-6.218174,8.684674,7.375188,2.192741,-8.630152,-1.094273,-7.589567,3.795211,8.125913,-5.857214,0.507458,4.212217,-4.376494,-0.573646,-6.896120,-6.190704,-7.829973,-5.510357,6.987276,9.468595,3.153330,-3.185534,-8.177304,0.473026,7.066072,-5.732660,-8.534854,9.655402,-4.069045,-1.415150,4.595150,9.873401,-9.336740,1.141302,7.585193,4.592419,-6.825682,7.828088,-9.768174,-7.691893,-0.862788,-7.670730,-5.140205,7.382330,7.093123,-5.066699,-9.105420,-7.173172,3.080125,7.756331,-7.446609,1.960563,-0.449946,3.145025,-9.315639,4.191849,5.743488,7.443983,6.467290,-4.636556,-8.367688,-2.526501,7.297515,2.006172,-2.683754,9.158561,3.225709,-9.374098,1.802967,-8.919419,9.136937,0.275013,2.359224,5.032338,8.317803,6.581416,-3.844772,5.715187,-9.921733,-5.770639,0.696703,-1.388544,-8.297595,-7.225560,-7.230210,9.639572,-6.829236,-3.745211,0.411726,6.386706,-1.255545,-1.318708,-8.061744,-2.643733,-1.962107,3.091949,-4.365367,9.735705,-0.262056,2.986047,-6.893190,4.700387,5.813578,5.681948,9.886163,8.384010,7.077583,-8.438716,1.474208,8.885346,6.711273,7.480679,-6.494756,-6.547421,0.893467,7.795500,1.511915,-9.531896,6.257060,2.350058,-4.073084,-6.811621,8.262547,5.776143,5.986858,-8.584295,-2.729432,-4.779937,-6.212847,5.770178,-0.213500,-0.526261,3.196825,-5.901570,-5.756781,4.842512,5.586818,-9.954703,-0.214584,2.016821,-3.425440,-1.177710,-7.803897,0.134576,-8.965884,-6.567088,-2.153004,-2.298186,5.050861,-0.414275,-2.432591,4.391998,2.504475,-7.093503,8.222245,3.078501,-2.945984,-4.376607,-7.683276,0.675247,3.959371,-2.314449,-4.956386,5.084320,9.708759,3.402512,-8.948160,9.776479,6.785616,4.470878,-0.477359,-3.602714,7.980408,1.106040,3.050345,-5.261735,-8.070497,-9.756620,8.966798,-7.974741,9.823631,-4.166054,-9.951709,6.839106,-1.908202,4.234198,3.071519,0.635725,-1.265853,-1.867159,3.301953,-0.042590,0.749504,6.481811,5.996478,-1.949430,3.192767,-4.261791,-8.386751,3.839172,-1.612316,2.997239,3.885468,-0.352892,0.538973,4.518955,9.974547,-8.081606,-5.976689,5.618533,-2.331633,-6.572666,3.566952,3.950141,-7.966310,-9.694319,4.515466,-2.286825,-0.387479,3.823548,1.495161,-9.606445,-3.853702,-0.875025,-5.768977,-3.271424,1.313591,5.899630,3.087390,-7.494288,5.857784,5.106213,9.271241,9.135777,-8.727970,3.137659,8.736408,6.572869,8.204681,-4.646424,4.942332,-2.144190,3.232642,9.744046,-4.965158,-4.743221,-0.709158,8.985758,4.000140,8.837469,5.817752,-9.232718,0.545338,-8.336527,5.366165,-1.787554,-2.736340,4.643027,-1.317797,-8.198277,-5.035053,5.155392,-4.955990,-6.752672,4.850559,-4.388956,6.219371,-7.095431,-2.431390,5.347603,4.417452,-2.488023,-1.021424,-5.349513,4.999261,0.908523,4.712094,-0.474136,0.724418,-8.126497,8.670858,0.180967,1.917415,3.825628,8.633519,2.947598,-2.190779,-3.449287,4.543791,-8.961760,3.568163,-4.485949,-0.082872,4.332066,-4.740775,-7.007233,-0.776406,-1.184510,7.363544,5.619521,-3.360840,-2.870984,-9.736908,1.245920,2.621175,-0.129718,2.190025,1.700226,-3.684607,-5.928695,-7.226283,-5.653308,-2.041765,-3.644513,-3.006588,-3.056454,-5.333238,3.605978,9.135686,-2.888863,-2.338424,-4.675192,-3.731910,1.056329,-2.733416,8.366079,9.886966,6.353839,-2.904628,7.428582,2.764103,8.392186,-1.926938,-8.907934,0.540598,-0.428384,-7.665673,4.523371,7.931500,0.613709,-8.530544,-1.429038,-6.679728,-1.717402,-7.035742,8.715934,0.613306,0.792346,6.423719,-8.838527,4.747927,7.089536,0.644840,-3.316966,9.556676,-0.535239,-4.283505,7.734602,-4.436904,2.707501,-7.855560,-3.967913,6.396415,8.127730,1.283712,7.930451,5.075322,-0.476572,7.038099,4.221374,-6.266805,0.135804,-6.045176,8.354491,-4.045745,9.106285,3.069700,-3.629502,-3.383220,-9.061337,4.015899,-4.707749,-1.148271,9.769847,8.781428,-2.969577,-7.058959,-3.701357,3.057773,5.667287,-7.992153,-1.804167,-9.812334,-8.600435,-6.224838,4.384820,-6.423934,-9.446577,-2.023106,-1.637494,-5.594551,-0.788492,-2.527025,-9.878990,-6.359139,1.040565,-2.676679,4.651809,7.864430,6.485608,-7.416080,4.292639,-6.947829,7.654662,-8.854083,-8.542006,-1.422771,4.053567,2.228797,-0.100462,-9.578229,-7.072749,4.016050,0.746173,3.483476,5.654617,2.692602,-8.645661,-7.512423,8.862150,-0.846937,-3.417045,-2.095806,9.776529,1.970065,6.918200,-6.804789,-3.903334,8.713116,-8.260302,4.541980,-7.514789,-2.175273,-7.362785,-9.812719,4.546630,-2.021362,-1.245823,-0.262558,-4.671930,5.134504,9.623383,-5.905839,-5.868008,2.130814,-9.140441,-8.934022,-9.665159,-7.834262,7.265533,-7.434768,8.636429,-2.874684,4.663895,1.597428,-6.379770,7.374241,-8.291742,-7.182725,-8.687225,9.224752,-7.637677,4.326678,0.399705,4.046689,7.706769,0.625927,-6.961690,-0.153988,-8.832551,-4.999099,-4.465413,-2.203064,4.623106,4.977026,5.041061,-7.057738,-3.639685,-1.318212,7.001762,4.439446,0.761675,7.446197,-4.195686,5.946765,-1.937043,-1.617948,6.872476,2.784476,7.130531,-1.828495,-9.316124,-3.890940,5.200843,-1.960356,-7.581937,8.130514,-7.861278,-7.275516,-4.158400,-6.677737,1.288930,7.613411,0.471821,5.339316,-9.267359,1.576485,-7.855926,4.945010,-0.735966,6.431816,1.433001,-7.718485,6.539135,9.718309,-1.981549,-7.229297,-9.291008,5.230108,7.437801,-9.106070,-4.763344,-1.016281,6.769627,-7.083994,5.434107,-2.374477,-2.344531,-0.054613,6.003068,3.801317,8.547391,0.367556,-4.284963,-8.913904,6.150190,9.971868,-9.289732,0.210853,8.275495,-1.003136,0.139442,-9.471816,9.529169,6.578086,-5.150314,9.235309,4.096156,3.289748,7.219433,9.510250,-3.967170,-1.489023,-0.793359,-6.647691,-3.954868,-5.509972,3.993513,5.231802,4.712437,-1.832280,-4.816597,-5.445433,-1.833206,6.471931,8.364586,4.773096,4.771214,-1.021063,6.053074,1.940856,3.213817,9.582130,-1.028176,-8.499784,2.515025,0.978009,-4.840077,7.540703,2.135960,-0.989623,6.735561,-1.885049,7.280178,-2.594538,2.518018,-1.411219,1.203497,-4.352118,9.430223,-1.722311,9.097431,-4.284827,6.702417,-4.814197,-6.411837,9.417670,-3.099115,-4.444959,-2.670078,-4.064318,-8.055897,3.574490,-8.206249,-2.016653,-1.845705,9.900124,-2.231012,0.654889,4.151612,9.351787,-5.116722,-5.136305,-9.728596,-1.670883,6.665037,0.731159,-5.647848,-8.033269,-2.633036,-9.429664,7.522275,-4.449129,8.791347,9.755317,6.247763,-3.652601,4.870105,4.421236,9.537527,-0.710482,-1.801778,-3.065227,-1.703946,-5.965002,7.178821,7.600850,-0.590549,9.709903,1.932274,-3.444886,1.502513,-7.150598,8.725552,-9.732339,-1.130735,-3.456514,-2.704809,4.929182,9.959113,7.377307,-6.820882,8.330929,-1.442102,-0.786955,7.392587,6.490205,0.084643,6.670114,5.907586,0.256145,-0.049710,-0.682826,-7.665434,-2.795420,2.400740,1.210199,-0.518061,-2.477764,5.232043,6.786068,-5.683131,7.109167,-8.381245,-5.458299,-7.553058,6.190838,6.507893,-9.712049,2.794117,8.349348,-3.346738,-7.061260,3.113022,-3.306665,3.426840,2.956485,-3.180221,9.916552,0.224184,-1.876361,3.389819,5.098379,1.849492,0.813576,-1.147309,-2.489447,0.516097,6.605655,8.491490,4.899450,0.590498,-7.004693,7.995078,8.501053,-4.691249,-0.331364,8.635083,-1.766265,3.981314,-2.607159,0.001325,4.322539,7.043921,1.008578,-7.969646,-5.002027,-8.317749,0.429443,-9.619734,-3.848417,-6.285174,7.052237,-8.912598,-1.853061,5.308098,2.769067,4.817439,9.336543,-0.876837,-4.705936,4.684315,-9.718730,7.952828,8.976219,-8.422484,-0.353899,-6.771840,6.051851,-2.921304,7.211467,-8.567666,-9.815322,2.411599,-2.620969,-1.491973,-5.869834,4.558834,5.440230,-4.050927,7.940372,4.857087,5.756601,6.429273,-3.255798,-9.484914,0.837701,2.969434,2.678379,1.189647,-8.964308,-4.893316,6.082144,7.143577,-6.061331,3.794472,1.882771,-1.010274,-3.993132,1.200266,0.061347,-1.660593,-3.100041,-5.161963,-3.353199,1.714879,2.624448,5.918466,-6.250369,-2.117228,-9.394411,-6.750961,-0.195833,-8.273119,-2.748635,3.064053,-0.726194,-2.834490,9.244695,-4.219415,-3.666196,-2.834655,8.304026,-9.525968,3.040744,-6.363459,-0.260568,3.347331,0.202468,7.117895,9.378467,0.545873,8.156524,-5.358590,-5.541564,-9.763697,-0.360987,3.310270,2.249299,6.994020,-6.984531,-9.579066,-0.892998,4.325680,-3.648049,0.719016,1.836418,0.289041,-1.193830,-4.725755,-3.527265,8.175458,2.790369,-5.716982,-4.801962,6.994313,2.226537,9.236916,0.189915,-7.707057,-9.827874,8.958114,-2.496743,-1.666289,-6.126027,-9.627250,1.136658,-3.501525,-5.752319,9.422557,-8.753873,7.062022,2.901413,-1.214550,6.208847,-1.468056,-4.212175,6.390144,-6.930518,-3.723487,-9.725907,5.913350,-2.233329,2.810102,-3.441438,-3.504250,2.978216,-1.895921,-4.316518,-3.392203,2.063226,9.274515,-5.867354,2.128836,-9.881928,-9.460288,-0.031722,4.075489,7.122225,2.206942,3.665305,-3.261461,7.878579,5.938720,3.904014,6.530229,-7.662167,9.620607,0.324796,7.945962,-5.234656,2.337535,0.102097,6.942918,9.906278,-5.313291,-6.600083,2.406339,-1.441432,-0.165025,-1.782624,-8.815068,-5.052904,-2.999892,-2.703923,-0.901371,2.153234,3.860154,-3.020253,2.713772,9.877033,-0.408768,-9.913042,4.605639,8.023842,5.945240,0.617157,-5.998020,1.996946,-2.054820,6.917301,-0.502447,-2.676874,3.368335,-6.479313,-4.831201,8.139531,-0.745335,-3.419789,-9.598107,7.175970,-3.138674,0.354874,-8.437841,0.576938,8.734802,2.219312,5.574919,9.862022,-0.087687,8.039261,-8.463065,-0.826772,-3.698196,-2.629435,-5.880080,-5.536928,6.031149,8.872734,-0.850992,-2.034489,8.927691,6.685081,8.246910,-9.860788,3.689325,-0.390448,-1.081327,-2.237256,7.927299,2.603486,-9.400871,-7.010917,5.846728,4.207496,-2.131512,4.695307,-1.251981,-2.639911,-4.187988,1.048827,-4.258556,3.439843,-9.711160,-2.520031,-9.579209,6.034394,5.344416,-5.201387,-5.968706,4.224976,4.042555,-8.289914,0.328243,3.021245,9.050344,1.228536,-6.186721,-3.572241,-1.041370,4.529642,-6.433199,9.630043,-8.605831,0.719907,-2.969715,-0.815788,8.679697,6.784273,3.911577,-8.282579,8.000232,3.664286,-8.596244,6.286963,-0.864588,-1.096704,8.385216,-6.661771,2.716325,-6.276130,-8.793424,-2.603843,-4.985763,5.774866,-1.911460,-3.747730,0.722628,-8.735414,-5.642372,4.696766,-6.733126,5.292808,1.195998,0.498272,7.435143,-7.491480,-1.895086,-4.202894,-3.011218,2.269511,8.252963,7.466061,4.519052,2.752662,5.964585,-4.874057,-2.606356,2.446821,0.802185,-5.888673,4.580944,4.602251,6.288206,-3.110314,2.242294,4.947611,1.642945,1.850929,-1.130000,-4.250328,1.539005,8.203884,6.025870,-7.445196,2.724012,1.081065,9.309868,5.179674,-5.346637,3.367852,7.675590,8.832243,9.372740,6.277231,5.304522,5.108768,-1.912280,-1.054658,5.112675,-9.013990,0.868078,8.326791,-3.408673,-3.215169,-2.033902,-9.341180,-6.091994,9.525228,2.412419,6.554946,-3.452908,6.891585,1.816107,-0.759338,-1.506675,0.520550,1.618535,5.722427,1.462982,-1.709173,3.222119,8.488126,-2.612505,0.848296,4.711968,-1.115586,6.182403,-2.957042,9.216547,2.582766,-6.627700,-8.562737,-5.950969,3.374472,5.330096,2.528510,7.852611,-1.166617,8.765801,9.076010,-2.651711,5.342689,1.576590,-0.629069,-4.835022,5.525705,-9.853029,-5.061739,6.425502,6.691290,-7.430578,1.456924,7.779115,8.227744,6.491446,-1.944145,1.074441,8.315736,0.876714,7.130378,7.088938,-9.004935,-4.327875,-4.991814,7.943635,-6.789372,3.406794,9.798171,8.734860,4.709143,3.441866,-4.597332,0.691523,7.133244,2.048315,9.378489,8.595562,2.571452,-0.264724,8.449928,9.966687,1.881437,5.466998,0.228885,-4.126700,8.173562,-1.227395,-6.506788,2.733284,6.560634,-5.907268,-3.676930,-5.414369,-0.073532,9.716648,-0.462303,9.877723,7.346499,-9.465333,-6.130801,-5.006797,-0.239934,1.380512,-3.949557,1.486135,-0.033686,-8.674357,5.654308,-7.438922,-2.784845,-4.419122,-7.700855,-4.194169,-0.213644,-8.567322,1.174127,3.236601,-6.378227,-2.381102,8.556652,-3.000300,-4.629030,-6.361488,2.660777,3.650468,6.104525,6.831271,7.271372,3.633741,-7.476717,-5.417281,-1.742260,-8.580464,7.754194,-5.854525,-8.498883,-5.338036,2.612804,-9.780296,6.519317,-8.857965,8.565964,-1.269615,-7.629342,9.596066,4.478478,-4.077257,5.528983,-0.910432,-1.434616,8.707103,5.265416,7.579921,2.045946,-9.342164,6.520271,0.218080,-2.494790,8.249329,2.032917,2.085414,0.404565,9.208076,-2.871540,3.855665,-1.949228,1.372053,-0.006688,-1.074236,1.750148,-2.998347,-0.457552,1.159180,3.420259,8.704321,6.459349,9.785668,-8.514539,0.684257,5.274991,9.017731,-9.768573,7.865217,3.484087,-4.264468,-9.643898,5.167270,-2.798422,3.161770,-0.217044,-4.993966,-0.828769,-5.139834,-4.153877,7.881128,-7.696424,8.979438,-7.554183,9.024793,0.053389,-9.147270,-7.892624,-8.589972,-8.669356,-5.556683,-3.171745,3.585279,-0.457629,7.875831,9.290423,-6.009987,-6.833473,-9.468958,3.472305,-2.750392,0.328519,-2.677182,9.442332,-9.346397,2.949768,-1.800040,-6.390068,-7.185093,0.302740,1.205069,-0.006702,-4.757581,-1.888447,3.858354,-6.365907,-6.222850,-2.221359,1.949055,8.366113,-8.052270,-4.773433,-5.593207,-0.451780,8.314367,-3.346025,-2.743751,2.952364,6.407927,-6.338793,7.658506,6.210527,-5.811367,-4.714047,2.680529,-2.319264,-9.049563,-4.864973,8.995562,5.609035,-0.835205,2.397419,6.184842,3.802605,-4.910017,9.204273,-3.057232,2.931091,3.943631,-1.220850,0.239035,-7.733370,9.580071,-8.412071,9.946459,7.742104,-8.381104,-3.864983,8.417728,-4.400512,4.259734,6.968991,-0.377074,2.211929,2.221685,-6.459721,-0.974889,-5.398232,7.806265,-7.645020,7.322425,-0.287906,-0.092490,5.432776,-5.238024,-5.156283,7.866015,4.810082,-5.157780,3.805371,-4.862186,1.404149,-9.875723,-6.196767,-4.987596,-0.062488,0.877474,9.136858,-8.414019,2.801221,6.579686,-0.976469,-2.625502,-7.524803,-8.370781,-7.511230,-3.516953,8.802078,1.839107,-2.464588,-7.979281,3.697504,-1.276712,-8.145427,2.205694,1.939846,6.781913,-2.353315,-7.787496,-3.344002,-1.707459,8.091698,-3.643663,-5.438407,8.425356,-8.481719,1.173193,0.959932,-4.957150,-7.919835,9.192651,-0.030500,-4.251506,-4.434826,-0.115965,4.782692,6.327877,9.940077,-7.718216,-7.607288,-8.594518,3.598929,-8.536930,6.746380,-9.910420,8.646383,-2.265591,-5.173741,-0.004632,3.909155,-0.141474,7.798500,1.866187,7.916638,-0.829761,4.772779,-8.242413,1.765187,5.646898,-0.331428,-0.899592,-4.238462,4.661885,3.985067,2.178308,-9.137888,-0.048481,-7.401145,-8.214205,4.896330,8.327909,-0.463002,2.533370,-7.875451,-8.074248,7.231294,-2.407448,8.743156,-6.660501,2.965222,7.928598,4.181524,-3.134842,-9.758515,-9.220786,1.726522,-0.503132,0.224129,2.143540,4.167721,-7.153878,4.433143,-0.428391,7.972856,4.765355,-3.902797,-4.905151,-7.927889,4.042075,-4.111966,-2.310295,5.454456,7.831495,7.534654,1.073540,-9.536254,9.880167,-4.779478,5.169570,-7.922980,7.261523,0.972531,3.848894,-0.910312,-1.289362,-2.555672,-6.033525,-4.812225], dtype = "float32")#candidate|3164|(1680,)|const|float32
call_3163 = relay.TupleGetItem(func_898_call(relay.reshape(const_3164.astype('float32'), [10, 14, 12])), 0)
call_3165 = relay.TupleGetItem(func_901_call(relay.reshape(const_3164.astype('float32'), [10, 14, 12])), 0)
func_1541_call = mod.get_global_var('func_1541')
func_1543_call = mutated_mod.get_global_var('func_1543')
call_3169 = relay.TupleGetItem(func_1541_call(), 0)
call_3170 = relay.TupleGetItem(func_1543_call(), 0)
output = relay.Tuple([call_3132,call_3147,call_3163,const_3164,call_3169,])
output2 = relay.Tuple([call_3133,call_3148,call_3165,const_3164,call_3170,])
func_3184 = relay.Function([], output)
mod['func_3184'] = func_3184
mod = relay.transform.InferType()(mod)
output = func_3184()
func_3185 = relay.Function([], output)
mutated_mod['func_3185'] = func_3185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_3189 = relay.TupleGetItem(func_3024_call(), 0)
call_3190 = relay.TupleGetItem(func_3025_call(), 0)
output = relay.Tuple([call_3189,])
output2 = relay.Tuple([call_3190,])
func_3195 = relay.Function([], output)
mod['func_3195'] = func_3195
mod = relay.transform.InferType()(mod)
mutated_mod['func_3195'] = func_3195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3195_call = mutated_mod.get_global_var('func_3195')
call_3196 = func_3195_call()
output = call_3196
func_3197 = relay.Function([], output)
mutated_mod['func_3197'] = func_3197
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3198 = relay.var("var_3198", dtype = "uint16", shape = (12, 16, 11))#candidate|3198|(12, 16, 11)|var|uint16
var_3199 = relay.var("var_3199", dtype = "uint16", shape = (12, 16, 11))#candidate|3199|(12, 16, 11)|var|uint16
bop_3200 = relay.greater_equal(var_3198.astype('bool'), relay.reshape(var_3199.astype('bool'), relay.shape_of(var_3198))) # shape=(12, 16, 11)
func_1816_call = mod.get_global_var('func_1816')
func_1818_call = mutated_mod.get_global_var('func_1818')
const_3207 = relay.const([[4.393299,-0.299860,5.561199],[-0.752651,8.519138,6.154414],[2.129214,-2.238902,-3.430508],[8.976671,1.175297,3.598390],[-0.764378,7.008002,-0.441929],[-0.269758,-0.066734,-7.252286],[4.964246,9.826085,-4.828836],[-9.213508,3.036736,2.536892],[6.392791,-4.044684,2.506641],[-4.112056,2.147455,-5.092844],[2.016303,9.485616,9.839766]], dtype = "float64")#candidate|3207|(11, 3)|const|float64
call_3206 = relay.TupleGetItem(func_1816_call(relay.reshape(const_3207.astype('float64'), [33,])), 0)
call_3208 = relay.TupleGetItem(func_1818_call(relay.reshape(const_3207.astype('float64'), [33,])), 0)
func_1949_call = mod.get_global_var('func_1949')
func_1951_call = mutated_mod.get_global_var('func_1951')
var_3225 = relay.var("var_3225", dtype = "float32", shape = (220,))#candidate|3225|(220,)|var|float32
call_3224 = relay.TupleGetItem(func_1949_call(relay.reshape(var_3225.astype('float32'), [4, 5, 11])), 0)
call_3226 = relay.TupleGetItem(func_1951_call(relay.reshape(var_3225.astype('float32'), [4, 5, 11])), 0)
uop_3229 = relay.sin(var_3198.astype('float32')) # shape=(12, 16, 11)
func_1237_call = mod.get_global_var('func_1237')
func_1239_call = mutated_mod.get_global_var('func_1239')
const_3240 = relay.const([[1.245803,1.625897,4.504309,-1.709676,2.641071,-7.435060,5.616875,0.978682,3.260312,-7.958475,-2.025623,8.658362,5.958923,-0.365644,5.891278,-4.855874,1.443874,-0.756429,2.124229,6.063542,0.279075,-6.660919,-6.309668,-0.444970,-4.781322,0.188780,-9.997329,1.030450,-7.165628,-2.155791,7.560491,-6.286035,-4.163616,6.152249,1.854831,-9.593193,-3.945364,-7.763425,0.920171,-0.492718,7.444759,-0.209652,1.709941,6.877291,1.368121,6.826532,-6.427888,0.517070,-2.186648,-4.943585,5.782516,-8.815902,6.627316,-2.249964,0.447609,1.846472,3.761520,-3.243125,0.424165,-5.391387,8.218464,4.185813,5.142965,-4.153256,-2.948234,-4.123593],[-2.729850,5.149132,4.911687,-9.812149,6.028370,6.196401,0.647473,9.398621,8.491558,6.623787,5.653741,-2.338594,-0.880727,-3.475865,5.969318,-7.964561,3.814072,-3.505106,-5.488111,4.059499,-9.574198,-0.456640,-5.916429,-3.991119,4.684050,6.428324,4.409371,9.307802,-1.937720,-2.817744,-1.566553,9.060858,-9.235684,-3.706154,-5.039410,-3.291555,-7.675339,-5.184365,-2.935184,-2.049194,3.211329,-8.137876,1.467390,-4.675658,4.482897,-7.660334,6.731231,4.526550,4.568191,-6.729452,0.236644,-6.143192,4.363358,0.590681,8.873130,8.167876,4.582726,0.643601,-0.736390,-9.336840,-7.120914,7.576114,3.814519,-5.876951,8.296238,-8.328795],[4.396121,-2.869618,-2.963743,5.083371,-1.206907,-7.446705,-9.496721,-8.824833,5.315894,5.391189,2.960542,5.509379,3.548091,2.098027,1.088992,-7.702251,-7.945313,1.919750,-2.269744,9.590339,-5.272286,-1.841411,1.117048,9.549416,6.689952,0.566326,0.878612,8.172191,-1.590604,2.264183,9.973425,-6.207185,6.768755,-7.245140,-4.847102,-6.924738,1.228008,-8.302474,0.233301,2.626926,-0.566285,-2.559266,0.075880,-4.492782,-9.377423,8.891002,9.650284,-4.393825,-2.205790,-6.434851,-9.602986,4.462025,4.559014,-9.980339,3.391459,-2.582829,-8.651457,5.841992,-5.183884,7.038227,-0.070539,-3.213040,4.137528,-4.726735,3.378438,-9.769249],[8.383398,5.344904,8.432192,7.726181,5.556358,-4.406981,-7.654264,-6.954548,-9.201691,-3.711216,-2.102363,-1.506255,1.595571,2.296446,-9.119279,-0.953746,2.745785,-0.547560,3.495345,2.209685,7.919046,5.635887,-4.333741,7.671111,1.958848,4.886196,-9.859903,9.909264,-5.269561,1.759224,7.948485,-9.019800,2.051902,1.744985,-8.957347,-1.771789,7.751772,-2.055980,1.090695,-0.329868,7.831209,-2.212678,1.742381,0.303984,1.446726,-1.087396,-6.484002,1.898789,-3.110265,-9.422294,-9.134209,-8.155942,-7.200790,1.885140,-9.534090,0.274884,0.678970,-3.311246,9.986438,-2.845300,-5.369823,0.885746,6.500879,-5.794014,-2.354633,-3.879267],[5.212034,-4.886285,4.562609,7.946070,0.500420,2.912694,7.629997,0.012425,8.060828,3.578999,9.414237,-3.808398,8.446002,-9.366573,-2.466054,-7.254996,7.971940,7.646930,-5.207997,7.974755,8.812258,-1.111454,-7.227077,-3.888513,5.228143,9.470041,-8.625966,0.034495,-0.976706,6.428628,1.191451,2.504208,-7.515452,8.812655,6.143635,-5.371319,-9.240606,8.754389,2.084808,-4.520436,1.428292,8.275557,-9.515112,-5.163629,-8.442299,9.137303,3.558491,-4.138936,2.344015,7.315548,-3.498593,-6.213878,-3.953588,3.571323,1.690249,2.970877,3.471735,-6.295068,5.440806,1.753648,7.681912,1.789965,8.006303,-6.370541,-4.011714,1.879953],[-9.432249,3.873649,-3.380294,-9.860731,-0.222404,-4.260299,-5.391000,8.947028,7.596616,9.888978,1.301750,-0.941006,-9.701522,-5.670595,-3.387251,-8.613251,7.779617,6.347534,-4.936261,4.790272,8.619007,2.450032,-0.649894,-5.354829,1.501166,-0.981542,-6.579459,8.388387,-6.283571,4.985586,7.581637,5.191272,2.104437,-2.748241,-8.811817,9.215871,-0.527599,8.278164,8.789736,-3.882490,9.307221,-0.807381,4.689565,-6.532232,6.666171,-1.484019,3.253409,0.664201,5.298611,5.582454,3.907575,3.662174,8.217053,-2.505349,-9.617803,6.896565,-1.717734,-3.172054,0.187423,3.948509,-1.215908,6.094673,3.777547,6.993159,5.960351,-0.516343],[5.744392,-4.937283,-7.447195,6.013988,7.822643,-8.488886,-9.418996,-6.283769,6.280091,-1.570003,2.974189,-1.032401,-0.966555,6.879525,-9.758595,-7.681828,-4.571150,-6.374485,-8.616966,2.105838,-5.752980,5.347406,-2.526492,-0.235958,0.869935,-0.573053,-2.832048,6.956217,-9.783829,-1.725826,-7.374069,-5.470007,4.133016,4.740371,-2.436990,-6.674241,-0.398406,-6.671758,1.318088,-0.882048,6.922405,1.553651,7.940408,4.935376,-0.877152,-1.231752,-5.902329,2.429036,1.594967,5.411006,4.825146,-7.967959,5.831381,5.259446,9.980880,2.124905,-0.527061,8.312598,7.375446,8.996598,-8.941263,-0.988919,-6.081721,8.018231,-9.362245,3.145938],[-2.832060,0.413801,-6.825192,-1.379299,6.059791,1.358602,-3.329599,8.503850,4.843172,5.006553,0.173949,-3.589535,5.025836,9.146429,3.054524,-8.621557,8.647630,3.813063,-7.445930,5.838959,-9.672303,6.603445,7.208541,-7.511357,0.578151,8.885653,-5.509249,-3.015704,2.529623,3.104663,-6.425201,-1.632445,-9.491350,-9.337583,8.502058,-5.476098,-4.253527,-3.539798,-7.992178,-2.529585,0.942748,-7.977616,4.548019,4.224705,5.259701,2.293287,-5.471151,8.254694,-6.703400,0.395288,1.848070,4.250164,5.498406,-6.222434,-1.876132,0.356693,-4.708206,3.266492,-9.489335,-7.331372,-6.026452,-8.277141,7.452496,2.984089,5.487155,3.596889]], dtype = "float32")#candidate|3240|(8, 66)|const|float32
call_3239 = relay.TupleGetItem(func_1237_call(relay.reshape(const_3240.astype('float32'), [11, 16, 3])), 0)
call_3241 = relay.TupleGetItem(func_1239_call(relay.reshape(const_3240.astype('float32'), [11, 16, 3])), 0)
output = relay.Tuple([bop_3200,call_3206,const_3207,call_3224,var_3225,uop_3229,call_3239,const_3240,])
output2 = relay.Tuple([bop_3200,call_3208,const_3207,call_3226,var_3225,uop_3229,call_3241,const_3240,])
func_3242 = relay.Function([var_3198,var_3199,var_3225,], output)
mod['func_3242'] = func_3242
mod = relay.transform.InferType()(mod)
var_3243 = relay.var("var_3243", dtype = "uint16", shape = (12, 16, 11))#candidate|3243|(12, 16, 11)|var|uint16
var_3244 = relay.var("var_3244", dtype = "uint16", shape = (12, 16, 11))#candidate|3244|(12, 16, 11)|var|uint16
var_3245 = relay.var("var_3245", dtype = "float32", shape = (220,))#candidate|3245|(220,)|var|float32
output = func_3242(var_3243,var_3244,var_3245,)
func_3246 = relay.Function([var_3243,var_3244,var_3245,], output)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3298 = relay.var("var_3298", dtype = "float64", shape = (6, 1, 5))#candidate|3298|(6, 1, 5)|var|float64
var_3299 = relay.var("var_3299", dtype = "float64", shape = (6, 3, 5))#candidate|3299|(6, 3, 5)|var|float64
bop_3300 = relay.power(var_3298.astype('float64'), var_3299.astype('float64')) # shape=(6, 3, 5)
func_542_call = mod.get_global_var('func_542')
func_544_call = mutated_mod.get_global_var('func_544')
call_3308 = func_542_call()
call_3309 = func_542_call()
output = relay.Tuple([bop_3300,call_3308,])
output2 = relay.Tuple([bop_3300,call_3309,])
func_3310 = relay.Function([var_3298,var_3299,], output)
mod['func_3310'] = func_3310
mod = relay.transform.InferType()(mod)
mutated_mod['func_3310'] = func_3310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3310_call = mutated_mod.get_global_var('func_3310')
var_3312 = relay.var("var_3312", dtype = "float64", shape = (6, 1, 5))#candidate|3312|(6, 1, 5)|var|float64
var_3313 = relay.var("var_3313", dtype = "float64", shape = (6, 3, 5))#candidate|3313|(6, 3, 5)|var|float64
call_3311 = func_3310_call(var_3312,var_3313,)
output = call_3311
func_3314 = relay.Function([var_3312,var_3313,], output)
mutated_mod['func_3314'] = func_3314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_752_call = mod.get_global_var('func_752')
func_754_call = mutated_mod.get_global_var('func_754')
call_3316 = func_752_call()
call_3317 = func_752_call()
output = call_3316
output2 = call_3317
func_3323 = relay.Function([], output)
mod['func_3323'] = func_3323
mod = relay.transform.InferType()(mod)
output = func_3323()
func_3324 = relay.Function([], output)
mutated_mod['func_3324'] = func_3324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3325 = relay.var("var_3325", dtype = "float32", shape = (8, 12, 16))#candidate|3325|(8, 12, 16)|var|float32
uop_3326 = relay.sinh(var_3325.astype('float32')) # shape=(8, 12, 16)
func_1206_call = mod.get_global_var('func_1206')
func_1208_call = mutated_mod.get_global_var('func_1208')
var_3329 = relay.var("var_3329", dtype = "float32", shape = (3, 60))#candidate|3329|(3, 60)|var|float32
call_3328 = func_1206_call(relay.reshape(var_3329.astype('float32'), [3, 10, 6]))
call_3330 = func_1206_call(relay.reshape(var_3329.astype('float32'), [3, 10, 6]))
output = relay.Tuple([uop_3326,call_3328,var_3329,])
output2 = relay.Tuple([uop_3326,call_3330,var_3329,])
func_3336 = relay.Function([var_3325,var_3329,], output)
mod['func_3336'] = func_3336
mod = relay.transform.InferType()(mod)
mutated_mod['func_3336'] = func_3336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3336_call = mutated_mod.get_global_var('func_3336')
var_3338 = relay.var("var_3338", dtype = "float32", shape = (8, 12, 16))#candidate|3338|(8, 12, 16)|var|float32
var_3339 = relay.var("var_3339", dtype = "float32", shape = (3, 60))#candidate|3339|(3, 60)|var|float32
call_3337 = func_3336_call(var_3338,var_3339,)
output = call_3337
func_3340 = relay.Function([var_3338,var_3339,], output)
mutated_mod['func_3340'] = func_3340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_3345 = relay.TupleGetItem(func_3024_call(), 3)
call_3346 = relay.TupleGetItem(func_3025_call(), 3)
output = call_3345
output2 = call_3346
func_3347 = relay.Function([], output)
mod['func_3347'] = func_3347
mod = relay.transform.InferType()(mod)
output = func_3347()
func_3348 = relay.Function([], output)
mutated_mod['func_3348'] = func_3348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mod.get_global_var('func_2824')
func_2825_call = mutated_mod.get_global_var('func_2825')
call_3349 = relay.TupleGetItem(func_2824_call(), 1)
call_3350 = relay.TupleGetItem(func_2825_call(), 1)
uop_3351 = relay.cosh(call_3349.astype('float64')) # shape=(6, 1680)
uop_3353 = relay.cosh(call_3350.astype('float64')) # shape=(6, 1680)
func_1999_call = mod.get_global_var('func_1999')
func_2000_call = mutated_mod.get_global_var('func_2000')
call_3360 = relay.TupleGetItem(func_1999_call(), 0)
call_3361 = relay.TupleGetItem(func_2000_call(), 0)
bop_3362 = relay.less(uop_3351.astype('bool'), relay.reshape(call_3349.astype('bool'), relay.shape_of(uop_3351))) # shape=(6, 1680)
bop_3365 = relay.less(uop_3353.astype('bool'), relay.reshape(call_3350.astype('bool'), relay.shape_of(uop_3353))) # shape=(6, 1680)
func_542_call = mod.get_global_var('func_542')
func_544_call = mutated_mod.get_global_var('func_544')
call_3367 = func_542_call()
call_3368 = func_542_call()
func_2459_call = mod.get_global_var('func_2459')
func_2461_call = mutated_mod.get_global_var('func_2461')
call_3373 = relay.TupleGetItem(func_2459_call(), 0)
call_3374 = relay.TupleGetItem(func_2461_call(), 0)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_3378 = relay.TupleGetItem(func_3024_call(), 3)
call_3379 = relay.TupleGetItem(func_3025_call(), 3)
output = relay.Tuple([call_3360,bop_3362,call_3367,call_3373,call_3378,])
output2 = relay.Tuple([call_3361,bop_3365,call_3368,call_3374,call_3379,])
func_3380 = relay.Function([], output)
mod['func_3380'] = func_3380
mod = relay.transform.InferType()(mod)
output = func_3380()
func_3381 = relay.Function([], output)
mutated_mod['func_3381'] = func_3381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3347_call = mod.get_global_var('func_3347')
func_3348_call = mutated_mod.get_global_var('func_3348')
call_3558 = func_3347_call()
call_3559 = func_3347_call()
output = call_3558
output2 = call_3559
func_3565 = relay.Function([], output)
mod['func_3565'] = func_3565
mod = relay.transform.InferType()(mod)
output = func_3565()
func_3566 = relay.Function([], output)
mutated_mod['func_3566'] = func_3566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mod.get_global_var('func_2824')
func_2825_call = mutated_mod.get_global_var('func_2825')
call_3572 = relay.TupleGetItem(func_2824_call(), 2)
call_3573 = relay.TupleGetItem(func_2825_call(), 2)
output = call_3572
output2 = call_3573
func_3583 = relay.Function([], output)
mod['func_3583'] = func_3583
mod = relay.transform.InferType()(mod)
output = func_3583()
func_3584 = relay.Function([], output)
mutated_mod['func_3584'] = func_3584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3583_call = mod.get_global_var('func_3583')
func_3584_call = mutated_mod.get_global_var('func_3584')
call_3615 = func_3583_call()
call_3616 = func_3583_call()
func_1419_call = mod.get_global_var('func_1419')
func_1420_call = mutated_mod.get_global_var('func_1420')
call_3620 = relay.TupleGetItem(func_1419_call(), 0)
call_3621 = relay.TupleGetItem(func_1420_call(), 0)
output = relay.Tuple([call_3615,call_3620,])
output2 = relay.Tuple([call_3616,call_3621,])
func_3638 = relay.Function([], output)
mod['func_3638'] = func_3638
mod = relay.transform.InferType()(mod)
output = func_3638()
func_3639 = relay.Function([], output)
mutated_mod['func_3639'] = func_3639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_3668 = relay.TupleGetItem(func_782_call(), 0)
call_3669 = relay.TupleGetItem(func_784_call(), 0)
func_1645_call = mod.get_global_var('func_1645')
func_1648_call = mutated_mod.get_global_var('func_1648')
const_3689 = relay.const([-4.638200,-6.183761,3.159822,0.719365,8.391916,-1.901448,9.731103,-3.812729,-9.045598,6.918445,6.244963,4.383464,0.959464,-4.603135,-4.234502,-4.891463,-5.777587,-5.885298,0.334627,1.970779,-8.862809,7.997829,-7.008682,-6.117165,-8.734910,-0.255837,5.397856,-1.530407,9.217643,0.748704,7.304489,7.006836,-7.477972,9.830057,0.546662,-2.815636,-3.154214,3.984011,-9.701436,7.919030,4.844142,-0.109423,7.563049,8.668195,6.263021,6.752901,-7.959410,-8.166397,-8.039847,-3.865544,-1.132229,9.862802,-1.392232,2.156123,-2.034342,3.965626,-3.369331,-2.298521,2.637573,-5.180749,-8.104648,4.029917,-4.586078,1.890546,1.700138,7.130055,1.040973,-5.162605,1.051595,-8.778873,4.497664,-8.229471,6.415378,4.526299,-4.646699,7.263276,3.560866,-3.522436,-4.829980,-8.198290,9.389125,7.120703,-6.582126,9.874591,8.736239,5.679674,9.480481,-3.140488,-7.804594,0.836544,6.392299,0.428528,1.316094,6.030310,-2.563324,1.043104,5.941010,-5.176040,9.274560,5.946079,9.498085,9.875897,-0.776871,6.541866,3.056552,-3.043661,7.360637,-2.508380,3.973372,-7.241864,7.180262,5.607234,-7.653696,0.412306,9.037042,-4.104955,5.469233,-7.936941,1.007735,6.957738,-5.868168,4.892239,1.221336,0.922944,2.212488,-8.292751,2.068263,4.897260,3.294530,7.568937,-1.734947,7.376783,5.793728,8.220895,5.120772,-4.816510,-4.045987,9.101961,3.477142,-2.294644,-4.981944,5.291552,0.094554,3.596470,1.261203,0.975137,-6.266659,-7.361929,-1.898734,-3.296643,-6.530732,-0.607008,2.470715,-1.891333,-5.270108,1.981589,-6.553867,-4.431205,-5.494092,-9.671041,7.096232,3.525180,1.310533,4.838297,1.183630,7.720869,-4.798461,0.589642,-9.213595,-7.389440,-2.244114,4.374940,6.281573,-6.854105,-9.968955,3.911109,8.736252,8.135861,-8.878944,-8.605578,3.449058,3.636620,1.084474,1.510422,1.807331,-6.217553,5.426876,-7.149093,-7.952524,-2.124534,0.997395,-7.234271,-3.445827,1.434735,-2.930008,5.806528,-0.487643,-3.499420,6.686415,3.911564,1.435724,-2.393811,1.481214,1.336453,-4.849159,-0.035091,-6.797073,-6.782130,2.571664,7.470805,7.163752,8.532376,-1.629021,-2.579282,8.796834,-9.915184,4.371590,4.965646,5.874999,-5.093077,6.542003,2.960109,4.926505,-7.485706,-4.934350,1.076025,-1.494958,7.326994,-8.455047,-0.630471,5.757146,-4.862438,-0.040647,4.644443,9.942244,8.494865,2.443899,-7.047139,-5.751632,3.973067,-6.543850,-7.821001,7.476720,9.925185,5.833308,2.791495,-6.034796,-5.347488,4.976393,-9.570993,0.815487,0.286267,9.770880,-9.539761,0.407431,-8.060038,-3.365349,-5.693868,-8.152432,1.125455,-0.392147,-6.155179,-6.628557,8.448137,-3.338257,-7.763740,5.142021,-1.853611,5.025446,-6.190498,-5.120910,7.835116,6.927906,-6.098804,5.001754,-6.440453,-0.112428,0.883842,4.744831,3.804721,-8.864597,2.402134,1.857828,-6.400678,-3.397576,4.299797,4.438633,2.168213,5.186518,-6.080418,0.657010,-1.844342,9.863818,3.002033,-1.133674,3.148917,-8.233279,-4.834189,-7.095931,0.747345,1.056525,-7.455927,9.698794,5.554122,3.044756,4.980634,-6.457589,1.767058,0.897259,-9.188935,0.877370,5.663829,7.307256,1.379696,-3.954597,-6.454082,-8.115112,8.712919,0.030238,-0.962562,-2.932905,0.394289,9.126629,8.152912,9.123321,-0.901866,7.796036,9.122137,1.583928,-3.990931,1.132779,4.982394,6.638291,0.994140,4.708360,-7.652317,0.028846,6.968840,-0.720496,-1.450396,-0.050052,-2.554757,-0.047982,-3.040189,-0.704826,0.971514,-7.959285,6.040544,0.012232,-4.098607,-1.424411,5.044611,-3.428412,-6.437824,9.306074,9.947583,5.854592,2.222509,5.370021,0.175450,-1.419415,9.765019,9.257988,5.358984,1.538028,-9.527751,-0.489229,4.480935,-4.832626,0.507107,-0.544213,8.267993,-7.402298,8.262518,0.651724,3.091285,-7.775894,-0.578122,-8.511513,-6.919569,4.395052,5.580214,-0.383894,-4.801106,4.251315,-6.793905,-6.559522,7.091511,-2.431782,-4.266184,-3.446288,-8.984798,-2.941935,-2.304043,-8.703328,-1.000563,7.104924,7.164813,8.992777,-5.340140,8.119757,-9.022521,6.291189,-9.111351,9.982433,8.974817,-4.502363,-3.219151,-2.321854,1.323720,3.683590,-6.997410,-7.255949,6.927971,2.275817,-3.020403,-5.285910,2.001012,-5.875172,-1.584610,-1.886020,7.610023,3.174837,-2.913302,2.401862,-7.477498,5.895160,2.971779,-1.284842,1.759053,7.787239,-8.170759,7.779538,0.302321,8.800436,6.046558,8.205708,-0.048121,-0.661908,-9.132164,6.106315,-7.375101,7.878032,-6.836277,-1.463903,0.105990,4.198760,-5.692994,8.057622,-3.086789,0.025380,9.533533,3.528664,4.118128,-5.145850,0.679824,-5.397348,-2.035310,5.976629,7.136393,0.133512,7.231662,-8.856709,2.024383,4.339921,-7.509057,5.474304,3.218515,0.159966,-7.713398,-9.659384,1.177847,7.762337,-4.363093,-8.404003,1.065828,0.900122,-2.630516,-2.400901,4.421287,-3.126432,-2.003926,5.425107,-3.814686,-5.587489,-0.414087,-8.802554,0.179750,-9.297254,-2.958450,6.333638,-9.605052,8.052112,-7.648342,-1.049279,7.993431,8.817526,-1.909366,-4.884856,0.123638,3.628137,8.054173,-7.332134,8.415515,7.792915,1.474588,0.422608,1.233171,9.659389,-3.917480,9.327634,-3.625506,6.952851,-8.428869,9.091612,-8.145092,8.313937,-7.704553,-6.391217,-1.465056,5.808419,-1.649257,2.461144,0.779083,8.381146,-6.315402,-0.191845,8.722901,3.502924,7.138516,-3.603386,4.882258,1.820785,7.756704,-7.742631,6.878976,6.724833,-5.372450,8.136687,4.124370,-4.780900,-1.228957,-2.294436,-3.535678,1.656236,-6.698614,-6.431875,8.708234,0.276374,1.625842,3.819511,-4.115262,7.843892,6.092896,-2.557646,2.025607,6.026858,0.985106,-3.955648,6.156937,8.192087,2.976130,-8.691557,-4.903923,0.875553,5.205847,-1.672228,9.770904,-6.385257,5.610788,-4.805069,7.646522,-5.274176,9.086728,4.162279,-4.340290,7.648132,-1.463533,-8.953284,5.388163,-8.885443,-9.255826,-8.281990,-2.482379,9.971731,-8.485654,9.458292,3.435196,-5.403454,-9.339417,8.240013,9.547697,-4.558572,-2.026229,-5.800765,-2.280633,-1.692791,4.286960,-6.910383,-2.424617,6.909559,0.490139,-2.411798,-9.875288,-6.353252,-4.843325,6.153364,-4.964271,3.645647,3.572459,-5.321805,7.009144,-4.660402,-8.771665,-2.321845,-0.581564,3.940510,-9.768739,-5.108394,-3.958767,0.347535,6.958341,-5.591531,-1.221085,-0.654244,3.385898,3.509367,-6.630594,-2.740017,7.445158,0.643693,-9.382945,5.912082,-1.840028,-1.250952,-8.105583,-7.223240,-4.371711,1.353233,-4.669651,-8.810290,7.825351,-8.341681,-6.217302,-2.622300,-9.355935,3.011284,-6.236923,6.984356,8.118212,7.298116,-0.241140,6.047979,8.868615,3.670214,-7.636006,0.443090,-1.494317,6.439038,-2.647283,-8.609521,2.584875,-9.974410,-3.256621,7.430483,3.270999,-6.298912,-8.974216,-6.296082,-0.755877,2.243199,-2.371039,-6.800663,3.355280,4.528719,7.959591,-6.126446,5.972428,-5.364251,-2.884740,6.313133,6.378764,9.912279,2.160265,2.880008,-4.445718,4.955563,9.272459,6.460891,8.340570,4.420710,-2.047525,-8.615812,-8.309424,3.314237,-0.244880,-9.341986,-8.397631,8.498184,8.868786,-6.638041,6.084945,-6.156320,0.187324,3.024786,-3.066667,-4.096865,-3.133065,2.071340,4.681066,-4.013270,3.332544,4.939922,-6.632673,-6.940377,8.951243,6.945113,-4.516454,-4.159846,5.560059,-1.434020,-9.761017,-5.356768,1.202279,9.521488,6.083214,-4.109446,-6.134998,-7.545817,-2.200918,-9.815839,4.587001,8.077656,-3.680665,-4.273172,9.878825,2.995695,7.437410,2.988547,2.941123,7.631749,-0.482146,-2.138795,-4.818224,5.027395,2.858087,-3.142913,-2.896018,-0.415251,4.553556,-7.609476,0.047171,-3.666250,-1.871056,-4.332563,-2.215073,-3.942903,7.819365,4.663677,6.626300,4.874843,7.613183,-5.361120,9.516404,-1.803297,5.666318,6.080486,-0.867708,0.946215,7.643114,5.739890,0.229272,-0.824212,-5.802960,-3.796492,4.759990,-9.715945,-7.324794,-2.202534,6.012903,-9.342462,0.788599,7.989351,-4.454368,-4.178434,-6.347171,7.584277,1.148225,3.967115,-0.117425,-8.276094,3.891411,-8.522734,5.529778,6.541662,1.950924,3.407723,6.553800,-2.081126,2.611894,-8.292507,-3.002899,3.792067,5.219725,5.746531,2.705468,2.387880,-7.394395,-0.270359,-3.680590,-1.645059,8.191565,8.635996,9.562865,-5.681609,-2.790945,-5.563929,6.700018,4.094655,-3.994609,-7.861631,-5.582572,-3.866646,0.468556,-6.463560,-4.994369,3.353929,-9.857227,4.491677,-1.981716,-2.608105,-7.667297,-7.374039,-2.912542,-5.974851,-5.668197,-2.424497,4.082527,-1.305370,8.825721,-5.501236,5.136861,-3.669983,-9.444926,9.113669,9.070322,-9.248396,5.532426,0.299826,-2.184519,-8.187654,-0.681716,2.134457,-7.033740,-6.296551,-5.158375,3.105019,-0.735783,5.157078,0.334682,-1.160012,-3.759640,-4.095579,3.778308,6.607522,-2.635201,-7.734074,5.050468,-7.106517,6.503180,1.597800,4.214100,-5.100816,-2.121753,7.076996,-8.640892,8.553771,-6.714767,-4.203926,5.817988,9.339661,-2.438584,7.654005,3.363862,0.995028,-8.265296,-9.637815,8.567165,-8.612342,-6.575893,-1.230564,1.506105,6.689367,0.396596,2.429179,5.574391,-1.386296,-7.873246,7.862088,2.229800,6.623503,-8.463591,-4.073937,-2.519084,8.955250,-7.928717,7.961946,0.559501,1.190911,4.865878,-1.540978,5.113850,-7.808142,-1.153395,6.849020,-7.309854,1.694994,-5.701701,-2.253341,-5.567024,9.558520,5.532532,-5.222978,6.524532,-0.510670,-1.308732,5.007947,9.834334,-8.947979,-3.150039,-2.011003,-4.621135,9.424773,7.210830,7.966996,1.305369,-7.955781,2.650353,-4.343738,-9.233219,5.663347,4.046685,-6.327541,-7.540162,-1.992035,-2.242026,3.697024,-9.383444,9.973367,5.676593,-9.151140,3.680349,5.146108,1.043957,7.071058,-0.695682,8.711985,3.913121,3.588942,-3.937100,-8.330631,-0.652971,6.769462,-7.911832,-2.445095,5.135727,4.343976,8.722953,2.009363,-4.801439,-3.899726,-0.172724,-4.760323,5.506503,8.041619,0.928456,-3.451417,-9.759161,-2.030668,-1.878132,-8.410815,7.462567,-4.655323,-3.840326,-9.795370,-3.718872,-0.924451,-9.247389,-0.192046,-1.729401,8.743976,-3.631090,3.914054,7.729583,8.119831,-3.619639,5.403397,3.411288,-5.606273,2.750029,-5.941544,3.604797,-2.451726,1.869595,7.357015,8.326913,8.025466,-7.737947,-2.929286,8.734637,9.348778,9.964464,7.240825,-9.580067,-5.276650,-2.497160,4.251762,7.931540,9.378078,-5.654501,-0.169533,7.970953,7.128092,-6.154089,7.553632,-3.530322,8.954748,7.550932,-1.201000,-2.828527,-7.507952,-7.340368,-6.811695,7.066632,-0.233932,-4.412627,9.510203,6.271799,1.845252,-2.578693,9.211350,0.623066,-2.216450,5.903386,-1.406468,-8.717860,4.403868,-5.365659,-5.714185,5.336676,-5.500048,-8.278955,-9.811960,-8.900674,8.091786,-5.081381,7.564256,-0.528955,2.715070,7.769540,6.988910,-1.315603,-2.384478,8.917331,-5.649688,1.329153,-5.254847,2.671047,1.406324,3.567108,-1.879138,8.067470,0.693987,-8.233733,-8.643828,1.683047,9.708413,-8.909214,-5.626958,-9.157486,-2.608020,4.953404,4.929115,3.403866,3.959341,-7.958540,3.136625,0.767641,0.222621,8.538482,2.158026,1.962131,-0.555092,-2.972813,2.199186,6.340766,3.510503,6.109468,4.220362,3.018142,4.567742,7.011357,-7.743196,1.247406,-1.726325,1.835257,2.007968,-4.084264,-2.322594,8.580934,3.604428,8.168550,0.752645,-5.672962,-9.327256,5.243295,7.570898,-5.354840,-8.074500,1.722261,-0.333601,-3.411215,7.510447,9.846832,-7.533708,-6.895215,5.297573,-5.316862,-3.545437,-9.971596,-2.195736,-0.088126,-8.485670,1.181995,-6.589791,8.687045,3.692538,6.511188,-0.702135,-3.589172,1.300925,-3.765372,8.577015,0.547165,2.993886,-4.241413,-4.290636,5.951926,1.541364,1.485525,4.266742,-2.771006,-3.298566,-6.659097,-6.192188,7.847326,3.369098,-7.054346,-9.288918,-0.032918,0.952103,-0.943579,9.678710,-7.990898,-5.472507,-3.033119,-2.120715,7.750884,-0.729273,6.347373,-7.729067,-5.061958,3.429309,-7.450517,8.179244,9.112772,1.076406,-9.534191,-6.309466,1.637146,-6.040691,-0.527654,-1.606254,9.063706,5.077219,6.109469,-8.114660,6.229414,0.270349,9.624108,-1.025262,5.574123,-2.162764,-8.816674,0.594534,-1.262318,-0.069195,-6.842801,-6.058670,4.295672,0.603588,5.299675,4.149608,4.370320,0.259685,1.400037,0.793407,5.625153,-4.928693,-9.164067,-1.192829,9.303983,-0.619487,0.777137,1.300554,-3.605538,-5.705546,-2.126836,9.557187,-1.302559,5.013241,-4.503225,-9.782223,-8.901427,-8.808072,-4.063593,2.597191,6.798076,-9.595651,-8.976190,5.698366,-9.085843,0.107804,9.653916,-9.984992,7.010069,9.388964,-5.901157,2.662474,-0.563539,-1.808319,-1.373279,-4.800762,0.301060,4.002248,5.417108,-4.806687,-3.442166,-1.271720,-0.183492,2.494605,-4.324610,-1.827463,-8.156004,-4.102210,3.483605,-0.350174,-2.491535,0.106887,7.802980,-8.420755,9.056143,-3.773202,-0.013107,-0.558073,0.075940,-6.027555,-4.748986,-7.503276,-7.817668,-5.939709,8.039589,-3.253159,6.098543,9.957152,-4.813437,1.382913,3.878860,2.101824,1.236335,-4.575238,9.862610,-1.266079,2.243337,-6.100796,3.338577,0.139414,2.710653,0.010446,2.891477,6.920392,-7.276332,-7.188848,-7.417438,9.844271,5.637936,-6.703933,-6.507470,-5.341450,-4.467354,3.805915,8.006311,-2.715980,-8.202008,-0.548466,8.086331,4.545659,-5.000503,3.007816,0.169911,-1.587375,-2.857028,2.175604,-8.118239,8.587164,5.138877,-9.246642,1.939031,3.697816,-8.410449,-1.893564,-8.115609,9.471435,2.629272,3.234037,5.151093,7.653109,5.614918,-9.615723,-9.421246,-4.206388,0.051107,1.067464,5.284201,-1.457916,-0.377057,4.575090,4.727600,7.949330,6.606196,4.049859,4.394262,1.720023,-7.059932,-7.170849,2.380144,-9.993274,6.928747,2.649962,-3.460671,2.657097,-9.884988,6.251597,3.647540,-1.931604,-5.198545,-5.104357,-8.753237,-7.131497,2.103685,-3.810151,1.575458,0.216170,-4.970739,3.149816,7.844111,8.550758,-6.978584,8.961058,7.886700,-6.713486,6.322207,2.793106,-3.544344,-4.654454,-0.780498,-8.118311,6.727908,2.146485,3.063673,0.747776,2.393964,-3.182715,1.604978,0.101369,-3.251579,-8.813766,-2.005575,7.219347,4.572556,2.645321,-2.631406,0.162896,5.502374,3.654754,-4.414335,2.346192,9.091504,9.929424,2.150624,-3.378001,-9.072673,-6.311152,-8.375146,-4.688542,5.246118,-9.772593,6.984504,-0.775448,-7.941374,1.325427,-7.991449,-5.265622,9.845554,-3.033147,-8.662209,-1.742411,-0.976098,-1.208312,-9.366788,-7.298603,-4.013389,-3.798467,6.901856,-3.698486,-6.511480,-5.199022,2.377129,8.067143,-0.527766,3.461803,-1.652365,0.172517,-3.350109,8.306347,-1.504107,5.557276,-7.382462,4.686342,-1.064443,2.356889,3.986282,9.320351,-7.071287,5.080385,-9.831248,-5.731402,-5.752506,2.523126,4.536943,-2.901718,0.154741,-6.271579,7.338559,1.335467,0.213144,-8.279589,-0.806482,1.718614,-1.779832,4.619895,-4.877039,1.967428,4.748700,4.550910,-7.727463,2.676848,6.206630,9.197101,8.217620,-2.075621,-8.841355,9.785092,-4.465448,8.706534,-2.149147,-5.142564,-5.904699,4.808378,-6.200818,-2.338444,-9.000098,-6.568359,0.838386,-0.264315,-4.686287,-8.976636,-2.020282,5.343319,-9.779668,4.999030,4.201110,8.836991,-4.467399,-1.046058,-3.600205,4.811463,-5.543827,-8.881926,6.630829,-5.082308,-3.497160,-3.751619,-1.402157,1.841632,3.398651,6.177898,-6.576994,-6.991822,-7.478855,-8.750047,-3.094327,0.626760,3.278832,-4.798304,4.050102,5.585591,2.644922,-6.103526,4.947666,1.143139,-7.979096,-6.045241,6.335063,5.159208,8.214476,-2.501190,1.015714,-7.218948,-0.467035,-3.363639,9.941886,0.449694,7.171506,-7.962880,3.593518,7.533687,5.202393,0.684740,5.763841,-4.316068,-0.347004,-7.834918,-9.197783,-3.977793,2.835636,-2.999931,-0.179947,-4.327671,2.958953,0.558504,-8.993930,8.419425,-3.396462,-4.195421,8.646315,-2.198442,-9.951011,-5.424950,7.188035,0.021555,7.585486,1.199591,7.455326,1.870612,-1.940216,4.175515,-8.423199,-5.978068,6.362767,-9.656109,5.090021,-0.207225,4.918554,0.251430,-4.068618,9.729502,-8.834647,5.576876,-1.297873,7.406174,4.094037,0.263620,0.027426,-2.943714,2.440050,4.420811,8.401119,-5.567051,-4.168717,5.125701,-4.715691,-5.404123,0.908526,-1.945336,4.412054,9.099852,-1.348306,-9.271620,-3.152263,1.008541,6.780951,4.187072,-3.431870,3.178834,6.311205,0.607385,3.528194,-7.163903,-9.443528,7.397037,-8.580039,-7.839649,7.400411,-5.157271,-9.886748,5.806218,8.833812,-1.577783,-6.022987,-3.366604,4.058981,4.053543,-4.247909,6.729092,-4.620475,-5.480032,4.499606,-2.122510,0.528521,3.946367,-7.846005,6.366933,7.285670,2.149972,5.654733,4.328823,-2.835722,2.244754,-7.222834,8.412798,5.701300,-1.462451,-6.301014,-5.820689,0.379563,7.262806,-7.842931,7.535213,1.707748,-2.960639,8.487642,0.471792,-5.162957,-0.099695,6.152491,-1.736391,1.069685,-4.396965,0.168266,0.143315,-8.188065,-3.028018,3.570047,-7.168757,-5.070975,1.099569,-2.643804,1.016268,1.184239,2.450613,7.370208,-7.191017,-4.718574,4.208065,8.362383,9.421331,2.859713,-2.238079,8.575547,3.499559,7.537413,1.681842,6.670177,0.623591,-7.962185,-6.687556,-7.607733,-6.542660,1.462884,-6.348629,-7.768873,-4.981580,2.154209,-7.575092,4.751858,-3.319313,-1.416961,-9.749439,7.710470,7.656513,-1.352224,0.596324,-8.907755,-8.630165,4.622278,-4.527702,-9.022710,-5.617539,9.564592,-5.922126,-4.555894,-7.731996,0.286938,0.321240,-6.131133,-8.042457,-7.806524,3.302388,-6.661965,-0.540626,-7.277069,7.203212,7.740462,-7.269291,6.352632,8.075130,9.827652,-0.372526,-9.172386,3.066661,-6.727267,2.349165,-3.329631,2.079682,-3.483556,-8.493188,-1.904828,4.136609,2.457046,7.124311,7.281942,1.858606,-8.362649,1.602337,7.290149,7.771790,-4.568001,-7.112606,4.474363,7.937785,6.718902,-5.611156,-0.191153,1.128778,8.868183,-0.172553,1.266104,7.668655,4.494663,-3.996423,-5.394588,8.462291,-2.111806,8.723908,7.386851,-7.977757,-4.440032,8.118683,-2.044012,7.882198,2.589929,-4.475969,0.963793,-0.338772,-8.042384,2.652948,-6.091305,-0.800084,-4.736062,-0.581764,-6.831487,-6.993363,7.109459,4.091479,-7.154424,4.751406,-7.611399,-7.591103,5.013816,2.404909,6.792385,-9.104828,1.855724,-4.094486,-2.344409,6.593031,1.296957,-4.388265,9.352660,2.979538,-1.708150,3.128895,-6.312570,-0.630159,-8.452156,-5.842244,-1.008991,6.913314,8.688260,0.650451,-1.124377,-0.617114,-6.941990,-5.214665,0.469003,8.351853,-8.805851,-0.272658,-8.196768,2.857969,-8.174909,-3.898453,-6.395883,-4.056772,6.708465,-6.515759,2.374391,-4.070324,0.791171,3.805529,-7.628132,-9.945109,-5.623039,2.496759,6.312165,4.094438,-8.131290,-0.801366,-8.840391,-4.827176,-4.975309,2.844470,-7.068123,4.150067,1.649571,-0.793579,3.672937,-2.149100,5.024089,-1.081281,-2.326856,2.310814,7.550044,-9.327036,-4.381854,0.035524,7.822887,-9.638474,-9.589620,7.665598,6.104888,5.504975,-7.626676,-2.742979,-7.562391,-6.735130,-6.937471,9.137520,8.656788,6.308283,0.012022,-8.007848,-7.906754,-4.013370,-0.238296,-0.932817,9.968264,-7.243225,8.370211,0.247919,1.974581,5.849791,6.531772,4.237364,-3.742091,2.527980,8.744231,-9.281626,-0.084932,4.147859,-1.239976,-9.907248,9.015499,1.357298,8.240060,-9.288108,-7.575899,0.863572,2.065240,-8.671395,2.484319,3.957464,3.943704,-3.877455,-3.924240,-5.840414,9.919979,-4.893142,2.536396,-8.449513,-4.210274,4.741121,-7.020489,7.113738,8.119185,9.038510,7.302999,7.068392,-2.047770,-5.104636,7.104029,8.650041,-4.411900,-3.740115,6.150240,-9.287644,4.503413,-1.445759,-5.669296,3.303318,6.383470,4.406786,2.743727,9.083095,-2.273723,-0.106625,-4.993612,8.557408,4.686192,-2.027966,-7.229486,9.852879,-4.919017,5.218935,9.233867,-1.413722,7.023796,8.368842,-3.247218,-2.376707,-1.262636,0.451529,-7.180708,4.750264,-6.936019,-3.765730,0.467511,-0.572033,8.133409,-4.930486,3.120825,1.481081,-0.155254,6.176890,6.132485,-8.567828,2.700268,-0.934621,-3.192870,4.195653,2.759672,0.058900,9.762100,-2.508273,8.044360,7.997777,2.955808,5.201959,5.537160,-5.388265,-2.636314,1.032008,-0.570969,1.471047,2.129734,7.597740,-2.699612,0.050856,1.246525,-7.873640,5.579348,4.594397,-1.585531,-5.163184,4.412931,-3.087756,0.570373,2.925858,0.861262,-9.650093,-2.297281,2.863227,-6.362858,-2.466155,-9.244832,-3.512572,3.704713,-7.593214,-6.946736,1.215243,7.192221,0.944626,4.253999,5.858172,8.542691,-1.167599,9.387849,-6.840276,-6.427507,2.606831,7.872290,-7.223758,6.157161,-7.001393,-7.168516,-6.166716,5.227262,-9.106478,-4.588327,5.896049,-4.337942,5.412772,5.706652,5.854936,8.074385,-0.560165,7.577310,2.172899,9.202611,-2.123707,8.499702,-9.612776,2.923608,-8.548952,-7.818515,1.463385,0.413440,-3.588498,9.533167,-3.456240,1.346169,7.909237,-4.085678,5.088903,1.448948,7.008199,-1.404431,2.063165,-8.396487,-4.267320,-6.380203,8.898017,-6.296171,-7.422430,-1.395440,-2.661073,-5.994141,-5.708235,-6.667537,-7.242516,5.053968,0.970080,8.426128,8.239350,-0.758154,-9.059189,-8.219281,-3.924772,-3.585231,-4.157899,3.573708,-9.674967,-6.034152,-7.876996,-8.184677,-4.645674,-8.848572,-2.019710,4.967126,-0.537468,0.035404,-5.737526,-9.477941,-5.226417,6.240792,9.000816,-2.261495,-7.207967,-0.418059,3.853846,-5.935751,7.097437,1.779772,-0.714710,7.603282,-3.471201,-3.235544,-3.131071,4.995526,0.143389,0.331264,-8.139785,-5.863041,7.422685,5.901905,0.779451,-9.094163,0.922503,-4.640745,-9.302320,-1.930141,-4.981717,6.419840,2.280084,-1.097398,-2.259162,-4.177400,7.900648,1.979824,4.741117,2.693638,-2.549053,2.008153,-6.608808,-3.556781,-5.441014,0.535518,2.128511,2.437614,-0.127704,1.486840,-3.183288,7.719984,-5.726742,-6.838031,6.846724,-1.673529,8.864035,6.703419,-5.017996,6.969320,-9.295812,5.469167,5.704051,2.335645,-5.193593,-3.287890,-8.924658,-5.260719,2.836639,-0.208207,7.562471,-5.182546,5.999346,-2.782774,6.227006,-8.976333,-5.845214,4.991559,-2.537177,0.557618,4.208992,6.685571,8.763833,-2.135364,-8.251048,-6.047901,-4.785933,9.372625,-7.573788,3.505755,2.850072,-7.801094,3.500874,0.010835,-7.552140,2.451070,0.407295,7.684248,-3.250344,0.619905,-3.771112,-3.197340,-6.724893,-2.620632,2.429272,8.359793,9.271539,0.214419,7.530419,1.573190,7.113500,-5.719877,4.313478,-9.871552,0.751327,7.465359,4.061437,-0.002326,1.962027,-8.311917,-7.648604,7.739745,0.459083,7.436564,5.402634,-4.625507,2.794389,9.628883,-4.067282,-1.545420,0.170357,-5.184476,-9.917186,8.220567,2.770297,-2.713252,3.216828,-2.432818,-6.248866,0.681166,-6.421720,4.100431,-6.618692,-3.565624,-0.484893,6.124662,-2.709180,-7.556909,-5.794359,-4.894552,8.548026,-4.047670,-4.004866,-3.639907,-8.036540,2.832304,7.908248,-3.069615,9.283686,3.499324,7.651440,-6.351592,-9.990683,-9.280247,-4.580808,-5.768433,-7.957116,-2.192872,8.595649,7.822095,-9.252278,-8.631594,7.359679,-8.869979,-1.628645,-2.242260,-3.570956,7.951150,3.256972,6.137672,0.864358,-8.841298,-9.749998,-4.480377,4.061255,3.744291,-6.427117,9.340353,-6.450371,8.950929,3.717534,8.006089,-4.176570,-2.946743,-9.254953,4.479990,-2.916170,3.416434,-0.258775,-2.587877,-2.096466,2.932582,-7.186469,-6.540689,-0.021565,4.630676,-5.795003,4.038918,7.702216,-8.070510,-8.789214,4.471565,8.634345,2.072584,0.344930,4.412503,-5.962611,-4.193800,-1.591051,9.392156,-1.603716,-5.532273,0.468212,8.959477,-7.876847,0.818899,4.670542,6.122780,2.610534,-8.941183,-3.438732,-8.914584,0.306818,7.806898,-1.998816,-3.212958,9.103735,0.750487,1.791585,-0.143219,-0.404964,-8.097253,-9.376308,7.553994,-2.865774,-5.604208,6.879034,2.496507,-2.827847,-5.608132,-4.252094,5.050445,-1.662632,-1.662749,-6.563696,0.533695,-5.056341,-1.828620,5.899284,6.461768,-0.818753,-3.604617,-1.767590,-8.001138,9.614753,9.462310,1.223037,0.385081,0.637211,6.574339,-9.679909,6.217017,-9.839853,-0.080964,7.399721,-0.999267,4.524951,4.990440,-0.446793,-4.483015,8.009012,6.070118,7.492565,-7.556450,1.981556,-4.844658,-1.070354,-9.869136,0.160697,-3.133983,-8.962928,-1.708891,8.232447,-1.041450,4.686670,2.917374,-9.250649,-5.275164,-2.663077,4.914130,-2.527936,5.010307,3.492718,-1.601121,-3.803002,6.219877,2.218502,2.159240,1.469941,-6.877541,-5.608942,0.500270,7.748542,-2.022754,-3.501280,5.898894,0.973403,2.132647,-6.586386,-9.177889,-4.526727,-6.842691,4.081112,4.173435,3.281004,-6.695236,3.138797,-8.584169,9.502704,-7.970599,-2.894039,-5.296144,9.335938,-8.441102,6.983790,-0.912459,-3.768201,0.380974,-0.591100,1.715236,0.759548,-3.266106,0.968720,8.324716,0.850303,1.521781,4.424104,-9.110154,3.686787,-7.378691,3.371550,8.616104,6.657757,9.732631,6.562350,2.150434,-7.970394,8.622019,4.141949,-7.673267,6.507194,-8.071751,-3.396068,8.714813,-3.013960,-6.319511,-3.105076,9.416595,6.688139,-6.349531,0.175044,7.107646,3.800403,-1.900608,9.570532,9.065016,-8.984524,5.377426,-5.441161,-3.347092,-6.981422,-9.318102,-8.886740,8.846319,1.702586,-3.212004,5.318324,-0.497826,8.105141,6.283393,-4.364976,5.277437,5.782594,8.502449,3.779749,-2.915556,-4.614938,-5.530624,-2.151756,-1.765124,7.175146,9.282091,-1.431969,1.984235,-7.914527,-3.964152,-8.360767,6.421706,-8.850743,5.333320,-2.622189,-4.405943,7.720748,-6.084421,-2.938885,3.671809,1.677956,-0.755134,-9.071271,3.946828,8.000425,6.533950,3.429816,6.135717,3.651501,2.792347,-3.319943,9.821090,9.677689,8.501145,-8.451008,5.160989,7.118749,-4.039409,-3.370953,-6.998155,8.995486,0.251860,-0.740169,5.158840,3.246723,-4.580847,-2.269613,6.326794,7.932830,2.753539,2.010587,0.593079,-6.671675,5.987598,-9.818328,-6.410334,0.942550,-2.256256,-4.055818,-5.976634,5.073119,4.927956,-3.840412,9.959276,-4.285763,8.436118,7.413401,-3.641517,-3.580720,-8.914054,-7.726108,7.907971,-1.427211,1.280871,0.377416,0.848774,-7.834358,-1.372423,7.565522,-7.249616,-3.493832,-3.775554,5.331997,4.517155,-2.216073,-2.996916,4.124993,-5.084517,9.988129,-1.887137,2.619034,1.045380,4.086535,-2.417064,5.269590,-9.469942,9.492696,-9.888106,4.195948,-3.951971,6.427731,-5.860250,-8.277313,4.038598,4.371600,-7.840814,8.145786,-3.421155,8.314857,3.831521,-7.578785,-8.640895,-2.696919,-2.608269,7.149980,7.138808,2.997402,5.115893,8.988080,5.478088,-7.768473,8.306694,-9.692528,-8.909601,4.317138,-0.355140,3.634614,3.485012,7.871013,-1.385205,-1.548115,-9.940582,2.721936,-2.725468,-5.058054,8.544445,8.541673,-1.376983,1.632448,-9.786881,-1.866327,-4.885012,7.574623,-9.958524,8.051337,7.460721,-0.341535,0.025279,5.933032,-9.845019,2.258708,0.731024], dtype = "float64")#candidate|3689|(2640,)|const|float64
const_3690 = relay.const([[-9,1,-8,4,8,6,2,3,-9,-7,-6,-3,10,-2,-3,4,-9,-9,-5,-1,-5,-4,-5,4,-5],[-8,-1,7,4,-4,4,-10,-4,-9,6,-4,9,9,-7,5,-5,-5,5,10,1,-8,-6,9,-9,-1],[-10,-7,4,-2,-10,3,1,-4,9,-8,9,-7,-6,5,9,-2,4,8,5,9,9,1,-7,8,10],[-6,4,4,-4,-7,8,1,-7,9,9,7,7,7,4,10,3,-5,-3,-9,9,-7,-5,6,-7,6],[-1,3,-3,-4,8,-3,3,-10,-6,-3,-6,9,-1,3,-9,6,-2,-2,1,-3,1,2,1,-10,2],[1,4,-9,-6,2,1,-7,-7,9,-4,-9,-8,9,-6,8,2,7,-9,10,-9,1,8,-5,9,-5],[8,-10,-6,8,9,9,3,-5,2,-8,-8,1,6,-3,3,10,1,-8,8,-8,-1,-6,10,-9,-1],[-3,5,-6,-3,-8,8,-10,7,-7,-5,1,9,2,-1,4,-7,10,3,7,-7,-4,2,-6,-1,3],[6,-2,1,6,5,3,-9,6,-3,9,7,-6,9,-7,5,-8,1,-7,4,-6,5,2,6,-9,-2],[-8,-4,-9,6,-3,5,-1,-1,-1,-4,-7,8,-5,1,3,4,4,4,1,9,-9,7,-1,10,7],[-10,-3,4,-3,3,10,-5,-3,6,-9,10,-9,9,7,-3,3,7,-2,-3,-7,10,4,-2,6,-1],[-4,4,7,-3,-3,9,10,2,-8,-6,3,-2,3,4,-3,4,-7,9,2,-10,-10,2,4,1,-1],[7,-5,9,-5,9,9,3,4,9,6,10,8,-6,-6,-2,-8,-8,-10,-2,1,10,5,-5,-7,-4]], dtype = "uint8")#candidate|3690|(13, 25)|const|uint8
call_3688 = relay.TupleGetItem(func_1645_call(relay.reshape(const_3689.astype('float64'), [2640,]), relay.reshape(const_3690.astype('uint8'), [325,]), ), 6)
call_3691 = relay.TupleGetItem(func_1648_call(relay.reshape(const_3689.astype('float64'), [2640,]), relay.reshape(const_3690.astype('uint8'), [325,]), ), 6)
uop_3694 = relay.asin(const_3690.astype('float64')) # shape=(13, 25)
func_1999_call = mod.get_global_var('func_1999')
func_2000_call = mutated_mod.get_global_var('func_2000')
call_3696 = relay.TupleGetItem(func_1999_call(), 0)
call_3697 = relay.TupleGetItem(func_2000_call(), 0)
func_3184_call = mod.get_global_var('func_3184')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_3700 = relay.TupleGetItem(func_3184_call(), 3)
call_3701 = relay.TupleGetItem(func_3185_call(), 3)
func_1074_call = mod.get_global_var('func_1074')
func_1075_call = mutated_mod.get_global_var('func_1075')
call_3710 = func_1074_call()
call_3711 = func_1074_call()
bop_3712 = relay.maximum(uop_3694.astype('float32'), relay.reshape(const_3690.astype('float32'), relay.shape_of(uop_3694))) # shape=(13, 25)
func_3347_call = mod.get_global_var('func_3347')
func_3348_call = mutated_mod.get_global_var('func_3348')
call_3717 = func_3347_call()
call_3718 = func_3347_call()
output = relay.Tuple([call_3668,call_3688,const_3689,call_3696,call_3700,call_3710,bop_3712,call_3717,])
output2 = relay.Tuple([call_3669,call_3691,const_3689,call_3697,call_3701,call_3711,bop_3712,call_3718,])
func_3719 = relay.Function([], output)
mod['func_3719'] = func_3719
mod = relay.transform.InferType()(mod)
mutated_mod['func_3719'] = func_3719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3719_call = mutated_mod.get_global_var('func_3719')
call_3720 = func_3719_call()
output = call_3720
func_3721 = relay.Function([], output)
mutated_mod['func_3721'] = func_3721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mod.get_global_var('func_2824')
func_2825_call = mutated_mod.get_global_var('func_2825')
call_3732 = relay.TupleGetItem(func_2824_call(), 1)
call_3733 = relay.TupleGetItem(func_2825_call(), 1)
func_1880_call = mod.get_global_var('func_1880')
func_1883_call = mutated_mod.get_global_var('func_1883')
const_3735 = relay.const([9.734718,1.235292,-3.264402,-4.524555,-0.737108,1.779721,-9.324274,-4.513718,-3.495318,-4.160336,1.568250,-1.947945,-2.658047,8.209452,3.025173,-9.525755,6.724499,-0.731890,-1.990639,9.258155,-9.067927,-4.613364,-8.947815,2.441693,-1.598295,8.039046,3.248043,-6.871549,3.497576,9.271761,-7.320372,8.280731,8.389433,-3.589765,6.916918,0.085122,-5.609280,-8.418908,-8.763161,5.040369,8.187624,-6.275126,-6.318623,-6.752207,-2.388730,8.871777,8.523870,-7.415199,-2.209572,3.026240,2.691089,4.461534,-8.706116,-2.728033,-0.891268,2.807609,-0.074466,-6.750148,-8.042747,-9.366889,2.685257,-1.783897,3.608820,7.539348,2.007145,3.443047,6.492614,-7.284751,-5.367624,4.790342,5.152175,-9.394904,-4.941046,-7.735752,8.937173,-9.904988,-6.080806,2.149536,6.741462,0.943531,4.202937,3.905270,-9.098481,-1.692427,-9.746122,4.639430,-6.029823,-4.215872,-7.294656,-6.730786,4.807957,-0.411431,5.193410,1.808266,2.562029,9.481691,3.599248,7.509351,-3.950130,-5.152648,3.232760,-4.759058,3.127281,9.413181,-1.865050,9.978768,-0.224294,4.378358,-6.770582,-4.087543,-5.976247,-3.153405,1.094288,8.419682,-9.359792,-6.847602,4.620429,9.752644,7.621186,-7.062902,-5.579130,-2.117833,-4.585675,-8.483405,-9.678563,-7.396527,-7.437831,9.502996,-4.244360,-6.833916,-8.107871,1.131035,7.604358,5.259358,0.986612,-1.264816,5.345064,-8.292627,4.478670,-5.155847,1.377710,-5.094642,-8.330089,5.962382,-7.636820,0.351218,2.417216,-5.920135,9.991607,9.286960,4.260881,6.002679,-8.181265,-1.035617,-6.982254,-4.342662,0.787266,-1.018580,-2.262644,0.203693,9.918307,6.046621,0.622978,5.461507,0.794045,6.797887,7.534913,-0.813770,-8.959961,5.279015,2.638709,-0.588108,-5.244332,-5.670233,2.253035,1.242346,-3.652544,9.088092,-9.678264,7.418104,4.549363,-2.620191,8.236276,7.879072,-1.467496,-7.366352,-4.992700,-2.864490,5.680576,5.713270,-6.050819,1.942205,0.022988,-1.978140,-8.234660,-5.562625,-5.744169,-6.034727,3.354797,7.878994,-7.788483,5.121239,1.703371,4.913293,6.572811,0.772977,1.368773,-9.145763,6.811264,-4.465142,-4.666897,9.360269,6.651014,-8.079123,1.299285,-7.665110,-9.589600,-1.947604,-4.273197,-8.157588,-4.424958,4.068255,7.342102,9.597013,6.144563,-2.119504,-9.779856,-6.313911,3.058979,-3.769833,1.516902,-7.951970,-3.858973,2.301796,-9.029231,-8.639364,5.893692,-1.236357,-1.966048,7.945070,8.774805,2.025094,6.047569,2.797386,1.300609,-7.804395,0.098580,-1.952491,5.031761,-7.448680,5.514385,0.448879,-8.702742,3.946876,9.519965,-1.208261,-8.651408,-7.696268,-6.640451,-3.540947,9.504803,-6.792777,8.883218,-7.120914,-6.711800,-1.141576,-5.265368,-2.520498,0.484626,2.063044,-0.440338,0.079825,5.991901,-5.039349,-4.314560,7.787968,2.769927,-4.238632,-2.850490,-6.949272,8.624783,3.479738,-4.332455,-7.089254,0.097180,-0.600916,-8.044369,7.049082,4.410418,0.847311,-4.148054,5.498009,-8.220180,3.292553,-8.781477,5.943337,-8.513244,1.134576,-4.759333,4.005614,8.934901,4.108919,5.198028,-6.068404,-4.313668,-5.648806,-8.530784,4.875767,1.292952,-7.966541,-0.060262,2.360131,-0.903070,2.949811,7.807685,-7.265522,-5.153456,-2.761672,-3.423577,-1.154152,-9.209683,-9.665843,-3.151104,1.353448,-7.028824,3.775976,9.006518,0.691783,-2.330368,-9.798994,6.213896,-6.712643,-7.857903,-7.399676,2.592217,8.453868,9.448160,2.017791,3.396196,-1.522969,-7.785329,-7.269668,-8.549942,1.912791,-8.497316,-3.774317,-9.308974,6.373693,9.424343,-6.592895,-4.457560,-9.955836,4.598058,2.639485,-1.009868,-6.139565,-4.294188,-4.454308,-5.994319,2.593765,5.579347,2.583492,-2.701192,-2.053179,-2.962081,6.677357,9.778504,-3.728901,7.145392,0.536734,0.960508,-5.929141,1.497256,8.428312,-6.507466,-3.371602,-1.188105,5.743336,0.996638,4.564767,-5.196570,-4.740045,-9.750572,-3.185572,8.567401,-8.563174,1.850317,-1.677885,7.309695,3.550374,-2.246184,-8.504573,6.418930,0.934819,0.817563,-3.848191,3.063438,4.165451,8.618905,0.488146,-1.185136,-8.552764,-1.394422,-3.557301,-0.766058,6.591576,0.979705,1.771459,-5.449919,0.975101,0.571294,4.912833,2.296408,9.560263,7.061233,9.460747,-5.612627,7.673761,-7.275834,-8.440852,8.929341,4.204147,0.029341,1.511696,0.067479,-2.673954,-4.388677,-8.265179,-1.454059,6.500888,-1.090360,1.431146,-9.927483,-3.022693,-9.901714,6.916099,-8.940090,9.212787,0.535790,6.858709,4.571341,-8.031290,-2.127792,0.852769,-3.943356,-7.615286,6.330042,3.926913,-8.637287,-5.198035,-4.573618,7.061721,-0.021195,6.439317,2.170544,4.813686,-4.350928,7.212768,-0.783237,2.012440,9.802700,5.161915,-8.810848,-0.327418,-9.330403,7.488708,-0.144958,-7.221388,4.323141,-8.735364,-0.343432,-2.118807,2.329916,8.610505,-3.597005,-2.191357,-1.676895,8.453616,-4.117509,-0.428807,-5.520724,-4.977042,-5.632132,-2.923740,-4.959520,-4.638807,-2.930304,1.522568,-1.607621,0.823074,7.601979,-3.999827,1.767587,-1.956844,6.032364,0.591162,4.619618,-8.518654,-5.054960,6.738627,-7.009902,9.066019,-2.642989,-5.274844,-0.709378,-5.935543,-8.784095,0.262458,-1.493013,2.026113,-1.403449,2.226233,-9.873825,2.017625,-9.308263,2.979418,5.839909,2.703393,5.391650,-9.651664,7.113340,-4.656259,-8.994960,-4.922339,5.470394,-4.949840,-5.962790,5.768516,-5.058526,9.526401,-6.738091,9.801721,8.080174,5.746434,-1.400904,-2.956714,-0.421346,3.397786,9.414273,1.893708,-7.951795,-6.630805,-5.931204,0.110464,4.710332,9.184339,-3.610048,1.442694,-6.841442,-2.921041,-4.692913,-7.139296,0.414177,8.451821,4.383159,-1.031538,8.620616,-2.536415,-4.611516,-9.231343,-3.583216,0.995611,-0.628248,8.385784,-1.414044,3.953804,-8.874010,3.690136,-7.054781,-9.260151,-1.507470,6.885690,-7.859366,2.090633,2.284376,-0.253956,2.815016,-9.312403,-4.536368,-3.100348,-6.052524,4.404520,-8.777444,-0.063369,-2.929278,-7.643397,4.859125,-0.832351,-7.957910,6.474178,6.568996,5.428801,3.671566,-3.664507,0.412947,-1.943009,-1.994020,8.680708,9.441117,4.790257,-6.465942,-9.780955,7.717373,8.962670,-4.343267,-8.181466,-4.321343,-2.713128,9.221586,2.021657,-9.916352,-3.870184,-4.226812,6.600535,-9.561950,7.736122,-4.355325,-8.785621,-3.795777,5.509584,-5.713184,-3.249194,-4.094556,6.454376,3.768668,-0.466838,-8.155051,-5.631343,-3.727336,-4.240561,4.364008,-5.073955,6.667050,4.927194,-8.594255,-6.560257,-8.402769,-6.110607,-2.456552,6.525865,-6.301778,2.630421,-5.471930,2.358218,7.806875,3.909276,0.559182,-7.609886,6.977977,-5.145799,6.514274,-8.660410,3.161598,-0.134916,-7.506838,0.068248,5.429020,-9.662945,5.220008,1.626316,7.424896,3.843861,-6.082415,-4.578703,0.972661,1.580887,8.984244,2.132263,-4.177261,-6.763145,9.873101,-6.783439,-1.344794,-9.894652,-4.958730,-6.987066,8.978707,7.274435,-9.190212,2.749700,-2.484119,-2.573352,-3.883920,9.711083,5.182182,-3.069567,8.156761,5.850327,0.715452,5.312366,8.398970,3.271587,3.609390,-4.579945,-4.716078,-5.938956,5.376827,0.892125,-7.484041,-8.866654,-7.549490,-1.839980,0.903477,-9.062065,5.759792,4.834054,2.230957,8.614260,3.016887,-1.431362,6.391948,-9.555931,6.499176,2.960571,-8.525766,6.444912,-5.120664,2.776111,-4.765285,-8.764721,9.607411,-8.913606,-8.800628,-4.997738,-3.366493,-9.342042,1.973688,-9.437485,-7.387751,-8.063660,3.474121,0.090091,2.577578,-4.302594,-6.757917,7.938933,-3.318123,9.924450,-0.438579,-9.808257,-5.237271,-8.586535,7.042237,8.107907,-6.732247,1.090509,5.326484,9.541615,5.435457,-1.096564,-0.675737,8.220780,-9.900274,-9.593976,-1.785339,8.087810,7.316474,-5.559947,-3.122438,-8.908019,0.769140,-6.661078,-9.558395,2.359670,1.573110,-9.002838,-5.365847,-2.486364,-1.355526,9.560882,7.776061,1.364446,-6.557207,-4.200129,4.305726,-0.630218,-1.612896,-3.335006,-9.782253,-8.266041,9.555819,-8.052782,-3.342699,-0.195893,0.148693,-3.752411,-8.683996,0.934982,3.424998,8.287539,-6.640449,-3.897115,3.142021,3.946717,-0.807766,7.444948,-5.916021,7.981530,9.896593,6.830368,0.305885,5.291305,-2.213202,3.764577,-6.038733,-5.951338,-1.916982,2.575079,9.061257,5.552556,-4.328823,-0.987202,-1.479135,-0.266548,3.744441,-2.409721,0.143716,7.187171,-2.956129,8.856133,9.647436,6.483842,-2.930128,5.561148,-5.703315,-4.403815,-8.802569,6.326918,-9.540430,-0.379200,-6.811984,9.502267,-8.648778,0.777687,1.801289,-1.903856,-7.025270,-7.896244,-8.633626,6.028559,-8.439817,-0.197057,-8.349645,-8.504516,6.276270,-4.258867,2.598495,2.518359,-5.460420,2.965710,1.395519,4.783963,2.177369,9.160664,2.337056,-4.223756,-8.569343,-7.946630,4.447766,4.245626,5.048460,-7.682364,5.012061,3.834282,-7.868296,4.506679,-3.191295,4.866298,-0.892459,4.640434,2.808359,-3.598275,-3.484869,-6.045493,3.233287,-0.214127,-4.537245,6.425067,-3.830969,3.342671,3.697505,0.499889,6.294236,-3.911142,7.943061,-3.895415,7.356532,-1.880799,0.007174,2.764359,-0.237855,-4.571414,-6.639650,5.487726,-0.651043,2.596221,5.411967,0.418705,-7.046732,7.512596,3.585346,-2.609431,-0.270021,4.674439,-6.839279,-7.784241,-3.658797,6.326905,-0.670911,-1.301915,0.755190,5.558370,-2.968865,-9.068474,-3.307306,-7.275661,9.649602,-2.421506,6.039330,8.238655,9.694220,-3.991978,-4.889763,-1.914871,-6.136289,8.758689,2.078135,0.203862,0.129660,-1.295955,6.099624,-0.120284,8.609278,-1.386641,-6.030492,-4.093573,9.492838,7.145890,-6.719401,-6.623960,-1.716905,0.867348,-5.632579,0.217236,-9.133944,3.460707,-3.701379,-6.370364,2.980874,-4.974674,-4.316164,1.386434,-7.970752,-3.384384,-1.756328,4.603832,-0.520341,-5.412011,3.094407,7.694787,8.476309,6.554794,-5.720280,-7.643306,-5.717237,7.631175,2.877812,-9.672928,4.919654,8.754762,-5.009781,3.207906,4.602727,7.870922,4.722977,-6.290677,-4.799302,5.486186,4.001432,-6.115505,-6.480353,-2.665865,-6.882106,5.167808,3.062628,2.955574,-6.939960,7.833947,9.642554,-0.665731,3.739785,3.018627,3.732360,-4.983533,-8.593590,-6.008839,-7.162220,9.053677,-8.079836,-2.075980,0.192993,1.556739,-5.814792,5.397761,0.563795,3.825970,-6.155942,-2.899682,6.484183,-2.406437,6.652654,-4.336020,5.458581,-3.440562,4.251119,-2.971383,7.739252,-0.478173,-7.858744,6.884368,8.042943,-6.718651,9.867324,4.928549,3.880634,7.870392,1.782391,-8.517145,3.432763,-8.880874,2.026956,0.698947,-8.259700,2.215301,1.214898,-7.690995,9.443713,-7.828180,-9.258685,7.418213,2.368070,-7.432923,-2.556400,3.289161,-6.620059,-4.630375,-2.144948,-1.968334,8.440612,7.528161,-9.100070,-1.038087,-1.437498,-7.701500,-5.941077,-5.348004,-3.472840,-1.599824,7.885305,-4.862601,5.962142,-4.416150,-9.572835,-0.220660,-0.215788,-7.073421,-5.027951,-2.790258,5.310711,5.888939,-4.566164,9.206705,-1.043634,1.620602,-7.324933,6.196294,5.685805,7.333009,-1.047452,4.256513,-8.819475,3.976990,-2.630242,9.035186,5.497658,-4.567802,3.841344,-4.276810,9.054053,4.747712,-3.624962,-6.369209,-9.387411,9.952698,4.026224,2.647916,1.918237,-3.701411,-6.394796,0.401489,-6.813022,9.611391,-9.226215,-4.009511,-3.726505,7.909241,-5.701343,-5.251608,7.859393,-4.040779,-9.809543,-5.891058,-3.306150,-7.584637,5.366802,-9.451568,8.459039,3.252831,-0.644089,8.836613,6.644321,5.209327,-4.608766,7.591824,3.312706,0.191434,9.256433,6.566741,-7.414337,8.921112,-4.680756,-1.118818,3.598865,1.438870,5.625633,-2.822161,6.160913,-1.691716,2.994470,0.923089,1.865062,0.235015,7.149393,9.521647,-2.520642,0.730982,-9.395586,-1.369777,2.574569,7.217572,-7.721205,9.670824,2.443169,-9.350846,5.615919,-4.377537,-4.979288,-0.591453,-2.355180,7.761630,-0.376934,5.179659,-3.351404,-2.535757,5.733013,-6.676518,-0.762028,8.124425,-2.207615,-7.888265,-9.057950,-7.660341,-3.676293,-8.149784,-4.922836,7.512717,-7.097058,-7.608380,-2.902893,-8.989941,-8.223260,-9.844874,-6.239213,3.265611,7.176207,8.923860,-0.374965,-4.710710,-9.637079,3.224201,-4.903459,3.046383,-1.939159,-4.713791,-9.613403,-2.085802,8.090796,3.831001,2.742987,-5.199424,7.969257,-8.269476,-9.524747,-2.201000,1.078554,6.939815,1.003151,-2.666707,-3.454438,-0.097221,4.734235,-8.412549,4.031860,-2.736224,-6.503182,9.998301,-9.549740,1.130523,-3.156709,6.519530,8.257424,-4.438860,0.929910,-0.996572,7.353370,2.870336,-7.592926,1.116166,4.609398,-4.009176,7.680870,1.482887,6.681231,-2.472956,2.185345,8.584425,-1.530709,6.986101,-1.336792,-0.479533,-2.078678,-5.598233,7.317294,8.559640,1.256569,-9.811033,1.391642,6.497340,-0.871505,7.034147,9.077191,-9.486399,-2.364021,-8.992914,-2.189628,-6.855564,-8.318398,7.052612,-1.142737,-8.723976,-7.143638,-3.091785,7.746081,-4.380764,7.541683,9.902315,-8.782753,8.947376,9.726112,3.328855,-7.441803,-9.213846,-9.270446,-6.317851,-0.075638,-0.956566,4.736030,4.398401,-6.678605,-4.624703,9.609229,1.381282,2.943367,-3.403777,-7.516183,-0.182943,6.895881,8.301373,-9.807962,-2.258093,-2.237739,6.386754,-4.998074,-7.166544,-7.256603,-3.003302,-9.761981,6.219694,-5.606405,-2.317031,4.227092,1.372003,-8.790725,-1.650703,-8.834916,2.250629,-8.800923,-8.794207,3.064782,6.644238,0.397671,1.771468,2.325942,-4.755236,-0.270407,-5.841325,9.167238,-2.465481,-2.848669,1.232355,-4.293281,-6.691419,4.738146,9.846785,3.150920,6.739350,-9.572716,6.741985,3.505257,-8.804743,-7.608503,-7.760717,-7.196642,7.688085,4.623092,-9.129632,-0.846227,-1.108793,9.538245,-8.706518,6.888917,-3.092794,9.701599,8.417600,9.320364,-3.551719,3.127568,2.492605,-1.089561,-4.314235,0.608023,7.372779,4.155201,-2.920362,1.269665,-2.570603,-7.422247,-9.324931,-5.717953,-5.249876,3.760643,8.262008,6.522556,3.567437,-3.783775,-7.857800,-7.692946,3.856935,8.613572,-7.134953,-4.962009,8.549428,2.803943,-6.114123,-6.749361,0.408341,-2.503746,-3.435223,-1.891631,9.458313,0.779226,-6.952362,6.948745,-9.260771,2.797287,4.649869,8.002276,-9.230116,-8.082430,-2.376984,-9.553076,6.318323,-8.745927,-6.656376,9.364212,4.594377,0.541202,-8.139820,6.026535,-4.060153,0.449012,2.394095,-9.938562,-4.119106,-7.383698,1.742385,-0.217263,8.327501,-7.204503,1.893016,0.025110,5.415118,9.573482,6.294559,-2.415393,1.493963,4.368309,-9.353453,8.668723,8.861483,9.577743,-0.563309,9.360935,-7.475410,7.307026,0.593107,6.291091,-4.702651,-0.422344,4.862719,8.809056,-4.274519,9.284727,-9.481534,1.194351,0.341402,3.538574,6.821528,4.449942,-7.842357,9.728758,-3.530273,-8.957619,5.663173,-0.844547,2.611270,-0.874842,8.674887,-4.379626,-1.390188,1.452521,-0.036809,7.850114,8.233224,-3.715040,9.125713,1.807326,-3.191094,-4.335082,-3.160082,-0.077963,-9.488955,7.381578,2.079835,-1.477908,-0.905288,3.199099,-4.642153,-9.648407,2.926079,7.400039,-6.283387,-8.154071,6.788145,9.383123,-4.882366,2.101462,-2.411204,-9.597900,2.181066,7.460536,-2.269486,-5.784703,6.763302,-6.929035,3.513790,5.241851,-8.840561,-1.211364,2.762735,9.240142,-4.499151,-0.098196,2.437931,-0.127654,9.245408,-4.969857,-3.430237,-8.606877,8.439770,-6.775807,0.331426,5.028342,-6.976146,8.968656,5.281376,2.733489,0.996582,-2.245468,-0.160084,2.837504,-0.152595,0.272462,2.900051,-1.113213,-9.429812,6.089363,-7.916506,6.295168,4.427492,-8.274860,8.303497,-5.847410,-4.297016,1.405437,4.636838,-2.539501,9.003078,-7.476960,-0.080732,9.988983,1.721974,-2.119585,9.597327,-5.260537,-3.502532,4.224485,-3.882375,-0.233550,-0.279284,6.336397,1.315686,2.187011,9.169345,7.533014,-6.233648,-2.624186,1.436049,-0.685485,-0.178564,5.813672,7.469902,-7.007486,-3.863829,-9.878249,7.756993,-6.023233,-6.795965,2.996066,2.071421,1.444970,6.123194,-4.964526,-4.457535,-2.864548,1.624092,7.368622,-8.595405,6.599322,-4.516607,-1.074853,9.419970,-8.961063,-4.805168,-7.831289,-4.860160,-2.891839,8.910677,5.889926,6.361675,7.280855,4.211113,6.597977,-3.114040,5.721781,6.377846,-8.469748,-5.731272,-0.658398,-4.041771,3.422121,-0.359884,2.617886,-6.343420,7.737670,-2.235810,-9.301115,6.389848,6.683877,-1.035245,-3.169942,-6.095439,0.044111,-8.382574,-0.325257,-4.129718,3.876435,9.249090,-8.254845,7.943961,2.084933,-6.606347,-4.000835,8.216953,-7.317986,-5.959580,9.435553,6.848702,9.786270,-4.435711,3.739751,1.122734,8.211341,5.312023,-0.917135,3.022939,-0.284133,-3.366340,8.369264,-0.865047,8.738860,4.022647,-1.617518,7.678986,-3.049497,2.280395,-4.206883,-1.487534,7.766055,-6.922400,7.757292,4.904254,8.655426,-0.012983,4.407441,-5.346279,7.163072,-6.003678,6.152941,1.068187,4.468980,1.759300,-5.222494,-4.658160,3.128779,9.379554,-5.112896,-0.128150,-1.281215,4.624604,2.493277,0.450527,8.413715,-7.642371,3.414935,-7.659269,-2.998957,9.339672,7.729712,-7.044340,-7.339230,8.313487,-2.026876,-0.263571,-7.670807,0.135644,-8.859758,-2.575496,-6.979255,-7.737679,2.471619,-7.793771,-9.643862,-2.182991,2.645822,-3.522930,-9.179371,8.867433,9.198078,-2.263585,7.476526,6.831246,-6.709644,4.228902,8.343791,-6.122416,-3.561886,-8.389494,-7.421687,-1.491985,-0.032058,4.211055,3.172333,2.729527,3.210389,-9.482173,2.627015,-9.267420,-2.830331,-6.998733,2.723412,-7.608077,-4.208923,-4.945376,1.097470,-5.523314,7.937740,-4.776534,-6.817551,4.819891,6.424471,-1.413129,9.259757,-1.635412,-5.639659,1.503600,-8.904549,0.603259,5.601330,6.024266,3.323123,-3.870725,-1.252542,9.520428,-9.278487,-5.987824,-1.151746,9.331776,8.626309,8.457692,-3.067361,6.095780,-8.155237,1.580360,-5.677142,-8.425405,0.906240,-1.739114,-8.368676,-9.026147,-5.529061,-3.764995,-6.726537,-1.445952,-2.983077,8.356799,0.867165,0.114266,-2.328437,0.533865,3.709547,-7.795598,-9.608693,-9.564807,-1.988320,6.436631,0.474257,1.028983,2.318465,5.419264,-9.140761,5.070422,0.540847,3.842837,4.503252,-2.334118,8.332482,4.168657,0.325157,-1.240162,2.723044,-5.355625,7.373165,-4.760148,-8.310433,-1.717523,-1.491563,-5.159702,-3.589761,9.238467,-7.648355,3.256330,-7.508006,9.669776,-5.642128,2.416059,1.241702,6.153058,-9.850522,-7.928613,1.404797,7.697238,-3.191286,-9.648439,6.946958,-9.015025,1.807066,1.418847,6.136523,-9.381600,-0.313262,1.017177,4.061336,2.798474,-4.595131,-1.465814,-1.234344,9.241449,7.472154,-9.374949,-3.383114,-0.938911,-5.835949,1.436605,-1.537482,6.935968,-9.900537,3.596230,3.562411,0.442040,-8.382112,-2.089106,1.437779,5.265056,5.686662,8.045881,-5.435501,0.687392,-3.104801,-3.383565,-2.309855,9.462674,-8.891003,2.753246,4.868669,0.953639,-9.087809,8.693912,-4.559786,9.531606,-1.942501,4.969536,-8.319747,9.857824,3.024177,-5.418686,2.249895,-3.646699,-3.068552,-0.316874,-5.963731,6.840317,0.210331,-4.998260,9.897426,8.790057,7.037003,-8.544254,9.624921,-8.730676,-5.938411,5.045978,-3.610331,0.227687,9.726123,9.979201,-8.924389,-6.452298,3.925822,4.743426,-6.060425,-6.059137,5.671378,-8.620294,-6.705795,7.416503,4.066088,-6.277888,1.891582,-7.162863,6.876940,-6.828829,-6.033226,0.157155,-4.619741,-2.753964,8.275430,-7.174892,2.206690,-6.115162,8.447365,-9.165286,-8.207012,-0.005047,9.987374,-3.298980,-3.711580,-4.951415,1.419624,-1.955356,-8.975726,3.048399,1.146749,-5.243833,-5.560890,-9.817416,-4.251257,-7.738565,-5.459949,-6.262167,2.157286,-6.191344,-5.051254,-9.814874,4.596325,5.206985,9.458351,8.002888,-4.780335,9.621551,-4.520495,-2.579595,7.743916,5.513597,2.031314,9.937411,-5.786807,5.718504,-7.669961,3.696830,-0.919186,1.687588,8.359863,2.772781,-1.020596,-3.333334,-0.332008,9.872091,0.763012,5.276219,3.582994,7.705299,5.727062,-0.146267,-1.763766,6.062250,-0.988029,-2.360050,6.749362,8.278882,-0.695999,4.584857,-0.001258,-5.010171,1.210105,-4.144212,-2.070424,5.996020,-0.489698,8.692253,0.986806,-9.042897,7.675120,3.630262,-7.507046,-1.586526,-8.931405,2.292460,7.273730,-4.661967,-2.409597,1.123153,-3.081134,-1.727963,-6.203974,4.002443,-6.464579,5.245213,-2.442851,-7.040308,3.621339,4.264866,-2.744415,-7.151342,6.281665,8.648661,4.670822,-6.616361,7.547859,6.218837,6.067311,8.064099,-9.547163,0.627163,0.346380,6.661256,8.746961,-9.086444,9.956562,6.690022,1.470427,-8.811016,6.371503,-0.608348,3.761233,-8.087205,-8.619355,-2.082053,-5.876452,5.235768,-6.835916,-0.897004,8.347158,2.847628,5.150452,5.157968,5.175995,5.664934,5.698745,6.469101,2.808603,6.231594,1.884805,-8.620947,4.206950,9.701500,-2.806445,0.403624,-3.612720,8.236888,6.713275,-7.454671,-7.739645,5.294961,9.480334,2.412474,-5.942710,-6.051070,-8.147209,8.780344,-9.118113,3.831611,-6.801893,3.472191,-9.152468,-3.126150,9.283745,-0.512243,5.434100,5.175048,4.243964,2.539974,2.271109,0.919312,5.351167,-4.079427,-4.425043,-3.597876,-5.261381,6.233378,-5.549293,3.202005,7.686432,-0.911207,0.673203,0.428105,-0.459988,7.921211,7.001157,4.316159,8.253632,-9.925098,-6.993646,2.292688,-6.633124,8.854894,-2.550721,2.491079,-3.827567,-9.092491,9.371157,-0.819489,4.546598,-0.833589,0.126716,8.245811,6.709483,-6.656516,-7.343773,-5.849254,-6.514236,-1.111912,-5.953981,-0.708842,0.024495,8.799257,5.954434,-1.505083,1.921502,2.218584,-8.403816,8.354441,-9.052461,9.732751,6.059009,-1.743866,5.776015,2.570502,-8.991524,1.651670,-8.415258,-2.654644,-1.821869,-5.018483,7.479646,-3.375300,-0.838176,6.770695,5.704480,-2.172782,5.915648,4.147829,0.276442,-9.121027,-8.645581,4.715751,-6.958306,-0.269503,-2.662626,-1.736823,-8.124305,1.902502,2.792436,-4.097393,-2.404138,9.755850,8.906677,-7.300020,0.632265,-0.346988,-6.555331,8.616276,3.065376,-6.797320,-0.817771,-5.485252,2.000712,-9.842577,-2.878473,-5.653624,3.534827,-6.653551,-1.295767,9.077303,-3.597749,6.392451,8.733355,3.503153,6.077339,-4.061376,6.239217,-9.112641,-2.594903,6.828458,9.436989,5.130014,2.114484,2.863283,7.172012,-8.490640,-1.168655,-3.333752,-7.719135,0.309566,8.540921,6.983335,-8.113832,-7.451028,-3.835122,2.880070,6.873736,-5.611280,5.554792,-2.967881,-3.078108,-8.138622,-2.153995,-8.848854,-0.749725,-6.230123,6.539621,-9.125561,-7.499300,8.810655,-7.696038,-9.461056,7.389093,3.593420,1.940429,2.199993,-3.189988,-3.952105,9.590725,2.142401,-3.948972,4.660702,9.669274,4.919509,-2.955218,2.549159,-4.611518,-5.264939,-3.991192,-8.557996,0.808265,-6.671110,9.689121,8.698817,8.697002,-5.023909,-7.245345,-2.865401,-2.612876,7.868130,-2.989196,9.346246,8.520697,-0.247671,0.534891,4.360342,7.470979,-2.205160,-5.527836,4.967329,-7.633341,-0.620932,1.090680,4.650846,-7.968358,5.261787,4.914483,2.642831,-2.794443,-4.636227,-4.185516,8.732988,0.861317,-1.255151,5.186643,-9.625458,-8.003466,-3.801768,6.733882,8.343571,4.255346,-8.583424,8.521293,7.617619,4.765685,-3.230621,4.720015,2.243653,8.110527,-2.659208,3.054842,5.008240,3.506577,-8.413740,2.873419,0.835743,-1.629001,7.540376,8.963191,4.712315,-1.653423,9.086356,7.922340,7.602645,-3.181471,2.097817,-3.716297,2.265029,6.096405,-5.472292,0.476372,3.526199,0.024438,-7.768653,0.725380,3.992015,8.583897,7.790339,-8.380204,8.741680,-0.553935,-8.947449,8.751381,1.609637,1.270802,3.368796,6.626118,-7.016475,8.831388,6.995874,6.711253,1.905967,1.354332,7.761468,7.243220,8.012183,-5.331505,-1.266687,2.324636,-7.253490,9.460061,-4.346059,-6.236317,3.359735,3.459854,-1.474247,2.386325,6.476821,-3.501501,-7.058173,9.021742,3.602807,-8.644564,-3.337820,3.360040,-3.055710,-7.183151,9.665118,-0.730611,7.095356,-5.094166,-4.768228,1.841986,-6.683541,-0.009059,0.709223,-1.492979,2.668978,-9.385186,9.586979,-4.977096,-8.503861,-4.905481,0.261636,-5.329707,-8.107698,-3.258159,-0.648199,-1.600213,4.707110,-9.262361,-1.337686,-4.834452,0.852934,8.994054,-8.698735,-1.623221,0.898977,4.114354,5.454621,9.964389,-3.547967,-8.230399,1.054921,3.102038,-8.403862,2.568998,9.864111,-6.822082,-9.600340,7.571062,-9.858724,8.829296,-2.763151,-0.873764,-8.961152,2.533095,-5.369451,7.091004,-3.336849,-2.701287,-7.273819,5.792221,8.308172,-0.635228,-5.187906,7.872832,-6.046152,-6.687962,2.382912,-4.824409,-6.889936,-1.083271,-4.910986,-6.432925,-8.155552,7.638286,-8.952393,-6.220587,-5.943879,3.698244,-4.786850,1.618641,6.159678,2.155521,8.413607,-6.170249,6.438837,-3.363936,-6.187182,-7.522319,6.303083,-9.335311,3.349138,-4.639434,0.876600,-9.961899,-5.737216,-2.255096,1.700790,-0.658974,-8.683983,-3.365959,1.902713,5.671195,7.801918,-2.615603,3.154248,-0.823566,-9.940882,-3.432962,-3.337038,2.989725,5.326442,-6.184683,-7.518622,3.263572,0.473593,-2.668659,-9.592040,-6.877998,-7.349786,-2.536363,0.170447,-1.020846,5.224639,-3.545471,3.423731,-3.714198,2.981471,3.090344,1.359409,-7.140591,-5.558735,2.889845,-5.837421,-8.147587,3.708535,-7.751485,1.743031,-1.056385,-0.048118,-1.409157,-5.210818,-2.335671,9.621937,2.491122,-4.444545,2.877122,6.027859,7.068194,-4.599893,-3.362261,-8.924661,8.725385,2.468391,4.802033,-3.753900,9.268293,-4.970755,-8.222288,7.283620,3.446763,-3.150614,-3.709541,7.494536,9.365648,8.817650,9.933639,2.891173,7.084549,-3.786039,-5.582555,-0.147575,-9.599888,2.007403,-3.876416,-4.309097,-0.878035,-1.793184,-8.013151,-0.393172,3.324885,1.167829,6.930795,4.354035,1.453178,9.339249,-7.817872,7.840453,6.764172,-1.274503,4.749743,4.308528,6.737240,-6.296472,7.470867,9.268705,-7.713289,-5.657380,6.630487,-5.566437,2.521816,-2.711415,9.814116,-7.609162,-5.576387,-1.839444,-7.322254,2.136781,5.531413,6.815986,-4.726591,-2.184823,-0.830967,1.050771,-3.228732,-9.503401,4.729033,-1.001137,8.890741,1.001694,0.619263,0.586520,3.601861,9.271530,7.686392,-4.854109,8.151812,-7.579201,7.505664,-8.314511,-5.058507,7.135402,4.124356,-9.398550,0.401090,4.080721,-7.307646,-0.626784,9.738112,-6.035113,-9.166229,9.235690,4.747319,0.108008,9.133305,3.385703,4.262807,0.833932,-8.165191,9.201339,-1.713739,-8.053580,7.452430,-9.665715,-0.429866,9.633647,4.614286,-2.287964,4.404392,1.349845,9.794485,-0.644010,-2.589754,-3.005473,7.482002,-1.696715,-5.631009,-4.925173,0.687937,-7.204147,-0.796565,-9.675492,-3.646120,-8.583283,4.434111,-2.657093,-4.613694,9.245958,0.092265,5.654436,6.432058,-5.312201,-6.744366,7.357055,9.993870,0.239513,-3.751174,-9.596360,9.810648,-6.138317,-7.073778,9.497265,6.455543,1.128785,-8.242407,8.662972,-6.693757,8.748561,2.049816,-8.084723,5.027184,-8.614320,-3.944137,-7.549425], dtype = "float64")#candidate|3735|(2640,)|const|float64
call_3734 = relay.TupleGetItem(func_1880_call(relay.reshape(const_3735.astype('float64'), [2640,])), 1)
call_3736 = relay.TupleGetItem(func_1883_call(relay.reshape(const_3735.astype('float64'), [2640,])), 1)
uop_3776 = relay.rsqrt(const_3735.astype('float32')) # shape=(2640,)
uop_3778 = relay.cos(uop_3776.astype('float64')) # shape=(2640,)
bop_3792 = relay.maximum(const_3735.astype('float64'), relay.reshape(uop_3776.astype('float64'), relay.shape_of(const_3735))) # shape=(2640,)
func_1330_call = mod.get_global_var('func_1330')
func_1334_call = mutated_mod.get_global_var('func_1334')
var_3796 = relay.var("var_3796", dtype = "uint64", shape = (441, 1))#candidate|3796|(441, 1)|var|uint64
var_3797 = relay.var("var_3797", dtype = "float32", shape = (1680,))#candidate|3797|(1680,)|var|float32
call_3795 = relay.TupleGetItem(func_1330_call(relay.reshape(var_3796.astype('uint64'), [7, 7, 9]), relay.reshape(var_3796.astype('uint64'), [7, 7, 9]), relay.reshape(var_3797.astype('float32'), [840, 2]), ), 1)
call_3798 = relay.TupleGetItem(func_1334_call(relay.reshape(var_3796.astype('uint64'), [7, 7, 9]), relay.reshape(var_3796.astype('uint64'), [7, 7, 9]), relay.reshape(var_3797.astype('float32'), [840, 2]), ), 1)
output = relay.Tuple([call_3732,call_3734,uop_3778,bop_3792,call_3795,var_3796,var_3797,])
output2 = relay.Tuple([call_3733,call_3736,uop_3778,bop_3792,call_3798,var_3796,var_3797,])
func_3801 = relay.Function([var_3796,var_3797,], output)
mod['func_3801'] = func_3801
mod = relay.transform.InferType()(mod)
mutated_mod['func_3801'] = func_3801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3801_call = mutated_mod.get_global_var('func_3801')
var_3803 = relay.var("var_3803", dtype = "uint64", shape = (441, 1))#candidate|3803|(441, 1)|var|uint64
var_3804 = relay.var("var_3804", dtype = "float32", shape = (1680,))#candidate|3804|(1680,)|var|float32
call_3802 = func_3801_call(var_3803,var_3804,)
output = call_3802
func_3805 = relay.Function([var_3803,var_3804,], output)
mutated_mod['func_3805'] = func_3805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2277_call = mod.get_global_var('func_2277')
func_2279_call = mutated_mod.get_global_var('func_2279')
call_3827 = relay.TupleGetItem(func_2277_call(), 0)
call_3828 = relay.TupleGetItem(func_2279_call(), 0)
var_3831 = relay.var("var_3831", dtype = "float64", shape = (33,))#candidate|3831|(33,)|var|float64
bop_3832 = relay.multiply(call_3827.astype('int16'), relay.reshape(var_3831.astype('int16'), relay.shape_of(call_3827))) # shape=(33,)
bop_3835 = relay.multiply(call_3828.astype('int16'), relay.reshape(var_3831.astype('int16'), relay.shape_of(call_3828))) # shape=(33,)
func_1999_call = mod.get_global_var('func_1999')
func_2000_call = mutated_mod.get_global_var('func_2000')
call_3836 = relay.TupleGetItem(func_1999_call(), 0)
call_3837 = relay.TupleGetItem(func_2000_call(), 0)
bop_3844 = relay.mod(bop_3832.astype('float64'), relay.reshape(var_3831.astype('float64'), relay.shape_of(bop_3832))) # shape=(33,)
bop_3847 = relay.mod(bop_3835.astype('float64'), relay.reshape(var_3831.astype('float64'), relay.shape_of(bop_3835))) # shape=(33,)
func_2824_call = mod.get_global_var('func_2824')
func_2825_call = mutated_mod.get_global_var('func_2825')
call_3858 = relay.TupleGetItem(func_2824_call(), 2)
call_3859 = relay.TupleGetItem(func_2825_call(), 2)
output = relay.Tuple([call_3836,bop_3844,call_3858,])
output2 = relay.Tuple([call_3837,bop_3847,call_3859,])
func_3861 = relay.Function([var_3831,], output)
mod['func_3861'] = func_3861
mod = relay.transform.InferType()(mod)
mutated_mod['func_3861'] = func_3861
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3862 = relay.var("var_3862", dtype = "float64", shape = (33,))#candidate|3862|(33,)|var|float64
func_3861_call = mutated_mod.get_global_var('func_3861')
call_3863 = func_3861_call(var_3862)
output = call_3863
func_3864 = relay.Function([var_3862], output)
mutated_mod['func_3864'] = func_3864
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3936 = relay.var("var_3936", dtype = "uint8", shape = (16, 7, 3))#candidate|3936|(16, 7, 3)|var|uint8
var_3937 = relay.var("var_3937", dtype = "uint8", shape = (16, 7, 3))#candidate|3937|(16, 7, 3)|var|uint8
bop_3938 = relay.bitwise_xor(var_3936.astype('uint8'), relay.reshape(var_3937.astype('uint8'), relay.shape_of(var_3936))) # shape=(16, 7, 3)
uop_3951 = relay.cosh(var_3936.astype('float64')) # shape=(16, 7, 3)
output = relay.Tuple([bop_3938,uop_3951,])
output2 = relay.Tuple([bop_3938,uop_3951,])
func_3965 = relay.Function([var_3936,var_3937,], output)
mod['func_3965'] = func_3965
mod = relay.transform.InferType()(mod)
var_3966 = relay.var("var_3966", dtype = "uint8", shape = (16, 7, 3))#candidate|3966|(16, 7, 3)|var|uint8
var_3967 = relay.var("var_3967", dtype = "uint8", shape = (16, 7, 3))#candidate|3967|(16, 7, 3)|var|uint8
output = func_3965(var_3966,var_3967,)
func_3968 = relay.Function([var_3966,var_3967,], output)
mutated_mod['func_3968'] = func_3968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2277_call = mod.get_global_var('func_2277')
func_2279_call = mutated_mod.get_global_var('func_2279')
call_3994 = relay.TupleGetItem(func_2277_call(), 2)
call_3995 = relay.TupleGetItem(func_2279_call(), 2)
output = relay.Tuple([call_3994,])
output2 = relay.Tuple([call_3995,])
func_4021 = relay.Function([], output)
mod['func_4021'] = func_4021
mod = relay.transform.InferType()(mod)
output = func_4021()
func_4022 = relay.Function([], output)
mutated_mod['func_4022'] = func_4022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1074_call = mod.get_global_var('func_1074')
func_1075_call = mutated_mod.get_global_var('func_1075')
call_4028 = func_1074_call()
call_4029 = func_1074_call()
const_4032 = relay.const([4.152830,5.246442,-2.394423,2.137387,-5.888652,-9.362898,-3.082489,-1.653907,-8.249193,7.647449,3.850391,-1.849680,-2.374305,9.957893,4.161450,-5.280374,9.777462,3.756009,5.072227,-2.225623,-4.210290,-7.294165,6.009355,-3.955339,9.904837,2.421185,8.126930,-7.153109,-3.371020,-0.801623,-5.684913,-5.508546,4.260366,6.959608,-7.188436,-6.898522,9.664016,8.023860,2.602145,-6.429180,4.545966,8.344355,-5.008503,-1.491573,-4.318867,-2.762010,-6.038688,-6.321935,-3.884185,-5.280566,5.768088,-3.240188,4.533218,-4.697500,0.533563,-1.223132,-8.124310,8.014510,6.972313,-7.690451,-8.237136,-6.347291,1.094524,-5.962186,-3.908318,5.130191,8.620323,-5.825801,3.052103,-2.369241,-8.411343,-0.571340,-4.943409,2.654661,2.712896,9.447354,-3.802509,-9.645382,-6.404709,-2.497117,4.346292,8.215645,1.006577,-0.015742,-2.845597,7.301465,9.417655,8.331949,9.809326,9.058461,-4.809454,-2.610138,-5.926524,6.750703,-5.960223,0.649617,6.990448,-7.875188,5.640885,4.386451,0.433607,-6.711113,-4.486386,0.707111,-3.436468,4.279012,9.806068,0.314123,-1.926446,4.409169,-4.913466,1.144519,2.196364,-9.649732,-2.387360,-1.783638,-3.805281,-6.069639,-0.417730,-8.420780,-5.513737,-6.780119,-1.063988,2.801326,-9.392581,5.262144,1.856629,-9.319360,-9.237530,2.811246,-8.895586,4.726700,-9.121964,-6.400067,0.512719,9.648542,-0.166638,7.976185,-4.915244,3.210863,0.709161,0.636115,1.766789,4.134426,2.668855,-5.723229,-8.444827,-8.914543,9.823296,-7.903546,-9.981810,-8.006238,4.245094,2.063681,-2.035673,-3.632547,1.666078,5.217924,3.110847,-9.752270,7.285195,-7.511753,-2.074583,6.479260,9.858931,-3.408402,7.557308,-5.797363,3.863468,-8.141639,2.903300,0.887532,6.160150,6.358139,-3.718941,3.109777,8.394551,4.131716,-8.371326,4.201759,-4.400204,7.952904,0.861313,-2.792809,6.758448,-6.911791,9.018178,4.683714,-8.612196,5.120594,2.487989,9.564430,8.562291,-5.554345,5.989715,9.287051,-3.192392,6.687849,5.840592,-1.687192,9.084923,3.897968,-0.029283,6.027626,4.254884,7.663219,0.762582,5.672840,-7.532080,-2.667637,-3.806858,4.306045,1.849166,-9.351133,2.682625,7.675253,1.855664,8.237734,-6.943445,2.193944,-5.021188,-6.125482,8.185830,-1.933416,8.854554,2.498269,-1.453820,-9.511998,8.447871,-6.537206,5.109639,7.206831,-1.885695,7.442946,0.653404,9.436778,6.915543,3.440903,9.815648,-5.383726,6.480720,-1.974158,0.665484,4.141771,7.591058,4.211354,7.871196,-6.167083,2.819001,-0.836064,-3.716929,-9.028905,1.264884,-5.193994,1.780940,-1.185881,-0.932497,0.802679,1.712204,-6.689479,-3.827491,-6.641378,0.969571,-3.481323,-6.718020,7.312249,-6.154729,-7.645958,-9.594354,-4.028035,-5.786213,-9.686460,-8.240727,-8.935556,-1.559187,-6.217649,-4.964234,-4.242391,5.961818,-0.466524,-7.651709,-7.307555,-4.301073,-9.260795,5.671549,-7.481367,9.273355,-6.086578,-5.121417,-5.878847,-2.131131,-3.407653,4.753803,-9.429729,1.577490,-4.058166,-3.576357,-5.904318,5.363390,0.613616,8.519809,-7.416032,-8.240397,-4.056539,5.217603,2.612516,-7.207799,-2.526345,2.469209,-5.637249,-5.731024,-0.319639,-9.023274,6.623856,7.118500,-9.720774,-2.853015,-0.124414,-3.767052,-6.896706,2.746938,6.077071,8.711930,5.155659,-5.906001,3.809546,-0.520110,5.349748,-0.224646,-4.240795,-9.176998,-0.310932,-2.290093,2.456302,-3.198513,-7.985661,-8.669067,7.793598,-1.076949,-6.807376,-4.587591,7.301824,6.290727,7.508929,3.341731,2.047503,7.674153,-1.253427,-7.417154,-4.358921,5.084775,-1.885850,-7.189361,8.498850,-5.180422,8.674589,8.762308,3.460608,1.199135,-0.069607,4.923949,-4.378846,-6.071701,-8.895973,3.743059,2.561831,9.262508,-0.780724,7.786605,-4.433438,6.241938,-6.158818,-1.678862,1.953063,5.542732,-2.178442,5.220877,3.681702,-8.356982,8.497965,-3.158730,-3.311107,-5.608308,6.233040,4.981778,-3.735682,2.368454,3.629222,-8.984166,2.159544,7.727044,-0.563990,2.269966,-9.018598,2.950090,1.117264,-0.466890,-6.765895,-8.067112,-8.741442,6.552973,-0.868806,5.759011,5.436711,-8.763715,6.686364,-1.276919,-8.939353,8.954073,9.469527,-9.777522,-5.638349,6.442179,-6.368774,-1.845105,4.194188,9.845545,-1.243359,3.252735,-7.788060,4.145749,7.380513,-3.566791,7.404729,-7.310101,-9.782717,6.271146,3.615626,4.964829,-0.325930,-4.225765,-8.283639,0.688480,4.921785,-5.570077,-3.485739,4.539281,0.036441,2.821608,-4.816157,-9.956649,5.648521,0.154047,-0.096313,-6.021706,1.932205,-6.650809,-7.620098,-4.562107,-2.709825,0.014508,-3.925518,4.362746,-4.343993,-4.608278,-6.544532,-2.545692,-1.677774,1.024664,-7.968925,8.517021,-0.787662,4.067615,0.578083,-7.665847,-8.803622,-0.467486,5.407239,0.962276,5.912581,-6.109440,-6.677834,3.624699,-1.754313,0.446313,-3.233343,-5.548222,-8.715139,9.312567,-0.224490,8.525703,7.256349,7.318139,5.852298,2.757285,8.027492,3.442112,-6.742133,-0.169355,3.670534,6.087548,4.101571,-8.354878,-8.698749,6.088522,-9.313510,8.732737,4.848967,-0.797760,8.837212,1.153092,7.645679,-5.855006,9.872387,-4.757015,-6.503603,-2.378192,-3.690041,3.602824,-3.894455,3.869830,-9.313587,-9.234707,9.485114,-0.792104,-7.145222,5.360332,-1.277327,0.471240,5.498584,-8.695426,-7.834766,6.771651,-4.489089,6.659720,2.415221,9.287868,3.032782], dtype = "float32")#candidate|4032|(528,)|const|float32
bop_4033 = relay.multiply(call_4028.astype('uint8'), relay.reshape(const_4032.astype('uint8'), relay.shape_of(call_4028))) # shape=(528,)
bop_4036 = relay.multiply(call_4029.astype('uint8'), relay.reshape(const_4032.astype('uint8'), relay.shape_of(call_4029))) # shape=(528,)
func_2277_call = mod.get_global_var('func_2277')
func_2279_call = mutated_mod.get_global_var('func_2279')
call_4040 = relay.TupleGetItem(func_2277_call(), 0)
call_4041 = relay.TupleGetItem(func_2279_call(), 0)
func_2131_call = mod.get_global_var('func_2131')
func_2133_call = mutated_mod.get_global_var('func_2133')
call_4043 = relay.TupleGetItem(func_2131_call(), 1)
call_4044 = relay.TupleGetItem(func_2133_call(), 1)
func_774_call = mod.get_global_var('func_774')
func_778_call = mutated_mod.get_global_var('func_778')
const_4054 = relay.const([-1,8,3,10,7,8,-8,-2,-4,-1,-1,1,-4,6,-3,2,-10,-10,8,-3,-5,-6,9,-8,-6,-4,-1,7,-9,-5,4,6,10,10,-5,2,5,-3,-7,-9,-9,-9,7,-8,-1,-9,-10,2,1,7,-5,6,-6,-6,1,7,-8,10,4,-2,-1,-9,-5,1,3,4,7,-9,2,-8,-3,-2,-1,4,10,-8,8,4,-10,-1,-2,-10,6,2,9,10,-4,10,-3,-9,-2,-8,8,-6,-8,1,4,9,-3,10,2,3,-10,-1,7,10,1,-4,1,-5,-8,10,-10,-4,1,-6,-3,1,1,-8,4,-2,7,1,-5,-6,-5,-5,-5,-9,-2,-9,3,8,-2,4,6,10,-9,9,7,7,2,-8,-2,3,-3,10,-4,10,7,-3,-10,-6,4,-5,5,-5,-3,-3,-10,-10,1,-9,-8,-3,4,10,9,-5,5,3,9,6,1,-8,8,-3,7,7,2,-2,8,-2,-2,-1,4,-7,-2,-8,6,3,5,-4,8,8,3,-8,-6,1,7,6,-4,8,-8,8,-2,10,6,10,7,-6,1,-5,-4,6,-6,3,-5,-5,-7,1,-5,9,-4,5,-8,-4,-5,-8,3,8,-6,9,-2,-8,-9,-8,-7,6,-7,-3,-2,-6,5,-5,7,10,-4,5,-5,-7,-10,-1,-2,-8,-7,-4,9,-5,-3,3,-4,1,1,-6,-9,-3,7,-7,10,-10,10,8,-3,2,-5,-5,-9,7,-2,-8,-7,3,-6,3,-10,5,-6,-7,-7,-4,-5,9,5,6,2,-2,5,-1,8,7,8,5,-4,-2,3,-1,-6,4,10,-1,-4,-1,8,9,7,-1,-7,-6,9,2,-5,2,-7], dtype = "uint8")#candidate|4054|(325,)|const|uint8
call_4053 = relay.TupleGetItem(func_774_call(relay.reshape(const_4054.astype('uint8'), [5, 13, 5]), relay.reshape(const_4054.astype('uint8'), [5, 13, 5]), ), 0)
call_4055 = relay.TupleGetItem(func_778_call(relay.reshape(const_4054.astype('uint8'), [5, 13, 5]), relay.reshape(const_4054.astype('uint8'), [5, 13, 5]), ), 0)
uop_4061 = relay.acos(call_4040.astype('float64')) # shape=(33,)
uop_4063 = relay.acos(call_4041.astype('float64')) # shape=(33,)
bop_4066 = relay.left_shift(uop_4061.astype('uint16'), relay.reshape(call_4040.astype('uint16'), relay.shape_of(uop_4061))) # shape=(33,)
bop_4069 = relay.left_shift(uop_4063.astype('uint16'), relay.reshape(call_4041.astype('uint16'), relay.shape_of(uop_4063))) # shape=(33,)
output = relay.Tuple([bop_4033,call_4043,call_4053,const_4054,bop_4066,])
output2 = relay.Tuple([bop_4036,call_4044,call_4055,const_4054,bop_4069,])
func_4072 = relay.Function([], output)
mod['func_4072'] = func_4072
mod = relay.transform.InferType()(mod)
output = func_4072()
func_4073 = relay.Function([], output)
mutated_mod['func_4073'] = func_4073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mod.get_global_var('func_2824')
func_2825_call = mutated_mod.get_global_var('func_2825')
call_4085 = relay.TupleGetItem(func_2824_call(), 2)
call_4086 = relay.TupleGetItem(func_2825_call(), 2)
func_898_call = mod.get_global_var('func_898')
func_901_call = mutated_mod.get_global_var('func_901')
call_4091 = relay.TupleGetItem(func_898_call(relay.reshape(call_4085.astype('float32'), [10, 14, 12])), 0)
call_4092 = relay.TupleGetItem(func_901_call(relay.reshape(call_4085.astype('float32'), [10, 14, 12])), 0)
func_2824_call = mod.get_global_var('func_2824')
func_2825_call = mutated_mod.get_global_var('func_2825')
call_4094 = relay.TupleGetItem(func_2824_call(), 0)
call_4095 = relay.TupleGetItem(func_2825_call(), 0)
func_3861_call = mod.get_global_var('func_3861')
func_3864_call = mutated_mod.get_global_var('func_3864')
call_4096 = relay.TupleGetItem(func_3861_call(relay.reshape(call_4094.astype('float64'), [33,])), 2)
call_4097 = relay.TupleGetItem(func_3864_call(relay.reshape(call_4094.astype('float64'), [33,])), 2)
bop_4102 = relay.left_shift(call_4085.astype('uint32'), relay.reshape(call_4096.astype('uint32'), relay.shape_of(call_4085))) # shape=(1680,)
bop_4105 = relay.left_shift(call_4086.astype('uint32'), relay.reshape(call_4097.astype('uint32'), relay.shape_of(call_4086))) # shape=(1680,)
output = relay.Tuple([call_4091,call_4094,bop_4102,])
output2 = relay.Tuple([call_4092,call_4095,bop_4105,])
func_4106 = relay.Function([], output)
mod['func_4106'] = func_4106
mod = relay.transform.InferType()(mod)
output = func_4106()
func_4107 = relay.Function([], output)
mutated_mod['func_4107'] = func_4107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3638_call = mod.get_global_var('func_3638')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_4112 = relay.TupleGetItem(func_3638_call(), 0)
call_4113 = relay.TupleGetItem(func_3639_call(), 0)
output = call_4112
output2 = call_4113
func_4121 = relay.Function([], output)
mod['func_4121'] = func_4121
mod = relay.transform.InferType()(mod)
output = func_4121()
func_4122 = relay.Function([], output)
mutated_mod['func_4122'] = func_4122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_752_call = mod.get_global_var('func_752')
func_754_call = mutated_mod.get_global_var('func_754')
call_4148 = func_752_call()
call_4149 = func_752_call()
func_4106_call = mod.get_global_var('func_4106')
func_4107_call = mutated_mod.get_global_var('func_4107')
call_4150 = relay.TupleGetItem(func_4106_call(), 1)
call_4151 = relay.TupleGetItem(func_4107_call(), 1)
func_2569_call = mod.get_global_var('func_2569')
func_2570_call = mutated_mod.get_global_var('func_2570')
call_4156 = relay.TupleGetItem(func_2569_call(), 0)
call_4157 = relay.TupleGetItem(func_2570_call(), 0)
func_1486_call = mod.get_global_var('func_1486')
func_1489_call = mutated_mod.get_global_var('func_1489')
const_4176 = relay.const([9.854564,-2.629733,6.011182,-3.354654,-7.239725,4.358172,4.032076,-0.918130,-3.457563,2.128165,9.048817,5.664144,-2.006155,-2.896009,1.430720,-9.137812,-9.551450,-1.225088,-9.297740,7.159251,2.295672,-4.473123,-3.961956,5.391346,-4.681265,-9.639173,5.600331,-9.917058,-3.303842,9.498830,-7.675171,-4.835571,-7.879208,-8.834085,8.897409,-5.911896,-6.419113,4.379057,2.568059,9.689333,2.482394,-3.497022,-4.078444,-0.911105,7.478715,-8.561673,-4.880469,-9.880805,5.497858,5.374274,-0.735959,0.062965,-2.155320,7.059300,-9.017394,-4.324714,-5.301532,-4.987809,8.596464,0.010783,0.759604,5.927089,-9.367782,-0.956934,-4.508100,-9.881334,5.172298,-2.422564,-0.999801,-1.422679,-0.631619,-5.689478,4.364530,9.892773,-0.142022,3.913381,-9.900534,1.141211,8.357888,-9.528454,3.118062,-9.484705,9.388845,-0.115207,6.651328,-2.200888,3.849480,-7.491944,0.944886,-6.773326,7.207960,2.696327,-5.776387,-9.940783,5.774449,1.945939,-2.707844,9.356118,-1.335429,9.326754,-0.529606,-8.589728,0.693750,-2.096011,-7.407240,-6.400060,9.352671,-2.557478,-3.718507,4.204666,0.054075,-2.635659,-3.017003,7.035826,9.926306,-7.982411,-8.026991,-5.978961,-0.022905,1.655471,1.050255,-1.542692,5.145145,-4.518038,9.897367,5.387437,-9.436736,-8.097658,-3.334488,-3.609644,3.997648,7.000196,4.862796,6.936200,0.166869,-1.394478,-7.564339,6.975338,4.821021,1.388764,2.096824,-7.158658,-7.749395,-2.852140,-4.726721,-3.367512,-6.237089,-5.445015,1.216877,4.991183,-4.164978,0.498654,-8.164964,-1.133103,-3.119106,-0.786348,0.465058,-0.460729,-8.024911,-8.936305,1.316305,-6.828738,-6.737988,2.602039,-7.451476,-3.018112,-6.203011,6.122279,-9.741421,8.959761,2.496482,-6.963702,-7.907822,-7.622454,-7.528943,0.103214,2.163546,6.753667,-8.137958,-4.384448,1.300941,8.131494,-7.088568,-7.421841,4.285734,-4.387291,4.908915,3.709562,1.361693,-3.954781,-4.282403,2.993267,8.751983,0.145709,3.644991,-1.395346,4.531779,-1.534960,-0.603472,-8.412138,-4.274689,-4.045757,-4.958024,7.227860,0.960889,1.964494,-8.023548,-5.407579,7.058232,0.619634,8.281592,5.067777,-9.369557,-4.923430,-0.490530,-5.158714,1.581653,-2.084905,-0.245213,3.806908,-8.861890,2.370527,8.064285,-5.093749,8.890072,4.091917,-6.191631,6.711087,0.746297,0.635883,1.572916,-3.859862,7.825865,-0.718675,1.899948,8.548926,-2.097063,-3.008086,-5.013474,-8.080851,-4.560535,-4.328102,-7.140981,1.068696,-3.470137,6.547106,-2.761098,-5.819762,-2.023346,1.702857,8.692042,2.042872,0.396761,1.571886,6.940094,-3.801997,-2.031508,-2.063299,-2.024432,-3.313857,-5.872880,-0.380267,9.738263,-4.067990,3.126712,5.744907,6.205748,-1.775806,-3.488921,-7.311250,5.981456,-5.937973,-1.434833,-5.229805,-0.945639,0.373946,-0.110398,-5.293731,-4.164149,-1.844347,-5.669064,-8.952864,-2.456390,2.569778,9.500184,-3.833872,-2.702909,-7.656840,3.265319,7.077359,7.955090,6.357460,9.725811,0.520141,-4.588662,5.421635,-4.174642,-9.315658,9.088636,0.113319,-4.566286,7.194394,-2.333771,2.894752,5.319149,-1.815720,4.991130,-8.697805,5.947756,-2.263177,9.023583,-6.051398,-5.749376,1.181810,-1.042544,-2.826096,-3.817396,2.591933,4.300548,9.612550,-1.820936,1.054866,6.749881,-6.196612,5.412231,-0.256261,-3.311306,-9.303346,-5.634843,-9.202414,1.116197,2.114537,0.170617,-9.857771,1.055549,7.145848,0.098676,9.168030,-1.708096,1.246656,-4.868898,6.947461,4.555030,7.653925,7.065091,-4.434718,-3.880243,-6.873655,7.831045,-4.628536,-9.951896,-4.364984,-7.579672,-5.041772,1.213602,8.772355,-6.125889,-4.747700,-6.653431,4.069773,-9.108140,-0.446579,8.396991,-4.250005,-5.502593,9.144852,-1.129690,-2.603659,6.556248,1.985103,1.560778,-9.398040,4.760586,8.628799,8.551464,9.905819,-5.413218,-7.563552,1.107165,-1.157722,-7.007510,-0.720385,1.634981,8.819931,-9.190369,5.070895,6.634071,8.832958,9.846941,9.070138,5.011670,-9.157673,-4.705279,7.644493,2.168580,3.773182,4.280374,-1.662787,3.530569,0.726276,-2.300277,4.038073,-1.300984,6.926953,1.150818,-2.812307,8.096528,-8.094791,-4.946142,7.020745,-4.636396,9.340458,9.760152,-2.878415,1.743740,-1.054549,0.410494,-1.959268,-3.134664,2.761491,-2.922938,-6.811185,-1.543168,1.639314,-4.838492,-0.615363,-5.085436,-5.724744,9.427380,-4.457764,-1.612993,-3.038217,-4.130734,4.673294,-2.801986,-3.644764,6.053107,5.068017,4.219185,-9.239722,2.513246,-7.986569,-6.770044,6.035138,-7.455249,-3.787867,-1.739222,-2.214261,1.209014,1.072911,-4.733557,-9.375237,-7.120205,7.115039,9.062263,3.902650,-4.359952,-2.062158,-8.506913,-4.982353,3.762226,0.409328,0.267422,-4.915262,-5.244356,3.654054,6.757419,-6.520601,1.372160,3.590060,8.662706,4.738437,5.138688,-9.780437,-1.591968,-1.190064,1.067004,5.606427,8.624967,-2.052604,-9.082669,-5.460408,7.891438,0.511140,-2.097008,6.863926,-2.275027,5.472599,-7.175054,1.619707,-4.844861,-2.183011,-0.105436,-7.026918,4.344830,4.331900,-1.168218,7.754865,-0.848745,-5.878484,-2.463459,-2.675459,1.154834,-2.020309,9.264250,-1.006030,7.190070,0.449508,-6.998810,5.141885,-1.489785,0.739810,-3.937898,0.186024,-9.084491,5.367905,8.577569,7.121562,5.352309,1.978623,1.021645,-7.420876,-2.699870,-6.741088,5.207123,2.589984,-3.152937,5.574299,8.630970,3.142596,-4.028175,-4.789187,-8.732265,-0.559382,9.562152,-7.636149,4.916661,8.044102,3.241763,8.950041,1.881735,-0.031546,8.297186,-2.735375,-5.643573,-5.200892,-9.121997,5.328033,-7.539542,-1.943834,6.497240,4.545590,1.925541,-7.629228,-3.328640,-9.397976,-3.157066,-3.498560,-2.250984,7.195975,-3.654830,5.690861,-6.167095,-8.232303,9.072273,7.777742,0.729562,0.529468,2.809111,9.397819,0.124862,-4.104796,0.925469,-0.499440,9.318551,-8.150335,8.995449,6.711861,-9.388977,4.940889,-2.559545,-3.769882,1.797030,8.300614,-5.976927,-0.124903,-2.405843,9.587546,2.881689,6.432136,2.659889,6.203808,3.391288,0.397474,-8.079730,3.131503,7.008878,-0.659073,-7.368794,9.162507,0.690333,-1.596802,-5.536345,5.484992,9.286995,7.524756,-4.920376,-7.564080,8.012569,-1.060873,-3.886821,-3.451618,0.443055,-0.750866,-3.149114,-5.225395,9.495334,9.111591,4.945369,-5.847301,5.197266,3.558575,-2.853995,-0.975836,7.877824,6.127226,-8.783299,5.582236,-8.280877,7.857788,-9.572485,-5.625514,0.336259,8.543107,-5.748516,0.926822,9.838240,-9.758135,-9.008726,4.369408,9.862883,6.538283,4.115697,9.547526,-3.756706,-9.722368,8.830960,8.039992,0.146693,1.749663,-8.812738,0.491531,4.060636,4.143098,-7.572501,-3.569298,7.867359,-2.713513,-5.295653,-7.518707,-8.048018,3.970768,-9.284591,-9.124445,-7.037312,2.801326,2.044521,-9.239114,-7.296544,-8.860458,9.578415,-3.613784,3.816089,6.952313,9.341884,-9.572068,-1.146577,4.695451,-4.041270,-3.271395,5.755608,9.510231,0.252246,9.673577,8.223472,-8.999436,-8.269607,5.531611,5.759802,-9.955329,2.721479,5.551375,-1.655952,-5.452070,-8.932527,8.657816,-4.621643,-5.466485,3.350753,-1.711808,-4.375798,5.474236,0.979942,-8.742834,1.339055,1.791093,8.996802,-5.025792,1.312604,0.357075,-8.780497,7.481606,1.724833,-6.917016,-5.494709,-9.452744,5.985107,0.924863,-8.785355,-7.955515,-9.272866,-9.895059,-1.454216,-2.764515,6.068278,7.221751,-1.052970,9.325083,0.615745,-0.442799,-5.918556,-6.383193,-6.316394,-0.986428,7.757779,-7.144757,8.263993,4.960180,-6.582415,5.986003,3.865051,4.896594,-5.816223,-4.319808,-5.181630,2.611821,3.316890,-7.656858,3.968618,-1.297520,3.030062,7.209427,-2.073685,-7.753293,-0.501663,-2.840955,0.220968,6.535520,-2.277283,3.663048,4.257053,8.426023,-0.272459,-1.227127,1.247370,-6.830097,-7.791339,0.428990,-3.059251,5.930987,9.391372,5.629135,0.696933,-9.418493,-7.955408,-2.874495,-3.246624,-5.163039,7.057625,4.110623,0.030971,-2.058827,9.653660,-5.900345,5.130002,-8.566261,-1.539211,0.222401,-3.582071,7.973914,2.396810,-1.593389,-5.002994,-9.268270,-9.350181,-1.299269,7.999381,2.742584,-0.263877,4.776640,7.994465,-1.309099,6.538386,8.590738,-7.515018,-9.512894,-8.604136,6.961945,6.711653,-2.634271,1.697739,3.855939,9.260994,3.428485,9.612911,-1.468784,-3.825718,-4.836511,-4.155401,-1.681085,-5.805237,9.770313,5.143765,0.234786,-8.300859,-8.599960,-5.085429,4.612803,-7.878765,4.001687,9.270165,-8.266950,6.122771,9.000105,-2.107477,-2.131943,-6.031407,1.278480,-8.533047,-4.674585,7.646950,3.900046,-6.043640,1.414290,3.956098,-4.003749,-6.956744,8.313131,0.875024,-2.094451,-1.513426,7.382213,-7.665466,-1.300951,9.543994,1.379371,-3.749540,6.899103,0.191681,7.607483,9.884898,2.278640,6.414114,0.542206,2.212504,-6.096541,-4.246725,-5.481357,4.632821,-7.346617,0.478844,9.553991,-2.906428,1.922772,2.669164,-4.199415,-0.665114,4.479861,-5.958183,4.172825,-4.280114,5.733156,0.955822,3.925905,3.354636,6.548988,1.153659,-8.905022,5.935404,-5.724804,-7.172490,-2.033851,-3.141073,-6.189434,-1.338844,1.572777,-1.999610,-3.006227,-9.195506,-9.689051,4.528263,7.276939,-8.206977,-8.115240,1.302489,-0.362614,1.426564,-2.150735,-5.993343,8.148131,-7.313466,8.247652,5.142222,-3.134770,1.771604,7.286264,7.123909,-5.716359,-6.082465,2.377738,3.981197,-8.586520,-5.962669,-3.564248,6.960843,-8.127081,-5.023607,-3.099776,6.092987,-4.435936,4.964008,0.844639,-5.658573,-5.424010,-4.674016,-4.237553,-6.524917,-0.365464,6.388604,3.155408,-0.090330,1.294262,-2.925516,0.831959,-1.507456,-9.329138,1.706496,-0.164584,8.991330,0.802782,3.558194,5.524405,-8.412519,-1.250313,7.486040,-1.864473,3.041220,-4.123102,-5.947255,2.614482,0.749049,-3.462272,9.196898,-0.507225,-7.117820,-6.089057,5.852628,2.034081,-9.872146,-5.086875,3.557832,1.911376,-7.315806,-3.357958,9.236920,4.227810,-7.373804,-9.168224,1.575725,-3.930616,-8.608805,5.783314,5.097008,4.131619,-0.372271,9.553953,-2.877685,3.478922,-6.097388,7.229901,0.907655,9.675722,0.205921,-8.005153,-3.933836,-5.619715,1.453824,7.188100,-7.010683,-2.784308,-8.621700,-4.811928,4.797955,0.423839,-0.337415,6.487069,0.833637,0.463576,-8.638005,5.995588,-0.574682,0.349965,9.478767,-8.715732,7.154798,0.700130,-4.193496,2.825396,0.419608,-4.257656,0.609603,5.011578,-1.238175,0.478486,-0.820056,7.775583,-6.536511,1.929917,4.869463,7.866533,-4.182016,-5.589119,2.375743,-8.270725,-3.153086,-1.588324,6.011597,2.685093,-0.842049,-8.560093,6.643826,5.671235,8.643522,-5.042010,6.499801,5.494549,-7.707294,-3.179893,8.225003,-8.917859,4.977360,-9.960059,-1.530594,-0.646376,-6.981023,-2.826910,0.555624,-8.320319,-2.134843,6.601634,-7.503945,0.242075,9.397657,-5.122779,1.161870,-2.942224,8.819446,3.606758,-0.583509,-5.978756,-9.008215,7.021278,1.114222,-9.473920,-4.561792,9.058721,8.254636,9.653834,-3.015099,0.089439,-9.090459,6.996177,-6.525597,2.842131,-6.259660,-4.187250,-9.423773,-1.619765,1.440840,6.663701,6.029750,-8.441926,-0.519205,1.928081,-6.123068,-8.304455,-6.182388,-0.658719,-3.086944,-6.177354,-5.108146,8.372537,-3.704511,-0.935047,2.042722,8.806793,-9.455901,6.585578,3.326510,3.105065,5.475045,-2.138753,3.490323,8.025588,-9.652575,1.850864,-9.580079,-8.767968,-9.851324,-2.803009,-9.706730,-4.041500,4.190702,8.002248,-5.771086,-8.407458,-3.366204,-4.624367,-8.313622,8.516766,6.661058,1.270759,-4.362121,-1.150821,-5.378741,-4.810467,-6.333304,7.081818,-7.113725,-1.088157,4.066322,-2.983182,9.725968,-1.052163,-4.639839,-2.798383,-5.650261,1.841818,2.425292,1.815527,-1.987765,2.294962,7.216167,5.025961,1.009274,-3.634534,-2.763531,6.606151,1.665993,5.884396,5.360613,5.378836,7.275317,-0.050741,-4.403315,-3.503822,1.875859,3.019100,-1.674937,-1.706965,-8.856313,3.427721,-9.139033,-1.712545,-9.887899,7.692042,-0.003580,5.385080,-4.286294,-4.695222,3.660587,0.547450,-8.079537,7.599954,5.717572,3.973925,6.421649,2.724091,3.678240,3.206342,2.829855,5.056799,-7.355126,-5.781514,7.930059,4.521551,4.451382,3.134937,-6.116547,0.037391,4.380682,0.346305,2.814919,-3.848015,9.580769,-2.066528,-4.780625,-1.345559,-1.103026,0.646198,7.661755,-5.693514,-7.482146,0.345224,9.151479,-4.524856,3.725219,8.639644,-6.798824,5.500674,5.583178,9.190782,4.455661,-2.040534,-5.346300,8.229367,1.839618,-7.329369,-0.214074,-0.810538,-4.803628,-4.258743,-0.109713,-9.124082,4.175215,-4.212794,9.389335,-9.602197,3.312234,-6.195272,3.500270,-4.323693,-4.834856,-2.533344,-5.008974,-7.220016,1.488211,-3.066662,-6.594349,0.334886,-5.093590,-0.648424,8.266160,-7.764651,-9.080369,-8.925823,3.090185,-7.835735,2.360740,-3.445972,4.260838,2.857791,4.726070,-0.301022,-7.697522,1.504022,-8.436633,2.539383,-4.952011,-9.435306,-6.095777,-7.640580,5.762516,0.004552,0.121330,-5.678918,-4.585797,-7.519555,0.320906,6.046821,-6.126242,-7.112785,8.469281,-2.701096,-9.362105,-5.847750,0.461553,-2.504964,7.009342,9.920789,3.767845,7.149082,6.364844,1.513106,-7.644547,7.412450,6.070230,0.009976,8.129218,-9.414694,1.045792,-7.120438,-8.714515,3.511734,6.906639,-6.941625,9.454418,-4.832292,3.925635,3.625612,7.095080,-9.640394,3.565132,2.479110,8.346981,-6.820904,-6.988364,7.707050,2.112445,-3.105339,-8.685559,8.109502,-7.684174,-6.698196,6.694008,0.836890,-1.172038,6.825597,-0.785633,-3.692519,-4.472773,-2.287063,-0.838426,4.369749,-3.957429,-5.125026,2.925036,-3.482378,5.398058,8.952709,0.193202,5.472326,4.493663,0.140304,2.603145,6.041358,-5.781309,-9.784394,-4.259592,-3.022169,9.664703,9.837999,-9.463721,-3.193126,-7.483733,-6.446396,0.010589,-1.175811,-1.183203,-3.435356,6.906022,5.356329,1.262676,-4.858413,-5.110078,-5.820264,5.846114,-4.142643,-2.503019,-5.700118,-2.785457,-4.291634,-9.159343,-7.615082,-1.022537,4.714627,8.739477,0.073151,-5.292101,-3.099104,-2.831703,3.417108,-6.987283,3.254030,-3.098617,6.219652,-7.592171,-2.729279,-9.096559,0.686478,7.864661,0.962489,5.682272,4.102754,-5.832819,-4.199223,6.658043,4.517228,9.219564,-1.592778,-8.034928,5.113171,2.891585,9.577942,-1.623757,-2.860050,8.568231,-9.532393,-8.364096,1.298138,0.892023,5.734121,8.743314,-0.225643,3.269561,-1.702321,0.306919,-8.993215,-0.664337,-1.965489,-5.447358,-6.422596,-1.348433,-1.115927,6.530970,-5.183656,-0.606860,6.542894,-4.090204,-5.865428,-1.902355,8.405364,-3.534017,-6.178863,5.512274,-1.730493,2.187341,-8.366253,9.238143,-8.901252,-4.281077,-7.288979,-0.633868,-2.555923,4.254404,-5.501333,1.799068,0.344835,9.548853,-0.399176,9.766898,-4.091780,-3.450412,-6.212507,0.285137,-8.838570,5.754670,-1.423801,-3.461647,-9.392568,-8.550720,8.513586,-9.621513,9.055312,-1.357711,1.917865,-5.623081,-4.688606,-2.144969,4.901498,9.363492,9.075561,-2.629277,-4.972077,-1.601826,-1.607749,8.266201,-3.928157,9.776981,9.260817,-6.646327,6.906076,-8.593422,2.757553,-0.253702,-8.102092,-7.198693,8.735314,-2.585257,2.770857,-5.031710,5.355133,5.152489,-7.011528,5.545587,-3.108580,-6.481879,0.107393,9.814155,5.350010,0.616342,5.653452,3.259867,-7.451810,-4.521348,-5.366355,0.402087,-8.030288,5.117347,4.593757,-5.326179,-8.217371,2.245426,2.545473,-7.237418,0.552232,-9.247798,3.282600,4.980906,4.953125,9.205030,-4.253614,3.802808,6.467804,9.624953,-3.268076,-5.658017,-5.444693,-5.162166,-5.340985,-5.120584,-2.006055,-6.230195,-8.314428,2.467175,7.284491,0.146594,9.440388,-9.057846,-2.476926,-3.135544,2.970399,6.829943,-4.461858,4.644977,3.570922,-6.234048,4.780059,6.088657,-6.413540,3.792117,-3.258755,-8.349657,-8.966067,-6.116817,-1.852198,6.892742,-4.405626,-1.643307,-4.245271,9.244924,1.157776,4.224473,0.812752,9.960662,5.711995,5.436998,3.591244,2.822948,9.206175,-9.260618,-3.155080,8.893213,9.959528,-2.230531,-3.949904,0.482043,0.984156,-3.311539,9.267416,6.652084,-4.421080,-4.501293,-1.683841,6.794687,-4.841363,0.056280,7.551939,4.796733,-1.230609,-7.629757,5.763181,1.770381,-8.889938,2.802640,6.215375,-5.445797,-9.196698,8.963649,6.306070,-0.127905,4.331291,-6.710659,-3.961050,3.368235,5.904667,7.361149,9.661005,-9.282334,-4.120175,9.565804,-0.147171,-5.814437,8.971780,5.963475,-7.458565,-9.232782,5.223745,5.534410,-7.202596,0.764440,-3.235140,-1.199964,1.103343,-0.890300,1.373281,7.072192,9.080609,-6.055242,2.655165,3.010636,8.915024,1.191519,6.216906,-9.541617,4.451419,6.405041,4.366959,8.049735,-4.866136,-8.887288,-9.833462,6.944785,6.366516,-1.337635,1.779896,7.332214,7.918401,-4.181158,9.383887,-8.361897,-0.429588,-3.233866,9.751111,-5.596349,0.154650,8.224392,-9.034863,-3.797088,-1.111782,-2.024086,-5.953037,-1.152353,2.097168,-8.845415,-2.053659,8.919341,5.773943,-7.137152,-5.449263,-1.079488,4.993209,6.209213,7.061635,-3.064434,-0.651377,3.053356,-7.202674,-9.680941,-0.001822,-7.512888,5.089659,4.850927,7.448308,5.189350,-7.482309,-5.077145,-9.513084,7.493085,5.457868,3.903862,1.272627,-7.956727,9.236131,2.081398,-1.257489,-1.396946,2.843664,-5.825651,8.394714,-5.614780,0.919043,0.363241,-8.135978,3.901111,-5.411418,1.786213,-5.730506,8.159476,-1.486669,7.065961,-1.727875,-1.411432,-5.079935,8.330998,9.581339,1.854794,-7.613264,-7.841267,-1.368699,-6.963545,-8.996076,-3.435526,7.795224,-8.163552,-5.744640,-0.911896,4.871833,-9.837049,3.355282,9.078762,-0.682730,-2.930618,-7.903263,9.571441,-4.528883,4.567223,-3.269702,2.180279,-6.820963,3.434717,-5.530059,9.912243,5.283379,4.864513,8.116801,1.658618,5.327899,-9.287049,-3.801654,-8.551419,2.469085,4.604902,4.140448,-3.546826,0.798576,-1.731118,4.381561,4.842800,-8.815977,-7.763836,-5.571788,3.106749,6.245585,2.072920,2.076170,-7.517876,2.731621,-3.558159,5.105556,-2.245647,7.730329,-8.574060,0.734130,9.853243,-2.731776,2.658306,0.050500,-9.940045,0.844089,-6.442172,-7.067526,0.505896,-6.321175,-4.382355,-3.920313,-6.319186,-5.194782,7.398471,0.202933,1.796850,-9.255842,-5.365968,2.399586,-2.479188,-9.571639,2.287410,7.155489,-2.657483,2.708040,0.834476,-8.327418,7.352708,-1.804391,-0.065775,7.952062,7.206662,-6.811714,7.869109,9.144465,-9.944229,-9.305152,-4.245466,5.019749,4.694580,0.236696,-2.719887,1.051287,-3.407559,-4.914564,5.083529,-3.019412,7.407567,-5.948609,-6.410532,-2.052077,5.340820,2.359674,4.127928,-9.781419,0.049233,0.506541,2.802815,3.615098,5.554421,-1.224836,7.730061,6.004573,-1.675505,3.393880,1.494498,9.431944,-4.877262,-3.663383,5.911779,-7.190532,9.356680,5.334905,-4.988169,-7.463084,-8.242044,-5.073837,-9.185845,6.319888,8.810124,2.427653,-1.532755,6.512719,9.892638,-1.702860,9.892417,3.377779,1.812052,7.895732,6.433382,1.957532,5.258964,9.112890,0.080188,-0.127364,8.007259,-7.656697,-0.351655,-3.933178,3.814117,8.687714,-6.003916,2.039587,1.807676,2.337319,5.929201,-6.785903,4.277431,-0.683585,-4.623306,4.552122,-1.469340,-1.943493,-7.405330,0.373534,0.527031,-0.626804,2.481526,3.437309,-1.897869,-4.923227,8.781542,-9.476945,-8.835745,-6.954479,1.450518,0.704241,8.262352,6.317741,-4.853473,8.803548,9.360099,5.272484,-2.602914,6.366878,-8.999374,-1.087473,-3.360688,-4.909017,6.290140,-3.656690,-3.137100,-6.174967,9.225565,6.359895,-9.475949,1.764876,-3.475114,8.927096,-1.656992,-4.627149,-1.813245,-2.477374,1.647665,8.394076,4.053441,-7.796090,7.839701,6.033741,-9.405645,3.284813,-1.286148,-5.825563,7.691885,7.992018,-9.840057,-5.793702,-9.548736,6.994161,4.424446,-7.239323,-6.069013,0.128826,2.808565,-8.660821,7.611532,7.790165,9.620540,9.180198,0.240851,-9.160283,-2.855317,-9.452924,0.828258,-6.997602,-2.540316,-8.236626,9.038926,8.448051,-0.593870,-5.672487,5.087370,2.264244,0.714009,5.386041,9.687921,-2.801872,6.178531,-9.639012,5.772198,2.192844,6.209015,-3.490654,9.634908,-4.531844,-3.448948,-9.723978,-0.824117,-9.585395,-4.889099,-2.970674,8.881920,5.115238,2.654372,3.870543,-7.142376,-6.883665,-7.568493,8.637169,-7.458629,-0.404534,-2.142724,-9.257295,-2.829866,2.609361,6.033114,9.520741,-9.441826,9.585737,-1.606535,-6.071123,4.068730,9.663592,-4.327761,-4.683839,-1.379067,0.074135,0.289249,0.127475,-0.794903,-2.585246,-8.352321,-9.793643,-5.090017,-5.686651,-1.163870,1.950413,8.799264,-5.382836,7.705049,1.812273,4.630897,7.484973,-3.230485,-1.062219,8.949506,-0.869722,-4.549822,-4.786138,-7.024305,-4.828649,-6.085087,2.170780,-9.112084,4.592486,-7.332441,5.489970,3.149759,-0.176970,2.989611,-3.128740,0.654871,-2.502538,4.154636,-4.464212,2.671387,-0.931197,-9.894656,7.100009,5.888598,3.028347,0.061180,2.182590,6.299092,1.284625,5.830038,9.021780,-0.672970,-8.495069,-6.352630,-2.127342,9.030195,5.278419,-6.696004,-9.248930,2.266854,3.512574,-9.145001,3.589173,-0.326577,-0.409265,-2.548366,-2.221410,1.380342,-8.527594,7.803166,6.966692,-2.562385,-2.079126,-6.796056,-5.480985,-1.623751,-0.463097,1.497445,-3.259232,-0.413085,9.814911,-7.804649,-9.253472,-1.581004,-7.191194,6.039772,9.840733,-8.563620,-6.486521,-5.825010,6.413783,-1.409862,-7.054551,0.914117,9.350737,9.224185,1.534886,-4.200308,-4.063502,-7.368659,-6.740652,-1.111811,5.877286,4.086877,7.892654,5.477474,4.385080,7.220277,3.478268,-8.741946,-2.281572,8.566247,-3.173714,6.910251,-9.949560,0.279813,5.705084,-1.336371,-5.036284,-5.279312,-7.666390,-4.034662,2.477123,5.892015,3.602916,1.910200,5.743490,8.765132,-1.672406,-6.469521,-9.409746,4.293409,-3.766998,4.751374,-4.885832,-1.447224,9.919140,-9.464318,-9.604342,7.272855,2.886852,-5.179109,3.933815,-8.360629,-1.291956,-3.451707,-4.936727,1.306727,-6.689629,-0.136689,-6.272923,9.839858,5.313051,7.188727,4.019744,3.654230,7.017642,8.426838,3.331743,6.335147,7.485290,1.454826,0.579619,-3.076781,5.201415,-6.612551,0.625711,1.479647,4.036489,3.022927,0.020626,-7.042140,-5.604680,5.386381,2.150104,9.440873,-1.435510,5.332363,9.519229,2.885242,-0.336073,0.454745,9.660626,-0.025813,8.403316,4.575118,1.948529,6.622978,-6.037269,9.076308,4.633350,-1.807803,5.846059,-7.002474,6.613229,3.033310,8.382679,0.581640,4.891658,-9.871874,5.488997,6.384769,9.465959,-5.147896,6.902262,4.831439,4.495806,3.946592,0.168427,5.320066,0.976910,-2.275490,0.611308,-7.571701,-9.859020,9.692669,-9.838100,-6.441173,-9.069427,3.632511,-7.688040,-6.047400,-9.004285,9.214258,5.589039,-6.037009,9.949286,-1.909367,3.019174,-5.449498,4.901150,6.779074,-3.684695,7.518091,5.800126,5.092548,9.812705,0.618518,5.278919,-6.689466,6.532298,9.474037,9.766263,-9.394092,-6.425146,-6.592690,-7.563001,-7.303488,0.920506,3.887204,-8.428824,9.994084,6.102125,-6.703235,2.796550,1.973799,7.812860,0.361867,-8.203194,3.985941,-5.993207,-1.085637,-4.550256,-9.621098,-7.856036,-3.868249,-4.196925,9.820066,-2.222902,-5.976669,-4.291155,-5.409214,-8.561060,-5.563221,5.076004,-7.146956,-7.116836,0.861861,3.533074,-0.566059,3.597930,-6.525110,-0.565768,7.257676,5.479511,-6.810584,-7.149741,-4.862548,6.903707,1.529559,-3.086032,-4.855006,4.615865,3.028988,8.290978,-7.502177,-0.737870,-3.015965,-5.543635,1.033768,5.169966,7.286978,2.791018,2.651515,5.230227,3.018465,-4.399400,-8.887254,4.103375,-6.035096,3.901434,-6.417913,2.706621,2.509529,-9.803395,-4.137886,-5.684881,9.949025,5.259661,-4.804639,-4.645287,-2.220651,-9.658250,-6.177635,3.669931,-4.533224,1.737825,-7.154650,-3.756257,9.936893,5.329112,-3.958304,1.911054,0.355318,-5.446028,8.697551,8.451037,7.477806,-9.614136,-4.585361,-3.698864,3.549244,1.934424,0.754646,5.536304,-6.445647,-3.270462,-3.139322,2.069976,-8.180641,-1.980275,-7.066449,9.159946,8.770473,7.234783,3.606981,-2.610002,8.155987,4.351597,9.636989,4.987426,3.723562,4.361107,-5.714204,0.614869,-3.470911,-9.560527,2.583492,0.899251,-5.332422,-3.024242,-6.204362,-7.362539,-8.165349,-9.164469,-4.641283,-2.055411,9.834556,1.188404,-6.862268,-0.932845,-7.297651,3.052124,1.451530,-1.924663,6.163046,0.629805,-5.572224,4.507047,6.931196,-5.814044,-7.813731,3.629164,-6.353704,2.671615,1.349605,-3.704948,-8.726414,-4.037861,-9.741383,9.118309,9.700754,1.064098,-4.335229,5.013599,7.479057,8.362183,-6.855501,0.021022,-3.764550,7.004298,9.967561,8.144585,2.039166,2.848492,2.333622,4.911409,0.972094,-4.478454,8.607035,-5.167137,6.765781,-8.533164,-7.351051,1.772972,-9.672061,0.334311,-2.660680,-2.420496,-3.871083,9.742771,-9.179626,-4.716864,8.287545,-7.279561,-1.756781,8.009268,-3.744437,7.007118,-2.302922,3.873928,4.943753,-8.653898,-6.668629,7.706415,-6.015691,-3.987943,9.782416,-2.356771,7.948702,-8.136369,1.327341,7.250922,6.673425,7.275187,9.733188,1.422085,6.214829,-1.490654,-8.991246,-0.110027,-1.079470,7.543162,7.487430,3.393379,-2.701594,8.086515,9.192298,-4.971634,7.196462,-6.355753,-5.706812,-6.229905,4.755182,9.168602,-9.561981,-9.764715,-6.410558,6.923169,-0.320181,-8.714278,-6.969882,-3.990481,7.782482,-2.741486,-3.265414,9.438360,-6.985332,-9.659234,5.038795,3.295989,0.108319,-7.639455,-9.725346,-8.357853,-7.367297,6.834091,-4.173365,8.993376,-9.084928,-5.786907,-2.410781,-0.822473,2.357732,9.531793,-0.888828,0.941880,-1.594857,-2.639553,0.472926,5.777340,2.616306,-8.636249,5.664163,3.817970,8.894917,-0.098906,-7.845679,2.474636,-4.271274,-4.150092,7.734269,-5.927634,5.942931,-9.285753,6.439246,8.206865,4.506293,-4.603543,2.300581,-8.856720,-3.505806,-4.228540,6.021250,-9.270170,-3.221236,6.162596,-2.451827,-0.352184,-0.917655,-0.156795,-8.168086,-5.866196,4.029367,-7.701991,3.616303,-0.244089,-0.982318,-5.437887,-5.237387,8.383380,5.300288,-4.439501,-5.323209,3.035071,-6.671955,8.566730,7.047050,-2.599955,-6.021592,6.432688,8.122387,9.109527,1.713355,-4.003981,9.995057,-9.784693,-7.590339,-6.058435,6.260515,2.376007,-5.021867,0.292693,-0.410823,-9.187919,-9.151348,-9.372231,0.138497,8.925010,1.122291,-0.423651,6.129265,3.477971,-7.086981,0.781434,-0.513029,0.013682,6.065736,-3.815817,-0.766854,-0.972446,0.910790,-3.588067,8.420556,1.344065,2.222218,3.876837,-8.607792,-9.242779,-4.161207,4.056962,-0.886733,3.245672,7.970613,-0.109519,8.427238,-9.326628,9.301707,6.709737,8.222334,-6.488782,4.476694,4.008923,-7.763728,-3.186192,8.010936,7.803422,-9.738687,9.130707,1.393003,3.854924,6.776022,5.428984,-0.562256,7.617193,1.042520,1.017084,3.995128,-0.835335,-7.801927,-9.090053,-3.976400,-9.578965,7.270336,-9.425059,1.970548,2.766513,-6.006554,7.853915,9.547365,-0.244257,-0.995150,5.937015,-5.638242,-3.743421,-7.628640,6.941992,-9.667347,6.211427,3.756527,-5.585319,8.981603,4.827924,-2.517486,6.543496,4.537001,-8.227159,0.541459,7.929267,-8.072397,-2.400334,3.310032,4.633964,5.579166,3.054277,8.896711,2.036048,9.061636,-8.416614,-9.605924,6.328015,4.027520,4.072606,-2.490801,-5.130162,-1.383026,2.605404,-5.708833,-6.598241,-7.699476,3.865748,6.864780,-8.747945,7.968436,0.109143,-5.224730,-0.136832,-3.310630,-2.418274,-5.756155,5.754928,-8.416207,-9.565677,-4.903200,-1.022328,-0.078730,-7.570711,0.969283,-2.498994,4.459328,-3.608865,9.104531,2.188051,-8.118526,-0.659338,-9.199375,-9.369586,-3.061886,-6.035059,2.843800,7.485252,-7.224654,0.357621,2.982019,-1.192076,7.842989,-4.581644,3.085820,8.500372,-6.342469,0.751246,6.172802,6.605013,-3.383760,-7.800691,-3.938290,-5.986682,9.325344,-4.790641,1.338263,0.285989,1.190526,6.361817,9.818158,1.787039,-0.338956,0.673602,-7.881239,-2.815616,-3.207377,-3.170549,-9.748524,1.303258,-0.994531,-1.084316,-9.039890,1.288506,-5.317129,6.357101,2.830955,9.240429,7.798264,5.582874,8.152203,-5.791854,3.868158,-2.850720,7.703641,3.740402,-3.919803,-6.959973,-1.427117,-2.180732,-1.459832,-8.047434,-6.989976,-0.328701,-2.408094,0.341758,3.434163,1.911797,-1.079121,-0.183852,7.102144,-1.523044,-9.579864,0.803706,-6.403705,8.872849,5.745589,-4.804999,5.520089,9.341426,-5.638293,4.234225,-9.657189,-1.879788,-7.431375,8.071960,7.711647,7.304168,-4.115307,-3.567692,9.534902,6.466161,9.825793,-0.876849,-8.036734,0.832941,1.696241,-6.357601,2.184068,-1.477135,-3.476266,-6.364572,5.940160,7.913823,-0.978796,-2.162405,2.157083,-5.694700,6.666225,4.175627,-6.039482,7.538124,9.522558,6.124729,-2.252278,-0.211353,3.732775,-7.810206,9.644445,-8.183216,8.119023,4.242386,7.228979,-0.640616,-4.923042,-5.525863,-4.067728,-2.418660,-5.307701,-3.280754,-0.981717,2.304653,7.001417,-3.750857,7.558231,-8.502352,-5.131961,4.878165,5.553174,-6.721540,8.557353,-5.754414,-3.602545,4.075032,2.470215,-6.792253,-2.962376,3.334284,1.184059,-5.014286,5.767396,-7.980474,-3.760025,5.048376,9.905295,-8.524261,-2.716832,-8.692224,0.930569,3.780259,9.439905,-0.470556,3.328210,-3.287707,-9.692819,6.021162,4.477297,3.731175,5.753673,-8.285036,-0.318200,2.006169,6.050787,-4.997797,2.044466,6.242427,0.721178,9.614211,-2.316158,9.498208,-9.211953,-9.581619,-8.361864,-8.778234,-5.428708,-5.594475,3.817580,2.504507,5.139544,6.551911,-6.253608,-7.210588,5.777915,-8.628383,5.250397,-7.732368,0.678679,0.510388,-4.677715,8.977493,-9.179097,6.351343,-2.448908,7.377223,-3.685927,-3.214749,2.462959,-2.794073,-6.263001,-8.251356,6.226839,-7.705240,5.891053,-5.499261,8.935816,-1.505145,-0.233530,4.004202,1.989167,-2.610209,0.307281,-4.988462,8.454724,3.119042,2.108501,0.655557,-4.103880,9.591767,-9.268443,5.515125,-4.375089,3.705549,-5.824733,0.892107,6.509660,5.362566,-0.808886,-5.538310,6.618149,-4.215498,4.925119,2.984313,1.244378,-2.795768,-0.785013,2.484793,0.815432,8.841393,1.870384,5.050714,6.792291,9.350013,-2.742048,5.590718,-9.249455,0.624999,-0.499493,5.106639,5.259398,9.554328,-4.529954,-5.196062,9.312095,0.128358,-9.966348,-2.643312,9.700988,-6.355582,6.472065,2.720286,2.910983,7.281912,0.354259,6.143865,-3.061553,4.940955,1.132328,2.823887,5.916516,5.680172,1.272314,4.090776,3.867756,8.628858,-2.864192,-6.839804,4.088364,8.677728,4.437206,9.732942,4.667209,-3.067392,2.884479,3.067497,-0.051617,-7.053443,-2.414780,-1.378616,3.620678,-2.036518,6.369288,9.904934,8.037590,3.659492,7.859040,-9.318017,8.651318,3.090034,-2.175242,-3.037467,6.789188,8.673421,-9.462240,-0.769980,5.818595,5.794496,9.402748,6.511771,9.519094,1.933492,9.363781,0.010906,-9.062989,1.641396,-1.551914,6.544789,4.628639,7.964783,5.322761,3.865012,1.481073,5.034376,-6.261411,8.122617,6.268730,-3.565380,-3.336888,-3.494835,7.550298,-1.735950,2.468189,7.737309,-0.944976,-2.889546,-7.495808,-9.683484,4.073873,3.839060,-1.113357,0.464159,9.129433,-0.142830,-6.116110,4.527495,2.275475,5.239150,9.120006,8.163052,2.616748,8.997234,3.093717,1.133565,2.707219,-9.860138,1.889399,-7.471525,-3.187313,5.466146,7.916543,-8.981121,-2.032020,3.513851,-2.265432,2.673949,-1.428016,-2.260924,-8.543016,-2.273599,-1.051119,2.603950,2.327894,-7.705151,-9.824515,-9.302138,-5.317775,-0.683160,-1.472355,3.792657,-7.204011,-2.369230,6.710820,8.463497,1.383165,-0.868224,-8.963841,8.501492,0.663563,4.313365,2.661971,7.744627,-0.992618,-3.414255,7.423549,-3.689372,-2.253118,-5.797045,7.440320,5.685476,-6.964477,-1.604935,5.971845,-1.045046,4.210736,2.274244,5.630571,1.986045,-1.882626,-2.954986,4.021698,-7.917549,6.316211,6.645812,-3.331773,2.795628,-3.446000,9.909258,-2.324341,-5.895280,-1.781810,-4.609024,-9.584838,8.161129,-2.879064,-1.249812,-0.618523,3.498830,-2.530677,-1.877545,-4.715669,5.431431,2.504483,-0.987571,-3.298887,-7.516315,-5.114797,-6.600610,-4.560004,-6.457663,5.486073,-3.175955,6.374481,6.215497,-1.057131,-8.629834,-9.983102,-5.709712,-3.923988,0.989535,7.418732,6.828436,-8.734303,0.174232,-0.151644,8.439564,-4.571848,1.690299,-8.063581,0.181271,3.884560,8.665801,1.021517,8.093948,-8.572971,-1.782774,-5.195381,-6.890418,5.395730,3.096938,7.499604,5.354504,-1.255645,1.718678,-0.408719,-2.682473,-4.282437,7.725880,2.566918,5.193747,0.769730,6.353781,-4.435594,-1.130866,1.774461,2.252525,5.522664,2.299374,9.453556,-8.357368,2.622553,7.738170,-8.881576,-3.026826,-1.010772,8.175456,1.145388,7.246681,-3.707982,-5.768627,-0.759511,-8.925167,-2.278360,1.066698,-3.058490,5.539824,-0.171908,6.920266,1.014676,-1.871558,-1.917166,4.497383,8.661566,1.155958,7.835831,6.943782,6.441747,7.235069,2.282308,0.015804,-3.354183,-8.771205,-1.649276,7.513913,0.167241,3.312742,5.704135,0.873300,1.962263,2.953957,-4.729081,-2.086388,-9.400540,-7.292188,7.077845,-9.728386,-4.900159,-0.841526,-0.196468,2.907560,-6.871214,4.417792,8.285478,-5.348047,6.557213,4.088460,-1.571612,5.125618,5.153509,1.102771,-5.360551,-0.548438,-6.823494,4.004237,-8.474025,-2.970919,0.640743,7.559328,-2.722463,5.832777,3.078797,-0.950128,2.106956,-0.571385,5.215309,6.688384,7.536005,-4.342442,-3.960316,3.015276,-5.026016,8.657820,8.398806,6.568200,-8.615446,-1.200349,8.805671,-7.691733,-2.633411,-3.788252,-1.983965,6.716191,1.202752,1.138285,4.344439,0.863932,-2.908711,8.380930,8.376756,0.117558,-9.613044,8.067783,-7.224809,-8.183861,-6.691658,-8.663199,-9.878834,7.370553,-4.932281,1.378332,7.759113,0.657909,-6.226240,7.411153,2.285405,2.667971,-1.797946,-0.903968,-6.215144,-1.215280,9.848321,5.277020,-2.742833,9.205838,5.479758,5.442528,2.489940,-0.351482,8.847056,4.734386,6.025196,-0.788702,2.331042,-6.550149,1.549098,1.832441,-6.747592,-8.297424,5.996950,5.180325,0.275869,7.687425,3.063332,-4.105624,2.200817,-6.841693,-7.305522,4.226870,7.931822,-3.817765,-7.508440,3.161170,-5.773599,5.980235,7.196206,2.679603,8.570727,-8.190030,-1.662341,-2.642930,-7.595309,-1.554211,9.096200,4.084354,-6.032180,-8.659403,5.659235,7.548199,0.387341,7.538092,0.520446,1.587088,1.423753,2.003234,-8.518552,5.612085,-9.795286,-6.627299,3.701752,-4.566579,1.337470,-5.661638,-7.421956,-7.757756,7.577686,7.668208,-4.862555,0.449549,-8.177876,-5.885660,-7.932777,9.453104,9.243405,1.461658,3.979748,-9.735089,-7.143840,5.460394,-6.551371,-4.461715,1.565031,-5.386995,4.133062,8.251791,3.230824,-0.779551,-0.181942,-7.311915,7.871915,-9.965436,-7.051709,3.842329,-4.124750,8.711377,0.661750,-9.394207,8.345363,-0.454834,-5.097547,-1.223126,6.681688,-0.586694,7.438526,-5.814227,-0.243493,1.659153,4.450301,5.697201,-2.926612,2.953601,-0.112753,-4.944123,-3.835354,-6.989436,4.336319,-1.531715,-3.071372,-2.887662,-1.353561,-2.727739,8.627915,0.621549,9.228124,-2.406209,9.112444,1.523809,6.041022,-5.387151,-7.001527,4.519438,8.077368,8.356719,-3.595668,4.755815,-3.344195,8.806179,-1.243652,-0.426148,9.916284,2.182167,-7.039073,-3.214594,-4.630553,-6.548760,-4.015213,-6.223627,2.267806,3.158261,9.769637,-6.894789,-0.744424,-3.159749,-8.722707,-3.379348,5.314596,7.316275,-6.437770,-0.050161,-4.730487,-7.621852,-9.040920,-5.807924,-9.878285,4.510045,5.072222,5.499931,8.907078,-7.287027,-9.883336,4.871603,-0.557331,-6.080585,-6.644326,8.358751,4.566908,5.590303,0.203608,1.405513,9.189433,2.766589,8.140326,1.171143,-9.211866,-0.601876,-4.419114,0.035165,-5.865386,-7.804819,-6.361089,5.899064,2.731765,2.265080,6.210974,-4.610571,2.880193,5.714379,-6.366055,1.022777,-9.061226,1.228740,6.724793,6.700314,-6.179543,-3.399451,0.432345,-3.250211,8.058784,5.287630,1.917649,2.428984,-8.571882,0.337717,3.813593,4.304296,-6.920140,3.806837,6.248449,-6.162562,-7.820308,-3.411686,-8.390131,-2.179633,-8.019769,-1.642399,4.312560,-3.531224,-6.838834,-5.150330,-7.619015,8.144695,-0.498040,-5.095595,4.460813,-6.077497,-3.257355,-6.228173,5.300499,-6.887666,-7.453069,6.676417,-1.369548,3.362593,6.856210,5.827413,-5.223662,4.689368,4.309663,-3.970640,-4.892477,-1.898010,-2.194086,8.359814,7.746010,5.649241,3.232866,8.236806,5.692745,-3.037215,-6.810705,-5.904420,0.206325,0.086840,-3.910859,6.701265,-6.303487,6.402025,-2.177876,2.588085,-4.484389,-4.771896,0.692879,4.321170,-9.893550,-7.853568,0.451976,9.908219,-0.511431,1.649730,4.292804,1.406168,-5.595379,-9.527518,5.976456,-6.156199,-3.013261,6.892503,-9.760401,-5.468671,7.641115,1.338752,-8.550581,9.351081,-1.440361,0.717384,4.901627,2.460920,8.981222,2.885866,3.202441,-8.482935,-0.286276,-3.993605,-7.660227,2.863054,5.600037,6.233939,-1.700357,-3.016524,7.001226,-1.136714,-9.398785,8.091152,7.604211,-9.121447,-5.026526,-8.459092,6.208914,-5.565831,-1.068972,9.598169,-2.402847,1.809916,2.281856,3.807602,4.822371,1.054983,-0.163678,7.648106,3.401296,-5.974232,-9.295778,-9.732083,9.428110,9.831078,5.622634,7.885123,3.681246,-5.479051,-1.876921,-3.218396,5.796715,8.295846,-0.476310,1.991544,9.412839,7.784883,-9.588926,0.109467,-0.882108,9.324931,7.657023,-6.892466,7.435849,8.845585,-0.104773,3.468062,9.128979,5.882039,8.416959,-3.119746,9.382463,-0.928503,1.821401,6.636737,9.767754,1.082877,-5.584634,3.734900,-0.078530,7.733674,-2.299804,-8.122880,-8.775309,4.359695,-0.851942,-5.249556,-8.621860,-9.297466,-0.678971,4.736639,-0.193126,-7.553671,-7.218659,1.795100,-7.852405,-6.798860,0.447945,-7.381969,-9.550281,-9.519855,5.179919,-6.319043,8.224055,-5.770782,1.872223,4.896669,-2.762076,-9.411071,-2.310795,-8.940330,-7.136263,3.262386,6.045980,7.474802,-4.351611,6.139107,-2.204424,2.694349,-1.830122,1.077767,7.296213,8.800787,-7.602840,5.489276,6.686020,4.662260,-8.406163,-0.357197,7.147186,1.519622,9.148802,1.313456,4.807208,3.438254,-3.752447,3.884404,-2.287027,-9.852173,-6.884357,6.708503,8.613101,2.860877,2.204700,7.172236,-1.225741,-5.225649,9.858619,3.633086,-8.757220,-9.987656,-1.795176,0.611774,1.643434,1.341129,3.630369,3.848595,-0.454077,-5.968192,-7.114023,-3.296948,-5.093853,-4.545992,-1.981968,-5.137610,6.908010,-2.113825,-1.729789,-3.715057,1.801622,6.420498,-1.660229,2.999039,-4.949800,-6.555933,7.995923,7.782866,-4.846857,-5.657709,8.790629,9.930886,6.096635,-4.057095,7.625466,6.466022,6.846388,8.736146,-3.613190,-0.530960,-1.780795,7.226705,4.380795,-1.560300,2.798730,-9.376405,0.802678,3.701647,9.932083,3.958230,-6.897877,7.220227,7.224845,7.356454,8.766252,-4.714753,-0.395164,-9.516278,-9.252819,6.247533,3.202300,6.339475,-1.864154,3.321288,-9.540491,-0.237923,-0.296277,-4.624327,0.180115,0.052868,3.464929,-1.778569,1.556402,0.186009,4.977725,7.121547,8.180504,-0.884638,0.159368,6.643417,-4.526723,-3.848135,-2.285156,-6.987826,-0.548790,-5.175531,-7.348316,-3.956731,2.032022,7.711057,-8.659879,8.838124,9.511021,6.787244,-3.090635,4.228696,1.134221,7.630071,-1.631942,6.070535,4.188909,8.086884,-7.965429,1.008910,0.609048,2.809512,-6.558230,9.525965,-6.722952,-9.346292,-1.165263,3.144029,-5.250407,2.138789,-4.504272,8.309579,-3.916359,7.695594,-5.159980,4.155736,-4.988671,-9.839174,9.101584,-8.066812,-5.358803,-6.437295,-3.254530,-8.815427,-6.032898,-6.422497,-3.122979,-7.204316,-3.832789,-7.829502,7.036071,-0.939234,-5.973953,-7.179169,3.167660,9.876133,5.039004,-6.721334,2.420900,-0.783060,-2.284884,-2.372792,3.460882,7.352435,9.243478,-9.150672,3.440428,-9.512995,6.318407,-6.890378,8.493464,3.742012,0.772540,3.100094,-4.680467,1.953432,-7.210844,-0.112421,-4.133457,0.886080,5.802777,-7.774063,-6.227780,-4.679252,5.428095,-8.197268,-6.876317,-8.949045,0.108401,-8.404941,2.012825,-2.792287,4.272960,5.262905,9.745152,3.454268,5.912029,2.428437,-8.242161,7.697200,-0.834819,8.147486,6.592422,8.775717,7.155665,8.376904,8.166088,-1.695850,-0.796717,-1.115076,-7.160814,-4.821896,-7.295278,8.516478,3.388062,-9.554724,5.741506,-8.155899,2.598838,8.373940,7.570104,-6.990958,1.788418,8.437345,-7.678294,6.908744,-2.204486,-7.809028,2.917528,9.786196,5.923919,9.514349,2.806236,6.008950,2.302604,9.621862,1.499594,5.823237,-4.964603,-0.730341,-6.053020,0.285721,0.360317,1.106635,-3.222730,5.883395,4.230894,-6.995420,-6.721459,1.752118,-1.176285,-9.055252,-0.740768,-6.805051,0.280821,-0.084011,-4.657187,-7.401269,4.645999,3.929716,-0.519676,1.464460,1.229185,5.481519,-0.336624,0.670259,3.319794,-2.666821,7.723573,6.969491,-2.866234,-0.699653,7.934707,-7.851570,8.310357,-7.548952,2.784386,4.453067,5.796447,-6.225022,0.786778,3.043782,-6.926080,6.968523,-4.835119,-9.969795,-9.128916,-9.257841,5.764763,-8.012135,-8.693620,-1.260407,8.557280,-8.325360,-4.807868,-1.425553,-3.273132,2.139456,0.114749,-0.169349,9.529229,-8.510934,1.868627,2.100840,-6.239581,9.618943,6.559777,-8.628975,6.577172,4.358166,2.428345,-1.019616,0.459951,-4.987741,-9.343817,1.179622,2.657933,0.095251,-5.955925,7.093615,-0.443788,3.072763,4.965389,-0.965426,-6.767264,-4.357255,5.591642,2.629961,-2.704862,-1.665217,-3.505373,-1.134206,0.034001,-6.449992,5.162397,-2.602620,5.583138,5.936125,0.913262,8.299436,8.794345,-0.875169,-3.267607,-8.999967,7.909020,2.541855,-6.352937,-3.207841,7.396923,6.583827,-8.741934,0.811377,4.276396,-0.152029,-8.721173,-7.210333,-4.663958,4.097256,-0.243935,4.338167,-4.788806,1.009160,4.922178,-3.623884,-0.659737,7.891182,-8.812767,-4.390344,7.749434,-0.441247,9.203644,8.457473,7.953477,-0.593462,-3.363254,-3.820963,3.446083,1.276971,8.595053,7.990870,5.953711,-2.280553,9.512931,2.115784,-7.225584,4.569005,-1.468008,2.051290,0.692861,8.646850,0.065724,-1.822301,4.594911,9.672112,6.498954,3.353013,4.703146,-5.303066,-2.083272,9.553576,-2.551819,-1.716541,-8.517900,-6.609447,-7.279559,2.498098,1.701982,-1.262814,-3.805281,9.454223,-3.426259,-3.269842,1.951398,5.153813,9.521690,-3.734340,5.214278,-7.387974,-8.321098,2.142451,5.863744,-2.336563,-9.568278,3.066702,0.858357,-1.543131,9.301450,1.845072,-6.054977,8.114747,-7.453611,2.299277,-1.012726,2.236753,-7.287266,1.566513,1.416229,3.650988,-8.086056,-6.770292,9.966195,-6.337647,-4.869975,7.410639,-3.922190,-5.978674,-9.163859,-4.482121,7.571759,8.795155,-1.018463,0.258603,5.728301,5.211660,-9.943038,1.992581,-4.200290,-1.804714,1.589840,0.601531,-2.858698,-8.814780,9.272170,-2.720832,-2.713977,7.733125,-1.565745,3.225887,9.511095,-9.480718,-4.687036,3.018257,1.088347,9.969322,-7.496604,-2.710166,-7.877637,2.531037,0.703902,4.900954,-9.176818,-3.263732,9.996692,-1.462931,-8.018964,-1.901975,-3.766667,0.835678,-4.196497,-4.980874,-5.520128,7.812692,-3.690140,-3.511636,-9.794771,4.037486,-1.054373,-1.153225,7.546215,-0.920369,7.541155,7.563625,5.604250,1.991583,2.172657,-9.504434,-6.820651,9.538663,-0.293202,-6.090359,4.803104,0.464506,1.274583,5.236925,-1.790350,-5.660496,7.023921,6.326495,-2.260732,-6.222512,6.219558,1.191997,-5.360361,-7.579666,1.439185,-5.784357,-4.920847,-4.002749,6.358118,2.792605,-1.733934,8.574526,4.595091,-2.265131,2.461915,5.799460,9.815042,-8.297830,3.432917,-2.019543,0.767304,0.196418,6.543764,7.135924,-4.776961,-8.890636,-2.516902,-4.019168,0.525120,5.627237,7.556046,0.663763,-2.841524,-2.728703,-1.631149,-6.584341,5.057349,1.436010,5.163883,2.096110,9.046035,-4.281962,0.787548,6.073131,0.482091,1.197178,-1.247347,6.748413,-4.073208,-4.206637,6.726280,-0.978029,1.261090,9.834944,-3.322953,-8.878867,-3.698854,6.630945,4.851278,-9.760387,-7.808947,6.221719,-9.633416,3.994523,-2.753261,6.744875,-7.344530,2.594707,-0.033145,-9.540906,5.205805,-4.969713,-4.597867,-4.029587,6.956348,-4.668087,-4.282364,-4.506143,3.226376,-1.415363,6.408496,5.772212,5.629578,0.376946,3.989456,6.405261,-5.089221,-3.159247,5.289512,-2.746986,-5.446013,-4.086480,-6.559260,9.930700,-6.969767,-6.816424,-0.640847,7.321468,-7.088397,2.555720,0.622735,-6.441895,-4.776665,-4.037709,3.780498,-8.157930,5.703986,8.219737,3.840456,8.307154,-7.176286,-7.007019,6.013155,-1.597963,-1.008705,6.691107,-3.873897,-1.818509,4.136188,4.245971,5.586277,-5.278340,-3.152687,1.210773,-2.413895,-5.944930,-4.964746,6.531358,-3.295308,3.329045,4.954133,-4.602304,-0.906723,2.007149,4.350449,3.839081,-7.290124,-2.896663,5.958847,0.314977,-3.442882,-2.588669,-2.879189,6.081566,7.252417,4.148132,2.625186,1.207769,-3.080190,7.705397,7.336902,9.844464,-5.841435,-4.679312,4.947629,-8.130166,6.245254,-9.458746,-3.001960,8.896409,-1.428814,6.158852,-0.526952,5.251123,8.635854,4.026495,6.291252,-1.396699,-8.638854,0.020595,-4.385967,8.331370,-9.384084,6.453454,9.632054,7.011404,-6.569820,-0.641829,1.744665,6.089356,-4.210956,4.818753,7.111450,-1.460218,-6.206576,0.380163,3.472656,7.527268,-6.680608,-4.859827,5.687512,2.934027,-4.284463,-4.628588,-3.818872,-2.791557,-7.119179,-8.462663,-2.823781,1.142253,9.109609,6.543947,-9.219749,-7.950115,-6.278479,-3.848613,-7.311920,4.190582,8.775951,-4.598827,9.594194,2.313968,-9.523396,-4.783522,-4.045050,-7.341282,-1.634830,-2.898926,-1.253427,-0.466116,8.646320,-2.532363,-7.986142,2.498384,0.159491,2.675794,-4.651124,9.377913,5.355419,9.362854,9.438360,6.779219,-0.186637,-6.163547,-5.975747,7.685005,-4.165137,-9.486462,3.751644,-3.882344,2.902795,9.578281,-5.528505,8.147102,-0.465135,0.103809,-1.183696,-3.135493,-1.181071,8.951575,5.445576,7.804553,-4.151383,-9.242190,0.917898,-2.324609,1.205781,-5.866181,-9.387235,8.752542,9.087778,6.456810,4.991093,-0.314190,-5.849960,-1.220591,-5.937322,6.679773,2.145992,-6.243886,8.302525,-2.101024,-3.855646,-3.530924,-5.469885,-3.139920,3.654824,2.101954,5.415576,-8.362487,7.002611,1.579619,-5.432005,-4.375971,-2.206605,-8.849435,7.515111,-8.182302,-7.027988,0.319211,-1.061146,-2.897333,3.531417,-9.999864,5.505912,-0.825281,-0.452170,-6.604489,5.995733,-1.535908,7.617298,8.937614,7.783684,-4.817322,-6.076210,-4.854195,2.589884,-6.257920,-1.977370,7.596914,-9.410652,-5.707885,2.891005,0.897433,6.294633,3.081157,0.533383,-8.804193,-0.455162,-1.162140,-8.469534,-8.567703,8.233074,-5.412513,7.960370,7.041760,1.851640,-7.448596,-5.634098,3.457817,-5.721075,-6.185631,2.104704,-1.127145,9.929490,6.762008,-1.345635,-7.109430,-3.964907,6.468033,-3.313754,3.105755,4.635212,3.316736,-5.325846,8.279200,7.820383,-1.359595,-9.629952,-6.158015,3.135256,9.120759,2.883999,1.224821,-5.652707,-4.850087,2.865804,1.352637,0.380851,-0.185850,8.927130,-0.278446,9.786901,-3.076163,-3.636054,0.520409,-1.896849,9.916222,-2.684007,2.377420,7.729299,-8.805199,-4.590892,8.201820,-3.098456,3.715639,-5.364738,-2.310814,-0.325928,9.288410,7.903009,-7.043572,-0.460201,-9.551303,-1.752865,4.551623,0.312166,-8.409639,7.687617,7.821308,4.984027,-2.265212,2.016900,7.442773,3.714391,-9.908327,6.603238,-5.512785,-8.094745,2.991325,-7.286292,-7.065963,-5.891465,8.412163,8.870364,6.203652,7.048957,-5.764174,-4.498727,-9.563109,-9.752030,-5.711102,4.099586,1.861909,3.494412,-1.562890,-2.565324,2.852038,5.397440,-7.611179,-3.257932,8.087608,8.885370,-2.029813,9.783521,8.368729,8.526834,-2.814413,-6.985271,-6.819353,-1.842218,-9.736038,5.582511,8.247921,-3.580970,1.819451,8.867735,6.088295,-8.731408,-2.343023,-8.775904,-0.356517,2.616972,6.485245,-3.624553,-2.129760,-1.998659,4.085158,-5.938872,3.863217,6.321817,3.542080,7.319424,5.195801,-1.904228,-0.533644,-9.733691,-1.081660,5.631775,9.446321,6.042659,-6.598533,-6.800801,-6.311891,-0.197870,-0.855733,-0.305289,-8.657085,-8.291705,-2.030756,4.419626,3.492307,6.283887,9.813050,2.909824,-6.722072,-9.359337,3.173309,2.313647,-3.566310,4.667610,0.744080,-2.580603,1.519344,1.199899,-4.120393,-7.570288,-9.607397,3.130826,-0.254980,5.606401,-0.372918,7.221436,-3.311867,9.550358,-9.186562,5.101620,-9.085781,8.836754,-0.225607,2.165359,3.001651,1.872369,0.592598,-9.717668,8.065829,4.376537,4.774863,3.660038,2.858080,-6.377333,8.302172,8.052695,-4.952911,-9.692384,5.661578,9.740655,6.442223,5.056990,5.194805,9.337352,5.365283,-1.175108,6.061456,-2.572321,-8.887478,7.816382,3.237324,-9.636260,5.692381,-1.513652,-3.556104,-5.347788,-0.290183,5.637160,8.089497,8.636175,7.297252,4.241401,6.653150,3.896647,3.395086,-2.174290,2.222918,-8.785285,7.184571,8.706325,-6.378462,7.890860,9.804467,-9.303787,8.489369,9.708562,-2.364480,-3.330788,7.524738,7.204723,-9.898705,6.879302,-8.297121,-5.320908,-4.384102,-0.186021,8.560552,-3.724965,-1.916434,9.680649,-0.730354,-0.671847,-6.744010,-4.625131,-3.405360,-3.843185,5.250586,-1.807664,8.069877,6.337141,-3.846386,-9.254201,-1.947739,9.412527,2.695612,-7.523501,6.713996,-1.652597,8.572257,8.150146,1.327286,-5.062527,6.455809,-3.715277,-0.672396,3.372393,1.376549,-8.227647,-3.437395,-4.105041,4.400537,2.271992,6.033114,-3.328025,-4.508658,-3.111220,1.591041,8.587019,7.289371,8.578110,7.203627,0.486702,-9.326023,-6.663308,1.256481,-8.003877,-4.986956,3.320840,-0.897061,-5.211089,-6.728215,-9.350702,-2.325920,-2.090690,2.758194,7.021621,-6.169464,-4.417756,-6.709170,4.345040,4.661417,-1.049430,4.591945,-9.043364,5.860526,1.297010,4.377728,4.323102,2.703755,-3.767047,3.226195,1.034259,-1.224073,-5.946090,6.934350,-0.807641,-2.864656,-3.629508,-7.856987,1.027730,9.343041,5.165733,-9.186570,-4.980193,3.333941,-8.303745,-1.214621,-9.225808,5.209631,-1.351164,8.395571,-2.245263,5.693894,6.093496,9.567048,-0.484408,3.444095,2.018555,-2.313605,0.606817,-5.670476,4.404402,-7.014060,5.664916,-5.173645,-6.944795,-3.748343,9.355441,4.987173,-5.760116,5.218218,9.576768,-9.850834,-2.798942,4.596583,-9.295614,-1.933253,-7.639055,-3.215499,-5.692621,3.981669,-0.254696,5.178743,-5.883795,-7.752889,5.063362,5.793397,9.147777,-2.055291,-7.815870,1.506796,4.852008,-9.333758,-1.222314,-1.291796,-7.704346,6.394774,9.377032,-4.969754,7.461682,-3.866788,7.624620,-2.985561,-6.976968,-7.915815,-7.911989,5.362171,7.923189,2.069164,-1.943483,5.471695,-8.694632,9.882097,1.409258,8.541816,5.773410,-3.878572,7.099882,1.669242,0.601831,-4.128811,4.140786,9.983660,-6.272476,2.020402,-7.223764,9.851893,2.183995,0.675418,-3.693025,-5.393417,-5.110805,-6.664083,3.493946,4.347169,-3.229761,-6.291837,-1.049338,-4.792536,-7.399245,6.235743,-3.445792,8.623880,-4.655397,4.517850,8.496623,-9.427210,-8.595868,3.740237,-7.759863,-9.806884,8.703467,-6.288085,-6.969144,-8.037636,-4.717404,-2.990099,-9.825127,1.234162,-8.552617,4.585622,-0.080852,6.947564,7.151707,-4.995859,-4.017547,-6.809114,7.232281,0.685550,4.722007,-6.966155,6.370380,7.685874,4.791908,-1.258759,8.594311,2.369700,1.495370,-9.504721,-8.213550,-4.358797,9.362063,-3.990457,-1.306995,-2.714335,6.640026,7.543100,8.708067,-9.103371,1.662789,-0.725697,-8.486728,-0.284586,2.093368,-3.564222,0.136253,-9.084289,9.702249,7.544819,-4.138206,-7.517262,3.460329,-5.297367,-8.433387,5.943320,-8.135487,-6.069910,5.171435,-3.252111,8.291017,-7.875122,-5.705593,6.070985,3.316075,0.841080,-1.497674,0.693826,3.123711,4.937412,-1.494654,-7.992652,-0.221331,-6.782616,2.798768,-1.360103,1.730932,-5.987224,8.588810,-5.365914,-3.210226,-5.194605,2.131745,-5.998455,-0.843099,-0.420285,-6.894568,5.419858,6.575456,9.592352,-8.441526,3.235756,-2.692441,1.430102,8.065062,3.224913,9.150706,-1.303147,3.729896,-3.780621,-8.983089,5.569062,0.781727,-8.745682,-7.974021,2.129590,0.046708,-6.155833,-3.608504,-7.351573,3.552094,-3.668678,4.989957,5.352882,1.963111,-1.613737,-7.618345,9.879584,-1.059702,-4.700391,5.835437,-0.309964,-6.838073,-0.867756,-1.253160,-1.514441,-3.538732,8.532406,-7.898327,4.968424,-2.900620,1.800727,6.244972,-0.200545,-3.012955,-9.670131,-0.634422,1.431160,3.475818,-6.197748,-9.324927,-4.098138,7.912596,-9.810645,-7.809718,2.844961,-4.168864,-1.988368,4.881877,3.348042,1.597009,2.393572,-2.493555,9.799152,9.176529,-2.237812,-6.342417,-0.761729,-0.234217,8.762193,-4.526464,4.651554,-1.356972,-5.797877,-4.967843,7.573396,8.815117,7.864852,2.627272,-3.169079,-1.835237,-6.772312,6.733647,-4.929061,-6.553517,-7.483026,9.738145,7.055693,0.361088,7.097706,5.550028,-9.339654,-8.649427,6.636874,-3.945163,-3.348210,-0.166345,3.295850,4.406977,8.576246,-1.817617,5.908448,3.285523,7.603744,-6.113182,-6.620336,2.591684,5.524576,-6.469633,-0.813166,-3.082701,-7.627462,1.755981,-3.971492,1.519404,-0.538000,9.670130,6.979350,-1.245189,-3.454676,-4.098252,9.258552,3.167610,9.163045,4.236643,-2.620452,-6.703432,-0.931522,-5.977152,-2.689846,-2.705645,2.598662,-8.467662,-2.290470,8.719040,-0.070172,0.946389,-5.008329,-5.747613,-6.446140,1.372168,0.809152,0.881889,9.581791,-5.435184,-8.714858,1.169209,-6.841992,-5.183135,-7.455936,5.261919,6.497903,-8.969603,4.738715,4.451874,-0.336929,-2.848900,-5.385854,4.452854,-1.421850,-6.400999,-4.144130,-1.318063,3.201448,3.693686,2.595316,-3.042063,3.443747,-1.932028,1.147373,6.760141,-5.030295,4.114243,6.841056,-8.198339,-2.300863,-5.618321,-6.128021,-6.216276,-1.620739,-9.983459,-7.616291,-1.907771,4.752562,3.637078,3.638868,1.983301,-2.843324,-7.046565,0.806621,9.654669,3.248571,9.671800,7.484639,-3.430409,7.912053,6.463894,3.584189,-3.107115,-1.061144,-8.830505,-7.219764,2.209926,-2.130967,-1.614843,-2.944633,-2.088074,-6.382823,-0.304970,9.111617,5.729335,8.881782,-3.732692,-8.037340,1.746933,-0.941061,-4.860769,8.141496,-2.148442,-5.506483,-7.699721,-7.083134,-7.226786,-7.837887,-5.936999,2.546215,-3.009516,-5.516201,-4.213638,9.743281,7.691176,6.016085,-9.454084,9.857181,-4.617031,-8.310856,9.315234,0.857136,3.554834,-5.018025,2.023481,3.175052,-8.060074,5.700862,-2.002457,-6.377971,-9.041063,-9.743165,4.004303,1.680780,7.394283,-8.429669,9.540171,-4.771169,3.064921,-6.582791,5.589371,-6.300640,-8.832052,-6.942627,6.513483,-2.456967,-1.806940,-4.027555,0.453320,8.631524,7.154297,0.740836,-8.200431,6.375779,-0.220615,-8.037275,1.102760,5.165875,-5.955160,8.509281,-8.024028,-8.781410,-1.815579,-1.581305,-9.516148,-4.782420,2.040278,-6.195357,9.221017,5.059681,-9.192026,2.973934,1.167184,7.954101,-3.782137,0.770051,-2.675623,1.253072,-8.004911,-0.490101,-3.601428,0.088416,-6.733722,7.930165,5.526079,2.580393,-3.012680,-6.433301,0.141792,-5.987987,-0.555972,5.426995,7.491940,6.050975,-0.976694,-2.370959,-3.841947,9.624103,-6.634721,-4.633321,6.496845,5.271301,5.125455,4.648407,7.495763,-4.046803,5.415645,-0.177593,8.841939,2.303677,-6.664719,-0.630440,1.218322,8.251867,-4.739572,9.712186,-2.134952,7.123269,-5.984230,-8.439398,-4.816591,1.087502,-6.841848,-0.501750,4.848685,-1.597206,-5.183578,-6.276408,-5.513289,3.209539,-5.796905,-3.703685,4.841101,-6.493545,4.436517,2.186855,1.770919,8.598725,-7.453414,5.528355,5.883557,0.775748,-4.082826,7.382193,-2.456897,1.007801,-7.533273,9.483116,-1.181430,4.470504,-5.015495,8.046692,-8.774057,-3.946510,2.172377,-0.425272,8.783380,-5.283850,-3.170963,-6.569334,-2.758323,9.210564,2.773463,-3.388595,-5.115911,9.649282,-0.976494,-8.547436,-8.813701,1.139142,5.496726,-7.476473,-9.198758,-0.839774,0.944214,5.853865,3.432130,-8.934510,2.642750,-9.274578,-0.786070,-6.944068,-9.587792,7.625083,1.928549,-8.276894,2.625250,3.284563,3.236830,-6.692943,-2.888722,-0.747991,-9.632050,7.469528,7.658622,0.591798,3.278396,-9.245571,-0.511049,-9.190080,5.207150,-2.752222,-1.329258,-6.730897,-0.083228,-1.253079,-3.328004,-5.667963,9.265854,-6.172187,5.924722,-2.979703,2.829352,-3.968341,7.286324,-8.486069,-7.988045,6.158251,-8.264678,-1.289287,-4.600731,-9.875284,-1.615248,1.394474,-2.460420,-6.318726,8.519539,-6.143016,-4.234918,-7.851030,-1.905774,-5.747140,-7.541051,6.478677,1.048865,8.754653,-1.540240,-1.676217,-5.135867,-5.604817,0.230768,-0.226488,6.227743,0.654266,4.464976,7.573883,-6.581157,-6.587659,3.082521,-1.436148,-7.505353,-4.065534,3.857097,3.097759,-6.004332,-5.267234,-1.488531,-9.813662,3.972555,6.672183,-7.001441,-8.188541,-3.771383,2.059548,-6.440437,-1.622409,6.944440,5.406520,1.873196,-0.988448,-7.831149,6.230618,4.268570,8.557804,-0.373395,3.205828,8.561369,9.363149,1.733355,-4.971857,-1.065434,-0.524464,9.830541,-7.460207,-0.982150,5.172922,6.681261,2.768803,-4.571982,-4.802350,-8.895382,8.466728,8.193963,5.629159,1.950495,6.379277,3.818314,1.904480,9.645701,6.359871,-3.072509,4.464172,-2.581308,-0.105111,2.186499,2.416139,5.101209,4.262977,6.080248,9.090012,-0.262496,2.469067,-7.331661,4.059266,-4.718336,2.273097,2.423608,2.796793,1.126816,-9.532166,-0.179120,-0.377468,2.097662,-9.638967,8.050261,9.453227,-1.071733,7.186237,-6.245208,0.483289,4.050718,1.055417,6.250265,-3.738032,6.329964,6.508529,-4.396150,5.597798,6.730112,1.523795,5.841710,2.994713,0.497248,-9.395658,9.771185,-4.525817,-3.318416,0.708234,-6.915176,-1.267271,-7.332260,2.651806,-8.120550,-4.011725,5.311410,-1.490381,4.391823,-9.173835,-4.680705,-0.444615,-9.788098,-3.921824,-0.881593,-8.381834,-4.837551,-7.461173,-9.427986,5.860354,-1.969289,3.442106,7.645746,-8.900434,4.744788,4.777228,2.638507,4.699106,2.128504,-0.197005,3.509995,-0.983279,-6.274555,-2.081593,9.934381,8.684631,-3.197630,5.838601,-4.596388,-7.747260,-3.114328,2.385853,2.075293,-0.014614,-4.264925,-3.277639,3.219050,4.394820,-1.668082,4.145682,-0.323044,3.848138,7.167104,-5.817053,0.319657,6.323376,9.277666,5.565086,4.872125,4.553595,7.404332,1.667270,-8.214559,-4.760310,-2.296207,-4.373724,-2.042280,9.406652,-4.686449,0.594912,-7.363555,-2.286904,1.932176,-4.931863,1.689235,-8.444044,-9.741522,5.917403,9.675594,4.622076,6.821551,-6.734756,6.160854,3.631735,0.017992,9.608187,4.534013,7.832709,-5.456827,6.165183,0.800851,-2.668926,0.781539,0.954390,9.126228,9.662802,-9.228149,-9.169269,8.926757,-6.162371,-8.472237,1.144094,5.144476,-8.711133,-0.549504,2.253898,3.518101,4.537318,8.405811,0.942815,6.882772,-5.851596,-2.590404,-7.130830,-0.061460,8.397253,-2.086824,7.492808,7.414949,3.170476,9.097560,-6.803447,-8.646941,-2.577842,-3.103447,-8.346372,-6.882447,9.680439,3.202943,-0.944752,-8.081721,-4.306252,-7.270225,-3.108933,9.331984,-6.856223,-4.874157,-5.829692,-7.573162,8.853544,-2.746623,9.541202,-9.956883,-3.886637,-5.554621,6.415200,-9.936347,7.539712,9.567758,-1.185574,-7.560533,-0.856590,3.645625,7.911266,7.254471,-0.601238,5.384212,-9.045657,8.124072,2.704731,4.926175,-4.526125,8.144389,4.428929,-0.930545,5.721166,-1.485959,7.359257,-1.864545,8.281537,6.004328,-4.313471,4.906306,-4.246561,7.384610,-3.397175,9.712303,-0.194975,8.499802,7.908725,2.228254,-9.654923,-1.176172,-9.836288,-4.251519,-7.493315,4.301031,-9.982748,6.095904,6.651029,7.077251,-4.851876,2.461798,5.334473,-1.241022,-3.521532,1.517854,1.716665,-7.952279,2.799369,3.053818,7.283268,-7.706445,-7.454763,-3.575394,-2.736306,2.615363,-1.226486,3.790510,3.937201,1.182323,7.265350,-3.628162,-6.732527,-8.112160,-1.104588,-3.188511,9.409061,2.321333,-5.816485,5.865556,2.284799,4.642139,9.793640,0.067349,-3.278337,-9.037721,-1.255804,-3.546765,-9.834853,-2.488753,5.031861,-5.894759,9.472957,-7.832904,4.198570,-8.879269,-0.739679,4.961390,-1.071009,6.048411,6.272499,-0.911803,-3.506994,-4.886886,-8.763476,6.454144,0.713546,-3.753151,-0.145732,2.906715,-5.663205,-2.643025,3.073825,5.225942,6.817797,9.985958,-4.321461,-8.463603,-7.464152,0.524223,8.496766,-9.695382,-8.556095,6.342437,2.900783,3.172286,-3.995149,5.235098,7.767911,2.544773,4.960681,3.104269,-3.313309,-7.746630,-5.799103,1.685808,1.983750,0.249870,-8.883373,-9.486689,5.997607,-8.856626,0.757453,6.951277,-9.986323,9.573769,9.851429,3.824829,-6.695595,1.774889,-3.461395,-9.558465,-6.617814,9.246325,-4.062636,3.955939,4.230793,8.820077,4.665692,1.890184,4.024427,6.526898,1.202756,4.382436,-6.347431,4.429881,9.609387,-9.333138,0.389164,2.626154,0.314467,1.561396,-2.184950,-8.875830,7.063665,2.808165,-0.739736,-3.692690,7.222227,-4.517246,-6.787240,-5.337069,4.343545,0.585451,9.145001,8.295074,4.728730,2.305867,3.638676,5.910311,-4.472360,-0.274919,4.519896,-0.308850,-2.448051,5.863397,-6.109960,-2.355603,-8.905255,-7.898230,-6.395711,3.309325,-7.331813,4.057111,-8.255945,3.460150,0.867281,8.350546,-9.990577,-0.398584,-5.418528,1.821559,3.850221,1.736985,2.335808,2.539743,7.167519,-8.077633,-6.160459,2.138214,-2.021362,7.312433,-6.053123,3.809793,-0.804894,4.962640,8.378705,-6.463959,8.022109,-8.346683,9.958613,-4.625557,-7.167430,1.808666,7.471686,1.757072,8.026394,6.590008,-2.547370,-9.907133,-7.414284,4.341503,-6.489633,0.298019,4.532606,-9.068434,3.245660,8.466136,5.361837,-7.596627,-0.855567,3.635950,-5.874210,9.203451,8.564910,-5.520646,-0.354354,9.486300,0.173528,-2.619950,-2.115264,8.951741,6.396857,-8.583900,1.825058,2.589661,-4.684343,3.414526,-7.686145,2.425785,-0.244666,0.716061,-1.376617,1.314218,3.004816,-7.712840,2.103529,-8.684058,5.930527,7.930339,6.322868,-3.337275,8.503629,3.757926,-9.739881,1.761643,-8.497909,4.565078,5.796373,-9.829149,-3.001715,1.988549,-3.813938,7.826938,-0.943112,4.983984,9.213278,7.381284,5.985363,-8.998012,-6.253279,5.968599,3.978934,1.841337,9.702620,5.270233,-8.031829,2.172562,-5.531460,-7.626674,-4.004519,8.689351,9.324778,-4.395441,4.649369,8.569920,8.058686,-9.756536,4.670853,4.361960,1.526485,6.472123,1.409055,-3.278729,8.567464,-9.133770,-3.998424,9.477317,3.086998,0.662874,0.536675,-5.446068,7.957209,7.800817,-2.501395,6.824006,7.152532,8.298553,-0.840753,8.578806,1.741330,6.812655,7.317027,9.547963,-6.646339,5.911136,7.269864,-7.963840,-9.348448,-9.305322,4.428292,-8.260220,-5.182084,6.595912,9.182098,-6.773478,6.744091,4.805665,-6.622147,5.889249,6.181397,-5.182961,-5.100383,6.085202,-0.673381,9.223017,8.881079,5.290651,4.030861,-3.358948,2.036736,9.648399,-2.618342,2.294262,-5.971346,-1.115469,7.178214,-5.078101,5.770675,-8.711004,1.256330,3.145580,3.644073,-4.680894,-2.726467,7.877549,1.826439,-3.562041,2.050594,2.581057,-5.078324,7.321590,-9.223558,9.789789,4.330248,-4.962788,4.695329,-0.004497,-9.026734,2.009440,6.451881,-1.158880,-2.910273,9.811713,-8.425241,8.067450,-8.244890,-9.867088,-2.521670,-4.211042,7.195487,5.187770,0.911147,6.358381,-3.638304,-8.786374,5.551188,6.399064,6.256010,-1.982730,8.878816,-4.708139,-2.397792,-3.264304,-4.581620,1.026091,6.065931,-1.669275,-5.424926,-9.742228,-4.858616,-0.111840,0.796237,4.824999,-8.843059,-2.276856,2.923961,2.540885,2.427136,0.194948,1.846737,0.544912,0.527407,8.236332,2.569975,-5.188806,-4.262192,-7.553102,-3.377790,-2.501013,1.645562,-9.765245,4.704381,-6.316569,-1.230287,-1.922480,-5.520005,-9.232604,2.827880,3.019599,-4.119925,-0.078452,9.555021,-5.332410,0.516237,-5.383036,-3.500659,6.720104,3.703317,-9.337536,6.144410,6.545084,1.362871,3.638706,3.312156,5.240694,8.614814,-2.558282,-3.139829,-2.583813,2.557820,-6.089039,-6.589138,9.197021,-6.935225,6.680976,-5.835953,2.997753,-6.344659,-8.233182,-7.194090,5.099821,8.743502,-7.522915,1.691055,3.772235,0.985604,-5.626598,-4.536023,3.398668,2.511787,-9.428576,8.105154,0.956072,6.546854,1.836744,-5.760005,7.105933,-2.775252,1.931236,-9.593037,-2.579792,3.038755,2.847428,-4.888846,-5.943111,4.736070,4.117016,-1.646468,5.605959,-6.703120,1.803204,3.040299,3.230097,-4.467662,3.847458,3.668615,8.734067,-7.741045,-1.170500,0.993762,6.992052,-8.355687,-3.284492,9.548131,-5.287875,-8.767105,-5.552171,-0.216425,-4.567185,8.756765,3.456697,5.393078,4.507685,-3.948064,0.661675,-5.624629,-1.264300,2.843866,8.161257,-8.296923,8.522148,-3.592049,9.673338,4.371778,8.255247,5.253387,3.761741,1.427354,0.890480,9.918563,-0.371503,5.149656,-7.669145,4.480848,9.783734,2.790544,-3.464169,9.631061,-9.296468,9.288223,6.761070,-3.604079,-3.392981,3.721531,0.212889,-2.503319,-4.196182,3.581409,-5.123807,-1.097014,-5.123025,-4.986528,5.249473,-1.257351,-9.527312,-1.275735,5.076683,6.339335,-4.724262,3.205035,8.032513,6.256115,0.305782,-9.207695,6.342345,6.896804,-0.932787,0.337255,6.179404,1.422809,5.623389,9.476212,-2.140309,-4.169958,4.156771,5.878168,0.812762,-7.770992,8.717337,5.136591,-8.819390,-6.725318,-4.846220,-5.395802,-7.440685,-0.089091,1.230117,-2.530577,-7.598246,4.213102,-6.024384,-8.648780,5.924499,-5.447650,5.526585,-7.719828,-0.569734,-1.309306,-6.237304,2.089288,-9.084205,-3.620079,6.359189,2.630968,-5.018272,-9.884022,7.591632,-7.002413,3.985647,2.502909,-8.005987,-2.782212,4.478479,-0.387514,-2.550880,-9.734629,5.169996,-4.111497,9.987517,-2.985669,-8.484398,-3.177411,3.777755,5.430500,8.398315,4.794950,-5.559254,-8.390198,-1.478248,7.311252,-2.477065,3.062941,-0.530163,2.602120,3.062981,6.942688,-8.932912,-0.021418,2.217998,-4.868944,-5.527546,-5.740519,-9.056369,-6.089262,4.662346,8.833480,2.154561,4.779961,-7.906343,6.097276,-8.577172,-7.111226,-0.438855,-2.349097,-0.028043,-0.922455,-7.202233,8.491392,-7.908972,5.534695,9.935050,0.977765,4.036992,-8.191430,4.327766,-6.063240,4.768191,-6.490455,8.350926,0.861450,-6.630300,-1.913454,-4.868353,8.431939,-1.466934,6.890218,7.666559,-1.548368,2.815918,-2.722893,2.253521,0.940762,2.330696,-5.945771,-5.343094,-2.251566,-2.532120,-2.399563,-5.549244,8.324848,-7.699281,-5.128141,4.097960,3.919208,-0.671446,-6.269352,-6.634613,-8.235242,4.427224,-4.426542,-8.023968,-8.364103,1.102251,6.420817,-6.035662,-0.883144,3.460727,-3.666258,-6.912622,-2.543267,-7.007096,-1.038566,-0.923304,-0.220192,5.106929,0.841325,-0.014703,-2.526477,-7.091282,6.428741,-7.895167,-2.013204,5.788185,9.489608,-7.520861,-0.837415,-0.214636,9.993818,9.079990,-5.145528,-1.236320,-0.466772,-4.688421,-3.293537,-8.261419,9.904691,-9.808120,7.401209,7.993076,5.912928,-0.174610,-0.980851,-3.677513,5.047268,8.512088,-5.859537,3.748029,-9.676703,-7.844500,2.349798,9.392787,7.845413,-8.050828,9.207096,0.890728,1.906956,-8.065830,-5.946213,4.900964,-3.046889,-2.573439,-1.824282,0.009992,3.397162,9.648131,-3.969000,5.379705,-2.232796,-5.600986,9.105218,-6.322530,1.095831,-5.206664,8.840735,0.892382,6.436993,9.257350,-4.313885,-9.051404,-0.137878,-5.727294,-3.428299,-1.700175,2.659508,-0.976574,3.195304,7.416465,8.834210,-9.830015,3.448336,-3.264839,6.687885,-8.522490,-4.165630,5.783181,-6.779318,-6.582094,-3.694580,-8.753249,3.168260,-3.843134,1.035089,-3.728780,-2.241785,-1.020413,-9.884668,-6.918246,-5.539553,0.735058,9.681839,0.372844,-3.684354,9.261856,-3.448442,-4.596318,-6.690520,-8.951360,-2.577531,7.254476,-8.758414,-2.180312,-1.769167,-3.423561,6.063932,-4.558564,0.213596,3.593265,3.668081,-6.960127,-3.748675,6.984876,7.568727,-5.943978,-1.599232,-0.517565,4.822568,-3.839976,7.454138,-4.699843,-5.082586,-8.151631,-4.307815,-8.864212,-6.083967,-9.251356,9.380368,3.534495,0.189880,5.636289,1.488891,-0.566528,-6.355104,8.395824,-2.766411,8.841745,-5.018524,-3.756290,0.982231,-6.415287,8.960123,-6.919907,-0.760331,9.438671,0.360729,-8.695374,8.083622,-6.354807,9.773164,0.672612,2.122172,-5.820099,-4.956964,2.148610,9.593766,7.497761,-3.297962,-5.080812,-8.682780,-3.143738,-1.584350,-7.340509,-6.936696,9.382469,-6.287916,2.312539,0.585371,8.168182,-0.892720,0.115184,-2.688262,-7.140707,-2.563475,-6.466870,-9.385279,9.793063,0.106805,-0.886630,-0.044510,8.838203,2.226231,-9.279045,-5.620193,-1.677710,-6.193826,5.566989,1.904231,4.964004,-9.365195,-5.925699,1.946365,1.528671,6.381707,-6.581631,1.699791,7.327489,-3.250189,-0.383725,9.857398,3.840012,-7.488166,1.910129,-2.261954,-7.087684,-9.209864,9.639273,-8.532765,-5.831365,4.440608,5.319570,-2.533003,5.843627,-7.031399,4.201888,-4.198303,-8.835877,0.257444,-0.383229,-6.819831,-6.336149,6.847719,-2.482951,-4.470610,-7.391297,8.526330,5.528973,-2.840526,-7.544835,-4.795566,-6.056530,-7.633310,6.538211,-3.628548,0.484436,-2.293871,1.101158,-4.870203,5.572094,-0.897557,-5.726952,1.278359,2.680846,-9.611012,1.143084,-2.005251,0.212157,-2.435301,-8.802576,5.629776,9.453312,-1.777667,1.709170,6.472253,2.997937,-7.201951,3.179563,7.337394,0.858040,1.525435,-6.734349,2.933012,-4.323083,9.549113,-1.506936,6.121314,-0.612944,4.181257,-2.217965,7.797772,-3.226996,2.081291,6.370874,8.807482,-8.504961,3.316537,-3.280206,-6.116025,-0.538715,1.459907,-0.642032,4.110481,-6.695265,9.273140,3.954585,9.279985,-4.302599,1.030672,8.959018,8.476462,7.247860,7.695562,7.189591,4.707553,0.690618,-3.310549,1.119927,-0.604460,-7.816030,-9.992552,-9.515254,-1.172908,-9.924115,7.381699,-3.990102,7.913633,6.587984,0.496696,-7.778372,7.536297,0.831234,-1.697534,1.748201,7.658316,-1.368709,5.185509,9.913813,8.206967,4.882539,8.540098,4.726809,-7.245818,1.247312,7.304263,-9.651141,8.200809,5.913656,-9.318469,7.504368,-5.777005,4.162411,-7.984766,1.684043,-3.346866,-0.036300,-0.759788,-1.450644,3.617209,-0.608000,1.877852,8.806621,6.810315,-9.795333,7.293481,2.302237,2.162958,1.875776,9.761251,-4.614782,6.646573,0.752760,-0.199940,-1.547318,-8.077000,7.989010,9.438507,-1.441702,4.778877,-5.813157,-3.413960,-2.061796,-7.345403,-3.433571,1.475076,6.325089,3.530306,-9.159645,-5.639123,6.217299,-6.592135,3.367522,5.976226,-5.126455,-3.358729,4.877816,-3.891064,0.506009,1.526430,-5.946452,-4.219707,-5.071867,-5.911140,2.689646,8.274562,0.270281,1.591207,-9.479487,4.279224,3.820691,6.053863,-7.223214,0.490400,5.036967,1.206414,8.518475,9.918239,-9.639323,-0.580987,6.201232,-2.255583,3.225674,7.989449,8.853089,-8.832177,-7.999082,8.050453,7.158504,-8.616760,-4.824783,-3.867222,0.262182,8.740695,-7.216702,-1.735694,7.824004,-4.487896,-3.530297,-7.196312,-8.906365,4.433443,0.181846,-3.944511,6.756687,7.505011,-2.883678,6.813750,3.803339,4.666217,-1.022479,4.909284,3.809311,5.464738,0.118153,9.561448,-2.335807,3.756302,1.543924,6.955246,-3.809163,-2.837197,-8.178774,5.937907,-2.318184,6.049174,-9.450773,6.383677,3.903518,4.138540,-9.442420,-8.731291,6.255142,-9.223054,0.839479,2.205429,-5.978178,5.308175,8.975795,6.583207,7.642892,1.930262,6.071482,8.594885,5.800911,-3.098874,7.452456,-4.787118,-8.858988,-1.321341,-0.468228,0.035721,6.945123,-0.265896,8.942455,2.539251,-1.337791,-6.879244,4.168181,-9.335897,2.730563,-2.747493,-5.537669,5.244258,-4.875715,-0.349987,-3.781404,8.624691,-2.996640,-6.302609,4.941792,1.303580,-5.757515,-8.529661,2.800357,-5.757189,2.072825,-9.056555,-3.663477,-5.817749,5.108134,3.111341,-3.339996,1.360600,-6.016710,9.540709,4.551829,-4.378868,-3.380867,4.428105,5.627595,-7.498612,3.390131,-1.081628,4.208868,-2.519827,-9.210445,-8.126133,-9.073179,4.482056,3.224694,2.151380,7.421828,3.848799,-0.249223,-8.444141,-7.363586,-9.298366,6.365051,8.776067,3.399945,8.031657,-1.137464,-8.647166,6.788124,4.025913,-5.520541,-1.532448,-8.693716,-9.594069,-1.452226,5.646750,3.601107,-9.118457,-3.751436,1.878997,4.423066,4.061682,-0.544445,8.005175,-5.483974,9.676167,5.722151,-8.700013,2.857201,-2.237161,3.928918,-3.835107,6.734585,6.173365,4.812002,5.840823,5.798512,-9.392983,-9.219233,-0.643846,-0.337597,-7.664638,4.244233,-1.260772,2.764162,-2.497293,-9.367001,2.679107,-7.472006,6.375539,-8.481707,-7.605148,-0.485995,1.329754,-0.838507,5.495361,9.322785,-6.819510,-5.651737,5.651337,3.631117,7.158948,3.100828,6.043225,7.690986,4.148706,1.504898,-3.902402,-4.607677,0.565067,7.354870,2.705102,-0.369823,2.331423,-8.100273,-1.591851,-8.929717,6.154963,-2.358123,9.178224,-2.751356,1.816943,7.481872,0.449051,-3.064030,-3.787949,5.557630,-9.736417,-5.885509,-4.294286,0.744452,-7.372518,-5.687120,7.877344,1.567489,6.041564,4.500218,5.972939,-5.522891,-1.280768,7.427045,-1.290659,-5.220214,-6.585642,-4.553087,-9.656615,6.433866,2.034905,-0.788622,3.731553,-4.943860,7.712596,6.633387,-1.874867,4.521164,-4.768860,5.534980,8.851597,-1.435123,-2.814501,9.030554,-2.673681,-5.782893,-2.506547,-7.709001,-3.527064,-0.386296,-6.270697,-0.563026,8.348675,9.440119,8.212251,-2.024759,-1.886409,-6.824573,7.527650,4.839706,2.852796,-2.941832,0.821071,9.948229,2.461297,5.499955,7.517002,-7.763424,-3.906755,2.013205,-0.551755,-5.720926,-2.846385,-9.982398,-6.325825,8.431308,1.353952,-4.459931,-5.537258,-4.376106,6.257452,3.855658,0.171246,-7.659250,1.383682,5.467466,9.900005,-6.132804,3.894132,-9.550220,2.788073,8.460312,6.987022,8.600295,1.134444,1.693782,2.103610,5.016802,-2.400656,-7.017344,2.170126,0.251714,-8.412608,-6.215787,-6.789437,9.127906,-2.144411,-8.767932,-3.005481,6.835405,3.964792,7.430411,2.740003,-0.651470,-6.376381,2.971962,-2.520360,-2.713366,7.766179,-6.664062,4.373987,4.197016,-3.215950,4.251040,5.277577,-7.127463,2.032422,7.843221,9.538436,-1.043928,3.135059,3.347935,8.655029,-3.385940,7.353636,-2.203179,-7.572663,-7.262586,-9.502956,-0.905492,7.107374,-1.305034,-4.675258,2.892558,7.801993,5.625621,-8.359210,3.354419,-0.100074,-0.114460,-4.231207,4.104255,-7.083946,-8.583635,3.317042,-7.030390,8.936340,-5.583513,-8.897226,8.402989,3.787688,-6.910587,-5.207173,2.656831,3.711243,-6.264596,0.747280,3.098234,7.814524,-1.094350,-8.466886,4.563439,5.580396,8.329860,-4.227000,-4.154939,0.383316,5.779594,-5.735816,-7.931658,-8.955358,6.131856,-8.871864,2.436394,-0.622388,0.302141,-5.615230,4.533701,-1.677039,7.059354,9.085558,-6.029215,2.673715,-6.194042,7.653052,4.791271,8.911472,0.860173,3.594275,-8.458476,-9.949658,-5.723644,-2.913451,-5.645328,-4.531512,2.675914,2.526798,-0.387807,8.560489,-8.565605,-1.929749,-1.518323,6.989290,6.067525,-0.207518,-8.299705,0.448869,3.549764,-0.768231,-9.605893,-0.505846,3.192662,-7.026319,-8.565298,-5.785167,-7.594171,-0.324531,5.770889,-6.734078,3.361856,-5.166189,6.459074,-0.796050,0.830635,-1.783510,-1.404883,-8.699877,7.968332,9.245220,-5.726538,-5.239227,-3.204796,-5.722549,-0.260748,1.937871,1.066268,-3.118874,3.180295,-9.333824,7.821226,2.210400,9.816661,7.684237,-2.424190,-3.421627,7.217269,7.491563,4.344345,9.075085,-1.051885,5.249594,-0.548778,-3.446868,3.345082,-1.890677,4.330346,-8.859767,6.744519,4.746070,-6.248711,9.950719,9.625780,-3.754116,-6.326042,-1.555474,-5.204712,-0.729077,7.461301,-4.091902,2.312637,-6.261143,-3.562226,8.182241,-8.378573,7.774434,-2.717220,-4.777001,3.686635,6.632173,-8.724398,-6.692477,5.222500,2.427876,4.758320,2.599900,5.341158,-6.835202,-2.641251,0.111176,-1.013889,-4.103145,5.464039,-5.368622,7.808239,-4.343125,-0.773760,-3.392548,-8.914846,-4.009401,4.525641,-4.223797,0.082893,1.774785,7.129670,8.593013,4.170252,-3.271678,-3.389510,-2.033967,-2.075861,-0.538204,4.845256,0.170316,-9.394989,-3.303451,6.709731,-0.995895,4.357057,5.120817,0.446955,-7.381177,-0.182973,6.014096,-9.995561,-9.148154,9.679664,1.041372,6.842232,-3.260961,-8.593931,9.527338,0.775666,4.333333,3.273465,0.048332,2.974989,-5.759765,2.691575,-1.734794,6.495480,-8.749407,5.962590,3.769560,-1.658279,1.815165,-3.327555,5.770204,-9.615290,-1.555409,9.109802,-7.277955,-0.431155,-9.096479,9.608468,4.404624,4.846703,0.994793,1.721787,7.925955,-7.272079,-0.699594,0.961287,-7.567258,-5.024054,-8.257547,3.250707,-6.966045,5.740116,5.336536,-9.505540,4.166528,-7.468141,-4.726605,7.632221,-7.190559,-4.718482,6.702099,-8.401460,-1.394127,-1.629405,-2.601084,7.034021,9.093079,1.429820,6.669796,9.972233,9.766802,5.792960,5.168609,5.744817,-2.089425,1.945591,5.351996,-6.095487,-5.210580,-6.807445,-1.854422,-3.686698,-4.275077,-9.445013,2.279692,-7.421554,7.774100,-5.756809,3.734309,-3.981149,-0.735488,8.366152,3.924747,0.840900,-4.332253,-7.541262,4.021146,4.003572,-5.884848,-3.219649,2.174314,-7.055948,-4.680482,-5.155269,-3.346041,-5.835464,-5.313458,0.694738,2.232057,0.439717,-3.683327,-8.771911,-6.526946,-4.949549,6.200648,-9.995779,4.813542,4.532923,-0.987253,7.644772,0.954808,6.315246,1.398708,5.634849,1.076528,7.533133,6.051057,1.383962,5.557775,-0.220215,-6.748273,9.257156,-0.238017,-6.030736,-9.441496,2.166770,7.061980,8.503504,7.731207,7.798786,-7.134340,0.502157,-1.137519,6.411483,-2.519738,-6.232701,4.664712,-6.945062,-6.955919,-1.319081,7.064423,-9.401088,-2.932088,1.262510,3.303505,-8.213126,9.587356,9.579425,-6.576758,4.410692,-5.536200,-1.975478,-2.207987,7.772690,6.376382,1.223568,-0.718353,8.010687,-6.356377,-4.638963,8.918106,1.368697,-1.215492,-3.734723,2.332529,0.312525,2.803937,8.150827,3.852577,-1.062016,-0.370025,3.534880,-8.738099,2.525447,3.892779,-3.055535,-9.629155,-0.086604,-9.907913,-3.791650,-4.345489,5.403644,0.056742,9.893105,-8.911276,3.291040,-3.930906,4.431809,9.876055,8.190651,-4.175535,6.535919,7.368361,-9.884683,-0.508452,9.457024,-2.568683,-4.520172,-4.529824,-6.664096,6.812570,1.640457,-1.460883,-7.348388,-3.996899,1.149375,1.457179,2.316683,-8.684242,-4.064097,-3.748830,8.201112,9.747135,-7.739056,-3.203897,-5.829203,-8.552959,3.980266,-5.928349,-5.585318,0.823343,1.381703,-0.024454,2.545055,-3.348947,9.940574,9.793925,-6.667733,-9.208691,-2.500415,6.578173,5.233755,1.298115,7.380111,-9.569884,-2.729784,1.310112,5.861149,-7.646535,-7.641430,-9.240952,-1.301415,-7.252072,-3.057540,0.910129,0.473537,4.064586,9.886580,7.603631,-6.394898,-8.834295,9.880267,6.788996,-6.237845,0.983416,-6.423544,-5.425218,-5.908335,8.256638,-6.109838,8.712705,-3.132485,-3.208032,8.140410,-6.165236,8.138719,-1.957335,-4.129478,3.795672,-9.605800,5.789406,5.515090,6.747519,-3.176753,-4.847295,3.676385,6.063031,3.990873,9.957396,2.918014,-2.900960,3.455042,-4.539058,-8.887249,-4.063502,-6.717098,-7.879676,9.211949,3.261673,-2.034414,-0.047748,-3.596575,8.405854,5.133807,-2.667970,-3.994778,-2.099672,-2.230930,6.081365,-2.469971,0.865436,1.853929,-5.996313,9.373451,0.710319,-8.243329,6.985952,3.935753,-1.409971,-0.937404,9.833545,9.187617,-9.379675,-3.175233,7.161018,4.001480,-1.845015,-1.777276,2.841992,-1.520498,1.490467,2.541387,8.291512,-9.773866,2.413401,7.625269,1.031694,-7.156366,-1.218146,-1.825081,-7.264007,-1.630441,-1.401082,0.464394,-7.435926,-1.706011,-0.709974,-7.689578,-9.346040,6.980735,9.514237,2.174490,-4.622684,-3.344577,-7.948046,-3.753820,-6.347799,1.157952,5.605493,8.779488,5.748316,9.511406,7.062482,8.544258,-5.694404,5.071981,5.816850,2.141993,5.695515,-4.896510,-4.422920,-6.087109,4.859006,2.447873,-6.600972,-2.898646,4.885125,-8.508174,-8.686499,-8.700784,-5.527487,-2.429150,-8.936745,0.867427,-9.146817,-3.454261,-6.011106,0.550546,-1.124701,-8.407445,0.100762,-7.733614,2.405668,1.323768,4.358166,-2.612358,-5.885517,0.514405,-3.123911,-6.360317,6.451911,5.030326,5.310153,1.332185,-1.106525,-9.722226,6.185118,-1.506796,6.669952,-6.559280,2.913575,2.954988,2.439981,0.386755,8.652904,-4.978745,-3.866198,8.303926,1.482923,6.754576,-4.062238,3.081880,9.135008,-5.475514,-6.738362,7.508945,-6.500081,0.256398,4.225641,5.274649,-1.835389,9.844661,-1.494201,-9.842584,-5.365582,3.426551,5.361482,-9.319353,-4.932435,-9.859357,3.622609,-0.514157,-8.753590,1.301009,-2.313524,-6.933838,9.471497,2.446930,-9.480279,0.751259,-6.340220,-4.445304,1.123759,-5.692557,2.843337,-5.136954,-5.772220,-9.177889,-5.386908,-6.496411,7.518152,8.818265,8.142067,-7.872790,-4.443439,-6.000125,-4.296450,2.630138,3.036644,1.278565,-0.927794,0.887466,-3.915519,4.188137,1.485552,-2.806892,-8.626093,6.452033,-9.957053,-5.971472,0.544600,3.909180,2.779258,-0.678316,-3.429502,0.846270,3.959646,3.077050,0.492224,3.882119,5.289123,1.696744,3.526652,1.033087,-0.802614,8.065805,-7.695893,5.147617,4.612490,-0.448318,5.427906,-2.340338,-1.362221,-7.107267,-1.673143,-7.553343,1.187527,4.511763,5.465676,2.511155,-8.373933,3.717265,1.581079,-3.744539,-0.973627,6.898019,4.679195,3.334967,9.653424,7.400579,3.272996,6.357024,8.456003,6.596144,4.821760,-9.112911,2.369840,-3.914105,-7.260696,1.644223,9.215762,-7.624003,-9.047951,-7.472701,3.253435,1.086902,-0.268195,-2.167582,-8.460696,-5.472332,-4.527690,8.874441,-0.100433,-6.954445,4.039699,-6.794231,-2.464041,6.469667,-0.839041,2.072336,7.116585,-4.698184,8.663696,8.761782,-7.912888,-5.105248,-2.059884,7.183886,6.238615,3.226940,8.251397,-4.544125,-7.536195,4.769304,9.983551,-0.526409,7.778188,-3.416915,0.719582,-8.347031,2.747034,-2.756364,3.637494,6.313369,-3.897001,6.917548,-5.296660,8.827762,6.304519,0.965525,7.835195,4.315520,-8.863754,-2.690359,5.718195,8.674752,9.201773,-8.048417,7.587999,1.543292,-9.497308,-5.267930,-1.665025,0.917874,-3.769903,3.324230,-2.199637,-6.152993,-6.845543,0.015119,-8.654671,4.212899,-1.782054,-3.895750,0.573205,3.060941,-9.752965,-4.576089,-8.741240,-1.694076,-6.109835,-5.713766,-7.895730,1.360321,7.068705,-4.196558,8.323564,6.415415,8.940134,-6.629445,-7.695273,-5.531834,1.070064,8.814391,-1.685099,-8.463074,2.108752,9.096763,9.093972,6.294768,8.134628,-4.787662,5.910448,1.136690,6.141857,7.522429,8.716816,-1.415854,-6.553841,-3.839714,4.524348,8.547423,-7.296422,-2.039288,8.719761,-8.131113,6.623921,5.917159,8.903289,9.262501,-7.258027,-1.798016,-2.510815,-4.994594,-0.730719,4.365768,1.713316,6.670082,-9.975679,-6.240172,4.460335,-0.829620,5.243307,7.909885,-1.764364,-3.195566,8.047844,0.696801,4.386328,-1.288163,-4.782767,-5.581744,-4.327976,4.399782,2.052691,-7.557729,2.631489,-0.055825,-5.433795,3.054324,-2.086179,-8.443800,-8.347166,-3.218227,1.603146,6.802045,-7.767520,-4.072379,1.893727,2.167864,1.983622,4.434150,2.419396,0.625429,1.278508,-2.893697,-8.317377,5.325011,-3.391926,4.863216,-8.816442,-8.680789,-3.460718,9.777232,-3.259836,-6.344511,-3.575360,-8.841385,9.253623,-0.360693,-8.822372,1.175236,2.884390,5.514732,-0.142092,7.472295,-4.157646,7.399796,-7.709198,-6.420183,-7.726281,-1.110289,3.401348,-7.579860,1.915918,8.966737,0.407493,-1.645499,-1.635251,2.741358,-3.239245,1.449429,-4.896219,9.250334,-9.125771,0.688188,8.928635,4.454555,1.824608,9.589713,-6.450978,-4.523510,3.372931,-4.161699,3.319925,-8.703618,9.977813,-2.753159,0.601861,-0.224058,1.566046,-2.826041,-8.645875,4.261994,6.680883,-9.430168,-8.495818,8.123419,4.800612,9.428772,7.141079,8.737434,6.850790,-8.671929,7.604158,-2.450306,4.789112,9.697833,1.038702,5.490040,-4.187766,-5.836006,-7.103159,-3.816579,-5.182402,-4.831025,-1.201186,-4.563048,7.590336,-9.830789,4.785325,-1.019198,5.962459,-8.335718,-9.496308,0.901193,2.141862,1.275979,2.856626,-3.904364,9.484145,-7.622822,-9.956491,-1.907652,3.421114,-4.069547,2.424423,5.052989,9.055472,2.449611,9.919433,-2.075226,9.666830,3.930179,2.905277,-5.363571,-8.229433,-8.916825,8.559454,3.672032,6.116737,3.917203,-1.961775,3.160235,2.788403,1.366425,0.103620,8.681733,-1.229928,-9.881226,-8.589452,-4.999739,5.709146,1.955664,2.287784,1.112372,9.555968,-2.092509,-9.372837,6.023353,-1.913256,-6.125716,-4.780974,-8.393121,-3.624769,-5.258936,9.532127,-7.645862,-4.998898,2.211984,-0.381211,-9.839100,-9.469755,5.007163,1.364936,-3.188756,9.101446,8.792322,-3.426088,-7.568834,-2.787744,-0.874021,-7.540098,-0.780243,-0.913407,-2.912617,5.071217,-5.973179,8.978041,-1.541978,-4.784216,5.210424,9.119544,0.860442,-7.760494,7.070349,4.237839,3.485413,-9.061634,-0.687803,3.604836,3.748633,5.638467,-5.214484,1.504979,4.060283,7.828202,9.707637,-2.228089,2.744075,3.411802,3.452894,-3.150093,-1.564583,0.168452,7.090953,4.451375,0.369267,6.660357,-3.879797,-3.309144,-7.797629,-4.299365,-7.078525,2.097276,2.620584,-5.129580,1.966642,0.821696,9.269821,-8.331608,-1.358079,4.695447,-1.371321,6.730808,3.139238,2.712758,-1.005976,-2.107867,-0.049815,-3.299601,-4.410177,-6.995647,3.135987,5.096637,-6.217757,8.910335,6.893083,-7.226911,1.278730,-2.274885,7.426481,4.315131,6.722187,1.626965,6.661418,-8.956557,-4.531549,4.788547,-1.380299,4.294584,-9.734906,9.555466,1.967186,9.266817,-2.460314,-3.801323,2.510287,2.683315,2.952894,-1.909972,-4.979488,-6.466844,-3.668076,-5.001409,-1.118227,1.231789,-5.257270,-1.154735,8.301544,9.792359,-8.573355,6.755545,5.224693,-2.734089,1.016301,6.745709,2.610790,4.255633,0.691789,9.815462,9.293433,-7.697277,1.013401,2.502061,-0.040855,-6.927607,-2.749243,8.367447,-3.469346,-3.516340,-8.652824,6.159193,4.827278,0.277282,-5.722751,-3.419199,-0.611912,-7.119557,-8.688627,-8.630780,-3.434871,2.308956,-1.617520,-7.827519,-9.838438,0.955592,-0.128076,7.586466,7.704651,-2.408965,1.677575,8.977212,7.320128,6.449518,0.438383,-1.086819,0.938684,6.636981,-4.840362,-4.407877,-2.831543,-7.383674,6.437652,4.210429,-5.682019,-5.581790,-6.292377,8.071851,6.348744,9.628216,-6.984717,-2.335960,9.926091,-9.943510,0.110693,5.187153,-8.191897,-2.167699,6.869155,-4.133228,9.976321,6.832008,-3.194964,1.194987,6.816729,-8.734253,7.514695,0.657476,-3.500956,-1.966322,4.600682,-1.625619,8.373327,9.522067,-0.524271,2.415509,-2.833877,5.580778,5.707795,0.393934,-4.890360,9.285691,-0.379309,-0.828921,-5.278747,7.506319,-2.420049,2.938801,-6.881403,-4.544368,-9.784715,9.424883,-0.084110,5.679821,2.334952,6.244294,-3.519683,8.602592,1.261624,-5.206449,8.155716,9.015429,2.673740,1.411927,6.122451,-2.308472,6.600119,9.436045,-4.391269,-7.614063,2.982514,9.128407,-4.140812,-8.550704,0.842029,0.998099,-2.525753,-5.869347,6.023101,-5.426810,-0.240196,-2.209101,-9.389241,9.786642,-6.388913,-6.233321,6.053132,3.013435,8.834280,-8.631196,-7.256979,9.423367,-5.072868,-4.875654,3.590360,6.605399,6.072197,-7.529639,8.232744,0.698021,1.732530,8.505655,9.972894,-9.462828,-1.242002,7.185364,-9.879073,-3.648520,9.282334,-2.845325,2.776111,-9.625289,3.500887,-1.502676,-5.688235,-4.858735,0.041809,0.338932,-6.403894,0.775402,-6.917048,-5.296954,8.227994,7.047101,9.042437,-0.596310,1.420091,-3.431269,3.005404,8.162341,-4.470388,6.308628,5.126549,-5.189023,-1.459912,3.660791,5.651993,7.190384,-0.130517,4.475675,-2.754257,-0.273924,-8.116712,-0.514466,2.142012,5.838855,8.620398,4.741963,4.348917,-7.025793,-1.057771,-2.012715,0.834739,-0.971850,0.354746,-3.379446,0.373942,4.429876,6.443505,5.993161,-4.622288,-9.868906,4.200129,-9.233889,0.770625,-9.684023,-6.601136,3.138889,-0.724253,3.325874,5.110301,2.513101,-0.965115,-9.284769,-8.909308,-6.848893,6.132993,-7.001130,4.686943,0.531510,-6.284568,-3.672140,2.312956,-6.477418,8.657195,1.376622,1.542318,-0.174400,9.112965,2.643476,-9.109869,-6.015579,-1.306408,2.759890,-6.859999,5.093560,-3.312143,4.198286,3.182227,-5.286155,-7.147617,-9.213402,-4.351107,0.811891,1.410451,-6.516414,7.339636,0.011152,5.186672,7.865560,-0.970913,-8.398396,-6.015134,-9.563999,-1.038801,-5.253414,-1.397827,-1.695280,3.141445,-5.803497,6.107828,4.967889,-5.622316,-5.261494,8.303036,3.751885,-4.128661,-2.333009,3.652349,4.006783,0.076667,-5.874727,-4.088344,5.537394,9.807052,-9.276056,-8.544714,0.629734,7.205708,-9.160042,9.698451,-4.901151,-3.122382,-2.590715,4.498682,7.836990,8.535101,-6.588989,-1.427374,-7.980600,3.948484,-0.099746,-4.308707,-0.166159,-8.509731,-5.630456,-6.320989,1.055588,0.778987,3.033214,2.507826,-3.178316,-3.241375,-5.654725,-8.859345,-4.251081,-3.748217,7.346846,-2.720129,-0.133438,-1.822879,-2.315331,3.343677,0.089463,7.774216,3.656338,7.404964,-4.411634,-4.638946,3.480809,9.070799,-0.966449,-3.539500,-8.663329,-2.304760,9.737844,2.871306,2.292545,-0.738873,7.485498,3.754612,-0.207828,-0.123341,4.328312,-0.088723,3.340762,-1.403838,8.679824,6.435937,-6.605761,-0.194635,0.077665,7.155744,-0.499795,7.198082,-5.340437,-3.113450,-8.292079,5.353079,9.335673,-4.430925,2.793842,-0.501790,0.153410,-9.926798,2.805073,-4.878201,-7.219944,-2.836152,1.412452,-4.734231,-7.719275,-4.438820,-8.253970,-6.200944,0.696719,-5.842730,-1.239906,8.434280,4.750224,4.694373,-0.998347,3.067841,8.036735,8.863837,2.622199,-0.160048,-1.108312,-3.226305,-9.689060,-6.873234,7.589201,-2.529848,-6.191565,-8.152113,8.803882,-6.903204,9.366592,-7.346290,1.807226,8.766407,-6.592183,1.652571,-6.719712,8.675404,-0.761520,7.746837,-6.366479,3.149225,7.683544,-1.482347,1.142306,1.578588,-1.888653,-0.630810,9.853518,8.346281,4.447387,6.401696,-1.687140,8.987690,-1.769411,9.847668,-3.788015,2.480861,-7.908521,1.036301,6.982834,-4.993006,-1.349195,7.210943,-1.089181,2.608142,7.525880,5.497280,2.212697,1.678833,6.120682,3.665660,4.636814,-7.491873,-2.567560,-1.720828,-1.180770,-9.165691,9.183094,-2.522491,-6.413279,8.723887,-5.783149,4.168015,5.734904,-1.223428,0.302155,3.586014,-6.811000,-7.368628,8.931651,-2.863348,0.735972,-9.434415,7.189069,-5.334776,8.518996,5.939026,2.673974,3.976862,3.292534,3.061365,5.634966,-1.904316,-9.323814,5.099533,3.688340,7.893849,-7.998643,1.983517,2.268185,8.321563,8.553843,-0.175903,7.139989,-2.774459,4.036386,-7.619737,-5.482985,5.248617,6.761261,-6.228353,-0.232296,-6.821532,7.616152,-7.651278,3.794554,4.107961,4.598384,7.499174,-5.415789,6.696026,-4.342580,-5.408887,-0.973123,0.260275,-3.856757,-8.766716,-0.563295,5.802403,-6.612484,-4.395418,1.545497,3.225427,1.680918,-4.333735,-3.452237,-7.151990,6.973308,2.128343,-5.831084,5.716415,-7.226212,8.246440,-9.209147,-7.212498,4.016332,1.041536,9.959273,3.466103,7.953061,-9.127552,8.149740,-3.880390,6.701440,1.621716,7.417933,8.975865,-8.223532,-8.472048,1.287295,-6.310604,5.157398,-5.871551,-0.452800,4.618657,8.649813,9.214544,-0.836667,1.576278,3.277231,3.626897,2.329388,-0.244274,-0.870017,7.064221,8.518746,-4.099135,9.293488,1.402587,-0.915632,1.180670,-1.374233,-5.053388,2.242845,1.900939,-9.208161,2.533708,1.917358,-8.927940,-0.872263,0.991582,7.680645,-3.492131,-5.548065,-2.616682,-8.835037,-6.349893,-9.036134,-2.637840,-8.402665,-0.888181,-6.589345,6.591019,8.928701,1.864369,5.409676,9.974240,-1.420415,7.353427,-6.955623,8.634940,2.361128,5.801089,9.750234,2.405920,1.610496,-6.605953,9.433531,9.553206,2.245675,-5.160223,-9.129925,9.393166,7.592471,8.705380,-4.498444,2.524360,6.115751,1.503028,-4.677650,-8.008728,-9.098569,1.075857,-8.125902,-6.624281,-5.226301,-0.288581,7.972812,7.383398,-9.601015,-9.631118,-3.048375,8.791103,-5.014453,-0.368502,9.433885,0.039652,2.014303,-1.296725,1.831152,-5.711385,0.981189,-6.905364,-0.860869,-2.268573,9.154482,-2.701577,-3.437311,4.328433,-7.248107,6.104122,-1.414062,-7.207084,0.377588,-8.205630,7.645410,-0.979973,5.859142,6.913632,6.510683,7.887921,-4.743396,-5.005703,2.878420,-5.417417,8.710707,5.114356,-0.222864,6.552380,-6.830098,-5.873125,-9.345917,9.640809,-8.437417,-7.219053,-2.570686,-7.433340,4.976427,2.706693,-5.769888,-7.413724,4.317892,0.891888,0.463357,8.906317,-6.626525,-0.796914,5.242256,4.164378,-4.087152,5.357038,4.398319,-6.333364,-8.123038,2.384919,1.412080,-1.990909,5.591700,-0.049958,-0.383369,4.075956,3.556903,-5.050314,5.213454,-7.052004,0.789702,-9.037113,7.569212,7.224132,-9.765619,-0.423048,-5.553910,-9.416198,0.411454,6.423607,-5.385257,-6.677976,-4.489505,-4.576756,-7.602223,7.044957,-7.438559,-0.693666,-9.552829,4.104719,-0.943895,-5.277030,-0.398124,8.616643,9.459189,-5.928467,0.203367,-9.163964,9.016426,8.300860,4.439970,0.990527,-3.553492,-2.492333,0.484350,8.807609,2.042428,-4.048651,-1.252809,2.392763,-2.690183,1.125108,3.290027,7.186782,4.092709,-5.775372,-2.663853,-6.288395,-4.659390,0.172658,0.344652,8.466685,8.074138,-1.732832,9.210847,9.573246,7.675040,4.882276,-9.581768,8.263457,8.369615,0.386789,3.462864,-1.032071,-6.581080,0.099013,-7.850873,-1.956438,3.634933,2.914852,7.007874,-8.914769,-5.248766,5.795012,7.547160,-2.125047,-1.132361,-0.857735,7.371419,6.310513,-2.735623,4.950081,-0.547578,-2.191536,5.513623,-7.465681,4.467347,1.001205,6.382547,-2.863733,-2.988682,1.347957,-4.717101,-7.153559,1.059993,3.376271,7.953875,-0.986070,3.160258,1.621987,2.142772,3.725422,-5.594630,-7.243440,5.982805,-1.113218,7.487497,-6.457162,4.957505,4.831244,4.444750,7.213508,-6.527363,-2.515315,-9.361690,-2.379218,2.036121,-3.149925,-7.909695,8.324594,-6.669138,1.353806,-9.263457,5.325746,9.772641,-2.750590,-5.422430,6.570645,1.476546,-2.892896,3.256834,6.878370,-6.812654,-8.008101,-5.645392,-0.471833,-4.369562,-5.529039,0.563977,-1.287544,7.963036,1.845129,-1.135872,-6.123647,-6.085744,-4.339295,4.725443,8.865333,0.265180,-2.897636,5.471472,-3.878922,4.113184,-9.910585,8.543593,4.954309,1.473503,-4.737105,7.189684,-7.923550,6.345172,9.973772,-8.215703,-8.928485,-3.916504,-5.167898,8.677085,3.024406,9.078759,8.498462,9.263863,8.819917,-7.609963,-9.599517,-4.679825,4.143351,8.581823,-5.636511,3.945643,-2.489668,-7.291401,-1.806074,9.297187,-2.110450,7.444729,4.599538,-7.756670,-3.759442,-4.948175,-5.871712,6.421757,-1.730996,-6.884378,-7.236369,1.260134,7.824204,6.828510,8.230372,-2.422704,-8.060355,-9.917148,-3.390492,-4.223448,0.856530,7.102126,-7.071390,6.980117,-9.798782,9.239142,-6.991816,4.498982,-5.372520,9.329388,5.829615,5.358274,5.523129,-4.106039,-2.748590,-7.196822,7.486664,1.690382,-5.264441,1.906137,-4.856672,-0.327304,2.431119,2.523165,-9.694807,-3.519291,-9.553384,4.415019,1.889207,1.462303,8.938175,1.904436,5.871193,-6.319532,7.137774,-4.904300,-5.798498,-7.026326,-3.240665,-0.544856,-5.862042,3.209570,-8.687511,6.828105,-4.381579,-6.061908,-7.136220,-8.823618,-4.022044,-9.065507,-4.492958,-7.094782,5.439920,7.906575,-2.557794,-6.031761,-3.604659,4.873987,3.813432,-6.401446,3.357165,8.549266,-4.022384,8.578798,-9.357314,-4.762815,8.912679,6.605155,-4.726740,-1.788638,-3.583632,4.602221,-5.306052,-4.418878,7.169724,7.354606,3.450703,6.624748,0.100193,-8.036433,-9.406307,-1.664234,0.511891,-4.371163,-5.467284,-4.073572,4.579737,2.559791,-8.765531,9.484075,-9.162437,-9.058553,6.707940,3.743379,0.212880,-5.349645,4.859339,0.797051,1.777740,-9.287721,-8.068907,-0.914536,-8.294551,-1.686411,1.683867,8.870949,-7.299866,6.221674,7.677471,-6.933288,7.129086,-3.142689,-6.044230,7.553923,2.773486,1.337167,1.363956,0.662918,-5.232369,-7.594556,-2.701886,4.306331,-6.805445,-1.407055,-5.996520,-4.426264,-6.625949,-3.519579,-0.124132,-6.423128,7.488054,6.816929,1.399825,-6.849156,-5.311491,-9.701145,-6.398121,-7.387615,-5.975087,-7.862144,7.234571,-7.040116,9.792964,-2.435232,0.777447,5.846497,3.636934,7.904278,-2.500626,-6.517646,-8.964017,3.881013,-8.850909,2.480116,-5.386679,1.857420,-8.312899,5.431649,-8.106132,5.965261,-2.869362,-8.197873,-2.345763,8.618249,-4.839218,8.926187,-4.578221,6.203825,-5.094794,2.464475,6.242577,6.186270,5.523367,5.961588,-3.194998,6.896905,-8.789380,-1.285231,4.484489,1.379246,0.465256,-7.651342,7.966882,8.760860,7.709384,-4.923709,6.712990,-5.672535,9.916502,8.750333,8.036854,-8.647762,-4.360575,-8.710575,-0.026075,1.217004,-3.463388,4.349644,-0.232966,-7.340941,-2.267547,-1.517266,-4.734540,-0.507296,-8.460982,3.719638,-0.994446,5.052045,6.994798,-4.198576,0.497023,0.346170,2.187100,7.373821,6.412717,1.760095,7.150790,-8.247306,8.093889,0.545783,-9.167165,4.687344,-8.059960,1.634352,-7.818141,-3.570620,-5.744882,0.887059,-6.341525,1.881367,-3.062810,1.168704,-3.410197,5.052370,-8.257045,4.854048,-0.166215,3.497715,-5.675056,-2.804599,-7.509025,-4.846814,-8.722952,6.610077,5.802307,3.054017,6.437363,8.554754,-2.070447,0.998293,2.793852,1.760572,5.765627,-9.087495,5.772698,-8.352347,3.652913,-0.018977,0.999073,9.630677,-1.356210,-9.140897,0.329596,5.668673,5.464670,1.434287,-9.324507,-5.747918,4.880742,7.632549,1.129834,9.530072,-1.483127,-0.741476,5.462204,-5.277556,-3.076906,8.371450,-2.942733,6.808784,-9.165530,-9.073421,4.128079,-7.088863,-2.540579,-9.107771,-9.006699,-0.333396,8.241916,-7.755179,-6.821404,6.280815,3.393854,2.232353,5.839157,1.792109,7.920792,-0.428053,-1.107462,2.742482,-6.593399,-7.777907,9.651152,-6.767569,-0.721608,1.149861,7.990127,7.255565,-2.532116,6.048502,-4.463565,6.795370,-2.559940,-7.526614,-2.134139,8.287257,8.081475,8.448578,5.538352,-1.738611,-4.185773,-2.143435,-7.765802,9.765280,-7.154078,-9.565074,6.418396,-0.699436,-9.993305,3.833673,7.688355,1.627266,-2.845926,7.600619,-0.660176,4.133856,-5.786393,4.679711,-6.367331,5.362199,2.463127,6.891976,9.975323,-6.328626,-4.438154,-8.397030,0.466253,5.263986,9.000855,3.780000,-4.331839,-9.788989,-9.443538,5.637551,-7.942214,-3.433598,-4.059073,2.771997,1.405551,0.145264,7.406711,7.338740,-6.751862,-0.601090,-9.416674,2.860953,9.941629,7.085940,2.787196,-4.387517,8.955004,6.213674,-5.929171,2.204368,5.435541,7.505267,-8.771043,5.284176,7.747688,-2.418603,0.329794,-4.073764,-3.892191,-0.728937,-9.655384,1.084432,0.264813,-7.953159,8.552308,-4.472269,-1.360016,5.166434,-0.071575,2.901501,2.957145,0.515512,-8.246438,8.117998,4.877046,-3.514789,-3.081970,7.713556,0.773753,4.433634,5.770285,5.420701,5.831960,4.193372,1.551098,-5.620121,-6.262999,0.841465,0.014999,4.662349,-7.985420,8.489839,-9.653889,0.891725,-7.436230,-7.869753,-6.403012,2.445393,5.165129,8.983629,-9.314780,7.606455,-6.644580,4.488904,8.882899,-8.869200,-1.646219,-3.239460,0.352843,-4.711821,-0.654005,4.493509,-2.168767,-2.769808,3.578034,-0.305965,6.766408,4.954120,-7.423904,-2.308459,5.724633,-5.361308,-7.127927,-3.221789,-5.610780,3.969510,-4.155595,7.577418,5.780750,-2.643192,4.868826,-4.896381,-0.772192,-5.748430,-1.608391,-5.997849,-2.658469,-3.854973,4.714129,-1.098552,9.456388,-0.192997,-4.463112,5.568192,3.515378,3.138662,-0.485703,-2.890879,6.547530,-3.225041,9.590649,6.760612,0.600511,-4.084181,4.142265,-7.442210,-3.480087,-1.874905,-3.975636,-4.779145,3.425257,-8.656498,-7.051135,-1.706402,-9.520585,6.565727,5.275376,8.478313,-0.332478,0.334901,-7.195725,8.228055,-1.315015,6.641498,5.589259,-9.448228,6.224607,-5.653492,0.970802,1.542484,2.808525,6.119644,-9.200195,0.227133,-1.626330,-9.535566,-2.389306,8.251079,2.261432,6.005245,9.455888,6.780611,4.067935,-4.113083,-8.259524,-4.970919,-5.549052,-8.593034,-3.392955,-6.912366,-9.472009,5.966720,-6.895447,7.120160,7.871874,-3.816727,-2.351332,-9.014226,2.419578,8.836180,-8.047681,-4.881609,0.555342,2.664428,-6.513914,6.997789,-0.332808,-6.440794,6.443142,-7.742630,-0.401418,1.723955,-8.517419,-5.113724,-8.623256,6.579677,1.661690,-0.662714,-7.409527,-0.571199,5.336318,8.947983,-3.918545,-6.869220,2.918796,9.856911,4.888872,0.513417,-5.256646,2.491975,5.014808,8.990672,-3.251767,8.578744,-3.041277,-3.089364,6.583879,7.296066,0.691271,-5.807503,0.927341,-9.891838,-8.801996,-0.426348,-5.062343,-5.259545,0.636519,-8.048665,2.058266,-0.231584,-6.279704,5.170156,0.463127,0.473963,-3.180030,2.588645,8.594284,-7.212636,8.338418,-4.945782,-8.387760,2.209371,4.272682,-5.731426,-6.824130,-7.904156,0.245181,-7.500607,-8.562831,9.800425,0.384456,-3.936319,-8.450800,7.001448,-7.839191,2.991706,-4.957289,-5.248523,0.186895,-4.735313,6.512674,-0.940460,-6.723422,8.006255,-2.401857,2.941958,-3.718244,9.806276,-9.086238,-2.602433,-2.022587,3.399758,6.973144,-7.141864,-7.370739,-0.235356,7.491077,-9.965804,0.913702,0.747332,-5.743442,-5.974336,-5.328357,-6.675492,-6.121001,8.560406,-8.650353,2.788153,-0.072837,-5.195707,-4.106241,5.022424,1.418711,2.016531,0.259050,5.852347,6.599950,-7.474023,9.444194,-5.472268,-3.034543,-3.225314,-7.487881,-5.217541,-9.402264,-4.712596,9.259513,-2.503094,3.566202,0.378488,-9.540581,2.411207,-2.063725,-4.567657,-0.710685,2.920132,-2.332952,5.249897,6.074939,-6.420038,4.276051,-3.192134,-2.710016,1.159622,-3.994147,-4.916847,4.674502,-8.336842,-7.104977,9.350356,8.904826,2.587983,8.496310,8.580229,-7.311697,-4.382319,-7.501383,-7.778710,3.194857,-9.476192,-3.288223,9.668456,-6.050822,-2.777128,-1.548684,3.212279,-2.535807,4.485570,-1.592676,6.708402,-6.122583,-0.407592,-7.766364,9.056123,-8.443570,-5.851769,4.906136,6.990799,9.634660,-5.769413,9.976822,-3.309925,-5.786660,9.709931,-2.850386,7.470307,-6.473074,6.726240,-2.730539,3.000929,-9.680663,1.111071,8.848494,-6.715977,-5.868980,-4.690938,-4.096936,-4.143837], dtype = "float32")#candidate|4176|(10080,)|const|float32
call_4175 = relay.TupleGetItem(func_1486_call(relay.reshape(call_4156.astype('float32'), [1, 1680]), relay.reshape(const_4176.astype('float32'), [6, 1680]), ), 2)
call_4177 = relay.TupleGetItem(func_1489_call(relay.reshape(call_4156.astype('float32'), [1, 1680]), relay.reshape(const_4176.astype('float32'), [6, 1680]), ), 2)
output = relay.Tuple([call_4148,call_4150,call_4156,call_4175,const_4176,])
output2 = relay.Tuple([call_4149,call_4151,call_4157,call_4177,const_4176,])
func_4188 = relay.Function([], output)
mod['func_4188'] = func_4188
mod = relay.transform.InferType()(mod)
output = func_4188()
func_4189 = relay.Function([], output)
mutated_mod['func_4189'] = func_4189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2888_call = mod.get_global_var('func_2888')
func_2889_call = mutated_mod.get_global_var('func_2889')
call_4218 = relay.TupleGetItem(func_2888_call(), 2)
call_4219 = relay.TupleGetItem(func_2889_call(), 2)
func_3195_call = mod.get_global_var('func_3195')
func_3197_call = mutated_mod.get_global_var('func_3197')
call_4229 = relay.TupleGetItem(func_3195_call(), 0)
call_4230 = relay.TupleGetItem(func_3197_call(), 0)
output = relay.Tuple([call_4218,call_4229,])
output2 = relay.Tuple([call_4219,call_4230,])
func_4236 = relay.Function([], output)
mod['func_4236'] = func_4236
mod = relay.transform.InferType()(mod)
mutated_mod['func_4236'] = func_4236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4236_call = mutated_mod.get_global_var('func_4236')
call_4237 = func_4236_call()
output = call_4237
func_4238 = relay.Function([], output)
mutated_mod['func_4238'] = func_4238
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4245 = relay.const([[[-1.904695,4.381255,0.210155,2.695470,-0.003777]],[[0.127187,-0.329443,-1.055243,-3.399162,9.694533]],[[-4.038273,-0.461966,-3.093318,-3.589939,-6.718472]]], dtype = "float32")#candidate|4245|(3, 1, 5)|const|float32
var_4246 = relay.var("var_4246", dtype = "float32", shape = (3, 1, 5))#candidate|4246|(3, 1, 5)|var|float32
bop_4247 = relay.floor_mod(const_4245.astype('float32'), relay.reshape(var_4246.astype('float32'), relay.shape_of(const_4245))) # shape=(3, 1, 5)
func_1052_call = mod.get_global_var('func_1052')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_4252 = relay.TupleGetItem(func_1052_call(), 1)
call_4253 = relay.TupleGetItem(func_1054_call(), 1)
output = relay.Tuple([bop_4247,call_4252,])
output2 = relay.Tuple([bop_4247,call_4253,])
func_4254 = relay.Function([var_4246,], output)
mod['func_4254'] = func_4254
mod = relay.transform.InferType()(mod)
mutated_mod['func_4254'] = func_4254
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4255 = relay.var("var_4255", dtype = "float32", shape = (3, 1, 5))#candidate|4255|(3, 1, 5)|var|float32
func_4254_call = mutated_mod.get_global_var('func_4254')
call_4256 = func_4254_call(var_4255)
output = call_4256
func_4257 = relay.Function([var_4255], output)
mutated_mod['func_4257'] = func_4257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mod.get_global_var('func_542')
func_544_call = mutated_mod.get_global_var('func_544')
call_4329 = func_542_call()
call_4330 = func_542_call()
output = relay.Tuple([call_4329,])
output2 = relay.Tuple([call_4330,])
func_4335 = relay.Function([], output)
mod['func_4335'] = func_4335
mod = relay.transform.InferType()(mod)
output = func_4335()
func_4336 = relay.Function([], output)
mutated_mod['func_4336'] = func_4336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3565_call = mod.get_global_var('func_3565')
func_3566_call = mutated_mod.get_global_var('func_3566')
call_4367 = func_3565_call()
call_4368 = func_3565_call()
output = relay.Tuple([call_4367,])
output2 = relay.Tuple([call_4368,])
func_4371 = relay.Function([], output)
mod['func_4371'] = func_4371
mod = relay.transform.InferType()(mod)
mutated_mod['func_4371'] = func_4371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4371_call = mutated_mod.get_global_var('func_4371')
call_4372 = func_4371_call()
output = call_4372
func_4373 = relay.Function([], output)
mutated_mod['func_4373'] = func_4373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
call_4379 = relay.TupleGetItem(func_602_call(), 2)
call_4380 = relay.TupleGetItem(func_604_call(), 2)
func_3380_call = mod.get_global_var('func_3380')
func_3381_call = mutated_mod.get_global_var('func_3381')
call_4383 = relay.TupleGetItem(func_3380_call(), 4)
call_4384 = relay.TupleGetItem(func_3381_call(), 4)
output = relay.Tuple([call_4379,call_4383,])
output2 = relay.Tuple([call_4380,call_4384,])
func_4398 = relay.Function([], output)
mod['func_4398'] = func_4398
mod = relay.transform.InferType()(mod)
output = func_4398()
func_4399 = relay.Function([], output)
mutated_mod['func_4399'] = func_4399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3323_call = mod.get_global_var('func_3323')
func_3324_call = mutated_mod.get_global_var('func_3324')
call_4414 = func_3323_call()
call_4415 = func_3323_call()
output = relay.Tuple([call_4414,])
output2 = relay.Tuple([call_4415,])
func_4435 = relay.Function([], output)
mod['func_4435'] = func_4435
mod = relay.transform.InferType()(mod)
mutated_mod['func_4435'] = func_4435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4435_call = mutated_mod.get_global_var('func_4435')
call_4436 = func_4435_call()
output = call_4436
func_4437 = relay.Function([], output)
mutated_mod['func_4437'] = func_4437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mod.get_global_var('func_2824')
func_2825_call = mutated_mod.get_global_var('func_2825')
call_4451 = relay.TupleGetItem(func_2824_call(), 3)
call_4452 = relay.TupleGetItem(func_2825_call(), 3)
uop_4461 = relay.exp(call_4451.astype('float64')) # shape=(10080,)
uop_4463 = relay.exp(call_4452.astype('float64')) # shape=(10080,)
uop_4466 = relay.cosh(uop_4461.astype('float32')) # shape=(10080,)
uop_4468 = relay.cosh(uop_4463.astype('float32')) # shape=(10080,)
bop_4469 = relay.multiply(uop_4466.astype('uint32'), relay.reshape(uop_4461.astype('uint32'), relay.shape_of(uop_4466))) # shape=(10080,)
bop_4472 = relay.multiply(uop_4468.astype('uint32'), relay.reshape(uop_4463.astype('uint32'), relay.shape_of(uop_4468))) # shape=(10080,)
output = relay.Tuple([bop_4469,])
output2 = relay.Tuple([bop_4472,])
func_4474 = relay.Function([], output)
mod['func_4474'] = func_4474
mod = relay.transform.InferType()(mod)
mutated_mod['func_4474'] = func_4474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4474_call = mutated_mod.get_global_var('func_4474')
call_4475 = func_4474_call()
output = call_4475
func_4476 = relay.Function([], output)
mutated_mod['func_4476'] = func_4476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2556_call = mod.get_global_var('func_2556')
func_2557_call = mutated_mod.get_global_var('func_2557')
call_4484 = relay.TupleGetItem(func_2556_call(), 0)
call_4485 = relay.TupleGetItem(func_2557_call(), 0)
output = call_4484
output2 = call_4485
func_4494 = relay.Function([], output)
mod['func_4494'] = func_4494
mod = relay.transform.InferType()(mod)
output = func_4494()
func_4495 = relay.Function([], output)
mutated_mod['func_4495'] = func_4495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1270_call = mod.get_global_var('func_1270')
func_1272_call = mutated_mod.get_global_var('func_1272')
call_4507 = relay.TupleGetItem(func_1270_call(), 0)
call_4508 = relay.TupleGetItem(func_1272_call(), 0)
func_503_call = mod.get_global_var('func_503')
func_504_call = mutated_mod.get_global_var('func_504')
call_4513 = relay.TupleGetItem(func_503_call(), 2)
call_4514 = relay.TupleGetItem(func_504_call(), 2)
func_1157_call = mod.get_global_var('func_1157')
func_1160_call = mutated_mod.get_global_var('func_1160')
const_4542 = relay.const([-1.001498,2.830583,7.765236,0.266642,9.973817,-2.876134,-9.530667,0.948886,7.498603,-9.396270,-9.395911,3.668102,2.498373,7.436417,3.994241,-1.899252,-8.636784,-4.142518,-1.854660,0.556598,1.006553,-5.693540,5.126183,-7.182094,7.619363,-6.758450,-3.041888,3.033808,8.123100,-4.483667,7.399986,-9.628466,-7.996094,3.686925,-0.793752,-4.673428,-8.303825,-1.482722,1.608222,8.045252,3.863984,-1.692146,1.192602,9.978641,-6.039997,-2.822421,5.657387,6.323900,3.438026,-5.365069,7.981896,4.617727,9.559616,6.754680,-5.927269,-3.471467,6.889712,-6.222581,-0.745419,0.856325,7.716141,9.966613,-1.267383,4.892242,0.535161,4.082443,-2.501011,1.907816,-8.727947,-5.858388,0.952543,-7.545066,0.963686,2.951117,8.436588,-1.661481,-7.157550,0.087133,-7.448501,8.307838,-8.862127,8.657294,4.892051,3.989293,9.754002,0.674797,-4.682560,8.476274,-9.795635,9.829441,4.189676,-1.629659,2.482817,-2.803342,-3.418520,-0.220461,1.954687,-0.075747,-5.726897,-4.010498,5.308738,-3.140478,-1.470212,-4.270612,-8.485621,-0.867706,3.212956,-9.404719,-6.539480,6.987533,-8.676737,8.644029,3.145932,-8.166732,5.482515,2.453095,-4.936337,-1.065211,-1.899874,9.271294,4.550032,-1.050000,8.948344,0.235625,-9.268805,-1.117164,-0.265115,-5.008411,1.249645,6.926951,8.593624,-0.284288,-7.023004,-1.131142,2.174798,-2.776384,7.719307,4.965430,8.747760,-8.940705,6.509164,-0.449115,5.910400,3.167608,8.238731,1.760470,-8.334242,4.329790,8.148574,6.290515,3.508980,3.761568,-9.165384,3.056163,1.584256,7.875613,1.572937,6.932276,-6.052039,3.319821,6.871401,8.624166,-6.621581,3.753834,-8.239427,-3.266121,-5.360862,2.320707,9.694066,-3.128469,-1.288360,3.044876,6.554237,-4.936187,-5.901077,3.585178,3.554838,3.984171,5.099963,7.309975,2.799190,-0.515129,5.502976,-4.390396,-1.793220,6.840679,3.127578,-6.096795,6.788847,-4.079016,4.669763,-6.430010,-8.648073,-4.299959,-9.030412,-0.007552,-1.656294,1.036450,-6.469298,-0.162505,-3.220942,0.679704,-0.416392,-2.794095,0.386128,6.751472,-0.662174,6.959416,0.185581,3.473209,2.568620,3.901483,-5.354404,5.347688,7.237305,8.237167,0.668982,3.938881,7.594733,-7.719554,-0.028114,4.325832,4.515796,-7.808490,-7.917145,-3.473594,2.417024,9.688603,-5.916984,-7.894104,-0.710612,1.086505,-1.472168,-9.111719,-2.886141,-8.097158,-5.667613,3.524359,-0.973127,2.228490,7.029453,-5.683325,3.706369,-4.859649,-5.760487,8.006674,5.704839,0.009254,5.246262,8.907991,-1.607134,6.014987,2.041730,-7.026829,-2.809728,-0.508908,0.017606,-2.320764,2.743153,-9.920662,7.688725,-4.945610,-3.511131,-6.342995,8.637983,7.207293,-8.560473,6.986376,0.877599,1.919961,2.677201,-5.096045,0.469399,5.716265,9.807355,-1.139518,-5.327295,3.627001,-9.488928,-8.892029,8.359623,4.564800,-0.961662,6.598233,-3.428423,2.965125,7.216498,-7.749155,-4.124926,5.002525,8.814499,-0.663367,-5.050900,-6.328634,-0.376766,9.360998,-9.335459,5.037658,0.129074,0.702030,8.882205,2.435176,-5.230378,1.466132,5.199394,-6.950409,2.919415,-4.640423,7.399311,-0.738946,-7.175236,2.295677,0.138219,8.458448,-6.475271,-4.753448,-7.161074,-8.282088,-0.434994,8.926027,-8.917795,-5.522136,1.656411,3.018797,-7.271629,-0.352088,6.081135,0.032469,-9.013306,3.243533,5.467727,-3.780759,8.144756,-2.821752,2.652894,-0.258523,-1.854489,2.002051,5.669002,-9.978575,-3.669121,-7.816124,-4.751907,-0.526543,2.311932,2.364238,-6.882345,-6.879295,-4.014286,7.415890,-8.657360,2.039734,-5.469726,-7.987496,-4.684731,0.498003,5.177760,-4.249799,-7.984837,-5.962916,5.676028,-7.918373,-8.235019,2.570280,-1.379110,-3.502438,-5.572477,9.854347,-0.663935,5.778785,-7.753361,0.938873,-1.673334,3.006081,8.910786,-6.076846,-6.602408,-4.057838,2.110806,8.572777,-0.997285,0.574859,-2.025864,1.948396,-1.168171,4.169480,-9.588539,9.079704,-7.253534,2.403706,-3.834699,-0.309112,-3.065942,2.136464,3.485346,3.634986,-1.075620,-4.800945,4.584047,5.339834,-3.918927,-2.371893,-2.057222,-3.626502,1.407249,-1.676436,4.901853,-2.553102,0.100413,-0.542172,-7.354816,-9.657791,-6.712131,0.702061,-7.822952,6.118530,6.569197,4.331722,9.083989,8.663367,6.317521,2.947721,-2.992529,2.400418,8.867065,-0.910463,3.890835,5.445636,-2.000033,-3.793593,6.984231,0.999222,8.087622,-4.399412,-1.769658,9.208530,1.439776,0.434202,-5.636835,4.855732,-5.686491,-6.713005,-1.139843,5.379228,-4.104512,-1.603235,9.704305,6.380741,-4.725506,-4.660386,7.436219,2.816850,-3.873097,-6.523267,0.622020,-0.975755,-7.706293,3.170384,-4.952558,1.082245,-0.465514,8.797067,7.408207,0.041349,-7.364002,2.177916,7.182369,5.620189,5.273581,3.756757,5.395796,-6.870070,-2.946327,8.720041,-5.608031,8.004417,-8.282735,-9.422464,7.091074,4.636449,6.656884,7.075299,9.235206,-0.945878,6.226736,2.124028,-7.936198,-8.698442,-5.168068,8.263610,-4.717598,5.035236,1.624098,-5.200176,6.721977,8.477592,-9.250396,-3.116663,1.066654,-0.590830,-8.379060,8.785849,7.834019,8.006031,5.936039,-8.180191,7.011833,-1.924351,-2.842258,-2.334339,9.347686,-7.341408,-8.138314,9.813546,-0.086052,-3.229588,-2.072475,7.234445,5.568886,5.905681,3.814551,-3.302320,0.909064,-4.198281,-3.854840,-8.993609,-3.659022,3.088006,1.788564,-8.872401,0.120372,-5.406675,-1.085154,3.354038,-2.606671,2.779685,9.116813,-2.378800,-0.518427,-6.545794,8.414264,-0.627556,3.708296,8.154111,8.708626,-4.498287,-5.313270,-5.385257,-7.487841,4.364963,-3.446888,6.681285,-1.950406,-5.651280,-5.750231,1.761473,6.036736,5.887485,-4.875233,1.402210,-5.599233,-4.804217,-3.825705,6.269564,-8.889949,8.687696,6.084685,-1.453313,7.270041,7.708494,1.396313,7.679344,-8.516491,-5.775818,8.063679,-0.919010,2.478856,6.061494,2.045276,6.555696,9.085903,-9.979144,5.840608,-1.002070,-2.147888,-6.760375,9.840643,-7.630751,-3.041777,-0.624329,4.174884,7.428636,7.353180,-8.953872,6.257662,-2.643896,4.242896,-2.618513,-7.259524,6.540468,-9.161766,-1.801268,6.314329,2.752046,7.554428,-8.055668,4.574082,-6.043389,-7.505760,6.191010,-9.563779,-7.431033,6.377429,-6.084335,5.051218,-2.413882,7.900646,0.638301,5.991131,-4.349745,-5.506981,0.417036,-2.592150,-2.689174,5.094102,-5.282139,-5.921923,2.401119,1.526862,9.029922,8.021310,-0.001418,-8.771689,4.488729,8.883285,2.396824,-7.743890,6.448310,-7.153367,0.362232,9.258616,6.598601,-3.078680,3.157324,-5.883119,5.559447,-3.762606,-5.372497,4.921083,1.758151,7.336489,2.724989,6.183677,-0.724785,-2.153129,9.909945,2.129220,5.684149,9.387591,-5.521711,4.090916,0.767714,8.683787,8.574938,-2.598531,6.410358,1.556814,2.135841,0.202325,-4.283990,-7.818020,-4.004847,-8.650468,9.098863,-0.637280,8.708249,4.023159,-0.969794,-7.407662,-9.194145,-0.460184,-3.104577,-8.171962,-1.046037,3.188548,2.297753,0.637495,2.811592,-0.454563,1.442576,-6.113791,-1.839786,-5.851450,1.043108,-0.674581,2.077404,0.774471,-1.879866,6.771447,-7.019539,5.421767,-7.345578,0.691367,-8.311102,9.329200,-3.319179,-9.591160,7.942182,9.937125,5.506232,-8.564615,-3.935294,-7.979387,5.291693,-1.645567,-3.757863,-6.796077,-3.496237,4.313542,7.421660,-7.543657,-5.158267,-2.121807,6.244714,-8.865834,-4.193020,0.061459,3.337307,8.511070,-2.237119,-2.099675,-6.902818,0.721037,-2.668637,2.507588,4.950766,7.267679,0.403570,-7.317155,-0.446220,9.944567,3.114992,8.456703,3.790013,-7.941134,-0.909544,-4.923065,1.977625,8.067023,-0.421352,0.882108,2.639054,-2.405121,-0.934656,4.774224,0.008157,4.556148,-4.723969,7.525626,-9.191522,7.329379,-2.213502,9.434614,7.736653,1.662182,7.850638,-6.498395,-8.154440,7.584770,8.324458,4.755342,-7.085064,4.084258,4.149186,-2.318419,-3.166347,4.194328,1.841475,-5.664868,6.478660,9.282877,-5.238156,8.949531,-1.685945,-4.803572,-8.114412,-9.629654,-6.910177,1.435453,7.251193,2.513382,5.351685,-1.751488,7.592277,7.335753,9.601260,-1.456775,-1.164412,-6.344178,-8.852049,-4.537431,-5.854514,6.510495,1.527311,-0.514301,-1.248635,-1.500654,-7.374941,1.039999,-9.772057,1.875851,8.000218,3.616698,4.080786,-1.862935,-0.727499,-5.035505,2.991953,-4.447405,-0.307433,0.920031,-2.578694,-4.136420,7.806062,2.373092,3.500291,9.212811,-5.540039,-5.460234,-9.900608,5.906721,-0.713382,9.307207,-1.729185,-7.166396,-8.496894,2.077902,5.062118,-0.321384,0.309185,-1.549520,-7.256344,8.261843,1.989441,-2.391985,-6.419809,-6.905747,-3.932082,5.432615,9.158529,7.544684,9.878721,1.944838,4.430460,4.181609,9.440911,4.668815,2.097287,-0.004383,-3.652726,-1.917680,-8.493363,3.772346,-4.858862,1.942128,-7.943069,-8.319023,-0.284950,2.470125,5.860964,-8.728435,-6.801240,-8.958022,7.455845,-5.185207,9.141561,-1.340390,-8.496920,-0.854180,-4.777774,-3.366318,1.391910,4.396009,-5.933572,8.990425,7.227324,-4.148325,6.749910,-4.688316,0.363642,-5.402035,7.805906,8.681750,4.454122,2.133006,0.610076,-1.686090,-7.692033,-0.677548,-8.923298,-6.099511,-5.598729,-4.560721,6.608257,-0.296811,5.410887,7.651127,4.407290,-9.067256,1.903671,8.367723,-2.937165,2.940624,4.451462,4.059548,2.363813,9.249055,2.571763,9.958785,-1.546914,4.505846,-4.653266,7.890561,5.715560,-2.376462,5.427044,-5.908955,-1.730647,-8.960378,2.992472,0.825003,4.423743,-2.385365,-6.568520,1.987329,2.338240,3.396858,4.958936,-8.459669,-9.179890,5.201389,-0.190739,9.391829,1.339206,-2.605188,-6.471636,7.379305,-3.557703,-6.056503,4.860442,-8.938216,-1.626548,7.987038,-0.095995,2.124564,-5.708868,-9.731055,-0.601955,5.262011,1.587273,-7.681808,-6.654779,5.388716,-1.494074,8.688929,0.219294,-0.632170,4.709529,2.048612,4.683744,1.627784,-4.369310,-4.587501,1.981374,-4.690555,6.228652,-1.674068,9.319901,0.667213,8.152353,7.795656,-2.475282,3.401323,7.406032,7.952124,1.991117,9.123819,-3.898869,-9.394590,8.902440,-0.145012,4.270099,-6.366914,-5.921071,-1.758673,6.563490,-6.209410,-7.105201,5.177714,-3.113654,-8.887957,7.685478,1.838306,-7.133471,-9.088102,1.404691,-3.657102,0.270149,6.990293,-7.873378,-4.238218,4.253893,1.195538,-9.528063,-5.097675,8.430759,-4.528401,-3.841065,-0.605753,5.416400,-4.686675,0.990696,7.325495,-3.158383,-8.375992,0.663177,-2.412371,4.581221,-2.612215,-5.790245,3.973793,6.632039,0.730166,6.815196,-2.569211,-2.103297,8.673746,-9.356849,-7.015674,5.608666,2.384734,8.572750,-8.937488,-2.368403,-9.277707,4.214616,-0.581335,1.652651,-5.810206,-4.128487,2.440421,5.435440,-7.155103,-0.205394,-8.681316,-1.967934,-3.317773,2.152161,-0.885881,6.801549,4.420036,-7.978649,9.735516,7.644453,9.234516,5.513718,-1.215118,5.648836,-0.770083,3.807888,-8.915234,-7.729084,-9.993398,3.944898,0.141982,3.453136,6.707463,3.304917,-1.895924,-6.641077,-6.889111,-9.432198,-5.128623,8.861572,4.857691,-0.522119,-9.491992,-1.469195,-5.086945,-0.322150,-5.613313,-9.792210,3.092086,2.554711,-8.456976,3.271738,8.790932,3.482076,-9.918648,-4.092691,-6.497304,4.131335,4.124556,3.579077,4.362502,-7.322842,7.664542,9.351240,-4.120644,-2.098484,-8.077303,8.796846,-6.081667,1.458989,9.255601,-3.045417,-3.558019,9.424125,-8.788921,-7.040537,-4.067955,8.259198,4.647405,-8.575710,4.702920,5.957868,4.952344,6.146832,6.984608,-0.435707,-7.163453,-1.830771,-9.802557,8.462686,-4.547399,-7.068898,-9.761377,1.144948,-2.144726,1.118040,-7.230417,8.787920,4.953305,7.851259,6.161310,8.549740,6.954906,2.781082,9.477740,-7.832695,-7.334561,-8.561978,-3.604177,-7.135230,-4.536311,7.320094,-4.598487,-9.928118,0.902117,5.214752,5.977570,8.067447,-6.755816,-4.403532,9.229491,-5.040178,3.821959,-1.863019,-0.835363,-1.251428,-1.486739,5.583006,-0.045417,-4.270968,-7.898361,-2.218689,-7.644684,-3.136459,-5.435197,1.608202,8.927925,1.883679,-4.652970,-6.913756,4.193700,2.502635,-7.096747,-7.272098,-4.579135,1.997085,-5.440314,-0.140717,8.462166,-0.881990,0.810186,0.087569,0.842910,1.256195,-8.174528,-4.553053,-8.280367,3.415949,-9.347013,6.480345,-2.158377,6.498925,9.437856,7.487081,-6.833706,-5.181815,4.168847,-3.693076,1.591118,4.846331,-1.028916,0.937911,2.559567,6.382536,-0.340778,0.619613,3.598545,-7.268787,-5.729356,1.767553,5.836366,8.648273,4.200697,6.144777,2.411419,-7.431095,-4.143991,6.820793,-2.667538,0.007388,2.410305,2.352272,-5.332625,8.731284,-0.076574,9.439569,7.109624,-9.391501,5.469127,9.038020,-0.981101,-7.283920,9.125269,9.146002,-7.824562,-1.418808,0.552697,8.194202,1.844799,-7.601546,7.190392,1.572325,-7.460158,-5.068708,2.964898,6.746220,1.792302,-8.606099,6.031845,7.515618,3.587923,0.918257,8.918174,-2.816066,-4.020836,-1.903460,-1.351860,-7.624139,-1.444917,-7.621280,-4.339406,5.898874,4.582032,-8.410954,5.438256,4.055090,6.695933,3.980025,5.586226,-4.423305,7.486259,3.964271,-1.932872,-2.089706,-4.265116,5.549765,-9.195063,3.027896,-8.169141,-4.294544,5.675519,-2.848488,4.363139,9.168701,3.742838,-8.314707,3.071556,8.739099,7.053247,-4.506293,-5.889914,-5.702239,-8.644951,2.763965,2.695346,3.135885,3.885464,3.765189,3.280042,7.279332,-8.678014,1.123158,4.598179,-2.714268,9.493739,1.804840,-7.392904,-9.685442,3.370347,0.263145,-7.917436,8.874494,0.323527,-0.478280,6.294396,2.949782,8.353783,3.828529,0.730801,8.990835,-2.905549,8.610952,-1.623958,-5.656345,6.028898,-3.638013,-2.610444,7.322481,-1.971173,-6.664887,2.323610,-1.005009,4.077688,1.139000,5.428182,1.419069,6.019863,-7.356775,-7.976923,8.574466,-9.135735,3.468852,7.647686,-4.053751,-2.012493,-6.101041,8.317141,-2.898026,-4.892745,7.607323,-2.192677,-8.804935,0.390678,2.688181,2.778008,6.200356,-1.262304,-0.670877,0.175665,-9.525622,1.836393,5.180154,3.279211,6.873388,-1.207112,2.031537,9.311094,-6.320475,-6.134212,6.028125,5.745222,7.346308,9.044627,2.981877,6.845326,8.121506,-8.393079,2.449821,-0.944508,-1.102230,3.462408,-7.215739,2.564539,-8.817343,-1.834518,4.525880,-5.346506,-0.230686,-9.330879,4.201072,8.704891,-9.238060,7.447858,3.460949,7.872091,-0.741472,1.934728,2.450962,-7.554819,-9.414369,5.315651,-4.191942,-4.701527,-8.311432,-4.624046,-0.179946,-4.069603,-5.259393,-0.328380,1.240916,6.136121,7.425499,-7.810324,1.199527,-4.767278,-6.431678,1.996128,6.650042,0.159259,-9.513407,3.455383,6.395301,5.537709,-7.746376,2.518626,1.871533,9.949001,8.368126,-0.088878,-7.040491,-3.010073,-1.695655,3.883746,3.857494,0.644688,4.801738,4.216775,-3.712793,-3.800680,-8.465743,3.211262,-7.633223,-2.982510,-6.366092,-7.105880,6.997067,8.130947,-6.649951,-1.493677,5.145550,0.108030,-8.108402,7.785788,4.547443,5.074205,6.021838,-0.853080,-0.837132,2.204235,4.708394,4.783059,-2.412778,-9.931992,-0.168419,7.944898,3.287963,-7.855156,6.494644,-1.112453,2.021254,-3.956188,-1.795413,-2.756393,-9.967160,-0.268611,9.836810,-1.921744,-4.199421,-0.425836,3.424535,3.713995,-0.898385,3.449033,4.458463,-3.173924,3.354468,-6.445889,5.919259,-7.084702,-9.242641,7.910211,9.334634,-5.657114,6.147433,-4.497993,-9.236082,2.965634,8.452300,-6.877591,-9.191795,5.320384,8.853955,-0.738024,-2.104967,-4.555405,3.554890,-6.839157,-1.511590,-9.896679,0.903289,-5.698920,-1.280443,-1.393679,-2.364195,4.064921,5.378866,1.022374,-3.074075,-6.327195,-9.352132,1.407183,-3.704235,-5.845880,-6.847283,-7.347437,7.968691,8.285428,-3.149844,2.977111,-2.483970,-4.628430,5.363509,2.795229,8.446602,-1.827452,-8.734047,6.157480,4.777854,0.461566,-0.199463,6.927182,0.587543,-9.591994,-9.049730,-0.508565,-1.147788,8.055619,-9.540947,8.804182,-4.164735,-1.846555,9.974737,9.148423,1.418268,4.711699,2.508957,-3.715655,4.531659,-3.303449,-3.260753,6.275955,8.429261,0.564083,1.612132,2.053166,-4.231852,-0.337845,6.185400,2.065036,5.287801,6.070903,7.095687,6.758127,-0.471891,7.117557,-8.364739,1.817518,5.478211,-2.939767,0.406024,-7.052253,0.554274,1.331042,-0.292379,3.260193,8.677428,-7.557898,-7.613333,-5.902492,-9.616264,-9.155446,-3.507823,-4.162635,-4.839383,-8.674701,6.380101,5.252294,4.620341,7.954514,5.656848,4.123010,1.566199,-5.437821,0.310203,-3.878614,-2.735292,2.483116,-5.349547,-0.526001,-2.402252,-3.398188,3.438232,-8.509405,3.522146,-6.919571,-8.799663,4.561626,-9.661822,-7.868061,-1.485546,8.710737,9.899150,4.037757,-8.584935,-1.058010,-1.646634,-1.637142,-4.801358,1.878410,0.179241,1.747939,3.506109,3.270012,-7.366769,-7.850421,1.275830,8.290273,-2.652478,-9.419514,-4.409534,2.547815,-1.480193,-1.300241,-4.494137,-2.126287,1.966497,3.359093,-5.694037,-3.509864,-0.640694,-8.538107,-4.123994,-2.362121,-2.410781,-0.720085,4.765762,-3.740925,1.947003,4.603902,-9.049609,3.698372,8.908912,-0.890731,-3.416555,-9.660749,4.759474,-6.727526,-8.685874,-7.161404,3.988396,4.757380,-2.148924,-8.537752,-4.163444,3.311975,5.523069,-7.118298,-9.010635,7.140456,-0.043585,6.312798,-0.960369,3.908146,7.355398,2.292077,-1.591636,0.257641,-7.931710,1.839506,7.746028,7.672165,5.254208,4.647676,9.903430,-6.113330,-5.237503,7.994126,7.782156,7.261121,0.591034,-4.683143,0.619012,-2.971576,5.783956,-9.262211,6.699095,-4.016072,-8.825810,-4.916710,-8.568247,6.193951,-4.367877,4.029958,5.135525,-4.439217,3.036041,5.397369,7.360193,9.194974,3.941499,7.616186,5.643873,6.447089,-6.420000,6.028156,4.624445,9.636922,-5.069053,6.973258,-6.926428,-8.067496,-8.966632,-6.563776,6.871897,2.868872,-8.078712,1.209572,-6.752771,9.422361,-3.795618,9.848915,6.369520,-4.000284,7.282026,7.088578,2.776648,8.114382,9.884615,1.258636,2.329347,1.764104,-7.582889,-3.267684,-9.721277,8.268399,-1.415190,-7.791207,1.487097,9.042850,-3.613361,-8.546546,-1.687813,-6.031623,-6.300533,7.842626,-3.783852,7.867570,9.001571,9.470239,6.583401,5.532135,9.111029,7.084845,-2.985004,5.750295,2.521730,-2.009309,3.794454,-6.129004,7.744447,-6.698244,-0.644134,-4.187501,9.635470,3.280148,-3.152140,-5.779135,-1.427051,-0.315303,6.668045,-6.777969,-7.987373,-8.948633,0.577760,5.438267,-0.125341,-9.872217,0.238474,4.977114,-8.045567,7.997914,8.476605,-6.197972,3.231930,-2.548717,-1.179384,3.035078,9.470092,-5.086279,-2.572835,5.356543,1.219628,-1.170166,-4.951248,4.349078,-8.200385,8.800318,7.514870,-6.541808,0.443142,3.803520,7.982470,-6.683075,-3.140383,1.257952,-2.581091,-6.598395,-9.128995,-1.088136,-0.590670,1.175117,-3.560969,-6.958733,-1.714673,-7.508707,5.973023,1.585174,-2.035369,8.824176,-6.965616,-7.162178,-3.320260,4.049421,6.761250,9.807952,1.652528,-3.750115,-3.490306,2.501967,5.944077,-7.191551,6.338513,2.908674,1.681056,1.802001,1.925704,-2.166845,-7.135596,-1.717694,7.134885,1.978749,-6.429342,-3.720505,-3.660918,2.356834,7.364200,-5.828611,4.587003,-0.847978,-5.590284,4.468196,1.996665,8.641523,5.887534,3.928869,-7.041120,9.214296,4.438249,6.050263,-0.921105,1.749392,-4.620856,-0.628077,-4.071546,-2.817418,-0.505428,-5.841725,0.976649,5.035573,-2.218228,1.683616,2.599239,6.137451,-8.881632,-2.211779,-4.634150,-8.701341,6.785000,-8.591487,7.876211,2.482931,-4.242615,-0.208587,2.257607,-8.929682,-8.227004,-5.742836,1.356646,-0.514257,-2.898867,-3.862742,4.952817,8.819904,2.669569,-1.213416,-4.222445,4.767927,3.403928,-6.816425,8.912125,-2.425038,-5.361581,-7.112718,1.019247,9.542632,5.491171,-6.920081,-7.706907,-4.810803,0.178629,9.762405,-8.333569,5.272966,-5.672016,-1.734653,-1.851722,3.984326,-7.588137,-6.587833,3.730311,1.211074,4.999581,2.341118,-4.094204,-6.972266,-3.303150,5.961999,-7.860187,-4.567255,4.882219,-2.561488,-3.924758,-3.313723,7.607926,-9.726266,6.232022,-6.361800,7.620871,-5.353287,9.595755,6.136257,-3.567259,-2.274612,9.524028,0.552623,0.531584,0.792267,-4.513103,-0.638806,-1.623385,-5.899444,4.868408,3.158221,-5.712431,-1.414225,-3.030745,0.930430,-3.193351,1.244683,-4.841026,-8.917165,-5.514124,0.167036,-5.247798,2.791433,-5.690687,-1.564751,-1.451480,-0.366510,4.751322,-6.370444,9.831324,3.015165,9.618299,5.277776,8.980654,6.595793,1.418020,-7.701636,3.425151,1.608471,3.217371,6.168769,0.886853,-2.456898,-6.454142,-9.815643,-1.542665,5.067961,-0.315355,-9.460942,0.593184,8.728527,-1.946137,-9.338205,0.864905,-5.338404,8.593146,-0.386701,7.421599,4.840588,9.212454,3.129460,5.835728,0.235666,-3.062619,-0.459746,-6.529817,-3.923348,4.937486,-0.304113,-4.867145,-8.124837,-8.171476,-2.780336,3.967011,3.544368,0.161567,6.997934,8.728740,-3.243486,-8.100479,3.581680,4.011552,4.677549,-2.604743,0.755930,-2.302521,-8.521127,3.719219,0.608270,7.326958,1.488439,9.907659,9.766261,-6.881953,-9.770801,-4.750931,8.487597,-6.406323,6.859957,-2.042153,6.183466,-7.639362,0.901617,6.778696,-6.414912,2.457222,5.219592,-7.182305,9.851636,6.357488,6.952674,-4.428665,8.751027,-8.783657,7.770899,3.689801,5.749051,6.209043,9.064714,8.653371,7.044474,-1.291772,-3.116306,6.573141,7.195853,2.396862,6.362472,8.200469,-7.752045,3.128798,-8.551782,2.137140,-4.264895,-7.453743,4.181683,5.153367,-6.823711,9.156284,8.908359,-7.933537,1.124860,9.274258,2.499913,4.953751,-2.429003,-2.598636,-4.179582,7.443501,-3.160320,-3.696021,3.255275,-5.884311,7.385999,-9.505579,-2.692853,3.446360,9.667884,-4.070900,5.098515,-3.672654,-7.819857,-7.856619,-1.742681,7.248908,1.458674,-3.087961,-9.125263,-3.054148,9.715412,-0.394399,-0.495572,6.394094,-2.938320,-4.849812,-5.933165,-6.134545,9.345501,8.895847,-4.389763,-7.279978,-8.983676,-6.696565,9.590782,3.255897,-0.204637,0.512218,3.883673,-3.814144,-1.184554,-5.173659,3.230984,-7.035817,0.359781,4.200088,-3.094475,-2.279696,-8.615803,2.337853,7.613775,-4.215869,-7.798872,-3.956415,6.157302,-7.575905,-6.529471,-6.171153,8.182547,-3.680590,-5.700882,-1.010769,-1.917846,9.204819,2.953916,-9.527426,7.053442,-4.785254,-4.850480,-0.148231,2.925516,-5.956196,7.094027,-7.153215,0.244444,0.279370,-9.358828,-4.453659,-4.153268,2.773975,0.150035,9.094889,6.043092,-0.927517,-9.422114,7.518122,4.273153,5.980306,-0.946750,4.782798,2.740516,8.463373,-1.634724,-4.562648,9.664139,8.747710,4.277401,-8.913870,-5.729168,3.211324,3.296234,9.233172,-4.604673,3.430469,-5.619421,-4.029466,1.197027,4.084191,8.234037,8.253044,2.519475,8.665356,5.074351,6.453664,6.859738,-9.227551,2.479590,1.369339,4.643548,-6.458804,-1.048234,9.810672,-2.207965,0.538006,-1.355544,2.889586,3.684573,-8.643487,-8.958894,2.550962,-5.791183,-2.083028,2.563114,6.407258,-7.368093,-4.764460,-4.280521,-4.155990,-5.114437,9.705796,-1.936923,-2.269623,9.312346,-4.368384,7.375896,2.041008,-5.095038,6.251355,-0.795146,-0.107818,1.263086,0.422534,-2.029075,-9.776583,5.692389,4.719965,-8.230304,-8.706039,-4.052092,0.416147,-5.404473,-4.981191,-1.886998,-6.783144,-0.809973,1.055736,8.908137,-0.038691,5.309937,-3.432315,-3.931082,-6.455172,5.222573,-0.599876,-5.486191,8.662175,4.191603,0.467559,-8.856425,-1.833182,-3.930580,-5.388810,-3.094073,6.528041,2.574327,-8.605942,6.564867,0.446835,0.484331,-6.620738,6.168487,-0.066588,7.676042,6.477209,4.923290,9.714555,4.104912,0.554673,-6.608728,3.814710,-2.796433,9.418462,6.465142,6.548905,-8.679516,-9.746632,6.244467,-3.505429,-5.121194,-4.996521,4.148687,2.429088,1.766715,-1.358474,4.568463,-3.778601,-4.085358,4.287924,-5.158705,-0.878698,-3.363466,-2.452878,-5.087771,4.602916,-6.604745,-9.395215,5.389777,2.937868,0.953988,-1.670896,9.832694,-7.439066,-9.455806,2.632980,-1.671488,7.588205,-0.465853,3.162400,6.989425,2.486605,-0.854043,1.997086,8.780118,9.097199,9.751583,2.352238,-1.038718,-5.030245,8.172343,9.744328,9.247881,5.833453,-7.982796,-7.610379,6.000292,-5.637976,-5.914377,1.623219,-2.887467,-9.383421,-5.197609,-8.669407,5.497613,9.899570,9.471918,1.469413,8.485974,-6.081154,2.362607,6.780973,9.359012,-2.537841,-2.046599,8.192143,-5.151434,-9.265393,-7.564343,2.258184,1.084293,-8.666915,8.985926,6.233543,-0.967395,6.013151,4.138282,-5.175270,-1.202920,-2.207726,-2.059625,5.924502,6.888641,4.535177,-6.441208,6.962564,2.293422,-7.103360,5.026560,-1.516663,-7.970600,7.760670,-5.063342,-4.566401,0.497400,2.998844,-7.813790,-2.857588,-0.464438,5.673367,6.670214,-0.462874,3.441559,0.380782,8.805498,-1.290689,5.959026,2.894835,-5.520668,-0.908594,-6.158529,0.556499,-2.959838,-6.200403,-2.587952,-6.469119,-5.965204,-7.726679,7.347735,5.467512,6.970969,-1.990384,8.882027,5.478297,4.055218,5.947407,4.516711,4.239577,1.544934,5.189841,1.976604,1.353370,-4.860765,1.272615,1.544334,-0.266295,1.603763,-2.543165,-0.600255,-9.771797,2.809673,8.290611,-3.577091,4.937994,-9.461605,2.211626,-5.177203,-3.302640,2.347996,-9.765430,-0.183024,6.188019,-1.526999,-5.342684,8.668018,-4.579020,3.918207,-6.738273,-1.302126,0.060049,-8.398395,3.863306,6.492267,6.698158,8.288547,3.984894,2.332134,5.306726,-2.177624,-7.779393,-7.315705,2.311123,3.860032,-9.841547,7.928933,-6.055161,-3.879127,-2.834791,4.340287,-0.027436,2.106842,-3.309755,0.934785,-2.033073,-8.018259,4.118612,-2.301987,-0.578518,-7.692525,4.862882,-5.876233,8.115738,3.303386,-5.757159,-6.493040,-7.763675,-5.303106,-2.663096,-0.127558,-1.331123,7.301361,-2.209518,-4.398472,8.198827,4.783492,-4.129271,9.684130,-5.184533,3.421105,7.991456,-5.762063,2.744105,7.971533,-1.022336,4.319944,-2.638804,-3.586478,-9.795462,7.435596,-6.132262,-1.553104,-8.525788,-1.353934,0.928059,0.173989,1.136468,-1.400784,-2.344101,-2.158844,5.585374,5.972232,3.946556,-9.419459,-1.789822,8.387854,-1.085235,6.391387,1.184751,-8.243326,4.881926,-0.887819,5.893958,-8.386779,-1.344679,-5.389956,-5.827340,2.884955,8.373794,3.202829,4.293685,-3.961137,-1.295324,-7.281360,-0.193728,-6.502361,-6.751402,-9.770150,1.549871,4.646633,-8.367425,-5.166083,-4.239444,-8.992287,5.090616,8.365192,-2.900041,5.383881,-1.356302,2.758696,-2.820745,-7.165173,-9.971972,-3.944874,2.118953,2.509018,0.171955,-7.535679,8.815064,0.193621,-9.764080,3.341986,1.498702,-3.440900,-2.311087,-8.784495,3.544900,1.628642,7.919377,-7.567180,3.642048,-8.896050,3.408073,-7.908308,7.702065,7.251888,3.678204,1.811259,1.907636,-6.442328,3.259581,-5.958902,3.914090,-1.233611,9.030230,-2.940835,-8.862927,9.793354,4.005549], dtype = "float64")#candidate|4542|(2640,)|const|float64
call_4541 = relay.TupleGetItem(func_1157_call(relay.reshape(const_4542.astype('float64'), [16, 15, 11])), 1)
call_4543 = relay.TupleGetItem(func_1160_call(relay.reshape(const_4542.astype('float64'), [16, 15, 11])), 1)
output = relay.Tuple([call_4507,call_4513,call_4541,const_4542,])
output2 = relay.Tuple([call_4508,call_4514,call_4543,const_4542,])
func_4546 = relay.Function([], output)
mod['func_4546'] = func_4546
mod = relay.transform.InferType()(mod)
output = func_4546()
func_4547 = relay.Function([], output)
mutated_mod['func_4547'] = func_4547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3111_call = mod.get_global_var('func_3111')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_4552 = relay.TupleGetItem(func_3111_call(), 0)
call_4553 = relay.TupleGetItem(func_3112_call(), 0)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_4554 = relay.TupleGetItem(func_3024_call(), 3)
call_4555 = relay.TupleGetItem(func_3025_call(), 3)
output = relay.Tuple([call_4552,call_4554,])
output2 = relay.Tuple([call_4553,call_4555,])
func_4567 = relay.Function([], output)
mod['func_4567'] = func_4567
mod = relay.transform.InferType()(mod)
mutated_mod['func_4567'] = func_4567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4567_call = mutated_mod.get_global_var('func_4567')
call_4568 = func_4567_call()
output = call_4568
func_4569 = relay.Function([], output)
mutated_mod['func_4569'] = func_4569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2768_call = mod.get_global_var('func_2768')
func_2769_call = mutated_mod.get_global_var('func_2769')
call_4570 = relay.TupleGetItem(func_2768_call(), 2)
call_4571 = relay.TupleGetItem(func_2769_call(), 2)
output = relay.Tuple([call_4570,])
output2 = relay.Tuple([call_4571,])
func_4594 = relay.Function([], output)
mod['func_4594'] = func_4594
mod = relay.transform.InferType()(mod)
output = func_4594()
func_4595 = relay.Function([], output)
mutated_mod['func_4595'] = func_4595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_669_call = mod.get_global_var('func_669')
func_670_call = mutated_mod.get_global_var('func_670')
call_4600 = func_669_call()
call_4601 = func_669_call()
output = call_4600
output2 = call_4601
func_4608 = relay.Function([], output)
mod['func_4608'] = func_4608
mod = relay.transform.InferType()(mod)
output = func_4608()
func_4609 = relay.Function([], output)
mutated_mod['func_4609'] = func_4609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3565_call = mod.get_global_var('func_3565')
func_3566_call = mutated_mod.get_global_var('func_3566')
call_4616 = func_3565_call()
call_4617 = func_3565_call()
output = call_4616
output2 = call_4617
func_4627 = relay.Function([], output)
mod['func_4627'] = func_4627
mod = relay.transform.InferType()(mod)
output = func_4627()
func_4628 = relay.Function([], output)
mutated_mod['func_4628'] = func_4628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4474_call = mod.get_global_var('func_4474')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_4631 = relay.TupleGetItem(func_4474_call(), 0)
call_4632 = relay.TupleGetItem(func_4476_call(), 0)
uop_4636 = relay.asin(call_4631.astype('float32')) # shape=(10080,)
uop_4638 = relay.asin(call_4632.astype('float32')) # shape=(10080,)
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_4644 = relay.TupleGetItem(func_4398_call(), 1)
call_4645 = relay.TupleGetItem(func_4399_call(), 1)
output = relay.Tuple([uop_4636,call_4644,])
output2 = relay.Tuple([uop_4638,call_4645,])
func_4649 = relay.Function([], output)
mod['func_4649'] = func_4649
mod = relay.transform.InferType()(mod)
mutated_mod['func_4649'] = func_4649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4649_call = mutated_mod.get_global_var('func_4649')
call_4650 = func_4649_call()
output = call_4650
func_4651 = relay.Function([], output)
mutated_mod['func_4651'] = func_4651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4121_call = mod.get_global_var('func_4121')
func_4122_call = mutated_mod.get_global_var('func_4122')
call_4682 = func_4121_call()
call_4683 = func_4121_call()
func_2888_call = mod.get_global_var('func_2888')
func_2889_call = mutated_mod.get_global_var('func_2889')
call_4684 = relay.TupleGetItem(func_2888_call(), 1)
call_4685 = relay.TupleGetItem(func_2889_call(), 1)
uop_4695 = relay.cos(call_4684.astype('float32')) # shape=(33,)
uop_4697 = relay.cos(call_4685.astype('float32')) # shape=(33,)
func_427_call = mod.get_global_var('func_427')
func_430_call = mutated_mod.get_global_var('func_430')
const_4702 = relay.const([-0.519481,-9.872677,1.766034,3.954404,8.815557,-9.692823,-6.449630,-1.872373,-8.962271,7.174929,-3.156100,1.972440,4.947176,9.285184,3.676771,3.474938,-0.673518,6.225964,-2.074108,3.314461,8.518171,1.976380,-3.750190,7.341669,-0.195290,-6.559516,3.442286,7.266919,6.753000,-3.048850,-9.065068,-1.754809,0.060220,-9.960040,0.839282,1.564193,3.293219,-2.978553,-6.305206,-5.054881,-9.401606,0.671878,-3.674737,4.716804,4.393119,-8.176195,9.916144,-6.084947,5.504730,4.711776,-5.524732,4.710173,6.873608,-7.724580,7.615764,0.222714,8.646419,-9.539450,2.882205,3.751044,6.667292,-5.679082,2.380829,0.909009], dtype = "float32")#candidate|4702|(64,)|const|float32
call_4701 = func_427_call(relay.reshape(const_4702.astype('float32'), [4, 8, 2]), relay.reshape(const_4702.astype('float32'), [4, 8, 2]), )
call_4703 = func_427_call(relay.reshape(const_4702.astype('float32'), [4, 8, 2]), relay.reshape(const_4702.astype('float32'), [4, 8, 2]), )
func_4254_call = mod.get_global_var('func_4254')
func_4257_call = mutated_mod.get_global_var('func_4257')
const_4721 = relay.const([-9.930164,2.609808,-9.222095,6.329397,4.903979,1.369983,-9.705922,-0.365488,4.191985,-2.287162,-7.624193,5.223149,-0.875675,-2.091432,-3.877953], dtype = "float32")#candidate|4721|(15,)|const|float32
call_4720 = relay.TupleGetItem(func_4254_call(relay.reshape(const_4721.astype('float32'), [3, 1, 5])), 0)
call_4722 = relay.TupleGetItem(func_4257_call(relay.reshape(const_4721.astype('float32'), [3, 1, 5])), 0)
uop_4728 = relay.sinh(uop_4695.astype('float32')) # shape=(33,)
uop_4730 = relay.sinh(uop_4697.astype('float32')) # shape=(33,)
bop_4734 = relay.right_shift(uop_4728.astype('uint16'), relay.reshape(call_4684.astype('uint16'), relay.shape_of(uop_4728))) # shape=(33,)
bop_4737 = relay.right_shift(uop_4730.astype('uint16'), relay.reshape(call_4685.astype('uint16'), relay.shape_of(uop_4730))) # shape=(33,)
output = relay.Tuple([call_4682,call_4701,const_4702,call_4720,const_4721,bop_4734,])
output2 = relay.Tuple([call_4683,call_4703,const_4702,call_4722,const_4721,bop_4737,])
func_4739 = relay.Function([], output)
mod['func_4739'] = func_4739
mod = relay.transform.InferType()(mod)
mutated_mod['func_4739'] = func_4739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4739_call = mutated_mod.get_global_var('func_4739')
call_4740 = func_4739_call()
output = call_4740
func_4741 = relay.Function([], output)
mutated_mod['func_4741'] = func_4741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3323_call = mod.get_global_var('func_3323')
func_3324_call = mutated_mod.get_global_var('func_3324')
call_4757 = func_3323_call()
call_4758 = func_3323_call()
func_4106_call = mod.get_global_var('func_4106')
func_4107_call = mutated_mod.get_global_var('func_4107')
call_4764 = relay.TupleGetItem(func_4106_call(), 1)
call_4765 = relay.TupleGetItem(func_4107_call(), 1)
func_3242_call = mod.get_global_var('func_3242')
func_3246_call = mutated_mod.get_global_var('func_3246')
const_4782 = relay.const([-6,-4,9,-2,-3,9,9,1,-1,3,-8,-1,10,10,-4,-4,3,-7,-5,-1,5,4,3,-10,-8,2,-1,-9,-7,-7,-9,-1,2,-5,6,-7,6,-7,-7,-3,1,3,8,-2,-10,-6,-3,-1,5,-4,-2,6,-2,-6,1,6,-5,-5,-2,8,8,-10,10,-4,5,-8,8,-4,-6,-9,-10,-10,-3,-7,-1,-6,-8,-8,8,-3,-1,-10,4,9,-4,6,3,-10,2,3,2,-2,6,9,3,6,3,-5,10,7,-2,8,1,-4,-7,6,-8,10,-8,7,10,-5,7,-10,-4,1,-1,3,-8,5,-6,5,-9,8,-3,-9,8,8,4,4,-6,-7,-3,9,9,-7,6,1,-6,-3,5,5,-5,-1,-10,8,10,-3,8,-6,-7,-6,-4,10,-7,10,4,7,8,-10,-3,-6,-6,7,10,-10,6,-2,2,-2,-5,-3,8,8,-8,-6,-7,-5,1,6,5,2,2,4,8,-7,10,1,9,-8,10,-9,6,1,-6,-9,-2,2,5,-10,-6,5,6,-8,7,-4,-9,5,7,-1,10,-3,2,-8,5,-1,4,9,-4,-7,-2,-10,-5,4,-1,-6,8,-5,7,9,-1,3,8,7,8,5,-4,8,-1,1,9,3,7,10,-3,-5,9,2,-9,-9,1,-4,-10,6,9,1,7,7,-6,-7,6,-3,-8,-4,4,-4,9,3,2,-9,7,1,6,5,3,-10,3,-5,10,10,5,2,3,5,3,6,-4,3,5,3,-1,8,-10,-9,-4,-6,-2,-7,4,-10,-4,8,-5,1,10,-7,-8,-6,-8,9,-3,-3,5,-10,1,-9,-10,4,-7,-3,-10,-7,7,-9,8,9,4,6,3,10,10,9,-4,3,-10,10,9,10,-1,-1,6,-10,-3,2,4,7,9,2,-1,-9,-3,10,-6,-10,-1,8,10,-10,4,-8,-1,-2,3,6,-1,4,3,10,8,8,10,7,-4,4,6,-6,-8,-9,-2,-6,1,-1,-6,6,8,1,2,9,-6,1,4,1,8,3,-9,5,9,-4,6,10,6,3,1,3,4,9,3,-9,2,-1,3,10,-1,-10,6,2,-1,-9,8,10,-6,-1,1,-10,-6,-3,-6,-2,7,7,-1,-5,-5,-5,-6,6,-5,1,-6,6,-1,-10,2,-7,5,-4,10,-9,4,7,-10,-2,-9,-9,-5,9,-6,4,-3,8,-2,4,-4,8,-8,7,-9,1,5,4,-4,7,-4,-9,1,-6,-2,8,5,3,2,-9,3,10,-7,8,-9,-1,-8,-1,10,6,10,-7,10,6,9,5,-3,-10,1,-2,-4,7,-5,-3,-6,6,-10,10,-10,2,-10,-3,-1,-5,-2,-5,2,-8,-10,2,9,3,9,-9,-10,2,7,-4,10,-3,8,9,-1,9,-10,-9,-8,-8,6,8,8,7,-7,8,-10,-2,-10,-10,-9,-2,7,8,4,2,3,7,4,-1,-4,-10,9,-5,-2,9,2,-2,5,-6,-8,-8,-2,4,-8,7,-1,6,-9,-10,6,6,-3,10,-10,6,7,-7,-10,5,6,-9,10,-1,-8,4,10,-3,8,-10,10,-4,-9,-5,4,6,3,8,-3,-2,10,3,6,5,-9,-2,-1,5,-7,-9,-10,2,-2,-7,-1,-6,-7,-1,6,6,-10,-4,5,1,10,5,-8,-5,9,-5,-5,1,1,4,7,3,-10,-6,-6,9,8,-6,-2,7,5,4,-5,1,-9,3,6,-3,3,-3,8,-5,-7,3,3,3,-3,7,5,6,-2,-10,-7,7,4,-10,-2,-1,5,-8,-5,6,9,-6,1,8,2,-2,-1,-10,-8,7,3,-7,-3,9,-6,-6,8,9,5,-3,-5,6,3,-1,4,9,10,-10,-2,9,-5,5,8,-5,1,-1,-10,-2,-3,-3,5,-8,9,5,6,1,10,7,10,-2,7,-9,10,-1,6,-10,8,-5,-6,10,6,-5,7,-6,-3,8,-2,8,-10,-5,-3,-7,-4,9,5,-4,-1,9,1,7,-6,4,3,9,1,8,-10,-4,-9,4,4,-7,7,5,1,-1,-6,-4,7,10,9,1,-7,6,1,2,-6,-10,-2,2,-6,2,-10,-3,-2,-4,-5,4,3,7,-8,7,7,8,4,-5,-2,6,-5,-8,2,-10,8,-8,-4,5,6,-7,-3,4,-4,10,8,-8,5,-2,8,5,-7,-9,1,-2,-7,-10,3,-8,5,-3,-5,7,-4,10,-10,10,-9,-8,-4,-7,-9,-1,-1,7,8,10,-10,-7,4,8,2,3,8,4,-2,-5,8,-3,-7,-8,2,-10,2,7,-5,-2,-7,-10,6,9,5,-9,9,5,-2,-3,-8,7,10,-8,10,-4,4,-4,-8,-10,-6,-7,1,-1,2,9,8,-1,-9,5,-10,-8,1,-7,-4,1,6,-5,9,-1,-3,-2,-6,9,-2,7,-3,8,-9,-4,-2,5,4,-6,-7,3,-7,10,8,9,6,-3,2,-5,-6,6,-8,9,-10,-5,2,-8,3,-4,-7,-10,-10,-4,-4,-7,-9,-2,3,-7,6,3,-9,9,-9,2,8,1,-7,-2,3,5,2,7,9,-10,7,5,4,-10,8,9,8,-6,4,-7,-7,8,-2,-7,-10,-7,10,-7,-5,7,10,1,-7,-4,5,9,6,3,2,-10,-9,-3,9,7,-6,-9,-2,6,-5,2,4,4,-1,-7,-1,7,-3,2,10,-6,-2,3,-3,-5,1,-10,1,6,-3,4,1,-5,-4,4,4,8,-3,4,-4,-6,-6,-2,2,-8,-3,2,-6,6,-4,1,10,-6,2,1,-8,-1,-5,3,2,-6,-4,7,-3,-9,3,7,-1,8,-2,9,6,-6,4,-2,-9,-1,5,4,-3,7,4,1,6,1,8,9,2,9,-3,4,7,8,7,4,-6,8,-4,7,8,-1,8,2,-5,7,10,-3,-1,3,-4,8,7,-2,-4,-4,-9,-1,-4,8,-2,9,-10,-2,-5,9,-9,9,-4,10,2,-2,-8,-9,-4,4,-3,1,-7,-6,-6,-2,-3,-5,-2,5,-9,-6,-8,1,-1,1,10,-9,2,1,-10,3,4,10,-2,-1,-2,10,-9,3,10,5,-3,-8,10,3,2,5,5,-1,2,10,6,-5,2,6,3,1,8,3,9,-9,-3,7,2,4,8,10,-5,1,-7,1,-2,8,-4,-9,-8,-5,5,-8,10,2,8,-3,9,10,3,-5,-6,5,3,-4,-2,-9,-3,-3,1,-2,-7,1,9,1,-5,-8,-7,-2,9,-1,-8,-10,-9,5,-8,8,2,-3,-3,4,1,2,7,8,1,-8,10,-2,-3,-1,-2,8,10,-4,6,-4,1,4,-9,5,2,9,-3,2,-7,-7,-4,2,8,1,-5,-10,-9,4,9,-8,-5,4,9,4,-1,-5,-5,10,-5,7,6,-6,-4,-2,2,-3,-8,-4,2,-3,6,7,6,-5,10,5,-1,-8,-3,-7,2,-1,6,-9,3,3,-1,3,10,2,-1,-4,8,-9,-4,-8,-6,-9,6,5,10,-3,8,2,-5,6,3,-10,1,4,6,2,-2,-8,-8,10,-9,-3,-10,-5,-1,-2,-10,-5,-4,6,10,-3,10,-3,-4,-8,-7,-10,-8,-1,-5,-1,-7,-5,7,2,1,2,-7,-2,9,4,3,-2,-10,-7,-9,-9,7,9,5,-1,-7,8,9,4,1,3,-5,-2,1,-9,2,-7,2,-2,5,3,-8,5,10,3,-9,-5,5,-9,-1,-5,6,1,-7,-5,8,-4,9,-2,-1,2,5,-6,7,7,6,8,-3,2,-1,2,-4,-4,8,-2,4,2,-1,10,-8,5,-8,-7,-3,-10,-5,4,1,-2,5,-1,-10,-8,3,-3,4,4,3,2,-10,10,7,7,-1,8,-7,-5,-1,-1,3,-7,2,-9,-3,-10,-5,2,-4,3,-8,-1,9,-1,1,7,6,10,-5,2,2,-5,-2,-1,4,2,-5,8,-9,6,-2,3,-9,5,-4,4,-9,-4,-3,-9,-1,10,2,-1,8,-2,-4,-10,1,-7,-2,-10,-7,4,-1,9,-4,7,-9,-10,10,1,8,-7,5,-4,2,-10,10,10,-8,3,-10,-1,-1,-7,-2,6,-8,-9,-4,1,-8,-4,-8,-10,-3,-10,3,1,-2,-6,-7,-4,-5,1,9,5,5,-6,4,-1,8,10,-5,-7,1,1,8,-4,-2,2,9,9,-5,-8,10,7,-1,9,-8,-2,4,9,-1,-4,-10,-2,-2,-2,5,-7,9,3,3,-7,2,1,5,7,3,-6,-8,1,-1,-10,-2,3,2,-5,-2,5,-4,-10,-4,-2,8,1,10,9,-4,-8,-5,10,-9,-2,7,-4,4,9,-1,-7,1,-7,10,2,5,10,3,9,5,4,1,-3,2,-4,-3,1,9,-4,-6,-10,-6,-4,10,-2,7,9,2,2,3,6,-7,1,9,-2,10,9,-4,-7,-6,-9,3,-2,1,-10,10,-2,6,-2,9,-1,9,6,-3,-6,-2,-4,5,3,-10,2,-10,8,10,-3,7,9,-6,-7,-10,9,-10,-8,-9,-4,-3,-10,3,-10,-9,1,1,-1,-4,7,3,-3,-9,9,3,8,2,-8,-5,5,5,1,5,-2,-10,1,5,6,7,3,-1,-6,8,-5,4,8,-7,5,10,-8,-6,-6,5,6,-9,1,-1,-4,-1,-3,-10,-8,9,10,-1,-4,9,10,1,-5,-7,4,-5,9,7,5,-3,8,-4,-5,-7,2,6,2,-7,2,5,-4,-2,8,-4,-9,-4,1,3,5,-5,-10,8,-10,10,1,-6,8,5,-7,9,-6,-3,10,-2,-10,1,-8,1,-8,-10,8,3,5,-4,-8,10,-5,-2,-9,-10,-1,-8,-2,9,-9,8,-6,-5,-10,5,1,4,6,-1,-10,5,-1,-2,-1,-2,1,-10,-2,10,-6,-10,10,-3,9,5,-2,-5,-1,-6,10,-3,-10,2,9,-4,8,-2,-9,7,6,9,2,2,3,-6,-8,5,-5,9,-10,-9,-8,-9,7,-5,9,2,10,-5,-4,5,3,3,7,-1,7,-5,2,-10,-1,-3,-10,2,-1,-10,-9,10,-5,1,4,-8,4,6,9,-7,2,1,-5,2,9,2,7,1,2,3,-5,-9,-8,5,2,8,-9,5,-9,1,-9,5,4,5,9,4,-10,-3,7,-6,9,2,-2,-6,-4,-8,-10,8,-10,-10,2,4,-6,-10,6,-1,-9,-7,-9,-1,-9,-7,-1,-3,-9,-1,6,5,-4,-4,-3,7,7,3,8,3,5,6,-7,9,1,-7,7,8,6,-4,-8,-1,7,-5,1,4,-7,10,-1,-10,-8,1,8,9,-3,3,3,6,-1,7,-8,6,3,-1,-6,7,7,-1,7,-1,2,2,1,7,1,-3,-7,6,6,4,-8,10,-1,2,-3,-10,6,-10,2,-8,3,3,10,-2,9,-10,1,6,-3,1,1,8,-5,-6,-8,-1,-6,3,-6,-4,-4,-5,6,-6,10,-4,-1,10,-3,-5,1,-3,2,4,-2,-4,5,-1,3,-2,7,5,10,-5,4,-5,-6,3,-4,-8,5,3,3], dtype = "uint16")#candidate|4782|(2112,)|const|uint16
const_4783 = relay.const([-7.356968,-8.420924,8.102102,-0.372442,2.962633,4.745375,-6.472156,1.341647,-5.585248,9.740669,-4.622706,-6.230280,-2.576972,2.121458,5.560944,0.412650,0.226410,-3.755365,-9.947106,-8.285281,2.973052,5.696218,1.836068,5.528028,2.919388,4.381106,-4.566404,-3.628006,0.679231,-6.886402,-4.500046,-9.890112,-0.977521,7.195075,-5.135056,-0.014319,2.816922,9.104543,-3.070721,-0.098593,9.291471,7.513193,-8.905923,-8.003772,9.766102,-0.560509,-6.848609,3.064115,8.914605,-8.238799,-9.295542,7.003936,-9.700393,-6.258646,-7.562715,7.025709,5.352604,8.012574,-2.395892,5.939377,-1.922931,1.779068,7.535570,4.136614,1.183953,-3.135729,-7.183457,-3.427609,-6.205033,8.291886,8.770249,-5.180405,7.488579,-7.448812,-7.718754,5.762864,-6.625900,2.727462,6.969861,-9.889878,-8.904740,6.419681,7.639221,-1.025917,-9.528395,-8.179237,-1.774141,-9.462620,-3.183982,2.387107,2.532040,2.931098,8.846739,3.324366,-3.824571,-1.222001,-7.541343,6.231130,9.777332,9.990264,-0.181635,2.882136,-8.481183,-4.550828,0.909667,7.802246,7.156945,-8.590909,-1.929938,3.836364,3.980820,2.560576,5.462456,6.888942,-4.856298,2.054177,-2.092292,0.627883,-3.230152,0.589113,3.635334,-3.791710,-3.923697,-7.281386,-3.157701,2.102682,2.573377,3.812214,6.107089,1.669274,2.545138,-9.870198,4.187557,4.500952,-6.668147,7.424021,1.742810,-5.463062,-7.754520,-4.939155,-6.731595,2.949553,7.563051,3.799283,4.601649,-5.919047,8.237281,7.442655,7.448602,-0.951331,2.328974,0.944783,-5.665052,-4.314449,-3.493815,9.045811,-1.461757,-8.285892,-7.341950,6.877251,-1.414380,-1.680547,-8.668643,5.505347,-7.093877,8.433701,3.887938,0.829193,-9.407628,5.293495,-3.683891,-2.241015,8.882416,-0.302233,-5.569181,2.889943,-5.040063,-1.812763,9.337544,-0.343399,3.866087,-0.096969,-1.860663,-5.278829,2.675880,-9.847838,4.393951,0.446730,3.868378,-7.909072,2.984590,2.679496,0.440450,-5.869329,8.609428,1.113920,7.272385,5.861355,5.559267,-7.924900,3.695900,-7.843207,7.560501,8.986043,-5.726986,-2.882508,-6.667990,3.789770,9.083579,-6.171949,-3.093663,-1.545226,5.675217,0.602631,4.477040,-6.891358,-5.270063,6.753033,-2.891069,5.412743], dtype = "float32")#candidate|4783|(220,)|const|float32
call_4781 = relay.TupleGetItem(func_3242_call(relay.reshape(const_4782.astype('uint16'), [12, 16, 11]), relay.reshape(const_4782.astype('uint16'), [12, 16, 11]), relay.reshape(const_4783.astype('float32'), [220,]), ), 5)
call_4784 = relay.TupleGetItem(func_3246_call(relay.reshape(const_4782.astype('uint16'), [12, 16, 11]), relay.reshape(const_4782.astype('uint16'), [12, 16, 11]), relay.reshape(const_4783.astype('float32'), [220,]), ), 5)
uop_4786 = relay.rsqrt(const_4782.astype('float64')) # shape=(2112,)
output = relay.Tuple([call_4757,call_4764,call_4781,const_4783,uop_4786,])
output2 = relay.Tuple([call_4758,call_4765,call_4784,const_4783,uop_4786,])
func_4829 = relay.Function([], output)
mod['func_4829'] = func_4829
mod = relay.transform.InferType()(mod)
output = func_4829()
func_4830 = relay.Function([], output)
mutated_mod['func_4830'] = func_4830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_4892 = relay.TupleGetItem(func_4335_call(), 0)
call_4893 = relay.TupleGetItem(func_4336_call(), 0)
func_4474_call = mod.get_global_var('func_4474')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_4902 = relay.TupleGetItem(func_4474_call(), 0)
call_4903 = relay.TupleGetItem(func_4476_call(), 0)
var_4909 = relay.var("var_4909", dtype = "float64", shape = (33,))#candidate|4909|(33,)|var|float64
bop_4910 = relay.minimum(call_4892.astype('uint16'), relay.reshape(var_4909.astype('uint16'), relay.shape_of(call_4892))) # shape=(33,)
bop_4913 = relay.minimum(call_4893.astype('uint16'), relay.reshape(var_4909.astype('uint16'), relay.shape_of(call_4893))) # shape=(33,)
uop_4920 = relay.log10(call_4902.astype('float32')) # shape=(10080,)
uop_4922 = relay.log10(call_4903.astype('float32')) # shape=(10080,)
output = relay.Tuple([bop_4910,uop_4920,])
output2 = relay.Tuple([bop_4913,uop_4922,])
func_4931 = relay.Function([var_4909,], output)
mod['func_4931'] = func_4931
mod = relay.transform.InferType()(mod)
var_4932 = relay.var("var_4932", dtype = "float64", shape = (33,))#candidate|4932|(33,)|var|float64
output = func_4931(var_4932)
func_4933 = relay.Function([var_4932], output)
mutated_mod['func_4933'] = func_4933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3101_call = mod.get_global_var('func_3101')
func_3103_call = mutated_mod.get_global_var('func_3103')
call_4935 = relay.TupleGetItem(func_3101_call(), 0)
call_4936 = relay.TupleGetItem(func_3103_call(), 0)
func_1074_call = mod.get_global_var('func_1074')
func_1075_call = mutated_mod.get_global_var('func_1075')
call_4959 = func_1074_call()
call_4960 = func_1074_call()
func_4371_call = mod.get_global_var('func_4371')
func_4373_call = mutated_mod.get_global_var('func_4373')
call_4983 = relay.TupleGetItem(func_4371_call(), 0)
call_4984 = relay.TupleGetItem(func_4373_call(), 0)
uop_4985 = relay.acosh(call_4983.astype('float64')) # shape=(33,)
uop_4987 = relay.acosh(call_4984.astype('float64')) # shape=(33,)
func_4627_call = mod.get_global_var('func_4627')
func_4628_call = mutated_mod.get_global_var('func_4628')
call_5006 = func_4627_call()
call_5007 = func_4627_call()
func_1541_call = mod.get_global_var('func_1541')
func_1543_call = mutated_mod.get_global_var('func_1543')
call_5012 = relay.TupleGetItem(func_1541_call(), 0)
call_5013 = relay.TupleGetItem(func_1543_call(), 0)
output = relay.Tuple([call_4935,call_4959,uop_4985,call_5006,call_5012,])
output2 = relay.Tuple([call_4936,call_4960,uop_4987,call_5007,call_5013,])
func_5028 = relay.Function([], output)
mod['func_5028'] = func_5028
mod = relay.transform.InferType()(mod)
mutated_mod['func_5028'] = func_5028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5028_call = mutated_mod.get_global_var('func_5028')
call_5029 = func_5028_call()
output = call_5029
func_5030 = relay.Function([], output)
mutated_mod['func_5030'] = func_5030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4188_call = mod.get_global_var('func_4188')
func_4189_call = mutated_mod.get_global_var('func_4189')
call_5031 = relay.TupleGetItem(func_4188_call(), 4)
call_5032 = relay.TupleGetItem(func_4189_call(), 4)
output = relay.Tuple([call_5031,])
output2 = relay.Tuple([call_5032,])
func_5040 = relay.Function([], output)
mod['func_5040'] = func_5040
mod = relay.transform.InferType()(mod)
output = func_5040()
func_5041 = relay.Function([], output)
mutated_mod['func_5041'] = func_5041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5182 = relay.var("var_5182", dtype = "uint64", shape = (8, 6, 10))#candidate|5182|(8, 6, 10)|var|uint64
var_5183 = relay.var("var_5183", dtype = "uint64", shape = (8, 6, 10))#candidate|5183|(8, 6, 10)|var|uint64
bop_5184 = relay.minimum(var_5182.astype('uint64'), relay.reshape(var_5183.astype('uint64'), relay.shape_of(var_5182))) # shape=(8, 6, 10)
output = relay.Tuple([bop_5184,])
output2 = relay.Tuple([bop_5184,])
func_5195 = relay.Function([var_5182,var_5183,], output)
mod['func_5195'] = func_5195
mod = relay.transform.InferType()(mod)
mutated_mod['func_5195'] = func_5195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5195_call = mutated_mod.get_global_var('func_5195')
var_5197 = relay.var("var_5197", dtype = "uint64", shape = (8, 6, 10))#candidate|5197|(8, 6, 10)|var|uint64
var_5198 = relay.var("var_5198", dtype = "uint64", shape = (8, 6, 10))#candidate|5198|(8, 6, 10)|var|uint64
call_5196 = func_5195_call(var_5197,var_5198,)
output = call_5196
func_5199 = relay.Function([var_5197,var_5198,], output)
mutated_mod['func_5199'] = func_5199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_5273 = relay.TupleGetItem(func_4398_call(), 0)
call_5274 = relay.TupleGetItem(func_4399_call(), 0)
output = call_5273
output2 = call_5274
func_5279 = relay.Function([], output)
mod['func_5279'] = func_5279
mod = relay.transform.InferType()(mod)
output = func_5279()
func_5280 = relay.Function([], output)
mutated_mod['func_5280'] = func_5280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3347_call = mod.get_global_var('func_3347')
func_3348_call = mutated_mod.get_global_var('func_3348')
call_5314 = func_3347_call()
call_5315 = func_3347_call()
func_1237_call = mod.get_global_var('func_1237')
func_1239_call = mutated_mod.get_global_var('func_1239')
var_5317 = relay.var("var_5317", dtype = "float32", shape = (528,))#candidate|5317|(528,)|var|float32
call_5316 = relay.TupleGetItem(func_1237_call(relay.reshape(var_5317.astype('float32'), [11, 16, 3])), 1)
call_5318 = relay.TupleGetItem(func_1239_call(relay.reshape(var_5317.astype('float32'), [11, 16, 3])), 1)
output = relay.Tuple([call_5314,call_5316,var_5317,])
output2 = relay.Tuple([call_5315,call_5318,var_5317,])
func_5325 = relay.Function([var_5317,], output)
mod['func_5325'] = func_5325
mod = relay.transform.InferType()(mod)
var_5326 = relay.var("var_5326", dtype = "float32", shape = (528,))#candidate|5326|(528,)|var|float32
output = func_5325(var_5326)
func_5327 = relay.Function([var_5326], output)
mutated_mod['func_5327'] = func_5327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_669_call = mod.get_global_var('func_669')
func_670_call = mutated_mod.get_global_var('func_670')
call_5338 = func_669_call()
call_5339 = func_669_call()
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_5352 = relay.TupleGetItem(func_4335_call(), 0)
call_5353 = relay.TupleGetItem(func_4336_call(), 0)
output = relay.Tuple([call_5338,call_5352,])
output2 = relay.Tuple([call_5339,call_5353,])
func_5363 = relay.Function([], output)
mod['func_5363'] = func_5363
mod = relay.transform.InferType()(mod)
mutated_mod['func_5363'] = func_5363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5363_call = mutated_mod.get_global_var('func_5363')
call_5364 = func_5363_call()
output = call_5364
func_5365 = relay.Function([], output)
mutated_mod['func_5365'] = func_5365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4435_call = mod.get_global_var('func_4435')
func_4437_call = mutated_mod.get_global_var('func_4437')
call_5420 = relay.TupleGetItem(func_4435_call(), 0)
call_5421 = relay.TupleGetItem(func_4437_call(), 0)
output = call_5420
output2 = call_5421
func_5430 = relay.Function([], output)
mod['func_5430'] = func_5430
mod = relay.transform.InferType()(mod)
output = func_5430()
func_5431 = relay.Function([], output)
mutated_mod['func_5431'] = func_5431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mod.get_global_var('func_2824')
func_2825_call = mutated_mod.get_global_var('func_2825')
call_5457 = relay.TupleGetItem(func_2824_call(), 1)
call_5458 = relay.TupleGetItem(func_2825_call(), 1)
func_1704_call = mod.get_global_var('func_1704')
func_1706_call = mutated_mod.get_global_var('func_1706')
call_5460 = func_1704_call()
call_5461 = func_1704_call()
var_5483 = relay.var("var_5483", dtype = "float64", shape = (33,))#candidate|5483|(33,)|var|float64
bop_5484 = relay.logical_or(call_5460.astype('bool'), relay.reshape(var_5483.astype('bool'), relay.shape_of(call_5460))) # shape=(33,)
bop_5487 = relay.logical_or(call_5461.astype('bool'), relay.reshape(var_5483.astype('bool'), relay.shape_of(call_5461))) # shape=(33,)
uop_5488 = relay.sin(call_5457.astype('float32')) # shape=(6, 1680)
uop_5490 = relay.sin(call_5458.astype('float32')) # shape=(6, 1680)
bop_5491 = relay.add(bop_5484.astype('int32'), relay.reshape(call_5460.astype('int32'), relay.shape_of(bop_5484))) # shape=(33,)
bop_5494 = relay.add(bop_5487.astype('int32'), relay.reshape(call_5461.astype('int32'), relay.shape_of(bop_5487))) # shape=(33,)
output = relay.Tuple([uop_5488,bop_5491,])
output2 = relay.Tuple([uop_5490,bop_5494,])
func_5495 = relay.Function([var_5483,], output)
mod['func_5495'] = func_5495
mod = relay.transform.InferType()(mod)
var_5496 = relay.var("var_5496", dtype = "float64", shape = (33,))#candidate|5496|(33,)|var|float64
output = func_5495(var_5496)
func_5497 = relay.Function([var_5496], output)
mutated_mod['func_5497'] = func_5497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2459_call = mod.get_global_var('func_2459')
func_2461_call = mutated_mod.get_global_var('func_2461')
call_5518 = relay.TupleGetItem(func_2459_call(), 0)
call_5519 = relay.TupleGetItem(func_2461_call(), 0)
output = call_5518
output2 = call_5519
func_5538 = relay.Function([], output)
mod['func_5538'] = func_5538
mod = relay.transform.InferType()(mod)
output = func_5538()
func_5539 = relay.Function([], output)
mutated_mod['func_5539'] = func_5539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4474_call = mod.get_global_var('func_4474')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_5562 = relay.TupleGetItem(func_4474_call(), 0)
call_5563 = relay.TupleGetItem(func_4476_call(), 0)
func_752_call = mod.get_global_var('func_752')
func_754_call = mutated_mod.get_global_var('func_754')
call_5565 = func_752_call()
call_5566 = func_752_call()
var_5567 = relay.var("var_5567", dtype = "uint32", shape = (10080,))#candidate|5567|(10080,)|var|uint32
bop_5568 = relay.divide(call_5562.astype('float32'), relay.reshape(var_5567.astype('float32'), relay.shape_of(call_5562))) # shape=(10080,)
bop_5571 = relay.divide(call_5563.astype('float32'), relay.reshape(var_5567.astype('float32'), relay.shape_of(call_5563))) # shape=(10080,)
bop_5574 = relay.subtract(call_5562.astype('uint16'), relay.reshape(var_5567.astype('uint16'), relay.shape_of(call_5562))) # shape=(10080,)
bop_5577 = relay.subtract(call_5563.astype('uint16'), relay.reshape(var_5567.astype('uint16'), relay.shape_of(call_5563))) # shape=(10080,)
var_5580 = relay.var("var_5580", dtype = "uint32", shape = (10080,))#candidate|5580|(10080,)|var|uint32
bop_5581 = relay.floor_divide(call_5562.astype('float32'), relay.reshape(var_5580.astype('float32'), relay.shape_of(call_5562))) # shape=(10080,)
bop_5584 = relay.floor_divide(call_5563.astype('float32'), relay.reshape(var_5580.astype('float32'), relay.shape_of(call_5563))) # shape=(10080,)
bop_5590 = relay.logical_or(bop_5581.astype('bool'), relay.reshape(call_5562.astype('bool'), relay.shape_of(bop_5581))) # shape=(10080,)
bop_5593 = relay.logical_or(bop_5584.astype('bool'), relay.reshape(call_5563.astype('bool'), relay.shape_of(bop_5584))) # shape=(10080,)
uop_5614 = relay.sigmoid(bop_5581.astype('float32')) # shape=(10080,)
uop_5616 = relay.sigmoid(bop_5584.astype('float32')) # shape=(10080,)
bop_5621 = relay.bitwise_and(uop_5614.astype('int16'), relay.reshape(bop_5581.astype('int16'), relay.shape_of(uop_5614))) # shape=(10080,)
bop_5624 = relay.bitwise_and(uop_5616.astype('int16'), relay.reshape(bop_5584.astype('int16'), relay.shape_of(uop_5616))) # shape=(10080,)
func_752_call = mod.get_global_var('func_752')
func_754_call = mutated_mod.get_global_var('func_754')
call_5632 = func_752_call()
call_5633 = func_752_call()
bop_5638 = relay.left_shift(bop_5621.astype('uint16'), relay.reshape(bop_5568.astype('uint16'), relay.shape_of(bop_5621))) # shape=(10080,)
bop_5641 = relay.left_shift(bop_5624.astype('uint16'), relay.reshape(bop_5571.astype('uint16'), relay.shape_of(bop_5624))) # shape=(10080,)
func_3719_call = mod.get_global_var('func_3719')
func_3721_call = mutated_mod.get_global_var('func_3721')
call_5643 = relay.TupleGetItem(func_3719_call(), 3)
call_5644 = relay.TupleGetItem(func_3721_call(), 3)
func_2373_call = mod.get_global_var('func_2373')
func_2377_call = mutated_mod.get_global_var('func_2377')
const_5646 = relay.const([5.648429,-9.025151,7.225245,-8.926021,-3.575935,5.258059,9.976649,7.717985,7.671260,3.280948,9.058220,6.947722,6.137284,-4.284236,8.348345,0.335160,1.780150,-3.122838,5.087448,-2.515549,0.049737,-6.592119,6.052235,6.560978,4.435571,-4.729621,-9.331012,4.183168,1.740779,-0.122930,-6.430592,-8.628260,7.524051,4.691963,3.931722,8.268389,4.261908,6.886832,2.200001,-2.888618], dtype = "float64")#candidate|5646|(40,)|const|float64
var_5647 = relay.var("var_5647", dtype = "float64", shape = (360,))#candidate|5647|(360,)|var|float64
call_5645 = relay.TupleGetItem(func_2373_call(relay.reshape(const_5646.astype('float64'), [1, 8, 5]), relay.reshape(var_5647.astype('float64'), [9, 8, 5]), ), 0)
call_5648 = relay.TupleGetItem(func_2377_call(relay.reshape(const_5646.astype('float64'), [1, 8, 5]), relay.reshape(var_5647.astype('float64'), [9, 8, 5]), ), 0)
output = relay.Tuple([call_5565,bop_5574,bop_5590,call_5632,bop_5638,call_5643,call_5645,const_5646,var_5647,])
output2 = relay.Tuple([call_5566,bop_5577,bop_5593,call_5633,bop_5641,call_5644,call_5648,const_5646,var_5647,])
func_5654 = relay.Function([var_5567,var_5580,var_5647,], output)
mod['func_5654'] = func_5654
mod = relay.transform.InferType()(mod)
mutated_mod['func_5654'] = func_5654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5654_call = mutated_mod.get_global_var('func_5654')
var_5656 = relay.var("var_5656", dtype = "uint32", shape = (10080,))#candidate|5656|(10080,)|var|uint32
var_5657 = relay.var("var_5657", dtype = "uint32", shape = (10080,))#candidate|5657|(10080,)|var|uint32
var_5658 = relay.var("var_5658", dtype = "float64", shape = (360,))#candidate|5658|(360,)|var|float64
call_5655 = func_5654_call(var_5656,var_5657,var_5658,)
output = call_5655
func_5659 = relay.Function([var_5656,var_5657,var_5658,], output)
mutated_mod['func_5659'] = func_5659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4494_call = mod.get_global_var('func_4494')
func_4495_call = mutated_mod.get_global_var('func_4495')
call_5664 = func_4494_call()
call_5665 = func_4494_call()
output = call_5664
output2 = call_5665
func_5692 = relay.Function([], output)
mod['func_5692'] = func_5692
mod = relay.transform.InferType()(mod)
output = func_5692()
func_5693 = relay.Function([], output)
mutated_mod['func_5693'] = func_5693
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5707 = relay.var("var_5707", dtype = "uint32", shape = (9, 4, 8))#candidate|5707|(9, 4, 8)|var|uint32
const_5708 = relay.const([[[-8,-8,-1,-7,5,-8,-3,5],[-8,10,9,-10,-4,6,9,3],[7,2,2,-5,-9,3,10,2],[5,7,1,-7,-6,-8,9,2]],[[-3,-5,4,-9,5,-6,9,2],[-9,10,-8,6,-9,1,-4,-7],[-5,-1,4,-3,3,5,-7,-8],[10,8,-6,-4,-7,-5,5,-7]],[[6,-1,-9,1,-4,-3,-5,-9],[10,3,-2,-3,9,1,1,6],[7,8,-10,5,7,-4,9,-7],[1,-9,6,-3,1,1,-3,1]],[[-2,3,10,-5,5,9,-5,5],[6,-10,-5,7,6,-1,-3,-8],[-1,-9,8,-8,-5,9,3,7],[-7,2,-9,-1,7,5,-2,6]],[[-1,-6,1,6,-1,6,-10,-3],[-2,-10,-2,-8,-2,-10,6,-10],[3,8,10,-9,-8,6,10,6],[2,2,8,6,5,-4,4,-7]],[[-2,10,-10,4,6,7,-9,9],[-10,9,3,8,1,-8,-8,1],[-10,3,-2,10,-6,5,10,1],[6,-6,5,-8,7,-9,-1,-4]],[[-3,-2,3,2,-7,-9,2,-4],[9,-7,5,-9,1,7,10,4],[-10,10,-8,-5,1,3,1,4],[-1,-4,-8,9,3,-3,9,8]],[[-6,3,3,3,9,9,-5,-1],[4,5,8,-3,-1,-6,4,2],[-4,-5,2,-1,6,-2,-3,-9],[8,-10,7,-9,-10,1,-9,-5]],[[7,-10,-10,9,-2,-8,5,5],[1,-4,-9,-1,6,-4,-4,-9],[-8,9,1,3,10,-10,1,2],[1,2,-9,-2,6,1,2,10]]], dtype = "uint32")#candidate|5708|(9, 4, 8)|const|uint32
bop_5709 = relay.right_shift(var_5707.astype('uint32'), relay.reshape(const_5708.astype('uint32'), relay.shape_of(var_5707))) # shape=(9, 4, 8)
bop_5735 = relay.less(var_5707.astype('bool'), relay.reshape(const_5708.astype('bool'), relay.shape_of(var_5707))) # shape=(9, 4, 8)
func_4608_call = mod.get_global_var('func_4608')
func_4609_call = mutated_mod.get_global_var('func_4609')
call_5745 = func_4608_call()
call_5746 = func_4608_call()
func_2075_call = mod.get_global_var('func_2075')
func_2080_call = mutated_mod.get_global_var('func_2080')
var_5759 = relay.var("var_5759", dtype = "float32", shape = (98,))#candidate|5759|(98,)|var|float32
var_5760 = relay.var("var_5760", dtype = "float32", shape = (11, 3))#candidate|5760|(11, 3)|var|float32
var_5761 = relay.var("var_5761", dtype = "float64", shape = (1320, 2))#candidate|5761|(1320, 2)|var|float64
call_5758 = relay.TupleGetItem(func_2075_call(relay.reshape(var_5759.astype('float32'), [7, 7, 2]), relay.reshape(var_5760.astype('float32'), [33,]), relay.reshape(var_5761.astype('float64'), [12, 220]), ), 5)
call_5762 = relay.TupleGetItem(func_2080_call(relay.reshape(var_5759.astype('float32'), [7, 7, 2]), relay.reshape(var_5760.astype('float32'), [33,]), relay.reshape(var_5761.astype('float64'), [12, 220]), ), 5)
output = relay.Tuple([bop_5709,bop_5735,call_5745,call_5758,var_5759,var_5760,var_5761,])
output2 = relay.Tuple([bop_5709,bop_5735,call_5746,call_5762,var_5759,var_5760,var_5761,])
func_5763 = relay.Function([var_5707,var_5759,var_5760,var_5761,], output)
mod['func_5763'] = func_5763
mod = relay.transform.InferType()(mod)
var_5764 = relay.var("var_5764", dtype = "uint32", shape = (9, 4, 8))#candidate|5764|(9, 4, 8)|var|uint32
var_5765 = relay.var("var_5765", dtype = "float32", shape = (98,))#candidate|5765|(98,)|var|float32
var_5766 = relay.var("var_5766", dtype = "float32", shape = (11, 3))#candidate|5766|(11, 3)|var|float32
var_5767 = relay.var("var_5767", dtype = "float64", shape = (1320, 2))#candidate|5767|(1320, 2)|var|float64
output = func_5763(var_5764,var_5765,var_5766,var_5767,)
func_5768 = relay.Function([var_5764,var_5765,var_5766,var_5767,], output)
mutated_mod['func_5768'] = func_5768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3347_call = mod.get_global_var('func_3347')
func_3348_call = mutated_mod.get_global_var('func_3348')
call_5791 = func_3347_call()
call_5792 = func_3347_call()
func_5195_call = mod.get_global_var('func_5195')
func_5199_call = mutated_mod.get_global_var('func_5199')
var_5801 = relay.var("var_5801", dtype = "uint64", shape = (480,))#candidate|5801|(480,)|var|uint64
call_5800 = relay.TupleGetItem(func_5195_call(relay.reshape(var_5801.astype('uint64'), [8, 6, 10]), relay.reshape(var_5801.astype('uint64'), [8, 6, 10]), ), 0)
call_5802 = relay.TupleGetItem(func_5199_call(relay.reshape(var_5801.astype('uint64'), [8, 6, 10]), relay.reshape(var_5801.astype('uint64'), [8, 6, 10]), ), 0)
output = relay.Tuple([call_5791,call_5800,var_5801,])
output2 = relay.Tuple([call_5792,call_5802,var_5801,])
func_5805 = relay.Function([var_5801,], output)
mod['func_5805'] = func_5805
mod = relay.transform.InferType()(mod)
var_5806 = relay.var("var_5806", dtype = "uint64", shape = (480,))#candidate|5806|(480,)|var|uint64
output = func_5805(var_5806)
func_5807 = relay.Function([var_5806], output)
mutated_mod['func_5807'] = func_5807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1419_call = mod.get_global_var('func_1419')
func_1420_call = mutated_mod.get_global_var('func_1420')
call_5809 = relay.TupleGetItem(func_1419_call(), 0)
call_5810 = relay.TupleGetItem(func_1420_call(), 0)
func_5028_call = mod.get_global_var('func_5028')
func_5030_call = mutated_mod.get_global_var('func_5030')
call_5829 = relay.TupleGetItem(func_5028_call(), 2)
call_5830 = relay.TupleGetItem(func_5030_call(), 2)
output = relay.Tuple([call_5809,call_5829,])
output2 = relay.Tuple([call_5810,call_5830,])
func_5831 = relay.Function([], output)
mod['func_5831'] = func_5831
mod = relay.transform.InferType()(mod)
output = func_5831()
func_5832 = relay.Function([], output)
mutated_mod['func_5832'] = func_5832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5430_call = mod.get_global_var('func_5430')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_5859 = func_5430_call()
call_5860 = func_5430_call()
output = call_5859
output2 = call_5860
func_5863 = relay.Function([], output)
mod['func_5863'] = func_5863
mod = relay.transform.InferType()(mod)
mutated_mod['func_5863'] = func_5863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5863_call = mutated_mod.get_global_var('func_5863')
call_5864 = func_5863_call()
output = call_5864
func_5865 = relay.Function([], output)
mutated_mod['func_5865'] = func_5865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2556_call = mod.get_global_var('func_2556')
func_2557_call = mutated_mod.get_global_var('func_2557')
call_5883 = relay.TupleGetItem(func_2556_call(), 0)
call_5884 = relay.TupleGetItem(func_2557_call(), 0)
func_4254_call = mod.get_global_var('func_4254')
func_4257_call = mutated_mod.get_global_var('func_4257')
var_5886 = relay.var("var_5886", dtype = "float32", shape = (15,))#candidate|5886|(15,)|var|float32
call_5885 = relay.TupleGetItem(func_4254_call(relay.reshape(var_5886.astype('float32'), [3, 1, 5])), 1)
call_5887 = relay.TupleGetItem(func_4257_call(relay.reshape(var_5886.astype('float32'), [3, 1, 5])), 1)
func_4627_call = mod.get_global_var('func_4627')
func_4628_call = mutated_mod.get_global_var('func_4628')
call_5888 = func_4627_call()
call_5889 = func_4627_call()
func_2667_call = mod.get_global_var('func_2667')
func_2669_call = mutated_mod.get_global_var('func_2669')
const_5894 = relay.const([-6,-9,7,-10,-7,-6,10,5,9,6,-8,-8,-10,-9,1,-10,-10,4,8,-2,2,3,-8,-3,-4,-2,1,-5,-7,9,-6,-4,9,6,1,4,5,-5,-4,10,9,-10,6,-1,-8,10,9,-2,2,-8,7,-8,7,-7,-6,-1,-3,-3,-6,1,-5,10,4,4,2,-3,-4,-5,-8,4,-9,7,7,10,-6,-9,-1,7,-1,-3,3,-5,-9,-7,-3,1,9,-4,1,10,-7,8,-6,-3,-6,-3,4,-5,8,-10,-5,3,-10,-10,4,-8,-7,-9,1,-3,10,-5,5,7,-2,-6,-9,-2,-9,10,2,-4,-6,3,5,-4,3,-7,-1,-4,3,-3,1,3,-8,1,3,-1,8,-6,-2,-6,-2,-3,-1,-8,-7,9,6,7,-7,6,-4,8,-2,5,-7,-9,5,-3,-1,3,2,7,3,2,2,9,6,10,-4,-10,-5,1,2,-8,-5,-2,-2,4,5,-5,-5,-5,-4,7,-9,8,-9,-5,2,-6,4,-3,9,2,-5,-10,-1,-9,1,2,6,-5,-10,-6,6,9,-1,10,2,-3,9,7,-2,5,-4,-5,-9,-3,-3,-3,-10,2,-7,-3,-4,-5,-4,3,7,-9,-6,-1,-5,6,-5,8,1,9,2,-6,10,9,2,-8,-9,1,-3,2,9,7,-7,1,9,-8,2,9,-5,-6,8,7,-2,3,-3,5,-3,7,-1,9,-8,1,1,4,6,-3,3,-2,-8,-10,9,4,10,-1,-10,9,9,10,9,4,-3,2,6,-8,-10,-7,6,1,3,-6,-6,10,6,3,-5,3,-5,1,8,6,-2,6,-4,-5,-1,-9,10,2,1,-3,4,4,10,9,-7,-5,9,6,-8,-10,5,-8,1,1,5,8,-2,9,8,-10,-4,-3,-6,-6,-3,5,-8,-1,5,10,-7,-1,1,-1,-7,-5,5,4,8,-6,-6,8,-4,-2,-4,8,3,2,-7,-4,-5,-5,-8,2,1,-8,8,3,-7,-10,-7,4,-8,-3,-9,-1,-7,-5,-7,10,6,7,4,-6,4,3,4,1,-4,-9,5,-9,10,7,4,7,5,-2,1,3,-3,7,4,9,6,4,10,4,-9,7,-8,1,-6,2,2,5,4,3,1,7,-2,9,-4,9,-3,7,1,-3,-5,-6,-4,4,-2,3,9,-3,3,-2,-4,-2,-1,8,-9,1,-10,2,-10,10,-3,7,5,4,1,-4,-9,2,5,2,-1,-9,1,-2,8,-3,5,5,-10,-9,-5,6,1,-3,-7,4,9,-8,-7,-1,4,-7,6,10,-9,6,4,-9,7,-3,9,2,-3,8,3,-4,-5,-6,3,6,-7,-7,4,7,-7,8,10,-6,10,-2,5,-10,6,-1,3,10,-8,2,10,5,-2,5,-1,-4,5,8,1,-10,5,6,9,-8,1,-10,7,-10,6,-2,6,-2,1,1,-7,9,-2,-7,-10,-9,5,6,3,-3,-1,8,1,8,-9,6,-2,7,9,-7,1,2,5,7,3,-9,-5,4,8,-9,-3,-2,-1,10,-4,-1,-3,8,2,-8,-5,1,-3,-5,-7,7,-1,-4,7,-2,-1,6,7,-1,-9,-6,-5,4,2,-8,-4,-10,3,5,7,5,-2,3,-4,8,5,-10,9,-8,-3,-1,-3,-2,-4,-10,-4,-3,5,6,10,5,-8,-6,8,9,2,8,10,4,7,-8,-9,9,-5,-3,1,-2,6,-5,4,8,5,-3,-6,-10,3,5,-9,5,-1,10,-10,-10,-4,1,-10,-6,-4,1,-10,-2,1,4,-6,-5,-9,9,-1,6,-4,3,-5,-1,2,9,-5,4,2,7,6,5,8,5,-2,5,7,4,-7,-10,-8,-10,2,10,-1,-2,-2,-2,-10,10,-9,10,2,-7,6,9,-8,9,-2,-4,8,10,2,2,3,3,-8,-8,-4,1,-6,-6,-1,4,3,-8,5,-3,-2,-10,9,-8,4,-7,-3,-10,1,3,10,5,9,-6,-3,-3,6,-1,5,-9,-5,9,5,9,5,7,-3,-1,-8,-7,8,6,-5,6,-6,1,3,1,1,-5,-2,-2,-7,-7,9,-7,-6,-10,10,3,1,7,-5,-4,-8,3,-1,5,9,6,8,7,-6,6,-3,2,-2,9,-7,2,-10,-5,9,3,-6,7,2,-9,-9,4,2,7,7], dtype = "uint8")#candidate|5894|(825,)|const|uint8
call_5893 = func_2667_call(relay.reshape(const_5894.astype('uint8'), [5, 11, 15]))
call_5895 = func_2667_call(relay.reshape(const_5894.astype('uint8'), [5, 11, 15]))
func_1999_call = mod.get_global_var('func_1999')
func_2000_call = mutated_mod.get_global_var('func_2000')
call_5907 = relay.TupleGetItem(func_1999_call(), 0)
call_5908 = relay.TupleGetItem(func_2000_call(), 0)
func_1074_call = mod.get_global_var('func_1074')
func_1075_call = mutated_mod.get_global_var('func_1075')
call_5909 = func_1074_call()
call_5910 = func_1074_call()
func_4474_call = mod.get_global_var('func_4474')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_5919 = relay.TupleGetItem(func_4474_call(), 0)
call_5920 = relay.TupleGetItem(func_4476_call(), 0)
output = relay.Tuple([call_5883,call_5885,var_5886,call_5888,call_5893,const_5894,call_5907,call_5909,call_5919,])
output2 = relay.Tuple([call_5884,call_5887,var_5886,call_5889,call_5895,const_5894,call_5908,call_5910,call_5920,])
func_5938 = relay.Function([var_5886,], output)
mod['func_5938'] = func_5938
mod = relay.transform.InferType()(mod)
mutated_mod['func_5938'] = func_5938
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5939 = relay.var("var_5939", dtype = "float32", shape = (15,))#candidate|5939|(15,)|var|float32
func_5938_call = mutated_mod.get_global_var('func_5938')
call_5940 = func_5938_call(var_5939)
output = call_5940
func_5941 = relay.Function([var_5939], output)
mutated_mod['func_5941'] = func_5941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2888_call = mod.get_global_var('func_2888')
func_2889_call = mutated_mod.get_global_var('func_2889')
call_5973 = relay.TupleGetItem(func_2888_call(), 2)
call_5974 = relay.TupleGetItem(func_2889_call(), 2)
uop_5993 = relay.tan(call_5973.astype('float64')) # shape=(10, 14, 12)
uop_5995 = relay.tan(call_5974.astype('float64')) # shape=(10, 14, 12)
output = relay.Tuple([uop_5993,])
output2 = relay.Tuple([uop_5995,])
func_6000 = relay.Function([], output)
mod['func_6000'] = func_6000
mod = relay.transform.InferType()(mod)
mutated_mod['func_6000'] = func_6000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6000_call = mutated_mod.get_global_var('func_6000')
call_6001 = func_6000_call()
output = call_6001
func_6002 = relay.Function([], output)
mutated_mod['func_6002'] = func_6002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3101_call = mod.get_global_var('func_3101')
func_3103_call = mutated_mod.get_global_var('func_3103')
call_6122 = relay.TupleGetItem(func_3101_call(), 1)
call_6123 = relay.TupleGetItem(func_3103_call(), 1)
func_4435_call = mod.get_global_var('func_4435')
func_4437_call = mutated_mod.get_global_var('func_4437')
call_6137 = relay.TupleGetItem(func_4435_call(), 0)
call_6138 = relay.TupleGetItem(func_4437_call(), 0)
output = relay.Tuple([call_6122,call_6137,])
output2 = relay.Tuple([call_6123,call_6138,])
func_6140 = relay.Function([], output)
mod['func_6140'] = func_6140
mod = relay.transform.InferType()(mod)
mutated_mod['func_6140'] = func_6140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6140_call = mutated_mod.get_global_var('func_6140')
call_6141 = func_6140_call()
output = call_6141
func_6142 = relay.Function([], output)
mutated_mod['func_6142'] = func_6142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_6145 = relay.TupleGetItem(func_970_call(), 2)
call_6146 = relay.TupleGetItem(func_972_call(), 2)
uop_6149 = relay.tan(call_6145.astype('float64')) # shape=(33,)
uop_6151 = relay.tan(call_6146.astype('float64')) # shape=(33,)
output = relay.Tuple([uop_6149,])
output2 = relay.Tuple([uop_6151,])
func_6157 = relay.Function([], output)
mod['func_6157'] = func_6157
mod = relay.transform.InferType()(mod)
mutated_mod['func_6157'] = func_6157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6157_call = mutated_mod.get_global_var('func_6157')
call_6158 = func_6157_call()
output = call_6158
func_6159 = relay.Function([], output)
mutated_mod['func_6159'] = func_6159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2131_call = mod.get_global_var('func_2131')
func_2133_call = mutated_mod.get_global_var('func_2133')
call_6180 = relay.TupleGetItem(func_2131_call(), 1)
call_6181 = relay.TupleGetItem(func_2133_call(), 1)
func_824_call = mod.get_global_var('func_824')
func_826_call = mutated_mod.get_global_var('func_826')
const_6191 = relay.const([0.151563,3.232720,-3.509632,9.378052,-4.914736,4.770978,-0.315685,7.823555,-5.301824,8.255563,-9.864964,-6.931696,2.401155,-9.376743,-8.625253,-0.678834,9.057680,5.636115,1.468523,-7.344292,4.395873,8.620065,-6.788285,6.643962,3.430992,5.976777,-6.331220,-1.816185,-0.454543,-9.218431,0.888020,5.825431,0.941618], dtype = "float64")#candidate|6191|(33,)|const|float64
call_6190 = func_824_call(relay.reshape(const_6191.astype('float64'), [33,]))
call_6192 = func_824_call(relay.reshape(const_6191.astype('float64'), [33,]))
output = relay.Tuple([call_6180,call_6190,const_6191,])
output2 = relay.Tuple([call_6181,call_6192,const_6191,])
func_6216 = relay.Function([], output)
mod['func_6216'] = func_6216
mod = relay.transform.InferType()(mod)
mutated_mod['func_6216'] = func_6216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6216_call = mutated_mod.get_global_var('func_6216')
call_6217 = func_6216_call()
output = call_6217
func_6218 = relay.Function([], output)
mutated_mod['func_6218'] = func_6218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4829_call = mod.get_global_var('func_4829')
func_4830_call = mutated_mod.get_global_var('func_4830')
call_6253 = relay.TupleGetItem(func_4829_call(), 0)
call_6254 = relay.TupleGetItem(func_4830_call(), 0)
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_6304 = relay.TupleGetItem(func_4335_call(), 0)
call_6305 = relay.TupleGetItem(func_4336_call(), 0)
output = relay.Tuple([call_6253,call_6304,])
output2 = relay.Tuple([call_6254,call_6305,])
func_6321 = relay.Function([], output)
mod['func_6321'] = func_6321
mod = relay.transform.InferType()(mod)
output = func_6321()
func_6322 = relay.Function([], output)
mutated_mod['func_6322'] = func_6322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_6383 = relay.TupleGetItem(func_4335_call(), 0)
call_6384 = relay.TupleGetItem(func_4336_call(), 0)
func_970_call = mod.get_global_var('func_970')
func_972_call = mutated_mod.get_global_var('func_972')
call_6396 = relay.TupleGetItem(func_970_call(), 1)
call_6397 = relay.TupleGetItem(func_972_call(), 1)
output = relay.Tuple([call_6383,call_6396,])
output2 = relay.Tuple([call_6384,call_6397,])
func_6406 = relay.Function([], output)
mod['func_6406'] = func_6406
mod = relay.transform.InferType()(mod)
mutated_mod['func_6406'] = func_6406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6406_call = mutated_mod.get_global_var('func_6406')
call_6407 = func_6406_call()
output = call_6407
func_6408 = relay.Function([], output)
mutated_mod['func_6408'] = func_6408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4739_call = mod.get_global_var('func_4739')
func_4741_call = mutated_mod.get_global_var('func_4741')
call_6501 = relay.TupleGetItem(func_4739_call(), 3)
call_6502 = relay.TupleGetItem(func_4741_call(), 3)
var_6515 = relay.var("var_6515", dtype = "float32", shape = (3, 14, 5))#candidate|6515|(3, 14, 5)|var|float32
bop_6516 = relay.multiply(call_6501.astype('uint16'), var_6515.astype('uint16')) # shape=(3, 14, 5)
bop_6519 = relay.multiply(call_6502.astype('uint16'), var_6515.astype('uint16')) # shape=(3, 14, 5)
bop_6525 = relay.logical_xor(call_6501.astype('uint64'), var_6515.astype('uint64')) # shape=(3, 14, 5)
bop_6528 = relay.logical_xor(call_6502.astype('uint64'), var_6515.astype('uint64')) # shape=(3, 14, 5)
output = relay.Tuple([bop_6516,bop_6525,])
output2 = relay.Tuple([bop_6519,bop_6528,])
func_6538 = relay.Function([var_6515,], output)
mod['func_6538'] = func_6538
mod = relay.transform.InferType()(mod)
mutated_mod['func_6538'] = func_6538
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6539 = relay.var("var_6539", dtype = "float32", shape = (3, 14, 5))#candidate|6539|(3, 14, 5)|var|float32
func_6538_call = mutated_mod.get_global_var('func_6538')
call_6540 = func_6538_call(var_6539)
output = call_6540
func_6541 = relay.Function([var_6539], output)
mutated_mod['func_6541'] = func_6541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1359_call = mod.get_global_var('func_1359')
func_1360_call = mutated_mod.get_global_var('func_1360')
call_6551 = func_1359_call()
call_6552 = func_1359_call()
func_824_call = mod.get_global_var('func_824')
func_826_call = mutated_mod.get_global_var('func_826')
const_6593 = relay.const([-5.356015,3.378793,-1.650950,-5.654620,-6.089176,-2.306810,8.107607,3.153992,0.291739,-2.673843,7.016766,-8.769617,4.019031,8.756543,-8.423024,8.092166,-6.831351,-1.587631,2.715712,6.134555,5.159083,6.664929,-6.548799,2.528432,-2.350057,-1.411497,-9.857202,9.948909,6.271905,-6.425125,5.276192,4.978989,-1.269275], dtype = "float64")#candidate|6593|(33,)|const|float64
call_6592 = func_824_call(relay.reshape(const_6593.astype('float64'), [33,]))
call_6594 = func_824_call(relay.reshape(const_6593.astype('float64'), [33,]))
func_4739_call = mod.get_global_var('func_4739')
func_4741_call = mutated_mod.get_global_var('func_4741')
call_6609 = relay.TupleGetItem(func_4739_call(), 2)
call_6610 = relay.TupleGetItem(func_4741_call(), 2)
output = relay.Tuple([call_6551,call_6592,const_6593,call_6609,])
output2 = relay.Tuple([call_6552,call_6594,const_6593,call_6610,])
func_6613 = relay.Function([], output)
mod['func_6613'] = func_6613
mod = relay.transform.InferType()(mod)
output = func_6613()
func_6614 = relay.Function([], output)
mutated_mod['func_6614'] = func_6614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4494_call = mod.get_global_var('func_4494')
func_4495_call = mutated_mod.get_global_var('func_4495')
call_6625 = func_4494_call()
call_6626 = func_4494_call()
output = relay.Tuple([call_6625,])
output2 = relay.Tuple([call_6626,])
func_6651 = relay.Function([], output)
mod['func_6651'] = func_6651
mod = relay.transform.InferType()(mod)
output = func_6651()
func_6652 = relay.Function([], output)
mutated_mod['func_6652'] = func_6652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6406_call = mod.get_global_var('func_6406')
func_6408_call = mutated_mod.get_global_var('func_6408')
call_6669 = relay.TupleGetItem(func_6406_call(), 1)
call_6670 = relay.TupleGetItem(func_6408_call(), 1)
output = relay.Tuple([call_6669,])
output2 = relay.Tuple([call_6670,])
func_6673 = relay.Function([], output)
mod['func_6673'] = func_6673
mod = relay.transform.InferType()(mod)
mutated_mod['func_6673'] = func_6673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6673_call = mutated_mod.get_global_var('func_6673')
call_6674 = func_6673_call()
output = call_6674
func_6675 = relay.Function([], output)
mutated_mod['func_6675'] = func_6675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2459_call = mod.get_global_var('func_2459')
func_2461_call = mutated_mod.get_global_var('func_2461')
call_6684 = relay.TupleGetItem(func_2459_call(), 0)
call_6685 = relay.TupleGetItem(func_2461_call(), 0)
output = call_6684
output2 = call_6685
func_6709 = relay.Function([], output)
mod['func_6709'] = func_6709
mod = relay.transform.InferType()(mod)
mutated_mod['func_6709'] = func_6709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6709_call = mutated_mod.get_global_var('func_6709')
call_6710 = func_6709_call()
output = call_6710
func_6711 = relay.Function([], output)
mutated_mod['func_6711'] = func_6711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5863_call = mod.get_global_var('func_5863')
func_5865_call = mutated_mod.get_global_var('func_5865')
call_6715 = func_5863_call()
call_6716 = func_5863_call()
output = relay.Tuple([call_6715,])
output2 = relay.Tuple([call_6716,])
func_6732 = relay.Function([], output)
mod['func_6732'] = func_6732
mod = relay.transform.InferType()(mod)
mutated_mod['func_6732'] = func_6732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6732_call = mutated_mod.get_global_var('func_6732')
call_6733 = func_6732_call()
output = call_6733
func_6734 = relay.Function([], output)
mutated_mod['func_6734'] = func_6734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1132_call = mod.get_global_var('func_1132')
func_1134_call = mutated_mod.get_global_var('func_1134')
call_6735 = relay.TupleGetItem(func_1132_call(), 0)
call_6736 = relay.TupleGetItem(func_1134_call(), 0)
output = call_6735
output2 = call_6736
func_6743 = relay.Function([], output)
mod['func_6743'] = func_6743
mod = relay.transform.InferType()(mod)
output = func_6743()
func_6744 = relay.Function([], output)
mutated_mod['func_6744'] = func_6744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4494_call = mod.get_global_var('func_4494')
func_4495_call = mutated_mod.get_global_var('func_4495')
call_6776 = func_4494_call()
call_6777 = func_4494_call()
func_1113_call = mod.get_global_var('func_1113')
func_1115_call = mutated_mod.get_global_var('func_1115')
const_6779 = relay.const([7,-8,1,9,-3,-6,-8,9,10,-1,-3,-2,-6,5,8,-5,-9,-9,-6,-10,1,-1,8,6,5,10,-10,2,-7,-9,3,2,-4,10,9,8,-5,-8,-10,-3,-4,6,-7,9,-3,1,-2,-8,3,-8,-10,-2,-7,10,-7,-4,-5,-4,-9,6,-1,10,9,-4,5,-5,-10,2,9,5,-4,-6,1,1,3,6,4,1,-3,8,-7,-3,-9,-4,-6,4,-10,-8,2,-3,-7,-1,4,-6,9,4,-6,4,-1,-6,7,-8,-4,-10,-6,-1,3,-7,8,-3,-9,2,4,-1,-4,6,10,-10,10,9,4,-10,4,5,1,6,5,-5,5,5,-4,-1,-5,-7,1,-1,-7,-4,-6,-2,7,7,7,-10,-10,2,-8,-8,-3,7,4,3,-9,-2,-5,4,-2,1,-4,4,8,8,10,-10,-5,-1,7,10,-8,-10,7,-5,6,-2,9,-4,3,-4,2,-6,-10,-5,10,2,-8,-10,-8,-5,3,5,-1,-8,3,-7,-3,-1,1,-2,3,-8,-8,-7,-5,3,8,-7,-8,-5,-4,-7,7,-2,8,-1,9,4,-8,-6,-3,-1,10,4,-3,-1,3,-6,8,1,3,6,1,-1,-3,4,-7,-9,-4,-5,1,-6,5,-7,1,6,-1,-5,-4,-3,-3,-3,1,9,4,-2,1,-9,1,9,5,-5,-10,7,7,1,7,2,5,-5,5,-5,-9,-3,2,2,9,-2,-8,-3,10,-4,-9,9,6,-4,-5,-9,5,3,-6,-5,-2,4,-7,-2,-10,-6,-3,-4,10,1,-6,8,-2,9,7,3,-10,-7,1,-3,-8,-1,-5,1,2,9,-10,-9,9,2,-9,-3,-9,5,-2], dtype = "uint8")#candidate|6779|(325,)|const|uint8
call_6778 = relay.TupleGetItem(func_1113_call(relay.reshape(const_6779.astype('uint8'), [325,])), 2)
call_6780 = relay.TupleGetItem(func_1115_call(relay.reshape(const_6779.astype('uint8'), [325,])), 2)
output = relay.Tuple([call_6776,call_6778,const_6779,])
output2 = relay.Tuple([call_6777,call_6780,const_6779,])
func_6785 = relay.Function([], output)
mod['func_6785'] = func_6785
mod = relay.transform.InferType()(mod)
mutated_mod['func_6785'] = func_6785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6785_call = mutated_mod.get_global_var('func_6785')
call_6786 = func_6785_call()
output = call_6786
func_6787 = relay.Function([], output)
mutated_mod['func_6787'] = func_6787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_6798 = relay.TupleGetItem(func_4335_call(), 0)
call_6799 = relay.TupleGetItem(func_4336_call(), 0)
output = call_6798
output2 = call_6799
func_6802 = relay.Function([], output)
mod['func_6802'] = func_6802
mod = relay.transform.InferType()(mod)
output = func_6802()
func_6803 = relay.Function([], output)
mutated_mod['func_6803'] = func_6803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1132_call = mod.get_global_var('func_1132')
func_1134_call = mutated_mod.get_global_var('func_1134')
call_6811 = relay.TupleGetItem(func_1132_call(), 0)
call_6812 = relay.TupleGetItem(func_1134_call(), 0)
output = call_6811
output2 = call_6812
func_6823 = relay.Function([], output)
mod['func_6823'] = func_6823
mod = relay.transform.InferType()(mod)
mutated_mod['func_6823'] = func_6823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6823_call = mutated_mod.get_global_var('func_6823')
call_6824 = func_6823_call()
output = call_6824
func_6825 = relay.Function([], output)
mutated_mod['func_6825'] = func_6825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5692_call = mod.get_global_var('func_5692')
func_5693_call = mutated_mod.get_global_var('func_5693')
call_6841 = func_5692_call()
call_6842 = func_5692_call()
output = call_6841
output2 = call_6842
func_6847 = relay.Function([], output)
mod['func_6847'] = func_6847
mod = relay.transform.InferType()(mod)
output = func_6847()
func_6848 = relay.Function([], output)
mutated_mod['func_6848'] = func_6848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6823_call = mod.get_global_var('func_6823')
func_6825_call = mutated_mod.get_global_var('func_6825')
call_6884 = func_6823_call()
call_6885 = func_6823_call()
output = relay.Tuple([call_6884,])
output2 = relay.Tuple([call_6885,])
func_6887 = relay.Function([], output)
mod['func_6887'] = func_6887
mod = relay.transform.InferType()(mod)
output = func_6887()
func_6888 = relay.Function([], output)
mutated_mod['func_6888'] = func_6888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1419_call = mod.get_global_var('func_1419')
func_1420_call = mutated_mod.get_global_var('func_1420')
call_6892 = relay.TupleGetItem(func_1419_call(), 0)
call_6893 = relay.TupleGetItem(func_1420_call(), 0)
uop_6898 = relay.atanh(call_6892.astype('float32')) # shape=(528,)
uop_6900 = relay.atanh(call_6893.astype('float32')) # shape=(528,)
func_4546_call = mod.get_global_var('func_4546')
func_4547_call = mutated_mod.get_global_var('func_4547')
call_6903 = relay.TupleGetItem(func_4546_call(), 3)
call_6904 = relay.TupleGetItem(func_4547_call(), 3)
var_6906 = relay.var("var_6906", dtype = "float64", shape = (2640,))#candidate|6906|(2640,)|var|float64
bop_6907 = relay.divide(call_6903.astype('float64'), relay.reshape(var_6906.astype('float64'), relay.shape_of(call_6903))) # shape=(2640,)
bop_6910 = relay.divide(call_6904.astype('float64'), relay.reshape(var_6906.astype('float64'), relay.shape_of(call_6904))) # shape=(2640,)
func_5195_call = mod.get_global_var('func_5195')
func_5199_call = mutated_mod.get_global_var('func_5199')
var_6923 = relay.var("var_6923", dtype = "uint64", shape = (120, 4))#candidate|6923|(120, 4)|var|uint64
call_6922 = relay.TupleGetItem(func_5195_call(relay.reshape(var_6923.astype('uint64'), [8, 6, 10]), relay.reshape(var_6923.astype('uint64'), [8, 6, 10]), ), 0)
call_6924 = relay.TupleGetItem(func_5199_call(relay.reshape(var_6923.astype('uint64'), [8, 6, 10]), relay.reshape(var_6923.astype('uint64'), [8, 6, 10]), ), 0)
output = relay.Tuple([uop_6898,bop_6907,call_6922,var_6923,])
output2 = relay.Tuple([uop_6900,bop_6910,call_6924,var_6923,])
func_6926 = relay.Function([var_6906,var_6923,], output)
mod['func_6926'] = func_6926
mod = relay.transform.InferType()(mod)
mutated_mod['func_6926'] = func_6926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6926_call = mutated_mod.get_global_var('func_6926')
var_6928 = relay.var("var_6928", dtype = "float64", shape = (2640,))#candidate|6928|(2640,)|var|float64
var_6929 = relay.var("var_6929", dtype = "uint64", shape = (120, 4))#candidate|6929|(120, 4)|var|uint64
call_6927 = func_6926_call(var_6928,var_6929,)
output = call_6927
func_6930 = relay.Function([var_6928,var_6929,], output)
mutated_mod['func_6930'] = func_6930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4236_call = mod.get_global_var('func_4236')
func_4238_call = mutated_mod.get_global_var('func_4238')
call_7060 = relay.TupleGetItem(func_4236_call(), 0)
call_7061 = relay.TupleGetItem(func_4238_call(), 0)
func_4121_call = mod.get_global_var('func_4121')
func_4122_call = mutated_mod.get_global_var('func_4122')
call_7065 = func_4121_call()
call_7066 = func_4121_call()
bop_7071 = relay.add(call_7060.astype('uint16'), relay.reshape(call_7065.astype('uint16'), relay.shape_of(call_7060))) # shape=(10, 14, 12)
bop_7074 = relay.add(call_7061.astype('uint16'), relay.reshape(call_7066.astype('uint16'), relay.shape_of(call_7061))) # shape=(10, 14, 12)
output = relay.Tuple([bop_7071,])
output2 = relay.Tuple([bop_7074,])
func_7075 = relay.Function([], output)
mod['func_7075'] = func_7075
mod = relay.transform.InferType()(mod)
mutated_mod['func_7075'] = func_7075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7075_call = mutated_mod.get_global_var('func_7075')
call_7076 = func_7075_call()
output = call_7076
func_7077 = relay.Function([], output)
mutated_mod['func_7077'] = func_7077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5831_call = mod.get_global_var('func_5831')
func_5832_call = mutated_mod.get_global_var('func_5832')
call_7098 = relay.TupleGetItem(func_5831_call(), 0)
call_7099 = relay.TupleGetItem(func_5832_call(), 0)
output = call_7098
output2 = call_7099
func_7117 = relay.Function([], output)
mod['func_7117'] = func_7117
mod = relay.transform.InferType()(mod)
output = func_7117()
func_7118 = relay.Function([], output)
mutated_mod['func_7118'] = func_7118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4739_call = mod.get_global_var('func_4739')
func_4741_call = mutated_mod.get_global_var('func_4741')
call_7119 = relay.TupleGetItem(func_4739_call(), 2)
call_7120 = relay.TupleGetItem(func_4741_call(), 2)
output = relay.Tuple([call_7119,])
output2 = relay.Tuple([call_7120,])
func_7138 = relay.Function([], output)
mod['func_7138'] = func_7138
mod = relay.transform.InferType()(mod)
mutated_mod['func_7138'] = func_7138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7138_call = mutated_mod.get_global_var('func_7138')
call_7139 = func_7138_call()
output = call_7139
func_7140 = relay.Function([], output)
mutated_mod['func_7140'] = func_7140
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7150 = relay.var("var_7150", dtype = "float64", shape = (4, 5, 9))#candidate|7150|(4, 5, 9)|var|float64
uop_7151 = relay.atan(var_7150.astype('float64')) # shape=(4, 5, 9)
output = uop_7151
output2 = uop_7151
func_7154 = relay.Function([var_7150,], output)
mod['func_7154'] = func_7154
mod = relay.transform.InferType()(mod)
var_7155 = relay.var("var_7155", dtype = "float64", shape = (4, 5, 9))#candidate|7155|(4, 5, 9)|var|float64
output = func_7154(var_7155)
func_7156 = relay.Function([var_7155], output)
mutated_mod['func_7156'] = func_7156
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7163 = relay.var("var_7163", dtype = "uint32", shape = (8, 15, 5))#candidate|7163|(8, 15, 5)|var|uint32
const_7164 = relay.const([[[5,-3,1,8,-6],[-7,-5,1,3,8],[10,-3,7,4,-3],[5,4,-6,1,-2],[-10,9,-10,-9,-8],[-8,-10,-7,-10,-6],[-1,-8,2,-1,-8],[9,-2,3,-1,-6],[9,5,-6,-8,-1],[-9,7,7,-1,-2],[3,-7,10,-8,4],[9,-9,5,-7,4],[-9,-2,2,4,10],[-4,-7,-10,3,-9],[-4,-2,-3,10,2]],[[-9,9,-5,-3,-4],[-7,7,-9,3,7],[-9,-10,-3,8,4],[9,10,7,9,-6],[-2,-3,-7,8,-4],[-1,7,6,4,-5],[-3,-2,-4,-8,-8],[8,-7,2,3,5],[-6,-10,8,3,1],[10,4,-7,-2,3],[-1,-3,2,-2,7],[2,-4,6,-10,3],[1,-5,7,5,-9],[9,-9,-8,-8,-6],[10,8,-10,-7,5]],[[10,-3,-1,7,10],[-4,7,1,-4,6],[4,8,1,8,8],[9,-1,5,5,-10],[9,3,-9,9,-5],[-3,-2,-3,-9,-2],[6,5,4,-9,-1],[1,5,5,-2,7],[-3,8,-1,10,-4],[7,2,7,-1,2],[-7,3,10,-8,-6],[10,5,-5,-1,-6],[-7,-4,4,-2,10],[-8,-10,-1,-1,-1],[-3,-8,-8,-7,-8]],[[-3,6,4,9,-7],[-2,7,8,-2,-8],[7,3,10,-10,8],[9,-5,-9,7,4],[6,-10,10,3,-8],[3,2,1,-7,10],[1,7,6,-4,3],[-6,-4,3,6,-5],[7,-8,-6,-1,-1],[8,-10,-7,-2,-9],[9,-5,-4,8,-4],[-2,3,-10,-2,9],[3,7,-2,-10,-7],[9,-4,8,3,-10],[1,10,4,10,-2]],[[-9,-6,-8,3,3],[7,-4,6,-1,-2],[-8,2,4,7,-2],[-2,-3,1,7,9],[4,1,9,3,-8],[2,5,-5,2,2],[-2,8,1,9,3],[-5,6,-4,7,4],[10,3,-1,-4,-2],[-8,-9,10,-6,-7],[6,4,1,-6,7],[4,-7,-3,-5,3],[3,4,8,5,4],[2,5,-2,6,-3],[-10,-10,-3,-7,-2]],[[-8,10,1,5,-1],[-6,-8,1,-7,10],[9,6,8,4,10],[6,1,9,5,7],[-4,10,-4,-6,9],[-1,-7,-10,8,10],[10,-5,1,4,-1],[-1,4,9,-4,10],[-10,-2,10,9,7],[-6,-5,-9,-7,2],[6,3,7,-9,-6],[2,2,2,-5,-1],[-2,1,-8,-6,5],[-2,-3,2,-8,9],[-2,3,-7,9,8]],[[6,7,-1,-8,-9],[-5,4,10,8,-7],[-6,-7,6,-4,8],[2,-3,-9,-3,1],[8,7,-4,7,4],[8,-6,9,-1,-6],[-4,-10,9,-1,-6],[6,-8,7,-1,3],[-10,-5,6,-8,-4],[5,-5,7,4,-6],[-10,-4,7,-2,6],[4,-6,6,-5,-10],[-1,9,8,7,3],[2,-8,-2,8,5],[-9,3,10,-9,4]],[[-3,4,8,-7,-4],[10,6,2,5,1],[-5,-1,-8,-8,5],[6,-4,2,-4,8],[-1,-4,8,-4,8],[-3,10,1,-4,-4],[-10,10,3,-7,3],[5,-8,1,-6,9],[2,9,5,-9,1],[-1,-6,-7,3,7],[3,-9,2,-5,7],[-4,-5,3,5,2],[-5,-6,-3,1,-7],[3,-10,-1,4,-1],[-1,4,-8,-9,-8]]], dtype = "uint32")#candidate|7164|(8, 15, 5)|const|uint32
bop_7165 = relay.minimum(var_7163.astype('uint32'), relay.reshape(const_7164.astype('uint32'), relay.shape_of(var_7163))) # shape=(8, 15, 5)
output = bop_7165
output2 = bop_7165
func_7169 = relay.Function([var_7163,], output)
mod['func_7169'] = func_7169
mod = relay.transform.InferType()(mod)
mutated_mod['func_7169'] = func_7169
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7170 = relay.var("var_7170", dtype = "uint32", shape = (8, 15, 5))#candidate|7170|(8, 15, 5)|var|uint32
func_7169_call = mutated_mod.get_global_var('func_7169')
call_7171 = func_7169_call(var_7170)
output = call_7171
func_7172 = relay.Function([var_7170], output)
mutated_mod['func_7172'] = func_7172
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7184 = relay.var("var_7184", dtype = "uint32", shape = (1, 12, 15))#candidate|7184|(1, 12, 15)|var|uint32
var_7185 = relay.var("var_7185", dtype = "uint32", shape = (2, 12, 15))#candidate|7185|(2, 12, 15)|var|uint32
bop_7186 = relay.bitwise_xor(var_7184.astype('uint32'), var_7185.astype('uint32')) # shape=(2, 12, 15)
output = bop_7186
output2 = bop_7186
func_7189 = relay.Function([var_7184,var_7185,], output)
mod['func_7189'] = func_7189
mod = relay.transform.InferType()(mod)
var_7190 = relay.var("var_7190", dtype = "uint32", shape = (1, 12, 15))#candidate|7190|(1, 12, 15)|var|uint32
var_7191 = relay.var("var_7191", dtype = "uint32", shape = (2, 12, 15))#candidate|7191|(2, 12, 15)|var|uint32
output = func_7189(var_7190,var_7191,)
func_7192 = relay.Function([var_7190,var_7191,], output)
mutated_mod['func_7192'] = func_7192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_7217 = relay.TupleGetItem(func_3024_call(), 1)
call_7218 = relay.TupleGetItem(func_3025_call(), 1)
func_2075_call = mod.get_global_var('func_2075')
func_2080_call = mutated_mod.get_global_var('func_2080')
const_7220 = relay.const([[0.438817,-0.464715,-4.447590,1.052145,3.630297,-0.701234,1.759946,-1.397340,-4.247119,-2.484413,-9.408679,5.261825,-2.201241,5.542890,-0.560443,-0.553695,7.752192,3.891399,8.502930,7.285894,5.603315,4.628939,-2.518608,-0.223006,-3.307810,1.743104,9.709765,-8.285319,7.234557,-4.571977,-2.491874,8.190060,5.687674,-6.558533,0.405764,8.993912,7.517703,6.629382,2.727162,-6.953318,-3.097290,-4.952077,0.978499,7.183962,-5.509800,-5.908088,-3.104252,-9.914982,-0.640088,1.718256,-7.404307,-8.536590,6.307818,-3.766094,4.789134,-7.075165,-4.328703,5.207330,0.330318,-0.036454,7.731469,3.863739,-4.900667,6.482831,-6.606066,-7.766504,-7.894161,-5.904114,-2.343355,-1.808716,9.346045,4.946681,0.466494,7.575380,0.662854,-0.260379,-9.010022,3.549951,4.925564,4.130461,3.659959,4.952399,6.535083,2.194222,-2.150458,1.192338,-6.814987,9.689634,-4.873969,-3.875638,-0.076757,-6.016677,-3.547810,3.123330,-1.918099,2.205830,-3.158290,8.101963]], dtype = "float32")#candidate|7220|(1, 98)|const|float32
const_7221 = relay.const([2.842174,6.217503,-5.377558,0.547319,9.547848,2.647429,6.268256,2.966208,-6.767036,2.995742,5.633028,-2.235283,7.867442,7.575337,0.336651,-0.257458,-9.732725,8.671624,8.311412,-8.428859,-1.366896,-9.649186,1.910027,-6.384711,8.838931,-5.717882,0.563133,-3.269628,0.886382,5.042273,6.343152,6.464390,6.350202,1.851978,-3.075768,3.259680,3.200413,-4.656682,-6.527852,-4.938301,-7.260593,-3.394513,2.609748,9.623329,9.923364,4.482851,-2.872929,-1.172852,1.082642,-4.338105,5.207204,-2.903304,2.279284,-3.093034,2.719961,1.205545,8.674486,1.191663,-0.262334,0.435147,9.828747,0.823314,-2.978296,5.722978,9.331524,1.508787,-9.153000,6.664130,-5.497850,5.572265,6.314248,5.067015,-9.871927,4.655419,6.607685,-9.687868,-9.276507,-9.202915,-3.296913,-4.027198,1.087416,-5.801199,-0.149839,6.279659,7.394502,-9.507457,-3.570960,1.548920,2.473685,0.484369,-9.016037,2.660264,0.396153,3.713880,-7.385195,3.743217,1.211506,1.305808,-9.956701,-8.196238,8.587986,-8.958693,-6.914375,-3.768081,-4.755311,5.665744,-3.228858,4.715904,-7.922872,2.041051,8.007818,8.203267,-6.506279,-8.273675,5.750792,1.364480,4.494350,-0.459566,3.615303,9.661000,6.848554,-4.663484,-1.951339,6.633311,-3.035758,3.283562,-4.456779,-2.420981,6.785611,0.277920,3.553168,6.472839,-5.050893,9.859784,-3.708013,2.329196,4.983460,1.532881,-5.526454,-7.044388,0.046021,-1.750017,-4.277268,6.258008,0.015476,1.925020,7.788193,4.283381,-8.933649,3.790335,-8.195854,-1.235539,0.381969,4.285633,8.978393,-3.189357,9.562352,-4.259592,-7.390287,7.045789,-8.645037,-1.781655,1.421550,0.632477,-6.578826,-9.765618,3.173744,-7.190443,1.677713,-2.266836,-1.784191,4.325765,7.593216,5.267650,8.685601,2.109587,7.939255,2.544143,-0.675225,5.289336,-4.736055,4.510022,-3.067093,-1.868502,3.194226,-5.528642,1.561710,5.176268,5.711832,-0.700485,7.154539,-2.050038,-3.810580,4.275645,-7.597317,3.717767,-4.404754,9.784949,9.721298,-4.404870,-6.813408,-5.211613,8.074892,7.353528,-1.120326,0.264277,8.928767,9.345537,-4.093032,-1.700300,4.798392,0.265751,-0.900563,-2.143253,-4.829579,-7.858815,-9.288405,-0.169205,-2.736639,-1.791981,-7.162812,-3.074156,-5.534639,2.404476,-3.463581,9.955937,9.962570,-8.962630,6.238528,7.374920,3.323667,4.386902,-9.576987,1.916359,0.437915,-1.309219,-3.790653,0.346779,-1.917557,2.241227,5.154327,-8.014402,4.833123,-2.398343,3.777927,-9.252792,-9.097293,-6.031064,7.867010,9.539269,-9.424163,-7.414814,9.435145,4.406478,-6.010397,-9.596467,3.430220,5.258061,0.217090,-2.754558,6.924067,-1.058198,-9.351861,7.801849,-6.130250,-0.039381,-3.508532,4.397779,-7.018275,7.201258,4.018572,-2.241515,-7.454249,2.976047,-6.075856,-2.002078,-1.593238,5.044735,-0.071028,9.922369,4.999669,2.439895,-8.351154,7.465429,7.016620,-6.361029,2.614571,2.824860,-2.303396,2.806751,-5.750092,-5.565388,-0.014535,2.578382,-1.801864,-3.079999,-8.307090,3.420708,-7.409247,-3.959492,0.737480,3.718332,1.334494,-0.970593,4.955312,-4.953670,-1.518618,9.037044,-7.283039,7.155511,0.577008,7.579414,4.162082,-9.483902,6.673856,6.332522,1.538554,3.760761,6.435759,-2.000369,-9.705700,7.249218,-0.622410,3.716788,9.270455,0.279675,-3.608427,9.728255,-9.458761,-2.444388,-2.728508,-1.776155,-5.721620,-9.981458,-2.741050,-7.025057,-1.178666,3.979231,-5.755710,0.472412,2.409128,-0.281053,5.937945,9.574846,-3.344029,-1.462871,8.945481,-6.630578,-6.045543,0.093527,-7.624211,4.782477,2.189616,2.351322,-3.292348,-1.890959,4.303943,4.357856,-5.547805,-0.811213,-1.760462,8.055515,-1.835840,6.016224,-8.998658,7.338432,6.598569,4.244255,6.651591,-2.677546,-4.119158,2.606614,-2.659129,-1.522567,1.628435,8.337847,9.785921,1.441922,-8.691798,9.869807,6.995093,2.873707,1.579586,-3.950008,6.998538,-4.655350,7.740419,-8.165359,6.926935,-2.686179,1.161962,-4.368049,-3.147499,-5.101690,6.464089,8.543249,-9.404194,9.116158,-1.181118,-5.798827,-6.492753,1.740681,-1.353554,1.460463,-4.172028,-0.256455,7.060936,5.889890,-8.286944,4.717154,0.139184,3.665972,4.995902,7.899479,-5.367443,-1.489961,8.292045,-9.711217,7.887269,1.042317,3.204450,5.658127,-9.225833,-8.378476,9.368590,-1.029775,-4.739501,-6.857802,-3.590019,4.365885,-5.276361,-1.249058,5.854989,8.069728,-7.845197,5.617190,9.222125,3.545722,4.571275,-6.024449,0.142025,4.491352,-6.904681,8.672004,5.463168,7.133644,-5.593463,2.517169,-7.079547,-7.263790,3.765883,-4.457812,5.913564,7.629651,3.901485,7.636795,-4.117150,4.555754,-2.489702,-6.541890,8.973945,1.953938,1.055919,-4.390733,-2.577817,-7.473869,-5.385529,-3.161145,-4.445635,-8.544839,2.133286,-7.138786,-8.420257,4.475693,3.560978,-3.232173,9.225250,-7.038989,2.710570,8.493987,-6.103955,9.097207,-5.053292,-6.064909,0.600235,5.391738,-6.149266,4.126015,6.509515,4.205015,-9.956507,1.179430,-2.670502,-1.541242,-8.233457,1.010927,2.770354,8.403763,-3.724655,2.207986,-2.596104,-3.147514,-9.659345,2.194666,-7.667995,-0.261465,5.495204,3.731687,-5.667781,6.389675,5.011585,1.902846,1.008387,-1.768171,-8.889041,-2.551095,-8.614445,0.130575,-5.768144,-3.744434,0.691891,4.135516,1.629471,-0.856030,-4.996401,-2.441398,-0.787536,-1.592621,6.445194,1.988547,-5.710724,-9.748672,7.261901,-6.006496,2.667570,-6.809253,2.362815,3.686143,-8.973208,-0.552072,7.901200,-5.502134,-4.404225,7.708322,-4.068599,2.887985,-1.435654,9.221402,2.579696,5.206777,7.745799,-2.612782,3.149624,7.578548,5.560093,-7.976983,-0.870752,9.406538,-8.722806,-2.458745,8.413193,0.034149,-7.258826,9.940096,-0.730344,-1.072896,0.997967,6.343310,-2.682670,-1.645781,-8.927147,-1.245227,-7.548735,-1.857270,-0.939276,8.262725,-6.739335,-9.549838,6.809668,4.057329,-3.714341,7.461569,-7.610148,7.599801,4.599519,-2.009412,-8.150730,0.832784,-4.447704,7.724627,-7.179724,4.165595,-7.701509,7.193839,2.058476,3.128824,-9.857328,1.934463,1.337340,1.882382,3.698788,4.365587,-2.870180,-4.513579,-4.250184,-0.338501,-5.592291,6.306150,7.913746,-1.219504,2.382283,-8.644068,5.001757,-1.804334,-8.274654,9.744770,-1.684245,-5.552649,8.917486,1.596178,-7.072243,9.885149,6.069626,7.065230,3.170798,-4.918676,-1.308596,2.642767,-0.086738,-6.538295,7.720967,-8.896315,-4.245461,9.164099,5.207098,9.948229,-0.339533,-6.364130,-7.351483,-1.477050,-0.566386,-9.294472,9.537771,-2.433355,-1.761109,0.285351,-5.635197,0.704752,-8.196093,3.051845,7.701733,5.180794,5.261229,-0.849640,-7.802281,2.083167,8.467869,0.092176,3.458161,-2.114952,-3.641214,-7.638712,-0.370593,-1.090156,-8.412142,-2.779214,-8.731841,8.755979,-5.987030,5.833906,-0.635404,9.341188,1.500048,-7.549855,-7.981863,-7.572063,-4.375561,7.199477,-7.786764,7.734939,2.475106,-7.053435,-1.379967,0.134803,9.850654,0.641923,-0.216019,2.415479,1.540512,-0.099008,9.060686,-1.533794,7.483183,-6.488828,9.167863,-7.559451,7.611592,6.123330,-3.883205,-9.651835,3.964517,6.859127,-9.369916,7.073427,0.147763,2.346168,-3.310028,-2.932493,-7.225655,0.044035,8.659473,-9.627136,8.712379,-0.619632,2.914728,8.305575,-3.637621,-3.060284,-5.122361,-9.316270,5.311970,-4.703874,1.222809,-4.988085,4.913848,-4.560464,8.308886,1.669276,-5.780711,0.570126,4.390307,-4.052699,3.843901,-0.285852,3.694758,2.082390,2.411747,-9.735861,4.650596,-2.314900,8.354103,9.664479,2.183774,3.359127,-3.425199,6.676071,1.895343,5.922017,-2.961782,-6.355642,-9.418756,9.853056,6.234549,-6.819167,-1.559480,9.368407,7.949387,-4.964743,-2.270041,-8.185180,-8.636645,-5.905835,-0.604582,9.197603,6.376780,-5.865687,8.431805,2.007956,3.085502,3.347468,-6.840012,0.744327,0.783340,1.039331,8.888736,-7.538694,9.251031,-2.842982,-5.265569,3.661781,5.633447,2.560407,8.092224,-1.169502,1.625704,-7.142139,-1.164457,6.116075,7.331753,0.590306,3.948272,6.173328,-7.521135,-8.985014,1.395065,2.974566,4.872043,5.987306,6.959362,9.791213,-9.090183,2.281870,-9.275730,-7.696214,0.426021,-8.014692,-4.804433,5.311412,0.604631,3.460736,0.439976,-2.794444,-1.438861,0.422982,3.170710,-1.272997,-3.038397,-6.028445,-0.329142,5.836675,3.951763,-0.885693,3.987709,-8.282850,1.930328,9.425917,-5.034449,2.981066,4.844690,7.119117,-7.506884,-4.060794,3.747100,2.201217,-8.232927,7.572375,-9.645722,3.192375,9.450529,3.929131,9.811760,-9.086391,-0.360491,-7.853113,-5.492727,-1.561199,4.218766,-1.497380,0.702100,2.383905,-0.471543,5.717704,-9.265601,-0.584017,1.270438,8.604882,-2.969676,-6.174175,1.116051,-3.459846,-9.975066,-2.680202,-5.908425,-6.303140,-8.675500,8.226512,-8.143237,-2.797905,1.416922,9.355697,-6.869876,9.163614,-7.929157,5.771521,9.990156,5.248804,-1.091585,1.523349,-9.865496,-9.085826,7.393324,0.744641,1.405625,6.236041,-3.890936,8.858454,8.096910,6.284851,-1.900531,5.648010,2.720360,-7.475013,1.047467,-3.092167,6.615874,-2.084166,-4.853586,4.099199,5.733118,-6.285551,1.435370,-6.774535,-7.735486,-0.771054,-3.290123,-7.185208,-2.710827,5.416644,4.081706,-8.838470,5.714508,6.033453,-3.403466,7.950502,4.312870,-3.919883,7.556436,1.680281,-5.179174,-9.445399,-6.715610,-8.680326,1.749791,-3.415168,2.541310,-8.196907,4.762093,-6.920156,-4.205134,-6.537031,6.108366,-7.453517,5.176968,0.105212,5.976108,1.915486,-4.725074,-6.780425,2.650753,-5.158493,8.398415,4.381249,0.713768,2.600828,8.803186,7.551982,-6.692601,8.635084,-0.626455,5.017440,3.678717,8.261035,4.601963,0.546844,-1.723782,8.165848,-0.929422,-8.426246,7.206226,8.505815,4.832797,0.863479,-2.728623,-9.811021,8.015652,-8.382109,-2.786277,7.942595,-4.855035,-2.154276,-0.322017,-8.928554,6.924234,-4.286057,-6.770631,2.508458,3.572809,8.837292,-0.931461,-0.439866,-8.307146,-4.672878,-4.181293,-9.284624,-9.963115,6.166853,-4.148160,-1.954482,-3.909617,-9.110215,-2.620024,7.513526,4.819105,-2.157459,-5.739098,5.812727,6.811053,3.746440,2.555639,-9.001581,-7.371932,1.568520,-7.954616,-3.317041,-8.784944,9.436445,7.086757,-5.303138,-0.133678,-7.741980,4.184566,2.160059,9.596657,-8.498935,-4.390797,-7.206803,-5.970566,1.526703,6.467356,-8.785560,8.154656,2.765659,-0.999060,7.340478,-9.740986,9.570869,8.268410,-8.922270,7.683908,-4.510239,-5.486062,-6.491425,-8.174258,9.805964,-7.804584,2.834848,1.480784,-5.652753,9.961005,-9.669365,7.558697,3.417251,-1.724945,8.200632,0.610935,3.168419,-8.130351,-6.005936,-5.911705,5.075022,7.826386,-3.934726,2.299563,-4.892743,-1.652205,-5.875988,-8.352190,-0.690154,6.333473,-5.373296,5.304283,-4.112009,-0.522288,-3.206248,-8.245796,8.020412,8.187050,6.032848,-9.126632,7.199980,-7.682648,-4.029111,4.330176,-9.080342,-3.502112,5.167626,-2.518435,4.129840,3.072985,8.543575,4.228064,2.936029,-6.382068,7.676184,2.531836,4.790599,-4.312850,-9.101057,2.849431,1.646394,-7.555837,5.870791,-4.803250,5.977053,8.314089,-5.905006,9.461790,4.545261,-9.992064,-4.753806,6.092837,9.806268,0.469469,1.289428,-8.362200,-7.284056,-6.527443,-6.809241,-2.372161,-1.379608,-1.126639,1.228309,-5.706507,-8.873915,6.764212,-5.892995,-1.509931,4.481586,-9.431532,-3.738099,2.530293,8.531456,8.485216,-3.221519,2.557028,5.826405,7.928152,9.064064,9.868346,-4.392411,-3.953794,5.121157,4.783493,-8.016487,7.078006,-3.709642,5.092608,-7.283367,6.586114,-3.138189,6.753195,2.477262,-2.350933,2.670746,-1.711273,7.573427,-4.739197,2.600038,4.289126,8.305336,4.973633,0.590624,0.982972,0.778071,-4.347404,4.952734,6.459340,9.400539,7.974793,4.617112,-5.784852,-1.578549,2.750252,-7.197759,9.904806,3.086783,-4.256224,3.936658,7.956937,-3.397850,6.465898,2.551172,-7.479550,-7.720404,1.197976,1.291938,-2.137330,5.526069,-4.270755,-5.320890,6.714918,-4.610727,-4.189629,-5.662466,-5.450561,-0.934688,-2.162142,-0.070690,-0.264576,5.866103,-9.602304,0.913365,-2.459931,-5.890273,6.753747,1.514738,-4.760861,-4.059504,9.813940,-8.685613,5.092610,0.188883,7.165940,2.246620,4.244558,9.004960,2.541606,-1.532884,2.428744,-9.467133,-5.138202,-9.562998,8.692704,8.486093,3.440085,-6.423804,-0.402879,-4.270933,7.302183,7.374491,-5.767298,-8.980114,-1.804486,-3.601930,5.705904,-2.100644,-6.077880,5.709371,3.133083,-8.827812,-9.996562,4.296794,5.822747,-1.208322,8.101600,4.464546,7.275553,-6.776273,-2.860246,6.195923,1.184036,5.111482,-8.622464,-0.935036,-0.208321,-1.966145,7.810658,5.470244,-5.953265,-2.485946,-5.105370,4.648901,1.518270,0.439699,-2.583941,-6.790798,-1.529281,1.991666,-0.002878,-2.911624,1.543776,3.120903,-3.687710,8.038389,3.259597,6.449429,0.223817,2.142688,-1.721399,-4.343181,7.296297,-8.442678,6.382150,8.823902,2.071307,-0.358023,-0.777221,-7.674783,-6.192774,8.793514,2.807917,4.954160,-8.964019,0.306966,5.267362,6.347515,-6.225652,-8.075477,-0.459318,3.009044,0.125955,-8.586215,-7.236639,8.949841,-1.006433,-0.227172,3.220998,-4.825433,-4.150765,-9.893385,3.074121,-7.127136,4.844578,3.130466,-8.309718,-6.424309,-8.857955,-2.482851,1.466818,-5.269051,-2.042606,6.256542,-2.261994,1.313983,7.178843,3.717740,-5.012133,9.897285,-0.193398,8.971627,0.108275,7.762973,-5.237618,-8.780145,9.540834,8.479236,3.926000,2.365497,-2.579854,-3.025717,-2.863136,-9.206016,-7.429119,-3.361632,4.341771,4.536076,3.274932,-1.508442,-1.463333,8.367896,6.258312,-1.101569,6.247572,3.299464,-3.111003,-7.547808,8.187387,8.853323,-4.056952,-8.909519,9.904811,-2.430500,-8.737465,-5.347662,-8.285065,-7.062290,-4.422243,-8.590985,-4.498553,0.240059,-5.245376,1.387358,2.023177,8.714683,2.589867,1.045213,8.632853,0.358688,-8.891130,6.609602,-5.791660,6.321827,-7.026080,-8.776147,2.004522,6.421726,7.016373,1.906746,-2.900750,-5.082122,-5.483872,-7.843085,-7.958803,-9.908617,-3.695289,7.368419,8.155817,5.089738,-6.328343,9.199130,-8.625042,4.953819,5.824481,-5.107519,8.025374,1.895488,-5.583961,-5.735061,-9.183896,1.832950,-2.467529,0.548031,4.804520,3.151537,-2.768399,6.782653,5.419433,1.699593,2.990795,-6.048153,-3.813563,7.889864,-1.063974,6.671681,-8.948135,1.079475,7.871768,-7.492862,8.773795,2.110402,-3.170516,-9.700090,4.500766,8.545258,8.634970,-5.340675,3.554334,-8.988996,9.228834,-4.463425,9.288663,-5.692072,-3.659779,6.076691,-2.178534,-7.093262,-8.876691,-9.099240,-7.486172,-6.591492,-3.157377,5.169970,-1.391086,7.802517,-9.467064,0.075821,7.484477,-7.366561,7.105883,8.791435,-6.353524,-9.616130,4.113697,3.570115,-2.035134,2.606879,-9.162584,3.898972,1.809813,-6.742358,-8.044374,0.050732,1.333992,-9.916890,8.256626,-0.563195,0.192221,-2.216872,2.808095,-9.131887,-8.107775,-0.185776,-0.524293,1.854550,-0.747645,7.365380,-8.735460,-0.376410,0.574572,-7.610271,6.575588,-0.184790,0.650655,2.090479,-2.078633,0.139838,4.977980,2.748013,8.085226,6.661704,-7.344264,-5.461793,9.508359,-4.080239,2.208344,-3.800507,8.158035,8.045003,0.703634,-3.875494,-5.034732,-4.641741,6.079587,-5.131859,1.066831,7.034051,-2.276188,-1.410486,-9.446854,-2.838995,2.706993,-7.009098,-6.798347,5.025657,-7.593851,8.285675,3.924347,1.909566,-4.400386,3.553733,6.837269,0.113167,3.869346,-5.655673,9.184996,9.962340,1.777159,5.233756,-2.866426,6.748866,-2.888168,9.786158,5.555668,1.990846,-0.487457,8.427017,7.086701,-7.333575,-3.781711,-8.269626,7.468774,-6.907787,-6.443965,-8.331247,-9.101865,6.391302,9.676671,4.993553,6.683604,-8.114026,1.378958,-8.129349,-5.113998,5.605712,7.965050,-4.668012,-4.294912,7.967631,7.022942,8.328204,7.580420,-9.278113,8.511232,5.134605,-3.779580,8.668515,1.851350,-7.877149,-2.556986,-1.002257,-9.038642,-3.572679,7.302970,0.406919,-4.447438,5.413071,0.383467,-4.438422,1.027506,-8.604237,6.023008,2.820606,9.440819,-6.071373,-9.725738,3.099813,-3.569350,7.577126,8.905791,-6.077060,6.884935,3.272571,9.010172,0.040451,-5.765846,3.789567,1.375162,-9.402057,-4.891470,-7.301915,-4.866327,4.622775,-1.852087,-5.192478,0.660503,6.110221,-4.644939,-4.914583,-8.747242,-9.665385,6.441482,-7.966392,0.829988,9.255402,9.843584,-9.921757,4.383995,-2.699626,-4.110804,9.289356,5.914623,-3.179493,3.360196,-8.325595,-0.806929,-1.581194,-0.202959,6.885870,-3.762278,3.920665,-8.887884,5.614099,-7.116808,9.980415,-6.811735,-3.595959,9.968931,-6.140042,4.488115,-8.040986,9.348524,9.028306,6.629943,8.496480,9.081360,-9.355075,-4.661862,6.616680,2.246457,2.022392,8.025222,-3.499287,-9.947753,-3.186612,8.902895,-6.149871,8.690620,-9.535710,-2.339819,-4.821927,-1.244253,3.217712,-5.967539,7.208506,-4.816126,-7.758671,2.176227,-6.333109,6.767307,6.115077,-0.862441,4.527922,-9.409821,-5.670564,-7.619137,-6.400970,6.358328,3.495300,9.203898,-6.138408,-8.783379,6.836386,2.728904,3.946944,-2.265017,8.391951,-8.027920,8.777003,-3.524286,3.409316,-2.642242,6.279683,-4.247305,-2.025890,-4.934240,7.857751,7.924995,-1.011859,-1.182049,6.252877,-2.164090,7.333690,7.937798,1.450064,1.517590,-7.269554,5.517134,9.526382,3.395684,6.273902,-3.674780,-4.900127,9.071029,-2.650499,-4.183049,6.651172,-3.855936,-2.445389,5.727630,2.748050,-7.334656,-8.586983,-3.711972,3.479566,3.529903,9.102485,8.682936,1.794061,-0.534180,7.810467,1.976985,8.416369,9.224145,-8.513356,-2.454071,1.984221,0.912732,-4.707320,-7.408092,1.308106,-8.860959,2.622853,-7.961555,-0.598094,1.522081,-7.659322,-8.820495,-1.805492,8.288953,-8.165346,5.532302,-7.630599,-4.593952,-8.236076,0.233357,-2.208491,-5.391955,0.372895,4.426783,9.353269,4.672992,5.055155,2.992900,-3.502988,-6.602272,-6.869482,-9.070671,0.528914,9.340720,9.796520,5.465059,-9.626856,-0.609713,2.533166,-9.870337,-2.537923,-1.253672,7.281825,1.226260,-7.037370,9.089395,5.877172,2.310681,-5.922346,-7.222788,7.388187,7.935900,3.828326,-0.922176,7.448345,2.562631,-3.232862,-1.721331,-0.942502,6.601254,2.054649,3.711082,4.552890,5.742448,-8.436820,1.758319,-2.857076,0.424032,-9.257313,-1.717947,-1.671408,9.655103,8.136396,6.929644,-1.940255,-0.556491,1.887169,-6.168529,-1.402342,-3.591521,-5.182805,3.760100,-0.877593,-0.888775,-0.944642,3.159431,1.946701,1.452803,-7.063483,-0.452920,-6.760648,-3.854055,-1.528415,-7.065035,7.114504,5.920239,-7.796220,-6.952916,-9.233166,-3.975504,8.886020,4.992573,-7.968914,0.531014,4.894696,6.874587,-2.356109,5.056408,1.263134,1.680975,-7.606625,-4.703223,4.851741,-6.758354,2.519210,-1.189166,-1.454108,1.455223,6.284373,2.415840,-5.942590,-1.612578,-4.167136,-7.119543,4.736143,-5.267391,-5.430616,-3.329058,0.582727,7.057085,8.069193,3.483114,-8.175343,5.619850,2.146201,-3.617321,5.078069,-3.135875,2.691368,6.800338,5.560244,-2.088242,-0.556504,8.786721,7.403693,7.280367,0.858629,-6.919575,1.825674,8.456036,-5.984833,0.483242,-2.054054,-5.597840,-5.658713,-6.277605,5.251311,7.895231,1.209289,-7.173970,-7.999596,-1.179337,-6.782049,3.636998,-4.222466,2.731709,-0.541433,-3.170918,-5.058509,-9.128947,7.111681,-5.562160,-1.962915,-7.062011,8.873512,-0.245607,-6.184697,1.850649,-5.717807,1.566186,3.543174,7.664096,7.351354,-4.229990,-1.573914,-8.441386,7.602996,2.064167,-5.887796,7.194509,-9.354261,5.085979,-6.491730,1.599225,4.324082,6.509578,5.341531,7.168560,5.399934,2.567841,-8.307977,8.500357,-0.095605,4.758116,-7.624825,-2.316849,6.357898,-4.685469,-5.314912,-7.422447,-8.332026,-1.539245,-6.596313,-1.243857,9.922109,-3.565264,8.289735,0.924055,-5.415476,-1.281500,-7.357845,0.090494,6.472757,9.529959,2.913728,2.702372,-1.239943,-5.519521,6.511535,-5.571342,-6.392319,2.672069,-6.953698,4.964619,0.752808,0.066140,9.969165,3.668072,-1.372159,-6.097164,-2.179958,7.735891,-1.968957,-1.774625,-5.244890,-5.926204,8.897925,-8.732990,1.575264,-1.821966,-8.882427,-1.229383,-0.668022,-1.876514,-1.857989,-0.549095,-9.203169,4.629555,0.972156,5.315033,-5.863426,-7.769331,0.397308,7.860867,2.239931,7.823133,-1.472529,3.890166,-0.901501,2.089534,-8.532820,4.124453,-7.253411,8.528294,-7.174255,2.498776,8.909824,-2.209094,3.630706,6.994439,9.389295,-1.967805,-9.158486,-2.635321,4.407033,9.478096,-9.461330,-0.390269,-0.406691,-8.634093,-3.842317,8.006008,-6.779939,-1.217889,-2.334952,-0.121645,0.814578,6.771243,-8.215428,-4.885415,9.724995,7.100750,-3.484943,-1.812748,-6.426779,-1.477450,2.989200,-8.914601,0.040154,1.383865,-6.265879,-2.875002,-8.741172,9.932057,9.577893,-0.304592,2.984968,-9.789466,0.733264,-2.015235,-9.816112,4.168461,2.804526,3.719781,-2.572510,-3.970296,-4.543575,-9.043155,-2.273380,3.142248,7.607831,-4.001576,3.071731,3.720639,-4.267115,-5.969626,-2.948443,-6.087459,9.125222,-5.380714,-4.266060,-4.446218,1.412968,3.190886,-6.444542,-0.636162,-2.423883,2.018628,9.701140,-2.443236,-2.779223,-7.521639,-7.081173,-8.872759,-9.725338,-8.090018,3.935478,4.286861,9.932582,-8.697752,4.786471,-1.558804,-0.712832,-8.325830,-4.527426,8.084243,0.576413,7.677471,-0.111100,-7.632301,-5.239363,2.505579,9.702189,4.562301,8.382789,5.375608,-5.696282,-5.268900,2.648443,-8.928095,1.754680,-7.210539,-5.347125,8.622545,-1.960762,3.073017,-4.820172,-1.413612,-3.317175,-5.862357,-1.161738,-0.068445,4.401896,5.639015,3.836248,-4.766993,9.614814,-2.089509,-2.334279,-7.286133,3.255351,-3.858627,-3.923662,0.902520,-6.084014,-5.283342,8.270186,9.954620,7.497819,5.220046,-2.546797,6.925140,2.187954,8.265686,4.953723,-8.916847,-2.896864,-8.047115,3.877974,5.425952,-3.377524,-8.479957,-2.731610,-9.327284,-3.996048,1.584920,-1.078004,-3.654903,-8.640359,3.269807,9.222880,-9.561529,-7.595914,-2.083659,-0.736360,3.273659,1.784833,6.209004,9.456816,6.200047,7.153160,7.940229,-7.846781,3.951370,1.570798,-5.148660,-2.135173,-7.567211,-5.292875,2.709370,-2.891023,5.664652,-5.371599,-5.943617,-5.638192,-5.083522,-3.607714,4.888476,0.533031,6.614988,-5.328959,-1.839597,-6.597275,8.538786,3.098368,3.786068,-8.942458,-0.239571,3.167606,-4.060335,-1.221073,-1.621272,-2.699236,1.924161,-5.648403,2.833294,1.575406,-2.196316,-2.659814,-3.780718,-3.367497,-2.528595,-2.513473,5.378749,8.231545,7.458168,-6.427722,-6.887679,-8.778639,8.112450,-3.602561,5.872828,-9.666684,7.429190,8.121590,-9.899040,7.391186,-8.745438,7.249434,-7.766496,-1.994272,5.848939,8.386801,8.926232,3.389242,-6.734674,0.511313,5.710213,7.231724,3.810093,-9.451952,-0.726013,-0.386140,0.033015,4.384017,-4.146288,-9.536451,-1.280786,6.524437,8.727544,-3.362115,-6.635041,8.058494,0.034971,-5.041325,5.874105,2.112328,-8.336245,6.934650,9.254146,7.937179,-6.253598,1.632166,8.273200,-8.678534,-3.314817,3.326218,8.754434,-7.820747,0.038058,0.943962,-0.089083,0.114479,-0.341594,-0.650940,5.476180,3.907140,2.195872,-0.968852,3.454231,5.796710,-3.922182,-2.175944,0.523332,-0.017629,6.346981,-9.896462,-3.879588,-1.523595,-2.682176,6.491547,5.768364,1.072390,7.104031,0.210119,-4.386117,-4.874441,7.962600,-9.154927,-4.262097,-7.622679,-4.198920,7.428868,-4.063495,4.699215,-9.796772,-9.228634,8.851445,1.303772,7.424711,5.450296,4.153721,-2.521180,-4.853592,-5.205432,-4.845652,-4.843341,6.101996,9.698288,-8.945401,-1.024709,0.940641,-4.719966,-8.943354,-0.395911,-2.194174,3.360126,9.035280,1.744066,2.816505,-3.522859,-5.107687,-5.056628,-6.597655,4.959542,1.732838,-3.293959,-9.415615,5.707276,-3.408241,-8.851642,-3.150004,-8.028176,-7.322659,6.744890,5.791514,0.480840,1.108064,6.581178,7.183351,-6.245687,-4.154263,-4.208368,0.089625,9.768958,8.538084,-8.399908,-5.904552,5.607970,-3.865656,-4.911060,2.121145,8.715443,1.559100,-8.815833,8.722529,3.744894,3.325653,-0.584187,-9.879094,-5.045496,-1.126327,9.092462,-6.358590,8.806263,5.219730,-2.862297,9.144169,1.580180,6.379923,6.120621,-8.275327,-7.025631,-7.222712,-7.885634,7.099729,-4.068191,-1.523242,-6.363248,5.159227,7.035156,0.714241,8.651478,-1.390058,7.589362,-5.920220,-3.663891,-6.180794,7.507608,-0.217095,7.871731,-5.899264,9.715778,7.134981,0.133683,5.210071,0.020429,4.380990,2.931386,-1.474371,7.510466,3.743043,6.750737,-6.909940,6.091342,8.957142,-3.573555,-6.599013,-6.300428,5.780291,-5.096613,-4.355885,9.989162,-9.625649,4.429703,-9.474528,-4.012701,1.918136,9.266718,-5.696397,-0.408999,7.459488,8.716201,-9.992618,6.942572,-2.736932,-4.792483,1.235501,-5.943949,-9.531485,-0.581579,-0.806208,-5.903868,8.042237,4.863471,-5.510087,3.444134,5.746228,-2.567601,-3.180283,2.814309,2.328090,5.300973,-3.120416,9.837301,-9.874839,2.336450,-1.452921,-3.957607,5.791726,6.508333,4.688125,4.488685,8.490742,-2.621486,5.383464,-5.428070,3.617581,9.315595,6.933018,-7.295030,0.413209,-2.892117,2.825532,0.350250,1.618803,2.749124,5.271612,4.325035,-5.065784,-8.651030,9.842369,-4.539451,-8.901952,-6.804427,-9.625624,0.570098,-3.322425,8.737018,-6.679258,-2.246368,1.487778,-1.834773,-9.140238,-9.300806,6.799811,-6.384167,4.604335,5.344071,3.427294,-7.924544,-5.167911,3.941477,1.009959,9.772598,9.967579,3.302378,2.692438,1.531291,6.059512,-1.950642,-0.825028,-0.738775,5.762936,9.620774,8.078271,3.838119,-0.676265,3.462954,5.188409,5.646333,-6.793751,-7.821446,2.585871,-6.323618,9.447593,9.011691,8.791367,4.118373,-4.330125,0.584321,-1.966467,5.427676,4.619184,4.400936,2.872012,8.511318,9.223380,2.012637,3.969946,-7.113135,-7.467981,-3.982013,6.132816,9.919529,8.272380,7.369439,6.092338,-4.476650,6.025229,2.871140,-3.446896,7.608869,-0.105109,-0.395081,-3.825786,-8.836399,7.707570,-3.286765,5.761177,-8.663896,3.954973,-8.054414,-2.704999,7.822967,-0.343603,6.094312,-3.100981,3.254444,7.806209,-7.574684,-9.669859,7.983587,-5.433909,-4.584662,9.029689,-7.742906,-5.030700,7.069169,1.999399,6.448150,2.485069,-8.217778,4.157647,7.697317,-2.241330,-5.211033,-6.561056,-1.246123,4.102584,-2.257094,6.688220,4.288060,-5.235262,-3.733787,-5.275435,0.538507,-7.502060,4.574277,2.567346,0.730088,-6.077255,-8.314208,6.929758,3.031772,7.349540,2.116349,-6.291866,3.537504,6.288785,-9.390571,9.582600,1.676928,-7.446705,7.788540,1.396197,9.552474,-0.362295,4.397539,-2.621380,-5.347309,-1.901262,-0.117962,2.936001,2.115891,9.159713,-8.731435,-3.819773,6.054328,-0.704934,-5.799966,5.476402,3.502662,-2.093008,4.536119], dtype = "float64")#candidate|7221|(2640,)|const|float64
call_7219 = relay.TupleGetItem(func_2075_call(relay.reshape(const_7220.astype('float32'), [7, 7, 2]), relay.reshape(call_7217.astype('float32'), [33,]), relay.reshape(const_7221.astype('float64'), [12, 220]), ), 0)
call_7222 = relay.TupleGetItem(func_2080_call(relay.reshape(const_7220.astype('float32'), [7, 7, 2]), relay.reshape(call_7217.astype('float32'), [33,]), relay.reshape(const_7221.astype('float64'), [12, 220]), ), 0)
var_7225 = relay.var("var_7225", dtype = "float32", shape = (7, 7, 2))#candidate|7225|(7, 7, 2)|var|float32
bop_7226 = relay.less(call_7219.astype('bool'), relay.reshape(var_7225.astype('bool'), relay.shape_of(call_7219))) # shape=(7, 7, 2)
bop_7229 = relay.less(call_7222.astype('bool'), relay.reshape(var_7225.astype('bool'), relay.shape_of(call_7222))) # shape=(7, 7, 2)
bop_7263 = relay.bitwise_xor(const_7220.astype('uint8'), relay.reshape(bop_7226.astype('uint8'), relay.shape_of(const_7220))) # shape=(1, 98)
bop_7266 = relay.bitwise_xor(const_7220.astype('uint8'), relay.reshape(bop_7229.astype('uint8'), relay.shape_of(const_7220))) # shape=(1, 98)
bop_7292 = relay.logical_and(const_7220.astype('bool'), relay.reshape(bop_7226.astype('bool'), relay.shape_of(const_7220))) # shape=(1, 98)
bop_7295 = relay.logical_and(const_7220.astype('bool'), relay.reshape(bop_7229.astype('bool'), relay.shape_of(const_7220))) # shape=(1, 98)
output = relay.Tuple([call_7217,const_7221,bop_7263,bop_7292,])
output2 = relay.Tuple([call_7218,const_7221,bop_7266,bop_7295,])
func_7303 = relay.Function([var_7225,], output)
mod['func_7303'] = func_7303
mod = relay.transform.InferType()(mod)
var_7304 = relay.var("var_7304", dtype = "float32", shape = (7, 7, 2))#candidate|7304|(7, 7, 2)|var|float32
output = func_7303(var_7304)
func_7305 = relay.Function([var_7304], output)
mutated_mod['func_7305'] = func_7305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mod.get_global_var('func_6802')
func_6803_call = mutated_mod.get_global_var('func_6803')
call_7371 = func_6802_call()
call_7372 = func_6802_call()
func_6823_call = mod.get_global_var('func_6823')
func_6825_call = mutated_mod.get_global_var('func_6825')
call_7375 = func_6823_call()
call_7376 = func_6823_call()
func_1359_call = mod.get_global_var('func_1359')
func_1360_call = mutated_mod.get_global_var('func_1360')
call_7379 = func_1359_call()
call_7380 = func_1359_call()
func_1999_call = mod.get_global_var('func_1999')
func_2000_call = mutated_mod.get_global_var('func_2000')
call_7382 = relay.TupleGetItem(func_1999_call(), 0)
call_7383 = relay.TupleGetItem(func_2000_call(), 0)
output = relay.Tuple([call_7371,call_7375,call_7379,call_7382,])
output2 = relay.Tuple([call_7372,call_7376,call_7380,call_7383,])
func_7389 = relay.Function([], output)
mod['func_7389'] = func_7389
mod = relay.transform.InferType()(mod)
output = func_7389()
func_7390 = relay.Function([], output)
mutated_mod['func_7390'] = func_7390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_7405 = relay.TupleGetItem(func_4398_call(), 0)
call_7406 = relay.TupleGetItem(func_4399_call(), 0)
func_2014_call = mod.get_global_var('func_2014')
func_2018_call = mutated_mod.get_global_var('func_2018')
var_7411 = relay.var("var_7411", dtype = "uint64", shape = (160,))#candidate|7411|(160,)|var|uint64
call_7410 = func_2014_call(relay.reshape(var_7411.astype('uint64'), [8, 10, 2]), relay.reshape(var_7411.astype('uint64'), [8, 10, 2]), )
call_7412 = func_2014_call(relay.reshape(var_7411.astype('uint64'), [8, 10, 2]), relay.reshape(var_7411.astype('uint64'), [8, 10, 2]), )
func_2490_call = mod.get_global_var('func_2490')
func_2492_call = mutated_mod.get_global_var('func_2492')
const_7449 = relay.const([[-9.263378,-8.937207,-2.403688,4.455097,-7.670256,2.851138,-6.141993,-1.525308,3.213447,-1.868582,4.811642,-6.602654,7.759182,5.277248,2.714196,8.332690,7.755095,-6.608835,1.848999,9.006916,-4.325667,7.223149,3.665821,-1.221154,-5.655970,9.212245,5.463837,-5.170622,8.121631,-7.983636,2.205105,-3.462476,7.937374,-5.346898,5.944408,-5.168204,-7.131888,-0.509017,-8.218780,-1.630674,0.240029,-3.872600,-4.385570,9.394536],[-5.966493,-5.630864,-7.310541,3.904471,-6.110931,-2.634416,1.409589,6.803411,-7.017773,5.382113,3.806142,-9.581478,0.143564,5.036235,0.019236,4.059753,-9.518110,1.552680,2.277130,9.655595,-9.664726,9.793415,-0.512983,7.845017,-9.141761,7.954205,3.591919,-2.072038,-6.793441,-2.936059,-0.078470,-4.281588,0.324932,5.399333,-2.128116,-1.728478,-0.449590,-9.533374,5.000078,-3.687872,-0.005120,3.687038,4.847318,-5.525326],[6.395167,5.542783,-3.250010,-5.136581,9.687191,-6.675042,-9.267557,-6.749142,-5.520294,-2.383327,-7.535706,2.313973,-8.410475,-8.794459,-1.440926,-6.742913,1.174433,-6.551517,8.947240,-2.148267,-7.728374,-8.787615,4.442531,-0.538913,0.214703,5.581154,3.215259,-1.617786,9.512305,3.342383,4.272288,4.765021,5.283759,-9.204429,8.736482,2.411965,-0.240008,-8.436023,-1.429098,1.003722,1.321445,6.874061,-4.855559,3.903682],[5.616132,2.695277,-9.620990,2.414417,-5.000808,-5.614851,-8.970657,-6.862401,5.087229,3.173166,1.505350,3.956663,2.064850,7.271198,-0.905008,-8.677372,4.008359,-0.565065,-2.664378,0.342804,6.850077,-1.312263,6.546424,-3.627050,-6.489532,-1.435319,3.657101,-2.925479,-9.604002,-8.627601,-9.216462,-4.416807,-2.637080,0.880832,6.546809,-1.172513,-3.017158,-2.815352,9.131408,-2.052924,-3.322867,2.367950,-0.475422,0.509118],[2.524579,9.611157,-7.575923,1.309608,-6.099986,4.724467,5.450530,8.444932,3.400565,8.419499,-9.097171,-7.181800,-7.937609,-5.382694,5.522146,4.636291,8.662097,7.402504,6.632328,8.620056,2.383065,7.088886,-6.768879,5.612260,-6.626139,-8.882928,-6.144451,-3.862690,-5.604063,-6.531802,-2.678208,-1.159568,-4.475701,6.628288,-3.791309,-0.467254,3.721227,-0.969898,-5.136465,2.376968,-2.399532,2.944223,-3.441319,2.141178],[6.309078,9.865843,4.004558,1.063972,9.868198,9.209061,4.343834,3.496385,1.065108,-8.637996,8.498103,9.851209,9.693837,3.350562,-3.343617,-4.201812,-4.491120,0.510666,4.106398,9.700914,9.724448,-0.689793,-2.939109,7.474764,6.203805,2.404371,-8.070026,-5.614600,-1.653966,8.252896,-6.125981,-6.707875,9.399620,9.229641,-6.679395,1.719026,2.462197,2.310440,-8.611798,-5.353666,-5.411432,-2.271633,-4.071392,8.173066],[-8.240397,9.529001,-9.350419,6.154971,6.186549,5.182897,-1.269567,0.908309,-6.602532,0.596902,9.651586,2.808192,-2.269626,-2.346373,-4.218809,6.317437,0.532150,-3.796397,-0.807651,2.691577,-5.954157,7.200562,-9.663406,-0.764865,1.943750,2.092618,3.575479,9.809485,-2.773940,-4.827375,2.349970,-7.219067,-0.362282,-6.753898,-9.365221,-7.812455,-7.351826,5.017260,-6.784992,-4.676317,-3.229903,5.314945,-2.593055,6.070248],[-4.531958,7.979058,6.116486,-9.992038,-6.931811,-8.959162,4.842482,2.538197,-9.208557,-0.129026,0.942365,6.329929,-2.626700,3.613302,2.238634,1.919076,5.711558,7.841424,-0.310088,-9.072104,-0.389162,-3.208432,-6.238786,-7.168259,-9.500821,2.838693,2.074993,7.879205,7.192288,-2.527401,3.333320,8.825709,-6.626933,9.328399,-2.552938,-4.064210,-4.704579,-7.266374,-5.411374,-8.144729,6.100535,-7.179954,-4.963358,-4.626778]], dtype = "float64")#candidate|7449|(8, 44)|const|float64
call_7448 = func_2490_call(relay.reshape(const_7449.astype('float64'), [11, 8, 4]))
call_7450 = func_2490_call(relay.reshape(const_7449.astype('float64'), [11, 8, 4]))
func_4106_call = mod.get_global_var('func_4106')
func_4107_call = mutated_mod.get_global_var('func_4107')
call_7475 = relay.TupleGetItem(func_4106_call(), 1)
call_7476 = relay.TupleGetItem(func_4107_call(), 1)
output = relay.Tuple([call_7405,call_7410,var_7411,call_7448,const_7449,call_7475,])
output2 = relay.Tuple([call_7406,call_7412,var_7411,call_7450,const_7449,call_7476,])
func_7482 = relay.Function([var_7411,], output)
mod['func_7482'] = func_7482
mod = relay.transform.InferType()(mod)
var_7483 = relay.var("var_7483", dtype = "uint64", shape = (160,))#candidate|7483|(160,)|var|uint64
output = func_7482(var_7483)
func_7484 = relay.Function([var_7483], output)
mutated_mod['func_7484'] = func_7484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5692_call = mod.get_global_var('func_5692')
func_5693_call = mutated_mod.get_global_var('func_5693')
call_7573 = func_5692_call()
call_7574 = func_5692_call()
output = call_7573
output2 = call_7574
func_7592 = relay.Function([], output)
mod['func_7592'] = func_7592
mod = relay.transform.InferType()(mod)
output = func_7592()
func_7593 = relay.Function([], output)
mutated_mod['func_7593'] = func_7593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6823_call = mod.get_global_var('func_6823')
func_6825_call = mutated_mod.get_global_var('func_6825')
call_7600 = func_6823_call()
call_7601 = func_6823_call()
func_4474_call = mod.get_global_var('func_4474')
func_4476_call = mutated_mod.get_global_var('func_4476')
call_7604 = relay.TupleGetItem(func_4474_call(), 0)
call_7605 = relay.TupleGetItem(func_4476_call(), 0)
output = relay.Tuple([call_7600,call_7604,])
output2 = relay.Tuple([call_7601,call_7605,])
func_7616 = relay.Function([], output)
mod['func_7616'] = func_7616
mod = relay.transform.InferType()(mod)
mutated_mod['func_7616'] = func_7616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7616_call = mutated_mod.get_global_var('func_7616')
call_7617 = func_7616_call()
output = call_7617
func_7618 = relay.Function([], output)
mutated_mod['func_7618'] = func_7618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4627_call = mod.get_global_var('func_4627')
func_4628_call = mutated_mod.get_global_var('func_4628')
call_7661 = func_4627_call()
call_7662 = func_4627_call()
output = relay.Tuple([call_7661,])
output2 = relay.Tuple([call_7662,])
func_7666 = relay.Function([], output)
mod['func_7666'] = func_7666
mod = relay.transform.InferType()(mod)
mutated_mod['func_7666'] = func_7666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7666_call = mutated_mod.get_global_var('func_7666')
call_7667 = func_7666_call()
output = call_7667
func_7668 = relay.Function([], output)
mutated_mod['func_7668'] = func_7668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6785_call = mod.get_global_var('func_6785')
func_6787_call = mutated_mod.get_global_var('func_6787')
call_7711 = relay.TupleGetItem(func_6785_call(), 0)
call_7712 = relay.TupleGetItem(func_6787_call(), 0)
output = call_7711
output2 = call_7712
func_7749 = relay.Function([], output)
mod['func_7749'] = func_7749
mod = relay.transform.InferType()(mod)
output = func_7749()
func_7750 = relay.Function([], output)
mutated_mod['func_7750'] = func_7750
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7836 = relay.var("var_7836", dtype = "float64", shape = (10, 3, 15))#candidate|7836|(10, 3, 15)|var|float64
uop_7837 = relay.erf(var_7836.astype('float64')) # shape=(10, 3, 15)
uop_7865 = relay.tan(var_7836.astype('float64')) # shape=(10, 3, 15)
output = relay.Tuple([uop_7837,uop_7865,])
output2 = relay.Tuple([uop_7837,uop_7865,])
func_7879 = relay.Function([var_7836,], output)
mod['func_7879'] = func_7879
mod = relay.transform.InferType()(mod)
var_7880 = relay.var("var_7880", dtype = "float64", shape = (10, 3, 15))#candidate|7880|(10, 3, 15)|var|float64
output = func_7879(var_7880)
func_7881 = relay.Function([var_7880], output)
mutated_mod['func_7881'] = func_7881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6887_call = mod.get_global_var('func_6887')
func_6888_call = mutated_mod.get_global_var('func_6888')
call_7917 = relay.TupleGetItem(func_6887_call(), 0)
call_7918 = relay.TupleGetItem(func_6888_call(), 0)
output = relay.Tuple([call_7917,])
output2 = relay.Tuple([call_7918,])
func_7919 = relay.Function([], output)
mod['func_7919'] = func_7919
mod = relay.transform.InferType()(mod)
mutated_mod['func_7919'] = func_7919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7919_call = mutated_mod.get_global_var('func_7919')
call_7920 = func_7919_call()
output = call_7920
func_7921 = relay.Function([], output)
mutated_mod['func_7921'] = func_7921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6321_call = mod.get_global_var('func_6321')
func_6322_call = mutated_mod.get_global_var('func_6322')
call_7958 = relay.TupleGetItem(func_6321_call(), 0)
call_7959 = relay.TupleGetItem(func_6322_call(), 0)
func_5863_call = mod.get_global_var('func_5863')
func_5865_call = mutated_mod.get_global_var('func_5865')
call_7966 = func_5863_call()
call_7967 = func_5863_call()
output = relay.Tuple([call_7958,call_7966,])
output2 = relay.Tuple([call_7959,call_7967,])
func_7980 = relay.Function([], output)
mod['func_7980'] = func_7980
mod = relay.transform.InferType()(mod)
mutated_mod['func_7980'] = func_7980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7980_call = mutated_mod.get_global_var('func_7980')
call_7981 = func_7980_call()
output = call_7981
func_7982 = relay.Function([], output)
mutated_mod['func_7982'] = func_7982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5363_call = mod.get_global_var('func_5363')
func_5365_call = mutated_mod.get_global_var('func_5365')
call_8057 = relay.TupleGetItem(func_5363_call(), 0)
call_8058 = relay.TupleGetItem(func_5365_call(), 0)
func_3583_call = mod.get_global_var('func_3583')
func_3584_call = mutated_mod.get_global_var('func_3584')
call_8066 = func_3583_call()
call_8067 = func_3583_call()
func_1816_call = mod.get_global_var('func_1816')
func_1818_call = mutated_mod.get_global_var('func_1818')
var_8077 = relay.var("var_8077", dtype = "float64", shape = (33,))#candidate|8077|(33,)|var|float64
call_8076 = relay.TupleGetItem(func_1816_call(relay.reshape(var_8077.astype('float64'), [33,])), 0)
call_8078 = relay.TupleGetItem(func_1818_call(relay.reshape(var_8077.astype('float64'), [33,])), 0)
output = relay.Tuple([call_8057,call_8066,call_8076,var_8077,])
output2 = relay.Tuple([call_8058,call_8067,call_8078,var_8077,])
func_8084 = relay.Function([var_8077,], output)
mod['func_8084'] = func_8084
mod = relay.transform.InferType()(mod)
var_8085 = relay.var("var_8085", dtype = "float64", shape = (33,))#candidate|8085|(33,)|var|float64
output = func_8084(var_8085)
func_8086 = relay.Function([var_8085], output)
mutated_mod['func_8086'] = func_8086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3111_call = mod.get_global_var('func_3111')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_8118 = relay.TupleGetItem(func_3111_call(), 0)
call_8119 = relay.TupleGetItem(func_3112_call(), 0)
output = relay.Tuple([call_8118,])
output2 = relay.Tuple([call_8119,])
func_8127 = relay.Function([], output)
mod['func_8127'] = func_8127
mod = relay.transform.InferType()(mod)
output = func_8127()
func_8128 = relay.Function([], output)
mutated_mod['func_8128'] = func_8128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3583_call = mod.get_global_var('func_3583')
func_3584_call = mutated_mod.get_global_var('func_3584')
call_8172 = func_3583_call()
call_8173 = func_3583_call()
output = relay.Tuple([call_8172,])
output2 = relay.Tuple([call_8173,])
func_8178 = relay.Function([], output)
mod['func_8178'] = func_8178
mod = relay.transform.InferType()(mod)
output = func_8178()
func_8179 = relay.Function([], output)
mutated_mod['func_8179'] = func_8179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6321_call = mod.get_global_var('func_6321')
func_6322_call = mutated_mod.get_global_var('func_6322')
call_8187 = relay.TupleGetItem(func_6321_call(), 1)
call_8188 = relay.TupleGetItem(func_6322_call(), 1)
func_6538_call = mod.get_global_var('func_6538')
func_6541_call = mutated_mod.get_global_var('func_6541')
const_8192 = relay.const([4.013461,-7.566142,-9.573090,1.692547,-2.653703,-8.763761,8.605385,-4.620486,7.541182,-2.600745,-9.670191,2.254785,5.399792,-6.055342,-1.766728,-5.332229,-6.689924,4.901824,4.881180,-2.317908,9.636792,-5.101145,-1.790947,2.975495,7.830511,-9.713879,-9.709688,-8.439923,1.639303,-4.329749,-4.973808,0.043946,-4.061032,-1.291072,9.538678,3.825806,8.096921,-2.304034,5.718235,3.318580,6.512977,-0.747597,3.784770,6.826195,0.222099,-0.149507,-2.032594,7.052333,-6.552726,-0.930907,-2.786086,-4.273878,6.397577,-5.905933,8.720582,4.019192,8.318906,-8.161693,-8.818658,1.709982,-2.226562,-0.191732,-8.380070,5.945158,5.868249,-0.202297,6.653861,1.789607,6.507971,0.369117,6.571111,-7.843450,5.472174,-4.074972,-2.471400,7.288375,1.048551,-4.980077,6.420238,0.066589,7.175063,4.776326,-8.155272,-5.774710,-2.690075,-0.916834,-7.544619,-6.342180,-9.013016,-5.159463,-1.803205,8.116424,0.401602,8.532298,4.107867,6.837556,9.031148,8.694629,4.588797,0.808927,-4.945736,1.534304,-5.682505,-9.541191,-6.076067,-9.390758,-3.242099,6.636846,7.934680,2.896566,4.868800,7.409304,4.616495,-5.929472,-6.707117,-0.945677,-0.874129,-5.659788,8.956479,5.707730,5.620327,-3.600153,3.108174,9.593222,5.028880,4.144406,3.691749,5.953686,1.697017,1.062217,1.063049,-6.032304,1.812583,6.529359,8.958160,3.562587,-7.053371,4.597023,1.387262,-5.730524,1.718121,9.091141,-3.881034,0.274336,-3.337451,-0.754473,-1.858172,4.759230,1.866028,-8.081986,5.028923,2.711637,9.192218,1.783603,3.039871,1.496480,2.024308,3.756069,6.449484,-4.090801,9.744500,-0.705666,7.327345,8.274999,-7.343927,-9.001642,0.433304,3.111862,-2.734577,0.962606,-8.627795,-5.846788,8.578558,6.357720,-7.123572,1.137305,-3.541769,6.545393,7.336599,-9.772832,-7.309090,-5.550365,-6.491333,-0.726332,-6.912252,-4.581118,3.974010,6.806567,-0.544819,7.486040,-1.377102,-6.304600,-0.235644,-4.573636,2.441961,5.424417,1.214030,3.498004,8.782407,-4.479117,-5.839323,-2.669882,5.164076,-9.868881,5.624775,-1.979474,-7.584452,-3.725591,-3.680264,4.571196], dtype = "float32")#candidate|8192|(210,)|const|float32
call_8191 = relay.TupleGetItem(func_6538_call(relay.reshape(const_8192.astype('float32'), [3, 14, 5])), 1)
call_8193 = relay.TupleGetItem(func_6541_call(relay.reshape(const_8192.astype('float32'), [3, 14, 5])), 1)
bop_8201 = relay.not_equal(call_8191.astype('bool'), relay.reshape(const_8192.astype('bool'), relay.shape_of(call_8191))) # shape=(3, 14, 5)
bop_8204 = relay.not_equal(call_8193.astype('bool'), relay.reshape(const_8192.astype('bool'), relay.shape_of(call_8193))) # shape=(3, 14, 5)
output = relay.Tuple([call_8187,bop_8201,])
output2 = relay.Tuple([call_8188,bop_8204,])
func_8217 = relay.Function([], output)
mod['func_8217'] = func_8217
mod = relay.transform.InferType()(mod)
output = func_8217()
func_8218 = relay.Function([], output)
mutated_mod['func_8218'] = func_8218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2768_call = mod.get_global_var('func_2768')
func_2769_call = mutated_mod.get_global_var('func_2769')
call_8222 = relay.TupleGetItem(func_2768_call(), 5)
call_8223 = relay.TupleGetItem(func_2769_call(), 5)
output = call_8222
output2 = call_8223
func_8224 = relay.Function([], output)
mod['func_8224'] = func_8224
mod = relay.transform.InferType()(mod)
output = func_8224()
func_8225 = relay.Function([], output)
mutated_mod['func_8225'] = func_8225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8224_call = mod.get_global_var('func_8224')
func_8225_call = mutated_mod.get_global_var('func_8225')
call_8235 = func_8224_call()
call_8236 = func_8224_call()
uop_8237 = relay.tan(call_8235.astype('float64')) # shape=(2640,)
uop_8239 = relay.tan(call_8236.astype('float64')) # shape=(2640,)
output = uop_8237
output2 = uop_8239
func_8244 = relay.Function([], output)
mod['func_8244'] = func_8244
mod = relay.transform.InferType()(mod)
mutated_mod['func_8244'] = func_8244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8244_call = mutated_mod.get_global_var('func_8244')
call_8245 = func_8244_call()
output = call_8245
func_8246 = relay.Function([], output)
mutated_mod['func_8246'] = func_8246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8257 = relay.var("var_8257", dtype = "float64", shape = (15, 6, 3))#candidate|8257|(15, 6, 3)|var|float64
uop_8258 = relay.cosh(var_8257.astype('float64')) # shape=(15, 6, 3)
func_774_call = mod.get_global_var('func_774')
func_778_call = mutated_mod.get_global_var('func_778')
var_8267 = relay.var("var_8267", dtype = "uint8", shape = (1, 325))#candidate|8267|(1, 325)|var|uint8
call_8266 = relay.TupleGetItem(func_774_call(relay.reshape(var_8267.astype('uint8'), [5, 13, 5]), relay.reshape(var_8267.astype('uint8'), [5, 13, 5]), ), 0)
call_8268 = relay.TupleGetItem(func_778_call(relay.reshape(var_8267.astype('uint8'), [5, 13, 5]), relay.reshape(var_8267.astype('uint8'), [5, 13, 5]), ), 0)
uop_8269 = relay.exp(uop_8258.astype('float32')) # shape=(15, 6, 3)
func_1132_call = mod.get_global_var('func_1132')
func_1134_call = mutated_mod.get_global_var('func_1134')
call_8292 = relay.TupleGetItem(func_1132_call(), 0)
call_8293 = relay.TupleGetItem(func_1134_call(), 0)
func_8178_call = mod.get_global_var('func_8178')
func_8179_call = mutated_mod.get_global_var('func_8179')
call_8297 = relay.TupleGetItem(func_8178_call(), 0)
call_8298 = relay.TupleGetItem(func_8179_call(), 0)
bop_8300 = relay.not_equal(var_8267.astype('bool'), relay.reshape(call_8266.astype('bool'), relay.shape_of(var_8267))) # shape=(1, 325)
bop_8303 = relay.not_equal(var_8267.astype('bool'), relay.reshape(call_8268.astype('bool'), relay.shape_of(var_8267))) # shape=(1, 325)
func_7666_call = mod.get_global_var('func_7666')
func_7668_call = mutated_mod.get_global_var('func_7668')
call_8305 = relay.TupleGetItem(func_7666_call(), 0)
call_8306 = relay.TupleGetItem(func_7668_call(), 0)
func_4567_call = mod.get_global_var('func_4567')
func_4569_call = mutated_mod.get_global_var('func_4569')
call_8309 = relay.TupleGetItem(func_4567_call(), 1)
call_8310 = relay.TupleGetItem(func_4569_call(), 1)
output = relay.Tuple([uop_8269,call_8292,call_8297,bop_8300,call_8305,call_8309,])
output2 = relay.Tuple([uop_8269,call_8293,call_8298,bop_8303,call_8306,call_8310,])
func_8313 = relay.Function([var_8257,var_8267,], output)
mod['func_8313'] = func_8313
mod = relay.transform.InferType()(mod)
var_8314 = relay.var("var_8314", dtype = "float64", shape = (15, 6, 3))#candidate|8314|(15, 6, 3)|var|float64
var_8315 = relay.var("var_8315", dtype = "uint8", shape = (1, 325))#candidate|8315|(1, 325)|var|uint8
output = func_8313(var_8314,var_8315,)
func_8316 = relay.Function([var_8314,var_8315,], output)
mutated_mod['func_8316'] = func_8316
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8325 = relay.const([[[-2.912123,-6.504997,9.978144,0.086603,9.451939,5.603950,5.132320,-2.620835,9.297533],[0.115740,7.454468,-9.615076,-7.998414,5.078310,4.584407,2.174749,9.368317,-3.341095],[-7.896085,2.401406,8.251776,1.719177,7.731239,-3.468751,2.923007,1.676836,1.264518],[2.549703,-9.463982,8.805527,5.763497,0.795480,-9.332840,2.678776,3.612896,-7.009621],[-5.639787,-9.319449,-4.142345,-5.889578,-7.150867,-1.788796,1.409993,9.027648,3.314356],[4.741318,3.589946,1.048674,-1.388019,6.478118,7.004402,-6.213304,5.444431,3.723450],[6.004855,2.168275,3.219417,9.341976,0.133056,-2.481663,6.904935,-1.745054,-6.507594],[-3.856594,-4.996639,4.865659,-9.882483,9.134244,-8.196822,9.314201,-7.856167,3.888589],[-4.377893,6.172113,0.219143,-6.600383,1.595151,-2.517428,-2.758157,2.659244,-1.564684],[-8.049751,-3.014229,-9.743886,0.042295,2.739841,-8.399204,7.337590,6.593203,-0.791715],[3.481240,-6.354535,3.141648,-2.383620,8.390119,2.406813,-0.112496,-1.158017,6.512514],[4.296717,-5.870897,9.582687,7.458202,-7.854173,2.398658,-5.539502,2.306906,0.112248],[4.002394,2.215641,8.955356,-0.562068,-0.999461,2.910940,9.562506,-1.132450,7.698586],[-9.744245,9.691782,0.242537,4.932931,1.257866,-4.374066,-5.212058,-9.213750,1.736591],[-5.245661,-1.319378,-7.978636,-6.000409,-7.760352,-8.758510,-9.912642,5.402680,3.004753],[-2.824838,-8.841294,4.646048,0.607989,-7.446909,5.504231,4.007432,5.457099,2.648390]],[[0.978769,5.841035,-1.918715,1.292599,-7.697780,-0.654127,-5.549177,-9.525005,-4.054979],[3.910570,7.658291,-5.136919,4.348508,-0.749146,7.918838,2.212079,-6.361297,-4.457440],[-3.393729,9.585485,-0.784077,-0.478478,1.514481,4.265948,-0.767882,9.356910,-5.526148],[6.293365,0.457384,-9.817561,3.047811,-7.256687,-5.448658,-6.602778,-4.289173,4.205134],[-5.765350,1.295072,3.309092,1.260938,-8.669499,0.436069,-7.392555,-4.822279,0.126941],[-0.738316,-9.179990,-1.495363,-3.994560,4.541921,-5.290261,9.767107,-2.087237,-4.083711],[-2.343083,-7.894252,-9.716786,6.649146,-1.848075,1.729632,1.393054,-4.609327,-8.934085],[-5.002720,4.546784,7.361895,2.000341,-0.403493,-3.765167,9.080154,0.313928,1.006954],[0.864235,-9.802638,-4.119813,2.873900,-0.725870,-6.648714,-6.356123,5.413107,-4.132367],[-2.241291,3.337664,-9.194614,7.641102,-6.951590,5.135812,4.402070,4.308173,-1.029555],[0.965431,9.042601,1.494373,-3.641748,-6.942565,6.830849,-0.248952,-1.108625,1.030585],[5.251571,-0.608415,4.931163,2.096083,2.444064,-0.272241,7.502713,3.895779,3.732737],[-6.413428,7.577326,0.686073,6.987721,-2.973543,-3.228842,-7.807227,-2.107461,2.505716],[-2.979473,-0.022485,4.914242,7.039823,-0.228801,3.702390,1.423704,5.261673,7.400674],[-1.339296,0.347750,-6.846812,-4.932565,7.749749,-5.136161,-3.837073,-2.996196,-9.602035],[3.515801,-6.988056,-2.199996,-7.429573,9.643573,-7.894677,-5.543549,2.991262,4.896178]],[[3.644535,3.216604,4.975187,-8.425193,-4.972225,-4.489049,-6.399044,2.262568,-8.932245],[5.771861,2.370864,-5.663771,2.166619,-7.510178,-1.093187,-4.839293,1.766004,6.252317],[3.017421,-0.272643,-7.640914,-9.563704,5.296917,1.935501,-1.728257,-2.275892,4.646914],[4.448419,0.629614,7.656364,-0.566410,-2.300364,0.601747,-7.819559,5.995780,7.939976],[1.413695,-2.944983,0.292170,-7.010020,-6.119049,3.489110,-1.591751,-7.218820,7.705912],[4.661777,-4.000519,2.938063,3.862199,-3.703863,3.221673,-1.629469,-0.070388,5.649662],[-1.295622,0.483837,-2.165225,-5.706365,5.978459,-7.043081,0.359104,-0.879519,4.528979],[7.518948,8.325156,6.903115,5.535579,-0.507547,2.186680,9.214753,9.519270,-5.814018],[-9.190711,-5.273466,-1.752174,-0.756688,7.094472,4.548803,-6.935912,0.184893,-8.878322],[-4.271575,5.997616,3.090946,-1.605140,-0.728451,8.760420,3.849065,-0.911572,-3.193952],[1.341530,-8.095659,9.856519,4.269619,-5.517131,-9.333917,-9.855378,0.883522,8.653502],[-1.046164,8.134133,8.321864,7.807106,-0.174805,1.156877,-5.516805,0.899281,5.403331],[-2.275986,3.842240,3.000150,-3.790858,-8.377825,2.548612,-2.361169,-5.515552,7.897716],[5.218571,-2.195875,-5.132042,-6.876234,-4.848170,6.081573,-3.655280,7.707662,-3.892010],[6.196777,-7.950086,-7.141834,9.195703,3.600724,3.590052,-0.752806,4.612610,-6.743089],[-4.199387,8.771692,6.238965,-4.360326,-2.955810,0.597984,-7.253165,6.487277,-0.007062]],[[1.803859,8.762282,5.477253,4.311289,8.565793,9.773204,-0.522620,-8.660160,-6.159022],[-2.838691,2.029342,-6.924652,3.317112,-5.817804,1.363391,2.318558,-9.524446,5.420727],[9.678206,0.090667,-7.636940,-1.759858,-0.103846,-3.409552,-3.341029,8.773636,3.144191],[-5.731553,5.248485,-9.339405,-8.917768,2.909368,-1.374562,-9.664720,0.259202,-7.403658],[-3.668041,-5.604963,0.737628,-6.959934,3.516317,1.508311,0.362293,5.067269,-8.089248],[-2.408523,8.242166,-5.821978,-7.913433,0.063630,-6.400203,0.528292,5.485269,-6.532440],[-5.406027,-9.887517,-6.266574,0.505324,-9.403024,-0.953776,-4.601928,5.068636,-0.377048],[2.690138,-4.541091,-9.752013,-2.739996,-8.355957,6.380325,-9.844176,8.981172,2.662172],[-3.288809,1.536785,-3.621613,-3.519565,-9.541426,-9.996778,6.035622,-7.183355,1.935126],[-2.782963,-3.738461,6.024571,9.986251,-1.124471,-5.362570,1.386476,-6.634343,4.178487],[-6.914989,4.943745,4.916266,-4.326034,6.166030,2.581710,7.427343,-5.970160,-9.249879],[-7.133785,0.566790,-1.799099,-8.781384,-5.047774,-6.602892,3.167959,2.411341,-0.810919],[1.614159,9.191144,1.786078,2.008810,2.292849,-9.738266,8.316096,2.157007,4.778414],[-4.189411,6.908766,-1.567042,6.377325,7.700497,-4.449729,3.501511,-8.150563,-6.907309],[8.961081,-1.754153,0.630049,-6.447342,8.468526,9.615256,3.693723,9.026268,3.927111],[5.342624,1.412860,4.507576,-9.929437,2.788809,-2.987292,-5.799699,1.858825,-5.455890]],[[2.566795,6.595523,-2.050032,-1.416211,1.427992,3.325059,9.824470,7.544675,5.671691],[1.060975,7.681164,-7.803429,-4.174079,-8.954243,3.430867,9.997860,9.455356,-4.989281],[7.891329,-8.331930,-7.752630,3.280395,-7.430543,-5.828389,-8.882523,1.031609,3.012479],[6.809060,-6.269566,5.737602,-1.367439,-3.598310,-5.218754,7.714815,0.075965,-9.199291],[4.329235,-3.567159,-5.640591,7.848736,-7.096863,-0.787357,-4.640411,1.136628,6.366182],[0.982088,7.317473,-2.598002,-1.111155,-5.453924,0.093571,7.322069,-4.031599,-2.304192],[-7.873156,9.969242,-9.473554,-7.036455,5.292294,9.947156,9.895191,-4.712184,-6.825083],[-2.116701,3.274198,8.266570,1.245286,8.704493,-8.381742,-9.096832,-4.611977,6.935371],[2.859746,9.453081,3.937904,-6.157605,3.414829,-9.432897,9.563578,-1.572323,4.146369],[1.294681,-5.364668,-7.790516,-3.825934,-8.348176,1.428755,3.964310,4.967567,5.940118],[6.220234,6.903376,6.062539,-2.942023,-0.605877,6.628896,-8.252094,-3.946470,5.574975],[5.421964,9.378955,-1.978472,0.603874,-9.671920,1.846789,-4.259541,5.367350,7.951091],[1.747269,6.445390,5.022890,1.248908,5.110194,-0.327871,-8.467905,-3.714424,1.728788],[-9.123754,-0.919874,-9.082691,0.327255,-9.492381,-8.120952,6.696814,9.410665,-2.000160],[9.387212,2.446944,1.502838,6.726930,8.654707,-5.693251,8.332824,-7.986740,5.143345],[6.994171,3.356210,4.792316,5.996188,1.966044,9.326657,5.673299,3.674934,2.108638]],[[7.980620,-2.334228,-5.828332,5.736464,-2.529968,1.098198,-8.660963,-5.134299,-9.753024],[-8.817537,-7.466822,-8.685256,6.205075,-2.879030,-5.418389,0.580707,-6.726200,9.222867],[-0.172480,-7.325261,-3.020155,-2.264994,-9.154624,-7.952739,-8.354046,0.813806,-6.465350],[-2.293925,0.502170,-4.891117,-5.012883,0.047853,0.032631,6.490650,-8.107312,-3.393115],[2.599954,1.666902,8.302515,-4.129942,-4.409894,-5.679063,-0.453490,-7.019633,0.261341],[0.642484,4.761426,9.626360,2.501156,-0.885434,-1.505770,-1.375345,-6.139200,-7.959968],[1.827702,1.561596,-3.462812,-7.311242,0.426763,-9.300833,0.396409,-4.515489,2.298748],[-0.531589,3.062146,-5.405311,3.145015,9.141648,-9.126743,-1.200839,3.233546,-9.278343],[0.181385,-5.363627,4.123440,-2.426212,-1.384079,8.937761,-4.660208,1.815552,5.772516],[8.108813,-2.642654,-2.460348,-7.560458,6.415243,-0.407461,5.739613,-6.603053,-5.401713],[9.809395,1.003618,-6.858106,8.682746,-4.285934,-6.558433,-9.499961,-1.390985,-1.741498],[3.635126,9.287012,-6.473375,-2.282181,-1.408361,5.076631,3.492424,4.748047,8.770437],[0.976342,-5.303866,5.046564,5.201321,-1.610493,-1.962040,-5.797205,-9.395372,-3.697884],[-5.319214,-2.349555,-2.378873,3.527461,-0.068112,-4.831698,-2.236349,-8.992940,9.189688],[2.794592,8.727788,-1.945569,4.983014,-9.102325,6.008273,-2.506768,3.166748,-1.706726],[9.416258,5.221953,-5.777255,4.215528,-0.785865,8.124537,9.828659,-4.582539,-0.033359]],[[-2.639597,-1.893502,0.933445,-9.684424,7.965911,0.109740,6.396693,4.609621,-2.033022],[-5.329156,7.878794,-6.114000,-3.060678,1.611372,-0.022995,1.458182,1.103707,8.076721],[3.504389,3.154272,-4.325629,-6.866016,6.785123,-4.450939,5.292161,3.150394,6.772089],[4.982740,6.487140,9.420789,4.510213,-6.165668,-3.903796,4.882634,5.147585,-9.611058],[1.206054,5.963589,-1.606496,6.368532,-3.199871,-2.701043,-1.592313,9.979334,3.909302],[2.199360,-1.583164,2.436674,-3.280221,-7.123357,8.734576,7.610676,-9.275577,5.141006],[-7.039655,-9.898486,5.191995,6.098800,8.006226,0.397410,2.909336,8.065730,1.081782],[-3.230392,3.959176,8.530506,1.764939,-0.113424,-0.556213,-4.494712,-2.970730,8.040963],[-4.866331,8.208943,-9.403647,-3.693100,0.604624,5.372870,-5.927699,-8.687235,-6.519059],[9.746379,-5.484143,2.123474,8.867095,-4.769685,8.164329,-1.818728,-9.445160,7.459542],[-3.335744,-6.427287,6.256369,-2.175668,9.956353,9.704549,3.924672,1.433306,-3.051576],[-6.103017,-1.693277,9.537741,-7.764884,6.180727,3.719503,5.807163,-1.719787,-0.810702],[3.336424,-3.207243,0.723265,6.652611,-7.073173,3.296234,1.463984,-0.311220,-1.567978],[5.147609,4.629017,8.488138,9.475480,4.905603,-5.153239,0.560312,-4.980410,-8.720404],[-7.816475,-5.455328,-3.042940,0.163912,1.537801,4.416510,-2.795610,8.085033,-1.181231],[-6.808333,8.792830,1.463712,1.128118,-0.462789,-1.098812,-9.875364,-9.975556,5.585787]]], dtype = "float32")#candidate|8325|(7, 16, 9)|const|float32
uop_8326 = relay.sigmoid(const_8325.astype('float32')) # shape=(7, 16, 9)
func_3965_call = mod.get_global_var('func_3965')
func_3968_call = mutated_mod.get_global_var('func_3968')
const_8338 = relay.const([[4,-4],[-10,2],[1,-7],[8,7],[7,-10],[3,4],[-1,7],[-7,-7],[-2,-7],[4,-10],[-5,-1],[3,6],[3,6],[8,-4],[-5,7],[5,10],[6,10],[7,6],[9,5],[-5,-1],[-7,-8],[7,3],[4,3],[-3,7],[-10,-3],[6,-7],[7,6],[-4,-2],[-6,-5],[-2,-6],[-10,8],[-1,7],[1,-6],[-7,2],[8,-6],[9,-3],[-8,-1],[-9,-9],[-7,4],[-1,9],[1,10],[2,-4],[2,-3],[9,7],[6,-10],[-4,-6],[7,8],[3,1],[-5,-1],[-3,-5],[6,5],[6,5],[-9,-7],[-5,3],[-4,-1],[10,-8],[4,-10],[-6,-3],[5,-8],[-9,2],[-9,2],[-3,5],[8,4],[-9,-1],[-4,2],[-7,4],[3,2],[-6,-2],[7,-6],[-1,-8],[8,-6],[-4,2],[7,-10],[6,-6],[-6,3],[-5,5],[-8,-2],[4,9],[2,9],[-2,4],[4,6],[5,-1],[2,-3],[8,1],[-8,9],[3,-4],[-1,10],[5,-3],[-5,-8],[-2,-1],[2,3],[1,10],[-7,5],[-4,6],[3,9],[2,-4],[-2,9],[-3,8],[6,7],[-3,9],[5,3],[-3,5],[7,-4],[9,-5],[-2,4],[-5,-3],[4,-8],[-9,1],[3,5],[3,1],[-5,6],[-5,-4],[-3,4],[-3,-7],[-7,5],[4,-1],[-10,-2],[-6,10],[10,-7],[6,1],[2,-7],[2,-1],[1,-4],[4,9],[-2,4],[3,-1],[-9,-9],[-2,4],[6,6],[-5,7],[-6,10],[-8,3],[-1,-10],[-10,-9],[-1,-6],[9,-6],[3,-4],[-10,-6],[-4,6],[5,-2],[4,-3],[6,7],[-10,-2],[-3,5],[10,-4],[-8,7],[-7,4],[10,-10],[-1,-1],[3,-6],[-1,2],[-9,-1],[4,-9],[8,-6],[1,-6],[-7,7],[9,5],[-8,-5],[-9,4],[-5,7],[2,6],[6,-2],[-2,-7],[-5,5],[4,6],[-10,2],[1,9],[1,-7]], dtype = "uint8")#candidate|8338|(168, 2)|const|uint8
call_8337 = relay.TupleGetItem(func_3965_call(relay.reshape(const_8338.astype('uint8'), [16, 7, 3]), relay.reshape(const_8338.astype('uint8'), [16, 7, 3]), ), 0)
call_8339 = relay.TupleGetItem(func_3968_call(relay.reshape(const_8338.astype('uint8'), [16, 7, 3]), relay.reshape(const_8338.astype('uint8'), [16, 7, 3]), ), 0)
output = relay.Tuple([uop_8326,call_8337,const_8338,])
output2 = relay.Tuple([uop_8326,call_8339,const_8338,])
func_8341 = relay.Function([], output)
mod['func_8341'] = func_8341
mod = relay.transform.InferType()(mod)
output = func_8341()
func_8342 = relay.Function([], output)
mutated_mod['func_8342'] = func_8342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4608_call = mod.get_global_var('func_4608')
func_4609_call = mutated_mod.get_global_var('func_4609')
call_8372 = func_4608_call()
call_8373 = func_4608_call()
func_3101_call = mod.get_global_var('func_3101')
func_3103_call = mutated_mod.get_global_var('func_3103')
call_8374 = relay.TupleGetItem(func_3101_call(), 1)
call_8375 = relay.TupleGetItem(func_3103_call(), 1)
func_4627_call = mod.get_global_var('func_4627')
func_4628_call = mutated_mod.get_global_var('func_4628')
call_8403 = func_4627_call()
call_8404 = func_4627_call()
func_6785_call = mod.get_global_var('func_6785')
func_6787_call = mutated_mod.get_global_var('func_6787')
call_8410 = relay.TupleGetItem(func_6785_call(), 0)
call_8411 = relay.TupleGetItem(func_6787_call(), 0)
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
var_8414 = relay.var("var_8414", dtype = "uint64", shape = (1, 160))#candidate|8414|(1, 160)|var|uint64
call_8413 = relay.TupleGetItem(func_7482_call(relay.reshape(var_8414.astype('uint64'), [160,])), 4)
call_8415 = relay.TupleGetItem(func_7484_call(relay.reshape(var_8414.astype('uint64'), [160,])), 4)
output = relay.Tuple([call_8372,call_8374,call_8403,call_8410,call_8413,var_8414,])
output2 = relay.Tuple([call_8373,call_8375,call_8404,call_8411,call_8415,var_8414,])
func_8416 = relay.Function([var_8414,], output)
mod['func_8416'] = func_8416
mod = relay.transform.InferType()(mod)
var_8417 = relay.var("var_8417", dtype = "uint64", shape = (1, 160))#candidate|8417|(1, 160)|var|uint64
output = func_8416(var_8417)
func_8418 = relay.Function([var_8417], output)
mutated_mod['func_8418'] = func_8418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3719_call = mod.get_global_var('func_3719')
func_3721_call = mutated_mod.get_global_var('func_3721')
call_8449 = relay.TupleGetItem(func_3719_call(), 7)
call_8450 = relay.TupleGetItem(func_3721_call(), 7)
func_2373_call = mod.get_global_var('func_2373')
func_2377_call = mutated_mod.get_global_var('func_2377')
var_8454 = relay.var("var_8454", dtype = "float64", shape = (40,))#candidate|8454|(40,)|var|float64
const_8455 = relay.const([-1.979181,8.908505,3.296811,-0.604970,-8.728069,3.735128,-3.547765,-8.727102,-4.824398,9.643791,-5.950130,-6.320853,9.317321,-6.252200,5.992813,-0.553445,4.142995,0.125100,0.970136,3.231953,-4.205435,-5.332886,-9.707937,-4.545263,-2.162453,6.134889,4.340148,3.157729,1.758261,-8.084235,7.779607,0.741048,-8.025889,7.303264,-2.052421,2.129720,1.852233,3.116897,-9.328756,-8.894798,4.665942,8.086718,9.377234,-2.800398,-0.762381,4.452259,9.539371,-3.350799,6.063517,-5.309832,-4.167094,0.532388,6.954108,2.943522,-0.914511,-6.083858,-9.950484,5.304649,-2.144760,-0.549641,-8.456253,-4.105798,-4.081595,4.339821,-3.126843,5.027144,2.626912,-8.382247,-6.933918,8.227783,4.780434,-1.726542,7.416487,3.007557,2.639205,2.006610,4.896035,-5.825776,-4.023491,-3.059957,0.771020,-4.569120,-8.895870,3.484245,-5.173689,1.770102,-1.621588,4.948904,2.511447,1.936826,4.113746,-3.323598,-3.172837,-4.199515,-2.691320,9.408127,8.843900,3.380788,-0.314128,-6.057203,5.023638,-8.644278,8.892964,1.457036,-4.846609,-3.160801,3.121621,-5.357441,8.038233,6.247640,9.127498,3.614719,-2.129701,-3.622611,0.697011,8.222210,9.441573,-5.887985,-0.534244,3.418501,-2.502680,-1.474859,1.963984,5.841466,4.538349,-2.509006,5.126001,0.858398,-7.289831,-4.843843,-8.666877,-3.825284,8.489981,3.681081,7.881822,-5.736823,-2.423629,9.314087,8.607562,-6.091772,1.972823,-5.903587,-1.972459,-9.513610,2.600839,-0.146359,8.961533,4.436339,7.519533,-7.927152,-8.783771,-3.302943,8.336769,-7.111359,-2.642253,9.731235,7.424167,-8.538292,-4.901680,1.519974,5.394828,0.747010,-2.429026,6.035356,2.037766,-6.984578,-5.127994,-8.619696,4.408408,-8.327422,1.912405,7.013245,0.554488,-5.095862,8.046162,-9.902837,2.257317,1.611814,-4.528608,7.961085,-4.298547,4.365422,-9.718230,-9.028431,-9.435601,1.867481,-3.173004,6.935854,-5.410466,6.916944,0.012197,-1.487689,-6.447967,-5.460985,-3.667050,-8.616606,-5.592496,2.959197,-4.648175,-7.899828,0.176850,-2.212061,-1.373779,1.247722,-3.099895,-8.158663,-1.787722,-3.716769,-0.312723,-6.323521,9.735993,7.484136,-0.211789,-1.725904,-6.577602,-1.102326,8.113538,-9.858595,-5.958664,-2.662503,-2.156817,-5.566266,-9.194579,9.839880,0.923876,7.213412,3.909502,-6.292173,-2.890198,-3.989156,9.132935,-4.615309,3.114896,4.935193,-0.343988,-7.311219,-9.266560,-5.835899,-9.480397,-0.189253,8.014667,-0.141809,-8.872267,-5.002941,9.785628,-9.867795,9.848849,2.027935,3.091385,-9.501349,5.473823,-3.527680,4.171171,-4.483086,4.326055,-4.001536,-2.773986,0.644823,5.198924,8.501727,-9.972148,-4.941321,-1.117102,-9.389805,-8.157814,-2.156451,-2.061631,4.620003,2.754774,4.731160,-4.351691,8.271780,-4.777285,-5.070004,-4.892597,-1.812458,2.079429,9.731762,6.773258,0.106588,-7.512265,7.427498,-5.960000,4.178525,-6.635644,-8.690490,-7.435857,2.272642,-4.904070,-6.182867,-0.734339,3.616711,6.230242,2.618418,6.501676,-9.260205,-2.444922,-0.299285,6.706473,-8.965517,-2.420313,-8.865815,-8.004909,2.922285,9.565535,-3.952129,-5.365290,6.449510,-5.176611,-1.332982,4.988655,8.364527,-8.169447,2.354030,8.180794,2.404293,-6.357365,-5.211216,-5.231913,-5.721088,-0.961885,0.077501,-9.615699,-2.418795,4.032624,-6.107435,-0.966974,0.634666,1.511092,-2.061659,-7.703487,-3.783572,4.217537,-9.889341,-9.812255,-1.592500,7.440582,-0.402824,-1.962505,-7.157646,0.322098,6.008653,-8.657428,2.127273,5.837618,2.763136,4.782658,-8.336519,-1.794765,-8.614359,3.303344,6.144271,-6.245430,0.915584,7.603474,6.508771,-6.800710,-6.048625,3.613587,7.252013], dtype = "float64")#candidate|8455|(360,)|const|float64
call_8453 = relay.TupleGetItem(func_2373_call(relay.reshape(var_8454.astype('float64'), [1, 8, 5]), relay.reshape(const_8455.astype('float64'), [9, 8, 5]), ), 0)
call_8456 = relay.TupleGetItem(func_2377_call(relay.reshape(var_8454.astype('float64'), [1, 8, 5]), relay.reshape(const_8455.astype('float64'), [9, 8, 5]), ), 0)
output = relay.Tuple([call_8449,call_8453,var_8454,const_8455,])
output2 = relay.Tuple([call_8450,call_8456,var_8454,const_8455,])
func_8458 = relay.Function([var_8454,], output)
mod['func_8458'] = func_8458
mod = relay.transform.InferType()(mod)
var_8459 = relay.var("var_8459", dtype = "float64", shape = (40,))#candidate|8459|(40,)|var|float64
output = func_8458(var_8459)
func_8460 = relay.Function([var_8459], output)
mutated_mod['func_8460'] = func_8460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2556_call = mod.get_global_var('func_2556')
func_2557_call = mutated_mod.get_global_var('func_2557')
call_8523 = relay.TupleGetItem(func_2556_call(), 1)
call_8524 = relay.TupleGetItem(func_2557_call(), 1)
output = relay.Tuple([call_8523,])
output2 = relay.Tuple([call_8524,])
func_8528 = relay.Function([], output)
mod['func_8528'] = func_8528
mod = relay.transform.InferType()(mod)
mutated_mod['func_8528'] = func_8528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8528_call = mutated_mod.get_global_var('func_8528')
call_8529 = func_8528_call()
output = call_8529
func_8530 = relay.Function([], output)
mutated_mod['func_8530'] = func_8530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6732_call = mod.get_global_var('func_6732')
func_6734_call = mutated_mod.get_global_var('func_6734')
call_8546 = relay.TupleGetItem(func_6732_call(), 0)
call_8547 = relay.TupleGetItem(func_6734_call(), 0)
output = call_8546
output2 = call_8547
func_8560 = relay.Function([], output)
mod['func_8560'] = func_8560
mod = relay.transform.InferType()(mod)
output = func_8560()
func_8561 = relay.Function([], output)
mutated_mod['func_8561'] = func_8561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1419_call = mod.get_global_var('func_1419')
func_1420_call = mutated_mod.get_global_var('func_1420')
call_8562 = relay.TupleGetItem(func_1419_call(), 0)
call_8563 = relay.TupleGetItem(func_1420_call(), 0)
output = call_8562
output2 = call_8563
func_8566 = relay.Function([], output)
mod['func_8566'] = func_8566
mod = relay.transform.InferType()(mod)
mutated_mod['func_8566'] = func_8566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8566_call = mutated_mod.get_global_var('func_8566')
call_8567 = func_8566_call()
output = call_8567
func_8568 = relay.Function([], output)
mutated_mod['func_8568'] = func_8568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4739_call = mod.get_global_var('func_4739')
func_4741_call = mutated_mod.get_global_var('func_4741')
call_8600 = relay.TupleGetItem(func_4739_call(), 4)
call_8601 = relay.TupleGetItem(func_4741_call(), 4)
output = call_8600
output2 = call_8601
func_8606 = relay.Function([], output)
mod['func_8606'] = func_8606
mod = relay.transform.InferType()(mod)
mutated_mod['func_8606'] = func_8606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8606_call = mutated_mod.get_global_var('func_8606')
call_8607 = func_8606_call()
output = call_8607
func_8608 = relay.Function([], output)
mutated_mod['func_8608'] = func_8608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4649_call = mod.get_global_var('func_4649')
func_4651_call = mutated_mod.get_global_var('func_4651')
call_8623 = relay.TupleGetItem(func_4649_call(), 1)
call_8624 = relay.TupleGetItem(func_4651_call(), 1)
uop_8625 = relay.log(call_8623.astype('float32')) # shape=(33,)
uop_8627 = relay.log(call_8624.astype('float32')) # shape=(33,)
bop_8628 = relay.bitwise_xor(uop_8625.astype('int8'), relay.reshape(call_8623.astype('int8'), relay.shape_of(uop_8625))) # shape=(33,)
bop_8631 = relay.bitwise_xor(uop_8627.astype('int8'), relay.reshape(call_8624.astype('int8'), relay.shape_of(uop_8627))) # shape=(33,)
output = relay.Tuple([bop_8628,])
output2 = relay.Tuple([bop_8631,])
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
