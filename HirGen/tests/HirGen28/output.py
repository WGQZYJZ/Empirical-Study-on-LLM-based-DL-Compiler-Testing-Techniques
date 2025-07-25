import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_282 = relay.var("var_282", dtype = "int8", shape = ())#candidate|282|()|var|int8
var_283 = relay.var("var_283", dtype = "int8", shape = (10, 10, 2))#candidate|283|(10, 10, 2)|var|int8
bop_284 = relay.less(var_282.astype('bool'), var_283.astype('bool')) # shape=(10, 10, 2)
output = bop_284
output2 = bop_284
func_289 = relay.Function([var_282,var_283,], output)
mod['func_289'] = func_289
mod = relay.transform.InferType()(mod)
mutated_mod['func_289'] = func_289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_289_call = mutated_mod.get_global_var('func_289')
var_291 = relay.var("var_291", dtype = "int8", shape = ())#candidate|291|()|var|int8
var_292 = relay.var("var_292", dtype = "int8", shape = (10, 10, 2))#candidate|292|(10, 10, 2)|var|int8
call_290 = func_289_call(var_291,var_292,)
output = call_290
func_293 = relay.Function([var_291,var_292,], output)
mutated_mod['func_293'] = func_293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_491 = relay.var("var_491", dtype = "int32", shape = (8, 2, 1))#candidate|491|(8, 2, 1)|var|int32
var_492 = relay.var("var_492", dtype = "int32", shape = (8, 2, 10))#candidate|492|(8, 2, 10)|var|int32
bop_493 = relay.not_equal(var_491.astype('bool'), var_492.astype('bool')) # shape=(8, 2, 10)
func_289_call = mod.get_global_var('func_289')
func_293_call = mutated_mod.get_global_var('func_293')
var_505 = relay.var("var_505", dtype = "int8", shape = ())#candidate|505|()|var|int8
var_506 = relay.var("var_506", dtype = "int8", shape = (200,))#candidate|506|(200,)|var|int8
call_504 = func_289_call(relay.reshape(var_505.astype('int8'), []), relay.reshape(var_506.astype('int8'), [10, 10, 2]), )
call_507 = func_289_call(relay.reshape(var_505.astype('int8'), []), relay.reshape(var_506.astype('int8'), [10, 10, 2]), )
uop_511 = relay.sin(bop_493.astype('float64')) # shape=(8, 2, 10)
var_513 = relay.var("var_513", dtype = "bool", shape = (8, 2, 10))#candidate|513|(8, 2, 10)|var|bool
bop_514 = relay.floor_divide(bop_493.astype('float64'), relay.reshape(var_513.astype('float64'), relay.shape_of(bop_493))) # shape=(8, 2, 10)
bop_523 = relay.greater(var_491.astype('bool'), bop_493.astype('bool')) # shape=(8, 2, 10)
output = relay.Tuple([call_504,var_505,var_506,uop_511,bop_514,bop_523,])
output2 = relay.Tuple([call_507,var_505,var_506,uop_511,bop_514,bop_523,])
func_554 = relay.Function([var_491,var_492,var_505,var_506,var_513,], output)
mod['func_554'] = func_554
mod = relay.transform.InferType()(mod)
mutated_mod['func_554'] = func_554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_554_call = mutated_mod.get_global_var('func_554')
var_556 = relay.var("var_556", dtype = "int32", shape = (8, 2, 1))#candidate|556|(8, 2, 1)|var|int32
var_557 = relay.var("var_557", dtype = "int32", shape = (8, 2, 10))#candidate|557|(8, 2, 10)|var|int32
var_558 = relay.var("var_558", dtype = "int8", shape = ())#candidate|558|()|var|int8
var_559 = relay.var("var_559", dtype = "int8", shape = (200,))#candidate|559|(200,)|var|int8
var_560 = relay.var("var_560", dtype = "bool", shape = (8, 2, 10))#candidate|560|(8, 2, 10)|var|bool
call_555 = func_554_call(var_556,var_557,var_558,var_559,var_560,)
output = call_555
func_561 = relay.Function([var_556,var_557,var_558,var_559,var_560,], output)
mutated_mod['func_561'] = func_561
mutated_mod = relay.transform.InferType()(mutated_mod)
const_617 = relay.const([[[0.111631,3.640881,0.144686,0.142907,-1.829002,9.362795,-5.411409],[9.665525,-6.150516,-8.673783,3.373793,6.226138,8.272526,-3.301123],[8.700978,-7.685382,-7.628103,-6.275488,-9.219957,-4.984278,9.361837],[-3.454435,-9.935153,-4.865100,-4.037156,5.128937,3.618818,-1.711180],[-9.253655,3.826619,-2.044701,-7.315147,5.096887,-1.922531,-0.309990],[-1.652483,-8.364753,4.476232,1.939492,0.687780,-7.818551,8.812113],[1.854588,0.850751,-2.458257,-6.413028,-6.711181,-5.651326,1.741547],[4.779362,9.585584,5.911342,-8.106184,-2.478156,-4.378180,4.739836],[-1.806202,-0.809846,-3.585305,9.851903,4.958735,-0.618065,-9.618982],[1.834062,8.549156,5.294874,4.578774,6.734860,4.593213,7.236558],[4.424079,5.376687,0.068564,-2.252324,4.198888,-9.894541,2.926535],[-1.190411,7.833904,9.609205,-7.151457,0.124009,-7.864200,7.925529],[5.836545,3.417077,6.211621,-8.738359,1.058384,-2.966792,8.965442],[0.745563,7.307484,-8.706784,9.509944,-3.944810,9.930838,0.805755],[-3.476974,6.307004,6.143247,-3.750078,5.294967,7.767075,1.415291],[6.388641,0.583650,4.123883,-8.886162,3.415682,-4.945082,9.087060]],[[-0.114317,7.245303,7.591600,-5.087855,1.029915,6.573348,5.970296],[8.613080,7.441755,2.364061,8.655963,0.859826,2.455656,-6.037876],[-3.967577,0.513925,-4.594137,4.433378,9.813352,2.844991,6.357710],[-9.156113,0.266602,7.588759,-8.997185,6.198444,-6.618075,-4.498651],[-3.598957,8.427118,-7.188671,9.098544,5.048648,9.561565,-4.805463],[6.231188,4.345023,-2.879982,-5.267767,0.276702,5.749229,-5.659706],[-9.675289,3.473300,9.917328,3.945533,9.402463,9.060609,-9.653658],[7.888989,1.535035,-4.344893,-8.420100,4.416337,-3.710004,-2.183750],[-1.674697,6.366925,4.903148,3.790266,7.911449,-2.716751,6.158878],[3.005529,-1.087928,-2.721408,-0.634615,4.070325,9.364521,0.338830],[6.456191,7.851466,-7.349846,-6.594775,0.895497,2.555364,9.148861],[2.731096,1.169997,-9.267760,-5.705897,3.675704,0.497284,9.351360],[5.753030,-3.406323,-8.069741,-7.182131,2.843679,-1.170640,-5.153469],[8.985386,-4.031499,-6.093294,-7.729221,0.601050,0.142641,6.296979],[7.222263,-7.439795,1.080718,-1.489655,-0.438653,-8.182672,1.126459],[8.638526,-9.422402,1.833427,7.394977,-0.193507,-8.600895,-4.061580]],[[-5.954455,-1.095731,8.220343,8.135552,-6.188847,-0.228610,-2.535836],[-5.270706,-9.972921,-9.532500,-1.567468,9.283871,5.815022,9.810690],[0.503772,-2.144038,0.923745,-4.639038,1.410134,1.297052,4.772258],[-3.351679,6.430613,7.798332,-3.652671,-1.268235,-9.514821,9.060357],[-2.678125,1.431533,-1.659358,6.852211,2.184009,-7.451300,2.851308],[-6.308466,-0.010821,1.012639,2.928535,4.382355,-8.717080,-8.081870],[3.631692,-6.185469,3.145872,0.096731,0.803297,9.119976,-6.532215],[7.245747,-6.886081,-1.362990,8.148870,-6.429298,4.829958,-2.912356],[2.920266,-3.195330,-9.433286,-3.281261,-5.561572,-4.983047,7.182859],[-4.951257,7.523671,1.762906,9.013918,-2.494013,8.328767,9.836123],[-1.843869,-8.244646,1.474974,-9.037288,-6.659206,3.878461,6.702455],[-0.100470,9.385867,-2.912482,8.366365,-2.267603,-5.962877,3.859127],[0.863504,-2.574174,-3.316690,-4.039575,3.373168,-6.343761,8.219244],[-3.988969,7.700849,2.518240,-4.753125,6.791308,-4.797499,-7.659082],[9.684440,-5.155365,0.801802,-9.684075,-6.940560,3.083852,-8.243183],[6.393465,3.080565,-8.632864,-1.860865,0.239650,3.480808,-3.563993]],[[0.574867,-0.539551,-3.504902,5.901142,8.993402,-8.822815,-0.372383],[9.499531,5.496825,6.478546,2.722917,1.649399,7.023870,-2.879297],[5.268383,-7.470255,9.258154,8.490470,-1.148438,8.833800,4.876969],[6.397180,6.191612,-0.833538,5.906173,7.906449,9.434724,-2.849515],[-7.567324,8.088917,-7.230573,-5.091155,6.483577,9.772335,-5.218625],[7.646346,-6.795701,-3.588840,-0.002789,-8.631642,-1.634033,-0.331116],[-9.159400,-4.705298,4.765387,3.643041,-6.280759,1.574034,4.476965],[6.842401,-2.022102,7.035797,1.389099,-7.668743,-3.924082,3.075997],[8.339139,-8.839609,-6.166264,-7.788778,5.124232,0.327701,1.320461],[2.959527,-3.076279,-6.386867,1.069777,8.476443,9.749107,-5.561675],[9.195384,-4.715502,7.177260,-4.196206,-4.504234,7.520844,-4.437718],[9.056635,-7.287240,9.735916,7.219523,7.019801,8.049326,3.531159],[-4.154392,1.212416,1.041747,-7.804224,-8.337303,-5.083122,5.318052],[-0.532518,6.412329,3.800508,-8.930589,-7.824309,2.492196,0.341787],[-8.896818,9.400012,-2.864932,-0.938411,9.582336,6.667529,-6.815773],[-0.973569,1.581694,4.082365,-8.722672,-3.004353,6.384281,-7.490366]],[[-1.799421,-1.095339,-8.605985,-5.302146,-7.717968,-1.155025,8.160839],[3.956817,6.065348,-1.220140,2.988964,6.888123,-4.710694,-9.207517],[-0.559155,-0.117262,-6.439105,-3.039877,9.658731,-0.993669,3.664813],[6.742817,-6.372015,-1.241887,-5.376746,-8.146281,6.527900,6.711165],[-7.873051,7.707139,-6.647953,7.888415,-1.852233,9.406819,-2.014976],[5.060788,-3.783786,9.796202,-9.607272,-6.274201,-2.914465,-7.920189],[6.007258,6.485660,9.412685,-6.686101,3.068434,4.307760,2.973456],[1.960363,-0.643252,-3.270248,8.224182,2.630315,4.286624,-5.879125],[-3.490908,4.103083,-9.617872,9.121458,-4.618925,1.198350,-3.418706],[5.475128,2.994076,2.994294,-9.161117,-9.724918,4.913201,7.595883],[7.391058,-2.819078,-0.243387,5.186433,6.684066,-5.299061,5.336936],[6.684112,-0.740301,5.498355,2.784718,5.893788,-5.129669,1.770565],[6.982443,6.565912,-0.695514,9.594628,0.634508,2.136883,9.100918],[-7.668573,5.641755,-8.292022,6.175259,7.901276,9.727433,-7.669742],[-8.888773,4.945856,-0.688960,-2.153498,4.876879,9.441939,1.252196],[2.105614,-5.150229,1.979159,0.476215,-4.715038,3.812166,0.082505]],[[-6.580245,8.633363,3.429010,3.076114,5.423287,-0.732844,3.836191],[0.454891,-9.119511,5.372647,8.271051,-3.677813,6.921216,0.695866],[-1.842991,0.348887,-6.949504,4.584567,3.171372,8.824497,-9.179954],[2.492869,8.559392,-9.914933,4.827701,-9.754271,-0.114834,8.617906],[5.546017,4.473808,9.608875,3.453828,3.016449,3.267477,0.020332],[1.462060,-0.985919,3.630592,7.300984,4.696520,1.643964,9.237214],[-5.024457,3.906307,2.964696,1.791297,4.364962,-9.288908,4.027350],[-4.277016,-9.541021,5.685549,-1.077252,-5.791597,-3.543821,0.760253],[-4.732367,-2.459281,0.017207,-7.530265,-3.210533,-8.497062,-8.872123],[-5.391089,-3.224158,-8.449317,-3.219528,-1.105588,-9.673297,-4.203466],[-6.247965,7.227568,4.985137,-1.806146,5.605051,6.634317,-7.566474],[-8.060031,3.955508,3.273754,9.013803,-6.423780,4.661127,-2.006707],[-2.344859,-4.068856,-5.958404,5.007654,9.030863,8.134600,-7.518023],[-0.259136,-0.911512,-4.809000,9.460380,8.731729,1.374923,-0.602546],[-4.751330,9.734950,-0.400387,-1.110756,7.189885,-1.070651,3.940408],[2.732888,-7.869337,-5.009104,-0.361223,-3.938289,-5.155428,-5.997901]],[[-6.693197,-6.663099,-6.373367,2.679509,-0.959539,4.487318,7.268145],[-6.116072,9.831010,-2.194378,-4.450376,-4.500844,6.565541,-7.692124],[9.402245,-2.731879,-6.959674,-9.902107,-6.607247,2.482121,7.839527],[-9.404725,-0.631876,7.663942,-7.884166,0.379349,8.017635,-1.058534],[7.839487,-8.138442,2.790231,-2.393315,-1.455352,-8.802389,-9.613966],[7.066089,5.250230,-3.506993,-7.911132,3.125328,8.886925,5.562358],[4.266466,-8.727303,7.627430,1.643486,4.164509,-0.794743,-2.048419],[-7.537836,-1.410999,4.555561,0.762693,1.486563,2.772814,-9.664723],[4.681069,6.305819,8.745679,2.165603,5.853848,-9.143000,-9.448115],[-9.797639,2.278313,4.032461,-6.297234,4.987597,-2.673645,5.106694],[-4.428557,8.262097,-7.220326,-9.440360,-2.131938,-5.624190,-1.242011],[-8.674182,8.663482,4.608614,9.656325,-6.547399,2.905424,7.473421],[-1.891168,-8.351809,-6.220785,-6.268185,-5.078347,2.276158,0.724763],[-6.227907,-6.703764,-6.817343,9.633994,-4.910482,9.394181,-1.486149],[4.633749,-8.149618,0.223081,-2.934552,-7.480073,-0.657507,2.761867],[8.065842,5.554331,-8.639318,-8.874011,3.830224,-4.793588,-9.021882]],[[-3.843227,6.635740,-8.663079,7.857848,-4.012960,-0.295944,-7.210641],[1.061951,-5.012643,-8.126308,6.865930,0.536379,-3.034859,0.650895],[-7.539203,-8.437975,5.539393,-5.049789,4.390631,9.920902,7.917998],[8.053141,-0.255026,1.799706,2.704127,-3.975600,-0.839276,9.160169],[-1.372241,-8.585217,-5.038733,0.151059,-7.100567,-0.499203,9.698654],[0.565668,0.681513,-2.187039,4.399686,-2.677578,-7.680085,0.905604],[-3.320603,7.489923,-1.254192,0.612882,-7.090315,-7.455068,0.066326],[-3.206983,-3.913573,5.741760,-1.538790,8.172048,-4.135724,0.713530],[-0.582175,1.943415,7.430945,8.291009,-3.451277,-3.893446,3.360006],[2.166068,1.454610,0.152069,3.934330,2.916711,-7.599639,-9.609638],[-9.984328,5.391258,-3.875836,8.206974,1.570571,8.792271,-8.105631],[-0.396524,-6.495374,-4.504495,-6.096276,6.630965,-8.361049,3.769486],[9.938305,8.656184,6.458886,-6.957271,-3.375801,7.651237,-3.745922],[0.790397,9.573086,-7.287095,-1.010154,1.737427,-6.409970,-3.904468],[-9.335819,-7.474558,9.507480,8.467584,-4.920222,8.233456,-1.910931],[0.758451,0.547946,3.491167,-5.186616,0.062407,-7.258902,6.196589]],[[2.195947,8.164036,-4.784055,-0.630001,-1.507272,-4.726996,3.859344],[4.628116,6.027653,2.559835,4.308903,9.930592,-7.283812,-9.479374],[2.347421,-8.470034,-5.257469,-0.330916,5.881406,-9.738101,0.760575],[-2.252939,-8.497078,-2.187909,-7.682003,1.875636,-0.106760,-1.249766],[1.070313,3.636542,-9.187686,9.415450,3.797777,7.711933,-0.983760],[-8.846747,6.405162,1.863525,-2.296033,5.659127,9.798643,0.348174],[6.574471,-8.717069,-5.497562,6.011895,7.435949,1.761206,5.432784],[2.647792,5.178996,7.624797,7.860173,-3.830149,-5.751451,-1.213285],[-6.058946,0.700232,1.739988,-2.652710,9.246006,1.608143,9.440717],[4.547429,3.117820,-8.572238,6.828163,2.285591,-7.663735,-4.519463],[3.034465,-6.071487,-4.715189,2.711284,-0.724010,-7.776430,-2.317209],[-0.394716,-8.005069,-0.695515,8.647302,-6.678242,-2.640996,4.503111],[-0.169404,7.868480,-9.220885,3.074495,3.980640,7.184935,8.898450],[6.937957,0.967359,6.326217,8.024269,4.292381,-8.466046,1.660716],[-9.424107,-2.139649,1.235104,-2.201414,5.880027,-1.108110,3.959940],[-7.680759,7.185224,-2.900185,-2.861902,8.865986,4.320266,-5.904957]],[[-4.947463,-9.336897,-4.574886,9.874103,-1.822498,0.784377,-6.832825],[-8.524080,6.337442,-1.826170,-0.587119,8.332421,-9.955328,-0.107818],[-8.733700,9.190690,9.480977,1.353730,-9.061776,1.505104,-5.687368],[3.898936,-7.643219,-4.600808,-1.347031,4.137694,6.945195,1.018343],[1.127327,1.009282,-7.086131,-9.561800,-6.018228,4.067009,8.529009],[3.779242,-0.566018,-0.672743,-1.037221,-1.732156,1.185572,0.722618],[2.475605,-6.037925,8.738619,-6.295521,-1.069938,0.774918,-4.681743],[-0.114070,2.726648,5.432509,-3.472423,-8.913390,4.763464,5.859368],[-6.253797,8.867144,-0.200716,-7.635760,-2.628835,2.477371,-1.529787],[5.356912,-4.789395,-3.164593,-8.251015,1.888116,8.116761,9.738415],[-4.680643,8.948353,-2.047569,-7.417383,-7.591892,-4.004739,9.027996],[8.340207,-5.173765,-0.610071,-8.258959,-2.598657,8.385901,2.074005],[4.048440,9.718305,-4.152431,3.388312,8.442442,9.526363,-9.202342],[-5.620438,1.159199,5.667781,0.233917,-3.477702,-3.873435,-8.468592],[-9.126903,-3.613345,-7.057507,-3.927782,-3.255646,4.033300,0.561536],[1.695857,-1.215375,-3.348832,-2.082272,1.684834,9.524079,9.842112]],[[-6.979798,6.445065,-6.506857,9.197492,6.303896,5.295269,0.858447],[-5.655164,2.353013,-4.639096,1.153916,3.052284,4.312053,4.864748],[7.576551,-2.426950,-8.859724,-1.723054,-7.380129,-8.774723,4.700548],[4.282703,-3.651417,-5.816973,-7.418863,-2.908413,8.226695,4.482065],[-0.318268,6.931756,5.088394,-9.503523,-7.049340,-9.021038,-6.934862],[-6.454097,-9.240310,-4.855044,3.803087,-1.521150,8.760568,-1.365742],[0.380672,5.326334,-8.908683,5.205004,1.736941,-6.961690,-1.417879],[-3.831693,2.102385,3.469898,-7.489863,-5.170639,-3.632617,0.848771],[3.395764,-4.467657,2.140897,7.703741,-1.581259,-9.324346,-7.314527],[2.092409,2.206098,6.733312,8.849080,3.506971,-3.240871,7.588444],[-2.780850,-0.139473,-3.957492,-1.128514,8.655267,-3.750563,-3.303833],[9.334821,6.558125,-7.468644,-2.009996,6.853817,-8.990685,4.803241],[-1.813569,0.249162,-0.805668,4.735832,-7.552868,-9.231777,4.426601],[4.400364,6.924641,-9.856171,-8.110098,-5.939873,-6.909391,-4.890230],[-4.944657,8.041235,-2.428622,5.025238,-7.290023,-6.572728,3.533676],[-7.714720,9.156304,-1.079243,-8.079103,4.868572,5.669251,3.696963]],[[3.329485,-5.234194,-8.529690,-4.059313,-1.251538,1.789417,-8.377868],[4.787741,-5.876999,-1.330780,-1.250279,0.468852,0.188133,5.877749],[-0.271946,-5.095557,-7.038627,6.492352,-9.733647,4.879932,1.051958],[-5.962181,-7.732772,2.608656,6.354457,-1.645566,0.272049,4.304655],[-5.910057,1.120037,5.644317,-7.580471,3.299756,-4.412331,-0.082734],[-9.767221,-4.616821,7.307386,6.869087,-0.967370,7.126983,-5.397556],[-0.283602,9.703970,-1.833034,6.490874,8.886118,0.903024,3.883305],[-4.574580,5.501309,4.609086,5.230181,8.369013,-6.262440,-4.303576],[-1.567725,-6.120049,-9.608216,-4.696535,-9.304329,-1.886960,8.941893],[-1.846798,-7.507126,-9.755080,-2.017973,7.691017,3.891590,-5.948509],[-0.859132,5.751703,7.884812,5.471080,9.563807,-7.041129,2.056304],[4.861998,-5.862428,2.118494,4.716545,-0.158120,-8.063890,8.711902],[-1.664676,3.508180,-5.038599,-6.335333,-7.418606,4.280961,3.427505],[6.294766,5.432524,3.342391,8.551757,-6.772053,3.668346,-0.578828],[-7.467338,4.558907,1.058459,-2.679653,0.386519,5.768221,-2.836799],[1.026859,-4.096882,9.415598,-8.917555,6.478123,3.957077,-2.546296]],[[-7.858990,-2.924347,-3.168100,-6.415093,-3.060773,-3.160068,2.629711],[7.811429,-1.788794,1.808615,-7.680288,-8.506715,0.118020,-4.191323],[4.450667,5.368455,6.908938,6.931724,8.687976,4.895548,-7.230301],[7.261282,3.684181,5.006778,-2.834755,-0.471957,8.614725,1.466077],[-6.858880,-3.767961,-8.452676,9.536047,9.341849,9.733673,-3.572022],[4.860714,-9.177490,-6.684070,7.414264,-7.586200,-4.397410,-1.438442],[8.409471,8.615313,7.008637,-6.166818,9.359682,0.866752,-6.052019],[-3.673614,2.573127,8.175946,-1.845625,8.484581,8.689091,8.083252],[-0.361231,-5.200828,4.028323,0.840195,1.619922,-1.420571,-8.220138],[6.397359,6.163541,4.767027,2.365966,-4.371031,5.106893,-5.082870],[7.775616,-8.748077,7.573288,-8.705692,-3.237646,-3.808126,7.081584],[6.061706,-0.854911,-7.974354,-2.163689,4.828263,-9.424125,5.006934],[2.660732,-8.284956,-6.250166,5.192117,9.650783,-1.180288,8.767683],[3.796957,-3.655841,-5.416609,-9.871946,-6.905790,6.328194,-3.837128],[7.734250,4.623881,1.361049,-1.213846,-6.613080,-3.058900,0.959891],[-1.766251,9.351665,9.596863,-1.748580,-6.157319,-2.679289,3.763918]]], dtype = "float64")#candidate|617|(13, 16, 7)|const|float64
uop_618 = relay.sin(const_617.astype('float64')) # shape=(13, 16, 7)
func_554_call = mod.get_global_var('func_554')
func_561_call = mutated_mod.get_global_var('func_561')
const_632 = relay.const([9,8,-7,-1,-4,5,-10,-8,-2,6,-8,5,-10,4,-4,1], dtype = "int32")#candidate|632|(16,)|const|int32
const_633 = relay.const([5,6,10,5,-9,-4,1,-8,9,3,-5,-7,-4,6,-4,5,-2,7,10,-9,6,-6,9,-5,9,4,-2,-4,4,2,-10,9,-9,-4,-10,-7,-6,5,-6,-4,8,-2,-9,-5,-4,-10,5,6,8,4,-5,-4,4,6,8,9,-8,-6,-7,9,-9,8,10,1,-8,-6,6,1,9,-3,7,-3,-3,1,2,-1,-1,-7,5,-3,-3,-5,10,10,-5,-6,-3,7,-10,7,-10,-4,-9,4,-1,8,-7,-2,1,4,-4,-8,1,-4,4,4,-10,-5,-1,5,-7,5,-6,-8,-10,-2,-7,3,6,1,-1,-3,7,-1,8,-10,1,-10,-6,-5,-3,3,7,-7,5,2,7,6,5,10,-3,10,-10,10,-1,4,-2,-5,5,2,2,-4,1,-10,-7,-4,3,-4,-6,-10], dtype = "int32")#candidate|633|(160,)|const|int32
const_634 = relay.const(-6, dtype = "int8")#candidate|634|()|const|int8
var_635 = relay.var("var_635", dtype = "int8", shape = (200,))#candidate|635|(200,)|var|int8
call_631 = relay.TupleGetItem(func_554_call(relay.reshape(const_632.astype('int32'), [8, 2, 1]), relay.reshape(const_633.astype('int32'), [8, 2, 10]), relay.reshape(const_634.astype('int8'), []), relay.reshape(var_635.astype('int8'), [200,]), relay.reshape(const_633.astype('bool'), [8, 2, 10]), ), 0)
call_636 = relay.TupleGetItem(func_561_call(relay.reshape(const_632.astype('int32'), [8, 2, 1]), relay.reshape(const_633.astype('int32'), [8, 2, 10]), relay.reshape(const_634.astype('int8'), []), relay.reshape(var_635.astype('int8'), [200,]), relay.reshape(const_633.astype('bool'), [8, 2, 10]), ), 0)
func_289_call = mod.get_global_var('func_289')
func_293_call = mutated_mod.get_global_var('func_293')
call_638 = func_289_call(relay.reshape(const_634.astype('int8'), []), relay.reshape(call_631.astype('int8'), [10, 10, 2]), )
call_639 = func_289_call(relay.reshape(const_634.astype('int8'), []), relay.reshape(call_631.astype('int8'), [10, 10, 2]), )
func_554_call = mod.get_global_var('func_554')
func_561_call = mutated_mod.get_global_var('func_561')
call_640 = relay.TupleGetItem(func_554_call(relay.reshape(const_632.astype('int32'), [8, 2, 1]), relay.reshape(const_633.astype('int32'), [8, 2, 10]), relay.reshape(const_634.astype('int8'), []), relay.reshape(var_635.astype('int8'), [200,]), relay.reshape(const_633.astype('bool'), [8, 2, 10]), ), 4)
call_641 = relay.TupleGetItem(func_561_call(relay.reshape(const_632.astype('int32'), [8, 2, 1]), relay.reshape(const_633.astype('int32'), [8, 2, 10]), relay.reshape(const_634.astype('int8'), []), relay.reshape(var_635.astype('int8'), [200,]), relay.reshape(const_633.astype('bool'), [8, 2, 10]), ), 4)
output = relay.Tuple([uop_618,call_631,const_632,const_633,const_634,var_635,call_638,call_640,])
output2 = relay.Tuple([uop_618,call_636,const_632,const_633,const_634,var_635,call_639,call_641,])
func_647 = relay.Function([var_635,], output)
mod['func_647'] = func_647
mod = relay.transform.InferType()(mod)
var_648 = relay.var("var_648", dtype = "int8", shape = (200,))#candidate|648|(200,)|var|int8
output = func_647(var_648)
func_649 = relay.Function([var_648], output)
mutated_mod['func_649'] = func_649
mutated_mod = relay.transform.InferType()(mutated_mod)
const_679 = relay.const(1, dtype = "uint32")#candidate|679|()|const|uint32
const_680 = relay.const([[[6,8,-7,-6],[8,-9,-9,8],[4,-1,6,-9],[8,7,3,-2],[5,-9,-9,-7],[2,8,8,1],[5,-3,8,2],[-3,7,-10,5]],[[1,8,-10,8],[9,-1,1,-1],[4,5,-7,9],[8,6,-9,3],[-6,9,-6,-9],[-1,3,4,8],[9,1,2,8],[8,-10,-6,4]]], dtype = "uint32")#candidate|680|(2, 8, 4)|const|uint32
bop_681 = relay.multiply(const_679.astype('uint32'), const_680.astype('uint32')) # shape=(2, 8, 4)
output = relay.Tuple([bop_681,])
output2 = relay.Tuple([bop_681,])
func_708 = relay.Function([], output)
mod['func_708'] = func_708
mod = relay.transform.InferType()(mod)
mutated_mod['func_708'] = func_708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_708_call = mutated_mod.get_global_var('func_708')
call_709 = func_708_call()
output = call_709
func_710 = relay.Function([], output)
mutated_mod['func_710'] = func_710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_708_call = mod.get_global_var('func_708')
func_710_call = mutated_mod.get_global_var('func_710')
call_711 = relay.TupleGetItem(func_708_call(), 0)
call_712 = relay.TupleGetItem(func_710_call(), 0)
output = call_711
output2 = call_712
func_718 = relay.Function([], output)
mod['func_718'] = func_718
mod = relay.transform.InferType()(mod)
mutated_mod['func_718'] = func_718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mutated_mod.get_global_var('func_718')
call_719 = func_718_call()
output = call_719
func_720 = relay.Function([], output)
mutated_mod['func_720'] = func_720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_708_call = mod.get_global_var('func_708')
func_710_call = mutated_mod.get_global_var('func_710')
call_740 = relay.TupleGetItem(func_708_call(), 0)
call_741 = relay.TupleGetItem(func_710_call(), 0)
output = call_740
output2 = call_741
func_749 = relay.Function([], output)
mod['func_749'] = func_749
mod = relay.transform.InferType()(mod)
mutated_mod['func_749'] = func_749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mutated_mod.get_global_var('func_749')
call_750 = func_749_call()
output = call_750
func_751 = relay.Function([], output)
mutated_mod['func_751'] = func_751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_752 = func_749_call()
call_753 = func_749_call()
func_554_call = mod.get_global_var('func_554')
func_561_call = mutated_mod.get_global_var('func_561')
var_762 = relay.var("var_762", dtype = "int32", shape = (16,))#candidate|762|(16,)|var|int32
var_763 = relay.var("var_763", dtype = "int32", shape = (160,))#candidate|763|(160,)|var|int32
var_764 = relay.var("var_764", dtype = "int8", shape = ())#candidate|764|()|var|int8
var_765 = relay.var("var_765", dtype = "int8", shape = (200,))#candidate|765|(200,)|var|int8
call_761 = relay.TupleGetItem(func_554_call(relay.reshape(var_762.astype('int32'), [8, 2, 1]), relay.reshape(var_763.astype('int32'), [8, 2, 10]), relay.reshape(var_764.astype('int8'), []), relay.reshape(var_765.astype('int8'), [200,]), relay.reshape(var_763.astype('bool'), [8, 2, 10]), ), 2)
call_766 = relay.TupleGetItem(func_561_call(relay.reshape(var_762.astype('int32'), [8, 2, 1]), relay.reshape(var_763.astype('int32'), [8, 2, 10]), relay.reshape(var_764.astype('int8'), []), relay.reshape(var_765.astype('int8'), [200,]), relay.reshape(var_763.astype('bool'), [8, 2, 10]), ), 2)
func_647_call = mod.get_global_var('func_647')
func_649_call = mutated_mod.get_global_var('func_649')
call_776 = relay.TupleGetItem(func_647_call(relay.reshape(call_761.astype('int8'), [200,])), 3)
call_777 = relay.TupleGetItem(func_649_call(relay.reshape(call_761.astype('int8'), [200,])), 3)
output = relay.Tuple([call_752,call_761,var_762,var_763,var_764,var_765,call_776,])
output2 = relay.Tuple([call_753,call_766,var_762,var_763,var_764,var_765,call_777,])
func_778 = relay.Function([var_762,var_763,var_764,var_765,], output)
mod['func_778'] = func_778
mod = relay.transform.InferType()(mod)
mutated_mod['func_778'] = func_778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_778_call = mutated_mod.get_global_var('func_778')
var_780 = relay.var("var_780", dtype = "int32", shape = (16,))#candidate|780|(16,)|var|int32
var_781 = relay.var("var_781", dtype = "int32", shape = (160,))#candidate|781|(160,)|var|int32
var_782 = relay.var("var_782", dtype = "int8", shape = ())#candidate|782|()|var|int8
var_783 = relay.var("var_783", dtype = "int8", shape = (200,))#candidate|783|(200,)|var|int8
call_779 = func_778_call(var_780,var_781,var_782,var_783,)
output = call_779
func_784 = relay.Function([var_780,var_781,var_782,var_783,], output)
mutated_mod['func_784'] = func_784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_837 = func_718_call()
call_838 = func_718_call()
func_554_call = mod.get_global_var('func_554')
func_561_call = mutated_mod.get_global_var('func_561')
var_840 = relay.var("var_840", dtype = "int32", shape = (16,))#candidate|840|(16,)|var|int32
var_841 = relay.var("var_841", dtype = "int32", shape = (16, 10))#candidate|841|(16, 10)|var|int32
var_842 = relay.var("var_842", dtype = "int8", shape = ())#candidate|842|()|var|int8
const_843 = relay.const([[4,7],[-5,-9],[-1,7],[-6,10],[-5,-10],[4,-3],[-4,3],[-7,-5],[2,-4],[9,2],[-10,1],[-5,10],[8,10],[-6,7],[2,-2],[-6,1],[-3,6],[8,5],[-8,-6],[7,-4],[9,-9],[7,-3],[-7,-5],[5,10],[10,-1],[-4,8],[3,5],[-1,-5],[3,3],[9,6],[-4,6],[10,9],[-1,-10],[-7,5],[4,9],[10,-6],[-7,2],[9,-1],[-2,2],[4,2],[2,-10],[-10,-10],[-6,-10],[7,9],[8,-2],[-3,10],[2,5],[-1,-1],[1,-3],[-6,-5],[-6,-9],[4,-6],[3,-7],[-1,-10],[-9,8],[6,-5],[1,-5],[-5,-1],[7,1],[-10,-4],[-3,7],[-10,-8],[4,10],[-5,4],[-7,5],[3,-10],[-6,4],[7,8],[10,5],[-4,8],[-9,7],[-7,4],[-4,-5],[-4,9],[-7,-5],[10,-6],[1,-10],[-6,-3],[9,3],[-5,-10],[-5,-7],[-10,-9],[9,3],[9,10],[3,-5],[8,-8],[-9,3],[-7,4],[7,-10],[-8,-4],[-3,8],[6,-2],[-8,2],[4,-5],[10,-7],[-10,-8],[2,2],[5,9],[-2,-1],[-5,-1]], dtype = "int8")#candidate|843|(100, 2)|const|int8
call_839 = relay.TupleGetItem(func_554_call(relay.reshape(var_840.astype('int32'), [8, 2, 1]), relay.reshape(var_841.astype('int32'), [8, 2, 10]), relay.reshape(var_842.astype('int8'), []), relay.reshape(const_843.astype('int8'), [200,]), relay.reshape(var_841.astype('bool'), [8, 2, 10]), ), 3)
call_844 = relay.TupleGetItem(func_561_call(relay.reshape(var_840.astype('int32'), [8, 2, 1]), relay.reshape(var_841.astype('int32'), [8, 2, 10]), relay.reshape(var_842.astype('int8'), []), relay.reshape(const_843.astype('int8'), [200,]), relay.reshape(var_841.astype('bool'), [8, 2, 10]), ), 3)
output = relay.Tuple([call_837,call_839,var_840,var_841,var_842,const_843,])
output2 = relay.Tuple([call_838,call_844,var_840,var_841,var_842,const_843,])
func_845 = relay.Function([var_840,var_841,var_842,], output)
mod['func_845'] = func_845
mod = relay.transform.InferType()(mod)
var_846 = relay.var("var_846", dtype = "int32", shape = (16,))#candidate|846|(16,)|var|int32
var_847 = relay.var("var_847", dtype = "int32", shape = (16, 10))#candidate|847|(16, 10)|var|int32
var_848 = relay.var("var_848", dtype = "int8", shape = ())#candidate|848|()|var|int8
output = func_845(var_846,var_847,var_848,)
func_849 = relay.Function([var_846,var_847,var_848,], output)
mutated_mod['func_849'] = func_849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_866 = func_718_call()
call_867 = func_718_call()
var_870 = relay.var("var_870", dtype = "uint32", shape = (2, 8, 4))#candidate|870|(2, 8, 4)|var|uint32
bop_871 = relay.divide(call_866.astype('float32'), relay.reshape(var_870.astype('float32'), relay.shape_of(call_866))) # shape=(2, 8, 4)
bop_874 = relay.divide(call_867.astype('float32'), relay.reshape(var_870.astype('float32'), relay.shape_of(call_867))) # shape=(2, 8, 4)
uop_878 = relay.atan(call_866.astype('float64')) # shape=(2, 8, 4)
uop_880 = relay.atan(call_867.astype('float64')) # shape=(2, 8, 4)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_884 = func_749_call()
call_885 = func_749_call()
bop_886 = relay.greater_equal(uop_878.astype('bool'), relay.reshape(bop_871.astype('bool'), relay.shape_of(uop_878))) # shape=(2, 8, 4)
bop_889 = relay.greater_equal(uop_880.astype('bool'), relay.reshape(bop_874.astype('bool'), relay.shape_of(uop_880))) # shape=(2, 8, 4)
output = relay.Tuple([call_884,bop_886,])
output2 = relay.Tuple([call_885,bop_889,])
func_901 = relay.Function([var_870,], output)
mod['func_901'] = func_901
mod = relay.transform.InferType()(mod)
var_902 = relay.var("var_902", dtype = "uint32", shape = (2, 8, 4))#candidate|902|(2, 8, 4)|var|uint32
output = func_901(var_902)
func_903 = relay.Function([var_902], output)
mutated_mod['func_903'] = func_903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_708_call = mod.get_global_var('func_708')
func_710_call = mutated_mod.get_global_var('func_710')
call_953 = relay.TupleGetItem(func_708_call(), 0)
call_954 = relay.TupleGetItem(func_710_call(), 0)
output = relay.Tuple([call_953,])
output2 = relay.Tuple([call_954,])
func_957 = relay.Function([], output)
mod['func_957'] = func_957
mod = relay.transform.InferType()(mod)
output = func_957()
func_958 = relay.Function([], output)
mutated_mod['func_958'] = func_958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_1048 = func_749_call()
call_1049 = func_749_call()
output = call_1048
output2 = call_1049
func_1055 = relay.Function([], output)
mod['func_1055'] = func_1055
mod = relay.transform.InferType()(mod)
mutated_mod['func_1055'] = func_1055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mutated_mod.get_global_var('func_1055')
call_1056 = func_1055_call()
output = call_1056
func_1057 = relay.Function([], output)
mutated_mod['func_1057'] = func_1057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_1111 = func_749_call()
call_1112 = func_749_call()
func_647_call = mod.get_global_var('func_647')
func_649_call = mutated_mod.get_global_var('func_649')
var_1114 = relay.var("var_1114", dtype = "int8", shape = (200,))#candidate|1114|(200,)|var|int8
call_1113 = relay.TupleGetItem(func_647_call(relay.reshape(var_1114.astype('int8'), [200,])), 6)
call_1115 = relay.TupleGetItem(func_649_call(relay.reshape(var_1114.astype('int8'), [200,])), 6)
func_554_call = mod.get_global_var('func_554')
func_561_call = mutated_mod.get_global_var('func_561')
const_1121 = relay.const([10,-4,-5,-8,-3,-5,5,3,-2,6,-10,9,-10,-6,9,-7], dtype = "int32")#candidate|1121|(16,)|const|int32
const_1122 = relay.const([[-6],[9],[-10],[1],[2],[-5],[10],[-10],[8],[6],[1],[-8],[-1],[-4],[-1],[-1],[3],[-4],[-6],[-7],[4],[3],[-9],[2],[3],[1],[-3],[10],[-8],[-6],[-1],[7],[-8],[-8],[-5],[-5],[7],[2],[1],[5],[5],[7],[-5],[-3],[-5],[3],[6],[1],[2],[-10],[-2],[-5],[-1],[5],[2],[-7],[6],[-6],[-4],[3],[5],[-5],[-7],[-7],[-4],[5],[2],[-7],[8],[6],[-1],[-8],[8],[7],[2],[-9],[-7],[10],[-1],[-2],[-3],[-2],[-8],[7],[-10],[7],[-5],[-10],[8],[3],[1],[-9],[-6],[-2],[-3],[3],[3],[1],[6],[-5],[-9],[10],[7],[5],[1],[-7],[9],[1],[-4],[-6],[9],[-5],[7],[-2],[-1],[9],[-1],[-4],[-3],[6],[-8],[-6],[-1],[-4],[-10],[-4],[-10],[-9],[-2],[-9],[-10],[-3],[-1],[9],[-7],[-8],[2],[-1],[9],[-7],[-6],[7],[-7],[-2],[-9],[-4],[-1],[-10],[-3],[4],[6],[4],[-6],[-10],[-10],[5],[8],[-3],[-10],[6]], dtype = "int32")#candidate|1122|(160, 1)|const|int32
var_1123 = relay.var("var_1123", dtype = "int8", shape = ())#candidate|1123|()|var|int8
call_1120 = relay.TupleGetItem(func_554_call(relay.reshape(const_1121.astype('int32'), [8, 2, 1]), relay.reshape(const_1122.astype('int32'), [8, 2, 10]), relay.reshape(var_1123.astype('int8'), []), relay.reshape(var_1114.astype('int8'), [200,]), relay.reshape(const_1122.astype('bool'), [8, 2, 10]), ), 5)
call_1124 = relay.TupleGetItem(func_561_call(relay.reshape(const_1121.astype('int32'), [8, 2, 1]), relay.reshape(const_1122.astype('int32'), [8, 2, 10]), relay.reshape(var_1123.astype('int8'), []), relay.reshape(var_1114.astype('int8'), [200,]), relay.reshape(const_1122.astype('bool'), [8, 2, 10]), ), 5)
bop_1127 = relay.logical_or(var_1123.astype('bool'), call_1111.astype('bool')) # shape=(2, 8, 4)
bop_1130 = relay.logical_or(var_1123.astype('bool'), call_1112.astype('bool')) # shape=(2, 8, 4)
output = relay.Tuple([call_1113,var_1114,call_1120,const_1121,const_1122,bop_1127,])
output2 = relay.Tuple([call_1115,var_1114,call_1124,const_1121,const_1122,bop_1130,])
func_1131 = relay.Function([var_1114,var_1123,], output)
mod['func_1131'] = func_1131
mod = relay.transform.InferType()(mod)
var_1132 = relay.var("var_1132", dtype = "int8", shape = (200,))#candidate|1132|(200,)|var|int8
var_1133 = relay.var("var_1133", dtype = "int8", shape = ())#candidate|1133|()|var|int8
output = func_1131(var_1132,var_1133,)
func_1134 = relay.Function([var_1132,var_1133,], output)
mutated_mod['func_1134'] = func_1134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_1141 = func_749_call()
call_1142 = func_749_call()
uop_1149 = relay.erf(call_1141.astype('float32')) # shape=(2, 8, 4)
uop_1151 = relay.erf(call_1142.astype('float32')) # shape=(2, 8, 4)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_1165 = func_1055_call()
call_1166 = func_1055_call()
func_845_call = mod.get_global_var('func_845')
func_849_call = mutated_mod.get_global_var('func_849')
const_1169 = relay.const([-3,5,-9,-6,-6,7,5,-10,-3,3,7,-1,5,-7,-5,9], dtype = "int32")#candidate|1169|(16,)|const|int32
const_1170 = relay.const([6,10,2,-6,-1,2,10,-6,-5,-5,1,-4,-8,-3,6,2,3,-4,5,-3,-3,-8,10,7,7,2,1,6,-6,6,-8,-4,10,5,9,2,5,-8,5,10,7,-10,1,-10,7,-9,-4,-6,-2,-10,1,5,-5,2,-8,2,6,8,9,4,-3,1,-9,-4,9,4,-7,7,1,1,-2,9,-4,7,4,-7,8,8,6,8,5,7,-10,5,-6,5,9,7,-10,7,8,2,-6,3,2,7,-1,3,-1,-5,7,4,-3,-1,5,-10,6,9,4,-1,-3,-6,-5,8,-9,10,4,-2,-2,3,-3,-2,-4,-8,-5,5,-9,4,1,-7,-6,6,10,-8,-1,2,3,10,7,6,-8,9,1,3,-5,2,-9,3,6,-2,4,8,9,7,-7,7,-1,7,10,-5], dtype = "int32")#candidate|1170|(160,)|const|int32
var_1171 = relay.var("var_1171", dtype = "int8", shape = ())#candidate|1171|()|var|int8
call_1168 = relay.TupleGetItem(func_845_call(relay.reshape(const_1169.astype('int32'), [16,]), relay.reshape(const_1170.astype('int32'), [16, 10]), relay.reshape(var_1171.astype('int8'), []), ), 0)
call_1172 = relay.TupleGetItem(func_849_call(relay.reshape(const_1169.astype('int32'), [16,]), relay.reshape(const_1170.astype('int32'), [16, 10]), relay.reshape(var_1171.astype('int8'), []), ), 0)
var_1174 = relay.var("var_1174", dtype = "float32", shape = (2, 8, 4))#candidate|1174|(2, 8, 4)|var|float32
bop_1175 = relay.bitwise_and(uop_1149.astype('int8'), relay.reshape(var_1174.astype('int8'), relay.shape_of(uop_1149))) # shape=(2, 8, 4)
bop_1178 = relay.bitwise_and(uop_1151.astype('int8'), relay.reshape(var_1174.astype('int8'), relay.shape_of(uop_1151))) # shape=(2, 8, 4)
uop_1184 = relay.acos(uop_1149.astype('float64')) # shape=(2, 8, 4)
uop_1186 = relay.acos(uop_1151.astype('float64')) # shape=(2, 8, 4)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_1210 = func_749_call()
call_1211 = func_749_call()
output = relay.Tuple([call_1165,call_1168,const_1169,const_1170,var_1171,bop_1175,uop_1184,call_1210,])
output2 = relay.Tuple([call_1166,call_1172,const_1169,const_1170,var_1171,bop_1178,uop_1186,call_1211,])
func_1224 = relay.Function([var_1171,var_1174,], output)
mod['func_1224'] = func_1224
mod = relay.transform.InferType()(mod)
mutated_mod['func_1224'] = func_1224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1224_call = mutated_mod.get_global_var('func_1224')
var_1226 = relay.var("var_1226", dtype = "int8", shape = ())#candidate|1226|()|var|int8
var_1227 = relay.var("var_1227", dtype = "float32", shape = (2, 8, 4))#candidate|1227|(2, 8, 4)|var|float32
call_1225 = func_1224_call(var_1226,var_1227,)
output = call_1225
func_1228 = relay.Function([var_1226,var_1227,], output)
mutated_mod['func_1228'] = func_1228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_708_call = mod.get_global_var('func_708')
func_710_call = mutated_mod.get_global_var('func_710')
call_1248 = relay.TupleGetItem(func_708_call(), 0)
call_1249 = relay.TupleGetItem(func_710_call(), 0)
output = relay.Tuple([call_1248,])
output2 = relay.Tuple([call_1249,])
func_1266 = relay.Function([], output)
mod['func_1266'] = func_1266
mod = relay.transform.InferType()(mod)
output = func_1266()
func_1267 = relay.Function([], output)
mutated_mod['func_1267'] = func_1267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_1292 = relay.TupleGetItem(func_957_call(), 0)
call_1293 = relay.TupleGetItem(func_958_call(), 0)
func_289_call = mod.get_global_var('func_289')
func_293_call = mutated_mod.get_global_var('func_293')
const_1297 = relay.const(-9, dtype = "int8")#candidate|1297|()|const|int8
var_1298 = relay.var("var_1298", dtype = "int8", shape = (200,))#candidate|1298|(200,)|var|int8
call_1296 = func_289_call(relay.reshape(const_1297.astype('int8'), []), relay.reshape(var_1298.astype('int8'), [10, 10, 2]), )
call_1299 = func_289_call(relay.reshape(const_1297.astype('int8'), []), relay.reshape(var_1298.astype('int8'), [10, 10, 2]), )
uop_1300 = relay.asin(call_1292.astype('float64')) # shape=(2, 8, 4)
uop_1302 = relay.asin(call_1293.astype('float64')) # shape=(2, 8, 4)
output = relay.Tuple([call_1296,const_1297,var_1298,uop_1300,])
output2 = relay.Tuple([call_1299,const_1297,var_1298,uop_1302,])
func_1303 = relay.Function([var_1298,], output)
mod['func_1303'] = func_1303
mod = relay.transform.InferType()(mod)
var_1304 = relay.var("var_1304", dtype = "int8", shape = (200,))#candidate|1304|(200,)|var|int8
output = func_1303(var_1304)
func_1305 = relay.Function([var_1304], output)
mutated_mod['func_1305'] = func_1305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_1363 = func_1055_call()
call_1364 = func_1055_call()
output = call_1363
output2 = call_1364
func_1386 = relay.Function([], output)
mod['func_1386'] = func_1386
mod = relay.transform.InferType()(mod)
mutated_mod['func_1386'] = func_1386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1386_call = mutated_mod.get_global_var('func_1386')
call_1387 = func_1386_call()
output = call_1387
func_1388 = relay.Function([], output)
mutated_mod['func_1388'] = func_1388
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1410 = relay.const(7, dtype = "uint16")#candidate|1410|()|const|uint16
var_1411 = relay.var("var_1411", dtype = "uint16", shape = (14, 2, 16))#candidate|1411|(14, 2, 16)|var|uint16
bop_1412 = relay.bitwise_or(const_1410.astype('uint16'), var_1411.astype('uint16')) # shape=(14, 2, 16)
output = relay.Tuple([bop_1412,])
output2 = relay.Tuple([bop_1412,])
func_1421 = relay.Function([var_1411,], output)
mod['func_1421'] = func_1421
mod = relay.transform.InferType()(mod)
mutated_mod['func_1421'] = func_1421
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1422 = relay.var("var_1422", dtype = "uint16", shape = (14, 2, 16))#candidate|1422|(14, 2, 16)|var|uint16
func_1421_call = mutated_mod.get_global_var('func_1421')
call_1423 = func_1421_call(var_1422)
output = call_1423
func_1424 = relay.Function([var_1422], output)
mutated_mod['func_1424'] = func_1424
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1448 = relay.var("var_1448", dtype = "float64", shape = (6, 6, 10))#candidate|1448|(6, 6, 10)|var|float64
uop_1449 = relay.sigmoid(var_1448.astype('float64')) # shape=(6, 6, 10)
func_901_call = mod.get_global_var('func_901')
func_903_call = mutated_mod.get_global_var('func_903')
var_1456 = relay.var("var_1456", dtype = "uint32", shape = (8, 8))#candidate|1456|(8, 8)|var|uint32
call_1455 = relay.TupleGetItem(func_901_call(relay.reshape(var_1456.astype('uint32'), [2, 8, 4])), 1)
call_1457 = relay.TupleGetItem(func_903_call(relay.reshape(var_1456.astype('uint32'), [2, 8, 4])), 1)
output = relay.Tuple([uop_1449,call_1455,var_1456,])
output2 = relay.Tuple([uop_1449,call_1457,var_1456,])
func_1462 = relay.Function([var_1448,var_1456,], output)
mod['func_1462'] = func_1462
mod = relay.transform.InferType()(mod)
var_1463 = relay.var("var_1463", dtype = "float64", shape = (6, 6, 10))#candidate|1463|(6, 6, 10)|var|float64
var_1464 = relay.var("var_1464", dtype = "uint32", shape = (8, 8))#candidate|1464|(8, 8)|var|uint32
output = func_1462(var_1463,var_1464,)
func_1465 = relay.Function([var_1463,var_1464,], output)
mutated_mod['func_1465'] = func_1465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_708_call = mod.get_global_var('func_708')
func_710_call = mutated_mod.get_global_var('func_710')
call_1590 = relay.TupleGetItem(func_708_call(), 0)
call_1591 = relay.TupleGetItem(func_710_call(), 0)
func_1462_call = mod.get_global_var('func_1462')
func_1465_call = mutated_mod.get_global_var('func_1465')
var_1595 = relay.var("var_1595", dtype = "float64", shape = (360,))#candidate|1595|(360,)|var|float64
call_1594 = relay.TupleGetItem(func_1462_call(relay.reshape(var_1595.astype('float64'), [6, 6, 10]), relay.reshape(call_1590.astype('uint32'), [8, 8]), ), 0)
call_1596 = relay.TupleGetItem(func_1465_call(relay.reshape(var_1595.astype('float64'), [6, 6, 10]), relay.reshape(call_1590.astype('uint32'), [8, 8]), ), 0)
output = relay.Tuple([call_1590,call_1594,var_1595,])
output2 = relay.Tuple([call_1591,call_1596,var_1595,])
func_1599 = relay.Function([var_1595,], output)
mod['func_1599'] = func_1599
mod = relay.transform.InferType()(mod)
var_1600 = relay.var("var_1600", dtype = "float64", shape = (360,))#candidate|1600|(360,)|var|float64
output = func_1599(var_1600)
func_1601 = relay.Function([var_1600], output)
mutated_mod['func_1601'] = func_1601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_1634 = relay.TupleGetItem(func_957_call(), 0)
call_1635 = relay.TupleGetItem(func_958_call(), 0)
uop_1644 = relay.exp(call_1634.astype('float64')) # shape=(2, 8, 4)
uop_1646 = relay.exp(call_1635.astype('float64')) # shape=(2, 8, 4)
uop_1651 = relay.sinh(uop_1644.astype('float64')) # shape=(2, 8, 4)
uop_1653 = relay.sinh(uop_1646.astype('float64')) # shape=(2, 8, 4)
func_289_call = mod.get_global_var('func_289')
func_293_call = mutated_mod.get_global_var('func_293')
const_1663 = relay.const(8, dtype = "int8")#candidate|1663|()|const|int8
const_1664 = relay.const([9,1,-6,-10,-5,5,5,-10,9,8,-4,-8,7,-10,-1,1,10,9,10,-6,-8,-6,-8,9,-10,9,-2,-10,-6,-6,-7,6,2,5,5,-7,-2,-5,1,8,-2,5,5,3,-8,-8,-9,-4,2,-2,-3,-1,4,-5,-3,-6,1,-7,9,-10,2,-1,6,1,-5,6,-2,2,4,-10,-2,10,-8,-4,8,3,3,10,-9,7,3,-1,10,-10,-1,-1,-9,-10,9,-3,7,-8,9,-2,-10,10,2,-8,-7,7,3,2,-1,8,-6,1,-8,-6,9,-3,6,-2,-9,3,3,3,-9,7,-7,4,-7,-9,-3,9,-2,3,-10,-8,-7,2,-10,3,9,-1,-4,-2,-9,-5,-5,-6,-9,-4,-4,-7,-1,1,3,1,6,2,7,1,4,-8,-10,-5,3,-7,2,-10,-2,-4,-4,9,-7,2,-5,-9,8,-10,-10,-7,-4,2,8,-1,-2,7,2,-8,7,4,-2,2,8,8,7,-3,-2,9,8,10,4,5,-3,4,4,1,9,-6], dtype = "int8")#candidate|1664|(200,)|const|int8
call_1662 = func_289_call(relay.reshape(const_1663.astype('int8'), []), relay.reshape(const_1664.astype('int8'), [10, 10, 2]), )
call_1665 = func_289_call(relay.reshape(const_1663.astype('int8'), []), relay.reshape(const_1664.astype('int8'), [10, 10, 2]), )
uop_1687 = relay.tan(uop_1644.astype('float32')) # shape=(2, 8, 4)
uop_1689 = relay.tan(uop_1646.astype('float32')) # shape=(2, 8, 4)
uop_1693 = relay.asinh(uop_1644.astype('float32')) # shape=(2, 8, 4)
uop_1695 = relay.asinh(uop_1646.astype('float32')) # shape=(2, 8, 4)
bop_1715 = relay.less(uop_1651.astype('bool'), relay.reshape(uop_1644.astype('bool'), relay.shape_of(uop_1651))) # shape=(2, 8, 4)
bop_1718 = relay.less(uop_1653.astype('bool'), relay.reshape(uop_1646.astype('bool'), relay.shape_of(uop_1653))) # shape=(2, 8, 4)
func_778_call = mod.get_global_var('func_778')
func_784_call = mutated_mod.get_global_var('func_784')
var_1731 = relay.var("var_1731", dtype = "int32", shape = (1, 16))#candidate|1731|(1, 16)|var|int32
const_1732 = relay.const([3,-4,-6,9,6,-10,9,3,4,4,8,5,-4,6,8,1,-3,-4,-3,-2,8,-3,-5,-8,-4,1,4,3,5,-9,5,8,6,-10,8,-7,4,-1,8,10,-6,3,-8,-7,8,-10,7,-4,2,3,5,-6,3,10,1,-3,-2,6,-7,-3,-10,-9,-10,1,6,-2,5,8,7,9,-9,-4,1,10,-4,4,-7,10,-7,-9,-6,-1,-1,1,8,-6,4,-7,10,6,2,6,4,-7,9,-3,-9,8,-7,9,-10,-4,3,-3,1,-6,9,2,-10,-6,7,3,-6,-7,3,10,-9,2,-6,-4,4,9,2,9,-10,-10,-6,4,-6,-7,-5,4,1,-7,-1,-3,-2,10,-6,5,-6,5,-8,6,-8,-6,-9,-10,-6,-7,-7,-2,5,-3,1,-8,-3,-8,2,8], dtype = "int32")#candidate|1732|(160,)|const|int32
call_1730 = relay.TupleGetItem(func_778_call(relay.reshape(var_1731.astype('int32'), [16,]), relay.reshape(const_1732.astype('int32'), [160,]), relay.reshape(const_1663.astype('int8'), []), relay.reshape(const_1664.astype('int8'), [200,]), ), 1)
call_1733 = relay.TupleGetItem(func_784_call(relay.reshape(var_1731.astype('int32'), [16,]), relay.reshape(const_1732.astype('int32'), [160,]), relay.reshape(const_1663.astype('int8'), []), relay.reshape(const_1664.astype('int8'), [200,]), ), 1)
uop_1734 = relay.cos(uop_1651.astype('float64')) # shape=(2, 8, 4)
uop_1736 = relay.cos(uop_1653.astype('float64')) # shape=(2, 8, 4)
output = relay.Tuple([call_1662,const_1663,const_1664,uop_1687,uop_1693,bop_1715,call_1730,var_1731,const_1732,uop_1734,])
output2 = relay.Tuple([call_1665,const_1663,const_1664,uop_1689,uop_1695,bop_1718,call_1733,var_1731,const_1732,uop_1736,])
func_1742 = relay.Function([var_1731,], output)
mod['func_1742'] = func_1742
mod = relay.transform.InferType()(mod)
var_1743 = relay.var("var_1743", dtype = "int32", shape = (1, 16))#candidate|1743|(1, 16)|var|int32
output = func_1742(var_1743)
func_1744 = relay.Function([var_1743], output)
mutated_mod['func_1744'] = func_1744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_1746 = func_749_call()
call_1747 = func_749_call()
func_708_call = mod.get_global_var('func_708')
func_710_call = mutated_mod.get_global_var('func_710')
call_1756 = relay.TupleGetItem(func_708_call(), 0)
call_1757 = relay.TupleGetItem(func_710_call(), 0)
output = relay.Tuple([call_1746,call_1756,])
output2 = relay.Tuple([call_1747,call_1757,])
func_1758 = relay.Function([], output)
mod['func_1758'] = func_1758
mod = relay.transform.InferType()(mod)
mutated_mod['func_1758'] = func_1758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mutated_mod.get_global_var('func_1758')
call_1759 = func_1758_call()
output = call_1759
func_1760 = relay.Function([], output)
mutated_mod['func_1760'] = func_1760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1266_call = mod.get_global_var('func_1266')
func_1267_call = mutated_mod.get_global_var('func_1267')
call_1846 = relay.TupleGetItem(func_1266_call(), 0)
call_1847 = relay.TupleGetItem(func_1267_call(), 0)
output = relay.Tuple([call_1846,])
output2 = relay.Tuple([call_1847,])
func_1848 = relay.Function([], output)
mod['func_1848'] = func_1848
mod = relay.transform.InferType()(mod)
output = func_1848()
func_1849 = relay.Function([], output)
mutated_mod['func_1849'] = func_1849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_1855 = func_1055_call()
call_1856 = func_1055_call()
output = call_1855
output2 = call_1856
func_1857 = relay.Function([], output)
mod['func_1857'] = func_1857
mod = relay.transform.InferType()(mod)
mutated_mod['func_1857'] = func_1857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1857_call = mutated_mod.get_global_var('func_1857')
call_1858 = func_1857_call()
output = call_1858
func_1859 = relay.Function([], output)
mutated_mod['func_1859'] = func_1859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_1911 = func_749_call()
call_1912 = func_749_call()
func_778_call = mod.get_global_var('func_778')
func_784_call = mutated_mod.get_global_var('func_784')
var_1914 = relay.var("var_1914", dtype = "int32", shape = (16,))#candidate|1914|(16,)|var|int32
const_1915 = relay.const([2,-2,2,3,-4,1,9,5,3,10,-8,-5,2,7,-2,8,10,-2,-3,-10,-4,-6,-7,8,10,1,8,-8,7,-10,2,3,-7,6,-10,8,7,10,4,3,4,1,1,-2,-3,-7,2,8,-5,-3,3,2,7,6,-7,-7,-5,5,-6,-6,3,7,-5,7,1,6,3,-4,7,-2,-8,-7,7,-1,-1,3,10,7,7,7,6,-4,1,-7,-7,-7,10,-2,-6,-10,-9,10,5,7,3,-1,-7,-6,-2,-9,6,8,9,-2,2,-3,7,2,-1,5,5,3,-1,-2,-5,-2,8,6,-9,-4,10,-1,1,10,-4,-9,1,1,-2,4,6,8,-7,3,1,-6,7,10,1,-1,7,4,-4,1,-9,-3,3,9,4,-6,9,7,-7,3,1,5,-6,7,3,5], dtype = "int32")#candidate|1915|(160,)|const|int32
var_1916 = relay.var("var_1916", dtype = "int8", shape = ())#candidate|1916|()|var|int8
var_1917 = relay.var("var_1917", dtype = "int8", shape = (200,))#candidate|1917|(200,)|var|int8
call_1913 = relay.TupleGetItem(func_778_call(relay.reshape(var_1914.astype('int32'), [16,]), relay.reshape(const_1915.astype('int32'), [160,]), relay.reshape(var_1916.astype('int8'), []), relay.reshape(var_1917.astype('int8'), [200,]), ), 1)
call_1918 = relay.TupleGetItem(func_784_call(relay.reshape(var_1914.astype('int32'), [16,]), relay.reshape(const_1915.astype('int32'), [160,]), relay.reshape(var_1916.astype('int8'), []), relay.reshape(var_1917.astype('int8'), [200,]), ), 1)
output = relay.Tuple([call_1911,call_1913,var_1914,const_1915,var_1916,var_1917,])
output2 = relay.Tuple([call_1912,call_1918,var_1914,const_1915,var_1916,var_1917,])
func_1923 = relay.Function([var_1914,var_1916,var_1917,], output)
mod['func_1923'] = func_1923
mod = relay.transform.InferType()(mod)
var_1924 = relay.var("var_1924", dtype = "int32", shape = (16,))#candidate|1924|(16,)|var|int32
var_1925 = relay.var("var_1925", dtype = "int8", shape = ())#candidate|1925|()|var|int8
var_1926 = relay.var("var_1926", dtype = "int8", shape = (200,))#candidate|1926|(200,)|var|int8
output = func_1923(var_1924,var_1925,var_1926,)
func_1927 = relay.Function([var_1924,var_1925,var_1926,], output)
mutated_mod['func_1927'] = func_1927
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1933 = relay.var("var_1933", dtype = "float32", shape = (6, 8, 14))#candidate|1933|(6, 8, 14)|var|float32
uop_1934 = relay.acosh(var_1933.astype('float32')) # shape=(6, 8, 14)
uop_1937 = relay.rsqrt(var_1933.astype('float64')) # shape=(6, 8, 14)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_1947 = relay.TupleGetItem(func_957_call(), 0)
call_1948 = relay.TupleGetItem(func_958_call(), 0)
func_1742_call = mod.get_global_var('func_1742')
func_1744_call = mutated_mod.get_global_var('func_1744')
const_1953 = relay.const([-6,9,-4,-3,-3,-7,-4,3,3,-2,-8,-4,9,2,-7,-1], dtype = "int32")#candidate|1953|(16,)|const|int32
call_1952 = relay.TupleGetItem(func_1742_call(relay.reshape(const_1953.astype('int32'), [1, 16])), 3)
call_1954 = relay.TupleGetItem(func_1744_call(relay.reshape(const_1953.astype('int32'), [1, 16])), 3)
func_1224_call = mod.get_global_var('func_1224')
func_1228_call = mutated_mod.get_global_var('func_1228')
var_1963 = relay.var("var_1963", dtype = "int8", shape = ())#candidate|1963|()|var|int8
call_1962 = relay.TupleGetItem(func_1224_call(relay.reshape(var_1963.astype('int8'), []), relay.reshape(call_1947.astype('float32'), [2, 8, 4]), ), 1)
call_1964 = relay.TupleGetItem(func_1228_call(relay.reshape(var_1963.astype('int8'), []), relay.reshape(call_1947.astype('float32'), [2, 8, 4]), ), 1)
uop_1969 = relay.sin(uop_1937.astype('float32')) # shape=(6, 8, 14)
const_1971 = relay.const([[[-0.831684,-4.378440,-5.732942,-0.426613,-9.400677,-0.389451,1.668167,-0.153534,-1.361282,9.750721,-7.796861,-0.692748,-7.715669,-0.694301],[3.706069,2.051918,6.123400,6.892023,-8.820842,-0.839597,2.394506,5.757172,-4.142966,4.114695,2.990546,3.586569,6.021054,5.142245],[5.004436,-8.862691,2.640521,-3.190863,9.435487,4.116800,-1.341706,8.250193,-3.331662,-4.414686,-0.660352,5.776925,-4.838585,4.685042],[8.267817,2.035924,-5.293980,8.446475,4.104861,5.418954,3.557138,-5.764712,-0.712971,-7.808096,-7.613074,1.596921,-9.794381,0.007146],[-7.284058,-1.205893,4.716684,-3.141282,0.695913,-6.199299,-7.163940,-4.205800,-5.751116,3.161006,-8.698169,1.563405,-2.867566,6.935776],[-5.382116,5.971504,-4.262383,-3.670357,-2.217410,0.133223,-9.199890,-1.985357,5.675384,-9.801093,-9.543771,-9.186971,2.660620,4.620502],[8.559380,-9.939953,9.152236,-1.760336,0.357920,-8.634498,7.321196,-1.627864,2.471209,-3.450061,8.877834,-5.014419,-7.386848,-3.393047],[-3.764687,0.171389,-7.680908,9.472704,-4.259580,3.131910,-5.059292,8.104035,-2.467102,9.811683,-5.725164,-3.952454,3.826225,3.511692]],[[-8.534659,3.613125,-6.996868,-3.293213,9.033721,-9.174585,9.756595,1.209002,7.050269,0.168188,-1.135465,3.863067,5.767206,-6.157129],[-7.167680,-8.978817,8.674256,-3.287559,4.616266,3.060813,-4.671359,-2.942002,6.466444,-3.204427,-2.241718,-7.263970,-0.410709,5.758865],[-8.499162,-7.132842,-2.500076,2.724660,9.146807,4.387736,-0.482608,2.172235,-2.664199,-3.328670,5.866926,1.885829,-7.324190,1.791606],[9.438598,-7.528509,-3.449557,3.290944,-8.438115,5.743256,-5.991459,-9.950437,4.309562,5.272849,4.423066,8.752956,-8.091195,-1.696312],[4.062334,-9.996951,-6.033640,-9.486181,3.163535,3.749983,-2.298888,5.375570,1.688696,6.266032,7.003389,0.643023,-0.517153,-9.775057],[1.376363,9.552586,-1.002483,5.128726,2.229471,7.069427,9.876521,-6.425978,4.402563,-3.051618,7.395970,6.271007,9.051952,8.944145],[-8.661558,-1.269826,-2.344656,-9.567867,1.102415,5.457171,6.523921,-4.062718,-7.988936,-5.902296,-6.293898,-1.026442,-4.627892,6.697410],[-9.151315,1.101565,-6.972504,-2.389524,2.948348,9.101681,7.538022,0.544601,2.415945,2.216873,-7.906285,-7.189087,9.801048,-2.354530]],[[-7.870690,5.302081,-8.334239,9.358688,-7.552116,3.910668,-5.468915,7.811606,-1.221125,-3.435730,-5.849544,9.273404,0.667240,1.622602],[-6.196009,-2.115578,8.752965,-4.575974,-0.981664,-0.793243,2.700065,0.587745,-6.243969,3.604675,5.993486,5.609467,-9.124693,4.064872],[-5.931881,-1.912645,-6.346916,6.780104,-5.048853,-1.862674,-2.110424,7.331933,-3.959197,8.830591,1.103211,7.061255,3.829606,-6.027429],[0.375638,7.662600,8.201429,8.067184,1.401242,9.861299,-5.276343,-2.492324,5.184607,-9.889602,-5.086455,-2.055081,0.964317,3.980548],[-6.145277,-3.557801,0.243242,0.243824,3.385226,-7.348996,-7.206061,-9.820972,3.269501,2.956576,-8.895394,7.252714,3.950975,0.209415],[5.207497,7.519390,-3.761019,-2.751024,-3.511056,-5.130314,-8.064102,-9.896656,3.954794,5.130232,2.980371,8.985294,-5.121567,9.546977],[-1.396395,-7.165212,2.498376,-2.297912,4.358156,7.929205,-6.686347,6.378034,-1.353828,9.562881,-9.361273,8.352512,7.147871,-8.973676],[3.308008,-9.524758,-0.334892,2.131045,-1.555947,2.752022,-8.984753,7.674722,8.010387,7.220695,-0.142066,4.801422,2.175781,9.759135]],[[6.052848,2.845237,5.705461,-2.412207,-6.562969,6.053157,0.362371,8.506093,3.621943,9.998892,3.156305,-8.989756,3.806850,1.726945],[-7.318849,-1.466882,-7.922008,-1.038943,2.556100,1.952178,3.338334,-6.331594,2.461520,-7.390012,9.368214,7.826986,3.358343,-5.067607],[7.766119,3.443364,-4.482376,5.099896,7.056029,-2.925802,3.847099,0.580323,-6.676692,6.626803,0.545514,-7.503697,5.305324,6.079501],[-8.192984,-0.974058,5.631706,9.883424,3.805993,-4.151153,0.920742,1.687696,-3.767303,0.814321,-9.082528,3.221017,-8.878976,-3.956167],[8.764854,-0.422443,-7.311960,-0.459247,7.602049,3.767362,-8.361240,7.407228,4.980018,-1.188906,2.635371,-1.843574,0.702338,6.985273],[-8.289524,4.384767,-6.291983,9.398811,-5.558863,-5.227556,4.693855,-3.327739,-3.995568,6.234496,-2.569641,5.045581,1.760254,-1.304583],[9.696538,3.929900,1.144548,-1.140764,-8.722128,-5.746101,3.890225,-4.235569,6.260118,-8.456963,4.217310,3.081195,-6.575492,5.094126],[-2.232608,-1.277673,-0.175325,1.631661,-9.762701,5.344726,6.327749,-9.559144,-7.873383,-0.769580,5.953432,4.019398,-4.521822,6.631148]],[[-6.948732,3.486020,-2.216790,-1.192952,1.539734,-6.812090,6.377878,-4.066379,-0.336330,8.906958,-8.093667,-0.641029,2.485153,-2.212500],[-7.427681,-8.526504,-5.119891,3.393917,4.016683,3.792789,-3.336646,-9.022870,2.970065,-6.362614,2.968030,6.959475,0.028145,-6.840592],[5.833005,7.658706,-1.805621,-8.596604,1.364280,9.624326,-6.607542,7.926503,-6.034735,-8.670742,-4.908049,0.988915,2.049315,5.952087],[-3.558514,2.296476,-6.996810,1.663238,-3.563989,-0.457768,-0.764210,-9.357739,-1.232503,8.200746,2.269797,0.467916,-8.456114,-7.690467],[0.351807,8.637267,5.829700,0.013026,4.328989,-9.752184,6.115505,3.885551,-0.531901,-2.785151,3.507240,5.177606,1.528633,-7.561028],[-5.262982,5.478221,2.204251,9.435101,8.707450,-2.523447,-8.637548,-2.850568,2.193635,8.588244,2.657951,9.130676,8.558102,-9.169886],[4.467863,-4.146420,3.313017,6.382300,-7.642804,3.275865,8.041759,-7.485832,-3.150405,5.833882,-7.187737,5.924319,-7.429090,-5.006541],[0.125165,2.553016,-4.668928,-4.736952,1.226540,-0.006725,9.629158,-7.211420,1.036683,-3.888374,1.311840,-3.583245,-4.539546,-5.618318]],[[-1.672602,-3.821171,6.891694,-0.581372,4.995428,8.669648,-6.197861,1.882719,3.275436,-2.999837,-7.869800,-8.858825,0.266292,-2.768087],[-8.789926,-5.467425,3.378989,-6.387566,-1.547611,-8.445300,-5.752708,2.541402,3.891254,-9.125343,-5.335417,-6.717626,8.379501,-5.004769],[2.169353,-7.489072,0.252073,-0.786535,7.210847,9.867686,6.974401,9.866085,4.689628,-4.217570,6.831909,9.730028,1.747174,8.863988],[-4.977300,2.013459,-2.610506,2.633394,0.127266,-4.734078,2.655165,-8.711986,-2.032264,-0.541273,-5.435330,-7.456261,9.480141,4.937013],[4.485698,4.201105,2.797223,9.912005,-9.073281,4.544876,-4.257804,-7.703653,-1.913464,-7.071362,-4.774287,-3.947767,6.176520,9.440288],[5.593714,-2.476257,2.417335,-1.586286,-4.186826,-8.486268,5.334160,-4.132637,0.140314,2.767888,-3.953040,-7.078022,-6.324838,7.985594],[-1.628257,-7.414036,-9.117631,-2.802319,-5.370828,-1.850851,9.362799,1.386403,-6.519742,-4.138718,-6.638988,1.097056,-6.490537,4.933755],[3.691946,-5.029078,3.657060,5.438388,0.540276,9.512422,-6.039593,3.686864,-3.951461,-2.302763,-3.858783,9.620224,-5.587138,3.108626]]], dtype = "float32")#candidate|1971|(6, 8, 14)|const|float32
bop_1972 = relay.power(uop_1969.astype('float64'), relay.reshape(const_1971.astype('float64'), relay.shape_of(uop_1969))) # shape=(6, 8, 14)
bop_1987 = relay.floor_mod(var_1963.astype('float64'), uop_1934.astype('float64')) # shape=(6, 8, 14)
output = relay.Tuple([call_1947,call_1952,const_1953,call_1962,bop_1972,bop_1987,])
output2 = relay.Tuple([call_1948,call_1954,const_1953,call_1964,bop_1972,bop_1987,])
func_1991 = relay.Function([var_1933,var_1963,], output)
mod['func_1991'] = func_1991
mod = relay.transform.InferType()(mod)
mutated_mod['func_1991'] = func_1991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1991_call = mutated_mod.get_global_var('func_1991')
var_1993 = relay.var("var_1993", dtype = "float32", shape = (6, 8, 14))#candidate|1993|(6, 8, 14)|var|float32
var_1994 = relay.var("var_1994", dtype = "int8", shape = ())#candidate|1994|()|var|int8
call_1992 = func_1991_call(var_1993,var_1994,)
output = call_1992
func_1995 = relay.Function([var_1993,var_1994,], output)
mutated_mod['func_1995'] = func_1995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_2023 = func_718_call()
call_2024 = func_718_call()
output = call_2023
output2 = call_2024
func_2031 = relay.Function([], output)
mod['func_2031'] = func_2031
mod = relay.transform.InferType()(mod)
mutated_mod['func_2031'] = func_2031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mutated_mod.get_global_var('func_2031')
call_2032 = func_2031_call()
output = call_2032
func_2033 = relay.Function([], output)
mutated_mod['func_2033'] = func_2033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_2044 = func_1055_call()
call_2045 = func_1055_call()
output = call_2044
output2 = call_2045
func_2046 = relay.Function([], output)
mod['func_2046'] = func_2046
mod = relay.transform.InferType()(mod)
output = func_2046()
func_2047 = relay.Function([], output)
mutated_mod['func_2047'] = func_2047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1266_call = mod.get_global_var('func_1266')
func_1267_call = mutated_mod.get_global_var('func_1267')
call_2057 = relay.TupleGetItem(func_1266_call(), 0)
call_2058 = relay.TupleGetItem(func_1267_call(), 0)
uop_2077 = relay.log(call_2057.astype('float64')) # shape=(2, 8, 4)
uop_2079 = relay.log(call_2058.astype('float64')) # shape=(2, 8, 4)
output = relay.Tuple([uop_2077,])
output2 = relay.Tuple([uop_2079,])
func_2099 = relay.Function([], output)
mod['func_2099'] = func_2099
mod = relay.transform.InferType()(mod)
mutated_mod['func_2099'] = func_2099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2099_call = mutated_mod.get_global_var('func_2099')
call_2100 = func_2099_call()
output = call_2100
func_2101 = relay.Function([], output)
mutated_mod['func_2101'] = func_2101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1848_call = mod.get_global_var('func_1848')
func_1849_call = mutated_mod.get_global_var('func_1849')
call_2128 = relay.TupleGetItem(func_1848_call(), 0)
call_2129 = relay.TupleGetItem(func_1849_call(), 0)
output = call_2128
output2 = call_2129
func_2132 = relay.Function([], output)
mod['func_2132'] = func_2132
mod = relay.transform.InferType()(mod)
mutated_mod['func_2132'] = func_2132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2132_call = mutated_mod.get_global_var('func_2132')
call_2133 = func_2132_call()
output = call_2133
func_2134 = relay.Function([], output)
mutated_mod['func_2134'] = func_2134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1848_call = mod.get_global_var('func_1848')
func_1849_call = mutated_mod.get_global_var('func_1849')
call_2179 = relay.TupleGetItem(func_1848_call(), 0)
call_2180 = relay.TupleGetItem(func_1849_call(), 0)
func_1923_call = mod.get_global_var('func_1923')
func_1927_call = mutated_mod.get_global_var('func_1927')
var_2189 = relay.var("var_2189", dtype = "int32", shape = (1, 16))#candidate|2189|(1, 16)|var|int32
var_2190 = relay.var("var_2190", dtype = "int8", shape = ())#candidate|2190|()|var|int8
const_2191 = relay.const([4,4,9,8,3,-5,-7,-6,-8,9,-7,-2,6,-5,4,10,2,-5,-5,3,10,-3,-2,-6,-7,10,8,2,-9,-6,7,-2,-9,1,7,4,-4,6,5,8,7,-6,9,8,-7,2,10,6,-10,3,-3,-7,-3,2,-5,8,8,10,3,7,2,-5,-3,2,-8,-1,2,-7,-2,-3,-9,2,6,-3,10,9,1,-6,3,-10,-3,-3,10,9,8,1,-4,3,5,-7,7,-6,-9,3,-10,-4,-3,-9,-6,-4,-2,-10,-8,-4,-8,-7,-8,3,7,1,8,-2,4,-5,2,5,-6,8,-9,-6,-5,3,-6,-1,4,-10,-9,7,-6,6,-4,9,7,4,2,-6,-3,-8,-7,1,3,6,-6,5,-5,-9,1,7,-7,-7,-2,-4,4,-3,-3,2,6,5,-3,3,3,-7,1,-4,6,7,-6,3,7,1,-10,5,3,9,2,5,5,-10,7,-5,9,1,7,5,9,1,9,5,-7,9,8,5,-6,-10,-2,6,-10,-7,2,-8], dtype = "int8")#candidate|2191|(200,)|const|int8
call_2188 = relay.TupleGetItem(func_1923_call(relay.reshape(var_2189.astype('int32'), [16,]), relay.reshape(var_2190.astype('int8'), []), relay.reshape(const_2191.astype('int8'), [200,]), ), 0)
call_2192 = relay.TupleGetItem(func_1927_call(relay.reshape(var_2189.astype('int32'), [16,]), relay.reshape(var_2190.astype('int8'), []), relay.reshape(const_2191.astype('int8'), [200,]), ), 0)
uop_2206 = relay.acosh(const_2191.astype('float64')) # shape=(200,)
func_2132_call = mod.get_global_var('func_2132')
func_2134_call = mutated_mod.get_global_var('func_2134')
call_2218 = func_2132_call()
call_2219 = func_2132_call()
func_2132_call = mod.get_global_var('func_2132')
func_2134_call = mutated_mod.get_global_var('func_2134')
call_2223 = func_2132_call()
call_2224 = func_2132_call()
func_1421_call = mod.get_global_var('func_1421')
func_1424_call = mutated_mod.get_global_var('func_1424')
var_2226 = relay.var("var_2226", dtype = "uint16", shape = (448,))#candidate|2226|(448,)|var|uint16
call_2225 = relay.TupleGetItem(func_1421_call(relay.reshape(var_2226.astype('uint16'), [14, 2, 16])), 0)
call_2227 = relay.TupleGetItem(func_1424_call(relay.reshape(var_2226.astype('uint16'), [14, 2, 16])), 0)
func_708_call = mod.get_global_var('func_708')
func_710_call = mutated_mod.get_global_var('func_710')
call_2239 = relay.TupleGetItem(func_708_call(), 0)
call_2240 = relay.TupleGetItem(func_710_call(), 0)
output = relay.Tuple([call_2179,call_2188,var_2189,var_2190,uop_2206,call_2218,call_2223,call_2225,var_2226,call_2239,])
output2 = relay.Tuple([call_2180,call_2192,var_2189,var_2190,uop_2206,call_2219,call_2224,call_2227,var_2226,call_2240,])
func_2243 = relay.Function([var_2189,var_2190,var_2226,], output)
mod['func_2243'] = func_2243
mod = relay.transform.InferType()(mod)
mutated_mod['func_2243'] = func_2243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2243_call = mutated_mod.get_global_var('func_2243')
var_2245 = relay.var("var_2245", dtype = "int32", shape = (1, 16))#candidate|2245|(1, 16)|var|int32
var_2246 = relay.var("var_2246", dtype = "int8", shape = ())#candidate|2246|()|var|int8
var_2247 = relay.var("var_2247", dtype = "uint16", shape = (448,))#candidate|2247|(448,)|var|uint16
call_2244 = func_2243_call(var_2245,var_2246,var_2247,)
output = call_2244
func_2248 = relay.Function([var_2245,var_2246,var_2247,], output)
mutated_mod['func_2248'] = func_2248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2046_call = mod.get_global_var('func_2046')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_2347 = func_2046_call()
call_2348 = func_2046_call()
output = call_2347
output2 = call_2348
func_2359 = relay.Function([], output)
mod['func_2359'] = func_2359
mod = relay.transform.InferType()(mod)
output = func_2359()
func_2360 = relay.Function([], output)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_2363 = func_718_call()
call_2364 = func_718_call()
func_1224_call = mod.get_global_var('func_1224')
func_1228_call = mutated_mod.get_global_var('func_1228')
const_2375 = relay.const(3, dtype = "int8")#candidate|2375|()|const|int8
call_2374 = relay.TupleGetItem(func_1224_call(relay.reshape(const_2375.astype('int8'), []), relay.reshape(call_2363.astype('float32'), [2, 8, 4]), ), 1)
call_2376 = relay.TupleGetItem(func_1228_call(relay.reshape(const_2375.astype('int8'), []), relay.reshape(call_2363.astype('float32'), [2, 8, 4]), ), 1)
output = relay.Tuple([call_2363,call_2374,const_2375,])
output2 = relay.Tuple([call_2364,call_2376,const_2375,])
func_2384 = relay.Function([], output)
mod['func_2384'] = func_2384
mod = relay.transform.InferType()(mod)
mutated_mod['func_2384'] = func_2384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2384_call = mutated_mod.get_global_var('func_2384')
call_2385 = func_2384_call()
output = call_2385
func_2386 = relay.Function([], output)
mutated_mod['func_2386'] = func_2386
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2389 = relay.var("var_2389", dtype = "float64", shape = (4, 8, 12))#candidate|2389|(4, 8, 12)|var|float64
uop_2390 = relay.sin(var_2389.astype('float64')) # shape=(4, 8, 12)
output = uop_2390
output2 = uop_2390
func_2404 = relay.Function([var_2389,], output)
mod['func_2404'] = func_2404
mod = relay.transform.InferType()(mod)
var_2405 = relay.var("var_2405", dtype = "float64", shape = (4, 8, 12))#candidate|2405|(4, 8, 12)|var|float64
output = func_2404(var_2405)
func_2406 = relay.Function([var_2405], output)
mutated_mod['func_2406'] = func_2406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_2408 = relay.TupleGetItem(func_957_call(), 0)
call_2409 = relay.TupleGetItem(func_958_call(), 0)
func_1462_call = mod.get_global_var('func_1462')
func_1465_call = mutated_mod.get_global_var('func_1465')
const_2420 = relay.const([[-3.896821,-5.085616,3.836917,-1.705034,9.006727,-6.502293,7.554392,9.827105,3.988777,4.366176,-1.486022,4.135877,-2.448434,-8.214221,3.526472,-4.483631,5.672298,9.869524,-8.710945,1.595644,5.472479,-0.731694,-5.613932,-9.886885,6.725660,1.302677,1.584327,-0.218754,-3.214359,-5.370175,2.155481,3.925086,8.753683,2.210779,-4.961725,0.794524,-6.906230,-4.218264,7.695578,-8.722385,-5.533868,-2.883197,4.383332,-6.300584,8.239343,7.321036,4.247951,-7.312943,0.156981,-8.031031,-3.052690,0.463408,3.782949,-3.686167,-4.277143,0.092968,-4.918348,-9.441460,-5.491471,2.060964,3.482390,-6.149194,5.499559,4.980918,-7.641220,5.994550,-2.793287,2.891488,-8.613108,-5.588380,1.367390,-1.257101,-1.114701,7.690974,8.689064,-6.065653,4.552895,6.037610,5.758508,1.142164,-6.176917,2.752903,3.852241,-6.579929,-4.952534,1.163849,-2.972486,8.456273,-5.859812,1.654180,-4.338439,2.953039,-8.664375,-4.634242,2.883524,3.201054,-1.651084,-2.206754,6.728220,-7.515010,-5.103797,1.585890,1.275992,9.997633,3.188734,7.864316,-8.733861,8.935090,5.813748,5.096273,5.439932,-9.389431,1.513083,-6.051758,9.215146,-3.091890,-9.197906,-1.769987,-1.187879,9.601380,-4.868870,5.672519,2.851307,4.787621,6.281979,-2.103019,7.694589,-1.219614,0.602584,6.869225,2.106838,-8.828908,-4.979393,7.762217,-7.345281,-0.075552,6.349805,-8.271688,5.296550,5.894708,-1.383762,2.216445,-7.798128,-0.974987,-8.149228,-7.451718,0.604424,3.952442,1.521539,-0.268392,-9.526593,-3.026928,2.936034,-3.201900,-4.062658,1.897284,7.472755,-1.645058,-2.696507,-5.958150,7.664282,8.852981,2.139326,-1.967610,6.260196,5.632571,5.531474,-0.794319,-4.957200,1.103768,-7.551368,6.237102,-0.136495,-5.252480,-9.475535,8.376579,1.162351,-6.564603,-4.180150,-4.300940],[8.090882,6.417891,7.257373,7.720295,-0.363217,1.550994,3.079656,3.545315,-1.747355,2.632131,-4.533398,-1.877804,3.676639,-6.895673,2.122669,9.087876,-0.118772,-7.893831,-0.858804,6.451307,-5.196484,-3.605084,4.923367,9.588859,1.819470,-0.013758,-0.987174,3.320879,7.993628,8.829040,-7.911206,-6.006632,4.427450,2.794066,-6.236084,-6.222503,0.397877,0.255985,-1.794638,-6.996793,1.707040,8.282107,-1.169382,6.459122,9.701379,-8.303480,2.302776,-9.428320,4.693063,1.510956,4.031179,7.345448,-3.277004,2.590546,9.742254,-4.704794,2.381665,-7.306545,-6.469367,8.633800,-6.173596,-3.468106,-8.618669,-0.850385,-2.575199,-1.967252,-9.338476,-1.362999,-0.981548,0.512720,8.139764,-7.090109,-4.837027,-2.657584,-9.406561,-2.465607,-3.278938,-3.594448,1.204541,-9.292920,-1.597617,9.903529,-1.264597,2.508715,-6.552981,0.144599,-9.409163,-3.186533,-4.182937,-3.032688,-8.253159,-8.195698,9.546787,-0.712994,7.100899,-0.563314,8.040424,-4.513554,5.078660,-8.712979,0.939065,1.859534,7.221194,-6.391304,7.234022,-4.524501,0.134886,-6.653337,7.002464,7.431901,2.920813,2.302298,-2.015497,0.796400,0.196538,2.159850,0.284165,9.350819,-1.032624,-4.348471,-8.368558,5.768025,4.267367,-8.002543,-9.014057,-6.654716,3.847387,-8.228727,0.297090,4.151676,4.882147,2.925030,8.453230,5.883353,-4.821456,4.353935,-3.764645,-6.715449,-0.217010,4.611020,7.845857,3.046689,9.183757,-2.965617,5.764963,8.238103,-1.927329,6.710726,5.312894,4.503689,-4.413877,-8.578231,6.719438,0.369350,2.310872,5.936479,-7.819005,0.917691,-5.607316,-4.023278,9.230330,6.044702,1.908637,-6.798244,7.380994,-6.396793,-9.841233,6.644877,-1.751859,-7.433920,4.032066,-0.853930,-1.986729,3.007320,5.409566,-8.072367,2.002266,-5.554707,-8.719504,-2.695670]], dtype = "float64")#candidate|2420|(2, 180)|const|float64
call_2419 = relay.TupleGetItem(func_1462_call(relay.reshape(const_2420.astype('float64'), [6, 6, 10]), relay.reshape(call_2408.astype('uint32'), [8, 8]), ), 0)
call_2421 = relay.TupleGetItem(func_1465_call(relay.reshape(const_2420.astype('float64'), [6, 6, 10]), relay.reshape(call_2408.astype('uint32'), [8, 8]), ), 0)
output = relay.Tuple([call_2408,call_2419,const_2420,])
output2 = relay.Tuple([call_2409,call_2421,const_2420,])
func_2429 = relay.Function([], output)
mod['func_2429'] = func_2429
mod = relay.transform.InferType()(mod)
output = func_2429()
func_2430 = relay.Function([], output)
mutated_mod['func_2430'] = func_2430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_2470 = func_2359_call()
call_2471 = func_2359_call()
func_2132_call = mod.get_global_var('func_2132')
func_2134_call = mutated_mod.get_global_var('func_2134')
call_2474 = func_2132_call()
call_2475 = func_2132_call()
output = relay.Tuple([call_2470,call_2474,])
output2 = relay.Tuple([call_2471,call_2475,])
func_2479 = relay.Function([], output)
mod['func_2479'] = func_2479
mod = relay.transform.InferType()(mod)
mutated_mod['func_2479'] = func_2479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2479_call = mutated_mod.get_global_var('func_2479')
call_2480 = func_2479_call()
output = call_2480
func_2481 = relay.Function([], output)
mutated_mod['func_2481'] = func_2481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2509 = relay.var("var_2509", dtype = "uint64", shape = ())#candidate|2509|()|var|uint64
var_2510 = relay.var("var_2510", dtype = "uint64", shape = (5, 3, 3))#candidate|2510|(5, 3, 3)|var|uint64
bop_2511 = relay.logical_xor(var_2509.astype('uint64'), var_2510.astype('uint64')) # shape=(5, 3, 3)
output = bop_2511
output2 = bop_2511
func_2516 = relay.Function([var_2509,var_2510,], output)
mod['func_2516'] = func_2516
mod = relay.transform.InferType()(mod)
mutated_mod['func_2516'] = func_2516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2516_call = mutated_mod.get_global_var('func_2516')
var_2518 = relay.var("var_2518", dtype = "uint64", shape = ())#candidate|2518|()|var|uint64
var_2519 = relay.var("var_2519", dtype = "uint64", shape = (5, 3, 3))#candidate|2519|(5, 3, 3)|var|uint64
call_2517 = func_2516_call(var_2518,var_2519,)
output = call_2517
func_2520 = relay.Function([var_2518,var_2519,], output)
mutated_mod['func_2520'] = func_2520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_2522 = relay.TupleGetItem(func_957_call(), 0)
call_2523 = relay.TupleGetItem(func_958_call(), 0)
output = call_2522
output2 = call_2523
func_2597 = relay.Function([], output)
mod['func_2597'] = func_2597
mod = relay.transform.InferType()(mod)
mutated_mod['func_2597'] = func_2597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2597_call = mutated_mod.get_global_var('func_2597')
call_2598 = func_2597_call()
output = call_2598
func_2599 = relay.Function([], output)
mutated_mod['func_2599'] = func_2599
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2600 = relay.var("var_2600", dtype = "float64", shape = (4, 5, 13))#candidate|2600|(4, 5, 13)|var|float64
uop_2601 = relay.asin(var_2600.astype('float64')) # shape=(4, 5, 13)
output = relay.Tuple([uop_2601,])
output2 = relay.Tuple([uop_2601,])
func_2610 = relay.Function([var_2600,], output)
mod['func_2610'] = func_2610
mod = relay.transform.InferType()(mod)
var_2611 = relay.var("var_2611", dtype = "float64", shape = (4, 5, 13))#candidate|2611|(4, 5, 13)|var|float64
output = func_2610(var_2611)
func_2612 = relay.Function([var_2611], output)
mutated_mod['func_2612'] = func_2612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2099_call = mod.get_global_var('func_2099')
func_2101_call = mutated_mod.get_global_var('func_2101')
call_2647 = relay.TupleGetItem(func_2099_call(), 0)
call_2648 = relay.TupleGetItem(func_2101_call(), 0)
output = call_2647
output2 = call_2648
func_2651 = relay.Function([], output)
mod['func_2651'] = func_2651
mod = relay.transform.InferType()(mod)
mutated_mod['func_2651'] = func_2651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2651_call = mutated_mod.get_global_var('func_2651')
call_2652 = func_2651_call()
output = call_2652
func_2653 = relay.Function([], output)
mutated_mod['func_2653'] = func_2653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1857_call = mod.get_global_var('func_1857')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_2657 = func_1857_call()
call_2658 = func_1857_call()
func_1462_call = mod.get_global_var('func_1462')
func_1465_call = mutated_mod.get_global_var('func_1465')
const_2663 = relay.const([8.115840,-6.310504,-0.251566,-6.200143,-1.358245,-1.526995,-9.247800,-4.770820,-5.411797,5.079680,-9.850114,-4.752254,-4.657004,5.600592,9.232803,-3.255073,4.559307,-9.328693,4.147678,-0.034423,-3.021193,6.725613,-7.487527,5.759397,6.964753,4.741387,-8.552993,0.175483,2.081633,-5.574194,-4.527965,-1.173403,3.997453,2.498235,3.167353,-5.109394,-2.396260,-7.449626,6.089647,7.343257,-4.455979,6.089787,9.774041,-1.560861,5.279220,0.823655,8.019836,0.100521,9.204123,5.362878,4.929010,-8.222727,-7.718010,-6.808811,-7.724414,-3.009842,-8.511902,6.118324,-4.719181,-1.214127,-2.541239,1.092106,2.146943,-8.384111,8.153884,8.558272,2.912817,5.174041,-9.645719,-3.700509,4.733054,-1.921717,-8.158951,5.398594,9.481869,-8.850372,-2.899385,8.574260,7.713018,-3.493016,-9.627914,6.898256,9.972224,5.678086,-2.344800,-6.857096,-5.071275,1.532705,-1.264332,-9.518470,-0.242269,4.520605,-7.165694,9.500456,-0.985878,1.904926,5.315455,-8.236067,3.918409,7.978386,9.926633,6.472617,-9.153741,-6.733792,-7.057983,-9.081258,-9.728836,1.404043,-0.253642,-8.204438,-0.802325,9.997239,-4.925130,-6.492542,0.621186,7.271341,6.172950,4.246433,1.892554,-7.983002,-8.205523,-4.084602,-3.355209,6.514338,-4.545808,9.290195,6.327147,9.147560,-8.416852,6.394828,4.290665,2.417703,-2.718090,-8.584222,-7.278825,0.959040,6.751602,4.412131,4.085687,-3.890053,-8.990857,-1.516966,6.144844,9.207111,5.213782,1.410347,7.419527,0.046273,2.441138,6.712690,-3.766472,-1.204031,2.039918,5.328686,5.654999,-1.881877,4.027586,8.626271,-0.323967,-0.184814,-8.552720,-6.897010,-9.292277,6.237638,1.774867,-7.811362,2.700752,9.480975,-5.641128,2.993665,4.389517,-5.673607,-3.987087,0.995444,-0.225485,-8.776840,7.296708,2.743621,-9.070131,-9.756252,1.297437,6.663138,2.395306,0.966954,4.231035,4.109302,9.698202,6.158486,-9.087744,-8.415062,-1.145834,8.245755,-0.098250,-6.003149,4.566642,-6.389269,5.045570,0.807869,1.263918,-1.951858,7.143250,2.113806,2.745281,-4.710479,9.366192,8.473427,8.674596,2.092048,0.738515,-1.652862,-8.438321,8.169564,-0.581864,8.676044,-6.247268,-1.465063,8.160597,-3.902679,-1.753692,-1.818892,0.328272,4.596939,-6.671276,-9.234381,-3.995236,-3.977666,-3.398666,-9.965703,-8.546056,-3.706331,-6.706029,-9.972247,-1.377082,-1.587535,6.108289,-8.140411,-6.259331,0.994975,-2.531594,-1.287543,-5.266120,-5.531211,1.717016,3.971948,-0.824012,-7.689068,-5.204127,-5.896845,2.309267,3.575521,-9.475317,6.915606,-9.073496,9.217971,2.673625,5.909093,6.385365,-0.529820,8.081684,-5.561085,9.127156,-0.983385,-2.643291,-4.588895,0.178996,-7.704440,6.963491,0.743814,5.182111,-7.879051,-9.350251,-5.092531,7.109346,-5.069388,9.007850,-4.244271,2.597135,-9.447739,-6.294718,6.063129,9.330309,7.602270,-9.879519,-0.289740,1.684750,-9.738432,-7.733975,1.480223,5.362329,-2.188258,9.976976,9.300269,3.108753,-4.674058,-7.736963,-3.770795,6.186844,-2.359450,-7.408872,7.991606,5.595320,0.495764,4.832961,-8.604441,7.696384,2.381353,9.506970,2.904989,-1.055569,-9.814398,-6.990902,-1.102028,-4.594841,2.344780,9.529441,8.630515,-6.963566,3.941779,4.036574,-7.695532,-5.362656,0.906831,-8.574641,0.907062,-7.841582,8.414601,-7.297638,1.381345,-8.959459,5.264963,9.205907,-2.124125,7.953521,2.830012,9.719217,1.916946,0.031292,-0.594985,-3.519385,4.081404,3.562367,1.742890,-9.590445,1.322598,3.413411,4.448674,4.138458,-7.134629,4.463431,9.008293,9.826248,-7.139204,-6.200105,-1.185863,-7.992099,4.838085,-4.790518,6.591121,4.791782,6.678363], dtype = "float64")#candidate|2663|(360,)|const|float64
call_2662 = relay.TupleGetItem(func_1462_call(relay.reshape(const_2663.astype('float64'), [6, 6, 10]), relay.reshape(call_2657.astype('uint32'), [8, 8]), ), 2)
call_2664 = relay.TupleGetItem(func_1465_call(relay.reshape(const_2663.astype('float64'), [6, 6, 10]), relay.reshape(call_2657.astype('uint32'), [8, 8]), ), 2)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_2667 = func_2359_call()
call_2668 = func_2359_call()
output = relay.Tuple([call_2657,call_2662,const_2663,call_2667,])
output2 = relay.Tuple([call_2658,call_2664,const_2663,call_2668,])
func_2671 = relay.Function([], output)
mod['func_2671'] = func_2671
mod = relay.transform.InferType()(mod)
mutated_mod['func_2671'] = func_2671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2671_call = mutated_mod.get_global_var('func_2671')
call_2672 = func_2671_call()
output = call_2672
func_2673 = relay.Function([], output)
mutated_mod['func_2673'] = func_2673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_2682 = func_1055_call()
call_2683 = func_1055_call()
output = relay.Tuple([call_2682,])
output2 = relay.Tuple([call_2683,])
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
var_2695 = relay.var("var_2695", dtype = "uint32", shape = (10, 9, 11))#candidate|2695|(10, 9, 11)|var|uint32
var_2696 = relay.var("var_2696", dtype = "uint32", shape = (10, 9, 11))#candidate|2696|(10, 9, 11)|var|uint32
bop_2697 = relay.bitwise_or(var_2695.astype('uint32'), relay.reshape(var_2696.astype('uint32'), relay.shape_of(var_2695))) # shape=(10, 9, 11)
uop_2702 = relay.rsqrt(bop_2697.astype('float32')) # shape=(10, 9, 11)
output = relay.Tuple([uop_2702,])
output2 = relay.Tuple([uop_2702,])
func_2704 = relay.Function([var_2695,var_2696,], output)
mod['func_2704'] = func_2704
mod = relay.transform.InferType()(mod)
var_2705 = relay.var("var_2705", dtype = "uint32", shape = (10, 9, 11))#candidate|2705|(10, 9, 11)|var|uint32
var_2706 = relay.var("var_2706", dtype = "uint32", shape = (10, 9, 11))#candidate|2706|(10, 9, 11)|var|uint32
output = func_2704(var_2705,var_2706,)
func_2707 = relay.Function([var_2705,var_2706,], output)
mutated_mod['func_2707'] = func_2707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_2718 = func_2031_call()
call_2719 = func_2031_call()
output = relay.Tuple([call_2718,])
output2 = relay.Tuple([call_2719,])
func_2723 = relay.Function([], output)
mod['func_2723'] = func_2723
mod = relay.transform.InferType()(mod)
mutated_mod['func_2723'] = func_2723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2723_call = mutated_mod.get_global_var('func_2723')
call_2724 = func_2723_call()
output = call_2724
func_2725 = relay.Function([], output)
mutated_mod['func_2725'] = func_2725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2755 = relay.TupleGetItem(func_1758_call(), 0)
call_2756 = relay.TupleGetItem(func_1760_call(), 0)
func_1857_call = mod.get_global_var('func_1857')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_2762 = func_1857_call()
call_2763 = func_1857_call()
output = relay.Tuple([call_2755,call_2762,])
output2 = relay.Tuple([call_2756,call_2763,])
func_2767 = relay.Function([], output)
mod['func_2767'] = func_2767
mod = relay.transform.InferType()(mod)
output = func_2767()
func_2768 = relay.Function([], output)
mutated_mod['func_2768'] = func_2768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2671_call = mod.get_global_var('func_2671')
func_2673_call = mutated_mod.get_global_var('func_2673')
call_2779 = relay.TupleGetItem(func_2671_call(), 1)
call_2780 = relay.TupleGetItem(func_2673_call(), 1)
func_1462_call = mod.get_global_var('func_1462')
func_1465_call = mutated_mod.get_global_var('func_1465')
var_2789 = relay.var("var_2789", dtype = "float64", shape = (360,))#candidate|2789|(360,)|var|float64
call_2788 = relay.TupleGetItem(func_1462_call(relay.reshape(var_2789.astype('float64'), [6, 6, 10]), relay.reshape(call_2779.astype('uint32'), [8, 8]), ), 2)
call_2790 = relay.TupleGetItem(func_1465_call(relay.reshape(var_2789.astype('float64'), [6, 6, 10]), relay.reshape(call_2779.astype('uint32'), [8, 8]), ), 2)
func_1923_call = mod.get_global_var('func_1923')
func_1927_call = mutated_mod.get_global_var('func_1927')
const_2798 = relay.const([-7,1,9,8,-4,1,-3,9,-9,3,-5,7,10,2,-10,-6], dtype = "int32")#candidate|2798|(16,)|const|int32
var_2799 = relay.var("var_2799", dtype = "int8", shape = ())#candidate|2799|()|var|int8
const_2800 = relay.const([[3,-1,6,6,-1,1,1,-6,-10,10,2,1,8,10,-5,5,10,-4,7,6,-6,10,1,-4,8,9,7,-1,-9,9,3,1,-9,8,4,-6,10,-8,3,-2],[-7,10,-4,2,-5,-7,-4,-2,3,9,-5,-8,4,-8,1,7,-4,3,-1,1,-6,4,7,3,7,5,-8,9,-2,-8,-8,10,-3,9,-10,9,9,5,9,-5],[-9,-8,-5,8,3,-2,-10,-4,7,-8,6,-4,1,2,-7,-8,-7,-3,5,-2,9,3,8,4,-3,-4,-10,-5,-6,-4,-3,-9,-1,5,-6,-8,2,-6,-9,6],[3,-10,-6,5,-3,7,3,8,-10,2,3,3,-9,6,1,9,-1,8,-5,3,4,-8,6,1,-1,6,-10,1,-7,-7,-10,2,-5,-1,5,-2,4,6,-8,-9],[-7,-4,3,-4,10,-1,-8,-4,-5,-3,10,9,-5,-7,-9,1,9,-3,-1,-5,10,3,-8,1,3,4,-1,-7,-10,-1,-1,5,10,-4,-6,-1,-4,-4,-1,-6]], dtype = "int8")#candidate|2800|(5, 40)|const|int8
call_2797 = relay.TupleGetItem(func_1923_call(relay.reshape(const_2798.astype('int32'), [16,]), relay.reshape(var_2799.astype('int8'), []), relay.reshape(const_2800.astype('int8'), [200,]), ), 5)
call_2801 = relay.TupleGetItem(func_1927_call(relay.reshape(const_2798.astype('int32'), [16,]), relay.reshape(var_2799.astype('int8'), []), relay.reshape(const_2800.astype('int8'), [200,]), ), 5)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_2804 = func_718_call()
call_2805 = func_718_call()
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2806 = relay.TupleGetItem(func_1758_call(), 1)
call_2807 = relay.TupleGetItem(func_1760_call(), 1)
func_2610_call = mod.get_global_var('func_2610')
func_2612_call = mutated_mod.get_global_var('func_2612')
const_2809 = relay.const([-6.066348,-0.409627,4.519635,-3.556234,4.177052,-8.100377,8.654130,9.576649,9.365712,-3.110822,-4.640634,-3.327094,6.565843,-7.111134,-1.216995,-2.729410,1.084734,-4.028736,0.184510,-6.001685,-0.818409,-0.538311,-4.072037,-2.706585,-6.103993,8.527519,-5.666492,3.249428,6.187345,-3.566034,-7.849270,-3.858296,-6.738551,-2.047137,-7.111712,-1.461272,6.298733,-6.418469,-7.523167,-2.886154,4.674573,-5.464415,9.694314,2.242022,7.373972,2.494981,-5.452520,7.154415,-1.026344,4.920438,0.977519,6.975204,-5.170528,-9.787931,3.438143,2.405399,2.103678,-4.537408,-9.914695,7.606087,-3.953509,0.878410,0.863066,5.412506,-3.697691,-7.496472,-1.859403,-3.858070,8.468097,-8.959085,3.525301,-5.749661,5.131309,-5.173812,-6.142977,3.225469,-5.529145,-2.624305,-0.576421,4.933350,-3.107145,-7.586223,3.238641,1.462211,9.304240,7.417589,7.311876,3.741299,6.143892,-4.092970,-7.530357,-2.277479,-4.872471,-0.637195,-2.163552,7.249265,7.874427,0.015141,9.142919,1.803163,-5.591805,4.798616,-8.707066,-6.649784,-6.648906,-2.226437,9.918265,6.533756,0.170207,-8.419199,7.808690,-4.603033,6.219661,-4.213426,-0.215939,7.804855,-2.586075,-1.136238,-2.203174,-3.255605,-4.054286,4.612983,4.891389,1.002625,-0.400903,-0.347335,-5.450595,-5.514806,9.044542,-6.458223,-6.204442,-4.335477,-8.897855,-9.569594,-2.394646,-7.504853,1.029922,-9.097623,-4.353884,1.648123,1.128808,8.331407,-7.692150,6.546144,-7.040587,4.064580,5.868556,5.831829,-7.287718,-0.982070,2.735150,0.647336,-8.970480,0.713301,-4.827692,4.057652,0.537953,6.779347,-4.308114,3.926756,-2.405346,-7.523880,-4.832582,9.988029,6.077938,2.691071,-4.597900,6.819717,-0.246017,-7.716702,5.450966,-2.746384,-6.950070,-7.190750,-8.426074,7.588881,-2.518524,3.005768,0.916559,5.226674,-3.903823,5.308138,-1.380987,-4.865928,-6.642061,7.982161,-4.432630,-6.921872,0.607745,-7.843220,-2.069398,-6.761665,2.878692,8.723222,-2.969181,6.174530,-2.895073,-7.959718,5.895403,4.753179,0.124517,9.024995,7.438224,-1.419382,-5.038892,-1.079565,-9.187449,2.436015,-5.182765,-7.962221,7.168825,-2.779568,3.113498,-3.642980,9.816923,-7.502031,-0.341138,-2.161767,2.623364,-8.548902,0.021556,-3.302543,8.313248,8.716870,-1.367562,8.424359,1.986932,4.774706,-5.435380,1.010355,-7.898787,-3.388508,7.046271,-6.449018,2.895799,-7.154645,2.662899,-7.339601,-7.346221,7.116906,8.219919,6.684573,-5.725946,7.901398,-1.762085,-2.539923,-8.173872,-2.259685,6.990249,-2.539563,0.152717,-1.430622,6.736602,-0.652975,-0.643414,3.544278,-2.495837,2.436953,5.948482,1.343661], dtype = "float64")#candidate|2809|(260,)|const|float64
call_2808 = relay.TupleGetItem(func_2610_call(relay.reshape(const_2809.astype('float64'), [4, 5, 13])), 0)
call_2810 = relay.TupleGetItem(func_2612_call(relay.reshape(const_2809.astype('float64'), [4, 5, 13])), 0)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_2830 = func_1055_call()
call_2831 = func_1055_call()
uop_2835 = relay.sinh(const_2800.astype('float64')) # shape=(5, 40)
const_2837 = relay.const([[0.524754,6.345793,6.480116,7.048166,4.407707,-6.585748,8.124226,-8.321235,8.896302,3.257782,-0.617846,-0.420228,8.560597,1.229898,-4.878069,1.208078,-8.717168,-8.526648,-1.009052,4.376342,-1.505256,-6.827860,1.317094,1.229799,2.859759,7.257871,-8.457508,0.742088,-3.083578,2.427215,-8.487113,-4.740502,7.093080,-9.249075,0.210012,5.621899,7.890799,1.140744,-6.101362,3.263515],[-9.703366,6.216719,2.779756,-6.733588,9.996106,-3.280212,7.392911,2.156935,4.782954,-6.149378,9.930817,-0.440107,5.012000,0.598677,8.339043,7.113343,1.003766,-8.058076,-6.253078,9.948758,-3.455631,9.934752,-4.965826,-9.809131,-1.998884,-1.091079,-2.748132,-1.429354,8.596906,6.733680,1.423535,-7.072118,5.406406,4.880358,4.196610,-1.449047,-5.974789,1.269446,-2.329841,-2.207801],[-3.546920,-2.707847,-9.813739,3.776212,6.146747,-9.995496,9.270891,2.536993,7.715340,-8.263771,4.152408,-5.048427,-7.232188,5.658618,8.978890,4.220240,-6.618689,-5.713916,5.300099,-0.448323,-2.638080,6.414985,0.193606,-0.920300,4.505998,-3.390060,9.994913,-0.099298,-3.358766,-3.983610,6.342639,-8.948322,-7.014992,-6.158097,-2.631686,-1.953170,5.792746,-7.820726,-6.818248,2.607050],[-1.445058,9.883314,-4.696335,5.318418,5.659399,-4.208942,-4.064087,-3.330267,5.809457,-5.105145,-7.705260,-3.123847,-7.207317,-6.836737,-3.997706,-2.399218,7.941669,-2.655421,4.152653,1.900746,-8.382953,3.400903,-2.838414,2.435853,8.107929,9.317139,-5.468804,3.299228,-5.653266,2.661569,-3.231213,1.332215,0.445216,2.009771,-0.145933,6.212160,2.625516,3.740372,0.703615,9.335915],[-5.842396,-3.810255,9.636311,0.148464,6.161384,-0.777347,-6.650594,-8.282011,3.034762,-5.215886,-6.526929,-4.571345,-4.003030,6.820764,-0.942651,-8.632786,8.269627,8.502486,3.788786,-7.083351,-1.317523,-6.180102,9.134245,-5.632885,-9.583350,-8.005305,7.031575,-0.330110,-4.403116,6.078154,4.298125,2.160652,-6.673281,6.396938,6.837155,-3.771643,-0.786392,-1.107676,6.562577,-1.618800]], dtype = "float64")#candidate|2837|(5, 40)|const|float64
bop_2838 = relay.floor_mod(uop_2835.astype('float64'), relay.reshape(const_2837.astype('float64'), relay.shape_of(uop_2835))) # shape=(5, 40)
output = relay.Tuple([call_2779,call_2788,var_2789,call_2797,const_2798,var_2799,call_2804,call_2806,call_2808,const_2809,call_2830,bop_2838,])
output2 = relay.Tuple([call_2780,call_2790,var_2789,call_2801,const_2798,var_2799,call_2805,call_2807,call_2810,const_2809,call_2831,bop_2838,])
func_2841 = relay.Function([var_2789,var_2799,], output)
mod['func_2841'] = func_2841
mod = relay.transform.InferType()(mod)
var_2842 = relay.var("var_2842", dtype = "float64", shape = (360,))#candidate|2842|(360,)|var|float64
var_2843 = relay.var("var_2843", dtype = "int8", shape = ())#candidate|2843|()|var|int8
output = func_2841(var_2842,var_2843,)
func_2844 = relay.Function([var_2842,var_2843,], output)
mutated_mod['func_2844'] = func_2844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1848_call = mod.get_global_var('func_1848')
func_1849_call = mutated_mod.get_global_var('func_1849')
call_2855 = relay.TupleGetItem(func_1848_call(), 0)
call_2856 = relay.TupleGetItem(func_1849_call(), 0)
output = call_2855
output2 = call_2856
func_2866 = relay.Function([], output)
mod['func_2866'] = func_2866
mod = relay.transform.InferType()(mod)
mutated_mod['func_2866'] = func_2866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mutated_mod.get_global_var('func_2866')
call_2867 = func_2866_call()
output = call_2867
func_2868 = relay.Function([], output)
mutated_mod['func_2868'] = func_2868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2767_call = mod.get_global_var('func_2767')
func_2768_call = mutated_mod.get_global_var('func_2768')
call_2923 = relay.TupleGetItem(func_2767_call(), 0)
call_2924 = relay.TupleGetItem(func_2768_call(), 0)
const_2949 = relay.const([[[8,-10,4,-9],[8,-6,4,-1],[-3,-7,-10,-2],[-4,3,-10,-8],[1,-7,8,6],[7,-6,-9,8],[-7,10,-3,2],[-7,-9,-3,5]],[[3,-1,-7,-8],[10,-7,-1,1],[-9,-7,-5,10],[-1,-9,6,-10],[-8,-1,-9,-1],[-4,-8,-3,-3],[1,-7,-9,10],[-5,-6,-5,-1]]], dtype = "uint32")#candidate|2949|(2, 8, 4)|const|uint32
bop_2950 = relay.less_equal(call_2923.astype('bool'), relay.reshape(const_2949.astype('bool'), relay.shape_of(call_2923))) # shape=(2, 8, 4)
bop_2953 = relay.less_equal(call_2924.astype('bool'), relay.reshape(const_2949.astype('bool'), relay.shape_of(call_2924))) # shape=(2, 8, 4)
func_2516_call = mod.get_global_var('func_2516')
func_2520_call = mutated_mod.get_global_var('func_2520')
var_2958 = relay.var("var_2958", dtype = "uint64", shape = ())#candidate|2958|()|var|uint64
var_2959 = relay.var("var_2959", dtype = "uint64", shape = (45,))#candidate|2959|(45,)|var|uint64
call_2957 = func_2516_call(relay.reshape(var_2958.astype('uint64'), []), relay.reshape(var_2959.astype('uint64'), [5, 3, 3]), )
call_2960 = func_2516_call(relay.reshape(var_2958.astype('uint64'), []), relay.reshape(var_2959.astype('uint64'), [5, 3, 3]), )
output = relay.Tuple([bop_2950,call_2957,var_2958,var_2959,])
output2 = relay.Tuple([bop_2953,call_2960,var_2958,var_2959,])
func_2969 = relay.Function([var_2958,var_2959,], output)
mod['func_2969'] = func_2969
mod = relay.transform.InferType()(mod)
mutated_mod['func_2969'] = func_2969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2969_call = mutated_mod.get_global_var('func_2969')
var_2971 = relay.var("var_2971", dtype = "uint64", shape = ())#candidate|2971|()|var|uint64
var_2972 = relay.var("var_2972", dtype = "uint64", shape = (45,))#candidate|2972|(45,)|var|uint64
call_2970 = func_2969_call(var_2971,var_2972,)
output = call_2970
func_2973 = relay.Function([var_2971,var_2972,], output)
mutated_mod['func_2973'] = func_2973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_3016 = func_749_call()
call_3017 = func_749_call()
output = relay.Tuple([call_3016,])
output2 = relay.Tuple([call_3017,])
func_3043 = relay.Function([], output)
mod['func_3043'] = func_3043
mod = relay.transform.InferType()(mod)
mutated_mod['func_3043'] = func_3043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3043_call = mutated_mod.get_global_var('func_3043')
call_3044 = func_3043_call()
output = call_3044
func_3045 = relay.Function([], output)
mutated_mod['func_3045'] = func_3045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2767_call = mod.get_global_var('func_2767')
func_2768_call = mutated_mod.get_global_var('func_2768')
call_3046 = relay.TupleGetItem(func_2767_call(), 1)
call_3047 = relay.TupleGetItem(func_2768_call(), 1)
func_2479_call = mod.get_global_var('func_2479')
func_2481_call = mutated_mod.get_global_var('func_2481')
call_3056 = relay.TupleGetItem(func_2479_call(), 1)
call_3057 = relay.TupleGetItem(func_2481_call(), 1)
output = relay.Tuple([call_3046,call_3056,])
output2 = relay.Tuple([call_3047,call_3057,])
func_3058 = relay.Function([], output)
mod['func_3058'] = func_3058
mod = relay.transform.InferType()(mod)
mutated_mod['func_3058'] = func_3058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3058_call = mutated_mod.get_global_var('func_3058')
call_3059 = func_3058_call()
output = call_3059
func_3060 = relay.Function([], output)
mutated_mod['func_3060'] = func_3060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_3094 = func_2359_call()
call_3095 = func_2359_call()
func_1266_call = mod.get_global_var('func_1266')
func_1267_call = mutated_mod.get_global_var('func_1267')
call_3097 = relay.TupleGetItem(func_1266_call(), 0)
call_3098 = relay.TupleGetItem(func_1267_call(), 0)
func_845_call = mod.get_global_var('func_845')
func_849_call = mutated_mod.get_global_var('func_849')
const_3104 = relay.const([8,-8,8,-2,-1,-1,-8,-9,-4,8,6,-5,-3,-10,-10,-4], dtype = "int32")#candidate|3104|(16,)|const|int32
var_3105 = relay.var("var_3105", dtype = "int32", shape = (160,))#candidate|3105|(160,)|var|int32
const_3106 = relay.const(-7, dtype = "int8")#candidate|3106|()|const|int8
call_3103 = relay.TupleGetItem(func_845_call(relay.reshape(const_3104.astype('int32'), [16,]), relay.reshape(var_3105.astype('int32'), [16, 10]), relay.reshape(const_3106.astype('int8'), []), ), 2)
call_3107 = relay.TupleGetItem(func_849_call(relay.reshape(const_3104.astype('int32'), [16,]), relay.reshape(var_3105.astype('int32'), [16, 10]), relay.reshape(const_3106.astype('int8'), []), ), 2)
output = relay.Tuple([call_3094,call_3097,call_3103,const_3104,var_3105,const_3106,])
output2 = relay.Tuple([call_3095,call_3098,call_3107,const_3104,var_3105,const_3106,])
func_3108 = relay.Function([var_3105,], output)
mod['func_3108'] = func_3108
mod = relay.transform.InferType()(mod)
var_3109 = relay.var("var_3109", dtype = "int32", shape = (160,))#candidate|3109|(160,)|var|int32
output = func_3108(var_3109)
func_3110 = relay.Function([var_3109], output)
mutated_mod['func_3110'] = func_3110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2868_call = mutated_mod.get_global_var('func_2868')
call_3155 = func_2866_call()
call_3156 = func_2866_call()
output = relay.Tuple([call_3155,])
output2 = relay.Tuple([call_3156,])
func_3177 = relay.Function([], output)
mod['func_3177'] = func_3177
mod = relay.transform.InferType()(mod)
mutated_mod['func_3177'] = func_3177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3177_call = mutated_mod.get_global_var('func_3177')
call_3178 = func_3177_call()
output = call_3178
func_3179 = relay.Function([], output)
mutated_mod['func_3179'] = func_3179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2384_call = mod.get_global_var('func_2384')
func_2386_call = mutated_mod.get_global_var('func_2386')
call_3198 = relay.TupleGetItem(func_2384_call(), 1)
call_3199 = relay.TupleGetItem(func_2386_call(), 1)
output = call_3198
output2 = call_3199
func_3204 = relay.Function([], output)
mod['func_3204'] = func_3204
mod = relay.transform.InferType()(mod)
mutated_mod['func_3204'] = func_3204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3204_call = mutated_mod.get_global_var('func_3204')
call_3205 = func_3204_call()
output = call_3205
func_3206 = relay.Function([], output)
mutated_mod['func_3206'] = func_3206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3204_call = mod.get_global_var('func_3204')
func_3206_call = mutated_mod.get_global_var('func_3206')
call_3210 = func_3204_call()
call_3211 = func_3204_call()
func_1303_call = mod.get_global_var('func_1303')
func_1305_call = mutated_mod.get_global_var('func_1305')
const_3221 = relay.const([-1,7,2,4,-6,6,-2,-5,-5,-10,-7,9,-2,-3,9,10,5,-9,3,-2,4,10,10,-10,-8,-3,9,-10,7,10,3,5,-1,-6,10,3,5,-2,9,-10,-10,-1,-5,4,2,9,5,-3,8,1,7,-2,7,7,-5,2,-2,-8,4,10,-5,-3,-10,-9,6,-8,3,-5,-5,-8,-9,-8,3,-7,-10,-5,5,7,4,8,5,-3,6,-1,-10,3,-9,-10,9,-1,6,5,-4,9,-10,8,-2,4,-8,-9,3,-8,3,7,7,2,-4,7,1,3,-4,5,-3,4,-5,10,6,-2,-9,-4,7,-2,-5,6,-6,5,2,-5,-10,-6,5,5,-5,-2,-6,-3,-2,-3,-3,-1,9,-10,-8,6,6,-5,10,-2,-8,1,3,-8,-6,-2,-1,-9,-2,3,-4,10,-3,-2,-6,7,-1,2,2,-8,1,9,-6,-2,9,-8,6,-4,-4,9,-1,6,5,-5,-7,5,-7,-10,5,1,9,7,-9,2,7,3,-10,-1,8,3,-3,3], dtype = "int8")#candidate|3221|(200,)|const|int8
call_3220 = relay.TupleGetItem(func_1303_call(relay.reshape(const_3221.astype('int8'), [200,])), 2)
call_3222 = relay.TupleGetItem(func_1305_call(relay.reshape(const_3221.astype('int8'), [200,])), 2)
bop_3226 = relay.logical_or(const_3221.astype('bool'), relay.reshape(call_3220.astype('bool'), relay.shape_of(const_3221))) # shape=(200,)
bop_3229 = relay.logical_or(const_3221.astype('bool'), relay.reshape(call_3222.astype('bool'), relay.shape_of(const_3221))) # shape=(200,)
output = relay.Tuple([call_3210,bop_3226,])
output2 = relay.Tuple([call_3211,bop_3229,])
func_3234 = relay.Function([], output)
mod['func_3234'] = func_3234
mod = relay.transform.InferType()(mod)
mutated_mod['func_3234'] = func_3234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mutated_mod.get_global_var('func_3234')
call_3235 = func_3234_call()
output = call_3235
func_3236 = relay.Function([], output)
mutated_mod['func_3236'] = func_3236
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3308 = relay.const([[[-1.965809,-3.360903,-8.162676,-7.730032,3.514924,1.483412,0.735584,-5.856964,1.637571,2.684225,-1.584752],[-5.581191,7.855871,-4.640842,9.227473,-0.387695,9.281793,4.537061,-3.396053,6.307381,-2.085129,6.811170],[6.298527,9.156592,-4.301105,4.177158,-9.642482,1.393867,-7.439404,9.041598,1.758605,6.918688,-2.088551],[4.517732,0.416897,-5.770456,5.941558,1.484020,6.999848,2.125855,6.908298,-9.172246,7.057616,-2.156948],[2.786317,7.264667,0.351986,-3.362057,4.446237,-2.593818,-3.973086,-8.129425,7.153116,-2.763799,-7.927677],[-0.537996,-6.442271,-1.428624,-7.766194,3.902269,-3.971999,3.908861,-1.068008,3.746586,3.855884,-5.750711]],[[7.085066,9.342886,-6.904261,7.441774,3.369584,-8.510486,6.485984,9.351776,5.590350,8.054089,-0.811590],[-0.122287,-0.149904,-3.908931,7.791173,-9.776553,-7.685444,1.043099,5.736232,1.964119,-4.602390,3.821166],[-5.640678,-0.342689,7.170710,0.163148,-2.741255,-9.223931,-3.733670,-9.546325,7.003132,-0.904876,-5.240467],[-0.697382,-5.947607,-1.337655,-3.141709,-5.908000,9.736656,-2.086011,1.310390,-0.017430,0.508954,-0.532419],[5.128109,-1.450729,1.234536,-0.738001,-3.739996,-5.588141,3.397262,-6.853669,-7.486075,-2.897552,9.656540],[-9.241093,0.996568,-6.983543,-4.218679,-3.505630,0.277407,-2.078430,8.823164,-5.717280,-1.088978,-5.528625]]], dtype = "float64")#candidate|3308|(2, 6, 11)|const|float64
uop_3309 = relay.log2(const_3308.astype('float64')) # shape=(2, 6, 11)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_3311 = func_1055_call()
call_3312 = func_1055_call()
var_3317 = relay.var("var_3317", dtype = "float64", shape = (2, 6, 11))#candidate|3317|(2, 6, 11)|var|float64
bop_3318 = relay.power(uop_3309.astype('float32'), relay.reshape(var_3317.astype('float32'), relay.shape_of(uop_3309))) # shape=(2, 6, 11)
uop_3329 = relay.asinh(uop_3309.astype('float64')) # shape=(2, 6, 11)
uop_3331 = relay.acosh(uop_3329.astype('float64')) # shape=(2, 6, 11)
bop_3341 = relay.subtract(uop_3329.astype('uint64'), relay.reshape(uop_3331.astype('uint64'), relay.shape_of(uop_3329))) # shape=(2, 6, 11)
uop_3344 = relay.sinh(uop_3329.astype('float64')) # shape=(2, 6, 11)
bop_3348 = relay.left_shift(uop_3344.astype('int16'), relay.reshape(uop_3309.astype('int16'), relay.shape_of(uop_3344))) # shape=(2, 6, 11)
output = relay.Tuple([call_3311,bop_3318,bop_3341,bop_3348,])
output2 = relay.Tuple([call_3312,bop_3318,bop_3341,bop_3348,])
func_3359 = relay.Function([var_3317,], output)
mod['func_3359'] = func_3359
mod = relay.transform.InferType()(mod)
mutated_mod['func_3359'] = func_3359
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3360 = relay.var("var_3360", dtype = "float64", shape = (2, 6, 11))#candidate|3360|(2, 6, 11)|var|float64
func_3359_call = mutated_mod.get_global_var('func_3359')
call_3361 = func_3359_call(var_3360)
output = call_3361
func_3362 = relay.Function([var_3360], output)
mutated_mod['func_3362'] = func_3362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2767_call = mod.get_global_var('func_2767')
func_2768_call = mutated_mod.get_global_var('func_2768')
call_3382 = relay.TupleGetItem(func_2767_call(), 0)
call_3383 = relay.TupleGetItem(func_2768_call(), 0)
var_3385 = relay.var("var_3385", dtype = "uint32", shape = (2, 8, 4))#candidate|3385|(2, 8, 4)|var|uint32
bop_3386 = relay.right_shift(call_3382.astype('int64'), relay.reshape(var_3385.astype('int64'), relay.shape_of(call_3382))) # shape=(2, 8, 4)
bop_3389 = relay.right_shift(call_3383.astype('int64'), relay.reshape(var_3385.astype('int64'), relay.shape_of(call_3383))) # shape=(2, 8, 4)
func_2099_call = mod.get_global_var('func_2099')
func_2101_call = mutated_mod.get_global_var('func_2101')
call_3396 = relay.TupleGetItem(func_2099_call(), 0)
call_3397 = relay.TupleGetItem(func_2101_call(), 0)
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_3398 = func_2651_call()
call_3399 = func_2651_call()
output = relay.Tuple([bop_3386,call_3396,call_3398,])
output2 = relay.Tuple([bop_3389,call_3397,call_3399,])
func_3418 = relay.Function([var_3385,], output)
mod['func_3418'] = func_3418
mod = relay.transform.InferType()(mod)
var_3419 = relay.var("var_3419", dtype = "uint32", shape = (2, 8, 4))#candidate|3419|(2, 8, 4)|var|uint32
output = func_3418(var_3419)
func_3420 = relay.Function([var_3419], output)
mutated_mod['func_3420'] = func_3420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_708_call = mod.get_global_var('func_708')
func_710_call = mutated_mod.get_global_var('func_710')
call_3447 = relay.TupleGetItem(func_708_call(), 0)
call_3448 = relay.TupleGetItem(func_710_call(), 0)
output = relay.Tuple([call_3447,])
output2 = relay.Tuple([call_3448,])
func_3452 = relay.Function([], output)
mod['func_3452'] = func_3452
mod = relay.transform.InferType()(mod)
mutated_mod['func_3452'] = func_3452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3452_call = mutated_mod.get_global_var('func_3452')
call_3453 = func_3452_call()
output = call_3453
func_3454 = relay.Function([], output)
mutated_mod['func_3454'] = func_3454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2597_call = mod.get_global_var('func_2597')
func_2599_call = mutated_mod.get_global_var('func_2599')
call_3475 = func_2597_call()
call_3476 = func_2597_call()
func_3108_call = mod.get_global_var('func_3108')
func_3110_call = mutated_mod.get_global_var('func_3110')
var_3487 = relay.var("var_3487", dtype = "int32", shape = (160,))#candidate|3487|(160,)|var|int32
call_3486 = relay.TupleGetItem(func_3108_call(relay.reshape(var_3487.astype('int32'), [160,])), 2)
call_3488 = relay.TupleGetItem(func_3110_call(relay.reshape(var_3487.astype('int32'), [160,])), 2)
output = relay.Tuple([call_3475,call_3486,var_3487,])
output2 = relay.Tuple([call_3476,call_3488,var_3487,])
func_3504 = relay.Function([var_3487,], output)
mod['func_3504'] = func_3504
mod = relay.transform.InferType()(mod)
var_3505 = relay.var("var_3505", dtype = "int32", shape = (160,))#candidate|3505|(160,)|var|int32
output = func_3504(var_3505)
func_3506 = relay.Function([var_3505], output)
mutated_mod['func_3506'] = func_3506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1386_call = mod.get_global_var('func_1386')
func_1388_call = mutated_mod.get_global_var('func_1388')
call_3559 = func_1386_call()
call_3560 = func_1386_call()
func_3234_call = mod.get_global_var('func_3234')
func_3236_call = mutated_mod.get_global_var('func_3236')
call_3576 = relay.TupleGetItem(func_3234_call(), 0)
call_3577 = relay.TupleGetItem(func_3236_call(), 0)
output = relay.Tuple([call_3559,call_3576,])
output2 = relay.Tuple([call_3560,call_3577,])
func_3581 = relay.Function([], output)
mod['func_3581'] = func_3581
mod = relay.transform.InferType()(mod)
mutated_mod['func_3581'] = func_3581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3581_call = mutated_mod.get_global_var('func_3581')
call_3582 = func_3581_call()
output = call_3582
func_3583 = relay.Function([], output)
mutated_mod['func_3583'] = func_3583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1386_call = mod.get_global_var('func_1386')
func_1388_call = mutated_mod.get_global_var('func_1388')
call_3592 = func_1386_call()
call_3593 = func_1386_call()
uop_3595 = relay.log10(call_3592.astype('float64')) # shape=(2, 8, 4)
uop_3597 = relay.log10(call_3593.astype('float64')) # shape=(2, 8, 4)
func_3581_call = mod.get_global_var('func_3581')
func_3583_call = mutated_mod.get_global_var('func_3583')
call_3602 = relay.TupleGetItem(func_3581_call(), 1)
call_3603 = relay.TupleGetItem(func_3583_call(), 1)
func_3452_call = mod.get_global_var('func_3452')
func_3454_call = mutated_mod.get_global_var('func_3454')
call_3628 = relay.TupleGetItem(func_3452_call(), 0)
call_3629 = relay.TupleGetItem(func_3454_call(), 0)
func_1131_call = mod.get_global_var('func_1131')
func_1134_call = mutated_mod.get_global_var('func_1134')
const_3655 = relay.const([-4,-4,5,1,4,6,7,1,4,2,3,-8,7,-9,-3,3,-3,8,-8,-5,-2,10,-1,-9,-10,4,-4,-4,-10,-6,-9,4,6,1,10,-6,-7,2,-9,2,-3,-3,-9,-10,9,-3,2,10,9,2,5,2,8,9,6,-9,6,-5,-8,-3,10,-5,3,-2,7,2,4,6,-9,-1,6,5,1,-6,-7,-6,-7,1,6,-4,9,-7,-1,9,9,6,-8,-7,1,10,4,-6,8,-3,-3,9,5,9,10,6,5,-3,3,4,5,3,-9,-2,-6,-3,-4,-3,10,-2,9,10,-2,-1,-4,10,-10,-9,-9,7,-6,6,-5,-8,4,-5,-10,9,7,6,8,1,8,-8,-10,4,-7,5,-3,5,5,-10,-5,6,10,3,7,-5,-3,3,8,-9,-10,-7,9,10,-1,8,9,6,-5,7,-3,8,5,-9,-1,-10,-5,3,6,-10,2,-3,-2,-2,1,3,-4,-10,-4,-4,7,5,-10,8,10,4,-5,-4,-9,-4,-6,2,9,10], dtype = "int8")#candidate|3655|(200,)|const|int8
const_3656 = relay.const(-5, dtype = "int8")#candidate|3656|()|const|int8
call_3654 = relay.TupleGetItem(func_1131_call(relay.reshape(const_3655.astype('int8'), [200,]), relay.reshape(const_3656.astype('int8'), []), ), 2)
call_3657 = relay.TupleGetItem(func_1134_call(relay.reshape(const_3655.astype('int8'), [200,]), relay.reshape(const_3656.astype('int8'), []), ), 2)
output = relay.Tuple([uop_3595,call_3602,call_3628,call_3654,const_3655,const_3656,])
output2 = relay.Tuple([uop_3597,call_3603,call_3629,call_3657,const_3655,const_3656,])
func_3680 = relay.Function([], output)
mod['func_3680'] = func_3680
mod = relay.transform.InferType()(mod)
mutated_mod['func_3680'] = func_3680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3680_call = mutated_mod.get_global_var('func_3680')
call_3681 = func_3680_call()
output = call_3681
func_3682 = relay.Function([], output)
mutated_mod['func_3682'] = func_3682
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3687 = relay.var("var_3687", dtype = "uint64", shape = (8, 2, 9))#candidate|3687|(8, 2, 9)|var|uint64
var_3688 = relay.var("var_3688", dtype = "uint64", shape = (8, 2, 9))#candidate|3688|(8, 2, 9)|var|uint64
bop_3689 = relay.bitwise_or(var_3687.astype('uint64'), relay.reshape(var_3688.astype('uint64'), relay.shape_of(var_3687))) # shape=(8, 2, 9)
uop_3701 = relay.sigmoid(var_3688.astype('float64')) # shape=(8, 2, 9)
uop_3708 = relay.cos(var_3688.astype('float32')) # shape=(8, 2, 9)
bop_3716 = relay.mod(uop_3701.astype('float32'), relay.reshape(uop_3708.astype('float32'), relay.shape_of(uop_3701))) # shape=(8, 2, 9)
output = relay.Tuple([bop_3689,bop_3716,])
output2 = relay.Tuple([bop_3689,bop_3716,])
func_3724 = relay.Function([var_3687,var_3688,], output)
mod['func_3724'] = func_3724
mod = relay.transform.InferType()(mod)
mutated_mod['func_3724'] = func_3724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3724_call = mutated_mod.get_global_var('func_3724')
var_3726 = relay.var("var_3726", dtype = "uint64", shape = (8, 2, 9))#candidate|3726|(8, 2, 9)|var|uint64
var_3727 = relay.var("var_3727", dtype = "uint64", shape = (8, 2, 9))#candidate|3727|(8, 2, 9)|var|uint64
call_3725 = func_3724_call(var_3726,var_3727,)
output = call_3725
func_3728 = relay.Function([var_3726,var_3727,], output)
mutated_mod['func_3728'] = func_3728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3236_call = mutated_mod.get_global_var('func_3236')
call_3847 = relay.TupleGetItem(func_3234_call(), 1)
call_3848 = relay.TupleGetItem(func_3236_call(), 1)
func_2767_call = mod.get_global_var('func_2767')
func_2768_call = mutated_mod.get_global_var('func_2768')
call_3869 = relay.TupleGetItem(func_2767_call(), 0)
call_3870 = relay.TupleGetItem(func_2768_call(), 0)
output = relay.Tuple([call_3847,call_3869,])
output2 = relay.Tuple([call_3848,call_3870,])
func_3887 = relay.Function([], output)
mod['func_3887'] = func_3887
mod = relay.transform.InferType()(mod)
output = func_3887()
func_3888 = relay.Function([], output)
mutated_mod['func_3888'] = func_3888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3581_call = mod.get_global_var('func_3581')
func_3583_call = mutated_mod.get_global_var('func_3583')
call_3907 = relay.TupleGetItem(func_3581_call(), 0)
call_3908 = relay.TupleGetItem(func_3583_call(), 0)
var_3939 = relay.var("var_3939", dtype = "uint32", shape = (2, 8, 4))#candidate|3939|(2, 8, 4)|var|uint32
bop_3940 = relay.equal(call_3907.astype('bool'), relay.reshape(var_3939.astype('bool'), relay.shape_of(call_3907))) # shape=(2, 8, 4)
bop_3943 = relay.equal(call_3908.astype('bool'), relay.reshape(var_3939.astype('bool'), relay.shape_of(call_3908))) # shape=(2, 8, 4)
func_3581_call = mod.get_global_var('func_3581')
func_3583_call = mutated_mod.get_global_var('func_3583')
call_3950 = relay.TupleGetItem(func_3581_call(), 0)
call_3951 = relay.TupleGetItem(func_3583_call(), 0)
output = relay.Tuple([bop_3940,call_3950,])
output2 = relay.Tuple([bop_3943,call_3951,])
func_3959 = relay.Function([var_3939,], output)
mod['func_3959'] = func_3959
mod = relay.transform.InferType()(mod)
mutated_mod['func_3959'] = func_3959
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3960 = relay.var("var_3960", dtype = "uint32", shape = (2, 8, 4))#candidate|3960|(2, 8, 4)|var|uint32
func_3959_call = mutated_mod.get_global_var('func_3959')
call_3961 = func_3959_call(var_3960)
output = call_3961
func_3962 = relay.Function([var_3960], output)
mutated_mod['func_3962'] = func_3962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_4000 = func_718_call()
call_4001 = func_718_call()
output = call_4000
output2 = call_4001
func_4007 = relay.Function([], output)
mod['func_4007'] = func_4007
mod = relay.transform.InferType()(mod)
output = func_4007()
func_4008 = relay.Function([], output)
mutated_mod['func_4008'] = func_4008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_749_call = mod.get_global_var('func_749')
func_751_call = mutated_mod.get_global_var('func_751')
call_4093 = func_749_call()
call_4094 = func_749_call()
output = call_4093
output2 = call_4094
func_4116 = relay.Function([], output)
mod['func_4116'] = func_4116
mod = relay.transform.InferType()(mod)
mutated_mod['func_4116'] = func_4116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4116_call = mutated_mod.get_global_var('func_4116')
call_4117 = func_4116_call()
output = call_4117
func_4118 = relay.Function([], output)
mutated_mod['func_4118'] = func_4118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3058_call = mod.get_global_var('func_3058')
func_3060_call = mutated_mod.get_global_var('func_3060')
call_4126 = relay.TupleGetItem(func_3058_call(), 1)
call_4127 = relay.TupleGetItem(func_3060_call(), 1)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_4130 = func_2031_call()
call_4131 = func_2031_call()
output = relay.Tuple([call_4126,call_4130,])
output2 = relay.Tuple([call_4127,call_4131,])
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
var_4215 = relay.var("var_4215", dtype = "float64", shape = ())#candidate|4215|()|var|float64
var_4216 = relay.var("var_4216", dtype = "float64", shape = (2, 1))#candidate|4216|(2, 1)|var|float64
bop_4217 = relay.floor_mod(var_4215.astype('float64'), var_4216.astype('float64')) # shape=(2, 1)
func_1421_call = mod.get_global_var('func_1421')
func_1424_call = mutated_mod.get_global_var('func_1424')
var_4224 = relay.var("var_4224", dtype = "uint16", shape = (448,))#candidate|4224|(448,)|var|uint16
call_4223 = relay.TupleGetItem(func_1421_call(relay.reshape(var_4224.astype('uint16'), [14, 2, 16])), 0)
call_4225 = relay.TupleGetItem(func_1424_call(relay.reshape(var_4224.astype('uint16'), [14, 2, 16])), 0)
func_1386_call = mod.get_global_var('func_1386')
func_1388_call = mutated_mod.get_global_var('func_1388')
call_4228 = func_1386_call()
call_4229 = func_1386_call()
func_3680_call = mod.get_global_var('func_3680')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_4234 = relay.TupleGetItem(func_3680_call(), 2)
call_4235 = relay.TupleGetItem(func_3682_call(), 2)
output = relay.Tuple([bop_4217,call_4223,var_4224,call_4228,call_4234,])
output2 = relay.Tuple([bop_4217,call_4225,var_4224,call_4229,call_4235,])
func_4236 = relay.Function([var_4215,var_4216,var_4224,], output)
mod['func_4236'] = func_4236
mod = relay.transform.InferType()(mod)
mutated_mod['func_4236'] = func_4236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4236_call = mutated_mod.get_global_var('func_4236')
var_4238 = relay.var("var_4238", dtype = "float64", shape = ())#candidate|4238|()|var|float64
var_4239 = relay.var("var_4239", dtype = "float64", shape = (2, 1))#candidate|4239|(2, 1)|var|float64
var_4240 = relay.var("var_4240", dtype = "uint16", shape = (448,))#candidate|4240|(448,)|var|uint16
call_4237 = func_4236_call(var_4238,var_4239,var_4240,)
output = call_4237
func_4241 = relay.Function([var_4238,var_4239,var_4240,], output)
mutated_mod['func_4241'] = func_4241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3177_call = mod.get_global_var('func_3177')
func_3179_call = mutated_mod.get_global_var('func_3179')
call_4257 = relay.TupleGetItem(func_3177_call(), 0)
call_4258 = relay.TupleGetItem(func_3179_call(), 0)
output = call_4257
output2 = call_4258
func_4272 = relay.Function([], output)
mod['func_4272'] = func_4272
mod = relay.transform.InferType()(mod)
mutated_mod['func_4272'] = func_4272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4272_call = mutated_mod.get_global_var('func_4272')
call_4273 = func_4272_call()
output = call_4273
func_4274 = relay.Function([], output)
mutated_mod['func_4274'] = func_4274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_4349 = func_2651_call()
call_4350 = func_2651_call()
func_3234_call = mod.get_global_var('func_3234')
func_3236_call = mutated_mod.get_global_var('func_3236')
call_4351 = relay.TupleGetItem(func_3234_call(), 1)
call_4352 = relay.TupleGetItem(func_3236_call(), 1)
output = relay.Tuple([call_4349,call_4351,])
output2 = relay.Tuple([call_4350,call_4352,])
func_4379 = relay.Function([], output)
mod['func_4379'] = func_4379
mod = relay.transform.InferType()(mod)
mutated_mod['func_4379'] = func_4379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4379_call = mutated_mod.get_global_var('func_4379')
call_4380 = func_4379_call()
output = call_4380
func_4381 = relay.Function([], output)
mutated_mod['func_4381'] = func_4381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2099_call = mod.get_global_var('func_2099')
func_2101_call = mutated_mod.get_global_var('func_2101')
call_4387 = relay.TupleGetItem(func_2099_call(), 0)
call_4388 = relay.TupleGetItem(func_2101_call(), 0)
var_4393 = relay.var("var_4393", dtype = "float64", shape = (2, 8, 4))#candidate|4393|(2, 8, 4)|var|float64
bop_4394 = relay.bitwise_or(call_4387.astype('uint8'), relay.reshape(var_4393.astype('uint8'), relay.shape_of(call_4387))) # shape=(2, 8, 4)
bop_4397 = relay.bitwise_or(call_4388.astype('uint8'), relay.reshape(var_4393.astype('uint8'), relay.shape_of(call_4388))) # shape=(2, 8, 4)
func_289_call = mod.get_global_var('func_289')
func_293_call = mutated_mod.get_global_var('func_293')
var_4410 = relay.var("var_4410", dtype = "int8", shape = ())#candidate|4410|()|var|int8
const_4411 = relay.const([7,-1,10,6,-1,10,-9,9,10,-10,-7,1,-1,-4,4,-6,-5,-3,-10,-8,10,-9,6,5,-5,4,3,-10,6,7,-5,3,9,-8,7,-10,-3,7,6,-5,8,5,-5,-8,-6,3,7,3,1,4,7,-4,2,10,-5,9,6,-5,-8,4,-7,5,-10,-9,-2,-9,-5,-9,-6,7,6,5,1,-3,-4,-2,3,-6,-8,3,5,8,5,-1,8,2,-5,8,-8,4,7,4,5,-2,-4,4,-7,3,10,2,-1,4,3,1,-2,-3,1,10,9,9,-8,-5,3,-8,-10,-3,-7,7,6,9,-1,6,4,-7,9,-6,-9,2,7,-7,10,-9,6,5,4,-9,-10,8,-2,-7,-1,7,-4,-1,7,-9,9,-4,-4,6,-4,-6,3,-6,-10,-5,-6,2,1,10,-5,-5,-6,9,7,-1,-2,5,2,-10,6,7,8,-3,-7,7,1,6,2,-7,-1,-1,-5,8,-10,4,-6,10,-10,-4,-6,-9,-4,4,10,-6,10,-8,4,6], dtype = "int8")#candidate|4411|(200,)|const|int8
call_4409 = func_289_call(relay.reshape(var_4410.astype('int8'), []), relay.reshape(const_4411.astype('int8'), [10, 10, 2]), )
call_4412 = func_289_call(relay.reshape(var_4410.astype('int8'), []), relay.reshape(const_4411.astype('int8'), [10, 10, 2]), )
const_4417 = relay.const([[[2.447958,-8.748245,4.004179,-6.678669],[7.327604,9.178822,-6.301251,6.362033],[8.616724,-4.073144,4.984060,-8.271611],[7.081440,-9.189770,-5.796490,-2.240954],[-4.202636,-0.592302,4.748439,-6.094114],[5.292809,9.191051,-7.854030,-5.892232],[5.525336,-6.622960,-0.005050,-9.614357],[-1.965784,4.854933,-3.902892,-2.439282]],[[7.073946,-5.124729,8.423394,0.405528],[-0.975289,-5.142190,9.036638,-9.947099],[-8.912584,9.514083,-9.852166,-5.056664],[5.823314,6.609230,1.323884,-6.230689],[-4.250180,7.012946,6.846815,-8.917527],[5.501464,5.086142,5.303871,-5.644026],[-0.925662,-2.538391,5.275765,-2.898564],[5.286965,-7.507727,6.897558,4.647831]]], dtype = "float64")#candidate|4417|(2, 8, 4)|const|float64
bop_4418 = relay.left_shift(call_4387.astype('uint16'), relay.reshape(const_4417.astype('uint16'), relay.shape_of(call_4387))) # shape=(2, 8, 4)
bop_4421 = relay.left_shift(call_4388.astype('uint16'), relay.reshape(const_4417.astype('uint16'), relay.shape_of(call_4388))) # shape=(2, 8, 4)
func_3108_call = mod.get_global_var('func_3108')
func_3110_call = mutated_mod.get_global_var('func_3110')
var_4436 = relay.var("var_4436", dtype = "int32", shape = (160,))#candidate|4436|(160,)|var|int32
call_4435 = relay.TupleGetItem(func_3108_call(relay.reshape(var_4436.astype('int32'), [160,])), 2)
call_4437 = relay.TupleGetItem(func_3110_call(relay.reshape(var_4436.astype('int32'), [160,])), 2)
func_2404_call = mod.get_global_var('func_2404')
func_2406_call = mutated_mod.get_global_var('func_2406')
const_4455 = relay.const([[9.256297,-7.502384,3.495071,-5.641728,-5.526778,1.947005,7.581205,-7.749492,-4.734910,-8.981236,2.136192,2.718128,-0.868236,4.401627,4.546741,4.733481,-7.869983,4.063566,5.137956,4.631337,-5.613287,3.020402,3.400081,-5.260083,-2.703789,-7.404382,-7.459640,4.761911,-6.641317,6.832948,-9.928373,3.272735,0.865029,-7.852030,-4.258452,-6.648382,1.928740,0.198160,3.015486,-0.265024,-3.672060,2.608343,8.300614,-8.391890,3.079056,6.835238,-0.715868,0.296643,4.903682,0.409194,2.546821,-7.842483,7.939079,3.073217,-1.688450,7.048493,-3.710315,5.027865,9.700219,-0.272797,4.579743,-8.932599,-1.640816,2.476859,7.293927,7.179252,-1.938925,9.907409,6.427080,-4.908094,6.712673,4.498669,-3.473654,7.170870,-7.128997,9.884038,8.588350,2.439719,1.113005,-4.811278,7.051745,3.031206,6.724453,-1.559014,5.870043,-8.824010,-8.996007,7.385678,-2.074346,-3.367306,-1.868292,4.969871,3.998091,1.834453,7.553888,7.109378,7.848048,1.795415,-2.219933,-3.798115,-4.304522,-7.355390,-8.145264,-2.289017,-2.986410,0.001609,-6.994794,-8.225406,4.734789,-9.397670,6.729129,-5.055562,-5.206928,-8.575803,8.440049,-4.087706,0.932088,-1.471019,-1.162603,1.399664,4.967116,3.687898,6.690269,3.652407,1.874506,3.358850,7.135443,-2.977516,2.491168,-9.532970,5.780709,2.113907,7.070296,-2.820859,-5.306771,-1.927557,-7.454200,8.471378,-3.243811,-5.522008,-6.155397,-2.208655,6.018555,1.521367,1.002486,5.246437,-8.775805,-7.059845,-3.583288,-9.442332,-6.630895,-4.132802,-4.087736,-0.756130,-6.339746,9.922706,-5.604889,0.848560,-4.697610,3.390028,-6.220097,-4.457940,5.841673,8.846381,8.839271,-7.255121,-1.868637,-1.418497,-3.909740,4.548904,1.299677,6.382324,6.836502,-3.909316,6.734111,2.226070,-2.095776,-7.092720,-4.332137,-6.934171,9.269124,1.052093,9.325407,0.448877,-6.754719,1.941103,8.466325,-0.569736,6.069874,-2.699836,-8.867094,-9.908204,9.177114,-8.850145,-2.676888,1.122716,4.813229,-8.545025,-9.019742,-1.113160,-6.609477,-2.334770,-8.143285,-0.552636,1.140002,-5.275755,4.210680,6.821836,4.337344,-9.220187,-9.148637,-3.004601,1.633327,-5.568870,-3.684516,-6.169635,-5.681394,-8.945725,5.356457,-3.622922,4.644764,-3.498812,-3.204577,6.312265,3.088123,8.379398,0.151516,6.892461,-2.316504,-7.909072,-3.304257,-0.017465,8.055501,8.441162,0.985503,-0.014766,-8.070097,5.774504,-3.712817,2.519181,5.533272,6.167272,-9.987281,7.781702,-1.956078,0.511193,-5.415474,-4.310299,-3.589278,1.391984,8.687701,-1.316555,-0.034213,-1.181007,-1.840697,9.755575,6.907942,-5.622647,0.046703,-3.077007,6.201931,9.737150,0.105636,1.017957,6.419412,-3.066981,-9.705908,5.671272,-0.037908,5.429301,4.587552,-4.663834,2.289018,-7.119377,-3.809834,3.239084,-8.308640,-6.881483,-5.246726,9.669313,-8.674282,-7.753226,-2.561827,1.227153,-5.785968,2.025141,8.631719,-7.320848,-6.044657,-9.663121,2.583971,-7.686215,-0.608653,-0.666328,-3.661062,-0.918313,7.509909,-2.145034,-5.266764,-6.369960,-1.401896,-5.878119,-1.235341,6.370767,2.624204,3.126860,0.676956,-4.853691,-1.184429,-5.320988,-6.273926,6.247240,0.130821,0.583572,-0.931138,-2.036639,6.819274,-4.132717,3.959136,-3.723208,9.492984,-0.367684,9.673675,-3.870624,0.226252,9.990355,-7.908939,3.770858,-9.256437,2.545791,-2.944133,4.402938,8.105770,2.805073,9.382607,4.012909,-2.282463,5.154545,5.035176,7.757408,-7.921064,-5.328288,-5.531022,0.714177,1.769182,5.622081,-0.774780,1.603423,-4.640280,1.458153,1.858133,1.723168,-0.221968,8.594578,-5.140154,-2.342353,5.503121,4.638388,-7.624994,-3.364879,-4.140334,1.663601,3.003898,-4.018157,-9.028977,7.885371,-8.004237,1.001758,-9.050519,-8.310295,7.121810,7.062200,-3.402434,-6.578249,0.137394,-7.466470,-6.867509,3.835943,-8.883705,-5.411095,3.382860,-2.727488,-4.217245,-8.389827]], dtype = "float64")#candidate|4455|(1, 384)|const|float64
call_4454 = func_2404_call(relay.reshape(const_4455.astype('float64'), [4, 8, 12]))
call_4456 = func_2404_call(relay.reshape(const_4455.astype('float64'), [4, 8, 12]))
func_3234_call = mod.get_global_var('func_3234')
func_3236_call = mutated_mod.get_global_var('func_3236')
call_4469 = relay.TupleGetItem(func_3234_call(), 0)
call_4470 = relay.TupleGetItem(func_3236_call(), 0)
bop_4471 = relay.minimum(call_4454.astype('uint64'), var_4410.astype('uint64')) # shape=(4, 8, 12)
bop_4474 = relay.minimum(call_4456.astype('uint64'), var_4410.astype('uint64')) # shape=(4, 8, 12)
func_647_call = mod.get_global_var('func_647')
func_649_call = mutated_mod.get_global_var('func_649')
call_4486 = relay.TupleGetItem(func_647_call(relay.reshape(const_4411.astype('int8'), [200,])), 3)
call_4487 = relay.TupleGetItem(func_649_call(relay.reshape(const_4411.astype('int8'), [200,])), 3)
output = relay.Tuple([bop_4394,call_4409,const_4411,bop_4418,call_4435,var_4436,const_4455,call_4469,bop_4471,call_4486,])
output2 = relay.Tuple([bop_4397,call_4412,const_4411,bop_4421,call_4437,var_4436,const_4455,call_4470,bop_4474,call_4487,])
func_4497 = relay.Function([var_4393,var_4410,var_4436,], output)
mod['func_4497'] = func_4497
mod = relay.transform.InferType()(mod)
var_4498 = relay.var("var_4498", dtype = "float64", shape = (2, 8, 4))#candidate|4498|(2, 8, 4)|var|float64
var_4499 = relay.var("var_4499", dtype = "int8", shape = ())#candidate|4499|()|var|int8
var_4500 = relay.var("var_4500", dtype = "int32", shape = (160,))#candidate|4500|(160,)|var|int32
output = func_4497(var_4498,var_4499,var_4500,)
func_4501 = relay.Function([var_4498,var_4499,var_4500,], output)
mutated_mod['func_4501'] = func_4501
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4516 = relay.var("var_4516", dtype = "float64", shape = (15, 6, 9))#candidate|4516|(15, 6, 9)|var|float64
uop_4517 = relay.cosh(var_4516.astype('float64')) # shape=(15, 6, 9)
output = uop_4517
output2 = uop_4517
func_4529 = relay.Function([var_4516,], output)
mod['func_4529'] = func_4529
mod = relay.transform.InferType()(mod)
mutated_mod['func_4529'] = func_4529
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4530 = relay.var("var_4530", dtype = "float64", shape = (15, 6, 9))#candidate|4530|(15, 6, 9)|var|float64
func_4529_call = mutated_mod.get_global_var('func_4529')
call_4531 = func_4529_call(var_4530)
output = call_4531
func_4532 = relay.Function([var_4530], output)
mutated_mod['func_4532'] = func_4532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_4552 = func_2359_call()
call_4553 = func_2359_call()
func_2404_call = mod.get_global_var('func_2404')
func_2406_call = mutated_mod.get_global_var('func_2406')
var_4564 = relay.var("var_4564", dtype = "float64", shape = (384,))#candidate|4564|(384,)|var|float64
call_4563 = func_2404_call(relay.reshape(var_4564.astype('float64'), [4, 8, 12]))
call_4565 = func_2404_call(relay.reshape(var_4564.astype('float64'), [4, 8, 12]))
func_2723_call = mod.get_global_var('func_2723')
func_2725_call = mutated_mod.get_global_var('func_2725')
call_4596 = relay.TupleGetItem(func_2723_call(), 0)
call_4597 = relay.TupleGetItem(func_2725_call(), 0)
uop_4603 = relay.cos(call_4563.astype('float32')) # shape=(4, 8, 12)
uop_4605 = relay.cos(call_4565.astype('float32')) # shape=(4, 8, 12)
output = relay.Tuple([call_4552,var_4564,call_4596,uop_4603,])
output2 = relay.Tuple([call_4553,var_4564,call_4597,uop_4605,])
func_4606 = relay.Function([var_4564,], output)
mod['func_4606'] = func_4606
mod = relay.transform.InferType()(mod)
mutated_mod['func_4606'] = func_4606
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4607 = relay.var("var_4607", dtype = "float64", shape = (384,))#candidate|4607|(384,)|var|float64
func_4606_call = mutated_mod.get_global_var('func_4606')
call_4608 = func_4606_call(var_4607)
output = call_4608
func_4609 = relay.Function([var_4607], output)
mutated_mod['func_4609'] = func_4609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4116_call = mod.get_global_var('func_4116')
func_4118_call = mutated_mod.get_global_var('func_4118')
call_4638 = func_4116_call()
call_4639 = func_4116_call()
uop_4655 = relay.acosh(call_4638.astype('float32')) # shape=(2, 8, 4)
uop_4657 = relay.acosh(call_4639.astype('float32')) # shape=(2, 8, 4)
output = relay.Tuple([uop_4655,])
output2 = relay.Tuple([uop_4657,])
func_4684 = relay.Function([], output)
mod['func_4684'] = func_4684
mod = relay.transform.InferType()(mod)
output = func_4684()
func_4685 = relay.Function([], output)
mutated_mod['func_4685'] = func_4685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2767_call = mod.get_global_var('func_2767')
func_2768_call = mutated_mod.get_global_var('func_2768')
call_4717 = relay.TupleGetItem(func_2767_call(), 0)
call_4718 = relay.TupleGetItem(func_2768_call(), 0)
output = call_4717
output2 = call_4718
func_4722 = relay.Function([], output)
mod['func_4722'] = func_4722
mod = relay.transform.InferType()(mod)
output = func_4722()
func_4723 = relay.Function([], output)
mutated_mod['func_4723'] = func_4723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2868_call = mutated_mod.get_global_var('func_2868')
call_4750 = func_2866_call()
call_4751 = func_2866_call()
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_4760 = func_2651_call()
call_4761 = func_2651_call()
func_2243_call = mod.get_global_var('func_2243')
func_2248_call = mutated_mod.get_global_var('func_2248')
var_4781 = relay.var("var_4781", dtype = "int32", shape = (16,))#candidate|4781|(16,)|var|int32
var_4782 = relay.var("var_4782", dtype = "int8", shape = ())#candidate|4782|()|var|int8
var_4783 = relay.var("var_4783", dtype = "uint16", shape = (448,))#candidate|4783|(448,)|var|uint16
call_4780 = relay.TupleGetItem(func_2243_call(relay.reshape(var_4781.astype('int32'), [1, 16]), relay.reshape(var_4782.astype('int8'), []), relay.reshape(var_4783.astype('uint16'), [448,]), ), 4)
call_4784 = relay.TupleGetItem(func_2248_call(relay.reshape(var_4781.astype('int32'), [1, 16]), relay.reshape(var_4782.astype('int8'), []), relay.reshape(var_4783.astype('uint16'), [448,]), ), 4)
func_1303_call = mod.get_global_var('func_1303')
func_1305_call = mutated_mod.get_global_var('func_1305')
call_4786 = relay.TupleGetItem(func_1303_call(relay.reshape(call_4780.astype('int8'), [200,])), 2)
call_4787 = relay.TupleGetItem(func_1305_call(relay.reshape(call_4780.astype('int8'), [200,])), 2)
output = relay.Tuple([call_4750,call_4760,call_4780,var_4781,var_4782,var_4783,call_4786,])
output2 = relay.Tuple([call_4751,call_4761,call_4784,var_4781,var_4782,var_4783,call_4787,])
func_4803 = relay.Function([var_4781,var_4782,var_4783,], output)
mod['func_4803'] = func_4803
mod = relay.transform.InferType()(mod)
mutated_mod['func_4803'] = func_4803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mutated_mod.get_global_var('func_4803')
var_4805 = relay.var("var_4805", dtype = "int32", shape = (16,))#candidate|4805|(16,)|var|int32
var_4806 = relay.var("var_4806", dtype = "int8", shape = ())#candidate|4806|()|var|int8
var_4807 = relay.var("var_4807", dtype = "uint16", shape = (448,))#candidate|4807|(448,)|var|uint16
call_4804 = func_4803_call(var_4805,var_4806,var_4807,)
output = call_4804
func_4808 = relay.Function([var_4805,var_4806,var_4807,], output)
mutated_mod['func_4808'] = func_4808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3581_call = mod.get_global_var('func_3581')
func_3583_call = mutated_mod.get_global_var('func_3583')
call_4814 = relay.TupleGetItem(func_3581_call(), 1)
call_4815 = relay.TupleGetItem(func_3583_call(), 1)
output = relay.Tuple([call_4814,])
output2 = relay.Tuple([call_4815,])
func_4828 = relay.Function([], output)
mod['func_4828'] = func_4828
mod = relay.transform.InferType()(mod)
mutated_mod['func_4828'] = func_4828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4828_call = mutated_mod.get_global_var('func_4828')
call_4829 = func_4828_call()
output = call_4829
func_4830 = relay.Function([], output)
mutated_mod['func_4830'] = func_4830
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4831 = relay.var("var_4831", dtype = "float64", shape = (6, 6, 2))#candidate|4831|(6, 6, 2)|var|float64
var_4832 = relay.var("var_4832", dtype = "float64", shape = (6, 6, 2))#candidate|4832|(6, 6, 2)|var|float64
bop_4833 = relay.divide(var_4831.astype('float64'), relay.reshape(var_4832.astype('float64'), relay.shape_of(var_4831))) # shape=(6, 6, 2)
func_3959_call = mod.get_global_var('func_3959')
func_3962_call = mutated_mod.get_global_var('func_3962')
var_4863 = relay.var("var_4863", dtype = "uint32", shape = (16, 4))#candidate|4863|(16, 4)|var|uint32
call_4862 = relay.TupleGetItem(func_3959_call(relay.reshape(var_4863.astype('uint32'), [2, 8, 4])), 0)
call_4864 = relay.TupleGetItem(func_3962_call(relay.reshape(var_4863.astype('uint32'), [2, 8, 4])), 0)
uop_4868 = relay.sigmoid(bop_4833.astype('float64')) # shape=(6, 6, 2)
func_2132_call = mod.get_global_var('func_2132')
func_2134_call = mutated_mod.get_global_var('func_2134')
call_4870 = func_2132_call()
call_4871 = func_2132_call()
output = relay.Tuple([call_4862,var_4863,uop_4868,call_4870,])
output2 = relay.Tuple([call_4864,var_4863,uop_4868,call_4871,])
func_4875 = relay.Function([var_4831,var_4832,var_4863,], output)
mod['func_4875'] = func_4875
mod = relay.transform.InferType()(mod)
var_4876 = relay.var("var_4876", dtype = "float64", shape = (6, 6, 2))#candidate|4876|(6, 6, 2)|var|float64
var_4877 = relay.var("var_4877", dtype = "float64", shape = (6, 6, 2))#candidate|4877|(6, 6, 2)|var|float64
var_4878 = relay.var("var_4878", dtype = "uint32", shape = (16, 4))#candidate|4878|(16, 4)|var|uint32
output = func_4875(var_4876,var_4877,var_4878,)
func_4879 = relay.Function([var_4876,var_4877,var_4878,], output)
mutated_mod['func_4879'] = func_4879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4379_call = mod.get_global_var('func_4379')
func_4381_call = mutated_mod.get_global_var('func_4381')
call_4891 = relay.TupleGetItem(func_4379_call(), 0)
call_4892 = relay.TupleGetItem(func_4381_call(), 0)
output = relay.Tuple([call_4891,])
output2 = relay.Tuple([call_4892,])
func_4895 = relay.Function([], output)
mod['func_4895'] = func_4895
mod = relay.transform.InferType()(mod)
mutated_mod['func_4895'] = func_4895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4895_call = mutated_mod.get_global_var('func_4895')
call_4896 = func_4895_call()
output = call_4896
func_4897 = relay.Function([], output)
mutated_mod['func_4897'] = func_4897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2132_call = mod.get_global_var('func_2132')
func_2134_call = mutated_mod.get_global_var('func_2134')
call_4906 = func_2132_call()
call_4907 = func_2132_call()
func_4606_call = mod.get_global_var('func_4606')
func_4609_call = mutated_mod.get_global_var('func_4609')
var_4934 = relay.var("var_4934", dtype = "float64", shape = (384,))#candidate|4934|(384,)|var|float64
call_4933 = relay.TupleGetItem(func_4606_call(relay.reshape(var_4934.astype('float64'), [384,])), 1)
call_4935 = relay.TupleGetItem(func_4609_call(relay.reshape(var_4934.astype('float64'), [384,])), 1)
output = relay.Tuple([call_4906,call_4933,var_4934,])
output2 = relay.Tuple([call_4907,call_4935,var_4934,])
func_4948 = relay.Function([var_4934,], output)
mod['func_4948'] = func_4948
mod = relay.transform.InferType()(mod)
mutated_mod['func_4948'] = func_4948
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4949 = relay.var("var_4949", dtype = "float64", shape = (384,))#candidate|4949|(384,)|var|float64
func_4948_call = mutated_mod.get_global_var('func_4948')
call_4950 = func_4948_call(var_4949)
output = call_4950
func_4951 = relay.Function([var_4949], output)
mutated_mod['func_4951'] = func_4951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_4975 = func_2031_call()
call_4976 = func_2031_call()
func_1421_call = mod.get_global_var('func_1421')
func_1424_call = mutated_mod.get_global_var('func_1424')
var_5018 = relay.var("var_5018", dtype = "uint16", shape = (448,))#candidate|5018|(448,)|var|uint16
call_5017 = relay.TupleGetItem(func_1421_call(relay.reshape(var_5018.astype('uint16'), [14, 2, 16])), 0)
call_5019 = relay.TupleGetItem(func_1424_call(relay.reshape(var_5018.astype('uint16'), [14, 2, 16])), 0)
func_4272_call = mod.get_global_var('func_4272')
func_4274_call = mutated_mod.get_global_var('func_4274')
call_5034 = func_4272_call()
call_5035 = func_4272_call()
func_3043_call = mod.get_global_var('func_3043')
func_3045_call = mutated_mod.get_global_var('func_3045')
call_5050 = relay.TupleGetItem(func_3043_call(), 0)
call_5051 = relay.TupleGetItem(func_3045_call(), 0)
output = relay.Tuple([call_4975,call_5017,var_5018,call_5034,call_5050,])
output2 = relay.Tuple([call_4976,call_5019,var_5018,call_5035,call_5051,])
func_5054 = relay.Function([var_5018,], output)
mod['func_5054'] = func_5054
mod = relay.transform.InferType()(mod)
mutated_mod['func_5054'] = func_5054
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5055 = relay.var("var_5055", dtype = "uint16", shape = (448,))#candidate|5055|(448,)|var|uint16
func_5054_call = mutated_mod.get_global_var('func_5054')
call_5056 = func_5054_call(var_5055)
output = call_5056
func_5057 = relay.Function([var_5055], output)
mutated_mod['func_5057'] = func_5057
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5081 = relay.var("var_5081", dtype = "int64", shape = (11, 10, 8))#candidate|5081|(11, 10, 8)|var|int64
var_5082 = relay.var("var_5082", dtype = "int64", shape = (11, 10, 8))#candidate|5082|(11, 10, 8)|var|int64
bop_5083 = relay.bitwise_or(var_5081.astype('int64'), relay.reshape(var_5082.astype('int64'), relay.shape_of(var_5081))) # shape=(11, 10, 8)
bop_5088 = relay.add(var_5082.astype('float32'), relay.reshape(bop_5083.astype('float32'), relay.shape_of(var_5082))) # shape=(11, 10, 8)
bop_5100 = relay.not_equal(var_5081.astype('bool'), relay.reshape(var_5082.astype('bool'), relay.shape_of(var_5081))) # shape=(11, 10, 8)
output = relay.Tuple([bop_5088,bop_5100,])
output2 = relay.Tuple([bop_5088,bop_5100,])
func_5114 = relay.Function([var_5081,var_5082,], output)
mod['func_5114'] = func_5114
mod = relay.transform.InferType()(mod)
var_5115 = relay.var("var_5115", dtype = "int64", shape = (11, 10, 8))#candidate|5115|(11, 10, 8)|var|int64
var_5116 = relay.var("var_5116", dtype = "int64", shape = (11, 10, 8))#candidate|5116|(11, 10, 8)|var|int64
output = func_5114(var_5115,var_5116,)
func_5117 = relay.Function([var_5115,var_5116,], output)
mutated_mod['func_5117'] = func_5117
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5128 = relay.var("var_5128", dtype = "bool", shape = (4, 5, 11))#candidate|5128|(4, 5, 11)|var|bool
var_5129 = relay.var("var_5129", dtype = "bool", shape = (4, 5, 11))#candidate|5129|(4, 5, 11)|var|bool
bop_5130 = relay.logical_or(var_5128.astype('bool'), relay.reshape(var_5129.astype('bool'), relay.shape_of(var_5128))) # shape=(4, 5, 11)
func_2767_call = mod.get_global_var('func_2767')
func_2768_call = mutated_mod.get_global_var('func_2768')
call_5145 = relay.TupleGetItem(func_2767_call(), 0)
call_5146 = relay.TupleGetItem(func_2768_call(), 0)
output = relay.Tuple([bop_5130,call_5145,])
output2 = relay.Tuple([bop_5130,call_5146,])
func_5165 = relay.Function([var_5128,var_5129,], output)
mod['func_5165'] = func_5165
mod = relay.transform.InferType()(mod)
mutated_mod['func_5165'] = func_5165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5165_call = mutated_mod.get_global_var('func_5165')
var_5167 = relay.var("var_5167", dtype = "bool", shape = (4, 5, 11))#candidate|5167|(4, 5, 11)|var|bool
var_5168 = relay.var("var_5168", dtype = "bool", shape = (4, 5, 11))#candidate|5168|(4, 5, 11)|var|bool
call_5166 = func_5165_call(var_5167,var_5168,)
output = call_5166
func_5169 = relay.Function([var_5167,var_5168,], output)
mutated_mod['func_5169'] = func_5169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3058_call = mod.get_global_var('func_3058')
func_3060_call = mutated_mod.get_global_var('func_3060')
call_5224 = relay.TupleGetItem(func_3058_call(), 1)
call_5225 = relay.TupleGetItem(func_3060_call(), 1)
func_2046_call = mod.get_global_var('func_2046')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_5231 = func_2046_call()
call_5232 = func_2046_call()
func_3204_call = mod.get_global_var('func_3204')
func_3206_call = mutated_mod.get_global_var('func_3206')
call_5236 = func_3204_call()
call_5237 = func_3204_call()
output = relay.Tuple([call_5224,call_5231,call_5236,])
output2 = relay.Tuple([call_5225,call_5232,call_5237,])
func_5238 = relay.Function([], output)
mod['func_5238'] = func_5238
mod = relay.transform.InferType()(mod)
output = func_5238()
func_5239 = relay.Function([], output)
mutated_mod['func_5239'] = func_5239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_5249 = func_1055_call()
call_5250 = func_1055_call()
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_5272 = relay.TupleGetItem(func_957_call(), 0)
call_5273 = relay.TupleGetItem(func_958_call(), 0)
func_2479_call = mod.get_global_var('func_2479')
func_2481_call = mutated_mod.get_global_var('func_2481')
call_5278 = relay.TupleGetItem(func_2479_call(), 0)
call_5279 = relay.TupleGetItem(func_2481_call(), 0)
func_4116_call = mod.get_global_var('func_4116')
func_4118_call = mutated_mod.get_global_var('func_4118')
call_5311 = func_4116_call()
call_5312 = func_4116_call()
func_1857_call = mod.get_global_var('func_1857')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_5315 = func_1857_call()
call_5316 = func_1857_call()
func_3452_call = mod.get_global_var('func_3452')
func_3454_call = mutated_mod.get_global_var('func_3454')
call_5340 = relay.TupleGetItem(func_3452_call(), 0)
call_5341 = relay.TupleGetItem(func_3454_call(), 0)
output = relay.Tuple([call_5249,call_5272,call_5278,call_5311,call_5315,call_5340,])
output2 = relay.Tuple([call_5250,call_5273,call_5279,call_5312,call_5316,call_5341,])
func_5349 = relay.Function([], output)
mod['func_5349'] = func_5349
mod = relay.transform.InferType()(mod)
output = func_5349()
func_5350 = relay.Function([], output)
mutated_mod['func_5350'] = func_5350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2597_call = mod.get_global_var('func_2597')
func_2599_call = mutated_mod.get_global_var('func_2599')
call_5353 = func_2597_call()
call_5354 = func_2597_call()
func_2684_call = mod.get_global_var('func_2684')
func_2686_call = mutated_mod.get_global_var('func_2686')
call_5358 = relay.TupleGetItem(func_2684_call(), 0)
call_5359 = relay.TupleGetItem(func_2686_call(), 0)
func_4379_call = mod.get_global_var('func_4379')
func_4381_call = mutated_mod.get_global_var('func_4381')
call_5364 = relay.TupleGetItem(func_4379_call(), 0)
call_5365 = relay.TupleGetItem(func_4381_call(), 0)
output = relay.Tuple([call_5353,call_5358,call_5364,])
output2 = relay.Tuple([call_5354,call_5359,call_5365,])
func_5376 = relay.Function([], output)
mod['func_5376'] = func_5376
mod = relay.transform.InferType()(mod)
output = func_5376()
func_5377 = relay.Function([], output)
mutated_mod['func_5377'] = func_5377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_5378 = relay.TupleGetItem(func_1758_call(), 1)
call_5379 = relay.TupleGetItem(func_1760_call(), 1)
func_1462_call = mod.get_global_var('func_1462')
func_1465_call = mutated_mod.get_global_var('func_1465')
const_5381 = relay.const([[0.390017,-0.023957,9.605296,-1.136437,-9.984524,7.578690,0.024467,5.081582,-1.650419,4.543414],[9.298324,-7.872844,7.689424,-7.978056,-7.322844,-9.965345,-9.154080,-9.470458,1.083204,-0.358458],[2.120479,3.848232,0.172974,-9.802901,-2.386489,2.412391,5.527849,-1.136262,5.889065,-3.580622],[-2.414757,3.045172,-7.607425,-9.597456,3.608315,4.453277,-2.481030,1.123288,-5.140985,3.755533],[6.161813,-1.174143,6.057964,-7.881384,1.695993,-4.705324,2.819330,-0.280258,6.705992,-1.913512],[9.358056,9.023193,-0.900691,4.674625,-6.147692,-1.336790,-2.965742,-2.801781,2.780568,-3.726887],[5.050797,-5.763981,1.582230,-4.877277,2.044301,5.936384,7.289818,-2.335389,7.253234,-4.428890],[-8.604571,-4.106279,4.140724,-4.199911,5.402189,4.832566,5.843654,6.191863,2.992130,7.448502],[-2.493230,8.180309,0.940426,-8.873533,-3.198812,-5.829988,8.651484,0.206314,4.188037,4.558731],[-2.287647,-0.335047,-7.941929,-8.468917,1.460661,-4.542306,-5.544590,5.814071,8.067917,5.060871],[-3.437505,-8.907628,-9.066935,-5.696022,-8.477583,-1.622848,7.858456,-6.961738,-9.576781,9.350316],[4.996111,-6.361899,6.071444,6.483162,4.725983,-6.435242,2.842325,3.886615,-6.303488,1.891517],[8.292722,-9.065040,-5.482262,-2.034822,9.477541,5.825611,2.355967,2.421563,8.828116,9.924303],[6.453779,1.749255,-8.322856,-0.788748,-6.279937,6.780609,0.634038,-7.846854,2.970266,-5.130518],[-5.570722,8.940159,5.728227,9.342786,5.426983,1.429886,-4.830814,3.677967,2.843270,-9.289029],[-6.774552,6.748378,9.755553,6.342514,-0.189341,1.700753,9.750665,-0.702281,4.434788,-8.863944],[-0.021618,4.849645,-5.080555,-0.894855,-7.938825,4.720980,-0.919457,-2.925379,1.802068,-5.589595],[-9.478624,-6.298294,-7.623266,-2.337719,-2.014222,7.639733,9.899984,-5.337475,6.572197,9.990794],[3.392949,-2.396204,-8.447999,7.649281,1.709234,2.412768,8.782082,7.743490,0.634821,-3.132575],[-6.371725,-8.628126,-4.350378,3.976143,1.882675,-8.663129,-1.814065,4.173934,7.866304,-1.966143],[-3.895786,-6.946720,0.017080,-2.331677,-8.631217,2.156225,-4.995428,-5.815767,-4.913182,-2.474077],[-4.420804,-9.238941,-6.444449,7.503430,-8.991655,-6.961646,-3.313849,-6.633704,-1.121172,-4.202483],[9.515467,-2.165819,0.201088,0.233951,-7.553725,-7.365048,-2.965913,5.354980,-3.956943,-0.409733],[-4.635007,6.203576,-1.554876,6.745760,-8.652372,6.467854,1.150301,6.825765,-8.402119,-4.611820],[8.324072,5.541898,2.285484,-3.410260,-1.671119,-6.253984,6.305228,4.824036,6.234301,-2.919726],[-6.395780,-2.572557,4.110835,-5.220280,-7.659799,0.204958,1.293984,0.261606,9.309553,-1.103027],[-0.377718,0.250597,0.267657,9.440523,7.075513,-9.727777,5.843912,7.222993,0.956832,-7.949415],[-7.504112,1.270995,7.245692,-6.068921,-4.897375,-9.179703,5.127627,-9.373340,-9.354357,5.798380],[5.803506,9.470314,-6.354905,-6.027736,-4.955628,5.174463,-2.754872,3.529627,8.043008,-4.057250],[-1.830760,4.879199,-6.893832,-4.966230,7.279539,-5.516970,-7.697829,-5.250454,-3.860236,-2.907001],[6.109883,9.069484,-8.108428,8.721473,-8.960123,5.350722,-1.827166,-4.522249,-2.295340,7.100995],[2.179501,-1.953871,1.897690,-6.881761,7.669409,3.388114,6.421204,-0.815158,3.676150,9.393873],[-5.827525,-1.929967,4.898779,6.157182,-8.199615,-0.031578,1.435088,7.035612,5.915744,-1.733057],[-0.379828,9.873782,9.001389,4.365760,-4.999381,-8.876957,2.575867,4.870598,-5.696375,-3.129231],[-5.300429,-3.531070,5.705308,-4.293892,5.897866,-5.882980,-3.179437,7.249117,9.120996,-0.173133],[-9.363544,-5.312694,-5.949960,-6.185270,9.682752,0.049739,9.278613,5.024031,0.338552,6.043995]], dtype = "float64")#candidate|5381|(36, 10)|const|float64
call_5380 = relay.TupleGetItem(func_1462_call(relay.reshape(const_5381.astype('float64'), [6, 6, 10]), relay.reshape(call_5378.astype('uint32'), [8, 8]), ), 0)
call_5382 = relay.TupleGetItem(func_1465_call(relay.reshape(const_5381.astype('float64'), [6, 6, 10]), relay.reshape(call_5378.astype('uint32'), [8, 8]), ), 0)
output = relay.Tuple([call_5378,call_5380,const_5381,])
output2 = relay.Tuple([call_5379,call_5382,const_5381,])
func_5385 = relay.Function([], output)
mod['func_5385'] = func_5385
mod = relay.transform.InferType()(mod)
mutated_mod['func_5385'] = func_5385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5385_call = mutated_mod.get_global_var('func_5385')
call_5386 = func_5385_call()
output = call_5386
func_5387 = relay.Function([], output)
mutated_mod['func_5387'] = func_5387
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5400 = relay.const([[[4,-4],[5,-6],[-4,-2]],[[-9,1],[-3,-10],[-2,10]],[[-4,8],[4,10],[7,10]],[[5,-4],[2,1],[-10,9]],[[-3,-6],[5,4],[8,3]],[[-5,1],[-8,-3],[-7,-4]],[[-3,-10],[-7,-6],[8,-3]],[[8,4],[1,-10],[-2,-8]]], dtype = "uint32")#candidate|5400|(8, 3, 2)|const|uint32
var_5401 = relay.var("var_5401", dtype = "uint32", shape = (8, 3, 2))#candidate|5401|(8, 3, 2)|var|uint32
bop_5402 = relay.bitwise_or(const_5400.astype('uint32'), relay.reshape(var_5401.astype('uint32'), relay.shape_of(const_5400))) # shape=(8, 3, 2)
var_5407 = relay.var("var_5407", dtype = "uint32", shape = (8, 3, 2))#candidate|5407|(8, 3, 2)|var|uint32
bop_5408 = relay.less_equal(bop_5402.astype('bool'), relay.reshape(var_5407.astype('bool'), relay.shape_of(bop_5402))) # shape=(8, 3, 2)
output = bop_5408
output2 = bop_5408
func_5422 = relay.Function([var_5401,var_5407,], output)
mod['func_5422'] = func_5422
mod = relay.transform.InferType()(mod)
var_5423 = relay.var("var_5423", dtype = "uint32", shape = (8, 3, 2))#candidate|5423|(8, 3, 2)|var|uint32
var_5424 = relay.var("var_5424", dtype = "uint32", shape = (8, 3, 2))#candidate|5424|(8, 3, 2)|var|uint32
output = func_5422(var_5423,var_5424,)
func_5425 = relay.Function([var_5423,var_5424,], output)
mutated_mod['func_5425'] = func_5425
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5448 = relay.var("var_5448", dtype = "float32", shape = (9, 3, 6))#candidate|5448|(9, 3, 6)|var|float32
uop_5449 = relay.exp(var_5448.astype('float32')) # shape=(9, 3, 6)
uop_5465 = relay.sqrt(uop_5449.astype('float32')) # shape=(9, 3, 6)
func_2243_call = mod.get_global_var('func_2243')
func_2248_call = mutated_mod.get_global_var('func_2248')
var_5475 = relay.var("var_5475", dtype = "int32", shape = (16,))#candidate|5475|(16,)|var|int32
var_5476 = relay.var("var_5476", dtype = "int8", shape = ())#candidate|5476|()|var|int8
var_5477 = relay.var("var_5477", dtype = "uint16", shape = (2, 224))#candidate|5477|(2, 224)|var|uint16
call_5474 = relay.TupleGetItem(func_2243_call(relay.reshape(var_5475.astype('int32'), [1, 16]), relay.reshape(var_5476.astype('int8'), []), relay.reshape(var_5477.astype('uint16'), [448,]), ), 0)
call_5478 = relay.TupleGetItem(func_2248_call(relay.reshape(var_5475.astype('int32'), [1, 16]), relay.reshape(var_5476.astype('int8'), []), relay.reshape(var_5477.astype('uint16'), [448,]), ), 0)
output = relay.Tuple([uop_5465,call_5474,var_5475,var_5476,var_5477,])
output2 = relay.Tuple([uop_5465,call_5478,var_5475,var_5476,var_5477,])
func_5483 = relay.Function([var_5448,var_5475,var_5476,var_5477,], output)
mod['func_5483'] = func_5483
mod = relay.transform.InferType()(mod)
var_5484 = relay.var("var_5484", dtype = "float32", shape = (9, 3, 6))#candidate|5484|(9, 3, 6)|var|float32
var_5485 = relay.var("var_5485", dtype = "int32", shape = (16,))#candidate|5485|(16,)|var|int32
var_5486 = relay.var("var_5486", dtype = "int8", shape = ())#candidate|5486|()|var|int8
var_5487 = relay.var("var_5487", dtype = "uint16", shape = (2, 224))#candidate|5487|(2, 224)|var|uint16
output = func_5483(var_5484,var_5485,var_5486,var_5487,)
func_5488 = relay.Function([var_5484,var_5485,var_5486,var_5487,], output)
mutated_mod['func_5488'] = func_5488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3177_call = mod.get_global_var('func_3177')
func_3179_call = mutated_mod.get_global_var('func_3179')
call_5495 = relay.TupleGetItem(func_3177_call(), 0)
call_5496 = relay.TupleGetItem(func_3179_call(), 0)
func_3887_call = mod.get_global_var('func_3887')
func_3888_call = mutated_mod.get_global_var('func_3888')
call_5500 = relay.TupleGetItem(func_3887_call(), 0)
call_5501 = relay.TupleGetItem(func_3888_call(), 0)
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_5503 = func_2651_call()
call_5504 = func_2651_call()
func_778_call = mod.get_global_var('func_778')
func_784_call = mutated_mod.get_global_var('func_784')
const_5506 = relay.const([5,-7,10,9,-5,-3,-1,-6,8,6,-10,-4,-3,-1,8,-6], dtype = "int32")#candidate|5506|(16,)|const|int32
var_5507 = relay.var("var_5507", dtype = "int32", shape = (160,))#candidate|5507|(160,)|var|int32
const_5508 = relay.const(9, dtype = "int8")#candidate|5508|()|const|int8
call_5505 = relay.TupleGetItem(func_778_call(relay.reshape(const_5506.astype('int32'), [16,]), relay.reshape(var_5507.astype('int32'), [160,]), relay.reshape(const_5508.astype('int8'), []), relay.reshape(call_5500.astype('int8'), [200,]), ), 4)
call_5509 = relay.TupleGetItem(func_784_call(relay.reshape(const_5506.astype('int32'), [16,]), relay.reshape(var_5507.astype('int32'), [160,]), relay.reshape(const_5508.astype('int8'), []), relay.reshape(call_5500.astype('int8'), [200,]), ), 4)
func_2610_call = mod.get_global_var('func_2610')
func_2612_call = mutated_mod.get_global_var('func_2612')
var_5515 = relay.var("var_5515", dtype = "float64", shape = (260, 1))#candidate|5515|(260, 1)|var|float64
call_5514 = relay.TupleGetItem(func_2610_call(relay.reshape(var_5515.astype('float64'), [4, 5, 13])), 0)
call_5516 = relay.TupleGetItem(func_2612_call(relay.reshape(var_5515.astype('float64'), [4, 5, 13])), 0)
output = relay.Tuple([call_5495,call_5500,call_5503,call_5505,const_5506,var_5507,const_5508,call_5514,var_5515,])
output2 = relay.Tuple([call_5496,call_5501,call_5504,call_5509,const_5506,var_5507,const_5508,call_5516,var_5515,])
func_5517 = relay.Function([var_5507,var_5515,], output)
mod['func_5517'] = func_5517
mod = relay.transform.InferType()(mod)
mutated_mod['func_5517'] = func_5517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5517_call = mutated_mod.get_global_var('func_5517')
var_5519 = relay.var("var_5519", dtype = "int32", shape = (160,))#candidate|5519|(160,)|var|int32
var_5520 = relay.var("var_5520", dtype = "float64", shape = (260, 1))#candidate|5520|(260, 1)|var|float64
call_5518 = func_5517_call(var_5519,var_5520,)
output = call_5518
func_5521 = relay.Function([var_5519,var_5520,], output)
mutated_mod['func_5521'] = func_5521
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5541 = relay.const([[[-7.062532,-5.265677,9.576940,-3.091728,-3.294490,-7.097853,4.849991,6.709555],[9.525646,-9.167890,3.695655,-4.811604,-1.055360,-4.066862,-4.735651,8.653792],[-5.373446,9.886788,0.547813,-5.024957,-8.411656,-4.232035,-0.776953,2.707382],[3.392832,-1.785532,-5.972191,5.642575,3.012334,4.481718,-4.414061,-0.031626],[2.751570,-9.704866,6.922365,-3.618496,-5.904535,-0.726644,-8.218508,-3.924890],[4.980596,9.856664,3.998599,9.387291,-4.881078,-7.557617,7.619603,-9.782431],[-9.522614,3.639680,3.417362,3.903684,-3.538064,9.458648,2.759578,-5.632484],[-5.457137,-0.471168,-3.187962,-0.094793,5.532731,0.664708,5.202940,1.926500],[1.980444,-5.188492,-7.675868,-3.553794,0.316399,6.336037,9.855159,9.160433],[6.512510,5.779714,6.421534,6.999661,-7.817636,0.682204,-7.739551,-8.602421],[1.306844,-5.291062,-8.575802,-2.405767,-3.344807,4.262935,2.248217,3.345970],[-1.184722,6.261923,-7.132771,-0.215482,0.770998,5.346844,-7.329951,4.194386]]], dtype = "float32")#candidate|5541|(1, 12, 8)|const|float32
uop_5542 = relay.acosh(const_5541.astype('float32')) # shape=(1, 12, 8)
func_2384_call = mod.get_global_var('func_2384')
func_2386_call = mutated_mod.get_global_var('func_2386')
call_5552 = relay.TupleGetItem(func_2384_call(), 1)
call_5553 = relay.TupleGetItem(func_2386_call(), 1)
uop_5555 = relay.sinh(uop_5542.astype('float64')) # shape=(1, 12, 8)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_5561 = relay.TupleGetItem(func_957_call(), 0)
call_5562 = relay.TupleGetItem(func_958_call(), 0)
output = relay.Tuple([call_5552,uop_5555,call_5561,])
output2 = relay.Tuple([call_5553,uop_5555,call_5562,])
func_5563 = relay.Function([], output)
mod['func_5563'] = func_5563
mod = relay.transform.InferType()(mod)
mutated_mod['func_5563'] = func_5563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5563_call = mutated_mod.get_global_var('func_5563')
call_5564 = func_5563_call()
output = call_5564
func_5565 = relay.Function([], output)
mutated_mod['func_5565'] = func_5565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4272_call = mod.get_global_var('func_4272')
func_4274_call = mutated_mod.get_global_var('func_4274')
call_5596 = func_4272_call()
call_5597 = func_4272_call()
output = relay.Tuple([call_5596,])
output2 = relay.Tuple([call_5597,])
func_5607 = relay.Function([], output)
mod['func_5607'] = func_5607
mod = relay.transform.InferType()(mod)
output = func_5607()
func_5608 = relay.Function([], output)
mutated_mod['func_5608'] = func_5608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5349_call = mod.get_global_var('func_5349')
func_5350_call = mutated_mod.get_global_var('func_5350')
call_5613 = relay.TupleGetItem(func_5349_call(), 5)
call_5614 = relay.TupleGetItem(func_5350_call(), 5)
func_4379_call = mod.get_global_var('func_4379')
func_4381_call = mutated_mod.get_global_var('func_4381')
call_5620 = relay.TupleGetItem(func_4379_call(), 1)
call_5621 = relay.TupleGetItem(func_4381_call(), 1)
output = relay.Tuple([call_5613,call_5620,])
output2 = relay.Tuple([call_5614,call_5621,])
func_5630 = relay.Function([], output)
mod['func_5630'] = func_5630
mod = relay.transform.InferType()(mod)
output = func_5630()
func_5631 = relay.Function([], output)
mutated_mod['func_5631'] = func_5631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_5733 = func_1055_call()
call_5734 = func_1055_call()
output = call_5733
output2 = call_5734
func_5737 = relay.Function([], output)
mod['func_5737'] = func_5737
mod = relay.transform.InferType()(mod)
mutated_mod['func_5737'] = func_5737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5737_call = mutated_mod.get_global_var('func_5737')
call_5738 = func_5737_call()
output = call_5738
func_5739 = relay.Function([], output)
mutated_mod['func_5739'] = func_5739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2597_call = mod.get_global_var('func_2597')
func_2599_call = mutated_mod.get_global_var('func_2599')
call_5771 = func_2597_call()
call_5772 = func_2597_call()
func_1303_call = mod.get_global_var('func_1303')
func_1305_call = mutated_mod.get_global_var('func_1305')
const_5791 = relay.const([10,-3,10,5,-1,-7,-2,5,4,-3,-10,-4,6,-8,-2,2,3,-1,7,6,-2,9,1,-8,-7,-1,-10,9,10,-8,2,-4,-5,-9,-9,-2,-7,-5,-6,3,-5,-2,9,4,3,-10,10,-10,-9,7,4,-10,-2,-7,-7,-4,3,1,9,1,-5,-7,-7,2,-5,-5,-10,-8,-8,-1,-5,1,-2,2,-8,-5,4,-10,8,6,-2,-2,3,-5,5,8,-2,10,1,-9,-4,2,6,-6,5,-8,10,1,10,-6,1,-4,3,1,7,1,-6,-7,6,-7,-5,9,-4,1,-6,8,-1,2,-10,7,5,-7,2,3,9,-2,4,-4,-2,4,-1,7,7,-7,-4,-2,-4,-2,-5,8,-7,-10,2,1,8,1,-8,-5,-10,1,9,-5,-6,-3,3,7,-2,1,1,-7,7,-2,6,1,-2,-10,-8,5,-3,5,2,8,-8,-5,10,10,9,4,9,-3,-8,1,-9,9,9,-10,3,2,-6,2,8,-5,6,-4,5,-6,-2,6,-7,5], dtype = "int8")#candidate|5791|(200,)|const|int8
call_5790 = relay.TupleGetItem(func_1303_call(relay.reshape(const_5791.astype('int8'), [200,])), 3)
call_5792 = relay.TupleGetItem(func_1305_call(relay.reshape(const_5791.astype('int8'), [200,])), 3)
var_5806 = relay.var("var_5806", dtype = "uint32", shape = (2, 8, 4))#candidate|5806|(2, 8, 4)|var|uint32
bop_5807 = relay.not_equal(call_5771.astype('bool'), relay.reshape(var_5806.astype('bool'), relay.shape_of(call_5771))) # shape=(2, 8, 4)
bop_5810 = relay.not_equal(call_5772.astype('bool'), relay.reshape(var_5806.astype('bool'), relay.shape_of(call_5772))) # shape=(2, 8, 4)
func_3581_call = mod.get_global_var('func_3581')
func_3583_call = mutated_mod.get_global_var('func_3583')
call_5814 = relay.TupleGetItem(func_3581_call(), 0)
call_5815 = relay.TupleGetItem(func_3583_call(), 0)
func_3058_call = mod.get_global_var('func_3058')
func_3060_call = mutated_mod.get_global_var('func_3060')
call_5819 = relay.TupleGetItem(func_3058_call(), 0)
call_5820 = relay.TupleGetItem(func_3060_call(), 0)
output = relay.Tuple([call_5790,const_5791,bop_5807,call_5814,call_5819,])
output2 = relay.Tuple([call_5792,const_5791,bop_5810,call_5815,call_5820,])
func_5821 = relay.Function([var_5806,], output)
mod['func_5821'] = func_5821
mod = relay.transform.InferType()(mod)
var_5822 = relay.var("var_5822", dtype = "uint32", shape = (2, 8, 4))#candidate|5822|(2, 8, 4)|var|uint32
output = func_5821(var_5822)
func_5823 = relay.Function([var_5822], output)
mutated_mod['func_5823'] = func_5823
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6005 = relay.var("var_6005", dtype = "float32", shape = (9, 7, 6))#candidate|6005|(9, 7, 6)|var|float32
uop_6006 = relay.log2(var_6005.astype('float32')) # shape=(9, 7, 6)
output = relay.Tuple([uop_6006,])
output2 = relay.Tuple([uop_6006,])
func_6010 = relay.Function([var_6005,], output)
mod['func_6010'] = func_6010
mod = relay.transform.InferType()(mod)
mutated_mod['func_6010'] = func_6010
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6011 = relay.var("var_6011", dtype = "float32", shape = (9, 7, 6))#candidate|6011|(9, 7, 6)|var|float32
func_6010_call = mutated_mod.get_global_var('func_6010')
call_6012 = func_6010_call(var_6011)
output = call_6012
func_6013 = relay.Function([var_6011], output)
mutated_mod['func_6013'] = func_6013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4137_call = mod.get_global_var('func_4137')
func_4139_call = mutated_mod.get_global_var('func_4139')
call_6061 = relay.TupleGetItem(func_4137_call(), 1)
call_6062 = relay.TupleGetItem(func_4139_call(), 1)
func_3581_call = mod.get_global_var('func_3581')
func_3583_call = mutated_mod.get_global_var('func_3583')
call_6064 = relay.TupleGetItem(func_3581_call(), 0)
call_6065 = relay.TupleGetItem(func_3583_call(), 0)
output = relay.Tuple([call_6061,call_6064,])
output2 = relay.Tuple([call_6062,call_6065,])
func_6068 = relay.Function([], output)
mod['func_6068'] = func_6068
mod = relay.transform.InferType()(mod)
mutated_mod['func_6068'] = func_6068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6068_call = mutated_mod.get_global_var('func_6068')
call_6069 = func_6068_call()
output = call_6069
func_6070 = relay.Function([], output)
mutated_mod['func_6070'] = func_6070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1386_call = mod.get_global_var('func_1386')
func_1388_call = mutated_mod.get_global_var('func_1388')
call_6074 = func_1386_call()
call_6075 = func_1386_call()
func_1224_call = mod.get_global_var('func_1224')
func_1228_call = mutated_mod.get_global_var('func_1228')
var_6108 = relay.var("var_6108", dtype = "int8", shape = ())#candidate|6108|()|var|int8
call_6107 = relay.TupleGetItem(func_1224_call(relay.reshape(var_6108.astype('int8'), []), relay.reshape(call_6074.astype('float32'), [2, 8, 4]), ), 6)
call_6109 = relay.TupleGetItem(func_1228_call(relay.reshape(var_6108.astype('int8'), []), relay.reshape(call_6074.astype('float32'), [2, 8, 4]), ), 6)
output = relay.Tuple([call_6074,call_6107,var_6108,])
output2 = relay.Tuple([call_6075,call_6109,var_6108,])
func_6119 = relay.Function([var_6108,], output)
mod['func_6119'] = func_6119
mod = relay.transform.InferType()(mod)
mutated_mod['func_6119'] = func_6119
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6120 = relay.var("var_6120", dtype = "int8", shape = ())#candidate|6120|()|var|int8
func_6119_call = mutated_mod.get_global_var('func_6119')
call_6121 = func_6119_call(var_6120)
output = call_6121
func_6122 = relay.Function([var_6120], output)
mutated_mod['func_6122'] = func_6122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1857_call = mod.get_global_var('func_1857')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_6149 = func_1857_call()
call_6150 = func_1857_call()
func_5821_call = mod.get_global_var('func_5821')
func_5823_call = mutated_mod.get_global_var('func_5823')
call_6157 = relay.TupleGetItem(func_5821_call(relay.reshape(call_6149.astype('uint32'), [2, 8, 4])), 2)
call_6158 = relay.TupleGetItem(func_5823_call(relay.reshape(call_6149.astype('uint32'), [2, 8, 4])), 2)
func_1742_call = mod.get_global_var('func_1742')
func_1744_call = mutated_mod.get_global_var('func_1744')
const_6160 = relay.const([-1,6,-6,-10,-6,5,-9,-1,-7,1,5,7,6,3,2,-3], dtype = "int32")#candidate|6160|(16,)|const|int32
call_6159 = relay.TupleGetItem(func_1742_call(relay.reshape(const_6160.astype('int32'), [1, 16])), 1)
call_6161 = relay.TupleGetItem(func_1744_call(relay.reshape(const_6160.astype('int32'), [1, 16])), 1)
output = relay.Tuple([call_6149,call_6157,call_6159,const_6160,])
output2 = relay.Tuple([call_6150,call_6158,call_6161,const_6160,])
func_6165 = relay.Function([], output)
mod['func_6165'] = func_6165
mod = relay.transform.InferType()(mod)
output = func_6165()
func_6166 = relay.Function([], output)
mutated_mod['func_6166'] = func_6166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4137_call = mod.get_global_var('func_4137')
func_4139_call = mutated_mod.get_global_var('func_4139')
call_6176 = relay.TupleGetItem(func_4137_call(), 1)
call_6177 = relay.TupleGetItem(func_4139_call(), 1)
func_4236_call = mod.get_global_var('func_4236')
func_4241_call = mutated_mod.get_global_var('func_4241')
var_6179 = relay.var("var_6179", dtype = "float64", shape = ())#candidate|6179|()|var|float64
var_6180 = relay.var("var_6180", dtype = "float64", shape = (2, 1))#candidate|6180|(2, 1)|var|float64
var_6181 = relay.var("var_6181", dtype = "uint16", shape = (8, 56))#candidate|6181|(8, 56)|var|uint16
call_6178 = relay.TupleGetItem(func_4236_call(relay.reshape(var_6179.astype('float64'), []), relay.reshape(var_6180.astype('float64'), [2, 1]), relay.reshape(var_6181.astype('uint16'), [448,]), ), 3)
call_6182 = relay.TupleGetItem(func_4241_call(relay.reshape(var_6179.astype('float64'), []), relay.reshape(var_6180.astype('float64'), [2, 1]), relay.reshape(var_6181.astype('uint16'), [448,]), ), 3)
output = relay.Tuple([call_6176,call_6178,var_6179,var_6180,var_6181,])
output2 = relay.Tuple([call_6177,call_6182,var_6179,var_6180,var_6181,])
func_6201 = relay.Function([var_6179,var_6180,var_6181,], output)
mod['func_6201'] = func_6201
mod = relay.transform.InferType()(mod)
var_6202 = relay.var("var_6202", dtype = "float64", shape = ())#candidate|6202|()|var|float64
var_6203 = relay.var("var_6203", dtype = "float64", shape = (2, 1))#candidate|6203|(2, 1)|var|float64
var_6204 = relay.var("var_6204", dtype = "uint16", shape = (8, 56))#candidate|6204|(8, 56)|var|uint16
output = func_6201(var_6202,var_6203,var_6204,)
func_6205 = relay.Function([var_6202,var_6203,var_6204,], output)
mutated_mod['func_6205'] = func_6205
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6226 = relay.var("var_6226", dtype = "bool", shape = ())#candidate|6226|()|var|bool
var_6227 = relay.var("var_6227", dtype = "bool", shape = (11, 14, 7))#candidate|6227|(11, 14, 7)|var|bool
bop_6228 = relay.logical_and(var_6226.astype('bool'), var_6227.astype('bool')) # shape=(11, 14, 7)
func_5349_call = mod.get_global_var('func_5349')
func_5350_call = mutated_mod.get_global_var('func_5350')
call_6232 = relay.TupleGetItem(func_5349_call(), 5)
call_6233 = relay.TupleGetItem(func_5350_call(), 5)
func_3887_call = mod.get_global_var('func_3887')
func_3888_call = mutated_mod.get_global_var('func_3888')
call_6234 = relay.TupleGetItem(func_3887_call(), 1)
call_6235 = relay.TupleGetItem(func_3888_call(), 1)
bop_6241 = relay.left_shift(var_6227.astype('int64'), var_6226.astype('int64')) # shape=(11, 14, 7)
var_6259 = relay.var("var_6259", dtype = "bool", shape = (11, 14, 7))#candidate|6259|(11, 14, 7)|var|bool
bop_6260 = relay.greater(bop_6228.astype('bool'), relay.reshape(var_6259.astype('bool'), relay.shape_of(bop_6228))) # shape=(11, 14, 7)
func_1421_call = mod.get_global_var('func_1421')
func_1424_call = mutated_mod.get_global_var('func_1424')
var_6298 = relay.var("var_6298", dtype = "uint16", shape = (112, 4))#candidate|6298|(112, 4)|var|uint16
call_6297 = relay.TupleGetItem(func_1421_call(relay.reshape(var_6298.astype('uint16'), [14, 2, 16])), 0)
call_6299 = relay.TupleGetItem(func_1424_call(relay.reshape(var_6298.astype('uint16'), [14, 2, 16])), 0)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_6300 = func_2031_call()
call_6301 = func_2031_call()
uop_6310 = relay.erf(var_6298.astype('float32')) # shape=(112, 4)
bop_6315 = relay.logical_and(uop_6310.astype('bool'), var_6226.astype('bool')) # shape=(112, 4)
output = relay.Tuple([call_6232,call_6234,bop_6241,bop_6260,call_6297,call_6300,bop_6315,])
output2 = relay.Tuple([call_6233,call_6235,bop_6241,bop_6260,call_6299,call_6301,bop_6315,])
func_6328 = relay.Function([var_6226,var_6227,var_6259,var_6298,], output)
mod['func_6328'] = func_6328
mod = relay.transform.InferType()(mod)
var_6329 = relay.var("var_6329", dtype = "bool", shape = ())#candidate|6329|()|var|bool
var_6330 = relay.var("var_6330", dtype = "bool", shape = (11, 14, 7))#candidate|6330|(11, 14, 7)|var|bool
var_6331 = relay.var("var_6331", dtype = "bool", shape = (11, 14, 7))#candidate|6331|(11, 14, 7)|var|bool
var_6332 = relay.var("var_6332", dtype = "uint16", shape = (112, 4))#candidate|6332|(112, 4)|var|uint16
output = func_6328(var_6329,var_6330,var_6331,var_6332,)
func_6333 = relay.Function([var_6329,var_6330,var_6331,var_6332,], output)
mutated_mod['func_6333'] = func_6333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4722_call = mod.get_global_var('func_4722')
func_4723_call = mutated_mod.get_global_var('func_4723')
call_6351 = func_4722_call()
call_6352 = func_4722_call()
func_2866_call = mod.get_global_var('func_2866')
func_2868_call = mutated_mod.get_global_var('func_2868')
call_6353 = func_2866_call()
call_6354 = func_2866_call()
output = relay.Tuple([call_6351,call_6353,])
output2 = relay.Tuple([call_6352,call_6354,])
func_6361 = relay.Function([], output)
mod['func_6361'] = func_6361
mod = relay.transform.InferType()(mod)
output = func_6361()
func_6362 = relay.Function([], output)
mutated_mod['func_6362'] = func_6362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6361_call = mod.get_global_var('func_6361')
func_6362_call = mutated_mod.get_global_var('func_6362')
call_6370 = relay.TupleGetItem(func_6361_call(), 1)
call_6371 = relay.TupleGetItem(func_6362_call(), 1)
var_6375 = relay.var("var_6375", dtype = "uint32", shape = (2, 8, 4))#candidate|6375|(2, 8, 4)|var|uint32
bop_6376 = relay.maximum(call_6370.astype('int32'), relay.reshape(var_6375.astype('int32'), relay.shape_of(call_6370))) # shape=(2, 8, 4)
bop_6379 = relay.maximum(call_6371.astype('int32'), relay.reshape(var_6375.astype('int32'), relay.shape_of(call_6371))) # shape=(2, 8, 4)
output = relay.Tuple([bop_6376,])
output2 = relay.Tuple([bop_6379,])
func_6390 = relay.Function([var_6375,], output)
mod['func_6390'] = func_6390
mod = relay.transform.InferType()(mod)
var_6391 = relay.var("var_6391", dtype = "uint32", shape = (2, 8, 4))#candidate|6391|(2, 8, 4)|var|uint32
output = func_6390(var_6391)
func_6392 = relay.Function([var_6391], output)
mutated_mod['func_6392'] = func_6392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2767_call = mod.get_global_var('func_2767')
func_2768_call = mutated_mod.get_global_var('func_2768')
call_6402 = relay.TupleGetItem(func_2767_call(), 0)
call_6403 = relay.TupleGetItem(func_2768_call(), 0)
func_4497_call = mod.get_global_var('func_4497')
func_4501_call = mutated_mod.get_global_var('func_4501')
var_6406 = relay.var("var_6406", dtype = "int8", shape = ())#candidate|6406|()|var|int8
var_6407 = relay.var("var_6407", dtype = "int32", shape = (160,))#candidate|6407|(160,)|var|int32
call_6405 = relay.TupleGetItem(func_4497_call(relay.reshape(call_6402.astype('float64'), [2, 8, 4]), relay.reshape(var_6406.astype('int8'), []), relay.reshape(var_6407.astype('int32'), [160,]), ), 0)
call_6408 = relay.TupleGetItem(func_4501_call(relay.reshape(call_6402.astype('float64'), [2, 8, 4]), relay.reshape(var_6406.astype('int8'), []), relay.reshape(var_6407.astype('int32'), [160,]), ), 0)
output = relay.Tuple([call_6402,call_6405,var_6406,var_6407,])
output2 = relay.Tuple([call_6403,call_6408,var_6406,var_6407,])
func_6413 = relay.Function([var_6406,var_6407,], output)
mod['func_6413'] = func_6413
mod = relay.transform.InferType()(mod)
var_6414 = relay.var("var_6414", dtype = "int8", shape = ())#candidate|6414|()|var|int8
var_6415 = relay.var("var_6415", dtype = "int32", shape = (160,))#candidate|6415|(160,)|var|int32
output = func_6413(var_6414,var_6415,)
func_6416 = relay.Function([var_6414,var_6415,], output)
mutated_mod['func_6416'] = func_6416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2099_call = mod.get_global_var('func_2099')
func_2101_call = mutated_mod.get_global_var('func_2101')
call_6433 = relay.TupleGetItem(func_2099_call(), 0)
call_6434 = relay.TupleGetItem(func_2101_call(), 0)
output = call_6433
output2 = call_6434
func_6437 = relay.Function([], output)
mod['func_6437'] = func_6437
mod = relay.transform.InferType()(mod)
mutated_mod['func_6437'] = func_6437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6437_call = mutated_mod.get_global_var('func_6437')
call_6438 = func_6437_call()
output = call_6438
func_6439 = relay.Function([], output)
mutated_mod['func_6439'] = func_6439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1055_call = mod.get_global_var('func_1055')
func_1057_call = mutated_mod.get_global_var('func_1057')
call_6456 = func_1055_call()
call_6457 = func_1055_call()
func_2404_call = mod.get_global_var('func_2404')
func_2406_call = mutated_mod.get_global_var('func_2406')
const_6459 = relay.const([-7.837960,7.982646,-2.069557,-6.922966,9.013317,-1.593557,8.993564,-8.185514,7.987600,0.069904,-7.761189,-8.424610,-4.577028,0.430676,-9.829439,7.259147,-2.995098,5.707539,3.682700,-7.429750,-1.684655,-3.561701,-8.111991,-2.670351,-5.209815,7.426848,6.407714,9.730735,4.953309,-6.215623,4.667042,5.713929,-2.951705,-6.597009,-8.489907,-8.694796,6.730967,-7.800511,0.353221,8.577713,-5.100835,-0.003048,-8.827217,2.042002,-8.194326,9.558283,-5.076407,-4.806548,4.070076,-5.984730,8.521001,-4.892250,6.267300,-7.620220,4.086603,-2.552122,-2.082359,3.243760,-2.563753,2.232543,-3.131374,-7.001151,5.241573,8.749517,8.482572,-4.904848,6.399767,9.996589,2.207602,1.213928,0.705072,-9.037531,1.949095,-2.194514,4.534770,-4.335788,-0.811691,-8.898483,9.874276,-6.223774,7.606513,2.618511,1.240310,1.210402,-0.276590,5.679715,-3.651252,-6.188099,-3.209905,-4.513992,-1.934246,5.760491,0.618166,-5.194705,-3.309862,-9.165963,6.672917,-6.738212,-3.114056,4.730170,-6.642361,1.616695,-2.635418,-0.181924,-5.289308,-5.450289,-2.439080,-1.685969,1.374067,-6.133864,4.787540,6.319040,6.419217,-2.037621,8.922124,-2.912939,-6.646565,0.778798,4.842050,9.173922,-4.073572,-5.820392,-4.789421,-8.077385,6.293370,3.948969,9.907763,5.593240,-8.553813,5.115777,7.130324,0.938861,9.229837,4.267745,0.573393,-1.391089,-7.891336,-7.525964,7.646371,5.849830,0.275905,-0.346201,1.297925,4.942913,1.284965,-2.995443,2.817536,-9.457561,-8.998660,8.755779,7.649282,8.513933,7.013679,-3.305704,-0.969015,2.954545,-5.500086,4.991773,-5.547552,7.096296,4.824010,-0.575385,2.226400,2.244406,-6.811651,2.046391,-0.095553,-3.663270,-3.159129,4.391682,-7.599482,6.811544,-8.697568,-5.766530,8.453556,-5.494072,8.845942,4.917715,3.703715,-0.723045,-3.962720,3.133400,-8.430709,-3.647742,-4.411902,-1.872295,-5.040603,2.646095,-5.586730,5.649850,9.055390,-6.671531,3.473073,-2.134376,-0.221795,-2.444476,-3.948773,0.434450,0.969298,-6.755992,8.007140,-4.725753,-3.379003,-9.291364,-2.040940,-2.627829,6.448453,-2.055399,4.101858,-5.874889,-7.479944,-9.260905,-1.707418,7.491087,0.602546,-1.483329,-4.016066,-0.812438,-5.793691,1.896568,0.454760,6.337023,-2.507183,2.207343,-4.619034,5.044698,-7.998699,3.450920,-9.902318,4.148563,-1.122202,-2.241381,-0.251243,9.544106,-3.350141,2.141024,6.394525,-3.329366,1.024317,1.978328,8.824480,-4.894429,-7.080818,9.116072,-2.671635,-8.268507,-8.824812,-5.741637,1.903629,5.309890,-8.892991,3.593102,8.759070,-4.873220,4.670379,-2.697127,-0.746661,8.009725,2.272691,1.966463,7.720649,-7.812142,7.058913,-7.789486,4.047340,-7.923696,3.080078,1.489043,8.227320,0.224653,8.845698,-1.117215,-2.989736,-7.675096,-5.973685,4.151104,7.414344,0.297508,-4.545521,3.410679,8.488089,-2.048504,-5.432456,-0.819226,3.217200,-4.289512,3.993450,-9.929452,-2.754297,0.958890,8.422309,-5.780173,7.534206,6.923221,-6.183899,3.393439,-9.783021,-2.186743,1.297982,-1.772025,-4.904303,9.012786,6.714754,1.586803,-6.710562,-0.635504,7.110124,-8.960026,-9.832701,8.382641,-1.855527,8.118855,-1.757172,1.669205,-6.943072,-9.493782,0.249479,-6.839635,0.644177,-2.426463,9.616251,3.037966,-8.821272,0.551367,9.365545,2.862209,3.134458,-6.541486,-2.099425,5.949024,-2.102877,5.338225,9.519087,-5.495469,2.905200,-9.425291,-2.211927,4.746893,7.675467,8.523162,0.407029,-2.104440,2.470300,-4.820047,7.914966,-8.726240,8.176617,4.348996,-2.884349,-1.585655,-2.723304,-7.704848,-6.013866,2.539100,-4.680584,5.958132,5.398418,-9.979241,-9.095916,-9.548977,-7.657548,8.248557,-8.394497,-3.857859,5.354118,-9.247778,9.939355,-6.187122,5.980933,5.450208,-0.803342,7.181947,-2.974921,0.163848,0.288418,-3.371006,-0.954860,9.886628,-3.494864,8.823206,-5.657328,-1.504411,-2.503292,-6.198198], dtype = "float64")#candidate|6459|(384,)|const|float64
call_6458 = func_2404_call(relay.reshape(const_6459.astype('float64'), [4, 8, 12]))
call_6460 = func_2404_call(relay.reshape(const_6459.astype('float64'), [4, 8, 12]))
func_845_call = mod.get_global_var('func_845')
func_849_call = mutated_mod.get_global_var('func_849')
var_6464 = relay.var("var_6464", dtype = "int32", shape = (16,))#candidate|6464|(16,)|var|int32
var_6465 = relay.var("var_6465", dtype = "int32", shape = (160, 1))#candidate|6465|(160, 1)|var|int32
const_6466 = relay.const(-8, dtype = "int8")#candidate|6466|()|const|int8
call_6463 = relay.TupleGetItem(func_845_call(relay.reshape(var_6464.astype('int32'), [16,]), relay.reshape(var_6465.astype('int32'), [16, 10]), relay.reshape(const_6466.astype('int8'), []), ), 5)
call_6467 = relay.TupleGetItem(func_849_call(relay.reshape(var_6464.astype('int32'), [16,]), relay.reshape(var_6465.astype('int32'), [16, 10]), relay.reshape(const_6466.astype('int8'), []), ), 5)
bop_6471 = relay.bitwise_and(const_6459.astype('uint32'), var_6465.astype('uint32')) # shape=(160, 384)
uop_6478 = relay.sin(var_6465.astype('float64')) # shape=(160, 1)
func_6390_call = mod.get_global_var('func_6390')
func_6392_call = mutated_mod.get_global_var('func_6392')
call_6484 = relay.TupleGetItem(func_6390_call(relay.reshape(call_6456.astype('uint32'), [2, 8, 4])), 0)
call_6485 = relay.TupleGetItem(func_6392_call(relay.reshape(call_6456.astype('uint32'), [2, 8, 4])), 0)
bop_6488 = relay.bitwise_and(call_6463.astype('int8'), const_6466.astype('int8')) # shape=(100, 2)
bop_6491 = relay.bitwise_and(call_6467.astype('int8'), const_6466.astype('int8')) # shape=(100, 2)
output = relay.Tuple([call_6456,call_6458,var_6464,bop_6471,uop_6478,call_6484,bop_6488,])
output2 = relay.Tuple([call_6457,call_6460,var_6464,bop_6471,uop_6478,call_6485,bop_6491,])
func_6493 = relay.Function([var_6464,var_6465,], output)
mod['func_6493'] = func_6493
mod = relay.transform.InferType()(mod)
var_6494 = relay.var("var_6494", dtype = "int32", shape = (16,))#candidate|6494|(16,)|var|int32
var_6495 = relay.var("var_6495", dtype = "int32", shape = (160, 1))#candidate|6495|(160, 1)|var|int32
output = func_6493(var_6494,var_6495,)
func_6496 = relay.Function([var_6494,var_6495,], output)
mutated_mod['func_6496'] = func_6496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6165_call = mod.get_global_var('func_6165')
func_6166_call = mutated_mod.get_global_var('func_6166')
call_6520 = relay.TupleGetItem(func_6165_call(), 3)
call_6521 = relay.TupleGetItem(func_6166_call(), 3)
output = call_6520
output2 = call_6521
func_6526 = relay.Function([], output)
mod['func_6526'] = func_6526
mod = relay.transform.InferType()(mod)
output = func_6526()
func_6527 = relay.Function([], output)
mutated_mod['func_6527'] = func_6527
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6548 = relay.var("var_6548", dtype = "int64", shape = (14, 7, 14))#candidate|6548|(14, 7, 14)|var|int64
const_6549 = relay.const([[[-3,-1,-8,-10,4,-10,2,10,3,-7,8,-10,6,-5],[10,2,6,4,10,4,-9,-9,-10,-2,4,-2,5,-5],[-5,2,4,7,-9,6,8,-3,6,5,-2,-9,-8,1],[4,-8,8,4,-4,-4,5,-2,9,7,9,1,1,-10],[-2,4,-8,-5,-2,8,2,-1,-1,-10,-10,8,-1,3],[-1,-10,-5,-9,7,-9,4,7,1,-5,-10,-5,-3,10],[-3,5,5,5,2,-2,9,-7,1,9,1,4,-2,-10]],[[1,-1,2,-8,-1,-6,8,-1,-3,8,-4,6,4,5],[-1,10,-4,8,-7,2,1,3,7,-4,2,-4,2,2],[-4,-1,9,-10,-2,-8,7,9,9,7,5,8,-7,6],[4,5,-2,-4,-8,5,-3,1,4,-9,-3,10,-10,-5],[-1,-6,6,5,-6,10,-5,5,9,-9,-9,5,7,-8],[-4,-5,6,1,1,-2,9,4,-9,4,-7,3,3,8],[5,-8,10,5,-3,8,4,-4,3,7,-8,-2,-7,-3]],[[-2,2,-6,6,2,-2,8,2,1,5,5,-6,6,-8],[-2,3,1,-3,4,2,3,-2,3,4,-9,8,2,6],[3,-1,6,-8,7,-3,1,8,1,-4,3,10,7,-7],[3,9,9,8,-3,-2,10,-5,5,4,3,-10,-7,2],[8,7,5,5,7,9,2,4,1,2,1,9,7,2],[-2,10,-4,-1,-2,-2,2,10,-7,7,-2,-3,8,-8],[-5,-8,5,-7,4,9,-6,6,-4,-3,1,-10,-2,5]],[[-9,4,-5,9,2,-2,-3,4,-2,9,-7,9,-4,-10],[-6,-6,-9,-6,-5,-8,-2,3,9,-7,10,-9,8,-4],[10,1,-10,-8,-9,7,1,9,4,-3,9,-4,-5,5],[-2,8,-4,8,5,-7,10,6,-7,-7,7,6,9,5],[4,7,-9,-9,-3,-1,3,-3,-9,-6,-6,-1,-4,-8],[-6,9,3,7,-3,6,-3,6,-2,1,-10,2,-2,8],[10,9,9,8,-3,5,-5,-4,8,6,-9,-5,-4,6]],[[2,3,1,9,-9,-3,4,-10,1,-9,2,-10,2,1],[-6,3,-10,-9,-8,1,5,-2,4,-10,-6,3,-4,-2],[-2,-4,9,-4,4,1,2,-9,-8,8,5,-6,-4,-10],[3,5,-6,-2,6,5,1,-2,-10,10,4,-9,-3,-1],[-3,7,4,1,-3,-4,-1,1,-6,3,-5,-1,10,-9],[6,-1,-2,5,4,-5,-9,10,-9,1,3,9,-8,9],[4,-2,8,7,4,6,-8,-7,-10,-8,-7,4,5,-7]],[[8,1,-4,2,8,9,-3,-10,-6,9,-5,6,-8,-1],[6,5,4,7,1,-9,9,1,-5,-3,9,6,1,-5],[2,1,3,-3,-6,-6,-8,-5,5,8,-6,-8,7,10],[-5,8,-2,7,-6,4,-1,-8,7,9,-9,9,-10,-4],[-4,4,1,9,2,1,-8,-2,7,-1,3,-6,5,-10],[6,-1,-8,10,-10,5,6,-1,-2,3,-3,6,2,-10],[1,3,4,10,2,3,10,3,-5,8,7,9,-6,10]],[[8,7,2,9,-8,9,-10,2,-10,3,9,-3,3,-10],[6,8,-10,5,7,-5,4,6,6,-3,-5,4,-8,-2],[-8,1,-10,7,-4,-1,10,-7,-2,10,3,6,10,1],[8,10,-8,9,-9,-8,-1,-7,7,-5,9,6,-9,-7],[4,-8,3,-8,10,-9,-4,-4,-7,7,-5,10,-10,-5],[1,-1,-9,-9,8,3,3,-6,8,5,1,9,8,1],[8,-10,-7,5,-9,-10,2,-2,-3,3,10,-9,3,8]],[[-9,-1,6,-7,-2,1,-7,-6,-2,3,9,-1,7,10],[7,-1,-9,-5,-4,8,-5,7,7,2,-2,-7,4,-7],[-9,10,5,4,6,8,10,-7,-2,10,8,1,6,10],[-7,10,6,-1,3,-4,3,-10,8,1,-2,1,10,9],[-1,7,-9,-1,-6,5,-8,-8,-3,-5,6,2,6,7],[5,-3,8,-4,6,10,-8,9,8,-6,-6,1,-8,9],[8,1,5,-10,5,-9,-9,-10,6,4,9,-4,-2,6]],[[-9,3,4,-3,-9,3,8,2,-1,-6,-6,-2,10,-9],[-2,-4,9,-10,-3,-3,5,6,-5,3,-5,-6,9,3],[5,-4,6,-10,5,-9,3,3,-7,3,7,10,5,2],[-6,-5,-8,8,7,8,-9,4,-10,-2,-4,-9,-9,5],[-6,7,-2,3,-3,4,10,-6,3,-1,-7,-10,-7,3],[1,-1,-5,-9,5,10,4,8,8,-2,-3,3,-7,-10],[3,2,3,1,6,-8,-3,-8,2,8,1,-10,3,4]],[[-8,4,-2,-5,4,7,-7,10,3,4,4,-7,2,-7],[3,-6,-10,10,9,-8,-3,-2,10,-8,-7,-8,6,4],[-5,4,-6,6,-1,9,4,-4,2,5,9,3,-8,9],[-8,-2,5,8,-4,-1,-1,-8,8,1,-9,10,-4,4],[-5,5,-5,8,-3,-5,-1,6,7,-8,-6,-4,9,-3],[-6,4,1,7,-8,-7,-1,2,9,7,-1,-10,8,-4],[-8,10,7,7,5,3,1,8,4,-6,-7,-10,10,7]],[[-4,2,9,5,-8,-3,6,-8,-8,9,-4,7,-7,-10],[-5,-4,-8,-10,-10,3,5,1,-4,8,-5,5,3,-3],[-7,9,9,-2,2,6,-6,10,-6,7,-9,-3,-4,-6],[-10,-9,-3,10,4,1,-5,7,-7,-7,5,-7,10,1],[-8,-3,7,5,2,3,9,-3,-2,-8,-5,-4,-8,9],[10,-2,-6,-9,8,-2,-1,-6,9,-5,-10,-10,9,-7],[4,6,5,-4,-4,-5,-7,1,-2,-8,-8,9,-7,5]],[[4,2,-10,-2,6,-8,-9,1,8,5,2,-10,-6,10],[-10,9,9,-2,2,3,-1,8,-4,9,-4,-1,-8,1],[-9,-9,-6,-3,-4,3,10,-3,9,-3,2,-4,-4,7],[5,8,-6,5,7,-8,-2,4,1,2,-1,-2,5,-1],[10,-3,-3,10,-7,-3,10,5,4,-3,7,6,8,-2],[3,-4,-1,-7,7,6,-2,-8,2,-6,3,3,5,-9],[-7,-8,2,3,-8,-8,10,6,-2,-4,-8,-3,8,-10]],[[-5,-7,-9,1,4,7,-8,6,-8,10,7,-6,-2,7],[-5,4,7,10,-6,-7,9,-4,-10,3,-3,10,4,-6],[-5,10,-1,7,8,3,-10,-6,-6,-6,-1,6,1,-5],[-2,-3,5,6,-2,5,2,-5,8,-3,-4,-3,-7,10],[-5,-3,9,5,-3,-1,5,4,3,2,-9,-8,-6,-9],[-9,1,5,10,-1,-7,5,-9,5,8,1,9,-6,6],[-7,-5,3,10,-1,1,5,-8,7,9,-3,7,-8,5]],[[-3,-8,-5,9,-10,-3,9,-4,-1,5,2,-9,2,8],[-6,3,-3,2,-5,-3,1,-5,1,7,2,9,5,-6],[7,6,-8,-3,-2,-8,-7,10,-8,-8,-4,10,-8,-9],[-8,-1,-10,8,-6,8,5,4,8,10,1,-4,5,-3],[4,6,-1,-7,-4,1,-6,-1,-7,-3,-9,1,-2,-4],[-1,-10,1,7,4,2,-6,1,2,-3,5,3,10,3],[-9,7,-6,-4,-2,8,4,-6,-5,-4,-7,5,4,7]]], dtype = "int64")#candidate|6549|(14, 7, 14)|const|int64
bop_6550 = relay.minimum(var_6548.astype('int64'), relay.reshape(const_6549.astype('int64'), relay.shape_of(var_6548))) # shape=(14, 7, 14)
bop_6571 = relay.less(const_6549.astype('bool'), relay.reshape(bop_6550.astype('bool'), relay.shape_of(const_6549))) # shape=(14, 7, 14)
uop_6576 = relay.sqrt(bop_6550.astype('float32')) # shape=(14, 7, 14)
func_1462_call = mod.get_global_var('func_1462')
func_1465_call = mutated_mod.get_global_var('func_1465')
const_6579 = relay.const([1.039145,-8.172381,-2.976200,9.711226,-7.642582,9.446302,-6.437857,4.591007,2.874030,-4.188897,3.034070,3.748296,9.827977,-9.682384,-7.839357,7.500760,-2.929170,0.909736,-3.414597,-5.336877,-6.695215,5.352905,4.764950,-3.531108,7.929636,-8.823805,7.694445,-5.285353,-1.973120,9.733925,-9.334716,-4.109903,0.062916,0.987851,-3.624991,-0.982095,8.964226,7.068484,-5.310180,-2.458761,-8.182323,-2.335699,-6.519379,8.768921,9.718450,3.734503,2.729224,9.902769,7.212391,8.477224,-8.507503,8.262347,0.884218,1.355621,-8.645905,4.490186,-7.347506,4.971957,0.712081,0.680601,5.584511,-9.846412,-4.684783,7.262063,5.477903,8.614138,-4.745862,6.576825,9.698580,-0.632312,-3.439291,2.897108,0.389873,-6.400274,7.473840,-7.117232,-6.348402,7.825201,-0.163300,3.031898,5.577190,9.530438,6.505555,3.441085,3.141676,-1.545395,-3.289086,-0.270952,-1.828032,-9.276446,-3.835102,9.576036,3.918638,3.582176,5.385602,9.002598,0.352747,8.621770,-0.951180,-6.156001,-9.603942,8.112095,-1.397371,-1.977679,-1.272233,-8.599628,8.005140,-9.229974,-5.268038,-4.113414,-1.080619,1.486257,5.930931,-6.547253,8.298946,2.652268,5.612030,-1.065505,5.899391,6.221801,8.725294,-2.767801,8.380099,-9.401126,0.677123,0.158722,-0.222663,3.042480,6.183166,3.757037,-6.841511,-5.411237,-8.389729,4.812658,-1.094961,1.212297,-8.607927,-6.087697,-7.233706,-9.671933,-0.808337,2.177873,-1.570360,-5.398756,-5.327398,-7.219492,-6.209520,6.561459,-5.104577,-3.059202,4.219713,-7.495908,-6.257926,5.648891,8.118049,-1.067522,3.833586,0.296725,-7.255501,-4.392576,1.077911,-3.599525,7.951376,-6.649123,-9.466026,-5.069903,9.404242,-6.384174,-8.410667,-3.871751,4.110933,9.650369,1.797518,-6.315260,-6.737287,-1.412473,3.149710,3.025740,-4.758362,-3.813671,7.620148,-0.742147,-0.218426,-4.997665,-0.676505,-9.356336,4.047548,5.222651,-0.576019,-3.234815,-9.044063,7.439591,1.907044,-9.223544,-4.026800,6.169275,-5.154346,-0.737063,-5.466944,4.353884,-4.143995,-0.091561,4.705463,-1.374561,2.655713,-6.526589,9.855590,1.168528,-3.812514,3.323280,8.869559,-1.762385,-7.362457,-7.407378,2.506850,-4.062361,2.180644,3.832559,-1.676990,6.135116,5.112213,5.362071,7.430836,1.453025,-8.381138,-8.481785,2.754209,3.342594,-6.047254,-2.946742,7.133737,9.271974,7.922200,1.688899,-7.357181,4.251938,-0.578450,-1.155365,-9.591209,-9.528557,-7.822639,-8.946814,1.686811,-3.390617,7.702883,-7.954757,7.381687,5.323663,-1.403551,-8.758733,2.884536,-0.168031,-9.011749,7.118844,3.115726,4.405431,1.813071,6.129829,-6.485209,-8.955334,6.318375,-8.282780,-3.349430,6.540056,3.187312,2.740243,-0.816872,-5.634419,-0.266844,3.788335,2.692308,-3.857851,-4.983254,-8.203877,2.612912,-1.071505,4.069492,2.446001,-4.157284,-2.945153,-5.719141,9.148355,-8.161829,0.493426,7.539363,-9.390773,6.418813,6.639367,-9.847449,-5.124077,-1.003179,-7.878507,-2.349065,2.944900,1.198746,-0.729014,6.256420,-4.957321,4.789832,7.722744,-6.703602,-0.791648,-1.264522,2.265509,0.441829,-0.633483,-6.167793,1.092292,-9.763867,5.541093,-9.695639,1.465572,8.910431,4.449558,8.387742,-7.440431,-3.020756,8.878892,-2.322088,-7.519605,9.928915,-8.719043,9.649005,-1.050308,-1.838241,5.789562,0.700526,3.722445,-5.487089,8.265502,9.398727,8.412610,-4.838179,-6.963703,5.389143,-3.468850,5.714767,-2.361596,-2.709047,-7.852728,8.163476,-2.220886,-4.653180,4.118789,-9.856533,-2.781273,-9.342243,-5.751502,-9.390906,-8.457452,4.619985,-2.966704,2.577867,4.053440,8.893551,-9.603766,-5.113501,0.885774,-8.016422,9.352312], dtype = "float64")#candidate|6579|(360,)|const|float64
var_6580 = relay.var("var_6580", dtype = "uint32", shape = (64,))#candidate|6580|(64,)|var|uint32
call_6578 = relay.TupleGetItem(func_1462_call(relay.reshape(const_6579.astype('float64'), [6, 6, 10]), relay.reshape(var_6580.astype('uint32'), [8, 8]), ), 0)
call_6581 = relay.TupleGetItem(func_1465_call(relay.reshape(const_6579.astype('float64'), [6, 6, 10]), relay.reshape(var_6580.astype('uint32'), [8, 8]), ), 0)
output = relay.Tuple([bop_6571,uop_6576,call_6578,const_6579,var_6580,])
output2 = relay.Tuple([bop_6571,uop_6576,call_6581,const_6579,var_6580,])
func_6583 = relay.Function([var_6548,var_6580,], output)
mod['func_6583'] = func_6583
mod = relay.transform.InferType()(mod)
var_6584 = relay.var("var_6584", dtype = "int64", shape = (14, 7, 14))#candidate|6584|(14, 7, 14)|var|int64
var_6585 = relay.var("var_6585", dtype = "uint32", shape = (64,))#candidate|6585|(64,)|var|uint32
output = func_6583(var_6584,var_6585,)
func_6586 = relay.Function([var_6584,var_6585,], output)
mutated_mod['func_6586'] = func_6586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5630_call = mod.get_global_var('func_5630')
func_5631_call = mutated_mod.get_global_var('func_5631')
call_6683 = relay.TupleGetItem(func_5630_call(), 1)
call_6684 = relay.TupleGetItem(func_5631_call(), 1)
output = call_6683
output2 = call_6684
func_6697 = relay.Function([], output)
mod['func_6697'] = func_6697
mod = relay.transform.InferType()(mod)
output = func_6697()
func_6698 = relay.Function([], output)
mutated_mod['func_6698'] = func_6698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6068_call = mod.get_global_var('func_6068')
func_6070_call = mutated_mod.get_global_var('func_6070')
call_6786 = relay.TupleGetItem(func_6068_call(), 1)
call_6787 = relay.TupleGetItem(func_6070_call(), 1)
output = call_6786
output2 = call_6787
func_6793 = relay.Function([], output)
mod['func_6793'] = func_6793
mod = relay.transform.InferType()(mod)
output = func_6793()
func_6794 = relay.Function([], output)
mutated_mod['func_6794'] = func_6794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_6795 = func_718_call()
call_6796 = func_718_call()
output = relay.Tuple([call_6795,])
output2 = relay.Tuple([call_6796,])
func_6804 = relay.Function([], output)
mod['func_6804'] = func_6804
mod = relay.transform.InferType()(mod)
mutated_mod['func_6804'] = func_6804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6804_call = mutated_mod.get_global_var('func_6804')
call_6805 = func_6804_call()
output = call_6805
func_6806 = relay.Function([], output)
mutated_mod['func_6806'] = func_6806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_6834 = relay.TupleGetItem(func_1758_call(), 0)
call_6835 = relay.TupleGetItem(func_1760_call(), 0)
output = call_6834
output2 = call_6835
func_6851 = relay.Function([], output)
mod['func_6851'] = func_6851
mod = relay.transform.InferType()(mod)
mutated_mod['func_6851'] = func_6851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6851_call = mutated_mod.get_global_var('func_6851')
call_6852 = func_6851_call()
output = call_6852
func_6853 = relay.Function([], output)
mutated_mod['func_6853'] = func_6853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_6908 = func_2359_call()
call_6909 = func_2359_call()
output = relay.Tuple([call_6908,])
output2 = relay.Tuple([call_6909,])
func_6910 = relay.Function([], output)
mod['func_6910'] = func_6910
mod = relay.transform.InferType()(mod)
output = func_6910()
func_6911 = relay.Function([], output)
mutated_mod['func_6911'] = func_6911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_708_call = mod.get_global_var('func_708')
func_710_call = mutated_mod.get_global_var('func_710')
call_6920 = relay.TupleGetItem(func_708_call(), 0)
call_6921 = relay.TupleGetItem(func_710_call(), 0)
output = call_6920
output2 = call_6921
func_6925 = relay.Function([], output)
mod['func_6925'] = func_6925
mod = relay.transform.InferType()(mod)
output = func_6925()
func_6926 = relay.Function([], output)
mutated_mod['func_6926'] = func_6926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_7013 = relay.TupleGetItem(func_1758_call(), 1)
call_7014 = relay.TupleGetItem(func_1760_call(), 1)
func_4529_call = mod.get_global_var('func_4529')
func_4532_call = mutated_mod.get_global_var('func_4532')
var_7045 = relay.var("var_7045", dtype = "float64", shape = (9, 90))#candidate|7045|(9, 90)|var|float64
call_7044 = func_4529_call(relay.reshape(var_7045.astype('float64'), [15, 6, 9]))
call_7046 = func_4529_call(relay.reshape(var_7045.astype('float64'), [15, 6, 9]))
func_4722_call = mod.get_global_var('func_4722')
func_4723_call = mutated_mod.get_global_var('func_4723')
call_7052 = func_4722_call()
call_7053 = func_4722_call()
func_3724_call = mod.get_global_var('func_3724')
func_3728_call = mutated_mod.get_global_var('func_3728')
const_7055 = relay.const([-5,-1,-5,7,3,9,-2,-7,-9,-10,-8,5,1,-10,-6,9,6,-2,-2,2,-2,9,-4,-6,9,-8,-7,10,3,-10,-3,-2,8,-9,-2,6,-6,9,-1,-2,3,7,5,7,-9,6,-8,2,-2,-6,4,10,9,9,-4,-10,1,8,-7,3,-4,2,7,7,5,-6,5,8,-5,4,7,8,-3,5,3,-10,7,8,5,5,-7,8,9,8,2,3,7,-9,-10,-4,2,-2,5,-7,3,10,-5,6,4,-7,-7,8,-4,8,-1,8,6,6,-10,-4,5,7,-2,-3,8,-5,-10,10,-7,-9,1,-6,9,-10,3,4,-8,9,3,-6,-1,7,-1,-7,-5,1,-6,-1,-6,-4,5,-8,-10,-2], dtype = "uint64")#candidate|7055|(144,)|const|uint64
call_7054 = relay.TupleGetItem(func_3724_call(relay.reshape(const_7055.astype('uint64'), [8, 2, 9]), relay.reshape(const_7055.astype('uint64'), [8, 2, 9]), ), 1)
call_7056 = relay.TupleGetItem(func_3728_call(relay.reshape(const_7055.astype('uint64'), [8, 2, 9]), relay.reshape(const_7055.astype('uint64'), [8, 2, 9]), ), 1)
func_718_call = mod.get_global_var('func_718')
func_720_call = mutated_mod.get_global_var('func_720')
call_7059 = func_718_call()
call_7060 = func_718_call()
output = relay.Tuple([call_7013,call_7044,var_7045,call_7052,call_7054,const_7055,call_7059,])
output2 = relay.Tuple([call_7014,call_7046,var_7045,call_7053,call_7056,const_7055,call_7060,])
func_7066 = relay.Function([var_7045,], output)
mod['func_7066'] = func_7066
mod = relay.transform.InferType()(mod)
mutated_mod['func_7066'] = func_7066
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7067 = relay.var("var_7067", dtype = "float64", shape = (9, 90))#candidate|7067|(9, 90)|var|float64
func_7066_call = mutated_mod.get_global_var('func_7066')
call_7068 = func_7066_call(var_7067)
output = call_7068
func_7069 = relay.Function([var_7067], output)
mutated_mod['func_7069'] = func_7069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5385_call = mod.get_global_var('func_5385')
func_5387_call = mutated_mod.get_global_var('func_5387')
call_7126 = relay.TupleGetItem(func_5385_call(), 2)
call_7127 = relay.TupleGetItem(func_5387_call(), 2)
const_7129 = relay.const([[5.042068,7.781473,6.508868,4.855131,6.155659,0.234498,3.881527,-3.421997,-1.914945,0.730757],[0.605558,8.028218,-9.196759,-1.628969,-4.428992,1.433114,-4.137810,7.071449,6.947768,-4.061424],[-1.651551,7.046971,7.212772,1.963399,1.076942,-9.714477,-1.013102,3.043208,-8.534792,-4.330122],[-1.520132,1.280882,-4.836875,-8.920146,5.372841,0.838934,-0.198992,-5.683364,-6.408187,-5.373058],[-4.692832,-3.324608,-7.974234,2.703237,1.362248,0.544308,-5.039873,-4.436055,1.964914,-9.682386],[2.266726,-5.970866,3.793411,4.059395,8.906457,5.268815,3.387054,-2.295868,1.271455,-0.741346],[9.033820,-9.992241,-3.518879,-8.987024,4.522912,0.818546,-5.072027,6.709407,-1.385947,9.994971],[-9.902586,4.193380,-6.762060,3.514042,-7.890312,-2.067815,-7.274714,1.410313,4.559507,-8.252109],[-3.080068,6.486296,-0.435421,-6.926695,-4.076694,-8.359972,-2.465038,-7.197757,1.857230,0.390449],[9.720541,2.834445,-6.131366,2.503493,-7.670714,1.450756,8.519710,-3.229273,1.251176,-8.950467],[-3.711425,-4.463770,-9.091994,-5.497694,-5.486359,3.769238,8.150527,5.460490,2.030782,-7.568644],[9.888139,6.641489,-0.880331,-3.687537,-2.250886,3.905522,5.066539,-3.308269,-5.028966,1.364547],[-5.274087,9.829394,7.133099,0.061112,6.317358,-9.673160,4.036806,4.109406,7.717244,8.882962],[-2.324945,1.125661,-8.361366,4.776957,-5.760913,-1.582394,-5.133983,-7.370235,-2.370499,-9.218835],[0.752999,-4.770967,-4.288094,1.663325,7.173803,-7.302658,5.704275,7.294864,2.037003,2.890989],[1.291009,-4.400093,3.310813,8.198227,-5.422392,5.803385,2.756956,9.263680,3.539061,7.932753],[2.668340,-1.727371,9.962723,9.649234,-5.659118,-9.862068,-0.723657,6.761718,-7.656254,7.565037],[2.806861,-4.418146,9.543839,-4.265271,-7.578965,5.320545,4.492362,2.053489,-6.738856,1.539585],[5.704995,-7.442177,-1.497558,8.512976,3.593394,-8.159649,7.162493,7.208262,-8.628707,2.136781],[4.047351,-9.948726,-9.637423,-5.301779,-5.034711,8.584229,8.409031,3.676076,-7.567161,-8.458723],[-4.236427,-1.687093,-9.222395,-5.224777,4.009656,5.353329,-2.777088,-9.198508,7.880294,2.597830],[-7.560339,0.829648,5.164668,-8.421308,6.528511,3.807959,9.160937,8.221143,5.971498,-9.835825],[2.228850,2.654132,2.458830,-7.506729,-6.629299,3.268938,4.633842,7.238167,4.352104,-8.535719],[-6.565895,-2.864934,0.320978,3.440325,0.291964,6.909444,-2.518948,4.418619,-5.219351,-1.987075],[7.564482,-4.383541,6.774811,7.743942,9.309356,9.634550,8.880278,1.656652,-4.371214,2.483324],[-7.562201,-7.064700,-9.846709,-6.459596,-2.413029,0.116528,-7.718593,-6.053499,7.852316,2.263716],[2.285394,7.828451,-4.558073,1.460878,2.641997,8.956688,6.605011,-1.029092,3.066639,8.618938],[-7.117538,2.073571,-0.442704,-0.421696,-0.719333,-7.538775,-4.555916,-2.263029,-6.221287,5.394707],[8.390970,5.717187,6.595332,-2.304053,-0.606977,-3.876163,-8.170434,-9.108092,0.101619,8.263341],[-1.919104,9.310573,0.011537,5.752087,3.805853,2.629993,4.396949,7.798148,7.581109,4.405345],[5.982242,-2.501512,-7.763955,-9.202529,5.223864,4.398915,7.635342,-3.435741,-7.171735,-2.105304],[1.538901,-4.316401,-6.212832,0.050032,0.747511,-9.887887,-2.948504,5.710106,4.685518,-0.073644],[8.866018,-4.562777,-9.147554,6.779593,-3.600528,-9.639062,8.174915,3.341985,-2.173083,7.256513],[4.105284,4.726791,-0.367692,-4.208537,-4.589419,-0.643735,-1.165306,7.020744,-4.782828,-4.013006],[-8.645782,-5.381667,1.110629,-4.061230,-5.152735,-2.209728,0.917081,0.710864,-0.623819,3.185543],[-4.198980,-9.533746,-7.293648,1.119433,-1.190084,9.323389,-0.138301,-2.242788,8.524093,8.334260]], dtype = "float64")#candidate|7129|(36, 10)|const|float64
bop_7130 = relay.floor_mod(call_7126.astype('float64'), relay.reshape(const_7129.astype('float64'), relay.shape_of(call_7126))) # shape=(36, 10)
bop_7133 = relay.floor_mod(call_7127.astype('float64'), relay.reshape(const_7129.astype('float64'), relay.shape_of(call_7127))) # shape=(36, 10)
func_3177_call = mod.get_global_var('func_3177')
func_3179_call = mutated_mod.get_global_var('func_3179')
call_7134 = relay.TupleGetItem(func_3177_call(), 0)
call_7135 = relay.TupleGetItem(func_3179_call(), 0)
output = relay.Tuple([bop_7130,call_7134,])
output2 = relay.Tuple([bop_7133,call_7135,])
func_7140 = relay.Function([], output)
mod['func_7140'] = func_7140
mod = relay.transform.InferType()(mod)
output = func_7140()
func_7141 = relay.Function([], output)
mutated_mod['func_7141'] = func_7141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2651_call = mod.get_global_var('func_2651')
func_2653_call = mutated_mod.get_global_var('func_2653')
call_7144 = func_2651_call()
call_7145 = func_2651_call()
func_6119_call = mod.get_global_var('func_6119')
func_6122_call = mutated_mod.get_global_var('func_6122')
var_7155 = relay.var("var_7155", dtype = "int8", shape = ())#candidate|7155|()|var|int8
call_7154 = relay.TupleGetItem(func_6119_call(relay.reshape(var_7155.astype('int8'), [])), 0)
call_7156 = relay.TupleGetItem(func_6122_call(relay.reshape(var_7155.astype('int8'), [])), 0)
output = relay.Tuple([call_7144,call_7154,var_7155,])
output2 = relay.Tuple([call_7145,call_7156,var_7155,])
func_7171 = relay.Function([var_7155,], output)
mod['func_7171'] = func_7171
mod = relay.transform.InferType()(mod)
mutated_mod['func_7171'] = func_7171
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7172 = relay.var("var_7172", dtype = "int8", shape = ())#candidate|7172|()|var|int8
func_7171_call = mutated_mod.get_global_var('func_7171')
call_7173 = func_7171_call(var_7172)
output = call_7173
func_7174 = relay.Function([var_7172], output)
mutated_mod['func_7174'] = func_7174
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7186 = relay.var("var_7186", dtype = "uint16", shape = ())#candidate|7186|()|var|uint16
var_7187 = relay.var("var_7187", dtype = "uint16", shape = (1, 14))#candidate|7187|(1, 14)|var|uint16
bop_7188 = relay.left_shift(var_7186.astype('uint16'), var_7187.astype('uint16')) # shape=(1, 14)
output = bop_7188
output2 = bop_7188
func_7193 = relay.Function([var_7186,var_7187,], output)
mod['func_7193'] = func_7193
mod = relay.transform.InferType()(mod)
mutated_mod['func_7193'] = func_7193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7193_call = mutated_mod.get_global_var('func_7193')
var_7195 = relay.var("var_7195", dtype = "uint16", shape = ())#candidate|7195|()|var|uint16
var_7196 = relay.var("var_7196", dtype = "uint16", shape = (1, 14))#candidate|7196|(1, 14)|var|uint16
call_7194 = func_7193_call(var_7195,var_7196,)
output = call_7194
func_7197 = relay.Function([var_7195,var_7196,], output)
mutated_mod['func_7197'] = func_7197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4007_call = mod.get_global_var('func_4007')
func_4008_call = mutated_mod.get_global_var('func_4008')
call_7201 = func_4007_call()
call_7202 = func_4007_call()
func_6851_call = mod.get_global_var('func_6851')
func_6853_call = mutated_mod.get_global_var('func_6853')
call_7209 = func_6851_call()
call_7210 = func_6851_call()
func_2046_call = mod.get_global_var('func_2046')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_7215 = func_2046_call()
call_7216 = func_2046_call()
output = relay.Tuple([call_7201,call_7209,call_7215,])
output2 = relay.Tuple([call_7202,call_7210,call_7216,])
func_7217 = relay.Function([], output)
mod['func_7217'] = func_7217
mod = relay.transform.InferType()(mod)
output = func_7217()
func_7218 = relay.Function([], output)
mutated_mod['func_7218'] = func_7218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7217_call = mod.get_global_var('func_7217')
func_7218_call = mutated_mod.get_global_var('func_7218')
call_7245 = relay.TupleGetItem(func_7217_call(), 1)
call_7246 = relay.TupleGetItem(func_7218_call(), 1)
func_4606_call = mod.get_global_var('func_4606')
func_4609_call = mutated_mod.get_global_var('func_4609')
var_7319 = relay.var("var_7319", dtype = "float64", shape = (384,))#candidate|7319|(384,)|var|float64
call_7318 = relay.TupleGetItem(func_4606_call(relay.reshape(var_7319.astype('float64'), [384,])), 1)
call_7320 = relay.TupleGetItem(func_4609_call(relay.reshape(var_7319.astype('float64'), [384,])), 1)
func_5376_call = mod.get_global_var('func_5376')
func_5377_call = mutated_mod.get_global_var('func_5377')
call_7323 = relay.TupleGetItem(func_5376_call(), 2)
call_7324 = relay.TupleGetItem(func_5377_call(), 2)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_7325 = func_2359_call()
call_7326 = func_2359_call()
output = relay.Tuple([call_7245,call_7318,var_7319,call_7323,call_7325,])
output2 = relay.Tuple([call_7246,call_7320,var_7319,call_7324,call_7326,])
func_7327 = relay.Function([var_7319,], output)
mod['func_7327'] = func_7327
mod = relay.transform.InferType()(mod)
var_7328 = relay.var("var_7328", dtype = "float64", shape = (384,))#candidate|7328|(384,)|var|float64
output = func_7327(var_7328)
func_7329 = relay.Function([var_7328], output)
mutated_mod['func_7329'] = func_7329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3452_call = mod.get_global_var('func_3452')
func_3454_call = mutated_mod.get_global_var('func_3454')
call_7360 = relay.TupleGetItem(func_3452_call(), 0)
call_7361 = relay.TupleGetItem(func_3454_call(), 0)
output = call_7360
output2 = call_7361
func_7371 = relay.Function([], output)
mod['func_7371'] = func_7371
mod = relay.transform.InferType()(mod)
mutated_mod['func_7371'] = func_7371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7371_call = mutated_mod.get_global_var('func_7371')
call_7372 = func_7371_call()
output = call_7372
func_7373 = relay.Function([], output)
mutated_mod['func_7373'] = func_7373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2429_call = mod.get_global_var('func_2429')
func_2430_call = mutated_mod.get_global_var('func_2430')
call_7410 = relay.TupleGetItem(func_2429_call(), 0)
call_7411 = relay.TupleGetItem(func_2430_call(), 0)
func_901_call = mod.get_global_var('func_901')
func_903_call = mutated_mod.get_global_var('func_903')
call_7421 = relay.TupleGetItem(func_901_call(relay.reshape(call_7410.astype('uint32'), [2, 8, 4])), 0)
call_7422 = relay.TupleGetItem(func_903_call(relay.reshape(call_7410.astype('uint32'), [2, 8, 4])), 0)
output = relay.Tuple([call_7410,call_7421,])
output2 = relay.Tuple([call_7411,call_7422,])
func_7430 = relay.Function([], output)
mod['func_7430'] = func_7430
mod = relay.transform.InferType()(mod)
output = func_7430()
func_7431 = relay.Function([], output)
mutated_mod['func_7431'] = func_7431
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7474 = relay.const([[[1.466763,2.512489,8.588744,5.179519,-3.019008,-4.598950,2.289676,8.677293,-8.594693,-2.488430,1.377058,-5.740033],[7.252897,-3.151774,-9.762481,-0.712768,2.118735,-2.289452,6.328372,-4.019222,9.745335,-4.797139,-8.460108,-6.290031],[6.611028,-9.161441,-7.255859,6.890975,9.864394,1.268829,-2.254035,-5.491255,1.919878,-3.832305,-8.430151,-2.345997],[-1.089916,-2.177584,-4.179105,4.011218,2.147056,-4.776028,-4.259662,-6.036310,2.490056,6.939793,9.534214,-8.516643],[9.181537,4.324306,3.572996,1.883049,5.817497,-8.571381,6.584712,7.651665,-2.417436,-5.230888,-7.338677,-2.989180],[-9.560898,2.119511,0.395219,-4.124948,-3.349782,-3.455521,1.012241,1.214417,-0.540276,-9.593463,-1.712850,-3.684589],[7.676493,2.982580,3.681277,-5.309275,-7.441860,-0.163521,0.265701,-4.129023,-5.439000,6.739572,-4.190004,-7.982727],[0.701334,-6.370892,7.652955,-5.011575,9.821378,-6.978525,0.368647,-9.589882,-8.885876,-5.588551,3.547183,9.225889]],[[2.277066,5.658017,-0.500715,-6.553161,-8.447193,8.698327,-2.917089,2.163425,7.155331,-5.407729,-3.092218,-0.836246],[3.364744,-2.277418,5.050065,7.182313,-4.151366,5.816415,-9.953090,-6.366289,-9.585030,-8.232657,7.806951,0.131955],[2.701273,-5.841423,-8.969701,-9.831783,0.927623,6.897950,4.860477,7.907404,9.846601,-1.328706,5.522403,1.982261],[-3.140495,-2.041082,9.666532,-4.819114,5.709876,-7.690401,-6.933115,-4.417639,8.452961,-0.605656,-7.703606,-3.962628],[-0.857570,1.524096,-3.914053,-8.628276,7.586477,-0.929423,-9.658322,1.237880,7.732268,1.481109,9.433141,4.603866],[8.704071,5.188552,-1.512949,-3.694199,-7.345255,-6.322190,-8.660383,0.332813,7.605752,-7.360695,-8.716985,5.039264],[7.587565,8.770472,-8.565109,1.996050,4.220272,2.201637,-2.056122,-6.669405,-8.557734,4.520136,9.482292,-8.198874],[2.958633,-1.150935,-9.326267,7.978545,0.734372,-1.948832,-6.366904,9.929654,-1.932546,9.036619,-8.176515,5.542262]],[[-2.930289,0.496588,0.736331,-9.765467,-9.273867,9.635950,-8.125009,-7.346142,7.157951,-0.970798,-9.709246,5.153372],[-0.760381,-1.446214,0.033970,7.370088,-5.422587,7.436081,-1.295535,-6.150886,4.759063,-5.578694,8.958649,7.083382],[7.053360,-1.270618,1.445108,8.442050,-5.157725,3.637906,3.339961,7.687886,4.689407,-2.210680,-2.598368,5.963753],[-9.118945,8.734796,-6.828670,-0.467925,-4.188942,-6.505174,6.108491,-9.674985,7.059179,5.144435,-6.960334,-3.697765],[6.292908,-8.243276,-3.646280,4.128935,2.504688,-5.995367,7.632760,4.052469,0.372005,-4.134042,9.591970,-8.259916],[-4.340317,-3.885478,-3.982273,-9.110974,4.286988,2.135007,-6.467016,-5.213286,6.314919,-4.588921,9.592986,0.523258],[2.380608,9.301101,-5.675220,9.320198,3.673637,8.863464,-7.844346,-6.821608,-9.973448,4.922174,-6.838548,-3.503000],[-8.392276,8.764161,9.446932,-0.853625,-3.058792,9.157499,2.413049,5.330286,-1.369522,-7.029640,-8.734170,-5.570739]],[[-2.283486,-7.471030,1.473582,8.102196,5.176421,-2.203019,0.128992,6.825701,-5.659332,-6.075854,4.488332,5.633661],[-4.824662,-1.805611,-4.690252,-6.519115,4.959609,9.708704,0.326863,-5.880174,5.330074,1.789968,-6.156533,-8.521105],[-7.572114,-9.480386,-9.111694,8.911171,-7.200183,-6.692849,2.769637,0.133494,1.209050,2.433380,9.399051,7.544081],[-2.320550,0.790243,6.575447,-8.432659,-5.324209,7.148442,-1.335573,-8.074778,-8.264609,2.912908,9.669070,-1.490081],[5.222029,4.535871,-5.253132,-1.607275,-2.711260,1.862170,2.687717,2.988614,-7.082744,3.066582,9.416633,6.304627],[-6.163440,5.269157,-3.707369,-8.836627,-6.420545,-0.957353,-2.346262,0.684439,0.340168,-4.085588,-0.916446,-4.120197],[-9.168206,4.795909,3.009601,5.183476,3.998337,7.866574,5.240961,-6.462984,-5.450320,-2.845715,4.825717,8.694690],[-0.938517,6.908265,6.080781,3.973471,6.586386,8.848765,-6.587643,-5.994131,-0.387992,8.732526,9.819858,9.537386]],[[-5.233092,-8.119251,2.551696,-7.744086,0.130872,3.028260,-8.921091,-6.937791,9.462851,-8.157533,6.358605,-1.071888],[8.628098,1.197346,4.969824,-3.812741,-0.801136,9.197384,-8.030565,3.643900,6.214471,-9.465826,5.280464,-7.235575],[-4.296299,-8.462892,7.628134,5.521895,-9.441065,-0.622252,2.853746,-1.893907,0.702585,-2.064014,0.323817,-2.809560],[-6.017911,-1.615421,5.365809,-5.434636,-0.334599,6.774452,2.752979,-0.934432,7.920938,8.568648,0.088330,-6.580169],[0.868997,-4.994937,-1.084637,-5.598549,5.890309,1.907822,1.825576,-6.000299,-0.719549,2.547509,9.456632,-5.173706],[-5.577849,8.964941,8.538094,9.415828,-5.829319,6.962036,-2.320814,8.257204,9.695651,-0.425000,3.957483,-8.718081],[8.678014,0.730610,9.145340,8.194488,-0.871647,8.004987,0.340864,-2.958945,-9.364231,-9.448652,9.092739,-4.270354],[-1.225263,2.298999,1.784167,-9.038262,-3.743275,0.232833,6.777622,1.179110,-4.589071,0.613586,3.033086,6.724420]]], dtype = "float64")#candidate|7474|(5, 8, 12)|const|float64
uop_7475 = relay.rsqrt(const_7474.astype('float64')) # shape=(5, 8, 12)
output = relay.Tuple([uop_7475,])
output2 = relay.Tuple([uop_7475,])
func_7477 = relay.Function([], output)
mod['func_7477'] = func_7477
mod = relay.transform.InferType()(mod)
mutated_mod['func_7477'] = func_7477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7477_call = mutated_mod.get_global_var('func_7477')
call_7478 = func_7477_call()
output = call_7478
func_7479 = relay.Function([], output)
mutated_mod['func_7479'] = func_7479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3236_call = mutated_mod.get_global_var('func_3236')
call_7499 = relay.TupleGetItem(func_3234_call(), 1)
call_7500 = relay.TupleGetItem(func_3236_call(), 1)
uop_7503 = relay.acos(call_7499.astype('float64')) # shape=(200,)
uop_7505 = relay.acos(call_7500.astype('float64')) # shape=(200,)
func_4529_call = mod.get_global_var('func_4529')
func_4532_call = mutated_mod.get_global_var('func_4532')
const_7522 = relay.const([-6.320865,-9.552222,-1.271937,9.391996,7.300036,-9.676930,2.714978,-4.427539,-2.961061,4.400005,3.757497,-0.879265,2.686642,5.860699,-2.604646,-3.432780,9.201754,8.201433,-2.377832,-0.538366,7.316990,7.870519,-5.815130,-2.760870,-6.777132,-1.545974,9.309663,4.637962,-2.733013,2.757545,0.168422,6.359298,-8.411287,-5.094429,-8.458532,3.597401,8.804251,-1.652037,-5.474561,-2.529523,6.207774,6.198257,7.356646,8.028022,2.647479,4.845790,-3.153333,-4.009116,9.085243,5.315525,1.140895,-8.630391,1.020966,-5.232508,3.168801,-4.262342,9.120146,-5.349847,1.055779,-5.763984,-6.363494,2.532644,3.875437,-5.652349,-3.988970,-3.869209,-3.699332,-5.261957,3.795053,3.100388,1.860313,5.403632,9.475550,-7.617000,9.939109,-4.265542,-0.674095,-8.761326,9.669280,-7.121350,2.281749,6.012952,0.099291,2.243624,-3.707604,-1.814170,0.116453,9.684331,8.728329,4.544537,-9.496363,-2.693082,9.283454,-8.990404,7.574891,-6.676218,3.330660,-2.767616,0.708503,-4.259223,9.462100,7.443954,-1.032335,1.009648,-4.547658,0.296279,-8.417602,5.997640,-2.345093,-6.950387,5.901600,-5.322151,-6.304508,3.861112,0.396437,-5.815569,-2.164114,0.432018,-9.645247,-3.060140,1.789415,0.097575,-1.663834,6.640554,3.457201,-2.290607,-9.029017,6.406446,-0.424905,-0.278660,-5.987810,-3.473702,-9.645438,-7.186548,-0.106771,-7.432232,-3.326862,-6.098020,-4.155178,8.322000,6.142849,-0.439744,9.643528,0.316683,1.041965,2.565749,-8.610198,-5.557182,4.687348,3.123757,-4.050961,7.268160,1.543235,1.211743,1.828670,2.992682,-6.753295,-6.617023,-9.655846,4.833767,5.778612,6.195547,-6.061173,-6.240435,-1.875554,-0.243851,7.968592,7.040986,4.130230,4.492482,-3.759085,0.468508,-7.220365,-3.443125,2.928968,-7.293285,-6.892345,-1.865343,-8.911195,-2.669570,-2.137374,2.538891,-2.974175,9.533624,2.142921,-1.816556,7.647026,-8.234548,0.892272,-9.723132,9.214872,3.990537,6.420752,-1.204852,-6.274445,-8.847805,4.973081,7.243985,7.607430,0.636723,1.901729,-6.592673,-5.681069,-1.127874,3.700839,-6.219575,-3.276820,-8.055306,-1.632143,3.442166,3.967382,0.835625,5.850766,-6.275362,0.740327,6.960351,6.826491,-7.201245,-9.487847,8.953013,5.724768,-2.014995,2.023774,7.723039,-8.558576,-9.708637,2.567320,-1.501690,-1.864438,3.251600,4.773154,-6.085505,-5.016782,-3.756926,-0.170028,-4.827565,8.455753,0.741364,2.074832,-7.462020,0.027803,9.735783,4.976917,7.299954,-7.204348,7.794335,2.693895,-2.241641,-3.707426,-9.122803,-9.983401,3.119688,-4.883339,-8.689092,3.114686,8.342603,8.459418,9.717921,-3.661821,1.677767,8.740100,-7.611240,-1.010285,-4.341055,7.344753,6.429621,9.299100,-7.555351,8.999017,9.562479,5.526999,3.906855,6.209890,8.607202,8.592051,-4.564609,-8.933104,2.689062,0.919413,9.357236,1.061773,-2.374887,8.033760,-3.355642,1.695018,-7.398554,-3.309629,-9.417234,-6.101772,8.861339,-3.403285,8.086181,5.892026,6.282060,-7.014415,7.466883,-2.187592,1.603942,-2.808262,-2.481668,2.094886,3.312729,3.035494,-0.961785,4.108797,8.097054,7.509010,-9.776519,-5.396594,-0.624222,3.372153,-1.177974,5.705653,2.811444,8.781757,-6.191140,-4.564273,-0.117257,4.693818,-3.985727,-3.687283,-6.439317,-9.748567,-0.773267,-4.146049,2.161784,3.414326,1.200679,0.641007,-9.732862,6.623431,-3.725834,-3.917020,3.456028,0.717745,9.009108,2.571142,5.936669,-6.224122,-9.731800,-1.844401,-5.001096,8.982181,1.581275,7.025660,2.602479,-6.367351,-4.083006,-7.600939,-4.879280,0.413725,-7.083549,9.333223,-7.166567,6.550230,-4.840195,1.103493,5.628541,1.797336,9.794433,9.515187,3.593584,-2.485052,-4.850825,3.313171,-0.067345,-3.623288,0.485559,3.691753,-3.511640,9.403849,-9.760938,5.554008,0.285932,-7.048278,2.880396,-9.031583,6.446975,1.658914,9.259676,-6.529826,5.304396,-9.773095,-4.345978,7.429729,1.217285,-1.570453,4.306940,5.604147,-3.330794,3.446431,8.345826,-7.269221,5.094737,6.729883,-3.952138,-3.698312,-7.225238,-7.003914,-1.020275,1.233247,-7.133188,-5.111657,-8.369893,7.827881,9.788577,-5.191477,-5.959690,-4.164185,-0.907642,-2.085591,0.852360,5.247790,-2.330874,3.292464,2.084385,-7.403389,-0.846318,6.801308,-8.291525,5.134415,5.235499,3.464584,-4.999209,0.670573,6.969839,4.335365,6.722486,-1.697641,-4.820469,-6.421520,7.799375,-5.337634,6.340824,-0.097870,-3.290685,-4.994419,8.507554,5.533613,0.313795,7.661985,-4.208321,7.235212,0.295183,7.253306,7.732070,2.809314,-8.886407,-5.294805,3.184196,-0.227420,-2.118696,4.766011,-1.973208,3.875622,-7.485655,-3.655494,6.564728,-2.316415,8.772749,1.208977,6.830306,9.277590,-7.951755,-5.171618,-3.965347,9.595051,7.991952,3.346318,9.694236,6.591852,4.686902,-0.061276,3.635608,0.320504,3.345810,-1.760577,2.721148,-2.873470,2.940303,2.763721,9.384590,2.831536,9.989584,-1.929959,8.805038,-8.081897,7.178188,-8.780653,9.665223,-0.337256,-2.735340,-5.739059,-8.431569,6.961404,1.355195,-1.835258,3.821387,1.085541,-5.008517,1.999173,1.610371,-2.929647,-5.285871,2.496838,-3.843621,-1.947123,-7.520384,-8.564398,-8.512153,2.502919,-4.121523,-3.834433,5.700263,-4.688967,-1.135707,1.621519,-5.716742,-7.568396,-0.561228,-5.496106,6.793294,4.382259,6.433514,5.979831,2.985073,6.394730,-7.052151,0.793952,6.401056,5.637647,2.117881,2.630914,-1.833894,3.929191,-3.215748,5.997320,-3.107625,4.082791,-8.830495,1.221272,9.698478,9.106535,4.602883,3.411560,-9.250861,-9.568520,-7.138604,0.036922,9.624652,4.786362,0.328290,-4.731610,-4.826542,7.191837,-4.085581,-0.083217,-7.428125,6.129798,5.963888,-8.678356,7.853804,7.074370,5.292205,-3.500876,2.220901,-9.482568,-6.106363,0.544783,-1.384431,0.317021,0.757120,5.132822,6.450096,2.435246,6.514683,-5.613171,-9.570524,-5.974362,5.887274,2.698344,5.164895,6.523861,-1.469900,-4.245412,1.761860,1.431917,9.690446,-9.281464,6.580627,5.710038,-8.675657,0.984264,-5.918517,-1.604049,-0.375261,-9.829247,0.929245,9.731657,-3.434393,-9.112765,8.206731,5.180234,-0.873137,4.210417,8.004034,3.255587,-6.042551,5.196809,-3.862672,-7.544861,0.181392,-1.229798,-2.891359,-6.683757,1.857038,0.411407,-1.842898,-8.142952,-6.970825,-5.056876,-0.481932,1.587108,-9.088941,4.534548,-9.433382,7.329208,9.509468,-1.941302,9.876818,-0.401841,-3.092184,5.965837,-1.940856,1.262056,9.956900,2.785153,7.747445,-3.038715,9.078338,7.840985,-6.504879,5.949664,-1.622520,8.502351,-1.228612,6.790087,6.424711,1.221564,-5.508348,1.920232,-7.089765,0.509784,4.698878,1.191647,-5.245214,3.614870,5.584060,-5.114913,-7.552991,3.540852,2.739883,4.215287,6.224989,5.487766,-6.921250,6.991532,5.035119,-7.476561,-9.736922,8.638700,-2.712235,5.247466,4.240110,-1.580171,-7.727945,-9.068801,-4.243321,-5.172470,-4.115637,7.267553,-7.108427,4.409992,2.930219,4.966838,8.052077,-7.886517,5.755904,4.870562,1.380208,-6.034717,0.580787,-2.285798,0.950186,1.016717,-9.595120,-2.044879,3.402511,-4.791717,1.121146,-7.160426,-3.368721,4.835264,1.532505,-3.538332,-1.749737,-2.045962,2.095754,5.470152,4.101527,-7.105534,6.692419,9.857252,-6.749676,7.006851,8.592004,-6.190009,4.922920,4.602516,-6.973369,3.033519,-7.210786,-1.850072,-3.798811,-3.752089,-2.940596,4.420447,1.533613,-7.012644,-6.100978,-7.870496,6.559240,8.684749,-9.728104,7.972487,-8.904647,8.296590,-0.472528,-7.771009,0.097010,7.462029,3.584458,9.078602,6.122334,-3.621867,5.813488,1.189716,4.963784,5.743338,8.262893,-9.980382,-7.110706,-6.077791,6.485497,4.606041,-8.712150,-9.788240,-3.881680,-8.210709,6.617965,4.689502,1.926255,-1.519032,-0.581900,-9.757360,-8.180077,5.571076,-2.988636,-9.954571,0.624447,-1.681360,-8.305428,6.682154,-6.878451,-7.937259,0.321345,5.621467,-7.019904,4.073894,4.573276,-4.833100,1.442694,-8.081172,6.807382,6.830574,2.052631,-1.486925,9.900003,-4.465755,-6.712359,5.935635,-0.777138,-0.368670,-4.001835,8.698995,-5.268025,-5.651644,-3.477446,7.952493,3.584215,-9.322130,5.940418,-7.633897,-1.104333,-2.450078,0.191906,-5.829347,-7.823594,-5.393291,5.818319], dtype = "float64")#candidate|7522|(810,)|const|float64
call_7521 = func_4529_call(relay.reshape(const_7522.astype('float64'), [15, 6, 9]))
call_7523 = func_4529_call(relay.reshape(const_7522.astype('float64'), [15, 6, 9]))
func_4007_call = mod.get_global_var('func_4007')
func_4008_call = mutated_mod.get_global_var('func_4008')
call_7525 = func_4007_call()
call_7526 = func_4007_call()
uop_7535 = relay.rsqrt(const_7522.astype('float64')) # shape=(810,)
func_3108_call = mod.get_global_var('func_3108')
func_3110_call = mutated_mod.get_global_var('func_3110')
var_7538 = relay.var("var_7538", dtype = "int32", shape = (160,))#candidate|7538|(160,)|var|int32
call_7537 = relay.TupleGetItem(func_3108_call(relay.reshape(var_7538.astype('int32'), [160,])), 5)
call_7539 = relay.TupleGetItem(func_3110_call(relay.reshape(var_7538.astype('int32'), [160,])), 5)
output = relay.Tuple([uop_7503,call_7521,call_7525,uop_7535,call_7537,var_7538,])
output2 = relay.Tuple([uop_7505,call_7523,call_7526,uop_7535,call_7539,var_7538,])
func_7543 = relay.Function([var_7538,], output)
mod['func_7543'] = func_7543
mod = relay.transform.InferType()(mod)
var_7544 = relay.var("var_7544", dtype = "int32", shape = (160,))#candidate|7544|(160,)|var|int32
output = func_7543(var_7544)
func_7545 = relay.Function([var_7544], output)
mutated_mod['func_7545'] = func_7545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5238_call = mod.get_global_var('func_5238')
func_5239_call = mutated_mod.get_global_var('func_5239')
call_7550 = relay.TupleGetItem(func_5238_call(), 1)
call_7551 = relay.TupleGetItem(func_5239_call(), 1)
func_7327_call = mod.get_global_var('func_7327')
func_7329_call = mutated_mod.get_global_var('func_7329')
const_7559 = relay.const([[1.194261,-7.657975,-9.195333,-8.731416,2.156421,-6.733956,5.491436,9.916191,-3.469215,0.244380,-9.229605,8.471334,-7.561821,-1.881409,9.084049,-0.039337],[2.453437,5.667979,-1.071757,-7.375895,-7.274087,3.452620,1.274395,-8.621186,-9.278716,-5.976239,4.016927,1.387889,-1.244402,-6.485932,-3.856047,4.978077],[8.190819,6.279616,-0.978331,2.207347,4.787171,7.677935,-1.924988,-6.947101,8.457236,1.227243,-2.965159,6.645446,8.591965,3.837273,-4.169011,9.146410],[1.826904,6.431367,-4.029495,-3.404859,5.618631,4.132434,3.096454,-0.326137,-4.794081,4.809833,0.345351,7.331075,-7.782054,-2.890397,4.272105,-4.900694],[3.774977,2.142820,-4.289450,2.748103,6.608501,9.353394,-3.304895,5.083418,-7.708989,-7.266534,2.214589,-6.194556,-5.866677,-0.191323,-4.153480,-5.256804],[5.904406,3.488885,0.008932,1.705771,2.013521,6.351865,3.522464,-6.075676,3.039501,3.920498,6.889160,-1.449807,-4.524660,9.708069,5.924615,-1.925853],[3.155642,-1.778211,-5.489107,9.006902,6.859613,-5.361470,-3.115452,-4.890110,1.689977,-9.115818,2.339588,-8.856743,-9.600425,-3.120850,9.966319,-4.577633],[-3.884263,1.535933,-3.087930,2.823139,7.760813,-5.734744,-4.380942,7.744683,-6.294531,-2.636171,-0.194793,-5.794784,5.191142,-0.216536,9.527168,2.054926],[0.648914,2.536296,-2.791876,9.385505,-5.789243,1.288214,-7.049181,-4.943133,-6.000724,-4.894991,6.742327,1.140214,7.267130,5.713587,-2.810822,2.940088],[1.006547,-6.198076,9.315819,5.814289,2.623637,-5.135577,2.080064,2.247378,-6.325180,-4.726022,-9.881719,-4.163526,0.415833,-9.187072,-2.511469,8.622496],[-1.376380,2.660251,-0.530294,8.198969,4.566790,4.955045,-1.835513,4.042642,4.994326,-6.954288,6.099082,1.153308,-6.449463,8.774150,8.246386,-6.657626],[-1.950344,9.017050,-3.205823,-7.367007,6.725877,-0.895435,-3.599872,-4.193194,7.985738,3.810502,8.182659,3.583729,8.490778,-7.092813,-1.686520,-6.626120],[4.135507,6.340082,9.273913,5.878204,4.188258,-2.103691,5.439340,8.103624,-7.827663,-8.466302,-4.553196,9.524482,-0.426683,-7.405250,5.287893,3.164858],[1.647089,-9.857305,-1.497231,3.158778,-9.195554,-4.285005,-4.053620,-9.449186,-7.683564,-8.759841,9.395009,-5.795782,8.393801,-7.467241,-1.921787,3.806822],[-6.168917,-8.968644,-2.748428,-9.918401,4.358629,-4.510097,1.777934,-1.876411,5.352543,-6.553573,2.714247,-1.039896,3.264193,3.323562,-8.056210,0.982680],[-7.175378,-0.823376,2.561908,6.921284,6.515928,-1.748951,2.491623,-2.518583,1.537673,3.385963,-9.304781,-5.481205,-9.771127,3.713892,-3.542896,1.156991],[-3.402578,8.090109,-9.076294,-0.207216,3.341730,-5.407907,-7.574169,7.250652,5.989562,-5.952315,4.906925,-3.268695,-3.555985,-8.190454,-8.115561,3.766282],[7.077088,6.130281,-1.907554,2.563605,-0.670967,-0.891746,4.622021,7.603372,-4.258338,-3.360539,-7.589429,4.930848,-3.199922,6.081034,0.069890,3.543079],[-4.517969,-6.843386,-5.076667,-1.536303,-4.194203,8.544737,-6.405957,-0.567862,-3.875847,-1.585086,8.508289,7.277320,-8.119176,0.003756,-2.315273,-5.243619],[5.750384,0.546192,3.904425,-4.725684,-6.274787,5.613918,-6.003704,7.905140,-7.805970,0.219242,9.223258,6.816327,-0.077416,1.386755,1.754697,5.883676],[-1.932750,-0.212468,-5.560832,3.791660,5.650200,3.591335,6.324570,-8.033415,7.433593,3.827001,9.701972,-9.448421,1.675758,-1.387172,7.897747,8.407527],[-4.434844,5.611772,1.619017,8.381031,0.655684,-9.605499,5.340248,-4.843139,3.438634,9.906667,-1.162742,-5.706179,5.958050,-8.105476,-6.460177,-2.253440],[-2.094496,9.353710,1.890825,-6.393071,3.778993,1.526089,0.551116,1.894393,8.960964,6.039641,-9.393212,-3.962180,-0.941732,7.543956,-8.468793,7.478494],[7.392431,-9.536195,3.548600,-4.659857,-5.725566,1.237127,3.202775,-3.818033,6.851288,0.596258,1.881919,4.815823,-2.773051,-4.178641,3.848289,7.540306]], dtype = "float64")#candidate|7559|(24, 16)|const|float64
call_7558 = relay.TupleGetItem(func_7327_call(relay.reshape(const_7559.astype('float64'), [384,])), 3)
call_7560 = relay.TupleGetItem(func_7329_call(relay.reshape(const_7559.astype('float64'), [384,])), 3)
func_6010_call = mod.get_global_var('func_6010')
func_6013_call = mutated_mod.get_global_var('func_6013')
var_7570 = relay.var("var_7570", dtype = "float32", shape = (378,))#candidate|7570|(378,)|var|float32
call_7569 = relay.TupleGetItem(func_6010_call(relay.reshape(var_7570.astype('float32'), [9, 7, 6])), 0)
call_7571 = relay.TupleGetItem(func_6013_call(relay.reshape(var_7570.astype('float32'), [9, 7, 6])), 0)
func_1266_call = mod.get_global_var('func_1266')
func_1267_call = mutated_mod.get_global_var('func_1267')
call_7602 = relay.TupleGetItem(func_1266_call(), 0)
call_7603 = relay.TupleGetItem(func_1267_call(), 0)
const_7605 = relay.const([[-9.848274,7.981541,-1.266866,-4.549692,3.087550,6.551484,5.617992,0.400864,-2.728415,-5.896983,-4.269457,5.199902,1.013672,4.332420,5.926093,-9.263326],[9.728299,-4.439147,7.901052,2.643321,-7.703543,2.180423,2.914468,1.404967,5.625955,-9.919075,6.294332,2.499828,7.453974,-6.309613,-9.113652,6.256764],[-8.964818,7.431044,-3.163282,8.614957,-4.017957,-6.194257,6.584900,9.184685,-4.766291,-2.135677,1.221968,-9.392442,1.139245,3.750421,1.914873,0.687566],[-2.093131,3.583411,9.655549,0.500875,7.230461,5.747693,-9.110014,7.217153,0.484874,-9.307288,-3.170525,6.634442,9.593101,8.356542,1.612773,-3.412160],[5.820872,8.258282,-1.448680,-8.470514,-1.071204,-3.552395,2.849601,1.239809,-4.684994,1.558886,1.791005,-2.720224,-8.081597,4.910583,-7.520747,5.708067],[-1.532265,8.486985,-4.563238,-1.933195,4.461290,0.810313,1.483641,2.907856,-8.275776,-6.729012,-8.388019,-3.422442,-3.624024,-4.132169,5.452651,-6.090845],[-2.461373,1.194072,-4.925941,-8.071210,-5.441780,-0.361917,-7.980661,1.768942,-0.778347,-8.132881,-4.727926,2.277216,2.412635,-6.601399,-6.261054,-0.794961],[-6.948192,4.434846,4.637771,-0.181455,3.401437,7.770223,5.339834,-0.338314,-8.387028,-2.042889,0.475690,0.136227,5.184808,3.539363,7.999732,0.136223],[4.425491,-0.694305,-6.171711,9.068685,2.263454,1.512450,9.273305,-4.057747,0.681711,6.978387,3.726212,1.418407,-2.741943,-3.772560,-1.137153,1.430748],[-3.659182,-5.417855,-1.799067,-2.016803,5.372760,-2.848377,9.526682,-7.150804,9.868375,3.379087,8.154076,-6.226724,8.046502,5.269674,-1.575159,-7.705715],[-7.303229,9.769596,-7.865953,-3.352572,4.148425,-2.145519,0.732432,6.533647,-2.911618,9.609850,9.169997,3.722005,-2.436797,-6.866256,5.131548,0.990004],[-8.365570,2.296901,-0.675269,-1.252667,-2.976081,-7.980058,9.261713,7.110734,-8.547804,3.683001,-8.845625,3.419191,7.107398,6.825825,-5.723105,-4.339711],[0.532519,9.072319,6.366759,7.501524,-4.250535,-2.592756,-6.410655,-8.375138,-9.137640,-0.932690,-5.107876,-5.392369,-8.947406,9.136807,-5.382055,0.169337],[0.727934,-9.036784,-2.211460,-5.698013,2.572232,-6.118428,-6.667075,0.442304,6.752243,6.199555,7.130775,0.720726,0.839252,-5.642746,9.024289,2.541477],[-9.191680,5.699234,-7.614792,1.056083,-5.292023,6.223097,-4.020276,-6.545568,-1.896305,-5.046974,8.539033,3.502446,-7.597633,-8.582407,7.702517,-8.342580],[2.458849,-8.292649,0.524975,-0.134293,-6.894811,7.855585,-9.110066,-5.468205,0.848714,-1.740416,-2.359981,-6.526673,1.138192,-6.879231,-1.118889,-8.188619],[8.004131,4.824071,-7.282431,-2.631726,3.609157,-1.130102,1.959270,5.110182,5.361752,5.752241,4.632394,-9.942174,8.088946,-1.214364,4.622673,7.857634],[7.827362,3.424817,-4.804642,-1.826370,1.124365,8.267253,2.334560,-4.723845,-5.770808,3.716531,4.303394,-2.394135,-7.090521,-9.265620,2.381090,-1.521527],[9.639227,3.287843,-6.012258,8.066573,-9.584995,-2.440371,7.980549,-7.449817,1.468921,-6.293532,0.579882,6.060970,6.924171,3.779228,3.575900,1.803809],[0.794193,4.247963,9.168232,-8.355515,2.961726,8.849602,4.506400,6.035854,5.739821,2.304149,-3.550357,4.591003,-0.221275,7.485159,-5.928703,-1.649148],[0.777202,5.906685,8.682963,-7.472058,9.782721,5.912586,1.511973,2.363422,-9.705117,6.064063,4.678340,-0.737858,8.490460,5.421289,3.180094,1.888823],[4.916153,1.554767,-6.568634,-3.161068,7.810827,-2.278112,-8.531029,-2.401975,-6.510652,1.579363,-0.761027,-9.285091,3.009233,4.446103,6.884087,5.725388],[-1.691677,1.538176,-6.141312,-7.168713,-4.403163,-1.532901,-3.117751,4.622135,-4.230907,-0.851650,8.211655,-4.774480,-7.274315,1.837560,2.893563,8.128129],[2.297956,-0.701837,-0.158961,1.436752,-3.066156,2.588452,-5.739088,9.623715,4.531787,0.432312,-3.369379,-3.294630,-5.380026,1.639236,-2.045602,9.607603]], dtype = "float64")#candidate|7605|(24, 16)|const|float64
bop_7606 = relay.greater_equal(const_7559.astype('bool'), relay.reshape(const_7605.astype('bool'), relay.shape_of(const_7559))) # shape=(24, 16)
uop_7614 = relay.erf(bop_7606.astype('float32')) # shape=(24, 16)
uop_7632 = relay.cosh(const_7559.astype('float64')) # shape=(24, 16)
bop_7634 = relay.right_shift(uop_7632.astype('uint32'), relay.reshape(uop_7614.astype('uint32'), relay.shape_of(uop_7632))) # shape=(24, 16)
func_4684_call = mod.get_global_var('func_4684')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_7647 = relay.TupleGetItem(func_4684_call(), 0)
call_7648 = relay.TupleGetItem(func_4685_call(), 0)
func_1386_call = mod.get_global_var('func_1386')
func_1388_call = mutated_mod.get_global_var('func_1388')
call_7651 = func_1386_call()
call_7652 = func_1386_call()
bop_7658 = relay.not_equal(uop_7632.astype('bool'), relay.reshape(bop_7634.astype('bool'), relay.shape_of(uop_7632))) # shape=(24, 16)
output = relay.Tuple([call_7550,call_7558,call_7569,var_7570,call_7602,call_7647,call_7651,bop_7658,])
output2 = relay.Tuple([call_7551,call_7560,call_7571,var_7570,call_7603,call_7648,call_7652,bop_7658,])
func_7662 = relay.Function([var_7570,], output)
mod['func_7662'] = func_7662
mod = relay.transform.InferType()(mod)
var_7663 = relay.var("var_7663", dtype = "float32", shape = (378,))#candidate|7663|(378,)|var|float32
output = func_7662(var_7663)
func_7664 = relay.Function([var_7663], output)
mutated_mod['func_7664'] = func_7664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6910_call = mod.get_global_var('func_6910')
func_6911_call = mutated_mod.get_global_var('func_6911')
call_7690 = relay.TupleGetItem(func_6910_call(), 0)
call_7691 = relay.TupleGetItem(func_6911_call(), 0)
output = relay.Tuple([call_7690,])
output2 = relay.Tuple([call_7691,])
func_7703 = relay.Function([], output)
mod['func_7703'] = func_7703
mod = relay.transform.InferType()(mod)
mutated_mod['func_7703'] = func_7703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7703_call = mutated_mod.get_global_var('func_7703')
call_7704 = func_7703_call()
output = call_7704
func_7705 = relay.Function([], output)
mutated_mod['func_7705'] = func_7705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4379_call = mod.get_global_var('func_4379')
func_4381_call = mutated_mod.get_global_var('func_4381')
call_7778 = relay.TupleGetItem(func_4379_call(), 1)
call_7779 = relay.TupleGetItem(func_4381_call(), 1)
func_4116_call = mod.get_global_var('func_4116')
func_4118_call = mutated_mod.get_global_var('func_4118')
call_7782 = func_4116_call()
call_7783 = func_4116_call()
func_4137_call = mod.get_global_var('func_4137')
func_4139_call = mutated_mod.get_global_var('func_4139')
call_7784 = relay.TupleGetItem(func_4137_call(), 1)
call_7785 = relay.TupleGetItem(func_4139_call(), 1)
func_6804_call = mod.get_global_var('func_6804')
func_6806_call = mutated_mod.get_global_var('func_6806')
call_7788 = relay.TupleGetItem(func_6804_call(), 0)
call_7789 = relay.TupleGetItem(func_6806_call(), 0)
func_4236_call = mod.get_global_var('func_4236')
func_4241_call = mutated_mod.get_global_var('func_4241')
const_7804 = relay.const(-8.233062, dtype = "float64")#candidate|7804|()|const|float64
var_7805 = relay.var("var_7805", dtype = "float64", shape = (2,))#candidate|7805|(2,)|var|float64
var_7806 = relay.var("var_7806", dtype = "uint16", shape = (448,))#candidate|7806|(448,)|var|uint16
call_7803 = relay.TupleGetItem(func_4236_call(relay.reshape(const_7804.astype('float64'), []), relay.reshape(var_7805.astype('float64'), [2, 1]), relay.reshape(var_7806.astype('uint16'), [448,]), ), 4)
call_7807 = relay.TupleGetItem(func_4241_call(relay.reshape(const_7804.astype('float64'), []), relay.reshape(var_7805.astype('float64'), [2, 1]), relay.reshape(var_7806.astype('uint16'), [448,]), ), 4)
const_7808 = relay.const([[[-4.222176,-5.266425,1.729188,-4.753781,-4.358928,0.276954]],[[1.900622,3.781953,-5.269598,1.166754,-4.948912,1.230156]],[[-4.330234,5.467868,7.094348,-8.671223,-4.044174,-0.425959]],[[-9.001836,3.858827,5.194228,-0.848093,3.667507,-9.440990]],[[-5.723962,-5.811668,4.479297,-4.780239,-6.043114,-6.944441]]], dtype = "float64")#candidate|7808|(5, 1, 6)|const|float64
bop_7809 = relay.not_equal(const_7804.astype('bool'), const_7808.astype('bool')) # shape=(5, 1, 6)
func_6165_call = mod.get_global_var('func_6165')
func_6166_call = mutated_mod.get_global_var('func_6166')
call_7826 = relay.TupleGetItem(func_6165_call(), 2)
call_7827 = relay.TupleGetItem(func_6166_call(), 2)
output = relay.Tuple([call_7778,call_7782,call_7784,call_7788,call_7803,var_7805,var_7806,bop_7809,call_7826,])
output2 = relay.Tuple([call_7779,call_7783,call_7785,call_7789,call_7807,var_7805,var_7806,bop_7809,call_7827,])
func_7833 = relay.Function([var_7805,var_7806,], output)
mod['func_7833'] = func_7833
mod = relay.transform.InferType()(mod)
mutated_mod['func_7833'] = func_7833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7833_call = mutated_mod.get_global_var('func_7833')
var_7835 = relay.var("var_7835", dtype = "float64", shape = (2,))#candidate|7835|(2,)|var|float64
var_7836 = relay.var("var_7836", dtype = "uint16", shape = (448,))#candidate|7836|(448,)|var|uint16
call_7834 = func_7833_call(var_7835,var_7836,)
output = call_7834
func_7837 = relay.Function([var_7835,var_7836,], output)
mutated_mod['func_7837'] = func_7837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3236_call = mutated_mod.get_global_var('func_3236')
call_7857 = relay.TupleGetItem(func_3234_call(), 1)
call_7858 = relay.TupleGetItem(func_3236_call(), 1)
uop_7869 = relay.cosh(call_7857.astype('float32')) # shape=(200,)
uop_7871 = relay.cosh(call_7858.astype('float32')) # shape=(200,)
func_2516_call = mod.get_global_var('func_2516')
func_2520_call = mutated_mod.get_global_var('func_2520')
const_7873 = relay.const(8, dtype = "uint64")#candidate|7873|()|const|uint64
const_7874 = relay.const([5,8,2,10,10,4,5,-3,-2,1,9,-5,1,-8,-3,4,5,-8,2,2,5,-1,-1,-1,7,10,-8,-4,3,8,7,8,5,-10,1,-1,9,9,4,-2,3,-8,9,10,2], dtype = "uint64")#candidate|7874|(45,)|const|uint64
call_7872 = func_2516_call(relay.reshape(const_7873.astype('uint64'), []), relay.reshape(const_7874.astype('uint64'), [5, 3, 3]), )
call_7875 = func_2516_call(relay.reshape(const_7873.astype('uint64'), []), relay.reshape(const_7874.astype('uint64'), [5, 3, 3]), )
var_7877 = relay.var("var_7877", dtype = "float32", shape = (200,))#candidate|7877|(200,)|var|float32
bop_7878 = relay.not_equal(uop_7869.astype('bool'), relay.reshape(var_7877.astype('bool'), relay.shape_of(uop_7869))) # shape=(200,)
bop_7881 = relay.not_equal(uop_7871.astype('bool'), relay.reshape(var_7877.astype('bool'), relay.shape_of(uop_7871))) # shape=(200,)
output = relay.Tuple([call_7872,const_7873,const_7874,bop_7878,])
output2 = relay.Tuple([call_7875,const_7873,const_7874,bop_7881,])
func_7884 = relay.Function([var_7877,], output)
mod['func_7884'] = func_7884
mod = relay.transform.InferType()(mod)
var_7885 = relay.var("var_7885", dtype = "float32", shape = (200,))#candidate|7885|(200,)|var|float32
output = func_7884(var_7885)
func_7886 = relay.Function([var_7885], output)
mutated_mod['func_7886'] = func_7886
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7987 = relay.var("var_7987", dtype = "uint32", shape = (14, 8, 13))#candidate|7987|(14, 8, 13)|var|uint32
const_7988 = relay.const([[[-3,-9,-9,-8,-6,-3,6,-8,3,-4,-3,-9,-3],[-3,-2,-8,3,5,10,-4,4,1,-1,-4,-8,-1],[9,2,-4,-7,-9,1,-4,-5,10,5,9,6,6],[6,10,-7,-9,3,3,-10,-6,-6,9,-9,3,5],[-9,-3,2,-8,-1,1,3,-5,-5,9,-8,-4,-6],[-8,-6,-10,5,-1,-5,9,-6,-5,-6,3,5,-3],[-9,-4,9,-4,4,-1,7,5,-10,7,-5,-3,5],[2,-2,-5,-9,5,-10,4,-3,2,-4,-4,-1,10]],[[-5,7,-3,-10,-2,-5,5,-3,-7,8,10,9,-8],[10,-6,-5,5,1,-3,-10,-7,9,5,8,7,-3],[7,-2,-7,-6,3,3,5,6,6,-4,3,6,3],[9,9,8,-3,3,-3,2,10,3,-9,3,5,8],[-9,5,6,2,3,1,10,-6,1,-8,3,-8,10],[-8,9,4,-10,-1,-10,-2,-5,-3,-9,8,8,2],[-9,6,2,-6,-9,10,-9,8,6,-4,-4,-7,-5],[4,-3,7,-7,-1,6,-1,-10,-6,3,-10,-3,1]],[[-1,-2,-3,2,-5,8,-9,-2,-8,9,3,9,-9],[-7,3,-2,6,3,-2,-7,-5,10,6,10,-4,-4],[-4,5,1,-8,9,9,5,9,10,-6,-1,-8,10],[-10,6,-3,4,8,9,-10,-5,6,-2,9,10,-4],[4,5,9,-10,9,9,-1,-9,-10,-1,-9,-5,3],[-10,1,-4,-7,9,-6,4,4,9,8,-8,-8,-5],[7,7,-6,-4,2,-2,-9,-6,3,8,-3,3,-6],[2,-9,2,-1,-7,-5,-5,-9,5,-1,-2,-3,10]],[[-9,7,-3,1,8,-9,2,7,8,-6,1,4,-4],[-4,9,3,6,-5,-1,-2,-4,9,8,-5,9,3],[5,-10,6,-6,-8,4,8,-7,-10,7,10,9,-3],[-4,6,-10,5,-9,-6,7,-5,9,2,2,5,-3],[-9,-4,-7,-3,-6,-1,5,-3,5,4,-10,-3,9],[4,7,2,10,-6,-6,9,4,-4,-7,7,-8,-2],[-3,3,-10,-9,-6,3,-5,-4,-2,3,-2,4,-8],[3,-3,6,-8,2,-8,7,10,-2,10,7,7,-7]],[[-9,-10,3,4,-6,4,1,-4,-6,5,-10,10,10],[-2,-7,10,2,-4,-1,3,-9,3,-4,1,9,-4],[2,1,-1,-3,-3,-6,-10,2,-9,1,1,-9,5],[4,7,-3,2,-3,6,-3,6,4,10,-9,10,-6],[-6,-7,-9,2,-9,-5,8,5,-3,-5,-6,6,6],[4,3,-10,-6,-9,7,1,6,-8,3,2,-10,4],[7,-3,-5,-2,6,9,-8,7,8,1,5,2,-3],[-3,-1,-2,-8,5,9,-2,-7,8,-7,-1,4,-1]],[[-3,6,-7,-10,7,9,6,-9,-1,-1,1,-4,-8],[-5,6,1,1,7,8,8,-1,3,3,4,10,-2],[7,-9,-10,-7,-10,-8,-10,9,-2,5,6,-1,-9],[-10,-10,-2,-8,-2,-5,5,-1,-6,-7,1,4,3],[6,-8,6,-6,2,-3,-10,1,8,-1,-10,-2,-4],[6,-2,9,-2,-5,-8,-5,10,3,7,-5,1,-3],[-3,-7,1,6,-4,-1,5,-5,10,3,9,10,-1],[10,1,4,10,2,7,-5,6,-9,4,3,-3,-6]],[[4,8,-2,-9,2,8,7,3,9,-8,6,5,-1],[-5,-5,-9,-8,-6,5,-5,1,1,3,-3,-4,9],[-6,1,3,2,-9,-8,-7,-7,-10,-1,6,-10,-6],[5,-3,9,1,7,-7,3,-1,3,7,-2,4,9],[-3,-1,1,-8,-2,-4,-6,10,-1,9,6,-9,6],[10,-5,10,-8,-5,-10,-3,-10,7,7,1,-10,9],[-4,1,-10,-10,1,-2,-2,10,-2,4,10,-9,-9],[-3,1,-9,2,7,-10,-8,-6,10,9,-1,2,4]],[[9,9,4,-10,-5,1,6,9,4,7,-8,-1,-8],[10,10,-4,-5,-8,6,-5,-5,-8,4,-9,7,-2],[4,3,-6,3,-5,6,1,-1,9,10,2,-9,7],[7,-3,-10,10,10,-6,-3,-2,-3,2,10,9,9],[7,-8,-3,10,-3,4,4,1,-9,-1,5,5,-9],[9,6,9,-6,-10,3,-7,-2,10,-9,6,-7,-10],[-2,-8,-2,10,8,3,-8,3,5,-8,4,-1,-8],[10,5,-6,5,-7,-4,4,8,-6,-2,-8,10,2]],[[-1,-5,-1,4,5,2,-7,-8,5,5,-1,10,1],[-8,3,4,-4,-4,-6,-10,2,2,8,4,-3,-9],[-1,10,8,-4,-10,6,9,-9,-2,-7,-9,-6,10],[4,-1,2,3,-4,1,-1,-6,5,7,-2,4,-3],[-10,-4,9,8,3,1,-3,7,3,-3,5,6,-3],[-2,10,2,6,-4,3,6,1,10,-2,-8,-4,-8],[10,-2,-4,1,-2,6,8,3,-2,-5,-6,-9,-3],[7,-7,-8,-1,-9,5,-1,-3,-4,-6,2,6,3]],[[4,4,6,-7,-6,-9,5,2,-9,6,-1,-3,-7],[-7,4,-9,-1,-6,-4,-1,5,-7,-7,10,-3,8],[-9,3,7,1,3,10,2,-2,-6,-7,2,-1,5],[4,10,-4,-4,6,-10,-5,-8,-8,8,7,4,4],[7,4,7,-2,2,7,-6,1,2,8,10,10,-7],[-1,10,4,1,9,-7,-6,-8,9,5,-1,-6,5],[-6,-4,-2,1,-10,-9,-4,8,3,4,-6,7,-3],[-8,-7,4,10,6,1,-5,-2,-2,5,10,4,1]],[[-5,3,7,6,6,9,6,-1,-3,-9,-3,3,-1],[-5,-7,6,5,1,-1,-7,-6,7,2,-10,4,-1],[-10,-4,7,5,8,-7,1,6,-4,-10,-9,-4,-5],[-5,-6,6,1,9,1,-4,-7,3,-9,-9,4,-3],[6,-4,-6,10,7,9,5,-6,4,-5,-10,-1,9],[-2,-9,6,4,6,8,1,-9,-3,-10,1,8,-7],[6,7,-7,-10,4,2,3,10,-4,-7,1,9,1],[-7,8,9,-9,-3,5,-3,-7,-9,-4,2,-9,-3]],[[10,-4,-2,10,-5,5,-7,-2,-10,-1,3,7,-10],[5,9,2,8,10,6,-9,1,7,-2,10,4,-7],[3,4,3,3,-7,-1,2,8,-3,9,1,-2,4],[3,3,-5,-5,2,-10,2,-1,-6,-6,10,-1,5],[-6,-5,9,8,-1,10,4,4,8,-3,10,-1,2],[-8,-2,-5,8,-9,-7,10,-10,3,-2,-7,-4,-9],[-10,1,-6,4,-9,-6,-8,-5,4,4,6,9,6],[-8,6,5,2,9,4,-5,2,-2,-8,7,2,5]],[[1,-6,10,5,3,-6,-7,-10,6,-4,7,-1,4],[-7,1,4,8,9,6,-7,-6,-2,6,4,7,4],[-3,-1,7,3,1,-2,-9,-8,4,4,8,5,-7],[-8,6,-10,-9,5,-10,3,-8,-2,-3,2,8,1],[1,10,2,6,-1,6,9,3,-10,5,-1,-4,9],[-4,-3,5,-1,-6,2,-3,-10,3,10,1,2,7],[4,10,9,-4,-10,-8,1,-6,-6,8,-7,5,6],[-7,-5,4,8,-5,-9,-1,8,-2,5,-6,6,-7]],[[4,8,2,-10,2,6,-9,8,4,9,-1,2,8],[7,9,-4,-7,-5,-10,6,9,3,-7,-6,-10,-2],[3,-7,10,-4,7,6,-2,3,-5,7,4,-2,1],[-1,-2,-4,-7,-7,-4,-9,-10,-4,-5,-6,9,4],[3,4,5,-5,-10,-3,1,-5,-2,-7,-7,-5,-10],[-3,-4,2,-5,9,4,9,6,-9,6,1,8,8],[-1,-10,-4,1,1,5,-2,10,-2,-9,4,3,-4],[6,4,-9,-9,-5,-1,-2,2,2,6,9,2,-4]]], dtype = "uint32")#candidate|7988|(14, 8, 13)|const|uint32
bop_7989 = relay.left_shift(var_7987.astype('uint32'), relay.reshape(const_7988.astype('uint32'), relay.shape_of(var_7987))) # shape=(14, 8, 13)
output = bop_7989
output2 = bop_7989
F = relay.Function([var_7987,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7987,], output2)
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
