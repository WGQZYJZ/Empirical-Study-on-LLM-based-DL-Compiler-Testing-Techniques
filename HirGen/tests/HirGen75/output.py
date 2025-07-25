import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_86 = relay.var("var_86", dtype = "int16", shape = (11, 6, 7))#candidate|86|(11, 6, 7)|var|int16
var_87 = relay.var("var_87", dtype = "int16", shape = (11, 6, 7))#candidate|87|(11, 6, 7)|var|int16
bop_88 = relay.bitwise_or(var_86.astype('int16'), relay.reshape(var_87.astype('int16'), relay.shape_of(var_86))) # shape=(11, 6, 7)
uop_103 = relay.atan(bop_88.astype('float64')) # shape=(11, 6, 7)
output = relay.Tuple([uop_103,])
output2 = relay.Tuple([uop_103,])
func_107 = relay.Function([var_86,var_87,], output)
mod['func_107'] = func_107
mod = relay.transform.InferType()(mod)
mutated_mod['func_107'] = func_107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_107_call = mutated_mod.get_global_var('func_107')
var_109 = relay.var("var_109", dtype = "int16", shape = (11, 6, 7))#candidate|109|(11, 6, 7)|var|int16
var_110 = relay.var("var_110", dtype = "int16", shape = (11, 6, 7))#candidate|110|(11, 6, 7)|var|int16
call_108 = func_107_call(var_109,var_110,)
output = call_108
func_111 = relay.Function([var_109,var_110,], output)
mutated_mod['func_111'] = func_111
mutated_mod = relay.transform.InferType()(mutated_mod)
const_250 = relay.const([[[-4.390330,8.560359,1.088030,-2.019884,-0.269375,5.096090,-7.090822,-2.611110,3.323921,-4.766562,6.642975,-5.716444],[1.834377,-2.498793,7.660237,1.983534,4.805967,5.117010,-1.289374,-2.835658,5.733737,-4.623869,-9.166485,-5.685752],[-7.036204,1.093168,2.694299,1.062898,2.383094,7.341297,2.297802,-7.423818,0.332592,-8.829817,3.266686,-9.062597],[-6.094548,-7.631466,9.953856,0.588846,-5.799708,-5.927723,-6.020141,-4.738351,2.503466,-5.734779,0.744630,-6.814546],[4.560743,-9.520650,1.155583,6.946729,9.229347,-1.293912,-0.379841,-7.720049,6.501144,-9.882178,-3.218851,2.516832],[-1.332528,9.675145,-9.877607,7.481355,-2.515700,7.736006,-3.771089,2.553129,-8.939865,0.736184,0.723805,1.842470],[-0.450829,-5.461921,0.414652,-5.010543,-8.479290,0.313895,3.503850,-9.301907,-0.972230,8.574970,-6.885996,7.090338],[0.252278,6.490058,-0.432062,1.762786,-2.421132,-3.139441,7.542939,-2.878464,-5.254825,-0.240845,-0.338151,7.397270]],[[-1.267824,3.477200,2.509370,-4.082739,7.587904,-8.002071,-7.749654,-0.136523,5.810306,-9.501616,-1.510791,-9.011350],[-0.027097,-5.513287,1.445244,-3.011327,2.469718,-4.102669,-3.721063,2.139311,-0.215094,0.656697,9.336886,-1.909268],[-9.513048,4.960111,7.307633,7.370005,-7.566634,-4.142907,8.835846,-1.883331,-3.826225,-9.420043,4.488275,9.230145],[4.496467,-2.109765,-4.187416,7.149297,-8.726303,1.998195,8.802557,3.720480,4.250706,1.152052,-7.473397,3.066444],[2.344100,1.036693,3.416806,-6.875529,-3.807768,2.410031,4.302360,9.064962,7.513023,8.483861,-4.604825,-7.463554],[-3.560936,-2.680685,7.873895,-1.111566,4.521569,8.449428,-6.047047,9.173395,0.716587,6.762304,-0.867573,-1.644502],[-2.649046,-4.382296,-1.628187,-0.155106,-1.405480,-7.299301,-8.994634,-7.991627,-7.015468,-0.856849,-2.794103,9.109072],[-1.522396,-3.978002,-5.946345,-5.492310,2.323055,8.778046,1.850046,-0.688373,-4.047883,-0.757370,3.667714,0.485683]],[[-8.450041,-4.030311,4.570813,-0.710570,0.879647,-4.548522,4.694494,-0.394592,6.473572,6.164268,6.345300,8.460137],[-8.104236,-5.760371,-3.630119,3.088795,0.422382,2.634747,-8.419441,-0.706093,1.361162,2.118622,4.822710,6.823860],[9.876853,0.748515,-8.266925,-1.474509,-1.348690,9.096330,-6.568172,-8.034157,-2.768751,9.035888,0.179199,-0.351429],[-1.965142,-2.676975,7.136029,7.430172,-8.816180,3.716179,6.182552,3.515149,-1.457050,-0.125372,7.953429,-6.313787],[1.062789,-8.282694,4.496387,9.942519,-7.911205,8.966522,5.306937,-7.540382,-8.886805,-0.485175,-4.190953,0.865919],[-6.231479,2.958251,-6.118542,-9.475048,7.826221,7.582806,7.664015,6.806166,-1.477873,-6.833181,9.297391,4.051469],[-4.065209,6.316453,0.265923,-9.032943,-5.499785,9.341637,2.502117,-4.386491,3.536626,-4.954314,-8.241653,-0.845771],[-1.274419,-4.252653,-1.390398,2.111628,-0.737637,3.423790,-9.532514,3.808213,5.606345,2.854884,-0.702006,-9.593547]],[[5.236925,9.305121,-2.599385,-0.589369,-7.456410,-2.812526,-0.068531,1.071645,-2.056624,-7.975472,-0.385647,2.843848],[4.614093,4.309187,3.356368,7.092220,-6.740870,-3.033413,-4.403032,9.655185,-1.150518,7.091784,-5.477167,8.532536],[1.439426,3.526723,1.587829,-8.715711,6.180518,9.541090,7.529483,-8.486930,1.536289,-9.304218,0.233844,-6.800976],[9.786803,4.685748,-5.683710,-4.615150,-1.259086,-7.012200,-3.747685,-2.288529,-1.902561,-5.668167,-9.232662,9.478076],[-7.557621,-9.007359,0.331712,3.727181,-6.885993,-4.567891,4.857537,1.315972,-6.786468,3.385516,-5.394864,5.354389],[8.985747,-1.890302,-0.357393,3.881923,3.048329,-7.529528,-5.805517,6.899633,-3.077217,-5.763898,-7.975953,-0.792051],[3.038458,7.852009,4.770896,-7.142715,8.180252,3.814380,-3.620954,-7.352178,-3.318648,-4.768973,-6.183156,8.288719],[-4.372969,-7.662915,5.038585,2.829665,-7.724040,-1.276516,5.578533,3.460596,9.310623,-3.773501,2.542531,7.564929]],[[-8.811971,0.632843,1.333788,3.236506,-5.398204,-8.892473,-7.257750,-4.048697,3.131989,1.504639,1.860727,1.498254],[2.425165,-7.109880,-0.049050,-9.035848,6.919391,3.125885,-1.080585,-2.571310,-1.980064,8.877798,8.739065,1.544446],[-7.697497,0.566737,4.698456,7.344396,2.239463,-7.500627,6.621344,-5.146744,-6.400365,-9.137000,-0.836660,2.981232],[6.864065,-4.684361,-4.597247,8.419813,-3.711559,-7.232113,8.262294,-8.136347,1.540928,-5.227335,3.772739,7.948728],[-1.466281,-0.627859,0.580071,4.441329,-5.072459,5.996992,-8.235721,-1.543079,9.567455,-8.407829,-9.474235,6.414677],[5.219072,-0.129508,-7.570628,-6.337342,0.265403,-2.104697,-9.755084,-1.767029,3.991359,4.242599,-1.915770,-4.427899],[-3.722615,2.646502,3.044252,-7.893671,-0.113730,8.120133,4.368636,-0.624160,-9.886318,6.816067,-8.113599,-1.638901],[6.554757,4.268001,5.792381,1.113420,1.655891,-9.601730,-1.556276,5.926036,9.954281,7.039427,2.625935,-3.006472]],[[-3.231442,-1.134671,2.323818,-3.799804,2.494765,-3.942303,1.739452,-3.320270,-1.248170,1.955863,-0.225534,-3.743620],[1.784706,-8.155718,9.466078,6.705830,-7.905039,-6.612280,-2.317041,-4.786299,5.268507,-8.445313,-9.842639,2.961711],[1.370108,7.153190,6.645496,7.098008,-7.911121,1.603679,-4.706578,4.592843,9.438446,-5.672676,5.255314,4.131079],[-6.101455,2.787175,-7.269512,6.804744,-3.527268,8.017182,-0.786733,-3.823132,-0.019036,-3.810814,-3.780010,6.693383],[-6.956303,0.083504,-3.541509,-7.666656,-7.253808,-6.320022,-3.478965,-7.182979,-6.921307,-1.993595,3.495704,6.853401],[9.847679,-7.717609,-6.244930,9.931829,-2.452098,-6.021770,8.081697,2.735538,-0.827251,-2.766719,6.022896,8.534229],[1.901645,2.900551,7.210782,-7.625163,-7.724110,-9.622986,1.732006,6.929599,3.166279,-0.128239,-3.004876,-4.339056],[1.276644,2.084707,-2.685398,9.989441,6.740268,-7.899447,0.358092,9.037100,9.236225,-2.456032,3.650728,-7.852948]],[[3.621710,5.703566,-0.687963,3.759319,-1.663738,9.800850,3.346094,-3.939445,0.706306,3.030028,-4.522884,-2.726144],[1.290810,-0.032487,9.737723,0.124136,5.321152,-6.630764,-0.227527,-1.150765,5.670943,4.306574,-6.019392,4.863455],[-1.990167,-5.623035,4.799223,6.467208,-1.225229,1.846129,-1.713930,-5.848242,3.914654,-8.554995,-9.443424,-8.725138],[-9.412437,1.321446,-1.859869,-3.141241,6.427074,6.262882,6.618410,6.673118,-5.577925,9.058352,8.165618,-7.702518],[7.310694,8.317312,3.917339,5.457244,7.844748,-0.281456,1.981946,6.338335,-1.413057,5.621946,6.556524,4.777824],[1.496059,-4.044528,-7.607847,9.842384,1.507870,-3.026750,-6.710864,-6.867823,-1.397358,8.884006,0.149669,-2.399453],[4.329994,-0.775466,1.462353,-3.324790,-7.191082,1.815407,-4.737005,-4.853371,2.520510,-2.363008,-5.435444,-7.592907],[-1.378132,-6.148932,-6.459562,5.741126,-5.661124,-0.024757,8.303766,-8.970422,4.347380,-7.814813,-5.889689,-1.287122]],[[3.623512,-8.161650,4.455697,-1.361369,-1.630173,-4.591105,-9.356726,2.799187,9.990231,-3.133980,-0.605294,-7.725187],[-0.336095,6.987100,-4.404588,9.675744,9.679328,0.385100,-3.218155,-5.914214,8.800499,4.069782,-3.022011,-0.160345],[-5.159208,-2.951790,-3.710844,-7.630401,5.961372,9.663618,0.804353,-0.479342,-8.067197,-2.700833,3.730149,-2.105600],[9.760879,-3.555569,-9.307076,0.335792,5.958890,3.081971,-2.278102,7.314698,-1.453823,6.995746,0.810155,-2.577167],[-5.492208,-7.786173,8.232405,-9.125808,-1.633029,-0.746993,8.518611,7.147879,6.767885,-7.772734,-3.458710,1.741805],[2.677221,7.126736,-1.646440,-1.262353,-2.142428,8.710460,6.679065,-3.083928,-0.417091,-0.551246,-7.294323,1.484343],[8.813718,2.578682,4.940162,-7.741554,-2.720909,4.790900,2.843854,6.226012,-2.359256,2.647161,-4.682998,6.070407],[-4.414095,-3.239581,7.930422,-3.597510,-7.343917,-9.747135,-6.547194,-1.122977,-1.897980,-7.002742,5.592338,7.962077]],[[-5.637054,-9.454549,-1.488218,2.513091,9.371659,4.259345,4.917794,9.183214,-6.706754,3.343773,-1.159544,7.385063],[1.701788,-2.942227,6.942937,-3.859199,-4.128708,-8.781840,-5.877915,9.752442,0.158301,-6.126450,-2.971838,-6.671100],[-0.979481,-0.149427,9.336670,1.295695,6.355437,-7.211565,-9.443549,-0.103548,4.493360,5.064335,-8.066417,5.559896],[-2.980595,6.131985,-5.341225,2.920187,3.897948,0.167045,9.665789,-9.203409,4.729816,4.105619,4.142220,-2.254707],[-3.692372,7.707007,6.856629,-8.647548,-9.812069,-7.134447,-8.238896,6.539862,8.250286,-0.100377,-7.854520,0.033253],[2.569682,5.618981,-6.072834,3.809259,7.934097,-2.537529,-6.257107,-7.120166,-9.634104,5.143082,-5.261552,-0.547836],[7.420125,-8.104856,6.803283,3.275293,-8.383190,-9.832891,2.977638,5.433570,-6.092591,0.024304,9.134143,9.094929],[-0.972428,-4.171174,-3.552959,9.968224,2.894214,2.570385,6.660122,-9.607344,6.143378,4.977203,-5.282120,0.789622]],[[-4.723517,3.909868,1.427851,0.826309,3.146158,-8.539233,-9.987483,-2.839086,-1.191331,7.803765,-5.639252,0.065230],[-2.099682,-9.794547,-3.866204,9.221985,-2.829217,-9.204673,1.152350,-6.013840,1.616910,-0.152294,-2.667582,1.526285],[-3.231133,-2.623088,-4.976663,-5.726730,-7.634780,-8.985947,9.831493,2.941031,-1.088262,3.434455,1.038318,4.170335],[-4.181641,7.700288,-1.338311,9.175912,5.304894,6.395656,-2.722559,-7.897426,0.771460,1.636401,-8.505630,-3.665394],[-0.098613,-9.307777,3.738291,-7.068232,-9.328959,-8.719309,-3.629630,1.553806,-3.881598,-9.878029,5.484328,7.099436],[2.549543,3.275788,-5.945907,-1.446233,6.903331,-9.062629,-6.879605,-2.449881,-5.698209,0.203839,5.321549,-3.585809],[-8.322684,-2.777346,2.849387,-1.724511,-2.724869,-0.966302,9.276780,7.334142,-8.191585,-5.876520,-1.784995,6.711930],[5.384981,7.169410,1.643062,-2.596433,-0.274651,1.005137,9.127564,-4.799186,1.630852,-7.779289,-9.497091,1.314007]]], dtype = "float32")#candidate|250|(10, 8, 12)|const|float32
uop_251 = relay.sinh(const_250.astype('float32')) # shape=(10, 8, 12)
output = uop_251
output2 = uop_251
func_254 = relay.Function([], output)
mod['func_254'] = func_254
mod = relay.transform.InferType()(mod)
output = func_254()
func_255 = relay.Function([], output)
mutated_mod['func_255'] = func_255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_278 = func_254_call()
call_279 = func_254_call()
uop_300 = relay.erf(call_278.astype('float32')) # shape=(10, 8, 12)
uop_302 = relay.erf(call_279.astype('float32')) # shape=(10, 8, 12)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_303 = func_254_call()
call_304 = func_254_call()
var_309 = relay.var("var_309", dtype = "float32", shape = (10, 8, 12))#candidate|309|(10, 8, 12)|var|float32
bop_310 = relay.add(uop_300.astype('uint8'), relay.reshape(var_309.astype('uint8'), relay.shape_of(uop_300))) # shape=(10, 8, 12)
bop_313 = relay.add(uop_302.astype('uint8'), relay.reshape(var_309.astype('uint8'), relay.shape_of(uop_302))) # shape=(10, 8, 12)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_319 = func_254_call()
call_320 = func_254_call()
output = relay.Tuple([call_303,bop_310,call_319,])
output2 = relay.Tuple([call_304,bop_313,call_320,])
func_321 = relay.Function([var_309,], output)
mod['func_321'] = func_321
mod = relay.transform.InferType()(mod)
mutated_mod['func_321'] = func_321
mutated_mod = relay.transform.InferType()(mutated_mod)
var_322 = relay.var("var_322", dtype = "float32", shape = (10, 8, 12))#candidate|322|(10, 8, 12)|var|float32
func_321_call = mutated_mod.get_global_var('func_321')
call_323 = func_321_call(var_322)
output = call_323
func_324 = relay.Function([var_322], output)
mutated_mod['func_324'] = func_324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_332 = func_254_call()
call_333 = func_254_call()
func_321_call = mod.get_global_var('func_321')
func_324_call = mutated_mod.get_global_var('func_324')
call_340 = relay.TupleGetItem(func_321_call(relay.reshape(call_332.astype('float32'), [10, 8, 12])), 2)
call_341 = relay.TupleGetItem(func_324_call(relay.reshape(call_332.astype('float32'), [10, 8, 12])), 2)
uop_349 = relay.sigmoid(call_340.astype('float64')) # shape=(10, 8, 12)
uop_351 = relay.sigmoid(call_341.astype('float64')) # shape=(10, 8, 12)
output = relay.Tuple([call_332,uop_349,])
output2 = relay.Tuple([call_333,uop_351,])
func_353 = relay.Function([], output)
mod['func_353'] = func_353
mod = relay.transform.InferType()(mod)
output = func_353()
func_354 = relay.Function([], output)
mutated_mod['func_354'] = func_354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_354_call = mutated_mod.get_global_var('func_354')
call_375 = relay.TupleGetItem(func_353_call(), 0)
call_376 = relay.TupleGetItem(func_354_call(), 0)
uop_381 = relay.log(call_375.astype('float32')) # shape=(10, 8, 12)
uop_383 = relay.log(call_376.astype('float32')) # shape=(10, 8, 12)
output = uop_381
output2 = uop_383
func_385 = relay.Function([], output)
mod['func_385'] = func_385
mod = relay.transform.InferType()(mod)
output = func_385()
func_386 = relay.Function([], output)
mutated_mod['func_386'] = func_386
mutated_mod = relay.transform.InferType()(mutated_mod)
const_480 = relay.const([[[2.311607,-0.696050,-7.086508,-6.200341,-9.901888,-6.686595,0.236397,6.864550],[-0.124159,-5.451248,5.058404,-8.837407,6.542028,-2.860318,0.764366,3.573236],[-1.135086,9.984289,6.099182,-0.624900,9.942810,8.836838,-5.027472,-7.699627],[1.641895,-9.881323,3.544195,6.965480,-6.158810,6.869159,6.308300,-8.806986],[-9.714390,-5.808836,0.659562,1.492081,1.894692,2.311857,7.128793,-2.558667],[-3.385040,0.368977,-4.354681,-0.349151,-0.596098,-8.889053,5.073450,7.070800],[-2.709722,7.589207,1.184947,-5.240435,9.612892,-2.733408,3.047786,-0.132777]],[[2.580333,-0.787198,-2.129263,-5.531676,-5.080185,-2.228369,1.183286,7.704048],[-9.714496,-4.753962,4.529475,-6.985105,-6.062709,-9.207241,-4.230699,-5.506325],[-8.925407,9.502977,1.654865,-5.506936,-6.390722,3.350440,-1.114726,6.694103],[-4.941334,-9.205837,3.926184,-3.633660,3.404415,7.701633,7.465125,9.756812],[-4.695108,-2.414656,-6.511314,7.623302,-2.615257,2.279554,8.854219,7.921524],[-5.843329,-3.692569,-3.297903,5.051607,7.165894,0.787005,-9.644674,-0.536404],[2.987525,2.109462,0.916025,-6.975436,1.236866,9.197707,4.652884,-1.234941]],[[-5.321412,0.491953,-4.008211,5.762245,8.779516,-2.163573,6.980981,4.588046],[-6.920622,1.366993,4.173891,7.203463,2.437991,-8.204150,1.448220,-5.911410],[4.480525,-7.898883,-8.363048,0.890253,8.363532,-5.125460,-7.406490,9.471982],[-0.908993,3.344807,6.671194,-4.246526,4.714394,6.711245,-3.513762,-6.825976],[0.295009,5.236652,-8.317818,8.244412,-1.513825,5.933657,5.956483,6.154765],[3.138235,-2.667387,2.186208,0.586778,3.247910,2.734235,-6.970226,7.581041],[5.437861,9.486615,4.302291,5.625521,-5.856273,-4.962125,6.734342,3.154623]],[[-2.466149,2.023710,1.245304,-1.917054,6.612756,-4.657733,-5.603948,0.567912],[-9.664681,2.645277,-0.725320,4.191064,6.819038,-2.729650,-9.306278,4.201062],[5.089204,-7.043386,0.684379,3.544561,3.683014,-5.827072,1.251224,8.858456],[8.127531,4.049982,4.490578,-8.319002,4.461040,9.266403,5.857208,-2.200609],[-2.756386,8.065710,-7.685357,-3.197425,-9.747218,6.910208,5.754609,5.350158],[3.092104,-8.002883,8.823198,-8.208130,6.307925,-3.355388,-3.328605,-2.249351],[-5.243329,2.478126,-0.311888,-4.921054,-4.752482,1.455343,-4.366241,-6.416404]],[[0.671032,-7.335152,-1.248475,7.843862,-6.347177,-9.450262,9.653837,4.342835],[-1.750006,-8.458609,8.211092,0.099276,-7.500054,2.249632,2.428355,-9.199455],[-5.898817,7.511729,8.207365,-4.302554,2.155901,5.818868,6.607841,-1.475159],[5.612557,2.127017,7.465412,-2.252605,8.677298,-4.396157,-6.734018,5.885428],[9.758333,0.804323,-7.574332,-7.943169,-1.649087,-3.255642,8.212258,4.459255],[2.433996,7.610345,1.237666,-3.412263,4.388661,7.295823,3.633715,-5.387358],[7.838714,-7.194017,4.599448,5.735319,-6.646277,-5.942912,-7.427559,-5.446790]],[[-9.185695,-2.631189,8.042293,-6.451027,8.522872,-3.969684,-9.753604,3.211167],[-4.295009,8.673100,5.602924,2.051626,-3.532517,6.286944,5.805141,-9.016582],[4.351044,9.058524,5.603328,0.436975,4.930684,-1.660519,-3.308581,-9.516550],[4.340669,-7.209249,-1.274718,-2.223411,4.344620,-6.629355,8.511572,-2.356633],[5.760707,3.544357,3.576855,-1.982819,8.297035,2.953726,-5.572029,-3.325819],[0.122733,-2.457703,1.909236,0.162203,-0.365159,7.377233,-1.816940,-7.777047],[-2.228728,7.108084,-7.807073,-3.826453,-6.592260,4.196897,3.776440,-1.942432]],[[1.545204,2.312285,1.936675,9.263400,-9.080351,7.072701,0.459792,-3.936617],[8.060758,8.905294,0.804910,2.435848,5.337661,3.021626,3.973297,-1.182762],[-9.278614,8.541013,-7.142138,-5.255184,1.210763,0.993963,6.005716,-6.360034],[8.693144,3.379666,-2.240442,-8.051474,8.931804,-2.634638,9.137453,6.718098],[-5.290706,5.255950,-2.127147,0.455001,4.888821,-6.843564,3.502977,-7.564864],[-5.083969,1.481549,-4.233192,1.627756,3.837139,-8.799054,-8.980907,5.122018],[-8.385327,0.278464,-2.532873,1.155037,9.454113,-5.120537,-3.390141,-8.703526]],[[-5.000501,1.563706,8.733569,7.846144,7.134811,-2.087348,6.424492,-8.628356],[-1.554459,-0.949466,0.003478,7.880342,1.105386,2.109751,-3.152252,7.204334],[0.006153,8.644952,1.241637,-9.040550,5.687385,-3.293089,-0.043152,-8.487235],[-6.571369,4.449231,-5.768699,-2.176298,-6.302180,-0.669712,6.720579,-3.800979],[-2.388859,-2.568818,-5.302896,-5.729932,8.036996,-9.170223,-6.249703,-1.438531],[-8.689024,-1.841222,-0.854234,-3.039946,-5.024928,5.361088,-9.009855,-1.010563],[-8.684156,-7.973257,3.436568,-2.449236,1.055472,-0.645343,3.606733,-7.208936]],[[-4.864958,3.837733,-9.270893,-7.703455,-1.363918,-1.430656,2.106359,5.967751],[7.258945,-4.616466,5.431328,6.612637,4.047201,-0.847498,1.321341,-4.668167],[1.190212,-0.294946,-0.501847,-0.312268,6.702070,8.953750,3.754376,-6.859977],[9.134059,-8.076486,7.201254,3.532511,4.857189,5.973247,7.189486,0.207288],[7.774607,-8.595864,-0.624269,-1.318323,9.910684,-0.198104,9.613800,-3.845765],[3.254360,2.359473,-2.875998,8.394842,-9.264426,-8.512416,2.231545,-8.666557],[-8.977648,-2.683932,1.915342,-8.522354,-5.295828,5.484159,8.111786,-3.749721]],[[-9.939833,9.809459,6.814649,7.289713,0.252013,8.284701,9.298713,-4.613179],[-2.327638,-0.680256,1.451133,-1.952046,3.435473,3.473358,4.173436,0.963420],[0.818671,4.944765,4.073641,-9.924928,-9.526740,7.324217,8.452789,2.755855],[-9.987606,7.321975,-4.167036,-5.822111,-6.431584,-4.831450,2.266586,6.154371],[-1.453669,0.753253,4.416818,0.853092,2.514872,8.878381,-0.462420,-9.179416],[-7.144568,-7.381734,-6.166752,-0.281107,9.422871,-3.449550,-8.289737,0.297262],[-5.718285,1.268910,3.740884,-2.288769,3.488661,4.680875,-7.479360,1.438332]]], dtype = "float64")#candidate|480|(10, 7, 8)|const|float64
uop_481 = relay.atan(const_480.astype('float64')) # shape=(10, 7, 8)
uop_485 = relay.cos(const_480.astype('float32')) # shape=(10, 7, 8)
func_353_call = mod.get_global_var('func_353')
func_354_call = mutated_mod.get_global_var('func_354')
call_490 = relay.TupleGetItem(func_353_call(), 1)
call_491 = relay.TupleGetItem(func_354_call(), 1)
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
var_495 = relay.var("var_495", dtype = "int16", shape = (462,))#candidate|495|(462,)|var|int16
call_494 = relay.TupleGetItem(func_107_call(relay.reshape(var_495.astype('int16'), [11, 6, 7]), relay.reshape(var_495.astype('int16'), [11, 6, 7]), ), 0)
call_496 = relay.TupleGetItem(func_111_call(relay.reshape(var_495.astype('int16'), [11, 6, 7]), relay.reshape(var_495.astype('int16'), [11, 6, 7]), ), 0)
output = relay.Tuple([uop_481,uop_485,call_490,call_494,var_495,])
output2 = relay.Tuple([uop_481,uop_485,call_491,call_496,var_495,])
func_501 = relay.Function([var_495,], output)
mod['func_501'] = func_501
mod = relay.transform.InferType()(mod)
mutated_mod['func_501'] = func_501
mutated_mod = relay.transform.InferType()(mutated_mod)
var_502 = relay.var("var_502", dtype = "int16", shape = (462,))#candidate|502|(462,)|var|int16
func_501_call = mutated_mod.get_global_var('func_501')
call_503 = func_501_call(var_502)
output = call_503
func_504 = relay.Function([var_502], output)
mutated_mod['func_504'] = func_504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_354_call = mutated_mod.get_global_var('func_354')
call_605 = relay.TupleGetItem(func_353_call(), 0)
call_606 = relay.TupleGetItem(func_354_call(), 0)
var_634 = relay.var("var_634", dtype = "float32", shape = (10, 8, 12))#candidate|634|(10, 8, 12)|var|float32
bop_635 = relay.minimum(call_605.astype('uint32'), relay.reshape(var_634.astype('uint32'), relay.shape_of(call_605))) # shape=(10, 8, 12)
bop_638 = relay.minimum(call_606.astype('uint32'), relay.reshape(var_634.astype('uint32'), relay.shape_of(call_606))) # shape=(10, 8, 12)
output = relay.Tuple([bop_635,])
output2 = relay.Tuple([bop_638,])
func_647 = relay.Function([var_634,], output)
mod['func_647'] = func_647
mod = relay.transform.InferType()(mod)
mutated_mod['func_647'] = func_647
mutated_mod = relay.transform.InferType()(mutated_mod)
var_648 = relay.var("var_648", dtype = "float32", shape = (10, 8, 12))#candidate|648|(10, 8, 12)|var|float32
func_647_call = mutated_mod.get_global_var('func_647')
call_649 = func_647_call(var_648)
output = call_649
func_650 = relay.Function([var_648], output)
mutated_mod['func_650'] = func_650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_385_call = mod.get_global_var('func_385')
func_386_call = mutated_mod.get_global_var('func_386')
call_667 = func_385_call()
call_668 = func_385_call()
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_690 = func_254_call()
call_691 = func_254_call()
func_353_call = mod.get_global_var('func_353')
func_354_call = mutated_mod.get_global_var('func_354')
call_696 = relay.TupleGetItem(func_353_call(), 1)
call_697 = relay.TupleGetItem(func_354_call(), 1)
output = relay.Tuple([call_667,call_690,call_696,])
output2 = relay.Tuple([call_668,call_691,call_697,])
func_698 = relay.Function([], output)
mod['func_698'] = func_698
mod = relay.transform.InferType()(mod)
mutated_mod['func_698'] = func_698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_698_call = mutated_mod.get_global_var('func_698')
call_699 = func_698_call()
output = call_699
func_700 = relay.Function([], output)
mutated_mod['func_700'] = func_700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_731 = func_254_call()
call_732 = func_254_call()
func_321_call = mod.get_global_var('func_321')
func_324_call = mutated_mod.get_global_var('func_324')
call_751 = relay.TupleGetItem(func_321_call(relay.reshape(call_731.astype('float32'), [10, 8, 12])), 1)
call_752 = relay.TupleGetItem(func_324_call(relay.reshape(call_731.astype('float32'), [10, 8, 12])), 1)
bop_759 = relay.logical_or(call_751.astype('bool'), relay.reshape(call_731.astype('bool'), relay.shape_of(call_751))) # shape=(10, 8, 12)
bop_762 = relay.logical_or(call_752.astype('bool'), relay.reshape(call_732.astype('bool'), relay.shape_of(call_752))) # shape=(10, 8, 12)
uop_767 = relay.asin(bop_759.astype('float64')) # shape=(10, 8, 12)
uop_769 = relay.asin(bop_762.astype('float64')) # shape=(10, 8, 12)
output = relay.Tuple([uop_767,])
output2 = relay.Tuple([uop_769,])
func_774 = relay.Function([], output)
mod['func_774'] = func_774
mod = relay.transform.InferType()(mod)
output = func_774()
func_775 = relay.Function([], output)
mutated_mod['func_775'] = func_775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_774_call = mod.get_global_var('func_774')
func_775_call = mutated_mod.get_global_var('func_775')
call_787 = relay.TupleGetItem(func_774_call(), 0)
call_788 = relay.TupleGetItem(func_775_call(), 0)
uop_805 = relay.acosh(call_787.astype('float32')) # shape=(10, 8, 12)
uop_807 = relay.acosh(call_788.astype('float32')) # shape=(10, 8, 12)
bop_809 = relay.left_shift(uop_805.astype('int8'), relay.reshape(call_787.astype('int8'), relay.shape_of(uop_805))) # shape=(10, 8, 12)
bop_812 = relay.left_shift(uop_807.astype('int8'), relay.reshape(call_788.astype('int8'), relay.shape_of(uop_807))) # shape=(10, 8, 12)
output = relay.Tuple([bop_809,])
output2 = relay.Tuple([bop_812,])
func_818 = relay.Function([], output)
mod['func_818'] = func_818
mod = relay.transform.InferType()(mod)
output = func_818()
func_819 = relay.Function([], output)
mutated_mod['func_819'] = func_819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_835 = func_254_call()
call_836 = func_254_call()
func_774_call = mod.get_global_var('func_774')
func_775_call = mutated_mod.get_global_var('func_775')
call_840 = relay.TupleGetItem(func_774_call(), 0)
call_841 = relay.TupleGetItem(func_775_call(), 0)
func_385_call = mod.get_global_var('func_385')
func_386_call = mutated_mod.get_global_var('func_386')
call_847 = func_385_call()
call_848 = func_385_call()
bop_854 = relay.bitwise_xor(call_840.astype('uint8'), relay.reshape(call_847.astype('uint8'), relay.shape_of(call_840))) # shape=(10, 8, 12)
bop_857 = relay.bitwise_xor(call_841.astype('uint8'), relay.reshape(call_848.astype('uint8'), relay.shape_of(call_841))) # shape=(10, 8, 12)
output = relay.Tuple([call_835,bop_854,])
output2 = relay.Tuple([call_836,bop_857,])
func_859 = relay.Function([], output)
mod['func_859'] = func_859
mod = relay.transform.InferType()(mod)
mutated_mod['func_859'] = func_859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mutated_mod.get_global_var('func_859')
call_860 = func_859_call()
output = call_860
func_861 = relay.Function([], output)
mutated_mod['func_861'] = func_861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_861_call = mutated_mod.get_global_var('func_861')
call_917 = relay.TupleGetItem(func_859_call(), 0)
call_918 = relay.TupleGetItem(func_861_call(), 0)
uop_924 = relay.sin(call_917.astype('float64')) # shape=(10, 8, 12)
uop_926 = relay.sin(call_918.astype('float64')) # shape=(10, 8, 12)
output = uop_924
output2 = uop_926
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
const_965 = relay.const([[[1,-10,10,1,9,-2,-9,9,8,-8,-2,9,10]],[[-2,-1,6,2,-10,-4,-8,5,7,-1,-1,8,5]],[[10,5,-7,-3,-4,2,-7,-8,5,5,6,-3,-6]],[[7,-4,6,-8,6,-10,4,1,9,8,8,-3,-1]],[[-5,-7,-1,-7,-7,-10,3,-8,6,8,8,5,3]],[[7,-6,-5,5,4,-6,-2,1,6,8,1,-8,1]],[[-4,-1,-2,5,9,1,-1,1,-3,8,2,1,10]],[[6,-9,-5,5,-2,-4,-5,6,-6,-10,-4,-9,10]],[[-8,3,-1,9,6,-4,10,8,-2,7,-10,5,-2]],[[-4,1,2,4,-1,-4,6,-4,1,-8,-8,-3,-8]],[[-7,-4,2,-10,3,-6,7,4,8,1,2,-4,2]]], dtype = "int8")#candidate|965|(11, 1, 13)|const|int8
var_966 = relay.var("var_966", dtype = "int8", shape = (11, 11, 13))#candidate|966|(11, 11, 13)|var|int8
bop_967 = relay.logical_xor(const_965.astype('int8'), var_966.astype('int8')) # shape=(11, 11, 13)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_972 = func_928_call()
call_973 = func_928_call()
uop_979 = relay.sqrt(var_966.astype('float32')) # shape=(11, 11, 13)
uop_981 = relay.asinh(uop_979.astype('float32')) # shape=(11, 11, 13)
bop_991 = relay.bitwise_or(uop_981.astype('uint64'), relay.reshape(bop_967.astype('uint64'), relay.shape_of(uop_981))) # shape=(11, 11, 13)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_994 = func_928_call()
call_995 = func_928_call()
output = relay.Tuple([call_972,bop_991,call_994,])
output2 = relay.Tuple([call_973,bop_991,call_995,])
func_998 = relay.Function([var_966,], output)
mod['func_998'] = func_998
mod = relay.transform.InferType()(mod)
mutated_mod['func_998'] = func_998
mutated_mod = relay.transform.InferType()(mutated_mod)
var_999 = relay.var("var_999", dtype = "int8", shape = (11, 11, 13))#candidate|999|(11, 11, 13)|var|int8
func_998_call = mutated_mod.get_global_var('func_998')
call_1000 = func_998_call(var_999)
output = call_1000
func_1001 = relay.Function([var_999], output)
mutated_mod['func_1001'] = func_1001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_1008 = func_928_call()
call_1009 = func_928_call()
func_818_call = mod.get_global_var('func_818')
func_819_call = mutated_mod.get_global_var('func_819')
call_1017 = relay.TupleGetItem(func_818_call(), 0)
call_1018 = relay.TupleGetItem(func_819_call(), 0)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_1027 = func_254_call()
call_1028 = func_254_call()
func_647_call = mod.get_global_var('func_647')
func_650_call = mutated_mod.get_global_var('func_650')
call_1031 = relay.TupleGetItem(func_647_call(relay.reshape(call_1008.astype('float32'), [10, 8, 12])), 0)
call_1032 = relay.TupleGetItem(func_650_call(relay.reshape(call_1008.astype('float32'), [10, 8, 12])), 0)
func_501_call = mod.get_global_var('func_501')
func_504_call = mutated_mod.get_global_var('func_504')
var_1037 = relay.var("var_1037", dtype = "int16", shape = (462,))#candidate|1037|(462,)|var|int16
call_1036 = relay.TupleGetItem(func_501_call(relay.reshape(var_1037.astype('int16'), [462,])), 0)
call_1038 = relay.TupleGetItem(func_504_call(relay.reshape(var_1037.astype('int16'), [462,])), 0)
func_353_call = mod.get_global_var('func_353')
func_354_call = mutated_mod.get_global_var('func_354')
call_1039 = relay.TupleGetItem(func_353_call(), 0)
call_1040 = relay.TupleGetItem(func_354_call(), 0)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_1042 = func_928_call()
call_1043 = func_928_call()
uop_1050 = relay.sin(var_1037.astype('float64')) # shape=(462,)
output = relay.Tuple([call_1008,call_1017,call_1027,call_1031,call_1036,call_1039,call_1042,uop_1050,])
output2 = relay.Tuple([call_1009,call_1018,call_1028,call_1032,call_1038,call_1040,call_1043,uop_1050,])
func_1060 = relay.Function([var_1037,], output)
mod['func_1060'] = func_1060
mod = relay.transform.InferType()(mod)
var_1061 = relay.var("var_1061", dtype = "int16", shape = (462,))#candidate|1061|(462,)|var|int16
output = func_1060(var_1061)
func_1062 = relay.Function([var_1061], output)
mutated_mod['func_1062'] = func_1062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_354_call = mutated_mod.get_global_var('func_354')
call_1071 = relay.TupleGetItem(func_353_call(), 1)
call_1072 = relay.TupleGetItem(func_354_call(), 1)
output = relay.Tuple([call_1071,])
output2 = relay.Tuple([call_1072,])
func_1074 = relay.Function([], output)
mod['func_1074'] = func_1074
mod = relay.transform.InferType()(mod)
mutated_mod['func_1074'] = func_1074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1074_call = mutated_mod.get_global_var('func_1074')
call_1075 = func_1074_call()
output = call_1075
func_1076 = relay.Function([], output)
mutated_mod['func_1076'] = func_1076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1074_call = mod.get_global_var('func_1074')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_1118 = relay.TupleGetItem(func_1074_call(), 0)
call_1119 = relay.TupleGetItem(func_1076_call(), 0)
output = relay.Tuple([call_1118,])
output2 = relay.Tuple([call_1119,])
func_1128 = relay.Function([], output)
mod['func_1128'] = func_1128
mod = relay.transform.InferType()(mod)
output = func_1128()
func_1129 = relay.Function([], output)
mutated_mod['func_1129'] = func_1129
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1140 = relay.var("var_1140", dtype = "float64", shape = (10, 1, 1))#candidate|1140|(10, 1, 1)|var|float64
var_1141 = relay.var("var_1141", dtype = "float64", shape = (10, 2, 1))#candidate|1141|(10, 2, 1)|var|float64
bop_1142 = relay.less_equal(var_1140.astype('bool'), var_1141.astype('bool')) # shape=(10, 2, 1)
bop_1151 = relay.greater(var_1140.astype('bool'), var_1141.astype('bool')) # shape=(10, 2, 1)
uop_1160 = relay.cos(bop_1151.astype('float64')) # shape=(10, 2, 1)
output = relay.Tuple([bop_1142,uop_1160,])
output2 = relay.Tuple([bop_1142,uop_1160,])
func_1168 = relay.Function([var_1140,var_1141,], output)
mod['func_1168'] = func_1168
mod = relay.transform.InferType()(mod)
var_1169 = relay.var("var_1169", dtype = "float64", shape = (10, 1, 1))#candidate|1169|(10, 1, 1)|var|float64
var_1170 = relay.var("var_1170", dtype = "float64", shape = (10, 2, 1))#candidate|1170|(10, 2, 1)|var|float64
output = func_1168(var_1169,var_1170,)
func_1171 = relay.Function([var_1169,var_1170,], output)
mutated_mod['func_1171'] = func_1171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_1235 = func_928_call()
call_1236 = func_928_call()
output = relay.Tuple([call_1235,])
output2 = relay.Tuple([call_1236,])
func_1253 = relay.Function([], output)
mod['func_1253'] = func_1253
mod = relay.transform.InferType()(mod)
mutated_mod['func_1253'] = func_1253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1253_call = mutated_mod.get_global_var('func_1253')
call_1254 = func_1253_call()
output = call_1254
func_1255 = relay.Function([], output)
mutated_mod['func_1255'] = func_1255
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1296 = relay.var("var_1296", dtype = "bool", shape = ())#candidate|1296|()|var|bool
var_1297 = relay.var("var_1297", dtype = "bool", shape = (1, 4, 10))#candidate|1297|(1, 4, 10)|var|bool
bop_1298 = relay.logical_and(var_1296.astype('bool'), var_1297.astype('bool')) # shape=(1, 4, 10)
func_501_call = mod.get_global_var('func_501')
func_504_call = mutated_mod.get_global_var('func_504')
var_1302 = relay.var("var_1302", dtype = "int16", shape = (462,))#candidate|1302|(462,)|var|int16
call_1301 = relay.TupleGetItem(func_501_call(relay.reshape(var_1302.astype('int16'), [462,])), 2)
call_1303 = relay.TupleGetItem(func_504_call(relay.reshape(var_1302.astype('int16'), [462,])), 2)
func_818_call = mod.get_global_var('func_818')
func_819_call = mutated_mod.get_global_var('func_819')
call_1316 = relay.TupleGetItem(func_818_call(), 0)
call_1317 = relay.TupleGetItem(func_819_call(), 0)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_1318 = func_254_call()
call_1319 = func_254_call()
output = relay.Tuple([bop_1298,call_1301,var_1302,call_1316,call_1318,])
output2 = relay.Tuple([bop_1298,call_1303,var_1302,call_1317,call_1319,])
func_1331 = relay.Function([var_1296,var_1297,var_1302,], output)
mod['func_1331'] = func_1331
mod = relay.transform.InferType()(mod)
var_1332 = relay.var("var_1332", dtype = "bool", shape = ())#candidate|1332|()|var|bool
var_1333 = relay.var("var_1333", dtype = "bool", shape = (1, 4, 10))#candidate|1333|(1, 4, 10)|var|bool
var_1334 = relay.var("var_1334", dtype = "int16", shape = (462,))#candidate|1334|(462,)|var|int16
output = func_1331(var_1332,var_1333,var_1334,)
func_1335 = relay.Function([var_1332,var_1333,var_1334,], output)
mutated_mod['func_1335'] = func_1335
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1394 = relay.const([[[6,-2,1,-6,-5,-1,6,-7,-4,-7,-7,-9,-7],[9,9,3,-7,6,-9,5,1,-7,3,3,-5,8],[-3,2,-5,10,-2,-9,10,-8,-8,-10,-1,9,-3],[3,-3,7,-7,6,1,-6,-10,1,-10,6,-4,-8]]], dtype = "uint16")#candidate|1394|(1, 4, 13)|const|uint16
var_1395 = relay.var("var_1395", dtype = "uint16", shape = (7, 4, 13))#candidate|1395|(7, 4, 13)|var|uint16
bop_1396 = relay.right_shift(const_1394.astype('uint16'), var_1395.astype('uint16')) # shape=(7, 4, 13)
func_501_call = mod.get_global_var('func_501')
func_504_call = mutated_mod.get_global_var('func_504')
const_1405 = relay.const([2,7,4,3,-6,-5,-7,5,7,9,-4,8,8,-8,-2,6,4,1,3,-5,-5,8,-5,-7,6,8,8,-1,-1,3,4,9,-5,6,-6,-9,-3,-5,1,-3,-10,6,-8,-4,8,2,9,9,-4,1,8,-1,4,-1,7,-1,-4,5,-6,1,-8,-5,4,10,1,-8,-9,1,-4,-10,6,-8,-8,4,-3,9,8,8,-8,-2,10,-7,8,2,-10,-2,4,9,-4,10,-10,1,-3,-1,-9,-9,2,8,3,1,4,10,-5,4,3,-9,2,-10,10,3,6,-10,7,-6,2,2,1,6,2,-7,3,-8,7,10,-1,9,-7,4,1,-4,9,8,9,-8,-5,6,3,5,-1,-9,7,8,1,8,3,-2,8,-4,6,-8,7,9,5,1,-8,-6,10,-1,-7,-2,10,5,-6,5,-9,2,-6,-9,6,6,-2,-1,8,5,10,8,-3,-8,-1,2,-7,-7,7,1,-8,7,1,4,7,-7,-7,9,-9,1,-1,10,-9,-8,-5,-8,-7,-2,-3,8,-6,-9,1,4,-6,-7,-10,-2,6,-3,-10,-3,-8,-5,-9,-10,-7,9,8,5,-10,10,1,-9,3,-7,7,-2,-3,5,-8,-9,6,3,1,8,10,3,2,-10,6,-10,5,5,8,4,-6,1,10,6,1,5,3,-5,-10,2,10,8,-3,-5,-2,7,3,10,1,7,3,3,1,-3,-3,-8,6,-2,8,9,8,10,3,5,7,6,-5,5,1,9,-2,8,-3,-8,8,1,-3,-5,10,-10,1,6,-9,4,-1,-3,-9,3,-1,-3,8,7,6,8,4,-4,6,-1,-2,-4,-9,8,-7,-2,-5,9,10,7,-10,1,-4,8,-6,6,5,3,-4,2,5,2,-10,3,9,-5,4,-2,2,8,-9,5,4,-8,10,-2,7,-3,8,-6,-4,5,-10,6,-7,1,1,-1,-4,7,-2,-7,4,-5,-5,-9,-1,-9,-3,2,-1,7,-9,-9,1,8,-5,-2,6,1,-6,2,-7,8,-4,-10,-5,9,7,-6,-3,2,1,9,9,9,-4,-5,-10,1,-5,-10,-9,-4,-8,5,-7,1,10,5,2,7,5,-7,4,2,8,-10,3,-3,4,-2,6,-9,3,-6,-10,-3,4,1,-7,-7,-4,-1,-1,-8,2,-10,-3,-5,-4,3,3,-8,-7,4,3,8,10,-4,6,10,2,-8], dtype = "int16")#candidate|1405|(462,)|const|int16
call_1404 = relay.TupleGetItem(func_501_call(relay.reshape(const_1405.astype('int16'), [462,])), 2)
call_1406 = relay.TupleGetItem(func_504_call(relay.reshape(const_1405.astype('int16'), [462,])), 2)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_1407 = func_254_call()
call_1408 = func_254_call()
uop_1424 = relay.log10(call_1407.astype('float32')) # shape=(10, 8, 12)
uop_1426 = relay.log10(call_1408.astype('float32')) # shape=(10, 8, 12)
func_321_call = mod.get_global_var('func_321')
func_324_call = mutated_mod.get_global_var('func_324')
call_1452 = relay.TupleGetItem(func_321_call(relay.reshape(call_1404.astype('float32'), [10, 8, 12])), 2)
call_1453 = relay.TupleGetItem(func_324_call(relay.reshape(call_1404.astype('float32'), [10, 8, 12])), 2)
output = relay.Tuple([bop_1396,call_1404,const_1405,uop_1424,call_1452,])
output2 = relay.Tuple([bop_1396,call_1406,const_1405,uop_1426,call_1453,])
func_1482 = relay.Function([var_1395,], output)
mod['func_1482'] = func_1482
mod = relay.transform.InferType()(mod)
mutated_mod['func_1482'] = func_1482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1483 = relay.var("var_1483", dtype = "uint16", shape = (7, 4, 13))#candidate|1483|(7, 4, 13)|var|uint16
func_1482_call = mutated_mod.get_global_var('func_1482')
call_1484 = func_1482_call(var_1483)
output = call_1484
func_1485 = relay.Function([var_1483], output)
mutated_mod['func_1485'] = func_1485
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1521 = relay.var("var_1521", dtype = "int16", shape = (10, 2, 4))#candidate|1521|(10, 2, 4)|var|int16
var_1522 = relay.var("var_1522", dtype = "int16", shape = (10, 2, 4))#candidate|1522|(10, 2, 4)|var|int16
bop_1523 = relay.bitwise_or(var_1521.astype('int16'), relay.reshape(var_1522.astype('int16'), relay.shape_of(var_1521))) # shape=(10, 2, 4)
uop_1536 = relay.cosh(var_1522.astype('float32')) # shape=(10, 2, 4)
output = relay.Tuple([bop_1523,uop_1536,])
output2 = relay.Tuple([bop_1523,uop_1536,])
func_1546 = relay.Function([var_1521,var_1522,], output)
mod['func_1546'] = func_1546
mod = relay.transform.InferType()(mod)
mutated_mod['func_1546'] = func_1546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1546_call = mutated_mod.get_global_var('func_1546')
var_1548 = relay.var("var_1548", dtype = "int16", shape = (10, 2, 4))#candidate|1548|(10, 2, 4)|var|int16
var_1549 = relay.var("var_1549", dtype = "int16", shape = (10, 2, 4))#candidate|1549|(10, 2, 4)|var|int16
call_1547 = func_1546_call(var_1548,var_1549,)
output = call_1547
func_1550 = relay.Function([var_1548,var_1549,], output)
mutated_mod['func_1550'] = func_1550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_354_call = mutated_mod.get_global_var('func_354')
call_1561 = relay.TupleGetItem(func_353_call(), 1)
call_1562 = relay.TupleGetItem(func_354_call(), 1)
func_321_call = mod.get_global_var('func_321')
func_324_call = mutated_mod.get_global_var('func_324')
call_1565 = relay.TupleGetItem(func_321_call(relay.reshape(call_1561.astype('float32'), [10, 8, 12])), 0)
call_1566 = relay.TupleGetItem(func_324_call(relay.reshape(call_1561.astype('float32'), [10, 8, 12])), 0)
func_774_call = mod.get_global_var('func_774')
func_775_call = mutated_mod.get_global_var('func_775')
call_1567 = relay.TupleGetItem(func_774_call(), 0)
call_1568 = relay.TupleGetItem(func_775_call(), 0)
output = relay.Tuple([call_1561,call_1565,call_1567,])
output2 = relay.Tuple([call_1562,call_1566,call_1568,])
func_1585 = relay.Function([], output)
mod['func_1585'] = func_1585
mod = relay.transform.InferType()(mod)
output = func_1585()
func_1586 = relay.Function([], output)
mutated_mod['func_1586'] = func_1586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_1599 = func_254_call()
call_1600 = func_254_call()
output = relay.Tuple([call_1599,])
output2 = relay.Tuple([call_1600,])
func_1619 = relay.Function([], output)
mod['func_1619'] = func_1619
mod = relay.transform.InferType()(mod)
output = func_1619()
func_1620 = relay.Function([], output)
mutated_mod['func_1620'] = func_1620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_385_call = mod.get_global_var('func_385')
func_386_call = mutated_mod.get_global_var('func_386')
call_1634 = func_385_call()
call_1635 = func_385_call()
output = call_1634
output2 = call_1635
func_1638 = relay.Function([], output)
mod['func_1638'] = func_1638
mod = relay.transform.InferType()(mod)
mutated_mod['func_1638'] = func_1638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1638_call = mutated_mod.get_global_var('func_1638')
call_1639 = func_1638_call()
output = call_1639
func_1640 = relay.Function([], output)
mutated_mod['func_1640'] = func_1640
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1682 = relay.var("var_1682", dtype = "uint32", shape = (13, 7, 11))#candidate|1682|(13, 7, 11)|var|uint32
var_1683 = relay.var("var_1683", dtype = "uint32", shape = (13, 7, 11))#candidate|1683|(13, 7, 11)|var|uint32
bop_1684 = relay.left_shift(var_1682.astype('uint32'), relay.reshape(var_1683.astype('uint32'), relay.shape_of(var_1682))) # shape=(13, 7, 11)
func_859_call = mod.get_global_var('func_859')
func_861_call = mutated_mod.get_global_var('func_861')
call_1698 = relay.TupleGetItem(func_859_call(), 1)
call_1699 = relay.TupleGetItem(func_861_call(), 1)
output = relay.Tuple([bop_1684,call_1698,])
output2 = relay.Tuple([bop_1684,call_1699,])
func_1709 = relay.Function([var_1682,var_1683,], output)
mod['func_1709'] = func_1709
mod = relay.transform.InferType()(mod)
var_1710 = relay.var("var_1710", dtype = "uint32", shape = (13, 7, 11))#candidate|1710|(13, 7, 11)|var|uint32
var_1711 = relay.var("var_1711", dtype = "uint32", shape = (13, 7, 11))#candidate|1711|(13, 7, 11)|var|uint32
output = func_1709(var_1710,var_1711,)
func_1712 = relay.Function([var_1710,var_1711,], output)
mutated_mod['func_1712'] = func_1712
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1847 = relay.var("var_1847", dtype = "float64", shape = (2, 16))#candidate|1847|(2, 16)|var|float64
uop_1848 = relay.rsqrt(var_1847.astype('float64')) # shape=(2, 16)
func_1253_call = mod.get_global_var('func_1253')
func_1255_call = mutated_mod.get_global_var('func_1255')
call_1858 = relay.TupleGetItem(func_1253_call(), 0)
call_1859 = relay.TupleGetItem(func_1255_call(), 0)
output = relay.Tuple([uop_1848,call_1858,])
output2 = relay.Tuple([uop_1848,call_1859,])
func_1862 = relay.Function([var_1847,], output)
mod['func_1862'] = func_1862
mod = relay.transform.InferType()(mod)
var_1863 = relay.var("var_1863", dtype = "float64", shape = (2, 16))#candidate|1863|(2, 16)|var|float64
output = func_1862(var_1863)
func_1864 = relay.Function([var_1863], output)
mutated_mod['func_1864'] = func_1864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_1901 = func_1638_call()
call_1902 = func_1638_call()
func_818_call = mod.get_global_var('func_818')
func_819_call = mutated_mod.get_global_var('func_819')
call_1908 = relay.TupleGetItem(func_818_call(), 0)
call_1909 = relay.TupleGetItem(func_819_call(), 0)
output = relay.Tuple([call_1901,call_1908,])
output2 = relay.Tuple([call_1902,call_1909,])
func_1917 = relay.Function([], output)
mod['func_1917'] = func_1917
mod = relay.transform.InferType()(mod)
mutated_mod['func_1917'] = func_1917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1917_call = mutated_mod.get_global_var('func_1917')
call_1918 = func_1917_call()
output = call_1918
func_1919 = relay.Function([], output)
mutated_mod['func_1919'] = func_1919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_353_call = mod.get_global_var('func_353')
func_354_call = mutated_mod.get_global_var('func_354')
call_1973 = relay.TupleGetItem(func_353_call(), 0)
call_1974 = relay.TupleGetItem(func_354_call(), 0)
output = call_1973
output2 = call_1974
func_1982 = relay.Function([], output)
mod['func_1982'] = func_1982
mod = relay.transform.InferType()(mod)
mutated_mod['func_1982'] = func_1982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1982_call = mutated_mod.get_global_var('func_1982')
call_1983 = func_1982_call()
output = call_1983
func_1984 = relay.Function([], output)
mutated_mod['func_1984'] = func_1984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_385_call = mod.get_global_var('func_385')
func_386_call = mutated_mod.get_global_var('func_386')
call_2016 = func_385_call()
call_2017 = func_385_call()
output = call_2016
output2 = call_2017
func_2030 = relay.Function([], output)
mod['func_2030'] = func_2030
mod = relay.transform.InferType()(mod)
mutated_mod['func_2030'] = func_2030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mutated_mod.get_global_var('func_2030')
call_2031 = func_2030_call()
output = call_2031
func_2032 = relay.Function([], output)
mutated_mod['func_2032'] = func_2032
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2044 = relay.var("var_2044", dtype = "uint64", shape = ())#candidate|2044|()|var|uint64
var_2045 = relay.var("var_2045", dtype = "uint64", shape = (11, 5, 5))#candidate|2045|(11, 5, 5)|var|uint64
bop_2046 = relay.bitwise_xor(var_2044.astype('uint64'), var_2045.astype('uint64')) # shape=(11, 5, 5)
uop_2050 = relay.asin(bop_2046.astype('float64')) # shape=(11, 5, 5)
bop_2061 = relay.bitwise_or(uop_2050.astype('int64'), relay.reshape(bop_2046.astype('int64'), relay.shape_of(uop_2050))) # shape=(11, 5, 5)
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
var_2071 = relay.var("var_2071", dtype = "int16", shape = (462,))#candidate|2071|(462,)|var|int16
call_2070 = relay.TupleGetItem(func_107_call(relay.reshape(var_2071.astype('int16'), [11, 6, 7]), relay.reshape(var_2071.astype('int16'), [11, 6, 7]), ), 0)
call_2072 = relay.TupleGetItem(func_111_call(relay.reshape(var_2071.astype('int16'), [11, 6, 7]), relay.reshape(var_2071.astype('int16'), [11, 6, 7]), ), 0)
output = relay.Tuple([bop_2061,call_2070,var_2071,])
output2 = relay.Tuple([bop_2061,call_2072,var_2071,])
func_2082 = relay.Function([var_2044,var_2045,var_2071,], output)
mod['func_2082'] = func_2082
mod = relay.transform.InferType()(mod)
var_2083 = relay.var("var_2083", dtype = "uint64", shape = ())#candidate|2083|()|var|uint64
var_2084 = relay.var("var_2084", dtype = "uint64", shape = (11, 5, 5))#candidate|2084|(11, 5, 5)|var|uint64
var_2085 = relay.var("var_2085", dtype = "int16", shape = (462,))#candidate|2085|(462,)|var|int16
output = func_2082(var_2083,var_2084,var_2085,)
func_2086 = relay.Function([var_2083,var_2084,var_2085,], output)
mutated_mod['func_2086'] = func_2086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1917_call = mod.get_global_var('func_1917')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_2094 = relay.TupleGetItem(func_1917_call(), 0)
call_2095 = relay.TupleGetItem(func_1919_call(), 0)
output = call_2094
output2 = call_2095
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
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_2107 = func_1638_call()
call_2108 = func_1638_call()
func_1546_call = mod.get_global_var('func_1546')
func_1550_call = mutated_mod.get_global_var('func_1550')
const_2110 = relay.const([5,6,-9,6,8,-3,1,6,7,8,9,7,9,-5,5,-3,-3,-2,3,-2,-7,-6,6,-10,-2,-10,10,-10,-7,6,-4,-2,8,-9,-2,-4,5,-9,5,-5,8,7,-5,9,-3,-3,1,-4,-9,-10,6,-2,-7,2,-2,9,4,-10,-3,10,1,3,-9,1,-1,-1,-8,-8,5,8,-8,-9,-3,1,7,1,3,10,-2,9], dtype = "int16")#candidate|2110|(80,)|const|int16
call_2109 = relay.TupleGetItem(func_1546_call(relay.reshape(const_2110.astype('int16'), [10, 2, 4]), relay.reshape(const_2110.astype('int16'), [10, 2, 4]), ), 0)
call_2111 = relay.TupleGetItem(func_1550_call(relay.reshape(const_2110.astype('int16'), [10, 2, 4]), relay.reshape(const_2110.astype('int16'), [10, 2, 4]), ), 0)
output = relay.Tuple([call_2107,call_2109,const_2110,])
output2 = relay.Tuple([call_2108,call_2111,const_2110,])
func_2118 = relay.Function([], output)
mod['func_2118'] = func_2118
mod = relay.transform.InferType()(mod)
mutated_mod['func_2118'] = func_2118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2118_call = mutated_mod.get_global_var('func_2118')
call_2119 = func_2118_call()
output = call_2119
func_2120 = relay.Function([], output)
mutated_mod['func_2120'] = func_2120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_698_call = mod.get_global_var('func_698')
func_700_call = mutated_mod.get_global_var('func_700')
call_2189 = relay.TupleGetItem(func_698_call(), 0)
call_2190 = relay.TupleGetItem(func_700_call(), 0)
func_774_call = mod.get_global_var('func_774')
func_775_call = mutated_mod.get_global_var('func_775')
call_2194 = relay.TupleGetItem(func_774_call(), 0)
call_2195 = relay.TupleGetItem(func_775_call(), 0)
func_998_call = mod.get_global_var('func_998')
func_1001_call = mutated_mod.get_global_var('func_1001')
var_2210 = relay.var("var_2210", dtype = "int8", shape = (1573,))#candidate|2210|(1573,)|var|int8
call_2209 = relay.TupleGetItem(func_998_call(relay.reshape(var_2210.astype('int8'), [11, 11, 13])), 2)
call_2211 = relay.TupleGetItem(func_1001_call(relay.reshape(var_2210.astype('int8'), [11, 11, 13])), 2)
output = relay.Tuple([call_2189,call_2194,call_2209,var_2210,])
output2 = relay.Tuple([call_2190,call_2195,call_2211,var_2210,])
func_2230 = relay.Function([var_2210,], output)
mod['func_2230'] = func_2230
mod = relay.transform.InferType()(mod)
mutated_mod['func_2230'] = func_2230
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2231 = relay.var("var_2231", dtype = "int8", shape = (1573,))#candidate|2231|(1573,)|var|int8
func_2230_call = mutated_mod.get_global_var('func_2230')
call_2232 = func_2230_call(var_2231)
output = call_2232
func_2233 = relay.Function([var_2231], output)
mutated_mod['func_2233'] = func_2233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2099_call = mod.get_global_var('func_2099')
func_2101_call = mutated_mod.get_global_var('func_2101')
call_2281 = func_2099_call()
call_2282 = func_2099_call()
func_2230_call = mod.get_global_var('func_2230')
func_2233_call = mutated_mod.get_global_var('func_2233')
const_2296 = relay.const([[-7],[2],[-3],[-1],[1],[-2],[-3],[2],[5],[1],[-9],[-7],[-7],[2],[-6],[-8],[1],[8],[5],[2],[1],[6],[6],[-1],[-9],[-8],[-3],[5],[-7],[3],[-3],[6],[-1],[5],[-2],[-3],[-2],[-9],[6],[1],[4],[-6],[-4],[1],[9],[-5],[-3],[4],[5],[-3],[10],[-2],[-4],[1],[2],[-9],[-3],[3],[7],[-1],[8],[-9],[-8],[8],[-4],[-4],[6],[7],[8],[-1],[-3],[-5],[7],[-6],[-6],[3],[6],[6],[4],[-9],[4],[5],[9],[9],[1],[8],[-2],[10],[4],[4],[-6],[3],[-8],[4],[-2],[4],[-8],[5],[2],[-7],[-4],[7],[-9],[-3],[-7],[-5],[5],[-3],[-7],[-7],[-3],[7],[2],[9],[4],[7],[10],[-3],[-4],[-5],[5],[-4],[-8],[-5],[5],[3],[3],[-9],[2],[8],[-1],[-5],[10],[-3],[-6],[3],[-6],[4],[-5],[8],[1],[10],[-3],[-8],[5],[2],[-1],[-1],[7],[-5],[-10],[-6],[7],[-10],[-9],[2],[10],[-3],[-9],[8],[8],[-3],[7],[10],[-6],[6],[-5],[-2],[-2],[-5],[-1],[-2],[-9],[5],[-7],[5],[5],[6],[10],[7],[-3],[9],[5],[2],[-6],[-10],[-6],[-7],[7],[-4],[-7],[2],[6],[3],[4],[-9],[-2],[4],[-4],[5],[-3],[-4],[-7],[-5],[-4],[-1],[-9],[2],[-8],[1],[-6],[-6],[-3],[-6],[-9],[4],[7],[-3],[2],[9],[9],[7],[-10],[3],[-6],[10],[7],[10],[8],[-4],[8],[1],[7],[-10],[-3],[4],[-8],[10],[-4],[5],[-9],[1],[3],[-3],[-9],[8],[-6],[-3],[-4],[-3],[1],[-9],[-10],[6],[-3],[-3],[-8],[-6],[10],[-1],[-8],[-6],[-9],[-9],[-9],[8],[-10],[6],[7],[6],[-5],[-2],[-7],[-3],[10],[6],[3],[2],[9],[3],[-4],[10],[9],[5],[-10],[-5],[4],[-7],[6],[8],[3],[3],[5],[8],[-9],[-4],[3],[8],[-9],[-9],[8],[3],[1],[-2],[9],[-2],[1],[-6],[5],[10],[4],[-8],[7],[-2],[-2],[5],[-5],[9],[8],[3],[-1],[-8],[2],[-1],[-10],[10],[7],[5],[-7],[10],[8],[-7],[-4],[10],[-10],[-7],[-10],[5],[3],[-1],[-7],[8],[-3],[9],[10],[7],[-5],[-2],[5],[-8],[7],[-7],[-2],[-2],[-8],[-7],[6],[-2],[8],[8],[9],[7],[-4],[-2],[1],[5],[7],[8],[6],[-4],[3],[-3],[9],[-9],[-5],[9],[2],[9],[-5],[4],[-2],[5],[-3],[-1],[-2],[-3],[-8],[-7],[10],[-8],[-1],[-2],[-2],[-1],[-3],[-2],[-4],[-6],[-1],[3],[-2],[2],[3],[-9],[-3],[1],[-3],[-9],[3],[2],[4],[2],[-3],[4],[5],[-1],[6],[-9],[3],[3],[6],[-4],[-6],[-5],[-4],[6],[1],[6],[6],[9],[-9],[-2],[-6],[-3],[10],[6],[1],[-6],[2],[7],[-8],[-4],[1],[-2],[1],[-2],[-4],[3],[-5],[8],[4],[3],[4],[2],[1],[-2],[2],[-8],[7],[2],[3],[-6],[6],[6],[6],[7],[10],[5],[9],[9],[-9],[-1],[-10],[-6],[10],[3],[-1],[2],[-10],[1],[4],[8],[-7],[-7],[-2],[-8],[-1],[2],[9],[6],[-7],[5],[-2],[7],[7],[8],[7],[-5],[-8],[-3],[-1],[1],[-2],[-1],[2],[-2],[-10],[7],[6],[-2],[4],[-6],[7],[-7],[4],[-5],[-3],[-4],[9],[7],[5],[-10],[-8],[7],[-3],[-9],[-10],[-9],[-6],[1],[-6],[-6],[-3],[5],[-8],[-5],[10],[9],[6],[-2],[-8],[5],[-7],[6],[1],[-5],[6],[-8],[-2],[2],[3],[-6],[-7],[-3],[-3],[-2],[-5],[9],[-3],[5],[-4],[3],[-2],[8],[-5],[-7],[-10],[-3],[7],[9],[-10],[-3],[8],[-9],[8],[-7],[6],[10],[-2],[-3],[9],[-5],[-2],[7],[4],[-1],[5],[-1],[7],[5],[4],[8],[1],[-8],[-8],[-8],[-3],[-7],[3],[4],[10],[-2],[-9],[-9],[3],[-4],[4],[-6],[9],[8],[7],[6],[10],[2],[-9],[-1],[-2],[-3],[7],[9],[-4],[4],[-4],[4],[6],[-3],[-7],[2],[-4],[1],[3],[-2],[6],[-9],[-5],[-1],[-3],[10],[-7],[3],[4],[8],[-6],[-9],[9],[6],[3],[-10],[-1],[-1],[7],[-9],[1],[8],[-2],[3],[8],[9],[6],[-6],[9],[6],[10],[-2],[4],[1],[-9],[4],[10],[10],[-4],[9],[-6],[7],[8],[6],[7],[-1],[9],[10],[-1],[7],[-3],[-2],[2],[6],[4],[-7],[6],[2],[-9],[-3],[-2],[5],[-2],[-5],[8],[-4],[10],[4],[5],[7],[5],[-10],[7],[-7],[2],[-5],[6],[4],[-7],[-2],[-10],[5],[-2],[3],[1],[9],[-3],[9],[2],[-8],[-7],[9],[-3],[3],[3],[-4],[-2],[4],[-10],[-3],[6],[-8],[-2],[-10],[-2],[1],[1],[3],[4],[-3],[-1],[-9],[-6],[1],[9],[-8],[8],[5],[-3],[-6],[-3],[-4],[-8],[8],[5],[8],[-8],[3],[1],[1],[-7],[-8],[-7],[5],[-8],[-6],[-8],[5],[9],[8],[7],[-2],[-5],[9],[6],[-10],[1],[6],[-9],[-7],[-1],[-7],[-3],[-7],[-8],[-6],[2],[-7],[10],[5],[-8],[-9],[-10],[-6],[-7],[7],[-3],[-1],[7],[-1],[-2],[9],[5],[-3],[4],[3],[2],[10],[8],[-3],[8],[-4],[-6],[-9],[2],[9],[7],[10],[-6],[6],[-10],[5],[-10],[5],[10],[2],[-10],[10],[3],[9],[1],[1],[-6],[9],[3],[-5],[4],[-6],[6],[2],[-9],[-5],[-3],[5],[8],[1],[-9],[-7],[-5],[-10],[-2],[5],[6],[10],[-1],[7],[7],[1],[9],[-5],[-7],[6],[1],[5],[-10],[8],[2],[7],[3],[2],[-10],[-5],[1],[6],[-1],[8],[-9],[6],[-6],[10],[7],[-7],[1],[9],[-1],[-9],[-9],[9],[-2],[1],[8],[-1],[-4],[9],[-9],[-5],[6],[5],[5],[-1],[-6],[9],[-5],[-7],[-3],[-10],[10],[8],[-10],[3],[3],[-6],[-1],[6],[5],[-6],[8],[-6],[4],[-9],[2],[8],[3],[-5],[2],[-2],[9],[5],[9],[7],[9],[-6],[-9],[-9],[6],[1],[-9],[1],[6],[7],[-7],[2],[7],[5],[9],[1],[-7],[2],[-1],[-2],[8],[6],[-4],[-1],[6],[-8],[-7],[6],[-8],[-1],[7],[6],[10],[4],[8],[8],[-9],[5],[-3],[4],[4],[-2],[-2],[6],[-1],[10],[2],[-4],[3],[-2],[3],[-9],[6],[8],[2],[-9],[-5],[7],[1],[-1],[4],[-2],[5],[-9],[-5],[-9],[2],[-3],[-4],[8],[-6],[-2],[7],[-10],[5],[-1],[-3],[7],[1],[8],[6],[-4],[-7],[-7],[-9],[-7],[-1],[6],[8],[-8],[-9],[4],[-4],[-2],[7],[-2],[-7],[-1],[3],[-3],[2],[-9],[-9],[-3],[-1],[2],[2],[2],[6],[-4],[3],[-6],[-10],[3],[3],[-8],[-8],[-10],[-2],[-3],[-5],[-4],[10],[-4],[1],[-1],[-2],[5],[4],[-7],[-5],[-1],[-4],[1],[-3],[-2],[9],[5],[4],[-10],[-7],[-9],[8],[3],[1],[-8],[-9],[-1],[-2],[-10],[9],[3],[-7],[-9],[-10],[-6],[-10],[10],[-9],[9],[-4],[-8],[5],[-7],[-4],[-2],[-10],[10],[5],[-10],[10],[6],[3],[7],[8],[3],[2],[7],[1],[-2],[3],[-7],[-1],[4],[-8],[-3],[-2],[-10],[4],[8],[5],[3],[3],[3],[-6],[-10],[-3],[3],[5],[9],[2],[6],[2],[1],[-5],[-5],[-2],[-6],[-10],[10],[7],[4],[8],[3],[-3],[-1],[-6],[-10],[-2],[2],[10],[8],[8],[9],[-4],[-4],[1],[-1],[3],[6],[-6],[-10],[-3],[9],[-1],[-5],[-2],[5],[6],[8],[4],[-2],[-7],[-6],[5],[-8],[-9],[3],[9],[9],[5],[-3],[6],[7],[-3],[-3],[6],[-2],[8],[-5],[7],[4],[-2],[-8],[-1],[2],[-1],[-4],[-6],[-9],[7],[-4],[7],[10],[-3],[8],[8],[6],[9],[2],[-2],[-7],[-3],[8],[-4],[-6],[10],[6],[7],[1],[-2],[-10],[3],[10],[-1],[-3],[1],[6],[2],[3],[2],[7],[-1],[-9],[10],[8],[1],[10],[-5],[5],[7],[9],[-9],[-1],[-10],[5],[4],[-3],[-6],[5],[4],[-7],[1],[-8],[-10],[-4],[-2],[-6],[-9],[-10],[-1],[-10],[8],[10],[-6],[9],[8],[5],[-3],[-8],[6],[1],[-7],[9],[-4],[-7],[-5],[-10],[8],[8],[-4],[-6],[-2],[4],[3],[-10],[5],[9],[10],[2],[-10],[-7],[-3],[9],[-6],[7],[-5],[-4],[3],[-2],[-1],[-7],[8],[10],[5],[-10],[-8],[1],[5],[-5],[6],[-4],[-7],[8],[6],[6],[4],[6],[1],[-10],[8],[3],[-10],[-1],[2],[-7],[-10],[-1],[-9],[6],[-9],[-5],[-8],[-7],[-6],[7],[-8],[4],[-5],[-2],[-1],[-7],[-1],[-7],[-7],[8],[-7],[-1],[5],[-6],[-6],[7],[-5],[1],[-5],[7],[3],[4],[-4],[8],[4],[-9],[10],[-6],[9],[-6],[-6],[8],[-1],[1],[3],[2],[4],[2],[9],[-1],[-6],[3],[-10],[1],[-2],[-4],[-9],[10],[-3],[-7],[-9],[-2],[5],[2],[6],[6],[-4],[9],[10],[3],[6],[-10],[2],[-4],[1],[9],[10],[-6],[7],[-10],[3],[-4],[7],[-9],[3],[8],[-9],[-6],[-8],[-6],[-4],[2],[8],[1],[-6],[-8],[-9],[6],[-6],[-4],[8],[2],[-2],[-10],[1],[-1],[1],[-8],[-1],[-2],[-4],[-8],[5],[-10],[10],[3],[7],[5],[4],[-2],[-1],[1],[-8],[9],[-10],[10],[5],[6],[1],[-10],[1],[9],[9],[-9],[-1],[-9],[4],[2],[-8],[3],[6],[-3],[-1],[-1],[-6],[-5],[4],[-5],[10],[-7],[5],[-3],[3],[2],[10],[1],[-9],[9],[3],[4],[10],[-6],[-7],[-7],[-7],[10],[-10],[10],[10],[-7],[9],[6],[-2],[8],[2],[-7],[-5],[-7],[6],[-1],[-8],[-4],[4],[2],[-7],[-2],[-6],[-4],[3],[6],[-8],[-8],[-3],[-5],[-10],[-1],[-7],[-7],[-2],[3],[-7],[-6],[3],[-3],[-4],[4],[9],[-6],[8],[5],[-8],[-8],[-3],[6],[-3],[5],[-3],[-5],[4],[5],[-7],[1],[10],[2],[9],[-7],[4],[-1],[-10],[4],[-5],[-5],[1],[5],[10],[-5],[-6],[4],[-2],[-7],[4],[7],[9],[6],[-7]], dtype = "int8")#candidate|2296|(1573, 1)|const|int8
call_2295 = relay.TupleGetItem(func_2230_call(relay.reshape(const_2296.astype('int8'), [1573,])), 1)
call_2297 = relay.TupleGetItem(func_2233_call(relay.reshape(const_2296.astype('int8'), [1573,])), 1)
func_698_call = mod.get_global_var('func_698')
func_700_call = mutated_mod.get_global_var('func_700')
call_2305 = relay.TupleGetItem(func_698_call(), 1)
call_2306 = relay.TupleGetItem(func_700_call(), 1)
func_2230_call = mod.get_global_var('func_2230')
func_2233_call = mutated_mod.get_global_var('func_2233')
call_2309 = relay.TupleGetItem(func_2230_call(relay.reshape(const_2296.astype('int8'), [1573,])), 2)
call_2310 = relay.TupleGetItem(func_2233_call(relay.reshape(const_2296.astype('int8'), [1573,])), 2)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_2312 = func_254_call()
call_2313 = func_254_call()
output = relay.Tuple([call_2281,call_2295,const_2296,call_2305,call_2309,call_2312,])
output2 = relay.Tuple([call_2282,call_2297,const_2296,call_2306,call_2310,call_2313,])
func_2316 = relay.Function([], output)
mod['func_2316'] = func_2316
mod = relay.transform.InferType()(mod)
mutated_mod['func_2316'] = func_2316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2316_call = mutated_mod.get_global_var('func_2316')
call_2317 = func_2316_call()
output = call_2317
func_2318 = relay.Function([], output)
mutated_mod['func_2318'] = func_2318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2316_call = mod.get_global_var('func_2316')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_2319 = relay.TupleGetItem(func_2316_call(), 5)
call_2320 = relay.TupleGetItem(func_2318_call(), 5)
uop_2331 = relay.tan(call_2319.astype('float64')) # shape=(10, 8, 12)
uop_2333 = relay.tan(call_2320.astype('float64')) # shape=(10, 8, 12)
output = relay.Tuple([uop_2331,])
output2 = relay.Tuple([uop_2333,])
func_2341 = relay.Function([], output)
mod['func_2341'] = func_2341
mod = relay.transform.InferType()(mod)
output = func_2341()
func_2342 = relay.Function([], output)
mutated_mod['func_2342'] = func_2342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_698_call = mod.get_global_var('func_698')
func_700_call = mutated_mod.get_global_var('func_700')
call_2389 = relay.TupleGetItem(func_698_call(), 2)
call_2390 = relay.TupleGetItem(func_700_call(), 2)
func_1546_call = mod.get_global_var('func_1546')
func_1550_call = mutated_mod.get_global_var('func_1550')
var_2395 = relay.var("var_2395", dtype = "int16", shape = (40, 2))#candidate|2395|(40, 2)|var|int16
call_2394 = relay.TupleGetItem(func_1546_call(relay.reshape(var_2395.astype('int16'), [10, 2, 4]), relay.reshape(var_2395.astype('int16'), [10, 2, 4]), ), 1)
call_2396 = relay.TupleGetItem(func_1550_call(relay.reshape(var_2395.astype('int16'), [10, 2, 4]), relay.reshape(var_2395.astype('int16'), [10, 2, 4]), ), 1)
uop_2402 = relay.atanh(var_2395.astype('float64')) # shape=(40, 2)
output = relay.Tuple([call_2389,call_2394,uop_2402,])
output2 = relay.Tuple([call_2390,call_2396,uop_2402,])
func_2416 = relay.Function([var_2395,], output)
mod['func_2416'] = func_2416
mod = relay.transform.InferType()(mod)
var_2417 = relay.var("var_2417", dtype = "int16", shape = (40, 2))#candidate|2417|(40, 2)|var|int16
output = func_2416(var_2417)
func_2418 = relay.Function([var_2417], output)
mutated_mod['func_2418'] = func_2418
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2423 = relay.const([[[True,False,True,False,False,True,True],[False,True,True,True,False,True,False],[True,False,True,True,False,False,False],[True,False,True,True,True,True,True],[False,True,True,True,True,False,True],[False,False,False,False,True,True,False],[True,False,False,True,False,False,False],[False,False,False,False,True,True,True],[False,False,False,False,False,False,True],[True,False,False,True,False,False,False],[False,True,False,True,True,False,False],[True,False,False,False,True,False,False],[False,False,True,False,False,True,True]]], dtype = "bool")#candidate|2423|(1, 13, 7)|const|bool
var_2424 = relay.var("var_2424", dtype = "bool", shape = (13, 13, 7))#candidate|2424|(13, 13, 7)|var|bool
bop_2425 = relay.logical_or(const_2423.astype('bool'), var_2424.astype('bool')) # shape=(13, 13, 7)
func_1585_call = mod.get_global_var('func_1585')
func_1586_call = mutated_mod.get_global_var('func_1586')
call_2437 = relay.TupleGetItem(func_1585_call(), 1)
call_2438 = relay.TupleGetItem(func_1586_call(), 1)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_2441 = relay.TupleGetItem(func_1128_call(), 0)
call_2442 = relay.TupleGetItem(func_1129_call(), 0)
func_2230_call = mod.get_global_var('func_2230')
func_2233_call = mutated_mod.get_global_var('func_2233')
const_2464 = relay.const([1,9,8,-8,-5,4,-1,5,4,-1,-10,1,5,-5,10,-10,-6,10,-10,-2,-3,2,7,-7,-1,-9,-5,8,6,6,3,-6,-4,7,-7,9,-5,5,6,-4,10,-2,6,7,-5,-7,-7,-1,9,5,9,7,4,-8,4,1,-7,-9,3,2,-6,-8,4,-6,-7,1,6,2,2,2,1,-9,6,-1,3,5,-4,4,4,1,4,9,-3,-2,10,2,9,2,-9,-2,-6,-4,2,10,-2,7,-6,6,7,4,-5,-1,-8,-10,7,1,-1,-6,7,-10,1,-2,6,-6,-9,-2,-7,-9,-7,-3,-2,-8,3,7,1,6,-5,-9,-8,5,5,2,-2,6,9,-6,8,-6,-9,9,-10,-4,-5,7,-7,-1,-2,2,-5,7,-10,6,6,-8,-3,-9,-6,-10,-5,4,-9,-2,-9,7,5,-7,7,-4,5,10,-3,-1,-1,7,7,-5,10,9,4,-5,-10,-5,-6,-9,-4,-9,7,5,-10,-3,-6,5,-6,7,-8,10,-5,-4,5,-1,6,6,-1,-1,-3,-10,-3,-7,9,2,4,-7,6,-9,-7,-1,-2,8,10,-6,6,-4,-3,9,-4,-7,-2,9,-8,-2,-1,-9,2,8,-7,-4,10,-1,10,-3,2,3,8,3,-10,-10,9,-6,7,4,-8,-4,-10,-1,6,5,8,1,9,2,2,-2,3,4,2,3,-10,-8,3,-1,7,-6,-3,1,-2,3,6,5,-5,-9,-10,-5,-9,-1,4,1,7,6,-4,-9,-1,10,-10,-7,7,2,-8,8,-9,10,-2,-5,-10,-6,-10,-1,-9,-10,-8,-6,3,-2,4,-8,8,8,-1,-8,6,5,9,8,-9,-1,-7,1,2,1,-1,10,-7,1,3,-8,3,6,-9,2,-5,4,9,-4,-7,8,5,1,-6,1,2,-10,-5,7,-3,2,3,1,-1,4,1,-10,-9,8,1,-5,-1,8,-1,9,-5,1,-1,9,-9,-2,4,-7,-2,8,-6,-8,10,-4,10,-5,8,-2,-10,1,-3,-2,-4,10,5,1,1,-10,-5,3,10,10,-6,5,3,-9,-8,5,-9,-9,-1,6,10,-6,-10,10,-7,-8,-5,2,6,8,2,7,6,-6,4,10,7,9,-5,9,-3,8,7,-8,1,8,-7,5,-1,-2,-2,-9,10,-8,10,8,4,3,-6,-6,-7,2,-1,9,7,-7,6,10,7,-3,-5,2,7,-1,-6,-9,5,-9,8,8,-1,-6,10,-7,6,-6,8,-10,-1,7,-2,-10,-8,3,9,1,6,-1,5,-5,-5,-10,7,10,-5,-5,5,-1,-6,-9,6,9,9,-10,7,3,-6,-6,5,3,7,4,-5,5,1,-10,-5,-1,-8,-7,8,-6,-3,1,2,-7,-4,-1,9,-2,-9,9,1,6,-3,-4,-3,9,-5,-3,2,4,-2,-5,-10,-1,-1,-2,-2,-2,3,8,-6,-1,5,6,5,-5,4,10,-9,2,3,2,2,10,10,1,-3,5,-8,7,-10,2,4,-7,-5,5,-2,-5,1,-10,-3,6,-5,6,-3,-9,-7,8,-5,6,-3,1,-8,-10,2,-1,-2,1,-10,-3,1,-8,4,-2,3,10,9,-1,-6,7,2,-2,-6,6,-1,-1,-2,3,-8,-3,-2,-9,4,9,3,-7,5,3,-2,7,9,-6,-10,-5,5,-9,2,-10,-8,-6,5,9,-1,-9,-1,-8,8,-1,4,-9,5,6,8,4,2,-8,-1,7,9,-7,-6,-1,1,-5,6,-2,1,-10,3,-4,2,-2,-1,7,6,-8,-10,-7,1,-4,5,9,5,7,-1,-10,7,8,-2,-5,10,9,4,-1,-9,1,-2,-1,8,-4,3,4,8,5,8,8,-5,7,4,-2,2,6,2,8,9,2,6,9,9,-5,6,-4,10,-8,-7,7,4,3,5,7,-5,-6,-7,6,1,-3,-3,-7,10,7,-6,7,10,-5,3,-10,2,-9,1,5,7,8,-6,-4,10,4,-8,7,2,4,7,4,-10,-8,-10,-2,2,-6,-6,-5,-2,4,1,-9,-5,-2,6,2,1,-6,3,-8,7,3,6,10,8,-9,7,-4,2,-5,-4,-4,-6,-5,-8,4,-1,-9,-7,-7,4,4,8,4,-5,-8,-7,-3,-3,-2,5,6,-4,-3,7,6,9,-3,-9,5,-7,5,5,6,8,9,-7,9,2,-4,3,-10,-1,9,3,6,-9,5,8,-2,-1,-10,-5,-2,1,8,4,-8,3,5,-3,6,-3,-4,4,9,-6,-6,8,-10,1,-4,-5,2,-2,-4,9,5,-2,-4,6,4,2,2,5,2,-1,-3,-1,-4,3,5,1,3,-10,2,10,-7,3,4,-3,-5,3,1,-2,-6,-7,6,-3,-3,-6,1,8,-8,-9,-10,9,7,1,7,-6,-8,-5,3,3,-3,9,-7,-1,-10,9,3,3,-1,1,-10,2,2,-4,7,8,-8,-5,-4,10,-7,1,-9,1,3,-8,10,2,-7,-4,-4,6,9,-7,-8,-6,7,4,-4,-6,8,1,-5,-10,1,-1,-4,9,6,6,-4,-8,2,9,-10,4,-2,-8,9,-3,1,7,9,-1,-3,-1,-9,-10,-3,-8,5,-3,-6,5,-10,-8,-10,-6,-3,8,-4,-5,-7,6,5,7,4,8,-2,7,-1,10,-10,-4,5,-10,-8,4,9,9,1,-7,-5,-9,10,-8,-1,-6,-9,3,-2,-3,-8,-10,-4,-5,5,4,-9,-9,-6,-1,9,7,10,2,-5,-2,9,-1,1,1,-8,-9,5,5,7,10,5,-6,9,5,-2,-8,1,7,3,-9,1,5,6,-1,6,-2,9,4,-5,-4,9,1,1,-1,6,-5,-8,4,2,10,7,9,-10,-5,-5,4,-3,2,-3,-8,5,-7,-6,8,6,-6,-9,-8,1,4,2,-9,-4,-9,-4,-7,2,1,-5,-8,8,-4,10,-4,3,8,-9,-2,-6,2,-10,10,-5,2,3,-10,3,-5,-6,-5,-10,-6,-9,-2,1,-6,2,-7,-10,-8,-8,-1,-4,5,7,9,-4,-4,3,-8,9,7,2,10,-2,5,7,-10,-2,9,8,5,-2,3,-7,10,-6,7,3,-2,-6,-5,-2,-3,4,4,-1,2,-9,9,-9,-2,-9,3,-6,7,1,-4,8,7,-3,-2,9,-8,-2,-6,9,3,7,-10,-2,-7,-10,8,-10,10,6,-8,7,-7,4,-9,1,2,10,3,10,9,-10,-8,1,-6,9,6,-1,-6,-6,7,-6,9,3,-10,-1,1,-5,4,6,-7,-5,4,5,8,-4,1,7,8,2,-1,8,-4,2,2,-1,6,9,-9,-9,-6,-5,-2,6,10,-9,-9,-6,3,5,7,-2,2,-4,-6,10,-5,10,7,9,-2,-10,-7,-7,4,4,10,6,-9,-2,1,-8,9,4,-4,3,3,-10,-8,1,-1,-3,2,2,10,-10,-8,-7,-8,10,6,-9,-7,-9,4,-6,6,-5,-9,-4,2,9,-2,-8,-9,-2,4,-6,-8,3,-7,-8,-8,-3,-3,5,-1,-7,1,3,6,5,-5,-8,-5,7,-1,5,10,-6,7,8,6,-10,3,-6,-9,6,1,-6,-6,-8,-10,8,-3,2,-8,9,-8,-10,2,-7,-9,4,-8,6,-5,-2,-9,4,-7,-3,9,-10,1,-7,9,4,8,6,10,1,-6,2,-7,7,-5,10,2,-10,-3,-6,2,8,9,7,6,7,-4,7,-7,5,7,-5,-7,-2,3,-1,-1,6,-3,-1,2,-10,9,6,-6,-8,-6,3,-10,-2,-4,-8,1,5,7,-2,-6,-5,-2,2,2,2,-3,-1,-8,5,-7,-7,9,2,-9,-4,7,-1,10,8,3,10,-2,8,6,-4,-6,-9,4,-10,-6,-2,-6,3,-8,8,8,7,10,10,7,-7,6,6,9,-6,2,9,1,-4,10,10,1,-10,1,5,5,-2,9,-4,6,5,-8,-4,6,-9,9,6,9,10,-7,9,-8,4,9,-8,-8,2,9,6,-3,4,6,-3,6,-4,-8,-5,-4,-6,5,-7,-8,8,5,5,-10,-2,-8,9,8,-7,6,5,-10,-2,-4,7,-6,-3,10,-10,6,-7,7,-10,-1,3,8,-9,8,5,-10,6,-9,8,-9,-10,-10,-1,4], dtype = "int8")#candidate|2464|(1573,)|const|int8
call_2463 = relay.TupleGetItem(func_2230_call(relay.reshape(const_2464.astype('int8'), [1573,])), 1)
call_2465 = relay.TupleGetItem(func_2233_call(relay.reshape(const_2464.astype('int8'), [1573,])), 1)
output = relay.Tuple([bop_2425,call_2437,call_2441,call_2463,const_2464,])
output2 = relay.Tuple([bop_2425,call_2438,call_2442,call_2465,const_2464,])
func_2468 = relay.Function([var_2424,], output)
mod['func_2468'] = func_2468
mod = relay.transform.InferType()(mod)
mutated_mod['func_2468'] = func_2468
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2469 = relay.var("var_2469", dtype = "bool", shape = (13, 13, 7))#candidate|2469|(13, 13, 7)|var|bool
func_2468_call = mutated_mod.get_global_var('func_2468')
call_2470 = func_2468_call(var_2469)
output = call_2470
func_2471 = relay.Function([var_2469], output)
mutated_mod['func_2471'] = func_2471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_2473 = func_2030_call()
call_2474 = func_2030_call()
func_1482_call = mod.get_global_var('func_1482')
func_1485_call = mutated_mod.get_global_var('func_1485')
var_2479 = relay.var("var_2479", dtype = "uint16", shape = (1, 364))#candidate|2479|(1, 364)|var|uint16
call_2478 = relay.TupleGetItem(func_1482_call(relay.reshape(var_2479.astype('uint16'), [7, 4, 13])), 2)
call_2480 = relay.TupleGetItem(func_1485_call(relay.reshape(var_2479.astype('uint16'), [7, 4, 13])), 2)
func_1546_call = mod.get_global_var('func_1546')
func_1550_call = mutated_mod.get_global_var('func_1550')
var_2482 = relay.var("var_2482", dtype = "int16", shape = (80,))#candidate|2482|(80,)|var|int16
call_2481 = relay.TupleGetItem(func_1546_call(relay.reshape(var_2482.astype('int16'), [10, 2, 4]), relay.reshape(var_2482.astype('int16'), [10, 2, 4]), ), 1)
call_2483 = relay.TupleGetItem(func_1550_call(relay.reshape(var_2482.astype('int16'), [10, 2, 4]), relay.reshape(var_2482.astype('int16'), [10, 2, 4]), ), 1)
func_1482_call = mod.get_global_var('func_1482')
func_1485_call = mutated_mod.get_global_var('func_1485')
call_2505 = relay.TupleGetItem(func_1482_call(relay.reshape(var_2479.astype('uint16'), [7, 4, 13])), 3)
call_2506 = relay.TupleGetItem(func_1485_call(relay.reshape(var_2479.astype('uint16'), [7, 4, 13])), 3)
var_2520 = relay.var("var_2520", dtype = "uint16", shape = (7, 364))#candidate|2520|(7, 364)|var|uint16
bop_2521 = relay.add(var_2479.astype('uint64'), var_2520.astype('uint64')) # shape=(7, 364)
uop_2528 = relay.log2(var_2520.astype('float32')) # shape=(7, 364)
var_2540 = relay.var("var_2540", dtype = "float32", shape = (7, 364))#candidate|2540|(7, 364)|var|float32
bop_2541 = relay.bitwise_xor(uop_2528.astype('int64'), relay.reshape(var_2540.astype('int64'), relay.shape_of(uop_2528))) # shape=(7, 364)
uop_2556 = relay.asinh(uop_2528.astype('float64')) # shape=(7, 364)
bop_2558 = relay.logical_and(bop_2541.astype('bool'), relay.reshape(bop_2521.astype('bool'), relay.shape_of(bop_2541))) # shape=(7, 364)
var_2561 = relay.var("var_2561", dtype = "uint16", shape = (11, 364))#candidate|2561|(11, 364)|var|uint16
bop_2562 = relay.subtract(var_2479.astype('uint8'), var_2561.astype('uint8')) # shape=(11, 364)
func_1917_call = mod.get_global_var('func_1917')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_2569 = relay.TupleGetItem(func_1917_call(), 0)
call_2570 = relay.TupleGetItem(func_1919_call(), 0)
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
call_2576 = relay.TupleGetItem(func_107_call(relay.reshape(call_2478.astype('int16'), [11, 6, 7]), relay.reshape(call_2478.astype('int16'), [11, 6, 7]), ), 0)
call_2577 = relay.TupleGetItem(func_111_call(relay.reshape(call_2478.astype('int16'), [11, 6, 7]), relay.reshape(call_2478.astype('int16'), [11, 6, 7]), ), 0)
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_2582 = func_1638_call()
call_2583 = func_1638_call()
output = relay.Tuple([call_2473,call_2478,call_2481,var_2482,call_2505,uop_2556,bop_2558,bop_2562,call_2569,call_2576,call_2582,])
output2 = relay.Tuple([call_2474,call_2480,call_2483,var_2482,call_2506,uop_2556,bop_2558,bop_2562,call_2570,call_2577,call_2583,])
func_2584 = relay.Function([var_2479,var_2482,var_2520,var_2540,var_2561,], output)
mod['func_2584'] = func_2584
mod = relay.transform.InferType()(mod)
mutated_mod['func_2584'] = func_2584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2584_call = mutated_mod.get_global_var('func_2584')
var_2586 = relay.var("var_2586", dtype = "uint16", shape = (1, 364))#candidate|2586|(1, 364)|var|uint16
var_2587 = relay.var("var_2587", dtype = "int16", shape = (80,))#candidate|2587|(80,)|var|int16
var_2588 = relay.var("var_2588", dtype = "uint16", shape = (7, 364))#candidate|2588|(7, 364)|var|uint16
var_2589 = relay.var("var_2589", dtype = "float32", shape = (7, 364))#candidate|2589|(7, 364)|var|float32
var_2590 = relay.var("var_2590", dtype = "uint16", shape = (11, 364))#candidate|2590|(11, 364)|var|uint16
call_2585 = func_2584_call(var_2586,var_2587,var_2588,var_2589,var_2590,)
output = call_2585
func_2591 = relay.Function([var_2586,var_2587,var_2588,var_2589,var_2590,], output)
mutated_mod['func_2591'] = func_2591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_385_call = mod.get_global_var('func_385')
func_386_call = mutated_mod.get_global_var('func_386')
call_2596 = func_385_call()
call_2597 = func_385_call()
func_1074_call = mod.get_global_var('func_1074')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_2599 = relay.TupleGetItem(func_1074_call(), 0)
call_2600 = relay.TupleGetItem(func_1076_call(), 0)
func_2118_call = mod.get_global_var('func_2118')
func_2120_call = mutated_mod.get_global_var('func_2120')
call_2611 = relay.TupleGetItem(func_2118_call(), 0)
call_2612 = relay.TupleGetItem(func_2120_call(), 0)
output = relay.Tuple([call_2596,call_2599,call_2611,])
output2 = relay.Tuple([call_2597,call_2600,call_2612,])
func_2613 = relay.Function([], output)
mod['func_2613'] = func_2613
mod = relay.transform.InferType()(mod)
mutated_mod['func_2613'] = func_2613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2613_call = mutated_mod.get_global_var('func_2613')
call_2614 = func_2613_call()
output = call_2614
func_2615 = relay.Function([], output)
mutated_mod['func_2615'] = func_2615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_2694 = func_1638_call()
call_2695 = func_1638_call()
uop_2702 = relay.acos(call_2694.astype('float64')) # shape=(10, 8, 12)
uop_2704 = relay.acos(call_2695.astype('float64')) # shape=(10, 8, 12)
output = uop_2702
output2 = uop_2704
func_2705 = relay.Function([], output)
mod['func_2705'] = func_2705
mod = relay.transform.InferType()(mod)
output = func_2705()
func_2706 = relay.Function([], output)
mutated_mod['func_2706'] = func_2706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1917_call = mod.get_global_var('func_1917')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_2767 = relay.TupleGetItem(func_1917_call(), 0)
call_2768 = relay.TupleGetItem(func_1919_call(), 0)
func_2705_call = mod.get_global_var('func_2705')
func_2706_call = mutated_mod.get_global_var('func_2706')
call_2778 = func_2705_call()
call_2779 = func_2705_call()
func_1619_call = mod.get_global_var('func_1619')
func_1620_call = mutated_mod.get_global_var('func_1620')
call_2782 = relay.TupleGetItem(func_1619_call(), 0)
call_2783 = relay.TupleGetItem(func_1620_call(), 0)
uop_2786 = relay.cos(call_2767.astype('float64')) # shape=(10, 8, 12)
uop_2788 = relay.cos(call_2768.astype('float64')) # shape=(10, 8, 12)
func_2316_call = mod.get_global_var('func_2316')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_2812 = relay.TupleGetItem(func_2316_call(), 2)
call_2813 = relay.TupleGetItem(func_2318_call(), 2)
output = relay.Tuple([call_2778,call_2782,uop_2786,call_2812,])
output2 = relay.Tuple([call_2779,call_2783,uop_2788,call_2813,])
func_2816 = relay.Function([], output)
mod['func_2816'] = func_2816
mod = relay.transform.InferType()(mod)
output = func_2816()
func_2817 = relay.Function([], output)
mutated_mod['func_2817'] = func_2817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_861_call = mutated_mod.get_global_var('func_861')
call_2834 = relay.TupleGetItem(func_859_call(), 0)
call_2835 = relay.TupleGetItem(func_861_call(), 0)
output = call_2834
output2 = call_2835
func_2842 = relay.Function([], output)
mod['func_2842'] = func_2842
mod = relay.transform.InferType()(mod)
output = func_2842()
func_2843 = relay.Function([], output)
mutated_mod['func_2843'] = func_2843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2118_call = mod.get_global_var('func_2118')
func_2120_call = mutated_mod.get_global_var('func_2120')
call_2951 = relay.TupleGetItem(func_2118_call(), 2)
call_2952 = relay.TupleGetItem(func_2120_call(), 2)
output = relay.Tuple([call_2951,])
output2 = relay.Tuple([call_2952,])
func_2963 = relay.Function([], output)
mod['func_2963'] = func_2963
mod = relay.transform.InferType()(mod)
output = func_2963()
func_2964 = relay.Function([], output)
mutated_mod['func_2964'] = func_2964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_2971 = func_2030_call()
call_2972 = func_2030_call()
output = call_2971
output2 = call_2972
func_2979 = relay.Function([], output)
mod['func_2979'] = func_2979
mod = relay.transform.InferType()(mod)
output = func_2979()
func_2980 = relay.Function([], output)
mutated_mod['func_2980'] = func_2980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2613_call = mod.get_global_var('func_2613')
func_2615_call = mutated_mod.get_global_var('func_2615')
call_2989 = relay.TupleGetItem(func_2613_call(), 1)
call_2990 = relay.TupleGetItem(func_2615_call(), 1)
output = call_2989
output2 = call_2990
func_3006 = relay.Function([], output)
mod['func_3006'] = func_3006
mod = relay.transform.InferType()(mod)
output = func_3006()
func_3007 = relay.Function([], output)
mutated_mod['func_3007'] = func_3007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2099_call = mod.get_global_var('func_2099')
func_2101_call = mutated_mod.get_global_var('func_2101')
call_3068 = func_2099_call()
call_3069 = func_2099_call()
func_1709_call = mod.get_global_var('func_1709')
func_1712_call = mutated_mod.get_global_var('func_1712')
var_3071 = relay.var("var_3071", dtype = "uint32", shape = (1001,))#candidate|3071|(1001,)|var|uint32
call_3070 = relay.TupleGetItem(func_1709_call(relay.reshape(var_3071.astype('uint32'), [13, 7, 11]), relay.reshape(var_3071.astype('uint32'), [13, 7, 11]), ), 1)
call_3072 = relay.TupleGetItem(func_1712_call(relay.reshape(var_3071.astype('uint32'), [13, 7, 11]), relay.reshape(var_3071.astype('uint32'), [13, 7, 11]), ), 1)
uop_3075 = relay.rsqrt(var_3071.astype('float32')) # shape=(1001,)
func_1982_call = mod.get_global_var('func_1982')
func_1984_call = mutated_mod.get_global_var('func_1984')
call_3079 = func_1982_call()
call_3080 = func_1982_call()
bop_3084 = relay.less(uop_3075.astype('bool'), relay.reshape(var_3071.astype('bool'), relay.shape_of(uop_3075))) # shape=(1001,)
var_3094 = relay.var("var_3094", dtype = "uint32", shape = (1001,))#candidate|3094|(1001,)|var|uint32
bop_3095 = relay.bitwise_and(var_3071.astype('int16'), relay.reshape(var_3094.astype('int16'), relay.shape_of(var_3071))) # shape=(1001,)
bop_3102 = relay.add(bop_3084.astype('uint64'), relay.reshape(uop_3075.astype('uint64'), relay.shape_of(bop_3084))) # shape=(1001,)
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_3121 = func_1638_call()
call_3122 = func_1638_call()
func_998_call = mod.get_global_var('func_998')
func_1001_call = mutated_mod.get_global_var('func_1001')
const_3130 = relay.const([[-6],[4],[8],[-6],[-3],[-2],[-5],[2],[3],[9],[5],[-1],[-4],[4],[8],[10],[4],[8],[5],[-8],[6],[-7],[-10],[-9],[1],[10],[1],[8],[6],[-7],[-4],[10],[10],[-10],[1],[5],[8],[8],[-3],[3],[-4],[1],[4],[-3],[1],[-5],[-6],[5],[-5],[2],[2],[5],[1],[8],[-2],[-9],[-5],[2],[-10],[-8],[-4],[6],[-1],[5],[-3],[-4],[-6],[5],[-4],[-1],[-5],[3],[-9],[-7],[-1],[-9],[-1],[-4],[-5],[10],[7],[5],[5],[-1],[2],[-5],[10],[-4],[4],[-9],[-8],[1],[-5],[-4],[5],[-8],[-8],[-6],[-2],[1],[-8],[-10],[-6],[-9],[-8],[9],[-9],[7],[-5],[-4],[-3],[-5],[-7],[3],[7],[-3],[4],[-3],[-2],[5],[3],[7],[-2],[5],[7],[8],[-2],[-2],[-5],[8],[3],[-6],[7],[-9],[4],[-10],[-8],[8],[-3],[-9],[-10],[2],[-1],[1],[-9],[5],[2],[-1],[5],[-9],[-4],[5],[-6],[-3],[-5],[1],[9],[-7],[8],[-4],[7],[-1],[5],[8],[-1],[-8],[-6],[6],[5],[2],[2],[-5],[-9],[-9],[10],[-3],[3],[6],[5],[-7],[-10],[1],[7],[9],[9],[-3],[-7],[9],[-1],[-2],[-2],[-8],[9],[4],[-9],[-2],[5],[7],[3],[5],[7],[2],[-6],[-9],[-1],[-8],[6],[-7],[-3],[2],[-1],[10],[-8],[-7],[1],[4],[10],[4],[-8],[3],[-6],[2],[8],[-10],[2],[10],[6],[9],[-7],[6],[6],[7],[-5],[10],[-6],[3],[-3],[-3],[-6],[-1],[-4],[-2],[-2],[-4],[-5],[8],[8],[7],[-8],[9],[1],[5],[8],[-6],[-2],[-3],[-1],[7],[-3],[-4],[-9],[2],[-2],[3],[8],[-6],[-3],[-5],[-1],[-5],[2],[-9],[10],[6],[-7],[4],[5],[-3],[4],[6],[7],[3],[3],[3],[10],[8],[4],[5],[-3],[9],[-1],[6],[-8],[-2],[-7],[4],[-2],[-6],[-4],[-8],[-4],[6],[-4],[-4],[-2],[-7],[-6],[1],[-3],[6],[-3],[4],[7],[10],[-8],[6],[7],[-2],[5],[-9],[8],[3],[10],[10],[9],[3],[-6],[9],[8],[7],[-10],[-8],[6],[-7],[3],[-1],[-4],[7],[-8],[-9],[-10],[-1],[1],[2],[-9],[-3],[-1],[-5],[10],[-10],[-10],[6],[-5],[1],[-9],[-2],[-3],[7],[-3],[3],[-9],[1],[7],[9],[-10],[2],[1],[-7],[10],[-10],[8],[-10],[-5],[7],[8],[-9],[4],[7],[6],[1],[-4],[-7],[3],[-1],[-1],[4],[3],[2],[-10],[5],[9],[-5],[4],[6],[-7],[-7],[2],[-5],[-7],[9],[-7],[9],[6],[-7],[2],[-4],[-6],[6],[10],[-9],[3],[-7],[-9],[1],[9],[5],[-3],[-8],[-10],[7],[9],[-5],[-10],[-6],[-4],[-7],[-10],[-3],[7],[8],[-4],[-3],[-9],[-7],[-10],[-1],[6],[5],[-6],[6],[5],[-9],[10],[-7],[-4],[2],[-7],[-6],[-10],[5],[9],[-8],[-3],[-3],[-3],[1],[4],[4],[-1],[-10],[5],[4],[9],[-8],[7],[6],[9],[-3],[6],[-1],[4],[-6],[3],[-2],[-10],[-9],[4],[-6],[-5],[9],[-6],[-8],[-10],[7],[-6],[2],[4],[8],[-9],[-2],[-3],[-3],[6],[8],[-4],[5],[-4],[6],[5],[-10],[6],[1],[-2],[-7],[-9],[8],[-10],[7],[-2],[9],[-5],[-5],[9],[-3],[-7],[-7],[6],[10],[7],[7],[-6],[8],[-7],[6],[-3],[5],[-1],[-7],[4],[-7],[4],[3],[-2],[-6],[-10],[-4],[7],[6],[8],[-5],[-7],[7],[3],[-10],[-5],[-9],[3],[-6],[4],[-3],[-4],[-3],[-1],[-7],[9],[10],[-2],[-3],[2],[-3],[2],[-5],[-3],[9],[1],[-2],[-3],[6],[-3],[2],[4],[-9],[-2],[3],[-8],[2],[-10],[5],[8],[-1],[-10],[-5],[-9],[6],[3],[8],[-2],[4],[-1],[-2],[5],[9],[1],[-9],[9],[-7],[4],[-1],[-3],[8],[5],[-5],[-3],[4],[8],[-3],[8],[-6],[-5],[7],[6],[7],[7],[4],[-5],[10],[-8],[-10],[4],[5],[8],[4],[-9],[6],[-7],[1],[10],[-5],[4],[-1],[-2],[10],[5],[-1],[3],[-10],[-3],[8],[5],[7],[10],[7],[-4],[9],[2],[10],[8],[-3],[1],[2],[1],[5],[-6],[-7],[1],[-5],[2],[1],[2],[7],[-7],[-7],[-6],[-9],[-6],[10],[-3],[-5],[-2],[-2],[-8],[1],[6],[-7],[1],[4],[10],[4],[6],[4],[-2],[-1],[-3],[-6],[1],[-5],[-4],[9],[8],[10],[-10],[7],[10],[8],[5],[-7],[-8],[4],[7],[6],[7],[-4],[-8],[10],[-9],[-7],[-7],[-8],[8],[-2],[-10],[9],[-7],[9],[2],[-1],[7],[-9],[8],[-4],[10],[-5],[8],[5],[-9],[-6],[-7],[-7],[10],[10],[3],[1],[7],[-6],[-9],[-2],[-2],[9],[10],[5],[-2],[10],[-7],[-4],[7],[9],[5],[10],[1],[-9],[-8],[3],[-7],[9],[8],[-1],[-4],[10],[2],[-8],[-9],[-8],[8],[8],[-6],[4],[-7],[-4],[-1],[6],[-7],[-10],[9],[-2],[-7],[9],[9],[2],[-5],[-1],[-9],[-3],[-1],[-3],[-9],[2],[7],[5],[-5],[7],[9],[-7],[3],[-8],[-2],[-7],[3],[9],[8],[8],[2],[-3],[3],[5],[7],[9],[-9],[-4],[8],[1],[8],[-2],[10],[7],[-5],[7],[-5],[4],[-8],[-8],[-10],[1],[-5],[-2],[-7],[-4],[-2],[8],[-10],[-2],[-9],[10],[-9],[4],[5],[2],[-10],[7],[-8],[-10],[-3],[-9],[-3],[-7],[-1],[-9],[7],[-4],[6],[-4],[3],[8],[-9],[-9],[-7],[9],[5],[5],[5],[2],[10],[-4],[-1],[-5],[-10],[9],[7],[5],[6],[2],[-4],[1],[8],[-7],[7],[-9],[-1],[6],[-3],[8],[-4],[-7],[6],[-6],[7],[-4],[-8],[2],[3],[9],[1],[7],[-10],[1],[-7],[-7],[5],[9],[-7],[4],[2],[6],[-4],[-6],[-10],[-7],[2],[10],[-8],[-7],[1],[6],[-9],[9],[-2],[1],[2],[-4],[6],[3],[6],[6],[3],[-3],[-8],[-10],[6],[6],[2],[3],[-8],[-8],[2],[9],[3],[-3],[-2],[-6],[-6],[10],[9],[2],[3],[-5],[3],[9],[-2],[6],[-8],[-1],[4],[9],[-4],[3],[-5],[-5],[-10],[-2],[-7],[9],[4],[-3],[-6],[10],[3],[6],[-7],[3],[9],[-3],[-8],[1],[-7],[2],[9],[-4],[-9],[9],[6],[-1],[3],[6],[10],[3],[-7],[6],[-9],[3],[9],[8],[7],[10],[8],[3],[-1],[5],[-2],[5],[-2],[3],[-9],[5],[5],[1],[-5],[1],[10],[-2],[-1],[2],[-1],[-7],[8],[5],[2],[-9],[7],[8],[4],[-6],[-8],[-3],[-8],[-7],[-1],[-10],[-6],[3],[9],[-3],[-8],[-4],[6],[6],[1],[3],[1],[-10],[-2],[-8],[5],[-5],[-5],[4],[8],[6],[10],[10],[-10],[-8],[-10],[-4],[8],[10],[10],[10],[5],[8],[-4],[5],[2],[8],[9],[-9],[-4],[-4],[9],[-7],[-2],[4],[-4],[9],[2],[9],[-4],[9],[-6],[-7],[5],[-6],[5],[5],[-7],[-1],[-1],[1],[3],[-5],[9],[-2],[8],[8],[-8],[-9],[-3],[6],[-6],[-1],[5],[-4],[-9],[10],[-8],[7],[-8],[-10],[-10],[-10],[-5],[5],[-5],[-5],[-2],[-8],[8],[-3],[-8],[9],[9],[3],[4],[-4],[4],[-5],[3],[9],[1],[-1],[-10],[-1],[-10],[7],[9],[-5],[-5],[6],[4],[6],[-5],[10],[-10],[-6],[-1],[-3],[-5],[-1],[-9],[4],[-8],[6],[7],[-3],[-1],[-2],[-9],[-4],[9],[2],[-8],[-3],[9],[9],[-6],[-8],[2],[-8],[-4],[-2],[9],[1],[4],[8],[5],[5],[5],[8],[6],[6],[10],[6],[5],[-1],[-4],[-6],[-6],[-4],[-2],[6],[-2],[-3],[-1],[-5],[-2],[-8],[-4],[-6],[-8],[-10],[9],[9],[2],[-8],[6],[4],[-4],[-7],[9],[1],[2],[4],[6],[4],[7],[10],[7],[3],[-3],[-4],[2],[-8],[-4],[-1],[-8],[6],[6],[5],[10],[-5],[1],[-4],[5],[10],[8],[-6],[1],[-9],[1],[-9],[6],[7],[7],[-1],[-1],[-5],[2],[-3],[-9],[-4],[8],[-9],[5],[7],[10],[3],[3],[-8],[-1],[-7],[-7],[-7],[2],[-7],[-4],[7],[-2],[4],[-8],[3],[8],[6],[7],[-2],[-2],[3],[9],[-10],[9],[-3],[-10],[-6],[9],[-10],[-10],[7],[-1],[9],[-6],[6],[-8],[-9],[6],[-10],[-9],[-9],[-5],[1],[-4],[3],[4],[-2],[-10],[2],[-2],[3],[-5],[8],[4],[-10],[3],[9],[-2],[-2],[-1],[-2],[4],[1],[5],[-9],[10],[-6],[6],[10],[-4],[-2],[8],[4],[4],[-8],[-2],[10],[-4],[-9],[4],[5],[-2],[1],[-7],[-10],[9],[-5],[-5],[-9],[-7],[-4],[7],[3],[6],[-10],[2],[4],[-6],[-3],[-4],[-3],[7],[4],[-9],[1],[-9],[-2],[-8],[8],[1],[-4],[-3],[6],[-3],[-4],[4],[-2],[5],[4],[-8],[-9],[7],[-5],[-10],[-1],[-9],[3],[-3],[-1],[10],[5],[-3],[6],[4],[2],[-5],[1],[2],[-9],[7],[3],[-6],[7],[-5],[-8],[-6],[-10],[2],[6],[8],[-8],[-9],[-4],[-4],[-5],[-4],[-8],[3],[4],[8],[3],[-4],[2],[1],[-2],[8],[-1],[-10],[1],[-10],[7],[-3],[6],[2],[3],[1],[3],[-9],[3],[-7],[-8],[-6],[3],[1],[-10],[-8],[-7],[-1],[6],[3],[1],[-5],[1],[-1],[1],[-1],[2],[-7],[-3],[-9],[-9],[9],[-10],[9],[2],[-7],[-7],[-7],[-4],[5],[6],[-6],[5],[-3],[2],[-1],[-1],[-9],[9],[-8],[1],[3],[-6],[8],[-9],[-9],[1],[3],[-1],[-4],[6],[-7],[4],[-7],[5],[3],[9],[-6],[6],[-8],[1],[2],[-7],[7],[9],[10],[-7],[-4],[3],[3],[7],[6],[1],[4],[7],[2],[1],[9],[-7],[3],[-10],[-3],[4],[-1],[1],[6],[1],[5],[-5],[-7],[2],[2],[5],[9],[-10],[10],[-9],[-8],[-2],[-9],[4],[-10],[-9],[-4],[5],[7],[-3],[9],[10],[10],[4],[1],[-2],[-6],[9],[-7],[3],[5],[4],[6],[-3],[7],[4],[3],[-7],[6],[-4],[-5],[-6],[-3],[10],[-8],[-9],[5],[-2],[-5],[6],[10],[1],[5]], dtype = "int8")#candidate|3130|(1573, 1)|const|int8
call_3129 = relay.TupleGetItem(func_998_call(relay.reshape(const_3130.astype('int8'), [11, 11, 13])), 2)
call_3131 = relay.TupleGetItem(func_1001_call(relay.reshape(const_3130.astype('int8'), [11, 11, 13])), 2)
func_2705_call = mod.get_global_var('func_2705')
func_2706_call = mutated_mod.get_global_var('func_2706')
call_3142 = func_2705_call()
call_3143 = func_2705_call()
output = relay.Tuple([call_3068,call_3070,call_3079,bop_3095,bop_3102,call_3121,call_3129,const_3130,call_3142,])
output2 = relay.Tuple([call_3069,call_3072,call_3080,bop_3095,bop_3102,call_3122,call_3131,const_3130,call_3143,])
func_3145 = relay.Function([var_3071,var_3094,], output)
mod['func_3145'] = func_3145
mod = relay.transform.InferType()(mod)
var_3146 = relay.var("var_3146", dtype = "uint32", shape = (1001,))#candidate|3146|(1001,)|var|uint32
var_3147 = relay.var("var_3147", dtype = "uint32", shape = (1001,))#candidate|3147|(1001,)|var|uint32
output = func_3145(var_3146,var_3147,)
func_3148 = relay.Function([var_3146,var_3147,], output)
mutated_mod['func_3148'] = func_3148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_385_call = mod.get_global_var('func_385')
func_386_call = mutated_mod.get_global_var('func_386')
call_3178 = func_385_call()
call_3179 = func_385_call()
output = relay.Tuple([call_3178,])
output2 = relay.Tuple([call_3179,])
func_3181 = relay.Function([], output)
mod['func_3181'] = func_3181
mod = relay.transform.InferType()(mod)
output = func_3181()
func_3182 = relay.Function([], output)
mutated_mod['func_3182'] = func_3182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2316_call = mod.get_global_var('func_2316')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_3189 = relay.TupleGetItem(func_2316_call(), 0)
call_3190 = relay.TupleGetItem(func_2318_call(), 0)
func_2341_call = mod.get_global_var('func_2341')
func_2342_call = mutated_mod.get_global_var('func_2342')
call_3206 = relay.TupleGetItem(func_2341_call(), 0)
call_3207 = relay.TupleGetItem(func_2342_call(), 0)
output = relay.Tuple([call_3189,call_3206,])
output2 = relay.Tuple([call_3190,call_3207,])
func_3213 = relay.Function([], output)
mod['func_3213'] = func_3213
mod = relay.transform.InferType()(mod)
output = func_3213()
func_3214 = relay.Function([], output)
mutated_mod['func_3214'] = func_3214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1074_call = mod.get_global_var('func_1074')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_3301 = relay.TupleGetItem(func_1074_call(), 0)
call_3302 = relay.TupleGetItem(func_1076_call(), 0)
func_1917_call = mod.get_global_var('func_1917')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_3312 = relay.TupleGetItem(func_1917_call(), 1)
call_3313 = relay.TupleGetItem(func_1919_call(), 1)
bop_3314 = relay.logical_xor(call_3301.astype('uint8'), relay.reshape(call_3312.astype('uint8'), relay.shape_of(call_3301))) # shape=(10, 8, 12)
bop_3317 = relay.logical_xor(call_3302.astype('uint8'), relay.reshape(call_3313.astype('uint8'), relay.shape_of(call_3302))) # shape=(10, 8, 12)
bop_3318 = relay.logical_and(call_3301.astype('bool'), relay.reshape(call_3312.astype('bool'), relay.shape_of(call_3301))) # shape=(10, 8, 12)
bop_3321 = relay.logical_and(call_3302.astype('bool'), relay.reshape(call_3313.astype('bool'), relay.shape_of(call_3302))) # shape=(10, 8, 12)
output = relay.Tuple([bop_3314,bop_3318,])
output2 = relay.Tuple([bop_3317,bop_3321,])
func_3322 = relay.Function([], output)
mod['func_3322'] = func_3322
mod = relay.transform.InferType()(mod)
output = func_3322()
func_3323 = relay.Function([], output)
mutated_mod['func_3323'] = func_3323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1982_call = mod.get_global_var('func_1982')
func_1984_call = mutated_mod.get_global_var('func_1984')
call_3327 = func_1982_call()
call_3328 = func_1982_call()
var_3329 = relay.var("var_3329", dtype = "float32", shape = (10, 8, 12))#candidate|3329|(10, 8, 12)|var|float32
bop_3330 = relay.mod(call_3327.astype('float32'), relay.reshape(var_3329.astype('float32'), relay.shape_of(call_3327))) # shape=(10, 8, 12)
bop_3333 = relay.mod(call_3328.astype('float32'), relay.reshape(var_3329.astype('float32'), relay.shape_of(call_3328))) # shape=(10, 8, 12)
output = bop_3330
output2 = bop_3333
func_3359 = relay.Function([var_3329,], output)
mod['func_3359'] = func_3359
mod = relay.transform.InferType()(mod)
var_3360 = relay.var("var_3360", dtype = "float32", shape = (10, 8, 12))#candidate|3360|(10, 8, 12)|var|float32
output = func_3359(var_3360)
func_3361 = relay.Function([var_3360], output)
mutated_mod['func_3361'] = func_3361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3006_call = mod.get_global_var('func_3006')
func_3007_call = mutated_mod.get_global_var('func_3007')
call_3387 = func_3006_call()
call_3388 = func_3006_call()
func_3322_call = mod.get_global_var('func_3322')
func_3323_call = mutated_mod.get_global_var('func_3323')
call_3394 = relay.TupleGetItem(func_3322_call(), 0)
call_3395 = relay.TupleGetItem(func_3323_call(), 0)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_3400 = func_254_call()
call_3401 = func_254_call()
output = relay.Tuple([call_3387,call_3394,call_3400,])
output2 = relay.Tuple([call_3388,call_3395,call_3401,])
func_3403 = relay.Function([], output)
mod['func_3403'] = func_3403
mod = relay.transform.InferType()(mod)
output = func_3403()
func_3404 = relay.Function([], output)
mutated_mod['func_3404'] = func_3404
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3409 = relay.var("var_3409", dtype = "uint32", shape = (11, 13, 5))#candidate|3409|(11, 13, 5)|var|uint32
var_3410 = relay.var("var_3410", dtype = "uint32", shape = (11, 13, 5))#candidate|3410|(11, 13, 5)|var|uint32
bop_3411 = relay.left_shift(var_3409.astype('uint32'), relay.reshape(var_3410.astype('uint32'), relay.shape_of(var_3409))) # shape=(11, 13, 5)
output = relay.Tuple([bop_3411,])
output2 = relay.Tuple([bop_3411,])
func_3416 = relay.Function([var_3409,var_3410,], output)
mod['func_3416'] = func_3416
mod = relay.transform.InferType()(mod)
var_3417 = relay.var("var_3417", dtype = "uint32", shape = (11, 13, 5))#candidate|3417|(11, 13, 5)|var|uint32
var_3418 = relay.var("var_3418", dtype = "uint32", shape = (11, 13, 5))#candidate|3418|(11, 13, 5)|var|uint32
output = func_3416(var_3417,var_3418,)
func_3419 = relay.Function([var_3417,var_3418,], output)
mutated_mod['func_3419'] = func_3419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_3444 = relay.TupleGetItem(func_3181_call(), 0)
call_3445 = relay.TupleGetItem(func_3182_call(), 0)
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
var_3447 = relay.var("var_3447", dtype = "int16", shape = (462,))#candidate|3447|(462,)|var|int16
call_3446 = relay.TupleGetItem(func_107_call(relay.reshape(var_3447.astype('int16'), [11, 6, 7]), relay.reshape(var_3447.astype('int16'), [11, 6, 7]), ), 0)
call_3448 = relay.TupleGetItem(func_111_call(relay.reshape(var_3447.astype('int16'), [11, 6, 7]), relay.reshape(var_3447.astype('int16'), [11, 6, 7]), ), 0)
func_1585_call = mod.get_global_var('func_1585')
func_1586_call = mutated_mod.get_global_var('func_1586')
call_3451 = relay.TupleGetItem(func_1585_call(), 1)
call_3452 = relay.TupleGetItem(func_1586_call(), 1)
func_774_call = mod.get_global_var('func_774')
func_775_call = mutated_mod.get_global_var('func_775')
call_3454 = relay.TupleGetItem(func_774_call(), 0)
call_3455 = relay.TupleGetItem(func_775_call(), 0)
output = relay.Tuple([call_3444,call_3446,var_3447,call_3451,call_3454,])
output2 = relay.Tuple([call_3445,call_3448,var_3447,call_3452,call_3455,])
func_3456 = relay.Function([var_3447,], output)
mod['func_3456'] = func_3456
mod = relay.transform.InferType()(mod)
var_3457 = relay.var("var_3457", dtype = "int16", shape = (462,))#candidate|3457|(462,)|var|int16
output = func_3456(var_3457)
func_3458 = relay.Function([var_3457], output)
mutated_mod['func_3458'] = func_3458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1253_call = mod.get_global_var('func_1253')
func_1255_call = mutated_mod.get_global_var('func_1255')
call_3474 = relay.TupleGetItem(func_1253_call(), 0)
call_3475 = relay.TupleGetItem(func_1255_call(), 0)
func_1253_call = mod.get_global_var('func_1253')
func_1255_call = mutated_mod.get_global_var('func_1255')
call_3477 = relay.TupleGetItem(func_1253_call(), 0)
call_3478 = relay.TupleGetItem(func_1255_call(), 0)
func_2468_call = mod.get_global_var('func_2468')
func_2471_call = mutated_mod.get_global_var('func_2471')
var_3481 = relay.var("var_3481", dtype = "bool", shape = (1183,))#candidate|3481|(1183,)|var|bool
call_3480 = relay.TupleGetItem(func_2468_call(relay.reshape(var_3481.astype('bool'), [13, 13, 7])), 1)
call_3482 = relay.TupleGetItem(func_2471_call(relay.reshape(var_3481.astype('bool'), [13, 13, 7])), 1)
output = relay.Tuple([call_3474,call_3477,call_3480,var_3481,])
output2 = relay.Tuple([call_3475,call_3478,call_3482,var_3481,])
func_3505 = relay.Function([var_3481,], output)
mod['func_3505'] = func_3505
mod = relay.transform.InferType()(mod)
var_3506 = relay.var("var_3506", dtype = "bool", shape = (1183,))#candidate|3506|(1183,)|var|bool
output = func_3505(var_3506)
func_3507 = relay.Function([var_3506], output)
mutated_mod['func_3507'] = func_3507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_3530 = func_254_call()
call_3531 = func_254_call()
output = call_3530
output2 = call_3531
func_3534 = relay.Function([], output)
mod['func_3534'] = func_3534
mod = relay.transform.InferType()(mod)
output = func_3534()
func_3535 = relay.Function([], output)
mutated_mod['func_3535'] = func_3535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3213_call = mod.get_global_var('func_3213')
func_3214_call = mutated_mod.get_global_var('func_3214')
call_3556 = relay.TupleGetItem(func_3213_call(), 1)
call_3557 = relay.TupleGetItem(func_3214_call(), 1)
output = relay.Tuple([call_3556,])
output2 = relay.Tuple([call_3557,])
func_3562 = relay.Function([], output)
mod['func_3562'] = func_3562
mod = relay.transform.InferType()(mod)
mutated_mod['func_3562'] = func_3562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3562_call = mutated_mod.get_global_var('func_3562')
call_3563 = func_3562_call()
output = call_3563
func_3564 = relay.Function([], output)
mutated_mod['func_3564'] = func_3564
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3572 = relay.var("var_3572", dtype = "float64", shape = (12, 3, 10))#candidate|3572|(12, 3, 10)|var|float64
var_3573 = relay.var("var_3573", dtype = "float64", shape = (12, 3, 10))#candidate|3573|(12, 3, 10)|var|float64
bop_3574 = relay.floor_divide(var_3572.astype('float64'), relay.reshape(var_3573.astype('float64'), relay.shape_of(var_3572))) # shape=(12, 3, 10)
bop_3587 = relay.greater_equal(var_3573.astype('bool'), relay.reshape(var_3572.astype('bool'), relay.shape_of(var_3573))) # shape=(12, 3, 10)
const_3598 = relay.const([[[1.973119,-0.876524,-3.538038,-5.763924,-1.660023,4.814456,-1.527970,-4.006314,6.181639,-4.922700],[6.940567,-9.322495,2.983236,-8.504977,1.529806,0.812028,0.585856,-0.868022,0.025635,9.922372],[9.419569,3.530160,-9.630878,4.521673,2.316983,5.805135,-8.754058,7.878553,-1.635219,4.795939]],[[4.797527,-3.572946,-0.824765,-0.929227,6.289692,4.531804,-8.871690,-5.730222,2.753125,-7.668455],[-6.898480,3.550521,-4.741149,-4.590333,-1.528556,-6.726016,-7.459153,-4.566395,4.698535,-1.979854],[-7.199069,0.723430,6.086796,-4.066085,4.479333,9.975463,-7.123737,-4.278418,9.504735,8.390738]],[[-0.884993,2.330550,6.299712,-5.907137,-9.979164,7.226238,-1.091799,-6.498257,1.980054,-9.709292],[1.414763,-5.277994,-9.723173,-9.402223,9.717167,9.454070,0.152106,-8.690519,-8.258606,3.621633],[5.330712,-3.542555,3.499209,4.622545,9.365168,-3.003666,-2.682356,-8.103486,5.119064,-3.359936]],[[-9.916392,9.773678,3.411148,-7.187414,-7.902755,-8.548317,3.416693,4.725981,1.273501,4.292504],[4.327580,-9.679696,-4.425844,-2.561557,8.484563,-1.127146,0.217540,-5.451741,2.942941,-5.907646],[-5.128133,1.555820,6.687651,9.593240,-8.073491,7.710366,-0.548634,0.438187,-0.984889,-5.134254]],[[-3.397981,-9.281949,-0.530597,-3.124721,1.542453,7.510116,-2.547753,8.344734,-5.974284,-2.448384],[0.907342,-4.598353,9.563805,-7.196620,6.537640,-7.515963,4.290612,6.204763,0.686214,5.681457],[8.199923,-2.259389,-8.541069,2.775399,-1.603953,2.346819,-5.135508,7.022120,0.623352,5.391937]],[[8.325470,-5.105524,-1.231921,-5.438588,-0.943622,5.090736,6.828035,5.827231,2.299862,-3.041957],[-4.321647,-3.962705,7.613172,2.742916,2.500520,5.485506,-2.287304,-1.864207,-4.290440,-9.282805],[-4.786463,-7.585738,5.944170,7.349089,-8.721151,1.084514,2.613362,2.105752,1.500499,6.474881]],[[-9.140156,1.124679,7.185564,1.686971,3.504592,-2.746971,9.255517,5.300680,-7.415320,-1.029727],[-9.607437,2.082955,9.138306,-2.405936,4.131306,2.085529,-5.719142,-6.666590,-0.821197,2.145453],[6.223614,-0.438594,-2.569978,-4.260590,-4.045325,-7.638280,-5.939795,8.988051,-1.304962,-5.858385]],[[2.056210,0.409987,6.092434,7.488583,-5.388048,7.727299,-8.981878,-1.373689,6.486931,0.311520],[7.663735,-9.041066,-6.821790,0.010747,9.636231,-3.276977,-2.412166,-0.672904,-9.091431,4.800382],[7.799970,-5.836943,-3.500211,-7.183352,0.835584,-8.841245,7.175898,-6.998223,-0.019452,2.971691]],[[-0.425124,-6.512055,0.772819,-0.497384,1.666269,-6.217934,-4.833545,-4.720517,-2.330333,-4.940544],[0.715693,-6.154139,2.472181,-6.943481,7.705823,4.626598,1.203631,-4.349612,-7.734956,-1.239020],[-1.080140,-9.331816,-1.791906,-9.304093,-4.958946,-8.956039,4.260645,-0.726884,-1.756458,-3.843625]],[[-1.628574,5.342024,9.190258,9.212170,-6.485041,7.593986,-3.359357,6.255559,8.261044,0.329629],[-4.962755,7.655276,1.201457,-6.689880,-7.244841,4.712163,-4.184100,-7.745728,-5.082632,9.339987],[-7.124941,5.313897,5.140861,8.456376,-8.800725,-3.173211,-3.959343,-3.609594,1.305914,3.243621]],[[5.746990,5.446253,4.378084,-4.704747,7.568381,-1.562637,-9.062839,-3.001603,-8.302089,-0.316134],[3.020515,9.910657,-0.806932,8.570539,-7.107951,4.399149,9.409227,8.773491,7.715875,-7.204510],[-0.002766,-4.316682,-0.313489,-2.489669,-9.245579,-3.760761,6.814173,6.633205,5.020539,2.296351]],[[-9.106571,-2.799398,7.646068,-8.699631,6.044019,2.930607,-5.179824,-6.363486,2.409454,6.857608],[-0.071225,2.541575,-4.642072,7.591503,8.945615,3.499354,-5.948165,6.718819,-5.200829,-2.692679],[-5.284911,0.606293,9.869362,4.436555,-2.579282,-5.052583,-0.080278,-0.819898,-2.384888,8.651252]]], dtype = "float64")#candidate|3598|(12, 3, 10)|const|float64
bop_3599 = relay.bitwise_and(var_3573.astype('int64'), relay.reshape(const_3598.astype('int64'), relay.shape_of(var_3573))) # shape=(12, 3, 10)
uop_3603 = relay.rsqrt(var_3572.astype('float32')) # shape=(12, 3, 10)
func_774_call = mod.get_global_var('func_774')
func_775_call = mutated_mod.get_global_var('func_775')
call_3607 = relay.TupleGetItem(func_774_call(), 0)
call_3608 = relay.TupleGetItem(func_775_call(), 0)
bop_3636 = relay.equal(bop_3587.astype('bool'), relay.reshape(bop_3599.astype('bool'), relay.shape_of(bop_3587))) # shape=(12, 3, 10)
func_1253_call = mod.get_global_var('func_1253')
func_1255_call = mutated_mod.get_global_var('func_1255')
call_3639 = relay.TupleGetItem(func_1253_call(), 0)
call_3640 = relay.TupleGetItem(func_1255_call(), 0)
output = relay.Tuple([bop_3574,uop_3603,call_3607,bop_3636,call_3639,])
output2 = relay.Tuple([bop_3574,uop_3603,call_3608,bop_3636,call_3640,])
func_3642 = relay.Function([var_3572,var_3573,], output)
mod['func_3642'] = func_3642
mod = relay.transform.InferType()(mod)
mutated_mod['func_3642'] = func_3642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3642_call = mutated_mod.get_global_var('func_3642')
var_3644 = relay.var("var_3644", dtype = "float64", shape = (12, 3, 10))#candidate|3644|(12, 3, 10)|var|float64
var_3645 = relay.var("var_3645", dtype = "float64", shape = (12, 3, 10))#candidate|3645|(12, 3, 10)|var|float64
call_3643 = func_3642_call(var_3644,var_3645,)
output = call_3643
func_3646 = relay.Function([var_3644,var_3645,], output)
mutated_mod['func_3646'] = func_3646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_3657 = func_1638_call()
call_3658 = func_1638_call()
var_3661 = relay.var("var_3661", dtype = "float32", shape = (10, 8, 12))#candidate|3661|(10, 8, 12)|var|float32
bop_3662 = relay.floor_divide(call_3657.astype('float64'), relay.reshape(var_3661.astype('float64'), relay.shape_of(call_3657))) # shape=(10, 8, 12)
bop_3665 = relay.floor_divide(call_3658.astype('float64'), relay.reshape(var_3661.astype('float64'), relay.shape_of(call_3658))) # shape=(10, 8, 12)
output = bop_3662
output2 = bop_3665
func_3669 = relay.Function([var_3661,], output)
mod['func_3669'] = func_3669
mod = relay.transform.InferType()(mod)
var_3670 = relay.var("var_3670", dtype = "float32", shape = (10, 8, 12))#candidate|3670|(10, 8, 12)|var|float32
output = func_3669(var_3670)
func_3671 = relay.Function([var_3670], output)
mutated_mod['func_3671'] = func_3671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1619_call = mod.get_global_var('func_1619')
func_1620_call = mutated_mod.get_global_var('func_1620')
call_3678 = relay.TupleGetItem(func_1619_call(), 0)
call_3679 = relay.TupleGetItem(func_1620_call(), 0)
func_3534_call = mod.get_global_var('func_3534')
func_3535_call = mutated_mod.get_global_var('func_3535')
call_3682 = func_3534_call()
call_3683 = func_3534_call()
func_1638_call = mod.get_global_var('func_1638')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_3686 = func_1638_call()
call_3687 = func_1638_call()
output = relay.Tuple([call_3678,call_3682,call_3686,])
output2 = relay.Tuple([call_3679,call_3683,call_3687,])
func_3688 = relay.Function([], output)
mod['func_3688'] = func_3688
mod = relay.transform.InferType()(mod)
output = func_3688()
func_3689 = relay.Function([], output)
mutated_mod['func_3689'] = func_3689
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3719 = relay.var("var_3719", dtype = "int64", shape = ())#candidate|3719|()|var|int64
var_3720 = relay.var("var_3720", dtype = "int64", shape = (1, 14, 16))#candidate|3720|(1, 14, 16)|var|int64
bop_3721 = relay.less_equal(var_3719.astype('bool'), var_3720.astype('bool')) # shape=(1, 14, 16)
func_1862_call = mod.get_global_var('func_1862')
func_1864_call = mutated_mod.get_global_var('func_1864')
const_3725 = relay.const([2.177998,-7.312677,9.240481,7.282572,3.135305,-7.536633,9.018763,-9.779199,2.159509,-4.334720,-6.796647,2.416450,-0.740475,-5.370541,0.597000,-8.890618,-4.059063,6.668677,-0.916987,8.717764,4.474876,-7.329633,-4.703950,-9.183086,-8.670692,0.323422,0.216789,-7.008539,-3.047800,6.606176,-5.714487,6.347384], dtype = "float64")#candidate|3725|(32,)|const|float64
call_3724 = relay.TupleGetItem(func_1862_call(relay.reshape(const_3725.astype('float64'), [2, 16])), 1)
call_3726 = relay.TupleGetItem(func_1864_call(relay.reshape(const_3725.astype('float64'), [2, 16])), 1)
bop_3733 = relay.less(var_3720.astype('bool'), relay.reshape(bop_3721.astype('bool'), relay.shape_of(var_3720))) # shape=(1, 14, 16)
func_2613_call = mod.get_global_var('func_2613')
func_2615_call = mutated_mod.get_global_var('func_2615')
call_3750 = relay.TupleGetItem(func_2613_call(), 0)
call_3751 = relay.TupleGetItem(func_2615_call(), 0)
bop_3752 = relay.maximum(bop_3721.astype('float32'), var_3719.astype('float32')) # shape=(1, 14, 16)
uop_3756 = relay.asinh(bop_3752.astype('float64')) # shape=(1, 14, 16)
output = relay.Tuple([call_3724,const_3725,bop_3733,call_3750,uop_3756,])
output2 = relay.Tuple([call_3726,const_3725,bop_3733,call_3751,uop_3756,])
func_3760 = relay.Function([var_3719,var_3720,], output)
mod['func_3760'] = func_3760
mod = relay.transform.InferType()(mod)
mutated_mod['func_3760'] = func_3760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3760_call = mutated_mod.get_global_var('func_3760')
var_3762 = relay.var("var_3762", dtype = "int64", shape = ())#candidate|3762|()|var|int64
var_3763 = relay.var("var_3763", dtype = "int64", shape = (1, 14, 16))#candidate|3763|(1, 14, 16)|var|int64
call_3761 = func_3760_call(var_3762,var_3763,)
output = call_3761
func_3764 = relay.Function([var_3762,var_3763,], output)
mutated_mod['func_3764'] = func_3764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1619_call = mod.get_global_var('func_1619')
func_1620_call = mutated_mod.get_global_var('func_1620')
call_3785 = relay.TupleGetItem(func_1619_call(), 0)
call_3786 = relay.TupleGetItem(func_1620_call(), 0)
output = relay.Tuple([call_3785,])
output2 = relay.Tuple([call_3786,])
func_3789 = relay.Function([], output)
mod['func_3789'] = func_3789
mod = relay.transform.InferType()(mod)
mutated_mod['func_3789'] = func_3789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mutated_mod.get_global_var('func_3789')
call_3790 = func_3789_call()
output = call_3790
func_3791 = relay.Function([], output)
mutated_mod['func_3791'] = func_3791
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3808 = relay.var("var_3808", dtype = "float64", shape = (6, 8, 10))#candidate|3808|(6, 8, 10)|var|float64
uop_3809 = relay.cosh(var_3808.astype('float64')) # shape=(6, 8, 10)
func_2816_call = mod.get_global_var('func_2816')
func_2817_call = mutated_mod.get_global_var('func_2817')
call_3816 = relay.TupleGetItem(func_2816_call(), 3)
call_3817 = relay.TupleGetItem(func_2817_call(), 3)
bop_3829 = relay.not_equal(var_3808.astype('bool'), relay.reshape(uop_3809.astype('bool'), relay.shape_of(var_3808))) # shape=(6, 8, 10)
func_3688_call = mod.get_global_var('func_3688')
func_3689_call = mutated_mod.get_global_var('func_3689')
call_3833 = relay.TupleGetItem(func_3688_call(), 0)
call_3834 = relay.TupleGetItem(func_3689_call(), 0)
const_3835 = relay.const([[[True,False,True,False,False,True,False,False,False,True],[False,True,False,False,False,False,False,False,True,False],[True,False,False,True,False,False,False,True,True,True],[True,False,False,False,True,False,True,True,True,True],[False,True,True,False,True,True,True,True,True,False],[False,False,True,False,True,True,False,True,False,False],[True,True,False,True,True,True,True,True,False,False],[False,False,True,True,True,False,False,False,False,True]],[[False,False,True,True,False,True,False,False,False,False],[False,True,True,True,False,True,False,False,False,True],[False,False,True,False,False,False,False,False,False,False],[False,True,False,True,False,False,False,True,True,True],[True,True,False,True,False,True,False,True,True,False],[False,True,False,True,True,False,False,False,True,False],[False,True,True,True,False,False,True,True,True,False],[False,False,False,False,True,False,True,True,True,False]],[[True,True,False,False,True,True,False,True,True,True],[True,False,False,True,True,True,True,False,False,False],[True,False,False,True,False,False,True,False,True,True],[False,True,False,False,True,True,False,True,False,True],[True,False,True,True,True,False,False,False,True,False],[False,False,False,False,True,True,False,False,True,False],[True,True,True,False,False,False,True,False,True,False],[True,False,False,True,False,True,True,False,True,False]],[[True,True,False,True,True,True,False,False,False,True],[False,True,True,True,True,True,True,True,True,False],[True,False,True,True,True,True,False,True,True,True],[True,False,False,False,False,True,True,False,True,True],[False,True,True,True,False,False,False,True,True,True],[False,False,True,True,True,True,False,True,False,True],[False,True,False,False,True,False,False,True,False,True],[False,False,True,True,True,True,False,True,True,True]],[[False,True,False,False,False,True,True,False,True,True],[True,True,False,True,False,False,True,False,True,False],[True,True,False,False,True,False,False,True,True,True],[False,False,False,False,False,False,False,True,False,True],[False,True,False,False,True,False,False,False,False,True],[False,False,True,True,False,False,True,False,True,False],[True,True,False,True,False,False,True,False,True,True],[True,True,True,True,False,False,False,False,False,False]],[[False,True,False,True,False,True,True,True,True,False],[True,True,True,False,False,True,False,False,True,False],[True,False,True,False,False,True,False,False,False,True],[False,False,False,True,True,False,False,False,True,True],[False,False,False,True,False,True,True,True,True,False],[True,False,True,False,True,True,False,True,True,False],[False,True,False,False,False,True,False,False,True,True],[False,True,False,False,False,False,True,True,True,False]]], dtype = "bool")#candidate|3835|(6, 8, 10)|const|bool
bop_3836 = relay.bitwise_or(bop_3829.astype('int64'), relay.reshape(const_3835.astype('int64'), relay.shape_of(bop_3829))) # shape=(6, 8, 10)
bop_3839 = relay.greater_equal(bop_3836.astype('bool'), relay.reshape(var_3808.astype('bool'), relay.shape_of(bop_3836))) # shape=(6, 8, 10)
uop_3844 = relay.log(bop_3839.astype('float32')) # shape=(6, 8, 10)
bop_3848 = relay.mod(uop_3844.astype('float32'), relay.reshape(uop_3809.astype('float32'), relay.shape_of(uop_3844))) # shape=(6, 8, 10)
func_3416_call = mod.get_global_var('func_3416')
func_3419_call = mutated_mod.get_global_var('func_3419')
var_3852 = relay.var("var_3852", dtype = "uint32", shape = (715,))#candidate|3852|(715,)|var|uint32
call_3851 = relay.TupleGetItem(func_3416_call(relay.reshape(var_3852.astype('uint32'), [11, 13, 5]), relay.reshape(var_3852.astype('uint32'), [11, 13, 5]), ), 0)
call_3853 = relay.TupleGetItem(func_3419_call(relay.reshape(var_3852.astype('uint32'), [11, 13, 5]), relay.reshape(var_3852.astype('uint32'), [11, 13, 5]), ), 0)
var_3857 = relay.var("var_3857", dtype = "float64", shape = (6, 8, 10))#candidate|3857|(6, 8, 10)|var|float64
bop_3858 = relay.right_shift(uop_3809.astype('int64'), relay.reshape(var_3857.astype('int64'), relay.shape_of(uop_3809))) # shape=(6, 8, 10)
func_2230_call = mod.get_global_var('func_2230')
func_2233_call = mutated_mod.get_global_var('func_2233')
call_3861 = relay.TupleGetItem(func_2230_call(relay.reshape(call_3816.astype('int8'), [1573,])), 2)
call_3862 = relay.TupleGetItem(func_2233_call(relay.reshape(call_3816.astype('int8'), [1573,])), 2)
output = relay.Tuple([call_3816,call_3833,bop_3848,call_3851,var_3852,bop_3858,call_3861,])
output2 = relay.Tuple([call_3817,call_3834,bop_3848,call_3853,var_3852,bop_3858,call_3862,])
func_3871 = relay.Function([var_3808,var_3852,var_3857,], output)
mod['func_3871'] = func_3871
mod = relay.transform.InferType()(mod)
mutated_mod['func_3871'] = func_3871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3871_call = mutated_mod.get_global_var('func_3871')
var_3873 = relay.var("var_3873", dtype = "float64", shape = (6, 8, 10))#candidate|3873|(6, 8, 10)|var|float64
var_3874 = relay.var("var_3874", dtype = "uint32", shape = (715,))#candidate|3874|(715,)|var|uint32
var_3875 = relay.var("var_3875", dtype = "float64", shape = (6, 8, 10))#candidate|3875|(6, 8, 10)|var|float64
call_3872 = func_3871_call(var_3873,var_3874,var_3875,)
output = call_3872
func_3876 = relay.Function([var_3873,var_3874,var_3875,], output)
mutated_mod['func_3876'] = func_3876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2842_call = mod.get_global_var('func_2842')
func_2843_call = mutated_mod.get_global_var('func_2843')
call_3885 = func_2842_call()
call_3886 = func_2842_call()
const_3887 = relay.const([[[5.387907,-2.139762,7.556047,-3.827244,-9.270575,-8.313437,3.136907,-6.255264,9.070174,-2.953894,-9.562254,8.851656],[-8.398186,-9.533267,5.945238,-3.190459,-1.189446,9.064659,9.460108,2.679406,9.047107,4.945820,2.602975,-8.171147],[1.883237,1.615262,-2.824883,3.118617,1.712515,1.323955,1.368705,3.727086,-3.994530,1.454444,-8.034417,5.896720],[-5.295848,-4.886467,-8.786748,9.413104,3.139200,-9.959275,1.686254,-0.250574,9.610777,0.450252,5.546062,5.100983],[3.586475,-8.944098,3.889059,1.992071,-7.299176,-7.630383,-9.198267,-3.978613,-6.404867,9.356205,-4.455536,-9.325218],[1.171080,0.157579,-3.473633,-9.355043,9.660564,7.285227,8.789445,2.361651,-5.184895,-5.822874,8.922545,5.212063],[0.349793,7.206058,-9.167263,-5.097499,5.256839,4.094644,-0.080461,-3.204129,-4.775096,-9.087687,-6.690811,0.821446],[9.654502,-1.898441,-2.738220,1.617196,-9.848470,1.148854,-1.651954,3.322001,9.115661,-3.956925,-2.528321,-9.235457]],[[-9.659949,-5.099676,-2.007632,-9.594170,-6.358769,-2.956439,-5.676580,-1.488008,-6.860622,7.842998,2.060824,-9.300710],[1.538278,-3.481547,9.053369,-2.933538,-7.673508,5.119467,-2.007414,-6.919375,-2.922073,0.153707,-2.202213,8.967297],[-3.659976,-6.742326,9.815640,-4.954017,7.082876,7.355551,4.684790,-0.474687,-0.375258,-5.460268,7.305567,4.993903],[5.890837,-3.814901,1.949789,-6.903709,6.183472,3.737696,-3.998306,6.753125,2.676826,-2.295241,9.996769,-1.195565],[-9.953533,-0.765960,6.161481,0.740634,5.290638,1.623366,-6.769371,-1.605039,-5.867375,-2.968080,2.361488,-6.269435],[-9.827073,-4.263107,3.266764,-0.809936,0.558258,-0.827589,-4.520400,-6.649757,2.403149,-6.914821,8.108045,7.256027],[1.950011,-8.500283,-6.270505,6.279222,-2.935422,-0.770762,-0.756393,2.814712,1.462088,-0.907354,-2.687096,8.007189],[-3.162990,9.627975,-0.534224,4.986371,-8.242059,5.582918,-4.487885,-3.885617,-7.978409,4.440622,4.435041,-9.489724]],[[-7.695302,-0.114888,3.968610,-5.317429,-3.370733,-5.578458,6.922170,-7.820338,8.182254,-2.366197,-8.941757,-3.820628],[2.042063,5.565738,6.162043,8.989081,-4.084947,-8.550238,-3.332003,-6.055701,-1.472436,9.224396,-3.672199,0.639224],[5.001432,-4.976334,-7.544069,-2.173617,-3.419894,-1.258444,-0.675837,5.472752,-7.639102,-8.009363,-6.256978,1.218103],[5.200506,-3.670389,-8.259917,-9.278563,7.175783,8.597201,3.640195,0.026169,9.567876,2.432637,-1.812716,-9.042504],[-4.872886,0.660458,7.140030,1.068210,6.181275,9.184204,-0.547826,-4.472481,-4.782458,9.965555,0.666864,9.131420],[4.137850,-4.138923,4.112610,-3.308398,-3.483159,-4.139009,-2.329652,-5.005265,-4.076640,2.645488,9.590856,-0.538503],[0.356346,-1.598523,1.032589,5.658245,-9.524443,-9.019583,-5.473625,-3.457298,-3.710214,5.891454,-8.824156,-6.981716],[2.381061,8.609918,6.742249,-1.662053,-2.222166,-7.218539,-2.296451,-7.684498,4.677248,-7.959569,9.589030,-7.777449]],[[6.878609,-6.739055,-5.445621,-8.790375,-9.249983,-4.970817,-9.142703,-9.631350,4.251326,-3.698551,-8.983606,0.408595],[2.677429,3.997010,-7.869515,-1.846184,1.330497,9.551908,1.358746,1.224170,-4.773487,-9.394678,-9.957793,7.995737],[0.096424,3.733565,-5.158243,5.835940,-6.971806,-3.077203,7.733814,5.485984,1.304890,-2.871958,-4.289417,-9.065157],[0.515664,1.380967,5.927447,-6.137472,-3.497646,-5.586340,-2.181084,-8.129361,-7.144597,0.626919,7.573101,3.767516],[2.261809,-5.340021,2.215185,-1.347541,9.993927,0.323286,-9.894049,6.073172,9.056245,7.001721,9.129592,4.151109],[-0.731706,7.920792,2.693308,-9.539500,-6.041319,-1.313727,9.917649,7.159197,0.387671,7.954293,-4.268131,-1.228170],[-9.412370,1.411763,-7.685502,-8.871851,5.832367,-6.531832,-2.763419,0.572544,8.818541,-8.126493,6.725541,4.647576],[-9.196853,-2.927622,2.922778,0.721064,3.113014,-1.124128,0.797287,-3.806769,-8.403802,9.398633,-9.138754,-4.786542]],[[-5.482725,-0.640674,-8.046171,-5.205964,1.229004,7.779815,-1.744828,-3.364549,0.160220,3.094334,4.779980,2.849282],[-7.209153,-3.759483,8.495283,9.026469,-8.666584,1.039377,7.985306,1.906079,6.493888,-9.847871,0.967194,1.472073],[3.121144,0.255587,-0.582692,-4.062034,1.450284,0.478372,1.089680,7.774717,3.566262,-7.025876,-9.770478,8.362663],[-8.698701,4.306061,-1.961053,-3.219526,5.674285,9.736633,-8.359395,0.957899,-8.249171,8.821057,2.822500,6.272365],[3.185998,4.613558,-7.637256,4.144615,-3.271267,-8.013121,0.662800,-9.987155,6.444740,5.700082,-0.363260,3.259955],[6.749816,-0.556660,1.867358,5.000921,-8.949307,4.707233,5.539598,8.729071,4.399672,1.610801,4.869011,-5.878317],[5.192683,-6.208760,-8.945787,-4.342094,-9.578922,-1.312142,0.232109,9.215890,-9.010033,-5.102108,7.099859,-5.993986],[2.223870,-9.921699,8.934150,3.876381,-1.737464,-3.253284,-3.295165,-0.360862,-7.801215,-0.132032,0.903000,3.467082]],[[-0.270901,1.851022,2.474128,9.316575,4.536814,5.117956,-9.121072,7.174721,7.625572,9.826889,0.175085,-3.515920],[-2.111624,5.937293,-3.665976,4.616426,-4.636343,5.913923,-1.369870,-0.999976,-3.102316,2.655970,4.275133,8.216081],[-5.932623,-9.310527,-4.211475,1.784537,4.847628,-2.921009,9.996838,1.235193,0.150906,-4.724691,3.343037,4.714716],[-2.266673,-7.155396,-4.410969,-9.199452,-9.690129,-9.250526,-0.976895,6.238493,-1.923183,3.920255,9.456406,1.442875],[0.280167,2.793845,-3.727376,-6.310828,8.680784,-7.373936,-4.394653,-5.810882,3.814615,-4.383896,7.001515,-6.216348],[7.466354,1.429803,-0.590956,6.263477,-8.040884,-1.846426,-8.640833,-5.515713,3.407895,4.716633,2.825227,-1.484243],[-2.836292,-2.373829,-6.123339,1.835946,4.166129,-7.771916,5.980264,3.722120,-1.376249,-8.979224,1.275261,-5.638723],[-4.617518,-7.868129,-6.015091,-6.761013,6.445675,-6.208134,4.480510,-5.531095,-0.889300,-8.979733,-6.346528,-0.079455]],[[5.078712,0.337458,6.960458,3.231680,9.100508,4.463502,-5.423777,-8.595607,8.091248,8.608119,-5.446006,4.602123],[1.589840,-2.303693,4.359101,-0.481184,-5.281984,4.457053,-1.907666,2.996682,9.714661,3.055727,-7.364098,5.694699],[-2.866414,9.587503,-6.102205,6.943365,-1.589056,-4.216272,-1.076548,8.774333,-7.027439,-6.896407,3.748089,4.842356],[2.695202,8.184964,-5.147781,3.301193,6.083378,-0.144767,2.106984,1.147476,0.959791,8.058384,0.281448,-9.933003],[-7.013179,-8.233461,-3.503738,-4.691768,-5.511520,-4.278545,-0.828420,3.798393,-4.542002,-3.240246,7.529717,4.212438],[7.975156,3.206464,0.519289,-0.197545,-2.542370,-7.766705,-3.035335,-9.439241,-2.730876,-4.195820,-0.869095,-9.498185],[3.177679,-9.495983,8.004995,5.785938,2.940069,8.269190,5.134120,-1.375712,-0.448629,-4.511929,1.218175,8.613071],[6.826675,-2.740158,1.974179,-0.724977,3.913814,9.192403,2.751877,1.357805,2.267848,2.877177,7.635392,5.543408]],[[-0.230677,-7.318090,-6.824361,5.592364,6.218012,-4.360766,3.115709,7.614969,5.967227,5.961375,-2.133340,0.859127],[9.648887,-0.591085,-6.911577,-7.135403,2.546752,-8.378453,-2.526056,-5.412809,-2.118392,-4.178268,5.783294,-2.829975],[-7.551176,2.606422,7.957851,1.136625,-9.611261,1.333935,9.963622,2.879339,-6.976723,-3.753167,-9.563737,6.957637],[7.561231,-0.760896,7.855450,-6.722932,-1.888332,-2.870847,-1.108921,-2.205077,7.649710,-2.932474,4.353126,-6.786586],[0.718331,-7.667826,8.960145,-6.525710,2.381378,0.754583,-2.609007,-3.656215,-0.624097,-1.726022,-3.155618,3.491756],[-8.879088,-6.850216,7.424465,1.899054,-7.595966,-9.192452,9.758540,-5.261467,7.327766,-1.467741,4.980111,-2.376237],[6.176142,4.765583,0.535519,-0.891251,-0.700142,5.694531,1.540400,-7.157478,-0.446214,4.759065,-5.368965,-4.753929],[5.822929,1.478453,-3.971718,-1.413444,-9.002837,6.645019,-0.807134,2.596877,3.303396,4.893589,5.624880,-4.781126]],[[-8.606927,-0.949514,3.175080,8.683771,7.482992,-9.321264,-2.826641,3.658737,-2.351992,5.339286,-2.602277,8.146692],[5.612585,-1.281100,-3.470417,1.178200,-2.542265,1.201387,-1.558678,2.764869,8.865085,7.404310,-1.471119,-1.307243],[-9.045104,-5.816277,-2.976525,-5.184273,-8.523155,4.447582,6.867273,1.372796,-6.331975,6.063124,1.990576,-7.388926],[-3.223928,7.724702,-1.293030,8.479982,1.595647,-8.209180,9.160482,4.612964,1.912242,5.776491,9.370974,6.480090],[0.956883,2.417710,9.517476,-1.389345,7.310220,-4.889916,2.916989,-2.257070,2.255049,5.623955,8.041498,-7.060743],[6.733419,6.232865,4.640938,-1.784335,-0.596926,0.645715,4.513924,2.913992,8.409659,-5.751020,-2.336666,5.999807],[0.245694,-4.138740,-0.341899,-9.911445,-4.656143,-7.970665,-5.264407,1.479458,-6.324946,-6.543859,-2.198184,8.657773],[7.336095,-1.374271,-3.492135,-7.551780,-3.098833,1.052045,7.733327,-2.141452,7.085831,5.011122,2.803210,-8.578561]],[[-5.662409,2.494948,0.528862,-6.708853,1.906198,-6.336161,7.422576,2.343876,1.622631,-1.078917,-9.089717,1.854707],[8.794100,0.503569,5.875038,3.497944,-5.666626,-2.777545,8.180238,3.772319,7.554431,-5.201121,-7.475711,7.021558],[-8.084507,-3.446202,-7.944473,2.905357,0.183786,5.950360,-6.409185,-1.533888,4.664505,-5.636574,5.104793,3.019048],[8.004046,1.304381,-0.170451,-9.330317,-2.020602,7.603863,-3.700396,0.135859,-9.287076,-2.095065,2.801948,7.480055],[4.276970,2.574173,1.727459,3.211035,-4.034170,-6.992758,1.858403,-2.635629,-1.511275,6.235947,-3.234089,-4.425116],[7.025919,8.920784,6.201310,2.076749,7.216317,7.274241,-0.246650,4.531516,-5.627383,2.801830,-1.660778,0.800672],[2.341787,8.625736,7.806767,-7.539868,-2.048229,0.935174,8.374028,-3.659430,8.241216,2.982891,1.045130,8.740163],[8.571037,2.062968,-7.002996,-6.636441,5.641297,0.911940,6.967044,5.328035,7.218105,4.907487,-7.066071,8.063661]]], dtype = "float32")#candidate|3887|(10, 8, 12)|const|float32
bop_3888 = relay.less_equal(call_3885.astype('bool'), relay.reshape(const_3887.astype('bool'), relay.shape_of(call_3885))) # shape=(10, 8, 12)
bop_3891 = relay.less_equal(call_3886.astype('bool'), relay.reshape(const_3887.astype('bool'), relay.shape_of(call_3886))) # shape=(10, 8, 12)
output = bop_3888
output2 = bop_3891
func_3908 = relay.Function([], output)
mod['func_3908'] = func_3908
mod = relay.transform.InferType()(mod)
output = func_3908()
func_3909 = relay.Function([], output)
mutated_mod['func_3909'] = func_3909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2099_call = mod.get_global_var('func_2099')
func_2101_call = mutated_mod.get_global_var('func_2101')
call_3941 = func_2099_call()
call_3942 = func_2099_call()
output = relay.Tuple([call_3941,])
output2 = relay.Tuple([call_3942,])
func_3948 = relay.Function([], output)
mod['func_3948'] = func_3948
mod = relay.transform.InferType()(mod)
output = func_3948()
func_3949 = relay.Function([], output)
mutated_mod['func_3949'] = func_3949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3562_call = mod.get_global_var('func_3562')
func_3564_call = mutated_mod.get_global_var('func_3564')
call_3957 = relay.TupleGetItem(func_3562_call(), 0)
call_3958 = relay.TupleGetItem(func_3564_call(), 0)
output = call_3957
output2 = call_3958
func_3961 = relay.Function([], output)
mod['func_3961'] = func_3961
mod = relay.transform.InferType()(mod)
output = func_3961()
func_3962 = relay.Function([], output)
mutated_mod['func_3962'] = func_3962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mod.get_global_var('func_2816')
func_2817_call = mutated_mod.get_global_var('func_2817')
call_4199 = relay.TupleGetItem(func_2816_call(), 1)
call_4200 = relay.TupleGetItem(func_2817_call(), 1)
func_2082_call = mod.get_global_var('func_2082')
func_2086_call = mutated_mod.get_global_var('func_2086')
var_4204 = relay.var("var_4204", dtype = "uint64", shape = ())#candidate|4204|()|var|uint64
const_4205 = relay.const([-1,-6,3,2,-2,-10,-10,3,10,-4,-8,9,-7,-2,-4,-3,-1,5,-10,3,10,1,10,4,9,-8,4,-4,8,4,-8,-6,8,4,8,10,-3,-8,4,-6,-1,3,-4,8,5,-4,9,-4,5,2,5,1,-2,4,-10,2,-7,-7,-4,-2,7,1,-10,-10,3,8,6,10,8,-6,6,-10,-5,-3,3,7,3,-5,-5,8,7,-5,-5,2,9,-4,8,-8,-2,-3,8,5,9,6,5,1,-2,-6,1,2,8,5,-1,-10,-5,10,-2,-7,-4,-5,9,-4,2,9,10,5,9,-3,-4,7,-5,-5,1,9,4,-8,-2,3,-2,9,-4,-7,6,-5,-4,-2,-7,-7,-8,8,2,3,8,-10,-8,2,5,3,1,6,10,4,4,8,8,3,1,4,4,10,4,2,-1,-3,-4,-8,6,2,3,-3,5,1,-4,5,-10,7,-7,3,7,10,4,8,2,-1,1,8,-10,3,-3,-9,5,6,9,10,5,7,-8,1,-6,-6,4,2,10,-7,6,-7,4,-3,-3,8,2,9,-2,-1,1,-5,1,1,5,-6,6,1,7,2,8,-7,-5,2,5,6,-3,4,-8,-5,5,-5,-5,10,2,-1,3,-3,-2,-8,8,-4,-4,-5,5,9,-3,10,1,-1,5,-7,8,7,-3,-9,-8,6,-3,-6,2,8,-8,-3,-2,5,-6,4,-2,-6,-3], dtype = "uint64")#candidate|4205|(275,)|const|uint64
var_4206 = relay.var("var_4206", dtype = "int16", shape = (1, 462))#candidate|4206|(1, 462)|var|int16
call_4203 = relay.TupleGetItem(func_2082_call(relay.reshape(var_4204.astype('uint64'), []), relay.reshape(const_4205.astype('uint64'), [11, 5, 5]), relay.reshape(var_4206.astype('int16'), [462,]), ), 2)
call_4207 = relay.TupleGetItem(func_2086_call(relay.reshape(var_4204.astype('uint64'), []), relay.reshape(const_4205.astype('uint64'), [11, 5, 5]), relay.reshape(var_4206.astype('int16'), [462,]), ), 2)
var_4221 = relay.var("var_4221", dtype = "int16", shape = (8, 462))#candidate|4221|(8, 462)|var|int16
bop_4222 = relay.not_equal(var_4206.astype('bool'), var_4221.astype('bool')) # shape=(8, 462)
output = relay.Tuple([call_4199,call_4203,var_4204,const_4205,bop_4222,])
output2 = relay.Tuple([call_4200,call_4207,var_4204,const_4205,bop_4222,])
func_4229 = relay.Function([var_4204,var_4206,var_4221,], output)
mod['func_4229'] = func_4229
mod = relay.transform.InferType()(mod)
mutated_mod['func_4229'] = func_4229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4229_call = mutated_mod.get_global_var('func_4229')
var_4231 = relay.var("var_4231", dtype = "uint64", shape = ())#candidate|4231|()|var|uint64
var_4232 = relay.var("var_4232", dtype = "int16", shape = (1, 462))#candidate|4232|(1, 462)|var|int16
var_4233 = relay.var("var_4233", dtype = "int16", shape = (8, 462))#candidate|4233|(8, 462)|var|int16
call_4230 = func_4229_call(var_4231,var_4232,var_4233,)
output = call_4230
func_4234 = relay.Function([var_4231,var_4232,var_4233,], output)
mutated_mod['func_4234'] = func_4234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2963_call = mod.get_global_var('func_2963')
func_2964_call = mutated_mod.get_global_var('func_2964')
call_4247 = relay.TupleGetItem(func_2963_call(), 0)
call_4248 = relay.TupleGetItem(func_2964_call(), 0)
output = call_4247
output2 = call_4248
func_4276 = relay.Function([], output)
mod['func_4276'] = func_4276
mod = relay.transform.InferType()(mod)
mutated_mod['func_4276'] = func_4276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4276_call = mutated_mod.get_global_var('func_4276')
call_4277 = func_4276_call()
output = call_4277
func_4278 = relay.Function([], output)
mutated_mod['func_4278'] = func_4278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2963_call = mod.get_global_var('func_2963')
func_2964_call = mutated_mod.get_global_var('func_2964')
call_4322 = relay.TupleGetItem(func_2963_call(), 0)
call_4323 = relay.TupleGetItem(func_2964_call(), 0)
output = call_4322
output2 = call_4323
func_4333 = relay.Function([], output)
mod['func_4333'] = func_4333
mod = relay.transform.InferType()(mod)
mutated_mod['func_4333'] = func_4333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4333_call = mutated_mod.get_global_var('func_4333')
call_4334 = func_4333_call()
output = call_4334
func_4335 = relay.Function([], output)
mutated_mod['func_4335'] = func_4335
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4338 = relay.const([[[-1,10,2,5,10,-9],[5,4,3,5,-3,7],[2,-8,-1,10,1,-4],[-10,8,-8,-8,-2,-5],[10,-10,2,8,-3,5],[-1,8,5,-8,8,6],[-2,-3,9,-9,5,-1],[9,3,6,-7,-2,-2],[6,3,5,-2,-4,-1]]], dtype = "uint64")#candidate|4338|(1, 9, 6)|const|uint64
var_4339 = relay.var("var_4339", dtype = "uint64", shape = (16, 9, 6))#candidate|4339|(16, 9, 6)|var|uint64
bop_4340 = relay.left_shift(const_4338.astype('uint64'), var_4339.astype('uint64')) # shape=(16, 9, 6)
func_3908_call = mod.get_global_var('func_3908')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_4344 = func_3908_call()
call_4345 = func_3908_call()
uop_4351 = relay.cosh(var_4339.astype('float32')) # shape=(16, 9, 6)
output = relay.Tuple([bop_4340,call_4344,uop_4351,])
output2 = relay.Tuple([bop_4340,call_4345,uop_4351,])
func_4362 = relay.Function([var_4339,], output)
mod['func_4362'] = func_4362
mod = relay.transform.InferType()(mod)
var_4363 = relay.var("var_4363", dtype = "uint64", shape = (16, 9, 6))#candidate|4363|(16, 9, 6)|var|uint64
output = func_4362(var_4363)
func_4364 = relay.Function([var_4363], output)
mutated_mod['func_4364'] = func_4364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_4368 = relay.TupleGetItem(func_3181_call(), 0)
call_4369 = relay.TupleGetItem(func_3182_call(), 0)
func_774_call = mod.get_global_var('func_774')
func_775_call = mutated_mod.get_global_var('func_775')
call_4377 = relay.TupleGetItem(func_774_call(), 0)
call_4378 = relay.TupleGetItem(func_775_call(), 0)
func_1585_call = mod.get_global_var('func_1585')
func_1586_call = mutated_mod.get_global_var('func_1586')
call_4380 = relay.TupleGetItem(func_1585_call(), 2)
call_4381 = relay.TupleGetItem(func_1586_call(), 2)
output = relay.Tuple([call_4368,call_4377,call_4380,])
output2 = relay.Tuple([call_4369,call_4378,call_4381,])
func_4383 = relay.Function([], output)
mod['func_4383'] = func_4383
mod = relay.transform.InferType()(mod)
output = func_4383()
func_4384 = relay.Function([], output)
mutated_mod['func_4384'] = func_4384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1128_call = mod.get_global_var('func_1128')
func_1129_call = mutated_mod.get_global_var('func_1129')
call_4402 = relay.TupleGetItem(func_1128_call(), 0)
call_4403 = relay.TupleGetItem(func_1129_call(), 0)
func_2468_call = mod.get_global_var('func_2468')
func_2471_call = mutated_mod.get_global_var('func_2471')
const_4411 = relay.const([True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True], dtype = "bool")#candidate|4411|(1183,)|const|bool
call_4410 = relay.TupleGetItem(func_2468_call(relay.reshape(const_4411.astype('bool'), [13, 13, 7])), 1)
call_4412 = relay.TupleGetItem(func_2471_call(relay.reshape(const_4411.astype('bool'), [13, 13, 7])), 1)
func_1168_call = mod.get_global_var('func_1168')
func_1171_call = mutated_mod.get_global_var('func_1171')
var_4420 = relay.var("var_4420", dtype = "float64", shape = (10,))#candidate|4420|(10,)|var|float64
const_4421 = relay.const([4.191736,8.961656,5.039046,1.824508,-4.320042,9.109565,0.298068,-1.810041,6.294896,5.874245,-9.229094,-5.811327,9.161039,-3.811151,-3.630824,-8.323214,2.762842,-8.158536,1.645447,9.129624], dtype = "float64")#candidate|4421|(20,)|const|float64
call_4419 = relay.TupleGetItem(func_1168_call(relay.reshape(var_4420.astype('float64'), [10, 1, 1]), relay.reshape(const_4421.astype('float64'), [10, 2, 1]), ), 1)
call_4422 = relay.TupleGetItem(func_1171_call(relay.reshape(var_4420.astype('float64'), [10, 1, 1]), relay.reshape(const_4421.astype('float64'), [10, 2, 1]), ), 1)
output = relay.Tuple([call_4402,call_4410,const_4411,call_4419,var_4420,const_4421,])
output2 = relay.Tuple([call_4403,call_4412,const_4411,call_4422,var_4420,const_4421,])
func_4425 = relay.Function([var_4420,], output)
mod['func_4425'] = func_4425
mod = relay.transform.InferType()(mod)
var_4426 = relay.var("var_4426", dtype = "float64", shape = (10,))#candidate|4426|(10,)|var|float64
output = func_4425(var_4426)
func_4427 = relay.Function([var_4426], output)
mutated_mod['func_4427'] = func_4427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_4497 = func_3961_call()
call_4498 = func_3961_call()
uop_4504 = relay.cosh(call_4497.astype('float64')) # shape=(10, 8, 12)
uop_4506 = relay.cosh(call_4498.astype('float64')) # shape=(10, 8, 12)
func_2416_call = mod.get_global_var('func_2416')
func_2418_call = mutated_mod.get_global_var('func_2418')
const_4516 = relay.const([[2,-6,5,5,10,-2,-4,-9,-5,7,10,4,-4,6,10,9,-6,-10,-4,8,2,5,8,-8,-8,3,-2,-5,-3,-8,-4,6,3,-4,10,1,1,-9,-1,-10,-2,10,-9,-10,5,-7,8,-1,-9,8,-5,1,-8,-3,-7,-9,-7,5,-1,10,5,-4,-3,4,10,-1,-4,2,-5,10,-9,5,5,2,6,-3,-9,4,4,4]], dtype = "int16")#candidate|4516|(1, 80)|const|int16
call_4515 = relay.TupleGetItem(func_2416_call(relay.reshape(const_4516.astype('int16'), [40, 2])), 0)
call_4517 = relay.TupleGetItem(func_2418_call(relay.reshape(const_4516.astype('int16'), [40, 2])), 0)
bop_4528 = relay.equal(uop_4504.astype('bool'), relay.reshape(call_4497.astype('bool'), relay.shape_of(uop_4504))) # shape=(10, 8, 12)
bop_4531 = relay.equal(uop_4506.astype('bool'), relay.reshape(call_4498.astype('bool'), relay.shape_of(uop_4506))) # shape=(10, 8, 12)
func_3908_call = mod.get_global_var('func_3908')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_4532 = func_3908_call()
call_4533 = func_3908_call()
func_3562_call = mod.get_global_var('func_3562')
func_3564_call = mutated_mod.get_global_var('func_3564')
call_4534 = relay.TupleGetItem(func_3562_call(), 0)
call_4535 = relay.TupleGetItem(func_3564_call(), 0)
func_1982_call = mod.get_global_var('func_1982')
func_1984_call = mutated_mod.get_global_var('func_1984')
call_4536 = func_1982_call()
call_4537 = func_1982_call()
func_1331_call = mod.get_global_var('func_1331')
func_1335_call = mutated_mod.get_global_var('func_1335')
const_4550 = relay.const(False, dtype = "bool")#candidate|4550|()|const|bool
var_4551 = relay.var("var_4551", dtype = "bool", shape = (40, 1))#candidate|4551|(40, 1)|var|bool
const_4552 = relay.const([-1,-6,10,-4,9,1,1,-2,9,7,-7,1,-10,-6,-10,4,10,4,7,-6,7,-10,1,5,3,-9,-5,-2,7,-9,5,-6,3,-4,1,-7,-7,-9,1,10,7,2,10,-7,4,-3,9,-5,-1,-3,8,3,6,-6,7,3,-5,-6,-1,-1,-10,5,6,-4,-10,1,6,5,-5,1,1,6,8,-1,8,3,8,9,-9,-1,9,-7,6,-9,7,5,-3,-1,4,10,-6,1,-5,8,-3,-1,8,9,1,5,5,3,-10,1,-8,7,5,10,8,4,-4,6,-4,-8,-1,3,2,6,-2,-9,7,6,1,4,3,-3,-2,1,-3,10,-3,-4,9,-8,-6,-1,2,-6,3,-4,-9,-5,7,-6,-6,-4,9,3,-7,-9,9,-7,7,-6,5,-9,9,5,10,6,-10,-3,8,7,9,2,7,-9,-5,5,6,-6,7,-1,-5,-1,7,3,9,5,-7,-6,-6,-9,9,-3,-9,10,-10,-1,9,-9,-5,4,-4,2,5,6,-2,-4,-10,-5,-6,4,-7,-3,8,-3,-8,-9,-9,6,8,7,8,10,-8,8,10,-10,-7,-5,6,-8,-6,-7,-7,-9,6,4,9,1,-6,9,-10,-7,3,4,10,6,-10,-3,7,-1,-9,-6,-8,4,-7,-2,-4,-6,10,10,1,-8,-10,-7,2,-9,-4,1,-3,5,-10,7,-9,2,-4,-1,-8,-7,9,-5,-3,-4,-9,-8,-2,4,-4,-5,-5,-2,9,3,2,4,-3,4,3,-4,5,-7,-7,-6,-2,-5,7,-6,-3,-4,9,6,-8,10,10,-6,-6,-9,-5,-7,7,-6,1,3,-2,-9,-6,5,-7,7,-8,2,9,-10,-8,1,-9,2,-2,-6,-3,-7,3,-4,8,-8,6,2,-3,8,-9,1,-8,10,7,6,2,-8,5,5,-3,2,5,5,-6,1,3,-5,-4,-3,-10,10,10,5,2,-1,-3,4,-6,-5,-1,-10,-8,-5,8,3,7,-10,-3,-6,-4,-10,9,6,5,8,8,10,10,6,7,8,5,3,-4,3,-4,-7,-10,-8,2,1,-3,6,10,3,-3,9,10,8,-1,-2,-5,-7,9,10,-3,-3,-3,2,-3,1,8,6,4,-10,6,-9,8,-7,-1,-2,9,-3,-4,-8,-9,-5,-10,5,-6,6,-6,2,-1,4,-8,-8,-10,1,-5,-3,9,1,2,3,2,9,-6,-3], dtype = "int16")#candidate|4552|(462,)|const|int16
call_4549 = relay.TupleGetItem(func_1331_call(relay.reshape(const_4550.astype('bool'), []), relay.reshape(var_4551.astype('bool'), [1, 4, 10]), relay.reshape(const_4552.astype('int16'), [462,]), ), 0)
call_4553 = relay.TupleGetItem(func_1335_call(relay.reshape(const_4550.astype('bool'), []), relay.reshape(var_4551.astype('bool'), [1, 4, 10]), relay.reshape(const_4552.astype('int16'), [462,]), ), 0)
bop_4560 = relay.logical_and(const_4516.astype('bool'), const_4550.astype('bool')) # shape=(1, 80)
bop_4565 = relay.divide(const_4550.astype('float64'), bop_4528.astype('float64')) # shape=(10, 8, 12)
bop_4568 = relay.divide(const_4550.astype('float64'), bop_4531.astype('float64')) # shape=(10, 8, 12)
func_3908_call = mod.get_global_var('func_3908')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_4573 = func_3908_call()
call_4574 = func_3908_call()
output = relay.Tuple([call_4515,call_4532,call_4534,call_4536,call_4549,var_4551,const_4552,bop_4560,bop_4565,call_4573,])
output2 = relay.Tuple([call_4517,call_4533,call_4535,call_4537,call_4553,var_4551,const_4552,bop_4560,bop_4568,call_4574,])
func_4582 = relay.Function([var_4551,], output)
mod['func_4582'] = func_4582
mod = relay.transform.InferType()(mod)
mutated_mod['func_4582'] = func_4582
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4583 = relay.var("var_4583", dtype = "bool", shape = (40, 1))#candidate|4583|(40, 1)|var|bool
func_4582_call = mutated_mod.get_global_var('func_4582')
call_4584 = func_4582_call(var_4583)
output = call_4584
func_4585 = relay.Function([var_4583], output)
mutated_mod['func_4585'] = func_4585
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4614 = relay.var("var_4614", dtype = "float32", shape = (9, 2, 16))#candidate|4614|(9, 2, 16)|var|float32
uop_4615 = relay.sqrt(var_4614.astype('float32')) # shape=(9, 2, 16)
func_3456_call = mod.get_global_var('func_3456')
func_3458_call = mutated_mod.get_global_var('func_3458')
const_4618 = relay.const([7,1,10,6,-8,4,-5,7,5,-8,-6,-2,6,-2,2,-10,-5,-8,2,4,-8,3,-5,3,-10,-4,3,-3,-10,6,8,2,6,10,-6,10,-3,9,3,9,-2,10,-7,-8,9,10,7,-1,-3,-5,-5,5,9,-7,8,8,9,7,2,-4,9,-8,-7,1,2,-9,2,7,1,-4,10,-1,1,-2,3,-3,1,1,2,7,10,3,1,-3,-5,-1,10,-1,-10,-3,-10,-9,10,8,2,8,-3,-3,-4,-9,5,2,-4,6,8,10,6,9,-7,-9,-6,10,9,-6,-2,-2,6,4,-6,5,2,2,-5,5,1,3,-1,7,-8,3,-9,-9,-8,7,5,-8,7,4,-2,-6,-3,8,-1,3,9,9,10,3,1,2,9,-5,-9,-10,8,-1,4,4,-6,7,3,-3,6,-3,-3,-4,-4,-3,-8,3,9,-8,5,10,-10,-9,5,-10,-8,-9,-7,-7,2,3,3,9,-1,-6,-10,10,-5,5,-2,2,-7,3,4,4,-2,-5,4,-6,10,1,-10,1,9,7,8,-3,10,8,8,7,2,4,7,-3,1,8,5,9,3,7,-7,8,-6,1,-2,-3,-2,10,-4,8,-7,9,4,-5,-5,-2,-1,-10,-9,-1,9,5,1,-3,-8,-2,-7,-4,10,10,2,-6,4,-1,6,4,-8,-9,4,-3,4,7,8,-2,3,-4,6,1,5,-3,-6,6,-7,2,-6,-8,-2,-2,6,-1,-8,5,4,-3,8,9,4,7,-10,-7,-5,7,-7,2,-4,4,7,-3,-3,-1,2,-4,-5,2,-3,-4,-1,8,1,-3,2,-7,7,1,8,-3,-1,-1,-10,-4,9,1,-10,-9,-10,7,2,-2,-6,10,-4,6,-10,2,9,4,3,-7,-6,-5,3,-2,-6,5,-9,5,8,9,-8,1,-6,-5,-10,-3,3,7,-7,-10,-3,-4,1,-6,-1,-10,-7,-6,4,3,6,-2,-3,2,6,-5,-10,-3,-8,-2,5,8,3,-4,-5,-2,-4,-7,-3,-1,4,10,-4,-5,-6,-1,-8,-5,-3,7,10,1,4,-3,9,-6,7,-5,2,5,-6,1,7,3,8,2,-1,-10,-8,-2,6,-10,-5,-5,-6,7,1,5,7,-10,10,-1,-2,6,5,-1,-5,3,7,-8,-10,-6,-6,-1,-9,-8,-4,9,-3,7,10,-8,-8,-6,-10,-9,-3,5,6,-4], dtype = "int16")#candidate|4618|(462,)|const|int16
call_4617 = relay.TupleGetItem(func_3456_call(relay.reshape(const_4618.astype('int16'), [462,])), 4)
call_4619 = relay.TupleGetItem(func_3458_call(relay.reshape(const_4618.astype('int16'), [462,])), 4)
func_3669_call = mod.get_global_var('func_3669')
func_3671_call = mutated_mod.get_global_var('func_3671')
call_4629 = func_3669_call(relay.reshape(call_4617.astype('float32'), [10, 8, 12]))
call_4630 = func_3669_call(relay.reshape(call_4617.astype('float32'), [10, 8, 12]))
output = relay.Tuple([uop_4615,call_4617,const_4618,call_4629,])
output2 = relay.Tuple([uop_4615,call_4619,const_4618,call_4630,])
func_4635 = relay.Function([var_4614,], output)
mod['func_4635'] = func_4635
mod = relay.transform.InferType()(mod)
var_4636 = relay.var("var_4636", dtype = "float32", shape = (9, 2, 16))#candidate|4636|(9, 2, 16)|var|float32
output = func_4635(var_4636)
func_4637 = relay.Function([var_4636], output)
mutated_mod['func_4637'] = func_4637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3322_call = mod.get_global_var('func_3322')
func_3323_call = mutated_mod.get_global_var('func_3323')
call_4644 = relay.TupleGetItem(func_3322_call(), 1)
call_4645 = relay.TupleGetItem(func_3323_call(), 1)
output = relay.Tuple([call_4644,])
output2 = relay.Tuple([call_4645,])
func_4657 = relay.Function([], output)
mod['func_4657'] = func_4657
mod = relay.transform.InferType()(mod)
output = func_4657()
func_4658 = relay.Function([], output)
mutated_mod['func_4658'] = func_4658
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4659 = relay.var("var_4659", dtype = "float64", shape = (12, 14, 13))#candidate|4659|(12, 14, 13)|var|float64
uop_4660 = relay.asinh(var_4659.astype('float64')) # shape=(12, 14, 13)
uop_4666 = relay.sigmoid(var_4659.astype('float64')) # shape=(12, 14, 13)
output = relay.Tuple([uop_4660,uop_4666,])
output2 = relay.Tuple([uop_4660,uop_4666,])
func_4668 = relay.Function([var_4659,], output)
mod['func_4668'] = func_4668
mod = relay.transform.InferType()(mod)
mutated_mod['func_4668'] = func_4668
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4669 = relay.var("var_4669", dtype = "float64", shape = (12, 14, 13))#candidate|4669|(12, 14, 13)|var|float64
func_4668_call = mutated_mod.get_global_var('func_4668')
call_4670 = func_4668_call(var_4669)
output = call_4670
func_4671 = relay.Function([var_4669], output)
mutated_mod['func_4671'] = func_4671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_818_call = mod.get_global_var('func_818')
func_819_call = mutated_mod.get_global_var('func_819')
call_4745 = relay.TupleGetItem(func_818_call(), 0)
call_4746 = relay.TupleGetItem(func_819_call(), 0)
output = relay.Tuple([call_4745,])
output2 = relay.Tuple([call_4746,])
func_4759 = relay.Function([], output)
mod['func_4759'] = func_4759
mod = relay.transform.InferType()(mod)
mutated_mod['func_4759'] = func_4759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4759_call = mutated_mod.get_global_var('func_4759')
call_4760 = func_4759_call()
output = call_4760
func_4761 = relay.Function([], output)
mutated_mod['func_4761'] = func_4761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1253_call = mod.get_global_var('func_1253')
func_1255_call = mutated_mod.get_global_var('func_1255')
call_4786 = relay.TupleGetItem(func_1253_call(), 0)
call_4787 = relay.TupleGetItem(func_1255_call(), 0)
func_4668_call = mod.get_global_var('func_4668')
func_4671_call = mutated_mod.get_global_var('func_4671')
const_4789 = relay.const([-5.395925,7.747457,2.562541,9.805149,4.452087,0.597979,-8.045543,-9.796183,3.368149,1.612868,-0.479228,-5.077906,4.336234,9.921701,5.828099,-2.272298,7.219067,0.694073,-6.123458,-8.229066,0.963671,1.087958,9.692397,0.883983,-9.310448,2.748789,-1.578827,-9.227825,6.883804,-5.869678,-7.343191,9.206800,4.473493,8.169815,9.288132,4.148829,7.851592,-6.260274,-0.015967,3.690336,-7.883738,7.245798,8.212379,-8.259107,-9.159618,2.525964,-2.681125,-0.492528,7.453065,2.341671,8.121936,6.529871,-7.087350,0.155322,2.332256,7.907278,7.428475,5.505648,-5.888477,-1.915168,-2.911361,4.608545,-8.087420,-8.523764,1.326196,-3.339872,-5.363544,4.365936,3.691747,-4.335113,-5.412205,9.904942,-2.989228,-9.354021,-2.764630,3.458533,-4.901378,4.631907,-6.233237,-6.368123,-0.545070,-5.709746,-0.020958,4.618587,-5.024049,-9.352460,2.927427,2.395918,-0.856163,-4.125175,-8.649503,-4.418251,-1.717883,5.249488,8.452573,9.394758,-7.380100,2.453199,0.679564,-5.684963,-7.019799,-9.730033,-8.451113,8.050483,2.088330,-6.085151,-3.806620,-7.084798,-7.105643,3.015376,1.436477,5.970157,8.252513,-9.704849,7.971267,-7.037758,-0.042473,6.571721,-0.038884,0.890745,-5.620449,0.524317,-2.624673,-7.366233,0.618112,6.671840,-8.363397,-0.713815,1.412036,-9.482942,-5.916910,-6.522002,-5.427257,1.152589,-8.154674,-0.416836,-5.954150,1.489893,-3.345045,-6.058159,-0.984700,-3.420907,-1.213152,-5.785304,-2.137687,8.376016,6.567751,2.448156,7.093994,4.161542,7.543176,5.520975,0.069495,0.253082,-5.468735,-1.106380,1.490183,4.051428,8.780383,9.649136,-8.489825,-8.445598,-6.578473,7.235549,9.621607,0.869738,6.606700,-3.647481,-9.074490,-6.611477,9.613198,4.089679,5.740308,1.844533,-3.849505,-1.703200,2.395957,-5.346484,-1.362707,2.930347,-4.115383,4.113428,2.966499,0.992571,1.314142,-9.538512,-2.060732,2.041045,-4.694801,-2.073290,2.386291,-8.009955,-5.508927,-3.586442,-6.553822,-5.340290,-0.622456,-1.088643,4.791935,5.886876,6.332073,-1.956920,1.282285,-9.229219,-0.587030,-8.949571,0.518018,-7.781597,-6.618489,1.131178,-4.092551,6.767093,6.276166,5.425637,9.035954,4.369076,-2.238664,-8.455996,0.205663,-1.820003,-1.329534,4.337453,1.420139,3.496917,-1.182795,-4.478292,-0.172429,5.213271,-6.409319,-4.540132,-4.815823,-5.128353,6.509857,-6.629887,7.664690,-7.284400,-5.331607,-8.400910,4.476143,5.439725,-5.223526,9.848894,8.999979,-5.911396,9.417970,-0.990269,-9.875102,-6.690187,6.263696,-3.304754,6.351810,-0.184647,-0.798708,5.719104,-2.928373,3.881278,4.838881,8.170055,2.213283,-8.539586,6.876226,-1.629023,3.137315,8.417537,-2.329084,-0.848970,3.125983,8.952613,9.418538,7.780062,1.961423,-4.967570,2.308660,4.294872,7.655989,5.002189,-7.627010,-0.048262,2.742833,6.910783,3.090159,7.254727,-1.911326,-9.199314,-6.845526,-6.995321,-8.051709,-6.506594,-5.897030,-0.866994,2.549818,-2.178820,-7.434882,7.268552,5.439088,0.724444,-4.238270,8.841319,3.038448,-8.014815,7.061388,3.918729,1.433449,-0.152373,4.061870,1.170876,-4.405123,5.021403,-9.073891,-0.839541,1.451220,-3.508630,0.033402,-8.352284,9.930389,-8.972933,2.894498,-9.548578,7.340371,7.408912,-1.026647,4.794635,-6.779031,6.060604,5.660658,-7.800178,6.873428,1.487750,-9.943631,3.065582,-4.479525,2.902910,0.842581,4.068569,-1.662763,8.747983,1.413461,9.277623,9.991520,0.718368,2.802199,5.093380,-5.753790,8.790084,7.340101,3.718176,-9.837889,3.419939,-0.969465,-9.923690,2.801941,2.091747,-0.696226,8.820280,2.250077,-5.381142,-3.349667,6.916465,-8.994747,-2.003887,5.087448,-2.807063,-4.122180,8.732543,-1.899830,9.008329,-1.319476,-7.921044,9.685665,-6.064269,-0.361016,0.591503,7.930683,-5.879020,2.111709,8.875280,-0.888112,-0.045186,4.034270,6.269184,7.511720,-0.184656,-3.300752,-2.508541,-0.179527,-9.560913,-1.127087,8.832306,6.260653,6.815952,-5.619672,7.450988,-1.086291,1.018585,-1.333049,0.675310,8.549947,1.093439,6.111850,-3.295565,-2.568061,-4.541254,-0.649811,-8.715196,0.042548,9.916670,-8.815355,-2.886565,-4.022711,4.466236,2.976622,9.677618,-0.594524,-8.790958,-7.906133,9.583212,0.685036,8.941771,5.129302,3.589075,-9.953579,5.216587,-8.485457,0.488408,5.562777,5.393793,-6.224718,-8.128738,8.736761,-3.979074,7.629060,-5.817499,3.940253,-1.476868,-4.460778,-5.721096,-9.559315,7.275279,9.384678,-8.833596,6.519944,7.151241,-6.710989,-3.019156,-4.728051,0.563810,-1.790349,1.151250,-1.357927,3.133915,2.024372,6.667897,8.955915,-5.085639,3.497672,8.982076,-8.741856,-5.840951,-2.711282,-5.304807,3.144257,-2.840110,-8.994840,-2.654909,-5.877312,9.703532,7.355859,9.476775,2.889280,4.408659,-1.726247,-2.447338,-0.352029,5.072164,2.498297,7.096481,-2.662649,6.534996,6.199932,3.439951,5.409701,-9.145589,8.056320,4.464516,5.734288,0.056010,7.798469,8.027931,2.906913,4.888810,-8.547854,2.068004,-7.712546,2.191605,-5.424600,3.827115,6.842345,-9.905281,-3.560398,-6.088797,7.522659,9.149721,9.577759,-5.426110,-1.595472,6.799720,-5.232482,3.447712,1.832473,7.209389,1.739130,7.003939,-1.391857,3.375680,7.940271,-4.350857,7.879782,-9.153327,-1.076666,8.425143,-4.955032,-5.906293,-4.990764,5.892764,-9.384150,4.638244,-7.667505,4.384294,0.125834,8.670640,-5.215749,9.510093,4.995345,-8.457534,-1.781954,-8.841699,-0.399307,3.772004,-5.812613,8.460175,4.836350,-3.514960,5.131551,-3.922740,-8.680406,-2.812387,-8.438503,7.116947,6.115904,7.419782,5.340204,-4.839846,-4.098225,-0.203663,-6.402755,-6.136700,2.993919,7.592027,-3.990034,7.706388,8.987867,7.351510,1.800789,-1.542142,-4.159560,-0.020831,0.934722,8.539872,-3.015076,0.385136,5.407158,8.948837,-7.931138,-4.500574,-5.404759,-6.751324,3.997922,9.727068,-1.041737,9.918938,-7.048627,-3.119960,-0.826857,5.834800,-6.297175,8.627937,-9.248759,-5.635246,-1.342045,8.119521,-7.024555,-1.842920,2.288216,-7.225797,5.287918,-4.330052,5.081048,-3.880331,4.263709,-7.823154,-3.362094,5.784044,-5.001108,9.835055,-4.362044,-7.940371,-3.866498,-1.808347,-5.024666,8.011007,-5.944610,2.603426,6.022837,8.182954,-5.195946,-0.344912,-5.084222,1.634907,8.134172,7.075346,-8.645356,-4.120068,-1.679172,-6.941278,7.012604,2.429914,-1.918053,2.878704,-9.673743,-3.590015,-6.644144,5.204010,-6.895145,-1.860716,1.433806,-9.254308,5.368570,1.813679,2.885754,-8.573335,4.935787,9.393944,7.168387,3.339676,7.892230,-5.991625,-4.556378,-1.902938,-3.110160,-8.720636,-6.102153,6.550088,1.885983,-7.443928,3.139023,1.587966,-2.340612,-2.890681,2.582118,4.224223,9.976488,3.572796,1.395568,-2.099292,-5.995944,9.854293,1.074459,-4.179041,6.994036,-5.198566,9.441802,-2.119979,-4.507030,6.334345,-7.627602,-1.594866,-8.466096,-8.494267,-8.034066,-9.520551,0.001679,3.009393,-0.079751,-4.007892,-1.900975,-0.637890,-3.949854,4.118318,3.987192,4.270163,1.756474,8.443150,8.170545,9.368273,3.966138,-1.888589,-1.821267,2.255841,4.224151,-5.265311,-2.940205,5.740398,2.519494,9.071763,-8.833640,5.571333,0.930761,0.128722,-4.894103,-5.538336,-4.587962,-1.591643,-2.851193,-7.073484,1.890174,-4.764254,2.962747,6.210460,-9.467112,-3.365914,1.351525,6.214386,-2.507517,3.845040,5.510668,-4.924338,-7.164106,-1.454609,8.811365,-6.946050,-0.431919,-5.405248,-2.286342,-6.755470,9.749081,3.895543,-1.802711,3.247388,-0.419922,6.453002,-5.017695,0.807122,8.216906,8.074594,-5.927358,6.402766,-8.383920,9.486288,9.501542,-3.041196,-7.912527,1.810328,-4.432855,2.288045,3.662240,-0.834019,7.042437,-1.468356,-8.417726,3.440970,7.791848,0.818510,-4.607458,7.691760,-6.553103,-1.303123,8.902263,-7.941252,-6.156038,-4.129856,-1.300766,5.356693,8.451349,-8.730289,-7.018658,-6.082144,2.196562,8.730352,-2.087227,0.701209,-0.797580,8.161629,-8.768091,0.502196,-2.531082,-0.985584,6.515732,-7.095002,-4.769393,-0.476612,-0.571303,-4.415061,-9.867176,6.381047,-6.412514,2.122405,3.260554,5.064779,-8.497580,-9.631334,-1.018130,-8.789972,7.419990,-6.147365,5.034268,-8.090787,-6.805228,5.239371,-6.884005,7.862606,-8.690917,-0.112410,-4.371164,7.609230,-1.802778,4.657316,-8.953782,-7.724316,-8.558547,1.941917,9.159702,8.994463,1.169241,-2.511818,6.838263,-1.970573,7.429589,6.911170,-3.837892,-4.770697,7.109416,-2.432992,2.262116,8.209573,1.322954,-9.255737,-1.323518,-3.112695,-7.776644,9.691811,4.726365,5.021808,-8.590570,-4.768818,3.722970,-1.290349,-7.460820,3.431887,0.643833,2.578495,5.067106,-7.026043,5.545264,2.715565,9.800646,1.615437,2.170182,1.874098,-0.282555,-6.248390,1.447202,-3.057969,9.747483,1.484210,-5.948580,-9.672398,-6.847696,7.117694,2.009954,-8.760500,0.204514,5.069887,-6.231158,8.628051,-0.028035,8.735493,-1.553754,6.909583,1.722711,-5.824910,4.882552,8.973833,3.931977,4.754620,-9.426179,-2.670581,-6.348858,-2.905989,-1.714345,3.838551,9.463647,-9.849020,-5.720220,-9.719038,5.586566,9.251328,9.727566,-2.466645,5.137071,4.453364,7.922484,1.636812,-0.878948,7.439557,4.966802,0.564451,4.588218,-5.697932,-6.395990,4.910563,-7.655162,-9.484357,9.853024,-4.742215,4.247766,-8.449724,7.022120,-0.729115,6.506922,8.643095,-5.992562,-2.251498,-3.387356,6.377897,2.161160,-0.849379,8.691058,2.832379,-5.194894,5.719198,2.618453,-2.039418,9.183222,-1.232737,-1.380292,-8.660618,6.276105,-7.604215,2.863200,-2.064456,-1.807630,-9.227487,6.409334,8.525559,-7.696402,7.813406,-2.072838,-8.307304,-3.467979,5.582311,-8.181288,8.297236,-8.192797,-9.466224,5.325094,-2.175966,2.427859,1.471196,-3.981943,-0.928822,6.577945,-3.073356,-7.337947,-5.499371,-6.620684,8.201467,8.259429,-0.282778,1.726662,9.607885,5.970593,-8.185777,1.790989,4.758656,-6.673367,-6.460705,-6.503804,-1.689220,9.299457,6.677427,-6.728612,1.315947,-8.897832,9.829541,-1.837424,-0.894905,-5.499272,-0.547936,2.342027,2.140971,-7.292377,0.874877,-0.134195,7.477322,-9.218580,6.524283,8.416905,-8.694548,-4.190081,6.521805,2.033548,-5.183625,9.449366,5.316057,2.529863,-3.690849,-9.585537,-8.781394,8.680656,-2.265895,-4.870941,-6.923902,-9.199154,5.783426,-8.022543,1.163435,3.817574,5.901779,1.274160,4.586544,4.677879,-1.679312,6.210848,6.992585,-3.572863,1.307920,4.297473,-5.821917,-8.075631,4.975663,9.524815,-0.805501,-9.050265,8.280718,-0.205646,-0.288615,-2.090976,8.063517,4.997810,3.247890,0.821095,9.550324,-4.543249,-1.511954,8.982269,-1.404229,0.013047,7.691401,-5.500118,2.749843,6.075622,6.122893,-1.221655,-1.171536,1.180823,4.241955,-6.614440,5.090493,-9.228722,9.484617,0.291159,-2.912120,8.844774,9.607796,-3.801007,-9.118121,-0.954674,-4.676470,3.080068,9.443545,-5.188238,8.192682,8.538069,8.897155,-3.263304,7.421000,-4.894677,-3.381382,-7.640449,-1.354637,-8.013771,-3.472802,-2.663330,0.596012,1.267690,-9.283638,9.131009,-7.256271,-6.039171,5.366795,5.298534,0.786066,-0.378834,1.298352,1.143422,-7.247521,-3.941166,-0.629540,6.780098,-3.200284,-2.607463,-3.603302,-8.622795,-2.131407,-4.771645,-3.044342,4.626004,-8.876800,9.869761,-5.089987,5.929940,8.689426,5.114182,-5.582010,2.973161,-3.138353,7.681953,-7.504431,9.377220,-0.133697,-5.662486,3.323803,-4.061122,0.722821,6.520262,-4.512390,-8.111679,8.485090,-8.079050,-0.052830,-7.707651,7.825778,2.764407,-8.232200,1.731210,6.067948,5.082463,2.044706,-3.665388,7.637556,-0.852824,-3.652271,7.683908,-7.498816,4.115258,-5.567924,1.905872,1.752505,1.911458,-2.379624,-6.731729,-6.198643,-5.307440,-8.631905,-6.931266,8.953836,6.132968,-0.290818,5.907494,-6.201769,7.049071,-9.903856,3.978381,-7.655901,4.360912,2.742526,-2.048232,2.696991,9.271443,5.733607,-7.157168,-4.988079,-9.024674,-8.779833,3.524399,-3.707459,5.668893,-6.683604,-4.694664,8.741308,5.197102,2.713002,-7.421468,-8.648673,-2.835101,-1.200091,-1.031803,7.519936,3.198051,-7.661276,-2.058368,9.927120,-9.051604,-6.725039,-0.723718,-3.293352,-1.251465,0.617703,6.340519,-4.614020,8.381789,-1.013066,6.625084,-2.632823,7.328951,-3.861944,3.735484,-0.674272,5.509525,-3.521144,-8.904495,2.202665,9.265240,-8.939548,-3.566763,-8.539578,2.313833,-5.339958,-9.159547,6.331900,8.493430,-4.774363,3.489653,-8.406632,0.709313,4.568257,-1.073560,1.251900,4.711914,-8.887554,-4.097998,-7.941281,2.913688,2.951677,4.530430,9.240702,-2.576970,-6.192526,-0.292072,-6.563879,8.248277,-1.990133,-5.526879,7.876079,1.525765,7.880874,9.503355,2.255900,-0.107384,-0.229704,7.860896,8.850251,7.499623,0.351170,-8.656283,-6.059443,8.860558,7.244393,-0.757258,-2.976879,-4.484835,6.186858,1.784540,-1.494985,6.310375,2.634884,9.748873,-3.901283,-8.762954,-4.834574,9.657643,6.075372,4.570132,-7.818718,7.909462,7.229664,5.276878,3.724089,6.274818,-0.698546,5.588730,0.445320,-2.122226,7.749004,-8.920932,-7.312113,-2.456576,-2.199611,-7.666805,5.465233,2.346999,-8.982482,-9.930637,8.248024,2.726213,-7.774963,-5.481410,7.513196,-9.584229,0.988290,8.321773,-3.231397,5.839382,1.944147,-8.543546,-9.372323,-8.126782,-8.441533,-2.938407,-0.578289,9.969169,-3.537873,2.034055,3.824918,8.961881,-9.729004,-8.564292,-0.878834,5.359585,2.052255,6.015449,-3.604375,-3.157631,-1.136189,-5.616894,9.756478,2.168489,5.529433,8.813154,-5.315715,-9.755467,3.040712,-0.411000,-0.862760,-6.677077,2.993943,4.725069,9.190958,-9.476670,8.309438,-3.873915,-9.467780,-4.505217,-5.879031,-6.441867,-4.159820,7.271591,8.170700,-0.652730,-6.633434,-1.395321,-0.346615,9.729476,2.876924,7.921764,-4.928761,7.943740,9.841265,9.247725,-3.455130,6.350240,-4.640350,-1.173895,-0.059617,7.308568,6.997143,-2.662619,-6.086817,1.947130,1.123255,-0.191076,8.609757,-7.698226,2.090555,-4.958795,-4.901366,6.085142,0.422347,-4.221302,-6.764812,-4.318263,8.829883,9.100584,-8.042700,-7.433296,2.140066,7.141507,-2.734607,4.733826,5.820076,1.479662,7.627886,-8.348361,2.916191,-7.373993,1.543230,5.898060,3.867195,-4.979911,-0.801187,3.185954,1.650263,-1.793534,6.414910,5.513056,9.698215,-3.288234,8.660269,0.588739,4.581896,-8.643150,-6.490317,-5.469848,-6.720963,7.773163,7.261098,-6.253556,-4.523168,-9.518462,0.776058,-7.239380,2.655000,6.939306,-7.187744,9.923570,7.918567,-7.739643,9.489671,9.207940,9.430346,-9.521664,-8.627640,3.743808,0.387923,-5.323666,7.608236,-5.362101,8.285170,-0.921394,-9.599360,4.064691,5.441764,-6.324350,-2.893222,5.182596,-3.585614,-1.633125,-0.281132,8.172550,-8.335735,-8.874561,4.955631,-5.396790,0.846558,-5.110507,-8.225065,8.121117,4.937839,-4.272596,0.096291,9.369734,-1.618715,-9.061895,4.746621,-2.271921,2.249279,8.197027,8.122877,1.374295,-2.565694,4.247201,-5.562690,1.092777,-8.170469,7.826049,5.242988,0.011698,5.045419,-2.993719,-4.579631,-5.520923,-8.801738,-5.303664,4.228453,-1.942873,6.508173,-2.829608,-2.936003,9.984759,5.532711,-7.159761,0.095030,-0.750121,-0.576649,9.814678,-0.958594,-6.863196,3.067217,-4.582146,2.335239,5.201720,-8.240031,-4.324453,2.273644,5.079171,-4.291633,6.946467,-1.150874,-8.119797,-0.525797,3.439755,3.335893,3.750740,-8.048582,0.665057,-4.113005,-2.413259,-9.789401,2.609692,-0.976920,1.779121,8.309194,-9.455371,-6.007278,-4.784491,-9.531794,9.319146,6.170833,-3.640459,5.462116,8.586763,-0.457280,-7.488331,-2.078242,-9.041604,6.329079,-3.853800,-3.124917,-0.433862,7.913637,-6.712980,-6.084902,-1.692982,-2.874662,8.913226,-4.336409,-3.390083,-4.258318,-9.825407,-9.323134,6.341220,-2.556155,-6.349610,-3.326240,6.564504,6.732767,3.371989,-3.702328,-7.238115,-9.658295,-7.977349,-0.095383,-4.104464,1.656132,-4.596279,3.383755,9.893099,8.349955,7.272398,-6.930047,4.862883,-3.874327,4.548424,-1.385046,8.029297,8.193885,-4.719396,-4.999555,-6.432652,3.383740,-2.986144,-9.576489,-5.632695,0.991474,3.209380,-1.081460,-1.617026,6.850153,7.300711,4.998287,2.595336,-2.486549,-7.380161,-9.669016,1.965757,7.159633,-9.031660,0.027694,2.753081,-2.312870,0.854217,-6.594369,8.421815,8.559222,4.244822,-3.964062,-2.458717,-1.337281,4.465991,8.625430,-1.993239,-4.312050,1.528456,7.478959,6.034851,9.228685,5.780322,-1.668755,-8.262019,4.089136,-1.375680,-1.587582,2.530313,0.067015,1.709059,3.137110,-0.362888,-4.280078,5.456246,-5.222384,-2.384286,6.455462,5.081511,-7.765006,-5.033853,-0.568783,7.452846,9.220585,9.909814,-0.005182,7.710455,0.245427,9.039669,1.724819,9.344492,8.613282,-9.629101,2.230772,-7.986922,7.352117,-2.899879,9.277625,-5.837198,-3.008167,-2.461074,-7.967928,-0.338008,0.127250,9.196822,-4.821182,-9.956234,-9.025217,0.367425,2.035375,-9.215570,-7.141845,-3.808764,-5.556547,-3.152794,-7.839968,2.271756,-7.881644,-2.742683,-5.469192,4.750798,1.390408,-1.376886,-2.001774,3.336224,-8.444996,-0.796176,-1.628750,-8.099659,7.718437,7.369066,9.941138,-8.205195,-9.737385,6.449168,-4.253358,-9.145411,5.377942,-0.260004,-8.791394,5.658323,8.907302,8.849469,-0.153192,-5.619920,-3.604850,3.715897,6.193894,7.885954,4.763165,-9.000787,1.402229,8.372826,2.244490,-4.668973,4.354248,-8.139288,5.169754,3.653087,-5.864991,2.901112,0.459153,-0.594964,-5.504731,5.269950,4.927807,-3.624978,-3.811800,1.931424,7.016883,9.275116,3.533020,1.730963,9.262527,-4.715298,-1.792910,-9.791884,-4.817609,-6.798461,-8.034315,-8.760692,7.938815,2.812445,-7.777447,-9.614986,-3.079452,9.830840,1.432950,6.426964,4.225252,-3.942778,1.277077,4.139508,-3.466001,8.913797,4.239865,-1.247778,-9.763950,-5.004160,-0.155320,-8.265633,-4.063109,-3.245730,-5.802786,-3.320359,2.973762,3.670302,4.924481,-7.163711,5.568685,8.156583,-6.941711,0.052137,5.680372,4.510026,-2.567587,-7.859274,1.431998,7.908501,-7.335774,7.308165,-5.268259,9.577156,-0.380493,2.945531,6.361536,-0.053746,-9.367644,-5.041418,-6.472504,4.762019,6.349700,9.156396,-8.303426,-3.564777,3.832372,-3.708980,-0.686831,4.830105,-8.789392,-2.896492,0.943784,4.490549,9.806890,8.139124,9.314286,-7.025825,9.689589,-3.408671,-9.232079,-3.638167,-0.169477,-5.023587,-3.178185,7.676898,-5.673536,-0.569301,7.282363,-7.382948,7.060195,-6.507275,-0.024505,3.292203,-7.806655,-4.929396,-8.829554,-7.914588,0.547113,-5.936493,2.164105,-6.066730,4.479609,0.950064,-6.196676,1.342407,-2.449523,8.657256,7.781889,-1.440688,-1.707344,-6.410422,3.376912,6.967969,1.752060,2.378132,-8.282386,6.960706,-7.583144,-4.565815,-0.297841,3.969813,0.898269,7.318091,4.352294,-8.615945,-1.410978,1.608458,-8.419341,1.128485,-7.586054,-9.057429,-0.756950,-3.734797,-4.481785,-3.470643,0.865059,0.370965,-8.807907,4.002228,-1.110625,3.654052,-9.411423,5.892398,9.086559,7.894930,1.950926,-7.569625,7.763861,-7.657137,2.753520,-3.898409,-7.538492,0.403597,-3.992452,3.091764,2.289651,-3.288925,6.687989,-2.443464,-6.269368,-5.001326,0.256097,2.988170,3.439001,-1.792969,-9.950240,4.375146,2.968514,3.651219,4.871343,-3.553635,4.342333,6.977820,-9.407973,-3.834703,0.200629,-7.523349,1.580970,9.174689,-4.482687,-2.078243,-1.151843,0.964306,-1.909885,9.034163,3.430151,-3.141091,-8.191862,3.864131,8.166319,5.380954,-6.514796,8.124553,-3.632215,2.094336,7.059019,8.919595,3.424258,2.899675,-3.572444,-4.696522,-5.532176,-2.254099,-5.790719,-7.776691,7.186794,-7.159055,7.720607,-5.799483,-0.820523,-1.055894,2.825979,7.216943,7.758402,-9.214416,0.717404,5.145665,-9.594592,1.219112,-0.337459,-3.931735,7.883725,6.349006,4.128850,-3.863984,0.130935,1.404482,6.485781,-6.187426,1.118909,-0.566206,1.123805,-8.182871,7.733292,-6.476557,6.520952,-8.119348,7.046546,-5.093536,0.890375,-8.692777,2.198689,4.489056,-9.768563,0.868137,-3.365453,-4.918089,-9.487058,2.025204,-0.742689,3.439640,2.509996,9.343036,9.474012,3.508651,-1.081109,-0.267140,6.177002,-8.150389,0.777124,9.901988,2.171455,0.983064,-4.650552,-2.465080,-2.707919,8.446295,1.023072,-4.530382,-8.394976,2.969285,0.868206,-2.094961,0.343644,-7.133247,6.173764,-2.966416,5.317832,-3.698589,1.269025,5.612000,-6.173568,1.609207,5.131241,-9.604893,3.391227,-7.936177,5.552905,1.603193,-5.209406,7.779781,5.241037,-5.721500,8.897000,-2.792037,8.077547,-5.679116,-5.867935,7.433726,9.545715,4.609245,7.403372,1.405314,0.464451,1.545642,-0.965388,0.237903,1.830124,0.873757,-7.650521,9.976360,6.731675,3.190645,7.751793,9.720917,-2.515925,7.350688,-0.251739,5.530908,6.062739,4.233658,3.672328,8.306775,5.744031,-6.095683,-4.368355,6.867588,2.850903,-8.913782,-9.940088,-1.496346,-7.461203,-4.126961,-5.801055,-1.857458,5.339161,-3.601787,-4.281977,6.222038,-4.033839,7.030188,3.309150,-4.430053,2.194232,1.197760,-6.427828,4.426277,8.543005,7.891201,0.922764,7.015520,-3.365192,4.528873,6.420000,-5.289107,-6.814382,-1.007304,-3.465086,9.261306,3.125048,6.145948,-8.225972,2.535185,0.425008,2.011960,-3.654128,4.611367,-4.194326,-4.937402,7.114776,0.008633,-5.627934,6.160676,-1.245830,0.961788,9.377243,5.995544,6.027637,0.779311,-1.590797,4.551150,5.623990,8.084741,0.353700,5.806567,-3.986725,7.487066,-3.440544,7.031838,1.910035,3.955953,-7.459953,-6.444280,1.625155,-9.095120,-5.108924,-7.884319,-2.354456,-2.316950,5.113566,-0.867367,-9.957140,5.031004,-4.661047,-9.951673,1.214351,-0.590746,-4.649457,5.597809,-6.597829,9.070736,0.783592,-8.070536,0.706158,9.956064,-1.658042,-2.796278,0.744502,1.999866,0.317768,8.019005,5.858284,-8.610310,-5.329818,3.897676,9.648909,-9.457419,0.292125,-8.613065,1.234442,5.035367,5.491611,-9.532126,7.904058,-7.036062,4.053657,7.859297,5.867267,0.969765,3.751493,-4.869563,8.353360,7.686552,4.357645,-8.767874,-1.542449,-4.740344,3.946623,-3.378089,-2.599914,6.136604,4.605198,9.308868,-8.570758,-6.197604,4.622456,-2.669699,4.447181,6.579067,7.312406], dtype = "float64")#candidate|4789|(2184,)|const|float64
call_4788 = relay.TupleGetItem(func_4668_call(relay.reshape(const_4789.astype('float64'), [12, 14, 13])), 0)
call_4790 = relay.TupleGetItem(func_4671_call(relay.reshape(const_4789.astype('float64'), [12, 14, 13])), 0)
func_2118_call = mod.get_global_var('func_2118')
func_2120_call = mutated_mod.get_global_var('func_2120')
call_4805 = relay.TupleGetItem(func_2118_call(), 1)
call_4806 = relay.TupleGetItem(func_2120_call(), 1)
func_1060_call = mod.get_global_var('func_1060')
func_1062_call = mutated_mod.get_global_var('func_1062')
const_4808 = relay.const([-1,2,-10,-10,10,4,-6,4,-2,-5,2,2,-8,9,4,-9,-4,8,-5,-10,10,3,-2,5,10,2,-5,-9,9,-3,7,-9,-5,4,7,-7,6,5,8,2,2,-1,-6,-10,-8,1,8,-6,-9,3,4,3,3,-8,9,-3,3,10,6,-8,6,10,9,5,6,-2,-1,10,6,-6,-9,-10,3,-4,9,-3,-1,-8,-1,-8,4,-9,8,8,-9,-1,-3,3,-10,-7,10,5,-5,4,6,6,2,5,-5,4,-9,-4,-5,-10,-7,3,7,1,-8,9,-6,6,-10,-8,7,-1,-6,-9,-6,-3,6,-10,-1,-4,-5,5,-9,9,-5,4,-8,6,-4,4,-4,2,-4,-2,3,-6,-10,-8,-5,8,-6,9,1,-8,2,4,-3,-7,-9,2,6,8,10,-9,-7,-2,-1,-6,10,-9,8,-2,2,-7,-10,-2,-6,6,-10,-10,2,-7,7,-7,-7,-9,2,7,-3,-4,3,1,6,-7,10,3,-1,7,4,-3,10,8,-5,7,-9,-1,7,-2,-9,9,-6,3,3,-3,4,7,-2,-8,-10,-5,6,-1,-1,-5,-4,2,-7,9,-3,-6,-10,10,8,9,3,-6,3,9,2,4,8,-8,-9,6,1,8,5,-5,8,-10,9,9,3,6,3,3,-6,-8,-10,-8,4,-2,5,-1,-1,-3,7,2,1,-7,-10,6,3,-2,8,-4,5,1,-3,-3,5,5,-10,-4,-7,-5,-3,-2,7,-9,-3,7,-9,7,3,6,-10,10,10,-2,6,5,-10,-6,-2,-10,-6,-2,-7,6,-3,-8,5,-4,3,-5,3,8,8,10,7,-6,9,9,-9,6,1,-4,3,3,-3,-4,-10,-10,6,-10,-2,-9,4,-6,7,4,5,4,7,-3,8,5,-2,6,-8,5,3,-10,-4,-2,8,6,-6,-9,-10,3,4,3,4,-7,6,-2,-6,7,-9,-10,7,-10,8,7,-4,3,-8,-5,8,5,-4,4,-1,9,-4,-9,-6,-5,8,4,4,-1,6,5,10,7,-8,3,3,-1,2,7,9,-4,-6,1,6,4,-2,5,10,-7,4,-10,-3,-4,-3,2,-7,-10,-7,-4,-5,-4,-7,10,-2,8,6,-2,2,-3,-9,6,-3,8,9,2,10,2,8,5,-10,3,2,4,-3,9,-2,-7,-1,-7,-9,-4,-7,-4,-2,-5,1,-8,-5,-5,9,-10,8,8], dtype = "int16")#candidate|4808|(462,)|const|int16
call_4807 = relay.TupleGetItem(func_1060_call(relay.reshape(const_4808.astype('int16'), [462,])), 0)
call_4809 = relay.TupleGetItem(func_1062_call(relay.reshape(const_4808.astype('int16'), [462,])), 0)
const_4819 = relay.const([[[3.863702,5.062761,3.362947,1.686753,-9.144803,9.323338,6.275299,-2.920818,3.493993,7.645401,-4.383538,4.740934,-3.020413],[-5.291343,-6.042425,-9.477494,5.855189,-4.453134,6.865018,2.760185,4.370495,7.251246,-1.102355,2.643024,-9.191481,-8.042094],[8.639825,0.825881,-1.738954,-5.186823,8.451226,-4.822517,3.510743,-6.143332,9.792957,-4.112053,-4.064963,3.076637,8.745045],[-1.527817,-6.341114,3.006606,5.814519,4.286947,-1.697844,-5.560618,3.048580,1.760507,0.570084,4.208102,8.634463,8.635218],[-3.379244,-3.583132,5.140036,4.074503,3.388224,2.930440,6.607850,5.717427,4.937193,7.074621,-0.837845,5.022418,-4.948734],[-0.978396,-4.229178,5.964375,2.481875,-0.027510,5.168082,-5.812860,-8.821492,9.143920,-6.208211,-9.463558,-9.787373,-0.015418],[-1.244886,6.371520,5.029204,-9.969281,2.046248,-1.818464,3.966475,-6.803396,-6.602479,4.315071,-0.733532,-2.307740,7.336153],[-7.109642,-7.522287,7.300122,-8.604743,-9.716622,-0.976378,8.349967,-8.424468,-3.428454,6.653533,-4.203188,1.184846,-8.560938],[-7.386746,5.255941,4.699192,-5.293441,-4.595024,-5.763279,-8.769526,-3.751554,9.197825,-7.341914,3.174960,5.161161,9.213834],[-4.640207,-0.133307,1.810511,3.643294,-4.290986,-6.477337,2.139554,-5.159092,-5.727100,-7.583389,-9.492384,-5.722525,9.820550],[2.797270,-4.730883,2.941790,-7.785387,-5.211570,-0.218495,-4.312410,-4.561450,3.277433,7.950371,-0.694485,-8.561034,1.913285],[-3.187998,-8.205278,7.453999,1.587765,-3.130388,8.420714,-5.503237,-1.909653,1.772407,6.182844,-8.634497,6.046381,1.272061],[2.539143,-1.135852,-0.826697,-0.567449,9.016334,-1.699393,-4.290927,5.328955,4.662268,0.666403,-3.686148,-6.254177,-2.857740],[4.067520,0.641964,2.566715,-0.937821,2.243205,1.685022,6.598344,7.221661,4.418258,1.285039,0.628299,-6.503693,-3.054757]],[[-8.275854,-3.957371,2.993489,-2.239324,-7.186380,4.107572,-9.783137,0.521127,8.733479,-2.710788,7.091551,-7.286436,-2.072174],[1.473863,-1.601452,0.293280,7.447540,8.760927,5.796409,0.572638,-7.140310,2.842578,3.930694,-6.476247,6.282812,6.266308],[-3.609223,5.700509,-2.418265,1.166905,6.040689,6.894967,-1.042770,7.233430,-7.208605,-6.278774,-8.437638,3.659633,-0.346017],[-5.756444,-9.592121,-3.954504,8.715232,5.002450,4.249153,-3.477950,-0.770853,4.854921,-2.118061,-3.173423,0.954746,6.163975],[-1.941909,7.323825,-8.981142,5.332783,0.785089,7.361466,4.782390,-2.088545,7.871322,9.545042,-8.029089,3.206120,-8.456569],[-0.391217,-0.966866,8.875330,-0.275272,9.887416,-5.904803,-8.381419,4.421620,-4.672688,-2.822239,3.105826,1.742855,4.601326],[2.634809,-7.088899,0.892096,2.383536,9.657855,-8.930784,0.451253,-6.420810,-1.276021,7.558228,6.368558,0.769014,0.240251],[2.913326,3.539567,-9.692139,0.288954,-6.236571,7.316508,-1.093853,-7.441626,3.757908,2.792658,0.084671,-5.096417,5.498979],[-5.892945,7.903399,0.122094,-5.901370,-2.316673,3.041807,-3.754924,-7.878299,5.503558,-4.504426,4.352659,0.126383,9.997954],[4.275175,0.142694,9.291985,0.748607,2.199805,-4.244897,0.495661,1.454875,-6.342990,8.997946,2.238813,-6.165667,-8.260744],[0.511481,-2.335756,0.687065,-6.168758,-4.419594,-0.122053,1.966976,-6.370472,-5.903677,-3.338687,-8.113766,5.890839,0.227928],[-3.441005,-7.316778,9.294662,-4.396089,-7.634230,4.344217,-2.374050,2.299094,2.327512,5.079472,-2.588861,-6.814640,6.106363],[1.613581,-4.397646,6.841322,-4.732133,4.261885,-7.687728,2.121189,4.133651,9.076658,-2.746240,9.468621,9.467653,4.475661],[-7.946906,-5.231795,-3.865220,-9.980539,-0.752047,3.593568,9.521685,1.442761,-3.169250,-5.035030,0.573536,-0.080606,-5.939034]],[[-0.873109,-5.647483,9.761319,8.373724,-0.029359,-0.520937,-9.463924,-9.543336,8.222684,-7.288208,5.219713,-9.151265,7.805257],[-5.056990,5.767128,9.622922,-7.557872,-1.740528,-2.334055,-5.990913,6.647187,4.879996,5.806556,-6.756060,5.220762,0.095517],[8.199954,-1.292073,-0.134338,-2.078115,-4.551826,0.021941,1.510188,-0.985608,8.818003,-2.506262,8.176969,-9.263275,-3.748585],[-2.533136,1.026520,-1.316661,4.773585,6.080271,9.797007,1.305840,7.949831,7.157847,-7.686948,-7.209660,-4.158287,6.521567],[-4.098232,-8.076167,-4.734902,-3.569733,2.173642,-4.291726,-2.085752,-5.139169,-7.241499,2.028623,-0.652963,-0.742439,-9.073950],[-9.426247,-0.806996,0.639105,9.125846,4.385128,-9.120793,8.385635,-9.215480,-0.403141,-1.920828,8.929013,-6.452736,-4.468514],[7.835919,-2.244985,-4.262368,-2.149501,-8.199458,1.637422,1.373449,4.902372,3.978318,3.713246,-7.565585,-4.852461,-1.110751],[8.280818,-6.981804,4.952694,3.229446,3.766480,-0.295712,-5.945092,3.886701,-8.215377,-3.472150,-4.251973,4.035889,2.725137],[6.271739,-5.614289,7.352214,6.741533,9.291335,8.952247,-4.897691,-5.225684,-9.438788,7.853789,2.941557,2.489792,9.225362],[6.244505,6.177330,-7.493591,-4.486736,7.463839,3.053549,4.276398,1.333811,2.275518,5.848970,8.827968,-6.011460,-5.384017],[-4.116461,7.727638,2.226184,-9.179634,0.337198,-4.289713,7.389450,-1.214215,-2.687243,-0.212217,-3.144236,9.046644,7.176678],[-3.751082,3.157516,1.819843,-5.131794,2.422605,8.913274,-8.589340,-0.252306,-8.383757,-3.425470,-7.974122,-0.495088,1.586507],[-0.380642,4.749814,0.505501,3.542415,-5.892819,-7.570036,3.577780,-3.224997,-7.321514,-7.232601,2.228010,-8.029170,3.298450],[-0.207778,9.097886,-6.042176,-5.675720,-0.622931,4.091116,-0.658833,-8.791925,-4.784745,-4.871015,4.989502,-2.512431,-8.486143]],[[-6.864357,6.816953,3.709218,-1.702896,5.836913,6.730737,-1.192416,6.247600,2.271040,1.707918,8.115438,-3.459116,-7.076039],[-2.739889,1.854404,0.959957,7.800762,6.339141,-4.549825,-0.715134,-2.337739,-2.250644,4.170834,8.098234,0.148920,-3.061230],[-7.256038,0.826152,-8.998000,1.849793,-8.565446,-9.130624,-8.865211,-6.706479,2.623487,-9.323780,-1.696501,-3.977974,1.402999],[7.723872,-0.428174,6.585792,-0.809025,0.697714,-6.752092,-2.964223,2.628687,-0.804420,-9.883645,7.300843,0.882176,3.208898],[-6.475246,6.816145,2.029327,-6.937738,7.335504,8.058567,-0.719767,-8.756287,6.581522,6.671879,1.165432,-9.133320,3.935034],[7.608784,-9.630848,-1.007255,-1.731902,-2.921049,-6.819421,6.591368,-6.999781,6.139186,-6.149458,9.906526,-5.494933,-4.051022],[-6.148999,1.857060,-2.822584,5.175610,-5.395124,8.169425,3.897889,-4.285210,4.044690,9.296650,-2.640565,-0.054718,0.238383],[8.710056,6.498329,1.737760,-1.774221,1.216737,-5.689143,4.283865,-0.174640,5.473282,-5.426099,-3.789304,-2.581391,1.758799],[-3.606345,7.482975,9.002539,-2.039918,-3.722969,1.827578,-6.550304,-9.290071,3.249290,4.016503,-3.441553,2.551428,9.968178],[-8.259079,-1.833521,-1.691834,-0.376834,-1.068886,-7.818217,-1.757719,-9.219489,-9.206831,-3.581709,9.119283,-6.848805,3.857583],[-3.286237,-6.187959,-4.016694,1.794823,-4.227795,-2.421406,8.508853,1.016401,8.483030,-9.058923,6.241745,-9.388287,1.145011],[3.511957,0.441848,0.913787,5.563790,6.008117,-9.156718,-8.309820,-0.292273,8.943367,7.342818,-4.016868,-3.675066,2.950934],[1.860873,3.096017,8.610216,-8.578678,-1.207259,-4.598692,3.615406,9.277373,-7.966585,7.782435,-6.851598,-5.207378,2.564681],[-8.117220,-9.825741,2.037927,-9.988984,-4.457862,6.373197,-2.490749,-5.809025,1.569778,-1.932190,-6.489308,7.843453,9.404174]],[[-0.510619,8.167266,-1.968659,-2.635351,7.039818,-0.470972,-0.792917,-7.280355,-4.249578,0.640678,9.405258,-9.660432,-3.578227],[6.124172,-7.108998,6.360211,-1.020966,-5.719522,0.594762,6.459052,-7.460219,-0.791556,8.131433,-7.861714,7.439475,-8.163550],[1.139963,-0.382096,7.735392,8.104271,-8.948922,8.412187,8.225144,-1.853294,-6.282003,-3.829950,3.128414,4.372483,0.439896],[-5.260029,-8.245263,8.584916,-2.547343,8.021990,9.787543,6.922885,1.886666,4.492823,5.802982,7.226381,6.773870,-1.475128],[-0.660246,0.247079,-7.285580,-9.515547,0.416320,-4.876860,2.763528,1.803104,-0.209449,2.132559,3.182945,-5.905092,-4.821194],[-9.616422,1.288899,-5.587570,3.778793,8.148071,-6.735592,-6.040697,-7.441630,0.341586,-5.201881,-4.832147,0.056162,-0.103495],[-9.644095,7.845451,7.993255,1.218366,6.027746,-8.539011,7.149135,-9.367675,-7.533764,5.103525,3.235503,-8.962172,-7.030792],[-9.180073,-5.656728,-1.171023,5.397232,5.527771,-9.378960,-6.431895,7.472669,-9.569682,-4.015222,-7.580283,9.563882,9.748938],[-7.506433,-8.132791,4.816678,-1.495005,2.932080,-5.471326,1.050928,2.181305,-1.862847,7.255803,1.695637,4.296073,-6.653446],[-1.063188,0.576831,-5.023960,6.638194,-8.731916,4.445148,6.271506,-9.711149,6.800089,1.601976,6.457073,-0.125417,8.373493],[-2.042187,-1.221467,-6.066663,-8.531123,-4.448123,2.668430,0.145340,-1.003415,6.111831,1.000253,-8.330270,6.940715,-0.222006],[7.016633,3.834920,-9.689992,6.901301,-3.086740,3.271556,-4.000279,6.582042,6.116397,0.263765,5.769880,0.738613,-8.556664],[8.311429,-0.219472,-2.031002,4.323707,-5.073803,3.926862,-4.236841,-9.812885,-1.101338,8.783650,-9.321567,-4.596203,2.018392],[-9.860283,2.724438,-9.004998,-2.439373,-0.779624,-1.346584,-0.603200,8.554075,2.885267,5.021074,0.089512,-6.796797,0.078283]],[[0.768751,-6.613010,9.491839,-6.362622,-0.197337,-5.742013,8.686310,6.669962,-3.495664,-0.316959,-6.285388,2.455342,5.445238],[3.333650,4.068182,3.462968,4.147352,5.802710,-1.630367,2.518437,-1.511398,-0.578624,-2.091114,-2.390611,2.406858,-0.607228],[-2.183676,-6.053021,-3.529372,8.208964,-8.389671,-6.655891,-6.365414,3.808612,2.428375,5.571638,-1.500871,9.355367,-1.147708],[8.867214,4.762145,8.115287,7.416194,0.927614,3.256160,1.713663,3.938655,6.379578,-0.031978,6.406456,2.877668,1.954796],[-2.651409,-7.083413,-1.873686,-3.235142,9.831636,9.770020,9.425553,-7.387516,1.946985,1.889827,-5.592357,2.076493,4.761882],[-4.331086,2.016093,-4.289674,9.492013,-4.770778,-8.825579,6.741841,-2.412426,-7.994707,6.593309,4.468652,-4.253597,-4.190194],[7.126564,9.612377,-6.493546,-4.750761,-5.055837,7.481651,9.223704,5.164314,-0.005793,-0.908796,-0.431031,7.644243,3.339454],[-8.560274,5.510919,-2.139037,-9.610075,3.475249,-3.196499,5.780891,-3.674146,-4.566599,-9.549921,7.723867,-8.788586,-1.760525],[-4.150418,-1.333972,-8.397916,0.255348,4.986615,-6.760381,-8.866450,-6.322435,7.856427,3.926552,-9.041986,-6.205685,6.523400],[-8.098406,2.613956,-8.745003,-4.618076,9.985997,-4.400181,-8.099196,8.850047,2.095913,-9.401833,-3.235027,9.891404,4.554821],[4.674348,8.217468,4.441036,-1.173496,-9.101081,-5.590893,3.672646,8.939007,-9.521110,-3.411374,-2.698434,4.818144,8.937578],[0.784855,0.031489,2.343629,-6.045619,-3.619383,-5.905981,-9.441351,0.399868,4.629210,-4.293377,-2.785452,-6.370203,-6.538188],[7.590715,5.490128,3.944877,9.536054,5.518243,8.851166,9.087623,7.802437,-5.371554,-5.448408,-1.927308,9.305815,-3.220965],[8.276681,-5.866245,-2.341757,-0.092681,-2.533769,-6.385455,-6.431907,-2.162248,4.763810,7.056683,9.942701,-8.205060,-6.840481]],[[4.124406,6.295195,7.584680,-1.907123,7.985039,5.188886,-4.373135,5.439677,-1.207646,-4.857204,-6.951063,-5.731408,-8.240136],[1.498964,-1.165767,9.362609,3.434302,3.374265,-9.807285,-1.716940,-4.477318,6.404867,-6.763419,0.585566,-8.495587,6.756493],[6.785668,0.314696,-6.782524,-9.776742,-1.619135,-9.588105,3.236446,-1.400050,-5.077635,0.148501,7.097861,3.070809,6.073858],[-9.684312,5.490136,-6.627065,5.036632,-9.731890,0.973360,-6.498234,7.502440,4.188848,0.902145,-6.723662,1.044811,-3.804320],[-2.045632,-8.529649,9.566840,2.505255,-7.105116,8.155709,3.574074,3.403334,2.576213,-7.930011,7.430020,0.083878,-3.457620],[-5.010480,7.208616,-8.285341,-4.177196,4.844008,0.019177,-0.316243,6.176182,5.176363,-1.792644,8.606339,2.720699,-3.006699],[4.932313,0.172520,4.595248,3.881711,-6.092857,-2.167641,-8.016423,-0.718468,-8.390369,-8.967232,3.097741,8.895118,-4.205645],[4.856284,-7.666964,-2.776601,0.553853,8.482079,4.896441,4.683717,-9.589028,9.264185,5.617189,-7.436292,-7.583602,1.635126],[2.487310,6.302743,8.121971,6.727689,-9.333422,-6.732552,8.228935,-0.215858,-0.471791,-2.223998,5.124716,-5.735987,-3.103426],[3.459602,5.936507,-4.010814,9.911141,-7.400318,-1.701490,-4.766995,-7.271363,-4.045720,8.867768,-8.957082,-1.634601,-9.941230],[-7.755787,-8.390528,-9.430266,-3.573553,4.371687,-7.501326,-4.936824,5.746478,-1.859834,-1.161414,-4.983308,-0.339917,3.670340],[-9.615670,9.977815,-0.444862,8.844657,-6.061101,-3.501860,2.929070,3.317532,-5.399938,-8.319209,-4.000096,9.770738,7.030579],[0.445620,9.501102,5.864662,-9.383860,7.308839,-0.468180,-6.936222,-8.189040,1.943657,-8.758686,3.510543,0.434965,-6.142272],[-3.961780,-5.069047,-9.143656,5.771815,-5.716630,5.923308,8.879662,6.939144,6.677427,7.799635,-8.632929,9.356822,1.787878]],[[0.830310,-6.815184,7.865437,-7.920960,4.445748,2.703173,-8.622262,5.361044,2.241866,-9.193965,-3.095181,-7.918109,8.109662],[2.455967,9.735652,0.977762,9.219173,-9.630704,-9.166524,-4.413875,1.248362,-5.902159,6.350743,0.327874,7.512757,-3.555543],[5.253765,0.362687,5.712144,6.334226,3.222014,-4.282212,0.126226,0.043134,1.210991,1.919612,-6.952103,-5.995928,9.940812],[-9.035579,-7.288579,-7.135283,1.989187,-3.674233,-3.842338,1.714910,0.805823,-1.368937,-9.005325,-5.454085,5.597551,3.261649],[-9.754454,-9.927407,6.105909,-4.319251,1.276257,-3.639731,-9.756016,3.329194,-2.329586,-8.204297,-5.732461,-4.225322,0.157831],[-9.574008,-7.396853,-9.840132,-0.882605,-3.210089,2.372901,0.560776,-9.353123,5.925691,-0.972759,1.914967,6.146964,-3.315995],[9.478658,-3.839516,-6.265566,9.728638,-9.887473,2.782580,-1.612508,0.304010,-0.792683,-7.642085,-5.975527,7.564485,5.021584],[7.890090,-3.659692,-0.189006,6.849285,-7.482153,-0.011459,-1.569896,6.947631,5.953482,-1.176745,6.427292,9.742921,5.443190],[7.051141,-2.046394,6.015682,6.416183,-0.201610,5.123607,6.652624,2.842623,-0.268011,-1.259914,3.765202,6.777880,-0.845602],[-2.254984,2.718700,1.978647,-7.375200,6.667429,-7.826332,7.648770,-9.030960,-3.111534,5.859238,9.102685,1.909588,7.931167],[5.444269,-9.294021,-5.024761,9.406235,-0.326694,-7.877110,5.472670,8.087435,8.639832,-4.848108,6.128464,8.597665,-5.316783],[-4.780245,-3.327822,-4.035037,4.157454,-8.288776,0.711628,3.861543,-9.009289,-2.992029,2.027067,3.919936,-7.594814,-8.480300],[-8.741895,-2.550482,4.319483,5.325119,6.285657,4.561223,-7.790458,-5.092521,-7.541318,-2.315887,9.646233,-1.645219,-2.028727],[5.893019,4.071811,-5.901418,2.182874,-8.478647,-0.203680,6.562612,0.558942,-3.027672,-7.401525,5.388681,-8.556631,6.101996]],[[-1.404446,-3.797143,-1.231479,4.504024,6.015812,0.339669,6.232506,5.520146,0.696864,7.436361,-5.819834,5.427502,-3.777713],[4.450735,-4.934958,-9.883181,-9.329436,6.370524,4.981357,-1.167671,-5.544698,9.492388,1.189350,5.109229,7.807638,1.131161],[-7.729870,-9.957475,9.501558,8.022426,1.590592,-4.778040,-9.514761,-6.910637,-6.243483,4.963840,-0.984403,-8.583658,2.582375],[6.890953,-6.360544,-2.209521,2.805478,5.111508,-9.395816,-7.598894,6.657572,7.490497,-3.205428,8.235780,-1.210325,3.591779],[5.540358,-1.619988,-9.050886,-8.711747,-0.755199,0.754473,6.819830,-6.668912,-8.889580,4.921496,9.705109,6.846207,-8.395773],[1.562920,3.973194,-9.449368,-0.719969,-9.962299,-8.562140,-4.933361,4.269674,-4.571791,-4.598089,8.421641,4.771070,-6.428319],[2.177128,-4.431279,-5.640013,8.170852,-6.009168,7.478155,-5.230672,3.017537,-2.003355,-4.063857,-7.098725,-4.125058,9.006510],[8.739811,5.121653,-5.231215,4.677152,-4.929419,-4.878586,-8.884626,9.234269,8.628446,5.201507,-1.988289,-6.351739,2.131020],[7.365502,-1.952879,7.018192,1.107402,7.936053,-8.960836,-6.108004,3.626994,-6.450555,-0.020932,9.852891,6.660803,-0.569473],[-2.465274,-0.851079,8.576914,0.219392,4.194746,4.335657,8.836130,-1.455460,-3.255364,1.076617,9.754049,0.442655,2.410956],[1.310398,4.172059,9.591030,8.957749,4.056871,2.300549,-1.624691,-0.112758,-0.803962,-4.945584,6.353540,7.301067,-7.570053],[-9.262813,-4.475134,-7.451368,-0.671964,-6.208370,8.998704,-4.541514,-6.086609,-7.764719,-8.586546,4.540588,-0.878124,6.981906],[-9.127339,-6.930966,4.885847,-7.662094,5.517648,8.777014,-3.833138,6.072305,8.042209,-3.765767,2.281682,-9.369051,3.406942],[-7.369701,-5.275762,1.482877,0.316957,9.528706,-8.421409,-9.300420,6.147433,-1.119309,0.077697,3.316955,0.908516,8.786542]],[[-5.315878,-1.310478,3.675190,-3.922007,-2.218547,-8.086860,5.325198,-5.559388,6.289138,4.889733,-8.203793,-1.387617,5.910686],[7.657763,4.078045,-2.653010,-0.488513,-3.398912,7.185424,5.334323,-4.164792,4.387680,-2.791071,-8.958489,8.377546,-6.373579],[8.784712,2.824482,-3.997301,5.071800,1.521065,-1.624058,-0.571182,7.844396,7.016231,5.880417,-7.249022,4.976803,-3.188483],[-6.686732,-2.948175,7.190145,6.732508,-9.365620,6.853758,-6.096346,5.515689,6.607140,3.295116,-6.509860,3.556640,-1.307429],[-6.534419,-6.876789,9.605964,-7.949561,0.616235,9.488567,9.441048,1.410253,4.485252,4.122609,-1.135375,-6.896214,-6.513056],[-4.464655,-6.772979,1.886568,-8.819974,0.709936,1.989841,1.567940,-0.946485,2.073085,5.773822,-3.933458,-2.040921,6.600523],[-0.338073,-7.676952,-7.955469,8.693884,-5.402025,-4.197974,-7.206331,-4.850095,5.295095,4.882333,2.386242,7.467602,8.103978],[6.056641,-9.968599,-2.333512,4.857419,2.355062,0.621160,-6.529846,9.271418,-3.546969,4.412263,4.381064,9.378466,-8.877242],[-1.165239,0.560276,0.965479,6.085792,9.836940,4.999808,4.340193,6.347597,9.075569,-1.492660,-0.109223,-8.123025,1.168893],[-5.108847,-4.402764,8.223782,6.549046,-5.584737,-5.256995,-9.013047,2.089108,-6.687287,-3.664147,8.461023,0.541756,-9.780824],[7.238517,3.996618,0.387138,7.794267,-5.137667,-5.589294,2.602144,0.418573,-1.920672,0.827468,3.192534,-5.710506,0.123598],[9.277679,8.274673,-3.762381,-9.305893,-6.550847,-6.652575,-1.835560,-8.242709,-0.811751,6.170778,2.623178,0.101925,-1.171800],[-9.817440,-8.393130,-3.295738,7.004949,2.733448,-2.487303,2.758724,4.747820,-9.281919,3.576692,-0.616710,-8.490559,5.786552],[-5.549353,9.316208,2.372896,6.833371,9.541711,9.065040,-6.177111,6.031310,-8.811382,2.308575,-2.802969,0.056845,-9.614885]],[[9.224594,-3.374651,5.045114,1.458716,9.501263,-2.311432,-5.043960,-2.729310,-6.343027,-0.073874,-9.607436,8.926384,5.181019],[0.306065,8.444512,-5.798339,5.713379,6.275301,6.376391,9.514004,1.740009,-0.298324,0.995482,1.255227,0.934226,9.791041],[-7.752514,7.572039,-3.044282,5.408778,-2.813832,-6.730271,-1.182825,-7.831455,-6.386746,-9.272734,-0.893409,4.811181,5.294907],[7.211707,4.759463,-7.608076,1.156544,9.720534,8.192701,2.093643,-3.626239,5.592016,5.521400,7.425412,9.950820,4.945820],[-0.867236,0.825484,0.869720,-9.876035,-2.801070,3.649763,-3.037524,5.806205,3.268077,0.104471,6.878842,-1.998967,6.805839],[-1.031157,9.515730,-3.165551,0.537078,9.141926,-3.901807,3.149086,3.883463,2.245731,2.261819,5.738975,7.634498,-0.202201],[8.653428,-7.351458,-0.946365,5.365691,-9.736573,1.713385,7.632213,7.300768,-2.056599,-0.032713,2.578780,9.457285,3.156967],[0.331385,-0.767648,5.947706,-9.072230,-2.854429,-0.735145,-7.086167,7.948708,-1.761518,-2.963021,-5.582066,-1.809653,-6.394434],[-4.404810,-7.972251,-9.591483,7.508785,-8.926971,-0.855427,-7.453205,1.526439,-3.221892,3.101219,-6.515619,9.931632,0.540014],[7.076419,-0.988801,0.164680,-3.605849,-6.703456,2.607511,3.579113,-1.602224,-8.903344,-9.414876,-3.469958,1.649011,-2.126599],[2.201642,0.856968,9.631550,9.224369,-5.763646,9.635245,-0.789568,-2.018155,8.994918,6.222677,4.764784,-7.693449,-1.980692],[7.843884,-9.246774,0.786505,8.160330,4.899399,2.709166,-7.476709,1.289453,-0.421542,-3.741584,-4.631017,-9.448473,1.038883],[5.747392,0.701481,-2.470525,-9.997027,-8.743612,3.859455,-9.744341,3.700550,6.823350,5.565764,4.024943,-3.502816,-3.664499],[7.542010,5.701015,9.823811,-0.503481,-0.838421,9.608280,4.265695,-4.671529,1.561531,6.426421,-7.551334,-0.777557,-9.127337]],[[-8.170112,7.340368,5.935892,9.261494,-1.069116,6.350195,-2.782772,1.751943,-9.305894,0.176282,2.946997,2.941890,4.736562],[5.086673,-0.558147,3.215895,6.499476,0.550036,0.131636,6.328600,2.510788,-1.400854,-1.246148,8.973024,5.006886,7.712078],[1.379289,0.809375,-2.088002,9.380889,-7.895974,7.211603,3.378858,-8.793725,-1.916039,-3.335934,2.047181,9.560597,1.814183],[-8.858271,1.484263,5.997853,6.298498,-7.542922,-7.729371,-8.713830,-3.927382,-2.174959,-1.880441,2.447841,-1.564076,7.556775],[-5.521830,5.098090,5.735992,-8.064741,6.161240,-7.224999,9.745079,-7.134784,-4.750282,-5.688644,8.209016,-3.960494,-6.620845],[-5.893236,-5.316687,-1.403055,-3.140418,-9.824230,9.095057,-9.012952,-8.180883,8.403684,6.602662,3.190569,-5.109999,6.408561],[-2.371136,-0.102587,1.126419,1.106884,-9.598470,-3.769370,8.593205,-3.304104,-2.299707,9.507493,0.228218,-9.422382,2.292882],[-7.745621,1.314485,9.668053,-6.923453,-4.066669,-2.321400,8.174067,9.763520,6.078670,-5.618605,-2.320188,-1.981308,5.406261],[-1.890445,4.205765,-7.842560,-2.001119,3.220074,0.314340,3.143547,0.204256,-2.083411,-5.779070,-5.468549,-0.517403,2.902417],[7.878898,0.993053,-2.312229,-6.585546,7.308392,4.361326,3.567976,6.600096,-7.049391,-6.178977,-0.394144,-7.156008,4.590152],[-7.244974,2.558827,-0.196948,6.033253,-8.950061,6.095348,4.751332,8.251338,-0.136372,0.152026,0.629940,-3.208373,5.821092],[-5.541269,8.173496,1.154901,-6.498960,-4.954413,0.177742,-7.089908,7.248866,1.301576,-1.304404,6.241031,4.596298,-6.180045],[3.559426,-8.624775,2.507638,-9.444633,-4.872702,-9.723712,8.224076,1.962500,-5.902671,-7.637123,-6.021436,1.706535,-0.773635],[7.070105,8.692957,-5.937035,2.289193,-6.499518,-4.159479,3.499965,-4.143861,0.873607,-4.267979,-6.928564,-8.980876,-4.957818]]], dtype = "float64")#candidate|4819|(12, 14, 13)|const|float64
bop_4820 = relay.greater_equal(call_4788.astype('bool'), relay.reshape(const_4819.astype('bool'), relay.shape_of(call_4788))) # shape=(12, 14, 13)
bop_4823 = relay.greater_equal(call_4790.astype('bool'), relay.reshape(const_4819.astype('bool'), relay.shape_of(call_4790))) # shape=(12, 14, 13)
output = relay.Tuple([call_4786,const_4789,call_4805,call_4807,const_4808,bop_4820,])
output2 = relay.Tuple([call_4787,const_4789,call_4806,call_4809,const_4808,bop_4823,])
func_4824 = relay.Function([], output)
mod['func_4824'] = func_4824
mod = relay.transform.InferType()(mod)
mutated_mod['func_4824'] = func_4824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4824_call = mutated_mod.get_global_var('func_4824')
call_4825 = func_4824_call()
output = call_4825
func_4826 = relay.Function([], output)
mutated_mod['func_4826'] = func_4826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_4866 = func_928_call()
call_4867 = func_928_call()
output = relay.Tuple([call_4866,])
output2 = relay.Tuple([call_4867,])
func_4880 = relay.Function([], output)
mod['func_4880'] = func_4880
mod = relay.transform.InferType()(mod)
output = func_4880()
func_4881 = relay.Function([], output)
mutated_mod['func_4881'] = func_4881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_254_call = mod.get_global_var('func_254')
func_255_call = mutated_mod.get_global_var('func_255')
call_4903 = func_254_call()
call_4904 = func_254_call()
const_4905 = relay.const([[[-1.174917,8.957348,-3.685036,0.857736,-9.654289,-4.776992,-2.867039,-7.346684,9.359034,1.023929,0.254126,8.673294],[6.127194,-5.849992,-6.659187,-4.762475,-9.181943,-5.900375,7.162529,-5.758701,6.497720,-0.264150,8.792354,-8.712336],[-2.728528,-8.905883,-5.063145,0.028276,-5.048463,4.884248,3.916641,5.401286,-6.496713,-2.130066,5.561577,9.103913],[-5.809961,7.218654,-0.710543,-2.313856,8.508558,-3.416142,-9.662220,8.582313,0.770674,4.753003,4.470194,-3.309052],[-6.489088,5.686730,-2.687534,8.763348,-0.218316,-3.587809,-4.203259,4.821711,-3.789459,3.274109,6.455642,0.460475],[-2.118415,6.873664,-2.976326,4.503982,-7.033457,-0.991106,3.886102,1.223935,-6.263778,-1.407931,-1.386657,-2.716998],[3.723731,-9.330457,1.762067,0.292819,-9.330671,9.373838,1.307167,-2.554114,8.193490,-0.575043,-6.192212,-8.876737],[9.654378,1.481810,-2.364545,-4.707999,-6.222385,-4.487911,9.245870,4.542104,-4.502785,-7.663296,6.700122,0.187674]],[[3.119553,5.348488,-1.527161,2.346963,-3.419039,9.622903,-6.654564,-3.870409,-1.043747,-7.804988,-6.878863,-5.031148],[-8.191672,-5.693535,7.311077,-1.734440,7.957590,-8.631748,8.186413,-2.507483,-0.595066,-3.650444,0.542275,0.880000],[9.575230,9.272882,7.463199,-2.846976,-5.606685,9.193331,1.897942,0.968928,1.834829,-5.414246,6.542235,-8.790469],[-2.025245,-5.727233,2.579618,-4.234129,-2.040048,4.876088,6.832027,6.025961,-1.611974,6.968545,1.541791,3.491920],[-0.754008,9.226273,-8.539446,1.754254,1.696852,-1.135109,-0.254290,7.015639,6.023348,-4.857309,8.466989,-3.818182],[0.986536,7.013932,-6.988429,9.498098,-6.564747,-7.674411,7.614921,1.490495,-3.766371,9.339861,-3.544673,7.140705],[3.045287,-5.001753,1.605281,0.029356,-7.435465,3.115053,4.744502,2.986220,-6.444277,-4.366043,-5.642214,-0.363722],[2.265051,4.881853,-5.780081,5.152963,-8.055231,-4.792060,8.090658,-6.313204,-0.493591,-0.341236,3.033912,4.715551]],[[-4.783405,3.894453,-2.259578,7.560217,5.938070,8.244398,0.431949,-5.505544,1.999651,4.423155,-4.496976,-7.058257],[-4.984601,-5.652465,8.097717,9.818796,4.347932,-0.038445,-0.671802,3.897860,-9.086791,4.953859,-6.653502,2.873960],[6.366798,-7.964829,5.511727,-8.824253,0.710170,2.440843,9.779731,-3.016729,4.600367,-7.112882,-2.838590,5.196572],[-7.330226,-9.924862,-2.990659,-5.661558,9.993977,4.664831,-6.517252,-0.857502,-9.841798,-4.898116,-8.067599,-9.966345],[3.747458,3.114751,1.486250,-2.502135,3.811875,-8.856469,-1.356504,4.297031,8.309767,-7.464349,9.771998,5.824169],[-2.778634,7.137249,2.784133,-6.433996,-0.306884,-1.935629,7.679683,5.217439,-3.220190,-7.441895,1.935160,-1.168112],[9.252353,-9.785392,4.566888,-6.148447,4.914153,-9.052657,-3.599708,7.989790,-3.831349,-5.180415,-0.300672,-4.687774],[9.468485,1.639869,8.975648,9.790583,7.663615,4.707807,6.295687,-5.027810,6.948623,4.413881,-2.693126,-6.169506]],[[6.535167,-0.514131,-1.910460,-7.158756,2.784995,-3.739182,9.039373,3.515977,8.551376,4.906762,6.240069,2.235002],[-1.801634,-1.278689,3.590549,7.831020,0.421985,-9.337917,-9.461847,1.448636,9.420505,-3.181299,3.476072,1.101472],[-9.352005,5.503621,-0.543152,-3.721322,-4.480208,5.976354,0.889200,-4.258952,-5.093372,4.503474,8.231604,2.508162],[-2.857024,8.874818,7.842955,1.395234,0.746000,7.925805,9.339868,-0.888090,-5.747888,-3.386455,-5.143584,-4.970614],[3.295975,3.035158,-0.738440,8.276770,1.129181,-8.193604,0.390590,-0.220722,3.765704,9.156764,-7.708111,-1.433494],[3.907238,-9.384421,4.460198,5.250381,-3.277762,8.091542,9.593332,-3.167865,1.994052,7.979684,-5.203599,0.458513],[-8.556774,-2.947573,-2.956033,6.206207,3.939458,5.200426,8.847713,-3.275416,3.408595,-2.236441,-9.210595,6.993253],[-8.681117,1.322747,0.838145,-8.327607,4.094835,-4.115957,5.110053,9.485075,8.916314,2.823729,5.474310,4.297114]],[[0.366096,9.737189,-2.901687,7.119964,-2.565198,1.607923,1.456649,6.462575,-3.501927,-8.906491,1.239661,6.146472],[-4.178238,7.245301,-6.613170,-0.416339,9.461070,6.523267,2.357375,-1.209860,5.474835,6.005635,9.669995,7.348141],[-4.604846,4.601952,-2.353659,-0.463128,2.126547,-8.245145,-2.036813,1.934966,4.672658,1.595382,3.552017,-7.371884],[1.016921,9.703531,-6.048673,4.443592,-3.480026,-4.074653,5.472468,8.545620,3.906375,-0.531777,-7.389354,0.910654],[-1.399887,-1.885731,-8.191779,3.460437,-7.353705,-0.267272,8.676373,1.742527,-7.997107,-3.531747,4.791667,-5.209939],[-5.550956,-1.577244,-2.039516,-9.690880,2.714805,-5.589612,9.295910,2.336231,-8.539709,-4.407744,3.172621,3.876967],[2.250072,9.637728,7.480058,6.985900,-5.141702,-8.308445,3.095694,-9.910903,-5.759808,-7.250881,-9.414201,5.470434],[4.989854,-6.960649,-3.319829,-5.536039,-6.160128,-1.141025,3.533597,1.077578,8.865627,-2.711258,-4.163008,0.060971]],[[2.230667,-4.554766,-8.834180,-2.885457,5.517913,-5.073853,-6.225796,6.087956,3.298490,-2.479661,-1.457684,-6.570034],[-5.718790,-1.260010,6.429802,1.821274,-3.511267,-0.766345,3.901854,-7.587145,-4.801558,-2.959741,-1.607171,7.773841],[3.527993,-1.670203,4.898435,-2.900562,-7.733087,-3.348409,-8.439112,-1.018852,6.123346,5.792223,-5.063104,0.178642],[4.855788,6.477375,9.575568,9.985743,6.511120,-0.530093,-7.863298,-6.072652,-4.802522,2.200456,-0.375737,3.205677],[-5.840573,-2.089638,-5.221651,3.683110,-5.941954,5.634879,0.113487,-4.492051,5.432828,4.996957,3.898025,-2.756072],[-0.630083,2.305993,0.160747,-1.313205,3.174509,-4.439259,-1.795872,1.418431,1.594534,6.107174,1.624174,6.961118],[-1.776397,1.129186,-0.213051,6.730068,0.371110,6.015482,3.158176,-3.328113,-8.703073,3.166680,6.962658,8.152266],[5.308649,2.084261,7.151322,2.292185,-5.352141,0.788167,-6.562034,1.720827,5.526689,1.146199,1.189390,-6.462355]],[[-7.894386,-3.398082,-6.658052,-6.298702,-0.163684,0.952792,-5.470621,-4.295683,8.486285,9.558103,-4.094347,2.984949],[9.325315,5.441025,-1.647130,2.365639,2.574166,-4.357233,3.599800,0.440799,0.742755,2.873350,-3.558147,-3.775889],[-6.905919,7.924390,-1.918504,-3.749739,8.957440,-7.981749,7.334572,7.639133,-5.804846,2.150435,-5.996491,9.670156],[7.344854,-3.881840,-3.745138,8.892796,-8.283701,-7.522203,3.333856,6.109319,-6.329768,-7.634503,3.950483,-4.570861],[-5.178974,2.045087,-1.981986,-8.781578,-4.931102,4.166567,2.005775,9.496414,-1.700066,-6.824187,-8.802000,-7.628756],[-8.971769,0.849214,-4.209243,5.749550,1.379559,-3.908051,4.904849,8.840416,9.160051,8.576258,8.832684,-9.840075],[-2.517635,0.908314,-1.070035,0.196954,-5.780700,-6.864965,-7.720497,8.174615,5.499357,2.365303,-7.596005,-7.699290],[-2.933632,-4.050803,-2.139413,9.678743,-2.429128,6.050044,-0.163477,4.508864,8.731471,-4.349362,8.181841,8.157823]],[[9.375408,0.308326,6.325893,3.645776,0.321951,4.426629,-3.224253,-8.479983,5.835641,-1.101631,-3.145572,7.006596],[5.482879,1.863667,8.323562,9.483593,-9.181422,6.920955,-3.242206,4.050718,-2.355358,5.904156,2.927778,2.192179],[-9.374398,-4.627818,5.230399,-7.528707,1.566513,0.256890,9.269706,4.009867,-8.682027,7.310741,6.603457,-3.009364],[-7.710711,8.167545,-5.884285,-3.375012,-6.144843,9.500401,-1.193375,-6.274432,-8.223009,8.454458,6.417163,0.033640],[5.422490,-4.385221,5.255331,-0.119316,9.488785,7.988765,1.307465,-0.982551,-7.707544,2.073908,9.374854,4.446530],[-5.082838,6.560462,4.129539,0.433493,-1.476563,-9.124644,-4.095446,2.359255,-1.881702,2.747241,-4.827154,6.620533],[-8.079599,-6.905086,-5.216564,0.192552,-0.835038,-0.405411,8.324524,-3.702681,-2.087621,1.358504,2.444012,-0.741560],[6.045085,7.627487,0.286335,-8.648998,-3.932789,5.735721,-5.623580,6.610166,-1.538210,3.117863,8.104218,2.885658]],[[-0.226838,-1.589497,8.762075,0.454118,9.698881,-6.134540,4.479252,-6.485643,4.565899,-3.187009,-7.499924,-7.102877],[-5.769355,-8.295475,0.530947,7.861778,-3.545781,-5.130230,-3.424812,-3.379804,-3.852979,-6.092509,0.668792,0.933620],[-6.153658,6.087288,9.278667,4.758484,2.635297,5.550740,6.271773,-0.057625,7.474510,6.928536,-1.206321,9.569902],[0.929349,-6.105566,-5.070411,8.157219,1.963655,5.905048,6.755774,-3.031466,-8.899492,1.337882,-8.365494,3.578447],[-3.892434,4.563202,-5.234220,-4.185783,-4.323301,-3.744102,-3.748942,-3.256948,-0.958294,3.023557,-1.894345,-3.857556],[3.847544,4.968414,0.056720,1.642300,6.882739,-7.697057,6.965826,4.530295,0.919201,-3.588184,-8.160887,-9.114025],[-1.213996,-8.682706,3.631661,2.274443,-4.703876,1.964258,5.641556,-7.266937,5.801171,-8.629362,8.945318,6.861148],[-0.157858,-2.394335,-9.165522,8.077113,-8.473828,1.831530,3.475995,3.960000,2.933656,5.136453,8.758173,-0.283847]],[[8.551784,-0.575944,-3.227841,5.791606,4.007383,9.578351,-4.400095,0.994722,-0.097610,4.898053,3.959061,-0.038050],[4.586547,-4.630096,9.880529,4.980321,7.412070,0.484966,8.729930,-6.847342,-3.105398,-2.441675,9.405985,-3.805601],[3.870385,0.789437,-8.829041,4.776307,9.415708,-8.878962,-5.923753,7.387862,6.924792,-6.784259,-8.139797,-7.801826],[-7.697585,9.070015,-9.161927,-7.485003,6.180539,-5.132648,0.493735,0.070538,4.212848,2.567678,-5.471714,-5.392397],[0.429599,-1.060930,8.948037,-2.153015,-2.983982,1.347758,2.501167,-6.660741,5.394910,-4.919214,-5.381557,-7.130034],[-6.393134,-2.043262,-7.396523,-5.001402,5.787747,4.665426,6.562492,-1.997934,-6.028597,-1.670779,1.041871,-7.943770],[-7.958224,3.494563,2.202290,-0.010157,4.155581,-9.557099,1.209324,0.463020,6.037931,-2.954965,2.429023,-2.419139],[-2.903823,4.725056,7.873498,3.847716,2.543478,1.302476,-3.076561,-3.525770,-9.926660,2.741152,0.389432,-2.086377]]], dtype = "float32")#candidate|4905|(10, 8, 12)|const|float32
bop_4906 = relay.maximum(call_4903.astype('int32'), relay.reshape(const_4905.astype('int32'), relay.shape_of(call_4903))) # shape=(10, 8, 12)
bop_4909 = relay.maximum(call_4904.astype('int32'), relay.reshape(const_4905.astype('int32'), relay.shape_of(call_4904))) # shape=(10, 8, 12)
output = relay.Tuple([bop_4906,])
output2 = relay.Tuple([bop_4909,])
func_4941 = relay.Function([], output)
mod['func_4941'] = func_4941
mod = relay.transform.InferType()(mod)
output = func_4941()
func_4942 = relay.Function([], output)
mutated_mod['func_4942'] = func_4942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_4957 = func_928_call()
call_4958 = func_928_call()
output = relay.Tuple([call_4957,])
output2 = relay.Tuple([call_4958,])
func_4962 = relay.Function([], output)
mod['func_4962'] = func_4962
mod = relay.transform.InferType()(mod)
output = func_4962()
func_4963 = relay.Function([], output)
mutated_mod['func_4963'] = func_4963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4383_call = mod.get_global_var('func_4383')
func_4384_call = mutated_mod.get_global_var('func_4384')
call_4964 = relay.TupleGetItem(func_4383_call(), 2)
call_4965 = relay.TupleGetItem(func_4384_call(), 2)
output = relay.Tuple([call_4964,])
output2 = relay.Tuple([call_4965,])
func_4966 = relay.Function([], output)
mod['func_4966'] = func_4966
mod = relay.transform.InferType()(mod)
output = func_4966()
func_4967 = relay.Function([], output)
mutated_mod['func_4967'] = func_4967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_4970 = func_3961_call()
call_4971 = func_3961_call()
output = call_4970
output2 = call_4971
func_4994 = relay.Function([], output)
mod['func_4994'] = func_4994
mod = relay.transform.InferType()(mod)
mutated_mod['func_4994'] = func_4994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4994_call = mutated_mod.get_global_var('func_4994')
call_4995 = func_4994_call()
output = call_4995
func_4996 = relay.Function([], output)
mutated_mod['func_4996'] = func_4996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4276_call = mod.get_global_var('func_4276')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_5000 = func_4276_call()
call_5001 = func_4276_call()
output = call_5000
output2 = call_5001
func_5003 = relay.Function([], output)
mod['func_5003'] = func_5003
mod = relay.transform.InferType()(mod)
mutated_mod['func_5003'] = func_5003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5003_call = mutated_mod.get_global_var('func_5003')
call_5004 = func_5003_call()
output = call_5004
func_5005 = relay.Function([], output)
mutated_mod['func_5005'] = func_5005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1982_call = mod.get_global_var('func_1982')
func_1984_call = mutated_mod.get_global_var('func_1984')
call_5014 = func_1982_call()
call_5015 = func_1982_call()
output = call_5014
output2 = call_5015
func_5016 = relay.Function([], output)
mod['func_5016'] = func_5016
mod = relay.transform.InferType()(mod)
mutated_mod['func_5016'] = func_5016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5016_call = mutated_mod.get_global_var('func_5016')
call_5017 = func_5016_call()
output = call_5017
func_5018 = relay.Function([], output)
mutated_mod['func_5018'] = func_5018
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5051 = relay.const([[[2,7,2,-8,4,-8],[-9,-3,-9,-7,1,-4],[-7,-1,-9,4,-5,-5],[2,-7,-3,3,4,-9],[4,-8,10,-3,8,-7],[-9,8,3,10,7,10],[-2,10,-10,7,-6,10],[8,5,9,4,-3,1],[6,-1,-9,-2,5,-7],[2,-10,-10,6,-4,-5],[-3,3,1,-3,-7,1],[7,-7,5,9,7,-8],[10,6,-7,6,-7,-9],[5,7,-6,8,-2,-8]],[[-8,-8,8,5,-2,-9],[1,10,-8,-8,10,-5],[-4,4,9,-4,-10,-5],[8,4,8,-10,3,-8],[-10,-2,-2,9,-3,3],[-4,10,-9,2,-2,9],[4,-10,3,5,-6,4],[-5,5,7,-1,-5,8],[-5,-5,-9,-10,6,-9],[10,2,1,4,-2,-6],[-5,1,8,-7,-2,-10],[9,-3,10,5,5,5],[-7,4,6,-10,6,4],[-3,-9,-5,5,10,10]],[[9,1,-5,10,5,-3],[3,-3,-5,5,10,-2],[-2,1,-6,-2,-6,-8],[9,-5,9,7,-9,3],[9,-5,-1,-6,-5,-4],[7,5,1,6,-1,-6],[9,4,-4,-4,-4,-4],[8,-7,8,-2,-9,2],[-10,2,9,4,1,-6],[5,-10,10,4,-7,-9],[-4,1,9,5,-2,-1],[-7,9,-2,-5,-4,6],[2,-10,-2,-3,1,2],[-9,-9,4,-4,-4,-10]]], dtype = "int64")#candidate|5051|(3, 14, 6)|const|int64
var_5052 = relay.var("var_5052", dtype = "int64", shape = (3, 14, 6))#candidate|5052|(3, 14, 6)|var|int64
bop_5053 = relay.greater(const_5051.astype('bool'), relay.reshape(var_5052.astype('bool'), relay.shape_of(const_5051))) # shape=(3, 14, 6)
bop_5056 = relay.not_equal(bop_5053.astype('bool'), relay.reshape(var_5052.astype('bool'), relay.shape_of(bop_5053))) # shape=(3, 14, 6)
uop_5095 = relay.sinh(const_5051.astype('float32')) # shape=(3, 14, 6)
func_2979_call = mod.get_global_var('func_2979')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_5100 = func_2979_call()
call_5101 = func_2979_call()
func_385_call = mod.get_global_var('func_385')
func_386_call = mutated_mod.get_global_var('func_386')
call_5117 = func_385_call()
call_5118 = func_385_call()
output = relay.Tuple([bop_5056,uop_5095,call_5100,call_5117,])
output2 = relay.Tuple([bop_5056,uop_5095,call_5101,call_5118,])
func_5131 = relay.Function([var_5052,], output)
mod['func_5131'] = func_5131
mod = relay.transform.InferType()(mod)
mutated_mod['func_5131'] = func_5131
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5132 = relay.var("var_5132", dtype = "int64", shape = (3, 14, 6))#candidate|5132|(3, 14, 6)|var|int64
func_5131_call = mutated_mod.get_global_var('func_5131')
call_5133 = func_5131_call(var_5132)
output = call_5133
func_5134 = relay.Function([var_5132], output)
mutated_mod['func_5134'] = func_5134
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5138 = relay.var("var_5138", dtype = "float64", shape = (1, 11, 15))#candidate|5138|(1, 11, 15)|var|float64
uop_5139 = relay.atanh(var_5138.astype('float64')) # shape=(1, 11, 15)
func_3948_call = mod.get_global_var('func_3948')
func_3949_call = mutated_mod.get_global_var('func_3949')
call_5142 = relay.TupleGetItem(func_3948_call(), 0)
call_5143 = relay.TupleGetItem(func_3949_call(), 0)
func_1619_call = mod.get_global_var('func_1619')
func_1620_call = mutated_mod.get_global_var('func_1620')
call_5146 = relay.TupleGetItem(func_1619_call(), 0)
call_5147 = relay.TupleGetItem(func_1620_call(), 0)
func_4425_call = mod.get_global_var('func_4425')
func_4427_call = mutated_mod.get_global_var('func_4427')
const_5149 = relay.const([[1.199929],[-2.947527],[8.767213],[7.072512],[-2.051866],[4.243507],[3.844050],[-6.281032],[-5.681383],[-4.118643]], dtype = "float64")#candidate|5149|(10, 1)|const|float64
call_5148 = relay.TupleGetItem(func_4425_call(relay.reshape(const_5149.astype('float64'), [10,])), 3)
call_5150 = relay.TupleGetItem(func_4427_call(relay.reshape(const_5149.astype('float64'), [10,])), 3)
func_321_call = mod.get_global_var('func_321')
func_324_call = mutated_mod.get_global_var('func_324')
call_5154 = relay.TupleGetItem(func_321_call(relay.reshape(call_5146.astype('float32'), [10, 8, 12])), 0)
call_5155 = relay.TupleGetItem(func_324_call(relay.reshape(call_5146.astype('float32'), [10, 8, 12])), 0)
const_5159 = relay.const([[[5.241120,-5.871035,9.441535,-4.175141,0.184592,3.680805,1.109577,5.615066,-7.437750,5.325911,6.900675,4.881658],[-5.914733,-0.924519,-7.472378,3.752325,8.950698,3.676606,-6.829611,-8.676459,-2.033156,6.769650,-9.656321,3.050692],[-6.968145,2.896629,1.627615,4.223941,7.204322,5.337429,-2.468990,2.252087,3.288244,-6.681564,-7.671383,3.562715],[-0.832311,-4.254046,5.632102,1.027740,-2.633319,-0.953565,7.971638,-2.242506,0.888330,-7.194312,-9.038000,-2.179843],[-7.615298,5.304838,9.961015,6.295266,-5.994420,6.088311,3.737674,9.068631,1.988521,-9.214938,3.430860,8.969278],[-2.814808,-1.384856,-1.396712,-1.496168,4.643219,5.324155,4.691391,-1.121369,2.748274,8.429232,-0.531523,-8.062786],[-3.030531,-9.607495,6.033084,4.514372,2.020270,9.346330,-4.354226,-2.783000,1.912034,-9.804131,0.259327,-5.357051],[-7.621223,0.059277,-8.598910,9.984972,-3.986032,9.223567,7.406846,-8.577898,-4.296646,-1.506448,1.727732,9.244123]],[[1.777541,9.548731,-0.286455,5.208753,-1.627743,-6.433943,-6.254909,7.239125,2.452686,1.887395,4.547517,-6.762413],[9.227140,-2.540538,9.039646,5.364780,-2.671994,6.284018,1.438541,2.032376,-0.151515,-1.708011,9.916349,6.541358],[-3.212973,-8.822977,-9.545119,-2.544974,7.064505,5.867655,-9.260040,1.783165,2.844324,5.126463,4.335465,-4.200628],[-3.422078,6.311924,5.475261,4.209751,3.653980,3.955941,-7.703917,5.784735,3.581611,-6.371255,9.390328,-9.819129],[0.789212,5.740651,-2.142549,-3.424563,0.128250,5.729907,-9.754360,-8.696174,-8.108722,-5.800564,1.277822,-4.125263],[-8.993950,-8.189764,6.028754,-5.129798,9.986766,6.112315,-1.326011,-3.483436,8.383436,-9.348255,-1.683072,0.651143],[-8.735914,2.229837,4.472370,-7.714220,5.512499,-8.442329,1.002359,5.398371,-6.610566,9.457020,-1.222999,-1.828009],[9.466018,1.198522,-2.291275,-4.521762,-7.629800,-1.340228,0.750282,2.303632,-8.108215,1.765285,0.723807,-6.130799]],[[-1.291243,-0.518708,6.936406,-8.593757,9.497096,6.283618,6.057208,-3.162948,1.693474,4.957225,-8.999647,7.033392],[-8.912580,-9.077661,6.147494,-3.426469,-9.248318,-1.829385,9.745627,-7.840586,6.278074,-4.436622,1.544179,-4.148310],[-1.596999,-5.923518,5.358327,8.571642,-0.390567,1.867640,-0.694566,7.824303,-1.493014,-9.805346,4.531425,-4.757791],[-0.184958,3.731289,0.480854,9.518182,1.684852,-4.890713,4.029778,5.331038,-7.402404,-9.238429,-0.323177,3.537118],[9.260123,-7.565610,6.021250,0.140763,-8.780840,3.365539,9.143465,7.865086,-0.431692,2.216195,8.506003,-3.867376],[9.641217,-3.845592,-1.620051,-8.895642,1.536522,-3.582484,0.415919,9.651098,-3.847398,2.968465,9.386947,7.045349],[6.447551,9.791940,9.242350,-8.287017,-6.768845,-2.631946,-8.256195,8.380707,4.404876,-4.065936,1.742489,-8.907982],[2.593096,3.387200,-4.443607,-0.684887,8.165428,-6.781199,3.019482,1.067985,0.763440,9.065451,-9.877966,-9.912228]],[[-5.780580,-3.450356,-6.251253,-2.226786,9.785974,-4.028384,-8.848837,3.665558,-8.803199,-7.001188,-2.715856,-4.629418],[3.808236,6.052074,-5.038240,1.034375,3.464634,-2.562287,1.676912,5.466597,9.826747,-9.999614,-4.880163,6.335343],[-7.730304,4.640581,-7.108637,-6.674005,0.468331,9.217110,7.804945,-3.207903,5.944878,-4.104503,4.514437,7.011156],[1.303587,-6.290882,2.318173,7.376042,0.090995,-8.484007,-5.337757,3.791407,-9.524297,5.167537,-9.417586,-3.289750],[-1.726109,-8.160875,-9.411196,-1.275707,9.162542,-7.679121,8.120463,-3.874393,-3.217105,-2.220631,-3.351276,-0.635488],[-4.113738,-5.638970,7.597004,-8.585291,-1.702384,-8.674137,-6.482612,-7.902919,1.606856,-5.672575,-4.722468,-4.420555],[4.866149,8.982883,-0.848848,3.285198,6.327558,0.018420,-8.466574,8.822291,-9.193789,-7.331456,-2.299760,3.088484],[1.474074,-7.158661,-9.419825,-0.432512,0.878403,3.781639,1.984095,2.552494,7.774462,0.046075,-5.865752,-9.937559]],[[-5.765784,-0.715340,4.232779,4.634815,0.286442,8.217678,-2.439201,-1.898753,3.738581,4.142674,-9.296718,-2.137481],[-8.824366,1.397355,-5.043363,2.154846,-7.724689,0.283318,1.082073,-4.154373,7.738154,9.570145,8.196161,0.131241],[8.216430,9.326996,3.454173,6.209962,-4.410396,2.997757,-7.984865,9.602686,-8.687114,9.150482,7.847117,-5.456701],[0.572554,-5.922780,9.784375,1.275037,0.527787,-7.787015,-2.462075,-2.010923,5.126551,5.004053,-1.857136,-1.189225],[-6.154891,0.781679,-6.691089,-0.233604,3.182778,-0.789677,-8.388949,2.126269,4.432756,7.844010,-9.786854,-2.141067],[7.844357,2.688772,-0.116665,-6.587288,9.164238,9.414229,4.278470,7.448848,-7.769635,-9.934118,-2.674779,-4.104100],[7.705165,9.253472,2.113456,0.633459,-4.336171,8.457118,7.849182,1.438930,6.436846,-1.027981,-0.729473,9.701798],[7.074078,9.032993,2.880556,1.510416,9.787845,-7.151379,-2.169977,0.968141,5.524746,-9.588184,-8.212902,2.288525]],[[-4.711708,6.645599,-7.803998,5.944445,-5.957113,3.750745,4.901494,-7.183647,3.703577,2.740182,8.018064,-4.724815],[7.418351,2.941279,-7.030189,1.086305,-3.598987,8.260840,3.538758,-7.491718,-3.614054,-1.055888,9.034990,-9.918835],[6.350011,-7.185618,6.564333,1.844783,6.863324,-9.302737,-4.708929,-1.552723,-2.285559,6.450772,7.288249,3.179625],[1.163537,0.965205,7.368215,8.229846,1.935265,4.167385,0.093848,-8.073077,6.002061,-9.909451,-7.876130,-5.091586],[9.562130,8.947785,3.580925,-6.244416,-8.209342,8.697197,5.838842,-9.618265,1.292396,1.237375,6.232212,3.151831],[8.717897,-3.384939,3.382905,-8.847537,-0.206599,3.939298,7.440734,-9.004123,2.934738,2.836616,-5.897549,3.235462],[3.105549,-5.288920,-8.310310,7.576030,-3.667553,-5.081642,-0.370659,-8.310549,-1.281482,-3.208877,4.518261,7.012899],[2.078213,7.432966,-5.693147,1.268258,-1.782719,-7.140071,5.459326,-1.505912,2.152451,4.942052,6.655959,-5.936241]],[[0.296051,3.105103,9.566267,0.401821,2.732549,5.287497,-2.477265,6.263811,-3.332382,5.484580,6.325867,4.983953],[-4.711751,-5.037031,-5.081594,6.192071,-7.764264,-6.823577,1.214121,-2.987276,5.421287,1.931286,-1.450170,-5.618838],[-9.536648,-6.186973,6.436944,7.750543,0.891852,2.671185,-9.889879,9.268238,-5.434471,5.408312,-1.115405,-2.249944],[2.424992,3.215436,8.438572,-0.464103,1.750353,3.302209,0.768972,8.772248,3.548089,-3.639907,5.510921,-9.371673],[-2.689731,-4.908056,7.335317,-7.042214,-5.464631,-4.439487,0.092018,7.859332,5.170975,8.231050,0.162380,7.117061],[3.878487,8.556316,-9.343097,-5.029182,4.185491,9.470969,-3.329002,5.580738,5.851614,-1.072264,-7.534322,1.157504],[-4.802605,-8.020495,3.076939,-6.148389,-1.095145,-3.375101,4.818874,1.075324,0.140322,4.339502,-3.909988,-3.363102],[-5.194396,-5.423206,-3.777319,5.199152,-6.417143,0.960620,7.898608,-2.468919,0.374808,-3.140657,-1.481454,1.626777]],[[-1.726743,8.642861,8.295017,-1.060486,-3.617903,-7.160449,8.887219,9.519642,-8.222936,1.407882,2.421140,4.633729],[-7.153036,5.255302,7.323974,-9.361577,-2.593278,-0.297836,5.834974,5.728162,5.659880,4.717908,7.852359,-6.246561],[4.238467,-9.775532,8.841652,8.916582,7.694139,-4.938929,1.184784,2.639945,-3.764424,9.157591,-3.456868,3.472166],[-9.859440,-2.461243,-4.208798,0.097544,6.352780,-4.393105,9.136909,-6.668266,-8.238119,8.249218,-9.851747,1.760982],[-7.537706,-9.605853,-5.363892,-6.872685,-7.304621,-0.815517,6.767083,-4.285792,3.964283,-8.193783,-7.222988,-6.332067],[2.953120,-1.052916,-6.688103,2.090463,-6.885145,0.531587,6.957322,-5.695062,0.354595,-2.937433,-3.124559,3.634449],[8.740260,7.703345,-8.627682,6.377188,6.443322,4.402073,1.259643,8.980175,3.688008,-6.271978,-1.130561,-7.345091],[-2.850938,9.259013,-4.807471,-3.911326,-8.512160,3.402799,8.944065,-3.977756,7.442081,-7.490491,-5.882169,-3.539867]],[[8.010726,9.140149,5.696078,4.117090,-9.494642,3.425144,9.598936,6.540395,8.445664,-0.196461,6.549844,1.681920],[4.531166,5.668116,9.057839,4.385485,6.667536,0.785777,-1.721566,-8.913598,0.518686,4.491911,6.378940,-7.835714],[-4.375645,-7.528737,9.224983,-1.133686,3.374797,1.626622,2.761653,6.412945,1.428881,-6.698596,1.822267,-8.282010],[-3.278806,7.003349,-5.199675,-3.920664,9.370364,-8.093556,-3.809418,6.577894,4.139226,3.702292,4.502499,9.605844],[4.572619,-4.824116,-6.266016,8.803693,6.998635,-5.778067,-6.398424,-1.077819,5.730420,-9.067396,9.170537,-9.761944],[-5.952804,8.743796,-9.438469,-3.231230,-7.891890,8.246941,-5.411876,6.160955,2.315814,3.556535,-2.154842,6.994944],[2.355193,-2.128799,1.379679,0.455579,-5.388539,9.742134,8.636298,-1.956323,1.493724,-3.410438,-5.547984,9.330468],[7.869406,1.848038,-0.895927,-1.345515,-8.172071,-4.486716,9.653602,-9.423470,-5.324292,-9.565302,5.553736,-0.891317]],[[-9.183938,-1.357548,-3.533121,2.283758,5.518779,-5.549222,5.969594,0.274977,4.202604,-5.525082,9.346853,-2.790565],[-3.342306,3.023517,2.147589,-4.924798,-6.528077,-0.474340,-6.749174,-4.017189,-0.655149,0.340488,2.928858,9.036765],[-1.583677,9.420574,-1.698124,-6.367694,2.570005,7.468215,4.489408,-3.615189,-6.512700,-2.030639,-0.096743,-2.637993],[3.124789,8.778551,-5.840665,8.622841,-3.156338,-2.390173,-7.657406,4.543806,-7.012165,-1.578544,7.018330,1.170394],[6.833056,-9.501080,9.419144,-4.147464,4.063984,0.784759,4.367707,-1.426391,-8.032572,-8.205045,9.987069,-6.167832],[-8.181774,5.444370,4.929878,-2.229865,6.960086,9.154866,0.400508,6.159991,7.276345,5.254394,-4.853436,-9.984696],[-9.456578,5.451481,-9.713186,-0.017515,5.033966,-4.572320,-8.367075,5.494205,-8.800433,-9.902842,9.664690,-1.097257],[1.507176,5.743586,7.569986,-9.596984,-2.127836,-5.638843,6.424868,-4.172783,-9.458460,8.387759,1.930493,-2.155127]]], dtype = "float32")#candidate|5159|(10, 8, 12)|const|float32
bop_5160 = relay.less(call_5154.astype('bool'), relay.reshape(const_5159.astype('bool'), relay.shape_of(call_5154))) # shape=(10, 8, 12)
bop_5163 = relay.less(call_5155.astype('bool'), relay.reshape(const_5159.astype('bool'), relay.shape_of(call_5155))) # shape=(10, 8, 12)
bop_5194 = relay.bitwise_xor(uop_5139.astype('int32'), relay.reshape(var_5138.astype('int32'), relay.shape_of(uop_5139))) # shape=(1, 11, 15)
output = relay.Tuple([call_5142,call_5146,call_5148,const_5149,bop_5160,bop_5194,])
output2 = relay.Tuple([call_5143,call_5147,call_5150,const_5149,bop_5163,bop_5194,])
func_5201 = relay.Function([var_5138,], output)
mod['func_5201'] = func_5201
mod = relay.transform.InferType()(mod)
var_5202 = relay.var("var_5202", dtype = "float64", shape = (1, 11, 15))#candidate|5202|(1, 11, 15)|var|float64
output = func_5201(var_5202)
func_5203 = relay.Function([var_5202], output)
mutated_mod['func_5203'] = func_5203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4276_call = mod.get_global_var('func_4276')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_5239 = func_4276_call()
call_5240 = func_4276_call()
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
const_5242 = relay.const([[-8,-4],[2,-5],[-8,10],[-6,-8],[-9,-1],[-1,-10],[-1,-4],[-8,-4],[1,-3],[7,1],[-6,1],[-5,-4],[-9,-5],[-1,3],[-1,9],[-7,8],[-10,-1],[10,2],[-5,9],[3,-4],[8,3],[6,9],[4,9],[-2,1],[9,-1],[-6,-4],[-8,-8],[-6,-3],[2,4],[-3,7],[3,-1],[4,-1],[2,3],[-6,8],[2,5],[8,2],[6,-10],[-9,6],[-7,-10],[-9,-6],[-2,-10],[8,2],[-3,5],[7,-5],[-3,1],[4,-7],[6,-3],[-6,-5],[-10,9],[-2,5],[10,-9],[9,-1],[9,-6],[1,5],[1,-2],[1,-7],[2,-8],[-7,-10],[-6,5],[10,-10],[7,-1],[9,8],[6,-9],[9,7],[-2,-8],[9,-9],[8,2],[9,9],[8,-8],[8,9],[8,-10],[-3,-10],[1,5],[7,-6],[-7,5],[10,4],[3,-5],[8,2],[1,4],[-8,-9],[4,2],[-10,-8],[-9,-3],[-4,7],[8,8],[-7,3],[2,-1],[2,3],[6,7],[4,-2],[-8,-3],[3,2],[3,1],[-10,-7],[-2,5],[10,1],[-1,-3],[6,9],[-2,8],[2,9],[8,7],[-4,10],[-5,-1],[-3,3],[3,-3],[1,2],[-4,-9],[10,4],[-7,6],[7,9],[-3,7],[5,1],[3,-4],[6,8],[-8,-10],[6,-6],[7,6],[10,-4],[-6,-8],[-10,-8],[5,-9],[-1,2],[-7,-6],[8,-6],[4,9],[-5,-6],[5,-3],[-4,-9],[-6,9],[7,-5],[-6,5],[-2,9],[3,9],[-10,-1],[10,-9],[9,-3],[-6,10],[-8,8],[-5,7],[6,-3],[-5,-8],[-7,1],[5,2],[-8,6],[-1,-1],[-3,-4],[4,8],[-9,-2],[5,-9],[-9,10],[10,7],[-10,6],[-1,-2],[-6,3],[-8,-3],[-3,-1],[-2,-1],[-9,-4],[-4,1],[-6,-7],[1,-1],[6,8],[-6,10],[3,8],[-2,-6],[-9,-1],[3,-8],[8,6],[-5,-8],[-5,-6],[7,-10],[7,-8],[6,-9],[-6,7],[4,-10],[1,2],[7,8],[6,2],[-9,-6],[2,-7],[-9,1],[-9,-7],[-6,-5],[-5,6],[9,-3],[-7,10],[9,4],[9,-8],[-8,-6],[-9,-9],[-1,3],[-3,9],[2,-9],[-9,7],[-5,9],[-10,4],[10,-4],[4,6],[-2,-1],[-8,9],[4,-1],[6,-3],[8,-7],[-3,-6],[-3,-9],[-8,2],[6,4],[-6,5],[2,-5],[5,9],[1,2],[1,4],[10,10],[-10,5],[8,1],[-6,-7],[2,5],[1,-1],[-2,-6],[-10,-6],[6,6],[2,2],[-5,-7],[-9,9],[6,1],[10,8],[4,6],[4,2],[-9,6],[2,-3],[-2,7]], dtype = "int16")#candidate|5242|(231, 2)|const|int16
call_5241 = relay.TupleGetItem(func_107_call(relay.reshape(const_5242.astype('int16'), [11, 6, 7]), relay.reshape(const_5242.astype('int16'), [11, 6, 7]), ), 0)
call_5243 = relay.TupleGetItem(func_111_call(relay.reshape(const_5242.astype('int16'), [11, 6, 7]), relay.reshape(const_5242.astype('int16'), [11, 6, 7]), ), 0)
func_107_call = mod.get_global_var('func_107')
func_111_call = mutated_mod.get_global_var('func_111')
call_5245 = relay.TupleGetItem(func_107_call(relay.reshape(call_5241.astype('int16'), [11, 6, 7]), relay.reshape(call_5241.astype('int16'), [11, 6, 7]), ), 0)
call_5246 = relay.TupleGetItem(func_111_call(relay.reshape(call_5241.astype('int16'), [11, 6, 7]), relay.reshape(call_5241.astype('int16'), [11, 6, 7]), ), 0)
output = relay.Tuple([call_5239,call_5241,const_5242,call_5245,])
output2 = relay.Tuple([call_5240,call_5243,const_5242,call_5246,])
func_5251 = relay.Function([], output)
mod['func_5251'] = func_5251
mod = relay.transform.InferType()(mod)
output = func_5251()
func_5252 = relay.Function([], output)
mutated_mod['func_5252'] = func_5252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4383_call = mod.get_global_var('func_4383')
func_4384_call = mutated_mod.get_global_var('func_4384')
call_5253 = relay.TupleGetItem(func_4383_call(), 2)
call_5254 = relay.TupleGetItem(func_4384_call(), 2)
func_2584_call = mod.get_global_var('func_2584')
func_2591_call = mutated_mod.get_global_var('func_2591')
const_5256 = relay.const([[4,7,4,-9,-4,-2,-6,-3,8,-4,7,1,-9,-6,3,-4,-3,2,-6,6,4,10,-6,9,-6,10,6,-3,-6,-8,10,5,-4,-3,-8,8,-6,3,5,5,8,-5,9,-1,-6,4,-10,-1,8,3,-2,9],[1,-1,-8,8,-2,-10,10,5,-10,-3,-10,3,10,-5,8,4,7,-8,10,1,-8,2,-4,-7,8,3,6,-5,3,-1,-3,2,8,5,5,-1,-10,-4,-2,9,1,-7,9,3,3,2,-1,-5,4,9,7,4],[-5,-2,-9,6,-4,-9,8,-4,8,-4,-2,-7,1,6,6,-5,-10,7,-7,-1,9,-3,-2,7,-7,-10,-1,5,-5,-10,-5,-3,4,-4,4,-2,-5,-1,6,-10,10,-1,-9,3,-9,6,-9,-7,-8,4,8,6],[-4,4,-4,2,4,-4,-8,-6,3,-9,8,5,-8,-1,-8,-2,5,-2,-10,-4,-6,7,7,-10,-3,5,8,-1,-1,-5,-9,-3,4,-5,10,9,8,-1,-9,-7,2,4,-4,-6,-7,-5,-9,1,4,8,-5,-9],[2,10,-10,4,9,-4,4,7,1,8,-10,1,-6,7,7,6,3,3,-1,7,-4,2,-1,1,-10,-1,-9,4,3,-1,-7,-2,-1,6,-9,-3,-4,-2,3,-6,-2,5,9,-1,3,5,-8,-10,9,10,-9,-4],[9,7,-9,7,9,-7,3,3,1,-4,6,-6,10,-4,3,1,5,-4,-10,-8,-4,1,4,-5,-3,-1,-3,-3,-7,1,6,1,-1,-8,7,1,-2,1,6,10,-5,8,10,-2,-2,-6,-8,-2,10,-9,5,-8],[-4,-10,5,2,10,9,-5,6,5,-6,9,-1,7,5,3,6,4,-10,7,-8,-5,-9,-9,10,7,8,-5,4,-10,1,-6,-3,-2,-9,8,-7,6,7,-1,9,2,-3,-6,-8,-9,2,-5,-6,-1,-7,-2,-3]], dtype = "uint16")#candidate|5256|(7, 52)|const|uint16
var_5257 = relay.var("var_5257", dtype = "int16", shape = (80,))#candidate|5257|(80,)|var|int16
var_5258 = relay.var("var_5258", dtype = "uint16", shape = (2548,))#candidate|5258|(2548,)|var|uint16
var_5259 = relay.var("var_5259", dtype = "uint16", shape = (4004,))#candidate|5259|(4004,)|var|uint16
call_5255 = relay.TupleGetItem(func_2584_call(relay.reshape(const_5256.astype('uint16'), [1, 364]), relay.reshape(var_5257.astype('int16'), [80,]), relay.reshape(var_5258.astype('uint16'), [7, 364]), relay.reshape(var_5258.astype('float32'), [7, 364]), relay.reshape(var_5259.astype('uint16'), [11, 364]), ), 6)
call_5260 = relay.TupleGetItem(func_2591_call(relay.reshape(const_5256.astype('uint16'), [1, 364]), relay.reshape(var_5257.astype('int16'), [80,]), relay.reshape(var_5258.astype('uint16'), [7, 364]), relay.reshape(var_5258.astype('float32'), [7, 364]), relay.reshape(var_5259.astype('uint16'), [11, 364]), ), 6)
func_928_call = mod.get_global_var('func_928')
func_930_call = mutated_mod.get_global_var('func_930')
call_5261 = func_928_call()
call_5262 = func_928_call()
output = relay.Tuple([call_5253,call_5255,const_5256,var_5257,var_5258,var_5259,call_5261,])
output2 = relay.Tuple([call_5254,call_5260,const_5256,var_5257,var_5258,var_5259,call_5262,])
func_5267 = relay.Function([var_5257,var_5258,var_5259,], output)
mod['func_5267'] = func_5267
mod = relay.transform.InferType()(mod)
mutated_mod['func_5267'] = func_5267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5267_call = mutated_mod.get_global_var('func_5267')
var_5269 = relay.var("var_5269", dtype = "int16", shape = (80,))#candidate|5269|(80,)|var|int16
var_5270 = relay.var("var_5270", dtype = "uint16", shape = (2548,))#candidate|5270|(2548,)|var|uint16
var_5271 = relay.var("var_5271", dtype = "uint16", shape = (4004,))#candidate|5271|(4004,)|var|uint16
call_5268 = func_5267_call(var_5269,var_5270,var_5271,)
output = call_5268
func_5272 = relay.Function([var_5269,var_5270,var_5271,], output)
mutated_mod['func_5272'] = func_5272
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5283 = relay.const(-4.647074, dtype = "float32")#candidate|5283|()|const|float32
var_5284 = relay.var("var_5284", dtype = "float32", shape = (12, 2, 1))#candidate|5284|(12, 2, 1)|var|float32
bop_5285 = relay.divide(const_5283.astype('float32'), var_5284.astype('float32')) # shape=(12, 2, 1)
output = bop_5285
output2 = bop_5285
func_5288 = relay.Function([var_5284,], output)
mod['func_5288'] = func_5288
mod = relay.transform.InferType()(mod)
mutated_mod['func_5288'] = func_5288
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5289 = relay.var("var_5289", dtype = "float32", shape = (12, 2, 1))#candidate|5289|(12, 2, 1)|var|float32
func_5288_call = mutated_mod.get_global_var('func_5288')
call_5290 = func_5288_call(var_5289)
output = call_5290
func_5291 = relay.Function([var_5289], output)
mutated_mod['func_5291'] = func_5291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1619_call = mod.get_global_var('func_1619')
func_1620_call = mutated_mod.get_global_var('func_1620')
call_5293 = relay.TupleGetItem(func_1619_call(), 0)
call_5294 = relay.TupleGetItem(func_1620_call(), 0)
output = call_5293
output2 = call_5294
func_5317 = relay.Function([], output)
mod['func_5317'] = func_5317
mod = relay.transform.InferType()(mod)
mutated_mod['func_5317'] = func_5317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5317_call = mutated_mod.get_global_var('func_5317')
call_5318 = func_5317_call()
output = call_5318
func_5319 = relay.Function([], output)
mutated_mod['func_5319'] = func_5319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4333_call = mod.get_global_var('func_4333')
func_4335_call = mutated_mod.get_global_var('func_4335')
call_5322 = func_4333_call()
call_5323 = func_4333_call()
output = call_5322
output2 = call_5323
func_5329 = relay.Function([], output)
mod['func_5329'] = func_5329
mod = relay.transform.InferType()(mod)
mutated_mod['func_5329'] = func_5329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5329_call = mutated_mod.get_global_var('func_5329')
call_5330 = func_5329_call()
output = call_5330
func_5331 = relay.Function([], output)
mutated_mod['func_5331'] = func_5331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mod.get_global_var('func_2816')
func_2817_call = mutated_mod.get_global_var('func_2817')
call_5385 = relay.TupleGetItem(func_2816_call(), 2)
call_5386 = relay.TupleGetItem(func_2817_call(), 2)
func_818_call = mod.get_global_var('func_818')
func_819_call = mutated_mod.get_global_var('func_819')
call_5391 = relay.TupleGetItem(func_818_call(), 0)
call_5392 = relay.TupleGetItem(func_819_call(), 0)
output = relay.Tuple([call_5385,call_5391,])
output2 = relay.Tuple([call_5386,call_5392,])
func_5393 = relay.Function([], output)
mod['func_5393'] = func_5393
mod = relay.transform.InferType()(mod)
mutated_mod['func_5393'] = func_5393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5393_call = mutated_mod.get_global_var('func_5393')
call_5394 = func_5393_call()
output = call_5394
func_5395 = relay.Function([], output)
mutated_mod['func_5395'] = func_5395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_5401 = func_3961_call()
call_5402 = func_3961_call()
output = call_5401
output2 = call_5402
func_5406 = relay.Function([], output)
mod['func_5406'] = func_5406
mod = relay.transform.InferType()(mod)
mutated_mod['func_5406'] = func_5406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5406_call = mutated_mod.get_global_var('func_5406')
call_5407 = func_5406_call()
output = call_5407
func_5408 = relay.Function([], output)
mutated_mod['func_5408'] = func_5408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3948_call = mod.get_global_var('func_3948')
func_3949_call = mutated_mod.get_global_var('func_3949')
call_5472 = relay.TupleGetItem(func_3948_call(), 0)
call_5473 = relay.TupleGetItem(func_3949_call(), 0)
output = relay.Tuple([call_5472,])
output2 = relay.Tuple([call_5473,])
func_5494 = relay.Function([], output)
mod['func_5494'] = func_5494
mod = relay.transform.InferType()(mod)
output = func_5494()
func_5495 = relay.Function([], output)
mutated_mod['func_5495'] = func_5495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1619_call = mod.get_global_var('func_1619')
func_1620_call = mutated_mod.get_global_var('func_1620')
call_5543 = relay.TupleGetItem(func_1619_call(), 0)
call_5544 = relay.TupleGetItem(func_1620_call(), 0)
func_4425_call = mod.get_global_var('func_4425')
func_4427_call = mutated_mod.get_global_var('func_4427')
const_5556 = relay.const([7.660981,-2.153114,9.613772,5.000997,3.133210,3.196086,-4.282451,-7.132577,7.467518,5.791128], dtype = "float64")#candidate|5556|(10,)|const|float64
call_5555 = relay.TupleGetItem(func_4425_call(relay.reshape(const_5556.astype('float64'), [10,])), 1)
call_5557 = relay.TupleGetItem(func_4427_call(relay.reshape(const_5556.astype('float64'), [10,])), 1)
output = relay.Tuple([call_5543,call_5555,const_5556,])
output2 = relay.Tuple([call_5544,call_5557,const_5556,])
func_5560 = relay.Function([], output)
mod['func_5560'] = func_5560
mod = relay.transform.InferType()(mod)
output = func_5560()
func_5561 = relay.Function([], output)
mutated_mod['func_5561'] = func_5561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_385_call = mod.get_global_var('func_385')
func_386_call = mutated_mod.get_global_var('func_386')
call_5576 = func_385_call()
call_5577 = func_385_call()
output = call_5576
output2 = call_5577
func_5589 = relay.Function([], output)
mod['func_5589'] = func_5589
mod = relay.transform.InferType()(mod)
mutated_mod['func_5589'] = func_5589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5589_call = mutated_mod.get_global_var('func_5589')
call_5590 = func_5589_call()
output = call_5590
func_5591 = relay.Function([], output)
mutated_mod['func_5591'] = func_5591
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5618 = relay.var("var_5618", dtype = "uint16", shape = (14, 15, 8))#candidate|5618|(14, 15, 8)|var|uint16
var_5619 = relay.var("var_5619", dtype = "uint16", shape = (14, 15, 8))#candidate|5619|(14, 15, 8)|var|uint16
bop_5620 = relay.multiply(var_5618.astype('uint16'), relay.reshape(var_5619.astype('uint16'), relay.shape_of(var_5618))) # shape=(14, 15, 8)
output = bop_5620
output2 = bop_5620
func_5633 = relay.Function([var_5618,var_5619,], output)
mod['func_5633'] = func_5633
mod = relay.transform.InferType()(mod)
mutated_mod['func_5633'] = func_5633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5633_call = mutated_mod.get_global_var('func_5633')
var_5635 = relay.var("var_5635", dtype = "uint16", shape = (14, 15, 8))#candidate|5635|(14, 15, 8)|var|uint16
var_5636 = relay.var("var_5636", dtype = "uint16", shape = (14, 15, 8))#candidate|5636|(14, 15, 8)|var|uint16
call_5634 = func_5633_call(var_5635,var_5636,)
output = call_5634
func_5637 = relay.Function([var_5635,var_5636,], output)
mutated_mod['func_5637'] = func_5637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5393_call = mod.get_global_var('func_5393')
func_5395_call = mutated_mod.get_global_var('func_5395')
call_5683 = relay.TupleGetItem(func_5393_call(), 1)
call_5684 = relay.TupleGetItem(func_5395_call(), 1)
func_2316_call = mod.get_global_var('func_2316')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_5705 = relay.TupleGetItem(func_2316_call(), 3)
call_5706 = relay.TupleGetItem(func_2318_call(), 3)
func_5393_call = mod.get_global_var('func_5393')
func_5395_call = mutated_mod.get_global_var('func_5395')
call_5716 = relay.TupleGetItem(func_5393_call(), 1)
call_5717 = relay.TupleGetItem(func_5395_call(), 1)
func_4966_call = mod.get_global_var('func_4966')
func_4967_call = mutated_mod.get_global_var('func_4967')
call_5733 = relay.TupleGetItem(func_4966_call(), 0)
call_5734 = relay.TupleGetItem(func_4967_call(), 0)
output = relay.Tuple([call_5683,call_5705,call_5716,call_5733,])
output2 = relay.Tuple([call_5684,call_5706,call_5717,call_5734,])
func_5736 = relay.Function([], output)
mod['func_5736'] = func_5736
mod = relay.transform.InferType()(mod)
mutated_mod['func_5736'] = func_5736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5736_call = mutated_mod.get_global_var('func_5736')
call_5737 = func_5736_call()
output = call_5737
func_5738 = relay.Function([], output)
mutated_mod['func_5738'] = func_5738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4657_call = mod.get_global_var('func_4657')
func_4658_call = mutated_mod.get_global_var('func_4658')
call_5803 = relay.TupleGetItem(func_4657_call(), 0)
call_5804 = relay.TupleGetItem(func_4658_call(), 0)
func_3789_call = mod.get_global_var('func_3789')
func_3791_call = mutated_mod.get_global_var('func_3791')
call_5813 = relay.TupleGetItem(func_3789_call(), 0)
call_5814 = relay.TupleGetItem(func_3791_call(), 0)
output = relay.Tuple([call_5803,call_5813,])
output2 = relay.Tuple([call_5804,call_5814,])
func_5817 = relay.Function([], output)
mod['func_5817'] = func_5817
mod = relay.transform.InferType()(mod)
mutated_mod['func_5817'] = func_5817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5817_call = mutated_mod.get_global_var('func_5817')
call_5818 = func_5817_call()
output = call_5818
func_5819 = relay.Function([], output)
mutated_mod['func_5819'] = func_5819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_861_call = mutated_mod.get_global_var('func_861')
call_5826 = relay.TupleGetItem(func_859_call(), 1)
call_5827 = relay.TupleGetItem(func_861_call(), 1)
output = call_5826
output2 = call_5827
func_5844 = relay.Function([], output)
mod['func_5844'] = func_5844
mod = relay.transform.InferType()(mod)
output = func_5844()
func_5845 = relay.Function([], output)
mutated_mod['func_5845'] = func_5845
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5885 = relay.var("var_5885", dtype = "float64", shape = (5, 10, 16))#candidate|5885|(5, 10, 16)|var|float64
uop_5886 = relay.sigmoid(var_5885.astype('float64')) # shape=(5, 10, 16)
output = relay.Tuple([uop_5886,])
output2 = relay.Tuple([uop_5886,])
func_5892 = relay.Function([var_5885,], output)
mod['func_5892'] = func_5892
mod = relay.transform.InferType()(mod)
var_5893 = relay.var("var_5893", dtype = "float64", shape = (5, 10, 16))#candidate|5893|(5, 10, 16)|var|float64
output = func_5892(var_5893)
func_5894 = relay.Function([var_5893], output)
mutated_mod['func_5894'] = func_5894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5329_call = mod.get_global_var('func_5329')
func_5331_call = mutated_mod.get_global_var('func_5331')
call_5902 = func_5329_call()
call_5903 = func_5329_call()
func_5016_call = mod.get_global_var('func_5016')
func_5018_call = mutated_mod.get_global_var('func_5018')
call_5907 = func_5016_call()
call_5908 = func_5016_call()
output = relay.Tuple([call_5902,call_5907,])
output2 = relay.Tuple([call_5903,call_5908,])
func_5917 = relay.Function([], output)
mod['func_5917'] = func_5917
mod = relay.transform.InferType()(mod)
output = func_5917()
func_5918 = relay.Function([], output)
mutated_mod['func_5918'] = func_5918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3322_call = mod.get_global_var('func_3322')
func_3323_call = mutated_mod.get_global_var('func_3323')
call_5923 = relay.TupleGetItem(func_3322_call(), 1)
call_5924 = relay.TupleGetItem(func_3323_call(), 1)
func_2842_call = mod.get_global_var('func_2842')
func_2843_call = mutated_mod.get_global_var('func_2843')
call_5928 = func_2842_call()
call_5929 = func_2842_call()
func_4994_call = mod.get_global_var('func_4994')
func_4996_call = mutated_mod.get_global_var('func_4996')
call_5947 = func_4994_call()
call_5948 = func_4994_call()
output = relay.Tuple([call_5923,call_5928,call_5947,])
output2 = relay.Tuple([call_5924,call_5929,call_5948,])
func_5956 = relay.Function([], output)
mod['func_5956'] = func_5956
mod = relay.transform.InferType()(mod)
mutated_mod['func_5956'] = func_5956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5956_call = mutated_mod.get_global_var('func_5956')
call_5957 = func_5956_call()
output = call_5957
func_5958 = relay.Function([], output)
mutated_mod['func_5958'] = func_5958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4994_call = mod.get_global_var('func_4994')
func_4996_call = mutated_mod.get_global_var('func_4996')
call_6040 = func_4994_call()
call_6041 = func_4994_call()
output = relay.Tuple([call_6040,])
output2 = relay.Tuple([call_6041,])
func_6054 = relay.Function([], output)
mod['func_6054'] = func_6054
mod = relay.transform.InferType()(mod)
mutated_mod['func_6054'] = func_6054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6054_call = mutated_mod.get_global_var('func_6054')
call_6055 = func_6054_call()
output = call_6055
func_6056 = relay.Function([], output)
mutated_mod['func_6056'] = func_6056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3688_call = mod.get_global_var('func_3688')
func_3689_call = mutated_mod.get_global_var('func_3689')
call_6159 = relay.TupleGetItem(func_3688_call(), 1)
call_6160 = relay.TupleGetItem(func_3689_call(), 1)
func_647_call = mod.get_global_var('func_647')
func_650_call = mutated_mod.get_global_var('func_650')
call_6164 = relay.TupleGetItem(func_647_call(relay.reshape(call_6159.astype('float32'), [10, 8, 12])), 0)
call_6165 = relay.TupleGetItem(func_650_call(relay.reshape(call_6159.astype('float32'), [10, 8, 12])), 0)
func_321_call = mod.get_global_var('func_321')
func_324_call = mutated_mod.get_global_var('func_324')
call_6176 = relay.TupleGetItem(func_321_call(relay.reshape(call_6159.astype('float32'), [10, 8, 12])), 1)
call_6177 = relay.TupleGetItem(func_324_call(relay.reshape(call_6159.astype('float32'), [10, 8, 12])), 1)
output = relay.Tuple([call_6159,call_6164,call_6176,])
output2 = relay.Tuple([call_6160,call_6165,call_6177,])
func_6205 = relay.Function([], output)
mod['func_6205'] = func_6205
mod = relay.transform.InferType()(mod)
mutated_mod['func_6205'] = func_6205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6205_call = mutated_mod.get_global_var('func_6205')
call_6206 = func_6205_call()
output = call_6206
func_6207 = relay.Function([], output)
mutated_mod['func_6207'] = func_6207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2842_call = mod.get_global_var('func_2842')
func_2843_call = mutated_mod.get_global_var('func_2843')
call_6240 = func_2842_call()
call_6241 = func_2842_call()
func_3642_call = mod.get_global_var('func_3642')
func_3646_call = mutated_mod.get_global_var('func_3646')
const_6249 = relay.const([-0.049145,2.121376,2.601751,-7.315913,-1.975813,5.500721,3.350785,-3.899742,7.794179,-5.265410,2.138762,5.259432,-3.848168,6.602562,-3.830949,4.835745,4.799479,-5.870209,5.709839,-7.123109,-0.315445,0.786431,-0.948996,-1.462194,6.852072,-7.173296,7.577735,-2.901253,3.311264,4.832376,-3.054369,-2.395705,-1.852921,-9.703137,0.120405,6.712342,7.451154,-5.862397,-8.975394,6.751547,5.803035,2.326257,-7.587037,-4.009033,5.058225,3.193001,-9.191836,4.590074,9.415928,-1.316235,-1.672141,-6.296458,8.180020,9.204378,8.462484,8.931956,3.910851,0.595115,-1.632015,3.670261,9.242261,1.595736,-0.174040,-0.079410,-3.044046,-4.403972,1.558961,-5.546739,9.043318,-4.976023,0.728272,4.445021,-4.217714,-2.092294,-6.511299,-7.529098,-4.000169,9.323257,4.659752,-4.753811,8.594603,-3.321301,9.826190,4.560794,6.355625,4.657685,0.095640,9.925207,1.025943,-0.744269,2.229577,-9.775757,-9.366525,-2.589474,9.465455,9.958930,6.790625,9.229965,7.311822,-0.319383,7.093704,3.721980,-1.136702,-6.847704,-5.633354,-0.338088,-9.539113,3.385191,-0.679089,-5.914788,8.805377,-4.118126,5.370425,2.240299,-4.877548,4.965446,-3.130514,-5.758136,0.929208,-2.687400,4.562996,5.070604,0.800679,-8.406656,-8.392467,-1.963841,4.003970,8.150454,-7.329552,4.084736,-1.309396,-5.732131,1.887279,3.981198,-9.460045,-1.315917,-4.735878,5.194520,-5.076751,-1.327875,-1.007743,-7.537512,6.935125,-6.237891,4.442413,5.812217,6.864626,-4.975124,-4.714198,7.137156,0.718524,4.749528,-3.399071,-9.039610,-6.970606,0.239403,3.581972,-1.847320,8.061992,-2.742170,-0.423025,-2.756009,-6.957630,-6.193664,2.961596,6.279517,4.326830,-8.991104,5.628112,9.783791,9.881301,-7.865840,-4.811291,-1.290981,6.831271,-1.941886,-2.903028,5.718697,3.634560,8.198687,-0.671473,-0.069734,0.323526,9.415065,9.679181,1.205851,4.233732,4.677170,-4.041320,-6.010916,-6.567025,-4.100110,4.818523,2.938483,5.960054,4.259499,2.059208,-6.794615,1.986778,5.567781,-0.564208,5.605210,-3.034154,2.780216,-5.831730,9.850779,9.959413,6.274408,4.066062,1.661443,-3.848992,-5.436091,-8.626419,-3.869824,-5.778547,-4.465936,-2.167948,7.549230,-7.439689,-2.389767,-8.523357,-6.127529,7.717612,-7.497895,-6.163928,5.143344,3.061296,2.752259,-1.844030,8.505271,5.194916,0.801613,5.961250,7.482835,-7.897787,8.304969,7.225747,-8.490330,4.035899,9.980736,-1.438738,-1.396799,7.213663,-6.562184,-1.761502,-9.332246,6.666374,9.145644,-1.043174,9.142379,-8.943880,4.914959,-9.846241,-2.625543,2.638656,6.596492,1.889962,6.814263,6.965378,-2.989454,7.575858,-8.186088,7.798774,7.557147,-2.554623,-5.580780,2.305329,-7.498411,7.371844,-5.493657,-9.837498,-4.090963,5.990523,-0.448457,6.142400,-1.810409,-3.845019,-2.955288,1.673549,8.183841,-9.412741,-9.282586,-8.665573,0.707952,-7.754936,-4.132367,1.650378,-2.857177,-9.875097,-3.307128,4.365512,-2.904236,7.112954,8.463688,-1.260564,-0.830793,-8.765119,9.392208,2.917904,-5.308497,-8.285820,-9.466111,-2.202949,-9.457331,-0.402476,-5.091304,-3.753168,1.125393,0.057193,-2.417584,7.521296,-3.764638,1.296701,-6.236619,-4.744126,-2.966988,4.468003,5.954055,2.920162,-4.850811,-0.295897,-4.225778,2.644915,-8.090447,-6.798788,4.185823,4.136328,-0.742245,6.536777,4.167715,7.844477,-8.052409,-6.018548,-4.678324,6.082506,8.966711,-4.176118,-1.344132,5.859279,-1.441634,2.369415,-0.389022,-7.840412,-5.426540,9.098180,3.961406,6.088305,-0.442309,2.998317,-7.387617,5.181422,-9.447425,4.117977,-9.745559,9.889006,-8.173143,-8.442766,9.074647,9.366255,-7.528077], dtype = "float64")#candidate|6249|(360,)|const|float64
call_6248 = relay.TupleGetItem(func_3642_call(relay.reshape(const_6249.astype('float64'), [12, 3, 10]), relay.reshape(const_6249.astype('float64'), [12, 3, 10]), ), 1)
call_6250 = relay.TupleGetItem(func_3646_call(relay.reshape(const_6249.astype('float64'), [12, 3, 10]), relay.reshape(const_6249.astype('float64'), [12, 3, 10]), ), 1)
func_501_call = mod.get_global_var('func_501')
func_504_call = mutated_mod.get_global_var('func_504')
var_6268 = relay.var("var_6268", dtype = "int16", shape = (462,))#candidate|6268|(462,)|var|int16
call_6267 = relay.TupleGetItem(func_501_call(relay.reshape(var_6268.astype('int16'), [462,])), 0)
call_6269 = relay.TupleGetItem(func_504_call(relay.reshape(var_6268.astype('int16'), [462,])), 0)
func_3403_call = mod.get_global_var('func_3403')
func_3404_call = mutated_mod.get_global_var('func_3404')
call_6270 = relay.TupleGetItem(func_3403_call(), 1)
call_6271 = relay.TupleGetItem(func_3404_call(), 1)
output = relay.Tuple([call_6240,call_6248,const_6249,call_6267,var_6268,call_6270,])
output2 = relay.Tuple([call_6241,call_6250,const_6249,call_6269,var_6268,call_6271,])
func_6279 = relay.Function([var_6268,], output)
mod['func_6279'] = func_6279
mod = relay.transform.InferType()(mod)
var_6280 = relay.var("var_6280", dtype = "int16", shape = (462,))#candidate|6280|(462,)|var|int16
output = func_6279(var_6280)
func_6281 = relay.Function([var_6280], output)
mutated_mod['func_6281'] = func_6281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5844_call = mod.get_global_var('func_5844')
func_5845_call = mutated_mod.get_global_var('func_5845')
call_6283 = func_5844_call()
call_6284 = func_5844_call()
output = relay.Tuple([call_6283,])
output2 = relay.Tuple([call_6284,])
func_6289 = relay.Function([], output)
mod['func_6289'] = func_6289
mod = relay.transform.InferType()(mod)
output = func_6289()
func_6290 = relay.Function([], output)
mutated_mod['func_6290'] = func_6290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4383_call = mod.get_global_var('func_4383')
func_4384_call = mutated_mod.get_global_var('func_4384')
call_6343 = relay.TupleGetItem(func_4383_call(), 1)
call_6344 = relay.TupleGetItem(func_4384_call(), 1)
output = relay.Tuple([call_6343,])
output2 = relay.Tuple([call_6344,])
func_6375 = relay.Function([], output)
mod['func_6375'] = func_6375
mod = relay.transform.InferType()(mod)
mutated_mod['func_6375'] = func_6375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6375_call = mutated_mod.get_global_var('func_6375')
call_6376 = func_6375_call()
output = call_6376
func_6377 = relay.Function([], output)
mutated_mod['func_6377'] = func_6377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_6378 = relay.TupleGetItem(func_3181_call(), 0)
call_6379 = relay.TupleGetItem(func_3182_call(), 0)
output = relay.Tuple([call_6378,])
output2 = relay.Tuple([call_6379,])
func_6380 = relay.Function([], output)
mod['func_6380'] = func_6380
mod = relay.transform.InferType()(mod)
mutated_mod['func_6380'] = func_6380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6380_call = mutated_mod.get_global_var('func_6380')
call_6381 = func_6380_call()
output = call_6381
func_6382 = relay.Function([], output)
mutated_mod['func_6382'] = func_6382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_818_call = mod.get_global_var('func_818')
func_819_call = mutated_mod.get_global_var('func_819')
call_6383 = relay.TupleGetItem(func_818_call(), 0)
call_6384 = relay.TupleGetItem(func_819_call(), 0)
output = relay.Tuple([call_6383,])
output2 = relay.Tuple([call_6384,])
func_6386 = relay.Function([], output)
mod['func_6386'] = func_6386
mod = relay.transform.InferType()(mod)
mutated_mod['func_6386'] = func_6386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6386_call = mutated_mod.get_global_var('func_6386')
call_6387 = func_6386_call()
output = call_6387
func_6388 = relay.Function([], output)
mutated_mod['func_6388'] = func_6388
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6392 = relay.var("var_6392", dtype = "int32", shape = (16, 5, 9))#candidate|6392|(16, 5, 9)|var|int32
const_6393 = relay.const([[[-7,-10,6,-2,1,10,6,-5,3],[-10,2,-10,8,-7,-1,-2,3,-5],[-3,3,-3,-5,1,8,9,-9,-3],[-3,9,5,-4,-2,10,7,-4,-7],[-5,6,2,2,-1,6,1,6,-9]],[[2,9,-2,1,2,10,-4,4,3],[-3,1,5,9,-5,6,7,1,3],[-7,-5,-2,2,9,6,-4,-6,-5],[10,-7,-1,3,2,-8,-7,1,-7],[6,9,-5,-9,3,6,6,-6,-3]],[[7,-6,9,-6,-2,8,-8,-9,2],[-3,5,-6,-6,6,-5,-8,6,3],[-2,4,4,3,6,2,-6,-7,-10],[3,-7,-7,-10,7,3,-3,-9,-8],[9,-6,3,-1,10,3,2,8,-5]],[[-2,-2,-4,8,-1,-4,-9,-2,6],[-2,6,6,4,5,7,-6,6,-9],[6,-8,4,8,3,-10,-5,7,-4],[3,10,9,8,10,5,6,7,-8],[6,-6,-6,-9,1,-4,-8,5,5]],[[-7,9,-8,-7,8,8,6,-2,4],[-3,10,-6,8,-3,4,-5,8,-10],[-2,1,-2,-4,3,-5,5,-10,9],[-1,-2,8,-10,-6,-10,-5,3,10],[4,-4,-1,8,4,-1,5,-9,-6]],[[-10,-1,7,3,4,9,-1,-10,-4],[5,-7,7,3,-1,9,-1,-6,-7],[4,4,-6,-3,-7,-4,-4,-10,-10],[-10,-1,5,-10,8,9,-10,5,-2],[-8,8,8,6,-2,2,3,5,4]],[[-1,8,-2,-7,1,-8,-3,-10,2],[4,1,-2,8,-6,9,-4,-8,-4],[-9,-5,-10,-3,-9,-5,-2,-9,-7],[-7,-8,9,-5,-10,5,-5,4,3],[3,7,1,-3,1,8,-2,-2,-10]],[[-10,3,-9,-5,-3,4,-2,-3,9],[1,1,-3,-1,-3,-7,-5,9,-6],[-6,-3,-7,6,4,-10,-5,6,-4],[-6,5,-9,4,7,2,4,-4,9],[-3,-3,-4,1,-4,9,5,-5,5]],[[-1,10,2,3,1,2,1,5,-6],[6,2,4,10,-5,10,-8,8,-10],[9,-8,-3,2,-8,7,-8,1,5],[-1,5,-7,-5,5,-5,6,10,-8],[-6,8,-7,-10,-10,-5,4,-7,2]],[[-3,2,-2,5,-5,-6,10,3,-8],[5,-5,6,-9,8,1,-1,-8,-4],[-4,-2,4,1,-10,1,5,3,-8],[-2,1,-2,-1,-9,-10,3,10,2],[-3,-7,9,10,-2,4,2,-9,-9]],[[7,6,10,7,-1,-9,10,-7,-5],[-2,8,8,6,-1,4,7,-1,5],[10,-5,10,3,-5,6,-5,-5,-4],[7,2,6,10,-7,-6,-2,-6,-7],[-2,6,-1,9,3,-8,-8,1,-5]],[[-6,-10,-5,5,3,6,-8,10,-8],[-8,-6,-5,-10,-1,3,-7,2,1],[-4,-9,-10,8,-5,-1,1,4,-10],[2,-9,10,1,-10,5,-2,-2,9],[-6,-9,5,-8,1,4,8,-3,10]],[[-9,-3,6,4,8,-1,-7,3,-9],[-10,-7,-6,4,8,1,3,1,-10],[-5,-6,-10,1,3,-5,-2,-9,8],[1,-1,3,1,5,3,10,2,10],[-3,1,-5,-2,3,-8,-9,7,2]],[[-6,-6,-6,8,7,-1,4,-8,-4],[1,-1,-7,9,10,10,4,4,8],[-8,-5,8,10,4,5,2,-3,-4],[2,8,7,-5,-5,10,-10,-10,1],[-2,8,-10,3,-10,-7,-7,-8,-2]],[[-5,6,7,-3,-2,1,-3,-6,-9],[5,-2,-8,-1,-7,-2,-2,5,6],[3,6,-4,-1,-10,-9,5,10,-1],[6,5,-1,-2,3,2,-9,3,-2],[-4,4,-10,-4,-7,4,-5,9,6]],[[7,4,5,-3,1,-10,3,-6,8],[1,2,-8,-7,-1,-3,6,-4,1],[-6,-6,10,-10,1,-9,-1,-3,-8],[3,2,-2,8,-4,-10,-4,9,5],[-7,2,10,-7,2,6,-8,7,-3]]], dtype = "int32")#candidate|6393|(16, 5, 9)|const|int32
bop_6394 = relay.minimum(var_6392.astype('int32'), relay.reshape(const_6393.astype('int32'), relay.shape_of(var_6392))) # shape=(16, 5, 9)
func_4582_call = mod.get_global_var('func_4582')
func_4585_call = mutated_mod.get_global_var('func_4585')
const_6402 = relay.const([True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False], dtype = "bool")#candidate|6402|(40,)|const|bool
call_6401 = relay.TupleGetItem(func_4582_call(relay.reshape(const_6402.astype('bool'), [40, 1])), 5)
call_6403 = relay.TupleGetItem(func_4585_call(relay.reshape(const_6402.astype('bool'), [40, 1])), 5)
func_3948_call = mod.get_global_var('func_3948')
func_3949_call = mutated_mod.get_global_var('func_3949')
call_6407 = relay.TupleGetItem(func_3948_call(), 0)
call_6408 = relay.TupleGetItem(func_3949_call(), 0)
output = relay.Tuple([bop_6394,call_6401,const_6402,call_6407,])
output2 = relay.Tuple([bop_6394,call_6403,const_6402,call_6408,])
func_6409 = relay.Function([var_6392,], output)
mod['func_6409'] = func_6409
mod = relay.transform.InferType()(mod)
var_6410 = relay.var("var_6410", dtype = "int32", shape = (16, 5, 9))#candidate|6410|(16, 5, 9)|var|int32
output = func_6409(var_6410)
func_6411 = relay.Function([var_6410], output)
mutated_mod['func_6411'] = func_6411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4994_call = mod.get_global_var('func_4994')
func_4996_call = mutated_mod.get_global_var('func_4996')
call_6422 = func_4994_call()
call_6423 = func_4994_call()
output = relay.Tuple([call_6422,])
output2 = relay.Tuple([call_6423,])
func_6436 = relay.Function([], output)
mod['func_6436'] = func_6436
mod = relay.transform.InferType()(mod)
output = func_6436()
func_6437 = relay.Function([], output)
mutated_mod['func_6437'] = func_6437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4657_call = mod.get_global_var('func_4657')
func_4658_call = mutated_mod.get_global_var('func_4658')
call_6445 = relay.TupleGetItem(func_4657_call(), 0)
call_6446 = relay.TupleGetItem(func_4658_call(), 0)
func_4880_call = mod.get_global_var('func_4880')
func_4881_call = mutated_mod.get_global_var('func_4881')
call_6454 = relay.TupleGetItem(func_4880_call(), 0)
call_6455 = relay.TupleGetItem(func_4881_call(), 0)
output = relay.Tuple([call_6445,call_6454,])
output2 = relay.Tuple([call_6446,call_6455,])
func_6458 = relay.Function([], output)
mod['func_6458'] = func_6458
mod = relay.transform.InferType()(mod)
mutated_mod['func_6458'] = func_6458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6458_call = mutated_mod.get_global_var('func_6458')
call_6459 = func_6458_call()
output = call_6459
func_6460 = relay.Function([], output)
mutated_mod['func_6460'] = func_6460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_861_call = mutated_mod.get_global_var('func_861')
call_6495 = relay.TupleGetItem(func_859_call(), 1)
call_6496 = relay.TupleGetItem(func_861_call(), 1)
const_6504 = relay.const([[[-1,-2,8,-1,-8,8,7,-5,7,3,3,-3],[9,4,-4,5,-2,10,-5,-5,-1,3,3,3],[7,9,3,10,6,5,-7,-5,-7,10,-8,-7],[10,-7,7,-2,7,4,-3,-3,8,-9,10,5],[1,-9,2,5,5,-4,-3,9,-8,-3,9,10],[-4,4,2,-1,-7,-1,-8,1,-10,10,-1,-3],[-3,-10,2,10,8,2,-3,3,5,1,10,-1],[-8,2,-1,10,3,6,9,-3,-10,-7,8,-5]],[[3,10,-9,-2,3,10,-10,8,2,9,10,10],[-5,-4,-8,9,4,-5,-2,4,2,9,-4,-7],[3,-8,6,-4,7,-7,7,-8,-7,6,1,-5],[3,7,3,4,8,8,1,6,-7,5,-10,5],[-6,-7,2,-8,-7,2,8,5,-7,-1,-2,8],[-1,5,4,9,2,4,1,9,-10,-10,-7,4],[8,4,-4,3,-5,-7,6,-10,-5,2,-10,-3],[-2,-9,-8,4,-8,-7,-3,10,-7,-1,-4,-3]],[[5,4,-8,6,-10,10,-7,5,5,10,4,-9],[8,6,-9,2,8,-1,-2,8,-3,-1,5,8],[10,9,9,-5,-6,-8,3,2,5,-10,2,1],[8,-8,10,2,-5,3,1,-10,10,3,-7,7],[-8,-10,-4,-10,3,-5,5,2,-10,-5,-5,-7],[4,-10,-5,-4,3,5,-7,2,-2,-4,4,-8],[-2,-5,-9,-4,4,-5,-1,2,-7,3,-2,3],[-2,3,-4,10,6,-3,-10,10,-10,-1,-6,-7]],[[1,-6,-7,-9,7,-4,-2,6,-10,3,-7,1],[7,-10,-6,7,-1,10,-3,6,10,-10,-4,10],[-7,-3,-7,-2,10,-1,-1,4,3,-9,-5,-6],[-6,-9,5,6,4,8,6,8,-4,-2,7,-8],[-2,-5,-3,-1,-1,9,10,10,5,-7,-8,8],[-2,-6,6,7,10,-4,7,1,-8,4,6,-3],[-1,-3,-3,-10,9,6,-1,-7,9,3,-9,-3],[-5,-4,-4,1,7,-6,-4,7,-4,1,8,-6]],[[9,4,-4,-4,8,1,5,7,7,-4,10,4],[-6,9,5,2,3,-4,5,-7,8,-2,1,6],[-3,-8,-2,6,9,4,9,10,2,-10,-5,-9],[-6,-7,2,-4,2,9,6,1,-9,1,-1,-1],[-8,1,9,-6,4,-1,-5,-3,-8,-2,-8,-2],[-10,-6,-4,7,9,5,9,-4,-3,1,-1,-6],[9,-5,-2,3,-10,6,-5,5,-8,-5,-10,-2],[-5,2,9,6,7,-2,-10,5,-3,3,-2,5]],[[9,-9,-8,-3,-5,-8,-4,-2,-8,1,9,-8],[-5,-2,1,6,-5,2,-7,-6,-1,-9,-9,-5],[-5,-6,2,-9,-7,3,10,2,8,1,-1,10],[-9,7,7,-6,-2,-9,6,-3,-2,-5,-8,8],[-10,-1,-3,-3,9,-2,-5,1,1,-2,-1,-2],[-1,-3,-3,-7,7,-6,-1,7,-10,-6,-7,10],[6,-7,-5,10,-7,7,2,-4,1,3,8,2],[9,3,-3,-6,-3,8,3,5,8,1,-5,-3]],[[5,-8,6,-3,8,-2,6,-1,-10,-10,8,-4],[-7,-10,-10,-9,-1,-1,9,-1,-9,9,1,-8],[-1,-6,4,-5,5,-5,8,-1,3,5,6,-8],[-1,10,-8,-4,7,-8,-8,-1,-8,-7,10,-5],[-7,-6,10,-8,2,-4,-6,-7,-8,1,-8,10],[-9,-4,4,2,2,6,2,5,-2,4,7,1],[6,1,6,-2,8,-4,5,-4,5,-1,4,3],[-6,3,8,-9,6,2,3,7,-10,-4,10,-4]],[[-1,-4,-2,10,5,1,7,-2,4,-7,8,10],[6,4,3,-10,6,9,2,8,-5,3,-1,-7],[8,1,7,-5,5,-8,1,5,4,7,-5,5],[4,-2,-2,-1,4,-8,3,-5,-5,9,10,3],[-7,-2,-7,-2,3,-7,4,7,10,-10,-9,3],[9,1,-5,-5,-7,5,-2,-5,3,-3,-10,7],[-8,-4,4,-2,-9,-2,7,7,4,8,-2,-4],[4,2,-8,3,5,-2,5,2,6,8,-3,7]],[[-10,-7,7,5,-9,-3,-5,-4,8,-9,-1,-8],[-5,10,3,7,-4,6,-6,-1,8,-1,-4,3],[-2,-4,-3,1,9,8,-1,-5,-9,-6,-2,7],[3,-4,6,7,-10,-2,5,3,-5,8,-5,-2],[-6,7,-7,9,-4,-5,2,8,-6,5,4,-7],[-8,-8,8,5,-2,3,9,-7,6,-5,7,10],[-6,7,2,2,7,-3,1,8,-10,-3,4,2],[-6,-8,-2,6,-5,9,-7,9,10,8,8,7]],[[8,9,-1,-1,9,10,10,-9,-1,2,7,1],[-3,-3,6,1,9,5,10,-7,-7,-8,2,-2],[6,-8,-7,-2,-7,-1,4,-8,-9,-3,1,6],[6,7,-1,-9,-6,10,8,-2,-7,-10,3,4],[-3,1,-6,5,2,9,2,-2,9,-2,6,-3],[-6,-3,-3,3,3,-1,2,2,10,9,1,10],[5,-8,7,3,-6,-6,-5,-6,-4,1,5,-2],[-7,6,-4,10,10,10,9,3,-2,-6,-8,7]]], dtype = "uint8")#candidate|6504|(10, 8, 12)|const|uint8
bop_6505 = relay.greater_equal(call_6495.astype('bool'), relay.reshape(const_6504.astype('bool'), relay.shape_of(call_6495))) # shape=(10, 8, 12)
bop_6508 = relay.greater_equal(call_6496.astype('bool'), relay.reshape(const_6504.astype('bool'), relay.shape_of(call_6496))) # shape=(10, 8, 12)
uop_6509 = relay.asinh(call_6495.astype('float32')) # shape=(10, 8, 12)
uop_6511 = relay.asinh(call_6496.astype('float32')) # shape=(10, 8, 12)
output = relay.Tuple([bop_6505,uop_6509,])
output2 = relay.Tuple([bop_6508,uop_6511,])
func_6522 = relay.Function([], output)
mod['func_6522'] = func_6522
mod = relay.transform.InferType()(mod)
output = func_6522()
func_6523 = relay.Function([], output)
mutated_mod['func_6523'] = func_6523
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6546 = relay.var("var_6546", dtype = "float64", shape = (13, 12, 3))#candidate|6546|(13, 12, 3)|var|float64
uop_6547 = relay.acos(var_6546.astype('float64')) # shape=(13, 12, 3)
output = uop_6547
output2 = uop_6547
func_6550 = relay.Function([var_6546,], output)
mod['func_6550'] = func_6550
mod = relay.transform.InferType()(mod)
var_6551 = relay.var("var_6551", dtype = "float64", shape = (13, 12, 3))#candidate|6551|(13, 12, 3)|var|float64
output = func_6550(var_6551)
func_6552 = relay.Function([var_6551], output)
mutated_mod['func_6552'] = func_6552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4759_call = mod.get_global_var('func_4759')
func_4761_call = mutated_mod.get_global_var('func_4761')
call_6557 = relay.TupleGetItem(func_4759_call(), 0)
call_6558 = relay.TupleGetItem(func_4761_call(), 0)
output = relay.Tuple([call_6557,])
output2 = relay.Tuple([call_6558,])
func_6559 = relay.Function([], output)
mod['func_6559'] = func_6559
mod = relay.transform.InferType()(mod)
mutated_mod['func_6559'] = func_6559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6559_call = mutated_mod.get_global_var('func_6559')
call_6560 = func_6559_call()
output = call_6560
func_6561 = relay.Function([], output)
mutated_mod['func_6561'] = func_6561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4880_call = mod.get_global_var('func_4880')
func_4881_call = mutated_mod.get_global_var('func_4881')
call_6622 = relay.TupleGetItem(func_4880_call(), 0)
call_6623 = relay.TupleGetItem(func_4881_call(), 0)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_6648 = relay.TupleGetItem(func_3181_call(), 0)
call_6649 = relay.TupleGetItem(func_3182_call(), 0)
output = relay.Tuple([call_6622,call_6648,])
output2 = relay.Tuple([call_6623,call_6649,])
func_6659 = relay.Function([], output)
mod['func_6659'] = func_6659
mod = relay.transform.InferType()(mod)
output = func_6659()
func_6660 = relay.Function([], output)
mutated_mod['func_6660'] = func_6660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1917_call = mod.get_global_var('func_1917')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_6661 = relay.TupleGetItem(func_1917_call(), 0)
call_6662 = relay.TupleGetItem(func_1919_call(), 0)
output = call_6661
output2 = call_6662
func_6664 = relay.Function([], output)
mod['func_6664'] = func_6664
mod = relay.transform.InferType()(mod)
output = func_6664()
func_6665 = relay.Function([], output)
mutated_mod['func_6665'] = func_6665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2979_call = mod.get_global_var('func_2979')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_6684 = func_2979_call()
call_6685 = func_2979_call()
output = call_6684
output2 = call_6685
func_6694 = relay.Function([], output)
mod['func_6694'] = func_6694
mod = relay.transform.InferType()(mod)
output = func_6694()
func_6695 = relay.Function([], output)
mutated_mod['func_6695'] = func_6695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6705 = relay.var("var_6705", dtype = "float64", shape = (13, 1, 5))#candidate|6705|(13, 1, 5)|var|float64
uop_6706 = relay.sinh(var_6705.astype('float64')) # shape=(13, 1, 5)
output = relay.Tuple([uop_6706,])
output2 = relay.Tuple([uop_6706,])
func_6711 = relay.Function([var_6705,], output)
mod['func_6711'] = func_6711
mod = relay.transform.InferType()(mod)
mutated_mod['func_6711'] = func_6711
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6712 = relay.var("var_6712", dtype = "float64", shape = (13, 1, 5))#candidate|6712|(13, 1, 5)|var|float64
func_6711_call = mutated_mod.get_global_var('func_6711')
call_6713 = func_6711_call(var_6712)
output = call_6713
func_6714 = relay.Function([var_6712], output)
mutated_mod['func_6714'] = func_6714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5016_call = mod.get_global_var('func_5016')
func_5018_call = mutated_mod.get_global_var('func_5018')
call_6721 = func_5016_call()
call_6722 = func_5016_call()
output = call_6721
output2 = call_6722
func_6723 = relay.Function([], output)
mod['func_6723'] = func_6723
mod = relay.transform.InferType()(mod)
output = func_6723()
func_6724 = relay.Function([], output)
mutated_mod['func_6724'] = func_6724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1619_call = mod.get_global_var('func_1619')
func_1620_call = mutated_mod.get_global_var('func_1620')
call_6820 = relay.TupleGetItem(func_1619_call(), 0)
call_6821 = relay.TupleGetItem(func_1620_call(), 0)
var_6827 = relay.var("var_6827", dtype = "float32", shape = (10, 8, 12))#candidate|6827|(10, 8, 12)|var|float32
bop_6828 = relay.bitwise_and(call_6820.astype('int16'), relay.reshape(var_6827.astype('int16'), relay.shape_of(call_6820))) # shape=(10, 8, 12)
bop_6831 = relay.bitwise_and(call_6821.astype('int16'), relay.reshape(var_6827.astype('int16'), relay.shape_of(call_6821))) # shape=(10, 8, 12)
output = relay.Tuple([bop_6828,])
output2 = relay.Tuple([bop_6831,])
func_6860 = relay.Function([var_6827,], output)
mod['func_6860'] = func_6860
mod = relay.transform.InferType()(mod)
mutated_mod['func_6860'] = func_6860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6861 = relay.var("var_6861", dtype = "float32", shape = (10, 8, 12))#candidate|6861|(10, 8, 12)|var|float32
func_6860_call = mutated_mod.get_global_var('func_6860')
call_6862 = func_6860_call(var_6861)
output = call_6862
func_6863 = relay.Function([var_6861], output)
mutated_mod['func_6863'] = func_6863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5406_call = mod.get_global_var('func_5406')
func_5408_call = mutated_mod.get_global_var('func_5408')
call_6908 = func_5406_call()
call_6909 = func_5406_call()
output = relay.Tuple([call_6908,])
output2 = relay.Tuple([call_6909,])
func_6918 = relay.Function([], output)
mod['func_6918'] = func_6918
mod = relay.transform.InferType()(mod)
output = func_6918()
func_6919 = relay.Function([], output)
mutated_mod['func_6919'] = func_6919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6918_call = mod.get_global_var('func_6918')
func_6919_call = mutated_mod.get_global_var('func_6919')
call_6928 = relay.TupleGetItem(func_6918_call(), 0)
call_6929 = relay.TupleGetItem(func_6919_call(), 0)
func_6860_call = mod.get_global_var('func_6860')
func_6863_call = mutated_mod.get_global_var('func_6863')
call_6935 = relay.TupleGetItem(func_6860_call(relay.reshape(call_6928.astype('float32'), [10, 8, 12])), 0)
call_6936 = relay.TupleGetItem(func_6863_call(relay.reshape(call_6928.astype('float32'), [10, 8, 12])), 0)
bop_6949 = relay.bitwise_or(call_6928.astype('uint64'), relay.reshape(call_6935.astype('uint64'), relay.shape_of(call_6928))) # shape=(10, 8, 12)
bop_6952 = relay.bitwise_or(call_6929.astype('uint64'), relay.reshape(call_6936.astype('uint64'), relay.shape_of(call_6929))) # shape=(10, 8, 12)
output = relay.Tuple([bop_6949,])
output2 = relay.Tuple([bop_6952,])
func_6976 = relay.Function([], output)
mod['func_6976'] = func_6976
mod = relay.transform.InferType()(mod)
mutated_mod['func_6976'] = func_6976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6976_call = mutated_mod.get_global_var('func_6976')
call_6977 = func_6976_call()
output = call_6977
func_6978 = relay.Function([], output)
mutated_mod['func_6978'] = func_6978
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7018 = relay.var("var_7018", dtype = "float64", shape = (5, 2, 1))#candidate|7018|(5, 2, 1)|var|float64
uop_7019 = relay.sin(var_7018.astype('float64')) # shape=(5, 2, 1)
output = uop_7019
output2 = uop_7019
F = relay.Function([var_7018,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7018,], output2)
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
