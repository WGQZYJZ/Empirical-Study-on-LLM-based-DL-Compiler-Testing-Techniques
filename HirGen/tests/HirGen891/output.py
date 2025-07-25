import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_297 = relay.const([[[2,-4,-8,1,5,-5,-8,6],[-3,8,3,5,-9,2,9,7],[-7,-4,-6,-10,4,1,-2,-2],[1,-9,5,2,10,3,-7,-3],[-3,-7,5,-1,3,-3,-10,3],[2,-6,8,1,1,7,6,10],[8,-8,7,2,-3,6,-9,-5],[-1,-7,10,-6,6,8,-5,1],[10,-6,9,6,4,-5,10,-3],[-4,9,2,4,-1,10,-5,-9],[8,-9,-5,1,6,4,8,5],[10,6,9,10,4,-6,-10,-3]],[[2,7,6,9,-6,8,-2,7],[-8,4,5,-7,-5,-10,-8,5],[-5,-9,10,3,-1,-9,-3,-5],[-9,8,6,-5,-10,5,-7,10],[-3,-1,7,9,6,-2,-4,9],[7,-9,5,-5,-10,5,-3,7],[3,8,-5,-9,5,-7,-8,4],[6,-10,7,5,8,-5,4,4],[2,-7,-1,8,-6,4,-3,-3],[2,-9,-9,-6,-6,-7,-5,-8],[-4,-3,-1,-10,-6,-3,3,-8],[-9,3,1,6,-2,-8,5,3]],[[-2,4,-9,-10,-9,6,1,6],[-10,10,10,-1,-1,1,-6,5],[5,9,4,-1,-4,-4,8,5],[-8,-1,2,-3,10,1,8,-4],[-7,-7,4,-1,-2,3,4,-9],[-2,-9,2,-9,5,10,8,-6],[-9,-4,-10,1,-2,5,-2,-8],[-5,-1,8,1,2,9,-5,4],[8,7,5,-2,-4,-4,-1,3],[9,5,5,-3,7,-6,-6,6],[-8,-4,3,-3,4,3,10,-1],[9,-10,-2,-9,6,-3,8,8]],[[2,-3,9,4,-3,-9,3,6],[8,4,1,-10,3,-9,3,-6],[-3,-2,5,8,-2,-5,-6,5],[-6,-5,6,-4,-9,7,2,8],[4,-8,7,7,2,4,-2,4],[-10,5,-4,-5,1,6,-9,9],[-8,10,-2,3,-10,3,-6,10],[-8,3,3,7,-4,-7,1,4],[-4,3,3,1,-4,7,-1,-7],[-3,3,2,8,-4,7,-3,-5],[7,-3,5,-6,-8,9,2,-10],[-10,-9,-10,-6,-5,2,-6,-5]],[[4,-3,-1,5,4,1,-2,2],[-2,2,-9,-8,5,-2,-6,4],[-4,6,8,7,7,-1,-6,1],[-4,-2,5,-7,10,9,-8,-4],[10,10,-3,-1,2,9,2,8],[3,9,7,-6,7,5,-8,10],[10,7,6,4,-9,9,-3,9],[4,3,4,-2,-7,-10,5,5],[9,-9,-2,-6,5,2,10,-3],[-9,-8,8,-8,7,1,6,-7],[10,2,10,2,-3,5,-8,-10],[7,-2,7,9,5,-6,-8,10]],[[1,-9,-1,-6,7,-8,10,-10],[5,1,1,8,1,-9,-6,-8],[-2,-8,8,-7,-7,-10,2,-5],[3,9,-7,-1,10,9,10,5],[-2,5,10,7,-7,-6,8,-6],[-1,-4,-9,-9,7,-6,-3,9],[3,7,7,1,-2,5,-2,2],[5,2,-3,4,6,6,-1,7],[10,7,10,5,9,-4,10,-2],[2,-10,6,-4,4,-4,-7,-8],[4,6,5,8,1,5,-7,-6],[-3,-5,-10,1,-9,8,-5,4]],[[-2,-3,-2,-3,2,6,-6,-10],[9,-10,-4,-3,-6,-10,-7,-10],[5,-10,-4,-1,2,10,2,-9],[-3,9,9,-2,-5,6,7,1],[-9,10,-3,-2,10,4,-1,-2],[1,-2,7,5,-6,-4,-7,4],[5,9,-9,-4,2,3,-3,8],[10,4,5,9,-2,-6,-5,5],[6,-1,-7,-8,-5,4,7,1],[3,-5,7,-2,7,8,-10,-4],[-8,-3,-10,-6,1,-2,-2,-8],[-8,-5,-8,-4,7,-7,-6,3]],[[-5,-9,-9,-1,-2,1,-4,1],[1,-7,-5,4,-4,8,1,3],[10,-3,6,-9,5,-4,-8,-2],[-1,8,1,-7,-2,-4,8,8],[-9,5,5,6,4,2,5,3],[-5,1,2,3,-2,-8,4,8],[-9,1,-7,-5,-8,-4,-2,-10],[-7,-5,8,-4,4,-3,-8,-2],[-4,-10,-1,-3,-3,-2,2,-6],[-3,-10,10,5,6,2,9,-10],[8,-3,6,-6,2,5,-1,5],[-3,-9,10,7,-10,-9,-5,-1]],[[8,10,9,-2,5,9,10,4],[-10,6,-4,6,-4,-4,-4,1],[-8,-6,8,-10,-5,1,-4,9],[-7,-5,-2,5,-8,4,-4,5],[-8,9,-9,9,9,-9,6,-8],[-7,-1,4,4,7,-5,4,4],[-9,6,-3,1,-6,4,2,-2],[-5,-5,-3,2,-6,-2,4,-2],[1,2,4,6,8,3,-2,-7],[10,-7,-1,-4,5,-7,3,4],[9,8,1,-5,-3,-9,3,-3],[7,7,-8,-7,8,2,5,-7]],[[-1,-8,-8,3,3,-8,5,-1],[-3,4,-1,4,5,3,1,-4],[5,-9,9,4,-2,-6,6,-1],[8,-8,-6,-6,-8,3,-9,4],[-1,4,-4,1,3,-3,7,-5],[1,1,8,10,-8,-7,-10,-8],[-3,2,-3,3,10,-4,-4,-1],[-2,4,-2,6,-7,-7,-4,-9],[-7,6,6,7,-7,-5,8,8],[8,2,6,10,-10,2,1,-3],[-4,2,10,8,-8,8,8,-10],[8,8,9,-9,6,5,3,-8]],[[8,-9,-9,6,7,-5,-2,3],[4,-3,-1,4,-2,-7,-10,3],[6,8,8,-3,10,2,-1,-9],[8,2,4,1,6,4,4,3],[1,5,5,-6,6,-6,-5,-3],[-7,-6,-10,1,-4,1,-2,8],[-8,-3,-1,-8,7,3,9,6],[-1,-8,-9,9,2,1,-6,7],[2,-7,-7,9,6,-7,-9,10],[-7,-3,7,-8,-1,5,8,3],[2,-2,-2,-4,-6,-3,5,-5],[4,-7,-9,2,-3,-9,-8,10]]], dtype = "int8")#candidate|297|(11, 12, 8)|const|int8
var_298 = relay.var("var_298", dtype = "int8", shape = (11, 12, 8))#candidate|298|(11, 12, 8)|var|int8
bop_299 = relay.minimum(const_297.astype('int8'), relay.reshape(var_298.astype('int8'), relay.shape_of(const_297))) # shape=(11, 12, 8)
output = relay.Tuple([bop_299,])
output2 = relay.Tuple([bop_299,])
func_322 = relay.Function([var_298,], output)
mod['func_322'] = func_322
mod = relay.transform.InferType()(mod)
mutated_mod['func_322'] = func_322
mutated_mod = relay.transform.InferType()(mutated_mod)
var_323 = relay.var("var_323", dtype = "int8", shape = (11, 12, 8))#candidate|323|(11, 12, 8)|var|int8
func_322_call = mutated_mod.get_global_var('func_322')
call_324 = func_322_call(var_323)
output = call_324
func_325 = relay.Function([var_323], output)
mutated_mod['func_325'] = func_325
mutated_mod = relay.transform.InferType()(mutated_mod)
var_454 = relay.var("var_454", dtype = "float64", shape = (10, 6, 11))#candidate|454|(10, 6, 11)|var|float64
var_455 = relay.var("var_455", dtype = "float64", shape = (10, 6, 11))#candidate|455|(10, 6, 11)|var|float64
bop_456 = relay.floor_mod(var_454.astype('float64'), relay.reshape(var_455.astype('float64'), relay.shape_of(var_454))) # shape=(10, 6, 11)
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
var_464 = relay.var("var_464", dtype = "int8", shape = (1056,))#candidate|464|(1056,)|var|int8
call_463 = relay.TupleGetItem(func_322_call(relay.reshape(var_464.astype('int8'), [11, 12, 8])), 0)
call_465 = relay.TupleGetItem(func_325_call(relay.reshape(var_464.astype('int8'), [11, 12, 8])), 0)
output = relay.Tuple([bop_456,call_463,var_464,])
output2 = relay.Tuple([bop_456,call_465,var_464,])
func_481 = relay.Function([var_454,var_455,var_464,], output)
mod['func_481'] = func_481
mod = relay.transform.InferType()(mod)
mutated_mod['func_481'] = func_481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_481_call = mutated_mod.get_global_var('func_481')
var_483 = relay.var("var_483", dtype = "float64", shape = (10, 6, 11))#candidate|483|(10, 6, 11)|var|float64
var_484 = relay.var("var_484", dtype = "float64", shape = (10, 6, 11))#candidate|484|(10, 6, 11)|var|float64
var_485 = relay.var("var_485", dtype = "int8", shape = (1056,))#candidate|485|(1056,)|var|int8
call_482 = func_481_call(var_483,var_484,var_485,)
output = call_482
func_486 = relay.Function([var_483,var_484,var_485,], output)
mutated_mod['func_486'] = func_486
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1170 = relay.const([[[-4.960443],[9.187654],[-3.641846],[2.970825],[7.058546],[4.409528],[0.368684],[-0.300025]],[[-6.284385],[2.386758],[6.421508],[-8.848520],[-6.249343],[-0.589910],[7.452477],[2.477379]],[[-6.163267],[-1.696927],[-1.776931],[6.934234],[-2.111020],[-3.738427],[-4.534116],[4.761880]],[[-8.386403],[8.881139],[0.917553],[1.516548],[-8.529729],[4.456334],[2.988145],[8.829261]],[[1.256891],[-0.174491],[-9.877285],[9.760803],[-4.805993],[-0.760175],[-4.576337],[4.680759]]], dtype = "float64")#candidate|1170|(5, 8, 1)|const|float64
uop_1171 = relay.sigmoid(const_1170.astype('float64')) # shape=(5, 8, 1)
output = uop_1171
output2 = uop_1171
func_1176 = relay.Function([], output)
mod['func_1176'] = func_1176
mod = relay.transform.InferType()(mod)
mutated_mod['func_1176'] = func_1176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1176_call = mutated_mod.get_global_var('func_1176')
call_1177 = func_1176_call()
output = call_1177
func_1178 = relay.Function([], output)
mutated_mod['func_1178'] = func_1178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_1208 = func_1176_call()
call_1209 = func_1176_call()
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_1212 = func_1176_call()
call_1213 = func_1176_call()
output = relay.Tuple([call_1208,call_1212,])
output2 = relay.Tuple([call_1209,call_1213,])
func_1214 = relay.Function([], output)
mod['func_1214'] = func_1214
mod = relay.transform.InferType()(mod)
output = func_1214()
func_1215 = relay.Function([], output)
mutated_mod['func_1215'] = func_1215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_1295 = relay.TupleGetItem(func_1214_call(), 0)
call_1296 = relay.TupleGetItem(func_1215_call(), 0)
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
var_1311 = relay.var("var_1311", dtype = "int8", shape = (1056,))#candidate|1311|(1056,)|var|int8
call_1310 = relay.TupleGetItem(func_322_call(relay.reshape(var_1311.astype('int8'), [11, 12, 8])), 0)
call_1312 = relay.TupleGetItem(func_325_call(relay.reshape(var_1311.astype('int8'), [11, 12, 8])), 0)
uop_1313 = relay.asin(call_1310.astype('float32')) # shape=(11, 12, 8)
uop_1315 = relay.asin(call_1312.astype('float32')) # shape=(11, 12, 8)
func_481_call = mod.get_global_var('func_481')
func_486_call = mutated_mod.get_global_var('func_486')
const_1329 = relay.const([9.343107,5.015337,-3.904388,-3.700022,-8.126484,2.556801,8.641334,-0.487539,-7.201290,-4.202412,-4.274745,-2.350517,-3.258137,8.866640,3.373512,4.306428,-4.125057,-7.125073,3.311241,4.765331,-3.773500,8.984676,-4.878900,-8.191399,9.367874,-9.250665,6.310067,-7.808139,4.331770,2.533732,-9.637622,9.063320,0.201215,-8.881050,9.994721,-8.125876,-1.251038,2.705907,0.230845,2.786078,3.333153,3.308258,-1.779677,-2.910192,6.290132,-8.437964,-1.303687,-2.987113,-7.919415,-9.726526,-0.430604,3.172503,-3.704835,0.273783,-2.367329,-4.332508,7.711749,-7.206396,5.274678,1.369256,2.589732,2.265823,-6.389145,1.469951,-0.792669,-4.344602,3.004619,5.614830,-6.232976,7.848135,0.214657,-5.269916,3.774211,7.211750,2.221756,7.947775,-7.136814,-9.736913,-9.032338,8.136528,1.262471,6.812677,6.013904,-1.495357,-8.126485,-3.271571,1.611052,-1.947264,-7.880685,-5.931079,-6.253151,-0.242188,-0.379257,3.444740,-2.884534,9.175515,-6.480473,-6.985703,2.469265,-9.908547,4.747966,9.840629,0.146428,3.649518,1.853207,-7.213495,-3.276111,0.115473,6.062924,7.786427,7.083494,-8.866975,-7.007507,-9.782586,4.089010,2.686941,6.901231,-3.931107,-1.122210,-0.959079,5.407306,0.930679,1.781902,-2.100424,-4.614653,6.416812,-4.035609,3.103698,-7.723911,-7.035901,-8.652030,-3.182541,-0.356317,3.074955,3.955459,0.327298,-0.067136,-4.360964,6.687577,-9.126420,-0.513355,6.680450,1.148400,8.773602,-3.904464,-2.428117,7.493407,5.009857,9.219072,-8.461127,-1.348827,4.449499,9.331249,2.305184,-8.787890,-6.961856,6.877874,5.763773,-8.842843,-3.473599,-9.583630,-0.316977,-3.997815,5.199110,-6.523041,-0.647908,3.829185,4.306928,4.331993,8.192263,-7.239161,-0.388446,-7.273883,0.322295,8.134480,3.911521,-0.247333,1.117159,9.633881,-3.239331,1.652558,4.219558,-2.195353,1.308871,8.371049,2.315637,-3.879471,4.306463,4.471278,3.539856,-4.049145,-8.340979,-2.561921,6.721731,-7.350936,3.573083,-6.025422,3.026890,8.068926,-4.845709,8.837107,5.522188,-0.119906,-0.968278,9.138376,-9.389473,0.117292,-4.424122,-1.324516,7.324061,4.027720,-0.107115,4.958719,-8.529002,-2.175653,4.800978,-1.164264,3.810670,3.665683,-3.919130,-0.970610,9.793429,0.454489,7.850200,8.915906,-9.907948,-4.819004,2.784008,-0.073427,-9.207920,-5.215061,4.526597,-7.736437,3.562361,-4.485234,-0.862791,-8.315565,-0.058017,1.237868,-8.993505,3.587052,7.367950,3.889100,5.805616,-5.493362,0.274244,-6.152608,3.774277,1.860707,-5.654714,-7.278454,-4.677329,-4.866176,-9.082285,2.263248,5.127009,-5.602838,-6.181944,6.736497,6.180587,1.926058,-7.742644,7.410776,7.233561,6.979252,6.453993,-9.370240,-0.190454,-6.980007,0.953811,1.358337,-6.542327,5.539703,-1.731295,6.771882,1.961504,-1.270991,-5.640919,7.217954,-7.241599,1.592295,3.655673,-9.567889,4.543559,-8.599519,-8.009995,8.699623,5.329515,8.665495,1.774569,-7.242933,3.079505,-0.933076,-3.553448,8.108366,-1.122564,-7.801355,6.225524,-5.831974,-7.714981,6.985637,-1.689818,2.611220,2.740381,6.211275,0.976302,4.588662,-4.845922,-0.092296,-8.246213,-5.158046,4.557708,-3.593136,3.592369,9.599056,0.266274,-7.720866,4.413811,-9.553757,-7.836613,1.268914,9.872887,-9.779493,-5.453625,-8.196995,2.382241,-5.962213,-1.667940,3.446418,9.710995,2.910236,7.410793,-4.283730,5.976315,8.399701,4.838365,-8.770762,-0.334314,-3.475348,5.068040,7.556633,3.771612,8.187486,-6.548151,2.219909,2.112441,-2.860018,-4.347837,7.444136,7.822645,0.692442,8.989470,6.042138,2.064748,0.446890,2.082924,7.189555,-8.724802,-1.644656,1.118837,-9.038556,-8.297933,6.714142,4.318628,-2.205510,6.302570,5.346164,2.915029,-8.664703,7.710715,-1.713620,-5.004943,4.714805,-7.640515,9.045932,-5.415579,6.155525,5.464084,3.576574,0.716740,9.628056,-0.610222,-6.209877,-2.992243,-9.254926,-3.506719,-2.835604,-0.966997,8.490891,2.617329,-8.151652,-0.352254,-6.663239,-2.045655,-7.990503,5.203313,-4.371631,1.415186,-0.628556,-2.723525,5.883885,7.467513,6.324906,1.062001,-8.863318,-2.454912,-5.967515,-8.680736,-8.409163,2.470549,5.187867,-7.760962,-7.080704,-0.278823,1.655244,3.981293,0.456045,-1.381342,-6.734719,5.553397,-2.630768,3.118180,-6.712460,1.058442,-2.919605,4.371115,-0.395066,7.279607,0.438060,7.572741,-9.124075,1.922622,7.305808,7.808538,-3.668408,-6.581313,-1.018080,3.565008,-6.855507,2.995801,6.289337,-5.034972,-4.451755,-6.080164,0.314960,2.573466,-3.935280,3.368211,-7.063655,1.627989,1.152595,-7.341602,7.042369,-9.954351,-0.137784,-8.012444,-0.831255,3.848183,4.157940,2.137795,0.591320,-7.544641,6.236345,3.301835,-0.196192,-7.771710,5.243732,8.914250,0.177272,-9.342155,1.167715,8.424332,5.281081,6.045274,0.590152,4.740637,7.265396,-3.120550,6.389732,-5.818944,3.795918,6.111066,8.796941,9.436034,-9.573024,6.907929,8.216525,5.137803,9.525001,7.344841,5.028316,-7.448515,-4.312190,-3.294082,-0.832495,-8.083782,1.905522,-0.154829,-2.029743,5.268047,6.536614,9.738176,-7.724367,1.877038,0.203015,-1.566101,7.705127,8.588225,4.852437,4.160853,-4.153986,3.644656,9.371538,9.362471,-5.814736,-9.390957,4.005385,-8.059990,9.639472,5.576869,-5.186288,8.634336,-8.471930,9.474184,-5.198369,-6.250487,-4.141673,0.012552,8.313152,-3.523799,8.748263,-1.349926,-0.858159,-9.943951,-5.087421,-4.764335,0.749635,2.914981,-0.696868,-5.358197,8.866095,0.295460,-5.799252,-8.306282,7.574693,0.714931,3.965698,5.742984,-4.520760,8.190865,-1.979684,8.714900,-8.723297,8.055068,-5.154908,8.340850,-0.495521,7.807519,8.417114,6.500223,-6.260720,-5.265308,-5.287105,9.120138,2.314522,7.604989,-3.935372,-7.204554,2.575838,4.392944,7.986758,-2.470296,-8.122522,-8.963139,4.945158,-7.383383,0.036745,7.444870,3.054651,-0.045286,-4.787463,-6.346901,6.679828,6.710063,-7.151836,-0.250495,3.791811,-5.271887,-3.538174,-2.378934,-9.579530,-0.476344,7.756444,6.840452,-4.492358,5.163261,1.336020,-4.554315,-0.666909,-6.632023,-9.409410,-8.722615,2.040899,9.622602,-4.839632,2.548802,8.171158,-5.297827,6.194315,6.320652,1.908940,-8.110410,-4.857423,1.041012,-6.358858,0.611561,-5.260647,8.531495,-5.073476,-7.299149,-0.835526,1.708565,0.897158,-1.708602,3.039312,-8.816590,-6.699623,-5.396105,1.631059,-0.893514,2.031013,9.823133,4.867759,4.808573,4.151603,-5.156822,4.248902,0.256694,2.662154,4.357047,1.997503,-0.179982,1.289632,-1.983266,-0.942794,-9.328410,0.039458,-5.805940,-9.009057,-1.387206,2.580471,8.268663,8.032061,5.825354,-9.860556,1.661635,-3.800820,-3.103341,-6.970917,0.658678], dtype = "float64")#candidate|1329|(660,)|const|float64
call_1328 = relay.TupleGetItem(func_481_call(relay.reshape(const_1329.astype('float64'), [10, 6, 11]), relay.reshape(const_1329.astype('float64'), [10, 6, 11]), relay.reshape(var_1311.astype('int8'), [1056,]), ), 1)
call_1330 = relay.TupleGetItem(func_486_call(relay.reshape(const_1329.astype('float64'), [10, 6, 11]), relay.reshape(const_1329.astype('float64'), [10, 6, 11]), relay.reshape(var_1311.astype('int8'), [1056,]), ), 1)
output = relay.Tuple([call_1295,var_1311,uop_1313,call_1328,const_1329,])
output2 = relay.Tuple([call_1296,var_1311,uop_1315,call_1330,const_1329,])
func_1331 = relay.Function([var_1311,], output)
mod['func_1331'] = func_1331
mod = relay.transform.InferType()(mod)
mutated_mod['func_1331'] = func_1331
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1332 = relay.var("var_1332", dtype = "int8", shape = (1056,))#candidate|1332|(1056,)|var|int8
func_1331_call = mutated_mod.get_global_var('func_1331')
call_1333 = func_1331_call(var_1332)
output = call_1333
func_1334 = relay.Function([var_1332], output)
mutated_mod['func_1334'] = func_1334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1338 = relay.var("var_1338", dtype = "float32", shape = (7, 10, 4))#candidate|1338|(7, 10, 4)|var|float32
uop_1339 = relay.sqrt(var_1338.astype('float32')) # shape=(7, 10, 4)
bop_1341 = relay.logical_or(uop_1339.astype('bool'), relay.reshape(var_1338.astype('bool'), relay.shape_of(uop_1339))) # shape=(7, 10, 4)
func_481_call = mod.get_global_var('func_481')
func_486_call = mutated_mod.get_global_var('func_486')
var_1366 = relay.var("var_1366", dtype = "float64", shape = (660,))#candidate|1366|(660,)|var|float64
var_1367 = relay.var("var_1367", dtype = "int8", shape = (1056,))#candidate|1367|(1056,)|var|int8
call_1365 = relay.TupleGetItem(func_481_call(relay.reshape(var_1366.astype('float64'), [10, 6, 11]), relay.reshape(var_1366.astype('float64'), [10, 6, 11]), relay.reshape(var_1367.astype('int8'), [1056,]), ), 1)
call_1368 = relay.TupleGetItem(func_486_call(relay.reshape(var_1366.astype('float64'), [10, 6, 11]), relay.reshape(var_1366.astype('float64'), [10, 6, 11]), relay.reshape(var_1367.astype('int8'), [1056,]), ), 1)
output = relay.Tuple([bop_1341,call_1365,var_1366,var_1367,])
output2 = relay.Tuple([bop_1341,call_1368,var_1366,var_1367,])
func_1376 = relay.Function([var_1338,var_1366,var_1367,], output)
mod['func_1376'] = func_1376
mod = relay.transform.InferType()(mod)
var_1377 = relay.var("var_1377", dtype = "float32", shape = (7, 10, 4))#candidate|1377|(7, 10, 4)|var|float32
var_1378 = relay.var("var_1378", dtype = "float64", shape = (660,))#candidate|1378|(660,)|var|float64
var_1379 = relay.var("var_1379", dtype = "int8", shape = (1056,))#candidate|1379|(1056,)|var|int8
output = func_1376(var_1377,var_1378,var_1379,)
func_1380 = relay.Function([var_1377,var_1378,var_1379,], output)
mutated_mod['func_1380'] = func_1380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_1390 = func_1176_call()
call_1391 = func_1176_call()
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
const_1418 = relay.const([8,5,-10,-5,-6,1,6,-10,-7,10,-10,9,-5,2,10,-4,-9,-4,-9,2,-9,-9,-10,6,9,5,2,7,2,-1,-5,3,-5,-1,-3,10,-7,9,-7,7,2,5,-5,3,-4,-2,-1,-2,-9,3,-7,-5,3,2,-8,7,-10,-6,-5,-2,5,-9,-6,-7,6,-8,4,-9,-7,8,-1,-7,-5,4,4,-2,-10,7,6,3,-5,-6,6,5,-8,1,8,-10,3,-5,-2,7,-10,7,10,7,-3,-4,2,-2,-2,2,1,3,8,2,-6,1,5,3,2,-1,-7,-1,4,-9,-6,-8,-3,-2,10,-10,-7,4,2,7,1,6,1,-5,3,-3,5,8,2,-8,8,-1,-10,4,4,6,7,3,9,5,2,-3,-9,6,2,4,-3,-2,-1,6,10,-1,4,-7,2,7,9,-2,2,10,3,4,8,-10,4,4,-8,1,9,-6,-1,4,4,8,3,10,1,-1,-9,8,8,7,7,9,7,8,2,-10,7,2,8,-7,5,-10,10,8,-1,8,-5,5,-4,-2,4,-3,-1,-4,-9,8,10,8,7,10,3,8,-6,-1,-6,7,6,3,-6,-6,8,1,-3,10,7,8,9,-9,8,5,5,-8,-3,8,-9,-6,-8,7,-8,-1,-8,-6,-4,-1,-6,-8,10,2,6,3,-2,-2,-8,4,-7,-2,4,3,-6,2,-3,-3,-6,-6,-4,-10,10,9,-3,5,-7,-5,6,1,-2,-3,3,8,10,-4,3,-3,7,2,-8,-10,-1,-6,-2,-8,-9,-1,-7,-4,3,5,1,10,1,-8,6,-4,2,5,-8,-8,3,1,-8,-1,2,-8,4,-3,-9,-4,8,3,9,-1,2,5,-9,-7,1,10,2,8,-8,-10,1,-4,-3,8,7,-2,1,6,6,-8,3,-10,-8,2,-9,-10,8,9,1,7,1,8,-7,-3,-10,-7,1,-10,6,-2,4,-5,-6,-6,-6,-8,10,-6,-2,9,-1,7,-4,8,6,-6,2,5,-8,8,1,10,3,10,6,-7,6,9,-10,-1,-7,-9,10,10,4,-3,-5,10,-10,3,-10,5,6,-5,10,-5,6,-9,-9,-6,8,-9,4,-1,10,10,-6,-3,8,-1,7,-9,-1,9,7,2,-5,-8,-10,3,5,-7,10,-7,1,9,5,1,6,5,-5,1,-8,9,10,-8,-5,9,-5,4,-4,4,-2,-7,-4,4,-1,-9,3,-9,-8,-9,-9,6,7,-2,4,-2,2,5,-4,-5,-1,6,-10,9,1,1,-10,-6,9,-8,5,-9,9,-2,10,-10,2,7,2,-10,-7,2,7,2,7,9,10,-10,-2,4,10,5,1,-3,-1,5,-1,-5,5,4,-9,-6,1,-10,8,4,-9,9,-4,-4,-5,-5,5,7,-9,-6,4,-7,-7,7,-2,-5,-2,4,9,5,6,4,-9,-5,-2,9,2,8,-5,-7,7,-2,8,-7,4,5,-1,3,-8,10,-9,5,-7,3,7,2,3,3,8,10,-3,3,-4,5,7,3,6,-9,8,-6,-3,-10,-2,10,6,-3,-7,-2,5,4,-5,-9,-2,4,4,8,8,-6,3,-2,7,8,2,-6,9,10,-6,3,-1,9,-4,-3,-5,5,-4,-6,2,7,-4,-10,3,-5,1,9,2,7,7,2,-8,1,-4,5,1,-10,4,-7,2,-8,-9,-6,4,-1,-1,4,-10,3,2,-9,-1,7,1,-4,6,-7,-8,-6,-4,5,9,-7,6,2,2,-10,-8,-10,-3,-1,8,-3,-1,-9,5,-10,-5,3,1,-9,7,-5,8,-4,-2,9,-5,4,-1,-8,-9,3,9,5,-3,10,4,5,-3,-3,5,2,-4,3,1,4,-4,-6,-4,3,-7,-7,10,-5,2,7,1,7,-8,-3,-4,1,-5,-2,-9,-8,8,9,9,3,3,-7,9,-2,-6,8,-1,9,5,6,-4,2,2,-2,-7,-10,-2,7,-3,-10,3,1,6,-1,-1,9,-1,-9,-2,4,3,2,-5,1,-7,8,-1,-3,9,10,-10,5,-9,6,5,-3,-6,-6,-3,10,7,7,7,7,-5,-7,-5,10,-7,7,8,2,6,-4,4,8,-4,-1,6,-8,-4,-10,7,5,6,-8,4,8,-8,9,-8,7,-2,2,6,-1,-3,1,10,-6,6,1,-3,-9,3,5,3,-3,10,-2,-5,7,3,10,4,2,-9,1,3,-5,8,-10,-1,5,-10,8,-2,-7,-4,10,4,-9,6,7,8,8,3,6,-2,-5,-9,-10,-1,8,6,5,-2,5,2,7,-5,5,-2,-3,-3,-7,-3,-3,-3,-2,-9,-9,1,8,5,5,-2,-9,1,-9,10,9,2,-10,3,6,-10,4,8,-5,9,4,-10,6,-4,-10,-10,10,10,-8,3,-8,8,4,-6,-8,1,-4,6,-6,4,7,-2,-9,8,-7,3,3,7,-7,8,-8,1,4,4,10,-4,4,-5,-10,10,3,3,3,3,3,-7,-4,2,6,6,4,4,-9,10,-1,9,2,-1,-3,8,10,6,-4,2,4,7,-9,5,9,9,6,5,3,-6,2,2,-9,-6,9,-2,-5,1,9,3,-3,-7,4,8,2,4,6,-6,4,-8,7,6,-1,7,4,6,-4,-8,-9,-4,10,4,3,3,-1,2,2,-1,6,-1,-8,10,1,10,4,-2,-1,-10,-6,4,3,5,-6,8,-4,4,5,-4,4,8,-8,-4,-7,-5,-7,-8,7,-6,2,6,-3,10,6,6,-9,-10,7], dtype = "int8")#candidate|1418|(1056,)|const|int8
call_1417 = relay.TupleGetItem(func_322_call(relay.reshape(const_1418.astype('int8'), [11, 12, 8])), 0)
call_1419 = relay.TupleGetItem(func_325_call(relay.reshape(const_1418.astype('int8'), [11, 12, 8])), 0)
output = relay.Tuple([call_1390,call_1417,const_1418,])
output2 = relay.Tuple([call_1391,call_1419,const_1418,])
func_1427 = relay.Function([], output)
mod['func_1427'] = func_1427
mod = relay.transform.InferType()(mod)
output = func_1427()
func_1428 = relay.Function([], output)
mutated_mod['func_1428'] = func_1428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_1524 = relay.TupleGetItem(func_1214_call(), 0)
call_1525 = relay.TupleGetItem(func_1215_call(), 0)
output = relay.Tuple([call_1524,])
output2 = relay.Tuple([call_1525,])
func_1529 = relay.Function([], output)
mod['func_1529'] = func_1529
mod = relay.transform.InferType()(mod)
output = func_1529()
func_1530 = relay.Function([], output)
mutated_mod['func_1530'] = func_1530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1427_call = mod.get_global_var('func_1427')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_1531 = relay.TupleGetItem(func_1427_call(), 0)
call_1532 = relay.TupleGetItem(func_1428_call(), 0)
output = call_1531
output2 = call_1532
func_1540 = relay.Function([], output)
mod['func_1540'] = func_1540
mod = relay.transform.InferType()(mod)
output = func_1540()
func_1541 = relay.Function([], output)
mutated_mod['func_1541'] = func_1541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1540_call = mod.get_global_var('func_1540')
func_1541_call = mutated_mod.get_global_var('func_1541')
call_1591 = func_1540_call()
call_1592 = func_1540_call()
output = relay.Tuple([call_1591,])
output2 = relay.Tuple([call_1592,])
func_1619 = relay.Function([], output)
mod['func_1619'] = func_1619
mod = relay.transform.InferType()(mod)
mutated_mod['func_1619'] = func_1619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1619_call = mutated_mod.get_global_var('func_1619')
call_1620 = func_1619_call()
output = call_1620
func_1621 = relay.Function([], output)
mutated_mod['func_1621'] = func_1621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_1691 = relay.TupleGetItem(func_1214_call(), 1)
call_1692 = relay.TupleGetItem(func_1215_call(), 1)
output = call_1691
output2 = call_1692
func_1696 = relay.Function([], output)
mod['func_1696'] = func_1696
mod = relay.transform.InferType()(mod)
output = func_1696()
func_1697 = relay.Function([], output)
mutated_mod['func_1697'] = func_1697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1427_call = mod.get_global_var('func_1427')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_1721 = relay.TupleGetItem(func_1427_call(), 1)
call_1722 = relay.TupleGetItem(func_1428_call(), 1)
var_1739 = relay.var("var_1739", dtype = "int8", shape = (11, 12, 8))#candidate|1739|(11, 12, 8)|var|int8
bop_1740 = relay.bitwise_or(call_1721.astype('int32'), relay.reshape(var_1739.astype('int32'), relay.shape_of(call_1721))) # shape=(11, 12, 8)
bop_1743 = relay.bitwise_or(call_1722.astype('int32'), relay.reshape(var_1739.astype('int32'), relay.shape_of(call_1722))) # shape=(11, 12, 8)
func_1331_call = mod.get_global_var('func_1331')
func_1334_call = mutated_mod.get_global_var('func_1334')
call_1751 = relay.TupleGetItem(func_1331_call(relay.reshape(var_1739.astype('int8'), [1056,])), 0)
call_1752 = relay.TupleGetItem(func_1334_call(relay.reshape(var_1739.astype('int8'), [1056,])), 0)
output = relay.Tuple([bop_1740,call_1751,])
output2 = relay.Tuple([bop_1743,call_1752,])
func_1758 = relay.Function([var_1739,], output)
mod['func_1758'] = func_1758
mod = relay.transform.InferType()(mod)
mutated_mod['func_1758'] = func_1758
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1759 = relay.var("var_1759", dtype = "int8", shape = (11, 12, 8))#candidate|1759|(11, 12, 8)|var|int8
func_1758_call = mutated_mod.get_global_var('func_1758')
call_1760 = func_1758_call(var_1759)
output = call_1760
func_1761 = relay.Function([var_1759], output)
mutated_mod['func_1761'] = func_1761
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1765 = relay.var("var_1765", dtype = "uint16", shape = (2, 2, 16))#candidate|1765|(2, 2, 16)|var|uint16
const_1766 = relay.const([[[-6,2,-9,-2,-2,3,4,9,-4,-4,-10,-2,-4,9,-1,-10],[9,4,-10,1,5,-1,-6,5,-5,-2,-8,5,9,3,-6,9]],[[-5,-5,9,7,10,3,10,7,-6,8,7,7,-9,8,-3,5],[9,-5,8,2,-1,5,2,-7,-2,4,10,7,-2,-7,1,-5]]], dtype = "uint16")#candidate|1766|(2, 2, 16)|const|uint16
bop_1767 = relay.left_shift(var_1765.astype('uint16'), relay.reshape(const_1766.astype('uint16'), relay.shape_of(var_1765))) # shape=(2, 2, 16)
output = bop_1767
output2 = bop_1767
func_1770 = relay.Function([var_1765,], output)
mod['func_1770'] = func_1770
mod = relay.transform.InferType()(mod)
var_1771 = relay.var("var_1771", dtype = "uint16", shape = (2, 2, 16))#candidate|1771|(2, 2, 16)|var|uint16
output = func_1770(var_1771)
func_1772 = relay.Function([var_1771], output)
mutated_mod['func_1772'] = func_1772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1540_call = mod.get_global_var('func_1540')
func_1541_call = mutated_mod.get_global_var('func_1541')
call_1893 = func_1540_call()
call_1894 = func_1540_call()
output = call_1893
output2 = call_1894
func_1900 = relay.Function([], output)
mod['func_1900'] = func_1900
mod = relay.transform.InferType()(mod)
output = func_1900()
func_1901 = relay.Function([], output)
mutated_mod['func_1901'] = func_1901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1529_call = mod.get_global_var('func_1529')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_1926 = relay.TupleGetItem(func_1529_call(), 0)
call_1927 = relay.TupleGetItem(func_1530_call(), 0)
output = call_1926
output2 = call_1927
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
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_1959 = relay.TupleGetItem(func_1214_call(), 1)
call_1960 = relay.TupleGetItem(func_1215_call(), 1)
output = call_1959
output2 = call_1960
func_1968 = relay.Function([], output)
mod['func_1968'] = func_1968
mod = relay.transform.InferType()(mod)
output = func_1968()
func_1969 = relay.Function([], output)
mutated_mod['func_1969'] = func_1969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1540_call = mod.get_global_var('func_1540')
func_1541_call = mutated_mod.get_global_var('func_1541')
call_1996 = func_1540_call()
call_1997 = func_1540_call()
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
const_2011 = relay.const([[3,-9,-3,-1,-8,-2,7,-8,-8,-2,3,-9,1,6,9,-2,-2,-9,5,2,3,6,1,-10,-8,-3,4,6,1,9,-8,4,4,-6,5,4,-3,8,4,-2,-10,-3,-6,-2,-1,-9,-1,-2,6,6,8,-7,-8,-5,-3,-7,2,7,-9,7,9,-10,8,-7,-9,-4,-3,-8,-8,-7,9,-3,-2,-3,1,-10,7,-5,1,9,-7,7,-6,2,5,4,-1,-7,1,-5,-1,5,6,-2,3,5,6,9,6,-5,-1,4,-8,-9,2,-3,1,-10,-9,-4,-6,10,2,2,-1,8,8,5,5,-6,8,-10,7,-7,-4,7,-1,-10,6,-10,8,10],[10,-3,1,-1,-7,9,-3,-10,-7,-5,-6,1,6,3,-7,-2,-10,3,-4,-2,7,7,-8,-7,6,3,-8,7,4,-1,-3,-10,-10,8,-9,-5,2,8,-8,4,10,9,-4,3,-6,-10,9,-6,5,3,4,4,-9,-7,9,5,1,-9,-10,-2,1,5,-4,-9,5,-6,-9,5,3,6,-3,3,-5,-8,9,9,-4,9,7,10,1,9,4,-9,3,-1,8,-10,-10,-8,-8,10,3,-1,-7,-10,-5,-10,2,10,-7,-4,6,-8,4,-7,4,6,7,8,6,-4,-9,-4,4,-10,4,5,-10,10,8,-8,-5,10,2,5,9,3,-6,1,-10,10],[-7,-7,8,2,-5,8,5,-1,7,-6,-7,-4,-5,-2,8,-2,7,-3,-7,10,-7,1,6,10,-7,-8,7,-7,7,-9,1,1,1,2,-10,9,9,-1,1,6,10,-4,6,-9,-1,9,2,-8,3,-2,-2,-2,2,-8,7,-4,-10,3,-10,-10,-3,-10,6,-7,-10,3,1,-5,-1,9,-6,2,-1,-3,-7,1,9,-4,-1,-5,-3,3,6,-8,-8,4,10,-2,-10,4,-8,-9,8,4,-6,10,-7,-3,10,1,-10,4,10,-3,-2,10,-5,9,-2,-5,-9,-8,-10,3,-4,-10,9,4,-1,-2,5,-5,10,-4,-6,-3,-5,-3,-3,7,-1,2],[2,-9,-3,7,2,-6,9,-7,10,10,-4,-2,-9,4,5,-10,-2,-1,-10,10,-4,4,-10,-6,2,6,1,3,-7,2,5,-1,10,1,-10,-2,1,8,9,-2,10,-7,7,2,10,-8,-3,3,2,-5,-9,7,-5,1,-8,4,-10,10,-4,-3,-4,1,-1,5,10,-6,-7,9,9,-3,-3,-7,-10,10,1,8,4,5,4,9,-9,3,7,7,3,4,-9,-7,-10,-2,-2,-6,-10,2,-2,9,5,7,-5,-7,-4,-2,-2,3,8,2,-8,6,1,3,8,-3,4,-4,-6,-7,2,5,-10,5,-6,8,5,-5,4,8,-9,-7,-2,-4,-2,9],[10,-7,4,8,8,5,2,8,7,-9,8,1,-9,-8,-6,4,-5,-8,-4,9,6,3,-4,-5,-6,7,-2,-6,3,-1,-3,9,-7,-6,-5,1,9,-9,-7,-3,-1,-9,-1,4,-8,-5,2,-8,-10,10,-9,7,6,-2,2,-6,-10,-8,7,-4,-6,6,2,-7,-10,8,-9,-9,2,-10,1,-9,-10,-9,-8,-3,-2,2,-7,-6,7,8,8,-3,-1,7,8,2,-3,-6,-3,-5,10,-1,-8,3,1,-3,9,9,10,1,-2,-5,-3,5,-10,3,8,8,-10,-1,-2,-8,-2,-10,-5,-10,3,3,6,2,-6,7,-8,8,-6,7,-5,7,-3,2],[8,-6,-7,5,-7,-9,-1,-7,-3,-6,-5,-7,9,-2,2,4,-3,-9,1,4,-2,-1,1,-5,-2,-3,6,-9,-5,1,2,5,6,-6,1,-5,2,7,1,-10,-5,-1,-3,7,-1,5,-2,3,-6,4,-8,10,4,-5,-1,7,-8,-6,1,10,10,7,6,1,-8,1,4,8,-1,3,10,10,10,-10,9,-5,7,-10,-2,7,6,8,1,9,10,6,4,7,-1,-7,9,9,3,-9,10,7,-5,-5,-2,8,8,4,-9,-8,-2,-3,8,-6,-1,10,-4,7,-3,-4,7,-10,8,-7,-7,-9,3,-9,-4,-3,-4,4,9,5,-4,-8,-5,-7],[2,-9,-10,-9,2,3,-5,-9,-9,-6,4,10,-2,-2,7,-9,-3,10,-7,-6,9,5,6,-2,6,-3,1,2,-2,-10,2,-7,-8,-10,-6,-5,8,10,1,10,9,-2,7,-4,6,7,5,-5,-3,-9,-3,-5,-2,6,-6,-5,-2,-5,-10,-7,7,6,-9,5,10,-10,-10,-6,7,-8,-10,10,-9,-10,-6,-5,2,4,-4,3,5,-7,-8,7,-6,-10,9,8,-5,-7,7,5,-5,1,10,-5,7,9,-4,-3,-5,-7,-3,4,-5,-8,-5,10,-1,-3,-4,5,-10,-1,5,5,8,-4,-8,8,1,6,8,8,-6,2,7,5,4,-2,-9,8],[-2,8,-3,5,-2,-10,4,2,8,4,-3,-3,-5,5,5,-1,8,-6,4,4,2,-8,1,8,6,-5,1,6,-6,-9,-6,7,-2,6,-6,-3,4,5,-3,-5,5,8,7,-3,6,-3,4,8,-2,-3,-5,-7,8,-4,-4,-2,8,-8,-3,-7,5,-3,1,7,4,-2,-4,9,10,5,-2,-7,-6,-5,-6,-9,-4,9,2,9,-6,8,-1,-4,-10,-8,-5,-1,10,1,8,-6,-2,8,-3,-3,-7,10,8,10,6,-8,-1,-3,7,-8,6,9,-10,-4,-3,3,8,9,-1,3,7,10,2,-10,9,-4,-1,-3,-10,-6,-5,-7,6,10,7,9]], dtype = "int8")#candidate|2011|(8, 132)|const|int8
call_2010 = relay.TupleGetItem(func_322_call(relay.reshape(const_2011.astype('int8'), [11, 12, 8])), 0)
call_2012 = relay.TupleGetItem(func_325_call(relay.reshape(const_2011.astype('int8'), [11, 12, 8])), 0)
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_2022 = func_1176_call()
call_2023 = func_1176_call()
bop_2037 = relay.divide(call_2022.astype('float64'), const_2011.astype('float64')) # shape=(5, 8, 132)
bop_2040 = relay.divide(call_2023.astype('float64'), const_2011.astype('float64')) # shape=(5, 8, 132)
bop_2045 = relay.logical_or(call_2022.astype('bool'), const_2011.astype('bool')) # shape=(5, 8, 132)
bop_2048 = relay.logical_or(call_2023.astype('bool'), const_2011.astype('bool')) # shape=(5, 8, 132)
func_1758_call = mod.get_global_var('func_1758')
func_1761_call = mutated_mod.get_global_var('func_1761')
call_2054 = relay.TupleGetItem(func_1758_call(relay.reshape(const_2011.astype('int8'), [11, 12, 8])), 1)
call_2055 = relay.TupleGetItem(func_1761_call(relay.reshape(const_2011.astype('int8'), [11, 12, 8])), 1)
func_1770_call = mod.get_global_var('func_1770')
func_1772_call = mutated_mod.get_global_var('func_1772')
const_2063 = relay.const([-1,2,-9,5,7,-7,-5,10,-9,-8,5,5,-10,-2,-4,-8,9,4,-4,5,9,2,3,9,-10,-6,4,7,-10,8,3,6,-8,1,-1,5,-8,-1,10,2,-7,-7,10,7,-10,-1,-1,-6,-9,-2,3,10,4,-6,-1,6,-7,-1,4,6,-2,-8,5,-1], dtype = "uint16")#candidate|2063|(64,)|const|uint16
call_2062 = func_1770_call(relay.reshape(const_2063.astype('uint16'), [2, 2, 16]))
call_2064 = func_1770_call(relay.reshape(const_2063.astype('uint16'), [2, 2, 16]))
func_1619_call = mod.get_global_var('func_1619')
func_1621_call = mutated_mod.get_global_var('func_1621')
call_2068 = relay.TupleGetItem(func_1619_call(), 0)
call_2069 = relay.TupleGetItem(func_1621_call(), 0)
output = relay.Tuple([call_1996,call_2010,bop_2037,bop_2045,call_2054,call_2062,const_2063,call_2068,])
output2 = relay.Tuple([call_1997,call_2012,bop_2040,bop_2048,call_2055,call_2064,const_2063,call_2069,])
func_2096 = relay.Function([], output)
mod['func_2096'] = func_2096
mod = relay.transform.InferType()(mod)
mutated_mod['func_2096'] = func_2096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mutated_mod.get_global_var('func_2096')
call_2097 = func_2096_call()
output = call_2097
func_2098 = relay.Function([], output)
mutated_mod['func_2098'] = func_2098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_2114 = relay.TupleGetItem(func_1214_call(), 0)
call_2115 = relay.TupleGetItem(func_1215_call(), 0)
func_1968_call = mod.get_global_var('func_1968')
func_1969_call = mutated_mod.get_global_var('func_1969')
call_2119 = func_1968_call()
call_2120 = func_1968_call()
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_2135 = func_1931_call()
call_2136 = func_1931_call()
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_2139 = relay.TupleGetItem(func_1214_call(), 1)
call_2140 = relay.TupleGetItem(func_1215_call(), 1)
func_1758_call = mod.get_global_var('func_1758')
func_1761_call = mutated_mod.get_global_var('func_1761')
const_2152 = relay.const([2,3,7,-7,2,-10,-8,-8,4,6,6,3,3,-3,-1,10,-6,-3,-2,7,-8,3,-5,-8,9,-9,1,2,3,4,-6,9,-9,8,-5,-7,3,10,3,9,9,10,-9,6,8,7,-6,7,-1,7,9,8,4,-9,3,2,5,3,-2,7,-1,-3,3,2,-4,-9,-3,-4,2,-5,-1,-6,-8,-2,8,-2,4,-5,7,10,-6,-6,-3,-7,4,-9,-10,-3,5,-1,-3,-1,-10,3,-4,3,-9,1,1,-8,-2,2,-3,2,-8,-1,8,9,8,9,4,-4,-1,6,4,7,-2,-10,3,3,7,-4,7,4,5,9,-5,4,-9,10,-6,-3,-5,5,7,9,3,-10,5,6,-7,-1,8,-8,8,2,4,-4,8,-7,5,-10,9,9,-4,-6,-7,-3,2,2,1,6,1,6,-7,-6,-9,3,6,4,6,-1,8,-8,7,-4,7,-4,8,-8,3,9,8,-1,-3,-4,-8,-2,1,1,-3,4,3,-8,8,-5,-8,4,-6,2,-2,8,3,6,-1,2,2,-4,6,5,8,4,6,-3,2,4,4,-4,2,-3,-9,-9,-10,5,6,9,-3,1,-2,-2,2,8,7,-4,-2,-4,-1,9,7,-9,-7,9,3,7,-4,2,4,1,10,2,2,2,-10,-7,8,-10,-4,2,6,-5,-8,-6,4,6,3,-7,-4,10,-1,-1,-1,-1,9,-4,-3,-7,3,7,-1,3,-3,-8,-9,-10,-5,9,-3,3,-6,-9,4,-3,-1,6,5,5,10,-4,-2,-9,-7,-3,3,-2,-2,9,1,5,-4,4,-8,5,2,7,6,-9,8,-3,7,-1,10,-7,2,3,-2,-5,-5,8,-2,9,5,-10,1,4,-1,-9,5,-4,-5,-4,3,7,2,3,-4,-9,-2,2,4,-3,2,-10,7,5,8,-9,1,-6,5,6,-4,8,5,1,-7,8,6,6,9,-5,3,9,4,-8,7,-10,-10,-8,8,6,-6,5,-2,7,-2,-10,10,2,5,5,-3,-4,3,10,3,-9,10,-3,4,-4,4,-3,3,8,-5,-9,-8,-3,-5,4,-9,-9,6,-1,-5,7,9,2,5,-10,-3,-9,2,-1,3,6,-8,-10,10,7,6,-3,-3,-7,-6,-9,5,-1,-9,3,10,5,4,-6,-7,-8,-6,8,-7,-10,-3,6,-6,-3,1,-7,5,1,-7,4,8,5,-6,-5,-9,7,-1,-9,10,-2,-8,-2,-2,4,9,-1,1,-3,2,-9,-3,2,9,-3,-3,-2,7,-6,6,-8,8,-6,-7,6,-8,-10,-1,-7,2,-1,-8,-8,8,3,1,-1,-1,8,5,-7,8,4,-10,2,-2,8,10,4,-9,-10,-6,-1,-9,5,4,-6,1,-4,2,2,-2,5,-8,8,6,10,-10,-9,2,2,7,-8,8,9,7,6,-4,9,-8,9,-4,5,2,4,9,-7,4,5,7,-3,-5,-4,-8,1,2,1,1,-4,10,-6,-2,5,8,9,4,-2,1,-8,-2,6,-10,-2,2,3,-1,-3,2,10,-10,7,-9,2,6,-8,10,-4,10,1,-1,-4,-5,-7,6,9,4,-1,9,-4,5,5,7,-6,-3,-9,-1,-9,3,-5,3,5,2,-2,-9,-7,-2,2,10,-6,-2,1,1,2,-4,-1,1,-4,-1,-5,7,-9,-2,6,-6,9,9,-5,-10,2,-4,-10,-10,7,3,6,-3,8,-5,-1,9,10,10,8,-2,3,-3,10,-9,7,-8,3,5,7,8,-10,8,4,-7,9,1,5,8,9,2,-1,-8,-2,-8,2,8,2,6,-5,6,-2,9,3,1,-5,10,3,-2,1,-5,7,-9,-1,-3,-7,2,8,-5,7,6,10,9,4,-10,3,-9,1,9,4,8,-3,-9,10,-5,-1,-8,-7,-4,-8,7,2,-2,-8,4,-5,1,1,-10,-5,7,-7,5,-1,6,-5,-3,-1,-9,7,10,4,-9,-3,-5,7,-2,-8,-8,-8,-2,-9,2,-9,-10,-4,8,2,-4,-8,1,4,10,2,3,-4,7,-10,-5,9,5,8,3,1,-4,10,-6,1,-6,-6,7,4,5,-2,-2,8,6,9,5,-1,-8,-8,-3,2,4,-10,10,-4,9,7,-8,-9,2,-8,-9,-8,9,-3,5,-4,3,-1,-10,-8,-2,10,-2,6,10,-3,-2,8,-8,-6,6,3,5,-2,2,2,7,-6,3,-2,-8,2,7,3,-10,-8,10,8,7,8,2,-3,-2,-7,-1,-7,-4,-10,8,-4,-4,-7,-4,-8,8,10,8,8,-10,-6,-4,1,2,8,-5,-10,-7,-3,-3,3,1,-1,5,-10,4,8,-8,5,2,-2,10,-8,-1,9,6,-7,-5,5,-8,7,-10,10,-5,8,10,6,3,6,-7,-8,-9,9,3,-4,-8,7,-7,5,-3,1,4,5,1,1,-8,-10,-6,-1,-2,4,-5,7,-7,7,-5,5,-6,-9,4,5,-1,-1,6,7,-6,-10,-9,6,-9,-8,-1,-8,-5,-4,-6,-3,5,-3,-7,-9,-9,-7,-7,-6,5,-3,-9,3,-7,-1,7,-10,-9,3,3,-8,-2,3,-7,8,-5,8,3,5,8,2,3,8,-7,7,-7,-4,-1,10,10,-10,8,-8,-9,10,-3,3,-6,-8,-5,5,-2,-3,-8,3,-1,-2,2,10,4,-9,4,-5,-4,-5,9,-1,1,-6,-8,-8,3,-8,1,-6,-9,4,-6,4,-1,9,1,1,-7,-2,5,2,1,10,-9,6,1,9,-8,-9], dtype = "int8")#candidate|2152|(1056,)|const|int8
call_2151 = relay.TupleGetItem(func_1758_call(relay.reshape(const_2152.astype('int8'), [11, 12, 8])), 0)
call_2153 = relay.TupleGetItem(func_1761_call(relay.reshape(const_2152.astype('int8'), [11, 12, 8])), 0)
output = relay.Tuple([call_2114,call_2119,call_2135,call_2139,call_2151,const_2152,])
output2 = relay.Tuple([call_2115,call_2120,call_2136,call_2140,call_2153,const_2152,])
func_2190 = relay.Function([], output)
mod['func_2190'] = func_2190
mod = relay.transform.InferType()(mod)
output = func_2190()
func_2191 = relay.Function([], output)
mutated_mod['func_2191'] = func_2191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_2280 = relay.TupleGetItem(func_2096_call(), 2)
call_2281 = relay.TupleGetItem(func_2098_call(), 2)
output = relay.Tuple([call_2280,])
output2 = relay.Tuple([call_2281,])
func_2294 = relay.Function([], output)
mod['func_2294'] = func_2294
mod = relay.transform.InferType()(mod)
mutated_mod['func_2294'] = func_2294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mutated_mod.get_global_var('func_2294')
call_2295 = func_2294_call()
output = call_2295
func_2296 = relay.Function([], output)
mutated_mod['func_2296'] = func_2296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1968_call = mod.get_global_var('func_1968')
func_1969_call = mutated_mod.get_global_var('func_1969')
call_2331 = func_1968_call()
call_2332 = func_1968_call()
var_2335 = relay.var("var_2335", dtype = "float64", shape = (5, 8, 4))#candidate|2335|(5, 8, 4)|var|float64
bop_2336 = relay.right_shift(call_2331.astype('uint64'), var_2335.astype('uint64')) # shape=(5, 8, 4)
bop_2339 = relay.right_shift(call_2332.astype('uint64'), var_2335.astype('uint64')) # shape=(5, 8, 4)
output = relay.Tuple([bop_2336,])
output2 = relay.Tuple([bop_2339,])
func_2357 = relay.Function([var_2335,], output)
mod['func_2357'] = func_2357
mod = relay.transform.InferType()(mod)
mutated_mod['func_2357'] = func_2357
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2358 = relay.var("var_2358", dtype = "float64", shape = (5, 8, 4))#candidate|2358|(5, 8, 4)|var|float64
func_2357_call = mutated_mod.get_global_var('func_2357')
call_2359 = func_2357_call(var_2358)
output = call_2359
func_2360 = relay.Function([var_2358], output)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2440 = relay.var("var_2440", dtype = "float32", shape = (15, 3, 1))#candidate|2440|(15, 3, 1)|var|float32
uop_2441 = relay.tan(var_2440.astype('float32')) # shape=(15, 3, 1)
output = uop_2441
output2 = uop_2441
func_2453 = relay.Function([var_2440,], output)
mod['func_2453'] = func_2453
mod = relay.transform.InferType()(mod)
var_2454 = relay.var("var_2454", dtype = "float32", shape = (15, 3, 1))#candidate|2454|(15, 3, 1)|var|float32
output = func_2453(var_2454)
func_2455 = relay.Function([var_2454], output)
mutated_mod['func_2455'] = func_2455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1900_call = mod.get_global_var('func_1900')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_2486 = func_1900_call()
call_2487 = func_1900_call()
func_2357_call = mod.get_global_var('func_2357')
func_2360_call = mutated_mod.get_global_var('func_2360')
var_2491 = relay.var("var_2491", dtype = "float64", shape = (80, 2))#candidate|2491|(80, 2)|var|float64
call_2490 = relay.TupleGetItem(func_2357_call(relay.reshape(var_2491.astype('float64'), [5, 8, 4])), 0)
call_2492 = relay.TupleGetItem(func_2360_call(relay.reshape(var_2491.astype('float64'), [5, 8, 4])), 0)
func_1968_call = mod.get_global_var('func_1968')
func_1969_call = mutated_mod.get_global_var('func_1969')
call_2510 = func_1968_call()
call_2511 = func_1968_call()
uop_2548 = relay.sin(var_2491.astype('float32')) # shape=(80, 2)
output = relay.Tuple([call_2486,call_2490,call_2510,uop_2548,])
output2 = relay.Tuple([call_2487,call_2492,call_2511,uop_2548,])
func_2564 = relay.Function([var_2491,], output)
mod['func_2564'] = func_2564
mod = relay.transform.InferType()(mod)
mutated_mod['func_2564'] = func_2564
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2565 = relay.var("var_2565", dtype = "float64", shape = (80, 2))#candidate|2565|(80, 2)|var|float64
func_2564_call = mutated_mod.get_global_var('func_2564')
call_2566 = func_2564_call(var_2565)
output = call_2566
func_2567 = relay.Function([var_2565], output)
mutated_mod['func_2567'] = func_2567
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2584 = relay.const(7, dtype = "int8")#candidate|2584|()|const|int8
var_2585 = relay.var("var_2585", dtype = "int8", shape = (11, 14, 15))#candidate|2585|(11, 14, 15)|var|int8
bop_2586 = relay.subtract(const_2584.astype('int8'), var_2585.astype('int8')) # shape=(11, 14, 15)
output = bop_2586
output2 = bop_2586
func_2594 = relay.Function([var_2585,], output)
mod['func_2594'] = func_2594
mod = relay.transform.InferType()(mod)
mutated_mod['func_2594'] = func_2594
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2595 = relay.var("var_2595", dtype = "int8", shape = (11, 14, 15))#candidate|2595|(11, 14, 15)|var|int8
func_2594_call = mutated_mod.get_global_var('func_2594')
call_2596 = func_2594_call(var_2595)
output = call_2596
func_2597 = relay.Function([var_2595], output)
mutated_mod['func_2597'] = func_2597
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2599 = relay.var("var_2599", dtype = "float32", shape = (13, 5, 8))#candidate|2599|(13, 5, 8)|var|float32
uop_2600 = relay.log2(var_2599.astype('float32')) # shape=(13, 5, 8)
output = uop_2600
output2 = uop_2600
func_2607 = relay.Function([var_2599,], output)
mod['func_2607'] = func_2607
mod = relay.transform.InferType()(mod)
mutated_mod['func_2607'] = func_2607
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2608 = relay.var("var_2608", dtype = "float32", shape = (13, 5, 8))#candidate|2608|(13, 5, 8)|var|float32
func_2607_call = mutated_mod.get_global_var('func_2607')
call_2609 = func_2607_call(var_2608)
output = call_2609
func_2610 = relay.Function([var_2608], output)
mutated_mod['func_2610'] = func_2610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1900_call = mod.get_global_var('func_1900')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_2623 = func_1900_call()
call_2624 = func_1900_call()
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
var_2636 = relay.var("var_2636", dtype = "int8", shape = (1056,))#candidate|2636|(1056,)|var|int8
call_2635 = relay.TupleGetItem(func_322_call(relay.reshape(var_2636.astype('int8'), [11, 12, 8])), 0)
call_2637 = relay.TupleGetItem(func_325_call(relay.reshape(var_2636.astype('int8'), [11, 12, 8])), 0)
func_1540_call = mod.get_global_var('func_1540')
func_1541_call = mutated_mod.get_global_var('func_1541')
call_2638 = func_1540_call()
call_2639 = func_1540_call()
func_1619_call = mod.get_global_var('func_1619')
func_1621_call = mutated_mod.get_global_var('func_1621')
call_2648 = relay.TupleGetItem(func_1619_call(), 0)
call_2649 = relay.TupleGetItem(func_1621_call(), 0)
func_481_call = mod.get_global_var('func_481')
func_486_call = mutated_mod.get_global_var('func_486')
var_2672 = relay.var("var_2672", dtype = "float64", shape = (660,))#candidate|2672|(660,)|var|float64
call_2671 = relay.TupleGetItem(func_481_call(relay.reshape(var_2672.astype('float64'), [10, 6, 11]), relay.reshape(var_2672.astype('float64'), [10, 6, 11]), relay.reshape(call_2635.astype('int8'), [1056,]), ), 0)
call_2673 = relay.TupleGetItem(func_486_call(relay.reshape(var_2672.astype('float64'), [10, 6, 11]), relay.reshape(var_2672.astype('float64'), [10, 6, 11]), relay.reshape(call_2635.astype('int8'), [1056,]), ), 0)
func_2564_call = mod.get_global_var('func_2564')
func_2567_call = mutated_mod.get_global_var('func_2567')
var_2678 = relay.var("var_2678", dtype = "float64", shape = (160,))#candidate|2678|(160,)|var|float64
call_2677 = relay.TupleGetItem(func_2564_call(relay.reshape(var_2678.astype('float64'), [80, 2])), 3)
call_2679 = relay.TupleGetItem(func_2567_call(relay.reshape(var_2678.astype('float64'), [80, 2])), 3)
output = relay.Tuple([call_2623,call_2635,var_2636,call_2638,call_2648,call_2671,var_2672,call_2677,var_2678,])
output2 = relay.Tuple([call_2624,call_2637,var_2636,call_2639,call_2649,call_2673,var_2672,call_2679,var_2678,])
func_2685 = relay.Function([var_2636,var_2672,var_2678,], output)
mod['func_2685'] = func_2685
mod = relay.transform.InferType()(mod)
var_2686 = relay.var("var_2686", dtype = "int8", shape = (1056,))#candidate|2686|(1056,)|var|int8
var_2687 = relay.var("var_2687", dtype = "float64", shape = (660,))#candidate|2687|(660,)|var|float64
var_2688 = relay.var("var_2688", dtype = "float64", shape = (160,))#candidate|2688|(160,)|var|float64
output = func_2685(var_2686,var_2687,var_2688,)
func_2689 = relay.Function([var_2686,var_2687,var_2688,], output)
mutated_mod['func_2689'] = func_2689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_2722 = relay.TupleGetItem(func_2096_call(), 6)
call_2723 = relay.TupleGetItem(func_2098_call(), 6)
output = call_2722
output2 = call_2723
func_2728 = relay.Function([], output)
mod['func_2728'] = func_2728
mod = relay.transform.InferType()(mod)
mutated_mod['func_2728'] = func_2728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2728_call = mutated_mod.get_global_var('func_2728')
call_2729 = func_2728_call()
output = call_2729
func_2730 = relay.Function([], output)
mutated_mod['func_2730'] = func_2730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2728_call = mod.get_global_var('func_2728')
func_2730_call = mutated_mod.get_global_var('func_2730')
call_2746 = func_2728_call()
call_2747 = func_2728_call()
output = call_2746
output2 = call_2747
func_2781 = relay.Function([], output)
mod['func_2781'] = func_2781
mod = relay.transform.InferType()(mod)
output = func_2781()
func_2782 = relay.Function([], output)
mutated_mod['func_2782'] = func_2782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1696_call = mod.get_global_var('func_1696')
func_1697_call = mutated_mod.get_global_var('func_1697')
call_2823 = func_1696_call()
call_2824 = func_1696_call()
const_2835 = relay.const([[[-2.447809],[-5.527384],[-2.555452],[-7.270314],[6.619626],[-1.491292],[-6.395574],[9.133495]],[[6.376698],[8.139662],[0.970416],[3.598622],[-2.870393],[-0.056242],[-0.009568],[-4.664275]],[[4.181854],[4.905460],[-8.712386],[-7.028173],[-6.084920],[-2.309753],[4.009779],[-2.772631]],[[2.576294],[9.907755],[7.605882],[7.865168],[-7.068812],[-5.509446],[9.644354],[6.117659]],[[2.697754],[6.266995],[-8.077911],[9.303339],[-0.214333],[-4.395897],[6.430309],[-3.650418]]], dtype = "float64")#candidate|2835|(5, 8, 1)|const|float64
bop_2836 = relay.bitwise_and(call_2823.astype('uint64'), relay.reshape(const_2835.astype('uint64'), relay.shape_of(call_2823))) # shape=(5, 8, 1)
bop_2839 = relay.bitwise_and(call_2824.astype('uint64'), relay.reshape(const_2835.astype('uint64'), relay.shape_of(call_2824))) # shape=(5, 8, 1)
output = relay.Tuple([bop_2836,])
output2 = relay.Tuple([bop_2839,])
func_2847 = relay.Function([], output)
mod['func_2847'] = func_2847
mod = relay.transform.InferType()(mod)
output = func_2847()
func_2848 = relay.Function([], output)
mutated_mod['func_2848'] = func_2848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_2910 = func_1176_call()
call_2911 = func_1176_call()
output = call_2910
output2 = call_2911
func_2927 = relay.Function([], output)
mod['func_2927'] = func_2927
mod = relay.transform.InferType()(mod)
mutated_mod['func_2927'] = func_2927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2927_call = mutated_mod.get_global_var('func_2927')
call_2928 = func_2927_call()
output = call_2928
func_2929 = relay.Function([], output)
mutated_mod['func_2929'] = func_2929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_2938 = relay.TupleGetItem(func_1214_call(), 0)
call_2939 = relay.TupleGetItem(func_1215_call(), 0)
func_1770_call = mod.get_global_var('func_1770')
func_1772_call = mutated_mod.get_global_var('func_1772')
var_2968 = relay.var("var_2968", dtype = "uint16", shape = (2, 32))#candidate|2968|(2, 32)|var|uint16
call_2967 = func_1770_call(relay.reshape(var_2968.astype('uint16'), [2, 2, 16]))
call_2969 = func_1770_call(relay.reshape(var_2968.astype('uint16'), [2, 2, 16]))
output = relay.Tuple([call_2938,call_2967,var_2968,])
output2 = relay.Tuple([call_2939,call_2969,var_2968,])
func_2977 = relay.Function([var_2968,], output)
mod['func_2977'] = func_2977
mod = relay.transform.InferType()(mod)
mutated_mod['func_2977'] = func_2977
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2978 = relay.var("var_2978", dtype = "uint16", shape = (2, 32))#candidate|2978|(2, 32)|var|uint16
func_2977_call = mutated_mod.get_global_var('func_2977')
call_2979 = func_2977_call(var_2978)
output = call_2979
func_2980 = relay.Function([var_2978], output)
mutated_mod['func_2980'] = func_2980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1529_call = mod.get_global_var('func_1529')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_2982 = relay.TupleGetItem(func_1529_call(), 0)
call_2983 = relay.TupleGetItem(func_1530_call(), 0)
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_3006 = func_1176_call()
call_3007 = func_1176_call()
uop_3014 = relay.erf(call_2982.astype('float64')) # shape=(5, 8, 1)
uop_3016 = relay.erf(call_2983.astype('float64')) # shape=(5, 8, 1)
func_2357_call = mod.get_global_var('func_2357')
func_2360_call = mutated_mod.get_global_var('func_2360')
var_3018 = relay.var("var_3018", dtype = "float64", shape = (160,))#candidate|3018|(160,)|var|float64
call_3017 = relay.TupleGetItem(func_2357_call(relay.reshape(var_3018.astype('float64'), [5, 8, 4])), 0)
call_3019 = relay.TupleGetItem(func_2360_call(relay.reshape(var_3018.astype('float64'), [5, 8, 4])), 0)
uop_3025 = relay.exp(uop_3014.astype('float64')) # shape=(5, 8, 1)
uop_3027 = relay.exp(uop_3016.astype('float64')) # shape=(5, 8, 1)
output = relay.Tuple([call_3006,call_3017,var_3018,uop_3025,])
output2 = relay.Tuple([call_3007,call_3019,var_3018,uop_3027,])
func_3033 = relay.Function([var_3018,], output)
mod['func_3033'] = func_3033
mod = relay.transform.InferType()(mod)
mutated_mod['func_3033'] = func_3033
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3034 = relay.var("var_3034", dtype = "float64", shape = (160,))#candidate|3034|(160,)|var|float64
func_3033_call = mutated_mod.get_global_var('func_3033')
call_3035 = func_3033_call(var_3034)
output = call_3035
func_3036 = relay.Function([var_3034], output)
mutated_mod['func_3036'] = func_3036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_3040 = relay.TupleGetItem(func_2096_call(), 1)
call_3041 = relay.TupleGetItem(func_2098_call(), 1)
output = call_3040
output2 = call_3041
func_3042 = relay.Function([], output)
mod['func_3042'] = func_3042
mod = relay.transform.InferType()(mod)
output = func_3042()
func_3043 = relay.Function([], output)
mutated_mod['func_3043'] = func_3043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_3046 = relay.TupleGetItem(func_2096_call(), 0)
call_3047 = relay.TupleGetItem(func_2098_call(), 0)
func_2357_call = mod.get_global_var('func_2357')
func_2360_call = mutated_mod.get_global_var('func_2360')
const_3057 = relay.const([-4.401595,-7.986153,-9.167963,-0.815268,5.761147,-2.809527,-1.606481,-4.764814,9.943409,4.150467,4.619873,-7.321782,-9.378083,7.664443,-1.850731,3.696594,6.375912,-5.554951,8.149169,-3.321261,-8.924089,-3.448562,-6.455770,-2.517524,9.078140,7.182351,-5.553247,-0.829291,8.582079,-2.487398,-0.389341,-3.182587,5.162371,8.347740,4.551479,0.053046,-5.894645,-9.202652,-1.468410,-7.907572,-0.437204,7.226040,-5.845435,-1.649387,5.384619,5.194482,-5.945064,0.938986,-5.918531,7.433822,5.349825,8.059680,-7.928084,-3.118175,8.764912,-5.348213,-7.596530,-6.222926,8.728687,-1.213107,8.339829,9.656879,2.640227,4.825728,0.575589,5.852595,-0.997173,4.062053,-3.634944,7.436214,-7.954647,-5.905014,3.148155,3.579108,9.828332,0.811772,7.565341,-9.031202,-7.400236,-7.968543,-1.091244,-5.529263,7.152598,1.859062,5.062449,5.871974,-5.397951,-5.819643,-3.053640,8.099447,-9.021827,-1.079439,7.511493,-7.276644,-7.716811,2.750886,6.207282,3.347685,4.171988,-0.317368,-9.987312,1.647715,2.867665,-7.676048,2.014879,2.829471,7.362007,-9.484387,1.383998,-7.782170,7.395158,-4.157278,2.275484,2.149859,7.144870,5.312267,6.480321,-8.622628,-4.830912,-1.523820,-2.114357,7.588677,9.846176,-1.816822,7.500490,2.995743,2.614937,6.081045,3.462017,4.331015,-6.376555,-1.208293,1.396458,2.985296,-6.159998,-3.253874,5.734311,-3.951566,2.428391,8.765968,8.799623,1.860048,0.808331,7.947919,-0.982971,6.750713,4.114384,-0.558353,-9.653145,-9.971282,-4.510375,-0.127885,9.676638,-3.379980,0.794928,2.400715,-1.210691,4.988494,1.837772,2.846498], dtype = "float64")#candidate|3057|(160,)|const|float64
call_3056 = relay.TupleGetItem(func_2357_call(relay.reshape(const_3057.astype('float64'), [5, 8, 4])), 0)
call_3058 = relay.TupleGetItem(func_2360_call(relay.reshape(const_3057.astype('float64'), [5, 8, 4])), 0)
output = relay.Tuple([call_3046,call_3056,const_3057,])
output2 = relay.Tuple([call_3047,call_3058,const_3057,])
func_3062 = relay.Function([], output)
mod['func_3062'] = func_3062
mod = relay.transform.InferType()(mod)
output = func_3062()
func_3063 = relay.Function([], output)
mutated_mod['func_3063'] = func_3063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1696_call = mod.get_global_var('func_1696')
func_1697_call = mutated_mod.get_global_var('func_1697')
call_3119 = func_1696_call()
call_3120 = func_1696_call()
output = relay.Tuple([call_3119,])
output2 = relay.Tuple([call_3120,])
func_3183 = relay.Function([], output)
mod['func_3183'] = func_3183
mod = relay.transform.InferType()(mod)
output = func_3183()
func_3184 = relay.Function([], output)
mutated_mod['func_3184'] = func_3184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_3260 = relay.TupleGetItem(func_3183_call(), 0)
call_3261 = relay.TupleGetItem(func_3184_call(), 0)
uop_3262 = relay.sinh(call_3260.astype('float64')) # shape=(5, 8, 1)
uop_3264 = relay.sinh(call_3261.astype('float64')) # shape=(5, 8, 1)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_3271 = func_2781_call()
call_3272 = func_2781_call()
func_1696_call = mod.get_global_var('func_1696')
func_1697_call = mutated_mod.get_global_var('func_1697')
call_3288 = func_1696_call()
call_3289 = func_1696_call()
func_1529_call = mod.get_global_var('func_1529')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_3294 = relay.TupleGetItem(func_1529_call(), 0)
call_3295 = relay.TupleGetItem(func_1530_call(), 0)
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_3304 = relay.TupleGetItem(func_1214_call(), 1)
call_3305 = relay.TupleGetItem(func_1215_call(), 1)
output = relay.Tuple([uop_3262,call_3271,call_3288,call_3294,call_3304,])
output2 = relay.Tuple([uop_3264,call_3272,call_3289,call_3295,call_3305,])
func_3311 = relay.Function([], output)
mod['func_3311'] = func_3311
mod = relay.transform.InferType()(mod)
output = func_3311()
func_3312 = relay.Function([], output)
mutated_mod['func_3312'] = func_3312
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3333 = relay.var("var_3333", dtype = "float32", shape = (6, 13, 13))#candidate|3333|(6, 13, 13)|var|float32
const_3334 = relay.const([[[-0.441604,-5.325430,-2.729715,-1.229285,-1.742793,0.125229,-2.651458,-5.923022,-4.821110,7.230064,5.543678,-1.239285,-9.879888],[-1.878327,-6.045225,-8.175470,-8.023087,3.025987,0.281047,-6.670324,-1.884010,-1.376555,5.852663,9.146625,-7.957898,-8.217962],[-4.580410,-7.102717,8.593221,1.837575,9.227852,-4.828137,4.576173,-6.420052,-7.319194,-7.218700,-5.019614,6.410951,5.430399],[8.399329,6.276199,3.869221,-2.120897,-2.873504,-1.813466,-3.413826,5.225429,4.443398,-7.808272,5.304283,4.807820,1.722439],[7.471407,6.624827,2.995746,-5.829766,7.302930,5.814961,9.674794,6.724394,8.519726,1.248226,-3.713053,9.529987,-0.138745],[6.175806,-6.291937,8.820629,-7.987591,-5.684531,-0.899380,-0.493584,-4.992754,7.258997,-9.819082,-4.812118,-8.225716,-7.783717],[-3.121488,4.589887,0.663881,-3.933254,7.258003,8.550719,1.195002,-7.557067,-0.994227,8.662629,-9.824154,-4.330895,0.555004],[-5.252722,1.534834,-5.333902,1.000394,-1.950011,4.170356,-5.524348,4.082186,-1.342165,-4.862547,-3.310245,4.931697,9.582937],[-4.311960,-8.049474,-1.774411,-9.207134,-2.556876,-5.281833,-8.191127,-7.344437,1.709381,9.178780,-8.927941,3.284286,-4.989211],[2.909797,8.144655,3.194257,-5.348938,0.561956,-3.268990,-4.691107,8.452475,-7.791768,-9.661656,0.242997,-9.481785,-1.055962],[-3.376688,2.118990,9.389705,-0.974334,6.138890,-0.908537,-6.567886,2.341892,5.271009,8.924940,-0.177351,3.347626,-0.662378],[-2.490889,7.106331,1.341951,0.810317,-9.826770,1.368994,6.303140,-2.227937,-0.080908,-1.823374,7.074664,-1.373196,-0.374533],[0.071626,4.536704,-8.796491,-7.016711,-2.979038,4.039798,-1.747767,-9.125420,-7.962576,-4.500041,4.835359,0.878782,-4.191660]],[[-8.906729,0.043145,3.313363,-2.745768,-5.303343,2.991663,-4.750228,-8.559667,1.770509,4.628730,-4.489018,0.689270,-7.933404],[-0.062543,-4.919757,-9.392648,0.097469,0.081176,-7.353156,8.218023,-7.276059,6.966524,-2.892865,-5.567566,-7.611752,0.340671],[-4.524607,-3.875119,4.911075,-1.648637,2.610870,-2.715088,4.375560,-5.973835,2.940405,-9.616727,-3.161706,-1.441461,-6.077698],[-4.875395,-0.373855,9.709264,-1.698256,5.454720,-9.388252,-1.229072,8.009961,-3.450980,-5.805381,-6.049684,-3.202527,-0.112641],[3.644772,2.240124,5.997420,-3.160919,6.220637,-8.064695,3.978735,-9.824305,-8.835769,-9.313806,6.743558,-6.131338,0.068814],[-9.157360,1.847225,-6.491442,5.687250,-0.205559,0.033695,4.836196,4.808042,-4.577653,7.741992,-8.514154,7.692910,0.628256],[-2.001853,3.025708,4.940167,5.188708,-4.209634,2.792612,-1.889746,-5.244743,-6.409888,-9.895143,-1.647042,9.803500,3.896471],[1.839323,-4.401231,-9.487340,-2.212150,-1.136016,1.353323,-9.058011,7.265459,0.555551,-5.922860,4.054763,1.675118,-5.493997],[-4.451066,-4.125256,2.150064,9.300749,-0.916573,-7.414777,8.739990,-3.889002,1.624535,-8.605628,-4.831013,-3.915107,6.746132],[-0.170150,2.517882,-6.858689,-1.043067,-4.154127,-4.050428,1.108974,5.553292,1.537879,-6.094284,2.731642,6.266153,-8.125896],[4.750051,-7.162089,-2.863390,-3.186457,8.247817,7.838007,4.117084,1.318145,4.835032,-7.889693,7.837274,9.855398,-9.369297],[0.137684,-0.931766,1.848514,-9.117775,9.814538,-5.526243,-3.131922,-7.493523,8.849550,2.712624,-4.841197,9.796524,2.781514],[-3.048857,-8.158450,7.148533,-6.230362,0.545860,-1.865994,5.190520,-5.732085,4.374845,3.849993,0.313901,5.132888,-0.291046]],[[5.036545,-6.737600,-3.055258,-8.995553,1.847060,-9.393087,4.954900,-7.426717,7.239901,0.679096,0.373666,-4.418060,8.832736],[-2.385535,4.493015,-3.660304,-6.468549,0.040453,6.965777,-1.462597,-4.981110,5.815704,-3.928613,8.431096,6.608472,-3.033662],[2.105733,-7.922533,-0.137436,8.609768,9.601863,-8.435361,-1.981048,-0.010652,3.551791,1.757072,7.441462,-4.881689,-1.196840],[0.001770,-5.394894,-9.568024,-1.911504,-2.338355,7.175576,-9.571418,1.035993,6.310366,4.284356,-4.372601,-0.440394,-5.071532],[-4.455371,1.427551,-9.153316,-5.222513,-5.270167,-0.153699,2.006379,7.560406,-9.836440,9.351238,6.485072,6.371425,-7.268797],[0.316198,0.626579,-5.977740,-1.495937,-5.156939,-4.692946,-5.507658,-2.125768,-3.676645,9.442283,-6.252387,0.130723,-8.782919],[-4.328746,9.118960,7.839569,6.850282,-5.910947,-9.867786,-1.524705,8.374932,9.693433,9.294225,-1.324614,-2.981277,-1.802078],[1.162513,-7.694023,-6.860216,-2.002993,-0.575676,-9.825707,-4.679936,8.194988,-9.609255,-2.550672,5.475304,4.474252,9.631421],[-8.535698,5.157673,-7.377960,-5.347697,-3.710650,-9.321372,8.377475,-2.613455,-8.620893,-8.493109,5.880555,3.254773,5.520684],[-5.833950,-5.274003,-7.137731,4.907247,8.578736,2.230148,-1.507588,-2.144795,-3.216992,3.078676,3.086485,8.555937,-0.787674],[-6.115235,-2.754865,-4.929193,-2.954210,-4.139128,4.138961,6.781589,-4.261626,-5.309594,-0.723106,8.467591,-1.587376,-2.274349],[-0.510019,-8.430363,-0.652655,6.960274,-8.137660,9.875660,-6.785222,9.155456,0.953757,-7.887898,0.925692,7.090330,8.541572],[-2.387324,5.837622,9.698335,7.820651,-3.995795,5.705684,-0.551414,2.023846,-0.267742,-3.923609,7.626284,-7.341586,2.064871]],[[6.710441,-1.492417,9.712483,-7.134478,7.064554,-3.130675,1.153814,-9.985468,-8.500790,-9.747645,0.923319,1.031981,1.897707],[1.142235,-4.300806,9.389104,6.286975,-5.934756,4.993196,-7.180200,7.246254,0.615092,7.183660,7.325040,-6.392567,-5.264587],[-6.530975,5.427016,-4.794444,-5.451819,7.878550,-4.354609,4.828188,5.328462,-5.259535,8.526239,1.993342,-3.535605,-2.005942],[-6.297012,-8.603388,-2.523622,4.607863,-1.692446,3.832213,-4.743018,-1.253487,6.898175,-0.180700,-1.638168,-9.648775,-6.957058],[-2.323063,9.653105,-4.907241,-0.386062,-7.463348,9.315548,-1.181597,1.055267,-8.014600,0.389372,5.458550,-5.645598,9.399828],[-7.621103,-6.877566,5.003741,4.762713,-6.697791,7.080840,-8.150843,2.860683,1.011234,8.198450,1.427060,-2.544778,9.004662],[-7.347536,6.191591,-7.125734,2.195672,-6.383066,-1.799799,9.049292,7.045845,9.462552,-0.607329,-7.917003,-2.691449,1.250742],[3.196479,-6.402239,1.113328,6.846429,1.524737,-7.972330,-5.869137,6.826498,-4.745806,3.206049,9.281878,-3.159883,-7.301783],[1.032637,-1.157743,-2.850065,8.894744,-3.192907,1.494752,7.891562,-8.126438,-9.404630,2.541741,2.806353,-2.874310,7.307641],[1.580210,-7.975066,-3.265604,-6.899405,-6.042497,6.274115,-1.570153,-1.269633,2.987723,-1.771365,3.449892,-7.145414,-7.078733],[-8.761500,1.419492,0.985688,9.008547,-1.774552,4.762820,3.963634,2.481080,7.791083,-4.352717,-6.401339,-2.284551,6.706591],[7.835361,-6.604566,4.755904,-3.019896,-1.117089,7.596215,1.701902,-5.532848,3.888937,-0.132081,-1.058055,-4.332926,9.538711],[-7.577434,8.253264,1.878071,6.519891,-2.469579,4.509642,5.208391,-3.591899,2.799532,-2.105714,1.486214,8.832021,9.834732]],[[2.865117,1.357886,-6.777619,-2.832607,5.911203,-1.724860,0.476955,-5.171976,8.492514,0.763407,-1.998354,-2.401211,-9.348603],[-8.354906,1.783154,8.526509,8.023530,-4.543750,-3.460586,2.860271,-2.331554,-7.307958,1.340925,-4.258321,2.842373,-5.783912],[7.936429,-0.610631,-0.834249,4.515839,-3.856057,6.600609,4.940221,3.435906,-4.442791,-7.252793,-5.850157,6.378884,5.069089],[3.893352,1.066098,-1.839181,-8.283370,-7.433153,-2.640034,-4.104980,-8.859986,-0.483255,6.827441,2.409850,9.904660,0.130308],[-2.809139,4.013122,-7.370384,-0.132305,-2.618641,-3.858244,-9.648864,-1.983181,9.788050,7.831054,-7.622957,9.303818,-0.001414],[0.890974,-0.941004,3.645437,6.992195,-8.076995,3.344550,0.887296,-9.824676,-5.449854,-2.208482,4.216454,-0.773076,8.378360],[-7.018536,-7.960298,4.178898,-5.964210,-8.791994,6.839843,-0.275789,-8.216263,-7.857188,-6.933165,6.785673,2.726993,4.511015],[0.979963,-8.490479,-7.978151,-6.860433,0.214449,-7.916873,6.723559,7.772266,5.055072,4.282134,-1.005245,5.571672,-7.495059],[1.311319,2.519438,-2.901268,-1.702914,7.721149,8.408605,-5.559108,-3.937288,0.214085,6.117979,-7.850574,-4.186242,-9.084800],[4.102072,6.994374,4.915099,-4.873543,3.372105,2.075144,5.993979,-9.968769,-6.170273,1.229324,-2.232177,3.647703,6.450875],[-9.127025,6.373682,-9.078455,-0.461740,-8.974514,7.895589,-9.451573,0.925542,-5.304240,0.770412,3.333754,9.656981,-9.698358],[1.127340,-9.453874,4.260615,0.596591,7.289513,4.706420,5.639219,6.847345,-7.809306,-6.108421,-9.840656,-3.379600,9.848260],[3.353045,-0.369962,-0.972130,9.641397,3.369049,6.108669,5.764464,-8.995578,1.609654,-2.783185,-0.763580,-7.856130,-9.229113]],[[-0.297157,-9.970562,2.280368,-5.642070,3.175393,6.600875,3.200982,8.397813,7.219221,-8.147236,-0.216467,-4.706699,-6.958810],[9.981728,2.648488,9.764527,2.437614,7.357401,-0.750871,-4.509661,0.987251,-7.818993,-9.697933,1.500781,7.080982,-4.169539],[1.906266,-9.634308,9.180341,2.528358,-3.085505,-0.030916,-7.420860,-3.173975,-2.772513,6.512315,-9.113340,-4.432006,0.185026],[1.169528,4.222773,-1.582339,-1.801185,2.528103,9.745400,-5.387662,4.441242,7.042413,-5.321527,-6.649834,-0.789525,-3.831923],[-6.284825,-3.700611,3.141977,-5.449321,4.826599,2.946479,3.977733,7.624853,3.931743,-9.709287,3.549466,8.984739,6.397908],[-2.839122,4.192550,3.089765,7.734563,9.779421,8.993306,-6.784900,1.317099,-5.409891,-2.835481,0.813245,9.362506,-3.365760],[6.919715,-4.843740,-0.222485,-4.132494,-2.283661,3.701164,2.329108,-7.769384,-1.554239,3.094202,-1.119248,-5.468952,-3.722299],[0.581029,-6.790151,-0.554368,8.888763,-7.953593,6.580140,6.752357,-7.873810,2.951936,8.594799,-5.684741,-3.586437,3.190249],[5.560158,8.345628,2.237343,1.945502,8.027577,3.762812,6.424543,-9.541642,9.343405,-4.184627,-5.997193,4.756660,9.409133],[9.310923,-5.435105,-2.182738,-9.928955,8.499013,-9.024170,1.133039,-0.958932,-0.040518,1.760507,-5.766224,-3.960437,-8.237036],[-1.950624,7.610264,-8.333115,-0.335941,1.951821,-6.139665,-6.399698,-7.170183,3.205566,-4.133270,-0.986191,1.532540,8.343975],[-5.731674,-6.659889,-0.907938,2.349791,-6.583166,-9.902109,-1.204979,9.358456,-9.337451,-3.943493,5.456145,-7.965350,9.606393],[-2.409514,-4.263292,-4.293665,-1.814072,-4.057242,2.436880,-0.973871,3.951013,-9.602902,-1.821160,-3.517169,-4.390376,3.510164]]], dtype = "float32")#candidate|3334|(6, 13, 13)|const|float32
bop_3335 = relay.floor_divide(var_3333.astype('float32'), relay.reshape(const_3334.astype('float32'), relay.shape_of(var_3333))) # shape=(6, 13, 13)
func_1529_call = mod.get_global_var('func_1529')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_3339 = relay.TupleGetItem(func_1529_call(), 0)
call_3340 = relay.TupleGetItem(func_1530_call(), 0)
uop_3341 = relay.sinh(var_3333.astype('float64')) # shape=(6, 13, 13)
output = relay.Tuple([bop_3335,call_3339,uop_3341,])
output2 = relay.Tuple([bop_3335,call_3340,uop_3341,])
func_3343 = relay.Function([var_3333,], output)
mod['func_3343'] = func_3343
mod = relay.transform.InferType()(mod)
mutated_mod['func_3343'] = func_3343
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3344 = relay.var("var_3344", dtype = "float32", shape = (6, 13, 13))#candidate|3344|(6, 13, 13)|var|float32
func_3343_call = mutated_mod.get_global_var('func_3343')
call_3345 = func_3343_call(var_3344)
output = call_3345
func_3346 = relay.Function([var_3344], output)
mutated_mod['func_3346'] = func_3346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_3385 = relay.TupleGetItem(func_3183_call(), 0)
call_3386 = relay.TupleGetItem(func_3184_call(), 0)
uop_3387 = relay.acos(call_3385.astype('float32')) # shape=(5, 8, 1)
uop_3389 = relay.acos(call_3386.astype('float32')) # shape=(5, 8, 1)
bop_3391 = relay.less(uop_3387.astype('bool'), relay.reshape(call_3385.astype('bool'), relay.shape_of(uop_3387))) # shape=(5, 8, 1)
bop_3394 = relay.less(uop_3389.astype('bool'), relay.reshape(call_3386.astype('bool'), relay.shape_of(uop_3389))) # shape=(5, 8, 1)
output = relay.Tuple([bop_3391,])
output2 = relay.Tuple([bop_3394,])
func_3396 = relay.Function([], output)
mod['func_3396'] = func_3396
mod = relay.transform.InferType()(mod)
mutated_mod['func_3396'] = func_3396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3396_call = mutated_mod.get_global_var('func_3396')
call_3397 = func_3396_call()
output = call_3397
func_3398 = relay.Function([], output)
mutated_mod['func_3398'] = func_3398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_3438 = func_1931_call()
call_3439 = func_1931_call()
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
const_3447 = relay.const([[3,-10,-6,8,-9,-6,4,-3,-10,-9,-4,10,10,-1,-5,1,-4,6,1,4,1,-6,5,-1,-10,6,5,-6,-1,3,3,-5,-5,7,-6,-6,2,-2,-1,-4,3,-7,-9,3,-1,7,10,-10,-4,9,-9,-7,-6,10,1,-2,-5,3,1,3,2,-5,3,-7,4,8,-10,-6,5,-8,9,5,9,7,5,4,-9,10,-6,-10,-3,-6,5,-3,-8,-1,1,1,3,1,-8,-5,-4,1,-2,-10,9,-9,-6,7,3,10,-3,3,-1,-1,-9,-7,1,-3,-9,7,-7,-4,-9,8,8,-6,-3,6,3,-6,-6,-7,1,2,-3,9,7,6,4,-8,3,7,2,1,-3,-10,-10,-5,-9,2,-8,-3,-4,-1,-2,-3,2,3,3,1,-3,-4,2,-3,-6,10,-3,9,1,-6,-8,7,10,5,-4,-9,1,-9,3,-1,-6,-5,5,8,3,-6,4,-4,-1,-10,-9,-1,2,-3,-1,-6,-7,-8,4,-6,-10,1,-6,-2,5,-6,-1,-5,9,10,4,7,-6,4,10,10,-4,8,5,9,-2,-6,-1,7,-1,-10,-10,8,3,-7,-4,7,-7,8,-4,4,3,10,3,6,2,-2,-4,-8,2,1,2,2,2,-1,-8,-4,-7,6,10,5,-7,-6,-7,7,-10,5,-6,-1,-8,7,-7,8,-5,-3,6,9,-9,2,9,-5,-10,3,7,8,-6,5,6,-7,-10,8,-2,-9,1,-7,3,-9,2,2,-6,9,5,-5,-9,-4,5,-5,8,-8,-5,7,-6,-4,-8,10,-7,6,-2,5,-3,10,-10,5,-9,4,7,-4,10,1,-6,-4,1,7,10,5,-2,3,8,-7,-10,-2,2,10,-6,2,6,-7,7,-10,-7,-2,8,8,-1,6,5,10,4,1,-3,-3,8,-5,5,2,10,10,9,-7,-4,4,9,-9,4,-6,-3,-9,1,6,9,8,5,-9,-8,5,-9,1,4,4,8,-6,-9,3,-9,5,-8,9,-1,-8,-7,10,3,-4,9,-5,-8,-9,-8,-6,-1,6,2,-3,-4,-3,-5,6,2,4,-10,10,4,2,2,-8,8,2,-7,-4,-7,3,8,1,9,-5,8,4,7,-1,-5,1,1,3,10,1,4,3,-3,-6,-2,3,6,-10,-5,-3,-8,-6,-8,10,-8,-7,-7,6,5,-4,3,-4,5,6,-5,-2,1,-5,-1,-9,6,-3,10,-2,-1,1,4,-7,-1,8,-9,-10,-2,-1,10,2,-10,8,4,5,6,3,3,-8,-10,2,-9,-2,-9,-6,5,-4,4,-6,-10,6,-9,6,9,-8,-2,-8,5,4,3,5,-9,-6,1,-1,-3,8,6,-3,10,3,2,-5,-3,2,-10,-5,-6,-9,-1,7],[-7,-7,1,-9,-1,-4,-6,-1,9,-5,2,5,-1,4,-5,7,8,-7,3,-3,-10,1,-6,-7,8,4,-3,10,3,5,7,-2,-5,-5,6,-5,4,4,-10,7,-4,8,9,-1,-1,2,8,2,-2,-6,-6,-5,-8,-4,-10,6,1,-3,-3,-3,-1,-2,-9,-6,5,7,2,-4,1,-9,-9,6,9,10,-4,-6,-8,-3,5,5,-9,3,-6,-4,-7,9,5,5,5,-6,8,3,2,-2,5,-9,4,8,9,9,4,-1,7,5,-3,2,-4,-9,1,3,1,-2,4,-4,-5,-10,-5,8,-10,4,3,-5,1,5,-7,9,2,10,-3,-10,9,7,-2,-6,7,6,-5,9,6,7,-4,-1,8,-2,-8,-1,-6,-3,-3,-1,-8,-2,-9,-9,7,-10,4,7,3,-5,4,9,4,8,-8,10,9,1,5,5,-9,2,8,-5,9,-1,-6,4,-2,-9,-3,-8,-3,2,-10,9,-4,3,10,-3,8,3,6,-5,-2,-1,-5,9,8,7,8,9,9,-6,-8,10,-6,-9,2,3,10,1,2,5,-3,2,-8,-5,-3,-6,1,6,-8,-2,-10,-6,-8,6,-9,2,5,3,-2,-10,1,-7,-3,10,9,4,6,2,9,5,-10,1,-10,-9,-5,9,-7,8,9,-3,-1,-10,9,2,7,-7,4,-2,-2,-7,10,-5,-10,8,3,8,8,-1,-7,6,-2,-2,-3,-9,3,-4,-1,9,1,9,-9,-8,-4,-6,3,4,9,2,-10,8,6,-8,10,8,-5,5,-5,-2,1,-9,-2,-10,1,-2,2,8,-10,6,-4,-3,-3,-4,1,-7,-4,9,-1,6,2,7,-5,-3,-9,-7,3,-1,-10,7,1,-8,-2,10,5,-9,1,10,-1,3,3,-3,1,5,1,5,-7,6,9,5,9,2,10,-7,6,-8,-9,-5,7,4,-3,-9,-3,10,-10,-7,-8,10,-10,6,-9,4,7,10,1,-3,2,-3,-8,6,-7,-6,1,-1,-7,8,-3,-3,4,-8,5,9,5,4,-6,-1,3,-8,-7,7,7,-7,-8,3,-4,-4,2,10,-7,1,5,6,9,-4,2,10,7,-8,-10,4,1,4,-3,-1,9,6,3,-3,4,9,-1,3,-6,2,3,-1,5,-10,-10,-1,-2,-4,-8,7,6,-8,-5,-4,4,-9,1,-3,-7,-7,3,-5,-6,10,-6,4,3,1,-4,10,-1,9,1,10,-7,5,6,5,-1,-4,3,10,-3,-5,4,-7,6,-8,-7,3,5,4,-7,1,-5,4,-6,-4,-3,-4,-4,-3,6,-7,10,-7,-5,-4,1,10,-4,-5,-9,7,-10,3,3,-6,9,-2,-1,-4,1,3,-7,9,7,10,-7,-2,-10,-2]], dtype = "int8")#candidate|3447|(2, 528)|const|int8
call_3446 = relay.TupleGetItem(func_322_call(relay.reshape(const_3447.astype('int8'), [11, 12, 8])), 0)
call_3448 = relay.TupleGetItem(func_325_call(relay.reshape(const_3447.astype('int8'), [11, 12, 8])), 0)
output = relay.Tuple([call_3438,call_3446,const_3447,])
output2 = relay.Tuple([call_3439,call_3448,const_3447,])
func_3456 = relay.Function([], output)
mod['func_3456'] = func_3456
mod = relay.transform.InferType()(mod)
mutated_mod['func_3456'] = func_3456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3456_call = mutated_mod.get_global_var('func_3456')
call_3457 = func_3456_call()
output = call_3457
func_3458 = relay.Function([], output)
mutated_mod['func_3458'] = func_3458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2847_call = mod.get_global_var('func_2847')
func_2848_call = mutated_mod.get_global_var('func_2848')
call_3488 = relay.TupleGetItem(func_2847_call(), 0)
call_3489 = relay.TupleGetItem(func_2848_call(), 0)
output = call_3488
output2 = call_3489
func_3507 = relay.Function([], output)
mod['func_3507'] = func_3507
mod = relay.transform.InferType()(mod)
mutated_mod['func_3507'] = func_3507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mutated_mod.get_global_var('func_3507')
call_3508 = func_3507_call()
output = call_3508
func_3509 = relay.Function([], output)
mutated_mod['func_3509'] = func_3509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_3541 = relay.TupleGetItem(func_3396_call(), 0)
call_3542 = relay.TupleGetItem(func_3398_call(), 0)
output = relay.Tuple([call_3541,])
output2 = relay.Tuple([call_3542,])
func_3543 = relay.Function([], output)
mod['func_3543'] = func_3543
mod = relay.transform.InferType()(mod)
mutated_mod['func_3543'] = func_3543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3543_call = mutated_mod.get_global_var('func_3543')
call_3544 = func_3543_call()
output = call_3544
func_3545 = relay.Function([], output)
mutated_mod['func_3545'] = func_3545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_3568 = relay.TupleGetItem(func_3183_call(), 0)
call_3569 = relay.TupleGetItem(func_3184_call(), 0)
var_3584 = relay.var("var_3584", dtype = "float64", shape = (5, 8, 12))#candidate|3584|(5, 8, 12)|var|float64
bop_3585 = relay.logical_or(call_3568.astype('bool'), var_3584.astype('bool')) # shape=(5, 8, 12)
bop_3588 = relay.logical_or(call_3569.astype('bool'), var_3584.astype('bool')) # shape=(5, 8, 12)
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
const_3591 = relay.const([4,9,-10,-5,-7,-6,-10,6,-3,3,-2,-2,10,-8,-10,8,-6,3,-1,1,-9,2,-9,3,5,-1,-2,7,6,-2,8,-10,8,4,-4,-7,3,4,2,-7,1,5,-1,-7,8,3,9,4,-1,-7,3,-9,7,-10,1,5,-5,7,-5,-5,4,-10,-3,10,-1,10,3,2,-3,9,2,-7,-6,-5,1,-3,7,-7,8,-6,-6,-4,-6,-9,1,-2,-3,1,5,10,5,-10,9,-7,-3,-7,-9,-10,-9,3,-6,-2,8,-8,-9,-9,-4,-9,4,-1,8,8,2,4,6,1,4,2,-7,5,1,-2,-2,-1,8,-7,-1,-6,4,4,7,3,9,3,10,-3,1,7,6,-2,-9,1,-6,2,-6,10,-2,-5,2,6,-6,-2,-4,-2,6,-3,5,-4,-10,2,3,-9,7,-5,-4,1,-3,8,-2,6,-8,-3,-2,5,5,9,-1,4,-4,7,3,-7,10,2,10,8,-8,3,9,-3,5,-2,-8,-4,-7,-10,10,-7,-7,-2,8,6,-2,5,7,6,7,10,-6,10,9,6,-1,10,1,-4,-4,2,-9,7,-4,-2,3,-8,8,4,10,-7,-2,-9,-8,9,-5,-8,-9,-2,2,-6,6,5,2,1,9,2,-4,-4,4,-6,8,3,1,-2,1,-7,10,1,1,-3,-10,4,6,8,-5,8,8,-3,-9,3,1,-7,4,-4,-1,-9,-3,-7,-3,8,-9,3,8,-8,9,6,-3,-4,10,4,-6,-2,-6,-8,4,-10,2,10,-7,6,-2,-9,-3,2,8,3,-8,3,-6,6,-6,-4,-8,-8,-5,-3,5,1,-5,-1,2,-9,1,-6,-4,10,9,-8,-8,-3,1,9,-10,-3,-7,7,8,-10,7,-9,-10,-1,-1,-5,-7,4,-6,3,-5,-10,1,-2,3,-2,-9,9,8,-8,1,9,-4,6,-6,-8,7,5,-7,-9,-10,9,1,-7,-10,-7,-10,8,1,-6,5,10,-3,-10,-4,9,1,3,9,-9,7,-9,4,1,-3,2,8,-8,1,-1,8,-10,9,-10,-5,7,-9,-9,6,-8,-4,7,-6,-4,6,3,3,-4,7,1,5,4,-4,6,-2,1,9,-9,-4,2,-6,5,-8,-4,-2,-7,-4,-8,-7,-10,-9,6,-10,2,7,5,9,-7,-6,-2,-7,-3,3,9,6,-8,10,-2,8,-4,8,-10,-9,5,-7,4,-7,5,10,9,-3,2,10,4,10,5,-9,-6,-4,-4,8,-5,6,-5,3,-6,-1,-10,4,1,3,-1,-2,1,-8,7,2,8,-3,6,-7,4,3,-8,-1,-1,6,-7,9,-6,-2,10,6,-1,3,9,-2,-5,-9,1,4,4,-4,-10,-10,1,-9,3,-10,-6,-4,2,-8,-10,-2,8,-3,-7,7,1,4,-7,-2,10,-9,-7,-3,-8,6,1,10,-5,4,-9,9,-6,1,-6,8,-5,4,9,-10,10,6,5,1,-9,2,-3,10,-4,5,-2,-7,7,10,9,-4,8,-10,-7,5,-3,-6,5,-8,-6,8,5,6,7,9,-8,4,-4,-10,-5,-9,-1,-7,-2,5,7,6,1,3,10,3,-6,7,-5,-10,-4,-9,5,-1,-10,-3,-2,-8,-10,2,-4,9,3,-9,-5,-9,10,-1,-5,-2,-1,-1,-5,-7,-9,-7,3,2,-2,-6,-3,-3,2,-8,8,-1,6,-3,10,-5,8,-3,-8,9,-7,-6,-10,3,-6,-1,2,5,-6,8,8,-5,5,-9,3,4,3,-2,2,-6,-8,-3,1,-8,-4,-10,-2,-1,5,2,8,-9,6,5,-7,-6,-10,-5,7,-5,-2,5,4,-2,8,6,-10,8,-6,-3,7,-8,-10,-7,6,10,-9,-3,3,-1,-7,-6,3,2,8,-4,7,-4,-5,-2,5,1,8,-6,-7,-1,-3,3,2,5,3,7,-1,6,1,9,1,9,-1,-8,1,5,8,-2,-5,10,-6,7,7,-5,1,-4,1,-10,6,3,9,5,-7,-8,4,8,7,9,-7,4,-8,10,10,4,-10,-5,-6,-10,7,-3,8,-1,7,10,-6,-3,1,-4,5,-6,6,8,4,-2,6,10,-7,10,2,-1,4,-3,-1,-5,4,3,-5,-1,-9,-9,-8,-8,1,2,-7,4,-9,6,1,-6,3,6,-10,-8,-9,3,-8,-4,-8,4,9,7,-2,-8,4,-1,-1,6,5,-10,3,-6,6,-9,8,2,-3,7,-1,10,7,4,-2,1,6,-4,7,-9,-1,9,-4,-9,9,-4,-1,8,8,7,-2,-7,-4,-7,-2,3,-5,-5,3,-5,9,5,-4,7,-6,-1,-7,-9,1,1,2,-7,6,5,-5,2,-2,4,-1,-9,7,7,10,4,-4,5,1,-3,5,6,10,3,-6,-1,8,-6,-10,1,-1,-1,4,-10,-9,1,3,-5,-7,9,5,-2,8,2,-1,1,-9,-8,10,7,-3,5,-8,-10,-1,10,-7,-1,-10,-6,-7,4,9,7,10,-9,2,8,6,-7,-7,3,9,2,8,-2,-2,10,-8,1,3,-10,7,7,10,-10,-8,2,10,9,-1,-4,-5,6,-3,1,10,3,3,-1,-1,-9,-6,8,-6,-6,6,-10,4,4,5,-5,9,10,-5,5,4,7,-7,-7,-4,10,3,-10,-7,8,4,-7,-9,-6,-10,4,-7,3,8,6,3,1,-7,-4,-9,-4,-4,-7,10,1,4,-3,8,4,-5,9,6,5,3,8,10,5,5,-10,3,4,-9,-8,-4,-5,5,-9,4,-4,3], dtype = "int8")#candidate|3591|(1056,)|const|int8
call_3590 = relay.TupleGetItem(func_322_call(relay.reshape(const_3591.astype('int8'), [11, 12, 8])), 0)
call_3592 = relay.TupleGetItem(func_325_call(relay.reshape(const_3591.astype('int8'), [11, 12, 8])), 0)
output = relay.Tuple([bop_3585,call_3590,const_3591,])
output2 = relay.Tuple([bop_3588,call_3592,const_3591,])
func_3614 = relay.Function([var_3584,], output)
mod['func_3614'] = func_3614
mod = relay.transform.InferType()(mod)
var_3615 = relay.var("var_3615", dtype = "float64", shape = (5, 8, 12))#candidate|3615|(5, 8, 12)|var|float64
output = func_3614(var_3615)
func_3616 = relay.Function([var_3615], output)
mutated_mod['func_3616'] = func_3616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_3660 = relay.TupleGetItem(func_2096_call(), 4)
call_3661 = relay.TupleGetItem(func_2098_call(), 4)
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_3675 = func_1176_call()
call_3676 = func_1176_call()
bop_3677 = relay.maximum(call_3660.astype('int16'), relay.reshape(call_3675.astype('int16'), relay.shape_of(call_3660))) # shape=(5, 8, 1)
bop_3680 = relay.maximum(call_3661.astype('int16'), relay.reshape(call_3676.astype('int16'), relay.shape_of(call_3661))) # shape=(5, 8, 1)
output = relay.Tuple([bop_3677,])
output2 = relay.Tuple([bop_3680,])
func_3682 = relay.Function([], output)
mod['func_3682'] = func_3682
mod = relay.transform.InferType()(mod)
mutated_mod['func_3682'] = func_3682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3682_call = mutated_mod.get_global_var('func_3682')
call_3683 = func_3682_call()
output = call_3683
func_3684 = relay.Function([], output)
mutated_mod['func_3684'] = func_3684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_3691 = func_1176_call()
call_3692 = func_1176_call()
const_3730 = relay.const([[[-7.940565,-7.690989,5.484642,9.508347,-4.638151],[-1.498033,6.737400,6.615960,-8.567535,-6.491761],[-7.228539,0.076598,-4.630113,0.274100,-1.853770],[-6.085038,4.361641,6.664032,5.964682,-4.865593],[-2.998925,-3.017014,-3.975516,2.418460,-6.440405],[-5.654658,4.907163,-3.517123,-4.387284,7.485375],[-5.489398,1.477410,-3.749059,-2.806421,-9.063053],[3.913413,4.497695,-9.485398,4.484200,1.151508]],[[0.361429,7.117732,3.291419,-3.844424,0.537230],[-7.854290,3.494233,9.155992,5.708901,-7.615951],[6.257096,-3.343912,4.714255,-7.144140,-1.581946],[-8.916773,-4.834250,-9.832048,3.123410,7.091741],[-4.383654,8.648248,-1.829979,4.911029,-4.330112],[5.697694,-6.247319,4.911668,-4.891908,-3.740201],[6.126010,-5.356493,-5.599633,6.630349,8.572294],[-0.618008,9.963214,-1.604435,0.169528,1.740563]],[[3.263175,8.990718,-1.377089,7.638802,-6.396122],[8.165778,-7.979863,6.809213,-4.636489,-8.774113],[-1.216089,8.699965,-1.755623,3.964816,3.193877],[-0.944271,8.558944,-2.879947,-2.697500,-7.168890],[-4.433220,-0.452702,5.124129,4.111848,-0.097988],[0.397399,1.169359,-1.236112,-0.765697,3.279482],[-7.381145,-2.423503,7.757786,4.510497,-5.684845],[-9.883205,1.808851,8.113041,6.692580,-4.062608]],[[6.385525,-0.166745,-2.914371,-3.919247,-1.340894],[8.472005,0.258146,-2.139892,-1.655729,-8.799339],[8.657084,3.153247,1.588163,4.620461,-0.048974],[7.401663,8.245048,-6.625653,-0.308618,8.808177],[-3.200604,-9.943608,-1.533894,-6.091570,-0.037171],[-9.617355,5.873928,9.173297,-4.965107,8.330855],[-9.705438,-5.217409,-7.819115,-4.216090,-8.159510],[7.261581,-7.604835,-0.153258,-5.484869,5.205047]],[[-5.412468,-2.813960,-9.425556,-3.512148,-3.856417],[4.847298,-7.017882,8.424643,-5.876735,-0.728365],[5.359744,6.527782,0.035804,-0.539541,-9.928434],[-2.156112,1.930362,-4.260013,-8.601962,8.251377],[7.740486,-7.491000,-4.721099,-0.108304,5.002068],[0.051404,0.721674,-2.519252,5.334625,-5.783648],[-0.743067,-8.049157,-3.602164,6.728454,2.997844],[0.121546,2.918718,2.792771,9.839332,-4.691128]]], dtype = "float64")#candidate|3730|(5, 8, 5)|const|float64
bop_3731 = relay.bitwise_xor(call_3691.astype('int64'), const_3730.astype('int64')) # shape=(5, 8, 5)
bop_3734 = relay.bitwise_xor(call_3692.astype('int64'), const_3730.astype('int64')) # shape=(5, 8, 5)
bop_3743 = relay.subtract(call_3691.astype('float64'), const_3730.astype('float64')) # shape=(5, 8, 5)
bop_3746 = relay.subtract(call_3692.astype('float64'), const_3730.astype('float64')) # shape=(5, 8, 5)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_3747 = func_1931_call()
call_3748 = func_1931_call()
uop_3754 = relay.erf(bop_3743.astype('float32')) # shape=(5, 8, 5)
uop_3756 = relay.erf(bop_3746.astype('float32')) # shape=(5, 8, 5)
output = relay.Tuple([bop_3731,call_3747,uop_3754,])
output2 = relay.Tuple([bop_3734,call_3748,uop_3756,])
func_3759 = relay.Function([], output)
mod['func_3759'] = func_3759
mod = relay.transform.InferType()(mod)
output = func_3759()
func_3760 = relay.Function([], output)
mutated_mod['func_3760'] = func_3760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1619_call = mod.get_global_var('func_1619')
func_1621_call = mutated_mod.get_global_var('func_1621')
call_3770 = relay.TupleGetItem(func_1619_call(), 0)
call_3771 = relay.TupleGetItem(func_1621_call(), 0)
output = relay.Tuple([call_3770,])
output2 = relay.Tuple([call_3771,])
func_3795 = relay.Function([], output)
mod['func_3795'] = func_3795
mod = relay.transform.InferType()(mod)
output = func_3795()
func_3796 = relay.Function([], output)
mutated_mod['func_3796'] = func_3796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3543_call = mod.get_global_var('func_3543')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_3849 = relay.TupleGetItem(func_3543_call(), 0)
call_3850 = relay.TupleGetItem(func_3545_call(), 0)
output = relay.Tuple([call_3849,])
output2 = relay.Tuple([call_3850,])
func_3877 = relay.Function([], output)
mod['func_3877'] = func_3877
mod = relay.transform.InferType()(mod)
output = func_3877()
func_3878 = relay.Function([], output)
mutated_mod['func_3878'] = func_3878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_3897 = relay.TupleGetItem(func_3682_call(), 0)
call_3898 = relay.TupleGetItem(func_3684_call(), 0)
output = call_3897
output2 = call_3898
func_3907 = relay.Function([], output)
mod['func_3907'] = func_3907
mod = relay.transform.InferType()(mod)
output = func_3907()
func_3908 = relay.Function([], output)
mutated_mod['func_3908'] = func_3908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3760_call = mutated_mod.get_global_var('func_3760')
call_3953 = relay.TupleGetItem(func_3759_call(), 2)
call_3954 = relay.TupleGetItem(func_3760_call(), 2)
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_3963 = relay.TupleGetItem(func_1214_call(), 0)
call_3964 = relay.TupleGetItem(func_1215_call(), 0)
func_2685_call = mod.get_global_var('func_2685')
func_2689_call = mutated_mod.get_global_var('func_2689')
var_3968 = relay.var("var_3968", dtype = "int8", shape = (1056,))#candidate|3968|(1056,)|var|int8
var_3969 = relay.var("var_3969", dtype = "float64", shape = (660,))#candidate|3969|(660,)|var|float64
var_3970 = relay.var("var_3970", dtype = "float64", shape = (16, 10))#candidate|3970|(16, 10)|var|float64
call_3967 = relay.TupleGetItem(func_2685_call(relay.reshape(var_3968.astype('int8'), [1056,]), relay.reshape(var_3969.astype('float64'), [660,]), relay.reshape(var_3970.astype('float64'), [160,]), ), 1)
call_3971 = relay.TupleGetItem(func_2689_call(relay.reshape(var_3968.astype('int8'), [1056,]), relay.reshape(var_3969.astype('float64'), [660,]), relay.reshape(var_3970.astype('float64'), [160,]), ), 1)
func_3759_call = mod.get_global_var('func_3759')
func_3760_call = mutated_mod.get_global_var('func_3760')
call_3975 = relay.TupleGetItem(func_3759_call(), 0)
call_3976 = relay.TupleGetItem(func_3760_call(), 0)
output = relay.Tuple([call_3953,call_3963,call_3967,var_3968,var_3969,var_3970,call_3975,])
output2 = relay.Tuple([call_3954,call_3964,call_3971,var_3968,var_3969,var_3970,call_3976,])
func_3982 = relay.Function([var_3968,var_3969,var_3970,], output)
mod['func_3982'] = func_3982
mod = relay.transform.InferType()(mod)
mutated_mod['func_3982'] = func_3982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3982_call = mutated_mod.get_global_var('func_3982')
var_3984 = relay.var("var_3984", dtype = "int8", shape = (1056,))#candidate|3984|(1056,)|var|int8
var_3985 = relay.var("var_3985", dtype = "float64", shape = (660,))#candidate|3985|(660,)|var|float64
var_3986 = relay.var("var_3986", dtype = "float64", shape = (16, 10))#candidate|3986|(16, 10)|var|float64
call_3983 = func_3982_call(var_3984,var_3985,var_3986,)
output = call_3983
func_3987 = relay.Function([var_3984,var_3985,var_3986,], output)
mutated_mod['func_3987'] = func_3987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2190_call = mod.get_global_var('func_2190')
func_2191_call = mutated_mod.get_global_var('func_2191')
call_3999 = relay.TupleGetItem(func_2190_call(), 5)
call_4000 = relay.TupleGetItem(func_2191_call(), 5)
output = relay.Tuple([call_3999,])
output2 = relay.Tuple([call_4000,])
func_4012 = relay.Function([], output)
mod['func_4012'] = func_4012
mod = relay.transform.InferType()(mod)
mutated_mod['func_4012'] = func_4012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4012_call = mutated_mod.get_global_var('func_4012')
call_4013 = func_4012_call()
output = call_4013
func_4014 = relay.Function([], output)
mutated_mod['func_4014'] = func_4014
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4027 = relay.var("var_4027", dtype = "float64", shape = (5, 12, 7))#candidate|4027|(5, 12, 7)|var|float64
uop_4028 = relay.sigmoid(var_4027.astype('float64')) # shape=(5, 12, 7)
output = relay.Tuple([uop_4028,])
output2 = relay.Tuple([uop_4028,])
func_4032 = relay.Function([var_4027,], output)
mod['func_4032'] = func_4032
mod = relay.transform.InferType()(mod)
var_4033 = relay.var("var_4033", dtype = "float64", shape = (5, 12, 7))#candidate|4033|(5, 12, 7)|var|float64
output = func_4032(var_4033)
func_4034 = relay.Function([var_4033], output)
mutated_mod['func_4034'] = func_4034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1900_call = mod.get_global_var('func_1900')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_4101 = func_1900_call()
call_4102 = func_1900_call()
func_2927_call = mod.get_global_var('func_2927')
func_2929_call = mutated_mod.get_global_var('func_2929')
call_4103 = func_2927_call()
call_4104 = func_2927_call()
bop_4117 = relay.floor_divide(call_4101.astype('float64'), relay.reshape(call_4103.astype('float64'), relay.shape_of(call_4101))) # shape=(5, 8, 1)
bop_4120 = relay.floor_divide(call_4102.astype('float64'), relay.reshape(call_4104.astype('float64'), relay.shape_of(call_4102))) # shape=(5, 8, 1)
func_3795_call = mod.get_global_var('func_3795')
func_3796_call = mutated_mod.get_global_var('func_3796')
call_4137 = relay.TupleGetItem(func_3795_call(), 0)
call_4138 = relay.TupleGetItem(func_3796_call(), 0)
output = relay.Tuple([bop_4117,call_4137,])
output2 = relay.Tuple([bop_4120,call_4138,])
func_4154 = relay.Function([], output)
mod['func_4154'] = func_4154
mod = relay.transform.InferType()(mod)
output = func_4154()
func_4155 = relay.Function([], output)
mutated_mod['func_4155'] = func_4155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2847_call = mod.get_global_var('func_2847')
func_2848_call = mutated_mod.get_global_var('func_2848')
call_4229 = relay.TupleGetItem(func_2847_call(), 0)
call_4230 = relay.TupleGetItem(func_2848_call(), 0)
func_1900_call = mod.get_global_var('func_1900')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_4231 = func_1900_call()
call_4232 = func_1900_call()
uop_4238 = relay.acosh(call_4229.astype('float64')) # shape=(5, 8, 1)
uop_4240 = relay.acosh(call_4230.astype('float64')) # shape=(5, 8, 1)
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_4241 = relay.TupleGetItem(func_3682_call(), 0)
call_4242 = relay.TupleGetItem(func_3684_call(), 0)
output = relay.Tuple([call_4231,uop_4238,call_4241,])
output2 = relay.Tuple([call_4232,uop_4240,call_4242,])
func_4250 = relay.Function([], output)
mod['func_4250'] = func_4250
mod = relay.transform.InferType()(mod)
output = func_4250()
func_4251 = relay.Function([], output)
mutated_mod['func_4251'] = func_4251
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4272 = relay.var("var_4272", dtype = "float32", shape = (9, 15, 9))#candidate|4272|(9, 15, 9)|var|float32
uop_4273 = relay.acosh(var_4272.astype('float32')) # shape=(9, 15, 9)
func_3759_call = mod.get_global_var('func_3759')
func_3760_call = mutated_mod.get_global_var('func_3760')
call_4277 = relay.TupleGetItem(func_3759_call(), 1)
call_4278 = relay.TupleGetItem(func_3760_call(), 1)
output = relay.Tuple([uop_4273,call_4277,])
output2 = relay.Tuple([uop_4273,call_4278,])
func_4289 = relay.Function([var_4272,], output)
mod['func_4289'] = func_4289
mod = relay.transform.InferType()(mod)
var_4290 = relay.var("var_4290", dtype = "float32", shape = (9, 15, 9))#candidate|4290|(9, 15, 9)|var|float32
output = func_4289(var_4290)
func_4291 = relay.Function([var_4290], output)
mutated_mod['func_4291'] = func_4291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3042_call = mod.get_global_var('func_3042')
func_3043_call = mutated_mod.get_global_var('func_3043')
call_4366 = func_3042_call()
call_4367 = func_3042_call()
func_2977_call = mod.get_global_var('func_2977')
func_2980_call = mutated_mod.get_global_var('func_2980')
const_4380 = relay.const([-4,5,-8,9,10,-6,10,8,-10,6,9,2,3,-5,4,-5,2,4,4,5,-9,-10,-3,-9,-7,4,10,4,-8,10,-2,2,-4,-8,-10,-10,-4,-7,1,9,1,-4,9,-4,-8,1,-7,7,-9,-10,6,9,-10,-8,-4,-9,-10,4,2,8,-2,3,2,-1], dtype = "uint16")#candidate|4380|(64,)|const|uint16
call_4379 = relay.TupleGetItem(func_2977_call(relay.reshape(const_4380.astype('uint16'), [2, 32])), 0)
call_4381 = relay.TupleGetItem(func_2980_call(relay.reshape(const_4380.astype('uint16'), [2, 32])), 0)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_4402 = func_1931_call()
call_4403 = func_1931_call()
uop_4409 = relay.atan(call_4402.astype('float64')) # shape=(5, 8, 1)
uop_4411 = relay.atan(call_4403.astype('float64')) # shape=(5, 8, 1)
output = relay.Tuple([call_4366,call_4379,const_4380,uop_4409,])
output2 = relay.Tuple([call_4367,call_4381,const_4380,uop_4411,])
func_4423 = relay.Function([], output)
mod['func_4423'] = func_4423
mod = relay.transform.InferType()(mod)
output = func_4423()
func_4424 = relay.Function([], output)
mutated_mod['func_4424'] = func_4424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1529_call = mod.get_global_var('func_1529')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_4473 = relay.TupleGetItem(func_1529_call(), 0)
call_4474 = relay.TupleGetItem(func_1530_call(), 0)
output = relay.Tuple([call_4473,])
output2 = relay.Tuple([call_4474,])
func_4478 = relay.Function([], output)
mod['func_4478'] = func_4478
mod = relay.transform.InferType()(mod)
mutated_mod['func_4478'] = func_4478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4478_call = mutated_mod.get_global_var('func_4478')
call_4479 = func_4478_call()
output = call_4479
func_4480 = relay.Function([], output)
mutated_mod['func_4480'] = func_4480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3907_call = mod.get_global_var('func_3907')
func_3908_call = mutated_mod.get_global_var('func_3908')
call_4559 = func_3907_call()
call_4560 = func_3907_call()
output = call_4559
output2 = call_4560
func_4573 = relay.Function([], output)
mod['func_4573'] = func_4573
mod = relay.transform.InferType()(mod)
output = func_4573()
func_4574 = relay.Function([], output)
mutated_mod['func_4574'] = func_4574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3062_call = mod.get_global_var('func_3062')
func_3063_call = mutated_mod.get_global_var('func_3063')
call_4601 = relay.TupleGetItem(func_3062_call(), 2)
call_4602 = relay.TupleGetItem(func_3063_call(), 2)
output = relay.Tuple([call_4601,])
output2 = relay.Tuple([call_4602,])
func_4614 = relay.Function([], output)
mod['func_4614'] = func_4614
mod = relay.transform.InferType()(mod)
output = func_4614()
func_4615 = relay.Function([], output)
mutated_mod['func_4615'] = func_4615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3311_call = mod.get_global_var('func_3311')
func_3312_call = mutated_mod.get_global_var('func_3312')
call_4619 = relay.TupleGetItem(func_3311_call(), 2)
call_4620 = relay.TupleGetItem(func_3312_call(), 2)
func_3543_call = mod.get_global_var('func_3543')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_4621 = relay.TupleGetItem(func_3543_call(), 0)
call_4622 = relay.TupleGetItem(func_3545_call(), 0)
bop_4634 = relay.left_shift(call_4621.astype('uint8'), relay.reshape(call_4619.astype('uint8'), relay.shape_of(call_4621))) # shape=(5, 8, 1)
bop_4637 = relay.left_shift(call_4622.astype('uint8'), relay.reshape(call_4620.astype('uint8'), relay.shape_of(call_4622))) # shape=(5, 8, 1)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_4638 = func_3507_call()
call_4639 = func_3507_call()
output = relay.Tuple([bop_4634,call_4638,])
output2 = relay.Tuple([bop_4637,call_4639,])
func_4647 = relay.Function([], output)
mod['func_4647'] = func_4647
mod = relay.transform.InferType()(mod)
mutated_mod['func_4647'] = func_4647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4647_call = mutated_mod.get_global_var('func_4647')
call_4648 = func_4647_call()
output = call_4648
func_4649 = relay.Function([], output)
mutated_mod['func_4649'] = func_4649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3907_call = mod.get_global_var('func_3907')
func_3908_call = mutated_mod.get_global_var('func_3908')
call_4658 = func_3907_call()
call_4659 = func_3907_call()
output = relay.Tuple([call_4658,])
output2 = relay.Tuple([call_4659,])
func_4669 = relay.Function([], output)
mod['func_4669'] = func_4669
mod = relay.transform.InferType()(mod)
output = func_4669()
func_4670 = relay.Function([], output)
mutated_mod['func_4670'] = func_4670
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4680 = relay.const([[[5.337772,4.241923,8.306801,3.076936,-7.056542,-3.564643,-9.904039,-8.683584],[6.887051,2.010993,8.044037,4.807004,1.562249,3.218790,7.060068,-0.501892],[5.542904,3.580814,1.282419,2.443569,3.119546,-5.828898,-8.066655,-5.014714]],[[-1.005995,9.170735,-7.705520,7.127206,9.272597,1.949642,-1.470653,1.006740],[9.509071,-4.164507,0.166411,9.366871,6.156358,-7.702838,-6.478343,0.896615],[0.569757,-6.076586,5.502993,3.491497,7.115806,-1.776107,-3.866443,2.095006]]], dtype = "float64")#candidate|4680|(2, 3, 8)|const|float64
uop_4681 = relay.sinh(const_4680.astype('float64')) # shape=(2, 3, 8)
func_4573_call = mod.get_global_var('func_4573')
func_4574_call = mutated_mod.get_global_var('func_4574')
call_4690 = func_4573_call()
call_4691 = func_4573_call()
output = relay.Tuple([uop_4681,call_4690,])
output2 = relay.Tuple([uop_4681,call_4691,])
func_4694 = relay.Function([], output)
mod['func_4694'] = func_4694
mod = relay.transform.InferType()(mod)
output = func_4694()
func_4695 = relay.Function([], output)
mutated_mod['func_4695'] = func_4695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2927_call = mod.get_global_var('func_2927')
func_2929_call = mutated_mod.get_global_var('func_2929')
call_4717 = func_2927_call()
call_4718 = func_2927_call()
output = relay.Tuple([call_4717,])
output2 = relay.Tuple([call_4718,])
func_4730 = relay.Function([], output)
mod['func_4730'] = func_4730
mod = relay.transform.InferType()(mod)
output = func_4730()
func_4731 = relay.Function([], output)
mutated_mod['func_4731'] = func_4731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_4746 = relay.TupleGetItem(func_3183_call(), 0)
call_4747 = relay.TupleGetItem(func_3184_call(), 0)
output = relay.Tuple([call_4746,])
output2 = relay.Tuple([call_4747,])
func_4789 = relay.Function([], output)
mod['func_4789'] = func_4789
mod = relay.transform.InferType()(mod)
output = func_4789()
func_4790 = relay.Function([], output)
mutated_mod['func_4790'] = func_4790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2927_call = mod.get_global_var('func_2927')
func_2929_call = mutated_mod.get_global_var('func_2929')
call_4794 = func_2927_call()
call_4795 = func_2927_call()
func_1770_call = mod.get_global_var('func_1770')
func_1772_call = mutated_mod.get_global_var('func_1772')
const_4799 = relay.const([-4,-9,-6,8,5,-8,-9,10,-1,1,8,8,-7,9,-4,3,-7,-5,-7,7,-8,2,8,-7,-6,10,6,-6,-5,-6,-5,9,1,5,8,3,-10,3,-1,-6,-3,-1,-6,-1,-1,-2,-7,-8,-4,10,8,-7,-10,-4,-3,8,-9,-4,-3,6,5,2,-8,2], dtype = "uint16")#candidate|4799|(64,)|const|uint16
call_4798 = func_1770_call(relay.reshape(const_4799.astype('uint16'), [2, 2, 16]))
call_4800 = func_1770_call(relay.reshape(const_4799.astype('uint16'), [2, 2, 16]))
var_4815 = relay.var("var_4815", dtype = "uint16", shape = (2, 2, 16))#candidate|4815|(2, 2, 16)|var|uint16
bop_4816 = relay.greater(call_4798.astype('bool'), relay.reshape(var_4815.astype('bool'), relay.shape_of(call_4798))) # shape=(2, 2, 16)
bop_4819 = relay.greater(call_4800.astype('bool'), relay.reshape(var_4815.astype('bool'), relay.shape_of(call_4800))) # shape=(2, 2, 16)
bop_4820 = relay.less(call_4794.astype('bool'), const_4799.astype('bool')) # shape=(5, 8, 64)
bop_4823 = relay.less(call_4795.astype('bool'), const_4799.astype('bool')) # shape=(5, 8, 64)
func_2977_call = mod.get_global_var('func_2977')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_4837 = relay.TupleGetItem(func_2977_call(relay.reshape(call_4798.astype('uint16'), [2, 32])), 0)
call_4838 = relay.TupleGetItem(func_2980_call(relay.reshape(call_4798.astype('uint16'), [2, 32])), 0)
func_4789_call = mod.get_global_var('func_4789')
func_4790_call = mutated_mod.get_global_var('func_4790')
call_4848 = relay.TupleGetItem(func_4789_call(), 0)
call_4849 = relay.TupleGetItem(func_4790_call(), 0)
bop_4856 = relay.logical_and(call_4794.astype('bool'), const_4799.astype('bool')) # shape=(5, 8, 64)
bop_4859 = relay.logical_and(call_4795.astype('bool'), const_4799.astype('bool')) # shape=(5, 8, 64)
func_2847_call = mod.get_global_var('func_2847')
func_2848_call = mutated_mod.get_global_var('func_2848')
call_4860 = relay.TupleGetItem(func_2847_call(), 0)
call_4861 = relay.TupleGetItem(func_2848_call(), 0)
uop_4863 = relay.cos(bop_4820.astype('float64')) # shape=(5, 8, 64)
uop_4865 = relay.cos(bop_4823.astype('float64')) # shape=(5, 8, 64)
output = relay.Tuple([bop_4816,call_4837,call_4848,bop_4856,call_4860,uop_4863,])
output2 = relay.Tuple([bop_4819,call_4838,call_4849,bop_4859,call_4861,uop_4865,])
func_4879 = relay.Function([var_4815,], output)
mod['func_4879'] = func_4879
mod = relay.transform.InferType()(mod)
mutated_mod['func_4879'] = func_4879
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4880 = relay.var("var_4880", dtype = "uint16", shape = (2, 2, 16))#candidate|4880|(2, 2, 16)|var|uint16
func_4879_call = mutated_mod.get_global_var('func_4879')
call_4881 = func_4879_call(var_4880)
output = call_4881
func_4882 = relay.Function([var_4880], output)
mutated_mod['func_4882'] = func_4882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_4889 = relay.TupleGetItem(func_3183_call(), 0)
call_4890 = relay.TupleGetItem(func_3184_call(), 0)
func_3982_call = mod.get_global_var('func_3982')
func_3987_call = mutated_mod.get_global_var('func_3987')
var_4895 = relay.var("var_4895", dtype = "int8", shape = (1056,))#candidate|4895|(1056,)|var|int8
const_4896 = relay.const([-6.651793,-6.180905,-1.032860,3.647087,0.815513,7.830614,2.034225,3.891389,9.732825,-3.788261,6.480836,-5.815593,-2.832117,8.391898,6.331912,-8.338704,8.933234,-5.167047,-1.803418,7.108801,4.371647,8.418295,9.001546,8.487896,-5.093493,5.935064,9.968782,7.523651,9.605798,-7.045331,3.502150,-8.697934,2.215475,-5.837915,-5.434215,-2.839197,7.838242,-2.084422,-1.973700,5.999964,-9.451626,4.067541,-0.157901,7.337394,3.115288,-8.983559,-5.827312,-2.361972,8.394677,-0.287981,-8.880822,-4.170734,-0.831247,-6.757677,-6.359009,1.025441,6.354796,6.518927,2.574914,9.984123,-1.130420,2.422137,7.429643,-6.859160,3.757545,-8.061829,2.779613,7.727275,-7.822495,7.031083,3.713422,3.942016,1.271374,-8.667391,6.238029,0.746617,5.491318,7.927276,-6.032777,3.088157,-8.452463,7.267133,-4.590482,4.744722,9.229560,-4.082835,4.314523,5.235727,-3.257808,1.238553,0.086653,8.622937,5.489570,7.303311,-3.811558,2.741541,2.955319,1.486214,7.964379,-2.751406,4.239449,1.267303,-1.282939,9.026076,-8.397223,-8.116291,7.065382,-7.701549,-6.368650,2.909227,4.126692,8.884274,2.557253,-8.406082,6.296473,7.671394,1.906890,2.509837,1.004450,-6.241911,1.553466,-4.909905,-4.621028,-9.790401,-9.679279,-0.453417,-9.857538,-5.385265,-8.315706,3.095648,4.772486,-8.498227,8.021877,-4.746538,-1.170708,8.629419,-3.755929,-2.237285,-7.859303,7.883096,-2.185063,-5.433190,-7.934075,1.976769,-0.250063,-9.044027,7.625990,-1.858757,5.333220,-0.611177,-7.424481,8.504169,3.913229,0.272043,-0.124757,-9.349928,-9.560516,-6.986310,-8.263158,6.513354,-9.260931,-9.530719,-3.713969,-0.275390,-5.084368,5.563746,-9.711741,3.739319,5.859879,-7.557324,1.197456,-6.173577,8.177943,-7.916762,-0.034537,-3.156604,-1.893668,8.248966,-0.078643,-8.428480,-3.717215,3.775089,-8.792740,-5.600916,1.883120,-8.831691,0.695057,3.661944,3.339200,-4.453606,9.465434,-2.303394,-7.372918,6.304616,6.443977,2.714902,4.875874,7.160854,3.658997,7.107126,-6.974283,9.251181,0.140779,-0.389569,5.930823,-7.306441,-7.130722,-5.385449,-0.973229,9.650232,8.841335,1.022357,1.332329,-3.491951,-1.612465,6.261184,1.683549,8.247024,6.799122,4.088712,-6.381628,-6.906598,-1.094252,8.488640,-4.413440,7.935596,1.653519,-4.011012,7.382388,2.079019,9.284762,-9.825060,-3.257656,0.134396,2.632704,-9.466556,-1.051593,-8.552308,9.869636,-2.843027,-8.489409,0.322749,-6.694429,-2.144020,-5.481164,-9.092453,6.088204,9.415095,-3.698625,3.091348,1.316886,4.311900,-9.652630,8.749108,-8.885779,8.428952,8.765428,-6.844047,0.764482,1.520125,3.571188,4.333565,-7.345807,-7.220123,3.107288,-6.947715,0.028765,-0.790202,-1.209497,1.886567,7.695095,2.132006,7.628111,3.775514,7.634368,-2.453238,-1.382916,3.072361,-5.816274,9.877968,4.680214,1.037901,7.771287,9.695572,3.962140,-8.605656,6.773111,8.322604,-8.329858,6.380451,8.558947,-6.512416,8.782852,-7.476351,9.390800,4.956088,9.632836,0.025322,3.457784,-0.484034,9.350905,8.159824,3.756130,8.199100,3.319266,1.282065,-1.044471,-4.420882,5.055517,-1.650323,-7.220115,3.597520,-2.289029,3.496560,7.825483,-3.957443,-6.169105,-6.500133,-4.870499,9.649462,-9.461282,-3.177274,-9.650095,0.902679,4.012590,-0.941839,4.406169,8.248634,-9.000089,4.264618,1.649363,-8.721733,-7.178470,8.423121,-1.126139,-4.326363,2.677964,-8.151851,-8.972946,8.772831,3.783041,5.792638,4.090349,-4.161611,4.013082,-0.013279,0.421198,4.522416,6.590482,-6.907328,1.898578,-9.202049,8.077033,2.034184,-7.811968,1.338488,-6.278780,4.074563,6.910552,-0.506990,3.119084,8.215364,5.492475,-1.611385,4.348057,5.729458,-9.504641,3.387909,-0.138049,9.298764,9.354206,-6.067525,6.724979,-0.592063,4.385317,-1.021698,1.665894,9.904314,-0.829427,6.872200,-6.961255,-9.411098,-2.178873,-3.120801,-3.354545,-8.691298,-2.378860,-1.353304,-5.118840,-8.131927,3.446187,-2.908501,7.875715,1.702018,-0.265472,6.413025,9.152360,2.771169,-4.615967,-9.925353,6.216740,-8.963280,6.847595,6.958999,3.477376,7.848246,-9.462671,6.116638,6.037483,6.724447,5.520385,-2.604262,0.399436,4.550757,4.301023,-6.301200,-3.743740,-0.549966,1.946010,1.279679,-1.042842,6.614751,-1.604274,-8.477337,-2.533147,6.537340,-2.940018,-6.366927,3.323291,7.470485,-1.238689,7.388152,3.310364,-0.643993,-2.814067,4.080203,7.714530,1.965131,-7.991963,9.038895,-2.217657,-8.026272,4.911836,-5.844798,-9.703676,7.663650,5.992774,2.219732,0.325621,-2.648998,7.555798,-7.118523,-3.922550,4.262479,6.765901,2.301910,1.691095,-7.808046,2.673489,-3.507887,4.826860,-5.000163,-8.949779,6.944421,1.870975,6.478392,7.524757,7.965828,-1.684085,-3.304403,-4.552913,8.943268,-7.595258,-4.207588,-3.458149,9.515796,-8.877746,-4.338011,-0.761383,-4.313791,5.239078,-3.410944,5.331286,6.533140,-3.881703,3.236465,9.879276,9.073447,3.556110,9.596916,-3.310506,3.355311,-4.981278,6.274661,9.202357,9.498185,-7.531131,1.031828,5.187183,2.518493,2.617629,-1.036495,2.390852,-5.387568,5.765386,-0.087499,-0.685456,5.606741,8.361933,1.080811,-2.933278,-4.260687,8.350169,0.432399,-2.001315,-4.294657,8.262617,-1.477076,-5.729498,5.295508,7.039949,8.680732,0.688946,-3.160512,-2.392080,7.189840,-1.466729,5.704383,-8.934926,7.037744,8.860358,-9.591514,-0.539560,3.349953,3.392316,5.536444,-8.331423,-3.543223,4.256345,-8.078128,0.118414,-2.980750,3.777416,1.468511,-3.177558,-5.240194,-1.972871,3.631419,-1.706913,-8.219466,2.555310,-7.011157,-0.339098,-2.429868,8.676343,6.127196,-9.221353,9.587174,7.688878,7.383576,4.712011,8.987177,-4.265860,-4.463292,4.030644,-5.457966,-9.300986,-2.755826,-6.363044,-1.219968,-4.917970,-6.261903,-1.543919,-8.779152,-4.517668,1.421174,-3.891510,6.626007,0.408373,0.608075,-7.204295,-7.735411,-4.398776,-8.449296,4.367587,-4.918958,-7.310126,-6.942119,-0.979977,5.777606,3.582331,-1.210453,1.299302,-9.539343,-3.268465,-2.896249,-2.076962,2.044297,6.079644,0.216014,9.992274,-1.513927,-7.167022,-9.452237,-7.800138,9.684320,-8.114892,2.498646,1.445704,8.316384,5.761496,0.944937,-6.963402,-7.797721,-4.567811,-5.503571,7.433991,8.441386,8.691944,1.230078,8.145898,3.432007,-7.589156,-3.472937,6.347289,2.229807,0.292350,-4.546364,-2.679491,1.624717,-3.662769,-1.712690,0.463447,6.896140,2.500525,-8.444369,4.904103,-7.918659,-8.106457,8.456320,-5.112403,-7.210720,6.875775,3.859378,3.999613,-7.136354,-5.589899,1.945222,1.526423,2.084097,7.873090,1.179403,5.918436,8.357535,-5.949634,3.182034,0.363644,-0.645911,-8.409872,-9.359111], dtype = "float64")#candidate|4896|(660,)|const|float64
const_4897 = relay.const([7.995706,8.723352,9.891878,6.361547,-6.006028,0.783995,5.720748,9.930565,-9.915215,-2.001947,-9.297415,-3.472376,4.412478,-8.680677,-8.273505,-6.187180,-5.783958,-4.098070,-1.085053,4.455933,-7.022089,8.608815,6.648102,-2.602012,1.847879,9.678804,1.189398,2.739078,5.280037,2.124192,7.738427,7.397226,4.152970,-2.888346,-8.692012,-1.412116,-0.263440,-3.118127,-2.686325,8.822410,1.279719,0.464117,9.665056,4.062880,-8.116833,-3.574818,2.303371,-6.214200,0.390612,-1.545444,-4.829335,-7.961022,-4.138820,-0.918590,0.217844,7.278158,-9.316672,-9.943137,7.602779,-2.991876,-8.935910,6.032447,5.041251,2.907218,-6.224188,-7.766550,-0.593089,-0.615927,5.348402,-2.266501,-3.175454,2.999848,-4.342660,-8.721558,-4.178936,-8.353524,8.140036,-5.061606,0.391047,0.604883,5.135150,-8.321540,9.439955,5.261942,3.307848,3.330940,3.070500,-6.859610,-8.791292,6.791503,-7.443684,-9.086578,6.739149,-9.816727,-8.399311,4.266480,2.641470,7.924187,-9.955282,1.541163,-3.060606,3.286482,9.195337,-1.318669,3.535272,-3.362168,1.139678,2.630041,8.664215,9.653334,-1.070372,-9.502659,-1.137117,-7.685499,-6.866558,-5.255625,-0.076727,-2.921255,8.749211,-3.178650,-8.347336,-7.299106,2.690594,-0.048409,3.575456,-9.457634,-0.396691,4.080178,-4.911085,4.685264,0.147847,-9.013696,-8.469083,-4.218218,8.275431,-9.291134,6.344592,1.777157,-3.064516,-6.191148,0.913537,4.916593,7.300851,-1.403177,-6.915812,-3.591558,4.929321,-6.765247,5.990856,0.891422,5.171821,-6.678704,4.098350,6.295038,2.877376,8.731413,-5.188564,1.596797,-0.559539,9.988095], dtype = "float64")#candidate|4897|(160,)|const|float64
call_4894 = relay.TupleGetItem(func_3982_call(relay.reshape(var_4895.astype('int8'), [1056,]), relay.reshape(const_4896.astype('float64'), [660,]), relay.reshape(const_4897.astype('float64'), [16, 10]), ), 6)
call_4898 = relay.TupleGetItem(func_3987_call(relay.reshape(var_4895.astype('int8'), [1056,]), relay.reshape(const_4896.astype('float64'), [660,]), relay.reshape(const_4897.astype('float64'), [16, 10]), ), 6)
func_4879_call = mod.get_global_var('func_4879')
func_4882_call = mutated_mod.get_global_var('func_4882')
var_4916 = relay.var("var_4916", dtype = "uint16", shape = (64,))#candidate|4916|(64,)|var|uint16
call_4915 = relay.TupleGetItem(func_4879_call(relay.reshape(var_4916.astype('uint16'), [2, 2, 16])), 2)
call_4917 = relay.TupleGetItem(func_4882_call(relay.reshape(var_4916.astype('uint16'), [2, 2, 16])), 2)
func_3343_call = mod.get_global_var('func_3343')
func_3346_call = mutated_mod.get_global_var('func_3346')
var_4925 = relay.var("var_4925", dtype = "float32", shape = (1014,))#candidate|4925|(1014,)|var|float32
call_4924 = relay.TupleGetItem(func_3343_call(relay.reshape(var_4925.astype('float32'), [6, 13, 13])), 0)
call_4926 = relay.TupleGetItem(func_3346_call(relay.reshape(var_4925.astype('float32'), [6, 13, 13])), 0)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_4927 = relay.TupleGetItem(func_3396_call(), 0)
call_4928 = relay.TupleGetItem(func_3398_call(), 0)
bop_4930 = relay.greater_equal(call_4915.astype('bool'), var_4916.astype('bool')) # shape=(5, 8, 64)
bop_4933 = relay.greater_equal(call_4917.astype('bool'), var_4916.astype('bool')) # shape=(5, 8, 64)
output = relay.Tuple([call_4889,call_4894,var_4895,const_4896,const_4897,call_4924,var_4925,call_4927,bop_4930,])
output2 = relay.Tuple([call_4890,call_4898,var_4895,const_4896,const_4897,call_4926,var_4925,call_4928,bop_4933,])
func_4938 = relay.Function([var_4895,var_4916,var_4925,], output)
mod['func_4938'] = func_4938
mod = relay.transform.InferType()(mod)
var_4939 = relay.var("var_4939", dtype = "int8", shape = (1056,))#candidate|4939|(1056,)|var|int8
var_4940 = relay.var("var_4940", dtype = "uint16", shape = (64,))#candidate|4940|(64,)|var|uint16
var_4941 = relay.var("var_4941", dtype = "float32", shape = (1014,))#candidate|4941|(1014,)|var|float32
output = func_4938(var_4939,var_4940,var_4941,)
func_4942 = relay.Function([var_4939,var_4940,var_4941,], output)
mutated_mod['func_4942'] = func_4942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2728_call = mod.get_global_var('func_2728')
func_2730_call = mutated_mod.get_global_var('func_2730')
call_4974 = func_2728_call()
call_4975 = func_2728_call()
func_4938_call = mod.get_global_var('func_4938')
func_4942_call = mutated_mod.get_global_var('func_4942')
const_4977 = relay.const([-1,-6,-2,2,10,-5,4,1,3,-6,-10,4,3,4,-2,3,-1,6,-1,3,2,2,9,8,9,-1,-7,9,-5,-5,9,2,-1,3,7,-3,4,-5,-7,5,6,-9,2,-2,-10,-6,5,8,6,-7,-7,-4,-6,-4,-1,-2,-6,8,8,7,-7,10,-10,-7,2,-3,-4,10,5,6,-4,1,-9,9,8,-9,8,-6,-10,7,9,-10,7,5,-5,-6,-9,-8,7,-8,-1,2,6,10,-3,7,6,-4,-9,-5,-2,-1,9,9,-7,2,6,1,-2,-10,-7,6,6,6,-3,-8,-1,5,-2,-5,1,-1,9,-1,-1,7,-7,1,7,9,-8,4,-9,1,-3,-2,-4,-1,3,6,-2,3,-10,-5,4,6,2,-3,-8,4,-1,-4,-9,9,-9,-7,-10,10,-7,-8,10,2,3,-5,-10,-10,7,-7,3,10,3,-2,-10,-4,1,7,-5,3,4,10,-1,6,-6,-6,-1,10,-8,6,9,6,-1,1,-9,5,-4,-7,5,5,-10,-10,-9,-6,7,4,3,7,-10,1,5,-3,1,4,-7,7,9,-2,-10,-5,10,4,-9,9,-9,9,6,-3,-5,-1,7,2,5,-4,2,-1,-9,8,-6,-7,5,9,9,-6,-8,-9,-7,10,-6,-7,6,-1,-3,-4,5,-5,9,-2,3,-5,7,5,6,5,4,8,-2,-6,9,-5,1,-5,-2,-9,6,-8,-7,-8,10,4,-5,-3,-3,-1,9,5,6,10,-4,4,2,-5,-5,-1,6,7,8,-10,9,1,9,-7,5,-4,-6,-1,2,-7,-6,-2,-6,6,10,-4,7,-8,1,-3,5,-7,8,1,-1,7,-9,-2,9,-8,3,-2,9,-7,7,9,7,-5,2,-7,6,-4,4,-1,-5,-5,-3,9,5,2,-5,-6,-7,-7,8,-5,9,-9,-7,-9,-1,1,9,6,7,8,3,4,6,10,-7,-6,4,1,-10,-4,-3,5,-6,-8,2,-2,-9,-4,10,-6,-9,-5,-2,4,7,2,-2,3,-9,10,-6,-6,-1,-9,4,-1,-2,6,3,5,-8,3,6,-10,7,-8,-4,-10,-7,-9,-8,4,7,5,1,-1,9,-1,-1,9,2,-3,-4,-5,-5,1,-5,5,-6,3,2,-6,-9,5,-9,8,-4,2,-7,8,-3,7,-6,1,5,-9,7,8,-6,4,9,-9,-4,-2,9,-2,1,-10,4,-8,5,-5,-5,-6,8,-6,-3,-4,9,-9,6,-1,-1,-3,-4,3,8,-2,1,-4,2,-7,-7,4,-7,-4,-2,-1,8,9,2,-3,-10,-3,-5,-9,9,9,-9,3,6,10,-2,3,4,4,-4,8,10,-4,-10,-9,2,-6,3,-8,5,-8,-8,9,-5,-8,7,-4,9,3,2,10,-2,-7,-6,-5,-1,-9,6,-1,-10,1,-6,6,4,7,-1,-1,3,-9,3,1,-7,-4,-8,-5,5,8,10,9,3,-1,2,7,-10,-6,10,-6,8,1,5,6,1,-1,8,-6,-5,5,-9,-5,-1,-9,-8,10,-4,-2,7,9,2,1,-2,-2,2,-6,-2,-9,4,5,-4,8,6,-9,9,-10,-1,-2,-6,10,2,10,-7,-8,-8,2,8,3,3,-4,1,-5,5,-3,-4,10,1,1,-10,10,3,-3,4,-2,8,-1,-10,-1,-6,5,-9,5,6,7,-6,-5,1,-10,3,-1,-6,10,-1,-10,-5,-8,-1,-4,10,4,-10,-6,8,-3,-6,4,1,1,-6,10,7,6,10,6,3,7,-10,2,1,-10,4,-10,-7,6,1,7,-3,-7,-4,2,-4,1,-3,3,-2,10,7,10,10,-9,3,2,-8,-8,3,-10,-6,4,-7,3,10,-5,3,2,5,-8,-9,4,-1,-2,10,-5,4,-8,-4,10,4,2,-3,3,-10,-6,-1,-6,1,-7,1,-1,-9,8,10,1,3,1,10,4,5,8,-8,-8,-4,4,-7,2,4,3,-8,-9,-10,9,-6,-1,-2,-7,-5,1,-10,-7,-2,4,9,-1,2,9,10,-1,8,-7,10,1,7,-7,1,-5,-2,-6,-6,7,-6,-9,2,-3,3,3,4,-1,9,9,3,-10,2,-6,-4,-6,9,9,7,-6,-3,-6,-4,-1,6,-3,-5,1,-3,-6,10,-9,9,-2,1,-9,-6,5,-1,-3,8,5,10,-1,-3,-10,-10,5,9,8,-5,8,1,3,2,10,-3,3,10,-6,2,-7,-7,4,10,-7,10,-8,9,-4,9,-10,6,8,7,9,10,-4,10,4,-9,-7,-6,-1,-8,7,6,2,9,7,1,-7,-4,1,-6,-6,-6,5,9,9,10,5,-1,7,-4,-8,-4,10,-6,4,4,1,2,-3,2,6,-6,-8,-7,-9,-3,8,3,-5,-8,3,8,3,-9,-1,-6,5,-2,-9,9,-2,6,-10,-9,-8,-6,1,4,-8,-10,-6,-7,-10,-5,8,10,8,1,5,-5,-8,-7,-8,5,-5,-4,3,1,10,6,-10,9,2,-8,-1,1,7,-10,-8,1,-10,-4,6,-10,-1,-6,5,-1,-9,-6,-3,2,7,-2,-9,-8,-10,5,8,-4,-4,-2,-8,-5,-1,9,-8,-1,-5,9,8,2,-2,3,2,8,10,2,4,-6,10,8,-6,-2,4,2,1,-1,1,-2,3,-9,-2,10,-10,-1,-2,8,-6,9,-2,-3,7,5,-7,-10,-6,3,10,4,-2,10,-1,-3,9,-8,-5,5,4,1,-6,2,-2,2,8,3,10,-5,-4,-2,10,-5,3,-6,-1,-10,10], dtype = "int8")#candidate|4977|(1056,)|const|int8
const_4978 = relay.const([0.572231,5.524350,-1.110671,9.355760,1.180134,4.423851,-1.786492,0.444428,6.685202,-1.122535,-7.462640,-7.580102,2.131854,6.166342,-7.508510,8.390010,7.376273,7.814739,7.244313,7.576134,9.061607,1.970890,2.018262,-6.906444,-1.508263,-5.042160,8.616285,5.906323,-2.742798,3.078350,9.868815,-1.129303,7.179084,-3.421024,8.528173,-0.367817,-2.352720,-9.415234,-4.061259,4.033413,4.228833,-6.132611,-5.510884,3.254621,-9.344270,4.765367,-1.824277,7.438736,-8.972026,-8.549711,3.962525,-4.612073,-3.877294,-1.468852,4.403328,-6.924274,9.187635,-7.319273,-0.547124,-1.793885,-8.693951,-6.561819,-6.713719,3.189770,3.059343,-4.556030,-8.434598,1.807762,5.308702,8.092214,0.713857,-2.896502,-8.747464,-2.669758,-5.467390,-4.884417,3.721707,8.862670,-3.323040,-2.528427,1.277338,-7.251426,9.428762,-8.532074,8.686955,2.947674,3.802121,-8.129652,-0.254925,-9.245652,8.462251,-8.224860,5.227496,-2.835451,-8.616008,-5.337553,7.462204,0.388513,-4.131305,-1.410643,2.564262,-7.944901,2.539071,2.993557,7.285703,-8.983149,-1.920710,6.314497,2.943011,1.788204,-6.263074,6.425692,-2.789284,-7.340913,-0.356489,4.907109,3.218320,4.897844,-4.322652,-6.274070,-3.611671,-7.924930,8.780180,6.858412,-8.653976,-3.603216,-3.960070,-3.611326,-7.693128,7.394406,1.166778,6.770870,-3.556041,3.298940,7.491210,-6.968435,3.676227,-2.549259,4.377670,2.529104,-7.893490,-2.889649,9.862854,1.017402,-5.764739,-9.985829,4.293208,-7.388602,-1.260809,-5.574697,7.761302,-5.148697,-1.324042,-0.452596,-5.480588,3.180229,9.992266,4.773609,-2.844227,3.449399,3.170292,0.016385,9.041611,-9.587915,0.241368,4.055350,9.510021,4.813867,-8.317793,4.829262,8.340826,8.710196,3.541058,1.835735,3.920050,-7.614628,2.128835,-7.809596,0.681671,-7.266556,3.275821,1.434663,5.980377,-4.604502,-6.593557,-2.834679,-0.285522,8.093603,-7.839934,-2.944166,8.743085,-7.065848,-8.533648,0.321067,6.088715,-9.113173,3.918924,-0.031351,6.471630,-0.204773,-3.739810,7.329091,-9.953764,-3.323229,-9.293227,-4.440276,7.959519,-5.992808,5.946965,6.399212,5.042349,-7.674817,-3.509441,-1.585100,6.241141,6.373163,8.479960,7.409829,0.898042,7.173836,-6.969731,3.857746,-4.876414,6.330561,4.663148,1.141385,-8.381534,8.921192,-2.431026,-3.415045,-4.172536,8.328619,3.741532,0.445239,5.718418,-4.873734,3.339096,4.162895,6.018499,9.490263,-3.990813,6.311833,-1.290554,1.070216,-7.222176,8.194887,3.935431,6.479885,1.775821,-9.170993,0.044416,-7.814021,-0.225205,-1.518896,-5.136539,2.748132,-0.452789,3.773110,1.171255,7.992105,0.337991,5.441132,-8.708216,4.052104,7.005128,-0.436676,-5.412028,6.539111,-6.808120,-5.792451,-7.599228,8.231085,-3.224458,3.803835,3.651199,-0.311388,8.528507,-4.424456,-3.115723,6.828859,5.136356,-9.763021,-8.481187,-9.323913,8.915957,2.401259,-8.367235,8.647280,-6.927480,6.404601,0.342940,-4.527916,8.441936,-8.892333,-0.212130,3.968658,6.067214,7.177632,-9.312912,4.838874,-8.728073,6.990920,0.610766,5.471905,5.011667,-2.342217,-3.850900,-9.324527,8.534378,9.916038,-1.683577,2.076522,-2.573178,-2.995615,-0.496549,7.263551,-7.589402,-9.345757,9.667477,9.446266,-4.888862,6.112963,-8.209775,-3.090911,1.499507,5.468405,-8.105140,7.040416,8.847912,1.301870,8.948541,-0.948647,4.404700,-3.466654,0.773987,-5.841488,4.245163,-7.570372,6.207304,8.793364,3.919994,-1.972228,4.375306,-1.380089,1.101455,-3.845642,-3.588858,2.660540,7.795866,-3.291278,2.052228,-6.570244,5.745867,9.724309,4.855937,4.863805,6.141231,0.017383,0.161975,-0.470277,7.143897,-5.944115,7.094490,-8.715239,6.966194,3.442757,4.013569,4.172495,9.863840,2.169094,4.401833,7.249094,-8.261346,5.879724,-1.482364,7.438728,-3.003017,-8.699506,8.050718,9.397341,1.623833,7.882611,-7.595217,8.800761,2.230548,3.395362,1.835481,-0.153868,2.621408,-8.135994,8.110240,9.702907,3.669043,2.550786,-7.847416,3.279979,-5.895815,-3.217543,2.475559,-4.773658,-5.782582,7.379980,-3.530772,-5.590260,3.844177,7.397209,-1.737654,-0.985077,-4.193945,-4.215579,-8.956979,8.935080,-5.172438,-7.516724,3.265875,0.167281,-1.091068,-3.495473,-7.068647,-8.495865,6.728114,-9.457257,-7.081685,0.404736,-3.755883,-6.411393,9.771795,7.435166,4.118322,4.571155,-2.160107,8.511381,0.736920,5.326327,-9.104714,2.049613,-3.182903,4.468684,-9.484739,8.135746,-4.123285,-7.858346,3.022093,2.918558,3.709522,-4.363789,8.917332,-4.785954,9.783997,-7.435894,0.038749,1.869430,6.049283,-6.467913,3.753652,3.693052,1.259910,3.868911,7.899677,-9.122155,1.758809,4.239967,-1.173865,9.455722,9.984596,2.968232,8.807002,-2.878728,5.269802,-3.044905,7.484635,-9.932996,5.679007,4.119538,-3.358843,2.666137,-0.282264,2.268112,-6.314357,-7.818394,-3.471360,-0.575676,-4.326979,2.225088,-1.574170,-7.804571,5.402135,-4.798870,-4.904000,3.963376,0.788108,-6.016300,6.869045,-5.528976,-1.831877,-7.407636,-8.373610,-0.807745,9.222434,-7.469386,-4.964658,6.109242,2.552560,-1.410390,-8.207082,6.756243,5.535372,9.132948,7.519648,-8.850840,2.900911,-3.736548,-2.766382,-5.670175,-3.314489,5.963774,-0.999987,-6.929950,-4.627810,9.856352,1.778558,0.736851,3.908549,4.048344,-8.981514,-4.428942,-9.030000,-2.687919,-0.644556,1.321566,5.222963,2.790609,2.776263,-8.094970,-3.253549,-9.378752,-3.100217,-3.405141,0.815810,-8.352975,-9.067390,1.837666,6.990123,1.521945,-0.035244,2.243340,1.284067,0.264140,-1.641755,-3.880802,-2.228684,-1.401772,-8.955220,-8.000115,2.617889,-9.099236,6.130316,-5.642593,4.109694,-8.517068,-0.754142,3.423552,-6.019169,9.556682,-6.566038,-3.393766,-5.684239,7.472711,2.877634,-9.761240,-3.700739,-3.302742,-2.810773,4.758911,-6.867385,-6.983952,8.069405,-0.367061,-3.435475,-6.337561,-3.367156,9.606463,-2.268915,9.544906,-3.869633,-6.199786,-2.204896,6.404065,4.473607,-9.923325,-9.084124,8.816310,9.617647,-6.138685,2.198685,-4.532823,5.807271,-5.621139,9.412773,0.613982,-6.022494,-0.093540,5.294571,0.455140,-1.376245,-6.367540,-1.581233,-5.642011,-5.852444,-0.637060,-3.528791,3.142777,-6.943278,6.390445,9.444398,-4.352816,-5.702963,1.172746,-4.056571,-3.918018,-6.477530,9.171789,-8.510392,-0.796265,-8.179669,-8.338273,-5.609470,-5.632012,-4.847919,-9.617594,9.181491,2.717021,7.873957,1.719069,1.440836,0.652473,-6.031323,2.213559,-0.254214,2.101057,-1.506253,1.052192,3.054422,7.271602,2.446643,-2.958294,-7.604463,-5.730934,-9.840669,9.823845,-6.438527,7.426381,-1.624865,8.357797,8.657972,0.949328,0.821678,-9.099186,0.719345,-6.646904,2.329293,3.868631,-0.086598,2.319001,3.955321,-1.337540,1.886306,-7.321432,-0.467557,4.786571,0.849618,4.711091,5.743896,8.226730,-4.465920,-1.649545,-8.657049,3.829048,1.955375,3.464161,-7.603617,-5.405943,-4.757326,2.737227,0.837725,-8.179078,5.110903,4.590925,8.544339,1.072138,-1.885367,7.222084,2.995194,0.967716,1.236923,6.538132,-5.818979,-1.727859,3.335165,-5.830897,-0.413875,3.795437,-6.900786,-6.624591,0.832442,6.919234,1.116413,7.057477,-2.990129,-0.628148,2.064118,8.290725,6.311306,-1.496189,7.846031,4.265293,4.536694,6.445320,0.293544,5.589601,-8.541992,-0.201917,6.502726,-5.380919,-2.564649,-5.711995,3.413846,-6.887638,0.730702,2.236883,3.990755,-8.662343,1.475158,-2.843580,4.879705,8.186387,9.792216,-1.949983,6.948576,-7.078068,4.081337,-8.581188,-7.461325,0.914562,9.250015,-4.488283,-2.162309,-7.531380,-8.834540,-1.780287,-2.624190,1.027397,-5.309192,1.569303,6.327496,0.632418,-3.697139,1.308470,-2.200105,-1.027201,9.438855,-2.486504,4.469427,0.652536,-9.954590,3.706964,1.428856,-9.055494,-6.964193,-2.663206,5.044867,-5.125078,5.127727,-1.659080,7.109057,5.160250,6.876063,-3.791286,-0.299681,-9.571102,5.813833,-2.005101,2.797400,-3.129358,-9.809418,7.246909,8.029729,6.978256,0.235475,-5.678314,-7.993120,2.017046,-0.212292,-2.034512,4.753018,7.821476,-3.185090,3.364060,-5.667331,-8.586528,-4.064379,-9.986354,7.713165,-9.205217,3.002149,1.699461,3.096383,8.359405,-3.398170,-7.751417,-8.847216,7.282854,8.043384,-3.269928,-6.647224,-5.538413,-1.470462,-5.595342,-6.397198,-5.830264,-5.640828,3.434235,-3.688206,3.536090,-2.188696,-9.911846,5.890625,-4.826687,8.342961,-8.807946,7.192658,-4.566833,2.269492,8.698979,-6.266604,7.190886,-9.518556,-5.494050,2.382092,2.098590,1.870700,-8.782615,9.231925,-5.653533,-9.683884,7.799501,7.206591,5.762425,-9.109278,2.147498,3.356051,4.653646,4.613199,-6.769336,8.417092,5.866280,-7.206439,9.546655,-1.177378,-3.486631,-4.775628,-1.008537,8.329048,-7.488116,-2.884964,-4.807631,-3.264121,0.647499,9.299076,-4.626350,-1.013953,-6.740363,-7.169810,-3.697208,6.524372,1.169158,-3.951099,9.743942,7.143054,-3.896777,7.076286,2.601009,-9.156228,-1.960296,0.538449,9.653178,-4.460298,-4.535053,2.510071,6.369784,7.786031,5.385826,-0.767874,9.188791,-7.554897,9.939309,3.197529,-7.181095,-1.698362,0.196808,0.767148,0.637713,-8.241223,-2.956304,-2.517875,-4.677434,-1.718971,-2.454944,6.021417,1.932711,5.122192,3.287770,0.750234,-4.064606,-3.647443,8.176929,-1.596762,7.711653,-3.032048,7.071587,5.605137,-7.505130,7.621891,-3.038613,8.046619,-5.645854,6.905104,0.796464,5.290704,-2.185808,5.136208,-3.673489,-1.931382,9.038340,0.083422,5.893899,-4.239030,4.743807,-0.271257,-0.190902,1.424413,-3.231842,1.294054,9.002984,-7.354308,-7.540205,-6.275134,2.997706,2.532107,2.208628,6.937367,4.896797,3.208486,0.598596,4.486731,1.482498,7.297737,0.469524,4.574488,8.120929,-5.471248,3.755045,-7.115649,0.867854,8.469482,5.431880,3.880184,5.769994,0.194077,4.636027,-3.414882,5.991679,-0.896330,-7.248627,4.189082,4.968342,-9.740382,-9.627953,-1.462816,-8.871829,7.068881,-8.689270,-0.554368,6.286297,1.055659,-8.745030,2.555253,2.723246,-1.813115,4.215353,9.490553,8.936919,9.900170,1.620841,2.334636,-7.832803,7.546997,-0.001210,-9.643993,7.965644,-7.241414,9.905052,6.681168,4.590890,9.692168,1.657944,-2.775946,-4.063551,8.590560,6.345709,5.663328,0.870066,-6.614755,-6.958677], dtype = "float32")#candidate|4978|(1014,)|const|float32
call_4976 = relay.TupleGetItem(func_4938_call(relay.reshape(const_4977.astype('int8'), [1056,]), relay.reshape(call_4974.astype('uint16'), [64,]), relay.reshape(const_4978.astype('float32'), [1014,]), ), 2)
call_4979 = relay.TupleGetItem(func_4942_call(relay.reshape(const_4977.astype('int8'), [1056,]), relay.reshape(call_4974.astype('uint16'), [64,]), relay.reshape(const_4978.astype('float32'), [1014,]), ), 2)
func_4694_call = mod.get_global_var('func_4694')
func_4695_call = mutated_mod.get_global_var('func_4695')
call_4980 = relay.TupleGetItem(func_4694_call(), 1)
call_4981 = relay.TupleGetItem(func_4695_call(), 1)
output = relay.Tuple([call_4974,call_4976,const_4977,const_4978,call_4980,])
output2 = relay.Tuple([call_4975,call_4979,const_4977,const_4978,call_4981,])
func_4997 = relay.Function([], output)
mod['func_4997'] = func_4997
mod = relay.transform.InferType()(mod)
output = func_4997()
func_4998 = relay.Function([], output)
mutated_mod['func_4998'] = func_4998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4789_call = mod.get_global_var('func_4789')
func_4790_call = mutated_mod.get_global_var('func_4790')
call_5078 = relay.TupleGetItem(func_4789_call(), 0)
call_5079 = relay.TupleGetItem(func_4790_call(), 0)
output = call_5078
output2 = call_5079
func_5098 = relay.Function([], output)
mod['func_5098'] = func_5098
mod = relay.transform.InferType()(mod)
output = func_5098()
func_5099 = relay.Function([], output)
mutated_mod['func_5099'] = func_5099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4573_call = mod.get_global_var('func_4573')
func_4574_call = mutated_mod.get_global_var('func_4574')
call_5134 = func_4573_call()
call_5135 = func_4573_call()
output = call_5134
output2 = call_5135
func_5136 = relay.Function([], output)
mod['func_5136'] = func_5136
mod = relay.transform.InferType()(mod)
mutated_mod['func_5136'] = func_5136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5136_call = mutated_mod.get_global_var('func_5136')
call_5137 = func_5136_call()
output = call_5137
func_5138 = relay.Function([], output)
mutated_mod['func_5138'] = func_5138
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5139 = relay.const([[[6.301755,-2.865311],[0.948974,-7.276042],[-5.428417,-7.194534],[6.635399,-0.076106],[1.209588,6.413894],[3.726628,-0.909357],[-4.003065,-5.355691],[-6.111795,2.293249],[4.112560,2.819931],[2.657560,-8.797339],[-0.952760,-5.552675],[8.199032,-4.376563]],[[-0.784305,5.693027],[1.776601,9.924528],[-0.635024,-0.424744],[7.539395,-1.780612],[8.778235,-4.282179],[8.366898,-9.341359],[5.062021,3.936171],[-1.627128,-7.768999],[8.560394,-3.182862],[3.418113,7.061291],[-5.165972,-6.570517],[4.001773,-7.815196]],[[-0.416951,3.888727],[4.866556,8.945747],[-0.258362,7.262438],[-6.881386,2.564656],[0.825071,-5.886064],[7.753044,-5.381054],[7.821389,-4.717660],[3.362234,-6.893813],[1.099115,6.149529],[4.051856,0.516910],[4.752021,-2.483301],[-8.798920,-4.904952]],[[-5.583998,-8.951644],[-7.952872,6.730286],[-7.529265,-9.852957],[-2.943115,6.494262],[3.729981,-8.544594],[-5.754859,-2.577922],[5.538014,8.161316],[7.169724,4.058501],[5.112392,1.390306],[3.965893,8.971218],[-9.336504,5.398813],[-0.906242,-3.551146]]], dtype = "float64")#candidate|5139|(4, 12, 2)|const|float64
uop_5140 = relay.erf(const_5139.astype('float64')) # shape=(4, 12, 2)
bop_5143 = relay.logical_xor(uop_5140.astype('uint32'), relay.reshape(const_5139.astype('uint32'), relay.shape_of(uop_5140))) # shape=(4, 12, 2)
output = relay.Tuple([bop_5143,])
output2 = relay.Tuple([bop_5143,])
func_5153 = relay.Function([], output)
mod['func_5153'] = func_5153
mod = relay.transform.InferType()(mod)
output = func_5153()
func_5154 = relay.Function([], output)
mutated_mod['func_5154'] = func_5154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5136_call = mod.get_global_var('func_5136')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_5192 = func_5136_call()
call_5193 = func_5136_call()
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_5197 = func_2781_call()
call_5198 = func_2781_call()
func_4730_call = mod.get_global_var('func_4730')
func_4731_call = mutated_mod.get_global_var('func_4731')
call_5203 = relay.TupleGetItem(func_4730_call(), 0)
call_5204 = relay.TupleGetItem(func_4731_call(), 0)
output = relay.Tuple([call_5192,call_5197,call_5203,])
output2 = relay.Tuple([call_5193,call_5198,call_5204,])
func_5205 = relay.Function([], output)
mod['func_5205'] = func_5205
mod = relay.transform.InferType()(mod)
mutated_mod['func_5205'] = func_5205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5205_call = mutated_mod.get_global_var('func_5205')
call_5206 = func_5205_call()
output = call_5206
func_5207 = relay.Function([], output)
mutated_mod['func_5207'] = func_5207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5153_call = mod.get_global_var('func_5153')
func_5154_call = mutated_mod.get_global_var('func_5154')
call_5230 = relay.TupleGetItem(func_5153_call(), 0)
call_5231 = relay.TupleGetItem(func_5154_call(), 0)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_5232 = relay.TupleGetItem(func_3396_call(), 0)
call_5233 = relay.TupleGetItem(func_3398_call(), 0)
func_4012_call = mod.get_global_var('func_4012')
func_4014_call = mutated_mod.get_global_var('func_4014')
call_5245 = relay.TupleGetItem(func_4012_call(), 0)
call_5246 = relay.TupleGetItem(func_4014_call(), 0)
output = relay.Tuple([call_5230,call_5232,call_5245,])
output2 = relay.Tuple([call_5231,call_5233,call_5246,])
func_5259 = relay.Function([], output)
mod['func_5259'] = func_5259
mod = relay.transform.InferType()(mod)
output = func_5259()
func_5260 = relay.Function([], output)
mutated_mod['func_5260'] = func_5260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5259_call = mod.get_global_var('func_5259')
func_5260_call = mutated_mod.get_global_var('func_5260')
call_5370 = relay.TupleGetItem(func_5259_call(), 1)
call_5371 = relay.TupleGetItem(func_5260_call(), 1)
output = call_5370
output2 = call_5371
func_5376 = relay.Function([], output)
mod['func_5376'] = func_5376
mod = relay.transform.InferType()(mod)
mutated_mod['func_5376'] = func_5376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5376_call = mutated_mod.get_global_var('func_5376')
call_5377 = func_5376_call()
output = call_5377
func_5378 = relay.Function([], output)
mutated_mod['func_5378'] = func_5378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4573_call = mod.get_global_var('func_4573')
func_4574_call = mutated_mod.get_global_var('func_4574')
call_5404 = func_4573_call()
call_5405 = func_4573_call()
output = relay.Tuple([call_5404,])
output2 = relay.Tuple([call_5405,])
func_5409 = relay.Function([], output)
mod['func_5409'] = func_5409
mod = relay.transform.InferType()(mod)
output = func_5409()
func_5410 = relay.Function([], output)
mutated_mod['func_5410'] = func_5410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_5431 = func_2781_call()
call_5432 = func_2781_call()
output = relay.Tuple([call_5431,])
output2 = relay.Tuple([call_5432,])
func_5445 = relay.Function([], output)
mod['func_5445'] = func_5445
mod = relay.transform.InferType()(mod)
output = func_5445()
func_5446 = relay.Function([], output)
mutated_mod['func_5446'] = func_5446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4669_call = mod.get_global_var('func_4669')
func_4670_call = mutated_mod.get_global_var('func_4670')
call_5474 = relay.TupleGetItem(func_4669_call(), 0)
call_5475 = relay.TupleGetItem(func_4670_call(), 0)
func_1619_call = mod.get_global_var('func_1619')
func_1621_call = mutated_mod.get_global_var('func_1621')
call_5481 = relay.TupleGetItem(func_1619_call(), 0)
call_5482 = relay.TupleGetItem(func_1621_call(), 0)
func_2564_call = mod.get_global_var('func_2564')
func_2567_call = mutated_mod.get_global_var('func_2567')
const_5484 = relay.const([2.453449,9.606429,3.226447,-2.468193,9.146889,-1.179783,0.034819,4.486693,7.716677,8.607576,-6.616481,4.420058,7.177966,-2.043480,5.096995,7.431969,5.651935,7.439953,-3.380691,-1.194661,-1.404692,-8.803133,2.887083,0.153112,1.830733,-2.741852,-2.244830,2.038224,-7.200560,2.278747,8.443967,-3.269843,3.605863,-5.836753,-0.062652,3.724685,7.929478,-6.964987,-3.253188,-1.104950,4.231209,0.261237,-0.511096,6.038281,8.566838,-1.541602,9.554463,8.872653,4.442625,-7.090119,-5.587975,-5.324473,9.942754,-7.294435,-1.488425,8.185579,-3.324987,1.142097,0.818050,3.660654,6.306071,-3.302893,-7.000922,3.374534,3.443986,1.718987,-5.711614,3.418357,3.065359,1.403959,-4.700128,5.676023,1.161916,-2.166345,1.916640,3.529597,7.187744,9.113304,-8.690588,8.175511,-1.704388,5.877259,-6.611648,-8.151047,0.918894,2.732496,-8.112267,-4.659584,-3.282611,9.695667,-7.211406,-9.764615,-9.788232,4.307214,1.159282,-5.312220,-6.419837,-7.681096,-2.393018,-5.699687,-0.585805,-7.604243,-4.814190,-9.820975,9.085667,-3.232835,3.712599,5.381334,-4.058343,-1.463443,-0.893955,6.246020,-4.866978,0.178801,-9.095387,-2.804900,-2.641115,0.084605,3.535871,1.987171,0.895160,-5.085344,-0.518164,-4.027637,0.030080,-6.227130,7.449881,-0.824238,3.626934,2.246982,5.915226,-8.037999,-2.044182,-3.678224,-2.383660,-8.247644,8.319912,-1.126518,-2.454575,-5.368869,1.066637,1.248481,-7.948408,-0.661201,-0.064880,7.019686,-5.194555,8.601582,9.953576,-9.750673,9.727690,-8.500716,-5.985463,-2.582263,0.980278,-1.591472,-9.843868,-3.619448,1.235428,-6.641419], dtype = "float64")#candidate|5484|(160,)|const|float64
call_5483 = relay.TupleGetItem(func_2564_call(relay.reshape(const_5484.astype('float64'), [80, 2])), 3)
call_5485 = relay.TupleGetItem(func_2567_call(relay.reshape(const_5484.astype('float64'), [80, 2])), 3)
output = relay.Tuple([call_5474,call_5481,call_5483,const_5484,])
output2 = relay.Tuple([call_5475,call_5482,call_5485,const_5484,])
func_5490 = relay.Function([], output)
mod['func_5490'] = func_5490
mod = relay.transform.InferType()(mod)
mutated_mod['func_5490'] = func_5490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5490_call = mutated_mod.get_global_var('func_5490')
call_5491 = func_5490_call()
output = call_5491
func_5492 = relay.Function([], output)
mutated_mod['func_5492'] = func_5492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3907_call = mod.get_global_var('func_3907')
func_3908_call = mutated_mod.get_global_var('func_3908')
call_5529 = func_3907_call()
call_5530 = func_3907_call()
output = relay.Tuple([call_5529,])
output2 = relay.Tuple([call_5530,])
func_5535 = relay.Function([], output)
mod['func_5535'] = func_5535
mod = relay.transform.InferType()(mod)
mutated_mod['func_5535'] = func_5535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5535_call = mutated_mod.get_global_var('func_5535')
call_5536 = func_5535_call()
output = call_5536
func_5537 = relay.Function([], output)
mutated_mod['func_5537'] = func_5537
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5558 = relay.const([[[1.588572,-0.470538,2.023789,-6.825038,-3.647397,-1.621049,3.636338,7.613526,9.652965,4.248365,0.521888,-4.650407,1.647614,0.238659,9.990173,4.103710],[-5.078182,4.127967,0.149307,9.695587,-1.760013,3.502901,2.077878,5.485461,9.117508,6.546042,0.067482,-4.412706,-5.431057,-7.199679,-6.164691,-6.426083],[8.286448,-4.943498,5.632494,5.592852,0.192270,2.151408,8.955720,-2.899485,6.210847,0.373587,2.589485,-2.212369,6.992120,-7.532534,-9.932739,-7.859399],[-0.343184,-6.628942,4.607520,5.009412,-4.264508,1.234768,7.382009,-5.208956,2.366114,8.649540,3.014561,0.319048,2.991969,-3.867135,-4.599841,4.524810],[-4.597657,0.649832,7.735142,-0.494676,8.291759,7.059188,3.290800,-5.967445,6.793510,-4.067212,1.371432,-5.765469,9.738307,-8.704580,8.585905,-9.500496],[8.635229,6.669935,-1.360253,3.331463,7.620022,-1.337362,-8.195608,-6.207899,5.018404,3.104249,-3.313787,3.365338,-8.275172,5.636296,9.261467,1.568727],[6.552108,-1.940410,3.807584,-1.644199,-2.645599,8.256772,6.685038,0.073936,-7.088332,2.307521,-7.829286,-0.622397,-6.645830,-4.353608,4.636393,-0.499322],[2.644977,-2.049134,-9.026093,7.252407,-0.317547,-0.592737,-6.854457,-7.361138,-8.065298,9.536034,-9.190874,2.709110,-9.817081,-2.303315,-0.962272,-4.596744],[2.471566,-9.473986,4.858854,0.902290,-0.872133,5.933074,6.098142,-9.920424,9.340666,-5.915333,1.141143,-1.166091,9.931575,-7.275245,-0.682294,6.661531],[3.302683,7.104022,-8.943882,-8.070648,-8.536831,6.059085,0.948631,8.230585,-0.254072,-6.656064,-2.514256,4.962390,-0.039789,9.369987,-7.036609,-9.198773]],[[-5.124324,0.487090,-1.874834,6.853713,8.653151,-8.121625,-9.317582,-9.278059,9.424874,0.166061,2.051177,-6.366794,-0.963796,-1.175621,-0.295647,-3.344440],[2.789140,1.564695,-0.780630,-4.300543,-5.217640,-7.800840,1.142676,5.563149,-9.970650,-5.739532,7.241049,3.242156,-6.998154,-9.246372,-6.622668,0.870661],[-0.955682,-6.558125,1.651540,7.329609,3.749284,0.016600,-3.262499,-8.764125,6.719069,-0.180943,5.279050,-1.397327,-7.593215,-0.382125,8.199931,-1.217352],[5.786576,-4.767975,6.760028,-0.783898,-6.707827,5.921979,-5.524638,6.159128,-2.660383,-2.950358,7.507057,9.680029,4.776590,-7.324977,6.918428,1.074356],[2.991771,-8.750631,3.817050,-7.875134,-3.485978,-7.294581,9.569761,-6.665893,2.608237,6.417054,8.688667,-7.855723,-4.085080,1.618927,2.464240,-2.264939],[6.440697,-4.566274,4.923455,-5.779922,-2.119377,-3.541869,-9.773541,-1.578454,4.409625,-4.967616,-5.671121,-0.152347,9.510413,1.382210,-4.303659,-1.810634],[-4.822120,-2.558399,0.671097,9.092504,1.491467,9.578056,-9.631202,0.458073,8.184049,-9.992250,7.284527,-4.473194,-2.341507,5.087074,-4.822817,-3.259923],[-9.189344,-2.643753,4.465974,-4.711764,-6.871983,-7.264500,6.451284,-4.214832,4.338111,-5.864068,6.086832,-6.665254,-8.417891,-6.061545,2.051695,8.475735],[8.938275,5.235194,6.355313,5.032282,7.281286,-9.770235,-0.867618,7.913258,1.548767,-3.046641,-1.855412,5.414800,-7.360624,0.362655,-1.738297,-0.393493],[4.292599,2.546780,5.999348,-2.360652,-9.526830,8.852237,7.049240,1.532220,-8.509204,-5.536492,-7.630259,-0.321122,5.340815,-2.196723,-6.841266,-4.704013]],[[-1.279468,2.794964,-7.186218,-5.371560,-9.566813,5.276077,-0.021908,6.185844,-9.474271,1.918651,4.362179,-7.892682,-2.415821,-7.439466,6.651987,-0.541925],[-7.536098,1.384695,6.496886,-7.482137,5.928370,6.094083,-3.466062,-2.658140,-5.200680,2.076440,9.571674,9.137789,-3.974807,4.103861,-4.262865,8.152015],[2.124627,9.444714,-3.443502,-1.135860,-1.447418,8.565822,-6.141820,4.140037,1.773820,-4.874231,-6.040707,-7.128736,-8.693004,-1.791068,6.367705,1.035528],[-1.506573,0.104588,-4.977521,-9.092921,-9.906162,4.310382,-9.752739,5.589029,6.237002,-0.906223,5.859233,-2.457957,-8.655150,-2.630042,-9.138696,-9.690875],[7.686612,7.407703,-7.910049,-3.917554,1.940863,1.548159,-8.234044,-1.749222,4.308936,-0.887784,8.482936,-9.922596,3.708175,-0.315132,-9.176452,3.235449],[-8.575957,-1.883830,-3.315943,0.484593,-3.792228,8.931178,-7.726840,5.354409,1.703813,-8.138218,-7.878250,-6.070958,-8.564503,-4.588329,-0.991643,-6.619362],[-1.641295,6.970407,9.541503,8.612139,6.130254,-6.556134,-4.815607,8.090001,1.544925,-9.475737,-8.631701,-5.641093,3.086498,-2.434641,-3.328935,5.830475],[8.419300,5.990806,4.849172,-1.764693,-7.944485,-1.524433,-6.877243,-8.338937,-9.026116,-2.503590,4.944013,0.067066,3.992915,-9.268962,-3.229780,-3.483153],[-4.322883,-6.838164,-6.215477,2.696557,1.019834,9.094316,2.360135,-0.954022,6.378152,6.906685,9.869061,0.406320,-5.273665,-4.458259,1.961137,-4.187505],[-0.499026,-8.065883,3.305074,0.537183,7.370903,6.150677,-7.693419,-6.307672,-5.148715,1.599415,-2.751629,-0.241555,-1.246940,7.952604,2.021217,-4.391616]],[[-2.600235,3.674154,-7.374845,4.236617,0.205782,-8.344002,-1.014975,2.733553,-4.102180,-0.245559,-1.602379,0.945129,7.320674,-1.113153,-8.891717,-1.280348],[6.214507,1.124179,8.280583,-1.113602,6.094525,-1.123387,2.872146,-2.191286,-6.186783,6.288528,0.579598,-8.705319,7.952497,4.421491,3.912601,9.737997],[9.496869,-2.193862,1.840860,-4.147345,9.489501,-9.139581,-2.677167,8.788241,7.115943,3.638019,2.815656,0.871528,3.674494,1.176072,-1.319884,4.120995],[5.121928,-4.228832,-4.450282,3.767556,-2.518778,9.410703,-6.305893,1.951141,5.733809,-6.274113,-9.310343,8.875268,-5.945951,-8.711338,1.253381,5.501463],[8.285641,0.916237,-7.728868,-9.490903,-6.230797,4.841746,-6.792532,-8.219706,-5.393631,-3.897418,-2.767622,-1.780137,-5.668995,-9.090514,-3.492086,-2.127196],[3.924688,-3.529005,-7.690729,-9.273455,-3.770144,6.505282,8.217992,-5.614138,-7.403236,-3.354103,-0.865151,-8.221247,-1.295548,7.392748,-9.407829,-6.342073],[9.134247,5.102425,4.151199,9.768226,1.707820,-1.709727,-6.194114,-6.124834,-3.141464,-0.274927,4.546643,3.363258,4.708138,8.423113,3.021703,6.820951],[-9.576208,-2.882177,9.300756,7.684546,2.413610,8.967861,-3.547758,-1.075484,-5.581531,6.781125,4.336189,3.226515,1.775397,-1.542342,6.516573,-3.587954],[-0.118783,2.926539,-1.552858,3.380415,4.495809,4.808968,-0.323560,-6.366483,-7.101325,4.584958,-5.378165,-5.035490,1.798345,-1.883402,5.571764,-4.190107],[-2.857345,6.700969,-5.741967,-9.972647,3.557475,6.886570,3.718886,-7.758408,2.319569,-9.494178,1.698025,-2.115272,7.471526,3.653530,3.512735,3.534804]],[[3.430070,-7.135740,0.883799,5.520619,-3.788559,-4.172602,-2.433834,-4.020871,-5.085164,-9.588326,3.823630,-0.015306,9.283658,6.327921,0.646537,-8.060253],[3.092864,-0.468974,4.433595,8.975775,-0.079938,-7.663228,9.710471,0.508196,4.757543,6.376406,-2.666182,7.219302,9.298957,-2.329436,5.761248,6.486090],[1.366865,4.326192,-2.340547,-5.394755,0.373488,9.306497,9.103882,-1.156761,-8.978503,-4.932986,-8.989407,1.678428,-9.939617,-7.324107,-5.721136,7.684295],[-6.826042,6.061756,6.257112,3.441665,-6.759911,8.653765,6.485340,-8.793545,2.927526,-2.297279,-8.390090,8.098642,3.323142,5.954163,-7.789914,1.331477],[7.698676,5.677924,7.884414,9.853812,0.229434,6.404441,0.334354,2.067379,-3.605471,-1.773163,9.493655,-4.665876,7.076141,-4.033177,-2.325469,-3.834545],[-6.848408,-2.962261,2.613942,5.680545,9.344490,9.629048,-0.044459,4.987666,3.308883,-1.508978,-2.990218,0.129499,-4.025165,1.239193,-8.455313,-2.469616],[3.322264,-6.407965,7.024214,7.212557,-5.215686,1.887692,3.039379,-4.783076,-3.559460,3.575274,3.496887,-4.376732,6.128312,-5.175158,-2.689395,-8.181662],[1.077963,-1.985918,7.562028,5.572538,-3.121680,-2.726257,-9.598855,-2.975355,2.217880,1.736507,5.052209,-0.704438,1.085940,-7.474901,-8.792055,5.487615],[9.872210,-0.257065,2.320440,-5.669973,-0.633943,-1.718486,3.471098,0.101359,-9.429138,3.533870,-7.229702,-0.437117,-1.292403,6.422637,-2.549336,9.449589],[-0.702319,-8.671378,4.499994,-3.217035,9.311473,-7.118441,2.743411,-6.882496,-9.421560,1.956558,0.555864,-3.432018,-0.588870,-7.202701,-5.590920,-3.021230]],[[1.935213,3.999468,-3.046527,-6.851355,-8.728154,-7.477325,-7.618174,2.517137,0.575061,-3.972557,4.939310,-0.007984,-5.865370,-1.807533,-0.381151,-3.925257],[4.617231,1.726731,4.867308,5.832660,-3.823833,4.031111,-6.480136,-5.554498,-0.049701,0.199025,3.654598,8.105888,-9.061509,0.468948,6.192893,2.028200],[5.621987,-5.715086,-5.918955,-5.507605,1.456756,-6.573560,-9.873295,4.404237,8.960604,-1.531781,3.408914,-3.389229,6.954258,-6.378518,6.460654,5.624435],[-2.464398,8.729125,-0.628050,-2.103574,-5.318292,4.968791,4.423189,9.630794,4.910890,0.898048,1.608319,3.286095,8.287522,3.758215,2.397517,2.901873],[-9.649855,-3.457443,-1.331570,2.607838,3.953256,-1.526644,0.482779,2.657436,7.624213,6.907792,9.454081,-9.936456,7.270960,4.906859,-4.684970,-0.137988],[-1.530682,6.155484,2.821288,0.707858,-0.961018,1.285964,5.784735,-1.777618,-4.074291,2.073861,-0.959176,-6.045448,-9.124020,-3.770007,2.774809,1.188187],[-6.264176,-0.153954,3.678188,-2.120762,0.826777,-7.639443,2.709483,-3.065090,-1.868453,3.507690,9.186031,-7.029345,8.753133,-4.664690,-9.125596,-2.578971],[7.300957,-4.953850,-8.828310,-8.247411,8.953188,-0.285862,1.601992,-8.114857,5.212510,0.741561,7.662641,-5.043711,-8.919998,9.694535,-9.360805,2.734924],[4.979072,3.359502,0.762285,5.467813,-1.142509,0.519581,-1.024191,1.441582,3.788883,-2.050005,6.884244,2.699674,-7.274563,-1.465004,1.897930,-5.801587],[5.639070,-7.719774,6.505578,4.890379,-8.585730,7.345778,-6.704172,-3.335856,3.276750,9.496997,2.625893,1.079654,8.616231,-4.279029,0.337084,5.974854]],[[-9.727630,5.412693,-2.945873,3.757229,9.528168,0.917727,-4.624037,1.846508,1.090543,-5.670676,-1.427351,-8.780419,4.483036,-5.532788,7.033095,6.870949],[1.350288,5.849041,-6.621332,-1.254488,9.289206,5.543228,4.345035,-4.209349,0.153198,9.025231,-8.282712,-8.597715,4.200217,-9.266440,-2.064275,-8.621447],[5.112469,9.812016,8.275149,2.746182,-5.827695,-4.829512,-6.715812,-0.603310,7.741303,3.929082,6.093551,2.537323,-1.992187,5.982925,5.676852,-0.572142],[4.160415,-8.642159,-0.059782,5.707105,9.370839,-0.813090,-2.299740,7.121098,0.679658,0.387194,-5.368860,3.326793,1.728365,-5.129679,-2.843759,2.991725],[-1.327574,-5.392193,5.183419,8.878123,9.593522,-0.151884,-6.638837,7.820784,-1.594924,-7.566808,2.458179,9.648476,-2.434974,-3.147680,2.426386,-9.655025],[2.073541,-2.564158,2.831985,1.303656,8.173549,-9.326871,-2.568843,0.192172,1.334977,0.196888,5.657670,1.741646,-6.453447,4.099401,0.157227,-5.625740],[-4.439227,8.416674,-8.065020,9.644770,2.531882,-5.185335,8.952675,-9.239900,8.140164,-9.101568,3.592505,4.026605,8.237781,2.705827,-9.278433,1.280075],[-7.010718,-8.498698,-4.549243,-5.295757,-4.128900,0.108677,6.122133,-0.814571,8.860432,6.050011,-6.606782,9.201535,4.687816,-8.045618,-0.787096,6.489668],[-8.108117,9.776501,7.823083,-9.743664,-2.338168,0.355548,-3.434024,7.497352,-4.099883,-5.502123,7.054400,-5.758296,-5.433654,-1.712561,7.450172,0.245379],[-4.465418,-8.374807,-0.247876,6.396253,-8.234953,-8.631647,-3.005072,-2.070512,7.942920,6.198211,-1.020519,3.425171,-2.496575,5.517138,3.267530,4.528232]],[[-4.379568,0.737527,2.381970,1.749517,-7.341284,-3.536773,9.358703,6.449712,5.322840,2.415498,8.544556,-8.312666,3.018120,7.323570,-9.076568,-3.743176],[-0.957429,8.876580,-2.627617,6.577352,4.745275,9.730851,-1.223325,7.354609,9.585828,-4.461147,2.259401,-7.810841,-7.043776,-6.077087,-7.933468,5.845321],[-7.395773,-7.060261,-1.606465,7.162567,7.654073,-7.315099,-3.277336,7.121177,3.039816,-0.747542,-9.417122,6.606434,-2.637724,2.233535,-4.362043,3.525689],[-4.534319,7.931960,5.981996,-3.935095,7.953390,-6.843711,-1.458137,8.315114,1.062888,-6.020195,-7.742470,1.905675,1.774476,7.773898,0.184300,6.991468],[9.341305,-0.806505,5.687526,0.181051,-3.369398,-6.349792,-0.815958,-9.313866,5.393101,4.334647,-6.614574,-8.982964,-0.259268,3.214119,-4.769740,8.056445],[7.726974,-5.277740,-6.687290,6.891215,-4.703189,6.296184,3.110594,-5.202550,-5.936341,-6.435247,-1.335473,3.906298,-9.098766,0.749569,8.046198,-5.645169],[-5.766519,8.201601,3.016375,7.020921,7.887967,-9.697236,-1.732622,8.942478,-3.548645,6.944918,9.915163,5.118704,8.074170,-4.372139,0.320979,1.993038],[-7.534438,-7.414633,6.659723,7.709788,-9.887993,1.196139,-9.962196,-7.931755,-3.001315,-6.385477,-8.907264,-3.422721,-3.301647,-3.342702,2.940677,1.617534],[-6.491835,2.137918,-9.914440,-8.167380,-8.041955,8.063271,4.743654,-3.180521,-6.367407,7.634040,-3.787984,-0.499532,-4.016228,7.071838,0.605458,5.642947],[-7.025238,8.950971,1.169145,-7.243103,-1.354087,1.803315,6.263486,9.952177,-3.420757,-6.318605,-5.528475,1.766011,2.993427,3.527042,9.760295,-0.023466]],[[5.260359,-2.226794,-0.652736,0.744932,0.687714,-2.670437,-2.485625,-3.854286,-8.448607,4.080925,6.087449,5.021999,1.180280,3.541337,-4.909651,2.615074],[-0.519208,-7.776229,-9.236493,0.569996,-3.403566,-8.541837,2.411883,1.215235,9.590398,3.169027,7.820667,9.828554,7.265644,-1.412828,-4.818011,5.615815],[5.590249,7.562429,9.923287,5.873076,-3.110380,-1.693784,-8.459633,1.314134,0.154610,7.978454,-5.203630,0.523297,1.811381,9.683490,7.143600,-0.875596],[-6.387382,-8.996700,-4.978846,-5.392954,4.100185,0.940306,-5.503405,1.905655,4.971170,0.614299,1.436780,5.618949,-9.756355,4.856013,0.633491,-9.142660],[0.021448,-7.168193,3.661380,3.472261,7.667634,-6.813975,5.811077,7.538675,-1.888051,-0.356432,-8.323335,2.350367,-4.622628,-8.757504,-3.225929,-2.689275],[-9.743180,-4.828079,8.333277,-1.057716,-4.366879,-5.256304,9.851770,-9.452457,-4.322567,6.767544,-2.780341,7.980743,4.499024,-5.053552,6.228816,-3.965818],[9.752227,4.415583,-1.183442,-1.030615,-1.130752,-3.106056,-6.889311,-7.727193,-2.563420,9.943085,-3.960943,7.717708,8.336702,6.542503,-9.486759,-6.541844],[-1.003354,-7.679582,9.005342,2.951244,-1.430911,2.138358,-0.862622,2.363326,-6.785309,2.220825,-9.266606,-8.402772,6.207443,-8.243511,0.540332,0.494251],[-1.966330,-1.821846,-7.948670,4.378841,-2.493774,-6.182723,-1.708950,1.627722,-2.396874,6.243826,8.038776,-3.431977,-1.801517,6.718088,9.084997,2.483281],[-9.159962,-5.606787,-6.426515,1.019382,-7.528069,5.014201,-6.557471,9.761952,-1.248085,3.402715,4.569281,-6.895768,-3.031509,2.791844,-8.665697,0.352706]],[[7.708440,-5.741565,5.860543,-6.278812,1.391660,9.809950,-3.473221,-8.587048,8.785812,-2.364152,-8.413387,-6.870336,-5.317094,-3.129158,2.714299,-9.386167],[1.174869,-6.135077,-4.117519,3.476430,-8.191831,1.135371,3.301258,3.993923,4.901058,9.412681,-1.653883,-9.811146,-8.213326,-3.211361,-3.163251,-6.781559],[2.310293,1.006008,2.065659,0.689381,2.986665,-1.714077,-7.814181,7.061975,4.551208,2.704784,4.085448,1.738634,0.431746,4.347802,-4.811507,8.934499],[-4.576341,9.185028,2.916070,8.864246,-9.102479,-8.518439,-2.075871,-1.863280,-5.876714,3.849349,-2.465656,6.321808,-4.768996,2.759141,-7.210238,-7.620085],[8.620950,-3.770002,-0.955044,8.749700,9.266998,-9.321998,-3.449176,-3.125107,-3.546680,-7.840116,-5.016573,-1.667323,-2.527766,3.812315,6.426076,3.438914],[8.421761,2.559079,3.923938,-3.101134,-6.180573,-1.234322,-1.111724,-2.961156,4.212361,6.271611,-5.174682,-7.075511,4.890732,-0.671419,-6.200354,-6.965226],[0.655238,4.849424,-0.739793,-1.629957,-8.681770,2.566453,5.374230,-6.529282,-9.814002,-8.339322,1.234724,6.081604,-9.006459,9.059978,6.218768,-4.144632],[-7.947838,-2.045397,-0.023262,4.560420,8.400044,2.546631,-7.609063,2.744468,4.688250,-3.164275,3.912511,8.910548,9.314641,-1.616927,-8.835444,2.341818],[-0.306754,-2.068818,-6.967203,-0.724067,-8.808456,-5.426013,6.981505,-9.810157,2.331342,8.035611,-2.119347,-2.950430,-3.596011,8.526287,-0.772362,1.691957],[-0.559095,9.039688,1.572482,-4.176381,2.447323,0.871371,7.018606,2.975970,-2.942129,4.256373,9.478597,-7.670185,-6.284631,0.413676,-7.580682,0.250239]],[[-6.659334,-9.497331,-3.141688,3.474748,6.292240,-9.959589,-4.687734,-3.300144,2.672783,-3.958773,7.009496,-5.248690,-6.391435,-7.781061,-4.486965,4.902428],[-9.526096,-9.258303,-4.695758,-8.369142,-9.533203,-2.203081,-5.804783,7.182273,-9.734489,1.527008,-8.737417,7.263691,2.117519,-9.216043,-6.365098,-8.824765],[0.532279,1.228409,-1.473288,0.672569,6.849687,-9.643489,-0.251227,7.906046,8.027154,5.340909,-7.739404,-2.608013,-6.974256,1.323290,-9.905293,-5.674093],[-7.828676,3.535388,1.668699,-5.279136,1.182923,7.318486,-6.847546,-7.270249,8.831912,-9.876254,8.653793,2.096022,1.752644,-0.629242,-1.513991,0.761549],[-8.480658,6.116534,4.178905,-3.574116,-2.076576,5.583577,-4.737242,-5.207689,2.239932,5.111094,2.044408,-5.608412,6.426799,-7.404049,7.099322,5.469643],[4.238214,-7.319154,-1.423929,1.865000,-3.841998,4.758345,-0.381629,-0.871071,-3.404457,-2.233503,-5.307554,-0.920414,4.645815,4.799717,-6.307240,1.989887],[7.830904,0.624390,-4.917539,4.297257,6.361179,-5.104866,-2.438078,7.945489,-5.809347,4.119777,-9.120501,2.354105,-0.591364,8.342403,1.114327,-9.819105],[-1.055053,-5.540098,-9.930286,8.412466,-5.027837,-1.662721,-5.729574,-1.922221,6.061227,3.248951,7.868330,-7.589567,5.252228,6.306325,-7.852185,5.171776],[5.337178,3.527420,9.445589,0.469544,-4.892464,4.309336,6.439668,-5.800497,4.193954,-5.647513,-5.029642,-8.216883,-7.111496,-2.350540,-1.573347,0.772608],[1.965936,9.476083,6.721807,-5.378936,-4.791016,-3.054129,0.922596,5.640638,-2.821982,-8.020891,-0.548518,-6.204717,-8.450588,0.499237,2.210964,-2.066557]],[[8.626910,5.023909,-9.501733,2.360448,8.536296,-3.843269,-7.095246,3.752191,7.315472,4.231338,6.588611,8.500202,-1.332365,-4.124753,2.583876,-9.004859],[-7.131856,-9.741945,0.601450,-6.644026,3.882933,-7.518417,-0.219807,4.929681,4.129919,6.084280,-8.519309,-6.530663,9.150491,-2.897125,1.540596,9.012514],[5.989744,-9.334170,4.254434,5.924654,9.627104,-0.613704,-0.207215,1.569959,-1.891410,-2.068738,0.300199,6.675097,1.415665,-6.074938,-5.381101,-5.595092],[0.834056,6.486709,3.171082,8.299646,-4.779802,-9.960149,4.082521,-7.973883,-7.591768,8.107985,6.801570,-1.484509,-7.961399,8.276924,0.814143,-4.656730],[-0.839899,9.141754,7.221270,-9.610359,5.965697,-0.613518,-4.144261,-4.842133,0.435381,5.068310,7.306336,7.844195,-2.430229,-9.685984,-0.357924,-8.060797],[-8.085533,7.319134,-6.988574,6.651034,-1.052292,6.988038,-8.817104,-6.107298,4.099000,-2.190614,5.355724,-0.104611,-3.601969,9.758216,-7.420435,9.511069],[-5.830381,-0.332619,-0.201229,-8.587782,5.835429,-4.169466,3.059293,1.631590,-6.376849,4.015963,1.542383,6.479388,1.695901,-9.841297,-8.796205,-1.890483],[-2.566477,8.174212,1.783905,-5.510239,8.311592,-7.871714,6.726290,2.817762,-8.639551,1.401975,6.436342,5.028203,-3.050140,-1.545407,-0.720039,3.509909],[2.004666,4.610123,-0.331738,3.491611,-9.523419,-9.220553,8.393622,0.797443,6.889174,8.270867,5.626335,3.185538,-9.742181,-8.080948,-4.183950,-7.968403],[5.006843,-7.857702,0.097730,5.483987,-6.536745,1.953056,-9.289218,0.133490,7.226657,-4.311747,0.252056,-5.705066,9.724122,-6.157953,-6.794377,9.996135]]], dtype = "float64")#candidate|5558|(12, 10, 16)|const|float64
uop_5559 = relay.tan(const_5558.astype('float64')) # shape=(12, 10, 16)
func_5205_call = mod.get_global_var('func_5205')
func_5207_call = mutated_mod.get_global_var('func_5207')
call_5570 = relay.TupleGetItem(func_5205_call(), 0)
call_5571 = relay.TupleGetItem(func_5207_call(), 0)
func_3877_call = mod.get_global_var('func_3877')
func_3878_call = mutated_mod.get_global_var('func_3878')
call_5581 = relay.TupleGetItem(func_3877_call(), 0)
call_5582 = relay.TupleGetItem(func_3878_call(), 0)
func_2728_call = mod.get_global_var('func_2728')
func_2730_call = mutated_mod.get_global_var('func_2730')
call_5583 = func_2728_call()
call_5584 = func_2728_call()
output = relay.Tuple([uop_5559,call_5570,call_5581,call_5583,])
output2 = relay.Tuple([uop_5559,call_5571,call_5582,call_5584,])
func_5585 = relay.Function([], output)
mod['func_5585'] = func_5585
mod = relay.transform.InferType()(mod)
output = func_5585()
func_5586 = relay.Function([], output)
mutated_mod['func_5586'] = func_5586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5585_call = mod.get_global_var('func_5585')
func_5586_call = mutated_mod.get_global_var('func_5586')
call_5666 = relay.TupleGetItem(func_5585_call(), 1)
call_5667 = relay.TupleGetItem(func_5586_call(), 1)
func_2564_call = mod.get_global_var('func_2564')
func_2567_call = mutated_mod.get_global_var('func_2567')
var_5674 = relay.var("var_5674", dtype = "float64", shape = (8, 20))#candidate|5674|(8, 20)|var|float64
call_5673 = relay.TupleGetItem(func_2564_call(relay.reshape(var_5674.astype('float64'), [80, 2])), 0)
call_5675 = relay.TupleGetItem(func_2567_call(relay.reshape(var_5674.astype('float64'), [80, 2])), 0)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_5691 = func_1931_call()
call_5692 = func_1931_call()
uop_5698 = relay.log2(call_5666.astype('float32')) # shape=(5, 8, 1)
uop_5700 = relay.log2(call_5667.astype('float32')) # shape=(5, 8, 1)
uop_5707 = relay.sinh(var_5674.astype('float32')) # shape=(8, 20)
output = relay.Tuple([call_5673,call_5691,uop_5698,uop_5707,])
output2 = relay.Tuple([call_5675,call_5692,uop_5700,uop_5707,])
func_5714 = relay.Function([var_5674,], output)
mod['func_5714'] = func_5714
mod = relay.transform.InferType()(mod)
mutated_mod['func_5714'] = func_5714
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5715 = relay.var("var_5715", dtype = "float64", shape = (8, 20))#candidate|5715|(8, 20)|var|float64
func_5714_call = mutated_mod.get_global_var('func_5714')
call_5716 = func_5714_call(var_5715)
output = call_5716
func_5717 = relay.Function([var_5715], output)
mutated_mod['func_5717'] = func_5717
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5725 = relay.var("var_5725", dtype = "int8", shape = (15, 2, 3))#candidate|5725|(15, 2, 3)|var|int8
var_5726 = relay.var("var_5726", dtype = "int8", shape = (15, 2, 3))#candidate|5726|(15, 2, 3)|var|int8
bop_5727 = relay.less_equal(var_5725.astype('bool'), relay.reshape(var_5726.astype('bool'), relay.shape_of(var_5725))) # shape=(15, 2, 3)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_5732 = relay.TupleGetItem(func_4154_call(), 1)
call_5733 = relay.TupleGetItem(func_4155_call(), 1)
output = relay.Tuple([bop_5727,call_5732,])
output2 = relay.Tuple([bop_5727,call_5733,])
func_5745 = relay.Function([var_5725,var_5726,], output)
mod['func_5745'] = func_5745
mod = relay.transform.InferType()(mod)
var_5746 = relay.var("var_5746", dtype = "int8", shape = (15, 2, 3))#candidate|5746|(15, 2, 3)|var|int8
var_5747 = relay.var("var_5747", dtype = "int8", shape = (15, 2, 3))#candidate|5747|(15, 2, 3)|var|int8
output = func_5745(var_5746,var_5747,)
func_5748 = relay.Function([var_5746,var_5747,], output)
mutated_mod['func_5748'] = func_5748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_5785 = relay.TupleGetItem(func_4250_call(), 2)
call_5786 = relay.TupleGetItem(func_4251_call(), 2)
func_4938_call = mod.get_global_var('func_4938')
func_4942_call = mutated_mod.get_global_var('func_4942')
const_5791 = relay.const([[-9,-3,-4,10,1,7,-9,10,-7,-3,10,-8],[8,-10,3,2,-2,8,9,-10,-5,4,6,-6],[-6,2,2,7,-9,8,9,-7,4,7,-5,-4],[3,-6,1,-2,9,-5,5,1,-10,-7,1,-10],[-9,-8,1,7,-1,5,-5,1,4,-6,-9,-2],[-8,-8,4,5,2,-2,-5,-8,-9,8,-1,-7],[6,-3,-2,2,7,8,7,-7,-7,3,-7,10],[-6,-2,-9,2,-4,-10,2,-6,-3,10,-10,-8],[-7,2,-4,2,1,6,4,-7,5,-5,-1,-5],[7,-6,-2,5,7,-5,-8,-8,-2,-2,4,-3],[9,7,-8,8,-6,2,9,1,-5,-7,-3,5],[-1,10,-8,-8,2,9,-6,7,9,1,-7,6],[-9,6,-7,-9,-7,8,3,-2,-9,-7,6,-8],[3,7,-4,-5,-3,6,1,-10,4,6,4,-6],[-9,-2,7,3,1,-4,-10,-1,10,-5,-3,-3],[-7,-8,-7,5,-7,4,-7,6,7,-7,8,2],[-3,1,3,7,-1,10,9,-7,-4,-10,7,1],[7,3,-3,-3,3,6,-8,-8,8,-8,-5,3],[7,2,-1,-10,-10,2,-9,4,1,-7,-5,-7],[-3,1,-1,9,10,-3,-4,-9,-7,10,8,-7],[-5,7,9,4,10,-4,-10,10,-4,-2,8,-5],[-2,1,10,-8,-2,5,-10,5,-4,10,2,5],[5,-4,-7,-9,1,-1,-8,8,-6,3,-1,4],[7,-1,-6,-5,-2,-5,6,-9,4,10,9,-3],[-10,-8,5,8,8,3,6,6,-4,8,-2,9],[-9,9,-6,2,9,8,-4,7,6,5,-7,9],[-9,-3,5,9,8,1,-10,-1,5,-4,6,10],[-3,-5,5,4,-4,-8,-7,-3,7,-1,9,6],[1,-10,5,-2,-4,-1,-2,6,3,5,1,7],[3,4,1,-3,-2,-1,2,7,2,-6,4,10],[-6,-7,2,4,3,-7,-10,9,3,10,3,3],[5,10,1,-5,7,-5,-6,-6,9,-5,4,-10],[4,-2,7,-4,5,10,-6,-7,6,3,1,5],[3,-6,2,3,7,-2,-1,7,-2,5,3,-2],[2,-5,5,2,7,-4,-5,6,-10,-6,-7,-8],[1,9,-5,-5,8,-9,-9,10,8,-7,-9,-5],[-1,4,4,-9,7,-1,10,-9,-9,9,9,5],[3,10,-5,5,-6,6,-2,6,-4,10,-6,-10],[9,-2,1,6,9,10,-3,-4,5,-8,6,4],[3,-3,5,4,5,2,1,-3,-8,-6,9,7],[-9,-1,-10,-4,1,2,3,1,9,-7,5,-5],[-5,1,3,10,-4,-9,-3,7,-2,-1,-4,4],[-6,-6,-3,4,-3,3,-5,-8,-1,-1,-1,10],[7,10,-4,5,-7,2,3,9,-3,10,5,-4],[6,-5,-6,-10,-8,6,-7,3,5,6,-3,4],[9,-1,3,-3,5,-5,4,-7,8,-4,6,10],[3,7,-3,2,-6,-6,-10,-7,-6,-7,-2,3],[-8,6,4,-3,-4,-7,-3,8,-1,8,1,8],[2,10,-10,3,-1,1,-8,6,-7,10,-9,-9],[1,4,7,-1,-5,-10,-7,-4,5,-6,10,-7],[-5,8,3,6,9,8,-10,-4,4,-4,8,-9],[-3,-7,7,1,1,7,1,8,3,-5,-6,2],[2,1,1,-4,-5,9,-5,3,4,-9,-3,-4],[-6,-1,-9,-2,-6,2,1,4,-8,-7,5,-8],[1,-5,-8,-1,9,7,-3,-8,10,-8,5,8],[-7,6,-6,-5,4,1,7,6,-4,-4,2,7],[10,-4,9,8,-8,2,-9,-2,4,-6,-5,-9],[-7,-5,-6,10,8,-3,-9,-7,-5,2,-3,-10],[-8,-2,-1,4,-5,-9,-1,-9,5,8,-2,3],[-3,3,1,-4,10,-4,6,-10,-6,4,-8,-8],[4,8,-2,-3,-10,-10,-10,2,2,-2,5,-1],[-3,-10,-7,-5,-6,-5,6,3,4,6,2,5],[-7,2,9,3,-10,2,-1,6,-1,-6,-1,-2],[-4,9,10,10,1,7,7,3,-5,3,-1,3],[-2,-9,-10,7,3,10,10,-9,3,-2,-10,-6],[-9,8,1,-3,4,3,-5,10,6,1,9,8],[10,2,6,-2,10,6,5,2,3,3,-6,8],[-2,-10,3,-5,-10,2,7,-1,-7,-6,-8,2],[-4,1,-10,3,-10,-5,5,-5,-6,-10,-10,-8],[10,9,-2,9,-8,9,-9,-9,7,9,3,6],[-10,2,7,-9,6,5,1,-6,-4,8,-7,-2],[3,8,-5,7,1,7,1,-9,4,-7,-9,5],[-7,-7,-1,1,-10,2,-5,3,8,6,-6,8],[-8,-4,-5,-10,-3,9,8,10,10,7,10,-1],[-2,10,3,-7,-3,10,1,2,-1,-7,-2,-6],[8,-10,-3,-1,-10,-2,-10,-8,1,3,-9,5],[-8,8,-1,4,10,-2,-5,-10,3,-9,-1,6],[-4,6,-5,-5,7,-7,-10,10,7,2,4,-8],[-2,-9,-4,8,5,-5,-5,7,4,10,5,1],[-5,-3,-5,-5,-9,-1,-3,-3,3,1,10,1],[2,-7,3,-8,-3,7,-3,4,-9,7,5,10],[-9,7,-1,-3,-10,-9,-10,-3,-1,10,5,7],[10,7,3,-3,-10,-2,-9,-3,5,3,-2,-10],[-9,6,4,-9,7,-2,-5,3,-7,8,7,-6],[7,10,8,-2,-10,-10,-4,-3,-4,1,1,-7],[-8,8,-6,10,6,3,-9,10,5,-6,-10,10],[-3,5,5,-4,-7,-8,7,-8,-7,-6,6,-8],[7,-10,2,-2,10,-8,-9,10,5,9,-8,-2]], dtype = "int8")#candidate|5791|(88, 12)|const|int8
var_5792 = relay.var("var_5792", dtype = "uint16", shape = (64,))#candidate|5792|(64,)|var|uint16
const_5793 = relay.const([9.710638,-2.778960,-8.591457,7.559477,-4.707947,2.890048,-6.779091,5.556781,8.447716,4.449242,-1.201217,2.624933,2.724237,-6.268812,-3.035795,-2.653474,6.766938,5.892411,-5.903170,6.245573,-2.917072,-8.604897,1.712657,2.245025,-4.099535,-5.260838,-4.621884,9.023535,-7.497479,5.115647,2.451289,-8.873234,-5.297369,-3.683844,-0.817647,-7.200984,1.511751,9.544845,-3.906396,2.046919,2.059831,-9.802184,9.740841,-1.142524,3.517518,0.772199,5.779040,5.102752,6.258636,-4.984352,1.234500,-3.805213,-2.131437,7.396158,-0.213522,0.282895,-1.101325,-0.136125,7.352397,5.935624,-0.559167,9.096243,-3.650324,5.489962,-8.937309,2.990835,-4.484759,-0.180657,1.793093,-6.807664,7.694791,1.971592,2.320897,1.678674,-4.364669,6.542484,8.699083,-7.940293,2.281641,-7.007427,-5.419175,1.769811,2.443732,8.165055,3.181594,1.633784,5.605438,-5.108767,-3.542451,2.725820,-7.363327,2.267294,4.497411,5.263222,2.728153,-0.106983,6.144895,7.413313,-2.193157,2.593097,-0.659866,-5.957007,3.541317,-2.357603,-3.483086,3.453039,-0.164642,4.889768,-3.006406,-0.340215,-5.409257,6.387254,-3.525757,-3.396707,9.194843,-7.561153,-0.380363,0.717045,0.764412,9.220267,7.922431,-0.539993,8.139191,0.140212,-4.797334,-1.106391,3.560769,-3.128202,-4.819405,-6.245238,-1.863675,0.609439,4.652380,-6.999377,-4.370001,-1.234277,-4.612504,8.072320,-1.843503,-8.170099,-9.585545,9.985278,-2.697964,6.269155,6.673180,6.819959,-9.085401,-1.397470,1.240268,-6.315952,0.740433,-0.696122,7.354539,2.885103,-3.126738,-5.655671,-8.887654,-1.370556,8.432143,4.317707,3.064139,-5.820613,6.131841,1.880708,2.247436,-8.576669,0.775014,8.774142,-3.981240,-9.327875,-5.622733,9.450871,8.928022,7.907252,1.679988,5.005373,2.055438,-3.861802,-8.649487,-3.136326,1.456281,-7.101924,4.968449,9.909563,2.722308,-6.392416,-7.625689,-5.007914,-1.339626,-9.622664,5.545748,-3.023079,9.140228,0.313037,5.831686,-5.167410,6.406360,0.065667,-0.075196,-3.546700,-6.617779,8.718651,4.423457,-9.889521,7.235815,0.622191,-2.539785,-5.796606,1.895246,-3.769141,8.446304,9.555099,3.600111,2.020124,-9.514317,4.709576,-1.156484,1.314710,4.076711,1.739231,0.969620,5.472802,4.076579,6.317577,6.948212,1.820892,-8.930096,5.197953,1.121279,9.732025,6.923510,-4.429070,5.421622,2.955336,-3.613340,-3.124251,3.756015,6.861212,2.790445,2.234939,-1.875901,1.846828,-8.645317,5.170264,2.971499,3.216703,9.342835,-7.219049,2.076726,5.611061,4.592991,8.292323,8.924877,6.572532,-7.353124,-6.713234,5.009539,4.614388,-6.787949,2.782192,-7.583821,-1.982069,-3.577621,-0.415028,-8.466247,7.145680,4.098933,1.481514,-0.214036,6.863139,9.189140,3.464492,9.283974,-6.923505,9.515695,9.866302,-4.240851,-1.735174,9.799546,6.079991,-4.640902,1.070839,4.237611,6.983889,1.463716,-6.409945,-6.472287,1.323187,9.834480,8.455645,2.435600,-5.968972,7.467630,-4.623454,7.592806,-5.743602,1.617821,-1.301847,-3.471352,-0.543330,-5.377367,1.313551,-9.656322,4.360405,-4.105626,5.011522,8.292365,-8.304021,-6.737835,3.810895,-8.209684,0.416373,6.377461,-1.611991,4.713609,3.775736,-4.216675,-3.580976,1.417830,-7.599207,7.608047,3.885006,7.617856,7.641276,5.327590,0.608758,-5.664581,3.317897,-7.228250,-3.405437,-3.574233,-1.501001,-7.036506,9.776048,-8.212941,6.009511,6.356674,-6.876328,-3.808635,-3.981688,8.026646,0.223490,0.993301,4.589610,7.914497,4.207963,-5.106865,-1.672432,3.953578,-9.344068,7.912644,6.760725,7.430765,4.912410,9.048315,7.421318,2.353593,-3.325794,4.107394,8.252665,2.089016,-0.126496,-0.980938,-1.196337,-4.870756,5.046187,4.508636,7.910776,-4.889147,-8.392066,-9.808597,-8.231551,1.028060,-9.172814,5.521515,9.374314,2.970938,-8.324353,-5.919379,8.863324,4.946613,-0.731341,1.840044,3.826774,-2.053446,5.161328,4.738953,-2.405293,-0.711818,4.116249,-5.290971,6.241575,-2.838670,1.480425,-7.042927,-6.496158,2.632554,-3.216170,-8.006497,7.689268,-1.024078,4.744788,-4.860732,-8.041857,1.695956,-5.226537,-9.578126,6.630766,1.503296,1.703194,8.740832,-5.607865,-9.972723,2.131723,-6.958711,9.417615,2.621170,4.738360,-4.874829,-6.535776,8.552443,-8.966635,-8.362946,1.886584,-0.177904,-7.448765,-0.159387,2.312780,2.936163,1.822946,6.406735,-6.045641,2.118207,-6.315316,3.363085,5.911633,-6.312966,-8.041943,8.472300,-2.325847,-4.945220,5.955668,3.220064,1.199379,2.926129,2.664818,1.332767,6.030227,0.835479,5.974186,7.661463,7.994033,-3.478782,-5.704034,3.009298,2.916941,5.475508,-8.173952,3.504659,-5.170845,-0.058955,8.317805,2.587848,8.464862,7.684834,-8.104574,0.585362,-2.070441,5.361351,-9.445389,7.237630,7.598108,-0.174922,-8.299740,5.374097,8.365008,-7.905379,-6.539440,0.770486,-0.877344,-5.293259,8.064087,-6.945629,0.737396,8.022741,7.492275,4.202897,0.166593,-1.984196,-7.887697,-1.729809,-4.517408,-9.781089,4.641982,-3.209003,-3.889613,-1.085485,-3.097670,2.596621,-6.653011,6.067188,-5.319118,-7.883839,8.051682,4.399872,3.532662,7.560234,-5.875487,-2.511958,0.929102,6.685245,2.757561,-0.222050,-2.899557,8.595528,-7.360222,-4.723619,5.719938,-0.430213,-3.042383,-2.648070,-2.452885,3.027821,-4.190651,-9.689765,-3.739659,6.603813,4.700405,5.947878,-4.255271,-1.281070,-8.367560,6.708622,-6.003755,-7.864606,9.325090,-6.164015,-4.120258,-6.477804,9.161177,-6.965699,-5.993088,5.314327,0.152930,2.934401,7.965292,-8.439152,1.979688,8.821190,-1.138156,-0.907522,5.061319,5.965961,-9.380781,-0.303676,-3.884538,0.266946,-6.931022,-3.730554,9.101465,9.609727,7.321356,-1.887942,7.606484,-5.033205,5.659535,5.435694,0.201101,-8.839890,-6.190436,2.193219,-1.803534,5.633186,8.614372,-9.120343,-6.425362,9.272251,-0.041942,-8.763099,-6.993824,3.846200,6.015402,-3.099995,7.936260,-4.355983,6.564736,-8.678754,-4.754765,-6.210164,0.998522,-6.657141,1.386665,8.419584,-0.716351,5.253356,7.419463,-5.391350,-1.107232,2.198159,-6.072509,0.807097,-3.154284,6.449963,-5.828109,-0.381802,-7.920213,0.012736,6.014698,9.308482,-5.303749,-8.198479,8.146657,-7.690403,2.167512,3.551329,3.827608,8.721755,-2.450787,-9.002440,-5.649766,-5.126478,3.060348,-5.517005,2.389308,-5.085119,1.725157,4.202032,-1.002291,-4.474068,8.296108,4.813998,-0.620118,-6.832569,5.842220,0.112123,-4.986158,-7.772211,1.264071,-5.683664,2.322716,-4.132177,3.432574,0.982520,5.014811,2.726568,-9.060345,3.190730,3.149321,4.341966,-8.396089,-9.547060,8.669089,1.745728,-9.107264,3.571210,-2.281659,-9.736432,3.831195,6.161664,2.677429,6.591684,7.945319,-6.082579,2.778531,6.660887,9.338263,-0.373477,0.881368,0.834903,1.545301,8.961013,7.325732,0.898868,2.053963,7.856745,0.838225,-5.598751,-8.902369,9.129409,3.092507,8.523818,-3.603731,2.872488,8.454236,6.202250,8.515170,2.265393,-7.791258,8.487215,0.461928,-1.529165,3.739067,-8.137613,-7.259934,9.319742,-2.235205,-7.655895,-0.913088,-2.748215,-3.083782,-5.109879,-9.391484,-5.831321,-7.558979,7.946527,4.789646,-8.694014,-1.303086,-7.475422,-7.514085,-3.996588,-7.027013,-0.683253,-4.182573,8.234039,-4.724949,-1.406337,1.582137,-0.857107,-3.457007,8.710655,5.788984,7.478492,-9.749856,-7.701564,4.730091,-4.944331,9.855376,8.679719,5.961954,5.006013,-7.455834,6.185193,-9.177168,-3.175318,4.504387,-8.988769,6.480828,-1.803945,2.646136,0.560933,-2.792728,2.345752,-7.287264,6.997915,4.364069,4.309085,2.529945,8.536814,-0.654686,-9.243928,8.350421,2.001002,-6.196352,9.805205,-8.933409,2.960723,-5.773238,3.625817,4.040422,-7.921132,8.723462,-1.273840,-7.420895,-4.487270,4.208484,-8.352638,-1.351072,-4.958448,-3.559496,-4.206011,-6.930686,6.065510,-0.345259,4.571988,7.542229,-6.282332,9.986155,8.583078,-3.839491,1.855390,9.198194,3.271009,5.068677,-7.025607,9.122976,-4.440988,-6.968363,-1.194231,-4.630711,-0.314311,2.658797,-2.589308,-8.809712,7.526011,-2.146682,-0.653708,-6.412491,5.212220,0.713245,2.822732,-6.634695,-4.042101,9.810783,-4.379837,-2.555710,-7.107960,8.834523,9.445185,-5.093730,8.033597,4.630484,-3.694151,0.595381,8.519161,-5.047714,1.507904,-8.172576,4.461507,-1.061183,-1.459473,2.860690,-3.223418,1.404358,-6.896423,-5.623323,-3.526745,5.590997,-0.660749,-6.197500,-0.577510,-4.116219,-5.971127,0.412703,1.236233,6.202060,2.681254,-5.191301,1.202058,9.041267,7.996472,1.181034,4.297444,0.354965,3.997558,9.090621,-5.033749,9.509595,-5.998676,-0.529298,-0.543683,5.249928,-7.510251,-4.908591,-0.880394,5.933164,2.973131,6.782323,-7.519430,-9.343225,6.996734,9.695446,-8.608925,-2.817254,1.554524,-0.561358,-3.527270,2.636007,3.946229,-7.164585,1.294541,8.746742,0.542390,4.212987,2.448331,8.987865,6.220888,-9.481412,-5.680664,8.688207,-2.589949,0.732107,2.535663,7.302661,-6.323842,-8.645711,-7.828592,4.696662,1.063563,8.182899,-3.036556,7.511529,0.542918,7.161162,-5.622999,7.416408,-9.098096,5.579364,-5.521594,-2.240682,-6.903326,-9.575643,5.359858,-7.805038,3.968794,7.202488,8.841816,1.172451,6.625960,-8.071545,2.250092,-2.462282,-1.634572,-9.702304,-2.835895,-3.502159,2.927505,6.810060,-3.000191,8.087239,1.581053,6.951403,5.772161,8.009474,-1.330051,-5.685894,-5.135249,5.544221,-5.822149,8.817236,5.704675,-3.781149,-9.546903,5.030082,6.789344,-5.741790,8.537874,4.451391,5.002424,6.717172,-7.432330,5.282906,-0.514851,-1.440700,-6.012655,-2.084233,0.838040,0.836548,-8.501081,-1.143785,6.577762,2.222506,-3.174308,-3.496446,3.444770,3.769647,6.351522,-1.020906,-3.008008,5.945297,-2.583178,-0.366400,-0.881242,-0.072151,-5.528419,-5.220951,7.522096,-3.943900,7.151750,5.017221,5.214512,-2.815116,-4.982780,-5.683772,7.276526,5.480137,2.866866,5.497166,9.253815,7.681417,-9.269151,-3.904720,8.180998,-0.724637,6.355674,9.630246,-9.567936,8.889463,8.599253,7.171987,9.755619,-9.709027,-7.932575,-0.145299,6.030505,3.064066,-0.456543,-7.951457,4.083443,-5.134412,-9.397605,4.854408,0.856007,1.794602,-2.216412,-7.499871,-5.715120,1.056550,-9.859749,-5.304875,2.301711,-0.146943,6.115012,4.888997], dtype = "float32")#candidate|5793|(1014,)|const|float32
call_5790 = relay.TupleGetItem(func_4938_call(relay.reshape(const_5791.astype('int8'), [1056,]), relay.reshape(var_5792.astype('uint16'), [64,]), relay.reshape(const_5793.astype('float32'), [1014,]), ), 4)
call_5794 = relay.TupleGetItem(func_4942_call(relay.reshape(const_5791.astype('int8'), [1056,]), relay.reshape(var_5792.astype('uint16'), [64,]), relay.reshape(const_5793.astype('float32'), [1014,]), ), 4)
uop_5796 = relay.log10(const_5791.astype('float64')) # shape=(88, 12)
bop_5800 = relay.greater(uop_5796.astype('bool'), relay.reshape(const_5791.astype('bool'), relay.shape_of(uop_5796))) # shape=(88, 12)
var_5823 = relay.var("var_5823", dtype = "float64", shape = (88, 12))#candidate|5823|(88, 12)|var|float64
bop_5824 = relay.not_equal(uop_5796.astype('bool'), relay.reshape(var_5823.astype('bool'), relay.shape_of(uop_5796))) # shape=(88, 12)
uop_5830 = relay.atan(bop_5800.astype('float32')) # shape=(88, 12)
output = relay.Tuple([call_5785,call_5790,var_5792,const_5793,bop_5824,uop_5830,])
output2 = relay.Tuple([call_5786,call_5794,var_5792,const_5793,bop_5824,uop_5830,])
func_5835 = relay.Function([var_5792,var_5823,], output)
mod['func_5835'] = func_5835
mod = relay.transform.InferType()(mod)
mutated_mod['func_5835'] = func_5835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5835_call = mutated_mod.get_global_var('func_5835')
var_5837 = relay.var("var_5837", dtype = "uint16", shape = (64,))#candidate|5837|(64,)|var|uint16
var_5838 = relay.var("var_5838", dtype = "float64", shape = (88, 12))#candidate|5838|(88, 12)|var|float64
call_5836 = func_5835_call(var_5837,var_5838,)
output = call_5836
func_5839 = relay.Function([var_5837,var_5838,], output)
mutated_mod['func_5839'] = func_5839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5098_call = mod.get_global_var('func_5098')
func_5099_call = mutated_mod.get_global_var('func_5099')
call_5841 = func_5098_call()
call_5842 = func_5098_call()
func_2453_call = mod.get_global_var('func_2453')
func_2455_call = mutated_mod.get_global_var('func_2455')
const_5844 = relay.const([-0.313252,-0.394062,-0.532130,-5.289315,-2.539001,2.826310,-1.144279,8.113283,1.040268,-2.809065,1.390100,9.262424,9.235179,7.799622,-6.841437,-4.910759,-5.880459,-4.683441,-2.355519,-6.113157,4.901135,-7.429662,9.375266,7.118246,4.415840,9.657728,3.441144,-7.701332,3.561170,5.887113,7.835457,8.924075,-2.595214,6.739715,-4.835783,0.260480,5.086363,-0.993128,-6.347113,-6.838233,5.961347,-0.958284,-0.894939,3.661506,3.920007], dtype = "float32")#candidate|5844|(45,)|const|float32
call_5843 = func_2453_call(relay.reshape(const_5844.astype('float32'), [15, 3, 1]))
call_5845 = func_2453_call(relay.reshape(const_5844.astype('float32'), [15, 3, 1]))
bop_5862 = relay.logical_and(const_5844.astype('bool'), relay.reshape(call_5843.astype('bool'), relay.shape_of(const_5844))) # shape=(45,)
bop_5865 = relay.logical_and(const_5844.astype('bool'), relay.reshape(call_5845.astype('bool'), relay.shape_of(const_5844))) # shape=(45,)
func_1696_call = mod.get_global_var('func_1696')
func_1697_call = mutated_mod.get_global_var('func_1697')
call_5866 = func_1696_call()
call_5867 = func_1696_call()
output = relay.Tuple([call_5841,bop_5862,call_5866,])
output2 = relay.Tuple([call_5842,bop_5865,call_5867,])
func_5870 = relay.Function([], output)
mod['func_5870'] = func_5870
mod = relay.transform.InferType()(mod)
output = func_5870()
func_5871 = relay.Function([], output)
mutated_mod['func_5871'] = func_5871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4012_call = mod.get_global_var('func_4012')
func_4014_call = mutated_mod.get_global_var('func_4014')
call_5896 = relay.TupleGetItem(func_4012_call(), 0)
call_5897 = relay.TupleGetItem(func_4014_call(), 0)
output = call_5896
output2 = call_5897
func_5919 = relay.Function([], output)
mod['func_5919'] = func_5919
mod = relay.transform.InferType()(mod)
mutated_mod['func_5919'] = func_5919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5919_call = mutated_mod.get_global_var('func_5919')
call_5920 = func_5919_call()
output = call_5920
func_5921 = relay.Function([], output)
mutated_mod['func_5921'] = func_5921
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5927 = relay.const([[[-7,9,-8,-2,-1,8],[-7,3,7,-6,-1,-3],[-5,-9,6,-6,-10,10],[9,2,-7,9,7,9],[10,-3,10,-9,1,-9],[-5,-7,8,-4,-9,9],[7,10,-4,8,-6,4],[-8,-1,2,5,-5,-4]],[[-2,-1,5,9,-2,5],[-7,9,-7,9,7,-6],[10,-8,-6,9,3,10],[-2,9,7,-1,1,10],[-4,-3,1,-9,1,-5],[10,-4,3,-10,-3,10],[-6,-4,10,3,5,2],[5,4,-9,-2,4,-1]],[[-10,-4,1,-2,-5,-4],[-2,-9,-2,2,4,-3],[6,3,1,-9,-6,-5],[6,-6,8,8,-8,9],[-9,9,-7,-8,8,-5],[7,2,-6,4,6,5],[-1,-6,-1,1,3,3],[4,3,3,3,-1,-5]],[[3,10,-1,-5,-9,3],[5,-10,-6,8,-4,-2],[-8,-9,1,7,5,-5],[-6,9,1,-5,-6,5],[-8,1,-4,9,1,3],[3,-6,-9,7,1,-1],[7,-1,1,-6,8,10],[-4,6,-6,7,-8,10]],[[-4,-5,4,-9,1,6],[3,2,-3,3,-1,5],[7,1,-5,-5,9,-3],[-5,3,-10,10,5,7],[4,7,9,5,4,-3],[6,-7,7,5,10,-8],[1,4,-1,5,-10,-9],[6,7,9,-10,-8,-7]],[[5,-9,-1,7,-6,-7],[-3,10,-7,-4,-4,-5],[-3,-7,2,-7,5,-3],[-4,10,1,-7,-2,-8],[10,1,7,9,1,-10],[-10,-1,3,-1,2,7],[9,-10,2,9,1,8],[-8,-7,-2,3,6,-7]],[[7,7,9,5,-9,10],[-2,-5,-3,-3,1,1],[7,-5,9,1,10,-5],[2,-1,-6,4,4,-3],[2,7,3,7,3,2],[-4,7,-3,-4,-6,-5],[6,10,-1,-6,-8,8],[-10,-3,9,-6,-10,-6]],[[9,7,-3,-10,4,-10],[5,-9,6,6,2,-2],[7,-3,-4,10,-9,1],[-1,-2,10,-3,-7,-8],[10,10,3,3,1,-7],[-5,10,-5,-5,-1,5],[-10,-8,1,-9,-2,-2],[-2,-5,1,1,2,-1]],[[2,5,-4,9,-1,10],[-7,-10,9,-3,7,7],[3,-7,9,10,-3,-9],[7,10,6,-9,-10,-1],[-3,3,4,1,7,-2],[3,2,-9,4,10,6],[-5,-1,6,-5,6,-10],[-7,10,6,-2,4,-8]],[[4,10,5,2,-3,-6],[-2,-7,-8,-3,-5,-10],[-4,3,-6,-2,-2,-6],[10,-6,8,-9,2,3],[2,-4,8,1,6,-10],[4,7,-4,-4,1,-7],[-3,-3,2,-4,9,-3],[-2,9,-8,-2,-2,-10]],[[-2,-3,6,3,-4,-2],[-10,5,4,6,-2,-4],[5,7,-5,-4,-3,7],[6,-7,-6,-9,5,6],[1,7,-9,6,-9,3],[-9,-8,-3,10,-4,-2],[-5,-7,-6,-2,-8,-10],[2,-3,8,2,3,10]]], dtype = "uint8")#candidate|5927|(11, 8, 6)|const|uint8
var_5928 = relay.var("var_5928", dtype = "uint8", shape = (11, 8, 6))#candidate|5928|(11, 8, 6)|var|uint8
bop_5929 = relay.not_equal(const_5927.astype('bool'), relay.reshape(var_5928.astype('bool'), relay.shape_of(const_5927))) # shape=(11, 8, 6)
uop_5939 = relay.atan(bop_5929.astype('float64')) # shape=(11, 8, 6)
uop_5941 = relay.sqrt(uop_5939.astype('float64')) # shape=(11, 8, 6)
uop_5948 = relay.atanh(uop_5939.astype('float32')) # shape=(11, 8, 6)
output = relay.Tuple([uop_5941,uop_5948,])
output2 = relay.Tuple([uop_5941,uop_5948,])
func_5954 = relay.Function([var_5928,], output)
mod['func_5954'] = func_5954
mod = relay.transform.InferType()(mod)
var_5955 = relay.var("var_5955", dtype = "uint8", shape = (11, 8, 6))#candidate|5955|(11, 8, 6)|var|uint8
output = func_5954(var_5955)
func_5956 = relay.Function([var_5955], output)
mutated_mod['func_5956'] = func_5956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_5981 = relay.TupleGetItem(func_4154_call(), 0)
call_5982 = relay.TupleGetItem(func_4155_call(), 0)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_6001 = relay.TupleGetItem(func_3396_call(), 0)
call_6002 = relay.TupleGetItem(func_3398_call(), 0)
output = relay.Tuple([call_5981,call_6001,])
output2 = relay.Tuple([call_5982,call_6002,])
func_6009 = relay.Function([], output)
mod['func_6009'] = func_6009
mod = relay.transform.InferType()(mod)
mutated_mod['func_6009'] = func_6009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mutated_mod.get_global_var('func_6009')
call_6010 = func_6009_call()
output = call_6010
func_6011 = relay.Function([], output)
mutated_mod['func_6011'] = func_6011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_6059 = relay.TupleGetItem(func_4250_call(), 1)
call_6060 = relay.TupleGetItem(func_4251_call(), 1)
var_6068 = relay.var("var_6068", dtype = "float64", shape = (5, 8, 5))#candidate|6068|(5, 8, 5)|var|float64
bop_6069 = relay.minimum(call_6059.astype('uint8'), var_6068.astype('uint8')) # shape=(5, 8, 5)
bop_6072 = relay.minimum(call_6060.astype('uint8'), var_6068.astype('uint8')) # shape=(5, 8, 5)
func_1770_call = mod.get_global_var('func_1770')
func_1772_call = mutated_mod.get_global_var('func_1772')
const_6075 = relay.const([-5,-7,10,8,-7,2,9,4,7,-1,-10,-7,-8,-7,2,-6,-5,-5,-10,-8,8,-10,5,6,-4,3,2,10,10,-6,5,9,-4,8,-1,-10,6,5,-3,-7,8,3,-2,1,-4,4,8,9,10,-7,-4,10,-8,-3,-6,10,-2,7,9,6,6,1,5,-7], dtype = "uint16")#candidate|6075|(64,)|const|uint16
call_6074 = func_1770_call(relay.reshape(const_6075.astype('uint16'), [2, 2, 16]))
call_6076 = func_1770_call(relay.reshape(const_6075.astype('uint16'), [2, 2, 16]))
func_1376_call = mod.get_global_var('func_1376')
func_1380_call = mutated_mod.get_global_var('func_1380')
var_6089 = relay.var("var_6089", dtype = "float32", shape = (280,))#candidate|6089|(280,)|var|float32
const_6090 = relay.const([[-9.464142],[-1.743395],[-7.099816],[-2.947991],[-9.993853],[7.725921],[-5.367337],[-5.060186],[0.634151],[5.400408],[1.326987],[-0.821742],[2.907728],[6.464881],[-0.511887],[-4.011774],[-8.306667],[8.554603],[6.530652],[4.693213],[-2.070375],[5.974318],[-1.022782],[-6.702507],[1.579540],[-4.809738],[-0.164393],[3.946989],[-2.984560],[1.979275],[6.217620],[-0.666925],[6.541129],[-9.716912],[0.851547],[-0.742942],[-6.591695],[-4.890961],[-5.303870],[-9.984151],[9.258934],[-2.123067],[0.679541],[0.913133],[-7.880482],[8.386073],[-2.464401],[0.015866],[9.088000],[-9.716426],[-9.956891],[-7.331350],[0.439672],[0.705425],[-2.495711],[3.712295],[4.229592],[4.772848],[2.760533],[-1.031684],[5.518196],[3.948624],[5.983941],[1.804649],[-7.763088],[3.783119],[0.203688],[0.508007],[1.671268],[-2.200671],[6.388187],[1.073107],[5.775280],[0.379148],[1.087079],[4.511153],[9.622479],[-8.322333],[9.355753],[-0.945563],[1.290333],[-8.769424],[3.445345],[0.915154],[7.527503],[-9.622755],[0.238431],[5.739663],[-7.297472],[-7.199803],[-0.008143],[4.459541],[-1.343468],[2.164090],[9.827772],[-4.858144],[2.563235],[8.416719],[-1.019933],[9.024011],[-5.875397],[-4.234722],[4.485349],[3.620574],[4.593455],[3.615643],[5.775977],[2.925240],[-9.536532],[2.325522],[-4.143469],[5.464471],[1.876777],[0.496963],[9.563779],[1.240038],[-1.129453],[-7.004325],[5.306931],[-7.099592],[7.263721],[-5.879229],[-4.492048],[-5.020831],[-1.524267],[-0.539357],[9.300811],[4.871696],[4.155791],[8.468285],[3.452983],[-5.928024],[-2.876694],[-0.494809],[-5.569458],[-7.736612],[-2.309724],[-2.471398],[2.094474],[-5.830579],[4.708978],[-0.879979],[-0.019973],[1.347849],[-6.779853],[-2.058134],[5.111316],[-4.294205],[9.133858],[2.728417],[0.093796],[6.514785],[-8.118269],[-7.669243],[2.452308],[-5.761973],[8.975177],[8.011663],[-4.212731],[3.026489],[9.191887],[-2.976082],[6.881461],[6.125529],[1.639710],[-3.325243],[-6.756723],[8.647593],[-3.898697],[-3.683529],[-4.732972],[-6.193013],[-3.605112],[7.337772],[-5.079070],[7.091744],[-8.412330],[-0.791356],[-7.237945],[4.134876],[-5.230498],[-2.642996],[7.421279],[8.934725],[7.104418],[9.169323],[-9.587329],[-0.585789],[-1.497050],[4.338894],[-9.146010],[-2.042603],[4.025982],[-5.956685],[-7.059993],[8.029611],[-7.355450],[-6.165722],[4.589766],[2.343344],[3.492330],[-1.822949],[-7.098152],[-8.923693],[-4.021796],[2.513705],[5.722189],[-0.598948],[-9.021314],[-6.810027],[-7.831847],[2.188167],[-1.515969],[-7.267066],[2.727784],[-6.051267],[1.382210],[2.482519],[2.334012],[-2.822966],[3.059364],[6.482518],[8.269974],[0.921170],[-2.601738],[2.168702],[-8.503010],[6.031380],[-6.679277],[-3.134913],[8.246629],[-9.280188],[-8.856473],[-3.981676],[-0.362998],[8.989652],[-7.012152],[-2.206446],[-9.133101],[0.003988],[9.101102],[2.972514],[0.994911],[-4.228543],[8.368274],[-8.493504],[-7.765775],[1.935007],[-7.958036],[-0.817930],[-3.940297],[-3.262262],[-8.758452],[-5.717932],[8.529792],[-3.906810],[-0.393532],[-5.915248],[-0.157633],[6.227339],[3.780484],[9.509159],[7.094794],[-6.432382],[-1.465650],[-1.609113],[6.542375],[-1.478415],[7.671455],[-5.918381],[-8.029665],[6.804090],[7.586178],[5.272359],[3.744360],[5.153522],[-2.436453],[-9.267420],[1.085177],[5.581261],[5.543026],[-5.968801],[-2.593865],[4.023159],[3.643984],[-5.946373],[-7.987712],[6.235348],[8.177536],[9.089803],[6.246574],[-7.952619],[6.259970],[7.110230],[5.499929],[4.799139],[-6.072157],[3.904233],[-8.687678],[-9.007479],[3.503681],[7.937002],[6.008517],[8.496621],[3.818260],[1.228161],[1.120342],[-2.898860],[-8.901323],[3.481190],[-6.590026],[-4.291904],[-2.694795],[-7.565989],[-7.190492],[-1.856301],[1.968722],[0.445965],[-1.876258],[-4.940321],[-1.916375],[1.084704],[5.712991],[-3.281229],[7.875882],[3.705314],[-3.532464],[2.668784],[-8.924756],[3.029315],[-9.528927],[-9.069894],[-8.251940],[-1.589364],[-7.932544],[-2.604165],[-6.358000],[-4.142906],[-1.982613],[6.446552],[-7.077473],[7.914816],[0.580531],[7.882462],[-7.859003],[-1.733137],[-1.665044],[6.517215],[4.284573],[-6.159571],[-0.709044],[-3.289972],[-8.183851],[-2.575935],[4.784989],[-3.981087],[-5.442819],[7.113191],[-1.378759],[1.385498],[7.063385],[-8.341578],[-0.152028],[-0.582915],[0.628018],[8.243008],[-5.295842],[4.692178],[-6.634559],[9.314531],[7.395098],[1.254795],[7.175984],[5.093669],[5.852556],[1.170976],[8.186563],[2.995890],[3.733364],[9.665907],[-9.311762],[-0.358507],[-8.590635],[7.358911],[6.716034],[-3.180756],[-4.187076],[-0.969665],[-5.085984],[-5.212112],[8.992715],[6.540141],[4.365408],[-4.565426],[-4.939589],[3.859906],[5.498353],[1.765232],[2.346445],[-9.666511],[6.352599],[-4.035706],[4.815865],[-4.748144],[-0.054219],[7.674967],[-7.710925],[-5.710452],[7.356447],[-6.557655],[-4.771942],[-2.609543],[2.530290],[2.373779],[-9.755003],[1.447806],[1.382473],[-1.844839],[-1.211493],[-5.006428],[8.590411],[-4.797080],[-6.507948],[8.658417],[-0.229199],[-7.859439],[1.376682],[-0.195000],[-5.867162],[-0.657991],[8.654567],[7.371349],[0.616512],[6.436511],[-3.651437],[-9.076853],[-8.308633],[4.343461],[-5.346659],[-8.058894],[-6.071277],[0.837733],[-9.479698],[-2.899344],[-6.381314],[8.556940],[-7.542300],[-5.133594],[-0.401429],[7.987257],[7.143831],[-6.825190],[6.280423],[6.336826],[-2.240234],[-2.754945],[-3.220519],[1.420312],[9.704760],[9.415269],[-4.766694],[3.565376],[4.369822],[-2.970192],[-0.598437],[-8.778871],[2.413788],[6.215348],[-6.272775],[-4.865944],[-1.025737],[2.867805],[9.723325],[6.283063],[-7.770508],[-3.760181],[-3.516867],[7.403949],[0.343486],[0.653296],[-3.102512],[7.718149],[3.363749],[-6.397341],[5.054113],[-5.920366],[7.807391],[-3.002187],[-2.652750],[2.743551],[3.460413],[7.291294],[7.092960],[0.937238],[-2.764412],[-0.826366],[7.609909],[0.219712],[-2.621630],[-7.305449],[-1.452434],[-1.298051],[3.396614],[-6.491371],[-4.837842],[-6.601148],[3.745520],[8.130270],[1.336705],[3.852984],[-2.252925],[-2.960267],[-3.932713],[-8.964957],[0.552857],[-3.865280],[8.825282],[7.736019],[-8.753799],[5.020691],[4.702634],[-4.005939],[2.768402],[4.578161],[-9.005164],[9.168945],[2.814787],[-1.212576],[5.339501],[-9.965584],[-3.739529],[-7.022475],[9.926609],[-9.802279],[-9.379140],[8.036098],[9.843530],[-1.854384],[3.344950],[3.685809],[0.626517],[-5.706950],[-3.379830],[-5.144947],[4.761685],[-7.031210],[3.222955],[-6.931423],[-2.138697],[-5.393974],[-7.535612],[-3.073397],[4.605225],[-0.264578],[9.188585],[1.604624],[-6.613758],[5.979324],[-4.151525],[-8.056096],[-9.514055],[8.911925],[-8.693948],[5.460738],[-1.650235],[7.251785],[2.378495],[5.618113],[-3.528561],[4.926331],[2.141570],[-7.469957],[3.019261],[1.780464],[5.384513],[4.743660],[-7.311339],[-4.613908],[-3.436441],[-4.252445],[8.749653],[9.899863],[6.709058],[-3.797408],[6.494520],[0.794402],[-8.824820],[-8.670196],[4.594968],[1.851797],[-0.780536],[6.734482],[-1.068606],[9.802961],[0.651525],[5.918072],[2.241935],[1.602934],[5.425955],[-8.300925],[5.373178],[-4.456223],[-5.617544],[9.713057],[-3.423275],[-4.111382],[-8.360475],[0.382079],[0.869783],[5.445872],[-5.388150],[-4.385715],[-7.058352],[1.414828],[8.101815],[-4.865258],[0.040530],[-0.551647],[1.799765],[-8.813246],[-3.776585],[-0.907102],[-2.296666],[3.776218],[-5.865551],[-2.051820],[-2.863038],[-9.304550],[-7.792613],[-9.938113],[-0.699242],[-2.849255],[0.318328],[4.328215],[9.563384],[-4.447641],[-2.440499],[-5.998484],[2.686746],[2.715607],[-4.530890],[-8.378614],[-9.840098],[1.960126],[-5.400129],[-5.343025],[-0.318834],[9.993423],[6.236080],[8.670103],[-2.821881],[-9.900353],[-3.941497],[3.924287],[3.290227],[-3.520552],[-6.068324],[-5.670862],[6.789951],[7.748945]], dtype = "float64")#candidate|6090|(660, 1)|const|float64
const_6091 = relay.const([[-10,4,2,-7,5,9,-4,-9,2,1,4,9,-10,-6,9,-8,5,-4,4,-3,9,-4,-6,4,-6,-5,-9,-2,9,8,8,-6,-7,-1,2,-1,5,-3,-2,-10,-4,-1,-7,-3,-3,-6,-6,5,5,-6,9,9,5,-4,1,-7,6,7,3,2,9,-8,-10,-10,-8,-1,4,-10,2,-9,-7,-7,4,-8,5,2,8,9,-2,3,5,-6,4,1,-9,8,-5,-1,-10,-6,9,-9,8,2,-8,10,9,-4,2,-8,6,-7,10,1,-6,-6,-3,-9,4,-10,8,-10,6,1,-1,-8,-4,9,-2,-7,5,3,-8,-10,-8,9,-10,5,2,1,5,-10,4,-5,8,-7,5,3,-4,8,-5,8,-5,-9,-8,-8,-2,6,-8,2,-4,8,-9,-5,-8,-3,-9,6,3,-10,-8,8,7,-5,6,10,6,-9,1,-8,-4,-1,1,8,-5,-8,9,4,-1,-2,6,-5,9,9,-8,10,7,7,-1,3,5,10,1,-1,-4,-9,4,3,10,7,9,9,1,4,-3,7,-10,4,-2,4,-8,6,-9,-5,-3,6,-2,-5,-1,2,-6,3,-7,-9,-2,4,-8,-3,-1,5,-1,-3,-5,5,-9,-9,-7,3,1,-6,9,-4,10,3,6,-5,-10,-1,9,1,2,-3,4,6,9,8,-1,4,-10,5,6,4,-8,-1,10,3,1,2,1,3,-9,8,5,-3,9,-10,8,1,8,3,1,1,-3,9,2,-5,-3,3,7,3,-6,10,-9,-1,10,-5,3,5,9,-1,-8,-4,-1,8,-4,3,6,-5,-6,-1,2,9,4,-9,-10,5,-7,8,7,8,-9,-1,-6,-1,1,-9,10,8,4,8,-10,-3,-4,-6,8,-2,5,-5,10,-3,8,5,4,3,-3,-3,5,-9,-8,2,1,5,9,-6,6,1,-5,-1,2,-6,-4,-5,4,10,10,-8,-7,-6,-4,7,-4,-3,7,-8,5,-1,3,-8,1,-1,-1,10,3,-6,8,9,4,-3,-4,-9,6,-10,7,8,-7,6,7,5,2,8,-5,-4,-9,-9,9,-3,-9,4,2,-1,-2,-4,5,-2,1,8,7,4,-10,-8,-2,-2,6,6,-1,-7,-5,5,-2,-6,-6,-8,6,-8,8,5,-9,-10,4,-4,-4,9,4,7,10,-9,-10,7,1,-4,3,9,-6,-8,-7,-9,-3,-8,4,-5,1,-9,10,-8,-3,-10,-10,8,-9,10,9,7,-8,1,2,-4,-7,-5,1,10,4,2,-10,-3,5,7,1,-7,10,-8,-3,7,-7,9,-8,4,10,7,6,-10,-3,6,2,-2,-9,-7,5,2,-8,2,1,-7,3,10,-6,-2,-9,3,-2,-4,-5,5,4,-4,10,8,3,2],[-1,-9,3,4,-2,3,-1,-6,5,8,1,-2,9,4,-5,-2,-9,1,-2,5,-3,-7,5,-3,-5,2,5,6,-3,-8,7,5,10,-9,5,6,4,4,-5,2,10,-5,-7,10,3,8,-9,7,3,4,2,7,1,5,-10,7,10,-8,-7,5,-8,2,-8,-9,-7,-10,-2,6,8,-1,-10,-10,-4,-5,7,-1,-5,-4,-3,5,-5,10,-1,3,10,8,6,-10,6,-1,7,10,6,6,-7,1,7,-1,10,8,10,1,5,6,7,6,1,8,10,-7,5,10,9,-10,7,-8,5,-3,-9,4,6,1,-8,5,3,6,7,-1,9,-3,9,-1,1,5,-3,-7,10,6,-7,7,-10,9,1,4,-9,-4,10,-3,9,2,-8,3,-9,8,-10,7,10,-9,-3,-10,-4,3,10,-5,-7,-5,6,-4,6,2,-9,-6,-4,-1,-8,1,5,-5,3,6,-9,-4,-8,1,-10,-8,1,-7,8,1,-9,9,-8,9,-6,-1,7,-1,2,8,4,-1,9,1,-6,-5,-7,-6,-9,-8,1,10,-5,-2,-3,-8,-6,6,-7,-5,9,5,-4,-3,-10,-8,10,-1,-10,-1,5,2,8,-9,2,5,3,7,5,-10,1,-7,7,8,-3,10,10,-9,9,3,-3,-5,2,-4,4,-1,-4,-7,-6,-6,-6,7,10,4,6,-3,8,5,-1,-7,3,-9,-6,-7,3,-1,2,5,-6,3,8,2,5,-6,-6,-3,-10,-7,-1,1,10,1,2,5,-6,-1,-4,8,2,-8,-6,-1,-3,3,5,-8,-5,-8,-6,4,-9,4,-10,5,-8,-2,3,-9,2,-2,5,3,-8,7,-1,-4,8,8,-2,-9,5,3,5,-6,-5,3,6,-1,6,-8,9,-9,-10,6,-1,2,-6,-4,6,-7,8,-2,5,-9,-9,8,-9,-8,8,-2,-9,-5,-9,8,-10,-6,-7,3,2,-5,-10,-3,-3,-9,3,8,-8,-8,3,-2,-1,1,7,-1,7,1,8,6,3,2,9,-9,-4,-1,1,2,-2,-9,7,9,6,1,4,-5,1,4,-9,4,-9,2,8,3,7,10,-4,7,-9,-3,-4,-1,-8,-6,7,2,-6,-8,-8,-6,-3,-10,3,6,-6,4,-9,-8,1,6,5,-6,4,-7,4,-9,10,-3,-7,-5,-8,-6,8,-6,9,7,-1,4,6,2,-7,-7,10,-9,1,-3,-5,-7,-4,-9,6,6,-8,7,-4,-6,-9,5,4,-10,8,-5,-2,-7,5,7,4,1,4,8,4,-8,-6,4,-6,7,8,8,-4,6,3,-3,9,-8,9,-2,9,-7,4,7,8,6,3,7,9,9,1,8,5,4,2,-8,-5,-6,-10,10,6,-5,-10,-8]], dtype = "int8")#candidate|6091|(2, 528)|const|int8
call_6088 = relay.TupleGetItem(func_1376_call(relay.reshape(var_6089.astype('float32'), [7, 10, 4]), relay.reshape(const_6090.astype('float64'), [660,]), relay.reshape(const_6091.astype('int8'), [1056,]), ), 0)
call_6092 = relay.TupleGetItem(func_1380_call(relay.reshape(var_6089.astype('float32'), [7, 10, 4]), relay.reshape(const_6090.astype('float64'), [660,]), relay.reshape(const_6091.astype('int8'), [1056,]), ), 0)
output = relay.Tuple([bop_6069,call_6074,const_6075,call_6088,var_6089,const_6090,const_6091,])
output2 = relay.Tuple([bop_6072,call_6076,const_6075,call_6092,var_6089,const_6090,const_6091,])
func_6100 = relay.Function([var_6068,var_6089,], output)
mod['func_6100'] = func_6100
mod = relay.transform.InferType()(mod)
mutated_mod['func_6100'] = func_6100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6100_call = mutated_mod.get_global_var('func_6100')
var_6102 = relay.var("var_6102", dtype = "float64", shape = (5, 8, 5))#candidate|6102|(5, 8, 5)|var|float64
var_6103 = relay.var("var_6103", dtype = "float32", shape = (280,))#candidate|6103|(280,)|var|float32
call_6101 = func_6100_call(var_6102,var_6103,)
output = call_6101
func_6104 = relay.Function([var_6102,var_6103,], output)
mutated_mod['func_6104'] = func_6104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1427_call = mod.get_global_var('func_1427')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_6129 = relay.TupleGetItem(func_1427_call(), 2)
call_6130 = relay.TupleGetItem(func_1428_call(), 2)
func_3907_call = mod.get_global_var('func_3907')
func_3908_call = mutated_mod.get_global_var('func_3908')
call_6137 = func_3907_call()
call_6138 = func_3907_call()
bop_6140 = relay.bitwise_xor(call_6129.astype('int64'), call_6137.astype('int64')) # shape=(5, 8, 1056)
bop_6143 = relay.bitwise_xor(call_6130.astype('int64'), call_6138.astype('int64')) # shape=(5, 8, 1056)
func_3982_call = mod.get_global_var('func_3982')
func_3987_call = mutated_mod.get_global_var('func_3987')
var_6146 = relay.var("var_6146", dtype = "float64", shape = (660,))#candidate|6146|(660,)|var|float64
const_6147 = relay.const([-7.021027,-8.141616,-9.259273,-3.505909,3.314207,-0.027600,-3.285954,4.090471,1.503006,7.119270,-6.681483,1.942178,2.593516,9.905325,0.728012,6.188996,6.401239,-4.775665,7.704601,6.162481,-7.723000,7.972990,-4.755749,-0.945212,-9.885033,6.189325,7.636774,2.877606,1.692713,9.898884,0.695550,-3.698463,6.813450,-1.728788,6.570140,1.718868,4.476290,-7.832778,0.167315,1.038653,8.296417,4.653002,-3.113915,6.240059,4.586703,-5.322603,-1.411224,3.508265,9.340492,-8.201385,3.870635,-2.125900,-9.136926,5.898715,9.941964,-1.745212,5.582236,-0.923155,-1.596768,2.169474,-1.499268,-7.311664,-7.429307,-8.410464,-1.547983,-2.741630,5.739398,-8.901837,-6.462965,3.118827,9.469110,-6.386153,4.954101,-9.070488,-3.896232,2.202458,1.538471,6.266703,6.228747,-4.205980,-9.040808,-6.731865,9.577440,-0.716671,-4.807960,-2.796222,0.128012,-1.555017,1.331434,-7.440338,2.277734,-5.359516,-1.782175,-0.425453,-8.611600,2.751423,-1.473758,-0.029068,-1.784437,6.006949,-6.385229,-2.894295,-9.722401,3.382173,1.004089,0.774311,3.103841,-8.555489,-9.834690,-3.308403,5.806168,4.321595,8.289999,6.769635,-8.740975,-4.574535,-0.003257,-0.908470,2.048742,-0.962572,-5.319966,8.424576,-3.392666,5.029304,3.674399,0.716786,2.378548,-8.322866,-9.881160,-0.980203,-4.016194,5.208572,-1.778986,4.464728,6.053693,-1.289736,5.344666,-6.951214,6.449402,-3.289731,2.474453,4.455982,0.520227,6.321371,-2.656408,-9.178808,-8.004127,9.948727,-3.224996,-6.718820,8.034795,1.855879,9.437461,-4.586663,1.858790,7.986908,-8.403621,8.019788,-8.471468,8.143069], dtype = "float64")#candidate|6147|(160,)|const|float64
call_6145 = relay.TupleGetItem(func_3982_call(relay.reshape(call_6129.astype('int8'), [1056,]), relay.reshape(var_6146.astype('float64'), [660,]), relay.reshape(const_6147.astype('float64'), [16, 10]), ), 1)
call_6148 = relay.TupleGetItem(func_3987_call(relay.reshape(call_6129.astype('int8'), [1056,]), relay.reshape(var_6146.astype('float64'), [660,]), relay.reshape(const_6147.astype('float64'), [16, 10]), ), 1)
func_4614_call = mod.get_global_var('func_4614')
func_4615_call = mutated_mod.get_global_var('func_4615')
call_6156 = relay.TupleGetItem(func_4614_call(), 0)
call_6157 = relay.TupleGetItem(func_4615_call(), 0)
func_5535_call = mod.get_global_var('func_5535')
func_5537_call = mutated_mod.get_global_var('func_5537')
call_6160 = relay.TupleGetItem(func_5535_call(), 0)
call_6161 = relay.TupleGetItem(func_5537_call(), 0)
uop_6166 = relay.sin(bop_6140.astype('float64')) # shape=(5, 8, 1056)
uop_6168 = relay.sin(bop_6143.astype('float64')) # shape=(5, 8, 1056)
output = relay.Tuple([call_6145,var_6146,const_6147,call_6156,call_6160,uop_6166,])
output2 = relay.Tuple([call_6148,var_6146,const_6147,call_6157,call_6161,uop_6168,])
func_6174 = relay.Function([var_6146,], output)
mod['func_6174'] = func_6174
mod = relay.transform.InferType()(mod)
var_6175 = relay.var("var_6175", dtype = "float64", shape = (660,))#candidate|6175|(660,)|var|float64
output = func_6174(var_6175)
func_6176 = relay.Function([var_6175], output)
mutated_mod['func_6176'] = func_6176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6208 = relay.var("var_6208", dtype = "float32", shape = (16, 3, 4))#candidate|6208|(16, 3, 4)|var|float32
const_6209 = relay.const([[[8.519335,2.439291,3.721919,9.203144],[1.822051,5.400470,-8.004101,3.877773],[-5.498387,2.109557,-7.455431,-9.536912]],[[-3.633278,6.311676,-0.857930,-0.902978],[0.264823,9.675951,-1.859591,-0.274322],[-3.978074,1.976297,-5.368699,-3.235670]],[[-7.154441,5.813572,7.018524,-8.649051],[-2.164350,-7.480060,-6.853483,-7.524098],[-7.700267,-7.697583,1.295240,6.757568]],[[-7.171077,-5.171561,2.243694,4.362504],[7.909861,8.128574,-5.534239,-6.093888],[0.557931,1.092747,6.066945,4.479120]],[[-1.770656,-8.124682,-8.761722,5.009572],[1.936771,-2.865248,-1.611973,-9.048858],[-6.739169,-5.843460,-7.713469,-5.947111]],[[3.917985,6.601418,0.907710,7.630732],[8.756506,3.063007,7.985706,-2.747738],[6.549508,3.605140,3.571022,9.961581]],[[2.576541,-8.839566,-8.468390,8.872482],[6.238513,5.936709,8.753509,-1.397330],[-6.164855,4.879287,-5.432051,-0.614933]],[[-9.015377,-4.113963,-6.095459,1.077973],[5.407372,4.716279,-0.629810,-2.995969],[2.887527,3.975318,-0.010226,3.734719]],[[7.719894,-8.926738,1.954819,2.001113],[-6.642450,5.092894,6.951405,6.750541],[-2.694847,8.606536,2.720230,-6.078363]],[[8.321122,-5.106961,6.285554,-5.061728],[-0.390783,7.216354,-2.658093,4.784731],[-5.335197,8.171129,7.811170,-7.943531]],[[6.609655,8.256224,5.764633,8.350568],[6.959493,-7.535771,-7.449226,7.854423],[2.613258,-9.259116,-0.801181,0.816784]],[[-4.376178,-3.105213,2.413393,0.105409],[-1.070131,7.639376,3.866352,-8.414449],[-3.607615,4.281156,-2.828167,4.923042]],[[5.650873,8.614219,1.244180,-1.497902],[4.974604,-1.603003,-6.327060,9.765370],[-2.881524,-2.402406,0.422954,-8.564850]],[[-2.920021,-3.360856,-4.594496,-9.188633],[5.833425,7.159980,-0.002498,-7.120975],[2.406495,-4.837452,1.553308,-9.000527]],[[9.970736,7.532733,-4.143942,-7.649356],[5.583746,4.275097,2.780363,-3.997894],[9.652061,1.677993,0.703364,9.193403]],[[-3.558406,-0.642133,1.917213,8.866442],[-9.462125,9.331765,-5.122051,8.684855],[6.193548,-9.626853,-2.915302,5.548762]]], dtype = "float32")#candidate|6209|(16, 3, 4)|const|float32
bop_6210 = relay.floor_mod(var_6208.astype('float32'), relay.reshape(const_6209.astype('float32'), relay.shape_of(var_6208))) # shape=(16, 3, 4)
output = bop_6210
output2 = bop_6210
func_6222 = relay.Function([var_6208,], output)
mod['func_6222'] = func_6222
mod = relay.transform.InferType()(mod)
var_6223 = relay.var("var_6223", dtype = "float32", shape = (16, 3, 4))#candidate|6223|(16, 3, 4)|var|float32
output = func_6222(var_6223)
func_6224 = relay.Function([var_6223], output)
mutated_mod['func_6224'] = func_6224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2190_call = mod.get_global_var('func_2190')
func_2191_call = mutated_mod.get_global_var('func_2191')
call_6247 = relay.TupleGetItem(func_2190_call(), 2)
call_6248 = relay.TupleGetItem(func_2191_call(), 2)
func_2781_call = mod.get_global_var('func_2781')
func_2782_call = mutated_mod.get_global_var('func_2782')
call_6256 = func_2781_call()
call_6257 = func_2781_call()
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_6259 = relay.TupleGetItem(func_3682_call(), 0)
call_6260 = relay.TupleGetItem(func_3684_call(), 0)
output = relay.Tuple([call_6247,call_6256,call_6259,])
output2 = relay.Tuple([call_6248,call_6257,call_6260,])
func_6270 = relay.Function([], output)
mod['func_6270'] = func_6270
mod = relay.transform.InferType()(mod)
output = func_6270()
func_6271 = relay.Function([], output)
mutated_mod['func_6271'] = func_6271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_6292 = relay.TupleGetItem(func_4154_call(), 1)
call_6293 = relay.TupleGetItem(func_4155_call(), 1)
var_6300 = relay.var("var_6300", dtype = "float64", shape = (5, 8, 3))#candidate|6300|(5, 8, 3)|var|float64
bop_6301 = relay.maximum(call_6292.astype('int64'), var_6300.astype('int64')) # shape=(5, 8, 3)
bop_6304 = relay.maximum(call_6293.astype('int64'), var_6300.astype('int64')) # shape=(5, 8, 3)
func_3795_call = mod.get_global_var('func_3795')
func_3796_call = mutated_mod.get_global_var('func_3796')
call_6306 = relay.TupleGetItem(func_3795_call(), 0)
call_6307 = relay.TupleGetItem(func_3796_call(), 0)
func_1968_call = mod.get_global_var('func_1968')
func_1969_call = mutated_mod.get_global_var('func_1969')
call_6315 = func_1968_call()
call_6316 = func_1968_call()
output = relay.Tuple([bop_6301,call_6306,call_6315,])
output2 = relay.Tuple([bop_6304,call_6307,call_6316,])
func_6321 = relay.Function([var_6300,], output)
mod['func_6321'] = func_6321
mod = relay.transform.InferType()(mod)
mutated_mod['func_6321'] = func_6321
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6322 = relay.var("var_6322", dtype = "float64", shape = (5, 8, 3))#candidate|6322|(5, 8, 3)|var|float64
func_6321_call = mutated_mod.get_global_var('func_6321')
call_6323 = func_6321_call(var_6322)
output = call_6323
func_6324 = relay.Function([var_6322], output)
mutated_mod['func_6324'] = func_6324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5153_call = mod.get_global_var('func_5153')
func_5154_call = mutated_mod.get_global_var('func_5154')
call_6348 = relay.TupleGetItem(func_5153_call(), 0)
call_6349 = relay.TupleGetItem(func_5154_call(), 0)
func_1900_call = mod.get_global_var('func_1900')
func_1901_call = mutated_mod.get_global_var('func_1901')
call_6353 = func_1900_call()
call_6354 = func_1900_call()
func_5490_call = mod.get_global_var('func_5490')
func_5492_call = mutated_mod.get_global_var('func_5492')
call_6363 = relay.TupleGetItem(func_5490_call(), 0)
call_6364 = relay.TupleGetItem(func_5492_call(), 0)
func_2453_call = mod.get_global_var('func_2453')
func_2455_call = mutated_mod.get_global_var('func_2455')
var_6374 = relay.var("var_6374", dtype = "float32", shape = (45,))#candidate|6374|(45,)|var|float32
call_6373 = func_2453_call(relay.reshape(var_6374.astype('float32'), [15, 3, 1]))
call_6375 = func_2453_call(relay.reshape(var_6374.astype('float32'), [15, 3, 1]))
output = relay.Tuple([call_6348,call_6353,call_6363,call_6373,var_6374,])
output2 = relay.Tuple([call_6349,call_6354,call_6364,call_6375,var_6374,])
func_6381 = relay.Function([var_6374,], output)
mod['func_6381'] = func_6381
mod = relay.transform.InferType()(mod)
var_6382 = relay.var("var_6382", dtype = "float32", shape = (45,))#candidate|6382|(45,)|var|float32
output = func_6381(var_6382)
func_6383 = relay.Function([var_6382], output)
mutated_mod['func_6383'] = func_6383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_6452 = relay.TupleGetItem(func_4154_call(), 0)
call_6453 = relay.TupleGetItem(func_4155_call(), 0)
output = call_6452
output2 = call_6453
func_6475 = relay.Function([], output)
mod['func_6475'] = func_6475
mod = relay.transform.InferType()(mod)
mutated_mod['func_6475'] = func_6475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6475_call = mutated_mod.get_global_var('func_6475')
call_6476 = func_6475_call()
output = call_6476
func_6477 = relay.Function([], output)
mutated_mod['func_6477'] = func_6477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4647_call = mod.get_global_var('func_4647')
func_4649_call = mutated_mod.get_global_var('func_4649')
call_6520 = relay.TupleGetItem(func_4647_call(), 1)
call_6521 = relay.TupleGetItem(func_4649_call(), 1)
output = call_6520
output2 = call_6521
func_6526 = relay.Function([], output)
mod['func_6526'] = func_6526
mod = relay.transform.InferType()(mod)
output = func_6526()
func_6527 = relay.Function([], output)
mutated_mod['func_6527'] = func_6527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2728_call = mod.get_global_var('func_2728')
func_2730_call = mutated_mod.get_global_var('func_2730')
call_6531 = func_2728_call()
call_6532 = func_2728_call()
func_481_call = mod.get_global_var('func_481')
func_486_call = mutated_mod.get_global_var('func_486')
var_6581 = relay.var("var_6581", dtype = "float64", shape = (660, 1))#candidate|6581|(660, 1)|var|float64
const_6582 = relay.const([-7,-10,10,5,1,-6,3,-10,1,3,6,10,4,2,-4,-9,-3,9,-9,3,4,-2,9,10,-9,-1,10,4,1,-7,-10,7,-7,7,1,-7,-9,1,-2,-7,-5,9,-10,-1,-8,-8,-9,4,-9,4,-10,4,10,9,-6,7,5,-7,9,-7,-8,-7,-2,-3,-1,3,-7,-1,2,-3,6,-2,-3,7,-8,-9,3,-3,7,6,-4,7,5,10,-8,8,10,7,10,5,2,6,2,-8,9,6,2,7,-3,-5,-10,7,2,5,-9,1,6,5,-9,6,-9,-1,10,-6,-5,-6,-3,-4,8,-8,2,6,-9,6,8,-5,-6,5,4,-9,-4,1,7,-4,-7,-1,4,-4,2,10,-4,6,1,8,-5,-4,3,8,-3,6,-7,-6,4,-3,-4,6,-7,-1,-4,-6,5,9,5,7,-10,-9,-10,7,7,-10,-2,-10,-9,-9,-10,-1,5,3,5,-10,-5,-1,4,-8,-7,-3,-7,8,-3,-8,-2,-8,-10,6,4,-2,5,-5,1,-1,4,-5,-8,-8,10,6,8,6,8,3,10,-3,9,5,1,-8,3,-7,-8,3,-4,7,-6,8,-9,-8,-6,-5,6,7,-9,2,8,-2,-6,-4,8,2,8,-10,3,-5,6,6,-1,9,7,9,-1,-4,10,7,1,3,-9,4,10,3,-9,-10,-1,8,10,-3,-2,8,-5,9,-4,5,5,7,1,3,-8,-10,-2,5,8,5,-5,4,-9,7,-7,-9,2,-10,-8,2,-6,5,1,-9,7,10,6,3,-7,9,3,-6,5,-7,-9,-1,9,2,-5,8,-5,-6,-2,-8,-1,1,-8,8,-3,8,-4,-4,2,-5,-8,-9,-3,6,7,-4,-3,-10,-2,-4,-5,-6,1,4,-7,-10,-5,-10,7,-6,1,1,-5,-5,-1,-1,-1,-5,-10,-6,1,-3,-9,7,-8,8,-10,-1,2,-1,7,9,-2,2,7,-8,6,-5,2,-8,-4,10,-7,-1,9,4,-6,3,9,-8,3,-5,7,3,3,-10,10,-2,-2,-8,5,-4,4,8,3,10,-2,-7,6,-8,3,-7,-9,2,2,-2,-9,-7,-6,-4,3,-4,-10,3,1,6,-3,-7,-2,6,8,-2,-6,9,5,10,-9,2,7,7,1,4,-8,6,1,-5,-10,5,5,-8,7,-8,-4,8,-8,-1,-8,-2,-7,6,10,6,-8,6,7,4,1,10,4,7,3,-10,-3,9,1,-8,7,-3,-9,8,10,-9,4,6,-7,10,9,3,4,-1,-7,8,-5,1,-7,-9,9,-7,7,-10,6,-6,-10,8,1,9,-10,-4,-5,10,-3,10,-7,6,-2,-2,-6,3,9,2,-3,-10,9,8,10,-5,-9,7,-3,1,9,4,-4,-5,-10,-5,-9,4,2,1,1,4,-2,7,-4,-1,-4,10,3,10,-4,8,1,-9,-5,-4,-6,-8,1,-4,-6,10,3,7,-5,1,4,-3,1,-10,2,-7,-6,9,-2,2,9,7,2,-9,-1,-8,-10,-3,-3,-1,9,-3,3,-2,-4,-3,6,6,2,-7,-6,1,6,-8,7,1,-5,10,-8,-5,9,-7,7,-5,1,-5,6,2,10,-10,7,-2,8,2,-6,-10,6,10,-3,2,6,10,3,-4,1,-9,-5,-3,-7,-1,-4,8,8,-3,2,4,3,7,-5,-9,7,5,1,7,4,10,10,-10,-5,-9,8,-4,7,-7,4,-1,3,5,5,-1,1,-9,-9,-9,-1,3,2,-8,-1,-3,10,8,-1,5,-4,-7,8,-7,-6,-3,-5,-6,-4,-5,-1,9,-6,3,9,-5,6,9,-9,-1,1,2,10,2,-4,8,9,7,4,3,9,6,10,-9,2,-6,6,10,5,2,8,5,9,3,1,9,-1,-5,-10,2,6,6,5,8,7,9,9,-5,7,2,-1,8,-5,3,-7,1,2,-3,-3,-6,10,8,-1,-10,8,-6,2,-10,-5,6,9,-5,-5,5,1,10,9,3,-10,8,-4,6,-8,-6,-9,-5,10,-7,-10,6,-6,-3,6,-6,-8,4,-9,-9,-5,2,-7,-2,8,-3,6,10,-8,8,8,10,-8,-7,5,6,8,5,6,2,9,-10,7,-8,2,8,-9,7,3,6,9,7,1,-5,-1,9,-4,-4,1,-7,7,-5,4,-6,6,-4,-6,-4,-4,4,-8,5,5,5,3,-1,7,-9,-5,-9,-6,8,5,1,-3,-7,9,4,-5,-10,-1,1,6,-1,2,4,3,2,-3,1,7,6,-2,-9,-9,7,1,-10,-5,-8,10,-7,-5,3,3,4,2,5,10,2,5,1,-5,-3,-3,9,4,-8,-8,-4,5,-8,-10,10,9,3,-1,-1,7,-9,4,6,8,4,-5,7,-8,6,10,-2,-7,-4,-1,-7,9,-1,-7,-1,-2,-3,3,6,4,3,-5,-4,2,-5,5,1,9,6,-10,-3,2,-9,3,-10,5,-1,-10,7,5,3,3,3,-6,1,6,8,7,4,-1,9,8,8,-6,-8,-8,-10,-6,4,2,8,9,-5,-3,10,-3,-2,10,-9,-7,-9,9,-6,4,7,-7,-5,10,5,-1,9,-4,7,1,2,2,-2,3,-5,8,-5,6,-1,10,-2,-1,-6,-2,-8,-6,10,2,-10,10,3,7,2,8,2,1,10,6,6,-7,-10,5,-5,-4,5,10,1,-6,9,-10,1,-6,3,6,-10,4,-10,-2,9,9,9,9,-5,6,-10,-6,6,-3,3,-8,4,5,-2,-10,4,-2,7], dtype = "int8")#candidate|6582|(1056,)|const|int8
call_6580 = relay.TupleGetItem(func_481_call(relay.reshape(var_6581.astype('float64'), [10, 6, 11]), relay.reshape(var_6581.astype('float64'), [10, 6, 11]), relay.reshape(const_6582.astype('int8'), [1056,]), ), 2)
call_6583 = relay.TupleGetItem(func_486_call(relay.reshape(var_6581.astype('float64'), [10, 6, 11]), relay.reshape(var_6581.astype('float64'), [10, 6, 11]), relay.reshape(const_6582.astype('int8'), [1056,]), ), 2)
output = relay.Tuple([call_6531,call_6580,var_6581,const_6582,])
output2 = relay.Tuple([call_6532,call_6583,var_6581,const_6582,])
func_6589 = relay.Function([var_6581,], output)
mod['func_6589'] = func_6589
mod = relay.transform.InferType()(mod)
var_6590 = relay.var("var_6590", dtype = "float64", shape = (660, 1))#candidate|6590|(660, 1)|var|float64
output = func_6589(var_6590)
func_6591 = relay.Function([var_6590], output)
mutated_mod['func_6591'] = func_6591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_6634 = relay.TupleGetItem(func_2096_call(), 2)
call_6635 = relay.TupleGetItem(func_2098_call(), 2)
output = call_6634
output2 = call_6635
func_6639 = relay.Function([], output)
mod['func_6639'] = func_6639
mod = relay.transform.InferType()(mod)
mutated_mod['func_6639'] = func_6639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6639_call = mutated_mod.get_global_var('func_6639')
call_6640 = func_6639_call()
output = call_6640
func_6641 = relay.Function([], output)
mutated_mod['func_6641'] = func_6641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3062_call = mod.get_global_var('func_3062')
func_3063_call = mutated_mod.get_global_var('func_3063')
call_6659 = relay.TupleGetItem(func_3062_call(), 2)
call_6660 = relay.TupleGetItem(func_3063_call(), 2)
func_1758_call = mod.get_global_var('func_1758')
func_1761_call = mutated_mod.get_global_var('func_1761')
const_6677 = relay.const([5,4,8,-10,-3,5,-7,-5,5,6,1,4,9,-1,3,8,-5,3,6,-2,-6,-2,10,-3,-3,-10,-5,8,8,-2,7,-8,4,6,5,-1,-2,5,-10,8,-1,10,3,-1,-7,-1,-5,-7,-10,-1,10,5,-4,-6,3,2,2,-2,-7,-5,6,-9,5,-9,8,10,-3,9,-9,4,1,-6,7,10,-10,10,-3,6,4,4,7,-1,-1,8,7,2,9,3,-7,-9,9,3,-8,-1,6,8,1,6,2,-2,7,7,5,9,2,-8,-9,5,4,10,3,-5,-7,-4,6,-8,-3,8,-4,9,7,8,-2,3,-1,6,-1,6,-4,7,-10,3,-1,-1,-10,-2,2,2,5,10,8,-7,10,7,6,6,-10,-7,-1,-7,-3,-7,10,-8,5,-10,5,10,-3,-1,-4,2,7,-6,-2,-9,-1,-7,-6,-4,5,3,-3,7,-3,-4,-5,-10,8,1,8,-4,-8,8,7,4,9,-4,-2,8,-9,-10,-9,-9,8,-8,9,5,-4,-1,8,5,-5,-8,1,-2,-8,-7,7,-3,-3,3,-4,1,-3,1,2,-9,-6,-5,4,-7,2,-9,-9,3,-5,8,-5,9,3,-1,9,-1,-10,-4,-6,7,7,6,-10,8,7,7,4,2,-10,-2,5,-4,2,9,10,-5,-2,1,-1,-9,4,10,6,5,7,4,3,-6,7,10,-3,-2,-7,9,3,-6,-8,5,2,-9,-9,2,-3,6,6,-9,2,-4,-6,7,-4,6,-1,3,3,2,-7,6,5,-3,-6,9,-4,7,7,9,6,3,-8,-3,-10,-5,-1,8,2,6,4,8,-10,9,-8,1,6,3,10,-7,5,9,4,4,1,-4,7,4,-4,5,3,-5,-9,5,8,-10,-5,-1,-8,-2,4,3,-7,-9,2,-4,9,6,-2,5,-4,-1,6,7,-6,3,7,1,5,-7,-3,5,-2,8,-3,-4,-2,5,8,1,1,5,-2,-1,8,5,1,-3,-3,9,-6,3,9,-5,10,-2,-4,8,-3,2,-9,3,8,-4,-7,-7,5,2,-7,-2,6,9,-9,3,-6,-5,5,4,4,-4,-1,5,-10,2,3,-6,8,-7,2,10,9,2,1,-9,4,-7,6,-10,6,-6,6,8,-9,10,6,-1,5,-1,9,-3,-3,9,10,-8,3,-5,-7,-4,7,2,-4,-10,-6,5,-1,10,9,-3,-1,5,-4,3,-3,-10,1,-8,4,-5,-9,8,1,1,-9,6,5,4,-4,-3,-3,9,-6,2,5,2,10,-1,10,-8,8,1,-7,-5,1,8,-10,2,6,-7,1,-6,-9,-1,-10,-10,-5,4,-3,3,-6,9,-1,-3,5,9,-7,-7,3,5,-7,4,5,3,8,3,-10,1,5,10,3,-6,-6,9,8,-3,-1,8,4,6,-9,7,3,-3,-3,8,4,-8,-4,-2,-5,1,9,-1,-1,6,-6,-1,10,-9,9,-8,-9,5,-7,8,-1,5,-6,-4,5,-7,2,2,-4,-4,-6,5,-3,9,-7,-10,-7,8,-3,-10,-2,-9,-9,-8,-2,3,9,3,10,1,-2,6,10,-3,-8,-1,-2,-7,-3,-3,9,5,5,9,-2,3,-3,-1,4,-6,-9,-5,1,-3,8,1,1,7,-4,1,9,1,-2,-7,-8,-3,1,-7,1,-9,5,10,6,2,-6,-7,7,-8,-2,-7,7,-7,-7,1,4,1,-9,-7,-6,6,-2,-6,-3,-7,-9,-5,-4,5,7,-3,7,4,3,-3,-10,3,-4,-10,5,-1,-2,1,9,9,-5,10,-4,-9,4,8,-1,-6,9,-9,1,-9,6,-1,9,2,-2,-5,7,-5,-6,-4,1,-9,6,-5,9,2,-5,2,-2,-9,9,3,7,-4,9,7,10,10,-5,-2,10,-2,8,-10,-10,-7,2,2,7,2,6,6,9,-1,-3,-1,-9,-2,6,-7,1,-3,3,-4,-3,-6,8,-6,-2,-3,2,-9,-4,-5,-3,7,6,8,-7,-10,9,-1,10,3,-4,6,-10,-6,8,-7,6,4,3,-1,-2,-1,9,-7,-7,10,9,-7,2,3,5,-10,3,-2,6,9,6,-1,9,-5,-10,-2,-2,-6,-4,-4,-1,1,10,10,-9,-6,-8,2,-4,-6,2,1,-8,-8,-10,-1,-1,-2,-6,-7,-3,1,-7,-9,-10,3,-4,7,5,-2,2,-5,6,1,2,-8,-8,-4,-2,6,-9,-5,7,-5,-9,-9,-2,1,-4,1,-10,-10,-8,7,-9,-1,4,-3,9,-7,-5,-9,-3,-7,5,-4,9,-7,-10,4,-7,-2,-2,-6,-1,9,-1,6,-9,2,3,10,10,6,2,-3,-6,10,10,-6,8,8,4,-3,7,8,1,-1,-7,-3,8,8,3,-1,-5,-3,-2,4,4,-10,5,2,-8,-7,1,-4,9,4,-9,2,-2,6,-7,2,10,-6,-10,8,-1,-4,8,3,9,7,10,1,6,8,10,7,-9,-4,1,-8,-9,-7,10,4,7,7,-5,-1,-8,6,-6,9,-6,-6,-4,-9,7,-2,6,-6,9,10,4,7,-10,-3,6,2,4,10,2,-1,-7,-8,10,8,9,-5,9,8,-7,-6,2,6,3,4,-7,-6,1,-7,-8,-2,5,4,1,5,-5,-10,6,5,-2,-7,-5,3,-7,-8,-5,3,-10,-6,-9,1,-10,10,-7,-7,3,7,-7,7,1,8,-6,8,10,-6,-2,2,8,-8,-7,3,1,2,-10,-3,-2,7,-3,-3,8,1,-6,2,5,8,-4,-3], dtype = "int8")#candidate|6677|(1056,)|const|int8
call_6676 = relay.TupleGetItem(func_1758_call(relay.reshape(const_6677.astype('int8'), [11, 12, 8])), 0)
call_6678 = relay.TupleGetItem(func_1761_call(relay.reshape(const_6677.astype('int8'), [11, 12, 8])), 0)
output = relay.Tuple([call_6659,call_6676,const_6677,])
output2 = relay.Tuple([call_6660,call_6678,const_6677,])
func_6695 = relay.Function([], output)
mod['func_6695'] = func_6695
mod = relay.transform.InferType()(mod)
output = func_6695()
func_6696 = relay.Function([], output)
mutated_mod['func_6696'] = func_6696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1696_call = mod.get_global_var('func_1696')
func_1697_call = mutated_mod.get_global_var('func_1697')
call_6713 = func_1696_call()
call_6714 = func_1696_call()
func_6381_call = mod.get_global_var('func_6381')
func_6383_call = mutated_mod.get_global_var('func_6383')
var_6717 = relay.var("var_6717", dtype = "float32", shape = (1, 45))#candidate|6717|(1, 45)|var|float32
call_6716 = relay.TupleGetItem(func_6381_call(relay.reshape(var_6717.astype('float32'), [45,])), 1)
call_6718 = relay.TupleGetItem(func_6383_call(relay.reshape(var_6717.astype('float32'), [45,])), 1)
func_2728_call = mod.get_global_var('func_2728')
func_2730_call = mutated_mod.get_global_var('func_2730')
call_6719 = func_2728_call()
call_6720 = func_2728_call()
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_6726 = relay.TupleGetItem(func_4154_call(), 0)
call_6727 = relay.TupleGetItem(func_4155_call(), 0)
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
const_6730 = relay.const([5,7,1,10,2,4,-8,-6,9,-2,-8,-2,-1,-1,-8,3,2,-9,-2,8,7,-2,2,3,-9,-4,7,10,-7,-10,5,10,-3,-2,-8,-9,-4,-1,8,-2,10,-5,-4,-3,-8,-7,6,10,-6,4,-5,-10,-3,-7,-6,9,-5,-1,1,-9,8,-10,3,4,4,-5,9,10,-8,-3,6,-10,-8,1,4,-8,7,-7,-10,10,-6,-5,-2,-7,1,-7,-3,9,6,1,-9,-4,-7,-7,-1,2,-3,2,-3,-8,-10,3,-9,-5,4,7,-2,-2,-2,-7,5,2,-10,3,-5,10,-5,-1,9,9,1,-7,-9,-4,-7,5,4,-1,-4,-10,7,-6,-4,7,2,-5,4,-8,2,-7,4,-10,-1,-5,-7,-4,4,7,7,-1,1,-4,9,-9,5,-9,-10,-9,2,-6,10,5,9,2,-5,-7,-1,1,-2,-3,10,7,-5,-1,-4,-7,-8,-8,2,3,5,6,-8,7,9,10,-4,-9,7,5,10,4,2,-3,2,-6,5,-2,-8,4,7,-9,2,9,2,9,-3,10,-4,4,10,-2,3,-7,-3,10,-6,2,-1,-5,4,-6,6,-4,10,8,-1,4,-6,-5,-3,-8,6,-5,10,1,-6,1,-5,-4,-7,5,-5,-2,-2,-10,3,-4,-10,7,2,6,-7,2,5,6,-10,-2,4,6,10,-2,5,-4,-6,-7,-1,6,9,1,-6,6,2,3,-1,-1,-6,-3,-1,-6,-8,-7,5,8,-3,-7,-5,-5,10,-2,-8,1,-6,-6,3,-5,-6,-1,-6,-6,5,-8,-8,-7,2,9,-2,5,-7,6,5,-3,4,4,3,6,3,2,8,10,-1,-9,1,3,-7,10,-2,2,8,-5,6,-1,-5,2,4,-3,-1,8,-6,-10,1,4,-4,1,-4,3,8,-1,-8,-6,5,7,-2,7,-7,-3,-8,4,-5,4,-9,-1,4,10,7,6,7,-7,10,9,5,-6,10,7,-4,7,9,-8,4,-8,-6,-4,-10,2,-6,-9,-4,4,-4,-1,1,2,8,4,2,4,8,8,8,2,-2,5,-6,2,-9,10,1,-1,-6,2,8,-3,-3,-6,5,-6,-9,-3,-1,6,-7,1,10,8,6,-3,7,3,-9,2,-9,10,-1,-2,9,-4,6,-4,-5,2,4,8,-1,3,1,3,8,-7,-8,3,9,-4,3,1,4,-1,-7,2,-1,-8,-2,2,6,-9,10,-2,9,4,-7,10,-8,-10,2,-5,-6,-5,3,8,-9,-4,7,2,5,8,2,-5,-8,5,8,-3,2,5,-7,7,-8,-9,-10,-2,6,10,7,8,2,-5,5,7,6,-5,2,1,6,6,-10,2,8,3,7,1,5,2,-2,9,10,2,-7,-4,4,6,10,-9,-10,-4,-4,-6,10,8,6,1,1,-8,8,-1,1,6,7,-2,8,4,2,10,6,6,-7,-8,4,-9,7,7,-9,-1,-10,5,-8,1,-7,-2,1,6,6,-8,-9,3,1,6,-4,-8,8,2,10,-6,4,-9,5,-5,-9,-3,4,-4,7,4,-7,-4,4,10,1,1,3,2,-7,-3,4,5,-2,-2,9,10,8,10,2,-8,-8,-10,-2,1,1,-6,-9,-4,1,2,6,7,-8,8,7,-4,-8,5,7,9,-1,-5,-7,-5,-9,-8,1,-10,2,-10,7,-5,-8,-5,10,3,9,4,-10,-4,-6,-5,10,7,-3,-3,10,-5,10,-3,4,-2,5,10,-4,8,9,-8,-9,10,-3,2,1,-4,-7,-1,-3,7,8,-5,4,-2,-7,3,-5,-7,6,-2,7,9,-2,-9,1,5,5,-2,3,3,4,5,-9,-10,4,-3,7,-6,-10,6,-3,5,-10,7,10,-5,-6,-6,5,-1,5,9,-5,4,2,-1,8,-10,-2,2,-7,-6,7,7,5,10,-1,5,4,3,7,10,9,-4,9,1,-2,8,-9,3,2,-6,-2,6,8,3,-3,-1,-5,1,10,3,-1,1,-5,-3,-8,7,-8,6,-4,3,2,-10,-10,4,-5,2,-7,3,9,-6,-5,-9,-7,8,3,-9,-7,3,-1,7,-3,1,4,-1,-2,-2,-1,-9,-5,10,-10,5,9,7,7,6,-3,-2,-3,-3,-2,-9,5,9,-6,-10,-7,4,-4,-6,4,-1,-8,-7,-7,-3,3,-10,-1,2,10,-4,8,-5,-10,1,2,3,8,9,10,4,8,-4,5,-8,10,3,1,-10,6,7,7,8,-1,1,-2,5,-1,9,-6,2,-9,6,3,-1,7,-9,-9,10,-5,-1,5,7,4,-3,-2,-6,2,-1,8,-7,1,9,-4,-1,-9,-8,-6,-2,2,1,-10,5,9,-8,9,1,-1,1,1,-6,2,-9,-10,9,6,-6,-6,-10,-6,-1,-4,-4,-7,2,-4,-10,-6,-5,10,8,1,-4,-4,4,-5,-4,9,5,2,-6,10,3,5,-2,-1,2,-6,-10,1,2,-9,4,-6,-6,8,5,9,6,7,10,-10,-3,-9,1,-7,7,-1,7,-3,6,-6,1,-10,-1,5,-8,-4,-3,3,6,-7,9,-5,5,-1,9,-3,-5,7,1,-5,-7,9,-5,-2,-4,3,6,10,-8,-2,8,-7,-8,7,4,-10,5,1,-2,1,3,-9,-4,2,-8,8,2,9,2,3,1,9,3,-6,-2,-2,2,7,8,9,6,4,-5,-1,-2,-4,-6,-9,-2,5,-1,-10,6,-1,9,-2,7,4,-2,10,-7,-7,7,3,10,-3,5,-5,1,9,6,-4,9], dtype = "int8")#candidate|6730|(1056,)|const|int8
call_6729 = relay.TupleGetItem(func_322_call(relay.reshape(const_6730.astype('int8'), [11, 12, 8])), 0)
call_6731 = relay.TupleGetItem(func_325_call(relay.reshape(const_6730.astype('int8'), [11, 12, 8])), 0)
bop_6732 = relay.bitwise_xor(call_6719.astype('int64'), call_6713.astype('int64')) # shape=(5, 8, 64)
bop_6735 = relay.bitwise_xor(call_6720.astype('int64'), call_6714.astype('int64')) # shape=(5, 8, 64)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_6741 = relay.TupleGetItem(func_3183_call(), 0)
call_6742 = relay.TupleGetItem(func_3184_call(), 0)
output = relay.Tuple([call_6716,var_6717,call_6726,call_6729,const_6730,bop_6732,call_6741,])
output2 = relay.Tuple([call_6718,var_6717,call_6727,call_6731,const_6730,bop_6735,call_6742,])
func_6743 = relay.Function([var_6717,], output)
mod['func_6743'] = func_6743
mod = relay.transform.InferType()(mod)
mutated_mod['func_6743'] = func_6743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6744 = relay.var("var_6744", dtype = "float32", shape = (1, 45))#candidate|6744|(1, 45)|var|float32
func_6743_call = mutated_mod.get_global_var('func_6743')
call_6745 = func_6743_call(var_6744)
output = call_6745
func_6746 = relay.Function([var_6744], output)
mutated_mod['func_6746'] = func_6746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6270_call = mod.get_global_var('func_6270')
func_6271_call = mutated_mod.get_global_var('func_6271')
call_6849 = relay.TupleGetItem(func_6270_call(), 1)
call_6850 = relay.TupleGetItem(func_6271_call(), 1)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_6868 = relay.TupleGetItem(func_4154_call(), 0)
call_6869 = relay.TupleGetItem(func_4155_call(), 0)
output = relay.Tuple([call_6849,call_6868,])
output2 = relay.Tuple([call_6850,call_6869,])
func_6878 = relay.Function([], output)
mod['func_6878'] = func_6878
mod = relay.transform.InferType()(mod)
mutated_mod['func_6878'] = func_6878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6878_call = mutated_mod.get_global_var('func_6878')
call_6879 = func_6878_call()
output = call_6879
func_6880 = relay.Function([], output)
mutated_mod['func_6880'] = func_6880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2296_call = mutated_mod.get_global_var('func_2296')
call_6887 = relay.TupleGetItem(func_2294_call(), 0)
call_6888 = relay.TupleGetItem(func_2296_call(), 0)
var_6889 = relay.var("var_6889", dtype = "float64", shape = (5, 8, 132))#candidate|6889|(5, 8, 132)|var|float64
bop_6890 = relay.logical_and(call_6887.astype('bool'), relay.reshape(var_6889.astype('bool'), relay.shape_of(call_6887))) # shape=(5, 8, 132)
bop_6893 = relay.logical_and(call_6888.astype('bool'), relay.reshape(var_6889.astype('bool'), relay.shape_of(call_6888))) # shape=(5, 8, 132)
func_1376_call = mod.get_global_var('func_1376')
func_1380_call = mutated_mod.get_global_var('func_1380')
const_6895 = relay.const([[9.770848,-2.477997,3.274263,4.794250,-5.944173,-7.531016,-3.298729,-0.253224,-3.177527,-1.138304,3.247125,-0.560646,8.913627,8.820438,-4.085795,-0.990512,-7.863466,-3.247073,1.163335,-8.061239,-7.188907,-1.354474,-2.975021,0.816074,-1.713423,3.440989,-1.917778,-6.898589,-4.655724,-7.401742,7.471478,-1.166238,5.002393,4.304688,-7.529894,-3.588706,9.275092,-3.291090,1.090871,-3.621386,2.407293,6.682110,5.152880,-6.137749,6.913097,-6.331047,4.991565,9.972783,-4.871208,-1.819350,-0.807465,2.928371,9.774569,5.551966,2.954632,-7.535484],[-8.099864,-7.152991,1.853982,3.783200,4.641022,-0.371575,-4.759759,7.700053,-0.296266,0.559611,-3.090090,-5.279186,-1.706931,-1.381589,6.441618,1.473750,-9.671959,5.151150,-1.425144,9.872833,2.801518,-3.536480,2.782326,-3.305941,2.047081,-0.359252,-2.308643,6.466418,8.659979,-8.638745,0.876838,-9.471207,0.276282,2.811218,-7.318569,-8.144175,-7.302992,3.159214,-8.287194,-7.380460,5.064077,-8.255867,1.904042,3.860416,4.537724,-7.416370,8.238008,3.007688,-4.881319,-1.080706,7.394309,-6.799176,1.827792,5.579863,5.654982,-8.235174],[-5.605510,-6.386981,-9.156119,-6.328672,7.859140,-4.364533,5.770176,-8.130714,7.430344,-6.645757,0.081846,-6.960062,-0.895867,-9.843580,4.678462,2.202571,3.816559,-9.810534,3.890625,-7.093177,1.951627,5.491162,-4.337743,-8.034782,-2.057484,-0.649806,-9.310375,-8.597400,-0.631061,-7.300086,3.254878,5.192884,-1.275657,1.771551,2.583586,-7.519654,-2.399471,9.370270,5.407018,-7.446736,2.727071,4.324322,-3.987838,-7.471542,4.795499,-8.149209,-1.839695,1.252296,5.297201,-6.773785,-0.780671,3.059346,-5.227943,4.703007,8.811696,8.259652],[-7.633560,-3.621531,2.997638,9.853654,4.785326,1.111128,-9.592407,-1.961103,9.844033,-6.171457,-5.098085,4.026826,-6.618555,-8.707148,-1.357828,-9.708747,9.344793,3.154648,-0.599514,9.232102,8.867932,6.436307,3.455334,5.245647,1.442749,6.082173,-0.714381,-0.789125,1.441466,-4.641915,2.387505,5.911389,0.090929,8.617335,3.288574,7.493146,9.608517,-6.791670,9.148306,-4.869902,7.058023,-1.862671,-7.750236,6.056675,7.047730,8.871094,-0.382312,5.026264,-3.881724,4.143361,4.802374,-7.085726,-3.357813,-9.428151,-7.680846,-2.432726],[-4.910965,5.421900,8.250607,-0.690500,-5.062603,8.138967,-6.073486,-3.315685,9.001588,0.723841,9.865739,-3.667014,-8.160269,4.223788,2.185706,0.433714,-2.344778,-3.392126,5.818063,-0.346312,-5.182019,-2.513630,4.565982,3.582763,7.995231,7.726820,-0.350815,-2.549777,-2.660132,-1.675417,4.119864,3.959355,-8.121406,2.767409,1.846711,-6.713178,-4.359491,-5.469686,8.532553,-7.503653,-3.845242,2.669504,5.824204,-3.035941,4.977137,3.094815,-7.662740,-6.070026,-1.813186,-1.918085,-1.107927,-2.005268,9.211234,-6.407130,-4.793827,2.759850]], dtype = "float32")#candidate|6895|(5, 56)|const|float32
var_6896 = relay.var("var_6896", dtype = "float64", shape = (660,))#candidate|6896|(660,)|var|float64
var_6897 = relay.var("var_6897", dtype = "int8", shape = (1056,))#candidate|6897|(1056,)|var|int8
call_6894 = relay.TupleGetItem(func_1376_call(relay.reshape(const_6895.astype('float32'), [7, 10, 4]), relay.reshape(var_6896.astype('float64'), [660,]), relay.reshape(var_6897.astype('int8'), [1056,]), ), 1)
call_6898 = relay.TupleGetItem(func_1380_call(relay.reshape(const_6895.astype('float32'), [7, 10, 4]), relay.reshape(var_6896.astype('float64'), [660,]), relay.reshape(var_6897.astype('int8'), [1056,]), ), 1)
output = relay.Tuple([bop_6890,call_6894,const_6895,var_6896,var_6897,])
output2 = relay.Tuple([bop_6893,call_6898,const_6895,var_6896,var_6897,])
func_6901 = relay.Function([var_6889,var_6896,var_6897,], output)
mod['func_6901'] = func_6901
mod = relay.transform.InferType()(mod)
var_6902 = relay.var("var_6902", dtype = "float64", shape = (5, 8, 132))#candidate|6902|(5, 8, 132)|var|float64
var_6903 = relay.var("var_6903", dtype = "float64", shape = (660,))#candidate|6903|(660,)|var|float64
var_6904 = relay.var("var_6904", dtype = "int8", shape = (1056,))#candidate|6904|(1056,)|var|int8
output = func_6901(var_6902,var_6903,var_6904,)
func_6905 = relay.Function([var_6902,var_6903,var_6904,], output)
mutated_mod['func_6905'] = func_6905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1529_call = mod.get_global_var('func_1529')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_6919 = relay.TupleGetItem(func_1529_call(), 0)
call_6920 = relay.TupleGetItem(func_1530_call(), 0)
func_3877_call = mod.get_global_var('func_3877')
func_3878_call = mutated_mod.get_global_var('func_3878')
call_6923 = relay.TupleGetItem(func_3877_call(), 0)
call_6924 = relay.TupleGetItem(func_3878_call(), 0)
bop_6928 = relay.greater_equal(call_6923.astype('bool'), relay.reshape(call_6919.astype('bool'), relay.shape_of(call_6923))) # shape=(5, 8, 1)
bop_6931 = relay.greater_equal(call_6924.astype('bool'), relay.reshape(call_6920.astype('bool'), relay.shape_of(call_6924))) # shape=(5, 8, 1)
func_2977_call = mod.get_global_var('func_2977')
func_2980_call = mutated_mod.get_global_var('func_2980')
var_6941 = relay.var("var_6941", dtype = "uint16", shape = (64,))#candidate|6941|(64,)|var|uint16
call_6940 = relay.TupleGetItem(func_2977_call(relay.reshape(var_6941.astype('uint16'), [2, 32])), 2)
call_6942 = relay.TupleGetItem(func_2980_call(relay.reshape(var_6941.astype('uint16'), [2, 32])), 2)
output = relay.Tuple([bop_6928,call_6940,var_6941,])
output2 = relay.Tuple([bop_6931,call_6942,var_6941,])
func_6953 = relay.Function([var_6941,], output)
mod['func_6953'] = func_6953
mod = relay.transform.InferType()(mod)
mutated_mod['func_6953'] = func_6953
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6954 = relay.var("var_6954", dtype = "uint16", shape = (64,))#candidate|6954|(64,)|var|uint16
func_6953_call = mutated_mod.get_global_var('func_6953')
call_6955 = func_6953_call(var_6954)
output = call_6955
func_6956 = relay.Function([var_6954], output)
mutated_mod['func_6956'] = func_6956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4423_call = mod.get_global_var('func_4423')
func_4424_call = mutated_mod.get_global_var('func_4424')
call_6974 = relay.TupleGetItem(func_4423_call(), 1)
call_6975 = relay.TupleGetItem(func_4424_call(), 1)
func_2847_call = mod.get_global_var('func_2847')
func_2848_call = mutated_mod.get_global_var('func_2848')
call_6979 = relay.TupleGetItem(func_2847_call(), 0)
call_6980 = relay.TupleGetItem(func_2848_call(), 0)
output = relay.Tuple([call_6974,call_6979,])
output2 = relay.Tuple([call_6975,call_6980,])
func_6982 = relay.Function([], output)
mod['func_6982'] = func_6982
mod = relay.transform.InferType()(mod)
output = func_6982()
func_6983 = relay.Function([], output)
mutated_mod['func_6983'] = func_6983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6639_call = mod.get_global_var('func_6639')
func_6641_call = mutated_mod.get_global_var('func_6641')
call_7024 = func_6639_call()
call_7025 = func_6639_call()
output = call_7024
output2 = call_7025
func_7052 = relay.Function([], output)
mod['func_7052'] = func_7052
mod = relay.transform.InferType()(mod)
mutated_mod['func_7052'] = func_7052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7052_call = mutated_mod.get_global_var('func_7052')
call_7053 = func_7052_call()
output = call_7053
func_7054 = relay.Function([], output)
mutated_mod['func_7054'] = func_7054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2190_call = mod.get_global_var('func_2190')
func_2191_call = mutated_mod.get_global_var('func_2191')
call_7085 = relay.TupleGetItem(func_2190_call(), 3)
call_7086 = relay.TupleGetItem(func_2191_call(), 3)
output = relay.Tuple([call_7085,])
output2 = relay.Tuple([call_7086,])
func_7089 = relay.Function([], output)
mod['func_7089'] = func_7089
mod = relay.transform.InferType()(mod)
mutated_mod['func_7089'] = func_7089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7089_call = mutated_mod.get_global_var('func_7089')
call_7090 = func_7089_call()
output = call_7090
func_7091 = relay.Function([], output)
mutated_mod['func_7091'] = func_7091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6011_call = mutated_mod.get_global_var('func_6011')
call_7110 = relay.TupleGetItem(func_6009_call(), 0)
call_7111 = relay.TupleGetItem(func_6011_call(), 0)
output = call_7110
output2 = call_7111
func_7123 = relay.Function([], output)
mod['func_7123'] = func_7123
mod = relay.transform.InferType()(mod)
output = func_7123()
func_7124 = relay.Function([], output)
mutated_mod['func_7124'] = func_7124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_7172 = relay.TupleGetItem(func_4154_call(), 1)
call_7173 = relay.TupleGetItem(func_4155_call(), 1)
output = call_7172
output2 = call_7173
func_7210 = relay.Function([], output)
mod['func_7210'] = func_7210
mod = relay.transform.InferType()(mod)
mutated_mod['func_7210'] = func_7210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7210_call = mutated_mod.get_global_var('func_7210')
call_7211 = func_7210_call()
output = call_7211
func_7212 = relay.Function([], output)
mutated_mod['func_7212'] = func_7212
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7242 = relay.var("var_7242", dtype = "float32", shape = (15, 8, 8))#candidate|7242|(15, 8, 8)|var|float32
uop_7243 = relay.log10(var_7242.astype('float32')) # shape=(15, 8, 8)
func_3062_call = mod.get_global_var('func_3062')
func_3063_call = mutated_mod.get_global_var('func_3063')
call_7249 = relay.TupleGetItem(func_3062_call(), 0)
call_7250 = relay.TupleGetItem(func_3063_call(), 0)
output = relay.Tuple([uop_7243,call_7249,])
output2 = relay.Tuple([uop_7243,call_7250,])
func_7253 = relay.Function([var_7242,], output)
mod['func_7253'] = func_7253
mod = relay.transform.InferType()(mod)
var_7254 = relay.var("var_7254", dtype = "float32", shape = (15, 8, 8))#candidate|7254|(15, 8, 8)|var|float32
output = func_7253(var_7254)
func_7255 = relay.Function([var_7254], output)
mutated_mod['func_7255'] = func_7255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5409_call = mod.get_global_var('func_5409')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_7266 = relay.TupleGetItem(func_5409_call(), 0)
call_7267 = relay.TupleGetItem(func_5410_call(), 0)
func_5136_call = mod.get_global_var('func_5136')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_7270 = func_5136_call()
call_7271 = func_5136_call()
output = relay.Tuple([call_7266,call_7270,])
output2 = relay.Tuple([call_7267,call_7271,])
func_7292 = relay.Function([], output)
mod['func_7292'] = func_7292
mod = relay.transform.InferType()(mod)
mutated_mod['func_7292'] = func_7292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7292_call = mutated_mod.get_global_var('func_7292')
call_7293 = func_7292_call()
output = call_7293
func_7294 = relay.Function([], output)
mutated_mod['func_7294'] = func_7294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3042_call = mod.get_global_var('func_3042')
func_3043_call = mutated_mod.get_global_var('func_3043')
call_7298 = func_3042_call()
call_7299 = func_3042_call()
output = relay.Tuple([call_7298,])
output2 = relay.Tuple([call_7299,])
func_7309 = relay.Function([], output)
mod['func_7309'] = func_7309
mod = relay.transform.InferType()(mod)
output = func_7309()
func_7310 = relay.Function([], output)
mutated_mod['func_7310'] = func_7310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5535_call = mod.get_global_var('func_5535')
func_5537_call = mutated_mod.get_global_var('func_5537')
call_7353 = relay.TupleGetItem(func_5535_call(), 0)
call_7354 = relay.TupleGetItem(func_5537_call(), 0)
func_4669_call = mod.get_global_var('func_4669')
func_4670_call = mutated_mod.get_global_var('func_4670')
call_7362 = relay.TupleGetItem(func_4669_call(), 0)
call_7363 = relay.TupleGetItem(func_4670_call(), 0)
func_5585_call = mod.get_global_var('func_5585')
func_5586_call = mutated_mod.get_global_var('func_5586')
call_7364 = relay.TupleGetItem(func_5585_call(), 1)
call_7365 = relay.TupleGetItem(func_5586_call(), 1)
output = relay.Tuple([call_7353,call_7362,call_7364,])
output2 = relay.Tuple([call_7354,call_7363,call_7365,])
func_7390 = relay.Function([], output)
mod['func_7390'] = func_7390
mod = relay.transform.InferType()(mod)
mutated_mod['func_7390'] = func_7390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7390_call = mutated_mod.get_global_var('func_7390')
call_7391 = func_7390_call()
output = call_7391
func_7392 = relay.Function([], output)
mutated_mod['func_7392'] = func_7392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5376_call = mod.get_global_var('func_5376')
func_5378_call = mutated_mod.get_global_var('func_5378')
call_7430 = func_5376_call()
call_7431 = func_5376_call()
output = call_7430
output2 = call_7431
func_7434 = relay.Function([], output)
mod['func_7434'] = func_7434
mod = relay.transform.InferType()(mod)
output = func_7434()
func_7435 = relay.Function([], output)
mutated_mod['func_7435'] = func_7435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6982_call = mod.get_global_var('func_6982')
func_6983_call = mutated_mod.get_global_var('func_6983')
call_7486 = relay.TupleGetItem(func_6982_call(), 1)
call_7487 = relay.TupleGetItem(func_6983_call(), 1)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_7488 = relay.TupleGetItem(func_4154_call(), 1)
call_7489 = relay.TupleGetItem(func_4155_call(), 1)
output = relay.Tuple([call_7486,call_7488,])
output2 = relay.Tuple([call_7487,call_7489,])
func_7490 = relay.Function([], output)
mod['func_7490'] = func_7490
mod = relay.transform.InferType()(mod)
output = func_7490()
func_7491 = relay.Function([], output)
mutated_mod['func_7491'] = func_7491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3456_call = mod.get_global_var('func_3456')
func_3458_call = mutated_mod.get_global_var('func_3458')
call_7544 = relay.TupleGetItem(func_3456_call(), 2)
call_7545 = relay.TupleGetItem(func_3458_call(), 2)
var_7552 = relay.var("var_7552", dtype = "int8", shape = (2, 528))#candidate|7552|(2, 528)|var|int8
bop_7553 = relay.less(call_7544.astype('bool'), relay.reshape(var_7552.astype('bool'), relay.shape_of(call_7544))) # shape=(2, 528)
bop_7556 = relay.less(call_7545.astype('bool'), relay.reshape(var_7552.astype('bool'), relay.shape_of(call_7545))) # shape=(2, 528)
bop_7557 = relay.right_shift(call_7544.astype('int32'), relay.reshape(var_7552.astype('int32'), relay.shape_of(call_7544))) # shape=(2, 528)
bop_7560 = relay.right_shift(call_7545.astype('int32'), relay.reshape(var_7552.astype('int32'), relay.shape_of(call_7545))) # shape=(2, 528)
func_4938_call = mod.get_global_var('func_4938')
func_4942_call = mutated_mod.get_global_var('func_4942')
const_7567 = relay.const([-9,3,-3,-7,-1,-1,-3,8,1,6,-3,3,6,2,-4,9,5,9,-2,-6,5,5,-6,8,5,1,2,10,3,3,10,1,8,3,6,-3,7,-9,-3,2,-2,7,-10,1,-8,-1,10,4,-3,6,-6,-10,-8,-6,7,-8,5,-4,2,-8,-2,9,-2,10], dtype = "uint16")#candidate|7567|(64,)|const|uint16
const_7568 = relay.const([5.897578,0.947306,-6.185173,-8.955423,-9.988334,0.816407,-3.436209,3.692485,7.729762,-4.427411,-2.011138,-0.446599,-0.016905,-9.151891,-4.469855,4.122723,0.604570,-3.551201,8.084813,6.685511,0.331966,-8.777481,-8.134424,1.780180,7.549354,-1.310638,-8.576623,-7.326562,-9.918491,-2.059727,-2.172486,-7.343597,-3.132670,6.995168,7.940939,-2.620743,8.956173,-3.661678,-2.799483,2.234703,-0.058029,0.159384,3.345254,1.028142,-6.913506,-5.802449,4.797051,8.244660,1.380774,-7.716213,0.618772,7.638717,1.636892,-7.627236,0.616830,1.137077,5.721726,-7.435814,-3.549466,-4.269267,-4.258623,2.048343,8.792453,0.478440,6.604257,-2.172353,-3.177825,-0.609413,9.892334,-8.247975,-8.497874,-7.931420,-7.889072,-3.069108,-8.902282,-5.496975,-1.144811,2.616751,-4.265872,-6.495171,-4.170478,-6.112427,9.446521,-8.973502,3.236996,2.606150,9.380527,-7.668066,8.644185,-8.556637,6.384731,-2.142575,4.254598,-5.572459,-4.264718,6.122689,7.625276,-4.543626,-2.027150,7.462229,8.876137,-8.946769,6.119308,-4.490766,1.305745,-6.385797,7.851926,-8.566317,-0.900070,-4.061599,-5.135151,6.802391,4.356907,-4.233232,7.041511,-2.464909,-3.374745,1.568025,5.287814,-2.677806,-0.688785,9.034458,3.054714,-5.183864,-0.083862,8.250645,5.473559,-6.242307,-7.412918,-0.229229,0.200150,-9.642316,5.651552,9.560659,1.512089,-0.951567,-2.803599,-1.761891,6.499805,-2.764407,0.757819,-8.019044,-7.027988,-8.216562,2.512908,-8.352315,3.230171,0.144838,-1.569779,1.589269,-7.422147,-6.206287,9.153511,1.883603,3.983496,9.306114,2.441869,2.072768,-9.795809,-3.289870,8.373505,-7.771429,3.750691,5.644737,-8.879216,1.487754,-5.476864,-1.390743,-3.621954,1.848874,2.380177,7.122264,-9.420454,-4.633960,-0.476813,5.623018,-6.142147,-7.913300,2.802575,7.363991,-2.694507,-3.161649,-2.386512,-6.291335,-9.395888,0.662627,-9.123854,-4.604539,3.299894,-3.158744,9.915543,6.675524,0.381421,0.155998,-6.356943,4.289127,-4.707738,6.083440,-3.303846,4.332112,7.593791,-1.862182,6.528719,5.173456,5.456990,-3.112379,0.290620,-6.257555,0.120374,5.866399,8.206456,-8.471927,-9.524553,-9.340307,-3.008790,-0.877052,-7.793887,1.793112,6.216411,9.737848,-5.372126,-2.304632,2.497923,4.067395,-0.716870,-2.518460,7.993660,3.152507,0.593806,-5.692071,-1.082459,9.366933,4.194137,-1.020080,5.776509,4.097789,-2.910146,7.355109,7.725901,-5.416461,7.499308,5.692680,-5.598699,4.853829,-5.076103,3.274740,-1.023209,-4.814369,8.433679,-8.140524,-2.885765,4.176379,2.672619,-6.473199,9.663314,4.347474,-3.228903,1.832936,1.639810,-0.789348,-5.653097,-2.292516,-5.596538,-7.408721,-0.033768,5.083326,-7.065292,5.138705,8.417341,-7.112802,-3.605522,-1.668393,-4.553757,1.086197,-3.129106,-2.877210,4.647822,9.723522,8.882445,-7.837646,-3.703055,-7.004572,-9.065536,0.149330,7.341703,-1.693361,9.814872,-9.709996,-7.775999,9.784038,8.224882,8.735563,7.490794,3.639953,-2.464206,-3.450498,4.577647,8.676846,-9.845519,8.688425,4.646743,7.755482,-8.233010,-9.847217,-0.196139,8.925835,6.892165,-8.489768,9.079864,7.153559,2.808286,1.881503,-6.642770,-5.468295,8.170165,1.620687,0.556263,0.229214,-9.752792,-3.283220,8.461903,6.146468,-6.166820,5.795551,8.228108,1.993510,-8.313303,2.131729,-5.055783,4.137328,7.338728,-2.904128,-8.599077,9.931382,1.113303,3.557523,4.731937,-7.383877,-5.099523,-4.843151,-3.340475,6.654238,-9.195229,-5.764835,-7.392347,-9.229240,-3.032583,3.447865,-9.529393,4.068802,-3.264953,-0.093921,9.523054,-1.147258,3.367515,7.831871,-3.867902,-0.289856,7.400999,1.458773,8.112096,-4.799835,-8.200750,-9.542171,-6.003679,7.484020,-4.806101,-2.308092,-4.583166,3.001502,2.013737,6.917307,8.871435,-6.856792,-5.568806,8.324086,9.896790,3.047056,2.783430,-9.258260,-3.018989,-6.634629,-7.215144,-0.642793,2.444755,-0.742370,9.763665,9.556308,1.038719,1.877576,6.637551,3.473149,-3.338690,0.284987,-0.899531,5.373676,1.919768,4.121376,8.493334,-2.616333,-0.972294,4.433134,-2.970384,-9.755697,5.473638,-3.413563,-7.371899,6.481305,-3.582891,-1.268287,4.992363,9.176316,-9.640328,-5.022779,5.510092,-5.339246,9.512887,1.469385,-5.456104,7.257083,8.305678,6.166732,-3.697960,4.884641,0.846132,0.031789,6.088741,0.741406,-0.250379,2.054123,-8.708405,7.332374,-7.049865,6.515815,-8.781110,-0.650648,-2.515208,-0.955287,-9.333165,-8.117883,0.152957,-2.475461,-5.814831,-6.256007,1.843328,-5.960761,-6.373424,9.144342,-1.206528,5.363488,-7.102643,7.974562,1.607073,5.037927,4.336706,0.973224,4.502921,5.748998,0.786833,-5.494728,-7.738477,-5.130153,-0.642303,4.762739,9.315350,-2.425250,-3.775002,-1.816361,7.393509,3.113814,6.396233,2.554827,5.201434,8.934525,9.845828,5.539881,-5.857234,-8.131318,-1.479430,-7.731247,-9.937192,6.715775,-0.692314,5.355251,0.198346,-8.348363,8.344695,8.862317,-1.941701,-3.823751,5.262469,1.833633,2.280444,-7.763587,8.938025,6.315981,9.005186,-9.016253,0.498278,4.122292,4.304162,5.611921,-5.353976,7.719882,2.350363,-6.118012,7.868346,7.195460,8.685983,-5.398144,-4.471009,-9.385124,-2.539105,7.843323,-7.926720,-3.247663,-5.864999,8.073074,8.976904,1.901817,-5.748482,8.024778,-6.978831,-0.125892,-4.467973,-6.003565,7.713498,8.654018,-9.755490,8.517174,3.512834,-7.357550,3.693335,-2.932495,-4.314170,-6.838976,5.236191,-7.043245,-3.735694,0.229299,-9.200411,9.215771,9.894317,5.869152,6.399351,-5.016551,5.277016,-6.131807,-7.944890,5.227773,-7.663918,7.277920,1.821638,7.873476,4.221096,-8.470354,3.056454,0.795325,-7.339182,-6.956381,7.623240,3.046628,0.869941,7.885674,-3.726038,-1.826691,-8.845815,9.677522,2.786676,0.632994,5.582473,-6.967757,7.876933,4.247602,0.651833,1.186487,7.172623,5.135494,-7.291100,-1.906604,5.961018,-7.272656,1.023774,8.499947,-8.731048,2.469410,-8.800847,-3.740324,4.010334,-1.488105,6.520189,6.408206,-5.047824,1.611793,6.212817,5.612001,-0.742013,9.377865,0.204391,3.685614,7.589858,-0.343454,-6.188880,-7.223659,-9.671962,-8.980245,-8.892693,-3.767680,-1.713011,-2.324490,-6.486317,-4.793037,3.103750,-5.691166,-9.035558,-3.493771,-0.942340,-0.496334,-6.121715,-8.127394,1.358757,-4.584770,-0.033914,-5.987342,3.088965,-9.690558,-6.531608,-6.792368,-2.493905,9.053805,-3.958634,9.335041,-6.431905,-4.859165,-6.881851,6.500325,3.654840,9.608373,5.218736,2.029825,-8.423793,-5.111096,-7.509484,-5.517811,0.845053,-2.881082,-2.814569,-6.029574,6.634755,8.241266,8.942167,5.212753,-6.627946,-8.408348,-2.017813,-6.784793,6.609524,6.250524,-0.143900,9.207390,0.586817,4.796314,6.673098,-1.094278,-8.446261,-2.924759,7.132494,8.413059,-4.568965,6.742705,2.921489,-1.922181,-5.138647,-5.467791,5.516678,-4.006217,3.083942,-0.727818,9.753645,9.062527,-8.156390,1.765341,4.594310,-4.358720,-7.535236,-7.414005,0.778530,-7.118059,8.432378,-8.759014,-0.996151,2.417790,2.987693,-2.917598,2.615775,-8.705751,8.350996,5.944117,-6.276338,6.136859,5.922894,-8.211722,-4.687519,-2.283313,-4.454676,-3.884600,0.194711,-7.420925,-5.518156,5.538793,5.073672,5.944566,9.798534,5.123345,-1.357600,-6.118635,0.174159,2.785086,4.817221,5.632945,-9.161695,2.060607,5.687848,-2.586912,-3.936674,6.798507,-8.326370,8.684406,7.191264,9.114277,6.901456,8.215273,2.734791,-6.059124,-3.211794,-3.571621,3.259487,-9.473589,7.999093,-0.749325,-7.865068,9.458825,1.270904,-6.015219,-8.616323,-1.015492,6.747829,-4.950606,-5.314220,-3.899973,-9.065638,-1.424975,-4.092136,-9.858793,7.931172,7.040894,6.809623,-9.936465,3.305665,6.273228,3.333633,2.477734,-9.037853,0.228218,-5.309805,7.975596,-6.692304,4.334951,5.883724,-9.246557,-7.977216,-9.460108,1.737466,-2.671066,-2.730307,-4.065861,-5.341326,-2.385438,0.731782,0.482243,6.942877,-9.274521,-1.073343,-6.106781,5.773583,3.748903,4.026807,9.511439,-2.041746,6.550945,-7.663023,-8.395889,-5.334458,8.480830,-3.503097,6.590079,7.786675,6.718914,5.323593,1.047284,4.274556,6.948469,9.780031,8.100490,-6.824716,-0.729327,-2.153070,5.239270,5.114264,-9.598412,-8.949779,-9.178756,2.837608,1.543287,3.072215,9.351897,6.756104,3.231504,-5.153187,7.556290,-2.369713,5.005529,-3.132851,7.225984,9.811095,-2.295874,5.803284,5.646989,-9.536097,-7.039632,-9.113442,-0.124728,-6.185779,-3.248953,-2.826196,7.059722,8.405337,9.839644,-7.109805,5.954170,-6.724063,0.852994,-9.861125,-1.888943,3.082210,2.155827,6.861796,-0.896116,4.298217,-9.599718,-9.539737,-0.175566,-2.667910,2.443323,-9.405042,-3.079080,-0.913155,4.924385,-9.594644,-7.776810,-0.797459,0.874367,7.307754,9.815900,-4.311087,1.145324,7.326747,-0.423691,5.224618,-6.471888,6.312296,0.976703,-8.267801,-6.766780,-8.254349,8.989319,-0.935392,-2.644238,-6.213163,8.156083,6.179619,3.499148,-8.109085,-6.569692,7.447491,-2.385836,8.294899,7.292399,-8.125186,9.056116,-5.569081,7.771961,2.759989,-1.681489,0.227302,2.773461,-2.160634,2.618993,-0.392087,7.828037,0.619378,-2.181345,2.546435,-3.194458,-8.350341,-5.705786,-2.627201,8.740785,-1.491912,4.280243,9.339407,-6.524087,8.532913,7.504872,-5.255714,-8.554821,-0.274463,-1.323761,-8.355951,7.841080,-8.415732,2.684205,5.188506,9.476961,-2.950152,9.301780,0.786626,-2.966002,2.299410,-2.411722,-0.179315,7.082356,-0.967327,-2.542032,3.417602,9.633957,7.780094,-3.291513,5.411643,-3.816985,0.338801,-0.548885,-4.563332,5.086349,-3.589436,3.122587,-3.467483,5.193391,-7.850694,3.353046,6.623381,-8.229420,8.487563,6.967849,-8.592296,0.061957,5.363345,-7.314089,-0.655148,2.611348,3.684226,0.416030,-6.741396,-9.810303,-9.723521,-8.809729,-5.870234,-1.958685,4.729522,4.068897,-8.635242,6.808885,-5.109187,2.574843,-9.375758,9.501120,6.651943,0.039021,0.678339,-5.548324,-1.376594,1.163945,7.097256,-0.222807,1.904762,-3.406953,-2.114112,1.107115,4.422024,3.169818,4.579284,-5.732148,1.525304,-2.192569,4.967686,-5.056277,5.411179,3.563981,-2.617312,-6.509886,4.631823,7.021016,-2.314641,-3.368340,3.124392,2.181249,-9.287709,8.822531,-7.625045,-9.280162,-0.289418,5.370696,-6.403098,4.475827], dtype = "float32")#candidate|7568|(1014,)|const|float32
call_7566 = relay.TupleGetItem(func_4938_call(relay.reshape(bop_7557.astype('int8'), [1056,]), relay.reshape(const_7567.astype('uint16'), [64,]), relay.reshape(const_7568.astype('float32'), [1014,]), ), 4)
call_7569 = relay.TupleGetItem(func_4942_call(relay.reshape(bop_7557.astype('int8'), [1056,]), relay.reshape(const_7567.astype('uint16'), [64,]), relay.reshape(const_7568.astype('float32'), [1014,]), ), 4)
const_7572 = relay.const([[6,9,1,2,4,-7,2,8,4,-8,-4,-1,1,-4,-2,-3,7,4,-7,2,-2,-6,6,2,-7,9,5,6,5,10,-9,10,6,3,-8,-7,-1,-7,-9,7,9,7,5,-7,5,2,10,-7,-3,2,-5,-6,-1,5,9,-6,-7,-2,8,5,-7,-7,-8,-3,-7,6,3,-10,4,6,7,-2,7,-9,3,8,2,7,2,-4,-7,2,-2,-6,-10,-10,2,-1,7,-4,7,-10,-1,-10,-7,1,5,-3,8,3,-10,4,8,3,-7,-6,2,3,3,6,8,-3,3,-1,-7,-8,9,1,9,-5,-4,3,6,-9,1,-8,-3,1,-1,8,7,5,9,-5,1,-9,10,-10,7,-5,5,7,-6,-7,-3,3,2,-7,-5,3,4,-2,1,-1,3,9,1,9,4,-4,-2,6,6,-7,8,10,2,-6,-6,-3,3,1,8,1,8,1,-4,-4,-2,3,10,2,7,-7,7,4,-2,5,-6,1,4,4,9,-8,8,3,-7,2,-4,-7,-8,2,7,-9,-4,5,-4,-5,6,6,-9,3,-5,-1,3,10,10,-3,-9,-8,-5,-2,3,-6,1,4,-10,-7,10,-3,-6,4,7,3,-10,-1,-7,5,-10,-10,2,10,-8,8,5,-3,-4,-6,-6,9,1,2,2,-7,-10,-3,8,-6,-2,-4,-6,7,6,3,2,6,3,-1,-7,7,-3,2,6,8,2,5,1,-10,-5,6,4,-5,4,-1,-2,10,1,-9,-2,4,-10,-2,3,9,4,7,9,-4,-8,4,3,7,8,10,-2,-1,-5,5,-6,6,-10,-9,-7,-4,8,-4,3,-5,-9,8,9,-6,-6,-2,7,-6,3,8,8,4,1,7,1,-5,-6,2,6,-2,10,7,-4,-6,8,-8,7,10,-9,-4,-8,-9,-3,2,10,2,-9,-9,1,1,-1,-4,10,8,1,-10,-10,5,-1,-1,-10,10,1,4,5,1,-4,-6,-1,4,6,-2,2,-10,-2,-3,-5,4,2,-9,-5,5,-5,6,5,9,1,-8,7,-7,10,-5,-2,-10,-7,5,9,-3,-1,2,6,-9,-3,1,6,2,7,8,6,-6,-9,7,3,6,-7,-1,-2,-2,-9,6,1,1,5,7,-9,4,-6,-8,1,4,-2,10,5,-8,5,2,-4,-1,-2,10,-1,-1,-7,7,-3,-3,6,-9,-5,7,-3,-5,-10,7,5,5,-2,-5,5,5,3,-3,3,-9,-2,-8,5,-3,-2,-7,8,4,-8,8,-3,1,5,4,-9,6,-9,-8,10,1,4,8,10,1,-3,3,-6,-3,-10,8,-1,-3,-1,-7,6,2,6,1,5,5,-3,-5,5,-1,-6,8,-3,10,-4,4,4,8,-9,-7,-3,4],[3,6,-9,4,-5,-5,-3,-4,-3,-7,-6,9,5,2,10,-3,-5,-2,-7,-2,-9,3,-3,1,7,4,-4,-1,-9,-9,6,4,3,6,10,-4,-4,-3,6,-6,1,-6,-3,5,9,4,6,-7,-2,10,-10,3,3,-2,9,2,7,6,-5,5,7,-7,5,-3,-6,9,7,-9,-9,1,-10,9,-9,9,-9,7,-2,-8,-8,-4,-4,-2,6,-5,-4,-2,-7,4,-7,9,-7,-2,1,-8,1,-7,6,7,-1,-8,9,3,-2,-2,-10,-4,9,6,6,-1,5,-1,7,6,2,-5,3,-7,-5,-5,-1,-9,-5,-10,-8,-7,1,5,-9,8,-4,-2,-10,-1,7,-9,-7,9,-3,4,-2,-4,10,-2,10,-2,-4,-1,-3,-9,-10,-1,7,8,8,1,4,4,-5,-5,-8,-9,-3,-7,5,-9,6,-2,7,-3,4,5,-9,2,-9,9,5,-10,-10,-5,6,-2,3,5,5,-6,-4,-7,-4,-9,9,10,7,10,-10,-4,10,-9,9,-6,-4,5,5,-2,-4,-2,8,5,-4,5,-4,10,-5,9,-5,-10,9,-8,9,5,-9,-6,-1,-4,-8,10,-8,-5,9,6,-9,2,10,-2,10,-4,-6,-7,9,-3,2,8,4,-2,-7,9,-3,-4,3,-3,5,3,6,-10,5,4,9,-5,7,-7,4,-10,9,1,4,-6,-1,-2,-2,4,6,-3,1,-7,7,-3,-2,-9,1,-4,4,-3,2,4,6,9,5,6,-4,-6,-6,2,-4,-10,3,-7,5,-3,-5,-1,4,-4,6,7,-2,-8,2,6,-5,8,-10,6,-6,4,-6,4,-9,-9,6,-4,6,7,-4,-1,-9,8,7,5,-10,7,-6,-6,-9,7,-8,4,-2,2,-3,-6,6,-2,-7,8,-7,-3,-6,-5,1,-2,4,-3,-8,4,-9,-6,6,8,6,-1,1,-4,-3,3,5,-5,1,5,6,-1,-2,10,4,1,3,2,8,-2,9,8,-1,10,2,3,5,-3,-2,6,2,-5,1,-3,-7,1,10,-7,2,-5,3,4,-2,6,1,-10,-1,-2,-6,1,-9,7,-10,2,-4,-8,-5,-6,9,-2,5,-7,-1,-9,3,-8,10,4,2,4,5,4,4,8,3,6,-4,-6,-2,-1,3,-9,-7,-7,-1,6,4,-5,-1,2,6,5,10,4,4,-7,5,2,-1,2,9,-5,9,1,-4,7,10,-10,1,2,-1,2,7,9,-2,-9,10,-6,-5,-10,-10,10,9,2,-6,-5,5,5,5,1,7,-10,7,8,5,-2,-7,6,-2,5,-5,3,2,-4,-1,4,-9,7,-2,-8,2,-3,4,-2,10,-2,-10,6,4,8,-7,5,9,-9,-4,-10,-1,-5,4,9]], dtype = "int32")#candidate|7572|(2, 528)|const|int32
bop_7573 = relay.greater_equal(bop_7557.astype('bool'), relay.reshape(const_7572.astype('bool'), relay.shape_of(bop_7557))) # shape=(2, 528)
bop_7576 = relay.greater_equal(bop_7560.astype('bool'), relay.reshape(const_7572.astype('bool'), relay.shape_of(bop_7560))) # shape=(2, 528)
output = relay.Tuple([bop_7553,call_7566,const_7567,const_7568,bop_7573,])
output2 = relay.Tuple([bop_7556,call_7569,const_7567,const_7568,bop_7576,])
func_7589 = relay.Function([var_7552,], output)
mod['func_7589'] = func_7589
mod = relay.transform.InferType()(mod)
mutated_mod['func_7589'] = func_7589
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7590 = relay.var("var_7590", dtype = "int8", shape = (2, 528))#candidate|7590|(2, 528)|var|int8
func_7589_call = mutated_mod.get_global_var('func_7589')
call_7591 = func_7589_call(var_7590)
output = call_7591
func_7592 = relay.Function([var_7590], output)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7640 = relay.var("var_7640", dtype = "float32", shape = (16, 11, 9))#candidate|7640|(16, 11, 9)|var|float32
uop_7641 = relay.cos(var_7640.astype('float32')) # shape=(16, 11, 9)
bop_7658 = relay.right_shift(uop_7641.astype('uint64'), relay.reshape(var_7640.astype('uint64'), relay.shape_of(uop_7641))) # shape=(16, 11, 9)
func_5136_call = mod.get_global_var('func_5136')
func_5138_call = mutated_mod.get_global_var('func_5138')
call_7663 = func_5136_call()
call_7664 = func_5136_call()
output = relay.Tuple([bop_7658,call_7663,])
output2 = relay.Tuple([bop_7658,call_7664,])
func_7680 = relay.Function([var_7640,], output)
mod['func_7680'] = func_7680
mod = relay.transform.InferType()(mod)
var_7681 = relay.var("var_7681", dtype = "float32", shape = (16, 11, 9))#candidate|7681|(16, 11, 9)|var|float32
output = func_7680(var_7681)
func_7682 = relay.Function([var_7681], output)
mutated_mod['func_7682'] = func_7682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1529_call = mod.get_global_var('func_1529')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_7768 = relay.TupleGetItem(func_1529_call(), 0)
call_7769 = relay.TupleGetItem(func_1530_call(), 0)
func_2564_call = mod.get_global_var('func_2564')
func_2567_call = mutated_mod.get_global_var('func_2567')
var_7790 = relay.var("var_7790", dtype = "float64", shape = (80, 2))#candidate|7790|(80, 2)|var|float64
call_7789 = relay.TupleGetItem(func_2564_call(relay.reshape(var_7790.astype('float64'), [80, 2])), 1)
call_7791 = relay.TupleGetItem(func_2567_call(relay.reshape(var_7790.astype('float64'), [80, 2])), 1)
uop_7794 = relay.log(call_7768.astype('float32')) # shape=(5, 8, 1)
uop_7796 = relay.log(call_7769.astype('float32')) # shape=(5, 8, 1)
output = relay.Tuple([call_7789,var_7790,uop_7794,])
output2 = relay.Tuple([call_7791,var_7790,uop_7796,])
func_7797 = relay.Function([var_7790,], output)
mod['func_7797'] = func_7797
mod = relay.transform.InferType()(mod)
var_7798 = relay.var("var_7798", dtype = "float64", shape = (80, 2))#candidate|7798|(80, 2)|var|float64
output = func_7797(var_7798)
func_7799 = relay.Function([var_7798], output)
mutated_mod['func_7799'] = func_7799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6011_call = mutated_mod.get_global_var('func_6011')
call_7804 = relay.TupleGetItem(func_6009_call(), 1)
call_7805 = relay.TupleGetItem(func_6011_call(), 1)
func_7390_call = mod.get_global_var('func_7390')
func_7392_call = mutated_mod.get_global_var('func_7392')
call_7821 = relay.TupleGetItem(func_7390_call(), 1)
call_7822 = relay.TupleGetItem(func_7392_call(), 1)
func_4573_call = mod.get_global_var('func_4573')
func_4574_call = mutated_mod.get_global_var('func_4574')
call_7823 = func_4573_call()
call_7824 = func_4573_call()
func_6901_call = mod.get_global_var('func_6901')
func_6905_call = mutated_mod.get_global_var('func_6905')
var_7826 = relay.var("var_7826", dtype = "float64", shape = (5280, 1))#candidate|7826|(5280, 1)|var|float64
var_7827 = relay.var("var_7827", dtype = "float64", shape = (330, 2))#candidate|7827|(330, 2)|var|float64
var_7828 = relay.var("var_7828", dtype = "int8", shape = (1056, 1))#candidate|7828|(1056, 1)|var|int8
call_7825 = relay.TupleGetItem(func_6901_call(relay.reshape(var_7826.astype('float64'), [5, 8, 132]), relay.reshape(var_7827.astype('float64'), [660,]), relay.reshape(var_7828.astype('int8'), [1056,]), ), 3)
call_7829 = relay.TupleGetItem(func_6905_call(relay.reshape(var_7826.astype('float64'), [5, 8, 132]), relay.reshape(var_7827.astype('float64'), [660,]), relay.reshape(var_7828.astype('int8'), [1056,]), ), 3)
output = relay.Tuple([call_7804,call_7821,call_7823,call_7825,var_7826,var_7827,var_7828,])
output2 = relay.Tuple([call_7805,call_7822,call_7824,call_7829,var_7826,var_7827,var_7828,])
func_7830 = relay.Function([var_7826,var_7827,var_7828,], output)
mod['func_7830'] = func_7830
mod = relay.transform.InferType()(mod)
mutated_mod['func_7830'] = func_7830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7830_call = mutated_mod.get_global_var('func_7830')
var_7832 = relay.var("var_7832", dtype = "float64", shape = (5280, 1))#candidate|7832|(5280, 1)|var|float64
var_7833 = relay.var("var_7833", dtype = "float64", shape = (330, 2))#candidate|7833|(330, 2)|var|float64
var_7834 = relay.var("var_7834", dtype = "int8", shape = (1056, 1))#candidate|7834|(1056, 1)|var|int8
call_7831 = func_7830_call(var_7832,var_7833,var_7834,)
output = call_7831
func_7835 = relay.Function([var_7832,var_7833,var_7834,], output)
mutated_mod['func_7835'] = func_7835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7913 = relay.var("var_7913", dtype = "float32", shape = (2, 6, 12))#candidate|7913|(2, 6, 12)|var|float32
uop_7914 = relay.exp(var_7913.astype('float32')) # shape=(2, 6, 12)
output = relay.Tuple([uop_7914,])
output2 = relay.Tuple([uop_7914,])
func_7930 = relay.Function([var_7913,], output)
mod['func_7930'] = func_7930
mod = relay.transform.InferType()(mod)
mutated_mod['func_7930'] = func_7930
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7931 = relay.var("var_7931", dtype = "float32", shape = (2, 6, 12))#candidate|7931|(2, 6, 12)|var|float32
func_7930_call = mutated_mod.get_global_var('func_7930')
call_7932 = func_7930_call(var_7931)
output = call_7932
func_7933 = relay.Function([var_7931], output)
mutated_mod['func_7933'] = func_7933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_7939 = func_3507_call()
call_7940 = func_3507_call()
output = call_7939
output2 = call_7940
func_7943 = relay.Function([], output)
mod['func_7943'] = func_7943
mod = relay.transform.InferType()(mod)
mutated_mod['func_7943'] = func_7943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7943_call = mutated_mod.get_global_var('func_7943')
call_7944 = func_7943_call()
output = call_7944
func_7945 = relay.Function([], output)
mutated_mod['func_7945'] = func_7945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3456_call = mod.get_global_var('func_3456')
func_3458_call = mutated_mod.get_global_var('func_3458')
call_7971 = relay.TupleGetItem(func_3456_call(), 2)
call_7972 = relay.TupleGetItem(func_3458_call(), 2)
func_4879_call = mod.get_global_var('func_4879')
func_4882_call = mutated_mod.get_global_var('func_4882')
const_7990 = relay.const([9,-5,-8,-7,3,6,8,-4,-9,-6,-8,-8,-2,9,8,-1,1,-9,-2,-1,-2,1,-7,10,-8,2,1,-2,-1,-4,-8,-7,10,-9,-4,7,9,3,5,-3,-10,-2,-5,1,-5,4,-9,-4,8,-9,-6,-6,6,-3,5,-5,9,5,2,-7,-8,-10,-3,-5], dtype = "uint16")#candidate|7990|(64,)|const|uint16
call_7989 = relay.TupleGetItem(func_4879_call(relay.reshape(const_7990.astype('uint16'), [2, 2, 16])), 3)
call_7991 = relay.TupleGetItem(func_4882_call(relay.reshape(const_7990.astype('uint16'), [2, 2, 16])), 3)
uop_7999 = relay.tan(call_7971.astype('float64')) # shape=(2, 528)
uop_8001 = relay.tan(call_7972.astype('float64')) # shape=(2, 528)
bop_8004 = relay.bitwise_and(uop_7999.astype('uint64'), relay.reshape(call_7971.astype('uint64'), relay.shape_of(uop_7999))) # shape=(2, 528)
bop_8007 = relay.bitwise_and(uop_8001.astype('uint64'), relay.reshape(call_7972.astype('uint64'), relay.shape_of(uop_8001))) # shape=(2, 528)
bop_8016 = relay.add(uop_7999.astype('int16'), relay.reshape(bop_8004.astype('int16'), relay.shape_of(uop_7999))) # shape=(2, 528)
bop_8019 = relay.add(uop_8001.astype('int16'), relay.reshape(bop_8007.astype('int16'), relay.shape_of(uop_8001))) # shape=(2, 528)
output = relay.Tuple([call_7989,const_7990,bop_8016,])
output2 = relay.Tuple([call_7991,const_7990,bop_8019,])
func_8020 = relay.Function([], output)
mod['func_8020'] = func_8020
mod = relay.transform.InferType()(mod)
mutated_mod['func_8020'] = func_8020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8020_call = mutated_mod.get_global_var('func_8020')
call_8021 = func_8020_call()
output = call_8021
func_8022 = relay.Function([], output)
mutated_mod['func_8022'] = func_8022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7210_call = mod.get_global_var('func_7210')
func_7212_call = mutated_mod.get_global_var('func_7212')
call_8061 = func_7210_call()
call_8062 = func_7210_call()
output = relay.Tuple([call_8061,])
output2 = relay.Tuple([call_8062,])
func_8063 = relay.Function([], output)
mod['func_8063'] = func_8063
mod = relay.transform.InferType()(mod)
mutated_mod['func_8063'] = func_8063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8063_call = mutated_mod.get_global_var('func_8063')
call_8064 = func_8063_call()
output = call_8064
func_8065 = relay.Function([], output)
mutated_mod['func_8065'] = func_8065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5445_call = mod.get_global_var('func_5445')
func_5446_call = mutated_mod.get_global_var('func_5446')
call_8167 = relay.TupleGetItem(func_5445_call(), 0)
call_8168 = relay.TupleGetItem(func_5446_call(), 0)
output = call_8167
output2 = call_8168
func_8205 = relay.Function([], output)
mod['func_8205'] = func_8205
mod = relay.transform.InferType()(mod)
output = func_8205()
func_8206 = relay.Function([], output)
mutated_mod['func_8206'] = func_8206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_8260 = relay.TupleGetItem(func_3396_call(), 0)
call_8261 = relay.TupleGetItem(func_3398_call(), 0)
output = relay.Tuple([call_8260,])
output2 = relay.Tuple([call_8261,])
func_8277 = relay.Function([], output)
mod['func_8277'] = func_8277
mod = relay.transform.InferType()(mod)
mutated_mod['func_8277'] = func_8277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8277_call = mutated_mod.get_global_var('func_8277')
call_8278 = func_8277_call()
output = call_8278
func_8279 = relay.Function([], output)
mutated_mod['func_8279'] = func_8279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4789_call = mod.get_global_var('func_4789')
func_4790_call = mutated_mod.get_global_var('func_4790')
call_8318 = relay.TupleGetItem(func_4789_call(), 0)
call_8319 = relay.TupleGetItem(func_4790_call(), 0)
output = call_8318
output2 = call_8319
func_8339 = relay.Function([], output)
mod['func_8339'] = func_8339
mod = relay.transform.InferType()(mod)
output = func_8339()
func_8340 = relay.Function([], output)
mutated_mod['func_8340'] = func_8340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_8344 = relay.TupleGetItem(func_6695_call(), 0)
call_8345 = relay.TupleGetItem(func_6696_call(), 0)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_8352 = relay.TupleGetItem(func_3183_call(), 0)
call_8353 = relay.TupleGetItem(func_3184_call(), 0)
func_4012_call = mod.get_global_var('func_4012')
func_4014_call = mutated_mod.get_global_var('func_4014')
call_8359 = relay.TupleGetItem(func_4012_call(), 0)
call_8360 = relay.TupleGetItem(func_4014_call(), 0)
bop_8367 = relay.right_shift(call_8344.astype('int16'), call_8352.astype('int16')) # shape=(5, 8, 160)
bop_8370 = relay.right_shift(call_8345.astype('int16'), call_8353.astype('int16')) # shape=(5, 8, 160)
output = relay.Tuple([call_8359,bop_8367,])
output2 = relay.Tuple([call_8360,bop_8370,])
func_8379 = relay.Function([], output)
mod['func_8379'] = func_8379
mod = relay.transform.InferType()(mod)
mutated_mod['func_8379'] = func_8379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8379_call = mutated_mod.get_global_var('func_8379')
call_8380 = func_8379_call()
output = call_8380
func_8381 = relay.Function([], output)
mutated_mod['func_8381'] = func_8381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7292_call = mod.get_global_var('func_7292')
func_7294_call = mutated_mod.get_global_var('func_7294')
call_8503 = relay.TupleGetItem(func_7292_call(), 1)
call_8504 = relay.TupleGetItem(func_7294_call(), 1)
const_8506 = relay.const([[[-4,-10,1],[4,-5,10],[5,6,3],[-7,-8,4],[6,-3,8],[6,6,-6],[5,-3,-4],[-8,10,7]],[[4,2,10],[-7,-1,3],[-10,-1,2],[-3,7,9],[-8,-2,-9],[-6,3,-6],[-4,-9,5],[4,10,2]],[[-3,1,1],[-5,7,1],[-4,-10,5],[-2,-6,5],[5,-7,-5],[9,3,1],[-1,7,2],[3,-5,7]],[[-6,-10,-1],[8,-4,-3],[5,10,1],[4,-8,10],[-10,-7,6],[6,2,8],[3,-9,10],[-8,3,3]],[[-9,-6,9],[-6,8,4],[7,8,6],[-3,10,7],[-6,-3,3],[3,-2,-7],[-4,9,-6],[6,5,-5]]], dtype = "int16")#candidate|8506|(5, 8, 3)|const|int16
bop_8507 = relay.bitwise_or(call_8503.astype('uint32'), const_8506.astype('uint32')) # shape=(5, 8, 3)
bop_8510 = relay.bitwise_or(call_8504.astype('uint32'), const_8506.astype('uint32')) # shape=(5, 8, 3)
func_2728_call = mod.get_global_var('func_2728')
func_2730_call = mutated_mod.get_global_var('func_2730')
call_8518 = func_2728_call()
call_8519 = func_2728_call()
func_6526_call = mod.get_global_var('func_6526')
func_6527_call = mutated_mod.get_global_var('func_6527')
call_8527 = func_6526_call()
call_8528 = func_6526_call()
output = relay.Tuple([bop_8507,call_8518,call_8527,])
output2 = relay.Tuple([bop_8510,call_8519,call_8528,])
func_8529 = relay.Function([], output)
mod['func_8529'] = func_8529
mod = relay.transform.InferType()(mod)
mutated_mod['func_8529'] = func_8529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8529_call = mutated_mod.get_global_var('func_8529')
call_8530 = func_8529_call()
output = call_8530
func_8531 = relay.Function([], output)
mutated_mod['func_8531'] = func_8531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4730_call = mod.get_global_var('func_4730')
func_4731_call = mutated_mod.get_global_var('func_4731')
call_8545 = relay.TupleGetItem(func_4730_call(), 0)
call_8546 = relay.TupleGetItem(func_4731_call(), 0)
func_5409_call = mod.get_global_var('func_5409')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_8561 = relay.TupleGetItem(func_5409_call(), 0)
call_8562 = relay.TupleGetItem(func_5410_call(), 0)
output = relay.Tuple([call_8545,call_8561,])
output2 = relay.Tuple([call_8546,call_8562,])
func_8571 = relay.Function([], output)
mod['func_8571'] = func_8571
mod = relay.transform.InferType()(mod)
output = func_8571()
func_8572 = relay.Function([], output)
mutated_mod['func_8572'] = func_8572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1214_call = mod.get_global_var('func_1214')
func_1215_call = mutated_mod.get_global_var('func_1215')
call_8578 = relay.TupleGetItem(func_1214_call(), 1)
call_8579 = relay.TupleGetItem(func_1215_call(), 1)
func_4879_call = mod.get_global_var('func_4879')
func_4882_call = mutated_mod.get_global_var('func_4882')
const_8588 = relay.const([[-5],[-7],[-4],[2],[4],[9],[3],[5],[-2],[-3],[5],[-5],[-3],[3],[-6],[-2],[-6],[8],[2],[9],[7],[-3],[9],[10],[-8],[8],[-7],[6],[-6],[5],[-8],[7],[-7],[-1],[4],[-4],[-2],[-3],[-9],[-4],[-8],[-10],[7],[-6],[-5],[-9],[9],[6],[-10],[7],[-8],[6],[8],[-1],[-6],[3],[9],[-10],[1],[1],[8],[-10],[5],[-5]], dtype = "uint16")#candidate|8588|(64, 1)|const|uint16
call_8587 = relay.TupleGetItem(func_4879_call(relay.reshape(const_8588.astype('uint16'), [2, 2, 16])), 0)
call_8589 = relay.TupleGetItem(func_4882_call(relay.reshape(const_8588.astype('uint16'), [2, 2, 16])), 0)
func_8529_call = mod.get_global_var('func_8529')
func_8531_call = mutated_mod.get_global_var('func_8531')
call_8608 = relay.TupleGetItem(func_8529_call(), 1)
call_8609 = relay.TupleGetItem(func_8531_call(), 1)
output = relay.Tuple([call_8578,call_8587,const_8588,call_8608,])
output2 = relay.Tuple([call_8579,call_8589,const_8588,call_8609,])
func_8621 = relay.Function([], output)
mod['func_8621'] = func_8621
mod = relay.transform.InferType()(mod)
mutated_mod['func_8621'] = func_8621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8621_call = mutated_mod.get_global_var('func_8621')
call_8622 = func_8621_call()
output = call_8622
func_8623 = relay.Function([], output)
mutated_mod['func_8623'] = func_8623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5376_call = mod.get_global_var('func_5376')
func_5378_call = mutated_mod.get_global_var('func_5378')
call_8665 = func_5376_call()
call_8666 = func_5376_call()
output = call_8665
output2 = call_8666
func_8667 = relay.Function([], output)
mod['func_8667'] = func_8667
mod = relay.transform.InferType()(mod)
output = func_8667()
func_8668 = relay.Function([], output)
mutated_mod['func_8668'] = func_8668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_8671 = relay.TupleGetItem(func_6695_call(), 1)
call_8672 = relay.TupleGetItem(func_6696_call(), 1)
output = relay.Tuple([call_8671,])
output2 = relay.Tuple([call_8672,])
func_8684 = relay.Function([], output)
mod['func_8684'] = func_8684
mod = relay.transform.InferType()(mod)
output = func_8684()
func_8685 = relay.Function([], output)
mutated_mod['func_8685'] = func_8685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5409_call = mod.get_global_var('func_5409')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_8752 = relay.TupleGetItem(func_5409_call(), 0)
call_8753 = relay.TupleGetItem(func_5410_call(), 0)
func_8667_call = mod.get_global_var('func_8667')
func_8668_call = mutated_mod.get_global_var('func_8668')
call_8772 = func_8667_call()
call_8773 = func_8667_call()
output = relay.Tuple([call_8752,call_8772,])
output2 = relay.Tuple([call_8753,call_8773,])
func_8778 = relay.Function([], output)
mod['func_8778'] = func_8778
mod = relay.transform.InferType()(mod)
output = func_8778()
func_8779 = relay.Function([], output)
mutated_mod['func_8779'] = func_8779
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8783 = relay.const([[[-3,10,-1,-1,-5,1,-2],[7,-8,8,1,-1,5,-6]],[[-6,-10,1,7,6,-2,-6],[5,5,7,6,9,-1,6]],[[2,4,-8,-5,2,-3,-3],[-9,2,-6,-5,2,10,-1]]], dtype = "uint32")#candidate|8783|(3, 2, 7)|const|uint32
var_8784 = relay.var("var_8784", dtype = "uint32", shape = (3, 2, 7))#candidate|8784|(3, 2, 7)|var|uint32
bop_8785 = relay.bitwise_and(const_8783.astype('uint32'), relay.reshape(var_8784.astype('uint32'), relay.shape_of(const_8783))) # shape=(3, 2, 7)
output = bop_8785
output2 = bop_8785
func_8788 = relay.Function([var_8784,], output)
mod['func_8788'] = func_8788
mod = relay.transform.InferType()(mod)
mutated_mod['func_8788'] = func_8788
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8789 = relay.var("var_8789", dtype = "uint32", shape = (3, 2, 7))#candidate|8789|(3, 2, 7)|var|uint32
func_8788_call = mutated_mod.get_global_var('func_8788')
call_8790 = func_8788_call(var_8789)
output = call_8790
func_8791 = relay.Function([var_8789], output)
mutated_mod['func_8791'] = func_8791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8277_call = mod.get_global_var('func_8277')
func_8279_call = mutated_mod.get_global_var('func_8279')
call_8810 = relay.TupleGetItem(func_8277_call(), 0)
call_8811 = relay.TupleGetItem(func_8279_call(), 0)
output = call_8810
output2 = call_8811
func_8821 = relay.Function([], output)
mod['func_8821'] = func_8821
mod = relay.transform.InferType()(mod)
output = func_8821()
func_8822 = relay.Function([], output)
mutated_mod['func_8822'] = func_8822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_8849 = relay.TupleGetItem(func_3183_call(), 0)
call_8850 = relay.TupleGetItem(func_3184_call(), 0)
output = call_8849
output2 = call_8850
func_8854 = relay.Function([], output)
mod['func_8854'] = func_8854
mod = relay.transform.InferType()(mod)
mutated_mod['func_8854'] = func_8854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8854_call = mutated_mod.get_global_var('func_8854')
call_8855 = func_8854_call()
output = call_8855
func_8856 = relay.Function([], output)
mutated_mod['func_8856'] = func_8856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6526_call = mod.get_global_var('func_6526')
func_6527_call = mutated_mod.get_global_var('func_6527')
call_8862 = func_6526_call()
call_8863 = func_6526_call()
output = relay.Tuple([call_8862,])
output2 = relay.Tuple([call_8863,])
func_8869 = relay.Function([], output)
mod['func_8869'] = func_8869
mod = relay.transform.InferType()(mod)
mutated_mod['func_8869'] = func_8869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8869_call = mutated_mod.get_global_var('func_8869')
call_8870 = func_8869_call()
output = call_8870
func_8871 = relay.Function([], output)
mutated_mod['func_8871'] = func_8871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1696_call = mod.get_global_var('func_1696')
func_1697_call = mutated_mod.get_global_var('func_1697')
call_8992 = func_1696_call()
call_8993 = func_1696_call()
output = call_8992
output2 = call_8993
func_8994 = relay.Function([], output)
mod['func_8994'] = func_8994
mod = relay.transform.InferType()(mod)
mutated_mod['func_8994'] = func_8994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8994_call = mutated_mod.get_global_var('func_8994')
call_8995 = func_8994_call()
output = call_8995
func_8996 = relay.Function([], output)
mutated_mod['func_8996'] = func_8996
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9086 = relay.var("var_9086", dtype = "float32", shape = (3, 10, 4))#candidate|9086|(3, 10, 4)|var|float32
var_9087 = relay.var("var_9087", dtype = "float32", shape = (3, 10, 4))#candidate|9087|(3, 10, 4)|var|float32
bop_9088 = relay.divide(var_9086.astype('float32'), relay.reshape(var_9087.astype('float32'), relay.shape_of(var_9086))) # shape=(3, 10, 4)
func_2453_call = mod.get_global_var('func_2453')
func_2455_call = mutated_mod.get_global_var('func_2455')
const_9093 = relay.const([4.882323,-3.302788,-1.259257,6.113685,7.766820,-5.673045,-8.805032,-6.790128,2.028687,9.760187,-2.097067,-3.343837,-2.150232,-2.560815,-3.474789,-2.640209,0.507858,-3.038662,-5.684552,4.224067,-6.369235,-6.862416,0.695497,-0.690000,7.648248,-9.190832,6.325889,-3.015415,-6.127229,-8.189172,-4.524621,-7.200214,4.306735,-8.776130,-6.073276,-0.777783,9.973396,9.768732,5.366753,-6.758040,8.989741,-3.537318,1.070664,4.862080,1.843929], dtype = "float32")#candidate|9093|(45,)|const|float32
call_9092 = func_2453_call(relay.reshape(const_9093.astype('float32'), [15, 3, 1]))
call_9094 = func_2453_call(relay.reshape(const_9093.astype('float32'), [15, 3, 1]))
func_8667_call = mod.get_global_var('func_8667')
func_8668_call = mutated_mod.get_global_var('func_8668')
call_9097 = func_8667_call()
call_9098 = func_8667_call()
bop_9112 = relay.multiply(call_9097.astype('uint32'), const_9093.astype('uint32')) # shape=(5, 8, 45)
bop_9115 = relay.multiply(call_9098.astype('uint32'), const_9093.astype('uint32')) # shape=(5, 8, 45)
func_3042_call = mod.get_global_var('func_3042')
func_3043_call = mutated_mod.get_global_var('func_3043')
call_9120 = func_3042_call()
call_9121 = func_3042_call()
output = relay.Tuple([bop_9088,call_9092,bop_9112,call_9120,])
output2 = relay.Tuple([bop_9088,call_9094,bop_9115,call_9121,])
func_9127 = relay.Function([var_9086,var_9087,], output)
mod['func_9127'] = func_9127
mod = relay.transform.InferType()(mod)
mutated_mod['func_9127'] = func_9127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9127_call = mutated_mod.get_global_var('func_9127')
var_9129 = relay.var("var_9129", dtype = "float32", shape = (3, 10, 4))#candidate|9129|(3, 10, 4)|var|float32
var_9130 = relay.var("var_9130", dtype = "float32", shape = (3, 10, 4))#candidate|9130|(3, 10, 4)|var|float32
call_9128 = func_9127_call(var_9129,var_9130,)
output = call_9128
func_9131 = relay.Function([var_9129,var_9130,], output)
mutated_mod['func_9131'] = func_9131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4423_call = mod.get_global_var('func_4423')
func_4424_call = mutated_mod.get_global_var('func_4424')
call_9190 = relay.TupleGetItem(func_4423_call(), 3)
call_9191 = relay.TupleGetItem(func_4424_call(), 3)
output = call_9190
output2 = call_9191
func_9192 = relay.Function([], output)
mod['func_9192'] = func_9192
mod = relay.transform.InferType()(mod)
output = func_9192()
func_9193 = relay.Function([], output)
mutated_mod['func_9193'] = func_9193
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9194 = relay.var("var_9194", dtype = "int16", shape = (1, 7, 4))#candidate|9194|(1, 7, 4)|var|int16
var_9195 = relay.var("var_9195", dtype = "int16", shape = (14, 7, 4))#candidate|9195|(14, 7, 4)|var|int16
bop_9196 = relay.logical_xor(var_9194.astype('int16'), var_9195.astype('int16')) # shape=(14, 7, 4)
output = bop_9196
output2 = bop_9196
func_9220 = relay.Function([var_9194,var_9195,], output)
mod['func_9220'] = func_9220
mod = relay.transform.InferType()(mod)
var_9221 = relay.var("var_9221", dtype = "int16", shape = (1, 7, 4))#candidate|9221|(1, 7, 4)|var|int16
var_9222 = relay.var("var_9222", dtype = "int16", shape = (14, 7, 4))#candidate|9222|(14, 7, 4)|var|int16
output = func_9220(var_9221,var_9222,)
func_9223 = relay.Function([var_9221,var_9222,], output)
mutated_mod['func_9223'] = func_9223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3795_call = mod.get_global_var('func_3795')
func_3796_call = mutated_mod.get_global_var('func_3796')
call_9238 = relay.TupleGetItem(func_3795_call(), 0)
call_9239 = relay.TupleGetItem(func_3796_call(), 0)
output = call_9238
output2 = call_9239
func_9267 = relay.Function([], output)
mod['func_9267'] = func_9267
mod = relay.transform.InferType()(mod)
mutated_mod['func_9267'] = func_9267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9267_call = mutated_mod.get_global_var('func_9267')
call_9268 = func_9267_call()
output = call_9268
func_9269 = relay.Function([], output)
mutated_mod['func_9269'] = func_9269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2190_call = mod.get_global_var('func_2190')
func_2191_call = mutated_mod.get_global_var('func_2191')
call_9280 = relay.TupleGetItem(func_2190_call(), 1)
call_9281 = relay.TupleGetItem(func_2191_call(), 1)
output = call_9280
output2 = call_9281
func_9284 = relay.Function([], output)
mod['func_9284'] = func_9284
mod = relay.transform.InferType()(mod)
output = func_9284()
func_9285 = relay.Function([], output)
mutated_mod['func_9285'] = func_9285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_9289 = relay.TupleGetItem(func_4250_call(), 2)
call_9290 = relay.TupleGetItem(func_4251_call(), 2)
output = call_9289
output2 = call_9290
func_9308 = relay.Function([], output)
mod['func_9308'] = func_9308
mod = relay.transform.InferType()(mod)
output = func_9308()
func_9309 = relay.Function([], output)
mutated_mod['func_9309'] = func_9309
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9407 = relay.var("var_9407", dtype = "bool", shape = (2, 10, 7))#candidate|9407|(2, 10, 7)|var|bool
var_9408 = relay.var("var_9408", dtype = "bool", shape = (2, 10, 7))#candidate|9408|(2, 10, 7)|var|bool
bop_9409 = relay.logical_or(var_9407.astype('bool'), relay.reshape(var_9408.astype('bool'), relay.shape_of(var_9407))) # shape=(2, 10, 7)
func_7309_call = mod.get_global_var('func_7309')
func_7310_call = mutated_mod.get_global_var('func_7310')
call_9427 = relay.TupleGetItem(func_7309_call(), 0)
call_9428 = relay.TupleGetItem(func_7310_call(), 0)
var_9433 = relay.var("var_9433", dtype = "bool", shape = (2, 10, 7))#candidate|9433|(2, 10, 7)|var|bool
bop_9434 = relay.floor_divide(var_9407.astype('float32'), relay.reshape(var_9433.astype('float32'), relay.shape_of(var_9407))) # shape=(2, 10, 7)
output = relay.Tuple([bop_9409,call_9427,bop_9434,])
output2 = relay.Tuple([bop_9409,call_9428,bop_9434,])
func_9449 = relay.Function([var_9407,var_9408,var_9433,], output)
mod['func_9449'] = func_9449
mod = relay.transform.InferType()(mod)
mutated_mod['func_9449'] = func_9449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9449_call = mutated_mod.get_global_var('func_9449')
var_9451 = relay.var("var_9451", dtype = "bool", shape = (2, 10, 7))#candidate|9451|(2, 10, 7)|var|bool
var_9452 = relay.var("var_9452", dtype = "bool", shape = (2, 10, 7))#candidate|9452|(2, 10, 7)|var|bool
var_9453 = relay.var("var_9453", dtype = "bool", shape = (2, 10, 7))#candidate|9453|(2, 10, 7)|var|bool
call_9450 = func_9449_call(var_9451,var_9452,var_9453,)
output = call_9450
func_9454 = relay.Function([var_9451,var_9452,var_9453,], output)
mutated_mod['func_9454'] = func_9454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3042_call = mod.get_global_var('func_3042')
func_3043_call = mutated_mod.get_global_var('func_3043')
call_9458 = func_3042_call()
call_9459 = func_3042_call()
output = call_9458
output2 = call_9459
func_9460 = relay.Function([], output)
mod['func_9460'] = func_9460
mod = relay.transform.InferType()(mod)
mutated_mod['func_9460'] = func_9460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9460_call = mutated_mod.get_global_var('func_9460')
call_9461 = func_9460_call()
output = call_9461
func_9462 = relay.Function([], output)
mutated_mod['func_9462'] = func_9462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_9463 = func_1931_call()
call_9464 = func_1931_call()
func_7210_call = mod.get_global_var('func_7210')
func_7212_call = mutated_mod.get_global_var('func_7212')
call_9467 = func_7210_call()
call_9468 = func_7210_call()
func_6953_call = mod.get_global_var('func_6953')
func_6956_call = mutated_mod.get_global_var('func_6956')
var_9473 = relay.var("var_9473", dtype = "uint16", shape = (64,))#candidate|9473|(64,)|var|uint16
call_9472 = relay.TupleGetItem(func_6953_call(relay.reshape(var_9473.astype('uint16'), [64,])), 0)
call_9474 = relay.TupleGetItem(func_6956_call(relay.reshape(var_9473.astype('uint16'), [64,])), 0)
func_3033_call = mod.get_global_var('func_3033')
func_3036_call = mutated_mod.get_global_var('func_3036')
const_9477 = relay.const([7.101136,6.865082,4.414198,0.561539,-0.449026,-2.657433,5.003874,4.849215,-2.916330,8.539633,7.145340,7.261476,4.813452,4.747998,5.496641,-8.711641,-7.030422,7.196525,6.748306,5.544806,4.410543,9.440378,-9.004038,1.349446,8.953507,3.896483,3.716543,5.378410,-3.538341,9.794762,-1.960437,-6.790068,-7.024582,9.306146,-8.013969,6.845882,-9.683348,-4.140880,7.936631,2.872289,-2.468524,-9.350835,7.713957,7.676293,-3.695257,-9.272958,-6.259548,3.607110,-9.076526,-9.926881,2.327613,1.497170,-5.295980,5.383561,8.093008,2.079290,3.042217,6.752057,7.111137,7.774297,-3.542809,-3.968227,-8.634285,8.395654,-5.735614,-0.673597,9.888025,-7.282744,7.135712,5.445969,-0.220213,3.851943,-3.603060,4.661735,3.859353,-1.846375,-4.265480,-1.628275,-3.975163,4.810774,-9.517559,3.071199,4.591503,7.947818,8.457204,2.131676,8.993240,9.358561,-9.332132,7.209352,4.146473,3.305059,3.407318,6.533073,1.051406,-5.484707,-3.131655,4.809535,2.056109,-6.970739,3.043408,4.606081,-3.592388,5.540011,2.974227,-1.876183,-8.780959,-9.422582,-0.048854,2.020641,-5.382968,3.887956,3.257365,5.981072,0.450383,5.369762,0.866746,-2.366682,-6.194091,-5.559623,-1.369561,-2.067424,-1.260981,-7.012839,-8.398574,-4.862585,-8.695472,7.300464,-8.348082,-7.294483,7.494577,1.561654,-2.381738,-5.998447,2.634425,-1.925335,-9.878209,-9.402499,0.935168,6.343469,-6.768940,7.764403,1.946238,3.197798,7.472868,1.443875,0.524896,5.744623,-2.874069,-9.399353,9.897597,-2.118164,-2.179467,-2.469989,4.001579,0.721249,-2.779675,-3.660307,-4.276852,1.080553], dtype = "float64")#candidate|9477|(160,)|const|float64
call_9476 = relay.TupleGetItem(func_3033_call(relay.reshape(const_9477.astype('float64'), [160,])), 3)
call_9478 = relay.TupleGetItem(func_3036_call(relay.reshape(const_9477.astype('float64'), [160,])), 3)
func_6901_call = mod.get_global_var('func_6901')
func_6905_call = mutated_mod.get_global_var('func_6905')
var_9482 = relay.var("var_9482", dtype = "float64", shape = (5280,))#candidate|9482|(5280,)|var|float64
var_9483 = relay.var("var_9483", dtype = "float64", shape = (660,))#candidate|9483|(660,)|var|float64
var_9484 = relay.var("var_9484", dtype = "int8", shape = (1056,))#candidate|9484|(1056,)|var|int8
call_9481 = relay.TupleGetItem(func_6901_call(relay.reshape(var_9482.astype('float64'), [5, 8, 132]), relay.reshape(var_9483.astype('float64'), [660,]), relay.reshape(var_9484.astype('int8'), [1056,]), ), 1)
call_9485 = relay.TupleGetItem(func_6905_call(relay.reshape(var_9482.astype('float64'), [5, 8, 132]), relay.reshape(var_9483.astype('float64'), [660,]), relay.reshape(var_9484.astype('int8'), [1056,]), ), 1)
func_5870_call = mod.get_global_var('func_5870')
func_5871_call = mutated_mod.get_global_var('func_5871')
call_9487 = relay.TupleGetItem(func_5870_call(), 2)
call_9488 = relay.TupleGetItem(func_5871_call(), 2)
output = relay.Tuple([call_9463,call_9467,call_9472,var_9473,call_9476,const_9477,call_9481,var_9482,var_9483,var_9484,call_9487,])
output2 = relay.Tuple([call_9464,call_9468,call_9474,var_9473,call_9478,const_9477,call_9485,var_9482,var_9483,var_9484,call_9488,])
func_9489 = relay.Function([var_9473,var_9482,var_9483,var_9484,], output)
mod['func_9489'] = func_9489
mod = relay.transform.InferType()(mod)
mutated_mod['func_9489'] = func_9489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9489_call = mutated_mod.get_global_var('func_9489')
var_9491 = relay.var("var_9491", dtype = "uint16", shape = (64,))#candidate|9491|(64,)|var|uint16
var_9492 = relay.var("var_9492", dtype = "float64", shape = (5280,))#candidate|9492|(5280,)|var|float64
var_9493 = relay.var("var_9493", dtype = "float64", shape = (660,))#candidate|9493|(660,)|var|float64
var_9494 = relay.var("var_9494", dtype = "int8", shape = (1056,))#candidate|9494|(1056,)|var|int8
call_9490 = func_9489_call(var_9491,var_9492,var_9493,var_9494,)
output = call_9490
func_9495 = relay.Function([var_9491,var_9492,var_9493,var_9494,], output)
mutated_mod['func_9495'] = func_9495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2847_call = mod.get_global_var('func_2847')
func_2848_call = mutated_mod.get_global_var('func_2848')
call_9659 = relay.TupleGetItem(func_2847_call(), 0)
call_9660 = relay.TupleGetItem(func_2848_call(), 0)
var_9667 = relay.var("var_9667", dtype = "uint64", shape = (5, 8, 1))#candidate|9667|(5, 8, 1)|var|uint64
bop_9668 = relay.not_equal(call_9659.astype('bool'), relay.reshape(var_9667.astype('bool'), relay.shape_of(call_9659))) # shape=(5, 8, 1)
bop_9671 = relay.not_equal(call_9660.astype('bool'), relay.reshape(var_9667.astype('bool'), relay.shape_of(call_9660))) # shape=(5, 8, 1)
output = bop_9668
output2 = bop_9671
func_9673 = relay.Function([var_9667,], output)
mod['func_9673'] = func_9673
mod = relay.transform.InferType()(mod)
var_9674 = relay.var("var_9674", dtype = "uint64", shape = (5, 8, 1))#candidate|9674|(5, 8, 1)|var|uint64
output = func_9673(var_9674)
func_9675 = relay.Function([var_9674], output)
mutated_mod['func_9675'] = func_9675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3543_call = mod.get_global_var('func_3543')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_9935 = relay.TupleGetItem(func_3543_call(), 0)
call_9936 = relay.TupleGetItem(func_3545_call(), 0)
output = relay.Tuple([call_9935,])
output2 = relay.Tuple([call_9936,])
func_9948 = relay.Function([], output)
mod['func_9948'] = func_9948
mod = relay.transform.InferType()(mod)
mutated_mod['func_9948'] = func_9948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9948_call = mutated_mod.get_global_var('func_9948')
call_9949 = func_9948_call()
output = call_9949
func_9950 = relay.Function([], output)
mutated_mod['func_9950'] = func_9950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7434_call = mod.get_global_var('func_7434')
func_7435_call = mutated_mod.get_global_var('func_7435')
call_9973 = func_7434_call()
call_9974 = func_7434_call()
func_4938_call = mod.get_global_var('func_4938')
func_4942_call = mutated_mod.get_global_var('func_4942')
var_9991 = relay.var("var_9991", dtype = "int8", shape = (1056,))#candidate|9991|(1056,)|var|int8
var_9992 = relay.var("var_9992", dtype = "uint16", shape = (4, 16))#candidate|9992|(4, 16)|var|uint16
var_9993 = relay.var("var_9993", dtype = "float32", shape = (1014,))#candidate|9993|(1014,)|var|float32
call_9990 = relay.TupleGetItem(func_4938_call(relay.reshape(var_9991.astype('int8'), [1056,]), relay.reshape(var_9992.astype('uint16'), [64,]), relay.reshape(var_9993.astype('float32'), [1014,]), ), 1)
call_9994 = relay.TupleGetItem(func_4942_call(relay.reshape(var_9991.astype('int8'), [1056,]), relay.reshape(var_9992.astype('uint16'), [64,]), relay.reshape(var_9993.astype('float32'), [1014,]), ), 1)
bop_9995 = relay.divide(var_9991.astype('float64'), call_9973.astype('float64')) # shape=(5, 8, 1056)
bop_9998 = relay.divide(var_9991.astype('float64'), call_9974.astype('float64')) # shape=(5, 8, 1056)
output = relay.Tuple([call_9990,var_9992,var_9993,bop_9995,])
output2 = relay.Tuple([call_9994,var_9992,var_9993,bop_9998,])
func_10004 = relay.Function([var_9991,var_9992,var_9993,], output)
mod['func_10004'] = func_10004
mod = relay.transform.InferType()(mod)
var_10005 = relay.var("var_10005", dtype = "int8", shape = (1056,))#candidate|10005|(1056,)|var|int8
var_10006 = relay.var("var_10006", dtype = "uint16", shape = (4, 16))#candidate|10006|(4, 16)|var|uint16
var_10007 = relay.var("var_10007", dtype = "float32", shape = (1014,))#candidate|10007|(1014,)|var|float32
output = func_10004(var_10005,var_10006,var_10007,)
func_10008 = relay.Function([var_10005,var_10006,var_10007,], output)
mutated_mod['func_10008'] = func_10008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9192_call = mod.get_global_var('func_9192')
func_9193_call = mutated_mod.get_global_var('func_9193')
call_10072 = func_9192_call()
call_10073 = func_9192_call()
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_10102 = func_3507_call()
call_10103 = func_3507_call()
func_8621_call = mod.get_global_var('func_8621')
func_8623_call = mutated_mod.get_global_var('func_8623')
call_10108 = relay.TupleGetItem(func_8621_call(), 3)
call_10109 = relay.TupleGetItem(func_8623_call(), 3)
output = relay.Tuple([call_10072,call_10102,call_10108,])
output2 = relay.Tuple([call_10073,call_10103,call_10109,])
func_10130 = relay.Function([], output)
mod['func_10130'] = func_10130
mod = relay.transform.InferType()(mod)
mutated_mod['func_10130'] = func_10130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10130_call = mutated_mod.get_global_var('func_10130')
call_10131 = func_10130_call()
output = call_10131
func_10132 = relay.Function([], output)
mutated_mod['func_10132'] = func_10132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3759_call = mod.get_global_var('func_3759')
func_3760_call = mutated_mod.get_global_var('func_3760')
call_10138 = relay.TupleGetItem(func_3759_call(), 0)
call_10139 = relay.TupleGetItem(func_3760_call(), 0)
func_5490_call = mod.get_global_var('func_5490')
func_5492_call = mutated_mod.get_global_var('func_5492')
call_10165 = relay.TupleGetItem(func_5490_call(), 3)
call_10166 = relay.TupleGetItem(func_5492_call(), 3)
func_1696_call = mod.get_global_var('func_1696')
func_1697_call = mutated_mod.get_global_var('func_1697')
call_10169 = func_1696_call()
call_10170 = func_1696_call()
output = relay.Tuple([call_10138,call_10165,call_10169,])
output2 = relay.Tuple([call_10139,call_10166,call_10170,])
func_10172 = relay.Function([], output)
mod['func_10172'] = func_10172
mod = relay.transform.InferType()(mod)
mutated_mod['func_10172'] = func_10172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10172_call = mutated_mod.get_global_var('func_10172')
call_10173 = func_10172_call()
output = call_10173
func_10174 = relay.Function([], output)
mutated_mod['func_10174'] = func_10174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5153_call = mod.get_global_var('func_5153')
func_5154_call = mutated_mod.get_global_var('func_5154')
call_10178 = relay.TupleGetItem(func_5153_call(), 0)
call_10179 = relay.TupleGetItem(func_5154_call(), 0)
output = relay.Tuple([call_10178,])
output2 = relay.Tuple([call_10179,])
func_10187 = relay.Function([], output)
mod['func_10187'] = func_10187
mod = relay.transform.InferType()(mod)
mutated_mod['func_10187'] = func_10187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10187_call = mutated_mod.get_global_var('func_10187')
call_10188 = func_10187_call()
output = call_10188
func_10189 = relay.Function([], output)
mutated_mod['func_10189'] = func_10189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6475_call = mod.get_global_var('func_6475')
func_6477_call = mutated_mod.get_global_var('func_6477')
call_10207 = func_6475_call()
call_10208 = func_6475_call()
func_4012_call = mod.get_global_var('func_4012')
func_4014_call = mutated_mod.get_global_var('func_4014')
call_10221 = relay.TupleGetItem(func_4012_call(), 0)
call_10222 = relay.TupleGetItem(func_4014_call(), 0)
bop_10227 = relay.maximum(call_10221.astype('int64'), call_10207.astype('int64')) # shape=(5, 8, 1056)
bop_10230 = relay.maximum(call_10222.astype('int64'), call_10208.astype('int64')) # shape=(5, 8, 1056)
func_7589_call = mod.get_global_var('func_7589')
func_7592_call = mutated_mod.get_global_var('func_7592')
call_10236 = relay.TupleGetItem(func_7589_call(relay.reshape(call_10221.astype('int8'), [2, 528])), 4)
call_10237 = relay.TupleGetItem(func_7592_call(relay.reshape(call_10221.astype('int8'), [2, 528])), 4)
func_6982_call = mod.get_global_var('func_6982')
func_6983_call = mutated_mod.get_global_var('func_6983')
call_10241 = relay.TupleGetItem(func_6982_call(), 0)
call_10242 = relay.TupleGetItem(func_6983_call(), 0)
func_7680_call = mod.get_global_var('func_7680')
func_7682_call = mutated_mod.get_global_var('func_7682')
var_10245 = relay.var("var_10245", dtype = "float32", shape = (1584,))#candidate|10245|(1584,)|var|float32
call_10244 = relay.TupleGetItem(func_7680_call(relay.reshape(var_10245.astype('float32'), [16, 11, 9])), 0)
call_10246 = relay.TupleGetItem(func_7682_call(relay.reshape(var_10245.astype('float32'), [16, 11, 9])), 0)
output = relay.Tuple([bop_10227,call_10236,call_10241,call_10244,var_10245,])
output2 = relay.Tuple([bop_10230,call_10237,call_10242,call_10246,var_10245,])
func_10260 = relay.Function([var_10245,], output)
mod['func_10260'] = func_10260
mod = relay.transform.InferType()(mod)
var_10261 = relay.var("var_10261", dtype = "float32", shape = (1584,))#candidate|10261|(1584,)|var|float32
output = func_10260(var_10261)
func_10262 = relay.Function([var_10261], output)
mutated_mod['func_10262'] = func_10262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_10329 = relay.TupleGetItem(func_4250_call(), 2)
call_10330 = relay.TupleGetItem(func_4251_call(), 2)
func_9192_call = mod.get_global_var('func_9192')
func_9193_call = mutated_mod.get_global_var('func_9193')
call_10344 = func_9192_call()
call_10345 = func_9192_call()
output = relay.Tuple([call_10329,call_10344,])
output2 = relay.Tuple([call_10330,call_10345,])
func_10385 = relay.Function([], output)
mod['func_10385'] = func_10385
mod = relay.transform.InferType()(mod)
output = func_10385()
func_10386 = relay.Function([], output)
mutated_mod['func_10386'] = func_10386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10172_call = mod.get_global_var('func_10172')
func_10174_call = mutated_mod.get_global_var('func_10174')
call_10452 = relay.TupleGetItem(func_10172_call(), 2)
call_10453 = relay.TupleGetItem(func_10174_call(), 2)
output = relay.Tuple([call_10452,])
output2 = relay.Tuple([call_10453,])
func_10476 = relay.Function([], output)
mod['func_10476'] = func_10476
mod = relay.transform.InferType()(mod)
output = func_10476()
func_10477 = relay.Function([], output)
mutated_mod['func_10477'] = func_10477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_10535 = relay.TupleGetItem(func_3682_call(), 0)
call_10536 = relay.TupleGetItem(func_3684_call(), 0)
func_3759_call = mod.get_global_var('func_3759')
func_3760_call = mutated_mod.get_global_var('func_3760')
call_10559 = relay.TupleGetItem(func_3759_call(), 1)
call_10560 = relay.TupleGetItem(func_3760_call(), 1)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_10566 = relay.TupleGetItem(func_3396_call(), 0)
call_10567 = relay.TupleGetItem(func_3398_call(), 0)
output = relay.Tuple([call_10535,call_10559,call_10566,])
output2 = relay.Tuple([call_10536,call_10560,call_10567,])
func_10577 = relay.Function([], output)
mod['func_10577'] = func_10577
mod = relay.transform.InferType()(mod)
mutated_mod['func_10577'] = func_10577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10577_call = mutated_mod.get_global_var('func_10577')
call_10578 = func_10577_call()
output = call_10578
func_10579 = relay.Function([], output)
mutated_mod['func_10579'] = func_10579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4614_call = mod.get_global_var('func_4614')
func_4615_call = mutated_mod.get_global_var('func_4615')
call_10628 = relay.TupleGetItem(func_4614_call(), 0)
call_10629 = relay.TupleGetItem(func_4615_call(), 0)
output = relay.Tuple([call_10628,])
output2 = relay.Tuple([call_10629,])
func_10631 = relay.Function([], output)
mod['func_10631'] = func_10631
mod = relay.transform.InferType()(mod)
mutated_mod['func_10631'] = func_10631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10631_call = mutated_mod.get_global_var('func_10631')
call_10632 = func_10631_call()
output = call_10632
func_10633 = relay.Function([], output)
mutated_mod['func_10633'] = func_10633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4478_call = mod.get_global_var('func_4478')
func_4480_call = mutated_mod.get_global_var('func_4480')
call_10701 = relay.TupleGetItem(func_4478_call(), 0)
call_10702 = relay.TupleGetItem(func_4480_call(), 0)
func_4423_call = mod.get_global_var('func_4423')
func_4424_call = mutated_mod.get_global_var('func_4424')
call_10707 = relay.TupleGetItem(func_4423_call(), 0)
call_10708 = relay.TupleGetItem(func_4424_call(), 0)
output = relay.Tuple([call_10701,call_10707,])
output2 = relay.Tuple([call_10702,call_10708,])
func_10720 = relay.Function([], output)
mod['func_10720'] = func_10720
mod = relay.transform.InferType()(mod)
output = func_10720()
func_10721 = relay.Function([], output)
mutated_mod['func_10721'] = func_10721
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10736 = relay.var("var_10736", dtype = "int64", shape = (3, 3, 3))#candidate|10736|(3, 3, 3)|var|int64
const_10737 = relay.const([[[2,-4,10],[-4,7,-5],[-8,8,-9]],[[4,-2,-6],[-10,2,4],[5,-7,-6]],[[8,-6,-1],[-2,4,-2],[-2,2,5]]], dtype = "int64")#candidate|10737|(3, 3, 3)|const|int64
bop_10738 = relay.not_equal(var_10736.astype('bool'), relay.reshape(const_10737.astype('bool'), relay.shape_of(var_10736))) # shape=(3, 3, 3)
func_10720_call = mod.get_global_var('func_10720')
func_10721_call = mutated_mod.get_global_var('func_10721')
call_10746 = relay.TupleGetItem(func_10720_call(), 0)
call_10747 = relay.TupleGetItem(func_10721_call(), 0)
output = relay.Tuple([bop_10738,call_10746,])
output2 = relay.Tuple([bop_10738,call_10747,])
func_10780 = relay.Function([var_10736,], output)
mod['func_10780'] = func_10780
mod = relay.transform.InferType()(mod)
mutated_mod['func_10780'] = func_10780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10781 = relay.var("var_10781", dtype = "int64", shape = (3, 3, 3))#candidate|10781|(3, 3, 3)|var|int64
func_10780_call = mutated_mod.get_global_var('func_10780')
call_10782 = func_10780_call(var_10781)
output = call_10782
func_10783 = relay.Function([var_10781], output)
mutated_mod['func_10783'] = func_10783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4669_call = mod.get_global_var('func_4669')
func_4670_call = mutated_mod.get_global_var('func_4670')
call_10810 = relay.TupleGetItem(func_4669_call(), 0)
call_10811 = relay.TupleGetItem(func_4670_call(), 0)
var_10818 = relay.var("var_10818", dtype = "int16", shape = (5, 8, 7))#candidate|10818|(5, 8, 7)|var|int16
bop_10819 = relay.greater(call_10810.astype('bool'), var_10818.astype('bool')) # shape=(5, 8, 7)
bop_10822 = relay.greater(call_10811.astype('bool'), var_10818.astype('bool')) # shape=(5, 8, 7)
func_2294_call = mod.get_global_var('func_2294')
func_2296_call = mutated_mod.get_global_var('func_2296')
call_10824 = relay.TupleGetItem(func_2294_call(), 0)
call_10825 = relay.TupleGetItem(func_2296_call(), 0)
uop_10826 = relay.log(var_10818.astype('float64')) # shape=(5, 8, 7)
func_5870_call = mod.get_global_var('func_5870')
func_5871_call = mutated_mod.get_global_var('func_5871')
call_10829 = relay.TupleGetItem(func_5870_call(), 0)
call_10830 = relay.TupleGetItem(func_5871_call(), 0)
output = relay.Tuple([bop_10819,call_10824,uop_10826,call_10829,])
output2 = relay.Tuple([bop_10822,call_10825,uop_10826,call_10830,])
func_10839 = relay.Function([var_10818,], output)
mod['func_10839'] = func_10839
mod = relay.transform.InferType()(mod)
var_10840 = relay.var("var_10840", dtype = "int16", shape = (5, 8, 7))#candidate|10840|(5, 8, 7)|var|int16
output = func_10839(var_10840)
func_10841 = relay.Function([var_10840], output)
mutated_mod['func_10841'] = func_10841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8205_call = mod.get_global_var('func_8205')
func_8206_call = mutated_mod.get_global_var('func_8206')
call_10864 = func_8205_call()
call_10865 = func_8205_call()
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_10910 = func_3507_call()
call_10911 = func_3507_call()
func_4647_call = mod.get_global_var('func_4647')
func_4649_call = mutated_mod.get_global_var('func_4649')
call_10913 = relay.TupleGetItem(func_4647_call(), 0)
call_10914 = relay.TupleGetItem(func_4649_call(), 0)
output = relay.Tuple([call_10864,call_10910,call_10913,])
output2 = relay.Tuple([call_10865,call_10911,call_10914,])
func_10928 = relay.Function([], output)
mod['func_10928'] = func_10928
mod = relay.transform.InferType()(mod)
mutated_mod['func_10928'] = func_10928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10928_call = mutated_mod.get_global_var('func_10928')
call_10929 = func_10928_call()
output = call_10929
func_10930 = relay.Function([], output)
mutated_mod['func_10930'] = func_10930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8667_call = mod.get_global_var('func_8667')
func_8668_call = mutated_mod.get_global_var('func_8668')
call_10964 = func_8667_call()
call_10965 = func_8667_call()
var_10966 = relay.var("var_10966", dtype = "bool", shape = (5, 8, 12))#candidate|10966|(5, 8, 12)|var|bool
bop_10967 = relay.multiply(call_10964.astype('float32'), var_10966.astype('float32')) # shape=(5, 8, 12)
bop_10970 = relay.multiply(call_10965.astype('float32'), var_10966.astype('float32')) # shape=(5, 8, 12)
output = relay.Tuple([bop_10967,])
output2 = relay.Tuple([bop_10970,])
func_10978 = relay.Function([var_10966,], output)
mod['func_10978'] = func_10978
mod = relay.transform.InferType()(mod)
mutated_mod['func_10978'] = func_10978
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10979 = relay.var("var_10979", dtype = "bool", shape = (5, 8, 12))#candidate|10979|(5, 8, 12)|var|bool
func_10978_call = mutated_mod.get_global_var('func_10978')
call_10980 = func_10978_call(var_10979)
output = call_10980
func_10981 = relay.Function([var_10979], output)
mutated_mod['func_10981'] = func_10981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5153_call = mod.get_global_var('func_5153')
func_5154_call = mutated_mod.get_global_var('func_5154')
call_10983 = relay.TupleGetItem(func_5153_call(), 0)
call_10984 = relay.TupleGetItem(func_5154_call(), 0)
func_5745_call = mod.get_global_var('func_5745')
func_5748_call = mutated_mod.get_global_var('func_5748')
const_10988 = relay.const([[-5,-3,3,-2,-1,-2],[4,-5,7,7,-10,5],[-10,4,10,-9,-10,9],[-2,-2,8,7,7,4],[-8,7,3,-2,10,10],[1,4,2,7,-8,7],[4,-9,-6,6,-5,3],[-8,-3,-2,10,-2,7],[2,10,-2,6,-8,8],[8,-7,-8,3,7,6],[-8,-3,1,-6,3,-2],[2,-10,5,-6,3,-7],[6,-8,-7,2,-1,8],[6,-4,10,3,-6,-2],[-2,-3,2,7,2,-2]], dtype = "int8")#candidate|10988|(15, 6)|const|int8
call_10987 = relay.TupleGetItem(func_5745_call(relay.reshape(const_10988.astype('int8'), [15, 2, 3]), relay.reshape(const_10988.astype('int8'), [15, 2, 3]), ), 0)
call_10989 = relay.TupleGetItem(func_5748_call(relay.reshape(const_10988.astype('int8'), [15, 2, 3]), relay.reshape(const_10988.astype('int8'), [15, 2, 3]), ), 0)
func_4669_call = mod.get_global_var('func_4669')
func_4670_call = mutated_mod.get_global_var('func_4670')
call_10991 = relay.TupleGetItem(func_4669_call(), 0)
call_10992 = relay.TupleGetItem(func_4670_call(), 0)
output = relay.Tuple([call_10983,call_10987,const_10988,call_10991,])
output2 = relay.Tuple([call_10984,call_10989,const_10988,call_10992,])
func_10993 = relay.Function([], output)
mod['func_10993'] = func_10993
mod = relay.transform.InferType()(mod)
mutated_mod['func_10993'] = func_10993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10993_call = mutated_mod.get_global_var('func_10993')
call_10994 = func_10993_call()
output = call_10994
func_10995 = relay.Function([], output)
mutated_mod['func_10995'] = func_10995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3877_call = mod.get_global_var('func_3877')
func_3878_call = mutated_mod.get_global_var('func_3878')
call_11154 = relay.TupleGetItem(func_3877_call(), 0)
call_11155 = relay.TupleGetItem(func_3878_call(), 0)
func_3614_call = mod.get_global_var('func_3614')
func_3616_call = mutated_mod.get_global_var('func_3616')
var_11173 = relay.var("var_11173", dtype = "float64", shape = (480,))#candidate|11173|(480,)|var|float64
call_11172 = relay.TupleGetItem(func_3614_call(relay.reshape(var_11173.astype('float64'), [5, 8, 12])), 0)
call_11174 = relay.TupleGetItem(func_3616_call(relay.reshape(var_11173.astype('float64'), [5, 8, 12])), 0)
output = relay.Tuple([call_11154,call_11172,var_11173,])
output2 = relay.Tuple([call_11155,call_11174,var_11173,])
func_11175 = relay.Function([var_11173,], output)
mod['func_11175'] = func_11175
mod = relay.transform.InferType()(mod)
var_11176 = relay.var("var_11176", dtype = "float64", shape = (480,))#candidate|11176|(480,)|var|float64
output = func_11175(var_11176)
func_11177 = relay.Function([var_11176], output)
mutated_mod['func_11177'] = func_11177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7490_call = mod.get_global_var('func_7490')
func_7491_call = mutated_mod.get_global_var('func_7491')
call_11259 = relay.TupleGetItem(func_7490_call(), 0)
call_11260 = relay.TupleGetItem(func_7491_call(), 0)
var_11269 = relay.var("var_11269", dtype = "uint64", shape = (5, 8, 8))#candidate|11269|(5, 8, 8)|var|uint64
bop_11270 = relay.less(call_11259.astype('bool'), var_11269.astype('bool')) # shape=(5, 8, 8)
bop_11273 = relay.less(call_11260.astype('bool'), var_11269.astype('bool')) # shape=(5, 8, 8)
output = relay.Tuple([bop_11270,])
output2 = relay.Tuple([bop_11273,])
func_11276 = relay.Function([var_11269,], output)
mod['func_11276'] = func_11276
mod = relay.transform.InferType()(mod)
var_11277 = relay.var("var_11277", dtype = "uint64", shape = (5, 8, 8))#candidate|11277|(5, 8, 8)|var|uint64
output = func_11276(var_11277)
func_11278 = relay.Function([var_11277], output)
mutated_mod['func_11278'] = func_11278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1933_call = mutated_mod.get_global_var('func_1933')
call_11280 = func_1931_call()
call_11281 = func_1931_call()
output = relay.Tuple([call_11280,])
output2 = relay.Tuple([call_11281,])
func_11286 = relay.Function([], output)
mod['func_11286'] = func_11286
mod = relay.transform.InferType()(mod)
mutated_mod['func_11286'] = func_11286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11286_call = mutated_mod.get_global_var('func_11286')
call_11287 = func_11286_call()
output = call_11287
func_11288 = relay.Function([], output)
mutated_mod['func_11288'] = func_11288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6982_call = mod.get_global_var('func_6982')
func_6983_call = mutated_mod.get_global_var('func_6983')
call_11297 = relay.TupleGetItem(func_6982_call(), 0)
call_11298 = relay.TupleGetItem(func_6983_call(), 0)
func_1331_call = mod.get_global_var('func_1331')
func_1334_call = mutated_mod.get_global_var('func_1334')
const_11306 = relay.const([[-2,-2,-10,10,1,-7,-5,-8,-1,-7,-8,-1,-5,-6,4,4,-5,-3,-9,6,-10,-8,9,6,-6,3,7,5,-6,-10,-3,6,-3,2,-4,3,-5,-9,-8,4,-9,7,1,-7,5,7,4,-3,-4,10,-7,-10,-5,-5,-3,6,-8,-7,5,7,-3,-5,8,7,-6,10,9,6,-10,-6,3,-4,-5,9,-8,9,1,-2,5,-2,6,6,3,-9,4,5,-7,8,3,3,4,-3,-7,5,-2,-3,-1,4,-3,-7,8,4,-3,1,-10,7,4,10,-5,-3,3,7,-7,8,-4,6,-8,-1,-3,-7,5,-8,6,-2,6,-9,-5,3,-5,-1,5,-5,8,-4,-8,-5,-8,4,2,4,3,-6,-8,-10,1,6,-9,-1,-4,-7,7,-5,-6,9,-7,7,-6,10,-4,-9,-2,-1,5,-7,8,-1,-5,-1,7,8,-5,-4,7,-5,4,6,-10,-6,-10,3,-6,-4,-3,1,-5,2,3,-10,-1,3,-2,1,7,-6,2,-4,4,-9,-3,4,1,-7,-3,-7,2,10,-9,6,10,-3,-9,-1,5,9,2,5,9,-10,-8,9,-8,-6,3,5,3,-8,-6,-7,-8,-10,-8,-4,6,-3,2,6,2,9,3,-9,-1,-1,5,-10,4,5,-5,-1,4,7,6,6,-5,-5,10,-5,2,-9,-3,2,-9,1,6,6],[6,6,7,3,-8,8,-2,-8,-10,9,-4,-3,8,8,6,3,-7,5,2,4,6,-7,-9,-1,2,4,-3,-10,1,-4,-1,-10,-6,2,4,-8,-2,-9,10,1,1,7,-4,-4,4,-3,-5,-5,9,10,5,-4,-5,-7,-2,-6,-6,7,-9,-7,9,9,-5,8,2,-7,-8,-2,-5,-9,-9,-2,-7,5,9,8,-3,3,-1,-2,-1,-8,4,-3,2,8,4,-6,-10,-6,2,9,2,3,-5,4,6,6,-3,8,10,7,-7,-6,4,6,-7,-3,-8,-10,-3,-10,8,6,-4,9,2,9,-8,6,8,-2,-8,-2,3,-1,8,-3,7,10,-6,9,-6,7,5,8,5,8,4,10,-4,2,-4,10,8,7,10,4,-4,2,4,1,-9,-3,-9,-10,5,6,-1,-5,8,-5,-7,4,9,9,5,5,10,-7,-10,-3,1,8,-8,10,-4,2,-1,-3,4,6,-3,-5,8,4,-1,6,-8,1,-7,2,6,-3,2,-9,-7,8,-7,-4,7,2,-7,-7,3,3,-10,3,8,-3,1,9,-9,9,1,9,-1,3,1,5,1,6,-2,7,5,2,-2,-4,-9,-4,-6,6,8,-7,3,-3,-1,-4,-5,5,-1,-6,8,-3,-4,-5,4,10,-5,8,-3,2,9,-7,7,4,8,10,-1,1,1,-8,1,4],[-6,-4,5,-3,2,-1,-3,-8,5,7,2,-3,-7,-10,10,-6,8,5,8,10,-9,10,5,5,9,-8,-1,5,-2,6,-9,-8,2,2,3,-9,-10,8,-8,-5,-4,-9,-4,3,-9,5,1,9,-9,3,-3,-8,-3,10,7,10,10,8,-4,-9,-10,-5,10,-4,4,-10,-10,-2,5,4,-7,5,2,1,-4,10,-5,-3,-8,-3,-4,9,-3,7,-3,10,-5,-9,-10,-4,-3,8,-9,4,-10,2,-9,-8,-2,-10,5,-4,7,-7,4,-9,6,-4,10,4,4,-2,7,-7,4,-1,-7,9,-8,9,6,8,7,8,-9,-5,-10,-8,-10,5,10,3,3,-1,8,3,-2,-7,5,6,10,9,-10,-9,1,4,-4,-1,1,-7,4,5,3,4,-9,-1,2,3,8,4,-7,-1,7,7,-5,-9,4,-6,-5,-4,1,-7,7,6,-1,-3,9,9,-9,6,-1,-5,-8,-2,3,9,-1,-8,-6,4,-7,6,-4,-3,-3,6,-3,-1,-2,-4,-10,9,-9,2,3,1,-6,5,-3,-10,7,-2,-7,-9,-7,3,8,-1,-9,2,-10,2,-1,-5,-7,-3,-10,-5,10,-3,-9,-4,-8,-3,9,-1,-8,6,-1,-6,-3,3,3,-8,3,10,10,8,3,7,5,-3,-2,-2,8,-3,6,4,-7,-4,8,2,-2,-7],[2,-6,-1,-9,6,10,-1,6,-3,9,-5,-8,-9,-2,-3,-5,-3,3,8,9,-5,-9,-3,4,-5,6,7,4,8,-8,-5,5,2,3,10,-5,2,1,-6,3,-9,-1,5,-2,-3,4,-3,-7,-9,-6,-2,-5,-4,-2,-3,-4,-4,-1,-2,3,-3,-5,-8,-3,1,-5,10,-7,-8,9,-4,6,-9,8,-9,-9,8,1,6,-2,-3,10,-6,-10,-6,6,1,7,-8,-3,7,-1,6,2,8,-9,-10,-4,7,-1,-4,-4,-8,7,7,-2,10,1,9,-7,7,6,8,6,-6,10,-1,-5,5,-4,1,-9,3,-8,5,-7,-3,2,7,-7,-2,-2,-3,-3,-8,3,4,10,-5,-10,-6,-3,-4,-10,-4,3,-6,-10,-2,9,1,-9,5,-4,8,1,3,-2,-10,7,3,-1,-4,10,-5,4,-1,4,-2,6,-4,-5,2,3,4,-7,1,6,8,-9,-4,-8,-8,1,-1,-4,-8,2,-8,2,-9,9,-7,-5,-2,6,9,-1,8,-9,-2,6,1,8,4,-1,10,-1,6,2,10,4,-3,8,-8,2,9,-8,5,10,-9,-2,-3,-6,9,-9,-7,10,-9,-3,5,-6,5,-3,-3,2,3,9,-7,7,4,-6,-8,-10,5,3,-1,6,-5,8,1,-8,-4,-4,-5,-6,6,9,-10,-2,-2,-7,-8,-9]], dtype = "int8")#candidate|11306|(4, 264)|const|int8
call_11305 = relay.TupleGetItem(func_1331_call(relay.reshape(const_11306.astype('int8'), [1056,])), 4)
call_11307 = relay.TupleGetItem(func_1334_call(relay.reshape(const_11306.astype('int8'), [1056,])), 4)
var_11317 = relay.var("var_11317", dtype = "int8", shape = (4, 264))#candidate|11317|(4, 264)|var|int8
bop_11318 = relay.bitwise_or(const_11306.astype('uint64'), relay.reshape(var_11317.astype('uint64'), relay.shape_of(const_11306))) # shape=(4, 264)
output = relay.Tuple([call_11297,call_11305,bop_11318,])
output2 = relay.Tuple([call_11298,call_11307,bop_11318,])
func_11329 = relay.Function([var_11317,], output)
mod['func_11329'] = func_11329
mod = relay.transform.InferType()(mod)
var_11330 = relay.var("var_11330", dtype = "int8", shape = (4, 264))#candidate|11330|(4, 264)|var|int8
output = func_11329(var_11330)
func_11331 = relay.Function([var_11330], output)
mutated_mod['func_11331'] = func_11331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7052_call = mod.get_global_var('func_7052')
func_7054_call = mutated_mod.get_global_var('func_7054')
call_11344 = func_7052_call()
call_11345 = func_7052_call()
output = call_11344
output2 = call_11345
func_11364 = relay.Function([], output)
mod['func_11364'] = func_11364
mod = relay.transform.InferType()(mod)
mutated_mod['func_11364'] = func_11364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11364_call = mutated_mod.get_global_var('func_11364')
call_11365 = func_11364_call()
output = call_11365
func_11366 = relay.Function([], output)
mutated_mod['func_11366'] = func_11366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7943_call = mod.get_global_var('func_7943')
func_7945_call = mutated_mod.get_global_var('func_7945')
call_11575 = func_7943_call()
call_11576 = func_7943_call()
output = relay.Tuple([call_11575,])
output2 = relay.Tuple([call_11576,])
func_11580 = relay.Function([], output)
mod['func_11580'] = func_11580
mod = relay.transform.InferType()(mod)
mutated_mod['func_11580'] = func_11580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11580_call = mutated_mod.get_global_var('func_11580')
call_11581 = func_11580_call()
output = call_11581
func_11582 = relay.Function([], output)
mutated_mod['func_11582'] = func_11582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6475_call = mod.get_global_var('func_6475')
func_6477_call = mutated_mod.get_global_var('func_6477')
call_11583 = func_6475_call()
call_11584 = func_6475_call()
output = call_11583
output2 = call_11584
func_11594 = relay.Function([], output)
mod['func_11594'] = func_11594
mod = relay.transform.InferType()(mod)
output = func_11594()
func_11595 = relay.Function([], output)
mutated_mod['func_11595'] = func_11595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8063_call = mod.get_global_var('func_8063')
func_8065_call = mutated_mod.get_global_var('func_8065')
call_11604 = relay.TupleGetItem(func_8063_call(), 0)
call_11605 = relay.TupleGetItem(func_8065_call(), 0)
func_2977_call = mod.get_global_var('func_2977')
func_2980_call = mutated_mod.get_global_var('func_2980')
var_11609 = relay.var("var_11609", dtype = "uint16", shape = (64,))#candidate|11609|(64,)|var|uint16
call_11608 = relay.TupleGetItem(func_2977_call(relay.reshape(var_11609.astype('uint16'), [2, 32])), 0)
call_11610 = relay.TupleGetItem(func_2980_call(relay.reshape(var_11609.astype('uint16'), [2, 32])), 0)
output = relay.Tuple([call_11604,call_11608,var_11609,])
output2 = relay.Tuple([call_11605,call_11610,var_11609,])
func_11620 = relay.Function([var_11609,], output)
mod['func_11620'] = func_11620
mod = relay.transform.InferType()(mod)
var_11621 = relay.var("var_11621", dtype = "uint16", shape = (64,))#candidate|11621|(64,)|var|uint16
output = func_11620(var_11621)
func_11622 = relay.Function([var_11621], output)
mutated_mod['func_11622'] = func_11622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6011_call = mutated_mod.get_global_var('func_6011')
call_11672 = relay.TupleGetItem(func_6009_call(), 0)
call_11673 = relay.TupleGetItem(func_6011_call(), 0)
var_11679 = relay.var("var_11679", dtype = "float64", shape = (5, 8, 8))#candidate|11679|(5, 8, 8)|var|float64
bop_11680 = relay.multiply(call_11672.astype('uint16'), var_11679.astype('uint16')) # shape=(5, 8, 8)
bop_11683 = relay.multiply(call_11673.astype('uint16'), var_11679.astype('uint16')) # shape=(5, 8, 8)
func_2453_call = mod.get_global_var('func_2453')
func_2455_call = mutated_mod.get_global_var('func_2455')
const_11687 = relay.const([-9.804210,-6.544189,6.716636,8.615711,-4.835334,9.273031,9.970667,5.426966,-6.459320,-4.052776,4.596802,-6.488451,-0.884734,-2.985377,-3.495860,7.834351,-2.541597,7.411365,5.317381,-5.385097,2.691295,-7.899347,-7.180466,6.070787,-6.297257,-2.445274,3.188913,8.100037,0.652660,-7.656239,4.055254,-0.123067,1.274269,3.607580,-4.168536,7.529251,-5.043183,-2.492811,8.587532,9.912207,-8.753211,5.300727,-7.184207,2.349334,2.895426], dtype = "float32")#candidate|11687|(45,)|const|float32
call_11686 = func_2453_call(relay.reshape(const_11687.astype('float32'), [15, 3, 1]))
call_11688 = func_2453_call(relay.reshape(const_11687.astype('float32'), [15, 3, 1]))
output = relay.Tuple([bop_11680,call_11686,const_11687,])
output2 = relay.Tuple([bop_11683,call_11688,const_11687,])
func_11701 = relay.Function([var_11679,], output)
mod['func_11701'] = func_11701
mod = relay.transform.InferType()(mod)
mutated_mod['func_11701'] = func_11701
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11702 = relay.var("var_11702", dtype = "float64", shape = (5, 8, 8))#candidate|11702|(5, 8, 8)|var|float64
func_11701_call = mutated_mod.get_global_var('func_11701')
call_11703 = func_11701_call(var_11702)
output = call_11703
func_11704 = relay.Function([var_11702], output)
mutated_mod['func_11704'] = func_11704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3543_call = mod.get_global_var('func_3543')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_11709 = relay.TupleGetItem(func_3543_call(), 0)
call_11710 = relay.TupleGetItem(func_3545_call(), 0)
func_8529_call = mod.get_global_var('func_8529')
func_8531_call = mutated_mod.get_global_var('func_8531')
call_11711 = relay.TupleGetItem(func_8529_call(), 0)
call_11712 = relay.TupleGetItem(func_8531_call(), 0)
output = relay.Tuple([call_11709,call_11711,])
output2 = relay.Tuple([call_11710,call_11712,])
func_11720 = relay.Function([], output)
mod['func_11720'] = func_11720
mod = relay.transform.InferType()(mod)
mutated_mod['func_11720'] = func_11720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11720_call = mutated_mod.get_global_var('func_11720')
call_11721 = func_11720_call()
output = call_11721
func_11722 = relay.Function([], output)
mutated_mod['func_11722'] = func_11722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4694_call = mod.get_global_var('func_4694')
func_4695_call = mutated_mod.get_global_var('func_4695')
call_11761 = relay.TupleGetItem(func_4694_call(), 0)
call_11762 = relay.TupleGetItem(func_4695_call(), 0)
func_8277_call = mod.get_global_var('func_8277')
func_8279_call = mutated_mod.get_global_var('func_8279')
call_11801 = relay.TupleGetItem(func_8277_call(), 0)
call_11802 = relay.TupleGetItem(func_8279_call(), 0)
func_1376_call = mod.get_global_var('func_1376')
func_1380_call = mutated_mod.get_global_var('func_1380')
const_11812 = relay.const([2.968453,-9.839737,-5.899659,-4.341574,6.643829,6.556111,-5.205630,9.314318,-1.316907,9.765039,-5.022304,7.122584,-5.977491,-4.980113,5.094124,-5.444009,6.905429,4.423832,-6.389922,-5.481674,-5.436529,7.954919,3.140060,-0.422813,-3.314925,-8.627288,-4.528885,7.343050,-0.503366,-2.052027,-1.598385,-8.705413,2.043809,0.024661,2.533731,8.734644,0.251496,8.237787,9.723512,-4.494248,3.149031,-4.453850,-5.116470,-2.533187,1.775440,1.225919,-7.730681,2.282394,4.847692,0.733674,6.261526,7.236518,4.671101,3.037574,-5.145811,5.329973,-8.516420,1.575792,1.390226,1.390084,-7.581894,-7.254178,4.179719,-9.889847,7.819466,1.172257,-3.756955,2.446552,1.587784,-0.390684,5.255931,8.891340,2.866162,-7.577900,1.722884,3.774266,-8.186965,-1.626083,-6.864878,7.991820,-4.567808,-2.032492,3.916678,5.272732,-3.510203,-9.075063,4.218523,-8.775169,9.803049,8.661906,-4.130150,-4.355707,-2.758039,-9.307092,-5.809255,-2.067637,1.421950,5.160517,6.818594,4.806147,2.847197,9.786386,-3.956123,2.160295,-3.016879,-3.524806,-3.710340,-7.810116,9.290963,1.019967,-6.158553,-0.718211,-1.537233,-7.623805,-1.614847,7.383549,0.202180,-3.424107,-1.621569,6.605551,-3.708503,-2.329617,6.631438,-9.046814,6.141179,-9.120559,5.246470,8.970962,-9.927717,8.242520,-0.583231,-8.774601,4.068229,5.183666,5.742447,7.885555,-1.609808,-7.032791,-2.192514,-3.053147,-4.070029,6.980564,5.539511,2.765098,-3.011579,5.090932,3.871269,-3.403862,-9.711480,6.477947,2.485806,-5.580753,-8.627708,9.047058,8.871634,-5.152337,-3.557233,8.124661,1.276441,4.254249,-8.618755,-8.529471,2.618000,-1.967099,-2.277893,4.344390,-0.417055,0.959779,-2.154159,6.751236,-7.770205,0.996990,5.418674,-2.453534,1.735633,-2.073356,-9.708082,1.635495,-8.369518,-5.340371,3.484274,-6.015570,1.331148,-4.502887,-9.863374,8.493081,-6.930170,7.757366,6.758378,-3.108527,9.373410,-5.179661,1.782729,8.298885,-8.638505,-6.524570,7.902709,2.212869,-3.859524,-7.643407,-0.755801,6.273934,-1.513255,-3.426307,-0.662346,-8.095287,-5.374773,-8.526897,0.972033,1.249519,4.490567,0.695275,-5.438938,4.305946,0.130840,0.018477,2.009821,-8.246136,0.989794,1.824622,0.619961,1.647230,9.888896,8.224352,-9.280670,-1.057869,-1.072105,-4.156013,-3.906852,6.394481,-5.328301,3.781030,9.394761,3.276310,0.158390,-5.850466,4.065157,-5.800639,5.121967,2.683078,-2.765775,2.903403,7.484006,3.629208,3.616394,0.332777,3.273971,2.233763,-5.304338,6.026058,-3.914236,-0.209324,0.797488,-0.093665,-4.455182,-4.988886,8.373110,2.214891,-8.755475,-6.441386,0.523824,8.293499,7.452260,2.850277,6.661424,4.420663,6.985954,1.568264,-2.511800,8.635340,1.881577,6.680476,-2.191224,-2.483712,5.160601,-2.789843,-8.380354,1.010515,9.670608,-7.141977], dtype = "float32")#candidate|11812|(280,)|const|float32
const_11813 = relay.const([2.064303,4.090366,2.614877,4.628576,5.615985,9.943177,4.670360,-4.310760,-6.872205,-2.623560,-0.695490,-8.741204,-6.528075,-5.075878,-5.642073,-7.352162,0.858839,2.363355,1.530094,0.410867,8.807712,-1.688990,-2.966457,4.937316,9.939084,-5.498912,0.138520,2.773124,0.490559,1.412361,-2.232088,5.672278,-2.461143,-0.127058,3.602739,-6.776490,-7.835820,-3.423532,7.924234,-4.377346,7.726735,-8.990945,1.272974,-5.337024,1.988161,4.304959,-5.719668,5.669275,9.311437,-4.287401,-9.156226,-4.225548,3.982391,7.505744,-5.451786,5.436880,-6.296418,1.328894,-6.944423,-0.048270,8.543873,3.944370,7.707373,-0.091703,7.240209,4.414040,2.862152,-3.804552,-1.256744,1.252352,4.500689,-9.201178,-2.829509,-4.258721,-3.611064,4.818161,-2.226847,1.633810,5.803089,-8.386320,-3.994527,-4.883165,3.948096,-1.362166,8.616216,8.836369,-9.189862,-3.320040,7.850670,9.654702,-1.512280,6.324111,-9.258076,-4.563405,4.096252,-5.011190,-1.479174,0.586177,2.018545,-3.196355,-5.936101,-5.422186,5.353779,4.290333,7.853863,-9.971771,1.442791,-0.824981,-8.197153,-6.334941,4.705502,8.382308,3.336633,-5.935541,-3.959818,3.508775,-6.868737,-6.853730,0.714486,-7.339451,-7.088411,-8.667243,-9.343906,2.719887,2.012104,-4.828964,-4.617857,-4.582717,4.778712,2.906894,3.123993,-9.012092,-1.264204,-1.712915,-0.237368,-7.625879,6.205543,6.011053,5.373178,7.262840,-7.511957,4.969965,1.597932,-8.545086,-8.075775,8.378496,5.484257,6.017447,-7.200267,3.405360,-5.312639,4.012554,-8.054090,-5.249830,-1.028452,-5.265702,3.204019,1.328035,8.864156,0.312052,7.825577,-4.277038,-9.052976,-4.683094,0.486531,-9.417971,1.405008,0.180221,-5.540872,6.400945,5.042459,3.122609,-8.061249,-8.779099,-2.284799,8.799972,-9.285656,-0.114072,-7.325468,0.463090,-5.720430,7.243448,6.603699,3.609409,-5.299632,-4.037588,-6.530498,6.023262,1.084916,6.092470,4.142677,6.071796,-1.855531,9.335076,6.549047,-1.404867,-0.751161,1.931299,-2.140581,2.275185,-2.663436,4.255965,9.179467,2.483214,-1.562003,-4.364761,0.933396,4.887087,-4.615504,-8.429456,5.909326,1.114452,2.026736,2.222819,-8.994284,-7.558440,6.612016,7.167636,-0.578374,0.411237,9.764230,7.901133,1.713097,-2.888240,8.479795,5.114900,6.656172,-3.561100,-8.344721,2.060748,-3.241664,1.314515,8.470305,-6.087432,5.999721,-6.849092,5.899199,9.240372,-6.759252,-0.424827,4.347148,-1.193987,6.799289,9.782006,-0.697861,-7.381345,-9.653578,-8.175713,-4.196420,-0.113209,-7.368808,1.479474,-6.874214,2.437809,-3.256576,-9.786282,6.782330,3.184628,9.041283,-4.727993,5.678361,-0.005979,-0.058321,1.834823,2.552770,-6.884216,-9.118012,9.281667,8.727842,4.184561,5.879322,2.334873,-2.447555,6.057820,5.094302,8.269609,-8.388679,-0.073635,8.307971,2.496212,3.827824,-7.457414,7.996757,-2.179949,-6.465712,6.966136,4.366272,3.843314,8.081197,1.723253,-9.169326,1.804144,-8.840948,-9.688165,8.311533,-8.551323,4.300726,-9.019637,3.698449,3.546586,-4.992946,9.473607,9.262492,7.923301,9.321448,2.334795,5.232803,-5.534530,5.112171,1.793181,-9.641966,6.438757,9.796376,6.662217,1.352668,-5.554784,2.629555,8.256935,-8.635873,1.800196,-2.022814,-7.736724,5.683409,7.460204,5.171626,8.660612,0.794732,1.895080,-9.537656,8.776891,-5.757295,8.725328,2.046044,-7.766841,7.559197,5.582695,5.937537,1.440223,-9.126803,9.032339,-1.272901,7.476638,2.588439,-5.932656,4.377055,1.070588,8.294104,9.964210,-4.033454,0.432801,2.028554,8.347108,-9.399277,8.462858,7.884073,-0.565875,1.488260,5.380593,-1.373299,-2.820833,5.158743,1.623280,-7.921975,2.074743,0.090840,-3.294897,3.733067,3.236364,4.506653,-3.123614,9.061122,-3.806490,7.211181,8.520545,3.750749,5.830311,-2.643497,7.358289,-6.887417,9.677824,8.130182,-6.277664,5.832747,-7.731524,2.439433,8.680209,7.072527,3.330438,-5.533973,6.528911,4.042017,-6.249842,3.638271,-2.152456,2.447502,0.642099,-6.931745,2.054402,6.754245,-6.101094,4.483272,8.288921,1.288992,3.354435,-7.439223,6.127269,1.524979,3.988360,0.190289,-0.986964,7.748741,-1.876099,-1.953078,2.005463,8.720969,-0.593144,2.479535,-5.674046,-4.973791,-1.789834,-5.906870,-0.966384,-5.152978,-3.262246,-5.601111,-3.462947,6.316280,0.832977,-5.768674,3.043064,-8.981673,-4.373674,-1.890377,-9.854810,-5.867749,2.057003,-0.507986,3.576636,2.548162,-9.697825,-9.490930,1.486225,6.913547,4.817539,9.385929,-9.734045,-1.541921,5.923312,7.982879,-5.467567,6.249563,-6.548759,3.889460,-4.711952,0.740668,-4.153234,3.409979,8.800648,-1.135300,-2.158742,-0.075776,3.988047,-5.058108,2.727669,-9.024991,6.919286,4.527045,8.441951,1.517984,9.520870,4.323823,2.499962,3.470359,8.199975,0.417452,7.005500,-3.370111,5.485543,8.654347,-3.669577,-9.971789,2.932262,5.404294,-7.378210,-3.578871,-7.686088,-2.232267,-0.786034,-9.667739,0.319345,-9.942092,8.137949,-3.094236,7.694997,6.430525,0.593359,0.256381,8.949111,-7.376865,-5.044316,3.282613,-7.621875,-9.127671,7.934087,-8.804650,-9.616529,2.087913,-2.433002,-3.684872,-9.114886,7.362071,6.090928,-8.045858,-2.462364,3.395358,-0.883144,7.028366,-4.955407,6.987262,-6.949941,-1.186439,-6.630732,6.185741,3.694568,-3.026186,1.238723,-3.742678,3.818600,-2.614968,6.916719,-2.997330,-0.941891,-5.794067,2.068632,2.694271,7.777118,-4.262533,8.628485,-7.720051,-4.450776,-7.156292,4.021175,-3.376042,-9.942666,-3.588732,-7.638105,0.799419,-4.246230,1.718621,9.865845,5.053585,5.665747,5.564988,5.623393,5.787788,-3.623309,-1.647560,-1.614613,-8.938499,0.681289,-1.089494,0.883745,-0.208434,8.123678,9.364912,-3.679149,-9.224008,6.926204,7.207539,9.961449,-6.234394,-4.522818,9.084052,9.313344,3.605026,-5.580698,4.255145,3.666352,5.239908,6.023639,-8.508973,-2.964839,3.362998,-4.321581,-0.977132,-3.879271,8.757455,4.635174,4.288005,6.903305,8.017004,7.422980,8.077001,4.768512,6.576470,-7.349823,-5.253270,-4.571484,-0.998072,-7.058182,8.500503,0.707254,-8.329252,1.214807,6.236182,-4.871876,9.641287,7.906245,1.972123,0.621150,-3.998307,-4.250906,-2.227123,-6.152901,5.811616,-0.476227,0.886834,5.484632,-1.539608,-4.740236,4.192474,4.451699,-3.318105,-8.888530,3.339615,-8.566729,4.569553,-9.338757,-0.101948,-0.856996,-3.910947,-1.040857,-5.139515,7.837402,-0.893996,-6.199973,-1.082011,-4.059078,3.163381,-1.756758,2.734801,-6.240388,3.372123,-7.741679,7.746238,9.874118,3.723752,-9.624008,-4.401913,3.633140,4.124390,-2.958211,4.144323,-5.941098,3.705581,3.758331,1.302741,0.987963,-4.808320,-4.243562], dtype = "float64")#candidate|11813|(660,)|const|float64
var_11814 = relay.var("var_11814", dtype = "int8", shape = (1056,))#candidate|11814|(1056,)|var|int8
call_11811 = relay.TupleGetItem(func_1376_call(relay.reshape(const_11812.astype('float32'), [7, 10, 4]), relay.reshape(const_11813.astype('float64'), [660,]), relay.reshape(var_11814.astype('int8'), [1056,]), ), 0)
call_11815 = relay.TupleGetItem(func_1380_call(relay.reshape(const_11812.astype('float32'), [7, 10, 4]), relay.reshape(const_11813.astype('float64'), [660,]), relay.reshape(var_11814.astype('int8'), [1056,]), ), 0)
bop_11830 = relay.bitwise_and(const_11812.astype('uint8'), call_11801.astype('uint8')) # shape=(5, 8, 280)
bop_11833 = relay.bitwise_and(const_11812.astype('uint8'), call_11802.astype('uint8')) # shape=(5, 8, 280)
func_6589_call = mod.get_global_var('func_6589')
func_6591_call = mutated_mod.get_global_var('func_6591')
call_11842 = relay.TupleGetItem(func_6589_call(relay.reshape(const_11813.astype('float64'), [660, 1])), 3)
call_11843 = relay.TupleGetItem(func_6591_call(relay.reshape(const_11813.astype('float64'), [660, 1])), 3)
const_11847 = relay.const([[[4,-3,1,-10,-7,-2,-3,-2,-10,10,8,-1,-2,8,2,-9,-5,-3,10,-3,2,-4,6,5,-8,-5,-4,-9,-9,-6,6,-9,-6,9,-8,5,-8,8,-4,9,-7,-10,-1,7,9,-10,9,-6,-4,2,-5,-1,-5,-6,1,3,-10,-8,6,-10,1,8,1,-6,6,6,-7,6,-7,1,10,3,8,10,9,9,-1,-9,-10,9,4,-9,4,3,10,7,-9,-7,-4,-1,8,-10,-6,3,-5,-3,-8,8,-8,3,-4,-7,5,-1,2,1,-1,-8,1,4,4,6,10,5,-4,5,3,2,7,-6,-5,-6,9,7,5,-9,-9,-10,9,-6,-8,-3,-2,-8,10,7,-10,-4,-4,2,-2,-8,-3,7,-6,5,3,-4,4,-5,5,-10,2,-7,-6,-8,7,7,-6,2,-9,-7,-6,9,-2,-6,6,-1,1,7,-6,-6,-4,-5,-9,-2,5,-1,10,-4,-4,-9,-6,9,10,-5,-4,9,5,-8,-10,-3,2,9,5,6,2,10,-8,5,6,4,10,9,7,10,-8,4,10,-3,5,-6,5,-4,6,10,-9,3,-6,-7,-10,10,-3,-7,8,-7,9,9,-1,6,-2,1,-9,-3,9,-7,8,-4,-4,1,2,4,-5,-5,3,4,-6,-7,9,1,9,-6,7,-7,2,-2,7,-6,-6,9,-2,7,7,-2,-5,4,-3,2,-2,-3,-6,-9,-1,-7,5,10,-8,5,2,-4],[2,-2,10,-7,2,5,4,-3,10,-4,6,4,1,-9,-9,-2,3,-8,-8,3,2,8,-5,-3,-8,10,2,-8,-3,8,2,-3,-3,-7,-5,-1,-10,4,-7,-8,7,9,-4,-4,7,-9,3,-3,-4,-9,1,-5,-6,-6,-10,-8,-6,6,-5,7,6,1,1,-8,-6,-3,7,-8,10,6,10,-7,-10,-6,-7,6,-2,-3,-3,-9,9,4,3,9,-7,3,8,6,7,4,7,-5,7,4,-2,6,5,7,5,-1,-2,10,8,-7,-7,7,1,5,-2,9,-9,5,-7,4,-8,-4,1,10,1,-2,-10,-4,-1,-10,-7,-6,6,-2,4,6,-1,2,-6,9,2,8,10,-3,-1,5,4,6,-5,-4,2,-10,-8,-3,5,-2,5,8,-1,8,4,2,7,9,-4,-8,2,-9,10,-5,-6,-3,6,-6,-10,1,-8,-3,8,-6,6,-9,1,9,4,8,2,10,-3,-6,-3,-9,9,7,-6,10,-8,-10,-8,2,-2,1,4,-3,10,-9,8,5,2,5,-6,9,3,-4,-8,-5,9,-4,7,-9,7,-1,6,2,-1,-5,1,2,-3,9,3,2,7,-4,-3,5,-10,7,-4,3,8,-4,-2,-5,3,6,7,7,-4,-10,3,-9,2,9,6,3,8,3,4,-6,-3,2,-2,5,9,3,1,-2,-7,-10,3,-7,3,-2,9,3,-2,-1,5,10,-1,5,-6,-6,-10,-6],[-4,-3,-2,-1,4,-2,-10,-3,-8,8,-8,3,9,-7,-10,1,7,-8,-2,-9,-4,5,3,-8,10,2,6,-4,-7,-6,-5,10,3,-10,-6,1,9,3,-5,4,-4,5,-4,-8,9,7,-1,5,-4,10,3,9,9,-5,2,2,-8,9,-8,-2,-1,1,7,-7,-3,10,-10,10,-2,6,6,1,6,5,-4,-1,7,8,-9,6,4,10,6,7,-4,-1,2,-4,9,2,-6,10,-6,9,5,-9,-1,5,8,-3,-5,-3,-6,5,6,-1,-10,-8,-9,-4,-10,3,2,9,8,-2,-6,-9,-6,8,-10,4,9,-8,9,-3,3,-2,-2,4,-3,-4,-5,-1,-5,-3,-5,-7,-1,3,5,10,-1,-4,3,4,6,7,9,10,-5,1,10,-6,-2,-10,4,6,4,10,-8,5,10,-3,10,-5,8,6,-5,-10,3,4,2,5,-10,5,-7,1,-4,10,-2,8,-2,-10,9,4,10,9,9,-7,-9,8,5,-7,6,3,-2,-9,-7,1,-9,-8,-2,10,-3,10,-1,9,-8,5,4,5,8,10,3,1,-6,-8,6,-8,6,2,-6,5,9,-1,9,9,-10,-5,10,-2,5,-3,-9,-3,-10,-4,7,-2,1,-7,9,-2,-5,-9,-2,-1,2,-9,6,-10,6,3,-5,-8,-8,1,-3,4,9,-2,6,-8,-1,3,-9,-4,-9,8,3,2,-5,9,-5,5,-8,-5,-2,5],[9,1,-3,5,-5,7,3,7,2,5,9,-3,6,-3,8,2,-8,-7,1,2,-9,1,-8,-9,6,-2,-1,-4,-1,-7,-5,-8,3,5,-1,7,-7,9,1,-10,1,2,4,-1,2,-8,5,1,3,-2,-4,2,9,9,-1,-7,-8,4,-4,1,-3,5,4,7,-2,2,10,-7,9,-1,4,3,-6,6,-4,-7,3,-4,-10,4,2,9,-2,-2,-4,-1,10,8,3,-9,-10,-3,-10,10,9,-1,-2,2,-9,-6,7,9,1,7,-3,10,-3,-6,9,-3,2,9,6,-9,-8,-6,-2,4,6,9,6,-5,-2,1,9,-10,-10,4,-2,9,-7,5,-3,5,10,9,5,6,6,-9,-1,-3,-9,5,1,-3,10,-8,-7,-2,-8,5,-6,-1,8,5,-10,-10,-9,-2,2,9,-3,7,-1,-9,10,4,-2,-8,4,2,4,-7,-9,-1,4,5,8,-9,10,2,9,8,1,-4,9,-3,7,4,-8,-9,7,-2,-5,-8,9,5,-5,1,-6,3,10,8,5,-3,9,5,-7,4,10,-7,1,-8,4,2,-4,-7,4,-2,-9,2,-9,7,6,10,-3,-6,10,1,-3,7,-2,4,2,-5,-2,-1,5,-1,-9,-8,7,-7,8,-10,-2,10,3,-8,-1,6,-9,6,-4,5,-7,6,-7,-10,10,9,7,4,5,-5,-6,-10,9,-8,-3,6,8,-4,4,3,4,-6,1,-2],[-3,-1,-7,3,-8,-1,-6,3,-1,-10,-10,9,-4,6,-4,-10,-3,-5,5,-10,-10,6,-8,-3,-7,-3,5,1,-8,3,-3,-8,-5,1,-4,-2,2,2,8,-6,-8,2,-3,-3,9,-3,-2,-1,6,6,4,6,-8,3,-4,1,-10,-9,3,3,9,-6,-7,-7,-10,-4,-5,-10,9,-8,-4,8,9,8,9,-6,5,1,-9,-6,-3,5,1,10,-9,-4,9,-9,-9,-2,8,7,2,-5,6,3,-6,-9,2,-8,10,-5,3,-7,3,-1,1,-4,5,7,-5,-3,7,-7,-3,-1,6,-2,-2,-1,10,7,9,-6,1,8,-2,-6,-4,9,5,-10,5,-9,-3,-3,-2,6,-2,-6,8,10,4,10,-8,-5,8,-3,9,2,-4,-5,-5,-8,3,-1,-9,-10,6,2,8,6,-5,9,-3,-4,-5,-3,-9,-7,-6,-5,9,7,7,7,7,3,2,-5,-2,2,-9,-8,-10,5,3,-1,7,-6,-9,4,-6,-9,-9,-3,-5,-8,4,7,9,9,3,-4,10,-9,-5,-5,9,9,-8,9,-9,-10,-1,4,10,-3,3,-3,9,2,-4,5,2,-1,6,6,7,8,-4,1,6,-6,3,-2,1,6,-2,1,5,-4,4,-8,-7,-10,-1,-4,-4,7,-10,-10,4,8,-9,10,1,-8,-4,-5,-5,4,7,-4,-8,10,10,3,-10,-10,10,-4,5,-5,10,-2,8,-2,3,7],[5,-3,7,-10,5,-5,-1,-7,3,-5,-3,-10,4,5,6,-1,9,-7,-8,-5,-7,9,3,4,9,1,-10,-2,-10,2,-10,8,-4,6,-2,-8,-3,-8,-4,-2,-6,6,3,8,6,-1,2,-6,8,2,-4,10,-7,6,3,-4,-3,4,-10,-1,-4,-3,-4,7,-4,2,7,-7,-2,-8,3,3,4,-1,-2,1,5,-4,-4,2,8,-5,-8,1,-7,5,3,-5,-5,-9,9,5,-5,-6,10,4,2,4,4,-9,6,-1,2,-6,-4,-6,-7,10,9,-1,-4,8,-6,7,10,3,10,9,-1,6,1,2,-2,10,-8,10,-7,7,1,-5,10,10,-1,-9,-3,-10,9,-2,4,-2,-4,2,1,7,3,-4,8,-2,-1,3,-6,-8,-5,-5,4,-9,10,-2,-1,2,8,9,-9,7,10,4,3,2,-4,-4,4,9,-7,4,1,-3,1,-7,3,-10,5,10,8,5,8,-2,-5,8,-3,9,10,3,4,-4,5,1,-10,8,-2,1,4,-6,-6,8,-7,-3,9,-10,9,9,8,6,10,9,8,-5,3,9,4,-1,4,-9,4,-5,3,-7,-3,-2,-8,6,9,8,1,-5,5,-9,2,2,-9,-8,-1,5,9,-9,-6,-3,-4,-1,10,-3,2,6,10,-9,-4,-3,-2,-1,6,8,-4,-9,3,5,-5,-8,2,10,-1,3,4,2,-2,6,2,-10,-4,7,8,-1],[-2,-10,3,6,-7,-1,3,-6,6,-5,-6,5,5,-7,5,5,-7,2,3,7,-7,10,10,6,-9,-4,-7,5,2,4,10,-5,-2,-10,-4,-4,3,-2,-1,-1,-1,-7,6,10,-6,7,2,4,10,-9,-2,7,9,10,-8,-4,8,7,3,-5,-10,4,6,-7,5,3,1,3,-9,-1,6,8,-5,9,2,9,-6,-5,-3,9,10,-5,1,-10,1,-1,-7,2,-4,1,4,-8,-5,3,5,5,-3,6,-8,-6,8,-7,-6,8,-9,4,9,6,-4,1,10,-5,-6,-6,-9,-3,-10,3,-1,-4,10,-6,9,-4,-10,2,-2,-10,10,-3,8,8,-10,4,2,4,7,2,1,-10,-2,2,3,-2,-9,4,3,-7,-10,4,10,-3,-7,4,-2,10,9,8,5,-5,-7,2,-8,2,-2,2,-6,9,-4,1,5,10,5,-6,-7,5,-9,-3,7,-8,6,9,7,-3,-10,6,10,-1,-5,-7,7,6,10,4,-9,-6,-2,-4,4,-1,6,10,-3,-2,8,-1,-3,3,-10,-3,-9,3,6,10,7,-6,9,10,7,-10,-3,-9,2,2,-9,1,5,-9,3,3,-1,4,5,1,6,-6,-6,7,-9,10,-5,-5,-6,3,4,-9,5,4,-7,-1,-8,-4,-5,10,2,-3,-2,-1,-5,-10,-10,-5,-2,6,-3,4,7,-6,1,-8,8,3,-10,-2,9,-5,9,-6,8,-2],[-1,4,4,-10,-8,9,-10,9,7,6,-1,2,2,3,-2,-4,-3,10,-10,4,1,-5,-6,-2,4,-6,10,7,10,5,-8,2,7,1,-6,-5,-8,7,-5,-8,8,5,6,1,5,5,-5,5,2,-1,-8,-5,-9,4,-3,4,-8,9,-5,9,6,-1,2,-3,1,3,2,-8,2,6,6,-7,1,8,4,-5,-3,1,4,10,-10,5,-2,-5,-6,-2,-3,7,-2,-1,6,9,2,-5,-6,2,-9,-9,1,-7,-9,9,5,5,5,-6,-1,10,-6,4,9,9,-2,-1,4,-1,-5,4,-8,-9,-6,6,1,5,-1,9,-4,10,-7,-10,-8,-6,1,3,1,-6,7,6,-10,-5,-9,-2,1,8,4,-2,9,5,8,-1,8,-5,1,-2,2,1,2,-4,-9,2,2,-6,-2,1,9,-8,-1,-3,-6,-3,-4,2,10,-10,10,-2,6,3,3,7,-8,-10,-9,3,-9,8,1,-1,7,1,3,-10,-5,6,-7,-7,-7,-5,-1,-4,5,6,-3,10,-8,7,-4,10,-10,-5,-7,-3,3,-3,-8,-5,-2,-2,9,2,1,-9,-6,4,5,-4,-4,-9,9,-1,2,10,8,6,4,-5,9,9,4,3,3,-2,-6,-5,-4,2,4,-9,-5,-10,-4,1,-10,1,4,-1,-1,5,5,-4,8,-6,-9,-3,-3,1,-7,-3,3,-10,7,-3,6,10,7,4,-10,-6,-7,-3]],[[-3,10,-7,8,8,-6,-9,5,-6,-1,-9,-8,5,-7,-4,-3,-5,8,7,-1,-4,-9,-7,-10,-7,5,4,-6,7,1,4,-8,-10,-10,-10,1,-9,9,-3,10,-10,8,8,4,7,-9,-1,1,-1,8,1,9,10,-9,-5,-4,4,10,8,-9,9,-8,-5,4,10,-9,-1,-5,6,-3,1,-7,-1,-8,1,4,5,10,2,6,-6,-5,5,10,-1,2,10,8,-6,-8,4,-7,-5,9,-3,-9,1,-9,-3,-6,10,10,-9,1,7,-4,-3,-1,10,-8,-4,5,1,10,1,-10,-7,-10,9,4,3,6,-1,-6,7,-7,1,6,3,7,5,-4,-6,-1,-8,-10,2,-6,-4,-5,6,-4,1,-10,8,-10,-5,-7,3,-5,-2,-3,-2,9,-1,7,-6,6,-2,4,4,-5,2,-9,10,5,10,6,7,9,2,7,8,-5,-10,10,-5,-2,-7,-2,-6,8,-5,9,2,1,-4,1,-2,2,-7,7,-7,9,-3,-2,-7,4,-7,-5,-10,4,-5,-6,1,-10,-10,10,-9,5,9,-8,10,-10,6,7,-2,-10,5,-3,-3,3,-9,5,4,-9,-7,-1,2,3,9,-1,-10,5,6,2,-10,-5,9,-8,-9,-6,-5,-5,-2,-4,-8,-1,8,4,3,-3,2,-3,-9,-4,7,9,10,-10,2,-1,-1,-1,-8,2,2,6,7,-4,10,7,1,1,7,4,-9,2,-9,8],[-7,-1,-10,-2,6,-1,6,-4,-1,-8,10,2,7,9,4,-3,10,1,-3,-4,10,3,-3,-5,-4,7,-5,3,-2,9,-10,8,-8,-9,-1,-8,-10,7,10,2,-2,-9,-7,-10,5,-4,4,6,-10,-3,-7,9,5,-1,-5,2,1,8,-6,-8,10,5,-3,-7,5,1,4,9,8,-6,-4,-2,-10,4,1,-6,-3,4,-3,8,-3,-9,-1,-6,-10,-1,9,-1,4,-6,7,-5,-4,-6,-1,4,-3,9,-3,10,5,10,-5,-6,6,5,3,-4,10,-3,-4,5,2,-1,8,8,5,9,7,-10,-5,-6,6,5,-10,8,-5,-3,-4,-2,6,-6,-8,-10,2,7,6,8,-5,-9,-1,-1,8,5,-8,4,7,-6,7,-9,7,-8,3,-4,-7,3,10,6,10,9,8,-6,5,9,10,-3,-6,-10,5,7,-9,-1,8,6,-1,-8,10,4,-5,-9,1,-2,5,7,-7,5,7,-4,5,3,-7,-5,-4,-2,1,6,7,2,3,3,4,-6,4,-7,2,-5,10,5,8,-7,-1,3,-2,-10,-6,4,1,-2,4,3,9,6,-7,-5,8,-6,-4,9,-5,2,-3,3,8,6,5,7,-7,-3,-4,9,-10,-1,5,-4,-10,-4,-3,-5,-2,-3,2,1,3,-6,-4,-8,-2,-1,-2,1,-1,3,2,7,2,-1,1,6,5,2,-6,4,-3,9,1,-5,5,-10,-7,10],[-8,6,10,7,3,-5,-4,-9,5,2,7,10,-7,-6,-9,8,7,9,3,3,7,-4,-6,-8,2,8,-9,-1,9,5,-6,-5,4,-8,-10,-4,8,10,3,-6,-9,-6,3,7,5,-1,-6,1,10,8,2,-1,-1,6,-8,-1,-9,7,2,-7,7,-7,-4,-2,10,8,-1,-2,-9,-8,-3,6,-6,7,9,7,1,7,-4,4,1,4,3,6,-4,-1,-3,-10,-1,9,10,4,-1,7,-1,9,-4,-6,1,-9,4,4,8,-8,-1,-7,-2,2,-3,1,1,8,5,4,-3,10,4,7,-10,-9,10,1,6,-7,6,2,10,-5,-3,-8,2,4,-4,6,-5,-4,-2,9,2,-6,4,6,-10,-8,9,-9,-5,-7,-3,-2,9,-3,3,-6,8,1,-1,-7,-7,-4,-10,-7,8,-6,8,-9,-4,-5,-6,1,-6,7,9,-10,6,3,7,-3,-6,5,-6,9,1,-8,7,-1,2,-10,-10,7,4,-4,-2,7,-7,-9,1,5,-4,-6,-2,3,5,-5,6,10,4,5,4,-1,6,-6,-8,8,-5,2,-3,3,2,2,-2,10,-10,-1,8,-5,-3,-3,3,-4,8,-10,-3,-1,-3,-5,-9,10,-1,-4,-4,-5,-2,-8,2,5,-8,-4,-8,-7,10,-5,-8,-8,7,-10,-9,-5,-5,-5,-5,-6,-7,-5,5,-5,6,4,4,-5,-4,-9,-9,-5,9,1,2,8,-10,-4],[5,-2,9,4,-7,-4,3,-3,2,-9,10,7,-9,-1,8,-6,5,5,-3,7,6,-3,5,-3,6,7,2,-5,-1,-2,2,-3,3,10,4,7,7,1,6,10,-6,7,3,10,8,2,-9,8,-2,7,-6,-8,-4,6,4,3,4,-1,10,10,5,-2,4,6,8,2,8,8,2,4,-1,8,-5,-2,-2,6,4,-2,6,4,1,-8,7,-3,-2,-5,-3,8,-5,4,-5,-7,-6,7,6,8,9,-10,-3,-7,9,-8,8,10,-8,-1,5,-2,-6,7,-2,1,2,-10,-4,2,3,-6,7,4,-2,-10,2,2,-3,-2,-3,-6,4,-1,-7,4,4,10,-7,9,-9,10,1,9,-8,-8,-4,7,-2,-10,1,8,-5,-7,3,4,4,-5,-6,8,-5,-9,3,-9,-4,4,3,3,2,-2,5,-1,2,4,10,5,10,-6,-10,8,6,-9,5,8,-1,6,-8,5,-1,-9,-2,-6,-8,5,-9,-2,-6,5,3,1,-4,10,-2,-2,-3,-5,5,7,-6,-3,-5,2,-6,-3,10,2,10,8,6,-8,10,6,-7,-3,7,-9,-1,-6,-8,5,-4,4,1,-10,1,-6,1,8,-6,2,7,8,4,4,-2,2,7,1,-7,3,-7,10,-4,8,9,3,-3,3,-4,1,-5,-3,-10,-10,-3,6,-5,-10,5,9,7,-10,-5,-8,-8,-7,4,7,2,1,-2,5,-3,4],[-2,10,5,10,2,8,-8,5,5,-6,-1,2,5,-9,-4,-6,6,-6,5,2,3,-9,5,5,-8,-6,-9,10,-8,4,-4,8,6,2,9,1,3,5,4,7,10,-10,-2,6,-9,-9,1,-2,1,-10,-7,-4,-1,-8,10,8,9,-2,-6,8,-9,10,-6,6,-8,2,7,6,7,-2,7,7,-8,6,7,1,3,-5,8,8,8,-1,-8,-5,-9,9,9,-4,7,10,6,-8,-7,-9,6,10,9,-1,8,-9,-4,-7,-8,-7,2,7,-1,6,1,2,5,3,5,9,1,4,-10,-8,1,1,7,3,6,7,-7,5,2,3,2,-3,-4,10,-6,-2,6,-4,3,10,-7,9,5,-3,9,-4,-2,6,2,9,4,8,-7,2,10,-1,8,-10,-3,-10,2,5,-9,-9,-7,-10,2,-1,-10,10,5,-6,1,-6,8,-7,9,4,5,10,4,2,-8,6,8,-8,9,-5,-8,7,6,8,-7,5,8,3,5,-1,-2,1,-4,2,2,6,-10,-8,8,-4,-10,9,4,3,9,10,-10,-1,9,8,1,-3,-6,7,-9,-8,-10,1,1,3,6,1,-6,10,8,-9,1,-9,-3,10,-9,-4,-7,5,7,-8,-1,8,-3,-5,6,9,-5,4,-7,1,5,7,10,-8,9,-1,4,10,-10,8,8,-5,8,-3,4,-2,-3,8,2,2,3,6,5,-7,-10,2,4,4],[-7,-6,-5,9,-1,1,5,9,-7,5,10,8,7,-9,-7,3,-2,-4,-1,-4,10,-6,-7,4,7,-7,-1,8,-4,1,9,-3,4,9,10,8,7,4,-8,-9,8,-3,-10,1,7,5,-7,-9,8,8,9,8,9,-1,10,1,7,-1,4,-1,7,7,4,6,-3,-10,8,10,9,4,3,-1,1,7,5,4,-6,5,8,4,6,6,1,3,1,-3,-5,7,8,9,4,5,-8,-1,-4,8,8,-5,-3,-1,6,-9,8,-6,1,-10,-1,-6,9,-5,-2,-2,10,1,6,8,-8,2,4,-2,3,4,1,5,9,3,-5,-2,-4,8,7,-1,-2,10,-9,3,-6,-8,-8,7,4,-7,-6,-6,3,10,2,4,-4,-2,-9,-7,-1,-4,-9,-6,-2,4,3,-10,-3,-8,-2,1,-7,1,7,10,6,-8,-6,7,-9,-8,10,1,-8,10,-1,10,-3,3,10,1,1,10,-4,-5,-10,5,1,-7,5,1,-10,4,-3,-5,-4,8,6,1,8,4,9,10,-5,8,-6,-6,1,10,-8,-8,9,-8,-5,6,-4,-3,-10,-4,-2,5,-3,-2,10,10,-7,10,4,3,-6,-7,1,-5,5,-4,-2,-4,-9,-1,10,-4,-10,5,2,-5,8,1,2,-10,5,-5,-2,-4,-7,7,6,6,-8,10,-10,-8,-9,-10,3,7,4,7,-10,7,5,7,-9,-7,-6,5,-6,-8],[10,-5,6,4,-5,-7,3,-4,-10,-10,-8,4,-8,1,3,-8,-7,-7,8,-4,4,9,5,-6,6,2,4,9,-6,-7,-10,-4,-9,-2,4,-9,-7,-6,4,5,-7,-4,-4,5,3,-1,-9,2,7,5,9,-10,4,7,5,8,3,-6,-6,9,5,4,6,-1,9,-2,2,5,5,4,7,5,5,-7,2,-10,-5,-2,2,3,9,-10,-7,-7,-8,-4,2,-5,1,-5,5,4,4,2,-7,-7,-10,7,3,-10,4,8,-5,10,2,-1,-3,-8,8,2,6,-4,-6,4,5,-2,7,-3,-2,10,-10,-10,5,1,1,1,-3,-4,5,10,-1,9,2,-2,-6,-8,-3,-3,-10,2,-8,-9,-5,1,10,-10,-6,8,-10,2,-3,6,1,-4,4,2,-6,-4,-3,-1,-8,1,7,-4,2,-6,-8,-10,-2,2,10,-5,-5,7,5,1,8,-7,-3,-3,9,-1,4,8,6,9,3,2,4,-8,-7,2,4,10,2,-4,7,-10,7,-6,-7,8,-10,10,2,-2,-8,4,-6,9,2,-1,-9,9,-8,-10,9,-6,10,10,3,-1,-8,3,3,-4,-7,5,5,-3,-8,-9,-1,-5,-9,5,9,-3,2,1,-9,-2,9,4,3,6,-10,-10,7,4,-10,-8,-4,8,-8,-3,3,7,5,3,-1,-9,3,4,5,-6,6,6,8,7,-2,-4,8,-4,-5,2,5,6,1,9],[-7,-2,10,2,1,-3,10,7,-1,2,7,1,-5,1,-9,5,5,9,-5,-3,-10,9,-6,-7,-7,-2,-5,6,1,8,-8,-6,-10,10,5,2,-10,5,-7,-2,3,9,-10,-10,6,1,-10,-9,-1,6,2,1,-10,9,-1,4,-6,4,1,7,1,-1,6,-3,-7,-4,8,-3,4,-6,3,-10,4,-5,7,10,3,-1,1,7,-3,-9,8,7,-3,4,-4,5,8,3,-3,3,4,6,-8,-3,3,1,-3,-3,3,2,-2,5,6,-5,-1,-6,2,10,4,2,7,-1,2,-9,-1,-4,8,5,9,5,-8,-7,-5,-2,-4,10,-8,4,-5,8,-1,-1,4,-5,5,7,2,-6,4,-6,2,10,7,1,4,-9,2,6,-7,-10,-10,4,2,-9,-7,5,-2,-1,-8,2,10,8,3,-7,-6,1,-6,10,-6,-6,-5,-4,5,-4,8,4,-9,-9,8,-3,4,10,2,10,8,-2,-7,8,4,7,-9,-9,3,3,5,-6,1,-1,-6,2,6,-7,-4,9,8,-1,6,9,9,3,-7,3,6,2,2,8,-10,5,1,-4,-9,-9,-5,4,-8,8,-5,5,2,3,-5,-5,5,1,-5,6,7,7,-4,8,8,-9,-6,4,4,-5,8,4,-2,-3,9,9,5,-10,6,10,5,-7,-6,10,-8,-8,4,4,-8,-3,8,-5,-7,-1,4,-9,1,-9,-6,-6,3,-5]],[[-10,5,7,7,9,8,8,10,-1,10,-4,-10,7,7,3,-8,-10,-3,10,-2,-3,-6,-8,-10,3,2,10,-8,-9,8,6,5,1,-2,-7,2,5,-10,2,3,-1,-5,-8,-9,-9,-8,-4,-10,10,-8,8,-8,7,5,9,7,4,2,-6,-8,-7,9,-9,10,2,-10,-9,-3,-8,6,-8,-7,4,4,-10,4,-1,1,-1,-1,9,3,-2,4,5,-7,-2,7,4,7,-4,-3,3,4,5,7,9,-3,6,-10,9,6,-4,9,-2,3,-7,-2,-8,-8,-4,-8,7,-5,-1,4,4,1,-10,-5,-7,2,-5,-8,-3,-8,1,3,7,1,-2,-8,-4,4,9,10,-10,-4,7,9,-8,8,-3,7,6,8,2,6,-4,2,4,3,-4,-8,-9,-8,4,-6,6,6,3,2,1,3,-10,3,7,-7,-3,10,4,8,-6,4,8,-4,6,-6,5,4,-4,-1,-3,2,5,-5,-3,-4,7,-3,-8,8,4,-2,-5,4,3,2,6,-9,7,-10,9,1,2,3,-10,5,-8,3,-3,-3,-4,4,9,1,-9,8,4,6,-3,7,1,-7,1,2,-7,-2,-2,-1,10,-8,-10,9,-8,-2,-3,4,3,2,-1,9,1,-9,10,5,1,-10,-2,6,1,10,-9,7,6,-7,6,-5,7,-2,-7,8,-2,10,7,-3,8,-4,8,8,-3,-2,-10,7,-2,-6,-6,6,3,2],[-6,2,-10,8,8,-3,2,9,2,-9,5,-5,2,-8,1,-6,-5,-8,5,-5,5,-3,3,7,7,2,-3,-2,-10,1,8,-8,-6,-10,-4,3,2,4,-7,3,-1,6,1,9,8,-5,-7,-3,-9,5,9,1,-3,9,8,-4,6,-4,-9,10,-5,6,-6,-5,2,-8,-8,-2,-6,1,-2,4,8,-7,-1,6,2,7,1,-4,-4,3,1,-2,-10,-2,9,-2,-2,-6,6,8,-4,-7,-7,-7,3,-2,9,3,9,2,1,-7,-3,-7,-2,8,-2,-10,-7,-9,-1,9,6,-9,-7,-3,7,3,-10,10,9,-10,6,-9,9,7,2,-9,-8,-3,1,5,-7,-7,-3,1,-6,3,10,-7,4,10,10,6,10,-2,7,-9,6,-1,5,-10,-4,-7,9,-5,7,-8,-7,-2,-4,-7,2,5,-4,-8,10,-3,3,1,3,-4,3,9,8,4,8,5,9,-9,-8,-3,-6,-3,8,2,9,-4,-2,10,-4,4,-8,-3,8,-10,-10,-3,3,7,9,3,-9,-2,-1,1,-9,-9,-1,-1,-4,-5,8,-1,5,10,-7,-6,3,-7,10,-10,-10,-3,-1,2,-9,-8,-7,6,6,10,3,2,-3,8,5,-2,7,8,2,-3,-8,-8,9,1,-1,1,-6,-8,1,2,-6,-3,-10,10,4,2,4,9,5,-3,10,10,6,-6,-6,3,3,-4,8,4,9,3,8,-9,3,-9],[5,-10,-9,-5,5,8,5,-10,8,-2,3,-10,-9,-4,-2,-7,6,7,-4,-2,-2,8,4,8,-5,9,-10,-9,-10,1,-7,9,6,1,-8,-10,5,8,9,3,8,1,3,-7,2,6,-6,3,1,-3,-8,1,-2,-3,5,-2,2,-3,3,9,-9,5,4,-9,-1,-5,-3,2,-3,4,-5,-3,2,-1,5,8,-6,1,-10,-4,1,2,6,-9,1,7,4,2,-5,10,-2,5,-3,10,5,8,5,-1,-6,-10,-6,4,6,-7,-6,2,-7,-7,-3,6,1,5,-4,7,-7,-8,3,-4,-7,-1,-7,-2,-1,-5,-8,-6,4,4,-8,-7,-7,9,-8,-10,-3,9,-5,-4,-2,3,-9,8,10,1,-5,6,-5,4,9,8,5,2,10,8,-7,1,-2,9,-3,2,9,1,-3,9,1,6,7,-7,5,9,10,8,-9,6,7,1,5,2,-1,2,8,-7,5,2,-3,4,10,-5,-10,4,-8,3,-9,3,-6,1,4,-9,-5,-1,-3,-10,-6,4,6,3,-5,7,-3,-3,7,5,5,10,-4,-6,7,-9,-3,-1,3,2,2,1,10,-6,-1,8,-4,3,3,-6,9,3,10,-2,-10,2,-2,9,8,-10,-6,-2,9,10,-7,2,4,8,9,-9,-4,1,4,9,7,9,-8,-6,6,-8,-4,9,-6,-2,-6,-4,-1,-6,6,7,5,-7,-6,-1,-8,-5,9,-10],[2,-2,4,1,-2,2,-4,-1,4,-1,10,-3,1,3,-4,5,-7,-8,-4,10,-6,3,-9,9,10,-4,-2,-1,4,2,-8,-8,5,-8,3,-2,8,10,-10,3,-9,-2,-3,-3,-6,-7,-4,-9,-10,-8,5,-5,7,-4,-4,-7,-5,3,2,7,3,-2,10,5,-10,-5,5,2,5,7,5,2,2,10,-3,2,10,4,7,9,2,-4,2,-9,4,-6,-1,-10,6,-7,-4,7,-4,3,-10,-9,-4,9,1,-5,-3,3,-1,-7,5,-8,-4,5,3,1,10,-6,-3,2,-5,8,-2,-2,-5,10,4,1,2,-9,-3,8,8,-8,1,6,1,-5,-6,3,-7,-3,2,2,1,-9,-10,8,3,3,-9,1,5,-10,5,4,10,-7,-3,-4,-10,9,-10,-2,-6,-8,-5,5,-4,-1,-2,-1,4,5,-6,-4,-4,10,1,-8,6,1,2,1,3,-5,1,-9,5,-4,5,-9,2,-2,1,1,-5,-1,10,-4,-8,-10,-8,-5,3,4,-9,6,4,4,9,5,8,2,7,-3,-7,-3,-1,8,8,-9,-6,-8,-2,-6,-8,4,4,-5,2,-8,-10,3,-1,-5,-2,-6,1,9,-6,6,-3,-9,-6,1,-2,-8,2,-6,-10,-4,7,-1,3,2,4,-5,-10,-5,1,-6,-7,-7,-4,5,-4,-8,-6,7,-8,1,1,-8,-2,-7,3,6,-8,2,-6,9,4,2,6,-3],[10,-6,-10,2,-1,5,-4,5,-3,-7,-2,2,-2,7,-4,4,-4,7,-9,8,-9,4,-1,7,-6,7,-9,-5,3,-2,-10,-3,9,10,8,-7,-8,-2,2,7,4,-7,4,5,-1,4,-3,8,8,1,-6,5,-1,-5,8,4,-7,-6,-10,8,-10,-7,-1,7,4,5,6,6,-9,-2,-2,-9,-7,9,8,1,10,-10,-4,8,5,-10,5,8,-6,9,7,8,-4,1,4,1,3,-5,-10,-7,-8,6,4,5,4,-9,-3,7,5,1,-2,-5,6,4,-3,-9,-9,-4,8,-2,-5,-5,1,8,-10,9,-3,-10,4,-5,4,-10,10,5,-1,-10,1,5,-9,-10,-5,-4,-3,7,6,-4,5,-3,-6,-1,-7,-5,10,10,4,8,-9,8,-5,-7,5,3,-5,-5,5,10,-8,-10,-7,-8,10,-10,8,-1,3,6,-1,-7,5,7,-9,2,4,-8,2,-1,3,1,1,6,10,-1,-1,7,-2,6,3,-1,-9,9,-6,-4,-4,-10,-7,-9,8,-7,-10,-5,-1,6,-8,-3,7,-8,2,1,5,9,6,10,-7,5,3,2,10,8,-6,-4,-2,-5,4,-8,-7,-2,6,9,1,1,-3,-8,2,2,8,10,-10,-2,-10,3,9,2,-9,9,4,-4,4,9,-7,-3,-7,-4,-7,-1,-9,4,-4,-1,7,3,-1,-8,8,-10,-10,-1,-3,6,-1,7,-5,-8,-7,-2],[-1,8,1,-5,-5,5,8,-4,2,1,1,5,-6,5,-2,-10,1,4,-5,-10,-6,8,2,4,-6,-9,-10,-2,-7,-2,1,3,1,3,-8,6,9,-7,10,5,4,-2,10,3,-1,10,8,-4,-3,-4,-10,-5,8,10,-3,3,-2,-4,-9,2,3,-1,-7,1,-4,1,7,2,7,-1,-10,-10,9,5,-10,-7,-10,3,5,-7,8,2,-3,-1,8,-3,-6,1,6,5,-2,8,-3,9,-4,7,-4,7,5,10,-10,4,-7,-5,-10,10,5,5,-10,7,1,-7,-3,4,4,3,-8,-4,-1,-1,-1,4,8,5,-6,-3,-8,-3,9,-1,1,9,-1,8,1,-5,-8,-8,10,8,8,6,4,-7,9,5,1,3,6,6,-9,-10,9,7,5,-9,5,-9,7,3,3,7,-4,8,2,-9,-4,-7,-1,4,10,-7,1,5,1,3,5,-9,-2,1,2,2,9,9,-6,5,8,-10,-7,6,-2,-3,-3,-8,-3,9,-8,-1,2,8,5,-5,-5,-4,1,-2,1,2,10,-8,-10,8,8,5,-1,2,-6,1,-4,-4,4,-8,1,-8,-3,-6,3,-8,-5,-5,-10,2,-3,-7,-5,2,9,4,-1,3,-9,4,4,7,9,-6,8,-4,1,8,6,-7,9,7,4,-3,-10,6,-2,-5,-4,7,3,5,-5,-1,-2,-6,-8,10,-2,4,3,-7,-5,-4,-7,5,4,-3],[-10,2,3,-2,10,2,8,-5,7,3,-8,5,8,5,-7,-5,-5,10,4,8,5,-7,7,1,5,8,-1,-9,2,-4,-6,-7,-3,-8,8,-10,-5,7,10,8,3,9,8,4,-5,10,-7,-10,-5,-7,4,7,8,-3,-1,2,-6,8,10,-5,-10,6,-5,8,-5,-2,-6,-2,2,-1,-6,-5,-5,-6,6,-9,10,4,2,-3,8,-9,4,-9,7,-9,4,-3,8,-5,5,-1,-9,-10,8,1,-1,-10,-2,-3,-10,9,-6,-2,-4,-9,1,3,6,3,7,9,6,2,10,-6,8,4,-8,10,-1,10,-10,4,-6,-9,-2,-10,-8,6,-10,8,-6,1,9,7,-10,-4,3,6,4,2,-4,4,-9,-1,3,-6,-4,-4,-8,-6,1,1,-7,-3,4,9,-10,-1,-5,5,-6,6,9,6,10,-8,-10,-5,9,10,-3,-3,-3,-9,1,-6,-6,8,10,-3,-3,-3,3,2,6,-7,-4,-2,-7,5,9,-6,4,10,-7,6,7,7,-1,-2,-2,8,9,2,2,-3,-1,-6,2,-10,-1,3,10,-6,8,8,6,7,-5,-1,-8,-8,3,5,9,8,-2,8,8,2,3,-7,5,4,5,-7,-10,-4,-8,-10,-4,9,-9,9,2,-3,-1,-5,4,-6,-7,-2,9,-1,4,-8,-10,-6,3,-6,7,3,10,2,-9,3,-3,-2,10,1,-5,-2,-5,5,6,-6,-1,-10],[-7,4,-3,2,9,-8,7,3,-10,6,5,-7,3,5,2,-4,8,-5,-3,6,-10,1,8,9,8,5,-9,6,6,5,-7,-7,6,-7,-10,1,9,-7,-5,-7,4,-8,-6,4,-6,-2,-7,-1,2,10,-10,3,-4,-8,-9,-9,9,-3,-2,1,-5,4,-3,-4,2,8,-8,5,1,8,10,-2,-5,-6,-3,6,9,1,4,8,3,9,-8,1,8,1,7,9,-10,10,1,3,-9,-3,-2,-10,-10,6,5,-7,-7,3,4,7,-6,-7,-6,-8,-7,-7,-5,-5,7,-2,1,9,10,1,3,-7,-6,5,-7,6,-5,4,-1,4,-4,-4,6,2,-3,-9,2,7,-10,-1,-7,-10,1,4,-7,-2,3,-6,9,-4,-1,-1,8,-3,10,5,1,2,1,6,4,-9,-3,-7,-10,-7,5,6,-7,4,-4,-7,-4,7,-4,-3,10,-7,-4,-7,7,-7,-3,-8,3,10,-8,-2,-5,-10,-3,-9,-5,-8,-3,7,-1,2,7,-6,9,8,2,-2,9,8,-6,-5,-5,2,-9,8,3,-6,10,-3,-8,8,2,-7,-1,5,3,-10,4,-8,1,5,-6,6,-4,2,-1,4,-10,4,-7,1,-10,10,-3,7,4,9,4,3,4,10,8,9,-6,-1,4,2,-5,8,-3,-1,8,5,5,9,-5,-5,4,1,8,2,-6,-6,9,8,-2,8,-10,3,3,5,3,-1,5,-9]],[[-5,-5,-5,9,-6,5,7,7,6,-1,1,7,7,3,9,2,-2,3,9,-1,-1,2,-10,5,10,5,3,7,7,1,3,9,2,3,8,-8,-2,8,1,6,-1,-3,2,-6,2,-6,-3,-10,-9,-8,-9,-7,-7,1,-8,9,9,-4,2,1,-7,8,-3,5,-3,8,-7,3,10,2,-4,-9,-3,-5,3,8,2,-10,-8,7,-5,-5,2,8,3,-3,-1,9,5,6,9,-8,3,8,-2,-3,1,-1,6,-6,7,4,-2,-1,-7,5,-2,9,-10,7,1,8,7,-7,-9,10,4,4,-6,-1,4,1,8,1,6,-1,-9,-10,-10,-7,-2,5,-2,-10,-5,-3,8,5,1,-5,8,-5,8,-1,-4,7,7,10,4,8,-2,10,-3,7,3,-3,1,-5,-5,5,-7,5,-8,-5,-8,2,2,-1,9,2,-1,2,-5,1,5,1,-10,-8,-5,1,-6,5,-6,-6,8,6,3,3,5,9,-10,4,1,10,-6,1,-5,1,-7,-8,-5,4,10,-5,1,-7,-8,-3,-4,7,8,-4,-8,-6,-2,-10,7,-6,-1,-6,-6,-5,3,-5,3,-6,10,5,5,-3,-6,-5,-6,1,-1,-2,-9,3,-7,6,-10,2,-2,-10,-8,3,5,-6,8,-2,6,8,-3,5,9,9,-6,1,-7,5,3,7,8,3,-3,-7,-1,2,7,-3,1,-6,-4,-2,-8,-8,5,-9,1,8],[-6,-2,-9,-10,-2,-3,-6,7,-7,-3,-6,-4,-8,-3,-4,2,-6,-7,-9,-3,2,3,6,10,-10,6,5,6,-4,2,-2,2,-1,4,7,-10,-5,7,-6,5,-9,2,3,-7,9,-9,-8,-8,9,8,3,-5,2,10,-8,-3,-7,2,5,9,1,-4,6,-7,-7,-10,-2,7,-6,3,3,2,-1,8,-6,-9,-4,7,8,-2,6,3,7,-3,8,-9,-9,1,-5,-5,5,-7,10,8,5,-1,3,2,-6,3,10,7,2,1,-6,-6,2,-1,-7,-10,-10,-7,5,-3,4,-8,-9,-4,-2,8,-3,2,-10,-10,3,-1,-9,4,-8,8,4,-6,3,-3,7,7,-6,5,-2,-2,3,8,2,9,-10,3,2,-6,-1,10,-10,6,-5,-9,6,-4,5,-2,-5,-8,-5,-10,2,4,4,-1,-2,-10,10,6,9,6,3,10,6,-2,8,-1,-9,-6,-8,7,6,7,-7,3,-4,-1,-4,4,8,4,-9,8,8,10,3,-8,-7,4,-9,-1,5,-9,-2,10,8,-7,6,4,3,2,3,2,8,-5,4,-1,7,-9,-10,10,2,-4,7,4,3,-4,7,-6,6,1,9,-9,1,-5,7,-10,5,7,3,-1,-9,-3,-3,-3,-4,8,-8,8,-7,2,-10,-4,8,8,5,2,-6,-10,5,7,10,1,-4,-7,5,4,-2,2,-10,-5,-2,8,-1,-9,6,6,-1,3],[-9,6,-10,9,1,-5,-6,7,-7,-7,5,-7,-10,-6,1,8,-8,5,-5,1,8,6,-6,3,7,-2,-4,5,3,6,-1,-5,7,8,-6,9,-4,-9,7,4,10,10,6,-7,-7,4,-7,8,10,-7,4,10,10,-10,9,-5,-3,-4,-10,-9,-4,-6,3,7,9,-10,2,5,-1,-3,9,1,2,-3,6,3,7,3,3,-3,-7,-9,7,3,9,8,3,-1,5,-9,-6,-3,2,-2,7,9,-2,-3,2,-7,-9,8,6,-6,3,-2,-8,1,2,-4,9,-4,-4,10,-10,-7,-9,2,-6,6,6,8,6,3,-3,8,-10,2,7,10,-8,10,-3,5,-1,-9,-3,-10,-6,-7,-9,2,-5,-3,-8,-4,1,-6,-4,-4,-1,1,-7,3,3,-6,-4,2,-5,-6,10,-9,-1,7,-5,-2,3,-10,-6,6,4,-2,10,-8,8,10,-3,3,6,-1,3,7,1,-6,4,-6,6,5,-1,3,-8,-1,1,-4,6,-8,-1,2,-4,-8,-10,5,4,4,-4,7,7,2,4,3,-3,6,5,7,6,-8,-2,4,4,3,2,-1,-10,5,10,1,-10,-1,-4,-6,4,9,-10,3,-9,-3,6,10,-8,-7,6,2,-6,-2,-1,-3,4,-4,4,-10,2,4,7,4,-10,4,1,-3,-10,7,5,8,-1,6,8,8,9,-9,-7,-4,4,-6,-5,-1,-4,-8,-10,10,9,-7],[-2,-10,-9,9,-2,7,-4,-8,-10,6,7,4,-10,-9,10,7,-2,-5,6,7,9,-3,-6,2,1,-1,1,8,-8,2,4,10,-8,5,8,-1,7,-2,6,9,1,6,3,-5,10,1,-9,-7,3,-1,7,10,6,7,5,7,-5,-1,-6,1,6,-9,-2,-1,2,8,2,3,1,1,-7,-3,3,3,2,7,-8,2,5,-7,-3,-6,4,-6,1,-2,-6,-3,10,-6,3,-10,-10,-1,6,-3,4,8,9,4,9,-10,-2,2,10,4,-3,-4,-9,-9,-2,7,-2,-5,-7,2,-6,1,-7,10,4,1,-2,-2,10,7,-4,10,-7,4,6,2,-10,10,9,-5,5,10,-10,8,4,2,10,-1,-6,3,-2,-4,1,10,-3,4,-2,5,7,-10,7,-8,-3,-5,5,-3,-4,-1,-2,-6,-7,-4,5,1,-3,4,2,-8,-10,-5,3,-1,-6,4,3,-6,-2,-9,2,-10,10,6,3,-6,8,-7,-9,8,9,7,1,4,6,10,-5,4,2,7,3,-10,5,2,6,-1,-9,8,-10,5,6,-3,-6,6,6,-5,7,1,-3,-5,-10,-3,-5,-1,3,-10,-3,-2,1,-7,1,7,9,9,-1,-2,-3,2,-8,-2,10,10,6,-2,-9,-5,3,8,7,6,4,-9,-5,-4,5,-3,-7,-8,-4,1,9,6,5,4,5,-2,-9,7,-3,6,4,-10,-4,-3,9,4],[9,10,5,-8,5,9,-2,-10,5,10,5,2,10,-8,1,-7,-3,4,10,-6,3,-8,2,-1,-4,-8,-3,-10,6,-2,-9,5,5,-10,3,-9,-3,-5,-7,-2,7,1,8,3,-9,-1,3,2,7,-4,-10,-9,1,8,10,2,9,5,5,3,4,-6,-10,-6,10,9,4,5,-4,5,2,-9,-1,2,6,-1,9,-7,6,8,-5,8,-7,-5,5,-2,7,7,10,3,-5,4,2,7,-7,5,-3,9,7,8,-4,-6,6,7,5,9,6,5,7,7,-8,7,-7,-1,2,4,-2,7,6,-3,5,10,-7,1,-5,-9,-1,4,3,-2,-7,-1,7,-8,-1,3,-2,1,-5,5,-1,5,-1,1,6,-8,-10,-3,-8,-9,9,7,4,-3,10,-1,2,-4,6,-6,-1,-5,-5,7,7,-4,-9,-10,-9,-9,10,-2,5,3,3,4,-6,-4,-7,-6,-8,-5,-1,9,-7,-1,-10,9,-2,9,-2,1,3,-10,-8,-9,7,5,-8,-10,-3,-3,-5,-10,-5,-4,3,-6,1,-9,4,-7,-9,-9,-7,3,9,6,-6,-2,-5,-7,-10,-5,9,-1,-1,4,-1,6,-1,1,-4,-5,-3,-1,-3,-7,1,5,-7,5,-5,7,-1,5,3,-1,2,9,-2,4,-9,8,4,-2,-10,-10,-5,2,-3,7,4,4,5,-1,-2,-2,-7,-2,6,3,-10,-2,1,4,-4,9,10,-5],[-5,-2,1,-9,-4,1,-5,-7,-9,-4,6,4,9,-7,-9,4,1,2,-9,2,1,5,-8,-1,-3,7,2,-7,-7,10,9,1,-1,1,3,3,-7,-10,-3,9,-7,-5,-8,-10,9,10,-5,7,3,5,-3,1,-1,4,5,9,-10,9,-9,2,10,-7,2,-10,-3,-2,-7,10,-6,-3,-8,3,7,5,-2,5,8,6,5,4,4,8,-8,1,-1,-7,7,8,-5,-1,9,-8,5,6,1,-7,5,-8,4,-1,2,-5,-9,4,-5,10,8,-10,3,4,-7,8,-8,6,-4,6,-4,-6,1,6,4,9,-3,6,4,-7,10,-4,-2,8,-9,5,-5,-6,-2,2,6,9,-10,-5,-4,7,10,4,-4,-1,9,6,-8,10,-3,-5,4,2,8,8,2,7,9,-5,4,-5,3,-6,-2,-2,-7,-7,10,4,-7,-1,10,-10,-9,-1,2,-7,7,-7,-8,-5,-5,-7,-2,-4,-5,-7,-4,5,1,-10,4,-7,1,-10,-10,-5,9,-9,-4,1,9,-6,4,-10,-7,-7,8,-2,7,-7,6,3,5,-8,6,-8,-7,2,6,-6,4,6,7,-10,-9,-3,-10,-2,-10,-4,10,-5,-6,8,-9,-9,-8,-5,-4,-9,-6,9,1,-1,-4,9,-6,-2,-3,6,-5,-7,1,-7,-10,7,-1,2,-10,4,7,-7,-10,-5,9,7,6,8,5,-2,4,-1,-8,8,5,3,5,-2],[10,10,-9,-5,8,-4,-1,-9,10,1,-10,-7,10,6,-9,-2,6,-10,8,3,1,10,6,10,-7,3,9,-2,-9,4,-9,-8,-10,-1,4,-4,-1,-10,2,-2,-8,-6,-4,-7,9,2,-10,2,-9,-6,-8,1,-5,-8,-10,5,5,6,-2,-4,-4,10,7,4,6,2,-2,-3,5,-3,-2,-2,2,8,-8,-8,9,6,9,-5,-10,6,1,1,3,-8,4,1,5,-1,-2,-7,4,-8,-3,-7,7,7,5,3,-1,2,-8,-1,-2,7,-9,6,10,-6,4,-8,-7,10,-2,-9,-3,-8,3,5,-2,-1,9,-6,-1,1,-6,-8,-3,-6,-1,-10,5,7,-9,-5,-7,2,8,-6,-10,4,-6,-2,1,4,2,-8,3,-7,8,-3,-2,2,5,-9,-4,3,-5,9,-3,-10,10,-4,-3,-5,-4,-7,-5,8,-8,-5,8,-4,-4,-1,-7,-2,8,10,-8,2,3,-10,-2,-8,-5,-5,-10,-8,-4,-3,-9,-8,2,8,-2,4,2,6,4,4,-7,-4,8,3,-2,-2,1,10,9,3,-8,1,-1,-2,10,-6,-5,-4,-4,-4,3,-9,-8,-8,-5,-10,-10,-3,-7,7,2,-4,4,9,-5,4,1,-4,10,-7,5,-10,-8,5,9,-3,-7,-8,-5,9,-2,-9,4,-5,7,1,-9,6,-3,3,5,3,-4,-3,9,-8,2,-5,3,5,2,-4,9,8,-3,4,-10,-9],[7,1,3,7,1,6,-4,5,-8,-6,-7,9,-7,9,9,10,-2,-3,4,-2,6,8,10,-5,-2,-3,5,-10,-4,-10,7,-2,2,-3,9,-1,5,4,-5,-4,-10,-6,9,-7,-5,10,6,-10,-9,-7,10,3,9,3,-6,1,-3,1,4,-7,-3,-10,10,9,3,-8,-4,-2,-10,-9,9,-2,-8,4,-9,3,-7,2,3,9,-7,-10,-9,4,-7,-8,2,9,-3,3,4,-7,-7,10,-2,7,-5,-10,9,-6,6,3,3,9,-4,9,8,-9,-7,-6,-6,-8,-10,-7,-2,-5,4,6,1,5,-8,1,2,-1,-9,-8,10,7,-2,-8,5,3,-3,-9,4,10,-10,-8,-1,1,-7,-4,-3,-6,-3,-9,8,-2,-1,-7,-6,-9,-8,-9,7,6,9,9,-10,8,9,-4,1,2,-8,9,8,10,-4,-2,9,2,-9,-9,-8,-2,6,6,5,-9,8,5,-5,-9,-4,-9,10,-8,-6,8,3,3,-10,-7,8,6,-6,-2,-7,-2,-4,1,-4,-3,-7,-6,-10,2,-9,-5,-6,5,-3,3,-9,-9,5,5,3,2,8,2,9,10,-2,-7,7,8,-10,-9,5,-10,-10,-4,4,2,-3,3,-8,-10,-7,9,-10,3,-10,-6,10,9,-2,2,-8,9,-9,-3,-3,-7,1,-6,5,-10,-2,1,-2,-4,3,10,2,-3,10,-8,-9,7,3,1,-3,-4,-7,8,5,-4]],[[8,10,-3,-3,-8,-10,-7,9,10,-9,-2,9,8,-1,-9,-3,-10,9,7,10,4,-4,-7,-3,6,-2,-3,-10,-10,5,-7,-10,-1,-2,-10,6,2,-5,5,-8,9,9,-2,-2,9,4,6,-3,-3,-7,-7,9,5,10,3,2,7,4,10,2,5,-7,9,10,-5,7,10,-3,9,6,9,-3,-9,6,5,1,5,9,-8,-8,-5,-8,2,-1,-5,4,-5,2,4,-3,7,6,-4,10,5,-6,4,7,-5,6,5,6,4,4,-8,-6,-1,-1,-9,-6,8,5,5,-5,-10,2,10,5,-8,4,6,-4,-2,3,-3,-6,-2,-2,-4,-1,9,-2,-3,-5,-6,8,-10,-2,-7,-6,5,-1,4,5,-10,4,8,-8,-3,-4,1,2,4,4,8,-4,-3,-9,10,-4,-8,2,4,-9,-3,5,-4,-5,-10,4,10,-10,-4,-7,3,-7,-2,9,6,-3,2,5,5,-8,9,-3,-9,2,-4,-8,-2,7,1,-2,-7,-10,-10,-7,-2,-2,-5,2,9,-5,-4,-9,-7,2,2,9,-8,-8,-1,-5,-8,-8,1,-6,5,-5,-6,5,9,-5,1,2,-4,-10,-5,-10,2,-5,9,7,-5,-10,5,4,5,6,-5,7,-9,4,2,9,1,8,7,3,6,-1,-3,6,6,3,-2,-9,-7,-7,7,4,-9,-10,-8,6,-8,-6,4,8,5,9,4,-8,-3,2,10,9,-8,8],[4,1,-5,-5,-10,8,6,5,-7,5,-10,9,-4,-1,-9,-10,7,7,10,-8,4,-8,-5,-4,-7,-2,5,7,2,-2,1,4,-3,7,-2,6,4,10,-8,-2,1,-10,-7,-6,8,-2,9,-6,-8,6,1,9,5,-3,-2,-7,-10,1,-5,8,6,2,-9,-10,1,-10,7,8,-7,-6,-5,-1,-2,-2,-1,2,-2,3,-3,10,-8,-8,8,-6,4,-5,6,4,10,5,-8,-7,9,4,2,8,4,2,10,8,-1,-7,-1,-5,8,-10,-4,9,-6,7,-6,-7,-1,-6,-8,-6,-9,8,-3,9,-10,10,-8,7,-1,-2,-9,9,8,10,-10,-5,-1,-9,5,-8,8,8,6,-10,2,-5,-2,1,-10,6,-9,-10,-5,7,-6,-4,2,10,9,-4,-3,2,-3,-7,-5,-4,-7,9,1,3,-10,2,1,9,-4,-1,-1,-4,7,7,6,10,-4,-7,-2,4,7,3,10,10,-6,2,-5,2,-8,5,2,7,-2,-3,-5,8,5,-2,5,10,2,-9,-8,8,-1,4,-6,-1,7,5,-3,6,4,2,9,-1,5,9,-2,-3,-9,8,8,-8,-3,7,-5,3,-10,-3,8,1,5,-9,8,-1,9,-6,9,1,6,8,-8,3,6,8,-9,9,10,10,-2,-7,-10,-9,5,-1,-8,2,-9,-6,2,-9,3,-4,8,1,5,-2,-10,-4,-10,6,5,4,5,-9,3,8],[7,-9,6,-6,9,-9,-6,-4,9,4,7,6,-7,-9,-2,-6,-6,6,6,-6,8,4,10,2,-7,3,-6,8,-5,-6,1,-8,7,-3,-3,-10,4,-9,-1,4,-9,3,-8,-9,-5,10,6,-3,9,8,4,-7,1,5,-6,9,7,-3,3,8,8,4,-5,9,-4,7,4,-8,-9,6,-3,-5,8,-5,-9,-9,-10,-10,-1,-10,5,-2,-3,-5,-7,-2,-7,1,4,-6,-1,-9,-7,8,6,-2,-9,-2,-9,7,-8,-6,-5,-10,-5,1,1,-8,8,6,-8,-7,-7,7,5,-1,4,-8,4,-9,6,4,-1,6,10,7,2,-3,2,4,8,2,3,-3,10,4,4,-1,-2,-8,1,-10,-7,4,5,-9,-5,4,-3,-5,-1,-8,10,-1,8,-3,-3,4,8,-1,7,-5,-5,10,-8,-10,7,3,9,8,-1,8,5,-6,-9,-5,1,9,-3,-3,-8,-9,2,2,5,-1,-2,4,1,2,9,6,-1,5,6,4,-2,8,-6,5,2,-2,5,4,4,-7,7,-4,-2,2,-8,1,1,3,-4,3,-6,-10,8,8,2,-6,1,-7,8,1,6,-7,-5,-8,-1,-3,-3,8,9,-3,3,1,-9,9,8,7,-3,-2,-5,7,9,-2,7,6,-10,-8,-10,9,7,-1,7,8,-2,-10,1,2,-1,4,6,3,-9,-9,2,-8,-5,4,7,-3,2,-6,5,3,-2,-4],[-7,6,-10,6,-2,-10,3,2,6,9,-1,1,2,-3,-2,-5,-6,6,-6,7,-9,9,-3,-4,-6,-8,-7,-6,4,-5,6,9,1,-7,10,-6,-3,10,6,8,6,-3,-7,-4,-6,-9,-9,4,4,6,5,2,1,-5,-6,10,-9,7,-2,8,1,10,-8,9,-4,-7,-1,7,8,8,5,8,-1,-1,-7,10,-8,8,-7,-7,4,-1,2,-4,10,-6,9,2,-10,-2,-1,5,-5,5,-9,-4,-8,-7,-1,-1,-2,9,-3,-1,3,8,-8,-3,-7,6,1,-1,2,-9,1,-7,9,4,6,-4,1,-3,6,-3,-4,-9,6,6,-7,5,5,1,-8,5,-4,-3,1,-5,1,10,-6,2,8,-2,-3,3,6,1,10,-10,-4,-9,-10,-2,10,-8,-10,8,8,-2,-6,-8,-8,-10,6,-3,2,7,-6,-3,-2,5,-1,9,5,-10,-4,-7,9,3,5,6,-9,1,4,2,-5,8,-1,5,6,-7,6,-7,1,-10,5,6,-1,-9,-1,10,9,-9,-5,-4,-2,5,7,4,-9,4,4,-8,-7,1,8,-1,9,7,6,7,2,-7,4,-7,-8,9,-1,9,3,-5,1,-10,-7,6,-6,-3,-7,-9,4,3,7,5,8,7,4,-4,9,5,1,-3,-4,-9,-7,-1,-4,-2,-6,-10,-3,-8,8,-9,-6,-7,6,5,-4,-3,3,-3,-8,-10,4,-1,-7,-1,2,4],[-4,6,10,-2,-8,-7,-8,-1,-5,-3,3,7,4,4,8,6,10,-4,5,-5,8,5,-2,4,-7,8,2,9,3,-6,3,5,-3,-4,-4,1,-8,-9,1,8,2,-8,-1,-2,10,5,9,-7,-10,9,7,-7,-6,-7,-2,7,-3,8,-3,8,10,9,7,10,-6,-1,-10,-1,-7,-3,3,10,-6,2,1,-3,7,-8,7,-2,-8,-7,3,5,4,8,-10,7,-7,5,1,8,-9,2,6,-10,-9,5,5,-2,9,-10,8,-3,6,-4,-8,-7,-9,-5,-5,3,4,-5,-9,-9,7,-5,5,-2,8,10,-10,-4,-7,6,-8,5,-7,10,-7,4,6,-1,-1,-4,10,-6,-2,-9,-1,-9,6,-10,6,10,-9,-7,6,-8,2,-6,5,-5,2,5,1,-4,-10,9,-4,-9,-3,-8,6,-6,5,5,3,8,-3,3,-9,-8,-9,4,8,-6,2,10,7,8,-9,5,-2,9,8,-7,9,5,-4,3,2,3,-1,-4,10,-2,5,-10,10,2,3,4,-7,-2,-8,1,2,6,6,4,1,4,3,5,-7,-1,6,-4,2,4,-1,-2,8,8,5,1,-8,-2,-10,2,3,10,7,-2,10,-1,-10,5,8,-3,5,-8,8,-2,6,8,7,7,-1,-5,5,-1,-6,5,10,-6,2,6,4,10,1,-7,3,-4,-5,5,-4,8,-3,-7,-1,-5,-9,-2,-8,2,8,8],[7,6,-3,-3,7,1,4,-2,1,5,8,-2,8,4,7,-7,-5,8,4,-7,3,-1,-5,2,-10,-5,-6,3,-5,10,-10,-6,-2,3,6,-10,-7,9,-6,8,-10,2,-2,-8,3,-8,-8,10,-1,-9,4,-7,10,4,7,-10,5,-10,1,3,-9,9,-7,7,-3,-4,-6,9,-7,2,5,10,7,8,-10,-2,-3,-6,1,8,-10,10,-5,1,-3,5,-6,1,-7,-9,-1,-5,5,7,-5,-9,-9,-2,-9,-6,8,2,8,-5,-4,1,-7,-2,-6,-8,7,-5,-8,1,-9,-2,10,-1,9,3,-10,9,-9,-2,1,7,7,4,-8,-3,-4,6,-8,2,2,-1,10,-2,2,-7,5,-2,-5,-8,-3,-1,-5,-3,-3,4,-4,10,6,4,-7,2,-4,-4,1,1,-4,-5,1,-6,4,-10,5,-2,-3,9,-9,3,5,2,1,4,-8,-6,6,3,-2,-8,-4,-7,7,8,9,1,9,4,9,-9,6,5,-7,-9,1,7,-8,-4,-2,-2,2,-9,-9,4,10,4,-9,7,7,-7,3,-6,10,-7,2,5,5,8,-8,1,-6,-5,5,-2,-8,-3,-5,-4,-10,-7,-4,-8,-8,-4,-9,-6,1,-1,-3,-1,4,-6,6,3,-4,-10,-5,-9,5,1,10,10,-1,10,-3,-9,-4,5,-4,7,1,6,6,-10,9,-4,1,10,4,-5,10,6,-8,5,-9,2,8,5],[5,4,7,3,-3,-7,5,-7,-8,1,4,-8,8,3,9,-1,-3,8,-6,-7,6,-7,-10,7,7,-3,-4,4,-2,10,-6,6,8,1,-5,-3,6,3,6,3,-10,6,9,7,-8,-5,-10,4,-2,-1,5,9,6,5,-6,9,7,9,5,9,5,-10,4,-2,-8,5,-9,-5,8,8,10,-9,3,3,8,-3,-8,9,-6,-10,5,10,-2,10,-4,-6,-6,-9,5,-6,8,5,4,-7,6,-5,-3,-5,-7,-6,3,-5,-7,7,10,4,-5,-3,-4,9,10,-10,-8,-9,-10,-6,-7,4,-7,5,-4,-3,-9,-10,-9,-4,3,-1,9,-6,4,-3,-4,4,-8,9,9,5,-10,-2,3,7,10,-9,-7,9,8,2,-1,-5,7,-2,-10,4,-1,-1,2,2,-6,-10,-5,-6,-3,7,7,10,10,8,-9,1,9,-2,-10,5,-3,-10,-4,-1,5,10,2,3,1,1,6,-8,4,7,6,9,-7,-10,-3,7,-1,-9,-6,-4,-8,7,-6,8,-8,-1,7,4,9,4,-6,-2,-9,-9,-5,-3,9,6,6,-3,-9,9,-6,-9,-8,9,-5,1,3,-8,-5,3,3,-9,-3,3,1,-7,6,4,-8,-8,-3,6,10,-4,7,9,7,8,2,-2,-5,10,7,-5,-6,-10,3,6,-2,-8,-10,-8,7,-8,1,-2,1,10,-5,-4,10,-3,-4,4,-1,-6,9,9,3,-5],[-7,1,-8,-7,5,-5,9,-8,6,8,4,10,9,-1,9,7,2,6,-8,-2,-6,10,4,-6,-1,8,10,1,1,2,-10,8,6,4,6,-8,3,-8,7,-7,-8,-4,-7,8,8,8,8,2,9,-7,-1,7,-7,3,9,-2,7,7,-2,-1,-4,10,4,-7,7,-8,-1,4,-10,-3,5,7,-3,5,9,8,5,-9,-10,-2,10,-7,4,10,6,-4,9,4,-6,-7,-7,2,3,-2,8,1,-5,1,-8,5,4,-7,-1,-7,4,-5,1,4,9,-8,-4,-4,-7,-10,8,1,5,7,2,6,-7,6,8,-3,-10,7,10,-4,-8,4,-10,-8,-4,4,8,-2,10,-5,2,9,-9,-5,-8,5,-3,-2,5,-9,-6,7,-2,-10,-8,3,3,1,8,10,-3,2,6,-9,5,-2,-3,-4,7,-7,1,7,4,5,-4,-8,1,-4,-5,10,3,10,10,-8,9,5,7,-3,10,3,-6,2,2,-6,9,6,7,-7,-9,5,-2,8,-2,10,-1,-7,-3,-6,-5,1,-8,5,10,-2,8,-9,-8,10,7,4,-5,7,-8,-3,5,6,-1,-7,-2,2,-6,10,5,6,4,-2,-8,6,-1,-8,3,10,-4,4,5,8,6,-7,-2,3,-2,-2,5,6,-9,4,10,-7,-10,2,7,-9,10,4,-1,-7,-5,1,8,-7,4,8,-7,8,-6,-5,2,7,-1,5,1,3]]], dtype = "uint8")#candidate|11847|(5, 8, 280)|const|uint8
bop_11848 = relay.multiply(bop_11830.astype('int16'), relay.reshape(const_11847.astype('int16'), relay.shape_of(bop_11830))) # shape=(5, 8, 280)
bop_11851 = relay.multiply(bop_11833.astype('int16'), relay.reshape(const_11847.astype('int16'), relay.shape_of(bop_11833))) # shape=(5, 8, 280)
func_10928_call = mod.get_global_var('func_10928')
func_10930_call = mutated_mod.get_global_var('func_10930')
call_11852 = relay.TupleGetItem(func_10928_call(), 0)
call_11853 = relay.TupleGetItem(func_10930_call(), 0)
func_3396_call = mod.get_global_var('func_3396')
func_3398_call = mutated_mod.get_global_var('func_3398')
call_11875 = relay.TupleGetItem(func_3396_call(), 0)
call_11876 = relay.TupleGetItem(func_3398_call(), 0)
func_4789_call = mod.get_global_var('func_4789')
func_4790_call = mutated_mod.get_global_var('func_4790')
call_11881 = relay.TupleGetItem(func_4789_call(), 0)
call_11882 = relay.TupleGetItem(func_4790_call(), 0)
bop_11890 = relay.minimum(bop_11848.astype('int64'), relay.reshape(const_11847.astype('int64'), relay.shape_of(bop_11848))) # shape=(5, 8, 280)
bop_11893 = relay.minimum(bop_11851.astype('int64'), relay.reshape(const_11847.astype('int64'), relay.shape_of(bop_11851))) # shape=(5, 8, 280)
var_11896 = relay.var("var_11896", dtype = "uint8", shape = (5, 8, 280))#candidate|11896|(5, 8, 280)|var|uint8
bop_11897 = relay.bitwise_or(const_11847.astype('uint16'), relay.reshape(var_11896.astype('uint16'), relay.shape_of(const_11847))) # shape=(5, 8, 280)
output = relay.Tuple([call_11761,call_11811,const_11813,var_11814,call_11842,call_11852,call_11875,call_11881,bop_11890,bop_11897,])
output2 = relay.Tuple([call_11762,call_11815,const_11813,var_11814,call_11843,call_11853,call_11876,call_11882,bop_11893,bop_11897,])
func_11900 = relay.Function([var_11814,var_11896,], output)
mod['func_11900'] = func_11900
mod = relay.transform.InferType()(mod)
mutated_mod['func_11900'] = func_11900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11900_call = mutated_mod.get_global_var('func_11900')
var_11902 = relay.var("var_11902", dtype = "int8", shape = (1056,))#candidate|11902|(1056,)|var|int8
var_11903 = relay.var("var_11903", dtype = "uint8", shape = (5, 8, 280))#candidate|11903|(5, 8, 280)|var|uint8
call_11901 = func_11900_call(var_11902,var_11903,)
output = call_11901
func_11904 = relay.Function([var_11902,var_11903,], output)
mutated_mod['func_11904'] = func_11904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3062_call = mod.get_global_var('func_3062')
func_3063_call = mutated_mod.get_global_var('func_3063')
call_11908 = relay.TupleGetItem(func_3062_call(), 1)
call_11909 = relay.TupleGetItem(func_3063_call(), 1)
output = relay.Tuple([call_11908,])
output2 = relay.Tuple([call_11909,])
func_11912 = relay.Function([], output)
mod['func_11912'] = func_11912
mod = relay.transform.InferType()(mod)
mutated_mod['func_11912'] = func_11912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11912_call = mutated_mod.get_global_var('func_11912')
call_11913 = func_11912_call()
output = call_11913
func_11914 = relay.Function([], output)
mutated_mod['func_11914'] = func_11914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11286_call = mod.get_global_var('func_11286')
func_11288_call = mutated_mod.get_global_var('func_11288')
call_11952 = relay.TupleGetItem(func_11286_call(), 0)
call_11953 = relay.TupleGetItem(func_11288_call(), 0)
func_8869_call = mod.get_global_var('func_8869')
func_8871_call = mutated_mod.get_global_var('func_8871')
call_11974 = relay.TupleGetItem(func_8869_call(), 0)
call_11975 = relay.TupleGetItem(func_8871_call(), 0)
output = relay.Tuple([call_11952,call_11974,])
output2 = relay.Tuple([call_11953,call_11975,])
func_11976 = relay.Function([], output)
mod['func_11976'] = func_11976
mod = relay.transform.InferType()(mod)
mutated_mod['func_11976'] = func_11976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11976_call = mutated_mod.get_global_var('func_11976')
call_11977 = func_11976_call()
output = call_11977
func_11978 = relay.Function([], output)
mutated_mod['func_11978'] = func_11978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5376_call = mod.get_global_var('func_5376')
func_5378_call = mutated_mod.get_global_var('func_5378')
call_11979 = func_5376_call()
call_11980 = func_5376_call()
output = relay.Tuple([call_11979,])
output2 = relay.Tuple([call_11980,])
func_11987 = relay.Function([], output)
mod['func_11987'] = func_11987
mod = relay.transform.InferType()(mod)
output = func_11987()
func_11988 = relay.Function([], output)
mutated_mod['func_11988'] = func_11988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6526_call = mod.get_global_var('func_6526')
func_6527_call = mutated_mod.get_global_var('func_6527')
call_11989 = func_6526_call()
call_11990 = func_6526_call()
output = call_11989
output2 = call_11990
func_11991 = relay.Function([], output)
mod['func_11991'] = func_11991
mod = relay.transform.InferType()(mod)
mutated_mod['func_11991'] = func_11991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11991_call = mutated_mod.get_global_var('func_11991')
call_11992 = func_11991_call()
output = call_11992
func_11993 = relay.Function([], output)
mutated_mod['func_11993'] = func_11993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3311_call = mod.get_global_var('func_3311')
func_3312_call = mutated_mod.get_global_var('func_3312')
call_11999 = relay.TupleGetItem(func_3311_call(), 4)
call_12000 = relay.TupleGetItem(func_3312_call(), 4)
var_12003 = relay.var("var_12003", dtype = "float64", shape = (5, 8, 1))#candidate|12003|(5, 8, 1)|var|float64
bop_12004 = relay.logical_xor(call_11999.astype('uint64'), relay.reshape(var_12003.astype('uint64'), relay.shape_of(call_11999))) # shape=(5, 8, 1)
bop_12007 = relay.logical_xor(call_12000.astype('uint64'), relay.reshape(var_12003.astype('uint64'), relay.shape_of(call_12000))) # shape=(5, 8, 1)
func_6270_call = mod.get_global_var('func_6270')
func_6271_call = mutated_mod.get_global_var('func_6271')
call_12008 = relay.TupleGetItem(func_6270_call(), 2)
call_12009 = relay.TupleGetItem(func_6271_call(), 2)
output = relay.Tuple([bop_12004,call_12008,])
output2 = relay.Tuple([bop_12007,call_12009,])
func_12017 = relay.Function([var_12003,], output)
mod['func_12017'] = func_12017
mod = relay.transform.InferType()(mod)
var_12018 = relay.var("var_12018", dtype = "float64", shape = (5, 8, 1))#candidate|12018|(5, 8, 1)|var|float64
output = func_12017(var_12018)
func_12019 = relay.Function([var_12018], output)
mutated_mod['func_12019'] = func_12019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7292_call = mod.get_global_var('func_7292')
func_7294_call = mutated_mod.get_global_var('func_7294')
call_12109 = relay.TupleGetItem(func_7292_call(), 0)
call_12110 = relay.TupleGetItem(func_7294_call(), 0)
output = call_12109
output2 = call_12110
func_12114 = relay.Function([], output)
mod['func_12114'] = func_12114
mod = relay.transform.InferType()(mod)
mutated_mod['func_12114'] = func_12114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12114_call = mutated_mod.get_global_var('func_12114')
call_12115 = func_12114_call()
output = call_12115
func_12116 = relay.Function([], output)
mutated_mod['func_12116'] = func_12116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12114_call = mod.get_global_var('func_12114')
func_12116_call = mutated_mod.get_global_var('func_12116')
call_12136 = func_12114_call()
call_12137 = func_12114_call()
output = relay.Tuple([call_12136,])
output2 = relay.Tuple([call_12137,])
func_12163 = relay.Function([], output)
mod['func_12163'] = func_12163
mod = relay.transform.InferType()(mod)
output = func_12163()
func_12164 = relay.Function([], output)
mutated_mod['func_12164'] = func_12164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4789_call = mod.get_global_var('func_4789')
func_4790_call = mutated_mod.get_global_var('func_4790')
call_12165 = relay.TupleGetItem(func_4789_call(), 0)
call_12166 = relay.TupleGetItem(func_4790_call(), 0)
func_6526_call = mod.get_global_var('func_6526')
func_6527_call = mutated_mod.get_global_var('func_6527')
call_12167 = func_6526_call()
call_12168 = func_6526_call()
func_7390_call = mod.get_global_var('func_7390')
func_7392_call = mutated_mod.get_global_var('func_7392')
call_12171 = relay.TupleGetItem(func_7390_call(), 0)
call_12172 = relay.TupleGetItem(func_7392_call(), 0)
output = relay.Tuple([call_12165,call_12167,call_12171,])
output2 = relay.Tuple([call_12166,call_12168,call_12172,])
func_12193 = relay.Function([], output)
mod['func_12193'] = func_12193
mod = relay.transform.InferType()(mod)
output = func_12193()
func_12194 = relay.Function([], output)
mutated_mod['func_12194'] = func_12194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4647_call = mod.get_global_var('func_4647')
func_4649_call = mutated_mod.get_global_var('func_4649')
call_12195 = relay.TupleGetItem(func_4647_call(), 1)
call_12196 = relay.TupleGetItem(func_4649_call(), 1)
func_4032_call = mod.get_global_var('func_4032')
func_4034_call = mutated_mod.get_global_var('func_4034')
var_12200 = relay.var("var_12200", dtype = "float64", shape = (420,))#candidate|12200|(420,)|var|float64
call_12199 = relay.TupleGetItem(func_4032_call(relay.reshape(var_12200.astype('float64'), [5, 12, 7])), 0)
call_12201 = relay.TupleGetItem(func_4034_call(relay.reshape(var_12200.astype('float64'), [5, 12, 7])), 0)
bop_12218 = relay.maximum(var_12200.astype('int64'), call_12195.astype('int64')) # shape=(5, 8, 420)
bop_12221 = relay.maximum(var_12200.astype('int64'), call_12196.astype('int64')) # shape=(5, 8, 420)
bop_12235 = relay.logical_or(bop_12218.astype('bool'), var_12200.astype('bool')) # shape=(5, 8, 420)
bop_12238 = relay.logical_or(bop_12221.astype('bool'), var_12200.astype('bool')) # shape=(5, 8, 420)
func_8778_call = mod.get_global_var('func_8778')
func_8779_call = mutated_mod.get_global_var('func_8779')
call_12244 = relay.TupleGetItem(func_8778_call(), 0)
call_12245 = relay.TupleGetItem(func_8779_call(), 0)
bop_12247 = relay.not_equal(bop_12235.astype('bool'), var_12200.astype('bool')) # shape=(5, 8, 420)
bop_12250 = relay.not_equal(bop_12238.astype('bool'), var_12200.astype('bool')) # shape=(5, 8, 420)
output = relay.Tuple([call_12199,call_12244,bop_12247,])
output2 = relay.Tuple([call_12201,call_12245,bop_12250,])
F = relay.Function([var_12200,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_12200,], output2)
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
