import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_42 = relay.var("var_42", dtype = "float32", shape = (3, 10, 12))#candidate|42|(3, 10, 12)|var|float32
const_43 = relay.const([[[7.684596,1.985716,0.115539,5.816880,9.118950,4.990653,5.022931,-7.935244,9.272108,-8.399682,-6.411949,-2.379338],[-4.974836,7.239770,2.544676,-7.062956,5.623377,4.161494,7.272326,0.537358,3.595700,5.988370,7.647147,3.841245],[-0.842276,-1.744291,4.944162,9.904513,4.471130,-2.309598,7.614555,5.623772,-9.320781,0.627421,2.548621,-9.130538],[6.394632,-8.536912,4.499615,8.595761,2.947810,-7.971672,-0.929536,2.003495,-1.263227,2.387880,-0.438738,-9.148707],[5.004138,-0.049642,-0.453139,7.035105,-1.057253,-2.672422,3.486117,6.543753,2.858555,7.123054,5.836891,2.214569],[-1.490368,-4.780142,7.188497,5.618260,-2.820489,-5.754084,-7.494865,0.838736,5.751921,-6.764913,6.314706,4.896868],[6.955735,5.524038,0.465680,9.981240,3.592911,9.593394,-7.894961,0.123990,-0.882607,-0.335667,3.343124,-9.721503],[9.297357,5.501878,-3.179160,-6.153125,4.729965,2.962652,-4.420819,9.589512,-2.345236,7.405467,6.927906,1.508382],[-6.808003,2.594578,2.570580,-3.156404,-5.490927,-8.666213,-9.984028,0.923655,-2.863317,5.038092,1.022518,-6.998509],[8.856605,-8.948976,-9.070089,-7.036315,1.070941,-1.253611,3.149956,-5.431064,-4.819098,8.277800,3.719387,-4.787367]],[[4.317040,-3.684089,-4.329084,-6.882033,-6.829074,3.133451,-1.712641,8.284699,0.769921,0.134594,-4.393216,-0.526511],[-8.531263,-2.736237,-5.919739,1.992600,-6.801510,-9.369899,-5.453287,-9.350845,-9.597967,3.640226,9.866500,-4.387628],[-5.097776,-0.234732,1.985177,1.368411,-4.035927,1.690605,-7.043810,-3.161558,9.107562,-3.283103,8.470345,-1.722161],[-7.378193,-0.418531,6.572134,-8.512556,-3.273884,-6.846341,8.986899,0.873336,2.813873,9.721364,6.579115,-2.896860],[-1.575546,-6.770565,5.016269,7.083834,-5.587797,-2.499653,5.751944,6.453360,5.648873,6.030828,8.174995,-1.163455],[-5.835331,9.961045,7.559750,-9.221449,-8.468144,2.453854,2.828406,5.670149,-9.136206,3.113524,-7.001597,-7.998032],[8.670498,-7.092218,-8.614985,3.319936,-3.005693,7.229985,8.159772,-9.818826,-1.561200,1.752167,-4.362883,-1.161510],[-4.255736,-8.845799,-1.847651,-0.505000,7.417928,6.373383,2.391822,-7.859773,1.264911,9.539836,2.221264,-0.484303],[6.632230,5.558702,-0.581388,6.992724,-8.012617,9.775362,-4.783977,-2.175733,-8.126537,4.409764,-5.747377,-3.720723],[5.011549,-7.105451,7.097136,4.464659,0.072332,-6.558784,-5.559231,-2.571952,-1.886455,6.187013,-4.549329,-2.441853]],[[8.039485,-4.132634,2.453904,1.809564,9.619395,2.188573,-2.172065,2.048773,0.543075,1.294324,8.399386,-7.027358],[4.466145,-3.761940,7.902033,3.967769,9.607215,0.954349,-4.717311,2.342082,-7.689596,-7.653251,7.504549,-8.744904],[4.144920,-8.285131,-4.558342,-9.582057,9.476445,2.577021,1.193307,7.239485,-6.490763,8.966702,-2.213008,-7.648498],[1.873456,8.845883,6.111729,-9.664617,-2.734683,8.174166,9.640293,-6.911791,1.988704,-0.190749,-9.807925,0.812530],[-8.019370,9.720065,2.767705,8.122487,-0.111763,-2.879211,2.947393,7.235326,1.477022,-0.869224,-2.315640,6.753764],[-7.004300,9.304823,-8.662193,8.831425,8.191294,6.560411,4.600465,-2.059360,0.182520,5.943903,1.687574,-2.681766],[0.063342,0.881745,-4.605254,3.521345,-3.704935,8.914263,8.613117,9.706633,-0.374514,-9.396578,-8.875134,6.057610],[7.339118,-5.151124,3.311873,3.406423,1.975511,1.960246,-4.781359,-5.804698,6.590855,2.256109,-2.600372,9.655801],[0.702768,-2.027281,-4.341330,0.813161,-0.823242,-1.352568,7.578234,7.199552,8.731541,-8.395375,5.703709,-8.258157],[-5.944009,-0.818931,7.113729,4.345583,1.421894,-2.653921,-6.374188,8.265495,5.732754,-4.443356,8.951785,6.800586]]], dtype = "float32")#candidate|43|(3, 10, 12)|const|float32
bop_44 = relay.mod(var_42.astype('float32'), relay.reshape(const_43.astype('float32'), relay.shape_of(var_42))) # shape=(3, 10, 12)
output = bop_44
output2 = bop_44
func_50 = relay.Function([var_42,], output)
mod['func_50'] = func_50
mod = relay.transform.InferType()(mod)
mutated_mod['func_50'] = func_50
mutated_mod = relay.transform.InferType()(mutated_mod)
var_51 = relay.var("var_51", dtype = "float32", shape = (3, 10, 12))#candidate|51|(3, 10, 12)|var|float32
func_50_call = mutated_mod.get_global_var('func_50')
call_52 = func_50_call(var_51)
output = call_52
func_53 = relay.Function([var_51], output)
mutated_mod['func_53'] = func_53
mutated_mod = relay.transform.InferType()(mutated_mod)
var_340 = relay.var("var_340", dtype = "float32", shape = ())#candidate|340|()|var|float32
var_341 = relay.var("var_341", dtype = "float32", shape = (1, 1, 16))#candidate|341|(1, 1, 16)|var|float32
bop_342 = relay.divide(var_340.astype('float32'), var_341.astype('float32')) # shape=(1, 1, 16)
func_50_call = mod.get_global_var('func_50')
func_53_call = mutated_mod.get_global_var('func_53')
const_353 = relay.const([-5.580579,-6.013555,-0.477355,7.137809,-3.883303,-1.902541,1.962017,4.519630,5.966139,6.135563,-3.488653,-2.879472,-7.202191,0.109849,-7.988749,9.272975,9.880029,3.854883,-9.099712,-9.024674,2.924205,5.167360,-1.463731,-2.802561,1.656500,-0.425223,-0.641666,-2.325501,-4.990701,-5.008208,7.563368,-1.595856,0.413406,-4.421603,-3.620834,-7.846400,-7.241420,0.862776,-8.277017,-2.583871,6.576216,3.531377,9.889506,-1.276062,-5.847899,-0.012536,-5.534071,-1.624776,1.498711,-2.387773,-2.978022,5.317565,-2.936612,7.439734,-7.532086,7.964916,-0.638030,5.206861,-4.618009,7.351938,-4.947635,-2.836137,-6.944400,-7.569899,-6.395976,-1.250845,8.885131,9.345466,-9.611697,-4.901736,-7.153007,-7.951352,5.523095,-1.872111,-4.019306,-6.159540,8.463565,9.104761,1.596640,2.065717,-6.624106,-7.164689,7.113213,-3.204080,-3.969867,-0.358677,-9.893351,0.358563,-7.006258,6.888134,-1.621528,0.064828,4.319680,4.683269,-9.598218,-7.698812,-8.095785,-1.496731,-2.155434,5.097970,-9.065246,0.311114,5.541712,-7.724416,-2.348530,-2.981479,2.754826,-7.227062,-9.161842,8.184413,0.767582,-1.586991,5.485387,0.071994,7.868669,-5.103719,8.579762,-8.112106,3.578669,-1.970908,-7.183693,-9.136478,4.027105,-4.573873,-6.717933,-6.816497,8.516970,-2.916266,-7.288916,-7.863354,-1.519217,4.787772,-0.673185,-4.238486,-0.347328,6.983820,6.961602,-0.861099,3.908066,7.176772,-0.694885,7.367457,-7.228063,-0.552325,3.103320,-9.486614,-5.876781,7.093543,3.053334,-9.898451,9.980571,-3.051762,2.240385,7.061527,-1.765903,-1.174770,-3.676215,-8.728270,8.026824,4.324645,-4.352283,0.881381,6.490556,7.657981,-2.739904,-9.795750,-8.655473,8.377424,1.804401,-5.513967,7.117405,6.720146,-3.576320,-5.278760,-7.517280,-4.788027,3.822044,0.725600,4.883751,4.881070,-5.834042,4.371818,-0.564948,-1.921391,2.501053,0.024174,-0.771024,-9.380467,9.268318,-3.210494,7.519024,-8.324046,-1.125753,4.353110,-1.702633,-0.255451,5.684774,1.850481,-0.949091,7.043315,-8.551362,-3.419889,5.752449,6.371091,7.243950,4.443390,5.935360,6.150725,7.032033,6.039978,8.980657,9.874454,2.388869,-6.567828,-3.014961,9.534248,2.479888,0.169552,-8.265532,7.782563,5.105754,-3.083781,-8.738291,-9.638287,2.344439,6.970477,2.650278,4.123430,-9.782100,-2.254849,2.950826,8.691893,2.828235,-4.452074,-6.638709,0.719276,-9.408968,-8.019212,0.435643,-0.113540,-7.958099,7.109539,-2.791419,-3.640364,3.850265,-8.774565,-7.601053,8.167173,-4.418927,0.600502,9.928325,-0.018997,8.511926,-6.917847,-8.697559,1.299225,-1.358616,-6.967880,2.439234,4.835276,-9.934330,7.114002,-9.623146,-7.186943,-5.787744,5.200669,9.103984,5.997990,-9.816249,4.219592,4.421547,7.901457,-4.745066,-9.759108,-4.354702,-5.381695,1.754420,2.478039,-0.212702,5.296863,9.312311,-4.608371,-8.063452,5.038085,3.751431,0.198423,5.011917,-3.459708,9.637105,5.553381,2.358022,-9.571789,-1.018874,-9.744011,6.264174,2.561303,-0.072943,9.831056,-7.251660,5.298982,-4.783795,-0.257729,7.491117,7.651360,9.197521,-5.917348,-1.952967,-6.666968,-1.078110,0.522532,-7.397827,-9.444042,-3.310534,1.081247,3.352117,-4.134767,-7.044568,9.646084,9.931005,-2.881689,-0.070366,2.829774,1.116969,8.312940,-7.348528,5.679048,5.011213,1.089418,-9.900368,-7.285054,3.914962,2.877094,8.802029,9.171644,8.664734,-0.625064,-7.853975,-8.092156,6.079456,8.906451,-3.056366,-8.552346,8.160811,2.187121,-5.936287,3.542022,-2.304752,4.979496,6.534036,-7.757926,-0.078885,-9.834506,9.611206,-0.691984,-6.235350,-2.238527,7.906008,5.729533,0.521385,-9.957345], dtype = "float32")#candidate|353|(360,)|const|float32
call_352 = func_50_call(relay.reshape(const_353.astype('float32'), [3, 10, 12]))
call_354 = func_50_call(relay.reshape(const_353.astype('float32'), [3, 10, 12]))
uop_358 = relay.exp(bop_342.astype('float64')) # shape=(1, 1, 16)
uop_361 = relay.rsqrt(uop_358.astype('float64')) # shape=(1, 1, 16)
bop_364 = relay.floor_divide(uop_361.astype('float32'), relay.reshape(uop_358.astype('float32'), relay.shape_of(uop_361))) # shape=(1, 1, 16)
output = relay.Tuple([call_352,const_353,bop_364,])
output2 = relay.Tuple([call_354,const_353,bop_364,])
func_369 = relay.Function([var_340,var_341,], output)
mod['func_369'] = func_369
mod = relay.transform.InferType()(mod)
var_370 = relay.var("var_370", dtype = "float32", shape = ())#candidate|370|()|var|float32
var_371 = relay.var("var_371", dtype = "float32", shape = (1, 1, 16))#candidate|371|(1, 1, 16)|var|float32
output = func_369(var_370,var_371,)
func_372 = relay.Function([var_370,var_371,], output)
mutated_mod['func_372'] = func_372
mutated_mod = relay.transform.InferType()(mutated_mod)
var_718 = relay.var("var_718", dtype = "float64", shape = (13, 4, 9))#candidate|718|(13, 4, 9)|var|float64
var_719 = relay.var("var_719", dtype = "float64", shape = (13, 4, 9))#candidate|719|(13, 4, 9)|var|float64
bop_720 = relay.less_equal(var_718.astype('bool'), relay.reshape(var_719.astype('bool'), relay.shape_of(var_718))) # shape=(13, 4, 9)
output = bop_720
output2 = bop_720
func_733 = relay.Function([var_718,var_719,], output)
mod['func_733'] = func_733
mod = relay.transform.InferType()(mod)
var_734 = relay.var("var_734", dtype = "float64", shape = (13, 4, 9))#candidate|734|(13, 4, 9)|var|float64
var_735 = relay.var("var_735", dtype = "float64", shape = (13, 4, 9))#candidate|735|(13, 4, 9)|var|float64
output = func_733(var_734,var_735,)
func_736 = relay.Function([var_734,var_735,], output)
mutated_mod['func_736'] = func_736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_804 = relay.var("var_804", dtype = "float32", shape = (6, 3, 3))#candidate|804|(6, 3, 3)|var|float32
uop_805 = relay.log(var_804.astype('float32')) # shape=(6, 3, 3)
output = relay.Tuple([uop_805,])
output2 = relay.Tuple([uop_805,])
func_813 = relay.Function([var_804,], output)
mod['func_813'] = func_813
mod = relay.transform.InferType()(mod)
mutated_mod['func_813'] = func_813
mutated_mod = relay.transform.InferType()(mutated_mod)
var_814 = relay.var("var_814", dtype = "float32", shape = (6, 3, 3))#candidate|814|(6, 3, 3)|var|float32
func_813_call = mutated_mod.get_global_var('func_813')
call_815 = func_813_call(var_814)
output = call_815
func_816 = relay.Function([var_814], output)
mutated_mod['func_816'] = func_816
mutated_mod = relay.transform.InferType()(mutated_mod)
var_856 = relay.var("var_856", dtype = "float64", shape = (9, 16, 12))#candidate|856|(9, 16, 12)|var|float64
uop_857 = relay.tan(var_856.astype('float64')) # shape=(9, 16, 12)
uop_863 = relay.cos(uop_857.astype('float64')) # shape=(9, 16, 12)
bop_870 = relay.multiply(uop_857.astype('int8'), relay.reshape(var_856.astype('int8'), relay.shape_of(uop_857))) # shape=(9, 16, 12)
func_733_call = mod.get_global_var('func_733')
func_736_call = mutated_mod.get_global_var('func_736')
const_876 = relay.const([[1.020850,-5.215951,0.379548,-6.037375,-6.459399,4.974035,-8.896659,2.406832,-1.944693,-3.787495,-1.258606,-3.387229,8.205532,-4.425575,0.714795,9.587129,-2.323199,-4.447179,8.759839,-3.020384,-0.082521,0.711834,-6.177821,-3.072880,-7.998404,0.698248,5.154167,-2.587180,3.427147,-0.335766,-8.259473,-3.506100,7.145763,8.241405,0.324565,3.344521,2.451134,-5.027959,1.819108,-6.347599,5.878453,-9.867510,-0.649238,1.653079,-0.106840,-0.419028,1.537450,7.764401,5.651264,7.415753,6.982890,-7.441461,-4.092330,-8.168368,3.081295,7.225519,-3.314849,7.244928,-3.315573,5.141852,-6.804267,7.266146,-4.124685,1.648456,3.755954,-3.189278,1.267426,-2.178353,0.425043,2.143119,9.287121,9.582213,4.313232,-0.836895,4.884554,-7.553561,5.487067,3.833313],[-3.314411,8.592643,7.252623,-0.170890,2.331683,-4.034477,-6.961276,1.140614,-6.661789,2.814986,-3.964565,2.763251,9.624440,3.366190,-8.188618,-6.511687,0.752244,-0.836176,4.369987,2.339576,9.164638,0.354774,-3.387478,-6.337240,8.080871,-6.457800,3.256171,6.978099,6.395968,-0.847112,1.853339,-9.459443,-3.038924,-5.684655,-0.035717,-7.458974,2.393339,7.966795,4.808628,1.311320,4.276353,-9.916903,3.867312,-6.039532,-4.022049,-8.089137,9.827882,3.882533,-8.686974,-2.865421,2.421008,-9.299554,-8.764746,-8.401484,4.276494,3.951859,8.924329,-4.065828,1.636028,6.149694,9.803791,-7.482468,8.103786,-6.904494,4.132854,-7.623905,-9.800667,7.376636,-7.156686,-7.443222,9.070976,-5.753002,5.124540,-2.480678,2.302007,-4.920377,6.325788,-2.335638],[-6.250259,-2.978299,9.327196,4.115176,-2.197091,-7.538175,-9.402731,-7.075813,-6.614486,9.300226,5.085877,0.532504,7.071278,6.737198,-4.222554,8.221074,1.884696,-5.499615,-6.352708,-5.352573,-9.249855,5.554823,1.587702,3.082463,9.803383,7.618705,-6.936478,2.501812,-8.165088,-0.550628,-9.799654,-4.957825,-2.237462,-5.007983,-3.638623,5.281904,-5.386144,5.075967,-5.108606,7.913358,1.148585,3.486560,4.745270,-0.602992,4.145546,-9.852336,-7.239181,2.812315,2.846222,-3.606975,-2.924270,1.479019,-8.809924,-0.885046,7.841479,-7.114689,-4.535764,-1.484981,0.121522,-2.345986,0.160235,-1.156228,5.123914,-0.571887,-9.524119,-6.853509,-2.859607,8.810861,-8.946299,-6.924044,4.607184,1.153715,-3.665577,-6.770907,-4.943209,-9.099008,6.090965,1.502168],[4.720801,-6.899850,-3.393133,-1.059558,-4.057852,-2.573001,-8.646003,-4.788368,4.211948,4.965388,4.137700,0.916562,-8.984156,3.436962,6.693829,-6.162770,9.761482,-0.109378,9.694975,-3.643273,-2.098332,0.345668,4.637141,-8.977022,3.157759,-1.775341,2.212010,-2.398986,-9.297028,-8.727704,-8.818482,-6.748464,8.459023,-4.894731,6.533236,-9.368935,3.709514,-9.322839,8.468213,9.669036,6.219605,4.772756,-9.041133,-7.587290,2.778083,-4.729183,-9.770785,6.233577,8.148534,-1.690807,0.817398,-3.501254,-9.490853,7.171766,9.033346,-5.682520,3.821263,-1.606168,8.930218,-1.313671,7.060855,9.139217,2.092601,4.960208,-8.875667,5.585019,-9.977102,-7.094644,9.483038,-6.575127,-0.558018,3.750463,-0.494611,4.428351,-7.532218,-0.388939,-4.083657,4.729473],[6.821186,-6.057614,5.256119,9.000286,8.179834,-9.841024,9.412700,-7.802828,-3.251001,8.299887,1.675184,-8.577060,-8.054117,8.067595,-5.714588,-8.114078,5.821548,7.205554,1.164745,-8.932712,-7.922761,4.192549,7.759584,-8.599734,6.784662,-4.760868,-4.850599,-8.598094,9.735055,-4.931156,5.905837,3.840624,1.223712,2.654253,7.176138,-1.024630,-5.242520,-6.982403,7.464768,6.952763,-9.103317,1.384200,3.792209,-6.076156,2.434940,-7.199855,8.798541,6.119405,8.192637,3.568883,-4.704276,-9.000225,8.074204,-8.383737,9.650282,5.031074,5.901051,3.967113,0.200126,2.388923,-9.411753,6.489234,-9.862745,-0.884147,5.310089,-4.295390,1.943724,-0.526423,1.296439,7.709480,4.331039,7.779105,8.246087,9.234957,-1.022523,7.251082,-9.268503,-4.243671],[0.346323,-5.746834,0.620286,-2.197186,-6.992963,3.557778,8.485686,-8.934990,-1.577191,4.325974,-9.984886,-8.825600,-7.588018,7.168723,-5.106508,2.240955,5.873852,-8.885565,-9.176824,3.534018,6.792476,5.680820,-7.584807,0.387324,0.614920,-6.427980,8.721898,-4.837779,9.622784,7.413055,6.154644,8.423732,-9.405873,6.181455,3.510052,1.631708,-9.015065,9.898693,9.960609,8.684889,-3.473169,-6.035347,-4.228578,9.217327,3.377851,4.836087,1.826440,9.553612,-5.911051,-2.723344,7.584731,-7.239887,-1.051632,-3.934397,7.034198,-1.808624,-9.795132,4.905108,8.463874,-4.330074,2.204230,-7.585771,-5.493883,7.880409,-0.685679,-2.373825,8.197331,6.017872,2.356421,1.848286,8.567653,-5.725543,6.158344,-9.023715,-6.129695,0.480054,-5.438321,-5.499588]], dtype = "float64")#candidate|876|(6, 78)|const|float64
call_875 = func_733_call(relay.reshape(const_876.astype('float64'), [13, 4, 9]), relay.reshape(const_876.astype('float64'), [13, 4, 9]), )
call_877 = func_733_call(relay.reshape(const_876.astype('float64'), [13, 4, 9]), relay.reshape(const_876.astype('float64'), [13, 4, 9]), )
var_887 = relay.var("var_887", dtype = "float64", shape = (9, 16, 12))#candidate|887|(9, 16, 12)|var|float64
bop_888 = relay.subtract(uop_863.astype('uint16'), relay.reshape(var_887.astype('uint16'), relay.shape_of(uop_863))) # shape=(9, 16, 12)
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
var_897 = relay.var("var_897", dtype = "float32", shape = (54,))#candidate|897|(54,)|var|float32
call_896 = relay.TupleGetItem(func_813_call(relay.reshape(var_897.astype('float32'), [6, 3, 3])), 0)
call_898 = relay.TupleGetItem(func_816_call(relay.reshape(var_897.astype('float32'), [6, 3, 3])), 0)
uop_899 = relay.sigmoid(bop_888.astype('float64')) # shape=(9, 16, 12)
func_733_call = mod.get_global_var('func_733')
func_736_call = mutated_mod.get_global_var('func_736')
call_903 = func_733_call(relay.reshape(call_875.astype('float64'), [13, 4, 9]), relay.reshape(call_875.astype('float64'), [13, 4, 9]), )
call_904 = func_733_call(relay.reshape(call_875.astype('float64'), [13, 4, 9]), relay.reshape(call_875.astype('float64'), [13, 4, 9]), )
uop_913 = relay.rsqrt(uop_857.astype('float64')) # shape=(9, 16, 12)
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
call_920 = relay.TupleGetItem(func_813_call(relay.reshape(var_897.astype('float32'), [6, 3, 3])), 0)
call_921 = relay.TupleGetItem(func_816_call(relay.reshape(var_897.astype('float32'), [6, 3, 3])), 0)
output = relay.Tuple([bop_870,call_875,const_876,call_896,var_897,uop_899,call_903,uop_913,call_920,])
output2 = relay.Tuple([bop_870,call_877,const_876,call_898,var_897,uop_899,call_904,uop_913,call_921,])
func_935 = relay.Function([var_856,var_887,var_897,], output)
mod['func_935'] = func_935
mod = relay.transform.InferType()(mod)
var_936 = relay.var("var_936", dtype = "float64", shape = (9, 16, 12))#candidate|936|(9, 16, 12)|var|float64
var_937 = relay.var("var_937", dtype = "float64", shape = (9, 16, 12))#candidate|937|(9, 16, 12)|var|float64
var_938 = relay.var("var_938", dtype = "float32", shape = (54,))#candidate|938|(54,)|var|float32
output = func_935(var_936,var_937,var_938,)
func_939 = relay.Function([var_936,var_937,var_938,], output)
mutated_mod['func_939'] = func_939
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1298 = relay.var("var_1298", dtype = "float32", shape = (6, 16, 7))#candidate|1298|(6, 16, 7)|var|float32
var_1299 = relay.var("var_1299", dtype = "float32", shape = (6, 16, 7))#candidate|1299|(6, 16, 7)|var|float32
bop_1300 = relay.greater_equal(var_1298.astype('bool'), relay.reshape(var_1299.astype('bool'), relay.shape_of(var_1298))) # shape=(6, 16, 7)
output = bop_1300
output2 = bop_1300
func_1310 = relay.Function([var_1298,var_1299,], output)
mod['func_1310'] = func_1310
mod = relay.transform.InferType()(mod)
var_1311 = relay.var("var_1311", dtype = "float32", shape = (6, 16, 7))#candidate|1311|(6, 16, 7)|var|float32
var_1312 = relay.var("var_1312", dtype = "float32", shape = (6, 16, 7))#candidate|1312|(6, 16, 7)|var|float32
output = func_1310(var_1311,var_1312,)
func_1313 = relay.Function([var_1311,var_1312,], output)
mutated_mod['func_1313'] = func_1313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1537 = relay.var("var_1537", dtype = "float64", shape = (13, 7, 13))#candidate|1537|(13, 7, 13)|var|float64
uop_1538 = relay.rsqrt(var_1537.astype('float64')) # shape=(13, 7, 13)
output = uop_1538
output2 = uop_1538
func_1551 = relay.Function([var_1537,], output)
mod['func_1551'] = func_1551
mod = relay.transform.InferType()(mod)
var_1552 = relay.var("var_1552", dtype = "float64", shape = (13, 7, 13))#candidate|1552|(13, 7, 13)|var|float64
output = func_1551(var_1552)
func_1553 = relay.Function([var_1552], output)
mutated_mod['func_1553'] = func_1553
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1671 = relay.const([[[2.685796],[5.394594],[-5.013237],[7.045397],[5.492567],[-4.388946],[-7.733881],[-8.194625],[-9.145539],[-3.704088],[-9.595575],[-1.042464]],[[-3.771338],[6.822992],[-1.429492],[-8.283870],[-3.986913],[1.233001],[4.383462],[-5.818019],[9.912687],[9.385047],[3.166150],[2.374777]],[[-1.236992],[1.953468],[0.143581],[-7.356339],[7.002238],[9.135609],[-8.722451],[4.020215],[-2.526361],[9.917965],[-4.956628],[-6.133961]],[[-3.719607],[7.631722],[7.941757],[5.201766],[0.532966],[-5.870039],[7.885047],[-8.468202],[-9.681176],[-1.614941],[2.376431],[8.079232]],[[6.895727],[5.676906],[3.486854],[8.661100],[-4.718698],[9.400241],[7.812391],[8.315383],[-1.436300],[8.784153],[-9.217764],[-0.990944]],[[-3.222384],[-0.459029],[-4.110802],[3.881566],[-8.001144],[5.127723],[-9.761864],[-3.609121],[-9.108476],[-9.499079],[-2.105810],[-8.612829]],[[6.037151],[-1.850761],[4.358966],[2.511822],[-6.970805],[-5.724701],[7.227391],[-2.676557],[-6.496138],[2.084511],[-8.476872],[2.053827]],[[-1.254493],[-5.328091],[3.136933],[7.519649],[6.380566],[4.964576],[-2.414686],[-7.760861],[-2.330691],[4.565762],[-7.752098],[8.287339]],[[-9.067318],[2.766689],[-8.318711],[6.017298],[-8.804079],[-2.102981],[-5.141585],[-0.521208],[3.910359],[-6.541672],[-3.677055],[-4.490152]]], dtype = "float64")#candidate|1671|(9, 12, 1)|const|float64
uop_1672 = relay.log10(const_1671.astype('float64')) # shape=(9, 12, 1)
func_369_call = mod.get_global_var('func_369')
func_372_call = mutated_mod.get_global_var('func_372')
const_1675 = relay.const(-1.757708, dtype = "float32")#candidate|1675|()|const|float32
const_1676 = relay.const([[-8.215252,-6.038736],[-8.803544,-1.776526],[1.293868,2.332985],[4.134994,-8.592779],[-9.166132,0.031545],[8.306301,-1.689746],[4.888984,0.858258],[4.360615,-7.243024]], dtype = "float32")#candidate|1676|(8, 2)|const|float32
call_1674 = relay.TupleGetItem(func_369_call(relay.reshape(const_1675.astype('float32'), []), relay.reshape(const_1676.astype('float32'), [1, 1, 16]), ), 2)
call_1677 = relay.TupleGetItem(func_372_call(relay.reshape(const_1675.astype('float32'), []), relay.reshape(const_1676.astype('float32'), [1, 1, 16]), ), 2)
output = relay.Tuple([uop_1672,call_1674,const_1675,const_1676,])
output2 = relay.Tuple([uop_1672,call_1677,const_1675,const_1676,])
func_1692 = relay.Function([], output)
mod['func_1692'] = func_1692
mod = relay.transform.InferType()(mod)
output = func_1692()
func_1693 = relay.Function([], output)
mutated_mod['func_1693'] = func_1693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_1763 = relay.TupleGetItem(func_1692_call(), 0)
call_1764 = relay.TupleGetItem(func_1693_call(), 0)
output = call_1763
output2 = call_1764
func_1771 = relay.Function([], output)
mod['func_1771'] = func_1771
mod = relay.transform.InferType()(mod)
output = func_1771()
func_1772 = relay.Function([], output)
mutated_mod['func_1772'] = func_1772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_1878 = relay.TupleGetItem(func_1692_call(), 0)
call_1879 = relay.TupleGetItem(func_1693_call(), 0)
output = relay.Tuple([call_1878,])
output2 = relay.Tuple([call_1879,])
func_1891 = relay.Function([], output)
mod['func_1891'] = func_1891
mod = relay.transform.InferType()(mod)
output = func_1891()
func_1892 = relay.Function([], output)
mutated_mod['func_1892'] = func_1892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1771_call = mod.get_global_var('func_1771')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_1949 = func_1771_call()
call_1950 = func_1771_call()
var_1952 = relay.var("var_1952", dtype = "float64", shape = (9, 12, 5))#candidate|1952|(9, 12, 5)|var|float64
bop_1953 = relay.mod(call_1949.astype('float64'), var_1952.astype('float64')) # shape=(9, 12, 5)
bop_1956 = relay.mod(call_1950.astype('float64'), var_1952.astype('float64')) # shape=(9, 12, 5)
func_369_call = mod.get_global_var('func_369')
func_372_call = mutated_mod.get_global_var('func_372')
const_1960 = relay.const(8.180209, dtype = "float32")#candidate|1960|()|const|float32
var_1961 = relay.var("var_1961", dtype = "float32", shape = (16,))#candidate|1961|(16,)|var|float32
call_1959 = relay.TupleGetItem(func_369_call(relay.reshape(const_1960.astype('float32'), []), relay.reshape(var_1961.astype('float32'), [1, 1, 16]), ), 1)
call_1962 = relay.TupleGetItem(func_372_call(relay.reshape(const_1960.astype('float32'), []), relay.reshape(var_1961.astype('float32'), [1, 1, 16]), ), 1)
output = relay.Tuple([bop_1953,call_1959,const_1960,var_1961,])
output2 = relay.Tuple([bop_1956,call_1962,const_1960,var_1961,])
func_1984 = relay.Function([var_1952,var_1961,], output)
mod['func_1984'] = func_1984
mod = relay.transform.InferType()(mod)
var_1985 = relay.var("var_1985", dtype = "float64", shape = (9, 12, 5))#candidate|1985|(9, 12, 5)|var|float64
var_1986 = relay.var("var_1986", dtype = "float32", shape = (16,))#candidate|1986|(16,)|var|float32
output = func_1984(var_1985,var_1986,)
func_1987 = relay.Function([var_1985,var_1986,], output)
mutated_mod['func_1987'] = func_1987
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1992 = relay.var("var_1992", dtype = "float32", shape = (5, 6, 10))#candidate|1992|(5, 6, 10)|var|float32
uop_1993 = relay.cosh(var_1992.astype('float32')) # shape=(5, 6, 10)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_1995 = relay.TupleGetItem(func_1692_call(), 3)
call_1996 = relay.TupleGetItem(func_1693_call(), 3)
output = relay.Tuple([uop_1993,call_1995,])
output2 = relay.Tuple([uop_1993,call_1996,])
func_2000 = relay.Function([var_1992,], output)
mod['func_2000'] = func_2000
mod = relay.transform.InferType()(mod)
mutated_mod['func_2000'] = func_2000
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2001 = relay.var("var_2001", dtype = "float32", shape = (5, 6, 10))#candidate|2001|(5, 6, 10)|var|float32
func_2000_call = mutated_mod.get_global_var('func_2000')
call_2002 = func_2000_call(var_2001)
output = call_2002
func_2003 = relay.Function([var_2001], output)
mutated_mod['func_2003'] = func_2003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1771_call = mod.get_global_var('func_1771')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_2054 = func_1771_call()
call_2055 = func_1771_call()
var_2059 = relay.var("var_2059", dtype = "float64", shape = (9, 12, 3))#candidate|2059|(9, 12, 3)|var|float64
bop_2060 = relay.left_shift(call_2054.astype('int32'), var_2059.astype('int32')) # shape=(9, 12, 3)
bop_2063 = relay.left_shift(call_2055.astype('int32'), var_2059.astype('int32')) # shape=(9, 12, 3)
bop_2068 = relay.bitwise_or(call_2054.astype('int32'), bop_2060.astype('int32')) # shape=(9, 12, 3)
bop_2071 = relay.bitwise_or(call_2055.astype('int32'), bop_2063.astype('int32')) # shape=(9, 12, 3)
output = relay.Tuple([bop_2068,])
output2 = relay.Tuple([bop_2071,])
func_2080 = relay.Function([var_2059,], output)
mod['func_2080'] = func_2080
mod = relay.transform.InferType()(mod)
var_2081 = relay.var("var_2081", dtype = "float64", shape = (9, 12, 3))#candidate|2081|(9, 12, 3)|var|float64
output = func_2080(var_2081)
func_2082 = relay.Function([var_2081], output)
mutated_mod['func_2082'] = func_2082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_2165 = relay.TupleGetItem(func_1891_call(), 0)
call_2166 = relay.TupleGetItem(func_1892_call(), 0)
output = relay.Tuple([call_2165,])
output2 = relay.Tuple([call_2166,])
func_2172 = relay.Function([], output)
mod['func_2172'] = func_2172
mod = relay.transform.InferType()(mod)
output = func_2172()
func_2173 = relay.Function([], output)
mutated_mod['func_2173'] = func_2173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_2254 = relay.TupleGetItem(func_1692_call(), 3)
call_2255 = relay.TupleGetItem(func_1693_call(), 3)
output = relay.Tuple([call_2254,])
output2 = relay.Tuple([call_2255,])
func_2260 = relay.Function([], output)
mod['func_2260'] = func_2260
mod = relay.transform.InferType()(mod)
mutated_mod['func_2260'] = func_2260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mutated_mod.get_global_var('func_2260')
call_2261 = func_2260_call()
output = call_2261
func_2262 = relay.Function([], output)
mutated_mod['func_2262'] = func_2262
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2299 = relay.var("var_2299", dtype = "float64", shape = (4, 12, 1))#candidate|2299|(4, 12, 1)|var|float64
uop_2300 = relay.asin(var_2299.astype('float64')) # shape=(4, 12, 1)
var_2320 = relay.var("var_2320", dtype = "float64", shape = (4, 12, 15))#candidate|2320|(4, 12, 15)|var|float64
bop_2321 = relay.power(var_2299.astype('float32'), var_2320.astype('float32')) # shape=(4, 12, 15)
uop_2337 = relay.cos(bop_2321.astype('float64')) # shape=(4, 12, 15)
uop_2339 = relay.acosh(uop_2337.astype('float64')) # shape=(4, 12, 15)
output = relay.Tuple([uop_2300,uop_2339,])
output2 = relay.Tuple([uop_2300,uop_2339,])
func_2344 = relay.Function([var_2299,var_2320,], output)
mod['func_2344'] = func_2344
mod = relay.transform.InferType()(mod)
var_2345 = relay.var("var_2345", dtype = "float64", shape = (4, 12, 1))#candidate|2345|(4, 12, 1)|var|float64
var_2346 = relay.var("var_2346", dtype = "float64", shape = (4, 12, 15))#candidate|2346|(4, 12, 15)|var|float64
output = func_2344(var_2345,var_2346,)
func_2347 = relay.Function([var_2345,var_2346,], output)
mutated_mod['func_2347'] = func_2347
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2361 = relay.var("var_2361", dtype = "int32", shape = ())#candidate|2361|()|var|int32
const_2362 = relay.const([[[-4],[5],[-9],[10],[-6],[6],[-10],[6],[5],[6],[-7],[10],[-3]],[[6],[-2],[-9],[9],[10],[5],[-3],[-2],[-10],[6],[-8],[7],[3]],[[-1],[5],[-2],[3],[5],[4],[5],[2],[-5],[2],[-4],[4],[6]],[[2],[-9],[9],[-10],[3],[5],[-7],[5],[-2],[5],[-10],[-9],[-10]],[[5],[-4],[5],[6],[3],[-4],[-10],[-4],[-3],[5],[10],[10],[-1]],[[6],[3],[4],[9],[8],[-6],[-7],[-10],[1],[-10],[-6],[3],[10]],[[-9],[9],[-1],[2],[10],[-1],[-4],[4],[-5],[-6],[-4],[6],[-1]],[[4],[2],[-7],[2],[-2],[2],[6],[-10],[2],[10],[-3],[-7],[-2]],[[7],[4],[10],[1],[-1],[4],[-6],[-6],[-2],[2],[-3],[-7],[10]]], dtype = "int32")#candidate|2362|(9, 13, 1)|const|int32
bop_2363 = relay.right_shift(var_2361.astype('int32'), const_2362.astype('int32')) # shape=(9, 13, 1)
output = bop_2363
output2 = bop_2363
func_2374 = relay.Function([var_2361,], output)
mod['func_2374'] = func_2374
mod = relay.transform.InferType()(mod)
mutated_mod['func_2374'] = func_2374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2375 = relay.var("var_2375", dtype = "int32", shape = ())#candidate|2375|()|var|int32
func_2374_call = mutated_mod.get_global_var('func_2374')
call_2376 = func_2374_call(var_2375)
output = call_2376
func_2377 = relay.Function([var_2375], output)
mutated_mod['func_2377'] = func_2377
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2399 = relay.var("var_2399", dtype = "int8", shape = (15, 13, 4))#candidate|2399|(15, 13, 4)|var|int8
var_2400 = relay.var("var_2400", dtype = "int8", shape = (15, 13, 4))#candidate|2400|(15, 13, 4)|var|int8
bop_2401 = relay.less(var_2399.astype('bool'), relay.reshape(var_2400.astype('bool'), relay.shape_of(var_2399))) # shape=(15, 13, 4)
var_2416 = relay.var("var_2416", dtype = "int8", shape = (15, 13, 4))#candidate|2416|(15, 13, 4)|var|int8
bop_2417 = relay.minimum(var_2400.astype('uint64'), relay.reshape(var_2416.astype('uint64'), relay.shape_of(var_2400))) # shape=(15, 13, 4)
uop_2420 = relay.cos(var_2416.astype('float32')) # shape=(15, 13, 4)
output = relay.Tuple([bop_2401,bop_2417,uop_2420,])
output2 = relay.Tuple([bop_2401,bop_2417,uop_2420,])
func_2436 = relay.Function([var_2399,var_2400,var_2416,], output)
mod['func_2436'] = func_2436
mod = relay.transform.InferType()(mod)
var_2437 = relay.var("var_2437", dtype = "int8", shape = (15, 13, 4))#candidate|2437|(15, 13, 4)|var|int8
var_2438 = relay.var("var_2438", dtype = "int8", shape = (15, 13, 4))#candidate|2438|(15, 13, 4)|var|int8
var_2439 = relay.var("var_2439", dtype = "int8", shape = (15, 13, 4))#candidate|2439|(15, 13, 4)|var|int8
output = func_2436(var_2437,var_2438,var_2439,)
func_2440 = relay.Function([var_2437,var_2438,var_2439,], output)
mutated_mod['func_2440'] = func_2440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1771_call = mod.get_global_var('func_1771')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_2451 = func_1771_call()
call_2452 = func_1771_call()
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_2454 = relay.TupleGetItem(func_1692_call(), 2)
call_2455 = relay.TupleGetItem(func_1693_call(), 2)
uop_2463 = relay.exp(call_2451.astype('float32')) # shape=(9, 12, 1)
uop_2465 = relay.exp(call_2452.astype('float32')) # shape=(9, 12, 1)
output = relay.Tuple([call_2454,uop_2463,])
output2 = relay.Tuple([call_2455,uop_2465,])
func_2472 = relay.Function([], output)
mod['func_2472'] = func_2472
mod = relay.transform.InferType()(mod)
output = func_2472()
func_2473 = relay.Function([], output)
mutated_mod['func_2473'] = func_2473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2472_call = mod.get_global_var('func_2472')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_2497 = relay.TupleGetItem(func_2472_call(), 1)
call_2498 = relay.TupleGetItem(func_2473_call(), 1)
output = call_2497
output2 = call_2498
func_2499 = relay.Function([], output)
mod['func_2499'] = func_2499
mod = relay.transform.InferType()(mod)
output = func_2499()
func_2500 = relay.Function([], output)
mutated_mod['func_2500'] = func_2500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_2511 = func_2499_call()
call_2512 = func_2499_call()
func_2436_call = mod.get_global_var('func_2436')
func_2440_call = mutated_mod.get_global_var('func_2440')
const_2514 = relay.const([[9,3,8,4,-6,-8,-4,10,-4,-9,3,7,-8,10,4,-1,-3,-1,-2,2,7,-10,9,-8,8,-5,9,3,-10,3,-5,8,-1,-1,-3,-10,3,5,9,8,-1,8,-4,5,-4,-7,-5,8,-4,-8,4,-1,-7,2,10,-5,2,8,2,9,6,-6,-2,8,7,-7,5,9,-2,9,-8,2,-8,5,8,8,3,4,2,3,9,8,6,7,8,-2,10,8,4,10,9,-5,-3,8,-10,-3,-9,-4,-10,-4,5,-7,-8,5,-8,6,-2,-10,10,10,-8,-1,-6,1,6,-4,-1,-7,6,5,-6,3,-1,-3,-2,-5,6,7,-2,7,6,-8,4,8,-9,6,-3,3,4,7,9,-6,9,-4,-6,7,-2,-10,2,6,10,-7,5,-9,8,-6,-9,9,-8,6,-3,7,-10,4,5,-3,4,-10,-2,7,-6,-4,-7,-10,7,10,-1,-7,-4,-2,1,-3,-7,-5,1,-8,4,1,-6,-8,-9,5,5,-2,5,7,-1,-2,-3,-9,8,3,-9,7,7,10,-4,-7,-1,8,-3,1,-5,-4,1,-5,1,4,2,7,7,-5,-6,-9,-1,10,-10,-10,7,3,7,6,-6,8,-2,-5,-4,-9,3,5,3,-10,10,9,-3,-3,10,8,4,4,-3,-4,-1,7,-10,-10,2,7,-1,7,-1,-6,-4,7,-10,-3,-1,-10,-1,-6,1,-4,-5,5,7,10,6,9,10,-7,8,-5,-10,-1,4,-10,3,-10,-4,4,8,-9,10,4,5,-2,5,4,-4,4,2,5,-9,6,1,-5,4,3,2,-3,3,10,5,-1,8,-7,3,-8,10,-4,-3,-1,-2,10,4,-9,-1,4,10,4,-5,10,6,8,9,-6,2,-9,2,6,-5,4,3,-3,-5,3,-10,8,1,4,2,4,7,-8,-5,8,1,-5,10,-9,4,7,-7,4,2,7,7,-8,7,5,10,1,3,-6,-5,-10,-9,5,-3,-3,6,-9,-3,7,-10,-1,4,-10,9,4,10,-5,2,-4,-10,9,9,8,2,-4,-8,3,-1,2,8,4,-1,-9,-10,7,-2,-3,-4,-4,6,1,7,7,8,7,-7,-5,1,-1,-7,-8,-5,-9,-4,9,3,8,-5,-7,6,10,7,10,-1,9,-9,6,-10,7,8,-5,-8,-2,-10,8,2,-9,-7,-5,10,-6,-10,5,7,-5,-9,-7,-5,-10,7,1,9,-8,-9,-5,-8,-7,3,-10,5,-7,-6,-1,-3,-8,-10,2,6,-6,-5,-3,-3,-1,6,9,7,-6,-8,7,-8,4,1,9,-5,4,7,-3,2,9,7,9,-1,8,4,3,-10,1,-4,-1,-5,-1,2,5,7,-2,-9,10,-8,1,4,5,2,5,6,7,1,-4,-1,9,-2,-4,-3,-2,3,-2,-9,2,3,-9,3,10,3,1,2,2,10,-6,-10,-4,6,-9,3,6,1,4,-1,-10,-8,-6,10,6,-4,2,5,-7,2,-5,9,8,9,6,6,-4,-8,7,-10,7,-7,8,-5,-2,2,1,-9,1,-10,-7,4,3,6,7,2,2,5,3,6,6,-3,9,-5,-1,7,5,1,-3,-5,3,-6,-9,6,2,7,7,-6,-5,9,10,-6,-9,-1,4,-3,-5,3,-4,6,-8,-6,5,3,5,-6,10,-9,8,1,8,-10,-5,-7,-1,-4,5,8,-2,-10,5,-1,5,-3,-10,7,-10,-2,-2,-3,3,-6,9,-8,6,-7,1,5,-8,3,5,-7,-8,10,-10,-5,-2,1,6,4,7,-3,1,-8,-8,-6,-8,-8,4,8,-10,-4,5,-6,7,1,1,-4,-3,1,1,4,2,8,9,7,1,4,1,7,7,-1,3,3,8,-7,3,10,3,-1,-6,-2,4,-2,-5,10,-6,-2,-8,5,9,5,-3,-9,-5,-1,-1,-5,-10,-7,-6,8,-9,1,7,5,9,-10,-7,1,9,2,-8,2,-5,-4,7,-3,4,6,-1,7,-1,2,-6,-9,-8,3,-9,5,-6,-3,3,-1,-9,6,8,-7,2]], dtype = "int8")#candidate|2514|(1, 780)|const|int8
call_2513 = relay.TupleGetItem(func_2436_call(relay.reshape(const_2514.astype('int8'), [15, 13, 4]), relay.reshape(const_2514.astype('int8'), [15, 13, 4]), relay.reshape(const_2514.astype('int8'), [15, 13, 4]), ), 1)
call_2515 = relay.TupleGetItem(func_2440_call(relay.reshape(const_2514.astype('int8'), [15, 13, 4]), relay.reshape(const_2514.astype('int8'), [15, 13, 4]), relay.reshape(const_2514.astype('int8'), [15, 13, 4]), ), 1)
var_2520 = relay.var("var_2520", dtype = "int8", shape = (10, 780))#candidate|2520|(10, 780)|var|int8
bop_2521 = relay.greater_equal(const_2514.astype('bool'), var_2520.astype('bool')) # shape=(10, 780)
bop_2529 = relay.bitwise_and(call_2511.astype('uint8'), const_2514.astype('uint8')) # shape=(9, 12, 780)
bop_2532 = relay.bitwise_and(call_2512.astype('uint8'), const_2514.astype('uint8')) # shape=(9, 12, 780)
output = relay.Tuple([call_2513,bop_2521,bop_2529,])
output2 = relay.Tuple([call_2515,bop_2521,bop_2532,])
func_2538 = relay.Function([var_2520,], output)
mod['func_2538'] = func_2538
mod = relay.transform.InferType()(mod)
var_2539 = relay.var("var_2539", dtype = "int8", shape = (10, 780))#candidate|2539|(10, 780)|var|int8
output = func_2538(var_2539)
func_2540 = relay.Function([var_2539], output)
mutated_mod['func_2540'] = func_2540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mod.get_global_var('func_2260')
func_2262_call = mutated_mod.get_global_var('func_2262')
call_2551 = relay.TupleGetItem(func_2260_call(), 0)
call_2552 = relay.TupleGetItem(func_2262_call(), 0)
output = relay.Tuple([call_2551,])
output2 = relay.Tuple([call_2552,])
func_2553 = relay.Function([], output)
mod['func_2553'] = func_2553
mod = relay.transform.InferType()(mod)
mutated_mod['func_2553'] = func_2553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2553_call = mutated_mod.get_global_var('func_2553')
call_2554 = func_2553_call()
output = call_2554
func_2555 = relay.Function([], output)
mutated_mod['func_2555'] = func_2555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_2601 = relay.TupleGetItem(func_1692_call(), 3)
call_2602 = relay.TupleGetItem(func_1693_call(), 3)
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
var_2618 = relay.var("var_2618", dtype = "float32", shape = (27, 2))#candidate|2618|(27, 2)|var|float32
call_2617 = relay.TupleGetItem(func_813_call(relay.reshape(var_2618.astype('float32'), [6, 3, 3])), 0)
call_2619 = relay.TupleGetItem(func_816_call(relay.reshape(var_2618.astype('float32'), [6, 3, 3])), 0)
uop_2625 = relay.tan(var_2618.astype('float32')) # shape=(27, 2)
output = relay.Tuple([call_2601,call_2617,uop_2625,])
output2 = relay.Tuple([call_2602,call_2619,uop_2625,])
func_2631 = relay.Function([var_2618,], output)
mod['func_2631'] = func_2631
mod = relay.transform.InferType()(mod)
var_2632 = relay.var("var_2632", dtype = "float32", shape = (27, 2))#candidate|2632|(27, 2)|var|float32
output = func_2631(var_2632)
func_2633 = relay.Function([var_2632], output)
mutated_mod['func_2633'] = func_2633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1771_call = mod.get_global_var('func_1771')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_2737 = func_1771_call()
call_2738 = func_1771_call()
func_50_call = mod.get_global_var('func_50')
func_53_call = mutated_mod.get_global_var('func_53')
var_2740 = relay.var("var_2740", dtype = "float32", shape = (360,))#candidate|2740|(360,)|var|float32
call_2739 = func_50_call(relay.reshape(var_2740.astype('float32'), [3, 10, 12]))
call_2741 = func_50_call(relay.reshape(var_2740.astype('float32'), [3, 10, 12]))
func_2000_call = mod.get_global_var('func_2000')
func_2003_call = mutated_mod.get_global_var('func_2003')
var_2756 = relay.var("var_2756", dtype = "float32", shape = (300,))#candidate|2756|(300,)|var|float32
call_2755 = relay.TupleGetItem(func_2000_call(relay.reshape(var_2756.astype('float32'), [5, 6, 10])), 0)
call_2757 = relay.TupleGetItem(func_2003_call(relay.reshape(var_2756.astype('float32'), [5, 6, 10])), 0)
func_2374_call = mod.get_global_var('func_2374')
func_2377_call = mutated_mod.get_global_var('func_2377')
var_2760 = relay.var("var_2760", dtype = "int32", shape = ())#candidate|2760|()|var|int32
call_2759 = func_2374_call(relay.reshape(var_2760.astype('int32'), []))
call_2761 = func_2374_call(relay.reshape(var_2760.astype('int32'), []))
output = relay.Tuple([call_2737,call_2739,var_2740,call_2755,var_2756,call_2759,var_2760,])
output2 = relay.Tuple([call_2738,call_2741,var_2740,call_2757,var_2756,call_2761,var_2760,])
func_2770 = relay.Function([var_2740,var_2756,var_2760,], output)
mod['func_2770'] = func_2770
mod = relay.transform.InferType()(mod)
mutated_mod['func_2770'] = func_2770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2770_call = mutated_mod.get_global_var('func_2770')
var_2772 = relay.var("var_2772", dtype = "float32", shape = (360,))#candidate|2772|(360,)|var|float32
var_2773 = relay.var("var_2773", dtype = "float32", shape = (300,))#candidate|2773|(300,)|var|float32
var_2774 = relay.var("var_2774", dtype = "int32", shape = ())#candidate|2774|()|var|int32
call_2771 = func_2770_call(var_2772,var_2773,var_2774,)
output = call_2771
func_2775 = relay.Function([var_2772,var_2773,var_2774,], output)
mutated_mod['func_2775'] = func_2775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_2782 = relay.TupleGetItem(func_1692_call(), 1)
call_2783 = relay.TupleGetItem(func_1693_call(), 1)
func_1771_call = mod.get_global_var('func_1771')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_2790 = func_1771_call()
call_2791 = func_1771_call()
output = relay.Tuple([call_2782,call_2790,])
output2 = relay.Tuple([call_2783,call_2791,])
func_2804 = relay.Function([], output)
mod['func_2804'] = func_2804
mod = relay.transform.InferType()(mod)
mutated_mod['func_2804'] = func_2804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2804_call = mutated_mod.get_global_var('func_2804')
call_2805 = func_2804_call()
output = call_2805
func_2806 = relay.Function([], output)
mutated_mod['func_2806'] = func_2806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2553_call = mod.get_global_var('func_2553')
func_2555_call = mutated_mod.get_global_var('func_2555')
call_2828 = relay.TupleGetItem(func_2553_call(), 0)
call_2829 = relay.TupleGetItem(func_2555_call(), 0)
func_1984_call = mod.get_global_var('func_1984')
func_1987_call = mutated_mod.get_global_var('func_1987')
var_2831 = relay.var("var_2831", dtype = "float64", shape = (540,))#candidate|2831|(540,)|var|float64
call_2830 = relay.TupleGetItem(func_1984_call(relay.reshape(var_2831.astype('float64'), [9, 12, 5]), relay.reshape(call_2828.astype('float32'), [16,]), ), 1)
call_2832 = relay.TupleGetItem(func_1987_call(relay.reshape(var_2831.astype('float64'), [9, 12, 5]), relay.reshape(call_2828.astype('float32'), [16,]), ), 1)
func_2631_call = mod.get_global_var('func_2631')
func_2633_call = mutated_mod.get_global_var('func_2633')
const_2861 = relay.const([4.674175,0.345740,2.837000,-8.411957,-4.449473,6.431918,-4.040457,-8.262859,6.641789,6.496025,2.774786,-8.231990,-4.782507,-3.396838,-1.649361,-1.234566,2.535410,6.912937,-8.335509,-1.350908,-5.388265,-0.500026,-3.955265,0.787166,8.348821,-0.441035,2.805798,-9.061368,-1.195629,0.066455,1.884268,6.677161,-6.135299,1.238854,-8.373043,7.090830,6.377698,6.342151,-5.661665,6.737633,4.114580,-7.405538,2.492150,5.619062,7.810884,-2.044659,-6.130179,-2.629716,-2.538247,8.057191,5.294502,-2.986955,-6.632554,-0.876544], dtype = "float32")#candidate|2861|(54,)|const|float32
call_2860 = relay.TupleGetItem(func_2631_call(relay.reshape(const_2861.astype('float32'), [27, 2])), 2)
call_2862 = relay.TupleGetItem(func_2633_call(relay.reshape(const_2861.astype('float32'), [27, 2])), 2)
output = relay.Tuple([call_2828,call_2830,var_2831,call_2860,const_2861,])
output2 = relay.Tuple([call_2829,call_2832,var_2831,call_2862,const_2861,])
func_2868 = relay.Function([var_2831,], output)
mod['func_2868'] = func_2868
mod = relay.transform.InferType()(mod)
var_2869 = relay.var("var_2869", dtype = "float64", shape = (540,))#candidate|2869|(540,)|var|float64
output = func_2868(var_2869)
func_2870 = relay.Function([var_2869], output)
mutated_mod['func_2870'] = func_2870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mod.get_global_var('func_2260')
func_2262_call = mutated_mod.get_global_var('func_2262')
call_2893 = relay.TupleGetItem(func_2260_call(), 0)
call_2894 = relay.TupleGetItem(func_2262_call(), 0)
output = call_2893
output2 = call_2894
func_2895 = relay.Function([], output)
mod['func_2895'] = func_2895
mod = relay.transform.InferType()(mod)
mutated_mod['func_2895'] = func_2895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2895_call = mutated_mod.get_global_var('func_2895')
call_2896 = func_2895_call()
output = call_2896
func_2897 = relay.Function([], output)
mutated_mod['func_2897'] = func_2897
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2962 = relay.var("var_2962", dtype = "float64", shape = (16, 10, 6))#candidate|2962|(16, 10, 6)|var|float64
uop_2963 = relay.atan(var_2962.astype('float64')) # shape=(16, 10, 6)
var_2968 = relay.var("var_2968", dtype = "float64", shape = (16, 10, 6))#candidate|2968|(16, 10, 6)|var|float64
bop_2969 = relay.subtract(uop_2963.astype('uint64'), relay.reshape(var_2968.astype('uint64'), relay.shape_of(uop_2963))) # shape=(16, 10, 6)
output = bop_2969
output2 = bop_2969
func_2984 = relay.Function([var_2962,var_2968,], output)
mod['func_2984'] = func_2984
mod = relay.transform.InferType()(mod)
mutated_mod['func_2984'] = func_2984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2984_call = mutated_mod.get_global_var('func_2984')
var_2986 = relay.var("var_2986", dtype = "float64", shape = (16, 10, 6))#candidate|2986|(16, 10, 6)|var|float64
var_2987 = relay.var("var_2987", dtype = "float64", shape = (16, 10, 6))#candidate|2987|(16, 10, 6)|var|float64
call_2985 = func_2984_call(var_2986,var_2987,)
output = call_2985
func_2988 = relay.Function([var_2986,var_2987,], output)
mutated_mod['func_2988'] = func_2988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2895_call = mod.get_global_var('func_2895')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_3040 = func_2895_call()
call_3041 = func_2895_call()
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_3077 = relay.TupleGetItem(func_2172_call(), 0)
call_3078 = relay.TupleGetItem(func_2173_call(), 0)
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_3085 = relay.TupleGetItem(func_2172_call(), 0)
call_3086 = relay.TupleGetItem(func_2173_call(), 0)
bop_3093 = relay.mod(call_3077.astype('float64'), relay.reshape(call_3085.astype('float64'), relay.shape_of(call_3077))) # shape=(9, 12, 1)
bop_3096 = relay.mod(call_3078.astype('float64'), relay.reshape(call_3086.astype('float64'), relay.shape_of(call_3078))) # shape=(9, 12, 1)
var_3099 = relay.var("var_3099", dtype = "float64", shape = (9, 12, 6))#candidate|3099|(9, 12, 6)|var|float64
bop_3100 = relay.add(call_3077.astype('uint8'), var_3099.astype('uint8')) # shape=(9, 12, 6)
bop_3103 = relay.add(call_3078.astype('uint8'), var_3099.astype('uint8')) # shape=(9, 12, 6)
output = relay.Tuple([call_3040,bop_3093,bop_3100,])
output2 = relay.Tuple([call_3041,bop_3096,bop_3103,])
func_3109 = relay.Function([var_3099,], output)
mod['func_3109'] = func_3109
mod = relay.transform.InferType()(mod)
var_3110 = relay.var("var_3110", dtype = "float64", shape = (9, 12, 6))#candidate|3110|(9, 12, 6)|var|float64
output = func_3109(var_3110)
func_3111 = relay.Function([var_3110], output)
mutated_mod['func_3111'] = func_3111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_3137 = func_2499_call()
call_3138 = func_2499_call()
func_2080_call = mod.get_global_var('func_2080')
func_2082_call = mutated_mod.get_global_var('func_2082')
var_3140 = relay.var("var_3140", dtype = "float64", shape = (324,))#candidate|3140|(324,)|var|float64
call_3139 = relay.TupleGetItem(func_2080_call(relay.reshape(var_3140.astype('float64'), [9, 12, 3])), 0)
call_3141 = relay.TupleGetItem(func_2082_call(relay.reshape(var_3140.astype('float64'), [9, 12, 3])), 0)
output = relay.Tuple([call_3137,call_3139,var_3140,])
output2 = relay.Tuple([call_3138,call_3141,var_3140,])
func_3142 = relay.Function([var_3140,], output)
mod['func_3142'] = func_3142
mod = relay.transform.InferType()(mod)
var_3143 = relay.var("var_3143", dtype = "float64", shape = (324,))#candidate|3143|(324,)|var|float64
output = func_3142(var_3143)
func_3144 = relay.Function([var_3143], output)
mutated_mod['func_3144'] = func_3144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2553_call = mod.get_global_var('func_2553')
func_2555_call = mutated_mod.get_global_var('func_2555')
call_3187 = relay.TupleGetItem(func_2553_call(), 0)
call_3188 = relay.TupleGetItem(func_2555_call(), 0)
output = relay.Tuple([call_3187,])
output2 = relay.Tuple([call_3188,])
func_3191 = relay.Function([], output)
mod['func_3191'] = func_3191
mod = relay.transform.InferType()(mod)
output = func_3191()
func_3192 = relay.Function([], output)
mutated_mod['func_3192'] = func_3192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2472_call = mod.get_global_var('func_2472')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_3252 = relay.TupleGetItem(func_2472_call(), 0)
call_3253 = relay.TupleGetItem(func_2473_call(), 0)
func_2868_call = mod.get_global_var('func_2868')
func_2870_call = mutated_mod.get_global_var('func_2870')
var_3264 = relay.var("var_3264", dtype = "float64", shape = (540,))#candidate|3264|(540,)|var|float64
call_3263 = relay.TupleGetItem(func_2868_call(relay.reshape(var_3264.astype('float64'), [540,])), 2)
call_3265 = relay.TupleGetItem(func_2870_call(relay.reshape(var_3264.astype('float64'), [540,])), 2)
output = relay.Tuple([call_3252,call_3263,var_3264,])
output2 = relay.Tuple([call_3253,call_3265,var_3264,])
func_3266 = relay.Function([var_3264,], output)
mod['func_3266'] = func_3266
mod = relay.transform.InferType()(mod)
mutated_mod['func_3266'] = func_3266
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3267 = relay.var("var_3267", dtype = "float64", shape = (540,))#candidate|3267|(540,)|var|float64
func_3266_call = mutated_mod.get_global_var('func_3266')
call_3268 = func_3266_call(var_3267)
output = call_3268
func_3269 = relay.Function([var_3267], output)
mutated_mod['func_3269'] = func_3269
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3339 = relay.const([[[-5.414969],[5.685738],[1.190238]],[[-3.562642],[-4.866050],[5.456357]],[[2.615488],[1.225109],[5.020332]],[[-8.908994],[-7.383503],[-7.756957]],[[-5.271483],[-0.647494],[-0.532515]],[[9.860625],[1.916607],[-4.042258]],[[-7.324158],[-7.456556],[0.683190]],[[-4.752982],[-9.928438],[-9.342016]],[[8.698392],[4.726416],[-8.838326]],[[-1.429086],[5.327952],[-8.532984]],[[-2.519390],[3.967751],[-8.850049]],[[-7.857117],[-9.329035],[3.773199]]], dtype = "float32")#candidate|3339|(12, 3, 1)|const|float32
uop_3340 = relay.asinh(const_3339.astype('float32')) # shape=(12, 3, 1)
uop_3343 = relay.cosh(uop_3340.astype('float32')) # shape=(12, 3, 1)
output = uop_3343
output2 = uop_3343
func_3348 = relay.Function([], output)
mod['func_3348'] = func_3348
mod = relay.transform.InferType()(mod)
mutated_mod['func_3348'] = func_3348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3348_call = mutated_mod.get_global_var('func_3348')
call_3349 = func_3348_call()
output = call_3349
func_3350 = relay.Function([], output)
mutated_mod['func_3350'] = func_3350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3348_call = mod.get_global_var('func_3348')
func_3350_call = mutated_mod.get_global_var('func_3350')
call_3378 = func_3348_call()
call_3379 = func_3348_call()
uop_3383 = relay.sqrt(call_3378.astype('float64')) # shape=(12, 3, 1)
uop_3385 = relay.sqrt(call_3379.astype('float64')) # shape=(12, 3, 1)
func_3191_call = mod.get_global_var('func_3191')
func_3192_call = mutated_mod.get_global_var('func_3192')
call_3386 = relay.TupleGetItem(func_3191_call(), 0)
call_3387 = relay.TupleGetItem(func_3192_call(), 0)
func_2895_call = mod.get_global_var('func_2895')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_3389 = func_2895_call()
call_3390 = func_2895_call()
bop_3410 = relay.floor_mod(uop_3383.astype('float32'), relay.reshape(call_3378.astype('float32'), relay.shape_of(uop_3383))) # shape=(12, 3, 1)
bop_3413 = relay.floor_mod(uop_3385.astype('float32'), relay.reshape(call_3379.astype('float32'), relay.shape_of(uop_3385))) # shape=(12, 3, 1)
func_3142_call = mod.get_global_var('func_3142')
func_3144_call = mutated_mod.get_global_var('func_3144')
var_3417 = relay.var("var_3417", dtype = "float64", shape = (9, 36))#candidate|3417|(9, 36)|var|float64
call_3416 = relay.TupleGetItem(func_3142_call(relay.reshape(var_3417.astype('float64'), [324,])), 0)
call_3418 = relay.TupleGetItem(func_3144_call(relay.reshape(var_3417.astype('float64'), [324,])), 0)
func_935_call = mod.get_global_var('func_935')
func_939_call = mutated_mod.get_global_var('func_939')
const_3420 = relay.const([3.045822,-6.526264,-4.524905,-5.462821,-0.299563,-4.602978,-4.185867,4.432400,-6.317828,8.973962,-3.921550,6.734656,0.134032,3.748265,7.284919,-3.255770,3.740628,9.638967,1.150864,-1.304406,-6.282804,9.460624,5.781151,4.278587,7.819309,-3.145152,-1.416725,-4.363316,8.990712,5.732234,-9.442869,2.780447,-4.759461,-9.263483,-0.570394,1.225007,2.414066,9.400550,-8.253081,1.631833,-1.102966,8.585361,3.935578,-3.472884,5.616381,-4.861710,6.871301,-3.128386,-0.132089,1.404133,0.688869,3.782884,-4.819365,4.539530,-5.334903,-5.339629,-4.680624,4.074127,5.383097,-8.893104,0.709350,4.310336,-3.207957,7.728291,-2.030403,9.121951,4.243587,-2.175292,3.384423,-1.911240,-0.358250,-4.515499,6.959018,6.566800,-2.356988,0.469821,-1.885353,-0.053120,-0.325042,7.849413,9.448023,-9.887588,-4.281236,-7.610298,-4.881879,9.280323,2.529342,3.651366,3.464005,6.259980,-4.249158,-1.652385,9.214819,7.756356,-4.208697,-8.763208,9.591957,-6.235459,-6.222685,-0.658225,-6.201820,3.383686,5.356777,-3.793167,8.251098,-5.384152,-3.088972,-1.326622,-3.200293,-5.900511,2.452231,-7.113187,2.800233,-4.161480,8.859285,0.565384,-0.071528,6.230494,1.617805,-0.670223,0.972415,8.403587,3.458762,-1.304800,1.529925,-0.339250,2.951507,-5.565319,-7.953948,-9.352652,9.817358,4.016991,4.980802,2.460456,-7.295495,2.613503,5.253644,8.494468,8.030770,-9.790546,-7.634480,7.038824,8.941892,8.194628,-4.399438,5.305195,9.634805,2.247521,2.083208,2.764673,-2.118673,1.116857,5.273640,3.731480,-8.878892,-2.098371,-9.711940,2.374863,6.358902,4.523750,-3.107135,1.619540,0.412382,-6.110993,9.468647,-7.732447,4.681184,3.436243,4.140580,3.667696,-9.762260,-1.988402,6.494805,-3.970355,-5.957385,-9.489784,-1.758575,-0.463247,-1.434006,-7.143921,4.076317,3.839598,7.476980,8.279486,9.444057,-4.347285,-0.544757,0.024351,-2.061770,-4.038198,7.958011,-3.448614,-0.208576,-3.466938,5.378226,6.618305,9.447848,3.924257,1.030611,4.467972,9.461406,3.432961,7.665713,3.117012,-9.989960,-7.595456,-5.840595,-0.559216,-7.492319,4.525949,9.293456,-6.395846,-9.711569,9.037508,-0.386209,-1.007976,1.833935,-5.507924,-0.694987,-0.905116,6.288910,9.114316,0.899011,8.180423,-9.627031,-0.964271,1.742834,-9.112279,-4.853388,6.732307,8.701588,0.585583,2.579739,4.356811,7.126335,0.248291,-8.975791,3.159621,-4.149338,0.474013,3.270847,-9.523380,-0.718652,-5.385404,1.100465,-2.823910,-0.113765,5.760183,7.892226,6.229740,-0.858072,9.846382,6.216065,8.662023,1.142570,-3.175910,-2.170570,1.874500,-7.516011,1.899570,-3.378011,-2.477734,7.376167,-2.068034,-2.262344,-1.828626,-5.708408,4.889313,-1.405493,0.709676,-9.776328,-5.346541,2.640293,0.819112,-3.907112,0.005336,-1.556019,3.372754,0.412681,-7.640865,0.940762,-0.964720,0.991931,-0.535256,-1.256789,6.460177,8.942012,5.592635,-1.673833,-0.009556,-3.618548,7.745950,6.666955,-3.414411,-4.356844,-1.338362,0.192913,-3.626911,6.898667,-0.714608,-5.032611,-3.530688,-2.590286,-6.878257,-0.485230,7.461020,-8.936272,-7.158204,8.239361,-4.854854,2.664691,7.729801,-0.713925,6.869304,-2.228597,2.374738,-8.645812,3.821406,-2.844019,8.975589,-6.826676,9.214395,1.398090,6.302517,-4.218309,-0.130817,-2.610597,7.923345,4.077133,-4.690009,-1.917882,4.354091,3.583351,3.732878,-3.703954,0.043214,4.959237,-6.237919,-2.176467,4.480757,2.204165,-2.379165,-6.035292,-7.112932,5.948123,5.300367,5.855745,-9.122270,8.644242,-4.499391,-8.278387,2.223277,-1.593967,-1.960057,9.721108,0.220980,4.446821,-0.682671,9.308623,-0.347828,-2.784056,9.698104,-1.387776,-6.737394,7.348502,4.788119,-5.629124,-7.938148,-9.224423,7.168458,-6.895971,7.949737,1.310268,7.814703,-3.919201,9.170938,-1.837951,-3.297814,-7.378944,-0.159554,3.890808,3.173065,-3.580827,-5.175463,-6.143622,-3.475981,1.743645,-3.111024,-9.855665,8.367852,0.434086,7.408145,5.152008,-5.783621,-0.513805,-0.034045,4.061798,-7.898675,0.253609,-5.408718,-5.438650,-3.978058,-1.111415,-2.173657,5.664207,-9.319217,-9.059088,-0.752903,1.834791,3.248431,0.740152,-7.323026,8.140696,5.839576,7.816724,-3.877525,-6.665379,9.720096,-0.260353,9.236254,-8.031345,-7.558200,8.590599,-6.314263,-5.698111,8.900898,5.666033,-6.631625,-8.655621,4.715690,4.670048,1.294106,3.433974,9.891454,6.833132,5.459126,-4.146231,-5.949173,-0.147394,-7.360751,7.626446,-2.352069,8.274931,1.680705,-0.384761,-8.883996,9.920629,-4.944190,-9.527765,-9.424945,-3.941259,3.627785,1.675279,6.496069,2.257402,-0.135775,5.549675,1.753032,8.823992,-9.949725,-4.085424,-9.251209,-7.687741,-0.195469,-1.738471,-4.091211,-8.410923,9.248772,-8.909284,0.053141,-2.726852,-1.179231,-6.723468,7.910180,-0.861759,-0.222792,-6.145474,-6.569341,1.751146,0.260553,4.719399,-1.810166,-0.492309,-7.748878,-9.481031,-0.733143,4.937813,-5.004318,-0.440300,-1.333371,8.317460,6.783517,5.859918,0.673729,-8.500957,-4.147644,-0.983932,1.607615,-7.214621,0.824453,9.132057,4.479504,-8.203687,3.803117,0.680421,-5.433755,-3.272112,-8.746954,1.662171,-8.318155,8.414668,-1.882473,2.508933,-4.270059,4.544562,4.411827,8.790827,1.033209,-3.743482,-6.218134,-1.967528,3.704988,6.685045,-3.248146,4.089496,-4.311072,9.675028,-5.202651,3.167438,-2.915696,9.083866,7.900403,0.212080,-0.123501,6.156527,7.256702,9.159287,-3.249989,7.579607,-6.834415,3.258055,6.298778,7.896314,-5.873123,-7.225393,1.010715,-1.408204,-2.314217,4.275357,7.447546,6.073602,6.021407,7.708739,5.581060,-8.879203,4.264049,9.338650,0.861416,9.356959,9.023735,-0.889170,0.468266,1.519967,-3.881638,-2.910034,-9.420614,7.180318,6.371630,7.807925,3.165342,-6.923893,-9.358357,3.847172,-5.358160,1.424199,-8.801307,-2.886909,-4.038055,4.042022,-8.584396,-7.141839,4.984727,-0.835385,4.027927,-9.537482,-3.813975,0.186944,-0.150302,-3.178746,7.248065,-3.425749,1.775994,2.572538,-6.813081,3.753610,9.532160,4.648663,4.454755,4.101741,-3.549950,1.060882,-2.978147,2.093056,5.134843,9.043542,2.940973,-1.772236,-2.739917,-2.254656,-5.615513,4.545830,9.978649,-6.708577,0.078054,0.696299,4.881194,-2.054559,-2.457638,-5.039561,8.214601,-9.921436,1.385436,9.214786,8.585005,7.358396,5.780238,4.951620,0.503462,6.106196,2.524484,-3.384794,7.804345,-4.379661,-1.009930,1.180458,-8.661880,-7.415190,-5.212250,0.545023,9.195584,2.840381,7.564148,-1.511848,8.170741,3.092517,-8.482418,9.470106,-1.379467,6.959160,1.479419,-1.531688,5.194871,6.250504,4.600885,0.695066,4.597393,0.379073,4.039057,-2.076228,-3.929124,0.609631,0.346016,-9.003460,-9.740841,7.566864,3.942359,5.919076,-8.663433,-8.198125,8.692371,6.783963,2.566685,6.738031,-5.040167,9.044791,-0.288167,8.426464,4.563921,5.171333,-1.379642,6.800429,7.206672,-3.222835,-0.010144,7.152024,-9.302170,-2.900989,1.702581,-3.299836,2.601293,-4.426639,-3.074858,-7.527293,-4.205294,1.875238,-1.285330,-5.026397,6.580015,5.837989,7.115106,6.536706,3.234062,7.248923,0.364630,-7.814298,5.741839,-6.824659,3.015438,-9.503890,6.833777,-1.682335,-6.285713,1.374518,3.760672,0.649778,2.668255,-0.095900,4.004508,0.976882,8.454835,7.755432,1.238901,-1.540789,-8.383558,-0.539115,-2.564851,4.056125,0.041694,-0.841201,-6.700000,9.518213,-0.369732,-4.708001,-9.242968,-0.246281,-0.910522,-7.626251,-0.751802,-0.428186,9.683778,-3.104574,5.090951,2.636899,-3.911221,4.500123,9.190427,-4.018559,-1.195825,2.072849,-7.897472,-8.078781,-0.592430,-9.429722,5.264182,4.754902,5.412758,-1.919652,-4.018800,6.460766,1.713997,5.133767,-2.997511,-4.992284,-4.797318,8.190087,0.940097,9.802259,-5.429356,-3.437395,-1.397624,5.549011,4.312467,-4.590437,9.946800,-0.430591,-9.348225,8.675310,6.347963,7.666997,-3.866222,2.916205,-2.249023,4.621929,-1.245064,-2.886306,0.164585,4.696856,1.973925,-0.625338,7.485902,6.856908,-7.221451,-8.103781,-3.180433,-9.101417,-5.396595,0.185870,-2.886910,-6.904783,-8.956014,-3.031174,-5.857261,4.799355,6.083955,-8.236013,-1.926784,8.348198,-4.754665,1.454441,0.958856,2.311925,2.827108,4.163157,5.688840,-8.963457,-8.682199,-4.202500,-5.852553,3.894600,7.064144,4.663292,8.807924,4.339904,-9.294538,2.166672,-5.631497,-9.954099,0.075885,1.534070,8.201801,-1.712255,-6.213687,-3.583476,-4.471465,2.410603,9.141604,-8.656216,2.641823,-6.698429,-7.769639,5.409448,9.409480,-5.924694,3.558813,2.534952,6.244160,9.760938,-4.989402,1.339683,5.144886,8.832935,7.177430,7.392858,7.837104,-2.510609,1.536585,-3.131027,6.940809,4.854745,-4.570220,2.272353,9.299588,-2.258563,-6.324780,-2.300966,-0.747103,-4.202808,5.364101,-4.392220,-3.625624,-7.693316,-7.370838,-0.248738,6.223760,5.433921,-4.316169,-1.914204,8.537433,-6.995222,-7.749811,3.003028,-4.600760,-9.596214,2.872651,-2.562226,7.297158,-4.416435,2.269285,-1.290918,-6.751617,-7.737177,-2.691998,-1.447125,3.598857,-0.543776,-0.173951,-7.874699,5.589426,-1.767375,0.319125,-0.316374,-3.187510,8.054510,2.666745,-7.342634,9.074889,6.853398,1.157189,5.429789,-0.674143,-9.244634,9.150243,9.790072,3.447108,8.610933,-0.048684,-8.434862,-1.982320,-8.606823,9.224114,-7.645186,7.329439,-8.516609,1.458072,-9.388528,2.557755,-4.575092,5.561422,-0.434336,-3.723474,-8.777808,1.241738,8.473051,-0.824304,-3.641496,-1.743452,-7.473051,-9.267835,3.959111,-6.030239,5.130579,-7.673140,-4.644032,7.272299,3.719267,-2.247915,-5.955117,-2.473193,-4.968127,8.887768,-1.701732,7.684660,2.200506,7.167381,8.412694,-2.319007,-0.435344,0.675233,0.270408,0.282489,-4.753653,-5.327240,4.351627,-5.771051,7.158855,-1.102416,8.060315,-1.576308,3.947018,1.168993,1.975413,7.590938,5.903448,-8.033204,4.483580,8.102632,4.809750,-7.164889,-9.467110,-8.958670,-3.095232,6.941550,-1.535756,0.290915,2.803052,5.275047,-0.683998,-1.588264,2.495178,-4.700860,-6.919510,-9.925853,3.716907,6.710091,1.760540,1.937412,-6.015269,4.558152,-4.075640,0.078347,-0.893579,-3.201420,9.132518,-3.491631,3.603006,-6.517492,-2.364150,-4.651491,5.913157,0.877355,6.650114,5.365304,4.656145,5.546538,3.502019,1.270790,3.126287,-6.047734,0.499513,2.318753,-9.332447,-9.218866,-4.146221,-3.461087,-7.620910,-8.515819,5.860282,-0.688268,-9.951763,-8.790342,-3.598825,6.211062,-8.635877,-0.076502,-8.166748,-8.160557,5.740439,2.400350,4.823661,-9.654116,9.063536,-5.192805,-0.953706,1.374249,-6.379693,-0.329519,-6.423965,-4.715344,7.483480,-9.618709,-9.096076,-8.424190,2.998520,8.511724,-5.419641,1.433990,-4.229045,-3.239209,-0.186582,6.486486,1.687403,5.142166,-5.807810,-6.571260,-0.372851,5.251196,-2.954342,7.613594,-8.229971,-9.160866,-8.847281,-8.548881,0.366720,9.341306,6.873309,-1.659080,-5.814676,-7.143024,3.809224,-0.186641,3.716860,-5.905647,-1.414343,2.989366,-8.390849,0.450048,7.721346,0.420480,-5.587384,-0.086961,-3.016012,-3.204563,-3.672770,8.697988,-2.713874,-6.306323,3.857163,8.620036,-0.572577,-1.009172,-8.314768,7.250253,-9.191830,4.277448,0.049068,-2.397519,-8.431750,-6.945183,2.163194,8.663263,2.978239,5.639327,-0.197978,-0.237148,3.891036,-1.463189,-1.279354,-7.093075,-2.796424,9.056526,4.402212,6.693238,6.658599,1.433986,8.748215,-7.019878,-3.805064,-2.223752,-2.893499,2.757901,7.711826,0.004844,4.211133,-9.645710,0.675866,1.636967,4.400613,2.200245,-0.302334,2.821202,2.046687,-4.351504,6.067353,-5.818566,-1.401367,-4.226722,5.191482,2.479355,4.773088,8.886086,-4.044678,8.859398,8.545880,-8.686401,9.865380,-0.644782,4.033960,-1.561212,6.730104,-5.693931,-5.808910,9.776035,-7.981688,-7.720360,6.681401,1.086004,-1.342821,1.810295,5.055607,8.715458,-9.186804,8.493905,3.589461,-3.396522,-1.907098,-4.411725,1.589732,3.780624,-8.585719,0.803328,3.732725,8.888067,-3.617162,6.998638,-1.429450,-7.666340,-8.708358,-3.717685,-2.556173,-7.602538,3.597443,8.945828,7.967576,6.837959,0.425829,9.980625,1.838312,-4.572978,5.632568,7.065696,1.116121,-9.052762,5.148587,8.240595,-5.339212,-6.163971,-1.037036,-2.125423,-9.208400,9.754966,7.752551,-8.079977,-2.639149,-9.363366,9.376456,4.008621,3.263692,-7.122354,0.133506,-6.760144,-4.770032,2.684224,0.893833,-4.633570,1.457480,8.416984,-5.325127,0.014287,-2.169992,-8.591932,0.128059,-2.437987,-7.893906,8.972181,-3.284301,3.835170,6.208469,3.641743,-0.893357,-9.640265,-1.828726,-2.965691,-0.602152,2.580456,1.470022,-1.830566,4.363310,-7.718648,7.785451,2.591091,8.906535,-9.767992,-2.360066,9.500179,8.437385,-5.967050,8.069497,-5.936182,3.911490,3.844573,-6.721474,2.656762,-7.787568,1.931700,-3.355210,-2.493923,0.336370,-1.675390,-3.452633,-5.094511,0.637061,0.645571,-1.198906,-0.285327,7.726455,-9.053875,5.037204,-0.642701,1.712937,-9.059978,-4.922043,-5.671444,9.104713,6.400594,-5.768080,-3.460128,4.264637,8.201482,4.316381,9.791459,3.154028,-6.065136,7.745997,-3.723008,-1.197401,-4.520679,7.971983,-1.761424,8.181883,2.090534,-7.524279,-1.112265,1.162668,3.076555,1.431871,-0.601887,-4.601670,-1.547480,3.196281,5.546062,4.880826,-2.146703,-4.936334,3.491631,5.940248,6.057591,-3.480520,4.584668,3.018868,1.356098,4.452630,3.493519,-0.901359,3.946664,3.299441,-0.337794,1.883347,3.512445,5.658316,2.828805,4.484353,-3.444065,-7.118510,-9.394795,-5.244659,6.919444,5.046737,-1.562189,-8.152191,2.043717,-5.236087,-0.666706,-1.058951,9.060549,-0.731833,-8.621888,0.842534,-3.669985,-8.303204,-5.288195,-2.607776,-4.399173,-1.142087,4.445936,5.079897,-1.797879,-3.103832,1.102473,2.290391,1.074133,7.861957,0.929274,-7.435918,6.382582,-5.407415,-3.550150,8.474008,-2.094083,1.222630,-2.625742,-3.615340,-4.307547,4.714735,-3.635169,-1.221226,-6.464129,2.420198,-6.785623,5.677259,4.974615,9.551935,-4.016569,-0.998391,3.210366,7.847750,-8.589531,-8.941285,-0.588468,-2.099693,-0.728433,-8.601663,2.328943,6.292720,-9.258156,6.735382,-0.826573,6.832049,3.285838,-9.318495,3.691467,-8.361809,9.754903,-9.136168,-1.589023,-0.903059,2.416554,3.271076,7.831175,-3.024262,-4.441072,0.866529,5.892617,1.973836,-2.078040,0.976293,7.544411,-1.010617,-2.330049,0.520781,1.692042,-7.556296,-4.782441,7.181221,-8.227974,9.113792,0.334625,8.872710,0.031643,1.381311,-1.320333,3.916747,-5.302668,4.295101,-5.644252,5.978059,-6.150556,-5.429699,-6.176448,-1.910144,-4.824784,9.340202,-8.188426,-8.407937,4.716058,-2.363824,-6.823583,-1.664722,2.530044,1.132032,-7.710230,9.996990,-2.247707,7.007678,-7.277228,0.581593,-4.854235,-6.429508,-6.610305,-7.341436,5.154140,7.337131,5.645157,-2.744442,5.908473,-4.686330,0.207931,8.568253,-5.053149,-0.281709,-1.466360,3.859470,-9.693203,-6.573980,-7.581479,-5.845864,8.017500,8.377964,9.545241,7.018899,1.073502,-4.126853,2.906258,8.724892,8.024480,-6.931593,3.220661,-2.190748,-3.159689,-9.394889,8.786427,-7.790634,4.347487,7.700845,1.346635,4.225378,5.623948,0.593182,4.422477,-7.820726,-3.110841,0.264768,-1.227412,7.569037,-8.964005,6.867996,1.030008,-6.804076,8.348955,2.463532,-6.827608,8.333830,0.841891,-0.787340,1.453387,7.216294,-1.855594,-8.130811,-2.744230,2.157493,2.434782,-0.148959,-0.728966,7.605634,2.772213,-2.697971,-2.710192,3.867703,8.907139,-8.660513,-0.560549,-3.850497,-4.135910,2.264722,7.444819,9.027899,2.742300,8.687276,-5.652646,9.148965,5.004175,6.675488,6.559240,5.221515,9.486701,-0.174876,4.582600,-1.040942,3.152151,-1.131623,-0.455591,0.984140,-6.378150,3.533857,-8.607693,-4.621672,-4.971342,2.606285,-9.019657,-5.527213,-4.507672,8.395209,-4.718742,-1.376692,5.518230,-1.672637,-2.467454,1.876970,-0.463614,-9.580881,3.521483,-3.208299,-9.498269,1.459908,2.208991,-5.153016,-5.265893,3.307419,5.147580,-7.087340,6.365157,-1.007927,7.674392,-5.591517,-7.315486,-1.816686,4.289977,-2.194952,-8.686487,-4.109728,6.014484,7.467722,-7.036582,-5.063310,-6.124044,-0.340141,1.270184,-0.018831,-5.813577,-4.685589,6.552859,-5.500030,-0.294575,-1.717181,-9.327341,-6.231751,-8.014125,-2.103635,-8.072780,-4.461936,7.294715,-2.299941,-5.484888,0.314923,5.180663,3.923813,-1.931182,5.274187,-5.872840,4.285845,-9.459821,9.166815,-1.280584,0.192718,-8.207526,8.296160,-2.892444,3.035135,-0.818060,6.929385,-4.269277,-7.264860,-1.151502,0.216403,-3.184302,-3.290547,-3.301505,5.446523,5.627001,-5.090578,-9.577740,1.628880,2.427593,6.765996,-7.428133,-2.685255,-6.345658,3.568935,-0.937609,8.770855,-3.049628,-5.160989,7.482248,6.484537,-9.422968,9.648318,6.062334,-9.570727,2.496438,9.961211,-7.407270,-0.232456,-0.195853,-3.434005,6.532444,1.957773,2.590229,-8.527170,3.447748,6.246551,7.853804,0.847245,1.887932,-3.203877,5.589656,-6.035320,5.890445,-3.274380,5.232245,-6.619883,0.082912,-4.232355,5.969297,5.174818,-2.004890,8.477702,4.653936,-2.141435,-6.513759,3.845558,-6.629768,3.032988,0.085676,-3.638022,-5.479366,1.957197,-1.031909,-3.778140,-8.824829,9.561343,-1.166093,1.904575,1.529899,9.753457,-2.740651,7.663645,-4.454929,-3.668508,0.048248,-0.686847,9.629601,4.863320,3.749050,-2.300702,5.905443,-4.776562,-7.035912,-2.390659,-5.360957,4.287464,-3.356349,3.351910,0.902587,-3.889689,-8.319221,4.671015,-7.012512,-8.015863,-1.205104], dtype = "float64")#candidate|3420|(1728,)|const|float64
var_3421 = relay.var("var_3421", dtype = "float32", shape = (9, 6))#candidate|3421|(9, 6)|var|float32
call_3419 = relay.TupleGetItem(func_935_call(relay.reshape(const_3420.astype('float64'), [9, 16, 12]), relay.reshape(const_3420.astype('float64'), [9, 16, 12]), relay.reshape(var_3421.astype('float32'), [54,]), ), 1)
call_3422 = relay.TupleGetItem(func_939_call(relay.reshape(const_3420.astype('float64'), [9, 16, 12]), relay.reshape(const_3420.astype('float64'), [9, 16, 12]), relay.reshape(var_3421.astype('float32'), [54,]), ), 1)
func_2553_call = mod.get_global_var('func_2553')
func_2555_call = mutated_mod.get_global_var('func_2555')
call_3429 = relay.TupleGetItem(func_2553_call(), 0)
call_3430 = relay.TupleGetItem(func_2555_call(), 0)
output = relay.Tuple([call_3386,call_3389,bop_3410,call_3416,var_3417,call_3419,const_3420,var_3421,call_3429,])
output2 = relay.Tuple([call_3387,call_3390,bop_3413,call_3418,var_3417,call_3422,const_3420,var_3421,call_3430,])
func_3454 = relay.Function([var_3417,var_3421,], output)
mod['func_3454'] = func_3454
mod = relay.transform.InferType()(mod)
var_3455 = relay.var("var_3455", dtype = "float64", shape = (9, 36))#candidate|3455|(9, 36)|var|float64
var_3456 = relay.var("var_3456", dtype = "float32", shape = (9, 6))#candidate|3456|(9, 6)|var|float32
output = func_3454(var_3455,var_3456,)
func_3457 = relay.Function([var_3455,var_3456,], output)
mutated_mod['func_3457'] = func_3457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mod.get_global_var('func_2260')
func_2262_call = mutated_mod.get_global_var('func_2262')
call_3510 = relay.TupleGetItem(func_2260_call(), 0)
call_3511 = relay.TupleGetItem(func_2262_call(), 0)
output = call_3510
output2 = call_3511
func_3524 = relay.Function([], output)
mod['func_3524'] = func_3524
mod = relay.transform.InferType()(mod)
mutated_mod['func_3524'] = func_3524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3524_call = mutated_mod.get_global_var('func_3524')
call_3525 = func_3524_call()
output = call_3525
func_3526 = relay.Function([], output)
mutated_mod['func_3526'] = func_3526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2553_call = mod.get_global_var('func_2553')
func_2555_call = mutated_mod.get_global_var('func_2555')
call_3547 = relay.TupleGetItem(func_2553_call(), 0)
call_3548 = relay.TupleGetItem(func_2555_call(), 0)
func_733_call = mod.get_global_var('func_733')
func_736_call = mutated_mod.get_global_var('func_736')
var_3556 = relay.var("var_3556", dtype = "float64", shape = (468,))#candidate|3556|(468,)|var|float64
call_3555 = func_733_call(relay.reshape(var_3556.astype('float64'), [13, 4, 9]), relay.reshape(var_3556.astype('float64'), [13, 4, 9]), )
call_3557 = func_733_call(relay.reshape(var_3556.astype('float64'), [13, 4, 9]), relay.reshape(var_3556.astype('float64'), [13, 4, 9]), )
output = relay.Tuple([call_3547,call_3555,var_3556,])
output2 = relay.Tuple([call_3548,call_3557,var_3556,])
func_3558 = relay.Function([var_3556,], output)
mod['func_3558'] = func_3558
mod = relay.transform.InferType()(mod)
mutated_mod['func_3558'] = func_3558
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3559 = relay.var("var_3559", dtype = "float64", shape = (468,))#candidate|3559|(468,)|var|float64
func_3558_call = mutated_mod.get_global_var('func_3558')
call_3560 = func_3558_call(var_3559)
output = call_3560
func_3561 = relay.Function([var_3559], output)
mutated_mod['func_3561'] = func_3561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3348_call = mod.get_global_var('func_3348')
func_3350_call = mutated_mod.get_global_var('func_3350')
call_3610 = func_3348_call()
call_3611 = func_3348_call()
func_3454_call = mod.get_global_var('func_3454')
func_3457_call = mutated_mod.get_global_var('func_3457')
const_3617 = relay.const([6.064264,9.082991,-2.948100,-8.719097,-1.070392,8.237483,9.948026,-7.762244,-0.793024,3.959199,-7.551422,6.324003,-6.961147,7.112043,-1.085683,4.472121,-8.614344,-7.870972,9.893417,1.801752,0.988225,-8.460229,-0.349032,2.652391,1.974545,3.303487,6.941351,-6.153125,-7.838048,1.781289,7.708947,-9.612414,-2.565749,7.476481,6.941871,2.144142,1.155381,-3.084497,-0.904596,-2.274767,-4.795119,-1.985692,-5.842489,-6.163360,-5.406551,5.101365,-9.117785,7.030404,-4.645786,-0.538256,2.548542,-9.736212,6.993667,-6.364981,-3.898217,-7.391021,-3.027047,-1.922688,6.779858,-6.203561,5.057618,-7.006880,0.856729,-4.601967,-0.969050,-1.934572,-0.760860,-3.373661,7.034192,3.384685,2.057474,-8.660028,-8.768374,-2.863082,6.768035,1.182139,-2.421591,7.577714,9.887857,5.834388,-2.538519,2.136897,-4.761364,3.603730,-4.073907,3.248528,-8.291228,-8.655998,-4.498811,-7.193538,1.214410,-1.293201,4.365168,3.014841,0.014685,-8.420236,-1.474967,-1.356195,7.912231,-7.838431,3.175931,7.713193,-3.722440,-7.295105,-1.591164,-3.141355,1.398923,1.932960,-6.930959,6.279028,6.455910,-2.834751,-7.842572,-3.159439,-6.547379,1.223746,-1.507698,5.198743,-6.706762,-1.260160,-3.761414,-4.316535,9.055619,2.334629,2.533599,-4.113127,-8.265720,-2.564065,0.131293,6.240778,-9.986559,5.969353,1.994500,9.818141,4.215694,0.687254,-8.116385,3.024177,4.050343,-3.745215,2.586567,-1.941929,1.361910,-6.503404,9.824277,-2.313028,7.553391,2.684916,-8.113677,-0.826856,-7.193433,8.106579,-4.434260,-8.955086,0.764406,-9.575802,2.005626,3.757367,7.083417,-9.372487,3.315006,-0.238606,-9.282973,2.217370,-0.289946,-2.750425,1.571255,-2.557846,-3.433586,-0.453226,9.003517,8.155235,1.938723,5.525286,-4.577403,9.320022,-3.757998,-0.230398,3.132816,9.241598,-0.164018,-5.828720,1.403769,3.064606,-7.154832,-9.026634,-9.396039,-4.295340,-8.307187,-1.831262,2.644473,-4.754342,-2.125570,2.615990,-6.410142,4.972732,-0.219775,6.185393,-3.546196,-5.472794,-3.687085,-4.292968,-9.261940,-3.180577,-2.897508,9.389537,-9.468901,9.350536,4.889518,5.224662,1.516566,-3.470284,-5.579624,-3.543857,-8.007404,1.512256,8.975762,4.901002,8.747616,-9.037188,-9.890073,5.206050,7.381180,2.544982,0.619129,-1.107814,-9.042234,0.851638,-0.733184,4.161463,-1.547899,4.836723,9.070560,7.511421,-6.957906,-3.529779,7.649563,-9.025770,7.996721,0.920832,-1.361329,4.640431,-9.876849,1.611044,-5.783701,5.030638,-2.647952,-1.645175,8.347891,-4.314929,6.752731,9.444059,-7.788704,5.869382,4.587977,6.959759,5.647318,-0.222721,6.881388,-5.899479,6.598539,-3.463784,6.088891,2.857799,-6.625186,-2.648464,-4.106634,-0.007311,8.428149,-1.406331,2.336474,-1.556767,1.515830,-7.419436,6.130437,-6.691006,7.994910,-6.578192,-8.486465,2.460582,0.802522,-2.247691,6.882571,-6.980131,0.202813,-0.576483,-5.969796,2.859651,3.606787,-4.981857,-2.865635,8.463669,8.479682,-6.690947,5.920849,-8.809204,-7.982833,2.854735,-5.225919,-9.077449,-1.761739,-1.521850,-4.434681,-3.371352,8.843145,-9.600653,-9.955469,1.216830,1.668943,0.802936,-9.628572,6.916870,-3.208415,-3.576194,-5.385354,-3.384336,2.392857,-3.505737,-6.337701,-9.357022,0.455396,-2.579983,-5.764398,-0.449531], dtype = "float64")#candidate|3617|(324,)|const|float64
const_3618 = relay.const([8.290920,-7.660519,6.019352,-6.838655,-8.715455,-8.403821,7.116766,2.879622,-4.353078,-5.126494,-2.130468,0.627700,-5.381015,-6.980719,9.181488,1.436320,-6.620656,-1.344962,6.494554,6.658289,-8.135226,3.738421,-2.077237,3.671886,-4.889784,4.284602,-4.704250,-6.173465,-4.927253,3.336005,-9.458347,-1.215334,-9.891025,-2.736028,-0.585280,5.985813,5.433420,-7.385710,2.895811,-5.119501,7.336484,-8.635869,-1.083393,2.594746,1.746705,-4.094402,9.319756,-2.822278,-1.439543,8.852613,6.221923,9.762025,-8.385257,-1.901836], dtype = "float32")#candidate|3618|(54,)|const|float32
call_3616 = relay.TupleGetItem(func_3454_call(relay.reshape(const_3617.astype('float64'), [9, 36]), relay.reshape(const_3618.astype('float32'), [9, 6]), ), 0)
call_3619 = relay.TupleGetItem(func_3457_call(relay.reshape(const_3617.astype('float64'), [9, 36]), relay.reshape(const_3618.astype('float32'), [9, 6]), ), 0)
const_3620 = relay.const([[[8.365942,4.511757,-9.675426,-8.909639,-4.365268,1.563840,5.918357,5.258832,8.566246,-2.806722,-3.062840,0.256872,-2.654298,-4.642695,9.364948],[2.018236,-8.604008,3.477834,-0.757474,9.961436,8.700394,-3.169244,-3.599235,-8.742109,1.080877,-8.817259,-4.940426,2.923908,-4.717624,-1.875659],[9.127629,-8.093963,-0.952115,-8.076017,-8.033103,9.365281,-4.274219,-5.406351,-0.140225,3.559603,6.916005,6.780542,2.754062,-2.585435,-8.744732]],[[9.408885,3.691279,1.652780,2.989509,-5.911500,0.602777,1.773834,-9.701915,-7.828092,0.387547,-9.308313,-8.375881,-8.807851,-3.049226,6.959731],[4.074496,-4.258054,-9.925895,2.641692,2.566875,5.234909,0.676998,6.323953,-6.795433,-0.462381,2.543257,1.112000,-3.357639,1.079597,-5.407530],[4.093494,0.532325,-9.125340,-9.510599,-2.783219,-7.741309,-1.179034,-0.389345,3.765466,-2.328453,-2.765885,-3.293260,1.121387,6.823925,7.018930]],[[8.194528,-1.844061,-7.236032,-3.377917,-6.020628,-7.390883,7.679322,-0.552341,-8.889675,-5.740969,-3.288397,-9.195275,-9.811053,4.753658,-6.850611],[-4.519978,-9.845453,1.131162,4.439176,5.311444,-2.603387,-9.460429,-9.902734,3.960829,-3.632136,7.846290,8.839168,7.087400,6.858046,1.605103],[8.112763,1.902972,-3.297891,-2.880320,4.025481,2.439670,-6.316716,3.753865,5.669901,9.903868,-6.294143,-1.035737,6.356418,-0.744525,-6.194241]],[[-9.668750,5.199489,0.411980,-5.849975,6.293819,7.732151,6.340560,7.181496,3.765608,-0.165004,-6.276991,4.586079,-2.386239,2.668986,-3.380727],[-3.571710,9.779631,-1.484100,-7.007571,6.779065,-2.311973,-0.420909,-5.451571,-7.501734,-1.413515,-2.050536,-6.509111,9.226276,-8.777601,6.706477],[1.717361,-2.797832,0.392046,3.207184,9.556094,6.084994,-8.054173,-4.325713,5.484462,-0.472210,7.301733,4.493530,-0.742614,-4.619694,3.795996]],[[2.577570,4.969087,6.427516,5.645576,-1.778345,5.582659,-9.042119,-6.295267,-2.770835,-8.015398,6.914645,-3.608590,3.989617,-5.560546,0.207425],[3.754361,-3.231113,-5.119449,3.534084,-5.004622,7.369370,7.734817,9.599497,-0.426506,-3.892307,-4.728164,-0.451542,-7.355823,-9.215023,1.464440],[-4.790711,-5.810273,5.624115,-7.511405,-1.848848,2.954370,0.383231,-1.281095,-7.968724,-0.698824,1.852643,-8.326334,6.179779,4.790911,9.730253]],[[-0.674357,9.637938,-6.756377,4.244288,9.376053,-3.676976,7.666315,2.671039,-4.184017,-5.812617,-2.895597,-9.345354,9.238550,7.912318,3.099508],[8.607271,-6.368327,-9.955047,-8.850378,-5.095035,-6.026687,-4.015951,-0.527798,5.513660,8.260871,7.065843,4.121431,-1.425518,-1.442062,5.589044],[6.782497,7.506691,3.820771,-4.264313,4.481545,6.686626,9.863721,-0.612800,7.232245,7.825544,0.525475,3.189170,-6.622593,-6.213968,4.549369]],[[-8.837963,-7.126826,6.937470,3.512075,4.045391,-0.787264,-3.013066,-7.734398,5.725021,-6.888823,-2.435255,4.947554,-3.551299,-1.049256,-1.948335],[-0.425237,-5.012553,-8.597641,-6.320575,8.430613,7.517589,-3.430691,-9.824482,-3.274497,6.382722,-0.281167,-8.915223,0.099294,7.684473,7.942979],[4.283235,-8.258015,6.080898,2.795777,-0.490476,3.717455,-2.067658,-2.698953,6.719491,-7.486670,9.898036,-6.867532,4.037622,7.573416,0.176413]],[[-6.679609,-4.458575,-8.192174,-2.403902,-6.112944,1.577234,-1.846727,2.937697,-0.692220,1.964722,1.628005,3.231303,-6.367896,9.438642,2.968672],[0.358357,-0.430159,-3.770898,7.896126,-2.114357,5.497653,5.560383,-4.701514,-1.971565,6.521233,5.336067,3.784036,1.722631,9.589327,6.433079],[4.586914,8.492316,-6.858206,8.413683,-6.548579,6.085123,1.317050,8.781071,-7.254814,-0.417032,0.977831,-4.415750,-3.120894,-4.512329,8.868194]],[[-2.617018,-0.433193,-1.775907,2.701092,-6.564818,8.274917,6.036102,1.346346,-0.071342,2.105528,4.642457,4.883032,9.999103,5.620074,4.612669],[4.805831,-8.182229,4.319610,-3.781615,-8.094242,-7.407895,1.706058,-2.963257,-5.511637,-0.127195,9.063850,-9.003958,5.196116,-2.799800,-4.715547],[1.381030,0.834213,2.997525,-0.873585,8.254547,2.744599,0.992817,2.885228,8.860244,-4.907715,8.582226,6.819486,-5.271669,6.668229,-6.978756]],[[7.584926,7.562878,4.332074,9.573693,7.026520,-7.401946,0.628470,7.732865,6.088574,-0.387678,-2.439233,3.475816,-5.412475,-5.227192,-7.208522],[2.365951,0.700610,-9.259561,4.660827,-4.646392,-9.642978,4.505515,-2.517873,-4.792176,2.485450,-2.151999,0.532496,-6.661447,3.713373,4.152182],[2.783961,1.578658,-0.240246,0.360089,-4.646969,-7.541717,-9.870083,-9.697566,-9.821269,-4.184786,0.175415,3.129216,-7.686129,-8.491098,-8.171655]],[[3.568385,-4.096668,-4.116414,-7.615178,6.048924,-4.224696,0.627453,4.869949,3.922144,-8.902599,-1.495521,-8.362038,-0.988799,4.136207,6.769300],[1.894766,1.578226,4.697015,-4.993213,1.576287,-6.984475,9.503808,-7.268990,9.203547,-1.749589,4.835862,-3.916495,-1.733173,-3.194183,2.811796],[9.679535,-8.726127,2.626591,4.457344,7.551901,2.738387,-1.383850,4.085925,8.158587,-9.646885,-0.882538,-1.613382,-7.820253,-1.183278,-2.752144]],[[-2.235586,-9.520256,-6.679849,-4.598556,9.215395,-9.615518,-5.405758,0.651828,2.461699,-6.421155,-0.193520,3.997751,3.958782,4.162201,-0.405472],[-8.867672,1.692201,5.273440,-8.959664,0.824586,1.379478,-0.475075,-2.581874,1.489359,-2.335880,-6.283865,2.274134,-2.083592,6.590961,-0.827006],[6.740958,-1.017307,9.244103,1.384457,6.725178,2.043646,-4.969381,-3.367363,5.719294,6.315335,-6.877179,-6.015705,7.222269,-4.962133,-0.436733]]], dtype = "float32")#candidate|3620|(12, 3, 15)|const|float32
bop_3621 = relay.greater_equal(call_3610.astype('bool'), const_3620.astype('bool')) # shape=(12, 3, 15)
bop_3624 = relay.greater_equal(call_3611.astype('bool'), const_3620.astype('bool')) # shape=(12, 3, 15)
output = relay.Tuple([call_3616,const_3617,const_3618,bop_3621,])
output2 = relay.Tuple([call_3619,const_3617,const_3618,bop_3624,])
func_3629 = relay.Function([], output)
mod['func_3629'] = func_3629
mod = relay.transform.InferType()(mod)
output = func_3629()
func_3630 = relay.Function([], output)
mutated_mod['func_3630'] = func_3630
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3644 = relay.var("var_3644", dtype = "float32", shape = (9, 1, 2))#candidate|3644|(9, 1, 2)|var|float32
uop_3645 = relay.log(var_3644.astype('float32')) # shape=(9, 1, 2)
output = relay.Tuple([uop_3645,])
output2 = relay.Tuple([uop_3645,])
func_3657 = relay.Function([var_3644,], output)
mod['func_3657'] = func_3657
mod = relay.transform.InferType()(mod)
var_3658 = relay.var("var_3658", dtype = "float32", shape = (9, 1, 2))#candidate|3658|(9, 1, 2)|var|float32
output = func_3657(var_3658)
func_3659 = relay.Function([var_3658], output)
mutated_mod['func_3659'] = func_3659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_3696 = relay.TupleGetItem(func_2172_call(), 0)
call_3697 = relay.TupleGetItem(func_2173_call(), 0)
output = call_3696
output2 = call_3697
func_3700 = relay.Function([], output)
mod['func_3700'] = func_3700
mod = relay.transform.InferType()(mod)
mutated_mod['func_3700'] = func_3700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3700_call = mutated_mod.get_global_var('func_3700')
call_3701 = func_3700_call()
output = call_3701
func_3702 = relay.Function([], output)
mutated_mod['func_3702'] = func_3702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mod.get_global_var('func_2260')
func_2262_call = mutated_mod.get_global_var('func_2262')
call_3706 = relay.TupleGetItem(func_2260_call(), 0)
call_3707 = relay.TupleGetItem(func_2262_call(), 0)
output = call_3706
output2 = call_3707
func_3716 = relay.Function([], output)
mod['func_3716'] = func_3716
mod = relay.transform.InferType()(mod)
output = func_3716()
func_3717 = relay.Function([], output)
mutated_mod['func_3717'] = func_3717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_3746 = relay.TupleGetItem(func_1891_call(), 0)
call_3747 = relay.TupleGetItem(func_1892_call(), 0)
uop_3763 = relay.rsqrt(call_3746.astype('float32')) # shape=(9, 12, 1)
uop_3765 = relay.rsqrt(call_3747.astype('float32')) # shape=(9, 12, 1)
output = uop_3763
output2 = uop_3765
func_3766 = relay.Function([], output)
mod['func_3766'] = func_3766
mod = relay.transform.InferType()(mod)
mutated_mod['func_3766'] = func_3766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3766_call = mutated_mod.get_global_var('func_3766')
call_3767 = func_3766_call()
output = call_3767
func_3768 = relay.Function([], output)
mutated_mod['func_3768'] = func_3768
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3794 = relay.const(-6, dtype = "uint64")#candidate|3794|()|const|uint64
var_3795 = relay.var("var_3795", dtype = "uint64", shape = (7, 7, 2))#candidate|3795|(7, 7, 2)|var|uint64
bop_3796 = relay.right_shift(const_3794.astype('uint64'), var_3795.astype('uint64')) # shape=(7, 7, 2)
func_935_call = mod.get_global_var('func_935')
func_939_call = mutated_mod.get_global_var('func_939')
var_3815 = relay.var("var_3815", dtype = "float64", shape = (1728,))#candidate|3815|(1728,)|var|float64
const_3816 = relay.const([5.847460,-2.007170,-2.723771,6.362130,1.766279,9.503674,0.177250,4.210266,-3.012847,-5.152085,7.005086,4.998499,0.429269,-7.092185,-2.915936,0.219706,2.200696,1.703931,-9.918689,-0.643154,-6.289742,-6.612356,-5.145416,-6.952613,-0.303874,9.938107,8.931961,3.619848,-0.413691,1.121714,-2.034310,-1.304842,-5.642943,-9.506769,-9.309753,7.557651,-4.900372,-8.747991,2.972837,0.185187,-6.380115,3.906966,4.187259,-2.067184,1.135380,-5.138421,-2.103808,0.667990,3.755994,1.212310,-1.620787,-2.884283,-8.219122,9.497049], dtype = "float32")#candidate|3816|(54,)|const|float32
call_3814 = relay.TupleGetItem(func_935_call(relay.reshape(var_3815.astype('float64'), [9, 16, 12]), relay.reshape(var_3815.astype('float64'), [9, 16, 12]), relay.reshape(const_3816.astype('float32'), [54,]), ), 2)
call_3817 = relay.TupleGetItem(func_939_call(relay.reshape(var_3815.astype('float64'), [9, 16, 12]), relay.reshape(var_3815.astype('float64'), [9, 16, 12]), relay.reshape(const_3816.astype('float32'), [54,]), ), 2)
func_2000_call = mod.get_global_var('func_2000')
func_2003_call = mutated_mod.get_global_var('func_2003')
const_3825 = relay.const([[4.690553,-2.995959,-6.560363,-2.731741,-1.410913,2.491733],[2.453305,-7.157333,-9.069212,-5.384567,-6.858254,9.151067],[6.229309,-0.979049,-6.197483,-7.314511,-1.273387,-4.634255],[-4.203748,4.535919,4.869173,1.079058,2.153498,6.720242],[7.553806,-4.764342,5.347605,2.360877,-3.694482,-2.504763],[-6.110054,-1.824735,0.073575,-2.090729,2.749087,-9.072985],[-6.815425,-5.127086,3.820549,4.026667,7.488057,9.339507],[-7.048540,3.777103,-8.174837,0.402000,8.970640,-6.205334],[-2.264275,-8.121963,-8.348433,-9.133806,7.549321,-8.359541],[-5.315137,8.000579,6.159983,-9.427974,-0.398273,-3.996305],[3.509541,2.581816,-6.813288,8.626452,-3.592796,-3.320874],[-4.663842,-6.313808,6.769541,7.140841,-7.575839,3.328205],[2.834519,4.239364,-2.319873,-8.534732,6.174914,-6.874514],[9.427615,6.860260,1.230171,-2.605261,-5.621628,9.887397],[-5.500735,-5.056577,-8.329927,-9.378622,7.902062,2.714880],[-5.603968,-9.560780,3.659331,7.314517,-7.184252,4.702247],[-1.305381,-8.664286,-8.951735,9.482381,-6.730579,8.108713],[3.805849,-3.727966,-5.700480,-3.614255,6.871789,-5.846056],[0.417354,-5.779737,-1.756409,-9.090768,6.702631,-5.729372],[-2.066920,-9.883928,4.866945,6.228915,-4.643095,0.896729],[2.256778,8.548739,-6.593329,-0.462140,5.010306,-1.542097],[-4.409476,-3.926480,3.581266,4.080884,-9.402158,-4.052574],[9.516570,9.937437,3.248285,-1.894297,-5.563988,8.754608],[-6.136654,8.152065,-3.159566,9.513940,-6.460701,3.438736],[-5.158768,4.488761,-2.107078,-5.839550,-0.901381,5.634727],[4.627275,-8.998779,6.264135,-2.128250,8.624825,8.602995],[2.724766,-9.842924,7.821799,4.414595,-4.314184,-9.701572],[-9.136987,2.995854,-1.169436,-1.681337,-1.299391,-1.757020],[3.951579,3.360896,-9.017058,-5.670226,-3.898426,1.210997],[-8.152480,5.656032,7.608990,-3.994888,8.113449,-4.067498],[-0.460709,7.363168,-0.494174,2.323688,-0.231587,-2.963830],[7.000496,6.514551,-8.754031,7.637013,5.770930,5.786513],[6.391260,3.731175,9.249063,-6.239177,-6.784645,9.052804],[6.831541,-3.233561,4.866480,-1.096044,-7.426447,-9.924500],[-6.101420,9.592271,1.656866,7.600946,-2.906222,1.675290],[-9.643595,-1.276755,8.789884,1.536921,-3.003742,-4.542684],[9.694632,-5.121400,-6.833091,-8.523154,8.470744,4.236097],[-0.820704,1.531655,9.481169,6.231029,-3.304455,-1.808072],[9.437709,5.285071,-0.073256,7.142196,-2.342647,3.698246],[5.274240,-9.287571,7.621075,8.732742,-6.194765,1.148797],[7.212696,3.351825,-1.145689,9.281051,-6.543828,0.338406],[-7.444844,-5.021777,-7.411105,-8.193813,2.861943,-3.161963],[-9.704861,-0.027000,-3.455375,-9.140366,-2.122611,-0.802438],[5.962715,-4.539094,-3.273962,-3.944762,8.611653,6.252918],[-1.875883,6.117663,-2.185761,8.451442,4.614271,0.773295],[9.008466,7.003850,-7.969296,-0.351106,4.082094,2.355860],[-7.573609,-8.278593,-5.945013,9.546826,8.908452,-5.999992],[6.555409,-0.911223,5.949532,-5.804241,9.076516,4.150265],[2.676087,-8.549491,-5.791895,-8.590003,8.486743,-4.862464],[7.538624,5.657249,-2.029761,-1.290886,6.094418,-0.214380]], dtype = "float32")#candidate|3825|(50, 6)|const|float32
call_3824 = relay.TupleGetItem(func_2000_call(relay.reshape(const_3825.astype('float32'), [5, 6, 10])), 0)
call_3826 = relay.TupleGetItem(func_2003_call(relay.reshape(const_3825.astype('float32'), [5, 6, 10])), 0)
uop_3833 = relay.log2(call_3824.astype('float32')) # shape=(5, 6, 10)
uop_3835 = relay.log2(call_3826.astype('float32')) # shape=(5, 6, 10)
output = relay.Tuple([bop_3796,call_3814,var_3815,const_3816,const_3825,uop_3833,])
output2 = relay.Tuple([bop_3796,call_3817,var_3815,const_3816,const_3825,uop_3835,])
func_3842 = relay.Function([var_3795,var_3815,], output)
mod['func_3842'] = func_3842
mod = relay.transform.InferType()(mod)
mutated_mod['func_3842'] = func_3842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3842_call = mutated_mod.get_global_var('func_3842')
var_3844 = relay.var("var_3844", dtype = "uint64", shape = (7, 7, 2))#candidate|3844|(7, 7, 2)|var|uint64
var_3845 = relay.var("var_3845", dtype = "float64", shape = (1728,))#candidate|3845|(1728,)|var|float64
call_3843 = func_3842_call(var_3844,var_3845,)
output = call_3843
func_3846 = relay.Function([var_3844,var_3845,], output)
mutated_mod['func_3846'] = func_3846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_3894 = relay.TupleGetItem(func_1692_call(), 1)
call_3895 = relay.TupleGetItem(func_1693_call(), 1)
output = relay.Tuple([call_3894,])
output2 = relay.Tuple([call_3895,])
func_3913 = relay.Function([], output)
mod['func_3913'] = func_3913
mod = relay.transform.InferType()(mod)
output = func_3913()
func_3914 = relay.Function([], output)
mutated_mod['func_3914'] = func_3914
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3954 = relay.var("var_3954", dtype = "float64", shape = (3, 10, 16))#candidate|3954|(3, 10, 16)|var|float64
uop_3955 = relay.exp(var_3954.astype('float64')) # shape=(3, 10, 16)
output = uop_3955
output2 = uop_3955
func_3992 = relay.Function([var_3954,], output)
mod['func_3992'] = func_3992
mod = relay.transform.InferType()(mod)
mutated_mod['func_3992'] = func_3992
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3993 = relay.var("var_3993", dtype = "float64", shape = (3, 10, 16))#candidate|3993|(3, 10, 16)|var|float64
func_3992_call = mutated_mod.get_global_var('func_3992')
call_3994 = func_3992_call(var_3993)
output = call_3994
func_3995 = relay.Function([var_3993], output)
mutated_mod['func_3995'] = func_3995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3348_call = mod.get_global_var('func_3348')
func_3350_call = mutated_mod.get_global_var('func_3350')
call_4023 = func_3348_call()
call_4024 = func_3348_call()
func_3766_call = mod.get_global_var('func_3766')
func_3768_call = mutated_mod.get_global_var('func_3768')
call_4053 = func_3766_call()
call_4054 = func_3766_call()
uop_4055 = relay.acosh(call_4023.astype('float32')) # shape=(12, 3, 1)
uop_4057 = relay.acosh(call_4024.astype('float32')) # shape=(12, 3, 1)
func_813_call = mod.get_global_var('func_813')
func_816_call = mutated_mod.get_global_var('func_816')
var_4059 = relay.var("var_4059", dtype = "float32", shape = (54,))#candidate|4059|(54,)|var|float32
call_4058 = relay.TupleGetItem(func_813_call(relay.reshape(var_4059.astype('float32'), [6, 3, 3])), 0)
call_4060 = relay.TupleGetItem(func_816_call(relay.reshape(var_4059.astype('float32'), [6, 3, 3])), 0)
output = relay.Tuple([call_4053,uop_4055,call_4058,var_4059,])
output2 = relay.Tuple([call_4054,uop_4057,call_4060,var_4059,])
func_4061 = relay.Function([var_4059,], output)
mod['func_4061'] = func_4061
mod = relay.transform.InferType()(mod)
mutated_mod['func_4061'] = func_4061
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4062 = relay.var("var_4062", dtype = "float32", shape = (54,))#candidate|4062|(54,)|var|float32
func_4061_call = mutated_mod.get_global_var('func_4061')
call_4063 = func_4061_call(var_4062)
output = call_4063
func_4064 = relay.Function([var_4062], output)
mutated_mod['func_4064'] = func_4064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1771_call = mod.get_global_var('func_1771')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_4095 = func_1771_call()
call_4096 = func_1771_call()
uop_4101 = relay.acosh(call_4095.astype('float64')) # shape=(9, 12, 1)
uop_4103 = relay.acosh(call_4096.astype('float64')) # shape=(9, 12, 1)
output = relay.Tuple([uop_4101,])
output2 = relay.Tuple([uop_4103,])
func_4104 = relay.Function([], output)
mod['func_4104'] = func_4104
mod = relay.transform.InferType()(mod)
mutated_mod['func_4104'] = func_4104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4104_call = mutated_mod.get_global_var('func_4104')
call_4105 = func_4104_call()
output = call_4105
func_4106 = relay.Function([], output)
mutated_mod['func_4106'] = func_4106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3700_call = mod.get_global_var('func_3700')
func_3702_call = mutated_mod.get_global_var('func_3702')
call_4129 = func_3700_call()
call_4130 = func_3700_call()
var_4150 = relay.var("var_4150", dtype = "float64", shape = (9, 12, 11))#candidate|4150|(9, 12, 11)|var|float64
bop_4151 = relay.mod(call_4129.astype('float32'), var_4150.astype('float32')) # shape=(9, 12, 11)
bop_4154 = relay.mod(call_4130.astype('float32'), var_4150.astype('float32')) # shape=(9, 12, 11)
output = relay.Tuple([bop_4151,])
output2 = relay.Tuple([bop_4154,])
func_4165 = relay.Function([var_4150,], output)
mod['func_4165'] = func_4165
mod = relay.transform.InferType()(mod)
mutated_mod['func_4165'] = func_4165
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4166 = relay.var("var_4166", dtype = "float64", shape = (9, 12, 11))#candidate|4166|(9, 12, 11)|var|float64
func_4165_call = mutated_mod.get_global_var('func_4165')
call_4167 = func_4165_call(var_4166)
output = call_4167
func_4168 = relay.Function([var_4166], output)
mutated_mod['func_4168'] = func_4168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3524_call = mod.get_global_var('func_3524')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_4200 = func_3524_call()
call_4201 = func_3524_call()
func_2538_call = mod.get_global_var('func_2538')
func_2540_call = mutated_mod.get_global_var('func_2540')
const_4239 = relay.const([2,8,-1,4,4,3,8,7,-1,2,7,10,6,-8,-8,8,10,-7,-1,-10,-10,8,5,6,8,-1,5,-7,-3,-2,7,-10,8,-7,8,-5,-10,-6,10,-1,1,-5,3,-7,-6,-5,1,-7,-3,-9,2,9,8,-9,7,-9,9,-5,8,9,3,7,9,4,-10,3,8,6,-7,-6,-2,-3,1,-5,1,4,-8,-9,-5,-1,7,-7,-5,-5,-5,-7,6,-1,-9,7,-10,6,-10,-9,8,-9,3,2,-6,-8,-7,-1,-4,-1,9,-5,-7,-9,3,-3,7,8,6,5,8,-5,10,-8,-8,-7,7,6,-2,2,-4,-6,6,10,-3,-6,-2,-6,6,-5,2,-1,-6,4,3,-3,2,-9,-3,-4,6,9,-10,-8,-8,-1,9,-1,9,2,3,1,7,6,1,-10,10,4,-6,-8,-9,7,3,4,-5,-5,4,-4,8,-2,-1,-5,-4,5,-3,-4,-4,-10,-1,8,-3,-4,1,-7,-9,-5,3,-5,10,5,-3,-8,10,-1,-4,-6,-3,3,8,10,-1,2,-8,-1,7,4,4,4,-1,6,-7,2,5,-2,5,2,1,-10,-1,5,-6,5,-10,6,7,7,-8,-3,-4,6,9,7,-4,-8,7,-2,-2,-5,-9,4,-4,-1,9,5,-1,5,3,-1,-9,3,-2,-1,5,1,-6,1,7,2,7,1,10,-9,6,-9,9,-10,-8,-9,6,6,-4,-4,10,9,5,3,-4,10,2,-6,1,4,-9,-2,-1,-9,-7,8,-8,5,4,9,-2,-9,-8,5,-3,3,-2,-6,-5,-9,-5,2,-3,7,6,-7,-6,-3,1,8,-9,-5,7,-5,8,7,-1,9,9,-3,-5,-5,7,9,-8,-4,-7,-7,4,-9,7,8,-6,-4,-4,-1,-7,1,-4,4,7,-8,-10,-1,8,9,-5,-3,-3,-7,6,-7,2,-9,-8,6,-2,2,-1,8,-4,-7,3,9,9,-4,-3,7,9,-10,8,6,4,4,2,7,7,4,-3,6,10,6,3,9,-1,10,-8,-1,-6,-6,-5,4,-6,-3,-3,1,-1,9,4,7,-8,5,5,6,1,10,6,9,4,1,3,5,10,-9,1,-10,-2,2,-2,-7,-2,-10,-2,-2,-3,8,-4,-1,6,-1,-5,-5,-7,-4,-7,6,9,10,5,8,5,-5,8,5,7,8,-8,-10,-1,-8,5,-10,7,4,1,3,9,-7,5,10,2,5,2,-5,-10,-1,-6,-7,-10,7,6,-9,8,-3,-2,7,10,3,9,-5,2,4,-7,-9,4,8,5,-5,7,-10,-1,-2,10,5,5,10,7,3,3,-3,-9,-6,-10,1,-1,6,-7,4,-6,-9,-10,6,1,3,3,-2,9,-9,1,6,-9,5,-5,-3,10,9,1,9,-5,7,-10,-10,-6,-8,9,10,-8,-3,-4,3,-10,-3,-8,-4,-5,-2,-7,4,3,10,-5,9,-5,-6,3,-4,2,6,10,-4,9,9,-8,9,4,3,-2,-3,-9,10,8,6,9,-9,-10,-3,-9,-6,7,10,7,-9,10,-9,-2,-10,3,2,8,3,6,-10,10,4,1,9,9,-10,1,-5,-10,-5,3,-5,1,-2,5,4,7,-5,1,-8,-3,7,-10,6,1,1,9,8,7,6,1,-7,7,-7,-5,9,3,-1,10,3,9,7,3,9,-5,-9,-5,3,10,10,-4,3,-5,-2,-2,-8,8,-10,-3,10,3,4,-8,10,8,-5,-9,2,5,-10,-7,-1,-4,-8,1,4,-7,-4,7,5,5,8,10,-7,3,3,6,7,-6,-8,2,1,-2,6,-10,-5,-1,-9,6,-10,-3,-1,9,-10,4,10,-8,5,7,-1,2,-9,10,6,4,-5,8,-8,3,-2,4,2,4,-3,-1,-7,10,-6,6,8,-9,-8,10,-6,2,1,1,-9,3,7,8,-6,1,-1,-5,6,-4,3,-10,7,6,-9,1,3,2,9,5,8,-7,-3,-8,8,-5,3,7,-7,-8,-1,4,5,3,6,9,-6,-3,-1,-9,-10,-10,-8,-5,-2,-1,1,7,1,-10,-10,3,5,4,-6,7,-9,-2,-7,-2,-7,-4,-10,4,10,10,-3,5,-10,6,-4,-5,1,10,4,7,-6,-2,1,-8,10,-3,3,-10,9,-3,10,-7,-5,9,10,-3,-6,-5,-10,9,2,-4,-2,-2,-2,-5,2,3,9,-9,9,-7,6,3,-4,-8,4,5,-8,-6,-1,1,3,3,8,-10,3,-2,-9,6,5,2,-8,5,6,-6,-4,-10,-3,-8,-4,-5,-8,-5,2,-2,5,-6,3,-9,-5,-3,4,-6,6,-7,4,7,-1,-9,-2,-9,5,10,-9,4,-3,-4,2,-1,6,9,2,-2,-8,5,9,7,-9,1,-5,3,2,3,9,-2,-4,5,-9,-10,-7,9,8,2,-4,-7,-8,6,-10,-3,7,-4,-8,-8,5,8,-2,9,-4,9,-4,8,7,-3,5,7,-3,4,1,10,1,-1,-4,2,1,-9,-8,-8,-3,3,7,1,-5,3,6,-6,-1,9,-5,-7,-2,3,1,6,-2,-3,3,1,6,3,-7,-8,-4,-8,-8,7,-1,-2,2,8,1,3,3,1,7,-1,3,-7,-4,9,-9,-4,7,-5,-5,2,-2,9,8,5,4,-10,-5,5,1,3,-2,-2,-4,9,8,5,-6,-7,4,10,8,-4,-10,-4,5,-2,-6,-6,-1,-2,-8,-1,1,1,-8,3,4,2,-6,-2,6,8,10,4,10,-10,-1,3,7,-9,-6,4,10,1,-2,7,-8,-10,2,10,8,-10,-1,4,8,4,6,1,3,1,4,-3,-4,3,-7,-8,2,-7,-3,-10,4,3,3,-5,-6,2,-4,-6,-8,-6,1,3,2,-4,-10,-5,8,6,4,8,8,1,4,4,-6,8,-4,9,-10,-2,9,9,-7,-1,-8,10,8,2,9,-6,6,-2,-5,-8,-6,-9,10,-4,-3,-6,3,-9,-9,5,-6,-3,-6,-3,-8,8,-5,-10,-5,2,9,-10,-5,-5,9,2,-2,-8,-2,1,-5,-5,-8,-5,-9,-10,6,1,9,6,6,5,-3,-8,5,-6,-2,9,7,-2,1,-5,2,-6,9,-2,10,-7,-10,1,-6,-6,-9,8,-8,-2,-2,6,2,6,-6,10,-6,10,-2,3,-7,8,-3,3,5,-2,4,-1,-10,2,7,-3,-9,-3,3,2,-5,9,7,3,9,10,-3,-2,10,-10,-5,4,-5,6,-2,-9,9,9,10,-9,-7,-4,2,5,1,-10,8,2,-2,-1,-7,3,10,3,6,-9,-2,5,-1,5,6,8,-1,5,-9,8,-9,-3,7,-7,7,-5,-10,-3,1,-3,-5,-8,9,2,10,-3,4,-5,1,1,-1,7,7,4,-9,-2,6,-3,-3,-1,6,1,-10,-9,10,9,8,-3,-7,2,2,10,-4,-2,-7,-10,-9,-5,5,9,5,7,3,8,-6,6,4,7,9,5,-4,-3,3,-3,-1,4,-8,7,10,3,-6,8,-5,8,-6,-1,7,5,-1,8,1,-6,-4,4,10,4,4,-8,6,-4,10,-3,1,-6,-8,-4,8,-10,5,-8,9,3,-1,6,-8,10,-8,-4,2,-1,4,-1,-7,5,-5,7,5,1,10,5,-8,5,-9,4,8,-4,-5,3,8,-2,-2,-8,8,5,9,-7,7,2,2,9,-5,10,-10,10,4,-10,2,3,1,9,2,-6,9,-6,6,-10,-2,9,-7,9,-2,8,-9,3,1,-10,7,3,-4,8,6,-10,-10,10,9,-7,-10,-4,-5,9,-10,-10,-6,4,2,9,10,6,-10,7,6,2,-8,5,7,1,4,4,-2,10,-2,2,10,-4,-4,2,5,-6,-4,8,8,9,-9,-1,-3,5,-4,9,-4,-6,4,-2,6,3,10,3,9,9,-5,10,-5,-5,-1,3,-7,-8,9,-1,-8,6,4,-6,-1,2,7,-8,-7,1,7,-7,-5,7,-5,-2,3,-10,7,-1,-3,8,6,-2,7,3,1,8,5,1,-4,-2,1,3,10,-10,-8,2,-2,-9,2,-3,-3,9,6,9,-5,6,-3,-5,4,5,-2,8,-5,-3,10,-10,-6,-3,10,-2,-1,10,9,8,-1,-7,-1,-6,-5,-5,-4,-8,-3,3,-2,-6,-7,-8,2,-2,-10,7,-6,-10,-4,6,10,-10,-6,4,-10,-1,-7,-3,-5,-3,6,8,4,2,3,-8,5,-5,1,-9,10,-7,-10,-7,7,-2,9,-4,-8,-3,-6,5,10,-2,-9,-1,-10,-5,1,7,-1,1,-9,-5,3,9,10,1,-3,-1,4,1,-4,-4,6,5,10,-9,10,5,1,-5,9,-3,8,7,9,6,4,-8,-3,10,-10,-2,3,6,-3,-7,6,9,7,4,5,9,1,-2,2,-8,10,-5,-7,-9,1,-7,7,8,3,9,-3,-7,-8,1,-10,-4,-10,5,9,2,-9,4,-4,-1,-6,4,1,-8,-10,-10,-9,-1,3,-8,10,-10,-8,9,9,-8,-2,-8,4,3,6,-4,-8,-6,3,-1,4,5,8,-4,2,5,6,9,9,6,5,-10,7,2,-10,4,-6,5,-3,-4,5,-10,-3,3,-1,9,8,-9,-5,-6,5,10,9,9,8,-8,3,4,-7,9,-3,-3,8,-6,2,10,2,-1,7,4,5,8,9,3,-6,-3,-3,-10,8,-5,-9,-8,-7,3,-10,1,10,3,-1,7,-3,8,7,-6,-5,-5,-8,-5,-3,10,7,1,3,7,2,-3,4,-8,1,-8,-7,-1,6,-1,-6,4,-6,-1,9,-5,3,4,9,-10,10,-7,9,-1,5,5,4,-5,4,-9,3,4,2,-3,1,-3,1,7,9,-8,1,6,-3,-6,-6,-2,1,-6,3,5,-5,7,8,10,2,-4,1,10,10,3,-3,6,10,-6,-1,8,-9,4,9,-9,-1,-5,2,6,-3,9,-1,-9,-4,3,8,-3,-8,-8,-2,9,-9,-6,2,-4,-9,1,5,3,7,-9,9,3,3,-6,6,8,2,8,-4,-10,-3,-4,-3,2,-3,4,-4,-1,6,-2,3,-10,4,10,10,2,1,4,3,5,-8,1,-5,1,-8,-8,2,5,-7,3,-4,-1,-1,10,-2,3,5,-5,6,4,8,-6,-1,6,7,5,6,-10,-2,2,-7,-7,-1,-3,-8,-3,-8,-9,-2,-6,6,-2,-9,1,3,9,-10,-2,-1,-8,-1,-5,1,-7,1,-4,7,1,-8,-9,-6,3,-7,7,-2,-4,9,10,-5,3,-10,-3,2,-3,6,5,10,-8,-5,-4,-1,7,-10,-9,6,1,8,-5,7,3,9,5,-6,-8,-9,7,1,-9,-3,-5,10,-6,-9,-7,8,2,-7,-9,-2,-3,9,1,6,-10,8,-9,-1,-5,6,9,-3,1,9,-1,9,4,-6,8,4,-10,-3,-1,3,-5,9,3,4,-9,6,-6,8,10,4,3,-6,-10,-1,3,6,-1,9,-6,9,-10,9,-9,7,-8,-9,-8,-5,4,-1,8,-3,4,-4,-7,-10,-8,-4,-6,6,9,-7,10,7,-6,9,8,2,5,4,8,10,3,-3,-4,-2,-6,-2,-1,-10,-9,-2,2,1,-1,-3,9,5,7,8,8,-4,1,1,-7,2,10,5,9,3,-2,-8,-10,-2,2,-8,-2,-5,2,-4,6,7,9,2,-1,-7,-9,-4,2,6,4,6,-8,-8,8,-1,9,4,1,7,1,5,-10,1,-2,8,2,-3,-5,-3,4,-9,2,-10,-9,5,2,-2,-8,6,1,-8,-6,-5,2,5,-4,9,-8,-10,-6,9,-6,2,-5,6,10,10,6,8,5,-4,-8,4,-3,-4,-9,9,-5,1,-7,5,10,-5,3,4,5,-7,-2,8,7,-4,-5,4,-4,-2,-10,10,4,-6,-7,5,10,-6,4,6,5,10,3,-4,6,9,2,-8,5,3,6,-5,-1,9,-4,-9,-6,-1,-2,7,-10,6,6,-10,1,2,-3,-6,-7,-4,-9,-9,3,-6,-4,2,9,-6,5,-3,-9,-6,1,1,-4,-6,7,1,-5,4,2,-5,-6,-8,-7,9,-6,-2,-6,5,-5,6,8,1,-4,5,3,-9,-1,1,-7,-5,5,2,-10,3,9,9,-5,-3,7,7,7,8,2,-7,-2,-4,2,10,4,-9,-1,2,-1,8,-2,10,10,9,-9,-3,-1,-8,4,6,9,2,-6,-9,9,8,10,-3,6,-6,-8,-4,5,-5,9,-6,-9,-10,3,3,-7,-3,7,-9,8,7,-4,9,4,6,-5,4,1,6,-5,5,-10,-1,6,9,7,4,-9,-1,-6,8,9,3,8,-3,-10,7,7,-6,-9,-9,-3,8,-5,-6,-5,-2,8,4,7,-1,6,-9,-7,7,2,-4,8,-8,8,6,8,-10,3,4,-3,-9,4,-3,-4,9,-6,-2,3,-1,-6,6,3,2,-10,-6,-1,2,-4,6,-5,6,8,-8,-10,5,6,-1,7,-4,2,-2,6,8,-8,8,1,-7,-1,-3,-5,-8,10,-9,5,-8,3,9,3,-7,-4,-6,-8,8,-9,-10,-9,-5,-10,-8,8,-3,5,8,1,-2,-2,-4,3,-8,2,9,6,10,8,10,-5,7,-7,1,4,-5,-2,-5,-8,9,2,-1,2,6,-3,-8,-9,2,3,4,-9,-4,-5,-7,-3,-6,4,3,1,8,6,-4,-4,-3,-2,-4,7,1,6,-6,4,-4,-9,4,8,8,9,-3,8,10,4,-10,-2,2,9,-7,-1,-1,9,4,7,-3,4,9,-1,-4,1,-5,-5,2,-6,6,1,-10,3,8,-4,6,9,9,-2,-7,7,9,9,-7,-10,4,2,-2,8,5,-4,-9,8,-3,3,7,-1,5,8,7,-6,-9,-5,-3,4,-4,-1,-1,2,-9,-5,-8,-3,-8,-4,-8,8,-7,2,-5,-8,-7,3,-7,-4,-2,5,7,1,-6,2,5,3,4,-2,4,-7,8,-8,5,-3,3,6,-5,-7,4,-7,1,1,-7,-4,2,9,3,6,1,6,-9,-4,-1,-5,2,6,-2,-9,-9,-8,-6,4,4,1,1,-9,-2,-3,6,2,10,3,4,-10,7,-5,-5,-6,8,4,5,-2,-8,3,-2,2,-2,3,9,8,-1,10,-1,7,-2,-1,-4,-7,9,-6,5,-3,5,3,-1,-9,-4,-10,-3,-8,-8,5,3,4,-2,-3,8,-3,3,-6,-7,-9,-4,-9,6,4,-6,5,1,-9,8,7,7,-9,-8,-7,10,7,8,2,3,7,-7,7,2,8,-8,-7,8,7,1,-10,-3,8,5,5,-6,-5,9,-10,10,2,-6,4,5,8,7,-10,7,2,-5,-7,-3,7,-6,10,6,3,1,6,9,3,-3,6,8,-9,-7,8,-9,-10,2,1,4,-2,1,2,-1,6,7,-4,-4,-1,-9,2,6,5,4,7,-9,-6,6,-10,2,-3,-2,7,9,-6,9,-8,-10,2,-10,5,-8,10,8,1,6,2,-10,-3,-6,-9,6,9,-2,-9,10,10,4,1,9,-3,-7,-4,-3,6,-5,6,2,-7,-6,7,-2,-3,-6,-10,6,2,10,10,5,5,-3,-1,-6,-1,5,-6,4,3,4,7,-9,-5,6,-2,-3,1,8,3,10,-4,-10,2,-10,6,-8,-3,-3,-6,6,-2,-5,-7,6,-6,-3,-1,-1,-9,-8,6,-7,5,-9,-10,8,-6,-4,-5,2,-7,4,-8,-1,-7,-3,6,-3,-9,-1,9,-1,-2,5,-5,3,-2,8,-1,10,-9,-10,-2,-6,-7,-1,6,-1,-7,10,-5,-2,7,10,10,-5,-10,3,-1,-4,6,7,7,2,8,6,4,-2,-7,-10,-2,-7,3,-6,-7,-3,8,-4,-9,9,-10,-1,-2,-7,7,7,2,2,3,10,-8,4,-4,-3,7,-10,-6,1,-8,-8,-4,2,10,-3,-2,5,-5,-8,-7,2,2,1,7,-7,-10,9,1,-2,-5,-5,10,-9,-1,6,5,-4,-1,4,-6,-4,5,2,5,8,-1,-7,5,7,-2,-3,-10,3,-1,1,5,6,7,5,-2,-1,5,5,5,-5,-5,-3,5,-6,10,-6,3,6,-9,-3,5,-5,4,-2,4,-6,-8,-3,3,-9,-7,10,6,3,1,6,1,-6,-5,-6,8,7,-10,-6,2,-8,10,-10,-5,2,8,-2,1,-4,8,3,-1,-1,3,-4,5,-3,-9,3,-7,-10,5,3,-1,10,8,-5,-8,-10,6,-5,3,7,-2,-7,-7,3,10,6,5,-1,1,-2,2,1,3,8,5,-9,6,-5,5,-5,-6,-4,-8,3,-1,-10,4,-3,-7,-4,-6,9,-9,7,4,8,-2,8,9,9,4,-5,3,7,6,-2,4,-6,-8,8,-2,2,9,4,-1,10,-6,-8,-10,9,-6,-10,-4,5,9,4,10,-5,-5,-8,6,4,10,9,6,-10,8,-5,8,4,5,-9,3,-5,5,-7,-1,2,-4,5,-8,-4,-7,-9,-1,2,-1,3,7,4,-1,-2,3,-6,-5,-1,-6,-9,6,-7,3,4,-2,-9,5,10,6,10,8,-8,-5,-7,-4,3,6,-8,1,2,9,4,-5,-1,10,10,-5,2,7,-10,-6,10,5,1,-10,-3,4,-2,-4,10,4,2,8,1,1,-8,-6,-1,6,9,6,-6,1,-1,-3,-7,-1,-8,2,6,-1,-2,-3,-8,-4,-7,-10,1,3,6,-3,4,-1,4,-10,-7,-5,5,-2,8,-1,6,-10,-5,-1,8,4,-9,-4,8,-5,2,6,7,2,5,2,7,10,-4,2,8,-6,3,-2,-4,10,7,5,3,1,5,1,7,5,-6,-5,-5,9,-1,-10,8,-2,5,10,7,8,-7,3,2,-5,-6,-1,1,8,-3,-8,-8,7,-8,-3,-8,-4,-10,7,6,10,-2,1,-5,7,9,10,-4,3,1,4,7,-4,-8,10,-3,-3,3,8,5,5,-9,-3,1,-4,2,-4,9,-5,-9,8,-5,-4,-7,6,8,-5,-6,1,-4,2,4,-4,-1,7,-2,-9,7,5,8,5,-1,-4,-1,-6,7,-3,-1,-3,4,4,6,-4,9,-7,9,4,2,-8,-10,-8,-4,9,7,-10,3,-8,-7,3,10,-4,10,10,5,-5,-4,-3,5,4,3,3,-9,-6,1,-2,-7,-1,-6,1,9,-8,10,-3,-3,-4,-2,4,-8,-8,10,-4,-8,-4,-6,-6,2,9,-3,-6,1,7,-9,-5,-3,-7,-2,-10,6,3,-10,8,-10,5,-1,-4,-10,-4,-1,-7,-1,-7,-5,-1,10,10,2,-3,7,8,6,-8,2,-9,-2,-9,-9,6,-3,5,-1,-3,-5,7,-4,-7,8,1,1,3,4,-8,8,9,9,5,10,-4,6,-4,8,-1,1,6,-1,7,3,-10,-7,2,-2,-9,7,-7,7,-3,7,3,7,-9,-8,-4,2,-2,3,-9,3,7,-3,4,8,-7,3,-2,-9,1,-9,-8,8,-4,-6,-6,-2,8,9,-7,1,-1,-6,-7,4,-2,-2,8,10,1,-6,2,1,-5,-4,-9,-10,1,3,-9,-7,-2,1,9,1,-5,8,-4,1,-1,-6,2,-3,10,-3,3,-1,-9,6,-4,-9,-5,-8,5,-10,6,9,2,3,5,2,-5,6,5,-3,10,-8,8,4,7,2,-2,3,10,-5,-1,-5,-9,-4,5,-3,-1,8,9,5,-7,-1,-5,-4,-10,1,7,-10,9,3,3,-8,7,6,-9,-3,-7,7,7,-8,-10,8,9,6,-4,-3,-2,-3,-7,6,9,4,4,-7,-3,-9,4,-2,7,-2,-6,-10,-3,9,4,-6,7,-9,1,3,1,-1,-9,-9,-1,-9,-3,5,-4,6,4,-10,-1,-1,5,8,-5,-10,-2,-3,7,1,-3,-7,-3,-6,6,7,7,2,3,5,-1,-2,-3,7,7,1,6,-8,1,-7,1,6,3,7,10,-4,6,-3,9,8,-7,5,-7,6,6,-6,-7,-3,10,6,2,8,-6,-5,-10,10,-4,-5,-9,-8,2,3,6,-10,6,8,-6,5,7,6,7,-9,4,-9,-2,-9,2,-4,8,5,-1,-3,1,-10,2,-8,-3,-7,8,1,4,4,10,2,-3,-3,2,-3,3,-1,-9,-1,5,-1,-5,-3,-10,3,-5,9,6,4,7,-10,1,5,-2,4,6,2,-8,10,-2,-10,-10,6,-1,3,-8,-8,8,-8,-2,10,10,1,5,-5,-6,5,-6,-3,3,-6,-3,-9,10,1,-4,1,-1,9,6,4,-9,-2,-3,-1,-3,7,-1,-6,8,4,6,-3,10,4,5,9,-10,8,-8,-10,-8,-6,7,-2,9,6,-1,-4,-2,6,8,-3,8,4,2,6,10,9,-4,-2,-6,8,-9,8,-3,-3,10,3,-7,4,8,-1,2,8,2,-8,-2,8,3,5,10,10,3,-10,10,-2,-3,-9,-5,-2,-10,-5,-1,4,-9,-9,-6,-1,-4,-1,-4,-3,6,-4,10,7,-8,-2,7,10,-6,7,2,3,8,8,-7,-10,2,5,2,4,6,7,-6,1,10,6,-7,-7,4,-10,-6,-7,6,4,4,6,-6,5,-3,-3,-6,6,9,2,-9,-8,3,-5,7,-5,-7,-3,7,6,4,-5,-10,6,6,-5,-8,-2,-8,2,-8,8,-9,2,-9,-7,8,3,-5,-7,5,-6,7,-6,8,-10,-4,-4,1,10,-4,1,7,8,-1,2,9,10,7,10,-5,-2,1,3,-1,10,-8,-5,-4,-8,10,-2,-8,-4,10,10,6,-4,7,-9,-8,4,-1,-2,6,2,2,6,6,-4,-5,2,6,8,-3,4,5,9,10,1,-5,-3,-6,-6,-10,1,-7,-7,-10,8,10,-7,3,1,9,-1,-4,1,5,6,-8,-1,1,9,4,5,1,-9,9,-8,-3,-5,3,-8,-3,-4,-1,-5,-4,6,-2,-2,-2,-7,-4,-1,6,-3,-2,-7,-5,-6,-7,-9,-5,-1,-5,-2,-7,-9,-6,5,8,2,8,5,-2,8,-1,-2,-3,5,-7,6,-6,4,-9,5,-6,-5,8,-8,10,2,4,-8,-7,6,10,10,10,7,3,-5,10,-5,-2,9,-8,3,-4,-8,6,9,-7,1,2,-5,1,-6,-1,-1,2,5,2,-2,1,-9,8,-4,-6,-2,-4,-5,-8,7,-2,4,-8,-5,-7,7,1,-6,6,3,4,2,4,-2,-10,4,5,9,-7,6,-5,3,-2,4,8,2,3,-9,-3,9,-9,-7,-1,10,3,3,10,2,6,10,3,7,7,-3,6,-6,-9,9,-1,9,8,10,9,-10,9,-10,-5,10,-2,4,9,2,3,7,4,-6,9,10,1,2,1,4,-10,8,1,1,-2,-7,6,-8,1,3,-1,5,-3,4,2,2,4,3,1,-5,-7,-7,8,5,9,-9,-1,2,5,7,-6,7,-8,5,-4,-2,7,-8,-5,6,1,4,-10,-5,4,2,3,-10,-10,2,-7,9,-4,-1,-9,2,-10,1,7,-7,-10,-3,-8,5,9,-6,-2,2,-1,4,10,2,-6,-4,-1,-6,-9,5,1,7,-7,-8,-7,6,5,-8,8,7,-2,-7,-1,5,9,9,-2,-3,9,-10,6,-4,6,6,-1,7,5,8,4,-5,-3,-6,1,6,3,-6,-1,-9,-2,10,9,7,-1,9,-8,10,-1,8,8,-3,9,-9,8,7,3,3,5,6,-5,-1,1,6,-10,5,-8,8,-6,8,-4,-3,-4,-1,-6,-5,3,-6,9,-8,6,-6,10,4,4,-1,8,-5,10,-1,4,9,-2,-4,5,-10,5,-7,-2,2,-2,-4,7,-3,7,5,-10,3,-7,10,10,7,6,2,-5,-5,7,9,1,3,6,3,2,5,-2,-5,7,-8,4,-2,-4,7,-8,-7,8,1,2,9,10,5,-1,6,10,10,6,6,10,-3,-8,7,4,10,-2,10,-5,5,5,3,-5,-1,6,3,1,-2,8,-4,7,-8,5,10,3,5,7,3,-4,5,4,-3,3,3,-9,4,3,7,-2,-7,2,-2,3,-1,10,6,-3,8,-6,-7,-9,1,7,-1,4,-1,-1,5,8,10,3,3,-5,-10,-3,-8,-2,-4,8,5,3,-8,10,-10,-1,-6,8,-10,2,6,9,-6,4,7,5,-1,9,-5,-7,5,9,4,-5,-10,4,-2,1,-5,10,-6,3,5,9,1,9,5,1,5,4,3,-3,-3,5,-9,10,-1,-3,7,10,-9,5,-7,1,-2,-7,-3,2,-5,3,-3,1,10,-2,-7,4,-9,10,-7,8,-8,-4,5,8,-2,-6,-6,9,-1,2,3,-4,6,8,6,3,-1,4,5,-6,3,-10,-8,-4,9,-9,-3,-5,-8,2,-1,6,6,-7,-2,-5,-6,-5,-5,-7,4,-7,10,7,8,-2,6,10,9,-10,4,-5,2,7,8,4,-2,10,6,10,7,-3,-1,7,-4,-1,4,-9,8,6,1,-2,4,5,-9,3,8,-1,1,-8,-4,-3,9,-5,-9,-4,4,3,8,-9,2,3,10,-8,-9,-7,-7,1,2,4,-8,2,-4,9,3,-9,2,5,-5,4,-9,-8,1,4,-3,5,-7,-3,-1,3,10,9,5,3,-4,3,-8,-2,10,2,-2,-5,3,-10,-10,-8,-6,-4,8,-8,-4,10,3,3,-7,7,4,-10,1,3,4,6,8,-8,7,3,-10,7,4,-9,7,-2,-1,7,-2,-7,-4,6,-3,8,-2,-5,-3,-8,-2,-8,4,-9,-10,-6,9,-1,-6,-4,-9,1,3,-6,8,-1,-2,9,-9,-10,7,3,1,10,9,6,-4,1,-5,-6,-2,5,-8,-9,-5,5,-5,9,-2,-3,10,-1,8,-6,3,-8,-8,9,7,10,5,3,6,7,-10,-1,10,7,-5,3,-4,3,3,-6,9,2,3,-3,-9,7,1,-4,-1,2,-3,-6,-7,-8,2,-1,-10,-3,2,4,-8,-5,-10,-1,9,6,10,8,2,8,-10,3,3,6,5,9,10,4,10,-10,-9,-10,10,-6,5,-6,-2,8,-8,5,2,-9,-7,-4,-8,-5,-1,-6,4,-5,6,6,4,-5,6,-6,-3,5,-7,6,-1,10,5,-5,8,8,3,1,-5,2,8,4,-2,-1,5,-4,-6,10,-2,10,9,3,-9,-1,-5,-8,10,4,10,-3,-3,-3,1,2,-10,-1,-10,1,3,6,5,-10,-7,-9,2,-3,-6,5,10,9,2,1,8,-3,-5,8,-6,-5,5,-1,-5,-3,1,-8,-9,-2,-9,-5,6,8,9,-9,6,-10,-9,9,5,5,-2,-8,-10,-2,-5,5,-4,-1,1,-10,8,-8,-2,1,9,-5,6,1,-6,-4,9,10,-2,-8,3,-10,9,7,4,-9,3,5,-9,-5,9,-6,9,-2,1,6,10,-6,-5,-10,-1,4,-5,3,-5,-1,-10,-3,-6,-1,-4,10,6,-3,-1,2,2,-5,-4,4,-9,-4,-3,9,1,-6,-1,-9,4,-8,2,6,3,-4,-4,-8,3,-3,10,-6,3,6,-10,-9,-6,9,4,-4,1,-7,8,9,1,8,5,4,7,10,-4,2,-5,-8,8,-7,1,5,1,-1,-5,4,4,-8,8,8,8,-2,9,-3,3,8,-5,-5,7,1,-6,4,4,3,-9,-4,9,9,7,6,3,5,-7,6,-6,-5,-3,6,-10,-9,-8,-5,10,-6,9,6,8,-2,2,10,-7,4,-4,7,-7,-5,9,3,-6,-6,-1,-7,-6,5,-8,-9,9,-5,4,-1,8,10,-5,-7,-2,-8,-7,-3,5,-2,2,-8,-7,-8,-6,-5,-2,-4,-8,10,5,-2,-2,-7,2,7,-3,6,1,2,-10,4,10,1,-10,-7,-6,7,-1,-4,-4,-8,8,-6,8,6,2,10,-7,-1,1,-2,-6,-6,3,-1,-10,1,-3,-9,-4,-8,7,10,10,-3,-9,7,-3,-4,2,-3,-4,-2,-3,5,6,-2,3,6,-3,-2,3,-10,4,-3,9,9,-10,8,2,9,-9,10,4,5,5,2,9,-4,-5,-1,3,-6,3,-6,-1,4,7,4,-1,9,-6,-6,4,-10,-7,3,-3,2,-7,2,3,-10,1,2,-10,-10,5,-3,-5,9,-6,-1,5,6,4,-10,3,7,-3,-5,-3,3,-10,6,9,-7,-10,-5,-4,7,-6,-4,8,-2,4,5,-2,-5,5,8,-9,-1,3,-1,5,-6,-4,2,4,2,3,5,-8,-8,4,-6,-10,9,3,4,-10,10,1,-6,6,-4,7,-4,2,7,9,8,-2,-7,-8,6,-1,4,10,10,-9,-5,-6,1,-5,5,-4,5,9,-3,-3,7,-7,8,10,-3,4,3,-9,9,3,-9,-6,-4,-8,-6,-8,-7,-1,-10,4,-7,-3,8,7,7,-1,8,3,-6,9,-2,-4,-1,3,-5,-7,5,5,2,-9,3,-7,9,2,-1,-7,7,-1,6,2,-10,6,-6,9,4,-1,9,-9,-8,-6,-4,-1,4,-1,-7,-4,9,4,-2,7,8,4,-4,6,5,-2,-6,-2,-4,-3,-6,-7,8,4,4,-7,-7,-2,5,6,1,-1,-10,7,7,-6,8,2,7,-9,5,-3,-6,-7,4,-1,1,10,-4,-9,9,-6,1,7,1,-8,2,3,8,-9,3,-5,-3,-10,-2,-7,-4,-9,8,2,-10,8,-4,9,2,4,9,2,4,8,10,-8,10,-7,3,-10,10,4,10,5,3,-7,-9,-6,-10,-1,-2,5,8,10,1,-4,-7,-4,4,-7,9,1,3,-2,-2,5,4,5,2,-5,5,-6,10,9,1,2,10,-9,1,-7,-4,8,-2,2,-2,9,-8,10,-6,5,7,-9,-1,1,2,6,10,-6,10,-10,-6,-10,5,6,10,-1,9,3,10,1,-4,8,2,8,-3,-4,9,-7,5,6,-5,2,6,-3,3,-6,4,1,-9,9,9,-5,7,-1,-7,10,1,-7,1,-3,7,-9,5,-6,1,10,-9,6,-7,10,5,8,-4,-3,7,7,-7,-5,-8,-9,-6,-7,-4,-3,-4,-8,5,-5,3,3,-5,-3,7,-5,1,-4,-4,2,-7,-2,-1,8,-6,-4,2,-6,8,-9,9,1,-9,7,-7,-3,7,5,-4,2,5,-7,-5,-6,-6,9,-9,5,5,-3,-2,-7,10,7,-5,3,6,1,-7,-4,9,10,2,-8,-9,1,5,-2,-2,-10,7,10,-5,7,-5,-7,-2,4,2,5,3,3,-8,5,-4,-8,6,6,-7,5,4,8,-7,-2,-6,-10,-4,7,10,1,-4,-6,-5,6,-7,-7,3,9,-8,8,-7,-3,3,-3,1,-8,-1,7,-1,1,4,-9,1,-6,8,-5,4,7,7,10,-2,-2,3,10,-2,1,8,4,9,-10,-6,3,-2,-5,10,4,-2,-6,6,8,-6,-8,1,4,2,7,1,-5,-10,-10,6,2,-2,4,4,-8,2,-7,-7,-3,4,-4,1,8,10,4,1,3,-6,-3,-8,3,8,5,10,2,-9,9,-6,1,-4,-1,3,-10,2,1,4,-1,1,-8,3,5,8,10,-2,1,8,-4,-7,-1,-8,8,6,4,5,-8,-4,10,10,8,-3,-9,3,5,8,9,-8,-9,8,2,7,-4,5,-1,-4,-7,7,1,1,-2,-1,6,9,6,9,5,-9,5,2,9,6,-4,-5,-7,-2,5,9,5,-7,7,8,-1,10,-1,3,-8,-7,6,-1,6,9,7,5,7,-2,7,6,-6,-6,-9,-6,-10,3,-5,-8,-6,-4,-6,-4,2,-9,3,-9,-4,-6,3,-1,-5,8,9,-10,-4,7,-5,3,6,-8,-7,-7,-1,-3,-7,9,1,1,-5,4,-7,-7,3,-2,4,-7,9,2,-9,6,1,7,3,1,-8,5,-9,10,6,8,-1,1,-9,10,9,-3,1,4,5,-2,-4,10,3,3,1,-7,6,-2,10,4,-8,-10,4,-3,-1,6,3,-9,6,-4,-3,9,9,-8,-5,-6,7,2,-2,-4,9,10,-6,8,1,8,3,5,1,8,-6,-9,-2,6,-5,9,-10,7,8,-7,5,2,5,9,3,-3,4,3,4,-4,-2,4,3,-8,-5,9,2,-10,-3,4,8,6,-3,10,2,6,-8,-8,2,-2,-2,-10,4,-1,1,-4,7,3,-1,-5,8,7,-4,6,2,6,1,-8,6,-4,9,7,6,-3,-4,9,4,7,10,5,-1,8,6,9,-7,2,8,1,-9,2,5,-5,-7,6,-6,-1,-3,-1,5,3,-10,10,-4,4,7,7,7,-10,2,2,-6,-7,4,-10,-5,-2,9,4,3,7,4,-2,5,5,-8,7,4,7,-9,6,1,10,-8,-3,4,2,3,-9,8,8,-5,-1,9,4,4,-4,7,-3,10,-7,8,-4,-5,-1,-9,10,4,-2,9,10,7,8,-2,9,9,-8,-7,-7,-5,7,7,-9,-9,3,8,-3,9,-9,4,-5,-7,-1,-5,-9,7,4,5,5,4,-6,-1,-9,2,-5,7,-3,-3,9,3,6,-7,-5,6,8,10,-4,5,-5,-3,-7,-8,-5,5,9,-5,9,7,-4,-6,3,-10,-8,10,4,-2,4,-1,3,4,-3,6,10,-8,8,-1,-3,-8,6,4,3,-8,8,-7,-5,-2,1,2,3,8,-5,2,1,-9,-2,-6,-9,-2,-6,-9,-10,-9,10,2,1,-7,-10,2,-3,-8,-4,-7,-9,-1,6,5,-2,6,-4,-7,8,-1,5,10,6,10,-10,-2,-6,3,-4,9,-3,-8,-3,3,-9,8,10,9,-5,4,7,-6,9,-6,-10,-9,-2,-1,1,4,8,3,1,-4,10,2,3,10,-9,-7,3,-3,10,-10,8,1,10,-6,6,7,-7,3,9,4,-2,-9,4,2,6,6,-7,-1,-3,-6,-8,-4,6,-7,-3,-4,-9,-1,-5,-10,4,4,-5,6,6,6,9,-1,9,1,-8,-10,8,-3,-4,-5,-8,-10,7,-2,2,-9,8,-5,9,-3,-8,7,4,-2,-2,7,-7,-5,-4,9,7,-6,-9,3,4,-6,-9,-2,-2,1,3,-4,-6,-5,9,8,-2,-10,5,1,-3,4,10,5,2,6,6,6,-2,-4,-6,7,-7,1,2,1,-8,7,1,-2,10,8,9,-9,6,-1,8,-2,-5,-6,6,-4,2,-4,3,-10,3,10,4,2,3,-4,-1,7,-9,5,-2,-2,8,9,-4,-6,-9,-1,-6,-2,-6,1,3,3,10,-9,-7,-7,9,-8,-7,9,1,-8,5,-7,6,-10,7,-3,3,9,5,5,-6,-4,-9,8,5,8,-7,10,-4,-4,-4,-8,-1,5,7,-7,-4,7,-5,3,10,-1,6,-10,-2,3,-1,2,-10,-7,8,-1,8,6,-2,5,-10,-10,-8,9,7,5,-3,-2,-4,1,5,-6,9,-6,1,-4,8,7,6,-5,6,-1,-4,1,1,4,3,1,-2,-2,8,1,-1,3,4,8,-7,8,-1,-3,-10,-10,-7,-6,8,1,5,-6,-2,-2,9,6,-9,9,-3,2,-1,8,-5,-6,-2,9,-1,-4,3,9,5,10,-10,-4,3,-8,-2,2,-1,-8,-7,2,3,-3,1,-10,7,-10,9,4,2,4,-8,-9,7,4,8,2,-2,-8,6,1,8,-4,7,-6,-10,3,9,9,-3,9,-10,3,-5,9,8,9,-1,-10,-1,-7,9,10,-6,-3,3,10,-3,9,3,3,8,-7,5,7,-6,-10,6,4,-1,1,-10,-9,-4,-3,6,8,8,-3,3,-2,6,-5,-1,6,-5,-6,-8,8,-5,8,-6,5,2,-8,8,5,9,-8,-8,-2,1,-9,-5,4,-9,1,-1,-9,6,1,7,-10,7,-9,-2,9,1,6,-7,5,-3,1,-3,-6,-10,-3,-2,-7,10,-3,9,8,1,5,2,-6,-6,-6,9,-8,-8,8,-3,-10,-1,7,-6,9,9,-9,-3,6,2,-6,6,10,4,-8,4,-2,-1,-4,-6,-8,6,5,-10,7,-3,-5,-7,-6,4,2,10,-3,-4,9,10,4,5,-3,10,-9,3,5,8,4,3,-1,9,5,-1,-5,2,-6,9,-3,1,6,-7,-5,2,8,5,-10,3,8,-2,6,-2,-2,-4,-2,9,9,2,-1,-5,-2,8,3,-9,-7,5,4,8,8,3,8,-1,7,3,8,7,-6,-3,-8,1,-5,1,-4,5,4,4,-9,-9,8,2,-9,7,-6,8,5,1,6,9,-2,3,-2,8,-2,6,10,-6,-9,-6,-3,10,6,8,-3,3,1,3,-3,-5,-7,-4,10,-8,5,5,8,8,7,5,2,7,-4,-7,3,-1,-4,9,-5,5,1,-9,-7,3,2,-6,-10,10,-7,-10,-10,1,7,7,5,3,-6,-6,-7,9,-1,-6,1,-4,2,9,6,-5,9,7,6,1,2,4,-6,-1,-1,-7,-2,1,4,5,9,3,1,-6,-9,8,-4,-1,7,-9,-8,1,5,3,1,1,9,1,-5,-9,-4,6,-1,-10,10,9,6,-7,1,2,9,3,9,-9,1,-1,-7,4,-5,-8,-4,4,-6,-2,-2,-8,-10,-8,-9,5,7,6,2,-1,2,3,-8,-5,7,-1,4,9,-4,-4,6,-2,7,8,-6,10,10,-4,-10,3,8,6,3,7,4,10,-5,4,8,1,1,-4,5,-9,10,-4,-6,-2,10,8,-5,6,1,-1,-4,-5,-6,-7,-8,7,10,8,-4,7,-2,-7,-5,8,-5,-5,3,-5,2,9,-8,-7,10,4,-6,9,10,-8,1,1,4,6,-7,-6,2,-8,-4,7,-2,9,6,7,-5,8,-10,-3,-4,-10,1,1,-1,-4,-6,8,-5,-8,-4,4,-10,5,-3,4,1,-2,2,-8,4,10,2,-8,5,-6,10,8,6,4,4,-9,-4,7,-6,-10,6,10,8,-5,-5,1,4,-7,-5,-10,-1,-3,-1,10,7,8,2,1,6,-2,-8,-6,4,-3,-6,-7,-3,1,-1,1,-3,-1,-7,-2,8,-3,10,-7,5,-3,-2,-10,-1,10,2,-1,-10,-7,-5,-9,-4,9,2,-8,7,-9,-4,-5,10,8,-9,-4,-3,6,-1,-3,9,-10,-2,-1,-2,10,-9,-2,2,-8,10,10,4,-3,2,9,10,6,8,2,6,-9,-9,-4,2,4,6,7,-9,-5,8,6,-5,-1,8,6,-5,10,3,-7,-8,9,4,-5,8,-7,6,-4,6,6,9,7,-5,10,-3,-5,9,-6,-1,7,1,-6,7,-7,-7,6,-3,10,2,-7,8,-5,-7,-1,9,10,3,-6,5,-3,6,-8,4,10,7,-8,-1,-3,3,-7,-3,-4,-2,-9,6,1,3,5,-7,-1,2,3,-4,2,-2,2,5,-4,-8,3,-4,10,-4,-3,9,7,-5,5,-7,-9,-5,6,8,-6,-10,-4,3,-2,-8,10,-10,1,7,7,2,-5,-8,8,9,-4,-10,3,-10,-2,9,6,-9,7,4,2,-1,-4,7,6,-5,-5,7,-10,-3,7,-4,-1,1,-1,-5,2,1,6,-7,4,-1,9,-6,-6,3,1,8,2,-4,-4,-5,5,-2,4,3,5,6,3,3,3,5,-3,7,-2,-8,10,-5,-1,-7,-8,2,6,7,10,-1,6,-6,-8,-6,-8,9,2,-4,-10,-10,3,2,-10,9,9,-4,5,-3,6,5,6,1,-7,10,8,-8,2,8,-8,-3,-6,-1,-8,4,-6,8,-3,9,-4,9,-9,-2,-6,-4,-9,1,-3,-4,7,-4,7,6,-1,-3,-5,8,1,6,4,4,-4,-9,-7,9,3,10,5,3,10,2,8,9,4,9,-3,1,7,-6,5,2,-9,9,6,-2,7,2,-8,7,6,1,-6,-9,-4,-9,10,-8,-4,7,-10,8,4,3,3,-5,-5,-10,-1,-5,-4,6,8,7,3,-5,2,10,-5,10,-4,-7,-5,1,-6,3,-3,-5,4,-6,-5,-10,4,5,-5,-9,3,-10,-3,-4,-7,10,-5,4,9,6,1,-3,10,-8,6,-5,-3,7,4,-6,6,5,-3,1,-1,7,5,-8,-1,-9,4,-6,-7,-5,-2,-5,9,2,-1,3,9,3,-4,-8,-9,-2,1,2,-8,-2,-9,3,-9,1,7,1,6,2,6,4,7,10,3,7,-10,4,-5,9,-3,3,4,9,-5,1,1,7,-3,-7,9,-8,2,-8,2,-1,8,6,-6,-6,-6,-4,-4,6,-10,-4,6,7,5,-4,-5,-1,-9,-6,1,-7,1,-3,-6,4,9,-6,9,2,-3,2,-1,2,1,-4,2,-7,-7,-7,9,-1,-7,-5,2,-4,-4,-4,3,-5,-4,7,4,-6,-6,4,-2,4,-3,10,8,2,-4,9,10,2,-4,-9,-2,-9,-8,2,9,-3,-8,-10,1,-10,-10,-10,4,-6,10,-9,10,9,-1,10], dtype = "int8")#candidate|4239|(7800,)|const|int8
call_4238 = relay.TupleGetItem(func_2538_call(relay.reshape(const_4239.astype('int8'), [10, 780])), 0)
call_4240 = relay.TupleGetItem(func_2540_call(relay.reshape(const_4239.astype('int8'), [10, 780])), 0)
func_2472_call = mod.get_global_var('func_2472')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_4255 = relay.TupleGetItem(func_2472_call(), 0)
call_4256 = relay.TupleGetItem(func_2473_call(), 0)
output = relay.Tuple([call_4200,call_4238,const_4239,call_4255,])
output2 = relay.Tuple([call_4201,call_4240,const_4239,call_4256,])
func_4258 = relay.Function([], output)
mod['func_4258'] = func_4258
mod = relay.transform.InferType()(mod)
mutated_mod['func_4258'] = func_4258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4258_call = mutated_mod.get_global_var('func_4258')
call_4259 = func_4258_call()
output = call_4259
func_4260 = relay.Function([], output)
mutated_mod['func_4260'] = func_4260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3766_call = mod.get_global_var('func_3766')
func_3768_call = mutated_mod.get_global_var('func_3768')
call_4272 = func_3766_call()
call_4273 = func_3766_call()
const_4274 = relay.const([[[-6.357367,0.738562,6.798988],[-0.671654,-4.598044,1.976976],[2.033173,-0.247441,-5.454594],[-3.813374,-6.457095,6.809311],[-2.203000,2.706915,6.377108],[-6.114832,-8.909005,0.793285],[7.986491,-2.406426,-1.244549],[-2.115631,-3.263469,-0.073937],[3.115673,9.437777,5.754023],[-3.628865,9.058188,4.851130],[-2.640029,-2.858203,9.633668],[5.590724,9.302218,3.772314]],[[9.069125,6.142898,-6.998308],[-4.874158,-3.926943,-9.514652],[2.291510,7.566115,-9.269092],[6.945877,-7.995933,8.596766],[6.867636,-7.184696,-5.578185],[-7.328909,2.547578,7.063725],[-6.480676,9.843133,-3.682064],[-0.055633,6.341301,-0.214428],[-9.713267,-7.029011,7.530498],[5.747970,-4.373358,7.183650],[6.099714,-8.527354,7.592326],[-7.715404,-6.911307,-2.772043]],[[1.875597,-5.862150,-6.397869],[-7.797316,-0.504503,3.389851],[-4.541333,9.472511,4.585971],[7.240041,-2.826258,0.382328],[-0.108950,4.627948,-9.655785],[8.798665,-9.025486,-6.373002],[-4.458173,-9.261569,5.978367],[-7.033256,-2.040077,5.821738],[-9.711123,-1.012366,-4.534878],[-1.388089,2.718494,4.567892],[7.353392,-3.604766,-3.425783],[-0.826948,1.331134,-2.643022]],[[-6.847115,3.018390,-6.217622],[-5.838465,3.055658,6.838330],[7.983480,-7.497518,-7.285091],[-8.307592,-8.385764,6.107186],[8.821322,4.255021,-4.261821],[8.409845,-6.857785,9.472189],[0.260257,0.318367,-4.428879],[6.752542,-9.478142,3.133800],[0.043398,-9.074581,-9.474823],[9.425368,0.079175,-5.380273],[-3.154904,2.213651,-1.925336],[1.972413,-7.899899,9.754574]],[[0.184543,-4.809746,-3.258282],[-4.443246,6.449841,-3.180707],[4.745775,6.451255,-0.935626],[-9.827515,-8.806998,-0.253136],[6.411600,-9.116868,-7.479384],[-7.044678,-6.457332,-0.372219],[-0.028828,5.107701,2.436081],[6.052310,0.900829,-0.180624],[4.280457,-2.568654,-4.725764],[-7.092222,-8.737266,3.496158],[-0.784997,-3.531759,0.660587],[-7.826918,-9.600554,1.277520]],[[8.694590,-5.438601,-7.516641],[-5.128824,4.796390,2.383342],[1.437049,2.072323,-3.084088],[0.699359,7.022435,-9.811537],[-1.087386,-8.151946,-1.392978],[-8.813607,6.957942,-0.933993],[7.464330,9.174896,6.581508],[-8.696191,-2.513641,-4.452932],[2.561118,-1.376853,0.792384],[4.434087,7.718850,-7.220013],[7.232094,8.774749,0.988366],[-7.413642,-7.819115,-4.965651]],[[-9.115302,8.915694,-1.115084],[-6.927415,3.998845,-8.986811],[0.450313,-9.224203,-9.551878],[-5.374883,2.304245,-3.120291],[3.430921,-0.832778,-0.958904],[2.444408,9.440509,3.901143],[-3.224864,1.421726,-2.628305],[-1.770802,2.873698,-1.286089],[-0.740980,-7.103401,-8.463193],[-2.378117,4.914083,-8.401379],[5.351679,9.772673,-8.027811],[7.022958,-6.644316,-6.754866]],[[-8.671145,-7.966743,4.575187],[4.557185,7.710116,7.666323],[-2.724969,1.220300,-8.732795],[2.556045,0.870845,2.511294],[-8.172340,-9.771274,4.556144],[2.983896,6.079581,-1.450754],[0.695891,-4.149669,2.513026],[-9.935215,-4.736767,0.649594],[3.804160,-5.062643,6.522916],[-2.272871,-8.829300,-9.821496],[3.244583,-9.553442,9.341587],[3.332760,-3.202387,7.720510]],[[-0.584497,-0.933505,3.587875],[5.168637,-3.171071,7.749480],[8.169800,1.760950,-5.730202],[-0.262627,-8.425764,5.177003],[8.275213,-8.534044,-3.062789],[4.338702,8.521157,3.849683],[0.509534,-4.789913,6.551319],[-1.888696,0.483709,-9.296844],[0.413447,-7.469149,7.304109],[-4.341995,-4.657962,9.299306],[-2.118256,5.087514,-3.085816],[8.070204,-2.237313,8.479992]]], dtype = "float32")#candidate|4274|(9, 12, 3)|const|float32
bop_4275 = relay.minimum(call_4272.astype('float32'), const_4274.astype('float32')) # shape=(9, 12, 3)
bop_4278 = relay.minimum(call_4273.astype('float32'), const_4274.astype('float32')) # shape=(9, 12, 3)
output = bop_4275
output2 = bop_4278
func_4282 = relay.Function([], output)
mod['func_4282'] = func_4282
mod = relay.transform.InferType()(mod)
mutated_mod['func_4282'] = func_4282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4282_call = mutated_mod.get_global_var('func_4282')
call_4283 = func_4282_call()
output = call_4283
func_4284 = relay.Function([], output)
mutated_mod['func_4284'] = func_4284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2472_call = mod.get_global_var('func_2472')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_4313 = relay.TupleGetItem(func_2472_call(), 1)
call_4314 = relay.TupleGetItem(func_2473_call(), 1)
func_2472_call = mod.get_global_var('func_2472')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_4329 = relay.TupleGetItem(func_2472_call(), 1)
call_4330 = relay.TupleGetItem(func_2473_call(), 1)
func_50_call = mod.get_global_var('func_50')
func_53_call = mutated_mod.get_global_var('func_53')
var_4332 = relay.var("var_4332", dtype = "float32", shape = (360,))#candidate|4332|(360,)|var|float32
call_4331 = func_50_call(relay.reshape(var_4332.astype('float32'), [3, 10, 12]))
call_4333 = func_50_call(relay.reshape(var_4332.astype('float32'), [3, 10, 12]))
var_4346 = relay.var("var_4346", dtype = "float32", shape = (9, 12, 10))#candidate|4346|(9, 12, 10)|var|float32
bop_4347 = relay.greater_equal(call_4313.astype('bool'), var_4346.astype('bool')) # shape=(9, 12, 10)
bop_4350 = relay.greater_equal(call_4314.astype('bool'), var_4346.astype('bool')) # shape=(9, 12, 10)
output = relay.Tuple([call_4329,call_4331,var_4332,bop_4347,])
output2 = relay.Tuple([call_4330,call_4333,var_4332,bop_4350,])
func_4359 = relay.Function([var_4332,var_4346,], output)
mod['func_4359'] = func_4359
mod = relay.transform.InferType()(mod)
mutated_mod['func_4359'] = func_4359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4359_call = mutated_mod.get_global_var('func_4359')
var_4361 = relay.var("var_4361", dtype = "float32", shape = (360,))#candidate|4361|(360,)|var|float32
var_4362 = relay.var("var_4362", dtype = "float32", shape = (9, 12, 10))#candidate|4362|(9, 12, 10)|var|float32
call_4360 = func_4359_call(var_4361,var_4362,)
output = call_4360
func_4363 = relay.Function([var_4361,var_4362,], output)
mutated_mod['func_4363'] = func_4363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_4411 = relay.TupleGetItem(func_2172_call(), 0)
call_4412 = relay.TupleGetItem(func_2173_call(), 0)
output = call_4411
output2 = call_4412
func_4428 = relay.Function([], output)
mod['func_4428'] = func_4428
mod = relay.transform.InferType()(mod)
output = func_4428()
func_4429 = relay.Function([], output)
mutated_mod['func_4429'] = func_4429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3629_call = mod.get_global_var('func_3629')
func_3630_call = mutated_mod.get_global_var('func_3630')
call_4487 = relay.TupleGetItem(func_3629_call(), 2)
call_4488 = relay.TupleGetItem(func_3630_call(), 2)
output = call_4487
output2 = call_4488
func_4501 = relay.Function([], output)
mod['func_4501'] = func_4501
mod = relay.transform.InferType()(mod)
mutated_mod['func_4501'] = func_4501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mutated_mod.get_global_var('func_4501')
call_4502 = func_4501_call()
output = call_4502
func_4503 = relay.Function([], output)
mutated_mod['func_4503'] = func_4503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3191_call = mod.get_global_var('func_3191')
func_3192_call = mutated_mod.get_global_var('func_3192')
call_4512 = relay.TupleGetItem(func_3191_call(), 0)
call_4513 = relay.TupleGetItem(func_3192_call(), 0)
output = relay.Tuple([call_4512,])
output2 = relay.Tuple([call_4513,])
func_4522 = relay.Function([], output)
mod['func_4522'] = func_4522
mod = relay.transform.InferType()(mod)
output = func_4522()
func_4523 = relay.Function([], output)
mutated_mod['func_4523'] = func_4523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3913_call = mod.get_global_var('func_3913')
func_3914_call = mutated_mod.get_global_var('func_3914')
call_4554 = relay.TupleGetItem(func_3913_call(), 0)
call_4555 = relay.TupleGetItem(func_3914_call(), 0)
const_4570 = relay.const([[[9.652183,1.264236,-8.373150,-8.067666,-9.448755,-6.220953,-2.398468,4.843489,7.165893,-7.196744,8.559619,-4.950586,-0.418993,-9.897616,5.383312,-3.545890]]], dtype = "float32")#candidate|4570|(1, 1, 16)|const|float32
bop_4571 = relay.power(call_4554.astype('float64'), relay.reshape(const_4570.astype('float64'), relay.shape_of(call_4554))) # shape=(1, 1, 16)
bop_4574 = relay.power(call_4555.astype('float64'), relay.reshape(const_4570.astype('float64'), relay.shape_of(call_4555))) # shape=(1, 1, 16)
output = bop_4571
output2 = bop_4574
func_4585 = relay.Function([], output)
mod['func_4585'] = func_4585
mod = relay.transform.InferType()(mod)
mutated_mod['func_4585'] = func_4585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4585_call = mutated_mod.get_global_var('func_4585')
call_4586 = func_4585_call()
output = call_4586
func_4587 = relay.Function([], output)
mutated_mod['func_4587'] = func_4587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mod.get_global_var('func_4522')
func_4523_call = mutated_mod.get_global_var('func_4523')
call_4661 = relay.TupleGetItem(func_4522_call(), 0)
call_4662 = relay.TupleGetItem(func_4523_call(), 0)
output = call_4661
output2 = call_4662
func_4682 = relay.Function([], output)
mod['func_4682'] = func_4682
mod = relay.transform.InferType()(mod)
output = func_4682()
func_4683 = relay.Function([], output)
mutated_mod['func_4683'] = func_4683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mod.get_global_var('func_4522')
func_4523_call = mutated_mod.get_global_var('func_4523')
call_4696 = relay.TupleGetItem(func_4522_call(), 0)
call_4697 = relay.TupleGetItem(func_4523_call(), 0)
func_3842_call = mod.get_global_var('func_3842')
func_3846_call = mutated_mod.get_global_var('func_3846')
const_4707 = relay.const([[8],[-9],[-3],[9],[5],[5],[-10],[5],[-10],[1],[5],[-1],[-3],[1],[4],[-1],[9],[3],[4],[-3],[-3],[-7],[1],[-8],[-8],[-4],[3],[3],[-10],[1],[6],[-8],[-3],[6],[-2],[-6],[-9],[-7],[5],[-1],[6],[-6],[-3],[-6],[5],[-8],[-9],[-5],[-9],[10],[10],[-6],[7],[9],[-1],[-8],[8],[-6],[5],[3],[-7],[-1],[7],[-9],[-7],[-8],[4],[-5],[-9],[6],[-5],[-7],[-8],[-3],[4],[3],[6],[10],[-9],[10],[9],[-10],[3],[-6],[10],[-2],[-4],[-7],[1],[5],[5],[-7],[-1],[-4],[5],[4],[-3],[-6]], dtype = "uint64")#candidate|4707|(98, 1)|const|uint64
var_4708 = relay.var("var_4708", dtype = "float64", shape = (1728,))#candidate|4708|(1728,)|var|float64
call_4706 = relay.TupleGetItem(func_3842_call(relay.reshape(const_4707.astype('uint64'), [7, 7, 2]), relay.reshape(var_4708.astype('float64'), [1728,]), ), 4)
call_4709 = relay.TupleGetItem(func_3846_call(relay.reshape(const_4707.astype('uint64'), [7, 7, 2]), relay.reshape(var_4708.astype('float64'), [1728,]), ), 4)
uop_4721 = relay.sqrt(const_4707.astype('float32')) # shape=(98, 1)
func_369_call = mod.get_global_var('func_369')
func_372_call = mutated_mod.get_global_var('func_372')
var_4729 = relay.var("var_4729", dtype = "float32", shape = ())#candidate|4729|()|var|float32
call_4728 = relay.TupleGetItem(func_369_call(relay.reshape(var_4729.astype('float32'), []), relay.reshape(call_4696.astype('float32'), [1, 1, 16]), ), 0)
call_4730 = relay.TupleGetItem(func_372_call(relay.reshape(var_4729.astype('float32'), []), relay.reshape(call_4696.astype('float32'), [1, 1, 16]), ), 0)
output = relay.Tuple([call_4696,call_4706,var_4708,uop_4721,call_4728,var_4729,])
output2 = relay.Tuple([call_4697,call_4709,var_4708,uop_4721,call_4730,var_4729,])
func_4737 = relay.Function([var_4708,var_4729,], output)
mod['func_4737'] = func_4737
mod = relay.transform.InferType()(mod)
mutated_mod['func_4737'] = func_4737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4737_call = mutated_mod.get_global_var('func_4737')
var_4739 = relay.var("var_4739", dtype = "float64", shape = (1728,))#candidate|4739|(1728,)|var|float64
var_4740 = relay.var("var_4740", dtype = "float32", shape = ())#candidate|4740|()|var|float32
call_4738 = func_4737_call(var_4739,var_4740,)
output = call_4738
func_4741 = relay.Function([var_4739,var_4740,], output)
mutated_mod['func_4741'] = func_4741
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4771 = relay.const([[[-3],[-7],[9],[2]],[[7],[-6],[5],[-5]],[[5],[-7],[-4],[10]],[[9],[-6],[-4],[-2]]], dtype = "int8")#candidate|4771|(4, 4, 1)|const|int8
var_4772 = relay.var("var_4772", dtype = "int8", shape = (4, 4, 5))#candidate|4772|(4, 4, 5)|var|int8
bop_4773 = relay.less_equal(const_4771.astype('bool'), var_4772.astype('bool')) # shape=(4, 4, 5)
func_2868_call = mod.get_global_var('func_2868')
func_2870_call = mutated_mod.get_global_var('func_2870')
const_4787 = relay.const([-9.227279,5.779770,2.443355,3.061079,-2.652641,-6.142354,2.638709,-9.725885,7.618930,-7.918133,-9.720185,1.461567,-1.465182,0.499523,-7.128476,5.342297,0.138522,-5.213377,4.159995,-0.436050,-0.388642,-8.230581,1.967145,-9.826290,3.854619,6.861963,7.602268,-7.904601,9.990625,-3.419830,-7.229083,-3.155728,-5.296297,4.916970,-1.817288,0.859293,-6.534804,4.764732,6.587285,-7.705536,-7.495828,-4.566826,-6.440357,0.045009,-2.404283,3.847030,0.143661,1.975292,2.030118,-5.554159,-3.363328,-8.559280,4.403552,6.132022,8.378902,4.321194,7.355237,4.471954,-5.535485,0.025085,-7.781447,-9.874680,-4.329638,-8.698038,-3.076607,2.430498,-8.072887,0.749555,1.710702,-2.508156,-8.524124,2.171682,7.867124,8.039191,0.106829,1.994144,4.409342,-0.601725,8.255191,6.876856,7.395299,-3.243881,-2.621151,1.551374,-4.707687,-5.246300,6.923783,-8.522109,3.445032,-8.078812,-0.438461,-6.509971,9.518244,5.929660,5.586061,-5.602467,-3.999407,6.384084,-0.343093,-1.585871,-1.855471,3.856221,-3.165134,3.551397,1.722816,7.266654,5.586457,-3.062397,-4.566384,9.784735,-7.105873,-7.659450,-7.862569,-9.630693,-7.775921,-9.063885,4.185773,-0.052237,0.015516,7.548025,3.686300,8.944410,8.951391,-4.862864,3.846709,7.858271,7.230365,-9.506087,4.300331,2.076300,-6.003100,3.694371,6.511642,9.269435,5.085122,-6.984940,1.188588,6.365581,9.148623,-5.252608,7.498161,-2.991905,5.983818,-3.672794,5.598977,-9.166198,5.238131,-8.882772,9.005996,-8.589273,-8.330304,-6.003951,-5.705203,-2.369446,3.733549,-8.779490,6.978501,2.247442,-9.537102,5.585457,8.234431,9.522715,9.459962,-3.940886,6.672819,9.682274,8.910004,-3.994924,5.074954,6.096944,8.983858,2.368180,-5.145946,-6.757599,2.342073,6.518584,6.324813,5.188130,-1.768705,-3.439054,-4.247416,7.913629,9.970072,4.173172,8.910471,2.574768,5.123336,7.159291,4.320946,-2.529786,0.563236,-1.839844,-1.005601,-6.457136,0.544333,-5.080970,-0.786533,2.659226,5.070560,7.091334,9.035342,-1.544527,9.450733,-1.683806,3.094481,0.586187,-2.716092,8.454148,-5.629148,2.630920,-5.281398,2.247163,-2.960380,-7.201385,-2.254704,-2.800224,-1.776822,-1.161763,-0.011405,5.830732,5.936885,-7.950448,-3.346811,-7.394853,3.668825,-9.757281,3.661020,0.633974,-5.044302,-9.787337,4.849452,-6.437267,4.115860,5.469388,1.913468,8.174342,-0.404179,1.215641,4.763491,1.988787,2.469796,1.678176,2.609303,-4.958982,-7.867763,-7.098053,0.643764,-1.976615,3.799413,-7.080064,-6.707541,9.769045,-9.866350,0.041222,-7.796189,-3.775993,-5.378731,7.270700,-5.609398,2.569559,-9.091761,-6.879520,-0.398989,-6.902918,2.671347,-0.894862,-3.392863,-0.107221,-8.413837,-6.144294,-1.323503,6.961087,-0.570311,-1.288401,-1.897420,-5.308322,-3.426058,9.300188,7.776573,-8.534175,-5.587693,-7.798859,0.924981,9.248888,-3.492062,-7.210328,2.426791,2.956310,-1.200870,-0.816026,3.330711,0.426134,-2.260575,-8.617535,-3.555128,-1.841790,2.630129,4.515456,3.669393,0.440734,5.380175,-1.170649,5.990368,-7.226256,3.025942,-5.464897,1.447351,-1.400279,-8.488233,9.665246,-9.654250,-2.277337,-4.072940,-5.997357,-6.351335,7.925843,5.789788,-5.124313,1.736519,3.908044,-2.189267,4.001667,8.798268,2.724829,-3.128080,3.556954,-2.760696,6.792624,2.930898,-2.206972,8.582171,5.849313,6.750406,2.920136,7.045713,5.201433,-1.329219,7.050749,3.396870,-8.554786,-3.207388,-7.082625,0.753123,4.194100,9.243041,-4.490777,-9.376159,3.735708,-0.382140,-7.305706,3.616893,9.041642,5.763698,-8.022606,6.882840,-9.293296,-7.981461,-6.065462,-7.559121,-7.105063,5.036743,-4.856112,0.346575,1.503817,-9.176268,5.330781,9.043199,-5.618633,3.892195,0.865893,9.550858,-1.946947,-5.705841,7.238631,9.966283,-7.944040,-9.474445,-0.509963,5.013416,8.887144,2.570276,5.671077,3.727211,4.013016,-1.144196,5.846846,6.255769,2.045418,-7.780824,-3.925473,8.239996,-6.912724,-3.912729,4.163589,-8.776104,9.732176,7.675803,0.693114,-7.242783,3.764131,3.017347,-3.880418,3.815389,1.785225,-4.954777,0.686169,-5.342964,-5.876620,-3.983530,-9.148335,-7.808386,-3.911881,8.797428,3.005319,2.925129,-1.275823,8.198707,8.635927,1.186812,4.028695,-9.887069,2.057321,-8.237609,8.023853,2.202320,-1.104675,-8.815331,1.542737,-3.576362,2.118690,5.535424,-5.682918,1.928161,4.185519,-0.292841,-8.805354,9.700460,-8.015881,5.616692,-3.509782,1.512188,3.777925,-8.494611,4.424465,6.482592,-8.845759,9.402563,3.896421,-1.218738,0.603839,6.368961,7.016520,2.334944,7.589520,-9.019415,3.255659,-9.900448,8.830724,6.821186,4.734291,1.460536,3.366977,-3.704667,1.727181,-7.470478,-8.206118,7.929396,-2.253511,5.198333,5.326276,-9.124738,4.061710,6.724213,1.733482,-6.679719,8.605584,-5.183576,-3.677602,-8.513262,1.569037,-1.754054,-5.973061,1.884937,-0.869860,-0.113812,-7.753950,-9.278006,4.534940,-3.618135,-3.739771,0.451543,3.221150,-2.460060,4.664838,9.162521,7.212866,-5.993160,8.980939,7.600536,-7.763430,-9.103118,-3.868860,-9.014410,-7.096694,-9.194840,4.639204,5.609031,8.852411,-9.331836,-3.563582,4.639003,0.751780,1.701190,3.601935,-0.633191,2.472054,0.855505,6.379758,5.162211,-2.002669,-8.487821,-9.140056,-4.828107,-8.702377,-5.663618,1.139378,-2.641108,7.422069,0.252542,-3.990094,-0.429333,-3.095655,6.414124,9.836923,-5.164065,-3.885353,-0.054971,-1.900711,-7.562932,5.350025], dtype = "float64")#candidate|4787|(540,)|const|float64
call_4786 = relay.TupleGetItem(func_2868_call(relay.reshape(const_4787.astype('float64'), [540,])), 1)
call_4788 = relay.TupleGetItem(func_2870_call(relay.reshape(const_4787.astype('float64'), [540,])), 1)
func_4359_call = mod.get_global_var('func_4359')
func_4363_call = mutated_mod.get_global_var('func_4363')
const_4799 = relay.const([3.900937,8.419590,4.692681,-6.247154,-1.990973,-4.815456,6.238396,-1.620100,9.379907,5.995860,-0.726750,-6.713787,-9.082979,-6.315230,-9.022630,8.673505,9.294125,3.324351,-6.979499,-7.935757,4.362940,-7.520725,2.950223,3.743811,6.715866,-1.950413,-1.791418,-2.399188,4.972052,-9.984738,-7.231508,4.008972,-2.813725,-4.757589,-4.144826,-9.124638,8.914972,-2.984037,0.674315,9.854604,-2.345913,3.492684,3.588853,4.575698,-8.729925,-6.308754,-7.483551,5.073061,-4.951348,6.312652,-2.644419,3.645975,-6.970625,-0.849094,8.872301,2.680223,5.120975,-6.132638,-3.396206,0.154581,-8.520011,4.036566,-7.656668,7.131656,-6.073399,9.028522,-8.342865,-2.152777,6.826304,0.669685,3.562382,-4.214750,6.049742,7.923178,3.285826,-5.672969,-5.378386,-0.992115,-0.600517,-2.679048,-5.616881,-7.735104,-6.638418,7.553182,6.494303,-3.263170,2.398110,-0.195662,7.938404,-7.221015,-4.926180,-4.520218,-3.965829,7.305604,7.757881,3.701871,-4.707159,-0.476617,2.341981,-1.681951,-1.410825,6.965781,6.554352,-0.193644,7.461417,4.040718,-8.093634,-6.947208,-1.525354,6.954887,7.443279,4.599771,-5.444672,-3.328281,-1.613188,1.419425,6.543906,-2.074522,-3.905026,-0.895727,-5.843728,3.138041,0.126435,6.070024,-5.432276,3.662093,-9.038100,8.148025,8.688631,-5.166179,-2.893032,-0.988623,-4.633986,-8.018062,-0.033515,-3.458746,5.907778,8.700226,5.362781,-5.275441,2.218665,-1.239847,8.330882,1.350941,9.972908,-9.543981,9.989854,-1.456283,1.713262,-9.326049,5.032012,-5.205290,-3.427283,1.545072,5.529399,0.693324,-0.850718,-5.324952,8.294005,-3.902570,5.296623,-2.886956,8.725938,-7.412880,-3.457918,-6.130848,3.448436,-3.271039,-0.750453,3.588843,3.305296,6.748607,-7.806291,3.030396,6.757298,8.406812,-2.767542,5.225973,-8.616442,6.221629,-0.400226,-8.176695,-5.522705,0.183272,-3.189817,-9.391214,-5.761344,0.013015,3.484685,-1.597948,-3.779417,9.710936,-1.133471,6.752559,-6.219522,1.137702,-9.373071,-1.602236,-2.050639,-0.428109,5.994533,-4.164114,-4.717499,-2.010165,7.174549,-4.135992,-2.560761,-0.984051,-7.905638,2.941456,-0.792305,5.714077,-6.416993,-9.522942,5.710561,-5.465104,9.553039,-3.503957,-4.979534,-4.039034,-9.889309,-7.082550,-0.042913,3.421560,-6.726478,-2.341154,5.080663,5.767735,8.460626,-3.158974,-8.168533,1.322201,0.174678,8.782798,4.558274,0.195803,-6.116757,-6.016305,2.972522,2.742694,6.055558,-7.702856,6.237527,-9.911814,5.488635,-0.571740,9.627830,-9.644072,4.428136,7.807725,6.349312,-7.053112,-8.792615,-8.438426,-8.980094,5.667964,1.580005,-4.622752,4.571290,-3.950958,3.234619,0.556506,-9.312577,-7.285941,1.055126,-1.282930,-9.151666,4.304546,-0.992667,-6.868784,1.727504,-4.015847,-2.870534,-7.814905,2.583132,-4.684942,4.383136,-0.206353,9.548749,6.995828,-2.736067,2.827155,8.002941,7.498090,7.698893,-6.290816,6.549530,1.914288,-9.088226,4.111046,-6.018520,-7.361846,8.004391,-2.366175,8.311931,-6.743221,1.949110,4.585935,-5.063167,-8.318568,-6.568926,-4.932012,8.495190,1.794604,7.637236,-3.132646,5.302218,7.860783,2.378961,1.081187,-7.213273,-6.734503,-9.108506,-9.209516,-0.714914,-7.393462,3.102407,-4.399284,-7.952740,-6.803339,-3.126833,-1.452973,-0.106958,5.955669,4.978345,-4.169409,-7.588939,3.519365,-7.380605,8.492060,1.381279,-1.181720,-4.007852,3.636430,-0.376341,7.744711,-9.797824,-1.886591,8.540366,-8.003436,0.695774,-2.802065,8.712438,-7.758961,3.692287,-0.099068,0.459612,-2.943327,3.620082,-8.072030,7.389144,9.742439,7.708551,-4.938410,7.190092,1.041118,-5.022668,-0.150201,-2.690400,8.859949,-0.354146,-8.132132,-7.006053,9.784319,-3.154394,-3.927659,2.401359,-9.842865,3.401069,-1.975224,5.789149,6.975839,0.936938,-6.837775,-8.241809,-7.350344,0.652158,-8.102098,6.441494,-1.955191,-6.498578,6.938773,-0.273419,-0.477616,5.494959,-8.117758,2.314024,-4.713424,5.597397,-8.571004,-9.480792,-3.048947,9.319342,-4.998566,-3.676308,-9.220398,1.506562,4.395583,7.680906,3.640311,-6.849476,-5.343519,-3.406333,-8.554832,8.770406,9.505368,3.142039,7.878136,5.213898,8.271224,-4.823350,-7.703372,-3.074170,0.870270,2.902424,-1.729976,-0.533717,6.240671,4.302551,-2.495309,-6.345263,-7.692725,8.936561,-2.934150,5.921599,0.830141,-0.635611,7.711390,2.346561,-0.231326,-1.225492,-1.730616,9.408451,9.118760,0.503774,0.009032,2.152763,-4.267590,-5.937554,5.491539,-0.822115,6.915414,-3.355835,6.370815,-9.979746,2.489420,-8.183307,8.948018,7.379545,-3.086644,4.896015,6.245906,-6.300367,6.787066,-1.919308,-4.081048,6.409900,1.519574,0.178228,5.366922,3.230453,-5.981980,-7.316233,9.241041,-1.334784,4.496985,-8.287364,-3.583029,-8.854152,5.714233,8.142161,8.435307,0.884575,-4.881420,-9.277464,-4.556845,-0.033890,7.009147,3.954378,7.597735,2.190890,8.746694,8.730534,-6.758623,9.855733,-4.160363,7.580677,-0.999196,1.279632,2.375936,-0.695734,6.676010,-0.254999,-2.435076,6.600538,6.753230,-1.838945,-3.940879,8.432113,0.007820,-3.567877,1.329364,4.130090,9.136806,-2.018343,-9.112937,-8.408076,-0.486576,8.221865,-5.570054,-0.375292,0.370358,-3.066053,-8.757719,-9.164657,4.235174,4.365584,-3.004946,-3.509595,1.924345,6.765151,0.032926,5.636083,-4.025866,-8.279904,-7.067980,6.906892,5.923425,5.954123,9.043559,4.122188,5.897975,5.257624,-2.706772,4.460020,-8.873362,3.479191,-0.642558,9.437743,7.076785,-1.033696,-2.526091,3.620688,8.023179,2.354281,-1.418603,4.275822,-5.823391,-1.511690,-2.220356,-0.740654,-3.982250,8.470231,4.298919,5.360001,-4.623944,-0.097776,5.447535,8.387890,-9.490040,2.019740,0.050074,-6.306870,8.883532,-6.999292,-3.337386,5.441691,4.024489,-9.937634,6.639813,9.925023,1.422074,0.583274,-3.930066,1.050518,2.053580,9.195207,-3.162578,-9.819567,-8.430759,3.868591,-7.859635,9.466005,9.907139,-4.520717,-8.656477,5.947397,6.572789,-9.262198,1.835853,-3.834755,0.450357,9.415576,-2.255937,1.279574,3.526624,5.937897,7.820583,1.730950,-2.992233,-5.957763,4.086237,-3.243034,-9.343716,-2.292089,7.522040,-7.560695,0.759454,-3.599290,-3.578597,-6.418177,-4.215296,6.548649,5.160782,3.401372,-8.593739,-1.955949,9.215625,-3.141556,8.909599,6.388980,6.378217,4.123657,2.394120,-6.050754,-1.766755,5.153798,6.555842,-3.159453,4.766947,-2.486984,6.866808,-3.884847,-3.042363,-4.116626,4.391578,-9.029574,-1.820320,3.351262,5.298908,2.609246,8.346305,-4.853422,9.048862,1.602741,-6.951328,-3.233391,-4.627236,-0.117584,0.573968,-0.578880,-7.273242,6.375088,5.791458,8.559847,0.670885,-1.706903,1.424665,9.820046,5.242732,-7.004909,-3.538690,-8.233855,7.641266,3.036293,6.851632,2.076886,-8.912253,-9.346549,-6.411497,-6.601772,-4.114068,-1.291470,-9.967551,-6.500275,-1.363918,8.459234,7.629804,5.583399,2.366796,8.949920,-1.831443,-7.403562,-7.130275,-1.679820,-6.008350,-5.216282,1.949205,2.491215,-2.004985,-3.367036,-6.683198,5.966885,4.847987,-2.687378,-4.448847,3.970482,-9.288084,3.771532,9.720305,0.686011,3.280947,-5.417094,-5.691320,-9.257873,-1.010385,6.718254,-9.905712,-0.925684,8.745274,-2.505765,3.593133,2.812814,-5.492692,-4.411963,-6.894290,0.144293,9.468121,5.539008,2.178959,-7.607449,-0.171212,-9.581904,-6.843091,-3.309768,0.325817,6.646294,-6.225880,6.018139,-7.315141,-6.484237,1.026325,-6.258749,-0.502929,6.486386,7.135861,8.462967,9.401286,-7.691666,-3.018910,-0.354635,-6.316654,-8.885989,-3.762021,4.211672,7.936044,5.102427,4.611305,6.572886,2.916390,-0.005657,-4.242225,-0.471151,2.769664,-9.818404,0.811567,-1.389625,-0.109426,4.512511,-4.294420,4.907440,-2.586479,-1.243642,-9.998013,5.815993,-1.598380,-2.598611,4.686946,9.795077,-9.592353,5.725174,-3.076770,4.451178,-9.935204,4.890754,1.781970,7.426982,8.067612,9.730001,8.598189,-3.720011,-5.229916,1.350793,9.222931,7.132092,-7.237814,-4.704316,-8.348866,2.094117,-0.411243,3.383697,-6.042172,6.792091,-8.213401,7.188294,-5.080395,-7.591903,8.952236,-0.017160,-9.627484,-0.724405,-2.423906,8.824668,-2.732258,-4.676505,6.627011,-2.364586,-5.976783,9.023413,-2.996188,-9.064304,-1.434563,-1.645767,-4.018854,7.649573,-0.967087,7.083041,-3.936697,7.107281,-3.752120,8.087846,1.739926,9.072042,4.358736,-7.472025,6.096634,-6.837735,0.254800,8.865082,-2.581793,-8.666595,-6.576240,5.469542,-5.659401,2.330282,-5.092844,-4.530949,-8.856737,5.522893,5.144141,-6.526924,7.646847,-6.941170,3.999431,-7.540617,-6.970402,-6.711395,1.055222,6.349975,-0.370738,-4.938147,7.810296,-3.634831,-6.190760,-1.010577,8.340178,-0.136913,4.131636,-9.436599,4.779035,-1.306515,7.052620,-0.382507,0.882518,9.995491,7.024551,-5.643722,-9.699006,-4.066742,4.525044,-8.721716,0.868409,0.769568,-1.540655,0.910618,-4.740064,6.898711,-5.668263,-3.763620,-5.153475,5.180377,5.750988,-0.364935,-2.741065,-1.502730,5.642408,6.904018,-9.310299,-6.217962,-1.235098,-8.151507,3.291749,-4.651783,7.802532,7.307510,-7.238273,8.650895,6.941983,-6.279902,1.257553,1.201706,0.607986,6.150428,7.848653,-9.356787,-7.474679,-3.424254,6.546431,7.066206,-8.847360,-6.819150,-7.727869,-1.794639,9.276660,7.220509,-6.204558,-3.838537,3.507658,1.076876,2.534224,-0.828103,-5.871456,5.288425,-4.739379,-0.547746,-2.521775,2.316417,7.886393,-1.975311,-4.082061,4.852931,-4.177073,9.470734,8.190058,-0.865214,-9.755685,-3.608736,2.180863,-5.038759,8.121538,-5.726651,0.536134,-6.293786,-3.298991,-9.607616,-9.809494,8.786197,2.602420,2.246346,6.023368,1.923350,-4.670352,-5.775616,8.929844,7.031894,9.199856,-2.600455,-6.637755,6.252358,1.273117,3.916651,1.530945,-7.506105,2.007951,-4.044688,0.808399,6.008851,5.613949,-7.572982,-9.681554,0.442168,2.554254,5.344799,-5.949230,-1.290580,-9.093905,-8.007635,-0.215560,-1.616397,-5.799749,-0.573061,-3.340438,0.699406,7.501850,-2.660136,-2.678435,-0.251190,-0.949549,2.411196,-5.477390,-2.554539,4.957606,8.104359,-0.615502,-6.198548,-0.670308,-8.611727,-2.481844,-5.220121,9.558397,8.970962,5.560235,-5.621284,0.088147,-6.067776,4.416019,-2.470754,9.406238,3.172203,8.275504,-1.530653,-6.931642,-8.193043,2.225154,5.684447,-3.364189,-2.294064,-2.973957,1.787483,-1.491750,6.095235,-8.433744,-3.412898,4.976184,6.863193,4.046680,-0.133105,8.775945,-1.087988,-0.332556,6.619029,8.208625,-4.178431,-3.018853,8.680517,9.026379,2.007416,7.767743,-6.479307,1.098788,1.400544,0.404451,-5.889012,2.725436,0.641686,-7.437992,-3.714699,-0.385307,0.007653,-9.782965,8.269662,-3.601852,2.019910,6.032011,-3.278618,-4.693271,9.227963,-9.869406,-6.465616,6.432238,1.424830,-2.995845,9.318068,-5.195564,-4.589656,7.250335,-5.193205,-0.768485,7.684833,3.948426,-6.597437,-0.611608,-6.203073,5.455557,-6.880723,-9.675742,3.077696,2.151707,-3.811317,0.496291], dtype = "float32")#candidate|4799|(1080,)|const|float32
call_4798 = relay.TupleGetItem(func_4359_call(relay.reshape(call_4786.astype('float32'), [360,]), relay.reshape(const_4799.astype('float32'), [9, 12, 10]), ), 0)
call_4800 = relay.TupleGetItem(func_4363_call(relay.reshape(call_4786.astype('float32'), [360,]), relay.reshape(const_4799.astype('float32'), [9, 12, 10]), ), 0)
output = relay.Tuple([bop_4773,call_4786,const_4787,call_4798,const_4799,])
output2 = relay.Tuple([bop_4773,call_4788,const_4787,call_4800,const_4799,])
func_4801 = relay.Function([var_4772,], output)
mod['func_4801'] = func_4801
mod = relay.transform.InferType()(mod)
var_4802 = relay.var("var_4802", dtype = "int8", shape = (4, 4, 5))#candidate|4802|(4, 4, 5)|var|int8
output = func_4801(var_4802)
func_4803 = relay.Function([var_4802], output)
mutated_mod['func_4803'] = func_4803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2472_call = mod.get_global_var('func_2472')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_4805 = relay.TupleGetItem(func_2472_call(), 1)
call_4806 = relay.TupleGetItem(func_2473_call(), 1)
var_4819 = relay.var("var_4819", dtype = "float32", shape = (9, 12, 11))#candidate|4819|(9, 12, 11)|var|float32
bop_4820 = relay.logical_xor(call_4805.astype('int8'), var_4819.astype('int8')) # shape=(9, 12, 11)
bop_4823 = relay.logical_xor(call_4806.astype('int8'), var_4819.astype('int8')) # shape=(9, 12, 11)
bop_4828 = relay.bitwise_and(bop_4820.astype('int64'), relay.reshape(var_4819.astype('int64'), relay.shape_of(bop_4820))) # shape=(9, 12, 11)
bop_4831 = relay.bitwise_and(bop_4823.astype('int64'), relay.reshape(var_4819.astype('int64'), relay.shape_of(bop_4823))) # shape=(9, 12, 11)
uop_4833 = relay.sqrt(bop_4828.astype('float64')) # shape=(9, 12, 11)
uop_4835 = relay.sqrt(bop_4831.astype('float64')) # shape=(9, 12, 11)
func_3716_call = mod.get_global_var('func_3716')
func_3717_call = mutated_mod.get_global_var('func_3717')
call_4836 = func_3716_call()
call_4837 = func_3716_call()
func_4165_call = mod.get_global_var('func_4165')
func_4168_call = mutated_mod.get_global_var('func_4168')
call_4838 = relay.TupleGetItem(func_4165_call(relay.reshape(bop_4820.astype('float64'), [9, 12, 11])), 0)
call_4839 = relay.TupleGetItem(func_4168_call(relay.reshape(bop_4820.astype('float64'), [9, 12, 11])), 0)
func_2553_call = mod.get_global_var('func_2553')
func_2555_call = mutated_mod.get_global_var('func_2555')
call_4844 = relay.TupleGetItem(func_2553_call(), 0)
call_4845 = relay.TupleGetItem(func_2555_call(), 0)
func_2472_call = mod.get_global_var('func_2472')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_4846 = relay.TupleGetItem(func_2472_call(), 1)
call_4847 = relay.TupleGetItem(func_2473_call(), 1)
var_4850 = relay.var("var_4850", dtype = "float32", shape = (9, 12, 11))#candidate|4850|(9, 12, 11)|var|float32
bop_4851 = relay.not_equal(call_4838.astype('bool'), relay.reshape(var_4850.astype('bool'), relay.shape_of(call_4838))) # shape=(9, 12, 11)
bop_4854 = relay.not_equal(call_4839.astype('bool'), relay.reshape(var_4850.astype('bool'), relay.shape_of(call_4839))) # shape=(9, 12, 11)
func_4801_call = mod.get_global_var('func_4801')
func_4803_call = mutated_mod.get_global_var('func_4803')
const_4875 = relay.const([-5,-5,1,-10,-7,-4,-5,-8,2,10,4,4,3,-7,10,-8,2,-1,-1,1,5,8,-2,2,-8,-2,4,-6,-3,-10,8,9,1,10,1,1,9,-8,8,5,-4,-8,-4,-9,-7,10,-9,5,1,2,-9,9,-4,8,-9,-8,1,-5,-10,2,3,5,2,-10,5,8,6,-1,6,-2,2,2,-8,10,9,-7,3,4,10,-10], dtype = "int8")#candidate|4875|(80,)|const|int8
call_4874 = relay.TupleGetItem(func_4801_call(relay.reshape(const_4875.astype('int8'), [4, 4, 5])), 2)
call_4876 = relay.TupleGetItem(func_4803_call(relay.reshape(const_4875.astype('int8'), [4, 4, 5])), 2)
output = relay.Tuple([uop_4833,call_4836,call_4844,call_4846,bop_4851,call_4874,const_4875,])
output2 = relay.Tuple([uop_4835,call_4837,call_4845,call_4847,bop_4854,call_4876,const_4875,])
func_4877 = relay.Function([var_4819,var_4850,], output)
mod['func_4877'] = func_4877
mod = relay.transform.InferType()(mod)
var_4878 = relay.var("var_4878", dtype = "float32", shape = (9, 12, 11))#candidate|4878|(9, 12, 11)|var|float32
var_4879 = relay.var("var_4879", dtype = "float32", shape = (9, 12, 11))#candidate|4879|(9, 12, 11)|var|float32
output = func_4877(var_4878,var_4879,)
func_4880 = relay.Function([var_4878,var_4879,], output)
mutated_mod['func_4880'] = func_4880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3191_call = mod.get_global_var('func_3191')
func_3192_call = mutated_mod.get_global_var('func_3192')
call_4978 = relay.TupleGetItem(func_3191_call(), 0)
call_4979 = relay.TupleGetItem(func_3192_call(), 0)
output = call_4978
output2 = call_4979
func_4987 = relay.Function([], output)
mod['func_4987'] = func_4987
mod = relay.transform.InferType()(mod)
output = func_4987()
func_4988 = relay.Function([], output)
mutated_mod['func_4988'] = func_4988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2895_call = mod.get_global_var('func_2895')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_5046 = func_2895_call()
call_5047 = func_2895_call()
output = relay.Tuple([call_5046,])
output2 = relay.Tuple([call_5047,])
func_5048 = relay.Function([], output)
mod['func_5048'] = func_5048
mod = relay.transform.InferType()(mod)
mutated_mod['func_5048'] = func_5048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5048_call = mutated_mod.get_global_var('func_5048')
call_5049 = func_5048_call()
output = call_5049
func_5050 = relay.Function([], output)
mutated_mod['func_5050'] = func_5050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mod.get_global_var('func_2260')
func_2262_call = mutated_mod.get_global_var('func_2262')
call_5064 = relay.TupleGetItem(func_2260_call(), 0)
call_5065 = relay.TupleGetItem(func_2262_call(), 0)
output = call_5064
output2 = call_5065
func_5078 = relay.Function([], output)
mod['func_5078'] = func_5078
mod = relay.transform.InferType()(mod)
mutated_mod['func_5078'] = func_5078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5078_call = mutated_mod.get_global_var('func_5078')
call_5079 = func_5078_call()
output = call_5079
func_5080 = relay.Function([], output)
mutated_mod['func_5080'] = func_5080
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5087 = relay.var("var_5087", dtype = "float64", shape = (3, 1, 1))#candidate|5087|(3, 1, 1)|var|float64
uop_5088 = relay.acosh(var_5087.astype('float64')) # shape=(3, 1, 1)
output = uop_5088
output2 = uop_5088
func_5094 = relay.Function([var_5087,], output)
mod['func_5094'] = func_5094
mod = relay.transform.InferType()(mod)
mutated_mod['func_5094'] = func_5094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5095 = relay.var("var_5095", dtype = "float64", shape = (3, 1, 1))#candidate|5095|(3, 1, 1)|var|float64
func_5094_call = mutated_mod.get_global_var('func_5094')
call_5096 = func_5094_call(var_5095)
output = call_5096
func_5097 = relay.Function([var_5095], output)
mutated_mod['func_5097'] = func_5097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3913_call = mod.get_global_var('func_3913')
func_3914_call = mutated_mod.get_global_var('func_3914')
call_5129 = relay.TupleGetItem(func_3913_call(), 0)
call_5130 = relay.TupleGetItem(func_3914_call(), 0)
uop_5134 = relay.cos(call_5129.astype('float32')) # shape=(1, 1, 16)
uop_5136 = relay.cos(call_5130.astype('float32')) # shape=(1, 1, 16)
output = relay.Tuple([uop_5134,])
output2 = relay.Tuple([uop_5136,])
func_5141 = relay.Function([], output)
mod['func_5141'] = func_5141
mod = relay.transform.InferType()(mod)
mutated_mod['func_5141'] = func_5141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5141_call = mutated_mod.get_global_var('func_5141')
call_5142 = func_5141_call()
output = call_5142
func_5143 = relay.Function([], output)
mutated_mod['func_5143'] = func_5143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3766_call = mod.get_global_var('func_3766')
func_3768_call = mutated_mod.get_global_var('func_3768')
call_5147 = func_3766_call()
call_5148 = func_3766_call()
func_3766_call = mod.get_global_var('func_3766')
func_3768_call = mutated_mod.get_global_var('func_3768')
call_5154 = func_3766_call()
call_5155 = func_3766_call()
func_2374_call = mod.get_global_var('func_2374')
func_2377_call = mutated_mod.get_global_var('func_2377')
const_5165 = relay.const(-3, dtype = "int32")#candidate|5165|()|const|int32
call_5164 = func_2374_call(relay.reshape(const_5165.astype('int32'), []))
call_5166 = func_2374_call(relay.reshape(const_5165.astype('int32'), []))
func_5078_call = mod.get_global_var('func_5078')
func_5080_call = mutated_mod.get_global_var('func_5080')
call_5173 = func_5078_call()
call_5174 = func_5078_call()
output = relay.Tuple([call_5147,call_5154,call_5164,const_5165,call_5173,])
output2 = relay.Tuple([call_5148,call_5155,call_5166,const_5165,call_5174,])
func_5175 = relay.Function([], output)
mod['func_5175'] = func_5175
mod = relay.transform.InferType()(mod)
output = func_5175()
func_5176 = relay.Function([], output)
mutated_mod['func_5176'] = func_5176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5189 = relay.var("var_5189", dtype = "float32", shape = (2, 10, 5))#candidate|5189|(2, 10, 5)|var|float32
var_5190 = relay.var("var_5190", dtype = "float32", shape = (2, 10, 5))#candidate|5190|(2, 10, 5)|var|float32
bop_5191 = relay.less_equal(var_5189.astype('bool'), relay.reshape(var_5190.astype('bool'), relay.shape_of(var_5189))) # shape=(2, 10, 5)
uop_5201 = relay.rsqrt(var_5189.astype('float32')) # shape=(2, 10, 5)
uop_5209 = relay.atan(uop_5201.astype('float32')) # shape=(2, 10, 5)
uop_5222 = relay.atanh(uop_5209.astype('float64')) # shape=(2, 10, 5)
uop_5227 = relay.asin(uop_5209.astype('float32')) # shape=(2, 10, 5)
func_4987_call = mod.get_global_var('func_4987')
func_4988_call = mutated_mod.get_global_var('func_4988')
call_5230 = func_4987_call()
call_5231 = func_4987_call()
output = relay.Tuple([bop_5191,uop_5222,uop_5227,call_5230,])
output2 = relay.Tuple([bop_5191,uop_5222,uop_5227,call_5231,])
func_5240 = relay.Function([var_5189,var_5190,], output)
mod['func_5240'] = func_5240
mod = relay.transform.InferType()(mod)
mutated_mod['func_5240'] = func_5240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5240_call = mutated_mod.get_global_var('func_5240')
var_5242 = relay.var("var_5242", dtype = "float32", shape = (2, 10, 5))#candidate|5242|(2, 10, 5)|var|float32
var_5243 = relay.var("var_5243", dtype = "float32", shape = (2, 10, 5))#candidate|5243|(2, 10, 5)|var|float32
call_5241 = func_5240_call(var_5242,var_5243,)
output = call_5241
func_5244 = relay.Function([var_5242,var_5243,], output)
mutated_mod['func_5244'] = func_5244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4682_call = mod.get_global_var('func_4682')
func_4683_call = mutated_mod.get_global_var('func_4683')
call_5246 = func_4682_call()
call_5247 = func_4682_call()
func_4258_call = mod.get_global_var('func_4258')
func_4260_call = mutated_mod.get_global_var('func_4260')
call_5257 = relay.TupleGetItem(func_4258_call(), 2)
call_5258 = relay.TupleGetItem(func_4260_call(), 2)
uop_5264 = relay.atan(call_5257.astype('float32')) # shape=(7800,)
uop_5266 = relay.atan(call_5258.astype('float32')) # shape=(7800,)
output = relay.Tuple([call_5246,uop_5264,])
output2 = relay.Tuple([call_5247,uop_5266,])
func_5267 = relay.Function([], output)
mod['func_5267'] = func_5267
mod = relay.transform.InferType()(mod)
output = func_5267()
func_5268 = relay.Function([], output)
mutated_mod['func_5268'] = func_5268
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5321 = relay.var("var_5321", dtype = "float64", shape = (4, 10, 5))#candidate|5321|(4, 10, 5)|var|float64
uop_5322 = relay.sqrt(var_5321.astype('float64')) # shape=(4, 10, 5)
output = uop_5322
output2 = uop_5322
func_5327 = relay.Function([var_5321,], output)
mod['func_5327'] = func_5327
mod = relay.transform.InferType()(mod)
var_5328 = relay.var("var_5328", dtype = "float64", shape = (4, 10, 5))#candidate|5328|(4, 10, 5)|var|float64
output = func_5327(var_5328)
func_5329 = relay.Function([var_5328], output)
mutated_mod['func_5329'] = func_5329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3524_call = mod.get_global_var('func_3524')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_5337 = func_3524_call()
call_5338 = func_3524_call()
output = relay.Tuple([call_5337,])
output2 = relay.Tuple([call_5338,])
func_5343 = relay.Function([], output)
mod['func_5343'] = func_5343
mod = relay.transform.InferType()(mod)
output = func_5343()
func_5344 = relay.Function([], output)
mutated_mod['func_5344'] = func_5344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2895_call = mod.get_global_var('func_2895')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_5433 = func_2895_call()
call_5434 = func_2895_call()
func_4877_call = mod.get_global_var('func_4877')
func_4880_call = mutated_mod.get_global_var('func_4880')
const_5438 = relay.const([-3.253748,-1.675393,0.559643,5.922712,5.792426,2.757290,-2.942388,6.067526,-0.891767,9.642737,-3.826544,-8.662088,-3.120237,0.246489,1.684970,-9.282726,1.798612,9.151138,-7.886150,-1.862812,8.391947,2.007860,9.583214,-1.405727,8.577100,-6.335549,-4.467498,-5.520915,4.233855,-1.616505,-2.974935,-8.992156,-6.241496,0.824481,-3.165307,-2.090390,4.060676,-1.207418,-9.573248,-3.909913,-4.364536,-6.874575,3.362410,1.136044,-8.001762,1.306449,-3.526078,-1.316931,-9.681763,-9.273048,2.649469,-3.519802,-7.483890,9.775618,6.088262,6.200187,-8.535165,6.600385,-4.663448,-4.622170,-9.927641,-7.052451,-2.744446,0.919586,-4.969645,2.306096,-8.589310,-0.808289,-5.615759,-5.486605,-5.569053,8.590956,2.928544,-8.978031,-8.847112,-5.813995,9.438781,3.726379,4.276909,-3.849042,-8.265682,0.725324,3.126793,-5.516538,5.124014,-2.645673,-7.821595,5.316956,-1.014123,6.415062,-1.038551,1.465265,-5.876159,7.316397,-8.143218,9.778609,-4.182238,3.174235,4.884853,4.325538,-3.180895,-6.233785,-5.984232,-4.654859,6.076639,0.659090,1.992262,9.305361,3.347815,9.497472,-7.138103,0.365640,1.600389,6.053045,-0.002252,-6.663992,-7.129944,7.664398,-7.333915,4.764824,3.099601,5.886017,7.625679,0.311469,-7.966606,-3.950232,9.832694,7.441914,8.760791,5.844224,0.064506,-5.242376,-1.095208,-8.843625,-9.144178,2.985594,-6.086589,-8.152517,0.683823,8.291481,4.652670,9.258692,8.541277,8.424150,5.659120,-8.072615,-5.247396,-2.001383,-3.933691,3.173822,-2.540294,-0.920769,-6.734588,-5.326312,-5.657707,4.845461,-3.681771,4.901792,8.454647,-9.370619,9.093576,2.891567,2.739221,4.587625,2.125024,-4.432584,9.023509,-4.069455,-0.394687,7.044357,-8.025933,-4.011356,2.397961,-3.091840,-7.452847,8.790860,5.614160,-4.214247,-6.134511,-1.815682,-5.267176,4.326574,-5.759591,3.537369,8.736523,5.368466,9.104033,-6.099831,0.427670,7.038167,7.835263,-3.049202,-8.903105,4.036591,-8.093684,-5.008897,1.186382,-2.753130,0.905130,-3.369051,-1.528473,4.120293,3.387670,7.917723,-8.204918,-9.971500,5.328170,1.564782,2.105189,7.322187,-1.315662,9.210707,7.919312,9.602489,2.881764,5.778889,-0.083946,-2.757713,-2.590416,-4.780532,-1.173878,-8.721240,4.929843,6.539866,2.802078,-5.010415,-6.838251,6.391984,6.366321,2.118817,-2.563344,6.389389,3.226483,-4.399299,5.346409,-2.145379,4.938027,7.815921,-1.512921,-1.920111,7.743773,-7.443103,-8.430790,-0.525510,-7.868061,-5.795745,-8.745998,5.154565,8.284469,-4.936851,6.304950,3.485465,7.313162,9.888368,1.787396,6.308378,0.886148,3.323225,7.688574,0.131673,0.617222,-2.696911,4.153857,4.131329,6.342036,8.546164,-4.702391,-1.249827,-5.458905,-5.812193,2.344039,-5.237642,8.929171,-2.350258,6.247416,-6.234448,2.220956,8.332658,0.502540,-6.727266,-2.162787,7.050005,-9.641808,-7.401102,0.108210,-9.418315,2.591630,6.110603,-1.107620,4.739748,-6.763126,-9.050544,9.286730,-3.756578,-0.914455,3.841855,2.007865,-8.314964,-8.839583,-3.209691,6.175899,-7.869810,3.366542,8.402023,2.396516,-8.659489,-3.114853,-3.142123,-7.553572,-7.356547,8.823238,2.184164,-4.273834,-7.891447,-6.121211,9.238137,8.696117,-3.443498,3.853245,2.181159,9.671865,-2.812996,-7.860616,6.169935,-9.477883,-6.252816,7.453869,-2.769524,0.036534,0.106586,5.649876,2.742063,-9.727097,2.238794,1.083434,8.389786,-1.887753,-2.723300,-3.415429,8.768937,-2.613261,-5.504047,7.275013,9.085941,7.723073,4.588099,6.692210,4.851091,-8.138686,-7.441558,0.945396,-6.901248,7.011992,1.860946,-0.368790,-8.189446,-0.242033,3.710048,1.726996,-2.951378,6.091997,4.480178,-6.569259,-2.395782,-3.020414,-8.582592,-2.340196,9.841566,8.621408,1.355470,-5.413907,-8.637102,-8.005539,-2.335451,7.863285,-3.208168,-4.347595,0.077595,9.083374,-6.686613,-1.186971,2.702479,4.157272,2.294635,3.858484,0.527142,-7.546928,-2.479509,3.584744,7.788856,6.315537,7.461735,5.718765,-7.110448,-3.972315,-3.632880,6.894564,-1.768649,8.284059,-0.356676,-1.330895,-9.671092,5.811221,-7.485138,9.343445,7.802306,9.279581,9.506806,-7.452002,8.443052,-8.995959,5.151539,-0.782756,-9.716208,5.181823,-4.090345,-9.555371,0.213749,-0.630653,-2.329553,0.348630,-5.048592,-9.095764,5.488748,-0.571271,-5.082299,6.587208,-5.811219,2.486448,4.974099,0.420290,-8.773656,-3.949956,-6.188857,4.929945,-2.296524,-6.653430,-1.789845,-9.187749,9.595312,-9.181808,2.558388,-0.325624,3.789053,8.737424,-4.357988,2.844139,-8.190446,-7.410635,-3.995061,-1.431442,-0.190133,7.373677,5.802843,5.628451,-3.203565,-6.267133,0.817759,-1.642377,-1.269021,1.122706,-3.553530,-3.714032,-3.777017,2.949407,-0.480981,4.353911,2.928482,5.118357,8.578905,6.991596,4.613019,8.660103,-0.260900,7.435437,0.569134,-0.480988,0.181672,8.607808,8.536741,-9.365297,-8.597991,1.488815,7.160441,-8.917096,9.561021,-6.972990,-0.668187,2.054506,1.217875,7.483329,0.932908,7.645974,-0.348267,-3.093903,3.731903,-3.410041,-0.860273,2.295659,-7.405138,-4.097780,-6.973896,-1.613107,0.647474,4.658173,3.180822,9.584204,-1.089055,9.708208,8.549304,6.378657,0.695005,-0.980648,1.358924,4.277171,-8.550207,6.579080,-8.242602,0.788611,6.247589,1.170185,1.598977,4.955917,6.244061,2.912475,-2.124989,6.472074,-0.261424,0.744965,-5.774949,2.471223,3.944836,7.804277,1.749640,0.645979,2.122277,3.215456,2.170174,5.737942,6.616041,-4.762900,2.097326,9.397562,4.911500,2.340194,0.366314,-4.294661,9.601526,5.972708,-6.425316,7.564490,7.501106,0.575854,0.585389,6.295179,8.749826,-7.379262,3.362090,-4.867145,-4.802194,-2.978468,-7.682811,-8.855736,-2.946629,-2.928616,-8.380715,6.227803,-2.234626,9.042048,4.916947,3.134599,-2.609125,4.005752,7.339567,-2.002064,6.709785,-1.535342,-1.185252,1.848240,-3.252254,9.780014,4.855741,-5.434864,4.448172,6.409839,-7.944084,5.960989,-6.260684,-5.264321,-3.673870,9.582559,-3.753706,-2.834741,7.986725,3.421385,9.477387,-5.354116,5.370890,5.216282,-9.679286,4.668974,9.732086,5.609918,8.272347,8.139374,3.667570,8.519518,-4.165267,-2.642860,3.422530,0.609860,-8.254651,6.806512,-5.080271,2.754000,6.747624,5.055568,2.014862,-9.476065,8.724396,0.843311,2.639398,-3.659064,-7.067475,4.127808,-8.476149,-6.947327,-8.003709,2.690277,-8.881058,-3.298758,4.033659,-3.640453,-6.510388,-7.702981,5.358597,-6.980811,-6.034832,-3.676819,7.212059,9.970216,1.302070,2.153661,5.358435,-5.151447,0.460705,-0.849216,1.229193,7.071928,6.188056,8.372242,3.833013,8.239494,-1.787416,-8.500493,2.549094,3.032572,-3.508623,6.109439,5.047749,0.503714,-5.043674,-4.730430,3.117786,8.749721,6.282035,2.444532,9.473581,-8.952808,-3.260774,7.485628,-9.720801,-0.559949,5.495955,8.194918,-0.551146,8.122470,-3.036884,-8.709716,-9.096986,-0.204022,-4.446399,-1.425455,0.907697,6.036762,-7.476147,6.520056,2.136746,7.301920,3.567460,-4.240326,6.198693,-4.370814,8.906839,3.244686,1.855570,4.641931,9.400971,1.971253,-2.859091,3.313992,5.554356,-2.006260,-2.900658,-2.142131,-4.289804,3.100474,-2.376240,1.322059,-3.204385,2.440368,-7.397880,7.376389,9.677288,-2.980606,6.103305,-8.405203,9.680383,-0.408475,-0.914782,8.761169,3.423273,-8.645819,2.483594,9.869511,2.543984,9.742478,8.572327,1.713663,3.850211,-8.468603,3.699454,7.904142,8.725261,2.453064,-4.523726,-7.462695,0.563009,-4.277104,-8.933532,8.434881,-0.452521,-4.703490,5.795592,-6.128285,6.039974,-2.715167,5.249161,4.255039,6.038606,-5.774656,-0.495248,8.494877,-0.501204,-0.304699,7.952301,-3.997005,-0.764222,9.460321,-8.090719,-9.183840,-8.148433,0.962805,-1.173572,0.441646,3.160313,-4.184282,-7.316851,8.155962,9.043097,-4.142985,4.870267,-0.319829,4.244317,-8.270138,-4.258524,8.585813,6.463874,-8.772959,-3.319877,0.944469,-5.105047,6.945559,4.955479,1.929576,-1.815498,2.502935,-5.534607,0.385609,0.927290,3.551573,-7.196680,-9.010976,0.420029,6.477720,-0.814868,4.908253,-3.483184,-6.630657,-7.105791,-4.315599,9.489012,-9.220786,-3.071937,3.805835,4.139431,6.399774,2.052561,0.056679,-4.616730,-7.122444,1.847633,9.782977,-5.196990,7.515144,7.333812,1.457375,7.778441,-5.668152,8.731660,0.929149,0.937949,-4.178809,6.297066,0.882620,5.184027,-1.609887,-8.296622,-0.446002,1.570720,8.405918,-8.215881,3.279160,-7.894954,7.293208,6.031821,1.821020,7.501724,-0.275218,3.636355,-7.436870,0.796620,-4.494321,9.247367,0.763240,-5.267394,9.995962,6.539281,9.825920,9.923469,-0.947366,8.483666,6.212248,8.610267,7.831841,2.528087,7.782902,4.803488,-8.789456,1.992668,4.701442,-3.623241,-2.538717,-1.583958,-1.884431,-3.559082,-3.942208,-8.483241,-5.372956,6.508153,-2.051317,6.961914,-6.620219,6.088811,3.448959,-3.037071,1.081782,-1.302244,-6.736048,7.087233,-3.214952,7.151186,9.400406,-2.540339,-8.528410,-7.326877,-8.137566,-3.817839,-1.015642,-7.279919,-6.181960,-4.741817,3.521502,0.590753,5.722261,-3.654235,-5.217848,9.433138,8.479532,9.632953,7.632576,6.943293,-0.115452,-6.588535,1.333290,-8.367002,4.179258,9.563719,7.944402,7.329606,4.480662,-6.794192,1.992075,-7.738874,8.082354,-7.706869,5.400772,5.629838,-0.250714,-4.142435,-5.257659,0.349783,7.112682,-6.450531,-1.402216,-9.060299,-9.509070,6.356122,-9.636972,-7.014419,-3.297554,-2.716204,-7.864127,5.148472,-5.011409,0.377792,-7.456334,-5.723174,4.894189,7.496796,-9.714014,-4.171294,-1.555483,9.042923,8.538378,1.503204,-8.238666,5.531791,6.431806,2.445786,-9.457731,-7.095308,-2.586259,-2.722313,0.971788,2.849418,7.254997,-7.892393,7.296896,-7.893658,-7.069462,-7.802744,-8.870146,0.301924,-8.430389,7.930912,4.272058,-9.906101,-2.983654,-0.319466,-5.527356,-8.504143,8.697976,3.586057,-4.836737,2.102794,7.547401,6.932802,1.815019,1.950558,-8.612175,-7.001154,-5.231731,9.442925,6.402673,7.002556,1.428697,-4.772233,-7.542025,8.256297,8.729332,6.140624,0.083163,-7.931350,-4.966078,-1.424341,-7.058499,-1.959353,1.008510,-3.521386,3.069053,-5.139262,6.350164,2.794215,9.527978,-0.870095,6.764977,7.795110,-2.869289,3.458692,-5.321082,2.303917,-3.248619,3.122161,1.871009,1.770475,8.775341,7.941785,-2.251263,4.215568,-7.380915,-9.093715,9.705371,-9.168552,-9.984859,-8.986036,8.104797,2.925588,-8.205301,-5.650128,-1.764514,-5.634113,1.728072,-1.857063,2.048120,2.149102,8.113761,3.499186,-7.954043,7.085623,-4.714335,2.269639,5.690708,1.163240,1.559251,-3.993647,2.355894,-9.778258,-8.945458,-7.086153,-4.005050,6.136341,-0.193610,-1.873771,-9.566885,9.474100,-9.459582,9.384888,9.664607,1.420063,-2.499410,2.759412,-3.364007,-8.571836,-9.577073,-8.352936,4.532665,1.893383,8.213410,-6.612622,1.519757,-7.138238,-1.934450,7.962646,-7.255266,-6.411853,-7.329504,5.388789,9.638332,-3.586091,-5.181435,-3.725209,-6.786260,0.723023,-3.918003,-4.952423,7.958567,9.690543,-9.716642,-8.670943,7.835699,0.681745,-9.371847,-5.068298,-0.012818,8.237847,-0.127687,-1.826772,2.381851,-5.131683,3.897387,3.161299,4.649227,-4.761227,-2.839860,-8.157567,-3.531621,2.161445,-8.793796,-4.563865,-0.962583,-0.465431,-3.345876,-7.681206,-8.012999,3.480740,9.322986,3.376493,5.081905,-0.750254,-3.539945,1.216008,-6.277837,0.262917,-0.441522,6.872840,7.536901,3.908504,5.211304,-5.082505,-8.205519,9.080337,-5.341345,-5.877465,8.944911,6.297215,-2.739137,-6.537299,-7.791146,6.468236,7.060330,5.039650,-5.481384,-9.725528,-2.705789,-4.901348,-9.533519,-6.263761,-5.871564,-3.250957,0.797079,5.924009,-1.101745,-2.061354,8.588478,-7.432798,3.960717,7.164347,-0.227372,9.219330,-2.310567,-8.331465,0.154312,-8.002438,3.150043,4.720573,-6.960407,-6.787479,-6.181682,4.952261,9.696533,1.913447,-5.170957,-7.858665,-0.101877,1.447624,5.051155,-6.196629,1.569592,-1.240386,2.213934,2.601780,-0.245058,0.792591,7.694720,-6.408911,-4.680917,0.151105], dtype = "float32")#candidate|5438|(1188,)|const|float32
call_5437 = relay.TupleGetItem(func_4877_call(relay.reshape(const_5438.astype('float32'), [9, 12, 11]), relay.reshape(const_5438.astype('float32'), [9, 12, 11]), ), 4)
call_5439 = relay.TupleGetItem(func_4880_call(relay.reshape(const_5438.astype('float32'), [9, 12, 11]), relay.reshape(const_5438.astype('float32'), [9, 12, 11]), ), 4)
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_5447 = func_2499_call()
call_5448 = func_2499_call()
output = relay.Tuple([call_5433,call_5437,const_5438,call_5447,])
output2 = relay.Tuple([call_5434,call_5439,const_5438,call_5448,])
func_5449 = relay.Function([], output)
mod['func_5449'] = func_5449
mod = relay.transform.InferType()(mod)
mutated_mod['func_5449'] = func_5449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5449_call = mutated_mod.get_global_var('func_5449')
call_5450 = func_5449_call()
output = call_5450
func_5451 = relay.Function([], output)
mutated_mod['func_5451'] = func_5451
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5452 = relay.const([[[-0.482780,6.966197,4.656005,-0.119275,-6.246107,6.955627,1.851931,-2.472340,-8.691271,-0.316766,-3.146776,3.772678],[-6.207386,-4.516004,4.233033,-5.242001,9.733533,4.666958,-3.726136,-6.759429,1.409356,4.758916,-9.524028,9.496439],[1.501887,-4.524173,-2.826201,-9.508869,-7.238252,-7.938811,-5.327078,8.967161,-7.648869,-7.193377,5.169551,-6.104633],[5.289069,6.871213,8.864436,-9.971518,-5.814393,-7.309867,-4.832378,-2.739355,8.969097,-6.939594,4.494954,7.008695],[-3.605940,-0.911262,-2.662261,0.163543,-0.020261,3.460469,7.730209,4.353286,2.529473,7.832709,-1.467598,-2.253058],[-0.143978,-8.659755,3.343470,8.225672,0.095285,8.771608,-3.043979,7.077267,2.835418,-1.389234,-0.019963,5.994802],[8.295420,9.908008,-6.439037,-3.796849,-4.590378,-6.172337,-1.974639,-6.925460,8.423390,-1.846509,-6.019888,-7.940316],[-3.209494,-6.519330,-0.435888,-5.756092,-3.087388,-5.167017,-6.596648,3.521675,1.781702,-1.195059,-8.113182,3.786790],[-0.123521,8.080008,-7.847203,-5.108280,5.607555,3.631838,-0.767793,4.473739,-9.094246,5.633382,-4.639849,2.340444]],[[-1.849308,-3.259536,-9.687639,-5.572934,3.155445,7.443216,-5.112992,-4.096243,0.115733,1.576057,-0.346456,-5.181147],[-9.979628,8.899512,4.996865,-4.452444,-9.728091,-8.523762,6.846981,2.153127,-1.574048,-5.404817,-9.141976,-9.339281],[-6.091593,-7.376936,3.694638,3.340213,-5.955654,-5.365218,-8.754136,-3.941655,6.872334,5.156702,2.804517,5.704720],[-3.680165,-1.493491,9.234356,-1.989466,1.482957,-4.033843,9.541235,-3.548433,-1.966404,8.532783,-3.723568,1.258190],[-4.002981,-7.095768,3.249998,-6.367412,1.174400,-6.767307,3.551235,-3.691161,7.171683,1.624496,9.056642,6.133423],[4.310822,-6.773770,-4.417259,0.128360,-8.740069,-3.767661,-7.568582,5.694908,-0.192250,-5.388554,-1.074348,-8.894092],[8.322439,4.859030,0.653221,-6.612202,0.260288,-9.065527,-8.919966,5.836645,2.429127,-1.250890,-9.931851,2.264608],[1.670206,-2.751771,2.595518,-1.361743,8.158423,3.311504,-1.922359,7.592207,-1.153681,5.776183,1.334437,0.003683],[-8.881466,-2.198996,-0.194975,0.645033,4.166996,9.123674,-4.306102,1.295182,4.983797,6.355266,-2.919399,-9.490774]],[[-2.158790,5.409078,-6.423102,7.918098,-1.428556,9.295927,5.485074,2.025133,-0.410765,9.512990,-6.475517,-5.814247],[4.194495,8.286700,-9.971956,-3.620266,5.541024,0.584167,2.313890,-4.881636,-2.975863,-4.189532,6.970145,7.588842],[-9.579411,-5.473942,7.183435,6.017286,-3.189450,0.694432,-7.314480,-3.680807,4.195704,0.176292,-6.178488,3.869360],[0.470180,-3.770049,2.163455,-2.968504,7.976159,-0.743042,-5.626554,6.442968,-8.166946,5.720647,0.863698,-9.268840],[2.176806,5.354571,4.847027,1.251299,-2.898149,4.328612,2.529137,0.830000,9.823152,8.810672,2.592443,-0.958780],[0.591536,-7.015789,4.870766,-5.023514,-4.379849,-6.224831,-0.091332,-9.983732,-9.397956,-5.632180,-9.401006,-5.149851],[8.558172,1.349194,-7.812583,-8.635273,6.057280,-8.166890,7.157630,-6.205761,-1.600653,2.104586,-0.647061,0.246309],[-7.481001,-0.417468,-2.660518,-8.163578,-4.270722,-5.086401,8.859736,0.466937,-0.151447,-4.225551,-3.121437,7.661600],[1.221186,1.860135,9.054491,-8.494100,-4.827634,-2.705931,1.501196,-1.330170,-5.279359,0.308438,2.951997,-9.175141]],[[-8.799314,3.051420,8.369750,-7.564272,5.992563,-1.042606,-9.927948,-7.261667,4.593324,0.421635,3.923708,7.726385],[6.023238,-5.327030,5.685797,-8.947654,3.321156,-6.165847,-0.245004,2.120453,-9.944428,-6.435859,6.118047,1.064864],[6.130015,2.452067,-4.687385,-7.741758,4.077971,-6.719665,-1.563168,8.408625,-3.361671,-5.757637,-8.918144,-4.819031],[-2.100708,3.894000,-4.723385,-2.272759,-3.340902,-1.487796,-3.459569,-8.398637,9.630388,-6.085725,0.757182,1.498799],[3.437960,-1.573021,-5.068344,-9.868602,-1.268932,-6.994589,-1.579323,-5.007595,-4.425382,3.869655,-8.191237,5.871254],[-8.711724,0.868705,8.875551,3.468297,-8.988406,-8.601378,4.144675,7.324220,-4.035691,-8.544206,9.597693,6.155831],[8.073706,-7.815451,-7.797758,-0.896302,-2.864236,-7.004551,-8.552223,-9.710522,-4.497200,9.983616,-2.853082,3.976325],[-4.336323,2.318323,-4.169251,-0.689596,-6.960872,9.655052,-8.340093,7.274971,2.292122,-2.663321,-6.658821,9.163489],[4.211032,-1.530828,4.348879,-2.044695,0.023456,2.835085,1.149394,5.149425,8.679501,-6.697202,-3.317224,-1.575102]],[[-1.989283,-8.881794,0.695374,0.113597,-4.260315,-5.123264,9.350546,-8.852764,3.212988,-5.122919,7.362026,-5.047702],[6.556066,-4.631554,-9.928994,9.570514,4.308936,1.202680,1.735972,4.616654,-2.903012,-3.760140,-0.788905,-3.380572],[-0.641446,-9.954922,6.861759,-5.303390,-5.581682,-5.789709,8.306013,3.643569,6.294744,-1.946130,2.192210,8.442442],[0.265041,2.313464,-2.090001,4.543777,-7.389143,-9.191215,-4.484641,-0.456165,0.934683,-9.528728,6.457341,6.290004],[-4.673210,1.639097,0.841710,-5.610449,-5.079449,-4.585732,8.195175,-0.905782,-1.317694,1.596798,2.327054,4.036111],[9.146258,-1.162722,0.315252,1.460836,2.507407,1.941529,7.435627,0.060941,1.730656,-2.988064,-0.035658,-6.690251],[5.834861,5.840238,-2.693718,3.031698,-6.603054,-6.867776,8.342690,-6.469492,-3.150908,1.671895,4.249508,-3.095365],[4.314352,7.919165,9.157595,-4.844697,-5.360269,6.479657,-7.467385,-7.850774,-4.260548,-5.748056,-3.279987,-4.127769],[-9.948723,7.355599,2.717714,-6.809009,-5.070127,-2.603216,8.859199,4.129079,-1.236715,-3.647643,5.684324,-8.055633]],[[2.857697,-7.578910,2.389859,5.229623,-0.790385,6.558721,-3.457614,-6.147732,5.887166,-2.220771,1.390711,-0.383195],[-0.543601,-7.180246,4.840496,-1.158257,4.877906,2.920668,1.217547,-7.916901,6.009214,0.900224,8.441625,-5.540221],[-7.746407,-4.484464,-3.425171,-7.349522,5.832151,5.385500,6.926625,-7.696334,-6.897851,6.406686,-4.710482,1.657916],[7.905868,7.715832,4.258864,0.657826,-6.045057,2.560059,5.401064,5.293688,0.597150,3.717299,-9.419782,2.043873],[9.635249,5.313300,9.502688,3.936170,3.947615,9.707215,7.056339,0.337179,-4.643832,-1.401198,-7.611971,2.823455],[-3.012722,-9.063812,-3.145913,0.361518,-8.316670,9.694852,-2.793085,-1.330417,7.218245,-2.984539,-2.768355,-2.575610],[-5.400816,-1.529970,-3.452015,-8.565856,0.166904,-4.906694,7.031050,9.024002,-1.009189,4.454078,-8.108786,-9.935846],[9.611188,-2.441380,-7.157079,6.358854,7.782451,4.898199,1.219403,2.607356,-2.697158,-0.543485,1.946683,8.587539],[-5.322932,-0.757078,-3.056807,-8.747540,1.374026,-1.768609,9.780091,9.541076,9.997554,-0.635566,-0.289529,5.602334]],[[3.170236,-9.118661,-5.974819,-5.150282,-0.422318,5.838180,-3.592793,6.735442,-5.829852,6.458886,2.690560,-4.846336],[-1.553357,2.793106,-6.942985,1.607048,-3.085175,2.833860,-1.419203,5.626207,-3.208216,5.417343,-8.610488,2.601005],[-0.228427,-2.492500,6.477701,2.002357,8.396026,-2.791416,8.737118,-0.937367,-5.809442,-2.469224,2.753276,2.728871],[-7.121379,-3.833489,5.324057,4.488473,2.116135,3.536445,7.869443,-0.441850,6.647549,-2.488770,-1.228747,-3.590591],[-7.611963,7.612797,-4.974562,-4.318094,-6.731659,4.363028,-9.400429,3.931373,-5.287288,-4.820638,0.978028,6.806362],[0.387412,-8.513336,-3.033741,-0.254050,0.109826,-7.426623,6.345300,9.496816,-7.118700,0.694455,0.894564,-6.807888],[-9.484318,9.895798,0.755730,-6.334335,1.042696,-4.842627,-0.199065,-4.986994,5.018907,9.411362,0.280584,-4.062079],[-4.067780,-5.944199,-3.838117,7.999572,3.034629,8.886094,3.691429,-6.840175,-8.646076,-7.582598,6.911111,-6.098940],[-1.273582,5.502689,-0.539910,8.772384,-8.176390,2.550298,-4.428302,1.216641,3.002399,-5.194667,-8.671023,0.585210]],[[0.612384,9.855563,1.356456,8.432223,-9.086666,6.835727,-5.167246,8.904769,4.776766,-7.305439,5.229199,0.458728],[-2.039596,-8.540281,-9.191773,7.362950,6.322894,1.823566,-7.957994,-0.613181,5.131039,-4.940492,-7.722336,-4.799359],[-1.045099,5.744413,-7.064332,-1.412138,-8.321184,-6.320643,1.711708,4.766945,-7.558832,7.204710,2.545989,3.113027],[6.671055,5.789026,4.119995,8.498792,-0.510454,-2.163459,-0.177244,6.565978,8.453261,7.037434,6.780236,8.979757],[2.754658,-3.614371,3.674984,-3.407774,9.590663,-6.914147,9.267542,-9.222429,3.925534,4.679733,-2.857584,-1.126553],[-9.110135,-1.759270,-9.430300,6.831518,-9.518918,6.368494,-9.658728,-0.519403,1.505080,-8.936775,7.634780,-8.927998],[2.916768,-9.709439,-1.345260,7.859553,-3.426868,-7.845150,-4.757685,4.619046,9.946119,-1.043501,-5.902448,-4.437141],[1.878551,-9.233061,0.097423,4.166887,-4.999841,-1.395355,8.897320,3.050169,4.217783,-8.436386,-8.539255,-9.636152],[-7.585388,8.729027,-8.862526,-4.308106,-2.310388,-9.105607,6.104264,6.242114,9.098438,-2.305184,0.726328,-3.765398]],[[3.926365,-8.693980,-3.658673,-9.974023,6.879284,9.619716,6.785982,-6.130839,1.651145,4.913526,-2.456630,-8.300332],[9.579453,-6.632524,3.528884,7.944900,-5.625628,-8.830149,9.099657,4.030909,-7.851084,-1.391792,8.712577,3.003817],[9.310557,6.193119,3.761397,9.680569,4.992597,-2.820591,-2.483673,4.411966,8.721948,-5.735460,-4.466431,-1.291623],[-2.668266,-8.270128,1.835096,-6.231350,5.344209,-7.450235,-6.642959,1.156487,-9.455408,-5.071529,3.970742,0.221846],[7.094608,6.018366,9.951388,-0.494723,-6.059887,4.777275,-5.689022,-6.145373,-3.086190,1.561174,-3.896558,-0.956641],[-7.966376,-2.657644,-1.677823,-6.495729,8.386141,-1.657223,1.737292,-2.080075,4.387355,7.237912,-4.319146,7.306392],[4.741793,4.476648,6.906454,-7.231005,-1.584924,-2.435927,-3.453009,-4.471717,-0.208821,-1.218432,0.730651,-4.502260],[4.365899,-6.436879,6.859346,-8.230396,-4.191392,7.800023,6.805074,1.167832,-5.586303,-6.182342,8.817353,-6.010887],[9.367066,4.174321,5.828751,-9.905281,-9.761610,-3.570239,-8.981112,-7.231551,-4.042466,3.810967,1.499810,5.176712]],[[-6.970356,-3.068490,-4.198898,7.553735,2.143273,-1.667221,-8.706279,1.359784,-3.630406,6.887531,-3.130994,7.306756],[6.389939,-7.942304,-4.093567,-7.846421,-7.633345,-4.640105,6.107256,-7.254416,-0.167290,9.621663,1.533768,1.063892],[2.336931,8.959542,-5.126850,-0.386541,1.864982,-4.440979,5.255328,-9.775937,4.995274,-3.360169,-5.719934,-2.596810],[-7.071103,-3.437145,-8.966413,9.467658,-9.328898,-0.523080,2.257905,-8.361211,2.750868,-5.805020,0.375890,-3.197458],[2.678067,5.236793,-9.754150,5.370593,7.122271,-8.453615,9.350189,3.429737,-0.306625,9.823164,6.979278,-0.705106],[-8.832229,1.821619,2.773137,9.103341,-7.581346,0.218494,-8.809745,9.344847,-3.760790,2.518843,9.324120,4.294943],[-1.195698,-3.603552,-1.220256,2.025552,3.751814,-7.119841,-6.370445,-8.946307,-9.972273,5.260757,-4.180817,-8.736389],[6.601040,-2.893315,2.475456,-8.310468,-9.242528,9.333398,-8.060943,-8.523374,1.998211,-5.673232,-4.438496,-4.814521],[-6.139448,6.735702,0.512935,0.209266,8.940586,4.360276,5.738262,0.812433,-6.729262,-7.516678,4.871315,9.562762]],[[1.560683,-6.718146,-0.693227,-2.895587,3.146154,6.121313,-1.496791,5.220931,-7.564515,-8.074709,-8.749405,-8.830619],[-3.079052,0.379633,4.940816,-4.762450,8.065269,-3.353460,3.830048,-7.378872,-4.394343,6.969307,4.262502,-6.038019],[-5.734912,3.983972,-5.115570,0.192789,7.226858,-3.328398,0.001908,4.185173,-1.135669,-9.895612,4.184740,-2.054268],[-9.935637,-0.111170,-4.473063,-7.269232,2.275960,9.209310,0.309633,-1.072101,-3.129841,9.621154,9.049444,-1.128308],[-6.123618,4.922261,4.926211,4.172913,-8.394664,2.077179,-1.537868,2.348856,-1.612015,-8.254638,9.895171,-7.342821],[2.489508,-8.843523,-4.528192,-9.603263,5.494009,-5.803247,6.313120,6.212651,1.713706,-3.750356,-2.368134,3.702196],[4.599499,-8.917846,-4.380498,-8.608543,-7.591337,-1.541381,0.588990,5.191168,5.274000,8.958081,1.899609,-6.086409],[-9.300925,-6.323393,-6.238068,9.130249,4.059328,-3.995679,-4.519018,-3.944115,5.451015,4.156000,0.991710,-7.924271],[4.784290,-1.386309,-8.477994,8.295878,5.290143,7.296618,-3.475853,7.049802,-7.512336,7.267695,-8.508586,0.738348]],[[3.483066,-0.157581,4.876282,7.996066,3.007714,9.732690,-0.307913,-7.294461,-1.115752,8.090652,-4.009555,7.327630],[-4.407930,1.422832,-2.379027,6.376929,5.702742,-9.397158,-9.322248,1.763181,5.467500,7.458455,-6.099521,-6.869221],[4.218048,6.774407,-4.393709,-5.416249,4.912494,-3.925656,-7.035438,0.022743,8.303536,-9.410452,2.399897,4.819768],[-0.275707,-2.583363,-4.946335,3.702331,-8.912274,4.531547,4.037199,-7.230839,1.925683,-7.254793,-1.798997,-4.274378],[-6.626278,7.442527,-9.089236,-0.214939,5.052107,2.944075,5.751495,5.042236,9.921466,6.402604,-4.024541,-1.477731],[-9.495333,3.939836,-2.360946,-0.308279,-2.184054,0.528405,2.132826,3.058389,-8.544045,-1.946980,3.952268,-9.818307],[6.808679,-7.537930,1.665262,9.183048,6.653547,-4.662042,-9.638565,-0.246716,-7.747909,-9.852624,-9.072131,-5.189285],[-9.276884,-2.300667,-8.563332,2.754830,-8.184642,2.238409,-4.693850,1.885370,5.183400,7.916165,4.573427,-3.689487],[4.569496,9.041897,-6.547549,0.673148,-4.128911,-7.419429,-4.227929,-3.959969,8.456595,-4.398638,5.796711,-4.459682]],[[8.711157,-5.243251,6.570000,-2.730624,3.564727,-4.975975,1.153787,0.813011,-2.125095,-5.597318,1.577372,5.366126],[-6.377402,-6.918710,-9.434322,-5.388149,-6.591193,-9.701048,5.701329,0.939020,-9.886141,-0.768306,8.752550,6.547610],[3.909266,-1.402937,1.860808,-0.704232,0.413425,6.963486,7.451173,0.899616,-7.999109,1.869018,-2.036268,8.132144],[0.482782,-8.694064,1.172895,-1.594733,5.766918,1.474233,-7.851912,-6.739688,-3.719060,6.628842,5.863077,7.786662],[-0.488251,6.831988,3.431326,3.531145,-2.194319,6.470834,-4.595517,-6.108237,-1.556716,-9.709172,1.136579,-4.100676],[-6.290307,6.994287,-8.045505,7.201834,-2.649053,6.714246,5.858394,-6.854354,-8.255105,3.365405,2.193003,-2.034446],[0.039051,-9.401002,3.943451,-6.184074,4.979145,1.615779,4.774594,-0.052010,3.590468,8.688254,4.613523,-2.594121],[-4.847878,-3.782919,-3.422527,8.187008,0.277893,-4.662260,2.547346,-6.878436,6.036182,-8.613000,-1.480953,-7.151174],[8.772379,0.843523,1.258031,-5.538883,3.621523,7.307345,-3.139290,-0.716219,-6.615612,-8.629184,7.019777,-4.585884]],[[5.554164,7.737756,-4.968522,5.084126,-8.699828,-9.702182,3.877251,6.348923,0.580784,-5.089912,3.186565,4.592811],[2.176620,5.231444,-0.980170,9.371019,7.285743,7.909089,-7.854486,6.326959,1.923204,-2.207357,-8.390108,-8.195160],[-8.000087,0.988281,5.537505,-4.377508,0.971004,7.745974,5.520099,9.181170,-6.454645,-4.287773,5.431651,0.918882],[9.194754,4.895077,6.494118,6.727619,-2.914642,4.505342,2.861464,6.543912,-5.008404,-8.233500,3.942200,-7.268239],[5.312463,8.345326,-3.374208,5.752842,-7.142665,5.044753,-2.296369,-9.689174,-6.086004,-3.918126,0.038654,-8.759602],[2.616661,5.945261,-5.900794,-2.416002,0.324119,-9.729959,-2.727520,3.276857,7.989698,-1.223697,-8.604387,-9.173829],[-9.721011,-0.289332,-3.206334,2.345917,-6.253605,8.118078,-1.401755,-9.002270,6.316236,8.547371,-7.169167,-7.230000],[-1.352443,-4.277433,3.117187,8.492319,9.910518,9.284428,-2.440378,2.152009,-1.373570,8.013208,-5.463406,-3.273957],[-2.937726,9.053886,-0.936637,-9.409343,-0.009623,0.204236,-8.307738,-4.948214,4.942577,5.625537,-5.265247,-3.231768]],[[8.165763,-8.861105,2.784248,7.375073,-6.048417,-8.180204,9.890381,6.673078,8.504633,4.421203,1.709384,-2.049443],[-5.919159,-9.274761,-1.857869,4.285757,-1.016958,-9.800386,-5.413194,-8.102656,-4.147581,9.472045,6.624787,-4.112453],[-1.593597,-5.545031,7.290757,-4.262537,0.302219,-2.948296,2.835355,0.091087,5.771652,4.522787,-1.801342,4.872318],[-3.652076,-5.397982,6.929294,9.382156,-3.944202,-9.384510,-1.455832,5.175286,2.001449,8.699199,5.876902,7.935346],[-6.351518,-5.647618,-1.014084,-8.586221,8.572582,-1.268708,8.381844,-7.739937,-7.521266,0.305507,0.156214,-7.611174],[-8.582668,6.419618,-4.219866,4.528258,7.545147,0.231548,5.833672,-1.716747,-2.666045,6.292526,-4.628185,-8.598402],[-2.922201,8.230847,-5.372577,2.511187,-4.973581,9.075170,6.072148,7.322410,-7.943000,-5.280322,-9.782683,-6.538514],[3.855709,-6.936455,1.169997,-6.644655,-0.092380,1.435229,5.875897,-3.624487,8.144881,6.962952,-6.095594,2.882607],[5.136743,-4.578155,3.883832,3.281770,-5.761559,-3.732285,-5.756609,-5.578039,1.713647,0.411535,-4.496810,-8.386800]],[[0.437542,-2.729451,-7.424211,8.802197,5.905552,-8.763908,-4.148856,9.553833,8.501551,9.318980,9.134331,5.360158],[5.224319,6.738770,-6.361739,-1.142620,4.714197,2.943391,-5.152036,-1.513277,-2.958885,-8.106716,-7.966204,9.630000],[-8.948791,6.061304,-8.390818,-7.552642,8.360498,4.667733,5.336328,-1.015103,-3.814388,-3.229054,-1.199858,-4.514925],[2.671979,1.238323,1.318690,-8.810000,6.898115,2.891775,-0.093176,-9.386769,2.988085,9.542771,7.393064,-1.263808],[9.423649,-0.183163,2.281750,-6.674450,-5.804443,-3.835834,-6.115975,3.075984,-0.928050,-4.639332,-7.626243,-0.705881],[-2.422123,-9.709836,1.815937,-7.584664,4.235499,-6.914038,4.179953,-3.551553,9.600144,6.167227,5.990948,7.883443],[2.033570,-4.738186,-2.213262,-3.511356,-6.136915,-2.095029,0.601458,-7.478297,-3.616865,9.239310,8.738582,1.214182],[-8.553789,-8.667536,8.305077,3.877573,6.631250,-8.959427,-9.828756,0.615223,4.862705,1.265018,-0.059334,5.398282],[-2.213900,-9.655052,-7.771957,-4.014741,6.840373,-3.943280,1.573936,1.789728,5.180106,-2.897306,-7.909609,-4.519563]]], dtype = "float64")#candidate|5452|(16, 9, 12)|const|float64
var_5453 = relay.var("var_5453", dtype = "float64", shape = (16, 9, 12))#candidate|5453|(16, 9, 12)|var|float64
bop_5454 = relay.maximum(const_5452.astype('float64'), relay.reshape(var_5453.astype('float64'), relay.shape_of(const_5452))) # shape=(16, 9, 12)
output = relay.Tuple([bop_5454,])
output2 = relay.Tuple([bop_5454,])
func_5476 = relay.Function([var_5453,], output)
mod['func_5476'] = func_5476
mod = relay.transform.InferType()(mod)
mutated_mod['func_5476'] = func_5476
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5477 = relay.var("var_5477", dtype = "float64", shape = (16, 9, 12))#candidate|5477|(16, 9, 12)|var|float64
func_5476_call = mutated_mod.get_global_var('func_5476')
call_5478 = func_5476_call(var_5477)
output = call_5478
func_5479 = relay.Function([var_5477], output)
mutated_mod['func_5479'] = func_5479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_5520 = relay.TupleGetItem(func_1891_call(), 0)
call_5521 = relay.TupleGetItem(func_1892_call(), 0)
output = relay.Tuple([call_5520,])
output2 = relay.Tuple([call_5521,])
func_5535 = relay.Function([], output)
mod['func_5535'] = func_5535
mod = relay.transform.InferType()(mod)
output = func_5535()
func_5536 = relay.Function([], output)
mutated_mod['func_5536'] = func_5536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mod.get_global_var('func_4501')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_5566 = func_4501_call()
call_5567 = func_4501_call()
output = relay.Tuple([call_5566,])
output2 = relay.Tuple([call_5567,])
func_5576 = relay.Function([], output)
mod['func_5576'] = func_5576
mod = relay.transform.InferType()(mod)
output = func_5576()
func_5577 = relay.Function([], output)
mutated_mod['func_5577'] = func_5577
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5654 = relay.const([[[-3.323296,8.737688,-2.600362,2.287213,3.966698,-0.457401,1.562924,-0.045155,7.008474,-8.329565,3.773388],[-6.916239,5.923842,5.399742,3.341408,-1.383717,5.709199,5.408330,4.775088,2.588963,-6.544626,7.501903],[-4.073040,-0.395439,8.588580,5.822185,4.509825,1.513575,-4.549883,1.934369,0.795454,1.258707,0.482887],[-6.452044,-1.106580,-1.333968,-0.103037,-6.069235,7.246335,-1.683660,9.596408,-3.086138,8.626611,1.917989],[-8.813948,-0.497629,-3.397979,-3.681066,-5.297629,8.837384,-4.081852,7.035038,9.897142,-9.724721,-0.284205],[6.799135,-4.067511,-5.461833,4.684678,6.221463,9.949660,0.039516,6.518057,8.849338,8.645281,-3.350998],[-2.525570,-4.619346,6.312256,9.305982,7.626493,-8.692455,-4.249209,-6.819531,-5.723538,0.792000,0.302256],[-1.589548,9.605465,-9.306147,-6.727086,-7.518867,-2.128823,-3.818728,5.343488,-6.007864,9.145399,-8.108804],[6.361173,1.246370,-1.648641,3.541630,-2.899147,2.330004,-3.608660,-4.813737,-5.871267,4.300374,0.391365],[0.330330,1.709205,3.401535,-8.954582,-9.756821,-4.380476,4.591433,1.093752,-3.910843,-8.179618,2.474459]],[[2.000645,7.294931,-0.836065,9.538098,2.867840,9.340851,-2.410814,9.174924,-3.480223,-0.169917,9.812224],[-4.015243,1.486205,-9.327055,-3.443500,-6.433077,5.117692,9.242094,-6.066165,3.536297,1.483690,0.298178],[-2.068042,-2.269145,-3.646948,7.212604,5.291340,-0.828587,2.151160,-6.562117,-2.454186,0.701505,1.971771],[-0.834489,5.944538,3.165947,-6.655538,-6.502749,0.236303,6.410665,-8.673092,1.776130,-6.396466,-5.052047],[5.504619,7.851949,8.644276,2.279212,-3.696195,-7.843563,-9.245730,-8.090822,-3.482102,6.118594,-0.325473],[-2.626243,4.064299,-8.694687,6.522719,8.316762,6.553888,9.833371,-9.252919,0.731291,-4.862567,-4.903090],[6.839676,7.214310,-7.347729,8.998644,8.871288,3.164701,-1.500842,9.873050,-5.668288,-0.245796,5.645176],[-3.573674,-0.722530,-6.767285,0.728648,0.199767,-9.289167,4.138070,6.359696,1.322124,-8.485783,-6.861573],[-6.784872,-3.039380,-4.627785,-8.605285,-5.326586,9.837835,2.263245,3.370608,2.021248,3.317205,7.131570],[-6.526075,-1.531668,-3.897680,-0.854021,7.717572,-9.830160,0.901770,-9.972862,-8.707708,-3.093683,9.237571]],[[-2.915428,-3.053958,-8.272688,2.631052,-0.947974,-7.783513,2.758078,4.525740,9.754125,-5.092200,8.736697],[6.097692,9.281002,-2.806928,5.372238,3.735439,5.872291,9.579553,-3.624663,2.299663,-6.328315,2.692440],[-5.053598,8.806484,7.036065,0.370665,5.966961,-5.185349,0.182032,-7.005399,-8.906890,-7.066456,-9.467561],[6.483094,-1.534969,7.197793,1.551557,-6.375166,-0.820250,6.899080,6.215594,-7.372582,3.944995,9.313962],[0.211083,-4.258824,-1.758331,8.332980,-1.353156,8.690175,-2.736516,-8.234532,6.194583,9.561957,-3.738057],[9.226081,-8.232574,2.776554,-7.379702,-9.514381,-7.444632,1.651022,2.337132,6.484860,-8.199291,-8.189532],[-9.722126,-6.090234,6.942849,3.499180,-2.807355,3.094715,-5.504888,3.235282,9.177586,-2.623511,-9.103133],[-3.444188,2.018587,1.488320,-3.402959,-7.529676,-6.059785,-1.089488,-7.133067,-0.337284,-4.656041,2.555207],[-6.041503,7.025453,-0.916183,0.457410,-1.884511,-4.719773,-2.163136,5.181129,4.806701,5.743950,-8.139651],[7.548867,9.204345,5.201766,6.955418,-0.633627,6.104565,-1.761167,1.494923,-6.392344,4.472397,1.574641]],[[1.610802,7.781870,-3.877215,-4.091409,-0.585242,-4.149295,0.336070,-6.610858,-3.490696,-1.016527,-8.167250],[-0.988566,3.171353,9.590933,2.629249,-8.762375,5.831232,-3.501740,-3.750162,-9.316803,-5.892799,-6.268358],[8.988510,8.303231,4.413148,5.556568,-3.496340,4.845857,2.775745,-2.984434,-9.003073,3.214646,-1.995085],[3.494434,-8.824907,-7.680454,-7.812082,1.343240,2.640204,-9.074013,-1.063414,-8.546125,0.560362,-7.069240],[3.094674,3.260036,6.822659,9.178347,-3.836491,-9.364531,0.832055,-0.949273,7.163414,9.951358,-9.474888],[0.664367,4.637608,8.509916,-4.114484,5.045651,-6.601309,8.437878,8.836416,-8.488850,3.560618,3.983203],[7.797342,4.210562,3.326553,0.292752,-8.230027,-6.462042,-0.760871,-4.353888,-2.277108,-4.045611,-0.367850],[-3.571129,3.153343,-8.823061,-9.636424,2.499294,8.273610,-0.813119,3.583267,-3.266820,3.131470,8.516776],[-5.587059,-3.820615,-0.223829,3.767310,-1.676859,-9.172040,-1.356238,-6.208221,-6.099502,-6.236552,-8.093993],[-6.459322,-1.542947,8.823169,-9.225313,-8.735450,-0.461024,2.839505,9.781424,-3.261606,-4.359927,3.686612]],[[4.371903,5.971082,6.779434,7.805250,5.673608,7.005992,-5.403712,1.196335,-8.684277,3.014946,-7.878992],[0.826672,5.523498,3.976145,-4.583240,2.834578,-9.139785,-8.699292,-7.733832,-8.826152,9.387669,-6.487662],[-4.692763,-8.972497,6.227016,-1.463702,-3.778177,3.507870,5.577452,-7.579769,-5.489672,7.394320,-2.642073],[-3.888756,0.501526,-4.533562,7.573514,-1.515480,-8.925516,-9.175645,-1.537235,1.176412,-2.553315,-5.994718],[5.615109,2.268316,-8.065727,6.429108,-3.941251,-2.735514,-0.095900,3.604109,9.484792,3.233352,-7.018309],[8.337182,-0.925470,-5.670806,2.735914,-1.484203,5.335685,-3.556529,-7.780479,-5.108301,-5.585602,-6.373001],[-9.480513,-2.809786,1.009428,3.067652,5.777559,-6.412468,-1.243637,-7.199383,-5.861211,-7.662009,-0.611482],[5.213517,-1.554425,-7.250054,-6.881151,6.279039,-4.707104,-1.426578,-5.610811,3.298326,-1.500720,3.876158],[-6.081972,2.968185,2.335703,-7.958994,-0.890822,-1.031620,-4.061190,8.302903,-8.332805,3.687624,-5.303256],[-0.136206,2.710185,-4.439232,-3.155742,-5.487273,1.889595,6.702394,-8.556144,0.615248,8.109323,6.462554]],[[-1.120017,2.677749,-1.000748,2.641569,-8.861662,5.610663,7.806952,-6.652836,8.510898,7.396085,-9.293505],[1.562286,-3.659694,2.284685,8.380592,2.716909,-2.742691,-4.628215,3.083263,0.259903,3.318027,-6.382177],[7.367055,-9.231754,2.807744,1.301939,-3.720741,-1.683472,7.890309,5.372644,2.105302,-0.882118,7.961183],[-0.008396,-6.796123,-7.446771,-9.977186,3.426421,8.665039,-3.765526,8.109127,-0.093565,0.669412,-2.555578],[6.227935,1.687342,6.168313,-9.858385,-1.775527,1.417970,-3.416076,-1.354874,-1.640535,-5.526595,-8.716730],[8.171237,8.102979,7.481223,-7.739694,1.749605,9.195186,-3.326977,6.190178,6.829182,3.024758,-9.315923],[0.555628,-1.654313,-0.552282,3.544335,-3.106040,-2.238000,8.980079,-6.836949,-4.482656,2.693705,-7.415845],[-3.400798,-5.156474,7.095262,-5.269680,5.251717,-6.910002,-9.458266,5.819590,9.462666,-7.650650,6.168466],[-3.020709,0.360178,1.369550,-1.432814,5.469497,3.796397,5.878705,1.722426,1.893118,0.003207,2.779192],[-0.564241,3.174560,-8.593751,-5.163480,5.270484,8.641701,4.801809,1.015058,-6.150616,-1.135021,-0.303859]],[[-6.607799,4.426131,4.867169,3.571060,-7.304333,3.673543,-7.005372,3.183385,8.176203,6.085426,-7.957397],[7.215652,-2.831609,-4.177099,-9.279505,-9.260569,-7.221967,-8.219981,-8.954183,-5.556904,8.450717,9.998836],[1.776644,-9.816422,3.532820,9.049278,-8.452236,-1.713062,-8.768866,4.380617,8.983200,6.433505,-8.720443],[6.083846,-0.873249,2.961049,2.054805,1.466347,-5.450847,8.738835,9.449128,9.778240,-5.824230,-1.682368],[-5.093724,9.337612,-0.906416,0.055958,-2.574255,2.571268,5.602668,-5.823485,3.188957,3.887433,-0.580645],[-7.305957,-1.093573,3.065847,9.627307,1.065212,-6.577025,8.774715,-3.589527,7.242796,-3.366183,3.063550],[5.141860,-4.508675,7.161221,-3.821574,5.686802,5.215140,-2.628365,-8.007856,-7.162962,9.284774,-7.019640],[4.822701,-9.468779,6.908105,-8.298893,-2.185774,-7.399336,-9.137901,-0.130286,0.785575,3.940778,2.788491],[-8.538691,4.206891,-3.512820,3.282681,-7.350540,6.603388,1.200478,5.296308,6.838122,5.926917,-2.626321],[7.198070,8.751055,-9.999658,3.465795,-1.161212,1.953558,-8.437203,1.758557,-7.608823,2.274879,-2.330609]],[[-4.953479,-1.090832,9.097352,-3.720679,2.268795,-9.742056,-6.050314,-7.269652,5.518696,4.081724,-0.406410],[-3.884192,6.244850,8.446124,-9.263542,5.595494,5.363215,-4.865028,-0.555359,8.943781,-3.361390,-9.629405],[-8.520094,-5.850906,3.781070,8.054364,9.769907,4.996211,-9.298054,7.846787,-7.014239,-6.529192,-2.252940],[-3.339354,0.153914,5.163709,-2.788391,-5.420935,-1.694216,-5.528958,8.563903,9.358669,2.392273,4.187836],[-2.547986,-2.867819,-0.977230,-4.238272,4.104413,8.078622,-8.981227,-0.531647,-9.427682,-5.671452,0.558563],[-3.351288,-5.477529,4.184075,1.979302,2.837035,-8.579633,-6.333700,-0.042893,5.386653,-1.195299,-1.962975],[8.845860,1.726656,-0.358287,-5.961940,-1.551497,-6.531642,9.447886,-3.915599,-6.611621,-9.608787,9.493684],[6.101968,5.396917,4.513474,6.018855,9.283264,-9.621254,-2.693833,-4.516568,-9.709490,-2.104428,0.211571],[-9.750465,-2.690923,1.161528,2.434203,1.262323,5.918450,-6.169803,-3.996484,-8.808515,-9.445046,-2.802112],[3.366686,-5.862702,1.127070,-5.890229,-3.069753,-8.457281,-5.780506,5.752912,-7.344715,-0.490886,8.671365]],[[-8.931021,6.241346,6.702613,7.595626,-9.809562,-7.480422,-4.936561,3.880807,-8.141781,-2.222203,-3.223637],[1.016071,-8.512811,1.559583,3.530533,2.826472,-3.672449,-9.925047,8.310696,-6.824245,1.091767,-0.354803],[-3.777636,-6.912507,5.897449,-1.866535,5.764975,9.936218,7.068783,3.921843,9.608799,9.205865,1.849034],[-8.091169,5.401259,-0.300961,9.343673,7.998763,6.207849,4.995756,-6.567189,-7.180086,1.767951,3.799866],[-4.007174,9.884544,-0.626360,-3.238552,-0.276027,-0.686986,6.524757,-5.829559,4.994441,-5.930347,-9.958153],[6.943152,9.198225,-9.530776,3.758342,-7.779457,-3.316704,1.020309,-6.870702,-0.532830,-5.512278,-4.859304],[-3.598241,1.756673,-2.008854,-9.144041,9.627987,0.754821,7.862603,7.295412,-8.057831,3.203476,1.602558],[7.512596,-1.076992,-1.305878,-8.661152,-9.780733,-2.875742,-8.707699,0.202454,5.354353,-0.758889,-1.465926],[-6.965142,-2.615942,5.840135,-0.260815,-3.597102,-2.842985,3.116223,-9.537206,3.090612,-1.601995,-8.629498],[0.626021,4.213333,-8.648105,3.669625,-6.009777,-0.838616,-2.790663,-5.926295,-4.003551,-2.244212,4.331404]],[[5.927294,9.307526,-2.992109,-4.053998,-8.923354,-4.667682,-4.254663,7.016638,7.261849,-8.380475,-6.611683],[6.119435,3.309244,-6.652346,-1.113364,4.333398,9.255426,9.212337,7.264643,-0.933049,8.835445,7.591006],[8.241021,9.875834,-5.524774,-1.057467,0.192319,4.446957,6.764843,-6.004803,7.059605,5.208067,1.857343],[-4.592695,1.767195,-7.533405,-1.157240,-3.109571,9.039809,-5.025574,8.900838,-2.296582,9.521323,0.434551],[9.887349,-7.363510,-2.564937,0.578418,-6.789678,-9.740979,-9.514729,-5.528065,-3.968726,-9.946541,1.457372],[-0.041495,2.566400,3.728304,-7.052992,4.795303,-6.220052,1.979872,-4.132711,-3.536470,-1.920626,-1.556808],[-6.110460,8.844119,9.695218,-0.491279,5.681210,-6.881345,1.178461,4.567564,-0.045352,-8.076227,-8.917816],[2.249274,-4.675054,-6.194336,-6.224645,-5.696467,6.256888,-7.423353,6.259190,2.008128,9.261762,-5.125150],[7.597091,-4.564250,-3.944145,7.096712,-9.404562,7.888742,-8.029450,-8.634866,-1.336592,3.572311,-5.126967],[1.033050,-6.553600,-6.338901,-7.058740,4.026804,-4.981913,3.188185,-8.607416,-7.649702,-3.672608,5.416735]],[[2.143228,5.227532,-8.550603,0.502130,-1.412846,6.173351,-9.742715,-3.993408,-7.571647,-5.802263,-2.674784],[4.292916,-9.429603,9.122271,-7.811137,-0.383630,-2.900879,4.928998,-5.433713,-5.574012,9.493475,-7.715611],[0.287910,-7.258144,-3.256032,6.567766,5.000802,6.582852,-6.714386,-7.165967,3.499043,-3.320078,-6.854985],[4.544519,-8.472337,-0.714694,7.103478,2.727546,8.045425,-1.114167,2.642397,-3.660111,-9.767996,-9.760526],[8.932184,4.560088,0.529729,-7.481756,-9.900716,2.131301,0.698935,-2.358771,-2.317249,-9.872021,-4.039779],[5.548530,-8.875366,-9.015637,8.618181,0.706469,2.210879,9.535814,-9.238469,-1.037566,1.703287,9.188540],[0.357560,2.389753,-4.052861,-6.026039,-4.109627,-4.088530,6.110560,-7.554841,6.325570,1.175319,-3.143492],[-9.907349,5.358750,8.678549,-0.049153,2.478669,3.697191,9.982248,-9.986972,-9.615877,3.787677,2.857586],[5.776233,4.429722,7.006391,3.221978,4.056872,-2.656875,-5.268045,-6.160763,3.364608,3.402783,-4.128196],[-4.236651,-7.216354,-3.802800,7.178483,-6.773982,9.994016,5.784482,2.742114,-8.009974,-0.134927,0.713878]],[[2.474411,4.529552,5.294342,4.779897,3.161343,6.772403,-9.446991,0.027056,9.970456,-4.903595,1.361967],[-0.969456,-3.442043,-6.094767,5.371098,7.161228,9.890522,1.490196,1.994022,-7.082386,-4.378455,-4.945776],[0.677300,-5.364358,-8.271198,6.852081,5.755910,-3.152269,7.012518,-4.299868,-1.614616,6.169190,5.616959],[-8.055448,3.135164,4.753551,-2.470276,-3.439626,-2.215086,6.322804,0.144578,-1.834583,-4.131757,-5.718449],[9.928452,-1.875608,-3.354096,3.464389,9.784344,6.550081,7.148660,-6.901146,-3.978158,3.796549,-3.545484],[8.563027,-9.422803,-2.325563,-9.439467,-4.576860,9.320221,4.308786,-5.240210,9.223283,1.755396,-0.107913],[-5.291926,-2.880174,0.417458,1.343476,-8.501249,9.606354,-1.083917,4.785792,-2.567842,4.994989,0.501812],[5.099498,7.420925,6.740829,5.820016,0.904540,-9.121016,1.041094,-4.485902,5.478586,6.936223,2.257650],[-9.744333,6.666432,-9.895384,1.581599,5.718428,7.032852,3.223151,1.324461,-4.535811,-7.963787,0.046487],[-7.715597,-4.905119,-3.268542,-1.851661,-0.634381,2.339524,2.299845,-4.178025,8.606162,9.097940,-3.470795]],[[2.260417,-7.839914,4.976229,-8.254725,-6.391908,-4.756031,4.329078,-8.302723,-1.904641,-9.644189,-2.001735],[4.201279,-5.246617,8.525912,7.304005,3.901019,7.629261,-4.630481,-5.216761,7.315702,4.096417,-3.819219],[1.595356,-3.311451,6.058686,8.489908,-9.722870,-4.124578,9.864576,-6.957316,6.428908,1.062627,3.549648],[9.528386,-6.585209,-5.042846,-5.539658,-5.535211,-4.526348,5.652334,-3.980223,1.824616,8.875918,9.498223],[6.473853,1.534441,9.793021,-0.453305,-1.950107,0.347067,-1.620285,-5.695391,-4.523848,-3.515503,9.446846],[-9.742553,-4.486064,-7.522988,3.725520,-6.829626,-1.957865,2.847537,-1.131116,-9.912015,-5.320861,-5.268261],[-6.812640,9.313846,9.861408,3.302120,-0.964246,-8.233209,5.474532,-1.674041,0.458071,-4.838389,8.045310],[9.203858,1.641727,-3.915037,0.537901,-8.911949,-2.767141,-6.679811,-5.831860,-3.522949,1.946230,7.610629],[-5.452504,7.006686,7.143503,5.428495,-8.199987,-4.708775,-7.409098,6.447137,9.749914,6.164368,5.123436],[-4.663170,3.684855,-5.157605,3.295376,-8.322967,-1.037498,1.906980,2.436598,-2.252488,-6.210864,5.948132]]], dtype = "float64")#candidate|5654|(13, 10, 11)|const|float64
uop_5655 = relay.acos(const_5654.astype('float64')) # shape=(13, 10, 11)
output = uop_5655
output2 = uop_5655
func_5660 = relay.Function([], output)
mod['func_5660'] = func_5660
mod = relay.transform.InferType()(mod)
mutated_mod['func_5660'] = func_5660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5660_call = mutated_mod.get_global_var('func_5660')
call_5661 = func_5660_call()
output = call_5661
func_5662 = relay.Function([], output)
mutated_mod['func_5662'] = func_5662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2472_call = mod.get_global_var('func_2472')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_5679 = relay.TupleGetItem(func_2472_call(), 1)
call_5680 = relay.TupleGetItem(func_2473_call(), 1)
uop_5683 = relay.erf(call_5679.astype('float32')) # shape=(9, 12, 1)
uop_5685 = relay.erf(call_5680.astype('float32')) # shape=(9, 12, 1)
func_3454_call = mod.get_global_var('func_3454')
func_3457_call = mutated_mod.get_global_var('func_3457')
const_5695 = relay.const([[-7.790471],[1.587264],[-3.253635],[-0.341274],[-1.540966],[1.736580],[-9.610886],[-1.318506],[-1.669426],[-0.891979],[-4.148602],[-1.993132],[-6.457919],[-7.424016],[-7.062173],[7.024955],[-1.536794],[6.465465],[-8.343768],[-5.043414],[5.259601],[3.664643],[-8.128211],[1.885553],[1.567895],[8.976502],[-3.076050],[-5.870156],[8.884333],[6.724217],[-6.297289],[-2.623598],[2.038904],[-6.322825],[3.609402],[-1.153778],[-9.255214],[5.926754],[8.497835],[1.669332],[-5.472518],[5.136733],[-1.412383],[1.212514],[-2.484112],[3.891108],[-7.746179],[-0.336012],[6.658015],[6.930259],[0.896352],[3.328605],[0.899579],[-8.363308],[-0.142020],[-8.935922],[-5.639659],[7.253386],[0.009386],[2.088062],[6.109937],[0.306039],[-6.916963],[6.365339],[-4.564282],[4.894810],[-3.716358],[8.261809],[0.415959],[2.792250],[6.584557],[-7.685513],[6.472378],[8.264707],[-6.045037],[-2.142557],[0.431696],[1.174205],[8.405225],[-2.587127],[9.421607],[-5.412066],[-1.968385],[-3.305295],[4.148181],[0.462850],[3.344784],[2.466516],[1.965215],[1.161319],[4.561542],[9.438559],[0.305945],[-3.159319],[5.639909],[-4.672114],[-2.377515],[7.806432],[-3.406151],[-0.136179],[8.856989],[5.752050],[5.021661],[2.673190],[2.837645],[9.327598],[-3.207883],[0.026690],[9.502179],[4.647231],[-3.013806],[-2.380024],[-3.325706],[-5.840446],[3.990934],[-2.391565],[-3.695337],[3.597629],[-9.451168],[4.004271],[7.092330],[-6.884665],[6.449739],[-7.604879],[-5.086318],[-9.675970],[5.956714],[8.839801],[-9.656573],[7.992964],[9.246780],[-8.551102],[5.644560],[4.422780],[-0.124107],[3.317308],[0.043558],[9.651807],[3.463186],[-9.117614],[5.760451],[8.548908],[3.021771],[-5.943703],[-0.791456],[8.581296],[-4.912477],[8.903981],[1.176595],[5.921735],[1.035875],[4.395464],[3.937692],[-7.718255],[-4.310537],[-1.119925],[0.426686],[5.836381],[-6.071106],[-5.380371],[3.168849],[-8.170177],[2.418809],[0.961943],[4.468061],[-2.270565],[6.521738],[9.761170],[-3.817171],[2.820927],[-4.703011],[5.595159],[9.434564],[-5.788148],[-1.614246],[-5.906058],[-7.989579],[2.519833],[0.863091],[-5.164459],[-1.033448],[5.834307],[7.782315],[-5.822452],[-0.332449],[-0.531287],[4.423734],[-2.076443],[-1.001106],[-7.158009],[0.304746],[-0.023037],[-6.031233],[5.285199],[-7.024076],[-7.085622],[-1.696045],[-0.484666],[-8.844872],[-9.830004],[0.595406],[-8.763269],[-5.358108],[2.268817],[6.177983],[8.972218],[3.903970],[5.402010],[-2.350318],[9.357322],[-7.046855],[6.646956],[6.153508],[-7.246814],[-4.621868],[4.089094],[-8.464904],[-3.461180],[-0.033886],[0.880649],[4.555130],[4.210992],[7.557294],[-8.517913],[6.551890],[-6.068692],[4.982581],[0.194889],[-6.305709],[6.361557],[-9.538848],[-5.264055],[-6.500259],[8.140689],[-2.750374],[-4.402691],[6.949140],[-3.951041],[-1.796438],[-5.699230],[-1.642228],[-3.292370],[-4.226752],[2.132624],[2.041726],[8.668515],[5.145828],[-0.261602],[-1.101707],[-3.605484],[3.572918],[8.932659],[-3.603721],[5.791223],[-2.892737],[9.445689],[-4.239573],[4.003008],[5.505818],[2.412457],[1.438432],[-2.802496],[-0.113154],[-9.602647],[-9.100045],[-9.637567],[4.165850],[-0.117557],[5.132759],[2.069391],[-5.725661],[0.174338],[-3.555953],[6.740632],[8.815113],[-6.010356],[-8.361491],[9.747672],[-8.338066],[9.332957],[-0.156261],[-4.522414],[6.571615],[-8.797719],[-5.914703],[0.935282],[-6.079335],[1.858379],[0.106168],[-8.274571],[-5.763977],[4.483643],[6.736510],[7.810079],[-8.525092],[-9.281258],[-7.563042],[-8.606191],[6.267902],[6.845405],[-6.890172],[-5.447594],[3.983311],[3.441463],[4.793884],[4.752333],[3.143066],[-1.272480],[2.559650],[-1.524791],[-0.859916],[-0.569160],[5.189652],[9.989550],[4.777727],[-7.100961],[6.966360],[-1.707431],[-8.821800],[9.863624],[9.490981],[4.618607],[0.695686],[8.723776]], dtype = "float64")#candidate|5695|(324, 1)|const|float64
var_5696 = relay.var("var_5696", dtype = "float32", shape = (1, 54))#candidate|5696|(1, 54)|var|float32
call_5694 = relay.TupleGetItem(func_3454_call(relay.reshape(const_5695.astype('float64'), [9, 36]), relay.reshape(var_5696.astype('float32'), [9, 6]), ), 7)
call_5697 = relay.TupleGetItem(func_3457_call(relay.reshape(const_5695.astype('float64'), [9, 36]), relay.reshape(var_5696.astype('float32'), [9, 6]), ), 7)
var_5698 = relay.var("var_5698", dtype = "float32", shape = (9, 12, 8))#candidate|5698|(9, 12, 8)|var|float32
bop_5699 = relay.bitwise_and(uop_5683.astype('int64'), var_5698.astype('int64')) # shape=(9, 12, 8)
bop_5702 = relay.bitwise_and(uop_5685.astype('int64'), var_5698.astype('int64')) # shape=(9, 12, 8)
output = relay.Tuple([call_5694,const_5695,var_5696,bop_5699,])
output2 = relay.Tuple([call_5697,const_5695,var_5696,bop_5702,])
func_5703 = relay.Function([var_5696,var_5698,], output)
mod['func_5703'] = func_5703
mod = relay.transform.InferType()(mod)
mutated_mod['func_5703'] = func_5703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5703_call = mutated_mod.get_global_var('func_5703')
var_5705 = relay.var("var_5705", dtype = "float32", shape = (1, 54))#candidate|5705|(1, 54)|var|float32
var_5706 = relay.var("var_5706", dtype = "float32", shape = (9, 12, 8))#candidate|5706|(9, 12, 8)|var|float32
call_5704 = func_5703_call(var_5705,var_5706,)
output = call_5704
func_5707 = relay.Function([var_5705,var_5706,], output)
mutated_mod['func_5707'] = func_5707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4585_call = mod.get_global_var('func_4585')
func_4587_call = mutated_mod.get_global_var('func_4587')
call_5722 = func_4585_call()
call_5723 = func_4585_call()
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
const_5725 = relay.const([-1.095552,6.297597,5.052582,8.960898,-9.970742,8.875134,2.421740,-1.368466,-0.189111,0.778275,1.585028,-3.656482,0.902085,4.134059,-4.108090,3.507751,6.016669,-3.499974,2.271601,2.372304,-2.358427,8.625085,1.828584,1.797844,2.072605,6.774124,-6.309343,4.224271,7.864430,-7.933394,2.429212,-1.347167,-4.591404,7.567992,8.555274,3.822201,-6.374073,1.640872,-4.605509,3.305166,8.217483,8.768394,-3.603177,3.549414,8.300295,1.027212,-8.778266,-6.537316,-3.450720,-9.440971,-1.090552,-9.540339,-7.160973,6.986803], dtype = "float32")#candidate|5725|(54,)|const|float32
call_5724 = relay.TupleGetItem(func_4061_call(relay.reshape(const_5725.astype('float32'), [54,])), 0)
call_5726 = relay.TupleGetItem(func_4064_call(relay.reshape(const_5725.astype('float32'), [54,])), 0)
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
call_5740 = relay.TupleGetItem(func_4061_call(relay.reshape(const_5725.astype('float32'), [54,])), 3)
call_5741 = relay.TupleGetItem(func_4064_call(relay.reshape(const_5725.astype('float32'), [54,])), 3)
func_5175_call = mod.get_global_var('func_5175')
func_5176_call = mutated_mod.get_global_var('func_5176')
call_5747 = relay.TupleGetItem(func_5175_call(), 4)
call_5748 = relay.TupleGetItem(func_5176_call(), 4)
func_50_call = mod.get_global_var('func_50')
func_53_call = mutated_mod.get_global_var('func_53')
var_5752 = relay.var("var_5752", dtype = "float32", shape = (360,))#candidate|5752|(360,)|var|float32
call_5751 = func_50_call(relay.reshape(var_5752.astype('float32'), [3, 10, 12]))
call_5753 = func_50_call(relay.reshape(var_5752.astype('float32'), [3, 10, 12]))
var_5769 = relay.var("var_5769", dtype = "float64", shape = (16, 2, 16))#candidate|5769|(16, 2, 16)|var|float64
bop_5770 = relay.greater(call_5722.astype('bool'), var_5769.astype('bool')) # shape=(16, 2, 16)
bop_5773 = relay.greater(call_5723.astype('bool'), var_5769.astype('bool')) # shape=(16, 2, 16)
output = relay.Tuple([call_5724,const_5725,call_5740,call_5747,call_5751,var_5752,bop_5770,])
output2 = relay.Tuple([call_5726,const_5725,call_5741,call_5748,call_5753,var_5752,bop_5773,])
func_5777 = relay.Function([var_5752,var_5769,], output)
mod['func_5777'] = func_5777
mod = relay.transform.InferType()(mod)
var_5778 = relay.var("var_5778", dtype = "float32", shape = (360,))#candidate|5778|(360,)|var|float32
var_5779 = relay.var("var_5779", dtype = "float64", shape = (16, 2, 16))#candidate|5779|(16, 2, 16)|var|float64
output = func_5777(var_5778,var_5779,)
func_5780 = relay.Function([var_5778,var_5779,], output)
mutated_mod['func_5780'] = func_5780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mod.get_global_var('func_4501')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_5800 = func_4501_call()
call_5801 = func_4501_call()
func_3266_call = mod.get_global_var('func_3266')
func_3269_call = mutated_mod.get_global_var('func_3269')
var_5812 = relay.var("var_5812", dtype = "float64", shape = (540,))#candidate|5812|(540,)|var|float64
call_5811 = relay.TupleGetItem(func_3266_call(relay.reshape(var_5812.astype('float64'), [540,])), 0)
call_5813 = relay.TupleGetItem(func_3269_call(relay.reshape(var_5812.astype('float64'), [540,])), 0)
func_4801_call = mod.get_global_var('func_4801')
func_4803_call = mutated_mod.get_global_var('func_4803')
const_5815 = relay.const([1,-5,-1,-5,3,8,-1,8,-5,10,-2,-1,-1,9,10,-4,-1,2,-7,7,-8,-10,6,-6,-6,-4,7,3,10,1,-3,10,3,-6,-8,2,9,-7,-10,7,1,6,5,-6,-5,-6,2,-2,8,5,2,2,-1,-8,3,-9,-7,2,6,8,5,-10,9,-3,-4,3,-8,-7,5,2,-3,2,-7,1,-10,-7,-2,-3,-2,6], dtype = "int8")#candidate|5815|(80,)|const|int8
call_5814 = relay.TupleGetItem(func_4801_call(relay.reshape(const_5815.astype('int8'), [4, 4, 5])), 2)
call_5816 = relay.TupleGetItem(func_4803_call(relay.reshape(const_5815.astype('int8'), [4, 4, 5])), 2)
func_3700_call = mod.get_global_var('func_3700')
func_3702_call = mutated_mod.get_global_var('func_3702')
call_5818 = func_3700_call()
call_5819 = func_3700_call()
output = relay.Tuple([call_5800,call_5811,var_5812,call_5814,const_5815,call_5818,])
output2 = relay.Tuple([call_5801,call_5813,var_5812,call_5816,const_5815,call_5819,])
func_5825 = relay.Function([var_5812,], output)
mod['func_5825'] = func_5825
mod = relay.transform.InferType()(mod)
var_5826 = relay.var("var_5826", dtype = "float64", shape = (540,))#candidate|5826|(540,)|var|float64
output = func_5825(var_5826)
func_5827 = relay.Function([var_5826], output)
mutated_mod['func_5827'] = func_5827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3629_call = mod.get_global_var('func_3629')
func_3630_call = mutated_mod.get_global_var('func_3630')
call_5840 = relay.TupleGetItem(func_3629_call(), 1)
call_5841 = relay.TupleGetItem(func_3630_call(), 1)
func_1771_call = mod.get_global_var('func_1771')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_5844 = func_1771_call()
call_5845 = func_1771_call()
func_4682_call = mod.get_global_var('func_4682')
func_4683_call = mutated_mod.get_global_var('func_4683')
call_5846 = func_4682_call()
call_5847 = func_4682_call()
func_3992_call = mod.get_global_var('func_3992')
func_3995_call = mutated_mod.get_global_var('func_3995')
const_5851 = relay.const([3.477918,0.995425,-4.067350,3.926978,-7.530956,-9.850490,-0.611995,-0.174862,-7.525088,8.661961,1.078029,9.565307,5.239589,9.117847,-5.842380,2.534015,0.824326,-6.939229,-9.842197,7.287777,8.588545,-5.929407,-5.271082,9.179088,-8.894136,-6.434576,9.607449,9.149055,4.498204,3.107932,-9.761612,-5.591370,-3.842953,2.120160,-9.520467,5.111476,-8.421952,0.432180,-3.763954,6.580716,5.578550,-4.578052,1.728489,0.941507,-6.444674,-9.840141,6.191495,-8.539895,-9.863897,-4.516216,4.913412,-8.658376,3.172656,-3.757610,-8.038300,-7.914568,0.195341,-2.913079,0.343170,-7.318499,-5.955828,-4.417295,6.991568,3.336963,6.227959,-6.916306,2.840947,-7.576190,-0.838542,-7.955046,2.545705,-2.912413,4.976142,9.007185,-4.529980,3.084400,4.479648,-2.870107,-4.455336,-4.924501,3.700308,-0.472372,9.222312,-1.972153,6.828301,-2.572343,3.891765,-4.911741,2.921306,0.396220,6.765146,-3.914611,7.695968,8.883150,9.781322,9.284333,-2.047295,5.638764,-0.424205,6.524168,0.028231,-0.764225,-1.042257,1.586078,7.481935,0.310887,5.304135,3.077451,-7.564850,5.408379,-2.699632,-2.507357,-8.177151,-3.689786,3.172581,7.985852,8.348542,-9.469119,-8.874586,0.635839,-9.145884,-2.713816,-4.273461,-9.729705,-8.516834,-1.528539,-3.515238,4.964026,7.295268,-0.980567,7.911121,0.581204,0.641994,-9.443583,6.886986,8.322449,-8.071370,-9.273589,8.901581,1.566402,-6.145767,-4.044428,-2.406077,5.930434,5.883423,7.997066,6.083142,1.568731,-7.576809,-3.191995,7.414362,7.808680,9.940793,4.882846,4.056376,-9.429706,-5.719602,-0.103380,-0.150166,-5.832995,1.400159,-4.620334,-7.088783,-0.128217,1.544120,5.489133,-9.583148,-3.231974,-3.472672,5.954863,-3.248623,6.409726,-0.051204,-6.971744,2.933577,0.148916,-7.366269,-1.668877,5.565884,5.612524,3.537804,-4.842311,3.105729,-9.054491,-4.799450,5.778415,1.505527,8.253699,5.796394,6.581642,9.410000,9.947360,-8.599963,-4.907087,-5.449873,0.982530,-1.843545,-3.762538,-5.038872,1.448457,-5.695580,-7.587629,0.042874,2.503070,1.572386,-4.202784,3.469821,-2.260622,4.839801,-7.905215,-6.298392,4.326055,0.542985,-7.387405,-8.480258,-0.863027,8.398459,8.267470,-0.546624,8.618816,2.728770,-9.710128,9.264666,-5.161316,-3.633513,5.806960,-8.357697,4.785144,-7.689530,-8.850769,-8.082884,5.117928,1.160350,-3.782264,9.958813,3.402326,1.723605,-0.643612,-6.605977,5.401286,5.641589,5.825847,-7.863109,6.767451,-5.736127,5.480872,-4.472766,-9.541396,8.343582,5.174567,-9.352061,8.342027,6.970274,4.861060,7.861114,-1.810345,1.861266,-5.541619,-9.705505,-1.184864,4.199666,5.376748,-4.124312,4.060641,3.127907,-7.059096,5.756622,3.141840,8.007319,-0.706953,-0.478741,9.399472,-4.751125,6.809107,5.864405,-7.161664,3.307197,-8.409256,6.490011,-1.968282,1.841157,1.543559,-4.866583,8.622539,1.557269,-8.458597,-1.718257,7.436239,-0.918680,6.799205,-3.691499,-8.083726,-8.970461,6.358343,0.507163,-4.525127,-8.584230,3.579131,-4.810260,3.684846,5.404205,2.266985,2.247519,-9.317296,4.486520,-7.945564,1.584698,-7.273804,5.215637,-4.447766,7.457733,2.647290,-9.033454,-3.855409,7.722116,-3.475057,-2.003083,-6.076918,-9.730603,9.927627,7.987750,7.247313,-2.916753,-4.723944,9.883313,-0.967339,0.847907,-5.051881,5.417230,-4.049720,-8.640682,4.678448,8.979327,1.757559,-0.242132,3.208490,-4.187721,1.514732,-7.431844,-7.903066,-3.501317,-9.736075,6.931291,1.818021,-7.582597,2.404883,-3.519002,3.145221,9.106629,0.224116,5.643174,0.792184,2.390319,-6.628762,-0.351550,7.770140,-1.187927,-6.538914,-7.798911,-5.522979,8.014934,-9.678307,-8.816547,3.000523,-7.921035,1.888036,-6.457776,0.899694,0.628274,5.565472,-1.343626,-5.571733,1.712441,-5.940077,-8.158673,-5.269433,0.337652,2.451405,-3.943078,7.760456,8.421466,-2.594850,2.677743,3.488306,2.243030,-1.185370,8.437158,-5.908503,5.370443,1.029882,3.765583,5.314370,-3.703699,-0.104708,-8.856565,4.599453,6.766446,0.797089,4.857405,7.059721,9.628341,-9.553860,0.539531,6.257050,-6.874881,-8.837872,-6.299679,-4.325707,1.233101,6.258461,-9.423108,4.705526,-1.249695,-7.309976,-2.302283,7.265586,3.197400,-2.428443,-1.741892,1.858494,-5.115849,6.109796,0.783564,8.899264,-1.949198,-5.901326,6.035542,-1.139083,-0.868764,8.034722,1.465866,0.391284,2.959308,1.263657,3.094202,-4.863178,-0.734294,5.003827,0.956309,-7.945499,8.320736,-5.887292,3.971108,8.939492,0.330688,-7.965254,5.957234,4.337385,4.181324,-8.967576,6.898209,0.707069,-9.184083,8.407432,6.100730,-0.264338,9.644991,-7.502284,6.717925,-2.856396,-3.833138,9.987445,-9.981967,-7.558844,0.759366,5.807014,2.688493,3.915923,7.198966,8.910370,-0.075389,5.924377,-9.774511,-9.611477,0.133766,-7.230534,4.181317,9.570805,-5.982626,-0.682150], dtype = "float64")#candidate|5851|(480,)|const|float64
call_5850 = func_3992_call(relay.reshape(const_5851.astype('float64'), [3, 10, 16]))
call_5852 = func_3992_call(relay.reshape(const_5851.astype('float64'), [3, 10, 16]))
var_5860 = relay.var("var_5860", dtype = "float64", shape = (324,))#candidate|5860|(324,)|var|float64
bop_5861 = relay.right_shift(call_5840.astype('uint64'), relay.reshape(var_5860.astype('uint64'), relay.shape_of(call_5840))) # shape=(324,)
bop_5864 = relay.right_shift(call_5841.astype('uint64'), relay.reshape(var_5860.astype('uint64'), relay.shape_of(call_5841))) # shape=(324,)
var_5866 = relay.var("var_5866", dtype = "float64", shape = (9, 12, 16))#candidate|5866|(9, 12, 16)|var|float64
bop_5867 = relay.right_shift(call_5844.astype('int16'), var_5866.astype('int16')) # shape=(9, 12, 16)
bop_5870 = relay.right_shift(call_5845.astype('int16'), var_5866.astype('int16')) # shape=(9, 12, 16)
func_3454_call = mod.get_global_var('func_3454')
func_3457_call = mutated_mod.get_global_var('func_3457')
const_5875 = relay.const([-7.549045,-8.683156,-4.906714,-6.860997,-2.368067,3.115322,3.810523,3.266051,-8.252696,6.112260,-7.176071,0.649791,-8.785786,8.033193,-1.890776,1.967275,8.790031,9.714425,8.793426,-4.880641,-3.677636,-2.493370,-5.850808,-4.427362,-7.652531,-6.282108,0.959853,2.539057,9.765996,1.144888,5.998225,1.038134,-8.947611,9.497234,-0.021246,4.924733,6.593289,5.273800,6.686256,0.517745,4.737516,-3.953032,1.136444,4.764001,4.842183,-9.695055,9.272187,8.864759,0.712912,9.845947,-1.650688,-6.311090,3.779530,2.759732], dtype = "float32")#candidate|5875|(54,)|const|float32
call_5874 = relay.TupleGetItem(func_3454_call(relay.reshape(bop_5861.astype('float64'), [9, 36]), relay.reshape(const_5875.astype('float32'), [9, 6]), ), 8)
call_5876 = relay.TupleGetItem(func_3457_call(relay.reshape(bop_5861.astype('float64'), [9, 36]), relay.reshape(const_5875.astype('float32'), [9, 6]), ), 8)
output = relay.Tuple([call_5846,call_5850,const_5851,bop_5861,bop_5867,call_5874,const_5875,])
output2 = relay.Tuple([call_5847,call_5852,const_5851,bop_5864,bop_5870,call_5876,const_5875,])
func_5879 = relay.Function([var_5860,var_5866,], output)
mod['func_5879'] = func_5879
mod = relay.transform.InferType()(mod)
mutated_mod['func_5879'] = func_5879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5879_call = mutated_mod.get_global_var('func_5879')
var_5881 = relay.var("var_5881", dtype = "float64", shape = (324,))#candidate|5881|(324,)|var|float64
var_5882 = relay.var("var_5882", dtype = "float64", shape = (9, 12, 16))#candidate|5882|(9, 12, 16)|var|float64
call_5880 = func_5879_call(var_5881,var_5882,)
output = call_5880
func_5883 = relay.Function([var_5881,var_5882,], output)
mutated_mod['func_5883'] = func_5883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4585_call = mod.get_global_var('func_4585')
func_4587_call = mutated_mod.get_global_var('func_4587')
call_5893 = func_4585_call()
call_5894 = func_4585_call()
func_1771_call = mod.get_global_var('func_1771')
func_1772_call = mutated_mod.get_global_var('func_1772')
call_5906 = func_1771_call()
call_5907 = func_1771_call()
func_4522_call = mod.get_global_var('func_4522')
func_4523_call = mutated_mod.get_global_var('func_4523')
call_5929 = relay.TupleGetItem(func_4522_call(), 0)
call_5930 = relay.TupleGetItem(func_4523_call(), 0)
output = relay.Tuple([call_5893,call_5906,call_5929,])
output2 = relay.Tuple([call_5894,call_5907,call_5930,])
func_5958 = relay.Function([], output)
mod['func_5958'] = func_5958
mod = relay.transform.InferType()(mod)
mutated_mod['func_5958'] = func_5958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5958_call = mutated_mod.get_global_var('func_5958')
call_5959 = func_5958_call()
output = call_5959
func_5960 = relay.Function([], output)
mutated_mod['func_5960'] = func_5960
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5964 = relay.const([[[-9.131410,-9.903987,-5.694006,-5.532191,8.642824,-5.434291,-8.504484,-2.689151,-6.860450,-2.289454,-8.076647,-3.940388,-7.487952,3.870541,3.612230,-9.358828],[-6.976117,0.938577,-9.961680,-8.870916,-8.354551,7.055420,3.361030,5.069185,3.966043,-9.713633,-0.491657,7.946975,-6.667097,1.975769,3.740393,1.494414],[-2.401716,5.683589,2.255243,-0.924892,-1.787686,-9.169672,-8.246110,4.229933,9.619932,1.091004,-4.313553,8.640937,4.505191,-6.488298,-6.718082,-0.353460],[5.103411,8.204084,-9.145989,-9.230439,0.680216,-8.983719,3.248746,-9.921306,5.334186,-0.257428,-9.598526,-3.034648,1.085505,7.857308,5.903492,-2.570878],[9.540928,6.201278,-3.647563,-2.378908,-4.691708,5.785412,3.206940,0.911654,5.567665,-3.772632,9.493285,0.825575,-4.225902,-6.740494,0.176070,-0.803193],[9.207978,-5.364878,3.269749,0.370759,8.202580,6.267856,-9.575280,4.473865,2.849493,-4.444528,3.206104,7.170010,-4.619358,5.165637,-9.776469,-3.274537]],[[5.400104,4.554016,9.761464,-0.841105,0.738916,0.663378,-8.083435,5.390650,4.320751,-0.676553,-2.931293,-1.263485,-0.995508,-6.804610,9.966475,-2.268038],[2.442367,3.442653,-3.566407,4.884135,-3.356392,-0.481271,4.293487,-5.568495,0.360441,4.769636,-1.109451,-1.434246,6.063283,8.875908,4.144307,8.472279],[-9.419588,2.504912,4.010363,-6.617799,-8.989072,-2.081070,7.986959,-4.373094,-3.718801,-1.163175,9.123403,7.093698,8.225466,2.780723,-6.251644,8.442462],[4.423054,0.663269,1.328419,-7.385621,-0.456540,1.638217,5.258030,-3.925182,-6.328746,-8.198803,6.247730,-1.755163,8.848612,8.664231,0.014091,-4.295754],[-7.081446,0.865230,7.342575,8.483685,-8.937166,2.021929,-8.579766,4.566625,-9.846436,-9.097485,1.964992,-6.311863,-8.075669,-9.842727,-4.369338,-0.637663],[9.415184,-9.816835,-5.664034,-6.801083,5.975274,-4.178560,-0.941381,-9.307596,-6.900286,-3.013985,0.496060,-7.597083,6.096997,3.682872,4.446080,-3.226832]],[[4.977810,9.775031,-1.150908,9.225030,-4.390515,6.090738,0.551459,6.164224,-4.586389,-0.046668,8.507228,4.098887,0.426160,-2.744614,-2.573475,7.156445],[-8.502722,0.758811,1.696758,-3.273548,6.836887,-9.928967,7.612147,-7.210694,7.913570,2.391935,4.320340,0.866744,-3.140912,0.623055,-3.201077,-6.466059],[9.458026,3.535608,-6.510672,-8.330938,9.089289,8.821221,6.656893,-1.681618,-7.696964,4.691793,-6.984332,-6.286850,-2.661135,-8.819999,9.719760,9.089244],[-8.790095,7.981464,-5.722950,-7.991454,-9.029920,-6.756630,9.680350,-2.093568,1.847249,1.209405,0.596201,-4.672830,7.882628,-1.900448,8.883031,-4.382153],[2.000983,2.852515,1.005875,3.533970,3.745721,1.576053,0.621796,-6.314550,8.550128,-7.537494,2.071745,0.186832,7.961988,5.397755,5.513582,0.881631],[8.258640,0.800573,-8.856313,-0.430051,-8.025558,1.667334,-7.973079,-4.433715,3.033182,-8.688505,2.023134,-4.813673,0.113057,-6.232801,7.700056,5.403078]],[[-3.870164,2.494224,-4.449452,-3.666826,-6.519556,-3.716791,3.373088,-6.165847,4.369267,5.581230,-5.115890,-6.618403,-9.599884,9.939045,-6.155164,-7.603001],[5.819085,9.655234,-3.480202,-6.526808,6.668864,7.354447,-2.881547,-3.902458,-9.299130,-0.446202,0.148891,-8.053234,9.395033,0.346526,7.463528,-7.127358],[5.028053,-8.685070,8.022473,-1.315568,3.141678,1.718075,-9.905236,7.139531,-5.667079,8.911059,-8.715791,6.770350,3.808623,0.681427,-0.191682,0.545030],[-3.510411,0.601801,5.125920,-4.115072,0.723990,-9.832397,5.503376,-8.658210,8.268643,5.835534,-8.524071,-8.035220,6.836829,-0.445381,9.162701,-0.241443],[7.342358,-3.592647,2.421856,0.709322,-4.986389,-4.591599,9.704162,3.409191,9.542516,2.072429,9.422800,3.623423,1.868475,4.593940,-6.043253,-2.600280],[4.134996,-2.251925,-4.376195,-8.771429,4.961115,-0.774365,3.558364,5.299766,9.162515,-8.957063,-5.939404,8.580314,3.871851,1.851474,-9.367685,6.414865]],[[-3.196793,3.940857,6.342549,3.140637,-4.499957,-3.363252,-4.624194,-0.496519,-5.226334,-0.695027,4.410928,-8.308007,-3.989846,-9.301249,-5.347403,6.211324],[4.797974,0.745749,-4.343280,7.529407,-9.097311,-7.110415,2.500234,-2.684139,-6.836899,3.436093,7.423206,-4.557272,8.607161,-6.396806,2.668326,-4.717471],[-8.800181,5.347909,-4.740637,-5.202783,-1.047722,5.372460,7.619627,1.061675,5.717539,0.548615,9.502662,-5.152226,-7.325431,-5.469318,-3.039615,-8.412667],[-2.494371,7.149786,-8.091172,0.880415,6.713272,0.862283,7.713004,-4.795392,2.181813,2.611862,9.769293,2.606393,-2.274517,6.810911,-0.349026,-4.854906],[-1.181497,7.960829,7.276608,4.801053,-5.235061,3.717226,-3.606602,-6.889450,-4.321645,-0.090912,6.103121,8.286297,0.861395,1.366463,3.863166,-3.545275],[5.613747,-4.178238,-3.769043,4.457021,-1.957514,-9.920314,-6.315456,-2.596034,-1.616762,6.004357,-2.286918,-9.083867,3.672630,6.409269,8.569392,-3.761883]],[[-0.216943,0.947734,8.252522,4.208041,0.740177,-9.299413,-4.146324,-6.255338,5.376216,-1.114416,3.833499,6.975119,-3.746063,4.911070,-9.130305,2.828484],[-3.147900,4.155540,1.969861,-6.489979,9.201983,7.209007,3.350691,-7.576443,8.006783,6.897084,9.558747,3.465054,5.785599,1.959199,6.422080,-6.424725],[7.227565,6.363421,-5.629827,-9.538089,-4.229563,6.930473,5.648096,-6.734457,3.617270,6.214696,-2.809914,-4.300371,5.866703,9.610664,-7.310311,6.796720],[7.952868,2.389977,-6.063406,3.273052,5.150824,-9.597143,6.333863,8.722762,-1.879905,0.460706,6.674347,2.922216,-6.540848,0.186713,-6.695575,-9.785402],[5.969850,-2.241605,3.742609,-7.102705,-7.118460,-0.203470,3.131136,-5.624145,-7.095635,-1.910808,-6.022540,4.143566,-0.941314,7.403306,7.480835,4.074370],[8.088914,-5.066146,1.890132,9.177318,8.787012,0.373687,0.276296,9.240646,-3.233135,-0.575053,4.684689,5.595548,-2.087279,-9.781200,-7.573688,3.619968]],[[5.412485,7.390431,-2.746654,2.343539,-8.262247,0.630771,-6.662040,0.557560,-7.974570,3.794069,0.274342,-5.522663,-3.662492,0.729651,-4.509610,-8.725918],[-0.461063,-0.210463,2.213686,8.338010,3.558924,4.143678,8.711040,-2.661143,-5.495350,1.901698,-2.573905,-4.480340,-1.405237,8.203820,-1.681940,6.758371],[0.058181,2.000989,8.206488,-9.519006,2.838769,-0.088350,6.539210,0.494188,6.821444,4.670792,-9.537704,-6.171385,-5.077520,7.824097,4.527397,5.280096],[-8.881857,7.599477,4.859437,-7.818677,-0.835708,4.836512,8.720638,3.569700,9.476069,-8.194765,-9.415460,4.155834,5.749583,1.229484,4.647658,6.515645],[-3.437896,7.594818,1.373259,-7.232844,-2.507609,5.067656,-4.543893,-9.280198,3.932493,4.126011,3.708952,-1.731491,4.839738,-8.813648,0.600065,3.020161],[-8.946211,8.326136,-3.723461,6.808203,-9.879572,7.560417,-0.877653,-9.586584,-0.734061,0.622276,-2.330523,-4.138577,-4.186275,-3.800317,6.686758,3.053940]],[[-7.886981,2.956363,-8.181996,-7.280942,0.807535,-1.487487,9.514017,4.629459,-6.047697,-8.678855,3.350100,7.831392,4.099563,1.119483,5.479696,-2.190801],[9.378192,-3.942179,2.242274,-2.553721,-9.959837,-2.475856,-0.184073,-1.517769,-1.553112,3.110709,1.654459,4.569653,7.635159,2.641109,5.432414,-4.376449],[6.767198,4.871759,7.598920,0.104542,-9.629862,-3.175039,-5.666079,9.563316,4.630783,-2.570222,4.584878,4.232282,-3.244694,0.486044,-8.068168,-6.346541],[4.642201,-5.814897,-9.261550,-9.122169,7.799747,0.684380,5.366819,6.196147,5.647949,-3.301610,5.140160,7.009827,-0.331632,-9.643018,2.150542,9.815932],[-2.243499,8.575816,4.543941,5.163521,-6.722298,-8.094777,1.406383,-0.898945,8.683625,-2.444872,-0.677112,-6.238361,-9.536786,-2.608083,-1.464899,-3.317660],[1.990241,2.657171,-4.907603,-0.459624,7.234998,-8.731783,-6.102456,8.538070,8.766788,-8.478432,-5.941024,9.009296,2.366293,-1.619249,3.864563,-6.008055]],[[-8.439808,9.238671,-5.692415,-9.083856,0.858393,5.409761,1.792877,6.471409,-0.514211,2.260546,6.940738,4.827775,-3.778695,-4.678035,4.651492,-0.992620],[-2.572792,-8.649462,5.821632,-4.748765,1.429274,-4.144336,-9.847451,-5.382290,-3.389331,9.668816,-7.006964,-1.149250,-9.268402,-3.258925,-5.749096,-1.056733],[-9.430884,4.588128,3.990838,-6.814560,1.647581,7.244908,7.494892,-5.067490,1.631957,4.763466,6.876354,-4.762148,-6.093938,9.115709,-7.841098,5.327330],[-4.703165,-6.097705,-5.361506,-2.341472,-6.598012,2.759467,0.970483,0.031241,-9.020631,-8.273602,-1.955846,9.045708,8.248649,7.875526,-3.012778,1.281187],[-3.665580,-4.358852,-6.968337,-8.408724,4.149409,-8.705160,-3.654290,6.610067,-1.487110,-8.985293,6.854962,3.654296,-5.695573,-0.523542,0.440158,2.247430],[2.998120,-8.781498,-0.818349,-7.679544,1.284727,3.496842,-5.359893,-9.746310,-0.406417,-0.205067,-0.902459,8.294472,-8.310153,-5.609805,1.383254,9.163633]],[[5.422312,-9.228731,4.544931,4.573694,-3.623281,-5.717621,-8.396269,6.413629,8.508024,-8.795986,-5.735584,-6.131263,3.562275,-2.569320,-5.175755,8.931111],[-6.468164,9.388425,6.459875,-2.771545,6.694660,-4.078769,4.095163,7.564924,1.494797,-1.145584,1.765468,4.860472,5.434036,6.591428,9.160480,-1.939077],[-6.041594,2.498868,-8.565780,7.278037,-1.654582,6.981104,-6.629156,-6.446409,-8.911072,0.533094,2.283783,-7.372321,-7.281529,-5.258208,9.545691,0.758994],[9.799671,7.767192,-7.001692,5.412980,-6.418147,-9.084349,2.915247,6.830249,-7.798870,3.429422,5.690224,-2.656790,7.369564,5.497013,3.313688,8.651661],[-3.245113,9.542911,9.852001,0.721990,6.277422,-6.378190,9.209150,3.455427,-1.539640,9.050856,-1.733065,-8.534969,8.690986,-8.577034,-0.641833,1.884132],[-0.453248,-9.951865,7.994961,-4.421091,5.473365,-2.322219,-8.016946,-4.351153,-9.522625,-3.578200,-3.244774,7.687729,-0.234318,-5.130444,7.611818,3.950527]],[[-4.471969,4.120310,-3.603167,6.764610,3.875549,-5.514372,5.729839,-9.464991,-9.083466,-6.423848,5.117355,-2.204739,-4.808518,3.843113,-6.612074,6.628273],[-5.878636,8.229603,-5.700856,-5.714204,-2.110178,4.838573,-7.092196,3.402487,-3.438671,5.262908,4.123823,-6.990135,-5.974119,1.945512,-9.454925,-0.053257],[-0.613471,0.223021,-2.233206,-4.064614,-6.755013,-4.942726,2.075524,-0.334848,1.381044,-0.349133,9.984251,-6.567717,-5.773427,4.996576,1.631715,8.788206],[9.737930,-2.982694,-7.822932,-4.799005,1.794913,5.327757,-6.097324,-3.413324,2.847544,2.328487,7.474390,6.574309,6.588195,3.528106,-4.781095,-2.133335],[4.872634,3.725296,3.559117,2.657741,-8.077652,-5.153858,-3.197256,-4.448160,1.956265,-7.609273,-4.933379,-6.586029,-6.675030,-2.214989,-1.322801,-4.203054],[2.885694,4.592014,7.998456,4.394714,-1.501410,4.634623,5.145611,-6.818429,9.297921,2.753942,-2.626950,8.554372,3.206736,2.943839,2.943698,-8.671258]],[[0.632150,7.067169,-4.116596,-6.857259,-7.072333,2.688273,-3.503261,-8.334453,-7.784312,4.002459,5.806580,-4.108253,-7.547060,-7.776119,3.926680,-6.536287],[6.111787,-6.435093,1.391984,-7.468315,-5.037024,2.018004,3.971502,-6.928105,9.361606,4.660533,-7.023414,-0.001106,1.314430,-3.976219,8.718799,-6.106254],[4.032622,-5.730749,3.103660,-7.159307,-4.712050,-6.010120,-5.800820,9.303841,-3.969752,-3.795658,-3.963607,7.811964,-0.329696,1.990137,1.530874,-2.393677],[-8.740909,6.323747,6.936645,7.935115,1.897232,6.380602,-2.106368,4.692331,6.705536,4.449553,-0.961913,-8.540790,1.100977,-6.445387,6.049477,8.332113],[9.165166,1.954630,-0.024532,-8.005883,0.402682,4.776746,7.903908,-3.125287,0.750500,-6.296866,8.661590,-0.098440,-3.894991,5.475456,5.534880,1.435477],[1.827434,8.347572,1.893063,0.131151,9.562853,-0.620809,3.647412,-9.434645,1.625683,6.581669,5.724951,9.717403,-4.401062,0.659599,1.314038,7.090955]],[[8.427411,-2.532705,-3.302809,3.872553,1.888224,-0.162165,1.616441,0.679583,-7.700841,7.996023,-4.059086,3.172090,3.412371,-0.257850,-4.992904,1.746265],[-0.101238,-7.573573,3.016512,-6.532114,-4.482893,0.799075,8.059340,-4.848249,1.867840,2.614635,-5.122635,6.329438,0.369365,-9.749674,4.432930,-1.120335],[1.077093,-9.051092,-8.023665,2.309409,-5.064488,-0.575396,4.137078,6.308610,-1.815130,-0.927714,9.952465,-9.365168,9.674446,-6.172972,-0.849205,-2.756687],[-3.226733,-4.966117,-4.964523,9.062040,9.780435,-7.112744,-2.523166,0.420751,9.031137,0.874301,7.078449,8.232028,-8.205723,2.526361,-4.704473,-7.968724],[3.079531,-7.057775,8.757706,-1.200873,6.953995,6.177390,-5.311648,7.628602,0.186577,-8.605206,-1.316109,5.484793,-1.572486,-0.116395,2.560408,7.223800],[5.276744,-6.297002,4.713853,9.970913,8.880085,-5.909438,-4.853004,7.147421,-0.527616,-6.721978,-6.917759,2.922234,1.509497,5.634694,-6.463704,2.752113]],[[-4.208071,-8.051775,-6.357772,3.439101,3.016271,3.076638,6.185957,3.793699,-5.083164,-3.778250,1.743663,1.681372,3.456000,6.065555,5.829383,-8.887620],[-1.044845,7.941339,-0.021789,7.584753,-9.075971,5.770869,3.896760,1.793688,1.173039,-6.566398,9.303740,1.024081,2.838010,0.489234,3.568915,-1.993029],[-5.648841,-7.670484,-3.476142,-3.941674,-3.659230,-2.987484,-4.821888,8.161821,-6.970799,7.834578,-1.573883,-7.879355,8.654448,-7.873558,9.135604,6.070933],[4.037845,4.167853,9.489537,-0.641735,1.977794,8.139997,4.112709,8.934184,6.106948,5.332199,7.513030,7.107796,0.670025,2.571057,-4.182940,2.106245],[-0.662162,-8.235111,-9.707903,3.668361,3.883984,-6.824089,-2.862653,-8.541542,-5.277716,8.669007,-2.300493,-1.111138,-3.766969,-0.362609,-1.212241,-9.159071],[-4.250670,-2.579606,-5.440909,9.985262,0.162579,-1.285792,4.558766,5.341745,-8.693420,-6.160715,0.347239,1.401956,-3.201331,-0.846466,9.886271,-6.076548]],[[3.050028,-2.624764,-2.272344,-6.274466,9.176890,1.276113,8.883739,-5.436087,3.132319,-8.804686,-7.360275,1.361344,-6.514056,1.610182,-4.342429,5.542633],[3.007950,2.340943,2.529113,2.768351,-1.799585,-0.775441,5.158193,-4.081790,5.608684,6.914957,-3.581467,-2.388840,-0.771636,-4.951783,0.788456,3.872425],[0.170614,3.054065,-0.183903,-8.744861,9.359990,-0.119513,5.957242,-6.551002,-4.217276,-6.556869,-5.956951,2.246816,4.105723,9.201326,2.546941,9.445952],[-6.614995,-0.649599,3.410913,7.750988,6.850208,6.618094,-2.701536,2.286875,7.170425,4.678904,-1.739873,-3.097190,-0.592108,2.060163,-9.229773,7.564325],[0.218018,7.740917,-2.480063,2.286657,2.165984,-8.544975,-0.005934,-3.296306,-3.481646,6.991039,-6.293289,-7.819467,-1.837308,-0.443084,-8.009585,0.649756],[5.255917,-8.741085,5.322062,3.122893,-2.050302,1.454503,0.181071,-5.479734,4.476037,9.191269,8.520000,4.530598,2.663211,7.771146,2.742486,1.044876]]], dtype = "float32")#candidate|5964|(15, 6, 16)|const|float32
uop_5965 = relay.atanh(const_5964.astype('float32')) # shape=(15, 6, 16)
bop_5973 = relay.add(uop_5965.astype('int16'), relay.reshape(const_5964.astype('int16'), relay.shape_of(uop_5965))) # shape=(15, 6, 16)
var_5982 = relay.var("var_5982", dtype = "float32", shape = (15, 6, 16))#candidate|5982|(15, 6, 16)|var|float32
bop_5983 = relay.maximum(uop_5965.astype('uint16'), relay.reshape(var_5982.astype('uint16'), relay.shape_of(uop_5965))) # shape=(15, 6, 16)
func_2553_call = mod.get_global_var('func_2553')
func_2555_call = mutated_mod.get_global_var('func_2555')
call_5987 = relay.TupleGetItem(func_2553_call(), 0)
call_5988 = relay.TupleGetItem(func_2555_call(), 0)
func_4165_call = mod.get_global_var('func_4165')
func_4168_call = mutated_mod.get_global_var('func_4168')
var_5998 = relay.var("var_5998", dtype = "float64", shape = (1188,))#candidate|5998|(1188,)|var|float64
call_5997 = relay.TupleGetItem(func_4165_call(relay.reshape(var_5998.astype('float64'), [9, 12, 11])), 0)
call_5999 = relay.TupleGetItem(func_4168_call(relay.reshape(var_5998.astype('float64'), [9, 12, 11])), 0)
bop_6011 = relay.multiply(var_5998.astype('uint8'), relay.reshape(call_5997.astype('uint8'), relay.shape_of(var_5998))) # shape=(1188,)
bop_6014 = relay.multiply(var_5998.astype('uint8'), relay.reshape(call_5999.astype('uint8'), relay.shape_of(var_5998))) # shape=(1188,)
output = relay.Tuple([bop_5973,bop_5983,call_5987,bop_6011,])
output2 = relay.Tuple([bop_5973,bop_5983,call_5988,bop_6014,])
func_6027 = relay.Function([var_5982,var_5998,], output)
mod['func_6027'] = func_6027
mod = relay.transform.InferType()(mod)
var_6028 = relay.var("var_6028", dtype = "float32", shape = (15, 6, 16))#candidate|6028|(15, 6, 16)|var|float32
var_6029 = relay.var("var_6029", dtype = "float64", shape = (1188,))#candidate|6029|(1188,)|var|float64
output = func_6027(var_6028,var_6029,)
func_6030 = relay.Function([var_6028,var_6029,], output)
mutated_mod['func_6030'] = func_6030
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6056 = relay.var("var_6056", dtype = "float32", shape = (7, 10, 11))#candidate|6056|(7, 10, 11)|var|float32
uop_6057 = relay.cos(var_6056.astype('float32')) # shape=(7, 10, 11)
output = relay.Tuple([uop_6057,])
output2 = relay.Tuple([uop_6057,])
func_6066 = relay.Function([var_6056,], output)
mod['func_6066'] = func_6066
mod = relay.transform.InferType()(mod)
var_6067 = relay.var("var_6067", dtype = "float32", shape = (7, 10, 11))#candidate|6067|(7, 10, 11)|var|float32
output = func_6066(var_6067)
func_6068 = relay.Function([var_6067], output)
mutated_mod['func_6068'] = func_6068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3766_call = mod.get_global_var('func_3766')
func_3768_call = mutated_mod.get_global_var('func_3768')
call_6106 = func_3766_call()
call_6107 = func_3766_call()
uop_6114 = relay.asinh(call_6106.astype('float64')) # shape=(9, 12, 1)
uop_6116 = relay.asinh(call_6107.astype('float64')) # shape=(9, 12, 1)
bop_6128 = relay.bitwise_xor(uop_6114.astype('int8'), relay.reshape(call_6106.astype('int8'), relay.shape_of(uop_6114))) # shape=(9, 12, 1)
bop_6131 = relay.bitwise_xor(uop_6116.astype('int8'), relay.reshape(call_6107.astype('int8'), relay.shape_of(uop_6116))) # shape=(9, 12, 1)
var_6134 = relay.var("var_6134", dtype = "int8", shape = (9, 12, 1))#candidate|6134|(9, 12, 1)|var|int8
bop_6135 = relay.minimum(bop_6128.astype('int16'), relay.reshape(var_6134.astype('int16'), relay.shape_of(bop_6128))) # shape=(9, 12, 1)
bop_6138 = relay.minimum(bop_6131.astype('int16'), relay.reshape(var_6134.astype('int16'), relay.shape_of(bop_6131))) # shape=(9, 12, 1)
func_5048_call = mod.get_global_var('func_5048')
func_5050_call = mutated_mod.get_global_var('func_5050')
call_6139 = relay.TupleGetItem(func_5048_call(), 0)
call_6140 = relay.TupleGetItem(func_5050_call(), 0)
func_4585_call = mod.get_global_var('func_4585')
func_4587_call = mutated_mod.get_global_var('func_4587')
call_6167 = func_4585_call()
call_6168 = func_4585_call()
func_3913_call = mod.get_global_var('func_3913')
func_3914_call = mutated_mod.get_global_var('func_3914')
call_6190 = relay.TupleGetItem(func_3913_call(), 0)
call_6191 = relay.TupleGetItem(func_3914_call(), 0)
func_4104_call = mod.get_global_var('func_4104')
func_4106_call = mutated_mod.get_global_var('func_4106')
call_6195 = relay.TupleGetItem(func_4104_call(), 0)
call_6196 = relay.TupleGetItem(func_4106_call(), 0)
func_4585_call = mod.get_global_var('func_4585')
func_4587_call = mutated_mod.get_global_var('func_4587')
call_6197 = func_4585_call()
call_6198 = func_4585_call()
func_2804_call = mod.get_global_var('func_2804')
func_2806_call = mutated_mod.get_global_var('func_2806')
call_6207 = relay.TupleGetItem(func_2804_call(), 0)
call_6208 = relay.TupleGetItem(func_2806_call(), 0)
output = relay.Tuple([bop_6135,call_6139,call_6167,call_6190,call_6195,call_6197,call_6207,])
output2 = relay.Tuple([bop_6138,call_6140,call_6168,call_6191,call_6196,call_6198,call_6208,])
func_6213 = relay.Function([var_6134,], output)
mod['func_6213'] = func_6213
mod = relay.transform.InferType()(mod)
mutated_mod['func_6213'] = func_6213
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6214 = relay.var("var_6214", dtype = "int8", shape = (9, 12, 1))#candidate|6214|(9, 12, 1)|var|int8
func_6213_call = mutated_mod.get_global_var('func_6213')
call_6215 = func_6213_call(var_6214)
output = call_6215
func_6216 = relay.Function([var_6214], output)
mutated_mod['func_6216'] = func_6216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5141_call = mod.get_global_var('func_5141')
func_5143_call = mutated_mod.get_global_var('func_5143')
call_6231 = relay.TupleGetItem(func_5141_call(), 0)
call_6232 = relay.TupleGetItem(func_5143_call(), 0)
uop_6233 = relay.log10(call_6231.astype('float32')) # shape=(1, 1, 16)
uop_6235 = relay.log10(call_6232.astype('float32')) # shape=(1, 1, 16)
func_4585_call = mod.get_global_var('func_4585')
func_4587_call = mutated_mod.get_global_var('func_4587')
call_6236 = func_4585_call()
call_6237 = func_4585_call()
output = relay.Tuple([uop_6233,call_6236,])
output2 = relay.Tuple([uop_6235,call_6237,])
func_6246 = relay.Function([], output)
mod['func_6246'] = func_6246
mod = relay.transform.InferType()(mod)
output = func_6246()
func_6247 = relay.Function([], output)
mutated_mod['func_6247'] = func_6247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2804_call = mod.get_global_var('func_2804')
func_2806_call = mutated_mod.get_global_var('func_2806')
call_6255 = relay.TupleGetItem(func_2804_call(), 0)
call_6256 = relay.TupleGetItem(func_2806_call(), 0)
func_4801_call = mod.get_global_var('func_4801')
func_4803_call = mutated_mod.get_global_var('func_4803')
var_6264 = relay.var("var_6264", dtype = "int8", shape = (80,))#candidate|6264|(80,)|var|int8
call_6263 = relay.TupleGetItem(func_4801_call(relay.reshape(var_6264.astype('int8'), [4, 4, 5])), 4)
call_6265 = relay.TupleGetItem(func_4803_call(relay.reshape(var_6264.astype('int8'), [4, 4, 5])), 4)
const_6271 = relay.const([1.906797,-1.354836,6.814028,5.720132,0.245455,4.422861,4.437149,5.871948,6.020016,8.307535,6.005846,-9.673533,1.735358,1.794485,-0.602444,3.765593,-9.925520,-3.342569,-7.244309,2.069223,-3.798047,-4.485584,-5.737342,-5.764312,8.955515,8.973865,4.194420,-3.848755,-3.908559,-1.783095,-6.235064,-6.439539,0.872016,1.497653,-7.999616,5.684431,1.194431,-4.078474,-1.038391,2.082821,-0.438109,-4.505687,-5.035181,-5.690753,3.489970,4.804343,1.935343,-5.575600,-8.662069,-6.450631,-8.923081,-8.677750,-0.569276,-2.613162,8.956818,-3.758908,-1.402275,7.409344,-3.297767,5.669757,-2.437270,6.443066,-7.811424,-8.417310,2.583702,1.998780,0.876574,0.856765,5.612659,-0.056957,4.265787,-6.643773,4.106955,-1.995106,-0.838712,9.720405,-6.919711,-5.507337,4.821974,-9.947358,4.329613,-4.267506,0.501411,-3.227731,1.565713,8.216568,-5.063652,3.830683,4.201733,9.477893,1.255511,6.581587,1.347996,9.794016,-8.807467,-5.999549,8.207879,-3.096874,-0.633976,4.390926,1.175083,0.090072,0.007719,-0.040592,-8.576347,-3.339825,-6.807264,-5.779096,5.138391,-8.076135,1.011246,0.260089,-2.803360,8.686642,3.370925,-3.832513,1.547032,-7.216292,-3.222320,5.018711,-0.931272,9.673072,0.699011,-1.932012,1.432107,2.271487,3.089886,9.223005,-1.765979,4.764071,-5.542989,1.034838,6.184779,-5.830783,-8.840684,-0.259677,2.002770,7.355182,4.300882,2.658093,1.109356,6.946571,2.733724,-2.937218,1.471554,7.631755,0.762378,3.655444,-4.674026,5.347207,-4.197332,5.298187,9.334991,-8.792275,1.947430,3.677230,-1.234937,1.110620,0.601050,-2.334412,5.704085,-7.359702,-3.532993,3.889465,4.127828,5.396191,0.812822,5.346028,8.221146,6.701182,5.007457,7.726844,-1.560971,-4.367154,-1.541090,-9.085051,-0.503116,8.083956,7.709841,-1.442433,5.310994,-0.788814,-6.893483,3.127854,3.081925,-8.936699,3.137372,7.739371,8.591057,7.259006,-9.874409,4.840715,0.227548,3.101745,-2.199846,9.983165,6.254102,-7.406451,-4.421097,9.211091,-7.812433,-9.422217,-3.438637,8.890242,1.291847,8.305698,5.081317,3.848461,2.665878,0.426841,-1.546752,6.659096,-8.302469,6.930145,4.663908,-9.993781,9.827009,5.778580,-1.471294,5.675865,-7.288779,4.783067,2.590136,-2.964224,8.075720,-4.004994,-5.410385,4.858863,9.476281,5.839738,-1.691562,3.533059,8.721462,0.846700,8.810768,3.852745,1.350064,0.028970,7.272126,-4.318114,5.261929,-0.988048,-7.720517,-8.094599,9.077512,5.362429,-8.809837,9.869065,1.412641,2.654081,2.730553,-1.076922,-0.475735,8.239086,9.517274,-5.911620,7.572055,6.865211,7.800314,4.200582,8.520279,-4.428141,5.025644,2.415755,-6.826769,-5.975073,-1.350318,-0.052613,-9.632981,-8.242221,2.050786,5.232457,-6.645745,6.905377,-6.772466,-6.506193,5.210196,1.381786,-1.268096,1.020730,-9.584490,-6.012927,1.386139,2.401772,-9.945596,9.325191,-0.342425,-7.253488,4.544959,-1.983099,0.895416,-5.099057,2.836988,7.503932,-6.159845,-4.802309,-3.243358,0.908935,-3.463526,-4.347518,6.747787,-3.293483,-9.430812,-2.514409,-5.314180,8.274812,8.967169,-8.221012,-6.226269,-1.429034,9.250306,1.125960,6.894131,0.679300,7.035915,-1.348200,6.701238,-1.450889,-2.068531,-6.673483,-4.569741,-4.486409,0.021901,-1.667690,-0.689864,-2.979214,-8.839327,-7.452911,2.751612,6.879422,8.880818,5.038992,-6.895923,-4.003470,-0.849338,-5.900427,-4.949064,-8.133403,5.002778,5.239016,4.986744,2.438151,6.153912,2.331646,2.448241,6.479331,-1.920873,-0.246842,9.096460,9.857505,6.181111,-7.717749,-2.530793,5.974577,3.324619,-4.466676,-9.864031,-0.766862,0.710282,-7.605143,-5.495860,6.180689,-7.201823,-9.304278,-8.167532,9.494106,3.586817,6.949661,-6.298856,9.557197,-8.799068,-5.712721,-1.050394,-5.595950,-9.965493,-5.107464,3.929319,-1.784833,2.716287,8.146944,-2.625860,0.718630,-6.700862,-2.111340,3.168114,-9.663536,5.989900,3.627637,-7.997540,6.918898,-7.723282,9.275724,0.301892,-9.806730,-8.250349,-2.165399,-1.022189,-0.976803,-9.886337,-7.930847,3.603685,3.215548,6.456506,-8.603253,9.279236,3.138638,9.861365,4.096897,-8.990398,-5.682725,7.787645,9.366896,-9.481657,-3.068471,-2.315619,4.045157,2.080537,-1.965521,2.410896,-7.911847,-1.885064,-3.543747,5.895767,-8.914276,3.272352,-8.922099,0.811541,1.496032,-6.408673,9.515685,-3.271225,-0.491054,2.707785,-0.095950,1.419702,8.728577,-1.796980,6.560483,9.970805,8.639975,-1.279312,7.945724,-8.496036,-3.396626,-0.691417,2.263025,-6.171922,5.829676,5.746397,-6.553048,-7.266029,-7.690810,8.346147,-7.009195,-9.434880,-2.747362,-2.618116,-5.462206,-3.634161,3.688361,-1.632961,1.165878,-5.758972,9.620036,-7.246943,-3.049679,8.714649,-7.043418,-6.751922,-3.278249,-1.005711,-7.287260,-0.362905,5.335451,7.346472,-8.371571,-0.004573,-7.290860,-0.327418,-6.890128,2.641660,4.563834,9.777228,2.230432,8.455562,-3.597043,-7.238125,-6.698745,-3.492101,1.909953,-4.693887,8.135334,0.952846,0.620218,1.060566,5.053098,-9.456490,-8.760613,-1.038624,9.743055,1.928253,6.737484,-8.412420,-5.173562,-2.153931,-3.753316,4.722100,0.105280,6.082380,-6.993333,-2.069874,6.007881,3.632630,-0.531808,-0.558263,6.158309,-2.190016,6.470330,-8.401161,3.233744,-2.974690,2.118368,5.222295,-8.324207,7.746630,-9.862952,-6.144281,-6.207329,8.483656,9.310137,-1.296278,0.008357,-7.417397,-2.654846,-7.626863,7.829580,5.820427,4.242041,8.012777,-4.816617,-9.724362,-1.170646,-1.951906,-6.722280,1.520429,6.534591,-1.153386,-8.978211,-9.783173,6.517444,-5.751816,3.311792,8.333457,4.951528,-3.983160,1.861578,-9.981671,-2.965086,-8.054403,-7.020367,-4.252463,-8.691843,-7.580476,2.622173,1.889794,9.076009,5.627663,3.437350,5.640882,0.148338,-3.296777,2.116542,-1.904286,-8.411007,-2.097728,6.333120,-9.037784,-3.797984,-5.110424,2.930940,-1.054047,-4.343277,4.614313,8.561764,-9.773188,9.384392,8.350665,0.865214,-8.688796,6.866524,-6.426946,4.714107,-2.515743,9.468884,-6.053099,-8.860158,7.701372,-2.460369,-5.196996,-2.800962,3.942984,-2.569899,-6.583189,-6.475837,1.173665,8.514367,-2.827394,-4.892862,-2.377182,-7.315827,2.754234,-3.512806,9.840567,9.114644,-2.819239,-9.384709,4.396487,-4.990269,-6.649965,-5.771197,-6.585205,0.483530,6.229035,7.448916,8.149348,-6.769248,-0.784170,7.697325,5.063349,-1.273804,-2.454731,1.466793,0.520552,0.002847,7.780458,1.435114,-8.465836,-1.135031,-4.652693,3.410832,0.234679,-4.686014,-2.049806,8.022226,6.490832,9.766257,-1.619394,7.946926,0.658794,7.446487,5.299747,-5.249932,5.710764,3.890413,0.154382,5.109755,-3.119097,-4.928682,-7.865257,-0.959812,2.783261,9.355287,4.135625,9.004914,-1.042163,1.817920,4.516265,7.752215,-9.495559,8.691548,5.267534,6.648974,-5.525738,4.841961,2.316892,-1.974981,4.749953,2.003378,2.942762,3.387725,2.947975,1.176020,7.757516,-2.753962,9.964141,6.134421,-0.092367,-6.346693,-4.872045,0.210530,1.563943,2.542703,-9.985879,7.332259,0.528081,6.409560,6.172736,-4.223817,1.129602,8.392068,-7.213309,0.386357,2.772002,0.687223,2.210177,1.079545,3.502929,-4.361382,5.346668,1.921481,-0.682528,-7.688554,9.552597,-4.602135,7.856390,1.263987,-0.024778,-9.213628,-1.221755,-3.735228,4.212731,-5.384356,-4.189592,-5.588588,2.865309,-3.325636,-7.806407,5.779405,2.105516,-2.741723,3.493338,-5.105415,-7.163974,7.143809,4.409423,0.750194,-1.774290,1.784059,-0.526848,-5.354184,4.079320,0.659143,9.586292,7.515763,9.847342,3.117023,3.030933,-5.572285,3.173501,-3.889368,9.141796,6.544582,0.780020,-6.161789,-0.940539,5.377847,-0.598306,4.549236,-8.729873,-2.889729,-2.478130,-6.539018,-2.203509,5.033655,8.485860,-0.604215,1.948109,-0.393599,-2.428889,-0.291344,6.496210,-7.427537,0.359719,-2.328376,-4.639982,0.540016,-7.026064,-1.509820,-7.901051,-9.376064,3.339940,8.169868,-0.568274,4.396487,-9.696167,8.738160,-4.481441,7.472171,7.779490,7.184147,3.209354,-0.408963,-0.471993,-4.927281,9.411204,-3.923462,3.028345,9.204119,2.797132,-7.728391,4.761004,-9.858810,0.386243,3.622677,7.149534,-8.900285,0.058341,-1.946951,8.962205,-9.601792,-9.978836,1.033343,-4.413467,2.787528,5.166564,-4.220709,-6.735532,-9.456884,-5.996912,-3.461997,-2.815263,-9.896097,-8.216773,-6.265989,5.832520,-2.062006,0.016430,2.763874,-8.515903,-1.316133,-7.653225,-9.015651,4.947219,-2.899287,-2.918421,2.468076,6.964332,-6.180617,-4.530847,1.089223,-3.805116,4.031798,8.410066,9.314134,-7.470405,-8.330223,-9.220579,1.313743,9.784240,-8.339810,-6.333287,2.461325,3.555158,2.157262,-4.167414,-7.093567,-6.302726,-9.956149,-2.269622,-0.457339,4.363395,-6.612191,3.037839,2.199333,0.695364,6.830247,4.064232,-6.370157,-9.802751,5.659489,-2.795688,7.301926,8.184304,3.667963,-5.070022,-2.933510,-3.603498,0.040907,-6.975914,-6.128903,-5.919107,-5.374436,-2.971288,7.735111,-5.326031,4.674426,-7.962780,-7.000687,8.942516,0.566807,0.520990,0.962027,-4.713849,4.098430,-5.404718,7.167272,7.211933,-1.019792,-3.534959,0.326468,-3.640601,8.842089,3.210809,9.157552,4.249395,-4.592608,-6.273055,-2.722454,6.689852,-1.716233,-7.709495,-5.347390,7.863773,9.889764,-8.362873,-9.158966,-3.654495,0.380325,2.809145,-6.156959,-1.593611,1.442467,-7.412346,7.240742,-9.180250,1.166559,4.696552,-8.182814,8.562058,-1.707838,-6.173952,-9.739139,1.675705,2.418774,-3.683320,2.156784,-2.186885,-5.766334,3.866713,-9.934331,4.255158,-7.148685,-2.823796,1.290483,-5.956143,1.887172,-6.680274,0.376404,-5.857659,6.460577,-8.645549,6.717372,6.079811,-8.856284,4.353575,-5.742887,-4.731456,-3.396178,-7.053623,-8.887482,5.019149,3.926131,-1.251682,3.079145,7.499516,0.744444,-8.589163,1.034819,-6.582092,-1.019879,-3.587205,-3.227093,8.299231,7.279812,-3.757849,-6.614078,-8.080891,-1.018229,9.034030,5.002276,-8.866608,-4.533728,2.058409,-8.796499,7.329035,2.958934,-5.207444,7.399973,-3.018405,8.379018,-4.248016,0.267151,1.891625,3.174403,8.654357,-0.456287,-0.418158,-3.263721,-6.410258,5.528805,8.834887,6.929317,8.684958,9.784302,-3.182437,-4.128056,0.998389,3.299361,1.581972,4.229117,1.547341,-4.360426,-5.556723,9.475646,-5.111703,1.160630,5.352588,1.344509,4.049355,0.763535,8.159883,-6.021039,2.152269,5.547501,1.836968,2.098250,-0.877977,-2.204215,6.360832,1.145688,-3.285120,3.759320,-4.697856,-6.440276,-2.237514,7.918896,-2.980356,-7.086613,0.666206,-2.544424,-4.178691,2.015948,-9.348881,2.229796,8.335168,2.873298,3.878991,1.817164,4.303211,6.629753,8.270290,9.493492,8.196403,0.348317,3.661501,7.809879,-7.947496,9.119251,-2.892700,-7.617423,5.910493,1.993769,-5.251413,-2.135429,3.445890,7.163512,-5.826261,-4.705923,-7.330993,-0.264753,4.968916,3.495032,-5.521249,-0.894052,-3.212690,-7.952052,-0.889101,-0.652704,5.655029,-6.806714], dtype = "float32")#candidate|6271|(1080,)|const|float32
bop_6272 = relay.less(call_6263.astype('bool'), relay.reshape(const_6271.astype('bool'), relay.shape_of(call_6263))) # shape=(1080,)
bop_6275 = relay.less(call_6265.astype('bool'), relay.reshape(const_6271.astype('bool'), relay.shape_of(call_6265))) # shape=(1080,)
output = relay.Tuple([call_6255,var_6264,bop_6272,])
output2 = relay.Tuple([call_6256,var_6264,bop_6275,])
func_6294 = relay.Function([var_6264,], output)
mod['func_6294'] = func_6294
mod = relay.transform.InferType()(mod)
var_6295 = relay.var("var_6295", dtype = "int8", shape = (80,))#candidate|6295|(80,)|var|int8
output = func_6294(var_6295)
func_6296 = relay.Function([var_6295], output)
mutated_mod['func_6296'] = func_6296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1692_call = mod.get_global_var('func_1692')
func_1693_call = mutated_mod.get_global_var('func_1693')
call_6319 = relay.TupleGetItem(func_1692_call(), 0)
call_6320 = relay.TupleGetItem(func_1693_call(), 0)
output = call_6319
output2 = call_6320
func_6321 = relay.Function([], output)
mod['func_6321'] = func_6321
mod = relay.transform.InferType()(mod)
mutated_mod['func_6321'] = func_6321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6321_call = mutated_mod.get_global_var('func_6321')
call_6322 = func_6321_call()
output = call_6322
func_6323 = relay.Function([], output)
mutated_mod['func_6323'] = func_6323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mod.get_global_var('func_5267')
func_5268_call = mutated_mod.get_global_var('func_5268')
call_6326 = relay.TupleGetItem(func_5267_call(), 0)
call_6327 = relay.TupleGetItem(func_5268_call(), 0)
func_2374_call = mod.get_global_var('func_2374')
func_2377_call = mutated_mod.get_global_var('func_2377')
var_6331 = relay.var("var_6331", dtype = "int32", shape = ())#candidate|6331|()|var|int32
call_6330 = func_2374_call(relay.reshape(var_6331.astype('int32'), []))
call_6332 = func_2374_call(relay.reshape(var_6331.astype('int32'), []))
output = relay.Tuple([call_6326,call_6330,var_6331,])
output2 = relay.Tuple([call_6327,call_6332,var_6331,])
func_6341 = relay.Function([var_6331,], output)
mod['func_6341'] = func_6341
mod = relay.transform.InferType()(mod)
mutated_mod['func_6341'] = func_6341
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6342 = relay.var("var_6342", dtype = "int32", shape = ())#candidate|6342|()|var|int32
func_6341_call = mutated_mod.get_global_var('func_6341')
call_6343 = func_6341_call(var_6342)
output = call_6343
func_6344 = relay.Function([var_6342], output)
mutated_mod['func_6344'] = func_6344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_6373 = relay.TupleGetItem(func_2172_call(), 0)
call_6374 = relay.TupleGetItem(func_2173_call(), 0)
output = call_6373
output2 = call_6374
func_6385 = relay.Function([], output)
mod['func_6385'] = func_6385
mod = relay.transform.InferType()(mod)
mutated_mod['func_6385'] = func_6385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6385_call = mutated_mod.get_global_var('func_6385')
call_6386 = func_6385_call()
output = call_6386
func_6387 = relay.Function([], output)
mutated_mod['func_6387'] = func_6387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6385_call = mod.get_global_var('func_6385')
func_6387_call = mutated_mod.get_global_var('func_6387')
call_6400 = func_6385_call()
call_6401 = func_6385_call()
var_6426 = relay.var("var_6426", dtype = "float64", shape = (9, 12, 6))#candidate|6426|(9, 12, 6)|var|float64
bop_6427 = relay.greater(call_6400.astype('bool'), var_6426.astype('bool')) # shape=(9, 12, 6)
bop_6430 = relay.greater(call_6401.astype('bool'), var_6426.astype('bool')) # shape=(9, 12, 6)
func_5576_call = mod.get_global_var('func_5576')
func_5577_call = mutated_mod.get_global_var('func_5577')
call_6432 = relay.TupleGetItem(func_5576_call(), 0)
call_6433 = relay.TupleGetItem(func_5577_call(), 0)
output = relay.Tuple([bop_6427,call_6432,])
output2 = relay.Tuple([bop_6430,call_6433,])
func_6440 = relay.Function([var_6426,], output)
mod['func_6440'] = func_6440
mod = relay.transform.InferType()(mod)
mutated_mod['func_6440'] = func_6440
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6441 = relay.var("var_6441", dtype = "float64", shape = (9, 12, 6))#candidate|6441|(9, 12, 6)|var|float64
func_6440_call = mutated_mod.get_global_var('func_6440')
call_6442 = func_6440_call(var_6441)
output = call_6442
func_6443 = relay.Function([var_6441], output)
mutated_mod['func_6443'] = func_6443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4682_call = mod.get_global_var('func_4682')
func_4683_call = mutated_mod.get_global_var('func_4683')
call_6505 = func_4682_call()
call_6506 = func_4682_call()
output = call_6505
output2 = call_6506
func_6516 = relay.Function([], output)
mod['func_6516'] = func_6516
mod = relay.transform.InferType()(mod)
mutated_mod['func_6516'] = func_6516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6516_call = mutated_mod.get_global_var('func_6516')
call_6517 = func_6516_call()
output = call_6517
func_6518 = relay.Function([], output)
mutated_mod['func_6518'] = func_6518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mod.get_global_var('func_5267')
func_5268_call = mutated_mod.get_global_var('func_5268')
call_6544 = relay.TupleGetItem(func_5267_call(), 1)
call_6545 = relay.TupleGetItem(func_5268_call(), 1)
const_6547 = relay.const([-9.898244,4.485138,3.984045,-6.674930,-2.473537,-3.599324,4.847467,-7.881505,8.427518,-9.553770,-3.365404,-1.407522,2.573044,-7.250044,-3.940116,-2.063131,2.178699,3.847384,6.935180,-3.225450,-1.734347,0.433305,-9.978261,-5.796525,7.398704,0.793985,-0.222292,6.113605,-1.263638,7.154293,-8.915518,4.856448,1.202584,-5.463329,5.560209,9.154961,0.947435,0.939539,-1.358148,5.984320,-3.547895,7.917744,4.751773,-0.975615,-6.300030,-1.811498,8.379269,-0.926009,2.041709,3.603658,6.607620,-6.064185,3.711014,-7.002084,0.492219,-2.614117,-0.608684,-5.698619,-7.135375,-7.443263,2.749174,3.974650,-9.952239,1.822562,-4.367005,-5.068278,3.998698,1.281088,-5.850798,-8.828812,8.898008,6.708847,-5.839201,5.390153,0.469497,5.675706,7.899297,2.697942,-7.488522,2.787844,-9.562068,-0.136450,-8.994216,-8.936107,-9.421223,-9.389270,1.945348,2.786828,4.221986,2.225027,-7.875855,6.718735,1.615618,-4.822246,-7.972579,9.417211,2.575632,-4.611915,5.193644,1.216551,-1.333512,7.484168,7.130444,0.476099,-5.424571,1.633546,-4.932538,-1.819330,-6.623562,1.080459,-2.990324,8.559526,3.821214,7.783837,-3.920694,-1.700402,-7.940850,4.817976,-2.733497,-8.882674,0.789124,-4.632477,6.404598,9.206140,1.540616,-8.509456,5.314633,3.958822,6.864853,5.997490,0.394225,-0.812087,-8.329576,-9.004863,3.426960,8.159770,-5.728329,-8.686884,-5.246325,5.315594,-6.691595,4.391223,5.267854,-1.164469,9.515437,8.354173,4.925358,-8.374254,7.170609,9.239785,2.748934,8.927717,-5.845654,3.534656,1.111711,-1.572709,-1.052764,-0.209653,-4.384016,5.486859,-7.208771,1.536627,-0.447525,7.582226,-5.992056,-0.063555,4.144161,9.166995,1.400135,-9.876546,-3.225370,2.609627,-8.557105,-6.391536,-1.439141,-2.923468,-9.406994,7.739902,5.729703,-1.596389,4.949872,-8.884289,-6.165301,-2.944137,-7.706038,3.056581,8.312472,-6.779949,-6.219003,-2.684275,-4.634448,6.217010,-5.976966,5.678647,-0.646129,6.488172,9.491179,-3.814040,-2.622981,8.865535,-8.976284,4.658641,0.069910,3.834082,-1.469387,8.932253,2.021102,-8.749080,8.191500,5.436741,8.021436,4.068428,-4.331760,1.826903,-7.421184,-7.221644,3.810360,-0.166428,1.760433,-8.949806,3.836338,-5.799290,-8.972623,3.765782,-2.183570,7.104847,3.783258,-0.418653,9.389854,-6.135746,2.138801,-4.999761,-3.429780,9.755572,-8.931814,-6.413529,1.882937,-6.989368,1.362966,9.576158,2.316252,8.266666,7.180560,-8.984973,3.776165,-3.509195,2.116028,0.623511,6.404580,2.048134,-8.758443,-0.643391,-5.785673,-0.142568,-7.249361,-9.942034,-8.147970,-6.539417,5.593334,-5.718301,-8.316871,5.534942,3.409962,2.408598,-3.990081,5.348742,-9.430804,-4.554736,-0.114320,-0.283725,1.090725,-9.339185,6.203600,9.218588,-5.310984,9.443017,3.665158,-2.353920,-6.467546,6.730228,2.596863,3.085386,-8.597159,-4.702188,-6.508086,1.209880,3.891979,-4.810402,1.541912,-8.981104,6.371475,-9.402588,-0.572512,-6.562516,-3.919331,7.212588,-9.301131,-8.305616,4.512359,4.154690,1.449773,2.051454,0.653065,6.988523,4.823865,-9.402030,-0.872222,7.176735,4.399652,7.306697,-8.187296,8.822104,6.221844,7.213435,7.829957,7.286171,-4.760151,7.348352,-1.102186,-7.893242,-2.268953,-6.052563,5.138175,-2.126775,5.816525,-4.066083,-0.506638,-3.341179,5.045495,-9.848960,9.263750,-4.477268,-0.352960,5.211128,-3.358060,3.792523,-0.990716,9.441831,6.464448,-0.066063,0.279977,-6.521980,6.384399,-9.907497,5.705234,6.054519,-9.169918,-2.022984,0.516892,9.487503,1.920949,0.294716,-4.661763,4.276194,-6.085584,1.950448,-8.399871,4.960185,-0.778263,3.831831,3.531698,-0.560127,-4.898740,-9.427009,-3.873014,5.048307,-9.022657,3.301065,-9.499214,0.702361,6.461444,-4.643110,-6.866956,7.223344,3.919755,-5.094843,6.299842,-7.524147,6.493077,6.483717,-4.351833,9.054421,6.714721,-7.574156,7.122751,-6.834229,-6.255718,7.059793,8.072773,6.675497,6.963502,3.419694,6.145510,-9.053531,-0.985604,-1.769531,-8.771181,-5.513435,6.428113,9.318500,-2.606619,8.912227,2.265065,4.165782,5.197117,4.423760,2.973417,0.293618,3.756654,5.082078,7.428724,-3.730159,-1.470043,-9.214948,7.946296,-5.933295,3.078753,-8.043154,-5.862162,6.727002,9.610592,-5.701347,0.175145,2.052134,7.529611,2.172418,-8.132431,6.984693,-5.942726,-1.346541,9.256571,2.847598,-4.723183,4.252055,1.794338,-1.026976,-3.519980,6.517411,-8.215932,-0.019299,-8.838518,2.599108,7.352767,8.908125,-2.508198,-4.376040,-2.475245,-9.974889,8.285293,-3.308975,0.013334,9.558177,9.632704,0.503584,0.850300,-1.029320,4.005516,8.563839,-0.801899,-5.617068,-7.901092,-5.371250,-8.195186,-1.058417,0.420419,0.805848,7.046905,-7.894486,9.901163,4.762108,4.936991,-6.387998,5.441865,7.020952,-5.851600,-5.440898,-8.493057,-6.303855,9.248788,1.424850,2.090793,0.077238,4.250804,1.816989,-6.348408,-3.231953,-1.302201,-8.591961,-1.929817,0.080457,-2.145219,8.565347,7.548661,2.761306,-2.354831,9.289113,9.449491,9.786136,-7.325885,-5.148133,6.524044,-9.175630,3.126967,9.487417,-9.975525,9.202768,-6.170318,-3.169913,-3.277027,-9.766572,-2.117732,-8.773632,4.154452,-4.791074,-2.892950,-4.935698,5.178881,-2.072663,7.633184,-0.261193,-6.027507,-5.326870,1.178371,-4.456715,2.174288,-1.764146,-0.314439,0.361847,-7.639473,8.787569,-1.351535,-4.197894,-7.991438,9.460006,-5.389831,-9.828812,0.579428,3.946568,5.878317,-6.878933,5.897269,-6.450574,0.466438,1.587466,9.903942,-1.736582,-7.178800,-3.223616,4.208830,-5.171910,3.675049,3.188440,-3.522344,5.589119,-2.221824,-2.330934,7.023484,-8.849634,-3.018388,-6.959837,-1.132711,-2.163964,-0.829125,-5.797200,-9.124860,6.076864,1.169778,-9.319535,-3.642937,0.932585,7.880975,-5.462841,-2.078017,2.351996,-1.288022,-0.729975,-7.905183,2.019052,9.230627,8.109647,-9.024187,-6.500254,2.259500,4.422025,-3.322736,-2.247804,-7.978105,-6.788371,3.114498,-6.388383,-4.228270,4.538114,1.800410,6.639042,-3.823511,-8.195245,3.507243,-9.414532,6.975233,-8.023339,-4.939183,5.897754,4.851391,1.702582,1.663647,-9.784361,-3.134871,-4.728703,-4.704572,9.485307,-5.961913,-9.085152,-3.153279,-7.898495,-4.678682,9.883803,-8.124941,-5.499151,1.904801,-0.200417,5.548860,-7.104843,-2.771434,0.182222,-8.813066,7.760459,-4.405730,-4.310358,-4.800639,-6.515324,-1.772823,9.766434,-0.329366,-0.269235,6.531600,-4.285825,-9.241168,0.386237,5.747936,0.331897,6.507494,3.265401,-3.395725,-5.693807,-9.337953,-3.857241,-4.693971,0.756191,9.988843,-9.444625,4.029439,2.809004,0.192548,-7.287616,1.107022,-4.892287,4.528686,-2.318522,-7.125113,-7.374249,2.990896,9.637178,5.257302,-2.099731,-9.443691,6.590417,0.763483,6.036184,8.981617,0.337803,-3.343760,2.456711,6.991690,2.688053,-0.918996,7.281435,-2.086675,-5.499909,4.364617,-1.398242,7.146879,9.909134,-2.465874,-6.101561,0.058661,-1.696543,2.135864,0.759288,6.348550,-9.295498,-0.614586,5.411684,-7.421123,-7.881347,-3.248231,-9.295029,2.918420,-9.536576,-1.552193,2.329939,3.510120,0.175828,-0.994954,0.304757,-6.943454,1.337719,3.881346,5.999517,-7.054888,-7.189017,4.367185,7.029872,-0.886320,-7.226016,-2.534636,-5.157787,-7.561153,-3.771662,-8.667924,-4.782678,-3.322359,-7.182543,7.100815,2.982804,9.468148,-7.747837,-1.252851,7.475614,-1.545647,-2.411221,-9.952701,-7.460070,-3.317808,5.546220,-2.543961,5.613426,6.409554,7.184641,-1.264248,2.135399,-8.662155,-1.955071,1.895243,0.450701,7.694023,-0.121807,9.152960,-5.306674,5.750291,-8.878327,-0.926905,-5.506501,2.392029,-2.113887,7.851979,-7.925303,2.814367,-6.407756,-8.769265,-8.872253,4.689964,0.475618,0.244577,4.511442,2.345141,8.321456,0.750173,-4.302451,3.881339,-9.422716,-5.790807,-5.658836,2.086146,-9.063991,-2.956334,-5.700839,4.572005,-6.982413,9.294776,5.177441,-0.252811,-5.229350,2.543341,-7.214159,1.588882,3.733522,8.535900,-1.447543,-1.289944,0.262073,1.507718,1.696695,1.361694,-8.116327,4.847316,-5.840064,-2.891654,7.034494,2.796026,-1.618856,5.293377,-8.971482,6.106368,7.930174,5.066168,-6.004351,-1.607130,0.500016,-0.311377,5.690101,0.174813,3.029568,-1.508649,5.757291,-1.811889,7.104401,2.322599,6.177976,-0.843764,9.039366,3.136165,-2.322085,1.073008,9.529170,2.920500,4.313020,-6.397446,-3.597473,3.650319,-0.303063,3.504697,8.883017,8.944654,0.914252,-2.336145,5.515042,0.851302,0.999928,9.775503,-1.593266,5.105639,-6.465093,-4.887124,6.630210,-6.746605,5.957853,5.982782,7.586422,5.092058,-6.392430,8.114609,3.517426,8.295496,1.749782,-4.384382,-4.797942,6.093037,9.823916,6.753474,6.234440,5.415703,-4.162630,-5.524684,0.314683,-9.346424,4.486850,-5.319283,-2.931662,2.559610,-3.108715,7.331157,-6.484894,8.948770,-8.836119,-0.053189,9.771916,1.017755,-2.469312,7.988132,9.171170,6.571552,9.143461,-0.325149,0.090009,9.508896,9.287719,-3.649128,6.537881,5.921453,7.992734,5.852670,0.713396,-9.131054,-4.659353,-2.281593,0.262460,-1.723978,0.366333,1.105834,2.097269,-6.438794,7.664881,-1.600055,8.575948,4.342372,1.173999,4.554288,0.781160,-8.881537,2.126571,3.432475,-3.039385,5.541998,-3.186864,-4.593812,1.173631,-5.338771,-2.713754,6.452205,6.417768,-7.782888,9.717598,6.463014,1.563438,3.224355,-8.928507,4.436315,-3.477560,-5.374858,8.786251,-3.869144,-6.380881,-0.648974,4.945835,-4.612055,-3.030244,8.296523,-8.026672,-4.037953,-1.984228,-2.430363,-3.283863,4.483523,-6.760857,-3.642498,3.849294,-1.670160,4.902587,-1.749719,-8.282499,0.782700,4.236037,-3.378914,-8.508613,9.007840,-5.492067,6.559683,3.303970,-9.940777,7.046659,-0.067974,1.344215,-6.149587,8.705069,-6.922906,4.509728,-4.302515,-6.757888,-2.447050,2.348650,-1.544458,6.035026,-3.387644,-6.701658,-1.789117,2.576953,-4.416683,1.856956,-2.196566,7.572404,-3.083438,-6.825520,7.096476,0.558664,5.769542,0.694977,2.766739,-7.125108,-1.174813,-0.638790,-4.028270,0.527415,-3.943354,8.310425,8.878425,9.890771,0.282713,-9.325558,3.037838,-9.316701,-3.406847,-6.525852,-0.101807,2.432197,6.254016,7.217963,-1.547454,9.576989,0.841264,0.460741,0.737794,-3.214671,-9.831600,-5.417180,-2.201365,3.249056,-1.967018,-4.267700,-0.848232,4.646855,0.911980,5.192145,7.478763,4.634435,7.713846,0.911375,0.859232,9.716256,-2.530743,5.061325,-5.816743,6.615071,-4.672519,7.031877,-0.859822,4.861780,3.041382,7.047748,3.270430,6.543551,3.889310,8.205089,-8.093495,-4.844102,-8.916278,5.148997,-7.140229,-5.127001,1.978513,7.612502,-2.104644,6.630140,1.281072,8.007617,1.547358,4.897570,4.092148,-4.319866,9.305424,1.600690,-8.397085,-9.827147,7.592371,-6.430458,-2.940690,-9.941562,-7.912316,-3.565852,-8.783165,-9.163638,-7.933220,-0.183623,-5.503598,8.896002,-5.325539,-1.816256,-6.781636,3.260017,3.547322,-0.799674,-3.001120,-7.077265,-5.003406,-2.126036,-9.036164,1.224192,1.507855,1.908428,-1.004989,4.142379,3.248913,4.659411,2.806742,3.780499,-1.909164,-1.074955,4.050231,7.130100,-6.132892,-8.234696,-9.335876,7.431907,-4.092934,-0.707833,-1.713719,7.839709,8.937140,2.702152,8.544909,3.675014,-1.156360,-5.880387,-1.410958,8.816125,-9.665641,-7.611397,1.064458,-3.310587,-9.928800,-6.584799,-8.541837,-2.284503,5.564507,-4.947466,-6.943321,-3.736904,-5.606552,-9.224730,7.162836,1.509858,-9.518030,-7.858314,5.224739,2.227687,0.643715,-3.090131,7.093354,4.513905,-7.773281,1.258689,3.763032,2.865924,3.487850,0.315916,-1.555273,-9.374619,-2.062465,-6.223394,7.961601,3.481178,-2.477180,-4.109833,-5.870487,-5.510478,-0.228754,9.495261,2.770463,3.263328,7.331137,1.532228,6.695108,-0.323893,9.816267,5.325895,-2.262035,3.002795,4.651019,-1.003058,-3.274833,-0.776035,-7.962305,-3.154520,0.137014,-7.527658,-2.342132,-4.060485,9.724544,3.068630,2.935041,1.325122,5.428560,-3.466234,7.461196,-0.245778,9.021937,-7.349459,8.384243,-7.009236,-2.940669,9.000454,-0.314407,-1.695734,-1.316860,-4.958901,-9.426475,9.263479,2.624952,-9.283855,-6.410626,-2.759911,-1.713008,1.549827,5.219680,-9.361438,6.377630,9.271762,3.406718,7.453409,5.345273,4.774236,-2.200302,-8.005085,9.811779,-5.968930,1.267252,6.456473,0.485410,6.458873,-5.625959,-7.913643,8.681045,-6.401896,5.805688,-8.300756,6.920276,-6.102187,-1.099372,2.946448,-7.161859,2.681417,-4.659757,7.597746,-5.611956,9.267930,-6.401949,-9.962376,7.368766,-6.014140,-6.752622,8.955580,-7.890926,0.013697,-0.863468,-2.468978,-9.110078,0.800626,3.451844,-3.398953,6.407608,-3.271267,9.874456,-2.285163,7.011600,6.302165,8.193229,-2.685039,6.932808,8.663602,-4.747638,-6.039594,9.341627,-7.582082,-2.553205,-8.508341,-7.658789,0.166794,4.658234,-2.775904,-1.845445,9.806064,-4.762555,1.354626,5.859032,-3.138188,4.450515,2.895868,-5.716789,1.831853,-4.519837,-9.885648,-7.112986,7.832327,3.351059,5.919693,4.907412,-3.696168,-5.417040,5.683664,-8.236462,1.810565,-7.775350,-8.476247,-8.017784,3.032385,-8.877095,9.397194,7.987767,-8.558635,-4.414719,-4.665025,-3.591282,-2.049057,8.978768,2.550211,0.870089,9.618410,5.251418,-8.842101,8.192129,-5.108315,1.252579,-5.251322,-1.092254,-3.132386,-1.174254,6.178600,6.393782,1.824420,1.763566,-9.251568,-7.056967,5.814964,2.182854,9.917197,3.793696,-3.894699,-2.003344,-9.884401,-9.241871,7.964343,9.921636,3.483474,-0.410867,3.820998,3.803457,-1.469059,4.469017,8.615686,5.952113,9.386014,3.013897,-0.216858,6.268253,-0.834906,9.323211,-2.979182,-9.636285,2.167897,1.073459,2.986661,-4.469172,-4.967150,7.945298,-6.024382,-6.296556,6.679761,-9.809490,4.754617,-8.966841,3.646961,-3.797195,4.272377,9.973013,8.220838,7.133790,-3.861641,4.483436,-3.933817,-2.228007,2.205712,-5.400905,-1.279081,-8.060150,-8.581846,-5.027298,-0.573995,-9.436790,9.364852,-3.740006,-0.520189,9.142888,4.105459,2.422271,5.087392,0.218463,-4.510425,-5.591621,-8.853850,4.603273,9.130624,-5.013833,-8.750679,4.437632,-5.526188,-4.619737,-9.952456,5.643491,-6.140026,0.471000,4.731553,5.825687,-0.483417,-8.556604,-7.485051,-3.795320,6.679573,-2.922299,0.934539,-8.308000,2.139262,-1.828790,-6.269094,-4.247431,-1.300025,5.948119,-4.977657,8.515217,-0.798528,0.627856,0.990402,-0.277985,-2.391882,-8.086470,3.885100,0.143876,-2.167193,-1.987260,-4.948404,2.041069,-2.979618,-7.712552,2.118057,0.518616,6.361337,8.947260,-0.188130,-9.569155,-9.735857,-6.245234,8.926889,-7.968794,8.206929,-3.267665,0.300581,-4.061362,-8.111651,-4.367572,3.960362,7.288210,-0.941749,4.736788,1.920608,9.416258,4.647950,4.101801,-6.503289,-9.048864,-3.766748,5.239851,-1.381980,4.215972,-7.136762,7.260286,8.214565,-5.628199,9.459470,5.390039,7.580477,-3.360801,-0.890434,4.299711,0.638038,3.616699,7.341143,-2.354703,-9.594218,-3.948474,6.958188,-4.427855,4.040688,1.512717,3.870049,0.455898,1.640557,9.403711,8.962983,-3.921392,-4.493558,-0.775865,-4.514060,1.934520,-1.596729,3.518819,1.295488,-7.728398,0.043159,1.833895,-2.705023,4.392846,-2.891450,-4.090019,-3.494533,7.732661,-8.948638,-7.671326,-2.771309,3.207093,4.645147,-0.038304,6.834570,4.677885,-5.943672,7.164868,8.069196,3.350797,3.490525,8.454386,-4.945806,-1.933410,-3.096405,-9.368720,-8.455205,5.345601,-3.207478,8.833470,6.797888,-7.865923,1.325100,-0.120463,1.714815,8.199738,1.107945,-1.304846,7.091615,-2.484270,5.217082,-6.800154,7.942033,2.869003,2.696660,6.948472,-8.359172,9.659069,0.715407,-1.735621,6.370250,6.154711,2.095820,-1.058640,-8.284810,-2.415117,8.224835,9.783957,1.352914,6.068301,9.311128,9.686301,-9.816790,-7.828886,-8.367708,-8.680787,-0.368621,2.458111,6.348319,-9.814586,-8.369685,5.910485,0.682746,-6.020080,-4.768191,2.320374,-2.690505,1.267902,2.501820,-7.805927,-0.636170,3.789493,-3.363660,-8.744990,8.373567,2.459308,-4.767914,2.957981,-8.984371,-1.186211,2.610155,-6.292069,-5.521050,1.493224,5.808394,5.027518,-1.392479,-4.978118,4.130319,2.154028,8.324150,2.619565,4.213966,4.968007,-2.476222,-5.545769,-2.341884,-7.802066,-2.302961,-6.190747,6.809515,-7.998677,0.396664,0.785763,1.250877,6.430456,9.892834,-2.079292,4.016700,-2.818118,7.485723,-0.850897,-5.745079,-3.238046,-6.174394,-5.015573,7.804055,3.566139,-5.558102,1.532444,8.033381,-2.608688,6.309017,-2.957262,5.811224,1.858196,7.699573,-1.604714,-0.529632,6.624826,3.805581,-3.872684,-4.977180,5.393526,-9.374579,-5.413100,4.698092,2.358671,-8.152411,-4.164602,-1.032298,-6.944119,3.288288,2.795138,-5.027036,-8.946537,4.821569,-7.321494,-6.387268,-1.895674,-1.839979,8.963829,5.616499,8.900930,-5.825658,0.355211,5.370668,-8.333598,-9.178230,-7.117879,-7.702596,6.318722,1.750837,7.807941,1.389221,8.206589,1.714970,-8.714329,1.514378,-9.475760,6.199363,-3.905310,0.195585,9.100774,3.120053,-6.434765,-4.861848,2.289120,4.964380,4.154214,-2.405122,0.712492,4.985819,-0.846642,8.554387,-0.311606,4.411725,3.756191,-1.460662,-1.573949,-1.483793,1.483724,-8.552921,-7.956220,-1.186294,3.670668,-4.899024,-7.485879,-4.461835,-8.597295,1.669090,-5.015002,-6.665102,7.554199,-7.875460,-9.578593,7.262838,5.509439,-5.558866,0.846067,1.079890,7.949994,5.650982,-6.657311,-5.126258,2.380843,3.438824,-7.995601,2.246492,-8.080811,-0.768285,-4.630077,5.111289,4.387395,-3.107926,-7.484394,6.763360,1.288979,2.119949,-5.333455,1.940292,6.331430,6.666312,-3.087708,6.991793,-8.626258,1.959175,7.856252,-6.536291,-5.077550,-9.706051,6.500324,-7.916132,-8.058208,-4.405668,9.529514,7.482345,-1.510016,1.666378,1.502780,-0.550268,-1.091881,3.584874,-6.944425,-3.958177,-8.024554,8.001036,3.135021,-8.264807,8.634795,-2.955809,-7.675250,8.156532,6.885055,0.179532,9.597316,-0.533283,9.898316,-8.680082,-0.430019,-0.846191,2.337899,-1.661047,3.666527,-2.145551,7.578192,-8.057197,-1.229503,-4.470951,-7.693146,1.693950,3.904620,9.648081,0.475351,-6.589349,-2.091453,-9.072648,-2.116327,-2.710664,2.175917,-0.514458,-3.805668,5.839918,-3.457776,-4.779109,3.720590,1.698324,8.268107,-5.919212,-8.329499,-1.705089,1.123687,-6.273769,2.060565,-9.312120,4.404967,5.414985,1.599548,5.824008,6.312278,-6.501913,7.813638,2.421285,-3.344783,0.157791,3.635323,7.006671,-1.674622,-6.771758,9.090164,-1.564964,-9.646884,-4.841712,-5.717788,6.216324,3.415465,0.040397,5.340134,3.625956,-9.815287,-4.249997,7.780474,-9.069614,4.587969,5.556226,1.860416,-0.672606,-9.845699,8.311528,-3.558413,-2.229682,-7.263168,-6.300747,-1.309540,3.179760,-6.204800,-1.072991,-0.377004,2.038248,-6.270613,-3.525459,-9.779844,0.280146,0.173607,-5.317655,1.284936,1.526643,-0.079135,-5.772840,7.810500,4.734683,8.620725,1.275851,-7.042105,-5.826482,-0.576887,4.725509,1.808952,4.893844,8.741173,-5.226296,-1.772613,6.760313,3.884214,7.976699,5.555870,-8.564450,1.810129,-0.641485,-1.561838,-8.824052,3.325295,9.515192,-5.781145,4.549162,-5.761031,-4.179055,5.718155,3.228041,7.274680,-1.854725,0.477038,-1.204557,-0.741882,5.665037,2.160033,9.808676,1.340645,5.200037,9.648894,5.762634,-2.916054,-7.506787,0.754690,-8.371726,5.528243,-7.261030,4.738385,2.612493,8.515897,-2.767655,-6.346550,-0.780828,-1.230972,8.724152,-2.713217,-7.472428,-3.542892,2.581878,-1.324593,2.390441,-8.898059,4.475129,-6.606792,1.659154,5.925933,-6.928930,-1.232660,2.237745,-4.782296,-7.950346,1.043949,0.409971,-5.621995,-0.736784,-6.987792,-0.555420,8.261742,-6.494501,-7.466659,8.364309,6.221233,7.076311,-4.710005,-5.420141,5.786663,-2.250385,7.636756,-0.207982,-0.563071,0.320566,-1.436835,6.064599,2.738104,2.978188,3.846037,4.426686,-9.602610,-8.070840,1.642349,3.993001,-1.061573,2.563765,8.719335,2.809445,-1.996488,-8.848351,-4.895506,-5.572397,9.508040,2.821204,4.688356,2.143941,1.581592,-9.511073,6.763496,3.904161,6.973444,4.278820,-4.166991,-6.689354,9.475373,-0.207294,-7.096631,1.350597,-8.290449,8.434800,7.435840,-6.549462,-0.392444,5.599512,-7.924300,0.570348,-6.707672,8.712056,1.691774,6.097311,-1.885697,-3.230013,6.863141,1.238774,-2.058495,3.491250,8.602800,-7.361520,-8.356511,3.334740,-0.963811,9.878406,-3.533183,-6.658175,-4.161606,-2.675816,6.428664,-1.732672,3.179719,-5.270415,-5.236201,8.293046,0.743353,5.546957,-0.084110,9.590938,-4.571519,2.030221,2.413049,-4.359544,8.928270,-1.440494,-5.760166,3.866029,-7.688189,7.868721,0.435049,4.388733,3.077653,7.832097,7.117279,-6.507441,5.984181,-3.806743,3.149280,-2.748896,-0.592757,9.940961,6.579893,-0.353803,6.250113,-0.189314,-3.094570,9.201953,3.601241,6.990024,4.578026,-3.420834,7.337410,1.785789,1.107980,-4.326050,6.023486,-5.837282,-1.645531,-7.678586,4.843503,0.060995,-2.292901,8.531357,4.421064,6.677659,-3.643317,3.459733,-2.757373,3.513659,-0.822187,3.735875,3.660385,5.622250,-3.635332,2.097796,-0.741370,-1.909031,-6.539193,-8.106416,-7.772405,-4.117853,2.197911,5.880778,9.710001,-8.332048,-5.598762,3.573766,4.132091,5.571989,-0.960310,2.455768,6.540051,-5.293911,4.637454,2.953214,-3.472883,8.313057,8.530797,4.807563,2.088310,2.969100,-0.173133,6.072548,2.717818,6.143628,-9.275005,-9.330890,-5.726849,7.924368,-7.840067,-9.988525,-4.709794,-3.228756,-4.936024,-3.789464,9.558429,6.304721,-8.234259,-7.520166,3.261906,-2.062517,-6.670853,-4.894457,6.215734,7.493700,-8.154143,-6.284561,3.805950,5.776309,-4.673868,1.646753,1.525207,2.999842,7.056331,0.201496,-4.162420,-5.631474,-8.957936,6.778926,-1.945135,7.171348,-1.829340,-2.739970,1.070789,6.281567,5.103356,6.228268,7.948445,7.113140,-1.403429,-1.441948,-4.811219,-7.706409,7.935855,-2.183320,-6.276338,-3.141037,3.835147,-7.701131,-9.815144,-5.209202,-3.171508,-0.410437,1.748890,-5.562432,-1.727718,-7.488710,-9.418260,-5.048014,-9.606937,0.919502,-7.575024,-0.204048,-8.262404,-2.030089,-1.811352,3.222545,3.170649,3.594176,1.110352,-6.619479,-1.042021,-3.061290,2.588871,-9.336932,1.570481,-4.021828,6.586501,5.940906,4.074499,9.329065,-0.754786,-7.583749,-4.020564,-6.976175,-5.309425,-3.611337,6.439099,5.675639,7.950123,3.042519,9.826311,-2.673588,-8.538325,4.486612,-1.848502,3.320897,5.244148,-5.926719,7.213940,8.583944,0.840439,-7.857594,-4.808487,-8.721426,9.058853,-2.346032,2.546184,-7.609590,-1.453823,-3.898218,-6.061259,7.298713,1.892981,1.098950,0.344373,-2.718539,-3.517336,3.964068,-1.147164,-7.625279,6.340647,6.698844,-2.881076,-9.797180,5.793213,7.578935,9.144173,0.823834,-6.490553,8.201424,0.343516,-5.104697,3.206684,-8.975655,2.263898,2.803015,5.310071,-0.825093,-6.395797,-2.903137,0.737381,9.300855,-0.379773,4.610609,-2.922619,-1.044990,0.308321,7.376213,2.458840,-0.539447,4.804003,6.725757,-3.885318,-4.503049,4.039885,-1.188980,-4.387870,2.332380,-4.073914,9.909403,5.964964,-4.442127,-5.097667,3.975949,5.364346,9.847685,-2.344607,3.388179,-4.892263,9.549732,-6.466043,-9.559707,-0.416821,-0.546975,-1.661259,2.956473,0.063666,-4.072632,6.013541,5.075473,-7.016310,2.631734,-6.483962,0.927754,-4.834677,-7.277473,9.201401,9.518327,-4.487071,-4.308136,1.360188,-0.892358,-4.394111,4.551922,5.269308,-7.798809,0.682223,-0.553304,3.823694,-8.372627,-4.386375,-7.567349,4.902584,8.720963,5.454650,-0.270080,1.677645,-1.251255,-3.466104,-7.333878,-6.021945,4.359961,-5.052022,8.855980,8.391910,-1.815558,-8.572371,6.012426,-8.632660,6.148906,5.332143,4.552764,0.045026,-7.683382,5.045290,6.284378,3.191153,1.093096,-1.820206,5.497611,-0.676052,8.955262,4.225375,-7.216135,-1.045800,6.311815,1.007725,-7.709010,-7.948780,-2.156087,0.499910,-6.328021,-1.434133,0.433395,-3.658217,8.820998,-6.366873,-1.424756,4.302383,5.077446,-5.480347,8.690822,5.526848,-5.623750,-2.759762,4.446802,-5.264687,2.486465,3.733612,2.120489,7.922278,-4.021796,-3.449373,7.197681,0.930507,9.720569,-8.850814,-8.131940,-1.990325,4.262987,9.200240,7.029894,-0.699143,8.650816,8.895553,-3.476060,2.255819,-6.314998,3.907820,4.384549,-9.377793,-4.886508,-0.104380,0.529916,-8.879969,2.144478,1.598229,4.897856,9.287264,-5.769322,-0.429445,-4.504986,8.639822,7.365371,-9.321092,-7.942226,9.776606,0.096960,6.691817,-4.024219,-2.495170,4.918715,-1.978441,9.592364,7.562485,-8.446744,-5.461882,0.977581,9.047577,-5.782635,-8.347149,3.197481,-3.252612,8.972457,2.469891,8.976921,7.235857,5.430522,1.234447,-1.499821,-9.877482,-9.644799,0.670087,6.998197,-5.455182,-1.806309,-9.847483,-5.730965,0.039440,-0.307512,-7.483485,-1.821503,-4.123373,7.157626,-1.872558,2.205693,9.367943,-4.790226,1.023909,6.514684,3.111094,-0.833125,9.171878,-7.365555,-1.013453,1.010111,-5.982544,8.455635,-5.653042,8.910828,-7.367536,2.366211,-7.098697,-1.915724,6.652144,-5.046659,5.056842,-6.130581,3.441879,8.368465,5.133098,-3.799786,-5.864069,7.575129,6.212063,-5.183420,7.079667,8.122252,2.648570,6.254356,3.360418,1.823387,7.598540,-9.650685,6.879250,-5.100997,-3.883185,-2.377590,-4.698079,0.815039,-0.449938,8.737961,-2.501737,-4.002142,-0.396628,-9.601525,9.688988,9.892366,-6.592727,9.021381,5.238766,-9.307615,0.894970,8.551966,-8.357938,2.239586,-6.787337,-2.235909,6.616034,-8.645448,4.070293,3.626981,-1.460673,1.265454,-9.704950,-4.877704,-9.254357,-9.779842,-8.699224,-7.558897,-6.466503,3.679026,-8.808532,7.211563,-0.994204,-6.072232,2.533033,-1.688638,-8.532906,-2.597889,3.251887,-1.064954,9.528045,4.391997,-4.790243,6.746618,8.145355,1.797349,-1.889639,1.064318,-0.784949,-7.388585,9.026613,-1.479221,-2.392814,3.885147,0.910332,-4.030907,-2.853056,-7.785478,7.132998,7.417867,9.363341,-1.306516,-3.444183,-2.771735,6.512046,-4.686686,-8.470665,-6.127134,2.779969,-3.366235,-1.169663,6.557653,-7.250615,4.106766,8.440494,-8.779928,-1.377307,8.883506,-3.898341,1.080752,-4.374997,-8.760813,-1.796027,-2.967230,-0.863131,3.211144,6.039742,5.644878,-3.396166,7.051090,-6.857534,-7.836445,-5.120981,5.772740,-4.687292,4.804723,-4.041641,2.595411,-6.169649,-3.146680,-5.580666,0.951055,-1.501891,0.221692,-2.033429,8.175870,-2.364809,3.866250,7.238894,7.386258,3.663943,-7.314950,-4.961591,8.865098,1.286746,-1.416395,3.804227,7.162542,-8.157103,-1.724307,2.328810,9.914108,-0.766522,6.972313,6.397638,9.513689,0.041774,-1.768711,0.646281,-9.481025,6.325337,-7.291781,0.833884,4.205791,-2.666842,-0.294395,4.837039,6.338313,-5.553610,4.836496,1.368056,-9.586551,-9.992538,-7.531523,-7.636423,8.048642,0.949144,-0.926982,9.603325,2.537384,-0.537890,-5.960902,1.534166,4.995893,-6.858810,-8.290594,0.047831,-1.648738,0.740857,6.232306,6.741948,-7.099337,-1.559738,0.540696,-6.564767,4.445015,-7.484579,-9.596963,8.946739,0.209650,-7.689282,5.866411,7.385512,6.413045,-3.397488,-8.228463,9.848386,3.842246,-1.562754,-4.677156,9.686820,4.613306,1.951661,5.334264,0.957719,-3.085786,-0.673330,3.169615,9.966093,2.812777,6.879396,3.374133,-4.572602,-6.979987,-7.534580,6.322022,-0.593765,9.365482,-3.392975,-3.816601,-8.190734,8.761151,-6.271909,-4.941700,7.556004,5.216481,2.426731,-2.114847,0.151969,-0.668016,5.441277,4.378861,-6.343888,0.246897,-4.014894,-5.511576,-2.840407,9.106105,-2.788784,-9.926121,3.612642,-2.206354,-0.182359,-8.094372,6.353933,9.657892,-9.370946,-3.149811,-5.477266,2.350255,5.178786,2.603011,7.497647,-6.746560,-4.101467,-9.560653,9.252421,-5.248416,4.426941,7.498380,-8.640692,1.714851,-8.388826,6.065064,7.640267,5.859040,5.848356,-9.117928,8.329947,-7.439708,4.693553,-6.401408,-3.321598,-1.705107,3.365567,-6.802493,8.155606,6.821490,-4.164479,-2.961439,5.997836,-9.586789,-5.833080,-0.098948,-6.896696,9.370434,1.855263,-5.125177,-2.914462,6.400327,-7.178146,9.498971,5.032670,8.033225,-4.364864,2.792171,9.807360,-7.287640,-6.270224,-1.267206,6.130593,-2.500232,1.063380,-6.053824,1.026128,4.519200,-4.576133,8.949181,6.903085,5.250940,-0.678293,-3.922655,-0.555807,1.489688,1.891875,3.918628,7.013616,7.354770,-9.549047,3.890805,1.945339,-5.689074,2.362996,7.041752,-0.430313,-2.801867,7.596345,1.392652,6.032937,-0.794230,-3.785414,-4.015248,8.209593,-6.851808,9.511390,0.705937,-5.413126,-3.449184,-6.333381,9.987737,-9.824862,2.884443,-7.382707,-9.113477,-7.231910,-9.187095,-7.946429,-7.713251,-1.008521,-3.805914,-3.972507,-4.669587,1.006152,0.391362,-6.677711,-4.994135,-1.222861,-7.975934,-3.967413,9.334529,1.181926,0.553345,-7.512390,7.284828,-0.458515,-8.994421,4.078644,-2.336106,-5.449813,-5.839897,-5.398943,7.674864,2.279374,6.694947,-7.550488,-6.566352,-4.380354,-1.300156,9.672051,8.018721,0.159550,3.612602,-8.583142,1.486813,4.859086,2.979217,-2.091474,-4.304138,-8.626870,-8.657508,-4.713052,-2.317332,-5.581059,2.421093,-6.535925,-6.352909,4.578226,-2.970014,7.152295,-4.741225,-0.205866,-7.216419,-5.926065,-6.768463,-3.700764,-6.405150,8.490065,2.734685,7.388047,0.623726,6.409362,0.955062,8.219935,-4.824880,1.640098,9.787124,-1.671164,-8.343857,9.702331,9.027548,7.589115,-0.423874,-7.230484,3.184124,5.223159,0.588607,-6.709080,3.014901,-1.888618,-8.878911,-0.361277,3.399607,0.036630,1.411843,-7.937997,-3.164639,-5.672110,-6.363064,-0.335561,-2.401905,7.787296,-0.117549,-2.368328,4.034592,0.008656,-7.166411,-6.323929,-0.837525,-7.412397,-3.209589,-6.326956,-7.291351,8.369170,1.598266,-8.267991,1.364059,2.114152,0.771384,7.521342,-4.495610,-7.398537,-2.590113,1.011061,-7.284812,9.323877,-0.585826,9.040547,-3.851557,-9.032463,-8.721696,-8.175066,-9.565338,3.522098,1.131758,-2.886436,3.222008,0.896286,9.334993,-6.410243,-0.776704,-1.000635,3.472277,2.345310,9.505434,3.920651,2.909832,1.139290,7.811096,0.942612,-7.165903,8.678334,2.313470,7.546826,9.398125,-5.200287,1.332979,-8.545718,1.407874,6.918645,7.885195,-3.255718,-5.324727,-9.680747,3.807713,-4.829131,-1.984008,2.670273,-3.323912,-8.944865,6.945205,2.759814,-4.226820,3.361175,-4.844479,-8.228359,-1.387859,-3.605928,-7.501425,-7.632730,-1.422700,1.805945,-9.244059,-2.030192,-2.347415,-0.474523,-1.975586,-1.211005,-7.310339,-3.343477,-9.714388,-6.686496,7.260192,7.460368,-9.812543,0.774168,7.292945,5.844469,-5.718765,-1.273512,-8.117894,-1.766746,5.233041,3.235487,-3.589913,-5.178573,-2.888092,7.983615,8.293460,-5.583067,1.306204,-4.027935,-8.756827,-6.884761,-1.680405,6.174257,-4.193244,4.458390,5.801470,9.794278,-5.210175,-2.267764,-4.600874,-3.552754,3.528977,1.732769,5.179487,0.768998,6.010626,-7.364641,-6.263039,4.046814,1.881613,-7.716580,5.304189,-1.903591,2.754890,3.999745,6.526845,0.939169,-8.233363,6.103964,7.770094,3.280533,-6.201231,-9.674454,-6.595606,2.391242,-4.483791,-9.704004,2.237447,5.083592,9.367589,5.346971,-4.812355,9.423215,0.695148,-2.426396,5.756451,-1.117622,4.910183,8.509164,-1.835495,8.300814,-9.664434,-4.782956,8.774118,6.838341,-9.300733,3.719526,5.148741,7.591573,3.266000,9.534888,-3.750815,-3.046942,-3.268759,4.169561,7.396022,1.201937,-8.418023,0.048772,9.934116,-4.551741,5.570343,6.559187,6.278635,-6.439523,-9.315294,9.854511,9.845544,9.742095,6.300987,-2.086605,2.972499,1.566791,8.461317,8.258137,1.304487,9.718572,7.792009,9.680798,5.835774,2.658333,-0.534462,-4.255959,5.639435,0.581500,-0.504834,6.155009,-6.306418,6.048248,0.220918,-1.527778,9.568910,-3.328344,-9.431441,9.110285,1.820601,-1.868416,3.418302,5.252969,-7.008657,-1.548209,-8.783217,-2.463954,-9.316066,-3.159425,3.823451,-2.464610,-8.517603,6.851869,-7.408404,2.983378,-3.332587,7.154716,-7.597989,-7.210745,-8.368729,-2.580777,-4.149399,8.656729,-0.585290,-5.562691,-8.048965,-6.168180,6.529589,-9.133784,-2.171411,7.970527,1.518075,0.523181,0.884553,-9.224806,-7.768732,-9.844407,4.469211,8.563510,-8.289178,5.141629,-9.298134,6.168792,-4.070041,9.779030,9.595439,6.773745,-0.681506,2.475447,-2.827131,7.385662,-8.163689,5.841786,6.386772,4.151043,-4.916944,-3.963834,1.537095,3.116429,9.677216,-7.026645,1.145092,2.258134,-6.784971,-2.462154,-6.770494,2.343942,0.266061,6.994402,6.922128,-1.967970,3.731880,-0.513859,1.344076,-1.495504,2.162513,1.296676,-7.249684,-3.849852,1.544461,9.204090,-4.916973,-3.798633,8.978080,-4.396835,2.101532,4.196138,6.164654,4.182663,2.627950,-2.451260,-7.549705,4.237569,-9.104997,-5.287577,-7.935645,-2.308622,-4.019883,5.102651,-7.100757,7.647011,-1.698325,-8.724155,-4.326663,-8.175420,-3.278853,-9.383658,7.554719,2.095016,9.414527,2.898117,-6.951063,-1.077917,8.292037,-3.110341,2.366439,8.738535,-6.857310,-4.231739,8.678822,-1.256942,7.403827,-5.991642,1.521722,-9.996097,1.623379,-6.286978,8.487853,9.519901,-5.005602,-4.174520,1.838078,-5.146568,-6.282674,-3.152609,5.738364,2.041160,-6.077837,1.166428,0.587610,-4.320191,-3.741928,-3.526541,-3.609430,-4.918488,-1.430475,-4.919766,-4.518483,9.145795,0.415835,-6.560649,2.687264,8.370829,6.395167,6.766896,3.545019,-6.681673,-4.093397,5.794669,-5.693223,-9.808199,6.721383,-6.843813,0.870838,-1.930549,8.373192,6.947271,-8.702241,-2.174507,-6.885262,-1.066791,-7.414211,8.437150,-5.933549,5.893901,-0.818200,9.719498,-5.539878,3.615181,8.696521,5.968618,-7.650793,8.307844,3.716592,-0.454680,1.031011,2.911635,4.784252,7.967198,-7.575466,-7.458545,-6.459198,-6.663949,4.843818,-1.802567,6.758833,-8.199533,-5.475759,-5.508908,8.480058,5.366096,3.692058,-4.091244,3.357947,-1.522152,-2.228085,-9.798416,-8.861965,-9.212411,-0.350295,2.340773,-6.209751,2.221873,4.155408,-9.264659,8.033784,-3.793531,2.804070,8.035710,-3.468252,-7.812463,3.762782,3.345979,8.420719,8.741117,-7.716932,2.107223,-1.098942,2.524263,-8.835785,4.391283,-1.837670,-0.048398,-5.295481,-4.212843,-0.040315,-4.422654,-4.413886,0.621959,9.861971,6.848840,0.575668,-0.703532,-0.420507,-2.215161,4.569714,-3.014662,0.299870,7.206873,-3.298954,-0.123157,-2.293745,-6.886940,-9.648836,-6.197903,8.502181,5.368180,-1.645181,-7.213173,5.010406,0.655326,-6.326481,-1.961043,9.091577,-3.073906,-6.174459,-3.422472,0.898833,5.080351,-7.816047,7.980334,6.651716,4.789640,-8.161233,-1.426483,-7.257747,-3.663551,8.593669,-8.020013,4.099566,8.105537,3.063701,-6.236451,-9.638155,-8.597258,-8.160896,-1.847825,-1.408813,5.127684,-8.454536,-0.695752,-1.054544,6.189688,-3.429705,-0.809097,-5.517010,1.500159,5.596590,-2.702299,1.385421,-4.960261,-5.466462,4.791656,-5.711363,4.736375,5.286117,8.239785,5.807457,9.185292,-5.942531,3.523176,4.261146,-5.103747,-0.152320,8.283546,2.297109,9.874594,-0.862436,-1.376469,-5.870409,0.414600,-8.518720,8.872819,-0.679036,9.616323,-6.481598,6.117141,7.050995,-4.882346,6.561909,1.057957,3.271980,-4.231886,3.307199,5.860363,1.216914,3.745240,2.635546,6.397207,-3.968778,3.114874,7.262171,-2.170985,-8.161897,-2.977385,-7.013900,5.574426,5.639145,-9.143864,-9.573742,-7.475190,-7.713161,6.553811,-5.684344,6.803206,0.746827,8.431114,-6.089602,8.938189,-1.709342,-2.794444,8.368094,-0.540777,6.474987,-1.294804,-5.082740,9.957039,-1.492407,3.075093,2.749061,6.939257,1.285846,7.689665,7.263754,-3.004057,9.898449,-5.841165,-1.224707,7.970545,5.212141,-6.824332,-9.245591,4.439017,-4.908462,9.944443,0.288538,3.733432,2.344315,-3.656234,4.096330,-7.703051,3.157277,-7.512503,7.251449,-1.320924,2.257794,7.346744,-3.485211,-2.416846,4.635110,8.181575,0.947644,5.336716,9.549918,2.215406,-3.437901,5.642619,-7.912700,-4.094573,8.282997,7.093973,7.441956,-2.981143,0.684467,-4.129717,-8.241203,5.051678,-7.068205,-7.223336,9.020058,4.403935,3.902132,0.992589,-8.697342,-4.818238,-2.416694,-0.006915,-3.299873,-1.363992,5.498270,-8.520232,-9.528415,8.235557,-0.521041,-2.399630,4.566460,8.452598,8.639646,6.596373,-9.402234,8.905748,6.286489,-0.540514,4.321284,0.908768,-4.425833,-1.130436,1.668332,4.093263,-3.791214,2.409395,0.385349,-5.097085,-3.989501,-5.592271,2.000657,8.618239,6.492256,-8.728197,-4.154270,-2.108836,4.470292,8.170320,-5.477649,-3.261493,1.113434,4.855673,9.738649,2.590783,6.581685,-3.917220,4.143057,8.328982,-0.413059,2.363285,7.856494,6.503419,7.304082,1.354498,1.865927,-0.377158,-0.825653,-8.717109,6.932329,4.023899,7.792486,-3.527425,1.127862,-1.520421,6.459970,0.023532,6.375173,-9.830515,9.989730,-2.694872,8.481838,1.722018,-8.557321,7.995471,4.396696,-1.685809,5.956650,-7.613802,-8.230745,-5.824336,-7.907067,-5.889319,-3.605738,-6.560027,2.874964,-5.410689,9.510932,-1.461885,9.056635,-1.756367,-9.847050,-5.970064,7.304151,-3.380292,1.208007,8.874845,-4.910699,8.120333,-9.747633,4.782615,-0.982874,3.582508,0.041317,-6.411330,4.472509,-0.554522,2.354340,5.583534,0.529884,5.553609,-1.341159,-6.722457,-4.952446,7.178099,-1.095017,-4.576023,4.058443,-6.265595,1.227399,5.881120,9.807119,-0.809755,-5.874496,4.946686,-4.966446,-3.317141,-0.745949,3.164935,-0.712700,4.269377,1.603059,-8.425061,6.626234,-9.511383,8.082830,-0.553610,8.367667,9.914124,-9.022877,9.882170,7.493991,-7.799485,-4.035253,1.228697,-4.663204,4.218826,-2.655735,-1.276346,9.631638,4.522146,7.072657,9.657854,-7.347641,-3.589339,-4.066703,2.483920,-0.340084,8.573315,-0.641612,7.478098,5.794411,-3.160570,-9.946297,-1.703457,0.418143,-9.593419,2.355739,4.308704,1.678616,-7.777750,8.867586,3.380296,9.349056,1.942337,5.238776,5.452262,0.327886,4.137487,-8.833522,8.263844,8.282643,-2.865030,-7.346335,-4.382215,-1.559661,1.323563,8.056214,6.423099,7.507607,-2.752268,0.857250,2.086401,1.075825,0.771189,-1.349607,-6.458617,-0.333045,-7.400160,-5.017564,-0.164913,-1.658136,3.061342,9.610984,-9.659341,0.828815,4.734416,-6.886620,8.643619,1.307137,-9.914594,-2.975904,6.285456,5.281099,5.431909,3.015998,-9.967967,0.593293,7.505404,-5.740584,0.871402,-0.007088,4.651215,1.084392,-5.285383,9.612729,8.887814,4.922022,-3.363592,-2.964226,1.071993,-9.005129,5.212428,5.344645,-6.377587,0.159144,3.179476,-3.182423,-9.905294,6.051401,9.646273,1.264667,-9.735448,4.090190,-1.084339,-9.264793,3.656175,4.225553,-0.791755,7.466544,7.038332,-7.132307,-1.848582,8.694236,5.901272,-9.023230,8.720685,0.271447,-0.690921,-4.268390,-5.848568,-5.747095,5.122720,0.073587,-3.923053,-1.554804,1.794081,-7.589280,-1.900682,-8.467902,4.318179,-6.961719,9.506438,-3.015967,-1.287295,-0.983822,-8.320190,7.078667,-7.010918,8.275942,9.429621,-1.091710,6.688237,1.160322,-9.173340,9.852749,-3.816823,-8.639040,9.096997,9.402707,-7.148204,-7.268923,6.626394,-3.449869,-5.075503,-7.489758,-6.538332,-0.174237,-7.168251,9.958118,-5.027096,-6.608652,-5.560951,-3.605790,9.042622,6.799524,7.377540,-6.301726,0.124261,-7.436004,3.375121,-6.344937,-5.510869,1.641448,-8.569431,0.962799,6.140300,0.782459,0.727520,6.017337,5.534773,-4.641630,-1.269665,8.761246,9.504308,-5.188351,6.097453,-1.709453,6.605687,-3.527184,-5.492047,-6.802266,1.876220,0.138007,3.461630,6.977568,-3.518373,4.931608,0.248601,-6.401050,3.501900,5.380216,0.785645,-5.474884,7.930763,-0.007765,-7.448809,8.564409,-8.152396,-4.557788,6.502427,4.078086,3.426470,-0.201074,6.468971,-7.539071,9.557996,8.506743,0.204157,-2.326187,-1.481354,1.550756,7.535337,-1.380016,9.402469,-8.157815,4.557841,-9.336396,-1.458421,6.183699,-9.022603,-4.303277,8.702873,-6.694424,4.000470,5.857276,-1.851946,2.478889,7.126985,4.084053,-1.030005,7.759957,8.084596,4.222972,-3.948230,-1.529492,-4.817874,8.333324,-6.904490,-3.095521,-7.474786,-3.385928,-1.390211,-5.330629,1.698778,7.967697,8.178967,2.435951,-9.009724,6.237435,2.017372,7.539489,-8.143321,4.895523,4.642827,3.598244,6.857150,-1.408489,8.795585,1.575394,-1.698146,-9.738053,9.878265,8.462036,-9.172083,9.225311,-8.456005,5.271792,7.312339,2.206788,7.754190,-6.539585,-3.124464,-9.381001,2.136755,4.523269,-7.579441,-4.450956,6.155200,-4.149816,-5.259378,-9.933106,-3.195848,5.916412,-9.053754,-7.830139,0.086808,0.638038,0.881399,1.061185,0.858332,7.811347,6.069370,-7.679283,0.004643,-5.490418,-0.624443,-7.667166,3.721601,-4.658809,-5.261087,1.882554,2.435746,-6.185720,-7.217568,6.604901,-5.646958,-4.827477,-1.419286,-8.947535,7.156892,2.032038,9.247162,-4.001909,-9.052288,3.014524,-7.648470,-8.180541,8.782467,-0.178672,2.370895,0.609364,-5.723898,7.193965,-0.364470,-7.326835,-5.349992,5.008112,3.888937,-5.601113,-1.507820,5.551248,-9.993705,-9.003740,-9.061124,-9.683044,3.126469,5.190866,1.589768,-1.813368,-6.910772,9.959792,5.717969,3.543190,-5.008553,-1.626396,8.624982,7.643818,0.309878,0.962923,1.818840,6.525209,9.518172,-6.524827,7.240543,6.275078,-2.708524,2.852868,3.871023,-7.871432,-1.218533,2.405070,-3.262459,-3.580066,-1.973978,6.959766,1.919175,-1.973621,6.463026,1.606445,-3.013438,9.521163,1.271771,-8.830369,6.540155,-7.511503,8.296375,3.857153,4.807258,3.021955,5.080722,3.144113,-5.141364,6.468437,-6.107451,-5.654461,4.885557,6.118988,-7.199895,-7.267663,8.139006,-2.679529,-5.562786,-9.449746,3.330018,1.159648,3.234120,0.474140,2.043358,1.234418,3.215418,-0.746376,0.809989,2.337088,8.177677,1.983272,-3.369789,4.190905,5.654901,-8.198807,9.873140,3.804798,-8.517331,-6.737384,-3.626543,-9.886848,-8.658083,-4.943306,-4.096687,3.358954,0.246231,-2.679101,-3.156087,-2.166499,-5.511302,-1.899521,8.150547,-7.815894,-0.613805,8.271614,-8.292476,-9.432215,-4.322667,3.615991,-5.397581,-8.635655,5.398167,-4.336652,-8.431359,-3.253785,2.210370,-2.312333,-0.668329,9.413530,-0.817413,2.533283,-2.976935,9.069639,1.396091,1.626625,7.363051,7.187814,2.313386,4.553968,1.200571,-1.025276,-4.301978,9.903770,6.611608,-3.204825,8.808491,-3.229027,3.149593,-1.601905,-0.451472,5.673111,9.139818,3.053070,-3.139594,-6.311191,-8.781703,-4.492957,2.409255,1.335421,-1.552142,-2.664247,-8.245851,3.459662,-2.749452,-0.320132,-6.673165,6.986049,-1.422595,-9.150734,4.632495,-5.671778,3.407110,-3.245874,-7.687280,5.836062,2.737703,-0.859493,-9.407493,-1.518230,5.829486,-4.852651,-5.822738,3.024913,-6.973386,5.738860,-0.394551,2.004315,-9.037918,7.032138,7.133290,-3.678714,-1.490888,-6.467713,-6.689108,-0.541301,2.017779,2.794688,-9.818912,6.344744,-3.770011,-4.785671,-1.686568,-9.682870,5.776888,-5.318910,-3.077479,-1.695482,7.380878,-7.145055,0.698148,-6.320474,1.948689,-2.428642,-1.328026,-7.600031,-7.992148,-5.135316,-2.512923,8.467124,-1.734035,-9.818204,-9.494685,9.908613,-7.847323,-5.793715,-2.377415,-8.082894,-7.750097,5.219451,-3.149420,-6.249693,-7.606847,-4.162204,6.595639,5.044378,1.739037,7.548471,-6.253428,5.701066,-0.694594,-9.797206,-4.198327,-6.316575,5.470702,-0.824725,8.749769,-8.253197,5.114486,-2.600029,-1.147769,-5.288794,2.371783,-6.216015,-6.585457,-4.626411,4.189320,-3.147630,-0.040598,-4.901824,-5.813755,3.736961,9.465322,-5.860232,-5.659691,-4.783097,-4.689537,-6.163070,-9.086318,1.431514,6.460029,8.954968,-2.185210,-4.457959,-8.256968,-8.549404,5.489478,-9.786350,4.492124,8.680828,3.101072,-5.245138,-1.605394,8.704070,8.259221,-2.484642,4.693493,5.493446,2.237521,-0.768364,6.363957,-6.227698,-3.421801,7.992013,0.064915,-1.989380,-3.219923,-9.734807,0.225761,0.880127,-8.657513,9.519940,3.142889,2.675222,3.359285,-6.383125,-2.434329,8.335828,4.433934,-8.429392,-6.925299,0.569436,-6.764485,7.114565,-8.284508,-2.978736,-7.338953,-9.665011,9.462757,-9.644384,8.349054,7.107323,-4.257137,-6.272938,3.549563,-9.486661,2.791306,9.202669,-5.687243,-9.057296,9.069284,0.915527,-8.668441,-5.831268,-9.308555,-8.625463,6.758391,2.544042,9.651524,-3.489821,8.046903,-7.267616,-9.645297,-8.115298,-5.557737,2.827781,5.838573,-0.465493,-7.885166,0.064007,3.034153,-2.814318,0.521100,-9.152863,-0.897645,-8.965954,-5.027467,-1.412852,-0.392601,0.820868,2.809553,-6.155371,8.074935,5.226252,9.296312,-7.938520,-0.425697,-2.546104,5.403326,-2.541225,2.106290,2.104540,1.504056,-9.038822,-1.606994,0.507551,2.411448,-0.138343,-8.904472,-8.907817,9.155019,-9.090094,-3.800778,0.836137,-5.038470,3.933780,-9.686182,6.289462,-7.345459,8.982561,3.777008,9.881861,1.158679,1.807454,1.899104,8.208849,2.751240,-8.732122,-4.983304,0.208680,-4.979156,-8.789924,6.120012,-5.048645,-5.463568,-8.105668,-2.343705,-3.538944,1.599914,7.148539,3.268321,2.206929,3.830374,-2.565952,-1.878578,-7.958003,-8.074581,1.876823,-0.066801,-6.814299,-0.113666,-3.352518,-0.197232,-0.974538,-8.246905,-2.180208,-6.356688,-9.029416,2.149700,-3.418382,-1.645061,-5.412969,3.319566,-1.673260,-0.783209,-8.208152,5.051312,9.047376,3.887408,-3.110357,-3.741736,-7.789970,-7.402115,-0.104301,1.034364,9.104751,1.179515,6.098001,-2.848616,-0.429125,-3.699400,7.367499,7.277570,1.370056,-6.890064,-9.533736,-8.106338,3.347793,-7.323996,-4.511038,-5.584553,2.202348,-3.831222,9.246476,2.902071,4.881950,-6.691024,1.919173,7.841377,8.599153,-7.636170,-3.040199,-7.911765,-1.700830,8.446950,-3.352656,-1.253164,4.078110,-6.368745,2.408963,-6.216216,0.733987,2.622619,-2.699623,4.298672,-2.911137,-4.175685,-0.651571,7.211658,6.696322,-0.308347,-7.970338,3.976275,5.478675,-1.615861,2.930763,3.118434,-2.186080,-3.087382,2.680409,-3.781826,7.540101,5.632695,4.205573,-5.450068,4.781674,-7.006157,-4.040929,-0.035800,-6.022601,-4.117060,3.477320,-4.544137,3.389442,9.143590,3.509682,-8.337570,-0.441281,-7.364777,-0.966179,-4.378476,0.624461,-2.630261,-8.854230,9.476901,9.933173,7.715096,5.691609,-5.602896,-0.143601,-4.155077,4.656611,-3.265919,-1.015278,6.432978,-9.662628,-7.156675,5.635559,8.624433,8.421594,-5.008088,-2.953139,-9.612541,9.898846,-3.289840,-9.590538,5.892242,-3.533736,6.045449,6.291620,6.172074,-7.608740,8.005066,-4.916585,8.155130,-8.454003,8.108355,2.342737,-3.341427,-0.424444,-6.034286,7.113926,7.612781,-3.915692,-6.593879,1.380539,1.762954,-2.137409,0.091522,2.782019,-1.862940,-3.932346,-7.313189,3.243613,2.060832,-6.724887,-8.097531,7.185618,9.436025,-8.378778,5.716125,6.504792,3.035869,-7.085664,3.123026,-9.434099,0.751261,5.326517,-6.990798,-5.531406,-8.069089,-3.505527,8.582509,-2.017447,0.852577,-9.732291,9.120633,6.082205,5.671742,4.895620,0.609447,7.754082,3.926924,-1.770646,2.363615,8.190532,0.997647,2.970522,9.045355,3.482597,-1.769574,-2.403008,-0.490450,1.566358,0.208490,-1.202960,-4.367418,8.227095,-9.969970,2.143554,-8.118624,3.765941,-8.903762,-9.216219,8.411037,-8.150127,-7.300777,6.733633,-8.481400,-8.330162,5.384909,-0.685882,-9.471005,8.180901,-8.078519,9.107518,2.881402,-7.271308,9.781025,-5.704356,2.464930,-6.901845,4.770381,-7.283579,-3.884195,6.020643,1.528023,1.745361,3.756533,-6.889621,-4.285298,-5.656363,-8.418005,0.519058,-3.469845,-1.130377,2.097825,4.619716,-9.066814,-5.905259,-1.618265,3.634028,-7.483069,-8.620593,5.785113,6.517944,-9.780377,-4.924491,-6.278465,-4.572334,3.334390,-4.469919,2.698845,3.797849,9.276797,2.572452,5.591941,7.558326,3.274737,2.928590,-5.300387,-6.448159,-4.808636,-9.960763,9.496765,0.445782,9.210608,3.480566,5.946038,4.479039,-6.035604,1.400523,5.358613,0.430510,-3.240205,9.632365,7.151924,3.636106,-1.953782,6.628410,-9.982805,-4.469394,-9.346969,-5.902673,-2.747390,6.482791,-0.835164,-7.251367,6.592027,1.900722,-2.473607,7.632414,-7.154431,-5.748254,-1.521074,-4.522686,-1.816525,-7.611120,-5.435199,8.504397,-6.017057,-0.981100,9.185070,-8.777746,-0.439971,-0.297309,1.641768,5.987808,-5.797480,-9.716796,7.886251,3.065854,-6.791662,-4.895539,-1.900427,3.825147,-6.273708,-9.956373,8.901349,7.485921,-2.325628,-6.118872,4.416693,8.370369,9.071300,-3.186432,7.326172,2.141626,8.438153,-7.982434,0.605347,5.393400,9.518863,2.619534,-4.470553,5.005808,-2.500453,-5.945932,2.053815,2.072470,-0.684627,3.850895,5.293931,1.791709,-4.473573,-1.600203,6.779076,-8.874041,6.449142,9.023428,-7.000633,-4.490504,7.665327,-5.423158,8.534122,1.226614,5.196144,1.746197,7.922870,6.922358,-1.670476,7.007390,7.652845,5.943344,9.701497,3.972985,2.268396,-4.477358,-5.333473,6.343265,-2.478046,0.509339,8.251107,-1.800878,6.606665,-3.745059,-5.721720,-6.234446,6.085201,-0.724104,-2.144165,-9.518873,-2.977360,-0.061619,7.465558,-3.369989,7.251416,2.235712,-4.656591,3.641574,-1.847948,1.441675,-8.450295,-9.180552,7.978169,-8.562339,-5.366446,1.811494,-1.096980,-2.371868,7.594489,0.811843,-2.395508,2.922989,3.830020,6.693021,1.946793,-2.931650,-4.724630,0.248656,6.065177,4.896680,7.131544,-3.400206,0.296534,4.208056,8.689815,6.460380,-6.913093,-2.826569,2.945920,3.665520,8.995426,-9.744785,-4.786411,8.947281,-6.125348,-1.264374,-5.235748,5.120905,5.113442,-9.362524,7.852630,-3.057144,3.840941,7.476089,-2.321742,6.250573,-7.675403,1.019465,2.561161,4.650864,-3.787051,0.374801,-3.360079,-0.563772,-4.082918,7.694149,-2.846464,3.819628,-5.671508,-0.953882,3.705607,-0.146218,-3.543302,-8.047475,9.452745,2.111608,9.654200,-1.940762,0.145198,2.267347,8.357030,8.299749,6.764618,5.686660,-3.662667,-0.967497,3.669325,8.004256,3.174589,-4.701658,4.222505,-9.029869,-7.302578,9.025999,2.385134,3.369322,5.060158,-3.286703,9.551416,-6.676627,6.346292,8.111849,-4.437572,-8.873478,2.952605,-4.272694,-4.825240,5.201969,7.545053,-6.415376,-1.264640,9.397475,8.149670,-0.778522,-9.904280,-1.919471,5.172953,-1.698948,-7.296790,5.954426,6.049005,6.009869,-8.031998,2.567508,3.066297,-6.399838,2.310624,4.160596,6.787883,-8.235145,-5.169254,-6.086805,-8.515605,9.062901,7.872787,-4.856234,-6.516812,5.251885,2.353854,-1.481826,-7.741269,-5.729000,0.969765,-0.648506,5.366815,-9.954830,0.368924,9.384755,1.124017,3.184990,-6.497554,-0.391061,4.867138,1.346303,-7.919829,5.185643,1.088557,-7.766635,7.364097,5.191532,2.395672,-2.214791,-5.702953,4.476533,2.732497,6.441705,-2.577845,-7.590379,4.526161,-8.779955,-8.512428,-4.048799,6.827358,-5.000007,-4.696119,1.913358,1.190434,-6.586322,-2.285987,9.089488,-0.139896,9.304518,-1.904864,-4.291583,7.603263,9.786078,-6.430665,6.353437,8.582960,-4.931170,-4.342512,0.390920,-6.909463,2.415656,5.226113,-6.356461,9.452550,0.945317,8.532537,6.326305,-7.593600,-5.547600,2.699694,8.286302,5.454804,-3.814928,6.453343,4.669500,3.704785,-6.165921,-3.593737,3.892868,-8.432838,5.455539,-6.796766,9.412480,-1.088806,-9.335201,0.214025,-4.130366,8.810888,-2.223053,-3.352159,-4.286559,3.321912,2.270961,0.273139,5.254297,7.905747,-5.831803,-1.132087,-8.098858,1.734900,-2.463963,-7.827261,-2.447560,3.048489,3.676371,-6.096029,6.665256,-7.352674,1.127070,0.486813,-4.053169,-3.967731,2.728971,-4.142103,8.229075,-7.404913,-6.863267,-2.090476,-8.464920,-8.841877,5.664875,-9.511660,-6.204575,9.033994,-4.325153,-7.412383,3.991488,5.611503,0.743473,3.512780,-8.931218,-7.888190,-0.472072,4.740831,-5.820640,-9.247703,-4.258800,9.340399,-1.748208,6.913467,2.662180,8.466100,-6.459968,6.624369,-6.182425,-2.328399,-6.244295,5.651774,3.681717,-1.992805,-6.981409,1.272131,5.174571,0.651146,-6.722416,-0.942597,4.110193,-9.578521,6.702452,7.323165,-6.409958,-2.482362,0.260980,-6.532369,-5.498576,-6.239217,4.587427,4.929355,-7.485916,-1.789503,6.689383,8.026171,-2.617511,-4.077596,2.953913,3.371347,8.918777,4.712794,-6.082961,8.599719,-4.109646,1.123824,-6.703817,-2.895929,-1.373818,5.717939,2.570287,-0.856617,-3.779118,2.579811,-2.178459,-6.720520,-3.110011,-8.254613,6.335428,0.486276,-2.359751,9.768505,-0.271936,6.609691,8.148196,-9.865500,7.692016,-3.413904,-6.019220,-2.179507,2.359381,-0.144419,-3.805145,-5.962740,8.498977,5.561312,-3.966841,-5.609247,-1.040220,3.037615,-6.863019,-4.613957,-8.104374,8.371574,8.404323,-8.854548,-6.750845,-5.640475,0.444089,-9.712159,3.517970,-9.388343,8.014462,-5.888697,1.070616,9.092425,1.101860,1.335334,-7.684249,-9.735634,-9.256966,-2.528596,-3.089177,5.260974,5.006744,-7.402890,8.455235,3.978252,0.010582,-7.522568,3.582133,-7.329919,-9.766483,0.433349,-1.030723,-3.747767,-9.103246,-3.710791,2.155440,-4.778174,9.513309,2.772209,-6.696193,1.948279,-2.556542,-6.881301,0.090722,3.425899,-7.627703,0.053757,-2.720529,-2.067632,-6.093958,1.227885,-9.224068,5.523668,-6.195756,1.629393,8.095924,-7.847198,-1.754580,1.038419,6.807312,3.308658,3.475281,7.553314,-6.771173,-4.243379,-5.330288,6.099969,-4.707775,-1.926135,7.314081,4.374330,5.309932,0.931016,-9.126137,2.027840,7.283329,6.541519,2.462826,-2.383003,-4.605029,0.474944,1.876729,-4.766130,3.233802,-1.447444,-6.619215,8.892915,-7.605718,3.866426,5.679143,-7.695772,-8.466947,-9.167036,-9.180649,0.718725,0.538421,9.100486,8.452505,-4.906612,7.510918,-3.975200,-2.007700,1.666970,-0.197758,3.991536,0.297817,-8.646884,-8.723921,-1.867411,8.872526,9.791253,-2.313634,7.282863,-3.623801,-4.905010,5.879936,3.048367,-9.644938,-9.967558,-3.996561,-9.643611,7.834870,9.010157,9.950070,8.378535,8.332410,-6.915211,2.029512,-6.585020,8.451256,3.372219,6.589087,3.561330,9.105256,-1.283949,5.565572,-8.202421,8.228327,-4.044456,2.479200,0.889200,0.959246,-9.604274,-6.128848,-9.554355,7.289498,-8.875188,9.962919,-4.621772,5.401810,-1.129612,0.108805,5.493583,-0.783795,-1.111903,4.071224,-9.229712,3.045178,-4.861079,4.191835,2.881040,-0.225634,8.547380,8.778458,2.320712,-2.052593,-8.782207,-9.829848,-2.356181,7.679791,-0.983761,4.698318,6.134649,7.451036,-1.998420,7.075290,4.247470,3.168476,3.420014,-6.592163,2.491547,-3.961615,-0.740778,3.819860,8.539836,3.538477,-4.082182,-7.223613,3.558848,9.892918,0.966003,-9.276729,-0.343900,3.359701,-1.702301,-3.845888,2.357924,3.748301,8.324496,-0.085736,-4.561060,-0.907394,-0.443641,-1.252377,-6.974011,1.900828,-6.273920,-7.980175,7.638762,-2.975272,3.609754,1.791165,1.574303,2.514184,-3.506124,8.869420,1.598429,0.964514,7.066859,-9.317083,7.059194,9.482962,0.465970,-0.945812,8.789630,-6.955278,-0.508513,6.809650,1.796887,-1.480850,4.266537,-0.008503,-0.206441,-5.619443,7.128621,4.742617,5.337008,2.234524,2.408677,1.443038,-8.577363,4.982484,-2.504259,8.249155,8.086290,2.007694,6.173994,-5.676753,7.116822,6.440727,8.261843,7.228514,8.327089,2.488670,-3.083466,-5.002422,-9.939198,4.731329,-1.696381,-6.503582,4.256222,-7.205491,8.208841,-1.572941,-7.209638,-5.049623,-6.489339,-9.476245,-1.450879,-3.697508,-9.778585,4.124427,5.492287,8.989101,2.477246,5.954682,5.562804,-4.492986,-8.333058,5.510562,-0.440485,-6.736246,2.219560,9.180281,-2.671642,1.169992,-7.453060,-0.191885,8.466913,6.279624,5.603608,8.755251,8.966866,-1.145530,-7.168012,-9.187723,3.784710,-8.496783,3.381395,-5.956906,0.535900,-4.954274,-2.481835,5.839846,0.901535,0.066467,-3.760065,7.200392,-9.942171,7.968006,-3.709256,1.269854,6.287271,-6.522959,3.170987,-3.580155,-5.586605,-0.022137,1.458601,2.064500,5.762326,-7.880515,0.095637,8.983457,6.788806,1.022803,-6.559537,5.034889,-7.802442,-8.425400,-9.494075,-6.345027,4.092852,2.170363,1.633459,8.852633,4.694490,-1.414439,-9.550667,-1.877681,-3.724969,0.989677,9.188895,-9.514263,-3.657317,4.160747,-1.857248,-5.625194,7.081931,-1.660824,-9.998139,2.811379,9.435592,-0.773303,6.511808,5.291978,-5.664708,-8.611384,3.971136,2.406492,8.634458,-7.211336,6.360098,0.148543,1.803704,5.937430,-3.179955,5.244282,-1.005183,6.048267,8.506310,0.132127,3.989782,0.214009,5.876852,-1.686080,2.080898,-3.676835,1.909126,4.776316,1.731641,-7.971859,5.686071,-7.732890,-9.157091,5.054154,-0.306710,0.737085,-8.740442,7.001928,-1.429693,-3.663028,-9.777610,-3.065632,6.186324,-2.471656,-8.982543,-2.145764,7.436686,2.382312,-2.062547,3.092360,6.453190,-1.220703,8.916782,2.968534,7.246214,2.294896,-2.625096,-4.571482,-6.688820,7.714723,3.159212,-3.262501,-5.642904,-4.999410,7.334144,6.210166,8.637506,-7.712639,4.194710,-4.291757,-9.101245,4.948866,7.513206,-4.673038,-1.646343,-3.399292,7.917766,-4.816333,-4.833162,-8.132939,-2.409163,-9.700293,5.960445,-3.275129,7.962302,1.660419,8.611578,-5.684843,-8.694042,-4.332933,-2.617127,4.207752,8.424546,2.407865,-3.008548,3.196377,-1.108501,-0.266466,5.450172,-6.829242,2.935143,-6.046877,-1.091633,2.457191,0.882625,-3.852104,-8.261098,8.263759,7.296020,0.939841,-8.342815,1.123068,0.809964,-2.549811,-0.908304,5.210407,-5.594546,-7.532260,-6.068338,-6.432056,5.749841,-5.262574,-5.398973,-5.949062,-1.688787,5.249324,-6.056733,5.693574,2.354038,-5.017381,8.530543,8.157214,6.387688,-5.230432,-1.232124,4.370237,4.402929,1.477727,6.144797,-6.748803,-7.788462,-0.066476,-6.649663,-4.239152,2.193370,8.075674,-4.722444,6.754112,8.317229,0.296380,-0.819333,4.561570,-2.181390,6.842249,-2.083714,-0.859213,7.284412,-1.072053,-0.489201,0.334600,4.332760,-9.912798,-4.877563,-7.014532,-6.828187,6.038736,-1.418610,-9.048949,8.293282,0.785200,9.639381,-6.825451,-3.791445,-6.193526,5.690052,7.912043,8.348723,-1.521232,8.709592,8.606697,6.810039,-3.131576,7.310337,-7.411057,-9.386462,1.463680,3.845070,-9.845737,-8.986398,8.135967,5.485396,-2.783566,-8.083619,-3.819173,0.179829,1.080189,-8.243072,1.063876,3.164322,-1.487933,0.469205,8.825943,-1.357996,-6.074398,6.776259,-1.705593,-4.638088,1.291486,-2.635669,-7.904598,5.691049,-5.208242,9.599897,5.934002,3.511627,-3.270246,2.975405,-9.111924,-4.532854,-3.047262,-0.134733,-3.996961,-4.252693,1.881472,9.500287,-7.155109,-0.376639,-4.364081,-2.171079,-3.892056,6.348840,-0.795454,-9.712180,-6.869779,-0.984077,-0.826117,-9.457290,2.272181,-5.387707,2.090625,7.760199,-7.584040,-3.195402,2.864190,7.835794,-0.406835,5.228453,4.213740,2.352458,-1.755775,4.733809,-0.942967,0.593041,-3.277044,5.864896,1.189767,1.203671,-6.638189,-1.372695,7.492727,9.712791,-5.351931,-5.694754,-3.085299,-5.862549,8.141377,-4.521956,8.618429,-1.116216,5.867452,1.671886,-9.742130,2.400728,-2.247767,-2.250145,4.447724,5.389334,-4.761631,3.886411,-9.780039,1.542383,3.007891,2.058645,8.110571,-2.680568,8.219198,4.002626,7.887576,-1.916861,-5.968805,5.965891,-4.854411,-1.536466,-6.912554,-7.454681,4.842555,7.593118,0.885472,0.273199,-1.417940,1.412414,3.269989,9.429716,6.242326,-5.831907,-9.129409,9.529834,-9.201543,-4.894617,-1.849680,6.181490,-9.843523,-1.486367,-5.235254,3.814653,-8.079184,-7.969224,7.235261,-3.348309,-5.244613,9.071114,-5.185220,2.286463,-9.250765,0.484636,-4.441411,-8.160549,6.092702,-3.877135,-9.263624,-4.416074,1.818979,-3.771151,-7.372943,4.341536,3.766753,-4.560621,-3.497769,-8.522106,5.258411,3.115250,6.839398,-3.995677,-9.613747,-7.954110,-8.728443,5.019370,8.275277,8.349733,-2.551069,-9.304546,2.294892,1.692062,9.394860,-1.170517,-9.482212,-5.775748,9.119989,-2.093392,-8.375605,-7.415157,-8.288475,-6.710859,8.037895,5.150094,-2.686633,1.974219,-7.772793,8.257258,-4.798258,-5.369974,6.674873,-0.212631,-1.968303,1.082519,2.990125,1.484317,5.411433,-7.647963,4.713556,0.616432,4.792328,7.969584,5.126103,4.011107,-9.902954,-5.153300,0.484154,-3.914144,-0.752562,-7.981766,3.339227,8.640297,2.723273,0.869643,7.479882,-8.607792,1.462965,2.269574,0.269562,3.285469,-9.812616,6.860976,-5.022099,1.900238,7.699487,4.937795,-5.665971,-0.840406,-8.536731,-3.761408,-3.586298,-9.494171,0.902255,-3.471555,6.449983,-3.064016,-9.304253,3.652971,-7.206065,4.604161,-2.002456,-0.874476,3.493398,-7.361574,9.100145,9.406468,6.086013,3.606900,3.442630,4.663085,2.601061,2.942245,-4.123606,4.820538,3.963393,-4.862651,3.479857,-0.583843,3.768599,-9.651597,-9.948694,-5.820791,8.751943,-9.156052,-4.520748,7.848571,6.779592,9.194015,6.599595,-1.508975,2.106008,-0.310075,-2.273954,1.374792,0.686740,-4.378543,9.827478,-9.894576,-5.511879,-6.389495,-6.255486,2.595746,-9.987738,8.128332,6.346163,-1.729828,9.846116,6.609715,-9.314047,3.136129,-8.169208,2.505147,1.928590,-9.302204,-1.136747,-4.840325,0.024628,-2.190411,-0.893573,6.272813,-6.399815,-1.865682,5.009888,8.895479,-2.475237,3.391303,-1.963726,-9.745680,-5.181005,0.857463,2.299474,-0.108587,8.993677,-9.607636,-7.200202,0.417405,-6.734607,-5.222677,7.844524,8.214600,2.520427,-7.228175,7.305738,3.686603,-1.032045,-0.409303,-8.080674,-5.097586,2.210286,3.191827,-1.858414,-1.164565,-0.169077,-7.582823,-7.739534,9.811811,2.280888,4.736684,-6.377650,-6.523490,-2.277557,4.947175,0.391039,-8.616480,-9.187834,5.248810,5.119963,6.288546,-9.661941,7.731868,9.863334,-2.320047,6.520198,2.537476,-4.396518,-6.387768,-5.263036,7.812780,0.046449,2.548147,2.969875,-8.646815,-6.025292,-7.366877,-6.408220,-9.515579,-9.254949,-8.428546,-2.357621,-8.130394,3.291384,8.020756,-0.079373,-9.928550,3.953457,5.707182,-4.686320,3.576673,-6.987759,2.562499,0.153194,-4.075962,3.352169,2.240294,8.605306,-8.742667,-3.991106,-5.611177,4.211609,-8.933793,-9.697062,4.794762,-9.680148,-5.532580,1.793581,3.721304,5.523972,-8.428875,-6.428537,-5.006603,3.985605,-4.856361,1.450133,-1.643965,8.515505,7.644577,5.077928,-7.830481,8.210155,-6.421427,5.194085,9.191343,7.379864,0.448279,-8.290472,5.435901,-9.403254,8.857574,0.653794,-9.163375,5.538023,-0.184565,6.529720,-2.998630,8.258019,7.866210,-7.936764,1.073735,-9.941507,5.974208,5.640773,8.137395,-1.228020,1.009466,-1.813614,8.419153,1.315470,-9.578619,-3.842177,5.993261,5.730962,-2.692669,1.090471,-7.241182,-0.802376,-3.730820,-3.569166,-8.472103,8.067917,-5.539181,1.589963,0.640462,-0.890370,2.787420,-4.616518,-5.081515,2.328148,7.288898,1.071691,1.589074,3.688583,1.993696,0.458089,-9.457209,3.625323,-9.559444,-4.563029,5.873922,-8.025872,-1.138442,7.123600,-5.581922,0.497031,3.866159,7.477634,2.133262,7.492042,8.745795,-2.192532,5.800244,-4.399755,-6.748446,4.576838,4.363139,6.266956,-4.059674,4.790441,6.320563,-1.854710,1.974621,8.454584,-9.844787,7.535074,4.553305,3.893725,4.696939,6.272207,9.186600,6.059201,-1.422216,-8.281127,8.162421,9.103572,-2.639833,9.575989,-9.859601,-4.894836,1.861361,-3.131424,8.381943,3.727620,7.316428,8.492365,5.138126,-3.571244,2.157928,-0.875023,-4.334338,6.531147,1.613350,-9.703956,-1.756799,-0.337639,-4.340913,-0.977264,7.717496,-1.191821,-0.083080,4.140658,-8.178993,7.976907,-7.815645,-8.864938,-3.871836,0.143387,-6.118793,3.969218,9.710266,6.754267,-8.173448,7.779809,2.920682,-8.099977,9.534663,-6.446353,9.742673,7.178805,7.715485,-6.031574,-8.775076,-7.197156,3.344160,6.656660,1.258512,-9.347201,-5.899985,3.153552,3.524107,-3.094182,3.582279,-2.242111,-2.525278,-5.279351,0.745893,0.637617,1.065825,4.544625,7.624573,3.831608,1.278179,-9.773370,1.032447,3.817730,-3.394226,-0.231364,-8.307880,-8.347146,-3.949025,9.128208,-8.098153,3.366322,-0.822547,-2.036481,4.645235,-5.960844,-0.647930,2.620930,9.998488,-9.737673,-8.412830,3.380504,-6.398342,6.172983,8.468644,-6.503586,-7.178716,2.044463,-3.745729,-3.690261,4.612592,-0.387097,-1.324145,9.246133,1.571783,4.346214,-3.852110,-7.613457,-4.546874,-7.684028,-9.304742,1.624427,-7.958133,0.800738,1.074717,6.328138,7.974616,-0.827711,7.832589,9.887265,0.238148,-7.456275,6.718797,-8.399927,-4.351742,0.114341,-6.322888,8.332630,9.769296,0.097938,4.331094,3.647703,7.751840,-4.755586,-8.321709,1.085061,-7.412187,6.579303,-4.966716,4.099555,-3.351980,-8.589044,-9.121163,-9.400765,-8.299410,-8.704345,-1.342917,-3.067923,5.459749,-9.085137,-6.672006,1.307740,4.979346,6.330235,7.903845,-2.109887,1.425546,-3.460168,2.565675,-9.725102,-9.773447,4.116565,-7.477955,-3.942549,-1.474200,4.278469,-5.405091,0.734236,-4.606044,-0.078614,6.856045,9.036357,8.674090,-8.413803,-8.451883,-9.681252,0.577417,6.864551,-0.830748,8.645972,-9.390215,7.774077,-8.585691,-4.365853,4.658579,-2.112177,-4.828519,-6.613348,9.893640,-4.942435,8.269995,-7.452923,-2.705649,-8.977490,-7.527804,4.169473,9.630212,6.223822,3.100593,-0.678342,-9.243222,2.502186,-2.108523,-1.376685,7.757815,-5.596816,-1.126075,7.916551,-8.996522,4.046029,-3.231530,-2.375191,5.027973,9.581002,9.607798,-6.199013,-7.091276,-2.270402,0.819411,-8.659809,4.516409,7.914305,2.138562,-3.366138,-6.778603,-5.126945,-3.482993,-6.736678,7.585737,-7.253382,3.524327,-6.194755,4.595004,8.432188,-1.773013,7.281249,-6.691007,5.201755,7.576523,0.705674,0.086918,-5.370102,-6.566958,6.078351,-9.495410,9.737702,-3.584015,1.757593,-6.396352,-7.950666,-4.728674,1.289845,-0.844229,0.333463,-2.923822,-3.198214,-6.288004,-2.493396,2.114982,-9.241707,3.550720,-5.799611,-4.274359,3.068515,-5.518595,4.216517,8.264829,7.935345,0.529312,-7.584073,4.189459,7.864116,3.514855,0.428943,3.973551,3.739883,8.603650,6.162922,8.710097,-0.788220,-4.541590,6.338384,-1.395324,-2.541252,7.104195,-5.879124,8.221117,-4.455611,6.300164,3.194141,-7.333313,0.821386,-3.482516,7.152492,-1.684701,5.596775,3.174647,-5.399350,2.071309,2.406895,7.463510,-6.813369,5.688115,-6.851045,-9.109004,4.421092,-8.223698,-0.924023,5.932570,-4.331406,8.685978,4.163984,-3.748445,6.835099,-9.906523,-0.675576,-0.168856,-3.719864,-1.612554,-6.494812,-0.438680,8.396490,-0.939827,-3.324714,8.444775,8.510046,-0.249599,3.932817,7.936479,2.072867,7.163503,2.219480,-2.066858,1.298121,-1.981927,9.563095,1.440387,6.067159,-6.115644,-4.533973,3.666203,-9.207558,-2.162318,-5.813313,-9.445616,6.330444,-1.278002,2.067585,-2.540724,0.671389,-3.070725,5.129629,6.732560,-7.359338,-6.373354,9.513786,-5.942775,-4.875208,6.189900,-3.402132,-1.671110,5.298297,4.430506,8.741227,4.665492,-2.948777,4.173795,0.085302,8.890184,-0.837667,-0.261539,7.564657,0.393059,2.210111,-3.446936,0.819465,2.067030,7.683776,9.745807,-5.804887,0.234849,7.758866,4.419374,9.156751,-5.930805,-7.703820,0.870910,1.888435,4.825739,6.048904,0.347283,-6.861238,3.381780,1.960802,-5.113816,9.926704,-8.983939,-0.294755,-3.748917,-5.364842,0.804966,6.008099,-2.677125,-4.005968,-3.032611,-2.444756,-4.372689,-7.870640,-1.034733,-5.405827,-3.413801,8.147940,-2.644513,-2.120702,0.422818,6.183600,0.943475,-9.408720,-5.615136,-1.224440,-1.269801,-4.551417,4.801577,7.154804,-8.822302,8.306237,8.952201,9.112411,-1.121383,-9.935446,9.239189,6.850543,9.748247,-7.184120,-3.170450,-1.913480,2.033229,5.804678,3.470807,1.147315,-0.707926,-6.365695,9.473015,-5.326746,9.296653,3.862842,-7.973366,-0.629852,-0.848322,5.747697,6.174612,-6.501357,-8.500296,1.889741,-6.514854,1.159119,0.588210,-9.442159,-6.328233,4.547303,-3.787585,-9.580253,1.085771,-9.484981,1.704594,-9.613251,3.889547,-9.564903,-8.012369,5.075255,-7.561564,1.181856,4.405684,-2.533081,-9.793989,2.687596,-4.037276,-3.461189,-0.626467,-7.244331,-9.973262,-3.778648,3.515242,-7.176744,1.110027,-4.510189,-2.757634,1.665849,3.828794,5.149527,3.254389,-4.147758,-0.883628,3.568675,0.591247,4.427408,-0.585218,7.843096,-4.516673,7.817865,-4.425690,1.196821,-0.671108,-3.116534,-9.344381,1.730073,-4.803551,5.741505,-1.644065,-4.089754,-1.556315,-3.330236,6.249409,-2.698524,3.892221,6.983888,6.503153,-1.486107,-5.094627,-9.621539,3.922910,-0.176154,1.155915,-2.137461,9.106600,-5.182283,-0.902044,-4.608924,-9.490664,7.023754,0.392397,5.042313,7.385412,-2.111024,-9.565377,-0.836892,-5.000420,-8.423916,4.636484,-5.935027,8.602244,-7.282588,6.597980,6.043933,-8.481406,9.531729,-3.744015,-8.528326,-7.252131,2.336439,3.162083,-2.652787,-6.640416,-5.585306,-9.769083,-9.187536,1.820715,1.059706,-3.562541,-8.046705,-3.571958,-7.219560,7.363914,-5.933677,3.830958,-1.345192,-5.654192,-6.064665,6.434730,-3.152211,7.589200,0.982424,3.548922,2.075219,-3.664115,-6.875930,1.254150,9.915136,-9.834665,8.262895,5.528952,-9.251876,-0.473361,-5.483864,2.055861,8.360689,-6.258333,5.835265,-7.979433,6.366189,3.038244,1.653547,-2.379072,3.010210,-2.105141,-5.962816,-2.757477,5.298063,9.362028,3.983057,-7.451040,-7.108660,7.038038,9.149009,-9.535547,-4.256759,-7.218304,3.536358,-8.458420,1.624206,0.883263,-5.505304,7.440702,-2.702142,-3.326930,0.807749,1.587163,9.759782,-4.580352,-5.111308,7.475755,-5.564027,-3.794937,-8.484537,-9.551701,5.683591,5.482926,5.737346,-3.985132,4.476869,1.667033,5.400527,-0.151293,-8.962258,7.645856,-3.464962,4.265452,2.598605,-2.841448,8.447848,2.330212,-3.933063,-8.860946,6.126010,8.339188,5.778736,-0.175282,3.865044,9.114965,2.393391,-3.507158,5.004753,-9.120673,6.821239,-6.028316,9.712886,-9.112973,-2.513300,9.543630,2.861306,8.575014,-2.856133,4.033249,-3.443087,8.078847,-6.114664,0.716438,2.639125,-7.755248,-1.677614,4.530773,-3.026284,2.434242,4.543284,9.671072,-0.741009,6.458366,-6.941700,-1.585159,-2.739393,-4.131831,-1.940401,-8.898011,3.173541,-6.142520,-7.901911,5.516281,9.664150,4.281566,6.487391,0.313511,9.044172,-8.975056,-9.221770,3.877355,-5.553833,8.212961,1.066403,2.471249,-0.851910,1.896807,6.478996,0.489474,3.190959,9.570381,4.468163,-8.752662,-4.017797,-7.121419,-4.625296,4.254896,1.862046,0.092487,-4.440612,5.381135,-5.739042,1.193124,1.033390,5.893276,-3.059794,-5.173495,2.785041,-0.996072,1.386473,-9.747886,-8.134634,7.845267,-6.017140,8.430727,3.042420,0.792007,5.086293,6.489264,-4.535792,8.694448,-8.169358,-3.720578,6.454784,5.530223,-3.120196,-7.596303,2.203491,-3.143265,-0.152576,-5.604596,7.722191,0.668330,7.161938,2.219476,0.691901,-9.724243,-4.748365,-6.419159,4.848486,7.966589,1.830003,8.119162,1.962903,6.932649,0.866443,0.910169,1.662146,7.765576,6.696497,-1.941570,9.357761,-3.773270,-4.440393,3.654496,-2.535382,3.694548,-8.239388,-8.416907,-1.184046,2.680586,-8.243956,-2.789256,-5.951240,-6.848121,6.732785,-7.246502,9.076070,-7.497059,2.153112,5.085196,-5.186116,-1.195369,3.954302,-4.474173,-9.366248,5.598564,-5.035856,-5.714664,5.877633,1.744063,-7.162393,-3.151665,-5.799134,4.229476,-1.835534,-6.743506,8.600796,-0.095621,4.410743,-2.475329,-1.291494,-7.203464,-8.421169,8.583226,5.223794,-6.452099,7.008956,7.058243,4.890147,2.744167,-6.635638,2.273389,-3.219616,-7.669510,-1.539479,1.808937,3.376677,-7.439959,5.645248,0.683140,-5.511468,-6.081784,-7.153425,2.888007,-4.369139,-1.596695,-6.451253,-6.280509,7.888195,6.993414,2.437008,-1.890745,-7.186035,-9.321804,8.364401,6.084210,3.408889,3.153301,0.252738,-0.421957,3.827272,-3.484567,-5.019671,4.265895,-0.654063,7.945687,3.959054,-7.978916,-3.653215,7.335155,-9.647884,1.497179,-8.325944,-0.834317,-7.438923,5.129005,1.247478,9.721540,-7.356234,0.642525,1.439370,5.307727,-4.340527,4.769278,-4.065192,-9.244167,9.311301,1.638359,-4.023433,6.477893,-0.765311,4.813205,7.243996,9.325976,5.372901,-7.563952,5.087173,0.346165,5.971593,8.971915,-9.277399,-3.149380,2.060505,7.060347,0.236261,-6.471595,-9.361943,0.202693,7.671923,5.609084,8.222583,7.395118,9.775586,1.915517,3.306177,9.045571,-1.272852,5.705692,4.838457,-1.282464,-3.469439,-7.861923,-7.284637,-7.890644,-7.836187,-0.775754,7.604936,-2.714142,-7.763935,4.242672,-4.921052,3.234818,-0.216565,2.479132,-0.319129,3.942851,-5.902128,0.103097,4.646783,-2.026145,8.409461,-8.958475,4.010345,-2.561952,-8.565719,2.714599,-6.487422,0.083350,-4.843238,-6.698475,-8.097634,9.016823,2.489003,8.961439,-1.555409,-9.192838,-4.770674,-6.641472,2.380599,-3.873417,-7.351302,2.357722,-2.896157,3.872144,8.181478,4.947121,9.000670,-9.012644,0.685499,-1.908893,-6.809059,-2.012133,4.730656,-7.611568,6.723401,-1.638694,-5.580716,-7.483041,-5.910049,3.236689,7.978838,-0.599514,6.787275,2.542567,-9.340189,-0.788395,-2.089565,-6.579420,9.290235,-0.871820,5.765355,-0.299546,-5.080592,-3.599990,9.101787,-2.073114,6.537632,8.721887,-7.231243,8.370131,-6.696640,0.010413,-1.481910,-8.489805,-6.902672,-5.903628,9.599941,3.310529,6.639638,1.202811,-1.216015,9.667774,-8.646314,-1.389300,6.809444,6.592753,-7.707324,-2.591748,-4.627466,-5.930682,-9.292613,-4.771492,-3.931287,5.940805,-5.530706,-7.064572,7.086037,-5.935708,-5.813898,-7.994343,-3.336432,-0.272704,-1.508190,-8.504943,3.151389,2.877283,2.201251,-7.540500,1.301315,-1.841124,-7.172822,-2.701771,-3.415785,6.874179,-9.021906,4.341206,6.387460,6.333840,-8.044832,3.572301,-6.597432,3.269098,-9.127260,0.014461,-1.014939,0.372584,-9.028809,-7.704623,-8.551637,-8.020810,2.193738,-8.805837,1.667948,-5.690670,3.780504,4.567056,-7.996725,9.860298,-6.389532,-9.962844,-9.217080,0.137048,-5.043297,-3.867948,8.087284,6.910914,-2.780210,-6.368719,0.442627,4.419847,-8.367999,-2.176612,-0.135721,0.891439,9.595297,8.420269,-9.511238,-7.789067,-4.291855,8.868318,2.863573,-5.054877,-1.994613,7.099082,7.761234,-5.894582,-5.230828,-3.387248,9.609737,6.431768,9.269696,-1.556295,-7.655387,-9.901980,9.273036,-4.534900,-2.712560,-7.017526,7.731226,-2.375517,3.306046,-2.120262,-7.806205,-1.500289,4.772979,-6.035213,-1.283499,-1.857114,5.473179,1.493695,-0.536126,-2.962535,-8.899212,-7.542192,-0.494958,-1.880761,9.545864,3.579257,9.946600,2.305514,-1.127799,0.659030,9.348837,1.336628,8.702959,1.540353,-6.869193,-4.951189,6.205070,4.712594,-8.153922,0.153548,-9.953842,0.545923,-9.186595,-9.639718,-2.395269,3.365851,5.589914,-9.417385,9.388777,8.163991,1.449880,-7.485042,-6.496693,5.468910,4.896768,-9.232222,8.864737,9.033881,9.125199,-3.823540,4.131374,5.588615,-1.153796,2.158601,2.876491,-7.695529,7.303138,1.068261,-8.119902,-8.528658,4.768034,7.807991,-3.839843,-5.111505,0.450539,8.124488,-1.567531,8.831230,-7.586855,-3.601734,4.915546,6.295339,3.773189,-5.156022,4.938372,1.382809,-1.341522,0.528755,7.098297,-5.749312,2.128116,-2.144736,-2.234336,-4.199691,-1.781783,-0.923076,9.839439,-9.700410,2.259725,-1.476642,8.599753,1.042308,2.647923,-6.438672,3.217312,5.970548,-0.660483,-2.270293,9.107608,-0.874010,-4.749963,-5.255811,-1.458987,-9.777932,1.568934,-6.034047,2.586390,-6.531582,-9.294648,0.767484,0.412473,-4.806904,-9.014606,-4.159289,-7.710047,-5.714347,-4.719594,-5.590819,9.081245,-7.684951,-8.272079,-8.745455,-5.353610,-8.980230,4.105431,-1.976557,-5.526541,6.360644,-9.777171,-3.259876,-7.772982,3.543928,7.624406,5.124281,-8.570885,-9.383916,-3.146088,-4.640976,1.998757,0.165625,2.098081,-4.326780,3.344150,-6.927874,0.142236,-8.332458,7.192424,-3.285499,2.223852,-6.311674,6.940138,-7.315548,7.268271,4.706977,5.962921,8.563926,-4.028044,-5.205628,0.897054,2.666592,-8.909902,-9.413924,4.577453,-5.221106,-0.911260,9.143278,5.371279,7.247780,-8.604503,-9.634783,-7.031357,-8.632850,1.461742,-4.646435,-0.734180,6.173366,5.872804,-4.944911,0.080278,4.412714,3.670598,4.914279,2.766617,1.885378,4.059584,8.133744,-5.509402,1.110632,1.214907,-2.051864,9.265942,-2.263478,-4.008246,-4.753504,6.626838,2.968444,-3.892914,-1.934696,-5.346783,5.022460,8.824730,0.639012,9.620820,0.416607,-7.874374,-8.804215,8.530221,-6.531320,4.267514,5.500107,-7.292082,-8.894293,-2.429323,-0.613053,-1.829923,-9.161446,0.125836,5.585436,-1.943448,1.837365,1.924928,1.112989,-4.868313,-0.541789,-3.183165,-6.990806,-8.785143,2.326835,7.971423,7.424539,6.628108,4.711797,5.309679,6.991247,0.211163,-9.623613,-2.812354,-9.388399,4.924772,3.417469,-1.413562,7.925167,-5.299978,4.995677,-5.516637,5.414619,9.785812,-6.329547,-5.914130,-9.536448,-0.959283,-3.990939,-6.630761,7.530294,9.581962,4.607886,6.954413,-2.094705,8.253332,1.137142,3.829663,-6.782606,-8.266378,5.677678,-4.182293,-1.348979,8.046265,-0.567764,1.124261,2.170588,-8.595384,5.649478,6.872169,3.063638,2.855590,7.133731,3.361230,5.195877,-7.000941,-9.389453,5.629525,-3.912793,8.079141,-0.531488,-6.951869,0.925952,8.988593,-6.368957,8.285813,5.090464,0.125181,7.727924,-9.627488,-8.328958,3.640789,-4.248851,4.428816,0.785546,0.501556,-0.795255,-8.133985,-4.142557,-9.665408,-4.234802,-5.610287,-9.835496,-2.400583,-2.876167,0.382584,-0.889887,-1.287033,9.349663,0.483260,-2.000270,-1.317169,-6.397839,2.368429,-0.924263,-7.226606,7.192842,8.604495,-1.830675,3.643465,-2.023144,7.809676,5.691939,9.563628,3.494276,-0.657605,2.076515,-8.075330,5.422036,-1.634148,2.450854,-1.942532,1.918926,1.565891,-6.589000,4.851799,7.038083,5.976081,-0.293654,3.030395,7.200813,3.300231,-8.830290,-1.829168,9.802621,-2.032108,3.150752,6.681186,-5.855813,-0.805714,0.934752,8.504527,-8.394292,-1.680724,-2.985241,6.304239,8.790812,-5.459512,-0.471499,4.942021,-7.713385,3.629787,-6.615003,-8.513578,1.933415,3.085681,-4.475503,9.315401,3.751274,5.339974,5.063392,1.531731,-8.105650,-7.891245,3.817255,-4.351883,7.858432,8.647769,3.974418,-0.931860,4.956557,9.349406,8.976694,-9.895248,-6.320472,-4.215310,-4.688591,-6.131575,1.174859,-7.435017,-1.066388,-6.066786,-8.805782,-7.931231,-0.694617,-7.704349,-1.980493,7.650755,-6.321861,6.635097,-6.408229,-8.815874,7.200787,6.395109,8.518349,7.291994,-8.315559,-4.580090,-4.948369,-6.826184,7.939393,-9.653069,0.509904,4.103682,5.996519,-2.767808,-7.806056,6.521955,-4.795310,2.410906,-9.434935,9.911417,-0.672475,8.540942,-0.635445,1.800693,-8.756448,-2.072715,-5.754437,4.315766,-2.536546,5.309305,-6.336339,-7.107634,8.539338,-9.574315,7.456509,-0.285341,1.903963,-0.831060,-8.471467,-5.130576,0.596838,-4.332571,-1.066296,7.641704,9.047281,-1.167257,2.768816,-2.723473,-5.808443,-0.898554,3.504974,7.204294,-6.061482,-2.528808,-8.976290,5.012476,3.782720,4.565301,0.077033,-5.913662,7.780630,-7.750816,-7.730723,0.450937,-5.456109,-5.193770,-8.133126,-2.996152,5.211813,0.670133,9.156907,2.394871,-8.970887,1.507614,0.303910,8.380024,-0.713451,-1.073231,-1.031727,8.705196,1.718422,-2.171556,3.656328,5.963372], dtype = "float32")#candidate|6547|(7800,)|const|float32
bop_6548 = relay.bitwise_and(call_6544.astype('int16'), relay.reshape(const_6547.astype('int16'), relay.shape_of(call_6544))) # shape=(7800,)
bop_6551 = relay.bitwise_and(call_6545.astype('int16'), relay.reshape(const_6547.astype('int16'), relay.shape_of(call_6545))) # shape=(7800,)
output = bop_6548
output2 = bop_6551
func_6557 = relay.Function([], output)
mod['func_6557'] = func_6557
mod = relay.transform.InferType()(mod)
output = func_6557()
func_6558 = relay.Function([], output)
mutated_mod['func_6558'] = func_6558
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6572 = relay.const([[[-3.597798,7.838302,-3.338590,1.409866,-5.650423,8.908008],[-6.232980,-2.652975,-0.513193,8.220174,-1.870848,4.850163],[-5.543742,-7.090023,-4.032682,-5.427917,-4.388796,7.341963],[-1.633616,-0.821959,-8.799538,-8.780681,-6.642121,8.670847],[-9.766053,1.562442,-9.098474,-2.621893,-6.744989,3.146837],[2.342384,7.664577,0.091815,-4.133416,-4.690392,8.458280],[-5.455668,5.193898,-9.777761,-2.412457,1.045415,7.156424],[-1.185266,-0.430883,8.120034,2.782357,8.569279,-9.745795],[3.878055,3.547383,0.655233,1.010943,-9.777417,-6.032375],[2.019032,0.236190,-7.874267,-5.386670,2.051985,1.534129],[-5.083489,8.791139,-5.475611,-0.383749,-3.459573,8.707494],[-1.334430,-6.052547,1.208259,-7.094292,0.386600,4.076338]],[[-6.563914,-4.829559,2.759784,-5.232171,8.180957,1.094978],[1.192323,5.993773,6.984829,1.277869,3.208505,-6.114852],[-0.478021,8.160363,8.205518,1.656287,-9.721081,1.713777],[-3.563570,3.662448,3.292868,1.447960,4.144770,-0.795300],[3.301078,-8.538413,5.338893,6.659098,5.009470,9.678711],[4.519675,0.562009,6.886355,5.164949,-1.937597,7.691830],[-9.208693,5.452517,2.966020,-9.097905,3.933404,-6.335268],[-3.878626,1.508422,-8.785492,-7.166077,5.769796,-5.605454],[-3.699523,-9.391107,-2.342414,-8.014564,-1.266700,-4.554984],[6.518404,-3.134037,-7.876750,-2.259033,-2.389113,-8.053746],[-6.055138,9.428747,-3.461214,-2.891540,6.632937,-3.424016],[-6.650647,-4.704998,-8.853359,8.059384,-4.237146,-1.439877]],[[-7.436534,9.413930,-2.776325,8.450304,-1.088407,5.186132],[-7.203896,2.895806,-7.584196,-2.254277,-3.097200,-5.927880],[1.092382,-2.233655,0.792289,-8.465568,4.275806,3.056105],[-9.519108,3.381575,2.293141,9.055017,-5.312680,7.471128],[-4.650095,-6.906672,9.058946,8.146009,-1.578145,-6.478812],[1.438388,0.659459,-4.750417,-3.344272,9.274591,9.118366],[-6.215285,0.691270,3.006649,-6.313209,-4.029253,-0.994935],[0.264097,-3.654985,9.982707,5.802726,-4.847669,-5.378774],[3.437061,6.196838,-7.436210,7.397377,9.354439,0.346627],[-9.357578,2.709778,-0.813170,-7.737642,2.832435,5.815698],[9.367041,4.666041,1.333312,-7.749403,6.952957,-9.057315],[-9.737624,-1.245745,-7.551623,-8.360403,4.144911,7.812238]],[[0.767432,1.893184,-6.359310,2.676970,-1.094090,2.381883],[-4.710206,-1.063981,5.471684,9.763700,9.885666,-7.152762],[-7.992500,-4.229935,-1.971005,2.399829,0.075411,-0.380162],[-6.606740,3.642377,8.274384,-9.634208,-0.413348,9.085539],[2.401783,0.335521,-2.250515,-5.251933,-6.313431,3.906131],[-4.629204,-7.871930,8.282109,-5.169063,-7.618980,-3.320963],[-9.998857,-4.054837,-5.263598,2.142415,-4.663188,-0.186638],[-6.369987,4.251773,1.987819,3.212560,-2.034163,8.866856],[-2.115944,6.477493,5.892174,-0.367932,-0.623147,-0.686578],[-7.637463,5.917731,-4.678289,-2.322378,-0.057640,5.790610],[-2.051465,-4.271502,-8.490214,-6.527737,2.834583,6.179788],[-3.068724,-9.298268,-3.979036,9.970460,-2.756450,-5.432290]],[[-2.046892,1.778194,-0.905642,-3.754077,8.185236,9.002346],[-6.928397,0.388933,2.831544,-3.234025,-8.608157,6.158656],[5.019484,-5.030198,0.505434,-0.488171,9.235245,-7.997905],[-5.502440,-7.767768,5.689032,2.695387,9.732997,9.611391],[7.052754,-1.388703,9.316138,3.660850,-7.284738,-4.191028],[-7.684936,8.236790,4.158105,0.890814,-3.309252,5.148998],[-3.628274,4.406172,8.982064,-1.962699,-2.113025,9.350929],[-8.912549,-5.082970,-7.950799,-2.655128,4.653461,-4.546523],[-4.537515,-4.537869,1.867089,-8.350062,-2.231822,6.503809],[0.742790,1.379071,8.647251,2.773170,8.717858,-7.418376],[-5.437081,-2.375958,5.732235,-5.571649,-5.687800,-4.581512],[7.533383,9.722044,1.399649,0.482828,4.616474,-2.744864]]], dtype = "float32")#candidate|6572|(5, 12, 6)|const|float32
uop_6573 = relay.log2(const_6572.astype('float32')) # shape=(5, 12, 6)
bop_6577 = relay.power(const_6572.astype('float32'), relay.reshape(uop_6573.astype('float32'), relay.shape_of(const_6572))) # shape=(5, 12, 6)
func_2374_call = mod.get_global_var('func_2374')
func_2377_call = mutated_mod.get_global_var('func_2377')
var_6590 = relay.var("var_6590", dtype = "int32", shape = ())#candidate|6590|()|var|int32
call_6589 = func_2374_call(relay.reshape(var_6590.astype('int32'), []))
call_6591 = func_2374_call(relay.reshape(var_6590.astype('int32'), []))
uop_6600 = relay.log(uop_6573.astype('float32')) # shape=(5, 12, 6)
output = relay.Tuple([bop_6577,call_6589,var_6590,uop_6600,])
output2 = relay.Tuple([bop_6577,call_6591,var_6590,uop_6600,])
func_6611 = relay.Function([var_6590,], output)
mod['func_6611'] = func_6611
mod = relay.transform.InferType()(mod)
var_6612 = relay.var("var_6612", dtype = "int32", shape = ())#candidate|6612|()|var|int32
output = func_6611(var_6612)
func_6613 = relay.Function([var_6612], output)
mutated_mod['func_6613'] = func_6613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2804_call = mod.get_global_var('func_2804')
func_2806_call = mutated_mod.get_global_var('func_2806')
call_6681 = relay.TupleGetItem(func_2804_call(), 1)
call_6682 = relay.TupleGetItem(func_2806_call(), 1)
uop_6690 = relay.log2(call_6681.astype('float32')) # shape=(9, 12, 1)
uop_6692 = relay.log2(call_6682.astype('float32')) # shape=(9, 12, 1)
bop_6699 = relay.not_equal(uop_6690.astype('bool'), relay.reshape(call_6681.astype('bool'), relay.shape_of(uop_6690))) # shape=(9, 12, 1)
bop_6702 = relay.not_equal(uop_6692.astype('bool'), relay.reshape(call_6682.astype('bool'), relay.shape_of(uop_6692))) # shape=(9, 12, 1)
func_3266_call = mod.get_global_var('func_3266')
func_3269_call = mutated_mod.get_global_var('func_3269')
var_6707 = relay.var("var_6707", dtype = "float64", shape = (540,))#candidate|6707|(540,)|var|float64
call_6706 = relay.TupleGetItem(func_3266_call(relay.reshape(var_6707.astype('float64'), [540,])), 1)
call_6708 = relay.TupleGetItem(func_3269_call(relay.reshape(var_6707.astype('float64'), [540,])), 1)
bop_6712 = relay.not_equal(uop_6690.astype('bool'), var_6707.astype('bool')) # shape=(9, 12, 540)
bop_6715 = relay.not_equal(uop_6692.astype('bool'), var_6707.astype('bool')) # shape=(9, 12, 540)
func_4877_call = mod.get_global_var('func_4877')
func_4880_call = mutated_mod.get_global_var('func_4880')
var_6726 = relay.var("var_6726", dtype = "float32", shape = (1188,))#candidate|6726|(1188,)|var|float32
call_6725 = relay.TupleGetItem(func_4877_call(relay.reshape(var_6726.astype('float32'), [9, 12, 11]), relay.reshape(var_6726.astype('float32'), [9, 12, 11]), ), 2)
call_6727 = relay.TupleGetItem(func_4880_call(relay.reshape(var_6726.astype('float32'), [9, 12, 11]), relay.reshape(var_6726.astype('float32'), [9, 12, 11]), ), 2)
func_6611_call = mod.get_global_var('func_6611')
func_6613_call = mutated_mod.get_global_var('func_6613')
var_6729 = relay.var("var_6729", dtype = "int32", shape = ())#candidate|6729|()|var|int32
call_6728 = relay.TupleGetItem(func_6611_call(relay.reshape(var_6729.astype('int32'), [])), 3)
call_6730 = relay.TupleGetItem(func_6613_call(relay.reshape(var_6729.astype('int32'), [])), 3)
output = relay.Tuple([bop_6699,call_6706,bop_6712,call_6725,var_6726,call_6728,var_6729,])
output2 = relay.Tuple([bop_6702,call_6708,bop_6715,call_6727,var_6726,call_6730,var_6729,])
func_6732 = relay.Function([var_6707,var_6726,var_6729,], output)
mod['func_6732'] = func_6732
mod = relay.transform.InferType()(mod)
mutated_mod['func_6732'] = func_6732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6732_call = mutated_mod.get_global_var('func_6732')
var_6734 = relay.var("var_6734", dtype = "float64", shape = (540,))#candidate|6734|(540,)|var|float64
var_6735 = relay.var("var_6735", dtype = "float32", shape = (1188,))#candidate|6735|(1188,)|var|float32
var_6736 = relay.var("var_6736", dtype = "int32", shape = ())#candidate|6736|()|var|int32
call_6733 = func_6732_call(var_6734,var_6735,var_6736,)
output = call_6733
func_6737 = relay.Function([var_6734,var_6735,var_6736,], output)
mutated_mod['func_6737'] = func_6737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mod.get_global_var('func_4501')
func_4503_call = mutated_mod.get_global_var('func_4503')
call_6847 = func_4501_call()
call_6848 = func_4501_call()
func_5343_call = mod.get_global_var('func_5343')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_6851 = relay.TupleGetItem(func_5343_call(), 0)
call_6852 = relay.TupleGetItem(func_5344_call(), 0)
func_3766_call = mod.get_global_var('func_3766')
func_3768_call = mutated_mod.get_global_var('func_3768')
call_6857 = func_3766_call()
call_6858 = func_3766_call()
output = relay.Tuple([call_6847,call_6851,call_6857,])
output2 = relay.Tuple([call_6848,call_6852,call_6858,])
func_6861 = relay.Function([], output)
mod['func_6861'] = func_6861
mod = relay.transform.InferType()(mod)
output = func_6861()
func_6862 = relay.Function([], output)
mutated_mod['func_6862'] = func_6862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3700_call = mod.get_global_var('func_3700')
func_3702_call = mutated_mod.get_global_var('func_3702')
call_6866 = func_3700_call()
call_6867 = func_3700_call()
output = relay.Tuple([call_6866,])
output2 = relay.Tuple([call_6867,])
func_6898 = relay.Function([], output)
mod['func_6898'] = func_6898
mod = relay.transform.InferType()(mod)
mutated_mod['func_6898'] = func_6898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6898_call = mutated_mod.get_global_var('func_6898')
call_6899 = func_6898_call()
output = call_6899
func_6900 = relay.Function([], output)
mutated_mod['func_6900'] = func_6900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2472_call = mod.get_global_var('func_2472')
func_2473_call = mutated_mod.get_global_var('func_2473')
call_6971 = relay.TupleGetItem(func_2472_call(), 1)
call_6972 = relay.TupleGetItem(func_2473_call(), 1)
output = relay.Tuple([call_6971,])
output2 = relay.Tuple([call_6972,])
func_6983 = relay.Function([], output)
mod['func_6983'] = func_6983
mod = relay.transform.InferType()(mod)
mutated_mod['func_6983'] = func_6983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6983_call = mutated_mod.get_global_var('func_6983')
call_6984 = func_6983_call()
output = call_6984
func_6985 = relay.Function([], output)
mutated_mod['func_6985'] = func_6985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5576_call = mod.get_global_var('func_5576')
func_5577_call = mutated_mod.get_global_var('func_5577')
call_7045 = relay.TupleGetItem(func_5576_call(), 0)
call_7046 = relay.TupleGetItem(func_5577_call(), 0)
func_5958_call = mod.get_global_var('func_5958')
func_5960_call = mutated_mod.get_global_var('func_5960')
call_7065 = relay.TupleGetItem(func_5958_call(), 1)
call_7066 = relay.TupleGetItem(func_5960_call(), 1)
output = relay.Tuple([call_7045,call_7065,])
output2 = relay.Tuple([call_7046,call_7066,])
func_7067 = relay.Function([], output)
mod['func_7067'] = func_7067
mod = relay.transform.InferType()(mod)
mutated_mod['func_7067'] = func_7067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7067_call = mutated_mod.get_global_var('func_7067')
call_7068 = func_7067_call()
output = call_7068
func_7069 = relay.Function([], output)
mutated_mod['func_7069'] = func_7069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6516_call = mod.get_global_var('func_6516')
func_6518_call = mutated_mod.get_global_var('func_6518')
call_7085 = func_6516_call()
call_7086 = func_6516_call()
output = call_7085
output2 = call_7086
func_7088 = relay.Function([], output)
mod['func_7088'] = func_7088
mod = relay.transform.InferType()(mod)
mutated_mod['func_7088'] = func_7088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7088_call = mutated_mod.get_global_var('func_7088')
call_7089 = func_7088_call()
output = call_7089
func_7090 = relay.Function([], output)
mutated_mod['func_7090'] = func_7090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6557_call = mod.get_global_var('func_6557')
func_6558_call = mutated_mod.get_global_var('func_6558')
call_7096 = func_6557_call()
call_7097 = func_6557_call()
const_7098 = relay.const([5,8,2,-1,8,-5,8,9,-10,-8,9,6,-8,2,-3,3,-4,-9,4,3,9,3,3,-3,-6,-6,9,-3,-8,6,-10,9,-3,10,-8,9,8,7,4,6,1,5,5,6,2,5,2,-6,4,-2,1,-2,-3,-2,-6,-7,2,6,1,-9,3,-5,-9,10,8,-8,1,-8,8,1,10,-1,-3,8,-9,5,4,-9,-2,8,8,9,-7,-4,-8,-9,7,1,-6,-4,-7,-9,10,5,6,1,1,-3,-8,-1,6,-7,9,4,6,-4,-8,5,10,7,-3,-10,-10,-3,4,7,6,-4,1,-2,-8,1,9,2,-3,-7,-7,3,4,8,-1,-9,-10,-4,2,9,4,6,3,5,8,4,-1,-5,-2,2,-9,-2,3,-1,6,7,-9,3,4,7,2,-9,8,-7,-8,-6,9,9,8,6,-9,3,-7,-9,-6,3,10,2,-6,10,9,5,6,7,4,-7,8,1,8,-4,-10,4,-9,-10,7,-10,-6,2,9,-7,5,-5,5,6,-8,10,9,10,2,4,-9,-8,1,8,-1,2,2,9,-3,-1,-9,-9,-6,-8,-8,-10,7,4,9,-8,1,-8,-5,-10,-4,-9,1,1,8,8,2,-5,-7,6,2,-8,-4,-4,5,-9,-5,4,-6,-7,-6,2,-4,-6,-5,9,-8,8,5,-5,8,-3,-2,-2,2,3,-4,-8,2,-9,8,-2,-7,10,-4,4,9,-8,-4,9,10,6,9,-10,7,5,7,2,8,6,1,8,9,10,6,9,-3,10,8,10,1,-1,-3,-4,6,-4,2,-6,-8,2,8,-10,8,-3,-1,-2,-10,-1,-5,-3,7,-10,1,-9,4,5,-5,-3,6,-9,-10,-9,3,3,-7,3,-6,-2,-8,-8,-4,-4,-1,-2,-4,-3,-4,-7,2,-9,6,2,4,3,-3,-4,-5,6,5,2,-2,6,-7,7,10,-8,-7,-2,-4,-2,-7,4,5,7,-9,-9,-6,-9,7,2,-1,8,3,-10,5,4,8,-4,-9,5,2,10,-1,10,-4,-5,-5,4,3,6,6,9,-9,1,6,9,9,5,-10,-8,-7,1,4,-1,1,-6,-9,-5,10,10,1,3,9,-10,10,5,-10,9,-4,-2,8,-2,-1,-9,2,-6,-9,10,6,8,9,3,-2,3,3,-10,1,9,-8,4,6,-10,-10,4,2,2,-5,-1,7,2,-9,-10,4,-4,-6,10,-10,-8,3,-6,3,-8,-5,7,5,10,10,6,-9,-6,-1,-8,9,1,9,-8,-9,3,9,4,7,-10,3,-3,-6,-9,7,8,-5,-7,8,9,4,-9,-1,-9,-8,9,4,-6,-3,7,-2,4,-6,6,-6,1,-8,-5,5,7,-2,5,-10,-6,5,1,-10,9,-5,10,-9,-3,1,-5,-3,-10,-1,-1,-9,2,-4,-3,7,10,6,-3,-1,1,-8,8,9,4,-6,-10,4,9,4,-2,-4,3,2,-5,6,-7,-2,-6,5,-2,-7,-8,-6,-10,-8,1,5,-2,-4,2,-4,-6,3,9,2,-3,-6,9,-5,-2,3,5,-9,-7,-3,-5,-9,3,-1,-4,-6,1,5,3,10,2,-9,1,3,3,8,-3,8,-1,-8,3,9,7,-3,3,-4,-7,4,-2,-8,5,4,-3,3,3,-8,-7,-10,10,-5,-9,1,-3,-5,-4,-10,9,6,-6,7,-2,6,1,-6,-7,3,9,1,-9,-6,9,3,-10,3,9,5,-4,-5,-5,5,1,10,-4,-1,-9,-9,5,-8,2,-10,3,6,-6,-4,1,3,-9,-3,5,-9,5,5,-7,-2,6,2,7,7,-9,4,-10,4,-1,-6,3,3,1,-5,-2,-9,-10,10,-9,3,-7,7,-6,-1,-8,-5,10,8,-7,2,-3,-10,2,-4,-6,-6,-4,4,-4,6,10,2,1,-3,-6,-10,6,3,9,-8,4,9,6,7,8,1,-7,10,-4,6,8,6,5,1,-7,-10,2,9,5,-8,-1,1,-2,6,3,-4,8,-6,-1,7,-3,-9,8,-5,-3,-8,-9,-10,9,7,-8,7,-2,8,-8,-1,6,8,-7,-9,-5,3,-5,7,9,-9,4,4,7,-9,-9,-7,-2,10,-9,10,-5,8,-7,5,-8,4,8,-7,-2,-1,-7,-7,-5,-8,8,-8,10,3,2,5,10,-1,-9,-5,-3,3,7,8,-7,-6,-6,-7,2,-6,-8,4,10,10,4,-8,4,-8,1,2,-6,-4,5,-1,-1,-1,5,1,-3,-5,-6,7,-6,10,-2,-7,1,3,3,2,8,-5,9,2,-6,-10,-10,2,-1,-3,-5,3,2,-1,-9,-10,-4,-4,10,-6,1,-1,-2,-8,5,8,-4,3,9,10,7,-7,-5,-6,4,-3,8,7,7,3,-9,-10,-3,8,9,2,-7,6,7,-9,2,8,-8,-9,4,-6,4,5,-1,9,-2,5,-7,3,3,-9,-8,4,-5,2,7,-2,6,-8,2,-8,-8,6,-5,3,3,-2,10,6,1,7,-5,-10,-6,-7,-8,5,-9,-5,-9,2,-2,-10,10,-10,-3,-2,-5,7,-3,-2,-1,-8,7,5,-2,8,1,6,6,-6,-2,5,-3,9,-9,8,7,10,-7,-1,-6,-3,-1,-10,-5,-5,-7,4,-5,7,-3,5,8,5,-4,8,-7,7,-10,-4,5,3,2,-5,10,2,-6,-5,-4,-2,9,8,-1,-6,2,-7,1,-3,7,1,-8,3,2,8,10,-6,-2,-5,-7,-5,2,8,-1,-6,6,6,-2,10,6,-4,2,5,4,8,-2,-2,6,-8,10,-5,-3,4,9,1,-4,4,-5,-1,-1,-10,-3,-7,-4,-5,-9,5,-1,-7,-3,-10,3,4,-2,-7,-1,8,-1,2,-2,-2,-7,-4,5,1,-10,-6,4,3,2,-3,-6,8,5,-5,-7,9,5,2,-5,-2,3,-9,10,7,9,7,-8,-5,5,2,-10,-5,4,-8,10,3,-10,10,-4,1,6,3,5,9,-9,-3,3,3,-5,6,1,-9,-4,8,-6,3,9,6,-3,3,7,10,-5,-7,4,-6,-5,-5,-3,-6,3,3,-7,-5,5,2,-5,-3,-5,-3,-6,-3,5,9,-2,9,6,7,-10,-4,10,8,-6,8,-3,-2,1,9,5,3,5,-3,5,-4,2,-1,-4,2,2,-1,10,-4,-1,6,-3,3,5,10,-8,7,2,4,1,-6,-5,-7,-2,-7,-8,-9,4,-10,10,10,-6,-7,9,6,9,-2,-1,-1,-2,8,-1,-10,8,5,1,5,-2,-8,6,-10,6,-1,-3,-1,-3,6,5,1,7,1,-1,5,-1,-6,-5,-3,-2,-7,1,1,-9,7,2,-7,-4,-5,7,10,-3,4,-7,-8,-3,2,-4,-7,-10,7,4,1,4,-5,-7,8,3,7,-9,7,-1,6,-3,-8,-9,5,1,-1,1,6,1,8,-6,-4,-10,-6,1,6,-7,7,1,9,-7,9,-6,-7,-8,1,-10,8,-3,10,-6,-7,1,3,7,6,-2,-3,-9,-5,5,-1,-8,-4,-1,6,9,4,-9,-3,-9,-10,3,1,-6,-7,2,-6,6,3,2,-9,-3,10,10,-10,-4,1,-6,7,9,-10,3,9,-4,7,2,-7,-10,10,-4,-8,9,-4,-2,-6,5,9,-2,7,3,-3,1,3,-9,-1,1,9,-1,-6,4,-3,8,8,2,-7,1,-3,8,-6,-9,9,-8,-10,1,-1,10,7,8,7,5,9,1,-10,8,-7,-3,-6,5,10,-4,5,7,-1,9,8,-9,10,9,-1,8,-3,-4,-3,-5,-9,8,-4,-7,-1,-2,-10,6,-2,-4,1,1,-4,-2,-8,-4,9,-10,-8,-5,-3,9,-7,7,-9,4,-2,5,2,7,-6,8,4,6,6,4,-10,5,10,-9,-3,-3,8,5,5,3,-4,5,-8,3,-6,-5,1,-8,-4,-4,-1,-3,2,10,-1,-9,3,-4,-8,-7,3,-5,-4,9,-9,4,-7,1,-7,9,4,-5,-5,-2,-6,-9,2,5,-6,-3,-7,-5,6,-8,-6,2,-6,-9,-6,5,-9,-2,8,-7,4,-9,9,-7,-1,9,-1,-9,10,9,-10,-7,-7,-2,-8,9,-8,-3,2,3,3,1,5,-1,10,10,-4,-1,-9,6,-1,-9,3,10,-4,-9,5,2,-1,-4,5,-5,4,-10,8,-10,2,1,-3,-1,4,-5,3,8,4,-7,9,-8,7,-3,5,-7,3,2,-1,-5,6,-3,-1,3,4,-2,3,3,7,6,-1,9,-2,-2,-6,5,8,1,8,5,-5,4,-9,9,-7,10,-9,-2,1,-2,-2,1,7,-1,7,1,-5,1,4,-1,-4,-8,3,-3,-3,-3,6,-7,9,9,6,-9,5,-4,-9,-9,-10,-7,-7,7,-9,-9,8,7,-3,-3,-6,-9,-2,9,10,6,7,10,8,-7,10,10,-1,-5,-3,5,-9,-2,7,-4,-1,6,-6,3,-8,10,6,5,-9,4,-9,3,3,-10,-7,9,5,-8,-4,6,3,9,8,-7,-4,-10,1,-2,-9,5,7,5,-9,-4,6,-6,-9,-8,-1,-5,7,-8,9,3,2,-7,9,-10,7,-3,7,-3,4,-3,-8,10,6,-6,-9,4,-4,-10,-4,-3,-6,5,-8,2,-10,7,-5,-5,-6,-5,-7,-6,-1,6,-7,-8,7,-10,4,7,9,3,-10,5,9,-10,-1,1,-3,9,8,-6,-3,-2,-8,-2,-4,3,7,-1,-9,5,7,4,-5,-1,2,-9,-6,3,-3,-3,4,-2,-3,7,2,-4,10,-1,2,-7,1,-1,-1,1,1,-1,-9,4,-4,5,-5,-6,-6,-9,1,3,3,9,6,8,-3,2,9,-5,7,10,-9,-6,-5,3,10,-8,-10,9,-4,-5,3,2,-3,5,-8,-1,-1,-4,-1,-10,3,-6,-2,10,9,6,3,3,4,-4,-3,1,-2,-8,-2,-4,8,-9,-4,-8,-4,-6,-2,-1,-9,1,9,-5,5,-4,4,1,9,-2,-8,-7,-9,-7,3,9,2,3,-10,-4,2,1,7,7,1,-10,-4,-9,-1,-3,-4,-6,10,8,8,4,-2,-5,6,-7,-1,-4,-8,-7,-9,5,3,-10,3,-5,-1,-10,-2,4,-6,5,-9,-4,1,-8,-4,-4,8,-9,1,3,-3,-5,-9,4,-9,5,-9,-7,-2,3,-1,2,2,-10,7,6,-8,6,-9,5,1,-10,-10,-9,3,8,-10,1,2,-4,7,-1,-3,4,-7,-2,10,-7,8,-1,-9,-4,9,-10,9,2,-7,4,-7,-2,9,3,7,-8,-7,9,-9,-6,10,-7,-3,6,-1,-10,1,5,7,9,-9,2,-9,-5,-3,5,10,-2,-3,2,1,4,-3,3,-8,-7,-3,-4,-9,-9,1,-4,7,3,6,-4,7,-10,5,-4,6,-10,10,1,5,2,3,-7,5,10,7,-8,-10,-7,-2,9,-2,-8,3,4,9,-3,5,5,-2,-1,7,-3,8,3,3,-7,-1,1,-4,3,2,-8,-8,5,7,8,5,-2,-3,10,-9,3,2,5,9,-9,-5,-6,-1,-2,-8,4,-10,-6,-3,1,5,-3,7,3,5,-7,-1,1,7,-10,-4,10,-1,8,-5,8,-2,7,9,7,5,4,8,-8,1,-2,2,-8,8,-9,-5,-3,9,8,3,2,1,4,5,8,9,10,2,6,-6,-3,3,-9,9,10,5,9,-2,-9,4,1,-5,-7,-1,-7,10,-9,9,5,7,9,9,-10,-1,-6,-6,10,-9,8,-2,8,-6,-2,7,2,-3,8,1,5,-8,-6,-9,6,5,-10,9,-6,-7,10,8,-9,-5,6,-6,-7,-1,9,-1,-8,8,-3,7,4,10,9,-7,10,5,7,5,10,-7,6,5,-4,3,10,9,-8,-7,6,5,-6,-1,6,7,4,2,-3,7,9,-7,1,-4,-4,6,-7,-5,3,-5,6,2,9,-1,2,2,-9,2,-4,1,-7,7,7,-6,1,-7,5,-6,-3,7,-8,-5,-9,-7,3,-10,-2,-4,-10,-7,-2,-8,4,-3,3,-10,-8,-8,-4,-9,-2,9,7,-2,4,8,6,4,9,6,-7,5,-3,-4,7,-6,-2,2,8,6,5,-7,9,-2,-9,10,-5,1,7,9,-9,-10,9,2,-6,-9,-4,4,6,-10,4,-10,7,9,7,6,2,-6,-8,8,7,-6,2,4,4,4,6,-9,5,4,5,-7,8,9,10,-1,-5,-7,7,-8,5,-10,-7,-3,6,-6,9,-9,-5,-4,-6,-3,4,-7,-1,-3,-6,-9,-2,5,10,-1,5,8,6,4,-7,-2,-6,3,3,-6,-8,10,-7,-10,-8,-8,8,-2,7,8,-2,-6,-9,-8,6,-1,-8,6,8,4,6,-9,-7,-1,-7,-8,-1,-9,-3,3,10,-4,5,-6,8,10,-2,-10,-2,-3,2,-9,-6,-3,7,8,10,-10,4,9,-5,-5,10,8,-6,2,-10,3,1,-5,-4,8,9,-10,-3,6,-9,-7,-8,-2,5,4,-5,3,3,-8,5,10,5,6,10,-8,-2,-10,1,5,-6,-5,-6,-8,-8,-5,-4,6,6,7,-1,6,9,4,-8,10,-7,-6,3,1,2,-4,-10,4,-10,1,6,-7,-3,-7,-7,8,1,-7,10,6,2,8,10,-8,-5,-6,-6,7,1,4,-2,5,4,6,10,8,3,5,-2,-6,2,9,4,-9,2,6,-6,5,-3,-6,4,6,-1,-1,-4,9,10,7,-4,10,2,9,-6,-7,-7,9,-8,7,6,2,4,9,9,-7,-2,8,2,1,-4,-5,5,10,-1,-5,-2,8,-8,9,2,-2,-2,8,10,10,-10,-2,-10,-10,-9,7,-2,9,-3,9,2,-10,2,8,9,-3,-2,-6,9,-3,-9,-10,-7,-10,7,6,9,-6,3,-2,-2,3,-1,-6,3,9,-2,-2,9,-1,-1,6,2,10,5,-10,-8,1,-10,-10,-8,6,9,3,1,-4,9,-2,-3,-6,4,-3,9,-2,3,-3,-10,-5,8,-6,-9,1,2,1,-6,4,-3,2,3,2,-3,-8,-7,-3,10,3,-2,9,8,9,-7,1,10,-3,-5,-8,1,3,-1,-2,-8,10,1,-3,-7,10,5,-5,7,9,-4,-2,5,2,4,6,-1,1,6,-9,-8,9,2,-10,2,3,-8,-3,-2,8,-9,9,1,-1,6,9,1,-5,4,4,-7,-3,3,8,9,3,-2,-9,4,1,-2,-2,-2,9,-4,-1,-9,-6,8,-10,-1,8,-5,10,9,-7,-4,5,6,10,-7,1,-5,10,10,-4,-3,6,-1,7,-8,10,-3,-7,-9,1,10,-3,8,10,-3,8,-7,4,-9,-8,5,-8,-5,9,2,9,1,-6,-7,-6,-3,4,9,9,-9,4,5,10,6,3,9,-1,5,-9,6,-1,-2,-10,-5,10,4,-7,7,-10,-9,3,6,-8,3,-3,3,-9,-3,5,-6,3,8,-10,7,7,4,2,6,-10,7,2,-7,6,-10,9,5,-9,-10,-9,-10,3,-8,1,-6,7,-4,5,9,-3,-2,8,-4,4,7,-1,10,8,-2,6,-2,3,-1,9,-10,3,-5,-3,8,-3,9,-10,1,-8,1,-10,6,-8,4,7,2,-7,-10,5,8,-3,-3,7,-2,-4,-1,-5,2,4,-3,-9,2,1,10,10,-4,-6,-5,-1,-10,-10,-1,-9,-10,-8,-5,-7,7,-9,-4,5,-1,4,-6,4,10,-8,-1,-6,10,-4,-5,2,-9,-8,-9,10,6,7,-1,-7,-7,3,-1,-8,7,8,5,3,-10,-6,6,10,-3,3,5,4,4,-9,8,-6,1,6,-3,-1,-4,3,-6,3,7,1,3,-6,-3,-1,-4,8,10,-3,-7,-7,3,10,-2,-7,6,-3,-3,7,3,9,-5,-5,2,-10,-2,9,-9,-5,1,-10,-9,-9,1,2,-6,-3,9,7,-6,2,6,-3,2,5,-7,-4,7,3,-9,-6,-6,-7,-7,-8,-3,-10,6,5,-1,-3,5,-9,9,4,6,5,9,7,-4,10,9,-10,7,-3,6,-9,1,7,9,-10,-9,5,4,-7,-10,8,1,2,-3,-6,-1,2,-10,-2,10,4,-4,9,-2,6,5,1,4,-2,8,-8,3,-1,-10,-4,4,10,-6,5,5,-9,-9,-6,4,2,6,-3,1,-3,-6,9,-4,7,8,-7,-5,-5,9,-9,-9,-6,-10,-7,-2,10,-7,9,10,3,-10,-4,9,1,-1,2,9,9,7,-10,6,9,1,-7,4,8,2,-10,1,10,10,-4,-10,-10,-8,-7,10,-10,-6,1,-8,-5,-1,3,6,4,7,-7,-2,3,-9,6,8,10,6,-5,10,-5,5,-3,-3,-9,8,7,-6,1,3,-5,-5,7,8,-6,-4,-9,10,1,2,6,-7,9,-3,7,10,-7,10,-8,7,-7,6,-9,-10,2,10,2,-10,9,3,-9,1,-10,1,-7,2,9,-10,4,1,-3,-5,8,-8,-9,4,-4,6,-6,-3,-7,-7,-3,-7,8,-5,8,-8,5,5,6,2,4,5,-6,3,3,10,-8,5,2,6,9,-6,9,6,1,-5,-7,7,1,5,-9,-2,-1,-2,6,-2,-4,-7,2,-8,3,-9,8,-4,-5,2,5,10,8,8,4,9,2,2,-1,-6,6,9,-1,-2,1,10,-8,1,-6,2,-10,-7,8,6,-10,8,-8,-1,-7,5,8,5,8,4,4,4,-8,8,-2,7,-7,-9,9,1,-2,-5,2,8,5,-7,-9,-7,-4,5,9,8,-5,10,9,-2,-10,3,9,5,3,-5,3,-1,6,2,6,-3,9,6,7,-10,7,2,-3,1,8,-8,5,7,5,-7,3,3,3,1,9,8,5,3,-4,-3,8,3,-3,7,2,-9,3,-9,1,-6,-1,6,4,-3,-4,3,2,-7,6,2,-7,-5,3,9,-3,-4,-1,2,10,6,-4,7,-4,-10,8,10,-3,8,-8,9,1,-10,6,8,7,-1,2,6,2,-6,-8,-8,1,8,-2,-3,-4,7,-4,5,10,4,-4,8,6,8,8,8,3,-9,7,-2,-6,9,4,1,10,6,6,9,5,8,5,-5,4,-7,-7,-9,8,10,2,7,-9,-7,6,8,5,-7,4,3,7,6,-9,-6,5,-8,-9,10,-8,2,-4,7,8,2,-7,9,-4,-7,-2,-9,-9,3,-2,6,1,-5,-10,-6,8,10,4,-1,-4,1,-1,2,-7,-10,1,10,5,7,-2,6,3,-7,-7,3,-7,9,5,10,8,1,-5,1,10,5,-3,2,-9,2,7,9,-2,-6,10,8,-5,7,-4,7,-8,-4,5,6,-6,10,-4,1,-7,-2,2,-5,3,-4,2,-8,8,-3,1,7,-6,3,3,-7,-1,-7,10,-10,8,7,7,-2,1,-8,-3,-10,-9,2,-6,-2,7,-2,3,-10,-3,-1,-4,5,-6,-8,5,1,-2,8,9,7,-1,-3,-8,-7,1,3,-3,-3,-3,-10,-10,4,2,-1,4,-9,6,3,-6,-7,10,-6,-10,2,1,-2,2,4,10,9,3,8,9,-5,2,5,4,3,-10,9,-8,2,-9,-6,-4,-2,10,-8,1,-7,7,-5,1,7,4,3,-9,1,-3,-6,1,-6,7,-1,9,-3,10,-1,9,-4,-6,-6,4,-2,4,4,5,8,5,-2,9,-5,5,-2,4,9,5,-6,1,-5,-7,2,-10,5,10,-2,-7,8,10,6,7,7,-1,10,10,-8,-4,-2,3,-2,7,3,-10,5,2,6,-9,3,6,3,-7,-7,-3,5,-6,-10,10,8,6,-10,7,10,-10,7,4,-6,-10,2,-1,1,6,2,-7,-6,6,-1,-5,-2,-4,3,-6,9,-3,1,-1,-1,6,-5,-8,3,-8,-8,7,-7,8,9,10,-1,-10,-5,5,-8,-3,-1,3,-4,10,3,3,-8,-2,4,4,5,6,-5,-9,-9,7,3,5,10,-1,-5,-4,3,8,8,-3,-6,-4,-9,5,3,-9,9,-4,-3,3,-7,-9,-3,-10,-8,3,-1,4,-7,-9,10,-7,-3,-9,5,-4,-9,5,-9,2,-7,1,9,7,4,-8,-3,5,-7,-4,-8,-7,1,-8,6,-6,-4,-8,-2,-1,-10,-3,6,-10,-2,-5,3,7,3,-4,5,1,-7,-2,-5,-7,4,7,8,2,4,-10,1,-2,-1,5,-6,-3,9,-6,-10,9,-3,-3,8,10,-5,10,6,-2,8,-4,8,-1,-5,-3,-10,-9,1,-3,-5,10,5,-8,1,9,1,-6,-3,8,-2,2,-3,4,-1,4,3,-10,1,-9,-9,-2,4,-1,-4,4,10,-9,-9,9,-3,-7,-7,3,4,2,2,4,-3,2,6,5,-6,-10,-9,-4,-4,-9,8,10,-5,7,-8,3,8,1,3,-9,-2,1,-10,6,-6,4,6,-9,-8,-8,7,-8,-7,10,-4,-7,10,8,5,-3,-8,8,-4,-6,-1,-9,-6,-5,5,-2,-6,5,-9,5,8,6,6,-1,8,3,2,10,-10,-10,2,-3,-1,2,5,5,-5,9,-6,4,-10,5,-8,9,-2,2,-10,-10,-7,-2,-10,-4,-9,-8,5,-9,8,6,-9,-3,-5,4,-2,-6,-9,-1,-7,-3,10,-9,3,2,4,-7,-5,5,-5,-5,3,6,-2,-10,2,5,-7,8,4,1,-8,-10,-9,4,4,-3,-3,-1,-7,-5,-8,-2,-5,-5,10,9,-4,-2,-6,7,6,-8,-10,-5,2,6,8,-5,10,-6,-5,10,-5,-2,-1,-10,-10,7,9,-9,-9,1,4,-4,5,5,-4,1,1,10,-4,-10,-9,6,-8,9,9,7,-7,10,-1,-5,-1,-6,-10,6,-7,8,-5,5,9,-1,5,4,10,-7,-8,-8,7,-5,10,-10,-8,-2,3,6,-1,-2,8,-2,1,-9,-2,-2,-1,-5,-8,8,3,1,-7,-10,8,9,-2,-4,10,4,10,-10,-2,-4,2,-6,-3,-1,-6,1,2,9,10,-7,-7,-2,-8,10,9,-2,-7,6,-7,-10,-7,-6,2,-5,7,5,-4,10,1,-5,5,5,-6,-10,7,4,1,-7,3,7,3,-3,1,2,-5,-6,2,10,10,1,-10,-5,4,5,-1,1,-6,-2,10,-9,-1,-3,4,-1,3,-6,-6,3,-1,1,-3,-8,7,-6,-6,-1,-1,9,10,-4,1,-6,-10,-9,9,5,-4,-3,-4,9,-5,6,5,-5,-3,-7,-8,-1,2,-9,2,5,8,-7,8,-2,-4,-10,2,-3,-4,-1,-3,-1,2,8,-6,8,-10,6,-8,-2,7,-3,-7,5,-9,4,-9,-9,-4,5,-9,-2,9,-8,6,-1,-1,-3,-3,10,5,5,8,6,-8,-10,5,7,-1,3,4,2,8,-4,4,-4,9,-4,3,6,5,8,1,-6,-10,-2,2,-2,7,-3,1,3,-7,6,9,1,10,-3,-7,-3,-7,5,-9,10,-2,-9,10,-4,9,9,2,3,1,4,7,7,4,-5,-9,-9,10,6,1,9,10,9,7,-7,-10,-6,-10,-2,7,7,2,6,5,-2,-4,8,8,-9,9,-3,6,-7,6,-3,7,-6,-8,-1,-6,1,5,-5,7,9,-9,5,6,6,-1,3,-10,7,3,3,4,-9,-1,3,8,4,-6,5,-2,4,-9,-1,5,-7,9,-8,-3,-1,3,4,8,3,8,-8,8,-4,-8,-7,5,1,-3,-7,10,-3,-4,6,-5,-9,-6,5,-8,4,6,-9,7,-6,-1,-7,3,-5,6,-10,-10,-4,-6,4,-10,10,-2,-6,8,-9,5,1,-7,6,8,4,6,8,-9,-6,3,-2,6,3,-1,5,10,5,-2,1,-6,-10,5,4,10,-2,7,-9,-5,7,7,-4,-7,6,-10,1,-4,-6,-7,-4,2,2,-1,2,-3,3,-10,7,-6,1,10,1,1,4,10,6,5,1,9,3,4,-2,-3,-4,-1,-6,-4,-6,6,2,-9,10,-6,-1,6,-7,-2,-3,-7,5,-3,-9,-1,4,5,5,-6,-8,-6,7,5,-10,-10,-1,3,5,10,-5,-10,-8,6,-1,-8,5,9,8,6,10,-5,5,8,6,-3,-9,-1,-8,-10,-1,9,6,10,2,4,-3,5,-8,7,1,4,-5,-6,-4,-1,7,-1,-9,-7,-8,-3,9,-1,10,-9,-8,-8,-10,5,1,8,-9,8,-1,-7,5,2,-9,-9,10,8,4,2,-2,-7,6,-10,-4,3,5,-6,1,4,-2,-6,4,-4,-2,2,5,9,-3,-8,-1,-4,-10,-9,-8,-10,-8,5,-10,10,-5,-10,-2,-6,9,-3,5,-9,6,8,2,6,-4,-4,10,-8,8,9,-6,4,9,10,-3,-10,8,4,-4,10,3,-2,-9,2,-8,-5,4,-4,5,6,2,8,2,9,-4,3,4,4,6,1,5,-10,5,9,-7,-9,-10,8,9,-7,-6,-2,-6,6,-10,-9,4,3,3,-1,-8,-9,7,10,5,-1,-10,3,-9,9,7,4,7,-1,1,3,2,8,1,7,5,-9,1,10,-1,1,9,9,5,10,-10,5,-7,3,-1,6,-10,-9,-6,-3,2,-7,3,6,-4,4,-1,7,-2,-8,3,-8,-6,4,-10,1,2,10,3,-3,-4,2,8,1,-10,-4,2,5,-1,-2,-5,10,2,-3,7,2,3,-5,3,-2,7,-7,-7,9,-1,-8,5,-4,-9,-1,-2,-6,-7,5,-6,-5,4,4,-2,1,3,10,9,-4,-10,3,-8,-7,9,-6,-9,-10,3,-6,6,-8,7,6,1,-4,-4,3,5,10,-1,3,-7,5,-8,5,-8,-2,1,1,-7,-5,2,-7,-7,3,3,-2,-8,8,-7,7,-6,-10,-6,-10,-6,7,2,-2,-1,9,-10,4,-7,1,7,-7,8,9,8,10,4,-9,1,5,8,-6,6,-4,2,5,5,2,1,9,3,-3,-7,3,-4,10,4,-2,-5,3,4,-7,-2,-4,10,-2,3,10,-8,7,-1,5,2,8,-4,5,9,-8,-10,-5,6,-5,-5,-10,-6,-6,-4,4,8,3,1,1,1,2,-2,4,-6,-8,2,3,-4,6,-10,4,-10,-2,-9,2,2,1,-3,-1,-4,10,-6,-5,-4,8,9,1,-3,10,-6,1,-6,-4,-9,-8,4,10,-2,2,-4,-9,-4,-4,-5,-8,7,-1,-4,-4,9,-8,1,-7,-5,-1,9,3,2,10,-2,-10,-10,5,-5,-8,2,-1,6,-10,-7,1,2,-9,3,-10,2,5,-1,5,-1,2,9,-10,1,9,10,-4,-5,-7,-4,3,-8,-7,9,7,-3,5,2,10,-5,1,-8,-10,-8,9,-5,-10,-3,2,-9,3,-7,5,-4,-5,3,-8,3,-1,-6,-4,5,2,3,9,10,-3,2,10,-2,-7,-3,3,5,-6,4,-10,6,-6,-5,-8,-9,-3,8,7,10,-4,-10,-8,10,-6,6,5,9,10,8,-10,-8,8,-8,-5,-10,1,3,-7,-5,-9,-10,-2,6,2,9,-1,-4,-2,-3,-1,3,4,-3,-1,5,-1,2,5,-5,-4,-10,-9,3,9,8,8,5,-9,5,9,8,7,3,-2,1,-1,10,-7,3,8,7,-5,9,1,2,4,-9,-3,-2,-1,10,4,-3,-2,7,10,-7,-6,-8,2,10,1,-6,-4,-9,3,-6,-9,10,-7,-3,-2,-1,9,-7,1,-7,-9,-9,5,-5,-9,-7,-1,-2,-5,7,-5,6,-10,-5,2,-5,6,3,2,-2,-10,9,-6,-2,-6,-8,7,-5,9,-10,-1,-2,-7,-10,3,-1,-1,-6,3,-7,7,10,-1,3,-6,-3,-7,5,9,4,5,7,-6,-2,1,8,7,1,4,10,-8,6,-7,9,4,8,-7,-5,5,9,-9,3,-4,5,-2,-7,-7,4,-2,10,6,-7,-10,-5,-10,-3,3,6,-4,-7,-6,-5,-7,-9,-3,7,4,4,8,10,-6,-8,3,-8,5,-3,10,-5,10,10,-10,3,-2,-9,6,8,-4,-1,-10,-6,-4,5,-9,-3,-6,-10,-9,-10,2,1,1,-2,-6,2,1,3,6,-9,10,-2,4,-3,-9,-4,-4,-2,4,10,6,8,-1,-3,8,-2,4,5,9,9,-2,-10,-7,1,-8,-3,-2,-2,-3,10,4,2,-7,4,-6,4,7,6,8,-5,-8,-1,-1,-3,-5,-6,4,-7,-6,7,-5,1,6,-5,-5,-1,1,3,-2,-8,1,5,1,-6,-4,-8,3,10,7,4,-10,-6,6,4,-8,-4,-6,6,-3,-6,-5,-6,4,-8,3,-4,6,5,1,-9,-4,10,3,9,6,3,-8,2,4,4,1,-4,9,-8,-1,-9,-1,4,3,-2,-7,-4,3,-10,5,8,-1,4,2,-10,10,-7,-6,-9,-4,-10,7,9,-10,-8,-2,-3,-9,-3,-3,-1,2,-6,-8,-9,-7,5,-5,-3,-3,9,7,8,-3,6,-6,8,4,-6,10,-9,6,-10,-10,5,-4,-9,-8,-7,-8,6,-10,1,10,-10,-3,-9,5,-10,-10,8,-9,7,2,10,-8,5,3,-4,3,5,-3,7,-2,2,-1,-8,-7,-10,10,10,-6,-6,1,4,-3,2,-1,-3,7,7,-6,-8,1,-2,10,6,9,7,-1,-5,-9,-10,7,5,9,-4,8,-5,-2,9,1,7,7,-9,6,3,-1,6,-6,-4,5,-7,-1,-2,-1,4,6,1,5,4,-4,-7,-9,4,5,10,7,-3,-2,-1,5,5,7,9,-6,5,1,4,4,7,10,-9,5,-5,-6,9,2,-7,2,2,2,-7,-9,4,2,3,9,1,6,10,-4,5,7,-6,-1,-6,-6,-5,7,-8,-3,1,5,-7,-7,2,9,9,3,-2,4,7,-4,-6,-4,-10,-7,10,-4,-2,-5,4,6,-8,1,-3,-2,6,5,-5,-8,5,-7,-7,3,3,6,1,-3,10,1,-10,4,-6,-9,7,9,3,8,-8,1,-10,-1,10,-10,-7,-4,3,-2,-6,-4,-8,-6,1,-1,6,2,-9,-6,6,-9,-6,-9,-10,2,4,2,8,-3,3,-10,5,4,-5,-5,6,-4,-7,-3,-6,7,-10,-3,7,9,-3,-9,-1,4,-5,6,5,6,-5,-2,-6,2,-8,-6,5,4,-4,-6,-10,-10,-3,6,8,-9,3,-3,-10,4,-4,-2,-6,6,-1,-7,-7,4,7,6,-4,-8,8,-7,-8,6,-3,-10,-5,1,1,7,-8,5,-2,9,-10,4,-8,-10,-4,-10,-7,6,-9,9,6,7,6,-9,7,-6,-5,-6,-3,-1,3,4,2,-3,8,10,-6,9,-10,-2,-6,-3,1,6,-6,-1,-8,8,-6,2,10,1,10,-2,8,-5,-2,-5,-8,7,8,2,6,8,10,7,4,8,7,4,3,2,-10,10,-8,1,-8,3,-10,5,3,-9,-9,-2,-8,6,10,9,-4,7,8,9,-8,8,-5,9,5,6,-7,-4,7,-8,-5,6,-6,5,-8,9,-9,7,10,-4,3,2,-10,-7,-6,5,-4,5,3,-5,4,-8,-1,-7,-8,9,-4,-3,9,3,-9,-9,9,-4,-1,3,2,-8,-6,-7,9,8,-9,8,-5,5,9,-6,9,-9,6,6,3,3,1,6,6,-3,-6,-4,10,-4,3,-7,7,-3,-8,-3,4,-10,7,-7,9,1,9,-8,-3,9,-2,10,-2,4,-3,9,-6,4,-7,8,1,1,5,2,-4,5,5,5,8,7,8,-9,-7,8,6,-9,-7,8,2,9,-10,1,-10,5,6,7,8,-8,9,-8,-6,-3,-9,-5,2,8,10,9,6,8,-6,5,3,10,3,-8,-6,2,-3,-8,-2,-8,4,2,1,-1,5,10,1,-9,-7,1,-7,9,-1,4,3,-4,9,-8,-6,-7,5,6,-7,-10,1,8,-6,7,-5,-1,-2,7,10,2,-4,-6,4,7,-6,-8,2,-8,-4,-8,-5,1,-3,-1,-6,9,-9,1,7,-7,-6,-4,10,7,-5,6,3,1,6,8,-2,1,2,-7,1,1,-8,6,-5,5,-9,3,-8,7,-4,-7,-10,10,-10,10,-10,9,-6,-9,9,4,-4,-9,1,8,8,4,4,1,-8,7,4,7,2,-4,9,-8,-4,7,2,-1,-3,-2,8,2,4,5,7,9,-7,10,-10,-8,7,10,-1,2,7,-10,7,10,-1,-1,-4,-8,5,6,8,10,9,7,-10,-3,-2,1,-7,3,5,-8,6,1,-4,7,-10,9,6,9,-4,-2,-9,8,-3,4,4,-6,-8,4,-1,-5,-7,-10,10,-8,6,-3,-2,-9,-9,-10,6,5,-2,-7,-9,5,9,-6,7,-5,3,-5,6,-9,-10,-10,-6,10,4,-10,10,-7,-1,9,-7,10,-2,-7,3,-3,-7,-7,8,9,-5,-2,-6,-5,4,-4,10,-2,-3,9,5,6,7,-4,-3,6,4,4,-9,-5,-6,-3,-5,7,6,-3,-9,4,4,-2,1,-6,8,-2,-2,-1,8,-5,10,2,-7,8,5,6,10,-8,-8,3,-6,-4,-2,7,10,4,3,6,10,-9,-8,4,-3,-6,-7,-6,1,-1,8,4,1,7,-1,-3,-9,-6,7,2,2,-10,6,-4,-7,-2,7,2,2,-2,-2,-8,9,-7,-5,4,-6,10,10,9,-1,4,-6,5,-6,5,-2,-1,6,-5,7,-10,-6,3,4,-5,2,2,8,8,-4,3,3,-7,2,-1,3,-9,2,5,5,-1,-1,-7,-2,-4,7,2,-1,-10,-1,9,-4,5,2,2,-1,-4,-9,5,5,6,7,3,-7,3,6,5,10,-6,1,-8,4,-9,5,2,3,4,-8,-10,-2,6,-4,-7,-3,7,-2,8,-8,-7,-1,3,-9,-6,3,-3,-8,2,1,8,-2,-8,1,8,-3,4,-4,-9,-3,-1,2,1,6,-4,3,-9,-9,9,2,-1,4,8,10,2,-4,-2,-10,6,6,-1,2,-6,-8,10,4,-5,-5,-6,-10,-2,5,1,-7,-1,7,-4,3,-1,-6,-1,2,-9,-8,-4,7,-5,10,-8,-2,-9,-3,9,4,-9,1,-1,5,-10,6,1,1,-6,1,7,-2,-4,9,3,3,4,-9,7,-4,6,2,-3,-5,-4,-2,-2,7,-1,9,-2,3,6,-10,7,9,-5,-3,4,7,6,8,6,-6,-2,1,7,9,-8,-6,4,-8,-6,9,-9,-9,8,3,-1,-10,-3,-6,-5,-4,5,-5,5,7,-6,-3,-3,-10,-10,-4,3,5,-5,8,7,2,-2,-10,-2,-10,3,3,-8,8,5,10,-8,-6,7,4,6,5,-4,-6,-1,-5,2,2,-1,1,-6,6,7,8,5,-7,7,10,-4,-8,-5,-9,10,-8,-4,9,-9,4,8,-9,4,-4,7,-4,10,-7,-4,-3,-8,7,9,3,-10,5,9,-1,-1,5,10,-10,1,5,-2,10,-1,-5,3,-10,5,3,1,-8,-10,10,-2,10,6,9,-6,-1,7,7,3,7,5,1,-3,-8,-2,10,-1,-5,8,6,-4,8,2,-3,5,3,9,7,3,-2,-6,-6,3,-3,-7,4,7,-5,9,5,8,-5,-2,-7,-8,7,-1,10,-6,6,3,7,2,-8,-7,-7,1,-2,-2,7,7,-3,-8,-4,-5,10,-10,7,-8,-5,10,-2,1,5,2,-5,-7,-9,1,-3,-6,4,9,-10,-6,4,6,-6,-9,-2,4,-9,-6,-8,-4,5,4,-7,-3,-2,1,-7,-3,4,6,2,-1,-3,-1,-6,-1,-4,2,-2,8,6,-1,6,7,-5,-8,-5,7,-8,6,-1,6,-6,7,-5,-1,6,-3,-3,4,5,4,-3,-5,-9,-4,2,8,-8,3,1,4,5,2,10,-5,-2,-7,9,-3,-5,-9,-8,-4,-3,10,2,-3,-3,-4,-5,-2,-9,1,10,-6,-2,3,-1,6,5,-10,-2,-3,-2,-10,7,5,10,4,9,-7,3,8,-1,2,10,5,8,7,-7,8,-10,10,8,-3,1,5,2,-2,10,8,-7,-2,-1,5,-9,-1,-6,2,-4,1,5,-3,-1,-9,-10,-1,-10,-2,-5,10,-1,-4,4,3,8,-5,-9,-9,5,3,5,-2,8,-7,-10,6,7,-10,-5,1,6,8,4,8,-5,5,-5,-8,-1,-6,1,-4,-4,-1,7,4,-8,9,-8,-3,7,5,-5,5,-8,-6,-2,1,-7,5,-6,7,1,-8,-6,4,-9,7,1,-7,-2,-2,-5,10,-7,6,-6,-7,-1,-6,8,-10,8,-10,-9,10,1,-8,4,10,5,-5,1,5,-9,-8,-10,3,-8,-7,-1,10,8,10,-6,-1,8,-9,8,-10,-7,-5,1,-3,10,-5,6,4,-1,-5,-7,-5,2,6,10,-8,-6,-1,10,3,-3,-2,-4,-2,3,4,-4,8,5,-10,10,3,3,-3,10,-5,-6,4,7,7,-3,-3,9,5,-3,-10,-2,-1,7,-10,-9,9,-5,-7,9,2,6,1,7,3,10,5,6,-9,-9,9,-5,5,-3,10,-10,-6,-10,-6,-2,8,-10,-5,10,-1,-4,-7,1,9,-8,-8,3,-7,-8,1,1,3,4,-10,-4,1,1,7,4,6,4,2,-7,-2,3,-6,-3,-6,6,1,-4,8,-2,9,-10,10,10,-3,3,1,-1,10,3,10,1,9,-4,3,3,-4,7,-9,7,2,-9,6,10,-3,4,-4,7,-10,-10,8,5,8,-9,-8,1,6,5,-10,-10,9,8,-8,-7,-7,1,2,-9,-7,9,5,-7,10,5,-10,4,-8,5,9,-4,10,-2,-1,-5,1,6,-4,7,9,-5,-8,8,-3,-1,4,-9,-1,9,3,-2,7,-2,-3,2,-2,10,-8,-5,-1,1,2,-2,-2,4,-4,-10,4,-10,3,-6,-1,-5,7,7,-6,5,-2,-2,-7,-8,3,-2,1,4,5,1,8,-4,5,3,4,3,5,8,2,-1,-7,-3,-4,-4,-1,-5,-10,6,-2,9,6,-10,5,-1,6,-5,-6,1,7,8,-10,-9,-4,6,-1,-10,4,8,-7,-8,10,4,-2,-5,-10,-9,8,1,-2,-7,-9,-1,-6,2,-7,-4,4,4,-5,-6,-4,7,2,5,4,-6,9,-8,6,8,-2,10,-4,-3,3,-4,-2,-10,-1,-10,-9,10,4,6,-7,5,1,-7,-10,-2,8,2,8,-8,-1,4,5,-1,-1,10,1,7,-1,-7,-5,-5,-6,4,-1,5,-9,3,2,-2,10,10,7,3,4,-10,10,1,-4,-2,-5,8,-7,-7,-4,-1,-1,6,-10,8,1,-2,-5,7,-6,-4,-5,5,3,10,-1,10,5,3,-6,-9,1,8,-4,5,1,3,2,-7,-1,2,1,5,-9,1,-1,4,4,10,-4,-10,-6,4,-10,-5,-9,3,1,6,-8,7,7,-3,-1,9,-8,4,-1,-4,-1,-3,5,2,6,6,-5,5,-2,3,9,-3,-2,-3,-7,-3,3,9,-4,4,9,5,-2,-5,9,2,-1,-9,1,-5,6,-7,6,8,8,-9,3,10,4,-2,5,-5,8,-9,-3,-9,2,7,-3,7,7,8,-10,5,-6,-9,2,7,-5,1,9,-6,-8,-1,7,2,-2,2,-9,-5,6,5,-7,10,-9,1,-2,10,-9,-3,-9,-10,3,4,-1,-6,5,6,6,-6,-6,-4,6,-2,-7,1,8,-6,3,5,-8,-10,-4,7,-2,-8,1,-9,-8,-4,-6,10,6,6,-5,-5,2,8,-2,10,7,2,-2,5,-4,4,3,5,-9,1,4,8,1,-3,-8,-7,-3,-3,2,4,6,-7,1,8,-6,5,-7,5,-7,-1,5,2,-8,2,2,5,3,6,-7,5,5,1,-3,10,-9,6,2,2,10,10,-10,-9,9,9,10,-9,-4,-7,-9,6,1,-1,-8,2,7,-10,-7,3,4,1,-6,9,1,4,4,-7,9,-9,-3,7,-1,8,-7,3,3,-3,2,-6,9,-2,-9,9,9,7,9,1,-2,-7,9,8,3,10,7,-10,-5,9,-3,4,-8,-5,6,4,-6,4,-2,7,8,-3,-3,-9,-5,-4,1,-2,10,4,3,3,3,-5,4,2,-1,-4,8,-3,-6,-3,5,-5,-3,1,9,7,3,-6,-8,-6,-3,-3,8,6,-5,2,-4,-6,-6,-7,3,4,8,3,-8,6,3,-4,9,6,9,-7,3,-4,-2,-1,-4,3,6,-1,6,8,9,10,-2,-2,-4,-3,-4,-5,7,3,2,-7,-3,5,-6,-1,-6,10,9,8,3,-10,10,3,-3,1,4,6,-4,9,7,-2,-4,1,-8,-7,-2,-10,-4,10,-9,5,-8,-3,3,2,-3,-2,-1,-10,-2,2,6,6,4,9,8,-9,4,-9,-5,8,-9,4,-3,-1,-3,-9,-4,1,3,-3,4,7,5,9,-1,9,7,-10,-10,-5,3,-4,-1,4,6,6,9,-10,-3,6,3,-4,1,-1,4,-5,-4,-3,-5,10,4], dtype = "int16")#candidate|7098|(7800,)|const|int16
bop_7099 = relay.not_equal(call_7096.astype('bool'), relay.reshape(const_7098.astype('bool'), relay.shape_of(call_7096))) # shape=(7800,)
bop_7102 = relay.not_equal(call_7097.astype('bool'), relay.reshape(const_7098.astype('bool'), relay.shape_of(call_7097))) # shape=(7800,)
output = bop_7099
output2 = bop_7102
func_7107 = relay.Function([], output)
mod['func_7107'] = func_7107
mod = relay.transform.InferType()(mod)
output = func_7107()
func_7108 = relay.Function([], output)
mutated_mod['func_7108'] = func_7108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7114 = relay.var("var_7114", dtype = "float64", shape = (15, 3, 1))#candidate|7114|(15, 3, 1)|var|float64
uop_7115 = relay.atanh(var_7114.astype('float64')) # shape=(15, 3, 1)
func_2631_call = mod.get_global_var('func_2631')
func_2633_call = mutated_mod.get_global_var('func_2633')
var_7123 = relay.var("var_7123", dtype = "float32", shape = (54,))#candidate|7123|(54,)|var|float32
call_7122 = relay.TupleGetItem(func_2631_call(relay.reshape(var_7123.astype('float32'), [27, 2])), 2)
call_7124 = relay.TupleGetItem(func_2633_call(relay.reshape(var_7123.astype('float32'), [27, 2])), 2)
output = relay.Tuple([uop_7115,call_7122,var_7123,])
output2 = relay.Tuple([uop_7115,call_7124,var_7123,])
func_7127 = relay.Function([var_7114,var_7123,], output)
mod['func_7127'] = func_7127
mod = relay.transform.InferType()(mod)
var_7128 = relay.var("var_7128", dtype = "float64", shape = (15, 3, 1))#candidate|7128|(15, 3, 1)|var|float64
var_7129 = relay.var("var_7129", dtype = "float32", shape = (54,))#candidate|7129|(54,)|var|float32
output = func_7127(var_7128,var_7129,)
func_7130 = relay.Function([var_7128,var_7129,], output)
mutated_mod['func_7130'] = func_7130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5343_call = mod.get_global_var('func_5343')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_7137 = relay.TupleGetItem(func_5343_call(), 0)
call_7138 = relay.TupleGetItem(func_5344_call(), 0)
output = call_7137
output2 = call_7138
func_7157 = relay.Function([], output)
mod['func_7157'] = func_7157
mod = relay.transform.InferType()(mod)
output = func_7157()
func_7158 = relay.Function([], output)
mutated_mod['func_7158'] = func_7158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4585_call = mod.get_global_var('func_4585')
func_4587_call = mutated_mod.get_global_var('func_4587')
call_7179 = func_4585_call()
call_7180 = func_4585_call()
func_6213_call = mod.get_global_var('func_6213')
func_6216_call = mutated_mod.get_global_var('func_6216')
const_7197 = relay.const([-1,3,1,-3,-5,-2,5,7,-2,-5,2,4,-8,5,1,2,3,3,-1,-10,5,7,2,6,-8,10,10,7,-2,-10,10,-4,9,-6,4,-9,2,7,-9,7,-3,9,-10,5,-9,-4,7,4,5,-6,-8,8,-8,3,9,9,8,7,-4,-9,-5,4,2,6,9,-6,7,-6,-8,-6,-8,9,3,-3,6,2,6,-5,-5,6,5,1,-6,6,-8,1,7,4,-7,7,-1,-7,4,-5,-3,2,-1,-7,-2,10,-7,-5,-2,2,-6,-3,5,-1], dtype = "int8")#candidate|7197|(108,)|const|int8
call_7196 = relay.TupleGetItem(func_6213_call(relay.reshape(const_7197.astype('int8'), [9, 12, 1])), 6)
call_7198 = relay.TupleGetItem(func_6216_call(relay.reshape(const_7197.astype('int8'), [9, 12, 1])), 6)
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_7213 = func_2499_call()
call_7214 = func_2499_call()
func_2895_call = mod.get_global_var('func_2895')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_7217 = func_2895_call()
call_7218 = func_2895_call()
bop_7220 = relay.maximum(call_7196.astype('float32'), relay.reshape(call_7179.astype('float32'), relay.shape_of(call_7196))) # shape=(1, 1, 16)
bop_7223 = relay.maximum(call_7198.astype('float32'), relay.reshape(call_7180.astype('float32'), relay.shape_of(call_7198))) # shape=(1, 1, 16)
output = relay.Tuple([const_7197,call_7213,call_7217,bop_7220,])
output2 = relay.Tuple([const_7197,call_7214,call_7218,bop_7223,])
func_7242 = relay.Function([], output)
mod['func_7242'] = func_7242
mod = relay.transform.InferType()(mod)
output = func_7242()
func_7243 = relay.Function([], output)
mutated_mod['func_7243'] = func_7243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6983_call = mod.get_global_var('func_6983')
func_6985_call = mutated_mod.get_global_var('func_6985')
call_7304 = relay.TupleGetItem(func_6983_call(), 0)
call_7305 = relay.TupleGetItem(func_6985_call(), 0)
func_7067_call = mod.get_global_var('func_7067')
func_7069_call = mutated_mod.get_global_var('func_7069')
call_7306 = relay.TupleGetItem(func_7067_call(), 1)
call_7307 = relay.TupleGetItem(func_7069_call(), 1)
uop_7314 = relay.sin(call_7304.astype('float64')) # shape=(9, 12, 1)
uop_7316 = relay.sin(call_7305.astype('float64')) # shape=(9, 12, 1)
output = relay.Tuple([call_7306,uop_7314,])
output2 = relay.Tuple([call_7307,uop_7316,])
func_7318 = relay.Function([], output)
mod['func_7318'] = func_7318
mod = relay.transform.InferType()(mod)
output = func_7318()
func_7319 = relay.Function([], output)
mutated_mod['func_7319'] = func_7319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5576_call = mod.get_global_var('func_5576')
func_5577_call = mutated_mod.get_global_var('func_5577')
call_7348 = relay.TupleGetItem(func_5576_call(), 0)
call_7349 = relay.TupleGetItem(func_5577_call(), 0)
output = call_7348
output2 = call_7349
func_7354 = relay.Function([], output)
mod['func_7354'] = func_7354
mod = relay.transform.InferType()(mod)
output = func_7354()
func_7355 = relay.Function([], output)
mutated_mod['func_7355'] = func_7355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2553_call = mod.get_global_var('func_2553')
func_2555_call = mutated_mod.get_global_var('func_2555')
call_7377 = relay.TupleGetItem(func_2553_call(), 0)
call_7378 = relay.TupleGetItem(func_2555_call(), 0)
func_6440_call = mod.get_global_var('func_6440')
func_6443_call = mutated_mod.get_global_var('func_6443')
var_7392 = relay.var("var_7392", dtype = "float64", shape = (648,))#candidate|7392|(648,)|var|float64
call_7391 = relay.TupleGetItem(func_6440_call(relay.reshape(var_7392.astype('float64'), [9, 12, 6])), 1)
call_7393 = relay.TupleGetItem(func_6443_call(relay.reshape(var_7392.astype('float64'), [9, 12, 6])), 1)
uop_7417 = relay.atanh(var_7392.astype('float64')) # shape=(648,)
func_6341_call = mod.get_global_var('func_6341')
func_6344_call = mutated_mod.get_global_var('func_6344')
var_7453 = relay.var("var_7453", dtype = "int32", shape = ())#candidate|7453|()|var|int32
call_7452 = relay.TupleGetItem(func_6341_call(relay.reshape(var_7453.astype('int32'), [])), 0)
call_7454 = relay.TupleGetItem(func_6344_call(relay.reshape(var_7453.astype('int32'), [])), 0)
output = relay.Tuple([call_7377,call_7391,uop_7417,call_7452,var_7453,])
output2 = relay.Tuple([call_7378,call_7393,uop_7417,call_7454,var_7453,])
func_7469 = relay.Function([var_7392,var_7453,], output)
mod['func_7469'] = func_7469
mod = relay.transform.InferType()(mod)
var_7470 = relay.var("var_7470", dtype = "float64", shape = (648,))#candidate|7470|(648,)|var|float64
var_7471 = relay.var("var_7471", dtype = "int32", shape = ())#candidate|7471|()|var|int32
output = func_7469(var_7470,var_7471,)
func_7472 = relay.Function([var_7470,var_7471,], output)
mutated_mod['func_7472'] = func_7472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3629_call = mod.get_global_var('func_3629')
func_3630_call = mutated_mod.get_global_var('func_3630')
call_7513 = relay.TupleGetItem(func_3629_call(), 2)
call_7514 = relay.TupleGetItem(func_3630_call(), 2)
output = call_7513
output2 = call_7514
func_7516 = relay.Function([], output)
mod['func_7516'] = func_7516
mod = relay.transform.InferType()(mod)
mutated_mod['func_7516'] = func_7516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7516_call = mutated_mod.get_global_var('func_7516')
call_7517 = func_7516_call()
output = call_7517
func_7518 = relay.Function([], output)
mutated_mod['func_7518'] = func_7518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4522_call = mod.get_global_var('func_4522')
func_4523_call = mutated_mod.get_global_var('func_4523')
call_7536 = relay.TupleGetItem(func_4522_call(), 0)
call_7537 = relay.TupleGetItem(func_4523_call(), 0)
func_5094_call = mod.get_global_var('func_5094')
func_5097_call = mutated_mod.get_global_var('func_5097')
var_7564 = relay.var("var_7564", dtype = "float64", shape = (3,))#candidate|7564|(3,)|var|float64
call_7563 = func_5094_call(relay.reshape(var_7564.astype('float64'), [3, 1, 1]))
call_7565 = func_5094_call(relay.reshape(var_7564.astype('float64'), [3, 1, 1]))
output = relay.Tuple([call_7536,call_7563,var_7564,])
output2 = relay.Tuple([call_7537,call_7565,var_7564,])
func_7567 = relay.Function([var_7564,], output)
mod['func_7567'] = func_7567
mod = relay.transform.InferType()(mod)
var_7568 = relay.var("var_7568", dtype = "float64", shape = (3,))#candidate|7568|(3,)|var|float64
output = func_7567(var_7568)
func_7569 = relay.Function([var_7568], output)
mutated_mod['func_7569'] = func_7569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_7586 = relay.TupleGetItem(func_1891_call(), 0)
call_7587 = relay.TupleGetItem(func_1892_call(), 0)
output = call_7586
output2 = call_7587
func_7595 = relay.Function([], output)
mod['func_7595'] = func_7595
mod = relay.transform.InferType()(mod)
output = func_7595()
func_7596 = relay.Function([], output)
mutated_mod['func_7596'] = func_7596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7595_call = mod.get_global_var('func_7595')
func_7596_call = mutated_mod.get_global_var('func_7596')
call_7704 = func_7595_call()
call_7705 = func_7595_call()
output = call_7704
output2 = call_7705
func_7718 = relay.Function([], output)
mod['func_7718'] = func_7718
mod = relay.transform.InferType()(mod)
mutated_mod['func_7718'] = func_7718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7718_call = mutated_mod.get_global_var('func_7718')
call_7719 = func_7718_call()
output = call_7719
func_7720 = relay.Function([], output)
mutated_mod['func_7720'] = func_7720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5576_call = mod.get_global_var('func_5576')
func_5577_call = mutated_mod.get_global_var('func_5577')
call_7763 = relay.TupleGetItem(func_5576_call(), 0)
call_7764 = relay.TupleGetItem(func_5577_call(), 0)
func_7107_call = mod.get_global_var('func_7107')
func_7108_call = mutated_mod.get_global_var('func_7108')
call_7768 = func_7107_call()
call_7769 = func_7107_call()
output = relay.Tuple([call_7763,call_7768,])
output2 = relay.Tuple([call_7764,call_7769,])
func_7770 = relay.Function([], output)
mod['func_7770'] = func_7770
mod = relay.transform.InferType()(mod)
mutated_mod['func_7770'] = func_7770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7770_call = mutated_mod.get_global_var('func_7770')
call_7771 = func_7770_call()
output = call_7771
func_7772 = relay.Function([], output)
mutated_mod['func_7772'] = func_7772
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7777 = relay.const([[[-6.075772,-4.575076,3.005971,0.060462,3.137485,1.976528,5.902156],[9.204906,6.083771,3.068583,-1.624130,2.838130,6.020525,4.209516],[2.034739,2.159029,-2.062115,-6.441382,-8.653546,8.192657,6.992666],[6.410006,7.557809,-2.694390,2.892714,7.650171,-3.188721,6.295175],[9.612587,-3.009087,-0.628798,-4.335179,-2.342560,-4.861269,-7.653099],[-6.482524,9.483379,-7.439867,7.013585,6.262204,4.812096,-8.746341],[-4.594498,3.072826,-3.427341,-0.836571,3.370256,-7.818636,6.745836],[3.195686,-2.749568,-6.198947,9.849915,9.588127,6.456368,6.986910],[6.529742,-3.899593,-3.607125,8.787395,-1.396988,8.795909,-4.982943],[4.416206,-1.004595,-2.596080,-9.548109,-0.845889,9.195791,-1.421695],[0.636552,7.791789,-5.200369,-7.489557,5.051973,3.579700,8.473565]],[[-2.663556,-8.594146,7.203101,-4.285436,-1.030955,-8.345043,-6.783733],[-2.661677,4.989058,9.954966,-6.583335,-3.837837,-9.046585,-3.749696],[0.857187,-3.114593,1.034502,5.091616,3.236516,-1.100686,2.867001],[4.294025,7.685433,-0.001986,8.184876,1.554933,0.806882,-0.164996],[-7.255955,-4.522327,-6.920111,9.469371,7.150415,-4.526041,-5.488956],[-7.938037,-6.640477,9.289713,9.840929,-9.155152,7.694286,-4.017798],[4.198156,-0.999446,5.018706,-5.540140,9.866736,-3.793437,-8.665564],[-9.033791,4.645393,-2.088881,-1.137215,2.402541,-4.616649,-9.240673],[-4.114482,-8.923282,7.922616,8.800802,9.914307,-4.408079,4.900942],[-8.528230,7.454379,-8.649213,3.265888,-9.704781,-8.558726,-2.028248],[5.810608,2.753302,3.990725,-6.838975,-4.387578,-1.743052,3.108482]],[[3.244960,7.879237,-4.779924,-8.933563,8.066368,-2.230633,7.584250],[-1.385340,8.991650,-5.193499,9.868421,-3.579317,-5.455232,4.751407],[7.180084,0.492900,3.134749,-9.552852,8.234714,-4.985227,-7.690232],[2.866874,9.891700,4.463475,4.443077,2.690972,-6.643656,-8.444196],[5.921108,7.673999,-5.254943,3.327452,0.794216,-7.016840,-9.898834],[8.186702,8.618547,-5.451057,-3.682850,2.263655,8.116749,-1.740648],[-4.319819,-6.332184,-9.654964,-7.528424,-6.648681,-0.454171,4.438613],[-0.635208,4.187158,0.257855,-8.311405,-6.022197,4.764170,5.694784],[-5.277886,-4.098043,-9.397613,-5.959228,-1.935740,-2.824114,-8.831047],[-0.002021,6.140085,4.849593,5.786596,3.730671,-7.907040,-5.572419],[4.368503,-7.378166,-0.100216,-3.590144,4.666754,4.175150,-1.000277]],[[-8.028846,2.905820,-0.907628,-1.265826,4.586841,-8.035491,4.799022],[-2.733654,7.894738,8.214477,-9.980426,-4.344097,4.479343,7.235137],[-9.843563,-0.050464,5.484975,7.642470,-6.521712,8.986057,4.145332],[-8.205597,0.213472,6.122559,-6.354471,-8.762511,-1.347408,7.289331],[9.886995,-4.287776,-7.073795,-7.842316,-5.920133,-2.654387,3.866898],[9.812389,8.706644,-6.045339,-2.344196,7.762073,-5.552624,7.245100],[5.942257,-7.257947,-9.737799,-3.084693,4.093948,-7.346347,-8.728181],[-1.284484,-4.576063,6.982497,6.765829,-8.217665,2.330423,-8.327471],[-8.150638,-0.430699,8.971010,-3.619674,6.895402,-6.734441,6.461234],[3.070704,2.293378,-6.494792,6.596065,-4.022729,9.834394,-2.509921],[-7.753654,-7.405840,9.201396,-7.850656,-8.281512,-8.147434,4.570828]],[[-3.109832,7.063967,3.553140,-6.189364,-5.519695,1.088947,-5.447410],[-2.113018,9.580369,-3.493950,0.328962,-5.878064,-4.646037,-0.073547],[-4.239072,7.392451,-2.137922,-5.778413,-1.467516,9.845011,-5.910382],[1.012195,8.988022,-9.925781,-8.659328,8.947701,-1.971165,-6.650910],[-2.535915,3.914500,-1.001608,1.000571,0.880320,-1.473706,-6.567173],[-3.227430,-6.196628,-6.560110,3.384090,-1.160114,6.532432,4.703901],[7.763531,-0.792753,-8.671844,1.297925,-1.442254,-2.284443,-0.108977],[0.322810,-0.044298,-9.001178,4.609914,5.608804,3.072954,9.668869],[5.694304,-0.811599,-9.390278,-5.429056,-2.978524,6.174441,-1.826701],[-3.527425,3.502582,-0.977002,8.198577,-4.811907,7.215131,-9.205590],[-8.080870,0.871539,-4.774908,-4.689733,-6.989669,-7.816433,-6.637151]],[[0.747382,4.237760,-0.893082,-3.726477,-3.474388,3.160776,-2.890531],[-1.658796,0.113073,-0.493875,-2.856642,-5.318549,8.133728,7.179511],[1.658225,-1.003264,4.530801,-4.862688,-1.551663,-7.193628,-5.131378],[7.135759,-5.424744,8.569649,-3.143194,-3.541250,5.995369,-6.257189],[1.005749,-0.182304,5.833804,9.739616,-9.323446,-4.587128,-1.955833],[4.394977,-4.188536,-4.934562,7.175364,-9.980779,9.800022,-0.352772],[6.191593,-1.936436,9.052758,6.000791,4.759561,8.960430,-4.515461],[-5.889517,-7.581455,-5.016168,-3.949433,1.273820,-5.759713,-1.778883],[-2.039096,-2.644570,9.849023,-6.160564,9.346580,4.878257,-1.589627],[-1.230579,5.468020,-7.383909,9.004811,-8.928544,9.995572,6.402104],[-3.095411,1.900476,-3.583577,-2.737508,-4.345430,-1.260009,9.927237]],[[-9.748301,-9.417984,-1.467654,0.401878,8.870031,9.219333,6.783122],[6.590102,5.281731,-6.229123,-1.102415,-4.752444,-4.180111,0.552732],[5.151435,-3.388620,7.098700,-7.243081,-8.169992,-8.719069,-1.417714],[-2.114963,-2.663812,-9.192662,3.258080,-5.976326,-7.500009,-5.224082],[-1.207567,9.436769,-9.717967,5.463457,8.987017,-7.088806,-4.290459],[1.855517,-7.809437,-5.112550,-6.323629,-2.706167,9.321854,6.560828],[-1.040130,-6.575470,-6.886560,-9.358493,5.115295,-3.297748,9.600847],[3.169453,8.931066,1.451606,-1.803354,-3.554771,-5.437381,-5.527511],[4.562579,4.754709,5.837195,-6.095953,-3.839238,3.548683,3.474357],[-0.473040,-4.102724,-9.710011,-1.508065,7.581089,1.731312,7.112471],[9.115906,8.529413,-8.476453,-7.344771,-7.410140,2.767924,7.780474]],[[-9.323583,-0.371429,1.592411,-6.151187,-0.385290,2.045742,5.230943],[0.651265,6.980141,-7.688666,7.211178,6.427661,3.628410,2.367010],[-3.343608,6.876784,1.627959,6.668074,-6.339746,-4.252120,2.825042],[-1.050214,-2.001672,3.894913,-6.152288,-6.878324,-4.729499,5.221696],[9.408774,-7.411377,3.370993,-6.203492,4.184032,-1.208238,-6.305673],[-8.030310,-2.546431,-6.033253,-9.352584,-5.415634,-3.609626,2.444104],[2.811685,-1.358316,7.519570,-7.865468,-5.134509,9.801983,5.514660],[1.640757,-4.965805,3.390900,-2.043802,6.626321,2.356923,-6.609606],[-7.098580,3.126986,-1.020696,-7.635502,-5.922342,2.525337,7.197163],[1.169163,-5.254244,-0.423215,-8.084697,1.827123,-5.658303,-0.627967],[5.359071,6.384656,-2.028092,6.492993,-4.568743,-3.693906,-1.033771]],[[3.993395,-1.748450,-6.578187,2.020495,8.264805,-6.685579,-0.118580],[5.377660,6.332737,0.813659,-3.240696,7.931235,5.721199,4.073982],[-2.935040,7.032761,7.963549,-8.766778,-3.983448,3.942353,-8.023402],[-7.870543,-3.894555,9.843927,-6.971515,-1.995756,-9.697911,-9.381709],[1.922484,9.490745,-1.154364,9.872776,-3.289280,7.497855,4.239843],[-1.798319,1.289239,-5.515076,-9.732433,7.878236,9.009509,0.529776],[5.950576,8.653165,1.087401,-8.849066,2.766558,3.044151,-6.697237],[-7.421228,4.536544,1.310951,0.576872,-7.820952,1.281555,1.981438],[8.763904,-1.673098,-3.801370,6.175685,-6.973463,4.237220,4.577773],[3.635542,-2.319067,3.177458,-1.702324,-6.050776,6.062616,6.564901],[-5.789610,1.190903,1.442871,-3.032151,4.537444,5.911561,5.134746]]], dtype = "float32")#candidate|7777|(9, 11, 7)|const|float32
var_7778 = relay.var("var_7778", dtype = "float32", shape = (9, 11, 7))#candidate|7778|(9, 11, 7)|var|float32
bop_7779 = relay.subtract(const_7777.astype('float32'), relay.reshape(var_7778.astype('float32'), relay.shape_of(const_7777))) # shape=(9, 11, 7)
uop_7783 = relay.log(var_7778.astype('float64')) # shape=(9, 11, 7)
output = relay.Tuple([bop_7779,uop_7783,])
output2 = relay.Tuple([bop_7779,uop_7783,])
func_7785 = relay.Function([var_7778,], output)
mod['func_7785'] = func_7785
mod = relay.transform.InferType()(mod)
var_7786 = relay.var("var_7786", dtype = "float32", shape = (9, 11, 7))#candidate|7786|(9, 11, 7)|var|float32
output = func_7785(var_7786)
func_7787 = relay.Function([var_7786], output)
mutated_mod['func_7787'] = func_7787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3913_call = mod.get_global_var('func_3913')
func_3914_call = mutated_mod.get_global_var('func_3914')
call_7794 = relay.TupleGetItem(func_3913_call(), 0)
call_7795 = relay.TupleGetItem(func_3914_call(), 0)
uop_7802 = relay.sinh(call_7794.astype('float32')) # shape=(1, 1, 16)
uop_7804 = relay.sinh(call_7795.astype('float32')) # shape=(1, 1, 16)
output = uop_7802
output2 = uop_7804
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
