import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_552 = relay.var("var_552", dtype = "float32", shape = (10, 11, 2))#candidate|552|(10, 11, 2)|var|float32
var_553 = relay.var("var_553", dtype = "float32", shape = (10, 11, 2))#candidate|553|(10, 11, 2)|var|float32
bop_554 = relay.minimum(var_552.astype('float32'), relay.reshape(var_553.astype('float32'), relay.shape_of(var_552))) # shape=(10, 11, 2)
uop_561 = relay.sin(bop_554.astype('float64')) # shape=(10, 11, 2)
uop_580 = relay.atan(bop_554.astype('float64')) # shape=(10, 11, 2)
bop_596 = relay.not_equal(uop_580.astype('bool'), relay.reshape(uop_561.astype('bool'), relay.shape_of(uop_580))) # shape=(10, 11, 2)
uop_627 = relay.cosh(bop_554.astype('float64')) # shape=(10, 11, 2)
output = relay.Tuple([bop_596,uop_627,])
output2 = relay.Tuple([bop_596,uop_627,])
func_634 = relay.Function([var_552,var_553,], output)
mod['func_634'] = func_634
mod = relay.transform.InferType()(mod)
var_635 = relay.var("var_635", dtype = "float32", shape = (10, 11, 2))#candidate|635|(10, 11, 2)|var|float32
var_636 = relay.var("var_636", dtype = "float32", shape = (10, 11, 2))#candidate|636|(10, 11, 2)|var|float32
output = func_634(var_635,var_636,)
func_637 = relay.Function([var_635,var_636,], output)
mutated_mod['func_637'] = func_637
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1772 = relay.var("var_1772", dtype = "uint16", shape = (6, 12, 12))#candidate|1772|(6, 12, 12)|var|uint16
var_1773 = relay.var("var_1773", dtype = "uint16", shape = (6, 12, 12))#candidate|1773|(6, 12, 12)|var|uint16
bop_1774 = relay.equal(var_1772.astype('bool'), relay.reshape(var_1773.astype('bool'), relay.shape_of(var_1772))) # shape=(6, 12, 12)
func_634_call = mod.get_global_var('func_634')
func_637_call = mutated_mod.get_global_var('func_637')
var_1782 = relay.var("var_1782", dtype = "float32", shape = (220,))#candidate|1782|(220,)|var|float32
call_1781 = relay.TupleGetItem(func_634_call(relay.reshape(var_1782.astype('float32'), [10, 11, 2]), relay.reshape(var_1782.astype('float32'), [10, 11, 2]), ), 1)
call_1783 = relay.TupleGetItem(func_637_call(relay.reshape(var_1782.astype('float32'), [10, 11, 2]), relay.reshape(var_1782.astype('float32'), [10, 11, 2]), ), 1)
uop_1788 = relay.sqrt(bop_1774.astype('float32')) # shape=(6, 12, 12)
output = relay.Tuple([call_1781,var_1782,uop_1788,])
output2 = relay.Tuple([call_1783,var_1782,uop_1788,])
func_1802 = relay.Function([var_1772,var_1773,var_1782,], output)
mod['func_1802'] = func_1802
mod = relay.transform.InferType()(mod)
mutated_mod['func_1802'] = func_1802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1802_call = mutated_mod.get_global_var('func_1802')
var_1804 = relay.var("var_1804", dtype = "uint16", shape = (6, 12, 12))#candidate|1804|(6, 12, 12)|var|uint16
var_1805 = relay.var("var_1805", dtype = "uint16", shape = (6, 12, 12))#candidate|1805|(6, 12, 12)|var|uint16
var_1806 = relay.var("var_1806", dtype = "float32", shape = (220,))#candidate|1806|(220,)|var|float32
call_1803 = func_1802_call(var_1804,var_1805,var_1806,)
output = call_1803
func_1807 = relay.Function([var_1804,var_1805,var_1806,], output)
mutated_mod['func_1807'] = func_1807
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2198 = relay.const(6, dtype = "int16")#candidate|2198|()|const|int16
var_2199 = relay.var("var_2199", dtype = "int16", shape = (12, 13, 9))#candidate|2199|(12, 13, 9)|var|int16
bop_2200 = relay.equal(const_2198.astype('bool'), var_2199.astype('bool')) # shape=(12, 13, 9)
output = bop_2200
output2 = bop_2200
func_2219 = relay.Function([var_2199,], output)
mod['func_2219'] = func_2219
mod = relay.transform.InferType()(mod)
mutated_mod['func_2219'] = func_2219
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2220 = relay.var("var_2220", dtype = "int16", shape = (12, 13, 9))#candidate|2220|(12, 13, 9)|var|int16
func_2219_call = mutated_mod.get_global_var('func_2219')
call_2221 = func_2219_call(var_2220)
output = call_2221
func_2222 = relay.Function([var_2220], output)
mutated_mod['func_2222'] = func_2222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3270 = relay.var("var_3270", dtype = "uint32", shape = (10, 7, 6))#candidate|3270|(10, 7, 6)|var|uint32
var_3271 = relay.var("var_3271", dtype = "uint32", shape = (10, 7, 6))#candidate|3271|(10, 7, 6)|var|uint32
bop_3272 = relay.maximum(var_3270.astype('uint32'), relay.reshape(var_3271.astype('uint32'), relay.shape_of(var_3270))) # shape=(10, 7, 6)
func_634_call = mod.get_global_var('func_634')
func_637_call = mutated_mod.get_global_var('func_637')
const_3277 = relay.const([-8.207980,3.181092,-1.375171,-7.648763,-3.353911,8.979306,5.250133,-8.919025,7.755188,7.588727,8.828602,1.761382,5.976909,-2.549408,4.173218,-8.501175,-6.690241,4.942350,9.077559,4.124807,1.381881,3.265193,-0.542788,4.090175,3.848758,9.225080,-7.245188,-0.398748,-4.370430,-7.863415,-9.125749,3.953785,-8.580672,0.907783,-9.151893,9.613441,1.668574,4.939572,-2.697253,-7.946384,9.528114,-4.738015,-3.739494,3.484891,-7.394147,-2.613613,-5.090522,5.438310,-5.037505,-0.364659,4.618662,-1.277722,5.214555,-3.553716,6.412293,5.937827,-1.369156,-9.327942,-1.370195,-2.704759,9.907320,0.594335,-8.147939,-2.820410,6.080829,-7.946958,-9.679357,-7.974267,-7.562776,6.791317,3.167574,-7.681998,2.722308,-7.767633,-2.326864,-7.550736,5.775692,8.693279,-1.686407,-8.279021,-9.459722,-4.013607,8.767008,-7.544449,6.499425,2.775029,3.549417,-3.653390,-0.937572,-2.678037,4.449325,-1.157511,8.292221,3.718108,6.358021,2.036772,-1.216257,-7.225267,-6.293475,4.293284,1.794338,-9.721611,-6.184329,8.721321,6.275813,1.823414,-2.313249,7.958689,5.615222,4.559053,-2.618016,-8.525866,-4.800642,3.073224,-9.088051,-7.098058,7.786671,-3.924610,0.676868,5.767849,7.227960,-2.925008,-6.116925,3.701096,-6.669678,8.739354,-1.820950,4.636920,-0.826957,6.051850,2.370370,-3.876856,3.516765,-5.089939,-0.526920,6.990367,-6.018846,0.114110,-1.472697,-4.959665,3.940132,0.179686,6.035966,-3.465921,7.137607,-8.323368,6.954816,-5.439614,6.829200,-7.922590,-2.687100,-8.324972,9.735964,5.640387,-3.001796,-3.784503,2.335222,8.422805,-2.609547,8.594855,-8.949173,-4.782029,-8.133658,-4.183071,9.770950,-3.015798,-0.391398,-6.939045,-9.231954,5.351202,5.082444,7.982438,-1.553660,1.874036,-6.681458,-7.541617,0.509087,8.961711,6.158843,2.246977,-8.505557,-5.744047,-0.125771,-4.703998,3.198371,-4.765822,4.757181,2.100529,-3.441616,-0.195763,5.769915,0.569928,7.339290,2.557521,-8.477299,0.519959,-9.297362,-5.461392,-4.815872,5.840923,-6.221724,-9.299545,4.007485,9.055853,-5.929862,2.765451,2.763221,-8.902819,4.870433,0.475546,4.133634,-3.068083,9.079334,-2.475508,4.399496,8.505093,2.308187,9.618235,6.061266,6.255974], dtype = "float32")#candidate|3277|(220,)|const|float32
call_3276 = relay.TupleGetItem(func_634_call(relay.reshape(const_3277.astype('float32'), [10, 11, 2]), relay.reshape(const_3277.astype('float32'), [10, 11, 2]), ), 1)
call_3278 = relay.TupleGetItem(func_637_call(relay.reshape(const_3277.astype('float32'), [10, 11, 2]), relay.reshape(const_3277.astype('float32'), [10, 11, 2]), ), 1)
bop_3281 = relay.bitwise_xor(call_3276.astype('uint8'), relay.reshape(const_3277.astype('uint8'), relay.shape_of(call_3276))) # shape=(10, 11, 2)
bop_3284 = relay.bitwise_xor(call_3278.astype('uint8'), relay.reshape(const_3277.astype('uint8'), relay.shape_of(call_3278))) # shape=(10, 11, 2)
output = relay.Tuple([bop_3272,bop_3281,])
output2 = relay.Tuple([bop_3272,bop_3284,])
func_3287 = relay.Function([var_3270,var_3271,], output)
mod['func_3287'] = func_3287
mod = relay.transform.InferType()(mod)
mutated_mod['func_3287'] = func_3287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3287_call = mutated_mod.get_global_var('func_3287')
var_3289 = relay.var("var_3289", dtype = "uint32", shape = (10, 7, 6))#candidate|3289|(10, 7, 6)|var|uint32
var_3290 = relay.var("var_3290", dtype = "uint32", shape = (10, 7, 6))#candidate|3290|(10, 7, 6)|var|uint32
call_3288 = func_3287_call(var_3289,var_3290,)
output = call_3288
func_3291 = relay.Function([var_3289,var_3290,], output)
mutated_mod['func_3291'] = func_3291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3758 = relay.var("var_3758", dtype = "float32", shape = ())#candidate|3758|()|var|float32
var_3759 = relay.var("var_3759", dtype = "float32", shape = (14, 14, 3))#candidate|3759|(14, 14, 3)|var|float32
bop_3760 = relay.divide(var_3758.astype('float32'), var_3759.astype('float32')) # shape=(14, 14, 3)
bop_3764 = relay.mod(var_3758.astype('float32'), bop_3760.astype('float32')) # shape=(14, 14, 3)
output = bop_3764
output2 = bop_3764
func_3810 = relay.Function([var_3758,var_3759,], output)
mod['func_3810'] = func_3810
mod = relay.transform.InferType()(mod)
var_3811 = relay.var("var_3811", dtype = "float32", shape = ())#candidate|3811|()|var|float32
var_3812 = relay.var("var_3812", dtype = "float32", shape = (14, 14, 3))#candidate|3812|(14, 14, 3)|var|float32
output = func_3810(var_3811,var_3812,)
func_3813 = relay.Function([var_3811,var_3812,], output)
mutated_mod['func_3813'] = func_3813
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4137 = relay.var("var_4137", dtype = "float64", shape = (5, 2, 10))#candidate|4137|(5, 2, 10)|var|float64
uop_4138 = relay.log2(var_4137.astype('float64')) # shape=(5, 2, 10)
func_3810_call = mod.get_global_var('func_3810')
func_3813_call = mutated_mod.get_global_var('func_3813')
const_4141 = relay.const(1.514414, dtype = "float32")#candidate|4141|()|const|float32
const_4142 = relay.const([7.122150,4.649618,5.669607,2.454003,-6.816616,-8.230406,-9.881954,-7.017518,-5.344419,1.295583,-6.050742,-9.142147,8.219203,-0.330953,-4.060529,8.448371,-1.957071,-6.927377,-4.715981,2.850323,-3.258155,0.829596,8.905189,5.016367,-4.757246,3.273118,3.716399,-1.664218,-6.343436,3.024493,-1.360641,-7.883903,6.158951,-0.647445,-2.442170,-9.037258,-8.228250,4.265716,-4.647046,7.833898,4.446562,6.334370,-8.314669,-0.451119,-9.769682,-3.743763,-2.197474,3.128011,3.982092,5.465287,-2.934113,-9.467855,-8.819009,-5.137434,1.532540,9.353432,-9.410203,8.077328,-0.310161,9.955190,6.450913,-9.976684,-5.662086,5.042379,8.377500,-0.491577,8.196714,-5.802504,-9.546484,-6.573699,3.713503,2.737122,-2.133176,-0.254483,-4.410434,7.533742,4.723605,5.373404,1.271147,3.290074,-5.899856,-0.764113,0.585695,8.930694,5.281936,4.242486,3.083500,3.318600,6.078994,-5.364660,2.757160,2.918350,4.970335,1.807759,7.472081,-6.018165,-2.875503,2.468014,7.479123,4.168661,-3.850638,1.306210,5.992060,9.553960,9.414024,-6.350798,3.972178,8.057514,1.514711,-1.158493,-4.996800,-7.882732,4.153760,-2.889026,-9.645284,-2.117473,-6.378798,-6.063173,-9.850683,-4.256241,8.734629,-5.857488,-1.103441,-3.026238,-3.069722,-2.565057,7.174749,8.901852,6.502848,4.736684,-1.090051,-4.755026,-4.751239,-1.156228,5.235885,-0.789116,-0.942849,8.606829,-7.741080,-1.203431,-3.712785,3.482641,3.360514,7.235744,-2.915697,-6.462342,-2.245198,1.402785,3.589909,2.590911,-1.852168,3.994976,-9.307334,6.579775,-2.567249,-9.573248,6.289347,-5.604457,-7.221067,0.857614,0.842536,3.187018,-1.019388,-3.314685,1.354724,-8.710952,7.112717,-1.833107,7.451367,-3.745961,0.034193,-8.407845,9.748378,2.767359,-7.088592,-9.341483,-1.222601,9.715686,1.411946,-8.409963,3.899711,-0.869958,-6.876126,3.621150,3.252205,-4.865168,-6.589601,7.278863,3.921551,4.739311,8.194485,1.770885,-3.985189,-5.289834,-9.991963,-7.677966,-3.077869,-7.264434,5.796865,-4.175765,-6.921435,3.009519,3.021107,-0.595076,3.947742,5.767515,0.864309,-1.354813,0.728843,1.535487,2.109622,-2.690328,9.974654,-7.534028,-6.458612,1.470256,1.807548,0.537708,2.135758,-4.614156,1.926928,6.911364,-7.074807,-6.504292,-2.093040,-4.459709,3.195141,3.235274,2.308313,3.028076,-7.240397,-1.527743,4.337003,1.300074,6.998953,3.776486,8.934686,-8.005680,-0.640000,2.059076,-5.635313,-6.669027,-8.145150,-8.011258,-8.085255,8.348475,-6.281081,-9.476044,2.545747,-6.772722,0.514486,-2.453810,-0.889152,9.007988,0.507472,-9.740554,-8.623373,-1.548668,-6.582672,-3.548056,-0.709889,-5.681039,-4.314022,3.982623,-7.682592,-4.680609,6.261371,-7.542632,5.640343,2.637281,-9.478691,8.844630,-1.266696,-5.590485,-9.129434,2.783242,-7.661043,-5.210107,4.223323,7.183020,9.659389,8.836787,-7.978156,5.790485,4.943197,-3.895376,-2.822893,-3.438982,0.369682,7.780958,-5.888305,6.981794,-7.640947,6.604629,4.373325,8.378955,-7.543229,3.832452,-0.627722,5.412597,9.301954,-6.118928,7.286295,0.202706,5.877114,-8.972578,6.470482,-1.619900,7.312009,1.802760,-5.213938,-9.724294,-9.261705,0.311933,-2.285536,-2.179933,5.992599,1.460910,-7.907218,1.388343,7.979843,6.514119,5.491287,1.128321,7.044558,8.623654,1.009833,-5.342195,-5.371618,8.794453,-4.529872,-3.371385,-0.220199,-9.371937,-2.161919,-4.398106,-9.947405,1.351357,6.044777,-0.042991,9.414815,1.237533,7.625869,-1.933365,8.265164,-6.346820,-2.996400,2.926463,-2.363344,4.210148,-7.882984,3.685458,0.899426,-2.008785,0.712707,3.521265,7.352830,8.529491,-3.557343,-5.020013,4.069559,-4.529097,7.553876,-9.154865,4.310286,1.587623,3.290763,-9.770588,3.493308,-9.567543,-7.779749,2.929969,-6.979283,-7.198523,1.143136,-7.598401,-4.199558,-3.842490,4.402794,7.137926,-8.867734,-7.892168,9.994311,-8.557268,2.902844,6.446505,-2.960971,3.500283,-3.249097,2.458365,-3.159870,-8.040416,-2.406940,0.222366,-2.831036,3.316171,6.763218,-1.662727,-6.607907,1.127771,0.347733,2.921243,0.931335,-2.593530,6.184216,2.704137,-3.810303,-6.791563,-1.293196,-7.853048,-4.276693,4.190987,5.856200,8.435805,-5.416428,8.592426,0.425124,2.139456,-7.586189,-6.347908,-8.712162,9.759370,-7.732013,7.553968,9.146938,1.737518,6.965986,3.014474,-4.223104,7.365995,2.506557,3.186438,0.761404,-2.922188,-0.293472,5.584770,-6.211884,6.091422,-3.837055,-2.597683,-0.984969,-7.363836,-3.984182,-3.710008,-4.228172,-4.788504,1.653716,-3.059603,-2.240582,-0.926982,-8.669669,3.819045,-3.496679,6.929454,-4.981227,9.325493,5.881960,-8.532256,7.889712,-6.484112,-8.559079,-5.220820,-8.548648,2.321420,6.529814,-4.516710,3.680726,-9.472961,-2.908765,3.996651,1.141622,-7.810950,-8.106065,4.660330,7.978949,7.430050,-8.712722,5.175262,-1.940840,5.114279,-8.059062,2.850337,-5.930291,-7.466808,2.010168,8.167746,-3.962420,8.569349,-9.045258,-6.418560,1.102387,-1.591495,6.124905,-9.333893,-2.291770,5.689102,4.948715,-0.793580,2.232030,7.613893,-7.780113,1.165030,-6.415869,9.871813,4.458678,-6.796499,3.459366,-4.926551,8.874333,0.326573,6.586124,-3.195735,8.283848,-6.526841,6.252828,-9.408740,-5.464430,-9.104320,-7.966422,8.191011,-5.008604,-1.192902,-7.939143,-3.973121,-0.128187,2.612666,1.898176,-8.944266,8.133463,9.034336,-6.181554,-0.263316,6.457720,3.626375,1.500270,-0.692558,0.010350,4.248974,6.583586,6.633547,6.671194,5.355554,-0.098254,-1.803145,-8.602838,3.430489,7.757416,0.770588,-6.255311,-0.714211,-8.001673,8.545724,-4.494648,2.431596,8.063257,9.177868,-6.764040,0.635144,-1.318454,-4.687940,8.752250,-9.030488,5.220758,8.060263,-4.330840,2.789555,-7.765800,-0.753518,-1.145318,0.361277,-8.110518,-4.080855,3.340417,-6.848436,0.168984,3.515236,-0.156168,2.205968,0.724736,9.006620,3.456569,-6.903897,-6.487529,-3.337246,5.771173,-1.421477,-8.512768,-1.818144], dtype = "float32")#candidate|4142|(588,)|const|float32
call_4140 = func_3810_call(relay.reshape(const_4141.astype('float32'), []), relay.reshape(const_4142.astype('float32'), [14, 14, 3]), )
call_4143 = func_3810_call(relay.reshape(const_4141.astype('float32'), []), relay.reshape(const_4142.astype('float32'), [14, 14, 3]), )
const_4165 = relay.const([[[9.158399,-1.745015,-9.421530,-5.531614,-5.616333,6.112884,2.080369,-8.690153,7.413685,-8.403980],[-6.405936,-8.210897,0.008326,-7.279444,-2.146856,-4.732201,-2.457136,0.152250,9.645279,6.463452]],[[-5.541177,1.447732,-2.482886,1.257013,8.164497,6.523430,-2.984055,3.232870,3.398163,1.989535],[3.298634,-3.897839,-9.046152,-5.113587,1.662602,9.484761,1.629451,7.974962,-1.206904,1.814157]],[[-7.305018,-3.793605,8.123929,-6.181686,1.669732,-1.773419,-6.243710,-2.458386,-8.873166,-6.532673],[-6.124052,3.722551,-7.098555,5.973841,6.091149,-7.538939,-7.033423,8.840954,-4.923261,-9.078400]],[[1.597977,-9.181138,7.789063,-7.922706,-3.896003,5.953579,-3.453435,-0.491683,-7.476540,-6.022830],[-4.843301,1.116000,8.725850,-7.565091,3.087004,3.983501,1.252331,-0.377916,-5.705219,1.318887]],[[9.122782,-9.798610,9.764537,-3.575685,-0.885440,-7.711472,2.019032,9.940972,-9.664006,6.281274],[2.772023,-1.748315,-9.276402,9.608847,0.698260,2.000502,-2.014149,-9.626709,-7.908939,2.228512]]], dtype = "float64")#candidate|4165|(5, 2, 10)|const|float64
bop_4166 = relay.less(uop_4138.astype('bool'), relay.reshape(const_4165.astype('bool'), relay.shape_of(uop_4138))) # shape=(5, 2, 10)
uop_4174 = relay.tan(uop_4138.astype('float32')) # shape=(5, 2, 10)
uop_4184 = relay.acosh(uop_4138.astype('float32')) # shape=(5, 2, 10)
output = relay.Tuple([call_4140,const_4141,const_4142,bop_4166,uop_4174,uop_4184,])
output2 = relay.Tuple([call_4143,const_4141,const_4142,bop_4166,uop_4174,uop_4184,])
func_4187 = relay.Function([var_4137,], output)
mod['func_4187'] = func_4187
mod = relay.transform.InferType()(mod)
var_4188 = relay.var("var_4188", dtype = "float64", shape = (5, 2, 10))#candidate|4188|(5, 2, 10)|var|float64
output = func_4187(var_4188)
func_4189 = relay.Function([var_4188], output)
mutated_mod['func_4189'] = func_4189
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6195 = relay.const([[[-5,-6],[-5,2],[-4,7],[-7,-6],[10,-10],[-3,9],[-10,6],[5,-5],[-1,3],[-9,-4]],[[-4,-7],[-5,-10],[10,-8],[-10,-8],[7,10],[-8,-2],[6,-4],[8,8],[-8,-5],[-9,10]],[[6,-4],[-6,-7],[-4,4],[-1,-10],[-2,2],[2,-4],[-6,-5],[-5,-6],[-4,7],[3,-4]],[[-10,9],[-5,-6],[3,8],[7,-8],[-2,-10],[2,10],[-6,-8],[1,-6],[-10,-2],[-3,-3]],[[8,4],[3,10],[6,4],[6,6],[3,1],[-7,4],[-3,4],[7,-4],[1,2],[-1,1]],[[2,9],[-1,4],[-10,7],[3,5],[-2,-1],[8,-5],[7,-5],[2,8],[-5,-4],[2,10]],[[2,-9],[3,-2],[-5,-5],[10,4],[-9,-6],[8,5],[-2,10],[8,8],[-1,6],[1,10]],[[-2,-10],[7,10],[6,-7],[3,-8],[2,1],[-9,-1],[-7,4],[-6,5],[1,10],[3,2]],[[-7,4],[10,7],[9,1],[8,-8],[-10,3],[9,1],[5,-8],[1,-8],[8,10],[-3,1]],[[6,1],[5,-1],[4,-8],[-1,-4],[10,5],[-1,-10],[6,-8],[-9,-2],[-10,-1],[6,9]],[[-5,4],[-8,4],[-10,9],[-3,-2],[-1,9],[-9,6],[-6,4],[8,-2],[10,1],[-6,-6]]], dtype = "uint32")#candidate|6195|(11, 10, 2)|const|uint32
var_6196 = relay.var("var_6196", dtype = "uint32", shape = (11, 10, 2))#candidate|6196|(11, 10, 2)|var|uint32
bop_6197 = relay.left_shift(const_6195.astype('uint32'), relay.reshape(var_6196.astype('uint32'), relay.shape_of(const_6195))) # shape=(11, 10, 2)
func_1802_call = mod.get_global_var('func_1802')
func_1807_call = mutated_mod.get_global_var('func_1807')
const_6222 = relay.const([8,10,-7,-5,-5,2,1,-6,6,-6,-6,6,7,-1,3,4,3,1,9,3,-6,-1,-6,7,9,-6,2,-2,-3,-10,10,-10,-1,7,9,-3,4,2,-9,1,-4,4,8,7,-10,10,2,-4,-2,-3,10,6,8,-5,8,-4,10,-8,-5,-2,1,-4,3,-6,-1,-4,2,7,7,-8,6,7,1,6,10,8,1,4,10,-7,-8,-1,2,-2,-10,5,-4,3,8,9,1,-9,1,-6,-3,3,-5,-4,4,7,-8,-1,-5,-8,-6,-10,8,9,3,2,10,9,-2,4,3,-2,-4,-5,-7,-3,-2,2,-10,-9,8,-9,5,-6,5,2,1,-8,7,7,8,9,-1,-10,-3,4,-8,-10,4,-3,3,-6,-1,3,-10,2,-8,-8,3,10,6,-5,-10,9,-10,3,-8,-10,-5,-7,-3,3,-1,2,6,9,-7,-6,1,1,10,7,-4,8,-1,-4,-5,8,5,-9,-2,-5,-3,6,-10,5,4,9,8,7,4,4,8,3,-1,-8,-1,2,6,9,-6,6,-6,-7,-4,-6,8,6,-1,9,3,5,-10,1,-4,2,5,-1,4,-7,-4,9,-10,-8,-5,-5,4,-6,6,2,6,-1,3,1,-1,8,-1,9,-1,4,-4,8,-10,4,-10,7,2,8,-1,-3,-9,-2,-9,2,8,7,9,-1,8,7,4,5,-4,-1,1,-1,-6,-1,-2,4,10,-1,7,-8,-9,-2,-10,9,9,1,6,2,-3,-7,-7,4,-4,-6,6,5,-10,-8,-3,4,-1,-4,7,8,-9,6,10,3,4,5,5,7,7,8,4,-2,9,1,1,7,-8,6,-4,2,-10,9,-6,-3,-2,1,-4,-1,10,-10,-3,1,-3,-7,-7,4,5,3,8,2,-6,5,7,-5,-10,-8,-4,-4,5,2,10,9,9,-9,-7,-6,6,-5,1,-10,4,4,6,-5,-9,4,4,7,5,-10,-8,7,10,-7,-1,2,4,5,3,-2,10,-4,-9,-8,8,7,4,8,-4,-5,-3,-2,4,-8,1,1,-7,-4,5,-9,9,9,-9,-7,3,10,10,4,3,-1,3,4,7,6,-1,7,2,3,-2,-4,6,-4,10,-10,-9,7,-5,3,2,-3,4,-3,5,-8,10,-5,-8,3,-6,-2,6,-8,10,-4,-1,-5,9,3,-6,3,5,-2,-5,-2,10,6,1,8,7,6,-8,-3,3,-1,7,6,-9,4,3,-7,-7,-8,8,4,5,3,2,-10,-2,-3,4,10,10,-9,9,6,2,-6,10,-6,-1,10,-5,-8,3,5,-5,-3,8,-7,-10,2,-7,-2,8,3,9,3,-8,-2,-6,-8,-1,-5,-3,-5,-3,6,-7,8,8,-5,9,-2,2,-5,10,-1,-4,-1,7,3,5,2,8,7,3,5,-3,8,1,-6,-9,-4,-3,2,-3,2,4,9,-7,-2,-10,2,-5,1,-6,-1,-5,-7,-1,10,6,1,-7,-6,7,-5,-6,-10,-9,-1,9,-9,-6,-3,-5,-1,7,3,-10,-10,-4,6,4,-10,-7,10,-2,10,-5,-5,10,-1,5,2,-10,4,7,-5,6,-6,8,-10,-6,8,-7,-2,-8,3,7,-3,-6,-3,9,-4,5,9,-9,-4,3,-6,5,-7,-1,8,-6,4,-10,-4,7,1,1,5,-2,5,-1,6,-7,10,-5,-5,-1,-2,-8,-7,6,6,1,5,10,-7,-1,8,-7,-5,1,3,8,1,2,8,-8,-5,-6,10,-2,-9,-3,-10,-9,5,4,-10,-5,-6,-10,5,1,-9,-2,-4,-8,-7,2,-1,4,-9,-6,-1,-1,-6,-1,1,2,-8,-8,1,7,-7,9,8,-6,2,-7,10,9,-8,-10,-2,-8,-9,7,2,-1,-1,-9,-2,9,4,6,-3,-2,5,10,6,-2,-4,-6,10,-3,6,3,6,3,-7,6,3,-1,-1,8,10,-2,-8,9,6,3,6,3,10,-4,6,-7,7,9,-10,5,8,6,-10,6,-1,-9,6,8,9,-3,1,3,-7,-8,-1,10,-4,5,-3,9,1,10,-1,3,10,4,5,1,-2,-2,-4,2,9,2,-10,4,1,9,2,-4,10,-8,-5,-9,-10,8,3,3,-7,4,8,-9,3,2,3,-2,4,-8,-8,6,7,-1,-5,-2,9,-10,-5,-5,10,-4,3,-6,5,-6,10,-1,5,7,6,2,5,-2,4,9,-5,9,-10,-7,-8,9,4,-6,2,10,-5,3,8,-10,-5,8,-1,-9,1,-7,-10], dtype = "uint16")#candidate|6222|(864,)|const|uint16
call_6221 = relay.TupleGetItem(func_1802_call(relay.reshape(const_6222.astype('uint16'), [6, 12, 12]), relay.reshape(const_6222.astype('uint16'), [6, 12, 12]), relay.reshape(var_6196.astype('float32'), [220,]), ), 2)
call_6223 = relay.TupleGetItem(func_1807_call(relay.reshape(const_6222.astype('uint16'), [6, 12, 12]), relay.reshape(const_6222.astype('uint16'), [6, 12, 12]), relay.reshape(var_6196.astype('float32'), [220,]), ), 2)
func_3810_call = mod.get_global_var('func_3810')
func_3813_call = mutated_mod.get_global_var('func_3813')
var_6239 = relay.var("var_6239", dtype = "float32", shape = ())#candidate|6239|()|var|float32
var_6240 = relay.var("var_6240", dtype = "float32", shape = (588,))#candidate|6240|(588,)|var|float32
call_6238 = func_3810_call(relay.reshape(var_6239.astype('float32'), []), relay.reshape(var_6240.astype('float32'), [14, 14, 3]), )
call_6241 = func_3810_call(relay.reshape(var_6239.astype('float32'), []), relay.reshape(var_6240.astype('float32'), [14, 14, 3]), )
output = relay.Tuple([bop_6197,call_6221,const_6222,call_6238,var_6239,var_6240,])
output2 = relay.Tuple([bop_6197,call_6223,const_6222,call_6241,var_6239,var_6240,])
func_6258 = relay.Function([var_6196,var_6239,var_6240,], output)
mod['func_6258'] = func_6258
mod = relay.transform.InferType()(mod)
var_6259 = relay.var("var_6259", dtype = "uint32", shape = (11, 10, 2))#candidate|6259|(11, 10, 2)|var|uint32
var_6260 = relay.var("var_6260", dtype = "float32", shape = ())#candidate|6260|()|var|float32
var_6261 = relay.var("var_6261", dtype = "float32", shape = (588,))#candidate|6261|(588,)|var|float32
output = func_6258(var_6259,var_6260,var_6261,)
func_6262 = relay.Function([var_6259,var_6260,var_6261,], output)
mutated_mod['func_6262'] = func_6262
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6748 = relay.var("var_6748", dtype = "bool", shape = (12, 4, 11))#candidate|6748|(12, 4, 11)|var|bool
var_6749 = relay.var("var_6749", dtype = "bool", shape = (12, 4, 11))#candidate|6749|(12, 4, 11)|var|bool
bop_6750 = relay.logical_or(var_6748.astype('bool'), relay.reshape(var_6749.astype('bool'), relay.shape_of(var_6748))) # shape=(12, 4, 11)
func_2219_call = mod.get_global_var('func_2219')
func_2222_call = mutated_mod.get_global_var('func_2222')
var_6797 = relay.var("var_6797", dtype = "int16", shape = (1404,))#candidate|6797|(1404,)|var|int16
call_6796 = func_2219_call(relay.reshape(var_6797.astype('int16'), [12, 13, 9]))
call_6798 = func_2219_call(relay.reshape(var_6797.astype('int16'), [12, 13, 9]))
output = relay.Tuple([bop_6750,call_6796,var_6797,])
output2 = relay.Tuple([bop_6750,call_6798,var_6797,])
func_6800 = relay.Function([var_6748,var_6749,var_6797,], output)
mod['func_6800'] = func_6800
mod = relay.transform.InferType()(mod)
var_6801 = relay.var("var_6801", dtype = "bool", shape = (12, 4, 11))#candidate|6801|(12, 4, 11)|var|bool
var_6802 = relay.var("var_6802", dtype = "bool", shape = (12, 4, 11))#candidate|6802|(12, 4, 11)|var|bool
var_6803 = relay.var("var_6803", dtype = "int16", shape = (1404,))#candidate|6803|(1404,)|var|int16
output = func_6800(var_6801,var_6802,var_6803,)
func_6804 = relay.Function([var_6801,var_6802,var_6803,], output)
mutated_mod['func_6804'] = func_6804
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7131 = relay.var("var_7131", dtype = "float32", shape = (4, 1, 5))#candidate|7131|(4, 1, 5)|var|float32
uop_7132 = relay.atan(var_7131.astype('float32')) # shape=(4, 1, 5)
output = uop_7132
output2 = uop_7132
func_7136 = relay.Function([var_7131,], output)
mod['func_7136'] = func_7136
mod = relay.transform.InferType()(mod)
var_7137 = relay.var("var_7137", dtype = "float32", shape = (4, 1, 5))#candidate|7137|(4, 1, 5)|var|float32
output = func_7136(var_7137)
func_7138 = relay.Function([var_7137], output)
mutated_mod['func_7138'] = func_7138
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7316 = relay.var("var_7316", dtype = "float64", shape = (10, 7, 11))#candidate|7316|(10, 7, 11)|var|float64
uop_7317 = relay.rsqrt(var_7316.astype('float64')) # shape=(10, 7, 11)
func_2219_call = mod.get_global_var('func_2219')
func_2222_call = mutated_mod.get_global_var('func_2222')
var_7325 = relay.var("var_7325", dtype = "int16", shape = (1404,))#candidate|7325|(1404,)|var|int16
call_7324 = func_2219_call(relay.reshape(var_7325.astype('int16'), [12, 13, 9]))
call_7326 = func_2219_call(relay.reshape(var_7325.astype('int16'), [12, 13, 9]))
func_1802_call = mod.get_global_var('func_1802')
func_1807_call = mutated_mod.get_global_var('func_1807')
var_7339 = relay.var("var_7339", dtype = "uint16", shape = (864,))#candidate|7339|(864,)|var|uint16
var_7340 = relay.var("var_7340", dtype = "float32", shape = (220,))#candidate|7340|(220,)|var|float32
call_7338 = relay.TupleGetItem(func_1802_call(relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7340.astype('float32'), [220,]), ), 1)
call_7341 = relay.TupleGetItem(func_1807_call(relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7340.astype('float32'), [220,]), ), 1)
func_4187_call = mod.get_global_var('func_4187')
func_4189_call = mutated_mod.get_global_var('func_4189')
var_7346 = relay.var("var_7346", dtype = "float64", shape = (25, 4))#candidate|7346|(25, 4)|var|float64
call_7345 = relay.TupleGetItem(func_4187_call(relay.reshape(var_7346.astype('float64'), [5, 2, 10])), 3)
call_7347 = relay.TupleGetItem(func_4189_call(relay.reshape(var_7346.astype('float64'), [5, 2, 10])), 3)
func_1802_call = mod.get_global_var('func_1802')
func_1807_call = mutated_mod.get_global_var('func_1807')
call_7354 = relay.TupleGetItem(func_1802_call(relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(call_7338.astype('float32'), [220,]), ), 0)
call_7355 = relay.TupleGetItem(func_1807_call(relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(call_7338.astype('float32'), [220,]), ), 0)
func_1802_call = mod.get_global_var('func_1802')
func_1807_call = mutated_mod.get_global_var('func_1807')
call_7360 = relay.TupleGetItem(func_1802_call(relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7340.astype('float32'), [220,]), ), 0)
call_7361 = relay.TupleGetItem(func_1807_call(relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7339.astype('uint16'), [6, 12, 12]), relay.reshape(var_7340.astype('float32'), [220,]), ), 0)
uop_7365 = relay.cosh(uop_7317.astype('float32')) # shape=(10, 7, 11)
output = relay.Tuple([call_7324,var_7325,call_7338,var_7339,var_7340,call_7345,var_7346,call_7354,call_7360,uop_7365,])
output2 = relay.Tuple([call_7326,var_7325,call_7341,var_7339,var_7340,call_7347,var_7346,call_7355,call_7361,uop_7365,])
func_7368 = relay.Function([var_7316,var_7325,var_7339,var_7340,var_7346,], output)
mod['func_7368'] = func_7368
mod = relay.transform.InferType()(mod)
var_7369 = relay.var("var_7369", dtype = "float64", shape = (10, 7, 11))#candidate|7369|(10, 7, 11)|var|float64
var_7370 = relay.var("var_7370", dtype = "int16", shape = (1404,))#candidate|7370|(1404,)|var|int16
var_7371 = relay.var("var_7371", dtype = "uint16", shape = (864,))#candidate|7371|(864,)|var|uint16
var_7372 = relay.var("var_7372", dtype = "float32", shape = (220,))#candidate|7372|(220,)|var|float32
var_7373 = relay.var("var_7373", dtype = "float64", shape = (25, 4))#candidate|7373|(25, 4)|var|float64
output = func_7368(var_7369,var_7370,var_7371,var_7372,var_7373,)
func_7374 = relay.Function([var_7369,var_7370,var_7371,var_7372,var_7373,], output)
mutated_mod['func_7374'] = func_7374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7573 = relay.var("var_7573", dtype = "float64", shape = (6, 14, 1))#candidate|7573|(6, 14, 1)|var|float64
const_7574 = relay.const([[[2.547048,-7.323029,0.367770,7.163475,0.843290],[1.507091,0.644182,6.488401,1.686021,-2.106167],[0.003555,-4.386397,5.092261,6.300992,9.165503],[1.718304,5.458104,-8.455153,-7.284571,-4.566247],[-5.376927,2.611082,5.267176,-6.098571,7.597714],[7.249440,7.221884,1.179140,-5.763491,7.612033],[1.643249,-3.083238,1.200516,-5.941916,1.203019],[1.811117,-8.392923,1.663329,9.194906,-6.311593],[-4.861161,3.910574,-8.207744,-1.707469,0.030130],[-1.586094,-7.947588,-4.074562,2.881670,1.765140],[5.707048,-5.944156,-1.107296,-8.210826,7.251230],[-1.028639,-8.292062,-2.704329,-2.734979,6.099583],[-1.221771,4.382700,3.473817,-7.882347,-6.129950],[5.128864,-9.600170,5.388408,1.242335,-6.726660]],[[-2.834665,6.076179,0.101357,2.630994,-3.561341],[9.908950,0.773528,-1.459991,-7.912394,0.406901],[-4.601852,1.366284,5.086576,6.580092,-9.618294],[8.259763,-7.219945,8.221795,-0.894590,-3.164683],[4.979185,-7.338229,-1.845249,3.118447,3.586243],[6.462772,0.235816,3.909707,2.228038,-0.628892],[-5.993857,-0.150633,-0.064393,-8.249706,0.364222],[8.032208,9.148406,2.181054,-0.967137,-7.554515],[7.544146,-4.520271,-7.397079,1.253135,-5.848740],[2.710311,-4.937815,-7.873793,8.515483,7.514221],[7.077915,-2.122060,-5.019875,-3.554370,-2.306615],[4.621163,-3.693096,0.398013,3.576247,-2.444962],[-9.790056,-2.756476,2.544590,0.595413,-1.434660],[5.556366,1.615982,-8.722030,6.304360,9.288551]],[[2.099594,-7.427062,-7.589718,7.550960,-8.103097],[0.749000,3.497121,3.850334,-2.371954,-1.880450],[-1.139292,-3.602998,5.641540,1.716552,7.879229],[-7.817924,4.856126,-9.942646,-5.994070,5.161169],[4.318802,8.828728,3.597538,-7.994309,6.602554],[-1.836546,-7.099244,-8.232277,5.224600,9.443485],[-8.624811,9.795193,-8.048670,7.466097,1.086376],[8.264896,1.079399,-3.270261,-0.047724,4.794178],[1.871971,7.186929,-1.175405,8.074845,6.304526],[8.363327,-1.963711,-2.210958,-2.297386,-4.072869],[-5.022886,6.261334,-6.940366,-2.853372,-1.111468],[3.167685,8.761616,3.238754,-2.294306,8.979242],[7.703200,5.222051,-6.170976,-4.117326,1.050888],[-6.811741,5.170765,5.735667,5.099781,-9.079342]],[[9.711028,9.161973,-9.239772,4.097176,9.720097],[-7.057299,4.833192,7.110831,7.437151,-4.031347],[-5.713865,8.814132,-1.183970,0.360462,-4.193140],[5.728025,9.709177,5.176055,-6.672381,-9.269991],[0.710221,-6.737871,-8.332296,-7.672235,-7.646459],[-9.381087,-1.156207,-5.248604,1.111024,-7.727518],[0.868613,3.875513,6.024714,-6.433436,2.656872],[5.755191,5.354563,7.590407,2.739773,-9.567882],[7.106263,-8.084924,-9.411796,-2.662808,6.598613],[0.409705,1.315254,4.753731,5.559277,-7.417283],[7.353370,-4.192051,3.672146,-1.076408,0.212615],[-0.805479,-9.149285,-1.900989,9.872517,-3.062840],[-9.553382,6.012729,-1.665740,-6.416874,-1.750458],[1.039921,-1.502143,0.098666,2.072709,7.776754]],[[-2.870201,6.701086,-0.440613,9.732933,2.621735],[-1.587008,4.498006,8.212422,1.255915,-3.822651],[-3.700716,3.744562,8.721537,-2.768540,-7.804824],[2.307956,-7.360380,7.752202,8.822696,-7.696384],[-5.858954,-7.538083,3.897589,-5.269814,2.056710],[-8.895323,-1.636349,-8.401092,-9.613265,-9.763006],[-8.859748,5.168532,4.978012,-3.891343,7.757287],[9.079788,8.275848,-3.543127,7.938141,4.378436],[5.505907,-1.591780,2.792475,1.637603,6.298296],[9.159080,4.952105,-6.068670,7.909466,1.471628],[-2.287776,6.091169,-2.106347,-0.579965,-9.562809],[-4.270044,2.424588,3.708776,-3.416545,8.333011],[-8.022606,9.193700,6.982117,-4.156411,-0.044721],[-2.992766,-1.390088,5.031286,2.995813,-8.273678]],[[1.433259,4.004404,5.173693,-7.785600,3.147886],[-6.010307,-4.313535,8.646119,3.807999,-0.724426],[-4.475862,-4.721847,-6.871658,7.433297,3.177983],[4.750207,7.575577,-4.873222,1.321786,-7.630350],[-1.501958,8.069931,-4.981293,-7.412506,-6.108109],[-5.698116,1.177500,-5.370523,-6.379509,5.211641],[8.363409,-1.027454,5.375138,-1.097197,5.219337],[0.652199,4.541394,-5.889969,-0.013248,1.014275],[-9.729417,4.988521,7.204281,1.117340,3.117828],[7.767851,-9.476902,8.805567,-6.759929,-7.869627],[-3.491945,9.870586,-8.890435,-4.055174,1.324085],[-7.767453,6.642074,1.852580,9.380222,-1.882701],[-0.609619,0.057818,9.785354,-8.928493,-6.956580],[-6.572572,0.288144,-6.617000,3.209835,-7.798583]]], dtype = "float64")#candidate|7574|(6, 14, 5)|const|float64
bop_7575 = relay.floor_mod(var_7573.astype('float64'), const_7574.astype('float64')) # shape=(6, 14, 5)
output = bop_7575
output2 = bop_7575
func_7590 = relay.Function([var_7573,], output)
mod['func_7590'] = func_7590
mod = relay.transform.InferType()(mod)
mutated_mod['func_7590'] = func_7590
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7591 = relay.var("var_7591", dtype = "float64", shape = (6, 14, 1))#candidate|7591|(6, 14, 1)|var|float64
func_7590_call = mutated_mod.get_global_var('func_7590')
call_7592 = func_7590_call(var_7591)
output = call_7592
func_7593 = relay.Function([var_7591], output)
mutated_mod['func_7593'] = func_7593
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7616 = relay.var("var_7616", dtype = "float64", shape = (14, 15, 1))#candidate|7616|(14, 15, 1)|var|float64
uop_7617 = relay.atanh(var_7616.astype('float64')) # shape=(14, 15, 1)
func_6800_call = mod.get_global_var('func_6800')
func_6804_call = mutated_mod.get_global_var('func_6804')
const_7633 = relay.const([True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True], dtype = "bool")#candidate|7633|(528,)|const|bool
var_7634 = relay.var("var_7634", dtype = "int16", shape = (1, 1404))#candidate|7634|(1, 1404)|var|int16
call_7632 = relay.TupleGetItem(func_6800_call(relay.reshape(const_7633.astype('bool'), [12, 4, 11]), relay.reshape(const_7633.astype('bool'), [12, 4, 11]), relay.reshape(var_7634.astype('int16'), [1404,]), ), 0)
call_7635 = relay.TupleGetItem(func_6804_call(relay.reshape(const_7633.astype('bool'), [12, 4, 11]), relay.reshape(const_7633.astype('bool'), [12, 4, 11]), relay.reshape(var_7634.astype('int16'), [1404,]), ), 0)
bop_7636 = relay.left_shift(uop_7617.astype('int16'), const_7633.astype('int16')) # shape=(14, 15, 528)
output = relay.Tuple([call_7632,var_7634,bop_7636,])
output2 = relay.Tuple([call_7635,var_7634,bop_7636,])
func_7645 = relay.Function([var_7616,var_7634,], output)
mod['func_7645'] = func_7645
mod = relay.transform.InferType()(mod)
mutated_mod['func_7645'] = func_7645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7645_call = mutated_mod.get_global_var('func_7645')
var_7647 = relay.var("var_7647", dtype = "float64", shape = (14, 15, 1))#candidate|7647|(14, 15, 1)|var|float64
var_7648 = relay.var("var_7648", dtype = "int16", shape = (1, 1404))#candidate|7648|(1, 1404)|var|int16
call_7646 = func_7645_call(var_7647,var_7648,)
output = call_7646
func_7649 = relay.Function([var_7647,var_7648,], output)
mutated_mod['func_7649'] = func_7649
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8088 = relay.var("var_8088", dtype = "int64", shape = (3, 1, 14))#candidate|8088|(3, 1, 14)|var|int64
var_8089 = relay.var("var_8089", dtype = "int64", shape = (3, 13, 14))#candidate|8089|(3, 13, 14)|var|int64
bop_8090 = relay.bitwise_or(var_8088.astype('int64'), var_8089.astype('int64')) # shape=(3, 13, 14)
func_7590_call = mod.get_global_var('func_7590')
func_7593_call = mutated_mod.get_global_var('func_7593')
const_8094 = relay.const([[-9.026603,-4.095051,-7.880216,0.513319,0.874860,-2.643892,-5.616218,8.693861,-5.309876,-5.396303,-6.967840,-9.857688,-9.992367,-1.850786,8.643072,-8.546468,-5.661491,4.996301,8.278462,-4.850624,9.993928,-1.708616,7.249380,3.893711,-2.450380,-4.442066,6.024785,9.327317],[-3.688354,-8.445439,4.423431,0.627828,7.986185,-3.090471,-4.542514,-3.303960,-2.021623,2.136154,-0.426471,7.624156,-7.964941,-2.004935,-1.075342,8.566080,3.256189,-7.596934,-6.137849,-8.593486,-2.769400,-0.355402,-9.603860,-8.044765,-2.431227,-6.455075,2.395248,1.503891],[5.840849,9.940135,7.085628,-6.316362,-5.174656,-0.281973,2.365143,1.728284,2.844758,-4.691924,-2.628444,-1.768719,-7.502110,0.762294,3.695540,7.315543,-2.398998,-5.786761,-6.567159,0.923916,-9.932559,5.670294,-3.167968,3.780902,8.895590,7.141559,9.641188,-5.929048]], dtype = "float64")#candidate|8094|(3, 28)|const|float64
call_8093 = func_7590_call(relay.reshape(const_8094.astype('float64'), [6, 14, 1]))
call_8095 = func_7590_call(relay.reshape(const_8094.astype('float64'), [6, 14, 1]))
output = relay.Tuple([bop_8090,call_8093,const_8094,])
output2 = relay.Tuple([bop_8090,call_8095,const_8094,])
func_8102 = relay.Function([var_8088,var_8089,], output)
mod['func_8102'] = func_8102
mod = relay.transform.InferType()(mod)
var_8103 = relay.var("var_8103", dtype = "int64", shape = (3, 1, 14))#candidate|8103|(3, 1, 14)|var|int64
var_8104 = relay.var("var_8104", dtype = "int64", shape = (3, 13, 14))#candidate|8104|(3, 13, 14)|var|int64
output = func_8102(var_8103,var_8104,)
func_8105 = relay.Function([var_8103,var_8104,], output)
mutated_mod['func_8105'] = func_8105
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8122 = relay.var("var_8122", dtype = "float32", shape = (13, 9, 11))#candidate|8122|(13, 9, 11)|var|float32
uop_8123 = relay.cos(var_8122.astype('float32')) # shape=(13, 9, 11)
output = relay.Tuple([uop_8123,])
output2 = relay.Tuple([uop_8123,])
func_8126 = relay.Function([var_8122,], output)
mod['func_8126'] = func_8126
mod = relay.transform.InferType()(mod)
mutated_mod['func_8126'] = func_8126
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8127 = relay.var("var_8127", dtype = "float32", shape = (13, 9, 11))#candidate|8127|(13, 9, 11)|var|float32
func_8126_call = mutated_mod.get_global_var('func_8126')
call_8128 = func_8126_call(var_8127)
output = call_8128
func_8129 = relay.Function([var_8127], output)
mutated_mod['func_8129'] = func_8129
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8156 = relay.var("var_8156", dtype = "uint32", shape = (13, 13, 15))#candidate|8156|(13, 13, 15)|var|uint32
const_8157 = relay.const([[[-5,-8,2,6,-7,-4,-5,-5,-1,6,-4,8,6,-7,8],[-3,-4,9,2,2,8,-2,-10,-4,6,6,-2,-7,-2,3],[2,6,5,-3,-1,-8,-2,-1,-1,-3,4,-1,6,7,10],[2,4,-9,-3,7,7,4,8,-2,-8,-8,-4,1,4,-10],[5,-8,1,-7,-10,-10,-10,8,8,8,5,-8,-2,-1,-6],[1,-4,-10,6,9,2,7,-4,1,-9,7,5,-4,-4,-3],[9,-2,5,-10,-1,-9,10,8,-4,-3,-10,-6,-8,1,-7],[-4,8,-9,-10,-4,-8,6,2,10,-5,-7,-5,-9,5,-7],[-4,-7,7,-5,-5,-9,-3,-10,1,1,7,10,-2,5,8],[-8,-2,-5,2,-5,-9,9,9,7,1,5,-5,-10,-5,2],[8,6,-6,-9,10,-5,-8,3,4,-9,-7,3,-3,-8,-9],[-4,2,-6,-2,7,9,-1,4,8,5,7,6,-3,-2,-9],[-5,7,-2,6,-8,-6,-2,-3,2,-8,-1,-8,-4,3,-5]],[[-8,-5,8,8,1,-6,2,-7,-6,-6,-5,-1,3,-5,-3],[9,1,-6,3,-2,1,-3,-5,8,9,-8,-1,9,-4,10],[-7,9,-5,4,1,4,3,5,-8,-9,-6,-3,-8,3,-9],[9,4,-3,-5,8,-4,-7,10,4,4,-6,2,7,4,-4],[-5,-8,-3,1,-9,-5,9,-9,-4,8,-8,-8,4,2,7],[2,1,2,-2,-3,10,-3,7,-10,6,-9,-2,5,-2,5],[-3,1,8,9,6,10,-7,7,-8,-7,6,-7,4,-6,8],[-8,-8,-8,-2,-6,-6,-4,-1,9,9,4,-3,-6,4,5],[-3,7,-2,10,10,4,-2,3,1,-5,-9,8,9,-10,5],[-6,-8,2,6,8,5,5,2,3,9,8,6,-1,9,9],[-7,-2,8,7,-3,-1,8,-8,-6,-6,8,5,7,10,-7],[1,5,-1,7,-6,-4,1,-5,-10,1,-7,9,6,10,-3],[-6,-1,8,-2,1,-7,7,4,-8,-4,-2,1,-5,-7,-2]],[[1,5,-7,-7,7,-8,-10,-2,-8,1,-3,-5,2,9,6],[-2,-9,3,9,6,-6,10,-9,2,-7,9,4,2,3,-7],[-5,8,-5,2,8,2,10,2,6,-5,7,-3,-8,-10,8],[-2,6,9,-8,7,-8,-2,1,-8,-9,2,-8,10,-1,9],[-6,4,-8,5,-5,3,-1,2,10,1,-6,9,7,2,-8],[9,9,-7,-8,4,-5,9,-6,8,-2,7,-1,1,-6,7],[-3,9,10,10,8,-3,5,-9,-2,6,5,1,-2,7,7],[-1,2,2,-5,4,-8,-8,-9,-1,3,7,3,-7,2,2],[-2,8,2,-8,2,-4,-8,-3,-9,-10,-4,-4,4,-1,-7],[-4,7,-5,-3,7,6,6,-4,-3,-1,-7,9,-1,5,9],[-6,-3,8,1,-10,5,-10,1,7,-6,6,-5,-7,10,-2],[-3,6,1,-1,-3,1,-8,8,6,3,6,-7,6,1,3],[-9,-10,-10,6,5,4,-9,8,2,-5,-8,-4,-3,-9,8]],[[-6,8,-9,10,4,7,1,10,3,3,-7,-8,4,-1,6],[4,-4,1,-5,-1,6,6,-3,-5,8,-4,-9,-4,-4,7],[-4,-3,7,4,-6,-8,-4,-8,-1,-3,2,-4,8,5,4],[-3,5,9,-3,-2,9,-9,-4,-9,-1,4,10,4,7,-1],[1,9,3,8,10,-2,9,1,-10,10,5,-5,-3,2,-2],[9,8,-1,-4,6,8,5,3,3,-8,-7,9,7,-2,-10],[-3,-10,-6,3,-8,8,-9,5,8,-7,1,1,-5,1,-7],[-2,9,1,-2,9,-3,8,-9,6,-1,6,-5,3,3,-7],[-5,1,2,-1,-4,6,9,-1,-9,6,8,-3,8,2,7],[2,-10,-8,-4,-7,-1,-6,-9,7,-4,9,4,6,7,3],[-7,8,9,10,-4,2,1,8,-6,1,9,-3,-1,4,7],[2,4,3,-5,-7,-3,-8,6,6,2,-2,-7,-3,4,-6],[5,-6,9,4,-6,5,-7,-4,1,-5,-7,-2,-1,-3,-2]],[[-5,7,10,5,-10,-3,8,9,5,4,-3,-8,-7,9,4],[-9,10,2,-3,-2,-8,9,-6,-10,10,-2,4,7,-9,-3],[8,3,9,-8,2,5,-6,6,7,-3,-9,-10,-5,6,3],[-6,-9,-9,-6,-3,6,8,4,-3,1,8,1,3,-4,9],[-6,8,-5,6,-5,-2,6,-4,6,-3,-5,7,10,-3,10],[-4,8,4,3,9,-10,1,-10,8,2,3,4,-3,-1,-1],[-10,-7,-8,-4,-2,9,3,-8,4,-9,1,4,-3,2,-5],[6,7,-4,4,-8,-2,-8,6,5,6,-8,7,4,1,5],[8,-3,-5,-2,8,5,8,2,3,-5,3,-8,7,10,6],[6,-7,1,-10,10,4,6,1,7,7,-5,-7,-3,-2,2],[10,-4,-9,-6,-7,-6,2,-4,-2,-10,-2,3,7,4,9],[-9,-6,-6,9,5,-8,8,3,-6,-2,-5,-1,-6,4,-8],[-5,-4,4,-7,1,1,-3,3,3,-10,-6,-1,-5,5,-8]],[[2,2,4,5,-6,-3,8,-6,-1,-10,5,-8,-5,3,2],[-3,-5,-2,8,2,4,1,-9,-4,-7,1,-2,-8,4,5],[5,2,-10,10,-2,1,6,-9,-10,-5,-7,1,-7,-4,-4],[-7,-6,10,-3,-5,-3,-2,-8,-5,-4,-9,9,10,-3,-5],[3,6,10,7,-4,-8,-9,-7,-1,-9,-3,6,10,-7,10],[10,5,5,9,1,-6,-4,9,-4,-2,-7,-3,8,-1,-8],[7,6,-3,-7,5,-10,7,8,3,-10,6,3,-2,-5,-4],[-4,3,2,1,10,7,10,4,-2,1,4,-9,9,10,4],[8,-4,6,-9,-7,-6,7,-2,4,-7,-8,-2,-2,8,-6],[-5,-8,7,6,4,5,2,6,2,-8,4,-4,2,-9,5],[3,-2,-10,9,-7,1,-3,-3,-5,-10,5,-10,2,4,-2],[-9,-10,8,-3,6,-9,1,8,-2,10,7,-8,6,-8,-5],[1,7,-6,3,-1,-9,-6,2,-8,-8,-8,6,3,-10,-2]],[[3,-7,-7,7,-4,7,-9,-8,8,9,4,4,-5,-10,9],[-8,-5,5,1,2,-10,-1,-3,-2,-2,-8,8,4,8,-8],[8,-3,2,7,-10,9,9,1,-6,2,1,6,-3,-5,-6],[9,-9,-7,10,6,-2,-2,-6,2,3,4,5,5,10,-8],[-3,10,-9,6,-10,1,-9,2,3,9,-7,4,-1,-9,-1],[7,4,-7,-4,-4,5,-8,-8,2,-4,1,-4,-3,-6,-7],[-9,-2,-4,8,1,-4,-7,3,-3,-1,7,-10,7,-9,-8],[-9,-3,-10,9,6,-9,-8,-3,4,-5,-2,-6,-5,-8,7],[3,2,8,-4,9,-7,-8,-5,-6,-6,-3,-5,-1,-4,-7],[4,1,-5,-8,-6,-6,-5,9,-5,8,-6,-2,-2,3,1],[-8,-9,2,8,10,-7,8,-3,2,10,3,-3,-10,5,2],[3,-4,-1,-6,-6,-2,7,7,-4,9,-10,-3,5,-7,-9],[10,-1,6,-1,-10,3,10,-1,-9,7,-3,2,10,-1,10]],[[8,-2,6,-10,2,-4,3,2,-2,-10,-1,-5,-1,10,4],[2,4,10,5,7,-3,2,-6,9,-7,6,-2,-1,-6,4],[3,-1,-3,-6,-4,-4,3,-10,-10,4,7,-5,1,-9,9],[8,-1,-8,1,-1,-7,1,-2,-9,-9,10,-5,5,5,4],[9,-5,-2,-7,8,-7,4,7,8,-8,10,-4,-7,4,3],[5,1,-4,-4,5,10,9,9,-10,3,-7,8,-10,10,-8],[-4,-5,-2,8,-2,7,5,6,1,3,5,-9,-1,9,-4],[4,-9,-5,-10,6,7,3,-1,-6,-6,8,-8,4,5,1],[-10,9,6,10,-8,9,2,-5,-3,-5,1,8,-2,9,6],[9,4,5,2,5,2,5,-8,-4,3,-9,7,-4,-2,6],[-2,3,-1,-6,-4,4,7,-7,-4,-5,4,-3,-3,-8,9],[-10,7,9,-4,4,9,1,1,-10,-10,-2,-9,5,-2,-7],[-7,4,-2,5,-1,3,8,4,3,2,9,10,-9,-1,8]],[[-3,-7,-10,-1,7,3,-10,4,-8,-9,10,6,-7,-5,-5],[-8,-7,-7,-8,-1,8,4,2,-3,-5,-3,-10,7,4,-8],[4,-9,-3,-7,3,-3,-1,-1,7,5,8,-8,-5,-8,6],[7,-9,10,-3,2,-6,-8,-4,-2,-5,-2,5,3,-7,-8],[-4,5,-3,7,4,1,4,9,-10,-8,9,10,-4,-3,-4],[5,8,-3,-5,-7,2,10,-7,4,9,-2,4,2,7,-8],[-8,10,3,9,6,8,3,-3,-5,8,1,-4,-4,-2,4],[1,-4,-10,-4,6,4,-9,-10,-5,-1,2,-5,-6,5,-9],[1,4,10,-2,-4,8,2,3,2,-8,-3,5,-7,6,-3],[4,4,9,4,2,-10,4,-8,4,6,-2,-2,-6,10,-4],[6,4,8,8,5,-9,-10,6,3,9,4,8,-8,5,-8],[-8,-7,-8,6,-8,-6,5,-2,-8,-3,-4,-6,-2,-9,-2],[-6,-1,3,-9,-5,-9,3,-1,-6,-2,3,7,8,-6,6]],[[2,-6,-8,-2,7,3,-10,-9,3,-9,-4,9,-6,3,-4],[9,3,-10,-6,8,-2,9,-9,-3,4,5,6,1,3,-3],[-5,2,10,10,4,1,-9,8,-9,-10,4,-10,3,2,5],[2,10,7,8,7,-5,10,9,4,10,10,9,-6,-1,-8],[-6,8,8,7,5,10,2,-6,7,-10,3,-2,-8,-7,-7],[-7,9,8,-3,3,-10,-7,-2,-5,10,7,3,-8,-6,-2],[-9,-5,-6,-4,-9,-6,2,1,-4,-5,10,-10,1,-6,10],[-9,8,-7,-8,-5,10,4,-3,-9,1,-5,-8,-6,10,6],[-1,-1,1,-5,-1,-4,2,-4,-4,3,-7,-6,3,3,-3],[5,4,-3,4,-3,-10,7,-8,-6,3,8,8,-6,8,-4],[8,5,5,-8,7,5,10,-7,2,1,-3,-7,4,3,5],[-3,9,7,-5,5,6,-7,-4,5,8,-3,-6,5,6,-4],[-5,1,4,-8,-3,-2,4,5,4,4,-9,-4,-7,-9,-6]],[[3,-9,-3,-2,-5,-3,6,-6,5,-5,3,-6,-9,5,8],[-10,-3,7,3,7,6,4,-9,-3,10,5,-1,10,8,7],[-9,8,5,9,5,-7,10,-3,4,5,-5,7,5,-6,-5],[8,-10,-7,2,-7,4,7,7,-2,7,5,10,-8,1,8],[8,1,4,5,4,2,7,-1,-1,-7,2,10,6,-7,-3],[3,10,-9,2,10,-5,-3,2,-7,8,-1,8,2,-3,-10],[-3,8,-7,-8,3,4,-10,2,-2,7,5,-10,-3,-6,5],[-3,-9,2,9,4,9,10,4,5,3,5,2,-2,2,-1],[3,3,-4,9,-8,3,-10,9,9,7,-8,1,-10,6,10],[-6,1,5,6,-7,7,-2,-7,1,4,7,10,1,2,1],[5,4,-7,-9,3,9,-10,-6,-1,2,-5,-7,-8,7,6],[-1,-7,6,6,-9,3,-8,9,9,-3,5,-1,-4,-1,-10],[-1,7,-8,2,-8,2,10,-4,7,9,6,7,4,-6,-6]],[[-3,7,-5,-3,-8,1,-4,-1,-10,-4,8,2,-5,9,-3],[-8,-4,-6,-2,9,10,10,-10,2,1,10,-6,-5,1,2],[10,2,-5,-4,-7,-4,2,-3,-9,4,-1,-7,9,7,9],[7,9,3,10,-8,-10,-6,-10,-5,-3,7,5,2,8,-5],[-1,6,4,2,9,-10,4,-1,4,1,5,5,4,6,-9],[8,-3,-9,-4,-10,-5,-3,-6,-3,-10,-10,-6,7,-4,-1],[3,-4,4,5,8,-4,-6,2,-9,2,3,6,-9,-9,-7],[-8,10,9,7,5,-9,-8,3,-5,-7,4,3,9,-5,6],[1,-2,-6,-6,-5,6,-1,7,4,-8,10,-3,2,-6,-2],[-8,-6,5,-1,3,-3,8,-5,8,8,2,-8,3,-9,-8],[1,6,-6,7,4,-1,-3,9,-5,-9,2,1,8,-9,-10],[2,5,-9,10,8,8,-1,10,10,8,6,-3,-10,-10,-2],[8,-4,-3,-3,8,9,3,-8,-9,-8,-2,-6,3,7,-7]],[[-4,4,-9,10,4,-3,4,10,-1,-2,5,-5,-10,9,2],[8,-10,-3,-3,-10,10,9,-1,6,9,1,4,7,4,1],[1,-1,6,-9,-8,-6,-6,10,4,-1,8,7,8,5,-9],[8,-8,10,-3,-2,1,9,3,-5,7,-1,8,6,3,9],[-10,1,-6,-1,-1,-1,-3,10,-2,-6,-2,6,5,9,-5],[-10,-7,-2,-4,-3,-8,-7,-9,-8,5,1,-10,-9,-9,5],[-7,9,-7,-7,4,6,-8,-2,4,-7,-7,-6,5,4,-6],[-10,-7,6,-7,-7,-7,-2,7,-2,-5,10,9,-1,-3,-10],[7,1,6,7,2,-2,-6,6,8,4,8,7,2,-2,4],[-4,-10,2,4,-7,3,7,-6,5,-10,-1,-5,-6,8,-3],[-7,-3,6,3,9,6,3,-3,6,-5,7,3,-8,-10,-6],[-1,4,2,-1,9,6,4,-1,-10,-5,1,3,-5,-4,9],[9,-5,-6,-4,1,-9,-1,8,-7,8,5,3,5,1,4]]], dtype = "uint32")#candidate|8157|(13, 13, 15)|const|uint32
bop_8158 = relay.greater(var_8156.astype('bool'), relay.reshape(const_8157.astype('bool'), relay.shape_of(var_8156))) # shape=(13, 13, 15)
output = bop_8158
output2 = bop_8158
func_8163 = relay.Function([var_8156,], output)
mod['func_8163'] = func_8163
mod = relay.transform.InferType()(mod)
mutated_mod['func_8163'] = func_8163
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8164 = relay.var("var_8164", dtype = "uint32", shape = (13, 13, 15))#candidate|8164|(13, 13, 15)|var|uint32
func_8163_call = mutated_mod.get_global_var('func_8163')
call_8165 = func_8163_call(var_8164)
output = call_8165
func_8166 = relay.Function([var_8164], output)
mutated_mod['func_8166'] = func_8166
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9893 = relay.var("var_9893", dtype = "float32", shape = (14, 3, 14))#candidate|9893|(14, 3, 14)|var|float32
uop_9894 = relay.atanh(var_9893.astype('float32')) # shape=(14, 3, 14)
func_634_call = mod.get_global_var('func_634')
func_637_call = mutated_mod.get_global_var('func_637')
const_9903 = relay.const([-0.520241,5.767534,-1.781636,0.585506,-8.293184,1.319205,0.445754,-1.801870,-7.386916,5.387966,-4.429052,-1.584946,-1.996530,6.482507,-6.988609,-4.127859,-1.600867,-1.458382,-3.030506,7.321641,5.126949,7.653627,-1.448023,-3.076045,3.217546,-0.337316,8.462420,-9.097727,-4.584495,1.222307,0.180694,-6.167153,-7.832736,-8.236792,-9.352443,0.445466,-3.320188,-5.633516,-3.477161,9.160309,5.344289,-8.632736,-7.291023,-3.607157,-0.202719,-7.092580,2.995863,-2.205293,3.312303,-6.151513,-1.438078,7.139226,1.948176,8.172564,-1.947648,0.036565,-3.225082,-9.908056,7.953214,-2.640547,6.842296,9.620637,4.944081,-9.503013,-3.100657,-5.802405,-9.965622,-2.482570,-8.192567,2.953079,-6.663093,-2.256381,-7.818211,-1.736116,8.069705,-0.758709,5.931043,-5.842547,0.495346,3.909242,8.150049,-5.197593,8.575635,1.342098,7.723990,-5.704496,-9.167855,-1.837331,-0.499888,-6.315741,7.158868,-0.838261,-4.496495,0.503310,4.262494,1.481388,6.523766,-0.255681,-7.502857,-0.485586,-6.992978,-7.547827,6.263572,-6.455073,4.760871,8.746090,4.840472,9.493805,-4.384807,8.300886,3.718341,3.691973,-0.314800,1.562931,3.069611,-9.961428,-6.711782,-8.692975,-5.367302,6.192167,5.729720,-0.724896,-7.944697,-7.429129,0.743896,-5.651723,8.983843,5.682118,2.973925,-3.742508,-9.802728,8.791364,5.297277,-1.653864,-2.591309,9.282766,-6.977262,-3.248217,6.929631,-0.461680,-2.800438,5.294028,-7.939607,6.579183,4.023117,-1.149823,3.150146,0.974622,-6.559043,-3.258541,1.910458,-1.949764,0.448222,3.453875,-4.496912,3.883521,-3.661323,-3.038428,8.391410,7.873327,7.663266,-9.493426,8.514556,-7.976928,6.838219,-1.550134,-1.997863,2.192639,1.462460,2.225932,-6.095177,-2.907120,5.451593,2.907212,-2.129187,-9.929366,-7.934506,-6.940141,-1.159812,9.578710,0.710457,-7.698003,3.886907,-9.543240,-2.396100,-3.720609,-7.810540,-5.449058,9.056508,3.623070,-5.443566,3.174103,-6.124566,-6.535246,-4.800048,2.171244,5.340180,-0.207824,7.457567,1.487191,-5.748044,-9.994225,-7.053126,-5.950796,-0.978871,7.458556,4.053830,4.776834,0.082042,-6.879714,-0.016068,8.547773,-3.502477,-1.050155,-9.822407,5.359763,0.911556,-3.628716,-9.347456,5.864327], dtype = "float32")#candidate|9903|(220,)|const|float32
call_9902 = relay.TupleGetItem(func_634_call(relay.reshape(const_9903.astype('float32'), [10, 11, 2]), relay.reshape(const_9903.astype('float32'), [10, 11, 2]), ), 0)
call_9904 = relay.TupleGetItem(func_637_call(relay.reshape(const_9903.astype('float32'), [10, 11, 2]), relay.reshape(const_9903.astype('float32'), [10, 11, 2]), ), 0)
output = relay.Tuple([uop_9894,call_9902,const_9903,])
output2 = relay.Tuple([uop_9894,call_9904,const_9903,])
func_9929 = relay.Function([var_9893,], output)
mod['func_9929'] = func_9929
mod = relay.transform.InferType()(mod)
mutated_mod['func_9929'] = func_9929
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9930 = relay.var("var_9930", dtype = "float32", shape = (14, 3, 14))#candidate|9930|(14, 3, 14)|var|float32
func_9929_call = mutated_mod.get_global_var('func_9929')
call_9931 = func_9929_call(var_9930)
output = call_9931
func_9932 = relay.Function([var_9930], output)
mutated_mod['func_9932'] = func_9932
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10218 = relay.var("var_10218", dtype = "float32", shape = (4, 7, 1))#candidate|10218|(4, 7, 1)|var|float32
uop_10219 = relay.log10(var_10218.astype('float32')) # shape=(4, 7, 1)
uop_10229 = relay.exp(uop_10219.astype('float64')) # shape=(4, 7, 1)
output = uop_10229
output2 = uop_10229
func_10246 = relay.Function([var_10218,], output)
mod['func_10246'] = func_10246
mod = relay.transform.InferType()(mod)
var_10247 = relay.var("var_10247", dtype = "float32", shape = (4, 7, 1))#candidate|10247|(4, 7, 1)|var|float32
output = func_10246(var_10247)
func_10248 = relay.Function([var_10247], output)
mutated_mod['func_10248'] = func_10248
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10537 = relay.var("var_10537", dtype = "int64", shape = (6, 6, 10))#candidate|10537|(6, 6, 10)|var|int64
var_10538 = relay.var("var_10538", dtype = "int64", shape = (6, 6, 10))#candidate|10538|(6, 6, 10)|var|int64
bop_10539 = relay.less_equal(var_10537.astype('bool'), relay.reshape(var_10538.astype('bool'), relay.shape_of(var_10537))) # shape=(6, 6, 10)
func_2219_call = mod.get_global_var('func_2219')
func_2222_call = mutated_mod.get_global_var('func_2222')
const_10561 = relay.const([-7,-2,8,10,-2,5,7,-3,7,7,6,-4,6,10,-1,-9,-1,-5,-2,6,-5,10,-2,4,10,3,-1,-1,-10,2,-5,-4,-3,-5,3,-1,-2,-10,-3,-6,-8,-9,5,-7,-2,-8,9,5,-10,8,-2,4,9,10,10,7,4,-6,-9,-4,1,9,-6,3,5,-1,-2,2,-9,-7,8,-5,-1,3,-4,-10,1,-9,2,-2,5,3,-8,-3,7,6,-4,-2,-3,-5,-2,-4,-2,9,-6,10,-6,-1,8,-3,-3,-4,1,-2,-9,-1,-1,3,9,9,4,-7,4,7,1,9,-9,1,-9,4,3,2,-10,9,-8,5,10,2,-7,6,-9,3,9,7,10,-9,-7,-7,7,-8,-6,7,-2,-8,8,-8,10,-6,-7,1,4,-8,-1,10,1,-3,9,-3,-8,2,6,4,1,-6,-5,-6,5,10,9,5,7,8,-7,9,-1,-3,10,10,-9,10,3,3,-9,5,-4,-9,8,9,8,1,8,6,-3,-9,-3,6,-4,6,-3,-5,-3,10,-4,7,8,1,3,-3,-4,-9,-1,4,6,-1,1,8,10,5,8,6,-1,-1,4,1,4,4,-6,3,6,-3,-9,1,10,5,-8,-3,8,3,7,8,3,7,2,-3,3,7,8,5,-4,7,1,-2,3,-1,-7,-2,-2,-2,-10,-3,1,-6,10,9,2,-7,-6,-4,-4,1,-5,-4,5,-1,10,-7,6,2,-7,-9,8,3,-6,-7,1,4,3,3,5,-3,10,6,3,3,2,8,1,-6,-8,9,-2,-3,2,-5,2,2,7,-1,7,-10,-7,10,10,4,2,-7,-6,-1,8,7,-3,-3,6,-1,-7,3,1,-1,3,1,9,-8,-8,-5,-5,8,1,10,-3,-2,4,-6,1,6,-3,7,-4,-8,6,-1,-8,-10,-10,6,-1,-6,4,-10,9,8,6,3,2,4,-7,-10,-6,3,1,9,-8,9,-7,8,8,8,-3,3,4,-3,4,7,-6,-6,-10,10,-2,-1,-1,-6,2,4,7,-1,9,-4,-9,-5,-3,-1,5,-2,-4,7,9,6,-7,9,10,-5,-5,-1,1,-9,-4,7,4,8,2,1,9,5,8,8,-3,4,-1,2,9,-6,2,6,-5,-1,-10,-8,-2,2,6,-7,-2,-7,-7,5,-10,3,-6,-7,-3,-6,5,-1,9,-8,-5,6,-9,2,-3,4,-10,7,-5,-5,-7,1,-8,-8,8,-4,4,-10,-6,-8,1,-2,8,7,6,-2,-4,4,5,-1,-1,-6,6,5,-8,8,-7,-2,-4,10,2,4,5,10,-1,5,-3,-4,-6,-10,3,6,10,5,-7,-5,-7,5,-6,-3,3,8,8,-6,2,9,-3,7,2,-9,-9,8,-5,7,7,8,-8,7,-8,-10,-8,-8,-3,6,9,4,4,-1,6,-8,-1,-2,-3,-5,-1,-5,-6,-2,8,-6,-7,-4,-4,-8,4,-1,4,-4,-4,2,-7,-6,10,2,8,-4,8,-6,2,3,1,2,9,2,8,1,-1,-8,5,-8,8,7,-9,-8,-6,10,7,3,-10,9,1,3,7,2,9,-4,-1,3,-6,2,2,-1,5,-4,9,3,5,1,-5,-3,-10,-1,2,2,7,-1,-7,9,-4,-5,8,2,-3,-5,-3,-3,7,-5,-10,-6,2,-5,10,9,6,-7,-3,10,-2,-2,-5,-2,-1,-1,6,7,7,-5,7,-10,-1,9,-8,9,6,-6,8,-3,-7,-1,6,-8,-3,9,-10,-5,8,4,3,-7,-5,-9,-1,4,-9,-10,7,7,3,-10,-4,2,8,-9,9,9,-9,7,-3,9,-7,6,-4,-4,6,8,8,6,-7,-7,1,8,-8,-1,9,-10,6,2,8,9,-9,-8,8,-5,8,-1,1,8,-6,8,-8,4,6,-6,-2,-8,1,-10,-9,3,-6,-6,-6,4,-5,9,-3,-7,-7,-3,5,9,-9,-4,3,-6,4,6,6,1,-4,-3,3,10,-3,10,6,6,10,4,1,-2,9,4,10,7,8,-5,-1,5,-5,4,6,-7,-1,-10,10,-7,10,6,-9,-3,4,9,2,3,-1,-1,8,3,-8,4,-3,-6,-2,-2,-5,9,-5,-9,4,-4,-9,-10,-2,8,6,-9,1,-1,-10,-6,-9,8,-3,1,-7,2,10,4,-7,-4,-2,-1,2,8,4,-1,-8,7,6,-1,-2,10,5,4,4,-2,-2,-1,-4,8,-4,-2,-8,6,-8,-6,9,10,9,5,-3,10,-9,-10,10,4,-7,-8,7,8,10,4,9,3,-10,-1,-5,-6,2,1,6,-5,2,-7,-7,4,10,-9,2,6,10,4,-8,4,-8,1,-2,6,-10,-3,-9,-6,-5,-7,7,-10,1,-4,4,-7,5,-6,-6,1,7,-3,-10,-3,-4,-3,-4,-7,5,-3,1,1,10,1,10,-2,-7,-3,-3,-2,-9,-7,-8,-7,6,-1,-2,3,2,7,-7,10,3,-10,2,-7,-7,-5,9,-7,3,-3,2,8,1,7,4,3,3,-8,-5,7,9,8,-3,4,7,-3,-5,-3,4,-6,9,8,3,6,-2,4,4,-9,1,3,3,4,-6,-4,-1,1,-10,-2,8,2,3,-9,-10,-4,-4,-6,4,2,-1,10,-9,-1,-1,-3,-3,7,1,-10,6,1,-2,6,-8,-4,7,10,7,4,-4,-7,1,10,-3,6,-4,-9,5,2,4,-2,-2,-8,4,8,-8,-3,-2,5,-5,3,8,-6,7,-8,-6,3,-5,-8,2,6,-3,-3,4,-8,-8,10,5,1,-6,5,1,9,-9,-6,-2,-1,3,-8,1,-8,7,5,4,5,6,9,6,-5,4,5,4,-9,-1,6,4,-3,1,-4,5,-4,-7,-10,2,9,-5,-2,-4,5,-1,-1,4,6,1,10,-9,-9,-9,1,-2,-7,-9,-7,-3,2,5,9,-7,-5,-6,6,-1,-4,-4,2,-9,7,2,-3,-6,1,8,1,6,4,2,7,-7,-6,8,-10,-8,3,1,-7,2,-8,-7,-6,6,-4,1,6,2,10,-9,-5,5,7,7,-3,-9,9,-2,8,6,10,3,7,5,5,8,-1,9,1,1,5,8,7,-1,-10,4,6,6,-3,3,-5,10,-7,5,5,3,5,5,1,-6,3,-3,-9,4,-9,10,9,-9,8,-4,9,4,9,7,-5,3,5,7,-4,-6,8,-5,5,-1,10,-8,3,7,3,-3,7,6,-1,-3,-4,6,-4,-8,8,4,7,9,5,-1,9,9,-10,-7,-8,6,9,5,-2,4,4,-10,-9,-10,-4,-5,5,-9,8,5,-6,9,2,1,-9,-6,3,6,4,6,-9,10,-4,-8,-7,-2,6,10,-7,4,6,-1,-5,-10,-2,-6,1,4,7,10,7,-6,-3,-10,7,-8,-3,3,5,6,2,-8,-10,-10,4,-10,2,-5,4,7,1,-4,6,4,-1,-9,-2,7,9,8,7,-6,8,6,-9,1,10,-4,-3,8,-7,-10,-5,-3,-6,10,1,-4,7,10,5,-4,9,3,-6,-9,-1,-6,-7,1,-9,9,-6,8,-5,7,-2,-6,1,-4,-4,2,1,2,-6,-1,3,-5,-3,2,3,-9,-4,-5,-6,-4,9,4,5,-10,-8,-3,3,1,1,5,5,-9,6,-4,3,3,-5,4,10,8,-4,-10,-1,2,-4,-7,10], dtype = "int16")#candidate|10561|(1404,)|const|int16
call_10560 = func_2219_call(relay.reshape(const_10561.astype('int16'), [12, 13, 9]))
call_10562 = func_2219_call(relay.reshape(const_10561.astype('int16'), [12, 13, 9]))
func_8163_call = mod.get_global_var('func_8163')
func_8166_call = mutated_mod.get_global_var('func_8166')
const_10580 = relay.const([-1,1,2,-7,9,-4,-10,7,9,4,6,7,5,-7,-10,10,-7,-5,2,-5,-7,-7,2,-8,3,-9,9,9,5,-6,6,-6,-8,2,-2,-2,-6,8,1,10,-8,-5,2,-3,-1,10,7,-10,9,-5,-1,-10,6,-6,5,-2,-5,-10,-2,6,9,1,-3,1,7,3,-4,8,2,-8,-1,8,9,7,-10,-5,10,-7,8,-5,3,-4,10,7,-7,-8,7,-6,-5,-8,-5,-6,-10,8,-8,-7,-10,9,5,1,-3,10,-9,6,9,-1,-8,7,-7,-10,-7,-9,7,6,-6,-4,10,-10,-10,4,-10,-2,-3,8,6,-6,-4,10,5,-3,-5,-3,-1,-5,-9,10,6,-2,3,-9,-8,1,-2,-5,-9,9,7,10,-4,1,-3,-7,-5,8,-8,6,-5,-10,-2,-5,3,-6,7,10,-10,-7,4,-4,10,6,10,-6,10,2,-8,2,1,6,1,-1,9,-4,1,-1,-9,-1,-8,3,-2,10,10,-3,-8,-10,5,2,9,-6,-3,1,5,-2,-10,10,10,2,-10,2,4,-8,3,-4,5,3,8,-1,-8,5,-8,8,5,-7,-4,4,2,8,10,-10,-1,-5,6,1,1,-4,1,8,-3,-2,5,-7,-5,-4,7,10,-6,-9,2,-8,8,-1,-5,6,3,5,1,7,-6,-1,-5,-3,9,-5,1,-2,-7,-7,-2,-10,-8,-3,8,-5,10,-9,10,-8,-1,-9,-8,1,-4,10,9,8,-7,-8,-10,-1,-2,7,-2,2,8,8,-2,5,-5,-9,7,4,2,-10,7,-3,2,1,-5,-9,-4,-2,4,-2,2,-5,-1,-10,-3,5,2,10,-10,-9,-6,1,-5,-6,-10,-10,-10,-9,6,-5,-2,2,10,9,5,-8,-4,10,-2,8,5,-4,5,-7,3,-1,-4,-8,-4,-6,-2,-9,3,-8,8,-9,-6,-9,4,-1,9,3,-6,10,7,9,2,8,7,-2,-5,-7,2,1,5,-7,5,-10,9,1,5,5,-7,-3,-2,9,-6,8,6,7,3,-8,2,-7,7,6,7,-1,6,-9,9,-6,8,-4,-5,-6,3,-7,1,5,-4,-9,-4,-5,4,-1,-4,9,-2,8,4,-6,-9,3,8,7,-10,-1,9,-7,2,10,-4,9,4,3,-5,-8,-1,4,8,1,2,-2,-10,7,-6,9,8,6,-7,-9,-10,-5,-7,-10,4,2,-5,-8,5,6,-4,3,-3,3,10,10,-10,-10,-8,1,4,-10,2,-6,5,10,7,1,-4,9,6,-3,8,1,-8,8,8,2,5,-6,-10,-10,-10,6,-5,8,-8,-6,-6,2,1,-7,7,-10,-7,-3,-5,-3,-5,-8,8,2,9,-10,-6,1,2,10,-7,-2,-7,3,-1,6,7,-6,10,-1,-5,3,3,1,-2,-7,-1,7,-5,1,-7,3,1,-9,9,-1,10,10,-10,1,1,-2,6,-2,10,-8,-8,-2,-2,1,10,-10,6,6,-10,-9,-4,5,2,10,1,-8,-10,-10,-1,6,5,-4,5,-8,-8,7,-7,9,-2,-9,6,1,-8,-10,4,-10,3,9,-5,-4,1,4,-8,7,-3,-10,-6,7,-4,10,-5,8,-6,6,3,4,-5,-3,-3,-2,1,-7,5,-8,1,10,10,-3,-4,-8,3,2,-4,1,-9,6,-7,6,9,2,4,5,9,-2,9,1,-4,9,1,-7,-5,10,-6,-3,-10,4,-8,-10,8,-1,4,10,6,-7,-1,7,7,-7,4,7,-6,10,3,2,-3,-10,-4,4,10,-7,4,-9,1,-6,-8,1,-8,-10,10,-2,-3,-8,1,-9,3,-3,1,-10,10,9,10,3,-8,7,-3,1,-9,4,-2,2,10,2,7,-4,-9,4,1,-5,10,-7,1,10,-8,2,9,5,9,-1,-1,-3,5,10,-7,-7,9,10,3,-1,-6,2,7,5,5,4,10,-8,7,5,5,10,5,5,2,10,1,3,7,5,5,-10,9,4,-8,-9,-8,-8,-9,-2,10,-8,3,-10,1,-4,7,5,-4,1,7,-4,8,-9,-4,7,2,5,-9,6,8,-8,6,10,-4,1,-10,-6,8,5,-6,-3,10,-6,3,-8,-3,-8,2,10,-9,-7,7,-7,-9,-4,7,-7,-7,5,-4,1,-1,-8,-6,-1,9,-4,-1,9,3,7,5,8,-9,-4,-8,-2,-5,-4,-7,6,2,2,2,3,7,7,8,-5,-8,9,3,5,-10,-9,-5,-4,-6,2,8,-3,-7,-6,-4,1,-10,-8,-10,3,5,8,8,8,-8,1,-6,-10,5,-10,-9,-10,1,-5,2,-2,9,-8,-4,8,7,-10,4,-9,-8,-7,-10,-9,9,-2,10,-10,4,6,4,-1,-3,-7,-1,-7,3,-7,3,4,7,-2,7,-6,10,10,5,-7,10,-9,-8,7,10,-6,9,-4,-5,-3,-8,5,2,2,-5,-10,-10,-6,-5,4,9,8,-2,-4,9,-3,-10,-5,-4,-10,3,-5,-8,5,-6,-9,-1,-2,-9,1,-6,5,5,-8,6,-1,9,5,-9,-1,9,9,-6,4,9,-3,2,-3,-9,-7,1,5,-5,9,1,6,-1,2,8,-3,1,-4,-8,-1,5,2,-5,-6,-7,2,-5,8,7,-5,3,-2,6,9,-10,-10,8,3,-9,2,5,4,6,8,-3,8,1,-2,3,-10,2,2,-4,-1,-5,10,1,-2,7,10,-4,-6,8,3,-9,-6,5,-1,2,-1,-9,1,-7,8,-4,4,7,-5,9,-8,-3,1,2,-6,-6,-5,9,4,8,10,2,-10,-5,6,4,-2,8,-4,5,-7,8,5,-6,5,-3,-6,10,-6,2,9,-5,3,-4,4,-7,-10,2,6,4,-2,6,-2,3,-9,9,10,-9,-7,-10,-2,-3,5,6,3,-1,-7,-10,-3,-6,-9,2,-6,4,4,6,2,8,5,9,4,-3,-8,9,-8,-6,9,-8,-9,-10,-8,-10,-6,-10,-2,6,-10,10,-4,9,-3,8,-1,9,-1,-4,3,-9,-2,-9,9,-4,-6,7,3,-1,1,10,-8,-3,-6,-7,-10,-10,-9,-9,-4,-9,7,-2,4,-7,-5,-8,-4,3,1,-10,8,5,7,-8,-7,5,3,-4,-1,3,-8,8,-5,3,-10,-6,1,8,5,10,2,-8,3,3,3,-9,-8,-4,-9,-8,-7,1,-6,-5,4,-5,-3,3,-4,-1,4,-9,-8,-7,9,-7,-2,4,7,10,-7,10,-9,9,1,4,1,-10,-6,7,2,10,2,3,3,3,-2,3,7,-7,-1,6,4,-10,-2,-6,1,-2,1,-2,-1,-6,9,-4,-1,-9,-2,4,-10,6,9,8,-9,-3,-6,-5,-4,-9,2,1,4,8,4,4,4,8,2,-5,6,1,7,-10,9,-3,-3,-6,6,-7,-6,4,10,5,-10,5,2,-10,4,-9,-9,3,9,-3,5,-7,8,1,5,-2,-8,-1,-2,9,-10,8,3,3,3,8,3,-9,9,1,-9,7,1,-10,-6,1,-7,7,-2,-3,6,5,9,2,-7,9,7,3,-3,-3,2,-7,2,-3,4,-1,9,10,1,5,-7,2,-2,2,-10,6,-8,2,-9,-6,1,3,-3,-8,-7,4,9,7,-3,-9,-5,-4,10,-7,-3,1,-10,3,-9,2,8,-9,-2,-8,-7,-7,-4,9,8,-10,-9,-4,7,-4,2,2,10,7,-10,-6,-4,3,-3,-9,-8,-2,3,-6,7,7,-6,7,4,9,-9,-3,7,10,-8,-2,9,1,-2,-2,-9,-6,10,2,-9,8,-5,2,6,-3,-2,-1,9,-3,-3,9,4,6,1,9,-10,-10,7,6,-4,10,-3,7,6,-2,6,8,9,5,-3,-9,-1,-7,-1,-6,3,-2,-8,8,-10,-3,-4,-6,5,2,-8,-1,10,-9,-1,5,-10,10,-8,2,-3,-4,-5,9,-4,10,-9,-10,6,-9,4,-3,-3,-2,3,8,-10,10,-3,-5,-9,-8,5,9,-7,10,-4,-8,6,-7,6,3,-8,-1,-4,-7,-3,-1,-2,2,9,-3,-5,-10,-10,9,2,4,-9,-10,-3,-5,-9,5,-7,1,10,-6,4,5,-3,-2,10,-5,-2,9,-10,-4,-1,2,-7,-3,-6,2,-7,4,3,4,-3,-2,2,4,8,-2,-8,-8,-7,4,1,3,-4,7,4,-3,-10,6,8,3,8,4,10,-1,-4,8,10,3,-2,-3,4,5,-1,-6,-9,-5,-6,2,-3,-1,-9,-10,4,-5,6,3,2,-3,-9,1,10,4,5,2,-1,2,-5,1,8,6,-1,-3,6,-7,-7,-4,2,-4,4,-4,-10,4,-9,-7,-10,2,-1,-6,10,-4,2,3,6,1,-5,6,9,1,7,-6,10,-10,-2,-1,-10,1,-5,-5,4,-2,9,4,-1,10,2,7,-4,6,3,-2,2,-4,10,7,-5,2,-8,4,1,9,9,-7,3,3,-1,-9,-6,10,-2,9,8,1,-6,-7,-8,2,4,-2,-5,3,8,8,6,-2,-7,-8,-10,2,4,5,-8,1,6,-9,10,6,-3,-6,4,-7,-6,-7,4,4,-1,-3,-8,10,-2,5,-10,-2,7,2,-3,-2,6,7,9,1,4,10,10,4,-1,-4,1,-4,1,8,6,4,1,5,7,-1,-8,1,-1,10,7,2,7,4,3,5,-6,-5,-4,-7,4,2,-9,2,9,3,-5,3,3,3,1,-7,-6,-4,-1,-1,-8,-9,-5,6,-2,-9,-4,-10,-10,-2,10,8,2,-8,2,9,2,7,-10,3,-4,10,5,-6,2,7,-7,-8,6,1,-3,10,-10,-5,1,-2,-10,-4,10,-9,-10,-4,3,6,-6,-9,-9,6,-5,-10,9,-3,4,-6,-9,-9,-3,-6,3,-6,-10,7,4,-1,-6,-7,-2,-6,8,-1,6,8,2,-6,5,-3,-6,4,-6,1,3,9,-8,4,-6,5,-6,1,-4,-3,8,-3,8,6,-10,10,-5,-3,-5,-9,1,-2,6,4,-10,-8,-5,-5,-8,-1,-8,-6,-1,3,3,4,7,-2,1,2,5,2,-3,-4,-9,-1,-7,9,-5,1,-6,3,-5,4,-1,9,-8,-5,-9,-2,-6,-5,-10,-3,9,-3,1,8,-1,1,-1,-5,3,-10,10,1,4,1,10,-9,9,6,5,7,-8,-7,1,10,3,6,-3,-1,3,-3,7,-4,3,6,3,6,-2,-10,5,6,-1,3,-1,3,6,9,-7,10,4,-7,-7,-10,-4,-3,2,8,4,-7,4,9,5,5,-2,9,-9,4,-9,-9,5,-3,3,-10,1,-4,-7,-6,4,4,6,-3,-2,-5,1,4,-7,-5,-6,-9,-2,3,9,-2,3,-8,-9,-4,-8,-2,2,-9,10,-9,-8,-5,-5,-2,10,-5,1,-9,-4,3,-3,-3,10,-6,-7,-9,7,-7,-4,5,4,6,3,8,-10,1,6,2,7,6,-5,9,1,-2,-7,-1,-9,6,2,-1,-7,-8,6,10,-10,-7,3,4,-4,-1,5,1,8,-8,-3,5,-9,4,-4,1,3,8,-6,2,-1,10,-6,2,8,6,-6,3,5,3,2,-3,5,-10,6,-2,6,4,3,-8,5,2,3,1,3,-7,-9,1,-4,7,-5,-6,9,5,-8,-2,-4,-6,-2,-7,2,-3,6,7,6,-7,-2,-4,-5,-4,-9,-5,3,-2,-10,-9,2,-7,5,-8,7,4,10,-10,-6,-5,-1,7,-4,8,-5,10,10,-6,1,-7,-9,8,8,2,4,-6,10,8,2,9,4,5,-5,8,4,6,4,-3,-4,6,-4,5,-6,9,-9,-5,8,-7,-2,-10,-8,-10,-2,5,-9,6,-3,-7,-3,9,5,-7,6,7,-6,-4,3,7,8,3,-2,1,9,-6,-4,-6,-1,-3,4,-4,-7,7,4,-9,-7,-10,-1,-6,-8,-3,-9,3,-2,8,-8,-8,-3,-9,8,-1,-10,4,1,2,-4,4,-5,-5,5,5,-6,-10,-8,7,-7,-1,-9,-8,6,-2,4,4,-2,6,-2,3,-4,6,4,-9,10,-9,8,-3,-7,5,-8,-1,-9,10,-10,7,7,-9,5,-3,-10,7,-10,-2,-3,8,-7,-6,10,6,-8,-3,6,-6,-1,-7,-1,-1,-5,6,10,-3,-5,-3,-6,4,-2,1,-10,-1,5,-2,-4,-5,-5,-9,9,4,-3,-10,8,3,2,9,10,-4,10,1,-10,3,9,4,7,3,-7,-9,6,4,-7,-9,5,-1,-9,8,-9,7,-4,8,-9,3,2,10,5,6,-8,-8,8,7,2,-9,6,-2,6,-4,-1,-10,1,10,5,10,1,-6,9,-8,-9,-3,4,-7,-5,5,10,-8,-5,-8,4,-6,10,-4,7,2,-1,-1,10,3,-9,-3,6,-9,-10,3,-9,-7,-1,5,-4,-4,-2,8,-2,-1,-1,-1,4,10,-1,7,2,-6,-4,-2,8,3,-10,-5,-4,-7,-9,-4,2,-8,-8,10,7,-4,-9,-1,-4,-8,-5,-9,7,6,6,-10,3,-1,1,3,-7,2,5,2,8,-4,-3,2,10,-8,7,7,6,-2,-9,-6,4,-2,-9,-8,6,-10,6,-9,-1,5,4,9,-7,-6,10,3,-10,-10,-1,8,10,-6,-1,3,3,1,9,9,4,4,-9,-5,4,-10,6,4,-7,2,-9,-1], dtype = "uint32")#candidate|10580|(2535,)|const|uint32
call_10579 = func_8163_call(relay.reshape(const_10580.astype('uint32'), [13, 13, 15]))
call_10581 = func_8163_call(relay.reshape(const_10580.astype('uint32'), [13, 13, 15]))
output = relay.Tuple([bop_10539,call_10560,const_10561,call_10579,const_10580,])
output2 = relay.Tuple([bop_10539,call_10562,const_10561,call_10581,const_10580,])
func_10598 = relay.Function([var_10537,var_10538,], output)
mod['func_10598'] = func_10598
mod = relay.transform.InferType()(mod)
var_10599 = relay.var("var_10599", dtype = "int64", shape = (6, 6, 10))#candidate|10599|(6, 6, 10)|var|int64
var_10600 = relay.var("var_10600", dtype = "int64", shape = (6, 6, 10))#candidate|10600|(6, 6, 10)|var|int64
output = func_10598(var_10599,var_10600,)
func_10601 = relay.Function([var_10599,var_10600,], output)
mutated_mod['func_10601'] = func_10601
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10886 = relay.var("var_10886", dtype = "float64", shape = (13, 4, 6))#candidate|10886|(13, 4, 6)|var|float64
const_10887 = relay.const([[[5.470291,-3.064760,-1.610270,0.438675,-2.189072,4.568958],[6.285177,-5.563402,-0.872341,4.120921,-3.248667,9.936237],[2.156231,-4.845011,0.936913,4.490146,-4.682674,7.081637],[-4.095094,8.957557,9.185193,-4.556961,7.777944,-5.535044]],[[-0.682474,0.069520,7.696043,6.855411,-8.206438,2.855439],[-7.545938,6.995693,-7.503288,6.631369,1.765354,3.606124],[1.811127,4.452127,4.963037,-4.980796,-0.874240,-4.319988],[-9.719613,-8.242061,-8.657533,1.550110,-2.529273,1.692583]],[[6.922315,3.845574,4.149671,8.657340,-0.598663,6.381353],[2.778643,0.032828,1.805572,4.288187,8.101285,9.617245],[7.268268,-3.834248,5.945674,-4.026839,-5.440149,6.200666],[-7.071564,-7.508960,-6.963187,-7.765115,-5.408951,8.625066]],[[-0.600081,1.152973,-7.889678,2.010482,1.007890,4.610880],[1.556112,3.867328,9.615663,6.142831,-2.426123,-3.986460],[8.029680,-1.989989,-7.890178,-2.774328,-5.770846,-9.203854],[-2.772377,-9.904840,-5.656488,-3.967671,6.620608,1.394622]],[[-8.650425,-0.248630,8.541941,0.045569,-9.032489,-9.909152],[4.283687,4.010575,-3.650583,-9.606840,2.531824,9.026000],[-2.590657,4.973398,3.903450,-0.504727,9.057680,-6.929990],[0.962794,3.871560,0.705220,-0.531176,-6.352711,-5.320736]],[[-9.069964,5.409644,5.203899,6.855342,-7.609382,4.362900],[0.231832,-0.526604,4.102230,8.493551,-7.103101,-8.210850],[-1.055907,6.746584,-9.901781,-4.456864,-0.591178,-5.137751],[-2.552088,-7.134042,-9.174668,-0.281052,1.798184,-9.052990]],[[-2.769643,-3.735301,-9.339550,-9.476739,4.630693,-2.300365],[-3.715657,-0.051560,-5.746289,-4.658836,-1.629309,-4.386487],[8.537032,6.679013,1.871379,6.853232,9.428601,-3.729945],[-9.152688,0.398306,-5.118872,0.525068,-2.526975,-3.635036]],[[-4.634681,6.069077,3.042793,5.774524,-7.300225,0.345026],[-6.575228,8.973803,-3.891359,9.634971,3.441585,7.135305],[-2.314714,-0.366467,-9.070278,-3.573799,5.685103,-8.642812],[2.128791,9.661027,-0.674133,0.146345,9.997191,-3.129624]],[[-3.943931,-8.934470,-9.669556,-6.412620,-8.561614,7.977760],[3.555808,5.892840,1.470225,7.202327,9.208501,0.671347],[6.295822,-7.612098,6.842472,0.637361,9.934005,4.959487],[1.593747,-6.069200,-0.521407,-1.792872,4.327164,7.485431]],[[2.551864,6.411205,9.841905,-3.832619,3.459988,-4.866318],[-3.947933,6.840437,5.672348,5.403248,-6.518558,8.984465],[-6.698152,-8.694770,4.555261,-9.826866,-5.387909,-6.237358],[-5.178274,-3.460138,8.756472,6.833425,-3.601347,0.200933]],[[5.853190,-4.511315,0.341852,6.532874,-6.776308,3.069135],[4.032063,-1.627600,-0.175098,9.113154,-7.277000,-2.498539],[-7.094843,5.075969,-4.088431,3.412483,3.661993,7.223800],[3.843309,-8.825009,-2.279178,1.622190,-6.712074,5.446794]],[[-8.792034,4.092097,4.673515,2.980681,0.985391,-0.814575],[0.032365,-5.861597,-7.379075,1.602282,-0.609179,8.206918],[-6.854781,-3.937749,-9.865245,8.904589,-7.660041,5.948051],[-8.327036,-6.525961,8.105655,-1.059021,-1.920224,-7.117442]],[[-6.191015,-8.880327,0.151333,-1.306654,-1.558570,-3.541683],[-9.196848,-6.389133,1.876122,-4.799684,-6.134555,3.907083],[-6.358699,-9.003352,-4.176054,4.927148,9.084978,0.830497],[8.766148,-3.970887,-8.179724,-8.768033,-7.617617,-7.481843]]], dtype = "float64")#candidate|10887|(13, 4, 6)|const|float64
bop_10888 = relay.floor_divide(var_10886.astype('float64'), relay.reshape(const_10887.astype('float64'), relay.shape_of(var_10886))) # shape=(13, 4, 6)
func_6800_call = mod.get_global_var('func_6800')
func_6804_call = mutated_mod.get_global_var('func_6804')
const_10899 = relay.const([True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False], dtype = "bool")#candidate|10899|(528,)|const|bool
const_10900 = relay.const([1,3,-10,1,4,-4,10,-8,-2,7,3,-7,-6,-6,-4,8,-1,-1,-7,8,6,8,-8,2,3,3,-7,-1,-1,9,-2,-1,9,1,4,5,3,-8,10,-3,1,9,6,10,-8,3,7,10,3,10,-3,9,-10,9,7,5,7,6,3,-1,5,1,-7,6,4,-1,-2,-5,5,6,-7,8,4,-7,9,10,-5,6,1,4,-9,-4,-5,-5,2,-10,4,-3,3,-7,-10,-6,7,-9,-3,6,7,-5,7,-3,-5,10,-3,8,-2,6,-2,-9,4,9,-10,-3,3,1,10,-10,7,4,2,-5,7,-8,-6,9,-6,1,-1,5,2,3,2,-9,-3,10,-5,10,6,10,-7,-4,-5,-9,9,10,3,-5,9,7,-7,9,-2,3,-9,2,1,-8,-2,7,-4,3,2,-4,4,-5,6,10,-5,10,7,7,-9,-6,-4,4,-10,5,7,-5,9,-1,-5,5,-5,1,6,-9,7,-9,8,8,10,-2,-1,9,8,-6,-10,-1,5,-6,4,-9,-1,-1,-10,9,-2,-1,9,-2,-8,7,9,-7,-4,9,-8,-8,-7,-2,-7,10,-3,2,-9,-6,-3,8,-3,-10,8,2,10,-7,-8,-5,-9,4,-4,-3,-1,1,-1,7,4,8,9,-7,1,-3,4,-4,2,6,-4,-10,-9,-8,10,4,-5,7,4,10,-10,6,2,1,-8,2,6,-7,-3,-5,2,-8,-4,10,8,5,6,6,-1,-4,3,-1,7,4,-2,-2,10,1,4,-4,-3,4,8,9,-4,8,-10,6,6,-5,3,-1,7,7,-3,-6,9,8,-8,9,-10,1,8,7,-9,2,-10,-7,7,2,4,-8,6,10,-3,-9,-8,4,8,-9,4,1,4,-4,-1,-3,-2,7,9,5,-6,8,5,-9,-3,-1,10,2,-9,7,3,-4,2,-5,9,-4,4,-1,4,-1,-8,4,2,2,-4,-1,8,10,-5,1,-6,-8,-7,-9,-9,-7,-1,-5,-1,-4,5,-10,1,2,-6,1,-8,-2,8,-7,10,-3,7,5,4,-2,7,9,1,-5,4,9,-4,6,-2,10,7,4,3,3,-1,4,7,5,7,-7,5,-5,-8,-3,-4,-2,-6,8,-8,-7,-7,4,-8,-4,-10,-8,-8,5,3,-6,-1,-9,-9,-8,-9,-3,-6,2,7,-9,-8,3,9,4,8,-9,2,-5,5,5,8,2,-4,-8,-10,-9,5,8,2,5,4,6,-2,-7,6,-2,-10,8,9,-7,6,-9,10,6,9,-9,-7,-9,9,5,9,-2,2,-5,8,9,-1,-9,-8,-10,-8,10,-5,-2,6,-10,9,-4,-3,-3,4,-7,2,4,2,-7,-5,4,5,-4,7,5,-7,-6,-1,-1,1,-10,5,5,9,8,6,-4,9,-3,6,-2,-1,3,-7,7,-6,5,2,-9,-9,-7,-10,-9,10,7,3,9,8,-6,-10,-7,9,-8,-1,3,7,-8,-10,-5,-10,-8,-10,7,-3,-4,-5,9,-2,-6,-5,4,9,-8,8,1,6,1,8,-5,-10,-4,-2,2,10,-1,-6,-7,-7,-6,-8,5,10,-9,5,-9,-5,-3,-6,4,-10,10,-10,-3,-4,3,9,4,-5,8,-9,6,-2,2,1,-3,-9,-1,10,5,4,-5,-6,-2,4,-3,-9,-8,8,-8,-3,4,-3,-10,-8,8,5,-8,-4,3,2,-2,7,-3,-9,-5,-3,-6,-3,-1,3,6,-5,-8,5,-7,-9,10,-9,10,8,-10,-4,9,-3,2,-4,-2,3,5,5,-4,1,10,-9,-7,8,9,-2,-1,1,-10,2,-3,6,-10,10,-5,2,-2,-8,9,6,7,-8,-4,-2,5,8,8,6,3,5,-8,5,-7,10,-6,4,6,-2,1,7,-9,-4,9,6,-5,-3,-8,-4,9,9,-10,-9,-4,-1,8,-3,-4,-5,-6,-8,3,-3,-8,-4,-10,-2,-7,-1,5,-8,-9,-1,7,-8,8,3,7,-2,4,4,10,-6,-9,10,6,-7,10,-10,6,1,5,-5,9,-9,-5,6,-9,4,9,1,3,-2,6,1,3,-5,-5,3,2,-8,-5,4,-9,1,4,5,2,4,1,-1,9,-5,8,10,-1,7,-5,1,1,3,-6,7,-8,-5,8,5,1,2,7,-1,2,-4,9,2,7,-7,6,10,-5,-4,10,10,9,-5,4,7,-2,-3,-6,2,2,8,-5,1,3,3,-3,9,5,-10,-9,-2,-8,3,2,9,7,10,-6,-2,-6,-6,-9,3,-10,2,-2,10,1,-3,-1,7,-10,9,-9,8,-7,-6,-1,10,-6,1,-7,5,6,-3,10,4,6,-9,4,2,-2,-8,9,-4,-10,-10,-8,7,3,-1,-7,-7,8,-9,3,-6,10,-8,1,2,9,-8,-9,10,-4,-6,-8,5,-9,10,8,7,-9,-4,8,-10,10,-5,5,-10,8,2,-1,4,3,-3,2,-6,-6,-9,-8,1,-9,6,4,2,4,-10,1,4,-9,-5,-9,-10,-3,9,-10,-1,9,-2,5,-4,6,-3,-7,-2,-6,-7,-10,-9,-10,6,1,8,9,10,3,-3,8,-5,5,-3,-4,5,1,-9,-4,-8,6,-2,5,-9,6,7,-9,10,10,4,-6,-10,-5,-6,3,2,2,-4,-8,5,-4,9,-7,-7,4,2,2,-5,-10,6,4,3,-3,-3,10,6,-10,-7,-6,3,6,8,-9,5,-3,-3,8,-3,2,4,5,6,-5,-4,9,-8,5,5,8,-1,10,10,-9,10,10,-3,-4,-2,-2,-7,-6,-8,-1,-4,2,2,1,-1,-6,4,-5,-2,-6,5,1,-10,6,-7,-10,8,6,1,3,-8,3,6,8,8,-2,-3,6,1,1,1,-9,-3,-10,-4,6,-3,-3,8,6,-7,-8,5,-6,-6,-4,-10,7,-10,8,3,6,-5,-4,4,1,-2,4,3,-4,8,-7,3,-2,4,-4,5,2,1,-3,7,6,2,-9,-9,7,2,-8,9,-5,9,9,-1,4,-6,9,-2,5,5,3,8,3,-4,-3,10,-8,-9,-3,-6,6,-7,-5,10,-4,-5,-10,7,-1,2,-5,-5,-3,10,7,-4,-7,-8,9,2,4,2,-8,-7,9,-6,4,-7,-6,-3,-2,7,-8,-2,2,2,-1,10,-3,-10,-8,9,8,7,5,-8,-6,8,10,5,-6,-10,3,-8,-8,-9,7,-6,-3,10,4,-5,-2,6,-5,-8,10,-7,9,-7,4,-3,3,-5,-4,-4,-4,9,-4,-10,8,9,7,8,9,-4,3,-3,7,-3,-4,9,8,4,3,-2,-3,6,6,9,-1,-10,10,-3,5,10,-4,7,-7,5,-6,-2,7,10,-3,-3,-4,1,8,3,-9,-3,5,7,1,-3,-9,6,2,3,7,-10,-9,-4,-4,-10,-3,-5,3,10,4,-8,10,-2,4,-8,9,1,-10,7,-6,-6,-10,-7,5,-6,5,-3,-2,5,-10,6,-2,1,3,-5,-5,-6,-6,-9,-4,-1,10,2,-10,-5,-2,4,-7,-4,-1,7,-2,2,-8,10,-5,-1,-8,5,9,-10,1,5,-9,8,9,-5,-8,8,7,10,-10,4,-3,8,9,5,2,-9,8,-10,-1,-8,3,9,-6,9,-9,6,2,-5,1,-2,-9,-5,-8,-4,1,10,-7,-3,7,1,-5,-9,8,-9,-6,-4,-3,4,4], dtype = "int16")#candidate|10900|(1404,)|const|int16
call_10898 = relay.TupleGetItem(func_6800_call(relay.reshape(const_10899.astype('bool'), [12, 4, 11]), relay.reshape(const_10899.astype('bool'), [12, 4, 11]), relay.reshape(const_10900.astype('int16'), [1404,]), ), 0)
call_10901 = relay.TupleGetItem(func_6804_call(relay.reshape(const_10899.astype('bool'), [12, 4, 11]), relay.reshape(const_10899.astype('bool'), [12, 4, 11]), relay.reshape(const_10900.astype('int16'), [1404,]), ), 0)
func_9929_call = mod.get_global_var('func_9929')
func_9932_call = mutated_mod.get_global_var('func_9932')
var_10910 = relay.var("var_10910", dtype = "float32", shape = (588,))#candidate|10910|(588,)|var|float32
call_10909 = relay.TupleGetItem(func_9929_call(relay.reshape(var_10910.astype('float32'), [14, 3, 14])), 1)
call_10911 = relay.TupleGetItem(func_9932_call(relay.reshape(var_10910.astype('float32'), [14, 3, 14])), 1)
func_6258_call = mod.get_global_var('func_6258')
func_6262_call = mutated_mod.get_global_var('func_6262')
var_10933 = relay.var("var_10933", dtype = "float32", shape = ())#candidate|10933|()|var|float32
call_10932 = relay.TupleGetItem(func_6258_call(relay.reshape(call_10909.astype('uint32'), [11, 10, 2]), relay.reshape(var_10933.astype('float32'), []), relay.reshape(var_10910.astype('float32'), [588,]), ), 3)
call_10934 = relay.TupleGetItem(func_6262_call(relay.reshape(call_10909.astype('uint32'), [11, 10, 2]), relay.reshape(var_10933.astype('float32'), []), relay.reshape(var_10910.astype('float32'), [588,]), ), 3)
func_7590_call = mod.get_global_var('func_7590')
func_7593_call = mutated_mod.get_global_var('func_7593')
const_10942 = relay.const([-8.484223,-6.430922,6.667469,-5.997891,4.116522,-1.237433,-0.916852,9.212119,1.433006,-3.054905,2.970262,-4.987020,4.011532,-6.533183,2.694679,3.343032,-3.842351,-3.790252,9.067380,9.733857,-4.688722,7.946462,5.962444,-9.675227,-4.039770,4.532657,-6.556047,0.810351,6.879741,-7.276325,7.667714,-1.002697,2.079333,-7.262223,0.085855,2.616369,6.979432,-5.555415,6.769630,8.204859,-5.749850,9.616724,3.690124,-7.506053,-7.410256,4.222089,0.202807,-1.620938,-8.236483,3.279677,-8.219664,7.847445,7.586613,-1.560681,7.516292,8.411840,-6.946127,-7.903185,2.427927,-3.448718,-7.943905,-1.435301,1.730970,-8.579135,9.049148,-5.387636,7.590694,3.326217,7.072886,0.111631,9.069977,-9.760372,-5.576926,1.817846,-1.375292,8.988857,3.935803,-2.258235,-6.674830,4.260811,-1.547756,-7.076204,7.462665,-0.100044], dtype = "float64")#candidate|10942|(84,)|const|float64
call_10941 = func_7590_call(relay.reshape(const_10942.astype('float64'), [6, 14, 1]))
call_10943 = func_7590_call(relay.reshape(const_10942.astype('float64'), [6, 14, 1]))
func_3287_call = mod.get_global_var('func_3287')
func_3291_call = mutated_mod.get_global_var('func_3291')
call_10958 = relay.TupleGetItem(func_3287_call(relay.reshape(call_10941.astype('uint32'), [10, 7, 6]), relay.reshape(call_10941.astype('uint32'), [10, 7, 6]), ), 0)
call_10959 = relay.TupleGetItem(func_3291_call(relay.reshape(call_10941.astype('uint32'), [10, 7, 6]), relay.reshape(call_10941.astype('uint32'), [10, 7, 6]), ), 0)
output = relay.Tuple([bop_10888,call_10898,const_10899,const_10900,call_10909,var_10910,call_10932,var_10933,call_10941,const_10942,call_10958,])
output2 = relay.Tuple([bop_10888,call_10901,const_10899,const_10900,call_10911,var_10910,call_10934,var_10933,call_10943,const_10942,call_10959,])
func_10965 = relay.Function([var_10886,var_10910,var_10933,], output)
mod['func_10965'] = func_10965
mod = relay.transform.InferType()(mod)
var_10966 = relay.var("var_10966", dtype = "float64", shape = (13, 4, 6))#candidate|10966|(13, 4, 6)|var|float64
var_10967 = relay.var("var_10967", dtype = "float32", shape = (588,))#candidate|10967|(588,)|var|float32
var_10968 = relay.var("var_10968", dtype = "float32", shape = ())#candidate|10968|()|var|float32
output = func_10965(var_10966,var_10967,var_10968,)
func_10969 = relay.Function([var_10966,var_10967,var_10968,], output)
mutated_mod['func_10969'] = func_10969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11113 = relay.var("var_11113", dtype = "float64", shape = (16, 1, 6))#candidate|11113|(16, 1, 6)|var|float64
var_11114 = relay.var("var_11114", dtype = "float64", shape = (16, 4, 6))#candidate|11114|(16, 4, 6)|var|float64
bop_11115 = relay.divide(var_11113.astype('float64'), var_11114.astype('float64')) # shape=(16, 4, 6)
output = bop_11115
output2 = bop_11115
func_11132 = relay.Function([var_11113,var_11114,], output)
mod['func_11132'] = func_11132
mod = relay.transform.InferType()(mod)
var_11133 = relay.var("var_11133", dtype = "float64", shape = (16, 1, 6))#candidate|11133|(16, 1, 6)|var|float64
var_11134 = relay.var("var_11134", dtype = "float64", shape = (16, 4, 6))#candidate|11134|(16, 4, 6)|var|float64
output = func_11132(var_11133,var_11134,)
func_11135 = relay.Function([var_11133,var_11134,], output)
mutated_mod['func_11135'] = func_11135
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11346 = relay.var("var_11346", dtype = "float64", shape = (4, 7, 13))#candidate|11346|(4, 7, 13)|var|float64
uop_11347 = relay.sinh(var_11346.astype('float64')) # shape=(4, 7, 13)
func_3287_call = mod.get_global_var('func_3287')
func_3291_call = mutated_mod.get_global_var('func_3291')
var_11355 = relay.var("var_11355", dtype = "uint32", shape = (420,))#candidate|11355|(420,)|var|uint32
call_11354 = relay.TupleGetItem(func_3287_call(relay.reshape(var_11355.astype('uint32'), [10, 7, 6]), relay.reshape(var_11355.astype('uint32'), [10, 7, 6]), ), 0)
call_11356 = relay.TupleGetItem(func_3291_call(relay.reshape(var_11355.astype('uint32'), [10, 7, 6]), relay.reshape(var_11355.astype('uint32'), [10, 7, 6]), ), 0)
output = relay.Tuple([uop_11347,call_11354,var_11355,])
output2 = relay.Tuple([uop_11347,call_11356,var_11355,])
func_11364 = relay.Function([var_11346,var_11355,], output)
mod['func_11364'] = func_11364
mod = relay.transform.InferType()(mod)
var_11365 = relay.var("var_11365", dtype = "float64", shape = (4, 7, 13))#candidate|11365|(4, 7, 13)|var|float64
var_11366 = relay.var("var_11366", dtype = "uint32", shape = (420,))#candidate|11366|(420,)|var|uint32
output = func_11364(var_11365,var_11366,)
func_11367 = relay.Function([var_11365,var_11366,], output)
mutated_mod['func_11367'] = func_11367
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12092 = relay.var("var_12092", dtype = "float32", shape = (3, 7, 10))#candidate|12092|(3, 7, 10)|var|float32
const_12093 = relay.const([[[3.578950,-4.154598,7.979835,-2.085980,-6.019533,-3.090552,-7.984926,0.917757,8.567071,-8.675427],[-5.741677,-4.962406,3.051774,0.149339,1.925481,3.095107,5.622225,-3.946105,-9.813124,8.837232],[4.966572,6.679008,-4.895038,-7.334361,7.090783,0.847993,7.987907,1.928921,-7.916018,-4.735193],[1.648359,-0.546774,-3.900840,5.234349,9.230518,9.769025,-9.869039,2.217098,0.669436,9.869953],[-3.208046,-8.671390,-9.751551,-1.479956,-7.872002,-2.388909,3.846463,0.818324,7.094260,-4.743813],[6.345769,5.800620,5.039008,-2.314683,0.343619,6.092630,-4.216858,1.038920,3.535077,4.084972],[-2.928441,8.468036,-8.632680,1.443112,8.801432,2.797324,2.940384,1.289141,0.262705,2.030710]],[[2.694278,-1.736724,4.325912,-8.816687,-7.503535,-2.397780,6.211678,-7.365540,-8.479954,-7.853289],[2.679178,-7.435635,-2.378036,4.289130,7.582024,-0.707226,1.114426,-0.498625,-9.858130,4.473825],[-9.824146,-7.876393,4.342781,-3.123182,-9.508965,-5.187030,-7.361689,5.596888,-6.382242,-5.761886],[0.127720,-1.739964,0.220463,0.873737,6.262927,-9.458445,4.887474,1.268752,1.030919,-7.894905],[-1.579498,-1.413691,-4.106062,-3.965730,-1.232093,-6.651918,9.311736,7.716611,-8.963151,4.032278],[1.679721,1.402017,-3.190085,-1.772699,-7.627954,9.641653,0.171871,6.451874,3.323284,-6.157359],[-8.922269,-3.599118,5.926067,1.712356,-1.159719,4.740760,-4.947674,-7.743708,1.149676,1.224621]],[[-5.116152,4.394359,-2.842127,5.577994,-3.323893,0.740285,-6.869066,-1.121456,1.926978,2.237545],[-2.106996,-5.209917,-6.238979,5.279019,5.352894,8.184796,-9.501639,5.221495,-7.932884,-5.694163],[-2.480763,0.297294,2.011257,-9.488579,4.087176,9.084246,-6.048957,3.136883,-4.752275,-0.680233],[6.350585,1.209413,-9.898937,-5.386952,8.639628,8.098153,-3.647843,5.120836,1.936323,4.362826],[7.868526,-7.015529,-1.419907,-3.595403,0.310422,-3.512912,6.036585,-5.249860,-6.555150,-8.474195],[7.488948,5.827454,-4.256400,-3.594979,-4.104531,3.476780,-5.692301,1.655204,9.971809,2.719822],[-8.406690,9.522851,-6.792158,-4.629588,-6.976690,-6.046723,-8.908165,4.799389,-4.045120,-1.881248]]], dtype = "float32")#candidate|12093|(3, 7, 10)|const|float32
bop_12094 = relay.power(var_12092.astype('float32'), relay.reshape(const_12093.astype('float32'), relay.shape_of(var_12092))) # shape=(3, 7, 10)
func_7645_call = mod.get_global_var('func_7645')
func_7649_call = mutated_mod.get_global_var('func_7649')
var_12111 = relay.var("var_12111", dtype = "int16", shape = (9, 156))#candidate|12111|(9, 156)|var|int16
call_12110 = relay.TupleGetItem(func_7645_call(relay.reshape(var_12092.astype('float64'), [14, 15, 1]), relay.reshape(var_12111.astype('int16'), [1, 1404]), ), 0)
call_12112 = relay.TupleGetItem(func_7649_call(relay.reshape(var_12092.astype('float64'), [14, 15, 1]), relay.reshape(var_12111.astype('int16'), [1, 1404]), ), 0)
func_634_call = mod.get_global_var('func_634')
func_637_call = mutated_mod.get_global_var('func_637')
var_12116 = relay.var("var_12116", dtype = "float32", shape = (220,))#candidate|12116|(220,)|var|float32
call_12115 = relay.TupleGetItem(func_634_call(relay.reshape(var_12116.astype('float32'), [10, 11, 2]), relay.reshape(var_12116.astype('float32'), [10, 11, 2]), ), 0)
call_12117 = relay.TupleGetItem(func_637_call(relay.reshape(var_12116.astype('float32'), [10, 11, 2]), relay.reshape(var_12116.astype('float32'), [10, 11, 2]), ), 0)
func_8102_call = mod.get_global_var('func_8102')
func_8105_call = mutated_mod.get_global_var('func_8105')
const_12120 = relay.const([-7,-8,8,2,4,8,-1,-1,3,-10,6,9,-2,7,-3,-1,1,-7,9,1,-7,5,3,3,-8,8,-6,5,-8,-6,-1,3,-8,3,10,-1,10,-7,1,-9,-2,-1], dtype = "int64")#candidate|12120|(42,)|const|int64
var_12121 = relay.var("var_12121", dtype = "int64", shape = (546,))#candidate|12121|(546,)|var|int64
call_12119 = relay.TupleGetItem(func_8102_call(relay.reshape(const_12120.astype('int64'), [3, 1, 14]), relay.reshape(var_12121.astype('int64'), [3, 13, 14]), ), 2)
call_12122 = relay.TupleGetItem(func_8105_call(relay.reshape(const_12120.astype('int64'), [3, 1, 14]), relay.reshape(var_12121.astype('int64'), [3, 13, 14]), ), 2)
output = relay.Tuple([bop_12094,call_12110,var_12111,call_12115,var_12116,call_12119,const_12120,var_12121,])
output2 = relay.Tuple([bop_12094,call_12112,var_12111,call_12117,var_12116,call_12122,const_12120,var_12121,])
func_12124 = relay.Function([var_12092,var_12111,var_12116,var_12121,], output)
mod['func_12124'] = func_12124
mod = relay.transform.InferType()(mod)
var_12125 = relay.var("var_12125", dtype = "float32", shape = (3, 7, 10))#candidate|12125|(3, 7, 10)|var|float32
var_12126 = relay.var("var_12126", dtype = "int16", shape = (9, 156))#candidate|12126|(9, 156)|var|int16
var_12127 = relay.var("var_12127", dtype = "float32", shape = (220,))#candidate|12127|(220,)|var|float32
var_12128 = relay.var("var_12128", dtype = "int64", shape = (546,))#candidate|12128|(546,)|var|int64
output = func_12124(var_12125,var_12126,var_12127,var_12128,)
func_12129 = relay.Function([var_12125,var_12126,var_12127,var_12128,], output)
mutated_mod['func_12129'] = func_12129
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12245 = relay.var("var_12245", dtype = "uint64", shape = ())#candidate|12245|()|var|uint64
var_12246 = relay.var("var_12246", dtype = "uint64", shape = (12, 6, 4))#candidate|12246|(12, 6, 4)|var|uint64
bop_12247 = relay.greater(var_12245.astype('bool'), var_12246.astype('bool')) # shape=(12, 6, 4)
func_11132_call = mod.get_global_var('func_11132')
func_11135_call = mutated_mod.get_global_var('func_11135')
const_12251 = relay.const([[4.623531,-3.563786],[-3.746040,7.083913],[-8.020536,-2.143441],[-3.527077,-9.622987],[-4.881098,7.547076],[-5.085383,-8.424621],[7.723506,-3.810424],[-2.516547,-7.023729],[-8.214129,2.963679],[5.099188,-0.601949],[6.589378,-6.544366],[0.310854,-3.067023],[-9.516684,-6.931739],[7.039390,6.769492],[-8.856728,-9.261148],[-1.509307,-9.058026],[-1.293235,7.712262],[-6.408816,4.555567],[-5.911853,-2.011785],[5.579208,8.176065],[-1.492999,-8.900080],[-4.387380,2.127899],[-9.983661,4.367108],[-4.826347,0.655482],[-6.676323,-0.785671],[-7.307730,-4.163525],[-7.509255,-0.840502],[4.993226,0.699005],[6.415695,1.472287],[-1.446121,-3.323881],[-5.074800,1.519755],[9.025036,7.197131],[4.134737,5.219668],[-1.982164,-8.961879],[-5.620509,-5.108112],[7.777124,5.275459],[1.179918,-6.541087],[5.106499,-2.789258],[7.987757,1.284784],[-6.991759,-2.094790],[-0.499604,1.625288],[2.543713,6.608557],[9.407422,7.271399],[-6.685504,5.805736],[5.034255,3.017879],[1.480505,-4.870761],[7.355154,5.426625],[1.864271,3.348542]], dtype = "float64")#candidate|12251|(48, 2)|const|float64
const_12252 = relay.const([-4.177209,-5.734093,7.923100,-1.115667,0.221737,5.013052,-7.171255,1.670170,0.823470,-4.460957,0.391459,-8.230797,2.968688,0.122872,8.311758,6.843990,4.130449,9.125391,9.841336,-0.453935,4.213601,4.640780,-4.802775,5.506264,-7.114776,-6.439660,-5.709207,-3.974914,-1.772392,-7.549109,5.670489,-7.813846,-8.982909,4.118898,1.921579,-2.314297,-8.615614,-9.909846,-7.993365,-7.556375,2.879252,1.694378,6.644877,8.000047,5.452355,0.762480,6.627790,1.577414,6.153483,6.318965,1.187946,-2.521683,0.619245,-6.202677,-5.430311,5.696740,-1.982705,8.164276,-5.853726,7.118546,5.603111,3.758123,-2.742809,-3.151717,3.885202,0.884497,3.132215,-7.591494,-0.266566,-1.359313,3.600781,5.221934,-0.158421,-9.812274,0.365341,-4.215369,-0.757259,-0.155109,5.520246,2.198273,-7.193975,8.461861,-3.633537,4.066329,-1.431326,9.710463,6.093407,6.468802,-4.722003,-0.150764,-9.212948,-6.182012,-6.213428,2.689223,7.577757,1.002619,4.765530,0.981828,-3.816457,6.029505,-4.626652,0.333255,3.706006,-9.179176,-5.106603,0.943030,4.941498,7.965539,-3.451070,6.446489,7.655161,-2.985362,0.732211,-5.217234,-5.244570,9.763776,5.451565,-0.788465,3.188708,-2.674996,8.387557,-8.316311,0.023527,5.851837,9.343364,8.756439,6.940915,1.983425,8.255021,-2.716240,0.370584,-8.682120,-8.164224,7.529836,1.660630,1.009928,-0.417590,-9.230302,-6.145778,5.310287,-5.563581,-2.328447,-8.691328,0.904887,-9.877423,6.258167,5.476657,-8.055225,-1.523345,6.838814,9.033189,1.601084,1.049520,2.005504,8.257336,2.726786,0.444391,4.188532,1.393127,5.054364,-5.645387,-4.125217,-1.004195,-9.086711,-4.300016,4.999952,-7.676684,7.449454,-7.536868,4.661603,-7.859564,5.106565,7.005947,6.249874,6.007891,-6.792358,-8.688047,0.792167,1.850841,8.383841,-2.019271,9.187563,0.183375,-6.885009,4.622714,8.717070,-5.145750,1.419232,9.129281,-5.593924,5.280674,7.396409,2.503852,-3.847769,-7.422096,0.733848,-9.489874,0.991399,9.200410,8.815472,-9.894341,-6.878639,-2.567978,-9.757962,7.960662,-0.977934,4.979160,-5.283473,3.796869,3.005400,-2.672178,-3.028543,4.803183,4.901976,9.387841,9.026385,5.807141,-4.916177,1.164869,-3.472204,0.451242,0.979008,-8.352369,-4.556578,-8.271110,3.326516,-3.089905,-6.410004,4.085189,-5.593321,-5.744153,-8.073223,-1.532096,5.239994,0.747728,-4.561128,3.747468,7.291554,7.419643,3.612155,0.646715,-1.600900,-9.476839,2.982942,-6.570853,-1.509791,0.271394,9.692250,5.811722,0.927690,-3.857636,7.524502,6.715902,6.220706,-1.272531,1.716952,3.144950,4.466128,-8.495996,4.720335,5.798865,3.490615,6.474319,-5.526143,-5.815037,9.235178,8.511900,-9.220134,-0.508875,8.703690,-9.125219,-3.094251,-4.189757,2.043504,5.223905,-0.139214,-1.021991,4.563333,-1.224243,-2.105109,-5.395325,7.327110,-0.809753,-1.323565,8.923014,-9.248933,-2.102966,0.848999,-3.794479,3.728762,2.953814,-3.835670,-0.729585,4.148615,3.430106,9.165998,-3.337375,9.450293,-1.268496,8.644936,7.162369,4.335513,-3.193463,5.330439,4.419497,-7.026661,-3.406510,-6.970009,4.924696,1.716286,1.899594,-5.735341,6.122808,-6.047885,5.168789,2.427942,4.316540,7.213124,7.846070,6.659731,6.075785,2.897310,-7.137048,-4.196075,-7.882268,6.289895,-1.948542,8.248504,7.339923,4.302687,0.053677,-1.579601,3.095172,-0.524878,-8.823726,2.323196,-0.856167,0.908932,-6.072847,-5.243569,3.652027,-6.195797,5.941305,7.206750,-3.574673,8.887624,7.033357,-2.543078,4.183874,1.726091,-8.977213,-2.782178,4.354878,-8.305945,9.048945,-5.069204,-1.158252,7.970400,-4.852554,-9.224209,2.725623,-4.505479,1.887323,-8.881429,-0.613036,-1.041461,-9.772551,1.453987,-5.684907,-1.146320,-5.156222,-3.717007,2.283448,-4.966355,-8.148638,-2.597112,-5.393171,-4.681812,-7.141097,8.053528,-3.755244,5.451498,-8.972229,2.138722], dtype = "float64")#candidate|12252|(384,)|const|float64
call_12250 = func_11132_call(relay.reshape(const_12251.astype('float64'), [16, 1, 6]), relay.reshape(const_12252.astype('float64'), [16, 4, 6]), )
call_12253 = func_11132_call(relay.reshape(const_12251.astype('float64'), [16, 1, 6]), relay.reshape(const_12252.astype('float64'), [16, 4, 6]), )
func_7645_call = mod.get_global_var('func_7645')
func_7649_call = mutated_mod.get_global_var('func_7649')
const_12255 = relay.const([[2.512980,6.061289,5.606687,3.790124,-2.628289,-0.233511,3.982827,8.296856,-1.639512,-5.032762,-6.388898,6.795549,-8.368409,4.535279,-6.337969,6.953691,-6.540889,-2.853198,1.239186,3.401277,-8.765541,-3.729502,-2.192491,7.145752,-9.102373,9.371252,-4.655296,-9.678451,-0.605582,-0.893537,0.997692,-9.233570,-9.158680,0.412498,-0.213041,7.176311,1.151346,-5.804201,2.686002,-2.689826,-7.234225,0.115728,8.663368,5.871171,1.121616,-4.683769,7.774955,-8.188449,5.491340,3.076437,2.317380,-2.890398,9.368144,-2.906566,-2.216826,-6.016808,-6.653025,-8.524651,2.359955,5.889332,0.274098,3.828137,-5.409634,-7.022360,-5.121818,-2.753320,-0.936835,-8.055290,9.149085,-9.286229,0.771375,-7.061820,-4.227649,9.803726,-6.999186,-6.470222,9.836064,2.841050,-0.809252,2.563444,2.648945,-9.099687,1.578866,9.585247,3.905124,-3.421877,7.305574,-0.276152,9.454078,0.776853,6.212636,4.763413,-8.487969,-0.104711,-0.715504,6.279870,8.520384,1.550905,-5.921527,-2.772313,0.575561,-5.756140,0.130565,-8.998773,5.830192,5.153540,-0.486498,8.971130,8.030219,4.194466,3.378634,2.721798,-8.620982,1.648971,-5.920615,-9.944650,6.781051,-0.291087,6.447491,4.063955,-4.911261,8.920665,-1.640871,0.997610,0.189370,0.822429,2.783171,2.744565,-6.621304,-2.600123,-7.852959,-4.512542,-5.846472,0.942274,0.717662,-6.042915,8.919462,-4.184991,-6.615084,6.070498,-3.422210,-4.112012,3.526802,3.118205,6.185113,-2.875125,-7.624559,3.328503,6.048414,9.548803,8.526961,9.470582,5.933652,-8.031832,0.288854,4.392126,8.399857,-9.228530,-2.071961,-1.478669,7.354372,8.507221,9.307767,-7.392364,9.041035,8.170130,8.304278,5.860219,4.407477,-0.458360,8.833335,-3.231065,-1.471243,-4.770739,3.055819,-8.359725,5.288944,-5.516933,-6.075924,-8.714853,-3.830060,-4.682158,-6.061465,7.212042,-9.063490,-9.530788,3.883312,-0.470820,6.073517,-4.723929,0.575249,-9.635723,5.084120,3.455177,3.140610,8.249181,3.545501,-8.813731,-3.081811,9.279703,1.120530,-6.029285,5.967182,-7.962890,5.196422,7.751882,7.328848,-9.328891,-0.137643,-5.785011]], dtype = "float64")#candidate|12255|(1, 210)|const|float64
const_12256 = relay.const([[-2,1,-4,-4,4,-6,-1,-6,9,9,-7,1,-1,-4,6,3,4,-10,10,9,-5,2,-3,-9,8,-2],[-10,-4,4,10,-2,2,7,-4,-5,3,-1,-5,5,-7,-3,9,-3,-8,3,-9,-3,10,-2,-8,-9,-6],[-6,-3,7,6,-2,-5,10,-4,-1,7,-3,-5,3,-1,-4,3,7,3,-9,-6,-3,-5,-4,7,1,1],[-5,10,-8,10,-7,-2,-2,-10,3,1,-7,-1,5,-8,4,-2,-6,6,-3,-5,-1,7,-3,4,5,4],[-10,-4,-4,1,4,6,-6,-3,1,9,7,5,7,6,3,-5,-6,9,-3,-8,6,4,-8,-10,5,1],[7,1,-5,5,8,4,1,4,6,9,-7,1,-2,-6,-10,8,-3,3,-6,8,8,-8,5,-3,5,2],[-8,9,6,6,2,-5,-3,-5,-7,-4,6,4,-3,4,-10,2,-1,-8,6,-5,6,-7,6,-9,-6,-8],[5,6,10,8,8,9,-2,-6,-1,-9,1,-7,8,2,8,-6,5,-3,-4,6,-2,9,4,-4,-8,-1],[9,-8,3,-2,-1,6,-2,10,3,-8,-4,10,-4,-2,-7,3,-10,-4,-2,-6,7,-8,10,-5,-7,9],[-1,9,1,-10,-4,-4,-8,9,-5,5,-4,2,-3,8,-1,-1,-6,-8,2,5,4,10,10,-2,-2,-8],[9,4,-7,4,-1,-8,7,-4,-5,5,-8,9,-4,-4,5,-5,-10,-8,3,-4,-9,1,-8,3,4,3],[2,-2,3,3,8,4,-8,6,6,-8,-10,-9,6,2,-9,-3,-8,-7,3,-1,-9,10,1,3,-3,10],[-1,-4,2,-6,2,4,-8,-1,3,3,-10,3,8,7,-6,5,-10,4,-4,5,-4,5,1,5,1,8],[-1,-1,7,-10,-6,2,-3,-8,-1,-4,3,8,-9,-8,1,10,-8,-10,-10,10,7,-2,2,-9,2,-7],[7,8,8,-4,5,10,-6,10,3,2,6,2,3,-9,7,1,-3,9,7,10,-9,7,3,1,-9,-7],[6,-3,1,5,9,-1,7,4,7,-7,-4,-4,-4,-4,6,10,-1,1,4,-9,4,-5,-1,-8,-3,-5],[-1,-4,3,-8,9,3,10,1,3,-8,9,-9,-2,-1,2,-2,6,-8,5,-10,-3,-4,8,-8,5,-8],[-7,7,4,4,5,-8,1,-9,-1,1,-1,-10,2,8,2,-4,-2,10,-10,-9,2,5,5,-10,-5,2],[-9,5,-10,1,-8,3,-5,-4,-9,9,2,7,-1,6,1,2,-10,-1,9,-2,-6,-6,10,-5,5,-2],[-9,-4,5,6,8,6,-4,-10,-1,-9,7,-6,-3,6,7,5,-7,8,-1,-10,4,-10,-4,-1,-1,10],[4,-5,-10,-7,8,-5,-2,-7,-1,5,4,4,-4,-3,-3,-4,-10,6,-7,7,4,10,-8,1,5,-5],[-1,-9,5,-3,4,7,-4,3,3,-9,-3,5,8,-3,3,-4,-8,-3,-4,1,-2,9,9,-9,4,-1],[7,-8,-1,-9,-10,1,7,-1,8,6,-10,6,-9,-6,-1,7,3,4,-10,-8,-8,-8,-1,-4,3,-9],[-5,6,7,6,-9,9,-10,-5,6,1,-2,-8,10,-2,-4,-7,5,4,5,4,-2,-5,-4,3,4,7],[-4,1,-9,-6,5,3,-7,3,-6,8,-8,10,-5,-5,8,-9,8,-4,-2,-1,6,-6,-10,6,4,4],[1,5,9,-7,1,-9,3,-6,-6,1,-3,-4,5,-9,-6,-10,-6,-2,-4,-2,-4,-4,6,3,8,-3],[-2,4,-9,-4,-7,-3,-9,8,6,8,2,-7,3,2,6,2,4,-3,10,-9,6,-2,9,-10,-1,-4],[-2,3,3,-5,-9,-8,3,-6,-1,-2,9,1,3,4,2,8,1,7,5,4,1,6,5,8,1,4],[3,1,-9,-1,2,-2,9,6,3,7,-6,-7,9,7,-7,-1,8,-8,4,5,7,9,-7,9,9,-4],[-10,-3,8,6,-3,-6,8,6,-1,8,-10,-5,3,9,-9,4,3,8,-9,5,-3,1,-6,3,-7,7],[-9,-4,-8,2,-5,-9,-4,-10,-3,-5,7,-8,-2,-10,4,-8,-2,3,7,-7,2,1,-3,10,-5,2],[2,4,-3,-7,-2,7,-9,-3,-6,9,8,-7,-10,-9,-4,6,3,2,-4,10,-3,-1,-9,-9,7,-4],[-9,-8,-8,1,-7,7,-6,-5,-9,-8,2,-5,6,-6,3,9,-1,-8,-3,-10,-9,-2,10,-5,10,9],[3,-3,-9,1,10,-3,-7,9,-3,2,-8,5,2,6,5,6,-1,-8,-1,-2,1,10,-8,9,10,3],[8,7,-10,-1,-8,5,-9,10,6,-1,-9,4,-1,-9,4,8,-10,1,-6,6,-3,-3,-6,2,-7,8],[5,-5,6,-5,6,4,8,7,-10,-10,-6,5,8,-5,-2,2,4,2,-1,-10,-2,-2,-10,6,2,2],[9,-1,7,-5,-6,6,4,1,7,-4,-8,9,7,-7,-1,8,-8,-8,-4,4,10,1,-8,-3,6,5],[-6,-1,2,-4,8,-5,-1,-1,-8,7,5,-3,-2,9,6,1,10,4,3,5,10,-8,-2,9,4,-7],[-4,1,1,-4,-3,8,1,5,2,3,-9,6,-10,3,-9,-2,-3,10,4,-10,1,2,1,-3,-7,-4],[9,-10,-3,4,5,6,10,3,-10,-1,-2,2,-10,6,-3,-6,2,-5,10,8,7,5,-10,1,3,2],[5,-1,-10,4,9,8,-5,4,-4,3,6,9,6,7,-2,-5,2,-5,10,8,9,-1,-10,-2,-9,6],[-2,-3,-4,6,-7,6,6,2,1,7,5,-4,3,9,-10,-7,-1,1,-1,3,9,-9,-1,10,10,-1],[5,4,-9,10,-10,-2,-9,6,1,8,-1,2,8,5,1,-7,-9,-4,3,-10,3,2,6,-2,7,6],[6,1,1,-4,-10,-9,-9,7,-7,5,-10,1,-6,2,4,-3,-5,-6,10,9,10,-9,8,-3,3,-4],[6,9,-10,-7,-7,7,-5,-8,-3,-5,6,-6,-7,1,8,5,3,-5,-4,-9,5,3,-9,4,-2,8],[10,2,2,9,9,5,-7,6,5,2,-1,9,-10,3,10,9,5,9,-5,9,-4,7,-7,5,-10,1],[4,5,-10,7,10,-10,-7,6,7,9,10,-5,1,-8,-6,6,8,5,10,10,10,-6,-8,1,8,9],[6,-6,3,-1,2,1,7,-9,-10,6,8,-6,-6,4,-7,-1,-8,-3,2,9,9,5,-6,4,1,5],[-4,6,8,-6,-6,9,6,4,-3,-2,-3,-10,-9,-4,-6,2,7,-2,9,-1,4,10,1,-6,6,-1],[-4,7,-7,6,9,-3,-5,3,-10,-10,6,4,3,-6,-9,8,-9,-9,-8,-10,-2,-5,-8,2,7,-4],[-3,2,2,6,4,7,1,-10,10,5,-2,8,3,10,5,2,-2,-5,-2,-6,-5,2,8,4,-3,-9],[-1,5,-8,-3,8,-2,-8,5,-7,6,5,-9,-9,10,-4,-7,5,-1,8,5,-9,-8,-5,7,-5,6],[-3,10,10,4,-8,-10,-6,5,5,9,8,-1,10,7,-4,-5,9,-9,-7,4,-5,-8,5,4,-5,6],[-10,-8,-8,8,-7,-7,8,7,8,-1,-6,-3,-2,5,-9,1,-1,-2,4,-10,-10,-1,-4,6,-2,4]], dtype = "int16")#candidate|12256|(54, 26)|const|int16
call_12254 = relay.TupleGetItem(func_7645_call(relay.reshape(const_12255.astype('float64'), [14, 15, 1]), relay.reshape(const_12256.astype('int16'), [1, 1404]), ), 2)
call_12257 = relay.TupleGetItem(func_7649_call(relay.reshape(const_12255.astype('float64'), [14, 15, 1]), relay.reshape(const_12256.astype('int16'), [1, 1404]), ), 2)
func_12124_call = mod.get_global_var('func_12124')
func_12129_call = mutated_mod.get_global_var('func_12129')
const_12269 = relay.const([5.797166,-1.855026,-0.453542,3.774006,1.773083,-5.828158,-5.232957,-2.695168,4.622266,-7.380558,2.513123,8.375871,5.206872,9.998976,6.214521,6.888097,-5.701436,8.804326,-5.169501,6.561998,0.995072,5.972869,9.319078,5.399384,1.802077,-6.674284,-1.417236,3.098104,5.749860,-4.013407,8.616724,0.544012,6.098613,-3.409392,1.865234,1.084847,-0.993997,7.890336,-5.105140,-1.407926,-7.238295,-8.467491,5.483152,-3.974216,6.329607,7.476703,-3.575318,-5.899123,-4.849453,1.295477,4.861922,-8.214122,-2.768206,5.197634,-8.356356,-9.327009,-3.051659,1.000617,-0.086764,-7.770937,4.027248,-2.772148,7.011456,4.055762,9.043197,1.501325,-2.478869,-3.277984,9.894950,9.761746,-6.763436,3.928971,9.122475,-1.441137,-9.021796,5.279722,-0.517067,-2.888067,-8.507811,8.532867,-1.875192,-4.235715,-3.474979,1.191917,-7.418579,1.735746,-8.938349,3.674988,-2.523996,0.292277,9.487005,-2.340690,-2.343655,7.393496,-3.611127,4.729036,0.670765,2.130614,-7.713356,-5.427998,-0.991194,0.507128,-4.425656,-9.593940,-2.037310,9.694750,-9.078125,-0.866927,-8.946411,7.209575,-8.884772,-3.293133,3.091789,-0.856002,-0.889887,-8.059473,-4.903225,-2.162365,7.883150,3.111527,-2.279964,8.802691,-8.650865,-1.647022,6.668682,-9.636943,-0.702396,5.164585,-8.022525,8.148522,-4.523683,6.154016,-7.319680,3.550466,-2.437070,3.359242,-1.798533,1.240336,-5.033348,6.987306,-2.209594,-6.373368,-7.134951,-0.686255,8.510117,-5.406619,6.869777,-0.323877,6.436526,4.645845,6.282147,-5.231790,1.711454,-7.209585,0.902320,3.993807,0.671985,-5.269387,-3.195179,9.255842,5.840925,0.387951,8.587479,-3.073589,-4.569565,2.748311,-5.541127,3.953815,9.354596,-4.086051,0.445876,-6.011338,9.604748,0.721506,1.860247,9.169865,-1.984078,-2.994270,-7.467003,-0.507312,-7.494735,-7.161839,2.127760,6.945320,-2.319039,-7.293691,2.970993,-7.059485,2.759882,-9.173902,-0.366155,9.547753,1.201289,9.454821,-4.819063,-4.710765,8.329263,-7.548798,-7.883649,2.984411,8.435650,-5.144414,2.075684,6.696386,-8.140641,5.892218,8.917422,2.132192,-8.527815,-0.874740,-2.643586,-3.998964,-0.698862,0.516086,-0.462494,3.806498,-2.879860,-0.286552,-6.891833,-0.939408], dtype = "float32")#candidate|12269|(220,)|const|float32
var_12270 = relay.var("var_12270", dtype = "int64", shape = (273, 2))#candidate|12270|(273, 2)|var|int64
call_12268 = relay.TupleGetItem(func_12124_call(relay.reshape(const_12255.astype('float32'), [3, 7, 10]), relay.reshape(const_12256.astype('int16'), [9, 156]), relay.reshape(const_12269.astype('float32'), [220,]), relay.reshape(var_12270.astype('int64'), [546,]), ), 1)
call_12271 = relay.TupleGetItem(func_12129_call(relay.reshape(const_12255.astype('float32'), [3, 7, 10]), relay.reshape(const_12256.astype('int16'), [9, 156]), relay.reshape(const_12269.astype('float32'), [220,]), relay.reshape(var_12270.astype('int64'), [546,]), ), 1)
func_10598_call = mod.get_global_var('func_10598')
func_10601_call = mutated_mod.get_global_var('func_10601')
var_12277 = relay.var("var_12277", dtype = "int64", shape = (360,))#candidate|12277|(360,)|var|int64
call_12276 = relay.TupleGetItem(func_10598_call(relay.reshape(var_12277.astype('int64'), [6, 6, 10]), relay.reshape(var_12277.astype('int64'), [6, 6, 10]), ), 4)
call_12278 = relay.TupleGetItem(func_10601_call(relay.reshape(var_12277.astype('int64'), [6, 6, 10]), relay.reshape(var_12277.astype('int64'), [6, 6, 10]), ), 4)
output = relay.Tuple([bop_12247,call_12250,const_12251,const_12252,call_12254,const_12255,const_12256,call_12268,const_12269,var_12270,call_12276,var_12277,])
output2 = relay.Tuple([bop_12247,call_12253,const_12251,const_12252,call_12257,const_12255,const_12256,call_12271,const_12269,var_12270,call_12278,var_12277,])
func_12281 = relay.Function([var_12245,var_12246,var_12270,var_12277,], output)
mod['func_12281'] = func_12281
mod = relay.transform.InferType()(mod)
var_12282 = relay.var("var_12282", dtype = "uint64", shape = ())#candidate|12282|()|var|uint64
var_12283 = relay.var("var_12283", dtype = "uint64", shape = (12, 6, 4))#candidate|12283|(12, 6, 4)|var|uint64
var_12284 = relay.var("var_12284", dtype = "int64", shape = (273, 2))#candidate|12284|(273, 2)|var|int64
var_12285 = relay.var("var_12285", dtype = "int64", shape = (360,))#candidate|12285|(360,)|var|int64
output = func_12281(var_12282,var_12283,var_12284,var_12285,)
func_12286 = relay.Function([var_12282,var_12283,var_12284,var_12285,], output)
mutated_mod['func_12286'] = func_12286
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14064 = relay.const([[[-6.205878,1.113617,2.996163,-7.379216,1.843807,0.600864,4.704888,-3.686826,-4.003024,2.479794,7.974870,-7.120761,-2.299326,-0.009704,5.308287],[-0.824793,-4.861867,2.393761,6.137278,-3.910546,6.956157,-1.662568,3.356286,5.076036,7.408352,-3.560189,-5.010083,1.687936,-4.043276,-4.059612],[4.655638,-6.762984,8.766306,-1.523881,2.012104,0.497496,-3.589116,0.513370,-3.262519,-5.314841,-0.642793,-6.231689,3.990419,9.185667,8.655516]],[[4.940871,5.341771,-0.850144,-8.012142,2.488260,-1.063025,-3.341471,-9.820841,-4.998269,-5.442888,3.687422,7.588112,1.794403,4.564591,-6.324732],[5.330470,-6.147647,8.009993,9.627373,7.764187,-1.338802,1.467761,-7.342574,-3.774464,9.254820,0.674080,7.035970,-0.262771,4.060905,-8.172527],[6.335765,-8.244972,-9.339050,-2.769976,3.791460,-9.893706,5.789798,-1.783238,-0.735431,-5.408110,8.303095,-7.869356,-0.460305,5.644873,-6.986014]],[[-6.548321,1.650377,5.134738,-8.836149,6.104028,7.471555,4.332087,-0.593433,8.558949,3.848767,-9.423667,4.635922,0.524776,7.316322,-2.394461],[-8.322410,6.227478,9.145425,9.510146,1.303872,5.777864,4.380953,8.742252,-3.449513,-7.453443,3.620189,-2.475125,9.337627,-9.658196,-2.292851],[-4.315248,0.761375,7.468503,6.050401,2.755938,3.055727,6.505182,5.735679,-2.998752,5.947417,5.700724,6.971607,-1.734941,-4.506874,-4.784925]],[[2.557753,4.011885,-4.869149,6.265735,-4.534005,-0.067496,9.336331,-4.087471,2.618867,-0.678746,7.280852,9.243814,2.553271,6.398883,-8.646285],[-9.353275,-1.719878,7.647475,-8.780644,-0.381254,9.897896,6.209091,4.995312,0.945889,-4.499172,8.561961,-7.827441,2.700682,-6.608281,8.937412],[-5.826548,-8.639679,5.247125,2.171107,-7.120790,-5.574726,9.618671,-4.404765,7.929101,8.913952,2.814335,6.875996,5.784858,2.189029,0.448221]],[[-8.800237,2.467560,3.455190,-3.054766,-3.289846,-5.254428,-4.916535,-3.681232,-5.632613,5.755939,-7.763440,1.741501,-3.974999,-7.825989,-5.423428],[-9.263479,0.072053,-4.247617,-4.516971,4.886838,4.668580,-7.388681,1.721692,7.774403,-5.914632,4.601093,9.447322,1.684881,1.312798,-7.640364],[8.390426,8.736552,-5.995322,7.218431,-7.085462,6.154472,8.875310,-6.795397,4.679438,-2.871839,-1.893985,-0.845203,-5.231810,6.923818,5.192251]],[[-3.363835,-2.768362,6.880620,2.218330,7.688750,4.509245,2.672393,-3.860467,-8.354007,7.942806,-6.596739,-3.365212,-6.991883,-4.784445,1.658074],[1.181235,-1.160961,4.777201,-5.318290,9.646576,-9.805054,-0.678227,2.752626,3.612923,-1.560336,-9.176110,-3.543447,5.668973,-4.969613,-3.926315],[0.525478,0.529728,4.641486,0.172718,2.951854,-8.424983,-6.033517,5.800919,1.856282,0.285505,-6.126751,-9.916697,-4.257193,3.707288,7.102500]],[[-4.608703,6.522552,8.476063,-1.121950,-9.389280,3.195694,-0.316001,1.853910,3.435017,-6.560264,7.320529,-3.924877,-4.845127,8.594632,2.687370],[6.630932,-4.018115,4.456965,-0.481609,-2.829719,9.089194,7.026374,8.543447,-4.824601,3.494848,9.567058,1.589433,6.542327,1.420704,5.272901],[0.295827,-3.927893,8.086768,7.516129,-8.179460,-5.766512,3.226969,2.259435,-8.929518,0.341031,-4.378020,-0.094517,4.255012,9.871592,2.197828]],[[0.996269,-5.965499,-3.340039,-6.463316,6.079074,3.508560,-3.711577,9.175699,-4.227409,4.444036,8.115636,-6.117554,3.522798,8.555269,-3.254426],[0.467715,-0.388540,-7.214506,8.406472,-7.522091,8.743304,-4.697084,3.194487,6.366368,-1.135158,4.305416,-3.797744,6.443399,3.363333,3.002665],[8.115992,-6.683911,-4.015387,-5.695643,2.969813,-2.921437,8.001151,-2.492787,-8.409468,-7.525323,1.940073,-1.448052,4.855022,3.253344,4.345109]],[[3.084457,-1.266805,-7.127599,-4.394417,-3.457204,5.785790,-1.321178,-7.506584,4.549181,-8.811615,3.962223,-9.907066,4.483484,5.794323,-8.222494],[0.747696,-9.643215,5.880899,-8.537298,9.850585,9.266000,7.803660,0.015168,3.012699,-3.426481,-8.980541,6.331146,-4.839284,9.839067,7.937440],[-1.569146,4.713229,-6.800958,3.065636,-2.057585,-2.616504,2.252120,0.312592,7.001683,-9.029273,-8.702927,8.364353,5.332149,-9.708084,9.101568]],[[-5.166139,5.110833,-1.591682,3.811884,-1.748848,9.045112,6.633140,9.714005,0.763681,8.176794,-0.881641,1.348402,1.306696,8.756001,0.967276],[-4.602525,-8.385570,3.999167,0.057636,-8.642015,-5.016897,-6.696946,9.617407,-4.987216,-6.511190,-0.758630,0.128817,-2.018890,-3.367512,-7.621739],[8.797113,2.831349,-0.592977,-6.728172,6.647517,-3.031592,-6.668761,-9.092746,-0.838370,2.760525,-8.374499,0.857054,4.443444,4.686831,-8.926658]],[[1.358905,-0.113569,8.816475,7.915441,-1.644850,1.170100,-9.732397,-5.012468,1.123951,1.620236,8.255685,-2.528369,9.461519,4.364302,7.557980],[-1.332602,8.508012,7.428361,-9.922926,-5.547482,-5.138270,2.013349,-3.959237,5.264090,-5.156753,-2.217498,-7.853060,-3.861102,-7.244806,-6.201557],[7.918745,-0.785489,1.065294,-5.975301,-1.191050,3.684709,-5.817806,8.223641,-3.963193,-9.058680,0.716422,-2.302900,1.092115,8.205811,-9.739768]],[[6.655854,-0.501465,-8.459058,7.585281,4.904310,-7.777849,-9.941377,9.575834,6.612585,-0.978863,-3.138156,-6.045882,-5.350611,-4.708336,1.456451],[4.723143,-4.622338,-3.897119,-0.883227,0.586490,5.555312,-9.600397,-9.413853,6.424367,6.033496,1.529343,1.930573,-4.732214,0.311131,4.244789],[-9.836788,0.920570,-3.948082,4.211749,-5.362585,1.692279,-9.893523,4.348502,6.249857,-3.376810,1.813158,3.772402,6.381080,-8.514623,-9.639514]],[[9.455411,-6.152606,9.015673,-1.199859,6.967598,-3.917484,-0.619914,-5.295226,8.324232,-0.676338,-8.179067,-4.502307,-2.506359,-3.925392,-2.599051],[-9.228103,7.404646,0.283484,-1.284088,6.930855,-1.576852,-2.641829,8.253543,-6.086501,-4.793539,-1.424701,-5.473049,-7.997662,3.531170,6.569866],[3.019534,8.082460,3.938776,-5.846119,0.869466,8.732964,8.609088,-4.612619,7.639852,1.295166,-3.885278,-2.317881,-4.880774,8.353125,5.293271]]], dtype = "float32")#candidate|14064|(13, 3, 15)|const|float32
uop_14065 = relay.acos(const_14064.astype('float32')) # shape=(13, 3, 15)
output = relay.Tuple([uop_14065,])
output2 = relay.Tuple([uop_14065,])
func_14073 = relay.Function([], output)
mod['func_14073'] = func_14073
mod = relay.transform.InferType()(mod)
mutated_mod['func_14073'] = func_14073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14073_call = mutated_mod.get_global_var('func_14073')
call_14074 = func_14073_call()
output = call_14074
func_14075 = relay.Function([], output)
mutated_mod['func_14075'] = func_14075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14073_call = mod.get_global_var('func_14073')
func_14075_call = mutated_mod.get_global_var('func_14075')
call_14151 = relay.TupleGetItem(func_14073_call(), 0)
call_14152 = relay.TupleGetItem(func_14075_call(), 0)
func_10246_call = mod.get_global_var('func_10246')
func_10248_call = mutated_mod.get_global_var('func_10248')
const_14155 = relay.const([[-9.248168,8.577844],[4.518592,-2.837549],[-1.345544,4.077475],[-9.323778,-9.562545],[3.725024,-6.476863],[-8.137758,-5.797803],[-1.600234,-1.604243],[3.848667,7.797252],[9.798117,9.485198],[-3.894877,6.455067],[-2.255270,6.739685],[-4.639290,-3.319345],[-0.977234,-0.611442],[9.890730,-4.745055]], dtype = "float32")#candidate|14155|(14, 2)|const|float32
call_14154 = func_10246_call(relay.reshape(const_14155.astype('float32'), [4, 7, 1]))
call_14156 = func_10246_call(relay.reshape(const_14155.astype('float32'), [4, 7, 1]))
output = relay.Tuple([call_14151,call_14154,const_14155,])
output2 = relay.Tuple([call_14152,call_14156,const_14155,])
func_14157 = relay.Function([], output)
mod['func_14157'] = func_14157
mod = relay.transform.InferType()(mod)
output = func_14157()
func_14158 = relay.Function([], output)
mutated_mod['func_14158'] = func_14158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14157_call = mod.get_global_var('func_14157')
func_14158_call = mutated_mod.get_global_var('func_14158')
call_14225 = relay.TupleGetItem(func_14157_call(), 2)
call_14226 = relay.TupleGetItem(func_14158_call(), 2)
output = call_14225
output2 = call_14226
func_14228 = relay.Function([], output)
mod['func_14228'] = func_14228
mod = relay.transform.InferType()(mod)
output = func_14228()
func_14229 = relay.Function([], output)
mutated_mod['func_14229'] = func_14229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14228_call = mod.get_global_var('func_14228')
func_14229_call = mutated_mod.get_global_var('func_14229')
call_14230 = func_14228_call()
call_14231 = func_14228_call()
output = relay.Tuple([call_14230,])
output2 = relay.Tuple([call_14231,])
func_14253 = relay.Function([], output)
mod['func_14253'] = func_14253
mod = relay.transform.InferType()(mod)
output = func_14253()
func_14254 = relay.Function([], output)
mutated_mod['func_14254'] = func_14254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14228_call = mod.get_global_var('func_14228')
func_14229_call = mutated_mod.get_global_var('func_14229')
call_14395 = func_14228_call()
call_14396 = func_14228_call()
func_8126_call = mod.get_global_var('func_8126')
func_8129_call = mutated_mod.get_global_var('func_8129')
var_14398 = relay.var("var_14398", dtype = "float32", shape = (1287,))#candidate|14398|(1287,)|var|float32
call_14397 = relay.TupleGetItem(func_8126_call(relay.reshape(var_14398.astype('float32'), [13, 9, 11])), 0)
call_14399 = relay.TupleGetItem(func_8129_call(relay.reshape(var_14398.astype('float32'), [13, 9, 11])), 0)
uop_14414 = relay.acosh(call_14397.astype('float32')) # shape=(13, 9, 11)
uop_14416 = relay.acosh(call_14399.astype('float32')) # shape=(13, 9, 11)
func_7590_call = mod.get_global_var('func_7590')
func_7593_call = mutated_mod.get_global_var('func_7593')
var_14429 = relay.var("var_14429", dtype = "float64", shape = (84,))#candidate|14429|(84,)|var|float64
call_14428 = func_7590_call(relay.reshape(var_14429.astype('float64'), [6, 14, 1]))
call_14430 = func_7590_call(relay.reshape(var_14429.astype('float64'), [6, 14, 1]))
func_14073_call = mod.get_global_var('func_14073')
func_14075_call = mutated_mod.get_global_var('func_14075')
call_14433 = relay.TupleGetItem(func_14073_call(), 0)
call_14434 = relay.TupleGetItem(func_14075_call(), 0)
output = relay.Tuple([call_14395,var_14398,uop_14414,call_14428,var_14429,call_14433,])
output2 = relay.Tuple([call_14396,var_14398,uop_14416,call_14430,var_14429,call_14434,])
func_14438 = relay.Function([var_14398,var_14429,], output)
mod['func_14438'] = func_14438
mod = relay.transform.InferType()(mod)
mutated_mod['func_14438'] = func_14438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14438_call = mutated_mod.get_global_var('func_14438')
var_14440 = relay.var("var_14440", dtype = "float32", shape = (1287,))#candidate|14440|(1287,)|var|float32
var_14441 = relay.var("var_14441", dtype = "float64", shape = (84,))#candidate|14441|(84,)|var|float64
call_14439 = func_14438_call(var_14440,var_14441,)
output = call_14439
func_14442 = relay.Function([var_14440,var_14441,], output)
mutated_mod['func_14442'] = func_14442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14073_call = mod.get_global_var('func_14073')
func_14075_call = mutated_mod.get_global_var('func_14075')
call_14473 = relay.TupleGetItem(func_14073_call(), 0)
call_14474 = relay.TupleGetItem(func_14075_call(), 0)
func_12124_call = mod.get_global_var('func_12124')
func_12129_call = mutated_mod.get_global_var('func_12129')
var_14477 = relay.var("var_14477", dtype = "float32", shape = (210,))#candidate|14477|(210,)|var|float32
var_14478 = relay.var("var_14478", dtype = "int16", shape = (1404,))#candidate|14478|(1404,)|var|int16
const_14479 = relay.const([9.262744,-2.586144,-1.153021,-6.002284,-6.449208,7.377584,7.327362,6.045825,9.177782,1.450362,-8.784751,-9.767435,-9.289728,-9.070043,-1.553060,-2.728178,9.804350,-1.110048,-1.769489,-6.919188,0.589853,5.788974,-9.190320,-9.661489,-2.379494,5.395922,-5.828242,-6.043985,-0.182199,-5.227088,-7.431559,-7.676290,-8.631385,9.304219,5.544503,6.445526,3.659978,-6.370137,6.632469,7.110546,-2.933195,-7.280217,-0.068849,7.117772,9.095806,8.086477,1.759047,-6.759164,3.093487,-7.897152,6.631142,0.683069,-0.940056,-8.229976,-5.110533,8.834686,-5.308583,2.833770,-1.726225,2.394402,2.612838,-1.127126,-1.171546,-6.509917,-7.156005,2.681504,-6.958768,8.379101,-2.245723,-4.776568,4.607470,1.216436,9.845185,7.943375,0.670120,4.377243,1.844492,7.582075,-8.083345,5.859927,-9.074720,5.513802,1.774146,7.656764,-5.121933,9.994127,-9.296777,-4.643820,1.941956,0.950810,-7.154923,7.137513,-4.402454,-0.534547,-2.322373,-9.755120,-8.613146,8.988615,-2.404967,8.533314,-3.700684,-5.626283,8.826836,-5.074785,-5.786537,1.329766,3.865360,6.934554,-5.186636,-8.702933,7.625819,1.512003,-9.984790,-9.337844,-0.172484,-8.259956,-4.509528,9.412100,3.202312,-3.398091,8.688187,-6.234013,4.375714,0.812533,0.176115,-3.188772,-9.997496,-7.706522,0.118623,4.370717,-2.064447,-0.852628,-6.432447,-2.420621,-2.063520,-7.774020,1.811784,-5.805535,-3.121439,-1.759424,6.869245,-3.273513,-5.505129,5.203791,6.618682,2.173592,-4.277797,-7.705448,1.749809,-4.418447,-2.922349,-0.707760,8.716965,-7.693671,-4.309575,-1.089997,8.398401,1.066651,4.124581,8.936183,9.055882,2.080677,7.984334,-9.284547,-1.991625,-8.647489,9.989506,-5.722375,2.726166,-3.568124,8.021709,2.494816,-8.848752,3.134347,0.237743,-0.157690,9.579023,-4.757474,-6.215069,-1.533161,1.581305,8.674997,9.652858,-5.929945,-5.043081,-4.067604,6.969468,-7.408173,-2.181867,9.053589,0.749820,-0.975897,6.540751,7.306728,2.069621,0.763717,-3.955929,-3.731812,-7.102161,-5.347426,5.356948,6.794424,-3.440040,-3.364664,9.870236,1.317449,-7.186487,2.067128,-1.030492,6.301046,-2.537439,7.208633,6.956829,-6.500042,-3.554779,-4.043703,1.869955,-2.647989,7.886014,-6.974410], dtype = "float32")#candidate|14479|(220,)|const|float32
var_14480 = relay.var("var_14480", dtype = "int64", shape = (546,))#candidate|14480|(546,)|var|int64
call_14476 = relay.TupleGetItem(func_12124_call(relay.reshape(var_14477.astype('float32'), [3, 7, 10]), relay.reshape(var_14478.astype('int16'), [9, 156]), relay.reshape(const_14479.astype('float32'), [220,]), relay.reshape(var_14480.astype('int64'), [546,]), ), 5)
call_14481 = relay.TupleGetItem(func_12129_call(relay.reshape(var_14477.astype('float32'), [3, 7, 10]), relay.reshape(var_14478.astype('int16'), [9, 156]), relay.reshape(const_14479.astype('float32'), [220,]), relay.reshape(var_14480.astype('int64'), [546,]), ), 5)
func_11364_call = mod.get_global_var('func_11364')
func_11367_call = mutated_mod.get_global_var('func_11367')
var_14483 = relay.var("var_14483", dtype = "float64", shape = (364,))#candidate|14483|(364,)|var|float64
var_14484 = relay.var("var_14484", dtype = "uint32", shape = (420,))#candidate|14484|(420,)|var|uint32
call_14482 = relay.TupleGetItem(func_11364_call(relay.reshape(var_14483.astype('float64'), [4, 7, 13]), relay.reshape(var_14484.astype('uint32'), [420,]), ), 2)
call_14485 = relay.TupleGetItem(func_11367_call(relay.reshape(var_14483.astype('float64'), [4, 7, 13]), relay.reshape(var_14484.astype('uint32'), [420,]), ), 2)
output = relay.Tuple([call_14473,call_14476,var_14477,var_14478,const_14479,var_14480,call_14482,var_14483,var_14484,])
output2 = relay.Tuple([call_14474,call_14481,var_14477,var_14478,const_14479,var_14480,call_14485,var_14483,var_14484,])
func_14486 = relay.Function([var_14477,var_14478,var_14480,var_14483,var_14484,], output)
mod['func_14486'] = func_14486
mod = relay.transform.InferType()(mod)
mutated_mod['func_14486'] = func_14486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14486_call = mutated_mod.get_global_var('func_14486')
var_14488 = relay.var("var_14488", dtype = "float32", shape = (210,))#candidate|14488|(210,)|var|float32
var_14489 = relay.var("var_14489", dtype = "int16", shape = (1404,))#candidate|14489|(1404,)|var|int16
var_14490 = relay.var("var_14490", dtype = "int64", shape = (546,))#candidate|14490|(546,)|var|int64
var_14491 = relay.var("var_14491", dtype = "float64", shape = (364,))#candidate|14491|(364,)|var|float64
var_14492 = relay.var("var_14492", dtype = "uint32", shape = (420,))#candidate|14492|(420,)|var|uint32
call_14487 = func_14486_call(var_14488,var_14489,var_14490,var_14491,var_14492,)
output = call_14487
func_14493 = relay.Function([var_14488,var_14489,var_14490,var_14491,var_14492,], output)
mutated_mod['func_14493'] = func_14493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14228_call = mod.get_global_var('func_14228')
func_14229_call = mutated_mod.get_global_var('func_14229')
call_14543 = func_14228_call()
call_14544 = func_14228_call()
func_3287_call = mod.get_global_var('func_3287')
func_3291_call = mutated_mod.get_global_var('func_3291')
const_14548 = relay.const([-9,-6,-5,-4,-2,8,10,2,5,6,10,5,-3,-2,-7,-9,-8,-3,-1,3,-7,-5,-8,-7,-8,10,-7,8,5,-8,-1,-1,4,-3,2,-8,6,7,4,-8,9,10,2,5,10,-2,-2,9,8,1,-7,-10,-4,-8,3,1,-3,-7,9,-2,7,1,8,7,3,7,-9,-4,4,-3,7,8,-5,4,-8,4,-2,-7,6,-8,2,-8,4,3,-3,6,10,-1,-10,-10,1,6,-10,6,6,4,3,8,5,5,10,1,7,7,-5,6,3,-3,-4,9,-5,10,7,5,-3,-4,-4,-3,7,6,6,-9,-5,-2,-1,3,-5,6,-2,8,3,-6,-8,-6,10,-8,8,-5,-2,-4,-1,-1,-9,-10,1,-6,-3,1,-3,6,-3,-2,-4,3,-6,-8,-3,5,9,-3,-5,-5,3,-8,5,2,10,8,-10,9,8,-5,8,3,5,-8,-6,9,-2,-6,2,-6,1,-8,5,-9,7,-3,3,-4,3,1,6,-7,-6,5,2,-4,-5,3,2,-2,5,-5,3,-9,3,6,-9,-8,-7,-6,-6,9,5,-3,2,-7,3,7,1,-2,7,6,10,-4,-8,-3,1,6,-4,2,-4,-4,10,5,-9,-8,5,-6,-7,-2,-1,9,-7,-5,-6,6,5,-9,1,-8,10,-9,-9,10,7,1,4,-9,7,-1,-10,-4,-7,2,6,-8,-4,-3,-4,-9,4,-7,9,1,-10,8,-9,9,-5,4,8,2,-9,-7,8,3,5,10,8,10,4,-1,8,1,-8,-7,-6,-10,-3,-9,-4,-1,-4,5,-2,1,-10,-3,10,-4,-8,7,-1,1,8,5,4,-3,8,-2,10,8,-6,10,6,6,-8,-10,-4,5,2,-3,5,-9,-1,-5,6,3,-6,-10,1,-6,3,-10,-8,-8,-4,-9,7,3,-10,-1,2,10,10,-8,-8,-10,10,-5,-2,9,3,4,-7,-10,-3,-3,6,3,-3,-5,-5,1,4,6,-8,1,-4,-3,-1,-9,-3,-1,6,-5,5,2,-4,9,-9,-3,9,-2,10,-7,-8,9,-9,-10,-4,-5,-4,3,10,-5,5,9,5,-1,5,-8,-2,-4,-7,7,-7,4], dtype = "uint32")#candidate|14548|(420,)|const|uint32
call_14547 = relay.TupleGetItem(func_3287_call(relay.reshape(const_14548.astype('uint32'), [10, 7, 6]), relay.reshape(const_14548.astype('uint32'), [10, 7, 6]), ), 1)
call_14549 = relay.TupleGetItem(func_3291_call(relay.reshape(const_14548.astype('uint32'), [10, 7, 6]), relay.reshape(const_14548.astype('uint32'), [10, 7, 6]), ), 1)
func_9929_call = mod.get_global_var('func_9929')
func_9932_call = mutated_mod.get_global_var('func_9932')
var_14569 = relay.var("var_14569", dtype = "float32", shape = (588,))#candidate|14569|(588,)|var|float32
call_14568 = relay.TupleGetItem(func_9929_call(relay.reshape(var_14569.astype('float32'), [14, 3, 14])), 0)
call_14570 = relay.TupleGetItem(func_9932_call(relay.reshape(var_14569.astype('float32'), [14, 3, 14])), 0)
func_14253_call = mod.get_global_var('func_14253')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_14575 = relay.TupleGetItem(func_14253_call(), 0)
call_14576 = relay.TupleGetItem(func_14254_call(), 0)
func_14253_call = mod.get_global_var('func_14253')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_14579 = relay.TupleGetItem(func_14253_call(), 0)
call_14580 = relay.TupleGetItem(func_14254_call(), 0)
func_7645_call = mod.get_global_var('func_7645')
func_7649_call = mutated_mod.get_global_var('func_7649')
const_14590 = relay.const([4.876386,2.337487,-8.878573,3.497969,6.658185,5.529225,-4.792052,-0.510407,6.709490,-6.857235,-4.702196,-9.673585,3.139782,9.504178,-4.602809,-0.054019,-0.159975,-7.543030,-0.656972,9.451457,-4.017802,0.873027,-5.700376,-2.039012,-9.027758,3.737578,-2.711391,0.402473,-0.069187,-0.036989,7.492517,-7.741656,-7.322727,-5.992295,-3.092819,-2.092187,-8.357389,-2.382453,4.693955,-8.105181,9.752005,-9.304831,8.892894,3.677677,-4.464583,2.332220,-5.697394,1.423934,-1.727167,5.785660,4.643996,9.197900,9.808985,-9.791088,6.820755,-3.049855,7.799867,-0.221778,2.148317,-6.078788,2.555478,3.875533,7.178535,-6.973796,4.922975,-8.183048,7.273031,-7.867738,6.678711,3.177168,-5.414274,-9.075687,2.081210,-4.629517,-2.861954,-2.057419,-9.995014,-4.808970,3.963123,1.625155,-8.344510,8.770263,-1.729567,1.713011,2.945942,-4.172652,-7.200664,0.389098,4.177036,-9.824115,-5.902859,5.298933,0.046237,-0.394967,-7.467441,3.384637,1.003790,-0.346484,-1.120758,-2.792952,-6.153807,3.814028,5.872256,-6.522023,6.397923,-2.599245,-4.454268,-4.146736,0.168647,-4.689305,9.112201,6.628851,-3.672850,-7.076602,5.339924,-7.727186,6.022139,-3.350993,-3.316160,0.503741,-3.239081,5.760624,0.066135,-7.890219,-8.878269,-6.362027,-5.010653,1.611635,7.829018,9.662468,-1.466801,-9.394433,-8.457965,-7.392733,-3.725645,-1.664790,6.400510,5.002842,0.787447,-7.259847,-8.414853,9.112576,-2.826946,8.121231,-9.283960,-0.373431,6.576277,-5.887268,7.435736,-6.796930,-1.764579,-3.855350,1.838299,-7.155895,9.453422,-6.994899,0.417987,-0.628037,-8.547105,9.650411,0.653534,5.829967,2.823090,-7.163204,-5.359101,-5.111116,9.209906,3.953187,-3.242475,0.817305,-6.973557,6.084347,-2.716699,1.858087,9.666137,7.104355,-4.848704,6.181134,6.445867,-8.334916,4.661428,-9.877237,-0.535964,0.672394,-2.924988,-1.646265,-6.465816,-1.608989,-7.780747,-7.149644,2.733752,-0.007826,-0.527434,0.349212,7.709488,-5.684557,-8.935935,8.797949,-6.160441,5.021782,6.057661,7.294082,3.213380,-0.597280,5.485854,3.960786,8.951348,-2.013180,-0.851747,4.713100], dtype = "float64")#candidate|14590|(210,)|const|float64
const_14591 = relay.const([-2,2,6,3,8,-4,-7,-7,-4,-10,-10,-6,-8,7,10,6,5,-8,-8,4,10,-2,-2,5,-5,-8,1,-3,10,7,-4,-2,3,-9,-2,4,-10,10,-5,-7,-9,5,-9,-2,-6,1,-2,-10,-4,3,-1,-9,-5,-2,-5,3,4,-5,-6,-3,6,4,-4,10,-5,-3,1,-9,2,-9,2,10,-9,10,10,10,5,3,-2,9,-7,6,-6,-4,-8,-5,4,8,-8,3,-2,-5,8,-6,2,-10,10,7,-2,-4,6,3,-3,-7,9,-3,2,-8,8,3,-1,-1,8,7,-8,10,-8,-4,-6,-4,-1,-8,6,5,1,-6,-2,3,4,2,9,-6,5,-10,2,-5,-2,6,-8,4,1,-4,-8,3,-7,3,-6,-4,10,-3,-9,-3,-3,7,-10,-3,-2,3,3,9,2,-7,1,-1,-7,-3,-5,5,7,-9,4,7,-8,3,10,-1,-6,-3,10,-9,-10,-1,-1,5,10,-5,6,10,4,-5,-7,-7,5,-1,-5,3,-5,10,-3,-3,9,-7,10,2,3,8,-6,-3,6,7,6,-5,-6,-8,2,-2,-1,-9,-6,-7,-8,9,2,6,-9,9,3,-8,-3,-8,10,-7,6,-2,-8,-1,5,-10,-3,-7,9,10,2,-3,-4,1,8,5,-5,-8,5,9,3,-9,8,-1,-3,-9,6,-9,2,6,-7,5,7,5,5,4,-5,-6,-10,-10,-5,8,-2,4,7,3,9,8,-1,8,8,6,4,8,7,6,8,5,-1,3,7,1,-4,-3,-3,3,-2,7,-2,-1,3,-3,1,1,7,7,-8,1,9,-8,-5,-4,-1,5,5,4,-5,-1,5,6,5,-7,6,-6,-3,7,-5,-7,3,-10,1,-8,-1,3,-10,9,6,8,-7,7,9,10,-7,10,2,-8,-6,-9,7,4,-3,-3,-2,-1,7,8,3,8,8,8,2,5,4,4,8,-9,4,1,4,2,9,-5,-2,2,5,-10,-8,4,10,3,7,-10,3,6,1,-9,1,-5,-1,3,-9,-2,9,-8,3,9,-5,-2,8,8,-7,4,-2,-1,5,6,8,-10,-3,7,4,-7,-5,-9,-8,-4,3,3,6,6,-9,-5,2,5,8,3,-10,-10,9,9,6,2,-9,5,-10,-7,5,5,9,-5,6,8,-8,2,-8,5,-4,3,4,1,9,3,3,-5,2,1,10,5,-10,5,9,1,-9,-1,2,-8,-1,7,3,-6,4,2,-7,-9,-7,4,-6,-1,1,9,5,4,-10,-2,5,-7,-7,2,-7,2,5,10,-3,8,7,7,5,-10,6,-6,-9,-9,-2,-2,-2,-5,-10,-2,-9,9,6,-8,9,3,-9,6,4,6,-8,6,-3,-1,-7,-8,-1,-10,2,7,-5,7,-1,-4,10,-2,-8,-10,-3,-8,4,-7,-2,4,-7,7,1,-6,9,-9,9,9,4,-2,2,7,3,-3,-1,1,5,-9,-4,-1,6,1,-5,-5,-10,8,-5,8,-9,7,5,9,7,-8,-5,-3,-1,6,-5,-7,-8,-6,9,2,-6,-9,6,3,-8,-4,2,-1,2,-10,-8,3,-1,-10,-5,-8,9,2,-7,-9,-7,-7,-2,3,8,10,-2,4,2,-4,4,7,-1,-1,5,-5,-6,-3,-3,-10,-2,4,5,-5,-2,5,-1,1,3,-2,5,3,2,-8,2,3,-2,8,-7,-6,4,-4,8,-8,-9,-1,10,4,10,6,-1,8,7,1,-10,4,-2,8,-4,-1,7,-7,-8,10,4,1,-4,-9,6,-7,-8,-2,-7,-10,-9,8,-5,-4,8,10,-9,-7,2,3,7,6,-1,8,1,1,-1,7,-3,-8,6,-3,10,7,6,-10,2,-8,6,-10,-4,-8,-1,-10,9,-5,7,-9,8,9,-8,4,-6,-2,10,1,5,8,6,2,7,10,7,-1,5,-8,-10,2,7,-8,6,-1,-9,-6,-5,2,-8,-6,-10,-10,8,8,10,-3,2,4,-1,8,3,6,-4,2,9,-7,-4,5,-2,-9,1,-1,-3,10,1,-5,3,2,10,-9,1,-9,10,-8,-5,7,1,8,5,10,-7,2,-6,5,-8,2,-8,-6,-3,3,3,5,-1,10,2,-4,4,-6,10,-4,-8,8,9,6,-8,1,2,7,-8,9,-8,-8,-9,-3,-10,7,-5,-3,1,-8,2,-2,5,8,-10,-5,2,-1,2,9,-2,9,5,4,3,7,-9,-10,10,-10,-6,9,10,8,5,-1,6,-4,4,-5,10,-2,10,-3,-1,3,8,3,1,10,-9,-2,-3,-5,6,1,1,5,7,-6,-3,-6,-10,-10,10,-6,3,3,-8,-10,-8,10,-6,5,-5,4,9,-2,10,-9,-4,-1,-4,-10,5,-7,-2,-4,-2,-6,1,6,1,-8,-9,-1,-3,9,-9,10,-10,-6,-5,-3,-3,-7,-10,-2,-10,1,-9,-4,9,10,4,-1,-8,-7,9,-2,-2,7,-2,2,-1,-5,9,1,-5,-5,2,3,3,4,1,-6,-7,-4,2,-4,3,3,1,10,-4,4,1,7,7,-7,1,3,4,8,-5,1,4,-10,8,2,4,-10,-5,-10,2,3,1,-3,1,-3,6,4,5,-6,3,5,-3,-6,-3,3,4,-9,9,-9,3,-9,-3,-10,7,1,3,-9,2,7,2,1,5,10,-1,-6,-1,5,10,-4,3,-8,3,5,5,-1,3,2,1,1,10,-10,4,7,-3,10,-4,2,-8,-3,10,-9,-5,10,4,9,9,-7,5,7,-2,-5,5,-6,-6,-5,2,-1,4,2,-3,2,-10,-6,-10,4,2,-8,7,-10,-2,9,-7,-10,2,-9,-3,-10,9,-8,1,-10,-1,9,-4,-1,4,-2,-10,3,4,-8,4,-10,6,-1,1,-9,10,10,-7,-4,-3,-5,9,-7,-2,10,5,-9,7,9,1,-10,-5,7,-5,4,-7,1,9,-9,-4,-6,-10,-1,5,4,-5,-9,9,4,-6,2,-1,9,2,8,-10,7,1,6,-6,-4,-7,5,8,1,-10,-9,-9,-1,-10,-9,5,-8,-1,-6,5,2,-2,9,6,8,-5,9,5,7,8,6,9,4,6,-1,-10,4,-9,4,5,3,6,5,1,9,-5,5,-8,-8,-8,7,1,10,6,-5,-5,-2,2,6,-9,-3,9,2,10,4,-8,-6,2,-1,1,9,6,-8,-1,2,-9,-8,-4,8,10,-1,-10,-9,2,-3,8,8,-5,2,9,6,8,8,4,-7,-7,5,5,2,-6,10,-6,7,5,7,-1,3,9,-3,-9,-9,9,6,8,1,2,7,2,-9,-3,-2,-9,6,-8,1,9,6,4,4,-9,-7,8,8,9,-8,4,-7,-5,-1,3,-2,3,-2,1,10,-1,-2,-2,9,-8,2,-7,4,-5,4,-10,10,-8,2,-6,-1,9,6,-6,3,-3,5,-5,1,8,7,4,3,10,3,-8,-5,-10,10,-7,9,7,10,-6,3,-8,4,-8,6,-4,3,3,-1,-10,-10,-4,-9,-6,-7,9,8,10,1,-1,-5,-6,-7,8,-4,8,5,5,-5,2,3,1,1,5,9,-9,-9,5,-3,-3,-3,-3,5,2,-8,3,8,-3,7,-2,-4,-3,5,-10,-2,7,5,2,5,3,10,5,2,-10,-7,-5,3,-3,-5,9,5,-1,-4,-2,10,-4,-1], dtype = "int16")#candidate|14591|(1404,)|const|int16
call_14589 = relay.TupleGetItem(func_7645_call(relay.reshape(const_14590.astype('float64'), [14, 15, 1]), relay.reshape(const_14591.astype('int16'), [1, 1404]), ), 0)
call_14592 = relay.TupleGetItem(func_7649_call(relay.reshape(const_14590.astype('float64'), [14, 15, 1]), relay.reshape(const_14591.astype('int16'), [1, 1404]), ), 0)
output = relay.Tuple([call_14543,call_14547,const_14548,call_14568,var_14569,call_14575,call_14579,call_14589,const_14590,const_14591,])
output2 = relay.Tuple([call_14544,call_14549,const_14548,call_14570,var_14569,call_14576,call_14580,call_14592,const_14590,const_14591,])
func_14593 = relay.Function([var_14569,], output)
mod['func_14593'] = func_14593
mod = relay.transform.InferType()(mod)
var_14594 = relay.var("var_14594", dtype = "float32", shape = (588,))#candidate|14594|(588,)|var|float32
output = func_14593(var_14594)
func_14595 = relay.Function([var_14594], output)
mutated_mod['func_14595'] = func_14595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14253_call = mod.get_global_var('func_14253')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_14597 = relay.TupleGetItem(func_14253_call(), 0)
call_14598 = relay.TupleGetItem(func_14254_call(), 0)
output = relay.Tuple([call_14597,])
output2 = relay.Tuple([call_14598,])
func_14611 = relay.Function([], output)
mod['func_14611'] = func_14611
mod = relay.transform.InferType()(mod)
mutated_mod['func_14611'] = func_14611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14611_call = mutated_mod.get_global_var('func_14611')
call_14612 = func_14611_call()
output = call_14612
func_14613 = relay.Function([], output)
mutated_mod['func_14613'] = func_14613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14253_call = mod.get_global_var('func_14253')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_14704 = relay.TupleGetItem(func_14253_call(), 0)
call_14705 = relay.TupleGetItem(func_14254_call(), 0)
output = call_14704
output2 = call_14705
func_14709 = relay.Function([], output)
mod['func_14709'] = func_14709
mod = relay.transform.InferType()(mod)
mutated_mod['func_14709'] = func_14709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14709_call = mutated_mod.get_global_var('func_14709')
call_14710 = func_14709_call()
output = call_14710
func_14711 = relay.Function([], output)
mutated_mod['func_14711'] = func_14711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14157_call = mod.get_global_var('func_14157')
func_14158_call = mutated_mod.get_global_var('func_14158')
call_14712 = relay.TupleGetItem(func_14157_call(), 2)
call_14713 = relay.TupleGetItem(func_14158_call(), 2)
output = call_14712
output2 = call_14713
func_14740 = relay.Function([], output)
mod['func_14740'] = func_14740
mod = relay.transform.InferType()(mod)
mutated_mod['func_14740'] = func_14740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14740_call = mutated_mod.get_global_var('func_14740')
call_14741 = func_14740_call()
output = call_14741
func_14742 = relay.Function([], output)
mutated_mod['func_14742'] = func_14742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14073_call = mod.get_global_var('func_14073')
func_14075_call = mutated_mod.get_global_var('func_14075')
call_14746 = relay.TupleGetItem(func_14073_call(), 0)
call_14747 = relay.TupleGetItem(func_14075_call(), 0)
output = call_14746
output2 = call_14747
func_14748 = relay.Function([], output)
mod['func_14748'] = func_14748
mod = relay.transform.InferType()(mod)
output = func_14748()
func_14749 = relay.Function([], output)
mutated_mod['func_14749'] = func_14749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14073_call = mod.get_global_var('func_14073')
func_14075_call = mutated_mod.get_global_var('func_14075')
call_14805 = relay.TupleGetItem(func_14073_call(), 0)
call_14806 = relay.TupleGetItem(func_14075_call(), 0)
func_634_call = mod.get_global_var('func_634')
func_637_call = mutated_mod.get_global_var('func_637')
var_14817 = relay.var("var_14817", dtype = "float32", shape = (220,))#candidate|14817|(220,)|var|float32
call_14816 = relay.TupleGetItem(func_634_call(relay.reshape(var_14817.astype('float32'), [10, 11, 2]), relay.reshape(var_14817.astype('float32'), [10, 11, 2]), ), 0)
call_14818 = relay.TupleGetItem(func_637_call(relay.reshape(var_14817.astype('float32'), [10, 11, 2]), relay.reshape(var_14817.astype('float32'), [10, 11, 2]), ), 0)
output = relay.Tuple([call_14805,call_14816,var_14817,])
output2 = relay.Tuple([call_14806,call_14818,var_14817,])
func_14821 = relay.Function([var_14817,], output)
mod['func_14821'] = func_14821
mod = relay.transform.InferType()(mod)
var_14822 = relay.var("var_14822", dtype = "float32", shape = (220,))#candidate|14822|(220,)|var|float32
output = func_14821(var_14822)
func_14823 = relay.Function([var_14822], output)
mutated_mod['func_14823'] = func_14823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14157_call = mod.get_global_var('func_14157')
func_14158_call = mutated_mod.get_global_var('func_14158')
call_14943 = relay.TupleGetItem(func_14157_call(), 1)
call_14944 = relay.TupleGetItem(func_14158_call(), 1)
func_14157_call = mod.get_global_var('func_14157')
func_14158_call = mutated_mod.get_global_var('func_14158')
call_14945 = relay.TupleGetItem(func_14157_call(), 1)
call_14946 = relay.TupleGetItem(func_14158_call(), 1)
func_6800_call = mod.get_global_var('func_6800')
func_6804_call = mutated_mod.get_global_var('func_6804')
var_14969 = relay.var("var_14969", dtype = "bool", shape = (24, 22))#candidate|14969|(24, 22)|var|bool
const_14970 = relay.const([5,8,-4,-5,-6,3,2,-2,-1,-9,-7,-10,5,7,8,-1,-7,-10,-5,-1,7,4,7,-10,-9,5,-5,8,-10,2,-6,-1,-5,-3,8,-3,9,6,3,6,-6,7,-5,-1,-3,-3,7,-9,4,3,5,7,-3,-10,1,-10,7,8,6,9,2,8,7,-2,-9,-3,10,10,4,-10,8,-2,9,8,-1,5,-10,-5,-10,8,-1,-6,10,6,10,9,-6,-4,2,10,-1,-9,6,8,10,-5,-4,3,1,-7,5,-8,8,-8,5,6,-3,-7,-8,4,10,8,-4,-9,2,5,-4,8,6,2,4,-9,2,5,-2,7,-10,-7,8,9,-4,7,9,7,1,-1,9,3,8,1,-7,-2,-5,-1,-7,-5,7,8,-7,-5,6,5,-6,7,6,-1,-8,10,-4,-10,-3,3,-7,8,-5,4,7,-9,8,6,-5,7,-2,1,-9,-8,-6,-4,3,6,-5,1,2,6,7,-5,8,8,-10,5,-9,-4,5,7,2,-8,-6,8,9,7,5,-8,6,3,4,5,-5,10,1,-10,3,-9,-6,-6,-2,-1,-6,1,7,-8,-4,-6,-6,-10,6,-7,7,7,-2,8,-9,-2,-10,-7,-7,-9,9,-1,-4,1,1,6,-3,-1,7,10,2,10,-5,10,5,-4,-5,-9,-7,8,8,8,-8,-6,-10,-2,8,-6,-1,4,4,-10,4,1,-2,9,-4,1,8,8,6,2,-1,9,-3,-10,1,-9,1,-6,8,3,4,3,-1,-2,8,-1,4,-3,-2,-7,4,10,5,-8,-3,4,-3,1,-7,-1,9,-6,-1,-10,-3,-6,5,2,-1,-5,-1,2,-8,-10,-6,-10,2,-7,-6,-3,-8,-3,6,2,-8,-4,6,5,-8,6,3,-10,3,-5,8,5,-1,-6,-6,6,5,-4,-5,2,-1,1,6,8,-1,-6,5,5,-2,4,-1,-5,-10,5,8,-3,8,5,-3,5,8,-5,5,-10,2,8,-6,-10,-1,-6,-4,8,-10,8,-5,-9,6,-7,-5,9,-3,-3,-9,-7,-7,9,-1,5,-9,-5,8,9,-10,-5,5,2,-3,1,7,-2,3,6,-8,3,6,4,-4,9,9,-8,-10,-6,-7,-4,-5,9,-8,9,-9,-5,-2,10,2,-9,5,-9,10,-9,10,-3,2,10,8,7,-2,2,-3,-10,-2,-8,-8,4,-10,-7,10,5,2,1,-5,-7,3,2,2,1,-1,-2,5,1,3,-8,-9,-3,10,-3,6,-3,1,-5,7,8,-6,-9,8,-8,7,4,-3,-7,2,-10,-1,-9,8,5,3,-3,6,2,1,5,-8,-6,-5,-5,-4,-9,-10,7,-4,3,-6,6,10,5,8,3,-8,-8,-1,-4,-10,8,-1,7,-7,-3,-9,-4,7,-4,9,10,4,4,2,8,3,1,-3,1,9,3,-5,8,-6,4,10,7,-5,-9,3,9,5,1,-10,-8,-8,-8,-9,4,1,-5,3,4,4,-5,3,2,7,8,6,6,-8,-9,-3,4,-3,4,10,-6,-3,1,6,-4,7,-8,-7,-8,-1,1,2,-7,-4,-2,10,1,8,9,-5,7,-4,-6,-1,5,-3,-7,4,1,6,-4,-1,2,-7,3,6,6,9,1,6,4,-2,6,5,-4,1,9,-3,1,-4,5,-6,-9,3,-5,-6,10,-9,4,4,-5,5,4,7,-9,-2,10,-5,3,1,-9,-6,-4,5,-9,7,-3,9,2,5,-6,6,-4,-9,9,4,6,6,7,8,-2,1,9,7,6,1,-10,2,-5,3,-8,1,9,3,-9,-1,8,-10,-1,-8,-10,1,-5,-4,-1,-6,5,4,-5,1,10,8,-5,-4,-5,3,1,-3,-6,-9,-7,-9,-2,-6,10,4,-1,-7,-9,1,5,-7,-10,5,1,-7,8,-1,-9,-1,4,10,-6,-2,-9,-8,8,3,10,-8,-3,-9,10,-3,-7,-9,-10,8,7,-2,2,-3,9,-10,5,10,-2,-8,9,1,-8,10,-1,-3,-10,-7,6,5,-7,2,3,-9,-3,5,-8,1,-1,3,1,10,-2,-4,-6,-4,3,4,-10,-9,10,6,-4,-6,-7,-9,-7,-10,6,9,-2,-7,-9,-1,4,1,-7,3,-3,8,-10,-10,6,7,-5,-5,7,4,-3,-2,-8,-10,-1,8,-2,8,3,-8,-10,-2,1,-6,9,4,-8,8,1,-10,-1,-8,5,4,4,9,-8,2,8,10,7,-1,2,10,-1,10,1,6,4,5,3,3,-5,-5,-3,2,8,-7,-7,8,9,10,5,-5,-6,-6,-4,-4,-6,-4,3,10,-1,4,4,-6,9,3,3,-3,-10,-10,2,5,-3,8,5,9,-5,-4,6,-3,7,1,6,1,-4,2,6,-3,-6,-5,9,5,-9,-2,-10,-10,-3,-8,-4,6,-9,4,-8,4,-10,-5,5,2,10,8,10,-8,10,3,5,4,2,1,6,5,6,-4,9,-4,-1,10,2,-4,6,-6,9,-8,9,10,-5,-3,3,4,5,-3,-4,-8,3,-9,-9,9,-7,8,6,-3,-3,4,6,-9,9,7,-7,8,-9,6,-3,8,3,6,-6,-10,5,-6,-5,-2,-9,8,6,-3,-4,-2,5,7,-8,7,3,-2,5,-9,-2,-5,-2,6,-8,10,7,8,-4,10,-9,-5,-6,3,6,10,-7,-1,-7,-4,6,-6,7,-7,-1,2,-5,4,-5,-1,-1,1,7,6,8,6,3,1,7,3,-4,-6,4,-10,-9,2,-3,9,-4,1,-4,-8,-10,8,-4,3,-6,8,-3,8,9,-3,10,10,6,6,10,-8,2,10,-7,-5,-6,-10,3,-8,-8,7,-4,2,10,-9,-3,-3,-2,-10,-7,-9,-9,-9,-7,-7,9,-2,2,-2,-3,3,7,8,10,-8,4,10,-8,-8,-8,-9,10,2,7,-4,-5,4,-4,1,2,-1,-9,-10,9,-2,-4,6,4,7,9,10,8,-6,-8,-6,-10,-7,-7,-4,6,3,-6,-5,4,10,3,9,-5,2,4,4,-5,3,-7,-6,2,2,-8,-6,10,8,-7,-3,-2,8,2,-1,2,-9,-10,1,-6,-8,1,-9,-4,-2,-5,-3,-1,4,2,2,-9,2,-8,1,-5,10,-5,-7,-7,-9,-6,-1,5,2,-1,3,7,-1,-10,9,-1,3,10,-6,9,-1,-10,-1,8,-6,8,-10,9,-10,-2,-8,9,-1,-3,8,-4,6,3,-3,-3,-1,10,-5,-1,-8,3,-9,7,-1,-7,-2,-2,-7,10,-6,-8,-1,8,-5,-1,5,-9,4,4,-6,-6,4,-1,-3,-10,1,7,4,9,6,4,-2,6,1,-1,3,-9,5,9,-8,-8,6,-2,3,-2,9,-2,1,7,10,-10,7,-1,9,4,-8,6,-10,-4,10,-3,4,-10,-5,-8,8,7,9,-2,5,-6,8,7,-2,2,9,-1,-1,7,-1,-1,2,4,4,-10,2,4,-9,10,3,3,7,2,-6,-4,-5,6,10,9,-6,7,-6,-9,-3,6,9,6,5,4,9,8,10,1,4,8,-2,9,5,3,-5,3,-8,9,-7,5,-8,9,-7,-2,4,-2,-4,-2,-10,-6,-4,10,8,-7,2,-2,-7,2,3,4,3,-4,10,3,-1,-5,-10,10,6,-4,1,1,-8,1,-7,1,-2,5,8,-2,-1,-7,3,8,7,8], dtype = "int16")#candidate|14970|(1404,)|const|int16
call_14968 = relay.TupleGetItem(func_6800_call(relay.reshape(var_14969.astype('bool'), [12, 4, 11]), relay.reshape(var_14969.astype('bool'), [12, 4, 11]), relay.reshape(const_14970.astype('int16'), [1404,]), ), 0)
call_14971 = relay.TupleGetItem(func_6804_call(relay.reshape(var_14969.astype('bool'), [12, 4, 11]), relay.reshape(var_14969.astype('bool'), [12, 4, 11]), relay.reshape(const_14970.astype('int16'), [1404,]), ), 0)
output = relay.Tuple([call_14943,call_14945,call_14968,var_14969,const_14970,])
output2 = relay.Tuple([call_14944,call_14946,call_14971,var_14969,const_14970,])
func_14973 = relay.Function([var_14969,], output)
mod['func_14973'] = func_14973
mod = relay.transform.InferType()(mod)
var_14974 = relay.var("var_14974", dtype = "bool", shape = (24, 22))#candidate|14974|(24, 22)|var|bool
output = func_14973(var_14974)
func_14975 = relay.Function([var_14974], output)
mutated_mod['func_14975'] = func_14975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14740_call = mod.get_global_var('func_14740')
func_14742_call = mutated_mod.get_global_var('func_14742')
call_15136 = func_14740_call()
call_15137 = func_14740_call()
output = call_15136
output2 = call_15137
func_15146 = relay.Function([], output)
mod['func_15146'] = func_15146
mod = relay.transform.InferType()(mod)
mutated_mod['func_15146'] = func_15146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15146_call = mutated_mod.get_global_var('func_15146')
call_15147 = func_15146_call()
output = call_15147
func_15148 = relay.Function([], output)
mutated_mod['func_15148'] = func_15148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14709_call = mod.get_global_var('func_14709')
func_14711_call = mutated_mod.get_global_var('func_14711')
call_15167 = func_14709_call()
call_15168 = func_14709_call()
func_6800_call = mod.get_global_var('func_6800')
func_6804_call = mutated_mod.get_global_var('func_6804')
const_15170 = relay.const([True,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,True,False,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False], dtype = "bool")#candidate|15170|(528,)|const|bool
const_15171 = relay.const([[-10,-4],[2,-6],[7,9],[10,9],[-1,-3],[6,-4],[4,2],[5,8],[-4,-10],[8,-5],[5,-9],[8,-9],[7,-7],[1,-5],[-9,-2],[-9,-2],[3,-9],[-7,-3],[10,7],[4,-6],[7,5],[-5,4],[-9,10],[7,1],[3,-10],[-6,-3],[9,-4],[-8,-5],[4,-5],[-10,2],[-5,7],[4,3],[-10,10],[-6,-6],[-4,9],[3,-9],[3,5],[-2,5],[1,3],[-2,5],[-7,-1],[7,-1],[8,-3],[3,-9],[7,-4],[-2,10],[10,1],[8,-5],[-2,-2],[-4,1],[3,4],[-7,4],[6,5],[-4,-3],[6,8],[1,-3],[-10,3],[-7,5],[-10,6],[1,-1],[6,6],[1,-8],[-5,-3],[10,1],[-2,-1],[1,-7],[-4,-8],[2,1],[-5,2],[6,5],[4,10],[-5,-1],[7,3],[9,-9],[-4,-7],[6,6],[5,-7],[6,4],[9,6],[-7,10],[3,2],[-5,3],[5,6],[8,-3],[10,7],[4,-9],[-7,7],[-4,-8],[2,8],[-8,-7],[-3,-6],[-8,5],[3,-5],[-5,-7],[1,-4],[3,-3],[1,-4],[-2,-4],[5,5],[3,1],[-2,-10],[-3,9],[3,1],[7,-2],[-3,7],[-7,-10],[3,8],[-5,-1],[-7,6],[-7,4],[-8,9],[8,4],[-10,-7],[-4,-1],[-4,4],[-8,-8],[5,5],[-7,-4],[-5,-2],[6,4],[-7,-3],[2,9],[-3,-3],[7,7],[5,3],[-2,-9],[-2,10],[5,6],[-7,-4],[-4,-4],[3,9],[-9,1],[8,-6],[-5,-7],[-5,6],[1,3],[-2,-8],[7,1],[-9,1],[7,-4],[8,-5],[-6,-1],[-7,9],[1,-9],[-9,7],[-1,6],[-1,10],[9,-4],[5,-1],[10,-1],[10,-9],[4,-4],[-5,6],[3,5],[-9,3],[10,-6],[-5,-7],[-10,3],[10,3],[-10,-4],[-9,-10],[-2,-6],[2,10],[5,1],[4,6],[-8,-4],[-3,-2],[-3,9],[-7,-4],[-5,-4],[8,-3],[10,2],[3,8],[6,-10],[8,-1],[8,-4],[-8,8],[9,-2],[-5,-1],[-8,9],[-2,3],[-10,7],[6,-2],[10,1],[-6,-3],[8,3],[10,-8],[-6,10],[-7,-8],[-7,-6],[4,5],[-4,4],[-5,5],[2,-9],[-2,1],[-8,-8],[3,2],[10,10],[6,10],[4,-9],[2,-4],[-2,7],[4,1],[-8,-6],[4,8],[6,10],[5,-9],[5,-10],[2,1],[9,-5],[5,-4],[7,-3],[-6,7],[-1,1],[6,-7],[-9,-7],[-10,-4],[-6,9],[-7,4],[1,-6],[-10,-10],[-1,-9],[2,-9],[-10,2],[5,-9],[5,2],[-1,9],[-8,2],[10,-1],[4,8],[-5,-8],[3,6],[-8,-1],[-3,6],[-3,-7],[-1,-9],[10,2],[7,1],[-10,8],[1,-3],[7,1],[-9,5],[3,3],[10,7],[-9,7],[2,9],[-6,-5],[-8,-5],[2,-6],[-6,-3],[2,5],[7,5],[2,3],[9,3],[-8,4],[9,-3],[-7,4],[-2,2],[-4,-6],[-10,6],[-3,5],[-10,7],[1,5],[1,10],[1,-1],[10,4],[2,-2],[3,6],[8,9],[-4,-7],[-8,-2],[4,-6],[6,7],[3,-10],[3,1],[2,5],[-1,-8],[-9,-9],[-9,7],[-4,8],[2,-6],[5,4],[-9,-8],[-2,-1],[-5,9],[3,-2],[-8,-4],[4,2],[5,3],[-5,-2],[1,5],[10,8],[2,1],[5,8],[4,8],[3,-6],[-2,-10],[7,1],[-1,3],[4,-1],[1,2],[5,1],[-1,9],[-1,-4],[-3,1],[-8,8],[-1,-3],[2,-3],[-5,-9],[6,-2],[-1,3],[-4,-6],[-3,7],[-1,1],[5,9],[9,2],[-7,-6],[3,10],[-9,-7],[-9,-3],[1,-4],[-4,4],[-10,-7],[-5,2],[-2,-2],[6,-10],[-6,1],[-1,8],[4,-4],[-6,8],[-3,4],[5,-9],[4,-3],[-5,9],[-3,7],[-7,-8],[6,7],[-4,9],[-9,-5],[-10,-3],[-6,-7],[3,-10],[-8,-2],[1,-6],[-4,2],[-8,-3],[-5,3],[-3,-2],[-5,9],[8,-6],[-6,1],[-6,6],[-10,8],[-1,-6],[1,4],[8,-4],[6,2],[-5,-8],[5,-2],[-8,3],[-7,5],[3,-6],[1,-10],[-3,-1],[-2,-1],[-1,9],[2,-1],[10,-8],[4,-6],[-5,1],[10,6],[-8,4],[-1,-6],[-8,10],[-6,10],[-2,4],[-10,-5],[5,-2],[7,-10],[-4,-2],[9,-7],[5,-7],[-6,-9],[-3,-6],[-5,1],[-7,5],[-10,9],[-7,-1],[1,5],[5,6],[-9,4],[8,-9],[3,1],[3,-3],[8,9],[3,6],[-7,-9],[-3,8],[8,5],[1,8],[-4,-3],[-4,-9],[8,-2],[7,-4],[-8,-9],[-8,4],[8,-1],[-5,-5],[8,5],[-4,-6],[2,3],[3,6],[-10,2],[-3,-3],[8,-1],[5,-10],[-4,4],[-9,8],[8,3],[-9,-5],[-7,7],[5,-2],[-6,-4],[1,-1],[-10,10],[-7,3],[2,-9],[6,-9],[10,4],[6,6],[10,-2],[-5,3],[9,-5],[6,4],[-5,-8],[-6,5],[-3,-1],[4,2],[9,-5],[6,-2],[-5,-3],[-6,-6],[9,-3],[1,1],[8,4],[9,-7],[9,-7],[-2,-1],[-5,-8],[3,-3],[10,-7],[5,-8],[10,-4],[-9,9],[3,-2],[-4,-3],[-9,-1],[5,-3],[9,9],[-8,6],[8,-8],[1,2],[5,10],[-8,8],[4,-8],[-3,-7],[4,8],[-10,1],[6,-2],[7,4],[9,-1],[9,-4],[1,3],[6,-8],[-3,-2],[5,-10],[3,10],[7,3],[-10,-4],[-8,-1],[2,-2],[-1,9],[-1,6],[6,-6],[9,10],[2,1],[-10,8],[-3,6],[10,-6],[-2,-6],[7,6],[-7,10],[-8,1],[4,9],[-6,3],[-7,-7],[-8,-9],[-9,1],[6,-7],[10,10],[-8,8],[-2,-9],[8,-10],[-10,4],[-1,10],[8,3],[-9,-9],[-10,8],[10,1],[7,-2],[3,-1],[-10,-2],[-8,10],[4,-1],[6,3],[-9,-3],[1,2],[-5,2],[-8,-10],[8,9],[4,1],[5,-10],[-2,-8],[-6,-1],[-6,-4],[9,10],[8,6],[-3,1],[6,-5],[4,3],[-8,8],[-1,-10],[3,-1],[-9,10],[4,5],[-10,-7],[8,7],[-7,7],[-1,-3],[3,-1],[-7,-7],[-5,6],[-2,7],[7,8],[5,-7],[-6,-2],[-7,-9],[-8,7],[5,2],[2,1],[8,7],[1,-1],[1,-3],[-2,5],[-1,10],[-7,5],[-10,3],[-4,7],[2,9],[9,4],[-8,8],[3,9],[-8,-1],[7,-6],[-2,10],[-3,10],[-1,9],[-1,-10],[9,10],[3,-5],[-10,5],[-2,-6],[-2,-2],[1,10],[-3,2],[3,6],[3,-5],[-7,5],[-7,-7],[-3,-3],[7,-10],[7,2],[3,7],[-9,-10],[-9,7],[3,3],[4,9],[3,2],[7,-2],[-4,-6],[10,2],[6,-2],[-7,9],[10,-10],[-2,-2],[2,4],[-8,4],[3,-8],[5,2],[4,-4],[-2,-10],[5,-7],[-10,-1],[-2,2],[3,3],[-9,-9],[-3,-6],[5,-7],[-3,1],[9,-4],[-6,-3],[-1,-10],[4,8],[-4,-6],[8,-5],[1,1],[-9,1],[-10,-10],[1,-9],[-10,-5],[-4,-8],[2,7],[-7,6],[-2,-2],[-1,10],[-10,-10],[-6,3],[9,10],[3,-2],[-1,4],[9,6],[6,4],[-2,9],[-7,-3],[9,6],[-4,-1],[-4,1],[-2,-3],[-4,2],[-8,-9],[3,2],[-10,-2],[3,-7],[6,-3],[3,-8],[-8,3],[10,5],[-4,-8],[-4,-8],[9,5],[7,8],[-2,-6],[6,7],[4,7],[-7,-4],[9,-9],[-6,9],[-6,5],[6,9],[-6,-4],[-8,6],[3,8],[8,-3],[7,1],[-9,-7],[5,-10],[-7,3],[-5,-6],[8,-7],[-9,-10],[-8,-5],[-3,8],[-7,8],[-7,6],[-7,-9],[-4,5],[9,2],[6,7],[3,3],[-10,-9],[-6,-10],[-7,-8],[5,-7],[4,-2],[4,3],[4,-8],[-3,2],[-1,-10],[-9,-9],[7,1],[7,-1],[-1,-4],[-7,-7],[-6,-7],[-7,10],[-3,5],[1,10],[-3,1],[10,1],[-7,6],[-1,-4],[-1,5]], dtype = "int16")#candidate|15171|(702, 2)|const|int16
call_15169 = relay.TupleGetItem(func_6800_call(relay.reshape(const_15170.astype('bool'), [12, 4, 11]), relay.reshape(const_15170.astype('bool'), [12, 4, 11]), relay.reshape(const_15171.astype('int16'), [1404,]), ), 0)
call_15172 = relay.TupleGetItem(func_6804_call(relay.reshape(const_15170.astype('bool'), [12, 4, 11]), relay.reshape(const_15170.astype('bool'), [12, 4, 11]), relay.reshape(const_15171.astype('int16'), [1404,]), ), 0)
func_11364_call = mod.get_global_var('func_11364')
func_11367_call = mutated_mod.get_global_var('func_11367')
var_15185 = relay.var("var_15185", dtype = "float64", shape = (364,))#candidate|15185|(364,)|var|float64
var_15186 = relay.var("var_15186", dtype = "uint32", shape = (5, 84))#candidate|15186|(5, 84)|var|uint32
call_15184 = relay.TupleGetItem(func_11364_call(relay.reshape(var_15185.astype('float64'), [4, 7, 13]), relay.reshape(var_15186.astype('uint32'), [420,]), ), 2)
call_15187 = relay.TupleGetItem(func_11367_call(relay.reshape(var_15185.astype('float64'), [4, 7, 13]), relay.reshape(var_15186.astype('uint32'), [420,]), ), 2)
func_6800_call = mod.get_global_var('func_6800')
func_6804_call = mutated_mod.get_global_var('func_6804')
call_15191 = relay.TupleGetItem(func_6800_call(relay.reshape(const_15170.astype('bool'), [12, 4, 11]), relay.reshape(call_15169.astype('bool'), [12, 4, 11]), relay.reshape(const_15171.astype('int16'), [1404,]), ), 0)
call_15192 = relay.TupleGetItem(func_6804_call(relay.reshape(const_15170.astype('bool'), [12, 4, 11]), relay.reshape(call_15169.astype('bool'), [12, 4, 11]), relay.reshape(const_15171.astype('int16'), [1404,]), ), 0)
bop_15209 = relay.equal(call_15169.astype('bool'), relay.reshape(call_15191.astype('bool'), relay.shape_of(call_15169))) # shape=(12, 4, 11)
bop_15212 = relay.equal(call_15172.astype('bool'), relay.reshape(call_15192.astype('bool'), relay.shape_of(call_15172))) # shape=(12, 4, 11)
func_12281_call = mod.get_global_var('func_12281')
func_12286_call = mutated_mod.get_global_var('func_12286')
var_15219 = relay.var("var_15219", dtype = "uint64", shape = ())#candidate|15219|()|var|uint64
var_15220 = relay.var("var_15220", dtype = "uint64", shape = (288,))#candidate|15220|(288,)|var|uint64
var_15221 = relay.var("var_15221", dtype = "int64", shape = (546,))#candidate|15221|(546,)|var|int64
var_15222 = relay.var("var_15222", dtype = "int64", shape = (6, 60))#candidate|15222|(6, 60)|var|int64
call_15218 = relay.TupleGetItem(func_12281_call(relay.reshape(var_15219.astype('uint64'), []), relay.reshape(var_15220.astype('uint64'), [12, 6, 4]), relay.reshape(var_15221.astype('int64'), [273, 2]), relay.reshape(var_15222.astype('int64'), [360,]), ), 6)
call_15223 = relay.TupleGetItem(func_12286_call(relay.reshape(var_15219.astype('uint64'), []), relay.reshape(var_15220.astype('uint64'), [12, 6, 4]), relay.reshape(var_15221.astype('int64'), [273, 2]), relay.reshape(var_15222.astype('int64'), [360,]), ), 6)
output = relay.Tuple([call_15167,const_15170,const_15171,call_15184,var_15185,var_15186,bop_15209,call_15218,var_15219,var_15220,var_15221,var_15222,])
output2 = relay.Tuple([call_15168,const_15170,const_15171,call_15187,var_15185,var_15186,bop_15212,call_15223,var_15219,var_15220,var_15221,var_15222,])
func_15245 = relay.Function([var_15185,var_15186,var_15219,var_15220,var_15221,var_15222,], output)
mod['func_15245'] = func_15245
mod = relay.transform.InferType()(mod)
mutated_mod['func_15245'] = func_15245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15245_call = mutated_mod.get_global_var('func_15245')
var_15247 = relay.var("var_15247", dtype = "float64", shape = (364,))#candidate|15247|(364,)|var|float64
var_15248 = relay.var("var_15248", dtype = "uint32", shape = (5, 84))#candidate|15248|(5, 84)|var|uint32
var_15249 = relay.var("var_15249", dtype = "uint64", shape = ())#candidate|15249|()|var|uint64
var_15250 = relay.var("var_15250", dtype = "uint64", shape = (288,))#candidate|15250|(288,)|var|uint64
var_15251 = relay.var("var_15251", dtype = "int64", shape = (546,))#candidate|15251|(546,)|var|int64
var_15252 = relay.var("var_15252", dtype = "int64", shape = (6, 60))#candidate|15252|(6, 60)|var|int64
call_15246 = func_15245_call(var_15247,var_15248,var_15249,var_15250,var_15251,var_15252,)
output = call_15246
func_15253 = relay.Function([var_15247,var_15248,var_15249,var_15250,var_15251,var_15252,], output)
mutated_mod['func_15253'] = func_15253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14073_call = mod.get_global_var('func_14073')
func_14075_call = mutated_mod.get_global_var('func_14075')
call_15255 = relay.TupleGetItem(func_14073_call(), 0)
call_15256 = relay.TupleGetItem(func_14075_call(), 0)
func_14709_call = mod.get_global_var('func_14709')
func_14711_call = mutated_mod.get_global_var('func_14711')
call_15259 = func_14709_call()
call_15260 = func_14709_call()
func_1802_call = mod.get_global_var('func_1802')
func_1807_call = mutated_mod.get_global_var('func_1807')
var_15262 = relay.var("var_15262", dtype = "uint16", shape = (864,))#candidate|15262|(864,)|var|uint16
const_15263 = relay.const([4.701287,-3.902965,7.855875,0.805299,-2.887530,2.297734,6.986798,-9.770385,3.268652,2.434613,9.681234,8.762103,1.041540,8.533665,-0.780884,6.129746,-7.808822,4.826939,-0.166476,8.442190,7.653139,3.575068,-0.181391,-0.319614,-2.853225,-8.759488,1.653114,-4.060911,6.694979,1.329993,-3.909771,9.825831,6.114612,-9.710834,1.820243,-6.468148,0.557872,2.313224,-6.455922,0.798915,-2.879584,-5.644711,2.757103,-0.242536,6.786623,-1.399579,8.626783,-8.533223,-2.089109,-6.005883,3.494507,3.980463,4.885617,-9.235971,-8.802681,-5.399267,-8.006417,-1.937737,-3.975710,-7.391088,-7.324159,8.407496,6.689497,-2.135690,1.330529,4.896754,-9.713490,9.974598,-1.457981,1.809337,3.567132,2.367304,-7.447266,8.402032,-6.544768,-5.217763,-4.591399,-3.844099,-8.192696,5.341226,-5.024131,-8.396970,5.002586,-7.331633,3.449174,-0.440819,7.187624,-9.441651,8.266892,-8.763794,-1.444376,2.641398,7.704176,-2.824223,-6.385602,4.974440,-8.102379,1.229599,5.877967,4.038403,1.794848,9.055496,8.434302,7.890571,3.299787,4.298099,-9.010157,-8.810521,-6.988810,7.042003,-1.844957,8.753946,-1.812229,1.939966,-8.648749,2.322884,-5.574195,5.868026,-0.265523,4.485797,-6.225905,1.514385,6.082887,-5.208100,-4.983308,-9.329219,-2.174264,-1.469596,9.547921,-7.907870,-4.495082,4.811030,-4.624032,2.934451,8.652768,-9.765655,4.852813,1.312025,7.758782,-8.498169,9.768062,6.263561,0.684965,1.732447,1.799938,-8.262047,9.171429,-1.956291,-6.224095,-6.697885,-9.762484,-2.725121,2.614102,-5.810663,8.938108,-7.903422,-7.210516,5.404143,3.968769,-3.660479,-7.128218,2.550971,-8.336473,-1.727534,9.283657,1.838983,0.415931,3.890372,3.180050,-0.841348,-0.020613,3.525694,-3.405765,-3.209057,8.456555,-8.620912,-3.622404,4.734683,3.670754,2.153671,5.570380,2.030356,-7.758228,1.368783,-5.130130,4.373170,-1.469718,2.040374,5.730802,6.049545,-2.536407,-4.753751,6.542380,-0.851593,8.148070,5.141422,-1.557240,-8.507010,6.435605,-8.689217,6.771492,-9.826620,-1.537569,-2.140562,-7.123208,7.670904,8.231629,4.170691,5.360550,4.628252,7.342645,9.203055,5.411084,2.727463,0.004903,8.037177,9.416935,7.582564,0.851316,1.604343], dtype = "float32")#candidate|15263|(220,)|const|float32
call_15261 = relay.TupleGetItem(func_1802_call(relay.reshape(var_15262.astype('uint16'), [6, 12, 12]), relay.reshape(var_15262.astype('uint16'), [6, 12, 12]), relay.reshape(const_15263.astype('float32'), [220,]), ), 0)
call_15264 = relay.TupleGetItem(func_1807_call(relay.reshape(var_15262.astype('uint16'), [6, 12, 12]), relay.reshape(var_15262.astype('uint16'), [6, 12, 12]), relay.reshape(const_15263.astype('float32'), [220,]), ), 0)
bop_15265 = relay.greater_equal(call_15261.astype('bool'), relay.reshape(const_15263.astype('bool'), relay.shape_of(call_15261))) # shape=(10, 11, 2)
bop_15268 = relay.greater_equal(call_15264.astype('bool'), relay.reshape(const_15263.astype('bool'), relay.shape_of(call_15264))) # shape=(10, 11, 2)
func_14973_call = mod.get_global_var('func_14973')
func_14975_call = mutated_mod.get_global_var('func_14975')
const_15274 = relay.const([[True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True],[False,True,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False],[False,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True],[True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True],[True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,False],[True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True],[True,False,True,True,True,False,True,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False],[True,False,True,True,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,False]], dtype = "bool")#candidate|15274|(8, 66)|const|bool
call_15273 = relay.TupleGetItem(func_14973_call(relay.reshape(const_15274.astype('bool'), [24, 22])), 2)
call_15275 = relay.TupleGetItem(func_14975_call(relay.reshape(const_15274.astype('bool'), [24, 22])), 2)
uop_15279 = relay.asinh(bop_15265.astype('float64')) # shape=(10, 11, 2)
uop_15281 = relay.asinh(bop_15268.astype('float64')) # shape=(10, 11, 2)
output = relay.Tuple([call_15255,call_15259,var_15262,call_15273,const_15274,uop_15279,])
output2 = relay.Tuple([call_15256,call_15260,var_15262,call_15275,const_15274,uop_15281,])
func_15282 = relay.Function([var_15262,], output)
mod['func_15282'] = func_15282
mod = relay.transform.InferType()(mod)
var_15283 = relay.var("var_15283", dtype = "uint16", shape = (864,))#candidate|15283|(864,)|var|uint16
output = func_15282(var_15283)
func_15284 = relay.Function([var_15283], output)
mutated_mod['func_15284'] = func_15284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14157_call = mod.get_global_var('func_14157')
func_14158_call = mutated_mod.get_global_var('func_14158')
call_15308 = relay.TupleGetItem(func_14157_call(), 0)
call_15309 = relay.TupleGetItem(func_14158_call(), 0)
func_12281_call = mod.get_global_var('func_12281')
func_12286_call = mutated_mod.get_global_var('func_12286')
var_15311 = relay.var("var_15311", dtype = "uint64", shape = ())#candidate|15311|()|var|uint64
var_15312 = relay.var("var_15312", dtype = "uint64", shape = (2, 144))#candidate|15312|(2, 144)|var|uint64
const_15313 = relay.const([8,7,1,10,-1,-2,-5,5,7,-3,1,-1,-10,9,5,-8,2,-7,-3,4,-9,-2,-9,-10,-2,1,4,10,-1,10,4,9,3,1,-2,3,3,-8,4,-9,8,2,5,7,-8,10,-5,10,-4,6,-7,-9,-6,-3,4,7,-1,7,-8,2,3,1,-10,10,1,-1,-6,-9,9,1,3,9,-6,9,-5,1,2,8,3,7,-3,-4,-1,1,6,-7,-1,-2,5,2,-2,-7,-5,6,2,-3,4,-8,-2,-6,3,7,10,-3,-1,-2,-6,-7,6,10,-9,-5,-2,-7,-1,3,6,10,-1,10,7,-5,3,-5,-5,6,-8,6,-5,-4,-6,2,9,8,6,4,-10,-6,8,9,-6,7,8,-4,6,1,9,4,7,9,-7,-7,-9,9,2,-3,5,-2,5,9,-8,-3,-6,-4,-8,8,-6,-4,8,4,-3,10,-1,4,10,9,-4,4,9,4,-3,-3,-9,-5,2,7,-8,-7,9,7,5,-9,8,10,5,5,8,6,8,-2,-1,-8,-6,-10,-6,-6,4,-9,-3,10,-3,-4,6,8,-1,4,1,-3,-5,-4,1,-2,-9,5,-10,-8,3,-5,3,-3,-4,-8,-7,2,5,4,7,-9,7,-6,3,1,7,-3,9,-9,-2,-8,10,-4,-9,1,4,-2,-5,9,4,4,-6,-6,-4,10,1,-5,-9,8,-7,3,8,-4,4,1,-3,-3,-1,-6,3,-10,-5,7,-6,-3,1,-6,-1,-2,-4,-5,9,8,7,6,1,4,3,-9,6,3,7,-8,10,5,6,-2,10,-4,3,8,-6,-9,6,7,1,-1,9,-9,3,4,-6,2,-6,4,8,5,-4,6,-4,2,-5,6,-4,5,-6,7,-3,7,-7,1,1,-3,2,-5,-4,-4,1,3,2,3,4,2,-8,9,10,-5,5,7,7,4,10,10,-7,-7,8,-6,1,-10,-9,-6,-8,-3,1,2,4,9,5,3,2,-10,-1,1,-6,-1,-1,-5,8,-3,8,6,3,-5,-7,-10,-10,7,9,-1,10,-2,-9,-1,-5,-5,-2,-6,-8,-3,9,4,-6,-1,1,-1,-4,-4,-10,-9,9,-7,-6,-6,-3,-9,-4,6,-6,-6,8,9,-8,4,-8,-2,-6,-10,3,-7,6,-3,-1,-2,-5,-3,6,5,-3,-4,10,9,-7,10,-4,-8,-3,3,-9,10,-5,-7,2,-5,-10,7,-4,-8,5,3,-3,2,-4,-9,-1,-9,1,-7,7,-10,-2,-7,-3,-7,2,-8,1,-2,-6,-7,1,7,-9,5,-8,-3,9,-7,4,1,-2,-1,-2,7,4,-8,8,-7,10,7,4,-8,-7,-7,9,-6,-10,3,10,9,1,-10,-3,-10,-8,2,-6,-5,7,5,-2,6,-8,2,-8,3,-10,-2,10,5,8,10,-10,-6,-8,3,-2,10,8,7], dtype = "int64")#candidate|15313|(546,)|const|int64
var_15314 = relay.var("var_15314", dtype = "int64", shape = (360,))#candidate|15314|(360,)|var|int64
call_15310 = relay.TupleGetItem(func_12281_call(relay.reshape(var_15311.astype('uint64'), []), relay.reshape(var_15312.astype('uint64'), [12, 6, 4]), relay.reshape(const_15313.astype('int64'), [273, 2]), relay.reshape(var_15314.astype('int64'), [360,]), ), 11)
call_15315 = relay.TupleGetItem(func_12286_call(relay.reshape(var_15311.astype('uint64'), []), relay.reshape(var_15312.astype('uint64'), [12, 6, 4]), relay.reshape(const_15313.astype('int64'), [273, 2]), relay.reshape(var_15314.astype('int64'), [360,]), ), 11)
func_14740_call = mod.get_global_var('func_14740')
func_14742_call = mutated_mod.get_global_var('func_14742')
call_15322 = func_14740_call()
call_15323 = func_14740_call()
func_3287_call = mod.get_global_var('func_3287')
func_3291_call = mutated_mod.get_global_var('func_3291')
const_15326 = relay.const([-8,-4,-4,4,3,-7,-4,6,-5,3,10,7,5,-3,2,6,6,1,-7,1,4,7,-5,10,-7,-10,-8,3,6,2,-4,6,-10,-10,-3,9,9,5,-8,-5,-6,5,1,-1,2,5,-4,5,-9,3,6,-9,-7,-2,-9,-3,4,-3,6,4,-9,-3,1,7,5,-3,-1,7,-9,6,-5,-5,6,4,3,-9,4,-3,2,-6,-9,7,1,9,-2,-8,-1,4,2,-9,-5,-7,-10,5,-2,8,-7,-1,-8,8,5,-5,-10,6,-8,-9,5,1,8,-9,4,-2,-4,-9,5,-2,-7,9,-7,-1,1,-5,8,6,-9,-8,4,-6,-5,1,-4,2,-10,-9,7,-2,-2,9,-3,7,9,9,-5,10,-9,2,3,-7,9,2,7,-8,-10,-10,1,-9,3,2,10,-10,2,-6,-7,10,8,2,5,-6,-7,10,-4,-6,6,4,1,-8,-5,-10,5,8,3,9,-2,-2,1,-6,-2,1,2,5,1,-8,6,-9,-1,6,-9,-9,10,-9,-3,8,-9,3,-6,7,-2,4,-7,10,-1,10,-1,-2,-10,4,8,-1,10,-10,-4,4,4,-5,4,-8,10,-7,-7,-4,2,2,-9,-8,-9,-5,-7,-9,10,3,9,-9,9,2,6,3,-3,9,8,-10,8,-7,6,-8,-2,-8,-4,2,4,-9,1,10,7,-5,-9,-9,2,-3,-6,5,-6,8,2,1,-5,8,-2,-1,8,-3,3,-5,2,5,3,-5,-5,-6,5,4,-10,10,-1,-3,9,7,10,8,1,9,3,10,-6,-4,-6,3,-9,9,3,8,-8,3,8,-9,5,3,-9,-4,1,-8,-6,-2,5,4,1,-10,-6,6,-6,-3,10,-9,-10,4,2,-6,-2,-3,10,-4,9,2,9,-1,3,-6,-1,4,9,-1,-1,-1,-7,-1,-2,-2,1,8,1,6,5,-9,-8,-8,-2,-10,-7,-7,5,-5,-2,-8,8,4,-5,-7,2,-7,-10,7,-5,6,-8,-8,2,-10,8,-9,3,-10,-4,1,3,-4,6,-5,-8,2,-6,9,-2,2,6,-8,5,-9,5,4,-1,-10,-2,5,6,8,-8,7,5,-1,1,9], dtype = "uint32")#candidate|15326|(420,)|const|uint32
call_15325 = relay.TupleGetItem(func_3287_call(relay.reshape(const_15326.astype('uint32'), [10, 7, 6]), relay.reshape(const_15326.astype('uint32'), [10, 7, 6]), ), 1)
call_15327 = relay.TupleGetItem(func_3291_call(relay.reshape(const_15326.astype('uint32'), [10, 7, 6]), relay.reshape(const_15326.astype('uint32'), [10, 7, 6]), ), 1)
output = relay.Tuple([call_15308,call_15310,var_15311,var_15312,const_15313,var_15314,call_15322,call_15325,const_15326,])
output2 = relay.Tuple([call_15309,call_15315,var_15311,var_15312,const_15313,var_15314,call_15323,call_15327,const_15326,])
func_15329 = relay.Function([var_15311,var_15312,var_15314,], output)
mod['func_15329'] = func_15329
mod = relay.transform.InferType()(mod)
mutated_mod['func_15329'] = func_15329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15329_call = mutated_mod.get_global_var('func_15329')
var_15331 = relay.var("var_15331", dtype = "uint64", shape = ())#candidate|15331|()|var|uint64
var_15332 = relay.var("var_15332", dtype = "uint64", shape = (2, 144))#candidate|15332|(2, 144)|var|uint64
var_15333 = relay.var("var_15333", dtype = "int64", shape = (360,))#candidate|15333|(360,)|var|int64
call_15330 = func_15329_call(var_15331,var_15332,var_15333,)
output = call_15330
func_15334 = relay.Function([var_15331,var_15332,var_15333,], output)
mutated_mod['func_15334'] = func_15334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14073_call = mod.get_global_var('func_14073')
func_14075_call = mutated_mod.get_global_var('func_14075')
call_15358 = relay.TupleGetItem(func_14073_call(), 0)
call_15359 = relay.TupleGetItem(func_14075_call(), 0)
const_15380 = relay.const([[[-7.911248,0.295456,6.468166,-9.361787,6.295181,-6.129172,7.680440,6.003739,5.518511,4.375934,8.238444,1.842692,-6.215651,-7.194202,6.661455],[0.166227,9.016544,-2.046207,-3.545425,6.530875,7.617111,-3.259382,5.045220,6.999580,4.279777,3.175181,5.366782,-7.895713,3.356381,9.824006],[-1.978684,-7.143414,8.174918,8.729954,-4.232380,3.697855,-9.592352,-3.758276,2.549631,-8.196467,-7.677360,1.044183,9.988985,0.407621,-7.383307]],[[2.056545,-7.645161,-5.156870,-5.324064,6.310358,9.189293,-8.392754,-1.023176,2.118057,5.110412,-1.282148,6.136296,6.091242,6.244014,5.571625],[7.414234,-4.900912,7.512732,0.039815,-8.938124,-8.972919,0.570214,-2.689540,7.760601,-9.885857,3.438843,-7.477425,-5.566692,5.353084,1.586475],[-4.502049,-8.706860,-6.450563,8.500898,8.651844,-1.675469,6.791033,3.046529,2.454115,8.859092,5.354493,-7.738070,-7.451298,5.644394,-4.155370]],[[-8.135981,-8.155975,6.122143,-3.007730,-1.131085,7.444712,3.515989,2.977536,-0.598843,6.030844,-5.786507,-4.173873,7.303088,2.358239,3.901551],[5.778723,-8.320476,-2.801646,-7.157567,9.260889,-0.358394,6.639854,4.903810,-8.033723,6.542923,-3.875369,-2.264902,-3.362690,9.590879,7.641950],[0.483612,-6.105434,-4.876393,2.224309,-3.666587,0.211168,4.152632,-3.360381,8.454820,-9.366894,0.986962,-0.763656,-0.545197,6.821637,7.411165]],[[-5.224989,2.053934,-1.345679,4.828772,-5.198848,-6.651066,-8.306678,-8.566844,6.666738,-0.843873,-1.477874,-6.045002,4.674562,9.851427,-3.201471],[9.264798,9.285397,8.268108,-0.537665,2.038373,-0.483917,3.366261,-6.231372,-7.178992,5.001750,3.254458,-1.328783,5.998253,-1.977416,-8.604969],[9.900253,9.430527,-7.939408,-7.176956,9.930846,4.645578,-4.286252,8.881184,-7.186819,-4.141991,-6.157812,6.745583,9.098958,-7.715507,7.025925]],[[-1.403683,5.984969,4.220151,-6.506613,-3.461822,3.279061,-5.138869,-8.128606,-4.451974,9.927283,5.225144,1.142129,-9.076899,3.001964,-9.584072],[0.462141,7.906600,0.352578,-1.465929,-3.229819,3.157882,-7.072723,5.434844,8.861079,6.759836,-3.052589,-0.171033,9.169332,-5.661437,-2.299358],[1.825950,4.666554,-2.360862,6.275304,5.238276,0.741439,0.656361,-7.627281,5.804558,4.180194,-3.747952,5.144880,5.308564,2.107376,1.824664]],[[-4.870628,0.855143,1.405520,-2.668072,-2.156431,-2.491003,6.046480,2.274643,2.992886,0.289506,6.384767,-8.813695,6.957909,6.660373,-6.507701],[-3.889768,0.254956,-5.194341,8.807725,7.000379,-7.985463,2.550161,6.316155,6.226770,6.198897,5.869020,-1.115266,8.234403,4.687712,-6.651385],[0.990663,4.026495,-0.682588,2.899864,-8.972761,6.340319,3.282904,-5.720578,3.879905,1.449928,3.147568,6.320916,-2.289836,8.792711,8.636649]],[[8.315071,-0.429387,2.090808,2.366517,-5.689421,9.115731,-6.633537,-7.006023,-8.533421,1.059780,5.378129,-5.063768,-1.175098,1.811676,6.440847],[-5.249020,-5.010803,9.104987,9.037027,-2.942751,-7.124183,-7.790931,-0.927411,-3.369146,-4.765600,-2.214864,-6.518760,4.222419,-9.174386,-0.082719],[6.129403,-6.241537,0.076954,-6.032257,-4.835018,-7.835127,-4.468092,-9.615642,5.011411,1.953776,-2.436114,1.462212,3.819006,1.130046,-4.179681]],[[3.985204,-1.751305,2.971913,9.722970,1.012621,-6.087835,-2.257019,-5.212218,-8.699739,9.051180,9.783170,8.186880,-6.103628,3.656441,-9.348693],[3.836973,-7.721907,-3.040043,5.096106,2.067146,8.092555,-9.503572,-3.443970,-4.214261,2.265398,2.004729,3.247862,4.116500,0.565328,-6.495699],[-1.515639,4.457936,9.744375,-9.509462,6.843430,4.429841,-4.013481,-5.399163,-0.841731,5.937969,9.924641,3.735946,8.954931,-9.473010,1.873309]],[[1.950108,5.607427,-9.349939,-1.513654,9.683144,-5.334598,-0.519687,9.513462,-9.169890,-8.331385,4.466037,-9.128309,-3.384041,4.360268,-1.378063],[4.385442,4.108685,-9.823902,-5.638473,-0.420998,-5.345303,-5.960078,9.821815,0.137628,-9.472230,3.370751,3.391068,-7.455112,-6.208118,8.421824],[-3.070259,-2.934380,2.086671,-4.592232,1.474840,7.049807,6.260468,-0.882653,9.552480,-2.580655,4.581567,0.669583,8.735645,7.745760,-3.920843]],[[-6.679244,9.745592,-9.548039,6.592287,-0.143998,4.889969,-0.283675,-7.813454,-2.016544,9.323514,6.141955,-0.575370,1.855159,-0.471731,9.990725],[7.000884,8.100811,-5.015550,8.682002,-1.642926,-8.687594,-7.303013,8.198133,-0.507974,-7.276886,-1.711253,-1.053401,7.975599,2.434880,-2.449430],[-8.961034,-5.473923,1.164999,1.377190,4.183303,-8.395062,4.418088,-5.065981,8.543087,-4.609485,-4.505935,6.922730,-0.094916,2.040666,-4.900722]],[[-4.338795,4.844572,7.552496,-3.357617,-5.966896,-5.123021,7.059442,2.654961,-3.978893,-5.863370,-8.689260,-3.583203,-4.978303,-6.904183,-7.018716],[8.186129,8.427563,6.434230,5.981836,4.049566,2.966186,2.103381,-5.329870,6.460770,2.115364,0.237460,-9.276902,-9.627840,-5.338732,-4.273134],[7.827246,-9.131111,7.105001,9.908825,6.881015,-0.362420,1.761052,2.506576,-5.708826,-6.882917,8.387660,3.502733,6.532753,-6.930327,9.002002]],[[-1.407172,-4.428695,0.643277,4.221218,2.022889,-2.617577,2.625559,4.259468,7.528815,4.830282,0.158944,1.222692,0.998168,-4.161569,2.702285],[-3.030329,1.332745,-2.149899,-1.289943,6.877811,-6.795236,2.312014,9.569387,-2.747958,-9.776808,5.851034,-6.031486,4.898623,1.849042,4.825944],[7.034266,1.225479,9.986422,3.474753,5.528087,6.506037,-8.928103,7.777756,7.034731,-8.032614,-6.862344,0.892997,0.306538,-0.141130,5.519015]],[[8.107265,9.761045,2.278518,-0.199258,5.284358,2.506736,7.351178,9.790127,-7.447629,-7.686192,4.030844,-3.060013,-2.997883,7.810069,-1.636664],[-5.169056,0.256042,-6.939957,-8.485015,6.275536,-6.468597,-4.896051,5.625692,2.006397,-9.679040,-8.598682,-7.455726,9.804572,-3.190138,9.353270],[9.672680,-9.837079,9.896188,0.095626,6.217314,2.079105,5.533856,0.323712,-9.678056,-5.490881,7.373061,-0.885205,4.292700,-2.671021,-5.615450]]], dtype = "float32")#candidate|15380|(13, 3, 15)|const|float32
bop_15381 = relay.minimum(call_15358.astype('int16'), relay.reshape(const_15380.astype('int16'), relay.shape_of(call_15358))) # shape=(13, 3, 15)
bop_15384 = relay.minimum(call_15359.astype('int16'), relay.reshape(const_15380.astype('int16'), relay.shape_of(call_15359))) # shape=(13, 3, 15)
output = relay.Tuple([bop_15381,])
output2 = relay.Tuple([bop_15384,])
func_15389 = relay.Function([], output)
mod['func_15389'] = func_15389
mod = relay.transform.InferType()(mod)
mutated_mod['func_15389'] = func_15389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15389_call = mutated_mod.get_global_var('func_15389')
call_15390 = func_15389_call()
output = call_15390
func_15391 = relay.Function([], output)
mutated_mod['func_15391'] = func_15391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14748_call = mod.get_global_var('func_14748')
func_14749_call = mutated_mod.get_global_var('func_14749')
call_15394 = func_14748_call()
call_15395 = func_14748_call()
const_15402 = relay.const([[[-3.200567,9.018993,8.804313,-8.648281,-4.798398,3.900882,6.591170,4.367809,-9.200783,-0.293127,7.887867,-5.669175,-0.461255,-3.735388,3.950759],[3.021588,1.851207,2.437222,-6.950389,-0.980750,-4.338413,-8.619886,-7.184181,-5.445139,-5.740954,-5.081131,9.691435,8.826361,8.694866,-3.185342],[4.031102,-7.041007,-2.206216,0.553488,-1.646562,6.950704,7.758962,-8.331973,-0.697030,-3.586744,4.404181,-6.615727,3.441252,-4.340081,-2.976300]],[[9.989791,-3.982171,-9.718574,9.576037,-3.563643,-8.144289,-7.951963,8.579144,2.877180,4.399467,-2.584678,-3.918394,-3.678548,-0.255607,-5.630862],[8.939997,-7.617955,-2.991642,-1.224152,-3.448209,0.045570,-6.983423,-7.123477,-4.707005,6.169347,-4.340531,4.879586,6.364883,-2.194146,-7.927181],[-6.046726,1.177033,-3.557897,8.594873,1.146660,5.408280,-6.261340,2.337672,3.082958,-1.781286,8.105924,-0.923427,-6.876478,-3.959327,1.106819]],[[6.071281,-5.143268,-3.115427,-4.209549,4.997901,1.563171,-5.804753,1.435403,-2.112102,-8.653297,8.664299,1.800212,-8.667076,0.360162,8.905831],[3.406054,-6.862625,0.157320,-6.084772,7.022042,2.768111,-5.655251,-1.434148,1.740627,-4.106434,-9.219934,-2.633195,1.914417,5.766896,2.263111],[4.541928,9.929622,4.613356,-6.195757,1.187462,4.657182,-6.361125,-3.044897,1.210249,-4.459580,7.868880,-6.099204,-4.447010,-9.428040,-1.542769]],[[-2.079954,7.152805,-2.510089,-1.058081,-6.926159,-0.629316,7.425212,-6.050900,8.962439,7.523335,3.462731,-6.058153,-8.286231,-2.862798,-9.203715],[7.301969,-3.296699,2.719512,4.018368,-6.156516,4.447757,5.181001,8.017817,-7.781025,-4.900261,-2.458623,5.328923,1.565218,-9.476611,-1.040255],[-0.445772,5.973515,-6.983269,8.938080,7.509523,-2.917614,-5.306205,3.272312,6.399838,9.215806,5.520690,4.152996,-7.872005,6.383388,-3.249843]],[[-3.968121,3.760084,-7.868149,-3.681234,9.298979,8.353990,-9.291772,6.822507,3.823800,8.726685,-6.967302,8.702438,1.726407,-9.657602,-3.733636],[8.567367,-6.113227,-2.581276,-7.204637,-3.117373,-8.520052,5.546266,-2.184206,-0.446771,7.158094,-5.607200,7.158871,-5.560493,3.190869,0.105890],[8.653453,-4.113618,4.802060,-3.254658,5.679567,7.647658,-1.255810,-5.262224,1.923643,0.697030,8.814708,4.047046,9.423169,3.404692,-5.017653]],[[-6.910871,2.236768,9.853014,9.025418,0.401922,2.802398,6.526616,9.186870,-0.703961,-2.815532,-8.205966,3.251745,-8.168971,1.322545,7.616101],[-1.203093,0.160492,6.773222,-2.632094,1.202847,9.519170,-7.654473,-7.834277,8.159392,3.398302,-0.853932,8.534047,7.840137,-5.515757,9.321153],[-1.757437,5.574885,-5.321057,5.013746,-9.712722,-7.381294,7.217880,-4.036507,-8.914743,-4.761699,1.166058,2.014034,-6.015910,1.015064,8.532366]],[[-1.177262,-9.511039,-3.650660,-0.760623,-7.914292,-2.777667,8.671745,5.881611,6.815882,4.156301,8.510938,5.905060,4.268308,9.226223,-2.936343],[9.328237,2.215193,8.332015,-2.162136,2.909870,-4.580937,4.992016,3.947547,6.761707,2.974272,-4.100713,8.045878,9.177161,1.807800,3.681925],[-0.915076,-1.796198,0.668659,3.960408,-8.191750,-4.903166,-7.583505,-2.035162,-7.351200,-6.300172,-9.306075,2.151372,-9.275311,-6.941464,5.813374]],[[-3.132828,-7.408970,7.579440,-5.305843,-3.637158,6.199857,9.882648,-1.226146,3.041743,8.317145,-1.757957,-3.478543,3.026199,7.298442,-6.460122],[-9.599279,-6.583050,-1.582587,-3.490877,-2.910421,5.192544,9.678381,0.819953,-5.951747,-9.140564,-2.843743,4.490384,-4.417932,-4.612588,-8.829308],[2.232567,6.115120,5.422401,2.513983,-4.866512,-9.837607,-4.889538,-1.957549,-4.671506,-8.686946,-2.163248,3.390521,-2.590115,-0.282582,6.564650]],[[7.335231,7.125480,-9.788097,-3.703648,-9.604194,4.490817,-8.575399,-1.602308,5.602213,2.070870,-8.449815,9.613564,8.589030,7.474596,-5.309652],[-5.096975,9.217992,-4.739431,8.823626,-2.919750,0.087145,-7.203712,4.895300,-2.922520,9.952783,-0.006346,2.036252,-9.364104,3.832754,-3.234470],[-2.293526,-7.666742,7.906468,-7.762064,1.891710,-1.894921,-4.874500,2.223689,-3.034229,5.938797,3.957066,5.108305,7.931719,-8.611483,3.793650]],[[-5.112003,7.509020,-5.265290,5.385649,7.376699,2.426630,7.455199,1.429214,0.762772,-6.613761,5.763665,-7.167433,-4.434051,-5.833751,7.009951],[4.189460,-9.710891,-2.313460,8.899403,5.900183,-6.164094,7.758577,-6.619439,-7.704529,-0.051985,-5.031161,3.004359,-8.872887,-0.442873,-5.249543],[-1.117734,3.142472,-3.986822,6.033252,6.392512,8.543554,0.702946,7.282095,4.235803,8.957951,-6.065640,9.333046,2.049472,5.609036,3.106823]],[[1.063321,-0.199757,-6.100963,-8.567541,-3.014780,-4.359899,8.567339,-3.342400,8.141526,5.491456,8.395371,7.514789,8.415746,-4.470494,-2.320150],[-6.560592,-7.997835,3.281147,0.190911,-0.433434,3.613372,8.811537,8.337422,-0.864375,5.638819,4.538427,1.879814,-7.342904,7.042657,-3.567220],[-4.855108,4.902870,8.014977,7.784802,-7.842445,-3.762458,-1.630449,7.129145,-2.248346,-0.828561,5.667230,-2.961837,-1.733541,5.108337,-7.430275]],[[-1.575992,-2.066466,7.289597,-8.282578,-5.750770,-1.315877,-5.492865,7.073701,-2.737064,0.548558,1.363723,0.603255,-6.587492,-6.563462,8.475762],[6.346486,0.273640,-1.444339,9.644236,3.626335,4.969466,-6.078468,-9.192371,8.467810,4.037850,-8.984445,2.330756,5.020137,0.762203,1.223244],[-3.087781,-6.535220,-6.359992,-0.394974,9.422278,-8.422938,7.345225,9.862239,-7.239562,8.528498,9.309759,-3.899521,5.978925,-4.239249,-9.820888]],[[3.512794,-8.311145,-9.598965,-9.174451,-7.767944,6.085386,4.956301,-4.126109,-6.017593,0.290448,-9.835229,8.918058,-4.611523,-3.374243,-8.697030],[-4.905718,1.647208,9.503405,-0.045165,-8.992872,-2.181639,4.528081,6.179854,-7.722162,-5.151886,0.315795,-2.295918,0.757588,5.402827,-2.448969],[-8.709253,4.762815,3.346367,-9.817981,8.455861,1.106009,-0.646863,9.654605,-2.320423,4.107820,5.131460,4.513716,-2.786345,-8.352181,1.940285]]], dtype = "float32")#candidate|15402|(13, 3, 15)|const|float32
bop_15403 = relay.left_shift(call_15394.astype('uint16'), relay.reshape(const_15402.astype('uint16'), relay.shape_of(call_15394))) # shape=(13, 3, 15)
bop_15406 = relay.left_shift(call_15395.astype('uint16'), relay.reshape(const_15402.astype('uint16'), relay.shape_of(call_15395))) # shape=(13, 3, 15)
output = relay.Tuple([bop_15403,])
output2 = relay.Tuple([bop_15406,])
func_15422 = relay.Function([], output)
mod['func_15422'] = func_15422
mod = relay.transform.InferType()(mod)
mutated_mod['func_15422'] = func_15422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15422_call = mutated_mod.get_global_var('func_15422')
call_15423 = func_15422_call()
output = call_15423
func_15424 = relay.Function([], output)
mutated_mod['func_15424'] = func_15424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14709_call = mod.get_global_var('func_14709')
func_14711_call = mutated_mod.get_global_var('func_14711')
call_15469 = func_14709_call()
call_15470 = func_14709_call()
func_14253_call = mod.get_global_var('func_14253')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_15480 = relay.TupleGetItem(func_14253_call(), 0)
call_15481 = relay.TupleGetItem(func_14254_call(), 0)
output = relay.Tuple([call_15469,call_15480,])
output2 = relay.Tuple([call_15470,call_15481,])
func_15484 = relay.Function([], output)
mod['func_15484'] = func_15484
mod = relay.transform.InferType()(mod)
output = func_15484()
func_15485 = relay.Function([], output)
mutated_mod['func_15485'] = func_15485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15422_call = mod.get_global_var('func_15422')
func_15424_call = mutated_mod.get_global_var('func_15424')
call_15491 = relay.TupleGetItem(func_15422_call(), 0)
call_15492 = relay.TupleGetItem(func_15424_call(), 0)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_15495 = relay.TupleGetItem(func_15484_call(), 1)
call_15496 = relay.TupleGetItem(func_15485_call(), 1)
output = relay.Tuple([call_15491,call_15495,])
output2 = relay.Tuple([call_15492,call_15496,])
func_15508 = relay.Function([], output)
mod['func_15508'] = func_15508
mod = relay.transform.InferType()(mod)
mutated_mod['func_15508'] = func_15508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15508_call = mutated_mod.get_global_var('func_15508')
call_15509 = func_15508_call()
output = call_15509
func_15510 = relay.Function([], output)
mutated_mod['func_15510'] = func_15510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14228_call = mod.get_global_var('func_14228')
func_14229_call = mutated_mod.get_global_var('func_14229')
call_15518 = func_14228_call()
call_15519 = func_14228_call()
func_6258_call = mod.get_global_var('func_6258')
func_6262_call = mutated_mod.get_global_var('func_6262')
var_15531 = relay.var("var_15531", dtype = "uint32", shape = (220,))#candidate|15531|(220,)|var|uint32
const_15532 = relay.const(-7.146874, dtype = "float32")#candidate|15532|()|const|float32
const_15533 = relay.const([-2.465661,-9.638182,-6.161221,-5.561194,0.410047,3.761534,6.056725,2.907729,8.189161,-4.339810,-5.013253,-0.522145,6.997426,-9.788830,2.573865,4.587988,3.716042,9.210152,-2.516541,6.685873,4.463824,-8.687691,4.374832,2.607446,-0.817753,7.983520,1.767011,-1.711814,-2.589261,-0.679141,-6.221356,-6.630117,0.760629,-4.422547,3.639979,1.850362,-7.236949,1.016414,9.518941,-5.458059,-3.502503,2.622209,6.248617,-7.097809,-9.474289,-0.527077,-5.321315,-7.531947,-4.392406,6.391433,-3.394403,-1.116547,-5.806823,-1.912324,-0.099397,-1.952124,-3.897102,-9.390131,6.012708,-8.923453,0.962311,1.487903,8.814416,0.655726,-1.395384,3.509082,8.094725,8.771449,0.428224,-9.911292,-1.327232,-7.366454,-6.377542,-4.832118,7.535528,4.075364,6.117284,8.693431,-5.429155,-6.837270,0.060705,2.096975,4.871893,7.295244,-2.497839,-0.746973,-8.472906,-9.068294,-5.167191,-5.350519,5.948913,-8.412781,-6.184330,0.524914,1.100153,1.784221,1.721387,3.086955,9.017891,0.937580,-9.805555,-4.528539,-8.303502,4.142110,-9.409546,-7.993020,5.516248,-2.384948,-7.153247,-1.533999,-6.148645,6.843001,-5.494486,-7.915089,6.088918,-9.637497,-2.203232,-9.442873,8.412862,3.719800,6.809647,2.627446,-7.082635,1.722260,0.005162,-7.049202,8.484390,9.830599,9.806479,-8.955143,5.567255,-9.037375,3.809092,-7.132961,1.734942,-3.324707,3.606345,8.676737,-0.195749,5.073930,6.948899,7.278845,0.451558,-4.950970,-9.285288,0.408381,3.762085,8.309600,-9.077751,3.684761,8.669453,-7.252060,4.094072,1.420482,-1.699816,2.687514,-4.308596,3.670636,5.006455,-0.515079,-9.263444,0.918574,-1.587233,-1.130135,-6.763481,-3.147699,-3.682611,0.279807,-6.523067,2.926720,8.104013,-7.405026,2.632013,3.094721,-5.658569,-3.831314,7.368951,-4.006950,9.039522,-2.391399,1.184157,8.039123,9.836768,0.109983,8.620651,5.863370,-9.570796,1.747841,4.416710,-5.701280,-1.034070,-2.902852,9.355065,3.258421,8.926721,-8.568618,-2.709858,-4.391618,-3.332439,-7.438036,-0.823193,-3.199805,6.859386,-3.430312,-7.788644,-8.109040,-4.954770,-0.873549,-3.439889,-0.368575,3.375653,-1.150893,-3.345679,-2.555646,-3.375851,7.920966,-4.581380,5.696502,4.438130,-1.814403,9.390033,-3.294714,6.375755,3.133002,2.289615,3.489657,-6.940479,-2.367267,2.266546,-5.141914,8.238731,-3.072149,8.424701,-1.033015,-6.989447,3.691098,9.078426,9.030194,-8.692191,-5.252048,-3.247098,5.550905,4.205389,0.519352,-4.574244,0.057318,5.012886,6.537142,4.836712,9.525844,-3.219449,9.635506,6.265024,-3.407067,9.239252,2.177536,-7.543873,5.166991,-0.829060,-7.533066,-9.510948,7.198436,-5.238774,-1.586174,-8.601246,1.484871,-8.794753,-6.097463,2.022359,-6.773893,-1.712670,-7.222984,-3.913986,-2.009215,-9.318593,2.023590,-4.778054,4.103160,8.684048,9.069361,6.280622,-9.870522,9.582445,6.648362,8.920725,-8.104097,7.337493,-3.238207,-7.566164,4.943597,-1.146892,2.281803,8.528757,6.941224,-5.429064,-9.304506,5.960516,-6.180958,1.349656,6.168924,5.161504,-2.579310,-2.489251,-1.563435,-9.213366,7.006973,-5.520551,7.301878,9.159350,-6.127266,8.350668,-3.604896,2.056088,-1.259299,-7.919394,3.528512,6.185940,3.087194,-9.548899,-8.370693,8.548747,9.156140,-3.867719,8.752981,5.333486,1.831050,-5.842483,1.888674,-8.876241,-5.601542,4.322974,-8.562785,-1.522005,-7.798673,1.631698,2.180487,6.707029,-2.084365,7.569362,3.864168,2.471677,-3.522379,-8.954405,4.037635,8.383323,-3.038594,0.504820,3.237973,-3.860266,6.302797,-9.857075,-3.003893,6.948322,0.533715,-6.678625,-7.997308,2.655003,3.914565,-2.468272,1.775935,-1.373828,8.067931,-3.275355,5.792506,-9.399754,2.813187,1.063166,-9.315746,-6.582491,-8.600951,7.606746,5.360832,5.531008,-6.489271,6.512145,0.649754,4.906332,-1.478155,1.746142,-2.590150,-3.782239,-4.853429,0.340359,-9.902573,-4.675494,-3.258229,2.195895,-7.160018,-9.044272,0.647432,-9.102952,-8.413073,0.516271,-1.412030,-4.852498,-6.819365,-5.193710,1.018958,-1.197780,4.192123,-0.327010,-4.318404,4.940705,-6.865712,6.012465,-6.947804,-9.564955,-2.539179,3.334934,-4.161700,9.441486,-2.899317,3.739175,-5.997305,3.826961,-1.629241,0.073451,-4.672015,1.039907,5.632374,-9.735978,4.596445,-6.421635,-7.243689,-4.559720,8.054666,5.396106,7.668701,3.128751,-4.162055,3.990675,-9.585755,1.527372,-8.490610,6.607188,-2.060064,9.991022,-1.753824,9.044399,9.581718,9.478241,8.774222,-1.259521,8.430507,-5.507236,-1.302824,-9.357293,0.416855,4.075973,7.234665,2.809639,-4.674863,8.569324,-0.041977,0.784553,-6.229963,-3.846553,-7.790998,-3.086223,2.108641,1.067282,-1.222999,-0.759285,-4.210181,8.045351,5.512357,2.166997,3.407081,-1.134266,2.609577,1.566745,4.054734,9.054181,-4.895216,7.415171,9.790439,-8.096948,4.746721,4.778051,-7.763070,6.701207,5.843141,-3.527938,4.740999,-6.214128,-6.397807,-7.887977,7.460977,8.797545,2.518333,4.954174,-2.140827,-3.190672,2.269919,7.347783,2.729438,9.195861,4.119433,7.814271,-0.452791,6.897088,-3.762045,-6.706330,7.204887,9.086107,2.087054,0.151434,-7.711345,2.849199,1.137769,-2.802045,9.771182,4.404113,4.538834,2.272739,-3.075154,-0.035770,-4.541722,6.923041,9.888613,-2.285269,7.619581,-1.184722,3.371985,9.569890,-2.410563,0.372086,9.775543,-2.079982,-0.814577,7.863150,-9.731867,6.501594,-7.439342,-2.054259,9.735889,-7.576007,9.701574,8.198032,-8.967273,8.573552,-3.493174,-9.740228,-0.666741,-6.188573,-2.792857,3.586288,8.265965,6.324706,6.078249,0.979616,-7.320385,-7.747635,-8.173218,6.501919,-4.659138,1.996948,9.652018,7.439681,-1.853592,-1.025448,8.148911,3.402022,-6.265466,-8.647858,1.557381,4.659867,-9.107349,2.351374,9.438039,7.863470,3.214470,-8.868145,5.551112,-7.923496,9.043647,-4.683653,1.895556,2.180593,5.485720,4.974700,-9.659811,-9.838410,-0.383988,5.885869,-3.316083,-8.414496,-1.315315], dtype = "float32")#candidate|15533|(588,)|const|float32
call_15530 = relay.TupleGetItem(func_6258_call(relay.reshape(var_15531.astype('uint32'), [11, 10, 2]), relay.reshape(const_15532.astype('float32'), []), relay.reshape(const_15533.astype('float32'), [588,]), ), 4)
call_15534 = relay.TupleGetItem(func_6262_call(relay.reshape(var_15531.astype('uint32'), [11, 10, 2]), relay.reshape(const_15532.astype('float32'), []), relay.reshape(const_15533.astype('float32'), [588,]), ), 4)
output = relay.Tuple([call_15518,call_15530,var_15531,const_15532,const_15533,])
output2 = relay.Tuple([call_15519,call_15534,var_15531,const_15532,const_15533,])
func_15543 = relay.Function([var_15531,], output)
mod['func_15543'] = func_15543
mod = relay.transform.InferType()(mod)
var_15544 = relay.var("var_15544", dtype = "uint32", shape = (220,))#candidate|15544|(220,)|var|uint32
output = func_15543(var_15544)
func_15545 = relay.Function([var_15544], output)
mutated_mod['func_15545'] = func_15545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_15617 = relay.TupleGetItem(func_15484_call(), 0)
call_15618 = relay.TupleGetItem(func_15485_call(), 0)
output = call_15617
output2 = call_15618
func_15622 = relay.Function([], output)
mod['func_15622'] = func_15622
mod = relay.transform.InferType()(mod)
output = func_15622()
func_15623 = relay.Function([], output)
mutated_mod['func_15623'] = func_15623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14740_call = mod.get_global_var('func_14740')
func_14742_call = mutated_mod.get_global_var('func_14742')
call_15687 = func_14740_call()
call_15688 = func_14740_call()
func_15508_call = mod.get_global_var('func_15508')
func_15510_call = mutated_mod.get_global_var('func_15510')
call_15707 = relay.TupleGetItem(func_15508_call(), 0)
call_15708 = relay.TupleGetItem(func_15510_call(), 0)
output = relay.Tuple([call_15687,call_15707,])
output2 = relay.Tuple([call_15688,call_15708,])
func_15709 = relay.Function([], output)
mod['func_15709'] = func_15709
mod = relay.transform.InferType()(mod)
output = func_15709()
func_15710 = relay.Function([], output)
mutated_mod['func_15710'] = func_15710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14748_call = mod.get_global_var('func_14748')
func_14749_call = mutated_mod.get_global_var('func_14749')
call_15809 = func_14748_call()
call_15810 = func_14748_call()
output = call_15809
output2 = call_15810
func_15818 = relay.Function([], output)
mod['func_15818'] = func_15818
mod = relay.transform.InferType()(mod)
mutated_mod['func_15818'] = func_15818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15818_call = mutated_mod.get_global_var('func_15818')
call_15819 = func_15818_call()
output = call_15819
func_15820 = relay.Function([], output)
mutated_mod['func_15820'] = func_15820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15389_call = mod.get_global_var('func_15389')
func_15391_call = mutated_mod.get_global_var('func_15391')
call_15864 = relay.TupleGetItem(func_15389_call(), 0)
call_15865 = relay.TupleGetItem(func_15391_call(), 0)
output = call_15864
output2 = call_15865
func_15898 = relay.Function([], output)
mod['func_15898'] = func_15898
mod = relay.transform.InferType()(mod)
output = func_15898()
func_15899 = relay.Function([], output)
mutated_mod['func_15899'] = func_15899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15422_call = mod.get_global_var('func_15422')
func_15424_call = mutated_mod.get_global_var('func_15424')
call_15909 = relay.TupleGetItem(func_15422_call(), 0)
call_15910 = relay.TupleGetItem(func_15424_call(), 0)
func_3810_call = mod.get_global_var('func_3810')
func_3813_call = mutated_mod.get_global_var('func_3813')
var_15921 = relay.var("var_15921", dtype = "float32", shape = ())#candidate|15921|()|var|float32
var_15922 = relay.var("var_15922", dtype = "float32", shape = (588,))#candidate|15922|(588,)|var|float32
call_15920 = func_3810_call(relay.reshape(var_15921.astype('float32'), []), relay.reshape(var_15922.astype('float32'), [14, 14, 3]), )
call_15923 = func_3810_call(relay.reshape(var_15921.astype('float32'), []), relay.reshape(var_15922.astype('float32'), [14, 14, 3]), )
func_10965_call = mod.get_global_var('func_10965')
func_10969_call = mutated_mod.get_global_var('func_10969')
var_15929 = relay.var("var_15929", dtype = "float64", shape = (312,))#candidate|15929|(312,)|var|float64
call_15928 = relay.TupleGetItem(func_10965_call(relay.reshape(var_15929.astype('float64'), [13, 4, 6]), relay.reshape(call_15920.astype('float32'), [588,]), relay.reshape(var_15921.astype('float32'), []), ), 6)
call_15930 = relay.TupleGetItem(func_10969_call(relay.reshape(var_15929.astype('float64'), [13, 4, 6]), relay.reshape(call_15920.astype('float32'), [588,]), relay.reshape(var_15921.astype('float32'), []), ), 6)
output = relay.Tuple([call_15909,call_15920,var_15921,var_15922,call_15928,var_15929,])
output2 = relay.Tuple([call_15910,call_15923,var_15921,var_15922,call_15930,var_15929,])
func_15957 = relay.Function([var_15921,var_15922,var_15929,], output)
mod['func_15957'] = func_15957
mod = relay.transform.InferType()(mod)
var_15958 = relay.var("var_15958", dtype = "float32", shape = ())#candidate|15958|()|var|float32
var_15959 = relay.var("var_15959", dtype = "float32", shape = (588,))#candidate|15959|(588,)|var|float32
var_15960 = relay.var("var_15960", dtype = "float64", shape = (312,))#candidate|15960|(312,)|var|float64
output = func_15957(var_15958,var_15959,var_15960,)
func_15961 = relay.Function([var_15958,var_15959,var_15960,], output)
mutated_mod['func_15961'] = func_15961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15622_call = mod.get_global_var('func_15622')
func_15623_call = mutated_mod.get_global_var('func_15623')
call_15983 = func_15622_call()
call_15984 = func_15622_call()
func_7590_call = mod.get_global_var('func_7590')
func_7593_call = mutated_mod.get_global_var('func_7593')
const_16009 = relay.const([[-4.550002,-8.303892,-2.745063,-3.653178,-2.652225,2.277278,3.880681,5.894640,6.191591,1.172580,-5.703927,-8.943244,-7.461463,2.525766,-9.729185,2.451575,-1.834411,9.364546,2.050243,6.890270,0.778753,-3.601647,-9.106136,-3.731839,3.672013,-3.620961,6.306239,-3.503213],[-2.659472,-7.764800,8.181567,3.292626,6.156304,-8.823563,-5.534618,-1.188038,-2.820265,7.411284,-0.951235,7.516848,7.869164,1.857597,-8.739808,-6.771723,-8.803150,4.307118,-8.962475,6.818898,-4.759703,5.928139,0.344884,-5.686435,-1.719364,-1.049090,4.807634,-6.647707],[0.329985,4.723809,0.036525,3.371877,2.629901,3.908419,2.598455,6.251470,0.313457,9.097505,4.360453,-6.030694,7.810177,-2.992483,-5.203842,0.671897,3.312136,-3.630890,-7.564550,-0.628338,-0.288283,7.405916,-4.286900,1.252845,2.375325,-2.986266,-0.056725,-9.242112]], dtype = "float64")#candidate|16009|(3, 28)|const|float64
call_16008 = func_7590_call(relay.reshape(const_16009.astype('float64'), [6, 14, 1]))
call_16010 = func_7590_call(relay.reshape(const_16009.astype('float64'), [6, 14, 1]))
func_14593_call = mod.get_global_var('func_14593')
func_14595_call = mutated_mod.get_global_var('func_14595')
var_16021 = relay.var("var_16021", dtype = "float32", shape = (1, 588))#candidate|16021|(1, 588)|var|float32
call_16020 = relay.TupleGetItem(func_14593_call(relay.reshape(var_16021.astype('float32'), [588,])), 2)
call_16022 = relay.TupleGetItem(func_14595_call(relay.reshape(var_16021.astype('float32'), [588,])), 2)
output = relay.Tuple([call_15983,call_16008,const_16009,call_16020,var_16021,])
output2 = relay.Tuple([call_15984,call_16010,const_16009,call_16022,var_16021,])
func_16034 = relay.Function([var_16021,], output)
mod['func_16034'] = func_16034
mod = relay.transform.InferType()(mod)
mutated_mod['func_16034'] = func_16034
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16035 = relay.var("var_16035", dtype = "float32", shape = (1, 588))#candidate|16035|(1, 588)|var|float32
func_16034_call = mutated_mod.get_global_var('func_16034')
call_16036 = func_16034_call(var_16035)
output = call_16036
func_16037 = relay.Function([var_16035], output)
mutated_mod['func_16037'] = func_16037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14748_call = mod.get_global_var('func_14748')
func_14749_call = mutated_mod.get_global_var('func_14749')
call_16051 = func_14748_call()
call_16052 = func_14748_call()
uop_16057 = relay.sinh(call_16051.astype('float32')) # shape=(13, 3, 15)
uop_16059 = relay.sinh(call_16052.astype('float32')) # shape=(13, 3, 15)
output = uop_16057
output2 = uop_16059
func_16064 = relay.Function([], output)
mod['func_16064'] = func_16064
mod = relay.transform.InferType()(mod)
mutated_mod['func_16064'] = func_16064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16064_call = mutated_mod.get_global_var('func_16064')
call_16065 = func_16064_call()
output = call_16065
func_16066 = relay.Function([], output)
mutated_mod['func_16066'] = func_16066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15508_call = mod.get_global_var('func_15508')
func_15510_call = mutated_mod.get_global_var('func_15510')
call_16136 = relay.TupleGetItem(func_15508_call(), 1)
call_16137 = relay.TupleGetItem(func_15510_call(), 1)
func_8126_call = mod.get_global_var('func_8126')
func_8129_call = mutated_mod.get_global_var('func_8129')
const_16159 = relay.const([-4.570432,6.718125,5.438271,-2.303773,-7.491066,-6.943087,8.544867,-5.371764,-0.999413,0.619527,-9.157948,2.508878,-2.654144,9.015809,0.804004,-3.050216,-6.770336,1.529562,1.565559,-6.690620,3.245294,-9.273251,8.346422,8.593628,-4.928418,8.313476,8.897621,4.158036,7.293205,4.448771,-5.193897,-5.822880,4.837162,-9.587806,-3.854357,5.373311,5.787999,-6.416408,-9.017270,1.018780,-1.826000,-2.722210,8.212471,6.415051,-7.309333,8.480945,-9.328932,2.491306,-3.437082,-3.895891,-2.574769,-3.450876,2.260496,6.163076,6.569702,-7.828895,2.089974,8.191813,9.658291,4.878555,-2.301578,-8.829271,8.230475,-7.150569,9.309239,-6.911577,-9.936755,-7.620553,3.247142,-2.871610,-3.217943,9.826913,7.045252,-4.737276,2.907955,-9.998985,1.380134,5.825129,2.739675,-6.982434,-1.759562,-2.909308,9.376243,0.599262,-4.463473,8.404817,-8.857268,-7.193198,-6.713789,-8.095394,9.852810,1.799917,8.547368,2.515596,-9.974301,-9.063687,-0.109483,-6.102103,7.932892,-0.066899,0.121497,-4.548841,-8.612289,9.588535,1.407054,1.365599,-1.380869,0.788195,1.192190,-2.609119,-6.621049,-4.996311,-3.006235,3.371289,-2.540357,0.800643,0.253791,-9.581025,6.434997,-5.411314,4.976240,8.533758,-2.909633,-2.517239,1.466773,-8.653413,5.985677,-9.400199,9.607173,8.525628,9.435409,8.947671,-2.530927,2.958402,1.915711,-9.265694,2.226167,-7.701890,2.068639,4.135606,-1.901386,-3.781233,-3.129109,5.680497,-5.739739,-3.117351,5.792594,4.797074,1.538655,7.835949,-4.186988,3.683850,9.468244,-3.609454,-4.179825,0.606982,8.999612,-9.357310,-5.240867,4.180148,-3.602835,2.478709,3.736822,6.872165,1.735506,3.237470,2.072797,1.695393,-4.807942,9.531849,9.016176,2.756249,-2.618281,-9.601098,2.188956,-8.749594,7.199771,-8.122144,-3.209480,8.724545,-1.349723,2.809380,-3.500065,8.446150,-7.361161,9.628866,2.099660,-1.648648,1.142609,8.803455,-0.475898,-4.456047,5.955024,-0.433195,4.854912,0.676645,-1.926616,7.771869,8.311981,-9.541127,8.391184,5.473343,-4.940144,-1.279692,-6.377186,0.657808,3.602776,9.274223,-1.471377,-1.655044,7.442375,9.774037,1.578111,-4.697924,1.035805,-8.688415,3.365680,-6.546056,-4.640835,5.353397,-3.102638,5.485562,-2.119523,-9.719062,1.526421,-2.351131,-9.621613,-1.723944,-0.351387,-1.006379,6.958170,-8.932892,-4.093615,1.922276,-1.321289,6.435583,3.598072,-3.224609,1.704212,-2.036858,-1.765759,-4.682703,-8.253413,-1.934087,0.119970,0.740356,4.169922,5.404166,-9.054216,-9.545484,9.215298,2.003151,8.854319,3.157540,-6.508221,0.981669,-1.674932,6.436555,-6.087432,-8.179373,-4.055043,8.036944,5.861305,5.039608,2.084859,-1.324809,2.231138,5.410366,-3.385733,-8.380994,-6.885075,6.813510,2.619256,7.778852,-9.175076,7.772836,1.203330,-2.873706,-5.890346,-3.818028,-8.986036,-8.162884,-5.234102,-0.549553,-2.457469,9.043859,-5.148687,-1.466813,1.717300,1.049827,2.541108,-5.009490,6.684454,2.231921,-0.679479,3.218215,3.663373,7.210040,9.387223,-4.134885,-4.373363,-1.415670,-2.274881,-8.629901,0.738643,8.038003,-5.456389,7.088736,-1.840147,4.184013,5.338020,6.959982,7.497122,-6.925413,-9.190067,-3.537355,7.495742,1.865312,8.518401,8.579249,-9.298666,5.817100,6.867479,-7.609311,-7.197995,-1.467492,6.162584,-2.936779,-7.244746,8.449920,2.407516,0.841238,5.577389,-2.191522,-9.515077,1.553616,-4.507718,-1.145671,1.427612,1.096515,-0.251872,1.568608,-9.095096,-1.259808,6.303953,9.885941,-5.019077,0.304841,-6.573668,-6.086385,5.374124,2.519375,6.474307,2.056091,-1.599062,-8.110811,2.774650,-5.557850,0.819567,-5.819925,5.627898,0.561787,3.095835,4.169126,-9.404284,-1.458778,8.391324,8.185120,6.534289,9.268837,0.232128,2.888745,-2.214906,-4.621233,-9.204416,-7.092945,6.010408,9.543627,-5.589879,-6.381727,5.301359,-1.850782,-4.485401,4.878488,9.107431,9.888222,-8.156326,0.824492,8.911259,-6.188737,-4.946290,3.485263,-0.564834,-8.557335,5.108476,5.100451,-9.847653,9.320706,8.597880,-5.497934,7.873817,0.483440,-5.259829,-1.818702,2.640737,-9.914809,3.392617,8.528729,-9.990710,-8.472768,-7.844158,-7.148927,-6.324873,7.014992,-4.332746,-3.724631,6.995681,9.624162,-5.256402,0.001330,-8.319238,9.020401,2.980165,2.373075,0.514661,9.389252,1.413919,-8.048266,0.192894,2.874337,1.416698,-6.443319,-4.622479,2.105925,4.321282,-3.285272,-8.684909,-0.852460,-5.055651,6.027182,7.356127,6.085997,1.270725,-2.641993,5.666240,-4.553358,2.815997,1.859787,9.443173,-6.883217,-4.329436,-3.416934,1.008815,-1.137388,3.289482,8.574038,1.417759,3.543533,-9.875157,3.330084,-9.424241,-9.707380,-1.080873,1.058232,-8.048079,6.696084,-8.824293,5.650101,-0.786906,9.567930,-3.921642,-2.697718,8.192087,-3.411027,-1.827718,3.950936,5.671622,-5.131181,7.949059,2.024125,-8.444615,-2.806174,7.756336,-6.302939,-4.523872,6.092758,-3.609709,-7.274285,2.000434,6.078284,-2.303889,-7.173589,-5.709485,-7.531244,-8.272473,-0.373296,-9.059638,2.493581,-5.057649,8.537612,9.866879,9.956394,-6.811534,1.582554,-3.642349,4.784746,8.578844,0.116594,3.418487,-5.011414,6.486863,-7.134992,8.552416,5.495682,0.123151,-2.538372,1.995862,-1.092985,6.483083,-2.974925,-0.961950,9.737842,2.850115,0.435418,-7.568503,2.317809,-4.187161,7.553245,8.865726,-1.264082,6.544023,-1.924214,-9.333641,-1.122621,-1.833254,-3.798200,3.554809,4.244216,-1.935823,1.338419,-5.989755,-6.555447,-2.093822,-1.234863,6.924846,-2.891477,-0.181331,5.437567,8.977606,-0.220417,-0.539698,-7.516384,-5.043458,1.460239,-2.297867,7.220090,8.166336,-3.247022,1.829806,6.662717,6.308535,7.485806,-9.575482,-4.096366,7.613486,-1.317542,1.219505,1.943646,-0.240396,-4.518432,2.796856,7.704723,-3.425327,-1.848433,-7.096406,-4.610152,6.312765,2.892371,-9.904754,7.323268,1.913535,-5.692046,-4.472467,-7.993419,-9.192646,1.121930,4.232169,-5.495821,-3.735067,3.590750,-1.056119,-6.718657,-9.925861,-4.727223,-6.107706,-7.606015,7.906556,-5.377979,-2.063686,-2.803116,-5.658417,-4.635469,-0.718880,6.083398,8.483976,6.741568,-0.656082,4.032937,-0.452632,4.273032,7.436670,-6.333120,-8.207606,-1.138600,2.333326,9.008703,-9.206146,7.932693,-6.457072,-4.613672,-5.403010,-5.765476,2.005698,3.262508,3.112086,-6.511413,-9.114877,0.447328,-5.104172,6.222067,-2.541848,3.988501,-4.438341,8.889596,9.573252,-0.952359,2.528338,-9.579551,-6.565472,-2.026750,-8.651624,-0.750927,2.112737,-4.423197,6.305001,-4.989857,-6.851417,-1.845595,-6.929859,-0.551894,3.668836,3.965008,8.845887,-6.328360,3.330333,0.680201,5.683339,-1.638395,5.696668,-9.482514,-7.455546,-0.761068,-3.653329,8.768071,-9.628573,-8.189213,-6.788122,-5.026840,6.905508,2.097627,-5.554583,6.405145,-7.236102,-6.114255,-3.683145,-3.187199,8.417750,1.128228,-3.798607,8.696920,-5.052293,-8.365243,5.661077,-4.793540,9.295929,-1.033295,-8.183765,-0.877973,9.157411,-6.810480,4.487221,7.425147,0.704329,5.028464,0.490357,-1.246755,-0.716454,6.594107,-4.106685,9.540532,2.461754,7.619756,2.437356,3.093297,-5.960777,-7.061941,-5.402666,4.645142,-8.002029,8.951194,6.676106,-2.295873,5.662373,1.857753,2.863202,7.363723,-7.904676,3.145140,-1.291915,2.197389,-3.105396,1.576997,6.970386,7.370826,3.334145,4.482391,-0.331682,-2.577952,8.817067,7.482237,-2.763124,-2.387298,6.124658,-4.891211,-5.871554,5.227453,8.781668,5.936169,6.122237,8.854678,-1.894369,9.078428,-1.081936,-6.117193,9.119513,-7.084800,-9.349175,7.868827,-8.714727,-8.525399,1.572471,-1.493625,-9.888952,2.246638,-9.759821,-1.102077,9.822824,2.462858,0.292123,-5.475901,-9.245229,9.247616,8.030586,-8.277666,-6.708516,-6.400605,-2.020342,9.198146,-3.100173,-5.178952,1.637940,4.893299,-4.148540,-2.187077,-4.895819,1.764719,1.366545,-2.390264,3.474827,7.002978,6.270767,3.845669,-6.348919,-2.745630,5.587221,1.710159,6.655043,3.001181,8.132683,3.514472,-0.178804,-6.561414,2.709580,-4.844333,-3.492272,0.634820,0.365690,9.901255,1.797105,8.482976,8.063210,5.824221,4.187593,-5.158812,-6.020522,4.740754,-0.650755,-6.816351,-7.340050,-5.895661,-2.276587,-8.271991,-4.470282,6.304915,6.355827,-8.387221,0.993276,6.207289,8.063376,-4.510322,2.044139,-1.573442,3.371736,-6.080960,-0.904602,-8.483717,-1.381269,-0.279430,6.873382,-2.444002,-4.170604,2.556735,-3.971520,6.813437,-1.236134,9.667445,3.234730,-1.432769,-9.462823,-2.445674,8.537724,-5.511820,8.865291,7.140427,-5.634814,2.289896,-5.586310,8.417824,6.335651,-6.609975,-2.923170,6.798816,-8.409129,-2.797071,-4.623898,9.198494,-0.548826,5.149234,-2.675352,-0.184312,-3.930455,-9.941914,-0.397979,6.568232,-3.470108,2.329161,4.662042,-3.476696,-9.727558,1.563978,2.111275,6.992496,-2.794658,6.590392,2.037190,2.764741,6.772192,-5.069658,9.895541,7.128547,-2.319476,-9.205036,8.068731,2.254268,-3.400906,3.928301,9.649323,0.984142,4.170290,-6.513886,-7.101312,5.379314,3.835206,8.238901,8.239761,-4.818052,7.060821,-1.945940,3.561183,4.337535,-4.480008,9.669668,3.694784,1.254743,3.501533,1.988485,0.433035,4.209377,-2.101039,-4.515568,2.263983,2.138052,4.590924,-4.596393,1.213018,-2.822654,-2.008564,2.232990,-7.591035,-5.405478,3.492171,2.441502,-3.320375,3.818369,0.614411,8.692478,6.182084,-7.221971,-5.573002,3.217406,-8.583468,2.759504,-9.587553,-7.076992,0.449573,-3.668228,-6.512367,0.934424,7.091679,7.475474,-2.478577,1.321833,-0.999818,1.046663,-9.633823,-3.395267,-6.066692,1.419252,9.261677,-1.207227,0.502865,5.346449,-5.202930,-5.991580,1.816837,5.968047,-6.269794,8.144488,-7.490018,7.464146,-6.930733,9.100949,9.921563,7.456689,-5.250429,7.357054,-6.544716,1.865838,-8.023180,-5.174709,5.433455,8.274175,3.251694,-1.445863,1.654183,-4.641815,-8.603034,5.086437,5.501155,-4.441116,-2.549592,4.420078,-3.262000,6.286227,-0.834997,-7.918938,4.840405,-3.751984,3.587485,-2.300764,-1.500258,-2.353171,-5.179321,8.291814,-8.222670,3.997125,3.869926,5.070947,0.846782,-2.497105,7.061623,-1.020247,3.244600,9.177244,4.025393,5.608123,-8.256760,-0.189729,1.746666,-5.297908,6.741013,-6.457176,-4.242879,-6.376638,1.578647,-4.391955,-3.823892,8.550445,5.054414,-7.297526,6.782353,-5.561828,7.423204,-2.907956,-2.600513,-8.075859,1.312969,7.662061,-3.344997,2.095268,-6.041084,-2.889436,-2.680590,-0.516701,-4.909045,0.330296,0.753328,-8.247119,-2.770059,4.686833,6.988131,5.176117,8.785087,3.442823,-6.201905,0.713555,-2.434429,8.165116,0.959594,-9.255671,-8.273131,2.216209,2.102849,-4.208453,8.593157,0.507827,9.363764,7.567575,4.751298,7.595967,9.179476,-6.107304,-8.461705,4.515665,-9.440084,-7.609178,6.910543,-7.263748,0.967013,-0.447902,-4.602577,1.811203,-8.277182,-9.863684,2.914557,-5.389932,-4.527914,-9.421179,-6.405278,7.932933,7.906622,-1.511907,0.083238,-0.633387,7.466348,0.303490,-5.127401,-2.114657,7.872141,-4.421908,-8.983689,-9.522122,6.200738,5.510182,-7.642997,-5.854429,-5.190865,-9.284029,0.836125,-8.074820,6.643834,6.185793,4.178563,3.286596,-1.736460,5.332815,-0.059374,-9.069045,3.803850,3.010329,-6.552627,1.526125,-7.323084,-6.044820,-1.846082,3.580794,5.407799,1.358542,-6.307500,5.225458,-2.694357,6.655772,-7.879991,1.145471,4.903906,2.033709,-4.476033,4.507437,-3.430868,3.549639,-4.452807,3.010302,2.154438,-6.305745,8.380503,-7.352482,4.184829,-1.399851,0.594177,2.143470,-0.664876,-4.248186,1.627061,-0.257783,-4.527689,1.116784,-0.424825,-7.818123,7.536907,7.527344,-7.277412,0.604320,6.665498,-6.373205,7.949157,3.556144,-2.259786,-4.788761,5.016450,-9.918521,-8.846854,4.992254,-1.987473,-3.273190,-1.348986,-2.270068,-3.573992,-4.428310,1.524085,-3.737280,-5.956078,-3.607418,-2.185707,8.292520,8.626231,3.371936,8.649626,-8.433028,-0.446396,2.901235,-9.075301,2.050385,9.939496,-9.166032,-5.295343,1.557748,1.466727,-1.132566,7.486035,2.642258,4.860084,-5.661380,9.557765,-5.925744,-2.852934,1.728957,8.532149,5.598198,-9.774529,1.021580,-5.775565,-4.352798,-1.634061,2.750012,-8.922364,8.960256,7.286273,-9.147666,-2.949663,-8.815703,-9.591206,-7.473973,4.647428,6.960021,7.853382,-2.255588,5.116467,5.635934,8.939667,0.492746,-3.042201,1.627837,6.946251,-6.751907,-3.423420,-1.830591,-8.318287,-5.086912,-3.480157,-4.507047,-7.611745,1.904103,2.452791,-0.210101,-9.561587,-4.405489,-1.081145,-7.840736,9.037868,6.401264,-3.128043,-7.801642,-3.639247,-7.160848,-4.655629,2.579889,3.553176,3.749010,3.104290,-9.478898,3.537957,-2.433167,-6.485927,1.250877,-4.453326,-9.823132,-3.006143,1.024922,3.594773,9.912211,-8.198920,9.623261,-7.149805,-8.734113,-2.819566,7.543105,6.786236,8.758140,-7.124565,7.554726,3.552129,6.674789,6.693667,6.108231,-0.798337,-7.418469,4.190970,9.199092,-2.180281,7.174794,-4.995286,4.540060,8.324537,6.253725,9.415868,-8.415802,-9.982217], dtype = "float32")#candidate|16159|(1287,)|const|float32
call_16158 = relay.TupleGetItem(func_8126_call(relay.reshape(const_16159.astype('float32'), [13, 9, 11])), 0)
call_16160 = relay.TupleGetItem(func_8129_call(relay.reshape(const_16159.astype('float32'), [13, 9, 11])), 0)
func_6800_call = mod.get_global_var('func_6800')
func_6804_call = mutated_mod.get_global_var('func_6804')
var_16174 = relay.var("var_16174", dtype = "bool", shape = (528,))#candidate|16174|(528,)|var|bool
var_16175 = relay.var("var_16175", dtype = "int16", shape = (1404,))#candidate|16175|(1404,)|var|int16
call_16173 = relay.TupleGetItem(func_6800_call(relay.reshape(var_16174.astype('bool'), [12, 4, 11]), relay.reshape(var_16174.astype('bool'), [12, 4, 11]), relay.reshape(var_16175.astype('int16'), [1404,]), ), 1)
call_16176 = relay.TupleGetItem(func_6804_call(relay.reshape(var_16174.astype('bool'), [12, 4, 11]), relay.reshape(var_16174.astype('bool'), [12, 4, 11]), relay.reshape(var_16175.astype('int16'), [1404,]), ), 1)
output = relay.Tuple([call_16136,call_16158,const_16159,call_16173,var_16174,var_16175,])
output2 = relay.Tuple([call_16137,call_16160,const_16159,call_16176,var_16174,var_16175,])
func_16184 = relay.Function([var_16174,var_16175,], output)
mod['func_16184'] = func_16184
mod = relay.transform.InferType()(mod)
var_16185 = relay.var("var_16185", dtype = "bool", shape = (528,))#candidate|16185|(528,)|var|bool
var_16186 = relay.var("var_16186", dtype = "int16", shape = (1404,))#candidate|16186|(1404,)|var|int16
output = func_16184(var_16185,var_16186,)
func_16187 = relay.Function([var_16185,var_16186,], output)
mutated_mod['func_16187'] = func_16187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14157_call = mod.get_global_var('func_14157')
func_14158_call = mutated_mod.get_global_var('func_14158')
call_16204 = relay.TupleGetItem(func_14157_call(), 1)
call_16205 = relay.TupleGetItem(func_14158_call(), 1)
output = call_16204
output2 = call_16205
func_16236 = relay.Function([], output)
mod['func_16236'] = func_16236
mod = relay.transform.InferType()(mod)
mutated_mod['func_16236'] = func_16236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16236_call = mutated_mod.get_global_var('func_16236')
call_16237 = func_16236_call()
output = call_16237
func_16238 = relay.Function([], output)
mutated_mod['func_16238'] = func_16238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15622_call = mod.get_global_var('func_15622')
func_15623_call = mutated_mod.get_global_var('func_15623')
call_16256 = func_15622_call()
call_16257 = func_15622_call()
func_15709_call = mod.get_global_var('func_15709')
func_15710_call = mutated_mod.get_global_var('func_15710')
call_16270 = relay.TupleGetItem(func_15709_call(), 1)
call_16271 = relay.TupleGetItem(func_15710_call(), 1)
func_14709_call = mod.get_global_var('func_14709')
func_14711_call = mutated_mod.get_global_var('func_14711')
call_16277 = func_14709_call()
call_16278 = func_14709_call()
func_11132_call = mod.get_global_var('func_11132')
func_11135_call = mutated_mod.get_global_var('func_11135')
const_16285 = relay.const([0.723537,7.603882,3.007261,5.551021,9.113769,9.892225,-0.206241,3.838688,-1.370515,8.104030,7.554280,5.939493,2.615427,-1.199674,-8.886812,7.456269,-4.213204,9.717790,-2.175359,-8.422326,-3.151573,4.800173,-4.115695,-7.900870,-0.044314,-9.637376,-1.573500,-3.717946,1.408512,-8.188144,3.119753,-7.537254,5.014589,-0.756658,-3.935127,5.567565,-3.241460,9.303144,6.411530,-5.149820,2.925944,5.252012,-3.127834,6.749091,-4.990437,7.392186,-3.226551,2.911373,5.359116,6.562386,9.011125,1.523488,-5.269399,-9.832049,-4.822985,6.404006,2.870789,9.423734,0.027413,8.334553,-6.589335,2.419423,-9.130841,-1.825839,-8.921132,7.571836,-5.341901,-3.619081,0.136925,1.068774,7.289638,6.925250,3.507933,-3.482271,-9.107659,8.289215,-3.851277,6.342642,2.237192,-2.942410,1.022805,3.644260,-2.402364,-0.519328,-3.589236,2.402777,2.039243,-2.105296,8.852349,0.671797,3.311032,0.305431,7.785355,-8.272685,-7.563211,0.133184], dtype = "float64")#candidate|16285|(96,)|const|float64
const_16286 = relay.const([-2.468893,5.937551,-3.256031,-6.030014,-4.907330,-5.932782,3.194109,0.324945,-7.127219,-2.972086,7.754981,6.396859,0.887714,8.382718,3.040465,6.926082,1.666975,2.588187,3.054742,5.516180,-6.511840,-0.939257,9.912533,-2.605952,-9.428558,6.144339,-4.946753,7.803392,7.167104,-4.138678,-4.230709,-1.753462,-9.090303,0.444087,3.548567,5.340959,4.989259,1.844303,0.962987,-8.945551,-0.601247,4.239000,-2.550197,9.501223,-1.538143,2.817342,4.426131,-9.975693,1.510415,3.169607,-2.072958,-4.502233,-9.731214,-7.245232,-9.842554,2.166081,-6.509506,3.810129,-2.999318,4.928270,-2.415592,2.931945,-7.485746,5.756591,-3.793387,4.330410,-0.505367,-2.028945,2.358531,-8.775684,9.650310,7.226372,7.505584,6.631600,5.218126,-5.635648,9.082126,4.210584,0.813217,3.905085,0.471780,-0.384785,-8.860205,3.191040,4.715442,8.227041,5.882103,-3.179369,0.109126,-6.116481,-4.997045,-0.160761,5.219472,-2.996033,6.522034,-7.157834,-6.817030,-3.145724,6.393325,-3.266253,6.790281,7.915603,-0.625818,6.439265,4.710797,-9.016862,-4.307144,4.899825,-1.588131,-8.465181,8.566468,0.676668,7.481802,8.031285,6.554769,4.101016,8.252343,9.645107,6.924402,-5.643107,6.668254,-8.120573,7.817513,0.303973,8.292367,1.193399,-5.017128,-7.519362,-9.738882,-5.803972,-1.206054,1.419289,-4.976748,9.427998,5.402229,9.249235,1.265322,1.129124,9.184176,-9.415210,-3.236939,-8.796299,-3.930262,9.521250,-8.647743,-5.834453,4.711660,-8.418288,8.735311,5.489206,8.550279,2.855030,0.050327,-3.243688,3.280242,7.783865,-7.933853,-7.132235,7.079869,-4.082194,4.962884,-3.684012,-1.718137,-1.944369,-9.188066,-2.524150,-2.911691,-4.993855,-5.423903,0.442817,-1.527052,-4.862546,-4.538668,8.267693,-0.712792,5.484516,6.764571,-7.683386,-8.792618,0.716132,8.698825,8.092212,1.727334,8.965666,-1.688687,3.401959,3.651874,7.619136,-3.431225,1.206036,-9.672897,-8.065691,-2.658673,1.559427,3.468818,-0.220850,9.643327,3.669845,1.720067,-6.702118,3.809274,-9.753333,6.874273,-3.818738,4.772514,-4.291008,-9.459950,2.701055,-9.889243,6.843296,8.260154,-6.836648,2.004852,2.991191,-0.622874,-7.530823,0.146013,-0.568175,7.715591,-4.963831,2.201902,-1.680435,1.708952,-8.989241,3.537289,2.972336,1.366294,6.532225,2.502987,-1.070543,-8.996279,0.559961,1.099564,8.271833,-3.042712,7.031146,-9.699081,3.691070,1.884307,9.954336,-3.913525,9.860992,-5.341950,-9.688819,0.645043,8.453525,-3.237101,3.460662,7.903016,-4.141891,-7.170529,2.289297,4.316609,-6.838375,-1.418795,5.763148,3.150100,9.653548,3.289989,2.686165,-8.544096,8.159721,-9.384395,-1.692626,3.204277,2.350461,6.264367,-0.954144,-7.398741,3.349152,1.431755,8.275995,-1.654318,-7.487621,-8.520712,-1.340014,7.161999,1.636912,5.258564,9.303479,-7.503890,-3.948846,0.251582,2.984225,-3.075291,-3.125595,4.212569,-8.080264,-8.096295,-3.821815,-3.682570,2.040322,-7.559561,0.965702,2.714708,-9.670399,-8.824615,4.047931,5.042324,9.427574,8.973943,6.663177,8.433757,-1.798859,9.405479,-6.200301,-0.277070,9.389035,2.024094,-5.382612,8.995694,-3.023274,8.972915,8.083868,-4.950743,-9.440608,-8.147479,5.152702,3.811707,-1.800452,-4.006668,5.747612,-4.465656,2.492717,3.978551,-0.846216,-5.353616,-1.453420,-4.251595,-4.076353,-8.954329,9.026818,9.504793,-2.409318,-9.102084,6.343135,-2.888690,3.522992,3.511158,-4.609998,-4.579609,5.850942,6.018837,4.078604,5.450731,0.928768,-9.428619,-0.213573,9.097426,5.570355,8.487536,-9.724947,1.437753,1.230490,-2.766766,5.260497,-8.445496,1.628296,2.352306,-1.514020,-9.241626,-4.630188,-3.952257,-4.541687,-1.513449,3.779312,-7.446054,8.261958,-4.599415,-1.419658,-9.873991,8.399712,-8.484680,-8.781605,2.245371,-2.543696,-5.097112,3.015269,-9.075831,-8.937243,9.045826,-2.742914,1.443214,0.209947], dtype = "float64")#candidate|16286|(384,)|const|float64
call_16284 = func_11132_call(relay.reshape(const_16285.astype('float64'), [16, 1, 6]), relay.reshape(const_16286.astype('float64'), [16, 4, 6]), )
call_16287 = func_11132_call(relay.reshape(const_16285.astype('float64'), [16, 1, 6]), relay.reshape(const_16286.astype('float64'), [16, 4, 6]), )
func_14073_call = mod.get_global_var('func_14073')
func_14075_call = mutated_mod.get_global_var('func_14075')
call_16294 = relay.TupleGetItem(func_14073_call(), 0)
call_16295 = relay.TupleGetItem(func_14075_call(), 0)
func_15245_call = mod.get_global_var('func_15245')
func_15253_call = mutated_mod.get_global_var('func_15253')
var_16302 = relay.var("var_16302", dtype = "float64", shape = (364,))#candidate|16302|(364,)|var|float64
const_16303 = relay.const([9,10,-3,-10,8,1,-8,-5,7,5,10,10,1,-6,-1,2,-10,-1,-3,1,-10,9,3,-3,1,-10,9,1,-9,-10,-9,-8,5,1,10,-1,4,8,-3,-10,9,7,9,8,4,-6,-2,-1,4,7,4,6,-8,-7,-7,5,-6,-6,10,-5,-3,9,-7,-2,-4,7,-7,-8,-9,-7,-4,4,5,-9,7,-1,-4,6,3,-4,-7,5,-6,-10,-9,-5,1,5,1,-3,7,-9,-4,-4,-4,-4,-1,-6,3,6,-7,7,2,4,-7,2,-10,-6,-9,-1,-1,6,5,3,-10,-10,-9,4,8,-7,-4,-8,1,9,4,-2,5,9,10,8,10,-8,2,2,-8,4,7,4,-3,9,3,2,-9,-9,-2,10,4,3,-8,7,-4,-7,2,3,6,-5,-3,-8,10,3,8,-6,-9,-10,3,-4,8,-2,-5,-6,-6,10,9,-4,-9,1,-10,10,7,8,-7,9,-4,-8,5,-7,-6,-10,9,4,-1,-5,-3,2,-7,9,3,-1,-10,-3,4,6,1,5,-10,-7,-3,5,9,5,8,-8,-4,7,10,9,-3,4,-10,3,-9,2,3,9,5,-6,9,-5,6,5,3,2,8,10,-6,-6,3,8,-7,10,10,-4,-3,-10,-10,-5,-10,9,-2,3,-3,-4,1,6,6,10,3,4,5,-5,2,8,-8,9,-9,9,-3,8,-4,2,10,7,-7,9,9,-7,-5,-3,3,2,-6,3,5,-3,-8,8,-6,1,-6,-5,4,5,8,-10,-2,2,7,-7,-1,-1,5,6,4,7,8,6,4,1,1,-3,-8,-1,2,-9,-6,1,2,3,5,-8,1,-6,7,-7,9,-1,6,-3,-8,3,-3,-7,2,-10,1,-1,-6,-7,4,-1,-3,1,-6,8,-7,10,-5,-2,7,5,2,10,5,-10,1,-4,-8,4,1,8,4,7,-4,-8,3,-9,-3,4,8,9,-7,-4,1,-7,-1,-10,2,6,-8,-7,10,-7,-6,-1,5,4,2,-5,9,5,6,6,-5,-3,7,-6,-7,9,4,-10,9,-8,-5,6,-6,5,-8,-1,-3,10,6,8,8,1,-1,-8,-8,-3,-1,6], dtype = "uint32")#candidate|16303|(420,)|const|uint32
var_16304 = relay.var("var_16304", dtype = "uint64", shape = ())#candidate|16304|()|var|uint64
var_16305 = relay.var("var_16305", dtype = "uint64", shape = (288,))#candidate|16305|(288,)|var|uint64
const_16306 = relay.const([4,4,-4,-6,-4,-7,-2,2,7,-2,8,9,10,8,9,-10,3,-4,-8,5,5,6,-10,1,2,6,-7,10,2,7,-5,6,-2,-4,-3,4,-1,-5,-9,-10,-2,-5,-9,6,10,3,-4,-5,1,7,-6,-10,-1,8,3,-3,2,4,10,5,7,7,-8,8,-10,1,-7,-5,-8,-8,-2,-8,10,8,-3,-2,-10,2,1,-5,-4,-1,1,-9,10,4,10,-6,3,2,4,8,3,2,-9,-5,7,-4,-1,-1,-10,-2,-4,-3,-2,-3,-9,2,9,3,5,3,-5,2,9,8,-6,-2,-1,-7,1,1,9,9,-9,9,4,6,6,5,1,7,-6,-8,-3,9,-3,4,-6,-3,7,1,-4,1,6,7,1,-5,-10,-3,-5,9,-3,-3,7,-5,10,6,-2,-3,-4,6,-2,-4,1,9,10,-8,-2,3,9,-4,4,2,-8,6,5,9,2,-4,-3,-1,-3,-7,1,6,9,-8,1,-9,-5,3,7,-7,-7,4,-6,-4,-5,5,4,8,5,-6,-6,-7,2,-8,4,-9,-8,5,-9,2,2,2,1,9,5,-4,2,9,5,-4,7,-4,-6,7,-7,-1,-6,-7,2,7,-3,8,6,9,9,2,7,-8,-2,10,6,10,-4,-3,3,4,2,-1,-3,10,6,-7,6,7,2,9,7,-2,-6,-7,-4,5,5,2,10,10,-4,8,2,-9,-1,4,8,10,8,5,10,-8,7,5,-2,3,3,7,7,2,6,7,-10,10,-4,-10,4,-9,7,-8,10,8,-3,7,-3,-7,4,5,-10,-4,1,-7,3,7,2,1,-9,3,6,-1,10,-7,1,-8,10,-3,7,5,-8,10,-10,-9,-1,-8,-2,-5,-6,-7,-6,-7,-9,7,-2,6,5,-9,-8,-3,-1,-6,-1,-5,5,3,9,10,-2,-3,-9,6,6,10,-4,-3,-3,9,-9,-10,-8,-8,5,-6,4,3,10,-9,7,-10,-2,7,1,-1,2,-7,-6,-1,4,10,-9,-1,-6,-7,2,3,8,1,-8,2,-4,2,5,-1,-1,6,7,10,10,4,3,-5,-7,-2,1,-5,-4,-4,-10,-7,7,-2,-1,-6,10,-2,-9,-5,7,3,3,2,-7,-10,1,-2,1,3,-6,4,2,8,4,10,-3,9,3,7,6,-10,5,5,4,9,-8,-6,8,2,7,3,-6,-8,-4,10,-10,-6,10,10,-9,6,9,-8,5,-1,3,-4,8,8,5,-9,8,-10,9,4,9,7,-1,-7,6,-1,-1,8,7,9,-3,8,6,-10,8,-2,2,-4,-6,-1,6,3,-7,7,6,5,-6,9,-1,-8,-2,5,-10,9,8,10,10,-3,4,-10,-8,10,-7,10,7,-6,-8,3,10,6,1,-3,-9,9,-8,6,3,-4,4,-10,-1,9,9,-5], dtype = "int64")#candidate|16306|(546,)|const|int64
const_16307 = relay.const([[6,9,-7,6,3,-6,-10,5,5,-2,7,5,10,2,4,5,1,-7,-10,-10,-9,-3,9,-2,7,-7,4,10,10,1,8,-3,9,-7,5,2,-4,-4,5,5,-9,-6,-6,8,10,1,7,-7,6,-5,-1,-4,4,-8,-3,10,-9,7,-5,-3,-6,5,10,2,-7,-6,6,3,-9,8,6,-6,-6,-10,9,6,-10,1,-4,-6,1,-7,-10,-6,3,-1,-4,6,9,9,-1,-5,7,-9,-8,9,-6,8,-1,5,8,5,-4,-2,-6,2,9,8,-3,6,-3,3,-3,5,5,10,-7,-7,-7,-5,3,10,-5,7,-5,-1,10,-6,-5,9,-3,5,-5,3,3,-4,-7,10,5,2,-2,8,7,5,7,3,-4,-1,1,10,4,-4,-10,-7,-2,5,-9,6,-9,9,-6,5,1,8,2,7,1,8,-6,6,-3,-5,-4,-10,1,-8,-2,-6,10,4],[-1,-9,4,6,2,1,-5,-8,7,-3,-7,-7,5,-1,-7,-9,8,1,-5,4,-8,-3,-1,-3,10,7,6,-10,7,-6,-8,1,2,8,8,7,6,1,2,6,-10,3,8,5,-3,-10,-7,-7,-4,6,-6,9,2,1,-6,8,-3,9,2,-9,-6,-8,-1,-2,9,-8,-3,-10,9,-1,-10,10,-9,9,5,-10,6,-4,2,-3,-5,7,7,3,9,-2,2,-4,-1,6,-10,6,2,-4,-7,-5,-9,-10,-8,-4,-4,5,6,-1,-2,-4,-1,10,-2,8,-3,-2,5,-1,-5,-9,-1,7,6,6,-4,2,-1,-1,-7,4,1,-4,-10,-1,-10,-3,5,-8,-1,10,-3,1,5,8,-10,-3,10,9,-2,4,1,3,-1,-10,3,8,-2,-1,10,10,4,2,1,-4,4,-7,7,-2,8,1,-1,7,-7,-2,-10,6,6,-7,-9,-1,9,9,-7,6]], dtype = "int64")#candidate|16307|(2, 180)|const|int64
call_16301 = relay.TupleGetItem(func_15245_call(relay.reshape(var_16302.astype('float64'), [364,]), relay.reshape(const_16303.astype('uint32'), [5, 84]), relay.reshape(var_16304.astype('uint64'), []), relay.reshape(var_16305.astype('uint64'), [288,]), relay.reshape(const_16306.astype('int64'), [546,]), relay.reshape(const_16307.astype('int64'), [6, 60]), ), 4)
call_16308 = relay.TupleGetItem(func_15253_call(relay.reshape(var_16302.astype('float64'), [364,]), relay.reshape(const_16303.astype('uint32'), [5, 84]), relay.reshape(var_16304.astype('uint64'), []), relay.reshape(var_16305.astype('uint64'), [288,]), relay.reshape(const_16306.astype('int64'), [546,]), relay.reshape(const_16307.astype('int64'), [6, 60]), ), 4)
func_14438_call = mod.get_global_var('func_14438')
func_14442_call = mutated_mod.get_global_var('func_14442')
const_16312 = relay.const([7.275425,-7.732456,-2.314460,-1.732280,4.332131,-4.688113,0.143487,-3.837924,-3.760925,8.971439,-0.537469,-4.596045,-3.362734,3.608833,-8.040929,5.196403,4.792911,7.627944,6.784285,4.385016,6.183636,2.713921,2.955638,2.136463,-2.516888,2.172900,8.065952,9.269254,9.484287,1.091475,-9.667808,-9.047210,6.165137,5.307099,4.676382,2.636492,-7.664511,1.584506,-9.261012,7.192091,-3.597942,-2.002066,9.241047,0.237296,-0.217725,-5.752367,9.616483,-7.303218,-5.011304,6.067039,-3.786382,0.780441,-9.409579,-2.768659,5.963695,7.547359,-7.505648,9.248522,6.663272,6.886945,-9.537158,-7.002347,-9.803706,-9.663107,-8.825367,-3.673884,-8.909879,-4.525781,-0.325418,-1.831920,-2.903004,9.207789,3.491074,-0.063572,1.931693,-3.382282,2.701499,-8.810712,4.924812,3.330208,-0.681869,-3.596096,9.827420,6.019049,5.200057,1.052984,3.428456,6.717369,-6.980967,-8.177596,5.640201,9.989314,8.129516,-6.143475,-1.377443,3.090290,5.198646,2.759047,-4.343829,-5.754785,-6.377071,1.173894,1.797612,-5.379429,6.695279,0.338627,3.449934,7.626520,-8.000601,7.345368,2.966439,-5.476905,-4.105625,5.159749,-9.850685,6.521670,-2.429778,6.503035,9.034259,4.923819,-7.526843,5.593578,4.471031,-9.774954,-9.588441,-2.574362,-1.423725,-5.376355,-9.048798,9.854598,5.671688,-0.917453,-1.833434,6.884101,2.966671,-8.595884,-1.187972,-4.940372,-4.023094,4.594642,-1.304319,2.165488,-5.642840,-1.697502,2.970999,-9.010846,-8.721802,-9.459188,-0.178837,-1.943871,-2.130282,4.823463,-2.908368,-4.477302,-5.765196,1.942842,7.441734,-5.789989,-1.249019,5.908996,-7.050853,-9.790749,-1.969709,3.507367,1.260080,-4.241136,-9.312989,-0.099613,6.597785,-6.440867,-9.593702,3.126893,-0.415748,-7.952821,-5.053675,-6.595239,4.940114,0.775808,-3.705433,-2.166533,-1.010053,5.465161,-4.160574,8.228897,4.753758,6.421048,6.386544,8.729059,-8.005822,-9.552556,8.110699,-1.610811,0.624157,-5.074840,-0.341641,6.111793,-8.596418,-8.648714,-8.293977,-3.089996,5.460196,-9.626482,-2.589912,-5.971952,1.219234,8.831990,3.550714,4.436252,7.249459,-9.038712,-4.954219,-0.797647,4.754677,2.780938,-3.733996,3.842910,5.024455,-7.966857,1.376468,0.079388,4.928189,-2.889398,-1.041107,-5.051607,0.365567,0.296366,-2.542301,-1.707606,-9.926480,-8.756187,-2.606862,-3.889522,5.718211,1.181720,9.317922,8.551593,-1.241890,-5.079290,5.110242,-4.094702,2.506531,-8.653099,-3.348173,8.205630,-1.140966,3.617101,9.774651,-7.379346,5.229326,-4.740371,-9.874069,5.029100,0.537811,6.205117,-3.573292,8.898575,-3.023233,-2.131302,9.999792,3.254318,2.234318,-9.715623,6.487106,9.116723,-1.321336,7.806571,4.822871,9.107935,-2.388651,3.390038,0.411870,9.805347,-4.073668,-9.189345,8.041367,4.269247,-6.401547,-8.031868,-1.372225,-2.049874,7.719672,-4.686014,3.740022,9.331384,-4.585343,-6.448744,4.325229,2.255819,9.466951,7.329444,-7.731535,9.802641,-9.655108,-5.951821,4.957132,-2.264135,-7.967022,7.155779,-9.522555,-6.734580,7.656923,-8.368924,-1.265171,-0.618158,6.720475,-8.811893,-2.800937,9.216618,6.484330,-1.971818,-2.597068,5.424515,3.999327,-4.992734,5.676093,-7.872410,-2.250426,-2.367741,6.850097,-4.389181,-7.848522,-0.542714,7.729746,-6.640524,0.771643,9.476361,2.765793,-8.597160,-6.633255,-4.985076,3.654137,-8.005713,-6.072441,-7.925634,-9.725268,-0.592226,-0.905401,7.038196,-1.103342,-5.815678,-0.667182,-3.209947,8.825808,-5.396535,4.303181,8.177099,-6.799712,-9.777415,-3.635189,-7.158084,-9.017791,-4.025511,8.970064,-4.880338,2.782689,9.963843,-3.874595,9.473014,-0.671100,6.915944,-3.196831,3.155053,9.996824,7.151120,-8.442171,-3.703580,6.530261,4.007636,-7.349925,-6.866462,2.727702,-2.838798,8.105822,9.095470,6.203885,-7.458793,4.383016,-5.707472,1.007871,2.917290,8.416777,-5.831822,-2.667430,1.978221,0.607072,-8.011674,9.871566,3.957970,-8.688794,8.247987,2.377958,3.630120,5.507852,7.340150,-5.020940,-7.224015,-7.305107,-6.726241,5.615667,-1.036456,1.144269,1.592294,6.290709,-5.262910,7.861351,3.999998,5.604261,2.405471,3.586048,0.897858,9.270636,2.187256,9.822767,-2.869176,-2.556745,0.541998,6.372718,-4.328355,0.102658,-4.119431,-3.060638,-5.047496,7.319762,-8.748487,-8.594754,-3.581685,-8.886126,-2.966848,3.628759,-3.384343,0.382653,8.536296,-5.107712,1.637040,-4.156384,-3.387208,4.904722,-4.222178,-6.233167,4.827194,1.900366,0.235315,-0.016817,3.222223,-4.300686,7.984674,2.092430,7.211387,-5.281323,-8.100670,-1.850750,-8.207097,6.732359,-7.904090,1.305254,-1.588686,7.821524,-0.328753,1.575953,1.981392,5.916831,3.648613,-7.720738,-6.335892,8.402521,7.194408,9.109976,-9.670114,0.689341,1.835560,-4.463525,8.173222,3.181748,6.484082,2.147071,-0.627604,9.166932,3.895124,-6.247250,2.372733,-5.669730,-2.628710,-0.772136,-2.046501,6.681136,-2.336994,-4.250820,-1.153703,-9.992115,-8.332808,-5.932611,-5.356479,3.203500,1.057588,-3.559122,6.229167,-4.146538,-4.961950,-5.453709,-3.895162,-3.347311,-4.281766,-1.541538,-9.024660,-7.562785,-1.385739,-6.670725,5.253999,-2.077334,1.816643,0.347551,-5.814642,-8.621685,-6.943566,4.283675,3.046474,7.583780,-8.655290,-4.794277,-9.071456,-8.856204,8.043361,-6.961018,-3.236801,-8.314219,8.738219,-5.293884,1.214700,-8.281530,-6.703812,-5.155428,-0.495283,0.820051,0.942397,5.655660,-0.156918,-0.148934,-4.749876,-9.330333,9.656390,5.811795,-6.873048,-3.554359,-9.837532,8.075022,7.685370,-9.372690,-8.657891,-3.093693,7.859712,6.693771,9.522566,-9.871059,-2.938268,-5.705470,4.739770,-0.147625,-7.029341,8.171259,-5.815210,9.296192,-9.051835,7.394882,8.774236,-3.254551,5.900264,-9.480570,0.557694,1.167762,-8.096098,8.190439,3.487406,7.704400,6.469079,-3.825927,-1.955928,4.248328,-7.135805,1.079399,-8.172077,-2.909033,5.338945,0.083409,3.910794,4.903211,-9.907116,1.481038,-7.556962,1.165367,3.741842,8.195157,8.932045,-9.320806,8.333897,8.988291,3.014796,-3.908787,4.164542,7.351767,-5.805078,-8.398017,-5.714103,-0.703610,-4.122743,-1.269518,9.680763,8.761713,-4.919381,-8.006780,7.638396,3.428829,-9.350353,-5.897183,8.451119,-8.570895,-4.429324,4.903943,4.442135,7.076466,3.899513,9.137901,-8.742163,-9.105521,6.267632,-2.909240,-8.823561,9.020378,4.810857,-0.902219,-5.825370,-9.003460,3.673897,2.129869,3.230133,4.674363,-4.787817,-7.234047,2.149401,8.859586,9.464698,-5.073690,1.577475,-7.339055,1.581952,-0.901620,-0.714077,-4.962361,-7.238906,-8.437356,-4.770695,-3.564414,-4.822185,4.754121,1.915700,-5.367832,2.882247,5.643062,8.152361,8.476433,-3.518688,-4.704058,8.110995,3.685279,-7.299619,1.403585,0.540276,3.128711,-6.545509,1.230254,7.162312,5.423240,-4.823554,2.046366,-7.395809,-9.923575,-6.716259,8.711874,3.762356,4.566624,-0.056963,6.179262,7.845002,-5.232861,2.009324,2.938916,6.119826,6.662648,9.273594,3.022736,-2.276291,3.749681,-3.118668,-8.147011,0.828973,7.882172,-3.858098,9.841267,3.905302,-6.453288,1.639993,5.065363,-9.624211,3.281881,-7.206495,1.931655,-4.630581,5.756711,-1.787007,2.982821,-4.469177,9.000416,5.431914,-6.868795,-5.117530,3.938913,-6.830340,6.507839,-2.907784,2.851932,5.835218,6.157454,0.122904,8.261106,-9.569922,4.389516,6.938760,1.509938,3.671596,-8.691132,-4.706803,5.163851,-7.986767,7.328579,3.633893,5.551474,-5.653531,6.433274,-6.955361,2.900380,3.835216,5.082453,8.593114,2.699989,-1.437037,3.098494,0.548396,6.944310,8.109939,-1.269029,6.673011,5.327237,-6.698236,4.720106,5.304966,3.772419,9.188938,-8.899529,-3.677623,5.463627,1.351217,4.358613,-4.714203,-8.532421,-5.592351,-2.002594,7.859759,0.619351,-8.460977,-2.122903,2.469213,-5.600168,-4.381711,9.378060,-4.299256,9.071439,5.333051,8.349521,0.038698,6.515702,-8.139640,-7.771132,-8.202774,-3.162330,-0.346075,-4.301090,-4.538668,1.476546,8.359565,1.278495,3.530349,5.693771,-3.008634,-8.524493,0.337402,6.502346,-3.694112,4.683105,1.327368,3.568574,-2.919215,8.800800,3.292105,5.014725,1.689146,-1.665705,4.708101,-6.091042,-2.477866,5.555951,-1.030165,-2.452848,-4.351103,7.330103,2.953802,-8.106580,2.967937,-2.850511,-2.569601,0.909929,2.194291,-7.027077,-5.542603,-2.058251,-2.707114,-0.498303,-5.001125,8.784560,-5.521849,-9.746041,5.423241,9.370352,-0.575465,3.684391,8.185686,-4.279738,2.338587,9.084589,4.512862,-9.597180,6.552637,3.928008,9.006792,3.487872,8.486790,1.786595,-7.671945,4.178542,1.016899,1.267838,-9.741083,3.854571,-8.505688,6.308170,-8.853108,1.835727,-2.069852,3.115886,2.484653,3.025888,-3.918061,-2.705114,4.455578,0.929359,-9.366987,7.830586,-4.940112,-9.176625,4.714552,7.189155,-8.997453,5.196042,6.972092,-3.361793,6.605923,6.219825,8.585094,-6.969092,-9.534128,3.445556,-4.093165,5.101230,5.702685,-9.914157,5.837685,-1.816893,-3.020592,-6.147710,-5.360415,1.325553,-8.181791,9.467799,-4.750061,-9.340656,8.164471,2.016932,-5.605511,-4.129493,0.256970,-7.879992,-5.200303,-4.159056,-3.588638,-6.362027,3.323762,0.831088,7.173928,7.708629,-5.976905,-3.071707,5.818848,-6.033625,-7.409422,3.972105,4.126092,-8.477746,-0.421557,-6.394032,4.746541,3.215096,-3.057746,-7.600009,6.152890,9.137157,1.427560,0.616920,-3.384459,-3.772066,8.271389,-7.850783,0.455067,-8.995363,6.955102,-5.571638,-1.583942,7.062466,-0.343917,-3.395284,-4.231890,-4.220879,5.907262,-6.456143,7.092659,-7.173598,5.959876,9.271932,0.663964,-3.475610,-7.935127,8.645242,7.047136,-7.422889,-7.934239,8.761585,-5.132058,-6.480802,-3.795532,5.298654,5.131491,-5.701161,-5.850818,4.660535,7.575716,-9.135939,-3.388681,-8.431800,5.814433,-3.952761,1.560843,-8.853914,2.198130,1.047356,5.236667,1.623113,-3.393552,3.872212,3.904876,-4.484870,7.937121,-2.919758,-7.745026,9.279739,6.771255,0.369055,8.939158,6.284173,-7.596430,-5.475635,5.169321,-5.278029,3.491410,3.510316,-7.136030,-5.276957,-7.021677,-3.587225,9.678160,-3.445080,1.150648,-8.688752,9.943211,7.109007,-5.386254,-5.929746,7.299056,-6.741765,-4.538112,1.094343,4.878428,-3.225342,-8.385240,3.716001,-4.615183,0.756145,3.787120,1.866944,6.528071,3.585991,-8.773719,3.199528,-0.659241,2.633257,7.750961,-1.453662,-9.391176,4.964619,3.567114,-8.845958,-1.554862,1.784787,7.245862,2.039493,5.848756,9.553002,-1.675179,2.161768,-0.908003,2.835466,3.846963,-9.594410,0.258263,-2.657446,-4.361646,-9.977053,-7.933428,7.316471,-6.777500,-6.059568,1.449010,-1.467176,9.975115,-4.164800,-7.872845,6.528884,1.044709,4.688997,8.895638,7.303652,-8.272451,4.533790,1.460344,6.505781,1.845351,7.731634,8.082810,-4.370563,5.283621,-8.260535,-1.433275,4.158788,6.682699,-1.054113,3.685905,3.919486,-4.772414,-2.397132,1.340271,9.433945,-3.732631,1.555071,-5.609151,-5.477930,-4.881820,9.249623,-0.362241,1.308473,1.701404,5.168673,2.852774,4.620777,7.837753,-7.467912,0.391103,1.436335,-4.488869,3.098855,-5.669005,0.927229,-2.454147,4.256259,1.667399,-0.770131,5.134642,7.656180,-1.496004,-8.213803,5.489028,-4.955960,-3.970459,-6.780643,-8.990161,-9.030978,2.729591,-5.529751,-5.491058,-3.946977,-6.625594,5.080989,-9.839255,-0.671597,2.619724,-8.527810,4.883841,8.234278,-0.604303,1.834401,8.621301,4.349260,2.675478,-8.036858,-0.810052,8.206926,8.656675,-6.273053,-5.658399,2.905989,0.435136,-9.742691,-6.588551,-9.527448,3.157808,-3.603007,0.500004,6.778576,6.557819,9.751700,-9.239799,-7.907150,3.124285,-6.961396,5.026358,4.731541,0.458932,-9.467250,1.583760,2.247443,-7.180162,6.549403,0.256768,-6.362573,-7.791492,-4.402261,-7.993371,-2.420510,9.420965,9.732331,-1.562864,2.750165,-8.291678,-8.481215,6.085032,-3.834078,7.222502,8.356740,-5.930199,7.031952,7.293661,-0.074175,-9.505265,7.962045,7.296421,-7.216535,4.239721,3.628125,9.028921,8.680312,6.694967,-1.721013,2.487425,-7.079490,5.702677,-7.953944,4.445587,3.935427,-3.950374,-9.876591,0.469108,5.394744,-1.625257,7.299755,-8.808849,-2.915502,-2.300456,-0.088167,5.598856,-3.649621,-6.205961,6.638742,9.777660,8.406994,-1.200186,5.213181,4.010841,-8.317056,6.114141,3.312211,8.683456,-4.093175,0.986708,6.972784,1.236907,7.303505,0.062776,0.612432,4.181353,-2.174317,-5.483262,-3.639600,-1.352841,-5.388170,-0.280968,-9.960111,0.434021,7.403686,5.052993,6.459176,-1.563787,8.271423,-5.863415,-2.431781,4.053068,9.425104,-0.312210,2.255005,-8.855762,8.040302,-4.085289,-9.167933,-0.107563,-4.747689,0.847589,-9.369493,-6.243124,5.781725,-8.342215,9.874690,-0.802101,-5.602046,-9.964689,4.522830,3.936979,5.181933,-6.345921,7.171296,5.852000,5.068284,-4.149109,9.852710,4.987789,1.798754,-4.903347,7.509810,2.232849,-6.945669,-0.031811,-7.699615,-7.120195,2.254786,-7.578376,0.059586,-7.127360,-5.649885,-4.024644,9.682203,-0.170071,2.539657,4.535073,4.861201], dtype = "float32")#candidate|16312|(1287,)|const|float32
var_16313 = relay.var("var_16313", dtype = "float64", shape = (84,))#candidate|16313|(84,)|var|float64
call_16311 = relay.TupleGetItem(func_14438_call(relay.reshape(const_16312.astype('float32'), [1287,]), relay.reshape(var_16313.astype('float64'), [84,]), ), 2)
call_16314 = relay.TupleGetItem(func_14442_call(relay.reshape(const_16312.astype('float32'), [1287,]), relay.reshape(var_16313.astype('float64'), [84,]), ), 2)
output = relay.Tuple([call_16256,call_16270,call_16277,call_16284,const_16285,const_16286,call_16294,call_16301,var_16302,const_16303,var_16304,var_16305,const_16306,const_16307,call_16311,const_16312,var_16313,])
output2 = relay.Tuple([call_16257,call_16271,call_16278,call_16287,const_16285,const_16286,call_16295,call_16308,var_16302,const_16303,var_16304,var_16305,const_16306,const_16307,call_16314,const_16312,var_16313,])
func_16333 = relay.Function([var_16302,var_16304,var_16305,var_16313,], output)
mod['func_16333'] = func_16333
mod = relay.transform.InferType()(mod)
var_16334 = relay.var("var_16334", dtype = "float64", shape = (364,))#candidate|16334|(364,)|var|float64
var_16335 = relay.var("var_16335", dtype = "uint64", shape = ())#candidate|16335|()|var|uint64
var_16336 = relay.var("var_16336", dtype = "uint64", shape = (288,))#candidate|16336|(288,)|var|uint64
var_16337 = relay.var("var_16337", dtype = "float64", shape = (84,))#candidate|16337|(84,)|var|float64
output = func_16333(var_16334,var_16335,var_16336,var_16337,)
func_16338 = relay.Function([var_16334,var_16335,var_16336,var_16337,], output)
mutated_mod['func_16338'] = func_16338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15146_call = mod.get_global_var('func_15146')
func_15148_call = mutated_mod.get_global_var('func_15148')
call_16346 = func_15146_call()
call_16347 = func_15146_call()
func_14611_call = mod.get_global_var('func_14611')
func_14613_call = mutated_mod.get_global_var('func_14613')
call_16362 = relay.TupleGetItem(func_14611_call(), 0)
call_16363 = relay.TupleGetItem(func_14613_call(), 0)
func_2219_call = mod.get_global_var('func_2219')
func_2222_call = mutated_mod.get_global_var('func_2222')
const_16368 = relay.const([10,3,3,-5,7,4,4,6,-6,1,2,-10,10,-8,2,10,-7,-7,1,5,-2,7,-10,-9,-3,6,6,-8,1,-1,-9,-4,-4,-7,3,-4,-2,10,6,-10,10,6,5,6,-10,-6,10,5,1,10,5,-8,4,1,-9,-9,-9,7,-9,-10,10,9,-8,-3,-6,4,4,8,-1,-8,-2,-9,1,6,9,-10,2,8,-6,10,1,-5,7,4,4,10,10,6,-7,3,8,4,7,-1,-2,-4,4,-9,3,-3,-7,1,-6,1,3,9,1,1,-7,8,-3,4,2,-10,-9,9,10,5,1,9,-10,-5,-6,-9,-9,2,-9,-9,2,-7,-6,8,8,-2,-7,-5,3,-10,-8,-2,5,-9,4,7,-1,6,-1,-3,-6,-2,-8,-2,8,-10,10,-3,9,1,-2,-7,5,10,8,8,10,6,8,-9,-1,-3,2,-10,-10,4,1,4,-5,-3,10,6,3,8,-2,-8,-7,-6,6,9,6,7,5,5,-6,2,2,-5,-9,-6,9,6,2,-4,7,-4,7,2,3,-3,-8,6,-4,-8,-6,-4,8,-3,-3,1,-2,-2,-6,-2,-4,7,-9,-3,-6,6,5,8,-1,4,-8,3,-7,9,-9,-2,4,-4,-2,6,8,-9,3,6,8,7,2,4,-2,5,-3,-4,-4,-10,5,-6,7,8,5,-3,4,7,-7,-7,5,10,-9,-5,-5,1,10,-7,-5,8,-10,10,-8,-2,-1,5,3,4,-2,-4,1,-8,-3,9,-9,7,-5,-3,-6,-9,6,-3,-9,-10,3,9,9,6,-10,1,1,9,7,-10,-7,-1,4,1,-2,-6,4,10,3,-7,-2,-4,-6,-10,5,7,-10,-4,-4,-10,7,-3,3,6,1,1,-10,8,-6,-1,8,-2,10,-5,-4,-3,2,3,9,-9,1,-6,5,-8,-2,-1,-1,-1,10,3,2,6,-2,-7,-6,-3,-8,-9,3,-1,8,-5,6,8,-1,-1,-9,-7,4,3,-2,-1,5,1,-9,1,6,-6,2,-10,9,8,-6,2,-10,-4,-1,-1,4,4,-8,-1,-3,-9,-5,1,-10,-3,-5,10,7,-8,-8,-7,-4,-6,-8,-7,5,9,6,-3,9,7,-8,1,-1,-6,-1,3,-5,-8,-7,-5,2,4,4,-6,-1,8,10,-7,-2,3,-9,9,-7,-7,1,-1,-8,2,-10,4,1,-3,5,3,-4,-9,3,6,-4,-8,-7,-7,-2,6,9,-3,5,-1,-7,-6,-3,5,2,7,4,-10,-4,7,-7,-8,-4,7,9,8,4,-9,10,2,3,9,-7,-10,7,7,-10,-8,-7,4,5,-4,-7,-6,6,10,-1,9,-7,9,6,-7,10,-3,-2,-3,-8,-8,9,-5,-3,-4,-5,2,-4,7,4,8,-1,1,5,-2,2,-1,3,-5,10,-1,-6,8,-4,2,9,4,-1,3,10,1,5,-2,-10,5,10,-7,-10,6,2,-6,8,-10,4,4,-1,5,-9,-2,-3,10,-4,-10,4,10,4,4,5,-8,1,4,-9,6,3,-8,7,-10,5,-5,5,-2,1,-10,3,-5,2,-4,8,10,10,-8,3,7,-9,6,8,-5,-5,-3,-5,-1,-10,9,-7,-9,-6,-7,6,-7,-6,1,3,3,2,-6,-6,5,4,-4,-4,1,10,9,9,1,10,-1,9,-1,-10,8,-4,2,9,-10,-8,1,6,-4,-5,-4,8,-8,-7,-7,-3,-3,-10,-4,10,1,6,6,3,9,-4,3,-6,10,-7,2,-4,7,-9,-4,-9,-7,-9,5,10,10,-6,-9,-1,8,7,-9,5,8,9,3,7,2,-2,5,-2,-9,7,5,-8,-7,-2,-8,4,-3,6,-2,-7,-8,-3,4,-10,-6,-10,7,3,-2,2,-4,-6,1,4,-6,10,-3,-10,6,7,-9,2,-4,1,10,8,2,-4,7,-8,10,-8,9,-9,10,-1,-4,6,-8,5,-4,5,-4,-1,-6,3,-9,8,-1,-6,-4,3,-10,7,9,7,3,-1,8,10,-3,9,-8,-1,-3,-1,4,6,-4,-1,2,-6,9,-6,9,10,-10,7,5,8,-7,-6,4,6,-2,1,-6,-1,-6,1,-4,9,-7,2,4,-1,-9,-3,-6,3,5,-3,2,-3,2,4,-4,-10,1,4,-1,6,1,-7,8,6,3,-2,5,5,-1,1,-4,-8,-4,10,-7,-7,8,3,3,9,1,3,9,1,-5,-7,5,3,6,-5,2,9,-8,-3,-6,-7,4,-10,5,4,6,-10,5,-8,-9,-5,-7,-8,-1,-5,5,-3,-1,-3,4,10,-9,1,-8,-6,-4,-7,-7,7,7,-6,-4,-3,-2,5,4,-8,-8,8,9,-10,-6,7,3,3,4,4,8,4,6,8,5,-2,4,-6,3,-10,-4,-4,9,-6,-7,-2,10,7,-7,5,-10,4,6,-8,9,-9,5,9,1,8,8,4,-7,-3,5,-6,-4,8,-4,2,-6,-4,6,-4,1,-6,-3,-8,-3,-5,-8,3,5,3,-10,1,-7,7,-10,-10,-5,9,-9,8,-7,-10,6,-6,-7,-10,-5,-4,-8,6,2,-9,4,-4,-5,5,-5,-7,-10,-4,2,-5,5,-1,-10,10,-3,-10,-9,10,-7,7,1,5,-7,-8,2,-9,-5,-1,5,9,-10,-9,-5,4,5,8,-5,5,3,-2,1,4,-10,-2,-8,-7,2,-9,4,-3,-3,4,3,2,7,2,5,-3,-3,-4,-6,9,-6,6,-2,-10,9,2,3,7,8,-7,7,10,5,-9,4,8,6,1,-3,2,-4,4,-10,9,-2,1,-8,-7,6,1,-4,1,5,10,2,9,-6,-7,-6,4,-5,-7,-7,-4,-2,2,-6,-8,6,10,-9,6,-4,4,9,9,-3,5,-3,-5,-5,-3,-2,3,-10,-6,2,6,6,7,8,-9,2,-2,-4,2,-4,10,9,-3,-6,9,4,-3,5,-6,-4,3,1,-5,-2,4,-5,3,-10,4,-7,4,-8,4,7,-8,6,-8,-7,-4,1,5,4,9,-6,10,6,7,-10,-9,10,7,9,3,-2,6,-6,-9,-1,-6,3,-2,-1,3,9,-10,9,7,5,-5,6,10,4,-4,-2,-4,8,2,-5,3,-8,7,10,-7,-3,-4,6,2,-7,-7,-9,-2,4,-8,-10,5,4,5,-5,3,-7,-6,2,2,-6,-8,9,2,3,-4,-1,-1,2,-2,-8,-4,1,7,8,5,-10,9,-1,5,-2,-9,10,1,5,7,-8,8,1,-5,9,-4,-10,-10,-5,9,4,2,7,3,7,-5,3,4,-1,6,6,-10,-5,1,5,-9,7,10,5,6,-7,4,-6,-5,-7,8,-1,4,-9,7,-5,3,-8,-8,8,6,6,-5,-10,1,1,3,-10,-9,-1,2,-3,-10,6,5,-1,-9,-2,-9,-7,10,-2,2,-9,10,7,6,5,-2,-3,6,9,10,2,-4,2,6,6,-5,-1,4,6,-8,5,3,9,3,7,-1,-5,-7,-10,2,-3,2,-3,-1,-8,10,-1,3,-2,-9,-10,-7,7,1,-1,7,9,7,6,10,9,7,-5,-1,7,-8,-2,1,3,9,4,-5,5,-6,3,5,8,-1,4,-3,-2,9,8,-3,3,-2,-8,-1,-2,-4,-3,-7,4,-5,10,1,-1,-5,-4,9,-2,4,1,-5,-10,-9,9,-3,4,1,-8], dtype = "int16")#candidate|16368|(1404,)|const|int16
call_16367 = func_2219_call(relay.reshape(const_16368.astype('int16'), [12, 13, 9]))
call_16369 = func_2219_call(relay.reshape(const_16368.astype('int16'), [12, 13, 9]))
func_15329_call = mod.get_global_var('func_15329')
func_15334_call = mutated_mod.get_global_var('func_15334')
const_16379 = relay.const(6, dtype = "uint64")#candidate|16379|()|const|uint64
const_16380 = relay.const([-7,5,-6,-10,9,9,-7,2,-3,-9,6,-2,-1,-4,-3,4,-5,9,-1,-2,-8,4,7,3,5,-10,1,3,-9,1,-1,-1,6,-8,9,-7,4,-4,-9,1,-6,4,-3,1,5,-3,7,-3,-5,9,-4,3,-10,-8,-4,1,-10,-9,-6,-6,-2,-7,6,-9,-2,7,7,-3,8,3,10,2,-3,-4,1,7,-10,2,4,-9,2,-4,7,-5,7,-7,-4,-9,-9,-3,3,-6,6,-1,1,-9,-5,1,10,-8,-4,6,-3,-4,-7,5,-8,-3,8,7,3,2,10,-1,-1,-9,-4,-4,9,-1,4,-6,-8,-9,4,-8,3,-4,-5,-5,-4,3,1,-4,5,9,-3,6,-6,8,2,-9,-5,-1,-10,1,3,1,-1,-4,-10,10,10,3,-10,7,8,-8,-3,-7,5,6,-2,-2,1,1,-1,-7,6,6,-2,7,-1,4,6,-6,7,-1,-10,-2,-10,-6,-6,3,-2,8,-4,-3,2,10,9,2,-9,-7,-7,1,3,-10,8,-1,-2,4,3,-2,7,4,-9,1,9,-8,8,4,7,-2,-5,5,9,-5,9,9,1,-1,10,-10,-10,5,-8,-1,3,1,-4,7,-8,-8,-10,-2,-10,3,4,1,2,4,-7,6,-8,-7,-5,-8,7,-9,-4,-9,-5,6,-8,3,-5,1,-4,9,3,-6,2,-1,-1,7,-5,-10,1,-8,-3,10,-2,7,9,9,5,2,9,-6,6,-6,10,-1,-9,9,-4,9], dtype = "uint64")#candidate|16380|(288,)|const|uint64
const_16381 = relay.const([3,5,-9,5,-8,5,-5,-5,-3,-6,-5,5,-9,2,-6,-6,-10,9,1,-3,10,-3,10,-7,-5,9,-10,-4,5,6,9,-10,-5,10,-5,-5,10,4,-7,5,6,2,10,4,5,9,-4,-5,-8,-6,-8,7,-8,10,-2,7,-10,-3,-8,8,-6,9,5,-10,-1,-5,-7,6,1,-3,10,-10,-3,-1,-9,6,9,9,1,7,8,-8,-4,2,-8,-10,-5,9,5,-8,-2,-4,-2,-4,-4,3,-3,-7,-5,2,-4,-4,-5,6,4,6,10,6,3,-5,1,9,10,10,-6,1,-7,8,1,-3,10,2,9,4,-9,1,6,5,7,-1,10,-3,-10,-10,-5,-5,-10,6,6,3,8,5,-3,10,-6,3,3,-2,4,-4,-4,-5,6,6,-5,7,-3,7,-1,-4,-8,-2,2,5,-7,-7,8,5,-7,-7,-10,-6,-7,6,2,4,10,2,-1,8,-6,6,8,9,2,8,2,-4,-8,6,4,-9,-7,6,6,3,8,-7,3,-4,3,1,-5,-6,-7,3,4,8,1,-7,-8,10,-4,-2,2,-3,7,4,-9,7,3,-1,-1,8,3,-10,8,6,-6,8,-6,5,-5,7,9,1,-3,-1,-1,6,-4,2,-6,-1,-9,-2,-10,-8,8,-10,-9,-1,3,-7,-2,-8,-3,6,3,4,8,4,-3,-2,8,-9,3,9,3,2,-3,2,5,5,-7,9,-5,3,5,-10,-9,2,-9,10,9,9,-6,-7,-9,8,-1,3,-10,-5,-4,-2,2,-5,-4,-6,8,-6,6,-5,8,-3,10,5,4,7,-5,-1,2,9,-2,1,-10,-2,2,5,1,-9,6,3,5,8,-8,4,-6,7,10,5,7,-8,7,7,1,-8,-9,7,-10,2,5,-1,-3,-6,-8,-2,-10,-4,-4,-4,-8,-6,-5,10,9,7,-2,-2], dtype = "int64")#candidate|16381|(360,)|const|int64
call_16378 = relay.TupleGetItem(func_15329_call(relay.reshape(const_16379.astype('uint64'), []), relay.reshape(const_16380.astype('uint64'), [2, 144]), relay.reshape(const_16381.astype('int64'), [360,]), ), 1)
call_16382 = relay.TupleGetItem(func_15334_call(relay.reshape(const_16379.astype('uint64'), []), relay.reshape(const_16380.astype('uint64'), [2, 144]), relay.reshape(const_16381.astype('int64'), [360,]), ), 1)
output = relay.Tuple([call_16346,call_16362,call_16367,const_16368,call_16378,const_16379,const_16380,const_16381,])
output2 = relay.Tuple([call_16347,call_16363,call_16369,const_16368,call_16382,const_16379,const_16380,const_16381,])
func_16385 = relay.Function([], output)
mod['func_16385'] = func_16385
mod = relay.transform.InferType()(mod)
output = func_16385()
func_16386 = relay.Function([], output)
mutated_mod['func_16386'] = func_16386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15898_call = mod.get_global_var('func_15898')
func_15899_call = mutated_mod.get_global_var('func_15899')
call_16445 = func_15898_call()
call_16446 = func_15898_call()
output = call_16445
output2 = call_16446
func_16461 = relay.Function([], output)
mod['func_16461'] = func_16461
mod = relay.transform.InferType()(mod)
output = func_16461()
func_16462 = relay.Function([], output)
mutated_mod['func_16462'] = func_16462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_16505 = relay.TupleGetItem(func_15484_call(), 1)
call_16506 = relay.TupleGetItem(func_15485_call(), 1)
func_15622_call = mod.get_global_var('func_15622')
func_15623_call = mutated_mod.get_global_var('func_15623')
call_16523 = func_15622_call()
call_16524 = func_15622_call()
func_7136_call = mod.get_global_var('func_7136')
func_7138_call = mutated_mod.get_global_var('func_7138')
const_16546 = relay.const([4.480425,-5.570876,-8.535232,-6.696097,6.338781,1.263436,9.698597,-4.661929,-4.339040,-5.612082,-3.617368,-3.253048,4.985858,5.788575,-1.380332,-7.374420,-8.863504,-8.429658,1.521353,2.946311], dtype = "float32")#candidate|16546|(20,)|const|float32
call_16545 = func_7136_call(relay.reshape(const_16546.astype('float32'), [4, 1, 5]))
call_16547 = func_7136_call(relay.reshape(const_16546.astype('float32'), [4, 1, 5]))
output = relay.Tuple([call_16505,call_16523,call_16545,const_16546,])
output2 = relay.Tuple([call_16506,call_16524,call_16547,const_16546,])
func_16550 = relay.Function([], output)
mod['func_16550'] = func_16550
mod = relay.transform.InferType()(mod)
output = func_16550()
func_16551 = relay.Function([], output)
mutated_mod['func_16551'] = func_16551
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16592 = relay.var("var_16592", dtype = "float32", shape = ())#candidate|16592|()|var|float32
var_16593 = relay.var("var_16593", dtype = "float32", shape = (10, 1, 1))#candidate|16593|(10, 1, 1)|var|float32
bop_16594 = relay.power(var_16592.astype('float32'), var_16593.astype('float32')) # shape=(10, 1, 1)
bop_16598 = relay.bitwise_and(var_16592.astype('int32'), bop_16594.astype('int32')) # shape=(10, 1, 1)
bop_16609 = relay.divide(bop_16594.astype('float64'), relay.reshape(bop_16598.astype('float64'), relay.shape_of(bop_16594))) # shape=(10, 1, 1)
output = bop_16609
output2 = bop_16609
func_16639 = relay.Function([var_16592,var_16593,], output)
mod['func_16639'] = func_16639
mod = relay.transform.InferType()(mod)
var_16640 = relay.var("var_16640", dtype = "float32", shape = ())#candidate|16640|()|var|float32
var_16641 = relay.var("var_16641", dtype = "float32", shape = (10, 1, 1))#candidate|16641|(10, 1, 1)|var|float32
output = func_16639(var_16640,var_16641,)
func_16642 = relay.Function([var_16640,var_16641,], output)
mutated_mod['func_16642'] = func_16642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16550_call = mod.get_global_var('func_16550')
func_16551_call = mutated_mod.get_global_var('func_16551')
call_16686 = relay.TupleGetItem(func_16550_call(), 2)
call_16687 = relay.TupleGetItem(func_16551_call(), 2)
output = relay.Tuple([call_16686,])
output2 = relay.Tuple([call_16687,])
func_16688 = relay.Function([], output)
mod['func_16688'] = func_16688
mod = relay.transform.InferType()(mod)
output = func_16688()
func_16689 = relay.Function([], output)
mutated_mod['func_16689'] = func_16689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16064_call = mod.get_global_var('func_16064')
func_16066_call = mutated_mod.get_global_var('func_16066')
call_16690 = func_16064_call()
call_16691 = func_16064_call()
output = relay.Tuple([call_16690,])
output2 = relay.Tuple([call_16691,])
func_16719 = relay.Function([], output)
mod['func_16719'] = func_16719
mod = relay.transform.InferType()(mod)
output = func_16719()
func_16720 = relay.Function([], output)
mutated_mod['func_16720'] = func_16720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16461_call = mod.get_global_var('func_16461')
func_16462_call = mutated_mod.get_global_var('func_16462')
call_16727 = func_16461_call()
call_16728 = func_16461_call()
func_14157_call = mod.get_global_var('func_14157')
func_14158_call = mutated_mod.get_global_var('func_14158')
call_16748 = relay.TupleGetItem(func_14157_call(), 1)
call_16749 = relay.TupleGetItem(func_14158_call(), 1)
func_12124_call = mod.get_global_var('func_12124')
func_12129_call = mutated_mod.get_global_var('func_12129')
const_16751 = relay.const([[-7.786512,-7.925077],[-4.370090,6.344093],[-8.595180,-3.979496],[-0.017248,-4.485727],[9.972262,1.373871],[7.015162,5.423809],[5.871323,2.874884],[-7.545396,6.989449],[-3.998714,0.746577],[-7.212446,7.716595],[5.287561,-1.600717],[-2.534203,-0.072419],[-9.207663,-9.625198],[-3.249512,8.317289],[-4.038471,7.176321],[5.025221,7.162066],[-9.739590,-8.651271],[3.195987,6.687850],[-9.289937,-9.169415],[-7.488538,-9.586230],[-2.084869,4.942233],[2.530677,-3.017222],[9.263038,-8.626752],[7.785141,-7.461663],[-7.211107,-4.906744],[-7.533855,-4.542094],[1.863065,-5.842172],[3.784113,-9.208590],[3.884939,2.936287],[2.396432,-2.351119],[6.953910,9.300475],[-4.437874,9.798166],[3.294072,-4.614210],[7.541184,-3.351907],[-0.355054,1.881205],[2.980542,0.552574],[4.703846,7.671928],[0.938685,4.330836],[1.077743,8.068425],[-2.563831,-0.044705],[-9.721489,-6.149470],[-8.409029,1.940324],[4.206946,-3.218527],[-7.482832,4.602272],[-2.179454,-0.256255],[-5.302028,0.558545],[8.018063,7.825184],[3.565853,2.346761],[-9.904738,8.390203],[-1.074697,4.605634],[6.220402,-4.153515],[-1.043370,7.807388],[8.970052,-5.829572],[6.188098,4.855397],[-9.011081,9.081493],[-1.063910,7.246082],[-2.923227,3.714319],[1.168740,-5.149660],[3.117775,2.594262],[-6.060620,-2.907901],[-7.257566,8.094816],[-2.127494,-4.172959],[8.596344,-8.723551],[-9.598240,-2.744534],[3.233902,7.482865],[9.763606,8.996859],[4.170435,-2.890075],[-4.882412,7.591882],[5.099736,-4.738118],[6.356048,-6.873795],[-3.364142,-0.908870],[-0.552339,4.167685],[0.379767,3.849249],[-7.478831,8.183126],[8.715488,5.041214],[-8.426692,-5.635891],[0.121139,-2.903654],[-2.475356,6.090574],[1.341259,3.017044],[7.205157,5.404046],[-5.408126,1.402871],[-5.610630,-9.577049],[-9.599783,2.930442],[-9.276057,-9.965998],[-1.967887,-4.399223],[3.443782,-4.011258],[8.167566,-9.054636],[-8.699852,7.796347],[-3.320321,-9.727947],[2.551639,-4.945258],[-6.149448,2.259696],[-9.152194,6.816616],[-5.596178,5.506479],[7.041210,-7.707683],[6.161786,7.080383],[9.610452,-5.393914],[7.099097,-1.522998],[2.871082,-8.679235],[-9.672845,-0.777207],[4.548441,3.165753],[7.058933,2.191048],[-0.966788,-5.543580],[9.788832,-6.161899],[-8.975680,-6.362515],[4.905567,2.318682]], dtype = "float32")#candidate|16751|(105, 2)|const|float32
var_16752 = relay.var("var_16752", dtype = "int16", shape = (1404,))#candidate|16752|(1404,)|var|int16
const_16753 = relay.const([-4.008320,-9.359543,4.659840,5.043968,7.887292,8.381708,9.965085,3.317238,7.480875,-3.950874,-4.784981,1.911264,4.494133,5.191014,8.461218,-3.172865,-6.644636,2.966289,-3.631461,0.966807,-8.521914,-8.989222,-2.060680,-9.887933,-2.711960,-3.046351,-4.838950,7.831836,-0.725295,-6.067229,7.605589,1.088115,6.728467,7.543877,9.704134,2.185899,9.540750,-1.650981,-8.017543,2.018268,4.917167,1.270477,-5.147411,1.869122,-5.255191,-6.879379,-0.397741,1.676209,-7.322245,-6.360535,2.314966,-6.315464,6.149487,9.466563,0.292755,-1.771716,-6.051032,-4.287657,-6.179370,4.030123,3.223796,-5.233376,-6.408755,8.170656,-1.094470,-8.186202,0.043935,3.356406,5.109154,-8.378200,6.309823,2.118321,8.834100,-1.850110,-1.081531,-4.127924,2.236040,1.674909,-4.396840,2.156963,-3.111122,-9.786499,-4.647840,2.972097,-5.657428,-7.520770,-7.358528,-3.088014,8.089433,-8.957956,-3.293706,1.157470,0.269396,5.517659,1.793437,5.359952,0.604101,8.214888,2.384454,3.024544,5.164273,0.736547,-9.928614,7.068184,3.069551,7.700633,-1.477418,5.531803,9.927232,2.709549,9.206780,3.702622,-5.015872,-1.171701,7.732883,-3.229131,5.998874,-5.708366,5.748897,5.016302,9.549746,-1.296312,2.698620,-2.276250,0.579149,5.900939,-7.946454,8.678866,-2.199808,-0.280061,2.370477,-5.010511,-0.354399,-9.620973,-3.509927,-6.036485,-2.950079,6.971710,3.926741,6.798466,7.087262,8.132421,3.852709,-5.092244,6.758346,6.153068,6.639768,2.127167,-0.689707,7.012883,-8.572935,5.561052,1.274247,-5.265404,-1.374603,3.378890,5.828558,0.860977,3.001728,-9.739228,-1.453323,6.382685,1.469589,2.063055,4.708065,-9.700084,8.299512,-2.364489,-2.966935,6.924759,-1.803086,-9.663330,4.162782,-3.865228,4.420582,1.141434,-2.268122,-3.230130,-3.092625,-6.997687,-5.099898,5.095888,-6.174774,-1.674521,-7.983128,1.173527,-7.540826,-1.527347,7.397519,-8.967310,2.731822,-1.113623,6.992432,7.114433,-1.983118,4.222213,-5.497854,-6.791588,-8.849373,5.168719,-6.084741,-2.228064,-8.526478,5.585197,9.226986,9.749514,4.084858,5.542968,-9.548048,-5.547816,-3.618603,7.999465,-1.530870,9.449001,3.975549,-4.556532,3.826600,-8.487786,7.123329,3.592640], dtype = "float32")#candidate|16753|(220,)|const|float32
var_16754 = relay.var("var_16754", dtype = "int64", shape = (546,))#candidate|16754|(546,)|var|int64
call_16750 = relay.TupleGetItem(func_12124_call(relay.reshape(const_16751.astype('float32'), [3, 7, 10]), relay.reshape(var_16752.astype('int16'), [9, 156]), relay.reshape(const_16753.astype('float32'), [220,]), relay.reshape(var_16754.astype('int64'), [546,]), ), 7)
call_16755 = relay.TupleGetItem(func_12129_call(relay.reshape(const_16751.astype('float32'), [3, 7, 10]), relay.reshape(var_16752.astype('int16'), [9, 156]), relay.reshape(const_16753.astype('float32'), [220,]), relay.reshape(var_16754.astype('int64'), [546,]), ), 7)
bop_16757 = relay.bitwise_or(var_16752.astype('uint64'), call_16748.astype('uint64')) # shape=(4, 7, 1404)
bop_16760 = relay.bitwise_or(var_16752.astype('uint64'), call_16749.astype('uint64')) # shape=(4, 7, 1404)
var_16763 = relay.var("var_16763", dtype = "float32", shape = (105, 2))#candidate|16763|(105, 2)|var|float32
bop_16764 = relay.not_equal(const_16751.astype('bool'), relay.reshape(var_16763.astype('bool'), relay.shape_of(const_16751))) # shape=(105, 2)
var_16777 = relay.var("var_16777", dtype = "uint64", shape = (4, 7, 1404))#candidate|16777|(4, 7, 1404)|var|uint64
bop_16778 = relay.subtract(bop_16757.astype('int16'), relay.reshape(var_16777.astype('int16'), relay.shape_of(bop_16757))) # shape=(4, 7, 1404)
bop_16781 = relay.subtract(bop_16760.astype('int16'), relay.reshape(var_16777.astype('int16'), relay.shape_of(bop_16760))) # shape=(4, 7, 1404)
output = relay.Tuple([call_16727,call_16750,const_16753,var_16754,bop_16764,bop_16778,])
output2 = relay.Tuple([call_16728,call_16755,const_16753,var_16754,bop_16764,bop_16781,])
func_16789 = relay.Function([var_16752,var_16754,var_16763,var_16777,], output)
mod['func_16789'] = func_16789
mod = relay.transform.InferType()(mod)
mutated_mod['func_16789'] = func_16789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16789_call = mutated_mod.get_global_var('func_16789')
var_16791 = relay.var("var_16791", dtype = "int16", shape = (1404,))#candidate|16791|(1404,)|var|int16
var_16792 = relay.var("var_16792", dtype = "int64", shape = (546,))#candidate|16792|(546,)|var|int64
var_16793 = relay.var("var_16793", dtype = "float32", shape = (105, 2))#candidate|16793|(105, 2)|var|float32
var_16794 = relay.var("var_16794", dtype = "uint64", shape = (4, 7, 1404))#candidate|16794|(4, 7, 1404)|var|uint64
call_16790 = func_16789_call(var_16791,var_16792,var_16793,var_16794,)
output = call_16790
func_16795 = relay.Function([var_16791,var_16792,var_16793,var_16794,], output)
mutated_mod['func_16795'] = func_16795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_16808 = relay.TupleGetItem(func_15484_call(), 1)
call_16809 = relay.TupleGetItem(func_15485_call(), 1)
output = relay.Tuple([call_16808,])
output2 = relay.Tuple([call_16809,])
func_16817 = relay.Function([], output)
mod['func_16817'] = func_16817
mod = relay.transform.InferType()(mod)
output = func_16817()
func_16818 = relay.Function([], output)
mutated_mod['func_16818'] = func_16818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16385_call = mod.get_global_var('func_16385')
func_16386_call = mutated_mod.get_global_var('func_16386')
call_16838 = relay.TupleGetItem(func_16385_call(), 1)
call_16839 = relay.TupleGetItem(func_16386_call(), 1)
output = call_16838
output2 = call_16839
func_16840 = relay.Function([], output)
mod['func_16840'] = func_16840
mod = relay.transform.InferType()(mod)
mutated_mod['func_16840'] = func_16840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16840_call = mutated_mod.get_global_var('func_16840')
call_16841 = func_16840_call()
output = call_16841
func_16842 = relay.Function([], output)
mutated_mod['func_16842'] = func_16842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14748_call = mod.get_global_var('func_14748')
func_14749_call = mutated_mod.get_global_var('func_14749')
call_16859 = func_14748_call()
call_16860 = func_14748_call()
output = relay.Tuple([call_16859,])
output2 = relay.Tuple([call_16860,])
func_16861 = relay.Function([], output)
mod['func_16861'] = func_16861
mod = relay.transform.InferType()(mod)
output = func_16861()
func_16862 = relay.Function([], output)
mutated_mod['func_16862'] = func_16862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15146_call = mod.get_global_var('func_15146')
func_15148_call = mutated_mod.get_global_var('func_15148')
call_16863 = func_15146_call()
call_16864 = func_15146_call()
output = relay.Tuple([call_16863,])
output2 = relay.Tuple([call_16864,])
func_16865 = relay.Function([], output)
mod['func_16865'] = func_16865
mod = relay.transform.InferType()(mod)
mutated_mod['func_16865'] = func_16865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16865_call = mutated_mod.get_global_var('func_16865')
call_16866 = func_16865_call()
output = call_16866
func_16867 = relay.Function([], output)
mutated_mod['func_16867'] = func_16867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14740_call = mod.get_global_var('func_14740')
func_14742_call = mutated_mod.get_global_var('func_14742')
call_16905 = func_14740_call()
call_16906 = func_14740_call()
output = relay.Tuple([call_16905,])
output2 = relay.Tuple([call_16906,])
func_16915 = relay.Function([], output)
mod['func_16915'] = func_16915
mod = relay.transform.InferType()(mod)
output = func_16915()
func_16916 = relay.Function([], output)
mutated_mod['func_16916'] = func_16916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15898_call = mod.get_global_var('func_15898')
func_15899_call = mutated_mod.get_global_var('func_15899')
call_16932 = func_15898_call()
call_16933 = func_15898_call()
output = call_16932
output2 = call_16933
func_16942 = relay.Function([], output)
mod['func_16942'] = func_16942
mod = relay.transform.InferType()(mod)
mutated_mod['func_16942'] = func_16942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16942_call = mutated_mod.get_global_var('func_16942')
call_16943 = func_16942_call()
output = call_16943
func_16944 = relay.Function([], output)
mutated_mod['func_16944'] = func_16944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14253_call = mod.get_global_var('func_14253')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_16947 = relay.TupleGetItem(func_14253_call(), 0)
call_16948 = relay.TupleGetItem(func_14254_call(), 0)
output = call_16947
output2 = call_16948
func_16958 = relay.Function([], output)
mod['func_16958'] = func_16958
mod = relay.transform.InferType()(mod)
output = func_16958()
func_16959 = relay.Function([], output)
mutated_mod['func_16959'] = func_16959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15898_call = mod.get_global_var('func_15898')
func_15899_call = mutated_mod.get_global_var('func_15899')
call_16960 = func_15898_call()
call_16961 = func_15898_call()
output = relay.Tuple([call_16960,])
output2 = relay.Tuple([call_16961,])
func_16974 = relay.Function([], output)
mod['func_16974'] = func_16974
mod = relay.transform.InferType()(mod)
output = func_16974()
func_16975 = relay.Function([], output)
mutated_mod['func_16975'] = func_16975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15146_call = mod.get_global_var('func_15146')
func_15148_call = mutated_mod.get_global_var('func_15148')
call_16983 = func_15146_call()
call_16984 = func_15146_call()
output = relay.Tuple([call_16983,])
output2 = relay.Tuple([call_16984,])
func_17005 = relay.Function([], output)
mod['func_17005'] = func_17005
mod = relay.transform.InferType()(mod)
output = func_17005()
func_17006 = relay.Function([], output)
mutated_mod['func_17006'] = func_17006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14740_call = mod.get_global_var('func_14740')
func_14742_call = mutated_mod.get_global_var('func_14742')
call_17020 = func_14740_call()
call_17021 = func_14740_call()
output = relay.Tuple([call_17020,])
output2 = relay.Tuple([call_17021,])
func_17024 = relay.Function([], output)
mod['func_17024'] = func_17024
mod = relay.transform.InferType()(mod)
output = func_17024()
func_17025 = relay.Function([], output)
mutated_mod['func_17025'] = func_17025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17024_call = mod.get_global_var('func_17024')
func_17025_call = mutated_mod.get_global_var('func_17025')
call_17036 = relay.TupleGetItem(func_17024_call(), 0)
call_17037 = relay.TupleGetItem(func_17025_call(), 0)
func_15508_call = mod.get_global_var('func_15508')
func_15510_call = mutated_mod.get_global_var('func_15510')
call_17039 = relay.TupleGetItem(func_15508_call(), 1)
call_17040 = relay.TupleGetItem(func_15510_call(), 1)
func_14438_call = mod.get_global_var('func_14438')
func_14442_call = mutated_mod.get_global_var('func_14442')
var_17061 = relay.var("var_17061", dtype = "float32", shape = (1287,))#candidate|17061|(1287,)|var|float32
const_17062 = relay.const([3.875712,6.618840,-9.039323,-3.240179,-9.867428,9.715981,2.046447,-7.870315,5.340842,-5.967056,-4.727536,-0.700913,-6.126065,5.654719,5.596029,-0.014079,-7.450929,1.838713,6.535449,-9.473513,-0.495162,9.398777,6.016995,5.252774,-6.743150,-4.415022,-7.627673,-9.980450,-8.294981,-9.146092,-3.706203,-4.093857,-4.664581,-1.661643,-9.606814,-6.066864,-0.587518,-5.911357,9.605217,-6.589880,6.464554,-5.680469,5.970685,-7.446311,7.526942,6.275497,2.319192,-3.483905,8.668928,3.349074,4.780770,-2.873841,4.832214,8.221854,1.468581,5.446089,-2.354361,-6.145919,-9.628911,7.766956,-2.279504,7.973888,8.131917,7.353569,-6.968213,-0.336413,-2.077184,2.144372,0.533552,6.055260,-5.988162,9.382021,-2.424594,-2.780065,8.941167,-6.904995,-6.108360,4.689570,3.788094,5.376530,-6.845355,6.072507,-7.476114,-7.656179], dtype = "float64")#candidate|17062|(84,)|const|float64
call_17060 = relay.TupleGetItem(func_14438_call(relay.reshape(var_17061.astype('float32'), [1287,]), relay.reshape(const_17062.astype('float64'), [84,]), ), 1)
call_17063 = relay.TupleGetItem(func_14442_call(relay.reshape(var_17061.astype('float32'), [1287,]), relay.reshape(const_17062.astype('float64'), [84,]), ), 1)
func_10246_call = mod.get_global_var('func_10246')
func_10248_call = mutated_mod.get_global_var('func_10248')
call_17067 = func_10246_call(relay.reshape(call_17039.astype('float32'), [4, 7, 1]))
call_17068 = func_10246_call(relay.reshape(call_17039.astype('float32'), [4, 7, 1]))
output = relay.Tuple([call_17036,call_17039,call_17060,var_17061,const_17062,call_17067,])
output2 = relay.Tuple([call_17037,call_17040,call_17063,var_17061,const_17062,call_17068,])
func_17073 = relay.Function([var_17061,], output)
mod['func_17073'] = func_17073
mod = relay.transform.InferType()(mod)
mutated_mod['func_17073'] = func_17073
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17074 = relay.var("var_17074", dtype = "float32", shape = (1287,))#candidate|17074|(1287,)|var|float32
func_17073_call = mutated_mod.get_global_var('func_17073')
call_17075 = func_17073_call(var_17074)
output = call_17075
func_17076 = relay.Function([var_17074], output)
mutated_mod['func_17076'] = func_17076
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17270 = relay.var("var_17270", dtype = "float64", shape = (8, 16, 3))#candidate|17270|(8, 16, 3)|var|float64
uop_17271 = relay.log(var_17270.astype('float64')) # shape=(8, 16, 3)
output = relay.Tuple([uop_17271,])
output2 = relay.Tuple([uop_17271,])
func_17274 = relay.Function([var_17270,], output)
mod['func_17274'] = func_17274
mod = relay.transform.InferType()(mod)
var_17275 = relay.var("var_17275", dtype = "float64", shape = (8, 16, 3))#candidate|17275|(8, 16, 3)|var|float64
output = func_17274(var_17275)
func_17276 = relay.Function([var_17275], output)
mutated_mod['func_17276'] = func_17276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16461_call = mod.get_global_var('func_16461')
func_16462_call = mutated_mod.get_global_var('func_16462')
call_17334 = func_16461_call()
call_17335 = func_16461_call()
func_16236_call = mod.get_global_var('func_16236')
func_16238_call = mutated_mod.get_global_var('func_16238')
call_17344 = func_16236_call()
call_17345 = func_16236_call()
func_7645_call = mod.get_global_var('func_7645')
func_7649_call = mutated_mod.get_global_var('func_7649')
const_17348 = relay.const([6.913199,9.880257,5.632258,-3.941354,-7.312207,-1.515542,7.099569,-0.355591,-6.310849,-5.284620,-4.252781,3.486323,0.585995,1.147332,9.939875,-1.214370,-1.654479,3.771704,-1.341165,-2.249490,6.614378,-6.681957,-2.913946,2.610367,-4.419818,7.922889,-4.608505,0.384194,7.663129,-7.975635,0.894169,6.965057,-4.076102,2.377162,-5.125401,2.317377,-4.494454,3.809079,6.584589,-4.087863,-6.373322,-4.199264,-3.829881,-6.968477,7.304378,6.645513,8.124406,-6.738271,9.839670,-4.967098,-5.308112,2.265648,-3.644073,8.540044,9.563799,5.433834,2.851230,6.592986,-8.543176,9.636621,-6.628637,-8.382189,-7.613686,-6.243670,-2.107975,6.590728,-2.390959,7.269570,5.894400,-3.060751,-0.943832,-6.648728,-8.039387,-0.514793,3.724235,-5.301691,-0.355279,9.793047,8.341476,-1.538724,1.396912,-0.095295,0.995495,-8.951661,3.431879,3.855339,-0.924251,5.041216,7.514977,5.138133,-3.226748,4.742334,-0.355755,8.273714,-4.048572,8.027418,7.122280,1.471153,-9.218445,-9.957169,7.785013,6.931960,8.195378,-4.653475,-0.093421,-0.732735,4.298711,6.956648,-7.073081,8.077121,8.952600,-8.769009,2.004353,5.859296,7.587998,1.204586,4.054509,8.979524,5.869506,-2.821271,7.944938,-9.227581,-9.745105,3.587892,-4.089338,4.442925,3.631817,5.148820,2.813594,-2.893607,-6.244849,7.489111,1.082287,-8.058203,-0.218875,-3.436779,1.728935,-5.915502,4.574700,9.227567,1.938020,9.117966,-3.269840,5.408230,8.813549,7.163214,3.379207,7.518812,0.617936,8.350467,-3.135608,8.226462,4.026594,8.707759,5.167500,-5.388828,6.216023,-9.453147,-9.572406,-4.320853,9.223271,5.638280,-0.694552,3.186916,8.641733,-0.494470,7.274624,9.998119,7.078711,5.146990,1.077547,0.993641,4.849303,6.482579,7.526254,5.888551,9.862497,4.394414,7.228401,9.499379,-7.956533,6.181001,2.337972,-1.503514,4.887728,-1.772299,9.136233,-3.394546,7.769703,3.040594,7.035620,8.516801,8.327164,-0.789513,-4.225592,3.972086,5.886187,-6.473984,-1.852434,-6.186600,-4.722951,-1.130782,-6.314008,-3.375087,-9.947129,6.740678,-6.691902,-3.544929,3.247387,-7.381048], dtype = "float64")#candidate|17348|(210,)|const|float64
var_17349 = relay.var("var_17349", dtype = "int16", shape = (1404,))#candidate|17349|(1404,)|var|int16
call_17347 = relay.TupleGetItem(func_7645_call(relay.reshape(const_17348.astype('float64'), [14, 15, 1]), relay.reshape(var_17349.astype('int16'), [1, 1404]), ), 2)
call_17350 = relay.TupleGetItem(func_7649_call(relay.reshape(const_17348.astype('float64'), [14, 15, 1]), relay.reshape(var_17349.astype('int16'), [1, 1404]), ), 2)
func_6258_call = mod.get_global_var('func_6258')
func_6262_call = mutated_mod.get_global_var('func_6262')
var_17354 = relay.var("var_17354", dtype = "uint32", shape = (220,))#candidate|17354|(220,)|var|uint32
var_17355 = relay.var("var_17355", dtype = "float32", shape = ())#candidate|17355|()|var|float32
const_17356 = relay.const([9.305675,-7.618090,-0.479679,9.833884,-9.341289,0.159731,-3.958398,8.646483,9.917672,-8.814754,-3.821685,-3.900395,-2.163599,1.088658,-0.806241,9.593648,-7.866059,2.401538,-8.723801,9.139130,-6.426315,2.292769,-5.930754,1.910905,-7.140825,-1.220150,-8.435093,1.621773,4.459025,-5.284553,-5.686421,-3.751042,1.949439,9.054665,-9.154583,9.199749,-8.094265,5.374863,6.999715,-0.737499,-6.874292,-5.758418,9.694765,3.791954,-5.425778,6.687098,4.082485,9.184231,9.297201,-6.206022,2.593136,8.490710,0.299218,3.489984,6.599915,-8.994175,-5.874431,-2.324193,-8.463437,8.746191,3.180671,5.313116,-2.784826,9.609015,-0.838565,1.178547,6.852635,2.912860,6.853623,8.974196,-4.955265,8.420442,3.473861,-8.194329,2.078131,-5.817753,-0.598661,-1.900019,9.271164,3.397558,7.198357,0.212158,3.154466,6.028297,6.652507,1.862336,-6.929403,3.103654,-0.482104,-9.871410,1.608708,-0.110843,-1.318254,-3.875564,-7.728593,3.427292,-7.652140,9.299803,9.475192,-0.240504,4.729016,-6.549881,-2.175477,8.181109,-8.220627,9.108983,5.860715,8.510571,-3.149184,7.979862,5.391607,-2.436030,2.103001,5.413304,0.591880,-7.020771,5.407351,-9.080779,-9.805133,-0.406401,5.559919,-0.875751,6.754371,1.624485,1.478146,2.345982,0.568855,-4.070475,1.441323,-6.044558,9.579326,0.769538,5.944030,0.810526,-2.791537,-5.940481,6.628584,-2.128353,2.199783,-0.824798,-4.818095,7.907679,8.692778,-1.098733,-0.861499,3.785977,5.126956,-3.190204,8.604408,-7.266301,-5.697038,1.714143,1.613599,-0.441707,8.639368,1.454076,-9.563442,-8.274493,-7.953922,-2.232000,3.615573,6.466780,9.706180,5.691825,7.167947,-7.549816,0.202463,7.562574,6.568729,4.007118,-2.176417,-7.552719,6.415578,-8.336708,7.811944,-7.265376,6.015805,-4.041451,-4.872989,4.637232,5.558072,9.165157,9.140919,-7.948091,-0.086057,-0.794190,-2.585143,-0.226187,9.581011,-3.065241,0.105043,6.861934,-4.069448,9.529728,7.163508,-6.531970,-1.815123,9.410155,-6.665585,-3.033585,4.314985,3.483669,8.736005,-7.209303,-5.862075,-0.722866,0.299154,-9.679489,1.698139,-3.431226,-2.890348,1.876621,-4.814144,9.928206,-6.310650,-9.304703,-2.715714,-1.315602,3.029074,-2.210128,9.115290,5.451945,-9.078569,-5.410648,-1.435449,-3.195168,8.157260,5.279268,7.171503,-3.436105,9.191714,4.659180,-5.849635,2.521150,-8.064170,8.217256,-2.689967,7.636635,7.014566,-3.358269,-1.325691,-7.031271,8.167444,-4.071401,-7.723447,-3.936848,9.410987,8.165558,1.125384,8.883417,-2.197608,0.135486,3.744074,0.953880,-9.221637,-7.151784,8.371613,-1.155515,1.869683,9.183135,4.027714,1.611808,8.949342,-8.858289,9.399078,4.404402,8.176973,5.765040,6.257652,0.952172,-6.194722,-0.015756,-3.480034,-0.156595,2.494554,-1.611596,-0.322557,4.007372,-2.870780,-0.171281,0.481985,-6.391348,8.049583,-3.430384,-1.829168,-8.979965,1.299323,-2.915003,-7.236563,2.163226,-8.113800,-5.365140,0.872404,8.238205,-9.490109,-2.970688,2.065362,-1.665654,-9.112013,6.133276,-8.997879,1.624249,-6.142928,4.333345,5.518335,6.518121,-9.613536,-7.604122,9.597690,-8.265357,4.332917,-5.212744,3.319136,3.640077,7.926477,-8.917588,4.420082,2.890955,-7.382988,-0.168283,-8.434823,6.236406,6.683053,-8.747478,6.432914,-3.364866,3.763657,2.735182,5.078040,-1.333371,6.571810,-6.540724,2.165768,3.986569,3.185798,6.948091,3.119692,-2.880188,-6.273068,7.073444,1.317620,-1.150676,-2.799390,4.752292,2.282321,-2.835876,7.784806,5.663153,7.259856,-1.861354,-1.139008,-3.160962,-9.374672,-1.437182,8.503043,5.835702,-1.073591,-6.268006,0.988195,-3.969719,2.942533,-6.996664,-1.672362,7.630458,-5.303781,-2.665167,5.238513,-0.438832,2.214299,-4.809169,-8.768493,-9.289837,-3.802538,-5.174754,-3.251621,-3.886329,6.407656,-0.137553,-9.712832,9.395866,9.144816,0.306059,-2.625800,4.923815,-1.453720,2.302782,8.251905,0.665388,-3.018643,8.398651,0.824521,-9.217304,-3.765202,-3.454929,8.939238,3.050697,1.924683,4.874771,-6.092171,6.796157,4.663880,-2.275771,-2.853301,-0.177545,9.901732,-5.856440,6.807624,9.741831,0.662009,-2.816586,-8.941812,-6.678377,-1.627158,8.260833,-7.551246,8.865765,9.692013,-9.275189,-9.006227,-4.770421,-9.168780,-4.702662,-2.823737,-5.785949,2.440742,-9.627396,-4.306389,2.275094,-3.070938,-3.316731,6.126402,-5.720111,7.383315,1.032716,5.808665,4.590701,-7.261236,4.444215,9.337021,-6.198208,-4.874791,-2.754852,1.125211,2.343935,8.852656,-3.552950,-7.965792,1.585823,6.482592,4.412498,2.883930,9.543398,-5.011533,-0.297332,-5.585151,-9.045483,8.423750,4.982195,-6.763441,-1.959443,-8.292275,-8.508290,-2.856363,-8.020477,-8.898061,-7.440184,-0.267699,8.328815,5.784421,2.613996,8.970879,-2.799419,-7.604352,3.387129,2.936755,-5.718169,2.552521,-7.064735,1.436011,3.980763,-2.215039,3.910993,3.074244,6.924067,-1.147744,-4.951776,-8.242785,-4.392479,3.010762,3.560948,5.190788,-3.058193,-2.210855,-5.320068,-0.580037,-8.481609,-9.275668,8.668545,-1.603312,-9.633033,5.100122,-6.105296,1.414882,3.615471,4.045053,5.578798,-5.773711,9.778652,-0.577240,-2.081265,5.203426,0.686386,-5.748996,-6.090888,6.155702,8.010822,1.591582,-4.609593,-3.138154,3.981905,-4.682044,6.393312,9.312087,-7.511294,-4.371672,-3.748736,7.913810,8.149203,-3.115740,-5.504342,-9.361684,0.871596,-9.826933,1.885743,2.328997,-5.558042,0.676377,-7.278794,-7.725840,3.561084,-1.764392,-4.113184,4.566973,3.023861,8.616653,-8.816747,-6.115530,-9.716324,5.892914,1.260989,-1.347602,7.968215,7.984693,-1.569021,-4.472909,8.732148,2.151366,-3.031880,5.376345,0.528856,3.368959,6.807831,9.033953,-3.294513,9.411272,7.480055,7.290654,9.009190,-8.868232,-9.178061,6.427731,3.635109,-4.386716,-8.408571,-0.885544,-4.732366,2.184849,7.721123,5.846365,0.609720,0.838949,3.501625,4.263329,-7.550077,-8.991584,-1.411292,-2.870612,0.442736], dtype = "float32")#candidate|17356|(588,)|const|float32
call_17353 = relay.TupleGetItem(func_6258_call(relay.reshape(var_17354.astype('uint32'), [11, 10, 2]), relay.reshape(var_17355.astype('float32'), []), relay.reshape(const_17356.astype('float32'), [588,]), ), 0)
call_17357 = relay.TupleGetItem(func_6262_call(relay.reshape(var_17354.astype('uint32'), [11, 10, 2]), relay.reshape(var_17355.astype('float32'), []), relay.reshape(const_17356.astype('float32'), [588,]), ), 0)
output = relay.Tuple([call_17334,call_17344,call_17347,const_17348,var_17349,call_17353,var_17354,var_17355,const_17356,])
output2 = relay.Tuple([call_17335,call_17345,call_17350,const_17348,var_17349,call_17357,var_17354,var_17355,const_17356,])
func_17368 = relay.Function([var_17349,var_17354,var_17355,], output)
mod['func_17368'] = func_17368
mod = relay.transform.InferType()(mod)
mutated_mod['func_17368'] = func_17368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17368_call = mutated_mod.get_global_var('func_17368')
var_17370 = relay.var("var_17370", dtype = "int16", shape = (1404,))#candidate|17370|(1404,)|var|int16
var_17371 = relay.var("var_17371", dtype = "uint32", shape = (220,))#candidate|17371|(220,)|var|uint32
var_17372 = relay.var("var_17372", dtype = "float32", shape = ())#candidate|17372|()|var|float32
call_17369 = func_17368_call(var_17370,var_17371,var_17372,)
output = call_17369
func_17373 = relay.Function([var_17370,var_17371,var_17372,], output)
mutated_mod['func_17373'] = func_17373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17005_call = mod.get_global_var('func_17005')
func_17006_call = mutated_mod.get_global_var('func_17006')
call_17382 = relay.TupleGetItem(func_17005_call(), 0)
call_17383 = relay.TupleGetItem(func_17006_call(), 0)
output = relay.Tuple([call_17382,])
output2 = relay.Tuple([call_17383,])
func_17389 = relay.Function([], output)
mod['func_17389'] = func_17389
mod = relay.transform.InferType()(mod)
mutated_mod['func_17389'] = func_17389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17389_call = mutated_mod.get_global_var('func_17389')
call_17390 = func_17389_call()
output = call_17390
func_17391 = relay.Function([], output)
mutated_mod['func_17391'] = func_17391
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17419 = relay.var("var_17419", dtype = "float32", shape = (9, 13, 5))#candidate|17419|(9, 13, 5)|var|float32
uop_17420 = relay.sigmoid(var_17419.astype('float32')) # shape=(9, 13, 5)
output = relay.Tuple([uop_17420,])
output2 = relay.Tuple([uop_17420,])
func_17438 = relay.Function([var_17419,], output)
mod['func_17438'] = func_17438
mod = relay.transform.InferType()(mod)
var_17439 = relay.var("var_17439", dtype = "float32", shape = (9, 13, 5))#candidate|17439|(9, 13, 5)|var|float32
output = func_17438(var_17439)
func_17440 = relay.Function([var_17439], output)
mutated_mod['func_17440'] = func_17440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15818_call = mod.get_global_var('func_15818')
func_15820_call = mutated_mod.get_global_var('func_15820')
call_17442 = func_15818_call()
call_17443 = func_15818_call()
func_14748_call = mod.get_global_var('func_14748')
func_14749_call = mutated_mod.get_global_var('func_14749')
call_17450 = func_14748_call()
call_17451 = func_14748_call()
output = relay.Tuple([call_17442,call_17450,])
output2 = relay.Tuple([call_17443,call_17451,])
func_17507 = relay.Function([], output)
mod['func_17507'] = func_17507
mod = relay.transform.InferType()(mod)
output = func_17507()
func_17508 = relay.Function([], output)
mutated_mod['func_17508'] = func_17508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_17518 = relay.TupleGetItem(func_15484_call(), 1)
call_17519 = relay.TupleGetItem(func_15485_call(), 1)
func_15898_call = mod.get_global_var('func_15898')
func_15899_call = mutated_mod.get_global_var('func_15899')
call_17533 = func_15898_call()
call_17534 = func_15898_call()
output = relay.Tuple([call_17518,call_17533,])
output2 = relay.Tuple([call_17519,call_17534,])
func_17535 = relay.Function([], output)
mod['func_17535'] = func_17535
mod = relay.transform.InferType()(mod)
output = func_17535()
func_17536 = relay.Function([], output)
mutated_mod['func_17536'] = func_17536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16915_call = mod.get_global_var('func_16915')
func_16916_call = mutated_mod.get_global_var('func_16916')
call_17540 = relay.TupleGetItem(func_16915_call(), 0)
call_17541 = relay.TupleGetItem(func_16916_call(), 0)
func_16865_call = mod.get_global_var('func_16865')
func_16867_call = mutated_mod.get_global_var('func_16867')
call_17558 = relay.TupleGetItem(func_16865_call(), 0)
call_17559 = relay.TupleGetItem(func_16867_call(), 0)
output = relay.Tuple([call_17540,call_17558,])
output2 = relay.Tuple([call_17541,call_17559,])
func_17571 = relay.Function([], output)
mod['func_17571'] = func_17571
mod = relay.transform.InferType()(mod)
output = func_17571()
func_17572 = relay.Function([], output)
mutated_mod['func_17572'] = func_17572
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17620 = relay.var("var_17620", dtype = "int32", shape = ())#candidate|17620|()|var|int32
var_17621 = relay.var("var_17621", dtype = "int32", shape = (5, 2, 11))#candidate|17621|(5, 2, 11)|var|int32
bop_17622 = relay.add(var_17620.astype('int32'), var_17621.astype('int32')) # shape=(5, 2, 11)
func_17368_call = mod.get_global_var('func_17368')
func_17373_call = mutated_mod.get_global_var('func_17373')
var_17646 = relay.var("var_17646", dtype = "int16", shape = (1404,))#candidate|17646|(1404,)|var|int16
const_17647 = relay.const([-4,-6,-3,6,-2,-5,-2,-2,-5,-6,4,-8,-6,6,-1,-8,3,1,-6,-1,6,3,-6,6,4,6,3,-8,4,-6,9,2,-7,-6,-10,3,-3,-5,-1,-10,2,-6,-9,3,-8,-10,2,-9,-5,-3,-3,10,-5,7,-5,-3,-5,1,5,9,4,2,-3,4,-5,-2,5,4,-8,-6,-8,-1,9,-6,7,-10,9,6,3,2,9,4,-8,4,7,-1,8,-7,8,-5,-3,8,7,5,-6,-5,1,-10,8,-6,-3,-2,-3,-2,-4,-5,-4,-8,7,-10,-8,-9,-6,9,5,3,-4,-3,-3,7,-3,-4,-3,7,-6,2,-4,5,2,-6,-1,8,-3,4,7,-3,4,-7,-2,7,-1,-1,10,7,-2,-10,1,2,-9,7,-10,8,10,2,-10,-9,8,8,-8,1,-7,4,-10,-9,5,-7,-10,10,8,1,1,-1,-2,8,-3,7,-1,-5,9,2,-1,10,3,1,-4,-1,6,3,-10,-5,1,2,-5,4,2,10,4,7,2,1,2,-2,-4,6,7,9,-3,1,-10,4,1,-5,3,-4,-10,2,5,-2,-10,-6], dtype = "uint32")#candidate|17647|(220,)|const|uint32
call_17645 = relay.TupleGetItem(func_17368_call(relay.reshape(var_17646.astype('int16'), [1404,]), relay.reshape(const_17647.astype('uint32'), [220,]), relay.reshape(var_17620.astype('float32'), []), ), 7)
call_17648 = relay.TupleGetItem(func_17373_call(relay.reshape(var_17646.astype('int16'), [1404,]), relay.reshape(const_17647.astype('uint32'), [220,]), relay.reshape(var_17620.astype('float32'), []), ), 7)
output = relay.Tuple([bop_17622,call_17645,var_17646,const_17647,])
output2 = relay.Tuple([bop_17622,call_17648,var_17646,const_17647,])
func_17661 = relay.Function([var_17620,var_17621,var_17646,], output)
mod['func_17661'] = func_17661
mod = relay.transform.InferType()(mod)
var_17662 = relay.var("var_17662", dtype = "int32", shape = ())#candidate|17662|()|var|int32
var_17663 = relay.var("var_17663", dtype = "int32", shape = (5, 2, 11))#candidate|17663|(5, 2, 11)|var|int32
var_17664 = relay.var("var_17664", dtype = "int16", shape = (1404,))#candidate|17664|(1404,)|var|int16
output = func_17661(var_17662,var_17663,var_17664,)
func_17665 = relay.Function([var_17662,var_17663,var_17664,], output)
mutated_mod['func_17665'] = func_17665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16942_call = mod.get_global_var('func_16942')
func_16944_call = mutated_mod.get_global_var('func_16944')
call_17667 = func_16942_call()
call_17668 = func_16942_call()
var_17699 = relay.var("var_17699", dtype = "int16", shape = (13, 3, 15))#candidate|17699|(13, 3, 15)|var|int16
bop_17700 = relay.logical_and(call_17667.astype('bool'), relay.reshape(var_17699.astype('bool'), relay.shape_of(call_17667))) # shape=(13, 3, 15)
bop_17703 = relay.logical_and(call_17668.astype('bool'), relay.reshape(var_17699.astype('bool'), relay.shape_of(call_17668))) # shape=(13, 3, 15)
func_16789_call = mod.get_global_var('func_16789')
func_16795_call = mutated_mod.get_global_var('func_16795')
var_17717 = relay.var("var_17717", dtype = "int16", shape = (9, 156))#candidate|17717|(9, 156)|var|int16
var_17718 = relay.var("var_17718", dtype = "int64", shape = (546,))#candidate|17718|(546,)|var|int64
const_17719 = relay.const([-2.295020,-7.096980,0.607250,6.827979,-2.585174,-4.100987,-0.632285,2.699676,9.116436,-8.536019,8.315928,-0.283341,7.495408,4.120633,0.886035,-7.974854,-4.183527,3.725868,3.789060,4.832897,5.860019,-4.057179,9.094895,9.572207,8.795257,-5.922349,2.365906,-5.704899,5.687198,9.664841,9.474265,-8.595834,-7.527365,0.287319,7.961827,4.096176,0.642185,-3.670746,5.757747,7.882455,6.608771,7.191361,5.538606,2.416987,1.320561,1.676294,-7.427366,-2.545453,5.317329,-6.128972,2.129520,-5.930195,-8.506303,5.742044,-2.262374,-6.292000,6.805099,-1.991755,-2.934033,2.689495,-7.875963,-6.639420,-1.677610,1.445655,-2.357815,-6.743939,5.910407,-6.456026,1.527528,-6.429205,8.179897,1.110530,-6.750178,8.736204,-4.844611,5.650347,6.099560,2.364008,-3.284826,-5.503516,7.746093,-9.842269,2.140954,-6.771012,9.715161,-2.604932,6.365427,2.069118,1.628666,-9.509062,0.281385,-9.305421,1.368224,-0.527718,-3.001827,2.333484,-5.972742,-7.517253,-1.984393,-9.619321,1.122689,-7.624554,7.103639,3.790635,-2.909111,-7.234303,8.542905,9.584764,-8.836623,-1.961693,-9.647851,-5.960107,-9.334521,-6.660321,2.381737,-7.933958,9.139962,-7.424441,-9.602471,8.867779,1.344880,-9.237722,-1.384006,-7.408501,8.781462,6.840449,-6.073081,-0.434994,-9.728899,1.026209,-0.924857,9.516132,6.424106,-8.830697,7.945663,-9.071665,1.892091,2.333764,-7.112893,-7.886380,-5.889305,9.910112,-3.491178,3.264202,-8.229960,-2.294197,-5.426188,-4.664988,6.117076,9.303325,-8.024951,-0.666340,-3.751339,6.839406,4.469838,4.322476,3.309881,-9.967691,-3.043042,7.012050,-7.087804,7.969139,7.853347,-0.167053,-5.207268,6.104678,-2.311770,-7.717733,8.970754,6.331466,-8.677764,-7.338867,-9.455151,7.891875,4.226038,0.443476,-4.363125,-8.899874,2.479186,8.331956,0.903476,-5.951278,-9.811980,-5.887894,7.986902,-3.589724,-7.278263,5.830188,3.787360,-8.746156,0.389274,-0.763102,-1.046469,4.591983,-3.790090,-2.415555,1.782904,6.680684,2.761177,3.091642,9.252094,-4.621788,2.940763,-4.589016,-7.846436,6.319968,4.298116,-6.911910,-6.568977,0.616538], dtype = "float32")#candidate|17719|(210,)|const|float32
var_17720 = relay.var("var_17720", dtype = "uint64", shape = (12, 3276))#candidate|17720|(12, 3276)|var|uint64
call_17716 = relay.TupleGetItem(func_16789_call(relay.reshape(var_17717.astype('int16'), [1404,]), relay.reshape(var_17718.astype('int64'), [546,]), relay.reshape(const_17719.astype('float32'), [105, 2]), relay.reshape(var_17720.astype('uint64'), [4, 7, 1404]), ), 1)
call_17721 = relay.TupleGetItem(func_16795_call(relay.reshape(var_17717.astype('int16'), [1404,]), relay.reshape(var_17718.astype('int64'), [546,]), relay.reshape(const_17719.astype('float32'), [105, 2]), relay.reshape(var_17720.astype('uint64'), [4, 7, 1404]), ), 1)
func_17507_call = mod.get_global_var('func_17507')
func_17508_call = mutated_mod.get_global_var('func_17508')
call_17736 = relay.TupleGetItem(func_17507_call(), 1)
call_17737 = relay.TupleGetItem(func_17508_call(), 1)
output = relay.Tuple([bop_17700,call_17716,var_17717,var_17718,const_17719,var_17720,call_17736,])
output2 = relay.Tuple([bop_17703,call_17721,var_17717,var_17718,const_17719,var_17720,call_17737,])
func_17738 = relay.Function([var_17699,var_17717,var_17718,var_17720,], output)
mod['func_17738'] = func_17738
mod = relay.transform.InferType()(mod)
mutated_mod['func_17738'] = func_17738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17738_call = mutated_mod.get_global_var('func_17738')
var_17740 = relay.var("var_17740", dtype = "int16", shape = (13, 3, 15))#candidate|17740|(13, 3, 15)|var|int16
var_17741 = relay.var("var_17741", dtype = "int16", shape = (9, 156))#candidate|17741|(9, 156)|var|int16
var_17742 = relay.var("var_17742", dtype = "int64", shape = (546,))#candidate|17742|(546,)|var|int64
var_17743 = relay.var("var_17743", dtype = "uint64", shape = (12, 3276))#candidate|17743|(12, 3276)|var|uint64
call_17739 = func_17738_call(var_17740,var_17741,var_17742,var_17743,)
output = call_17739
func_17744 = relay.Function([var_17740,var_17741,var_17742,var_17743,], output)
mutated_mod['func_17744'] = func_17744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17024_call = mod.get_global_var('func_17024')
func_17025_call = mutated_mod.get_global_var('func_17025')
call_17746 = relay.TupleGetItem(func_17024_call(), 0)
call_17747 = relay.TupleGetItem(func_17025_call(), 0)
output = call_17746
output2 = call_17747
func_17748 = relay.Function([], output)
mod['func_17748'] = func_17748
mod = relay.transform.InferType()(mod)
mutated_mod['func_17748'] = func_17748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17748_call = mutated_mod.get_global_var('func_17748')
call_17749 = func_17748_call()
output = call_17749
func_17750 = relay.Function([], output)
mutated_mod['func_17750'] = func_17750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14748_call = mod.get_global_var('func_14748')
func_14749_call = mutated_mod.get_global_var('func_14749')
call_17836 = func_14748_call()
call_17837 = func_14748_call()
func_4187_call = mod.get_global_var('func_4187')
func_4189_call = mutated_mod.get_global_var('func_4189')
var_17859 = relay.var("var_17859", dtype = "float64", shape = (100,))#candidate|17859|(100,)|var|float64
call_17858 = relay.TupleGetItem(func_4187_call(relay.reshape(var_17859.astype('float64'), [5, 2, 10])), 5)
call_17860 = relay.TupleGetItem(func_4189_call(relay.reshape(var_17859.astype('float64'), [5, 2, 10])), 5)
output = relay.Tuple([call_17836,call_17858,var_17859,])
output2 = relay.Tuple([call_17837,call_17860,var_17859,])
func_17861 = relay.Function([var_17859,], output)
mod['func_17861'] = func_17861
mod = relay.transform.InferType()(mod)
var_17862 = relay.var("var_17862", dtype = "float64", shape = (100,))#candidate|17862|(100,)|var|float64
output = func_17861(var_17862)
func_17863 = relay.Function([var_17862], output)
mutated_mod['func_17863'] = func_17863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16550_call = mod.get_global_var('func_16550')
func_16551_call = mutated_mod.get_global_var('func_16551')
call_17868 = relay.TupleGetItem(func_16550_call(), 1)
call_17869 = relay.TupleGetItem(func_16551_call(), 1)
output = call_17868
output2 = call_17869
func_17887 = relay.Function([], output)
mod['func_17887'] = func_17887
mod = relay.transform.InferType()(mod)
output = func_17887()
func_17888 = relay.Function([], output)
mutated_mod['func_17888'] = func_17888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16461_call = mod.get_global_var('func_16461')
func_16462_call = mutated_mod.get_global_var('func_16462')
call_17910 = func_16461_call()
call_17911 = func_16461_call()
func_15389_call = mod.get_global_var('func_15389')
func_15391_call = mutated_mod.get_global_var('func_15391')
call_17934 = relay.TupleGetItem(func_15389_call(), 0)
call_17935 = relay.TupleGetItem(func_15391_call(), 0)
func_17005_call = mod.get_global_var('func_17005')
func_17006_call = mutated_mod.get_global_var('func_17006')
call_17937 = relay.TupleGetItem(func_17005_call(), 0)
call_17938 = relay.TupleGetItem(func_17006_call(), 0)
func_6800_call = mod.get_global_var('func_6800')
func_6804_call = mutated_mod.get_global_var('func_6804')
const_17941 = relay.const([False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False], dtype = "bool")#candidate|17941|(528,)|const|bool
var_17942 = relay.var("var_17942", dtype = "int16", shape = (1404,))#candidate|17942|(1404,)|var|int16
call_17940 = relay.TupleGetItem(func_6800_call(relay.reshape(const_17941.astype('bool'), [12, 4, 11]), relay.reshape(const_17941.astype('bool'), [12, 4, 11]), relay.reshape(var_17942.astype('int16'), [1404,]), ), 1)
call_17943 = relay.TupleGetItem(func_6804_call(relay.reshape(const_17941.astype('bool'), [12, 4, 11]), relay.reshape(const_17941.astype('bool'), [12, 4, 11]), relay.reshape(var_17942.astype('int16'), [1404,]), ), 1)
output = relay.Tuple([call_17910,call_17934,call_17937,call_17940,const_17941,var_17942,])
output2 = relay.Tuple([call_17911,call_17935,call_17938,call_17943,const_17941,var_17942,])
func_17952 = relay.Function([var_17942,], output)
mod['func_17952'] = func_17952
mod = relay.transform.InferType()(mod)
var_17953 = relay.var("var_17953", dtype = "int16", shape = (1404,))#candidate|17953|(1404,)|var|int16
output = func_17952(var_17953)
func_17954 = relay.Function([var_17953], output)
mutated_mod['func_17954'] = func_17954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17389_call = mod.get_global_var('func_17389')
func_17391_call = mutated_mod.get_global_var('func_17391')
call_17975 = relay.TupleGetItem(func_17389_call(), 0)
call_17976 = relay.TupleGetItem(func_17391_call(), 0)
output = relay.Tuple([call_17975,])
output2 = relay.Tuple([call_17976,])
func_17977 = relay.Function([], output)
mod['func_17977'] = func_17977
mod = relay.transform.InferType()(mod)
mutated_mod['func_17977'] = func_17977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17977_call = mutated_mod.get_global_var('func_17977')
call_17978 = func_17977_call()
output = call_17978
func_17979 = relay.Function([], output)
mutated_mod['func_17979'] = func_17979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15146_call = mod.get_global_var('func_15146')
func_15148_call = mutated_mod.get_global_var('func_15148')
call_17984 = func_15146_call()
call_17985 = func_15146_call()
output = relay.Tuple([call_17984,])
output2 = relay.Tuple([call_17985,])
func_18004 = relay.Function([], output)
mod['func_18004'] = func_18004
mod = relay.transform.InferType()(mod)
output = func_18004()
func_18005 = relay.Function([], output)
mutated_mod['func_18005'] = func_18005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16974_call = mod.get_global_var('func_16974')
func_16975_call = mutated_mod.get_global_var('func_16975')
call_18019 = relay.TupleGetItem(func_16974_call(), 0)
call_18020 = relay.TupleGetItem(func_16975_call(), 0)
func_14486_call = mod.get_global_var('func_14486')
func_14493_call = mutated_mod.get_global_var('func_14493')
const_18022 = relay.const([-6.020338,-1.084751,-6.095600,-8.086546,-9.811255,-5.693388,8.614578,-8.809155,-3.496059,-6.042598,-5.621264,-8.561153,-8.572363,5.914039,3.991694,4.104660,8.794257,-2.103274,-6.654489,2.448980,-6.098946,-6.546998,1.682889,4.363550,4.989347,3.673800,-2.125687,-2.247472,-7.774686,-6.720844,5.665332,0.675032,-2.020616,7.056896,-8.506467,3.576257,-6.909973,-4.081284,-7.028268,3.605596,0.712901,0.714075,3.828900,-8.825492,-5.062034,2.002738,7.624840,-7.416942,9.390904,-4.796794,9.442953,-3.669849,0.893037,9.506143,-2.897147,-1.026680,-7.027390,9.713830,0.126315,1.013848,-5.539026,8.703490,3.972811,4.928686,5.027660,-1.737962,-2.038457,-1.280804,2.129178,6.710278,9.475445,3.075348,-9.645003,9.149493,-5.984711,8.134067,9.056404,-1.107072,-8.164458,4.405884,-2.252312,-9.340705,-7.096859,-3.976720,1.083225,4.111661,0.932357,-1.407023,5.649176,9.378702,-2.142035,6.914626,-3.655929,-9.316594,7.943311,-7.132028,4.926864,-9.141376,-7.869799,2.211750,7.871499,-3.793855,5.158746,-8.551914,-7.985453,-3.758511,-4.334297,-2.776550,-2.231903,6.792510,3.669975,0.255736,3.477111,-3.225987,-6.515811,5.687790,1.667692,5.098208,-1.734486,3.903592,1.368676,0.234094,0.461556,-9.251339,-2.810742,-2.646848,-8.026218,-8.447360,3.688111,4.937761,-0.940641,4.384940,-8.659472,-3.382216,-0.268957,1.653280,9.575882,6.366731,-4.247548,-3.521733,-4.685959,-6.656157,-3.426233,-1.729617,-4.727890,-5.994699,-1.302805,-1.422315,-0.582739,9.236156,-0.869682,-8.413662,6.253433,8.482881,-6.189345,-4.268463,-2.909781,0.912061,3.703475,-8.070755,9.730708,-9.122469,8.144085,-1.418924,9.025731,-5.474649,-4.147840,3.342530,1.303346,1.873672,1.299449,-5.755180,5.028535,-9.641388,2.175264,-1.803845,7.859069,-8.139512,0.360973,-4.796082,-1.158200,-5.974847,-1.616179,-4.855108,-2.545596,3.462346,6.317264,4.220419,6.513215,7.520143,0.985254,9.097043,-4.941851,4.705025,-3.016871,-3.243004,-2.604835,3.843589,-7.975727,-5.372101,6.347112,-8.753713,8.990706,7.296750,-3.263070,4.028872,-5.379468,-5.483015,-1.593460,-0.377879], dtype = "float32")#candidate|18022|(210,)|const|float32
var_18023 = relay.var("var_18023", dtype = "int16", shape = (1404,))#candidate|18023|(1404,)|var|int16
var_18024 = relay.var("var_18024", dtype = "int64", shape = (546,))#candidate|18024|(546,)|var|int64
var_18025 = relay.var("var_18025", dtype = "float64", shape = (364,))#candidate|18025|(364,)|var|float64
const_18026 = relay.const([4,-10,3,-8,8,-10,-9,5,-1,-2,6,2,8,1,5,-1,-9,3,-7,-4,9,5,-2,-5,-1,-2,7,-10,-3,2,-8,-7,6,-10,1,9,-7,1,7,4,5,5,-9,4,6,10,-1,-5,-6,-3,9,10,-8,-7,7,5,7,-1,-6,10,4,-6,-8,-3,5,3,10,2,-4,-5,10,10,-9,-6,9,5,-6,8,1,8,9,-2,5,-9,4,-10,1,4,3,2,-5,-7,7,5,-1,6,6,-1,3,-10,1,5,-1,1,-10,8,-10,-6,-10,-7,-4,3,2,-1,-1,5,-2,-5,9,7,-6,5,-9,5,10,2,-6,1,8,-4,-2,10,-9,-7,8,-8,-8,-2,-3,-10,-8,6,7,1,-1,4,-6,-9,1,5,-9,-6,7,-8,7,-3,10,9,9,5,-9,-3,-7,-1,-8,8,1,-6,5,9,2,7,1,3,7,10,-9,10,5,4,10,-3,-7,-1,7,-4,-2,-2,6,3,-5,7,5,-10,1,-8,-8,-5,-3,9,6,8,-6,-3,6,-6,-8,-5,-2,-7,-10,7,-7,-5,9,-10,-9,3,9,-10,1,-5,8,-5,-8,-5,-9,-8,-5,9,-9,8,-9,5,-6,-4,10,-9,-1,1,9,8,10,-8,-9,6,-8,-7,-5,5,-9,2,8,10,-8,-9,-6,-6,-2,-1,1,-10,4,-6,-2,-4,-1,2,10,1,10,-4,6,5,6,9,-5,-6,6,8,4,9,-8,7,3,-5,-9,-1,3,-2,-2,-4,-8,6,4,-2,-5,6,-3,3,-2,-1,1,5,-8,3,-8,8,9,1,-7,-2,7,-10,-2,8,-3,-6,-9,-10,-9,-8,10,-2,8,-4,8,9,-5,-6,2,-2,1,1,10,6,4,4,-9,-7,-2,2,-7,3,-10,1,-3,8,3,-3,-1,-2,-2,-3,5,-8,10,-6,10,1,10,-3,4,-6,-1,10,7,-8,-8,-2,2,-1,9,-1,9,-1,1,4,3,4,9,7,6,7,-8,-7,6,-5,7,5,6,-7,-10,-4,-10,-9,2,5,3,2,-8,4,-8,10,-4,1,5,-9,-8,-9,3,5,8,-3,-9,-2,5,2,8,-9], dtype = "uint32")#candidate|18026|(420,)|const|uint32
call_18021 = relay.TupleGetItem(func_14486_call(relay.reshape(const_18022.astype('float32'), [210,]), relay.reshape(var_18023.astype('int16'), [1404,]), relay.reshape(var_18024.astype('int64'), [546,]), relay.reshape(var_18025.astype('float64'), [364,]), relay.reshape(const_18026.astype('uint32'), [420,]), ), 8)
call_18027 = relay.TupleGetItem(func_14493_call(relay.reshape(const_18022.astype('float32'), [210,]), relay.reshape(var_18023.astype('int16'), [1404,]), relay.reshape(var_18024.astype('int64'), [546,]), relay.reshape(var_18025.astype('float64'), [364,]), relay.reshape(const_18026.astype('uint32'), [420,]), ), 8)
output = relay.Tuple([call_18019,call_18021,const_18022,var_18023,var_18024,var_18025,const_18026,])
output2 = relay.Tuple([call_18020,call_18027,const_18022,var_18023,var_18024,var_18025,const_18026,])
func_18045 = relay.Function([var_18023,var_18024,var_18025,], output)
mod['func_18045'] = func_18045
mod = relay.transform.InferType()(mod)
mutated_mod['func_18045'] = func_18045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18045_call = mutated_mod.get_global_var('func_18045')
var_18047 = relay.var("var_18047", dtype = "int16", shape = (1404,))#candidate|18047|(1404,)|var|int16
var_18048 = relay.var("var_18048", dtype = "int64", shape = (546,))#candidate|18048|(546,)|var|int64
var_18049 = relay.var("var_18049", dtype = "float64", shape = (364,))#candidate|18049|(364,)|var|float64
call_18046 = func_18045_call(var_18047,var_18048,var_18049,)
output = call_18046
func_18050 = relay.Function([var_18047,var_18048,var_18049,], output)
mutated_mod['func_18050'] = func_18050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14611_call = mod.get_global_var('func_14611')
func_14613_call = mutated_mod.get_global_var('func_14613')
call_18056 = relay.TupleGetItem(func_14611_call(), 0)
call_18057 = relay.TupleGetItem(func_14613_call(), 0)
output = call_18056
output2 = call_18057
func_18089 = relay.Function([], output)
mod['func_18089'] = func_18089
mod = relay.transform.InferType()(mod)
mutated_mod['func_18089'] = func_18089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18089_call = mutated_mod.get_global_var('func_18089')
call_18090 = func_18089_call()
output = call_18090
func_18091 = relay.Function([], output)
mutated_mod['func_18091'] = func_18091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14157_call = mod.get_global_var('func_14157')
func_14158_call = mutated_mod.get_global_var('func_14158')
call_18116 = relay.TupleGetItem(func_14157_call(), 2)
call_18117 = relay.TupleGetItem(func_14158_call(), 2)
output = call_18116
output2 = call_18117
func_18130 = relay.Function([], output)
mod['func_18130'] = func_18130
mod = relay.transform.InferType()(mod)
output = func_18130()
func_18131 = relay.Function([], output)
mutated_mod['func_18131'] = func_18131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_18132 = relay.TupleGetItem(func_15484_call(), 0)
call_18133 = relay.TupleGetItem(func_15485_call(), 0)
output = relay.Tuple([call_18132,])
output2 = relay.Tuple([call_18133,])
func_18150 = relay.Function([], output)
mod['func_18150'] = func_18150
mod = relay.transform.InferType()(mod)
mutated_mod['func_18150'] = func_18150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18150_call = mutated_mod.get_global_var('func_18150')
call_18151 = func_18150_call()
output = call_18151
func_18152 = relay.Function([], output)
mutated_mod['func_18152'] = func_18152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14611_call = mod.get_global_var('func_14611')
func_14613_call = mutated_mod.get_global_var('func_14613')
call_18156 = relay.TupleGetItem(func_14611_call(), 0)
call_18157 = relay.TupleGetItem(func_14613_call(), 0)
func_14438_call = mod.get_global_var('func_14438')
func_14442_call = mutated_mod.get_global_var('func_14442')
var_18159 = relay.var("var_18159", dtype = "float32", shape = (1287,))#candidate|18159|(1287,)|var|float32
const_18160 = relay.const([9.802688,-7.131707,0.867308,-5.234110,-7.836260,8.608630,8.008399,4.740611,1.895736,4.035775,4.485252,-7.508451,9.383370,-3.098436,8.812904,7.185915,-5.293433,-0.760890,2.144338,-8.531454,-7.684622,3.848836,-3.698941,0.490480,-9.508850,8.355491,0.745037,0.091115,8.961944,2.697674,-1.973753,9.161933,-3.692774,-1.595368,0.047711,3.692740,-4.667341,6.862278,9.841519,-3.641854,0.267952,8.691069,5.175048,9.758349,9.353615,7.871745,9.895459,-4.725339,3.533417,-0.246341,-3.054954,-9.727586,-1.007670,8.035624,4.124420,2.500732,6.914531,0.289249,8.668461,3.191928,7.082015,-9.931819,7.831549,-3.382373,8.268005,8.712469,-8.897975,-0.964835,-2.678876,-1.684169,-1.967138,-9.713193,-3.696714,-3.406320,4.502924,-4.639477,0.037906,8.598250,-8.583154,8.324429,-6.734118,8.110262,-5.043040,2.835292], dtype = "float64")#candidate|18160|(84,)|const|float64
call_18158 = relay.TupleGetItem(func_14438_call(relay.reshape(var_18159.astype('float32'), [1287,]), relay.reshape(const_18160.astype('float64'), [84,]), ), 3)
call_18161 = relay.TupleGetItem(func_14442_call(relay.reshape(var_18159.astype('float32'), [1287,]), relay.reshape(const_18160.astype('float64'), [84,]), ), 3)
func_16865_call = mod.get_global_var('func_16865')
func_16867_call = mutated_mod.get_global_var('func_16867')
call_18180 = relay.TupleGetItem(func_16865_call(), 0)
call_18181 = relay.TupleGetItem(func_16867_call(), 0)
output = relay.Tuple([call_18156,call_18158,var_18159,const_18160,call_18180,])
output2 = relay.Tuple([call_18157,call_18161,var_18159,const_18160,call_18181,])
func_18185 = relay.Function([var_18159,], output)
mod['func_18185'] = func_18185
mod = relay.transform.InferType()(mod)
var_18186 = relay.var("var_18186", dtype = "float32", shape = (1287,))#candidate|18186|(1287,)|var|float32
output = func_18185(var_18186)
func_18187 = relay.Function([var_18186], output)
mutated_mod['func_18187'] = func_18187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16550_call = mod.get_global_var('func_16550')
func_16551_call = mutated_mod.get_global_var('func_16551')
call_18203 = relay.TupleGetItem(func_16550_call(), 2)
call_18204 = relay.TupleGetItem(func_16551_call(), 2)
output = relay.Tuple([call_18203,])
output2 = relay.Tuple([call_18204,])
func_18212 = relay.Function([], output)
mod['func_18212'] = func_18212
mod = relay.transform.InferType()(mod)
mutated_mod['func_18212'] = func_18212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18212_call = mutated_mod.get_global_var('func_18212')
call_18213 = func_18212_call()
output = call_18213
func_18214 = relay.Function([], output)
mutated_mod['func_18214'] = func_18214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16688_call = mod.get_global_var('func_16688')
func_16689_call = mutated_mod.get_global_var('func_16689')
call_18243 = relay.TupleGetItem(func_16688_call(), 0)
call_18244 = relay.TupleGetItem(func_16689_call(), 0)
func_16942_call = mod.get_global_var('func_16942')
func_16944_call = mutated_mod.get_global_var('func_16944')
call_18258 = func_16942_call()
call_18259 = func_16942_call()
output = relay.Tuple([call_18243,call_18258,])
output2 = relay.Tuple([call_18244,call_18259,])
func_18261 = relay.Function([], output)
mod['func_18261'] = func_18261
mod = relay.transform.InferType()(mod)
mutated_mod['func_18261'] = func_18261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18261_call = mutated_mod.get_global_var('func_18261')
call_18262 = func_18261_call()
output = call_18262
func_18263 = relay.Function([], output)
mutated_mod['func_18263'] = func_18263
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18283 = relay.var("var_18283", dtype = "uint32", shape = (8, 9, 3))#candidate|18283|(8, 9, 3)|var|uint32
var_18284 = relay.var("var_18284", dtype = "uint32", shape = (8, 9, 3))#candidate|18284|(8, 9, 3)|var|uint32
bop_18285 = relay.greater_equal(var_18283.astype('bool'), relay.reshape(var_18284.astype('bool'), relay.shape_of(var_18283))) # shape=(8, 9, 3)
output = bop_18285
output2 = bop_18285
func_18288 = relay.Function([var_18283,var_18284,], output)
mod['func_18288'] = func_18288
mod = relay.transform.InferType()(mod)
mutated_mod['func_18288'] = func_18288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18288_call = mutated_mod.get_global_var('func_18288')
var_18290 = relay.var("var_18290", dtype = "uint32", shape = (8, 9, 3))#candidate|18290|(8, 9, 3)|var|uint32
var_18291 = relay.var("var_18291", dtype = "uint32", shape = (8, 9, 3))#candidate|18291|(8, 9, 3)|var|uint32
call_18289 = func_18288_call(var_18290,var_18291,)
output = call_18289
func_18292 = relay.Function([var_18290,var_18291,], output)
mutated_mod['func_18292'] = func_18292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15422_call = mod.get_global_var('func_15422')
func_15424_call = mutated_mod.get_global_var('func_15424')
call_18307 = relay.TupleGetItem(func_15422_call(), 0)
call_18308 = relay.TupleGetItem(func_15424_call(), 0)
const_18311 = relay.const([[[-4,-9,10,-8,6,7,8,-10,7,6,-4,3,7,7,-1],[-7,1,-6,7,-7,-3,-9,-4,8,2,-7,6,8,-3,7],[9,-9,-3,3,-10,4,-7,-8,4,2,-2,6,8,-1,8]],[[5,3,2,-10,5,7,5,4,3,-9,-6,4,9,6,3],[8,-5,-1,-5,2,-10,1,1,9,3,-8,9,1,-4,-5],[-10,4,-4,-2,5,-10,3,10,-7,9,-7,1,1,-3,8]],[[1,-3,-5,9,7,-1,8,-10,-7,9,9,5,3,3,-2],[-8,-10,9,7,3,3,-2,-8,-1,-9,5,8,9,5,-7],[-4,-9,5,2,-7,9,10,10,4,-7,4,3,1,3,-4]],[[4,-5,-2,2,-6,10,-8,5,-8,-9,-1,6,-5,6,2],[8,7,10,8,5,8,7,6,4,-2,1,-8,-7,-6,10],[-4,6,4,5,6,5,-7,-2,6,-1,10,4,-10,10,-6]],[[6,1,-3,5,-6,-10,-7,-3,10,-4,10,2,2,6,10],[6,-4,-5,1,-7,-3,8,-1,-8,4,3,-7,-9,1,-5],[-9,-4,-6,-2,-10,-4,5,2,6,-9,5,-6,1,3,3]],[[10,7,-7,-4,1,-9,9,-8,-9,3,5,-4,-10,6,-4],[9,1,1,-10,10,-8,-6,-2,-8,-9,1,-10,-6,-7,-4],[-3,6,-9,-3,-1,-10,-9,-8,1,2,-8,7,-5,8,5]],[[-4,5,2,6,-4,-8,9,-1,10,4,3,4,-10,10,10],[2,-6,3,-10,7,9,-10,-5,-5,2,-7,-1,-2,-8,3],[-2,2,-9,-9,-8,-4,-2,-5,-5,1,10,-2,-7,-6,-9]],[[-4,1,2,-5,-2,7,-7,-2,5,-3,-5,-2,-5,-1,5],[7,4,9,1,-5,6,1,-3,8,-8,-2,-5,10,-5,-9],[5,-4,-6,-3,7,-10,-1,8,3,2,6,-6,10,1,1]],[[8,7,-2,-4,-2,4,4,2,-1,-10,6,-7,-9,10,-4],[1,4,-3,3,-3,8,6,7,6,4,-1,3,5,-6,-1],[6,2,10,-8,5,-7,-1,7,-4,5,10,-10,-5,5,2]],[[2,8,9,3,2,-9,1,3,-7,4,6,-8,-6,-3,-4],[9,-2,4,-6,9,5,8,-1,5,-9,-9,-2,3,-2,3],[3,4,10,9,6,-3,-7,8,-3,5,3,-10,5,-7,2]],[[-2,9,-2,-5,4,-6,-4,-9,2,-7,-7,-3,7,10,2],[1,7,-4,-10,8,2,-2,-1,-9,6,-8,-6,8,8,5],[-8,-5,-8,-5,-8,2,-9,6,-9,10,3,-6,10,4,10]],[[9,-8,6,-3,-6,-4,-3,-5,2,6,-7,2,9,7,-2],[-3,-8,7,-6,-5,-1,1,9,-5,-9,-2,9,4,-8,1],[10,2,4,-4,-10,-5,7,7,3,6,10,-10,4,8,5]],[[-5,-3,6,6,10,-10,-9,10,-2,5,-4,-8,5,-10,-7],[4,3,8,-7,-9,2,-9,-6,-6,-1,-6,7,3,7,7],[-10,5,10,-3,2,1,3,5,-10,-8,4,-10,-10,-5,8]]], dtype = "uint16")#candidate|18311|(13, 3, 15)|const|uint16
bop_18312 = relay.right_shift(call_18307.astype('int64'), relay.reshape(const_18311.astype('int64'), relay.shape_of(call_18307))) # shape=(13, 3, 15)
bop_18315 = relay.right_shift(call_18308.astype('int64'), relay.reshape(const_18311.astype('int64'), relay.shape_of(call_18308))) # shape=(13, 3, 15)
output = relay.Tuple([bop_18312,])
output2 = relay.Tuple([bop_18315,])
func_18325 = relay.Function([], output)
mod['func_18325'] = func_18325
mod = relay.transform.InferType()(mod)
mutated_mod['func_18325'] = func_18325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18325_call = mutated_mod.get_global_var('func_18325')
call_18326 = func_18325_call()
output = call_18326
func_18327 = relay.Function([], output)
mutated_mod['func_18327'] = func_18327
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18381 = relay.var("var_18381", dtype = "float64", shape = (12, 16, 3))#candidate|18381|(12, 16, 3)|var|float64
uop_18382 = relay.tan(var_18381.astype('float64')) # shape=(12, 16, 3)
func_15389_call = mod.get_global_var('func_15389')
func_15391_call = mutated_mod.get_global_var('func_15391')
call_18388 = relay.TupleGetItem(func_15389_call(), 0)
call_18389 = relay.TupleGetItem(func_15391_call(), 0)
func_18288_call = mod.get_global_var('func_18288')
func_18292_call = mutated_mod.get_global_var('func_18292')
const_18401 = relay.const([-10,-1,7,4,10,6,8,-3,-9,-10,4,-9,-3,-5,1,3,10,8,-10,1,2,8,-9,10,-3,6,-10,-6,-7,-8,-2,-10,7,-4,-10,8,4,2,6,3,4,9,-6,1,-5,-2,9,3,-1,4,-2,3,-8,-1,-9,-6,-4,9,9,3,-8,-4,8,5,-4,9,1,2,-9,4,7,-2,-6,-1,2,2,9,-7,3,6,-2,5,-9,3,-2,-5,-10,2,-8,10,8,-8,-7,-6,10,10,-7,5,4,5,8,6,6,1,-10,-2,4,5,-8,6,3,9,-2,7,4,-3,1,-10,7,1,-6,-8,-4,4,6,-1,7,-10,-8,-7,10,-7,-1,-9,8,-8,2,7,-2,1,2,-6,4,9,4,6,-6,-6,8,7,-5,2,-2,-5,-9,-2,-10,1,-6,-8,4,6,-5,-9,8,-2,-3,-2,5,-1,6,7,-4,2,7,-2,-3,5,3,-4,-1,5,1,1,5,-2,5,-6,10,-1,-7,-9,3,10,-9,-8,9,6,-1,9,9,4,3,-5,8,-9,8,7,2,-9,10,-3,1,2,-6,-7], dtype = "uint32")#candidate|18401|(216,)|const|uint32
call_18400 = func_18288_call(relay.reshape(const_18401.astype('uint32'), [8, 9, 3]), relay.reshape(const_18401.astype('uint32'), [8, 9, 3]), )
call_18402 = func_18288_call(relay.reshape(const_18401.astype('uint32'), [8, 9, 3]), relay.reshape(const_18401.astype('uint32'), [8, 9, 3]), )
uop_18408 = relay.cosh(var_18381.astype('float32')) # shape=(12, 16, 3)
func_17507_call = mod.get_global_var('func_17507')
func_17508_call = mutated_mod.get_global_var('func_17508')
call_18416 = relay.TupleGetItem(func_17507_call(), 0)
call_18417 = relay.TupleGetItem(func_17508_call(), 0)
var_18434 = relay.var("var_18434", dtype = "float32", shape = (12, 16, 3))#candidate|18434|(12, 16, 3)|var|float32
bop_18435 = relay.bitwise_and(uop_18408.astype('uint16'), relay.reshape(var_18434.astype('uint16'), relay.shape_of(uop_18408))) # shape=(12, 16, 3)
func_3810_call = mod.get_global_var('func_3810')
func_3813_call = mutated_mod.get_global_var('func_3813')
const_18445 = relay.const(-8.437853, dtype = "float32")#candidate|18445|()|const|float32
const_18446 = relay.const([3.350594,-3.150679,1.154037,7.644072,-4.153931,1.992757,-8.327412,7.583327,1.561713,-9.677277,-0.639725,-3.047316,6.322431,1.789109,0.564573,-0.605476,-3.127755,-4.284242,8.801361,-5.629623,-0.203135,-5.123204,9.325883,-6.401758,7.014719,3.678658,6.920649,8.753678,6.744263,0.183239,1.849503,6.230114,2.501608,7.512052,4.334647,-4.527712,7.979286,-3.622433,-8.946638,-8.174928,1.668030,3.153860,9.210957,7.086481,4.304201,2.270163,-6.761870,1.848358,-3.689613,-1.574454,-5.470437,5.977375,8.824604,-7.781462,-3.983506,9.420056,-9.340400,-1.364690,4.788161,-8.485704,8.183146,-9.207450,-8.767759,1.057822,-5.040832,-1.208250,-2.386989,2.291309,3.047007,-0.596150,-2.787048,6.601782,-5.985947,-2.111107,0.661987,8.829425,0.681975,-3.238637,7.575271,-3.365493,9.885580,-3.227596,4.256307,6.497766,5.050940,-3.992509,2.808594,-4.201599,-5.109723,-2.229224,-6.145866,-5.131051,3.431749,7.450656,-9.772646,-7.976096,6.683375,5.134095,-8.095002,4.262757,-9.720849,8.208522,-7.002655,-6.127295,0.526834,-4.600354,-3.468002,3.989736,-0.038798,-2.404679,-9.837041,-0.400447,6.453181,-2.480613,3.066291,1.427876,-1.487701,7.338236,-7.400939,9.624376,-8.836718,5.552255,-4.494579,-6.537476,-0.075840,9.978730,-0.080953,-2.720453,2.178560,5.644498,-7.950832,6.191831,-7.541097,8.045149,-7.560229,-5.500484,1.062733,1.373822,-8.208451,-8.696586,-3.594188,0.070195,4.999933,-5.303062,4.211732,3.979114,-5.596529,-9.421217,-4.869432,8.953571,-2.229582,7.968320,-0.445014,0.938525,9.090393,9.521992,8.542057,-3.002328,-6.955881,3.323874,-4.439541,9.630166,1.602639,3.753683,-4.232670,-8.521333,-5.862651,-5.404920,-2.473285,5.339703,2.510067,5.389759,-5.737526,1.546323,-1.258393,-1.269990,-9.064097,6.296502,2.804828,6.968365,-3.058508,-6.986203,0.221947,9.502539,-3.529625,0.081386,5.271772,-9.005789,-8.867166,-0.800907,-8.081380,-4.271949,-2.500751,5.152794,-6.345826,2.441179,-8.437910,-4.889040,-9.541214,-0.912123,-3.113870,-2.761987,-2.767837,4.483485,8.692363,-3.168836,-0.362243,-4.170272,-6.172982,-8.537336,-2.500628,9.898485,6.385710,-3.603889,6.406056,-6.417985,1.091867,2.928358,6.949309,-5.860716,-4.829195,2.654435,7.933682,-8.551371,8.422503,6.428513,-0.817706,-2.308484,-4.136785,-9.693737,0.463028,0.744925,6.003456,7.270203,-0.475541,9.193420,-5.755735,6.894099,-1.602142,1.606113,3.072374,3.928129,-5.478403,7.277575,7.534154,-6.699077,0.888991,4.902570,9.489662,1.183747,-0.145851,-1.871590,2.919523,3.678452,3.655098,7.888409,1.876757,1.467516,3.527750,-5.465770,-4.493372,6.130419,-1.761288,-6.628016,2.196270,2.165969,9.510486,-6.917296,-0.464948,-4.739298,7.410751,-7.383359,5.518060,-8.822974,-9.429759,4.295060,1.101658,-4.741140,9.693280,8.951529,8.002391,-3.272272,6.631897,7.153217,-6.697068,3.870846,-5.429262,-0.012513,0.646280,-2.686367,3.842861,-8.919149,-3.125372,3.277412,-0.201961,3.680262,9.740032,-2.979273,-2.652514,-8.401720,3.880205,-4.535221,3.501557,7.479588,4.884906,6.256031,7.052307,-2.494440,-1.445959,0.333448,-9.033415,-6.522436,2.605267,-5.538051,6.257812,-1.275259,2.299178,-0.184907,-1.354786,3.268732,6.329228,-9.214371,8.959664,-9.049692,-7.930608,-0.671126,-7.769763,1.743418,6.914060,-7.466859,-8.891185,4.051439,7.536744,4.380324,-6.239698,-8.112146,1.532537,-6.153974,2.441729,-4.157764,8.365304,-1.596065,-6.100786,9.121881,-3.736254,-2.325400,-7.604153,-3.023524,2.590684,7.422058,-2.514916,5.198363,8.983239,-2.528345,-3.882781,-9.856317,3.740257,-1.743935,-5.147279,3.079697,1.514575,-6.280794,-0.515060,9.706816,-5.467591,2.126455,-5.968581,-4.735577,-8.166473,-7.828873,4.315745,-3.589247,-4.161965,-5.218314,-6.610929,2.660430,0.372473,-7.507022,-1.015014,3.070999,-3.366032,3.793403,1.542466,-5.020956,7.418011,5.366885,-7.418597,8.675619,-4.577803,3.488218,-5.554041,-9.928913,-1.724100,2.847592,-3.269229,4.914897,1.364374,-9.895813,-7.782498,-8.420824,6.428219,6.179772,-8.336837,-0.805687,-6.206389,9.520480,-4.966751,3.424398,-5.664688,4.933764,9.502543,-3.601027,-3.278196,-7.170471,0.752256,-2.708106,-4.565301,-9.647796,-8.208583,0.532317,9.531023,6.094846,-9.830287,-1.546115,4.182524,0.034152,3.060904,4.404242,-8.442102,-6.190208,7.211823,4.710075,-1.449678,-6.599333,-5.596410,-5.474576,-2.656557,-3.428900,-2.209072,-6.367306,-5.681019,-9.086692,4.847944,5.544826,9.756387,7.905181,-3.726237,-3.857184,7.904546,-8.530867,-6.851667,6.324000,-7.066899,8.490379,-6.714122,6.517959,-4.374622,-3.622058,2.653007,9.491927,-9.570396,2.513485,7.963771,8.755392,-7.545144,4.238123,-7.979277,-0.413763,-1.441673,6.036568,9.759935,6.474801,1.915026,7.389866,-3.130864,3.617987,6.564980,8.158302,2.066720,4.599769,-6.786340,-8.797382,0.017273,-7.297247,0.969754,6.425735,-2.845222,-1.277159,-4.498796,-6.351279,-5.909336,8.408826,2.792964,4.123846,-3.404577,-8.782441,3.139857,4.252081,3.773691,-1.107180,-5.860572,8.429991,-6.413965,-3.310628,5.227078,9.380132,-4.247035,-0.112036,-3.597437,-7.629631,-8.514660,0.024542,-3.594453,4.455148,-0.802030,-8.663956,6.020244,5.313416,7.852725,-4.239559,7.728339,-3.351213,1.633717,3.346480,-3.250432,-4.514476,-7.114735,-5.331660,-2.213784,0.274840,2.966397,9.605233,6.475226,5.850483,-5.525286,-4.323083,2.989325,-9.570901,9.479911,-0.095163,9.064186,-6.770588,9.398203,-7.466631,-1.058451,-8.946456,3.874566,-7.143481,9.714764,3.827089,-2.599593,4.243085,0.621735,-8.480863,7.079409,-7.992200,3.929111,-4.715803,-0.627807,-5.640972,-2.562100,-7.055349,5.573116,6.267643,-8.588849,-9.085486,-9.030479,2.470614,2.715016,-8.234719,-7.105064,-9.013004,2.175346,-0.263266,5.315746,3.404017,-1.722549,-2.721928,-5.645937,-8.042441,-0.849913,0.345065,-5.674647,-4.099543,-5.066739,-2.933637,-1.463299,-0.188795], dtype = "float32")#candidate|18446|(588,)|const|float32
call_18444 = func_3810_call(relay.reshape(const_18445.astype('float32'), []), relay.reshape(const_18446.astype('float32'), [14, 14, 3]), )
call_18447 = func_3810_call(relay.reshape(const_18445.astype('float32'), []), relay.reshape(const_18446.astype('float32'), [14, 14, 3]), )
func_18185_call = mod.get_global_var('func_18185')
func_18187_call = mutated_mod.get_global_var('func_18187')
var_18450 = relay.var("var_18450", dtype = "float32", shape = (429, 3))#candidate|18450|(429, 3)|var|float32
call_18449 = relay.TupleGetItem(func_18185_call(relay.reshape(var_18450.astype('float32'), [1287,])), 2)
call_18451 = relay.TupleGetItem(func_18187_call(relay.reshape(var_18450.astype('float32'), [1287,])), 2)
uop_18455 = relay.log2(bop_18435.astype('float64')) # shape=(12, 16, 3)
func_14973_call = mod.get_global_var('func_14973')
func_14975_call = mutated_mod.get_global_var('func_14975')
var_18459 = relay.var("var_18459", dtype = "bool", shape = (528,))#candidate|18459|(528,)|var|bool
call_18458 = relay.TupleGetItem(func_14973_call(relay.reshape(var_18459.astype('bool'), [24, 22])), 0)
call_18460 = relay.TupleGetItem(func_14975_call(relay.reshape(var_18459.astype('bool'), [24, 22])), 0)
func_16688_call = mod.get_global_var('func_16688')
func_16689_call = mutated_mod.get_global_var('func_16689')
call_18463 = relay.TupleGetItem(func_16688_call(), 0)
call_18464 = relay.TupleGetItem(func_16689_call(), 0)
output = relay.Tuple([uop_18382,call_18388,call_18400,const_18401,call_18416,call_18444,const_18445,const_18446,call_18449,var_18450,uop_18455,call_18458,var_18459,call_18463,])
output2 = relay.Tuple([uop_18382,call_18389,call_18402,const_18401,call_18417,call_18447,const_18445,const_18446,call_18451,var_18450,uop_18455,call_18460,var_18459,call_18464,])
func_18488 = relay.Function([var_18381,var_18434,var_18450,var_18459,], output)
mod['func_18488'] = func_18488
mod = relay.transform.InferType()(mod)
mutated_mod['func_18488'] = func_18488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18488_call = mutated_mod.get_global_var('func_18488')
var_18490 = relay.var("var_18490", dtype = "float64", shape = (12, 16, 3))#candidate|18490|(12, 16, 3)|var|float64
var_18491 = relay.var("var_18491", dtype = "float32", shape = (12, 16, 3))#candidate|18491|(12, 16, 3)|var|float32
var_18492 = relay.var("var_18492", dtype = "float32", shape = (429, 3))#candidate|18492|(429, 3)|var|float32
var_18493 = relay.var("var_18493", dtype = "bool", shape = (528,))#candidate|18493|(528,)|var|bool
call_18489 = func_18488_call(var_18490,var_18491,var_18492,var_18493,)
output = call_18489
func_18494 = relay.Function([var_18490,var_18491,var_18492,var_18493,], output)
mutated_mod['func_18494'] = func_18494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16974_call = mod.get_global_var('func_16974')
func_16975_call = mutated_mod.get_global_var('func_16975')
call_18509 = relay.TupleGetItem(func_16974_call(), 0)
call_18510 = relay.TupleGetItem(func_16975_call(), 0)
func_17438_call = mod.get_global_var('func_17438')
func_17440_call = mutated_mod.get_global_var('func_17440')
call_18513 = relay.TupleGetItem(func_17438_call(relay.reshape(call_18509.astype('float32'), [9, 13, 5])), 0)
call_18514 = relay.TupleGetItem(func_17440_call(relay.reshape(call_18509.astype('float32'), [9, 13, 5])), 0)
output = relay.Tuple([call_18509,call_18513,])
output2 = relay.Tuple([call_18510,call_18514,])
func_18515 = relay.Function([], output)
mod['func_18515'] = func_18515
mod = relay.transform.InferType()(mod)
output = func_18515()
func_18516 = relay.Function([], output)
mutated_mod['func_18516'] = func_18516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17748_call = mod.get_global_var('func_17748')
func_17750_call = mutated_mod.get_global_var('func_17750')
call_18530 = func_17748_call()
call_18531 = func_17748_call()
output = relay.Tuple([call_18530,])
output2 = relay.Tuple([call_18531,])
func_18561 = relay.Function([], output)
mod['func_18561'] = func_18561
mod = relay.transform.InferType()(mod)
mutated_mod['func_18561'] = func_18561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18561_call = mutated_mod.get_global_var('func_18561')
call_18562 = func_18561_call()
output = call_18562
func_18563 = relay.Function([], output)
mutated_mod['func_18563'] = func_18563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17389_call = mod.get_global_var('func_17389')
func_17391_call = mutated_mod.get_global_var('func_17391')
call_18564 = relay.TupleGetItem(func_17389_call(), 0)
call_18565 = relay.TupleGetItem(func_17391_call(), 0)
output = call_18564
output2 = call_18565
func_18576 = relay.Function([], output)
mod['func_18576'] = func_18576
mod = relay.transform.InferType()(mod)
output = func_18576()
func_18577 = relay.Function([], output)
mutated_mod['func_18577'] = func_18577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18588 = relay.var("var_18588", dtype = "uint64", shape = (3, 9, 14))#candidate|18588|(3, 9, 14)|var|uint64
const_18589 = relay.const([[[8,-6,8,-1,10,3,-7,5,8,5,3,-8,2,-7],[10,-7,-1,-5,2,7,-7,7,3,-9,3,-4,3,-7],[6,4,-8,-4,-5,-8,-4,1,9,5,-2,-10,8,1],[-6,10,4,7,4,-1,-2,-6,-5,-8,-4,4,-7,3],[10,1,-4,-7,-3,-2,-6,8,1,-2,10,1,-5,4],[-1,9,2,-7,-1,7,-9,-2,10,-10,-3,-9,6,-9],[-5,3,9,-7,-4,-7,9,8,3,-2,8,-7,-6,-6],[-6,-3,9,7,10,8,10,-6,3,8,3,-10,4,4],[4,2,6,-9,3,-2,3,4,7,-4,-5,-6,-2,1]],[[-6,6,6,7,7,-4,5,-1,6,-2,7,-5,8,-1],[10,8,1,-3,6,-9,-10,-3,-1,-1,-2,-1,-9,-1],[10,9,8,-3,3,-7,9,-2,-1,2,-1,-10,-6,-2],[-9,-1,-9,-6,-10,-7,8,2,8,-6,8,2,3,-2],[4,5,1,2,-8,8,-1,1,-6,7,-8,4,3,7],[9,6,-5,9,-8,-7,-9,-4,-9,10,-9,-1,1,3],[5,-1,-9,-10,-7,2,9,-2,6,9,-1,3,5,7],[1,-2,-7,-3,-10,-1,-1,2,4,-8,-10,-6,-3,2],[-2,6,8,2,-10,4,-7,7,-9,7,3,-4,10,5]],[[-8,3,-8,7,-6,-1,-3,4,-9,-9,-2,-2,2,9],[5,-7,-2,4,9,4,-10,10,10,-5,-9,-9,-1,-7],[6,-6,1,-5,6,-1,-1,-10,1,-4,8,-4,-4,-7],[4,7,-9,3,6,2,-7,7,-1,-9,-7,-5,-2,1],[4,8,-1,9,8,1,-10,-4,-8,-5,7,1,-6,-10],[-7,-4,-8,-10,7,-2,-5,-9,-6,4,-5,2,2,8],[10,-6,-1,-10,3,10,3,-7,5,-3,-10,-6,3,-8],[9,-3,-6,-8,9,5,-1,-4,-9,1,8,6,1,4],[9,-1,6,7,-4,8,-6,5,-10,-10,-1,-4,6,-8]]], dtype = "uint64")#candidate|18589|(3, 9, 14)|const|uint64
bop_18590 = relay.less_equal(var_18588.astype('bool'), relay.reshape(const_18589.astype('bool'), relay.shape_of(var_18588))) # shape=(3, 9, 14)
func_16236_call = mod.get_global_var('func_16236')
func_16238_call = mutated_mod.get_global_var('func_16238')
call_18600 = func_16236_call()
call_18601 = func_16236_call()
var_18621 = relay.var("var_18621", dtype = "uint64", shape = (3, 9, 14))#candidate|18621|(3, 9, 14)|var|uint64
bop_18622 = relay.logical_and(var_18588.astype('bool'), relay.reshape(var_18621.astype('bool'), relay.shape_of(var_18588))) # shape=(3, 9, 14)
func_9929_call = mod.get_global_var('func_9929')
func_9932_call = mutated_mod.get_global_var('func_9932')
const_18627 = relay.const([-4.689118,-5.425399,0.981420,6.816495,-4.605073,2.736788,-3.626333,1.003941,-4.860602,0.429595,6.532185,0.279046,-7.849505,2.332767,-6.278327,1.148110,9.663514,-0.254797,1.554138,2.472366,6.637680,8.656849,-5.454581,-2.359343,3.241570,5.599774,7.137751,4.504069,-8.060164,-5.520385,4.534356,9.211438,0.811555,-4.880637,-5.667707,-9.793733,-8.011077,3.400563,-1.643301,6.157519,1.292485,-0.584415,-1.269649,-1.586561,-3.366660,2.267007,-6.933627,8.689366,-3.958493,-0.169339,2.720845,0.032538,-9.371174,-2.036339,-6.550432,1.309185,-3.135138,-3.556717,2.951233,3.351736,9.304147,1.231422,-2.922169,0.998558,-8.017422,0.886358,-5.062104,-3.732267,5.466477,1.212218,-0.573414,6.538825,-0.269188,8.115013,-1.976936,-5.123427,6.991540,-5.335467,-3.985281,4.059505,3.520128,-4.703075,1.642357,4.947276,-7.163116,-5.033653,6.128444,2.801155,1.425680,8.726558,-8.260193,-5.633798,2.596618,3.986431,-8.325706,8.805359,2.738435,-2.055650,-9.821442,0.520075,-7.353188,3.079843,8.789643,-8.267943,-1.293432,-5.021226,0.613120,-6.783738,8.056220,-6.246576,-9.268614,-5.362570,1.305191,-1.515590,-8.563211,-8.973762,1.486194,-8.394636,3.256998,-7.247443,-9.994370,-6.832350,1.993507,-8.764279,-5.020680,-7.298075,-0.851288,-0.433072,1.403038,9.288645,-9.184682,4.007758,-5.506549,-6.254948,-8.329983,5.056396,6.519625,-2.058261,-0.903290,-9.074002,9.767657,-5.605079,3.053727,5.122678,4.480929,-9.086764,1.307922,-6.352150,1.641324,4.965074,4.171632,-4.020063,-8.086898,0.587120,3.620022,7.489124,-4.028849,7.528891,-5.698192,2.199343,3.312697,2.844610,4.390323,-8.557479,-8.164875,-2.894997,-8.564421,-3.152310,1.813511,-3.474942,5.181481,8.152246,1.876505,1.021642,2.873312,1.664893,-7.629617,7.196476,-9.107316,-2.625749,4.282802,-6.594757,1.818755,-6.050503,-9.693956,-6.144947,-5.258800,-2.279218,-3.784418,3.006469,-7.095524,-7.338206,7.087005,-0.469026,-8.429929,-3.865180,4.572276,1.446520,-3.320135,8.021774,-5.653806,-1.526314,5.317256,-8.313754,5.137310,2.716502,6.341502,-4.891835,-2.857420,-9.886215,-8.374222,-4.857146,-4.570848,-0.791106,-1.409490,4.736264,1.999544,0.610082,-7.853746,-7.039782,-7.414457,4.233565,-8.516265,-2.294052,-4.716261,1.913027,-9.961691,-7.844450,1.081211,3.644615,-6.987274,2.563622,-8.237399,-2.218234,-1.666170,-2.294030,2.047924,-8.306278,-1.189526,-2.928189,-2.136141,5.762182,6.602114,9.546603,-0.097260,-0.644425,8.269399,9.583236,7.766218,1.456155,-6.802968,-4.250418,1.433126,5.994379,9.091632,1.925072,1.828542,-9.521824,-4.287546,-5.716264,-9.074291,-0.620768,-6.743138,-4.901691,8.062625,2.855519,9.141177,4.829192,9.371551,-2.689509,-5.990962,-6.789375,-8.377960,1.817122,-6.325906,-8.738022,-1.195500,-4.531061,-1.456382,-1.314344,-7.654875,7.555642,6.698042,0.207916,-4.581536,-5.169374,0.126180,-5.444795,7.120759,-0.900633,9.658217,5.956577,1.393587,-9.700994,-5.189538,-5.071410,8.158442,-4.918356,-6.974876,9.322066,-7.586531,-2.160993,-4.226595,6.557714,-8.035170,4.197077,-3.116993,3.189641,-0.784840,3.922372,7.098319,-3.372778,-5.150939,4.675041,-9.875454,0.094728,-9.987136,-3.524574,-7.813161,9.874423,2.587439,4.304479,3.173764,-3.677575,-1.479570,-7.945211,0.628233,-0.417079,0.773274,-1.097873,-9.461538,-9.760131,7.460350,1.809037,9.079489,-2.677985,6.864586,-3.863188,0.532469,0.167616,9.582419,3.744171,-9.546663,-7.274112,1.436446,5.109780,-9.659595,3.938733,-4.069329,1.014497,9.410157,-2.103719,3.360820,6.480243,0.972870,5.546947,-8.484210,6.754181,-7.180598,-3.542648,6.323442,-5.073986,-2.634883,6.405426,-9.216411,-9.705910,4.976585,7.528042,8.044650,2.126418,3.163206,5.184505,9.083100,-7.589082,-0.202780,2.321022,-4.193680,7.671036,0.171767,4.152928,-3.426348,6.566800,-0.927043,-1.877218,2.128419,0.271136,-9.867698,-3.432227,5.551588,-0.866462,-2.665738,8.080834,5.121457,8.757961,-6.120524,-8.417747,-1.289957,-3.652087,-2.578412,-1.945570,-5.383979,-3.667737,2.259713,-9.371755,0.560911,-6.462987,-4.251270,-5.789211,6.628634,7.168491,-3.843932,-4.826456,1.734381,-3.273049,1.423376,-7.346798,-9.741596,8.835638,0.081235,-2.848684,-4.071507,-2.894339,9.690888,-9.364373,-1.638487,-7.510407,5.698530,3.881777,6.257437,1.070031,2.487893,-2.116873,-1.441090,7.269025,3.005750,5.548729,-6.010375,-7.677979,-6.835483,-3.365343,-2.978525,-2.457431,1.186970,8.583170,4.055284,-2.138440,-2.149302,-8.074023,-9.606094,-8.976781,5.776897,4.338113,-3.834971,3.299890,-7.070362,4.948442,-8.572012,-4.046527,-3.310972,-2.106067,-3.559114,-1.590391,7.219422,-4.500992,-2.262921,5.141920,-2.007328,1.519039,6.739810,8.879066,3.341690,-6.640836,-4.503795,2.768102,-7.914316,-1.030798,-7.960177,9.191165,9.654272,2.972910,0.386240,-0.903997,8.959621,-8.259831,-8.517116,-2.520121,-7.097984,-8.894557,-5.961876,6.528708,4.594628,8.690822,-9.141258,-3.684608,-7.656888,1.424889,-6.684529,9.175640,-6.552841,-7.854544,-5.720982,-3.322845,-9.471334,4.372637,-0.931959,5.783556,4.390390,-2.640635,-4.065301,7.015545,-2.288068,-2.050331,-3.034187,4.677293,0.152670,-9.100344,-6.525882,-8.333525,1.345643,0.610285,0.993010,3.751968,-3.730867,-9.829255,-5.028836,4.927432,4.745781,-3.870295,-1.890697,-2.209961,2.840050,2.191877,9.034402,-4.492910,5.701084,-6.648229,4.747436,4.678734,2.806239,-9.578002,-9.152575,9.074230,6.683592,1.566675,0.392155,1.772759,-3.696330,-4.417661,-5.542028,-3.589562,4.946343,-3.445585,6.020507,-9.897847,-0.461000,-3.422794,-6.600041,-6.198658,6.561887,0.834081,5.875373,-7.145287,9.539288,8.309273,2.015587,-4.909519,-2.902684,8.687383,-0.120549,1.127231,-4.325682,0.636324,1.885787,-3.617177,-4.755152,9.491677,-7.539899,6.391004,-0.669146,-8.266731,5.879325,-6.944027,0.703669,8.102661,8.079418,-5.689378,-5.776564,3.806779], dtype = "float32")#candidate|18627|(588,)|const|float32
call_18626 = relay.TupleGetItem(func_9929_call(relay.reshape(const_18627.astype('float32'), [14, 3, 14])), 0)
call_18628 = relay.TupleGetItem(func_9932_call(relay.reshape(const_18627.astype('float32'), [14, 3, 14])), 0)
func_10246_call = mod.get_global_var('func_10246')
func_10248_call = mutated_mod.get_global_var('func_10248')
call_18653 = func_10246_call(relay.reshape(call_18600.astype('float32'), [4, 7, 1]))
call_18654 = func_10246_call(relay.reshape(call_18600.astype('float32'), [4, 7, 1]))
func_18130_call = mod.get_global_var('func_18130')
func_18131_call = mutated_mod.get_global_var('func_18131')
call_18655 = func_18130_call()
call_18656 = func_18130_call()
output = relay.Tuple([bop_18590,call_18600,bop_18622,call_18626,const_18627,call_18653,call_18655,])
output2 = relay.Tuple([bop_18590,call_18601,bop_18622,call_18628,const_18627,call_18654,call_18656,])
func_18658 = relay.Function([var_18588,var_18621,], output)
mod['func_18658'] = func_18658
mod = relay.transform.InferType()(mod)
mutated_mod['func_18658'] = func_18658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18658_call = mutated_mod.get_global_var('func_18658')
var_18660 = relay.var("var_18660", dtype = "uint64", shape = (3, 9, 14))#candidate|18660|(3, 9, 14)|var|uint64
var_18661 = relay.var("var_18661", dtype = "uint64", shape = (3, 9, 14))#candidate|18661|(3, 9, 14)|var|uint64
call_18659 = func_18658_call(var_18660,var_18661,)
output = call_18659
func_18662 = relay.Function([var_18660,var_18661,], output)
mutated_mod['func_18662'] = func_18662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15709_call = mod.get_global_var('func_15709')
func_15710_call = mutated_mod.get_global_var('func_15710')
call_18708 = relay.TupleGetItem(func_15709_call(), 1)
call_18709 = relay.TupleGetItem(func_15710_call(), 1)
func_14973_call = mod.get_global_var('func_14973')
func_14975_call = mutated_mod.get_global_var('func_14975')
var_18712 = relay.var("var_18712", dtype = "bool", shape = (528,))#candidate|18712|(528,)|var|bool
call_18711 = relay.TupleGetItem(func_14973_call(relay.reshape(var_18712.astype('bool'), [24, 22])), 1)
call_18713 = relay.TupleGetItem(func_14975_call(relay.reshape(var_18712.astype('bool'), [24, 22])), 1)
func_14253_call = mod.get_global_var('func_14253')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_18714 = relay.TupleGetItem(func_14253_call(), 0)
call_18715 = relay.TupleGetItem(func_14254_call(), 0)
func_8163_call = mod.get_global_var('func_8163')
func_8166_call = mutated_mod.get_global_var('func_8166')
const_18728 = relay.const([-3,-6,-3,5,-10,-8,2,-10,6,-9,-2,8,-10,8,-5,10,6,-2,5,-10,4,7,-6,4,-4,-8,7,6,3,3,8,5,1,5,-5,-8,-3,-6,4,4,3,6,10,-1,-7,10,-10,-1,4,-5,-1,9,-10,6,7,9,1,-1,-9,-3,-9,-4,-10,7,1,3,5,-9,-1,6,-4,-7,4,8,-2,-10,6,9,-10,-7,8,-4,-6,-7,-7,-4,-2,8,10,-9,-8,5,-2,-9,-9,-3,8,10,-2,10,4,10,4,-1,-3,9,9,7,-8,-6,-1,-6,10,-3,-6,10,7,-5,-10,-7,9,6,2,3,-10,-1,-10,1,4,2,9,10,-4,6,3,8,-1,-2,-10,5,6,10,-2,5,7,7,-1,-9,-2,-10,-2,9,-5,-6,-9,-4,8,10,4,-7,-5,6,-1,-5,-4,10,-3,7,3,4,8,-7,-1,8,4,-6,-10,-7,9,-6,6,7,8,-9,9,4,-9,-4,8,6,9,-1,6,2,1,-8,-7,-6,9,5,-9,7,-10,8,5,9,10,5,-1,1,6,-9,-4,-7,2,-3,10,9,-1,9,-5,-1,10,10,2,3,9,-10,-5,-6,-8,-8,-8,-10,7,6,8,6,-1,7,-6,-1,2,-9,-8,-4,3,5,-10,-10,-2,9,-2,-8,-1,-6,7,3,-1,-6,9,-5,3,-4,3,-2,-10,7,-7,-5,-1,-7,-2,-6,5,2,-4,-6,7,2,6,6,-6,-8,-9,-3,-7,7,-3,2,6,1,1,5,-9,-9,-2,1,-10,-2,1,9,10,-7,10,-2,-3,4,-4,3,7,-8,-7,-8,-7,7,-10,6,-2,-2,2,9,-8,-1,-4,-6,6,-10,5,3,-10,8,7,-9,-6,-3,6,-4,-5,-9,-1,9,-10,-2,9,-5,-8,-9,10,7,-1,-4,4,-3,5,7,-8,-3,7,5,3,-5,4,7,1,10,4,-1,4,-7,-8,4,3,6,3,6,-1,8,-6,-1,-6,-1,5,-9,5,-7,-8,-9,-8,-1,-6,8,9,-3,10,-3,5,7,3,-2,-9,1,9,2,-5,-10,-1,8,-6,-6,7,3,1,-5,-7,5,5,5,8,-3,2,5,4,5,6,-4,-1,8,-8,-8,-9,1,1,-10,-5,1,10,1,9,4,5,10,-7,-10,1,-10,-3,6,8,4,-3,-1,2,7,-7,-7,-8,-10,7,-2,10,-9,-4,8,5,7,8,10,-1,-9,7,3,-7,2,3,-10,-7,-5,-8,-5,4,10,2,-1,-9,1,8,-3,7,7,-3,-2,-10,1,1,-10,8,6,-3,10,7,8,-7,10,-8,3,-8,2,-1,5,-9,-6,6,-6,1,1,-9,-5,1,10,6,3,-6,9,7,1,8,4,9,3,6,-10,-2,-3,2,-2,-5,-10,9,-2,5,6,-9,9,10,10,5,-3,4,-2,7,5,-1,5,-6,8,-8,-5,5,-9,-6,-1,10,10,9,-2,-7,10,-2,8,2,9,2,-1,8,10,-8,6,4,-1,9,-9,8,6,4,10,-2,10,-1,-1,-10,4,3,-5,8,-9,-9,5,10,9,-5,-2,8,-1,6,9,-2,-5,10,1,7,-5,10,6,-1,-4,6,1,1,-2,-3,-2,-3,-1,6,-1,4,1,-7,-4,4,5,5,5,-10,-10,9,10,-8,4,-7,-8,4,4,6,10,-5,3,10,5,-6,-3,-6,4,-7,9,5,2,-7,-1,-6,5,5,-3,-6,7,5,7,-4,-7,-9,-5,-4,-4,-5,5,5,7,10,8,-10,9,4,7,7,1,10,2,2,8,10,-1,7,-8,-7,4,9,1,7,3,3,10,9,1,8,9,5,7,-7,9,-1,-9,6,6,-9,-9,-3,8,-3,-3,8,-2,-1,3,2,-10,-6,-3,-1,8,-10,-4,10,-4,1,-5,-9,-2,-4,6,8,10,7,8,4,9,5,-8,-7,9,2,-9,-8,1,5,-1,7,8,-7,-3,-2,-7,-8,-3,9,-5,5,2,-4,-7,-4,1,-10,-5,-5,9,1,-6,3,5,1,-3,-3,-10,-9,5,5,-5,7,5,-10,-9,2,-1,-5,7,8,2,4,-10,9,8,-3,3,5,-4,-2,-6,-10,-9,7,3,-5,-9,-9,4,6,5,5,1,-4,4,8,10,9,5,5,-3,4,-1,-3,-2,5,10,5,-7,-6,7,-3,4,-6,9,-8,4,-6,-5,-10,-8,6,4,-1,2,-3,3,-6,7,-7,-7,-9,-7,8,4,2,-2,1,-2,8,-2,-3,-7,4,-2,2,-8,-10,6,8,7,-5,10,6,10,4,-5,7,-5,-7,1,-4,-10,3,-4,7,3,-10,-8,3,-10,-8,-3,8,3,4,-3,-3,5,-9,9,2,-8,4,-1,-1,-5,8,3,5,9,2,-10,-7,4,-7,1,-6,-4,-2,9,-7,-4,4,9,5,-1,-4,-5,7,4,-2,-3,-4,1,3,-3,6,-5,7,2,-4,1,3,8,5,5,-8,8,-9,-10,-8,-3,10,-5,-2,9,9,3,-7,-3,4,2,10,4,6,10,-8,-10,-10,5,3,7,7,-5,2,7,-8,6,8,5,-5,-9,9,1,-6,1,-4,1,-8,-6,-4,4,3,-2,-1,4,-4,-7,4,-2,6,-2,-2,10,9,10,-10,-9,-4,3,-8,1,1,4,-8,6,2,4,2,3,1,-7,8,3,7,-9,-4,6,8,1,-8,2,6,3,-10,-9,10,4,-2,-1,-5,-5,-1,-4,-2,-7,-3,-10,4,7,10,7,-2,7,9,4,-8,-5,-9,-10,-6,-1,7,-8,-7,-5,10,8,-4,-7,-4,-9,9,1,-4,7,7,9,-1,5,1,-6,3,-5,10,-1,3,7,5,10,-9,9,6,10,-4,-5,6,-10,-7,7,6,-2,-8,-3,-6,-2,1,-1,-9,2,7,-2,1,3,6,-5,-7,-5,7,10,2,-8,-5,-8,1,2,7,4,-4,6,-4,4,8,-8,9,8,-2,-2,7,-3,-10,-8,-9,-7,-9,4,-3,-7,-10,-8,5,-8,-2,5,-10,10,5,9,2,6,-8,-7,1,-4,10,-7,7,3,-6,1,-9,6,-8,-8,10,2,-6,-10,2,7,-5,-7,2,4,-10,-5,-5,-5,-5,-5,-8,-4,-7,-3,-10,3,7,-8,1,6,-8,-10,-4,-7,-7,6,3,-2,-6,-1,5,2,3,-10,3,-6,9,-3,9,1,-4,1,-1,-10,-8,-3,-5,7,-6,-2,5,1,2,-6,-4,8,8,-7,-4,5,-8,-7,5,10,-10,-2,10,8,7,-4,-3,-1,4,7,7,-10,-2,7,-10,9,-9,5,-6,3,7,4,-4,10,-5,5,-10,-8,-1,-8,-1,-3,9,2,-8,-9,-6,4,10,-5,-10,-8,5,-3,-10,-9,9,1,-9,5,10,2,-7,-4,-2,-1,-9,-5,4,3,8,-4,4,-4,8,10,-3,4,1,-6,-6,7,7,-2,-7,-6,-6,9,8,5,-5,6,1,8,5,-7,3,8,4,-3,-4,-6,-1,-4,-10,-5,-8,-3,-8,-1,4,-5,1,-7,5,6,10,2,6,-8,-7,-1,5,-3,4,-7,-1,-5,8,-7,-3,2,2,-3,-10,-7,8,-1,4,6,-8,-8,5,-3,-7,-4,1,4,-10,6,-1,-8,-10,2,4,6,10,3,9,-8,6,9,-8,5,-3,9,-1,-5,-9,-9,-4,7,8,9,7,4,-7,-3,9,4,-6,-5,1,9,6,1,2,-4,-9,6,8,7,4,-2,-5,-4,-1,-7,-1,-10,-6,-7,-10,-7,-3,3,4,9,-2,-2,1,-10,-6,-3,-5,4,-6,8,-1,5,9,-7,1,-10,1,2,7,-4,-10,10,10,7,-4,-3,1,10,9,-2,7,3,-5,2,6,-6,1,-2,-9,-8,-5,9,3,5,-9,2,10,-6,2,-8,1,5,-10,-6,3,4,-7,3,2,-1,6,7,-1,-10,2,-1,1,-7,-10,-10,9,2,-6,-7,6,9,5,7,-10,9,6,7,4,6,8,-9,-1,4,-8,4,-3,6,-1,-4,-2,3,2,3,3,-2,-9,-8,3,-8,7,7,-6,-7,-5,-8,-5,5,10,-5,-1,-3,-9,-1,-7,5,10,3,4,1,-5,8,-9,-7,-5,1,3,-4,-7,7,1,-9,6,7,3,9,6,-8,-4,-3,9,-3,-7,5,4,-9,5,-8,-9,-1,2,10,9,4,-3,2,-8,-2,-2,1,10,10,6,-6,-2,7,9,3,-5,3,3,-8,10,8,-1,-7,8,6,-7,1,1,5,-5,-10,-5,-6,8,-9,-8,-10,5,7,7,7,8,-3,-6,-7,-7,3,9,8,5,-4,6,1,-1,5,2,2,-2,6,-5,2,1,-4,5,8,1,5,7,-9,2,8,7,-5,7,8,-6,4,4,-10,9,-10,-1,8,-1,-8,-10,-1,6,-8,7,7,-4,5,-8,-8,-4,-9,-3,4,-5,-9,1,-4,5,-2,-7,8,-1,-9,7,-7,-6,-7,-5,-5,7,7,-5,3,-4,2,5,1,2,-4,-9,-1,7,-6,-3,5,8,-6,-5,-2,-5,10,-4,-5,-3,7,-9,-9,-8,-3,7,-9,-9,5,-3,5,-1,9,8,-4,-4,-4,-9,3,7,6,-1,-6,-9,6,-10,-3,6,8,7,-6,3,4,-3,9,3,2,4,8,-1,-7,-7,-1,2,8,1,8,4,-8,-1,6,4,-1,8,-2,-4,-9,9,6,1,-1,-8,8,3,10,3,-1,4,7,-9,-10,-8,-6,10,10,-5,-6,10,-8,8,-10,-2,7,-10,7,-3,-4,7,-2,1,-10,3,-1,8,9,-5,-8,-7,-4,-1,-8,-1,7,-2,7,-1,10,-5,-10,-10,10,7,4,-2,2,-1,-8,-5,-10,-4,-10,6,-2,1,-3,-2,-8,-8,4,9,3,-8,-2,-4,2,9,-4,2,-3,9,-5,8,9,-6,-6,-10,-6,-8,1,-9,3,-5,-1,4,-3,2,3,1,-6,4,1,10,2,6,-1,8,-2,-2,1,9,-8,-2,-10,4,2,-5,4,2,5,-1,2,-2,-2,7,8,-9,-8,-7,6,4,9,-2,-7,9,2,-10,-9,9,5,-7,6,1,-9,-4,-2,-4,10,-4,-10,-10,-4,9,3,5,5,-4,1,5,-6,4,7,-8,4,3,6,-10,-6,-2,-6,8,2,-10,-7,-3,-4,-8,-7,-8,-10,-6,-6,5,-5,10,7,-3,-10,-3,10,8,3,4,4,-10,3,-9,2,1,-2,-1,9,-9,6,5,-8,-1,3,-10,7,1,7,1,7,-9,4,-9,3,-3,-8,7,3,6,1,-1,7,10,-4,-5,4,-10,-5,5,-7,-7,7,2,9,-4,-5,1,-8,9,-4,5,-10,8,5,3,10,-10,3,-6,1,5,4,-1,-6,6,-5,-8,7,-8,9,-6,-1,-5,10,7,1,9,-7,-10,9,5,-1,6,-10,2,-8,-8,7,-3,7,6,1,5,-6,-5,5,8,4,3,2,3,4,-9,7,7,2,-3,-9,-3,5,1,-7,-5,-4,-2,6,6,-9,2,-7,-1,2,-1,2,7,1,7,-6,-6,-3,-5,-6,-10,6,-2,-8,-1,6,-3,-8,-6,-8,-7,-7,3,3,-10,10,5,-1,10,-1,10,-7,-6,3,5,6,6,-5,5,10,9,7,-10,3,8,3,1,-2,6,-10,-9,-1,10,-7,-3,4,8,6,-10,8,-4,7,-10,6,-6,-6,-3,-1,2,1,4,-7,-7,-8,5,6,-8,7,-3,5,9,8,8,-6,9,6,-3,6,10,-8,2,4,-10,-8,-6,-4,-2,-9,-2,-1,-10,-4,3,-2,6,8,5,-7,-7,-8,8,9,4,2,-1,-7,-3,-4,1,-9,-6,-4,-3,8,8,2,-7,7,9,7,6,10,3,6,-2,10,4,-10,6,6,3,-9,-8,-2,-10,6,-1,3,-4,1,-6,3,6,8,3,-8,-3,-7,-5,-10,7,9,4,-3,3,-4,4,8,5,4,9,4,-8,2,1,-10,-8,6,3,2,-5,2,4,-1,-5,6,-8,-7,-3,-2,1,-3,-1,2,-10,9,-9,-5,2,-3,-3,-2,-1,-7,-7,1,1,8,-2,-7,5,8,-10,8,-10,-10,9,-4,-2,-7,10,-9,-9,-6,-7,5,-10,5,-7,3,-5,-10,4,7,5,-6,-9,9,-10,-10,7,-9,10,8,-9,5,-3,-8,-1,4,8,-2,-5,-4,-5,3,2,10,8,-9,10,-2,-1,1,-7,9,-6,-2,-1,7,-1,-9,-4,4,10,2,-5,4,-5,9,3,-7,8,-2,-6,-6,-3,1,-5,-1,6,4,8,-9,-4,-6,6,-8,5,-5,10,9,8,3,2,-8,-7,-10,-2,-9,9,5,-1,2,-4,-6,-10,-10,-4,4,6,6,4,-2,7,3,7,1,-3,-3,-2,1,-5,-2,3,6,-8,7,-8,-8,-10,-3,1,4,-9,-10,7,4,-4,2,-4,9,1,-4,6,-8,-5,3,6,-9,-6,7,2,-5,10,6,-8,-6,2,9,-1,4,9,1,5,-2,3,-4,3,-3,-9,-8,5,-5,5,-7,-5,2,10,-9,5,8,1,3,5,6,7,10,-10,-1,3,3,10,-1,-1,7,-4,-6,-9,8,6,-8,9], dtype = "uint32")#candidate|18728|(2535,)|const|uint32
call_18727 = func_8163_call(relay.reshape(const_18728.astype('uint32'), [13, 13, 15]))
call_18729 = func_8163_call(relay.reshape(const_18728.astype('uint32'), [13, 13, 15]))
func_10598_call = mod.get_global_var('func_10598')
func_10601_call = mutated_mod.get_global_var('func_10601')
var_18733 = relay.var("var_18733", dtype = "int64", shape = (360,))#candidate|18733|(360,)|var|int64
call_18732 = relay.TupleGetItem(func_10598_call(relay.reshape(var_18733.astype('int64'), [6, 6, 10]), relay.reshape(var_18733.astype('int64'), [6, 6, 10]), ), 1)
call_18734 = relay.TupleGetItem(func_10601_call(relay.reshape(var_18733.astype('int64'), [6, 6, 10]), relay.reshape(var_18733.astype('int64'), [6, 6, 10]), ), 1)
func_17977_call = mod.get_global_var('func_17977')
func_17979_call = mutated_mod.get_global_var('func_17979')
call_18741 = relay.TupleGetItem(func_17977_call(), 0)
call_18742 = relay.TupleGetItem(func_17979_call(), 0)
func_17389_call = mod.get_global_var('func_17389')
func_17391_call = mutated_mod.get_global_var('func_17391')
call_18745 = relay.TupleGetItem(func_17389_call(), 0)
call_18746 = relay.TupleGetItem(func_17391_call(), 0)
func_16861_call = mod.get_global_var('func_16861')
func_16862_call = mutated_mod.get_global_var('func_16862')
call_18749 = relay.TupleGetItem(func_16861_call(), 0)
call_18750 = relay.TupleGetItem(func_16862_call(), 0)
func_14228_call = mod.get_global_var('func_14228')
func_14229_call = mutated_mod.get_global_var('func_14229')
call_18752 = func_14228_call()
call_18753 = func_14228_call()
output = relay.Tuple([call_18708,call_18711,var_18712,call_18714,call_18727,const_18728,call_18732,var_18733,call_18741,call_18745,call_18749,call_18752,])
output2 = relay.Tuple([call_18709,call_18713,var_18712,call_18715,call_18729,const_18728,call_18734,var_18733,call_18742,call_18746,call_18750,call_18753,])
func_18754 = relay.Function([var_18712,var_18733,], output)
mod['func_18754'] = func_18754
mod = relay.transform.InferType()(mod)
mutated_mod['func_18754'] = func_18754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18754_call = mutated_mod.get_global_var('func_18754')
var_18756 = relay.var("var_18756", dtype = "bool", shape = (528,))#candidate|18756|(528,)|var|bool
var_18757 = relay.var("var_18757", dtype = "int64", shape = (360,))#candidate|18757|(360,)|var|int64
call_18755 = func_18754_call(var_18756,var_18757,)
output = call_18755
func_18758 = relay.Function([var_18756,var_18757,], output)
mutated_mod['func_18758'] = func_18758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15508_call = mod.get_global_var('func_15508')
func_15510_call = mutated_mod.get_global_var('func_15510')
call_18774 = relay.TupleGetItem(func_15508_call(), 1)
call_18775 = relay.TupleGetItem(func_15510_call(), 1)
func_3810_call = mod.get_global_var('func_3810')
func_3813_call = mutated_mod.get_global_var('func_3813')
var_18785 = relay.var("var_18785", dtype = "float32", shape = ())#candidate|18785|()|var|float32
var_18786 = relay.var("var_18786", dtype = "float32", shape = (588,))#candidate|18786|(588,)|var|float32
call_18784 = func_3810_call(relay.reshape(var_18785.astype('float32'), []), relay.reshape(var_18786.astype('float32'), [14, 14, 3]), )
call_18787 = func_3810_call(relay.reshape(var_18785.astype('float32'), []), relay.reshape(var_18786.astype('float32'), [14, 14, 3]), )
output = relay.Tuple([call_18774,call_18784,var_18785,var_18786,])
output2 = relay.Tuple([call_18775,call_18787,var_18785,var_18786,])
func_18795 = relay.Function([var_18785,var_18786,], output)
mod['func_18795'] = func_18795
mod = relay.transform.InferType()(mod)
mutated_mod['func_18795'] = func_18795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18795_call = mutated_mod.get_global_var('func_18795')
var_18797 = relay.var("var_18797", dtype = "float32", shape = ())#candidate|18797|()|var|float32
var_18798 = relay.var("var_18798", dtype = "float32", shape = (588,))#candidate|18798|(588,)|var|float32
call_18796 = func_18795_call(var_18797,var_18798,)
output = call_18796
func_18799 = relay.Function([var_18797,var_18798,], output)
mutated_mod['func_18799'] = func_18799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16958_call = mod.get_global_var('func_16958')
func_16959_call = mutated_mod.get_global_var('func_16959')
call_18899 = func_16958_call()
call_18900 = func_16958_call()
output = call_18899
output2 = call_18900
func_18902 = relay.Function([], output)
mod['func_18902'] = func_18902
mod = relay.transform.InferType()(mod)
output = func_18902()
func_18903 = relay.Function([], output)
mutated_mod['func_18903'] = func_18903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15508_call = mod.get_global_var('func_15508')
func_15510_call = mutated_mod.get_global_var('func_15510')
call_18911 = relay.TupleGetItem(func_15508_call(), 1)
call_18912 = relay.TupleGetItem(func_15510_call(), 1)
output = call_18911
output2 = call_18912
func_18913 = relay.Function([], output)
mod['func_18913'] = func_18913
mod = relay.transform.InferType()(mod)
output = func_18913()
func_18914 = relay.Function([], output)
mutated_mod['func_18914'] = func_18914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16550_call = mod.get_global_var('func_16550')
func_16551_call = mutated_mod.get_global_var('func_16551')
call_18980 = relay.TupleGetItem(func_16550_call(), 3)
call_18981 = relay.TupleGetItem(func_16551_call(), 3)
func_16942_call = mod.get_global_var('func_16942')
func_16944_call = mutated_mod.get_global_var('func_16944')
call_18984 = func_16942_call()
call_18985 = func_16942_call()
func_7590_call = mod.get_global_var('func_7590')
func_7593_call = mutated_mod.get_global_var('func_7593')
const_18987 = relay.const([6.241895,5.448615,-7.822502,-7.543394,-0.899384,8.637142,-0.436274,-1.675388,-2.412417,-1.510104,-8.147615,-7.953377,-3.103988,-3.387382,4.007043,-0.878491,-5.501911,-7.403338,-5.375873,-7.447931,-1.857167,1.873946,-3.601495,-6.764764,-1.788868,8.831574,0.931773,-6.675073,-2.782926,-6.116324,-6.452104,-0.562385,-0.488290,0.270678,4.593786,7.002848,-8.750768,-0.072912,1.356120,6.928243,8.679675,-5.714075,0.821500,-6.476550,9.310666,5.720537,-5.580166,-6.530817,-0.528968,6.998394,8.925921,-2.007418,1.892437,2.359901,5.051267,-0.690514,0.675004,-9.556270,2.620032,-2.367578,9.610093,0.772185,7.057919,-7.617659,7.783842,9.032524,-4.460165,-0.118667,-4.384531,-7.666766,5.462099,-9.008435,-1.382148,1.765221,-6.515057,-5.911107,2.529325,5.839407,-3.685446,-1.462800,8.650392,-7.647275,7.021813,6.152099], dtype = "float64")#candidate|18987|(84,)|const|float64
call_18986 = func_7590_call(relay.reshape(const_18987.astype('float64'), [6, 14, 1]))
call_18988 = func_7590_call(relay.reshape(const_18987.astype('float64'), [6, 14, 1]))
func_14253_call = mod.get_global_var('func_14253')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_19002 = relay.TupleGetItem(func_14253_call(), 0)
call_19003 = relay.TupleGetItem(func_14254_call(), 0)
func_16184_call = mod.get_global_var('func_16184')
func_16187_call = mutated_mod.get_global_var('func_16187')
const_19008 = relay.const([True,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True], dtype = "bool")#candidate|19008|(528,)|const|bool
var_19009 = relay.var("var_19009", dtype = "int16", shape = (1404,))#candidate|19009|(1404,)|var|int16
call_19007 = relay.TupleGetItem(func_16184_call(relay.reshape(const_19008.astype('bool'), [528,]), relay.reshape(var_19009.astype('int16'), [1404,]), ), 5)
call_19010 = relay.TupleGetItem(func_16187_call(relay.reshape(const_19008.astype('bool'), [528,]), relay.reshape(var_19009.astype('int16'), [1404,]), ), 5)
output = relay.Tuple([call_18980,call_18984,call_18986,const_18987,call_19002,call_19007,const_19008,var_19009,])
output2 = relay.Tuple([call_18981,call_18985,call_18988,const_18987,call_19003,call_19010,const_19008,var_19009,])
func_19013 = relay.Function([var_19009,], output)
mod['func_19013'] = func_19013
mod = relay.transform.InferType()(mod)
var_19014 = relay.var("var_19014", dtype = "int16", shape = (1404,))#candidate|19014|(1404,)|var|int16
output = func_19013(var_19014)
func_19015 = relay.Function([var_19014], output)
mutated_mod['func_19015'] = func_19015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16942_call = mod.get_global_var('func_16942')
func_16944_call = mutated_mod.get_global_var('func_16944')
call_19062 = func_16942_call()
call_19063 = func_16942_call()
output = call_19062
output2 = call_19063
func_19077 = relay.Function([], output)
mod['func_19077'] = func_19077
mod = relay.transform.InferType()(mod)
mutated_mod['func_19077'] = func_19077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19077_call = mutated_mod.get_global_var('func_19077')
call_19078 = func_19077_call()
output = call_19078
func_19079 = relay.Function([], output)
mutated_mod['func_19079'] = func_19079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15389_call = mod.get_global_var('func_15389')
func_15391_call = mutated_mod.get_global_var('func_15391')
call_19085 = relay.TupleGetItem(func_15389_call(), 0)
call_19086 = relay.TupleGetItem(func_15391_call(), 0)
output = call_19085
output2 = call_19086
func_19096 = relay.Function([], output)
mod['func_19096'] = func_19096
mod = relay.transform.InferType()(mod)
output = func_19096()
func_19097 = relay.Function([], output)
mutated_mod['func_19097'] = func_19097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17977_call = mod.get_global_var('func_17977')
func_17979_call = mutated_mod.get_global_var('func_17979')
call_19109 = relay.TupleGetItem(func_17977_call(), 0)
call_19110 = relay.TupleGetItem(func_17979_call(), 0)
func_15898_call = mod.get_global_var('func_15898')
func_15899_call = mutated_mod.get_global_var('func_15899')
call_19116 = func_15898_call()
call_19117 = func_15898_call()
output = relay.Tuple([call_19109,call_19116,])
output2 = relay.Tuple([call_19110,call_19117,])
func_19118 = relay.Function([], output)
mod['func_19118'] = func_19118
mod = relay.transform.InferType()(mod)
output = func_19118()
func_19119 = relay.Function([], output)
mutated_mod['func_19119'] = func_19119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16840_call = mod.get_global_var('func_16840')
func_16842_call = mutated_mod.get_global_var('func_16842')
call_19132 = func_16840_call()
call_19133 = func_16840_call()
func_16064_call = mod.get_global_var('func_16064')
func_16066_call = mutated_mod.get_global_var('func_16066')
call_19138 = func_16064_call()
call_19139 = func_16064_call()
func_8102_call = mod.get_global_var('func_8102')
func_8105_call = mutated_mod.get_global_var('func_8105')
const_19142 = relay.const([-9,-8,1,-2,-3,1,3,2,-6,-5,1,9,-8,-4,-10,-10,7,-3,-10,-3,9,8,-7,-5,-3,5,8,5,-9,-8,1,-9,9,-1,9,2,7,8,-2,-6,5,-1], dtype = "int64")#candidate|19142|(42,)|const|int64
const_19143 = relay.const([10,9,4,-5,-2,-7,3,-4,-1,-9,-6,-2,-8,-6,-10,6,-7,-8,-7,-6,-9,-10,6,-9,9,-6,9,-9,-6,5,-6,-8,8,-3,-10,3,-1,-4,-1,6,1,4,1,-6,-8,7,-1,-6,2,5,-10,3,-3,8,10,-3,5,8,1,-7,4,-3,-8,6,-8,-3,-9,-10,3,-4,4,-1,-7,9,4,6,-7,-3,-8,6,-1,-8,5,-3,-8,1,-6,-2,-3,10,-6,-5,7,-9,-8,5,-6,-2,-1,-1,-3,2,7,2,-7,-9,-1,8,-4,-5,4,4,2,-2,10,-3,-8,-2,-1,6,9,2,10,9,7,-8,3,2,7,-8,9,-10,6,-1,8,-6,-3,-6,6,-8,-9,-5,-8,8,1,2,9,7,6,4,-7,1,-7,-4,-4,10,-1,-8,2,-6,-3,-2,-2,10,9,4,-2,-8,5,6,6,-5,-10,8,10,-4,-4,-9,-9,6,1,-6,8,4,5,5,7,-10,4,9,-4,8,3,-6,-4,-10,6,-10,9,-8,-5,8,2,8,-8,9,-4,-1,4,-9,2,7,-9,-2,2,-3,-2,10,-10,9,7,-1,-7,-10,-4,1,-2,5,5,10,-7,6,-5,-3,-5,5,10,-5,-2,8,-5,1,-9,-9,-4,-6,3,2,6,-2,-8,5,5,-7,-4,-1,7,-8,-8,5,-7,5,-10,-7,2,7,6,-10,-1,-10,-5,6,4,-8,-3,6,-3,10,-6,10,-6,-8,9,5,-6,-5,-5,10,-6,-4,3,-9,-9,-8,5,2,6,-6,-7,-5,6,-3,2,4,6,-7,6,-5,-4,-9,-2,-2,1,1,9,-3,7,-9,3,-7,1,-10,-9,-1,8,3,3,8,3,3,9,-10,4,-3,3,6,1,1,10,4,4,-10,3,10,-9,-10,7,-5,9,7,-8,-6,-10,-1,-8,8,2,-8,8,-1,-9,7,10,10,-10,1,-2,8,-3,2,-4,5,10,9,1,5,2,7,-4,1,-6,1,-1,-9,8,8,-6,7,6,4,-7,-7,-2,1,1,-9,4,4,9,-10,9,-8,-10,-10,1,4,-4,-7,5,-2,9,5,1,1,-5,6,10,8,7,6,2,7,1,2,-1,-4,6,-6,-9,5,-7,-9,-5,6,-6,1,4,-6,2,-1,-2,3,-4,-3,5,10,-10,-6,-5,8,-7,-1,-5,-6,-5,-9,-3,3,3,-4,-5,-10,-1,-10,1,10,-7,8,8,-10,-2,9,3,-7,-7,5,-5,-7,-5,5,-4,-3,7,-2,9,9,-9,9,10,8,-6,9,10,-8,-2,-1,1,5,9,-5,9,10,-2,-10,4,10,-3,-3,-5,-7,5,3,-4,-6,-6,-9,-6,-3,-7,-1,-4,-3,1,9,-7,3,6,10,4,3,10,5,3,4,-4,1,7,-5,9,4,-2,-10,3,-8,-9,-7], dtype = "int64")#candidate|19143|(546,)|const|int64
call_19141 = relay.TupleGetItem(func_8102_call(relay.reshape(const_19142.astype('int64'), [3, 1, 14]), relay.reshape(const_19143.astype('int64'), [3, 13, 14]), ), 1)
call_19144 = relay.TupleGetItem(func_8105_call(relay.reshape(const_19142.astype('int64'), [3, 1, 14]), relay.reshape(const_19143.astype('int64'), [3, 13, 14]), ), 1)
func_16236_call = mod.get_global_var('func_16236')
func_16238_call = mutated_mod.get_global_var('func_16238')
call_19187 = func_16236_call()
call_19188 = func_16236_call()
output = relay.Tuple([call_19132,call_19138,call_19141,const_19142,const_19143,call_19187,])
output2 = relay.Tuple([call_19133,call_19139,call_19144,const_19142,const_19143,call_19188,])
func_19218 = relay.Function([], output)
mod['func_19218'] = func_19218
mod = relay.transform.InferType()(mod)
output = func_19218()
func_19219 = relay.Function([], output)
mutated_mod['func_19219'] = func_19219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19118_call = mod.get_global_var('func_19118')
func_19119_call = mutated_mod.get_global_var('func_19119')
call_19255 = relay.TupleGetItem(func_19118_call(), 1)
call_19256 = relay.TupleGetItem(func_19119_call(), 1)
func_17861_call = mod.get_global_var('func_17861')
func_17863_call = mutated_mod.get_global_var('func_17863')
const_19267 = relay.const([-9.459198,6.449843,0.964805,4.043687,-9.679025,1.682232,-1.248406,3.665816,4.496657,-9.061927,9.150720,6.435359,8.060039,-0.076565,-2.639329,-1.473066,1.132475,-2.792324,7.089741,3.206949,4.109453,0.412609,-8.207764,-0.116990,2.426640,7.989089,7.888344,-8.445150,-4.479874,0.292318,-3.965067,-8.258811,2.787591,-9.463763,-5.310203,-4.814209,-6.478966,-1.466327,-8.452912,-5.887490,1.213167,-8.918380,-5.014348,0.577703,0.428091,5.868590,5.008759,3.218070,-1.716707,1.049025,-5.123861,-5.896473,7.400652,1.937101,-2.970848,3.929105,-6.210423,-8.563385,-2.360839,2.807408,7.599774,7.101322,-6.986502,5.527215,-8.244752,-0.545951,9.841173,3.596536,6.722492,-9.512191,-0.077597,3.725976,-4.058281,3.103982,-8.467130,-5.551462,-2.425271,-4.629480,6.983627,9.614343,-0.197099,-8.273490,3.379585,-8.241556,-5.893544,-2.390630,-7.609113,7.948659,4.130785,-8.258462,-2.956304,0.416994,-5.759970,2.420067,-6.277217,-8.947483,-4.488600,-2.128639,-4.605946,-1.181147], dtype = "float64")#candidate|19267|(100,)|const|float64
call_19266 = relay.TupleGetItem(func_17861_call(relay.reshape(const_19267.astype('float64'), [100,])), 2)
call_19268 = relay.TupleGetItem(func_17863_call(relay.reshape(const_19267.astype('float64'), [100,])), 2)
func_14486_call = mod.get_global_var('func_14486')
func_14493_call = mutated_mod.get_global_var('func_14493')
var_19294 = relay.var("var_19294", dtype = "float32", shape = (210,))#candidate|19294|(210,)|var|float32
const_19295 = relay.const([-4,-5,-4,-6,5,9,-5,5,5,2,-5,5,-3,7,6,-5,8,-5,6,-7,1,9,2,-3,7,-8,-6,4,-5,3,6,-4,-9,-9,10,-5,4,1,10,-5,-1,7,-6,-7,3,2,1,4,-7,-2,-10,10,-3,-2,-4,9,-9,-3,9,-6,3,10,8,-1,-8,3,-1,4,5,6,4,-7,4,-10,1,3,-5,-5,8,9,-10,-4,5,-7,-3,-2,-10,1,-8,-7,6,2,-5,-6,6,1,-8,-8,-2,-5,-10,3,5,-6,-3,-3,-6,-10,-5,-6,-2,6,-1,-4,1,-1,6,5,-5,6,5,-9,-8,2,7,-4,-6,-10,-7,3,4,3,5,3,8,-2,-3,-3,-9,-4,-4,7,1,8,-4,7,2,-9,-7,-1,-6,-7,-1,9,5,10,2,-1,7,-10,-10,-10,-9,3,5,-1,6,-9,-8,9,-10,5,8,-4,7,7,-2,-4,-8,-7,3,-4,-5,6,-1,-9,5,4,1,-10,3,8,4,8,-10,-7,-2,2,5,-1,4,-1,3,4,-5,-4,10,6,5,8,-9,-10,7,10,-1,-10,2,-6,9,1,-4,4,9,2,4,-3,6,-5,7,-4,-6,-5,-8,-5,5,-2,-3,5,-6,5,-8,2,4,-6,3,-1,-6,9,-9,2,-2,-3,1,-6,6,9,-2,7,-10,-6,2,-4,-4,-6,-9,9,5,8,-3,-4,-8,2,-4,5,-1,-7,-10,1,5,-1,8,-8,3,8,2,4,5,-9,4,-4,-9,-7,-3,-7,8,5,-7,6,2,-3,-7,4,2,2,-9,2,-9,-9,7,-3,1,10,4,7,1,-8,-8,10,-8,-7,-9,5,7,-10,-1,9,2,1,5,-10,9,-7,-2,8,-1,7,5,10,7,4,5,-9,5,3,-7,8,-2,-4,4,-4,-8,-7,-4,-2,-8,-8,-4,-2,-8,-10,-7,-4,5,-3,9,-6,-8,-1,1,-3,4,4,2,-6,8,-7,6,3,-9,-4,4,7,-4,-6,2,4,3,-3,-3,-7,-6,-7,6,-6,6,3,-2,6,1,-1,-1,10,-4,-1,3,-9,2,3,-5,3,1,-5,-8,-8,-3,1,-5,-10,-3,7,10,-7,1,-10,-9,10,-1,-2,4,-10,-1,10,2,-5,2,-3,8,-5,-9,7,-2,-9,-2,1,-1,4,2,7,6,2,-4,10,-6,2,4,3,-6,8,-3,3,-10,7,-1,-9,-6,4,-8,5,3,-9,-7,-2,5,1,9,-4,-1,2,-5,10,1,-3,-10,1,6,-10,-2,-7,2,-7,-4,-9,-1,-10,1,-6,-3,1,7,-7,-4,7,-1,5,4,4,2,-6,4,9,-5,-10,-6,-10,-7,-6,-7,-8,-9,2,6,3,7,3,5,-9,-7,-9,-1,5,-7,8,-8,-2,9,10,8,-5,5,10,-8,-2,-9,-9,9,8,-9,-2,5,3,8,1,-7,2,-2,3,1,-6,-6,3,-3,5,-9,8,-3,-10,-4,-6,5,4,2,7,5,-6,-2,-10,1,-6,4,-4,5,-7,-5,10,5,-7,-3,2,10,1,-8,7,-6,-10,7,7,-10,-10,7,4,6,-1,-6,7,3,-9,8,-2,1,7,10,9,-8,6,1,-9,1,-5,3,6,1,8,-3,4,-6,9,4,-7,-9,10,-5,6,-9,5,-3,7,-6,3,-9,1,-7,3,-10,-6,5,8,4,-6,-5,2,-1,1,-8,-5,1,-4,8,-2,10,-9,3,-5,-3,10,3,7,-3,-9,1,1,2,2,5,-10,3,1,1,3,-8,-4,-4,-5,7,9,-2,2,6,-5,10,-7,7,7,4,3,-2,7,8,-3,7,-5,-2,4,2,10,-5,3,3,-9,1,-2,-9,-8,-2,1,5,-10,-4,-9,-2,-6,-4,-8,-10,-7,-10,-3,10,7,-4,-1,6,-8,-4,7,-5,-4,4,9,2,5,7,-3,1,8,2,-6,3,-1,2,4,10,8,1,-6,-3,4,-8,6,-9,-5,-8,-9,5,-7,-7,4,-10,-1,-8,-3,-9,1,-8,-7,3,-7,-2,-1,8,4,10,3,8,10,-3,7,4,9,6,8,-7,2,5,8,1,9,8,1,7,4,-6,2,-2,1,-9,9,6,-7,5,4,-7,-9,-6,5,-2,5,-1,-10,-10,-10,2,6,1,10,-1,5,-9,3,5,-3,6,-8,7,-9,-1,-7,-8,-2,8,-6,6,7,8,-3,9,-1,-3,3,9,8,-10,-4,10,9,9,7,9,-3,3,9,1,6,-10,-6,10,8,3,-8,9,-10,-5,4,-10,-2,-2,-6,2,10,8,1,-2,-8,3,7,-7,10,6,7,-2,3,-9,-8,-9,-3,4,7,-4,-10,-2,1,-6,3,-7,-1,7,-1,-1,7,7,8,-3,7,9,4,-6,3,6,-7,-6,9,10,-10,-1,10,-9,1,-3,-1,8,6,-10,8,-6,-10,3,4,1,4,-2,-2,-1,5,1,-6,1,5,-2,-9,9,-9,-1,4,10,6,2,-5,2,9,-3,-4,-9,-8,-3,-9,8,-3,-2,1,-6,-4,-8,1,8,-3,5,7,-6,4,4,2,-3,1,3,-7,-10,5,-9,-7,-8,-8,-8,6,-10,5,-6,-5,3,4,9,-5,2,6,8,-8,4,9,1,-9,-10,6,-3,-4,-7,2,-10,7,-7,-3,6,1,-7,5,-8,10,3,3,-7,4,-7,-1,3,9,1,-7,5,-1,8,2,-2,-5,8,-1,-7,10,1,-3,9,4,-5,-7,9,-3,-3,7,9,10,-10,-4,-6,-4,-6,-1,8,5,6,-6,-9,6,-5,-9,2,4,10,2,-4,3,3,7,9,7,-3,4,3,5,-10,-6,4,8,-10,10,-9,6,-8,5,4,-5,-6,-2,-9,-1,-3,-5,7,-1,-6,-10,7,-6,10,2,-3,4,8,-8,-3,5,-6,-5,4,9,-8,-4,9,-9,9,-5,-10,10,5,2,9,-5,10,9,5,-3,-10,-9,-6,8,-2,6,3,8,7,7,-1,-2,-2,4,-10,-2,5,9,-2,7,-1,-5,-10,-4,7,5,-4,9,-10,5,4,-10,1,-2,-6,6,-3,-4,8,-2,-9,-4,-3,-1,10,3,-3,4,-2,-6,7,-8,5,-3,-1,-9,-1,-5,6,9,4,-9,-5,-1,-1,-7,-9,7,6,8,-5,10,-9,-2,3,-2,-5,3,6,-9,1,3,1,-5,-2,-4,1,2,-9,7,-8,-10,-10,5,9,2,9,9,7,-7,-8,-5,5,10,-4,9,-8,4,-3,3,-4,1,2,3,5,-8,1,3,3,-1,2,8,10,-7,3,-5,7,-10,8,-8,-3,8,-4,-9,6,-3,-3,-8,4,-6,-5,4,6,1,-7,-7,-9,-4,7,9,7,-2,4,-3,-5,-7,-7,2,-7,7,4,-6,-10,6,-8,-1,-9,-5,-4,1,-7,-2,1,10,-9,-4,3,-7,-2,2,-8,-3,7,9,-8,3,-1,8,10,-2,6,-1,-5,2,1,-7,9,5,-10,9,7,3,-8,-9,-10,-7,-6,5,-5,3,3,5,2,7,-6,-1,-10,-10,5,7,2,-2,-2,-4,-4,-3,6,6,-9,1,-9,10,-5,10,-4,7,-10,-8,4,9,8,-2,1,-2,2,10,6,-3,-2,4,1,-6,8,5,-6,7,-8,8,-8,-2,6,4,-3,4,1,3,-9,2], dtype = "int16")#candidate|19295|(1404,)|const|int16
const_19296 = relay.const([-7,-2,10,-5,1,-3,-6,6,2,6,-5,3,-8,9,10,-9,-8,3,-3,8,-4,7,-9,-9,-2,-6,5,-7,4,4,5,-10,6,-2,-4,3,3,-7,4,-3,4,-5,1,-1,-7,8,8,-6,-3,-3,3,4,-7,8,8,10,-1,10,-7,6,6,8,3,-10,4,-5,1,-3,-10,-4,2,-2,-8,-6,1,-1,-7,-3,-4,-1,6,5,5,8,1,-6,5,-8,10,2,-8,-10,-1,-9,6,5,-6,-1,-10,-8,10,-4,4,10,7,-7,4,-2,-10,3,-1,-8,-9,-7,10,2,1,-7,-9,9,10,1,-3,10,-3,9,-1,10,8,9,-5,7,6,-9,10,10,-5,-3,-5,-2,-6,-2,-2,7,2,-7,8,10,-8,10,10,8,-3,2,6,6,-8,10,-3,-9,4,1,-10,7,-4,7,-7,7,-6,5,6,-5,-10,-2,4,7,7,-10,-8,4,4,-4,-6,10,-4,5,6,2,-5,-8,-6,-6,10,-8,5,-2,3,3,-9,-1,-7,10,-8,-3,7,-1,6,-5,-5,7,-7,2,-7,9,-7,-8,1,-2,-2,-2,-4,-5,-2,9,3,1,6,-2,-8,8,3,2,6,3,-6,-1,7,3,6,9,9,-1,-3,6,4,-9,-2,3,4,7,8,-2,-6,6,-10,-1,-5,2,5,-1,3,-6,-8,2,4,2,9,-8,-3,-7,9,2,10,4,-3,4,3,-1,-8,5,-4,5,2,-8,-8,-10,5,-3,-5,2,-9,5,8,-5,1,-10,6,8,-9,-7,-3,5,6,-7,-2,8,-7,3,9,10,7,-4,-5,5,1,2,8,4,-5,4,1,-9,6,-2,2,-6,-3,-4,-3,4,-10,7,-4,-3,-3,-6,-10,3,-7,-5,-6,-7,-1,9,1,-9,-10,10,-9,-2,-9,-9,3,9,6,8,4,2,10,3,-5,-4,-9,8,9,-2,-10,9,4,3,1,1,1,-3,5,2,-8,-4,3,7,-3,10,2,9,7,-6,-5,6,-10,-5,-4,-4,5,9,9,-10,5,-10,-9,-4,10,7,-7,-1,1,-2,5,7,-4,-8,10,-9,-7,-3,7,5,5,3,6,-9,-10,-1,-8,6,3,-7,1,-10,-5,7,10,9,5,-9,8,7,2,-4,4,-2,-6,-2,7,7,6,-5,-5,4,-8,2,-5,-3,-7,-7,9,-10,10,-9,-3,-10,10,5,-10,9,4,-4,-2,-5,-4,-2,2,7,3,9,-4,-6,2,2,-4,2,4,-6,2,5,-2,10,-8,-7,3,-10,-5,-1,-2,1,-8,4,8,8,3,-8,2,-10,5,3,1,4,2,5,2,1,-10,2,7,7,-5,5,-3,8,-10,5,-6,1,6,-3,-3,-8,9,10,2,-4,-2,-2,5,2,-1,-9,8,5,6,-4,-2,2,4,5,-9,3], dtype = "int64")#candidate|19296|(546,)|const|int64
const_19297 = relay.const([[-2.821341,4.202730,-1.954580,-7.998570,4.970106,6.940948,-0.661505,-6.997194,-7.637549,-2.765560,-8.148822,2.755795,9.431000,7.097774,-7.386897,1.620714,-4.295680,4.212630,-3.352696,-1.256795,2.039081,-0.069752,3.699812,8.223349,0.272960,-5.312979,0.894403,0.585165,6.327588,0.058162,-6.719533,-2.209931,2.353332,7.462087,8.562436,3.146275,-1.330593,-2.477349,-1.523333,0.935087,5.590143,-9.344341,7.314100,-9.923983,-0.575901,0.541059,-3.217487,8.387716,6.101514,0.253178,1.994858,9.303645,-0.150278,1.588159,-6.981376,-0.221154,-4.539438,-3.647015,-5.450467,-6.692738,-1.354016,-6.869948,5.522254,-3.475616,-7.334776,3.510471,-5.475730,4.807394,-0.892434,-2.778490,-1.153198,8.112536,4.613855,-8.760230,-6.642282,-2.937216,-8.180203,5.660925,-1.986905,5.795789,5.793296,-1.879087,5.072127,-4.854640,-4.863434,-0.862132,-3.671309,-9.104914,-4.058596,7.796653,0.068935,3.568117,-1.184954,-1.403639,2.541861,-8.652211,-6.179833,-9.909509,-1.864086,-9.458519,2.577108,7.017029,-4.150958,9.035697,3.424368,1.193326,-4.002964,-4.322145,9.210776,-0.014648,-8.658241,2.310538,2.076778,8.042834,-2.779535,0.517766,-6.106737,1.919822,-4.637457,9.314968,-1.350273,-4.327039,-0.107273,0.670520,6.049169,-4.437763,-9.089665,0.347018,3.895225,-2.155848,-6.421105,-7.854219,-3.693460,4.591867,-3.205139,-2.055504,1.506439,-3.934570,-6.680659,1.218465,8.050724,6.543992,7.189626,0.919172,2.485770,-5.418538,4.536158,0.648624,4.829675,-1.268845,8.105314,-2.269642,-0.617530,-4.911847,-8.494681,-3.201036,7.035766,-2.715109,-2.248050,-3.545180,4.717203,7.290785,3.695668,-5.149031,2.110101,-1.758995,-0.345291,2.346561,0.160444,7.335114,3.667093,0.740306,2.894656,3.944128,-3.929432,-9.935438,8.993229,-1.341511,-1.503154,1.162150,-4.265685,-6.625279,-1.670016,4.023828,-3.721355,1.597692,-1.125254,-1.052791,-6.811735,-6.090954,3.902993,-3.194505,-4.277578,2.582342,-4.160475,6.934597,2.899960,7.570991,1.263723,3.914694,8.072822,-2.467949,-2.709444,0.561765,-3.663001,8.580667,-6.745226,-0.611357,-7.776830,8.857132,-8.048752,7.563278,0.555640,4.057531,4.798210,-8.908424,-6.041044,7.467624,2.301113,7.640452,-2.550338,-5.385790,9.246474,1.497353,-0.656317,-0.427495,5.424591,-1.716379,-6.503285,-0.817720,9.074164,-2.006806,1.314902,-0.573124,-2.803858,-1.011293,-8.740879,-3.309811,-5.417454,5.988274,-3.140858,3.295382,-0.770609,-0.480378,-6.326682,-6.316658,3.149656,0.131071,-5.303893,-4.704753,6.274162,9.056515,5.805048,3.104454,-4.712037,-9.725254,-4.190287,-5.890539,-8.373214,7.200368,4.040792,-9.523411,-2.323760,0.809227,1.521197,-2.683092,0.155720,-3.599163,2.750169,-6.288482,-5.190508,-2.474269,-8.275327,8.110054,-1.700056,2.142201,9.986482,-6.794723,9.981616,-2.973642,8.951489,-9.559897,1.502927,8.237897,-6.938633,-7.422401,9.944513,-6.980045,4.584748,-9.566389,-8.291013,-5.740732,8.686837,-0.679711,-5.398063,2.790019,9.796333,-2.817624,-7.421802,4.134484,6.435483,3.945442,-3.920296,7.706657,-3.653076,3.304816,6.983314,-6.410943,9.965560,-8.338612,1.798375,0.366692,8.819186,3.459352,-6.482609,-8.335414,-6.053237,-8.416302,2.770014,8.990008,1.208895,4.506874,-1.614180,7.755645,-9.620846,6.110022,1.064247,-5.268586,6.120266,-7.993071,-8.327768,7.384975,-8.571036,3.396165,6.659200,3.727813,-6.374986,-8.066265,-6.778518,-1.179503,8.606047,9.106546,-8.721685,7.454068,9.599887,9.901625,-8.184487,7.450170,-4.705311,8.004286,4.380314,-9.734003,2.670448,-0.553246,-6.974432,-0.662672,-6.116934,-4.647090,7.474119,-4.566139,4.915726,-3.010378,2.106250,4.354749]], dtype = "float64")#candidate|19297|(1, 364)|const|float64
var_19298 = relay.var("var_19298", dtype = "uint32", shape = (420,))#candidate|19298|(420,)|var|uint32
call_19293 = relay.TupleGetItem(func_14486_call(relay.reshape(var_19294.astype('float32'), [210,]), relay.reshape(const_19295.astype('int16'), [1404,]), relay.reshape(const_19296.astype('int64'), [546,]), relay.reshape(const_19297.astype('float64'), [364,]), relay.reshape(var_19298.astype('uint32'), [420,]), ), 4)
call_19299 = relay.TupleGetItem(func_14493_call(relay.reshape(var_19294.astype('float32'), [210,]), relay.reshape(const_19295.astype('int16'), [1404,]), relay.reshape(const_19296.astype('int64'), [546,]), relay.reshape(const_19297.astype('float64'), [364,]), relay.reshape(var_19298.astype('uint32'), [420,]), ), 4)
output = relay.Tuple([call_19255,call_19266,const_19267,call_19293,var_19294,const_19295,const_19296,const_19297,var_19298,])
output2 = relay.Tuple([call_19256,call_19268,const_19267,call_19299,var_19294,const_19295,const_19296,const_19297,var_19298,])
func_19301 = relay.Function([var_19294,var_19298,], output)
mod['func_19301'] = func_19301
mod = relay.transform.InferType()(mod)
var_19302 = relay.var("var_19302", dtype = "float32", shape = (210,))#candidate|19302|(210,)|var|float32
var_19303 = relay.var("var_19303", dtype = "uint32", shape = (420,))#candidate|19303|(420,)|var|uint32
output = func_19301(var_19302,var_19303,)
func_19304 = relay.Function([var_19302,var_19303,], output)
mutated_mod['func_19304'] = func_19304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18325_call = mod.get_global_var('func_18325')
func_18327_call = mutated_mod.get_global_var('func_18327')
call_19309 = relay.TupleGetItem(func_18325_call(), 0)
call_19310 = relay.TupleGetItem(func_18327_call(), 0)
output = call_19309
output2 = call_19310
func_19319 = relay.Function([], output)
mod['func_19319'] = func_19319
mod = relay.transform.InferType()(mod)
output = func_19319()
func_19320 = relay.Function([], output)
mutated_mod['func_19320'] = func_19320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14611_call = mod.get_global_var('func_14611')
func_14613_call = mutated_mod.get_global_var('func_14613')
call_19335 = relay.TupleGetItem(func_14611_call(), 0)
call_19336 = relay.TupleGetItem(func_14613_call(), 0)
func_18089_call = mod.get_global_var('func_18089')
func_18091_call = mutated_mod.get_global_var('func_18091')
call_19341 = func_18089_call()
call_19342 = func_18089_call()
func_4187_call = mod.get_global_var('func_4187')
func_4189_call = mutated_mod.get_global_var('func_4189')
var_19351 = relay.var("var_19351", dtype = "float64", shape = (100,))#candidate|19351|(100,)|var|float64
call_19350 = relay.TupleGetItem(func_4187_call(relay.reshape(var_19351.astype('float64'), [5, 2, 10])), 1)
call_19352 = relay.TupleGetItem(func_4189_call(relay.reshape(var_19351.astype('float64'), [5, 2, 10])), 1)
func_10598_call = mod.get_global_var('func_10598')
func_10601_call = mutated_mod.get_global_var('func_10601')
var_19354 = relay.var("var_19354", dtype = "int64", shape = (360,))#candidate|19354|(360,)|var|int64
call_19353 = relay.TupleGetItem(func_10598_call(relay.reshape(var_19354.astype('int64'), [6, 6, 10]), relay.reshape(var_19354.astype('int64'), [6, 6, 10]), ), 2)
call_19355 = relay.TupleGetItem(func_10601_call(relay.reshape(var_19354.astype('int64'), [6, 6, 10]), relay.reshape(var_19354.astype('int64'), [6, 6, 10]), ), 2)
func_16942_call = mod.get_global_var('func_16942')
func_16944_call = mutated_mod.get_global_var('func_16944')
call_19361 = func_16942_call()
call_19362 = func_16942_call()
func_18658_call = mod.get_global_var('func_18658')
func_18662_call = mutated_mod.get_global_var('func_18662')
const_19364 = relay.const([-7,-6,9,-4,8,-2,1,-10,5,-9,-2,-9,-1,-10,-3,6,1,2,5,10,3,-4,-2,-9,-4,9,7,9,-2,-5,-2,-5,-5,3,-5,5,7,-2,6,5,2,-8,-3,8,-5,-10,-8,-10,-6,-4,7,8,-9,-2,-4,6,2,6,10,3,-9,-2,10,1,-4,6,2,-3,8,7,2,-9,-7,2,-9,5,-9,-6,-7,-6,9,2,8,4,3,-10,-7,1,-2,-3,7,-10,3,7,10,-2,-5,-10,-4,-1,-8,-1,-9,-8,7,-3,-9,3,8,3,3,-9,-4,5,5,-2,-8,9,7,-10,1,9,8,-4,-1,-8,-6,7,6,-5,-8,4,-4,-3,2,-5,1,-3,-7,-7,5,7,2,1,-5,-9,-7,-9,7,2,-9,4,-5,9,5,-2,-3,4,-2,3,3,-10,-6,3,-3,5,-4,-10,-6,-10,-4,3,-1,3,4,-9,-8,9,-8,-9,7,-10,3,-7,8,-1,-10,-2,-1,-4,-10,2,-2,4,-1,-10,7,9,-2,10,-6,4,5,-6,-10,-9,-3,-10,2,-4,7,3,-6,5,-9,-7,5,-10,9,7,4,2,9,-2,-4,-5,-2,6,-1,3,-7,4,4,-2,-7,4,7,3,-6,8,-3,2,3,3,-10,-5,-9,-10,-10,9,3,3,7,-7,-10,4,10,-9,7,-9,10,-5,3,-5,-2,-2,-8,-7,10,-10,1,-4,-2,-5,8,-8,-8,-9,-10,3,1,-7,10,-3,-9,3,-9,-10,3,-1,-9,-9,-2,7,-7,4,-6,6,-6,-8,-6,-5,-7,5,10,1,5,-8,10,-10,4,4,6,7,3,-7,6,1,8,-3,3,2,6,6,-3,-3,-10,-10,1,8,-3,-2,-10,-4,10,-1,-3,-3,-2,5,5,6,-6,-4,4,-10,9,-5,4,9,7,9,2,-9,10,2,1,-5,-2,4,10,-2,4,10,-7,2,-1,-3,2,7,-3,9,5,-1,-2,-3,-6,3], dtype = "uint64")#candidate|19364|(378,)|const|uint64
call_19363 = relay.TupleGetItem(func_18658_call(relay.reshape(const_19364.astype('uint64'), [3, 9, 14]), relay.reshape(const_19364.astype('uint64'), [3, 9, 14]), ), 3)
call_19365 = relay.TupleGetItem(func_18662_call(relay.reshape(const_19364.astype('uint64'), [3, 9, 14]), relay.reshape(const_19364.astype('uint64'), [3, 9, 14]), ), 3)
output = relay.Tuple([call_19335,call_19341,call_19350,var_19351,call_19353,var_19354,call_19361,call_19363,const_19364,])
output2 = relay.Tuple([call_19336,call_19342,call_19352,var_19351,call_19355,var_19354,call_19362,call_19365,const_19364,])
func_19367 = relay.Function([var_19351,var_19354,], output)
mod['func_19367'] = func_19367
mod = relay.transform.InferType()(mod)
var_19368 = relay.var("var_19368", dtype = "float64", shape = (100,))#candidate|19368|(100,)|var|float64
var_19369 = relay.var("var_19369", dtype = "int64", shape = (360,))#candidate|19369|(360,)|var|int64
output = func_19367(var_19368,var_19369,)
func_19370 = relay.Function([var_19368,var_19369,], output)
mutated_mod['func_19370'] = func_19370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17748_call = mod.get_global_var('func_17748')
func_17750_call = mutated_mod.get_global_var('func_17750')
call_19372 = func_17748_call()
call_19373 = func_17748_call()
func_14973_call = mod.get_global_var('func_14973')
func_14975_call = mutated_mod.get_global_var('func_14975')
var_19386 = relay.var("var_19386", dtype = "bool", shape = (528,))#candidate|19386|(528,)|var|bool
call_19385 = relay.TupleGetItem(func_14973_call(relay.reshape(var_19386.astype('bool'), [24, 22])), 2)
call_19387 = relay.TupleGetItem(func_14975_call(relay.reshape(var_19386.astype('bool'), [24, 22])), 2)
func_6258_call = mod.get_global_var('func_6258')
func_6262_call = mutated_mod.get_global_var('func_6262')
const_19399 = relay.const([[2],[-3],[-5],[10],[-7],[6],[5],[5],[-2],[-1],[-7],[2],[-6],[8],[8],[-6],[-9],[-9],[-4],[-2],[2],[-6],[-9],[-1],[2],[-3],[-2],[1],[-10],[3],[2],[-8],[-8],[7],[10],[2],[-9],[-10],[-3],[-1],[-3],[-6],[-1],[-5],[5],[-9],[-7],[9],[-6],[9],[8],[-9],[-2],[-7],[-10],[-10],[3],[9],[2],[-7],[4],[-3],[4],[8],[10],[5],[1],[-5],[3],[-9],[-10],[-7],[6],[9],[10],[4],[-3],[-6],[-1],[-7],[4],[-9],[8],[-9],[7],[3],[9],[-2],[-5],[-5],[-8],[-10],[-6],[-8],[-1],[-7],[8],[9],[9],[-8],[-7],[6],[2],[3],[9],[-4],[-6],[8],[9],[8],[10],[4],[-9],[-6],[10],[-9],[-5],[-3],[2],[-4],[-3],[-8],[3],[9],[-9],[-1],[-2],[6],[7],[-4],[-6],[-1],[5],[-9],[9],[8],[2],[-9],[9],[8],[-8],[-8],[3],[4],[8],[6],[-8],[-6],[-1],[1],[-8],[2],[-6],[-6],[2],[4],[4],[-10],[6],[8],[1],[-9],[-1],[3],[-9],[1],[-7],[9],[7],[-8],[-1],[1],[-6],[2],[-5],[7],[4],[-5],[10],[4],[4],[7],[2],[5],[-3],[-10],[-9],[10],[10],[-7],[-4],[-10],[-2],[-1],[5],[-10],[-5],[-2],[-2],[8],[-2],[-10],[7],[-4],[3],[1],[10],[6],[-10],[-2],[4],[-6],[8],[-8],[5],[-6],[2],[5],[7],[6]], dtype = "uint32")#candidate|19399|(220, 1)|const|uint32
const_19400 = relay.const(1.776656, dtype = "float32")#candidate|19400|()|const|float32
const_19401 = relay.const([4.529775,-6.730180,-1.055147,-0.435452,-4.633751,-5.427363,-7.407678,2.974392,-2.948218,5.354032,0.812494,-9.826443,3.181160,-0.964174,3.858339,7.248619,-5.970983,-2.273279,-9.480100,-9.799005,-6.950038,5.240037,-0.087187,-1.557517,5.092162,9.328810,-4.299801,2.638003,9.140963,0.239787,-1.445071,7.965597,-6.503405,6.164088,8.873836,0.731408,-3.696221,-3.800621,-5.064005,-6.348986,-6.939084,-9.065101,4.420475,-2.209748,8.278958,9.313587,5.255617,-5.744639,-1.520822,-1.212627,8.114441,1.825612,-9.280540,-1.401284,-9.762856,-4.467528,7.672600,8.770133,-9.154949,0.485017,8.810634,0.816835,-6.883970,9.900203,-5.002769,-4.026755,0.447345,5.616165,7.728633,-2.333154,-0.646872,-0.744885,1.804689,-9.879568,9.382843,9.906174,-8.556273,2.707522,1.819514,9.891048,4.919106,5.012877,0.665681,-6.416451,6.538443,-9.000741,-8.960256,7.905849,8.899845,4.016522,5.566191,7.231901,-3.347164,-6.836319,8.760355,0.103604,7.060688,-2.306104,6.035044,7.962840,0.469281,8.514464,-9.485289,-1.561018,-8.440508,4.843178,-4.495720,-2.283325,7.670012,-5.028292,-2.491424,2.915381,0.419063,4.302579,9.809141,0.213715,-3.723890,-0.135907,7.123520,-7.156354,-8.923400,7.879488,9.365893,4.907175,7.160038,9.296830,9.797422,5.733954,-0.182365,-7.364225,-7.316638,8.316294,-5.580240,0.896008,-9.410900,5.425936,0.753408,8.706556,-9.051141,-4.873599,8.339394,-8.814040,-8.977219,6.319158,-4.029903,-9.698044,9.326500,8.579290,2.125167,7.991879,5.980298,4.245853,3.937394,2.147001,9.800652,7.688433,8.862997,-8.366558,-9.497227,3.616997,2.090273,2.349470,0.020659,-0.990305,3.762876,-8.162091,-2.868704,-6.199417,-7.124512,-6.771983,8.154665,-3.083598,1.619827,-2.397052,-5.937814,-4.820289,-6.155254,-7.087377,-4.321624,-1.601169,-5.894790,-0.978189,-0.551806,9.808310,-3.106892,8.684010,8.735894,9.826787,-0.127833,-2.243988,7.913957,-0.885939,-6.390377,8.437569,8.606484,4.762709,-3.479212,-8.895810,-3.086834,8.942497,3.391964,-1.806223,6.568119,9.208004,8.237588,-7.010515,-2.647056,-8.378377,-8.751138,-1.458602,-7.795819,8.711009,7.408794,5.603797,5.975755,4.705828,0.052435,-8.825366,6.372809,-8.559742,4.151739,8.230796,5.265811,9.373230,8.330392,5.681451,5.157725,-9.827312,6.025751,-4.071334,-8.668384,5.817031,0.315991,-1.166199,-3.910498,4.671043,-5.733064,0.643191,3.461929,0.163674,-9.340892,-4.240655,8.150087,6.150591,-0.759032,-1.817060,1.598946,5.312816,9.712536,5.437732,-5.096952,8.095034,0.121817,5.973603,0.730890,5.862802,5.890725,6.227445,-0.857423,0.127828,-6.358584,8.393260,-7.877546,-6.701568,2.171586,9.736167,8.363132,-1.925069,6.849050,9.830332,-1.079573,2.549197,-4.768367,-1.649344,9.447056,2.878764,6.177483,4.471176,2.478864,0.276324,8.960353,9.198258,-8.403227,4.661370,3.254377,-5.418267,3.899236,1.493989,4.952726,-0.092301,-8.455244,-2.176090,-3.324869,5.533603,-5.030938,-3.497804,2.005795,-8.484616,3.181646,9.085116,-0.901086,-8.868090,9.119798,7.434664,-0.888139,5.647375,5.695911,-4.400888,8.496646,-1.731457,1.072537,7.203270,-0.394767,-5.309457,0.362308,-0.129927,7.597720,8.229841,-0.367397,4.282377,-6.606409,6.228697,5.639284,-9.800327,5.719415,-9.337706,8.947848,5.057587,9.747255,-4.880030,-2.620640,-0.203270,0.032252,-2.556450,-5.628532,-1.174923,2.240608,-3.609598,-6.302989,3.743720,7.143794,-9.741845,-0.913654,-1.831341,1.544505,-9.955423,1.677148,3.439659,9.669648,2.412015,-9.362030,-2.835367,3.326343,-7.676721,1.462541,-6.089018,0.391535,-4.565383,-0.309466,5.555377,1.867454,8.498108,-6.300414,1.601256,0.200317,3.402111,1.514103,9.326606,-7.804068,-4.570233,7.482595,6.433808,0.479037,-8.093807,-3.445001,8.749610,-3.527026,9.045865,9.590796,-6.405830,2.209617,-2.864739,2.353570,4.877275,8.221337,-5.479117,-9.547425,7.109820,4.724885,-2.015438,8.047033,4.488655,-1.608622,-0.580728,9.040541,-3.007214,-2.957168,5.553922,-5.264009,-4.653933,-3.560587,5.301876,-9.766192,-2.312345,-4.045856,1.545531,-5.170902,9.976485,0.608203,9.591632,-7.840500,3.416659,-2.940029,0.635546,-3.045095,7.160441,-8.670870,4.794717,9.049809,-5.827951,-9.542344,-9.100426,-0.240585,-5.836319,6.577799,-8.260913,5.744962,8.863820,7.467620,7.582694,-7.454288,-1.392020,9.930589,3.454649,-2.260169,-6.940642,4.234822,7.142452,3.737221,-9.948657,0.724441,-7.509294,-8.812600,9.114293,-3.823123,7.427112,6.547934,6.570603,-0.434744,7.075115,-9.063534,0.703984,-1.290448,8.153127,-1.206080,9.911713,3.233297,1.690003,2.572611,9.912790,6.524493,-2.904825,-9.255252,8.365857,-7.425331,6.274482,-6.018476,-3.761540,-2.401822,-8.658853,2.920159,-7.648652,-5.783273,4.586986,-6.080854,9.384686,4.512501,-6.579897,-3.787466,-9.890350,9.106351,2.225403,4.410000,-5.409121,-8.940571,-2.546709,-4.101437,-4.519349,-0.850020,-5.545419,-3.069709,-6.408756,9.470831,0.675383,-0.390000,-2.615862,-6.280416,-1.269276,-5.421168,4.229903,2.931096,-0.009580,-2.000236,-4.340067,-7.225040,-1.584728,3.201018,3.972584,1.787710,-8.188545,-1.051152,8.117818,-9.255087,-2.113530,4.280906,7.497986,-2.526354,-8.529081,-9.821304,4.710432,-8.871368,9.682304,1.430585,-5.647509,-0.540753,-4.038490,-5.116499,9.315569,9.170691,4.046378,6.008336,-0.470898,-4.940962,-9.085751,2.274188,-0.586781,5.953599,0.022320,-8.545132,-5.140273,-2.919657,9.866036,-2.038537,-1.726169,3.616890,-1.705795,-3.948036,-9.846601,-4.822301,-9.453509,-7.038647,8.364680,-9.454720,-1.008214,-0.409814,3.949678,-9.047516,9.793349,2.065058,-5.164732,3.218919,8.290613,9.280025,8.086439,2.311967,-3.434394,-3.682862,0.080210,-7.665507,7.590042,-8.714612,-3.851802,9.866107,-7.651469,4.242125,9.087917,5.641489,-4.122245,-3.031328,-4.701343,7.575461,-2.555254,-3.013395,7.467595,3.490898,-5.333491,1.608545,-2.396250], dtype = "float32")#candidate|19401|(588,)|const|float32
call_19398 = relay.TupleGetItem(func_6258_call(relay.reshape(const_19399.astype('uint32'), [11, 10, 2]), relay.reshape(const_19400.astype('float32'), []), relay.reshape(const_19401.astype('float32'), [588,]), ), 1)
call_19402 = relay.TupleGetItem(func_6262_call(relay.reshape(const_19399.astype('uint32'), [11, 10, 2]), relay.reshape(const_19400.astype('float32'), []), relay.reshape(const_19401.astype('float32'), [588,]), ), 1)
output = relay.Tuple([call_19372,call_19385,var_19386,call_19398,const_19399,const_19400,const_19401,])
output2 = relay.Tuple([call_19373,call_19387,var_19386,call_19402,const_19399,const_19400,const_19401,])
func_19406 = relay.Function([var_19386,], output)
mod['func_19406'] = func_19406
mod = relay.transform.InferType()(mod)
mutated_mod['func_19406'] = func_19406
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19407 = relay.var("var_19407", dtype = "bool", shape = (528,))#candidate|19407|(528,)|var|bool
func_19406_call = mutated_mod.get_global_var('func_19406')
call_19408 = func_19406_call(var_19407)
output = call_19408
func_19409 = relay.Function([var_19407], output)
mutated_mod['func_19409'] = func_19409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17507_call = mod.get_global_var('func_17507')
func_17508_call = mutated_mod.get_global_var('func_17508')
call_19411 = relay.TupleGetItem(func_17507_call(), 1)
call_19412 = relay.TupleGetItem(func_17508_call(), 1)
output = call_19411
output2 = call_19412
func_19479 = relay.Function([], output)
mod['func_19479'] = func_19479
mod = relay.transform.InferType()(mod)
output = func_19479()
func_19480 = relay.Function([], output)
mutated_mod['func_19480'] = func_19480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16461_call = mod.get_global_var('func_16461')
func_16462_call = mutated_mod.get_global_var('func_16462')
call_19512 = func_16461_call()
call_19513 = func_16461_call()
uop_19523 = relay.log2(call_19512.astype('float64')) # shape=(13, 3, 15)
uop_19525 = relay.log2(call_19513.astype('float64')) # shape=(13, 3, 15)
output = relay.Tuple([uop_19523,])
output2 = relay.Tuple([uop_19525,])
func_19526 = relay.Function([], output)
mod['func_19526'] = func_19526
mod = relay.transform.InferType()(mod)
mutated_mod['func_19526'] = func_19526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19526_call = mutated_mod.get_global_var('func_19526')
call_19527 = func_19526_call()
output = call_19527
func_19528 = relay.Function([], output)
mutated_mod['func_19528'] = func_19528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_19585 = relay.TupleGetItem(func_15484_call(), 1)
call_19586 = relay.TupleGetItem(func_15485_call(), 1)
func_17748_call = mod.get_global_var('func_17748')
func_17750_call = mutated_mod.get_global_var('func_17750')
call_19607 = func_17748_call()
call_19608 = func_17748_call()
func_16461_call = mod.get_global_var('func_16461')
func_16462_call = mutated_mod.get_global_var('func_16462')
call_19625 = func_16461_call()
call_19626 = func_16461_call()
func_18325_call = mod.get_global_var('func_18325')
func_18327_call = mutated_mod.get_global_var('func_18327')
call_19639 = relay.TupleGetItem(func_18325_call(), 0)
call_19640 = relay.TupleGetItem(func_18327_call(), 0)
func_18185_call = mod.get_global_var('func_18185')
func_18187_call = mutated_mod.get_global_var('func_18187')
const_19647 = relay.const([[-6.299276,7.277081,-2.438128],[-3.967855,-5.478738,4.491426],[-4.970022,-4.565251,4.866589],[-2.352506,-5.560933,-3.539628],[2.751799,-1.378732,8.063362],[9.233567,9.836451,-9.946774],[-1.136369,-8.104068,-0.515781],[-0.702991,4.585934,6.475149],[-0.673126,-9.647647,4.325762],[-8.658347,-4.883276,-1.596953],[-5.815544,0.793123,5.652978],[7.902882,-0.680632,-6.674277],[5.695280,3.433583,-2.241736],[7.665759,3.548798,5.357616],[7.595382,6.667698,3.250025],[1.847649,-3.273532,1.842439],[1.051468,3.105668,7.243652],[-8.394404,-1.790051,2.105356],[-6.674847,9.385785,-7.629729],[8.108042,3.615953,5.397459],[-0.796030,-2.171084,6.813189],[-7.017820,0.230027,-0.859515],[-7.781934,0.918226,2.195440],[2.430436,-2.937863,4.712308],[6.043554,-6.359578,5.832506],[1.532251,-9.868426,-3.114357],[-8.063284,-4.088423,8.817387],[-8.213065,-2.975342,-3.195191],[-9.315083,8.410779,7.162256],[-3.266100,8.412684,8.850156],[-5.789981,3.710499,-3.067464],[7.542454,-7.853358,-7.210537],[-1.861467,4.296379,2.304466],[-7.425981,7.471310,-5.751021],[-0.687769,-1.623446,5.344493],[0.801127,-7.934855,-4.166659],[-1.520062,6.926823,-9.239822],[-9.975902,-9.918193,2.813511],[-9.948649,-1.061383,9.758498],[-7.035890,3.135066,-7.762205],[-5.826380,-4.447312,-2.606057],[2.515145,-4.000906,4.976826],[0.438031,-3.526214,-8.641755],[5.021365,8.014336,-6.617460],[-5.280367,4.439492,2.711269],[-4.466305,3.418199,7.651498],[7.645894,-5.745685,0.128618],[-9.749285,-4.566330,1.529883],[-2.851170,5.785335,-5.664447],[3.977756,-0.841943,-3.858601],[-7.552044,5.180854,3.995006],[8.527223,5.016072,3.405210],[6.225244,1.295330,-1.112225],[-1.736814,6.760012,-9.293021],[-0.887745,-0.019624,-2.604702],[-9.840717,2.804296,-2.720095],[-8.540525,-4.820465,-1.069074],[1.660057,1.220228,7.545836],[2.983809,7.881067,2.687683],[-5.388045,1.833602,-8.185388],[4.361301,-6.476060,-6.658913],[7.703652,-2.207278,-6.397813],[0.197832,-0.457902,6.893100],[-9.014322,-1.808022,7.886154],[-2.836577,2.800806,2.114202],[5.598594,-1.973182,9.509885],[0.956754,-9.566610,-8.395355],[-8.493421,-2.126926,3.707377],[-4.486495,-0.489251,2.712466],[-2.867552,0.248766,5.778804],[0.009802,4.586557,-4.789797],[-7.688696,3.347678,2.283906],[8.241329,-4.253370,-9.147984],[0.530993,8.301098,6.697688],[-2.382401,-2.151141,9.649674],[-2.011920,9.472829,3.171320],[-5.880063,0.892201,-2.790310],[-5.972087,-6.485509,4.862443],[-8.030527,3.959866,-6.755014],[-7.804971,-4.692443,-3.556783],[-0.143549,-6.983374,-3.080059],[4.511047,7.503125,-0.746523],[7.238499,5.928535,8.711378],[-0.876409,-8.216793,-5.806856],[3.383520,0.491286,7.220924],[6.901539,-3.051987,8.679582],[2.725086,7.013363,4.650124],[-3.405983,-0.202059,-4.510098],[-5.707243,6.916700,-5.066379],[6.043382,-9.614702,7.083634],[-2.367993,3.406067,-3.640462],[8.811529,2.453395,-6.228232],[5.670717,9.669389,6.154430],[3.308757,7.557375,-9.804371],[-5.825631,9.466676,-6.267637],[8.151539,8.776511,7.398566],[9.709636,-0.213130,5.719162],[-0.445901,3.536710,5.201097],[3.370192,9.174307,1.810578],[9.193319,0.314346,8.251038],[9.844768,8.582750,7.786526],[5.045913,6.390463,-5.299240],[-4.974596,4.938973,-8.003432],[-2.675394,-6.025349,-0.595912],[4.989295,1.360151,-9.082283],[-8.754109,1.505004,6.987410],[-8.958966,-1.925315,-2.895822],[7.249329,0.569475,-8.343117],[6.007547,0.937385,-1.861222],[9.501527,9.434001,1.442368],[5.020479,-7.906315,1.310234],[-0.692940,-5.451673,5.740030],[9.499049,7.739013,-2.837627],[-2.448552,6.012674,6.510049],[-8.346143,7.095770,4.044929],[6.530071,3.078041,-8.440548],[3.450881,-6.550764,4.255319],[-3.933321,-1.170482,0.590121],[-4.494836,-6.071550,3.128458],[4.317767,6.942798,-0.505574],[1.982651,6.898807,1.883407],[0.348654,-1.656086,-2.627190],[-3.865134,-2.382634,-0.737129],[2.274882,-0.411246,-0.929892],[0.504592,6.791630,7.867014],[9.429507,8.639457,0.893923],[-6.611222,-4.847209,-5.933269],[-1.274479,7.740868,-1.262746],[-2.692911,-1.750530,1.561018],[6.202400,3.102415,7.454840],[-5.117822,5.482326,-2.655517],[-9.927937,-7.418107,5.172122],[9.484086,3.290335,6.966853],[-5.233799,4.879933,-5.446791],[-2.468956,8.473131,-3.519559],[-7.477976,5.898097,-7.058194],[-5.021723,1.759189,2.602724],[0.081133,-3.354353,-7.714982],[-3.681107,-8.100073,9.573991],[0.549782,-3.497586,1.228374],[0.969884,6.038275,-9.531915],[-5.391318,-3.828125,4.162506],[2.694340,-8.742513,1.836008],[4.528617,3.973103,1.048645],[-4.660018,-5.937258,6.349210],[7.754559,6.259019,8.234001],[-7.392452,-5.498143,1.652998],[8.799214,7.849261,5.450631],[-8.113804,-1.260195,-3.527834],[-5.377743,-2.182828,7.784996],[5.551110,3.146341,8.292514],[-5.932998,-2.482359,-8.616205],[-5.933600,-0.126696,5.999207],[-4.073270,-9.540594,8.182091],[-5.222030,7.642699,0.048241],[-6.794390,3.712003,6.915969],[-0.580160,9.206355,8.335497],[8.144065,5.448414,3.829510],[3.193267,-7.917215,-2.597321],[-8.904325,5.964403,-5.386476],[-8.320347,8.495710,-3.360799],[-9.623396,-1.616590,8.462225],[4.821947,7.570251,8.180028],[5.115812,-1.687577,-2.640096],[4.880923,7.430109,4.886617],[4.380633,-6.063403,9.160163],[-1.701051,-1.137419,1.029074],[-7.475413,-0.650188,5.301977],[-1.270714,-4.893314,-4.400305],[1.662858,2.683645,8.110445],[-1.714434,-1.718365,6.460236],[7.264123,3.532532,1.821571],[-3.042914,6.830273,1.553024],[-9.035023,7.268612,7.254441],[4.763073,0.742237,3.452366],[0.622886,-6.342770,5.297417],[-3.884343,4.590337,-0.702476],[-0.628085,-4.441229,3.081923],[8.237676,8.863001,-1.902828],[-9.530963,8.588993,-8.819534],[-8.310203,3.185541,8.128143],[0.662335,5.849482,3.877758],[4.836240,-1.520748,4.397402],[4.840374,5.708431,8.791300],[5.618398,-6.850778,6.503958],[-1.434879,-8.550977,-0.986124],[-2.116341,6.716216,-2.656443],[3.736298,8.959808,4.609970],[1.993930,1.791548,2.786356],[-8.360469,-8.332539,-8.613503],[9.946258,-3.871071,-8.358078],[1.345982,-0.502801,-1.527615],[2.514337,-7.500829,-5.785784],[4.605730,-3.358353,-6.830286],[7.845733,6.273212,0.387234],[6.538320,-8.124957,7.898084],[4.765276,8.660989,6.141207],[-1.370470,7.663274,9.577532],[2.038462,0.765198,1.745653],[9.205342,-3.019074,4.011069],[-7.729034,-8.124906,-8.332140],[1.478471,-6.998242,3.956650],[3.939577,-4.400388,-5.434560],[-7.180272,-5.505495,4.527712],[0.138583,-8.308209,3.643797],[-4.794491,-3.545322,-3.748702],[-2.070873,-5.327793,-6.680337],[-4.771221,-8.628038,-3.292954],[0.572588,-4.756810,-3.954536],[1.802906,-5.567764,0.678976],[0.915955,-8.619910,-1.680161],[-8.696158,-6.950167,9.177956],[-2.193833,-1.306299,-1.203474],[0.266468,4.291212,2.235629],[-3.966664,-3.179065,-9.488347],[-1.406591,3.054409,-3.186761],[-7.339325,-4.586215,1.336636],[0.812114,1.426861,-3.194346],[8.857926,8.204139,2.357214],[-1.518825,-6.648507,8.827406],[5.689712,-9.305330,-1.035287],[-3.118946,-0.109317,6.468287],[6.875442,5.210374,6.089872],[-2.489480,-1.479692,7.090714],[6.786814,8.587748,-8.263527],[-9.507059,-0.312619,-2.364946],[8.119485,7.807571,6.450782],[-6.100809,-8.545047,-8.140241],[9.781429,-8.693684,-1.716794],[-4.105259,2.340741,4.774819],[-3.991583,4.023744,5.420515],[1.238995,3.218091,-4.179554],[3.850615,3.082624,-9.718948],[9.281484,-3.800007,2.697571],[-2.973020,-7.443641,3.590621],[6.625814,-1.701889,7.110653],[5.459567,-8.439733,5.636095],[4.168561,1.213677,-4.162604],[-2.284891,-8.488838,9.420927],[-1.303998,3.864371,-0.611222],[-0.172666,-1.175685,-6.408723],[-1.004237,-1.479071,-2.720267],[8.548314,-2.884443,-8.167074],[9.805311,3.310043,-6.511837],[9.061769,-6.076790,1.674668],[-1.856422,-7.916406,-4.214167],[-8.393036,-2.371741,-7.718089],[-9.340073,7.733106,-8.142728],[-3.446737,-9.897708,2.702023],[-4.954403,9.492101,2.774164],[2.620331,9.571782,-9.481612],[3.351030,-5.087276,5.160095],[-3.828829,8.810014,6.936653],[-8.128918,6.376011,5.601220],[7.029771,4.502952,-6.611466],[5.479956,-7.572255,7.318865],[7.105457,0.974039,8.292873],[-6.611352,3.304119,7.427454],[7.614604,-6.147535,-0.791323],[-1.268679,2.434054,0.068713],[-4.225678,-5.495891,1.990300],[-5.213268,-4.361169,-2.930921],[-0.478432,1.078813,-8.732659],[-7.747394,-7.897365,-4.278255],[-0.062102,-0.328814,4.142349],[3.464909,4.672158,-1.629887],[-1.183281,8.152279,0.681615],[-9.977637,-4.628473,6.669809],[-6.859626,-6.452331,-1.530417],[2.297301,3.542906,-4.584778],[9.811541,1.015989,9.978868],[7.030359,-0.413337,-9.533027],[5.021583,0.242961,3.743269],[-7.384871,7.260935,-4.467980],[-1.989672,-3.019861,-0.744407],[-2.040353,4.242003,-6.818020],[7.563295,-1.684112,-5.822404],[5.109841,2.988464,9.462621],[1.840976,-8.348367,-8.727718],[-2.448507,-1.703714,3.383512],[-7.552901,2.600594,5.811032],[-4.990163,9.078099,-2.837869],[-2.199189,2.804531,-0.722861],[-8.187151,6.856243,-6.055839],[2.293724,-7.564642,-3.935001],[-6.013639,2.097552,-8.445788],[1.944102,7.493858,9.697177],[-9.879960,-8.966295,8.023879],[-7.530200,-1.355669,-7.203277],[-4.636581,-5.737027,3.593975],[-1.697295,7.003959,7.062151],[-7.660216,-6.510552,-6.501756],[3.032194,4.048635,-6.543131],[-3.315068,-8.793474,-2.785495],[-7.883653,9.403790,7.500488],[5.627621,-8.672583,7.966626],[-3.580980,2.567518,-4.756242],[-5.734135,-6.931192,7.611358],[-3.032963,-7.977218,-3.364241],[0.721423,2.672389,4.409210],[2.281288,-9.690849,1.439082],[-8.656437,1.642755,8.759769],[6.892726,6.092924,2.842927],[-5.139732,-9.316557,7.490919],[-9.953106,9.803271,3.775678],[-4.690866,9.472640,-7.303644],[1.047500,-8.498261,-7.741345],[-6.254573,1.069769,-2.186871],[-0.046379,-9.367190,6.316853],[4.419387,-3.709046,8.593038],[-1.212905,1.282286,-8.909004],[-7.069778,-3.652553,-2.343691],[-7.715760,-9.604340,-8.767737],[7.555961,8.598441,3.556403],[7.538301,-6.153634,-1.748419],[8.776440,-1.213994,-8.214156],[-9.886420,-9.516916,-7.823572],[-3.722560,2.448546,-9.871939],[5.716446,-4.752797,-5.311645],[0.767921,-8.902995,5.621741],[5.796743,0.508625,5.847247],[-2.780866,9.075726,-0.460694],[5.378002,-7.264612,7.692569],[-2.742089,-0.539529,-5.900751],[-0.849986,-6.917530,4.379437],[6.815536,-8.703277,-4.115770],[8.527706,-6.618988,9.848596],[-7.898990,4.588843,3.187802],[9.087733,6.335275,-8.531768],[-7.705141,7.411446,-3.219347],[8.145746,6.439757,-0.452559],[3.390311,-6.315019,-2.849646],[3.564606,-1.725574,-3.243741],[5.827743,2.642657,0.589002],[-8.858247,-5.144348,8.020969],[2.385652,7.828721,-8.257089],[-3.899407,2.347066,1.156430],[4.700859,-5.749785,0.281762],[7.156799,-8.467444,5.584164],[0.822135,-9.985656,7.421825],[-4.287221,-5.231728,6.617728],[2.319900,-1.023130,-3.571466],[5.547610,-6.071130,4.241680],[-6.379955,3.594864,6.945203],[-6.048976,-4.178423,2.202405],[-3.955917,-4.557888,8.105605],[-8.523657,-6.174510,5.345312],[-6.831740,-8.601659,-9.416746],[2.266353,-8.804036,5.767968],[6.663953,-0.565581,-8.971174],[-4.516735,1.472123,7.484215],[-8.507980,-8.884322,3.304020],[-2.031644,-3.351457,-6.722228],[-7.342524,1.117876,-3.609924],[5.525941,-5.646007,-5.175175],[9.140048,-6.486870,2.312429],[5.253829,4.107439,-7.619290],[5.873896,-0.833094,5.250886],[-9.718400,-1.559967,8.094545],[-7.644471,6.062456,-4.075177],[-4.181426,-9.558405,0.382172],[-9.196975,5.703204,-4.002867],[-9.030744,-8.594672,2.309625],[-8.298285,-5.448508,7.268294],[8.592939,-1.909819,-6.484705],[-4.819299,-8.382850,7.387403],[0.560310,-5.557977,2.496562],[-4.225351,-7.435727,4.525225],[1.147995,1.510829,-3.914735],[2.990964,-9.995837,-7.269231],[-7.895136,5.929937,6.761433],[-6.155942,8.173410,-0.757260],[8.691630,-9.915900,3.094636],[7.490725,9.414110,-4.206168],[2.088622,-3.132240,1.211573],[4.930270,6.902709,-9.768972],[1.341637,4.210784,7.612337],[-9.729445,4.939477,-7.191778],[-9.289540,9.137815,-5.543441],[8.452826,3.543312,-5.802938],[2.870047,-7.548230,-1.759956],[3.080559,-8.067305,-0.311494],[-1.449988,-6.962178,-8.562053],[3.710004,0.478341,-4.507374],[-3.868394,0.776687,9.334915],[6.973201,9.630043,-9.653431],[-2.255296,-6.409342,-1.335702],[9.644714,7.016617,-3.728327],[-2.878318,-4.798333,-1.831035],[-3.105281,-1.893977,-6.198323],[8.061070,-1.641023,-2.126290],[-8.475018,4.385332,5.349380],[-7.256124,-2.106254,-0.592845],[3.908402,-6.426744,-8.935904],[-4.563673,-0.912156,5.767289],[4.724057,-9.046314,9.521707],[-5.849091,2.269695,-7.377741],[9.396064,0.519548,-2.694691],[2.841191,5.219372,7.468124],[-6.305338,-9.325835,7.128388],[-1.235917,-1.836073,-3.239400],[8.179693,3.035016,-6.901753],[3.229186,-3.682239,-4.125708],[-3.693856,-7.883861,4.402124],[-4.417485,-2.359616,-1.158121],[-9.595813,-4.137251,5.699547],[-5.136320,9.134947,-1.071599],[-3.926866,9.507262,-3.503054],[2.164752,5.912833,-3.919609],[-0.660526,8.925647,9.307770],[-9.238944,-7.961036,-7.459855],[8.741663,-7.548129,9.186530],[5.505792,-4.708532,-4.697609],[-1.575632,0.572725,-8.426767],[-7.365495,-5.422328,5.614901],[-8.594485,1.728140,-8.201252],[-5.757914,1.039366,-2.383101],[4.191246,-1.879483,-7.803698],[5.198351,-1.899169,8.048131],[-8.910344,8.218194,7.791540],[7.990951,-3.909924,-0.863512],[-2.380315,7.644319,0.234191],[-8.355610,9.298356,-0.931338],[-6.312724,-6.933186,-2.254749],[0.276615,7.505186,-1.539679],[7.498613,-4.999404,-9.477589],[-8.717021,-6.800122,-3.458978],[8.176967,-1.178768,4.890069],[-3.566824,-0.220929,2.225596]], dtype = "float32")#candidate|19647|(429, 3)|const|float32
call_19646 = relay.TupleGetItem(func_18185_call(relay.reshape(const_19647.astype('float32'), [1287,])), 3)
call_19648 = relay.TupleGetItem(func_18187_call(relay.reshape(const_19647.astype('float32'), [1287,])), 3)
output = relay.Tuple([call_19585,call_19607,call_19625,call_19639,call_19646,const_19647,])
output2 = relay.Tuple([call_19586,call_19608,call_19626,call_19640,call_19648,const_19647,])
func_19654 = relay.Function([], output)
mod['func_19654'] = func_19654
mod = relay.transform.InferType()(mod)
output = func_19654()
func_19655 = relay.Function([], output)
mutated_mod['func_19655'] = func_19655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16817_call = mod.get_global_var('func_16817')
func_16818_call = mutated_mod.get_global_var('func_16818')
call_19696 = relay.TupleGetItem(func_16817_call(), 0)
call_19697 = relay.TupleGetItem(func_16818_call(), 0)
output = call_19696
output2 = call_19697
func_19715 = relay.Function([], output)
mod['func_19715'] = func_19715
mod = relay.transform.InferType()(mod)
mutated_mod['func_19715'] = func_19715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19715_call = mutated_mod.get_global_var('func_19715')
call_19716 = func_19715_call()
output = call_19716
func_19717 = relay.Function([], output)
mutated_mod['func_19717'] = func_19717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19715_call = mod.get_global_var('func_19715')
func_19717_call = mutated_mod.get_global_var('func_19717')
call_19754 = func_19715_call()
call_19755 = func_19715_call()
output = relay.Tuple([call_19754,])
output2 = relay.Tuple([call_19755,])
func_19767 = relay.Function([], output)
mod['func_19767'] = func_19767
mod = relay.transform.InferType()(mod)
mutated_mod['func_19767'] = func_19767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19767_call = mutated_mod.get_global_var('func_19767')
call_19768 = func_19767_call()
output = call_19768
func_19769 = relay.Function([], output)
mutated_mod['func_19769'] = func_19769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14748_call = mod.get_global_var('func_14748')
func_14749_call = mutated_mod.get_global_var('func_14749')
call_19827 = func_14748_call()
call_19828 = func_14748_call()
output = call_19827
output2 = call_19828
func_19838 = relay.Function([], output)
mod['func_19838'] = func_19838
mod = relay.transform.InferType()(mod)
output = func_19838()
func_19839 = relay.Function([], output)
mutated_mod['func_19839'] = func_19839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18150_call = mod.get_global_var('func_18150')
func_18152_call = mutated_mod.get_global_var('func_18152')
call_19848 = relay.TupleGetItem(func_18150_call(), 0)
call_19849 = relay.TupleGetItem(func_18152_call(), 0)
output = call_19848
output2 = call_19849
func_19855 = relay.Function([], output)
mod['func_19855'] = func_19855
mod = relay.transform.InferType()(mod)
mutated_mod['func_19855'] = func_19855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19855_call = mutated_mod.get_global_var('func_19855')
call_19856 = func_19855_call()
output = call_19856
func_19857 = relay.Function([], output)
mutated_mod['func_19857'] = func_19857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19319_call = mod.get_global_var('func_19319')
func_19320_call = mutated_mod.get_global_var('func_19320')
call_19881 = func_19319_call()
call_19882 = func_19319_call()
func_17661_call = mod.get_global_var('func_17661')
func_17665_call = mutated_mod.get_global_var('func_17665')
const_19886 = relay.const(-8, dtype = "int32")#candidate|19886|()|const|int32
var_19887 = relay.var("var_19887", dtype = "int32", shape = (110,))#candidate|19887|(110,)|var|int32
const_19888 = relay.const([-9,-5,-2,8,3,-6,9,-4,1,10,1,5,-9,-2,-1,7,-3,-10,5,-10,7,7,-4,-4,8,-8,-3,6,6,-9,4,-8,8,9,-7,2,-7,-10,9,-7,8,-8,8,7,2,10,1,1,5,3,-3,6,3,2,-1,-10,4,-2,-2,4,-4,-9,4,4,-2,-3,-1,6,6,5,6,-6,5,-1,-6,8,3,3,-9,-7,6,-7,-9,-1,8,-10,-3,-3,4,-3,2,8,-3,1,2,3,5,4,-3,-9,-1,5,7,2,5,2,1,1,3,-5,9,2,10,-8,-1,3,-9,-7,8,8,7,1,9,3,3,8,8,5,-6,-10,-1,-8,-3,7,-4,-7,4,-10,-9,7,-5,-1,5,-2,9,5,-6,2,-7,3,3,-2,-7,10,-9,7,1,6,5,4,-1,6,3,-9,9,2,3,9,-6,5,5,9,1,2,5,-2,7,6,-7,2,8,-8,-6,10,-7,9,-8,-7,-4,-6,5,7,-5,-5,9,-8,1,-9,-4,-1,3,-4,8,1,10,-1,5,-10,1,5,-3,9,1,-1,7,8,3,3,5,3,3,-4,-4,-1,8,-6,-10,-4,-3,6,6,1,7,-1,10,-10,10,5,8,10,3,8,-5,2,5,9,5,-3,4,7,-7,-8,10,-2,9,-6,-2,-4,5,4,-8,-5,2,5,9,-9,8,-5,1,9,-9,-2,9,7,-4,6,-3,4,7,1,-1,4,8,-10,-7,8,-3,-9,6,8,7,3,5,5,-7,1,9,-7,-5,5,-5,-9,3,3,-2,-1,-5,8,2,-5,4,-8,1,7,2,7,-4,8,-4,7,1,6,-4,5,10,8,-6,-4,-2,5,4,3,-8,-7,1,-8,-6,6,9,-8,3,-4,10,8,-2,8,-4,-5,-2,-7,-10,3,1,6,3,10,7,7,-3,-9,-7,-10,8,5,2,10,7,8,5,8,7,5,6,-1,-8,-4,9,-8,-3,-8,-5,9,-4,-1,-10,-4,-1,-10,3,-5,-6,-8,5,4,8,-5,8,6,10,10,8,-8,5,3,-3,-8,7,2,1,2,-5,4,-10,9,2,1,-3,7,8,5,10,10,9,-9,-7,-2,7,-10,-10,6,-8,2,-7,9,-10,-7,-10,-8,-1,1,-10,-2,3,-4,3,-5,-7,2,7,-9,8,7,-5,6,4,3,2,-10,1,8,-6,-7,-1,6,10,4,3,5,10,5,-1,-9,6,-8,5,-1,2,-1,6,-10,7,6,7,10,-5,3,-3,-10,2,-4,-7,-6,-2,1,-8,-6,-5,5,-6,-1,-1,-8,7,-1,-8,-7,-1,-4,-4,3,-6,-7,3,-6,10,-3,-4,-3,-1,-1,1,-3,-3,-5,2,8,-9,8,10,3,3,-1,7,7,10,6,-6,-6,-6,5,-1,5,-10,1,8,10,-2,-6,6,-6,3,-8,10,9,4,-3,9,-4,10,-10,3,-10,2,-3,-1,-3,-10,-3,-6,6,8,-7,-7,7,8,8,7,6,3,-8,-6,-1,3,-7,-8,-8,-2,3,-6,9,-8,-7,4,-6,1,-3,4,-5,8,3,7,-10,6,8,-4,8,-1,-8,-6,-4,-8,-8,-9,-7,-7,2,-4,2,-8,4,7,-7,-4,-5,-1,9,-6,-2,-2,-3,-1,-2,9,-7,-6,2,-2,4,-4,-10,10,2,8,2,-5,8,1,-3,4,9,2,3,-10,3,10,7,-3,-7,-7,9,-3,9,7,-4,3,-2,7,-2,4,1,9,7,10,-4,-2,-8,2,-9,-9,-9,-8,-9,8,-2,-7,8,2,9,-9,9,-8,6,-2,8,-10,2,-9,5,-2,-10,1,-6,-5,-4,-10,6,8,7,-7,-1,-1,4,-6,7,-5,9,-7,8,-2,6,7,-9,4,-7,2,-7,-3,-4,2,-6,-10,-7,-10,9,-9,-5,5,-1,1,-9,6,-5,-10,5,-2,-3,8,9,4,1,3,10,-1,8,-9,-6,-4,1,1,6,-6,8,-8,3,5,5,-9,7,-4,-3,-1,-5,1,-8,1,-8,4,3,2,-4,-10,-6,-2,1,9,10,-5,4,-2,-8,10,-1,1,6,2,10,-9,-2,-1,-10,9,10,-4,1,9,-10,-5,-5,5,-10,3,8,6,4,5,8,3,-9,2,-4,9,-2,-5,3,-8,8,2,-3,5,6,1,-3,1,1,4,-8,9,1,9,-3,-8,-10,6,1,-3,3,-2,-10,10,8,-9,9,6,-2,-6,2,8,6,-5,7,-5,-4,9,-4,5,5,8,-2,5,-9,-2,5,-5,6,-10,-10,3,6,7,-1,1,8,9,4,-7,5,8,-9,-2,2,8,-1,-7,-3,6,-9,-9,4,9,3,3,-5,-7,3,-9,-3,9,10,-10,10,-10,-1,-6,-8,-5,10,9,10,-10,-7,-7,10,4,-2,4,10,-3,-4,8,-3,-2,-2,10,7,4,-3,-4,-9,-2,3,-4,-1,-6,5,6,8,5,-7,3,-7,7,1,10,10,-2,-9,9,-5,-4,8,2,-5,7,10,-7,-8,6,8,9,9,2,-2,-9,-6,9,2,-2,-8,3,1,-4,6,8,7,3,-3,-5,6,3,-6,5,-6,7,8,-10,9,5,8,-1,-3,1,7,-10,-10,4,5,-8,-8,3,-4,-4,10,10,5,3,6,-3,-9,-8,5,-9,-5,3,3,-9,2,-1,3,10,-5,-7,6,7,-4,-8,-9,3,-5,7,-2,-4,10,-7,-7,2,-10,4,-10,5,8,-4,2,10,4,3,6,10,-3,10,4,5,-2,3,-1,-7,-4,3,8,3,-3,-6,6,-4,5,-10,-5,-4,-3,10,-7,-1,5,5,9,5,-4,10,9,8,7,2,2,-10,4,9,6,10,-5,-7,5,-6,-5,1,-2,5,-9,-3,2,6,-5,7,4,-7,6,-3,7,2,-8,5,3,9,-6,5,-8,-6,-5,-8,-2,-9,-10,1,-2,9,-5,-9,-4,-2,-1,-10,7,3,1,-4,6,-3,-4,6,-7,-7,9,3,-4,-6,2,-7,-4,-3,-4,9,-8,6,9,9,7,10,-4,1,-8,7,5,-8,-4,7,8,8,10,-10,-8,-7,-7,-2,8,8,-4,-5,-9,-9,6,3,-2,9,-8,3,8,-2,-4,5,-2,9,10,-5,9,-5,2,8,-10,-7,6,4,-9,8,-3,-7,-7,-8,-4,-9,-9,-7,-2,-6,-4,1,-5,1,-1,9,-3,6,-7,-9,9,4,-2,-8,8,5,9,9,10,7,-8,-5,5,10,-6,-2,7,-3,-7,-3,7,6,-5,9,4,9,4,-4,5,-2,-5,8,-8,-2,3,9,-5,-5,7,-8,-10,4,8,3,-2,-6,9,10,4,2,7,-7,-4,5,-6,6,-9,-2,-8,2,-1,-8,2,-6,10,-4,-9,1,3,9,-2,-7,-3,10,5,-3,10,-5,-9,-9,-10,8,-3,-3,7,-8,-6,10,8,-1,1,7,5,-6,-4,-3,-7,4,-10,-8,10,7,-5,-5,6,3,-10,-1,-4,-9,-1,5,-1,-7,7,-9,-1,4,1,6,7,-9,2,4,-8,-6,-5,-6,-9,7,-8,6,-3,7,2,-3,5,-6,1,-2,-10,7,-9,-2,-8,8,-7,9,-5,-4,-2,-5,-9,3,-8,-1,3,-6,3,-5,-6,10,7,3,-6,10,4,-4,-4,-4,-1,-3,-3], dtype = "int16")#candidate|19888|(1404,)|const|int16
call_19885 = relay.TupleGetItem(func_17661_call(relay.reshape(const_19886.astype('int32'), []), relay.reshape(var_19887.astype('int32'), [5, 2, 11]), relay.reshape(const_19888.astype('int16'), [1404,]), ), 2)
call_19889 = relay.TupleGetItem(func_17665_call(relay.reshape(const_19886.astype('int32'), []), relay.reshape(var_19887.astype('int32'), [5, 2, 11]), relay.reshape(const_19888.astype('int16'), [1404,]), ), 2)
func_18515_call = mod.get_global_var('func_18515')
func_18516_call = mutated_mod.get_global_var('func_18516')
call_19915 = relay.TupleGetItem(func_18515_call(), 1)
call_19916 = relay.TupleGetItem(func_18516_call(), 1)
func_7368_call = mod.get_global_var('func_7368')
func_7374_call = mutated_mod.get_global_var('func_7374')
const_19931 = relay.const([5.254197,-3.692013,-4.026839,-5.012295,-6.562304,-8.463986,2.864975,6.688482,-0.537769,5.716215,-8.576819,1.292294,-5.327741,-7.464600,0.069053,-2.510543,5.662606,1.294666,6.932021,1.140465,-3.554704,3.006733,2.507549,7.111454,2.620149,2.508288,4.884293,-3.767171,8.593314,-2.003624,0.084271,-8.149392,2.418374,-1.957696,6.297050,7.276175,-4.638634,2.799926,5.813643,9.102275,5.850221,1.842307,-0.150847,-0.126276,-1.398343,-3.226848,8.281815,-0.072960,-6.231943,-0.412445,-1.903862,4.824905,-9.185988,9.541427,-8.649041,-7.281984,0.832942,-3.124063,1.657939,-3.039144,4.364738,2.347580,2.306798,-5.509522,7.733488,5.010068,-0.417344,-0.421084,7.345880,-3.212034,-4.492042,-4.519560,-6.219026,0.145641,8.938601,-5.409025,9.191487,-3.819849,2.062212,-2.612999,8.531854,5.718445,5.813244,-7.689089,5.277414,-5.638786,-7.696868,6.235366,8.220742,-6.639016,-8.111074,-6.628158,4.425189,-9.363537,7.934232,1.838374,-9.631054,-5.685355,-2.323714,8.042773,1.101572,3.267158,-4.666983,5.088789,-6.470359,-6.051803,-1.544811,-2.608718,5.730452,-9.491628,9.705853,8.061494,-6.745009,1.473495,3.147508,-8.645675,-0.186357,-2.456418,3.584602,1.711925,3.206884,-2.576678,-0.116498,6.381506,-1.918882,-8.597720,1.265689,4.602188,9.928338,-3.297718,3.175148,6.759531,3.895099,-2.651803,6.622120,-6.494744,-8.242423,-1.018142,6.733601,-2.415728,-1.670735,6.427005,2.547274,0.557732,-3.811947,4.943708,3.591642,2.018735,-2.392798,8.986634,3.210791,-7.486619,-4.867292,-9.662573,1.335306,3.374751,3.029614,8.958289,-7.298439,8.683307,9.444381,-6.726205,-0.005754,4.727296,-8.245964,-3.767397,-4.929559,9.070496,-9.213044,-0.447404,-7.327557,7.213108,-3.185160,-9.534521,1.235046,6.888496,-8.617734,0.117665,-2.570839,5.197134,1.807112,-1.041075,2.155947,8.375040,-1.820007,2.859352,5.216863,-6.768937,0.368299,-1.344005,9.729754,1.940717,-7.014866,-2.868917,8.943404,3.224388,3.604504,-7.295208,8.753167,-7.349508,0.447117,-9.945999,-0.164164,7.613382,-3.167208,7.878572,5.044696,4.593862,1.093006,-6.760435,-4.105598,-9.954539,-7.590417,-0.208772,-5.649291,8.561995,-5.944824,-3.319685,-5.444229,-2.136006,-2.303228,-0.624648,7.422105,4.888485,6.831373,7.088249,1.958691,-3.422633,9.318277,3.803591,3.079756,3.468783,-3.820858,0.508561,4.551783,4.655248,5.059461,-1.078742,-2.470793,5.016212,7.549495,1.537939,-4.572972,-5.186579,-2.277666,1.173255,-9.947270,9.967320,1.822131,-3.594147,-0.240414,-1.348097,7.981496,-4.310446,-6.284312,-7.693301,9.308001,-9.962579,7.673189,5.397014,-3.314231,9.645990,2.885791,6.471389,6.429362,-7.641809,-9.605920,8.140899,4.086039,7.874579,-0.122774,6.824491,9.205240,4.010742,3.176011,-4.968143,-7.912719,-2.107513,-3.913050,-2.330113,1.972236,9.437555,5.422365,-4.439998,6.423701,-8.362230,0.511271,9.451195,3.888325,2.051527,9.726623,-8.423929,8.221304,1.764055,-5.331285,-5.440857,-1.486724,5.758990,-3.166795,-8.908692,9.026200,4.234071,7.771332,6.011617,-1.704077,9.701134,-2.758429,6.948399,-9.782189,8.617906,-1.773723,7.996233,-4.773071,-8.419093,-4.884737,-5.839251,7.521579,-2.209572,-2.033909,8.250577,-6.538834,-9.491487,-8.044893,-6.292639,-4.891176,6.482181,8.418271,-6.178462,-6.375645,4.632507,4.285785,-9.346485,7.529276,4.804304,2.818068,-6.708445,2.045206,-5.381229,-3.834648,9.555539,0.330995,0.001901,0.374831,-6.699874,-4.300183,-1.128604,0.271140,-5.525360,0.583535,-4.443663,-3.543165,-7.625326,6.192121,5.075547,1.797724,-1.854679,-8.390182,-8.037300,5.374679,2.350562,-3.611552,-5.468021,-7.488714,-2.065686,-7.214677,-8.318022,-2.307434,8.560932,-3.937701,1.992799,6.889688,-0.864611,-3.193607,3.857705,9.740110,5.180640,-8.096404,7.265051,4.921723,-2.319648,-3.526387,-8.847458,0.945844,-6.399196,6.127291,0.854386,8.603957,-3.526468,-1.222257,-4.682335,-8.219316,1.100421,4.040560,0.248778,2.559434,-6.905329,5.742218,-2.921019,-2.871924,-6.770804,-8.498032,-7.645841,2.458599,2.425272,-8.046358,0.190431,-6.636595,9.240974,6.617944,-4.178505,-9.580010,-5.870641,3.404202,-7.890073,8.666087,9.662566,5.738341,3.234005,-7.661563,-5.807204,-6.539326,5.113998,4.242274,-7.051699,-3.452346,8.029063,-1.758478,-1.079652,-7.094617,9.237696,0.844320,2.512516,0.740090,4.743866,-4.227135,-9.384552,0.879594,5.561193,6.231432,0.915249,-5.457263,-6.467965,-3.102948,-7.780535,-8.219874,-6.998499,5.592192,-5.777006,-0.391080,-6.177670,4.660172,-9.443590,0.803388,9.524782,2.163597,-7.050414,6.902144,-9.465066,3.961382,-0.685083,8.832241,8.906542,5.797430,0.285090,8.678254,-1.087869,-3.973224,4.280259,-3.489341,-0.931070,0.524855,7.742774,-6.261811,-3.588585,-8.441445,7.496864,4.347972,-0.817411,-8.326693,-6.752911,-1.235514,-4.708487,9.952764,-4.597271,9.171528,-3.375620,6.210276,6.355265,7.262536,1.902667,8.717771,1.576298,8.450010,7.352570,0.902526,3.846094,-4.051531,6.088812,7.612002,5.955258,-7.281840,1.713603,4.203312,1.200504,-5.199775,-9.849197,1.161712,-0.424886,-5.369119,-9.578340,4.034710,7.174138,-3.233965,-0.816147,-5.098653,-9.767858,0.363005,-5.809386,-8.984927,4.452004,-2.858105,-6.457392,-6.692251,-9.104992,-0.907956,-0.841295,-3.210661,4.336506,-8.153537,-8.587010,5.762415,-1.993786,-6.236811,0.020555,-1.554525,2.504923,2.605173,5.159273,-6.650304,-5.059201,-6.752509,-7.970832,-9.635400,0.485526,1.637328,9.365041,-0.089737,9.205756,-4.872931,-8.266389,-6.092993,5.839285,9.786940,8.338612,-4.650590,3.890830,-6.110700,5.981783,3.609707,-7.084776,-6.260877,-9.167859,9.601758,8.186363,-3.320782,-5.785879,7.463999,-4.022982,-5.454229,-3.964890,0.974270,-0.774810,9.700766,-8.727799,-4.682982,-2.375149,-2.645883,-2.520783,-3.690072,5.167871,3.308492,1.901687,4.442338,7.002687,9.338075,-5.396517,4.209924,0.645259,-6.719885,-1.066684,-3.330348,4.419342,8.122654,-4.156072,6.555678,-6.324909,3.412139,2.972782,-1.821556,1.050844,-3.253049,-2.299408,-3.833325,9.938127,-0.681480,1.226662,-3.274515,6.994011,-2.905627,5.039376,-9.582148,-5.974867,-4.527973,-0.365161,6.254691,-5.727308,-2.880933,9.237756,-7.496326,2.227110,-2.064332,6.314523,-1.809348,-3.699958,-5.352726,-0.096695,-5.939319,0.262915,1.660907,2.623286,0.405082,-8.461815,-3.133463,-6.464983,-5.184640,4.508452,-9.014778,4.500817,-5.719982,-0.966710,-7.670105,4.280057,0.661781,1.118554,-2.120782,8.609594,-4.156846,1.112339,-5.876466,-8.299088,-6.432084,1.527512,-0.952895,4.042952,8.834369,-8.153805,-7.482933,-1.454619,-6.452848,-4.924991,-5.005492,-6.109187,-7.393674,5.007450,0.529938,8.523705,-8.519775,-4.452078,-6.520987,1.715066,4.000997,0.449193,2.440150,-6.111616,3.827104,-5.868039,-6.783470,-1.353558,7.813678,2.638321,6.107687,-0.266173,-5.688781,7.382460,-1.076038,-6.323834,-4.774552,9.327666,0.530430,0.043118,6.201109,-8.029825,-5.085032,-9.437771,-6.326096,-6.503669,-0.282959,6.448541,4.645888,5.371787,8.840099,-7.289313,5.762853,8.211690,8.637272,8.564068,3.827693,-6.005936,0.211313,7.739964,2.183144,1.212188,-3.692127,-8.152195,6.435079,4.945892,6.750951,-4.066700,1.754049,9.678602,-0.766343,5.966398,-6.425403,4.521757,-8.367209,3.040330,-6.193835,-6.073351,-3.075071,8.250506,-8.142473,-3.031879,-4.435905,6.159723,2.234029,-5.680018,4.805600,0.004717,0.050170,9.559374,6.417238,1.500426,-5.701077,-2.797613,-4.540863,-3.361395,-3.828038,-7.735539,-5.331454,-7.491512,-0.301247,5.732725,5.604878,4.160757,-8.539991,-4.781892,-6.647137,5.342750,2.233850,9.070737,9.098210,1.257924,-5.425224,-6.044752,5.656902,-0.557262,5.157487,0.767072,-8.736823,-1.104919], dtype = "float64")#candidate|19931|(770,)|const|float64
var_19932 = relay.var("var_19932", dtype = "uint16", shape = (864,))#candidate|19932|(864,)|var|uint16
const_19933 = relay.const([-7.546331,-4.679287,-0.928137,8.654254,1.234077,-9.718185,0.397764,-7.794878,-7.054944,0.256950,1.826180,5.469191,-0.708027,1.902900,-0.806954,-6.407992,-6.451718,-9.179354,-6.158601,5.776971,-1.718155,7.117011,-0.775823,-5.481282,0.116446,7.716204,4.196723,-6.011531,-8.643644,5.109597,0.418574,0.398401,2.291510,-1.125457,-9.454984,4.896841,7.350770,-5.837079,-3.712839,-3.495972,-5.871770,-6.687449,8.298757,-0.166472,1.454924,-7.885958,8.654723,-2.953731,6.719197,-1.707679,-0.863957,-1.350501,9.582035,8.587603,8.986764,6.083334,3.130030,-6.700836,-6.887829,7.257519,-5.967994,-6.602390,7.402328,-3.914729,-5.059754,-4.024520,3.189516,-2.795380,9.259353,-6.300865,-7.606094,0.708336,-8.064216,-7.724604,-4.943844,-8.042405,2.579233,-0.900766,4.644276,5.976541,-0.415994,-1.673136,-6.570383,-3.682736,1.558220,-6.999539,-3.833695,2.750704,5.572919,8.334707,8.888691,5.760317,8.010445,-5.995665,-9.190066,-6.191070,2.649312,-4.834234,5.173233,-3.844367,-3.987008,-1.795228,-5.187148,5.093369,6.478475,0.333706,-3.097734,1.762587,-0.735855,-6.286111,0.520727,5.725080,0.250437,-4.844660,-0.871135,3.567224,-6.858105,0.572563,-0.579676,-4.737364,-8.626728,-5.188599,-9.792481,-7.924130,7.782819,-6.742431,8.909808,-3.086869,3.585718,8.870322,7.163217,-7.536328,6.642371,-9.887116,-6.478962,7.070690,-9.879658,8.277665,-0.005105,5.850805,-5.820654,-4.117791,-9.562647,0.792070,-7.305202,4.460682,8.743332,7.362203,-4.194588,-1.983783,-7.568050,1.304397,-6.780697,-7.072828,-0.069211,-9.223256,4.737739,-0.850468,6.889274,8.083737,-1.884181,0.821666,5.298227,-4.400638,-5.301964,-7.220353,1.385200,3.418394,8.237528,-1.219158,-3.340580,-7.260801,9.232383,2.700794,-2.943863,-2.377003,8.026867,4.072552,-2.674444,-1.762612,-7.001804,-1.039104,-4.327647,5.788281,0.337003,4.813893,3.474118,0.661997,-7.698783,4.458723,9.396002,-9.878327,-3.233506,0.486843,9.874974,4.245972,0.284989,2.115424,-8.970730,5.523709,-2.269352,9.522702,-9.930686,1.053725,8.625260,-3.208538,-0.451565,1.078589,-7.658727,-6.456503,7.460126,3.739680,0.257617,-6.008996,-9.112775,6.440885,8.961345,-1.273603,8.451669,-4.923225], dtype = "float32")#candidate|19933|(220,)|const|float32
var_19934 = relay.var("var_19934", dtype = "float64", shape = (100,))#candidate|19934|(100,)|var|float64
call_19930 = relay.TupleGetItem(func_7368_call(relay.reshape(const_19931.astype('float64'), [10, 7, 11]), relay.reshape(call_19885.astype('int16'), [1404,]), relay.reshape(var_19932.astype('uint16'), [864,]), relay.reshape(const_19933.astype('float32'), [220,]), relay.reshape(var_19934.astype('float64'), [25, 4]), ), 0)
call_19935 = relay.TupleGetItem(func_7374_call(relay.reshape(const_19931.astype('float64'), [10, 7, 11]), relay.reshape(call_19885.astype('int16'), [1404,]), relay.reshape(var_19932.astype('uint16'), [864,]), relay.reshape(const_19933.astype('float32'), [220,]), relay.reshape(var_19934.astype('float64'), [25, 4]), ), 0)
output = relay.Tuple([call_19881,call_19885,const_19886,var_19887,const_19888,call_19915,call_19930,const_19931,var_19932,const_19933,var_19934,])
output2 = relay.Tuple([call_19882,call_19889,const_19886,var_19887,const_19888,call_19916,call_19935,const_19931,var_19932,const_19933,var_19934,])
func_19944 = relay.Function([var_19887,var_19932,var_19934,], output)
mod['func_19944'] = func_19944
mod = relay.transform.InferType()(mod)
var_19945 = relay.var("var_19945", dtype = "int32", shape = (110,))#candidate|19945|(110,)|var|int32
var_19946 = relay.var("var_19946", dtype = "uint16", shape = (864,))#candidate|19946|(864,)|var|uint16
var_19947 = relay.var("var_19947", dtype = "float64", shape = (100,))#candidate|19947|(100,)|var|float64
output = func_19944(var_19945,var_19946,var_19947,)
func_19948 = relay.Function([var_19945,var_19946,var_19947,], output)
mutated_mod['func_19948'] = func_19948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19118_call = mod.get_global_var('func_19118')
func_19119_call = mutated_mod.get_global_var('func_19119')
call_20010 = relay.TupleGetItem(func_19118_call(), 1)
call_20011 = relay.TupleGetItem(func_19119_call(), 1)
output = relay.Tuple([call_20010,])
output2 = relay.Tuple([call_20011,])
func_20029 = relay.Function([], output)
mod['func_20029'] = func_20029
mod = relay.transform.InferType()(mod)
output = func_20029()
func_20030 = relay.Function([], output)
mutated_mod['func_20030'] = func_20030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18212_call = mod.get_global_var('func_18212')
func_18214_call = mutated_mod.get_global_var('func_18214')
call_20054 = relay.TupleGetItem(func_18212_call(), 0)
call_20055 = relay.TupleGetItem(func_18214_call(), 0)
func_3287_call = mod.get_global_var('func_3287')
func_3291_call = mutated_mod.get_global_var('func_3291')
var_20079 = relay.var("var_20079", dtype = "uint32", shape = (420,))#candidate|20079|(420,)|var|uint32
call_20078 = relay.TupleGetItem(func_3287_call(relay.reshape(var_20079.astype('uint32'), [10, 7, 6]), relay.reshape(var_20079.astype('uint32'), [10, 7, 6]), ), 0)
call_20080 = relay.TupleGetItem(func_3291_call(relay.reshape(var_20079.astype('uint32'), [10, 7, 6]), relay.reshape(var_20079.astype('uint32'), [10, 7, 6]), ), 0)
output = relay.Tuple([call_20054,call_20078,var_20079,])
output2 = relay.Tuple([call_20055,call_20080,var_20079,])
func_20085 = relay.Function([var_20079,], output)
mod['func_20085'] = func_20085
mod = relay.transform.InferType()(mod)
mutated_mod['func_20085'] = func_20085
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20086 = relay.var("var_20086", dtype = "uint32", shape = (420,))#candidate|20086|(420,)|var|uint32
func_20085_call = mutated_mod.get_global_var('func_20085')
call_20087 = func_20085_call(var_20086)
output = call_20087
func_20088 = relay.Function([var_20086], output)
mutated_mod['func_20088'] = func_20088
mutated_mod = relay.transform.InferType()(mutated_mod)
const_20100 = relay.const([[[-4.166261],[-8.838598],[-3.388094],[1.505129],[-3.911450]],[[-0.828633],[2.438990],[3.241921],[7.429210],[-2.426427]],[[-5.202402],[1.857989],[8.060269],[2.076098],[-5.990133]],[[3.336330],[-1.078305],[-1.645759],[-8.446166],[-1.331553]],[[7.686887],[2.044706],[7.393572],[2.038557],[-6.828032]],[[-6.322813],[-9.040218],[4.379785],[-4.265771],[-6.260658]],[[-0.115257],[7.995147],[-8.904197],[4.793488],[-2.870348]],[[5.846906],[-1.304037],[-0.153256],[3.028960],[-8.767938]]], dtype = "float32")#candidate|20100|(8, 5, 1)|const|float32
uop_20101 = relay.atanh(const_20100.astype('float32')) # shape=(8, 5, 1)
bop_20107 = relay.bitwise_or(uop_20101.astype('uint64'), relay.reshape(const_20100.astype('uint64'), relay.shape_of(uop_20101))) # shape=(8, 5, 1)
output = bop_20107
output2 = bop_20107
func_20118 = relay.Function([], output)
mod['func_20118'] = func_20118
mod = relay.transform.InferType()(mod)
output = func_20118()
func_20119 = relay.Function([], output)
mutated_mod['func_20119'] = func_20119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14228_call = mod.get_global_var('func_14228')
func_14229_call = mutated_mod.get_global_var('func_14229')
call_20126 = func_14228_call()
call_20127 = func_14228_call()
func_19096_call = mod.get_global_var('func_19096')
func_19097_call = mutated_mod.get_global_var('func_19097')
call_20164 = func_19096_call()
call_20165 = func_19096_call()
func_6800_call = mod.get_global_var('func_6800')
func_6804_call = mutated_mod.get_global_var('func_6804')
const_20170 = relay.const([[True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,False,False],[True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,True,True],[False,False,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,True,True],[True,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False]], dtype = "bool")#candidate|20170|(4, 132)|const|bool
var_20171 = relay.var("var_20171", dtype = "int16", shape = (9, 156))#candidate|20171|(9, 156)|var|int16
call_20169 = relay.TupleGetItem(func_6800_call(relay.reshape(const_20170.astype('bool'), [12, 4, 11]), relay.reshape(const_20170.astype('bool'), [12, 4, 11]), relay.reshape(var_20171.astype('int16'), [1404,]), ), 1)
call_20172 = relay.TupleGetItem(func_6804_call(relay.reshape(const_20170.astype('bool'), [12, 4, 11]), relay.reshape(const_20170.astype('bool'), [12, 4, 11]), relay.reshape(var_20171.astype('int16'), [1404,]), ), 1)
output = relay.Tuple([call_20126,call_20164,call_20169,const_20170,var_20171,])
output2 = relay.Tuple([call_20127,call_20165,call_20172,const_20170,var_20171,])
func_20175 = relay.Function([var_20171,], output)
mod['func_20175'] = func_20175
mod = relay.transform.InferType()(mod)
mutated_mod['func_20175'] = func_20175
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20176 = relay.var("var_20176", dtype = "int16", shape = (9, 156))#candidate|20176|(9, 156)|var|int16
func_20175_call = mutated_mod.get_global_var('func_20175')
call_20177 = func_20175_call(var_20176)
output = call_20177
func_20178 = relay.Function([var_20176], output)
mutated_mod['func_20178'] = func_20178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16719_call = mod.get_global_var('func_16719')
func_16720_call = mutated_mod.get_global_var('func_16720')
call_20180 = relay.TupleGetItem(func_16719_call(), 0)
call_20181 = relay.TupleGetItem(func_16720_call(), 0)
output = relay.Tuple([call_20180,])
output2 = relay.Tuple([call_20181,])
func_20188 = relay.Function([], output)
mod['func_20188'] = func_20188
mod = relay.transform.InferType()(mod)
output = func_20188()
func_20189 = relay.Function([], output)
mutated_mod['func_20189'] = func_20189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18325_call = mod.get_global_var('func_18325')
func_18327_call = mutated_mod.get_global_var('func_18327')
call_20190 = relay.TupleGetItem(func_18325_call(), 0)
call_20191 = relay.TupleGetItem(func_18327_call(), 0)
output = relay.Tuple([call_20190,])
output2 = relay.Tuple([call_20191,])
func_20214 = relay.Function([], output)
mod['func_20214'] = func_20214
mod = relay.transform.InferType()(mod)
output = func_20214()
func_20215 = relay.Function([], output)
mutated_mod['func_20215'] = func_20215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17887_call = mod.get_global_var('func_17887')
func_17888_call = mutated_mod.get_global_var('func_17888')
call_20216 = func_17887_call()
call_20217 = func_17887_call()
output = relay.Tuple([call_20216,])
output2 = relay.Tuple([call_20217,])
func_20229 = relay.Function([], output)
mod['func_20229'] = func_20229
mod = relay.transform.InferType()(mod)
mutated_mod['func_20229'] = func_20229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20229_call = mutated_mod.get_global_var('func_20229')
call_20230 = func_20229_call()
output = call_20230
func_20231 = relay.Function([], output)
mutated_mod['func_20231'] = func_20231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15709_call = mod.get_global_var('func_15709')
func_15710_call = mutated_mod.get_global_var('func_15710')
call_20235 = relay.TupleGetItem(func_15709_call(), 1)
call_20236 = relay.TupleGetItem(func_15710_call(), 1)
func_11132_call = mod.get_global_var('func_11132')
func_11135_call = mutated_mod.get_global_var('func_11135')
var_20315 = relay.var("var_20315", dtype = "float64", shape = (96,))#candidate|20315|(96,)|var|float64
const_20316 = relay.const([[-6.082959,-7.390193,-2.556175,-1.176672,-8.849288,-3.180741,0.987210,0.668339,3.465172,-5.504165,-0.725439,1.647048,3.717622,-4.248488,8.260180,-0.497086,3.126129,4.507617,8.339265,9.695565,8.504185,1.331362,-1.273748,-0.679392,7.009689,5.864540,-2.165626,4.959226,5.406084,0.740691,-4.755305,5.939716,-8.191326,7.533127,-0.276594,-7.693716,-7.291753,9.134432,-6.489247,8.410511,-9.093966,6.510964,8.633298,-0.599614,-8.041037,8.964890,-3.868764,-7.275568,-0.952627,-1.529578,1.045293,-7.045105,-0.568687,-4.222649,-9.028020,-1.467410,8.463911,6.763619,-9.769450,6.212083,5.187733,0.277393,0.470576,5.428351,-7.189403,5.243425,-5.673822,8.918344,9.645866,8.256561,6.706411,-8.478904,7.099979,0.125415,1.295640,6.241283,-2.262709,-1.019214,-5.858482,6.054195,8.930962,-9.060492,-1.789225,-6.318545,-2.426844,0.685282,4.939492,-3.846318,3.512120,9.011131,-8.972536,-7.379412,9.835773,1.865542,-3.086702,-6.144226,2.155176,3.934284,2.056617,6.332531,7.797288,4.752378,-2.024084,6.103250,-0.710855,-7.274256,6.778934,9.965935,-1.949835,1.514343,7.146353,-4.701841,-9.987661,-4.360807,-4.014323,7.014496,5.770345,-5.480748,-8.015006,4.004840,-0.240230,-2.911742,-2.833635,6.724785,-1.246738,5.440359,-5.333616,-4.630732,6.270021,-0.269300,-0.366184,6.047909,8.986384,5.903991,-9.766776,-4.999615,-2.042734,-4.934090,-7.886146,6.118645,-7.583349,-4.048089,6.341626,-7.164228,5.127566,-0.560629,-8.932692,0.724147,0.693621,-7.723981,-1.872877,8.961788,7.237859,9.286445,3.020786,-9.018351,-0.658683,-4.305549,4.941688,-0.072767,-9.371159,-4.470113,2.745816,-8.705550,-0.146616,-3.266793,6.910520,4.252144,5.306071,-5.266634,-1.349345,9.093632,6.847591,-9.943101,-5.486920,3.210338,5.034502,4.458818,-3.738900,8.223475,-8.996441,0.051473,3.033935,-6.895888,5.248376,1.835729,7.414725,-7.227104,4.622088,4.505090,-3.398239,-0.779485,-3.524443,-7.546306,1.267585,3.652085,3.552634,6.099739,-4.068980,8.327508,-0.053905,4.683749,6.474076,-1.899221,-1.898405,-9.250100,-6.428454,-6.647716,9.397067,2.771467,-3.985705,-3.415967,1.592546,4.565190,-2.159670,-9.398484,5.476434,-2.249398,9.469511,2.369980,2.125247,-0.586185,-5.322403,-2.024972,4.039136,-0.676266,5.490976,1.104701,-5.442237,-9.210349,-7.393792,6.887804,-1.817409,-0.908945,-4.366958,2.707323,-1.467640,-0.747909,-9.956915,-6.865623,-6.561380,9.117007,6.250213,5.735133,6.540330,-6.554793,-8.368333,-8.992500,-8.565098,-6.905075,-6.838738,-3.399713,-2.408361,-9.047761,7.724939,-4.468592,8.084815,4.303190,0.070161,6.991538,-9.590078,-3.603548,7.850245,5.303222,7.439850,1.644091,7.533983,-7.421581,-5.537258,-9.368240,8.945307,1.402323,9.842283,-0.145834,0.959974,0.779035,7.737851,-2.518565,-7.789327,-9.540279,-5.335936,-9.740543,6.350069,7.558998,9.915373,-8.937425,-4.381023,5.082272,-9.083407,-3.162615,1.816598,-7.099902,7.995691,-2.309776,-1.404872,-1.893894,-9.020788,5.071455,2.997053,2.895584,-4.949272,-0.304070,1.351685,-2.972361,3.744830,-1.984088,7.545587,1.997179,7.050248,-5.379675,6.553047,-6.617161,1.106302,1.347411,-1.488814,9.393125,-4.032870,-4.434924,-5.156806,-0.341329,6.522283,-1.226110,0.800245,-7.640527,2.243102,-4.117189,0.716681,-2.921120,-0.074949,2.386028,-6.061359,-5.711232,-8.806177,2.717201,2.443354,-1.261148,-7.779874,9.753570,6.151611,-2.674881,0.572782,7.236845,-8.478049,8.840231,3.657455,5.816671,-1.951103,6.233026,-1.776115,2.583849,-6.530671,5.362121,-1.075848,-2.835336,-6.165386,1.740590,2.895423,-6.250543,-1.401276,2.792879,-5.697216,-9.849541,-3.864975,-2.743946,-1.934426,-1.893960,6.381636,1.345132,9.938704,7.762230,-5.352584,4.304889,6.501619,3.693545,9.595908,-6.431457,-6.359606,-8.870900,-0.452610,4.627194,-1.794349,2.402486,4.544848,-3.687883]], dtype = "float64")#candidate|20316|(1, 384)|const|float64
call_20314 = func_11132_call(relay.reshape(var_20315.astype('float64'), [16, 1, 6]), relay.reshape(const_20316.astype('float64'), [16, 4, 6]), )
call_20317 = func_11132_call(relay.reshape(var_20315.astype('float64'), [16, 1, 6]), relay.reshape(const_20316.astype('float64'), [16, 4, 6]), )
output = relay.Tuple([call_20235,call_20314,var_20315,const_20316,])
output2 = relay.Tuple([call_20236,call_20317,var_20315,const_20316,])
func_20318 = relay.Function([var_20315,], output)
mod['func_20318'] = func_20318
mod = relay.transform.InferType()(mod)
var_20319 = relay.var("var_20319", dtype = "float64", shape = (96,))#candidate|20319|(96,)|var|float64
output = func_20318(var_20319)
func_20320 = relay.Function([var_20319], output)
mutated_mod['func_20320'] = func_20320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16865_call = mod.get_global_var('func_16865')
func_16867_call = mutated_mod.get_global_var('func_16867')
call_20325 = relay.TupleGetItem(func_16865_call(), 0)
call_20326 = relay.TupleGetItem(func_16867_call(), 0)
output = call_20325
output2 = call_20326
func_20327 = relay.Function([], output)
mod['func_20327'] = func_20327
mod = relay.transform.InferType()(mod)
mutated_mod['func_20327'] = func_20327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20327_call = mutated_mod.get_global_var('func_20327')
call_20328 = func_20327_call()
output = call_20328
func_20329 = relay.Function([], output)
mutated_mod['func_20329'] = func_20329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19715_call = mod.get_global_var('func_19715')
func_19717_call = mutated_mod.get_global_var('func_19717')
call_20360 = func_19715_call()
call_20361 = func_19715_call()
output = call_20360
output2 = call_20361
func_20379 = relay.Function([], output)
mod['func_20379'] = func_20379
mod = relay.transform.InferType()(mod)
mutated_mod['func_20379'] = func_20379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20379_call = mutated_mod.get_global_var('func_20379')
call_20380 = func_20379_call()
output = call_20380
func_20381 = relay.Function([], output)
mutated_mod['func_20381'] = func_20381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16974_call = mod.get_global_var('func_16974')
func_16975_call = mutated_mod.get_global_var('func_16975')
call_20422 = relay.TupleGetItem(func_16974_call(), 0)
call_20423 = relay.TupleGetItem(func_16975_call(), 0)
output = call_20422
output2 = call_20423
func_20429 = relay.Function([], output)
mod['func_20429'] = func_20429
mod = relay.transform.InferType()(mod)
output = func_20429()
func_20430 = relay.Function([], output)
mutated_mod['func_20430'] = func_20430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16064_call = mod.get_global_var('func_16064')
func_16066_call = mutated_mod.get_global_var('func_16066')
call_20443 = func_16064_call()
call_20444 = func_16064_call()
uop_20447 = relay.acosh(call_20443.astype('float32')) # shape=(13, 3, 15)
uop_20449 = relay.acosh(call_20444.astype('float32')) # shape=(13, 3, 15)
output = uop_20447
output2 = uop_20449
func_20452 = relay.Function([], output)
mod['func_20452'] = func_20452
mod = relay.transform.InferType()(mod)
mutated_mod['func_20452'] = func_20452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20452_call = mutated_mod.get_global_var('func_20452')
call_20453 = func_20452_call()
output = call_20453
func_20454 = relay.Function([], output)
mutated_mod['func_20454'] = func_20454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15818_call = mod.get_global_var('func_15818')
func_15820_call = mutated_mod.get_global_var('func_15820')
call_20487 = func_15818_call()
call_20488 = func_15818_call()
func_17368_call = mod.get_global_var('func_17368')
func_17373_call = mutated_mod.get_global_var('func_17373')
const_20506 = relay.const([9,-5,-10,1,-6,-6,-9,-2,-8,-4,-7,10,1,4,2,-7,1,-2,-6,-6,-1,-7,-9,-3,-1,2,8,-10,4,2,-3,-9,-2,-7,5,1,8,-6,-1,3,-6,8,7,-2,-1,-8,-3,1,9,2,-5,-8,2,-9,-3,-3,-7,2,8,-4,-6,5,9,-5,-6,-10,9,-4,-4,-2,-5,-7,-5,-6,-2,-3,-1,10,-4,8,-9,3,-8,8,1,-8,-6,-1,-3,7,-7,4,7,-8,6,-3,4,-6,4,-4,-8,3,9,-7,1,8,4,-6,5,-4,-1,9,-4,6,10,2,4,2,-7,6,2,-6,5,9,-9,2,-9,-3,-7,-10,-1,-3,-8,-6,5,-5,-5,5,-4,-9,-7,-10,3,1,4,-7,4,10,6,-6,-10,-7,-3,-5,7,9,7,10,7,-10,-3,-8,8,10,5,-2,-9,8,-1,9,8,-2,9,5,-3,7,-3,-6,2,-4,4,-2,6,4,-4,7,-1,7,1,6,-10,-2,7,-3,-4,7,-4,10,8,9,-9,4,-5,9,-4,2,9,6,-1,-8,7,-2,4,-10,8,-6,8,-6,-10,1,-4,-5,-6,-1,-9,2,4,-6,-6,1,-8,10,7,-10,-2,1,5,-9,9,8,10,-6,3,-3,10,2,10,-5,9,6,-6,9,6,-4,9,5,-1,-2,-2,-3,8,2,9,-9,-1,-10,-3,-10,-7,6,-6,5,-1,-4,-1,-7,6,1,7,2,4,-6,-2,-7,-3,-7,5,8,9,3,3,-1,1,2,1,-5,9,1,8,-2,-5,1,9,8,-3,7,2,7,-1,9,-7,6,-6,7,9,6,-6,-3,-6,2,5,7,9,-1,3,4,-4,5,-9,3,-2,1,-4,5,-9,-9,-8,10,-10,-10,10,-4,6,4,2,5,-8,3,3,4,-5,-4,1,10,6,-6,-6,3,-10,9,-6,-5,9,10,6,-3,7,5,3,1,7,-8,-10,7,9,1,8,-2,5,-10,6,-3,-3,2,4,-9,-5,-6,-7,-4,-8,-2,2,-7,5,-10,-3,3,3,-5,-3,10,1,-10,10,5,-8,6,2,-6,1,8,-1,1,10,-3,-10,8,8,10,-3,-5,3,-10,-3,1,-6,-9,2,3,7,3,-8,1,-1,3,7,5,-9,4,-3,9,4,6,-7,-7,2,4,-1,7,7,5,10,-5,-5,3,3,-7,10,-10,2,-3,-7,6,3,1,-3,-5,8,-2,-8,1,8,8,-3,7,8,-10,9,5,1,-6,-6,-7,-3,-5,7,2,-6,-3,1,-4,2,-3,2,-6,8,7,-3,6,7,-4,-1,-10,-9,6,7,-8,-4,1,-1,-10,7,2,-6,-3,-4,-7,-5,2,4,-3,-7,-9,4,-8,-4,-3,-8,10,-5,-6,10,-2,4,1,3,8,-7,-3,-4,-5,1,-1,4,2,-6,10,4,3,7,6,9,8,-9,-8,-3,-5,-2,-3,10,8,8,4,-10,-9,-2,-7,-9,9,-7,4,2,4,8,2,5,-5,-10,4,-5,-8,-10,-8,-1,10,3,-8,5,-9,-9,2,3,-8,6,4,7,-8,7,7,-2,6,2,10,-5,-10,-10,-10,-2,5,-8,-9,10,-3,3,5,-6,-9,-2,-6,10,1,10,2,-10,10,-7,-3,6,4,-6,3,7,-2,2,7,-4,1,-10,6,3,7,6,-7,-8,2,-7,7,10,4,-7,-6,-9,-7,-4,-10,8,7,9,-6,4,-2,6,8,9,2,4,9,6,4,-8,9,2,-9,9,-8,7,7,-9,3,-6,8,-2,-3,2,10,-2,5,4,-4,1,-9,4,-6,-10,3,-4,6,-7,-6,-6,8,-7,1,6,6,7,-10,1,4,-2,5,-9,2,2,4,6,6,-4,5,-2,9,-6,10,2,-7,2,-2,5,-6,4,4,1,-3,7,-5,9,-8,-3,-2,-2,-3,3,9,1,-6,7,-7,10,-5,8,-5,6,-3,10,7,-4,-10,6,-6,5,4,-2,2,10,8,-9,-6,6,5,-7,-2,3,-8,1,7,-6,10,1,9,-1,-9,1,3,-9,3,-1,4,9,2,-6,8,10,-9,1,-2,4,-3,1,2,6,-3,-2,-10,1,-3,-1,-10,-10,-1,6,5,5,6,-6,3,6,7,-6,-1,9,5,-6,10,-5,-10,4,-2,-5,-2,-7,-1,4,-2,-6,-7,-8,6,9,-1,7,-5,7,10,8,-1,9,-9,-1,-3,-6,4,3,10,-6,-4,10,-3,-9,-7,5,1,1,6,2,10,10,-4,2,4,-2,-10,-10,-9,4,-5,5,2,7,-7,9,-7,-1,-1,2,2,6,8,3,-4,-3,-5,-6,-4,6,1,1,6,8,7,-5,-6,9,4,1,-10,-10,5,-3,-8,-2,-4,-7,-7,8,-5,-10,-3,-6,2,8,2,-6,-1,-5,8,7,2,-4,7,2,-6,-4,1,5,-7,-7,10,-5,-2,9,-10,4,10,-3,-10,2,5,-5,6,-4,-5,-2,-4,-6,-7,-8,3,1,10,4,-6,7,2,2,6,-1,-4,-5,-9,-5,-8,-3,5,-6,-7,8,-9,-7,-9,-9,4,7,2,-6,-5,-7,-6,-5,6,7,-4,-9,1,3,6,6,-1,-7,7,6,-8,8,-3,4,-4,5,7,-2,1,-10,-7,-8,-3,3,-2,-3,-10,-2,-4,4,-1,-8,4,-9,-5,-5,-7,-1,10,10,1,-10,-6,7,1,10,2,-10,-9,-3,-8,-7,1,-7,1,1,-5,-6,5,3,-5,-6,2,-3,-5,-7,7,9,-3,-9,6,-8,-2,9,10,-1,-4,1,-5,9,3,4,-2,-7,1,-9,5,5,-6,5,8,-8,-5,10,-5,9,-5,-7,-7,-1,-8,5,-10,3,5,-1,-3,5,9,-7,4,-2,10,5,-2,8,-9,-5,1,6,-5,-9,7,6,9,10,-9,2,10,7,-6,-3,-5,-5,-8,4,-9,2,5,1,9,-7,4,8,-9,-7,1,1,8,-4,-8,-10,9,2,-9,-2,-6,7,-10,-3,1,5,10,7,1,-4,2,-3,-5,-7,-10,3,7,4,-6,-6,9,-10,-7,-6,-10,7,-4,3,7,-6,-10,-1,-10,4,-3,6,4,-10,-2,-9,-9,-4,-7,4,8,1,10,7,-8,-7,-3,-5,-6,-8,-3,3,-3,7,-8,4,-3,-6,-6,1,3,-4,-1,-3,-4,-7,10,-1,9,-5,-8,-4,3,-2,-10,2,2,-8,-5,-4,-4,7,3,6,-3,10,9,2,2,2,8,-5,-2,-7,-6,7,2,-3,-2,-8,10,-8,-1,-3,-6,-7,9,-9,7,-7,7,-4,-9,-5,-5,-8,2,-6,-8,-8,-1,3,8,-10,-7,9,-2,4,-9,-2,1,-3,-6,8,7,-10,-4,10,-2,9,9,3,3,3,-6,10,3,-2,4,2,-7,-2,3,3,4,7,1,5,7,10,2,-1,-3,3,3,9,-8,-1,2,-8,-5,10,-5,4,2,7,3,-9,1,6,-9,-3,7,-10,5,5,-5,10,1,-3,-7,9,8,-8,1,-10,8,-7,-7,-6,-7,4,8,-3,9,4,-6,-6,2,-1,8,3,-7,3,-1,8,-9,-1,8,8,8,3,-6,6,3,-10,1,6,-6,-3,5,-7,4,1,-10,9,-2,3,1,3,9,4,-9,-9,9,-3,1,-1,6,7,3,-5,10], dtype = "int16")#candidate|20506|(1404,)|const|int16
const_20507 = relay.const([9,7,7,9,2,-10,2,-7,3,-8,-10,-6,-4,-7,3,6,-2,-2,-4,5,-1,-9,10,5,-4,6,-1,8,-5,8,1,-10,6,-1,4,-8,-3,-9,-3,-8,-9,-4,9,6,4,-4,9,-9,-7,-7,6,-8,-4,-6,3,-5,-10,-5,-10,-3,-8,-1,-10,-5,-1,-7,-10,10,4,-1,9,1,7,-6,-10,1,-5,-4,5,1,-2,4,7,-5,7,-10,-4,-6,1,-7,-5,9,-3,5,4,3,-6,7,-1,6,10,6,1,4,8,-2,-10,-2,-6,8,-3,-6,-7,4,-7,8,8,-1,8,10,-7,-6,3,-7,-5,9,-7,8,-9,-6,3,-6,-5,-10,4,-8,2,5,2,-6,-10,-4,1,-5,-4,-1,-2,-10,5,2,7,10,4,5,-9,4,8,-8,-1,3,3,-6,8,4,5,-3,-5,-2,-8,8,9,-9,-1,-10,-10,-2,5,-8,4,-8,-7,1,-4,3,-1,-9,3,9,-7,-8,2,-9,-10,1,8,-2,10,5,6,6,-8,-8,-5,5,-6,8,-5,-4,-4,8,4,-5,1,10,9,-5,-3,6,-9,-9], dtype = "uint32")#candidate|20507|(220,)|const|uint32
const_20508 = relay.const(-0.550286, dtype = "float32")#candidate|20508|()|const|float32
call_20505 = relay.TupleGetItem(func_17368_call(relay.reshape(const_20506.astype('int16'), [1404,]), relay.reshape(const_20507.astype('uint32'), [220,]), relay.reshape(const_20508.astype('float32'), []), ), 7)
call_20509 = relay.TupleGetItem(func_17373_call(relay.reshape(const_20506.astype('int16'), [1404,]), relay.reshape(const_20507.astype('uint32'), [220,]), relay.reshape(const_20508.astype('float32'), []), ), 7)
func_15709_call = mod.get_global_var('func_15709')
func_15710_call = mutated_mod.get_global_var('func_15710')
call_20521 = relay.TupleGetItem(func_15709_call(), 0)
call_20522 = relay.TupleGetItem(func_15710_call(), 0)
output = relay.Tuple([call_20487,call_20505,const_20506,const_20507,const_20508,call_20521,])
output2 = relay.Tuple([call_20488,call_20509,const_20506,const_20507,const_20508,call_20522,])
func_20532 = relay.Function([], output)
mod['func_20532'] = func_20532
mod = relay.transform.InferType()(mod)
mutated_mod['func_20532'] = func_20532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20532_call = mutated_mod.get_global_var('func_20532')
call_20533 = func_20532_call()
output = call_20533
func_20534 = relay.Function([], output)
mutated_mod['func_20534'] = func_20534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18130_call = mod.get_global_var('func_18130')
func_18131_call = mutated_mod.get_global_var('func_18131')
call_20590 = func_18130_call()
call_20591 = func_18130_call()
func_17073_call = mod.get_global_var('func_17073')
func_17076_call = mutated_mod.get_global_var('func_17076')
var_20595 = relay.var("var_20595", dtype = "float32", shape = (143, 9))#candidate|20595|(143, 9)|var|float32
call_20594 = relay.TupleGetItem(func_17073_call(relay.reshape(var_20595.astype('float32'), [1287,])), 4)
call_20596 = relay.TupleGetItem(func_17076_call(relay.reshape(var_20595.astype('float32'), [1287,])), 4)
func_14486_call = mod.get_global_var('func_14486')
func_14493_call = mutated_mod.get_global_var('func_14493')
var_20598 = relay.var("var_20598", dtype = "float32", shape = (210,))#candidate|20598|(210,)|var|float32
const_20599 = relay.const([7,9,6,-9,10,-6,6,-5,3,2,5,2,4,-1,5,7,4,7,5,2,9,-10,5,5,5,-9,7,8,-1,4,-3,-9,9,6,4,-9,8,-8,-7,1,2,2,-3,5,-9,1,9,6,6,2,-4,2,2,-4,-3,-1,-7,8,-3,-4,-1,-2,-3,-8,2,10,1,-7,2,-2,-8,-3,3,-3,-4,7,-1,6,9,4,4,-9,-6,7,-8,4,-9,-1,10,-1,10,-2,8,5,-1,-1,3,-9,-8,8,5,-4,-10,-1,8,7,-1,-10,-6,-8,-4,-10,-3,-7,-7,-7,-6,9,5,-8,-3,2,3,-2,-9,-6,3,1,6,5,10,8,-4,-3,8,-5,-6,4,10,-10,8,1,5,5,9,-7,-5,-6,3,-9,1,-1,-2,-8,-2,-9,-6,2,-4,3,9,2,-4,-3,10,-9,6,7,6,10,6,6,2,3,7,9,7,-9,2,9,4,2,-9,-9,6,1,-9,-6,-7,6,9,9,9,-7,2,4,6,-7,6,-8,-7,8,9,8,-5,9,2,-9,8,3,-4,7,2,6,1,-4,-4,6,-8,-9,-9,-6,10,1,3,-7,10,8,-7,-1,10,-9,-10,10,-7,1,-9,8,-4,7,-4,4,-10,7,-7,-8,-6,3,-9,-5,4,-4,-5,-4,1,6,-8,1,-5,5,-7,-10,7,-10,-6,3,-3,3,-9,-8,-10,8,-7,6,-7,3,-4,-8,6,-9,5,4,-1,5,-6,2,9,2,9,5,10,2,1,-9,10,-1,4,-10,-2,4,-9,-2,6,-4,3,-3,-7,9,4,5,5,-6,9,3,4,7,-4,2,2,-5,5,-8,-2,8,-4,-10,9,8,-4,9,-8,1,-5,2,-9,4,6,6,-10,3,-7,3,-1,-4,-1,2,9,-3,-8,-6,5,-3,-6,10,3,-10,-8,-8,5,3,5,7,-3,-2,9,-10,-8,5,1,-9,-9,-5,-3,6,-5,6,-6,-5,7,-10,5,-9,4,-6,9,9,6,7,-9,9,-3,5,2,-8,7,-3,9,-5,8,-6,-1,-9,1,8,8,-3,4,10,-7,-5,8,9,2,8,7,8,-1,5,-2,1,2,-1,-1,4,-9,4,-7,-3,-7,8,7,4,-3,-9,1,5,3,4,6,5,7,3,4,-4,8,-7,-9,2,-9,9,2,-5,-7,-2,9,8,-7,-9,-6,-2,-4,-1,1,5,6,-9,-7,5,5,8,-3,9,7,10,2,2,-4,-9,6,-2,9,3,8,-1,-3,9,5,-5,6,8,9,4,-2,-6,-10,-3,2,4,-1,-2,-3,-10,9,-3,-1,4,2,5,4,2,-10,2,10,1,-2,8,6,-4,-3,3,-7,-6,-7,-2,-2,5,-1,5,5,-7,-1,-2,2,3,2,-9,-2,-7,4,2,-6,-8,-5,10,-9,7,-1,8,-5,-9,6,8,-1,-9,-6,2,9,9,-5,4,-8,-5,-1,4,-5,-5,-1,10,-7,8,1,5,4,-4,7,-4,-2,-5,1,1,2,-8,8,-4,9,8,6,10,9,6,3,-10,8,-7,5,-6,1,-10,1,6,10,8,9,-3,-3,4,-8,8,-10,-8,1,3,-7,3,-9,-6,2,2,-3,10,3,-1,-10,10,3,6,1,10,-2,-3,-1,-9,-4,-6,5,4,-2,2,3,-4,9,2,9,5,-6,-4,9,2,4,4,-8,1,3,-3,-5,-3,-7,4,9,-1,10,-2,9,-6,-3,-4,9,2,9,8,-2,-8,-10,-9,4,3,-5,6,-10,9,-3,6,-8,-5,4,1,-8,7,3,-6,5,-4,-6,-4,-3,10,6,1,4,1,1,4,-10,9,6,-4,-5,-1,9,5,-10,1,5,-10,-9,-9,-2,2,-5,-9,6,-3,-2,-2,-4,6,-6,-10,10,-9,4,1,-10,-1,-4,7,-4,1,-7,-10,1,-6,2,5,-7,-2,2,-8,6,7,-8,10,-7,9,-5,6,4,1,10,-9,-10,-10,4,-3,7,-10,6,-8,-4,-8,5,-3,8,4,-9,6,6,2,-4,-10,-6,-6,2,-7,1,5,1,-5,-1,-8,-4,2,10,7,8,3,-8,6,2,-6,1,9,9,-5,-2,3,-7,5,-8,1,2,7,4,-1,1,9,9,5,9,10,-5,9,-7,-1,-1,-10,8,-4,-3,9,2,-7,4,-1,-4,-6,6,-10,4,-10,4,7,-7,4,-3,5,1,-8,-6,9,2,8,5,-10,1,-1,10,-9,-8,-9,8,-6,-8,5,5,-3,-1,4,-2,4,-4,10,-4,1,6,3,-3,-4,-5,-4,-4,7,9,1,6,7,-10,-4,-10,6,-2,-1,-10,-6,3,-7,-9,2,8,1,1,-3,-5,-7,9,-10,-4,8,5,1,5,4,-6,4,-2,-7,-3,3,-7,-2,6,1,-10,-4,-4,2,6,-5,-6,6,6,-2,6,-4,8,3,-7,-1,-3,3,-3,9,2,-2,5,-8,-5,-9,-6,6,-10,-5,3,-5,3,6,-2,5,-8,-4,-7,5,3,-3,-6,4,-9,-2,-6,-9,-4,5,9,-2,7,2,-8,-5,1,-3,-8,3,-5,10,-2,10,-5,2,5,2,9,5,1,2,8,10,-10,3,-8,7,-3,7,-2,-1,2,8,-7,3,-2,1,8,-8,-4,6,-4,-3,-9,-3,9,7,-7,-7,9,10,4,-5,-3,-3,-4,9,1,2,-4,3,1,9,7,10,-5,-9,-4,-1,5,-5,2,-6,-8,5,5,7,9,4,9,10,-6,3,1,-8,6,5,9,-5,10,-1,9,3,-2,-2,10,-7,2,6,-3,-2,-8,-9,10,4,-3,7,2,9,-6,7,2,-10,-5,10,1,-7,8,-5,-9,10,-3,3,8,9,3,-8,1,1,-6,-2,-10,-5,-4,-9,-9,-6,-8,10,-10,-10,7,10,-7,4,2,10,6,2,-6,-4,4,9,-8,7,-8,-3,-6,2,3,-9,-3,-7,-4,8,4,7,1,-9,5,-9,5,-9,-4,-6,-7,2,-4,9,-9,-8,-9,10,-10,-1,7,7,5,-4,-7,7,-3,-5,7,-5,-1,1,7,-3,10,-2,-5,8,-7,8,1,1,4,3,2,-10,-10,-6,-2,-3,-3,7,6,-8,8,-6,-3,4,-4,1,-2,10,3,8,3,6,-6,3,-10,2,1,6,-8,-3,5,8,-8,1,4,-7,-9,-2,7,7,-10,-5,1,-7,2,-1,6,6,8,5,5,9,-4,2,-10,-9,10,-9,5,-9,-8,6,10,7,-9,9,4,-9,3,-2,-10,1,-6,10,8,10,10,9,-8,-7,1,-1,6,-5,-1,1,-9,3,3,-7,-5,-7,3,-6,-10,-5,10,8,-6,-6,10,-2,8,-4,-1,3,8,-2,4,9,10,7,-2,10,7,-8,-3,-8,6,-3,-3,-2,6,1,9,-8,-7,-2,1,6,-6,-7,-3,-2,-8,-5,-1,1,10,-1,-5,-9,-3,9,1,-4,-10,-7,-7,-3,4,-6,-6,4,3,4,-4,8,3,3,-5,-4,9,9,10,1,-3,-9,-7,6,2,-8,4,-6,-5,3,-6,-6,-10,-3,8,-4,-2,-9,-8,9,-4,6,4,7,1,-9,8,-3,10,-7,-9,-9,-4,2,-5,3,9,-9,1,2,5,2,9,-10,-1,-9,-9,-3,-1,6,9,7,-9,1,-2,6], dtype = "int16")#candidate|20599|(1404,)|const|int16
var_20600 = relay.var("var_20600", dtype = "int64", shape = (546,))#candidate|20600|(546,)|var|int64
const_20601 = relay.const([[-8.073664,-2.533049,-3.357086,5.060627],[-0.330646,9.403802,7.838181,2.651833],[5.849932,0.403912,9.357531,2.828578],[-9.622843,-9.855486,9.370744,-1.452255],[-0.036492,-6.453910,-1.536961,1.329958],[-8.575607,4.043653,0.655984,9.278850],[-0.286108,7.585561,6.147262,-7.280822],[9.286038,-5.535925,3.902880,-3.323334],[4.770843,-0.638365,-8.229788,5.168423],[-7.573781,-4.750173,0.334794,-9.747621],[-2.799580,-0.135134,-6.296893,-5.749745],[0.040756,1.010758,4.733748,-0.058087],[-8.993723,4.478086,2.058282,3.549926],[2.701533,7.587185,9.095727,-3.268999],[8.986621,9.043455,9.949550,5.398303],[2.640374,6.052799,-6.673329,3.611851],[-6.976318,1.786040,1.474671,7.067408],[-0.623789,-8.070773,7.530525,-2.722056],[7.684894,-7.617251,5.887698,7.653404],[-1.487549,7.551081,-6.905068,1.482080],[0.486067,-6.635870,6.006509,7.013101],[-5.417800,-0.569812,-3.865218,-7.328329],[-7.843951,5.308986,-6.508968,-9.152253],[4.110278,3.265150,1.619492,6.192473],[9.728684,7.968347,8.997411,4.204466],[-2.799936,3.759786,-7.000923,-0.073765],[7.328687,-7.288409,-8.760130,-6.966978],[-5.813666,-7.631767,8.018819,3.329810],[1.642810,4.196877,1.856814,6.297559],[-4.516349,2.103921,-4.645229,-5.095038],[0.614169,-5.725670,8.030632,9.638457],[-7.810305,9.383761,8.950122,5.483753],[-3.276197,-0.274236,2.192956,3.484211],[-6.952304,-1.600802,7.072404,-8.152082],[6.708162,-6.374898,-1.610516,-6.442967],[2.718669,-5.874820,-7.014991,-9.220537],[-1.931864,6.966208,-1.764465,-1.317420],[4.753669,9.971734,9.068723,7.510422],[-3.189165,8.968557,4.029666,-0.156188],[-8.898629,-6.274836,-9.065868,6.727461],[9.023373,-9.039959,9.532209,-4.007941],[8.295511,0.728488,-1.690664,7.148263],[0.175558,2.951943,-3.336260,3.327592],[-2.701007,-9.290156,-7.036307,9.109686],[-9.228666,9.731886,-5.092882,-8.146725],[-2.707776,-1.556522,-6.173404,3.499473],[2.369496,-4.382044,-1.365695,-6.039679],[4.166937,0.953221,-4.923582,8.718453],[-9.002889,-4.768271,3.896523,-7.631885],[7.882305,-0.175555,-0.678795,6.641840],[-3.646360,-5.031377,5.592773,5.592578],[7.217711,0.919764,6.936112,-4.422948],[5.624543,4.380100,8.458150,-0.024417],[-0.487677,-8.740637,5.154207,-7.902970],[3.142652,-3.151760,8.562951,-0.150381],[0.471084,-2.574765,-6.130540,-7.606104],[-5.631344,-3.931554,-0.697046,-1.389265],[7.664252,7.527491,-0.769540,-4.678173],[-9.614141,-0.934718,-0.406271,-5.288469],[-6.577039,7.130884,7.389165,0.164973],[6.252667,0.012522,-1.406762,-1.460302],[-8.379230,-8.348222,-5.193354,1.373759],[-0.473777,-5.514000,-4.631612,-8.128585],[-3.638876,1.039421,3.353830,8.808012],[5.550402,-5.568189,-9.393240,4.219034],[6.202501,2.103859,6.506701,-9.977306],[-6.309483,-3.129314,-5.298399,-0.402572],[-4.916859,-8.652691,-2.630631,-9.355378],[8.776419,4.266750,-5.611563,-8.390778],[3.607345,5.294065,-5.031720,-1.003690],[-9.782989,4.621726,6.377137,2.592958],[-8.501979,4.153628,6.769154,-2.833739],[0.383930,-0.310420,-3.985606,4.820328],[-3.603480,-7.511128,-4.443524,-4.774776],[-7.686081,1.755998,5.455220,6.443103],[7.712125,-4.523628,9.072894,7.094014],[-9.152257,-5.651179,-2.922142,-4.793739],[-4.325916,-0.943371,3.073056,0.816130],[-4.582114,6.379711,-8.330007,1.620978],[-8.779685,-7.046614,-6.343529,-9.829789],[-8.358959,-3.652175,-3.623357,8.991153],[2.037657,1.585515,-8.949116,-0.761043],[-3.425644,-0.636448,6.443160,-1.305038],[5.368859,4.987333,-6.569850,1.188415],[-8.774159,7.975058,-0.987777,3.001112],[-5.546370,8.136826,4.808816,-3.063178],[1.261593,-8.974756,-9.584608,-1.566716],[-0.925161,-5.860519,7.936918,8.351357],[9.569768,-9.945664,2.873050,2.687684],[6.688262,1.319747,8.124449,-2.946232],[-9.336161,7.101591,6.972734,6.439872]], dtype = "float64")#candidate|20601|(91, 4)|const|float64
const_20602 = relay.const([[-10,-4,-2,10,-3,-6,3,5,-7,-5,6,2,-5,9,-10,7,-4,8,10,-1,-4,-1,1,6,5,-2,7,9,2,7,9,-3,-7,-10,-7,-9,9,10,8,-8,9,-1,6,10,10,-2,-1,3,-4,-4,-7,3,-1,-4,1,1,3,-6,-4,1,-6,-4,-7,-7,-3,3,-2,-3,-1,3,10,2,7,-6,-6,8,7,-3,10,-7,-10,2,7,6,-2,-10,6,10,9,8,-1,1,10,-4,3,5,2,-5,3,-8,4,-9,-1,-6,5,10,-10,-7,3,1,3,-9,-3,7,-8,3,5,2,3,8,2,5,9,10,-3,9,-7,2,-5,-8,-6,-6,-6,-6,-6,6,-4,-8,3,4,1,2,4,-1,-3,-1,-1,9,-5,6,-3,1,-5,8,-9,2,8,9,7,10,-1,10,-7,-1,6,-6,-2,-4,-6,-5,-9,-6,-2,-8,6,-9,-8,-1,8,9,-1,-10,-2,2,-9,2,7,-4,4,7,9,-9,7,-3,-1,-8,7,-7,-4,-6,7,8,7,-2,5,3,5,2,3,6,10,-6,2,8,2,7,-4,-3,1,6,-3,10,2,-10,9,-8,-10,8,10,7,9,-1,-3,6,2,-7,-10,4,9,8,2,7,-10,5,10,-2,-8,-4,1,-2,-3,-7,6,-6,7,-4,-9,2,-9,-1,-9,-10,10,-5,-5,4,-7,-10,4,9,9,2,-8,7,-1,6,1,-6,-9,2,9,-9,-6,-1,-4,-2,6,1,6,3,6,9,7,-10,8,10,7,4,-10,-4,5,-9,7,9,10,3,3,-5,7,7,-9,-5,-10,-10,3,-9,7,3,10,9,6,-5,-6,-9,8,-10,-7,-3,-3,-9,6,-7,6,9,4,3,2,10,8,2,-7,3,5,-3,9,-5,8,8,-5,-7,6,8,-9,5,8,-5,8,-1,4,-3,5,-7,-3,-6,-3,5,6,7,-4,3,10,8,-6,4,4,6,-7,-2,-10,-7,5,2,7,-5,2,6,-5,-3,-5,4,4,9,-3,-2,-3,-5,10,8,-7,-2,-2,-4,-3,2,5,9,6,-1,-3,1,1,-2,5,2,-6,4,3,7,-4,5]], dtype = "uint32")#candidate|20602|(1, 420)|const|uint32
call_20597 = relay.TupleGetItem(func_14486_call(relay.reshape(var_20598.astype('float32'), [210,]), relay.reshape(const_20599.astype('int16'), [1404,]), relay.reshape(var_20600.astype('int64'), [546,]), relay.reshape(const_20601.astype('float64'), [364,]), relay.reshape(const_20602.astype('uint32'), [420,]), ), 0)
call_20603 = relay.TupleGetItem(func_14493_call(relay.reshape(var_20598.astype('float32'), [210,]), relay.reshape(const_20599.astype('int16'), [1404,]), relay.reshape(var_20600.astype('int64'), [546,]), relay.reshape(const_20601.astype('float64'), [364,]), relay.reshape(const_20602.astype('uint32'), [420,]), ), 0)
func_16184_call = mod.get_global_var('func_16184')
func_16187_call = mutated_mod.get_global_var('func_16187')
var_20611 = relay.var("var_20611", dtype = "bool", shape = (528,))#candidate|20611|(528,)|var|bool
call_20610 = relay.TupleGetItem(func_16184_call(relay.reshape(var_20611.astype('bool'), [528,]), relay.reshape(const_20599.astype('int16'), [1404,]), ), 5)
call_20612 = relay.TupleGetItem(func_16187_call(relay.reshape(var_20611.astype('bool'), [528,]), relay.reshape(const_20599.astype('int16'), [1404,]), ), 5)
output = relay.Tuple([call_20590,call_20594,var_20595,call_20597,var_20598,const_20599,var_20600,const_20601,const_20602,call_20610,var_20611,])
output2 = relay.Tuple([call_20591,call_20596,var_20595,call_20603,var_20598,const_20599,var_20600,const_20601,const_20602,call_20612,var_20611,])
func_20633 = relay.Function([var_20595,var_20598,var_20600,var_20611,], output)
mod['func_20633'] = func_20633
mod = relay.transform.InferType()(mod)
var_20634 = relay.var("var_20634", dtype = "float32", shape = (143, 9))#candidate|20634|(143, 9)|var|float32
var_20635 = relay.var("var_20635", dtype = "float32", shape = (210,))#candidate|20635|(210,)|var|float32
var_20636 = relay.var("var_20636", dtype = "int64", shape = (546,))#candidate|20636|(546,)|var|int64
var_20637 = relay.var("var_20637", dtype = "bool", shape = (528,))#candidate|20637|(528,)|var|bool
output = func_20633(var_20634,var_20635,var_20636,var_20637,)
func_20638 = relay.Function([var_20634,var_20635,var_20636,var_20637,], output)
mutated_mod['func_20638'] = func_20638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16840_call = mod.get_global_var('func_16840')
func_16842_call = mutated_mod.get_global_var('func_16842')
call_20715 = func_16840_call()
call_20716 = func_16840_call()
output = call_20715
output2 = call_20716
func_20728 = relay.Function([], output)
mod['func_20728'] = func_20728
mod = relay.transform.InferType()(mod)
mutated_mod['func_20728'] = func_20728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20728_call = mutated_mod.get_global_var('func_20728')
call_20729 = func_20728_call()
output = call_20729
func_20730 = relay.Function([], output)
mutated_mod['func_20730'] = func_20730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17024_call = mod.get_global_var('func_17024')
func_17025_call = mutated_mod.get_global_var('func_17025')
call_20762 = relay.TupleGetItem(func_17024_call(), 0)
call_20763 = relay.TupleGetItem(func_17025_call(), 0)
output = call_20762
output2 = call_20763
func_20777 = relay.Function([], output)
mod['func_20777'] = func_20777
mod = relay.transform.InferType()(mod)
output = func_20777()
func_20778 = relay.Function([], output)
mutated_mod['func_20778'] = func_20778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18576_call = mod.get_global_var('func_18576')
func_18577_call = mutated_mod.get_global_var('func_18577')
call_20810 = func_18576_call()
call_20811 = func_18576_call()
output = call_20810
output2 = call_20811
func_20859 = relay.Function([], output)
mod['func_20859'] = func_20859
mod = relay.transform.InferType()(mod)
output = func_20859()
func_20860 = relay.Function([], output)
mutated_mod['func_20860'] = func_20860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20327_call = mod.get_global_var('func_20327')
func_20329_call = mutated_mod.get_global_var('func_20329')
call_20878 = func_20327_call()
call_20879 = func_20327_call()
output = call_20878
output2 = call_20879
func_20884 = relay.Function([], output)
mod['func_20884'] = func_20884
mod = relay.transform.InferType()(mod)
mutated_mod['func_20884'] = func_20884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20884_call = mutated_mod.get_global_var('func_20884')
call_20885 = func_20884_call()
output = call_20885
func_20886 = relay.Function([], output)
mutated_mod['func_20886'] = func_20886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18261_call = mod.get_global_var('func_18261')
func_18263_call = mutated_mod.get_global_var('func_18263')
call_20895 = relay.TupleGetItem(func_18261_call(), 1)
call_20896 = relay.TupleGetItem(func_18263_call(), 1)
output = relay.Tuple([call_20895,])
output2 = relay.Tuple([call_20896,])
func_20947 = relay.Function([], output)
mod['func_20947'] = func_20947
mod = relay.transform.InferType()(mod)
mutated_mod['func_20947'] = func_20947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20947_call = mutated_mod.get_global_var('func_20947')
call_20948 = func_20947_call()
output = call_20948
func_20949 = relay.Function([], output)
mutated_mod['func_20949'] = func_20949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16719_call = mod.get_global_var('func_16719')
func_16720_call = mutated_mod.get_global_var('func_16720')
call_21028 = relay.TupleGetItem(func_16719_call(), 0)
call_21029 = relay.TupleGetItem(func_16720_call(), 0)
func_3810_call = mod.get_global_var('func_3810')
func_3813_call = mutated_mod.get_global_var('func_3813')
var_21038 = relay.var("var_21038", dtype = "float32", shape = ())#candidate|21038|()|var|float32
var_21039 = relay.var("var_21039", dtype = "float32", shape = (588,))#candidate|21039|(588,)|var|float32
call_21037 = func_3810_call(relay.reshape(var_21038.astype('float32'), []), relay.reshape(var_21039.astype('float32'), [14, 14, 3]), )
call_21040 = func_3810_call(relay.reshape(var_21038.astype('float32'), []), relay.reshape(var_21039.astype('float32'), [14, 14, 3]), )
output = relay.Tuple([call_21028,call_21037,var_21038,var_21039,])
output2 = relay.Tuple([call_21029,call_21040,var_21038,var_21039,])
func_21045 = relay.Function([var_21038,var_21039,], output)
mod['func_21045'] = func_21045
mod = relay.transform.InferType()(mod)
var_21046 = relay.var("var_21046", dtype = "float32", shape = ())#candidate|21046|()|var|float32
var_21047 = relay.var("var_21047", dtype = "float32", shape = (588,))#candidate|21047|(588,)|var|float32
output = func_21045(var_21046,var_21047,)
func_21048 = relay.Function([var_21046,var_21047,], output)
mutated_mod['func_21048'] = func_21048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18576_call = mod.get_global_var('func_18576')
func_18577_call = mutated_mod.get_global_var('func_18577')
call_21078 = func_18576_call()
call_21079 = func_18576_call()
func_14486_call = mod.get_global_var('func_14486')
func_14493_call = mutated_mod.get_global_var('func_14493')
const_21111 = relay.const([-9.728069,-1.183217,1.469390,6.312848,-1.111244,2.598003,9.363342,1.517698,4.810015,7.288128,6.571026,0.444778,3.517307,5.818320,-4.440887,-4.487869,8.709347,-5.326246,7.087396,-0.203867,6.523148,6.154012,-6.337299,-4.050110,-6.157918,-5.821969,-7.116380,1.154885,-9.790942,-4.643957,-6.067399,4.453578,-2.036034,-7.444163,-6.705904,1.953625,-7.228231,-2.148548,1.964067,6.893041,-7.612427,-2.104465,1.880200,-0.149097,-2.807197,-0.188990,2.628065,7.015582,0.031101,8.855021,-3.046935,3.883539,-8.309134,5.425255,9.751808,4.874011,-5.954974,-9.482702,9.498732,-2.393138,-8.776378,3.503044,-5.819640,2.889009,-2.387557,6.296765,3.797186,-8.506687,-4.098721,-7.416451,-5.523908,4.050209,4.409109,-4.570433,-3.850676,-3.541551,-5.989637,-9.021246,-7.935226,-7.230792,6.173488,-2.959234,8.839168,-4.010411,-0.222789,7.507342,-5.101516,-1.456478,-4.478623,-9.987430,4.141219,7.272445,-9.556451,-0.569354,8.940094,-8.655700,7.852144,-5.812956,4.901115,-3.941988,6.983821,-8.847683,9.361492,9.595646,1.506408,-7.551934,-3.982291,-6.982156,-1.982256,-6.759114,-3.705301,-9.507982,8.138531,-0.466574,5.235784,-1.544334,-3.420676,-8.112876,5.921326,0.478714,3.705931,7.188892,-1.820714,4.136529,6.046232,-2.355743,-1.509952,5.302827,4.166175,-0.680009,-0.681523,4.368978,4.671363,-5.792768,0.788222,5.497845,-7.992090,6.588509,5.265271,5.115616,-4.569180,-9.567247,-2.922453,-5.833268,3.663466,-0.565582,3.727820,-1.445870,3.228998,-1.094205,-8.151063,5.571872,-2.423074,7.628563,4.484506,-0.960833,3.397428,-5.642328,-9.036685,7.599397,9.734220,-8.126668,-7.745283,8.017225,4.513640,-7.449668,-1.306868,-9.169056,-6.685421,-3.828487,-3.881693,4.637849,0.824961,4.627827,-7.496421,5.344640,-9.326450,1.443228,-9.347901,-1.682956,-5.986021,0.996196,1.753243,2.358077,-1.841377,1.001645,4.852924,-3.440452,0.609998,-4.710062,-4.254610,2.605141,9.091717,7.023467,-7.074248,-7.788068,5.695087,0.893393,0.070316,-7.468010,-8.433063,3.622971,7.745623,-3.576950,9.341913,-9.342771,-5.636830,1.004209,-1.461024,1.940586], dtype = "float32")#candidate|21111|(210,)|const|float32
var_21112 = relay.var("var_21112", dtype = "int16", shape = (1404,))#candidate|21112|(1404,)|var|int16
const_21113 = relay.const([[2,2],[3,1],[6,6],[-3,9],[5,-3],[-4,-3],[8,-5],[10,9],[-1,4],[-3,-7],[6,8],[-6,3],[3,-8],[6,1],[3,-1],[9,5],[-3,3],[-5,-2],[6,10],[-8,-5],[10,-9],[7,2],[-8,-3],[5,9],[8,-1],[-2,1],[4,4],[-6,-3],[4,-3],[-2,1],[10,-8],[-3,-10],[-9,-1],[5,-1],[-5,8],[-3,8],[-1,-8],[-7,-4],[6,-1],[-1,7],[1,2],[-4,-2],[-9,-2],[1,2],[4,6],[3,-8],[4,-6],[-10,4],[5,-7],[9,7],[2,-2],[1,7],[-6,-9],[-5,-5],[-8,-1],[-8,-10],[-10,-1],[8,9],[-9,-5],[5,-6],[-6,-9],[1,7],[9,-8],[2,-9],[8,-3],[5,-8],[-3,5],[-4,-10],[-7,9],[-6,-9],[-4,-1],[8,-3],[7,-3],[-8,-9],[4,2],[8,-8],[4,4],[6,7],[4,-10],[-8,-9],[7,-1],[2,7],[-7,-4],[2,1],[1,-5],[1,-9],[-10,7],[2,-4],[7,5],[7,-5],[-2,9],[-3,9],[8,-3],[4,3],[-2,1],[-8,2],[-2,3],[10,6],[-9,7],[5,-7],[8,1],[-5,5],[9,-1],[2,-10],[-2,-4],[3,8],[4,3],[1,-4],[2,-10],[-4,-4],[2,-7],[1,-9],[-4,-7],[4,8],[-1,9],[3,-1],[-1,-3],[8,7],[3,6],[-5,6],[9,-4],[-1,1],[5,5],[5,6],[9,-2],[-5,10],[-3,1],[-1,-7],[4,-3],[6,-8],[6,-3],[-1,9],[-6,-10],[-10,-8],[-7,2],[10,8],[1,-9],[-7,-9],[2,6],[-9,-5],[5,-6],[4,-7],[5,-8],[-7,8],[-8,-4],[-4,8],[3,9],[-8,-6],[10,8],[-8,-4],[4,-9],[-8,10],[4,1],[-7,3],[-2,3],[-7,-4],[3,-10],[7,-5],[7,6],[8,3],[2,-9],[-2,10],[-7,3],[3,2],[9,8],[-9,9],[-6,-3],[-2,8],[10,-2],[2,-4],[4,4],[5,3],[9,10],[-4,-5],[-7,-7],[-5,-1],[-2,7],[5,-4],[3,6],[5,1],[-1,-3],[-3,5],[7,7],[7,-8],[2,-3],[-1,8],[5,1],[3,4],[-5,9],[7,6],[-6,-9],[2,1],[5,1],[-1,9],[2,5],[-3,9],[8,-4],[2,1],[2,2],[-9,7],[7,1],[8,-3],[1,-4],[-9,-10],[1,-3],[3,-4],[6,-8],[8,-9],[5,2],[-10,-4],[5,5],[10,-10],[-1,-7],[-9,-1],[6,-7],[7,1],[6,5],[-10,-8],[6,-6],[1,1],[-1,6],[9,2],[-7,2],[-5,-7],[-8,-8],[3,1],[9,8],[-7,10],[9,-7],[-3,6],[10,-5],[-2,-5],[-9,9],[8,1],[-1,-5],[-10,-6],[1,7],[-2,4],[-2,-6],[-5,7],[5,4],[-9,-9],[6,9],[-9,4],[10,-3],[-6,-4],[-10,-5],[3,-7],[-1,10],[-7,-10],[-2,-10],[-6,2],[6,8],[-2,2],[-3,7],[8,-4],[6,-9],[-2,-8],[10,9],[2,3],[5,-2],[6,-1],[1,-4],[-1,-8],[-2,-9],[-7,-3],[5,-2],[1,7],[-9,-7],[4,-3],[-7,4],[5,4],[-10,-2]], dtype = "int64")#candidate|21113|(273, 2)|const|int64
var_21114 = relay.var("var_21114", dtype = "float64", shape = (7, 52))#candidate|21114|(7, 52)|var|float64
var_21115 = relay.var("var_21115", dtype = "uint32", shape = (10, 42))#candidate|21115|(10, 42)|var|uint32
call_21110 = relay.TupleGetItem(func_14486_call(relay.reshape(const_21111.astype('float32'), [210,]), relay.reshape(var_21112.astype('int16'), [1404,]), relay.reshape(const_21113.astype('int64'), [546,]), relay.reshape(var_21114.astype('float64'), [364,]), relay.reshape(var_21115.astype('uint32'), [420,]), ), 7)
call_21116 = relay.TupleGetItem(func_14493_call(relay.reshape(const_21111.astype('float32'), [210,]), relay.reshape(var_21112.astype('int16'), [1404,]), relay.reshape(const_21113.astype('int64'), [546,]), relay.reshape(var_21114.astype('float64'), [364,]), relay.reshape(var_21115.astype('uint32'), [420,]), ), 7)
func_14593_call = mod.get_global_var('func_14593')
func_14595_call = mutated_mod.get_global_var('func_14595')
const_21118 = relay.const([0.605096,-0.464411,0.328665,-8.873490,-2.454305,9.286586,-0.801420,7.721614,3.215289,-5.203256,-2.662024,8.852166,-7.240789,-7.125546,-2.847921,-5.628725,9.195449,-8.568251,9.774387,8.444052,4.507932,-5.512294,-4.598469,-0.247718,-4.163660,-3.606949,-5.151981,-2.200864,9.095564,9.163135,-1.836765,4.453869,-1.651097,9.302154,8.873073,9.612068,0.591316,-7.741620,-6.224514,-7.008372,7.876183,5.756287,-3.686443,2.484112,0.127539,-9.492660,-8.734197,3.878905,1.646882,8.552877,5.975866,6.037876,-8.108799,-1.756155,-5.188996,5.217048,-4.966297,4.303788,-0.411571,-2.191668,2.051945,-7.262900,-5.645934,8.961853,-3.100930,-6.937301,4.426912,-9.785321,-1.969107,-1.028736,8.911579,-5.585300,8.009945,7.328535,-9.199841,4.101670,-2.957555,-1.514603,2.012152,-1.075259,-0.697860,-2.848741,-2.322801,2.306293,1.267426,6.518537,-9.285670,-7.333726,4.128624,5.672850,8.383352,-6.463111,-1.693282,0.355005,-9.416726,8.768301,-6.149137,-5.937942,5.576375,6.482639,-8.642329,4.102365,6.713493,-9.114190,7.180551,-3.648507,-9.502315,-9.340087,0.502067,-1.867465,4.904470,-4.701260,9.477461,-2.315659,4.482941,-1.823352,-7.217214,-3.274364,8.031527,3.929373,-9.041473,-0.437976,-4.865416,-0.252568,-8.454681,1.928083,-6.605569,3.414856,-9.217519,-5.261732,-0.259127,6.595055,1.086885,-3.955748,-8.262525,0.732180,9.025013,8.037621,6.934600,-3.269211,9.607146,0.615004,7.128322,3.208441,8.002379,2.596931,-7.725342,-1.155099,-0.247695,8.895785,-1.500164,-6.084061,-2.731908,4.418390,2.658819,6.397207,6.856773,-1.470065,1.658606,8.349093,-5.822427,-8.500267,4.697276,-6.329892,1.912732,1.420313,-9.853466,-7.049064,9.185197,-8.452863,8.678559,1.609861,6.243383,2.745522,-5.599705,0.241589,-9.007436,8.218988,-1.653684,3.660453,1.813283,-9.069628,-6.584311,-7.933496,-6.830749,-4.028302,-2.570943,5.462750,-9.685137,3.848417,0.266494,7.328562,-3.925437,3.310547,-8.826545,2.989152,7.907089,0.978241,-6.379688,-3.719347,8.129392,-6.537385,-4.020282,9.280213,-8.174736,9.727940,8.313169,9.978033,-8.370917,-6.840553,-6.349161,-3.834454,6.136136,7.444838,-6.928904,5.963237,6.428167,0.667043,0.646931,-5.448672,6.701204,7.720538,-8.342344,9.355153,0.615012,8.747787,1.915183,-8.605002,5.112928,-8.845682,9.944820,6.447932,9.628470,-1.893741,6.553303,-3.912244,6.558573,5.424129,4.229448,-5.587693,4.914491,-2.231895,2.719043,9.867421,-2.093171,-5.352148,4.817058,-9.143087,2.133783,1.207560,3.687869,4.528334,2.279537,-0.856964,4.170471,-9.876738,-3.297445,8.373439,5.084438,6.133109,-1.555343,9.215254,9.643292,-3.897241,-8.981963,-0.402669,-2.466126,-2.563091,-0.363624,-9.864824,1.479858,-7.715195,8.259466,-5.251365,7.049160,-4.686655,8.624688,7.889938,-0.269774,5.585900,-4.109828,-5.453231,-4.068912,-6.581139,-4.238993,-8.552866,4.987414,7.256142,3.025654,9.451313,2.786343,-3.070571,8.258036,-3.452581,-9.171840,7.196926,3.189385,4.656082,-6.001487,-2.788144,-7.425831,8.091900,-3.748319,-4.694965,-9.875233,-7.054190,5.830091,-2.499383,-3.828002,-7.735805,4.487481,1.539829,-7.717351,-9.268686,0.977819,5.009146,9.733550,0.470026,9.555393,7.312722,-1.523135,-2.226708,3.562014,-5.459350,1.859831,-9.783873,-1.750548,4.712948,-2.409368,-3.026329,-1.117711,4.621237,-9.795887,7.082603,-2.559319,6.906030,-6.660473,-9.934795,-8.161270,-5.635740,-8.413867,-7.734827,-5.734444,4.969448,5.201661,-3.737780,3.814987,-9.123448,9.419492,2.985726,-4.118602,-3.679500,-7.965051,-9.796385,9.777158,-0.980893,6.171012,4.074718,-7.466658,-5.385718,-0.571123,-2.255599,-2.320495,2.257905,-7.121186,7.225764,3.168188,-5.950190,4.104199,-4.247746,2.184403,-4.887969,-8.544812,-3.733657,-4.877630,-3.929003,-9.308045,-9.289769,1.840636,-5.224073,-5.082459,5.896669,0.898387,-0.384719,-8.742418,9.617434,7.021692,6.451258,9.220297,0.661895,-0.273355,-4.268500,-0.851035,-4.292975,-1.162634,0.914437,-4.208005,-2.849120,-5.674120,-4.931623,-3.270246,-2.103803,4.054894,1.296484,-6.938463,-9.480373,-7.113728,1.631606,5.621054,4.128867,-1.710310,7.583720,9.809481,-5.515371,-6.836369,-2.950156,-8.797188,-5.643530,-8.217409,1.881339,-0.218911,-4.158579,-4.030681,1.696917,8.100886,-0.589196,-5.418252,-2.580059,7.290366,9.128585,-2.865575,-0.344861,7.800599,-4.297116,-7.694149,-6.800714,-3.432009,-5.176027,-6.671632,-5.436595,-6.011292,2.932476,-6.178074,-9.206814,-1.614395,3.596922,8.051912,1.498487,1.594215,5.116969,9.988664,-4.159198,-8.042906,1.250808,5.921055,-8.565061,-2.170649,-8.281207,1.213001,-5.983520,-9.720287,-3.922426,-0.859979,-4.478337,-2.937908,9.770572,3.825985,2.010685,-6.334367,-5.739820,-0.269028,5.878138,-0.473728,-3.530410,-2.783881,4.746794,-8.713574,6.191052,-2.129283,-3.090701,9.877766,-1.616952,-1.219527,-1.659688,-2.647341,-9.169265,0.874245,7.785415,2.101891,2.268733,9.850783,-3.606739,1.710248,-3.682780,-3.734068,-2.670811,-1.281711,-2.818112,-4.019033,-6.053448,-0.283264,7.622025,-5.405021,2.987778,-4.303096,-0.840463,-4.833889,-8.398154,-0.863059,0.059814,5.073194,-3.097478,-1.144753,-7.383833,8.189640,-5.679483,8.552334,9.462463,-2.074712,1.035320,7.277840,-0.125912,6.072750,0.709827,0.090348,-3.634633,-2.665556,9.129018,1.775637,6.856800,-5.570858,-9.684186,-3.631964,4.979641,4.997494,2.436699,-7.139451,-8.557848,-5.811684,3.792846,-9.305188,8.574560,-8.260467,9.920574,-4.147200,-5.414404,-8.115134,5.076885,-8.054684,-6.907160,2.959501,6.592242,4.500605,5.229021,8.310484,-7.612952,-0.419102,0.786765,-9.237681,5.046284,6.243832,8.420382,-6.186622,-4.051239,4.843863,-5.368826,9.542184,1.587581,4.329083,-4.640964,0.543214,-9.505820,-1.441649,0.586078,7.759711,-3.024733,-0.657850,-7.147265,-7.101192,-8.028257,6.842143,-9.867264,-8.099122,-2.972883,4.931568,-4.527993,4.511335,-8.735018], dtype = "float32")#candidate|21118|(588,)|const|float32
call_21117 = relay.TupleGetItem(func_14593_call(relay.reshape(const_21118.astype('float32'), [588,])), 2)
call_21119 = relay.TupleGetItem(func_14595_call(relay.reshape(const_21118.astype('float32'), [588,])), 2)
func_20118_call = mod.get_global_var('func_20118')
func_20119_call = mutated_mod.get_global_var('func_20119')
call_21125 = func_20118_call()
call_21126 = func_20118_call()
func_17952_call = mod.get_global_var('func_17952')
func_17954_call = mutated_mod.get_global_var('func_17954')
call_21129 = relay.TupleGetItem(func_17952_call(relay.reshape(var_21112.astype('int16'), [1404,])), 3)
call_21130 = relay.TupleGetItem(func_17954_call(relay.reshape(var_21112.astype('int16'), [1404,])), 3)
bop_21136 = relay.logical_xor(var_21114.astype('uint64'), relay.reshape(call_21110.astype('uint64'), relay.shape_of(var_21114))) # shape=(7, 52)
bop_21139 = relay.logical_xor(var_21114.astype('uint64'), relay.reshape(call_21116.astype('uint64'), relay.shape_of(var_21114))) # shape=(7, 52)
output = relay.Tuple([call_21078,const_21111,var_21112,const_21113,var_21115,call_21117,const_21118,call_21125,call_21129,bop_21136,])
output2 = relay.Tuple([call_21079,const_21111,var_21112,const_21113,var_21115,call_21119,const_21118,call_21126,call_21130,bop_21139,])
func_21143 = relay.Function([var_21112,var_21114,var_21115,], output)
mod['func_21143'] = func_21143
mod = relay.transform.InferType()(mod)
mutated_mod['func_21143'] = func_21143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21143_call = mutated_mod.get_global_var('func_21143')
var_21145 = relay.var("var_21145", dtype = "int16", shape = (1404,))#candidate|21145|(1404,)|var|int16
var_21146 = relay.var("var_21146", dtype = "float64", shape = (7, 52))#candidate|21146|(7, 52)|var|float64
var_21147 = relay.var("var_21147", dtype = "uint32", shape = (10, 42))#candidate|21147|(10, 42)|var|uint32
call_21144 = func_21143_call(var_21145,var_21146,var_21147,)
output = call_21144
func_21148 = relay.Function([var_21145,var_21146,var_21147,], output)
mutated_mod['func_21148'] = func_21148
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21165 = relay.var("var_21165", dtype = "float32", shape = (13, 13, 7))#candidate|21165|(13, 13, 7)|var|float32
uop_21166 = relay.sinh(var_21165.astype('float32')) # shape=(13, 13, 7)
func_19367_call = mod.get_global_var('func_19367')
func_19370_call = mutated_mod.get_global_var('func_19370')
const_21170 = relay.const([6.957137,-1.109113,4.026639,7.757083,-7.161036,2.066858,-9.236015,9.245790,3.028907,-9.106679,7.469024,8.647540,-5.909452,-7.058725,9.029815,-2.231337,-6.724144,6.661565,5.712843,6.854902,6.166037,-9.399917,-9.867275,-1.814478,3.717787,-6.524672,-8.034600,-5.707087,-0.301498,-4.922436,4.545989,-8.146933,-1.951987,7.081029,6.669862,0.152359,-3.311751,-5.461500,0.767520,-7.423682,-4.422954,-5.218513,-2.013113,7.555213,5.076107,-0.484717,-7.489491,6.970101,5.517084,-3.102940,8.084787,9.159150,-0.558193,3.862522,-0.699592,-1.453027,-2.325813,1.233617,8.622911,8.857949,-9.312887,6.459531,6.607531,1.985276,4.601302,2.756327,6.585627,-1.755368,-9.585299,-1.469125,1.193327,9.604317,9.258557,7.687327,8.827977,6.332848,-7.324501,9.780258,2.861376,-6.588453,-7.088739,-1.915748,-5.157853,7.362710,-5.160018,3.373929,-2.445823,7.949770,5.711093,-7.420432,-2.433779,6.145040,-2.074184,-5.231351,8.914489,3.238780,-6.361351,-8.634912,-4.871073,5.897151], dtype = "float64")#candidate|21170|(100,)|const|float64
const_21171 = relay.const([8,-1,-7,-2,-2,3,-10,-2,-2,5,2,4,5,-2,-2,8,-2,-8,-8,5,5,-3,-6,-5,-10,2,-2,-3,-6,9,1,-1,4,2,-2,-3,-7,-3,-3,-3,1,-9,4,1,9,2,-7,5,-2,5,-5,2,7,7,4,-5,5,-7,3,3,-5,-2,-7,4,-3,5,7,2,-3,-6,-8,9,2,-4,-1,9,-1,-10,9,10,-3,1,-4,-6,1,1,10,3,-7,8,-6,-6,9,7,-2,-1,-6,6,5,-5,3,-4,-10,-6,-7,-7,-5,-10,-10,4,6,6,-8,-1,4,9,-4,2,-1,-10,-7,1,-9,6,-10,1,8,9,2,10,8,7,4,7,-10,-6,-4,-10,-10,4,9,-9,7,-4,9,-6,5,8,-3,-7,-4,1,-9,-2,-9,10,-4,-6,8,9,-6,-4,-10,-10,-9,-7,9,-8,-1,9,9,-8,8,-3,4,4,10,-2,-10,3,-1,-2,-8,-9,3,9,-7,4,-10,6,10,3,7,10,8,-9,-2,9,1,1,8,-5,-6,4,5,-8,-7,-5,-8,4,-6,7,3,-10,-4,8,10,6,-2,1,-8,2,-2,2,2,8,-10,-8,8,7,10,5,1,-5,2,10,-7,-9,-9,-8,8,9,-10,-9,4,2,3,3,9,-7,-5,2,9,-10,-2,-9,6,-6,-4,5,-3,1,6,-2,-5,-5,7,-2,-9,-7,3,-1,4,5,4,-6,-1,-5,-3,10,-5,8,-4,-10,-3,6,-1,-6,6,-2,3,9,7,1,-10,-7,7,7,-6,-4,4,-8,9,-9,-5,-5,-9,6,-6,-7,7,-1,9,-8,7,-7,-4,-5,9,5,-4,-6,-5,-10,-9,-7,-1,3,-10,-9,2,7,3,6,5,9,4,-6,-10,-9,-5,5,9,-8,-8,-6,-6,-6,-7,2,6,3,7,-8,-8,-5,-3,1,-2,-1], dtype = "int64")#candidate|21171|(360,)|const|int64
call_21169 = relay.TupleGetItem(func_19367_call(relay.reshape(const_21170.astype('float64'), [100,]), relay.reshape(const_21171.astype('int64'), [360,]), ), 8)
call_21172 = relay.TupleGetItem(func_19370_call(relay.reshape(const_21170.astype('float64'), [100,]), relay.reshape(const_21171.astype('int64'), [360,]), ), 8)
func_7136_call = mod.get_global_var('func_7136')
func_7138_call = mutated_mod.get_global_var('func_7138')
var_21206 = relay.var("var_21206", dtype = "float32", shape = (20,))#candidate|21206|(20,)|var|float32
call_21205 = func_7136_call(relay.reshape(var_21206.astype('float32'), [4, 1, 5]))
call_21207 = func_7136_call(relay.reshape(var_21206.astype('float32'), [4, 1, 5]))
output = relay.Tuple([uop_21166,call_21169,const_21170,const_21171,call_21205,var_21206,])
output2 = relay.Tuple([uop_21166,call_21172,const_21170,const_21171,call_21207,var_21206,])
func_21208 = relay.Function([var_21165,var_21206,], output)
mod['func_21208'] = func_21208
mod = relay.transform.InferType()(mod)
mutated_mod['func_21208'] = func_21208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21208_call = mutated_mod.get_global_var('func_21208')
var_21210 = relay.var("var_21210", dtype = "float32", shape = (13, 13, 7))#candidate|21210|(13, 13, 7)|var|float32
var_21211 = relay.var("var_21211", dtype = "float32", shape = (20,))#candidate|21211|(20,)|var|float32
call_21209 = func_21208_call(var_21210,var_21211,)
output = call_21209
func_21212 = relay.Function([var_21210,var_21211,], output)
mutated_mod['func_21212'] = func_21212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20777_call = mod.get_global_var('func_20777')
func_20778_call = mutated_mod.get_global_var('func_20778')
call_21238 = func_20777_call()
call_21239 = func_20777_call()
output = call_21238
output2 = call_21239
func_21264 = relay.Function([], output)
mod['func_21264'] = func_21264
mod = relay.transform.InferType()(mod)
output = func_21264()
func_21265 = relay.Function([], output)
mutated_mod['func_21265'] = func_21265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17389_call = mod.get_global_var('func_17389')
func_17391_call = mutated_mod.get_global_var('func_17391')
call_21271 = relay.TupleGetItem(func_17389_call(), 0)
call_21272 = relay.TupleGetItem(func_17391_call(), 0)
output = call_21271
output2 = call_21272
func_21280 = relay.Function([], output)
mod['func_21280'] = func_21280
mod = relay.transform.InferType()(mod)
output = func_21280()
func_21281 = relay.Function([], output)
mutated_mod['func_21281'] = func_21281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19855_call = mod.get_global_var('func_19855')
func_19857_call = mutated_mod.get_global_var('func_19857')
call_21324 = func_19855_call()
call_21325 = func_19855_call()
output = call_21324
output2 = call_21325
func_21332 = relay.Function([], output)
mod['func_21332'] = func_21332
mod = relay.transform.InferType()(mod)
mutated_mod['func_21332'] = func_21332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21332_call = mutated_mod.get_global_var('func_21332')
call_21333 = func_21332_call()
output = call_21333
func_21334 = relay.Function([], output)
mutated_mod['func_21334'] = func_21334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21469 = relay.var("var_21469", dtype = "uint16", shape = (6, 16, 14))#candidate|21469|(6, 16, 14)|var|uint16
var_21470 = relay.var("var_21470", dtype = "uint16", shape = (6, 16, 14))#candidate|21470|(6, 16, 14)|var|uint16
bop_21471 = relay.greater(var_21469.astype('bool'), relay.reshape(var_21470.astype('bool'), relay.shape_of(var_21469))) # shape=(6, 16, 14)
output = bop_21471
output2 = bop_21471
func_21474 = relay.Function([var_21469,var_21470,], output)
mod['func_21474'] = func_21474
mod = relay.transform.InferType()(mod)
var_21475 = relay.var("var_21475", dtype = "uint16", shape = (6, 16, 14))#candidate|21475|(6, 16, 14)|var|uint16
var_21476 = relay.var("var_21476", dtype = "uint16", shape = (6, 16, 14))#candidate|21476|(6, 16, 14)|var|uint16
output = func_21474(var_21475,var_21476,)
func_21477 = relay.Function([var_21475,var_21476,], output)
mutated_mod['func_21477'] = func_21477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18130_call = mod.get_global_var('func_18130')
func_18131_call = mutated_mod.get_global_var('func_18131')
call_21540 = func_18130_call()
call_21541 = func_18130_call()
output = call_21540
output2 = call_21541
func_21549 = relay.Function([], output)
mod['func_21549'] = func_21549
mod = relay.transform.InferType()(mod)
output = func_21549()
func_21550 = relay.Function([], output)
mutated_mod['func_21550'] = func_21550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20532_call = mod.get_global_var('func_20532')
func_20534_call = mutated_mod.get_global_var('func_20534')
call_21614 = relay.TupleGetItem(func_20532_call(), 0)
call_21615 = relay.TupleGetItem(func_20534_call(), 0)
func_20188_call = mod.get_global_var('func_20188')
func_20189_call = mutated_mod.get_global_var('func_20189')
call_21622 = relay.TupleGetItem(func_20188_call(), 0)
call_21623 = relay.TupleGetItem(func_20189_call(), 0)
func_20318_call = mod.get_global_var('func_20318')
func_20320_call = mutated_mod.get_global_var('func_20320')
var_21636 = relay.var("var_21636", dtype = "float64", shape = (96,))#candidate|21636|(96,)|var|float64
call_21635 = relay.TupleGetItem(func_20318_call(relay.reshape(var_21636.astype('float64'), [96,])), 3)
call_21637 = relay.TupleGetItem(func_20320_call(relay.reshape(var_21636.astype('float64'), [96,])), 3)
var_21665 = relay.var("var_21665", dtype = "float64", shape = (14, 384))#candidate|21665|(14, 384)|var|float64
bop_21666 = relay.logical_or(call_21635.astype('bool'), var_21665.astype('bool')) # shape=(14, 384)
bop_21669 = relay.logical_or(call_21637.astype('bool'), var_21665.astype('bool')) # shape=(14, 384)
uop_21673 = relay.acosh(call_21635.astype('float32')) # shape=(1, 384)
uop_21675 = relay.acosh(call_21637.astype('float32')) # shape=(1, 384)
uop_21677 = relay.erf(uop_21673.astype('float64')) # shape=(1, 384)
uop_21679 = relay.erf(uop_21675.astype('float64')) # shape=(1, 384)
func_20379_call = mod.get_global_var('func_20379')
func_20381_call = mutated_mod.get_global_var('func_20381')
call_21682 = func_20379_call()
call_21683 = func_20379_call()
uop_21684 = relay.acos(uop_21677.astype('float64')) # shape=(1, 384)
uop_21686 = relay.acos(uop_21679.astype('float64')) # shape=(1, 384)
bop_21693 = relay.less_equal(uop_21677.astype('bool'), relay.reshape(uop_21684.astype('bool'), relay.shape_of(uop_21677))) # shape=(1, 384)
bop_21696 = relay.less_equal(uop_21679.astype('bool'), relay.reshape(uop_21686.astype('bool'), relay.shape_of(uop_21679))) # shape=(1, 384)
output = relay.Tuple([call_21614,call_21622,var_21636,bop_21666,call_21682,bop_21693,])
output2 = relay.Tuple([call_21615,call_21623,var_21636,bop_21669,call_21683,bop_21696,])
func_21697 = relay.Function([var_21636,var_21665,], output)
mod['func_21697'] = func_21697
mod = relay.transform.InferType()(mod)
var_21698 = relay.var("var_21698", dtype = "float64", shape = (96,))#candidate|21698|(96,)|var|float64
var_21699 = relay.var("var_21699", dtype = "float64", shape = (14, 384))#candidate|21699|(14, 384)|var|float64
output = func_21697(var_21698,var_21699,)
func_21700 = relay.Function([var_21698,var_21699,], output)
mutated_mod['func_21700'] = func_21700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18515_call = mod.get_global_var('func_18515')
func_18516_call = mutated_mod.get_global_var('func_18516')
call_21749 = relay.TupleGetItem(func_18515_call(), 1)
call_21750 = relay.TupleGetItem(func_18516_call(), 1)
func_19855_call = mod.get_global_var('func_19855')
func_19857_call = mutated_mod.get_global_var('func_19857')
call_21752 = func_19855_call()
call_21753 = func_19855_call()
output = relay.Tuple([call_21749,call_21752,])
output2 = relay.Tuple([call_21750,call_21753,])
func_21786 = relay.Function([], output)
mod['func_21786'] = func_21786
mod = relay.transform.InferType()(mod)
mutated_mod['func_21786'] = func_21786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21786_call = mutated_mod.get_global_var('func_21786')
call_21787 = func_21786_call()
output = call_21787
func_21788 = relay.Function([], output)
mutated_mod['func_21788'] = func_21788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20029_call = mod.get_global_var('func_20029')
func_20030_call = mutated_mod.get_global_var('func_20030')
call_21807 = relay.TupleGetItem(func_20029_call(), 0)
call_21808 = relay.TupleGetItem(func_20030_call(), 0)
func_19118_call = mod.get_global_var('func_19118')
func_19119_call = mutated_mod.get_global_var('func_19119')
call_21809 = relay.TupleGetItem(func_19118_call(), 0)
call_21810 = relay.TupleGetItem(func_19119_call(), 0)
output = relay.Tuple([call_21807,call_21809,])
output2 = relay.Tuple([call_21808,call_21810,])
func_21811 = relay.Function([], output)
mod['func_21811'] = func_21811
mod = relay.transform.InferType()(mod)
output = func_21811()
func_21812 = relay.Function([], output)
mutated_mod['func_21812'] = func_21812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19319_call = mod.get_global_var('func_19319')
func_19320_call = mutated_mod.get_global_var('func_19320')
call_21819 = func_19319_call()
call_21820 = func_19319_call()
func_21264_call = mod.get_global_var('func_21264')
func_21265_call = mutated_mod.get_global_var('func_21265')
call_21828 = func_21264_call()
call_21829 = func_21264_call()
output = relay.Tuple([call_21819,call_21828,])
output2 = relay.Tuple([call_21820,call_21829,])
func_21830 = relay.Function([], output)
mod['func_21830'] = func_21830
mod = relay.transform.InferType()(mod)
mutated_mod['func_21830'] = func_21830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21830_call = mutated_mod.get_global_var('func_21830')
call_21831 = func_21830_call()
output = call_21831
func_21832 = relay.Function([], output)
mutated_mod['func_21832'] = func_21832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20859_call = mod.get_global_var('func_20859')
func_20860_call = mutated_mod.get_global_var('func_20860')
call_21842 = func_20859_call()
call_21843 = func_20859_call()
func_20429_call = mod.get_global_var('func_20429')
func_20430_call = mutated_mod.get_global_var('func_20430')
call_21844 = func_20429_call()
call_21845 = func_20429_call()
func_15709_call = mod.get_global_var('func_15709')
func_15710_call = mutated_mod.get_global_var('func_15710')
call_21846 = relay.TupleGetItem(func_15709_call(), 1)
call_21847 = relay.TupleGetItem(func_15710_call(), 1)
uop_21849 = relay.asin(call_21844.astype('float64')) # shape=(13, 3, 15)
uop_21851 = relay.asin(call_21845.astype('float64')) # shape=(13, 3, 15)
func_15329_call = mod.get_global_var('func_15329')
func_15334_call = mutated_mod.get_global_var('func_15334')
var_21859 = relay.var("var_21859", dtype = "uint64", shape = ())#candidate|21859|()|var|uint64
const_21860 = relay.const([[3,-3,3,1,-4,-2,-9,3,8,-3,-1,-1],[-5,-9,-2,-6,4,-10,-9,-7,-6,-9,3,-5],[6,-4,-10,-5,5,-8,1,-2,3,6,-2,6],[5,3,7,-7,-7,10,-9,2,3,8,4,-10],[3,1,-8,-3,4,9,5,-4,10,-8,1,10],[2,9,-10,-4,-5,-10,4,6,-1,-9,4,9],[-9,10,8,5,9,-7,3,4,8,10,7,-2],[-4,5,6,1,-10,7,-2,10,-6,-4,10,-4],[-4,-2,2,-9,9,-4,7,-10,8,-5,-10,2],[1,5,-6,2,7,10,10,-8,5,-3,9,9],[3,-6,10,10,-5,-5,-6,-2,-10,2,2,-8],[4,-1,-7,8,6,-4,3,-10,-9,-3,9,-9],[6,9,-3,-6,10,-10,8,6,2,-2,4,-7],[-6,-1,4,6,-3,-1,-3,3,-6,10,-9,-10],[8,9,-4,6,-7,-5,-7,2,-5,6,9,1],[2,-9,-8,3,-1,-10,9,2,-5,6,9,3],[10,-2,-9,-4,4,2,-2,-10,9,7,9,3],[-8,7,-6,1,-8,-5,-6,7,-2,-4,4,-9],[-7,1,8,10,-5,-3,-5,-9,5,-9,-4,-3],[-5,-3,4,-4,-8,4,10,-10,-9,8,-7,-9],[2,5,4,10,-6,10,5,-10,-8,-9,-10,-5],[-3,-5,9,-3,1,7,-6,7,-2,-4,9,-9],[10,-7,-6,1,5,-10,-9,-5,8,8,-1,-10],[1,7,1,9,4,4,-8,1,-1,10,-1,2]], dtype = "uint64")#candidate|21860|(24, 12)|const|uint64
const_21861 = relay.const([7,-6,10,-2,7,2,5,-4,10,-3,7,-2,-6,2,-6,10,10,10,-1,-4,8,-8,6,3,8,-8,2,2,5,-5,-6,4,-1,5,-9,-2,-6,9,4,9,7,-7,-7,6,4,3,-8,-7,3,1,-10,8,-3,10,-10,9,6,8,-4,5,8,9,5,3,7,-10,6,3,-7,-9,1,4,-2,1,7,-6,-4,-10,-1,8,6,-5,8,-4,-2,-1,8,2,-10,-10,9,-5,-2,-3,-8,3,1,-10,5,-3,6,-9,3,-8,4,-3,3,5,1,-8,-1,6,-8,-10,-10,-9,-8,3,-8,6,7,5,5,7,2,-8,-6,-4,3,-5,-8,1,3,-9,5,4,-5,5,-1,-8,6,5,-2,-6,4,10,-6,-9,-7,9,-4,-5,4,-8,10,7,2,10,2,1,-7,-1,3,1,10,3,5,-2,-8,3,6,8,3,-4,-3,-4,-5,3,-6,-10,-8,-8,-1,-3,3,-10,7,7,-5,-8,7,9,6,-1,-10,-9,-4,-3,-9,5,-4,9,3,3,10,-8,-3,8,-3,-4,-10,1,-9,-10,-1,-8,-9,6,6,2,1,10,9,5,-9,-6,9,-4,2,-7,-8,-9,4,9,-7,4,2,-1,-4,-6,-7,-3,-8,7,10,4,-8,4,-10,-10,7,4,9,-2,-4,-7,1,-7,8,10,5,7,8,-5,-6,5,10,3,-5,-4,5,9,-1,4,10,9,-7,1,6,6,-3,-5,10,-4,-5,3,-10,-4,9,-2,2,-4,-8,6,3,7,-3,-10,-10,-8,-3,-3,-5,5,6,3,-1,-7,-2,-4,-7,10,3,2,4,-8,-3,1,-9,2,-8,-3,1,-7,-5,7,-1,-9,-9,-8,3,10,-7,1,-1,-3,-7,-7,6,-1,-6,10,-7,2,2,-9,-5,10,-1,-10,-6,-9,-9,1,-2,-6,-3,6,7,-8], dtype = "int64")#candidate|21861|(360,)|const|int64
call_21858 = relay.TupleGetItem(func_15329_call(relay.reshape(var_21859.astype('uint64'), []), relay.reshape(const_21860.astype('uint64'), [2, 144]), relay.reshape(const_21861.astype('int64'), [360,]), ), 4)
call_21862 = relay.TupleGetItem(func_15334_call(relay.reshape(var_21859.astype('uint64'), []), relay.reshape(const_21860.astype('uint64'), [2, 144]), relay.reshape(const_21861.astype('int64'), [360,]), ), 4)
uop_21876 = relay.asinh(uop_21849.astype('float64')) # shape=(13, 3, 15)
uop_21878 = relay.asinh(uop_21851.astype('float64')) # shape=(13, 3, 15)
func_20085_call = mod.get_global_var('func_20085')
func_20088_call = mutated_mod.get_global_var('func_20088')
var_21882 = relay.var("var_21882", dtype = "uint32", shape = (420,))#candidate|21882|(420,)|var|uint32
call_21881 = relay.TupleGetItem(func_20085_call(relay.reshape(var_21882.astype('uint32'), [420,])), 2)
call_21883 = relay.TupleGetItem(func_20088_call(relay.reshape(var_21882.astype('uint32'), [420,])), 2)
output = relay.Tuple([call_21842,call_21846,call_21858,var_21859,const_21860,const_21861,uop_21876,call_21881,var_21882,])
output2 = relay.Tuple([call_21843,call_21847,call_21862,var_21859,const_21860,const_21861,uop_21878,call_21883,var_21882,])
func_21886 = relay.Function([var_21859,var_21882,], output)
mod['func_21886'] = func_21886
mod = relay.transform.InferType()(mod)
mutated_mod['func_21886'] = func_21886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21886_call = mutated_mod.get_global_var('func_21886')
var_21888 = relay.var("var_21888", dtype = "uint64", shape = ())#candidate|21888|()|var|uint64
var_21889 = relay.var("var_21889", dtype = "uint32", shape = (420,))#candidate|21889|(420,)|var|uint32
call_21887 = func_21886_call(var_21888,var_21889,)
output = call_21887
func_21890 = relay.Function([var_21888,var_21889,], output)
mutated_mod['func_21890'] = func_21890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18261_call = mod.get_global_var('func_18261')
func_18263_call = mutated_mod.get_global_var('func_18263')
call_21911 = relay.TupleGetItem(func_18261_call(), 1)
call_21912 = relay.TupleGetItem(func_18263_call(), 1)
output = call_21911
output2 = call_21912
func_21914 = relay.Function([], output)
mod['func_21914'] = func_21914
mod = relay.transform.InferType()(mod)
mutated_mod['func_21914'] = func_21914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21914_call = mutated_mod.get_global_var('func_21914')
call_21915 = func_21914_call()
output = call_21915
func_21916 = relay.Function([], output)
mutated_mod['func_21916'] = func_21916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21830_call = mod.get_global_var('func_21830')
func_21832_call = mutated_mod.get_global_var('func_21832')
call_21920 = relay.TupleGetItem(func_21830_call(), 1)
call_21921 = relay.TupleGetItem(func_21832_call(), 1)
func_7645_call = mod.get_global_var('func_7645')
func_7649_call = mutated_mod.get_global_var('func_7649')
const_21933 = relay.const([-9.648621,-7.050111,-1.341046,-5.702256,4.670216,-0.413335,9.760164,3.019135,-5.307263,7.298281,2.158009,1.322375,1.085987,5.108798,8.870266,-7.442150,8.927531,9.061292,-7.023345,1.415943,-1.753738,-8.867986,-9.289052,-2.545536,-7.709019,7.925180,0.100733,-4.163219,0.001863,3.659125,5.677932,-1.204201,7.648513,-7.955945,-0.776029,1.777865,7.096003,-4.517312,9.721352,-7.754488,-8.038324,-3.500479,-4.282885,-1.960297,-1.511476,8.286610,3.896093,-9.621138,5.623033,1.159824,-8.060742,-5.487682,-1.444519,-6.320511,8.754497,6.275812,-4.186355,9.379838,-5.334582,-3.313194,-6.779521,-6.789632,-1.230895,-5.187576,0.451771,6.946955,-0.248323,3.561459,-7.178217,9.203479,1.192610,4.469015,-3.377867,-6.641492,-0.581488,0.695520,-4.561922,7.004364,-5.958485,-6.368454,4.996915,7.241475,2.239210,-2.726098,-2.629489,6.097551,-4.138647,2.324518,-1.406707,-4.518677,2.898639,4.892407,6.708012,-3.825203,-3.078368,-4.104485,-9.335302,3.854941,-3.589398,4.576830,6.076432,-5.325468,6.700236,-5.789945,-1.064953,-4.005703,-6.807963,3.376077,-4.125958,9.213496,5.397984,-6.313718,-5.743593,5.156642,2.197127,7.815369,-3.585871,2.191087,-7.872388,8.044158,-3.205338,-2.861249,3.534062,-6.623559,8.809796,-6.817649,5.881382,-7.060508,-7.803870,4.917945,-0.285507,1.928446,-8.074952,-0.762365,-1.112268,8.719183,8.906272,-5.716839,-1.504771,3.371765,-8.398146,-7.128635,-2.255475,6.719008,-3.309899,3.773370,-8.028831,0.474071,0.705265,4.679230,7.324610,-5.641480,-7.431246,9.019410,4.464062,-3.681277,-4.901709,-8.640462,8.561347,-5.899443,-1.931692,-2.545905,-9.421131,0.410681,2.968061,1.100167,-2.366449,8.912546,-3.728943,0.483378,2.141284,-6.527981,-4.919096,7.705125,-4.717083,0.305641,6.343562,4.773881,-2.812407,5.765305,4.698534,-2.896784,-8.265631,-3.888269,1.401947,-3.390060,5.826364,-1.113643,2.821287,6.410146,6.536596,-0.452087,-8.695825,-6.267104,9.537598,-4.509539,7.078710,-8.543814,6.687326,-9.682812,-5.936919,6.591314,2.530727,2.065641,4.112054,4.488332,2.385754,7.511322,6.234262,-3.480655], dtype = "float64")#candidate|21933|(210,)|const|float64
const_21934 = relay.const([-2,-5,-6,-3,-6,-10,-7,3,1,-1,2,-2,-3,-5,4,9,5,-6,-2,-3,-1,-3,7,10,-8,6,1,10,-1,-8,-5,10,9,-8,-2,9,8,-10,10,3,-3,7,-7,7,10,-2,10,-4,5,-2,-4,10,3,-7,4,-10,-10,-10,-3,-6,4,-7,-9,5,-2,-1,-8,-8,-5,-5,-4,-3,-3,1,1,9,3,-2,-7,-6,-4,5,2,-4,-6,-3,3,5,10,-1,1,-8,6,-9,-7,-1,-4,2,8,10,-4,-4,-10,6,-5,2,-7,-4,-2,-3,10,9,-8,9,-10,2,3,-2,7,4,5,9,8,-2,-6,9,-10,-9,1,6,10,-5,6,-7,-7,6,-7,-3,-8,-3,-3,2,1,4,3,5,-10,6,10,-8,4,-1,8,-6,-1,5,-3,9,-2,8,-3,-9,-3,-8,10,-2,-1,-7,-6,-9,4,-3,3,-3,-5,10,-5,-10,8,3,-5,4,7,6,4,4,-9,7,1,7,-2,-3,-8,5,-2,-5,5,-4,3,-10,7,-7,3,8,-3,-1,2,1,-8,5,7,8,1,6,5,-1,10,-9,-3,6,-2,10,-10,1,9,9,-7,-8,10,-2,-8,7,2,-10,3,-10,4,8,-3,1,6,-6,6,3,7,-10,8,-4,5,5,1,-2,5,8,-10,10,10,1,1,3,9,5,-3,10,-5,8,10,1,-2,5,-2,8,-2,-10,-2,1,8,-1,-4,-1,-7,5,8,5,8,10,9,-2,6,4,-6,-1,10,7,4,5,6,-9,9,-6,7,7,-5,-7,-4,9,7,-6,4,4,-1,7,10,-6,3,-4,-8,-6,-3,-4,-7,4,-4,2,-4,-6,-3,6,1,2,2,4,-8,-2,5,-5,8,-6,-2,2,3,2,-1,1,10,5,9,1,10,-8,9,7,5,-4,2,-4,2,-4,6,-2,-9,8,6,7,5,1,1,3,-3,-4,1,-1,5,5,-1,8,3,1,-7,5,6,-6,-8,-6,6,-8,-9,1,6,-5,-2,-8,9,6,10,8,1,-4,4,2,9,8,-10,-3,-4,5,1,3,-5,-8,4,10,1,-8,3,7,-9,1,4,6,-2,4,-4,-5,-9,3,-10,-3,-6,-6,-9,10,-7,-9,-5,-9,-8,10,3,3,8,-7,9,-9,-1,4,9,-1,-5,7,7,-6,-10,-9,10,7,7,4,6,-1,-8,10,-8,-4,-1,-2,-9,-5,3,-6,-7,-10,-8,2,-8,4,9,5,-5,10,-2,-8,1,3,-9,-6,1,3,-2,3,8,-8,-1,4,-4,4,7,8,-5,-3,-8,-3,6,-8,8,8,1,5,-1,-10,3,10,5,-9,8,7,10,-5,-5,-5,-6,-1,1,1,-4,6,4,-9,-3,-3,10,-7,1,7,6,-9,6,-1,5,-10,2,6,1,9,6,5,2,-8,-3,-9,8,-3,-7,3,6,-2,-9,-8,-6,6,-7,-7,2,-1,2,-6,-9,5,5,9,1,-2,10,3,-5,7,10,2,-1,9,-5,4,-5,-10,-8,2,10,2,-3,3,5,-3,-6,-9,10,-2,2,-10,4,-7,-1,-4,2,9,2,-7,-4,2,-5,-8,-8,1,6,-8,1,5,-4,-1,6,4,-3,-6,1,-6,-10,1,-5,-9,4,-1,1,-7,4,3,-7,9,10,-7,-5,9,-7,3,-5,-3,10,-1,10,7,-5,6,-9,-4,-2,2,-3,-3,3,4,-10,4,1,-10,5,-6,10,-4,9,-10,8,8,-4,4,9,-5,3,9,-7,6,8,4,-4,-5,-6,-3,6,8,6,-7,-7,6,-2,-5,-3,2,-3,-7,7,-1,8,9,-9,6,-8,10,7,-9,-10,9,7,5,2,-8,-8,1,-5,4,1,7,4,7,3,10,10,7,3,-9,5,-3,6,-1,-6,5,4,7,9,-9,9,6,-9,9,6,-8,-5,4,-4,-2,-7,-10,-7,8,2,-10,7,4,-10,1,-9,7,-9,-5,5,7,-2,-6,5,-7,-3,2,5,-7,7,3,4,-1,-4,-8,-4,2,2,-5,1,-8,10,-4,3,4,-9,9,-10,8,7,-2,1,-6,-3,3,-4,-10,-8,3,-8,-5,-5,-2,-5,8,8,-2,5,3,-9,-4,5,9,-10,9,9,-7,-8,-9,9,4,9,-8,4,-4,8,-7,-4,10,-9,4,-3,-4,9,-6,1,8,8,4,-7,-8,-8,10,1,6,1,2,10,-6,7,7,-4,10,1,7,-4,-3,-9,-2,6,-2,9,-10,-10,-10,-10,7,-4,-9,2,-10,-10,7,-9,10,9,10,-8,9,-1,-4,-7,-7,9,3,2,8,-10,1,-3,5,-7,-4,-7,4,3,9,1,1,3,-3,-9,9,3,-9,5,2,10,8,8,-7,9,3,3,-4,-5,-3,6,-6,-6,-9,10,2,7,9,-1,10,-4,2,4,6,-2,6,3,-9,6,9,-9,-3,-2,-6,1,-4,7,-2,3,10,7,3,7,-10,-10,-6,1,-7,-4,-5,-7,9,5,4,-7,1,-2,5,-6,2,-3,3,10,6,-3,10,-8,-7,-10,10,7,5,-6,9,-7,-8,-9,-6,-2,-4,3,-6,-5,-5,4,-4,7,-10,-2,-6,10,-9,4,-10,8,-3,10,-4,-4,3,4,-9,-9,-7,10,7,-7,10,4,8,-6,4,2,-2,-9,-4,-2,-6,-4,1,-6,5,-7,-7,-7,-6,7,8,8,-4,4,-9,-1,-9,-8,10,-1,9,1,10,2,8,5,-7,-5,1,-8,-8,-7,-5,-7,3,1,-7,-10,10,-2,1,6,4,8,-1,-8,-7,-7,-2,-7,-2,6,3,-6,-8,-3,10,7,-3,9,-3,-4,-2,5,5,8,2,-7,-10,10,-3,-8,-4,-5,10,-2,1,-7,7,6,6,9,7,-5,-9,8,-7,5,1,-10,-5,6,-10,-8,5,-1,9,-8,-10,-7,7,-10,-2,-8,6,6,4,-5,4,-3,1,-9,8,1,10,6,5,-2,3,-2,1,8,7,-8,-1,2,-7,-4,-10,-2,3,10,5,5,-5,5,-2,-9,-8,-3,-10,-1,-8,5,-10,-10,4,-10,-5,7,1,-6,-4,-5,-4,1,3,-4,-9,-1,-3,-9,-5,7,4,-10,5,2,-8,4,-5,-7,-9,1,7,4,-3,8,3,-7,-9,-4,10,-4,2,2,4,-6,-10,2,9,9,10,1,5,10,5,-10,9,5,3,9,-9,-2,-1,8,10,-3,7,4,2,-9,10,-1,-3,-10,-6,-6,3,-3,10,-6,1,1,-5,-3,8,5,-1,-7,-5,-3,-8,-5,6,-7,3,7,7,3,4,1,10,-10,-4,-7,7,-9,10,-8,-6,-3,10,-3,1,-9,4,6,5,4,4,8,1,4,3,-8,-9,-6,-4,-8,-6,9,-6,-1,9,-2,-7,4,-10,-1,-2,-2,1,-10,8,9,4,2,-3,4,-8,-4,-7,-3,9,-9,-3,2,8,1,9,-2,10,-4,6,-4,2,-1,8,-5,-10,-8,5,8,-1,3,-1,-10,8,-3,-1,1,6,-4,8,3,-6,-10,10,-8,9,8,6,-10,-3,-9,9,-10,3,-3,-3,-10,7,2,10,-8,-1,8,8,2,-10,-6,2,-5,-9,-8,5,3,-10,1,7,8,8,7,-3,-5,-9,-1,8,6,6,-10,-1,-3,10,-10,3,-6,3], dtype = "int16")#candidate|21934|(1404,)|const|int16
call_21932 = relay.TupleGetItem(func_7645_call(relay.reshape(const_21933.astype('float64'), [14, 15, 1]), relay.reshape(const_21934.astype('int16'), [1, 1404]), ), 0)
call_21935 = relay.TupleGetItem(func_7649_call(relay.reshape(const_21933.astype('float64'), [14, 15, 1]), relay.reshape(const_21934.astype('int16'), [1, 1404]), ), 0)
output = relay.Tuple([call_21920,call_21932,const_21933,const_21934,])
output2 = relay.Tuple([call_21921,call_21935,const_21933,const_21934,])
func_21953 = relay.Function([], output)
mod['func_21953'] = func_21953
mod = relay.transform.InferType()(mod)
mutated_mod['func_21953'] = func_21953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21953_call = mutated_mod.get_global_var('func_21953')
call_21954 = func_21953_call()
output = call_21954
func_21955 = relay.Function([], output)
mutated_mod['func_21955'] = func_21955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16550_call = mod.get_global_var('func_16550')
func_16551_call = mutated_mod.get_global_var('func_16551')
call_22011 = relay.TupleGetItem(func_16550_call(), 3)
call_22012 = relay.TupleGetItem(func_16551_call(), 3)
func_18045_call = mod.get_global_var('func_18045')
func_18050_call = mutated_mod.get_global_var('func_18050')
var_22019 = relay.var("var_22019", dtype = "int16", shape = (1404,))#candidate|22019|(1404,)|var|int16
const_22020 = relay.const([-10,8,-8,-4,-5,2,-4,-1,-8,-1,6,-7,-4,6,8,-6,8,6,1,3,-3,-1,-5,-5,-9,1,4,2,5,-10,5,1,-1,9,7,10,-6,-6,-5,-8,-9,-2,7,3,-9,-4,8,-10,-4,-3,-3,-10,3,-4,9,5,-10,-5,10,-10,-2,5,-10,10,-8,-5,-5,-1,-5,9,6,-5,10,5,9,-8,8,10,-10,3,5,-8,7,3,6,-5,7,-9,10,-8,9,-10,9,6,4,9,1,10,-9,-9,6,-7,6,1,-10,-4,4,6,8,5,3,-9,-1,2,5,-5,5,-3,8,6,-2,-8,8,10,-8,-8,-10,7,8,-1,9,4,-8,7,-1,-5,-5,9,-9,-1,-3,9,-6,5,4,-6,4,8,-9,9,8,-4,6,-8,2,3,-8,1,7,-7,3,-5,-5,2,-8,5,4,-10,-3,-7,-10,2,-3,10,-8,10,-10,2,-7,-9,-3,10,-4,-2,-9,-1,9,4,6,-1,-1,-8,5,-8,4,7,2,7,-8,-10,-7,-7,-6,-10,7,9,-4,2,-8,-4,-8,2,-10,5,-7,6,-7,4,-8,-8,-8,4,5,-3,-8,7,-8,5,7,8,6,10,1,-9,-10,3,-5,10,-4,-4,10,6,10,7,-3,3,-3,5,7,-10,-10,-5,-9,-6,9,-3,5,8,3,5,4,-5,1,8,3,-6,-10,-9,-7,-10,-7,7,2,-7,3,-1,10,-2,8,-8,8,6,-7,5,-10,-2,7,10,7,6,-9,-6,5,-9,-8,5,-1,5,4,1,6,4,5,5,-1,-9,-10,-9,-3,-9,5,8,-3,-3,-5,-4,10,-6,-9,-4,-2,1,9,8,-10,2,10,-1,-7,3,-9,-2,-4,3,-9,-6,-1,4,10,-10,8,-6,-6,-1,-3,4,1,2,-4,1,-1,6,-7,-10,2,-5,-5,-1,10,-3,-8,5,-3,-7,2,-2,-6,-5,-9,-9,-8,-5,7,-6,-8,10,-8,-5,3,-9,9,-8,-10,-9,-9,-3,-3,1,-2,7,-6,6,-3,4,-3,9,-6,9,1,6,6,-8,-6,9,4,10,4,-5,-6,-2,-3,3,9,5,9,1,-1,-4,-8,6,8,5,1,10,-6,-10,-5,-8,4,6,5,1,-8,2,8,1,4,-10,3,-6,-2,10,9,4,3,9,9,5,-2,7,-7,-8,2,7,7,4,10,-9,-2,-2,-4,5,10,-5,9,4,8,-6,-9,-6,8,8,-4,7,-1,-2,-2,2,-9,6,-9,-3,-10,7,-1,8,3,-7,4,-4,5,-3,7,10,-2,-3,7,-8,-4,-8,10,-2,1,-1,-3,1,-2,-6,-10,4,-5,5,-4,8,-9,-1,-4,1,2,2,6,-5,8,7,10,-1,10,-4,8,10,-10,-4,6,10,7,5,-5,-2,-2,4,2,-4,1,7,-1,5], dtype = "int64")#candidate|22020|(546,)|const|int64
var_22021 = relay.var("var_22021", dtype = "float64", shape = (364,))#candidate|22021|(364,)|var|float64
call_22018 = relay.TupleGetItem(func_18045_call(relay.reshape(var_22019.astype('int16'), [1404,]), relay.reshape(const_22020.astype('int64'), [546,]), relay.reshape(var_22021.astype('float64'), [364,]), ), 2)
call_22022 = relay.TupleGetItem(func_18050_call(relay.reshape(var_22019.astype('int16'), [1404,]), relay.reshape(const_22020.astype('int64'), [546,]), relay.reshape(var_22021.astype('float64'), [364,]), ), 2)
output = relay.Tuple([call_22011,call_22018,var_22019,const_22020,var_22021,])
output2 = relay.Tuple([call_22012,call_22022,var_22019,const_22020,var_22021,])
func_22033 = relay.Function([var_22019,var_22021,], output)
mod['func_22033'] = func_22033
mod = relay.transform.InferType()(mod)
mutated_mod['func_22033'] = func_22033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22033_call = mutated_mod.get_global_var('func_22033')
var_22035 = relay.var("var_22035", dtype = "int16", shape = (1404,))#candidate|22035|(1404,)|var|int16
var_22036 = relay.var("var_22036", dtype = "float64", shape = (364,))#candidate|22036|(364,)|var|float64
call_22034 = func_22033_call(var_22035,var_22036,)
output = call_22034
func_22037 = relay.Function([var_22035,var_22036,], output)
mutated_mod['func_22037'] = func_22037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19096_call = mod.get_global_var('func_19096')
func_19097_call = mutated_mod.get_global_var('func_19097')
call_22099 = func_19096_call()
call_22100 = func_19096_call()
output = relay.Tuple([call_22099,])
output2 = relay.Tuple([call_22100,])
func_22102 = relay.Function([], output)
mod['func_22102'] = func_22102
mod = relay.transform.InferType()(mod)
output = func_22102()
func_22103 = relay.Function([], output)
mutated_mod['func_22103'] = func_22103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20118_call = mod.get_global_var('func_20118')
func_20119_call = mutated_mod.get_global_var('func_20119')
call_22113 = func_20118_call()
call_22114 = func_20118_call()
func_14073_call = mod.get_global_var('func_14073')
func_14075_call = mutated_mod.get_global_var('func_14075')
call_22117 = relay.TupleGetItem(func_14073_call(), 0)
call_22118 = relay.TupleGetItem(func_14075_call(), 0)
func_19855_call = mod.get_global_var('func_19855')
func_19857_call = mutated_mod.get_global_var('func_19857')
call_22121 = func_19855_call()
call_22122 = func_19855_call()
func_20532_call = mod.get_global_var('func_20532')
func_20534_call = mutated_mod.get_global_var('func_20534')
call_22131 = relay.TupleGetItem(func_20532_call(), 2)
call_22132 = relay.TupleGetItem(func_20534_call(), 2)
bop_22137 = relay.multiply(call_22113.astype('uint16'), call_22131.astype('uint16')) # shape=(8, 5, 1404)
bop_22140 = relay.multiply(call_22114.astype('uint16'), call_22132.astype('uint16')) # shape=(8, 5, 1404)
func_8163_call = mod.get_global_var('func_8163')
func_8166_call = mutated_mod.get_global_var('func_8166')
const_22142 = relay.const([6,9,-1,6,-2,7,8,8,8,-9,-10,-9,9,-5,6,2,-3,2,8,5,-5,-7,-6,-1,6,9,-9,7,6,-10,1,6,2,6,-8,-9,5,5,8,6,-8,-10,-1,4,10,-10,5,-4,6,5,3,6,-8,9,-7,-2,10,-1,-10,10,10,-2,6,9,6,-5,-8,6,1,5,-2,4,-8,3,-1,-9,-3,-3,-5,-2,-8,7,-7,3,-10,-8,5,2,-7,1,-8,-7,1,1,-4,-6,-1,10,8,7,-4,-10,-9,4,9,-3,8,-9,2,5,-4,-10,-6,4,8,3,8,-2,-8,-2,4,6,-5,-10,-5,-5,-8,6,7,-1,1,8,-9,-8,-9,-4,8,-2,4,-10,-9,-10,9,-4,-5,-5,8,10,6,-4,10,7,-7,1,-2,-10,5,9,-5,-4,7,7,-5,-3,-4,-5,7,2,-10,5,1,3,5,-2,5,1,7,7,6,10,-1,4,-6,1,-9,-8,-2,-8,4,-9,8,-1,9,-5,-10,-5,-2,8,-5,-6,5,-5,-8,6,-5,-9,5,9,7,-1,1,-9,-2,2,6,-2,-5,-6,1,3,6,-10,3,7,3,1,1,-8,-7,-4,2,1,-4,2,-10,-3,8,-9,5,3,3,4,3,1,-4,-10,3,-6,10,-4,3,-7,5,4,-2,-7,-10,-9,5,-3,-4,-5,-6,-6,9,7,9,2,9,-3,-2,4,-3,5,6,7,10,-9,-7,3,2,7,-3,7,-7,-1,-3,1,1,-6,-3,-6,-6,-9,7,8,-1,5,6,-4,-2,-1,1,3,-9,8,1,-7,7,2,10,-5,7,-3,-2,7,3,9,2,-7,-10,-5,8,-9,-9,-1,3,10,-8,6,-3,3,10,1,7,-3,2,9,-1,7,1,9,-5,-7,-3,4,3,1,3,-7,9,-7,-9,2,-5,10,-6,10,-1,6,-10,-1,10,-8,5,1,-5,-6,3,6,7,-3,-6,-6,-2,2,-5,-4,-4,-5,-10,-2,5,1,6,-7,5,5,3,-10,-6,-8,5,5,6,8,-6,-1,8,10,-9,-6,7,6,7,-6,8,3,5,3,-7,7,1,8,-10,-1,7,3,-1,3,-7,-10,-2,10,-2,-1,4,-6,-4,2,3,2,3,2,-8,-3,-6,4,7,-9,7,-9,6,3,8,-5,-1,10,6,-9,1,-1,-6,-8,7,1,5,-4,-5,-4,-4,-5,8,10,-9,6,2,8,-2,-10,-4,-4,3,4,7,-1,7,-8,1,-6,-9,-2,-2,1,-9,-5,-6,-3,-7,4,-5,6,1,6,4,-2,-6,5,7,4,-1,-8,-7,5,-10,-1,4,-6,1,-4,-5,9,-3,1,-2,-3,-5,-9,3,-10,3,-7,-9,3,-6,7,5,3,10,-5,3,7,-10,2,-10,-6,4,-1,6,-6,-1,4,-1,-4,-4,-5,-9,-5,-9,-4,-9,-4,-4,9,1,4,10,-9,-8,-4,-4,-7,3,3,9,3,-8,3,3,3,7,5,-9,8,9,-10,-1,7,-9,6,-6,7,5,5,10,-2,-9,-4,-3,-8,4,-7,-4,-9,-5,-2,5,4,-7,-9,-10,6,10,-10,4,-9,-3,-3,1,10,10,-6,9,-4,10,5,-6,9,-3,-1,4,-5,-6,-6,2,-2,7,-5,9,-5,5,-1,5,7,9,-4,5,2,8,8,-3,2,10,8,-9,10,-7,4,-3,7,-8,4,2,3,-5,10,1,10,1,3,-3,3,8,-9,10,-10,10,-10,-4,-2,5,-9,-6,-10,-8,-7,9,-2,-9,5,-8,-8,1,-1,-4,-3,7,-5,-2,-9,9,-1,4,-3,-4,-4,3,3,9,-8,8,-2,-5,7,-4,-8,-10,1,-4,-1,-3,3,5,2,1,-9,-3,-4,-9,-8,7,4,-6,-3,9,1,7,10,9,9,1,-8,10,7,-1,10,2,5,-1,10,-4,-4,4,-4,3,4,-3,2,-2,-1,-3,-5,7,3,-10,-7,-4,7,4,-1,-7,3,-7,3,2,-6,-7,2,-1,-3,9,-5,-3,-1,6,-4,-8,2,1,-5,-1,10,2,-3,6,-3,-6,-8,-1,-3,-2,9,-3,-5,8,9,-3,-7,-10,5,6,1,-8,-10,9,-7,10,10,9,-10,-5,6,8,10,-4,6,-5,-2,7,2,-5,6,7,1,-9,-10,-1,-2,-10,9,-9,5,-3,7,-7,7,-9,9,8,1,2,4,10,4,-8,5,9,1,7,3,10,7,-2,-5,-6,-8,8,4,5,9,3,1,3,6,-4,5,-1,-3,-9,-1,-5,-3,-10,2,-5,1,4,-1,-7,-9,8,-3,6,-1,-6,-10,-3,5,-10,-3,9,-2,-7,4,-2,5,6,-10,-5,9,-7,-2,2,8,-8,6,2,-2,2,2,-10,-7,-4,1,2,-9,-9,-1,-10,-2,7,-8,7,-7,8,5,6,-4,-1,-10,-5,9,-3,4,9,-2,5,3,-1,-2,-2,5,-1,10,4,-2,-10,2,5,-7,-3,9,10,-1,-6,8,-10,-8,1,-2,10,3,-8,3,2,-6,-2,4,-8,-3,-8,2,3,8,8,1,5,-7,-9,-4,4,-10,6,-6,-1,-7,-9,6,9,-8,-5,4,-2,-10,-3,4,8,-2,7,9,9,6,6,-2,5,3,-8,9,8,-3,-8,6,2,-8,-8,-7,-4,-6,7,5,-7,-4,-5,-9,2,4,10,6,10,10,-3,-6,2,-7,-8,-10,3,4,-7,-1,-4,1,-2,3,-2,-1,-2,2,-7,-2,3,3,-6,-4,-9,-3,7,-6,-10,-3,4,5,-9,7,-8,-4,-10,7,-4,-10,5,6,5,2,-3,-8,-1,10,-2,7,-7,-10,-7,-5,-9,4,8,7,1,1,-6,-10,1,-8,-10,-2,-5,-6,-3,-3,-7,8,6,1,5,-1,8,-10,3,10,3,8,6,10,6,4,10,-1,5,4,-1,-3,-8,7,-10,-3,-1,-1,-7,-8,6,-10,-2,-3,-2,-1,3,1,-6,3,7,1,6,-7,-2,-10,9,-7,9,-9,10,-6,-3,-4,-7,-9,2,-2,-9,-3,-8,-3,3,9,1,-4,10,-6,7,4,-7,-8,-2,-7,-1,-5,-3,7,8,7,4,2,1,6,8,-10,4,5,-8,6,5,2,10,6,-3,-9,6,2,-1,-3,-10,-5,-3,-10,-3,2,-8,7,-4,-7,-6,6,10,-7,-6,-2,-5,1,-7,9,-7,-9,-7,-4,7,-8,10,3,3,10,2,8,-9,5,1,-8,-9,3,1,-7,-1,-9,10,-8,4,6,2,-3,-4,6,4,-4,-1,9,6,-8,10,5,-1,-6,-5,-9,8,-7,-10,-8,9,9,8,-1,3,-1,-7,4,-3,3,5,-4,-3,5,-8,-10,-4,-8,-5,9,8,-3,-10,5,9,1,1,9,8,9,-7,-4,6,-7,1,-10,-8,6,-2,-9,-8,-7,6,4,9,2,10,1,8,-10,-4,9,-5,-9,-5,-10,-1,-3,4,-2,9,-3,2,7,-1,-10,-7,-10,4,-1,-2,-4,-9,-1,-6,-8,-9,-6,-4,-10,9,-4,10,3,3,-7,-5,7,9,9,-3,10,7,-2,8,7,-3,-8,-5,1,2,-5,10,-1,10,-4,-6,-4,2,-5,7,10,3,6,-6,7,6,5,4,3,-7,-6,3,7,5,6,3,3,-3,-7,-8,8,-6,8,-2,-3,-9,-3,8,-8,3,-4,-1,4,8,4,8,7,-5,-4,-5,-6,-10,7,-1,3,-10,-10,-6,4,8,7,1,9,-7,3,-4,6,-9,3,7,-4,3,-5,-10,10,-10,3,-10,-7,9,-1,-10,6,10,-9,-3,2,-9,-4,10,7,2,-1,-6,1,8,-6,-9,-8,-2,-5,-10,-1,-6,7,1,-5,-8,7,-3,-9,10,-9,-8,9,-4,4,-1,-4,-10,-10,9,-3,-2,-10,9,-7,-7,-2,-1,-6,5,-8,5,-1,5,5,7,-10,10,-5,1,10,8,2,2,6,-8,-2,-8,-7,4,-6,3,1,6,-2,10,5,-5,9,7,-3,-2,7,9,3,-7,6,5,-3,7,-9,1,-5,3,2,-9,-4,-3,1,4,-7,4,-10,3,1,-3,7,6,-8,5,-8,8,-5,10,3,9,6,-3,2,2,-8,-4,8,-8,-9,-8,-7,-9,-7,8,5,-10,-1,-7,-3,-6,5,7,-2,-2,9,-9,6,9,-9,5,-2,-4,10,-6,4,5,4,5,-8,-6,-6,-3,3,8,-9,-5,-10,6,4,-4,-5,-10,-4,6,9,-10,7,9,-7,1,2,9,-8,-5,-8,-1,-9,-2,5,4,10,-10,9,-8,-8,10,-6,5,3,-6,-8,-4,7,1,-3,-7,1,1,-7,-4,-7,-7,5,-7,-2,9,-10,-9,8,1,5,8,5,5,8,1,6,-8,-1,-9,-8,3,3,4,-1,7,-5,1,-4,-6,-6,8,6,-4,3,-8,-4,-8,2,-10,-1,7,10,7,-6,6,1,-5,4,-2,3,-7,-10,3,8,-2,-10,4,9,-4,6,9,6,2,3,6,-3,-2,9,-2,-9,-8,5,9,-5,3,4,9,-5,-1,-7,2,-1,1,-10,-9,-1,-7,8,2,-8,-5,6,2,6,-8,10,3,6,3,10,6,10,-6,9,2,-5,-10,4,10,5,3,2,1,1,-6,8,10,5,-6,6,-2,8,1,5,-2,-3,-8,-2,-5,-4,1,2,8,9,-4,4,7,-9,2,2,-4,10,10,-2,-4,-5,-8,8,6,10,6,7,3,-4,2,10,2,10,1,-6,-10,-10,10,4,9,8,-9,-9,-3,-9,10,10,9,-6,6,5,-5,-4,-7,2,4,9,7,6,-2,4,6,6,6,8,-5,7,2,-6,-2,4,10,-1,-3,8,4,1,-8,5,-10,7,8,5,9,-6,10,9,5,-1,-9,-6,-1,-10,6,4,-10,1,-6,5,-8,6,-3,9,7,6,9,6,1,-10,5,10,6,1,-8,7,1,5,10,-2,6,-2,2,-6,8,-9,-9,-8,2,6,8,-5,9,-3,-4,8,6,4,10,2,-5,10,-2,10,8,4,-1,6,-9,-3,-7,4,2,3,7,1,6,7,-2,10,2,7,-4,-5,6,-7,-8,-6,10,-4,3,-8,-9,-7,-1,10,-2,7,3,-9,10,10,9,-8,-5,4,8,-9,9,5,-4,1,3,9,10,5,-6,-7,2,1,-8,9,1,10,-5,-7,-1,4,8,1,3,-9,-2,-3,-2,6,-3,7,-3,3,-3,9,-1,-1,6,9,10,10,4,10,10,-7,1,5,10,-3,10,-8,-5,-10,-3,-2,-6,-6,-4,8,10,-6,-9,4,1,-6,-9,2,5,5,-2,10,-7,-10,-1,-6,-4,-2,3,6,-5,-5,-7,10,-10,10,2,-1,4,-4,8,8,2,8,-7,-1,7,1,-4,5,-6,7,-5,-8,10,6,2,3,-5,9,-3,8,-8,-3,-8,10,5,3,-8,9,-3,-9,10,-8,10,8,-2,3,-5,-4,-7,6,-4,2,-10,-1,9,-9,-9,-5,-8,4,9,-10,6,-7,8,6,4,5,10,-10,-5,7,8,5,-5,4,8,10,7,10,-5,-9,-4,-5,-10,5,-4,1,4,-7,-7,-5,-6,3,-4,-3,9,8,-6,-10,-9,-4,-7,6,5,2,-8,-10,-4,10,-6,-7,-4,-10,9,9,-7,1,-9,7,2,-7,8,5,-10,2,-9,-1,-3,3,1,9,4,1,-1,-9,-10,3,4,2,4,-10,-10,-6,-9,6,-1,-5,-9,10,5,-2,8,4,3,7,-7,-10,7,-3,-7,8,6,-2,-2,-6,4,3,-1,-5,3,4,1,9,2,-6,-1,-6,8,5,-10,6,-6,7,5,4,4,-8,-1,-2,-8,-1,-3,-9,3,-10,2,-1,4,-8,10,7,-9,8,1,-3,2,-10,-9,5,-3,-8,-2,5,-7,-7,4,-10,10,-3,9,3,-7,6,2,-9,8,-1,-6,-8,-9,9,-10,8,-6,4,6,9,-10,1,-8,-10,10,9,-8,-1,4,2,-9,-8,1,2,-1,1,8,5,4,6,-7,-4,-4,3,4,-5,-8,-10,5,6,-5,-7,-1,-10,-10,-1,-3,-3,1,-6,1,-10,2,-8,1,5,1,8,-6,8,-7,2,-5,7,-1,1,-4,-1,-8,-5,10,-5,-2,4,-3,4,3,-2,-3,4,-3,5,5,-4,-2,-4,-1,-7,3,-2,6,-8,6,-5,10,2,-4,9,-3,-4,5,1,-6,10,-2,8,10,4,8,6,9,-9,7,4,-2,8,4,-3,8,2,8,7,-7,-6,10,-3,2,-4,2,8,6,-3,-5,-3,-2,4,-4,-7,-2,8,-7,-3,-4,5,-6,-2,-10,3,1,-8,-10,2,3,-6,2,-7,4,-7,8,4,6,-8,-1,10,6,7,-2,9,8,-10,-1,1,-10,4,10,-4,4,-1,-3,-6,-2,-3,2,10,9,-2,1,-6,4,1,-9,-10,-6,-7,3,6,-10,10,4,4,3,4,1,-7,1,9,-2,5,10,-5,-9,10,1,-1,-3,-8,1,2,-3,7,6,8,-6,6,-6,1,-1,3,3,8,-9,4,-10,1,7,1,-5,1,-1,7,7,1,1,3,9,1,8,5,-2,-3,-6,2,1,-5,10,10,-2,-9,-6], dtype = "uint32")#candidate|22142|(2535,)|const|uint32
call_22141 = func_8163_call(relay.reshape(const_22142.astype('uint32'), [13, 13, 15]))
call_22143 = func_8163_call(relay.reshape(const_22142.astype('uint32'), [13, 13, 15]))
func_16385_call = mod.get_global_var('func_16385')
func_16386_call = mutated_mod.get_global_var('func_16386')
call_22153 = relay.TupleGetItem(func_16385_call(), 0)
call_22154 = relay.TupleGetItem(func_16386_call(), 0)
output = relay.Tuple([call_22117,call_22121,bop_22137,call_22141,const_22142,call_22153,])
output2 = relay.Tuple([call_22118,call_22122,bop_22140,call_22143,const_22142,call_22154,])
func_22155 = relay.Function([], output)
mod['func_22155'] = func_22155
mod = relay.transform.InferType()(mod)
output = func_22155()
func_22156 = relay.Function([], output)
mutated_mod['func_22156'] = func_22156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15422_call = mod.get_global_var('func_15422')
func_15424_call = mutated_mod.get_global_var('func_15424')
call_22160 = relay.TupleGetItem(func_15422_call(), 0)
call_22161 = relay.TupleGetItem(func_15424_call(), 0)
output = relay.Tuple([call_22160,])
output2 = relay.Tuple([call_22161,])
func_22162 = relay.Function([], output)
mod['func_22162'] = func_22162
mod = relay.transform.InferType()(mod)
output = func_22162()
func_22163 = relay.Function([], output)
mutated_mod['func_22163'] = func_22163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16461_call = mod.get_global_var('func_16461')
func_16462_call = mutated_mod.get_global_var('func_16462')
call_22245 = func_16461_call()
call_22246 = func_16461_call()
output = call_22245
output2 = call_22246
func_22255 = relay.Function([], output)
mod['func_22255'] = func_22255
mod = relay.transform.InferType()(mod)
output = func_22255()
func_22256 = relay.Function([], output)
mutated_mod['func_22256'] = func_22256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19218_call = mod.get_global_var('func_19218')
func_19219_call = mutated_mod.get_global_var('func_19219')
call_22257 = relay.TupleGetItem(func_19218_call(), 2)
call_22258 = relay.TupleGetItem(func_19219_call(), 2)
output = relay.Tuple([call_22257,])
output2 = relay.Tuple([call_22258,])
func_22274 = relay.Function([], output)
mod['func_22274'] = func_22274
mod = relay.transform.InferType()(mod)
mutated_mod['func_22274'] = func_22274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22274_call = mutated_mod.get_global_var('func_22274')
call_22275 = func_22274_call()
output = call_22275
func_22276 = relay.Function([], output)
mutated_mod['func_22276'] = func_22276
mutated_mod = relay.transform.InferType()(mutated_mod)
const_22287 = relay.const([[[9.074498,7.221850,9.336798,6.624225,-2.360088,0.956548,-4.625476,-2.854771,3.899545,-3.955215,5.909748,-4.928652],[-9.103494,-6.312477,0.832541,9.455621,8.404285,6.989203,2.807996,-1.720359,3.134656,4.731584,-8.347141,-3.682261],[-2.069197,1.479603,5.259906,-3.173225,-9.606576,0.170963,-8.384793,4.607188,7.789851,-0.679746,0.084892,-6.252298],[-9.767765,-3.686875,-2.102012,-3.424902,-2.928940,-3.890223,8.979856,6.810407,9.549798,-9.437761,5.358258,-9.613534],[-0.026817,-2.633503,9.326804,-0.323905,-0.374073,-2.313469,8.762422,0.586475,-3.875730,-1.222749,-1.377956,-8.453874],[-2.519240,3.269091,-0.120332,-5.397341,-4.133586,-9.308859,-4.617177,8.430116,-9.585477,8.996728,0.115567,5.927809]]], dtype = "float32")#candidate|22287|(1, 6, 12)|const|float32
uop_22288 = relay.atanh(const_22287.astype('float32')) # shape=(1, 6, 12)
bop_22294 = relay.power(uop_22288.astype('float32'), relay.reshape(const_22287.astype('float32'), relay.shape_of(uop_22288))) # shape=(1, 6, 12)
output = bop_22294
output2 = bop_22294
func_22302 = relay.Function([], output)
mod['func_22302'] = func_22302
mod = relay.transform.InferType()(mod)
mutated_mod['func_22302'] = func_22302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22302_call = mutated_mod.get_global_var('func_22302')
call_22303 = func_22302_call()
output = call_22303
func_22304 = relay.Function([], output)
mutated_mod['func_22304'] = func_22304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18913_call = mod.get_global_var('func_18913')
func_18914_call = mutated_mod.get_global_var('func_18914')
call_22310 = func_18913_call()
call_22311 = func_18913_call()
output = call_22310
output2 = call_22311
func_22314 = relay.Function([], output)
mod['func_22314'] = func_22314
mod = relay.transform.InferType()(mod)
mutated_mod['func_22314'] = func_22314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22314_call = mutated_mod.get_global_var('func_22314')
call_22315 = func_22314_call()
output = call_22315
func_22316 = relay.Function([], output)
mutated_mod['func_22316'] = func_22316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19479_call = mod.get_global_var('func_19479')
func_19480_call = mutated_mod.get_global_var('func_19480')
call_22353 = func_19479_call()
call_22354 = func_19479_call()
output = relay.Tuple([call_22353,])
output2 = relay.Tuple([call_22354,])
func_22362 = relay.Function([], output)
mod['func_22362'] = func_22362
mod = relay.transform.InferType()(mod)
output = func_22362()
func_22363 = relay.Function([], output)
mutated_mod['func_22363'] = func_22363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15508_call = mod.get_global_var('func_15508')
func_15510_call = mutated_mod.get_global_var('func_15510')
call_22382 = relay.TupleGetItem(func_15508_call(), 1)
call_22383 = relay.TupleGetItem(func_15510_call(), 1)
output = call_22382
output2 = call_22383
func_22387 = relay.Function([], output)
mod['func_22387'] = func_22387
mod = relay.transform.InferType()(mod)
mutated_mod['func_22387'] = func_22387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22387_call = mutated_mod.get_global_var('func_22387')
call_22388 = func_22387_call()
output = call_22388
func_22389 = relay.Function([], output)
mutated_mod['func_22389'] = func_22389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15146_call = mod.get_global_var('func_15146')
func_15148_call = mutated_mod.get_global_var('func_15148')
call_22390 = func_15146_call()
call_22391 = func_15146_call()
func_20214_call = mod.get_global_var('func_20214')
func_20215_call = mutated_mod.get_global_var('func_20215')
call_22412 = relay.TupleGetItem(func_20214_call(), 0)
call_22413 = relay.TupleGetItem(func_20215_call(), 0)
output = relay.Tuple([call_22390,call_22412,])
output2 = relay.Tuple([call_22391,call_22413,])
func_22414 = relay.Function([], output)
mod['func_22414'] = func_22414
mod = relay.transform.InferType()(mod)
mutated_mod['func_22414'] = func_22414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22414_call = mutated_mod.get_global_var('func_22414')
call_22415 = func_22414_call()
output = call_22415
func_22416 = relay.Function([], output)
mutated_mod['func_22416'] = func_22416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18130_call = mod.get_global_var('func_18130')
func_18131_call = mutated_mod.get_global_var('func_18131')
call_22439 = func_18130_call()
call_22440 = func_18130_call()
func_12124_call = mod.get_global_var('func_12124')
func_12129_call = mutated_mod.get_global_var('func_12129')
const_22444 = relay.const([[-4.169799,-1.851372,-9.484410,3.209905,4.098815,-9.113536],[4.188544,8.354147,2.123164,1.739092,-5.724582,9.716579],[3.020081,7.918911,5.097668,-4.936700,-3.591274,-6.457675],[-6.490868,4.168296,-8.501555,8.150948,-3.505458,8.397922],[-4.629636,-7.408313,9.208350,5.191143,-0.335239,-2.367685],[8.309418,-8.745789,-4.730633,5.384263,-5.678795,-6.973149],[-3.273714,-2.015246,-4.871595,-5.525034,2.386009,9.346485],[3.751781,6.080745,1.891665,5.721022,1.195420,-8.975653],[-6.523942,-6.509569,0.093937,4.452325,-8.592565,-4.397505],[-0.108175,-5.338949,-4.759807,-5.443794,-5.197742,3.083153],[2.765084,3.615498,-6.969109,-4.520214,0.002729,-6.679428],[-9.700163,-4.074937,7.612083,6.908087,8.408397,9.073709],[-7.146109,5.127223,-5.917180,-0.870398,-5.120207,-0.238683],[-4.510490,7.856324,9.432500,-0.313286,-4.395181,5.121807],[0.435366,8.792037,-9.283615,-5.487286,-3.133590,5.990978],[1.793586,-2.316287,1.645590,-5.389490,-8.405325,3.342851],[1.492880,3.882806,-8.481319,-9.158854,3.396652,5.268231],[-9.393649,-5.365328,8.894445,2.180565,-8.350070,-5.457874],[-6.802022,5.073457,1.037281,0.164493,-2.792715,-6.489520],[7.780433,-1.917587,-2.416863,-3.155116,-7.992208,0.995365],[-9.962300,-7.078847,-2.165804,7.096420,9.112875,5.254992],[9.194703,-3.346110,8.192925,4.123217,1.843130,-6.020008],[0.116739,-8.706474,9.973234,3.055678,1.877189,-6.275008],[6.712490,-1.807338,-3.678307,0.928969,-6.909825,3.830518],[-0.711587,-1.427303,5.225137,0.748762,7.647058,-9.534100],[7.577324,7.284418,9.773203,-0.431013,0.517774,7.465661],[4.500508,0.715489,-0.880408,4.713800,2.080764,-4.557894],[-4.422829,5.829820,-5.960156,1.652798,-4.344864,-1.482589],[-0.482394,-4.315207,0.708349,-8.817009,-5.973791,7.509550],[-9.298755,2.527632,-0.180850,-5.504716,0.279578,4.854037],[4.167142,4.858551,4.229423,6.887314,-8.476970,4.512023],[-4.615105,-1.404108,1.572951,7.271300,3.282145,-8.866055],[7.875932,-9.490378,-1.264013,-6.855570,-2.033477,3.790251],[3.681187,-8.261737,-7.771384,7.884388,0.128157,2.483018],[3.827566,-4.925985,6.662097,1.722271,-9.059675,1.388182]], dtype = "float32")#candidate|22444|(35, 6)|const|float32
const_22445 = relay.const([9,1,-3,10,-10,-2,-8,1,8,-8,-6,-2,2,8,-9,-6,-8,-2,9,1,-5,-4,3,4,-5,-6,7,-2,1,-10,-1,-1,-3,-2,-6,-10,7,-5,9,-4,4,-9,-7,-2,3,9,8,4,4,2,8,1,5,-6,5,-1,9,2,3,4,-7,9,-4,7,-9,-8,-10,-2,4,1,9,10,4,-2,9,-2,-3,-2,-3,5,-9,-1,-9,-3,-3,4,-8,8,8,10,9,6,2,9,8,-9,4,-5,3,7,4,-7,-6,6,-8,5,-8,-1,8,4,-1,-4,-3,9,-7,-3,8,5,9,-9,-8,6,5,6,7,-3,5,3,-4,-3,9,-4,-7,10,-2,3,-5,-6,6,6,-4,-2,-4,-4,-7,3,-4,-10,6,7,1,8,8,-6,7,-10,1,-7,-8,7,-9,-1,7,-6,-3,3,-10,10,8,-6,6,-6,-9,3,-8,-3,1,2,7,-3,8,6,8,9,10,2,1,-4,-5,-8,-9,9,-4,10,-10,2,8,7,-2,3,-4,-9,-5,7,-1,-10,-3,2,2,9,-4,2,-8,9,7,-3,9,6,-6,3,-6,-10,3,-6,-4,9,-5,10,-9,-7,-3,7,-4,-7,8,10,2,-4,-3,-4,-7,-3,-3,8,-1,8,5,7,10,2,5,-1,3,4,8,-1,10,-5,-6,-4,-8,-5,8,4,8,-6,-9,10,2,8,-3,-5,4,5,-5,-10,-1,-5,7,-7,-7,-9,-1,8,4,-3,6,1,8,-1,5,5,6,-5,1,-9,-6,-7,-7,10,1,-10,3,-9,9,5,1,2,-2,-8,10,3,6,-4,-5,4,-2,-4,-8,-8,-3,3,-3,-9,1,-9,-7,-8,4,-5,10,8,-8,7,-5,4,-5,4,-9,4,2,-10,10,5,-2,5,-2,4,-5,-7,-3,2,6,-8,9,-5,-9,-4,-5,-5,9,-8,4,2,-2,-2,10,3,-10,-2,-4,1,-4,-2,-4,-5,-8,-6,7,-4,7,-2,-1,-4,7,-1,-3,-6,-9,-3,9,6,2,-10,9,6,9,2,6,-3,10,-7,6,9,4,-8,1,-10,3,-2,5,8,-9,-6,-6,9,2,-10,-1,-4,2,-8,4,-8,2,-1,9,1,-2,4,-7,-6,8,7,-9,-4,5,-6,4,7,-3,2,-10,1,-1,1,-7,-9,5,6,-9,4,6,2,-5,5,9,-1,2,2,6,-3,10,-2,8,-8,-10,-8,4,6,10,7,-1,-8,-10,-6,4,3,-1,-9,-3,-3,-9,7,4,-1,7,4,6,-10,-2,5,8,-10,-3,6,-5,-6,4,8,-9,10,8,-3,-6,3,9,-6,7,6,4,-5,2,5,-9,2,5,3,6,8,-8,1,-10,-6,4,7,3,9,7,9,-9,3,3,-7,-9,2,-5,-5,-2,2,-3,4,-2,9,-8,-5,-1,1,2,4,3,1,9,-3,-8,-4,3,-7,2,-2,6,7,6,3,4,-3,3,6,-3,2,-3,4,-6,-9,-9,-9,10,2,4,6,-3,6,5,8,9,9,6,-8,-4,-1,9,8,5,-5,-7,6,2,-6,2,-4,1,4,7,-2,-8,2,4,-7,1,-8,5,-8,8,3,-5,-2,10,-8,8,8,4,3,1,6,2,-10,-10,1,2,7,-2,-6,6,1,-3,-2,-10,-2,5,-7,-4,1,5,1,9,-5,-8,3,-4,-2,3,3,-10,-6,-4,9,10,-1,5,2,-9,-3,9,-5,-8,9,2,5,-8,-5,6,8,8,-2,-1,-7,1,-1,7,3,-4,9,6,-6,-6,7,-6,7,4,7,4,-8,-5,7,-7,-7,7,-5,-9,9,1,-9,-9,-1,8,10,3,8,9,7,-10,-4,-2,9,-9,7,4,-9,4,8,9,1,8,-9,7,-2,2,-3,7,6,-2,-8,-10,-9,-8,-4,7,-8,-7,3,-2,-10,-2,-7,-6,-7,-7,-3,1,-9,1,5,-1,6,-7,-3,-7,-3,7,-10,-4,-9,9,6,-6,-8,-8,-8,5,8,-4,-10,7,9,-3,5,3,8,10,5,-9,-4,5,8,7,-1,1,9,7,2,-7,7,2,4,-9,7,-2,-7,-4,-9,4,-1,3,5,-8,-10,-3,-4,4,7,9,-3,7,-9,6,-4,-10,-7,5,-5,-6,-9,-3,6,-3,3,8,-2,-8,6,1,-6,4,-5,5,3,2,2,5,5,10,-9,-3,-3,-5,7,-10,-6,8,5,-9,7,-8,-9,9,-10,-1,7,-3,-7,1,2,-6,-6,-10,-8,-9,4,-3,10,-6,-1,1,-3,10,1,-3,-1,-3,-3,-7,-4,5,-4,1,-2,-4,6,-3,-8,-6,-2,-3,-7,-1,-9,-9,-7,-3,5,-4,-2,10,-2,4,5,10,-8,10,9,-6,-2,-3,1,9,-1,1,-1,-1,5,4,7,7,7,1,-9,-4,3,-9,5,-8,-10,2,-3,4,-8,8,-2,-1,2,-3,-10,-3,4,5,9,6,6,1,-10,-7,-5,4,-10,6,-6,3,8,8,10,-1,-9,-10,-6,-4,10,-5,-8,2,-3,-8,-9,-4,8,7,7,7,-7,-3,-10,9,10,-4,-10,-6,7,3,-6,-1,1,2,-7,4,-10,9,3,1,-2,2,1,7,2,4,-9,4,-4,-7,-7,-7,7,-8,-5,-6,4,-1,7,-3,-9,7,-1,-5,-7,-5,5,-5,1,-5,-2,5,10,-1,3,-6,-2,-8,3,-7,8,-9,8,-5,7,5,-2,3,4,9,-1,-2,7,5,7,-2,-6,8,-5,2,7,-1,-6,1,10,1,-4,-4,5,10,-1,-5,-5,2,-9,4,-10,5,9,7,-5,-1,-1,1,-6,6,-5,-6,-7,2,1,-2,-9,8,-2,-9,5,-7,7,-4,10,10,-4,-10,7,7,-8,-10,5,-6,4,3,5,10,7,-5,-6,6,3,1,8,7,-6,-2,6,-7,1,-2,7,10,-5,-4,-10,-1,6,3,1,-9,-7,-9,7,3,-3,8,-6,5,-3,-4,-9,6,-8,-9,-8,-7,9,6,-1,6,4,5,2,5,9,8,8,-5,-2,-7,-3,3,-2,8,10,9,-9,7,-4,-7,-4,3,9,-8,2,-9,-2,9,-3,-9,-4,-8,1,-6,-8,8,-10,-3,8,-9,-1,-9,5,8,6,3,-6,-3,-6,1,-4,7,-9,4,-6,-10,-5,9,-7,-10,-4,3,3,4,6,3,-4,5,-3,-3,-4,-3,1,1,-8,-1,3,10,-9,-5,-2,7,1,1,3,-2,-8,7,8,7,8,-8,-3,7,5,-9,10,-4,7,4,9,6,4,7,3,8,4,-2,-4,-9,9,-5,3,10,5,10,2,3,9,-8,6,4,3,6,-5,8,4,-4,3,7,-10,5,-2,9,-10,4,2,7,5,5,-10,-5,6,-9,3,-8,2,-4,2,6,10,-10,-9,10,-10,-4,-7,3,8,2,-10,4,-6,4,4,1,-9,10,8,2,4,6,-4,-3,-5,-6,9,-4,-10,6,10,10,10,7,-10,4,6,-5,3,5,-5,10,10,-1,-6,-4,4,-6,-4,2,4,7,-8,-2,-10,-8,7,1,5,10,10,-8,10,9,-10,9,7,-6,8,-9,-5,7,6,-1,-1,4,7,-6,-7,2,-5,3,-6,-10,-7,5,5,-5,-10,-4,7,2,10,-2,4,6,6,-1,10], dtype = "int16")#candidate|22445|(1404,)|const|int16
const_22446 = relay.const([[0.700343,-8.909294,0.939488,9.906894],[5.121414,-6.388959,-8.364160,-6.891216],[6.227260,-9.142986,-0.139503,-6.089932],[5.334717,1.602609,3.781227,-9.638574],[-7.922456,-7.496006,4.328408,2.666479],[-8.032962,7.350975,-5.639741,-1.108243],[-5.051265,2.332843,1.018885,-0.565193],[0.447822,0.148948,7.077598,8.568181],[-5.100163,5.866577,-3.326682,-2.605801],[5.253009,4.638974,3.395249,5.091643],[-2.050502,4.087332,-3.486484,1.201604],[2.281369,-4.584536,-1.600817,-2.059580],[-6.747428,-4.673022,-7.492162,5.072916],[7.513756,-5.615886,-7.490710,-6.784900],[-0.768033,-5.800745,2.584595,6.499939],[-0.324028,5.207350,9.387888,-6.122584],[-9.068564,-1.580353,2.156973,-2.987796],[5.731388,-4.507750,-5.271156,-0.215185],[-2.448166,-9.120103,-8.080516,-5.404052],[1.759862,1.199753,5.109843,-3.732269],[9.134504,4.034139,-1.980322,6.287448],[-9.973480,6.263350,-2.541485,3.851793],[1.681205,-0.604517,1.376957,-2.670688],[-1.509269,-6.985671,5.435155,7.698926],[9.711451,-5.579736,-5.617761,4.029759],[1.151536,-6.835379,9.026934,-7.002136],[0.292969,-1.230656,1.904742,1.380638],[2.040316,3.560468,4.664896,8.795281],[7.871306,-4.881061,5.258189,-6.065290],[3.421813,-3.539083,1.007389,9.122768],[3.301122,2.479184,-2.979582,-6.666473],[-9.012770,3.221641,4.624244,1.964519],[-8.255668,-4.695631,1.347176,-5.380717],[8.324939,9.763486,6.315523,6.045236],[8.833573,7.975227,-3.929460,0.778814],[7.596218,-6.532030,1.718156,-6.662309],[8.663993,3.532659,0.849991,8.548210],[-1.808461,6.801945,7.746344,-4.882024],[-3.617474,8.340059,2.233054,5.003836],[5.413576,3.202843,0.834783,-8.868195],[4.478261,-3.037647,6.360995,3.396833],[-3.301687,3.846566,-5.528868,-7.005666],[0.842189,3.996918,-6.307251,6.146076],[-3.890072,-2.755902,-0.802433,-4.730310],[-1.901719,7.049858,6.324812,1.434412],[8.954190,5.215213,-5.951717,-2.112714],[8.278471,4.242683,0.160079,9.460299],[0.603674,4.048695,-5.188566,8.739087],[-1.171211,-4.610624,-4.915333,-0.061169],[-2.527080,4.829671,0.977730,-9.347883],[1.749003,7.403886,1.082907,-5.383247],[-3.168816,-0.147439,3.039186,-4.895970],[-4.674478,2.389471,-7.227934,1.595257],[-2.950659,-3.323385,-6.464725,-1.936690],[-9.840971,-7.331096,8.947329,-3.103221]], dtype = "float32")#candidate|22446|(55, 4)|const|float32
const_22447 = relay.const([-7,-6,5,-4,-5,6,1,4,-10,-2,10,1,-8,-9,1,4,4,4,9,2,8,-7,1,9,-8,4,-8,3,1,7,-3,10,2,-7,-2,5,6,-9,3,-10,8,8,8,-3,3,-1,-10,4,-4,3,9,-6,-1,-3,2,3,7,7,3,4,-10,2,5,4,-6,-5,-6,-9,-7,-1,-6,-10,-6,-8,-5,-6,-7,-8,6,-2,-8,9,-2,-1,1,-10,6,9,5,4,-8,-6,3,-7,-6,3,-8,8,-1,10,10,-8,-8,-2,-2,2,9,7,1,-10,3,-1,-6,-2,7,-6,10,5,10,-10,4,-4,-9,4,5,9,7,-10,10,-9,-5,-5,-10,-2,10,5,-3,6,10,-6,-3,-2,6,3,-5,2,-9,5,-9,-2,-1,2,5,-10,7,-1,-10,1,6,-1,-8,3,1,-7,-6,-7,5,3,-7,-9,8,5,3,-5,9,4,-10,-5,4,9,-2,-9,6,-8,-6,7,5,3,9,-10,5,-8,-10,7,-6,6,-5,-4,10,5,-9,1,6,5,-3,6,9,-4,-6,5,-9,1,-7,-8,8,-4,-8,10,-8,-1,-10,-8,2,7,4,1,4,-9,6,-9,-1,-1,7,-6,8,5,-6,-8,6,-6,9,4,-1,4,10,-4,-8,3,8,-10,7,-6,-10,-1,10,-5,-7,2,-1,7,-10,4,8,3,7,2,-1,-6,3,-7,7,3,2,3,-10,7,-3,-7,-10,-5,-4,-10,-7,5,-4,-4,6,-6,-3,-2,-1,-2,-3,3,7,-10,-9,5,-9,-8,3,-5,-9,5,-9,-4,9,-3,5,6,8,-3,8,-2,8,-1,2,-8,-4,3,-2,-2,-5,3,-4,1,5,-8,-4,2,-2,3,-9,-7,3,-4,8,-8,-2,-10,8,-8,-7,-9,-9,-3,6,-3,6,-5,1,-6,9,10,2,10,3,-4,4,-1,6,2,-1,-6,6,-6,3,5,-3,-5,-7,7,-3,-10,6,-10,7,-6,-10,5,-4,-4,-10,-10,4,-10,-10,-10,-9,2,4,-10,5,-9,-8,10,5,2,-10,8,10,4,-4,7,-3,-9,-8,-7,-6,-7,-3,8,-8,3,5,-2,9,8,-8,-9,1,-9,-8,3,7,6,-6,9,-7,2,4,-8,1,10,-9,2,6,3,2,-6,6,8,-8,-6,9,-8,3,8,2,-3,7,-2,-1,-7,-1,-9,-4,-10,5,-9,5,9,-3,-10,-5,7,2,-6,-4,-3,3,5,10,4,-3,-10,-2,4,6,-2,1,-4,9,-4,-3,10,-9,-5,-10,4,4,2,3,-1,2,-1,-3,3,-6,-4,4,-5,9,-9,1,-4,9,10,2,2,-5,4,-9,9,-4,6,-5,8,-3,4,-4,8,4,5,9,9,-10,3,10,7,-3,1,-4,-3,-9,2,7,7,7,-7,-7,2,1,-7,5,6], dtype = "int64")#candidate|22447|(546,)|const|int64
call_22443 = relay.TupleGetItem(func_12124_call(relay.reshape(const_22444.astype('float32'), [3, 7, 10]), relay.reshape(const_22445.astype('int16'), [9, 156]), relay.reshape(const_22446.astype('float32'), [220,]), relay.reshape(const_22447.astype('int64'), [546,]), ), 7)
call_22448 = relay.TupleGetItem(func_12129_call(relay.reshape(const_22444.astype('float32'), [3, 7, 10]), relay.reshape(const_22445.astype('int16'), [9, 156]), relay.reshape(const_22446.astype('float32'), [220,]), relay.reshape(const_22447.astype('int64'), [546,]), ), 7)
const_22453 = relay.const([[-9.791125,7.468396,4.212571,2.223091],[6.119344,-4.273822,6.546012,-6.130386],[-7.538902,-2.225475,6.520892,-8.392888],[-6.363778,-1.894311,9.071233,-8.483001],[1.949474,-1.915271,5.381998,9.798125],[6.688144,1.829241,-3.226339,7.414947],[-9.765340,-7.826080,9.839264,-7.988290],[-1.411686,8.519784,6.988456,4.369465],[6.770818,0.106287,7.583465,8.675631],[-9.519978,-7.128124,-9.375575,2.732145],[5.672851,-1.436141,6.957254,-3.485768],[-6.632446,9.250140,-8.704681,-4.362446],[1.424328,-2.745601,-6.113447,2.642712],[-7.122412,-7.596157,0.255179,-1.250557],[4.325369,7.197030,2.498017,-5.809089],[5.178875,4.121069,2.982222,7.474123],[1.920099,1.318831,6.730869,8.249315],[-8.358795,6.521022,4.909323,-7.593638],[-3.381703,1.192969,-6.981264,2.225696],[-0.308843,7.951446,-5.954091,-8.562630],[-2.551683,-0.003594,-8.406751,3.772912],[2.197356,6.010598,-6.015556,6.503562],[3.803930,1.244955,0.822404,-8.498800],[0.768110,3.628546,-8.364831,-3.301055],[4.700265,9.167815,-0.548776,7.465387],[9.448497,-2.554572,-0.967665,-3.629154],[7.096930,2.849951,2.713996,-1.213085],[1.457153,-4.233401,6.188527,-5.968261],[1.559998,-0.751771,6.455120,2.154684],[-4.789540,-7.437598,-1.650579,5.812451],[-8.688327,-8.563112,-8.071441,7.690719],[-9.173942,9.161182,-2.037437,-2.881541],[4.839887,1.028317,-5.372113,6.973908],[-0.687616,-6.024830,5.123935,-2.627913],[-6.056700,0.975903,4.986956,1.937391],[-3.345198,0.455983,-8.713668,4.344759],[2.382495,-6.181346,3.051504,-0.906658],[-4.677879,-8.820305,-4.595027,8.503845],[8.172150,7.986195,8.969503,-8.409388],[-2.864685,-3.444129,-9.820433,-8.358269],[-3.629096,3.385127,6.288487,-1.528581],[-2.575573,8.453948,4.227826,-3.193370],[4.154794,-4.638500,-3.026685,-3.901266],[-3.708832,2.190992,-9.884293,-4.748241],[1.267595,0.975829,-4.103143,-9.107027],[-3.515907,8.810010,-2.387384,1.963176],[-9.465961,1.074989,-7.038666,6.976657],[-1.021582,6.142842,-0.782058,-2.613557],[-8.254372,-1.235963,3.433835,4.587575],[-6.445024,4.318256,-7.419030,-4.431257],[-6.398190,7.787828,-8.692232,-6.211922],[-0.345688,0.106888,2.589328,-0.640997],[8.262245,-2.759300,4.276504,4.957450],[9.069239,-8.561170,9.733164,-9.462385],[-5.945738,-0.211034,-5.597236,-3.707851]], dtype = "float32")#candidate|22453|(55, 4)|const|float32
bop_22454 = relay.mod(const_22446.astype('float64'), relay.reshape(const_22453.astype('float64'), relay.shape_of(const_22446))) # shape=(55, 4)
func_19218_call = mod.get_global_var('func_19218')
func_19219_call = mutated_mod.get_global_var('func_19219')
call_22472 = relay.TupleGetItem(func_19218_call(), 3)
call_22473 = relay.TupleGetItem(func_19219_call(), 3)
output = relay.Tuple([call_22439,call_22443,const_22444,const_22445,const_22447,bop_22454,call_22472,])
output2 = relay.Tuple([call_22440,call_22448,const_22444,const_22445,const_22447,bop_22454,call_22473,])
func_22480 = relay.Function([], output)
mod['func_22480'] = func_22480
mod = relay.transform.InferType()(mod)
output = func_22480()
func_22481 = relay.Function([], output)
mutated_mod['func_22481'] = func_22481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18325_call = mod.get_global_var('func_18325')
func_18327_call = mutated_mod.get_global_var('func_18327')
call_22532 = relay.TupleGetItem(func_18325_call(), 0)
call_22533 = relay.TupleGetItem(func_18327_call(), 0)
func_11132_call = mod.get_global_var('func_11132')
func_11135_call = mutated_mod.get_global_var('func_11135')
var_22555 = relay.var("var_22555", dtype = "float64", shape = (96,))#candidate|22555|(96,)|var|float64
const_22556 = relay.const([4.688587,-1.707704,8.745182,-6.644340,-7.692724,0.518162,-3.982791,-9.636738,-3.529564,-1.070505,4.050402,-0.153941,-5.274857,-9.507161,2.701650,5.681152,-3.258970,2.797853,-4.348525,0.657521,4.212246,-2.680302,-3.580883,-5.999463,7.752308,-6.313154,-1.921904,2.581513,-3.861032,-2.681724,2.398179,-8.337001,3.018938,5.115943,-7.866128,-3.732070,2.183851,9.415675,3.643609,5.937974,-5.408312,3.726761,-4.709321,-1.219998,2.362158,5.594979,-0.349680,-8.683043,8.998008,6.598169,6.433277,4.969645,-3.858461,-0.420192,-0.036017,6.989208,9.504004,9.134716,6.713599,-5.724313,-4.421289,0.468956,-9.151599,-9.047490,7.047854,3.842975,-6.225989,1.149703,5.930109,-6.256171,3.484107,3.180379,3.115805,8.016115,-5.034256,7.772751,3.993419,7.903617,-4.051529,0.770177,7.081514,-8.537275,7.194518,4.447537,4.689799,-7.233949,4.725797,4.659328,-9.398580,7.925587,3.388912,8.178032,1.774512,-0.493236,-1.470291,8.596608,-1.564374,2.630342,4.472264,-8.823204,4.180292,-6.733168,-5.808143,9.431382,-5.157123,6.207185,9.544049,-7.796381,8.604088,-2.482658,-0.084112,-9.509086,-2.357192,-9.601648,-6.783351,-5.505349,6.579688,-9.141401,2.152615,-9.636643,-2.007926,6.118882,-0.185085,-3.040007,-4.747082,5.494607,-3.725175,6.697024,-7.599007,-3.454000,-2.948688,-6.297312,6.078244,-2.590226,-2.955561,-3.843988,-9.230849,-8.649463,6.032157,0.755633,2.788868,-7.167665,-1.836584,-6.195115,5.957732,7.264422,-6.234861,4.746502,-4.223291,-0.180777,-2.411056,5.630745,-1.242193,0.566858,-6.603346,6.275251,-3.609893,4.976927,4.768317,8.680589,-2.978710,-0.488847,-8.944517,4.498906,7.739711,2.743991,-1.926763,1.335234,-4.568581,5.365834,8.166392,-6.264755,-0.659759,-3.115529,-0.337899,5.032665,-9.318403,8.080446,5.250811,4.984305,-1.367214,6.745970,8.279755,6.458601,0.955226,-3.685509,8.334920,-0.959193,-3.655126,7.137525,-2.833300,3.295368,-3.303600,7.615382,1.378382,8.953629,1.816331,5.058189,6.904295,-7.971742,8.695217,8.527831,-4.047980,-5.194771,-4.510580,5.769026,-4.076445,6.983705,6.509247,5.500012,5.782880,-5.675835,0.932596,3.587858,-8.100416,4.204273,-8.737556,-7.616460,7.563310,5.475639,-4.329152,-6.328676,9.783484,7.278450,2.812153,-9.099762,4.531782,8.020047,-6.218622,0.453810,2.897852,-8.973203,5.651888,-2.124968,3.641181,-2.489261,-8.638164,5.084464,-7.986324,-6.812526,4.544224,-5.516594,9.479760,0.139431,-9.286149,-2.016897,5.065380,9.782746,4.389486,6.114505,3.861040,-0.068464,3.641635,-3.213641,-2.986502,9.285337,3.855390,6.063149,9.501808,-3.204499,4.363341,9.366627,6.903475,-9.216161,-2.970340,7.135593,0.099380,7.538818,1.536334,1.123831,-5.948875,4.015715,-9.969876,-0.003459,1.223453,-0.874630,5.022140,-2.550325,-1.423520,5.641768,-4.928367,0.093448,-7.126614,-1.850538,-8.972889,-8.134151,-0.601334,-9.026275,-6.640214,2.624280,1.451000,-0.694521,6.299083,1.489055,9.693089,9.865268,8.870980,-7.062218,0.076357,-4.845299,-9.641823,6.915085,-7.729684,6.408332,-0.586301,1.413027,-1.272587,1.555453,-0.085959,-3.978823,2.944434,8.031159,-3.109864,7.308829,7.996289,7.743545,-7.884492,-6.759061,-7.385595,7.124111,-1.188616,-0.830056,-6.908998,1.189315,-1.086025,5.213147,3.062678,-6.133698,-4.998898,7.306411,3.296386,5.867954,8.640798,4.879215,1.899823,6.282695,2.057622,8.575849,9.851644,-0.442397,-0.118087,2.612322,-2.720289,7.832744,8.656856,-8.565273,5.802378,-8.459739,-3.429385,-7.755081,-1.716192,6.917568,7.949253,-7.380418,3.363605,-9.298374,-3.570181,8.970540,7.833234,6.810481,-9.152329,-6.032492,3.324584,-1.385171,-3.515360,3.602681,-9.090115,-8.964280,1.217948,-5.784120,9.236312,-2.550743,3.480232,-7.453641,-7.999469,7.999898,-0.414165,-7.079825,5.206444,1.901824,0.713360,-4.360661,6.996492,9.859552], dtype = "float64")#candidate|22556|(384,)|const|float64
call_22554 = func_11132_call(relay.reshape(var_22555.astype('float64'), [16, 1, 6]), relay.reshape(const_22556.astype('float64'), [16, 4, 6]), )
call_22557 = func_11132_call(relay.reshape(var_22555.astype('float64'), [16, 1, 6]), relay.reshape(const_22556.astype('float64'), [16, 4, 6]), )
output = relay.Tuple([call_22532,call_22554,var_22555,const_22556,])
output2 = relay.Tuple([call_22533,call_22557,var_22555,const_22556,])
func_22570 = relay.Function([var_22555,], output)
mod['func_22570'] = func_22570
mod = relay.transform.InferType()(mod)
mutated_mod['func_22570'] = func_22570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_22571 = relay.var("var_22571", dtype = "float64", shape = (96,))#candidate|22571|(96,)|var|float64
func_22570_call = mutated_mod.get_global_var('func_22570')
call_22572 = func_22570_call(var_22571)
output = call_22572
func_22573 = relay.Function([var_22571], output)
mutated_mod['func_22573'] = func_22573
mutated_mod = relay.transform.InferType()(mutated_mod)
var_22627 = relay.var("var_22627", dtype = "float64", shape = (9, 6, 8))#candidate|22627|(9, 6, 8)|var|float64
const_22628 = relay.const([[[4.926507,-5.086836,8.753573,4.950180,-5.188498,0.584737,8.229666,-9.113909],[5.464167,-2.987080,3.953858,4.701489,8.034236,-8.524901,-1.060755,8.053059],[-7.079756,-5.745955,1.503922,1.819814,9.165280,1.082174,0.280448,1.817535],[-0.186881,-5.775165,3.170319,2.587258,4.848876,5.109597,-4.190328,7.988701],[-8.202943,-6.045174,-3.726444,-4.283681,-8.566124,-2.215878,9.742950,-1.318636],[-9.095416,4.254845,5.247221,-1.442288,5.522795,-8.421751,-1.218998,-2.598214]],[[2.030763,1.620045,-1.400100,4.899631,5.520211,3.786848,7.503124,-8.825195],[-8.739721,-2.430722,9.451760,4.863168,-2.709478,-3.617051,9.078180,0.200636],[7.259155,-4.146492,-0.277094,-5.273328,-0.105675,-6.226897,-6.056233,9.744711],[0.014707,-4.704259,-4.111427,3.750584,5.699025,2.868180,-0.236541,2.040485],[4.880164,-7.780138,4.744658,-0.723877,-4.361895,-7.766279,0.319608,8.607470],[0.984382,6.478609,1.102205,-5.077951,-8.497237,-7.129968,-0.706789,-6.106506]],[[7.076045,-0.499166,-3.789489,-4.919512,0.031861,4.664991,-0.687257,3.747319],[-4.302244,2.814989,6.065367,-4.059901,-2.907354,7.535875,-1.919997,-7.809885],[-3.016141,-5.822382,6.012813,7.876880,1.843835,-1.631376,4.409427,2.649258],[-3.340444,-2.182447,-1.152564,-5.975045,3.653951,-1.123171,8.060662,9.304432],[8.743517,-2.403572,4.412561,5.160724,-9.055479,-7.731944,-9.194215,2.752448],[6.752054,-5.953238,-5.249448,-7.495082,-6.869762,7.868324,9.396551,6.502333]],[[8.104760,-9.946282,2.766871,4.118903,3.274378,-2.766348,-8.977554,-0.097013],[8.650980,9.068125,9.865875,2.590499,-7.747630,-3.012668,7.501674,-2.567008],[6.983487,2.248834,7.751240,8.370966,1.740249,-4.949669,0.075004,0.473826],[7.464152,3.239475,-6.855002,0.190286,1.761828,-5.661642,7.149090,0.047787],[6.649568,-3.394681,-6.244117,0.815027,3.960357,7.942798,4.287533,4.695203],[0.737549,5.189365,5.314639,3.454795,-0.167535,2.373245,-2.041416,8.518530]],[[-9.940572,-8.914645,4.355229,-6.978979,3.557950,8.750392,-4.171766,-2.250673],[4.952375,6.352496,-9.892850,-1.630425,-8.835129,-9.635120,-3.394306,2.983143],[7.483005,3.603683,2.509205,6.917410,7.824494,2.804567,3.009363,-7.236771],[-6.489948,7.585624,-5.513007,4.997598,-3.746807,2.595444,7.872725,1.095559],[6.455995,0.897658,-0.559325,8.511552,-6.673291,5.226227,-6.464174,-6.703989],[0.323758,4.483915,1.363414,-5.538531,5.012306,2.715261,-6.724193,7.316339]],[[1.332359,1.506286,-8.820721,-5.828177,0.008077,-2.348737,0.938803,-4.471134],[7.057713,-4.610862,3.940214,-3.180733,-8.641227,6.756043,-0.583610,-0.084404],[-4.499912,4.640449,9.805537,0.607279,9.767994,-9.754725,-9.131687,7.124855],[6.150481,7.056197,-8.277849,5.308691,0.880420,-1.889082,1.000782,5.205799],[-6.306630,-1.465412,-2.566702,-1.869226,-6.872777,-5.168045,-9.527441,-5.765831],[8.580987,-7.802565,7.821140,3.849989,-0.325250,-2.020728,-6.294966,5.682262]],[[-4.247381,-5.226998,7.671453,-4.949989,-6.523866,8.801384,-5.835818,-5.576109],[9.229327,3.086118,-7.766243,2.029985,-9.725569,-0.742420,2.187008,7.482102],[-2.410746,5.521529,3.648357,3.025436,-8.153512,-2.130473,-6.608613,0.220902],[7.782830,-4.174716,9.609624,-8.864392,2.047484,-9.211634,5.914198,-9.300334],[-3.478618,9.319205,9.534252,5.823981,9.907611,-2.971094,-3.489523,1.534073],[-2.743701,4.167801,2.992855,-2.789177,-5.264704,-3.525542,-4.049036,1.523332]],[[-3.047182,-3.081344,3.364300,8.355684,2.356141,-1.980859,9.447496,7.716004],[7.566693,9.081684,2.394555,2.631180,1.011568,2.704991,-4.495609,-3.027786],[3.096653,-2.768897,-2.226435,-1.525951,4.603009,4.176268,-8.772379,9.140672],[1.518219,0.622257,-0.833038,-1.708987,-7.620914,7.031050,9.061781,1.692994],[1.525473,8.696287,6.275481,3.253671,0.716314,-5.160316,-1.847620,9.485025],[-5.565439,-8.614080,-6.770699,-1.102102,-8.334923,8.230916,9.581770,-1.761728]],[[7.219264,-8.523744,9.441638,2.739364,-9.208409,8.323345,5.269735,-1.339649],[0.008492,-8.884105,-6.369770,-2.838574,1.430486,-2.207729,-6.178342,5.909474],[-7.902878,-2.737675,3.862089,-8.515081,1.349540,-1.833056,7.788937,6.125719],[2.734041,-9.432210,-0.584398,-6.084621,-1.022985,9.912579,-1.796536,-4.007201],[-1.056360,-3.138243,3.657391,-6.228924,-3.505916,9.162642,5.262126,-2.087035],[6.616349,-0.785066,3.957342,4.590802,5.112889,-3.212999,5.198512,2.974623]]], dtype = "float64")#candidate|22628|(9, 6, 8)|const|float64
bop_22629 = relay.power(var_22627.astype('float64'), relay.reshape(const_22628.astype('float64'), relay.shape_of(var_22627))) # shape=(9, 6, 8)
func_18576_call = mod.get_global_var('func_18576')
func_18577_call = mutated_mod.get_global_var('func_18577')
call_22635 = func_18576_call()
call_22636 = func_18576_call()
func_17738_call = mod.get_global_var('func_17738')
func_17744_call = mutated_mod.get_global_var('func_17744')
var_22657 = relay.var("var_22657", dtype = "int16", shape = (585,))#candidate|22657|(585,)|var|int16
const_22658 = relay.const([-6,2,2,-10,5,3,-3,-5,-9,-3,-6,-1,-6,10,-8,-6,8,4,7,8,4,-5,-8,-9,3,-2,-9,-6,3,7,-3,-6,2,-2,-4,1,2,6,6,-1,-9,8,5,3,1,1,-4,4,-9,-2,-7,-2,1,-2,-5,-6,5,2,-7,8,-4,2,8,-3,2,-9,-2,-9,10,10,4,10,9,9,-7,-5,-6,1,3,-2,-1,6,-3,-6,6,-10,3,10,-10,-1,-6,7,1,7,-2,-1,-1,8,-3,8,-4,2,6,1,-10,4,7,9,1,-6,-8,-8,5,2,-4,-7,-7,-6,-10,-1,-9,10,8,8,7,4,2,-4,-2,4,5,4,2,-6,-7,7,-4,6,6,3,7,-9,-1,-5,-9,9,-4,-7,3,1,10,7,-4,-8,-6,-4,-8,3,5,-2,-1,-8,2,-1,1,-4,-9,7,-6,4,5,7,10,-3,-10,-9,6,3,-5,4,8,6,-10,3,-7,-8,-4,8,-4,8,7,-4,7,2,4,9,-7,1,8,-3,-2,9,-7,7,9,-5,5,9,9,-5,1,-6,8,6,-3,5,2,-9,-1,10,4,-6,7,10,-9,10,8,8,3,-4,-3,-4,-2,-3,1,-3,-3,5,-6,-7,-3,-7,-10,7,-9,4,1,-8,-10,8,-6,-8,1,10,-2,2,-1,6,-2,-9,-5,4,8,1,-2,-9,9,1,3,-5,8,10,-6,3,1,-10,4,4,-5,1,-1,8,-2,-10,-10,-1,4,-8,-10,-10,-4,7,4,1,4,7,-4,7,-3,10,6,2,5,-2,-10,3,-3,-1,2,6,-3,5,-9,-5,3,-8,9,9,-7,-8,-3,10,-3,-3,-10,-5,4,-4,4,7,-7,6,-4,-1,-6,-9,-3,-7,7,-3,10,2,10,9,7,1,3,-1,10,10,-4,7,8,-4,-3,-4,7,-9,5,-10,5,8,7,-5,-3,7,5,-5,-7,2,7,4,-3,10,-10,10,-4,-3,8,-9,4,10,-9,4,5,-7,1,8,-4,-4,1,-2,-2,5,5,-5,-2,-8,-4,-9,10,3,9,7,-2,-10,5,-7,6,-1,7,-10,10,2,-2,-5,10,6,-9,-3,-6,-1,4,9,1,-3,-3,9,-10,-9,5,7,-2,-5,7,-10,-2,3,-1,7,2,10,2,-1,4,7,4,5,8,-4,7,-10,-5,6,-7,7,5,-5,1,-9,5,-4,-9,-6,-8,-4,6,-3,-8,8,4,-3,7,3,-5,10,-6,1,-3,2,7,6,9,6,-10,1,2,-10,5,4,6,7,10,9,7,5,-7,-9,10,-4,-10,4,-2,-8,8,4,-9,7,-1,3,8,-3,-10,-3,-8,1,-3,-9,-1,-1,-2,-4,8,-8,-10,8,-10,-4,3,-3,4,8,-10,2,5,-10,-8,6,8,6,9,-5,-5,1,6,-7,-7,10,2,-9,-7,6,3,-1,7,8,-1,7,2,4,-2,-10,5,-6,-2,-8,4,-4,5,10,5,10,-9,-4,6,10,-8,-7,-8,4,10,9,-5,2,10,-1,-8,-3,-9,1,-4,3,9,6,7,-9,3,2,3,-7,-6,8,-1,-4,-5,-6,-3,-10,1,2,-10,-6,9,9,1,-2,4,10,10,-6,8,5,-2,-6,5,-2,8,-5,5,-6,-2,3,10,-3,-9,7,-2,-1,-9,7,4,6,7,-7,-7,-9,5,9,9,-6,-1,-8,-7,-7,-5,-8,-4,-10,-8,-3,2,-6,-8,-2,6,-5,-5,2,-1,6,-3,-4,-1,-6,-3,-3,-3,-4,5,7,-6,-10,5,-2,-1,2,-7,9,-5,6,-7,5,-10,-10,4,6,-10,-4,-6,-1,7,1,4,-1,-8,-6,-7,-5,-7,4,4,5,4,-1,6,-9,9,-8,-3,-9,7,6,-6,3,-7,7,4,-7,1,-1,2,-1,-4,-4,-7,8,10,-10,-4,-10,-9,-6,8,5,3,-10,8,8,10,6,6,-3,-7,-1,-5,6,7,-9,5,-8,-10,5,-10,9,-4,-7,-1,5,1,-1,-6,-2,-6,9,5,-10,-6,4,-8,5,-9,10,-1,8,-10,10,-5,-10,5,2,1,-8,9,-2,-6,6,-9,5,-3,4,3,1,8,7,-5,5,3,2,5,8,2,7,2,1,-7,7,3,-6,-1,6,3,1,-5,9,-8,-1,1,-2,-2,-6,-2,-10,3,5,2,2,-3,3,-8,7,-7,8,8,1,-7,-2,-10,-1,10,-8,9,8,-5,-9,-3,-2,-5,-10,-4,-5,-8,9,9,2,8,-2,2,-7,2,1,-2,-10,5,2,-3,-10,5,-10,1,-6,1,-4,-9,-1,8,-10,7,9,-2,-3,1,-7,-5,1,-8,-5,-4,-4,-1,-5,7,3,-5,-7,-5,-3,8,-3,6,8,-2,3,-3,8,-1,7,10,3,-2,4,3,-6,-5,5,-4,5,8,-1,-4,7,3,3,-3,9,-9,3,-8,2,-9,-7,1,-8,-10,10,-7,1,-10,-3,1,8,-5,-1,-1,10,-3,2,1,-3,-8,-6,9,-7,2,-3,2,-4,-4,9,1,5,6,-7,1,9,10,-6,-3,-9,-1,-9,-6,1,9,5,-9,5,10,-6,10,10,-1,1,7,10,-4,4,-5,8,-5,5,3,-1,9,-6,3,1,2,9,-3,1,1,7,-8,-9,10,-7,3,8,7,3,1,5,7,5,4,-7,-9,10,-1,-8,-4,-4,5,3,9,10,-1,3,9,-5,-2,-10,7,8,-9,-1,-3,2,-8,-8,2,-6,4,-8,-7,-8,7,2,7,6,-10,1,-1,-3,-9,-7,-10,-1,-2,9,-5,-10,2,10,6,5,10,-1,-10,-9,5,7,9,-2,-10,2,-6,10,6,9,-6,8,-2,-9,1,-9,-4,-4,8,-5,6,6,10,2,-7,-10,7,1,4,10,-7,-4,9,5,-3,-8,8,1,-1,5,-5,-3,2,-2,3,4,2,1,5,9,-6,6,-2,-3,-1,-10,-3,9,-6,-4,2,9,5,5,5,1,-10,5,-4,-4,-9,3,9,7,-4,4,-8,-10,-2,6,-1,-9,4,3,-2,-4,3,-3,1,8,3,-3,-3,-6,10,-2,-9,-1,5,-10,3,10,-3,-8,6,-4,-8,-2,2,7,1,2,-8,-2,1,2,10,-1,6,9,-5,-9,-10,5,-8,-3,-2,9,-9,5,-7,-5,-8,9,-6,-3,3,-8,-4,4,-5,-3,1,-9,4,-4,10,9,-6,1,9,4,10,5,-5,8,-6,-9,2,1,1,-9,3,-8,-6,-2,6,9,10,-8,4,6,-6,1,2,-3,7,3,-10,8,1,5,6,1,-9,-10,6,5,1,-7,-7,-6,-4,4,-10,-2,-4,6,10,-7,-8,-3,5,6,5,-8,6,9,-3,-4,9,1,4,5,-9,-2,-1,3,5,1,5,-4,-5,10,8,-8,3,-2,1,8,2,-6,7,1,1,3,3,-6,2,6,-2,-9,-4,-10,10,4,10,-9,3,10,-3,-9,-10,-7,-1,-2,-5,-9,-4,5,-9,-8,-3,7,-6,-8,-9,7,2,-2,7,7,7,-3,7,4,1,8,-8,7,-3,3,2,9,-4,-8,-5,2,-2,-4,7,8,2,9,2,-6,-1,-5,10,8,5,4,-2,3,-3,5,-6,7,1,-8,2,-8,-2,9,-8,-6,2,4,-8,9,5,3,-9,9], dtype = "int16")#candidate|22658|(1404,)|const|int16
var_22659 = relay.var("var_22659", dtype = "int64", shape = (273, 2))#candidate|22659|(273, 2)|var|int64
const_22660 = relay.const([[4,-6,-6,9,-9,3,4,2,5,9,9,8,-9,5,-6,-5,1,-3,-8,-8,-3,2,-4,-3,4,-7,-2,-10,-1,4,2,-8,-3,-9,-5,-9,1,10,-6,2,-6,2,4,-7,-9,-2,2,-3,1,5,-10,-6,6,6,-8,-3,-9,-10,-6,-8,10,5,8,-7,1,-8,-8,4,10,-7,8,3,-2,-10,4,3,-8,5,6,6,4,8,8,-6,-10,7,1,-7,4,3,-5,-1,-3,-8,6,6,-10,2,4,8,-8,-6,-6,-4,-10,10,1,10,-8,5,-4,6,3,4,5,-5,-7,-4,4,5,4,9,9,-3,8,2,7,8,3,1,-3,1,-7,-5,4,5,5,5,-5,-10,-6,-9,-8,7,10,-1,4,3,8,4,-7,-2,-7,6,-5,9,9,-6,-6,10,1,-8,-7,8,-10,9,-3,10,8,-4,-4,-6,-10,10,5,1,-3,-1,-2,6,-9,-9,-6,4,9,-6,-10,6,5,5,7,-4,-7,-3,-3,-2,5,-7,-2,-4,-7,-4,3,7,5,7,-10,-4,-5,-5,-5,-1,8,-1,8,-1,-6,-10,-4,-6,-10,3,-6,-6,-4,-9,10,9,-9,10,6,2,6,-10,10,-1,10,10,-9,-7,9,-1,-10,-7,-3,-8,-10,-10,2,-9,9,-5,-2,-5,1,-5,1,-9,8,-10,5,-9,-8,-3,10,-7,4,8,-4,8,-6,-8,-8,-8,5,7,-7,6,5,8,-3,-4,4,2,6,7,-4,-1,-2,-1,6,-6,4,8,3,-5,-10,5,1,-4,-9,9,4,6,-8,2,4,-6,-9,-8,-2,-1,9,6,3,-7,1,-4,5,-10,6,6,9,6,10,-10,-6,5,-5,5,1,10,9,6,3,-6,7,7,-8,3,9,-10,-4,-10,8,-9,-9,-2,3,4,-5,3,4,9,4,-10,7,8,7,-2,-5,-5,-2,-5,-6,-2,-1,4,-6,-7,-6,3,-9,5,-1,2,-2,4,-3,-10,10,-9,-7,-6,7,-3,-2,-6,-9,6,10,8,4,-7,-1,-5,8,-1,10,-8,-9,-2,7,-2,9,-6,8,2,-6,-9,5,-7,2,8,5,1,-6,7,-10,-2,8,9,-4,8,-1,6,-4,9,-2,10,-4,1,3,-7,-6,-2,-9,-10,4,-2,4,-1,4,6,8,3,-6,-5,-2,-2,1,3,-6,4,1,-7,7,-5,9,-7,7,10,-6,-10,7,-9,7,10,-4,-5,10,10,-1,8,-6,8,7,-5,-3,3,9,10,-3,9,-3,-10,8,2,-5,-9,5,4,-5,7,6,-10,2,-2,10,-10,-6,8,2,-3,-10,8,2,-9,1,-9,-8,3,-8,-4,-6,1,-7,-8,-9,-6,5,-4,5,6,-9,-4,-3,-6,-4,1,-5,4,1,8,2,7,-7,-8,4,10,-8,-2,-5,-4,-9,9,-7,-5,-4,8,-7,7,6,8,-7,5,5,8,4,-7,7,6,-10,4,-3,1,-7,-6,2,-5,2,-8,-5,-5,10,-3,-1,-3,-9,-4,-9,-4,3,-1,4,8,8,-3,2,-4,-1,9,6,-4,1,7,2,8,1,-2,7,-1,6,8,1,8,8,5,-1,9,6,2,9,-5,9,-5,7,-3,-7,1,-4,-1,8,8,-4,3,-5,10,-7,4,4,4,5,-4,-10,-2,6,7,-9,5,-2,-5,-5,2,-2,8,8,-7,1,7,8,6,-1,10,-7,-5,-5,-7,9,-2,8,7,6,-8,7,8,3,1,-8,5,-8,-4,5,5,3,-5,1,-6,7,-4,7,2,-6,7,-8,9,5,10,9,3,5,10,1,-3,-9,-5,-8,10,3,-8,-8,-6,-4,-4,-4,-2,9,4,-9,-10,-3,7,-3,-5,-2,7,2,4,10,9,-7,2,5,5,5,2,-10,9,-6,8,-9,-8,8,9,4,-1,-8,-6,-1,9,-8,-3,-2,10,9,5,-4,-3,7,-2,1,-1,-8,-6,-9,4,5,-6,2,-2,5,-10,-2,-1,8,-1,7,-10,10,4,10,-9,-7,-10,10,-9,3,5,-6,-4,2,-3,-9,5,-8,9,1,3,-2,5,8,10,-5,5,-5,-4,-6,7,-10,5,5,8,-3,-2,-3,-8,2,10,-4,9,-6,6,9,-7,8,-1,-5,1,-9,2,1,-2,-7,10,-9,-9,-1,-9,10,3,6,-3,10,-9,-6,-2,-1,9,9,9,6,5,5,-10,-9,-3,5,-10,-9,-8,9,1,4,-8,-9,3,5,5,-3,4,-7,1,-4,-1,-9,9,8,-8,2,-7,4,-8,-9,10,-7,-8,-3,10,-9,10,1,7,-9,-2,-2,-2,9,7,3,2,4,-8,-8,-4,-9,-8,-4,-8,10,6,8,-10,9,5,-5,-2,6,7,8,2,6,8,4,4,7,-8,9,-2,-5,10,3,-2,2,2,9,-9,-5,-4,4,-5,-10,-8,10,7,6,-9,9,-7,-9,3,4,-2,9,-9,7,-6,6,-8,-3,-4,-2,7,2,-4,-4,10,9,8,-9,-2,3,-5,-1,7,-8,2,-4,1,4,9,-4,-7,-1,10,-4,-8,10,7,-6,5,5,-6,-10,-7,4,-4,4,-1,6,7,-4,8,2,-5,-2,-2,10,8,-7,-4,-10,7,-8,1,2,6,6,-1,-1,-7,-9,-2,9,8,-4,4,3,-9,2,6,9,9,8,-4,-6,-4,9,5,5,-1,8,-6,-9,-3,-7,6,-3,-1,-4,-9,-5,-7,-6,-10,8,3,-1,10,-4,-2,1,6,2,4,2,8,4,-2,10,5,-5,7,-7,-7,-9,1,6,4,5,-4,9,6,9,-6,-10,-8,-9,-3,1,5,-9,-8,4,-3,-9,-5,8,4,9,-6,-10,8,-9,-6,-10,-10,9,-4,-1,-1,-3,-1,-10,-10,-4,10,3,5,-8,4,-4,-9,-4,6,-9,6,-3,-4,-1,-4,3,8,9,-9,4,6,-8,1,-7,9,-1,-7,3,9,-6,-8,-6,-4,-10,3,6,2,-6,8,-9,9,-4,-6,10,9,-10,-6,3,-1,-2,-7,-6,4,3,5,-1,-1,3,-1,7,-10,9,3,-7,-5,1,-9,2,-8,7,6,-6,-4,6,-1,-5,2,-6,-6,-9,3,-4,6,-8,-10,6,5,-2,-2,-4,5,-5,-5,-10,-5,1,-1,-10,2,1,-3,7,2,6,-2,-6,-10,-2,3,6,-4,-6,4,2,-4,-8,-2,4,8,8,8,5,-7,5,-10,8,9,-9,-9,-1,-3,-9,-5,9,-3,-3,10,-1,6,5,-6,-2,-6,-8,-1,8,-9,1,10,-9,-4,5,10,-9,1,-4,8,4,8,-8,10,-5,3,-4,3,-7,4,10,-8,-2,-6,10,4,-9,5,-3,3,5,-3,8,-10,4,-7,-10,7,5,-2,-7,-6,-9,4,-7,2,-3,-1,-3,-6,-7,-3,-7,2,-4,-5,-9,9,-4,-3,-10,-3,10,-3,-4,-1,-1,9,7,-10,-4,-5,-9,-4,-9,-4,-2,3,-8,4,-7,-3,1,6,3,-8,2,3,-10,-4,4,8,-4,7,-9,-4,-7,-5,-10,6,-9,-4,10,2,-4,6,4,-5,7,10,6,2,-2,-4,8,-10,6,7,3,5,6,7,-7,10,-8,-10,6,-10,9,-3,-3,1,8,5,-7,-9,2,-7,-2,-5,-9,7,-6,-4,-2,-9,3,-4,8,-2,-10,10,-1,-2,-5,-5,1,10,2,2,4,-9,-3,-7,6,10,2,-9,8,-6,-6,7,-7,-5,-10,3,8,8,6,-6,5,-8,5,-10,7,-6,-8,-10,-8,6,-10,2,2,3,7,2,-3,-9,-8,-1,-4,9,10,9,-4,7,-5,-6,-1,4,-8,10,-7,-2,-5,-3,2,2,-3,9,7,5,-5,8,-10,3,-1,9,-9,6,-4,2,-10,7,7,-3,1,6,-9,-1,-9,8,7,-9,-8,10,-3,-9,1,8,-1,-2,-1,10,5,2,6,-5,7,9,10,-9,-6,-7,4,4,-8,-8,5,2,9,-3,2,-10,-3,-6,2,5,4,4,-9,3,-5,10,-1,7,6,9,-7,9,-1,2,-8,1,10,2,-6,-9,-8,-10,-1,2,-8,-5,1,-6,7,-4,-6,9,-4,7,5,-2,5,3,10,3,-6,4,2,-8,7,-6,-10,-1,7,6,-2,-7,2,-4,7,10,-6,1,-4,7,-4,4,-1,8,-3,-9,5,-3,-8,-9,4,8,-6,6,-9,-1,9,5,-2,-5,9,9,4,9,9,-6,-9,-3,-3,-5,3,5,1,9,5,8,1,-8,-1,6,-8,3,7,2,-4,-4,1,10,-1,7,6,-2,5,2,10,8,-8,-3,8,7,-10,-10,10,7,10,7,-9,10,10,2,10,6,-10,5,4,-9,-4,-9,10,6,-10,-3,-2,5,-7,-2,6,4,-6,-3,2,-9,10,1,-4,9,9,-4,-6,-5,-5,-7,6,4,-2,-6,-8,3,5,-9,10,-2,9,4,-5,6,9,-9,-9,-6,-2,7,7,10,-3,-10,7,6,10,-1,2,-2,-3,5,-8,2,3,-1,-1,-2,-2,-9,-6,6,8,8,-7,10,-5,-3,-4,-4,6,9,8,2,-6,10,-8,8,6,-4,10,4,-7,-10,-1,1,-10,3,-4,6,5,-3,-4,9,-9,-4,6,-6,-4,7,-9,-5,9,-6,2,-4,-10,4,-8,-6,5,-7,10,8,-8,-3,3,7,-5,-6,5,-8,5,-10,2,-1,8,9,-9,-5,-4,-5,6,1,-5,8,7,4,7,-6,-10,7,-4,7,5,-2,10,-6,-1,8,3,5,-2,-5,-5,-10,-7,2,-3,-7,-2,-7,-8,9,-9,-7,-2,6,5,5,-10,4,1,-3,6,-3,10,-1,5,10,-4,8,-9,-2,-4,4,-3,5,4,-8,-7,1,3,6,9,-1,2,2,6,8,10,-5,-10,-7,-10,7,6,-7,-7,6,-8,2,10,1,-8,5,-9,-3,5,-5,2,4,-9,8,3,-5,-3,-9,1,-7,9,6,-4,-8,8,-6,5,-2,-9,2,4,-3,4,-8,-3,3,10,-1,10,-5,-5,3,-9,6,-3,9,6,4,3,-5,10,-8,9,5,3,10,-9,7,7,-5,2,10,8,-7,8,7,10,-8,-7,8,1,7,10,9,9,-10,1,-10,5,-10,-1,-1,-2,-2,2,-10,-10,6,-5,9,-10,-5,-8,10,2,6,-4,-4,8,9,8,2,8,-7,-2,7,3,2,6,-5,-1,4,10,4,-6,5,-4,-9,6,5,10,1,-5,9,7,2,6,3,-3,-1,2,10,-6,8,5,-1,7,-2,-5,4,4,-9,-9,6,1,-1,-5,7,-4,-3,-10,7,6,-10,10,-4,7,5,-8,-9,8,10,-5,-5,3,9,2,-9,-5,9,2,-10,-7,-6,-3,3,-7,5,1,-10,-7,6,-4,10,-3,-3,-2,-3,-7,5,-3,3,1,-3,-9,-7,-3,8,7,5,6,-6,-2,-9,-9,10,3,6,-3,-8,-2,-9,-7,2,-4,7,-6,10,5,8,-4,-8,2,-4,-10,7,9,-9,-4,4,8,10,6,6,9,-7,-2,3,8,-1,2,-2,-8,9,2,2,7,-7,-3,-6,7,-9,-8,-7,2,5,-7,-8,10,7,-3,3,2,-4,-3,9,-4,2,-1,-6,-4,10,10,6,-5,3,1,-7,7,8,-2,1,5,5,10,-2,4,8,8,-5,5,1,3,-9,-9,-10,3,-6,5,-6,-3,-1,-10,1,3,3,4,-5,1,-7,10,3,9,4,1,10,10,-2,-2,-10,-9,-6,6,9,-5,10,-4,-1,-4,-8,4,-2,-1,5,-7,2,-6,10,8,-1,-8,10,-8,6,3,9,-5,-4,-5,-2,3,-2,-10,3,4,5,-5,-5,-6,-4,-8,-8,6,-9,-10,5,5,-2,-2,5,9,9,4,8,6,9,-7,-6,9,-5,-6,-2,-10,8,-1,7,4,5,-1,-8,-5,2,7,8,-3,7,-5,-2,5,-8,-4,8,2,-6,6,-9,-4,-4,9,7,7,3,2,9,-7,6,6,9,-9,1,10,6,-1,5,6,-1,-5,-5,2,-6,2,10,8,-6,-6,-10,-6,-2,-1,-6,8,-8,-2,10,8,2,-8,8,6,2,-2,10,-3,5,-9,10,6,10,2,1,6,10,10,9,-3,-9,5,10,-4,-1,6,2,-9,2,-2,1,-10,1,8,-7,-3,5,8,4,-2,6,-6,2,1,-7,8,-3,9,-8,4,-2,-4,4,4,-3,-5,-6,7,6,-1,5,3,8,1,-2,1,-3,1,-6,-9,1,8,-5,-7,-7,8,-10,7,6,3,-3,2,-1,5,-7,-8,8,-10,-3,8,7,-9,6,4,5,9,-6,-6,-5,-6,-7,3,-10,-10,7,-4,-3,-1,2,2,5,-5,-4,9,4,-2,-10,8,-5,5,-6,8,4,10,-7,3,-6,4,-1,-7,-8,8,3,10,-4,-4,5,-2,3,5,8,5,-6,4,-2,4,2,-10,8,5,-4,-6,10,8,-2,5,-2,-4,9,-10,10,3,-6,7,10,9,10,4,3,-5,-6,-7,-1,1,-10,5,4,10,-10,5,-8,5,-2,-7,-1,-2,-3,9,3,-5,10,-10,7,-4,8,8,-6,1,-2,-2,9,1,-6,-5,10,-1,2,-5,-1,6,8,5,-7,-3,5,3,3,7,4,-8,5,-5,1,4,8,-3,-3,4,5,10,-5,7,9,-7,7,9,7,9,-5,9,-4,-2,3,9,-3,9,4,-6,-9,7,-10,-9,2,4,10,1,-8,-1,6,8,-10,7,-4,-6,8,10,-10,5,-5,-7,4,7,10,-2,9,-8,-8,1,-10,4,10,5,1,10,-9,-10,-9,-7,-6,-7,-1,-4,-2,1,-3,9,7,3,-4,-3,-2,-7,2,9,-3,3,-5,-2,-1,10,-6,-7,-5,-2,-5,-3,9,-7,-6,-9,7,2,8,-9,-7,-4,8,-5,-4,-1,3,6,-5,-3,3,9,-5,-10,-5,3,-7,-4,-8,7,7,3,-1,-1,3,-7,-7,4,7,4,-2,3,-2,4,5,4,-9,-1,-5,7,6,4,-10,5,4,-9,-4,4,1,-10,9,-8,10,-1,2,4,-3,3,-9,-1,8,7,-6,10,1,4,3,-10,-3,-1,-8,3,5,5,4,7,7,4,9,1,-3,1,8,2,-10,-6,-7,-10,-7,-8,-10,-3,-1,10,-2,-1,7,2,3,7,-4,-4,6,-5,8,3,8,-6,-4,10,-9,-8,1,2,-3,-9,-5,-10,-6,1,-8,-3,2,-5,8,-10,-4,-3,-2,1,7,-2,3,-1,-5,-5,9,-9,-7,-7,10,2,-10,3,2,-7,3,1,-9,7,5,9,9,-6,2,3,-5,-10,-10,6,6,-2,1,5,6,-6,-3,8,4,-10,9,2,8,8,-4,3,6,-9,9,-10,7,9,-2,-1,10,5,-5,-1,7,-3,4,1,9,8,5,6,-4,1,9,2,-5,9,4,-3,9,-1,9,-4,3,10,-10,1,9,-1,6,-10,-2,1,10,6,9,4,-1,-10,-8,4,7,3,-9,-6,10,8,-6,-8,4,-8,1,-2,-8,-9,-3,6,8,5,6,4,9,7,-10,4,9,6,-3,4,-3,10,6,5,7,-3,1,-8,9,8,10,-3,3,1,-2,-7,-6,10,-3,5,-4,3,-8,-8,6,-6,7,7,3,-7,-3,-9,-1,10,-1,-6,-5,-10,1,10,3,6,-9,3,-1,8,-5,2,3,2,10,1,-8,-10,9,8,8,-4,-9,1,-7,3,-4,-8,10,3,1,-7,6,-9,5,-9,-3,10,-1,-1,9,-8,2,10,-9,2,-8,10,4,9,7,4,2,-2,-6,9,9,-8,7,-3,-2,6,-5,4,-6,-3,-10,4,3,-2,1,6,-1,2,-2,-6,-1,-4,9,-8,-10,9,-7,1,1,1,-9,1,-1,9,10,-2,6,-7,-4,1,3,-6,-10,-2,-4,-2,-10,-2,8,6,5,-8,4,7,2,5,-7,-8,2,10,1,-9,-7,-3,2,-4,7,-9,9,2,3,7,-10,7,-4,-8,-8,-5,-5,1,-8,-6,7,10,1,-7,1,4,-10,-3,-9,9,-5,-4,3,-10,10,-9,-1,-3,1,5,-6,3,-4,-10,5,-10,-6,-5,-10,1,10,7,9,2,-1,-1,-9,-7,-1,4,8,10,-2,2,-9,4,-5,1,-2,-5,3,2,-2,-3,-5,1,-4,-7,6,-8,2,-4,-2,10,-7,7,-1,-2,-9,8,-3,-7,-9,-3,4,8,3,5,-7,9,2,-6,6,-7,-4,-1,1,-3,-4,5,-10,-4,-7,10,5,-9,-9,9,-4,2,-1,-2,1,-5,6,1,-7,10,-5,9,2,-7,3,-6,-4,3,-9,10,-4,5,6,-3,2,-8,-4,8,-5,6,-3,-4,-9,4,4,10,-8,-8,-10,1,4,10,6,-5,3,8,-4,-4,-1,-4,2,-5,-8,9,5,9,-9,9,-7,8,-6,7,-1,4,1,1,2,6,-8,-6,-4,2,6,-1,-8,4,-7,5,-3,-2,-8,8,10,8,6,10,-10,3,8,10,3,9,4,8,4,2,4,2,1,-1,-3,-6,7,-1,-5,8,-5,-8,2,8,7,-10,9,6,-9,6,-9,-8,-4,-1,10,-7,-8,-5,10,-10,3,-1,-9,10,-5,3,1,-2,10,3,5,-6,4,5,5,2,-3,-10,-1,2,9,2,7,-6,-7,7,-1,-7,6,-1,-7,-1,-8,-5,-3,5,-4,-3,-10,8,-2,-3,9,9,10,-8,-5,-9,2,-3,3,-9,6,-10,3,-6,-2,-7,7,-8,-8,-7,-7,-7,10,-8,-8,4,8,-10,1,-7,7,3,2,4,-10,-4,-5,10,10,2,4,4,9,5,4,-2,8,6,1,-1,-8,9,-5,-3,-6,5,-1,4,-4,2,2,8,1,9,3,2,2,-7,2,-2,-4,-8,5,-9,-10,-7,-4,2,9,9,9,3,5,-8,1,5,6,-4,-7,10,-1,2,1,5,3,-4,-9,6,9,3,6,7,3,-5,-2,8,3,3,1,-6,1,-1,-8,-6,-2,9,5,4,-7,8,3,7,5,-1,-7,5,8,-10,-2,5,3,4,2,-8,6,-2,-2,-6,-8,-3,6,5,-1,-2,9,-9,-3,-2,2,8,4,10,9,-2,4,4,-3,-6,3,-9,5,-5,-2,5,-7,-3,-3,8,8,-10,5,-4,2,3,8,-10,-2,1,-3,8,-1,2,6,5,10,-10,-3,1,2,3,-8,3,7,1,-2,10,4,7,-2,5,10,-6,10,8,-3,-4,-3,8,2,-10,2,8,-3,-7,-7,-8,-10,2,2,-3,-3,8,3,8,7,10,7,7,-4,5,-7,-2,7,-6,-6,-6,4,-6,9,-4,1,8,-3,8,-7,1,-7,-10,7,-3,-5,-5,-2,7,7,10,5,-8,2,8,-10,-3,3,1,-1,4,-5,6,2,-1,-5,8,10,8,3,-1,-6,2,-2,-9,9,-1,-4,2,-10,-6,-7,-3,-10,8,1,-6,6,6,1,2,-3,-2,10,5,-10,-3,5,1,10,-9,-1,-8,3,6,1,3,9,-1,3,6,-8,8,6,-1,1,7,-4,-8,9,2,1,2,-3,8,-10,7,7,3,7,10,-3,9,-2,-6,-2,-8,4,-3,-6,2,9,-6,-7,10,3,3,8,5,10,8,-2,4,-10,-2,2,-2,5,7,-9,9,8,-9,-3,-4,-10,6,-3,-7,-1,-9,2,4,-1,3,-10,1,-2,4,-7,-10,-3,8,-9,8,1,-3,-9,4,1,-10,-8,1,-1,9,5,6,8,-5,6,-6,-1,4,7,-1,-5,-1,4,-5,9,5,-3,-2,-7,-7,2,-2,4,4,3,-2,-10,3,7,9,2,-9,-6,-8,-10,8,8,-5,-7,6,6,-10,2,-10,-1,-2,4,-10,4,5,-2,-4,-2,-3,-9,9,-8,4,2,7,-5,-6,2,-3,-3,10,3,6,-4,4,-9,-3,-4,6,-2,-1,6,10,-5,-4,-1,-4,8,-10,10,-10,-1,-5,-9,-2,6,2,5,9,4,8,10,2,3,-2,7,3,4,-4,-1,-6,4,-8,-9,-8,-2,10,10,10,3,-8,6,10,-9,3,-3,-6,6,-5,-1,-9,7,5,-9,-5,-10,7,-4,4,-1,3,7,-2,-3,9,8,-9,7,-6,-10,1,4,6,4,3,-8,-3,8,-9,2,7,5,-7,-9,-9,2,10,7,-5,-7,-8,7,-9,7,-5,5,-9,7,3,8,8,-3,7,-6,2,-1,8,4,-2,-7,-9,1,3,5,8,9,3,-6,-1,-5,6,7,-5,-3,-1,-3,5,2,4,5,9,7,5,6,-4,10,10,-5,-8,1,-1,4,10,5,1,5,-3,6,4,3,-5,-7,2,-10,-10,-2,7,8,-1,-1,-2,-6,7,-2,-6,-10,-2,7,-8,-6,10,-3,5,-4,2,-1,-2,-1,1,-1,-10,1,7,-6,7,-7,-10,-5,10,1,5,-10,3,7,5,-2,-8,-7,-2,-1,-4,9,-7,-9,2,-2,-6,-5,4,-2,9,-3,8,9,2,-1,8,-2,-2,5,3,-2,-2,9,-8,-4,-4,1,9,-3,2,9,4,7,2,-2,1,-7,1,-8,6,6,-1,3,-1,-10,10,4,-9,-10,5,8,-5,9,-1,-7,-9,7,1,9,-6,-4,-8,-10,1,2,1,-2,-6,-4,-7,4,-3,-9,2,-6,-7,-7,-1,6,7,10,7,-6,-4,-8,3,-1,4,3,-8,-4,-3,1,-8,-8,2,-4,-1,-2,3,7,3,-4,-8,10,-8,-10,-7,-5,-8,9,4,-1,-6,-1,4,-6,-6,1,-7,-1,-7,-6,-1,-7,-5,-1,2,3,6,8,1,-4,-4,4,-7,-6,5,-9,2,-7,4,7,1,-7,-5,-6,9,-7,4,4,-6,6,-10,-8,-10,-3,-3,4,4,3,-6,-8,-9,-8,8,-6,10,-4,8,-7,6,-5,-2,-3,8,-6,4,-9,-10,-8,7,-3,-6,9,10,2,-6,5,6,4,5,-10,5,4,6,-4,-3,-2,-3,-5,-9,-8,-6,4,-2,-9,10,8,1,-3,-1,2,1,7,6,-8,2,1,9,-1,-6,2,2,-5,1,7,-2,-7,2,-8,7,3,-2,-7,-2,3,-1,-7,-4,-3,8,-6,9,-5,9,-9,-1,-6,-9,-3,-3,10,-3,6,-9,2,-1,10,-2,-2,10,9,-6,-4,10,-7,-8,-9,-3,-8,-4,-10,9,-4,6,-3,-9,-2,7,-1,5,-2,-4,2,5,-2,10,-3,-3,-9,-5,9,-5,9,7,1,-8,5,-3,1,-8,-7,4,-5,-9,8,-7,7,8,-3,6,8,-8,-7,-9,9,1,6,-5,4,7,7,-1,-5,-10,5,-4,-9,-4,-3,7,2,5,-5,1,4,1,2,-4,2,-7,10,-8,4,-7,6,-9,10,-8,-4,-4,7,-2,9,5,-1,-6,4,10,-5,6,-1,-10,9,-7,7,5,-9,2,-2,9,1,-2,9,-4,-1,6,5,4,-3,1,10,-3,-3,-7,6,-6,-1,-2,4,-5,-8,6,6,-1,1,-9,8,-2,-9,-5,6,1,-2,8,-1,-1,-5,-6,9,1,9,-10,2,-9,-10,-5,6,4,1,3,6,-2,-3,3,8,-1,-4,6,-1,-8,-9,-7,-8,-2,4,10,-9,4,-5,-3,3,-9,-3,2,2,-8,2,4,8,-1,-1,-4,-5,2,5,2,9,2,6,9,5,-9,-3,-9,10,3,10,2,4,-7,9,-7,-1,-10,5,7,7,9,8,10,7,-9,-1,-6,5,5,3,2,-3,2,-2,-9,4,8,7,2,-9,5,-2,-6,4,-10,-3,10,-5,-3,-3,5,-2,1,-8,5,4,9,1,-4,7,2,4,-4,-6,7,1,7,4,-3,1,-2,-10,-2,6,-3,-7,1,-7,-4,5,-2,-3,10,-7,2,4,4,6,-2,9,5,2,-1,2,4,7,6,5,7,-10,1,-2,-8,8,-9,9,4,10,10,3,3,-10,-7,-4,8,-1,10,1,-10,-7,-7,-4,8,8,-8,-4,8,10,10,10,-10,4,-4,5,5,4,-10,2,-4,10,3,5,-9,-9,-8,6,1,5,6,-3,6,2,8,8,6,4,-1,1,3,-8,10,-9,5,-8,8,1,-9,-1,-6,-8,6,-2,-10,-6,4,4,-9,4,-8,4,-4,-1,-5,9,-3,6,9,-6,-2,10,8,9,-6,1,5,-4,-8,1,7,-9,-9,10,2,4,10,-9,7,-6,-10,1,-2,-6,7,-8,-9,9,-1,-3,4,-6,-1,-3,-2,5,7,9,8,4,5,4,-8,-2,-1,-1,-4,1,3,-6,-4,8,7,-3,-5,2,10,3,-8,-6,-2,6,-5,1,-1,-2,8,-8,-7,9,9,-1,-7,6,1,-4,10,-7,7,10,5,-4,-2,-9,5,-1,9,-3,10,4,3,4,-8,-6,-1,4,8,10,-8,9,8,8,-5,4,10,7,-5,-7,-2,-9,-9,8,1,-9,10,2,7,-5,-1,-8,-6,6,-3,-8,6,-9,-2,-4,6,2,1,-4,-4,-3,-8,9,3,7,10,3,5,-3,-9,-8,2,3,-3,-4,-5,-3,-7,7,10,7,1,6,-2,-3,-7,7,10,-5,-8,2,-7,4,-7,-3,9,5,-10,6,-1,4,-1,-1,3,-5,-6,-4,-10,-6,-1,4,-9,-10,1,10,4,-1,-4,-5,10,-8,7,-9,10,3,-6,-3,-5,3,-8,7,-8,-8,-1,-1,-3,7,-3,-6,-4,6,6,-5,2,-5,3,-2,-10,-7,-5,10,-1,7,-3,-7,-4,7,4,-8,-1,7,-5,-7,1,-6,4,4,2,9,8,6,-3,-9,4,3,2,-1,3,2,4,10,-3,-5,-10,4,-2,-10,-3,2,-8,-5,9,7,-4,5,6,-7,-4,6,9,-1,-10,6,10,1,6,-6,1,-6,2,-4,1,-7,-6,-8,-5,-7,-10,8,-2,-7,6,3,7,-4,-3,9,-2,8,1,4,-6,1,-6,5,-10,8,8,-3,3,5,-6,1,-1,7,-6,10,-3,-8,-9,-7,-7,-5,6,-9,-5,-6,-9,10,-5,-3,-7,-3,-5,-9,5,-3,3,-7,-8,-10,3,6,3,3,3,9,1,2,2,-10,9,7,-3,-3,-3,4,10,-5,3,3,5,8,3,-2,1,-9,-5,-6,-1,7,-5,9,8,8,-3,9,-2,-4,7,7,-5,-2,-3,7,9,-9,7,-8,3,8,1,-3,-4,-8,-10,1,-1,6,-1,-1,10,-3,-9,2,10,-9,-7,4,9,4,-8,7,-8,-5,-7,-9,6,2,4,-9,-3,-7,-1,4,2,-1,5,-10,-10,-3,-1,4,6,-5,1,7,2,-6,5,-3,2,-5,-2,3,2,-1,-10,-2,-2,-9,1,-10,-1,4,-10,3,2,10,-5,-4,-1,-9,1,-9,8,-7,-5,-2,5,2,-4,7,3,8,2,-4,-8,-2,-6,-1,9,3,-6,10,-10,9,7,10,5,7,-3,-8,6,1,3,6,1,-7,2,-2,-10,-8,7,7,9,1,7,-4,-1,4,-6,-7,-10,8,4,6,-1,10,-4,1,-1,5,2,-2,4,-1,8,1,-4,10,9,9,2,-9,8,-10,-2,8,4,-1,8,1,9,4,1,1,-3,9,2,2,9,1,-6,-7,9,-1,1,-4,3,6,-3,-3,9,-2,9,-3,5,-10,-2,-3,9,9,5,-10,1,-2,5,3,-7,-7,8,-7,-3,-3,-7,8,-10,4,10,6,2,-8,-3,-10,-5,-1,6,-7,8,-6,6,-1,-2,-2,10,6,5,-8,-4,-3,5,5,3,-10,9,5,1,2,2,-8,1,6,-7,-6,-3,1,2,-9,7,5,-7,-1,-6,-6,8,-1,-5,7,-3,2,-2,6,-10,-9,6,2,4,-6,8,-7,3,5,6,1,-7,-7,-7,-2,-10,5,-7,-9,-10,-1,4,-5,7,6,-4,-5,1,9,-7,-6,-4,-10,6,3,-4,-6,-2,7,3,-3,2,7,9,1,6,10,-8,4,10,4,2,4,3,3,7,-2,-1,-2,4,4,-5,-2,5,-9,-5,-10,-4,-1,8,-2,10,-5,4,1,5,8,2,-2,-7,-5,-5,9,1,-6,-4,5,-2,-4,10,-4,3,-2,3,-5,7,5,4,1,4,6,4,1,-2,2,-10,-4,8,9,1,4,-3,10,-2,3,-6,3,10,8,7,-3,-8,-2,-6,10,7,5,-4,5,4,10,-9,-2,7,1,1,2,3,-6,7,6,3,-1,-6,10,8,-10,5,6,-1,5,-2,-1,-3,6,4,-3,5,3,2,-9,-7,7,-2,-3,1,5,7,10,3,-7,2,-6,-3,8,4,8,-8,-3,-8,-3,6,-2,-2,-10,-2,3,-8,1,-10,9,-6,-7,-1,-7,1,-8,8,10,4,-8,-9,-10,-2,8,-10,7,-5,-4,-9,5,-1,-6,3,-10,6,-3,8,1,6,3,-6,6,7,8,-1,5,-8,-2,7,-9,-1,-7,8,1,7,2,6,-7,-7,10,-9,-1,-8,-9,-8,-7,3,-10,-9,-6,6,-2,-5,-7,3,2,4,1,10,-6,-10,-9,-6,5,3,4,1,-4,-4,-1,-10,-8,-10,-8,-1,-1,9,6,-3,3,-2,7,-4,2,-4,4,7,8,-3,10,-1,6,4,-7,3,-5,8,10,5,-1,-4,2,-9,1,-9,7,-3,-1,-7,4,-8,-6,-10,-10,10,-3,6,-8,-6,-8,-9,6,-10,-6,3,6,8,-8,2,-5,-1,9,-4,2,-5,6,7,-5,-6,1,-3,-1,-3,-1,-8,9,5,-7,-2,-8,3,-2,-3,-5,-8,-10,-7,3,-1,7,3,1,2,6,8,3,-7,2,-2,10,-3,-2,-1,-10,-1,2,-1,-1,-10,10,-10,-1,-10,8,-10,-3,-9,3,1,-2,10,-8,8,7,6,-10,-10,3,4,9,10,-8,8,10,-7,-2,8,-10,-9,6,2,-10,-7,-2,4,6,5,2,-5,1,-7,-9,-2,3,5,7,-5,2,9,4,5,-7,6,-2,-4,-3,7,-7,-10,-10,-2,-4,3,-9,-10,-6,-5,-5,-4,9,9,10,5,-5,-10,2,4,-8,-2,1,-10,-8,2,5,10,6,8,-7,3,-8,1,-4,-5,-5,-7,-10,-5,-3,2,5,-4,3,-6,6,4,-4,-3,-1,-9,5,3,7,4,7,10,5,-4,9,-1,-1,9,2,-4,-10,9,10,-1,-10,-9,-8,-2,6,-3,7,-9,9,-6,10,3,-4,5,4,3,8,2,4,1,9,-2,-10,-7,-9,-9,2,8,4,-1,7,2,-7,-5,8,8,2,4,-3,10,-3,-10,2,-2,-9,-7,-5,6,-5,3,-9,-3,-3,2,9,7,-2,8,4,10,-10,-2,8,-9,2,-8,-2,-1,-9,10,-6,9,-3,2,4,-1,-1,-1,4,1,1,5,10,10,-1,-7,-7,-5,-3,8,-10,-4,-3,-9,-5,2,-10,1,5,9,-2,-4,-5,1,-5,7,-9,6,6,-8,-6,8,7,7,-3,-9,5,7,-2,7,-7,-5,-3,-10,-4,1,1,7,-3,2,-1,2,-4,-5,7,-4,-6,3,-9,10,3,5,-5,2,5,3,-4,-3,3,-5,-9,5,9,5,-2,3,-8,-7,-1,8,-4,-3,5,-9,1,9,6,-5,3,-4,5,-10,6,-6,8,-2,-7,3,10,-2,-7,-10,8,-7,-5,8,8,5,-7,10,4,-10,-6,5,-4,-8,-2,3,6,-1,-10,-3,6,2,-6,1,-4,-3,5,-10,-8,1,7,-8,-3,-3,7,-1,1,-8,-6,9,3,4,-3,-6,-1,1,-10,-10,-7,6,-9,10,-10,9,9,-10,3,10,-10,-6,-5,10,5,6,5,7,9,-5,8,-7,-3,9,2,-1,8,-5,4,6,-5,3,-6,-5,-10,4,-4,4,1,-5,-5,-7,-4,5,6,-1,-4,3,7,-5,-8,-6,1,2,-3,6,1,-10,4,7,7,-2,-2,-2,-5,-7,-7,5,-3,1,2,-6,9,-2,-3,4,8,-2,-3,1,-3,-8,3,10,10,4,7,7,-9,-8,9,-4,-7,7,-3,7,9,8,-9,-10,8,-3,7,10,8,-8,-9,3,-9,6,-1,7,8,-1,-4,8,-6,-6,8,9,-5,6,-9,1,-9,1,-2,9,-6,9,-3,1,-7,-4,-6,-2,2,-6,-6,1,6,5,-2,9,7,7,6,-1,8,7,-10,2,8,-5,5,-10,-9,2,-1,1,-1,-10,-8,-8,-6,-8,-6,8,-10,-8,10,9,-5,3,2,-6,2,-7,-6,-7,-4,9,-9,1,2,6,7,3,6,10,10,8,1,-4,-4,7,8,-7,-5,-6,-10,-10,10,1,-9,-4,6,-3,-1,3,-8,3,-8,-4,-9,-9,5,-5,3,10,6,1,8,-8,10,4,4,5,8,-7,10,-7,7,1,-8,2,-7,-6,8,3,7,-10,-7,-5,6,3,9,-2,-1,-6,4,-5,-2,3,6,2,5,4,-6,-6,-10,10,-8,6,3,-10,-10,7,5,4,8,-5,-7,-5,-8,7,4,9,-10,-3,5,-10,-8,8,7,-5,9,7,8,3,7,-8,-7,-2,10,-2,9,-9,-10,-10,-1,1,-4,-6,-2,-10,10,7,5,-6,5,9,9,2,-6,-6,9,5,-8,8,1,-9,8,-8,-7,7,2,7,3,-1,-2,-6,-4,4,3,2,-2,2,-8,10,-5,-9,-2,-8,-8,3,-8,2,-9,6,8,3,10,9,-8,-5,-7,-1,3,-3,-10,10,7,-10,8,-8,5,-8,1,-4,6,3,6,-2,5,9,-4,-3,-2,-7,10,-9,-9,1,4,-8,-5,-4,4,9,1,-5,8,6,-1,-2,-8,-8,-10,6,4,-6,2,-1,8,-6,-9,-6,6,-9,-4,-2,6,1,10,-9,9,5,-7,-8,8,4,4,6,-9,-9,-8,9,-2,9,6,-8,5,-8,2,5,-9,-7,8,-5,8,2,-6,9,1,-1,6,-2,3,-3,-6,-6,9,10,-9,-6,10,3,9,3,10,7,-3,6,10,2,-2,-3,-4,-8,-9,-9,2,-2,-4,1,10,1,-10,3,8,8,-4,1,-5,10,-3,10,1,-6,-10,10,-8,5,-7,8,4,5,6,-5,-3,4,3,1,7,-8,8,-4,6,4,8,9,7,-9,8,-3,-10,-8,8,-7,-1,-9,5,-5,7,-6,-3,-8,-9,-3,-2,9,-1,6,-6,-6,10,-6,-3,7,4,4,8,-8,-8,3,7,-1,-9,-10,2,4,3,8,-2,-5,-10,-6,10,7,-4,7,4,-10,7,-10,7,-2,5,-6,6,-7,-8,-5,4,-6,4,-2,3,3,-3,2,8,-10,-3,4,-8,8,-2,6,-6,-8,8,-9,1,5,-5,-6,1,10,4,5,-4,8,7,4,8,4,-2,-9,6,-9,-10,-6,2,-5,9,-6,3,7,-10,3,-4,4,-1,9,6,8,2,5,9,10,-9,9,2,2,-10,8,2,-8,-4,10,-4,5,4,1,1,-1,8,4,9,-2,1,-3,-3,-7,9,-8,-6,10,-5,3,-2,10,-6,10,2,-4,-3,9,-7,2,4,8,2,-1,-9,-7,-1,-1,-3,2,-2,-8,5,-10,4,8,-3,-1,6,-4,-8,-8,-9,-6,9,-6,6,7,-3,-4,2,-6,-2,-9,-9,-5,-5,-6,1,5,-1,10,-8,9,-5,-2,-6,-9,-7,9,3,-3,-7,3,10,-6,10,6,-5,3,9,5,4,-4,-4,7,6,-6,-6,3,-6,6,-6,-5,-9,-1,4,6,1,6,-4,5,-2,5,9,-3,6,2,-4,-3,7,-3,-1,6,-8,9,7,2,-4,-7,-4,1,-2,5,2,-10,1,10,10,-4,-10,10,7,-5,10,8,-4,5,-2,5,8,4,9,-3,-8,7,2,-5,1,3,-4,5,-10,8,-3,-7,-6,-4,5,-4,-6,2,2,8,7,-5,2,3,-2,-3,1,8,3,4,9,10,3,-5,9,-8,-5,-1,3,-9,4,10,4,-5,-9,-4,1,6,-5,-6,-6,-5,7,10,-8,5,-2,7,4,-2,5,5,-1,-7,-4,3,1,-3,-3,-8,-5,-3,7,-5,-6,-6,-3,4,-2,2,-7,-5,2,7,-4,-6,-6,-6,-1,-6,7,7,-2,6,3,9,-1,-10,-6,-8,-2,7,-5,2,1,-2,-1,8,9,9,-10,-6,5,-5,3,-1,-2,-4,1,-3,-6,-1,-6,-2,3,-1,-2,-5,2,-9,-7,-1,-7,6,-3,-10,-7,-9,10,-10,-5,-7,7,-5,5,-6,-2,-3,-4,-9,-1,-9,10,3,-9,4,-3,2,-4,-9,-9,-3,-3,-2,-7,-3,7,-7,10,-6,3,7,-2,8,-4,-7,3,5,-8,3,5,-6,-2,9,2,-2,-9,5,-8,9,1,4,-8,1,6,-3,-4,3,-3,5,-2,-2,-8,2,9,7,-7,-5,-9,-3,2,6,-7,9,3,-5,3,-4,6,6,-7,-7,-3,9,9,-9,-10,-5,3,-8,8,-1,-3,-1,-3,6,9,4,6,-3,7,-5,6,3,4,8,-7,4,-4,-10,-3,6,-10,1,4,-2,-8,6,-9,-5,-2,-6,10,8,-4,-10,5,-6,-6,4,2,1,-4,-4,-7,5,-2,10,-10,7,-7,2,4,-8,6,-10,-9,-10,9,-6,-5,-8,4,10,-6,-2,5,-6,4,1,7,2,-2,9,-6,-8,9,-9,-3,9,-5,4,-6,1,6,2,3,9,6,-7,-6,5,-2,-8,-1,-8,-1,6,-3,-7,-9,2,1,-7,3,1,-10,5,-9,9,-4,-8,-9,10,3,1,-6,-2,-6,6,-3,-9,3,7,8,4,4,5,-8,5,4,-3,-9,-9,-4,-2,-2,-1,4,-9,-5,4,-6,-3,8,6,-4,-2,6,7,6,8,-2,-5,9,1,-8,5,6,8,4,5,5,-10,-9,-10,6,-7,8,-5,7,-5,10,8,-6,9,-2,-7,-2,-5,-1,7,4,-6,-7,1,8,8,-4,6,-3,-9,1,-2,-2,-5,-4,10,8,10,8,1,9,-4,6,-2,-6,3,-8,10,4,3,-10,5,9,-5,-9,5,-6,1,-10,2,-6,3,2,4,-1,-1,7,10,3,7,10,10,-10,9,-5,-5,-5,-5,-6,-2,-5,9,-1,10,-2,6,8,1,8,-9,8,6,-4,4,-1,8,-9,7,-4,2,5,-2,-5,-2,-1,-7,-5,-6,-5,1,-7,1,-4,6,7,-7,-5,9,2,-4,-2,-5,4,-8,-4,-5,7,-6,6,10,9,10,-6,5,-10,-4,8,1,-3,-10,-9,-7,-3,-9,3,4,7,-8,-3,-3,-2,5,-6,-3,-7,-3,10,-5,3,1,3,9,-9,3,10,5,2,-1,8,5,-6,6,-10,-8,4,2,5,5,8,8,-3,9,4,-2,-5,10,9,7,6,4,-5,7,-8,5,-10,6,-7,1,-7,6,1,-3,-3,-2,6,-8,2,10,-8,8,8,-5,10,-8,8,1,1,2,4,2,-9,8,8,3,-3,-5,-6,-9,6,-7,3,-4,2,10,-7,8,5,-7,-4,-8,-3,9,3,8,-7,-4,3,-5,-3,2,9,5,-6,4,7,10,-7,9,-6,1,-2,-4,-10,-1,-5,-2,3,-6,-4,-2,4,-8,10,3,4,1,-7,-10,-3,-2,4,-5,-3,-9,-3,7,2,10,-5,-9,-5,7,-5,-8,10,9,6,-2,-4,8,-3,-7,-4,-8,-8,-10,-9,-4,5,-5,4,10,7,-10,4,-10,-5,-3,-4,6,10,-6,4,-3,1,-6,1,6,-8,3,-4,-1,2,6,9,-9,-9,-9,-4,-3,-2,2,5,-3,4,-6,-9,-5,-3,6,-4,-10,-9,-7,-3,7,-1,7,9,-8,-6,-1,-1,5,-9,5,-5,8,6,-6,-10,-2,-4,-5,-1,-5,-7,-1,5,2,6,-9,4,2,5,-7,-2,5,8,-8,5,5,10,-8,-3,-10,10,7,-7,2,-8,8,-7,-6,5,5,9,-1,7,5,2,6,-3,5,-3,-3,-7,-3,-5,1,-4,1,-6,2,2,3,3,7,2,9,9,6,-4,-2,7,3,10,5,-6,9,-6,-3,2,6,-2,-9,8,8,-6,5,2,5,1,7,-6,-7,-1,-1,2,6,6,-8,-5,-8,-7,-6,-10,2,-2,-1,7,1,10,-2,-1,10,-6,-2,3,3,3,-8,10,-4,-10,1,3,-7,5,-7,8,6,4,-8,-7,8,8,-3,-7,-1,4,-4,5,9,-1,-6,4,6,9,-8,2,-6,-3,1,8,8,-7,8,-6,-9,5,-7,-7,-8,6,3,-3,10,-10,7,4,-1,-10,2,5,-4,-7,9,5,-10,-5,-8,-2,6,9,1,1,-6,-10,-6,10,-5,-2,-2,-4,-7,-5,-9,3,-8,-9,10,10,10,4,5,9,-4,-6,9,9,1,2,1,-7,10,10,7,-5,8,-6,-7,2,-5,8,-8,-9,2,-1,7,-4,6,-8,-3,-2,6,3,3,5,-2,2,-1,-1,2,-6,9,-7,-5,8,10,9,7,7,5,-8,6,-9,10,-8,1,3,-5,5,-5,-7,6,-1,8,-5,-2,4,-4,3,-2,-8,6,-4,-4,-2,-3,-4,-9,-4,-4,1,-1,-4,-9,-10,-9,-5,2,7,-8,4,1,4,6,-6,6,-6,4,3,6,-6,4,1,1,-1,-8,4,-7,-7,6,-1,1,-9,-7,10,-6,2,8,-5,3,1,2,-1,6,10,-3,4,8,3,-6,3,-7,-3,8,5,-3,-3,4,2,5,-1,2,-6,-9,-10,-10,-8,-5,4,-8,-5,5,-7,-3,8,2,-8,-3,7,-3,-8,9,10,6,7,2,6,-1,8,-4,4,6,-10,-8,10,3,4,3,-6,-7,4,9,9,-4,4,1,-4,1,5,-1,3,-4,-8,1,9,-10,-9,4,-7,-3,8,2,-3,4,-4,-5,-10,4,-10,-5,2,2,2,-7,6,-3,-6,-6,10,6,-6,-1,-2,8,7,-10,7,-10,8,2,-9,-8,-10,3,4,-1,2,1,-6,-7,10,-6,9,-10,5,-1,-4,1,-3,3,-4,10,-8,-2,-7,1,-6,8,3,4,-7,2,4,-7,-10,4,7,-1,-4,1,-4,1,-7,7,7,8,4,9,-5,-5,-7,8,3,-8,4,8,-2,-8,-10,-9,-6,-4,10,10,-10,-10,-6,-10,10,5,9,-2,4,2,-6,-4,-9,-7,-2,4,-4,6,5,-8,-7,-2,8,-9,-5,10,-1,6,-3,-9,-1,-4,9,4,9,10,-7,-2,6,9,10,5,-2,-1,5,9,-5,3,-2,-8,1,6,-10,-2,10,10,-1,-1,-7,7,4,-9,8,3,-9,2,8,-7,-6,9,-2,-6,-5,5,1,5,7,-4,-6,-8,5,4,-8,4,-9,8,1,4,10,7,1,-7,-7,-5,8,-7,-3,-8,1,-3,-6,-4,6,2,-5,-7,4,7,5,-4,5,-9,2,9,1,4,6,6,-5,-6,-1,9,7,7,-7,-8,-2,-3,4,8,6,5,-3,4,1,-10,-2,-8,-4,2,5,6,-7,-4,10,8,-7,10,6,-5,3,-9,-4,-6,1,-10,10,-6,4,7,3,4,10,7,7,3,1,4,9,4,10,6,1,-6,-3,10,2,-5,7,8,-8,-3,3,4,9,-1,3,10,1,-10,-1,-10,4,5,9,-3,-6,-6,6,-10,8,-6,9,9,-2,-4,-9,7,-2,-5,8,8,6,3,-3,-9,-4,-2,-10,5,-9,-6,5,-4,-6,8,6,-9,9,6,-7,-1,-9,4,-5,3,9,-4,1,-9,-4,-4,-2,-5,-7,1,8,-4,8,-8,8,8,-9,10,-2,-8,6,9,4,-9,6,4,-5,-1,-6,-7,-8,-2,1,8,2,10,-7,8,-4,2,-10,-4,-5,-9,3,7,-4,10,-2,-9,-2,4,9,-3,-2,4,1,6,-4,9,2,-9,-7,-2,-7,5,1,1,3,6,8,7,10,7,2,-1,6,-3,-1,3,-7,9,10,-9,-3,10,4,1,3,-8,-8,9,1,6,-6,-9,-7,-10,-8,2,3,1,1,3,-1,-9,2,-10,2,4,-5,1,-1,3,-10,-9,8,4,1,3,8,1,-4,2,9,1,9,7,5,-7,4,-9,5,2,-1,-10,-1,-9,-3,8,-7,7,-5,3,-6,-4,-8,3,-8,-1,-3,8,-5,-8,1,2,7,3,-6,9,-1,-2,-7,2,3,-4,8,8,-2,4,2,-9,-5,-2,-3,3,-5,-10,-2,-10,8,9,8,9,-6,1,-9,9,-7,9,2,-1,-6,1,-7,-3,7,-3,1,-6,7,7,10,-3,6,6,-1,7,1,-7,3,3,4,-6,8,-4,-9,-10,-6,7,-5,2,-1,-5,-10,-9,4,2,6,3,-2,-8,7,-2,-2,-4,2,-3,6,-5,2,-9,6,4,-3,-5,-5,6,2,4,-8,9,6,-5,9,1,4,8,5,-9,9,1,-6,6,6,-1,8,-4,-9,-9,7,-10,1,-8,-9,5,2,2,7,-7,5,5,6,-10,-8,-5,-8,-5,-2,7,3,-9,-2,-4,-8,9,-7,-1,-6,1,-9,-1,3,7,-1,9,8,9,-9,-8,2,-2,-4,5,3,5,2,8,2,-1,10,8,-7,10,10,5,-7,-2,-2,-2,2,-7,-5,-10,-10,9,10,-10,4,5,9,-5,-6,9,5,3,1,4,4,-3,4,4,1,2,-5,-9,-6,-5,3,-2,-7,8,6,-4,-5,-5,-10,4,5,9,3,-8,-4,3,7,8,4,-4,7,3,6,10,10,-9,9,9,-6,3,10,-9,-5,2,4,-2,-3,-4,4,5,7,-1,4,2,-6,9,-3,4,-5,9,-10,10,-7,-2,-8,7,5,-4,7,-8,-1,9,-5,-3,-9,8,5,-5,-2,-3,8,-6,7,1,-5,7,3,-1,-8,9,-1,9,4,-8,2,7,-1,-2,-2,-10,-1,-5,2,-3,2,-10,-8,9,-4,8,-6,10,5,-6,7,6,-3,-2,-6,-7,-6,1,7,-6,7,-1,-9,2,2,-3,-4,-7,-9,-3,-4,3,-9,-4,6,-1,3,10,2,-6,-10,5,7,10,-1,-10,3,-4,10,1,5,-1,-4,10,2,4,2,-5,-3,4,-8,-8,-10,7,10,5,10,6,6,-1,10,10,7,5,-8,4,5,-1,6,-2,6,2,5,9,3,-10,7,9,3,4,2,1,1,2,-10,4,4,-1,5,10,1,-5,8,-4,7,-4,7,-8,-7,-6,5,-4,-7,7,4,1,7,-6,7,6,8,-5,-5,-3,-1,3,8,-6,2,-8,3,4,5,-3,-9,-8,-10,2,-4,-2,-4,3,-10,-1,-4,-9,-8,7,4,-8,10,2,1,-9,-8,9,4,8,-3,-8,-7,6,-1,-1,-2,8,8,-3,-3,-1,-3,-7,-6,-3,-5,10,8,-1,8,2,4,-3,1,9,-10,6,-5,-10,-9,2,4,8,-5,-10,3,-4,-3,7,-2,-7,9,6,8,4,9,-1,-5,6,10,-4,8,-9,-2,-7,5,9,-9,7,-10,-5,5,5,-7,-2,5,-9,2,5,6,-10,-8,-4,-3,4,-2,-4,5,8,10,-8,-4,9,-6,-1,6,3,10,1,-10,9,-2,-10,-4,-8,6,9,-4,7,-3,-4,10,5,7,-7,10,9,-1,-10,5,1,-5,-5,-9,1,-1,-2,-2,-4,4,-8,-9,8,-5,-7,6,6,-8,-10,-1,10,-6,4,-3,1,-2,-2,5,3,10,-2,7,10,7,6,-3,-4,1,10,-8,9,-7,1,5,-4,3,5,-4,-7,7,2,10,-2,4,4,3,2,-6,-4,8,-8,-1,-2,10,-7,5,-10,5,-5,-3,1,-4,-6,9,-3,-5,7,-6,3,8,-4,1,-7,5,5,3,-4,2,-9,-9,7,5,-1,3,-8,8,-6,-5,5,-9,8,8,-10,1,1,-2,-5,2,-8,4,10,8,-10,2,-5,-8,4,-4,-8,4,6,-8,10,8,9,-6,3,4,10,-1,-7,-7,-6,-5,-9,-4,2,-7,3,4,5,-10,5,2,-10,-10,1,-7,-8,1,-1,2,6,10,5,1,4,-8,5,-4,-2,-3,-2,10,-7,9,8,3,-1,5,-5,-7,10,-7,7,2,-6,4,7,9,-7,-2,-10,-8,8,-8,-2,1,2,4,9,-1,-3,4,1,6,4,4,2,6,7,-2,-2,-8,-9,4,-10,-7,-1,5,-6,1,-8,3,-7,10,4,-3,-3,1,-5,3,1,8,-1,-4,-3,-7,10,-3,-9,-2,-2,-1,6,-8,8,-6,-1,9,-9,-1,7,-5,7,3,10,-1,10,7,6,7,-9,1,9,-4,-2,-3,2,-6,-8,5,6,-10,9,-2,-5,9,4,-5,-3,-1,3,-5,-4,4,-10,9,4,-2,-7,10,-7,-7,10,-4,-3,7,1,-1,-3,-6,-3,-10,-4,-1,-9,6,-9,-7,-7,1,5,7,2,-10,4,-9,-3,-5,-1,10,7,-6,-1,7,-3,7,8,6,4,6,-4,-5,4,-5,-6,5,-3,10,-5,1,7,7,-1,-7,9,-3,10,9,7,9,9,9,-6,-5,7,-8,-5,10,-6,-3,2,-7,3,4,-9,5,6,1,2,2,3,4,5,-4,-10,-7,2,-5,-9,6,2,6,-5,2,5,9,-4,-8,6,1,8,8,-1,4,2,7,-3,-3,-4,-8,-7,-8,1,-1,7,-2,-1,6,5,-3,2,-2,7,-3,-8,-9,-9,9,5,6,-3,9,-3,9,5,-7,-4,-9,-4,-1,3,-1,-8,-2,-10,7,7,1,-8,-7,4,7,-5,-8,-9,3,-2,-4,-5,-5,5,2,5,3,4,6,8,-6,10,-1,-7,-10,-1,1,-3,10,-8,1,8,7,-7,-9,-6,7,-3,4,-5,10,1,1,-8,1,5,-9,9,4,1,-3,2,-5,-10,-6,-5,10,-8,1,6,-9,-7,6,6,-4,-5,4,-6,-4,-1,-1,1,-4,4,4,-9,-3,-3,2,8,6,10,-3,-10,3,9,10,5,8,9,-1,7,5,-2,-9,1,-4,-7,9,3,-1,-4,-2,-4,10,4,-2,-7,1,3,10,7,-7,10,-4,-8,5,3,-2,-10,10,8,-5,10,4,9,-7,7,-1,-2,8,-7,1,-2,8,-7,-8,-2,-10,10,-6,-8,-5,9,-10,10,-8,-2,-8,-3,-8,5,-7,-8,7,-1,-9,6,-3,-2,5,-2,-9,-3,9,-3,6,3,-5,2,-3,5,-3,-7,-9,1,9,6,-6,-6,4,-1,9,6,9,6,-1,3,5,2,7,7,-5,-7,-1,-7,4,7,-4,-7,-1,4,-5,7,8,-3,5,4,-4,-2,-2,2,-6,1,-10,-4,1,-4,-8,-8,2,-3,5,4,6,4,4,-6,-3,-2,-5,-5,-6,-5,-9,1,8,6,-1,1,-8,-5,-1,5,-8,-8,-5,9,1,8,-9,-3,2,8,-2,1,6,-4,-7,-10,8,-7,-2,-4,10,-6,10,-4,9,-6,-3,-2,-4,-3,-7,-5,-4,6,9,-10,2,8,5,4,5,4,-8,-4,-3,3,-1,-5,-3,10,10,2,8,-4,3,-7,-8,4,-7,10,5,-2,-4,-3,7,-10,5,-1,-4,-6,-10,3,5,-8,8,-4,1,-1,-4,-9,-8,-10,-1,-6,3,-1,-6,-5,-4,5,8,6,7,4,2,4,4,-2,4],[-9,-9,-2,-5,-8,-9,-2,4,8,-5,-5,-6,4,-3,-5,4,4,4,-2,4,-9,-5,-3,7,4,-4,9,-8,-1,1,7,-2,3,-8,7,5,8,7,2,-3,-7,5,-8,-9,3,-7,-7,3,4,-5,7,5,1,-7,5,7,-6,8,-5,-2,-8,1,7,7,9,-10,-1,2,-8,-5,8,5,-6,7,-1,-2,-10,-6,10,8,-5,-6,5,10,-8,8,-1,-9,7,10,8,9,-4,-5,-8,4,3,-4,9,-4,3,4,-7,10,-10,4,-2,-6,-7,3,-3,-3,-8,-5,-2,-5,-10,-8,-1,-5,-1,-10,1,1,6,7,2,4,-6,-10,-9,-5,3,8,-4,-6,-1,9,-2,-1,-6,-8,6,-2,-2,-3,7,-9,-1,-6,-9,9,-1,-3,-1,-1,-1,-9,10,1,4,-2,2,-1,10,8,-10,-1,-7,3,-9,7,5,6,9,-7,3,-4,-3,-8,10,6,2,10,2,-9,2,-10,4,-2,7,-6,1,5,-4,-10,-8,-4,-4,2,-2,8,9,-10,-7,-7,-2,-5,4,-10,5,-1,-6,3,-1,-9,-6,-8,-6,7,9,-10,-9,-7,-8,-9,8,-6,-7,6,4,3,-2,-6,-7,4,8,-8,-10,8,-3,1,-7,8,5,-1,1,10,3,4,10,-8,5,-3,-3,2,-10,-9,-9,-2,-5,3,7,1,-1,1,-4,-8,-5,3,6,5,-2,2,5,6,-6,-6,-4,4,2,7,-4,-5,7,-6,7,6,10,-9,-3,3,-5,6,-5,-5,8,3,6,-1,-7,-6,10,4,-2,-5,9,8,-8,-5,5,-10,-3,-4,-10,-4,2,1,-3,-4,-7,4,8,2,-6,-6,7,3,8,1,-2,7,4,-8,3,4,2,10,9,5,-8,-6,9,-5,7,-5,2,3,-9,4,6,6,7,-9,7,-2,6,-10,-7,2,-2,3,10,-9,-8,5,-3,1,6,-4,3,-7,-4,-4,1,-5,4,6,-3,-4,-8,-4,-9,-10,-4,-9,-10,7,-3,-7,6,9,9,5,10,4,8,10,-4,6,5,-6,-2,-3,4,1,-9,10,-6,1,-4,-8,2,4,8,-5,-5,-10,-3,-4,-2,-7,-5,-10,-1,1,-5,-2,6,-4,-3,-9,-1,5,-1,-1,4,-3,-4,-4,-5,4,3,-8,9,-3,-2,-3,1,-7,9,-5,-7,-3,-3,-7,1,8,-5,-3,8,-9,8,3,9,4,-9,10,9,-6,10,1,-5,7,5,8,-8,4,-8,7,-7,7,2,-2,1,-3,1,6,3,10,3,-1,-5,-7,4,-2,7,-8,7,7,-8,-2,-6,-9,-10,-7,6,-4,-7,-6,6,-3,-7,9,-1,-3,7,-9,2,2,-6,-6,10,-5,-2,-7,9,9,-3,2,-3,4,-8,4,1,-5,6,-3,-3,5,-1,2,-4,-8,7,10,4,-3,7,4,5,8,3,10,-10,-9,-7,1,-2,-8,-10,3,4,-6,-3,-2,-2,-2,2,8,6,4,-10,7,-5,-3,7,7,-1,-4,-5,-5,-7,-9,10,2,7,-1,1,7,7,1,5,5,2,10,-6,-2,3,-3,-1,1,10,-4,-2,-9,2,-2,9,-1,-5,-8,-8,-3,4,-6,-2,2,8,5,9,-8,-5,6,-8,-4,-9,-5,3,-2,5,-1,-2,8,-10,-10,6,-10,8,4,-2,-10,-3,2,2,-2,-9,-3,9,-10,4,-10,10,3,5,-4,10,-9,-9,-8,4,-8,-4,-5,4,-1,-7,-1,10,-5,-5,-1,-4,-5,-3,4,2,4,4,-8,7,7,2,-3,5,-7,-8,5,-1,5,-5,3,2,5,7,4,-7,-9,10,3,-1,-8,-9,3,7,-3,-8,2,-4,-5,2,-4,-10,-10,-5,8,1,5,2,1,-7,-2,3,-4,-2,-7,-6,-3,-5,9,-4,-6,-4,9,10,-5,-6,-1,-2,-5,1,7,4,6,-5,-9,-1,-5,7,-4,6,5,6,-9,8,3,8,9,-1,1,-9,4,7,-6,7,-3,-9,3,2,-6,-7,-2,-10,-7,5,7,-10,3,-4,2,-10,2,-3,7,-8,8,3,-2,-2,-3,7,-10,-5,-4,3,-10,-1,2,-9,9,-5,5,-8,10,6,-4,5,1,6,-9,-1,2,1,-4,-5,2,-2,8,3,-8,1,-3,-8,6,-10,-3,-2,-3,-8,-7,-9,-3,-5,-1,-6,9,-2,4,9,-2,-5,-9,9,-3,-8,8,-9,-10,-1,-7,9,6,10,-1,-2,-7,-7,3,8,-3,-6,6,1,2,-7,10,-4,-7,-6,3,-1,-2,-9,-6,-3,-5,-9,4,7,3,4,-1,-8,3,9,2,8,-10,-3,4,-7,-4,-10,-8,6,-2,-5,-9,1,8,9,10,8,-4,8,4,9,-2,6,-9,-1,3,1,-10,-5,2,10,3,4,8,7,7,-10,8,-1,8,-7,-10,4,-1,-10,-5,7,-8,-7,-4,8,4,-2,-6,9,-5,-7,-5,4,-2,-2,-5,-6,1,1,10,7,-9,-6,10,-9,4,-9,-8,6,5,8,-7,7,10,3,7,-3,9,-9,7,-3,3,7,-2,1,10,-9,6,7,4,-5,2,-7,-7,7,6,2,-1,-9,5,2,9,-4,-9,-10,-5,-4,-5,5,1,8,1,5,3,4,-5,-3,8,-1,10,-10,8,-1,6,7,-7,3,6,-9,3,5,10,2,7,4,7,-4,9,10,-1,-5,1,-6,7,6,-9,-9,10,8,7,9,-8,-8,8,2,-4,-8,6,-4,9,4,4,8,5,3,10,3,-5,-4,-9,-4,5,8,6,-4,-3,-5,-10,-10,1,-6,-7,8,9,9,-10,1,-5,-5,-2,-7,7,-3,-7,1,-8,10,5,-9,1,4,-1,7,5,-10,-2,3,1,4,1,-9,-2,6,8,-4,3,2,-5,3,-2,-9,2,-4,10,-2,-5,9,1,-5,-3,9,6,-2,-2,-1,10,1,-1,-6,2,1,-10,-5,8,-9,8,6,1,5,7,-2,-5,10,7,-9,3,-8,-2,3,2,2,-1,-6,-8,-10,6,-1,-4,-8,-6,-3,7,-3,4,-1,-7,-8,1,3,-4,4,4,10,-4,-10,-3,1,-4,-9,10,9,-2,8,-3,-3,-3,-7,-2,-4,5,-9,6,-10,-4,-3,2,-2,10,-8,-10,-10,-9,9,-3,-2,-6,1,-10,-6,-2,7,-2,-8,10,5,-10,4,-1,-3,-5,-5,5,-6,-6,9,3,2,6,10,-10,7,-10,-9,3,5,8,-10,-3,8,-9,9,-5,-7,-3,-9,2,2,7,4,3,8,1,-4,2,-6,-1,3,8,-8,-9,-5,-5,6,6,1,-1,-3,-7,-7,-1,2,-9,-9,-8,-7,4,-1,-7,-10,-7,6,-2,-10,-10,-1,-1,-4,-9,7,-7,-6,6,-9,-4,-8,2,9,-5,-6,-8,-7,-10,-1,-1,8,-5,-1,2,4,1,-7,7,10,6,8,-2,5,5,1,-8,-6,-3,-4,10,-3,1,5,-5,-2,2,-5,5,4,-7,6,6,-8,10,6,-9,1,8,-8,5,-5,1,9,1,-8,2,4,7,-7,-4,-6,-3,-3,-7,5,2,-8,2,-1,-3,-1,-2,-1,7,-5,-2,-3,2,-5,6,10,1,-3,7,4,-4,5,10,-4,-5,-9,3,-9,6,3,-3,10,-3,7,-8,10,-5,-7,-10,-1,3,9,2,9,1,9,-9,9,3,-1,-6,4,-5,-6,3,9,7,-10,-5,6,4,-3,-6,4,8,-2,-10,4,7,-10,7,-6,7,-5,6,-2,9,-1,8,6,-5,-10,7,10,-6,-6,-10,-9,-8,-3,10,-3,9,-3,3,2,-2,-3,-8,4,-3,-7,3,-2,-4,5,10,-10,6,-5,7,-7,2,7,-2,2,-3,8,6,-9,7,-4,-4,6,-10,-8,-10,5,4,-2,6,2,4,7,4,-2,-2,7,-1,-7,-6,9,2,8,7,-4,5,-4,10,8,-9,-4,-9,10,-6,2,-4,5,-4,-1,4,-7,3,-5,3,4,8,-5,-1,-6,2,6,-8,1,6,4,-7,-9,2,-3,1,-7,5,5,-8,2,8,5,1,-7,-8,-8,-2,7,-5,9,8,-5,1,-1,-1,-9,1,5,10,8,3,-4,3,10,-2,3,8,-2,-10,-8,-4,-9,10,4,6,-9,7,7,-7,-7,-8,6,8,5,-9,-8,7,-9,-3,-9,4,-9,3,1,3,-6,8,-6,-2,-4,-3,5,2,-9,6,4,-5,-2,-1,8,-1,-4,8,5,3,2,-2,6,-2,6,2,-9,5,5,4,-9,-10,4,-4,-10,6,3,-9,-9,5,-9,7,3,-9,9,4,8,10,-1,-9,-1,3,3,4,-2,-9,-5,-9,10,9,-1,7,6,-1,2,-8,-5,9,-10,9,-10,-3,5,-5,9,-4,6,10,-1,-9,-1,7,7,-3,9,-10,-10,-5,-6,2,4,-8,9,4,-10,-2,3,8,-5,8,-7,-4,5,4,10,9,-1,-8,-6,8,-7,-1,-10,-10,-2,-1,-1,5,-4,9,4,2,4,6,2,10,-6,10,9,-3,10,-1,-8,-7,7,10,4,7,-10,2,8,-1,-2,-10,-3,-4,-6,-4,-3,-9,-6,2,-1,-10,3,-2,1,-3,6,-5,-6,-10,6,-9,6,1,-6,-4,3,7,5,7,5,-10,-5,10,6,4,-5,-4,10,4,8,5,1,7,3,1,-6,-1,-8,2,4,-7,-8,1,-6,-6,-3,6,-2,10,-9,-5,4,5,8,7,3,10,-4,-9,-6,-5,-5,2,5,3,5,-8,4,2,-9,4,10,3,-7,-6,-9,-3,-5,-2,-9,4,-2,4,6,-10,2,8,1,7,8,-2,-6,1,-10,-4,9,4,2,9,-1,-6,-6,6,-8,5,8,-4,2,8,10,2,1,3,3,1,3,-8,4,6,9,-7,-9,-3,-8,-5,-4,10,-5,9,2,-4,9,-4,8,-2,-1,3,-4,3,1,10,8,-1,2,-1,-1,-9,-8,1,3,10,6,4,-2,-2,6,8,-2,7,10,8,4,10,-2,-6,6,-9,-1,-2,1,-6,8,10,-7,-3,8,8,3,-4,1,-4,-5,-1,7,1,-7,-4,5,6,3,-8,-5,3,-4,-4,6,-4,-10,-9,-8,4,9,2,-2,-3,8,-7,8,10,6,9,-2,5,5,1,-4,9,-3,-7,-9,-1,2,9,-10,1,3,-10,-10,8,-8,-9,4,-8,-8,1,3,-4,1,-6,2,-7,-7,9,1,-7,8,1,-3,-8,-2,-10,-10,4,10,4,-7,-7,9,6,-7,9,8,-7,9,-5,4,-9,-2,10,1,3,5,6,8,-4,-4,10,2,-4,5,-3,-7,-5,-5,2,-9,6,7,-1,-6,9,7,2,9,2,7,2,10,-2,4,-3,-9,10,2,2,-6,8,2,-5,-7,-2,-6,8,-4,1,4,-1,-4,10,2,-4,5,-4,-1,8,7,6,-6,1,5,-8,-5,-6,1,5,-10,-2,8,-3,-4,-10,-3,-8,1,9,-1,-8,5,5,8,9,-8,4,-8,6,-10,-7,-5,3,2,3,-8,-10,-3,-1,5,-2,3,-1,-2,3,5,4,2,-5,9,8,1,4,-2,-8,5,2,-3,-8,-9,-9,-10,-4,10,9,-1,1,-4,5,-10,-5,-2,-2,9,2,-1,-2,-3,7,8,-5,2,1,10,4,-9,-4,9,8,6,-7,10,-9,-8,8,-2,-4,-10,-2,1,10,-8,-2,2,6,9,-4,5,-4,2,10,5,-8,-9,5,10,-3,-2,5,7,2,7,7,-1,-4,10,-5,-7,10,-7,9,2,6,-9,8,4,-1,5,-10,8,-7,7,-7,-9,10,4,1,-1,10,10,5,-7,5,-6,-8,1,7,9,2,-1,-2,-10,-10,2,1,9,7,2,-8,1,5,1,-9,3,8,4,8,-5,-6,-8,10,-1,-3,-1,1,7,3,5,-10,-3,-4,-2,-2,-1,-5,-3,6,2,-9,10,-2,-6,-9,-6,1,9,10,-10,-8,9,1,8,8,-9,-2,6,8,-10,-5,5,-8,3,-6,10,-5,-7,3,-6,-7,9,-3,-3,9,5,-10,1,-5,-7,7,-6,6,-1,-1,1,3,7,-7,7,4,9,2,-3,4,9,7,8,-9,2,7,5,-5,3,3,-7,4,4,-8,5,8,5,-7,9,-1,5,-6,7,-5,3,-2,8,8,2,-8,8,-10,1,6,-5,-3,-5,3,2,2,-7,-6,10,6,2,8,-9,-2,6,-2,-7,1,6,3,1,5,-2,4,7,-4,3,-8,10,3,-10,-7,2,10,-2,-7,-10,3,-5,6,7,10,3,2,-10,1,2,8,6,3,10,-10,-4,4,2,-3,9,-10,-3,-8,-1,-4,5,-8,-1,8,5,-4,5,-10,6,-7,-7,9,-1,-3,-4,-7,9,1,-8,-1,-10,-4,3,-1,7,5,-5,4,-9,-8,1,3,1,-2,-2,-4,8,-7,-1,-9,6,-2,8,7,-10,10,2,-3,-7,6,8,4,-7,6,-9,4,-10,-6,-2,-6,2,6,-9,-1,-4,8,4,-9,-4,8,-1,-9,-9,-1,-2,3,-3,9,10,8,6,7,9,10,-10,-7,1,5,-4,2,1,1,-6,6,2,-9,4,-8,-1,-8,-9,5,-2,-1,-7,4,8,-4,6,2,7,-4,-9,-6,3,5,-9,-1,1,9,4,-5,-9,-9,-10,10,-4,6,9,4,-6,-5,9,7,-7,-7,-2,-3,3,5,-3,-9,-1,10,7,-3,5,9,3,4,-4,1,5,-6,-8,-10,-6,-7,5,9,3,6,-2,-2,1,-5,8,3,-1,-2,10,9,-10,-2,-6,-7,-5,-9,-8,-3,8,5,5,-9,-7,-5,-2,2,3,-9,7,9,10,10,-10,8,1,4,-1,4,6,4,4,-2,-2,-7,6,2,8,6,6,-4,9,-5,-2,10,-8,8,2,10,-10,2,7,-3,-9,2,5,6,-5,6,-2,7,-3,-4,4,7,-3,9,-7,6,1,3,4,-10,10,6,2,-10,10,-10,-7,8,7,3,-2,-10,-5,-9,-10,-7,4,-10,9,-1,-5,-5,7,-6,3,-8,6,-7,9,-9,-4,-9,2,-5,1,-9,-7,1,-10,-8,-6,-7,2,-5,-8,10,-3,-10,-8,5,1,6,-10,3,5,2,-10,6,-1,-5,-7,2,-3,6,-7,3,-7,-7,-7,9,-4,5,-8,-5,4,-9,-6,5,-5,-3,2,-2,6,-7,4,6,7,-1,4,5,8,3,6,5,8,6,3,-2,9,-1,7,10,-1,-8,-1,-7,6,-2,7,-8,5,-9,-3,-7,-2,5,8,-1,10,-7,2,-9,5,3,-9,9,6,-2,10,-1,-2,10,-6,10,-10,-5,3,1,5,10,-8,10,10,10,3,-2,10,6,5,-9,5,9,10,-7,-7,-1,-9,-6,-2,9,-10,2,-7,3,4,-8,8,8,9,-4,-4,9,5,2,-4,7,-4,-3,7,4,9,-4,-9,-6,-10,5,3,-7,1,-8,-10,8,-3,-4,8,4,10,-6,-2,7,3,6,-6,-6,10,-2,6,4,-3,-10,6,10,-3,7,1,7,-6,9,6,8,9,6,-2,-5,-1,-7,2,-5,6,-10,3,-2,-10,2,-6,2,10,3,10,-8,6,8,-5,-10,-4,-9,-10,8,1,6,8,-5,7,2,-7,-10,6,-8,2,1,10,3,-10,-10,10,-10,-5,9,-2,-1,1,-9,-9,5,7,-5,7,-7,-10,-8,4,-1,3,-10,2,4,-3,10,2,-3,-3,-7,10,-7,-2,1,5,6,-3,-4,10,-10,-3,-6,8,-5,10,1,-8,10,-5,8,4,-7,10,4,9,2,-4,8,-8,3,7,-5,4,2,6,-7,-4,9,-8,-4,7,-1,-4,5,4,-9,-3,3,-2,7,7,-10,10,4,10,-5,4,10,-6,2,-6,-2,-9,-6,-2,-9,-9,-1,-8,-7,3,-7,-9,-6,5,-7,-3,10,6,3,9,8,-2,-6,-1,1,6,-10,-7,2,-6,-3,-9,-1,8,-2,7,-6,-6,9,7,3,8,-8,2,8,-10,9,5,2,-5,10,-4,-10,1,10,-9,-9,8,5,9,2,-6,7,-10,-5,-5,6,3,2,7,-2,-6,-7,-10,8,8,9,8,7,4,6,9,9,-10,-8,4,3,-2,-6,-3,-2,-2,-6,6,2,-7,1,10,10,2,5,9,-6,10,-3,-6,-7,7,-1,-7,3,9,10,6,9,9,4,6,8,3,1,8,10,-1,8,-3,-2,7,-4,-1,2,7,-7,-7,-8,-8,-10,9,4,10,-10,5,7,-3,6,2,-5,4,-3,-6,-9,-2,-3,-10,2,8,-3,3,4,9,-1,8,1,5,2,6,8,-2,-8,-7,-2,-4,8,5,3,-4,6,-8,5,-2,7,-10,-6,5,5,-6,-6,2,-8,-10,10,3,7,4,7,10,-5,-8,-3,7,-6,4,3,-10,4,10,-3,1,-6,-3,-2,6,5,8,-8,7,8,-8,9,2,7,7,-6,-1,3,7,8,3,-7,1,-8,1,-10,-6,8,-2,9,4,-6,-8,-8,-4,-8,10,-10,3,9,-3,-5,-8,5,8,9,-9,-7,-6,4,3,-9,-9,4,-6,-6,-10,7,3,-9,-8,-5,3,-8,8,9,3,-4,6,4,9,-2,-2,8,-3,-8,-5,-1,-4,-9,10,6,5,-8,6,-4,6,7,-5,7,1,-10,-10,-7,10,9,-4,-7,-2,10,9,-6,-10,-4,7,-2,9,-7,2,3,9,-4,-6,-2,6,-8,-7,-1,-7,-1,-6,-5,2,-4,-5,8,9,-7,-3,-3,2,-5,8,-6,-10,-1,8,3,-9,8,-2,-10,-10,-5,-7,-3,2,7,-3,6,10,10,-5,-9,10,10,4,2,-8,-7,7,-5,-8,-10,-5,-2,4,-2,7,-1,9,-8,3,4,-8,6,3,-6,-4,-9,1,-4,5,3,-9,8,8,-8,-5,2,-5,9,-10,6,1,4,9,6,6,-8,6,1,-10,-4,-3,-6,-5,-8,-2,-10,2,-5,-4,6,2,4,-10,1,4,-2,-10,-7,7,-3,-2,2,-6,6,9,9,6,9,-8,5,-6,3,7,-4,-7,-3,-9,-2,3,-7,10,6,-1,3,7,-3,6,10,6,-10,-10,-2,10,-4,-2,5,-8,9,6,-9,9,-8,10,8,4,10,3,-3,-6,5,-1,-9,3,-8,-7,4,3,-10,-1,-8,10,-1,10,5,-4,-3,1,3,7,3,-10,-1,-10,-5,-3,6,-3,-6,2,8,-2,-10,-2,-6,-4,-4,-9,-7,-7,-10,7,4,4,2,9,-3,-2,3,5,2,2,2,-2,10,3,-10,5,-8,-3,-8,-10,-5,-3,-6,-10,6,6,-3,10,10,3,-2,5,9,2,-2,8,5,-8,10,9,9,-7,-6,6,-8,7,9,-2,1,8,6,-3,-9,-2,-8,-8,-8,1,-10,1,8,-2,9,-5,-7,6,-9,6,9,-9,-9,-3,-2,3,3,-1,-4,-6,-6,3,-4,-9,-7,2,-3,2,8,8,-2,-1,7,-6,5,-3,-2,6,-7,-10,-2,-2,-3,-4,4,2,-7,10,9,4,-7,6,-7,-5,9,-1,-8,-3,-7,-6,3,6,-3,3,-2,5,-5,-9,3,-7,9,-3,-10,10,5,8,-3,7,3,-9,6,6,-7,6,-1,4,10,9,-6,-7,4,-1,2,-7,6,9,2,-5,-8,-8,-5,-9,2,7,6,10,-1,-6,-7,-5,-9,-6,8,9,-2,7,1,-4,-3,-2,-3,8,1,7,9,10,-4,10,-8,10,-7,-9,4,-3,2,-7,-6,-1,10,-5,-9,10,3,-7,-10,5,5,-10,-9,5,8,8,-6,-3,8,7,4,3,9,10,-7,1,-9,9,1,9,6,5,10,-8,5,6,-5,7,-6,-7,2,-7,6,8,1,-9,7,-9,-2,-3,-2,-6,-7,3,2,10,-8,2,2,1,7,10,-4,9,6,2,-3,7,3,-5,1,-6,2,-3,10,-10,2,9,1,-1,-1,6,-1,-4,-4,9,4,-6,-5,-3,-1,-10,-2,-10,-8,-9,1,-1,-10,-7,5,2,1,-8,-7,1,-3,-2,9,-2,-2,-6,-8,-7,3,3,-2,-9,-2,-1,-9,8,3,-1,-3,-9,-3,2,-3,8,-5,-4,-7,-9,-2,-8,3,5,8,-8,8,-8,4,2,8,-3,-2,-9,-2,8,1,6,-3,-9,6,4,7,-7,-3,-8,9,-6,-10,2,7,7,7,3,-4,-3,-2,-6,-8,-9,10,-3,-1,-3,-4,-5,4,-9,3,1,4,8,10,6,7,-10,-5,7,10,8,-5,-6,-5,10,-7,-5,-2,9,-9,9,-10,-2,-1,-2,-10,-8,-3,4,9,6,-4,9,6,-7,2,-10,6,-9,2,10,2,-7,-10,5,-6,5,3,-5,1,5,-9,-10,-8,1,-10,2,-1,-7,1,-10,2,-4,-1,-6,-10,-8,8,3,6,-6,7,8,-8,-8,-6,3,-6,-5,-7,-1,-3,-5,8,-7,-1,1,-2,7,4,6,-6,2,-9,10,9,2,-10,-5,2,-3,6,3,2,7,-5,-10,5,4,-10,-9,-6,4,-5,-6,-2,1,4,-7,6,-6,8,-6,7,-4,-4,7,3,8,2,-4,5,-2,3,-7,5,2,9,-4,-7,5,-1,-1,-6,2,-3,10,-4,-8,4,-6,9,10,-7,4,5,5,-2,2,-5,3,3,-7,8,5,-1,2,-10,-5,9,3,9,-1,4,8,-8,-9,-6,7,4,-7,5,-4,-4,-4,-2,-8,-4,-1,-10,10,-10,8,-9,-2,-9,9,-8,10,6,8,10,-9,3,-5,-9,-1,-7,-6,6,-9,-5,-10,3,-9,-4,7,1,10,-3,8,-1,-2,-10,5,4,-4,4,6,-3,-8,-3,3,-8,9,10,-5,8,1,8,5,-4,5,-2,7,7,2,-10,-4,-10,4,-2,-2,8,10,3,-8,-4,-5,3,2,9,9,-1,-2,10,2,6,-4,-9,-10,10,9,10,-2,10,-4,10,-10,10,1,-9,2,8,10,10,10,-8,4,5,-5,-2,3,6,-2,-9,-6,7,-4,4,10,3,-4,1,3,5,-2,-8,-8,2,9,-2,-10,3,-2,7,10,6,-1,3,-4,3,-5,10,-3,3,4,9,4,5,10,10,1,6,-4,7,7,-3,-9,8,-5,-8,-6,-2,-10,8,10,1,-5,-3,-6,-6,-8,-5,-2,-1,-4,8,7,-10,-9,-8,-8,8,6,2,-10,4,5,-5,4,6,6,-10,3,9,-10,-1,-5,-2,10,4,-2,10,-2,6,2,6,5,-8,-5,2,-5,4,4,3,-1,4,7,-5,-10,7,-3,7,-8,-10,-3,10,7,-9,3,-5,-9,10,-4,7,5,3,8,10,6,-10,-2,8,-8,10,-9,6,3,-3,2,-8,-3,-9,-2,6,-6,-8,1,-8,3,8,1,9,1,-1,-2,-2,-4,8,9,-4,4,-3,-8,-4,9,2,-8,-5,2,4,9,-3,-8,-6,8,-9,-2,9,-5,4,3,-5,-8,1,-8,-6,-10,9,3,-4,7,-5,-8,-10,5,7,1,-2,2,-9,-6,-9,-5,8,-4,-10,6,10,10,-8,-6,-7,-7,-4,-2,-3,-7,7,-9,-3,-7,-3,-8,8,-7,-7,1,9,-2,-1,7,3,6,-7,6,9,-3,-6,-7,1,3,8,9,-6,-10,5,10,-1,-9,3,-10,-9,-5,4,-1,8,10,-2,3,1,-4,1,8,2,2,-3,8,-7,-8,4,5,-7,-8,-5,-6,4,-7,-6,9,-2,-5,-5,-8,-5,3,-8,-3,-5,-2,4,1,8,3,2,-5,-4,1,3,-2,-6,10,-7,-6,6,5,8,7,3,-1,1,1,-6,7,-2,10,5,-1,-4,5,7,-9,-7,10,-6,6,4,-5,2,2,10,-3,1,-9,2,-7,5,5,-4,-3,5,10,-9,-2,8,4,-3,4,10,2,-9,-1,5,-8,1,1,-9,7,-9,-8,10,-4,-6,10,-4,-7,1,9,4,-7,7,10,9,3,-4,-5,-2,1,9,-5,4,-8,-10,1,2,-6,3,4,-3,2,-7,-4,-7,-6,-4,9,-3,-3,4,4,9,5,-7,-6,6,-8,4,-2,6,-7,-9,10,-5,-4,4,-5,9,7,-8,8,10,7,-7,6,6,-4,10,-6,7,-6,-9,4,-10,6,3,-10,-10,-8,5,-10,7,-4,10,-4,2,-7,-10,9,-3,7,-6,10,5,3,-2,-1,-9,-6,6,5,1,-9,5,2,-2,6,8,-4,-2,5,9,2,10,6,-9,6,-5,2,4,9,-1,-1,-9,-3,1,-6,3,-6,-8,-1,-3,7,-3,-9,-3,2,-3,4,-10,-6,5,1,10,1,2,-4,-10,-5,2,-1,-2,10,7,-9,2,-10,-7,-5,10,4,-1,-9,3,-5,9,1,-10,-9,6,-8,1,-5,10,-5,7,4,-2,-8,-10,4,-10,1,8,9,-7,-2,4,9,7,-4,-7,-4,-5,6,7,5,6,7,7,10,2,4,-9,-2,1,5,-6,9,-3,-7,6,8,-9,8,3,-1,9,-3,-10,-7,2,-1,2,2,-2,6,10,-1,-10,-4,-6,2,-2,-6,-1,-5,6,1,-3,-5,-1,-4,6,-1,-4,-3,-2,6,9,6,6,1,5,-3,-5,5,9,7,5,-6,-3,-9,-2,-6,-8,1,4,-7,-5,9,-9,4,-6,-5,-8,-9,-10,3,5,4,-4,7,-8,6,7,1,-2,5,-7,6,-3,-4,5,-6,-9,-4,-7,10,7,9,3,-3,-7,10,1,7,3,9,-1,10,7,-2,5,10,-7,-10,-8,-5,1,7,1,10,-7,6,5,-7,-10,-9,-2,8,9,-10,-9,4,-10,4,6,7,-2,-3,-9,-1,1,3,-2,-3,-9,10,9,1,-4,1,8,5,-3,9,9,10,-4,3,5,7,-10,3,-10,9,9,5,-7,9,7,3,-2,7,-7,-9,6,-8,2,8,-8,-7,-4,-6,1,3,7,-5,1,2,2,-10,-9,7,-10,5,-1,-6,-5,7,10,-7,8,-6,3,6,-3,-8,-5,-6,-1,2,5,6,-2,7,5,-9,-5,-3,-4,6,3,10,8,-2,6,10,4,1,-8,-8,-2,7,3,-8,9,6,9,-2,3,7,-10,1,2,1,-2,-5,7,2,4,-1,-3,4,7,8,-10,9,9,-7,6,2,-9,10,1,-10,-9,5,-9,3,-7,-8,-5,8,-9,-6,-4,-2,-5,1,-4,10,-1,5,-6,-10,9,-9,-4,-10,-3,-7,5,10,-2,6,1,9,-3,-5,-7,1,10,-2,-6,-9,-9,3,-6,3,-5,5,-7,9,-3,10,-7,5,8,4,-10,-2,-9,-2,-2,-6,6,-3,6,-4,4,8,-2,3,-10,7,-9,-8,7,-7,5,-4,-3,-5,-8,-9,-2,6,-9,5,5,9,2,-4,9,6,5,6,-8,6,-9,-8,1,4,-2,-9,-2,5,-8,-3,-2,-3,-10,2,10,-3,4,-8,5,3,3,-8,-2,9,2,9,10,1,-10,7,3,-9,-1,-2,-8,-8,6,-6,-9,-8,-8,6,-8,-7,10,-10,-5,-7,-7,5,-3,6,8,-10,8,9,5,-3,10,3,7,-2,4,1,8,7,-10,5,-9,-7,10,-5,1,10,-10,-3,8,-9,5,-4,-5,-8,-5,3,5,1,7,-2,3,-2,-7,-2,-2,-9,-1,4,5,-9,5,6,-3,7,4,8,3,2,7,-7,5,6,1,9,1,8,-1,6,-3,6,2,5,-4,-7,1,1,-2,-9,6,2,-8,-5,-7,5,-4,5,4,3,-7,10,6,1,8,-4,-7,-6,-9,4,-2,5,-1,-1,-10,-3,-7,-2,-4,-5,-2,9,-7,6,5,-3,-10,-10,9,-4,-8,-6,1,9,3,-8,-5,6,-3,10,-2,-5,-1,3,-8,1,-5,-10,8,-10,5,8,8,-4,6,-8,-6,1,8,9,3,10,10,-4,1,-9,-3,-8,9,-1,5,3,10,3,2,-4,4,2,-5,-10,2,7,-6,-6,9,2,-7,-7,1,-5,-2,7,-4,-1,7,7,3,-5,-9,4,8,-1,-10,-2,-10,3,7,-9,-1,9,-4,-5,2,-3,-1,-10,10,-4,2,3,-4,-6,-8,-3,7,-7,2,-5,-4,-7,7,3,-9,-10,-4,6,7,2,-9,6,-9,-7,7,-5,-2,5,8,-7,-7,-9,-7,-3,-7,4,2,-3,1,1,-2,8,-7,-5,10,-3,8,2,-6,-4,1,-10,5,3,-3,-5,-9,1,3,10,-8,4,4,3,-2,5,-4,4,10,5,-2,-8,-3,-6,5,-2,10,8,4,3,10,-7,5,-4,-1,-8,-9,-3,-3,9,-8,10,-10,9,2,8,-2,-6,8,-3,9,3,8,-2,-8,9,-3,1,9,-7,-4,5,-2,6,-1,1,2,9,2,1,2,4,-10,1,5,-2,-5,-4,10,-8,-8,-2,-5,-10,-2,-8,10,-2,-9,2,2,-2,1,-3,7,-1,-10,-5,5,5,6,-2,5,7,-8,5,-2,-5,4,-7,9,6,-2,6,8,-3,-5,1,10,2,-8,7,8,7,2,-3,-2,2,-1,9,2,-4,-10,6,4,9,-7,-3,10,6,-4,5,-9,-9,-7,-2,4,-5,2,4,9,7,10,10,-2,4,-5,-1,7,-5,-10,-3,-2,7,-10,-9,4,5,-7,-6,9,-4,-10,-9,5,-1,-10,9,5,-5,7,-5,1,7,-5,9,-4,10,-8,-10,2,7,-8,-1,2,-1,1,4,-8,-4,-5,-8,-5,-4,7,7,-7,-1,-3,-1,10,8,8,7,-2,-8,1,-7,-6,3,-4,5,7,10,8,-6,1,-4,-5,-4,2,-5,8,1,-4,-7,5,2,8,3,-3,-8,3,5,3,-7,3,-7,-8,7,5,10,8,3,6,-3,4,-3,-3,7,10,-10,9,-6,-10,-7,-8,4,-1,-1,-4,5,-6,-7,9,-7,-1,1,-6,5,1,10,2,-5,-4,1,-1,-6,-5,5,8,-4,-1,-8,-4,-5,-8,-4,1,-5,-8,-3,-3,5,1,-3,-4,-9,-1,-1,4,2,1,2,7,-6,-4,-3,7,4,-10,10,-3,6,-8,1,-3,3,10,7,-5,-4,4,-3,-7,-9,-3,10,10,9,5,1,4,-3,1,2,4,4,-5,-9,3,9,8,1,-5,5,2,-9,10,-1,-3,9,-10,7,8,-8,-5,9,8,1,-2,-5,-2,3,8,5,6,9,4,3,-2,-3,10,10,1,1,-8,2,-3,-2,-8,2,-8,1,-9,-4,-5,-7,10,-3,9,-6,4,-6,2,6,2,3,-9,2,9,8,-4,1,4,-4,-1,1,10,-2,3,2,6,-7,-4,-4,4,8,-8,-1,4,7,-8,3,-6,-10,-3,-6,2,5,-4,-8,10,6,7,-2,3,-10,-10,8,-6,-6,-3,-7,8,10,10,10,-5,9,6,-7,-3,-1,-8,10,7,4,-2,4,4,4,3,-3,4,4,-3,8,-6,10,8,-9,-10,5,-3,-4,5,10,-3,10,-4,7,3,-7,6,2,-9,-9,3,1,-4,-10,2,-9,-2,-2,3,-8,-5,-5,4,5,8,4,-7,-7,9,-2,-9,10,1,-10,1,1,4,-7,3,2,5,5,1,6,1,-5,-2,2,6,8,-3,-5,4,5,-5,3,5,3,1,-7,9,5,-8,-5,-10,-2,-5,-9,-1,8,-3,8,-10,5,-2,6,-6,-3,9,-9,-4,-1,1,7,6,8,8,-9,-6,-2,9,-10,-8,-1,4,5,4,8,-7,7,-2,-5,10,-1,-10,-5,-10,6,-1,-6,-9,-4,8,-8,8,-10,-10,-3,1,-7,6,2,8,-7,-6,-3,-3,-10,8,5,5,8,-2,-8,-4,6,8,7,5,-4,-6,-8,5,-9,-5,-10,-4,8,7,1,-10,3,-4,-3,-6,-1,-5,3,-4,2,1,-2,10,10,-3,-3,7,-10,-8,-1,-9,1,9,3,-8,-7,-10,-3,6,-10,-6,3,-10,-6,5,5,10,-9,9,6,-8,6,9,-8,5,-7,2,-4,-2,-3,10,2,-1,2,-4,7,9,-10,3,7,-10,8,-4,-6,-7,-7,4,-8,2,-7,6,8,7,8,-10,9,9,1,4,-4,-6,-7,-2,-7,4,-3,-10,-8,1,-9,2,10,-7,-7,-10,-1,3,9,4,-2,-4,1,-5,10,-6,6,9,9,9,-9,8,7,2,7,-4,4,-1,1,-3,-2,2,-5,8,-8,-10,7,-1,-9,2,6,-4,-3,7,-3,-5,-7,6,9,-8,10,6,-5,-4,7,-2,-2,-5,-3,9,3,4,-2,-4,2,-7,-9,2,9,8,-9,-1,7,6,-10,-8,2,5,-2,-4,-10,-9,-6,-4,-6,-1,5,8,9,3,-2,2,-5,-7,-5,-1,5,-5,2,6,-4,-7,-10,-10,-2,8,-6,-7,7,-7,-6,-7,-2,-2,6,4,-6,8,7,-4,-2,2,-5,10,2,2,8,9,-6,6,-8,9,-3,-9,-8,9,7,10,10,-2,7,-2,-5,-7,-1,-2,-5,-2,-9,-1,6,-7,-3,5,-6,8,2,10,-3,10,-2,-5,-3,-5,8,1,6,-6,-6,-2,7,6,4,-7,-5,-2,-7,-3,-4,5,2,7,-6,7,-4,-4,3,-8,-8,-3,-2,-9,2,9,10,-1,2,2,-10,1,10,-5,-7,-7,10,9,4,8,10,3,3,-4,-9,4,5,-5,1,7,7,-5,5,6,2,5,-5,-3,10,5,4,-1,5,6,-10,-5,9,1,-4,5,-4,9,9,-10,-9,-2,-6,-2,1,-10,10,-5,5,-5,4,4,-2,-9,-7,4,6,1,-9,5,-10,2,-10,1,4,4,-7,7,-3,2,5,-8,-10,-5,1,-10,2,-10,-8,8,8,1,10,7,-4,5,-3,-2,-9,3,-6,-10,-6,3,-3,5,2,-7,3,6,-2,-9,-4,-9,10,5,-8,4,-7,-5,7,2,-5,-10,4,6,-8,3,7,-7,8,3,-6,8,-4,-6,7,10,10,10,7,1,2,9,8,6,-5,1,-6,7,-4,-10,-4,2,-10,7,10,-5,2,4,10,-5,9,-8,-5,-6,9,-1,-8,-4,-7,8,-1,-10,8,4,-3,3,-4,-10,6,-9,4,8,3,10,5,7,-4,-10,2,2,-2,1,6,7,7,-6,8,-3,-8,-2,5,-10,10,-3,5,-2,-10,4,-6,7,1,-4,-1,-1,-2,-1,-6,-5,-4,-1,-4,7,5,10,-4,-5,-4,3,6,4,7,-4,-8,-9,9,-3,-2,7,-10,9,5,9,2,5,-6,-7,-6,-7,-4,-9,6,-4,-10,6,-7,8,-8,3,8,10,-9,-8,10,9,2,6,2,4,10,-4,4,9,8,2,2,-2,8,5,-3,-1,4,1,-7,10,7,-2,-7,-5,-5,-2,6,5,2,-4,-6,-10,-2,6,9,9,-9,9,4,-10,-8,5,4,9,-1,3,-8,8,5,1,2,-10,-1,-7,-10,5,1,3,1,3,5,-9,-10,-4,3,-7,-5,5,5,-4,-3,2,-8,-9,-6,-1,10,-3,7,5,3,4,-8,-8,3,5,-1,-9,-3,6,-3,-10,6,-5,-3,2,2,-5,-5,3,-3,3,7,-2,2,-2,6,-2,-7,5,7,5,-3,10,-3,5,3,-1,2,3,-1,1,-6,10,-9,-5,-10,6,1,1,-10,2,-8,4,-6,6,-9,-7,-1,10,9,4,6,-5,7,2,4,-9,-9,-4,7,4,-8,-2,-7,-7,-6,10,-5,8,2,-7,6,-1,-10,-1,5,-4,-8,2,-7,-4,1,4,8,8,-5,-8,-3,-5,-2,-2,4,1,-2,-9,-1,-3,-10,8,2,10,1,8,5,-8,2,5,6,9,-1,9,5,4,-1,-3,-8,-10,-1,4,-2,2,-4,1,6,-10,-10,9,-2,-3,7,8,1,6,-6,5,-7,-1,7,-1,-4,10,-1,-1,1,-10,2,-4,7,4,-4,-1,-7,10,-6,8,3,6,-6,10,3,-6,7,-7,-1,8,-9,6,3,3,-8,-1,-1,-6,-4,-6,6,1,1,-6,8,-10,4,4,-2,9,7,3,-9,-7,-5,1,3,5,-1,-8,6,7,-6,7,9,7,8,-6,-1,1,3,9,5,2,4,6,-2,10,-7,3,5,-3,-4,-1,1,-2,5,2,5,7,-6,1,-7,3,8,-9,9,-5,1,7,7,6,-1,3,2,7,-4,-5,9,-6,-7,-1,6,-1,-1,7,-10,-1,1,8,3,-1,-6,-9,-6,4,-9,2,-1,10,-3,-10,-2,-5,5,6,1,-7,6,1,-1,7,-2,-5,2,-2,2,10,-3,9,-10,-9,4,7,-4,-4,-7,-4,2,9,5,-10,5,3,5,-7,-6,-6,-2,2,3,-10,-9,-7,-4,-4,10,-7,6,-5,1,5,-10,-10,6,-8,-8,-9,-5,-5,-5,-7,4,9,4,-2,6,2,10,6,-2,5,5,6,-2,-8,-1,-9,-10,7,-10,9,-8,-2,1,-4,-4,-4,7,-8,10,-4,-2,-9,3,6,-7,-1,-6,-3,1,-1,-10,-4,2,6,10,6,-4,8,-1,3,9,-2,5,3,5,-2,6,4,10,3,-7,-3,2,-10,-6,-2,5,4,-1,9,-9,-5,-5,-7,6,-6,-9,-5,2,5,-8,-5,-2,6,-5,3,4,-3,4,5,-9,4,1,8,-5,-1,3,8,6,3,7,-5,4,1,7,-10,6,-4,-3,10,9,-1,-7,10,-2,-5,8,9,10,-10,7,-5,3,-2,6,-4,-3,-9,-5,4,-1,6,8,3,-7,-5,4,9,-1,-4,3,2,-5,8,10,-7,10,-2,1,8,-8,-4,5,10,6,-1,-3,5,-1,-10,-5,-2,10,-5,9,1,-8,-10,10,-9,5,5,2,-8,5,6,4,-6,1,-7,5,-8,5,-6,-7,1,-4,1,-6,-10,8,-10,-1,-1,8,-3,-6,-9,-8,-5,-1,-8,-3,-10,-2,2,6,6,-10,2,-5,-4,7,-3,8,1,-6,-4,-1,-10,5,-5,-5,10,6,-3,6,-3,1,-9,3,8,-10,10,7,4,-1,-4,-10,2,-4,-8,-2,-5,-4,-2,6,-8,-2,-6,10,2,-1,-10,9,-8,6,-5,-4,3,-7,-8,-5,-9,-7,-6,7,8,2,-8,7,6,-1,-4,-3,4,2,-5,8,-3,-9,10,7,-5,-6,-2,10,-8,10,7,-1,-7,2,-1,6,-7,-5,10,-5,-2,9,-3,3,9,5,9,6,8,-8,10,5,8,4,-3,-4,-1,-1,1,8,-9,7,-9,-6,2,-8,-7,-2,10,-4,9,9,10,-6,6,-4,-1,7,-5,-8,8,-3,-6,1,-3,10,4,3,9,-6,5,2,-10,-7,9,-3,-9,1,1,3,8,7,-3,5,-2,-7,-2,5,7,8,-5,-2,-7,-2,-6,6,10,-5,6,7,10,6,-4,-5,-3,6,3,-4,2,1,-3,-3,10,6,-9,-5,8,2,-2,-10,7,1,-3,-10,-1,4,-8,6,6,-8,-6,3,-2,-5,-1,7,10,-7,5,7,-10,1,-9,-10,1,-9,10,-1,8,-9,1,-6,6,-4,-3,-8,-4,-5,-5,10,-2,3,3,-6,-9,2,9,-1,-1,7,-5,-1,3,4,10,4,-4,-3,2,-10,2,-3,9,-7,8,-6,-10,-4,10,1,-3,-1,-5,-6,4,1,9,9,5,-8,-4,6,3,7,7,3,-6,-8,1,-9,9,2,-4,-6,1,-4,10,8,-1,7,4,9,-6,-2,-9,3,1,-8,8,-5,-7,3,8,-1,6,-6,-9,10,-10,-4,3,8,5,-10,9,-2,-4,-4,-6,-3,2,-1,-4,6,-3,-6,-10,-2,-10,9,-8,6,8,6,4,4,-9,-6,-8,-9,-5,-9,9,1,2,9,-3,-1,4,2,-7,3,-5,-10,-3,6,-4,-6,-4,4,-9,7,-7,-2,6,-8,-2,10,2,-2,9,-7,-3,-7,2,-5,6,2,10,4,-7,10,7,-9,-10,-6,-1,3,5,-10,-3,7,-7,-3,-10,3,-3,-9,3,-9,-10,-9,7,-6,-3,-1,-1,4,-7,5,5,-7,8,-9,5,-1,3,8,5,-4,10,3,-8,-1,5,4,-1,10,-10,-10,5,2,5,-9,3,9,1,-7,10,-3,4,-6,-10,-6,-5,5,-2,-7,-8,7,10,-5,7,-1,9,-3,3,8,8,-6,-2,3,10,9,8,9,4,-2,-7,-10,-7,1,-2,7,-5,-1,6,9,5,5,-7,-3,10,2,8,-6,-4,-7,8,-6,-9,-9,2,2,-7,-5,3,5,-3,3,-8,-8,-7,-9,-1,7,-4,6,4,7,6,6,-8,-5,8,4,-6,-2,-7,8,-8,9,-3,9,-2,-1,-6,10,-9,-7,-2,5,-1,-2,8,8,7,9,2,-7,2,-5,-6,2,-9,-2,-10,-10,4,3,2,-9,1,-8,5,9,5,6,2,-7,-9,-3,-6,1,-5,-5,6,-5,-3,1,-2,5,-8,-1,1,1,-6,10,-7,3,7,-8,-1,1,-10,2,-5,-9,8,-1,-7,2,7,5,-4,6,4,6,9,-9,-10,-10,8,7,-3,-6,1,4,-9,-1,-9,4,-3,1,8,10,3,-4,-3,-8,7,7,-1,5,-1,-2,-5,4,-9,-7,-6,-6,1,9,-10,10,-10,-7,-9,-10,-1,1,-3,2,-1,-10,8,-6,-7,-4,-2,6,3,-3,-6,-5,9,10,2,-3,-1,-9,-2,-1,-2,6,9,-5,5,-7,3,5,7,-4,-7,1,2,8,-7,-3,-4,-2,-2,7,7,6,5,1,-7,2,-6,2,3,3,9,-8,6,-5,-6,-6,6,4,3,5,2,4,10,-5,-5,4,4,-6,3,9,-4,4,-6,5,-4,9,-8,6,-8,3,-1,9,9,8,-9,-3,3,-6,6,8,2,7,-10,-7,6,-6,-5,4,2,-7,-8,-5,8,10,1,-5,5,2,-7,-6,7,1,6,-9,7,1,-6,6,6,-9,4,-1,-6,-4,9,5,1,9,3,-8,-6,6,5,-8,-10,9,9,-10,-10,7,4,7,-9,-3,-6,3,-9,-4,10,5,-8,-3,6,-3,8,8,-3,-7,5,7,2,5,-8,8,-10,-8,-9,7,-6,2,2,8,-6,8,-7,-3,4,2,7,-9,-3,9,-10,7,-7,-10,10,-4,2,-8,-8,10,10,-1,-10,-6,-9,-4,1,3,-2,-9,-10,9,-7,-3,-7,-5,2,4,8,4,-6,6,-10,9,1,-2,-3,3,7,2,-6,1,-7,-10,8,2,-2,3,-7,-6,10,-9,9,2,-9,-2,-3,5,-1,-7,-10,-4,7,-8,10,5,2,-5,-8,-8,1,-4,-4,-6,-5,-3,2,-9,5,-7,1,-8,-4,5,10,-8,5,7,10,-4,6,10,-5,1,8,6,8,4,7,-5,-5,5,-5,-1,6,10,3,2,-2,-9,-10,2,8,-9,7,9,-7,4,-9,-8,8,-8,1,10,-4,-4,3,2,1,-8,5,10,6,-7,9,-1,-5,-2,3,-2,1,1,1,9,3,2,-5,-4,-8,-5,6,6,6,-10,9,6,-7,6,-8,-1,2,-3,-8,9,5,3,-1,5,-8,-8,8,-9,-1,-4,-9,4,-8,10,3,10,-3,-1,3,-4,4,9,6,-6,10,7,-5,-3,-7,7,-4,10,-1,4,9,-6,-9,-5,-1,-3,-1,4,-1,-6,-2,8,1,3,-9,5,-4,10,-8,-10,6,-1,4,-10,2,3,1,8,-9,2,-8,5,2,7,10,8,-3,-10,2,-3,-8,-8,10,-10,9,-7,3,-8,7,4,3,3,10,-2,-5,-7,-1,-3,3,10,-9,8,8,6,3,5,1,3,-1,-4,-10,-9,-7,4,8,-1,-10,9,-9,5,7,10,-8,-1,-6,7,-7,-8,1,-4,5,-7,4,-3,1,5,-10,7,-7,-8,5,-10,-2,-5,-2,3,4,-2,-6,-3,5,-8,-4,4,5,-6,-9,-1,7,-5,6,-6,-10,9,5,6,2,4,8,7,2,-4,-10,-4,-2,7,9,-6,-4,-6,9,-1,-5,-8,5,-8,1,-7,-4,9,10,-4,1,-7,-5,4,-6,-6,9,5,1,10,3,4,-10,5,-9,8,-9,5,-1,-9,-5,7,-2,10,6,-7,9,6,4,-9,10,-3,6,2,-8,-2,9,6,4,5,8,-6,-3,6,8,10,-7,-7,-2,8,-2,-2,-2,2,-6,5,-9,1,-7,-9,6,-3,6,-6,10,8,-6,5,-1,-5,4,-1,3,6,10,-5,7,-9,-7,-1,9,-3,2,-3,4,1,10,-2,-3,2,-6,-10,-4,-7,-4,-2,-2,5,2,8,-8,6,1,10,8,7,-9,-8,8,8,6,4,-2,1,-9,-9,-7,4,5,-4,-5,7,-10,7,-2,9,-4,3,1,1,4,8,7,1,-5,-4,-6,2,-8,3,5,-8,-4,-8,-9,-7,-1,6,9,1,-4,2,-8,5,5,-7,-1,-3,8,-2,-2,-1,5,4,-5,-6,10,9,4,5,4,-4,-7,-10,10,-3,2,-7,1,3,-6,7,8,-3,3,-4,10,-4,6,-5,7,-1,3,-7,1,2,-8,-3,-6,1,-6,8,2,4,-5,6,-6,2,5,6,9,5,-9,-6,-7,-6,-1,-9,-4,4,-2,3,7,9,-7,10,-5,7,-3,10,-9,5,9,-6,-6,4,1,8,-5,10,4,-9,-4,2,9,-9,6,-2,-5,10,9,1,-5,5,-6,3,-4,-8,9,6,-1,6,-7,4,7,5,-10,-5,5,-7,7,-8,10,-9,-5,-7,-10,-6,3,10,4,5,4,-10,-4,-8,7,-3,-4,-8,-7,-7,-9,-5,1,-2,3,-2,9,-3,-1,3,-9,-4,9,3,-6,5,1,8,3,8,7,-2,2,-9,-8,-10,1,1,-8,7,3,9,-10,-8,7,1,-8,8,8,-2,4,-5,-5,-6,-1,9,5,-9,-7,9,5,-5,3,-2,3,-9,-5,3,-3,5,3,7,3,4,5,1,-5,4,2,-3,1,3,8,-9,6,-2,-9,-9,-7,10,8,5,-10,3,6,-8,-8,2,-8,7,-7,4,-10,-8,-6,2,-2,7,-5,-3,-4,7,-1,-8,-9,4,5,-2,9,-3,-8,8,3,3,6,8,-8,-2,3,-9,-6,-10,9,8,-2,4,8,-2,-9,-9,-3,-5,-2,-2,-10,9,2,-6,5,-10,5,-9,-9,-3,9,5,9,-3,-8,7,-5,-3,10,-7,-5,2,-4,4,3,2,-1,4,-7,-10,1,5,6,3,1,-8,1,-8,-10,-6,2,-5,-7,3,-7,10,-2,3,7,1,8,-4,-7,3,7,-2,-9,3,7,9,1,-1,-6,-1,2,3,-9,-10,1,6,3,8,5,6,-1,6,-6,-5,3,7,5,-9,9,3,-1,8,6,-5,-1,-5,-10,4,-1,-10,4,2,-9,6,-8,-6,9,-6,1,-10,-6,5,-7,10,8,2,7,-3,-5,-4,1,6,5,-7,-3,1,1,5,-2,5,7,4,-3,2,-8,-3,-6,9,2,8,-10,-7,4,8,-7,8,2,7,8,5,4,3,8,-9,-7,-8,-5,-7,-4,-5,-9,2,4,9,9,-8,-4,2,4,-4,10,5,6,-4,-8,-9,3,-2,-3,1,-5,-4,1,-2,-9,3,8,-5,-1,-5,10,-9,7,4,-2,-3,-3,7,5,6,-6,3,6,-10,-9,-9,9,3,-9,10,-1,8,10,-7,-5,-8,1,-6,-1,5,1,8,4,-8,10,4,-10,5,-8,-8,-5,-5,-10,-3,-9,-1,-6,2,2,-1,-1,4,-7,-3,1,-9,10,1,9,10,-6,-10,-10,2,-6,2,8,-9,5,2,-5,-10,-7,4,-9,-3,5,-7,8,7,-4,9,7,7,-10,-9,1,10,2,-3,-10,8,-10,2,-6,-1,-2,-2,-10,2,-9,-5,-2,-8,10,-7,-6,6,2,5,9,-8,-8,-1,-1,-10,-5,1,-1,4,-10,2,8,5,7,9,8,10,-8,-6,-5,-1,1,-10,3,-4,4,1,5,3,-6,10,10,1,1,10,6,-6,3,1,-9,9,2,-7,-5,-1,-5,-6,2,-4,9,-9,-3,-3,-3,4,-1,5,-2,10,-5,10,-1,6,4,-6,-3,-7,2,-5,-6,6,4,1,-6,-5,2,-2,2,8,-7,10,-1,-8,-8,-7,4,2,-7,-3,-5,-5,-4,2,6,-3,-6,4,-1,-2,7,-5,-5,8,9,-6,-2,1,-9,-3,5,-1,-10,-10,-7,-1,-4,-5,3,-2,7,-9,8,-4,-5,5,4,4,-8,6,-9,-2,-5,-1,-10,-5,10,5,-3,4,-7,-9,4,6,8,-9,-3,9,8,8,-2,7,6,9,-5,7,-3,-7,-10,8,7,4,-8,7,4,6,-8,-7,8,-2,-10,-7,7,-9,-6,-6,4,-4,4,10,7,-3,2,-9,-7,-5,2,-1,5,10,7,-6,-8,3,2,-10,-1,3,-7,6,-3,-3,3,8,4,-1,3,-1,-8,3,-10,-6,-7,6,3,-10,-1,5,-6,3,-10,10,10,2,-6,7,-9,-6,-3,-2,4,-5,4,-10,1,-2,-8,4,-2,5,3,-3,-6,-1,-1,5,5,-2,-10,-1,8,1,4,3,2,-5,9,-7,8,3,-1,7,-8,6,3,-8,1,-6,-7,-4,-4,-3,-6,7,-10,-3,1,-8,-1,7,-2,-5,-6,-1,-8,1,-3,-9,7,-2,8,-10,7,8,-4,2,-1,10,-9,-10,3,3,6,-4,-7,1,-6,-4,1,-3,-8,1,-3,7,-2,-1,8,3,-5,8,7,-9,4,-6,-7,2,-5,5,5,-1,8,-4,-7,2,-7,-6,-2,7,-8,3,-3,1,7,7,-7,-9,-2,1,1,1,-4,4,4,3,6,7,10,-7,-3,7,3,-5,8,-4,1,-8,-4,2,4,10,-1,9,-7,6,-1,10,-8,8,-2,8,-10,6,-1,-2,4,-4,10,-6,-2,-7,-7,6,3,-5,6,6,-2,-10,3,-9,-3,-5,8,10,-6,-10,7,10,10,2,-1,-2,5,7,3,8,-8,-10,2,4,-8,-3,-2,4,-8,-10,7,3,5,1,-3,3,-9,8,5,-1,10,-8,7,-6,10,-6,-7,10,-9,9,1,-3,-5,4,-5,-2,1,7,6,6,9,-5,-3,8,8,-3,-9,1,-9,5,2,-1,9,-2,1,-1,2,-5,-10,6,-2,9,5,-7,-5,-2,-10,-1,-9,4,-2,10,-10,8,10,10,-3,3,-10,-4,-3,-5,9,1,-10,-10,9,-8,-5,-9,-10,-8,1,-1,-4,-8,-3,-7,9,-10,3,3,10,-1,8,1,-10,-9,2,1,-8,10,-2,-4,7,9,-4,1,2,10,-1,-7,1,3,-7,9,5,-7,-8,-5,-6,4,5,-5,-5,-8,-5,-1,-1,10,-9,5,8,-9,2,-1,8,-8,9,3,-8,4,4,-2,10,-4,8,-2,-1,3,7,-2,9,2,-5,6,4,9,-5,-6,10,1,9,-6,-6,-4,3,10,9,-10,4,10,-3,-9,-9,-3,-5,8,-10,4,3,9,-7,-6,8,1,-1,4,-9,4,8,-8,4,6,-2,7,10,1,-4,2,-6,-6,5,3,-4,1,-6,6,-6,-1,-3,-6,-6,-10,8,2,6,-1,1,4,-2,-7,5,8,6,-2,2,3,4,8,-5,6,-2,2,-10,7,1,-10,-9,-8,2,5,-7,-1,2,-5,-2,10,-5,-7,9,6,-10],[-8,9,-4,-7,4,-7,-5,6,6,8,-2,-8,-9,-3,-9,-3,1,-3,4,4,-4,-5,-10,8,1,-1,2,-3,8,-5,-10,4,-4,-6,8,8,-1,-10,6,-6,-5,-1,8,-7,-2,3,-5,-3,5,7,1,3,10,4,3,-6,-9,-7,-3,-5,-9,6,7,-2,3,6,-7,-8,4,7,-2,-6,-10,-9,-7,7,-1,1,6,-10,5,1,-5,-2,-10,6,10,4,5,4,-6,-10,-5,6,-6,-8,-2,-4,-9,6,3,-3,4,-4,3,-4,8,7,-7,-5,-9,4,4,-10,4,4,10,2,-7,4,6,-8,-2,-10,-7,-1,-7,-10,5,-4,8,8,-5,3,-9,-3,-6,9,-7,-8,3,-3,-4,-1,-6,10,3,3,8,-2,-4,-2,-8,-8,-2,-1,6,5,-8,-3,-1,8,8,-4,7,3,-2,4,6,7,10,2,4,8,-4,-6,-3,-1,-6,-5,-10,6,3,-4,-4,6,-10,10,6,4,10,-6,-4,3,-1,-5,-9,3,-5,-1,-9,-2,5,-1,-3,-4,-6,-5,-9,-2,-9,1,2,-7,2,-5,-5,8,-9,5,-5,-5,1,-3,10,-1,4,6,8,2,-1,1,-4,-10,-1,4,-3,-6,1,-5,7,-2,7,-9,-9,-7,10,10,10,-6,2,6,1,10,-3,4,8,-1,2,-4,-10,3,10,1,-3,8,7,1,-7,-9,-5,-8,-9,-9,-8,-1,-3,-6,10,-2,6,-8,-5,-2,-9,3,-6,-6,2,3,8,8,-10,4,-4,3,-8,3,-10,-6,-8,1,-1,-8,-2,-5,-6,-4,7,-8,-6,-1,2,8,10,10,-4,-3,-10,10,-1,4,7,-4,8,5,3,-10,9,8,1,-9,-9,-10,3,-2,-6,-2,6,7,-7,2,8,6,8,-9,10,-2,8,1,-3,-6,9,3,-5,3,-5,-4,5,-2,-4,1,-9,-6,-6,-8,7,-9,-3,6,-5,10,2,-4,-3,-1,7,10,5,-3,-10,4,-7,8,7,8,2,1,9,2,-4,-9,-3,9,7,-10,4,-6,9,3,-7,8,-8,-5,6,10,-8,-1,10,-10,-1,-3,6,-8,-7,-9,-3,-6,-5,9,-6,-1,10,9,1,8,-2,9,-2,3,9,4,10,-4,-10,-6,3,-3,9,-4,3,-2,-3,-3,9,4,9,-1,-7,3,9,-6,-9,7,2,10,-5,10,-3,-3,-10,-10,7,7,-8,3,-10,-2,-9,6,-2,7,-9,5,10,6,-5,1,10,7,-6,5,-1,-6,-6,2,-9,5,-3,-1,8,-5,6,6,3,1,-8,-7,5,-9,-6,-1,7,-2,-8,-5,2,1,7,-1,-3,-10,-1,1,-10,7,9,-10,5,9,7,-10,-8,-7,8,-7,-4,-3,-6,1,5,4,7,2,-8,-5,-9,-5,6,5,-4,7,1,-3,6,-5,-5,7,-2,5,-2,-6,7,-1,5,-5,8,7,3,6,-3,8,-1,9,4,5,6,10,-3,4,-6,-9,2,2,5,5,-1,5,10,7,-9,3,-4,-9,-3,-6,-4,3,-8,-3,5,10,-3,-9,-10,6,-7,-7,1,7,-8,2,6,2,-10,-9,-3,2,6,8,8,-7,10,-7,9,4,6,1,-3,10,-8,-10,-7,-6,6,7,7,-8,-8,-9,-10,4,10,8,10,7,-6,-8,1,-4,-9,10,6,4,-4,3,-5,8,4,-9,5,-2,-2,3,-6,10,-1,3,10,-3,10,8,3,-1,5,1,5,-2,6,2,-4,9,-5,-5,10,9,4,-7,3,-5,-9,8,-10,1,-8,7,-7,7,1,-7,10,2,3,-10,-9,-5,-1,-10,-5,-6,6,-5,2,-5,4,3,-7,-7,-4,7,3,-2,8,5,5,-8,-7,-5,7,-3,3,-4,-2,-1,1,2,9,-6,5,10,-5,10,3,4,-7,-10,2,9,6,-10,7,9,-5,-4,-8,-10,-5,8,6,-6,6,1,10,4,1,5,8,-7,10,-3,8,-5,2,10,3,10,4,1,-5,-1,9,-6,1,9,-7,-2,-4,7,-8,5,-7,-3,8,6,-9,2,5,4,-5,9,-5,-4,-6,4,-2,-7,6,9,-6,-9,-5,4,3,8,-2,8,6,6,-5,-7,-1,-5,8,1,10,-10,3,5,-3,3,-9,-5,-3,8,5,-4,-4,3,2,8,6,-8,-4,-6,-7,-6,-10,-3,4,-2,1,-5,-6,8,6,3,-4,2,4,-6,-7,-9,-3,-1,-4,-6,-2,1,-3,9,3,-1,10,6,1,7,4,6,-6,4,3,-6,-3,2,-6,-3,-2,-7,-8,-8,-4,-7,-1,-4,2,-1,-8,-10,6,4,5,-10,-2,1,9,-8,-4,-1,-10,4,-3,-8,1,-9,-4,-8,2,7,-4,-5,8,6,-10,9,-2,-5,7,5,3,-5,-8,-7,-9,-8,3,-8,7,-4,-2,9,7,8,-7,-10,-6,-9,-7,9,-3,1,-10,-10,4,6,-9,10,10,10,1,-10,-6,-3,7,9,9,-7,-10,8,3,9,-10,7,-7,9,-6,4,8,-3,1,7,3,-9,-1,6,-2,5,4,-3,-9,-8,1,-7,1,-6,-3,2,-6,-6,9,-2,-6,2,9,10,8,-2,-2,-8,8,-7,6,6,2,1,-5,2,-10,-1,2,6,1,-10,7,-8,-1,-8,4,-1,8,-8,2,4,6,10,7,9,4,-1,-9,-9,-3,9,3,-8,9,5,7,3,3,1,-9,-7,2,-7,-8,1,-5,3,-10,2,6,-1,5,6,9,-9,2,3,-6,4,9,7,6,6,10,5,5,9,-2,-9,6,9,-4,1,7,5,-1,-1,-2,-2,5,10,-3,-10,-8,6,-7,-2,-1,2,-8,-3,-9,5,1,6,7,6,5,-7,-4,-6,1,-1,-1,-8,10,-10,-8,-10,4,-7,-2,-3,10,9,-4,-5,3,7,1,-4,9,-7,9,-5,3,-6,-6,1,10,10,-7,10,2,-7,-3,1,-5,8,-8,-8,7,-8,-4,7,-1,9,1,-1,5,4,-6,-9,-5,-6,-1,6,10,-9,4,-8,4,-4,-5,7,-10,-9,8,-1,6,-6,2,3,7,-6,-9,-6,10,-5,7,-6,-5,-5,-2,3,-4,4,-4,-9,8,-2,8,9,9,4,8,-3,6,3,6,7,-9,-7,-8,2,2,3,3,9,-8,8,-6,6,-10,-9,6,-8,4,8,4,8,-5,5,4,9,-8,7,-9,5,3,10,9,-4,5,-7,-3,2,-7,-5,-2,5,3,-3,7,6,9,1,3,-3,9,-7,4,-8,8,-1,8,-10,10,-7,-9,-6,8,8,-3,10,-10,4,-8,-4,6,9,-3,-8,10,7,6,-2,1,6,3,-7,4,-7,-2,1,6,3,-6,-2,4,-10,5,7,-3,1,8,1,7,-4,-8,-8,-2,-6,4,7,-9,10,-10,-1,9,-9,8,-7,-7,-6,4,1,-7,-6,-7,10,-1,-2,-9,-4,-5,-3,2,-9,-1,-3,-1,2,-1,10,1,-6,10,3,-2,-6,-7,-1,-1,9,-5,8,9,5,-8,10,3,-2,-5,-2,2,-2,-9,10,-5,-1,-3,8,8,-4,8,-6,1,6,4,10,10,-5,-7,8,-5,-2,-9,-2,4,3,-1,3,-8,-5,8,8,-9,6,9,-8,4,-3,-2,10,-1,8,-4,4,-1,-4,-6,9,-7,-5,-9,-9,5,-8,6,-5,-2,9,-5,8,3,8,-6,9,10,-8,-7,5,-8,10,-2,-3,7,2,6,-9,4,2,-2,1,-3,2,7,-3,-2,-1,6,-1,-5,-5,5,-9,1,8,2,-7,10,6,-9,-4,-2,5,6,-10,-1,1,-9,6,4,5,-5,3,-4,-5,-10,3,-2,9,-4,-1,4,-2,2,4,2,-2,-2,2,-3,-8,-4,4,-9,7,10,10,-8,8,10,8,1,-9,-4,-8,6,2,7,9,7,-1,2,2,6,1,-1,-10,-8,5,7,-1,-9,4,-6,-2,-7,-1,-4,2,-4,6,4,8,-4,-6,-6,4,7,-9,-1,8,-4,10,6,8,6,7,-9,-2,8,3,-4,-7,-9,5,-9,-9,-4,3,-2,1,-6,-6,3,-9,5,-5,1,1,2,9,9,-8,-10,6,-3,-9,-5,-3,4,-9,4,-9,10,4,-6,-5,2,9,-6,3,1,-6,7,-5,1,-10,-2,9,-9,-5,-5,-9,6,2,-4,-9,7,1,7,6,2,1,7,5,3,8,-10,7,-4,8,-4,-2,4,-8,9,-7,2,-2,-9,4,7,-10,-8,5,-5,-1,-1,3,-6,6,-7,-6,-4,7,-5,3,-10,1,1,-1,8,-9,-4,-4,-3,6,7,8,-10,3,3,-9,1,2,-3,-10,4,-2,2,-7,-8,5,-4,-7,8,-10,-9,4,7,4,9,-5,-5,-1,2,-4,-10,-6,-3,-9,-4,-10,5,3,-9,6,-2,1,7,-4,10,9,-8,6,-9,-10,1,-6,-3,-2,9,-2,-8,-10,-5,-4,-4,-4,-8,-4,3,-10,6,-5,-8,-3,5,-7,8,-10,2,7,6,8,2,-1,-6,3,8,10,3,2,-9,-2,8,10,-7,8,10,7,10,9,8,9,-10,-3,-4,-2,6,2,10,-6,10,-10,1,-4,-5,8,-7,-1,-6,1,-9,-5,-10,1,-10,7,-2,-2,-6,6,1,7,1,-6,-2,6,-1,8,-9,-3,5,-1,-9,-10,9,-6,-9,8,-3,-6,-1,-6,-5,-8,-3,-3,5,7,-7,8,-4,8,-1,3,1,7,-4,-8,9,-3,-9,1,10,-7,-5,-5,-3,-2,9,6,-5,-6,8,-7,-2,-9,7,-6,-10,-4,-9,-3,1,-7,-3,2,8,6,-4,4,3,6,5,-5,-6,-1,-7,9,2,-8,-1,-2,10,6,2,7,-5,-3,6,7,-6,-7,5,-1,-2,-3,-1,1,-4,3,-8,1,-7,6,-2,-5,3,3,10,4,-5,6,-3,-7,-5,-3,3,6,8,-3,-5,9,4,6,8,-7,-9,10,9,7,10,-5,-5,4,3,4,-8,7,-6,8,-3,6,-6,-3,6,9,1,-8,4,-10,9,-6,6,3,-6,-6,3,-2,10,6,-5,-1,-8,5,-1,1,-8,9,2,-5,-10,-1,7,-6,9,3,8,2,-3,1,3,-3,1,-6,3,-1,-4,-10,6,-8,-1,-10,-6,-6,-1,-10,9,7,7,-2,7,-5,-8,2,2,-8,2,1,-2,7,-6,-10,-2,6,2,-10,-3,-8,2,4,1,-7,2,2,-7,-9,-6,1,-6,7,-6,5,-4,2,-6,-9,10,1,-4,-8,-2,7,6,5,-6,9,9,-1,10,8,2,4,-1,-6,10,9,10,9,5,-7,-6,1,2,-8,-7,-10,-2,-1,-1,-2,-10,2,-9,6,-5,-3,9,4,-7,-4,9,-5,8,5,-2,10,-10,-4,5,10,-10,9,-8,1,-7,2,-10,-8,3,-10,2,9,-4,2,-2,9,7,3,3,3,-10,-8,1,3,-1,9,4,-7,2,10,-2,-7,-7,6,-6,-9,-3,-9,5,6,-4,9,-4,8,6,1,-5,10,-1,-1,7,-5,9,5,-7,-9,-8,1,-5,-10,-5,2,1,1,10,1,5,8,-4,-7,-3,-4,-5,5,-1,2,7,-7,7,4,-1,-3,-3,-2,3,9,-8,-9,5,-4,2,-2,1,9,9,-5,10,-9,-10,-9,-10,1,1,-10,5,-3,-1,5,-6,10,-10,6,-7,-3,5,2,-2,5,2,-8,-1,-3,7,4,4,7,-1,6,-9,6,2,-1,-8,8,2,-6,-8,-7,7,-6,-7,9,-7,7,3,-10,-1,9,-7,-1,2,4,-6,-5,-2,6,-4,-7,-9,9,-8,-4,9,-8,10,-7,-7,-2,-4,6,8,3,-8,-4,-7,-6,1,-3,3,9,1,6,9,-10,7,-8,9,-8,4,-3,-7,5,9,2,-7,5,-9,5,1,2,1,-2,1,-9,-5,5,1,4,8,-4,-7,5,10,-7,-5,-8,6,9,3,4,10,2,1,-3,-3,4,-6,7,8,8,2,-10,-9,8,8,-1,-3,-10,-10,5,-10,3,-7,1,-6,-1,-6,-7,-1,-6,-8,7,-2,8,-10,7,-4,-5,3,-8,-6,7,9,6,10,-9,10,10,5,-6,-2,6,-5,7,-6,1,4,-3,-4,3,2,2,9,4,3,10,6,1,6,1,5,-5,10,9,8,7,5,-2,5,-2,-7,-4,-8,-4,5,10,7,-6,-7,2,1,5,-1,4,-2,-4,7,-2,5,1,3,-9,-9,9,3,1,-3,10,3,1,8,-4,5,4,-4,-9,8,-7,-4,3,10,-1,-10,8,-5,-9,-6,2,1,-3,-10,-1,-2,-5,7,-6,-4,1,-8,-9,1,9,-3,1,6,-8,-6,-7,9,7,-2,4,-9,-1,-5,-9,-8,-4,-9,6,8,-2,-5,5,10,10,4,-9,-9,10,-1,-10,7,-10,8,-4,10,-1,6,8,9,-10,-2,-7,-9,4,-6,-9,-8,-3,-4,3,2,8,-1,6,6,4,-4,8,-8,3,7,-8,10,-1,8,-8,-7,10,5,-7,-3,9,-2,1,9,3,-6,3,6,-10,-10,-7,-7,7,5,4,-5,-5,10,-8,-2,7,5,5,3,-6,-4,-10,-1,6,10,-4,-5,-3,-7,-3,3,-8,-9,-8,8,5,-6,-4,1,5,-10,-8,9,9,4,6,4,-6,7,-5,-9,-7,-7,-3,1,-2,6,7,3,1,9,-5,-3,6,-4,-5,5,-7,4,-1,-8,5,2,9,-7,-3,10,-9,-6,3,10,-2,-1,-7,10,10,-2,-10,-9,10,-1,-2,8,6,-8,5,-8,-3,7,-5,-8,3,-2,-4,3,-6,-4,7,-2,7,1,-10,-10,-9,-2,4,-1,-2,1,3,10,10,10,8,-10,5,-7,-2,7,4,8,-1,-6,-2,-9,-4,-6,4,4,9,-7,7,9,-2,5,-6,-5,-3,-2,-9,2,9,-10,4,-7,7,-9,-9,-6,-7,-7,3,1,-3,1,-3,7,-10,7,10,1,7,2,10,-6,-6,-1,-5,6,-5,-1,-9,10,-5,5,2,-3,-6,6,-10,3,5,6,6,9,-1,10,9,1,-9,-1,10,2,6,2,-2,3,-10,-9,-3,8,9,3,-7,5,-1,-9,-8,-9,-10,-2,9,-2,-8,-3,-9,4,8,9,-4,-1,1,-9,10,-5,10,-5,-7,-8,-7,-6,4,8,1,-5,-2,-1,-6,-3,-8,-1,8,-7,-2,-1,-8,7,9,1,-3,-7,3,-7,8,-9,8,7,5,-4,1,-8,-2,-8,-10,-3,5,9,9,1,8,6,-10,-6,6,-4,3,5,-6,-10,-4,-9,-4,1,6,3,-1,-2,9,-8,5,-6,-1,-8,6,3,-3,-10,-3,-2,-10,5,-1,2,4,-9,-1,9,-5,-1,7,10,-8,-8,-1,2,-3,-5,-5,-8,-9,9,-1,-4,-7,9,6,-3,2,-5,-2,-6,-5,1,8,-8,6,6,6,-6,-4,-9,6,7,3,-1,-9,2,-8,6,4,-4,1,-10,2,2,-2,-6,-2,4,-5,2,4,9,-9,-7,-1,5,-2,1,-2,-10,5,-3,-1,6,-4,1,4,-9,7,8,-8,9,10,6,4,-6,-3,6,8,9,10,-9,2,-9,-5,-6,-2,6,5,-3,7,-8,10,6,5,7,7,-4,-5,9,-2,6,-2,-5,4,5,-9,4,6,5,-7,-1,-10,7,-7,-9,3,-4,-8,3,-9,3,-1,5,-1,3,5,-4,8,-2,10,-6,7,-10,-9,6,1,-5,-8,-4,-1,9,-8,10,-6,10,6,-1,-6,-9,-3,-4,-6,-9,-9,5,7,-5,9,-2,2,1,10,2,-2,-2,7,7,8,2,-8,-7,-1,1,-2,4,-7,-1,-6,2,5,1,3,-9,-6,6,8,-1,10,8,7,5,7,-10,10,-1,7,10,3,-8,-8,5,2,4,1,5,4,-3,-7,-5,4,-3,-9,-8,-10,-3,3,-4,-5,-8,-2,4,2,-8,8,-3,1,-3,8,-5,10,-7,-6,-9,-9,5,7,-7,7,-7,3,9,-5,-6,-4,1,1,-8,-9,7,-3,1,-2,-10,-6,-3,-6,-4,-5,-5,-3,4,4,-2,10,-3,2,4,2,2,-10,6,-7,8,-1,10,9,10,9,-8,-1,-1,-3,-4,8,3,-1,5,-9,10,6,-8,8,-10,-9,-6,-9,1,2,7,3,2,-8,4,8,9,-5,-2,-4,8,3,4,-10,4,-4,6,10,3,-2,7,-10,7,3,6,4,-3,-9,8,5,3,-2,9,6,-2,-1,-10,5,-6,-7,-8,-8,7,-9,7,9,-5,1,-5,-8,-3,5,-7,3,1,-8,10,-1,5,3,5,-4,-5,4,9,-8,-10,10,-3,3,-2,4,-6,2,-4,5,-9,10,5,-5,-6,1,-5,-3,3,-4,-6,-8,3,6,-2,-7,-2,-4,-10,1,1,-4,-2,-9,-3,-7,-1,-1,-2,-2,-8,7,3,-6,2,1,-9,2,-1,4,3,-5,8,-1,-5,-7,9,4,7,6,-9,-3,-3,-10,5,10,-7,4,-5,6,-7,4,6,9,9,-5,4,7,-4,-4,10,8,-1,1,-9,-5,-9,-2,8,-10,-9,-5,2,2,8,-4,-10,-4,-7,6,-3,10,-3,-6,-6,-9,-1,7,6,-7,5,-3,-6,-5,-3,8,-3,5,-5,-6,7,-5,10,2,-3,-2,-2,3,-3,10,-9,-9,1,6,-7,6,-8,2,2,5,3,-4,-4,3,-5,-3,-5,5,-8,-1,-3,-1,-7,10,9,5,-5,-8,-7,-6,6,-5,4,7,10,9,5,6,-4,-1,2,-6,-6,5,5,-4,-3,-2,-8,10,-8,-3,8,-5,6,7,4,4,-6,-3,-2,-2,5,-1,4,3,2,-5,5,-5,5,-8,5,-9,1,-2,9,6,-9,-9,2,-4,-7,-5,8,3,1,-4,-3,7,-5,5,-4,-1,9,5,3,-6,-8,-5,10,-2,9,-5,-7,6,-1,7,3,-8,10,-6,3,-3,10,7,-6,-10,5,9,10,-5,8,8,-1,-4,10,-4,-1,-3,-5,-2,9,5,-9,-5,2,2,3,-1,-6,5,-6,-8,4,-1,-4,-9,5,7,10,5,-4,-2,-8,-1,-2,2,-3,-7,4,5,1,10,-8,1,3,-2,6,-3,-8,1,-1,10,-5,-1,6,-8,-2,2,9,9,-1,8,4,-4,-8,-4,9,-2,-2,-5,9,-3,6,-10,-1,7,-10,1,-8,8,-9,-4,-6,-3,7,7,3,-8,5,2,-9,-10,-5,4,-6,-9,5,-1,10,-1,2,-5,-6,-4,5,1,-6,-4,3,-4,10,-6,-7,-8,-3,-5,5,-1,-7,5,2,5,-6,1,-6,-2,10,-3,-5,5,-8,-4,-10,-5,10,8,-6,2,-3,3,9,8,-3,6,2,7,-2,2,-4,1,-6,7,-4,-4,-3,-6,4,2,7,-7,-1,-8,3,-9,8,4,10,8,2,3,-10,-10,5,4,-1,-10,5,-9,7,-9,9,10,5,-5,9,6,7,8,9,-5,-4,7,2,-10,-4,-5,-2,-2,3,8,7,3,-2,-5,4,-3,4,8,4,4,-6,-10,-2,-5,-2,-8,7,-3,4,-9,-10,5,-2,8,10,3,1,-2,8,7,-2,-10,-6,-7,-3,-9,1,-4,6,9,6,-9,7,-9,1,-8,-2,-2,-1,1,7,4,-3,-9,4,6,-1,-8,-8,-5,4,-2,2,-9,2,7,-1,7,1,4,3,-7,4,-3,2,-3,-3,-5,8,-6,-3,2,-5,-7,-5,4,-2,4,-8,-10,7,7,6,-3,-7,7,-3,5,5,6,4,10,3,-1,1,1,3,-5,3,5,10,-1,10,1,-7,-7,-9,8,1,4,1,9,7,-4,4,2,1,7,9,-7,6,-9,3,10,-7,5,4,-3,-7,-3,8,5,1,3,1,-6,5,6,3,1,10,9,7,-7,10,-7,7,2,-5,8,4,-5,-1,9,6,-5,6,-2,-5,1,-9,8,2,4,2,5,7,-8,-10,-10,9,-5,-9,-9,-4,-2,9,-10,7,-10,7,-6,5,1,-1,4,-8,6,-3,-2,7,1,5,9,-7,-2,2,9,3,5,-2,-5,-7,8,8,-9,7,1,3,-5,-8,-7,6,-10,-5,-3,5,7,-1,-1,6,-3,2,-4,-5,5,5,-8,7,10,-4,-1,2,-10,-7,-1,-3,-6,10,9,-9,1,-8,5,-8,1,7,-10,4,-4,-2,-3,-1,9,-1,9,7,-5,10,4,4,-9,-7,-2,10,9,-2,7,3,7,8,-5,-7,-2,10,-4,-9,-7,-3,-9,-6,-2,-3,2,-7,-10,-4,-2,7,7,-9,-4,-5,7,2,10,4,-6,3,3,-6,6,9,-2,-1,-6,1,9,2,5,-3,2,7,4,-6,1,-3,-6,5,1,-9,6,-6,8,-2,10,8,-3,-9,-6,-6,-1,-5,3,4,-8,10,3,-1,-4,3,-8,-7,5,-8,3,7,-2,10,4,9,7,6,-5,-8,-9,4,-2,-6,9,6,-7,7,-7,7,10,-1,-7,-4,5,-3,5,-2,8,-1,-2,-8,-2,-2,-1,8,7,6,-8,10,6,-10,1,-5,-7,-6,5,-10,9,4,3,1,3,7,2,7,-1,7,6,-10,10,4,2,-10,7,2,8,-1,-3,-2,-6,-10,-5,-6,1,-6,6,6,-5,10,2,2,-7,1,-3,-4,-4,-3,-3,10,9,-5,-5,2,9,1,-3,-3,10,-10,-9,-2,-1,1,-6,-8,-6,-9,-5,-2,2,-8,-8,7,9,1,-4,-10,-7,-6,4,7,6,3,-6,8,10,-3,8,-6,-7,-4,9,-3,9,-9,-3,2,-2,-3,-2,4,-6,10,-9,1,-3,-7,3,9,3,-4,4,-8,-3,-5,-9,-8,-10,-8,-5,4,-6,-10,-5,2,9,-4,1,1,10,-10,-9,-3,5,5,-8,9,2,-6,10,-2,-1,-4,-8,-8,-5,9,-7,2,-2,3,7,-8,1,5,10,-10,6,3,3,4,10,-3,-6,8,-3,9,-10,9,1,-3,-3,-1,-1,5,-8,3,4,4,4,-9,-2,6,-7,5,3,6,1,7,4,7,4,-9,-9,-10,4,9,-10,-7,-4,-5,-10,-2,-8,4,-2,-3,2,-5,-6,3,8,5,-7,-7,7,-5,-10,-10,8,2,7,-6,-9,10,-8,5,-5,6,-3,10,-2,6,3,-4,-2,-1,-2,-7,-10,8,2,-5,-2,-6,1,-6,4,-9,-10,8,-7,-10,-7,-4,6,4,3,-4,10,1,-7,-6,-1,-7,-6,-2,5,-6,10,9,9,-5,-5,-9,-10,-6,-7,9,-7,-6,3,-10,1,3,5,9,-9,8,3,7,-8,-10,7,-3,-6,-9,-9,1,6,-5,-8,-7,-9,1,4,7,2,7,9,-4,-8,-5,-4,1,10,9,10,-7,10,-3,7,-8,-9,8,4,-2,7,-3,4,8,-8,6,-4,-7,2,-1,-1,-9,4,8,-1,2,8,6,-9,-9,-1,7,9,-10,-5,1,-9,-8,-10,-1,-7,-7,-8,8,-7,-6,-2,-6,6,-4,-8,-1,-9,-10,-5,10,-3,6,1,-1,-1,-1,-10,7,-4,9,8,-8,8,6,8,5,4,-3,3,5,10,10,2,6,-6,9,6,3,-5,9,-4,5,4,-2,1,-5,-3,1,-10,-1,-3,-2,-8,-4,3,-8,-8,4,-2,-10,-4,-4,-8,4,1,6,-6,2,3,-10,-9,-5,3,8,-8,10,1,-10,-8,-9,-10,4,3,-3,-4,-5,3,-10,1,-4,6,2,-10,8,-9,-9,-10,-6,-9,-1,3,-5,-8,-5,-3,-10,2,6,-4,-10,-1,-1,-1,8,-7,-2,5,-7,4,-1,-10,6,3,-4,8,2,-2,-4,2,-5,-1,7,6,-8,-5,-7,-2,-7,-7,-3,-4,6,-8,10,-4,-8,4,10,1,-10,1,-1,2,-9,8,6,7,-7,6,-6,2,3,9,-6,5,7,5,8,-8,8,1,8,-8,4,2,-4,3,-8,3,5,10,-4,1,-4,-1,7,-6,9,-9,8,4,-6,9,1,10,2,7,-6,-7,7,3,-9,8,7,-2,1,-6,3,2,1,-8,-3,8,3,-2,-3,-6,-7,2,-4,-8,-2,-3,-4,-9,-1,8,3,-5,-1,-1,-3,-9,-3,-2,-7,3,5,-4,-3,3,-1,-9,-7,3,3,-4,-10,7,-6,-2,9,4,-3,4,3,-1,-8,-1,5,1,-7,-4,-8,2,-10,-8,-10,-5,-3,1,4,-10,-10,-5,4,-3,-3,-10,8,6,8,6,-8,-3,8,7,-5,6,8,2,-1,3,-2,4,6,-7,-6,2,-4,5,8,5,8,9,-7,8,-8,2,5,-1,8,5,10,7,4,-5,-3,8,-4,-7,-9,-8,5,6,-6,1,4,-5,3,8,4,-2,4,10,6,-8,4,2,6,1,7,-5,8,-7,3,-10,7,-6,9,-8,5,2,1,-1,3,8,-4,3,4,4,-5,4,6,4,8,-2,9,-6,-7,-9,9,-2,-10,-8,7,2,6,-6,8,8,4,-10,-6,-3,-3,5,10,6,6,-4,6,5,-2,6,2,5,-6,9,1,-4,6,8,-1,-8,10,8,-10,10,7,-1,10,7,2,9,-9,10,4,-1,-2,-2,1,-8,4,-2,-6,1,10,3,3,-7,-4,-8,-3,-3,-8,-7,4,9,-5,-10,5,-6,-7,-8,10,-1,-4,-3,7,-4,-1,-3,8,5,-4,-6,-4,5,3,2,-1,-6,-3,4,4,-5,10,-2,-2,4,3,5,6,1,-5,1,-5,3,-5,-9,2,6,4,2,6,-3,8,6,-10,-1,9,3,10,-3,-10,8,8,5,3,-9,-3,-9,2,5,4,7,2,9,-5,-9,-7,-10,-2,-7,2,5,8,-8,-1,10,-3,-1,10,-6,-4,-1,-3,-6,-8,9,8,-9,8,-5,-2,-8,-4,9,1,-1,2,8,5,-10,6,6,3,-8,-3,-4,8,2,-1,7,8,-6,10,-8,7,-9,-7,-5,-10,-3,-4,10,7,5,4,-9,-8,3,-9,2,-10,9,5,10,-6,8,10,-3,9,6,-10,6,-1,7,-3,-8,-1,10,10,3,3,-8,-9,-3,-9,-4,7,8,-2,-10,3,7,6,1,-7,3,-6,-6,-2,-7,-7,1,-2,2,3,10,3,-1,5,8,-8,4,2,1,7,6,-9,-10,3,7,-7,1,2,-2,5,9,-10,7,2,-7,-4,-7,-7,3,10,-5,5,-10,9,-6,-9,-8,-9,-5,1,-10,-5,7,5,-4,-8,-3,-7,3,-4,-10,5,3,3,5,-10,-10,-3,8,6,2,-3,10,9,-7,4,5,7,3,8,3,-6,-4,9,8,4,-3,8,-8,-7,-7,2,8,2,9,-3,7,-5,-2,-2,4,-2,-4,8,-7,-7,-4,10,10,7,-1,2,-4,10,-3,-6,-8,-4,1,6,-9,-6,-4,8,6,1,-8,7,2,-9,10,4,6,-2,-1,6,-3,-2,-9,-3,8,4,9,-9,9,-5,-3,-6,-6,7,9,7,8,-3,2,1,9,5,5,6,1,-2,8,-3,-8,-2,-6,1,10,10,-9,9,4,-4,9,-2,1,5,2,6,10,9,8,-1,-3,8,2,9,-3,-5,-5,5,1,-7,-9,4,-4,-9,-2,-9,-1,-8,6,9,2,-4,-10,-3,8,-5,7,-8,2,-3,8,-1,1,-2,-9,-8,2,6,-2,5,2,-9,-1,10,-4,10,-5,1,-2,-4,-3,-10,8,-8,-8,2,-5,9,-10,1,-3,6,-2,5,1,3,-4,8,10,2,-1,7,7,-3,-6,1,-3,-9,-3,9,4,7,-8,1,2,-7,10,-10,2,4,-8,-9,-1,8,-5,-9,10,8,-10,7,4,7,-5,-3,-10,7,3,1,-6,-9,7,-9,-1,-4,-8,2,-2,-6,-6,8,-5,6,-10,-3,5,5,-7,8,3,-10,4,3,-3,-6,7,6,6,-1,8,-3,5,4,4,1,-5,-8,-6,-4,-9,9,2,-7,5,7,1,8,-7,9,6,9,-2,-10,-8,-9,-5,-1,2,-9,10,-2,-5,-9,5,-4,-8,10,-1,-10,7,6,-6,10,8,6,-7,-1,1,5,-5,-4,-3,3,-7,5,-2,5,-1,-5,8,9,4,-6,-7,10,9,7,2,-9,4,-4,-8,-4,6,10,-3,-7,-8,-3,-3,6,-8,-7,-4,-1,10,-3,-4,7,-8,-4,-7,-9,6,-9,6,-5,10,-7,8,-1,5,9,2,-9,-5,3,-8,7,6,-6,-1,7,3,-4,-3,-1,2,8,-8,-8,2,4,-6,5,-5,6,-2,-7,-8,7,-9,-2,10,7,-8,10,-6,1,5,6,7,-6,-7,-7,6,-8,4,-6,-9,4,-5,9,-9,5,-6,-4,5,3,4,6,-6,5,-6,6,-1,5,5,9,-2,-7,-7,3,-4,-3,8,8,-8,2,3,1,8,-4,-10,6,9,-2,6,-10,4,1,-7,-4,4,-8,5,3,-5,-8,-9,-9,-8,7,-8,6,-2,-4,6,3,7,6,-3,7,3,-5,8,3,6,-1,8,-8,6,1,-1,9,8,-10,-4,8,-2,2,-6,-7,-8,1,-10,8,3,6,-8,4,2,-8,2,-6,1,-6,6,1,6,9,1,9,-1,-9,-4,4,6,-4,9,5,-1,-7,4,10,10,-5,-9,4,-3,-8,6,5,-5,2,-3,2,-8,3,-6,4,-6,-8,5,-4,7,-7,5,4,-1,4,3,-9,6,3,-7,-10,5,-8,10,-1,6,-9,-8,-3,-1,-4,-2,7,7,9,-6,6,5,-4,-8,1,10,6,-2,8,5,-8,-7,4,5,-7,-2,-4,9,-3,2,-2,3,2,-9,9,-4,-3,-3,6,-10,-1,-10,-1,-5,-5,-8,9,6,-9,2,9,6,-1,-8,-9,2,1,8,-10,-8,-10,-1,-10,-2,2,-6,2,-2,2,-1,-8,-2,-6,3,-5,-10,-9,-6,10,5,-4,2,2,-10,-3,5,4,10,-10,-6,6,-10,1,-2,-3,-2,10,4,9,6,5,-3,1,-8,8,3,-4,-9,-10,3,-1,-10,-10,-3,-8,-10,10,-1,7,-9,-5,-1,9,3,4,-3,-2,4,-9,2,-5,10,6,-6,3,1,2,-9,3,-8,-8,10,4,-4,2,-2,-8,4,-6,-10,8,6,-5,-8,-7,-5,-7,-4,10,8,6,9,-2,10,3,-4,-3,-8,-7,7,5,8,-7,-7,-2,9,2,-2,2,2,-3,-6,-9,7,5,8,5,3,8,-9,4,-6,7,-3,-1,-6,-1,3,9,6,3,3,9,10,-6,8,8,-10,-6,-5,10,-3,4,-3,-7,4,-4,-10,2,10,10,10,6,4,-7,-8,2,9,7,-6,2,4,8,-7,-3,-10,9,-2,2,-6,5,-5,5,-3,-8,7,-3,-4,-7,1,1,5,-1,-4,3,3,6,-6,-2,3,8,-9,-3,1,-5,-1,4,-6,-5,2,-2,7,-1,-9,2,4,-2,-2,-6,-4,-7,-7,3,8,4,7,2,-4,-4,9,-4,7,-8,2,2,-4,3,10,5,-5,7,-4,5,-6,-2,-7,8,6,-5,-1,-4,-5,-8,-4,-6,-1,2,-4,7,6,-4,10,8,-9,2,-9,-5,-5,1,6,-10,-10,6,9,-5,5,-9,3,-10,-10,2,-9,6,-10,3,6,-6,-6,-2,6,-2,-5,7,-10,-10,-1,2,1,-4,-4,-8,-2,7,-7,-5,-4,-7,9,9,-2,2,5,-3,-9,-7,8,3,4,-10,-9,-5,3,4,-9,-3,-5,-4,8,-7,6,10,-3,-4,5,7,8,-6,5,4,6,5,-4,-2,-6,-9,-4,6,4,-4,3,-10,5,-3,8,4,-5,-5,-10,1,-7,10,-9,-1,-6,9,-6,2,7,-2,3,10,7,-8,2,2,-10,-1,9,-10,-6,-6,-10,-4,6,-3,-3,8,8,-6,-5,-10,-1,4,4,6,-2,10,3,-10,-1,-5,-8,4,-10,8,9,10,10,1,-7,4,9,3,10,-8,-10,5,7,6,10,-3,-4,10,-7,10,5,-3,-7,-6,-4,8,-9,-2,10,4,-3,-8,9,3,-6,10,-4,-10,3,-8,10,9,-8,-8,2,-8,-6,-4,-4,-3,-9,-6,7,-3,-1,7,8,-3,-8,5,-2,5,-1,4,-5,8,9,-6,-9,9,4,1,2,10,-6,2,-10,-5,7,8,6,7,-1,4,-3,-10,-6,1,-9,-2,6,3,2,-8,-9,4,-2,3,-3,5,-9,-3,10,-3,-4,3,8,5,8,-2,8,4,-4,-5,-5,4,-7,-9,10,-7,-6,2,8,7,-1,-5,-4,10,8,-6,8,-9,7,-4,-9,-3,1,2,-5,7,7,-4,1,-10,9,-5,7,4,9,5,10,4,3,3,4,-1,-2,-3,-7,5,2,7,-2,-5,10,1,-6,-1,1,-5,4,6,-1,2,-4,7,6,5,-4,1,10,2,-8,-7,7,-4,9,8,10,1,-6,10,-2,-10,-7,8,4,5,3,1,-5,-2,6,6,9,-10,4,6,6,2,-10,3,10,-8,-10,-4,5,-1,3,8,3,-8,-9,4,-4,-1,7,-8,1,-2,4,-8,-10,-1,6,-9,-7,-7,3,4,-2,-10,8,-7,-2,10,5,-5,6,-9,5,-1,-3,1,-4,3,-1,-4,-1,-7,-10,-8,-4,-7,1,5,4,-8,-6,2,7,7,-10,-8,2,3,2,-6,-6,-1,8,3,-1,8,-2,-1,-8,9,-9,-9,4,-2,3,5,10,-6,-1,2,-10,3,-3,-2,-3,10,-10,5,-9,2,-5,-1,4,-5,6,9,10,-7,8,-5,-2,3,2,-8,4,-4,7,-6,-5,-6,-10,9,10,-2,-7,9,2,3,-1,6,1,6,9,8,7,-7,2,-9,-1,-1,10,8,-4,-5,-4,-2,-2,4,2,-5,8,6,-7,-4,-7,-5,-7,-8,-5,-7,5,5,-6,9,1,-7,-8,-10,-7,1,3,1,-10,2,2,-6,9,-4,-10,-4,-9,-9,3,9,-8,-6,-8,-1,-5,-8,2,-2,7,5,9,8,10,4,-9,-5,-5,9,9,-6,3,-1,-7,-8,-9,2,4,-9,-7,10,-7,-4,8,-8,3,3,-7,5,-7,8,7,7,10,-6,6,3,-2,6,2,1,7,3,6,7,10,1,-7,-9,-2,-4,-4,4,5,8,-5,3,2,-7,4,4,-1,-3,3,5,-10,8,5,-8,3,8,-6,3,6,6,3,-4,-5,3,9,-5,-7,3,-4,-4,8,6,-10,-9,8,6,3,6,-7,6,-8,-6,-4,9,-9,-5,-5,-10,10,1,7,9,-9,10,3,3,6,6,-10,8,-8,-8,-3,-7,-10,-3,10,-8,5,5,3,9,1,9,-2,3,-9,-2,1,-7,10,9,2,-6,-3,-6,3,8,-1,-5,6,-3,-9,9,-4,3,8,3,7,-8,-2,-1,-10,-1,5,-3,4,-8,-1,-4,-7,9,7,7,1,8,-10,10,-5,-10,-7,-5,-9,5,-2,-2,-4,-6,1,8,-1,-7,3,-2,10,-3,4,-7,1,-2,-1,-3,5,9,-5,10,-1,-8,6,-7,1,-3,-7,10,4,-2,6,3,5,9,-9,5,-8,6,-2,-2,4,9,-8,9,1,-9,7,8,4,-9,8,4,-6,2,5,2,-1,-1,10,-1,1,7,3,-7,3,-1,9,-7,-8,-4,4,2,-7,-4,-3,7,8,10,-1,10,3,7,9,-9,-4,1,9,5,8,-2,-6,-3,-6,8,9,3,1,6,-3,-8,9,5,5,-5,-1,2,-9,4,9,3,9,-2,4,-10,-6,-4,-8,-5,10,3,-7,9,-9,1,4,-6,8,3,7,-10,2,7,4,-2,-2,-6,-10,-6,7,-9,-1,-3,-6,-2,-10,5,6,-1,-6,7,-9,-8,5,2,-3,-4,-7,-1,5,-5,6,8,-3,-4,-3,-8,3,1,-2,-1,-3,7,-4,-4,-4,4,8,5,1,2,-2,6,6,3,-2,3,9,-9,10,2,2,-7,-7,4,2,4,4,-9,-1,10,-7,1,5,-1,-3,1,10,-6,8,7,-5,6,-2,4,7,7,7,4,-9,-6,-9,-8,5,-7,5,5,-6,-3,-5,-4,-1,10,10,-9,-8,-9,-4,-7,-2,-1,10,-9,6,7,-7,8,1,-5,10,9,-2,9,5,4,10,-6,-1,9,7,1,-8,-1,6,1,1,-8,-8,9,-10,-3,-8,5,4,-7,1,-6,-8,9,4,-2,9,7,4,1,9,-8,-2,4,-8,-8,2,9,10,6,9,-8,7,-8,-3,8,-2,7,-9,4,6,8,8,8,7,-2,1,7,-5,-10,3,-10,-4,2,2,3,-10,5,-8,5,-8,-4,-7,6,5,2,-4,4,1,-1,4,2,5,-1,4,-10,1,1,6,-9,3,-10,6,-5,4,2,10,-9,3,9,5,10,-5,3,-8,4,-6,10,-10,10,1,-1,8,-5,1,-8,5,-2,9,-4,10,10,-2,-9,-5,8,3,-6,-1,-1,5,9,-9,2,6,7,-4,1,1,-10,-9,2,-10,-2,-9,5,4,6,5,-3,6,9,1,5,10,-8,-4,2,1,6,6,-6,5,4,-1,-3,9,6,1,-1,5,-1,-2,-6,6,-2,1,-3,-1,-8,-5,1,2,5,-7,6,6,4,2,-10,9,-1,4,-1,-4,-9,-10,3,8,-5,4,10,1,-9,-1,1,5,-4,-9,-3,-2,2,-5,-5,-4,-1,-4,-8,4,-5,-8,-6,-10,1,-3,-10,7,8,8,-8,-6,1,-9,-4,-8,-7,-7,1,-3,-7,-7,5,9,-7,-7,-9,3,2,9,-2,-6,3,-1,-1,7,3,4,-7,1,10,-8,-2,7,2,1,2,4,-9,10,-1,7,-10,-4,-4,10,7,-10,-10,5,2,-7,-1,10,7,-3,8,4,9,-4,5,6,3,-10,-5,-6,-1,1,-3,4,-2,8,-7,7,-2,-10,4,-10,-1,1,-5,3,7,8,5,-10,10,-7,10,-2,5,-1,7,-8,-2,-2,-4,-3,-1,1,-4,4,-8,-1,-5,3,5,10,7,-8,-5,-8,-7,9,3,-5,2,-10,-10,-1,4,-6,-9,-10,-4,-7,-1,9,-7,8,-10,-6,-10,-5,9,-5,1,1,10,8,10,-5,2,10,2,-1,1,-7,6,-3,-9,8,-2,9,10,7,7,-10,-4,10,10,-10,-9,-6,-10,-1,-9,-6,8,4,7,8,3,-4,-10,-7,-8,-5,-6,3,10,-3,-3,-4,8,-6,1,-10,-2,5,1,-6,9,-5,2,10,-3,3,-4,4,-4,9,-6,2,-3,4,9,10,-9,4,6,3,9,-5,2,-4,-4,4,2,-8,2,-7,-1,-10,6,2,-10,-1,-3,-1,-8,1,-10,1,-10,-6,-2,5,2,2,1,-9,-8,-7,1,-6,-5,-2,-4,6,2,8,5,-7,-1,6,-2,-3,7,3,-10,-8,8,1,-1,-7,8,-8,1,1,-4,-5,2,-9,8,9,-3,-2,-7,2,-1,-2,4,-4,-5,8,2,6,-1,-4,-8,-6,2,-1,-2,-6,2,2,5,-3,-10,10,6,7,2,4,-6,3,10,-6,7,-3,-9,-4,-8,-5,-10,2,2,1,1,-7,8,7,-4,-8,5,1,-6,-8,-2,5,-9,-5,-6,-6,4,4,-3,-1,3,9,1,-2,5,-5,5,8,-9,-9,-1,-10,8,10,2,-8,9,3,-9,10,6,-10,5,7,3,7,-10,-1,-10,10,10,-8,-9,-2,-7,2,-8,-6,-2,-7,10,-1,4,9,-2,-7,-8,3,10,-6,8,2,-4,-8,-3,3,10,4,-5,9,3,-2,-3,-10,2,1,8,3,4,-10,8,-8,7,-4,4,-2,9,2,10,-6,10,2,3,-9,9,-1,3,5,3,4,3,6,1,6,10,4,1,7,1,2,3,7,5,6,3,7,6,-10,1,-8,9,-10,-10,-8,-3,1,6,-4,1,-8,9,-4,9,2,1,-1,-6,3,-10,-6,-3,-10,6,9,3,-6,5,9,-4,-3,5,-5,7,-4,3,9,-9,-3,3,4,9,10,10,7,-2,-8,8,-5,-5,3,9,2,-3,4,-6,3,8,1,-3,-9,3,-10,-3,6,-6,-6,3,4,2,1,4,-5,-9,10,7,7,-9,10,3,-1,-5,5,-4,3,5,-6,-9,-1,9,10,-3,7,7,-5,3,1,-3,-7,3,5,-3,-7,1,-3,-1,10,4,-5,5,1,-6,-8,-9,5,5,10,-10,4,-6,4,2,3,-1,4,8,6,10,-10,10,-10,7,5,-6,-9,-6,2,-8,1,-3,7,-4,5,8,-10,-3,3,10,-5,7,-1,-8,-2,-7,-6,-9,4,-6,7,4,-4,10,5,5,6,-6,8,1,-2,2,1,-3,-5,3,4,-1,-2,-6,-1,-9,-7,-6,-8,-5,-5,10,-8,-10,1,7,1,-6,9,2,-2,-6,5,-4,-7,5,5,8,8,8,-5,7,-3,9,-4,1,-1,5,-9,8,7,7,-9,-5,7,6,-8,-8,-5,-4,-9,7,2,-7,-2,-6,-10,-2,2,-4,1,-10,5,2,6,-1,3,-4,-9,-5,-6,9,-7,-5,-8,-7,10,-10,7,7,9,6,-5,8,-3,-4,-5,-7,7,1,-10,6,8,-7,9,-8,-3,10,-7,3,-1,-1,1,1,9,-3,2,10,-5,-7,-2,-3,-1,2,-1,-10,-3,1,8,-2,-7,7,-6,1,6,6,-3,5,-1,-4,4,-7,4,9,-1,10,-9,7,-3,-7,-6,-9,1,5,-10,4,-2,9,8,-7,-2,-9,3,6,-6,-5,7,5,7,-10,10,1,5,-7,9,-6,-10,-3,2,-9,4,5,9,9,-10,2,-3,2,-4,-4,3,-5,-4,-4,-8,9,8,-3,-1,-10,1,3,-7,-3,3,4,-7,9,-5,-10,-7,-5,10,-9,-10,6,-4,-5,-5,2,8,-4,-4,6,7,4,-4,8,-5,-9,-9,-6,5,4,2,7,-9,-2,-7,4,-4,-9,-5,6,-5,7,-9,7,-4,3,-4,-3,5,-7,6,6,8,-10,-2,7,1,-3,4,-4,10,6,10,-8,7,-7,7,-2,-9,-1,9,10,9,10,-3,6,2,9,1,6,5,10,-9,10,-9,10,-9,7,4,-3,-2,2,1,5,-1,10,6,-7,-6,-4,-7,2,5,-4,-7,-9,6,-4,-3,8,1,9,10,4,-4,-1,-3,7,-2,-10,-7,-7,-8,-1,1,-6,-7,-2,2,3,6,-7,4,-8,6,-5,-5,-8,-5,-8,8,1,-1,-2,-10,-9,8,-5,9,-1,1,9,-2,1,-8,6,-4,-1,9,-6,-10,-5,-10,-5,4,-5,3,3,3,-3,-4,6,7,3,-3,-4,3,-3,10,5,3,-10,-5,2,-8,8,-7,2,-2,-9,-3,1,-4,10,-2,9,6,-4,2,-7,-4,-4,9,-2,-10,-9,-5,10,5,-3,-6,6,2,1,7,-6,-4,1,-8,-8,5,-3,8,-10,-5,1,5,-1,9,-5,-1,7,-3,1,-3,-2,-8,1,-8,10,5,-3,1,9,8,-6,5,6,-4,-1,-8,7,8,4,8,9,7,4,-10,8,7,6,-7,-1,-1,-10,-5,-5,-3,-9,2,4,2,7,-3,9,-9,1,9,-9,-4,9,5,2,-10,-1,-1,-2,-5,6,-4,-5,1,-10,-9,9,9,-5,-2,2,-8,-6,10,-1,-9,-10,-1,5,-4,-10,-6,-8,-9,-7,10,4,-4,4,-10,-8,1,9,6,3,3,-5,-4,-3,-8,5,4,3,-2,2,3,9,10,5,6,-6,-3,7,5,-2,4,8,-9,-6,1,2,-9,-7,1,-3,-2,-5,9,4,-5,7,-6,-9,-8,-5,-4,5,8,-10,-6,5,1,4,-1,4,-5,-5,-5,-5,9,4,-6,7,-10,2,-10,-5,6,-3,-10,-5,5,5,4,5,-9,-9,7,-1,-4,5,10,7,1,-5,4,-5,9,2,-9,1,5,5,5,-1,10,3,5,-8,-9,-9,-2,-3,-4,6,-2,-5,6,-3,7,2,-9,9,-4,-2,9,-5,6,4,4,5,-7,-5,2,4,1,1,10,3,7,8,-7,-9,-2,2,2,-4,-2,10,8,-7,1,-8,-6,-4,8,-10,-6,9,1,5,-1,-4,9,-8,9,3,-1,-10,4,1,7,-9,10,2,1,9,-6,4,-7,2,8,-6,8,8,-2,-8,-10,-2,6,6,-1,7,7,5,-8,10,4,-6,3,-6,3,-4,10,-7,-9,-2,-7,-2,-4,8,5,7,7,-2,7,5,-2,5,6,6,5,8,9,-6,-6,-5,6,10,5,-4,-10,4,-10,1,3,1,-9,9,8,1,4,5,-7,-3,-7,-7,-6,6,-2,-1,-8,2,-1,5,8,3,3,-2,-3,5,2,6,4,5,10,-10,8,8,-5,-1,1,7,-4,-6,-5,-6,4,-6,-5,-4,-7,-5,-8,-6,-4,-6,-1,-8,-3,1,-5,3,-10,-10,10,-7,-10,-1,5,-1,-4,-5,9,7,10,-10,-6,6,3,-8,2,9,-10,-2,8,4,-2,5,4,5,-2,9,-7,-2,3,-3,-7,-6,-3,-2,4,2,-6,-9,-1,-4,-7,-8,10,-5,2,-5,-10,-6,3,-3,5,-3,4,-3,6,5,10,8,-5,-2,-2,-8,10,-7,-3,2,-8,10,8,-5,1,-8,5,-1,-10,1,-10,6,2,-4,4,2,-10,-1,6,-3,-8,-5,6,7,-9,-7,5,8,7,-2,-8,2,-7,-6,-9,-7,9,-1,-10,-10,7,7,-1,9,6,10,6,-4,4,-5,1,1,-5,-5,-1,3,4,-9,-6,-4,10,8,3,10,-2,-10,6,-2,-4,-8,-2,2,-3,-3,-1,-1,1,8,1,-1,2,5,7,-1,-4,7,-1,4,-1,-3,3,5,5,-8,-3,9,-4,-7,2,1,6,6,6,1,8,-2,-8,-7,-2,9,-7,3,3,-2,8,4,3,3,-9,-9,-10,8,-7,3,9,5,10,-7,9,-9,7,3,3,-9,2,-9,-8,10,-1,5,5,-8,-9,8,-8,-5,2,5,3,8,-2,8,6,-7,3,9,-3,2,3,10,-9,-6,-2,-8,5,-10,3,-10,8,-5,9,-8,2,4,10,-9,-8,9,8,-5,-3,9,-5,-6,6,3,-7,10,8,9,10,6,4,8,-5,4,-5,6,2,2,-3,-5,-5,2,-1,-3,10,8,5,6,6,7,-3,-3,5,4,2,10,8,-3,4,9,5,6,3,1,-1,3,3,10,-3,8,8,3,2,5,3,-10,3,-10,9,8,-2,-6,6,3,-10,5,2,4,-5,10,2,6,-7,2,8,5,-10,4,-7,-5,9,7,-9,5,-7,-10,6,-4,10,8,5,-7,6,-1,8,2,-8,-9,7,9,-1,-4,-2,-10,6,2,1,4,-9,-10,1,-6,-10,-3,1,2,-10,-8,7,-5,-4,-4,-6,-4,-5,2,8,-6,3,7,1,5,-8,-4,-9,-9,7,1,6,-8,10,7,-10,-8,4,8,-5,-9,-5,9,3,10,5,-5,5,-10,-7,-4,-1,1,-8,-1,1,-5,2,-2,-5,-8,2,-9,-1,3,-7,-7,9,-4,-7,9,6,6,-1,-6,1,-5,9,1,3,10,-2,10,4,-10,10,1,-5,-5,-5,3,5,10,-1,6,4,-8,2,8,2,7,5,-8,-4,9,4,-7,9,4,8,-8,5,-7,-1,-3,10,7,-7,-8,-9,-2,8,-3,9,-8,7,-7,1,-1,8,-5,3,6,6,1,-2,8,6,-8,9,2,-2,-10,3,-5,-7,-1,-4,-8,-2,8,6,3,-7,7,-7,-4,7,1,-7,-3,7,-3,-1,-3,-2,7,5,1,1,8,6,6,-5,-5,1,7,4,-1,2,9,3,3,-6,-1,-4,-6,2,6,-8,2,-1,-9,8,1,4,-4,-6,6,-3,10,6,8,7,-5,-6,-6,5,-3,7,-3,-6,9,-5,-3,-10,6,8,-5,-9,-1,9,-4,-5,7,5,-5,8,10,-9,-4,3,-8,-7,7,3,-2,7,7,5,8,-6,10,8,-7,-2,-7,-2,-7,6,-4,-3,-5,2,-4,8,8,6,-7,-5,-3,-7,1,5,-10,-3,-4,-1,-7,-9,-2,5,-10,-8,-7,-3,-10,-1,4,1,7,-8,-10,-7,4,10,-6,7,-7,-5,8,5,10,10,-1,8,7,-8,7,-6,5,8,-2,-7,10,5,10,5,-5,-4,8,-6,-7,3,-2,-4,4,8,9,-7,5,-6,-2,-7,-9,-5,2,-3,-8,1,-5,8,-9,7,2,-6,6,4,-4,-6,1,-10,-5,-1,9,-4,7,4,-8,3,-5,-7,-10,8,3,6,5,6,-1,4,9,4,10,3,9,10,-6,4,9,1,-7,-5,-5,4,-7,5,6,3,9,6,1,-5,-4,-2,-2,4,-10,-2,9,2,-2,-2,-8,6,1,9,-9,-1,-3,5,-8,5,-5,4,10,-10,2,-3,-4,-2,-5,9,5,-7,2,4,-1,7,-3,-10,6,-9,9,-1,-3,10,-3,-1,6,7,-10,-8,-9,6,6,6,5,2,-7,1,-7,-9,-9,-1,8,6,8,-10,-9,-8,4,8,-9,-5,3,-8,8,-1,8,5,9,-6,5,3,-2,-10,-2,8,-9,8,1,-10,-3,-10,-4,-9,-4,1,10,-5,4,-1,-4,-10,3,2,-5,-5,-7,1,9,6,4,-5,1,1,5,-4,2,-1,9,9,8,-4,10,-8,-5,10,-4,-6,-5,2,10,7,7,6,-3,-2,2,8,1,-9,-10,6,6,-9,-10,8,-7,1,-5,10,6,9,-7,-8,-2,-3,-7,-6,-10,1,6,-9,6,-4,10,1,5,-2,6,1,8,-8,-2,6,-9,-3,8,-9,5,-9,9,-1,-9,-9,4,1,-3,-4,5,-10,-1,-3,-8,-5,-6,-7,4,1,10,6,-9,3,10,-8,1,3,-2,1,7,-2,2,-7,-7,10,8,9,-5,-1,4,-1,-9,7,1,1,5,2,-3,6,9,7,-9,7,9,-10,9,-7,8,-2,-3,-6,8,-8,8,3,7,7,6,-2,1,-9,-5,-3,-10,1,-9,2,6,-2,-1,4,-7,-7,-2,-10,-3,7,3,3,4,9,-3,-3,-10,-5,-10,-10,-7,-7,-6,-6,-6,-8,-3,-4,-5,10,-1,-8,6,3,-2,2,-10,2,6,4,1,10,-5,2,-9,-9,-5,-3,-10,-8,7,-4,9,-2,4,-8,2,-10,4,6,-2,6,-1,10,-3,-8,8,-9,7,-3,-9,-5,-1,-7,-7,-10,7,-8,-5,4,9,-10,3,6,-1,3,2,-3,3,9,5,8,-7,4,7,10,9,10,9,4,-5,-4,-4,-1,8,-8,-1,-7,-5,2,9,5,-4,-2,3,5,-2,6,-7,-5,-6,10,-1,6,9,7,10,8,9,8,-7,-1,-1,4,-3,-5,-4,-6,3,1,2,2,10,-7,-1,2,-6,-6,1,7,1,-2,-8,-9,2,4,10,5,7,10,7,-5,-6,-1,1,10,1,-8,-10,-3,9,-6,5,-8,3,2,1,-2,8,-3,-3,-2,4,-7,-7,7,-8,-4,4,9,1,9,9,-10,-7,8,7,-8,2,-5,6,4,5,-10,9,8,9,3,-1,6,7,1,8,4,7,-8,1,10,9,7,-9,9,4,-7,4,-4,1,-6,7,8,7,-8,7,6,-7,-3,8,6,3,-7,-9,9,-6,-9],[-5,8,3,2,-5,-6,-1,-1,-1,9,10,-3,6,-9,9,9,6,-5,5,-1,-8,-5,5,8,-2,-10,-2,1,6,-2,9,8,9,4,-5,-6,-1,-1,-8,-2,5,-3,6,-5,-6,-9,10,-8,-1,5,-7,-8,-4,5,-8,-2,-1,-8,-1,-1,-1,1,8,-10,-4,-6,6,9,2,1,1,3,-10,-10,5,9,-4,9,2,2,4,6,1,-1,-9,5,8,1,10,-1,5,-4,10,10,3,-7,9,9,7,4,-4,6,-8,10,-10,-6,-10,-3,-2,-2,4,-3,3,4,-6,7,-9,10,2,7,10,9,4,10,-5,-2,-4,-4,1,-8,-6,4,10,3,5,-3,3,-5,-4,-4,9,-9,-3,3,-1,-10,8,2,-10,-9,5,2,-4,5,-3,-8,-5,9,-4,-3,-3,-1,6,6,-8,-3,-7,-1,3,10,6,-2,8,10,-2,-6,5,6,1,-7,7,10,-6,-6,8,7,-5,-5,-10,3,-10,-7,-6,-6,4,-6,5,6,8,2,-7,9,10,5,9,-4,-6,-3,3,-9,-5,10,2,3,6,-7,-8,5,2,-10,7,-1,-2,-5,-4,-3,-1,8,9,-5,-7,-7,1,-3,-1,4,-4,1,9,-4,-10,9,10,-7,9,5,8,-10,-6,-2,5,-5,10,8,3,2,9,-7,9,9,7,5,-5,-4,10,-10,-1,6,2,-3,-8,-8,-6,-7,8,6,-9,3,-6,9,-3,10,3,-7,2,9,5,-6,-2,-10,8,-10,-5,-4,-7,6,1,4,-4,10,9,5,-7,-6,5,-1,-2,-1,-1,-7,-10,-10,8,7,-5,9,4,-9,-6,-10,-1,-3,2,-9,3,-5,10,5,1,2,-7,-1,5,-2,7,2,-4,10,-1,3,6,8,-5,-5,-3,2,8,-10,3,3,-7,7,-2,-1,7,-8,2,-10,6,-3,4,10,-9,4,4,4,-6,5,10,-10,8,4,3,8,9,10,-7,5,1,-1,-1,-8,-6,5,-9,-6,5,8,4,-1,9,8,2,-5,-5,1,9,-2,-2,-2,-2,-7,-8,6,5,7,-9,-2,-8,-5,1,-8,-5,7,7,-8,10,7,4,-2,-1,1,-3,2,-9,-4,-4,1,3,9,-9,-1,2,-1,-3,5,3,5,-10,9,7,10,-6,-3,10,10,-8,-2,-9,9,5,8,-10,8,-2,-9,-10,2,-9,6,-6,-1,-7,5,6,-10,5,-3,-10,7,5,3,-3,1,10,3,4,-10,-9,-7,-6,5,4,10,-8,8,-1,9,7,-7,-7,-5,-6,-2,-8,9,-7,-9,4,-6,4,-6,-6,10,6,2,-10,6,2,3,8,-5,-8,-5,4,5,-7,3,-7,-9,-10,8,-10,8,-4,-1,2,-7,-2,3,4,-2,-2,-4,-9,1,6,1,-6,9,9,2,7,2,-2,5,-4,8,-3,-4,-9,-4,-6,10,-4,-2,8,4,3,-7,10,2,-1,9,-7,8,10,1,-9,-8,2,7,3,-7,7,1,6,-3,-8,-2,-7,-10,-2,-5,-2,3,-4,-3,-4,-5,-6,10,2,10,-10,-6,1,-6,-7,-6,-5,-4,-1,-7,-9,6,9,-7,3,-4,10,-10,7,5,-10,-4,10,-5,5,6,4,-9,-9,-7,-4,5,-10,6,-2,1,2,6,-3,2,5,-10,-9,-4,-5,-9,4,6,9,-1,-3,-5,-10,-8,4,-9,-10,-7,-9,-7,4,5,2,-1,-3,3,7,-2,1,-7,4,3,6,2,1,-2,-5,-2,-10,7,-3,1,10,-8,7,-7,3,2,-2,-7,-4,-9,-7,8,-1,-1,7,6,-7,-2,10,-5,9,-4,-2,5,1,-6,2,6,-9,8,10,5,10,4,-7,3,-4,9,10,-3,8,9,-3,3,-3,8,-7,-3,-2,-7,3,7,8,5,-9,-1,8,-7,5,1,-3,1,5,6,-10,6,-4,-9,10,2,-2,6,-3,1,3,7,-4,-5,-4,-6,-8,6,-7,8,-2,-7,-3,4,-8,-7,-8,8,-5,-1,-7,-3,-9,-9,-7,2,-7,-4,5,-8,7,-5,-10,-7,9,-5,-4,1,1,-8,7,8,2,-6,-3,2,-10,5,2,-8,-1,-7,-3,-8,10,-5,-9,-3,-8,-8,3,-9,6,6,5,1,7,8,-8,-6,-4,7,5,-2,7,2,-9,5,-4,-5,3,4,4,9,8,-10,6,6,9,4,8,-8,-6,4,3,8,3,-5,-4,9,-4,6,10,3,8,5,-1,6,-7,-9,10,-6,7,-2,-8,5,-1,1,-1,-1,2,-6,1,2,2,8,-7,5,-6,7,7,7,10,-9,2,1,-6,-7,-9,-4,-10,-3,7,-3,6,-6,-1,-10,2,-2,-9,-8,-10,-3,6,1,2,-5,3,-1,-7,9,1,-8,1,7,5,-9,2,5,9,-6,-10,-9,10,-10,-6,-6,2,-10,-6,-5,2,-7,5,-4,9,-7,-2,4,6,-8,4,-1,-8,1,8,6,-9,-4,-6,-9,10,-6,2,-2,-3,-1,2,5,-3,-3,-2,2,-3,-6,-7,-4,10,-7,1,1,2,2,5,6,-4,10,-10,-9,-9,2,1,2,7,4,-1,-1,-8,-6,10,1,-3,-4,-1,5,-8,-5,2,-10,9,8,-10,2,2,3,2,-10,4,7,4,7,-9,-3,-4,-2,9,-2,9,-9,1,-4,7,-9,5,8,8,-5,2,9,-3,6,1,2,-1,10,4,-7,8,-2,2,4,5,-6,-9,2,6,-1,5,4,6,-10,-7,-9,-2,8,1,3,-3,-3,-4,2,3,6,9,-4,5,3,-2,7,-5,8,-8,2,-2,6,1,5,-3,2,10,-5,1,-6,-2,6,1,5,-7,-3,-3,-6,-6,10,3,-9,9,7,-4,4,-10,-5,-8,-10,-7,-5,-1,7,-3,5,9,8,-8,10,2,7,-8,-10,-1,1,-3,-10,-7,-2,-4,-6,-8,2,1,-9,-10,4,-7,2,7,9,10,-6,6,9,4,-6,-2,-10,4,6,6,-10,6,-2,-7,-7,-10,-6,-1,-10,-2,7,7,-7,-9,-3,-4,-7,-6,5,1,2,7,10,5,-2,8,-9,1,4,-10,2,-1,-4,7,2,-5,1,-2,-9,3,-2,-3,4,8,3,-4,-3,3,3,9,9,-10,6,-9,7,-8,-3,-3,-6,-6,10,-3,6,-10,-5,-4,5,-3,6,-5,6,-5,4,-7,-8,9,-4,2,-8,8,-3,8,-8,8,6,8,-7,-2,-10,3,-3,-7,7,-6,-2,-8,9,-1,-8,-1,-4,-8,-4,4,-1,-4,-1,1,2,3,-2,-7,7,-7,10,-1,1,-5,-10,-8,8,-5,-5,-9,4,1,2,-8,-9,-6,-5,1,-4,10,7,-5,2,-8,-6,3,8,7,-3,1,-8,-9,1,8,8,1,5,-2,6,3,-6,4,-2,6,-4,7,1,6,8,9,-1,1,6,3,3,4,6,-3,-6,6,-3,5,-9,-8,-6,-2,9,5,9,5,-5,1,-6,-2,5,-6,10,-4,2,-7,1,7,5,5,-9,-7,-1,8,5,4,7,-10,-1,6,-8,-4,-4,-1,3,2,6,10,10,-7,-9,6,-10,3,-3,-7,-3,4,-3,6,-8,-10,10,4,-8,-4,1,-3,6,-4,-6,-2,1,-4,-10,2,9,-4,2,8,10,-8,-1,4,6,8,9,1,-7,-6,-3,5,-10,2,9,-3,1,-10,2,-10,1,2,-10,-2,6,-4,-6,-3,-9,8,5,5,-1,-8,8,-3,8,9,-6,6,8,-3,10,1,-2,-7,8,-3,-8,4,-9,-5,2,-6,6,2,-4,8,-2,-3,-8,3,2,-7,-9,6,-7,6,6,10,5,-6,7,-3,5,-5,-4,-8,-8,-7,-7,-4,6,6,3,-2,7,7,1,5,6,8,-10,-8,-3,-5,10,7,-1,-5,-10,-3,4,1,2,3,7,7,10,-8,-10,3,2,3,-6,8,-7,3,2,9,1,1,-5,-5,-4,6,-4,4,-3,-9,-9,-5,7,8,-1,3,-10,7,-1,-8,7,-8,7,9,3,8,-5,6,10,-9,-2,-10,5,8,4,-2,2,-2,-4,-10,6,-6,-3,-3,8,-2,4,-3,-3,-8,8,6,2,10,6,2,10,-5,2,-5,-9,1,1,6,-4,1,-6,2,4,3,-4,5,3,-6,-7,-5,8,-2,9,-2,-4,-5,-9,-8,10,4,6,-7,-9,-6,-4,3,-9,2,4,-1,7,1,-4,9,-8,-10,-2,5,-2,6,-6,-9,-5,-10,-4,-9,8,9,9,-8,2,-3,-6,6,3,-5,2,-1,6,-9,-6,-3,10,-6,9,8,-3,6,3,-7,-5,-5,-8,-7,10,7,6,-10,-2,-5,-2,4,6,-3,3,3,-4,-6,-5,-7,1,-2,-5,-1,-9,-2,9,-8,-6,-4,-3,-9,-7,9,10,-8,-1,-7,-3,7,-5,4,-3,-1,-5,1,5,-5,7,-4,-10,-7,5,1,-2,-1,-5,5,9,-10,2,-2,-1,9,9,-4,-8,-3,-5,-2,-1,6,-9,-8,6,3,-9,-4,2,-6,-9,-3,3,1,-8,-7,-7,9,-5,-4,-4,10,4,6,9,8,-4,6,-6,-5,9,5,6,-2,2,-1,-5,-2,9,6,9,8,6,1,1,8,8,8,9,5,7,8,9,2,7,9,-5,-9,1,5,-6,3,-8,5,2,9,-8,-1,6,-6,-5,-10,2,-3,9,-4,-3,-8,10,8,-5,-9,-3,-9,-8,-3,2,3,-5,8,4,-1,-10,8,2,10,-3,10,3,-7,8,4,-5,5,-3,6,-4,-6,3,4,10,-7,-7,10,-8,-1,-7,8,9,-2,6,-2,4,-7,-4,4,-7,8,10,3,3,6,-6,3,-10,10,2,8,-3,-3,-6,-10,10,6,-4,-9,1,-8,-2,4,8,1,9,-6,-6,9,9,-4,7,-10,9,9,-3,-6,-10,8,-6,9,-10,-8,-5,-8,-4,5,4,-2,3,2,-2,4,1,-1,-2,-2,5,-7,-5,-9,9,2,-9,6,-8,9,-9,2,-6,-4,-3,-9,6,-1,4,4,3,-9,-10,4,5,8,8,-1,2,1,6,4,-9,-5,-4,-6,-2,-9,10,-2,9,-9,9,9,9,-9,-3,7,9,-5,-8,9,-8,4,-2,-2,-8,7,-3,1,8,7,4,-3,3,-5,1,-4,-4,6,7,-6,1,4,-2,7,4,1,-7,10,-4,-4,-9,-1,-9,9,-5,2,-10,1,9,2,-4,-3,9,1,-6,-8,3,8,-8,-7,3,10,-4,-5,-1,-8,2,-5,5,-6,-1,8,8,6,-2,-1,-4,10,4,-3,-4,1,4,-9,-2,-2,1,-8,5,-5,9,-3,8,1,1,-8,-4,-1,7,-9,-2,3,-10,-2,-7,3,-4,-8,-2,-2,-2,-7,1,9,5,6,-9,-3,-10,-6,-4,4,7,-8,-1,-3,-3,3,8,2,10,-3,7,-7,-2,5,-2,-4,10,-10,-4,-8,-5,3,-3,-9,4,-1,9,-1,1,-7,-4,-3,-4,-7,-8,-5,6,-8,-4,-1,10,-3,-9,2,-10,-2,1,-3,10,1,-7,-3,-6,-3,10,3,5,1,-10,-4,1,7,3,6,1,3,4,10,-7,-4,-6,-8,-3,-7,-1,3,10,5,1,-9,9,-8,-6,-4,-3,1,-5,2,-8,-9,1,3,4,-5,1,5,5,-2,-4,-3,7,6,-3,-10,-7,-1,2,2,-6,-9,10,-5,-7,-6,-5,8,5,4,10,10,-4,8,9,-2,-6,9,6,2,3,6,1,10,6,5,-9,-7,-7,2,4,10,6,-9,5,8,1,8,8,7,3,3,-6,8,5,1,4,1,-5,4,2,-10,8,3,5,1,10,1,-4,3,-8,9,8,-4,10,2,2,3,9,5,5,-1,1,3,10,-5,10,2,5,10,-4,5,4,3,3,-7,-5,5,10,-1,4,1,-1,-6,9,-10,-10,-8,-3,10,-10,-6,5,2,9,-8,-1,-1,-3,9,-2,-4,5,7,-2,6,3,-8,-3,-6,4,-7,4,-7,2,-9,-6,7,5,-1,-2,-1,-1,5,-9,-8,6,8,-1,9,1,-10,-2,-10,10,4,-10,-6,1,-5,-4,-3,-8,2,-8,-7,-10,-7,1,-9,-9,-10,5,-10,-9,9,9,4,5,-1,9,-1,2,-1,-5,5,-3,-3,-2,7,9,5,-7,7,4,-2,-5,-4,-1,3,7,-10,-2,-9,5,6,-9,3,-7,-10,10,6,5,4,6,1,-5,2,-3,2,6,-3,-6,-2,7,-7,-4,-4,-4,-8,-8,-4,10,-10,8,3,9,-10,2,-1,-4,8,3,10,2,8,6,5,-7,-1,7,6,9,3,7,-2,2,2,4,3,-9,8,-10,-3,7,9,-7,-10,-10,-8,6,-2,2,4,-6,-1,-5,-4,1,-1,1,-2,4,5,-4,-4,4,1,-10,1,-1,4,-1,-2,-6,-9,-2,7,3,-1,-6,-9,1,-8,4,-8,2,-2,8,5,4,3,7,1,4,8,9,2,-7,10,10,10,-9,6,4,-3,7,6,8,3,1,1,9,1,-4,9,10,5,-10,9,2,6,-2,5,-2,-1,8,-5,5,-2,7,-2,-1,-6,-10,8,-9,-3,-7,-10,-7,-1,4,1,-2,-10,-6,-5,1,-9,10,-5,4,-9,-6,-1,1,7,10,7,-3,-10,-1,-6,-10,-5,6,9,-10,10,-7,-1,5,-6,-8,-6,1,-1,-2,-9,4,1,6,10,8,1,3,6,2,2,4,-2,-3,-9,2,5,2,7,-8,3,7,1,-10,7,-8,1,-8,-9,7,-5,-6,6,8,7,10,-2,-7,-8,-2,6,-5,-4,-3,-3,-10,1,1,-5,9,-5,-3,-6,1,-5,9,5,-2,9,1,-6,-2,-9,4,-2,-8,-4,5,3,-3,1,2,8,-4,-9,-10,-5,4,3,-10,3,-3,10,6,-8,-2,5,-4,9,-1,-2,-5,-1,-3,-9,3,-4,8,6,7,-6,-4,6,3,7,-6,-7,8,-2,-4,7,-2,4,4,5,-6,4,-2,-10,-8,3,4,4,7,4,-8,1,-9,-1,6,6,-9,-4,1,-7,8,10,9,-5,-4,8,-9,2,-3,-3,-3,3,-9,2,-8,8,1,10,-6,6,6,-1,-4,-5,8,-8,-10,2,7,-1,6,-2,1,-9,-7,-6,3,-7,2,6,3,10,4,-3,7,7,-5,-10,-9,1,6,-10,-7,-5,-1,9,-4,7,1,10,-4,-1,4,-5,-10,10,6,-4,6,-1,10,-3,9,2,-10,9,-9,-2,4,9,-6,2,8,-4,-5,5,7,10,8,7,6,1,-8,10,2,8,8,-9,-5,-3,10,-8,6,4,-9,1,8,-1,-8,-10,2,-10,7,-9,4,7,-9,-10,10,-10,-6,-6,-4,-3,-10,3,-3,2,-2,-4,-2,10,-5,-10,-6,-6,1,7,9,-6,-4,-2,-9,9,-7,8,4,-3,-8,-6,3,-7,3,8,5,-2,-2,-8,-1,4,9,-5,8,6,3,10,-1,8,10,-6,1,-8,2,-6,2,-1,2,8,6,-5,3,2,-2,-9,-8,9,-3,-10,2,10,-6,7,-6,7,8,-10,-7,6,-3,-4,-2,-10,-10,1,-8,8,-3,1,1,-3,10,-1,-6,-8,3,-1,5,-9,-4,10,5,-6,-4,-10,-5,-5,6,3,4,2,1,4,7,-4,-6,-4,2,-1,-9,3,-4,10,-4,-4,2,8,1,3,5,-10,-2,4,-4,-2,8,6,2,3,-7,-6,3,4,6,-2,5,-4,6,-10,-6,1,8,5,-3,7,5,9,-9,-4,10,-8,9,1,1,-6,-6,1,6,5,4,9,7,-1,-3,-1,-2,10,-10,-7,-4,8,-9,5,4,-5,6,-10,-4,-1,-8,9,-1,3,10,4,4,6,-2,-9,5,-5,-9,-3,-7,-9,-9,5,9,-3,8,5,-1,5,3,10,-9,-8,1,3,-8,-3,3,8,3,-3,1,3,10,-7,-4,-1,-3,5,-2,4,-1,6,-4,-5,8,-10,-5,-2,2,10,-8,1,9,7,-4,-1,7,-6,2,8,1,-8,2,3,-3,10,-3,-5,8,-4,-3,7,10,3,-7,3,-10,4,5,5,-10,9,7,6,6,-10,-2,-10,-2,-6,3,-7,-4,-4,10,-5,6,4,8,3,-9,-4,9,3,9,10,-3,-7,-10,6,-2,-10,4,4,-5,7,-9,5,5,1,9,5,10,9,-3,-10,5,-3,-4,-3,5,3,9,2,-5,-7,6,-8,-4,-6,3,1,-6,9,5,-10,-1,2,10,5,1,-10,4,3,7,6,-7,-8,-3,-6,-8,-9,-1,1,7,7,-8,4,6,-1,-9,3,-5,-1,-7,-7,5,-5,6,-8,-2,10,-3,-3,2,-4,-2,-8,-9,5,8,-2,-9,9,-1,-8,-9,4,-3,-1,-2,5,-1,2,4,7,-1,-4,3,6,8,10,2,-1,10,9,6,-7,7,-8,-9,4,3,-10,1,4,-8,9,6,-5,4,10,8,-9,-9,7,-2,-7,6,1,3,-9,8,3,9,-10,-3,-5,8,-5,10,6,-2,-7,2,8,-3,-8,-6,-7,-10,2,-9,-4,8,5,-1,10,-4,4,4,1,10,10,-2,-2,4,-6,8,10,-9,-6,4,6,2,3,-1,-3,6,6,10,10,4,7,-6,-10,1,-7,-1,-4,2,-6,6,1,-3,-9,7,-7,5,-2,10,-8,-9,8,8,10,-3,-3,8,-8,3,3,7,2,3,-3,-8,-6,5,-7,-9,-3,5,-9,1,3,-7,5,-8,5,1,-6,10,5,9,-10,-1,1,2,9,9,7,-2,-1,-7,4,6,-6,4,-4,5,9,1,-2,-10,-6,6,-7,4,-9,-4,-1,-2,9,-8,9,8,-9,-10,4,3,2,-1,-8,-9,-10,-1,-5,7,1,6,-9,9,-5,-3,2,-9,5,-3,7,-3,5,7,7,4,9,7,6,8,-7,-10,-6,1,-9,8,8,-4,-3,5,-4,5,8,-3,-8,-6,3,1,-7,5,-9,-5,-4,2,-1,-7,-5,-10,6,9,-6,10,5,1,6,-9,8,-5,-2,-2,-3,7,5,3,1,-7,1,8,-9,-7,4,-3,9,-7,-5,1,9,-6,-5,6,-2,-5,-10,-10,-2,7,2,-10,-8,-1,5,-10,10,-9,-6,-3,5,3,10,6,10,-10,3,-3,-7,5,4,8,-1,3,9,-6,-5,-2,2,-9,-1,-3,8,-7,-10,-9,-8,-2,-2,-6,10,-5,-3,-2,-7,5,9,-2,8,2,-2,4,-5,-8,-9,8,-6,-6,2,-2,-8,-6,-9,-6,10,4,-8,-1,-3,2,3,5,6,8,9,8,-9,4,5,-4,9,-8,-6,-2,9,-3,7,-2,9,-1,-10,-6,3,8,2,-4,9,8,2,4,-5,2,7,2,-1,-4,2,-9,-10,7,-8,2,5,-5,-1,6,8,-7,3,-8,-4,5,-2,3,3,5,2,-1,9,-4,6,6,10,-8,-5,-7,-9,-5,1,5,9,-7,9,-8,5,9,-1,-3,8,-4,-8,-2,-3,1,6,-8,-6,-7,-5,1,6,9,-7,-10,6,10,3,4,-8,2,1,-8,-4,-9,-10,9,4,-5,4,6,9,7,-7,-10,6,-10,3,-3,4,8,-6,-2,-6,-9,-4,10,10,-7,-8,3,-10,-10,-10,-2,7,-8,6,1,-9,-4,-5,8,2,4,4,-6,10,-7,-1,5,-10,8,5,10,2,-8,-8,4,-2,2,8,10,5,10,-10,-3,2,-6,3,-2,10,1,6,10,6,6,1,1,7,4,-10,6,10,-8,10,7,-10,7,-6,6,10,-3,7,-7,-9,2,7,1,1,-2,9,-8,10,3,-4,-5,10,-5,5,-3,-4,4,-2,1,-4,2,-2,10,-10,7,3,-8,1,-2,-7,1,-8,3,9,3,6,-7,-8,2,4,-9,3,-2,1,1,6,9,8,-6,-7,2,-2,4,8,7,-7,-10,6,-5,3,6,9,-5,-7,-3,8,10,4,2,-1,-7,5,-9,7,-7,9,2,-9,4,-8,10,2,-7,-5,-2,6,-7,7,2,-9,6,2,-7,-7,-7,-7,10,-9,8,6,2,-9,4,4,-10,5,-2,-6,-10,-9,-9,-5,6,7,-10,3,-6,-1,-8,6,-6,8,10,7,8,-6,-2,5,7,-1,-5,-8,-9,-1,4,9,-10,7,10,9,-2,4,-8,-2,-8,-3,-1,4,-2,9,4,-5,2,6,8,1,-4,3,-1,-8,-10,-4,4,3,4,-1,9,-7,-7,-4,-10,-4,7,6,-4,8,7,-5,9,8,-9,6,-4,8,5,6,-6,-10,10,2,10,8,-2,-10,-2,-8,7,8,6,3,-9,-9,-3,-9,-2,-7,-2,2,9,-9,-10,1,-3,-9,6,-2,-2,9,7,8,-8,4,9,4,-7,6,-9,7,7,-1,-7,-7,4,-4,-5,-2,7,-5,-1,-2,-3,10,-7,-4,-2,-7,-1,-9,2,6,8,-10,-4,-9,3,7,-2,-8,1,-1,-10,-3,-5,-6,8,4,-1,-10,1,-2,-1,-10,4,-1,-3,-10,-1,4,9,-2,-1,4,-3,7,-4,-8,-7,-9,10,8,2,-6,4,10,-9,10,-9,4,-7,-5,9,7,4,7,-3,7,4,8,-3,-1,1,4,4,-3,8,-3,1,-5,3,9,10,1,9,-1,-8,-7,-4,10,-1,-10,-10,8,-2,-8,-8,2,5,1,5,-8,-6,3,-8,-7,-3,-9,-9,-6,-1,-5,1,6,-3,2,1,-2,-5,-7,7,3,1,4,-9,3,3,1,-7,2,6,-9,-3,5,5,2,-6,-1,7,8,-6,-7,1,4,9,-10,-9,-3,10,-2,-10,7,9,2,5,-1,-5,9,8,-5,-1,-3,4,5,-4,8,-1,-9,-5,8,4,-1,10,4,3,-7,4,7,6,1,8,5,8,-4,6,3,1,-9,-3,-9,10,-3,5,-2,1,-2,-7,-10,10,6,-6,-8,-2,-8,-9,1,4,-6,1,2,3,1,-9,-3,-5,-7,-7,-7,-9,1,-3,-9,-6,8,3,9,3,4,-1,1,5,4,-10,-10,-8,-10,5,10,2,-9,9,9,-8,-2,-9,4,10,5,-10,2,9,-9,-9,6,-8,-8,-4,6,1,10,2,5,3,5,-6,1,9,10,8,3,2,2,-10,8,8,-3,-4,-6,8,-10,6,-10,3,5,5,-7,9,10,10,1,6,10,-10,-6,-6,1,-10,-9,10,-4,1,-9,-3,-8,-7,-10,-10,-4,7,-9,8,6,-2,1,-10,6,-8,-10,3,5,8,4,6,-10,-10,7,-2,6,-10,5,-5,9,-7,-6,10,2,-7,-6,8,5,7,-4,6,3,10,-4,-1,8,-6,8,-8,-2,1,-7,3,5,-5,-7,2,5,-9,6,-3,-8,1,-5,-10,-1,4,-10,-9,7,7,-4,-5,8,9,-4,8,-1,9,7,2,2,5,5,8,-9,7,3,-2,5,-7,-4,-2,6,-3,-3,-3,3,7,-4,-1,10,-6,-9,4,-2,3,-5,-10,-8,-6,-10,-4,-6,10,-5,-5,-8,-10,3,-10,-4,-8,-10,2,3,-9,-6,7,-3,4,-9,-7,-1,-3,10,7,10,2,8,-10,-3,-6,-9,3,-2,-3,5,8,-4,10,6,-7,5,-8,5,-5,-6,-9,6,8,6,-6,1,7,-7,-1,-6,-1,8,-5,-9,5,-3,-10,-4,-4,-2,-5,6,-10,1,-8,-10,8,-10,2,3,-3,-2,5,3,-10,4,8,7,3,-9,-5,-9,6,-5,-7,8,7,4,7,3,-2,3,9,8,-8,-2,-6,5,10,-10,10,-10,-9,-1,2,6,-3,6,8,3,-10,8,-7,6,5,-6,-8,-6,-1,-3,-2,-8,7,6,-5,3,3,-1,-6,-10,7,-10,4,-1,-2,7,5,-9,-9,-10,-4,-4,-4,-9,-2,-5,-7,-1,10,4,-8,6,-10,6,7,-8,6,-10,-4,5,8,-4,-5,-3,-9,-7,-2,8,7,1,-9,5,-8,-10,-3,-10,-4,-5,-1,4,-9,-9,-5,3,3,5,5,-7,-6,9,1,2,6,-4,10,-9,10,-10,-4,-6,10,-9,3,2,-5,1,-10,9,2,3,3,9,-9,-10,-5,-2,-10,-4,8,-4,-6,-7,8,2,-3,-10,-6,-2,1,10,10,4,4,5,-3,5,4,8,9,-1,-5,-9,-1,8,4,-9,3,-4,-3,-8,-8,8,4,1,5,6,-3,3,-5,-6,-2,-3,10,1,-8,10,2,5,3,9,-8,-10,-1,4,5,-7,7,-1,9,2,10,1,-1,10,-2,4,6,-10,-8,-5,6,-1,1,-4,5,-8,-8,-9,-5,3,-9,-7,2,4,-4,4,-10,-5,-8,-1,-4,7,8,-1,6,2,2,2,9,-3,-6,4,-1,-7,9,9,9,-5,4,1,1,-7,3,4,-7,6,3,7,1,10,-4,-3,-7,-9,2,10,3,6,-7,7,-9,-7,-5,6,-10,5,-5,8,-7,-2,-9,4,-10,-8,-1,2,10,-4,-4,10,-5,10,5,4,5,3,-6,5,-7,4,-8,10,6,2,2,-5,-8,9,-1,7,8,-9,7,2,-7,-4,5,-2,7,2,-5,-10,-10,-8,3,6,-5,6,10,-8,8,-3,-7,3,-6,-5,10,4,6,2,5,-1,-4,6,6,-3,5,7,-1,-8,-7,-8,10,-8,1,-6,-7,-1,-3,-7,1,5,-7,10,7,7,-10,-3,-4,-7,-1,5,9,1,1,4,9,9,-6,-8,-4,-6,-7,-5,10,-7,-6,-8,-8,-8,8,-2,3,-7,-8,-1,7,7,6,6,-5,-6,-7,5,-5,6,-6,2,-10,10,3,10,-9,-5,-10,-1,-8,-3,1,-2,-10,-2,9,-6,7,6,-7,2,-7,1,2,2,6,6,-5,8,9,2,5,6,5,-4,10,8,-4,5,-10,-7,4,8,2,-5,-5,6,6,-4,3,3,3,-3,10,-5,4,-9,-5,-8,-2,-7,-7,-8,6,3,-9,7,8,3,7,-10,-1,-9,-7,-5,-7,5,9,10,7,-7,10,10,-1,9,2,8,10,2,-6,6,1,-1,7,6,-5,-10,-6,-4,-7,6,2,-3,-3,10,3,-5,7,5,-7,8,7,-6,10,1,-3,-7,2,9,-6,-7,3,3,9,-4,10,-8,-9,9,6,-9,8,-6,-7,-8,-4,-1,-8,-8,2,-3,3,-9,-6,4,-10,-3,-2,-9,-3,-3,1,-5,6,-5,-5,-1,8,1,-10,-7,1,-1,8,1,6,-8,7,7,7,2,-8,8,-4,-3,-7,7,10,-10,-7,-10,6,3,3,9,-9,10,3,-7,-1,1,1,-6,3,9,-1,-4,-9,2,-6,2,1,5,1,9,2,-10,8,-4,-3,3,-2,-3,-6,10,6,-7,5,-1,2,8,9,-7,-5,-8,-1,-2,-9,-1,10,5,7,-2,-4,9,-2,9,5,2,6,8,-2,10,7,-4,-7,4,-3,-6,-1,2,-2,-9,-9,-8,-1,-4,-9,2,-10,-3,-9,10,-7,-6,1,-2,-3,1,1,8,-6,-5,-9,-8,-5,-5,-10,-6,-1,-5,-2,-5,-9,-8,-4,2,-9,2,4,-6,-3,-5,5,-9,-6,1,1,-5,-2,1,-9,5,-10,7,-9,6,5,-6,-3,-1,9,-6,-5,3,2,-3,-8,1,7,3,3,9,-1,2,-10,-10,2,9,7,-5,5,1,8,1,-2,-5,-6,-4,-9,-10,7,6,-5,7,7,2,3,7,-7,-9,5,-5,8,7,-6,-6,6,-2,-9,7,-2,1,-4,7,7,2,9,4,-7,-9,-9,-5,9,9,6,-7,5,-2,-6,-2,-4,-6,4,-4,-2,-5,8,-7,-7,6,-2,-2,8,-8,2,7,6,2,-5,4,-1,-10,7,5,-4,7,-1,5,-2,6,-2,-3,8,2,-4,-1,-3,4,-10,8,-10,-2,-4,4,9,-4,-3,-3,2,2,-2,-9,-6,9,-1,-2,1,-4,10,-3,-8,-1,-1,9,2,9,8,8,-2,10,1,-6,5,-7,10,7,6,8,-4,3,10,-7,4,4,4,1,7,10,-1,-8,-9,-8,3,-4,-5,-3,3,-5,9,2,3,-9,-5,2,-7,7,-5,3,-3,7,6,-4,1,-5,-9,2,-2,-4,-3,3,9,8,-4,-6,-7,-6,-4,-9,10,-3,-1,-4,-9,2,-7,2,2,3,-10,-7,-1,-8,-3,-10,-3,3,10,-10,10,-1,-4,4,-2,6,-6,-8,3,-2,7,9,-4,5,-4,3,7,-10,8,9,-8,3,-5,1,-9,6,4,5,10,2,-4,-7,-2,2,-8,3,5,2,-8,-9,5,-2,-1,-8,8,-4,-8,3,-5,-1,7,10,1,1,-4,-8,-8,-9,9,9,-9,10,-3,9,-2,-2,4,1,4,7,-4,7,5,-10,-5,-2,3,4,-8,5,-1,9,1,-3,3,2,-6,1,7,8,2,6,5,-3,-1,1,9,1,9,4,-5,9,-7,3,-4,6,2,-3,-2,-9,7,8,1,4,3,-2,-6,10,-3,-9,-7,-5,7,-5,4,-3,-6,-5,-10,7,-10,-4,3,-2,-8,-5,6,-5,8,3,3,-3,8,-6,-8,2,3,4,1,-2,7,-5,7,-7,9,7,7,-3,-7,-5,-1,2,-4,-7,2,-3,7,1,7,7,7,8,-3,1,7,2,5,-1,10,-2,-7,3,-3,6,-4,6,8,-7,4,-8,6,-10,-5,7,-8,10,-6,-9,-9,10,9,-7,9,-5,-4,5,-2,10,-5,5,-8,9,9,-4,3,4,-10,-9,4,4,-5,-9,-4,-6,-8,2,-5,-1,-1,5,-10,7,9,-3,-10,-5,7,-3,5,-10,10,2,-7,2,-9,-5,7,3,8,10,-2,-2,-1,8,4,-2,3,2,8,-7,4,-7,4,6,3,-1,-3,4,7,1,-1,8,6,4,-5,-10,-3,-7,-7,10,-10,-7,-3,8,-2,-1,-3,-6,8,-10,1,1,7,10,4,-5,10,-9,10,2,10,6,-2,-2,-2,-3,-4,-6,4,-6,7,-3,3,1,1,7,7,-5,-6,9,-9,1,-9,-4,-3,1,2,-1,8,-10,5,2,-1,-1,6,-2,-4,-8,-10,-6,-5,-4,-3,-3,7,3,1,6,-4,8,8,-7,-5,-5,-9,9,-8,-4,8,-3,3,6,3,7,-10,-9,6,-1,1,7,5,-6,9,-5,9,3,-5,-7,3,-8,-10,-9,1,9,-6,-1,-2,-7,7,7,1,8,-9,6,1,-4,1,7,-5,-5,3,-3,3,6,-1,7,-5,10,2,-7,-2,-3,-4,4,-9,2,4,-8,7,-8,9,2,4,9,10,10,4,-2,6,-10,4,10,9,-7,-4,-5,-2,-10,-1,-2,-4,10,8,8,7,-10,2,-10,-9,-7,4,7,-1,2,-5,-2,9,-7,-3,10,5,-2,1,9,-9,-3,2,-8,-7,4,9,1,7,4,2,-9,-5,5,-3,5,5,-4,10,-10,4,-8,-2,-10,4,-9,9,7,-7,1,-9,3,-6,10,8,-2,-6,7,9,6,-3,-2,-3,10,3,1,10,7,10,2,7,-2,4,2,-7,7,-5,4,-9,-9,6,6,3,-3,-1,1,-1,-5,-4,-8,-7,-3,-7,-10,1,-1,-9,-4,10,-5,2,-1,1,-8,2,8,-5,2,9,-8,-3,-9,6,7,3,-7,8,-10,5,-5,-5,6,3,-2,2,-3,9,-9,5,10,-8,3,-6,-8,-2,-10,6,-7,-6,9,8,-6,4,-3,3,-9,2,-10,6,1,-1,-2,-9,-3,-9,6,4,6,7,-9,5,-3,1,-9,-1,4,3,6,7,8,2,5,8,-8,-3,7,-6,-6,4,-3,-6,-5,-4,-3,-10,9,7,-2,7,9,-6,9,7,-8,-1,-5,9,-7,1,-6,-3,5,-8,6,-4,5,-3,1,-10,-2,9,9,9,10,8,-3,10,-2,4,4,-2,9,3,-7,8,-3,7,6,8,6,-4,6,8,4,5,-1,9,4,1,-7,3,7,-2,7,-8,5,-3,-8,10,-2,-10,-3,4,-2,-3,1,9,-7,10,-10,-7,2,7,-1,-2,3,8,4,7,5,5,5,4,6,6,-4,-2,-4,-8,7,2,3,-7,-9,3,4,2,5,-3,-1,6,3,4,8,-6,2,-6,-7,-2,-9,2,4,-5,1,-9,-9,10,4,3,3,-8,7,-2,8,3,-10,3,9,2,-7,4,7,-10,-7,-2,2,7,-5,-4,-2,2,-1,3,-2,2,7,5,-10,-4,8,7,-7,9,-3,7,-9,-5,-4,2,7,-7,-10,10,-7,-6,10,5,10,-1,7,8,9,-6,-4,-8,2,5,8,-3,10,2,-5,-7,-10,-5,6,-3,-7,-7,9,1,-3,-3,-2,7,-6,-1,-9,5,7,-8,-5,10,-2,-4,2,-2,4,7,-4,9,7,-2,-8,-6,6,10,5,-5,6,-5,5,-5,-3,-6,-9,8,4,-10,4,9,-10,-3,-10,-9,8,-7,3,3,-4,-4,5,-7,-9,-3,-3,-5,5,7,6,2,-1,-6,-10,-4,-9,7,10,3,3,6,-2,8,-9,-3,-10,-9,-3,-9,4,-7,-2,7,10,-3,9,8,10,-9,2,4,-6,-7,7,-5,-9,-6,-9,-5,4,-2,9,4,-8,10,4,4,-6,2,6,6,10,-6,-6,7,-1,5,-9,-9,4,8,3,2,2,-5,-1,-6,5,-1,-3,1,7,3,-4,4,-2,-6,6,-8,-3,-9,-6,-7,-6,-1,7,4,7,2,2,9,-10,-2,-4,5,3,-2,-10,1,-7,7,-4,8,10,5,5,7,1,-2,-8,-4,2,2,-7,7,7,8,5,-5,7,7,3,7,-3,-1,-5,-4,3,8,10,1,-1,9,6,-3,3,5,3,-2,-1,7,-7,3,-6,-9,-8,6,-3,7,10,-2,-9,-10,9,1,4,5,9,-3,-1,-5,-5,10,5,-7,7,-9,6,-9,1,4,9,9,9,5,6,-9,-1,9,6,3,5,10,-3,-8,-10,-10,-6,-7,10,-5,3,7,4,-4,-4,-4,10,2,-4,8,7,-2,-8,7,4,6,5,3,-1,-10,3,4,7,-7,-10,-4,4,9,-7,-9,6,8,9,1,-6,5,-4,-3,8,-3,-4,7,-4,-9,3,-2,3,10,-1,4,-1,-9,1,-7,1,-9,-6,-4,-1,9,-10,4,-1,9,-7,-1,3,3,-1,5,10,-8,10,-5,6,-6,-7,4,-7,9,-6,-4,10,7,10,3,7,4,-7,10,-3,2,9,7,8,1,6,-5,5,-6,-3,2,-4,9,5,5,-8,-7,2,4,-10,4,-10,-2,10,-7,9,-4,6,-4,-3,-9,3,-7,-10,5,-5,5,7,-10,5,9,-7,-7,-6,-5,10,-9,10,10,-4,9,3,5,-3,-6,-2,-4,-7,3,-2,2,2,6,5,3,10,-9,8,-4,8,-9,2,1,-4,3,-5,-9,4,1,3,1,8,8,-5,-8,2,-5,-3,-4,-3,5,1,6,-1,-5,3,-8,7,8,10,-4,5,9,-8,-7,9,6,7,-5,9,3,-7,4,8,-3,9,-1,9,-4,-2,-7,-2,2,6,-10,-1,-8,3,-10,3,-9,5,9,-1,-2,-4,5,1,-9,-9,2,9,6,-2,-5,4,-7,8,-4,9,-4,-2,-2,10,-9,-8,9,-1,-3,3,-5,-4,7,-10,-2,4,3,5,-10,5,-4,-10,-2,9,-3,-5,-1,-3,-2,-9,2,-10,-1,8,-2,3,-8,8,-4,-7,-9,-7,3,1,5,-10,3,-9,5,-10,-4,4,5,-4,-8,8,-5,-10,-7,4,10,6,-3,10,6,-6,2,-2,1,8,9,9,-10,-2,9,-8,9,-2,1,-2,-3,-7,10,2,5,1,3,-10,8,-2,8,-5,4,-1,1,-3,-6,7,-2,-7,8,-3,-7,-8,2,3,-9,-1,8,-7,-7,-3,-1,-9,1,1,4,-4,4,-10,-1,-10,-3,-3,-3,2,-1,5,7,-6,-9,-2,1,-6,8,-3,8,9,-2,-4,5,7,3,9,-5,2,3,1,-2,1,4,10,7,5,4,-4,-7,4,-2,-2,1,5,8,10,-2,1,-4,9,-2,1,-4,-4,8,3,-2,-9,8,9,-9,-7,1,-6,-9,-6,-9,-7,-6,6,-9,-3,3,-4,-7,9,1,4,6,-6,-7,5,3,-1,-3,2,5,2,9,-10,-10,-10,-9,-4,-8,-9,7,1,8,-9,-8,-2,8,2,4,6,5,7,-4,-8,-3,5,2,10,-7,-10,1,7,-10,9,-5,9,10,-3,-9,7,9,-2,10,-3,-2,-4,-7,-10,-2,-2,-3,8,-7,10,-3,9,-10,4,-4,9,-10,-7,-3,-3,-6,-3,-5,4,1,9,-2,-7,1,2,-8,9,1,-4,-3,-1,-3,-1,3,-2,1,10,2,-4,9,-8,9,7,-5,6,2,-10,10,-3,7,7,9,-1,-5,7,3,2,-5,1,2,10,3,-6,1,7,-9,8,-2,-10,-4,-2,4,-10,-3,-9,-8,-6,10,5,-5,1,-7,-1,-10,9,-10,2,4,-3,2,-1,-2,3,-1,5,-3,8,-7,-10,-2,10,7,-7,5,8,-1,-10,-6,-7,3,2,10,7,-1,-6,-3,6,-10,3,-3,3,-1,-7,7,-3,5,8,5,3,-2,10,5,7,1,1,2,7,6,-10,7,-5,9,8,-1,-4,9,-8,2,-10,-7,6,-6,5,-7,6,8,-6,7,3,-4,8,-10,8,2,-6,10,10,-7,7,-8,9,6,-5,9,10,-4,9,-5,-10,6,7,10,-3,2,2,-4,-8,-6,1,10,1,2,-9,-6,5,5,-9,1,1,-1,-5,-3,5,-3,-5,10,6,5,-8,-4,-4,-8,3,6,-3,6,3,-1,1,7,-7,-1,8,8,-8,10,1,-6,7,8,-2,-8,-6,-5,2,-10,-8,2,8,1,-4,9,-1,8,8,8,10,6,4,2,1,5,-4,7,-8,-7,1,8,10,10,1,9,3,-9,7,2,-3,9,-5,9,-5,8,4,-8,3,4,5,7,-9,2,8,-5,-3,8,1,1,-8,1,-6,-8,-8,-3,8,-10,8,4,-8,-9,-1,6,8,7,-8,-8,1,1,6,4,-8,10,6,4,-3,2,-1,8,-8,3,-5,-10,5,-8,7,-7,-4,-1,-3,2,-7,9,-5,-5,-2,-10,-9,3,-4,-7,3,-8,-2,-7,3,8,6,-9,-4,5,-5,1,7,-10,-7,6,10,4,2,-7,-3,-6,-10,-1,9,10,-2,8,7,4,6,3,-1,-7,10,-9,-9,-1,2,-5,7,7,-6,-1,-4,8,-5,7,10,1,10,-3,7,-7,-6,-1,8,4,-6,1,-2,-1,2,2,-2,1,3,10,-8,10,-1,-8,-1,-5,9,-9,4,7,10,7,-4,-5,-2,6,1,-3,9,1,4,-8,-1,4,-1,-3,-4,-2,-9,-3,9,1,7,4,3,-5,1,-10,2,-2,-6,-1,-7,7,9,7,3,-2,1,-4,9,-3,-5,-7,-6,-10,-5,-5,8,-10,-3,-7,-6,7,-4,2,-4,-6,-8,6,3,10,-10,10,-6,5,7,8,-10,1,-9,7,-9,-10,7,3,-3,10,8,9,2,5,-5,-5,9,-9,10,-10,1,8,-8,-2,5,-6,3,9,1,-7,9,1,9,-6,10,-9,-8,10,9,-10,-5,-7,4,-6,-10,-1,-4,-6,-4,1,8,4,-5,3,10,8,2,4,3,-8,2,1,2,8,-10,2,8,-6,-4,-9,-4,8,4,9,3,-2,9,-10,3,-8,8,4,6,9,1,-4,4,-3,5,10,1,2,7,10,-1,-6,-8,5,10,-6,1,-8,-2,-5,-2,5,-7,5,1,6,4,1,2,-10,7,1,-5,-2,9,6,-2,-7,7,5,-7,-10,-2,-5,-6,-5,10,-2,7,4,3,7,10,-6,-6,-7,-1,6,-9,-8,-5,-1,-10,-1,-8,3,4,9,-6,5,6,-6,10,-10,2,-5,2,-3,-8,9,1,7,6,1,1,-3,-9,-5,3,-9,5,4,-1,-10,-3,-7,3,-10,-2,-10,-9,1,3,7,1,-3,-4,-4,5,-6,-2,-3,-8,3,-5,2,-7,-4,-9,8,-8,6,7,-9,-1,1,9,-10,8,-5,-8,9,-2,-8,3,-8,-5,5,4,4,-10,-3,-8,3,8,-1,7,-2,2,-9,-5,9,3,4,9,-5,3,-7,-10,-9,10,-5,-9,-7,10,-9,3,7,-4,-3,2,-2,-7,8,-1,8,-4,-10,3,-5,1,7,1,-10,-8,-8,5,5,-10,1,-7,-3,-3,5,8,8,1,-5,-9,7,-10,-8,-6,-8,4,-8,-10,4,-1,9,7,1,3,2,1,-1,-6,-7,-2,9,-6,-8,7,10,-9,9,8,-5,6,-3,1,-9,5,-9,4,-2,6,-7,-2,-1,7,8,-8,4,-4,-2,-3,2,-10,4,1,-2,-9,-8,-5,-3,-8,6,8,1,-9,7,-5,-1,-9,9,-4,-7,-2,-4,-5,-9,-10,9,9,7,3,1,2,3,8,3,4,4,6,-3,3,-2,-1,8,-10,-9,1,-1,3,-6,5,-2,9,5,2,-6,1,9,-10,-1,5,3,9,1,-9,2,6,5,2,1,-7,2,-7,-2,-9,9,-3,10,-6,4,7,1,2,9,5,9,-8,-2,1,6,-6,-3,-5,1,-5,-1,2,4,-8,-9,4,7,-10,-1,-4,2,9,-1,10,10,-6,8,2,2,-4,5,1,-3,4,2,8,9,1,4,3,-7,-6,7,-6,8,-3,1,6,5,-8,7,2,5,-8,-7,4,10,-10,8,9,7,10,6,-1,-5,7,-5,7,-2,-9,-6,4,5,-2,-9,8,2,5,-3,8,-5,7,4,2,-3,-7,-5,4,3,2,8,8,-9,8,9,-7,1,-8,2,-10,-10,3,-8,-7,4,2,1,-1,-3,2,7,10,-7,-2,6,-5,1,-4,-4,9,-10,9,-1,2,3,9,5,-7,-8,1,-3,2,4,-2,-7,-6,1,8,10,-5,-4,-3,4,1,-9,7,9,-5,-7,1,7,1,-7,-10,-1,-7,1,-5,-10,-6,1,2,-5,4,3,6,-5,9,-7,8,-4,-6,7,-8,2,-7,-1,4,5,8,3,9,2,-3,-5,-9,-8,-1,-10,1,7,4,6,-6,6,-8,-7,-1,4,-7,5,-9,-5,-7,1,7,-7,-10,9,-3,-7,3,9,-2,-8,-2,-7,5,1,-4,-9,4,2,-8,-9,5,1,9,-4,2,10,-4,-7,8,10,-4,-5,-4,4,7,2,-9,-1,-4,1,-8,4,-9,-10,10,-1,8,5,-4,-3,-4,4,-1,-4,-2,1,-8,-4,5,-6,-6,1,4,8,-7,-8,8,-6,8,4,-7,-2,1,3,-9,-2,7,-9,-1,6,7,-9,-5,4,5,5,-4,-8,-2,10,10,-8,-7,-8,5,-6,-10,-9,-2,-10,2,10,4,-10,8,10,4,-7,-5,9,10,4,10,7,-10,-10,4,-10,-7,3,-2,3,10,-7,4,-7,-9,6,-8,-5,10,1,-5,-10,-1,8,-7,9,1,-4,-2,-3,4,2,10,10,-3,4,2,-2,9,8,1,3,3,-10,10,8,1,-8,9,3,-7,-2,2,-3,4,-7,9,8,7,9,-1,3,-8,5,9,1,-6,6,-7,-7,8,-7,-3,-1,2,2,-6,5,6,-1,-9,-10,5,5,4,-4,-7,1,5,2,1,-9,9,-9,6,-9,-2,4,-6,1,10,-2,6,8,-5,-7,4,-3,1,-9,4,6,6,5,-8,2,10,6,9,-7,4,-3,9,-3,-10,9,-10,-9,-4,10,9,-9,-6,-6,7,-3,5,-9,-4,7,5,-5,3,-1,6,-7,1,-7,9,6,-7,6,7,-8,-10,-2,-3,7,-10,-2,-8,-5,-5,8,4,-1,-4,-2,-6,1,-7,8,9,7,2,8,-8,-10,5,-10,-5,9,10,10,4,-10,4,5,3,-5,-1,6,-7,-6,-8,1,-7,-3,-4,3,-2,-10,-10,10,-5,10,-7,9,5,-6,2,-6,-8,6,-10,9,-3,-10,2,-8,-4,-6,7,7,-1,-4,-10,1,-9,-9,7,5,-7,-3,-7,-7,-9,6,-8,-7,5,3,-4,-3,-1,-4,-8,-6,-5,3,10,-5,-5,-5,3,4,-5,-1,-1,-4,7,-1,-8,-10,-8,7,5,8,-2,-4,7,2,5,3,-10,-8,-6,1,-8,8,-6,-5,-6,2,8,-2,-6,-10,-8,6,-1,-2,-3,-10,-6,8,-3,4,8,5,5,-2,2,9,7,7,-10,-3,-3,-8,1,-2,9,-2,-3,-4,6,9,-9,7,4,4,-2,10,1,-4,-2,-7,-2,9,-9,6,-10,-3,-3,-5,-4,-2,-7,4,10,10,-4,-4,-7,-4,7,-2,-4,6,-7,4,-3,10,9,-5,1,3,-2,6,2,-6,1,-6,4,2,-6,-5,-3,8,-10,-2,-8,-10,2,2,5,2,7,-1,-1,-6,-1,7,-7,-7,6,2,6,6,6,-3,7,9,5,-9,-4,5,-8,-9,-7,-4,8,9,-7,-4,-7,6,-10,10,-6,4,-5,-7,-1,-10,5,-3,1,6,9,1,-5,-9,-5,-2,9,-2,7,9,-6,-8,2,-3,-3,1,9,7,-10,-2,-7,-5,-2,-3,8,7,-9,-6,-6,6,-10,-1,-8,6,5,2,-2,-8,-5,3,3,7,5,-4,4,8,4,4,8,-9,-8,6,-9,-4,7,6,-7,3,8,-1,-7,6,-10,5,-10,2,-7,-8,5,9,-9,-2,-9,6,-2,10,10,1,6,-10,10,6,10,-4,-4,-5,-7,9,3,3,-4,5,9,-4,1,3,5,1,-3,-10,-5,10,-3,-7,-6,-2,-3,6,10,-7,3,-4,-1,-4,9,1,-9,7,-2,8,5,8,-4,10,-4,9,-8,8,10,-4,-7,3,6,10,4,-5,8,9,-10,10,-5,-3,-1,-4,6,10,-1,-9,-2,-4,-7,-7,4,10,4,-10,-10,2,6,4,4,-5,-6,-1,-3,7,7,8,-10,5,-10,-3,-10,2,2,7,-10,10,-7,6,-9,-2,7,-8,-10,-2,-10,1,-3,5,10,1,6,-6,6,5,-5,2,8,-2,4,7,1,5,2,9,-4,2,6,5,9,7,-8,7,-10,-4,-5,8,8,9,-5,-2,3,-1,1,10,7,-6,-6,-10,-2,-1,-5,2,-4,5,-1,8,-2,-2,-4,-5,-10,5,1,-2,-2,-9,-2,2,2,-5,6,-9,-2,-3,3,-5,-6,1,-8,2,6,6,-10,5,-8,7,4,4,6,10,3,4,-10,9,-8,7,-10,-3,3,-4,-8,5,-6,-8,6,6,7,-9,7,-2,-8,-8,-4,-1,-8,-6,-6,10,1,6,8,-7,2,-10,3,-3,-3,-9,1,-3,-5,-7,1,-2,-5,-8,-10,6,2,-10,-9,5,-3,10,4,-7,10,9,9,-4,10,7,-8,4,10,4,-9,3,3,8,-5,-6,8,8,7,-4,-5,-8,4,2,10,-3,-5,10,10,-7,2,-1,9,8,3,-4,10,1,8,10,-1,4,1,-6,-2,5,-8,-4,8,-2,3,9,-10,9,-6,-5,-4,-3,-4,8,-1,2,1,-6,-8,-10,-6,6,9,-5,6,10,-10,-5,-1,2,7,-1,10,7,-8,8,-6,-4,-10,10,1,-6,-6,-7,5,8,3,-10,1,-10,-6,4,3,-9,-7,8,2,8,6,-4,5,3,-3,9,-10,-2,-7,10,-2,-2,-9,-6,-6,-6,2,-3,2,-4,-9,-1,-4,-7,9,3,-4,2,-7,4,-7,-4,-10,5,-3,9,2,10,2,6,-3,-5,-4,-2,-9,4,7,-2,-7,1,6,1,-1,-3,-8,-8,-8,10,2,-4,-10,-7,-10,-8,-8,6,-10,-1,6,7,2,7,-8,5,10,-3,10,1,-8,5,-7,-9,8,9,-5,7,10,1,-2,-8,-6,5,10,3,3,6,-1,-7,7,2,-2,1,-5,-10,9,-9,8,8,-2,-5,-3,4,-6,-2,9,-6,2,-3,-2,-6,-2,3,-1,-7,5,7,-3,-1,-6,-5,-6,-7,10,9,-4,2,-10,-3,9,-1,4,-4,10,7,10,-10,4,-9,7,8,-1,-7,-9,-1,2,5,-1,-2,-6,-7,-2,-5,4,3,-1,5,5,-2,-4,-5,6,-2,-10,-10,-5,5,3,6,-3,3,3,-6,1,5,5,-10,1,-8,6,9,4,-1,-3,8,-9,2,8,10,-7,5,-6,-3,-6,-8,-10,6,-1,2,-5,10,1,3,9,9,10,-10,-8,3,-7,-8,6,-2,2,-10,6,8,1,7,9,-10,1,-5,-4,-4,-9,-5,-8,-3,2,-7,3,-6,-9,8,10,-8,5,-9,-2,-9,5,8,-2,-4,-4,3,-8,-6,1,-6,-10,-9,6,6,-8,10,9,-7,-1,-5,3,4,6,-8,-2,5,7,-8,1,4,7,5,4,-6,4,-9,1,8,-3,-4,1,6,-5,-4,6,-8,-1,-10,-4,1,-10,-4,-6,-10,-1,4,8,-1,-4,-1,-2,-5,1,-10,-4,4,-1,-6,-3,6,3,-7,9,5,-2,4,-5,-6,4,3,7,3,8,-7,-6,-6,-2,-1,2,4,2,7,-9,-8,-1,1,10,7,3,-10,6,1,8,1,-10,5,5,1,-7,8,-10,5,3,8,8,7,4,4,-2,4,-1,5,-3,1,7,-7,8,-9,-5,-1,6,7,-5,-4,7,10,8,-6,-2,-10,-8,-8,-10,1,3,-8,-9,-9,-5,3,2,2,9,-1,-8,-1,-8,5,3,1,8,-7,4,1,-8,5,-10,-7,6,-9,9,-1,9,4,3,-10,-5,-8,-2,2,5,-7,4,-3,4,-5,2,-1,-3,4,10,-9,-2,8,7,-1,9,9,-4,6,-4,4,-8,-8,-9,8,-8,-4,5,-2,4,-7,3,-6,8,-8,2,10,-8,10,-1,-7,-7,-9,5,-7,7,1,1,1,-7,2,3,-9,8,-8,-2,-10,-6,-3,10,-1,3,-9,7,-4,8,-8,-5,10,8,6,3,-9,3,-1,2,-10,-3,-1,-6,7,-10,5,-1,1,-4,-9,1,5,2,6,7,-8,4,1,4,-6,-4,-10,-5,-4,9,6,-5,-5,7,10,-9,6,-10,3,-6,8,9,5,-2,5,-4,3,-1,6,-2,-6,7,-4,1,-2,-8,9,10,-3,2,-4,-8,8,7,-1,-4,-10,9,9,1,8,-2,7,8,-6,8,9,-9,9,-4,-3,-7,1,-6,5,2,9,8,-7,7,-9,5,3,6,8,-2,10,5,-5,-2,10,-4,7,4,10,-9,-6,-8,6,3,-6,6,-6,7,-2,4,10,-1,-1,3,6,-2,-4,-3,4,6,-3,-8,-1,-10,4,5,1,-3,10,-6,7,7,6,-4,6,-2,10,7,5,-6,-3,-2,-6,-9,-2,1,10,-1,-9,-7,-4,-5,-9,6,2,-10,3,-1,9,-3,2,-2,-3,-1,7,9,-8,-6,9,-10,3,7,-4,-5,8,-5,4,-5,10,9,-5,-1,-3,10,10,-4,-10,1,9,8,-5,-8,-2,-6,-10,-2,-3,7,-1,-7,-7,-3,2,-10,3,-8,10,-7,-2,5,-8,-8,9,7,2,-10,-7,-5,-1,1,2,-10,7,5,10,1,8,-9,5,-6,1,10,-10,-8,10,3,-9,6,-2,-5,-2,2,-8,-4,6,1,-7,7,6,8,-5,9,8]], dtype = "uint64")#candidate|22660|(4, 9828)|const|uint64
call_22656 = relay.TupleGetItem(func_17738_call(relay.reshape(var_22657.astype('int16'), [13, 3, 15]), relay.reshape(const_22658.astype('int16'), [9, 156]), relay.reshape(var_22659.astype('int64'), [546,]), relay.reshape(const_22660.astype('uint64'), [12, 3276]), ), 2)
call_22661 = relay.TupleGetItem(func_17744_call(relay.reshape(var_22657.astype('int16'), [13, 3, 15]), relay.reshape(const_22658.astype('int16'), [9, 156]), relay.reshape(var_22659.astype('int64'), [546,]), relay.reshape(const_22660.astype('uint64'), [12, 3276]), ), 2)
output = relay.Tuple([bop_22629,call_22635,call_22656,var_22657,const_22658,var_22659,const_22660,])
output2 = relay.Tuple([bop_22629,call_22636,call_22661,var_22657,const_22658,var_22659,const_22660,])
func_22668 = relay.Function([var_22627,var_22657,var_22659,], output)
mod['func_22668'] = func_22668
mod = relay.transform.InferType()(mod)
var_22669 = relay.var("var_22669", dtype = "float64", shape = (9, 6, 8))#candidate|22669|(9, 6, 8)|var|float64
var_22670 = relay.var("var_22670", dtype = "int16", shape = (585,))#candidate|22670|(585,)|var|int16
var_22671 = relay.var("var_22671", dtype = "int64", shape = (273, 2))#candidate|22671|(273, 2)|var|int64
output = func_22668(var_22669,var_22670,var_22671,)
func_22672 = relay.Function([var_22669,var_22670,var_22671,], output)
mutated_mod['func_22672'] = func_22672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21811_call = mod.get_global_var('func_21811')
func_21812_call = mutated_mod.get_global_var('func_21812')
call_22721 = relay.TupleGetItem(func_21811_call(), 1)
call_22722 = relay.TupleGetItem(func_21812_call(), 1)
output = call_22721
output2 = call_22722
func_22730 = relay.Function([], output)
mod['func_22730'] = func_22730
mod = relay.transform.InferType()(mod)
output = func_22730()
func_22731 = relay.Function([], output)
mutated_mod['func_22731'] = func_22731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_22778 = relay.var("var_22778", dtype = "bool", shape = (1, 11, 2))#candidate|22778|(1, 11, 2)|var|bool
var_22779 = relay.var("var_22779", dtype = "bool", shape = (11, 11, 2))#candidate|22779|(11, 11, 2)|var|bool
bop_22780 = relay.logical_and(var_22778.astype('bool'), var_22779.astype('bool')) # shape=(11, 11, 2)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_22786 = relay.TupleGetItem(func_15484_call(), 1)
call_22787 = relay.TupleGetItem(func_15485_call(), 1)
uop_22813 = relay.sin(bop_22780.astype('float32')) # shape=(11, 11, 2)
bop_22816 = relay.logical_xor(bop_22780.astype('int16'), relay.reshape(uop_22813.astype('int16'), relay.shape_of(bop_22780))) # shape=(11, 11, 2)
func_17005_call = mod.get_global_var('func_17005')
func_17006_call = mutated_mod.get_global_var('func_17006')
call_22832 = relay.TupleGetItem(func_17005_call(), 0)
call_22833 = relay.TupleGetItem(func_17006_call(), 0)
func_22033_call = mod.get_global_var('func_22033')
func_22037_call = mutated_mod.get_global_var('func_22037')
const_22858 = relay.const([7,5,1,-2,-3,9,9,2,9,-6,6,-7,-6,10,-5,7,-9,2,10,6,-2,1,-6,-3,1,-6,-3,-7,-5,6,10,-6,4,8,3,-9,8,10,5,8,3,2,-7,7,-7,-6,4,5,-9,6,-8,8,-7,1,10,-7,-3,10,-7,4,8,3,9,2,3,-1,-2,-9,7,-10,-9,-1,5,2,8,10,-3,10,10,-1,9,-6,-1,10,4,7,9,8,9,8,4,-3,-8,3,4,-3,-8,-4,3,-8,-5,4,1,8,10,7,-3,-4,-1,2,-1,-8,3,7,-5,-7,-10,-4,1,-10,9,6,8,-4,-5,6,-1,-4,-6,2,-9,-2,8,-9,10,-9,-9,-1,-2,-7,3,-4,8,9,-2,5,-10,10,5,-6,-1,5,9,-6,-3,10,6,2,-4,8,-2,7,4,-1,-5,5,1,5,-6,-2,3,6,-6,3,-9,-5,-6,4,-8,-10,-1,10,-2,5,5,8,-9,-5,-1,4,9,-1,-2,6,2,-4,10,-9,6,-2,-9,-6,3,3,10,-3,9,-8,3,-10,2,7,5,-6,-8,-3,-1,7,-2,9,10,-5,-10,-9,-6,5,10,-10,10,7,8,-6,10,-2,-8,6,-5,-8,-3,5,3,-7,-3,-9,7,-2,-5,-2,4,9,5,1,-6,4,-3,9,10,-10,-5,8,2,-4,8,3,-2,-5,10,8,2,-5,10,2,10,-4,10,6,2,10,10,2,-10,10,1,-3,-9,-10,2,2,6,8,8,10,6,9,-5,-7,-8,-4,4,-3,-6,3,-9,-2,10,10,4,9,-10,-5,9,-2,6,5,-3,-2,-3,9,-7,-6,-2,7,8,7,4,5,-1,-10,2,6,6,-4,-10,-3,-7,6,-7,7,-8,-3,4,6,6,-2,-1,-4,6,-8,-3,7,-9,-9,-7,2,-9,-6,5,-10,-7,-9,-3,-7,-3,7,-3,-7,-7,-9,-3,8,7,6,-7,3,1,4,9,10,6,9,2,-4,-4,-1,-5,10,-6,-2,-5,9,-10,-7,-4,-10,-6,2,5,-5,8,-6,9,-4,4,-8,-2,-4,-7,1,2,2,10,-4,-7,-6,8,-9,-9,10,9,-4,-2,-3,-1,-2,6,1,-5,3,-5,-10,-10,-10,2,-4,-7,-3,-7,1,1,-3,5,-2,-10,-6,-3,-9,-7,-4,8,-1,-6,-7,-1,5,10,-8,3,-7,5,9,2,-1,-7,-8,-2,-2,-5,1,7,-7,-3,2,-5,8,-6,5,5,7,-10,-8,7,-9,1,6,6,-5,-8,-5,-7,2,2,-1,5,10,6,8,-10,-4,8,8,-3,3,1,-6,-2,4,-8,-2,5,-6,4,2,2,-6,6,-4,-9,4,-4,-8,9,-2,-7,9,10,2,-1,7,-10,2,9,7,-3,-5,9,7,5,6,6,3,1,10,-10,3,-2,-6,-3,6,-1,-6,6,10,-3,-3,-2,-6,2,2,5,-9,-4,-5,-5,-4,-5,9,-4,-3,5,-7,-2,7,1,3,-9,-2,-7,-10,1,1,4,7,8,6,-6,10,8,-10,-9,6,7,-10,6,-9,2,2,1,-6,9,-4,-7,-1,-2,-5,-3,-10,10,7,8,2,7,7,-3,-6,-7,7,5,-8,-8,9,-5,-4,-6,2,6,-3,-9,-10,5,5,8,-5,-10,9,7,3,-6,-8,7,-6,3,-5,-2,-5,3,-1,3,-4,-9,3,3,-8,3,1,6,-5,9,-3,7,9,7,-2,6,-5,1,10,4,-10,6,8,-1,4,7,10,-5,-5,-1,-5,3,3,-8,7,-3,-10,10,-4,3,8,3,-3,7,1,4,-4,-5,-2,-1,4,6,4,2,-5,-6,-4,-3,9,6,7,-5,-1,-7,3,10,2,9,-1,6,5,-3,10,7,-3,9,-7,10,-7,8,6,5,-5,-6,7,-6,-3,-5,-4,-2,7,8,8,-9,6,-2,7,-10,6,-3,-7,7,-8,3,-5,9,-8,6,-5,-10,-4,3,4,6,-1,-2,9,-8,-10,-9,6,6,6,-2,9,-4,-6,4,2,9,2,2,9,-6,-1,-5,-4,-2,5,3,-6,4,-4,2,-2,-9,-2,-6,3,1,9,-10,9,5,-6,7,-3,-5,-1,3,8,10,7,1,7,3,-8,-9,6,2,-10,5,-9,-2,-7,-8,9,5,3,5,7,-6,-2,3,-8,-2,-3,-6,7,-3,-3,1,8,-1,9,-10,5,-3,-10,-6,3,-1,-7,7,4,-10,2,2,-5,-10,8,-3,6,9,4,6,-5,4,-3,8,2,6,-9,-5,-1,1,6,2,1,10,9,5,-5,6,7,-7,1,-4,-4,-5,7,-4,-9,7,-8,-7,2,-10,8,-7,1,-7,-9,-1,1,10,1,1,10,1,-2,4,-2,-3,2,7,-5,-6,-5,-9,-2,-4,-1,-4,-10,9,-7,10,-7,10,-4,-5,-9,-3,-7,-3,-9,3,-2,3,5,-8,4,10,10,5,4,10,8,-2,-4,-5,1,-5,8,-5,-9,-3,-8,6,-2,-1,-8,4,6,4,-10,-5,8,2,-9,9,9,-2,-9,-8,-9,9,-1,7,10,9,10,-1,-5,6,-1,3,9,10,4,-8,8,-2,4,-6,1,-4,-1,-1,9,10,4,-3,-9,-10,-2,7,8,9,-1,6,-10,4,7,-8,3,-10,1,10,8,-4,10,10,-1,10,4,3,-8,7,-2,-6,5,2,1,8,3,10,3,1,-9,-7,9,-8,9,-4,2,-6,6,-3,-1,6,2,5,-8,-1,-9,1,-10,-7,-6,-10,3,-5,5,7,6,-9,-9,-4,-3,5,3,2,-9,-2,3,3,-7,8,4,-9,-7,1,-5,7,9,-1,-10,-6,5,-3,-8,-8,-5,-9,10,-3,6,-4,-8,10,3,-10,8,3,3,-4,2,-8,-6,10,-4,-2,-5,-3,9,10,7,-6,-3,-8,7,-9,-4,8,5,8,8,-2,-8,8,10,-9,6,-4,6,-9,-6,2,5,-1,-7,-10,9,-2,8,-4,7,-5,-1,-6,-1,-2,1,-8,-3,7,-10,-8,8,5,9,-4,5,1,-10,-2,10,-9,-7,7,8,3,10,6,-1,-4,10,-9,7,10,-7,-10,8,9,-8,7,-2,-3,-2,-10,10,7,2,-5,-8,-8,-9,3,8,5,10,-2,-4,7,-4,1,3,-3,4,7,5,6,-4,3,10,-9,-2,7,8,2,-2,-3,10,1,-4,-5,-4,4,7,1,7,-10,-5,-7,-10,2,-3,-9,2,9,8,4,-3,9,8,-9,-2,-8,-7,-9,-5,1,9,-2,-9,7,-5,9,-1,-1,-8,8,1,-10,-2,-7,1,6,9,-3,1,6,-2,5,3,4,6,5,9,-6,-4,7,-3,7,1,10,9,9,1,5,-1,7,-3,7,-8,5,7,9,-5,10,6,9,6,-7,1,2,2,-9,2,9,8,9,-5,5,-7,-7,7,-10,-1,1,-10,-4,-2,9,1,-1,-3,-6,1,10,10,-10,-1,-1,9,6,5,-4,-5,9,3,6,-2,-6,-6,10,-4,-3,3,9,6,-1,-5,7,10,-7,8,10,-6,5,-3,-7,7,3,-2,10,-6,-8,-8,3,3,-10,3,-2,-6,-2,4,-7,-7,-9,-1,-8,1,-9,3,8,2,-8,10,6,9,-7,7,-3,4,-7,10,5,-1,4,-8,9,-2,7,-7], dtype = "int16")#candidate|22858|(1404,)|const|int16
var_22859 = relay.var("var_22859", dtype = "float64", shape = (364,))#candidate|22859|(364,)|var|float64
call_22857 = relay.TupleGetItem(func_22033_call(relay.reshape(const_22858.astype('int16'), [1404,]), relay.reshape(var_22859.astype('float64'), [364,]), ), 1)
call_22860 = relay.TupleGetItem(func_22037_call(relay.reshape(const_22858.astype('int16'), [1404,]), relay.reshape(var_22859.astype('float64'), [364,]), ), 1)
var_22867 = relay.var("var_22867", dtype = "float32", shape = (11, 11, 2))#candidate|22867|(11, 11, 2)|var|float32
bop_22868 = relay.add(uop_22813.astype('int64'), relay.reshape(var_22867.astype('int64'), relay.shape_of(uop_22813))) # shape=(11, 11, 2)
output = relay.Tuple([call_22786,bop_22816,call_22832,call_22857,const_22858,var_22859,bop_22868,])
output2 = relay.Tuple([call_22787,bop_22816,call_22833,call_22860,const_22858,var_22859,bop_22868,])
func_22873 = relay.Function([var_22778,var_22779,var_22859,var_22867,], output)
mod['func_22873'] = func_22873
mod = relay.transform.InferType()(mod)
mutated_mod['func_22873'] = func_22873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22873_call = mutated_mod.get_global_var('func_22873')
var_22875 = relay.var("var_22875", dtype = "bool", shape = (1, 11, 2))#candidate|22875|(1, 11, 2)|var|bool
var_22876 = relay.var("var_22876", dtype = "bool", shape = (11, 11, 2))#candidate|22876|(11, 11, 2)|var|bool
var_22877 = relay.var("var_22877", dtype = "float64", shape = (364,))#candidate|22877|(364,)|var|float64
var_22878 = relay.var("var_22878", dtype = "float32", shape = (11, 11, 2))#candidate|22878|(11, 11, 2)|var|float32
call_22874 = func_22873_call(var_22875,var_22876,var_22877,var_22878,)
output = call_22874
func_22879 = relay.Function([var_22875,var_22876,var_22877,var_22878,], output)
mutated_mod['func_22879'] = func_22879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16861_call = mod.get_global_var('func_16861')
func_16862_call = mutated_mod.get_global_var('func_16862')
call_22972 = relay.TupleGetItem(func_16861_call(), 0)
call_22973 = relay.TupleGetItem(func_16862_call(), 0)
func_22480_call = mod.get_global_var('func_22480')
func_22481_call = mutated_mod.get_global_var('func_22481')
call_22984 = relay.TupleGetItem(func_22480_call(), 1)
call_22985 = relay.TupleGetItem(func_22481_call(), 1)
func_21830_call = mod.get_global_var('func_21830')
func_21832_call = mutated_mod.get_global_var('func_21832')
call_23034 = relay.TupleGetItem(func_21830_call(), 1)
call_23035 = relay.TupleGetItem(func_21832_call(), 1)
output = relay.Tuple([call_22972,call_22984,call_23034,])
output2 = relay.Tuple([call_22973,call_22985,call_23035,])
func_23037 = relay.Function([], output)
mod['func_23037'] = func_23037
mod = relay.transform.InferType()(mod)
mutated_mod['func_23037'] = func_23037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23037_call = mutated_mod.get_global_var('func_23037')
call_23038 = func_23037_call()
output = call_23038
func_23039 = relay.Function([], output)
mutated_mod['func_23039'] = func_23039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18212_call = mod.get_global_var('func_18212')
func_18214_call = mutated_mod.get_global_var('func_18214')
call_23050 = relay.TupleGetItem(func_18212_call(), 0)
call_23051 = relay.TupleGetItem(func_18214_call(), 0)
var_23057 = relay.var("var_23057", dtype = "float32", shape = (4, 1, 5))#candidate|23057|(4, 1, 5)|var|float32
bop_23058 = relay.minimum(call_23050.astype('float64'), relay.reshape(var_23057.astype('float64'), relay.shape_of(call_23050))) # shape=(4, 1, 5)
bop_23061 = relay.minimum(call_23051.astype('float64'), relay.reshape(var_23057.astype('float64'), relay.shape_of(call_23051))) # shape=(4, 1, 5)
uop_23067 = relay.sin(call_23050.astype('float32')) # shape=(4, 1, 5)
uop_23069 = relay.sin(call_23051.astype('float32')) # shape=(4, 1, 5)
bop_23071 = relay.multiply(bop_23058.astype('uint16'), relay.reshape(var_23057.astype('uint16'), relay.shape_of(bop_23058))) # shape=(4, 1, 5)
bop_23074 = relay.multiply(bop_23061.astype('uint16'), relay.reshape(var_23057.astype('uint16'), relay.shape_of(bop_23061))) # shape=(4, 1, 5)
output = relay.Tuple([uop_23067,bop_23071,])
output2 = relay.Tuple([uop_23069,bop_23074,])
func_23085 = relay.Function([var_23057,], output)
mod['func_23085'] = func_23085
mod = relay.transform.InferType()(mod)
var_23086 = relay.var("var_23086", dtype = "float32", shape = (4, 1, 5))#candidate|23086|(4, 1, 5)|var|float32
output = func_23085(var_23086)
func_23087 = relay.Function([var_23086], output)
mutated_mod['func_23087'] = func_23087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15422_call = mod.get_global_var('func_15422')
func_15424_call = mutated_mod.get_global_var('func_15424')
call_23198 = relay.TupleGetItem(func_15422_call(), 0)
call_23199 = relay.TupleGetItem(func_15424_call(), 0)
output = relay.Tuple([call_23198,])
output2 = relay.Tuple([call_23199,])
func_23200 = relay.Function([], output)
mod['func_23200'] = func_23200
mod = relay.transform.InferType()(mod)
mutated_mod['func_23200'] = func_23200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23200_call = mutated_mod.get_global_var('func_23200')
call_23201 = func_23200_call()
output = call_23201
func_23202 = relay.Function([], output)
mutated_mod['func_23202'] = func_23202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22362_call = mod.get_global_var('func_22362')
func_22363_call = mutated_mod.get_global_var('func_22363')
call_23203 = relay.TupleGetItem(func_22362_call(), 0)
call_23204 = relay.TupleGetItem(func_22363_call(), 0)
func_16840_call = mod.get_global_var('func_16840')
func_16842_call = mutated_mod.get_global_var('func_16842')
call_23220 = func_16840_call()
call_23221 = func_16840_call()
output = relay.Tuple([call_23203,call_23220,])
output2 = relay.Tuple([call_23204,call_23221,])
func_23238 = relay.Function([], output)
mod['func_23238'] = func_23238
mod = relay.transform.InferType()(mod)
mutated_mod['func_23238'] = func_23238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23238_call = mutated_mod.get_global_var('func_23238')
call_23239 = func_23238_call()
output = call_23239
func_23240 = relay.Function([], output)
mutated_mod['func_23240'] = func_23240
mutated_mod = relay.transform.InferType()(mutated_mod)
var_23297 = relay.var("var_23297", dtype = "float64", shape = (2, 3, 11))#candidate|23297|(2, 3, 11)|var|float64
uop_23298 = relay.acosh(var_23297.astype('float64')) # shape=(2, 3, 11)
output = uop_23298
output2 = uop_23298
func_23300 = relay.Function([var_23297,], output)
mod['func_23300'] = func_23300
mod = relay.transform.InferType()(mod)
mutated_mod['func_23300'] = func_23300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_23301 = relay.var("var_23301", dtype = "float64", shape = (2, 3, 11))#candidate|23301|(2, 3, 11)|var|float64
func_23300_call = mutated_mod.get_global_var('func_23300')
call_23302 = func_23300_call(var_23301)
output = call_23302
func_23303 = relay.Function([var_23301], output)
mutated_mod['func_23303'] = func_23303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_23326 = relay.TupleGetItem(func_15484_call(), 0)
call_23327 = relay.TupleGetItem(func_15485_call(), 0)
func_21045_call = mod.get_global_var('func_21045')
func_21048_call = mutated_mod.get_global_var('func_21048')
var_23380 = relay.var("var_23380", dtype = "float32", shape = ())#candidate|23380|()|var|float32
var_23381 = relay.var("var_23381", dtype = "float32", shape = (588,))#candidate|23381|(588,)|var|float32
call_23379 = relay.TupleGetItem(func_21045_call(relay.reshape(var_23380.astype('float32'), []), relay.reshape(var_23381.astype('float32'), [588,]), ), 1)
call_23382 = relay.TupleGetItem(func_21048_call(relay.reshape(var_23380.astype('float32'), []), relay.reshape(var_23381.astype('float32'), [588,]), ), 1)
func_15622_call = mod.get_global_var('func_15622')
func_15623_call = mutated_mod.get_global_var('func_15623')
call_23391 = func_15622_call()
call_23392 = func_15622_call()
func_17977_call = mod.get_global_var('func_17977')
func_17979_call = mutated_mod.get_global_var('func_17979')
call_23399 = relay.TupleGetItem(func_17977_call(), 0)
call_23400 = relay.TupleGetItem(func_17979_call(), 0)
output = relay.Tuple([call_23326,call_23379,var_23380,var_23381,call_23391,call_23399,])
output2 = relay.Tuple([call_23327,call_23382,var_23380,var_23381,call_23392,call_23400,])
func_23404 = relay.Function([var_23380,var_23381,], output)
mod['func_23404'] = func_23404
mod = relay.transform.InferType()(mod)
mutated_mod['func_23404'] = func_23404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23404_call = mutated_mod.get_global_var('func_23404')
var_23406 = relay.var("var_23406", dtype = "float32", shape = ())#candidate|23406|()|var|float32
var_23407 = relay.var("var_23407", dtype = "float32", shape = (588,))#candidate|23407|(588,)|var|float32
call_23405 = func_23404_call(var_23406,var_23407,)
output = call_23405
func_23408 = relay.Function([var_23406,var_23407,], output)
mutated_mod['func_23408'] = func_23408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18089_call = mod.get_global_var('func_18089')
func_18091_call = mutated_mod.get_global_var('func_18091')
call_23442 = func_18089_call()
call_23443 = func_18089_call()
output = relay.Tuple([call_23442,])
output2 = relay.Tuple([call_23443,])
func_23448 = relay.Function([], output)
mod['func_23448'] = func_23448
mod = relay.transform.InferType()(mod)
output = func_23448()
func_23449 = relay.Function([], output)
mutated_mod['func_23449'] = func_23449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15508_call = mod.get_global_var('func_15508')
func_15510_call = mutated_mod.get_global_var('func_15510')
call_23504 = relay.TupleGetItem(func_15508_call(), 0)
call_23505 = relay.TupleGetItem(func_15510_call(), 0)
func_10598_call = mod.get_global_var('func_10598')
func_10601_call = mutated_mod.get_global_var('func_10601')
var_23523 = relay.var("var_23523", dtype = "int64", shape = (360,))#candidate|23523|(360,)|var|int64
call_23522 = relay.TupleGetItem(func_10598_call(relay.reshape(var_23523.astype('int64'), [6, 6, 10]), relay.reshape(var_23523.astype('int64'), [6, 6, 10]), ), 3)
call_23524 = relay.TupleGetItem(func_10601_call(relay.reshape(var_23523.astype('int64'), [6, 6, 10]), relay.reshape(var_23523.astype('int64'), [6, 6, 10]), ), 3)
output = relay.Tuple([call_23504,call_23522,var_23523,])
output2 = relay.Tuple([call_23505,call_23524,var_23523,])
func_23528 = relay.Function([var_23523,], output)
mod['func_23528'] = func_23528
mod = relay.transform.InferType()(mod)
mutated_mod['func_23528'] = func_23528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_23529 = relay.var("var_23529", dtype = "int64", shape = (360,))#candidate|23529|(360,)|var|int64
func_23528_call = mutated_mod.get_global_var('func_23528')
call_23530 = func_23528_call(var_23529)
output = call_23530
func_23531 = relay.Function([var_23529], output)
mutated_mod['func_23531'] = func_23531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16385_call = mod.get_global_var('func_16385')
func_16386_call = mutated_mod.get_global_var('func_16386')
call_23544 = relay.TupleGetItem(func_16385_call(), 4)
call_23545 = relay.TupleGetItem(func_16386_call(), 4)
output = relay.Tuple([call_23544,])
output2 = relay.Tuple([call_23545,])
func_23552 = relay.Function([], output)
mod['func_23552'] = func_23552
mod = relay.transform.InferType()(mod)
mutated_mod['func_23552'] = func_23552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23552_call = mutated_mod.get_global_var('func_23552')
call_23553 = func_23552_call()
output = call_23553
func_23554 = relay.Function([], output)
mutated_mod['func_23554'] = func_23554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21264_call = mod.get_global_var('func_21264')
func_21265_call = mutated_mod.get_global_var('func_21265')
call_23565 = func_21264_call()
call_23566 = func_21264_call()
output = relay.Tuple([call_23565,])
output2 = relay.Tuple([call_23566,])
func_23600 = relay.Function([], output)
mod['func_23600'] = func_23600
mod = relay.transform.InferType()(mod)
output = func_23600()
func_23601 = relay.Function([], output)
mutated_mod['func_23601'] = func_23601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20188_call = mod.get_global_var('func_20188')
func_20189_call = mutated_mod.get_global_var('func_20189')
call_23657 = relay.TupleGetItem(func_20188_call(), 0)
call_23658 = relay.TupleGetItem(func_20189_call(), 0)
func_12124_call = mod.get_global_var('func_12124')
func_12129_call = mutated_mod.get_global_var('func_12129')
var_23675 = relay.var("var_23675", dtype = "float32", shape = (210,))#candidate|23675|(210,)|var|float32
const_23676 = relay.const([-1,-2,-4,-8,-10,2,7,6,-8,-10,-6,-5,-7,-10,-2,6,6,4,1,-10,8,-6,-5,10,7,-10,-10,-1,-5,9,-2,5,-7,7,-10,-10,-2,7,9,1,-7,1,8,-4,1,-2,-2,-4,-5,6,-9,-6,-1,6,-10,7,2,5,-10,-4,-6,-5,-5,-5,9,8,6,-6,-8,-8,-3,-6,-3,-4,-1,3,5,6,-8,-2,2,4,5,6,6,2,1,4,-8,-6,-7,8,10,5,7,-6,7,-9,-3,4,1,9,-3,-3,-3,3,1,-3,-7,8,6,-5,5,5,-8,-5,6,-8,-7,9,-3,10,-6,-4,3,-7,5,2,-3,-8,-8,2,9,1,3,7,-4,2,2,-3,8,-6,1,5,-6,6,7,8,-10,-3,-2,-10,7,-6,-8,6,10,-8,-1,-6,-7,-1,-2,10,9,-4,-4,-9,8,10,6,-1,7,7,4,4,-8,6,5,4,1,-7,4,-6,1,6,9,6,-7,-3,-8,4,2,-10,8,-3,1,8,5,-6,7,6,1,3,4,-1,-2,2,5,-3,3,-5,-5,8,6,-8,9,-2,-5,2,-10,-4,8,-6,-8,-9,4,-5,-9,-1,-10,10,3,2,7,-9,-7,-1,1,-1,6,-9,-7,1,9,3,-3,1,-4,-3,-6,-10,-5,1,8,-4,5,-9,2,-10,-4,-2,-5,2,-5,2,7,-6,3,-8,-3,-9,10,1,-10,2,-4,-10,5,-8,-6,4,2,-6,1,-8,-10,3,7,-9,4,10,6,-7,-1,-3,-5,2,9,4,4,2,-1,4,-10,-2,6,4,-1,5,4,-2,-5,6,-2,1,4,-2,10,-2,8,-5,-7,8,-8,3,1,2,-10,9,3,-2,5,2,7,-6,-2,-1,9,-9,10,-2,-7,-8,-7,3,-9,4,6,-1,-4,9,-9,-4,-10,7,7,3,-6,-5,8,-10,10,2,2,10,-10,1,-9,-8,-10,-1,4,4,-6,2,6,2,-6,3,-6,3,2,-5,-10,2,-10,10,-10,6,3,10,8,7,-6,1,3,-10,-7,-10,10,9,-6,3,-5,-1,-5,-8,-3,-6,-7,-1,-10,-7,-3,-7,8,2,7,9,-4,-8,9,3,-3,1,7,-10,10,-5,-4,-8,8,-6,7,5,-6,-2,3,9,8,7,1,-2,7,-5,-2,3,5,5,5,-3,6,-7,3,-6,5,6,-3,6,8,2,8,-9,7,5,5,4,-5,2,-5,1,-2,-6,5,-8,7,2,7,6,-7,-7,-1,6,4,-6,-6,10,3,-6,10,-3,4,-10,-1,5,9,2,7,-6,6,9,-8,-2,5,-1,-2,1,4,-6,-10,-2,-7,1,-2,2,-10,10,1,10,9,-2,10,6,-7,-8,5,7,4,-3,-6,2,7,-5,3,-4,-9,-5,2,-2,4,-7,9,1,4,10,9,8,-6,-6,-6,-3,-9,-3,-10,1,6,4,-3,-1,-7,9,-4,3,7,1,2,-10,2,1,2,-9,9,4,-6,-1,7,-2,6,-3,7,-8,-9,7,6,7,-1,4,8,1,4,-1,-3,-6,-8,-4,4,-1,2,6,9,4,10,7,-8,3,4,7,-7,-4,3,-2,-10,1,5,10,1,-2,-3,-8,-1,7,7,1,-6,-2,5,-5,9,8,3,7,-1,-4,8,-9,5,4,-9,-7,-2,-5,5,1,-8,-7,7,7,-3,-6,5,1,9,-3,10,7,-10,-8,-4,8,-10,-7,9,6,-4,-2,-6,-8,-10,-5,-2,-2,-7,-7,1,-5,10,-5,5,-2,4,8,9,-6,1,-9,6,-5,-4,-3,8,4,-1,1,-2,5,-9,5,10,-6,3,-4,-9,-9,1,-5,-2,-1,10,9,4,-8,-8,10,-4,-1,-4,-3,3,-5,8,5,9,-4,-9,10,8,6,-1,-4,-7,-10,-9,5,9,-8,9,8,9,-6,-7,-2,4,-1,-8,-10,1,5,6,-3,7,-3,-5,4,-3,4,9,-4,-6,10,1,9,3,-1,-2,-4,-4,-7,8,-4,-4,-2,4,5,-1,4,-6,-2,-6,10,7,-9,2,9,9,-10,10,3,-8,-4,5,2,10,2,9,4,-7,7,10,9,7,-2,3,-1,-4,-1,4,2,-9,9,-6,4,-9,3,6,9,-1,-10,-6,5,-9,-9,-4,-6,5,3,-2,7,7,-1,1,-6,-10,-7,1,-6,-10,3,8,-7,9,-8,-8,-2,-4,9,2,-8,-6,-9,-6,-9,-2,2,-4,-4,-10,5,7,2,10,-7,-9,-5,9,-1,-10,5,3,-5,8,-1,2,-6,-5,2,-10,-8,-5,1,8,3,2,-4,-7,1,8,4,10,-1,-8,10,4,-8,-2,3,1,-10,3,-8,-10,-6,3,-8,-9,7,4,7,5,6,-4,-7,-6,10,10,-2,6,-9,-9,1,-8,7,-6,-1,-10,8,6,1,-2,-1,-10,3,10,-5,10,7,4,3,10,1,-9,-6,-4,-8,9,-1,2,-4,-7,-3,5,-7,6,9,2,-6,8,-7,-10,-3,4,-7,-9,1,2,-2,-6,7,7,-7,-7,1,4,10,-4,-4,-8,-7,4,10,3,-4,-1,8,9,8,-8,-1,-10,8,-7,-4,-3,-9,-8,4,3,10,-1,1,-4,5,-9,-6,-1,-10,-7,3,-5,9,-3,9,-1,1,7,-1,10,-3,-6,5,3,8,-2,-10,-3,-4,-1,4,2,-3,7,10,-2,6,3,-9,-1,-6,8,-1,6,9,10,7,-1,9,-6,7,3,8,-7,2,-4,10,-6,-2,8,-8,-9,8,-5,7,-7,9,-8,-4,6,2,4,-3,-2,-1,-8,-9,-3,-6,6,-2,-10,3,-2,4,2,-9,7,-7,6,-1,8,-1,9,-3,-1,-7,10,8,6,-9,7,5,1,-4,3,-1,-5,3,-8,-8,3,-7,-5,4,-6,-10,-2,-6,10,-8,-3,-3,1,-2,-4,5,6,-10,-8,2,7,6,8,2,2,-8,-1,7,9,-9,10,2,-10,6,-7,2,10,-3,2,6,-5,2,7,6,-7,-3,-2,4,7,10,8,-8,-1,-9,-4,8,-1,-5,-10,-6,-7,5,-4,-3,-8,-3,-8,7,1,4,-10,7,3,-10,5,1,5,-3,-2,9,1,6,-4,9,-8,-3,7,10,5,4,-7,4,-8,2,5,-2,5,8,-3,-7,1,-1,-1,10,-2,8,7,1,8,9,-3,2,1,7,10,-6,5,1,8,-4,6,-10,-1,-10,2,-4,10,-5,7,-6,-8,-8,-10,9,-10,10,2,-9,-9,-3,10,-8,-5,-5,6,9,-2,7,8,9,6,4,-9,4,-5,1,-6,10,-3,-4,-4,5,2,7,-5,-7,-6,-2,5,-3,2,-8,4,-10,10,-7,6,10,1,7,-4,8,7,-6,-5,5,-4,6,8,4,9,-2,-1,-5,10,8,-8,7,-6,2,-4,9,-9,-6,2,-4,-9,-7,9,-3,-6,6,-9,1,-7,-9,9,9,-6,4,-4,10,-7,4,-9,-6,1,-8,4,-10,-4,2,-8,3,5,-3,-8,-2,7,2,4,10,-1,-8,10,7,-6,1,-9,9,4,5,-2,-6,3,-7,-7,2,5,-2,-7,-3,8,-6,-8,3,6,3,-4,-7,8,-6,10,2,10,-2,-3,-8,9,-9,1,-9,1,5,1,-4,5,-6,10,2,-2,-4,1,7,10,-7], dtype = "int16")#candidate|23676|(1404,)|const|int16
var_23677 = relay.var("var_23677", dtype = "float32", shape = (220,))#candidate|23677|(220,)|var|float32
const_23678 = relay.const([[-1,7,6,-9,4,-5,8,3,-9,6,-4,2,2,-4,10,-5,7,-7,1,-9,-1,6,-10,-3,-8,3,-6,5,-9,-9,5,1,7,-6,-4,-3,-1,6,10,10,-10,9,-8,-8,-1,7,10,-7,-8,5,-8,-6,-9,-10,-4,6,3,-2,8,-9,4,7,6,10,7,-3,-6,-3,3,-4,4,-3,-3,-10,-4,4,-7,-3],[-4,-4,-8,7,-9,-9,-6,1,2,6,8,10,7,1,4,-6,7,-1,-10,-9,1,-3,-2,6,10,-1,10,-2,3,2,7,6,-9,-9,5,9,-7,-2,9,-2,10,1,3,6,9,5,-7,8,-8,-6,-4,-1,-9,9,-1,-1,4,-10,5,5,5,10,1,-7,-6,5,9,-2,-1,8,-3,4,1,6,-3,2,1,9],[1,-2,-2,-8,5,1,10,-1,-8,-2,-2,-5,-7,2,-8,-1,-10,5,-2,-2,10,6,-3,-4,-1,-10,-5,7,-3,-2,-3,-9,10,4,4,10,9,7,-2,-5,-9,5,1,6,2,-4,-4,7,-6,5,-6,5,10,9,2,4,-10,-5,-2,4,10,-8,-2,8,5,7,8,-9,3,10,-6,7,5,7,-5,-3,3,-1],[8,1,3,-7,10,-1,7,-8,-8,-9,9,2,10,-10,1,-8,-3,4,-8,8,10,1,-1,-10,-6,-1,8,-10,1,1,-5,2,-9,5,1,7,3,9,-9,-10,-2,3,-6,-8,4,10,-10,9,-3,9,8,-5,6,-4,5,-9,6,-4,-6,1,4,1,-6,-7,3,-2,4,1,-1,2,-8,2,-4,6,1,-9,-1,-8],[1,5,-1,-4,-6,4,9,-3,8,2,-2,-3,-6,-5,-5,3,10,9,-6,-8,-9,10,-8,-6,8,2,6,10,-8,-8,-10,8,-10,-3,1,1,-6,9,-3,4,-2,-9,10,10,-6,10,3,8,-4,-2,-6,4,-5,8,7,-9,-8,7,10,5,-8,-4,4,4,4,-4,2,-2,2,-5,2,8,-4,8,-2,4,10,1],[-9,-4,5,-3,8,2,-7,-9,-2,-9,-9,2,1,-1,3,7,-9,5,10,10,7,-8,-8,-3,3,7,-10,1,-5,4,-6,-10,-3,8,-6,3,-10,-6,-7,1,1,-2,-6,-4,-7,1,-9,-8,-9,-6,-5,-8,10,-3,3,9,-1,8,-5,-2,-9,8,5,10,2,-1,-5,-10,-3,1,9,3,-2,9,1,2,6,10],[3,7,6,-2,5,5,9,5,8,7,-8,9,-10,1,-10,7,-3,-1,-10,-9,7,4,-1,-3,8,-1,8,8,-1,-2,-2,-6,-1,3,10,-8,-5,2,-5,7,4,-10,9,10,6,3,-1,2,-6,7,6,-4,10,-9,10,8,5,8,-7,8,-2,-3,1,-7,10,-2,9,-9,1,-6,3,5,-6,-6,3,6,4,-8]], dtype = "int64")#candidate|23678|(7, 78)|const|int64
call_23674 = relay.TupleGetItem(func_12124_call(relay.reshape(var_23675.astype('float32'), [3, 7, 10]), relay.reshape(const_23676.astype('int16'), [9, 156]), relay.reshape(var_23677.astype('float32'), [220,]), relay.reshape(const_23678.astype('int64'), [546,]), ), 4)
call_23679 = relay.TupleGetItem(func_12129_call(relay.reshape(var_23675.astype('float32'), [3, 7, 10]), relay.reshape(const_23676.astype('int16'), [9, 156]), relay.reshape(var_23677.astype('float32'), [220,]), relay.reshape(const_23678.astype('int64'), [546,]), ), 4)
uop_23697 = relay.atan(var_23677.astype('float32')) # shape=(220,)
func_20229_call = mod.get_global_var('func_20229')
func_20231_call = mutated_mod.get_global_var('func_20231')
call_23701 = relay.TupleGetItem(func_20229_call(), 0)
call_23702 = relay.TupleGetItem(func_20231_call(), 0)
output = relay.Tuple([call_23657,call_23674,var_23675,const_23676,const_23678,uop_23697,call_23701,])
output2 = relay.Tuple([call_23658,call_23679,var_23675,const_23676,const_23678,uop_23697,call_23702,])
func_23703 = relay.Function([var_23675,var_23677,], output)
mod['func_23703'] = func_23703
mod = relay.transform.InferType()(mod)
var_23704 = relay.var("var_23704", dtype = "float32", shape = (210,))#candidate|23704|(210,)|var|float32
var_23705 = relay.var("var_23705", dtype = "float32", shape = (220,))#candidate|23705|(220,)|var|float32
output = func_23703(var_23704,var_23705,)
func_23706 = relay.Function([var_23704,var_23705,], output)
mutated_mod['func_23706'] = func_23706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16865_call = mod.get_global_var('func_16865')
func_16867_call = mutated_mod.get_global_var('func_16867')
call_23736 = relay.TupleGetItem(func_16865_call(), 0)
call_23737 = relay.TupleGetItem(func_16867_call(), 0)
func_18515_call = mod.get_global_var('func_18515')
func_18516_call = mutated_mod.get_global_var('func_18516')
call_23746 = relay.TupleGetItem(func_18515_call(), 1)
call_23747 = relay.TupleGetItem(func_18516_call(), 1)
output = relay.Tuple([call_23736,call_23746,])
output2 = relay.Tuple([call_23737,call_23747,])
func_23765 = relay.Function([], output)
mod['func_23765'] = func_23765
mod = relay.transform.InferType()(mod)
mutated_mod['func_23765'] = func_23765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23765_call = mutated_mod.get_global_var('func_23765')
call_23766 = func_23765_call()
output = call_23766
func_23767 = relay.Function([], output)
mutated_mod['func_23767'] = func_23767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15484_call = mod.get_global_var('func_15484')
func_15485_call = mutated_mod.get_global_var('func_15485')
call_23812 = relay.TupleGetItem(func_15484_call(), 0)
call_23813 = relay.TupleGetItem(func_15485_call(), 0)
output = call_23812
output2 = call_23813
func_23829 = relay.Function([], output)
mod['func_23829'] = func_23829
mod = relay.transform.InferType()(mod)
output = func_23829()
func_23830 = relay.Function([], output)
mutated_mod['func_23830'] = func_23830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21549_call = mod.get_global_var('func_21549')
func_21550_call = mutated_mod.get_global_var('func_21550')
call_23836 = func_21549_call()
call_23837 = func_21549_call()
func_20214_call = mod.get_global_var('func_20214')
func_20215_call = mutated_mod.get_global_var('func_20215')
call_23842 = relay.TupleGetItem(func_20214_call(), 0)
call_23843 = relay.TupleGetItem(func_20215_call(), 0)
output = relay.Tuple([call_23836,call_23842,])
output2 = relay.Tuple([call_23837,call_23843,])
func_23850 = relay.Function([], output)
mod['func_23850'] = func_23850
mod = relay.transform.InferType()(mod)
output = func_23850()
func_23851 = relay.Function([], output)
mutated_mod['func_23851'] = func_23851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21953_call = mod.get_global_var('func_21953')
func_21955_call = mutated_mod.get_global_var('func_21955')
call_23913 = relay.TupleGetItem(func_21953_call(), 3)
call_23914 = relay.TupleGetItem(func_21955_call(), 3)
func_23829_call = mod.get_global_var('func_23829')
func_23830_call = mutated_mod.get_global_var('func_23830')
call_23928 = func_23829_call()
call_23929 = func_23829_call()
output = relay.Tuple([call_23913,call_23928,])
output2 = relay.Tuple([call_23914,call_23929,])
func_23933 = relay.Function([], output)
mod['func_23933'] = func_23933
mod = relay.transform.InferType()(mod)
mutated_mod['func_23933'] = func_23933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23933_call = mutated_mod.get_global_var('func_23933')
call_23934 = func_23933_call()
output = call_23934
func_23935 = relay.Function([], output)
mutated_mod['func_23935'] = func_23935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20327_call = mod.get_global_var('func_20327')
func_20329_call = mutated_mod.get_global_var('func_20329')
call_23973 = func_20327_call()
call_23974 = func_20327_call()
func_19096_call = mod.get_global_var('func_19096')
func_19097_call = mutated_mod.get_global_var('func_19097')
call_23980 = func_19096_call()
call_23981 = func_19096_call()
output = relay.Tuple([call_23973,call_23980,])
output2 = relay.Tuple([call_23974,call_23981,])
func_23992 = relay.Function([], output)
mod['func_23992'] = func_23992
mod = relay.transform.InferType()(mod)
mutated_mod['func_23992'] = func_23992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23992_call = mutated_mod.get_global_var('func_23992')
call_23993 = func_23992_call()
output = call_23993
func_23994 = relay.Function([], output)
mutated_mod['func_23994'] = func_23994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23992_call = mod.get_global_var('func_23992')
func_23994_call = mutated_mod.get_global_var('func_23994')
call_24049 = relay.TupleGetItem(func_23992_call(), 0)
call_24050 = relay.TupleGetItem(func_23994_call(), 0)
func_14253_call = mod.get_global_var('func_14253')
func_14254_call = mutated_mod.get_global_var('func_14254')
call_24072 = relay.TupleGetItem(func_14253_call(), 0)
call_24073 = relay.TupleGetItem(func_14254_call(), 0)
output = relay.Tuple([call_24049,call_24072,])
output2 = relay.Tuple([call_24050,call_24073,])
func_24089 = relay.Function([], output)
mod['func_24089'] = func_24089
mod = relay.transform.InferType()(mod)
output = func_24089()
func_24090 = relay.Function([], output)
mutated_mod['func_24090'] = func_24090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16958_call = mod.get_global_var('func_16958')
func_16959_call = mutated_mod.get_global_var('func_16959')
call_24106 = func_16958_call()
call_24107 = func_16958_call()
output = call_24106
output2 = call_24107
func_24109 = relay.Function([], output)
mod['func_24109'] = func_24109
mod = relay.transform.InferType()(mod)
mutated_mod['func_24109'] = func_24109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24109_call = mutated_mod.get_global_var('func_24109')
call_24110 = func_24109_call()
output = call_24110
func_24111 = relay.Function([], output)
mutated_mod['func_24111'] = func_24111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20947_call = mod.get_global_var('func_20947')
func_20949_call = mutated_mod.get_global_var('func_20949')
call_24122 = relay.TupleGetItem(func_20947_call(), 0)
call_24123 = relay.TupleGetItem(func_20949_call(), 0)
output = relay.Tuple([call_24122,])
output2 = relay.Tuple([call_24123,])
func_24144 = relay.Function([], output)
mod['func_24144'] = func_24144
mod = relay.transform.InferType()(mod)
mutated_mod['func_24144'] = func_24144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24144_call = mutated_mod.get_global_var('func_24144')
call_24145 = func_24144_call()
output = call_24145
func_24146 = relay.Function([], output)
mutated_mod['func_24146'] = func_24146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16958_call = mod.get_global_var('func_16958')
func_16959_call = mutated_mod.get_global_var('func_16959')
call_24180 = func_16958_call()
call_24181 = func_16958_call()
output = call_24180
output2 = call_24181
func_24196 = relay.Function([], output)
mod['func_24196'] = func_24196
mod = relay.transform.InferType()(mod)
mutated_mod['func_24196'] = func_24196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24196_call = mutated_mod.get_global_var('func_24196')
call_24197 = func_24196_call()
output = call_24197
func_24198 = relay.Function([], output)
mutated_mod['func_24198'] = func_24198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14709_call = mod.get_global_var('func_14709')
func_14711_call = mutated_mod.get_global_var('func_14711')
call_24221 = func_14709_call()
call_24222 = func_14709_call()
func_22570_call = mod.get_global_var('func_22570')
func_22573_call = mutated_mod.get_global_var('func_22573')
var_24232 = relay.var("var_24232", dtype = "float64", shape = (96,))#candidate|24232|(96,)|var|float64
call_24231 = relay.TupleGetItem(func_22570_call(relay.reshape(var_24232.astype('float64'), [96,])), 2)
call_24233 = relay.TupleGetItem(func_22573_call(relay.reshape(var_24232.astype('float64'), [96,])), 2)
func_16719_call = mod.get_global_var('func_16719')
func_16720_call = mutated_mod.get_global_var('func_16720')
call_24248 = relay.TupleGetItem(func_16719_call(), 0)
call_24249 = relay.TupleGetItem(func_16720_call(), 0)
func_23085_call = mod.get_global_var('func_23085')
func_23087_call = mutated_mod.get_global_var('func_23087')
const_24251 = relay.const([[-8.036280],[-8.124265],[-8.272730],[8.078127],[-1.014336],[4.820919],[4.755744],[-6.951393],[8.219023],[8.803560],[-8.970876],[1.749026],[7.120789],[9.963598],[0.521628],[8.443768],[-2.186769],[-6.696708],[-4.269030],[0.645539]], dtype = "float32")#candidate|24251|(20, 1)|const|float32
call_24250 = relay.TupleGetItem(func_23085_call(relay.reshape(const_24251.astype('float32'), [4, 1, 5])), 1)
call_24252 = relay.TupleGetItem(func_23087_call(relay.reshape(const_24251.astype('float32'), [4, 1, 5])), 1)
func_19319_call = mod.get_global_var('func_19319')
func_19320_call = mutated_mod.get_global_var('func_19320')
call_24257 = func_19319_call()
call_24258 = func_19319_call()
output = relay.Tuple([call_24221,call_24231,var_24232,call_24248,call_24250,const_24251,call_24257,])
output2 = relay.Tuple([call_24222,call_24233,var_24232,call_24249,call_24252,const_24251,call_24258,])
func_24265 = relay.Function([var_24232,], output)
mod['func_24265'] = func_24265
mod = relay.transform.InferType()(mod)
var_24266 = relay.var("var_24266", dtype = "float64", shape = (96,))#candidate|24266|(96,)|var|float64
output = func_24265(var_24266)
func_24267 = relay.Function([var_24266], output)
mutated_mod['func_24267'] = func_24267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20118_call = mod.get_global_var('func_20118')
func_20119_call = mutated_mod.get_global_var('func_20119')
call_24269 = func_20118_call()
call_24270 = func_20118_call()
output = call_24269
output2 = call_24270
func_24293 = relay.Function([], output)
mod['func_24293'] = func_24293
mod = relay.transform.InferType()(mod)
mutated_mod['func_24293'] = func_24293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24293_call = mutated_mod.get_global_var('func_24293')
call_24294 = func_24293_call()
output = call_24294
func_24295 = relay.Function([], output)
mutated_mod['func_24295'] = func_24295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_24299 = relay.var("var_24299", dtype = "float32", shape = (11, 3, 10))#candidate|24299|(11, 3, 10)|var|float32
var_24300 = relay.var("var_24300", dtype = "float32", shape = (11, 3, 10))#candidate|24300|(11, 3, 10)|var|float32
bop_24301 = relay.less_equal(var_24299.astype('bool'), relay.reshape(var_24300.astype('bool'), relay.shape_of(var_24299))) # shape=(11, 3, 10)
uop_24307 = relay.asinh(var_24300.astype('float32')) # shape=(11, 3, 10)
output = relay.Tuple([bop_24301,uop_24307,])
output2 = relay.Tuple([bop_24301,uop_24307,])
func_24319 = relay.Function([var_24299,var_24300,], output)
mod['func_24319'] = func_24319
mod = relay.transform.InferType()(mod)
mutated_mod['func_24319'] = func_24319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24319_call = mutated_mod.get_global_var('func_24319')
var_24321 = relay.var("var_24321", dtype = "float32", shape = (11, 3, 10))#candidate|24321|(11, 3, 10)|var|float32
var_24322 = relay.var("var_24322", dtype = "float32", shape = (11, 3, 10))#candidate|24322|(11, 3, 10)|var|float32
call_24320 = func_24319_call(var_24321,var_24322,)
output = call_24320
func_24323 = relay.Function([var_24321,var_24322,], output)
mutated_mod['func_24323'] = func_24323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19838_call = mod.get_global_var('func_19838')
func_19839_call = mutated_mod.get_global_var('func_19839')
call_24472 = func_19838_call()
call_24473 = func_19838_call()
output = call_24472
output2 = call_24473
func_24489 = relay.Function([], output)
mod['func_24489'] = func_24489
mod = relay.transform.InferType()(mod)
mutated_mod['func_24489'] = func_24489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24489_call = mutated_mod.get_global_var('func_24489')
call_24490 = func_24489_call()
output = call_24490
func_24491 = relay.Function([], output)
mutated_mod['func_24491'] = func_24491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21830_call = mod.get_global_var('func_21830')
func_21832_call = mutated_mod.get_global_var('func_21832')
call_24571 = relay.TupleGetItem(func_21830_call(), 0)
call_24572 = relay.TupleGetItem(func_21832_call(), 0)
output = relay.Tuple([call_24571,])
output2 = relay.Tuple([call_24572,])
func_24602 = relay.Function([], output)
mod['func_24602'] = func_24602
mod = relay.transform.InferType()(mod)
mutated_mod['func_24602'] = func_24602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24602_call = mutated_mod.get_global_var('func_24602')
call_24603 = func_24602_call()
output = call_24603
func_24604 = relay.Function([], output)
mutated_mod['func_24604'] = func_24604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20859_call = mod.get_global_var('func_20859')
func_20860_call = mutated_mod.get_global_var('func_20860')
call_24673 = func_20859_call()
call_24674 = func_20859_call()
func_15146_call = mod.get_global_var('func_15146')
func_15148_call = mutated_mod.get_global_var('func_15148')
call_24675 = func_15146_call()
call_24676 = func_15146_call()
output = relay.Tuple([call_24673,call_24675,])
output2 = relay.Tuple([call_24674,call_24676,])
func_24685 = relay.Function([], output)
mod['func_24685'] = func_24685
mod = relay.transform.InferType()(mod)
mutated_mod['func_24685'] = func_24685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24685_call = mutated_mod.get_global_var('func_24685')
call_24686 = func_24685_call()
output = call_24686
func_24687 = relay.Function([], output)
mutated_mod['func_24687'] = func_24687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22387_call = mod.get_global_var('func_22387')
func_22389_call = mutated_mod.get_global_var('func_22389')
call_24702 = func_22387_call()
call_24703 = func_22387_call()
output = call_24702
output2 = call_24703
func_24718 = relay.Function([], output)
mod['func_24718'] = func_24718
mod = relay.transform.InferType()(mod)
mutated_mod['func_24718'] = func_24718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24718_call = mutated_mod.get_global_var('func_24718')
call_24719 = func_24718_call()
output = call_24719
func_24720 = relay.Function([], output)
mutated_mod['func_24720'] = func_24720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22102_call = mod.get_global_var('func_22102')
func_22103_call = mutated_mod.get_global_var('func_22103')
call_24730 = relay.TupleGetItem(func_22102_call(), 0)
call_24731 = relay.TupleGetItem(func_22103_call(), 0)
func_20085_call = mod.get_global_var('func_20085')
func_20088_call = mutated_mod.get_global_var('func_20088')
var_24733 = relay.var("var_24733", dtype = "uint32", shape = (420,))#candidate|24733|(420,)|var|uint32
call_24732 = relay.TupleGetItem(func_20085_call(relay.reshape(var_24733.astype('uint32'), [420,])), 0)
call_24734 = relay.TupleGetItem(func_20088_call(relay.reshape(var_24733.astype('uint32'), [420,])), 0)
func_4187_call = mod.get_global_var('func_4187')
func_4189_call = mutated_mod.get_global_var('func_4189')
const_24766 = relay.const([3.956947,-3.051555,-7.061335,9.778044,3.827954,6.368246,2.091965,-2.812077,-0.596897,2.115841,5.853585,9.728529,7.110929,-4.443226,3.398258,3.592622,-2.616934,3.251163,-9.548746,7.108424,6.945796,-0.535663,-5.717043,-3.854228,-1.441834,6.582976,4.463183,7.761259,-4.110022,8.801591,4.238385,-7.534546,-4.051195,-2.205278,-3.669771,0.034104,-7.858050,7.379360,-6.294845,0.379316,8.445183,-8.310528,2.409246,5.366148,-8.149044,7.040930,-7.882417,4.660990,8.014076,1.669613,-4.099456,-1.731760,-2.070185,7.907627,1.827321,2.945050,9.861509,6.393743,-6.696101,-7.526584,-4.364619,-6.857007,5.960767,7.521018,5.288358,6.335881,2.523095,-6.697633,0.458360,9.805857,6.026757,6.106537,-6.296953,9.370042,1.575687,1.918971,-5.422393,-2.138335,-5.925785,-3.343874,-4.130277,4.380038,4.280935,7.758946,3.505076,-4.077688,-7.429254,0.876202,-8.702334,4.365840,-7.098262,7.401634,-2.250026,-8.180942,-3.792024,-6.692961,-1.453664,-7.172627,0.202208,-8.481165], dtype = "float64")#candidate|24766|(100,)|const|float64
call_24765 = relay.TupleGetItem(func_4187_call(relay.reshape(const_24766.astype('float64'), [5, 2, 10])), 1)
call_24767 = relay.TupleGetItem(func_4189_call(relay.reshape(const_24766.astype('float64'), [5, 2, 10])), 1)
func_16817_call = mod.get_global_var('func_16817')
func_16818_call = mutated_mod.get_global_var('func_16818')
call_24775 = relay.TupleGetItem(func_16817_call(), 0)
call_24776 = relay.TupleGetItem(func_16818_call(), 0)
func_20214_call = mod.get_global_var('func_20214')
func_20215_call = mutated_mod.get_global_var('func_20215')
call_24798 = relay.TupleGetItem(func_20214_call(), 0)
call_24799 = relay.TupleGetItem(func_20215_call(), 0)
output = relay.Tuple([call_24730,call_24732,var_24733,call_24765,const_24766,call_24775,call_24798,])
output2 = relay.Tuple([call_24731,call_24734,var_24733,call_24767,const_24766,call_24776,call_24799,])
func_24808 = relay.Function([var_24733,], output)
mod['func_24808'] = func_24808
mod = relay.transform.InferType()(mod)
var_24809 = relay.var("var_24809", dtype = "uint32", shape = (420,))#candidate|24809|(420,)|var|uint32
output = func_24808(var_24809)
func_24810 = relay.Function([var_24809], output)
mutated_mod['func_24810'] = func_24810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23992_call = mod.get_global_var('func_23992')
func_23994_call = mutated_mod.get_global_var('func_23994')
call_24867 = relay.TupleGetItem(func_23992_call(), 0)
call_24868 = relay.TupleGetItem(func_23994_call(), 0)
func_22480_call = mod.get_global_var('func_22480')
func_22481_call = mutated_mod.get_global_var('func_22481')
call_24892 = relay.TupleGetItem(func_22480_call(), 1)
call_24893 = relay.TupleGetItem(func_22481_call(), 1)
func_22255_call = mod.get_global_var('func_22255')
func_22256_call = mutated_mod.get_global_var('func_22256')
call_24911 = func_22255_call()
call_24912 = func_22255_call()
uop_24919 = relay.erf(call_24911.astype('float64')) # shape=(13, 3, 15)
uop_24921 = relay.erf(call_24912.astype('float64')) # shape=(13, 3, 15)
func_17389_call = mod.get_global_var('func_17389')
func_17391_call = mutated_mod.get_global_var('func_17391')
call_24923 = relay.TupleGetItem(func_17389_call(), 0)
call_24924 = relay.TupleGetItem(func_17391_call(), 0)
output = relay.Tuple([call_24867,call_24892,uop_24919,call_24923,])
output2 = relay.Tuple([call_24868,call_24893,uop_24921,call_24924,])
func_24932 = relay.Function([], output)
mod['func_24932'] = func_24932
mod = relay.transform.InferType()(mod)
output = func_24932()
func_24933 = relay.Function([], output)
mutated_mod['func_24933'] = func_24933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_23448_call = mod.get_global_var('func_23448')
func_23449_call = mutated_mod.get_global_var('func_23449')
call_24977 = relay.TupleGetItem(func_23448_call(), 0)
call_24978 = relay.TupleGetItem(func_23449_call(), 0)
func_18658_call = mod.get_global_var('func_18658')
func_18662_call = mutated_mod.get_global_var('func_18662')
const_24980 = relay.const([7,3,10,2,7,-3,6,-1,-8,9,-1,-4,10,4,1,-3,-9,-2,6,-1,2,5,4,2,8,-3,-10,9,10,4,-7,10,3,5,6,2,9,-5,-3,9,10,2,9,-2,5,10,10,9,2,3,-1,-7,2,5,10,-7,-6,-2,10,-3,9,10,3,-5,5,-4,-2,-7,2,-10,-8,7,-5,10,-5,2,-6,5,4,-6,-7,5,1,6,6,10,-4,-9,-5,6,-3,4,-3,-1,-9,5,-7,-7,-2,4,8,3,10,-3,-2,5,-1,7,7,10,4,2,-6,2,2,4,-9,-2,-1,-5,5,-10,-10,10,-2,-5,-6,8,6,9,-5,7,-2,-4,-5,-7,1,-9,-2,-10,9,-1,-2,8,8,-5,-10,6,3,-6,10,-1,9,-2,6,5,5,4,-6,5,-10,6,3,4,3,4,-3,4,4,-3,8,-8,8,2,4,8,8,-6,8,-6,-1,-6,-5,6,-8,10,9,-1,-1,10,2,1,-2,8,-8,2,-5,4,1,-9,-9,7,8,6,2,-5,4,4,-3,-7,-9,10,9,3,-4,-9,3,2,5,-9,5,-1,9,6,-8,-3,-6,-10,-9,-5,7,-7,-1,10,-8,-4,4,-2,3,-7,5,-9,-6,-3,3,-7,3,1,-2,1,3,-3,-1,1,4,-6,-1,9,-3,2,2,8,-1,1,-3,5,10,-2,4,-6,5,-7,-6,-2,1,-6,-3,-10,5,-10,-6,4,-1,-6,2,-5,-3,-1,-1,7,-9,2,-7,-6,4,9,-1,7,-9,-6,6,-8,-4,-7,4,-6,6,4,-2,4,-8,-7,5,-10,-6,5,-10,10,-4,10,10,-10,3,10,8,-1,-6,-3,2,-7,-2,10,-7,-5,-5,8,10,-4,4,6,7,-6,8,5,-5,-8,-9,8,-7,7,-7,-1,-5,-9,8,-10,-5,-7,-8,-2,-7,9,-9,1,9,1,-5,4,-7,8,8,-8,4,5,8,-6,-10,-2], dtype = "uint64")#candidate|24980|(378,)|const|uint64
call_24979 = relay.TupleGetItem(func_18658_call(relay.reshape(const_24980.astype('uint64'), [3, 9, 14]), relay.reshape(const_24980.astype('uint64'), [3, 9, 14]), ), 5)
call_24981 = relay.TupleGetItem(func_18662_call(relay.reshape(const_24980.astype('uint64'), [3, 9, 14]), relay.reshape(const_24980.astype('uint64'), [3, 9, 14]), ), 5)
output = relay.Tuple([call_24977,call_24979,const_24980,])
output2 = relay.Tuple([call_24978,call_24981,const_24980,])
func_24997 = relay.Function([], output)
mod['func_24997'] = func_24997
mod = relay.transform.InferType()(mod)
mutated_mod['func_24997'] = func_24997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24997_call = mutated_mod.get_global_var('func_24997')
call_24998 = func_24997_call()
output = call_24998
func_24999 = relay.Function([], output)
mutated_mod['func_24999'] = func_24999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18576_call = mod.get_global_var('func_18576')
func_18577_call = mutated_mod.get_global_var('func_18577')
call_25015 = func_18576_call()
call_25016 = func_18576_call()
output = relay.Tuple([call_25015,])
output2 = relay.Tuple([call_25016,])
func_25027 = relay.Function([], output)
mod['func_25027'] = func_25027
mod = relay.transform.InferType()(mod)
mutated_mod['func_25027'] = func_25027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25027_call = mutated_mod.get_global_var('func_25027')
call_25028 = func_25027_call()
output = call_25028
func_25029 = relay.Function([], output)
mutated_mod['func_25029'] = func_25029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24602_call = mod.get_global_var('func_24602')
func_24604_call = mutated_mod.get_global_var('func_24604')
call_25052 = relay.TupleGetItem(func_24602_call(), 0)
call_25053 = relay.TupleGetItem(func_24604_call(), 0)
output = relay.Tuple([call_25052,])
output2 = relay.Tuple([call_25053,])
func_25073 = relay.Function([], output)
mod['func_25073'] = func_25073
mod = relay.transform.InferType()(mod)
output = func_25073()
func_25074 = relay.Function([], output)
mutated_mod['func_25074'] = func_25074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_24718_call = mod.get_global_var('func_24718')
func_24720_call = mutated_mod.get_global_var('func_24720')
call_25107 = func_24718_call()
call_25108 = func_24718_call()
output = relay.Tuple([call_25107,])
output2 = relay.Tuple([call_25108,])
func_25116 = relay.Function([], output)
mod['func_25116'] = func_25116
mod = relay.transform.InferType()(mod)
mutated_mod['func_25116'] = func_25116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25116_call = mutated_mod.get_global_var('func_25116')
call_25117 = func_25116_call()
output = call_25117
func_25118 = relay.Function([], output)
mutated_mod['func_25118'] = func_25118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22162_call = mod.get_global_var('func_22162')
func_22163_call = mutated_mod.get_global_var('func_22163')
call_25155 = relay.TupleGetItem(func_22162_call(), 0)
call_25156 = relay.TupleGetItem(func_22163_call(), 0)
func_19013_call = mod.get_global_var('func_19013')
func_19015_call = mutated_mod.get_global_var('func_19015')
var_25160 = relay.var("var_25160", dtype = "int16", shape = (1404,))#candidate|25160|(1404,)|var|int16
call_25159 = relay.TupleGetItem(func_19013_call(relay.reshape(var_25160.astype('int16'), [1404,])), 5)
call_25161 = relay.TupleGetItem(func_19015_call(relay.reshape(var_25160.astype('int16'), [1404,])), 5)
output = relay.Tuple([call_25155,call_25159,var_25160,])
output2 = relay.Tuple([call_25156,call_25161,var_25160,])
func_25162 = relay.Function([var_25160,], output)
mod['func_25162'] = func_25162
mod = relay.transform.InferType()(mod)
mutated_mod['func_25162'] = func_25162
mutated_mod = relay.transform.InferType()(mutated_mod)
var_25163 = relay.var("var_25163", dtype = "int16", shape = (1404,))#candidate|25163|(1404,)|var|int16
func_25162_call = mutated_mod.get_global_var('func_25162')
call_25164 = func_25162_call(var_25163)
output = call_25164
func_25165 = relay.Function([var_25163], output)
mutated_mod['func_25165'] = func_25165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19218_call = mod.get_global_var('func_19218')
func_19219_call = mutated_mod.get_global_var('func_19219')
call_25218 = relay.TupleGetItem(func_19218_call(), 2)
call_25219 = relay.TupleGetItem(func_19219_call(), 2)
func_17738_call = mod.get_global_var('func_17738')
func_17744_call = mutated_mod.get_global_var('func_17744')
var_25221 = relay.var("var_25221", dtype = "int16", shape = (585,))#candidate|25221|(585,)|var|int16
const_25222 = relay.const([3,-3,-8,6,-5,-6,-8,6,9,6,6,-2,5,-4,-1,-1,8,-3,4,-6,-10,3,7,-9,-3,-4,9,9,-10,-2,-3,5,-6,10,8,10,-6,5,-4,10,7,6,2,9,-8,2,3,-5,-8,10,8,-3,5,-8,10,8,-1,-5,-2,4,-9,-1,8,1,10,-1,3,5,-1,1,-2,-3,3,-6,4,5,10,6,-4,3,2,4,-9,-5,3,-2,-5,8,2,-3,7,2,5,-7,-6,-7,-6,4,-2,-4,7,10,10,9,5,10,3,-1,-9,9,9,-4,7,-10,8,-3,-9,-6,4,-5,-1,-3,7,5,4,-5,-10,-10,8,-7,4,-3,7,-4,-7,10,-3,4,-10,-10,-3,-1,-4,1,1,-8,1,7,-3,9,-1,-9,3,-8,10,-1,-3,-5,1,8,-7,-6,10,-4,-8,2,-1,6,2,-1,4,-3,-2,3,-6,7,9,-10,7,-1,-9,4,2,6,-6,4,8,-6,-8,6,-9,-9,-4,-7,-5,8,9,-3,-2,5,-7,7,-10,8,1,4,-4,-10,4,-1,-6,-2,-1,-10,-8,-2,-5,2,1,3,-1,3,10,4,-1,-2,4,-5,-2,7,-9,-7,-7,8,-9,1,8,5,-7,1,-4,8,8,10,-8,10,-5,10,5,9,8,4,-5,-3,8,2,-8,9,-4,8,7,9,-6,-3,6,-7,-3,10,9,-2,-9,10,-7,-5,-9,2,4,7,10,-3,1,3,-8,-4,8,4,2,-5,3,1,7,-10,-5,-9,5,3,1,-2,9,-5,-3,4,-5,6,1,1,-9,6,-6,-10,8,-10,1,9,-7,-7,-5,8,10,-9,-9,8,1,-3,3,-9,9,2,-1,-10,-5,-1,-9,-10,10,1,-10,-9,-7,8,-8,-10,8,8,3,8,-6,8,-7,-6,8,8,6,-6,10,2,-3,-6,6,-10,2,7,-8,-5,3,-6,9,-8,-1,-8,10,-8,4,-4,8,9,4,9,-3,9,-8,-9,-6,1,-3,8,-9,-8,10,3,-8,7,-2,-3,3,-3,4,-7,2,8,7,1,-4,-10,5,-4,10,2,-8,-9,7,-3,5,-1,-7,4,-7,-1,6,-7,7,-3,-3,-8,-1,3,8,-7,7,2,9,8,-1,-6,8,-9,7,1,8,-10,-8,-7,10,-9,-3,10,7,5,5,-6,-9,10,-6,3,-2,-10,-7,-7,2,3,-7,5,-9,1,-6,-8,1,-8,-9,-8,5,1,7,-8,-4,-2,5,6,-2,9,7,10,3,4,10,-5,1,6,4,7,-6,-2,10,7,6,-7,-3,-10,8,10,-5,2,1,-6,-3,-2,5,2,-3,-7,-4,3,-3,4,6,-9,1,8,3,-6,10,7,-1,1,7,4,-2,9,-7,-7,8,-5,-9,-10,1,-9,3,4,-7,9,-1,-5,7,8,-6,-10,-3,5,10,-4,-1,-9,1,10,8,-1,-2,4,8,-5,9,3,10,3,5,-2,4,-1,-7,-4,2,-6,2,4,-5,6,-6,-7,-9,8,-2,10,-2,-3,-6,3,-2,10,2,4,5,-3,-1,9,3,-5,8,10,-8,8,-8,2,2,4,8,-3,-9,3,-7,1,-10,4,4,7,-5,-8,5,-4,1,-3,5,-1,-2,-6,7,-10,8,4,-8,-5,-5,5,-2,7,7,2,7,8,-8,-8,-6,3,-2,3,7,2,-1,-3,8,-6,-1,-8,-2,6,3,-8,-6,-2,-7,8,-2,-7,1,-8,2,-5,4,9,-10,-7,-3,-3,-5,7,9,-7,10,-6,6,10,-9,8,6,9,-6,-2,-3,-8,-7,10,4,9,-3,-5,-10,-8,-7,4,6,3,2,-1,-10,3,5,5,3,3,10,9,-10,1,-3,-3,10,3,1,7,4,-1,7,10,10,10,-1,2,-5,-3,7,9,3,-9,5,-8,-10,-10,2,7,-5,-2,5,2,-6,-8,2,-2,7,-9,-1,-3,-5,8,-7,9,-3,10,6,7,8,9,-1,3,6,2,1,10,2,-1,-4,-1,-5,6,5,-5,9,1,7,-9,7,10,-9,-4,-8,-10,-7,-1,3,6,-9,1,7,7,9,6,-9,6,9,-9,-4,9,-9,6,8,-10,-6,-4,-4,-8,-8,10,3,5,3,8,2,-1,-8,3,-10,4,5,-9,-10,3,-1,5,-7,7,4,-7,3,-7,6,8,4,-2,-1,-7,7,-8,1,6,4,9,-7,4,6,-4,3,8,5,6,2,6,5,10,7,-5,-7,1,-3,-5,-10,1,10,-3,-9,10,4,1,-10,-5,-6,2,-7,9,-9,8,5,3,9,2,-6,-9,8,10,-10,-7,-7,10,-1,1,5,-1,9,8,1,5,-2,-8,2,-10,-2,9,-5,3,-9,-8,-6,-5,-3,2,-2,-1,-9,9,-6,-6,-6,-10,-5,9,-9,-8,-3,9,-5,2,-10,-4,-2,2,1,-8,4,-10,-1,3,-5,3,2,-6,7,-6,10,5,4,10,7,4,6,-2,-2,-4,-4,5,-3,4,-8,4,-2,-8,10,4,5,-1,-2,5,6,1,8,-7,-4,8,3,7,-5,-2,4,2,-3,-8,8,1,5,-5,5,-4,4,2,-8,-3,-6,7,2,-7,4,2,-3,5,2,-10,3,7,-8,5,7,-6,-2,3,2,-2,9,8,8,7,3,-8,-1,-4,-3,-4,4,5,5,-3,-10,-3,9,-9,5,7,-5,-6,10,-7,6,5,-1,9,8,3,5,5,9,10,-1,-2,2,3,8,4,1,-6,-10,10,-5,6,-1,3,-4,-4,10,1,3,-3,-4,-5,-8,9,5,6,2,-9,4,3,-7,-4,2,-8,-9,-8,-7,10,-3,3,-10,-8,-2,7,3,3,8,6,3,7,-2,-9,-7,6,9,9,-10,-2,-6,-10,1,-8,3,9,5,-1,10,-7,8,6,-3,-9,-4,7,1,8,5,9,9,7,3,-10,-8,9,-10,-5,3,-6,-4,6,4,-7,1,8,-5,1,-3,-2,-10,6,9,-3,-7,7,5,7,9,-10,-4,-8,3,9,-4,6,-4,-4,-6,-3,-7,4,-6,-1,9,-3,2,-1,3,-1,-3,-1,-3,-9,-1,2,7,-9,-9,5,-4,10,-2,-8,-3,3,10,-4,-8,-2,7,6,9,6,6,7,-2,3,-10,-2,-2,10,9,-4,6,6,9,-9,7,-8,7,-2,-4,6,8,6,2,-3,-7,10,3,9,9,-10,-3,9,4,10,8,10,3,5,4,-8,5,6,-3,-9,3,9,8,8,1,9,-4,-3,-7,-4,-6,-1,10,10,2,-8,-9,-3,-6,8,-8,7,6,-1,-10,-1,9,9,9,5,-9,8,-9,-6,9,4,-10,3,3,-8,-1,9,-3,9,10,-5,6,-8,2,10,9,-3,5,5,-10,-8,4,-10,10,10,5,10,9,-6,3,4,-10,-8,-3,-2,6,5,-1,-8,6,10,3,3,-9,3,-5,-1,6,-1,-4,1,4,1,-2,-6,-7,10,-8,2,-1,7,-1,-8,-10,5,1,6,-5,3,-8,-6,7,4,8,-3,2,5,-2,2,4,-8,5,-2,-10,8,4,-2,-1,-8,-6,-7,5,-2,7,-9,-1,-3,10,9,-10,10,10,-5,-2,-9,8,-7,-10,-9,2,5,6,10,-5,10,5,-9,3,5,1,-6,-1,-9,1,-7,8,4], dtype = "int16")#candidate|25222|(1404,)|const|int16
var_25223 = relay.var("var_25223", dtype = "int64", shape = (546,))#candidate|25223|(546,)|var|int64
var_25224 = relay.var("var_25224", dtype = "uint64", shape = (12, 3276))#candidate|25224|(12, 3276)|var|uint64
call_25220 = relay.TupleGetItem(func_17738_call(relay.reshape(var_25221.astype('int16'), [13, 3, 15]), relay.reshape(const_25222.astype('int16'), [9, 156]), relay.reshape(var_25223.astype('int64'), [546,]), relay.reshape(var_25224.astype('uint64'), [12, 3276]), ), 5)
call_25225 = relay.TupleGetItem(func_17744_call(relay.reshape(var_25221.astype('int16'), [13, 3, 15]), relay.reshape(const_25222.astype('int16'), [9, 156]), relay.reshape(var_25223.astype('int64'), [546,]), relay.reshape(var_25224.astype('uint64'), [12, 3276]), ), 5)
output = relay.Tuple([call_25218,call_25220,var_25221,const_25222,var_25223,var_25224,])
output2 = relay.Tuple([call_25219,call_25225,var_25221,const_25222,var_25223,var_25224,])
func_25226 = relay.Function([var_25221,var_25223,var_25224,], output)
mod['func_25226'] = func_25226
mod = relay.transform.InferType()(mod)
var_25227 = relay.var("var_25227", dtype = "int16", shape = (585,))#candidate|25227|(585,)|var|int16
var_25228 = relay.var("var_25228", dtype = "int64", shape = (546,))#candidate|25228|(546,)|var|int64
var_25229 = relay.var("var_25229", dtype = "uint64", shape = (12, 3276))#candidate|25229|(12, 3276)|var|uint64
output = func_25226(var_25227,var_25228,var_25229,)
func_25230 = relay.Function([var_25227,var_25228,var_25229,], output)
mutated_mod['func_25230'] = func_25230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17748_call = mod.get_global_var('func_17748')
func_17750_call = mutated_mod.get_global_var('func_17750')
call_25235 = func_17748_call()
call_25236 = func_17748_call()
func_21811_call = mod.get_global_var('func_21811')
func_21812_call = mutated_mod.get_global_var('func_21812')
call_25251 = relay.TupleGetItem(func_21811_call(), 1)
call_25252 = relay.TupleGetItem(func_21812_call(), 1)
func_17571_call = mod.get_global_var('func_17571')
func_17572_call = mutated_mod.get_global_var('func_17572')
call_25259 = relay.TupleGetItem(func_17571_call(), 0)
call_25260 = relay.TupleGetItem(func_17572_call(), 0)
output = relay.Tuple([call_25235,call_25251,call_25259,])
output2 = relay.Tuple([call_25236,call_25252,call_25260,])
func_25268 = relay.Function([], output)
mod['func_25268'] = func_25268
mod = relay.transform.InferType()(mod)
mutated_mod['func_25268'] = func_25268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25268_call = mutated_mod.get_global_var('func_25268')
call_25269 = func_25268_call()
output = call_25269
func_25270 = relay.Function([], output)
mutated_mod['func_25270'] = func_25270
mutated_mod = relay.transform.InferType()(mutated_mod)
var_25301 = relay.var("var_25301", dtype = "uint64", shape = (8, 1, 1))#candidate|25301|(8, 1, 1)|var|uint64
var_25302 = relay.var("var_25302", dtype = "uint64", shape = (8, 9, 14))#candidate|25302|(8, 9, 14)|var|uint64
bop_25303 = relay.left_shift(var_25301.astype('uint64'), var_25302.astype('uint64')) # shape=(8, 9, 14)
output = relay.Tuple([bop_25303,])
output2 = relay.Tuple([bop_25303,])
func_25308 = relay.Function([var_25301,var_25302,], output)
mod['func_25308'] = func_25308
mod = relay.transform.InferType()(mod)
mutated_mod['func_25308'] = func_25308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25308_call = mutated_mod.get_global_var('func_25308')
var_25310 = relay.var("var_25310", dtype = "uint64", shape = (8, 1, 1))#candidate|25310|(8, 1, 1)|var|uint64
var_25311 = relay.var("var_25311", dtype = "uint64", shape = (8, 9, 14))#candidate|25311|(8, 9, 14)|var|uint64
call_25309 = func_25308_call(var_25310,var_25311,)
output = call_25309
func_25312 = relay.Function([var_25310,var_25311,], output)
mutated_mod['func_25312'] = func_25312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14740_call = mod.get_global_var('func_14740')
func_14742_call = mutated_mod.get_global_var('func_14742')
call_25314 = func_14740_call()
call_25315 = func_14740_call()
output = relay.Tuple([call_25314,])
output2 = relay.Tuple([call_25315,])
func_25318 = relay.Function([], output)
mod['func_25318'] = func_25318
mod = relay.transform.InferType()(mod)
output = func_25318()
func_25319 = relay.Function([], output)
mutated_mod['func_25319'] = func_25319
mutated_mod = relay.transform.InferType()(mutated_mod)
const_25328 = relay.const([[[7.515312,1.769514,-6.513893,8.562497,0.184447,1.941697,9.263921,5.308673,-5.651870,-5.280370,-2.541469,3.033355,0.462426,-1.338789,-7.026334,6.250850]],[[3.402371,-9.702319,-9.042932,9.890610,-4.953653,7.175385,6.147724,6.054985,-6.646905,-1.898788,-2.709755,1.283900,-6.765317,-4.224894,8.661018,-9.659469]],[[-9.080774,8.351927,-3.971376,-3.406576,6.924005,4.314399,-8.265152,-6.666723,-0.324178,4.585011,-6.565277,7.306948,6.478340,9.170099,5.210302,2.617704]],[[3.586555,-0.455030,6.368171,-9.221795,-0.268519,3.245563,9.508836,0.050346,7.687816,-9.410255,-5.743950,-7.891413,6.060546,-3.596853,-9.906845,5.451181]],[[-0.791565,2.991809,-1.074924,7.572460,6.377743,-6.325928,-9.391420,2.826305,-8.306431,-3.929044,9.098233,-4.488580,-9.109579,6.622916,-3.430901,-5.537911]],[[-3.285653,1.265393,-2.047153,6.175999,5.549671,-0.977570,2.783294,2.049035,3.914241,-2.538513,6.303697,-2.401252,-0.901260,-1.641478,-8.135634,6.371313]],[[-4.322091,3.797943,5.297767,5.570293,-6.012780,9.772830,7.724935,-4.853241,-2.543578,2.966516,6.503733,8.044541,2.566560,7.886153,2.220507,-8.413000]],[[3.766478,-7.286288,-2.298199,8.020714,3.878933,-4.950471,-5.460461,2.070389,-9.150939,-9.537344,-2.022858,3.100905,9.461216,3.271470,9.921758,-7.207356]],[[-4.298417,-1.228859,-7.767623,2.273373,-4.192911,-3.040757,-6.644098,3.197960,-4.634023,1.491955,2.517031,-5.261134,7.508345,3.069786,4.119194,3.785216]],[[-8.868831,-3.131103,1.744103,-9.844323,-0.793194,-1.205629,2.556498,2.962719,9.339568,-8.561098,1.364501,1.398757,0.203765,0.906266,0.094610,-1.059223]],[[-3.542572,-9.676257,-6.628874,6.363497,-5.863010,-4.436325,4.216733,9.206585,-8.033920,-0.497403,3.894537,-2.472562,-9.835575,1.804274,-1.627005,-6.373417]],[[2.773689,-7.558453,7.109563,-0.344740,-3.701600,6.272628,-7.530748,-1.093874,0.237967,-8.669636,2.673606,6.487100,-7.618801,1.164917,-7.798429,-3.227039]]], dtype = "float32")#candidate|25328|(12, 1, 16)|const|float32
var_25329 = relay.var("var_25329", dtype = "float32", shape = (12, 12, 16))#candidate|25329|(12, 12, 16)|var|float32
bop_25330 = relay.floor_mod(const_25328.astype('float32'), var_25329.astype('float32')) # shape=(12, 12, 16)
func_17368_call = mod.get_global_var('func_17368')
func_17373_call = mutated_mod.get_global_var('func_17373')
var_25334 = relay.var("var_25334", dtype = "int16", shape = (1404,))#candidate|25334|(1404,)|var|int16
var_25335 = relay.var("var_25335", dtype = "uint32", shape = (220,))#candidate|25335|(220,)|var|uint32
var_25336 = relay.var("var_25336", dtype = "float32", shape = ())#candidate|25336|()|var|float32
call_25333 = relay.TupleGetItem(func_17368_call(relay.reshape(var_25334.astype('int16'), [1404,]), relay.reshape(var_25335.astype('uint32'), [220,]), relay.reshape(var_25336.astype('float32'), []), ), 4)
call_25337 = relay.TupleGetItem(func_17373_call(relay.reshape(var_25334.astype('int16'), [1404,]), relay.reshape(var_25335.astype('uint32'), [220,]), relay.reshape(var_25336.astype('float32'), []), ), 4)
output = relay.Tuple([bop_25330,call_25333,var_25334,var_25335,var_25336,])
output2 = relay.Tuple([bop_25330,call_25337,var_25334,var_25335,var_25336,])
func_25347 = relay.Function([var_25329,var_25334,var_25335,var_25336,], output)
mod['func_25347'] = func_25347
mod = relay.transform.InferType()(mod)
mutated_mod['func_25347'] = func_25347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25347_call = mutated_mod.get_global_var('func_25347')
var_25349 = relay.var("var_25349", dtype = "float32", shape = (12, 12, 16))#candidate|25349|(12, 12, 16)|var|float32
var_25350 = relay.var("var_25350", dtype = "int16", shape = (1404,))#candidate|25350|(1404,)|var|int16
var_25351 = relay.var("var_25351", dtype = "uint32", shape = (220,))#candidate|25351|(220,)|var|uint32
var_25352 = relay.var("var_25352", dtype = "float32", shape = ())#candidate|25352|()|var|float32
call_25348 = func_25347_call(var_25349,var_25350,var_25351,var_25352,)
output = call_25348
func_25353 = relay.Function([var_25349,var_25350,var_25351,var_25352,], output)
mutated_mod['func_25353'] = func_25353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15146_call = mod.get_global_var('func_15146')
func_15148_call = mutated_mod.get_global_var('func_15148')
call_25424 = func_15146_call()
call_25425 = func_15146_call()
func_14593_call = mod.get_global_var('func_14593')
func_14595_call = mutated_mod.get_global_var('func_14595')
const_25442 = relay.const([-9.277674,8.423070,-8.768929,5.282028,9.345852,-9.863495,-6.301471,7.368517,5.371197,6.610956,3.472773,-3.364807,-0.658475,2.159086,4.434887,7.067992,-9.583126,3.659938,-4.976557,8.195429,5.915568,0.572528,-0.824584,-3.775416,1.102901,6.626741,-7.134944,-9.194085,-7.844669,-1.550057,-3.641459,0.846406,-2.501786,4.142796,-5.965225,4.056677,-1.987352,2.807843,8.484985,-2.867373,4.612200,-9.117681,3.131766,-0.415247,-0.618398,6.699009,3.642878,-3.693224,3.013862,-8.811203,-2.056369,0.227488,-0.809971,-6.884485,-1.144577,-0.692509,-7.320338,0.848022,0.291933,7.745437,7.869688,-6.921646,-4.165854,-8.199684,-6.097107,1.191386,-5.428377,6.727756,3.545113,7.391728,-7.558913,-4.563083,-8.418465,-4.447427,7.347959,6.621486,4.623517,2.469451,-7.633556,7.809676,-5.719518,-8.645584,-1.192212,-2.728237,7.917950,9.585122,1.960508,-1.860026,-6.984307,-5.008294,-7.537136,-9.537814,0.830159,7.012028,1.926154,5.613579,4.950872,6.428049,9.879458,-5.944482,3.235413,2.446738,4.064027,-7.717950,-5.406202,5.652106,-0.482356,-1.317840,-6.539391,-1.096214,9.667577,4.445163,3.513716,-9.590312,-1.336735,5.374550,-4.581182,5.169878,-3.308316,0.554601,-7.291631,5.266382,-6.122734,-8.989081,-8.603101,4.610305,-9.953050,-1.709796,5.753393,6.349624,4.119105,9.105399,6.991061,5.716464,-2.665694,-0.745055,-3.144621,9.637749,-9.669542,4.311916,-3.104537,-5.772747,8.843474,-0.839609,6.501179,1.881483,-9.561739,-2.280663,3.281376,3.492469,8.636805,-3.498166,-6.235273,-9.036568,3.844916,3.445281,-9.030170,9.759678,-3.633266,-8.800255,6.740314,8.618856,-1.294086,4.314900,3.066080,6.646426,-4.699083,-2.289240,-9.559622,6.245631,-6.974976,7.593336,-0.215410,7.051268,1.686631,-1.252408,8.799270,-3.158364,-0.795826,0.995076,9.868138,-2.259443,-4.336549,-2.290338,8.094797,-4.510320,-8.798739,3.217574,-5.331448,2.294117,-1.257321,-0.342275,1.328152,-4.882999,-0.095022,-3.843789,-0.726090,-7.787006,6.095511,1.609414,-1.986456,2.762472,-9.377313,-8.374340,5.488228,-8.094886,4.979915,3.257429,0.684356,-1.799297,8.094001,0.197583,2.142741,-7.901682,-9.059829,-5.267342,3.677174,2.947352,-9.372293,1.707872,-8.492910,6.969389,-6.266291,-4.478612,-4.322846,-7.281108,1.776628,-3.381408,1.710070,-2.523949,-8.565443,-9.185668,-2.943777,9.480610,5.208584,-8.133400,-2.673593,-2.605528,-9.936847,0.302143,2.447392,-1.010739,7.225364,-2.806893,1.380164,9.323511,5.056694,0.133583,2.839693,-4.926416,6.724435,-8.438423,-9.939233,4.808334,-6.863074,-3.882788,-7.195385,-4.221564,3.481171,-6.317709,0.242896,-0.345329,1.927146,-8.330277,3.494767,-0.907952,3.667090,-3.926333,5.365784,-8.189911,-0.611197,6.447968,6.041937,1.044094,-6.162527,3.839266,2.635619,-0.368273,-4.949913,1.347095,2.152163,-8.136598,5.217689,6.296728,-7.919764,-5.786366,-0.986048,0.040100,7.924500,-1.946767,-1.159424,-1.514507,0.072557,4.589601,9.924955,2.438989,-4.019697,-1.784596,0.045439,-7.394450,3.693490,-1.557227,-4.457009,-8.968965,-2.675512,-5.199693,-1.246937,-2.368491,1.017311,9.648076,4.477623,-1.711059,8.385943,2.312584,-6.396961,-4.885552,-3.186122,8.366861,1.472705,-5.182213,-3.450728,-6.162745,6.503618,-5.843496,-8.224934,-4.115666,4.577595,5.963878,3.621590,3.247389,-1.323907,2.164310,-6.909826,-4.567493,-6.270753,-4.651946,9.264511,-1.734064,5.835162,9.898144,-1.761282,7.997027,-2.720897,-5.201404,8.137680,0.274925,-6.003190,-6.617826,1.719758,-4.236734,-9.164523,-6.965917,5.215785,-9.544860,-8.765449,7.987343,6.670122,-1.402750,9.814278,3.074360,-4.337936,4.604413,-6.195791,2.291853,-7.353792,4.442629,-5.223739,-5.366318,-5.621417,7.671303,-9.679333,-0.982412,0.039905,-6.058283,7.963937,-9.411622,-6.372128,-4.803967,7.953358,1.088173,1.303493,-2.884100,-2.293652,-8.583357,-7.255492,2.061311,-7.993306,-5.541842,-5.582651,-9.425696,6.530739,6.184115,-6.880652,-9.431010,-0.058825,9.505730,-7.861813,0.764558,-0.849123,-4.473757,0.306371,-7.422212,9.989453,-0.139996,4.806817,8.062332,8.055779,-4.387112,2.234525,8.868456,-7.222617,4.287824,6.984045,-3.035700,-5.363689,-7.848074,-0.532161,5.356626,5.398778,-5.904857,9.293528,3.582902,-1.412970,-3.158168,-3.100085,5.695812,3.802256,-8.699787,-5.496523,-3.461230,1.620716,-5.757162,8.253462,0.427733,0.350094,9.091974,6.193928,2.997065,4.708849,8.121414,-3.219593,-8.064405,-0.394677,-2.111519,2.054106,4.961561,2.814889,6.737579,-1.980575,0.161963,-9.421669,-1.950138,-7.845249,8.264016,6.918770,9.161377,-8.612532,8.135578,-5.052988,5.945332,7.430121,-7.822747,-8.061738,5.951792,-9.273055,9.401335,-9.226895,5.696390,5.367991,-4.488480,5.904941,-5.636600,4.595431,-3.805450,5.433373,-9.644174,6.725475,0.654808,-3.621106,-8.826933,-8.969205,6.453077,2.243065,3.843354,2.913811,1.237510,4.239003,-3.566566,-3.634749,3.827459,-1.817283,-8.708920,-5.865594,-0.748103,-8.167760,-5.895500,-3.706620,9.435606,-8.107685,-1.707529,-1.820322,-5.580647,-2.557404,7.923850,-1.756729,-6.184929,-6.587541,-3.118129,8.639298,4.104398,1.096331,-4.702148,0.721226,1.442266,-0.293501,3.859918,3.734661,-9.514485,2.179849,-1.549631,-4.780527,-7.603590,5.897278,-3.679998,6.174733,7.418439,5.969887,-3.195647,4.236454,-9.570069,-8.512477,9.372187,7.687140,8.954465,4.835119,-1.721952,-3.329995,-3.961876,8.117427,-4.565431,-4.975466,7.218960,3.346950,-9.379850,5.662577,-7.767446,-8.419229,-9.168228,-1.253293,-8.110518,7.568261,9.316884,-3.555255,-2.754979,-8.183361,-4.150044,-6.517449,-5.015231,-4.168956,-9.027451,9.904286,5.474195,-2.413614,-2.819958,7.472814,-1.573556,7.984649,-1.387494,6.414187,-9.811075,-3.609331,-0.536438,-0.543943,-5.448626,3.807173,9.779978,-3.261584,3.415128,-2.258374,7.752454,-6.645987,-5.419721,8.689293,5.910229,6.911493,2.636528,4.816824,-0.393532], dtype = "float32")#candidate|25442|(588,)|const|float32
call_25441 = relay.TupleGetItem(func_14593_call(relay.reshape(const_25442.astype('float32'), [588,])), 7)
call_25443 = relay.TupleGetItem(func_14595_call(relay.reshape(const_25442.astype('float32'), [588,])), 7)
func_21811_call = mod.get_global_var('func_21811')
func_21812_call = mutated_mod.get_global_var('func_21812')
call_25448 = relay.TupleGetItem(func_21811_call(), 1)
call_25449 = relay.TupleGetItem(func_21812_call(), 1)
func_20777_call = mod.get_global_var('func_20777')
func_20778_call = mutated_mod.get_global_var('func_20778')
call_25467 = func_20777_call()
call_25468 = func_20777_call()
func_7590_call = mod.get_global_var('func_7590')
func_7593_call = mutated_mod.get_global_var('func_7593')
const_25483 = relay.const([[-8.105646,-4.978307],[-7.812774,-5.770013],[-6.641253,-2.448875],[8.197118,6.454911],[2.665924,5.437309],[4.288011,-5.645394],[7.680696,-5.497874],[-4.674259,-1.364089],[8.863351,2.848586],[-8.638262,8.113870],[-8.889999,-6.126509],[3.809178,-3.303223],[6.452811,-0.284771],[4.317641,1.614151],[6.113509,-2.481302],[-1.746116,-9.132729],[0.866708,9.300521],[0.156003,-2.530340],[-5.474974,0.865514],[-5.510137,-7.953323],[-7.833316,-9.814541],[-2.940316,-9.927900],[5.147369,5.602212],[9.708758,1.902024],[2.139061,-0.826345],[-6.577123,-5.202444],[3.422258,-0.099154],[4.688384,7.732078],[-5.623927,4.859566],[6.693264,-6.625222],[-8.230538,-2.843174],[1.222021,-9.612819],[-8.003959,4.433076],[3.032792,6.349796],[-6.731596,0.696696],[7.020758,6.209895],[-8.944172,-0.073380],[-9.633635,1.018053],[-4.705571,-6.278260],[3.201323,-5.164134],[5.147567,-3.895645],[-5.157097,2.224717]], dtype = "float64")#candidate|25483|(42, 2)|const|float64
call_25482 = func_7590_call(relay.reshape(const_25483.astype('float64'), [6, 14, 1]))
call_25484 = func_7590_call(relay.reshape(const_25483.astype('float64'), [6, 14, 1]))
func_20229_call = mod.get_global_var('func_20229')
func_20231_call = mutated_mod.get_global_var('func_20231')
call_25495 = relay.TupleGetItem(func_20229_call(), 0)
call_25496 = relay.TupleGetItem(func_20231_call(), 0)
output = relay.Tuple([call_25424,call_25441,const_25442,call_25448,call_25467,call_25482,const_25483,call_25495,])
output2 = relay.Tuple([call_25425,call_25443,const_25442,call_25449,call_25468,call_25484,const_25483,call_25496,])
func_25504 = relay.Function([], output)
mod['func_25504'] = func_25504
mod = relay.transform.InferType()(mod)
output = func_25504()
func_25505 = relay.Function([], output)
mutated_mod['func_25505'] = func_25505
mutated_mod = relay.transform.InferType()(mutated_mod)
const_25506 = relay.const([[[5.859247,7.356350,1.751944],[3.252898,-7.086003,-2.700312],[6.084506,-7.138790,3.320545],[-0.726562,-2.747802,8.142014],[-9.590180,1.960949,-7.932702],[4.818803,1.513686,5.008635],[-2.121310,-5.342050,-2.812300],[-2.254123,-0.160959,-1.001578],[-6.080897,2.776435,7.923341],[-7.422754,-8.305736,-4.763841]],[[4.965948,-2.191637,-9.047393],[1.660761,9.865514,3.760340],[-6.298026,2.294300,3.837860],[-5.252649,-4.912042,-7.427218],[-9.192996,5.122028,-6.276648],[-9.626108,6.550665,-7.373311],[-1.434616,5.934923,4.519736],[5.107446,-3.504908,7.032871],[-6.215156,1.607180,9.132205],[1.951609,-2.122363,-8.555828]],[[-7.135460,-5.230505,-8.174138],[0.805662,-1.939135,-0.866696],[-0.093474,8.408013,-0.204087],[-3.723775,0.039970,-2.161733],[1.557451,-6.581311,-9.468027],[4.248434,8.949829,9.663157],[-7.200528,-8.957855,5.755505],[4.430395,7.332377,-6.613416],[4.725609,-6.926369,-9.687174],[5.698395,-0.378682,4.859841]],[[-7.252665,1.841615,7.480943],[7.003092,-9.767376,-1.975301],[-6.716039,9.269773,7.028870],[-3.733625,-6.576928,8.836074],[0.943926,-2.444021,-8.541499],[-8.568374,-0.198597,4.203728],[-4.660005,-6.944660,-8.949052],[-3.365584,-4.425045,-6.722792],[1.051297,-5.869685,-7.505148],[-7.504190,-9.197653,3.999893]],[[1.028936,7.793833,-1.052460],[1.149648,-4.776864,1.246409],[-5.561772,6.045677,3.579096],[-4.609170,-6.874203,-3.236484],[-0.925151,-4.586718,8.046809],[-4.007931,-7.827965,7.380338],[-4.905036,7.719947,-0.111522],[1.071573,0.149123,2.115578],[6.135032,7.859761,-0.322374],[-2.311646,0.130322,8.229340]]], dtype = "float64")#candidate|25506|(5, 10, 3)|const|float64
uop_25507 = relay.sinh(const_25506.astype('float64')) # shape=(5, 10, 3)
output = relay.Tuple([uop_25507,])
output2 = relay.Tuple([uop_25507,])
func_25513 = relay.Function([], output)
mod['func_25513'] = func_25513
mod = relay.transform.InferType()(mod)
output = func_25513()
func_25514 = relay.Function([], output)
mutated_mod['func_25514'] = func_25514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16461_call = mod.get_global_var('func_16461')
func_16462_call = mutated_mod.get_global_var('func_16462')
call_25515 = func_16461_call()
call_25516 = func_16461_call()
output = call_25515
output2 = call_25516
func_25522 = relay.Function([], output)
mod['func_25522'] = func_25522
mod = relay.transform.InferType()(mod)
mutated_mod['func_25522'] = func_25522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25522_call = mutated_mod.get_global_var('func_25522')
call_25523 = func_25522_call()
output = call_25523
func_25524 = relay.Function([], output)
mutated_mod['func_25524'] = func_25524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21953_call = mod.get_global_var('func_21953')
func_21955_call = mutated_mod.get_global_var('func_21955')
call_25551 = relay.TupleGetItem(func_21953_call(), 3)
call_25552 = relay.TupleGetItem(func_21955_call(), 3)
output = relay.Tuple([call_25551,])
output2 = relay.Tuple([call_25552,])
func_25553 = relay.Function([], output)
mod['func_25553'] = func_25553
mod = relay.transform.InferType()(mod)
mutated_mod['func_25553'] = func_25553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_25553_call = mutated_mod.get_global_var('func_25553')
call_25554 = func_25553_call()
output = call_25554
func_25555 = relay.Function([], output)
mutated_mod['func_25555'] = func_25555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_22314_call = mod.get_global_var('func_22314')
func_22316_call = mutated_mod.get_global_var('func_22316')
call_25573 = func_22314_call()
call_25574 = func_22314_call()
output = relay.Tuple([call_25573,])
output2 = relay.Tuple([call_25574,])
func_25576 = relay.Function([], output)
mod['func_25576'] = func_25576
mod = relay.transform.InferType()(mod)
output = func_25576()
func_25577 = relay.Function([], output)
mutated_mod['func_25577'] = func_25577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_25587 = relay.var("var_25587", dtype = "float64", shape = (7, 1, 13))#candidate|25587|(7, 1, 13)|var|float64
uop_25588 = relay.cosh(var_25587.astype('float64')) # shape=(7, 1, 13)
bop_25592 = relay.greater(var_25587.astype('bool'), relay.reshape(uop_25588.astype('bool'), relay.shape_of(var_25587))) # shape=(7, 1, 13)
func_19406_call = mod.get_global_var('func_19406')
func_19409_call = mutated_mod.get_global_var('func_19409')
var_25602 = relay.var("var_25602", dtype = "bool", shape = (2, 264))#candidate|25602|(2, 264)|var|bool
call_25601 = relay.TupleGetItem(func_19406_call(relay.reshape(var_25602.astype('bool'), [528,])), 0)
call_25603 = relay.TupleGetItem(func_19409_call(relay.reshape(var_25602.astype('bool'), [528,])), 0)
uop_25607 = relay.sinh(bop_25592.astype('float64')) # shape=(7, 1, 13)
bop_25615 = relay.right_shift(bop_25592.astype('uint16'), relay.reshape(var_25587.astype('uint16'), relay.shape_of(bop_25592))) # shape=(7, 1, 13)
output = relay.Tuple([call_25601,var_25602,uop_25607,bop_25615,])
output2 = relay.Tuple([call_25603,var_25602,uop_25607,bop_25615,])
F = relay.Function([var_25587,var_25602,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_25587,var_25602,], output2)
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
