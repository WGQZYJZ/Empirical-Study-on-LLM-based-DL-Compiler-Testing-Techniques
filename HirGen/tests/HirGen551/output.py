import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_192 = relay.var("var_192", dtype = "float32", shape = ())#candidate|192|()|var|float32
var_193 = relay.var("var_193", dtype = "float32", shape = (16, 2, 8))#candidate|193|(16, 2, 8)|var|float32
bop_194 = relay.power(var_192.astype('float32'), var_193.astype('float32')) # shape=(16, 2, 8)
uop_202 = relay.erf(var_193.astype('float32')) # shape=(16, 2, 8)
bop_206 = relay.bitwise_or(uop_202.astype('int64'), relay.reshape(bop_194.astype('int64'), relay.shape_of(uop_202))) # shape=(16, 2, 8)
uop_228 = relay.exp(bop_206.astype('float32')) # shape=(16, 2, 8)
output = uop_228
output2 = uop_228
func_232 = relay.Function([var_192,var_193,], output)
mod['func_232'] = func_232
mod = relay.transform.InferType()(mod)
var_233 = relay.var("var_233", dtype = "float32", shape = ())#candidate|233|()|var|float32
var_234 = relay.var("var_234", dtype = "float32", shape = (16, 2, 8))#candidate|234|(16, 2, 8)|var|float32
output = func_232(var_233,var_234,)
func_235 = relay.Function([var_233,var_234,], output)
mutated_mod['func_235'] = func_235
mutated_mod = relay.transform.InferType()(mutated_mod)
const_348 = relay.const([[[-0.911312,-5.158401,-0.733440,-1.607800,4.947253,-2.848471,-1.777928,-9.120224,5.619204,-7.538126],[-2.377407,5.567306,7.913381,-6.458366,-7.011774,-2.619352,-5.136879,2.314963,-2.819943,2.400062],[8.586540,-8.982269,6.617895,8.280556,-3.254671,0.319506,-2.352336,1.457299,2.354320,8.896853]],[[3.107959,-3.084994,-1.211216,1.462908,1.073114,4.025301,-9.428355,7.922489,-7.153128,7.272933],[-9.951546,0.007351,5.998584,-6.264322,7.239803,-5.057196,7.916834,-3.652356,-6.807384,-0.646833],[1.645530,-3.224394,8.340223,1.095797,-4.896247,-7.637238,9.288956,-2.295782,9.450095,2.241767]],[[-3.989382,2.459057,-4.360921,-5.896060,9.333925,-2.584732,-4.690529,4.622297,-8.258106,3.730224],[8.096297,5.838250,-3.328230,5.192252,-1.253516,-4.700793,-3.767912,5.438648,5.359277,2.330258],[-7.236726,8.936765,2.298065,9.123938,6.360346,-0.284952,-8.927164,5.533826,2.699377,-4.909266]],[[5.696388,4.224268,6.816730,-9.452593,-5.521682,9.795009,-3.740918,6.655064,6.401732,4.665077],[7.517481,7.010155,-1.305417,-3.561482,4.143193,3.106717,6.318552,-2.517263,8.941165,-2.440970],[7.092181,6.330104,-4.207135,6.625517,8.086183,8.002334,-0.911644,-5.934799,3.486070,1.344059]],[[-7.042304,-9.771108,8.271085,-3.991624,2.138193,-5.602496,-9.958697,-4.854563,-0.996653,6.165348],[4.018452,-5.170821,9.474800,-6.372565,-6.689102,-6.241036,-2.211125,-6.869281,1.620778,4.219740],[1.630366,6.885089,7.314358,1.272322,0.459695,8.942308,2.645517,8.204292,-5.609565,1.589005]],[[5.302368,2.063239,-9.576678,7.328531,-0.011664,0.653486,-7.232189,-1.239927,-8.861372,1.358118],[-2.169526,-0.264122,-5.994172,-8.710907,4.348852,2.534054,4.530681,8.356122,5.693565,-2.950098],[1.791492,6.348902,-7.196408,8.303397,2.978325,3.055500,2.887598,5.305032,1.861146,-9.804670]],[[-0.993228,5.554552,5.447185,5.732520,0.668817,-0.117138,1.775815,-3.534283,4.168995,7.990119],[-7.164735,-4.704086,-6.121021,2.012809,-8.305141,1.732534,-7.918857,-0.276997,7.599512,-0.961517],[3.544627,2.728174,-4.770314,5.827701,3.673288,1.119546,0.272506,6.703009,9.170182,8.841419]],[[-8.922447,-1.929414,2.174822,-5.832085,2.710234,6.382087,-1.865693,3.634413,-5.670493,-0.817419],[5.463630,5.321955,-5.104631,3.826724,0.827895,3.509021,3.255273,-6.937768,-6.501039,9.113224],[9.130411,4.859420,0.889446,4.692296,7.757111,4.263423,3.029027,2.516682,4.567330,6.587998]],[[1.220281,-6.556128,4.066017,3.816657,-7.059791,9.267360,8.084764,1.114363,1.709119,-9.150061],[-7.693541,-1.399484,-3.676383,2.412271,-6.146425,-8.484386,7.842462,-6.162637,-4.318173,1.091868],[-5.544831,-4.530813,6.380216,-5.764389,-4.100282,6.628616,-5.799806,-3.510075,3.585583,-9.662800]],[[1.449169,0.689169,9.146470,4.660159,6.359797,-2.771185,1.032132,8.687139,-2.581313,0.220897],[-7.230961,-3.245794,-5.103612,4.082372,-9.557991,3.227835,-2.838978,0.267523,-9.891072,5.497395],[7.045561,8.778341,3.809341,8.515905,-2.170586,-3.590540,7.236695,6.902018,-0.802566,1.519268]],[[-6.643421,-7.453603,4.835801,4.455446,-8.737302,8.464517,-4.304824,-0.229853,1.217208,-6.492717],[-2.525350,-4.803273,0.337723,-6.465640,-5.287899,-2.624731,-3.783993,1.676908,-7.697596,-4.614505],[-9.126272,-7.903171,-6.522174,-4.114510,-9.011765,-4.501182,9.545114,-2.089334,-8.328382,-6.405841]],[[-2.495160,-5.749019,5.100890,-1.035902,-7.725027,-8.624156,-7.994895,6.944921,7.583806,-2.590811],[-5.276821,9.874936,0.991680,-3.738389,-2.677859,-2.660142,-1.460700,1.760794,1.635273,8.973681],[-9.392186,-7.382588,2.524497,-1.328419,4.763742,-0.067765,6.018929,8.726808,-3.746508,-7.761215]],[[6.805577,5.678653,3.736705,9.821438,6.682151,-4.936813,9.411722,-1.512739,9.721372,8.892452],[-5.179606,-2.277423,1.103150,-8.890188,-7.846245,-5.584809,-9.013585,0.183296,5.449982,-5.341636],[3.721103,-0.730859,8.664480,7.103738,0.017241,6.687474,1.640888,2.344014,6.327943,-8.767820]],[[4.014801,8.944282,-5.777588,2.811632,-1.714794,-0.159185,7.958257,-5.379557,-9.915956,8.136261],[-0.526227,8.887548,-5.702503,0.051135,-9.421949,7.825124,-6.262311,8.960914,5.657000,-5.758409],[-3.151683,-1.086228,-3.516467,-2.884206,-8.492585,-2.618331,-2.533912,-2.589154,0.004800,2.851489]],[[9.037968,0.591575,2.228391,3.313534,1.667216,-9.623252,-0.456674,9.158761,2.471623,7.470478],[8.506202,2.157819,5.120382,8.243476,5.865755,9.953364,3.147401,-4.362479,0.069063,-9.975665],[-7.417081,8.740493,6.907501,4.429770,-6.165592,-4.498587,-7.577226,-7.476125,-6.059637,-4.244181]],[[-9.371227,-8.988719,-0.776976,-3.413261,-4.226856,8.845377,-4.931337,-8.158451,7.031335,-6.876947],[-1.871092,-5.879200,-8.053870,8.163515,-0.992042,-9.733516,7.665025,-3.368063,-3.575242,2.110707],[7.058886,4.217770,1.770747,2.006533,8.894123,5.827752,6.865607,-2.073244,-7.564821,-9.016071]]], dtype = "float64")#candidate|348|(16, 3, 10)|const|float64
uop_349 = relay.cosh(const_348.astype('float64')) # shape=(16, 3, 10)
uop_356 = relay.rsqrt(uop_349.astype('float64')) # shape=(16, 3, 10)
func_232_call = mod.get_global_var('func_232')
func_235_call = mutated_mod.get_global_var('func_235')
var_362 = relay.var("var_362", dtype = "float32", shape = ())#candidate|362|()|var|float32
var_363 = relay.var("var_363", dtype = "float32", shape = (8, 32))#candidate|363|(8, 32)|var|float32
call_361 = func_232_call(relay.reshape(var_362.astype('float32'), []), relay.reshape(var_363.astype('float32'), [16, 2, 8]), )
call_364 = func_232_call(relay.reshape(var_362.astype('float32'), []), relay.reshape(var_363.astype('float32'), [16, 2, 8]), )
output = relay.Tuple([uop_356,call_361,var_362,var_363,])
output2 = relay.Tuple([uop_356,call_364,var_362,var_363,])
func_380 = relay.Function([var_362,var_363,], output)
mod['func_380'] = func_380
mod = relay.transform.InferType()(mod)
var_381 = relay.var("var_381", dtype = "float32", shape = ())#candidate|381|()|var|float32
var_382 = relay.var("var_382", dtype = "float32", shape = (8, 32))#candidate|382|(8, 32)|var|float32
output = func_380(var_381,var_382,)
func_383 = relay.Function([var_381,var_382,], output)
mutated_mod['func_383'] = func_383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_719 = relay.var("var_719", dtype = "float64", shape = (15, 15, 9))#candidate|719|(15, 15, 9)|var|float64
uop_720 = relay.rsqrt(var_719.astype('float64')) # shape=(15, 15, 9)
output = uop_720
output2 = uop_720
func_729 = relay.Function([var_719,], output)
mod['func_729'] = func_729
mod = relay.transform.InferType()(mod)
var_730 = relay.var("var_730", dtype = "float64", shape = (15, 15, 9))#candidate|730|(15, 15, 9)|var|float64
output = func_729(var_730)
func_731 = relay.Function([var_730], output)
mutated_mod['func_731'] = func_731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1000 = relay.var("var_1000", dtype = "float32", shape = (7, 15, 3))#candidate|1000|(7, 15, 3)|var|float32
uop_1001 = relay.atanh(var_1000.astype('float32')) # shape=(7, 15, 3)
var_1003 = relay.var("var_1003", dtype = "float32", shape = (7, 15, 3))#candidate|1003|(7, 15, 3)|var|float32
bop_1004 = relay.mod(uop_1001.astype('float64'), relay.reshape(var_1003.astype('float64'), relay.shape_of(uop_1001))) # shape=(7, 15, 3)
output = bop_1004
output2 = bop_1004
func_1010 = relay.Function([var_1000,var_1003,], output)
mod['func_1010'] = func_1010
mod = relay.transform.InferType()(mod)
mutated_mod['func_1010'] = func_1010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1010_call = mutated_mod.get_global_var('func_1010')
var_1012 = relay.var("var_1012", dtype = "float32", shape = (7, 15, 3))#candidate|1012|(7, 15, 3)|var|float32
var_1013 = relay.var("var_1013", dtype = "float32", shape = (7, 15, 3))#candidate|1013|(7, 15, 3)|var|float32
call_1011 = func_1010_call(var_1012,var_1013,)
output = call_1011
func_1014 = relay.Function([var_1012,var_1013,], output)
mutated_mod['func_1014'] = func_1014
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1060 = relay.var("var_1060", dtype = "float64", shape = (4, 10, 9))#candidate|1060|(4, 10, 9)|var|float64
uop_1061 = relay.log(var_1060.astype('float64')) # shape=(4, 10, 9)
output = relay.Tuple([uop_1061,])
output2 = relay.Tuple([uop_1061,])
func_1064 = relay.Function([var_1060,], output)
mod['func_1064'] = func_1064
mod = relay.transform.InferType()(mod)
mutated_mod['func_1064'] = func_1064
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1065 = relay.var("var_1065", dtype = "float64", shape = (4, 10, 9))#candidate|1065|(4, 10, 9)|var|float64
func_1064_call = mutated_mod.get_global_var('func_1064')
call_1066 = func_1064_call(var_1065)
output = call_1066
func_1067 = relay.Function([var_1065], output)
mutated_mod['func_1067'] = func_1067
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1289 = relay.const(-8, dtype = "uint64")#candidate|1289|()|const|uint64
const_1290 = relay.const([[[10,2,-10,3],[4,6,6,4],[-4,-2,-7,1],[-9,2,5,-3],[-7,8,4,1],[-5,-5,5,-2],[-2,-1,7,8],[2,-1,-2,-5],[9,-8,5,2],[8,-3,-9,-1],[-1,10,8,-4],[-8,9,-1,-10],[-8,-5,2,4],[-7,3,4,-6],[8,-3,-4,7],[3,-3,-2,5]],[[5,-4,-7,7],[5,-9,5,4],[-1,-10,-3,8],[-4,-10,-6,-6],[-5,8,-9,8],[-6,-3,-2,2],[3,8,-10,-3],[7,-1,-6,-8],[9,5,-2,2],[-9,6,-3,5],[-2,-1,9,-7],[7,3,-6,4],[-6,3,-3,-5],[1,6,-2,7],[3,-8,-4,-9],[2,-4,-3,-6]]], dtype = "uint64")#candidate|1290|(2, 16, 4)|const|uint64
bop_1291 = relay.bitwise_xor(const_1289.astype('uint64'), const_1290.astype('uint64')) # shape=(2, 16, 4)
output = bop_1291
output2 = bop_1291
func_1295 = relay.Function([], output)
mod['func_1295'] = func_1295
mod = relay.transform.InferType()(mod)
output = func_1295()
func_1296 = relay.Function([], output)
mutated_mod['func_1296'] = func_1296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_1300 = func_1295_call()
call_1301 = func_1295_call()
func_380_call = mod.get_global_var('func_380')
func_383_call = mutated_mod.get_global_var('func_383')
var_1308 = relay.var("var_1308", dtype = "float32", shape = ())#candidate|1308|()|var|float32
var_1309 = relay.var("var_1309", dtype = "float32", shape = (256,))#candidate|1309|(256,)|var|float32
call_1307 = relay.TupleGetItem(func_380_call(relay.reshape(var_1308.astype('float32'), []), relay.reshape(var_1309.astype('float32'), [8, 32]), ), 2)
call_1310 = relay.TupleGetItem(func_383_call(relay.reshape(var_1308.astype('float32'), []), relay.reshape(var_1309.astype('float32'), [8, 32]), ), 2)
output = relay.Tuple([call_1300,call_1307,var_1308,var_1309,])
output2 = relay.Tuple([call_1301,call_1310,var_1308,var_1309,])
func_1359 = relay.Function([var_1308,var_1309,], output)
mod['func_1359'] = func_1359
mod = relay.transform.InferType()(mod)
var_1360 = relay.var("var_1360", dtype = "float32", shape = ())#candidate|1360|()|var|float32
var_1361 = relay.var("var_1361", dtype = "float32", shape = (256,))#candidate|1361|(256,)|var|float32
output = func_1359(var_1360,var_1361,)
func_1362 = relay.Function([var_1360,var_1361,], output)
mutated_mod['func_1362'] = func_1362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_1415 = func_1295_call()
call_1416 = func_1295_call()
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_1423 = func_1295_call()
call_1424 = func_1295_call()
func_1010_call = mod.get_global_var('func_1010')
func_1014_call = mutated_mod.get_global_var('func_1014')
const_1444 = relay.const([-5.582980,-0.365938,9.001888,-5.220704,-9.769048,8.063429,-8.081092,8.667440,4.909078,1.878138,4.144948,1.588161,2.881825,9.164057,-9.917066,4.910662,7.228819,1.012472,1.027960,7.296560,5.501387,-5.181976,-5.603870,-7.091039,6.454046,1.582592,-2.072399,-3.523098,6.925542,-9.697272,-6.036327,8.229423,2.357920,-1.304399,-8.841720,0.410810,-4.150865,5.957238,0.861216,-3.064012,2.709120,-6.202527,-9.870745,0.210942,-7.288795,-6.493771,1.945016,-6.759690,-4.022948,-3.661746,-6.854770,5.968399,2.345561,8.267643,-0.371684,9.472072,5.173189,6.343850,-2.586555,8.545127,4.090708,2.359135,6.835736,1.043575,-9.936907,-6.453818,8.465771,6.225199,-5.482728,-5.869209,-7.028198,-1.985986,4.397740,-0.931479,0.143493,-4.876700,1.729228,4.526787,9.903570,-0.542834,-5.431817,-9.927965,-7.458104,7.087168,-1.369243,-3.763537,7.088815,-7.447082,-4.107901,3.694293,-3.272980,-2.372479,6.445895,5.647445,9.607983,8.763061,-5.093342,3.563420,3.477062,-9.370260,-9.749623,3.273458,7.004305,-4.530051,-0.483804,5.855666,2.813117,-2.988601,-2.980853,8.994935,8.766557,2.929401,-9.192312,2.823953,8.682944,6.336335,-2.699975,-2.806693,-8.833815,0.231276,-4.259927,-8.442642,2.206818,-5.460389,-5.109528,1.371367,-0.775286,7.154479,8.568062,2.934695,-5.844356,3.902027,0.941893,9.237247,-9.111238,-4.146022,2.077570,5.072452,2.440067,-8.083252,2.037432,0.466239,1.538532,2.507273,6.424555,1.899049,6.484780,-2.454461,-9.887652,8.790227,8.276636,6.389645,-9.942897,7.019991,9.825464,3.052272,3.148401,-0.489311,1.989624,9.278624,-8.026785,7.133402,0.230507,-3.557354,1.934359,9.799228,6.154252,3.258178,4.352732,1.665240,6.091116,0.324642,-3.552293,7.641582,3.524766,-6.854051,2.900063,-6.710876,-1.094226,5.621443,-0.828552,-2.062432,3.995623,8.044218,-1.164431,5.262728,6.139076,-6.589141,8.485783,7.624387,-7.294783,-8.035040,8.585408,0.641964,-3.599727,5.570089,4.628608,-7.168231,-8.388799,9.555138,0.847591,-2.415913,5.969861,-0.714587,-1.353762,-0.039452,8.160484,-1.951086,0.591574,-4.829907,-5.047388,-8.928819,5.534565,5.102843,-3.252983,-2.212083,9.945188,-7.114818,7.299904,6.331409,-7.035815,4.808520,4.456376,5.247802,9.568137,-5.664774,6.131737,8.275962,1.286071,-2.577127,1.257534,8.340050,4.240598,1.430903,-3.854141,-2.510339,-6.100069,2.793475,-4.931342,-0.686414,-6.898118,2.336655,5.255474,7.427509,7.486176,-6.174772,-5.092544,-4.370257,8.897783,7.545591,-3.694814,1.446920,6.075038,-6.431199,2.307910,8.090070,3.473703,5.512990,5.294030,-0.752815,6.494693,9.129233,-0.185696,3.895964,3.360474,-4.434119,3.424531,0.540197,-5.757289,-3.410239,-2.212792,2.619834,-5.693778,1.219736,7.138645,5.847171,-5.630205,5.905073,-8.921789,2.822275,1.660910,6.439708,5.525887,1.667453,5.071716,9.866435,4.510211,4.405950,9.130164,5.563707,-8.162639,4.657559,3.742689,-8.350142,-7.304196,5.969094,2.315342,-7.768712,1.725103,-7.190593,8.004742,8.402779,-6.573011,-4.118768,5.835925,5.547924,-3.634298,-9.269768,8.063031,8.102438,-1.536535,7.127693,-8.281717,-9.398924,8.595631], dtype = "float32")#candidate|1444|(315,)|const|float32
call_1443 = func_1010_call(relay.reshape(const_1444.astype('float32'), [7, 15, 3]), relay.reshape(const_1444.astype('float32'), [7, 15, 3]), )
call_1445 = func_1010_call(relay.reshape(const_1444.astype('float32'), [7, 15, 3]), relay.reshape(const_1444.astype('float32'), [7, 15, 3]), )
func_1010_call = mod.get_global_var('func_1010')
func_1014_call = mutated_mod.get_global_var('func_1014')
call_1450 = func_1010_call(relay.reshape(call_1443.astype('float32'), [7, 15, 3]), relay.reshape(const_1444.astype('float32'), [7, 15, 3]), )
call_1451 = func_1010_call(relay.reshape(call_1443.astype('float32'), [7, 15, 3]), relay.reshape(const_1444.astype('float32'), [7, 15, 3]), )
func_1064_call = mod.get_global_var('func_1064')
func_1067_call = mutated_mod.get_global_var('func_1067')
const_1462 = relay.const([-8.518428,3.663722,3.363018,-3.614013,9.023089,-9.682450,-4.772208,7.987446,-2.545169,-1.990156,-0.023263,9.069974,7.736585,-4.134666,4.401331,4.872075,-5.569069,7.217807,7.718316,3.666655,-3.073457,7.559466,5.144730,-9.680196,-3.931147,7.741873,-1.240655,-5.002280,-5.018297,-4.678238,-7.787224,-9.208139,-5.513326,8.141231,9.450132,-4.465734,-9.826291,-0.317323,-7.682391,-8.600204,9.051311,-3.012397,-0.080318,-2.292564,1.695893,-9.088582,-0.641999,-7.802790,7.464984,-9.570471,-4.344806,-7.961745,-2.846454,-7.695116,-5.821512,-5.444169,3.329374,8.445021,7.949618,-8.622069,-2.334072,-0.644693,6.295385,-8.870095,-0.837469,2.746264,1.657386,-7.258453,-2.619968,7.338990,7.578049,4.537106,-2.147452,-4.231139,-6.272697,-8.865317,5.856932,3.631481,7.191317,4.268681,-5.317437,1.144247,8.068314,5.703619,-0.913923,-2.652993,-0.081196,-1.993684,-7.215092,-2.118950,-1.755944,9.975760,-7.120546,-4.027391,-0.307861,9.480811,0.986551,4.056816,-3.033163,-6.486889,7.139692,-9.309670,-0.510017,-8.413913,5.825196,5.212908,3.485329,-8.763218,3.085437,6.727845,-2.876783,-2.657098,5.163502,-1.870895,6.095605,0.748865,4.152534,-2.166993,-7.792899,-6.954314,-3.728540,8.197854,1.493102,0.827380,2.326200,-4.932333,0.380608,9.578549,-3.592211,4.553711,-4.227941,-5.162957,-9.823907,-0.823143,5.498771,9.031657,-4.594091,1.683406,-4.206124,2.213727,-1.656376,4.491878,-2.731673,-3.145736,7.917555,-6.747603,-6.455534,1.048751,-0.090716,-7.022745,6.384725,8.557798,-9.661842,8.726273,2.010453,-7.838950,-2.103139,8.908778,-0.149993,-7.707275,1.834541,-4.508460,0.121123,6.370640,5.756490,-4.284440,5.699112,-4.138733,-2.528178,-2.687790,-2.225352,6.688334,-1.513650,-2.795951,3.038903,-5.072780,7.194799,-5.187678,9.607373,-5.190984,4.507962,1.956541,-3.636315,3.445130,9.037805,-4.848300,-5.460211,-1.841600,4.257545,-4.372232,8.919649,1.453384,7.503605,-2.535410,1.462604,6.969318,6.327214,8.711911,-2.661416,-8.510466,-3.647212,-8.190715,8.397095,-1.725861,9.810938,9.437438,0.149429,2.855068,-0.551510,6.693032,0.861102,0.572225,2.335500,-1.729796,3.033773,4.116736,-7.835732,-7.349176,3.703974,-4.527390,7.606044,0.233926,-5.569725,3.584113,-8.190180,9.933195,9.131885,-4.660012,7.035611,9.276983,-6.431342,8.348947,-5.970994,-3.104110,-1.991194,-5.341269,-2.799135,-4.524665,-4.432130,1.986056,4.684134,-2.809545,3.166357,1.951289,-9.300355,6.140577,-9.635146,1.298543,6.532478,-7.121804,-8.041074,1.709409,-3.233053,1.602599,-8.857198,-7.728303,0.490376,-6.240502,1.677494,-4.549361,-0.126302,-7.088379,-6.581421,1.142921,5.628988,8.544771,-6.455874,-0.311664,-6.598713,-6.563416,3.468742,-6.362624,1.571945,1.099110,9.624044,-2.178525,-2.610901,-8.868506,-6.180533,-7.626061,1.362897,8.830521,-6.221633,-1.203108,-6.732716,5.952221,0.667615,-3.711273,2.660822,-3.763059,2.232569,-9.477338,3.684999,-0.741388,4.258402,-7.348277,-4.777111,-2.786350,9.851023,-2.132816,4.254699,7.415842,2.866648,-2.770104,-5.024900,6.875402,1.523257,1.020908,-3.601588,3.111002,-5.024567,-0.871288,6.495996,6.899718,-5.777405,-3.725033,-3.507356,-1.838262,-3.782518,-4.827329,0.094735,-7.561133,7.462445,-9.735841,-9.764994,5.915668,6.408309,4.431957,4.926326,3.008714,-0.583846,7.282420,-7.701963,9.289872,-5.459155,0.652100,9.343731,0.668365,6.685561,3.554818,5.728387,-3.514599,-1.670685,8.822332,-1.848116,9.204158,4.320012,5.075726,3.604313,-5.370984,-1.127497,5.097579,2.737069,0.314689,-2.419732,-5.848269,7.979428,-8.841081,7.844376,4.506662], dtype = "float64")#candidate|1462|(360,)|const|float64
call_1461 = relay.TupleGetItem(func_1064_call(relay.reshape(const_1462.astype('float64'), [4, 10, 9])), 0)
call_1463 = relay.TupleGetItem(func_1067_call(relay.reshape(const_1462.astype('float64'), [4, 10, 9])), 0)
func_1064_call = mod.get_global_var('func_1064')
func_1067_call = mutated_mod.get_global_var('func_1067')
call_1472 = relay.TupleGetItem(func_1064_call(relay.reshape(call_1461.astype('float64'), [4, 10, 9])), 0)
call_1473 = relay.TupleGetItem(func_1067_call(relay.reshape(call_1461.astype('float64'), [4, 10, 9])), 0)
func_1010_call = mod.get_global_var('func_1010')
func_1014_call = mutated_mod.get_global_var('func_1014')
call_1496 = func_1010_call(relay.reshape(const_1444.astype('float32'), [7, 15, 3]), relay.reshape(call_1443.astype('float32'), [7, 15, 3]), )
call_1497 = func_1010_call(relay.reshape(const_1444.astype('float32'), [7, 15, 3]), relay.reshape(call_1443.astype('float32'), [7, 15, 3]), )
output = relay.Tuple([call_1415,call_1423,call_1443,const_1444,call_1450,call_1461,const_1462,call_1472,call_1496,])
output2 = relay.Tuple([call_1416,call_1424,call_1445,const_1444,call_1451,call_1463,const_1462,call_1473,call_1497,])
func_1506 = relay.Function([], output)
mod['func_1506'] = func_1506
mod = relay.transform.InferType()(mod)
output = func_1506()
func_1507 = relay.Function([], output)
mutated_mod['func_1507'] = func_1507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1506_call = mod.get_global_var('func_1506')
func_1507_call = mutated_mod.get_global_var('func_1507')
call_1526 = relay.TupleGetItem(func_1506_call(), 1)
call_1527 = relay.TupleGetItem(func_1507_call(), 1)
output = call_1526
output2 = call_1527
func_1532 = relay.Function([], output)
mod['func_1532'] = func_1532
mod = relay.transform.InferType()(mod)
mutated_mod['func_1532'] = func_1532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1532_call = mutated_mod.get_global_var('func_1532')
call_1533 = func_1532_call()
output = call_1533
func_1534 = relay.Function([], output)
mutated_mod['func_1534'] = func_1534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1506_call = mod.get_global_var('func_1506')
func_1507_call = mutated_mod.get_global_var('func_1507')
call_1581 = relay.TupleGetItem(func_1506_call(), 6)
call_1582 = relay.TupleGetItem(func_1507_call(), 6)
output = call_1581
output2 = call_1582
func_1597 = relay.Function([], output)
mod['func_1597'] = func_1597
mod = relay.transform.InferType()(mod)
output = func_1597()
func_1598 = relay.Function([], output)
mutated_mod['func_1598'] = func_1598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1598_call = mutated_mod.get_global_var('func_1598')
call_1615 = func_1597_call()
call_1616 = func_1597_call()
func_729_call = mod.get_global_var('func_729')
func_731_call = mutated_mod.get_global_var('func_731')
var_1628 = relay.var("var_1628", dtype = "float64", shape = (2025,))#candidate|1628|(2025,)|var|float64
call_1627 = func_729_call(relay.reshape(var_1628.astype('float64'), [15, 15, 9]))
call_1629 = func_729_call(relay.reshape(var_1628.astype('float64'), [15, 15, 9]))
func_1010_call = mod.get_global_var('func_1010')
func_1014_call = mutated_mod.get_global_var('func_1014')
const_1636 = relay.const([-5.100219,-9.656770,-1.312391,-4.066650,-4.060337,2.487274,-1.331412,5.927702,-9.899781,2.545384,3.618002,-1.315589,-2.571743,5.243469,-8.943784,1.511319,1.360369,1.315705,0.002572,-3.490255,-4.036831,-9.200422,-2.929790,-5.349974,-9.092912,7.272491,2.332194,6.187323,-3.707052,1.520864,0.366000,-3.394432,-9.810987,1.950977,5.855625,6.724278,3.013640,-3.822074,3.436447,-8.240750,6.180201,-8.073964,6.565324,-8.277161,-2.731891,-3.073715,-8.048653,-6.504842,7.741415,-9.304898,-8.415742,-3.625584,2.937502,1.794620,9.027937,-2.742376,3.800442,9.167907,5.764556,2.562491,9.793654,9.412933,-5.776451,-5.791067,3.281130,-3.426941,6.838146,1.202629,-4.914900,7.246170,-3.255584,-4.093144,-6.604604,0.496258,5.053496,-8.065713,-2.253765,0.734885,4.361887,-8.251089,-7.353666,-8.676392,5.706488,5.222432,-1.506350,-2.654623,-3.450201,6.207118,-7.929522,-8.944752,1.006035,7.156628,7.529020,-0.480599,-2.961086,1.243605,1.861722,-9.501959,-9.040318,-5.902494,0.200401,1.298017,5.345253,-0.003310,8.183030,-3.747895,9.420852,3.155282,-4.968306,-2.510371,-9.926588,0.357553,6.236006,3.268216,0.637758,7.312417,-5.974293,9.564921,3.445581,0.524138,-5.135092,6.110756,1.519856,-1.148905,-2.841382,4.926189,2.622157,-4.994516,-0.730154,-8.094342,-3.382050,-6.408562,-5.917950,-8.873564,-5.279880,5.381793,3.695878,-5.550344,1.639128,-5.846875,7.642696,-4.814030,1.467872,-1.871095,-3.928158,6.666850,-9.999442,5.314765,3.779199,-4.432578,-0.236766,4.233025,-3.367696,-8.644255,-2.304731,5.360501,-2.174134,-8.832187,-5.383183,-4.553536,4.560585,2.992733,6.714211,3.585657,9.551821,-3.978680,1.229011,1.806802,-2.153087,3.191360,3.721481,-3.709046,-5.525986,9.784745,2.790337,-4.702627,7.672381,-6.754184,-4.445288,-0.607603,8.590723,5.761009,-1.652014,-4.321402,2.624011,2.606224,-7.764666,-2.471383,8.520386,-8.210466,2.754636,4.475804,-5.482055,-7.857987,7.906187,-7.172000,7.670403,2.985682,5.388653,-1.037770,8.150850,3.616200,-4.376465,4.756594,5.694335,-8.205056,-0.708944,1.328695,-3.679204,7.483349,-4.014174,-9.747007,-6.535068,7.313456,-4.593620,-2.137397,-4.653876,4.025339,0.149749,-6.372845,-7.090640,-3.740404,-3.591198,-7.493252,3.849360,2.797927,9.113182,3.709107,7.031651,7.193974,4.990021,-4.153702,2.721589,-4.104389,-5.552614,2.312772,7.004085,9.841898,-7.881219,-6.099533,6.331075,2.577353,-3.867936,-6.952261,-8.929858,9.668717,7.249595,3.317045,8.250368,-0.912005,-4.869136,3.607026,1.902048,9.567435,-7.130368,8.843571,8.540044,-5.466386,3.865345,-2.596561,7.068774,0.069946,4.694068,1.322301,-1.482979,-8.301669,-2.493353,3.154643,-2.617507,3.310195,-5.009027,-7.193132,8.060753,9.033543,-3.677934,-7.524751,0.765380,-2.334731,-6.243417,-9.692384,6.513772,1.194810,-1.165793,2.255265,-9.323643,8.178909,9.723522,-7.604500,-5.532705,-1.397072,6.710310,-4.474060,-4.099717,9.502962,6.169121,-4.453309,-8.634795,-4.468664,-4.633976,3.568707,-7.513935,1.232187,8.434991,-6.226626,-9.545330,-8.788975,-9.164016,-2.842946,9.390351,0.206942,6.153808,-0.743274,-6.409294,-3.999251,-6.074660], dtype = "float32")#candidate|1636|(315,)|const|float32
call_1635 = func_1010_call(relay.reshape(const_1636.astype('float32'), [7, 15, 3]), relay.reshape(const_1636.astype('float32'), [7, 15, 3]), )
call_1637 = func_1010_call(relay.reshape(const_1636.astype('float32'), [7, 15, 3]), relay.reshape(const_1636.astype('float32'), [7, 15, 3]), )
output = relay.Tuple([call_1615,call_1627,var_1628,call_1635,const_1636,])
output2 = relay.Tuple([call_1616,call_1629,var_1628,call_1637,const_1636,])
func_1639 = relay.Function([var_1628,], output)
mod['func_1639'] = func_1639
mod = relay.transform.InferType()(mod)
mutated_mod['func_1639'] = func_1639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1640 = relay.var("var_1640", dtype = "float64", shape = (2025,))#candidate|1640|(2025,)|var|float64
func_1639_call = mutated_mod.get_global_var('func_1639')
call_1641 = func_1639_call(var_1640)
output = call_1641
func_1642 = relay.Function([var_1640], output)
mutated_mod['func_1642'] = func_1642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1532_call = mod.get_global_var('func_1532')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_1644 = func_1532_call()
call_1645 = func_1532_call()
output = relay.Tuple([call_1644,])
output2 = relay.Tuple([call_1645,])
func_1653 = relay.Function([], output)
mod['func_1653'] = func_1653
mod = relay.transform.InferType()(mod)
mutated_mod['func_1653'] = func_1653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mutated_mod.get_global_var('func_1653')
call_1654 = func_1653_call()
output = call_1654
func_1655 = relay.Function([], output)
mutated_mod['func_1655'] = func_1655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_1693 = func_1295_call()
call_1694 = func_1295_call()
output = call_1693
output2 = call_1694
func_1698 = relay.Function([], output)
mod['func_1698'] = func_1698
mod = relay.transform.InferType()(mod)
mutated_mod['func_1698'] = func_1698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1698_call = mutated_mod.get_global_var('func_1698')
call_1699 = func_1698_call()
output = call_1699
func_1700 = relay.Function([], output)
mutated_mod['func_1700'] = func_1700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_1759 = relay.TupleGetItem(func_1653_call(), 0)
call_1760 = relay.TupleGetItem(func_1655_call(), 0)
uop_1773 = relay.asinh(call_1759.astype('float32')) # shape=(2, 16, 4)
uop_1775 = relay.asinh(call_1760.astype('float32')) # shape=(2, 16, 4)
func_1506_call = mod.get_global_var('func_1506')
func_1507_call = mutated_mod.get_global_var('func_1507')
call_1784 = relay.TupleGetItem(func_1506_call(), 3)
call_1785 = relay.TupleGetItem(func_1507_call(), 3)
output = relay.Tuple([uop_1773,call_1784,])
output2 = relay.Tuple([uop_1775,call_1785,])
func_1798 = relay.Function([], output)
mod['func_1798'] = func_1798
mod = relay.transform.InferType()(mod)
output = func_1798()
func_1799 = relay.Function([], output)
mutated_mod['func_1799'] = func_1799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_1823 = relay.TupleGetItem(func_1653_call(), 0)
call_1824 = relay.TupleGetItem(func_1655_call(), 0)
var_1827 = relay.var("var_1827", dtype = "uint64", shape = (2, 16, 4))#candidate|1827|(2, 16, 4)|var|uint64
bop_1828 = relay.not_equal(call_1823.astype('bool'), relay.reshape(var_1827.astype('bool'), relay.shape_of(call_1823))) # shape=(2, 16, 4)
bop_1831 = relay.not_equal(call_1824.astype('bool'), relay.reshape(var_1827.astype('bool'), relay.shape_of(call_1824))) # shape=(2, 16, 4)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_1834 = func_1698_call()
call_1835 = func_1698_call()
uop_1842 = relay.sin(bop_1828.astype('float32')) # shape=(2, 16, 4)
uop_1844 = relay.sin(bop_1831.astype('float32')) # shape=(2, 16, 4)
output = relay.Tuple([call_1834,uop_1842,])
output2 = relay.Tuple([call_1835,uop_1844,])
func_1845 = relay.Function([var_1827,], output)
mod['func_1845'] = func_1845
mod = relay.transform.InferType()(mod)
mutated_mod['func_1845'] = func_1845
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1846 = relay.var("var_1846", dtype = "uint64", shape = (2, 16, 4))#candidate|1846|(2, 16, 4)|var|uint64
func_1845_call = mutated_mod.get_global_var('func_1845')
call_1847 = func_1845_call(var_1846)
output = call_1847
func_1848 = relay.Function([var_1846], output)
mutated_mod['func_1848'] = func_1848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1532_call = mod.get_global_var('func_1532')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_1938 = func_1532_call()
call_1939 = func_1532_call()
output = call_1938
output2 = call_1939
func_1946 = relay.Function([], output)
mod['func_1946'] = func_1946
mod = relay.transform.InferType()(mod)
output = func_1946()
func_1947 = relay.Function([], output)
mutated_mod['func_1947'] = func_1947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_1967 = relay.TupleGetItem(func_1653_call(), 0)
call_1968 = relay.TupleGetItem(func_1655_call(), 0)
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_1970 = relay.TupleGetItem(func_1653_call(), 0)
call_1971 = relay.TupleGetItem(func_1655_call(), 0)
bop_1985 = relay.bitwise_and(call_1967.astype('int16'), relay.reshape(call_1970.astype('int16'), relay.shape_of(call_1967))) # shape=(2, 16, 4)
bop_1988 = relay.bitwise_and(call_1968.astype('int16'), relay.reshape(call_1971.astype('int16'), relay.shape_of(call_1968))) # shape=(2, 16, 4)
bop_1994 = relay.logical_and(call_1967.astype('bool'), relay.reshape(bop_1985.astype('bool'), relay.shape_of(call_1967))) # shape=(2, 16, 4)
bop_1997 = relay.logical_and(call_1968.astype('bool'), relay.reshape(bop_1988.astype('bool'), relay.shape_of(call_1968))) # shape=(2, 16, 4)
bop_2007 = relay.logical_or(call_1967.astype('bool'), relay.reshape(call_1970.astype('bool'), relay.shape_of(call_1967))) # shape=(2, 16, 4)
bop_2010 = relay.logical_or(call_1968.astype('bool'), relay.reshape(call_1971.astype('bool'), relay.shape_of(call_1968))) # shape=(2, 16, 4)
func_380_call = mod.get_global_var('func_380')
func_383_call = mutated_mod.get_global_var('func_383')
var_2018 = relay.var("var_2018", dtype = "float32", shape = ())#candidate|2018|()|var|float32
const_2019 = relay.const([[-7.378456,-1.697780,-4.005014,0.015486,-9.761294,4.934767,-5.116127,9.135857,-3.519959,-1.694870,-5.393619,2.721873,-3.891012,9.376447,-5.273273,-2.409875,-6.516242,-2.457435,-0.807971,3.362573,6.719504,-5.288173,7.536442,4.103732,1.534226,8.529485,2.619639,-8.874386,4.898783,6.625857,-5.364463,-9.522747],[-7.383352,8.408169,-0.115642,-3.979157,-9.293599,-0.722121,-9.477747,8.035003,0.856089,-5.497905,5.487697,-0.940150,-1.372084,-4.960389,6.214175,-6.703423,-7.763276,4.922625,-7.250868,-9.865984,-6.204837,-1.617882,-9.339541,-5.494497,-0.276929,3.596826,7.538647,3.605690,3.691677,-2.784489,-0.425664,-8.890895],[-4.779216,-7.741939,5.493378,3.565294,2.510941,9.366757,4.150719,5.509147,-9.686595,8.606931,-2.226597,1.294109,0.426672,-6.252195,-2.312132,-4.170857,-0.749315,6.270371,0.122870,6.515775,5.194456,-0.917281,-2.192058,-8.546147,-9.663065,-1.522774,-0.627995,-9.741321,2.397236,-6.508937,-8.493504,4.064494],[3.366277,-1.779112,6.650717,7.550867,-1.040079,-0.642253,4.733179,0.966098,-2.221942,-6.545826,-5.069310,-8.566757,4.497514,6.180500,0.625041,1.003675,-8.699833,3.935041,7.727489,-7.698729,6.301228,9.428789,7.606051,-4.552858,-2.363135,5.703362,-5.430685,7.941805,-7.262750,4.161888,0.180652,-6.083578],[-8.619688,5.776809,-8.579383,-4.403498,-2.091528,-9.777220,-5.904133,-6.655214,5.403099,0.815970,4.365651,9.856521,-5.333247,-3.521046,3.368759,6.143043,-4.481346,-5.189519,-4.138533,-0.417119,-0.435085,-4.045002,-4.418284,6.652469,-0.506248,3.321690,8.923475,1.802452,1.402242,7.508642,-5.897617,-0.536406],[-2.243418,4.516746,9.574978,8.671963,-7.293314,4.312098,-4.344672,-2.603558,4.894635,9.480019,3.965196,-7.970845,-9.912594,1.279455,-9.582941,0.791182,-4.414407,6.523056,4.062891,6.433286,4.414489,-7.022761,-5.789881,-3.244759,-7.146175,-7.106594,9.763652,-7.096571,3.854217,-3.493704,3.567415,-1.791253],[8.303831,-0.669896,-5.425598,-0.030634,-9.215050,-1.773493,-7.694941,-1.310710,-9.604482,-6.540326,-7.297390,4.202879,-7.361179,0.053203,3.320349,-5.950082,-0.206047,5.384662,-9.075210,-1.606147,-1.671501,5.904353,6.425479,6.208529,9.862493,8.965991,-7.406926,2.986337,2.768807,1.691601,-7.662384,1.839615],[-7.517016,2.640795,-5.706178,9.831015,-8.167409,7.766245,-6.748826,4.505621,-6.013251,2.246314,7.096854,-4.172500,-2.257454,-9.279080,0.756491,4.393261,-8.431219,-5.367978,-5.733039,-8.033256,3.290424,-4.546446,-8.434408,6.720949,4.887607,-7.355641,9.420491,2.261684,-0.117751,-4.004268,7.826916,3.625924]], dtype = "float32")#candidate|2019|(8, 32)|const|float32
call_2017 = relay.TupleGetItem(func_380_call(relay.reshape(var_2018.astype('float32'), []), relay.reshape(const_2019.astype('float32'), [8, 32]), ), 0)
call_2020 = relay.TupleGetItem(func_383_call(relay.reshape(var_2018.astype('float32'), []), relay.reshape(const_2019.astype('float32'), [8, 32]), ), 0)
func_1597_call = mod.get_global_var('func_1597')
func_1598_call = mutated_mod.get_global_var('func_1598')
call_2023 = func_1597_call()
call_2024 = func_1597_call()
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_2036 = func_1698_call()
call_2037 = func_1698_call()
output = relay.Tuple([bop_1994,bop_2007,call_2017,var_2018,const_2019,call_2023,call_2036,])
output2 = relay.Tuple([bop_1997,bop_2010,call_2020,var_2018,const_2019,call_2024,call_2037,])
func_2038 = relay.Function([var_2018,], output)
mod['func_2038'] = func_2038
mod = relay.transform.InferType()(mod)
var_2039 = relay.var("var_2039", dtype = "float32", shape = ())#candidate|2039|()|var|float32
output = func_2038(var_2039)
func_2040 = relay.Function([var_2039], output)
mutated_mod['func_2040'] = func_2040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_2066 = relay.TupleGetItem(func_1653_call(), 0)
call_2067 = relay.TupleGetItem(func_1655_call(), 0)
output = call_2066
output2 = call_2067
func_2079 = relay.Function([], output)
mod['func_2079'] = func_2079
mod = relay.transform.InferType()(mod)
output = func_2079()
func_2080 = relay.Function([], output)
mutated_mod['func_2080'] = func_2080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_2170 = func_1698_call()
call_2171 = func_1698_call()
const_2174 = relay.const([[[-7,10,3,-8],[-2,-6,4,4],[8,-6,-2,-6],[-1,4,-5,3],[-9,7,-10,2],[8,10,-7,3],[-8,-10,7,7],[-9,5,3,7],[2,-6,6,4],[-6,-9,1,-2],[-10,9,-10,-5],[-7,-4,-8,-6],[2,-3,-2,6],[3,2,-9,3],[7,-7,8,8],[2,-8,3,-3]],[[8,7,2,5],[-1,9,3,9],[4,9,-8,9],[-8,-2,-3,-6],[-8,-8,-6,-10],[-3,-7,1,-4],[-2,8,9,1],[6,-8,8,-9],[-9,-1,-1,-4],[-9,9,-6,6],[-8,-9,-2,4],[-6,7,6,-2],[-3,2,1,-10],[-6,2,-4,2],[-3,-8,-3,-4],[-5,-3,-9,10]]], dtype = "uint64")#candidate|2174|(2, 16, 4)|const|uint64
bop_2175 = relay.greater_equal(call_2170.astype('bool'), relay.reshape(const_2174.astype('bool'), relay.shape_of(call_2170))) # shape=(2, 16, 4)
bop_2178 = relay.greater_equal(call_2171.astype('bool'), relay.reshape(const_2174.astype('bool'), relay.shape_of(call_2171))) # shape=(2, 16, 4)
func_729_call = mod.get_global_var('func_729')
func_731_call = mutated_mod.get_global_var('func_731')
var_2181 = relay.var("var_2181", dtype = "float64", shape = (2025,))#candidate|2181|(2025,)|var|float64
call_2180 = func_729_call(relay.reshape(var_2181.astype('float64'), [15, 15, 9]))
call_2182 = func_729_call(relay.reshape(var_2181.astype('float64'), [15, 15, 9]))
func_1010_call = mod.get_global_var('func_1010')
func_1014_call = mutated_mod.get_global_var('func_1014')
var_2188 = relay.var("var_2188", dtype = "float32", shape = (315,))#candidate|2188|(315,)|var|float32
call_2187 = func_1010_call(relay.reshape(var_2188.astype('float32'), [7, 15, 3]), relay.reshape(var_2188.astype('float32'), [7, 15, 3]), )
call_2189 = func_1010_call(relay.reshape(var_2188.astype('float32'), [7, 15, 3]), relay.reshape(var_2188.astype('float32'), [7, 15, 3]), )
output = relay.Tuple([bop_2175,call_2180,var_2181,call_2187,var_2188,])
output2 = relay.Tuple([bop_2178,call_2182,var_2181,call_2189,var_2188,])
func_2190 = relay.Function([var_2181,var_2188,], output)
mod['func_2190'] = func_2190
mod = relay.transform.InferType()(mod)
var_2191 = relay.var("var_2191", dtype = "float64", shape = (2025,))#candidate|2191|(2025,)|var|float64
var_2192 = relay.var("var_2192", dtype = "float32", shape = (315,))#candidate|2192|(315,)|var|float32
output = func_2190(var_2191,var_2192,)
func_2193 = relay.Function([var_2191,var_2192,], output)
mutated_mod['func_2193'] = func_2193
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2204 = relay.var("var_2204", dtype = "float32", shape = (15, 10, 2))#candidate|2204|(15, 10, 2)|var|float32
uop_2205 = relay.atanh(var_2204.astype('float32')) # shape=(15, 10, 2)
func_1639_call = mod.get_global_var('func_1639')
func_1642_call = mutated_mod.get_global_var('func_1642')
var_2210 = relay.var("var_2210", dtype = "float64", shape = (2025,))#candidate|2210|(2025,)|var|float64
call_2209 = relay.TupleGetItem(func_1639_call(relay.reshape(var_2210.astype('float64'), [2025,])), 1)
call_2211 = relay.TupleGetItem(func_1642_call(relay.reshape(var_2210.astype('float64'), [2025,])), 1)
output = relay.Tuple([uop_2205,call_2209,var_2210,])
output2 = relay.Tuple([uop_2205,call_2211,var_2210,])
func_2220 = relay.Function([var_2204,var_2210,], output)
mod['func_2220'] = func_2220
mod = relay.transform.InferType()(mod)
var_2221 = relay.var("var_2221", dtype = "float32", shape = (15, 10, 2))#candidate|2221|(15, 10, 2)|var|float32
var_2222 = relay.var("var_2222", dtype = "float64", shape = (2025,))#candidate|2222|(2025,)|var|float64
output = func_2220(var_2221,var_2222,)
func_2223 = relay.Function([var_2221,var_2222,], output)
mutated_mod['func_2223'] = func_2223
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2300 = relay.var("var_2300", dtype = "float32", shape = (11, 15, 8))#candidate|2300|(11, 15, 8)|var|float32
uop_2301 = relay.acos(var_2300.astype('float32')) # shape=(11, 15, 8)
output = uop_2301
output2 = uop_2301
func_2305 = relay.Function([var_2300,], output)
mod['func_2305'] = func_2305
mod = relay.transform.InferType()(mod)
var_2306 = relay.var("var_2306", dtype = "float32", shape = (11, 15, 8))#candidate|2306|(11, 15, 8)|var|float32
output = func_2305(var_2306)
func_2307 = relay.Function([var_2306], output)
mutated_mod['func_2307'] = func_2307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_2377 = func_1295_call()
call_2378 = func_1295_call()
output = call_2377
output2 = call_2378
func_2385 = relay.Function([], output)
mod['func_2385'] = func_2385
mod = relay.transform.InferType()(mod)
mutated_mod['func_2385'] = func_2385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2385_call = mutated_mod.get_global_var('func_2385')
call_2386 = func_2385_call()
output = call_2386
func_2387 = relay.Function([], output)
mutated_mod['func_2387'] = func_2387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2079_call = mod.get_global_var('func_2079')
func_2080_call = mutated_mod.get_global_var('func_2080')
call_2395 = func_2079_call()
call_2396 = func_2079_call()
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_2411 = func_1698_call()
call_2412 = func_1698_call()
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_2418 = func_2385_call()
call_2419 = func_2385_call()
func_2220_call = mod.get_global_var('func_2220')
func_2223_call = mutated_mod.get_global_var('func_2223')
const_2422 = relay.const([-0.093653,2.974963,-3.664196,-6.173761,-0.478813,3.584323,-5.874341,-2.154504,-1.688753,-8.914084,1.807729,-0.862375,2.522784,-0.335074,-0.813319,-6.767748,-8.554420,-5.196210,2.195453,8.617625,8.327938,8.257183,-4.285989,1.580839,-7.221938,4.977855,3.053154,6.893404,3.561273,-5.290508,5.256850,-7.512096,-8.526381,0.257461,5.431934,1.038990,6.367548,4.468047,2.098205,-0.273303,-8.502954,0.859641,7.979936,7.512607,-2.465475,1.014161,-4.808158,5.888338,-1.172080,-2.608934,-1.971413,-0.901285,-8.423229,4.365964,6.239567,-0.564913,4.896548,9.012102,-4.259270,9.841417,-6.712957,4.114081,3.421797,-6.762858,2.224799,5.507043,-4.689776,1.216362,2.966857,-3.390088,7.768838,2.839506,-2.564884,5.384083,7.425671,6.327647,9.465013,-9.090046,-8.779672,7.174263,6.528437,2.138199,-9.559095,3.161981,5.140068,-6.319206,-4.855397,-4.179927,5.627381,1.883933,-1.552868,-0.742786,1.812117,-6.646181,0.657630,1.162497,5.522603,7.724488,-7.988225,8.727433,-5.756390,-1.931959,8.920042,-9.786024,-5.909095,4.851998,-9.392935,9.183833,-6.932040,4.798100,3.759627,3.720886,1.556752,-0.516847,7.439570,-6.251208,-6.290761,-1.185318,4.141080,-9.745634,-5.933247,-6.261149,1.073429,9.092713,-5.616905,-8.552336,0.634063,-2.099146,-5.827098,-9.538224,-7.815801,8.619428,7.014090,1.105840,-7.852901,7.992603,5.883068,-5.706915,7.793359,3.102054,-7.523569,1.540858,9.097592,5.027293,-7.012370,3.352055,-5.131061,2.078103,-5.134778,-9.737113,-5.173391,3.040880,6.128405,1.604701,0.857577,-1.841841,-1.920997,-7.919919,4.274218,5.568644,9.363450,9.520147,2.953213,-7.525153,8.349219,4.913442,-4.986889,1.888336,-2.116209,-3.812429,5.838241,6.397971,-4.732765,5.782660,1.770790,0.677944,3.301486,-1.525395,-9.953235,-4.995477,4.252182,7.889023,5.396951,-1.790166,2.815136,9.152180,8.158268,-9.873685,-1.235135,-7.781402,-6.195418,7.368955,-0.081786,3.264046,-5.597503,-2.774129,3.400249,7.687136,-3.182721,-9.733154,-9.154600,3.006716,-2.257014,5.868276,7.579960,7.127910,3.482917,-3.132176,-0.052789,-8.195415,4.620899,3.001643,1.522385,2.913136,-7.634216,3.542691,-6.283070,-3.669809,4.300193,5.414012,1.509633,-7.670700,4.142223,-3.495729,-6.003500,-4.049970,8.446165,-4.974056,-3.585850,9.288422,8.165843,2.451686,7.864528,1.497242,2.677903,1.331006,9.972974,-9.182763,-9.367415,-0.714079,8.537120,9.041889,-2.009470,5.645855,6.003070,0.803163,-6.422381,-6.853791,4.119629,-6.060394,3.553941,8.735119,9.258351,3.192163,5.801771,1.972485,9.839495,7.083988,-6.078848,-8.419435,5.559947,3.851762,5.600614,3.408298,0.044372,1.905246,-1.921276,9.327444,-7.428971,0.420116,-7.848177,8.859799,9.811653,-1.910901,7.956501,-1.633637,-8.518437,-3.649876,7.383690,-5.823306,3.785382,0.898875,6.959503,-1.761461,-2.144608,0.430327,-9.941441,-7.646351,3.493973,7.706810,0.750070,-5.077470,7.352287,7.647447,-2.814459,6.715534,-4.012207,3.481857,9.848614,8.926042], dtype = "float32")#candidate|2422|(300,)|const|float32
var_2423 = relay.var("var_2423", dtype = "float64", shape = (2025,))#candidate|2423|(2025,)|var|float64
call_2421 = relay.TupleGetItem(func_2220_call(relay.reshape(const_2422.astype('float32'), [15, 10, 2]), relay.reshape(var_2423.astype('float64'), [2025,]), ), 0)
call_2424 = relay.TupleGetItem(func_2223_call(relay.reshape(const_2422.astype('float32'), [15, 10, 2]), relay.reshape(var_2423.astype('float64'), [2025,]), ), 0)
output = relay.Tuple([call_2395,call_2411,call_2418,call_2421,const_2422,var_2423,])
output2 = relay.Tuple([call_2396,call_2412,call_2419,call_2424,const_2422,var_2423,])
func_2426 = relay.Function([var_2423,], output)
mod['func_2426'] = func_2426
mod = relay.transform.InferType()(mod)
var_2427 = relay.var("var_2427", dtype = "float64", shape = (2025,))#candidate|2427|(2025,)|var|float64
output = func_2426(var_2427)
func_2428 = relay.Function([var_2427], output)
mutated_mod['func_2428'] = func_2428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2449 = relay.var("var_2449", dtype = "uint16", shape = (8, 13, 5))#candidate|2449|(8, 13, 5)|var|uint16
const_2450 = relay.const([[[-8,7,-3,-2,-8],[-4,-5,-4,5,-6],[7,2,6,-2,9],[-4,-6,-7,-5,-4],[9,7,10,-6,7],[7,-1,-3,-10,-8],[9,-6,-5,6,1],[-5,9,-4,-3,-3],[-4,8,3,6,8],[-2,8,-2,10,2],[-9,4,9,6,-8],[-6,-9,-10,8,6],[10,3,-8,8,4]],[[-1,-9,10,3,-3],[4,5,-4,8,1],[-7,3,-6,4,1],[7,10,7,5,-5],[4,8,5,-4,-5],[8,-5,-10,2,-8],[2,2,-3,-2,-2],[-7,-6,-6,8,-5],[-5,2,2,3,-6],[6,8,9,-9,-2],[-8,7,-3,-9,3],[3,-5,-9,7,-10],[5,-2,-5,6,4]],[[7,6,-9,7,1],[10,-7,9,3,-10],[-10,8,-9,6,7],[1,3,-7,6,10],[5,1,6,-10,5],[-1,-6,-10,-4,-8],[6,6,-9,-2,9],[4,2,6,5,-5],[5,-9,7,-3,4],[1,-5,9,-9,8],[-1,-10,10,-10,-1],[7,-3,6,-6,8],[-4,-1,-5,2,-9]],[[2,5,-4,-7,9],[-1,5,-3,-1,-1],[10,-9,4,-9,-8],[9,10,-1,10,-9],[5,7,4,-10,-10],[6,-8,-1,9,-1],[2,-8,-5,-7,4],[-5,-7,-10,2,-6],[10,-4,-6,-1,9],[-3,-3,3,9,-2],[-9,-3,-9,5,-2],[-6,2,-1,7,5],[-5,6,9,-5,-1]],[[-1,-5,-5,7,8],[3,-2,-5,3,-6],[-9,7,8,-5,4],[9,6,-2,-10,3],[10,1,-10,6,10],[2,-2,5,6,-2],[-5,8,7,-2,-2],[-5,10,-6,-4,-6],[4,-4,-6,6,-8],[-2,9,4,-1,3],[3,6,5,6,4],[-4,9,-5,-8,6],[-9,-8,-8,8,-1]],[[5,-10,7,-4,-5],[-6,-7,8,7,2],[1,-2,4,1,3],[3,-6,-10,-8,-8],[3,1,-7,1,-4],[-9,-6,4,-3,2],[-9,-6,9,7,-10],[-10,9,10,-2,-1],[-4,3,-3,10,4],[-4,10,-7,5,6],[-9,6,-2,5,7],[-2,8,1,-4,9],[-6,2,-4,4,-1]],[[5,-9,-9,9,-6],[-9,7,4,9,10],[8,3,-1,7,6],[-6,-1,4,-5,-3],[1,-9,-9,6,-3],[-6,-4,10,-5,9],[-6,-6,9,6,-5],[4,1,4,-6,-8],[9,-1,4,-8,-10],[-4,-1,5,2,-3],[2,-3,-9,-5,-7],[8,-10,9,-10,-4],[-4,-7,9,-5,5]],[[8,-3,2,-5,-1],[-3,-10,-7,4,-8],[8,-9,8,-8,8],[1,5,-6,8,-6],[-6,7,2,5,-1],[-6,-4,7,2,-5],[1,8,-9,-2,6],[7,9,-9,10,-6],[-6,4,-7,4,-6],[-10,6,-2,-2,4],[-6,-1,-9,-5,4],[-1,-4,-4,4,8],[8,9,-6,1,-9]]], dtype = "uint16")#candidate|2450|(8, 13, 5)|const|uint16
bop_2451 = relay.add(var_2449.astype('uint16'), relay.reshape(const_2450.astype('uint16'), relay.shape_of(var_2449))) # shape=(8, 13, 5)
func_2038_call = mod.get_global_var('func_2038')
func_2040_call = mutated_mod.get_global_var('func_2040')
var_2455 = relay.var("var_2455", dtype = "float32", shape = ())#candidate|2455|()|var|float32
call_2454 = relay.TupleGetItem(func_2038_call(relay.reshape(var_2455.astype('float32'), [])), 4)
call_2456 = relay.TupleGetItem(func_2040_call(relay.reshape(var_2455.astype('float32'), [])), 4)
output = relay.Tuple([bop_2451,call_2454,var_2455,])
output2 = relay.Tuple([bop_2451,call_2456,var_2455,])
func_2459 = relay.Function([var_2449,var_2455,], output)
mod['func_2459'] = func_2459
mod = relay.transform.InferType()(mod)
var_2460 = relay.var("var_2460", dtype = "uint16", shape = (8, 13, 5))#candidate|2460|(8, 13, 5)|var|uint16
var_2461 = relay.var("var_2461", dtype = "float32", shape = ())#candidate|2461|()|var|float32
output = func_2459(var_2460,var_2461,)
func_2462 = relay.Function([var_2460,var_2461,], output)
mutated_mod['func_2462'] = func_2462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_2483 = func_1295_call()
call_2484 = func_1295_call()
uop_2486 = relay.sinh(call_2483.astype('float32')) # shape=(2, 16, 4)
uop_2488 = relay.sinh(call_2484.astype('float32')) # shape=(2, 16, 4)
output = relay.Tuple([uop_2486,])
output2 = relay.Tuple([uop_2488,])
func_2491 = relay.Function([], output)
mod['func_2491'] = func_2491
mod = relay.transform.InferType()(mod)
output = func_2491()
func_2492 = relay.Function([], output)
mutated_mod['func_2492'] = func_2492
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2601 = relay.var("var_2601", dtype = "float64", shape = (2, 3, 8))#candidate|2601|(2, 3, 8)|var|float64
uop_2602 = relay.sigmoid(var_2601.astype('float64')) # shape=(2, 3, 8)
bop_2605 = relay.bitwise_xor(uop_2602.astype('int8'), relay.reshape(var_2601.astype('int8'), relay.shape_of(uop_2602))) # shape=(2, 3, 8)
output = bop_2605
output2 = bop_2605
func_2634 = relay.Function([var_2601,], output)
mod['func_2634'] = func_2634
mod = relay.transform.InferType()(mod)
mutated_mod['func_2634'] = func_2634
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2635 = relay.var("var_2635", dtype = "float64", shape = (2, 3, 8))#candidate|2635|(2, 3, 8)|var|float64
func_2634_call = mutated_mod.get_global_var('func_2634')
call_2636 = func_2634_call(var_2635)
output = call_2636
func_2637 = relay.Function([var_2635], output)
mutated_mod['func_2637'] = func_2637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_2702 = func_1295_call()
call_2703 = func_1295_call()
output = call_2702
output2 = call_2703
func_2708 = relay.Function([], output)
mod['func_2708'] = func_2708
mod = relay.transform.InferType()(mod)
output = func_2708()
func_2709 = relay.Function([], output)
mutated_mod['func_2709'] = func_2709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1506_call = mod.get_global_var('func_1506')
func_1507_call = mutated_mod.get_global_var('func_1507')
call_2717 = relay.TupleGetItem(func_1506_call(), 1)
call_2718 = relay.TupleGetItem(func_1507_call(), 1)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_2728 = func_1295_call()
call_2729 = func_1295_call()
output = relay.Tuple([call_2717,call_2728,])
output2 = relay.Tuple([call_2718,call_2729,])
func_2733 = relay.Function([], output)
mod['func_2733'] = func_2733
mod = relay.transform.InferType()(mod)
output = func_2733()
func_2734 = relay.Function([], output)
mutated_mod['func_2734'] = func_2734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2079_call = mod.get_global_var('func_2079')
func_2080_call = mutated_mod.get_global_var('func_2080')
call_2774 = func_2079_call()
call_2775 = func_2079_call()
func_1946_call = mod.get_global_var('func_1946')
func_1947_call = mutated_mod.get_global_var('func_1947')
call_2785 = func_1946_call()
call_2786 = func_1946_call()
func_2733_call = mod.get_global_var('func_2733')
func_2734_call = mutated_mod.get_global_var('func_2734')
call_2811 = relay.TupleGetItem(func_2733_call(), 1)
call_2812 = relay.TupleGetItem(func_2734_call(), 1)
output = relay.Tuple([call_2774,call_2785,call_2811,])
output2 = relay.Tuple([call_2775,call_2786,call_2812,])
func_2816 = relay.Function([], output)
mod['func_2816'] = func_2816
mod = relay.transform.InferType()(mod)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mutated_mod.get_global_var('func_2816')
call_2817 = func_2816_call()
output = call_2817
func_2818 = relay.Function([], output)
mutated_mod['func_2818'] = func_2818
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2892 = relay.const([[[-2],[2],[6],[-1],[-3],[-6],[-10],[-9],[5],[-1],[6],[-5],[9],[-5],[-1]],[[-7],[-1],[3],[8],[-8],[2],[-8],[-2],[3],[6],[8],[10],[-8],[9],[1]],[[6],[-5],[9],[-4],[3],[-8],[5],[5],[4],[7],[-4],[3],[8],[-6],[-5]],[[-7],[7],[9],[1],[2],[5],[-8],[7],[-8],[-3],[-10],[1],[2],[7],[8]],[[-5],[2],[-10],[-7],[-4],[4],[-9],[2],[6],[-9],[-6],[-6],[4],[-8],[-6]],[[-2],[5],[2],[-7],[-6],[-7],[10],[3],[-4],[-1],[-7],[-5],[6],[1],[-2]],[[-2],[7],[-10],[-1],[-7],[8],[7],[2],[10],[-8],[10],[-2],[10],[-4],[-1]],[[7],[1],[-3],[2],[-8],[2],[5],[-3],[-1],[4],[8],[7],[-8],[-7],[8]],[[-1],[5],[9],[-2],[1],[2],[-7],[-3],[3],[-5],[-3],[8],[4],[-7],[-10]],[[-1],[9],[2],[-2],[-1],[-8],[8],[-7],[6],[-5],[6],[6],[10],[-1],[1]],[[3],[4],[-7],[-2],[-5],[-6],[5],[8],[5],[1],[-7],[-9],[-10],[-4],[-9]],[[4],[-8],[6],[7],[8],[10],[-4],[-6],[-6],[-8],[-2],[-5],[-7],[2],[-7]],[[8],[-3],[-4],[-4],[6],[4],[4],[10],[2],[-10],[4],[-3],[-2],[5],[2]],[[7],[5],[-6],[8],[9],[-2],[1],[-3],[-5],[-8],[3],[-10],[2],[-9],[-8]]], dtype = "uint8")#candidate|2892|(14, 15, 1)|const|uint8
var_2893 = relay.var("var_2893", dtype = "uint8", shape = (14, 15, 2))#candidate|2893|(14, 15, 2)|var|uint8
bop_2894 = relay.multiply(const_2892.astype('uint8'), var_2893.astype('uint8')) # shape=(14, 15, 2)
const_2898 = relay.const([[[-5,10],[4,-8],[1,-5],[10,9],[-4,-2],[4,-3],[-1,4],[3,7],[-3,-10],[6,-3],[-8,9],[2,-5],[-8,-1],[6,-3],[-6,-6]],[[-10,-7],[-1,-9],[-6,1],[3,-9],[9,-9],[4,1],[3,8],[10,-6],[-8,-3],[-9,3],[7,7],[-7,2],[4,-5],[1,-10],[-10,4]],[[2,-2],[3,9],[-8,-7],[-8,4],[3,-3],[9,-5],[2,5],[-4,3],[8,-6],[1,-3],[8,5],[-4,-5],[-6,4],[-4,6],[-4,9]],[[-1,-4],[6,-2],[-7,-5],[4,-5],[10,5],[-6,-1],[-8,8],[1,10],[8,3],[-5,-10],[-1,-7],[6,5],[-10,1],[-9,-8],[-9,-9]],[[-4,4],[-4,-7],[-3,3],[-3,-9],[2,6],[-4,2],[9,-10],[-6,1],[-9,-3],[2,-4],[-6,-7],[7,9],[-1,5],[-2,-7],[-5,-9]],[[6,-3],[5,-10],[4,1],[2,1],[5,-1],[5,-2],[-1,7],[-5,-8],[-8,-10],[7,-1],[-5,-2],[-10,6],[-3,4],[3,4],[-4,-1]],[[-7,2],[2,-10],[1,1],[-2,2],[-6,-1],[-5,8],[8,1],[2,3],[-1,-7],[-6,-3],[8,6],[6,4],[-6,2],[10,1],[-1,10]],[[-6,-5],[7,-1],[10,-3],[-5,10],[6,-5],[9,-8],[-7,-6],[3,2],[-8,-8],[2,1],[3,-2],[-2,-2],[-8,-3],[-2,5],[1,-8]],[[9,4],[8,6],[1,-3],[1,3],[-10,2],[-1,5],[9,3],[-3,-6],[10,2],[2,-1],[5,-9],[1,-8],[8,9],[8,-3],[3,-6]],[[-8,1],[-2,7],[2,1],[1,-2],[4,3],[1,-1],[5,-7],[-9,-7],[7,6],[-2,7],[10,1],[-8,4],[-4,-3],[-9,5],[8,2]],[[-7,6],[-8,3],[-5,8],[-8,7],[-2,7],[-1,3],[5,-4],[10,-10],[-7,-2],[7,9],[-8,7],[3,-2],[-8,3],[1,9],[-3,-7]],[[-9,1],[3,2],[-9,-2],[-5,-2],[7,-7],[5,4],[3,-10],[-6,-9],[-5,-2],[-4,-8],[5,-1],[-3,3],[7,4],[-8,-7],[-2,9]],[[-5,-3],[-9,-9],[-9,-9],[7,9],[2,-9],[-9,-2],[9,-10],[-8,9],[7,6],[-8,2],[-9,4],[-10,-7],[4,-3],[9,4],[9,-9]],[[2,2],[1,-7],[2,8],[10,-9],[-6,5],[2,-5],[-7,9],[2,5],[-7,5],[-7,-10],[-4,10],[10,-6],[-6,8],[-1,9],[3,-4]]], dtype = "uint8")#candidate|2898|(14, 15, 2)|const|uint8
bop_2899 = relay.logical_or(var_2893.astype('bool'), relay.reshape(const_2898.astype('bool'), relay.shape_of(var_2893))) # shape=(14, 15, 2)
output = relay.Tuple([bop_2894,bop_2899,])
output2 = relay.Tuple([bop_2894,bop_2899,])
func_2912 = relay.Function([var_2893,], output)
mod['func_2912'] = func_2912
mod = relay.transform.InferType()(mod)
mutated_mod['func_2912'] = func_2912
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2913 = relay.var("var_2913", dtype = "uint8", shape = (14, 15, 2))#candidate|2913|(14, 15, 2)|var|uint8
func_2912_call = mutated_mod.get_global_var('func_2912')
call_2914 = func_2912_call(var_2913)
output = call_2914
func_2915 = relay.Function([var_2913], output)
mutated_mod['func_2915'] = func_2915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2708_call = mod.get_global_var('func_2708')
func_2709_call = mutated_mod.get_global_var('func_2709')
call_2920 = func_2708_call()
call_2921 = func_2708_call()
func_1532_call = mod.get_global_var('func_1532')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_2927 = func_1532_call()
call_2928 = func_1532_call()
uop_2941 = relay.erf(call_2927.astype('float32')) # shape=(2, 16, 4)
uop_2943 = relay.erf(call_2928.astype('float32')) # shape=(2, 16, 4)
uop_2950 = relay.tan(uop_2941.astype('float64')) # shape=(2, 16, 4)
uop_2952 = relay.tan(uop_2943.astype('float64')) # shape=(2, 16, 4)
var_2958 = relay.var("var_2958", dtype = "float64", shape = (2, 16, 4))#candidate|2958|(2, 16, 4)|var|float64
bop_2959 = relay.right_shift(uop_2950.astype('uint16'), relay.reshape(var_2958.astype('uint16'), relay.shape_of(uop_2950))) # shape=(2, 16, 4)
bop_2962 = relay.right_shift(uop_2952.astype('uint16'), relay.reshape(var_2958.astype('uint16'), relay.shape_of(uop_2952))) # shape=(2, 16, 4)
bop_2963 = relay.floor_mod(call_2927.astype('float64'), relay.reshape(var_2958.astype('float64'), relay.shape_of(call_2927))) # shape=(2, 16, 4)
bop_2966 = relay.floor_mod(call_2928.astype('float64'), relay.reshape(var_2958.astype('float64'), relay.shape_of(call_2928))) # shape=(2, 16, 4)
uop_2971 = relay.log10(uop_2950.astype('float64')) # shape=(2, 16, 4)
uop_2973 = relay.log10(uop_2952.astype('float64')) # shape=(2, 16, 4)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_2979 = relay.TupleGetItem(func_2816_call(), 2)
call_2980 = relay.TupleGetItem(func_2818_call(), 2)
uop_2983 = relay.asin(uop_2971.astype('float64')) # shape=(2, 16, 4)
uop_2985 = relay.asin(uop_2973.astype('float64')) # shape=(2, 16, 4)
output = relay.Tuple([call_2920,bop_2959,bop_2963,call_2979,uop_2983,])
output2 = relay.Tuple([call_2921,bop_2962,bop_2966,call_2980,uop_2985,])
func_2990 = relay.Function([var_2958,], output)
mod['func_2990'] = func_2990
mod = relay.transform.InferType()(mod)
var_2991 = relay.var("var_2991", dtype = "float64", shape = (2, 16, 4))#candidate|2991|(2, 16, 4)|var|float64
output = func_2990(var_2991)
func_2992 = relay.Function([var_2991], output)
mutated_mod['func_2992'] = func_2992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2708_call = mod.get_global_var('func_2708')
func_2709_call = mutated_mod.get_global_var('func_2709')
call_3008 = func_2708_call()
call_3009 = func_2708_call()
output = relay.Tuple([call_3008,])
output2 = relay.Tuple([call_3009,])
func_3012 = relay.Function([], output)
mod['func_3012'] = func_3012
mod = relay.transform.InferType()(mod)
output = func_3012()
func_3013 = relay.Function([], output)
mutated_mod['func_3013'] = func_3013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2733_call = mod.get_global_var('func_2733')
func_2734_call = mutated_mod.get_global_var('func_2734')
call_3042 = relay.TupleGetItem(func_2733_call(), 0)
call_3043 = relay.TupleGetItem(func_2734_call(), 0)
output = call_3042
output2 = call_3043
func_3050 = relay.Function([], output)
mod['func_3050'] = func_3050
mod = relay.transform.InferType()(mod)
mutated_mod['func_3050'] = func_3050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3050_call = mutated_mod.get_global_var('func_3050')
call_3051 = func_3050_call()
output = call_3051
func_3052 = relay.Function([], output)
mutated_mod['func_3052'] = func_3052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1946_call = mod.get_global_var('func_1946')
func_1947_call = mutated_mod.get_global_var('func_1947')
call_3105 = func_1946_call()
call_3106 = func_1946_call()
func_2634_call = mod.get_global_var('func_2634')
func_2637_call = mutated_mod.get_global_var('func_2637')
const_3126 = relay.const([9.046541,-0.007003,3.460211,8.985128,-5.909293,6.358937,8.291487,-3.768648,0.428797,-2.960112,-5.435525,-8.571708,-2.686993,9.752429,-7.848952,-2.140706,-1.859961,8.565348,-9.529955,0.922489,7.925421,-1.286576,2.198382,2.915855,-2.573508,2.836420,0.510122,8.028658,5.102331,4.823328,1.780133,0.142531,-5.492508,5.195104,8.669060,-3.920076,0.806278,2.404668,3.660690,8.593256,2.487983,-9.792898,2.335724,-3.005487,-1.897725,-7.193125,6.787485,5.711139], dtype = "float64")#candidate|3126|(48,)|const|float64
call_3125 = func_2634_call(relay.reshape(const_3126.astype('float64'), [2, 3, 8]))
call_3127 = func_2634_call(relay.reshape(const_3126.astype('float64'), [2, 3, 8]))
output = relay.Tuple([call_3105,call_3125,const_3126,])
output2 = relay.Tuple([call_3106,call_3127,const_3126,])
func_3129 = relay.Function([], output)
mod['func_3129'] = func_3129
mod = relay.transform.InferType()(mod)
output = func_3129()
func_3130 = relay.Function([], output)
mutated_mod['func_3130'] = func_3130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3012_call = mod.get_global_var('func_3012')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_3152 = relay.TupleGetItem(func_3012_call(), 0)
call_3153 = relay.TupleGetItem(func_3013_call(), 0)
var_3179 = relay.var("var_3179", dtype = "uint64", shape = (2, 16, 4))#candidate|3179|(2, 16, 4)|var|uint64
bop_3180 = relay.left_shift(call_3152.astype('uint16'), relay.reshape(var_3179.astype('uint16'), relay.shape_of(call_3152))) # shape=(2, 16, 4)
bop_3183 = relay.left_shift(call_3153.astype('uint16'), relay.reshape(var_3179.astype('uint16'), relay.shape_of(call_3153))) # shape=(2, 16, 4)
output = relay.Tuple([bop_3180,])
output2 = relay.Tuple([bop_3183,])
func_3184 = relay.Function([var_3179,], output)
mod['func_3184'] = func_3184
mod = relay.transform.InferType()(mod)
mutated_mod['func_3184'] = func_3184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3185 = relay.var("var_3185", dtype = "uint64", shape = (2, 16, 4))#candidate|3185|(2, 16, 4)|var|uint64
func_3184_call = mutated_mod.get_global_var('func_3184')
call_3186 = func_3184_call(var_3185)
output = call_3186
func_3187 = relay.Function([var_3185], output)
mutated_mod['func_3187'] = func_3187
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3264 = relay.var("var_3264", dtype = "uint32", shape = (6, 2, 16))#candidate|3264|(6, 2, 16)|var|uint32
var_3265 = relay.var("var_3265", dtype = "uint32", shape = (6, 2, 16))#candidate|3265|(6, 2, 16)|var|uint32
bop_3266 = relay.bitwise_or(var_3264.astype('uint32'), relay.reshape(var_3265.astype('uint32'), relay.shape_of(var_3264))) # shape=(6, 2, 16)
func_729_call = mod.get_global_var('func_729')
func_731_call = mutated_mod.get_global_var('func_731')
var_3270 = relay.var("var_3270", dtype = "float64", shape = (2025,))#candidate|3270|(2025,)|var|float64
call_3269 = func_729_call(relay.reshape(var_3270.astype('float64'), [15, 15, 9]))
call_3271 = func_729_call(relay.reshape(var_3270.astype('float64'), [15, 15, 9]))
bop_3282 = relay.equal(var_3264.astype('bool'), relay.reshape(var_3265.astype('bool'), relay.shape_of(var_3264))) # shape=(6, 2, 16)
uop_3287 = relay.sin(call_3269.astype('float32')) # shape=(15, 15, 9)
uop_3289 = relay.sin(call_3271.astype('float32')) # shape=(15, 15, 9)
bop_3290 = relay.left_shift(uop_3287.astype('int16'), relay.reshape(var_3270.astype('int16'), relay.shape_of(uop_3287))) # shape=(15, 15, 9)
bop_3293 = relay.left_shift(uop_3289.astype('int16'), relay.reshape(var_3270.astype('int16'), relay.shape_of(uop_3289))) # shape=(15, 15, 9)
bop_3295 = relay.logical_and(uop_3287.astype('bool'), relay.reshape(var_3270.astype('bool'), relay.shape_of(uop_3287))) # shape=(15, 15, 9)
bop_3298 = relay.logical_and(uop_3289.astype('bool'), relay.reshape(var_3270.astype('bool'), relay.shape_of(uop_3289))) # shape=(15, 15, 9)
output = relay.Tuple([bop_3266,bop_3282,bop_3290,bop_3295,])
output2 = relay.Tuple([bop_3266,bop_3282,bop_3293,bop_3298,])
func_3299 = relay.Function([var_3264,var_3265,var_3270,], output)
mod['func_3299'] = func_3299
mod = relay.transform.InferType()(mod)
mutated_mod['func_3299'] = func_3299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3299_call = mutated_mod.get_global_var('func_3299')
var_3301 = relay.var("var_3301", dtype = "uint32", shape = (6, 2, 16))#candidate|3301|(6, 2, 16)|var|uint32
var_3302 = relay.var("var_3302", dtype = "uint32", shape = (6, 2, 16))#candidate|3302|(6, 2, 16)|var|uint32
var_3303 = relay.var("var_3303", dtype = "float64", shape = (2025,))#candidate|3303|(2025,)|var|float64
call_3300 = func_3299_call(var_3301,var_3302,var_3303,)
output = call_3300
func_3304 = relay.Function([var_3301,var_3302,var_3303,], output)
mutated_mod['func_3304'] = func_3304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1532_call = mod.get_global_var('func_1532')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_3327 = func_1532_call()
call_3328 = func_1532_call()
output = relay.Tuple([call_3327,])
output2 = relay.Tuple([call_3328,])
func_3333 = relay.Function([], output)
mod['func_3333'] = func_3333
mod = relay.transform.InferType()(mod)
output = func_3333()
func_3334 = relay.Function([], output)
mutated_mod['func_3334'] = func_3334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1598_call = mutated_mod.get_global_var('func_1598')
call_3383 = func_1597_call()
call_3384 = func_1597_call()
output = call_3383
output2 = call_3384
func_3391 = relay.Function([], output)
mod['func_3391'] = func_3391
mod = relay.transform.InferType()(mod)
mutated_mod['func_3391'] = func_3391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3391_call = mutated_mod.get_global_var('func_3391')
call_3392 = func_3391_call()
output = call_3392
func_3393 = relay.Function([], output)
mutated_mod['func_3393'] = func_3393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1946_call = mod.get_global_var('func_1946')
func_1947_call = mutated_mod.get_global_var('func_1947')
call_3394 = func_1946_call()
call_3395 = func_1946_call()
output = relay.Tuple([call_3394,])
output2 = relay.Tuple([call_3395,])
func_3401 = relay.Function([], output)
mod['func_3401'] = func_3401
mod = relay.transform.InferType()(mod)
mutated_mod['func_3401'] = func_3401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3401_call = mutated_mod.get_global_var('func_3401')
call_3402 = func_3401_call()
output = call_3402
func_3403 = relay.Function([], output)
mutated_mod['func_3403'] = func_3403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1506_call = mod.get_global_var('func_1506')
func_1507_call = mutated_mod.get_global_var('func_1507')
call_3425 = relay.TupleGetItem(func_1506_call(), 7)
call_3426 = relay.TupleGetItem(func_1507_call(), 7)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_3427 = func_1698_call()
call_3428 = func_1698_call()
var_3434 = relay.var("var_3434", dtype = "float64", shape = (4, 10, 9))#candidate|3434|(4, 10, 9)|var|float64
bop_3435 = relay.divide(call_3425.astype('float64'), relay.reshape(var_3434.astype('float64'), relay.shape_of(call_3425))) # shape=(4, 10, 9)
bop_3438 = relay.divide(call_3426.astype('float64'), relay.reshape(var_3434.astype('float64'), relay.shape_of(call_3426))) # shape=(4, 10, 9)
func_3333_call = mod.get_global_var('func_3333')
func_3334_call = mutated_mod.get_global_var('func_3334')
call_3443 = relay.TupleGetItem(func_3333_call(), 0)
call_3444 = relay.TupleGetItem(func_3334_call(), 0)
func_2634_call = mod.get_global_var('func_2634')
func_2637_call = mutated_mod.get_global_var('func_2637')
const_3481 = relay.const([6.113926,7.042426,-1.638763,5.805554,-0.244493,-1.217989,-9.339018,-0.144285,-9.162021,-6.685687,5.216143,8.516781,1.074805,3.768347,-0.648113,-6.815002,-7.173107,-0.842273,-9.503262,-7.585481,-0.416872,-2.323827,-6.285636,-0.599384,5.795306,-8.946863,9.085983,1.501717,4.134014,3.338525,-0.815615,-9.977652,6.446635,0.555882,-8.772138,2.396037,-8.033482,9.063544,-9.106803,-4.291184,-0.463226,-9.047254,-8.176279,-0.859888,2.180291,3.186081,0.374923,-4.744047], dtype = "float64")#candidate|3481|(48,)|const|float64
call_3480 = func_2634_call(relay.reshape(const_3481.astype('float64'), [2, 3, 8]))
call_3482 = func_2634_call(relay.reshape(const_3481.astype('float64'), [2, 3, 8]))
func_3333_call = mod.get_global_var('func_3333')
func_3334_call = mutated_mod.get_global_var('func_3334')
call_3484 = relay.TupleGetItem(func_3333_call(), 0)
call_3485 = relay.TupleGetItem(func_3334_call(), 0)
output = relay.Tuple([call_3427,bop_3435,call_3443,call_3480,const_3481,call_3484,])
output2 = relay.Tuple([call_3428,bop_3438,call_3444,call_3482,const_3481,call_3485,])
func_3503 = relay.Function([var_3434,], output)
mod['func_3503'] = func_3503
mod = relay.transform.InferType()(mod)
mutated_mod['func_3503'] = func_3503
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3504 = relay.var("var_3504", dtype = "float64", shape = (4, 10, 9))#candidate|3504|(4, 10, 9)|var|float64
func_3503_call = mutated_mod.get_global_var('func_3503')
call_3505 = func_3503_call(var_3504)
output = call_3505
func_3506 = relay.Function([var_3504], output)
mutated_mod['func_3506'] = func_3506
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3553 = relay.var("var_3553", dtype = "float64", shape = (9, 14, 11))#candidate|3553|(9, 14, 11)|var|float64
uop_3554 = relay.cos(var_3553.astype('float64')) # shape=(9, 14, 11)
bop_3557 = relay.minimum(uop_3554.astype('uint8'), relay.reshape(var_3553.astype('uint8'), relay.shape_of(uop_3554))) # shape=(9, 14, 11)
output = relay.Tuple([bop_3557,])
output2 = relay.Tuple([bop_3557,])
func_3563 = relay.Function([var_3553,], output)
mod['func_3563'] = func_3563
mod = relay.transform.InferType()(mod)
var_3564 = relay.var("var_3564", dtype = "float64", shape = (9, 14, 11))#candidate|3564|(9, 14, 11)|var|float64
output = func_3563(var_3564)
func_3565 = relay.Function([var_3564], output)
mutated_mod['func_3565'] = func_3565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_3576 = relay.TupleGetItem(func_1653_call(), 0)
call_3577 = relay.TupleGetItem(func_1655_call(), 0)
output = call_3576
output2 = call_3577
func_3579 = relay.Function([], output)
mod['func_3579'] = func_3579
mod = relay.transform.InferType()(mod)
mutated_mod['func_3579'] = func_3579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3579_call = mutated_mod.get_global_var('func_3579')
call_3580 = func_3579_call()
output = call_3580
func_3581 = relay.Function([], output)
mutated_mod['func_3581'] = func_3581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2708_call = mod.get_global_var('func_2708')
func_2709_call = mutated_mod.get_global_var('func_2709')
call_3611 = func_2708_call()
call_3612 = func_2708_call()
func_1845_call = mod.get_global_var('func_1845')
func_1848_call = mutated_mod.get_global_var('func_1848')
call_3618 = relay.TupleGetItem(func_1845_call(relay.reshape(call_3611.astype('uint64'), [2, 16, 4])), 0)
call_3619 = relay.TupleGetItem(func_1848_call(relay.reshape(call_3611.astype('uint64'), [2, 16, 4])), 0)
func_2426_call = mod.get_global_var('func_2426')
func_2428_call = mutated_mod.get_global_var('func_2428')
var_3630 = relay.var("var_3630", dtype = "float64", shape = (1, 2025))#candidate|3630|(1, 2025)|var|float64
call_3629 = relay.TupleGetItem(func_2426_call(relay.reshape(var_3630.astype('float64'), [2025,])), 5)
call_3631 = relay.TupleGetItem(func_2428_call(relay.reshape(var_3630.astype('float64'), [2025,])), 5)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_3637 = func_2385_call()
call_3638 = func_2385_call()
func_2708_call = mod.get_global_var('func_2708')
func_2709_call = mutated_mod.get_global_var('func_2709')
call_3658 = func_2708_call()
call_3659 = func_2708_call()
uop_3662 = relay.cos(call_3611.astype('float32')) # shape=(2, 16, 4)
uop_3664 = relay.cos(call_3612.astype('float32')) # shape=(2, 16, 4)
output = relay.Tuple([call_3618,call_3629,var_3630,call_3637,call_3658,uop_3662,])
output2 = relay.Tuple([call_3619,call_3631,var_3630,call_3638,call_3659,uop_3664,])
func_3671 = relay.Function([var_3630,], output)
mod['func_3671'] = func_3671
mod = relay.transform.InferType()(mod)
var_3672 = relay.var("var_3672", dtype = "float64", shape = (1, 2025))#candidate|3672|(1, 2025)|var|float64
output = func_3671(var_3672)
func_3673 = relay.Function([var_3672], output)
mutated_mod['func_3673'] = func_3673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3333_call = mod.get_global_var('func_3333')
func_3334_call = mutated_mod.get_global_var('func_3334')
call_3728 = relay.TupleGetItem(func_3333_call(), 0)
call_3729 = relay.TupleGetItem(func_3334_call(), 0)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_3734 = func_1698_call()
call_3735 = func_1698_call()
func_1798_call = mod.get_global_var('func_1798')
func_1799_call = mutated_mod.get_global_var('func_1799')
call_3736 = relay.TupleGetItem(func_1798_call(), 0)
call_3737 = relay.TupleGetItem(func_1799_call(), 0)
output = relay.Tuple([call_3728,call_3734,call_3736,])
output2 = relay.Tuple([call_3729,call_3735,call_3737,])
func_3745 = relay.Function([], output)
mod['func_3745'] = func_3745
mod = relay.transform.InferType()(mod)
mutated_mod['func_3745'] = func_3745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3745_call = mutated_mod.get_global_var('func_3745')
call_3746 = func_3745_call()
output = call_3746
func_3747 = relay.Function([], output)
mutated_mod['func_3747'] = func_3747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2079_call = mod.get_global_var('func_2079')
func_2080_call = mutated_mod.get_global_var('func_2080')
call_3748 = func_2079_call()
call_3749 = func_2079_call()
output = relay.Tuple([call_3748,])
output2 = relay.Tuple([call_3749,])
func_3755 = relay.Function([], output)
mod['func_3755'] = func_3755
mod = relay.transform.InferType()(mod)
mutated_mod['func_3755'] = func_3755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mutated_mod.get_global_var('func_3755')
call_3756 = func_3755_call()
output = call_3756
func_3757 = relay.Function([], output)
mutated_mod['func_3757'] = func_3757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2733_call = mod.get_global_var('func_2733')
func_2734_call = mutated_mod.get_global_var('func_2734')
call_3798 = relay.TupleGetItem(func_2733_call(), 1)
call_3799 = relay.TupleGetItem(func_2734_call(), 1)
output = call_3798
output2 = call_3799
func_3803 = relay.Function([], output)
mod['func_3803'] = func_3803
mod = relay.transform.InferType()(mod)
output = func_3803()
func_3804 = relay.Function([], output)
mutated_mod['func_3804'] = func_3804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1532_call = mod.get_global_var('func_1532')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_3812 = func_1532_call()
call_3813 = func_1532_call()
output = relay.Tuple([call_3812,])
output2 = relay.Tuple([call_3813,])
func_3819 = relay.Function([], output)
mod['func_3819'] = func_3819
mod = relay.transform.InferType()(mod)
output = func_3819()
func_3820 = relay.Function([], output)
mutated_mod['func_3820'] = func_3820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_3832 = relay.TupleGetItem(func_1653_call(), 0)
call_3833 = relay.TupleGetItem(func_1655_call(), 0)
output = call_3832
output2 = call_3833
func_3847 = relay.Function([], output)
mod['func_3847'] = func_3847
mod = relay.transform.InferType()(mod)
output = func_3847()
func_3848 = relay.Function([], output)
mutated_mod['func_3848'] = func_3848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3050_call = mod.get_global_var('func_3050')
func_3052_call = mutated_mod.get_global_var('func_3052')
call_3863 = func_3050_call()
call_3864 = func_3050_call()
func_1506_call = mod.get_global_var('func_1506')
func_1507_call = mutated_mod.get_global_var('func_1507')
call_3876 = relay.TupleGetItem(func_1506_call(), 4)
call_3877 = relay.TupleGetItem(func_1507_call(), 4)
uop_3890 = relay.sigmoid(call_3876.astype('float32')) # shape=(7, 15, 3)
uop_3892 = relay.sigmoid(call_3877.astype('float32')) # shape=(7, 15, 3)
func_2491_call = mod.get_global_var('func_2491')
func_2492_call = mutated_mod.get_global_var('func_2492')
call_3903 = relay.TupleGetItem(func_2491_call(), 0)
call_3904 = relay.TupleGetItem(func_2492_call(), 0)
func_232_call = mod.get_global_var('func_232')
func_235_call = mutated_mod.get_global_var('func_235')
const_3915 = relay.const(7.859654, dtype = "float32")#candidate|3915|()|const|float32
var_3916 = relay.var("var_3916", dtype = "float32", shape = (256,))#candidate|3916|(256,)|var|float32
call_3914 = func_232_call(relay.reshape(const_3915.astype('float32'), []), relay.reshape(var_3916.astype('float32'), [16, 2, 8]), )
call_3917 = func_232_call(relay.reshape(const_3915.astype('float32'), []), relay.reshape(var_3916.astype('float32'), [16, 2, 8]), )
func_2733_call = mod.get_global_var('func_2733')
func_2734_call = mutated_mod.get_global_var('func_2734')
call_3933 = relay.TupleGetItem(func_2733_call(), 0)
call_3934 = relay.TupleGetItem(func_2734_call(), 0)
bop_3943 = relay.mod(call_3863.astype('float64'), relay.reshape(call_3903.astype('float64'), relay.shape_of(call_3863))) # shape=(2, 16, 4)
bop_3946 = relay.mod(call_3864.astype('float64'), relay.reshape(call_3904.astype('float64'), relay.shape_of(call_3864))) # shape=(2, 16, 4)
func_3819_call = mod.get_global_var('func_3819')
func_3820_call = mutated_mod.get_global_var('func_3820')
call_3948 = relay.TupleGetItem(func_3819_call(), 0)
call_3949 = relay.TupleGetItem(func_3820_call(), 0)
uop_3951 = relay.log(uop_3890.astype('float32')) # shape=(7, 15, 3)
uop_3953 = relay.log(uop_3892.astype('float32')) # shape=(7, 15, 3)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_3955 = relay.TupleGetItem(func_2816_call(), 2)
call_3956 = relay.TupleGetItem(func_2818_call(), 2)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_3967 = func_1295_call()
call_3968 = func_1295_call()
output = relay.Tuple([call_3914,const_3915,var_3916,call_3933,bop_3943,call_3948,uop_3951,call_3955,call_3967,])
output2 = relay.Tuple([call_3917,const_3915,var_3916,call_3934,bop_3946,call_3949,uop_3953,call_3956,call_3968,])
func_3969 = relay.Function([var_3916,], output)
mod['func_3969'] = func_3969
mod = relay.transform.InferType()(mod)
mutated_mod['func_3969'] = func_3969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3970 = relay.var("var_3970", dtype = "float32", shape = (256,))#candidate|3970|(256,)|var|float32
func_3969_call = mutated_mod.get_global_var('func_3969')
call_3971 = func_3969_call(var_3970)
output = call_3971
func_3972 = relay.Function([var_3970], output)
mutated_mod['func_3972'] = func_3972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1532_call = mod.get_global_var('func_1532')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_3982 = func_1532_call()
call_3983 = func_1532_call()
output = call_3982
output2 = call_3983
func_3986 = relay.Function([], output)
mod['func_3986'] = func_3986
mod = relay.transform.InferType()(mod)
mutated_mod['func_3986'] = func_3986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3986_call = mutated_mod.get_global_var('func_3986')
call_3987 = func_3986_call()
output = call_3987
func_3988 = relay.Function([], output)
mutated_mod['func_3988'] = func_3988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3986_call = mod.get_global_var('func_3986')
func_3988_call = mutated_mod.get_global_var('func_3988')
call_4006 = func_3986_call()
call_4007 = func_3986_call()
output = call_4006
output2 = call_4007
func_4035 = relay.Function([], output)
mod['func_4035'] = func_4035
mod = relay.transform.InferType()(mod)
output = func_4035()
func_4036 = relay.Function([], output)
mutated_mod['func_4036'] = func_4036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_4040 = func_2385_call()
call_4041 = func_2385_call()
output = call_4040
output2 = call_4041
func_4045 = relay.Function([], output)
mod['func_4045'] = func_4045
mod = relay.transform.InferType()(mod)
mutated_mod['func_4045'] = func_4045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4045_call = mutated_mod.get_global_var('func_4045')
call_4046 = func_4045_call()
output = call_4046
func_4047 = relay.Function([], output)
mutated_mod['func_4047'] = func_4047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mod.get_global_var('func_3755')
func_3757_call = mutated_mod.get_global_var('func_3757')
call_4110 = relay.TupleGetItem(func_3755_call(), 0)
call_4111 = relay.TupleGetItem(func_3757_call(), 0)
uop_4124 = relay.sigmoid(call_4110.astype('float32')) # shape=(2, 16, 4)
uop_4126 = relay.sigmoid(call_4111.astype('float32')) # shape=(2, 16, 4)
func_3819_call = mod.get_global_var('func_3819')
func_3820_call = mutated_mod.get_global_var('func_3820')
call_4148 = relay.TupleGetItem(func_3819_call(), 0)
call_4149 = relay.TupleGetItem(func_3820_call(), 0)
output = relay.Tuple([uop_4124,call_4148,])
output2 = relay.Tuple([uop_4126,call_4149,])
func_4158 = relay.Function([], output)
mod['func_4158'] = func_4158
mod = relay.transform.InferType()(mod)
mutated_mod['func_4158'] = func_4158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mutated_mod.get_global_var('func_4158')
call_4159 = func_4158_call()
output = call_4159
func_4160 = relay.Function([], output)
mutated_mod['func_4160'] = func_4160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_4169 = relay.TupleGetItem(func_2816_call(), 1)
call_4170 = relay.TupleGetItem(func_2818_call(), 1)
var_4186 = relay.var("var_4186", dtype = "uint64", shape = (2, 16, 4))#candidate|4186|(2, 16, 4)|var|uint64
bop_4187 = relay.floor_divide(call_4169.astype('float64'), relay.reshape(var_4186.astype('float64'), relay.shape_of(call_4169))) # shape=(2, 16, 4)
bop_4190 = relay.floor_divide(call_4170.astype('float64'), relay.reshape(var_4186.astype('float64'), relay.shape_of(call_4170))) # shape=(2, 16, 4)
output = bop_4187
output2 = bop_4190
func_4195 = relay.Function([var_4186,], output)
mod['func_4195'] = func_4195
mod = relay.transform.InferType()(mod)
var_4196 = relay.var("var_4196", dtype = "uint64", shape = (2, 16, 4))#candidate|4196|(2, 16, 4)|var|uint64
output = func_4195(var_4196)
func_4197 = relay.Function([var_4196], output)
mutated_mod['func_4197'] = func_4197
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4229 = relay.var("var_4229", dtype = "float64", shape = ())#candidate|4229|()|var|float64
var_4230 = relay.var("var_4230", dtype = "float64", shape = (1, 2, 6))#candidate|4230|(1, 2, 6)|var|float64
bop_4231 = relay.less(var_4229.astype('bool'), var_4230.astype('bool')) # shape=(1, 2, 6)
var_4238 = relay.var("var_4238", dtype = "float64", shape = (4, 2, 6))#candidate|4238|(4, 2, 6)|var|float64
bop_4239 = relay.not_equal(var_4230.astype('bool'), var_4238.astype('bool')) # shape=(4, 2, 6)
output = relay.Tuple([bop_4231,bop_4239,])
output2 = relay.Tuple([bop_4231,bop_4239,])
func_4247 = relay.Function([var_4229,var_4230,var_4238,], output)
mod['func_4247'] = func_4247
mod = relay.transform.InferType()(mod)
mutated_mod['func_4247'] = func_4247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4247_call = mutated_mod.get_global_var('func_4247')
var_4249 = relay.var("var_4249", dtype = "float64", shape = ())#candidate|4249|()|var|float64
var_4250 = relay.var("var_4250", dtype = "float64", shape = (1, 2, 6))#candidate|4250|(1, 2, 6)|var|float64
var_4251 = relay.var("var_4251", dtype = "float64", shape = (4, 2, 6))#candidate|4251|(4, 2, 6)|var|float64
call_4248 = func_4247_call(var_4249,var_4250,var_4251,)
output = call_4248
func_4252 = relay.Function([var_4249,var_4250,var_4251,], output)
mutated_mod['func_4252'] = func_4252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1532_call = mod.get_global_var('func_1532')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_4254 = func_1532_call()
call_4255 = func_1532_call()
func_4158_call = mod.get_global_var('func_4158')
func_4160_call = mutated_mod.get_global_var('func_4160')
call_4276 = relay.TupleGetItem(func_4158_call(), 1)
call_4277 = relay.TupleGetItem(func_4160_call(), 1)
output = relay.Tuple([call_4254,call_4276,])
output2 = relay.Tuple([call_4255,call_4277,])
func_4287 = relay.Function([], output)
mod['func_4287'] = func_4287
mod = relay.transform.InferType()(mod)
output = func_4287()
func_4288 = relay.Function([], output)
mutated_mod['func_4288'] = func_4288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3391_call = mod.get_global_var('func_3391')
func_3393_call = mutated_mod.get_global_var('func_3393')
call_4295 = func_3391_call()
call_4296 = func_3391_call()
output = relay.Tuple([call_4295,])
output2 = relay.Tuple([call_4296,])
func_4298 = relay.Function([], output)
mod['func_4298'] = func_4298
mod = relay.transform.InferType()(mod)
mutated_mod['func_4298'] = func_4298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4298_call = mutated_mod.get_global_var('func_4298')
call_4299 = func_4298_call()
output = call_4299
func_4300 = relay.Function([], output)
mutated_mod['func_4300'] = func_4300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4401 = relay.var("var_4401", dtype = "float32", shape = (10, 15, 11))#candidate|4401|(10, 15, 11)|var|float32
uop_4402 = relay.exp(var_4401.astype('float32')) # shape=(10, 15, 11)
output = uop_4402
output2 = uop_4402
func_4410 = relay.Function([var_4401,], output)
mod['func_4410'] = func_4410
mod = relay.transform.InferType()(mod)
var_4411 = relay.var("var_4411", dtype = "float32", shape = (10, 15, 11))#candidate|4411|(10, 15, 11)|var|float32
output = func_4410(var_4411)
func_4412 = relay.Function([var_4411], output)
mutated_mod['func_4412'] = func_4412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3745_call = mod.get_global_var('func_3745')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_4466 = relay.TupleGetItem(func_3745_call(), 1)
call_4467 = relay.TupleGetItem(func_3747_call(), 1)
func_1798_call = mod.get_global_var('func_1798')
func_1799_call = mutated_mod.get_global_var('func_1799')
call_4468 = relay.TupleGetItem(func_1798_call(), 1)
call_4469 = relay.TupleGetItem(func_1799_call(), 1)
func_3755_call = mod.get_global_var('func_3755')
func_3757_call = mutated_mod.get_global_var('func_3757')
call_4472 = relay.TupleGetItem(func_3755_call(), 0)
call_4473 = relay.TupleGetItem(func_3757_call(), 0)
output = relay.Tuple([call_4466,call_4468,call_4472,])
output2 = relay.Tuple([call_4467,call_4469,call_4473,])
func_4476 = relay.Function([], output)
mod['func_4476'] = func_4476
mod = relay.transform.InferType()(mod)
mutated_mod['func_4476'] = func_4476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4476_call = mutated_mod.get_global_var('func_4476')
call_4477 = func_4476_call()
output = call_4477
func_4478 = relay.Function([], output)
mutated_mod['func_4478'] = func_4478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4298_call = mod.get_global_var('func_4298')
func_4300_call = mutated_mod.get_global_var('func_4300')
call_4483 = relay.TupleGetItem(func_4298_call(), 0)
call_4484 = relay.TupleGetItem(func_4300_call(), 0)
func_729_call = mod.get_global_var('func_729')
func_731_call = mutated_mod.get_global_var('func_731')
var_4493 = relay.var("var_4493", dtype = "float64", shape = (2025,))#candidate|4493|(2025,)|var|float64
call_4492 = func_729_call(relay.reshape(var_4493.astype('float64'), [15, 15, 9]))
call_4494 = func_729_call(relay.reshape(var_4493.astype('float64'), [15, 15, 9]))
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
const_4502 = relay.const([6.398469,9.008746,6.387247,-1.760846,6.362956,-1.294051,-0.379373,6.499343,4.655967,-2.640974,9.688676,-9.847799,-1.483042,3.327073,-2.745271,-0.392073,0.492045,3.619451,5.395617,-6.673579,-7.528442,-4.959454,1.800142,9.711393,5.504445,-8.456282,2.152892,9.325759,-9.109976,-7.000861,7.996890,-3.371379,-2.626993,-6.709561,-2.624386,-2.558159,4.753625,5.213431,-0.268809,0.428531,-4.637491,0.438388,5.086378,6.058332,1.460473,-7.617770,-5.441380,8.462171,-1.231933,2.650772,3.612177,-1.678029,-5.428235,4.386691,-1.668957,-2.243362,-7.738270,6.531376,-2.285548,2.009816,-7.852284,4.185441,0.707563,5.734722,-4.327749,-4.519796,-5.752418,-6.718990,-6.356497,-0.961828,-3.955471,3.916985,-2.932439,-1.951509,-0.520847,-5.166002,-9.739964,2.220309,-1.710380,2.459206,8.685224,-4.703307,-3.561730,0.207432,-6.236166,-6.183992,-5.682947,-2.592181,-9.711442,-9.628172,-4.625688,2.994296,-3.285617,-6.827905,3.104232,4.117608,2.978972,-1.573124,-4.735370,-7.643753,8.233149,1.042098,6.123557,-1.996333,4.346331,-1.486336,4.201264,-9.967542,-8.938419,5.581099,-0.263000,8.664163,-7.736372,-3.929134,0.743065,-4.631294,7.187123,-8.179493,5.996924,-6.937226,0.482277,-7.614852,-7.836884,-0.129102,-7.168404,-8.767560,-8.810977,-1.158710,4.309251,4.000662,-6.992281,-4.625387,-3.621417,-5.275421,1.489108,-4.625648,1.386105,-8.008133,4.211429,-4.084425,-5.962326,-9.589436,-6.511508,2.714639,9.515923,-0.621105,-6.570528,3.998093,-6.373178,-1.579378,-3.411989,-0.205293,-3.286717,1.332972,-8.148846,1.835285,-5.750943,0.400535,-3.340714,4.353428,-0.545444,4.983660,-9.741881,7.968203,-0.533547,-1.652380,-8.229499,-5.006884,4.478275,-2.361160,-5.728513,-1.868533,1.131999,2.857339,9.446317,-5.766666,1.253769,-7.266041,-8.764427,-6.514115,-6.498864,-8.679508,1.946626,6.469467,-1.340586,-4.568750,0.746211,-0.224945,0.969709,-0.343582,-4.224743,-6.214275,7.346028,0.468324,-4.270796,-0.734805,-7.845927,7.351410,-7.209233,1.150425,-7.111958,5.612880,-0.303825,-9.154958,8.760329,-4.518907,3.141628,3.373418,-5.976594,9.207136,-7.025870,0.357256,-0.147818,1.140465,3.642558,7.044514,-7.761355,3.570755,-2.901332,-9.417627,-1.015518,3.346499,8.892675,-9.729713,8.732732,-2.415099,-0.664268,9.343806,-4.086377,0.166396,2.966434,0.684570,7.822544,-7.867395,0.749027,3.097178,-3.366745,3.013219,-7.970904,7.110214,3.260159,4.887163,7.855037,-9.001173,0.085144,6.185687,2.643450,2.828821,8.787551,-0.977127,-9.311718,-8.771902,8.988217,0.315024,-6.169768,6.914754,-4.437669,0.868243,5.489505,-8.198602,3.697582,5.429310,-2.564313,6.804538,5.877508,-3.675140,0.626789,-3.787513,6.709694,-7.464715,-7.411976,2.549075,7.545759,-8.622537,3.335351,3.695059,-0.682979,5.568844,0.474076,-9.079820,-7.892705,1.291448,6.599320,-2.279788,2.556540,-4.727721,4.553638,-2.751154,-7.905361,9.502283,6.360404,-7.284842,-0.685358,0.082119,-4.574265,-0.262117,-4.885289,8.671212,6.837122,-5.425640,-7.803211,-2.319651,2.481925,-9.227719,2.739649,3.820837,0.781949,-0.175675,3.234443,3.657905,6.016227,-4.058684,8.289001,0.838286,-1.652618,8.792085,5.960303,-2.385507,8.653732,-8.204535,-0.880884,5.676956,-2.307886,4.949536,8.882604,0.244573,-8.526755,3.294353,5.965939,-1.145509,-6.040318,1.613828,9.359641,-6.414339,-0.182564,4.213931,-0.257915,-5.167586,-9.319472,-9.537346,1.170949,-8.109493,-9.863722,2.574041,2.813058,6.932479,-7.233866,7.459765,-3.295762,-3.150348,-7.409509,1.011638,-3.804352,1.507198,-6.861504,6.391738,-9.425218,9.220245,4.992323,-4.591506,2.951892,-4.507861,-7.675278,8.069228,-8.741556,-7.315264,-8.258515,9.733756,2.924616,5.231902,4.383557,9.674699,7.770145,-4.302273,-2.037041,4.055399,-1.327553,9.081181,5.420903,5.995750,-0.421486,-4.727533,0.476665,1.489865,0.934216,-5.259193,5.877377,-0.644515,5.662817,0.297188,2.907544,1.172499,9.108346,0.338328,2.511155,-7.519035,-4.341047,-7.125589,-3.705605,-6.786993,6.341878,-2.615015,7.739585,2.338524,4.005051,-5.893699,5.071630,-9.758096,-6.401163,8.966867,-8.052337,6.985515,-9.067246,0.124295,4.753609,-4.781566,-6.791083,-9.075140,1.851537,-5.593478,-2.969866,-4.739840,-2.118130,-7.215337,-8.611679,5.376897,2.787334,8.106328,-2.533972,3.782673,-8.739093,-5.943782,-3.032031,-8.175549,-5.350842,5.622282,6.254965,-5.499757,-3.897140,-9.921371,-7.353992,-2.867705,-4.281243,-8.709628,-9.147317,2.540138,7.040508,6.371141,-9.067928,-7.516439,3.544827,7.261910,0.030163,-7.950150,6.835583,-2.488444,-8.336813,0.443560,-6.347547,-2.483286,7.541418,3.209539,1.800777,3.162163,4.256096,4.905999,5.738485,4.350710,-1.410967,-4.805647,4.533402,-4.395251,6.540027,-8.809426,3.114736,-4.934474,-3.230006,4.001730,6.888196,7.913489,-5.417166,5.203229,-1.401423,-5.279219,-8.826325,-0.801864,0.048183,-9.548048,-6.397373,-6.443081,9.173909,0.562321,1.905051,4.740774,6.686247,7.853965,5.099391,5.111651,4.559235,9.994709,-7.838254,9.155114,-1.560048,5.092844,2.470172,-3.281773,-8.514324,-1.225334,-5.056074,-7.215513,4.491455,-6.038981,-5.810886,-4.614409,3.187148,-2.254310,7.594718,-9.442983,9.617632,-2.666613,5.293475,4.634907,-7.686602,6.971371,6.842390,-2.360463,7.083179,-5.849084,-2.845114,-3.478012,-4.874644,-1.708224,-7.011865,7.820418,-4.769922,-6.598738,-9.739135,0.847976,-0.732108,5.388243,5.103905,-9.342020,-7.580530,-8.171921,8.409433,5.524547,8.675061,1.763501,-5.905643,1.781350,-4.873054,-9.766900,6.314182,-8.896086,2.774072,-2.760179,6.278027,0.566596,1.896886,1.265386,-7.368385,-2.109327,-7.073366,-9.738288,-7.742765,3.605110,5.626248,2.901114,3.422499,-9.940540,7.742665,9.327745,5.370955,5.695762,4.820159,1.663342,3.853694,6.601489,7.228543,-5.828318,-7.349027,2.211128,7.116340,-0.335547,-2.252186,6.812770,1.097552,-8.315286,-3.924446,7.493237,-7.952087,0.169488,-5.560680,2.240497,-2.873341,3.560770,2.896503,8.171217,2.679842,-9.919480,-7.784440,-5.739418,-4.166997,2.668495,-1.740362,-8.565767,4.819076,-5.300995,5.872492,-5.050408,8.306280,-9.165779,-7.056551,1.975952,7.401610,0.917045,-6.150989,-2.885622,-5.315022,9.846508,-4.908788,-7.052549,9.879374,-9.681606,-3.761628,2.785016,-3.010357,5.552052,7.145346,2.613207,-6.724534,-1.605268,-0.240969,1.708301,-6.466520,6.990795,1.797130,2.496675,-6.428289,1.588262,-0.047840,-2.556830,-0.114527,1.242302,-4.356635,-7.294655,7.007845,0.538810,9.393608,-0.072599,9.667842,7.678187,5.604875,-5.267322,-6.712357,9.489527,-0.910047,0.910432,7.626843,-0.760080,4.251014,-2.133957,2.429271,-2.858514,-4.371914,6.726039,-4.465932,-5.005706,8.528209,7.411919,-8.953740,-7.502807,-5.658249,7.205874,-5.304200,-7.213096,8.313414,-4.389346,-8.510520,4.038655,2.233225,7.275468,7.542805,-4.381646,-6.508169,-7.570739,-7.551209,5.450934,3.392274,-9.336807,-0.091839,9.599498,2.329096,-1.825743,0.417365,-3.536150,-5.691548,-6.051149,-8.289563,-8.007217,6.159939,1.312290,2.131570,-1.562448,-8.753189,-4.344369,4.990421,-8.664240,3.249532,0.868510,-9.986451,-4.733699,9.092450,8.491340,8.386773,-6.590826,-0.798420,-1.915916,-4.170179,-4.244854,3.837742,8.477629,8.351991,3.313436,-2.320778,9.119208,-4.368879,-6.759980,-1.047358,7.788036,9.048795,-2.394498,-9.559353,-7.559025,-7.030192,6.409786,5.607500,-0.438865,-0.207955,-2.960525,-3.359662,7.768433,4.430578,-3.171591,2.027666,0.220488,4.736597,5.309392,-9.701586,-8.589219,-0.409094,-2.652994,-6.525722,-4.571168,-2.607225,-7.130599,-3.906346,3.217612,2.853311,-8.749384,-6.828163,2.993542,1.396201,1.620463,-9.559965,-2.991664,8.185520,5.861332,-9.029863,-0.221663,-6.062751,8.429598,-1.216463,-6.517539,6.312513,6.644108,-0.400093,8.782624,1.626769,3.250158,8.097664,-9.388222,-1.810605,-6.179673,-0.819856,8.647606,8.706152,8.527201,0.213689,6.701868,-6.226497,-2.637260,-4.874524,0.743039,-5.582978,8.149347,-6.511691,-9.440156,9.326334,6.577463,9.146168,-3.849658,-0.476578,7.040155,8.803534,-2.897765,9.754858,-3.486353,-1.463657,5.098723,-8.084355,-8.190797,-1.505014,4.306315,-8.078133,5.123786,4.854399,-5.022894,-6.898635,-1.836764,2.862670,2.230243,1.812433,-7.742979,5.970607,9.036049,-9.289255,2.079378,-3.257850,3.652474,6.147072,0.294307,-5.744523,-7.594145,3.969307,6.436746,7.914344,3.850332,-1.037533,4.356154,0.022605,-0.520331,-2.766503,-5.428480,-1.989586,5.065962,4.794094,0.730981,2.958380,-5.081557,-7.948954,1.882945,-5.464635,-2.672877,-1.556585,3.342621,-0.658702,7.211901,0.035412,-0.281525,5.060962,5.110053,-7.861371,1.755871,3.218613,-8.345185,5.947782,9.009060,-4.996108,-7.659195,1.332601,-5.940663,5.105826,7.886973,8.529061,0.775662,0.503197,3.913251,7.076318,3.210719,-7.925151,-4.366040,8.433119,-6.566998,7.142577,-2.028320,-8.976256,6.676998,2.609400,-8.062245,-5.889021,6.414030,-2.769090,5.681015,5.885078,-5.233460,-7.627439,6.052652,5.877243,1.350764,1.337420,0.656481,-9.772667,2.381778,6.595249,-9.337235,4.527872,-6.234349,5.596325,1.373464,-1.431578,-1.459925,-9.709884,9.897272,6.872911,0.008551,-2.587595,-9.623060,3.771645,-9.043957,3.364312,-5.898346,6.271422,8.658115,-0.136554,5.558432,-0.758491,2.647957,-6.872086,-2.455729,7.986165,-5.128687,5.360304,-3.550014,-1.503557,8.032053,1.831602,3.381524,-8.782551,4.172229,7.043964,-8.652528,1.817294,0.110029,-4.127739,6.563213,3.570671,7.433605,6.061880,9.278851,6.232423,2.544279,-9.995845,9.962984,3.829096,2.952478,0.599737,6.440079,0.394471,-0.639486,-3.424791,4.842629,6.901797,-7.993287,-0.185920,4.237842,4.667848,-4.041427,7.424401,-6.324123,2.617150,6.242430,2.698342,2.007410,8.568572,-3.286098,1.147422,5.896529,7.531284,1.870756,3.306973,4.150279,-3.382626,-0.768482,9.490834,-7.493638,-0.651233,3.199838,-5.702337,-2.019304,5.310689,-7.389386,-1.542947,7.134877,4.683339,5.629450,3.306661,4.083533,6.896666,5.657992,2.340173,4.726202,-1.625097,7.006568,9.337504,-0.067200,8.817545,6.214630,4.494833,8.111943,-5.487210,7.788485,2.351679,7.004217,6.464688,8.131842,-8.258661,-5.911438,5.064285,-6.410116,-0.976148,9.596994,1.909176,2.888269,-3.071284,3.462323,-8.110842,-7.525286,-4.019119,-4.181157,4.253310,-9.669738,-7.036471,-1.202111,-5.080831,-0.668153,0.404513,-4.026652,-4.698129,2.867902,-5.938044,0.988021,-8.112683,-1.818354,6.670991,-1.015262,-1.437276,2.721726,3.067894,1.480906,-4.431452,-1.674711,8.712015,-0.405954,4.873787,-8.634022,-3.633161,-9.559001,-7.823502,1.872158,4.457876,-1.589398,-9.918998,-7.804976,8.309898,-7.748845,2.956578,6.625684,6.790513,-4.352031,-7.644544,4.593896,0.127765,9.881594,-4.432809,3.027322,-2.489971,-4.105945,7.507264,-2.292637,-1.161971,-3.596161,-4.637412,-6.155256,8.351080,-1.378397,-4.912468,3.244042,3.752430,3.000209,4.991172,0.929247,-1.952539,6.187334,-2.866266,-5.282380,-9.895273,-4.319403,-9.769699,-7.772596,4.767549,2.366795,-1.773167,9.687623,2.609418,-1.631954,-0.696728,-1.404578,3.304872,-1.606320,-6.571583,-6.577040,-4.156064,7.552751,2.658371,-9.837438,-1.301401,-9.540256,-2.543501,-6.845279,-1.982148,6.866761,-3.564041,9.194330,4.159529,7.193608,-0.267938,-2.905161,-2.217381,-2.880911,0.967547,-0.815716,-1.953389,2.883837,2.443987,1.601253,-0.098613,-4.667451,-2.319511,-6.860301,3.381545,1.346952,3.997540,-7.497503,6.593023,8.728511,-9.462538,-4.425591,9.400051,9.024258,3.572077,-8.726573,6.996489,-6.599040,0.623904,2.452025,-7.770158,-8.654085,-6.569726,8.004670,2.843627,4.173232,5.412173,5.094379,2.200705,1.411293,5.145081,-3.806475,-4.716645,-6.446522,6.793094,-8.823080,9.008020,9.847234,-0.305140,6.625854,0.504441,1.343325,1.302646,5.213707,4.254114,3.894375,1.684579,-3.012785,4.758996,0.003064,-8.542558,-8.671175,-7.792946,-1.631810,3.178498,4.702790,-0.939693,4.037538,7.229237,-9.425979,8.926612,9.958020,5.630917,-9.682836,-5.492089,9.316874,2.736893,-7.998708,1.882602,-2.280263,1.862464,9.806101,-4.620332,1.356600,-5.689232,1.475020,9.683930,-1.956530,-4.828463,7.783976,-1.069087,1.571101,9.232093,6.057710,-7.516159,1.580172,7.781804,4.177153,4.140143,3.896634,-7.864096,9.013464,2.065437,-5.841338,-8.292517,6.857090,-7.322933,-3.551129,-8.695241,-6.947198,-0.689181,-6.936338,1.380156,2.962567,-3.805597,-8.675850,1.779154,6.329412,1.253457,-7.989004,3.686723,-3.254472,3.135353,7.645288,-9.867010,-5.651883,7.550856,0.465610,6.074273,5.325603,4.038997,-9.434913,1.720933,-7.258503,-0.019101,-0.425646,-1.082286,4.323816,-9.961880,9.357581,5.971308,2.446847,9.945669,2.232680,2.405538,-6.269392,-0.968220,-7.554450,-5.354654,-2.458728,1.051609,3.684083,2.865982,9.957577,0.282012,-8.563611,9.524663,-8.099641,-5.643779,9.732017,-8.763294,4.119041,-3.522744,2.718451,-7.182917,8.344119,-5.101093,5.366038,-5.349466,0.043758,4.910385,-1.934625,5.743832,0.324068,-1.263405,-3.436116,4.833292,0.459593,5.125907,-2.878050,-7.339551,8.164974,-2.320921,-9.923530,-3.194069,6.862697,6.106634,-0.503809,-9.748312,2.207303,-8.713483,8.731173,8.430630,4.932501], dtype = "float32")#candidate|4502|(1320,)|const|float32
call_4501 = func_2305_call(relay.reshape(const_4502.astype('float32'), [11, 15, 8]))
call_4503 = func_2305_call(relay.reshape(const_4502.astype('float32'), [11, 15, 8]))
var_4509 = relay.var("var_4509", dtype = "float64", shape = (2025,))#candidate|4509|(2025,)|var|float64
bop_4510 = relay.left_shift(var_4493.astype('uint8'), relay.reshape(var_4509.astype('uint8'), relay.shape_of(var_4493))) # shape=(2025,)
uop_4514 = relay.cosh(var_4509.astype('float64')) # shape=(2025,)
uop_4527 = relay.atan(uop_4514.astype('float32')) # shape=(2025,)
output = relay.Tuple([call_4483,call_4492,call_4501,const_4502,bop_4510,uop_4527,])
output2 = relay.Tuple([call_4484,call_4494,call_4503,const_4502,bop_4510,uop_4527,])
func_4529 = relay.Function([var_4493,var_4509,], output)
mod['func_4529'] = func_4529
mod = relay.transform.InferType()(mod)
mutated_mod['func_4529'] = func_4529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4529_call = mutated_mod.get_global_var('func_4529')
var_4531 = relay.var("var_4531", dtype = "float64", shape = (2025,))#candidate|4531|(2025,)|var|float64
var_4532 = relay.var("var_4532", dtype = "float64", shape = (2025,))#candidate|4532|(2025,)|var|float64
call_4530 = func_4529_call(var_4531,var_4532,)
output = call_4530
func_4533 = relay.Function([var_4531,var_4532,], output)
mutated_mod['func_4533'] = func_4533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3401_call = mod.get_global_var('func_3401')
func_3403_call = mutated_mod.get_global_var('func_3403')
call_4535 = relay.TupleGetItem(func_3401_call(), 0)
call_4536 = relay.TupleGetItem(func_3403_call(), 0)
func_3969_call = mod.get_global_var('func_3969')
func_3972_call = mutated_mod.get_global_var('func_3972')
var_4554 = relay.var("var_4554", dtype = "float32", shape = (256,))#candidate|4554|(256,)|var|float32
call_4553 = relay.TupleGetItem(func_3969_call(relay.reshape(var_4554.astype('float32'), [256,])), 5)
call_4555 = relay.TupleGetItem(func_3972_call(relay.reshape(var_4554.astype('float32'), [256,])), 5)
func_2491_call = mod.get_global_var('func_2491')
func_2492_call = mutated_mod.get_global_var('func_2492')
call_4557 = relay.TupleGetItem(func_2491_call(), 0)
call_4558 = relay.TupleGetItem(func_2492_call(), 0)
output = relay.Tuple([call_4535,call_4553,var_4554,call_4557,])
output2 = relay.Tuple([call_4536,call_4555,var_4554,call_4558,])
func_4562 = relay.Function([var_4554,], output)
mod['func_4562'] = func_4562
mod = relay.transform.InferType()(mod)
mutated_mod['func_4562'] = func_4562
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4563 = relay.var("var_4563", dtype = "float32", shape = (256,))#candidate|4563|(256,)|var|float32
func_4562_call = mutated_mod.get_global_var('func_4562')
call_4564 = func_4562_call(var_4563)
output = call_4564
func_4565 = relay.Function([var_4563], output)
mutated_mod['func_4565'] = func_4565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3391_call = mod.get_global_var('func_3391')
func_3393_call = mutated_mod.get_global_var('func_3393')
call_4591 = func_3391_call()
call_4592 = func_3391_call()
func_3050_call = mod.get_global_var('func_3050')
func_3052_call = mutated_mod.get_global_var('func_3052')
call_4596 = func_3050_call()
call_4597 = func_3050_call()
output = relay.Tuple([call_4591,call_4596,])
output2 = relay.Tuple([call_4592,call_4597,])
func_4600 = relay.Function([], output)
mod['func_4600'] = func_4600
mod = relay.transform.InferType()(mod)
mutated_mod['func_4600'] = func_4600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4600_call = mutated_mod.get_global_var('func_4600')
call_4601 = func_4600_call()
output = call_4601
func_4602 = relay.Function([], output)
mutated_mod['func_4602'] = func_4602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3986_call = mod.get_global_var('func_3986')
func_3988_call = mutated_mod.get_global_var('func_3988')
call_4633 = func_3986_call()
call_4634 = func_3986_call()
func_2912_call = mod.get_global_var('func_2912')
func_2915_call = mutated_mod.get_global_var('func_2915')
var_4657 = relay.var("var_4657", dtype = "uint8", shape = (1, 420))#candidate|4657|(1, 420)|var|uint8
call_4656 = relay.TupleGetItem(func_2912_call(relay.reshape(var_4657.astype('uint8'), [14, 15, 2])), 0)
call_4658 = relay.TupleGetItem(func_2915_call(relay.reshape(var_4657.astype('uint8'), [14, 15, 2])), 0)
func_1946_call = mod.get_global_var('func_1946')
func_1947_call = mutated_mod.get_global_var('func_1947')
call_4659 = func_1946_call()
call_4660 = func_1946_call()
output = relay.Tuple([call_4633,call_4656,var_4657,call_4659,])
output2 = relay.Tuple([call_4634,call_4658,var_4657,call_4660,])
func_4671 = relay.Function([var_4657,], output)
mod['func_4671'] = func_4671
mod = relay.transform.InferType()(mod)
mutated_mod['func_4671'] = func_4671
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4672 = relay.var("var_4672", dtype = "uint8", shape = (1, 420))#candidate|4672|(1, 420)|var|uint8
func_4671_call = mutated_mod.get_global_var('func_4671')
call_4673 = func_4671_call(var_4672)
output = call_4673
func_4674 = relay.Function([var_4672], output)
mutated_mod['func_4674'] = func_4674
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4679 = relay.var("var_4679", dtype = "float64", shape = (14, 12, 5))#candidate|4679|(14, 12, 5)|var|float64
uop_4680 = relay.atanh(var_4679.astype('float64')) # shape=(14, 12, 5)
uop_4682 = relay.atan(var_4679.astype('float32')) # shape=(14, 12, 5)
func_1845_call = mod.get_global_var('func_1845')
func_1848_call = mutated_mod.get_global_var('func_1848')
var_4686 = relay.var("var_4686", dtype = "uint64", shape = (128,))#candidate|4686|(128,)|var|uint64
call_4685 = relay.TupleGetItem(func_1845_call(relay.reshape(var_4686.astype('uint64'), [2, 16, 4])), 0)
call_4687 = relay.TupleGetItem(func_1848_call(relay.reshape(var_4686.astype('uint64'), [2, 16, 4])), 0)
const_4688 = relay.const([[[3.585788,0.932177,7.679820,5.985725,-9.703875],[-3.136654,7.994190,-5.239151,2.138288,-1.250446],[7.843882,1.898892,-2.011122,-5.419425,-5.400339],[9.565378,1.622260,-6.523807,6.631598,-1.432256],[-0.242460,8.346049,2.816167,5.132413,-1.403441],[8.921891,5.460481,-5.615651,7.074054,-3.316887],[-7.835418,-0.946991,-9.513986,9.585561,-3.654351],[-7.340951,-2.518056,-1.351211,6.632496,4.834584],[5.981303,1.096547,3.652168,7.948614,5.055724],[3.969020,2.487434,9.244183,-5.896243,6.572554],[-1.632906,7.361182,1.256431,-5.394412,0.693173],[-7.399258,-0.166850,-6.503652,1.595744,1.590162]],[[0.545966,7.168134,-0.701267,1.760188,8.733405],[5.451854,-4.606406,-8.496115,-7.327222,-3.770535],[-5.451470,0.393977,-9.348774,1.381386,9.473538],[-1.889850,4.076823,7.794117,-1.098484,-6.219977],[2.940109,-4.304388,6.416634,7.518238,6.759387],[1.373248,-1.987700,5.803324,-0.352118,7.293480],[8.349991,5.267431,2.754221,-9.339793,3.047423],[9.753244,-6.120400,-4.945823,-8.579481,8.283675],[7.688889,-9.383643,1.628716,-8.563463,-2.670051],[9.753810,-8.872063,-8.938390,6.393430,4.061832],[0.876505,9.564090,-9.963868,2.646978,4.405342],[1.619119,-6.817750,2.296281,9.210444,0.605264]],[[8.617349,5.915277,6.269223,0.333644,-3.605962],[8.813571,1.746615,3.589913,-6.941212,-3.461335],[1.730439,-1.083525,9.114292,-1.208125,-1.729567],[-0.990501,-4.933357,5.981700,1.056743,0.511653],[4.616462,-2.870430,6.564578,7.127568,-6.961497],[-7.303348,0.042388,6.772674,-4.054960,5.802792],[-3.468153,-6.818608,9.220480,-4.961501,-4.540492],[-0.389777,3.505416,-1.304248,-6.988913,-3.757731],[3.067703,-2.681629,-6.762683,-4.112057,2.539895],[1.180298,4.655347,0.325988,1.261687,-5.804198],[3.135872,7.570083,5.210874,6.184446,5.637566],[-4.038103,-6.572040,3.118108,0.626513,8.123936]],[[0.141565,-0.649494,-4.592604,6.882420,2.529452],[0.301276,-9.004530,5.479398,-3.422220,4.173497],[4.521249,5.907643,8.675913,-4.355941,-0.607094],[0.926404,-2.387699,-3.281572,1.323176,-1.776692],[2.061793,2.617834,-7.122162,1.296629,-8.770637],[4.765781,3.892288,2.135701,1.422984,0.268254],[-5.163202,-2.012241,-0.159134,4.870329,-0.532472],[-5.718260,-3.917922,-4.315443,1.669514,9.544250],[-0.015319,7.134469,1.080493,-9.352935,-0.747763],[-8.385481,1.676841,8.665220,-3.558566,7.900054],[-9.192056,-4.914464,-2.892147,0.036087,0.968780],[8.486991,8.138475,9.202937,4.446680,-6.870560]],[[4.500369,-3.792802,1.166742,-6.526276,7.264328],[-9.527427,7.582339,-4.563098,0.396130,8.104447],[-5.279891,1.466328,7.416653,2.035725,-5.083797],[-4.990023,-9.028958,-3.635358,-2.467392,4.177705],[7.140917,4.671907,8.570894,-5.205719,-9.381697],[3.287462,-3.386464,-7.973373,1.482577,-1.554442],[3.659645,6.370986,-6.536702,9.379684,-6.214964],[-7.598424,4.785509,-8.971242,8.931330,6.927049],[8.188295,-9.200823,8.578602,4.051969,-4.505813],[9.187811,6.299462,-3.592820,-5.847241,-7.294078],[-2.459699,-7.468055,2.686204,-4.534642,0.249612],[-9.225268,-7.929614,-2.664157,0.873386,-2.476679]],[[-1.473136,-3.385779,-8.759772,6.039754,-2.722488],[2.974086,-6.850337,-5.625732,7.295320,-8.837376],[7.014652,0.954094,8.857891,2.385283,2.037157],[2.332490,0.520488,8.014112,-8.567056,5.932010],[6.694607,8.598750,-6.224127,7.821264,7.904990],[1.467176,-2.372170,-1.661659,-8.330850,-5.140536],[-3.225091,2.795331,8.250129,8.286429,4.365789],[2.365663,-0.997719,-3.676415,-6.091723,-2.019846],[8.609614,-5.667273,-0.445936,-7.454438,8.625607],[-9.076501,-5.764946,5.148687,5.751359,1.755187],[8.834197,8.101699,0.606249,3.844307,1.367840],[0.203539,1.464217,-7.357338,9.111788,-2.613717]],[[0.195028,-8.078972,2.658295,-4.586217,-8.572110],[8.485357,-4.556394,6.133061,2.518706,9.855607],[-3.953019,2.636791,3.676653,1.774000,-2.946344],[7.671620,5.977248,0.540485,6.937769,2.583316],[6.980645,-8.146864,0.213775,-0.463026,-7.279902],[3.126097,-7.944769,-4.045025,-9.125717,-3.254705],[4.483784,-8.455563,3.809216,7.022647,8.021562],[6.557306,-8.954446,-0.479113,6.333386,-1.498103],[0.821213,2.418812,-1.123483,4.962380,1.323321],[-5.836420,4.079711,9.720066,-1.657625,1.374102],[9.459226,9.572763,-5.459781,0.831069,-8.294154],[9.446126,0.007599,8.280351,-9.395226,-5.988803]],[[7.711684,2.426629,-4.738262,2.004863,2.747575],[-9.892283,3.533710,-9.050416,-1.066844,-5.851738],[2.111363,-5.974560,-9.924462,2.907044,-0.799636],[-2.920238,-0.216790,-2.138092,6.681346,8.128875],[-1.625866,9.940313,0.249797,-2.008301,-6.097574],[-8.259347,-3.477035,-9.879597,1.737314,-8.620162],[-6.814712,0.358754,-2.657969,2.886303,7.573021],[-8.131357,-9.531254,-5.292929,-8.914053,0.133027],[2.520835,-9.843035,-4.069427,-1.351218,-1.846129],[2.560397,1.098362,6.780304,-4.281216,1.213891],[-4.025256,-2.380818,-0.278281,-0.555615,8.866666],[0.793146,-5.138703,-2.895073,-7.174261,-3.116099]],[[6.926553,8.985728,-2.056366,-8.880722,7.439003],[-7.866903,-9.740910,7.019709,9.696866,3.222872],[1.742055,1.630643,-9.864473,7.981757,-8.703759],[-2.929596,1.424425,4.895163,-9.460298,0.425955],[4.220890,8.660075,-0.798876,-9.459964,5.575072],[-1.243136,-9.511080,-1.023973,1.121232,-2.599544],[9.424229,-6.754175,-5.564165,-6.210330,6.299941],[5.719218,4.661714,-3.411747,9.943841,-5.401855],[-6.466978,7.345518,-4.191764,-4.829498,0.507157],[-9.863396,5.757409,-2.642376,-0.177578,-6.781983],[-8.508269,-2.537945,7.279811,9.850128,-0.311270],[2.272162,-3.399439,8.411778,-8.486799,-7.458979]],[[-5.167419,-4.541416,1.266245,-7.835045,4.686015],[-2.886985,-3.516414,0.811818,9.702648,-0.459247],[-7.034163,6.768569,-5.504429,-8.542984,-3.798279],[6.962233,2.771374,-1.515795,-3.763817,-1.434793],[0.267911,3.078986,7.551791,6.188887,5.597913],[-0.028141,8.306720,-4.222854,6.286765,-9.823563],[1.095394,-2.266597,2.017783,-5.124432,0.903709],[4.808539,0.093113,-7.532500,-0.750005,4.405396],[7.762149,9.055565,2.899618,3.526331,-1.051619],[-1.431255,0.178359,-5.197576,2.978936,-6.206659],[9.690296,-7.629597,-0.239399,-2.665820,-9.728497],[-1.995562,0.703415,2.949995,8.053495,8.810398]],[[-7.207228,3.804507,8.200548,8.966270,-5.980541],[0.814531,7.876881,-3.883193,5.903333,-4.219116],[9.695252,7.598207,4.778641,2.219292,1.681342],[-5.732874,0.405296,9.538460,-2.549141,6.004817],[-7.272912,-4.123655,-6.269735,5.109637,3.452141],[-5.090525,-8.629081,-4.777504,-8.478998,-1.068386],[-9.647392,0.779979,1.083764,-7.171021,7.948665],[-5.814964,0.916258,-0.863719,-8.483046,2.101802],[9.543282,-6.524295,9.920957,3.651821,-8.422609],[-0.357049,7.967259,-1.061640,-4.676674,-0.625894],[9.437606,-2.244015,7.434683,-8.229603,-5.197101],[-7.900594,3.815423,-0.622433,0.555583,-8.082543]],[[7.303611,-9.188648,3.543870,1.891512,-0.282637],[1.233908,7.041258,-5.901417,-1.013882,-7.538193],[-7.821083,8.867383,9.632268,-4.734977,3.076980],[-8.158621,8.464089,6.886827,-1.435640,7.356032],[-5.932345,-3.251498,-2.058773,2.885635,6.294483],[1.774192,-8.708895,-4.000765,-1.576017,-8.775338],[7.952974,4.346656,1.562268,2.273185,3.311087],[-9.112523,-1.645484,5.873009,7.844741,0.066055],[-1.565883,-5.980983,0.822865,-4.440296,-2.833366],[-5.233895,-6.170395,-4.875504,-4.767380,8.184494],[-4.596350,-2.048450,-5.413195,9.949189,-5.697510],[-9.406156,-1.017556,2.793966,6.756080,4.274648]],[[-3.791817,-3.214641,2.365268,-6.604063,-6.734763],[-2.146960,-3.240753,8.395597,-2.013023,-4.182454],[-2.863846,-3.230196,-0.368562,-0.350137,6.734446],[7.000205,8.968762,-3.698021,-1.323033,3.219377],[-8.283778,-5.222363,-8.505165,1.967293,-6.741308],[5.778417,4.034123,5.084022,5.069600,1.996076],[-0.734775,-3.094620,-6.207197,-3.292957,3.623803],[-0.244160,8.489916,-5.379258,-6.111401,5.861836],[-5.274456,6.035917,-7.049948,5.342617,9.296830],[-1.881267,5.870829,1.960775,-7.167298,-1.637714],[7.690970,5.977947,0.586004,-2.028207,-9.284735],[0.615373,-2.088740,-5.476621,1.574371,-0.425284]],[[-8.023452,-2.772478,2.256636,-2.322477,-9.401165],[-8.089370,4.647890,-3.348328,6.612117,-0.201891],[-9.716482,-9.673920,7.331860,7.670180,-6.503465],[2.051678,6.726245,-3.705330,6.481449,-4.141623],[-6.959565,-9.979779,-4.867571,-1.196340,0.310514],[3.433874,-3.751056,2.421980,-2.043818,5.300956],[-2.130881,-9.574665,-6.345675,2.756445,4.203107],[5.529033,-7.490452,4.759527,3.903085,-0.606951],[-2.419408,-0.882280,-0.478603,-0.120218,4.724676],[6.972292,-0.986070,2.736296,1.888732,9.366096],[-4.927096,-8.999115,-5.202716,1.895781,1.776555],[-7.404843,-0.287597,1.961719,-6.440796,5.041389]]], dtype = "float64")#candidate|4688|(14, 12, 5)|const|float64
bop_4689 = relay.floor_divide(uop_4680.astype('float64'), relay.reshape(const_4688.astype('float64'), relay.shape_of(uop_4680))) # shape=(14, 12, 5)
output = relay.Tuple([uop_4682,call_4685,var_4686,bop_4689,])
output2 = relay.Tuple([uop_4682,call_4687,var_4686,bop_4689,])
func_4692 = relay.Function([var_4679,var_4686,], output)
mod['func_4692'] = func_4692
mod = relay.transform.InferType()(mod)
var_4693 = relay.var("var_4693", dtype = "float64", shape = (14, 12, 5))#candidate|4693|(14, 12, 5)|var|float64
var_4694 = relay.var("var_4694", dtype = "uint64", shape = (128,))#candidate|4694|(128,)|var|uint64
output = func_4692(var_4693,var_4694,)
func_4695 = relay.Function([var_4693,var_4694,], output)
mutated_mod['func_4695'] = func_4695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2491_call = mod.get_global_var('func_2491')
func_2492_call = mutated_mod.get_global_var('func_2492')
call_4739 = relay.TupleGetItem(func_2491_call(), 0)
call_4740 = relay.TupleGetItem(func_2492_call(), 0)
uop_4779 = relay.acos(call_4739.astype('float32')) # shape=(2, 16, 4)
uop_4781 = relay.acos(call_4740.astype('float32')) # shape=(2, 16, 4)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_4783 = func_2385_call()
call_4784 = func_2385_call()
output = relay.Tuple([uop_4779,call_4783,])
output2 = relay.Tuple([uop_4781,call_4784,])
func_4790 = relay.Function([], output)
mod['func_4790'] = func_4790
mod = relay.transform.InferType()(mod)
mutated_mod['func_4790'] = func_4790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4790_call = mutated_mod.get_global_var('func_4790')
call_4791 = func_4790_call()
output = call_4791
func_4792 = relay.Function([], output)
mutated_mod['func_4792'] = func_4792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mod.get_global_var('func_4158')
func_4160_call = mutated_mod.get_global_var('func_4160')
call_4804 = relay.TupleGetItem(func_4158_call(), 1)
call_4805 = relay.TupleGetItem(func_4160_call(), 1)
output = call_4804
output2 = call_4805
func_4806 = relay.Function([], output)
mod['func_4806'] = func_4806
mod = relay.transform.InferType()(mod)
output = func_4806()
func_4807 = relay.Function([], output)
mutated_mod['func_4807'] = func_4807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3847_call = mod.get_global_var('func_3847')
func_3848_call = mutated_mod.get_global_var('func_3848')
call_4830 = func_3847_call()
call_4831 = func_3847_call()
output = call_4830
output2 = call_4831
func_4834 = relay.Function([], output)
mod['func_4834'] = func_4834
mod = relay.transform.InferType()(mod)
output = func_4834()
func_4835 = relay.Function([], output)
mutated_mod['func_4835'] = func_4835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3012_call = mod.get_global_var('func_3012')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_4896 = relay.TupleGetItem(func_3012_call(), 0)
call_4897 = relay.TupleGetItem(func_3013_call(), 0)
output = relay.Tuple([call_4896,])
output2 = relay.Tuple([call_4897,])
func_4906 = relay.Function([], output)
mod['func_4906'] = func_4906
mod = relay.transform.InferType()(mod)
output = func_4906()
func_4907 = relay.Function([], output)
mutated_mod['func_4907'] = func_4907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4600_call = mod.get_global_var('func_4600')
func_4602_call = mutated_mod.get_global_var('func_4602')
call_4951 = relay.TupleGetItem(func_4600_call(), 0)
call_4952 = relay.TupleGetItem(func_4602_call(), 0)
output = relay.Tuple([call_4951,])
output2 = relay.Tuple([call_4952,])
func_4959 = relay.Function([], output)
mod['func_4959'] = func_4959
mod = relay.transform.InferType()(mod)
output = func_4959()
func_4960 = relay.Function([], output)
mutated_mod['func_4960'] = func_4960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3391_call = mod.get_global_var('func_3391')
func_3393_call = mutated_mod.get_global_var('func_3393')
call_4969 = func_3391_call()
call_4970 = func_3391_call()
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_4971 = relay.TupleGetItem(func_2816_call(), 2)
call_4972 = relay.TupleGetItem(func_2818_call(), 2)
output = relay.Tuple([call_4969,call_4971,])
output2 = relay.Tuple([call_4970,call_4972,])
func_4978 = relay.Function([], output)
mod['func_4978'] = func_4978
mod = relay.transform.InferType()(mod)
mutated_mod['func_4978'] = func_4978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4978_call = mutated_mod.get_global_var('func_4978')
call_4979 = func_4978_call()
output = call_4979
func_4980 = relay.Function([], output)
mutated_mod['func_4980'] = func_4980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3130_call = mutated_mod.get_global_var('func_3130')
call_4994 = relay.TupleGetItem(func_3129_call(), 0)
call_4995 = relay.TupleGetItem(func_3130_call(), 0)
output = relay.Tuple([call_4994,])
output2 = relay.Tuple([call_4995,])
func_5020 = relay.Function([], output)
mod['func_5020'] = func_5020
mod = relay.transform.InferType()(mod)
output = func_5020()
func_5021 = relay.Function([], output)
mutated_mod['func_5021'] = func_5021
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5047 = relay.var("var_5047", dtype = "float32", shape = (7, 1, 12))#candidate|5047|(7, 1, 12)|var|float32
uop_5048 = relay.acos(var_5047.astype('float32')) # shape=(7, 1, 12)
func_2190_call = mod.get_global_var('func_2190')
func_2193_call = mutated_mod.get_global_var('func_2193')
const_5065 = relay.const([9.348526,1.365658,2.309610,0.174040,-7.443824,-6.622249,-7.922933,-2.665773,-0.184907,-9.844705,-0.701956,-2.670028,-2.919893,1.375763,2.542846,-7.463127,9.895924,-0.614892,2.053696,0.966890,-2.515019,5.597955,-0.410596,1.560028,-5.145893,7.814135,2.607471,-9.500298,4.626969,3.757452,7.930762,-5.756008,6.416959,9.244228,-1.613243,-4.164443,7.801207,5.267657,7.350307,-0.011485,2.793660,-5.133014,6.954805,-9.506899,4.912615,6.495133,-6.078487,5.974585,-2.462216,-1.749119,8.640462,-7.606090,-4.077760,-2.510760,-2.563154,6.506378,-2.767070,-5.122173,-6.141607,-4.065438,-1.581100,-8.388828,7.322335,-1.178630,8.808688,0.032120,6.413190,6.701087,4.514278,8.653516,-3.882420,3.965724,0.255512,-9.981256,0.482714,3.627451,1.728977,-6.582950,8.013055,-5.876981,1.570766,3.627458,8.422978,-2.949332,-6.334512,-5.436173,-1.889276,7.967132,7.947334,6.561766,-0.765351,-6.780939,6.550347,4.859113,7.400876,2.584213,2.881844,0.340192,3.968659,3.274339,-3.288801,-5.126488,-2.651526,-6.284885,4.865063,-4.811805,-2.648683,4.035420,1.810719,-1.943910,5.718430,4.043218,-3.965995,9.490155,-1.524861,4.560284,6.331149,4.631064,8.979227,1.209470,7.288885,-5.672503,3.235637,8.643150,-0.788610,3.129177,0.183277,-3.449773,-1.812013,9.898478,5.203170,7.995931,-4.179324,-2.292549,-2.198252,9.462468,5.216380,3.032594,5.629697,1.405963,-2.952255,7.104776,8.326931,5.421954,-5.918556,-7.859485,3.972773,-4.153943,-0.266738,7.349750,-1.921227,-7.423429,-1.793977,-7.645989,9.463314,-9.285096,2.518246,0.674658,6.594924,-5.246679,-0.584975,1.074975,-0.481582,3.073357,-4.191919,9.277403,6.274279,-6.732865,3.805063,-7.026862,-9.099017,-3.639236,-2.422607,-2.083953,-8.287822,1.089353,5.123480,-4.744811,-5.775308,-3.710349,-9.893125,-5.563481,-8.284236,7.894813,5.204653,-2.422323,-1.168016,4.300138,-5.448550,3.174565,-1.503640,6.024240,7.288913,3.553699,-4.055830,8.199729,8.124525,-0.129131,-6.820667,2.599037,3.573450,-7.596660,-9.744706,6.319093,7.716894,3.855964,8.741432,-9.954622,-6.800565,3.514150,7.104483,8.274124,-3.088342,-4.943095,-4.746412,-6.284650,5.019859,7.521632,0.604528,0.151008,1.688264,-9.877815,2.363799,-9.374815,2.024714,-2.252420,-3.277390,5.731118,-0.298451,7.696635,-6.636515,-7.952420,-8.406843,1.318365,-3.815913,2.596111,-7.876203,0.895094,-9.424918,2.167138,7.639975,-3.515257,-1.229666,-1.841448,-8.696584,4.837426,7.353930,-8.528979,2.605272,5.757447,-9.062803,-7.928555,8.479223,1.761450,9.803185,1.851543,-8.504718,-6.967358,2.696267,5.821508,-0.219696,-1.607859,5.269331,-9.482981,0.489180,-6.066433,-0.524396,-0.620170,-1.252412,5.599225,-1.033524,-8.960683,-3.056038,6.023553,5.234330,9.525123,5.295246,-1.869967,4.574083,-7.746482,-3.698249,-0.058481,9.688368,-4.089875,-8.108521,9.453494,-8.584423,-2.547912,-0.456635,4.100375,-8.242249,1.932395,-1.268001,-3.359491,-9.398558,-9.916802,-5.026832,6.934459,5.004108,5.092294,1.293114,6.396305,1.143883,4.896695,1.348957,7.107219,0.453829,-2.152852,-3.972359,0.630255,1.480788,-3.689400,2.366882,0.843681,6.529754,-6.572128,5.712435,8.851499,9.446387,-0.670502,5.690474,3.752799,-1.459138,-9.620015,-7.313286,-1.621902,-3.947267,2.087011,-9.784471,-4.120573,-3.118266,8.031757,-3.368197,-7.018581,5.577724,4.125073,-2.027808,4.627743,-6.435183,-2.480725,-8.861959,-1.434740,6.656431,-2.867228,-7.136526,5.020933,4.084189,-1.700618,8.149046,-4.569050,6.395736,8.287190,-1.990676,-6.861027,3.142398,4.647867,6.371478,-6.944673,-8.170973,8.648392,5.471470,8.149379,0.314787,0.692888,-7.429409,0.185538,8.230685,0.244122,4.931652,-9.045445,-1.750379,-1.593722,8.421315,-4.490175,2.449408,-6.332051,5.725714,-5.200714,7.408836,0.970758,0.658038,5.802835,-3.913537,-8.630325,-4.155256,-3.112932,-1.553077,3.964258,1.401176,7.807438,6.989256,8.300106,7.300307,8.533388,4.774904,-9.948453,9.895795,5.356004,3.443493,5.443423,-4.741001,-6.472059,4.269438,-1.035148,-0.859234,6.827813,8.181361,-7.069345,-2.668623,5.207447,-5.890972,-0.362444,2.430949,8.178753,1.173258,1.865955,-1.567104,5.308157,2.551675,-2.821607,5.893622,9.352266,1.256519,-4.206958,4.016000,1.191626,3.380462,3.051573,-7.790751,7.023571,2.905236,0.002408,8.387269,1.730354,0.338651,-7.697709,-7.447790,4.470723,6.314619,2.859886,-5.352670,-6.009514,0.667377,-1.526892,4.617169,7.024425,-9.505052,-2.332625,1.586729,-1.599498,-3.097441,-9.875575,-1.433888,-6.998316,0.383721,-0.922402,-8.990435,5.390708,-3.957212,4.359163,-6.087463,7.537774,-5.703601,-7.109585,6.423360,-2.899311,1.818875,-0.886061,-7.602785,9.249747,5.365864,4.664831,-4.300043,1.814104,6.147251,-7.230270,9.308202,-8.604778,-1.915727,-9.749252,-6.121716,2.493633,7.044704,2.236857,-5.249626,7.478143,5.181827,0.451174,5.624707,-4.610558,-6.008994,-7.257072,-0.779510,7.367042,3.231068,4.423600,-1.559469,2.352963,-1.697300,7.150918,3.111267,-7.408596,-8.772498,2.718231,-3.982096,-4.108533,-9.523392,7.992430,5.667134,4.096383,-8.232298,-6.122589,2.621819,-0.827223,7.355017,-7.081515,-0.942747,6.684859,3.817305,-6.262355,-4.084730,-3.551511,-4.208123,-1.004107,-4.951500,-7.342380,-4.652039,2.312271,1.196327,8.448444,8.370051,9.273772,8.500028,-6.452032,2.883558,-9.243158,3.308755,6.997254,-9.050795,-4.662610,0.058121,1.296437,6.771545,-0.834110,-3.468555,0.312760,8.333808,1.853084,7.853919,8.538669,7.883628,7.660360,-3.701457,-6.846820,-4.433844,8.440590,1.436428,5.902021,8.522809,5.555514,6.500847,-1.264695,-9.682312,2.048459,3.523736,-4.128627,0.387376,-4.935133,-2.492483,-2.714574,3.897947,3.464461,0.571649,7.526044,-7.373258,-7.534459,-9.179590,-7.866231,9.458104,-0.352832,7.774418,4.014324,-0.740008,-8.633980,-6.443242,1.707188,7.566133,-7.080407,5.285191,2.069065,1.494728,-8.150259,-8.724234,-6.804724,-8.037798,0.666869,5.503333,-4.348878,-1.366361,9.026073,-4.982297,-4.355783,0.493556,-8.880361,-7.783927,-6.984835,8.056398,2.304322,9.562181,9.318597,1.861154,7.347942,5.369508,-4.925893,9.622903,-4.687163,4.587585,9.039737,-1.334052,4.376950,8.673422,-2.445769,-2.985307,7.898108,6.366001,-9.998320,6.856921,1.910946,8.357780,-9.462020,1.226426,-6.560092,3.555212,9.994286,6.633022,-8.102094,-3.010213,-0.773396,3.342010,3.001035,-7.024684,8.947367,6.648853,8.666392,-8.305353,2.877417,-2.714000,-4.811217,5.758735,9.964664,2.699102,-3.052504,-3.831264,-6.454308,-6.315638,-5.313555,3.246535,-0.834919,9.066891,-1.932481,6.830177,8.809204,5.268637,9.623642,-5.344508,-6.769157,-1.736887,2.570897,3.079334,-1.623890,2.965523,-7.342132,-4.572196,-6.630781,-2.415967,-6.282947,-4.002750,-8.975310,0.652867,7.975762,-0.674465,5.318922,-4.301633,-7.257363,1.223226,1.555787,3.612392,4.637363,-5.526926,9.735253,-0.288291,-6.880712,-3.087336,2.292158,-2.948324,3.742383,-3.228394,0.053615,6.458510,-0.024815,2.339733,-1.272351,6.049595,-9.027716,8.921241,4.059768,6.430158,-9.561938,-0.883904,-1.480117,-0.451908,1.937836,-9.357914,8.072268,-3.989635,-7.183745,1.129317,6.778017,1.668431,-1.196195,0.293538,-5.668342,1.661223,-1.145763,-4.267358,-4.306114,-9.249704,3.186435,2.344284,8.156991,-7.436276,7.816867,-3.939330,6.833232,-8.892454,-7.290149,7.096571,3.650547,3.056412,-2.545003,-6.064075,9.182242,-3.937958,7.719530,7.109990,-8.209605,0.498496,-9.392821,-5.361348,0.508403,0.985942,-7.535220,-9.018198,-8.599579,-7.300303,-4.027902,3.372150,8.655151,-8.106810,6.494856,9.685829,-0.944269,4.430536,-6.841817,-4.665814,0.256900,1.106824,-7.591664,7.672664,-3.437342,3.142954,-5.926722,-2.116912,-2.273605,-9.093959,-4.469365,8.148832,-7.722555,3.457589,-1.547042,-8.296593,-1.055410,-5.161189,-8.284011,3.368019,7.910946,7.025785,4.351643,8.415875,-4.055558,-8.232469,-3.735488,7.209474,-8.220651,1.162744,-7.522086,-3.376289,-8.112103,6.353401,-6.496346,1.999576,4.980701,3.053725,-5.744750,1.683198,1.351310,0.529040,8.919847,-3.527986,-0.721161,3.906228,-3.153499,9.768370,-8.281953,4.503185,0.891402,-5.535389,6.465083,5.454278,-4.439964,-1.373395,-1.180794,1.589249,9.733244,-8.396625,-4.367830,-5.390655,9.044438,9.211471,2.175981,7.091502,2.106760,9.022807,4.754481,-6.675943,8.634446,8.473644,-9.092764,-3.439835,3.123238,5.575189,-4.225188,-6.581979,9.283534,4.521075,-7.869999,8.093527,-3.391215,-3.620591,-1.920529,5.674498,9.295513,3.824577,-2.985614,3.601129,-3.096382,2.800563,7.045039,6.563164,8.113248,9.086613,2.322124,4.812677,8.133183,2.825933,-5.543362,-7.411178,-5.320756,9.804612,4.788933,-0.312456,-6.971360,-7.047278,1.502755,-0.699365,-3.868271,-5.913144,3.347041,6.007683,3.827585,-2.686781,4.349409,7.783513,-4.323075,-0.116168,-0.245464,-8.297664,-5.594008,-2.668338,-5.371639,-5.883376,-6.413585,-0.099339,-4.248287,-9.728894,-5.993555,4.337136,6.593075,7.012053,-2.383062,8.766523,-7.938147,6.996128,-1.703365,-7.832785,-4.793695,5.181941,1.241991,-2.412806,4.211217,1.360052,0.948475,-4.792960,-7.462176,4.615281,4.477446,5.679772,-8.955057,5.701751,-1.041935,8.355600,-0.274457,7.328439,-9.312253,-7.093049,-7.633994,1.366822,-2.792460,3.483880,-5.801334,8.436869,1.081287,3.017757,1.637811,0.589413,0.888485,6.819442,8.624804,5.464415,-8.381754,-8.757103,-1.422283,8.551876,9.877421,7.134021,8.593434,5.912100,0.294461,-6.872204,1.086174,-6.904744,-0.427612,5.674020,-7.803509,0.848739,-4.641653,7.745030,0.746955,6.176064,9.014311,-1.561358,-7.182325,-8.931075,5.701691,-5.925686,-5.706344,0.644991,-6.555639,-0.479468,6.705826,-7.840621,4.214844,-9.440193,-4.524074,5.840272,-4.069718,-4.663369,-2.594034,-2.998597,5.552708,-5.708241,2.172743,-2.020922,-3.251408,-5.336214,-4.109931,1.538687,6.966771,-1.498993,-5.286441,0.334865,-0.943663,2.212731,-2.926924,-0.265947,-2.837786,9.802983,-9.047023,-3.690388,8.068347,-3.039429,8.976164,9.463446,-0.461724,-1.441028,-3.715760,6.639290,6.079782,5.619810,3.291415,8.218685,-0.561480,5.387021,-3.241705,-5.697441,8.895803,3.210098,-3.105863,6.538433,-9.114477,0.330969,4.843433,5.967278,8.307978,8.643698,-0.006435,2.636211,8.433990,2.771616,-8.420644,2.583920,2.828684,-0.297211,-3.734875,-9.798503,2.338203,8.445374,-8.668419,8.179261,1.862253,-1.718233,3.930904,-1.159476,8.595128,-5.121506,4.738571,8.815455,-4.584957,6.859743,0.812030,6.563870,4.794633,4.646742,-6.087544,-1.025543,5.474459,3.923318,-6.326821,-3.223649,-6.439550,7.008970,-0.894144,-4.188298,-4.570013,0.986869,6.517040,-0.094778,6.786930,-7.016784,-4.597757,4.695237,-1.987668,-1.791620,8.285957,-3.498092,1.032370,4.151962,-6.269766,-1.679261,9.158971,-0.461145,-8.852222,-6.343274,-3.224604,7.484241,9.115208,4.172741,-8.501654,-0.615631,-8.963933,7.535419,-3.527732,0.523855,-3.828523,9.577799,-8.971202,-3.602076,-0.076305,-2.465857,6.019207,8.280248,9.738733,-0.953053,-7.168801,5.570899,0.984839,-3.619684,6.519373,-1.079785,4.547500,-2.087409,5.614645,-9.617693,3.744098,6.826011,1.951708,0.110742,9.960711,-4.942465,-2.003700,-7.681407,-1.724323,3.686685,-3.743828,1.776590,2.006363,1.494214,-5.960385,-1.130250,9.345839,-1.655510,-7.843502,6.052665,-6.810832,0.025078,8.938584,-4.141389,-2.098782,7.763695,-5.016557,-0.248870,-5.355369,-4.381383,7.767791,-5.638103,-3.173745,8.949834,-6.525539,-3.431220,-1.716475,0.702039,4.882044,8.708604,1.997120,3.549626,2.066899,7.389493,5.546101,-8.461305,-6.732560,4.923126,-6.677045,5.898730,7.264959,3.791148,4.690153,5.363609,-9.097322,-8.557831,-3.275832,2.020651,9.051380,4.021724,2.526721,-1.324636,2.874939,-5.638790,-0.848625,-2.976965,-2.057503,-7.899798,6.123823,-6.384886,-5.785391,0.599008,-0.329608,5.758382,-5.458622,6.691603,-4.318903,1.741591,3.556405,5.304247,-7.762830,-2.424086,6.036800,-1.971859,-3.542622,7.140726,-2.879244,0.692961,5.771858,-5.080008,-1.205160,8.903667,2.606038,-0.870623,5.048512,9.345514,5.179327,-3.058759,-1.307541,4.590553,3.053435,5.750901,-3.018964,5.434517,9.519252,3.920685,6.160443,6.238816,7.517139,0.170019,2.692758,-1.300297,-3.101642,-2.935160,-9.678370,-9.407692,-4.319981,5.470560,-6.671705,-3.408812,-7.941906,9.457010,5.971535,5.096115,-3.770496,3.603627,0.414475,2.388026,-7.376415,-9.642716,1.296688,-0.906425,-0.613436,-3.801343,-9.798979,5.755517,-9.013928,-2.050976,4.918785,0.073730,3.747744,5.529586,-8.156735,-2.325734,-9.317084,0.204914,8.990618,2.136347,1.405174,7.341053,6.905202,5.314240,7.304988,8.046017,2.331699,9.523409,4.575120,2.536790,6.627169,-1.810486,-1.570746,3.475094,6.314395,2.899590,1.315548,4.215230,2.791697,-4.220924,-6.813498,1.354490,-3.515799,-3.810944,-2.998545,-4.643507,-9.003955,6.241303,-4.161981,-5.001004,-9.472272,5.924677,-7.000261,-2.211184,9.292771,7.235473,-7.088600,9.853750,8.597748,-4.748059,4.931052,1.473850,7.996885,-8.162487,2.001146,1.795974,-2.770709,9.636766,2.048236,8.057851,2.444756,4.940656,8.707330,-1.735958,-9.847711,-7.322679,7.495938,5.462606,4.140751,5.095544,3.933702,-7.168905,3.768303,-7.193325,8.281085,0.936565,-8.945522,-3.357972,5.235937,-5.558543,4.524049,0.963924,-7.401429,7.742074,-8.004631,4.108461,8.386060,7.689628,9.901590,-0.854286,5.896484,1.269318,-7.697610,-6.493957,6.999535,9.369860,8.940900,9.296450,-3.113647,0.626687,6.160578,-6.189632,-2.152373,5.593509,2.883330,-0.933261,7.682618,8.348865,0.882892,9.826846,-2.035173,2.450639,6.221455,-1.891301,1.821632,-9.664478,-5.513324,-3.275861,4.446651,-1.526228,5.659623,7.928851,2.058505,-6.493167,-4.631356,1.225312,-0.457885,0.993363,7.566747,6.750332,5.608304,-3.174448,-0.444873,6.959826,-1.392397,0.170745,-1.095035,0.799976,4.714349,6.397385,2.794470,-3.085264,4.394355,-1.659040,2.563682,-4.542312,8.257198,-7.758846,8.994984,5.972488,-7.637661,3.382690,-6.631766,-8.553729,-0.450109,8.828892,-6.321268,5.117817,1.822038,-4.282887,-8.852632,-9.868627,9.639454,9.850063,-6.162825,1.109713,9.350402,3.336261,4.813494,0.837914,9.185938,2.609465,0.885113,-9.613395,-5.466664,1.639487,2.271093,6.854523,9.474800,5.261332,7.194500,-0.460604,7.675627,-9.662744,8.916515,-7.696560,8.611312,-8.461110,-6.771597,4.095105,9.716307,0.454830,-4.999113,-1.550443,-9.357033,2.924654,-7.656376,-5.849303,-6.271928,-7.357577,9.958312,-3.412092,-0.086578,7.818543,7.720253,-6.266775,8.941401,8.107493,-3.754105,5.086389,6.769949,-4.564687,-0.103229,3.235956,-4.261219,-6.431081,-8.981473,-8.128584,2.014710,-8.233270,-5.494118,-9.309950,-3.382977,-4.429253,9.688164,2.890363,-9.068854,-2.991660,8.882211,5.831853,0.147438,2.391930,4.513654,-3.893637,4.840909,8.556587,8.602532,7.889215,-8.027384,-2.140962,-8.021794,-1.850803,-2.736315,5.873380,7.470689,2.695850,6.997992,-9.331071,-3.373885,8.861238,3.216238,0.847678,-8.484895,1.787965,-5.608732,-5.864203,7.338648,-3.802217,1.324950,8.288014,-4.325440,5.111020,4.672274,-7.542575,2.264886,0.776524,4.634631,0.007061,-0.797059,-3.231098,8.945960,9.103456,4.461854,-4.416809,2.393762,1.388670,-5.641792,8.572607,6.555683,9.375732,-4.648767,4.049607,4.874892,9.257003,0.601525,7.305659,5.707323,-4.121467,-7.410232,8.032252,-4.405541,0.425061,-2.378823,5.516300,8.899234,-9.114525,9.446480,1.384156,-9.816675,-1.628072,-8.796000,-9.587630,-8.710056,-1.759241,2.561683,4.288466,5.690212,-6.710288,7.971249,0.828503,-6.964077,-0.101494,3.046999,8.227806,1.225108,-0.138016,2.296941,3.935449,7.623330,-1.321529,2.546383,-6.200119,-8.578083,-9.843557,-2.048160,-1.837535,3.900633,1.065759,-8.890339,0.586857,-9.017004,2.901358,-8.879108,-8.579922,1.481919,6.700577,-8.230946,3.004538,-8.828216,-7.422608,6.410485,-8.574228,-2.783718,8.170150,-0.707466,-4.013570,-6.407870,-0.380274,-9.748067,-3.311422,0.763318,-7.874199,-5.248163,-5.954711,-6.571535,1.239491,-9.402152,-3.349406,2.723088,4.005769,-1.575180,5.423123,-0.752460,-2.256312,-6.894910,-5.114157,-9.827580,5.285302,-6.876402,2.763280,-8.666364,-7.599113,-1.841113,2.606114,-4.048652,3.889591,-6.703756,-3.618582,-6.089558,0.413279,8.876406,-8.960587,7.534356,-9.935288,-0.993843,-9.225975,8.956082,0.016572,1.702215,1.310028,1.756600,2.771905,8.862724,-0.622957,-6.003268,-5.903464,9.968082,7.315230,-8.576352,-3.531241,2.927047,-8.573332,9.200499,1.293555,-0.031808,7.361050,8.232476,-4.414392,-3.477832,7.815997,-5.835112,-6.401531,-0.937604,-6.689408,-0.607344,0.460917,2.881013,-5.568872,3.835835,-4.223760,-1.522777,-8.285462,-3.641162,0.836684,4.789818,2.770512,-4.448024,-7.998050,4.382074,-3.954831,6.756809,7.637596,0.313775,-0.975502,4.748911,-2.126154,-9.297213,-3.342280,8.459279,2.610772,-6.933519,9.463047,-3.513880,6.603841,-5.713885,1.362404,-6.446906,2.229756,-4.011549,-8.057146,-1.905441,-2.750589,6.353951,2.656967,-9.814409,-8.731640,5.191923,8.830734,8.918179,8.984560,-4.064787,8.897212,2.332590,-1.468257,-2.077687,-0.749438,-2.913517,1.576941,6.223312,-7.122757,7.995814,-6.194650,-9.705439,6.197728,-5.730988,-3.949216,5.668748,6.926691,-3.881524,1.468017,2.375989,7.994744,-1.476759,2.264158,7.696457,2.852145,-3.368285,5.112103,8.287754,-8.058332,4.420095,3.397686,9.224481,8.569918,-3.009262,-6.779534,-5.938021,8.270634,8.182278,-9.820547,1.202410,5.010150,7.428473,-4.597350,7.812105,5.680620,7.486713,-5.767864,9.884942,-0.498585,-5.612709,0.516172,-0.640563,0.293015,-7.018718,-3.623811,9.986727,1.191648,-2.450082,5.690201,7.897546,-6.411518,1.918241,2.448724,9.622098,4.461556,-0.036425,-1.340364,4.132671,-1.740149,-6.083303,9.059262,7.736227,-9.678904,0.391887,9.644274,-2.760379,6.623244,-8.501366,5.655639,1.256970,1.968165,6.239649,-0.012927,7.811863,-4.071654,-4.659725,4.646274,4.810209,8.296960,-6.421277,0.483030,2.847853,-1.029445,2.577416,0.130810,-0.821252,-0.489990,-0.204521,8.721035,-0.689481,4.378360,2.323314,-6.349902,2.566550,7.571252,-2.995717,-4.791752,-0.021432,-6.680961,-6.080748,-4.697129,-8.423618,2.467578,5.482639,1.949841,-5.259244,-8.930936,3.175621,-6.814960,0.111030,-2.800557,-9.319231,8.949156,-2.570248,-8.636676,0.135889,7.310697,-4.060538,-5.407627,4.910111,9.697923,1.318563,-4.443201,-0.050026,9.951547,-3.541625,7.589573,-8.760603,8.279474,-9.206952,-0.710577,-0.077464,-0.876374,-6.573923,0.063010,-6.112375,3.021384,-6.364967,-9.770687,2.995490,-7.686415,-2.322848,-6.136269,-3.112813,3.633966,-5.578934,-9.272719,3.500568,5.516409,-6.126462,-7.166352,4.860308,-6.900940,7.060564,-1.985071,-4.695380,-5.588551,-1.854964,8.379454,6.246296,-7.884918,-3.051118,-8.824563,9.579039,5.373527,-2.955633,-2.744248,-3.304501,-5.917631,6.031901,-4.244031,1.573601,-6.131350,3.485438,1.905163,-6.224948,-1.317362,-0.214361,5.780088,-6.818008,2.473189,-1.794633,-8.602922,-7.015370,-1.610500,1.473576,1.183807,7.606341,6.940517,-0.750660,2.009838,-0.342031,0.020752,9.028066,-3.226073,-5.390929,-2.828853,9.468104,2.630005,6.661626,1.450226,-8.424860,-9.503770,3.407111,-7.626429,-0.862484,-2.473881,-1.122072,5.698828,-3.745252,1.435618,-6.083412,4.119321,1.997503,0.031024,-5.016560,0.011348,-6.054354,9.932733,1.320186,5.299622,6.962534,-0.040754,1.999603,5.030484,8.733289,-1.460452,9.927281,7.945938,-3.854103,4.415997,-0.996152,8.973765,-0.587918,-2.235512,7.191624,9.572380,1.864529,-1.599213,-1.679230,3.392603,-8.177859,4.045417,9.872801,-1.053628,8.252369,4.807595,6.847793,-7.235490,4.266671,1.599058,-7.377467,9.992431,7.784824,3.287530,-3.085652,9.982158,-3.272691,-7.285316,-8.725749,-3.807552,-6.769424,3.276950,-9.294096,-8.195199,-3.519487,-2.280947,-9.279669,-8.328325,4.473101,6.000749,-1.555260,6.045427,5.510545,3.077750,-6.257681,-6.172827,0.632658,-1.981888,2.065935,6.599787,8.042720,9.564480,0.169930,5.022348,9.166315,-8.095075,8.344332,-7.092261,2.814890,-5.965388,3.114286,0.964249,-7.450790,1.884423,-1.149106,8.912365,-6.055360,5.156695,5.363506,9.812164,-4.756485,-3.846559], dtype = "float64")#candidate|5065|(2025,)|const|float64
const_5066 = relay.const([-4.292767,-7.587603,2.212162,-8.630649,-6.627567,-7.792305,-4.154837,-3.991858,-6.232845,8.329125,-6.544645,-8.795364,-4.789253,-2.085950,9.155688,7.167062,-1.777566,-8.343817,1.479184,4.298173,-7.093163,-2.901811,-9.566318,6.193384,-8.699896,-9.923074,8.944486,7.148938,5.173553,6.438965,5.995826,5.659521,1.038425,5.031361,-0.159383,-0.140429,-0.161590,-9.544250,0.086939,3.379803,-5.866060,-9.072934,-8.909901,8.818548,2.344135,2.644088,0.560043,-6.684184,-2.449145,7.465002,6.684046,6.636276,-6.960729,-6.153112,8.820441,-5.215905,0.245768,-8.959484,-4.479158,2.039611,-6.846201,-1.520676,8.325956,-3.430694,0.101040,1.430381,3.041622,-4.805656,-9.051098,5.529185,0.962231,6.205852,-7.830823,-4.277604,5.234295,5.713926,-4.542152,-6.182222,-2.167216,6.498420,-2.036059,-1.087551,3.744023,-5.128277,5.017648,-0.995256,6.409680,5.806322,6.858233,-3.731884,-4.922422,-5.846159,-1.431144,-2.607608,-2.055806,-0.870462,-2.557670,-1.213534,7.340112,5.467018,0.457925,9.054758,9.391709,-6.115866,7.818543,-7.390669,-9.414361,-1.019192,3.055446,-6.872626,1.640329,-3.924087,4.205588,4.774684,0.005988,-3.945745,-0.122340,4.192758,-4.198142,-5.466608,3.030221,9.638772,-2.426631,-5.500620,4.182390,9.371144,6.855245,-2.684555,-4.631116,2.707182,8.048659,-5.478004,-9.320704,1.489868,-9.607201,-4.343584,-5.167747,6.952604,1.533233,-2.362791,-3.298737,9.620555,-3.805113,5.557806,-3.163305,-5.172656,-5.404078,8.864911,9.867989,3.025004,6.300043,5.579250,-6.961087,-3.873589,-9.670126,-3.896278,-6.093446,-7.502980,8.716420,3.358400,-4.106863,4.240646,9.180949,8.411724,-9.408330,-6.319303,-6.114148,0.800050,-0.311944,5.629772,7.639947,-0.350770,8.644098,-0.235265,-1.240732,-5.643481,0.702736,8.789073,1.183591,3.690967,5.807316,0.754796,6.628692,-6.136856,-7.931426,-9.186282,1.673857,0.717030,2.767424,-4.645186,5.983337,2.451158,-5.807840,0.880639,9.342916,2.985888,-3.617753,1.974921,-6.174727,-7.665553,3.195329,-5.692487,2.340835,8.173936,1.473735,-5.091630,8.118815,2.954908,-9.405797,5.149490,-0.897921,-1.216704,8.101095,-0.144486,-9.747028,-7.880218,-4.946614,-2.978977,-9.882032,-7.783043,4.656173,-2.966240,-0.634158,0.398312,6.082466,5.977038,0.590638,-6.233078,7.496003,-0.890052,4.501500,7.147943,5.890619,2.287150,3.316846,6.226056,-0.557459,2.291905,-2.654346,4.816922,4.163467,3.066550,8.481500,0.598519,-0.164048,-3.144616,-8.566787,9.184030,4.071339,8.483954,6.697761,-0.416081,1.094057,-6.420041,-9.698864,7.464434,-0.452120,-2.747671,-9.081173,-5.345566,-4.358578,6.548156,-6.505343,-3.803818,1.017369,2.067697,3.415530,0.394739,7.150269,-2.024832,4.104092,-1.042576,-7.172315,1.468844,-5.955369,9.633234,-8.144262,-0.902125,-2.901925,6.759275,-7.930953,-5.618240,-7.519930,-2.921406,3.894568,5.576322,-7.075636,5.955594,-1.747528,-2.242164,-0.971480,2.981061,-6.477158,-1.610499,0.589296,-9.036011,-3.716865,9.728030,-3.112004,-4.273050,-6.865950,1.322715,3.478179,4.166257,1.026282,9.034769,3.264715,8.615410,-7.123042,-2.328869,8.495434,0.938687,2.246596,-8.084357,5.183410], dtype = "float32")#candidate|5066|(315,)|const|float32
call_5064 = relay.TupleGetItem(func_2190_call(relay.reshape(const_5065.astype('float64'), [2025,]), relay.reshape(const_5066.astype('float32'), [315,]), ), 4)
call_5067 = relay.TupleGetItem(func_2193_call(relay.reshape(const_5065.astype('float64'), [2025,]), relay.reshape(const_5066.astype('float32'), [315,]), ), 4)
output = relay.Tuple([uop_5048,call_5064,const_5065,const_5066,])
output2 = relay.Tuple([uop_5048,call_5067,const_5065,const_5066,])
func_5068 = relay.Function([var_5047,], output)
mod['func_5068'] = func_5068
mod = relay.transform.InferType()(mod)
var_5069 = relay.var("var_5069", dtype = "float32", shape = (7, 1, 12))#candidate|5069|(7, 1, 12)|var|float32
output = func_5068(var_5069)
func_5070 = relay.Function([var_5069], output)
mutated_mod['func_5070'] = func_5070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4045_call = mod.get_global_var('func_4045')
func_4047_call = mutated_mod.get_global_var('func_4047')
call_5111 = func_4045_call()
call_5112 = func_4045_call()
output = relay.Tuple([call_5111,])
output2 = relay.Tuple([call_5112,])
func_5129 = relay.Function([], output)
mod['func_5129'] = func_5129
mod = relay.transform.InferType()(mod)
mutated_mod['func_5129'] = func_5129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5129_call = mutated_mod.get_global_var('func_5129')
call_5130 = func_5129_call()
output = call_5130
func_5131 = relay.Function([], output)
mutated_mod['func_5131'] = func_5131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3401_call = mod.get_global_var('func_3401')
func_3403_call = mutated_mod.get_global_var('func_3403')
call_5179 = relay.TupleGetItem(func_3401_call(), 0)
call_5180 = relay.TupleGetItem(func_3403_call(), 0)
func_2491_call = mod.get_global_var('func_2491')
func_2492_call = mutated_mod.get_global_var('func_2492')
call_5185 = relay.TupleGetItem(func_2491_call(), 0)
call_5186 = relay.TupleGetItem(func_2492_call(), 0)
output = relay.Tuple([call_5179,call_5185,])
output2 = relay.Tuple([call_5180,call_5186,])
func_5206 = relay.Function([], output)
mod['func_5206'] = func_5206
mod = relay.transform.InferType()(mod)
mutated_mod['func_5206'] = func_5206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5206_call = mutated_mod.get_global_var('func_5206')
call_5207 = func_5206_call()
output = call_5207
func_5208 = relay.Function([], output)
mutated_mod['func_5208'] = func_5208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4959_call = mod.get_global_var('func_4959')
func_4960_call = mutated_mod.get_global_var('func_4960')
call_5229 = relay.TupleGetItem(func_4959_call(), 0)
call_5230 = relay.TupleGetItem(func_4960_call(), 0)
func_3969_call = mod.get_global_var('func_3969')
func_3972_call = mutated_mod.get_global_var('func_3972')
const_5234 = relay.const([9.475140,-4.705465,-1.005170,-1.359354,1.028092,-1.964212,1.409189,-2.043478,7.986156,0.562713,-2.734189,8.539041,-8.459784,3.935784,-5.721687,6.288783,-8.758699,-5.979348,-5.998593,-9.648617,2.643083,7.143464,-1.897939,-7.279162,7.090783,-0.009104,-1.747977,7.807999,0.459270,-2.425914,-3.977813,7.086045,-6.442615,3.789995,-3.757039,-7.917192,-1.815730,-2.741615,3.400926,-5.472323,-7.446847,-3.252696,-6.206077,-9.817318,-9.596974,0.187768,-2.811607,3.861667,-5.380530,4.582455,-5.321463,-5.178963,7.572546,-4.216111,-8.365504,2.642596,6.723799,3.793504,-3.872666,7.992191,7.373204,8.408987,3.285976,-7.943093,6.455805,-3.522718,1.099445,-2.149133,7.392940,4.811591,9.395329,8.884312,-1.942702,-1.352444,-3.414274,6.690824,4.181336,5.312709,0.708952,-7.616735,0.281293,-4.541086,-5.575080,-8.153057,8.777241,7.491824,-9.035497,7.069237,4.706888,4.016051,4.240604,2.044384,0.205398,6.880934,-7.339605,1.377795,-8.123932,-0.698395,-0.571852,0.064646,-1.017688,-9.709633,6.867162,5.848879,-4.247114,-9.837979,5.519348,-9.138681,-2.992392,9.042219,1.689039,-0.893217,3.215463,-6.634657,5.748440,7.676435,-0.540500,4.998869,-4.593452,7.890217,5.762730,-3.225802,0.915332,-5.032010,2.496409,7.586802,-1.713457,-8.425100,-0.363171,-8.596078,-3.039658,-1.672461,7.962281,-9.551934,-9.066421,-2.282925,3.303501,5.817682,0.030475,-3.891777,7.132436,-5.187618,-9.359330,4.145557,4.243072,-6.995750,-2.448112,5.755597,-7.034990,9.650671,6.544572,3.011567,-6.266758,2.564148,-8.996433,-5.387805,2.038351,5.315881,-8.993246,2.077383,-4.772925,4.347401,-1.878482,5.552954,1.663834,4.194158,-5.974430,6.455272,3.620722,0.645971,6.987854,-0.374869,-8.028210,-5.635171,-0.209552,-6.776984,4.655067,7.449374,-2.981350,6.775341,7.365466,-1.426188,3.764105,0.545922,4.997668,-9.785627,-1.746318,1.969061,-1.176040,9.820477,1.089723,-4.639991,-0.953302,-9.534120,-8.460056,-8.305482,9.678786,1.869907,-5.781447,6.512991,1.733608,-2.346624,-8.182764,-5.393578,3.679071,-6.367319,-9.389004,-1.918968,-5.394988,2.165207,-9.911486,6.736681,3.570402,-7.900743,2.038421,8.946306,6.032509,-0.920592,4.494175,-6.425904,2.728784,-3.838505,5.680662,-4.862538,1.947853,-0.200963,1.330408,5.036451,1.485635,-0.947610,-4.585725,6.952343,-2.110211,7.448663,5.902047,-3.983691,-1.182396,-5.115107,2.635825,-2.691152,-5.185495,-0.364348,-0.454584,-7.839067,9.005251,-5.550634,-0.109623,1.100859,1.319376,9.719625,3.453021,0.550060,-9.037925,1.266719,-6.874001,-3.641517], dtype = "float32")#candidate|5234|(256,)|const|float32
call_5233 = relay.TupleGetItem(func_3969_call(relay.reshape(const_5234.astype('float32'), [256,])), 3)
call_5235 = relay.TupleGetItem(func_3972_call(relay.reshape(const_5234.astype('float32'), [256,])), 3)
output = relay.Tuple([call_5229,call_5233,const_5234,])
output2 = relay.Tuple([call_5230,call_5235,const_5234,])
func_5242 = relay.Function([], output)
mod['func_5242'] = func_5242
mod = relay.transform.InferType()(mod)
mutated_mod['func_5242'] = func_5242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5242_call = mutated_mod.get_global_var('func_5242')
call_5243 = func_5242_call()
output = call_5243
func_5244 = relay.Function([], output)
mutated_mod['func_5244'] = func_5244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2708_call = mod.get_global_var('func_2708')
func_2709_call = mutated_mod.get_global_var('func_2709')
call_5278 = func_2708_call()
call_5279 = func_2708_call()
output = call_5278
output2 = call_5279
func_5295 = relay.Function([], output)
mod['func_5295'] = func_5295
mod = relay.transform.InferType()(mod)
mutated_mod['func_5295'] = func_5295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5295_call = mutated_mod.get_global_var('func_5295')
call_5296 = func_5295_call()
output = call_5296
func_5297 = relay.Function([], output)
mutated_mod['func_5297'] = func_5297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3391_call = mod.get_global_var('func_3391')
func_3393_call = mutated_mod.get_global_var('func_3393')
call_5304 = func_3391_call()
call_5305 = func_3391_call()
output = relay.Tuple([call_5304,])
output2 = relay.Tuple([call_5305,])
func_5308 = relay.Function([], output)
mod['func_5308'] = func_5308
mod = relay.transform.InferType()(mod)
mutated_mod['func_5308'] = func_5308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5308_call = mutated_mod.get_global_var('func_5308')
call_5309 = func_5308_call()
output = call_5309
func_5310 = relay.Function([], output)
mutated_mod['func_5310'] = func_5310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_5444 = func_2385_call()
call_5445 = func_2385_call()
func_5242_call = mod.get_global_var('func_5242')
func_5244_call = mutated_mod.get_global_var('func_5244')
call_5451 = relay.TupleGetItem(func_5242_call(), 2)
call_5452 = relay.TupleGetItem(func_5244_call(), 2)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
var_5496 = relay.var("var_5496", dtype = "float32", shape = (6, 220))#candidate|5496|(6, 220)|var|float32
call_5495 = func_2305_call(relay.reshape(var_5496.astype('float32'), [11, 15, 8]))
call_5497 = func_2305_call(relay.reshape(var_5496.astype('float32'), [11, 15, 8]))
output = relay.Tuple([call_5444,call_5451,call_5495,var_5496,])
output2 = relay.Tuple([call_5445,call_5452,call_5497,var_5496,])
func_5529 = relay.Function([var_5496,], output)
mod['func_5529'] = func_5529
mod = relay.transform.InferType()(mod)
var_5530 = relay.var("var_5530", dtype = "float32", shape = (6, 220))#candidate|5530|(6, 220)|var|float32
output = func_5529(var_5530)
func_5531 = relay.Function([var_5530], output)
mutated_mod['func_5531'] = func_5531
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5539 = relay.const([[[-2.250746],[-4.985641],[1.902715],[-8.455337],[-8.830662],[9.049615],[6.295716],[0.875865],[-7.094599],[-0.911617],[-8.816180],[3.730410],[-8.259952],[-0.113461],[-3.086662]],[[-7.358815],[0.451395],[-8.611715],[5.071116],[-8.538818],[2.783536],[8.171458],[-4.457846],[2.417636],[5.949039],[9.525272],[4.864958],[-0.479564],[1.958952],[0.429259]],[[-2.712838],[-7.697375],[-7.754479],[1.377285],[4.437413],[5.828086],[2.658885],[-8.975200],[4.422435],[-8.566113],[4.185419],[-3.031461],[5.351063],[-9.563490],[5.781353]],[[-1.965015],[7.085936],[9.512913],[0.832188],[-0.904016],[2.665601],[-4.492592],[-6.919621],[-9.632181],[-7.630795],[-2.238033],[-7.020885],[-0.877578],[9.289179],[-7.250935]]], dtype = "float64")#candidate|5539|(4, 15, 1)|const|float64
uop_5540 = relay.asinh(const_5539.astype('float64')) # shape=(4, 15, 1)
output = relay.Tuple([uop_5540,])
output2 = relay.Tuple([uop_5540,])
func_5542 = relay.Function([], output)
mod['func_5542'] = func_5542
mod = relay.transform.InferType()(mod)
mutated_mod['func_5542'] = func_5542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5542_call = mutated_mod.get_global_var('func_5542')
call_5543 = func_5542_call()
output = call_5543
func_5544 = relay.Function([], output)
mutated_mod['func_5544'] = func_5544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_5555 = func_1295_call()
call_5556 = func_1295_call()
func_3563_call = mod.get_global_var('func_3563')
func_3565_call = mutated_mod.get_global_var('func_3565')
const_5566 = relay.const([-6.033189,-4.566230,-1.775435,-2.226338,-6.666436,-6.796386,1.027856,-4.611946,1.145276,-1.512097,-8.815236,6.256447,-7.425912,-8.115720,7.880762,2.530779,-1.084016,3.368601,-7.494167,3.015680,7.717319,2.423656,1.112696,2.187953,-6.684955,8.230347,8.017532,-9.362466,-1.935361,-7.443158,-3.092307,-4.572589,3.591255,8.178549,6.014697,-4.376981,9.439324,4.035892,8.144663,3.595205,-1.207880,0.801791,2.230591,9.048234,-0.465997,-3.192366,-1.285152,2.418221,-6.097117,4.717776,9.476115,-2.642224,2.155646,-6.822639,-5.629262,2.856327,-5.004663,7.347056,-1.114813,-6.553873,-8.064955,4.693793,2.509652,-5.974748,-0.740090,4.321264,-1.535687,-2.559982,4.311109,-1.957504,-0.731408,6.814751,-2.573662,-9.393402,4.160719,-4.290531,3.620313,-2.161991,-1.784071,-6.933175,-6.571551,8.811977,4.394561,6.158658,-8.868147,0.121723,5.080107,6.090300,8.897721,-5.439213,-9.903540,-4.968856,-8.518510,-3.697601,3.190833,6.399197,-5.611972,-5.280784,-4.801148,0.487197,-8.871424,4.390132,9.815974,7.734320,2.222883,9.026893,-9.337578,9.443961,2.347145,-1.898907,3.943354,-8.979646,-9.557763,2.521857,-2.562838,4.046799,9.354544,-5.256119,0.719111,7.463565,7.179638,0.266799,-2.373192,4.253827,-7.906293,6.637847,6.730656,-0.028079,-9.693737,4.255535,-0.971088,2.490419,0.786861,-7.543162,-2.804555,5.884086,-2.224716,1.068974,-2.158727,-1.533640,-9.886089,-9.600801,-9.636431,7.216465,-3.338695,6.491703,5.332523,9.623278,8.676414,-8.117644,1.887302,9.983971,-9.592799,2.587020,3.499752,9.833664,4.019449,-6.550154,-3.215249,-5.771050,-5.037501,4.756782,9.677143,-4.333709,-1.127074,-7.450884,3.753774,-4.815301,-2.292670,-6.696156,4.404860,-6.194339,3.174995,-7.710130,-0.958772,-6.602569,0.797930,3.138760,-8.982604,7.301173,-2.983211,9.495379,4.816744,0.125431,5.360815,-3.744521,6.190421,1.412638,7.709976,8.062461,-8.855574,-4.447056,5.546962,-5.573016,0.223009,7.538627,4.894042,8.779622,-1.015321,8.331919,-1.603026,-2.558504,-6.481765,-9.554643,-0.166859,0.106973,-4.868008,-3.536580,4.239744,7.505300,-6.766216,-0.093415,5.089011,-5.248862,-9.534210,9.378949,8.072042,8.161860,6.665385,1.238555,7.377419,5.261604,-0.166037,1.315825,-6.965944,0.852620,0.080514,2.324254,1.449341,-9.445541,0.477131,9.661903,-0.405927,-1.821231,-0.023442,1.140076,-4.609311,7.038856,-6.953527,1.713447,-9.428475,8.275173,-1.256347,-5.645576,-7.751700,-2.210785,2.055660,8.183684,-2.368672,6.743511,3.415447,-7.135973,0.525555,1.253826,-2.546370,9.036508,4.786128,7.433970,3.702738,9.609861,-4.746190,2.922876,5.448120,7.895616,-0.919637,6.427625,1.903091,5.919495,8.178709,-4.235193,8.630841,-6.519055,-1.876317,6.225649,-7.647090,-4.384596,-2.207165,-6.381768,-2.038619,5.141484,-6.200666,-5.023270,-0.058596,2.181680,-8.340029,5.264361,3.470780,-8.429396,8.605532,1.770798,7.613018,5.451995,0.634855,9.382006,3.544782,-0.010949,2.823914,-3.024553,-1.994452,-2.847194,2.802584,9.537809,5.884040,4.171689,4.363332,-6.584893,-8.829325,-9.557390,1.941075,3.382407,-9.330277,7.823928,-5.778384,3.723201,8.537765,-1.199727,3.689769,9.550023,6.755133,-3.791028,1.288385,8.419095,-8.751139,9.711420,-1.808000,-6.341799,-6.967283,-3.241558,1.574493,8.789176,6.340380,-3.176746,0.288076,-0.010921,-5.987380,8.093367,1.816179,7.364806,-7.926556,-7.342527,3.888726,3.409494,-7.713564,-9.609663,4.759858,-3.009656,1.564170,-7.183959,-1.460343,-9.401269,5.096086,-7.554386,-4.125114,-9.237524,-1.345757,6.433711,6.986425,2.675668,3.783231,-4.973514,1.805283,8.369366,4.577573,-9.993464,-8.669123,-9.049747,-0.385461,0.693811,-4.535321,-3.625222,-2.026320,-9.973410,-4.917818,9.674812,4.191266,0.236967,-2.312308,-5.570781,-6.883958,4.080441,8.920682,-6.090484,-4.945650,-1.778482,7.797839,0.522750,8.941784,8.518512,8.494034,9.147051,-8.033295,5.906745,7.507365,-8.841075,-0.135077,8.265391,4.523301,-3.452674,6.795277,-8.321038,8.450400,-1.860116,6.654570,-1.279502,-1.242621,-3.329637,-2.232811,4.288619,7.431462,3.444759,3.100927,4.599139,-6.316676,-4.568178,-5.341488,-3.310411,-2.297794,-3.061547,8.009396,-1.816858,-9.716602,-0.479251,-4.002100,9.312789,-5.071172,-0.675722,1.850579,-8.795141,7.953723,9.211292,-8.422887,6.275301,-7.033743,-5.115971,-8.696839,5.649535,2.789501,-1.078155,9.050492,4.172303,-3.520205,2.345839,4.130961,-7.306552,-2.498195,3.619033,8.833943,8.643901,-0.843601,3.396239,-1.401368,-7.824776,1.773561,5.641198,-3.809175,-4.777562,-3.044079,-6.134244,0.581921,-5.668625,-1.338925,-6.550479,-6.273322,0.753475,-6.370681,-0.075831,6.508236,-9.759481,2.559467,3.746605,4.277374,-2.642206,2.012596,3.510987,0.567845,-3.090919,2.632380,-9.311369,-1.014275,3.422151,-0.352849,0.142219,-5.801283,-8.122495,8.594047,7.670973,9.292947,1.415699,-7.741451,-5.611392,-1.249657,2.763734,9.500048,-2.528302,0.284560,-3.672164,2.206746,9.370508,-7.865631,7.964559,9.654681,-1.890695,-5.062014,0.190259,-1.088911,0.921152,-4.824877,7.993411,-7.325880,6.107883,0.540732,6.613700,0.800544,-6.424852,7.574254,7.517987,-9.512646,4.830687,8.670954,9.463194,-0.123531,4.118334,8.019613,4.102401,-4.877991,8.149884,-9.262155,-4.002066,9.361039,2.856917,-1.269345,2.643471,-3.921318,8.517397,7.774897,-6.128193,8.739116,-8.182917,-0.861583,-7.641512,-7.358795,-2.017586,6.795953,-8.450312,3.085834,2.414433,-8.802497,-8.491600,8.318513,9.450292,-8.836524,2.247832,6.635872,-2.993393,3.103301,-3.326409,-1.208141,-3.861227,0.581225,-2.005921,4.437406,-7.678722,-2.864051,-9.723879,-5.153733,-2.866592,5.767202,3.878297,2.243376,-7.714152,-5.686801,-0.681043,4.304402,-0.194291,7.411280,1.489460,-9.386199,-3.986676,-8.714650,4.115863,-8.490349,3.373893,1.927527,-4.236619,-0.835545,1.365059,8.530144,9.748199,-3.378242,9.257881,-1.387482,-2.013349,-4.205074,7.586859,-0.434497,-0.317283,-0.882362,-1.961144,-5.683595,-3.502462,-7.199354,6.593210,1.802724,-2.120832,6.693797,3.150451,1.727118,-1.195216,9.732902,-1.218490,-6.186158,-4.252352,0.638848,-6.497731,-4.207600,-0.780044,-2.514070,-8.805528,3.645175,-5.957108,1.529773,-6.017307,2.402066,-1.572461,9.434712,-6.394670,6.927491,-3.458078,-7.975002,-1.460335,-9.637529,9.970160,5.706162,-2.502888,-4.512870,9.418451,2.851967,-0.844482,-1.941920,7.748815,-0.267311,-1.816049,-8.255586,-6.493117,6.111231,8.569281,9.460168,0.089106,2.389740,5.993083,-1.493407,5.743484,8.177760,-0.747244,-8.527496,8.359871,-8.747127,3.886310,-8.175755,3.049396,-5.092569,8.617172,5.288395,-7.286964,3.260665,-3.444495,-2.710855,6.412042,-2.733315,-6.866348,5.016601,5.705520,0.478066,-4.492125,-7.684965,6.996016,6.699564,-2.862416,0.837192,9.409333,9.069899,-2.736555,2.673370,2.300116,-0.793405,-3.493910,0.140158,2.406186,-4.403857,-8.019714,7.654226,-4.177322,7.037109,5.697539,7.316637,5.329117,-1.929814,7.329124,7.343997,1.943634,-0.924483,5.346394,6.653100,-6.416237,-1.284609,-0.269562,-8.471403,-0.030998,-6.977455,5.112002,-7.483710,-8.179767,-4.081180,-8.423242,-0.190720,5.651538,-5.616476,-2.383191,7.738165,4.351468,4.129653,6.628691,-1.672304,4.218461,8.475012,7.928005,7.486600,5.818955,7.465884,7.604150,2.687574,-5.923294,6.392616,-0.136004,2.011794,3.102251,4.017049,-3.341326,-7.050598,-1.611584,-4.479604,-1.706616,7.969994,-5.813631,8.260335,-2.868924,-9.885647,-2.192557,7.064087,9.964690,0.173105,-3.702147,5.799508,-7.984929,-3.659148,-5.512310,-5.668323,5.266618,-2.468014,-4.187829,2.301100,-0.170842,2.865386,-1.829623,4.822371,7.410711,-3.043774,-7.636876,4.816180,9.078826,0.099040,-8.068051,-8.877399,-9.689239,6.728660,0.949624,3.815648,0.146652,-0.790346,-5.530986,1.413832,-7.629560,8.975451,6.109524,-9.732769,-7.865238,-8.935279,7.856590,-8.671113,1.182096,5.264056,1.738092,8.605420,3.843384,-6.154295,3.667144,-0.355848,3.075125,-4.639566,-2.053235,0.636147,4.520394,4.919586,8.083831,-9.437712,-5.312034,1.230120,-8.420847,-2.354346,-4.001366,6.792246,-5.254693,-7.481884,5.658472,-3.963200,8.013753,1.873903,-5.481471,9.456896,-8.822380,-7.230800,3.874926,-3.507917,-9.030938,-2.640270,1.554302,7.916499,6.833140,7.402130,-8.162123,-8.384997,-2.670742,-2.204042,-0.150970,-6.303266,2.412498,2.515563,-8.557669,5.019372,-4.871068,9.899487,5.494401,7.772864,-3.563005,-1.071628,4.959447,-6.680799,-0.338712,-6.817748,9.794945,8.462627,8.152881,3.401741,0.267819,9.404053,-7.140327,3.256587,6.580612,-7.177976,-0.785469,-3.285917,3.495298,4.939797,-7.169693,2.631126,-6.960607,-4.237984,2.689106,2.970050,-7.448494,0.831538,9.445625,5.325350,9.895657,0.896316,-7.745494,5.592021,-6.542615,1.628229,-4.801754,-6.202975,3.207178,8.370177,8.612622,0.035165,7.078883,-6.034340,-2.981515,5.305029,-7.905317,6.241973,-2.717649,-0.767771,6.626937,2.325030,-2.839672,-7.769045,4.298927,7.168821,-0.516496,-7.350687,4.166939,-3.180928,-6.869102,0.435932,-0.941726,8.440241,-5.914559,-3.989058,0.336224,3.296286,1.062676,-4.987228,7.674937,6.183044,-6.166605,3.584472,7.891718,3.960179,0.475128,-9.429326,5.959414,0.244626,7.078124,7.119772,2.284401,2.876381,-4.906912,3.966585,3.891804,7.854367,6.334032,2.615388,9.041486,-5.072618,9.813989,-9.441835,8.057894,-2.111251,5.823558,3.645300,4.189650,-7.553081,-7.820862,8.521790,-8.899646,-2.470574,-5.725017,-0.262823,-7.007880,-4.836131,4.364649,8.965512,-8.448215,-3.058973,5.141880,0.017789,-8.980155,4.742499,6.713437,-5.293874,1.041648,6.897326,-8.310629,9.750725,8.079122,-8.931581,0.699623,3.350815,-5.160969,5.766980,7.170576,-0.351355,-6.606602,8.130759,-2.567976,-1.393967,-9.516272,9.905007,9.628857,5.486698,1.739352,-2.051867,1.508740,-3.491758,8.292914,-0.661318,-9.920305,-4.338566,-6.037748,0.284706,7.409790,-9.792754,2.009831,-5.549332,9.308023,3.221134,2.155947,8.262737,7.775314,-5.108378,3.997330,-9.554188,4.426016,3.403102,-9.724710,7.516206,-3.299411,9.452610,1.143503,-7.053999,5.476174,5.979020,5.816816,-7.052214,4.382251,0.201436,4.772405,-5.896540,-3.109286,-1.119591,-1.409730,-1.482859,4.339094,1.260894,9.970015,4.036819,3.990816,-5.355417,2.093382,-6.715346,8.086397,-0.274139,3.477328,-4.738816,-3.275229,-5.904340,-0.587704,8.858890,-5.951937,-0.547586,-6.466590,-7.632526,8.788703,9.401638,0.867798,2.273832,1.373927,7.622213,-8.516331,1.109342,-3.227431,-4.838053,-0.847856,7.911249,-1.160623,5.709769,7.907957,-7.876368,-0.663509,-1.592029,6.944576,-9.869073,5.875276,3.431382,8.464621,-0.659784,-8.329215,-4.507254,-1.085886,0.345478,-9.005137,6.922228,5.870630,-0.924936,5.810758,9.337160,-2.555779,-4.739939,-4.597185,4.609475,-7.118621,0.496791,-3.590115,7.470919,5.309958,7.850173,8.266650,-4.741293,3.006415,-0.553991,3.210335,9.778909,-7.238858,6.741299,-0.893925,-5.301654,-1.423119,0.808470,-3.408490,2.965921,-5.731257,8.078399,7.451804,-2.647222,-8.852184,-9.303017,-9.245364,3.414774,5.433884,2.039628,6.095790,-8.933814,-8.629151,1.144092,-6.455835,-4.907693,7.105020,1.165548,3.265254,0.618495,-7.740330,1.298333,-8.413245,3.881501,6.588425,2.794561,4.239181,-2.566656,1.200923,-0.416756,-9.258827,-9.130719,-8.245211,5.250140,7.107058,7.924197,-8.765798,3.179259,7.224922,-4.380145,2.625367,7.739254,6.642394,-4.401319,1.225803,-2.140615,-2.439175,-6.607067,-4.409604,-5.152529,-4.578438,-0.062112,2.015877,0.696104,-2.363228,4.780203,4.863534,-9.328425,1.136009,-2.972027,1.089621,-1.396915,7.432591,-3.299752,-6.603229,-1.524120,-2.486186,8.473453,-5.203576,-9.832664,-7.341644,-3.622723,7.315197,-2.995647,-9.814835,2.950259,-3.317616,3.368387,-3.581731,5.797711,-0.028035,-7.754870,-5.795748,-8.932077,-8.738073,-1.341478,0.003047,9.416108,6.282982,7.446389,-1.258353,-7.383309,-1.281602,-5.330692,9.638271,-4.758478,5.279185,4.027160,-9.012281,-4.037101,-3.311664,-2.446273,-8.619052,-6.259419,5.950626,8.870857,1.377699,-3.010681,4.678116,-5.749855,8.302129,-4.450779,6.704545,-5.485151,-3.034273,9.039645,2.186385,-7.593707,6.656667,-6.363600,-6.072596,-5.804442,9.404695,5.359309,7.704340,1.869184,-3.097307,-4.067924,0.810839,-6.931157,0.662489,0.293888,1.756932,-8.716795,-3.556804,5.670043,-0.825265,-1.939020,0.848406,-6.291557,-8.462159,6.631572,-2.420357,-9.830389,-1.882274,7.119700,-3.601016,0.210974,-7.592211,-1.558976,-6.954429,5.693125,7.575955,-2.807468,7.820726,-9.257864,-8.286997,7.911556,9.888025,8.048833,-8.459238,5.210664,2.145636,-4.221295,9.585427,-9.872013,-7.454852,-3.170371,-8.024013,-0.033041,-5.791190,3.705087,-9.276911,0.599899,-7.692861,-1.038451,3.325357,-4.178258,-9.580030,-5.816835,9.265763,1.945895,-1.034570,-1.641669,-8.157927,-2.012779,9.450398,2.544397,-8.780779,0.839404,1.029674,1.205999,6.572370,9.283968,-3.677651,9.940096,8.678449,-2.225051,6.684341,-0.744962,5.779597,-8.708331,-2.470245,0.778658,-5.388309,2.934804,-4.190635,-4.634699,-3.153702,6.452559,2.369827,1.569678,1.009275,-1.327878,-3.202204,-1.406204,7.529798,-0.853468,-7.233212,2.797775,-3.785144,2.474297,0.710013,-8.257598,6.925296,0.575446,3.763147,2.503270,-5.509484,7.975508,-4.753092,-7.714274,-9.571942,9.141015,-9.236215,7.757564,-4.767438,9.146593,-7.861390,2.677452,4.293786,-7.445938,5.071861,1.242233,8.024216,-6.138385,-0.392860,8.513280,4.227910,-4.985121,8.161062,-2.853890,-7.008835,-8.231398,-5.257377,-4.758730,-2.029392,-9.338446,0.448242,7.437960,-2.105854,-0.766359,-7.678282,6.837544,1.024866,-7.172184,8.242607,-6.897428,-4.367649,-0.695000,-1.211892,0.686552,4.662190,9.544660,8.737522,6.113763,-4.407811,7.468947,5.565751,4.779919,-6.304215,-3.262931,-7.842672,0.282056,1.281715], dtype = "float64")#candidate|5566|(1386,)|const|float64
call_5565 = relay.TupleGetItem(func_3563_call(relay.reshape(const_5566.astype('float64'), [9, 14, 11])), 0)
call_5567 = relay.TupleGetItem(func_3565_call(relay.reshape(const_5566.astype('float64'), [9, 14, 11])), 0)
func_4247_call = mod.get_global_var('func_4247')
func_4252_call = mutated_mod.get_global_var('func_4252')
var_5577 = relay.var("var_5577", dtype = "float64", shape = ())#candidate|5577|()|var|float64
var_5578 = relay.var("var_5578", dtype = "float64", shape = (1, 12))#candidate|5578|(1, 12)|var|float64
var_5579 = relay.var("var_5579", dtype = "float64", shape = (48,))#candidate|5579|(48,)|var|float64
call_5576 = relay.TupleGetItem(func_4247_call(relay.reshape(var_5577.astype('float64'), []), relay.reshape(var_5578.astype('float64'), [1, 2, 6]), relay.reshape(var_5579.astype('float64'), [4, 2, 6]), ), 0)
call_5580 = relay.TupleGetItem(func_4252_call(relay.reshape(var_5577.astype('float64'), []), relay.reshape(var_5578.astype('float64'), [1, 2, 6]), relay.reshape(var_5579.astype('float64'), [4, 2, 6]), ), 0)
func_5542_call = mod.get_global_var('func_5542')
func_5544_call = mutated_mod.get_global_var('func_5544')
call_5583 = relay.TupleGetItem(func_5542_call(), 0)
call_5584 = relay.TupleGetItem(func_5544_call(), 0)
output = relay.Tuple([call_5555,call_5565,const_5566,call_5576,var_5577,var_5578,var_5579,call_5583,])
output2 = relay.Tuple([call_5556,call_5567,const_5566,call_5580,var_5577,var_5578,var_5579,call_5584,])
func_5589 = relay.Function([var_5577,var_5578,var_5579,], output)
mod['func_5589'] = func_5589
mod = relay.transform.InferType()(mod)
mutated_mod['func_5589'] = func_5589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5589_call = mutated_mod.get_global_var('func_5589')
var_5591 = relay.var("var_5591", dtype = "float64", shape = ())#candidate|5591|()|var|float64
var_5592 = relay.var("var_5592", dtype = "float64", shape = (1, 12))#candidate|5592|(1, 12)|var|float64
var_5593 = relay.var("var_5593", dtype = "float64", shape = (48,))#candidate|5593|(48,)|var|float64
call_5590 = func_5589_call(var_5591,var_5592,var_5593,)
output = call_5590
func_5594 = relay.Function([var_5591,var_5592,var_5593,], output)
mutated_mod['func_5594'] = func_5594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1946_call = mod.get_global_var('func_1946')
func_1947_call = mutated_mod.get_global_var('func_1947')
call_5697 = func_1946_call()
call_5698 = func_1946_call()
func_4298_call = mod.get_global_var('func_4298')
func_4300_call = mutated_mod.get_global_var('func_4300')
call_5702 = relay.TupleGetItem(func_4298_call(), 0)
call_5703 = relay.TupleGetItem(func_4300_call(), 0)
output = relay.Tuple([call_5697,call_5702,])
output2 = relay.Tuple([call_5698,call_5703,])
func_5710 = relay.Function([], output)
mod['func_5710'] = func_5710
mod = relay.transform.InferType()(mod)
mutated_mod['func_5710'] = func_5710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5710_call = mutated_mod.get_global_var('func_5710')
call_5711 = func_5710_call()
output = call_5711
func_5712 = relay.Function([], output)
mutated_mod['func_5712'] = func_5712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3333_call = mod.get_global_var('func_3333')
func_3334_call = mutated_mod.get_global_var('func_3334')
call_5713 = relay.TupleGetItem(func_3333_call(), 0)
call_5714 = relay.TupleGetItem(func_3334_call(), 0)
func_232_call = mod.get_global_var('func_232')
func_235_call = mutated_mod.get_global_var('func_235')
const_5728 = relay.const(-4.204386, dtype = "float32")#candidate|5728|()|const|float32
var_5729 = relay.var("var_5729", dtype = "float32", shape = (256,))#candidate|5729|(256,)|var|float32
call_5727 = func_232_call(relay.reshape(const_5728.astype('float32'), []), relay.reshape(var_5729.astype('float32'), [16, 2, 8]), )
call_5730 = func_232_call(relay.reshape(const_5728.astype('float32'), []), relay.reshape(var_5729.astype('float32'), [16, 2, 8]), )
output = relay.Tuple([call_5713,call_5727,const_5728,var_5729,])
output2 = relay.Tuple([call_5714,call_5730,const_5728,var_5729,])
func_5740 = relay.Function([var_5729,], output)
mod['func_5740'] = func_5740
mod = relay.transform.InferType()(mod)
mutated_mod['func_5740'] = func_5740
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5741 = relay.var("var_5741", dtype = "float32", shape = (256,))#candidate|5741|(256,)|var|float32
func_5740_call = mutated_mod.get_global_var('func_5740')
call_5742 = func_5740_call(var_5741)
output = call_5742
func_5743 = relay.Function([var_5741], output)
mutated_mod['func_5743'] = func_5743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_5787 = func_2385_call()
call_5788 = func_2385_call()
output = call_5787
output2 = call_5788
func_5792 = relay.Function([], output)
mod['func_5792'] = func_5792
mod = relay.transform.InferType()(mod)
mutated_mod['func_5792'] = func_5792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5792_call = mutated_mod.get_global_var('func_5792')
call_5793 = func_5792_call()
output = call_5793
func_5794 = relay.Function([], output)
mutated_mod['func_5794'] = func_5794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2491_call = mod.get_global_var('func_2491')
func_2492_call = mutated_mod.get_global_var('func_2492')
call_5803 = relay.TupleGetItem(func_2491_call(), 0)
call_5804 = relay.TupleGetItem(func_2492_call(), 0)
output = call_5803
output2 = call_5804
func_5820 = relay.Function([], output)
mod['func_5820'] = func_5820
mod = relay.transform.InferType()(mod)
output = func_5820()
func_5821 = relay.Function([], output)
mutated_mod['func_5821'] = func_5821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4806_call = mod.get_global_var('func_4806')
func_4807_call = mutated_mod.get_global_var('func_4807')
call_5825 = func_4806_call()
call_5826 = func_4806_call()
func_3391_call = mod.get_global_var('func_3391')
func_3393_call = mutated_mod.get_global_var('func_3393')
call_5837 = func_3391_call()
call_5838 = func_3391_call()
func_3819_call = mod.get_global_var('func_3819')
func_3820_call = mutated_mod.get_global_var('func_3820')
call_5877 = relay.TupleGetItem(func_3819_call(), 0)
call_5878 = relay.TupleGetItem(func_3820_call(), 0)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_5901 = func_1698_call()
call_5902 = func_1698_call()
func_4906_call = mod.get_global_var('func_4906')
func_4907_call = mutated_mod.get_global_var('func_4907')
call_5903 = relay.TupleGetItem(func_4906_call(), 0)
call_5904 = relay.TupleGetItem(func_4907_call(), 0)
output = relay.Tuple([call_5825,call_5837,call_5877,call_5901,call_5903,])
output2 = relay.Tuple([call_5826,call_5838,call_5878,call_5902,call_5904,])
func_5911 = relay.Function([], output)
mod['func_5911'] = func_5911
mod = relay.transform.InferType()(mod)
mutated_mod['func_5911'] = func_5911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5911_call = mutated_mod.get_global_var('func_5911')
call_5912 = func_5911_call()
output = call_5912
func_5913 = relay.Function([], output)
mutated_mod['func_5913'] = func_5913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4959_call = mod.get_global_var('func_4959')
func_4960_call = mutated_mod.get_global_var('func_4960')
call_5926 = relay.TupleGetItem(func_4959_call(), 0)
call_5927 = relay.TupleGetItem(func_4960_call(), 0)
output = call_5926
output2 = call_5927
func_5933 = relay.Function([], output)
mod['func_5933'] = func_5933
mod = relay.transform.InferType()(mod)
mutated_mod['func_5933'] = func_5933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5933_call = mutated_mod.get_global_var('func_5933')
call_5934 = func_5933_call()
output = call_5934
func_5935 = relay.Function([], output)
mutated_mod['func_5935'] = func_5935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5020_call = mod.get_global_var('func_5020')
func_5021_call = mutated_mod.get_global_var('func_5021')
call_5957 = relay.TupleGetItem(func_5020_call(), 0)
call_5958 = relay.TupleGetItem(func_5021_call(), 0)
const_5963 = relay.const([[[1,2,5,-6],[4,-4,3,-4],[10,-8,-6,6],[-2,6,5,1],[4,-7,-9,-8],[2,5,1,6],[7,6,-3,-7],[-3,6,8,3],[-1,9,-1,10],[10,3,-3,3],[-7,3,3,6],[2,-1,-9,2],[-5,9,9,1],[5,1,5,7],[-2,1,-2,-1],[-8,5,-9,9]],[[-8,-9,-8,-6],[-6,-10,-10,-2],[-9,10,-9,8],[-5,9,9,-5],[-8,6,5,-8],[1,-2,7,7],[-7,1,-10,-7],[1,-9,6,9],[-8,-2,9,6],[10,-4,9,6],[10,4,-4,7],[5,-6,-1,4],[2,-4,8,4],[5,-4,9,2],[7,9,5,7],[-3,-2,1,-4]]], dtype = "uint64")#candidate|5963|(2, 16, 4)|const|uint64
bop_5964 = relay.logical_xor(call_5957.astype('uint32'), relay.reshape(const_5963.astype('uint32'), relay.shape_of(call_5957))) # shape=(2, 16, 4)
bop_5967 = relay.logical_xor(call_5958.astype('uint32'), relay.reshape(const_5963.astype('uint32'), relay.shape_of(call_5958))) # shape=(2, 16, 4)
output = bop_5964
output2 = bop_5967
func_5972 = relay.Function([], output)
mod['func_5972'] = func_5972
mod = relay.transform.InferType()(mod)
mutated_mod['func_5972'] = func_5972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5972_call = mutated_mod.get_global_var('func_5972')
call_5973 = func_5972_call()
output = call_5973
func_5974 = relay.Function([], output)
mutated_mod['func_5974'] = func_5974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3819_call = mod.get_global_var('func_3819')
func_3820_call = mutated_mod.get_global_var('func_3820')
call_6043 = relay.TupleGetItem(func_3819_call(), 0)
call_6044 = relay.TupleGetItem(func_3820_call(), 0)
uop_6072 = relay.exp(call_6043.astype('float64')) # shape=(2, 16, 4)
uop_6074 = relay.exp(call_6044.astype('float64')) # shape=(2, 16, 4)
func_3503_call = mod.get_global_var('func_3503')
func_3506_call = mutated_mod.get_global_var('func_3506')
const_6076 = relay.const([9.976725,6.373364,8.056709,6.958994,5.814547,0.640044,-7.491323,-5.532233,-5.530816,-5.475617,3.909896,1.491954,-2.940730,-9.276635,9.251012,0.188984,2.158404,-6.699827,-8.277739,1.892635,-8.411741,-7.468334,3.592300,5.473263,6.094709,6.791363,2.298165,8.501887,1.447313,4.411548,4.267842,-7.865161,6.185125,0.243773,-7.405766,2.907717,0.151969,2.561150,-3.166134,-0.655635,-5.379803,6.813835,-5.609247,-0.184058,-7.085587,5.512254,-2.773896,-3.261886,-9.098582,2.898368,8.094216,3.781943,-0.642563,1.763210,2.485341,6.397421,-0.180548,-0.923502,9.063218,-4.006304,-9.538962,0.243390,5.993218,2.555924,3.004254,1.997897,6.550171,-1.315118,3.173102,9.634500,0.232094,6.949921,5.756905,9.476260,-5.410594,-3.131830,2.680525,4.431160,6.407806,-9.327333,6.715351,9.050475,6.598610,0.953844,-6.149501,5.441684,2.001726,2.101197,-4.754369,3.173686,-7.167186,-7.234232,-2.579078,5.017282,-6.967191,-5.296458,4.029541,-1.515039,1.117923,7.049507,-6.702447,-8.693740,2.011985,-1.533948,-7.333572,-2.243023,5.413898,-7.496117,-6.465672,-1.600601,8.332791,5.921737,-8.112847,0.053830,5.098508,6.558208,-5.078751,6.731836,4.975436,2.513328,1.117276,4.595249,-3.030343,-8.111932,4.687830,2.201776,-1.425695,8.022259,9.027210,-5.428130,2.935131,-7.274052,0.572097,-4.452054,-4.548287,-9.182537,5.066219,-6.530795,9.792365,4.771840,7.129055,-5.258538,8.409784,0.681298,-5.755842,7.736157,4.761076,6.073072,0.768185,-9.539062,-3.329417,3.473131,-1.941675,4.762814,7.956067,-2.535867,-0.515448,-3.927757,-7.059035,-0.963646,5.339980,-4.493652,6.430622,-3.052659,1.106081,-6.246014,3.924946,-2.031923,-1.082895,-5.252233,-0.450854,-4.425978,7.215443,-2.409198,-0.756124,-2.663530,-4.322027,0.326506,4.393400,-7.703298,-4.343406,-9.212310,-4.886799,1.719373,-1.266353,-3.619246,-7.320521,4.547288,8.359427,9.857164,-0.161494,-6.184182,-8.010923,7.681782,8.161441,7.961737,-1.635189,2.596691,-9.395802,6.096954,-2.226470,7.186732,1.702943,-0.411353,-3.449781,-9.388950,-6.670413,1.810647,-9.370412,-8.199194,-8.050576,9.759885,6.409893,8.180314,8.787230,-9.436423,8.843580,-4.452444,7.609740,5.977830,-3.480697,-8.892348,-4.426482,-3.345784,-0.750286,-7.049224,-0.869505,-0.399150,6.199886,1.956386,-9.897863,-0.177406,4.966887,-0.576993,-3.129524,-6.995778,-1.767396,8.271756,-6.882875,1.055750,-2.543302,4.891144,-0.719893,-5.892733,1.444112,-0.430215,1.777570,1.608964,-9.985875,3.425045,-3.851744,3.203910,6.543852,8.313801,-8.353621,-2.168972,4.685602,1.678838,7.610543,1.868159,1.545891,5.018984,-4.431836,4.595711,-4.216706,6.657456,-6.951365,8.699983,1.514219,7.193753,-1.159748,-4.373954,5.646484,4.263466,6.431195,-3.742920,-5.048183,-7.769064,-4.052150,4.272219,-1.554742,3.642840,-5.769533,-6.959968,-1.593293,6.498040,-0.460836,-6.255546,-5.535077,-2.140132,-7.867237,-3.724443,-4.594306,9.539009,8.101824,-0.208414,-5.668909,-0.674004,-3.496397,-8.613629,7.069181,9.246720,-2.806157,0.733368,4.909440,-8.393250,-3.711937,6.942684,4.737790,-4.307093,7.055129,3.465549,-2.889770,-3.611734,-7.261211,2.255210,5.994673,5.955317,-9.434808,-4.504178,9.591325,4.307217,7.163029,-1.553799,-6.820292,6.697564,1.951851,3.647787,6.508148,9.239131,-0.425528,2.347652,5.050215,1.598919,8.965211,-7.952785,8.510874,3.921809,-2.149374,2.402677,-2.382013,-8.492363,4.915426,1.526595,-0.084107,3.179522,-7.460043,-4.472898,3.558829,6.472501,4.778564,1.194537,-3.057408,0.618731,6.590600,9.936637,-2.816706,0.868812,3.686855,-6.072606], dtype = "float64")#candidate|6076|(360,)|const|float64
call_6075 = relay.TupleGetItem(func_3503_call(relay.reshape(const_6076.astype('float64'), [4, 10, 9])), 4)
call_6077 = relay.TupleGetItem(func_3506_call(relay.reshape(const_6076.astype('float64'), [4, 10, 9])), 4)
func_5206_call = mod.get_global_var('func_5206')
func_5208_call = mutated_mod.get_global_var('func_5208')
call_6090 = relay.TupleGetItem(func_5206_call(), 0)
call_6091 = relay.TupleGetItem(func_5208_call(), 0)
output = relay.Tuple([uop_6072,call_6075,const_6076,call_6090,])
output2 = relay.Tuple([uop_6074,call_6077,const_6076,call_6091,])
func_6096 = relay.Function([], output)
mod['func_6096'] = func_6096
mod = relay.transform.InferType()(mod)
mutated_mod['func_6096'] = func_6096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6096_call = mutated_mod.get_global_var('func_6096')
call_6097 = func_6096_call()
output = call_6097
func_6098 = relay.Function([], output)
mutated_mod['func_6098'] = func_6098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mod.get_global_var('func_4158')
func_4160_call = mutated_mod.get_global_var('func_4160')
call_6118 = relay.TupleGetItem(func_4158_call(), 0)
call_6119 = relay.TupleGetItem(func_4160_call(), 0)
func_4562_call = mod.get_global_var('func_4562')
func_4565_call = mutated_mod.get_global_var('func_4565')
const_6121 = relay.const([[-2.633996],[-9.969702],[-2.486679],[7.675688],[0.502212],[-3.241077],[-3.775968],[-0.800045],[-7.641859],[5.025121],[-8.011643],[5.668348],[-3.757911],[-6.678621],[3.740071],[2.034763],[4.497942],[8.390733],[0.354259],[7.765124],[-5.797091],[-8.289717],[-0.915995],[-5.520185],[-3.641293],[-5.267433],[-4.141099],[7.393723],[6.352070],[1.541471],[-4.840123],[-3.232481],[5.643299],[9.818770],[-6.230238],[2.070241],[-0.740037],[2.677116],[3.882069],[-5.231738],[7.603565],[-6.233297],[-6.067580],[-0.315552],[-0.475120],[-9.320730],[-7.548987],[-0.568540],[-4.081568],[7.213412],[3.153410],[2.642230],[-6.424758],[-9.347565],[-4.363848],[0.616085],[-0.425707],[-3.741199],[4.003162],[-5.386391],[-5.202164],[-3.215386],[3.572822],[-7.668840],[-4.954093],[-5.129612],[3.028751],[-1.939799],[-3.575191],[8.922270],[4.401534],[-3.637088],[-0.655121],[-3.759430],[2.252455],[0.730579],[0.993520],[4.175828],[3.230213],[-7.326125],[2.295911],[6.691353],[-3.912002],[-8.776634],[-2.999214],[-0.391259],[-5.914878],[0.543310],[2.760205],[-2.047596],[-3.588506],[-6.332076],[1.324622],[-8.842221],[-9.953144],[-1.614844],[8.781141],[-6.221998],[2.619052],[-7.544890],[-5.279579],[7.874973],[7.620841],[1.098931],[-8.937209],[-3.687903],[-9.973691],[-2.990973],[-2.543189],[-7.220037],[1.554523],[-0.800264],[-3.370150],[6.218936],[0.456315],[0.607356],[-5.604915],[-0.670313],[-3.620041],[-1.758551],[2.809142],[8.639602],[0.219517],[7.067451],[7.883244],[-4.980484],[-3.631095],[3.341785],[7.735084],[2.572833],[0.377547],[-2.129216],[8.649324],[1.033594],[4.345639],[6.645625],[-2.117740],[-6.137743],[-1.977583],[8.815100],[8.980611],[9.163337],[-0.875242],[-8.159103],[9.826185],[-7.382192],[-2.374826],[-2.932152],[9.599687],[3.682136],[0.995193],[3.382242],[-0.345540],[2.331350],[7.719202],[-5.975757],[1.658592],[6.745510],[-9.184594],[7.411948],[6.299030],[-4.723533],[2.501422],[1.292013],[8.555164],[2.908606],[7.466829],[-6.744151],[-5.837068],[5.891704],[5.396380],[-0.449127],[5.422235],[-6.034340],[2.288391],[3.003120],[-7.268311],[-0.768867],[-1.052944],[-6.282801],[5.039104],[-0.693823],[4.134995],[-8.583228],[-2.261142],[0.955492],[8.710713],[-6.969865],[5.945411],[-2.626107],[7.521974],[1.811939],[-7.565298],[6.100721],[-6.051429],[-8.741235],[0.735264],[-5.394738],[1.672269],[-5.614498],[-6.929490],[5.573079],[7.876881],[-4.133443],[0.951540],[4.405733],[-1.686869],[-5.973659],[-6.760120],[3.570761],[3.219130],[-7.923476],[-5.650883],[4.087982],[6.640591],[-1.701992],[-4.482160],[2.603463],[3.472869],[-2.389407],[5.237090],[2.751595],[5.156240],[-5.764437],[1.259461],[-9.607246],[4.027026],[7.452510],[0.999921],[2.625483],[-3.448349],[4.056698],[-8.598128],[-8.148226],[-5.571857],[-8.968634],[-4.143431],[-8.035158],[5.629984],[-4.034387],[-4.833501],[6.010915],[2.264074],[-6.650197],[-3.276168],[-9.020369],[9.582683],[6.135315],[-3.885620],[0.042853],[-1.931416],[-4.505944],[-0.681032],[-0.014731],[9.585538],[-1.706067]], dtype = "float32")#candidate|6121|(256, 1)|const|float32
call_6120 = relay.TupleGetItem(func_4562_call(relay.reshape(const_6121.astype('float32'), [256,])), 3)
call_6122 = relay.TupleGetItem(func_4565_call(relay.reshape(const_6121.astype('float32'), [256,])), 3)
var_6124 = relay.var("var_6124", dtype = "float32", shape = (256, 9))#candidate|6124|(256, 9)|var|float32
bop_6125 = relay.floor_mod(const_6121.astype('float32'), var_6124.astype('float32')) # shape=(256, 9)
output = relay.Tuple([call_6118,call_6120,bop_6125,])
output2 = relay.Tuple([call_6119,call_6122,bop_6125,])
func_6130 = relay.Function([var_6124,], output)
mod['func_6130'] = func_6130
mod = relay.transform.InferType()(mod)
mutated_mod['func_6130'] = func_6130
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6131 = relay.var("var_6131", dtype = "float32", shape = (256, 9))#candidate|6131|(256, 9)|var|float32
func_6130_call = mutated_mod.get_global_var('func_6130')
call_6132 = func_6130_call(var_6131)
output = call_6132
func_6133 = relay.Function([var_6131], output)
mutated_mod['func_6133'] = func_6133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2733_call = mod.get_global_var('func_2733')
func_2734_call = mutated_mod.get_global_var('func_2734')
call_6150 = relay.TupleGetItem(func_2733_call(), 0)
call_6151 = relay.TupleGetItem(func_2734_call(), 0)
output = call_6150
output2 = call_6151
func_6154 = relay.Function([], output)
mod['func_6154'] = func_6154
mod = relay.transform.InferType()(mod)
mutated_mod['func_6154'] = func_6154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mutated_mod.get_global_var('func_6154')
call_6155 = func_6154_call()
output = call_6155
func_6156 = relay.Function([], output)
mutated_mod['func_6156'] = func_6156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4978_call = mod.get_global_var('func_4978')
func_4980_call = mutated_mod.get_global_var('func_4980')
call_6171 = relay.TupleGetItem(func_4978_call(), 1)
call_6172 = relay.TupleGetItem(func_4980_call(), 1)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_6180 = func_1698_call()
call_6181 = func_1698_call()
func_4158_call = mod.get_global_var('func_4158')
func_4160_call = mutated_mod.get_global_var('func_4160')
call_6196 = relay.TupleGetItem(func_4158_call(), 0)
call_6197 = relay.TupleGetItem(func_4160_call(), 0)
output = relay.Tuple([call_6171,call_6180,call_6196,])
output2 = relay.Tuple([call_6172,call_6181,call_6197,])
func_6199 = relay.Function([], output)
mod['func_6199'] = func_6199
mod = relay.transform.InferType()(mod)
mutated_mod['func_6199'] = func_6199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6199_call = mutated_mod.get_global_var('func_6199')
call_6200 = func_6199_call()
output = call_6200
func_6201 = relay.Function([], output)
mutated_mod['func_6201'] = func_6201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5972_call = mod.get_global_var('func_5972')
func_5974_call = mutated_mod.get_global_var('func_5974')
call_6244 = func_5972_call()
call_6245 = func_5972_call()
func_3391_call = mod.get_global_var('func_3391')
func_3393_call = mutated_mod.get_global_var('func_3393')
call_6254 = func_3391_call()
call_6255 = func_3391_call()
output = relay.Tuple([call_6244,call_6254,])
output2 = relay.Tuple([call_6245,call_6255,])
func_6259 = relay.Function([], output)
mod['func_6259'] = func_6259
mod = relay.transform.InferType()(mod)
output = func_6259()
func_6260 = relay.Function([], output)
mutated_mod['func_6260'] = func_6260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6199_call = mod.get_global_var('func_6199')
func_6201_call = mutated_mod.get_global_var('func_6201')
call_6261 = relay.TupleGetItem(func_6199_call(), 1)
call_6262 = relay.TupleGetItem(func_6201_call(), 1)
output = relay.Tuple([call_6261,])
output2 = relay.Tuple([call_6262,])
func_6271 = relay.Function([], output)
mod['func_6271'] = func_6271
mod = relay.transform.InferType()(mod)
mutated_mod['func_6271'] = func_6271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6271_call = mutated_mod.get_global_var('func_6271')
call_6272 = func_6271_call()
output = call_6272
func_6273 = relay.Function([], output)
mutated_mod['func_6273'] = func_6273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_6345 = relay.TupleGetItem(func_1653_call(), 0)
call_6346 = relay.TupleGetItem(func_1655_call(), 0)
func_5020_call = mod.get_global_var('func_5020')
func_5021_call = mutated_mod.get_global_var('func_5021')
call_6350 = relay.TupleGetItem(func_5020_call(), 0)
call_6351 = relay.TupleGetItem(func_5021_call(), 0)
func_4529_call = mod.get_global_var('func_4529')
func_4533_call = mutated_mod.get_global_var('func_4533')
var_6364 = relay.var("var_6364", dtype = "float64", shape = (2025,))#candidate|6364|(2025,)|var|float64
call_6363 = relay.TupleGetItem(func_4529_call(relay.reshape(var_6364.astype('float64'), [2025,]), relay.reshape(var_6364.astype('float64'), [2025,]), ), 0)
call_6365 = relay.TupleGetItem(func_4533_call(relay.reshape(var_6364.astype('float64'), [2025,]), relay.reshape(var_6364.astype('float64'), [2025,]), ), 0)
func_5129_call = mod.get_global_var('func_5129')
func_5131_call = mutated_mod.get_global_var('func_5131')
call_6402 = relay.TupleGetItem(func_5129_call(), 0)
call_6403 = relay.TupleGetItem(func_5131_call(), 0)
func_5710_call = mod.get_global_var('func_5710')
func_5712_call = mutated_mod.get_global_var('func_5712')
call_6420 = relay.TupleGetItem(func_5710_call(), 1)
call_6421 = relay.TupleGetItem(func_5712_call(), 1)
output = relay.Tuple([call_6345,call_6350,call_6363,var_6364,call_6402,call_6420,])
output2 = relay.Tuple([call_6346,call_6351,call_6365,var_6364,call_6403,call_6421,])
func_6424 = relay.Function([var_6364,], output)
mod['func_6424'] = func_6424
mod = relay.transform.InferType()(mod)
mutated_mod['func_6424'] = func_6424
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6425 = relay.var("var_6425", dtype = "float64", shape = (2025,))#candidate|6425|(2025,)|var|float64
func_6424_call = mutated_mod.get_global_var('func_6424')
call_6426 = func_6424_call(var_6425)
output = call_6426
func_6427 = relay.Function([var_6425], output)
mutated_mod['func_6427'] = func_6427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5308_call = mod.get_global_var('func_5308')
func_5310_call = mutated_mod.get_global_var('func_5310')
call_6434 = relay.TupleGetItem(func_5308_call(), 0)
call_6435 = relay.TupleGetItem(func_5310_call(), 0)
func_5020_call = mod.get_global_var('func_5020')
func_5021_call = mutated_mod.get_global_var('func_5021')
call_6464 = relay.TupleGetItem(func_5020_call(), 0)
call_6465 = relay.TupleGetItem(func_5021_call(), 0)
func_3671_call = mod.get_global_var('func_3671')
func_3673_call = mutated_mod.get_global_var('func_3673')
var_6505 = relay.var("var_6505", dtype = "float64", shape = (9, 225))#candidate|6505|(9, 225)|var|float64
call_6504 = relay.TupleGetItem(func_3671_call(relay.reshape(var_6505.astype('float64'), [1, 2025])), 0)
call_6506 = relay.TupleGetItem(func_3673_call(relay.reshape(var_6505.astype('float64'), [1, 2025])), 0)
func_2912_call = mod.get_global_var('func_2912')
func_2915_call = mutated_mod.get_global_var('func_2915')
const_6513 = relay.const([[-7,6,-9,3,6,-2,-6,-1,-4,5,2,8,-4,9,-4,-2,-9,1,5,-4,9,-6,-8,6,-3,-9,-3,-3,5,-10,2,-2,-2,-8,10,10,2,6,2,2,-1,10,-8,-2,4,4,3,4,-8,4,8,7,9,10,5,7,-2,1,-10,3,-4,8,10,3,-8,-7,-1,8,8,-3,1,1,7,-3,5,-10,2,4,-4,1,-6,-8,-5,-8],[6,7,1,1,10,-6,-10,1,6,4,-6,10,5,10,-8,-2,10,-2,-7,-1,-8,9,-3,10,10,7,-10,8,9,-5,8,1,-7,1,7,9,8,3,-10,3,8,-8,9,2,-5,4,4,-1,10,3,3,7,1,5,5,-1,-7,9,-4,5,10,3,7,-7,4,-8,-1,2,-5,3,-6,2,3,1,-6,9,6,-2,-3,-1,8,-8,4,-2],[7,-8,-2,-6,4,4,-4,8,4,2,-10,8,4,-8,6,-5,7,-7,8,6,1,-3,-5,-4,10,10,-10,-9,-4,1,1,6,3,-9,-7,2,4,-2,6,-2,1,-8,10,-5,6,-6,-4,-3,4,-6,6,8,3,3,-5,6,4,-8,1,9,-9,-2,-7,-8,8,1,-3,-6,-10,-6,3,-2,-5,-1,4,-4,7,4,3,-5,9,7,-7,-10],[1,4,9,-2,6,3,-5,3,-4,-6,-10,-10,-6,-2,-9,4,8,5,-3,4,-10,9,3,-7,-8,6,3,10,-2,-6,5,-4,-5,-2,5,8,-4,-5,1,-6,5,1,-7,-1,3,3,-7,-3,-5,3,-3,-9,9,4,4,-1,3,10,2,10,-9,3,9,8,-3,3,-3,-2,4,4,-9,10,-8,-1,-2,-6,-5,6,-7,5,-9,-7,-1,-5],[-9,5,-6,8,-5,-4,2,-9,1,1,4,-9,4,-3,6,-10,-1,-1,-9,-10,-7,-3,-6,-8,-8,6,-4,-2,2,-3,-7,1,9,-4,-10,5,1,-10,10,6,6,-9,9,-7,1,9,-5,4,4,-4,-2,-6,9,-10,4,9,9,8,-1,1,7,8,4,-7,1,7,-2,-6,10,2,-3,-4,10,4,-1,5,-7,-1,6,3,1,1,-2,-6]], dtype = "uint8")#candidate|6513|(5, 84)|const|uint8
call_6512 = relay.TupleGetItem(func_2912_call(relay.reshape(const_6513.astype('uint8'), [14, 15, 2])), 1)
call_6514 = relay.TupleGetItem(func_2915_call(relay.reshape(const_6513.astype('uint8'), [14, 15, 2])), 1)
output = relay.Tuple([call_6434,call_6464,call_6504,var_6505,call_6512,const_6513,])
output2 = relay.Tuple([call_6435,call_6465,call_6506,var_6505,call_6514,const_6513,])
func_6520 = relay.Function([var_6505,], output)
mod['func_6520'] = func_6520
mod = relay.transform.InferType()(mod)
var_6521 = relay.var("var_6521", dtype = "float64", shape = (9, 225))#candidate|6521|(9, 225)|var|float64
output = func_6520(var_6521)
func_6522 = relay.Function([var_6521], output)
mutated_mod['func_6522'] = func_6522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_6537 = relay.TupleGetItem(func_2816_call(), 2)
call_6538 = relay.TupleGetItem(func_2818_call(), 2)
func_3803_call = mod.get_global_var('func_3803')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_6564 = func_3803_call()
call_6565 = func_3803_call()
output = relay.Tuple([call_6537,call_6564,])
output2 = relay.Tuple([call_6538,call_6565,])
func_6573 = relay.Function([], output)
mod['func_6573'] = func_6573
mod = relay.transform.InferType()(mod)
output = func_6573()
func_6574 = relay.Function([], output)
mutated_mod['func_6574'] = func_6574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4287_call = mod.get_global_var('func_4287')
func_4288_call = mutated_mod.get_global_var('func_4288')
call_6575 = relay.TupleGetItem(func_4287_call(), 1)
call_6576 = relay.TupleGetItem(func_4288_call(), 1)
output = relay.Tuple([call_6575,])
output2 = relay.Tuple([call_6576,])
func_6577 = relay.Function([], output)
mod['func_6577'] = func_6577
mod = relay.transform.InferType()(mod)
output = func_6577()
func_6578 = relay.Function([], output)
mutated_mod['func_6578'] = func_6578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4045_call = mod.get_global_var('func_4045')
func_4047_call = mutated_mod.get_global_var('func_4047')
call_6579 = func_4045_call()
call_6580 = func_4045_call()
output = call_6579
output2 = call_6580
func_6581 = relay.Function([], output)
mod['func_6581'] = func_6581
mod = relay.transform.InferType()(mod)
output = func_6581()
func_6582 = relay.Function([], output)
mutated_mod['func_6582'] = func_6582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4978_call = mod.get_global_var('func_4978')
func_4980_call = mutated_mod.get_global_var('func_4980')
call_6583 = relay.TupleGetItem(func_4978_call(), 1)
call_6584 = relay.TupleGetItem(func_4980_call(), 1)
func_5589_call = mod.get_global_var('func_5589')
func_5594_call = mutated_mod.get_global_var('func_5594')
const_6605 = relay.const(-8.258887, dtype = "float64")#candidate|6605|()|const|float64
var_6606 = relay.var("var_6606", dtype = "float64", shape = (12,))#candidate|6606|(12,)|var|float64
var_6607 = relay.var("var_6607", dtype = "float64", shape = (48,))#candidate|6607|(48,)|var|float64
call_6604 = relay.TupleGetItem(func_5589_call(relay.reshape(const_6605.astype('float64'), []), relay.reshape(var_6606.astype('float64'), [1, 12]), relay.reshape(var_6607.astype('float64'), [48,]), ), 6)
call_6608 = relay.TupleGetItem(func_5594_call(relay.reshape(const_6605.astype('float64'), []), relay.reshape(var_6606.astype('float64'), [1, 12]), relay.reshape(var_6607.astype('float64'), [48,]), ), 6)
func_1010_call = mod.get_global_var('func_1010')
func_1014_call = mutated_mod.get_global_var('func_1014')
const_6611 = relay.const([8.646868,-7.754487,1.949302,0.506831,1.413156,6.330887,6.916495,-3.959106,-5.671344,-7.382983,-2.655077,5.849023,5.836073,-7.947813,-0.568831,-0.820989,7.925630,-2.982051,-0.597103,-2.619379,-8.525001,4.140578,-8.039499,-5.708679,-8.089671,-2.014709,3.528524,3.919130,8.548614,9.043397,0.447807,-8.781441,0.727506,0.482076,-0.697719,2.470952,-0.375480,-4.227160,-3.765324,4.962593,5.760281,5.188398,8.313671,7.939427,-5.867769,-9.340899,5.334136,-0.123913,2.363763,-8.389252,1.009247,0.689996,-6.274331,-6.890413,-7.221488,-3.108258,-3.498683,-0.811360,-4.591934,-4.822655,2.464195,0.424713,7.359014,7.000967,3.497110,1.772075,0.911157,-6.985411,-5.412139,-9.207839,-2.703508,0.422052,-2.034198,3.486057,4.589003,8.708659,-3.150792,7.478702,3.744041,6.559711,-5.684935,4.869568,6.483818,-4.850520,7.801033,-3.372008,7.882570,-2.161272,-0.357643,-9.893085,4.653152,-7.172825,-7.535935,-4.178107,-7.460604,6.994512,-8.186209,-4.120734,-2.748834,3.211923,0.343995,-6.060863,3.645116,-0.098890,-5.587492,-2.416309,-3.576450,1.652676,-7.469372,-7.097267,4.091291,-2.870688,0.692853,1.435504,5.705993,1.582938,3.802325,3.834580,-2.545276,-0.012647,-4.662963,-9.973352,9.905574,-2.126410,0.782755,-8.944286,-2.794423,-9.752213,0.607289,6.654308,1.909672,3.302764,-9.263575,1.647651,-2.490558,5.486345,-9.238311,3.865615,-4.058051,-4.346728,6.057349,-1.543258,0.282035,1.016743,2.021170,3.229631,5.862734,3.737740,8.946843,-6.785196,-0.640531,-9.476142,8.236851,-0.931289,6.845764,-3.947799,4.874504,-0.547141,9.667336,4.312051,6.938245,5.792072,6.978104,-7.410744,-4.749531,-0.692558,6.101993,4.334107,-7.201289,-2.803568,-4.985914,-8.977131,3.904855,-9.067977,-6.870847,8.991178,-8.734380,-9.979010,8.273177,-9.845246,3.300832,-4.911549,-9.825082,-6.004031,6.695210,-4.744613,5.567141,9.321095,-1.657062,1.088981,8.382952,-1.157109,-2.875348,0.155549,3.606433,8.897159,-3.916728,4.054910,1.557752,-9.097794,-4.112585,8.310077,4.533366,6.530682,-9.506234,5.615353,6.745463,-2.505741,-0.918985,-1.636433,0.631748,6.682895,4.755467,-7.655360,-9.386166,-2.191659,-4.578365,-1.578823,-3.703203,1.406261,-7.573711,1.864649,-0.750506,7.205059,2.414003,-8.903757,1.089982,9.865908,7.645779,-4.466953,-7.094972,-4.470095,-3.939567,-3.238199,-9.718894,9.259966,-8.531787,4.164580,-2.703109,-5.293881,-1.165849,0.228940,-9.223879,-3.876420,-5.852489,1.598613,9.695975,5.158968,-3.824689,0.409688,1.987670,0.667983,6.217334,-0.681226,-7.971707,9.350306,-4.192334,-4.734671,4.230869,-8.936104,9.279036,-4.857923,5.442841,-2.888525,-3.172988,5.941176,3.801837,8.296614,1.851775,-0.530296,-2.700538,-6.534615,-5.468266,2.270090,9.350008,-9.189817,5.755819,-3.952497,-8.139096,-1.412037,-5.522996,2.769854,8.439990,-2.643366,-9.191037,-4.528153,-9.049701,1.144576,1.984580,3.559406,-7.063549,-3.807609,-1.650602,9.833108,3.460343,9.438978,7.539805,0.986892,-3.689753,6.404787,4.743615,0.842733,-8.882567,-6.264998,-6.516194,-4.465158,4.212172,-7.114814,2.882605,7.422286,-8.768845,-7.672398,1.652750,-3.400593,5.149529], dtype = "float32")#candidate|6611|(315,)|const|float32
call_6610 = func_1010_call(relay.reshape(const_6611.astype('float32'), [7, 15, 3]), relay.reshape(const_6611.astype('float32'), [7, 15, 3]), )
call_6612 = func_1010_call(relay.reshape(const_6611.astype('float32'), [7, 15, 3]), relay.reshape(const_6611.astype('float32'), [7, 15, 3]), )
output = relay.Tuple([call_6583,call_6604,const_6605,var_6606,var_6607,call_6610,const_6611,])
output2 = relay.Tuple([call_6584,call_6608,const_6605,var_6606,var_6607,call_6612,const_6611,])
func_6615 = relay.Function([var_6606,var_6607,], output)
mod['func_6615'] = func_6615
mod = relay.transform.InferType()(mod)
mutated_mod['func_6615'] = func_6615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6615_call = mutated_mod.get_global_var('func_6615')
var_6617 = relay.var("var_6617", dtype = "float64", shape = (12,))#candidate|6617|(12,)|var|float64
var_6618 = relay.var("var_6618", dtype = "float64", shape = (48,))#candidate|6618|(48,)|var|float64
call_6616 = func_6615_call(var_6617,var_6618,)
output = call_6616
func_6619 = relay.Function([var_6617,var_6618,], output)
mutated_mod['func_6619'] = func_6619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5820_call = mod.get_global_var('func_5820')
func_5821_call = mutated_mod.get_global_var('func_5821')
call_6631 = func_5820_call()
call_6632 = func_5820_call()
output = relay.Tuple([call_6631,])
output2 = relay.Tuple([call_6632,])
func_6653 = relay.Function([], output)
mod['func_6653'] = func_6653
mod = relay.transform.InferType()(mod)
mutated_mod['func_6653'] = func_6653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6653_call = mutated_mod.get_global_var('func_6653')
call_6654 = func_6653_call()
output = call_6654
func_6655 = relay.Function([], output)
mutated_mod['func_6655'] = func_6655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1946_call = mod.get_global_var('func_1946')
func_1947_call = mutated_mod.get_global_var('func_1947')
call_6667 = func_1946_call()
call_6668 = func_1946_call()
output = call_6667
output2 = call_6668
func_6679 = relay.Function([], output)
mod['func_6679'] = func_6679
mod = relay.transform.InferType()(mod)
output = func_6679()
func_6680 = relay.Function([], output)
mutated_mod['func_6680'] = func_6680
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6721 = relay.var("var_6721", dtype = "float32", shape = (13, 2, 13))#candidate|6721|(13, 2, 13)|var|float32
uop_6722 = relay.tan(var_6721.astype('float32')) # shape=(13, 2, 13)
output = relay.Tuple([uop_6722,])
output2 = relay.Tuple([uop_6722,])
func_6724 = relay.Function([var_6721,], output)
mod['func_6724'] = func_6724
mod = relay.transform.InferType()(mod)
mutated_mod['func_6724'] = func_6724
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6725 = relay.var("var_6725", dtype = "float32", shape = (13, 2, 13))#candidate|6725|(13, 2, 13)|var|float32
func_6724_call = mutated_mod.get_global_var('func_6724')
call_6726 = func_6724_call(var_6725)
output = call_6726
func_6727 = relay.Function([var_6725], output)
mutated_mod['func_6727'] = func_6727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3745_call = mod.get_global_var('func_3745')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_6740 = relay.TupleGetItem(func_3745_call(), 1)
call_6741 = relay.TupleGetItem(func_3747_call(), 1)
output = call_6740
output2 = call_6741
func_6759 = relay.Function([], output)
mod['func_6759'] = func_6759
mod = relay.transform.InferType()(mod)
mutated_mod['func_6759'] = func_6759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6759_call = mutated_mod.get_global_var('func_6759')
call_6760 = func_6759_call()
output = call_6760
func_6761 = relay.Function([], output)
mutated_mod['func_6761'] = func_6761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_6852 = func_1698_call()
call_6853 = func_1698_call()
output = call_6852
output2 = call_6853
func_6878 = relay.Function([], output)
mod['func_6878'] = func_6878
mod = relay.transform.InferType()(mod)
output = func_6878()
func_6879 = relay.Function([], output)
mutated_mod['func_6879'] = func_6879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6259_call = mod.get_global_var('func_6259')
func_6260_call = mutated_mod.get_global_var('func_6260')
call_6880 = relay.TupleGetItem(func_6259_call(), 1)
call_6881 = relay.TupleGetItem(func_6260_call(), 1)
func_1845_call = mod.get_global_var('func_1845')
func_1848_call = mutated_mod.get_global_var('func_1848')
var_6904 = relay.var("var_6904", dtype = "uint64", shape = (128,))#candidate|6904|(128,)|var|uint64
call_6903 = relay.TupleGetItem(func_1845_call(relay.reshape(var_6904.astype('uint64'), [2, 16, 4])), 1)
call_6905 = relay.TupleGetItem(func_1848_call(relay.reshape(var_6904.astype('uint64'), [2, 16, 4])), 1)
output = relay.Tuple([call_6880,call_6903,var_6904,])
output2 = relay.Tuple([call_6881,call_6905,var_6904,])
func_6906 = relay.Function([var_6904,], output)
mod['func_6906'] = func_6906
mod = relay.transform.InferType()(mod)
var_6907 = relay.var("var_6907", dtype = "uint64", shape = (128,))#candidate|6907|(128,)|var|uint64
output = func_6906(var_6907)
func_6908 = relay.Function([var_6907], output)
mutated_mod['func_6908'] = func_6908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5242_call = mod.get_global_var('func_5242')
func_5244_call = mutated_mod.get_global_var('func_5244')
call_6925 = relay.TupleGetItem(func_5242_call(), 0)
call_6926 = relay.TupleGetItem(func_5244_call(), 0)
output = call_6925
output2 = call_6926
func_6939 = relay.Function([], output)
mod['func_6939'] = func_6939
mod = relay.transform.InferType()(mod)
mutated_mod['func_6939'] = func_6939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6939_call = mutated_mod.get_global_var('func_6939')
call_6940 = func_6939_call()
output = call_6940
func_6941 = relay.Function([], output)
mutated_mod['func_6941'] = func_6941
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6942 = relay.var("var_6942", dtype = "int64", shape = (16, 12, 9))#candidate|6942|(16, 12, 9)|var|int64
var_6943 = relay.var("var_6943", dtype = "int64", shape = (16, 12, 9))#candidate|6943|(16, 12, 9)|var|int64
bop_6944 = relay.maximum(var_6942.astype('int64'), relay.reshape(var_6943.astype('int64'), relay.shape_of(var_6942))) # shape=(16, 12, 9)
func_1698_call = mod.get_global_var('func_1698')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_6956 = func_1698_call()
call_6957 = func_1698_call()
func_2491_call = mod.get_global_var('func_2491')
func_2492_call = mutated_mod.get_global_var('func_2492')
call_6958 = relay.TupleGetItem(func_2491_call(), 0)
call_6959 = relay.TupleGetItem(func_2492_call(), 0)
output = relay.Tuple([bop_6944,call_6956,call_6958,])
output2 = relay.Tuple([bop_6944,call_6957,call_6959,])
func_6960 = relay.Function([var_6942,var_6943,], output)
mod['func_6960'] = func_6960
mod = relay.transform.InferType()(mod)
mutated_mod['func_6960'] = func_6960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6960_call = mutated_mod.get_global_var('func_6960')
var_6962 = relay.var("var_6962", dtype = "int64", shape = (16, 12, 9))#candidate|6962|(16, 12, 9)|var|int64
var_6963 = relay.var("var_6963", dtype = "int64", shape = (16, 12, 9))#candidate|6963|(16, 12, 9)|var|int64
call_6961 = func_6960_call(var_6962,var_6963,)
output = call_6961
func_6964 = relay.Function([var_6962,var_6963,], output)
mutated_mod['func_6964'] = func_6964
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6995 = relay.var("var_6995", dtype = "bool", shape = (5, 14, 12))#candidate|6995|(5, 14, 12)|var|bool
var_6996 = relay.var("var_6996", dtype = "bool", shape = (5, 14, 12))#candidate|6996|(5, 14, 12)|var|bool
bop_6997 = relay.logical_or(var_6995.astype('bool'), relay.reshape(var_6996.astype('bool'), relay.shape_of(var_6995))) # shape=(5, 14, 12)
func_1946_call = mod.get_global_var('func_1946')
func_1947_call = mutated_mod.get_global_var('func_1947')
call_7002 = func_1946_call()
call_7003 = func_1946_call()
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
var_7019 = relay.var("var_7019", dtype = "float32", shape = (1320,))#candidate|7019|(1320,)|var|float32
call_7018 = func_2305_call(relay.reshape(var_7019.astype('float32'), [11, 15, 8]))
call_7020 = func_2305_call(relay.reshape(var_7019.astype('float32'), [11, 15, 8]))
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_7031 = func_2385_call()
call_7032 = func_2385_call()
uop_7033 = relay.log(var_6996.astype('float64')) # shape=(5, 14, 12)
uop_7042 = relay.sinh(uop_7033.astype('float64')) # shape=(5, 14, 12)
output = relay.Tuple([bop_6997,call_7002,call_7018,var_7019,call_7031,uop_7042,])
output2 = relay.Tuple([bop_6997,call_7003,call_7020,var_7019,call_7032,uop_7042,])
func_7055 = relay.Function([var_6995,var_6996,var_7019,], output)
mod['func_7055'] = func_7055
mod = relay.transform.InferType()(mod)
var_7056 = relay.var("var_7056", dtype = "bool", shape = (5, 14, 12))#candidate|7056|(5, 14, 12)|var|bool
var_7057 = relay.var("var_7057", dtype = "bool", shape = (5, 14, 12))#candidate|7057|(5, 14, 12)|var|bool
var_7058 = relay.var("var_7058", dtype = "float32", shape = (1320,))#candidate|7058|(1320,)|var|float32
output = func_7055(var_7056,var_7057,var_7058,)
func_7059 = relay.Function([var_7056,var_7057,var_7058,], output)
mutated_mod['func_7059'] = func_7059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mod.get_global_var('func_4158')
func_4160_call = mutated_mod.get_global_var('func_4160')
call_7107 = relay.TupleGetItem(func_4158_call(), 1)
call_7108 = relay.TupleGetItem(func_4160_call(), 1)
func_6581_call = mod.get_global_var('func_6581')
func_6582_call = mutated_mod.get_global_var('func_6582')
call_7121 = func_6581_call()
call_7122 = func_6581_call()
output = relay.Tuple([call_7107,call_7121,])
output2 = relay.Tuple([call_7108,call_7122,])
func_7153 = relay.Function([], output)
mod['func_7153'] = func_7153
mod = relay.transform.InferType()(mod)
mutated_mod['func_7153'] = func_7153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7153_call = mutated_mod.get_global_var('func_7153')
call_7154 = func_7153_call()
output = call_7154
func_7155 = relay.Function([], output)
mutated_mod['func_7155'] = func_7155
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7169 = relay.var("var_7169", dtype = "int32", shape = (6, 3, 8))#candidate|7169|(6, 3, 8)|var|int32
var_7170 = relay.var("var_7170", dtype = "int32", shape = (6, 3, 8))#candidate|7170|(6, 3, 8)|var|int32
bop_7171 = relay.right_shift(var_7169.astype('int32'), relay.reshape(var_7170.astype('int32'), relay.shape_of(var_7169))) # shape=(6, 3, 8)
func_6878_call = mod.get_global_var('func_6878')
func_6879_call = mutated_mod.get_global_var('func_6879')
call_7185 = func_6878_call()
call_7186 = func_6878_call()
uop_7194 = relay.atanh(var_7170.astype('float32')) # shape=(6, 3, 8)
func_6573_call = mod.get_global_var('func_6573')
func_6574_call = mutated_mod.get_global_var('func_6574')
call_7200 = relay.TupleGetItem(func_6573_call(), 0)
call_7201 = relay.TupleGetItem(func_6574_call(), 0)
func_232_call = mod.get_global_var('func_232')
func_235_call = mutated_mod.get_global_var('func_235')
var_7215 = relay.var("var_7215", dtype = "float32", shape = ())#candidate|7215|()|var|float32
var_7216 = relay.var("var_7216", dtype = "float32", shape = (256,))#candidate|7216|(256,)|var|float32
call_7214 = func_232_call(relay.reshape(var_7215.astype('float32'), []), relay.reshape(var_7216.astype('float32'), [16, 2, 8]), )
call_7217 = func_232_call(relay.reshape(var_7215.astype('float32'), []), relay.reshape(var_7216.astype('float32'), [16, 2, 8]), )
uop_7219 = relay.exp(uop_7194.astype('float64')) # shape=(6, 3, 8)
func_4035_call = mod.get_global_var('func_4035')
func_4036_call = mutated_mod.get_global_var('func_4036')
call_7224 = func_4035_call()
call_7225 = func_4035_call()
output = relay.Tuple([bop_7171,call_7185,call_7200,call_7214,var_7215,var_7216,uop_7219,call_7224,])
output2 = relay.Tuple([bop_7171,call_7186,call_7201,call_7217,var_7215,var_7216,uop_7219,call_7225,])
func_7233 = relay.Function([var_7169,var_7170,var_7215,var_7216,], output)
mod['func_7233'] = func_7233
mod = relay.transform.InferType()(mod)
mutated_mod['func_7233'] = func_7233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7233_call = mutated_mod.get_global_var('func_7233')
var_7235 = relay.var("var_7235", dtype = "int32", shape = (6, 3, 8))#candidate|7235|(6, 3, 8)|var|int32
var_7236 = relay.var("var_7236", dtype = "int32", shape = (6, 3, 8))#candidate|7236|(6, 3, 8)|var|int32
var_7237 = relay.var("var_7237", dtype = "float32", shape = ())#candidate|7237|()|var|float32
var_7238 = relay.var("var_7238", dtype = "float32", shape = (256,))#candidate|7238|(256,)|var|float32
call_7234 = func_7233_call(var_7235,var_7236,var_7237,var_7238,)
output = call_7234
func_7239 = relay.Function([var_7235,var_7236,var_7237,var_7238,], output)
mutated_mod['func_7239'] = func_7239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5295_call = mod.get_global_var('func_5295')
func_5297_call = mutated_mod.get_global_var('func_5297')
call_7332 = func_5295_call()
call_7333 = func_5295_call()
output = call_7332
output2 = call_7333
func_7338 = relay.Function([], output)
mod['func_7338'] = func_7338
mod = relay.transform.InferType()(mod)
mutated_mod['func_7338'] = func_7338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7338_call = mutated_mod.get_global_var('func_7338')
call_7339 = func_7338_call()
output = call_7339
func_7340 = relay.Function([], output)
mutated_mod['func_7340'] = func_7340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2079_call = mod.get_global_var('func_2079')
func_2080_call = mutated_mod.get_global_var('func_2080')
call_7386 = func_2079_call()
call_7387 = func_2079_call()
output = relay.Tuple([call_7386,])
output2 = relay.Tuple([call_7387,])
func_7435 = relay.Function([], output)
mod['func_7435'] = func_7435
mod = relay.transform.InferType()(mod)
mutated_mod['func_7435'] = func_7435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7435_call = mutated_mod.get_global_var('func_7435')
call_7436 = func_7435_call()
output = call_7436
func_7437 = relay.Function([], output)
mutated_mod['func_7437'] = func_7437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6939_call = mod.get_global_var('func_6939')
func_6941_call = mutated_mod.get_global_var('func_6941')
call_7471 = func_6939_call()
call_7472 = func_6939_call()
output = call_7471
output2 = call_7472
func_7489 = relay.Function([], output)
mod['func_7489'] = func_7489
mod = relay.transform.InferType()(mod)
output = func_7489()
func_7490 = relay.Function([], output)
mutated_mod['func_7490'] = func_7490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mod.get_global_var('func_3755')
func_3757_call = mutated_mod.get_global_var('func_3757')
call_7505 = relay.TupleGetItem(func_3755_call(), 0)
call_7506 = relay.TupleGetItem(func_3757_call(), 0)
func_3803_call = mod.get_global_var('func_3803')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_7519 = func_3803_call()
call_7520 = func_3803_call()
output = relay.Tuple([call_7505,call_7519,])
output2 = relay.Tuple([call_7506,call_7520,])
func_7521 = relay.Function([], output)
mod['func_7521'] = func_7521
mod = relay.transform.InferType()(mod)
mutated_mod['func_7521'] = func_7521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7521_call = mutated_mod.get_global_var('func_7521')
call_7522 = func_7521_call()
output = call_7522
func_7523 = relay.Function([], output)
mutated_mod['func_7523'] = func_7523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_7576 = func_6154_call()
call_7577 = func_6154_call()
func_1010_call = mod.get_global_var('func_1010')
func_1014_call = mutated_mod.get_global_var('func_1014')
var_7624 = relay.var("var_7624", dtype = "float32", shape = (315,))#candidate|7624|(315,)|var|float32
call_7623 = func_1010_call(relay.reshape(var_7624.astype('float32'), [7, 15, 3]), relay.reshape(var_7624.astype('float32'), [7, 15, 3]), )
call_7625 = func_1010_call(relay.reshape(var_7624.astype('float32'), [7, 15, 3]), relay.reshape(var_7624.astype('float32'), [7, 15, 3]), )
output = relay.Tuple([call_7576,call_7623,var_7624,])
output2 = relay.Tuple([call_7577,call_7625,var_7624,])
func_7648 = relay.Function([var_7624,], output)
mod['func_7648'] = func_7648
mod = relay.transform.InferType()(mod)
var_7649 = relay.var("var_7649", dtype = "float32", shape = (315,))#candidate|7649|(315,)|var|float32
output = func_7648(var_7649)
func_7650 = relay.Function([var_7649], output)
mutated_mod['func_7650'] = func_7650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_7705 = relay.TupleGetItem(func_2816_call(), 1)
call_7706 = relay.TupleGetItem(func_2818_call(), 1)
func_1639_call = mod.get_global_var('func_1639')
func_1642_call = mutated_mod.get_global_var('func_1642')
var_7710 = relay.var("var_7710", dtype = "float64", shape = (2025,))#candidate|7710|(2025,)|var|float64
call_7709 = relay.TupleGetItem(func_1639_call(relay.reshape(var_7710.astype('float64'), [2025,])), 2)
call_7711 = relay.TupleGetItem(func_1642_call(relay.reshape(var_7710.astype('float64'), [2025,])), 2)
output = relay.Tuple([call_7705,call_7709,var_7710,])
output2 = relay.Tuple([call_7706,call_7711,var_7710,])
func_7717 = relay.Function([var_7710,], output)
mod['func_7717'] = func_7717
mod = relay.transform.InferType()(mod)
var_7718 = relay.var("var_7718", dtype = "float64", shape = (2025,))#candidate|7718|(2025,)|var|float64
output = func_7717(var_7718)
func_7719 = relay.Function([var_7718], output)
mutated_mod['func_7719'] = func_7719
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7724 = relay.const([[[4.030445,4.588023,-0.163296,3.996594,7.783409,-4.717290,-6.966795,2.357363,1.092656],[-2.094904,-0.893688,-3.560831,9.106253,3.019880,-9.680266,5.910849,9.856144,7.031199],[5.160448,-1.018137,7.343299,-1.441537,6.319652,-1.269017,-1.722920,7.248320,-6.778656],[8.228092,1.938514,-4.687201,7.656503,3.903325,-7.687777,-5.248826,4.779737,-1.154344],[1.406559,9.657895,-4.429365,6.692427,-1.478938,3.198168,0.282221,2.955582,8.099498],[-3.253955,0.160137,-2.656728,-9.789392,8.123746,8.780980,2.224818,-3.483548,1.184147],[-4.581212,0.677830,2.783283,7.524444,4.182842,-1.808672,-7.112904,3.511909,-0.547912],[3.312485,-7.003584,5.406569,8.597715,5.496360,1.072141,-4.709815,0.233030,-7.608763],[5.919255,1.445511,-9.172488,0.355085,-5.121321,-0.637659,-3.986929,-4.294761,-0.360967],[-7.057694,-3.689549,0.780840,-3.756256,9.482400,-9.622777,2.515181,-5.677715,-7.708291],[-3.125988,9.536190,5.600439,1.356091,-4.832176,-6.450319,5.996936,-6.041203,-5.287873],[7.843856,3.329990,7.763720,7.679407,8.869187,0.673602,-7.633891,-3.860050,5.986264],[-1.563730,1.356355,-4.450584,9.704953,9.065449,7.019855,-2.396781,-6.179183,9.210028],[4.386226,-4.016889,-1.779556,-0.922883,7.842913,6.792294,-4.517353,-9.779277,-6.913712],[-5.049537,-8.864701,8.675701,8.917769,5.893277,8.955154,3.429429,4.460474,-0.511810]]], dtype = "float64")#candidate|7724|(1, 15, 9)|const|float64
uop_7725 = relay.asinh(const_7724.astype('float64')) # shape=(1, 15, 9)
func_4476_call = mod.get_global_var('func_4476')
func_4478_call = mutated_mod.get_global_var('func_4478')
call_7729 = relay.TupleGetItem(func_4476_call(), 2)
call_7730 = relay.TupleGetItem(func_4478_call(), 2)
output = relay.Tuple([uop_7725,call_7729,])
output2 = relay.Tuple([uop_7725,call_7730,])
func_7731 = relay.Function([], output)
mod['func_7731'] = func_7731
mod = relay.transform.InferType()(mod)
mutated_mod['func_7731'] = func_7731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7731_call = mutated_mod.get_global_var('func_7731')
call_7732 = func_7731_call()
output = call_7732
func_7733 = relay.Function([], output)
mutated_mod['func_7733'] = func_7733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3745_call = mod.get_global_var('func_3745')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_7737 = relay.TupleGetItem(func_3745_call(), 2)
call_7738 = relay.TupleGetItem(func_3747_call(), 2)
var_7739 = relay.var("var_7739", dtype = "float32", shape = (2, 16, 4))#candidate|7739|(2, 16, 4)|var|float32
bop_7740 = relay.power(call_7737.astype('float32'), relay.reshape(var_7739.astype('float32'), relay.shape_of(call_7737))) # shape=(2, 16, 4)
bop_7743 = relay.power(call_7738.astype('float32'), relay.reshape(var_7739.astype('float32'), relay.shape_of(call_7738))) # shape=(2, 16, 4)
uop_7755 = relay.cosh(call_7737.astype('float64')) # shape=(2, 16, 4)
uop_7757 = relay.cosh(call_7738.astype('float64')) # shape=(2, 16, 4)
output = relay.Tuple([bop_7740,uop_7755,])
output2 = relay.Tuple([bop_7743,uop_7757,])
func_7761 = relay.Function([var_7739,], output)
mod['func_7761'] = func_7761
mod = relay.transform.InferType()(mod)
var_7762 = relay.var("var_7762", dtype = "float32", shape = (2, 16, 4))#candidate|7762|(2, 16, 4)|var|float32
output = func_7761(var_7762)
func_7763 = relay.Function([var_7762], output)
mutated_mod['func_7763'] = func_7763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3333_call = mod.get_global_var('func_3333')
func_3334_call = mutated_mod.get_global_var('func_3334')
call_7782 = relay.TupleGetItem(func_3333_call(), 0)
call_7783 = relay.TupleGetItem(func_3334_call(), 0)
output = relay.Tuple([call_7782,])
output2 = relay.Tuple([call_7783,])
func_7790 = relay.Function([], output)
mod['func_7790'] = func_7790
mod = relay.transform.InferType()(mod)
mutated_mod['func_7790'] = func_7790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7790_call = mutated_mod.get_global_var('func_7790')
call_7791 = func_7790_call()
output = call_7791
func_7792 = relay.Function([], output)
mutated_mod['func_7792'] = func_7792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5542_call = mod.get_global_var('func_5542')
func_5544_call = mutated_mod.get_global_var('func_5544')
call_7812 = relay.TupleGetItem(func_5542_call(), 0)
call_7813 = relay.TupleGetItem(func_5544_call(), 0)
output = call_7812
output2 = call_7813
func_7827 = relay.Function([], output)
mod['func_7827'] = func_7827
mod = relay.transform.InferType()(mod)
output = func_7827()
func_7828 = relay.Function([], output)
mutated_mod['func_7828'] = func_7828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7880 = relay.var("var_7880", dtype = "float64", shape = (14, 3, 14))#candidate|7880|(14, 3, 14)|var|float64
uop_7881 = relay.sigmoid(var_7880.astype('float64')) # shape=(14, 3, 14)
output = uop_7881
output2 = uop_7881
func_7887 = relay.Function([var_7880,], output)
mod['func_7887'] = func_7887
mod = relay.transform.InferType()(mod)
var_7888 = relay.var("var_7888", dtype = "float64", shape = (14, 3, 14))#candidate|7888|(14, 3, 14)|var|float64
output = func_7887(var_7888)
func_7889 = relay.Function([var_7888], output)
mutated_mod['func_7889'] = func_7889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4978_call = mod.get_global_var('func_4978')
func_4980_call = mutated_mod.get_global_var('func_4980')
call_7891 = relay.TupleGetItem(func_4978_call(), 0)
call_7892 = relay.TupleGetItem(func_4980_call(), 0)
func_5542_call = mod.get_global_var('func_5542')
func_5544_call = mutated_mod.get_global_var('func_5544')
call_7900 = relay.TupleGetItem(func_5542_call(), 0)
call_7901 = relay.TupleGetItem(func_5544_call(), 0)
func_6581_call = mod.get_global_var('func_6581')
func_6582_call = mutated_mod.get_global_var('func_6582')
call_7902 = func_6581_call()
call_7903 = func_6581_call()
func_7790_call = mod.get_global_var('func_7790')
func_7792_call = mutated_mod.get_global_var('func_7792')
call_7916 = relay.TupleGetItem(func_7790_call(), 0)
call_7917 = relay.TupleGetItem(func_7792_call(), 0)
func_2038_call = mod.get_global_var('func_2038')
func_2040_call = mutated_mod.get_global_var('func_2040')
const_7937 = relay.const(5.100161, dtype = "float32")#candidate|7937|()|const|float32
call_7936 = relay.TupleGetItem(func_2038_call(relay.reshape(const_7937.astype('float32'), [])), 5)
call_7938 = relay.TupleGetItem(func_2040_call(relay.reshape(const_7937.astype('float32'), [])), 5)
func_2190_call = mod.get_global_var('func_2190')
func_2193_call = mutated_mod.get_global_var('func_2193')
const_7941 = relay.const([[3.432916,9.372113,2.709947,6.115154,-4.002419,-9.974941,-9.316513,0.349149,-5.898448,9.327136,-8.493304,3.619602,-1.190979,6.551776,3.504740],[0.790199,1.493066,8.821647,-4.439317,8.703744,0.979902,-2.820713,4.095431,0.995675,-8.502108,2.240498,9.234238,-5.158256,4.215516,-9.783859],[6.307556,1.180624,-8.859543,6.877807,-5.060699,1.882232,-0.151492,7.175969,0.187588,-2.513665,4.138101,-5.272578,-8.252891,7.018161,-1.913421],[-4.015847,3.557934,-4.501910,-1.279327,-8.085278,-9.345568,-3.733031,-4.062490,-3.933180,-3.792565,0.736310,-4.400289,-8.871160,-3.929862,6.344874],[8.920365,-6.051727,1.345102,-9.465432,1.190776,-4.915352,-6.760537,-8.743059,-1.963428,0.546949,6.053950,1.401962,-4.447245,-6.079948,8.753432],[-1.331128,2.202966,9.224747,4.931516,8.146501,7.799277,0.296916,-5.219828,-9.187013,-9.475587,-5.032686,-9.945030,-5.063291,4.175451,-0.832960],[-0.616298,-3.264779,5.794371,-8.794962,1.145579,3.893827,-8.715714,1.146485,9.448776,0.760843,1.927852,7.989445,1.778693,-9.895650,8.777247],[9.093936,7.250028,5.123762,-7.390013,-5.948266,7.854278,-4.660896,-4.851511,9.606266,7.507519,4.797909,-8.645603,-3.032628,-0.182438,-4.091697],[5.970919,6.180989,4.759598,-7.053725,6.238022,-9.333968,-1.756127,-6.692857,-9.759889,-1.981624,-9.203443,-6.162045,5.009648,2.306664,0.717464],[9.765170,1.676473,-0.222205,2.727251,-3.126335,7.576878,-9.833547,1.601915,-9.298169,-0.567626,4.239418,-3.398805,7.235213,4.641204,-8.279020],[-7.802932,1.873969,-1.433485,2.887421,-6.333595,-5.041792,-1.467574,-5.869920,1.505157,5.373095,9.776248,8.465726,-7.440933,3.021977,6.269218],[-2.087965,8.783836,3.305929,6.784607,-2.533679,6.585622,7.350103,1.727707,5.009179,-3.713569,-1.135238,-6.711270,-2.009442,-0.886675,-4.532366],[8.137240,3.991153,-1.720859,-7.192306,2.726274,-8.585103,-5.315001,-4.087833,0.674627,-4.431423,-0.605369,2.873174,-1.093213,7.558626,-5.869846],[-6.333142,5.562638,-7.002582,4.040210,8.191119,9.171199,8.286848,-3.718925,4.364820,5.474332,6.382593,-5.108226,-5.699362,-9.078845,9.330577],[3.651001,-3.605602,-4.279133,6.120574,-2.918636,-3.442949,-5.201634,7.442680,-0.916674,-0.508123,-4.512964,2.340188,-0.261598,-0.063039,-2.236839],[3.278779,3.369438,-6.623906,8.579476,2.066724,-9.417180,7.764908,4.661352,7.072110,-0.697653,-2.719101,-7.908721,2.629548,6.223440,7.151179],[-3.310441,-0.364678,4.691008,5.883023,-5.370085,-9.260267,-1.910958,6.622963,-9.562543,5.040638,-7.600932,5.929863,-5.126081,6.867051,-9.489532],[6.578223,-2.876484,6.546521,-9.664984,-3.040831,7.611131,7.803462,-7.191163,-6.470127,-9.012138,8.694703,8.517111,7.751570,-8.335548,5.940872],[6.304033,6.186392,-8.929738,1.434524,8.780052,3.622235,-8.636701,-9.779467,2.360922,1.198223,1.547342,-6.025082,-4.306624,-1.314549,8.984843],[1.967461,-4.723698,-8.630830,9.545490,9.013884,2.737702,-0.329526,0.650072,-7.171511,6.766658,-9.218162,3.256322,7.808704,-7.350168,-3.908498],[4.284445,4.759427,-8.280396,4.162659,1.159421,-6.256012,9.250015,6.761060,2.471924,-1.425850,4.280487,2.120633,0.378449,-8.651787,-6.903986],[7.937610,9.712587,3.806051,-5.472428,4.658375,7.832234,-9.192119,-7.780870,-4.459978,-4.855092,-0.828364,0.124333,-5.251053,-2.573229,4.912556],[9.220990,0.306143,8.904424,-4.347519,7.906894,0.118809,9.476510,2.751217,3.270538,4.038627,-4.137610,-9.669999,-0.557804,3.702583,5.891720],[4.370475,9.973901,3.682983,-6.575226,9.400486,-1.544496,-3.015596,-4.301823,7.622834,1.797317,4.152739,2.003340,-3.184557,-3.045596,-7.731275],[-7.731631,-1.578766,-9.436841,-5.103513,4.384965,-1.045193,-7.352638,1.038405,2.163714,4.610334,-6.813905,-5.908010,-1.277327,0.900809,-4.053514],[-3.444490,0.514027,7.474969,3.844283,-2.807075,5.648760,-3.252202,-9.778309,-7.522203,-8.128607,-6.577167,8.199387,-7.304437,9.293315,-4.269164],[-6.113050,-3.701351,-5.931356,4.576721,7.684038,-4.324072,4.779172,2.932281,6.565123,5.511406,1.554945,-4.858428,-1.080374,-0.385649,-9.335393],[-6.461663,7.314565,-6.949358,-7.229388,7.503569,-8.626187,-8.306777,-4.409190,5.828747,1.376087,-7.556840,-2.555343,1.546406,1.117154,2.209910],[1.693259,-9.671453,-9.166516,-1.257370,8.966228,9.213462,5.303659,5.079238,1.051804,5.665545,1.920127,5.718274,-3.147766,-7.980104,-7.522403],[2.729071,8.653879,-2.925915,9.523211,-6.523246,8.703984,-8.295293,8.414478,-3.535467,-2.604458,-2.831632,8.011113,2.424765,-0.198513,-0.290909],[3.398206,-9.569575,1.996896,5.117724,9.453514,1.567725,9.373654,-0.971194,0.670059,4.383780,-6.705604,0.055801,0.423550,-2.210795,3.451045],[-7.760308,-6.402189,8.734016,1.810546,-7.238514,5.270784,8.668167,7.237395,0.318753,5.355385,-0.993095,-3.355128,5.229265,5.638808,-9.284845],[-3.974944,2.283729,3.416211,6.399210,5.133470,-1.262031,5.671398,4.151111,8.745503,-2.779150,8.512824,-5.678723,-2.322788,3.680584,5.333282],[-6.783499,-1.995063,5.503909,8.521149,7.156523,-1.620288,2.192379,0.211637,4.602418,2.535408,0.016005,-5.502474,3.686114,-0.317360,-7.326632],[-1.547396,0.496579,7.797200,-2.300456,6.818373,3.307306,3.412886,-1.702797,-1.600014,5.629482,4.994083,-4.263126,5.339720,-4.107783,0.659378],[3.856965,-9.015986,-5.579076,0.803854,-2.721590,-2.772590,2.676088,-3.244079,2.941968,8.775474,-4.484327,4.362667,-5.127964,-1.086639,-7.905601],[-3.864633,6.163918,0.854170,-6.141777,9.086667,7.606786,-6.907635,1.089656,-2.775864,7.523617,-6.753701,-2.337616,8.221696,-7.610044,-9.147815],[6.108297,-6.511054,0.784292,-1.600933,6.663675,-8.698853,-3.872981,5.679005,8.296361,-6.652453,9.862592,-7.719456,-9.873087,-8.502279,-0.532222],[-6.664526,1.784473,-2.426032,-9.578570,-4.023438,-7.216050,-5.786930,-3.654096,5.437374,-9.867915,-8.798322,-8.617973,9.387349,-7.832443,9.399838],[-8.321116,-3.637727,-2.768881,-2.466026,-5.786244,-5.455446,4.560508,9.906187,-8.376768,7.641392,-9.996502,-4.827974,3.541738,9.275971,-1.696517],[-1.669754,-0.615263,-7.035569,9.704039,9.705258,-5.057988,5.170818,3.074704,9.730456,4.339569,-5.100241,-4.083957,-9.032417,-1.452685,-6.323429],[-0.590371,-1.265973,4.329366,1.163772,7.428465,-3.970057,6.501756,-9.961897,-3.529556,-6.884270,-1.622182,1.777697,-1.576375,-9.478498,-7.616406],[4.447457,1.431989,3.198372,-1.420906,-7.803881,-9.292021,7.687707,-3.259533,-7.837220,6.232618,-9.422971,4.902623,2.140644,7.158994,-3.922819],[-6.113728,-2.645820,3.193027,-7.012154,-9.354574,-6.422157,-1.037508,-4.173230,1.544527,2.693901,-3.719150,-5.660223,-7.156518,9.946043,-9.518248],[5.892344,2.660709,-8.595132,3.456275,-8.749822,3.667352,-6.128805,9.232529,-7.642898,8.054475,5.904092,9.284962,7.791442,7.313422,4.170094],[4.451419,-7.247867,-5.570344,3.396501,-3.336987,-4.307399,-1.021841,9.982574,2.779630,-8.583235,2.888123,-9.314526,-4.360080,-3.738769,-4.235377],[0.960240,-8.874824,-1.321134,-5.169260,9.312843,-6.683766,9.111869,-7.823869,-5.564180,-1.565941,0.922596,-5.383697,6.713132,7.231309,9.663077],[4.850588,6.729529,-3.633540,1.418026,-4.434163,7.705411,-5.215315,3.153886,0.627426,-3.117294,8.830813,-7.449851,-7.317219,-4.540559,4.191471],[6.918335,-8.267071,1.049171,3.944282,2.531513,6.335753,-8.456260,9.183674,-2.583060,4.601831,3.130618,-0.409669,-1.144879,3.556805,7.244595],[-3.915683,3.242700,1.848362,-9.751514,6.035425,-9.774996,-0.598290,-4.735536,6.948335,8.231203,-5.700630,4.373214,-4.144133,5.361607,-1.030851],[-5.098545,7.894703,9.770680,-2.791723,8.966723,1.922293,-8.770393,-1.849768,-7.717394,-9.712709,-2.091589,-0.147273,9.058600,-5.610043,-2.975771],[3.811393,9.863935,-4.357527,-0.125043,-8.416788,5.381640,6.338005,-8.855953,-1.969572,2.408882,-7.114261,1.250068,8.038934,1.662710,9.340953],[-5.626533,-0.744329,-3.236864,-4.347272,-6.817756,-6.500415,1.837966,8.762645,-2.224821,-2.606148,-7.391089,3.005573,7.238533,7.985428,-5.547155],[-1.661661,9.113106,0.168897,7.333638,-8.582703,-5.285912,8.908077,9.097005,3.932955,4.858318,6.823590,-0.429840,2.625342,-2.963670,-7.231672],[-3.212318,3.676463,-6.721300,1.482113,6.854326,3.118089,-9.911376,4.820275,5.314225,6.888703,-4.356254,1.735464,-3.257069,-4.905757,4.120610],[9.976673,2.197331,0.881357,1.442364,9.285381,9.017548,0.110979,-1.687061,7.594926,4.004472,-9.328901,7.394639,9.949537,-2.902231,-4.114795],[-6.073280,5.313618,0.081591,6.076810,7.927570,4.278664,7.262189,3.016177,2.335980,-6.546155,1.999128,-5.230255,-8.948864,-9.589272,9.749409],[-5.449320,4.308395,9.889044,-7.250093,7.165600,8.544006,-8.596254,6.431664,-3.210648,-7.173111,-9.215004,3.932558,5.859761,-7.433916,0.885137],[-9.530046,8.224615,5.577588,-8.283904,-9.122509,-2.303078,-5.513193,-3.968250,-6.214142,-0.811498,1.253446,-5.994876,4.519480,-0.049852,-1.502806],[3.230566,2.310166,-4.779643,7.945358,8.995675,-3.194422,-5.029859,-5.792040,4.336803,7.923140,-4.623495,-1.825612,-0.854105,-3.678843,7.198868],[-8.581814,8.446007,2.571146,-1.213031,0.731799,-7.961715,0.079444,-2.865151,-8.567189,-7.452089,-5.826190,-9.386625,-1.774816,-5.236943,-5.982632],[7.070864,9.058685,-7.148198,-5.349760,9.430848,-2.860500,6.198029,-3.128686,-9.768761,6.443910,2.403918,4.037131,-8.703857,-3.358176,-1.516116],[-1.620582,3.070816,-9.228423,6.839008,-5.540544,-4.391551,-6.015191,8.982862,-0.454351,5.559827,-8.144517,8.234270,7.325659,8.331457,-2.606581],[-2.505998,2.366359,-4.475462,4.250458,-2.924513,6.963746,9.313815,4.203060,-5.110101,-2.067752,7.503777,-9.480205,-6.024540,7.940443,1.041074],[1.693400,-1.317317,6.434567,-7.317324,-5.678091,3.584071,-4.723061,-7.250830,3.295946,5.306772,-6.818390,-4.433128,8.108909,-5.816298,1.301567],[-4.283069,2.743055,0.220796,-0.606111,-5.387423,1.216399,-5.842508,-5.111022,1.620685,5.127762,1.698784,1.493677,6.354067,-0.243414,1.943726],[9.707324,-8.800675,3.919587,-4.332127,1.755519,-9.729698,-8.605656,-1.405807,8.968250,-4.195363,-5.959487,5.157018,6.614282,-1.758119,-5.556875],[5.886389,-1.776414,6.873679,-9.609880,4.148046,-9.219286,-1.114390,-8.881103,9.331199,-4.637001,-6.672005,9.065115,-5.419704,-9.194982,-2.436152],[3.297144,4.139662,1.762330,3.154824,-6.802070,9.168344,-1.941597,8.631163,4.254677,2.170898,-7.274441,-4.349700,4.589501,-5.199900,-2.222557],[-9.927549,4.175299,2.995283,-7.116182,-2.206864,1.700549,0.982768,6.562832,-1.430390,5.154827,-5.004365,5.633717,6.301759,3.178843,1.199003],[-5.158389,8.689075,3.275707,-7.903579,3.166258,-7.251519,2.361641,8.579161,-7.616023,4.718816,8.326642,6.713239,-7.683520,9.742005,-8.342905],[3.778902,-9.678432,-4.655386,7.209913,-7.981941,7.227105,5.313091,-6.320647,6.764781,-1.092310,9.635857,-3.924862,8.914088,8.570628,7.000176],[2.461169,3.679808,1.757189,3.607840,-8.543773,-6.039897,-4.603584,-9.666431,-4.315111,6.441396,-5.886714,-6.566786,5.407089,-8.883055,-1.053333],[-2.350529,-4.364676,5.721741,-9.715373,3.694831,-9.438104,-8.925434,3.492516,-5.309190,3.452503,8.460239,-1.557587,-2.954291,1.839517,-1.722933],[-6.887472,4.158952,-5.046745,6.532954,4.214129,-5.150685,-9.707050,-3.994928,4.062843,2.282515,-7.721940,6.317463,-6.859288,-3.719590,-0.347141],[0.427139,3.660934,1.603397,7.608928,-4.979824,9.210263,5.807068,-1.882461,-0.680230,-1.122184,-0.047586,-8.216291,7.042413,5.851931,-1.026326],[-1.863320,9.696770,-5.317641,-2.591123,0.491491,-2.514642,7.712029,-2.832098,9.416715,7.485558,-4.686837,-7.521701,6.185178,6.379833,0.951604],[-4.567431,8.087901,1.183074,6.642359,3.802228,4.855360,1.126530,8.075150,-6.717000,-3.061333,-7.730288,0.625751,0.261401,-2.371040,1.576267],[-1.838642,-7.950958,6.039202,9.279215,4.257396,1.873936,-8.724632,5.741447,-6.338304,-1.917595,6.607404,1.921698,6.083954,-6.404606,5.966046],[6.971667,7.904853,2.488235,-1.643276,9.696445,-5.041031,-3.573431,-1.062082,-4.131054,3.628337,4.989079,-6.959570,0.275545,-3.880501,9.352917],[3.777908,5.974639,-9.941757,-7.527955,-0.553568,-0.281090,-4.455031,8.427808,-7.172367,-5.453569,2.181881,7.820685,-2.439649,5.710107,-2.822923],[2.388241,-1.022214,-3.144853,3.241287,1.690843,8.116503,-8.866379,-4.606443,-2.056672,-0.655151,-9.499155,-2.515166,9.105931,-1.218934,1.413296],[9.769183,-8.128496,-5.543590,3.698380,6.335620,3.816670,-4.746031,8.166221,5.457996,-0.592715,-2.782343,2.767736,-9.873581,2.189842,-7.820494],[0.834608,1.856260,2.648084,-1.296541,-0.169666,7.649598,-2.268158,3.659546,-8.761400,7.210569,-6.752262,3.997663,5.271285,-4.473443,-9.844683],[3.876772,4.124429,1.738113,-5.640888,9.515684,-6.104273,-8.422151,-2.300540,-2.831645,1.558383,4.088345,0.128073,0.234525,-4.798527,2.061183],[-3.172203,-6.304315,-5.865861,-5.722149,-6.873631,6.272483,-5.641449,0.231657,6.131099,9.236943,-4.682646,8.625242,2.703884,-8.098895,-3.974713],[-7.998549,-7.008086,-5.885148,3.449807,-4.227992,-1.586545,-2.886918,3.713991,-7.445179,3.513781,9.639198,-4.656498,4.279317,-9.461650,-9.554487],[8.893260,8.931980,0.799989,-1.642468,0.798397,-8.840635,-5.552435,-5.077110,8.232127,3.604818,5.561266,-9.861544,0.902137,6.768019,6.546101],[-8.538349,7.461360,-6.382947,-4.974050,5.141446,1.387142,8.640792,-0.667919,-7.762318,-2.450972,-3.309296,-3.907083,-5.556819,-0.195871,3.129840],[4.593721,-2.059431,-0.657639,5.060396,-1.166062,-8.342070,2.944469,5.866924,8.281549,8.094142,2.890547,0.881638,-1.573390,6.408292,-6.110107],[-0.513193,4.878557,-5.001034,8.981407,-6.530203,-7.429309,-1.477663,-6.862332,2.485723,8.720032,-4.813423,-7.977343,-4.959623,8.875381,6.900580],[2.253122,8.030823,-8.592208,-0.322006,2.868999,1.209043,8.102842,1.669109,-1.375115,6.201646,8.979631,-8.890712,-0.684351,-7.739601,4.092224],[0.518952,2.803381,2.935889,-2.620424,-2.456886,-5.507373,1.932203,0.612994,3.618002,1.402637,7.771937,-8.737019,-5.773243,-0.874768,-7.912286],[-0.169973,-0.737776,-0.014262,8.270358,8.972636,1.687740,-5.565572,5.844015,5.489025,4.012279,-6.817124,-0.614192,-6.019941,4.600177,5.884764],[-7.635467,2.631145,-6.180647,-2.966085,-7.789479,1.549486,5.379271,-4.225017,3.999347,-3.817998,-4.419258,5.665528,6.889014,6.690746,-4.650089],[1.469474,-3.294144,-8.595735,-3.762639,-7.683793,-2.376623,-6.864676,8.963109,7.230850,0.307207,2.796496,-3.795722,-1.256965,8.907578,-4.060682],[-7.929377,-0.318390,-4.216832,7.083071,-1.870876,4.204181,1.548517,-6.403199,-4.936349,2.957873,4.643760,8.433255,2.265114,-9.181036,2.376440],[0.599070,-6.956676,-2.656863,-6.284712,7.238447,3.286047,6.248538,7.929630,-5.698543,9.602656,9.444823,-5.816419,-1.443166,-9.180300,-9.807943],[7.109030,7.537939,-0.102243,-1.303675,-1.839896,5.532334,-1.767619,-0.149129,-2.467045,1.988423,1.541875,2.213160,1.484583,0.728929,-5.440035],[7.177089,2.477394,5.594683,-7.143683,-5.014513,1.613146,1.951640,3.899900,6.758014,-7.077467,0.361754,6.448329,2.861900,4.112637,-7.793948],[1.325595,3.131301,9.559954,-6.753587,7.950107,-8.137667,-0.014557,-9.724537,5.553410,3.443889,1.611907,4.649347,7.263521,4.664663,-7.639024],[-9.978395,-2.028636,-1.749452,-7.465936,7.277511,-1.160902,7.612182,6.996357,-6.442313,4.426680,-9.309540,-0.166232,-9.436756,2.141862,-9.269335],[7.820441,4.117776,6.982130,8.860872,-9.146407,4.463082,-0.262658,7.009222,-6.244141,7.301793,0.290566,-5.124895,3.309772,-4.381649,3.213643],[-0.937850,8.619288,-8.784605,-0.608269,0.520412,-8.199896,4.432941,2.060739,4.683165,-4.602889,6.837650,-9.940458,6.239162,-2.072465,-7.260187],[7.408977,5.302870,-4.352275,2.868927,7.590533,9.687928,1.704508,7.171078,5.059629,-9.176050,1.870261,-6.089860,-9.787858,5.627455,9.654613],[-7.245958,9.701226,3.919610,2.291229,-7.526425,8.005587,-1.040413,-9.869622,3.748513,-6.283500,1.658467,-7.426145,-8.851029,0.368958,4.826496],[8.143002,6.661580,5.390485,2.128842,6.118189,-8.701952,6.671553,1.835786,-0.342527,-2.685575,2.016608,-6.978761,4.880023,-6.133419,-9.417417],[3.445936,9.950235,-4.815601,9.965484,2.673117,4.087813,-5.153829,-2.744911,-3.649335,-2.745854,-9.465585,-8.974460,2.168859,1.467486,6.772224],[-5.464615,2.489090,7.082287,-8.099336,5.888289,-9.902069,0.010075,-0.119515,-9.617801,-2.338499,3.524234,-3.329942,6.572682,5.328174,1.143217],[3.474908,6.957890,7.112772,-3.925677,4.977877,5.175529,5.125212,-4.836465,9.336475,-6.350689,-3.047028,-4.935777,-2.121579,-5.999858,-8.282270],[-7.619058,0.587119,-9.286085,-9.115214,1.199535,2.054944,3.740375,5.858504,-3.605384,2.580902,9.004451,-1.292847,-7.944782,9.010633,-7.871546],[5.445223,3.562897,-1.343041,6.304726,2.824496,-8.407175,-3.770301,5.024489,-0.152151,-4.352451,-0.976923,8.447584,8.973267,1.243545,-6.423726],[-5.982202,-3.185038,1.856461,8.942169,-2.917072,3.081611,2.943118,-8.562264,5.544367,-1.265377,-9.918655,2.092656,5.102366,-5.373114,-5.825313],[-0.155198,-0.291888,-1.057301,5.267660,-5.732922,-5.982381,8.540905,2.145668,-7.119136,-6.595609,-1.433794,-6.137765,-8.208773,-2.899830,-3.714677],[3.101369,8.709493,-8.199243,7.847505,-8.131714,0.395968,6.203431,-7.413521,-9.770672,-2.059487,-3.629574,-3.409033,-8.938198,-2.442609,4.676597],[8.965091,-4.881305,-1.191370,3.260341,-1.795152,7.723339,-5.886193,-0.332289,-6.750018,-8.743043,6.985864,3.995769,0.195411,-5.824702,7.883524],[-9.363757,4.750094,6.278789,2.219780,0.142277,-0.409733,8.562801,-2.796136,-1.466968,2.165540,0.039888,3.799942,-6.134504,-7.966774,-6.846158],[-7.596294,1.424843,3.158324,8.409238,6.022850,1.226263,2.463042,-3.647253,-8.372694,-7.056941,1.527581,5.226089,8.655232,7.315508,-6.780879],[7.697095,1.325448,-0.129612,4.183240,3.676882,6.059227,6.930628,-2.695526,-4.837676,-8.026226,-1.355238,-6.192434,-9.752209,0.345701,0.791029],[2.701391,-4.384917,7.486540,-5.648017,-7.479389,2.311351,-5.534750,-5.505324,2.836100,1.091275,-7.714180,2.262584,3.643221,-6.918946,-4.277858],[4.968143,-3.888549,-3.845126,-2.099213,-4.132859,-7.512009,-4.113493,-2.511040,4.189769,7.292223,0.575451,-9.369407,-8.955492,-7.483390,-0.132337],[4.766605,3.734843,8.044814,8.479961,-3.466325,-9.318522,-6.700174,8.947706,-8.399820,-8.954817,9.189558,6.021985,-4.210426,-8.366542,-0.147371],[1.996432,-7.760073,8.992701,-5.996456,5.801458,-0.769697,-1.351211,5.331737,-5.522675,-0.161051,6.012712,-0.726953,-8.150275,7.406270,-9.668073],[6.408593,1.186235,-2.429833,-3.075176,0.315405,3.833568,2.776548,-6.066533,0.332350,-9.214969,8.647429,0.077541,-7.256157,1.252559,-3.320952],[7.304714,2.886857,4.775585,2.867018,4.637217,-3.074376,4.627725,-6.772869,-9.978797,-2.894674,3.609802,-2.319463,4.001030,-7.108160,-6.621232],[-4.174913,0.176322,-3.428524,8.647466,-2.961479,9.879180,5.051970,-1.382028,-4.538969,5.780068,-8.064017,6.075446,-3.844532,9.649152,1.450783],[1.473637,-1.049791,5.095024,-5.161694,-2.200990,7.520825,5.218736,-6.155493,-2.862760,-2.848286,5.814755,4.625403,2.602808,-3.259777,-6.534421],[4.514785,4.850186,-3.075966,-3.903740,-1.300915,7.414814,-9.750100,-7.055147,3.471440,-8.014184,8.005512,-9.315033,-7.969622,-9.743587,-6.980158],[-8.966168,-4.203914,8.702843,-8.427058,2.406998,7.015485,3.059586,3.582927,-5.030075,-8.433423,-8.700609,4.732212,-1.997509,8.814090,-3.840142],[-0.100936,1.882376,-0.430644,1.248708,-5.739884,6.587940,-9.437209,-9.258747,7.851212,-5.494066,3.428338,4.640522,2.779037,-2.860057,-9.081916],[-6.938616,8.030204,5.413032,0.092366,-4.333839,-5.942417,2.909154,-7.603904,-8.312010,-6.006717,-7.901271,-5.644353,-2.225325,6.128772,-0.924340],[3.503048,-1.716831,-4.343467,6.550781,4.617827,7.491317,1.974614,-5.160775,-8.800961,3.325491,7.458907,-9.492390,7.798018,4.273306,5.002071],[-4.535480,-3.134964,3.512198,7.707913,-5.640946,1.053874,-1.321029,-9.696352,-5.395253,0.407867,-6.522878,5.589354,-2.536041,7.292011,-4.878348],[0.935333,-0.535672,7.645752,-2.958183,-3.124807,0.455099,7.697970,-2.988180,-8.116961,-2.501545,9.009677,-5.453921,-7.776790,2.560256,-4.628045],[-9.102082,9.644383,-7.829614,0.204050,8.623585,3.454595,2.771439,-2.025629,6.784804,-6.684975,-4.353465,-2.898996,6.358165,-9.445451,-1.894132]], dtype = "float64")#candidate|7941|(135, 15)|const|float64
var_7942 = relay.var("var_7942", dtype = "float32", shape = (1, 315))#candidate|7942|(1, 315)|var|float32
call_7940 = relay.TupleGetItem(func_2190_call(relay.reshape(const_7941.astype('float64'), [2025,]), relay.reshape(var_7942.astype('float32'), [315,]), ), 0)
call_7943 = relay.TupleGetItem(func_2193_call(relay.reshape(const_7941.astype('float64'), [2025,]), relay.reshape(var_7942.astype('float32'), [315,]), ), 0)
output = relay.Tuple([call_7891,call_7900,call_7902,call_7916,call_7936,const_7937,call_7940,const_7941,var_7942,])
output2 = relay.Tuple([call_7892,call_7901,call_7903,call_7917,call_7938,const_7937,call_7943,const_7941,var_7942,])
func_7954 = relay.Function([var_7942,], output)
mod['func_7954'] = func_7954
mod = relay.transform.InferType()(mod)
mutated_mod['func_7954'] = func_7954
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7955 = relay.var("var_7955", dtype = "float32", shape = (1, 315))#candidate|7955|(1, 315)|var|float32
func_7954_call = mutated_mod.get_global_var('func_7954')
call_7956 = func_7954_call(var_7955)
output = call_7956
func_7957 = relay.Function([var_7955], output)
mutated_mod['func_7957'] = func_7957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7790_call = mod.get_global_var('func_7790')
func_7792_call = mutated_mod.get_global_var('func_7792')
call_8002 = relay.TupleGetItem(func_7790_call(), 0)
call_8003 = relay.TupleGetItem(func_7792_call(), 0)
func_4298_call = mod.get_global_var('func_4298')
func_4300_call = mutated_mod.get_global_var('func_4300')
call_8014 = relay.TupleGetItem(func_4298_call(), 0)
call_8015 = relay.TupleGetItem(func_4300_call(), 0)
func_1845_call = mod.get_global_var('func_1845')
func_1848_call = mutated_mod.get_global_var('func_1848')
call_8016 = relay.TupleGetItem(func_1845_call(relay.reshape(call_8002.astype('uint64'), [2, 16, 4])), 0)
call_8017 = relay.TupleGetItem(func_1848_call(relay.reshape(call_8002.astype('uint64'), [2, 16, 4])), 0)
output = relay.Tuple([call_8002,call_8014,call_8016,])
output2 = relay.Tuple([call_8003,call_8015,call_8017,])
func_8018 = relay.Function([], output)
mod['func_8018'] = func_8018
mod = relay.transform.InferType()(mod)
output = func_8018()
func_8019 = relay.Function([], output)
mutated_mod['func_8019'] = func_8019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_8140 = func_6154_call()
call_8141 = func_6154_call()
output = call_8140
output2 = call_8141
func_8147 = relay.Function([], output)
mod['func_8147'] = func_8147
mod = relay.transform.InferType()(mod)
output = func_8147()
func_8148 = relay.Function([], output)
mutated_mod['func_8148'] = func_8148
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8163 = relay.var("var_8163", dtype = "float32", shape = (16, 3, 1))#candidate|8163|(16, 3, 1)|var|float32
uop_8164 = relay.atan(var_8163.astype('float32')) # shape=(16, 3, 1)
func_1597_call = mod.get_global_var('func_1597')
func_1598_call = mutated_mod.get_global_var('func_1598')
call_8166 = func_1597_call()
call_8167 = func_1597_call()
func_6520_call = mod.get_global_var('func_6520')
func_6522_call = mutated_mod.get_global_var('func_6522')
const_8181 = relay.const([-0.906798,9.699835,3.897076,1.217902,0.525229,7.944505,2.646559,-9.342096,-9.111151,2.022879,6.086685,-1.836103,-8.279756,3.325755,-6.569164,-4.791161,-6.734486,9.384535,2.378778,-4.718873,-9.113363,0.059415,5.340598,9.060858,2.936819,2.900189,-7.602071,6.947218,6.686448,3.905026,-0.822278,-8.846699,8.647110,-1.265491,-1.266599,9.815019,-6.941515,3.620943,6.345934,2.361830,0.323421,2.556052,2.480520,-1.107969,-1.160511,-3.317994,-2.127444,2.867986,-8.371942,-0.210810,-7.075447,-7.230011,-0.606500,8.078550,-4.235772,2.274618,7.628153,-0.749063,8.935571,2.666513,-6.452159,-5.570865,1.419181,-6.546005,0.232076,-9.414810,-4.266581,7.521727,-7.521377,-7.680972,7.575054,-9.191899,1.203991,0.278035,-9.866821,-7.192736,-7.131518,1.480459,-5.637552,-3.651189,-5.390351,-9.044585,6.338342,6.429627,-7.235482,-2.188683,7.800050,-8.724367,4.177832,-1.057720,7.721338,-1.912682,8.114518,9.778167,3.378690,-6.632761,-7.245394,5.978978,-3.237049,-2.729662,-3.705953,-0.034609,0.858765,-5.461609,1.628208,-3.753666,8.009157,-6.765191,-8.863054,3.085943,3.672127,2.642688,-8.144443,5.483581,-8.617391,3.920301,2.895161,-2.724700,-9.608215,0.401829,0.917255,-8.616937,4.275574,-9.205490,-5.625514,9.195750,4.001786,-3.588338,4.065421,-2.997336,0.666377,4.231345,5.265078,0.936691,-3.423907,0.767922,8.625032,6.453395,9.887308,-6.203738,3.616025,5.523059,9.473282,-7.362120,-6.254247,-1.380744,-3.303319,-4.681264,6.485107,0.998677,-5.005288,-1.146983,7.495543,-8.193868,2.939724,-7.164540,6.411057,5.374021,3.041074,5.785695,-7.154112,6.509039,7.141780,-9.605355,-1.582919,2.760908,7.134340,-2.996230,0.942780,1.927039,8.876868,3.882763,7.649476,4.680159,-2.224641,-7.978265,-9.523948,2.491967,8.629367,9.656554,8.591972,5.479155,-3.068280,2.686030,-7.593453,-9.923287,5.982314,-2.252921,-7.022645,2.200890,6.793957,4.758156,-5.372081,1.340903,-6.710413,8.025226,3.479477,-5.397681,-4.570565,4.265673,-4.810428,-4.465729,6.020140,7.676379,2.514155,-5.987285,-4.152607,-9.364240,-8.977495,2.208392,-4.182176,0.206071,6.152507,4.335089,3.492943,-6.762354,-2.640024,6.867729,-4.138565,8.287810,-1.041430,-8.571856,1.406845,9.323514,-3.765376,3.411383,5.590324,8.165413,-5.687917,-7.292097,6.385455,-2.218031,2.859927,-8.236520,-2.647727,8.012230,8.221249,2.121452,8.420392,1.215598,5.106981,-3.331550,8.371326,4.077262,3.605044,7.335486,8.581194,-9.812595,-2.239253,-2.607947,5.098392,0.959344,8.419606,8.862696,1.183145,-9.360023,2.415465,2.008981,-3.936578,1.638805,-9.061482,0.093723,-8.158341,-3.309864,-4.472053,1.519039,1.378260,-9.146036,2.967417,3.574851,-0.569470,-4.694071,-0.296358,-7.113679,-2.483957,-5.597001,9.491291,-2.681248,-6.431146,-4.027934,6.873692,-9.420730,-8.899679,6.019308,-1.061522,-1.764161,6.510484,9.788155,-7.582241,-5.362179,2.762513,9.054162,-0.700547,-3.767723,-2.960556,9.536023,-9.061453,-2.722786,0.757444,-1.480977,-6.191886,-6.481467,9.369787,-2.172277,-6.592138,9.124945,2.289559,-3.280716,-3.718707,-6.885831,5.920693,8.184284,2.160927,-6.703390,9.862576,8.579686,3.933890,8.345646,2.028550,-7.079409,8.540279,5.969896,-8.272624,-6.667686,-1.278534,4.532894,1.360702,8.215217,0.054560,7.480309,-5.773660,-1.731278,-6.005678,0.166346,2.324947,6.926434,0.177176,-0.398689,-2.824126,-4.740478,8.563256,-9.223607,-1.461865,-6.849459,8.784463,8.344807,-9.224073,4.787490,1.168700,-2.387646,-2.522332,6.815729,-8.782813,9.816971,4.652988,1.272404,-3.346768,3.291434,1.869769,-4.008091,6.329082,-2.666904,5.118765,-5.472792,-2.415860,-4.447797,8.148885,-7.199494,8.220821,-6.163881,-3.270440,7.266696,-0.098088,5.441039,-2.555669,-6.267101,8.517866,3.145272,2.619048,-5.638934,-2.862132,-6.859112,-3.682348,0.685941,9.292209,-1.795708,0.485780,-6.908681,-0.099562,9.670229,2.690878,-3.915716,9.210860,0.744765,-9.033042,-4.981688,-1.180081,-8.507914,-5.645238,-2.738748,1.872176,4.956219,9.090059,-6.859325,8.934208,-8.023338,-5.603779,-5.826783,9.728821,-3.671171,6.863178,-6.403592,0.531456,-1.240434,7.156362,6.116087,-4.731879,8.797087,-5.075377,4.552217,-5.586364,-2.466510,2.748911,-5.603931,8.939444,-2.025069,0.219175,-6.840218,7.888978,-5.262948,-0.641145,8.046818,-8.480982,-8.068047,4.332330,9.176940,5.963415,-5.745640,-4.278381,8.887618,4.556146,-4.924758,4.788964,7.891600,6.680045,2.278282,-6.545723,-9.875096,7.373328,4.256646,8.994021,-0.558440,8.845170,5.865372,5.933450,7.807089,-9.454502,-9.647631,-3.615110,-1.014927,6.213723,6.166127,-3.002134,9.032668,-7.301587,-6.902528,4.611444,3.800991,0.511396,-6.448709,3.478137,3.908434,0.794734,6.697770,-1.876548,7.032616,8.775421,2.263238,8.782998,-2.648810,3.334151,1.102498,0.684166,0.615282,2.997318,-4.446258,7.419479,-1.240319,7.099759,8.867340,0.208277,2.266558,7.575204,-0.599152,2.272543,5.011020,-6.055281,9.652456,5.824444,-1.689266,-7.510218,8.361188,9.232734,-5.079516,-0.586410,-6.493723,8.165479,-2.759819,-6.699592,1.271782,5.994204,-8.215239,7.615421,-5.416313,8.477369,8.104332,0.474518,5.673155,-0.993007,8.139711,9.565668,-7.297386,8.182286,-9.933309,0.869962,-5.745040,-3.449655,-9.807619,-5.869279,-1.364234,-7.730735,-1.405359,-1.620202,-7.723020,5.368708,9.814619,2.428232,6.973177,0.552712,-0.142541,4.061456,9.438347,6.366277,3.882766,-9.835860,9.523150,0.928627,-5.737142,-3.234656,-5.798137,-3.975494,-1.648140,4.179465,0.998700,9.684347,-2.965478,-4.634651,-7.117785,2.064094,2.416237,7.216417,-9.983643,-7.231305,1.711896,5.509824,3.511160,2.023284,5.072560,2.493015,8.274477,-5.492441,-0.323094,-4.228112,4.725016,-9.786134,6.468470,8.600267,4.749734,8.675879,-6.885080,-6.086720,-4.700238,-1.760747,3.688463,-2.486218,-8.680685,-3.849965,7.825572,-7.339772,-9.175165,-3.110706,-8.265805,-0.845400,0.354516,-0.970016,-3.538507,9.161285,3.418030,7.173914,-0.853190,0.975959,-2.609819,6.150723,-7.665823,-5.559514,-1.405691,7.876933,6.517190,-9.604197,9.162344,-9.507649,-9.315108,-5.418809,9.849820,-3.037500,-3.173429,5.536597,6.814106,-9.649827,-3.771694,-2.191184,6.871724,8.795152,5.261860,-3.192008,5.226917,4.997997,-3.057627,6.140979,1.594625,9.582559,3.220435,-5.824278,5.515018,3.343169,-2.144998,7.261179,0.615314,-3.327154,-6.666410,5.095470,1.547404,3.361738,-4.709178,-6.694373,-5.662623,3.414117,-7.574128,-7.212727,8.690700,1.271836,-0.946406,8.371049,9.390102,-8.523458,-3.006233,2.406309,-7.639775,-5.076080,0.783058,-6.776197,-1.400457,-8.148426,-5.049319,9.123978,-2.701466,5.521779,9.555728,-1.263396,-7.896428,-7.437455,-6.354169,-5.191177,8.830778,3.989999,0.945686,-3.666630,-8.721360,-5.522934,-0.272650,-8.927492,-7.206032,7.106517,-4.446522,7.875223,-4.287234,-7.876580,7.776945,-8.207552,8.726047,-5.132059,2.893237,-1.393803,3.309348,-0.448920,-3.459827,-2.230907,-8.816664,-0.834188,0.116676,9.645404,-7.441846,-3.181152,1.393487,-6.987926,-2.625434,7.393505,1.886920,7.338326,4.563679,-0.309414,-2.331434,-4.084475,-2.131913,-0.022817,-7.565635,-4.915874,6.818377,5.471912,3.192568,2.326623,-8.512460,7.872909,-7.707784,-1.152019,2.632911,-0.416148,2.740493,-3.254726,3.257196,6.766984,4.774757,-5.901520,-3.383860,4.550965,0.946283,4.333017,9.026697,-4.196507,-9.882129,8.897514,8.714147,0.896774,0.804776,2.302670,-5.160790,-5.744692,-6.243753,-4.795412,-0.093740,-5.608063,-5.244189,9.527353,-8.471901,-0.421737,-9.786249,-0.410824,8.273847,-8.878268,-3.730021,1.274535,-2.788679,-2.773378,3.691747,0.289253,-4.943473,4.064444,-1.758712,-9.970705,-3.829821,5.859426,6.028748,6.727344,6.848259,5.591209,9.452855,2.690470,-9.672131,-1.988741,-7.554075,-0.654928,2.368638,-3.112632,-2.479164,-2.814153,6.481383,-3.362507,-9.960763,4.349334,5.903366,4.338759,1.112194,2.286363,-4.590637,3.563645,2.700133,3.156064,-3.573487,-0.560579,-9.676976,3.127166,-8.337325,-1.466361,3.558748,1.529023,-1.930957,7.004438,9.535926,-4.558054,-6.228821,-4.419594,7.674518,-3.505639,1.644405,-9.020515,-6.598256,0.259493,6.996265,6.030022,1.737867,-1.556854,5.628740,-3.079547,-2.049584,-6.818557,-2.794657,-4.714769,-4.910064,7.910993,-6.740144,7.317359,-5.744938,5.305869,6.372059,-4.214710,8.407018,-3.029690,0.051560,0.833015,1.014352,-5.946286,8.308945,7.083706,-4.168689,0.815544,2.891919,9.449889,-2.186150,2.289474,0.975215,-1.801442,-1.290362,1.432352,7.784986,2.088132,-7.301888,6.427799,1.679754,1.414192,8.454259,-1.147269,3.056485,-8.319769,-7.061435,5.755130,-8.874308,3.261156,5.869109,-4.400351,8.395189,2.667117,0.561881,7.051814,-4.274281,-4.433707,-4.941923,-6.692102,-8.125567,4.092885,-8.307585,-6.928671,-9.365618,-9.155079,-1.542060,7.100458,-8.118146,8.969624,0.797514,-9.793607,8.556860,5.977041,0.475028,-6.743555,4.983669,8.161915,-9.645563,-6.934111,1.881479,-2.653975,2.313205,8.426294,3.974865,5.526176,-5.951624,-7.945503,8.598210,1.479863,9.300267,-3.050093,9.293929,-8.289712,-2.637920,-4.971505,2.558903,6.628528,-1.083560,3.008696,-8.899599,-6.061319,-5.644377,-0.167634,7.154832,1.132286,2.516156,0.257745,7.700146,0.202112,-5.730950,2.192928,-5.442156,-0.217334,2.677461,-5.459572,-9.592083,-2.910308,1.000506,-0.255095,-1.721076,4.094342,-4.578274,-7.039666,3.021836,5.970475,-3.825043,1.137597,1.503016,6.873337,0.075375,-7.414844,4.125426,4.005618,-2.024988,2.932417,4.176072,-8.845450,8.413643,2.549314,-2.290962,-7.511974,7.852364,-8.119907,0.939075,6.258228,6.606991,-8.540720,4.141444,-9.269290,-8.389095,-5.120421,-8.940381,8.086609,-0.904599,-9.464182,8.408380,4.455948,3.815085,0.793122,8.045760,3.226171,5.092747,9.742405,7.440882,-3.665619,9.467005,8.433570,6.704908,7.129127,8.021224,9.306188,-1.840812,2.597677,-5.853170,-5.115805,-8.079042,-8.673463,-2.117716,-6.463312,8.287056,9.067335,3.688439,1.511639,1.803877,-4.373508,-9.897025,8.165071,-9.574709,-0.836225,0.902993,0.235856,4.428220,1.544086,5.214649,4.464294,-2.173998,-5.228220,-4.469734,8.152671,-9.231182,-3.202278,6.564414,-6.052663,9.513673,-4.361336,8.185786,-2.193345,8.024435,-3.653991,4.831783,-0.441317,-6.340262,9.178785,-9.176186,-8.689647,8.068009,6.239284,-0.413040,-4.430967,0.089924,2.717837,-2.388867,9.578397,1.804359,8.393853,9.194648,2.054068,-3.333031,-7.678739,6.605817,8.631220,-3.818598,6.761757,-9.125510,-7.019398,-9.824684,8.773246,4.314166,-2.949843,-7.867923,2.478006,9.941246,-3.120162,1.347371,-5.884455,2.322720,6.318190,4.504528,9.001320,4.422510,7.348799,4.497064,-4.318696,9.510752,0.483067,-0.200682,0.987171,5.753774,3.306947,2.262833,4.540824,-0.031353,-8.064791,0.348121,3.040902,9.986178,-0.529057,4.362181,2.849597,-6.639511,6.368341,6.519640,-9.880218,-7.016457,1.639977,-3.152537,-0.270883,-5.970660,-4.856131,-0.315823,-2.596033,-6.831690,-9.470133,7.896301,-8.741121,4.599413,5.945934,-5.583474,8.127786,3.261516,-9.024180,-7.509138,-1.126252,8.105178,-5.784659,5.915479,6.363410,-9.173782,9.919533,9.491490,1.640398,3.589673,1.696807,-9.866074,-1.138769,-0.158267,3.888753,-9.253577,2.980483,-1.531914,2.608938,-3.887493,5.367997,3.584405,-5.275853,-3.706734,1.101663,-8.952051,-7.583316,9.135248,0.963903,1.100671,-9.114601,-7.554762,-6.511049,-4.278755,-4.380606,-2.971100,9.158694,7.836969,0.217232,4.177706,2.449562,0.855474,-7.182063,5.162739,-4.927615,6.396253,-1.424600,-4.398762,-0.425297,-5.810227,2.546610,2.007924,-4.666864,7.195075,-5.164072,-1.001737,-7.049821,8.999242,8.612781,-4.021349,-0.274277,-9.426709,-3.613728,4.050086,9.768607,2.890495,-5.183992,9.470804,4.589873,-3.049751,0.575590,-1.873552,5.332524,3.667368,-5.417889,-7.244970,6.670853,0.405639,-5.095284,-1.649744,-4.980768,-6.407932,-1.222039,-6.965141,-7.247200,-0.054043,6.384145,-1.840475,-4.139386,8.545750,0.310998,0.992995,0.062118,-5.266830,2.764788,1.369143,6.939325,3.146413,-6.554124,8.002766,-6.343938,-7.749230,-2.545984,-9.587256,-6.972160,4.547550,-6.240043,-6.613270,0.815216,3.704810,-3.537011,1.257038,-9.955626,3.275197,-8.208274,-1.891178,-2.665908,-4.167970,2.869753,-7.205467,6.100861,0.361303,-2.117488,3.504972,8.058611,6.131557,5.752013,1.130962,3.519342,-4.867810,1.663889,-8.099697,-9.112765,9.701702,-8.093623,1.748320,1.957111,5.440443,0.527723,-4.808827,6.528833,-3.372658,-1.204174,-0.062194,-8.286816,7.277592,6.567850,-2.896206,-2.656292,2.628571,6.624686,-4.501619,-4.644840,-8.340098,-4.279290,-1.405824,-9.749331,9.325557,-2.555114,-5.368214,-1.958017,-7.186270,-2.826808,8.002244,-5.107060,6.523399,-0.721487,6.194547,1.122370,-9.637831,-8.073849,1.922947,6.336567,7.749010,-1.377660,-6.549893,5.897242,5.540164,2.168626,-4.782469,5.286067,4.061468,-7.374368,-9.115297,9.643344,0.534797,8.372377,-6.036483,9.268508,-8.564131,-2.645892,5.277517,-4.121222,3.893885,5.896018,7.474024,2.787050,-0.790713,1.878292,3.953790,4.991274,-1.760461,7.456140,3.505700,-2.479799,-9.803226,7.508988,-2.393606,-3.554192,6.215584,-8.793870,6.445019,-0.028799,8.976379,-0.928213,-0.606685,8.885543,0.263722,0.800391,-8.649319,-4.953558,-4.058165,-4.241835,4.308548,-4.654837,-4.098975,-8.216800,-7.159949,-5.975966,-2.402535,-4.583065,-8.555445,-5.538600,-8.771623,3.829509,7.027343,-0.508061,9.450248,2.605515,4.243735,0.937676,-2.842284,9.221303,-4.023177,-4.189670,6.954618,7.887295,-9.772883,2.916912,-2.739512,9.079244,-1.210835,7.152662,-0.315798,4.028244,1.862497,-4.886935,-2.981484,-3.007044,1.576768,2.848797,-2.512391,-8.353027,-2.483890,1.339431,-4.519225,6.542093,-3.024139,-6.811103,5.310055,6.497305,9.871481,-4.304802,1.317382,-0.016624,5.440771,5.513879,4.189686,-9.543706,8.961155,-3.064712,1.670425,1.759133,-7.079509,-9.100938,3.534142,-9.516382,9.839258,-5.830510,-9.763595,9.918376,-5.231815,7.148202,5.402399,-3.289331,5.707847,-0.726352,-0.551264,5.388267,-1.758456,-0.205351,6.058813,-8.179584,8.754526,8.039193,0.980983,2.913224,-5.844376,4.668578,-5.612123,-4.461668,-5.056159,-3.302300,-6.896047,-8.633470,-3.912875,-1.838295,8.814739,-0.244818,1.065336,-9.055410,8.262803,2.758945,-7.182281,3.217667,-6.137184,4.819908,-6.352331,8.832425,1.317196,2.420427,-1.169201,7.209786,-0.908142,-0.555268,6.892452,9.693676,-4.810451,-6.766182,4.030385,9.428348,-1.188637,1.073993,0.124742,2.589538,-5.442528,-7.958410,5.243582,-3.772573,9.853060,3.169105,-9.460165,1.948670,5.691305,8.066066,8.966700,-3.153916,7.529174,7.674466,-6.255973,6.481354,1.377516,5.524000,8.408396,4.437029,-6.569186,-6.016076,5.018971,0.240579,9.984296,2.657429,-4.365706,-9.266658,0.191581,-6.442557,1.654150,-1.440862,9.661088,5.116327,-0.923063,0.946782,6.138606,5.504827,-5.334430,-3.428115,6.546037,-5.433892,3.875506,-8.827269,-8.736950,0.881018,-6.038775,4.143587,5.506442,8.151083,8.095412,3.551060,-1.561047,2.604353,5.000013,-5.831000,8.216133,-1.782796,-9.721979,-5.389346,2.371408,-0.594364,6.272059,4.819110,-5.351532,-1.031584,-5.196710,-8.219738,-9.969476,8.284008,8.480404,2.783870,-5.993323,-7.461392,-6.178002,-0.996710,-9.890301,9.496325,-1.074101,-6.927725,2.738483,-1.088993,-2.286768,-6.275135,-0.577164,4.526816,-7.584291,-1.938733,-9.485586,3.530280,8.226657,7.252117,-6.095640,-3.239162,2.004918,4.119446,1.368279,-5.817648,-1.806308,2.299645,-7.254265,3.903794,8.787160,-6.342778,-7.386671,-9.933746,9.041200,0.469725,-3.650928,-1.581574,-4.650085,6.524588,0.008357,-7.985839,-2.560919,-1.092652,-8.640832,2.380370,1.647152,1.477935,6.072055,-3.829835,5.428935,-4.383896,9.050943,-8.861523,-8.411772,8.849539,8.470260,-6.571268,1.142257,3.517675,-6.726479,3.398042,-6.886515,1.104580,-9.704371,-3.783040,0.802935,-8.483978,2.173286,-0.181964,-8.914243,5.423696,0.012036,5.284730,-4.527750,-3.808677,-1.500794,-9.255893,3.306455,-2.248701,3.725832,3.028169,-1.624707,0.449711,-8.277866,3.911274,-9.848854,7.446340,-9.873540,-9.390462,1.991307,0.815836,8.389079,-2.558194,6.206454,-2.439331,4.178598,3.868846,4.190568,7.553039,0.059925,-3.743168,4.533772,1.817122,3.311295,-8.053344,7.540831,-3.307592,3.707828,1.068911,2.326231,-7.661789,0.157591,-6.583610,-0.079689,6.712433,6.723329,1.617501,9.016336,-5.122215,5.228354,7.187772,3.901357,5.704360,-5.882721,5.332240,-8.520571,-1.246598,-0.244881,5.304858,-6.973829,-0.724619,-5.066886,-1.076123,-7.624748,-5.358016,6.602357,-5.728560,2.370780,9.606535,-9.981266,-2.277562,-5.874221,2.492226,4.908044,-8.222310,1.484500,3.206509,-7.487735,5.071820,7.658194,-0.313354,8.524224,0.646579,-1.426622,-9.932233,5.914185,-3.354680,9.457716,-1.029647,-4.893645,-3.618560,3.175309,0.973633,6.928127,9.935490,1.458842,8.883224,-7.467924,9.035370,2.208361,-1.422226,-5.783445,1.437109,-4.484303,4.804848,-2.252108,-5.837070,3.620847,4.856545,-2.016647,0.199703,8.214583,-3.998064,3.006589,-9.421388,1.714719,-0.184151,1.478439,3.680098,3.104967,-0.253738,-2.149904,-6.613952,9.311257,-0.855841,-9.661173,5.592984,-3.321340,8.101155,5.375501,-3.061208,-6.125111,5.557130,-0.842202,8.235680,3.598105,3.910856,-1.465383,3.764630,-9.845136,4.257683,-5.866502,-5.944486,-5.676890,-0.005031,3.621464,-7.951158,7.926527,-9.449159,-7.870633,-4.066049,4.699198,7.805451,0.415965,1.386838,-1.249312,-0.225437,4.171913,7.541464,-1.959878,-0.693057,7.564908,-8.594242,-6.544820,-1.553017,-6.942564,-4.628067,7.566269,-7.184455,-4.177658,-1.480674,-6.418140,1.080529,3.061672,-6.338531,9.226372,7.359692,6.770970,8.664453,-0.167258,2.191370,-0.699583,0.853690,7.587862,-3.470400,2.330101,9.836304,0.452954,-2.543653,0.329272,0.044683,2.510684,0.618135,-9.515663,-5.701282,2.944858,8.425395,5.703491,5.394235,-1.799042,-5.303150,-7.475788,-2.011425,8.349893,-1.822328,9.010518,1.542556,-7.144548,2.418132,7.457641,-6.427312,1.933016,6.655136,-7.781704,-7.726088,-0.767927,-9.303935,-7.528132,7.184628,4.620958,-7.265934,7.458590,9.178870,9.444399,-8.731659,-8.348529,1.554372,-2.580133,-7.075263,7.889821,-0.152361,-3.726171,-3.692140,4.668862,-6.722115,7.254151,0.598939,-7.629046,-8.497948,2.359640,-5.946196,8.493186,-6.629388,-9.942148,-8.338747,8.310403,-7.083893,-1.337332,-8.188409,-5.370269,-1.553635,4.487903,-0.080356,0.283133,6.217569,6.069974,-8.251111,7.153436,-5.216946,-9.250323,9.979644,3.545178,9.070456,-6.665658,4.677362,-7.527163,-9.018118,9.525849,8.265751,-8.727040,-6.559760,-3.880591,-6.848381,4.333107,-2.853851,-5.067378,6.658778,3.341895,9.244131,-7.685832,-0.739714,-5.896719,-2.453326,1.196328,-5.137392,9.436754,1.893662,-6.348345,3.641439,-2.708073,1.947910,-6.033888,1.969655,1.978490,3.890382,9.004681,-1.560591,3.328931,-6.683503,-5.044719,-3.183639,3.391230,3.269854,6.949535,7.080765,-6.611347,-1.276151,9.928582,-2.409998,-8.675869,-5.687971,5.542515,-6.910083,1.632469,2.790989,8.343959,7.801899,6.919494,-6.118620,-6.790486,9.127314,-3.686260,7.594445,3.840148,-9.963142,5.486572,7.808811,6.718434,6.300976,-4.645463,-7.694498,-8.096041,-0.541972,3.175190,2.322067,-8.116631,-7.823225,-8.209058,-5.736562,-3.357794,-1.106841,2.742360,-6.350354,4.975722,-9.727505,5.966006,5.305242,-5.419937,3.016344,9.104450,8.374869,0.023479,-7.679844,6.681997,5.844767,-7.750132,-5.778291,-7.793099,-7.340864,-1.914527,0.013675,-2.200632,-4.402646,3.393179,-9.130238,-4.389994,-4.623004,5.192994,3.082539,-3.698773,-1.801974,-8.992710,-5.377419,-3.500347,-0.486589,9.943999,-2.290474,4.907642,3.826535,-4.315345,4.704262,2.029816,5.390013,-7.319909,-1.243468,0.240619,2.540184,2.979723,-2.916230,9.190088,-9.403188,6.322269,-5.528905,4.207043,5.450102,6.085034,-9.291560,-5.177318,0.296045,3.719549,9.948098,5.931149,-4.788620,0.627311,-7.463689,-0.908988,8.686213,0.195067,-3.405385,0.273137,-0.766138,-2.315825,-2.840611,-2.663507,9.233722,0.491018,9.390427,-4.194938,5.477437,-5.926167,-5.332780,-5.486028,-5.469858,5.005951,1.590763,-6.653929,2.828771], dtype = "float64")#candidate|8181|(2025,)|const|float64
call_8180 = relay.TupleGetItem(func_6520_call(relay.reshape(const_8181.astype('float64'), [9, 225])), 1)
call_8182 = relay.TupleGetItem(func_6522_call(relay.reshape(const_8181.astype('float64'), [9, 225])), 1)
bop_8196 = relay.less_equal(uop_8164.astype('bool'), const_8181.astype('bool')) # shape=(16, 3, 2025)
func_3563_call = mod.get_global_var('func_3563')
func_3565_call = mutated_mod.get_global_var('func_3565')
var_8212 = relay.var("var_8212", dtype = "float64", shape = (1386,))#candidate|8212|(1386,)|var|float64
call_8211 = relay.TupleGetItem(func_3563_call(relay.reshape(var_8212.astype('float64'), [9, 14, 11])), 0)
call_8213 = relay.TupleGetItem(func_3565_call(relay.reshape(var_8212.astype('float64'), [9, 14, 11])), 0)
func_6096_call = mod.get_global_var('func_6096')
func_6098_call = mutated_mod.get_global_var('func_6098')
call_8216 = relay.TupleGetItem(func_6096_call(), 1)
call_8217 = relay.TupleGetItem(func_6098_call(), 1)
output = relay.Tuple([call_8166,call_8180,bop_8196,call_8211,var_8212,call_8216,])
output2 = relay.Tuple([call_8167,call_8182,bop_8196,call_8213,var_8212,call_8217,])
func_8218 = relay.Function([var_8163,var_8212,], output)
mod['func_8218'] = func_8218
mod = relay.transform.InferType()(mod)
var_8219 = relay.var("var_8219", dtype = "float32", shape = (16, 3, 1))#candidate|8219|(16, 3, 1)|var|float32
var_8220 = relay.var("var_8220", dtype = "float64", shape = (1386,))#candidate|8220|(1386,)|var|float64
output = func_8218(var_8219,var_8220,)
func_8221 = relay.Function([var_8219,var_8220,], output)
mutated_mod['func_8221'] = func_8221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8147_call = mod.get_global_var('func_8147')
func_8148_call = mutated_mod.get_global_var('func_8148')
call_8261 = func_8147_call()
call_8262 = func_8147_call()
func_3803_call = mod.get_global_var('func_3803')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_8296 = func_3803_call()
call_8297 = func_3803_call()
func_3803_call = mod.get_global_var('func_3803')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_8315 = func_3803_call()
call_8316 = func_3803_call()
uop_8323 = relay.log(call_8261.astype('float32')) # shape=(2, 16, 4)
uop_8325 = relay.log(call_8262.astype('float32')) # shape=(2, 16, 4)
output = relay.Tuple([call_8296,call_8315,uop_8323,])
output2 = relay.Tuple([call_8297,call_8316,uop_8325,])
func_8335 = relay.Function([], output)
mod['func_8335'] = func_8335
mod = relay.transform.InferType()(mod)
output = func_8335()
func_8336 = relay.Function([], output)
mutated_mod['func_8336'] = func_8336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8147_call = mod.get_global_var('func_8147')
func_8148_call = mutated_mod.get_global_var('func_8148')
call_8346 = func_8147_call()
call_8347 = func_8147_call()
output = call_8346
output2 = call_8347
func_8348 = relay.Function([], output)
mod['func_8348'] = func_8348
mod = relay.transform.InferType()(mod)
mutated_mod['func_8348'] = func_8348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8348_call = mutated_mod.get_global_var('func_8348')
call_8349 = func_8348_call()
output = call_8349
func_8350 = relay.Function([], output)
mutated_mod['func_8350'] = func_8350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2385_call = mod.get_global_var('func_2385')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_8357 = func_2385_call()
call_8358 = func_2385_call()
func_7055_call = mod.get_global_var('func_7055')
func_7059_call = mutated_mod.get_global_var('func_7059')
const_8361 = relay.const([[True,True,False,True,False,False,False,False,False,False,True,False,True,True],[False,True,True,False,True,True,True,False,True,True,True,False,True,False],[False,False,True,True,True,True,False,True,False,True,True,False,True,True],[False,False,False,False,True,True,False,False,False,True,True,True,False,False],[True,True,False,True,True,False,False,False,True,False,True,True,True,True],[True,False,False,True,True,False,True,False,True,True,True,True,False,False],[False,True,False,True,False,False,False,False,False,False,False,False,False,False],[True,False,True,True,False,True,False,True,True,False,False,False,True,True],[True,False,True,True,True,True,False,True,True,False,True,False,False,False],[False,False,False,True,False,True,False,True,False,True,False,True,True,False],[True,False,True,False,False,False,True,True,True,True,True,True,True,False],[True,True,False,True,True,False,False,False,True,True,True,True,False,True],[False,True,False,True,True,True,True,False,False,False,True,True,True,False],[False,False,True,True,True,True,False,True,False,True,True,True,False,False],[True,False,True,True,True,True,True,False,True,False,False,True,True,False],[False,False,False,True,True,True,False,False,True,True,True,True,False,False],[False,False,False,True,False,False,True,True,True,False,True,False,False,False],[True,True,False,False,False,False,True,True,False,True,True,True,False,True],[False,False,True,False,False,False,False,False,False,True,True,True,True,True],[False,True,True,True,True,True,True,True,True,False,False,True,False,True],[False,False,False,False,True,False,True,True,False,True,False,False,False,True],[True,True,False,True,False,True,True,True,False,False,False,False,True,False],[True,True,False,False,True,False,False,False,False,True,False,False,False,False],[False,False,True,False,True,False,True,False,True,False,True,False,True,False],[False,False,False,True,True,False,True,False,True,False,True,True,True,True],[False,False,True,False,False,False,False,False,False,False,False,False,False,True],[False,True,True,False,True,False,True,False,False,True,True,True,True,False],[True,False,True,True,False,False,True,True,False,False,True,True,False,True],[True,False,False,True,False,False,True,True,False,False,False,False,True,True],[False,False,True,True,True,False,False,True,False,True,False,False,True,True],[True,True,False,False,False,True,True,False,True,False,True,True,True,True],[True,False,False,True,True,True,False,False,True,False,True,True,False,False],[False,True,True,True,True,False,False,True,True,True,True,False,False,False],[True,True,False,False,True,False,False,False,False,False,False,True,True,False],[True,True,False,True,False,True,False,True,True,False,False,False,False,True],[False,False,False,True,True,False,False,False,False,False,True,False,False,True],[False,True,True,True,False,True,False,True,True,False,False,False,True,True],[True,True,False,True,True,False,True,False,False,True,False,True,True,True],[True,True,True,True,True,False,False,True,False,False,False,True,True,True],[True,False,False,False,True,False,False,False,True,True,False,True,False,False],[False,True,False,False,False,True,True,True,True,False,True,True,False,True],[False,True,False,False,True,False,False,False,True,False,False,False,True,False],[True,True,True,False,False,True,False,True,False,True,False,True,True,True],[True,False,True,True,True,True,True,True,False,False,True,True,False,False],[True,False,False,False,True,True,False,False,False,False,True,False,False,True],[False,True,True,True,True,False,False,True,True,False,False,True,False,True],[False,False,True,True,False,False,False,False,True,False,False,False,True,True],[False,True,False,False,False,True,True,False,True,False,True,True,False,True],[False,False,False,True,False,False,False,True,False,False,True,True,True,True],[True,False,False,False,True,False,False,True,False,False,True,True,False,False],[False,False,True,True,False,False,False,False,False,False,True,False,True,False],[True,False,True,True,False,True,True,True,False,True,False,False,True,False],[True,True,False,False,True,False,True,True,False,True,False,False,True,True],[False,False,False,True,False,True,False,False,True,True,True,True,True,False],[True,False,False,False,False,False,False,True,False,True,True,False,False,True],[False,False,False,False,False,False,False,True,False,False,True,True,False,True],[False,True,True,True,True,True,True,True,True,False,True,False,True,False],[False,False,True,True,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,True,False,False,False,True,False,True,True,True],[True,True,True,False,True,False,True,True,True,False,True,True,False,True]], dtype = "bool")#candidate|8361|(60, 14)|const|bool
const_8362 = relay.const([7.080586,4.972360,0.036545,-0.005183,-6.836913,-3.698047,-7.206139,-3.663072,-8.605552,-9.253990,-7.731144,8.660216,3.211698,0.410062,7.930315,-4.240242,-6.539789,1.060029,4.223614,-1.883083,-4.501953,-5.585972,-8.985195,-6.189982,-0.102497,0.425222,-8.717660,8.751116,8.944951,-2.820688,7.756224,7.193084,-7.260715,1.109842,4.938527,5.663475,-0.497701,-2.673901,7.901018,0.668481,4.360743,-8.867461,4.295543,-1.168097,0.460172,4.754022,5.681472,-4.750318,1.620861,-1.978662,-4.634031,-3.901023,3.542534,8.114774,-8.136638,-1.121232,1.086682,7.463400,-1.832780,8.678348,0.223836,-7.302371,-0.015281,-3.546929,-2.663441,-8.175717,6.628530,0.994603,1.636612,2.353576,9.656017,-9.080514,-0.971426,-7.085710,0.617981,-3.925456,-9.772524,1.145816,-2.119434,0.360471,-8.357256,5.497451,-0.025671,0.816133,2.388220,0.437001,-6.150423,3.646637,-6.887807,-6.913936,-1.788631,-7.580856,7.314177,5.141807,1.776734,7.287448,-4.277313,2.238292,5.561676,-8.514630,6.891992,-5.425087,1.133342,7.121914,3.544991,7.917454,-1.836959,-7.384939,-8.871586,3.356775,-4.169010,4.918564,9.755065,-6.423891,8.915765,6.824267,-3.034447,6.589046,-4.183380,5.513610,-0.655044,7.609984,-2.101317,-6.131879,5.781095,2.494727,-1.296648,-3.518781,8.474331,6.759707,1.227918,-0.618185,-3.217207,-0.711168,-5.445381,-9.726485,-1.935635,9.799402,5.432675,9.707883,-2.099420,4.973304,-5.268640,-1.419100,-6.298666,-9.364734,1.677882,7.060305,-4.240263,-8.525088,-2.529837,6.753558,-6.945143,8.102102,9.875711,-9.484038,1.985614,-5.294370,6.380797,-6.520097,-3.892097,7.930765,2.265578,2.523349,-6.554570,-0.933903,-0.521114,-4.123615,-7.625086,9.406984,-2.905810,5.497722,2.716627,7.744020,0.406261,-9.202512,7.549519,9.197375,-7.694946,-6.050277,-2.042075,1.260965,4.260880,9.320935,-4.138820,0.213848,-5.376353,-1.745607,-3.386400,-4.667943,2.855476,-4.234869,-6.507015,8.188705,-4.014251,-5.908317,-4.029797,-6.581937,8.525746,-0.027722,-3.564382,-8.617068,-7.385601,-1.878378,7.502274,-4.170210,9.329897,0.603965,-5.801335,-4.104407,-9.416544,5.250978,3.491557,-3.432076,6.137508,-6.575776,-7.283930,-3.252129,0.610095,-2.447991,7.159204,-0.415040,8.625157,2.533675,-1.069828,-8.074626,-6.110679,-4.710656,3.395492,-2.852212,6.318890,-3.153865,2.225969,-8.854000,9.639686,2.386725,-1.609188,6.598889,1.615124,0.728571,6.509475,5.238067,-9.542008,2.160035,-3.049386,-7.619734,-9.348523,-5.023790,-4.687822,-3.465828,8.458913,-7.470338,1.462690,6.256947,-0.131003,2.931567,-9.120364,6.975673,-1.894370,9.938750,-2.253089,-6.177139,-7.212144,9.436247,8.020734,0.727753,3.173067,-0.405761,7.518439,-7.807621,4.751557,8.550672,-5.771063,-9.762033,1.247741,9.197567,1.849418,-5.181163,-9.896273,-9.674289,-2.223032,-7.559009,-3.134899,-5.124276,-4.508930,8.076906,-2.391306,-2.870655,-3.324351,8.896520,-6.820734,8.739629,-5.062894,1.966429,4.100529,9.541890,9.411835,-4.077732,-0.460035,-8.028055,7.199580,-3.443671,-3.740278,-4.059821,4.426727,1.102961,-3.486585,-0.701074,-9.007783,-7.862424,5.212931,7.048679,2.616532,-3.483633,5.729579,3.498806,1.156101,-3.679543,-7.429670,-1.276310,2.363747,7.858436,-9.190433,-2.005795,9.172975,6.848751,-8.230317,-4.237330,-8.342977,-2.022254,1.397564,-5.954117,5.025139,-4.605123,6.911974,-2.242668,-4.695836,-4.405980,5.834706,-4.243202,0.141260,3.399240,-5.167117,-6.452780,2.432626,-7.435353,-2.698827,8.966568,-5.832421,1.116730,-0.604130,-4.594461,0.365248,2.411845,0.480812,7.527116,0.760687,0.454069,-0.393643,-8.682129,-3.855217,-8.826914,2.044150,-5.485551,-2.565388,7.792824,6.883888,4.527118,1.655095,2.527518,-1.507908,9.175852,-4.892151,-7.672889,-9.758758,-8.756479,1.947921,5.538360,-7.123213,-0.093657,2.259630,1.890766,1.713319,8.561129,4.754637,-7.390190,-8.406633,-9.063203,-8.898639,2.790292,9.070986,9.390665,4.474683,-7.389197,-9.484087,-9.496623,-9.406982,9.743389,-9.157728,-6.885949,6.294386,-2.739867,2.513695,-9.349897,7.950724,-0.363675,6.557640,3.009633,3.352865,-1.081875,6.179319,0.050355,-3.547935,5.468939,-5.143393,7.726808,-7.445491,6.035902,-7.638070,0.547644,8.606613,-8.863717,6.627807,8.135190,3.786198,8.194155,-8.432597,0.170172,3.764405,-6.556432,-2.336241,4.509621,8.850691,-3.525962,4.437722,6.879708,-5.953924,5.325413,4.153330,-2.210162,7.444002,9.433233,-7.119280,-4.785498,-2.306859,9.209898,-4.380724,9.017432,3.542547,1.877805,-6.952714,-5.138555,9.086876,-1.629048,-6.909675,8.013960,-2.137497,-7.958564,4.001108,-3.798062,3.453691,7.878168,4.384516,1.461514,-3.733226,2.116275,9.333878,1.120815,6.449001,5.042649,-2.829145,5.508197,-6.252491,-7.820113,9.935708,1.291739,-7.086334,-1.355118,7.340983,6.781641,8.888129,-8.379897,-6.644647,2.465900,-5.258178,9.859642,7.877623,9.012068,-7.238876,-5.569720,6.455179,-3.126686,-7.120244,5.923745,-4.420143,1.709035,9.179948,-4.609627,-6.297016,5.025190,3.989805,6.584089,-1.717689,-3.390159,-8.662105,-3.446388,-9.950793,-1.528518,3.277971,-1.676002,-5.636392,0.778089,-4.476479,3.981663,7.956619,3.115800,0.490359,-3.464405,5.452995,4.814966,7.313011,1.906942,-0.706243,-9.540802,2.847909,-1.245326,-6.631222,9.013385,3.874307,1.045148,-8.475623,1.338768,-9.736452,0.942161,-5.782488,6.455470,-3.953510,3.114746,-8.727571,-5.871915,2.359402,4.929234,8.331329,-0.994588,8.196618,9.127888,-9.997816,-0.785111,-8.407486,-8.955416,-2.124213,-1.018497,5.382641,6.386334,8.056836,4.821602,-0.405022,6.815300,-4.012463,5.244940,1.543676,3.179202,5.366714,-9.518351,5.947874,6.260150,9.023805,-5.098360,5.161091,-2.457800,3.854372,0.044562,3.867858,8.854720,-0.445080,2.459623,-3.322275,5.502902,-5.639469,7.283963,5.413892,4.910092,7.658300,7.865412,-0.206832,3.710893,7.358669,0.269802,0.116302,-8.504817,0.516687,-5.127613,-3.177942,-6.413295,4.242129,-4.669650,-7.241806,6.173128,9.940630,-1.434735,8.856440,-7.355307,1.715568,0.758286,-8.683600,-6.081648,6.031801,3.238167,6.537489,5.080007,-6.942925,7.826234,5.995490,-3.327204,4.649778,-3.907964,-3.317650,2.664877,2.894148,7.151553,8.798534,1.069267,-2.619918,-4.294707,-9.438258,-1.105311,-6.357471,8.043366,3.014609,-5.100524,0.991720,9.505561,5.106148,6.186047,1.928434,1.153385,-0.288462,1.161606,2.692066,-2.369708,9.477574,-4.902409,-1.300683,-7.095952,4.476659,-0.449304,2.439009,6.844713,0.826689,6.671910,6.145894,9.285659,-9.584795,-8.774309,-4.084756,3.616903,5.981742,9.530934,-8.119656,7.279797,8.967955,-6.792862,7.030273,2.134246,-3.143081,3.536965,7.671843,2.540967,-5.394996,-1.595388,0.466675,-7.349369,9.520766,-3.774345,9.246238,-1.292598,-9.708841,-4.925598,-3.463799,-7.555208,-8.986217,-2.017805,-7.137348,5.601067,9.032934,2.225786,-8.807510,9.130643,-4.401242,8.681154,-3.943119,-9.858175,-5.181393,-9.950775,-5.762788,8.338640,4.880388,4.774553,9.118433,-5.056978,-8.277154,1.937866,0.705786,-2.829501,1.252141,-2.238809,9.558109,-9.474530,2.282406,-4.878195,7.308072,-9.308806,6.048523,-1.038542,8.340614,0.043767,-0.006042,-9.687407,-9.404151,1.601798,-7.350357,8.320203,-5.781855,5.266844,-0.410663,-1.752089,8.309135,-8.050822,-0.164893,6.896855,6.467814,6.021067,-8.570494,-0.688438,-4.742934,-9.286745,3.764787,5.646253,3.390527,4.343669,-5.390676,4.672773,-7.503978,9.872072,-7.216384,-9.954057,6.928979,4.724490,4.479676,-5.328911,-7.727376,-1.712379,-2.994755,5.109743,-1.323456,-2.364678,-0.828360,-5.310073,2.860487,4.189693,0.741493,-3.838124,1.481690,-6.372735,2.405046,3.477945,4.513846,8.668778,0.275832,1.731097,2.815249,-9.264582,2.011586,-1.963271,-9.204144,-7.174640,-4.293656,3.323195,-6.509249,-8.135987,-7.168390,9.283958,-6.503577,-2.641127,-3.494158,2.258239,7.452407,8.340949,8.243024,7.350307,-1.260640,8.528053,-9.570145,-8.338853,-5.029969,-3.731834,-6.456357,-5.288990,-9.201395,-4.082073,-8.817802,-8.313099,-8.109389,-9.073149,-5.827888,7.750044,5.509907,6.304757,6.738405,-1.918522,-8.852748,6.976065,4.930017,6.570383,-4.361487,-5.095069,-6.609018,-6.278978,-5.606051,-2.196603,-3.342833,7.578417,-5.235077,-6.413271,5.416784,1.762682,6.652968,-9.605661,-5.187620,4.767537,-5.500341,0.523606,-8.759881,9.251139,-2.600460,4.105062,7.077301,-4.392292,5.934594,-3.304045,7.198601,1.126614,-5.738687,4.719351,2.625177,0.223829,-7.349013,-9.216957,-5.514619,-6.956738,8.292893,9.076443,-8.722083,-9.849572,-4.643564,-0.740303,-6.019575,9.137670,-0.085967,5.098234,3.017973,2.572611,2.602897,-5.095672,0.800434,-1.050457,1.989812,0.709902,3.178356,4.349960,-9.415510,-5.663091,4.699289,4.460995,-8.131646,-2.074620,1.007070,-9.447729,9.109013,-4.949219,6.912755,-3.227245,3.220765,-8.252150,6.218848,-3.584608,-7.895740,9.073950,-5.949467,9.929113,7.313077,-2.230836,0.292859,-8.089060,-6.120592,2.565308,8.514431,-3.327997,7.988100,-8.123428,-2.748482,5.545871,4.365288,8.805948,5.594876,-3.830584,-5.276682,-7.064904,2.866526,-1.561087,1.844411,4.126188,4.314238,9.067169,3.128622,-2.449598,0.141358,-7.288879,-6.915905,-0.211527,-7.111956,-4.509916,-6.292714,-1.738324,9.213113,6.955515,-2.603401,-5.973093,-6.056278,-7.427959,3.395639,6.786456,-1.381481,0.206859,8.650355,5.655806,-6.713387,-2.994555,-7.060002,8.785056,-9.213631,-6.941687,3.440801,-2.934115,6.390056,4.502677,5.549933,5.727185,-6.391289,-8.926277,-4.822117,7.434125,-3.489765,7.311131,-2.196204,-6.713518,2.709526,4.705236,3.873714,-9.528182,1.109187,0.393461,3.645510,-7.241093,1.391635,6.816705,-9.700586,8.942219,0.311216,1.411965,5.611524,-4.705016,4.051569,8.134167,6.080487,9.425620,-0.521142,-9.489386,2.537302,3.235765,7.417025,-8.519964,-3.461944,-1.589865,1.554817,1.844784,-1.865577,8.496587,-6.140119,-9.703665,4.230358,-1.477563,0.383790,4.733656,6.147444,5.904613,3.792612,4.684327,8.777759,4.995875,2.294600,9.597840,-7.783833,8.088796,-5.618182,2.430911,8.095034,9.818057,-5.988881,5.252597,6.212306,-4.596302,1.290194,-5.869473,-9.201712,8.431222,1.370410,2.489146,7.955010,-0.529931,-6.605879,5.846791,1.169643,-3.270611,3.197163,5.982114,6.842180,-8.373462,8.731273,8.994622,-8.501649,-4.098317,-5.195750,-0.412475,-1.905469,1.583162,-7.278627,0.182884,7.004931,6.273369,5.422636,4.272667,-1.411228,0.349221,1.309490,3.747131,5.668074,5.873119,6.905661,-3.672183,-5.737242,5.616191,-6.848219,-5.073016,-2.938332,8.117585,-2.514289,-3.735955,-1.902439,9.243743,7.977425,1.896974,-3.418881,-2.995675,-4.357795,7.853247,-1.174680,8.608058,1.873948,-9.654100,8.049484,-1.946269,-9.587602,2.873729,-4.089388,-9.952249,2.895426,8.253580,-4.212171,-7.128247,-0.082224,9.521958,-2.872627,8.098815,-6.059170,0.485994,9.342328,-9.563404,4.625560,-2.404793,-2.865641,6.960513,5.435021,5.118365,-7.154679,-9.042351,9.270757,4.155134,1.202514,-6.999910,-3.862342,7.218627,2.501548,0.405442,4.410638,-9.895307,0.959951,-6.866863,-4.718769,-1.761444,5.540858,0.207089,0.802711,-7.711258,-4.320760,-3.115493,-7.665299,-5.041404,3.793854,-6.519703,-8.733498,-9.566319,-4.581697,-3.722144,-0.722445,5.219866,9.529436,8.588884,2.879042,2.351642,-1.524424,-4.325249,-5.514526,-0.967599,6.528963,-0.981407,4.861143,8.641526,7.251568,9.172541,-5.119617,2.725606,3.584209,-6.999375,-3.688919,-8.567665,-0.497998,-0.224189,-7.305976,-9.463593,2.918028,5.869767,-0.422225,9.683999,-4.682226,2.543777,1.495074,-2.798049,2.867653,-5.238713,9.613791,-8.123048,6.736403,-9.895449,3.889301,5.584759,5.053537,-9.999115,6.947997,-3.003645,-7.624285,6.898905,-8.177468,-2.810948,-7.452142,-7.153504,-7.572233,7.010096,8.684116,2.812370,3.166405,1.340949,2.391576,-0.597125,2.438365,-8.017443,-4.615830,-8.419645,6.147441,9.793221,2.226871,4.023084,-0.436505,1.487494,-7.859112,0.869583,-4.973803,2.798455,-5.676656,-4.563903,-9.414787,6.206968,-7.173393,1.469422,-1.231869,-3.635609,-3.298865,8.934226,-6.894800,-8.871324,0.337810,-4.835452,3.719705,9.831678,3.991594,3.179756,-3.903652,9.472395,-2.364333,2.718483,7.674166,-2.455944,4.594992,-2.466209,3.583764,2.505127,-5.489553,-0.277845,0.981996,6.203621,1.050996,-9.081261,2.044595,1.980132,-2.517978,6.227551,-1.716310,-5.393394,0.118215,1.184090,1.684042,-3.796273,4.850315,8.664552,-8.597910,1.504726,-5.357997,-1.214927,7.432996,3.859997,-8.342010,9.777525,3.696957,-0.897606,1.408522,4.044419,-1.676673,-6.151592,-1.633354,-3.824028,4.172492,-8.224273,0.784895,4.470623,-5.075689,4.712274,9.872620,5.334851,-1.865484,-7.453701,-5.209556,-5.503024,2.665837,-4.750583,3.531647,-5.082891,-0.832544,-7.817863,6.996591,3.286994,-1.608297,-3.167082,5.079828,-9.666797,-7.293168,9.775615,-9.689225,7.696119,4.956183,4.725179,4.907966,2.851668,0.540148,2.529967,1.290472,-8.581697,6.316925,-4.805716,7.707443,-6.554223,8.366928,-8.541177,-2.343917,6.085005,8.820224,-6.636346,-5.761472,-8.300921,2.167449,7.436559,-4.859475,-2.994929,-6.562654,2.578538,-1.713396,4.954665,2.862477,2.179428,-2.510122,0.088962], dtype = "float32")#candidate|8362|(1320,)|const|float32
call_8360 = relay.TupleGetItem(func_7055_call(relay.reshape(const_8361.astype('bool'), [5, 14, 12]), relay.reshape(const_8361.astype('bool'), [5, 14, 12]), relay.reshape(const_8362.astype('float32'), [1320,]), ), 5)
call_8363 = relay.TupleGetItem(func_7059_call(relay.reshape(const_8361.astype('bool'), [5, 14, 12]), relay.reshape(const_8361.astype('bool'), [5, 14, 12]), relay.reshape(const_8362.astype('float32'), [1320,]), ), 5)
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_8364 = relay.TupleGetItem(func_1653_call(), 0)
call_8365 = relay.TupleGetItem(func_1655_call(), 0)
func_3847_call = mod.get_global_var('func_3847')
func_3848_call = mutated_mod.get_global_var('func_3848')
call_8368 = func_3847_call()
call_8369 = func_3847_call()
output = relay.Tuple([call_8357,call_8360,const_8361,const_8362,call_8364,call_8368,])
output2 = relay.Tuple([call_8358,call_8363,const_8361,const_8362,call_8365,call_8369,])
func_8393 = relay.Function([], output)
mod['func_8393'] = func_8393
mod = relay.transform.InferType()(mod)
output = func_8393()
func_8394 = relay.Function([], output)
mutated_mod['func_8394'] = func_8394
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8401 = relay.var("var_8401", dtype = "uint8", shape = (7, 1, 3))#candidate|8401|(7, 1, 3)|var|uint8
var_8402 = relay.var("var_8402", dtype = "uint8", shape = (7, 13, 3))#candidate|8402|(7, 13, 3)|var|uint8
bop_8403 = relay.multiply(var_8401.astype('uint8'), var_8402.astype('uint8')) # shape=(7, 13, 3)
func_6960_call = mod.get_global_var('func_6960')
func_6964_call = mutated_mod.get_global_var('func_6964')
const_8418 = relay.const([9,8,3,-9,6,-8,-9,1,8,-10,2,10,-9,-10,10,-2,-7,8,-8,-6,-10,-9,1,8,7,-10,-8,-3,-7,-3,4,-7,-6,10,-3,-10,-3,1,-6,-3,7,-4,-6,-3,-1,10,-4,8,-2,-5,7,6,-4,-3,-6,-7,-10,9,7,-8,8,6,3,-3,-4,-9,-4,2,4,10,2,4,-8,7,-4,-6,3,6,9,10,-8,6,-6,1,6,1,-9,-9,7,-2,2,-7,1,-10,5,-4,1,-6,-8,6,-8,-1,1,2,7,2,2,-6,-3,1,-10,-2,7,-7,-2,-1,1,7,-2,-9,3,-2,-1,7,-7,-3,-5,8,-10,7,10,-4,7,-1,2,-2,3,7,-4,-7,3,8,4,10,-10,10,2,-1,7,2,3,-4,9,10,6,-2,9,8,5,9,-4,5,5,9,-7,-1,4,-9,-9,-4,-6,5,-6,1,3,-7,9,5,8,-5,-4,5,4,-10,-3,-7,1,-6,-6,-10,-7,10,-7,-9,8,9,-10,9,-10,-6,-3,4,4,-5,-7,3,-10,-9,7,-3,1,8,-8,-7,6,-3,-6,-7,9,5,6,9,1,6,-7,3,-3,-9,-8,1,-2,4,-5,10,-4,-1,3,8,-9,1,3,2,-5,-7,1,-8,4,1,-5,-3,-6,-9,4,10,-10,-9,-5,7,6,-2,3,8,-1,7,9,-7,6,-1,-3,-6,-4,-6,-8,10,10,-10,3,10,-8,2,-9,-2,4,9,-8,10,2,4,2,5,-9,3,-7,-8,2,-2,-10,7,-2,1,1,-6,1,4,-6,-5,6,-5,-3,-7,4,5,6,9,-8,1,-4,-2,-7,-8,5,-5,5,3,-4,2,-10,3,-9,-5,3,-6,-3,1,5,2,-7,1,7,-10,2,1,9,7,4,-6,-10,-3,-1,2,6,-5,10,-2,10,10,-2,-6,-2,-10,9,-3,-6,-1,-1,-2,8,7,-5,-7,-1,-1,-7,-5,-1,9,-8,-8,-1,3,3,-8,-7,1,5,1,6,-8,-8,-5,-5,9,-9,2,-6,-1,-4,-2,-5,5,2,4,5,-2,-5,3,3,7,-1,-1,6,7,-10,-1,1,-5,-9,2,10,-10,-3,7,7,8,-1,-4,-1,-6,-8,-6,-2,-4,9,-6,10,-6,-7,10,4,-1,-7,3,3,-10,6,-4,8,-9,3,-8,9,7,6,1,5,7,6,1,9,2,7,4,-3,-4,6,9,-5,-3,-4,-1,6,-5,7,-4,7,-2,4,-10,6,-1,-8,-10,-9,-4,-7,3,4,-8,4,-5,-7,-5,-2,-6,-1,-3,-9,1,-5,-2,1,-10,3,-6,-7,8,-10,3,-10,-10,-7,-9,5,-8,-5,7,-6,-3,-2,-10,3,-2,-10,5,-5,-10,-8,-1,-9,7,9,-1,8,6,4,10,-3,-10,-7,-3,-10,5,2,-4,4,4,-5,8,1,-5,1,2,-8,-7,9,-7,2,8,-9,2,4,-9,-1,2,5,6,-3,-10,-3,7,-6,1,-6,2,3,-1,10,-6,8,-2,7,7,-8,-2,3,-3,4,6,4,9,4,2,1,6,8,-2,-7,7,-7,6,-10,8,-2,-6,-4,4,5,1,-6,5,6,10,-6,7,-8,3,2,4,6,2,4,-8,-2,5,10,1,-7,7,8,7,9,-3,-9,-6,-6,-7,-4,1,7,-3,8,-3,5,-8,-6,-8,-5,5,-10,3,1,10,6,-9,-9,-2,-6,-4,4,5,-9,6,-8,9,4,-5,3,-8,9,4,2,5,-10,3,2,-6,1,-4,3,-8,-7,-9,10,-9,-7,-7,10,8,-2,4,9,5,-3,10,6,2,10,-4,-1,9,8,6,9,-8,7,5,3,7,-10,-2,2,10,5,4,10,3,-1,-8,7,1,9,9,7,7,-10,4,5,5,1,-8,-5,1,-2,-6,4,-2,-3,-4,-8,8,2,-1,7,10,7,10,-9,-8,7,-9,-3,-3,-3,-7,-8,8,-8,-10,6,6,8,-7,-5,9,1,5,10,-10,-5,-3,-3,-4,9,-7,-3,-10,7,9,2,-5,5,-5,-8,-7,2,-5,-10,-6,-4,-6,8,-10,-3,8,-7,6,-3,-7,8,3,2,4,8,3,-7,-10,4,9,-1,1,-9,9,2,4,-8,9,-2,3,7,3,2,-6,-5,4,-3,3,-3,-6,6,4,-5,-5,-8,-1,4,-8,7,-5,-10,-8,1,4,4,9,-10,-6,-8,5,1,10,10,-2,-1,-9,3,3,-9,-9,9,-10,1,-5,7,4,6,3,-3,2,1,6,-7,9,-5,6,6,-2,-4,-5,-9,-10,4,-2,10,10,3,7,-4,7,-5,-1,1,-8,-2,-9,-2,5,-4,-3,-9,6,-1,-6,-7,4,6,-3,-1,-5,3,-2,-2,-3,6,-1,-2,-8,7,-10,7,-6,-1,1,1,-3,-9,-1,5,-7,3,5,2,10,7,4,6,-6,-3,7,2,-10,6,-2,-7,-2,-9,-8,8,2,10,1,10,-10,-4,-6,-8,9,-8,-7,-2,-7,-3,1,3,-9,1,-6,7,1,5,-8,-2,7,8,4,10,-2,-4,-6,-6,1,-5,6,5,3,-5,-2,-10,6,2,1,-9,9,-5,4,10,-9,-2,-8,4,-6,-4,5,-9,5,1,7,6,7,9,-3,5,-7,-6,-4,6,-9,-10,8,5,3,9,8,-6,-9,6,-7,3,-8,6,-1,-5,7,-5,7,10,8,3,-7,10,-5,7,7,-3,2,10,4,-6,-3,5,2,1,5,7,3,7,6,-8,-5,-10,2,10,5,6,6,-7,9,10,4,-7,7,-4,9,5,-5,-10,-7,3,-8,-10,-2,-5,-7,-8,-4,-7,-8,-5,-5,10,-7,6,-5,-6,10,7,4,-5,-9,-3,8,4,-3,3,-9,-7,-7,2,4,3,5,7,2,-2,5,-5,-5,10,-10,-5,8,-7,7,-5,7,-6,-7,-2,7,1,-9,-6,5,-2,9,-4,-9,9,10,10,1,-2,9,1,-9,-9,-1,3,-10,-3,-2,5,-9,1,10,9,-7,2,-6,-3,7,3,8,-4,-3,-7,-3,10,7,-1,3,8,2,8,-5,3,5,-10,4,-9,-10,-3,9,4,3,2,-9,5,-2,-9,6,-9,-8,1,-4,8,-9,6,2,-3,-9,-2,5,8,-2,6,-9,-8,5,-8,2,-2,6,-10,-10,-5,9,-7,-7,-4,4,-5,-5,9,-4,7,-2,8,7,-6,2,5,-1,6,9,-4,-7,3,4,2,-10,4,7,10,2,10,9,5,-10,-7,10,10,-2,1,-9,-4,1,-1,-9,-2,-8,5,2,9,-1,-10,6,10,5,4,2,10,-5,2,1,5,10,9,1,1,2,5,-1,8,6,-9,9,2,2,5,9,5,3,-9,-3,6,-4,-7,-6,3,6,-10,5,6,7,-1,5,-6,-3,3,-9,-3,-2,10,-3,1,8,4,-7,-9,4,-3,-9,7,5,-7,-9,-7,-9,10,-3,3,2,3,10,4,-5,2,5,5,9,4,2,-8,10,5,9,-5,7,-2,3,10,-2,-1,2,-7,-9,9,-4,-4,-7,8,-1,6,-2,-5,-4,-10,-9,-5,10,-4,-5,-10,-3,3,-7,5,5,-6,-2,9,-7,-4,3,-9,-1,2,7,-5,8,10,1,3,-7,-3,1,-4,-5,9,6,-1,-3,5,4,-10,-9,8,-6,-8,-2,-9,-4,-3,1,-7,2,-4,-10,4,-10,-6,5,-1,-9,-3,1,-5,-6,6,-2,2,10,6,-6,5,5,7,7,2,-8,-6,8,5,-10,1,3,-6,1,4,2,-7,1,8,3,-4,6,9,-3,-8,-5,-7,-2,1,4,-5,3,5,6,-1,-5,8,-7,5,-5,-3,2,9,2,9,7,2,6,3,-1,8,1,7,-7,8,-5,-2,-2,5,3,1,10,10,-1,7,-1,-9,-3,2,9,3,2,3,6,-7,-3,-1,-2,-8,-5,-6,-2,-9,-1,6,-1,-4,-4,-7,6,-1,4,2,2,10,5,-4,-3,1,-3,4,5,9,6,10,-1,10,3,-3,10,-2,3,1,10,10,8,-7,3,-2,1,-8,5,10,-10,4,-6,6,-4,-5,-8,8,-10,-10,-3,1,-8,-8,9,-2,-1,-8,7,-8,10,5,-10,-5,-10,-3,-1,8,-3,2,-6,-10,5,6,1,-2,7,10,-10,8,-4,-4,-5,-4,-1,-2,-3,6,10,9,-5,-4,-8,-10,1,-10,-8,10,9,4,10,-8,6,-10,-3,-8,2,3,-6,10,-10,4,7,1,-6,7,-9,-9,-7,1,-2,10,-3,-3,7,-8,-4,-5,6,8,-9,10,-9,4,1,-8,6,-4,3,10,9,-5,2,-5,-5,2,7,3,2,2,7,-4,-7,4,6,-10,-3,1,4,-6,8,-5,2,10,9,7,1,-9,-2,8,8,-4,-2,8,10,7,6,4,1,-1,-8,-6,-10,7,7,-1,-3,6,9,-3,10,6,3,-3,3,-7,-2,10,-8,-5,4,10,10,-5,1,-9,-10,-6,-6,9,3], dtype = "int64")#candidate|8418|(1728,)|const|int64
call_8417 = relay.TupleGetItem(func_6960_call(relay.reshape(const_8418.astype('int64'), [16, 12, 9]), relay.reshape(const_8418.astype('int64'), [16, 12, 9]), ), 0)
call_8419 = relay.TupleGetItem(func_6964_call(relay.reshape(const_8418.astype('int64'), [16, 12, 9]), relay.reshape(const_8418.astype('int64'), [16, 12, 9]), ), 0)
func_4978_call = mod.get_global_var('func_4978')
func_4980_call = mutated_mod.get_global_var('func_4980')
call_8425 = relay.TupleGetItem(func_4978_call(), 0)
call_8426 = relay.TupleGetItem(func_4980_call(), 0)
func_8348_call = mod.get_global_var('func_8348')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_8434 = func_8348_call()
call_8435 = func_8348_call()
uop_8448 = relay.sigmoid(call_8417.astype('float64')) # shape=(16, 12, 9)
uop_8450 = relay.sigmoid(call_8419.astype('float64')) # shape=(16, 12, 9)
func_4959_call = mod.get_global_var('func_4959')
func_4960_call = mutated_mod.get_global_var('func_4960')
call_8455 = relay.TupleGetItem(func_4959_call(), 0)
call_8456 = relay.TupleGetItem(func_4960_call(), 0)
output = relay.Tuple([bop_8403,const_8418,call_8425,call_8434,uop_8448,call_8455,])
output2 = relay.Tuple([bop_8403,const_8418,call_8426,call_8435,uop_8450,call_8456,])
func_8458 = relay.Function([var_8401,var_8402,], output)
mod['func_8458'] = func_8458
mod = relay.transform.InferType()(mod)
var_8459 = relay.var("var_8459", dtype = "uint8", shape = (7, 1, 3))#candidate|8459|(7, 1, 3)|var|uint8
var_8460 = relay.var("var_8460", dtype = "uint8", shape = (7, 13, 3))#candidate|8460|(7, 13, 3)|var|uint8
output = func_8458(var_8459,var_8460,)
func_8461 = relay.Function([var_8459,var_8460,], output)
mutated_mod['func_8461'] = func_8461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7153_call = mod.get_global_var('func_7153')
func_7155_call = mutated_mod.get_global_var('func_7155')
call_8470 = relay.TupleGetItem(func_7153_call(), 1)
call_8471 = relay.TupleGetItem(func_7155_call(), 1)
func_7790_call = mod.get_global_var('func_7790')
func_7792_call = mutated_mod.get_global_var('func_7792')
call_8479 = relay.TupleGetItem(func_7790_call(), 0)
call_8480 = relay.TupleGetItem(func_7792_call(), 0)
func_8458_call = mod.get_global_var('func_8458')
func_8461_call = mutated_mod.get_global_var('func_8461')
const_8486 = relay.const([-6,8,4,-9,3,7,-6,-8,-5,-9,-6,-6,6,6,-6,1,-10,3,-4,9,2], dtype = "uint8")#candidate|8486|(21,)|const|uint8
const_8487 = relay.const([-10,2,6,6,6,8,-4,7,-7,-3,-7,1,1,-9,7,3,-9,-5,-6,-8,4,6,2,9,-4,-8,-1,4,-10,4,-3,5,4,8,2,4,-3,6,-6,5,-7,2,-2,9,9,9,4,5,-5,-10,10,5,-6,7,7,-3,6,4,4,-10,-1,-7,5,5,-7,-7,10,-8,-4,-2,8,-9,3,-4,9,9,5,6,-8,-9,7,1,9,-6,8,-6,-3,3,-8,-10,3,8,-5,-7,5,-1,-10,-10,4,4,3,-8,-4,-2,-10,-1,6,-8,-6,-6,-10,3,-1,-1,-10,7,-2,2,8,10,10,10,3,-7,-4,1,-1,-4,-9,5,7,-5,-9,-6,-2,-6,10,-8,-3,-3,7,-10,8,9,8,-9,10,-5,10,7,-2,8,-8,-6,-1,-9,-4,-7,3,-2,-3,-6,-2,1,4,7,2,7,-2,-2,-3,1,10,-10,7,-1,-2,3,-10,9,4,-2,-3,-4,-2,-6,-7,-4,7,9,-7,-4,9,-4,-4,5,-9,2,-3,-7,-5,4,1,9,2,-4,10,6,5,-10,-3,7,-9,-5,5,1,-4,2,-1,-5,-2,-1,-7,4,9,1,9,5,6,2,10,1,-8,-9,-7,3,-3,2,1,2,-9,1,10,4,4,7,-1,9,-3,-10,5,10,6,-6,9,7,10,4,2,7,-5,-1,5,8,10,-10,9,-1,-3,2,-6,10,4], dtype = "uint8")#candidate|8487|(273,)|const|uint8
call_8485 = relay.TupleGetItem(func_8458_call(relay.reshape(const_8486.astype('uint8'), [7, 1, 3]), relay.reshape(const_8487.astype('uint8'), [7, 13, 3]), ), 2)
call_8488 = relay.TupleGetItem(func_8461_call(relay.reshape(const_8486.astype('uint8'), [7, 1, 3]), relay.reshape(const_8487.astype('uint8'), [7, 13, 3]), ), 2)
output = relay.Tuple([call_8470,call_8479,call_8485,const_8486,const_8487,])
output2 = relay.Tuple([call_8471,call_8480,call_8488,const_8486,const_8487,])
func_8492 = relay.Function([], output)
mod['func_8492'] = func_8492
mod = relay.transform.InferType()(mod)
mutated_mod['func_8492'] = func_8492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8492_call = mutated_mod.get_global_var('func_8492')
call_8493 = func_8492_call()
output = call_8493
func_8494 = relay.Function([], output)
mutated_mod['func_8494'] = func_8494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1798_call = mod.get_global_var('func_1798')
func_1799_call = mutated_mod.get_global_var('func_1799')
call_8507 = relay.TupleGetItem(func_1798_call(), 0)
call_8508 = relay.TupleGetItem(func_1799_call(), 0)
func_3401_call = mod.get_global_var('func_3401')
func_3403_call = mutated_mod.get_global_var('func_3403')
call_8509 = relay.TupleGetItem(func_3401_call(), 0)
call_8510 = relay.TupleGetItem(func_3403_call(), 0)
output = relay.Tuple([call_8507,call_8509,])
output2 = relay.Tuple([call_8508,call_8510,])
func_8518 = relay.Function([], output)
mod['func_8518'] = func_8518
mod = relay.transform.InferType()(mod)
output = func_8518()
func_8519 = relay.Function([], output)
mutated_mod['func_8519'] = func_8519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5911_call = mod.get_global_var('func_5911')
func_5913_call = mutated_mod.get_global_var('func_5913')
call_8582 = relay.TupleGetItem(func_5911_call(), 4)
call_8583 = relay.TupleGetItem(func_5913_call(), 4)
output = call_8582
output2 = call_8583
func_8588 = relay.Function([], output)
mod['func_8588'] = func_8588
mod = relay.transform.InferType()(mod)
output = func_8588()
func_8589 = relay.Function([], output)
mutated_mod['func_8589'] = func_8589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5972_call = mod.get_global_var('func_5972')
func_5974_call = mutated_mod.get_global_var('func_5974')
call_8657 = func_5972_call()
call_8658 = func_5972_call()
output = call_8657
output2 = call_8658
func_8664 = relay.Function([], output)
mod['func_8664'] = func_8664
mod = relay.transform.InferType()(mod)
output = func_8664()
func_8665 = relay.Function([], output)
mutated_mod['func_8665'] = func_8665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7435_call = mod.get_global_var('func_7435')
func_7437_call = mutated_mod.get_global_var('func_7437')
call_8694 = relay.TupleGetItem(func_7435_call(), 0)
call_8695 = relay.TupleGetItem(func_7437_call(), 0)
output = relay.Tuple([call_8694,])
output2 = relay.Tuple([call_8695,])
func_8711 = relay.Function([], output)
mod['func_8711'] = func_8711
mod = relay.transform.InferType()(mod)
mutated_mod['func_8711'] = func_8711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8711_call = mutated_mod.get_global_var('func_8711')
call_8712 = func_8711_call()
output = call_8712
func_8713 = relay.Function([], output)
mutated_mod['func_8713'] = func_8713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8335_call = mod.get_global_var('func_8335')
func_8336_call = mutated_mod.get_global_var('func_8336')
call_8714 = relay.TupleGetItem(func_8335_call(), 0)
call_8715 = relay.TupleGetItem(func_8336_call(), 0)
func_4562_call = mod.get_global_var('func_4562')
func_4565_call = mutated_mod.get_global_var('func_4565')
var_8719 = relay.var("var_8719", dtype = "float32", shape = (256,))#candidate|8719|(256,)|var|float32
call_8718 = relay.TupleGetItem(func_4562_call(relay.reshape(var_8719.astype('float32'), [256,])), 1)
call_8720 = relay.TupleGetItem(func_4565_call(relay.reshape(var_8719.astype('float32'), [256,])), 1)
func_7790_call = mod.get_global_var('func_7790')
func_7792_call = mutated_mod.get_global_var('func_7792')
call_8728 = relay.TupleGetItem(func_7790_call(), 0)
call_8729 = relay.TupleGetItem(func_7792_call(), 0)
func_6653_call = mod.get_global_var('func_6653')
func_6655_call = mutated_mod.get_global_var('func_6655')
call_8758 = relay.TupleGetItem(func_6653_call(), 0)
call_8759 = relay.TupleGetItem(func_6655_call(), 0)
output = relay.Tuple([call_8714,call_8718,var_8719,call_8728,call_8758,])
output2 = relay.Tuple([call_8715,call_8720,var_8719,call_8729,call_8759,])
func_8762 = relay.Function([var_8719,], output)
mod['func_8762'] = func_8762
mod = relay.transform.InferType()(mod)
var_8763 = relay.var("var_8763", dtype = "float32", shape = (256,))#candidate|8763|(256,)|var|float32
output = func_8762(var_8763)
func_8764 = relay.Function([var_8763], output)
mutated_mod['func_8764'] = func_8764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3130_call = mutated_mod.get_global_var('func_3130')
call_8858 = relay.TupleGetItem(func_3129_call(), 1)
call_8859 = relay.TupleGetItem(func_3130_call(), 1)
func_4529_call = mod.get_global_var('func_4529')
func_4533_call = mutated_mod.get_global_var('func_4533')
var_8863 = relay.var("var_8863", dtype = "float64", shape = (9, 225))#candidate|8863|(9, 225)|var|float64
call_8862 = relay.TupleGetItem(func_4529_call(relay.reshape(var_8863.astype('float64'), [2025,]), relay.reshape(var_8863.astype('float64'), [2025,]), ), 2)
call_8864 = relay.TupleGetItem(func_4533_call(relay.reshape(var_8863.astype('float64'), [2025,]), relay.reshape(var_8863.astype('float64'), [2025,]), ), 2)
output = relay.Tuple([call_8858,call_8862,var_8863,])
output2 = relay.Tuple([call_8859,call_8864,var_8863,])
func_8865 = relay.Function([var_8863,], output)
mod['func_8865'] = func_8865
mod = relay.transform.InferType()(mod)
mutated_mod['func_8865'] = func_8865
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8866 = relay.var("var_8866", dtype = "float64", shape = (9, 225))#candidate|8866|(9, 225)|var|float64
func_8865_call = mutated_mod.get_global_var('func_8865')
call_8867 = func_8865_call(var_8866)
output = call_8867
func_8868 = relay.Function([var_8866], output)
mutated_mod['func_8868'] = func_8868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7338_call = mod.get_global_var('func_7338')
func_7340_call = mutated_mod.get_global_var('func_7340')
call_8913 = func_7338_call()
call_8914 = func_7338_call()
output = relay.Tuple([call_8913,])
output2 = relay.Tuple([call_8914,])
func_8928 = relay.Function([], output)
mod['func_8928'] = func_8928
mod = relay.transform.InferType()(mod)
output = func_8928()
func_8929 = relay.Function([], output)
mutated_mod['func_8929'] = func_8929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6878_call = mod.get_global_var('func_6878')
func_6879_call = mutated_mod.get_global_var('func_6879')
call_8998 = func_6878_call()
call_8999 = func_6878_call()
func_4692_call = mod.get_global_var('func_4692')
func_4695_call = mutated_mod.get_global_var('func_4695')
const_9012 = relay.const([1.331398,-0.082903,5.519918,7.352552,1.156385,-5.009222,0.553861,0.204439,-0.430734,4.764988,-6.954533,2.231991,-1.611256,-9.387783,-7.813110,9.047547,0.220809,-8.407634,1.620324,-1.249137,-0.811650,1.708919,-6.838405,-2.404876,-0.298406,-9.723265,2.357278,6.790936,-5.322866,7.679780,4.030627,7.211072,-9.939603,-7.028857,5.770092,9.388423,2.883631,2.381188,6.833957,9.717455,6.355724,-9.958746,8.805038,-2.726686,4.372389,-9.874806,-5.203678,1.517508,1.821997,-3.385661,-0.136445,-7.164629,-7.424798,0.007519,2.166555,6.218674,-3.734041,1.746359,-4.229944,-2.992371,7.193618,-0.521298,-7.471819,5.375993,0.579862,-2.703721,7.521545,-4.041451,-6.007314,2.673764,-4.268906,-2.303773,-5.578487,-3.761307,1.333348,-5.662183,-6.254005,-1.825367,-2.548256,-9.920223,9.133354,1.901213,-8.718529,-5.883564,4.211878,-7.763817,3.710479,-2.004137,4.563715,-8.724469,3.752249,0.449160,7.746651,-8.839787,2.052923,-0.431936,0.684843,4.669519,2.665047,-5.338319,6.546141,-6.318522,0.252439,-6.762861,5.240864,7.538521,0.712542,-7.623088,-9.173630,-4.383361,-2.333717,-7.237699,-6.852422,6.838212,-9.646403,-9.675324,-1.587723,-7.429270,-3.861042,-8.679414,8.450102,-5.590766,6.046471,4.356346,-9.637493,7.739325,-0.436393,-6.607564,-2.006508,-8.058121,-8.581748,-8.343162,2.019085,-4.665868,-1.581930,-6.985838,4.911256,-1.965260,4.065458,-8.986812,-3.947934,-5.590268,-8.061268,6.758708,-7.601572,1.463381,1.912078,-2.934834,-4.031199,-4.983764,1.230699,-0.527089,7.271855,0.655663,-9.024177,-2.642819,-3.764262,-2.950908,-6.013389,8.503908,4.591171,0.931464,-5.592701,-4.140966,-0.993963,2.880830,7.478322,-9.540831,3.630087,6.077370,-7.669347,-7.986503,2.457492,6.503213,-5.641540,-1.758766,0.098195,-0.091822,3.762731,-2.956811,2.794750,-9.512840,1.221869,-1.750674,-7.614009,-5.549921,2.780751,5.683937,2.604408,-8.959580,9.920690,-6.419397,-1.018539,1.959511,8.447856,-3.574032,7.760219,8.034262,9.790773,4.541111,9.626268,-9.225445,-3.728403,7.411164,-7.400971,-8.233906,1.740758,-5.223657,0.324335,5.427646,0.806941,-3.996087,-5.155227,8.710886,2.038348,-4.098482,2.711800,8.420550,-4.881356,1.689371,2.544429,1.357199,-4.455378,-3.303886,2.032701,-5.115726,2.755581,1.081202,-5.061216,-6.115403,-6.785243,8.218917,9.819120,8.893272,4.103984,3.768130,-3.489662,4.978259,-8.665493,7.375860,-8.012178,9.536481,-9.376567,2.030719,6.095805,-5.002388,-4.417871,3.827170,-1.282292,-8.084052,-0.775750,-2.862371,-4.249240,5.363520,-3.947759,-7.392623,5.406516,-7.514809,-3.053553,-8.023793,5.025193,7.145083,-8.427091,-2.092114,-9.420788,8.460424,-8.537802,1.034772,4.400104,3.545604,4.403389,-1.604946,5.698167,-2.130961,7.862133,-2.086205,0.129924,-7.974656,-8.853653,3.392509,5.330621,7.117526,-6.597874,-7.543726,-0.807970,0.188641,1.009453,-4.124950,0.245736,6.312898,1.428402,4.954615,1.163494,5.932810,-1.202621,-7.494920,8.889186,4.642738,7.429590,3.347655,-6.567492,0.945673,3.485809,-5.964179,4.000816,1.759765,1.597145,5.188187,-2.382978,2.834667,2.752045,1.619088,8.975027,4.959296,-8.154226,-9.420087,9.548261,7.110706,1.367451,7.119533,4.385768,-4.137126,-4.492248,5.611891,-1.926248,3.860404,3.825691,-0.101599,-8.283246,9.811953,-1.863595,8.939359,6.559129,-1.474087,-0.398918,1.637183,-4.551890,8.075836,-5.679209,-9.062309,6.535572,-7.902373,-4.204263,2.986115,-7.360757,7.186872,2.394819,7.150117,3.349345,9.861165,9.974693,5.821726,-9.508327,-2.878536,-5.988514,0.881499,4.707954,-2.833003,-0.775195,-1.612450,-4.802526,-7.456291,-2.710248,-9.654123,3.029812,8.712763,0.344314,2.320504,7.692467,-1.950381,-1.745935,8.770503,5.787790,3.624496,-1.585744,5.991425,1.560940,-0.511940,6.954888,-8.135690,-0.799332,0.236942,-1.740794,-6.534128,5.144057,1.797341,-3.107127,2.163104,-4.882632,-6.937886,-3.263061,8.029326,7.940636,0.770517,5.806298,2.930663,3.003245,0.845108,2.299918,-9.985282,-8.364384,-8.936455,-2.283896,-3.568847,-2.791523,2.326147,-5.905519,7.271949,-4.709033,-9.368409,-3.054274,-1.162936,3.537933,3.675711,7.741551,5.407526,-7.583598,-3.178935,4.617810,0.363673,5.201099,-3.812156,-5.569509,1.966820,-3.153935,-6.529961,-7.647950,-8.220869,-1.884510,-3.018905,5.743866,0.063001,-9.753563,8.504383,-2.206239,5.224097,2.812119,-2.202124,7.335706,7.188761,9.962221,-3.800841,-1.429096,0.655006,7.865497,-3.788488,8.657352,-5.707868,6.926595,7.210894,-3.689266,-3.193929,-9.139341,0.747604,-4.570691,2.368578,-6.670086,7.478143,0.425475,1.190397,5.457515,0.534353,6.669115,-6.722671,2.860096,5.002619,-5.126906,-7.552315,-7.997831,8.233889,-3.235895,-0.125357,-1.307055,8.317486,8.194879,-0.405073,-1.035343,0.400459,0.545801,-1.425246,-2.294698,7.558217,2.127441,9.495991,5.717180,8.741311,-5.158220,3.658105,3.262404,-3.501233,4.608559,2.539200,-2.428575,-1.612184,-3.654577,2.048687,-1.716038,-8.701947,-4.060872,2.518887,-2.696495,9.193399,-5.058672,4.371320,9.488856,-4.085832,6.622479,-9.312016,9.939664,2.269259,8.683570,-7.884544,3.799787,-7.873060,-9.723677,-7.571896,-4.647495,5.038383,-0.314377,-7.551325,-3.926640,-1.826386,1.897628,-5.612512,0.898841,-6.137844,-0.006491,-0.352155,0.770231,8.181212,-9.267876,-7.849342,3.275527,-7.853675,9.531349,8.057956,6.937826,1.535746,-5.130823,9.242664,0.131594,-4.068839,-4.281155,-3.472004,6.948895,-5.177875,2.942010,-6.890493,-8.726589,-8.069943,-9.913497,-1.158174,3.021805,-9.892351,1.784097,-2.922840,9.582870,-3.295043,0.659690,-1.288075,-7.287192,6.626026,6.152416,-8.097338,-5.090029,7.256542,-3.750201,-1.306820,6.205248,4.909885,2.546427,-5.552166,-9.331598,-7.983646,6.643944,2.966880,0.733412,9.183795,-2.646598,1.694502,-0.790117,5.711957,-2.389597,-2.596311,-7.999032,-0.502358,7.511540,3.178102,5.488283,-5.941440,-0.755836,-5.148544,-3.179341,-5.843594,9.392181,4.797883,2.054320,-8.897089,-3.504164,7.759900,-8.919718,-5.070794,-0.995476,1.518197,-4.503095,-5.670628,2.205181,-4.743855,-1.940852,1.413411,-7.059148,4.520557,6.253626,0.847453,4.576354,9.372943,-6.212283,2.482450,4.826732,-5.602473,-6.205423,-9.238823,6.982968,5.189945,8.340759,8.772773,2.208093,4.499354,-2.438595,9.777434,-3.494641,7.427161,-1.368031,7.374633,-1.245509,6.692200,9.462828,-1.736419,7.894377,-0.307929,-6.493362,-7.730364,0.642770,0.875601,7.867574,5.262261,1.488368,-1.364302,2.782408,9.309326,-3.687479,7.010385,-2.423609,-7.004315,0.644462,-7.620137,1.752556,-6.731874,5.144502,-7.567883,-7.611710,-1.564699,8.663004,0.965427,-4.417582,-3.586668,-1.780856,-5.931292,2.735177,-2.184380,-0.946944,5.508680,2.844290,-9.595936,3.276883,2.490133,-5.562659,4.081134,4.634485,-3.812900,5.744559,-1.406449,-3.119766,-4.965858,5.978903,8.690910,2.866706,1.708944,-0.589815,8.357893,9.288147,4.353753,-6.925421,4.470909,0.981431,-3.273343,-0.188934,-2.429229,8.803606,-1.589330,1.181504,-7.786841,-6.291329,-1.145948,8.826233,-6.094048,-1.676883,-9.548932,-4.287388,-2.100179,-9.528133,-8.098618,7.625566,2.077742,4.374291,-3.428294,5.776708,-7.585598,-7.272524,-7.534511,-8.986133,-3.711362,-3.498706,-3.422330,-9.685825,6.564278,2.235715,0.194007,-4.379232,5.288193,7.490103,6.508011,6.034271,-5.170031,-0.585361,2.763433,-0.904913,9.555036,6.819171,5.714564,0.831904,-2.864903,5.221581,1.051561,-3.021415,7.160715,-1.141335,7.464663,-3.587966,-9.613090,-0.764685,-1.628594,5.159649,-8.377306,5.640565,4.236717,-4.595126,9.881468,5.539350,8.437251,8.546664,6.275208,1.127506,9.145670,9.408628,-0.909458,-7.773994,-6.652570,5.957561,-3.932424,-0.576156,5.468772,3.642917,-7.953488,9.533662,-0.399671,8.831153,5.543309,-4.845036,-4.926162,-4.916224,-0.359978,0.937249,-2.425420,3.784385,3.381755,-6.829377,-8.817236,4.226973,9.150193,-7.118910,-9.737881,4.269763,6.393077,-6.774440,0.339935,-1.022813,5.223999,-3.744571,-9.978563,-8.414540,-3.841565,-1.752190,-1.106636,1.093105,9.800593,-0.094652,2.817522,0.937694,1.452453,0.170699,-3.459765,-0.517332,6.034146,9.650390,-0.811017,-5.265317,1.526218,6.431984,-5.109435,0.425509,5.631950,1.674516,1.782071,7.734674,8.230390,-3.147356,-6.621055,9.017063,8.673926,-9.927522,1.125884,-9.037296,7.059124,-1.573072,2.351078,3.727243,5.603808,2.815812,8.413662], dtype = "float64")#candidate|9012|(840,)|const|float64
call_9011 = relay.TupleGetItem(func_4692_call(relay.reshape(const_9012.astype('float64'), [14, 12, 5]), relay.reshape(call_8998.astype('uint64'), [128,]), ), 2)
call_9013 = relay.TupleGetItem(func_4695_call(relay.reshape(const_9012.astype('float64'), [14, 12, 5]), relay.reshape(call_8998.astype('uint64'), [128,]), ), 2)
func_2190_call = mod.get_global_var('func_2190')
func_2193_call = mutated_mod.get_global_var('func_2193')
var_9021 = relay.var("var_9021", dtype = "float64", shape = (2025,))#candidate|9021|(2025,)|var|float64
var_9022 = relay.var("var_9022", dtype = "float32", shape = (315,))#candidate|9022|(315,)|var|float32
call_9020 = relay.TupleGetItem(func_2190_call(relay.reshape(var_9021.astype('float64'), [2025,]), relay.reshape(var_9022.astype('float32'), [315,]), ), 1)
call_9023 = relay.TupleGetItem(func_2193_call(relay.reshape(var_9021.astype('float64'), [2025,]), relay.reshape(var_9022.astype('float32'), [315,]), ), 1)
uop_9043 = relay.sin(const_9012.astype('float64')) # shape=(840,)
output = relay.Tuple([call_8998,call_9011,call_9020,var_9021,var_9022,uop_9043,])
output2 = relay.Tuple([call_8999,call_9013,call_9023,var_9021,var_9022,uop_9043,])
func_9045 = relay.Function([var_9021,var_9022,], output)
mod['func_9045'] = func_9045
mod = relay.transform.InferType()(mod)
var_9046 = relay.var("var_9046", dtype = "float64", shape = (2025,))#candidate|9046|(2025,)|var|float64
var_9047 = relay.var("var_9047", dtype = "float32", shape = (315,))#candidate|9047|(315,)|var|float32
output = func_9045(var_9046,var_9047,)
func_9048 = relay.Function([var_9046,var_9047,], output)
mutated_mod['func_9048'] = func_9048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3579_call = mod.get_global_var('func_3579')
func_3581_call = mutated_mod.get_global_var('func_3581')
call_9066 = func_3579_call()
call_9067 = func_3579_call()
func_3563_call = mod.get_global_var('func_3563')
func_3565_call = mutated_mod.get_global_var('func_3565')
const_9112 = relay.const([[0.803585,1.276151,-4.334181,-7.518964,-4.783332,9.094755,-6.686823,8.799279,-1.065768,-5.337096,-8.024355,-4.197957,7.709905,-9.629098,-2.520936,4.322285,1.903733,8.166239,1.661331,7.387848,-5.847907,-2.895806,-5.481308,0.094733,4.913686,-0.215413,-4.657664,-7.472052,1.656412,7.056999,9.460295,5.508577,5.720786,-3.580135,6.989621,-7.052869,2.243487,-2.111692,4.637465,-9.555649,4.784723,-9.469688,2.098774,5.396920,5.870709,-4.115946,3.404741,-0.622376,-9.119075,6.206550,-9.729770,-2.562749,6.724956,1.873818,-8.754310,3.306439,-2.104258,7.186806,-7.669239,-2.595830,4.266511,-3.396454,7.926847,2.467918,-3.320482,4.613284,1.195391,-1.281846,-6.845677,0.361776,5.472774,-2.393321,-9.143467,7.005176,8.745190,1.590882,5.373771,4.670635,-8.463988,-9.667841,-0.902526,6.288147,8.012909,-5.670388,9.452953,6.157722,-9.917917,-4.625127,2.024377,0.589041,-2.227019,-7.092719,4.962369,-5.635459,-6.832840,-8.522916,-1.990275,-7.284374,3.055610,0.514961,-1.987046,1.972369,-5.002791,-1.533422,2.680985,-2.523094,-1.391463,5.864023,8.310840,1.057506,9.057999,-6.260195,0.897946,3.259433,0.527468,7.930189,9.004756,-8.948040,-8.945758,-3.096067,-1.003876,8.969595,9.471175,-3.103933,-2.209602,-1.336598,6.217794,3.261799,-5.869393,9.360173,9.042061,1.525152,8.927149,9.658348,-6.509543,-2.587208,-0.111452,5.786910,-1.755228,-7.794513,2.015312,-4.087606,1.561784,8.130795,6.904287,6.313957,5.959265,5.913703,-9.560513,7.041304,-5.533531,-0.852872,3.731561,-3.972367,0.123337,1.555372,-5.148870,-9.398094,6.060921,5.692821,-9.678339,-2.406217,9.208520,0.876852,-9.323956,7.412503,-3.068677,2.919683,1.692153,3.118080,9.178786,-6.502712,5.258169,9.259494,-9.411754,2.341030,-0.289001,7.301680,5.108388,9.083483,8.262391,3.987477,-0.968986,2.528245,-2.121071,2.785645,9.190807,3.415955,-2.536098,-1.323196,8.868517,9.145701,6.914723,-5.261933,5.486582,-5.526599,-0.242735,-7.601120,-5.921250,-5.910527,6.289205,-3.262107,7.531224,6.520587,1.304387,1.138844,6.856522,-2.445541,6.325286,0.292965,-2.084573,3.559835,5.136049,-5.122851,1.678263,5.960819,-1.169463,-5.080861,1.998450,6.679268,7.965136,-7.024972,8.664562,2.925889,1.122112,-7.021991,-7.288840,-6.193628,5.584464,2.125390,2.420646,8.978062,6.107914,-6.971514,1.172286,6.506621,-4.653882,7.639439,-2.529262,-0.520430,-8.161978,5.602194,-9.180097,-5.446896,-4.719801,-1.168686,-5.419911,5.714179,1.179044,1.216497,2.103607,6.501462,-9.773430,-9.937445,4.649065,-2.661680,2.809725,-5.422983,2.201413,2.613438,3.692204,6.827372,-6.912311,2.302395,-9.064986,-8.154819,3.985283,7.602576,5.512301,-7.993430,-1.146300,-0.047504,-0.511651,1.874805,3.187601,-8.689399,1.392345,1.125408,-2.718830,2.243848,8.194320,5.962562,-1.887215,-3.704275,-1.487919,-4.773054,0.333406,-9.645722,-7.824760,3.510251,-6.373869,-8.587350,9.074485,7.909416,-7.348394,1.805118,8.535505,-5.538348,7.121452,6.332615,7.199866,7.194819,-1.058292,-1.174213,5.408526,-1.954280,3.212061,1.442403,-1.232913,8.894273,-7.868436,-1.502608,0.375060,3.487699,6.458469,-2.358225,-0.401066,2.259011,1.149834,4.095813,3.095337,-5.472336,-7.875713,-6.165752,4.707275,8.961283,-5.210686,5.295686,-2.968429,-7.493103,6.513239,-2.012941,-2.761995,-5.460135,-5.324319,5.976816,3.369758,-6.728621,6.526842,8.639426,-4.887504,-3.726388,-1.517464,-4.816768,-5.937014,3.950417,1.885896,-0.508567,0.258806,7.252569,-2.781190,-2.544905,1.298428,-4.396759,1.508426,7.263869,-9.999660,-3.362470,2.198821,-2.559638,7.165328,2.856126,7.498106,1.332050,-4.664159,-1.915394,6.376491,-2.765925,-8.929754,8.547297,-4.110818,2.796414,2.438161,-7.294593,0.982831,-3.262529,-2.739964,4.278788,8.898208,-5.691578,-0.723433,7.881715,4.731663,-0.503985,-5.423999,1.007064,-8.320659,7.053339,-3.109007,-0.473844,-7.767320,8.695005,-9.672328,2.881138,7.918676,2.268247,-6.806240,1.253929,-0.126737,0.039603,4.022665,-0.290951,-6.523328,7.967554,7.222094,-2.132570,0.706151,-1.248509,-8.114657,8.653725,9.433727,8.173227,3.408039,-7.659857,-8.095269,-4.160236,-6.126212,4.999098,9.588533,-1.385509,-8.180401,-1.953458,-1.395592,0.136217,-8.422797,-3.428181,7.202936,-6.699351,-3.885445,3.912158,-3.953546,-0.290035,-9.615566,4.590945,8.624759,-6.850723,-1.264853,7.014785,3.117581,-6.147832,8.048518,1.464075,-4.016169,-7.535926,-0.894477,-3.672777,6.604682,-3.186509,-9.624001,1.591711,1.551586,-5.482336,3.517163,-2.533945,-3.383500,-4.645101,4.755788,5.672224,7.390711,-6.627994,7.150555,7.869149,6.448134,-8.891604,7.585663,5.573618,0.197718,8.415827,1.584617,2.340313,-7.493564,-1.968474,8.454283,2.076350,6.348462,0.598563,-0.131696,6.494858,-2.969951,-5.490019,-4.515950,-8.840943,4.007644,-4.235336,2.433734,-5.320306,9.594576,0.159713,-7.641709,-0.241998,-9.219112,-1.388117,-4.468488,-7.413973,0.028644,-9.822450,6.218157,6.449981,-9.222080,3.811943,1.792000,7.188347,-0.148362,-9.717744,-8.879285,-9.544545,-7.359442,3.009744,0.857722,7.112995,-6.153834,-8.393242,-5.078867,-6.422360,8.678963,-6.544627,-3.182810,2.825919,-0.634792,4.339679,-0.283903,9.678397,1.752406,1.735601,-6.781720,8.911621,1.811842,-2.595894,-5.112286,-4.510833,4.938151,-8.526534,6.373967,-6.194656,3.996425,-1.874183,-6.912592,-9.245843,-6.254349,-4.084033,-5.294330,-1.706504,5.414845,9.125351,7.626994,8.785728,-8.334790,-0.537221,0.386292,4.081515,2.222408,5.926395,9.347047,0.098969,6.300152,5.255439,3.466760,1.697052,-2.458300,-8.913222,4.454641,-6.001187,-3.250452,2.954908,-5.810225,-1.422205,-5.954512,6.758769,-9.475171,5.052276,-0.348848,2.138896,-1.185204,-1.510055,-4.147099,9.847330,-1.027228,1.399140,-3.425861,-9.373753,-2.854729,-9.390209,-8.509622,-3.348255,-0.616445,2.794496,-4.422266,7.153102,0.299806,-9.256481,-0.733556,2.788360,9.913657,9.754589,3.898715,-2.019713,9.004326,-2.228998,-2.410220,-5.726122,0.730525,4.902464,-7.119054,-4.736698,-7.290218,6.003521,-6.231296,2.261143,-7.305212,-2.920386,6.519733,3.800055,2.700554,-7.819291,-4.404291,4.347251,-5.161595,-5.264795,1.431100,8.714259,6.706729,-7.541076,7.688495,2.237968,6.341752,-4.016996,4.392567,9.044745,4.802462,-6.357265,-9.167001,9.592832,7.254669,3.593732,4.483814,-7.666284,-0.433289,-3.060313,4.574523,1.189766,9.342985,2.222189,8.700789,-3.935228,-0.815110,-7.357717,-3.821439,-3.126835,4.174947,-0.668208,-6.307258,2.335689,1.158908,-5.655886,-1.633310,6.339406,7.714925,-0.691383,1.313498,-1.664569,1.707950,-0.263605,-5.566373,8.988813,9.886120,-6.608799,4.874528,-5.543911,-3.052056,3.267453,-3.196377,-6.518679,8.814174,-7.881142,2.754727,-7.659498,9.566624,-2.523030,9.332910,-6.853663,3.464497,-5.749341,-9.950224,-0.209319,-7.343839,5.458541,-6.610636,-8.488981,-7.950967,5.250385,2.247548,2.614229,-9.080429,8.524225,8.097329,-7.169693,-1.189821,8.558876,2.989797,3.172787,6.775219,-7.951571,5.725827,0.372266,9.782225,5.806329,7.571168,-4.770334,3.261720,2.027902,1.797702,2.878897,5.630729,-7.413625,-3.552759,-6.418313,9.565093,-8.238021,3.298042,-9.587007,-9.845206,-8.970505,-5.701689,0.890383,-7.525858,3.448470,7.562702,0.748805,2.931054,6.722951,-9.148640,-5.202799,6.343539,-7.149488,-3.294698,0.021403,-7.552268,-9.142261,-9.103997,-5.039245,6.159068,-2.681423,8.176357,0.418433,-1.588024,-2.615260,-5.238316,-6.947471,8.719523,-7.786346,3.522058,-7.572488,7.600940,7.202788,2.834835,-3.652380,0.959569,0.158775,0.554120,8.096273,1.418991,-2.309630,-9.394190,2.019237,9.863347,-2.114037,-9.007766,-0.296061,5.138274,6.908377,-9.687183,3.089801,2.535471,-0.926160,7.340169,-5.042116,8.953781,-2.469500,1.809514,-8.265277,-9.335306,9.041203,4.924986,-3.767581,0.399782,2.246675,-2.274245,4.456152,4.130478,-1.004420,-1.218255,-1.024284,2.611967,5.958330,-5.533628,4.642471,-4.291886,7.123411,-6.129385,5.469251,-9.874074,9.793132,2.427784,-6.497827,-3.767920,-3.007731,8.310456,8.698706,8.671161,2.998181,-2.909541,-6.397410,3.555831,-9.637668,-5.205040,-6.849917,1.654450,6.818346,-6.812190,7.979321,-3.493067,9.483040,-2.402444,-4.400419,-7.361805,-7.371176,-2.915744,1.757455,-2.162438,1.149198,4.776272,2.253808,-1.641818,-3.923882,-4.520731,5.873889,9.697757,-3.205584,5.201951,8.273826,-3.418298,-8.765390,8.333418,6.229147,-5.382901,-3.306110,-5.176979,-5.467043,-6.386223,5.764663,-7.241847,3.107374,-0.878853,-5.574158,-2.705694,3.380560,5.479303,6.321325,8.467059,-6.594848,7.385253,-9.425134,4.339170,-1.277551,1.889834,-1.086113,8.836495,3.829880,-6.520486,0.581832,0.232434,5.920924,2.896063,9.690117,8.654262,-3.614132,-9.103386,-2.159190,6.567925,0.239761,8.850125,-3.736880,2.557956,-7.340939,3.809954,-0.987638,-5.995365,0.367204,-1.573305,-0.596142,8.263983,7.028201,0.741818,4.153691,-8.161791,9.830732,-1.365334,-6.506746,7.087365,1.303931,2.886073,-0.055566,-7.597913,0.118008,-2.663850,-8.538412,-7.416391,-9.860846,-0.601309,-0.471820,-1.642648,-2.013089,7.349048,5.431214,2.064941,-1.247274,-7.314329,-4.812917,-7.736403,-8.757573,5.737726,-7.017338,-8.309576,-8.000563,-5.059624,4.300593,-1.937472,-0.845550,0.049767,7.549182,-2.936183,9.837148,-1.833760,0.879100,3.990971,5.362657,1.596059,-7.507331,-3.400174,-9.645474,9.545984,-4.529884,8.036442,0.006976,-5.465966,4.114429,-1.774839,9.595095,-3.968466,-7.523750,-0.202198,-5.203835,5.311121,0.015104,4.799516,8.952652,-7.268900,2.326827,-2.456369,-9.306374,2.397641,8.704387,-4.516139,-7.804661,-0.906027,-8.388035,-0.384925,-7.997008,7.274470,-4.401966,4.647834,2.242955,0.535993,3.260622,0.765532,-2.355459,3.506023,4.903532,-8.671823,-8.168751,-9.522397,-9.159371,0.475470,-0.003703,-5.268183,-1.588341,-3.363877,5.947506,-4.656298,4.065797,-4.868021,-6.842001,-3.136517,8.498513,8.314007,9.117054,-2.230660,-0.152335,-3.949076,-7.541142,9.650606,-3.865381,-7.299999,7.428533,-5.696425,4.396244,-9.828960,-8.324930,5.838022,-3.674420,0.519644,-3.612888,9.981852,5.330553,1.578999,-5.904769,-0.485154,1.207248,4.948730,5.029132,4.224399,-0.515797,-7.497821,-0.717798,5.372507,-7.019211,-0.626614,-7.616984,-2.078440,5.687384,-8.889842,-4.207764,-8.378360,4.965262,5.530767,1.526331,5.824406,-3.432607,-9.145125,5.670267,6.004450,-8.902949,-6.686711,6.753110,5.133477,9.510302,5.118189,-9.156107,4.054512,0.565613,7.541280,0.727867,-8.348045,-5.966582,2.678783,-3.176236,-7.290799,-2.863816,-7.887683,8.987855,6.698244,2.057600,-7.934897,-8.738904,6.797994,-8.812808,2.257317,-3.867229,-4.871946,-1.322602,-2.124105,-6.182358,-0.062053,-3.492975,6.457634,-4.543195,-1.041292,2.731786,0.980989,-0.876659,1.873912,0.829383,-8.334796,-8.049931,0.657147,-7.458206,-8.026177,-5.673222,-5.234469,4.970701,-4.404685,-1.860840,6.716755,6.333994,3.492097,5.244530,5.601340,3.224534,-9.282468,-3.067489,3.483867,-2.107484,8.009452,-2.776644,1.291543,4.716644,2.362155,-7.036662,4.535243,5.134401,2.165022,3.594914,-9.636897,-1.012188,4.269980,-9.152767,-3.675522,-7.066207,3.216502,1.528398,-0.203836,-1.335161,-4.148895,-5.963841,-5.878316,-5.840057,-5.590226,-2.175527,8.277859,-3.647538,1.725825,4.315584,9.343578,-7.213437,-9.914147,4.257508,-1.365739,-7.049986,-2.140785,8.271551,-5.674645,-6.001305,9.955664,0.340001,5.101344,6.953734,-6.907350,-9.281878,-1.139316,-9.091530,-2.811381,7.466701,5.604474,4.215053,-0.156952,5.425966,4.121061,-4.572837,-7.389259,1.470807,2.557724,7.395999,4.320319,1.104524,-7.624372,-4.888918,5.783307,6.552193,0.099895,-1.314584,6.221993,-9.870187,9.414214,-8.821230,2.111618,5.996843,-1.575164,-9.506576,2.701482,-9.030442,-6.705062,-9.123432,-0.671407,-9.983809,7.054052,-9.461139,-5.481034,6.270623,9.436659,-0.482488,2.501503,9.308961,-4.123227,4.796836,8.403148,3.532179,-1.109552,8.548384,2.689874,-3.401457,-8.889786,-7.541741,5.157907,-0.341802,4.362575,8.562511,-9.533528,-9.521969,9.553801,-3.792621,4.521554,-6.570772,-3.704513,1.340689,2.445172,-2.438271,-3.474651,2.083152,-3.436253,-3.491092,-4.480355,-8.642255,-0.267307,8.148427,-6.071336,-6.868903,8.218045,3.415678,-8.551030,9.748825,-4.777070,2.303201,-1.340597,-6.267830,-6.161610,-1.436919,9.128081,6.229528,-7.689745,8.968167,9.779519,-3.333861,-9.931696,-1.834263,-9.235851,-7.523526,4.561654,2.246096,-5.166788,-2.911604,-7.544372,7.132099,1.794108,0.424453,9.273041,-7.642787,-2.009034,8.329307,-7.197653,8.359281,-4.036333,9.674546,0.006953,7.268325,-9.795356,-2.221357,1.118422,-9.893714,0.991114,-3.432010,-0.475130,9.327213,0.514311,9.203206,-3.746055,9.316161,1.285778,-5.759645,2.864026,-6.189088,3.600579,4.142027,0.842978,5.602745,5.844283,2.732081,-2.712177,2.735844,-2.460045,2.904431,1.252435,8.376572,2.965647,-6.380057,2.348900,-8.963153,4.668593,7.305484,-6.034938,5.300238,-8.637581,3.347464,5.471906,3.711608,-6.446054,-0.491755,7.407492,-0.717568,0.728513,2.475494,6.381637,8.340376,4.607045,3.215438,9.937094,-9.729407,-9.423731,-3.269669,-6.987414,4.279788,-9.043031,-7.043749,8.234850,-0.807211,9.710681,4.023015,-4.333714,-9.959462,-1.272539,1.943553,-2.855768,4.675468,6.829701,4.994371,0.155768,-1.671795,-6.038900,4.368269,9.710948,7.316096,-8.688225,-5.129509,1.094668,-0.821064,-7.100116,-1.526468,7.059568,0.908665,2.738448,-2.638581,1.916109,8.612731,-1.005356,1.369993,-4.777610,-0.383232,-3.387711,9.298889,9.774092,1.002009,0.358375,2.576542,2.375992,-5.362470,2.270442,-1.776848,1.406082,-8.503337,-1.178432,-4.098987,-5.497030,0.212434,4.420251,4.916638,1.970305,-2.064836,-3.419737,0.108947,5.073845,-9.294369,3.388657,9.501994,-6.528985,-1.542566,-1.578432,-6.263472]], dtype = "float64")#candidate|9112|(1, 1386)|const|float64
call_9111 = relay.TupleGetItem(func_3563_call(relay.reshape(const_9112.astype('float64'), [9, 14, 11])), 0)
call_9113 = relay.TupleGetItem(func_3565_call(relay.reshape(const_9112.astype('float64'), [9, 14, 11])), 0)
func_6520_call = mod.get_global_var('func_6520')
func_6522_call = mutated_mod.get_global_var('func_6522')
const_9120 = relay.const([5.583550,1.301890,-4.936200,-4.702753,-7.587426,-6.056337,-8.067896,3.961797,8.892412,-5.721329,6.986740,-4.019928,7.087516,-0.645000,7.088836,-0.164251,-1.290801,-4.167062,6.562163,-8.618264,-2.368636,8.328355,8.886034,-0.369527,-7.358010,1.216851,3.130243,-2.309919,9.711080,7.243581,-1.617076,9.639770,4.857841,0.344278,3.938565,-3.594103,7.503630,-1.388743,8.876230,3.394105,-9.495507,8.242444,9.372341,-1.544192,9.748777,7.020322,5.263419,-4.228867,-2.107598,-3.918687,2.365993,7.387985,-1.846407,5.683915,-3.109182,0.736568,5.047174,-1.622784,5.738329,0.772661,1.364608,-9.424605,-7.607587,6.338513,8.921074,-3.737719,2.801884,3.234574,2.483800,6.537402,7.805143,-1.623794,0.798441,4.949038,3.099822,7.511261,-9.646121,-1.535538,-1.528007,0.717736,5.793900,1.826058,-3.752086,-1.057464,0.134020,0.105152,-2.399118,-5.742568,4.873607,-2.526815,-4.983606,0.430000,-1.003346,1.251459,5.946465,-9.449047,-0.019637,4.984470,-1.507401,5.304490,2.249576,-4.557609,-9.496409,-3.122315,2.242535,8.093401,-0.486420,-2.225845,-9.697578,-2.277760,-1.838983,-2.907470,-6.007142,5.583775,0.467071,-1.869986,-4.589033,-8.114885,7.654470,-8.289412,-9.583519,2.414064,-2.253042,7.989402,2.674378,-5.611097,-6.818141,3.542287,4.151402,7.438235,0.694722,6.646273,-9.267624,-8.046617,-8.671978,-3.596759,-1.604054,-3.191520,0.330624,9.048837,7.942260,8.110105,-9.445344,-4.851510,2.356703,-1.558538,0.347122,-1.200447,-1.352984,-0.740679,5.551102,9.390985,-1.933448,-0.518274,5.408742,-7.824978,-4.842426,-8.417677,-5.928603,-2.628304,-8.326523,-6.708922,-7.531600,6.510206,-6.337623,-7.940847,8.609167,1.295637,6.193651,9.507224,-5.103480,3.992406,0.491870,8.533990,-0.840002,-5.989369,1.413870,-7.717026,7.546879,-6.834344,3.590859,-8.000661,-1.347318,-3.010167,4.561176,-4.985139,-9.262572,-8.376969,8.546858,4.242808,4.292326,-6.737251,4.939030,6.938017,-2.774671,-3.710932,-1.479210,-3.124333,-2.761497,-2.766198,3.980331,2.968167,-3.120896,9.682894,-0.487768,5.648326,-4.853676,-7.448776,-0.535143,4.656145,8.154066,1.706685,-7.927172,-7.502668,-6.521967,-3.634912,1.821017,6.663123,-8.760740,1.884321,-8.402941,-6.846126,-3.175291,-1.447299,-1.584724,5.625507,7.005026,4.101917,9.222213,-6.418125,-5.076993,4.779664,5.982587,7.589179,0.818997,-5.409127,5.513966,0.773753,0.594377,8.101485,8.528751,5.355042,0.748409,-2.455256,-2.071598,-5.854048,8.388967,-7.932743,3.181420,-5.838106,-9.512969,-9.766044,-6.790253,6.583856,3.282600,6.263069,0.024087,4.249991,-1.854137,0.501649,-1.263395,4.562149,5.706095,-4.735924,-7.980993,-7.245432,2.634660,-2.710166,-5.598368,6.132265,-0.835264,-6.575900,0.198100,-7.160713,1.750331,-4.139838,-9.678164,7.946293,1.911745,-1.738331,8.982216,-5.450163,3.136780,-7.026013,-3.943075,4.649520,-0.945864,7.286073,6.185346,3.209870,5.260464,-0.335352,-0.656893,-4.094585,-4.271260,2.065341,5.806911,-5.444233,-4.565515,-5.112992,0.241753,-2.182142,6.720971,3.570432,9.220786,6.061825,9.134654,-5.140919,8.767980,3.384668,1.128071,4.652072,4.499372,4.211748,-5.483360,-4.324435,9.233738,-2.065266,-3.090066,8.713706,-0.068946,0.803650,2.332280,4.925791,-6.660002,-3.334222,0.001573,-7.498664,7.113970,4.887900,3.391837,2.004215,-9.814159,2.777924,-3.964539,-3.114389,6.016920,-1.650942,-5.221460,5.690498,-7.601710,-5.170210,-0.365625,-3.679146,4.865645,4.623344,-5.193697,4.799438,-9.849863,5.927174,-3.089380,-6.725510,3.294647,-3.115201,-7.370735,-4.684292,8.333777,1.056477,8.894187,6.056440,9.823524,0.376162,-2.434099,-3.372242,5.000419,2.453877,6.835199,8.101999,-4.820115,-8.720953,-8.104336,2.794614,-5.716478,5.257420,8.674269,-9.715801,1.032788,-1.820876,-4.940215,8.370675,-8.616354,8.797726,-7.607003,6.129148,-3.267487,3.948881,-3.625660,-4.037674,2.172127,3.812811,2.565907,2.187225,2.620218,-1.414184,-8.801083,-4.568634,-6.403790,4.136547,-2.465911,2.226812,-3.130480,6.095980,6.049657,2.868880,4.371741,4.902851,-2.548293,-9.143633,-9.961190,-3.158807,-8.588649,-4.354287,-2.510857,2.760314,-9.633786,-4.894483,1.844528,6.764530,5.439080,-9.060922,4.776719,8.081436,-4.421866,-1.886917,-7.454343,-3.034990,8.209480,5.691754,-6.708359,-0.752155,6.211608,9.743981,2.895547,-6.181711,-7.265624,0.507519,-0.163281,1.102426,-4.136095,-9.247947,-6.570120,0.967924,3.448652,-6.305609,3.535559,-4.343244,9.300728,-7.733549,-1.512739,0.480347,0.380468,9.394010,-2.762170,-5.227422,-9.512249,2.269172,9.091164,-5.650079,-9.470832,-3.196586,9.957468,-9.597713,3.307515,8.011583,8.726104,-9.857627,-7.036039,4.884849,-0.945815,8.047088,-4.272413,-1.132087,-7.388962,-1.280481,7.033456,-7.997861,5.419743,8.405851,2.146046,-3.139042,3.154218,9.208565,-2.303900,-8.488092,0.443672,1.403880,1.489965,0.208277,-4.389105,-4.459287,6.957451,0.524196,9.809500,2.388153,8.921331,-7.953066,-1.612440,-0.410914,-7.216434,2.780017,4.085734,5.609352,-0.551770,-7.970515,-2.909148,-6.568361,7.328097,-5.220158,-4.256690,-1.921408,9.727905,4.934875,-9.880961,9.317892,-4.122717,-9.717955,7.178982,-5.402227,8.655900,9.870607,6.511158,3.350108,7.175828,-1.152645,8.666702,7.651694,7.108686,-3.079045,4.970001,-7.693433,-7.956318,8.092562,-8.230214,-6.473156,-1.709886,7.827369,2.290902,-4.713862,-4.732456,8.114728,0.105268,-2.703434,5.505935,1.790427,-9.373852,-0.094535,-5.941646,0.274229,-7.593691,-9.647708,6.914779,-1.041397,-5.370182,1.107106,2.432478,-3.763088,2.956827,9.903942,5.719145,3.565744,-3.985599,4.870526,3.691015,1.451237,-6.804872,-2.950982,5.894587,-4.250672,-0.355991,-0.345198,-0.565121,-5.766779,-2.690206,-0.324107,-1.541742,0.053801,-9.296160,-4.572660,5.065936,7.977503,9.644215,1.672230,-6.412505,8.533400,1.625706,9.785095,-9.564520,-0.107046,8.283180,1.549918,-5.468870,8.684707,0.178358,9.312755,0.719997,-8.814356,-1.511802,-6.364059,3.563793,0.284087,3.626468,7.085649,9.216516,-6.503828,-9.166348,-5.793669,3.184500,8.352454,6.376625,0.352972,9.505579,-2.375793,-4.913234,7.250397,-1.529624,-6.037756,5.928665,8.875605,9.917578,9.250277,0.245363,3.036879,4.099501,6.526213,5.659957,-7.804411,-5.070853,-9.324969,1.564181,4.777200,0.093172,3.282951,7.374612,2.950598,5.770654,-6.469418,-5.625587,7.243322,1.030935,7.811653,5.002614,1.394345,-8.344791,-9.953181,2.314697,9.252693,-9.852487,1.994645,5.980632,-2.419718,-4.046608,-9.839882,-0.626967,-5.015632,-6.811509,-9.045880,7.604564,-7.314612,-1.072982,6.328569,-0.346572,-3.380510,-2.184254,-3.789951,-1.669362,-8.495299,4.599284,2.815429,-2.986797,9.345019,8.886041,-4.599183,-5.221247,-1.839307,-0.737102,-2.546258,-9.521617,6.478172,6.697466,9.562937,-5.317187,-8.366478,-6.789774,-9.594558,3.809740,6.611398,6.722422,-1.066158,-8.249023,-9.090228,-8.203532,9.243002,8.010105,4.580708,-3.903644,-8.226092,-3.921697,1.560868,0.326178,2.983443,6.287937,1.672896,3.336136,-1.192584,0.100180,-1.654710,-4.402063,-7.661668,-6.619110,-6.926756,-4.163455,4.252895,1.360020,2.667257,-2.977696,0.902520,-6.765028,2.944181,-4.134133,3.372103,-4.548574,-8.825422,-6.304656,4.220081,-2.587884,4.754624,-0.070889,-7.029346,2.362537,-9.590039,-3.441600,-4.805181,3.961905,-2.974110,9.664630,3.647053,6.380738,-4.854801,-5.456942,-2.475238,2.531615,-9.156566,9.425774,4.970478,-8.306259,-2.073995,-5.285306,0.346004,-8.379036,2.923124,-6.423754,-0.960854,-7.230645,4.470550,-7.955077,-8.667756,8.315964,8.309020,8.807702,-1.299069,5.998556,-3.502646,0.468660,3.233305,-2.797634,9.285976,9.849084,-1.377478,8.650382,-9.417531,-1.272181,2.977667,2.206262,-7.569250,-7.577613,8.272218,5.627125,1.555863,8.851894,6.431590,1.722629,-5.231075,-4.310459,8.201487,-7.964886,2.282312,-6.582946,4.850291,5.163485,-0.775276,-5.050597,6.718763,5.542765,-0.716260,8.572469,-6.984462,-0.114160,8.939168,-9.385099,-6.305201,9.575403,4.582304,3.305582,9.475369,-1.982535,-0.348831,1.444636,-7.367666,-0.519891,-6.049026,-7.996227,-4.905893,7.646450,3.766232,-6.652294,3.018489,3.229495,8.781683,8.585831,-3.297249,-7.146561,-8.232668,-5.063359,1.328926,6.503495,3.718377,-4.742984,-0.105441,1.420755,4.384755,-9.028530,3.208448,4.716808,-9.507286,-9.397397,-2.833193,0.783065,-7.943671,-0.090547,-7.406551,5.954154,9.590134,9.712207,-1.728974,-5.025265,7.430797,-2.515279,-4.140894,3.188252,-5.527723,0.179204,4.421632,8.518261,5.912698,8.800081,4.849445,7.251801,-6.670615,-9.772142,7.351752,3.484698,1.647012,-2.660425,7.483849,-3.757739,9.249759,2.714323,-9.136696,-6.007836,-5.331486,8.773275,9.387935,-2.813826,-3.899076,-7.084264,2.934238,-5.331528,4.381422,4.465800,-5.567369,-7.868774,3.704127,-4.786793,-1.251098,8.109526,-8.035985,-8.217387,9.652784,-6.859993,2.840040,-4.057027,-8.004759,-7.998177,6.541908,-8.912880,8.844322,5.681274,-1.797794,6.555093,-6.084095,6.729415,0.775803,-2.591002,5.644149,-2.101416,3.614550,0.219067,0.931506,4.803996,8.405350,8.774518,-3.086215,-0.347923,-1.434397,9.556271,-0.367500,-7.304379,-9.307907,9.366670,1.763203,0.549665,-2.809694,-8.586935,-7.098402,-5.696066,6.495357,-5.084015,-5.352587,8.628037,-0.575294,9.297420,8.681895,6.481519,7.610557,6.201875,-9.638884,0.256996,-6.869283,2.085035,-6.791901,-2.261165,0.504341,6.805256,4.453896,-2.041534,-6.737629,9.715840,8.572380,5.480979,2.122148,6.347811,2.127798,-0.858474,-1.139496,-2.906352,6.484353,1.372915,-0.667783,-0.971798,7.316661,2.658615,-1.170601,9.957588,0.802501,-2.668090,-3.406743,4.129847,2.649962,6.221916,3.863568,-6.334817,-4.194808,9.760671,-2.642875,8.184297,-8.866747,0.018132,5.596054,7.123930,-3.979986,6.793253,0.547334,-7.858025,-1.262335,8.560941,-2.483622,-8.243558,1.988729,5.081340,6.583950,4.573779,2.814720,-8.153647,5.413605,-7.077008,-9.185573,-8.255347,-8.184001,-0.782660,-2.363970,-1.355385,7.800021,-0.709648,-9.085436,-8.401692,-0.251858,5.648985,0.905894,-4.772433,0.664706,-7.443878,-8.396487,-5.094117,1.431788,8.616748,-4.612931,-9.126304,-9.720464,-1.751192,-3.520360,-4.918170,-5.350645,7.037594,4.503014,-2.137741,-6.524462,-9.110834,-6.493152,8.218796,8.289545,7.132817,-5.376987,4.740779,-7.672709,6.939530,1.590871,8.503553,0.720080,6.037444,-7.669894,-6.683542,-0.499667,8.188158,5.053937,-8.123198,0.324451,-2.329632,-8.794460,-2.867814,4.764776,3.306668,6.013466,-2.637611,4.791574,-3.489842,1.591778,-3.747408,2.191326,-3.613067,-4.187612,-3.027615,7.088390,8.991129,-3.178767,-0.865376,3.767236,-1.189239,5.526224,-7.911568,-4.416926,-7.483770,7.830349,2.035190,3.283188,5.251331,2.865777,2.262075,-4.682465,-5.399376,5.670427,-9.092798,-4.826322,1.073860,0.359469,8.419707,-5.013771,8.030322,-9.584462,1.577211,2.898800,-1.204913,-9.139778,7.927232,-3.786548,3.666897,-7.853847,3.598278,4.953849,-4.924847,-7.438083,-9.845156,-5.848769,-0.895993,2.873125,-1.118903,-3.974163,5.526909,-9.473065,1.156643,-3.979347,-3.458634,-8.713707,8.965596,9.011597,-2.827010,8.506485,-9.684561,-7.656073,4.288674,-7.865362,-2.672154,-4.039191,0.483543,-9.267308,7.804131,-8.979676,-2.213445,4.858233,-1.107044,9.898939,-0.412573,2.049339,-7.433518,6.508854,0.943669,1.783341,-3.629125,1.712366,3.553765,-2.524647,-3.069774,-2.009924,4.845548,5.769405,-1.202351,-1.659750,1.146648,-1.557928,-6.141125,5.898492,1.732661,2.868060,-9.899515,-5.267462,4.705462,1.343462,4.108303,-6.689940,2.434027,-1.489429,-4.670463,0.510656,-4.922270,-4.823069,4.325787,5.875534,-0.317917,7.555655,2.872609,-2.688395,-4.617758,4.929011,-8.901001,2.331713,5.169281,0.712847,-6.410429,6.237793,-3.254891,8.252502,-8.260494,3.705947,-1.183347,6.378216,-3.251846,-3.633641,7.830988,-8.961189,0.808093,-5.623454,4.246385,-4.712275,-9.204009,-3.298010,5.476827,-1.401655,-8.580287,6.591916,-4.656444,5.810343,-8.650920,-4.828607,7.600818,0.582695,-3.574362,0.457456,-0.949931,5.499138,6.032516,4.903636,-6.526207,-5.223243,5.912531,8.563142,1.167725,-9.241187,-5.070742,6.871132,4.911989,-6.524001,-2.313121,8.747280,3.253780,2.860782,5.698262,-8.305375,4.344134,-9.148678,-8.029737,-1.132325,-2.835823,1.649028,4.361341,-2.891537,-4.974464,-8.405329,-9.503676,0.495719,8.871287,6.760775,3.587045,-2.755990,-7.269028,-0.559017,-7.081067,-9.183523,5.561580,7.565099,6.468795,-8.184988,-0.790907,-3.584227,-2.364409,-6.786110,2.496132,-4.519067,1.284039,0.006014,-3.386239,-0.678247,-2.142769,1.355259,5.557254,1.545142,8.137282,-7.562738,-1.799421,-0.013476,-6.911027,-1.356246,-3.492772,-5.790731,2.478853,-9.235167,1.874756,-1.736048,5.593923,-8.114517,-6.676772,3.374782,5.000546,6.833449,7.716841,-8.088591,7.829766,5.550369,-5.146448,7.314498,8.475523,3.344912,8.820200,-9.195684,3.822598,6.683742,-6.373700,9.929271,-6.377030,-6.867891,4.650593,4.428464,5.911673,-1.503413,-3.408184,-2.824798,1.340444,5.935572,5.412498,-3.307097,-3.828584,9.705657,-9.167192,-4.684593,1.727589,-1.873610,9.705251,7.960866,-2.563440,-6.962528,-6.205294,-4.353987,-1.448271,-5.065838,-6.479391,3.115421,-7.837055,1.986898,6.218735,2.563193,-3.918657,3.912574,1.985998,9.490313,3.316338,-1.906462,-2.950103,4.097830,-4.925496,-6.922612,-4.617060,6.904129,-5.675293,-6.110325,-8.057752,6.417189,5.160762,1.615301,3.890642,1.656480,-3.766721,-7.390485,-0.208499,-3.771614,5.039440,7.147970,-2.433196,-8.397105,-3.201778,-8.492783,-4.725667,4.483764,8.758436,-7.005332,5.247511,7.410105,-1.796118,-9.367939,9.884910,1.643672,-6.837413,4.714401,-9.447971,4.516591,-0.309403,0.939553,8.651287,-6.943121,2.600092,-0.303701,-0.731709,8.777732,0.012557,-3.419956,-2.445292,-5.698636,-1.223174,3.425338,0.547255,0.049204,-5.747576,4.870923,-1.087764,-2.209021,-0.558323,-4.660471,-6.490582,6.207068,-5.220034,1.312117,-6.556776,8.600925,6.035306,1.898958,8.700289,-9.785481,7.229568,-7.854720,4.216575,-8.853844,9.637205,3.338965,-9.075398,2.154731,-1.690106,2.700325,-7.170056,9.511132,9.976755,2.277730,-1.600857,-0.372654,3.136451,0.225622,-9.451703,-9.724914,-0.458067,0.408559,7.831843,5.764387,8.780206,-4.439897,4.220273,9.333910,-7.640592,-4.171780,-3.911248,-2.891973,7.222401,3.549990,6.482839,9.987982,7.509213,-7.772348,2.507197,-7.699483,-0.231417,5.454842,-4.913956,-6.744361,1.459695,8.924788,-3.429427,1.598962,5.765097,9.087954,-1.122761,8.672818,5.373210,-1.008291,5.162689,-7.754924,2.496823,-4.259245,-8.762246,-2.237663,0.116404,-2.891329,-5.567466,9.092099,-4.235194,-7.461199,9.017685,-0.681250,-6.277498,1.958502,7.511443,9.026863,8.556078,-9.745312,0.049072,7.206059,0.032746,-7.217484,4.231709,2.895985,-7.744923,3.730430,4.879759,-5.234125,-2.295886,-8.329853,2.829172,8.296304,5.515083,4.210679,-9.159168,6.879310,-7.868636,0.232567,3.837638,9.623634,5.454691,8.675063,-6.436171,-0.516449,2.852614,-1.910350,-3.579592,-1.253498,9.427005,-7.384142,-3.201152,9.138034,3.338098,6.714522,-8.304196,-6.969823,7.561199,-4.852070,-6.445841,-3.230308,9.599777,-2.778319,-4.806806,2.223553,-9.632644,-1.899271,6.835589,3.484468,-7.409778,0.456029,2.376497,-8.342005,1.273942,-9.029146,4.256098,-2.097823,7.288256,6.125312,5.200521,-3.574056,-1.450497,-2.976579,-8.477509,3.306785,-8.638991,1.575808,-7.853302,-3.832859,9.646016,2.353421,-1.188903,0.838044,4.379850,3.349248,-1.651923,-4.233536,-3.782028,-8.751162,3.042198,-8.763917,8.446148,9.150286,2.922185,0.380493,4.135440,-4.308257,-5.493678,0.203542,-0.081100,-6.067009,-1.782315,9.341621,-9.042407,-6.963293,4.595290,7.768342,-1.116330,0.994326,8.143621,-4.148265,9.940451,-7.105514,4.551011,9.405737,-7.358764,-1.899445,8.875834,-8.746618,6.345026,7.810374,5.805384,0.795723,9.353140,1.853873,-2.533901,4.475979,-2.169638,8.344250,-9.746563,7.701935,8.530948,7.657222,-4.961906,-9.395243,-1.482029,-7.267584,-3.367996,-5.031919,-4.000034,-4.353402,4.101586,9.198357,4.517673,5.655479,5.862185,6.675129,-2.542874,4.411607,-7.006484,6.003422,4.263900,-8.803727,3.547611,-9.009859,-1.057872,-3.943368,-0.634894,-0.650205,5.554422,1.385944,-1.159976,9.556975,-2.424137,4.705019,-5.325097,3.755790,3.562759,1.675096,-4.555098,-0.702256,7.569335,4.440258,-3.541373,7.394193,1.289044,5.994846,4.882219,0.009934,4.548183,-2.403529,4.056113,-1.544752,8.825537,3.007559,8.139787,7.607564,0.531284,-3.156331,-4.909268,4.241616,6.424170,8.465364,0.732848,-7.186368,-9.652077,-1.905948,-8.346880,-4.363252,-2.590153,-0.470680,2.060895,-3.278193,-1.266342,2.294362,1.287156,-3.974448,3.986436,1.292521,-9.282163,9.949458,0.546046,-5.072179,-7.032671,4.606003,7.595154,-0.222125,1.118604,5.475219,-5.485425,-0.731946,5.127934,-5.109961,7.325020,2.738717,0.258217,-7.806048,-7.246832,-8.394136,0.643427,4.482361,7.639659,6.185610,4.334094,-7.529095,8.382599,9.204790,-1.826600,6.526809,7.900541,2.693877,-5.132900,1.669506,8.312372,2.320647,-7.130145,9.743616,9.145071,-0.219475,1.310275,-3.637379,-7.762054,9.629367,6.665134,-8.327726,7.047326,9.492719,6.282531,-6.716702,-8.937434,7.995717,-6.669638,6.395978,0.616694,-4.009715,-1.116313,-0.597761,-8.231131,1.384283,-2.824464,7.033143,-7.988073,6.603718,2.145244,-3.673952,-3.023390,-6.394028,-6.443848,-8.958513,-6.544265,-1.719788,3.475283,6.329939,-1.493600,2.563141,-5.835961,-4.483735,9.617709,-0.743143,4.002956,-4.851092,-6.248529,-1.462460,-4.941376,-6.360977,-9.532510,-9.384384,1.614894,6.660051,-4.255333,6.598026,3.304777,1.552441,9.709758,-7.741226,-3.816709,-0.232446,1.766255,9.327226,9.780103,-8.578180,-6.885635,4.567090,-5.615026,6.076890,5.196435,8.435739,-1.936891,1.931871,-0.495461,-5.166472,2.818700,2.958842,-3.532981,-3.691423,4.125656,9.750195,0.512991,3.505603,8.998461,1.647706,9.482282,-6.597227,1.298744,-2.729494,6.648482,7.560219,9.688563,1.585424,0.834088,-0.459112,8.332915,1.209523,-1.840212,-9.523605,7.604096,6.438274,4.764011,1.413329,9.475724,-0.601477,-2.852585,9.344707,1.691139,0.817194,9.865057,9.488474,3.967124,8.293425,5.310136,-6.239338,1.600760,-0.943386,5.891043,-2.785665,2.716991,0.763604,-6.908120,7.323801,1.279668,-4.051995,-0.501912,6.945427,-5.466363,-1.757996,3.616518,4.908612,-8.983113,1.334539,0.763696,-8.911644,-6.599061,-1.927890,7.169606,-9.186471,4.757448,6.697601,-6.800765,4.156018,7.363986,0.279867,-2.477354,-5.914526,-1.063700,-0.815978,3.383222,-4.448567,-0.075581,-9.529296,-5.552158,2.352834,3.574125,-0.322076,1.218475,2.728134,3.071864,7.223713,0.831955,-0.785876,6.950076,5.233036,8.548681,0.838936,-5.829672,0.517038,-6.009771,-2.867370,2.815531,-4.730403,7.601767,-3.747694,-2.791183,-5.642230,9.679498,5.475569,-7.703374,9.327912,-1.664883,2.937266,-3.635263,0.767067,5.651037,-4.396083,-4.336541,-0.432292,-4.386900,-6.767149,-1.059464,-4.899239,8.596667,4.441706,-6.167731,-9.496395,1.904895,-2.748580,-9.524284,-1.256206,0.077011,8.951008,4.617943,0.179894,-3.694277,-7.250639,6.819563,-2.722967,-9.124241,-1.282043,-1.706189,5.714482,-5.587608,1.763913,-8.423148,1.303935,-4.561739,2.104566,-5.345819,-7.388695,5.757645,4.799122,8.187940,2.018746,6.423530,0.279686,-8.717412,4.488497,-5.673317,-3.158904,4.867485,-9.308764,-1.855600,6.323426,1.557009,8.330800,1.854467,4.198231,-9.305647,-3.781129,-1.169116,7.627346,6.596243,1.164199,6.897312,-8.750090,3.539196,-8.992423,-2.892523,-1.748879,2.980438,-0.762696,4.188290,-1.553508,9.143582,2.651918,-3.966122,-1.577589,-3.796566,4.553792,3.100569,-9.846316,-8.732986,-2.512036,-5.327185,-5.814729,-7.885693,-5.591867,-8.943892,1.328695,-3.204236,0.119248,6.542935,-9.437989,-1.256455,4.324773,3.388329,-2.677342,0.155724,-6.878588,-0.350146,8.299052,-3.469472,-1.880792,-1.099957,-7.513232,-2.397134,3.905317,5.364495,5.964824,7.103329,-9.651044,-2.483361,3.953667,8.663594,-3.834773,-2.405943,2.162850,9.033974,-6.395290,0.802740,-5.375566,-7.606315,-7.665491,2.065166,7.633538,-8.976290,6.128526,4.954411], dtype = "float64")#candidate|9120|(2025,)|const|float64
call_9119 = relay.TupleGetItem(func_6520_call(relay.reshape(const_9120.astype('float64'), [9, 225])), 0)
call_9121 = relay.TupleGetItem(func_6522_call(relay.reshape(const_9120.astype('float64'), [9, 225])), 0)
output = relay.Tuple([call_9066,call_9111,const_9112,call_9119,const_9120,])
output2 = relay.Tuple([call_9067,call_9113,const_9112,call_9121,const_9120,])
func_9131 = relay.Function([], output)
mod['func_9131'] = func_9131
mod = relay.transform.InferType()(mod)
mutated_mod['func_9131'] = func_9131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9131_call = mutated_mod.get_global_var('func_9131')
call_9132 = func_9131_call()
output = call_9132
func_9133 = relay.Function([], output)
mutated_mod['func_9133'] = func_9133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5242_call = mod.get_global_var('func_5242')
func_5244_call = mutated_mod.get_global_var('func_5244')
call_9146 = relay.TupleGetItem(func_5242_call(), 1)
call_9147 = relay.TupleGetItem(func_5244_call(), 1)
func_2708_call = mod.get_global_var('func_2708')
func_2709_call = mutated_mod.get_global_var('func_2709')
call_9161 = func_2708_call()
call_9162 = func_2708_call()
func_1506_call = mod.get_global_var('func_1506')
func_1507_call = mutated_mod.get_global_var('func_1507')
call_9169 = relay.TupleGetItem(func_1506_call(), 7)
call_9170 = relay.TupleGetItem(func_1507_call(), 7)
output = relay.Tuple([call_9146,call_9161,call_9169,])
output2 = relay.Tuple([call_9147,call_9162,call_9170,])
func_9171 = relay.Function([], output)
mod['func_9171'] = func_9171
mod = relay.transform.InferType()(mod)
mutated_mod['func_9171'] = func_9171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9171_call = mutated_mod.get_global_var('func_9171')
call_9172 = func_9171_call()
output = call_9172
func_9173 = relay.Function([], output)
mutated_mod['func_9173'] = func_9173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7731_call = mod.get_global_var('func_7731')
func_7733_call = mutated_mod.get_global_var('func_7733')
call_9184 = relay.TupleGetItem(func_7731_call(), 0)
call_9185 = relay.TupleGetItem(func_7733_call(), 0)
output = relay.Tuple([call_9184,])
output2 = relay.Tuple([call_9185,])
func_9212 = relay.Function([], output)
mod['func_9212'] = func_9212
mod = relay.transform.InferType()(mod)
mutated_mod['func_9212'] = func_9212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9212_call = mutated_mod.get_global_var('func_9212')
call_9213 = func_9212_call()
output = call_9213
func_9214 = relay.Function([], output)
mutated_mod['func_9214'] = func_9214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1798_call = mod.get_global_var('func_1798')
func_1799_call = mutated_mod.get_global_var('func_1799')
call_9280 = relay.TupleGetItem(func_1798_call(), 0)
call_9281 = relay.TupleGetItem(func_1799_call(), 0)
output = call_9280
output2 = call_9281
func_9282 = relay.Function([], output)
mod['func_9282'] = func_9282
mod = relay.transform.InferType()(mod)
mutated_mod['func_9282'] = func_9282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9282_call = mutated_mod.get_global_var('func_9282')
call_9283 = func_9282_call()
output = call_9283
func_9284 = relay.Function([], output)
mutated_mod['func_9284'] = func_9284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6573_call = mod.get_global_var('func_6573')
func_6574_call = mutated_mod.get_global_var('func_6574')
call_9323 = relay.TupleGetItem(func_6573_call(), 0)
call_9324 = relay.TupleGetItem(func_6574_call(), 0)
output = relay.Tuple([call_9323,])
output2 = relay.Tuple([call_9324,])
func_9328 = relay.Function([], output)
mod['func_9328'] = func_9328
mod = relay.transform.InferType()(mod)
output = func_9328()
func_9329 = relay.Function([], output)
mutated_mod['func_9329'] = func_9329
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9451 = relay.var("var_9451", dtype = "int8", shape = (2, 10, 15))#candidate|9451|(2, 10, 15)|var|int8
const_9452 = relay.const([[[-10,-3,4,-1,2,3,2,-7,8,-10,4,1,-1,-7,-1],[-7,5,-10,-7,3,10,1,1,-3,-10,10,-8,-8,-4,-6],[-1,3,-2,-4,5,10,-3,-7,9,-3,-4,2,6,1,-6],[-2,-1,-2,-8,-3,8,-8,4,-7,-7,9,5,-3,3,10],[4,-6,-9,-7,-7,-1,2,5,-7,9,3,5,-1,-1,-6],[-4,7,5,-8,-4,-1,-9,-4,-10,-9,5,9,1,2,-4],[5,9,8,7,-4,-3,5,1,8,-8,-2,-10,5,-1,-5],[5,5,-3,8,10,-2,9,5,-7,-1,10,10,-4,-3,-1],[-2,-10,8,3,-3,8,-6,-3,8,3,-4,3,-5,6,4],[6,-4,4,-8,-8,9,-8,-6,7,-8,-3,3,4,-5,-6]],[[10,4,6,5,-6,-7,-2,2,-6,10,-9,-6,-1,2,3],[-4,8,8,-5,-2,-8,7,-3,-6,8,-3,-2,-9,1,8],[7,-8,9,3,-9,-6,3,6,2,7,1,7,10,6,-7],[-5,6,3,9,1,8,-6,-1,-7,6,5,5,-1,-7,-4],[1,1,3,3,8,2,1,9,10,-9,9,4,-5,8,-3],[-10,-4,-2,-5,-10,10,10,-10,5,4,-6,7,8,-6,8],[1,-6,9,3,-2,8,7,-3,-9,-6,-4,8,4,-7,-2],[-2,3,7,5,-5,-5,8,2,-8,2,4,6,-1,-7,3],[-3,4,2,-7,1,3,-6,-7,-4,9,-7,-6,-4,5,3],[-1,-2,2,8,10,-5,7,-4,2,-9,8,2,1,8,7]]], dtype = "int8")#candidate|9452|(2, 10, 15)|const|int8
bop_9453 = relay.right_shift(var_9451.astype('int8'), relay.reshape(const_9452.astype('int8'), relay.shape_of(var_9451))) # shape=(2, 10, 15)
output = bop_9453
output2 = bop_9453
func_9486 = relay.Function([var_9451,], output)
mod['func_9486'] = func_9486
mod = relay.transform.InferType()(mod)
var_9487 = relay.var("var_9487", dtype = "int8", shape = (2, 10, 15))#candidate|9487|(2, 10, 15)|var|int8
output = func_9486(var_9487)
func_9488 = relay.Function([var_9487], output)
mutated_mod['func_9488'] = func_9488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8018_call = mod.get_global_var('func_8018')
func_8019_call = mutated_mod.get_global_var('func_8019')
call_9528 = relay.TupleGetItem(func_8018_call(), 0)
call_9529 = relay.TupleGetItem(func_8019_call(), 0)
func_4600_call = mod.get_global_var('func_4600')
func_4602_call = mutated_mod.get_global_var('func_4602')
call_9532 = relay.TupleGetItem(func_4600_call(), 1)
call_9533 = relay.TupleGetItem(func_4602_call(), 1)
output = relay.Tuple([call_9528,call_9532,])
output2 = relay.Tuple([call_9529,call_9533,])
func_9538 = relay.Function([], output)
mod['func_9538'] = func_9538
mod = relay.transform.InferType()(mod)
output = func_9538()
func_9539 = relay.Function([], output)
mutated_mod['func_9539'] = func_9539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8348_call = mod.get_global_var('func_8348')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_9643 = func_8348_call()
call_9644 = func_8348_call()
func_7827_call = mod.get_global_var('func_7827')
func_7828_call = mutated_mod.get_global_var('func_7828')
call_9651 = func_7827_call()
call_9652 = func_7827_call()
func_7954_call = mod.get_global_var('func_7954')
func_7957_call = mutated_mod.get_global_var('func_7957')
var_9658 = relay.var("var_9658", dtype = "float32", shape = (105, 3))#candidate|9658|(105, 3)|var|float32
call_9657 = relay.TupleGetItem(func_7954_call(relay.reshape(var_9658.astype('float32'), [1, 315])), 7)
call_9659 = relay.TupleGetItem(func_7957_call(relay.reshape(var_9658.astype('float32'), [1, 315])), 7)
uop_9666 = relay.acos(call_9657.astype('float64')) # shape=(135, 15)
uop_9668 = relay.acos(call_9659.astype('float64')) # shape=(135, 15)
func_5972_call = mod.get_global_var('func_5972')
func_5974_call = mutated_mod.get_global_var('func_5974')
call_9672 = func_5972_call()
call_9673 = func_5972_call()
output = relay.Tuple([call_9643,call_9651,var_9658,uop_9666,call_9672,])
output2 = relay.Tuple([call_9644,call_9652,var_9658,uop_9668,call_9673,])
func_9682 = relay.Function([var_9658,], output)
mod['func_9682'] = func_9682
mod = relay.transform.InferType()(mod)
var_9683 = relay.var("var_9683", dtype = "float32", shape = (105, 3))#candidate|9683|(105, 3)|var|float32
output = func_9682(var_9683)
func_9684 = relay.Function([var_9683], output)
mutated_mod['func_9684'] = func_9684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mod.get_global_var('func_3755')
func_3757_call = mutated_mod.get_global_var('func_3757')
call_9704 = relay.TupleGetItem(func_3755_call(), 0)
call_9705 = relay.TupleGetItem(func_3757_call(), 0)
func_5740_call = mod.get_global_var('func_5740')
func_5743_call = mutated_mod.get_global_var('func_5743')
var_9719 = relay.var("var_9719", dtype = "float32", shape = (256,))#candidate|9719|(256,)|var|float32
call_9718 = relay.TupleGetItem(func_5740_call(relay.reshape(var_9719.astype('float32'), [256,])), 1)
call_9720 = relay.TupleGetItem(func_5743_call(relay.reshape(var_9719.astype('float32'), [256,])), 1)
func_5792_call = mod.get_global_var('func_5792')
func_5794_call = mutated_mod.get_global_var('func_5794')
call_9741 = func_5792_call()
call_9742 = func_5792_call()
output = relay.Tuple([call_9704,call_9718,var_9719,call_9741,])
output2 = relay.Tuple([call_9705,call_9720,var_9719,call_9742,])
func_9746 = relay.Function([var_9719,], output)
mod['func_9746'] = func_9746
mod = relay.transform.InferType()(mod)
mutated_mod['func_9746'] = func_9746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9747 = relay.var("var_9747", dtype = "float32", shape = (256,))#candidate|9747|(256,)|var|float32
func_9746_call = mutated_mod.get_global_var('func_9746')
call_9748 = func_9746_call(var_9747)
output = call_9748
func_9749 = relay.Function([var_9747], output)
mutated_mod['func_9749'] = func_9749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5933_call = mod.get_global_var('func_5933')
func_5935_call = mutated_mod.get_global_var('func_5935')
call_9769 = func_5933_call()
call_9770 = func_5933_call()
func_4247_call = mod.get_global_var('func_4247')
func_4252_call = mutated_mod.get_global_var('func_4252')
const_9774 = relay.const(8.547603, dtype = "float64")#candidate|9774|()|const|float64
var_9775 = relay.var("var_9775", dtype = "float64", shape = (12,))#candidate|9775|(12,)|var|float64
const_9776 = relay.const([-6.143135,4.264927,-2.916429,0.615257,-5.615386,-3.172199,1.984342,-2.379390,7.853687,-9.655515,8.482199,-9.965959,8.730325,2.616140,-7.187449,-9.929390,-3.200188,-0.368647,-2.507092,2.831891,-0.892199,1.142733,9.548691,-4.084476,4.984738,7.778505,-7.257271,-4.423294,2.063324,0.662356,7.833078,-5.688043,3.938422,-0.567293,9.153928,-7.959355,-2.766688,4.082626,4.766061,-7.744169,-9.249509,5.167831,7.486814,-8.353729,-6.984003,-3.224012,-2.417186,2.234297], dtype = "float64")#candidate|9776|(48,)|const|float64
call_9773 = relay.TupleGetItem(func_4247_call(relay.reshape(const_9774.astype('float64'), []), relay.reshape(var_9775.astype('float64'), [1, 2, 6]), relay.reshape(const_9776.astype('float64'), [4, 2, 6]), ), 1)
call_9777 = relay.TupleGetItem(func_4252_call(relay.reshape(const_9774.astype('float64'), []), relay.reshape(var_9775.astype('float64'), [1, 2, 6]), relay.reshape(const_9776.astype('float64'), [4, 2, 6]), ), 1)
output = relay.Tuple([call_9769,call_9773,const_9774,var_9775,const_9776,])
output2 = relay.Tuple([call_9770,call_9777,const_9774,var_9775,const_9776,])
func_9782 = relay.Function([var_9775,], output)
mod['func_9782'] = func_9782
mod = relay.transform.InferType()(mod)
mutated_mod['func_9782'] = func_9782
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9783 = relay.var("var_9783", dtype = "float64", shape = (12,))#candidate|9783|(12,)|var|float64
func_9782_call = mutated_mod.get_global_var('func_9782')
call_9784 = func_9782_call(var_9783)
output = call_9784
func_9785 = relay.Function([var_9783], output)
mutated_mod['func_9785'] = func_9785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9328_call = mod.get_global_var('func_9328')
func_9329_call = mutated_mod.get_global_var('func_9329')
call_9790 = relay.TupleGetItem(func_9328_call(), 0)
call_9791 = relay.TupleGetItem(func_9329_call(), 0)
func_3986_call = mod.get_global_var('func_3986')
func_3988_call = mutated_mod.get_global_var('func_3988')
call_9794 = func_3986_call()
call_9795 = func_3986_call()
output = relay.Tuple([call_9790,call_9794,])
output2 = relay.Tuple([call_9791,call_9795,])
func_9806 = relay.Function([], output)
mod['func_9806'] = func_9806
mod = relay.transform.InferType()(mod)
output = func_9806()
func_9807 = relay.Function([], output)
mutated_mod['func_9807'] = func_9807
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9910 = relay.const([[[4.136548,2.173563,-5.473316,-9.391217,1.654320,-6.680168],[1.194317,9.234405,4.941958,-7.824506,7.578745,0.770146],[-2.674147,-9.639892,0.643090,-3.474772,-5.164822,0.129848]],[[3.106715,-3.456208,1.577166,4.994749,-7.021455,-1.621230],[-2.925716,3.220449,0.935653,-6.787394,1.096121,-6.065414],[-9.598748,-9.862823,0.695081,7.823261,2.845439,3.094317]],[[-9.948883,5.485762,3.666011,9.287375,-4.686590,-6.520189],[0.636620,-9.748994,3.327376,-4.594116,3.933917,-2.169351],[-2.483100,1.303767,1.622844,-4.168387,-6.299788,-7.914150]],[[-6.945851,4.260574,-1.738199,-3.873404,-1.789541,-2.821409],[-5.356159,-6.330171,3.680715,-7.614900,-1.100369,0.244752],[-2.842949,-9.376037,1.507775,-0.895137,-8.443087,3.024969]],[[3.682080,-9.102744,-9.917257,8.549165,9.656136,-0.380904],[-7.085232,8.735630,-0.204719,-7.870150,-4.948503,0.746614],[5.114839,9.822674,-5.926343,-7.424765,0.113684,3.402204]],[[-2.125927,-1.717935,-2.473931,-7.439298,7.671927,-8.377968],[4.556805,-0.901704,1.020245,4.929431,4.398982,-2.777954],[4.210019,-7.175428,3.188410,-3.125606,-4.714413,-6.933105]],[[5.488791,-7.958869,-1.131394,8.199338,6.936611,5.392407],[6.477737,-4.065014,-1.412258,-2.688073,4.481312,-0.345411],[9.751399,-4.509525,9.393650,-7.055376,-2.014321,9.516673]],[[0.724262,-1.014295,-1.953456,3.432567,-8.163585,-8.392729],[-1.131917,0.677764,6.563558,7.476064,-2.267514,7.548986],[-3.759583,7.900486,-9.188924,7.276040,8.488480,-4.128162]],[[9.626086,4.916191,9.227846,-9.746094,9.150101,-4.611481],[0.992659,4.800827,8.978856,0.029002,-9.471040,-1.631810],[2.896696,8.787350,2.560565,-2.560538,2.332874,8.902751]],[[-6.294292,7.023484,5.601326,-4.082702,6.733090,-0.581525],[-5.144181,-3.977858,-4.007525,3.394298,-8.459386,-8.181434],[3.007039,-2.321358,6.046855,7.750088,-5.661654,9.878184]],[[-2.769557,-8.517477,8.171087,3.170446,4.862887,-1.338031],[-4.199820,0.245199,-7.992374,7.421079,2.635097,2.282065],[4.191667,-0.094674,2.693955,3.620811,4.200060,5.408544]],[[-1.662873,9.600324,-4.805965,-5.062381,2.426721,9.919201],[8.579978,8.552623,-2.326767,0.881567,-7.320709,6.349919],[7.081751,6.964800,0.597248,0.176880,7.256189,4.319415]]], dtype = "float32")#candidate|9910|(12, 3, 6)|const|float32
uop_9911 = relay.rsqrt(const_9910.astype('float32')) # shape=(12, 3, 6)
func_8865_call = mod.get_global_var('func_8865')
func_8868_call = mutated_mod.get_global_var('func_8868')
const_9918 = relay.const([3.507515,1.268321,-3.982307,9.796897,4.010640,-6.316526,-3.187689,8.584223,-9.203376,-2.024188,-9.245916,-6.322885,-2.452377,-3.005259,-6.223881,-8.416083,6.616980,1.516497,-1.701043,-4.062409,-5.021192,-5.805938,-1.311393,5.556274,8.019888,-3.622421,-7.203234,8.205210,1.003977,-5.739401,-7.094139,1.396003,5.451900,1.336804,-0.749561,7.349573,-2.788345,2.988408,5.508163,2.095241,-5.286674,5.007250,-3.585420,1.076837,-1.107687,2.176640,-0.361472,-5.884265,8.314690,7.597961,6.860090,-4.771059,9.389175,9.731924,-1.933278,1.862799,-2.205029,-3.588344,-5.424629,-7.245148,3.193822,6.850770,0.996481,5.231646,1.555313,-6.847811,-4.458974,-4.303277,-1.209274,-3.783277,-4.810289,4.814352,-0.480213,0.123884,-9.052413,6.546688,4.170250,8.713703,8.928357,3.952005,-8.257022,5.965852,8.790462,-6.572231,6.661561,-2.363177,-7.943643,2.754840,4.404492,7.080466,-5.345205,-2.262316,0.501529,-2.861393,-7.969642,3.941183,2.535873,0.255383,-9.554650,-0.732181,9.430095,1.908576,4.597359,-4.767809,4.695706,-1.907233,4.011343,7.199941,-3.671682,3.814004,-2.732921,3.796502,6.345476,-7.944062,-0.266269,-1.552486,3.680725,-8.154530,-2.059185,-7.254422,-8.542600,1.396023,9.657284,3.777518,7.509022,-5.905638,0.907079,2.294029,5.742909,3.589090,4.754981,1.196464,2.080563,1.611447,-9.604069,-5.920354,-8.789785,-2.235389,-2.387837,1.921547,-9.879119,8.107098,-4.424071,7.589726,-9.581821,4.542538,-8.445104,4.181640,-0.296889,2.530476,-5.115721,-9.220069,7.832617,-0.436987,-2.812759,6.868280,9.958638,-5.523119,-6.151306,8.218761,-5.450591,-0.766221,0.495345,1.149600,-5.400149,3.217167,-2.245906,4.437011,-2.623568,6.055803,8.161974,-8.800285,-1.817420,-4.072614,-8.043994,3.970599,0.128954,1.364033,1.133562,-8.324879,0.518343,-8.406319,7.580161,4.105072,2.829105,-7.423843,-2.437802,-5.690113,-5.343893,7.703340,-2.274680,5.549528,-8.693969,5.233209,2.816949,1.206379,2.074060,-4.490819,8.241650,-1.604929,9.894033,3.647789,9.857034,-9.982016,5.678093,-2.413956,-0.610313,5.468819,-9.552518,8.808249,-6.447161,-4.403388,-8.005740,6.004181,3.190492,8.968569,-5.113922,-8.953294,-1.447466,6.579850,-4.666666,9.336655,-6.019278,0.913324,6.739549,-2.303297,1.384120,3.493354,-8.790314,7.054778,5.227007,-9.740926,5.531373,2.120652,6.260753,0.303637,8.646637,-1.244564,5.500689,-3.588149,-4.442015,8.739860,-7.839029,-9.926490,8.108136,-0.188459,-2.864065,-7.775258,5.091941,6.747429,2.655193,-6.487975,4.181012,-0.427348,-2.531646,-0.152601,2.363135,-1.926984,-8.007282,-8.117051,-6.449596,-0.126369,3.931736,-0.670935,5.475326,6.279305,8.404257,3.817210,6.925152,6.674664,-5.749717,-0.877030,5.229027,6.203324,0.843727,6.806671,-9.895521,-4.858675,2.865611,-8.036823,-6.380466,1.398989,2.387627,1.943953,-5.527933,-6.607085,-1.935523,-1.969637,1.385028,6.416226,-3.167602,-1.273742,2.052841,-5.030456,-1.501369,3.017976,5.703834,-3.269322,4.121744,2.784972,-4.734157,-1.891963,-3.084511,0.500375,7.387628,8.282002,6.900191,-3.213145,-6.687787,1.110561,-2.324084,-8.626955,1.036983,-2.411954,-1.564092,-7.263909,-1.703513,9.383917,-8.716409,-4.801282,5.118236,3.213353,-1.698285,4.628613,-1.304207,7.357778,1.307746,-0.841729,-4.395754,6.974594,-1.742324,3.801173,5.125594,-3.103037,0.038380,0.274972,-8.048512,-6.056681,-1.763987,9.580627,-6.654916,8.138518,-2.652686,0.359074,4.238029,0.497303,-6.645596,-7.823063,3.381245,1.162574,0.132849,-3.371093,0.266986,-0.004109,-5.744694,0.883184,-0.020534,6.300248,-7.905184,9.425606,6.890659,-9.540793,-1.748422,2.092810,2.258147,-9.653905,7.229072,-2.065668,5.705062,4.416937,-7.218993,0.465063,0.883861,-1.222848,5.793455,7.193200,-6.182297,-1.788124,-8.912855,5.717454,5.426865,7.491283,-4.548636,9.435262,-6.745556,6.334969,9.150916,-9.883447,9.399003,3.290837,-3.290332,-1.663849,-8.753202,5.462690,-6.404437,-3.522677,6.664182,6.686998,9.786965,2.821702,8.466418,-9.818422,8.008558,7.867340,6.757390,1.030280,-5.545829,1.681930,9.066087,9.517014,2.943183,1.799165,4.478498,-8.712480,6.943501,2.583451,-2.904522,-8.325570,-9.933193,5.636502,-5.277829,4.063156,-6.023519,8.850039,-9.140698,4.714241,-7.456464,-7.746147,9.456603,-5.220543,-9.992305,4.698514,9.737393,1.090478,-8.218221,-3.064603,6.562436,7.611377,-1.034257,6.625742,4.106230,-6.130625,9.051692,-4.847882,9.495551,-4.240432,-7.135071,-2.020142,9.767863,8.878576,-6.208281,-6.241675,5.847000,4.339914,-6.076341,-5.207299,-6.838584,7.627211,4.945792,-2.509100,-8.788152,0.192549,5.117330,-7.601611,2.846758,-5.062816,0.351340,4.353325,-5.783333,-2.215501,-4.280284,-0.506476,9.240529,-5.246017,6.708334,0.869670,8.722368,-9.061784,2.400108,8.649610,-3.241803,-8.925175,-2.167779,1.289365,3.128780,9.234178,-1.856803,-5.975903,1.506062,8.685396,9.107057,-7.449655,1.679832,6.041681,-8.462358,6.908073,-6.884969,-8.697860,3.380191,3.637426,-1.974096,-1.558388,9.898564,-9.115189,-0.485938,2.814390,8.574697,-3.766567,8.927748,3.962776,4.767913,-1.166567,-3.900304,-8.503716,-4.732806,-4.311910,4.410596,-2.863984,0.710911,9.484164,-2.086037,-8.622973,2.474711,-3.581966,-1.863496,-6.584425,-6.808734,-2.419030,2.662087,-7.428754,-9.328357,-6.172485,-3.357394,-6.716809,-8.473227,1.763238,6.196818,-1.187776,-1.392659,4.192237,-0.890513,-8.112916,-3.726188,3.101607,-1.339631,-5.893157,8.996380,-8.701402,4.987060,3.960333,-9.760850,-8.638608,-0.667594,-4.031126,5.247964,-3.157884,1.282342,-1.154990,9.070258,-6.208015,5.277531,-0.670634,7.372218,-4.426218,-3.133292,-3.241527,-2.876881,-8.605995,6.105472,-4.170524,-9.099123,-0.704305,6.077935,9.343501,5.006730,-9.590391,-5.086459,7.492091,2.442103,-7.188128,4.356040,1.447288,7.459094,7.249306,-2.079979,7.125931,-2.168618,5.280115,-7.702857,-9.144591,-3.635426,6.130906,9.841619,-9.933847,-9.989679,-3.681509,-1.759924,-9.371922,0.784096,-2.224372,4.614355,-3.225024,-2.550994,5.409216,0.653909,-3.786023,4.263692,-5.764985,-0.180260,8.338292,-9.051235,-2.833160,1.386310,-1.792416,-3.533644,7.091123,9.587288,8.628468,0.364650,-3.140599,-8.745951,-5.725659,-9.841835,4.399189,1.811194,-1.427283,-6.721556,-4.476832,9.823108,1.326383,-7.590229,3.108247,-8.791717,2.002591,4.737716,-0.041540,-1.220258,0.230045,-2.701889,4.194428,-4.632057,9.981889,-9.792669,-7.668690,-8.864150,-0.111713,-2.637690,-0.391095,-7.189799,-7.377450,-3.547427,-9.295986,1.909352,7.354394,-5.951396,-3.622207,-0.163213,7.386829,2.486508,-2.318940,3.945833,-6.109310,-9.074578,7.376722,-9.142809,9.746430,-6.996557,0.876455,7.376546,5.181241,8.030553,-9.623303,9.751047,0.024026,-3.798983,6.720005,-7.567141,7.549255,-3.773944,5.171426,7.541784,1.770813,-8.008422,0.131595,-7.203256,2.715210,-3.619649,0.447572,-8.310965,8.110297,9.492524,-7.127390,-2.758969,-6.740227,-8.764135,-9.701435,-4.808893,-4.105002,-8.118833,4.484408,-0.587328,1.488759,-4.665661,3.681166,7.324781,9.286504,2.696831,-1.280102,-2.543448,-1.539320,-1.524821,-5.488511,6.667975,-3.431369,-2.181037,-0.112661,-9.349783,-0.896016,-6.408487,3.204524,-7.187929,-5.896059,6.967922,5.520663,-2.467361,-1.134643,-5.514746,8.851959,9.300148,-8.910529,9.934920,5.529020,-2.590240,9.492167,1.794600,-7.321698,9.104150,7.025499,5.929458,-4.578841,-3.701459,-2.454846,0.898775,-1.234612,5.422880,5.775063,4.440669,6.848223,-7.161656,0.846725,1.611658,0.028059,-3.310964,9.021204,6.520063,5.494161,4.410750,7.211500,-8.175431,2.582671,-6.357411,-0.294928,8.906655,1.730589,-7.704208,9.850255,-4.293761,3.307512,3.650015,-4.292863,-7.973357,2.447768,1.149302,5.881789,-5.734274,-1.062863,2.951339,9.578963,-1.744356,-6.395153,1.706124,-6.732247,-5.571025,-0.508132,5.211021,-2.149728,9.505839,5.684614,-0.064737,-1.561996,7.768678,2.807247,9.435656,-3.718683,5.659690,6.343760,-4.722348,-9.974528,7.772794,6.951751,2.971244,-1.757465,6.728249,-2.082673,-8.054893,-9.686954,9.006482,-7.260113,-4.732499,-9.143903,4.490976,-5.717371,3.875530,-8.718920,-2.098225,1.559788,-3.146538,-5.480283,7.598928,8.588117,4.742788,-0.923094,-5.369593,9.945612,9.351100,-5.281277,3.307585,-8.005201,-0.407961,3.442007,-7.746678,-7.113238,2.590877,-2.768299,6.652185,-6.524918,-3.480963,7.913376,-3.851766,5.203436,-0.776237,-4.541195,2.775864,1.863874,-6.271871,-5.734854,5.768331,7.267910,3.038388,-2.281143,7.588604,0.976433,9.854129,-4.969010,3.612851,8.580336,-8.471492,-1.974566,-9.313176,9.152202,-1.881436,-7.678515,-0.509369,-7.693388,5.243750,7.934945,-3.016330,-2.013287,2.257754,6.523446,3.376232,2.259719,-7.240013,1.741718,5.758882,1.517238,-4.951109,9.907247,0.965990,-4.575421,-0.364039,-6.643260,-2.550809,-3.158607,2.892666,-7.734868,-8.433579,-7.533929,0.734977,-7.288900,-8.514205,1.258229,0.266295,-3.835480,-4.744454,7.331911,-1.129827,3.329739,4.053800,-9.254821,5.030522,1.394611,-5.409336,3.604889,6.276460,-5.318633,5.574584,-0.696987,2.100113,-7.757794,1.364955,-4.175946,2.840065,-6.300959,-4.795744,4.120772,0.280950,6.276961,2.078215,-7.081052,-8.721172,-5.518224,-7.235676,-4.793754,5.081766,6.570550,4.926417,-1.649102,-8.018735,1.073332,-7.234507,-0.530328,5.312615,4.246741,-5.742265,9.451320,9.999491,7.461889,-7.065707,0.029739,-0.772392,-9.278162,-2.369781,-3.358875,2.994380,1.546222,-9.829074,0.555203,-9.073832,-0.643339,-2.727720,8.297366,-8.083254,4.563818,7.182353,-7.927866,-3.157507,4.251780,-3.140956,8.435960,6.467870,6.219579,-0.258821,6.618861,5.489229,-9.401793,8.520487,8.287387,-9.398395,-9.931370,0.460213,1.485569,0.542078,3.199909,-5.228838,8.617407,7.928286,5.634544,2.577740,-0.657029,0.904591,6.247363,9.042566,-3.255504,4.195582,2.366226,2.040876,-0.857951,7.246084,-8.424737,-8.263676,6.116864,-0.346257,-8.304895,0.012153,5.418437,3.814452,9.560635,1.481754,-2.175737,-0.208647,-4.035424,-0.166609,-6.601934,-5.628327,7.333843,-1.478382,-7.874307,2.080909,-3.986174,-2.538188,5.395361,-5.516852,-4.953659,-1.889907,8.278416,-0.359495,3.944407,-5.505648,-1.009456,-8.807196,-8.719671,-7.517763,-6.004881,5.853928,-2.376830,-4.331766,9.795355,-9.084998,-1.475136,-7.207942,7.836791,4.787612,7.061098,-4.494814,-4.524623,1.228582,1.349284,-7.208146,8.593724,-2.919628,9.443190,-1.253149,-0.879470,-1.689433,4.615509,-1.671768,4.223878,7.342249,8.500384,-9.365307,6.691235,-4.195857,5.237001,-1.273515,-1.843664,-2.286508,9.894284,-0.936747,5.791748,-6.679005,6.601603,8.141578,4.353154,8.565662,-5.967362,-2.977262,8.959261,-3.242380,3.605325,-8.564081,2.748517,4.996380,0.700944,-3.402462,-5.385833,4.136257,3.327424,-8.165290,-3.939980,-0.963237,5.418842,-4.298870,2.205831,6.037149,0.953069,2.628985,-6.611608,0.835348,-6.157418,-6.972762,-4.193685,7.053006,-8.463735,-9.214403,2.948845,6.071893,-5.953718,-1.762553,-4.136095,-2.836941,7.424386,3.628643,5.316321,2.076257,-4.200603,-5.256903,2.877529,0.776715,-2.466078,-3.180998,-2.947787,-2.815553,1.709845,-3.265181,4.605851,6.019566,-2.539286,-8.247132,8.030548,-7.535385,-5.691567,7.899332,-1.636413,9.859381,-9.260636,-9.809171,-7.266196,5.615763,9.396304,9.936608,8.745033,1.173776,1.644132,4.692159,2.756022,8.013242,-0.498575,-9.859842,8.794599,1.706629,3.680458,-2.029037,4.496225,-5.181639,9.764848,5.855803,-5.715096,7.051708,-7.687242,9.005168,-3.881485,8.127376,8.662600,9.384197,-1.283153,-1.596761,-4.672173,8.823136,5.177845,6.800532,0.766072,6.551583,5.595038,-0.974313,7.961681,-7.145849,-6.808387,-0.348126,2.274680,-0.895209,7.474208,4.547195,3.923769,7.427109,-1.707837,7.293185,4.184664,-0.509399,9.006694,-7.035554,-1.092639,-4.010622,7.041508,-4.798118,-5.549007,-1.794409,5.275502,-6.666051,-8.450748,1.397689,-7.123269,-0.993944,1.481193,-6.881752,7.321020,6.217612,3.224433,-4.570572,2.741721,6.432169,6.289163,7.092397,-4.290869,5.400799,2.702605,0.094462,-7.184866,8.253655,-2.121272,-8.158449,-7.941233,4.324427,-4.671882,-3.245163,-2.171235,3.083319,8.748703,2.578766,-8.525793,-3.309362,2.283764,4.028895,-3.218562,-6.776976,3.868228,-2.631720,-8.646182,4.637322,-7.110133,-5.925939,-7.033623,-6.830750,-5.662217,2.287867,8.409067,-7.336619,4.138040,-9.953392,-9.375096,3.350545,4.469944,-9.631373,9.754491,-3.378250,7.096265,9.264131,5.751747,-9.387775,4.120889,-9.524035,3.313976,1.433285,7.146861,-3.237655,-3.278742,9.405096,-3.706421,-3.826161,2.017327,7.496643,4.710911,-7.694473,-6.438755,3.580103,-0.166365,-6.064109,-9.613573,2.966214,9.474792,-2.137209,6.264767,-2.049281,3.897802,1.740343,4.503564,0.393491,8.914381,1.562059,-0.779005,8.349580,8.574334,9.535736,-2.573905,2.239993,-2.630619,3.628286,5.565550,0.032555,-0.137320,1.491031,0.278786,7.670215,2.864017,4.325223,9.721641,-9.827680,-8.521261,-5.672627,-0.517641,6.393601,7.954749,-8.801475,-7.010320,3.786128,6.105580,-8.121596,-0.674740,5.182981,6.153380,0.550710,-1.454473,0.232248,7.665215,8.068534,7.196944,7.346838,0.892224,8.756960,2.508399,2.919247,1.525091,-2.746001,1.569814,0.125880,-9.267490,5.889211,1.873532,2.890380,-0.057396,-6.551886,5.329804,8.957439,-0.405099,-0.035565,5.027893,-1.211551,-5.382631,-0.586561,-0.169204,-5.996313,0.167825,5.367318,-8.662542,2.594847,0.700055,-3.082909,3.696732,-5.714722,-4.359722,-8.436812,-2.103564,-5.599390,4.095739,-4.394106,0.251739,-5.647009,-5.524684,7.764232,-2.770412,5.809547,-4.437920,4.560036,6.800525,9.712492,-6.553996,-2.512891,-1.898407,0.511625,2.064618,-3.642676,-3.446624,0.584867,-0.099131,9.518701,-8.878593,4.223991,-2.991273,-2.886954,-2.523427,1.473243,2.141209,3.487702,6.786911,2.052072,-6.706922,8.787388,-1.427271,4.843833,9.154195,-3.145608,3.994163,-0.620476,-4.744760,-8.199464,2.007772,4.541627,9.890871,-3.978770,-1.996191,0.647006,6.305394,8.537803,-8.164933,9.473739,-9.285521,3.979883,9.493205,5.408779,-9.690072,-3.231212,-0.999011,7.804351,-7.357713,-9.395935,8.981175,2.600837,-8.557231,8.041543,6.580022,-8.287394,-1.473432,5.936566,7.912838,6.910638,-4.991891,8.398345,6.626322,-8.039406,1.312687,-0.774641,0.743627,3.547075,8.288063,-7.359413,6.672183,-9.799461,-0.774858,7.515122,-8.435553,7.026364,-9.701153,8.887346,7.864358,9.355995,-8.512471,-4.837266,9.936846,2.831527,-4.522337,7.675395,-0.756521,8.816474,-7.277382,5.773164,4.618139,7.785652,4.431450,5.109417,4.850632,2.200585,1.454286,2.637235,-1.985575,6.924715,-8.363496,-2.999061,-3.915452,2.803758,0.170078,8.799747,1.482359,-8.803316,-3.692969,-3.729674,1.897913,4.162118,1.496884,3.510993,-2.763278,-7.567573,-1.519291,0.245758,-9.074578,2.599020,4.244852,-7.863798,3.192101,-1.906681,-3.079460,0.063375,-0.872832,-4.253690,4.188310,9.667211,-2.549990,-8.123074,3.597865,5.746929,-7.727048,3.626496,-7.245986,6.973957,-9.938398,0.001584,-8.516791,-4.850261,6.839915,-1.269450,0.353629,-9.112898,3.649063,-4.025875,0.941390,-8.367592,-2.417730,0.917961,7.842290,-4.178894,-5.893055,-6.755644,1.729951,-9.969260,-4.226515,0.800622,-2.986631,8.764805,4.131827,-4.518500,-1.144584,-5.029328,-8.622812,0.673110,-4.895059,-3.335182,7.748621,0.672046,7.417394,4.594225,-2.909947,6.681190,1.397950,-2.321764,-7.717674,7.570294,7.309648,6.780706,8.362275,4.996438,2.295266,5.357631,0.341671,6.727276,-3.291048,-6.313683,9.950915,3.220690,-9.764403,5.330660,2.147149,1.806339,9.173133,-0.982685,2.179908,-4.654572,5.766019,3.906661,7.260721,-4.580189,-8.036911,-2.919567,-1.944896,-7.690666,-2.360042,-7.936585,-5.568359,-3.642048,-4.961492,-0.950473,8.929326,-4.262147,-9.518951,0.852967,-3.150550,7.799723,-9.866518,9.998237,-4.330295,0.990187,5.185175,-2.019446,-7.142044,1.073209,3.882141,-2.505675,7.684022,-0.751472,7.628448,1.895521,6.581047,-9.743521,-4.149966,-8.394777,3.679486,4.562727,7.237005,-8.205370,8.142960,2.644989,2.701753,9.973849,-8.399461,9.626116,9.287308,-3.932057,3.351950,-7.887356,-1.845050,-5.518169,-3.240153,-4.616230,6.317834,2.699615,2.999364,-0.304763,9.796318,9.344182,1.143906,7.284304,2.824771,2.294654,-5.049153,-2.897447,-4.130435,-7.476916,7.970718,0.185687,4.657517,6.282493,1.209074,9.302158,6.760052,-3.592082,6.522526,8.484248,2.213165,-5.908035,-3.565572,-0.190006,4.204861,6.337528,-5.391916,-5.195545,-6.847496,-7.827463,8.332499,-0.524122,-0.493911,7.799527,-1.744925,-4.715116,6.559801,2.960656,8.376462,-9.421887,-5.572338,9.464149,-4.771303,-3.450643,2.811818,-9.058639,-6.156939,9.552150,-8.875054,6.025009,1.612009,-5.401824,-5.592444,-0.589059,-0.835170,-9.445047,0.125147,2.505500,2.609171,-8.825564,-2.575092,8.168889,3.081540,9.403164,0.292724,-7.104739,-2.489302,6.802876,-4.172187,-4.778154,5.411667,0.015212,2.872099,-4.551473,-6.997870,2.325350,-1.578906,9.500712,-8.826236,9.608897,1.185004,-2.190253,-2.845719,-1.421339,-8.371867,8.492457,-1.979236,-7.124307,0.795687,-4.763282,7.913230,-8.996388,7.303882,9.807800,-7.424511,0.897949,-6.279186,4.860471,-6.340384,1.343154,3.593936,-2.401570,8.899338,8.943685,9.331832,-2.459861,6.306004,-5.259269,-1.813259,-2.723606,-6.362021,4.106729,-5.772956,-6.681379,-1.862784,0.239760,-8.825083,0.423118,-3.741142,9.148578,5.330548,-3.851772,-4.366589,0.929182,-0.374106,-4.556102,1.259943,2.272348,-9.628333,-7.953477,3.822985,-1.960683,8.345515,1.864100,-8.971733,-0.969795,-3.154594,0.654590,2.664474,4.838569,-4.572995,6.893998,6.582300,1.462773,-3.340334,0.758345,0.313208,3.038563,7.796530,-1.486438,9.816063,9.304200,1.980040,1.838761,4.389524,-0.557124,-7.895501,-4.797411,-2.433306,1.808293,4.296586,-2.146693,2.475123,-8.251458,-2.136992,-2.597524,4.180031,0.841489,-7.216862,5.601959,-3.812311,-8.518476,4.778596,-1.819611,-0.339513,-2.892490,-8.243279,9.686470,5.835455,1.055410,-5.475019,1.523945,9.223960,9.627544,3.635943,-2.739173,-2.302811,-2.340072,5.841966,-6.863920,1.399712,9.969284,6.165396,0.749847,-6.345710,2.539412,-8.543281,-5.682356,8.399430,-0.879439,5.402407,-2.122781,7.571275,8.625377,-2.945650,-4.107520,7.013163,8.722808,-6.250497,6.863811,1.631730,-2.468304,5.604686,-1.951492,-3.250044,-1.987307,4.716241,0.172303,0.626748,9.951619,-1.539110,0.919187,4.710703,7.140086,4.977814,1.579444,9.945005,8.297100,-4.976011,7.101991,-3.798461,-8.731682,4.305361,-8.315566,0.224717,-9.686381,5.140222,1.811477,-1.160493,9.802831,1.592920,0.650417,-2.579656,2.565191,-9.205330,2.962815,-0.258086,-7.375540,1.075473,1.687737,-0.176137,0.740956,4.284258,-7.890333,2.319999,-3.419187,-0.820551,9.017790,-1.038015,-1.677947,9.410964,1.675060,2.889922,9.993334,-6.796103,1.766289,-9.085122,-6.442718,5.462712,-9.800139,-1.884811,4.323730,-4.041921,2.727614,-8.156254,2.945549,9.861979,1.870609,-7.289558,-1.121670,9.657107,9.994706,-3.742105,-8.315094,-1.165412,-2.421998,1.197197,-5.521128,-0.534309,-5.241657,6.257109,-5.017303,-2.563864,6.252307,5.245522,6.845121,-9.806339,-1.928986,-8.829166,-8.693571,2.833255,-7.253137,4.095079,-2.152733,-2.542629,-4.129538,-9.271867,8.626081,-4.597492,2.267444,-6.372927,0.698626,8.713835,1.762857,-6.274961,9.060625,-0.620085,-2.333552,-4.843734,8.895324,5.220093,-4.926706,-9.192022,-9.797499,-7.722712,-3.246478,-2.460256,4.525524,-8.537002,5.585527,3.453645,-7.176553,-6.121434,2.239924,-3.516568,-0.632083,-6.005414,9.982625,-6.086715,6.571046,-4.824747,6.847629,3.461329,-3.555223,4.037225,-8.109715,-0.299247,-0.793241,4.923180,7.552253,-0.368706,3.448194,-6.596032,7.133022,-3.141008,-5.279156,5.064845,0.369571,-7.298172,-5.855927,-7.026769,-2.440102,1.844976,9.091562,-8.508388,-9.437921,-6.281442,2.954595,5.542234,8.919345,-4.169321,-5.623532,9.785822,-8.390218,0.545160,4.156386,-1.316595,3.067125,-0.806821,-0.732604,8.667731,7.741083,5.878956,4.820948,-5.130768,-9.771716,-3.696481,-7.960865,3.055220,3.721471,6.038722,-0.804301,5.275193,9.909932,-2.028620,-8.132947,7.451691,-7.429775,3.167077,5.178860], dtype = "float64")#candidate|9918|(2025,)|const|float64
call_9917 = relay.TupleGetItem(func_8865_call(relay.reshape(const_9918.astype('float64'), [9, 225])), 1)
call_9919 = relay.TupleGetItem(func_8868_call(relay.reshape(const_9918.astype('float64'), [9, 225])), 1)
func_1064_call = mod.get_global_var('func_1064')
func_1067_call = mutated_mod.get_global_var('func_1067')
const_9939 = relay.const([[-2.022688,3.842178],[-0.676410,-6.898536],[5.595336,-5.884527],[4.879240,0.578099],[-0.307493,-6.425438],[-7.163872,-6.998420],[8.069948,2.100603],[3.598159,-6.912405],[2.060025,4.782201],[0.426269,3.960302],[-7.563326,1.332779],[7.872692,1.436483],[9.093571,6.675347],[7.149616,-4.691962],[9.907314,-5.181310],[-6.060320,-8.927067],[-6.784498,1.610909],[-5.270991,-1.776563],[-1.102844,-5.733308],[3.350634,9.909612],[4.889715,-6.748634],[7.400039,8.068716],[-0.221208,3.129942],[-0.536404,-0.733005],[0.173751,-1.341318],[-4.108658,-8.609916],[4.184088,2.777053],[-5.138453,8.577437],[1.515240,-8.013930],[-4.998975,5.347365],[4.350136,1.252410],[5.288966,-2.109562],[5.198170,-2.709105],[-4.806915,6.356660],[8.855069,-8.775424],[9.212276,7.585507],[0.842973,8.984706],[3.442388,-2.219833],[8.456977,-3.034947],[5.984420,0.715105],[-5.615883,-5.579731],[-3.795890,-5.604709],[-3.768032,3.300322],[-8.084142,-3.624642],[-7.127153,6.778994],[6.017406,-9.901049],[-6.980563,2.257288],[-3.718275,-1.277783],[-4.085324,9.836317],[-1.237859,-8.474940],[-1.959872,4.608222],[-5.823310,-4.615313],[6.721544,-7.291095],[6.585409,-6.771197],[5.393939,6.316203],[-1.833045,-3.116759],[-7.528946,-5.527163],[6.652758,-3.737933],[-5.049936,-4.734984],[3.586702,-6.951669],[3.612849,4.352847],[6.779921,-0.158124],[8.004982,-3.286740],[9.936176,-6.731261],[-9.876955,1.133445],[0.212756,4.594451],[5.945505,-3.000171],[-4.126725,5.212684],[0.736169,-8.253359],[-2.058518,-6.026309],[-9.342011,-1.682375],[2.973279,-5.253225],[8.351049,-7.858830],[9.401604,-9.293928],[1.675049,1.649278],[2.175653,3.185443],[-1.971207,-7.767323],[-9.598137,-0.997462],[3.633312,2.399361],[-8.650610,7.847638],[7.199612,-9.466644],[2.368712,1.537138],[-4.333866,8.961415],[7.110608,-2.235869],[-0.776612,8.710862],[0.304161,-7.124249],[-9.784770,-1.461108],[4.797031,-6.434769],[2.870824,8.440892],[9.709466,5.323057],[8.419712,-8.301832],[-4.002085,-7.647709],[0.633076,4.932963],[-8.393612,1.406787],[4.741509,9.897877],[9.665470,8.981146],[-8.725902,-3.731695],[6.796493,0.773349],[-9.949165,-5.945464],[1.902795,7.537221],[-9.622342,0.445886],[-0.163282,6.339974],[-0.962672,-2.969687],[-8.365493,-9.345245],[-0.084894,-2.588621],[0.364358,7.432647],[6.336951,-8.894429],[-3.934167,8.972174],[-8.927041,4.342306],[-6.991535,8.585337],[7.580304,-1.903241],[6.913007,6.635267],[3.580942,-9.190351],[7.464672,-2.321707],[6.423810,9.720056],[4.859312,-1.560833],[-1.773083,-9.466207],[-8.230189,2.265916],[-8.554050,6.273954],[0.977672,3.132459],[-6.811992,1.788927],[7.659443,1.674580],[-3.641712,2.339876],[7.143649,5.632394],[0.867696,-6.770547],[7.425984,-5.929743],[-8.189677,-7.893559],[-6.850665,-9.821843],[3.225488,-5.778509],[-2.776762,0.939086],[4.394024,-5.359661],[-1.545980,-0.884324],[8.614378,8.760170],[-5.740777,-4.036267],[5.887501,-6.795183],[4.470142,-1.591637],[-3.976012,2.372352],[-5.851321,4.112190],[5.753642,0.372510],[-2.404340,-1.290729],[-0.857296,-1.151979],[6.330843,5.065860],[7.499419,-9.273461],[4.977805,0.717644],[9.723316,-5.116912],[8.038645,3.099326],[0.165062,-7.046072],[-9.403410,4.208798],[-6.387325,-1.088505],[7.617827,-4.250371],[9.284045,0.947411],[-5.686041,4.430531],[6.054280,7.325372],[7.272040,-3.092546],[1.667157,-9.979425],[3.549669,4.823872],[-7.883058,5.665099],[5.089018,-4.492324],[-5.380930,9.873257],[5.605580,-3.717541],[-8.680899,0.381190],[9.566185,-6.298158],[6.523524,-3.161640],[0.031772,-1.558830],[4.097408,3.663613],[-7.928346,-5.127645],[4.242126,3.939953],[-7.019297,4.502880],[1.032770,-8.524115],[-2.463102,-4.801674],[-1.805289,-3.157689],[-9.114717,7.974237],[-0.451570,-6.756578],[-5.372186,4.254178],[8.290631,-6.204991],[0.059462,-3.770142],[5.453361,0.291021],[-6.342958,3.401152],[-5.554788,-3.278944],[-1.598508,7.456540]], dtype = "float64")#candidate|9939|(180, 2)|const|float64
call_9938 = relay.TupleGetItem(func_1064_call(relay.reshape(const_9939.astype('float64'), [4, 10, 9])), 0)
call_9940 = relay.TupleGetItem(func_1067_call(relay.reshape(const_9939.astype('float64'), [4, 10, 9])), 0)
func_5972_call = mod.get_global_var('func_5972')
func_5974_call = mutated_mod.get_global_var('func_5974')
call_9945 = func_5972_call()
call_9946 = func_5972_call()
bop_9954 = relay.floor_divide(const_9939.astype('float32'), relay.reshape(call_9938.astype('float32'), relay.shape_of(const_9939))) # shape=(180, 2)
bop_9957 = relay.floor_divide(const_9939.astype('float32'), relay.reshape(call_9940.astype('float32'), relay.shape_of(const_9939))) # shape=(180, 2)
output = relay.Tuple([uop_9911,call_9917,const_9918,call_9945,bop_9954,])
output2 = relay.Tuple([uop_9911,call_9919,const_9918,call_9946,bop_9957,])
func_9959 = relay.Function([], output)
mod['func_9959'] = func_9959
mod = relay.transform.InferType()(mod)
output = func_9959()
func_9960 = relay.Function([], output)
mutated_mod['func_9960'] = func_9960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8711_call = mod.get_global_var('func_8711')
func_8713_call = mutated_mod.get_global_var('func_8713')
call_10027 = relay.TupleGetItem(func_8711_call(), 0)
call_10028 = relay.TupleGetItem(func_8713_call(), 0)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_10029 = relay.TupleGetItem(func_2816_call(), 2)
call_10030 = relay.TupleGetItem(func_2818_call(), 2)
output = relay.Tuple([call_10027,call_10029,])
output2 = relay.Tuple([call_10028,call_10030,])
func_10031 = relay.Function([], output)
mod['func_10031'] = func_10031
mod = relay.transform.InferType()(mod)
output = func_10031()
func_10032 = relay.Function([], output)
mutated_mod['func_10032'] = func_10032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3803_call = mod.get_global_var('func_3803')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_10048 = func_3803_call()
call_10049 = func_3803_call()
output = call_10048
output2 = call_10049
func_10074 = relay.Function([], output)
mod['func_10074'] = func_10074
mod = relay.transform.InferType()(mod)
output = func_10074()
func_10075 = relay.Function([], output)
mutated_mod['func_10075'] = func_10075
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10081 = relay.var("var_10081", dtype = "float32", shape = (1, 15, 3))#candidate|10081|(1, 15, 3)|var|float32
uop_10082 = relay.sigmoid(var_10081.astype('float32')) # shape=(1, 15, 3)
uop_10090 = relay.cosh(var_10081.astype('float32')) # shape=(1, 15, 3)
func_10074_call = mod.get_global_var('func_10074')
func_10075_call = mutated_mod.get_global_var('func_10075')
call_10099 = func_10074_call()
call_10100 = func_10074_call()
uop_10114 = relay.atanh(var_10081.astype('float64')) # shape=(1, 15, 3)
output = relay.Tuple([uop_10082,uop_10090,call_10099,uop_10114,])
output2 = relay.Tuple([uop_10082,uop_10090,call_10100,uop_10114,])
func_10125 = relay.Function([var_10081,], output)
mod['func_10125'] = func_10125
mod = relay.transform.InferType()(mod)
var_10126 = relay.var("var_10126", dtype = "float32", shape = (1, 15, 3))#candidate|10126|(1, 15, 3)|var|float32
output = func_10125(var_10126)
func_10127 = relay.Function([var_10126], output)
mutated_mod['func_10127'] = func_10127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9328_call = mod.get_global_var('func_9328')
func_9329_call = mutated_mod.get_global_var('func_9329')
call_10133 = relay.TupleGetItem(func_9328_call(), 0)
call_10134 = relay.TupleGetItem(func_9329_call(), 0)
output = call_10133
output2 = call_10134
func_10139 = relay.Function([], output)
mod['func_10139'] = func_10139
mod = relay.transform.InferType()(mod)
mutated_mod['func_10139'] = func_10139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10139_call = mutated_mod.get_global_var('func_10139')
call_10140 = func_10139_call()
output = call_10140
func_10141 = relay.Function([], output)
mutated_mod['func_10141'] = func_10141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7521_call = mod.get_global_var('func_7521')
func_7523_call = mutated_mod.get_global_var('func_7523')
call_10163 = relay.TupleGetItem(func_7521_call(), 1)
call_10164 = relay.TupleGetItem(func_7523_call(), 1)
func_3299_call = mod.get_global_var('func_3299')
func_3304_call = mutated_mod.get_global_var('func_3304')
const_10177 = relay.const([8,-10,-7,-4,-8,5,7,1,-3,3,-4,4,-10,4,-10,9,-4,-8,10,7,6,-9,6,-6,-1,-6,7,-6,4,4,-4,3,-2,6,-2,-9,-7,-3,10,-3,8,8,1,2,-6,1,-9,-6,5,4,9,8,-4,10,-2,-7,-4,8,10,3,8,6,8,10,-7,1,-10,1,-9,1,6,2,2,-7,1,10,4,9,-1,-3,5,-4,4,10,8,5,-9,4,-8,-4,1,-10,-2,-6,8,-1,5,8,1,-3,1,-3,-6,2,9,4,-1,-4,-3,-6,-2,-6,10,-4,-3,-10,-4,5,-9,5,4,-10,6,-8,6,4,10,-3,-5,3,-4,4,-5,10,-7,-4,6,6,7,3,-9,-1,6,-1,-3,-8,-7,-6,1,-8,1,-9,-3,-9,10,-6,-8,10,-1,4,5,-10,4,7,-2,-6,-5,9,4,10,9,-5,-3,2,5,-5,-8,5,10,9,-4,-4,4,9,-1,-1,7,9,10,1,7,-8], dtype = "uint32")#candidate|10177|(192,)|const|uint32
var_10178 = relay.var("var_10178", dtype = "float64", shape = (2025,))#candidate|10178|(2025,)|var|float64
call_10176 = relay.TupleGetItem(func_3299_call(relay.reshape(const_10177.astype('uint32'), [6, 2, 16]), relay.reshape(const_10177.astype('uint32'), [6, 2, 16]), relay.reshape(var_10178.astype('float64'), [2025,]), ), 2)
call_10179 = relay.TupleGetItem(func_3304_call(relay.reshape(const_10177.astype('uint32'), [6, 2, 16]), relay.reshape(const_10177.astype('uint32'), [6, 2, 16]), relay.reshape(var_10178.astype('float64'), [2025,]), ), 2)
bop_10189 = relay.less_equal(call_10176.astype('bool'), relay.reshape(var_10178.astype('bool'), relay.shape_of(call_10176))) # shape=(15, 15, 9)
bop_10192 = relay.less_equal(call_10179.astype('bool'), relay.reshape(var_10178.astype('bool'), relay.shape_of(call_10179))) # shape=(15, 15, 9)
func_7233_call = mod.get_global_var('func_7233')
func_7239_call = mutated_mod.get_global_var('func_7239')
var_10234 = relay.var("var_10234", dtype = "int32", shape = (144,))#candidate|10234|(144,)|var|int32
const_10235 = relay.const(4.024613, dtype = "float32")#candidate|10235|()|const|float32
var_10236 = relay.var("var_10236", dtype = "float32", shape = (256,))#candidate|10236|(256,)|var|float32
call_10233 = relay.TupleGetItem(func_7233_call(relay.reshape(var_10234.astype('int32'), [6, 3, 8]), relay.reshape(var_10234.astype('int32'), [6, 3, 8]), relay.reshape(const_10235.astype('float32'), []), relay.reshape(var_10236.astype('float32'), [256,]), ), 7)
call_10237 = relay.TupleGetItem(func_7239_call(relay.reshape(var_10234.astype('int32'), [6, 3, 8]), relay.reshape(var_10234.astype('int32'), [6, 3, 8]), relay.reshape(const_10235.astype('float32'), []), relay.reshape(var_10236.astype('float32'), [256,]), ), 7)
output = relay.Tuple([call_10163,const_10177,bop_10189,call_10233,var_10234,const_10235,var_10236,])
output2 = relay.Tuple([call_10164,const_10177,bop_10192,call_10237,var_10234,const_10235,var_10236,])
func_10239 = relay.Function([var_10178,var_10234,var_10236,], output)
mod['func_10239'] = func_10239
mod = relay.transform.InferType()(mod)
var_10240 = relay.var("var_10240", dtype = "float64", shape = (2025,))#candidate|10240|(2025,)|var|float64
var_10241 = relay.var("var_10241", dtype = "int32", shape = (144,))#candidate|10241|(144,)|var|int32
var_10242 = relay.var("var_10242", dtype = "float32", shape = (256,))#candidate|10242|(256,)|var|float32
output = func_10239(var_10240,var_10241,var_10242,)
func_10243 = relay.Function([var_10240,var_10241,var_10242,], output)
mutated_mod['func_10243'] = func_10243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3401_call = mod.get_global_var('func_3401')
func_3403_call = mutated_mod.get_global_var('func_3403')
call_10260 = relay.TupleGetItem(func_3401_call(), 0)
call_10261 = relay.TupleGetItem(func_3403_call(), 0)
func_8218_call = mod.get_global_var('func_8218')
func_8221_call = mutated_mod.get_global_var('func_8221')
var_10269 = relay.var("var_10269", dtype = "float32", shape = (48, 1))#candidate|10269|(48, 1)|var|float32
const_10270 = relay.const([5.210958,9.882338,-6.844520,5.548192,2.492909,3.562839,-0.792300,3.802774,-6.669018,-1.880823,-8.162401,3.650984,8.397471,5.597266,2.077611,-7.531720,-5.827144,8.922351,6.556682,-4.556343,9.217325,6.634187,-9.877147,4.665665,-9.051586,-5.228401,-9.081210,6.030295,-4.733037,-1.490798,6.591634,-5.504600,-0.488004,7.912829,-4.277420,-5.083112,3.853854,8.974374,4.600602,-2.220972,1.784005,-0.438859,-7.587959,3.604829,9.131456,-5.304603,-9.806066,-1.188367,-1.113157,-0.074108,7.563012,7.365549,-6.746296,-7.578507,5.156199,7.102608,-2.057645,-9.750507,3.316669,6.271700,-0.603999,4.929380,-1.064402,5.907639,5.244187,9.438114,2.839331,0.860717,7.747270,7.871966,-6.916109,3.634143,-3.620932,8.724799,7.716455,-6.009150,5.711877,-2.861094,7.348495,-5.172697,8.130996,-7.397996,-2.684158,-1.913523,5.284126,-5.833219,-5.401997,-1.920664,-0.680902,-6.232176,-8.198565,5.065837,2.223282,8.218852,3.334956,2.980957,4.084445,2.873412,-8.297156,-8.205068,5.498274,3.174101,-5.411644,3.573435,-6.803829,8.952648,-6.106030,-8.161970,-6.463892,7.248224,6.112575,7.899204,-2.573833,5.703367,-1.771288,-5.566169,-6.780244,-4.556240,-1.276007,1.575194,5.648607,2.085028,8.836856,3.062619,-4.231313,-0.856592,-3.500076,-7.435926,-5.900767,2.902661,5.515880,1.377514,9.559120,5.378065,8.199034,-0.141208,1.379695,-2.704255,0.166490,-1.314365,-2.429969,-0.510207,-7.008590,2.674986,-8.130209,-7.375672,2.108249,6.743634,2.845419,-5.189567,-7.762237,8.567389,-8.868402,-2.572962,-4.414089,4.038622,6.157813,9.303165,4.471900,2.238608,3.734502,5.654151,1.068102,6.576573,0.827941,0.834489,0.110816,1.099057,-5.870612,0.052102,8.476832,-7.482168,-5.296245,-5.815627,-9.092018,0.135358,4.174833,-4.559789,-4.360467,3.931077,9.526365,3.397879,-2.360212,8.293203,-0.066190,3.756129,7.262574,1.905363,9.392216,5.150575,6.396533,1.346207,-3.616622,8.327482,1.200346,-7.742081,8.173891,5.149983,4.489853,-8.468241,-3.928242,5.355594,8.163661,4.789029,-6.921065,7.910848,-9.507077,7.102721,-4.377916,8.277962,3.131090,5.764776,8.781654,-4.309675,5.312773,-5.161929,-4.791343,0.791579,-3.209359,-9.103792,-2.445187,-5.754180,-5.577424,0.754341,-1.810915,0.790984,-3.219288,-9.775163,5.944739,-7.772421,-8.954730,-6.059422,-4.194231,-1.752955,3.182969,-9.464401,-2.966885,-3.029087,-7.716286,-8.849920,-0.402527,-5.763951,-0.770265,-0.387182,-2.929682,-4.282031,5.785614,7.600211,-9.101192,7.572590,9.537848,1.729632,-4.252372,-9.227998,5.066072,-0.405714,-6.244535,5.790654,4.502618,4.478441,-8.771746,-3.173710,-0.630899,-3.982466,-0.316431,-7.176712,8.030817,7.488898,2.506589,-0.917807,-4.347128,-9.377750,7.414541,2.267369,6.862438,-7.167478,-8.177735,-3.859558,5.991546,-7.627551,-3.721251,1.842886,-4.459664,9.744325,-9.252264,4.476546,-3.779479,-4.727304,5.720988,2.798357,-5.142527,-5.541536,-3.008887,4.539225,5.800371,2.475543,5.717968,7.878812,-1.999140,4.286439,-9.721191,0.862530,7.293496,6.692317,-5.514017,7.999912,-9.444181,5.904125,-1.692612,-8.340187,-7.600636,4.061664,-2.344213,-5.146356,-5.204143,-7.201068,-0.373329,8.677743,7.749456,-2.926897,4.773225,-6.839836,1.493633,3.818036,-9.322427,-5.970939,8.384318,-7.351541,-6.827093,-1.682559,2.212366,-6.402100,1.059133,2.199599,-5.046911,-2.154893,2.257615,6.056149,-4.138456,7.436174,2.538021,-4.535013,4.605219,-6.383738,0.015796,-6.449579,6.901528,-3.286453,6.904006,8.244455,4.670943,3.862768,-8.853641,6.527845,1.537911,-1.770436,-5.811414,-1.721852,9.352422,-6.789665,0.408060,3.878326,3.467518,2.144149,2.844820,-9.379269,-9.802720,-1.652505,-0.465881,-2.289164,-7.806433,-1.765084,6.674774,-7.039335,-5.908272,1.083717,-9.981142,-7.797503,-0.327639,-4.068382,1.365379,-4.403993,-8.453935,-1.850600,-1.292659,8.789275,8.884430,-8.664472,-4.378843,-6.402372,4.295792,-4.637431,-4.931092,2.889689,7.551295,2.672316,-3.474223,-5.998346,-7.101816,2.855054,4.714251,7.936233,3.167811,7.107719,-6.707303,-5.319402,6.629949,7.108664,8.696975,-7.370792,-1.060092,5.727265,1.372553,-2.640243,1.729381,4.699566,-5.157519,6.786384,-9.695108,4.779006,-8.336731,-3.228135,-1.032311,-6.529038,-7.949403,-8.352997,-2.798640,3.560843,-6.007971,3.776140,9.599041,-8.533885,1.279404,5.098835,8.511854,-8.132097,-1.314131,5.973182,3.351622,6.395910,8.711795,-5.374002,9.050848,1.614624,1.925219,2.994816,2.277376,-3.247413,-3.475531,-6.827864,-0.309518,9.466706,2.379964,-6.181199,-0.321325,-3.108657,8.377214,6.661180,-3.931077,-2.689583,9.521611,2.268515,-0.302549,3.405721,4.625965,-0.472426,7.453061,8.651032,-1.715395,0.457967,9.549729,-0.498265,-4.242146,5.870450,6.536606,7.277587,-9.449282,0.266378,-1.360920,5.235481,2.649963,-2.386632,0.931695,7.180373,0.119592,8.020280,3.502657,6.046992,8.953050,-0.921927,0.671024,-0.740695,-4.076268,-6.474896,-1.813569,9.427362,9.481892,-2.519697,2.720822,-1.924501,-3.075108,0.379021,-5.795964,-6.408193,5.689162,-2.465946,-5.337981,-0.198816,-7.166052,7.773135,-0.462169,-4.637856,-6.092347,1.575635,4.272607,-5.078504,0.463541,5.417216,5.096088,9.785871,-9.340742,3.797116,-2.860613,-8.974400,-3.521225,-0.902692,-5.322958,-5.520692,5.616809,-4.185512,3.419690,1.224641,-1.380483,-6.080873,-2.981538,-7.714665,7.145624,6.207711,-5.295050,8.479604,6.740138,0.204038,-5.271889,8.210706,1.091694,-1.027844,-1.761455,5.079579,-9.545782,-6.488124,-5.122446,-1.495667,-5.453185,9.645904,9.317447,7.815791,-5.446516,-0.470600,-2.340577,0.588864,1.927973,3.458145,1.580389,-4.397896,-4.551514,-0.326503,0.257332,6.216806,-4.177229,-7.698367,5.882202,-2.771812,5.102148,-7.522417,-8.912467,4.794423,-6.919717,-2.021110,-5.595519,6.949823,9.902932,4.036592,-5.929621,3.716602,2.967618,-9.992249,1.521247,0.930191,3.094037,1.542138,3.689113,3.652908,8.185754,4.032175,-0.530052,-9.913960,-2.967623,3.151303,-5.717150,6.321057,-9.795465,-9.152297,-9.737875,-9.675548,-4.183625,-5.085250,4.328930,8.870427,7.920539,-3.312601,0.180483,2.400969,-9.992605,0.300356,6.721625,-1.815776,-0.902279,-1.751805,-1.819332,1.229552,-7.860029,-0.704711,7.642209,-9.186638,-1.317179,2.337485,9.562129,6.330762,4.596350,1.654222,5.918995,-5.472038,-9.691463,8.489913,-8.381640,3.032002,-3.271001,-7.297348,0.708003,-2.005153,7.568813,-6.875481,-6.062404,-0.639279,-4.927518,0.584248,7.981913,1.454543,-1.420542,4.563220,0.530301,2.967093,-6.604752,-6.021612,-5.798515,-8.844359,-0.741617,-3.310202,-6.289260,-8.681926,-9.179745,4.929515,8.699032,-3.792649,6.113427,-1.079188,-1.065256,-4.204775,5.164177,0.546624,8.447419,9.572593,-0.863215,-3.770354,-5.915530,4.136676,-3.210083,5.910548,2.548242,7.670330,7.051370,-9.502005,1.282266,-7.131249,6.077994,-4.081591,8.521770,-5.577723,-5.735612,1.841624,7.263610,7.045952,9.297046,0.164946,-3.179253,5.173783,3.449398,-2.746125,-5.114010,2.674563,-4.064496,-1.880436,-9.290798,6.072738,1.706864,9.470068,2.635578,5.503977,0.705548,8.228424,9.437221,0.466172,-3.779009,-9.758460,6.074007,-9.642546,6.129859,6.256236,1.160794,-9.555958,1.149243,2.915386,9.690606,1.414234,-4.864987,-3.392688,0.017080,-4.985968,6.376546,-5.010071,-9.303636,-3.126721,9.985939,0.961715,-5.890827,-2.104340,-7.920610,-1.879242,-2.235419,-3.756800,4.576795,-9.156431,7.905580,-3.209650,5.704613,1.999858,-9.761069,-4.677686,5.429103,-0.024179,8.167774,-0.629936,6.908060,5.246698,-8.550048,-3.391824,4.465708,2.510703,1.975098,5.789464,-5.283661,-0.492066,7.509523,5.378731,9.129970,-2.659170,-8.722023,-2.658903,-3.517685,9.168696,3.995253,-0.959697,-8.428476,7.735014,3.902088,3.746869,2.024333,-4.980610,-6.087072,-4.431878,-8.613631,-9.417224,1.162542,-5.916989,0.100036,-0.805445,4.084088,6.726620,-5.658350,2.945030,7.496875,-5.618575,-3.003553,9.837914,-7.499904,-1.300278,4.153674,4.155389,4.478660,-5.356445,1.904373,-3.398560,5.254250,-0.064719,-3.613955,0.680003,-4.705880,3.930828,5.592790,4.679104,-2.757419,-1.576456,2.082867,-1.155466,9.793488,4.179723,1.412430,7.480522,9.994748,1.778194,9.681005,7.008857,-2.956408,-0.431616,-2.262224,4.372011,-4.563298,-6.955467,5.265349,-6.766035,0.095668,7.939969,4.727718,6.746629,-4.323365,5.331210,6.027564,-5.789698,9.740519,6.926092,-0.462700,-6.738945,-9.124518,-2.261349,5.040371,-9.888877,-5.062921,4.346473,-8.527884,-7.166797,2.953876,-3.245946,9.337164,-4.188548,-1.752896,-8.931309,-0.386019,5.444956,6.016251,-7.965105,-1.687951,6.230711,-7.195152,2.051329,5.370181,-7.485709,9.563969,4.611813,2.056124,9.203548,-0.561313,-6.807695,-1.339097,5.577655,-4.437851,-8.746653,9.440400,1.476636,-2.744329,-9.345238,0.439784,9.117210,-6.488011,7.276101,-9.714732,6.155323,-5.146323,-7.484410,8.950759,-9.493047,2.722199,-5.774725,-0.587289,9.779723,-4.904893,-1.763501,-7.737716,-2.344074,-5.141127,-6.151108,-7.327787,9.751671,2.220488,4.971568,-8.713928,-6.487907,-8.973356,-0.090765,2.450716,-4.898500,6.504248,6.402426,-3.211454,-7.969903,5.212893,1.297599,-6.244903,-9.165224,-1.481943,-8.378281,0.282179,2.465605,-8.659040,-2.319900,4.674507,0.252622,6.947195,-9.370109,0.439159,-2.783132,4.479783,-7.111310,9.016680,8.218247,7.387890,-2.819331,3.844701,-9.729150,7.869081,2.049831,5.980800,7.339630,4.865148,-5.949328,0.388930,5.657993,6.714547,-0.233649,-1.684790,-3.375147,-0.387414,-0.285681,-9.624017,9.252405,6.756536,-8.070219,6.804957,2.632806,5.661151,6.327096,-2.538057,2.345896,3.920669,-4.359920,-3.086633,2.851932,6.577393,-4.364070,-1.149820,5.444309,-0.828273,0.018900,-3.925187,-3.249454,-0.732680,-0.740092,-3.606312,-1.891387,7.473942,5.938684,-7.529482,-2.144797,-9.973175,8.415177,-2.785283,-2.471723,6.856463,8.383151,-4.164745,1.040302,5.799466,8.312260,-4.826569,8.564110,2.185236,5.475773,8.904484,5.906803,-6.909936,3.019428,-8.569246,9.936612,8.917641,0.502136,-8.282665,-1.082687,-0.763308,0.508121,-9.235313,-4.811671,9.271169,9.452195,-6.984462,-6.103814,5.524012,2.947506,1.787614,7.554109,7.897708,-2.717410,-9.033996,-4.226060,-7.796461,7.846395,-9.094834,-9.800531,5.713035,7.970655,0.347647,-9.235808,0.286719,-5.882020,-2.159249,2.521248,-8.637019,0.764088,-5.910883,4.045416,3.307737,7.513363,-4.111953,6.096851,4.585788,9.475137,-6.151131,-0.184368,-9.325269,-5.614812,-4.375400,-9.200905,8.057755,5.149971,4.977551,-3.867444,4.149033,5.758277,-8.096608,0.716670,8.602402,-9.485425,-0.599975,6.656196,1.873202,0.934996,3.935973,-9.092715,7.713264,-9.426589,-3.766497,8.115588,4.592128,3.597929,8.435905,6.288535,-1.677944,-7.375901,-4.108534,7.627392,7.510852,-8.269734,-3.925519,8.383090,-9.388221,4.227831,8.149742,9.573320,3.025214,-2.308206,2.439913,9.616202,8.823205,6.305173,5.468110,9.642585,8.545385,5.438597,-1.429910,-2.157446,-5.297760,3.227821,-4.291433,-6.676954,2.535679,7.841546,6.622038,-4.591475,-2.448715,-0.706939,-4.671642,1.869703,4.769867,-9.818453,8.117965,3.023547,-3.401395,3.836564,9.224552,-0.814600,-6.012839,2.375995,-5.761854,-7.406406,7.131416,-6.415378,-9.423429,-6.645488,-7.477345,3.422412,5.028702,7.301053,2.820706,-3.340630,6.690532,-8.023803,-8.350928,9.222406,0.306709,-1.130546,-6.305942,0.846749,-1.038207,0.543344,-7.891822,-2.213735,6.722391,8.816277,9.150076,7.191472,-5.918665,-7.756403,2.873385,9.794712,-7.939700,-9.692662,-3.240801,0.915907,7.415908,1.753720,-8.018366,1.451616,9.445773,-1.477963,-8.680639,2.682302,4.942329,-9.260001,6.878887,-8.765717,9.461216,3.171403,-8.460092,-3.884089,1.684512,9.810359,9.425940,9.634058,3.569467,8.780390,7.352433,-8.217150,1.444251,3.555415,-2.911389,-3.665341,-9.956693,5.732925,-7.082426,-9.554391,2.437664,0.432225,-7.209663,9.870240,9.347184,-6.535768,-4.676653,6.925070,5.269862,-9.490946,-6.883590,3.740290,-8.563108,0.391845,-7.538734,-4.570236,6.246984,-8.334116,-8.644217,7.973524,0.747196,-8.262957,-0.348267,4.711360,2.371317,8.293010,-8.573510,-7.933918,7.062026,6.785115,-8.403934,3.524293,-1.459066,1.032405,-1.393010,-8.628044,-1.929992,7.581660,-2.571205,-7.396626,-4.933682,-3.436633,-1.483097,-3.427127,-7.883457,3.615186,8.842545,8.328303,0.312039,9.270107,7.588164,8.343673,-5.716674,4.627491,8.974208,-7.124239,1.680661,-2.323447,-2.080576,-2.282250,-3.521843,7.845918,-6.682749,6.045920,6.429524,1.444115,-0.575857,9.892751,2.695854,-0.183029,-3.897007,6.624499,6.289120,-1.185514,-3.914073,-7.672704,-4.114003,-9.149776,-9.130748,-7.171470,-8.014529,2.232257,-3.508330,-7.891191,4.579055,-9.195387,5.070497,2.209422,4.442510,-4.707836,-6.602834,4.505352,-8.621377,-2.004755,0.817874,6.202299,-0.731801,7.385940,1.889863,0.155335,-6.486577,-0.100482,6.980384,-4.013391,5.248095,-3.025275,9.975257,7.225599,3.341583,6.835412,-4.713029,2.461618,9.130949,-1.936824,-8.553684,4.888545,7.630077,-9.324837,3.654515,-1.774089,-6.459104,5.544593,-0.492256,7.876790,-6.290704,-1.159398,8.248057,4.225831,-9.890947,1.581858,7.318877,8.295984,9.516103,8.190787,-5.972505,7.098875,-3.265893,1.684495,7.605050,0.723203,5.073874,5.128314,5.591460,7.712926,-0.335684,-1.561782,5.673611,-6.865198,2.206432,5.606079,3.595630,-9.517244,7.012954,-9.475673,6.741230,-5.821319,-2.210332,3.053106,6.683288,7.636598,-8.380788,0.584737,-9.875394,-3.434875,-1.687915,9.286664,-3.591674,8.958153,6.653884,0.850605,6.655590,1.712922,2.957263,4.666106,5.116982,-9.818180,-7.858567,9.285904,2.601092,0.753759,-9.018072,-0.410390,-5.912029,-6.058580,7.384322,-2.868419,-4.416128,-7.495163,6.210233,-1.973662,6.168681,-4.063206,-8.667869,-8.872121,2.709620,3.317268,-7.513984,-9.070886], dtype = "float64")#candidate|10270|(1386,)|const|float64
call_10268 = relay.TupleGetItem(func_8218_call(relay.reshape(var_10269.astype('float32'), [16, 3, 1]), relay.reshape(const_10270.astype('float64'), [1386,]), ), 2)
call_10271 = relay.TupleGetItem(func_8221_call(relay.reshape(var_10269.astype('float32'), [16, 3, 1]), relay.reshape(const_10270.astype('float64'), [1386,]), ), 2)
output = relay.Tuple([call_10260,call_10268,var_10269,const_10270,])
output2 = relay.Tuple([call_10261,call_10271,var_10269,const_10270,])
func_10276 = relay.Function([var_10269,], output)
mod['func_10276'] = func_10276
mod = relay.transform.InferType()(mod)
mutated_mod['func_10276'] = func_10276
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10277 = relay.var("var_10277", dtype = "float32", shape = (48, 1))#candidate|10277|(48, 1)|var|float32
func_10276_call = mutated_mod.get_global_var('func_10276')
call_10278 = func_10276_call(var_10277)
output = call_10278
func_10279 = relay.Function([var_10277], output)
mutated_mod['func_10279'] = func_10279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6581_call = mod.get_global_var('func_6581')
func_6582_call = mutated_mod.get_global_var('func_6582')
call_10314 = func_6581_call()
call_10315 = func_6581_call()
output = call_10314
output2 = call_10315
func_10319 = relay.Function([], output)
mod['func_10319'] = func_10319
mod = relay.transform.InferType()(mod)
output = func_10319()
func_10320 = relay.Function([], output)
mutated_mod['func_10320'] = func_10320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8018_call = mod.get_global_var('func_8018')
func_8019_call = mutated_mod.get_global_var('func_8019')
call_10399 = relay.TupleGetItem(func_8018_call(), 0)
call_10400 = relay.TupleGetItem(func_8019_call(), 0)
func_4834_call = mod.get_global_var('func_4834')
func_4835_call = mutated_mod.get_global_var('func_4835')
call_10427 = func_4834_call()
call_10428 = func_4834_call()
output = relay.Tuple([call_10399,call_10427,])
output2 = relay.Tuple([call_10400,call_10428,])
func_10438 = relay.Function([], output)
mod['func_10438'] = func_10438
mod = relay.transform.InferType()(mod)
output = func_10438()
func_10439 = relay.Function([], output)
mutated_mod['func_10439'] = func_10439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8664_call = mod.get_global_var('func_8664')
func_8665_call = mutated_mod.get_global_var('func_8665')
call_10473 = func_8664_call()
call_10474 = func_8664_call()
func_4978_call = mod.get_global_var('func_4978')
func_4980_call = mutated_mod.get_global_var('func_4980')
call_10490 = relay.TupleGetItem(func_4978_call(), 0)
call_10491 = relay.TupleGetItem(func_4980_call(), 0)
func_4906_call = mod.get_global_var('func_4906')
func_4907_call = mutated_mod.get_global_var('func_4907')
call_10495 = relay.TupleGetItem(func_4906_call(), 0)
call_10496 = relay.TupleGetItem(func_4907_call(), 0)
func_6096_call = mod.get_global_var('func_6096')
func_6098_call = mutated_mod.get_global_var('func_6098')
call_10500 = relay.TupleGetItem(func_6096_call(), 0)
call_10501 = relay.TupleGetItem(func_6098_call(), 0)
func_10319_call = mod.get_global_var('func_10319')
func_10320_call = mutated_mod.get_global_var('func_10320')
call_10502 = func_10319_call()
call_10503 = func_10319_call()
func_7887_call = mod.get_global_var('func_7887')
func_7889_call = mutated_mod.get_global_var('func_7889')
const_10519 = relay.const([[8.060332,-6.789147,3.611997,-0.181599,-8.156081,-3.085557,-0.180298,6.297278,-4.404047,8.553735,-6.061554,4.065998,-7.129218,-8.938806,-0.368230,4.082021,-6.792603,7.428317,2.355670,-7.926317,-2.600240,-2.476212,7.345368,-6.273059,-0.813175,1.591758,-2.893025,-0.738101,3.782783,5.391510,-1.109917,8.025476,9.976648,-1.480498,-2.853963,-2.646386,-2.421840,4.592999,-3.954591,5.302884,-9.353918,-2.059111],[9.625398,2.880760,6.188180,-7.667493,3.593697,-4.796716,-7.961316,5.714713,-4.775474,4.752067,2.929213,-9.771301,-9.261116,-5.751256,-3.150028,-8.793238,2.087306,-6.546592,-5.519522,-8.969620,-8.440260,-4.837138,1.289819,2.578702,-1.191892,-0.126163,8.646068,0.411993,-1.524900,-2.372217,-0.673978,-2.405018,-0.065737,4.673130,-8.038438,3.526911,-5.006006,5.522129,6.037215,4.538808,-0.649859,4.201431],[-8.556056,7.179267,-8.202043,8.972561,-3.459723,-9.802756,-9.402660,-1.937927,8.076391,2.299046,3.792053,-5.040426,1.232796,-9.634962,9.086432,-4.953650,7.852335,3.375272,6.736978,-7.142059,-4.463522,8.826004,-6.489791,8.325712,4.150130,-2.577766,-9.748895,8.565931,-1.948836,8.734781,-8.011628,-6.939382,2.260143,8.329969,-0.610688,7.240011,2.890443,-6.459236,-0.877846,1.802163,-0.849127,-0.244023],[-4.499344,0.200439,-7.743395,4.839587,-1.992201,-9.934152,9.515105,-0.657953,8.715813,-0.738025,-8.311640,2.093228,1.189312,-8.179372,-9.534296,-4.561802,3.250222,8.643003,-5.328227,-7.661364,-9.268367,-5.049629,-1.422285,-9.422721,-2.779589,-1.761461,1.985629,3.987452,2.038014,-9.026129,5.889761,-0.803057,-1.459183,-6.274045,-1.903805,6.881262,0.122653,-1.827273,8.673771,4.060397,-1.998796,-6.733499],[2.136534,-6.191268,-8.765981,-9.878003,9.925929,-5.066026,5.978433,-1.621054,8.988761,-4.770731,1.966019,-5.147444,9.436531,2.788556,-3.636298,8.596822,4.963470,-8.958213,5.572009,3.497528,2.361800,-5.647659,-7.666433,0.046334,7.295230,-5.088799,-2.553797,9.967642,4.899659,0.304694,-4.578896,9.706745,-5.679695,6.743212,7.880518,-1.175369,-1.528147,5.133547,2.724193,-9.685693,-5.634150,-8.368797],[-4.755642,4.650057,-5.428293,0.366225,2.221037,-8.823138,-8.412164,3.412619,0.252718,-6.210197,8.089542,-2.472643,-7.247394,7.503860,-5.390281,-8.656088,1.427702,-2.141177,-0.761401,-8.921390,-0.455316,-0.961105,7.874289,-4.228482,8.052622,-3.023776,-3.095033,-8.589054,-1.838255,-2.415210,8.800949,0.448881,-7.734159,-2.743946,9.509551,-6.297787,3.405207,-9.417938,1.218058,4.443304,9.124035,4.952610],[4.558820,9.719429,4.112277,-5.014929,-6.015892,7.981398,5.995798,9.001442,-3.184731,-7.293889,-1.887365,-8.511783,-7.221327,3.723522,-3.666350,5.539704,-9.994263,7.609622,-5.079285,-9.372028,1.068277,9.191883,7.769325,0.892568,4.788867,4.866678,-9.512322,9.874804,-8.878011,-9.194642,6.760301,-2.027973,-0.091576,5.075859,4.101874,0.445508,9.306303,8.787496,-2.916457,-5.931098,-8.540084,3.177835],[-0.573623,0.332288,6.844919,1.191284,-0.969220,-9.313091,8.343540,0.093793,3.301470,1.930999,-0.902666,6.672016,0.790064,-3.288605,-6.231877,-7.695917,-6.414631,4.755246,0.332108,-7.209412,-7.597663,5.975357,-7.049073,-0.998254,4.462506,-5.798700,-6.828923,-0.696463,0.255180,9.350305,2.513371,-8.992313,-4.620053,7.740889,-2.162450,4.664745,0.046027,-5.632495,7.899778,7.414962,-5.936519,-9.854125],[-7.809211,-9.510617,1.122220,0.989939,6.183408,-5.620729,9.560693,-5.727777,7.038727,-6.786519,-9.741342,-2.649613,9.123976,-0.379445,1.413737,-2.895330,-8.655271,-7.208445,-7.990203,-9.573226,1.587072,6.885024,-6.225781,5.558837,1.432178,-6.172274,-7.834029,-1.325122,4.024171,-6.938093,6.538440,-3.160916,4.423702,-9.673513,-5.358145,-9.414232,5.340952,-4.044453,6.669757,-1.047429,1.547025,-9.672613],[9.637716,8.493660,1.998739,-6.467400,-5.012084,-3.311973,1.544004,6.912107,4.553135,6.067656,-2.771373,5.489806,4.633662,-7.177943,-3.941833,4.307291,0.222693,-7.841614,-4.469442,-1.768381,1.996453,-7.466665,5.492051,-4.894490,8.634638,1.713851,7.936275,2.334406,-5.435485,3.832665,-6.717810,4.096769,9.421724,3.289278,-5.825994,-2.783852,-2.382200,-4.814476,2.964713,5.562475,-1.496184,-3.030584],[7.807135,1.152761,4.074503,-1.294622,0.613528,-6.223271,-9.600478,-5.911012,3.632609,-9.920479,4.121367,0.458171,-5.153067,-5.305296,6.902086,-3.956499,-8.187215,3.149954,5.788241,-2.147820,3.074487,4.425984,-3.788578,-5.779705,0.382734,4.960591,9.895264,3.602969,1.098842,-4.827766,-8.132387,2.708845,-0.972202,-6.188531,8.789139,-1.578108,3.692672,-7.758467,1.878305,9.012651,0.173775,-2.333889],[4.348364,-6.793496,4.076516,-6.923016,-5.958023,-2.122319,-5.631591,-4.700377,7.759692,-7.913884,-9.117611,-3.572662,2.783304,-4.827877,4.608861,3.373886,-2.374580,0.062416,-9.417685,6.790714,-0.587521,-9.588016,9.623415,-6.549900,9.417288,2.933864,1.798065,-7.227135,-6.071177,0.002149,3.694726,-3.013474,7.595877,4.926482,9.421958,-0.553410,-9.873590,-2.683200,0.435826,9.328297,8.464414,-6.727905],[-5.572473,0.252402,-4.062640,-7.082614,0.052650,9.576471,3.248069,6.852208,-2.116922,-2.588036,-2.546061,-0.646016,0.148328,-6.567065,-8.704710,5.589216,7.780072,8.159703,3.375703,8.039273,0.942282,8.141281,4.542155,1.773052,-0.294951,4.188827,1.750094,-5.685721,1.438808,3.013289,-1.950483,-2.811500,-3.547953,9.395009,-2.099414,-7.598009,4.478988,-3.550843,-9.866713,-6.074743,7.801424,9.275226],[4.681612,1.844871,6.975339,3.232575,7.602841,3.523404,0.156579,0.004167,-8.803780,9.964018,-0.231128,-0.265924,-7.102901,6.509889,-5.296326,-0.917635,0.786808,-2.881021,-3.542635,-5.583322,-5.785905,1.772067,-2.266161,6.799430,2.167001,-2.248811,-0.404866,-6.578700,-9.766668,-5.531220,2.951512,-8.198796,-0.113232,0.765833,-3.697877,-7.961970,2.839404,6.715309,-1.229176,-6.853654,6.127049,7.055625]], dtype = "float64")#candidate|10519|(14, 42)|const|float64
call_10518 = func_7887_call(relay.reshape(const_10519.astype('float64'), [14, 3, 14]))
call_10520 = func_7887_call(relay.reshape(const_10519.astype('float64'), [14, 3, 14]))
output = relay.Tuple([call_10473,call_10490,call_10495,call_10500,call_10502,call_10518,const_10519,])
output2 = relay.Tuple([call_10474,call_10491,call_10496,call_10501,call_10503,call_10520,const_10519,])
func_10527 = relay.Function([], output)
mod['func_10527'] = func_10527
mod = relay.transform.InferType()(mod)
output = func_10527()
func_10528 = relay.Function([], output)
mutated_mod['func_10528'] = func_10528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10529 = relay.var("var_10529", dtype = "int16", shape = ())#candidate|10529|()|var|int16
var_10530 = relay.var("var_10530", dtype = "int16", shape = (10, 12, 1))#candidate|10530|(10, 12, 1)|var|int16
bop_10531 = relay.multiply(var_10529.astype('int16'), var_10530.astype('int16')) # shape=(10, 12, 1)
output = bop_10531
output2 = bop_10531
func_10536 = relay.Function([var_10529,var_10530,], output)
mod['func_10536'] = func_10536
mod = relay.transform.InferType()(mod)
mutated_mod['func_10536'] = func_10536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10536_call = mutated_mod.get_global_var('func_10536')
var_10538 = relay.var("var_10538", dtype = "int16", shape = ())#candidate|10538|()|var|int16
var_10539 = relay.var("var_10539", dtype = "int16", shape = (10, 12, 1))#candidate|10539|(10, 12, 1)|var|int16
call_10537 = func_10536_call(var_10538,var_10539,)
output = call_10537
func_10540 = relay.Function([var_10538,var_10539,], output)
mutated_mod['func_10540'] = func_10540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5129_call = mod.get_global_var('func_5129')
func_5131_call = mutated_mod.get_global_var('func_5131')
call_10596 = relay.TupleGetItem(func_5129_call(), 0)
call_10597 = relay.TupleGetItem(func_5131_call(), 0)
output = call_10596
output2 = call_10597
func_10603 = relay.Function([], output)
mod['func_10603'] = func_10603
mod = relay.transform.InferType()(mod)
mutated_mod['func_10603'] = func_10603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10603_call = mutated_mod.get_global_var('func_10603')
call_10604 = func_10603_call()
output = call_10604
func_10605 = relay.Function([], output)
mutated_mod['func_10605'] = func_10605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1598_call = mutated_mod.get_global_var('func_1598')
call_10621 = func_1597_call()
call_10622 = func_1597_call()
func_4476_call = mod.get_global_var('func_4476')
func_4478_call = mutated_mod.get_global_var('func_4478')
call_10628 = relay.TupleGetItem(func_4476_call(), 2)
call_10629 = relay.TupleGetItem(func_4478_call(), 2)
output = relay.Tuple([call_10621,call_10628,])
output2 = relay.Tuple([call_10622,call_10629,])
func_10632 = relay.Function([], output)
mod['func_10632'] = func_10632
mod = relay.transform.InferType()(mod)
mutated_mod['func_10632'] = func_10632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10632_call = mutated_mod.get_global_var('func_10632')
call_10633 = func_10632_call()
output = call_10633
func_10634 = relay.Function([], output)
mutated_mod['func_10634'] = func_10634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_10701 = func_1295_call()
call_10702 = func_1295_call()
func_8518_call = mod.get_global_var('func_8518')
func_8519_call = mutated_mod.get_global_var('func_8519')
call_10703 = relay.TupleGetItem(func_8518_call(), 1)
call_10704 = relay.TupleGetItem(func_8519_call(), 1)
func_7761_call = mod.get_global_var('func_7761')
func_7763_call = mutated_mod.get_global_var('func_7763')
call_10709 = relay.TupleGetItem(func_7761_call(relay.reshape(call_10703.astype('float32'), [2, 16, 4])), 1)
call_10710 = relay.TupleGetItem(func_7763_call(relay.reshape(call_10703.astype('float32'), [2, 16, 4])), 1)
func_6271_call = mod.get_global_var('func_6271')
func_6273_call = mutated_mod.get_global_var('func_6273')
call_10730 = relay.TupleGetItem(func_6271_call(), 0)
call_10731 = relay.TupleGetItem(func_6273_call(), 0)
func_2305_call = mod.get_global_var('func_2305')
func_2307_call = mutated_mod.get_global_var('func_2307')
var_10737 = relay.var("var_10737", dtype = "float32", shape = (1320,))#candidate|10737|(1320,)|var|float32
call_10736 = func_2305_call(relay.reshape(var_10737.astype('float32'), [11, 15, 8]))
call_10738 = func_2305_call(relay.reshape(var_10737.astype('float32'), [11, 15, 8]))
func_2220_call = mod.get_global_var('func_2220')
func_2223_call = mutated_mod.get_global_var('func_2223')
const_10740 = relay.const([7.501940,-6.408089,3.365164,-6.333252,-5.057974,2.234882,5.150966,9.906992,-3.530072,-2.461426,-6.257114,-9.875744,6.381678,0.085238,-7.945493,5.366147,9.623322,6.818260,6.896669,-5.118161,-9.568982,9.435860,-4.257994,-7.824599,-4.532201,-3.062564,5.212162,4.084343,-9.158138,-5.063127,9.706779,-2.575581,4.025734,0.819037,-3.581036,-8.211009,-5.513963,-8.032637,2.845182,2.497570,3.062540,-4.939073,-1.674698,6.879738,3.050641,7.837830,-4.780026,7.259999,-5.741566,-6.702068,-4.778161,1.494878,-3.360631,8.369651,-2.720275,-0.577112,-9.021476,0.287950,-2.103551,9.138749,-2.798033,5.464508,1.063741,-3.622872,9.637059,-0.159444,9.880233,-8.409808,0.007137,4.704304,-4.418920,3.470427,8.768478,-0.049077,8.027544,6.196091,-3.121645,-6.856494,7.435232,1.790961,6.299179,1.422898,2.829056,4.697299,8.926997,9.769921,-5.040959,8.384219,5.100306,4.791439,7.090941,-6.243250,2.170331,4.788262,6.610617,-3.125493,-0.506409,4.065086,1.637215,-0.830795,-5.873058,6.158147,-3.387610,-2.206792,-5.780100,6.535166,-9.488456,5.614188,-0.383307,-6.403472,-6.276007,0.526357,-9.047156,-9.235527,0.143025,2.172194,-6.021279,-4.327403,9.669600,-1.037322,-3.124864,0.798026,2.648792,1.443402,-3.710007,8.359060,-3.477769,2.751252,-8.918035,-6.542898,8.217322,5.301615,-7.581951,-3.128488,-1.089918,3.175805,-3.136149,8.602952,-4.531783,-8.654130,-5.516395,6.007156,-9.814808,-7.986592,-2.881239,-1.155669,-8.949843,-5.300395,4.785007,-3.766118,0.342612,-3.648853,-1.949457,-8.795459,-1.005745,0.144789,-7.156637,0.659772,-4.350126,4.576466,9.351844,-1.382702,2.904040,-6.090914,5.264784,-0.213359,2.218334,5.311723,-7.155768,-8.198719,-2.744481,-9.666437,-5.157594,7.648635,4.124090,1.131273,-7.159087,-5.289965,-6.664751,-7.480859,5.183322,6.999119,3.258340,-5.800876,-5.539777,3.958975,9.722141,1.117487,6.002781,-6.581746,-6.571185,6.308708,9.285409,-9.120292,4.168089,1.238254,-4.552124,0.204765,7.440972,1.946020,-7.711939,-8.637508,-7.725206,0.969294,-2.062673,-0.548794,7.927334,3.134151,7.186018,3.225572,-8.397375,5.450030,9.829624,7.655373,4.160079,-6.466195,1.976486,7.419195,-0.764751,8.270821,-6.931179,6.391156,-3.919107,-7.296483,5.877807,-1.034049,-4.817194,-0.319924,-0.640389,6.566502,-3.906098,7.617159,-7.522944,-1.795850,1.112281,-8.472504,0.474986,0.227442,-2.262212,-8.558697,1.662290,-6.221445,-4.501165,1.203380,-1.949188,-4.139469,-3.402516,-7.033716,-6.114019,-2.956993,-8.170985,5.663981,-5.824681,1.812920,-9.805258,-6.021910,-1.649052,-0.192993,8.310124,8.468209,-1.637051,7.524844,1.601688,0.239847,-2.555932,1.121025,-1.660821,-7.213565,-6.851891,-9.147313,0.777611,-2.140618,2.189583,7.056645,4.366406,-9.434072,-3.633053,-1.411242,6.782538,-8.073242,2.030197,-2.723743,-7.888025,6.357186,1.399981,-9.880150,-8.241170,-9.028650,2.019614,7.267546,6.582097,-2.011410,2.178463,0.195152,-5.883851,-5.270682,-6.063690,-6.154266,6.999794,5.372955], dtype = "float32")#candidate|10740|(300,)|const|float32
const_10741 = relay.const([-3.389061,5.752562,-4.376076,-5.263540,-7.807498,8.741109,-2.877653,-8.167382,-6.298596,-3.038314,8.688780,-1.558600,-7.051544,2.371045,4.467126,-6.744889,9.789009,9.077155,-2.611812,6.015640,-9.401301,-7.132146,0.228211,5.017272,4.504608,-5.899652,-6.880384,8.294168,-4.397780,-1.394603,-9.267830,-9.930250,-3.802995,7.382433,2.292565,0.639281,-8.039581,-3.660766,-5.100892,1.663950,-6.469554,6.081040,-3.638142,5.564613,7.951715,-2.551644,-5.868247,0.697871,-0.380349,7.711247,7.154044,8.152499,-9.845780,-1.923725,-0.003090,-1.135186,7.038551,3.111035,8.512951,3.917679,1.104723,-7.837084,-1.988136,-1.975262,5.257904,-8.409197,2.351569,-2.131262,-6.775514,-7.839919,-1.166685,0.437668,-6.482183,-0.809451,2.726715,7.723336,3.008318,2.879982,9.600479,9.543850,9.582529,-0.156801,4.762036,0.066742,7.844831,-9.215043,-0.238110,3.659781,6.428088,-9.344988,3.910460,6.515333,-1.819702,-9.329888,-0.672378,-1.636663,-7.523551,-7.812324,0.561112,4.930274,-4.668924,-2.590297,2.843712,8.937761,8.628078,1.449072,4.812772,-9.528072,3.412980,-7.826798,-7.070377,-2.922363,4.801382,-6.694171,-2.007924,0.524215,-5.644715,5.906633,4.922090,-5.193671,7.410196,-8.470975,-4.125393,-2.632457,4.711945,6.743904,3.762629,-2.926157,9.538915,4.452752,-8.627666,-5.016779,-6.603115,-9.002690,-3.718485,9.350637,1.835035,1.553933,-4.216886,0.771423,-6.165212,9.214305,-2.413599,-9.017610,-2.831198,7.202578,-4.644206,2.564683,-6.256165,-7.035110,-0.808662,-6.540983,3.370271,9.266704,0.400939,-5.582317,-3.570432,1.680979,2.867995,-1.717022,5.831057,7.997493,8.674987,-4.847105,-1.472654,-2.894329,-1.798038,-2.670699,-6.461133,1.413303,2.883705,0.722980,5.865211,-6.233928,-5.045901,0.294255,4.603726,4.545376,9.197974,-5.540894,5.276562,9.201895,9.709426,4.357132,4.464044,4.145053,-9.600219,-4.061112,2.453425,0.240139,9.744054,3.054513,8.998880,4.270130,-9.645350,-8.778553,1.566469,-1.234024,-5.583888,-3.621236,-1.964572,-7.033631,2.018934,4.936439,5.584057,-4.909498,7.907825,1.404012,5.288645,2.835768,-5.199208,6.266238,3.341417,-9.176507,6.421675,-6.380036,-5.014754,7.650619,2.399711,-7.148310,9.943507,-2.922645,-3.320332,4.947960,-0.207320,-8.675626,-6.378845,-3.076663,7.224914,4.680016,-3.326007,-9.580287,-8.751696,-1.480361,-6.975738,3.477409,9.441078,-4.652785,3.028462,4.385655,9.032348,4.338310,6.560132,0.343015,-2.753358,-7.958923,-8.730297,-6.540988,-8.671417,8.046378,0.838169,-6.922110,-1.939369,3.581238,-2.282615,9.070245,-5.161954,0.608264,2.920013,-8.982590,-3.320953,-5.252978,3.710922,3.835489,9.319533,4.445993,4.171141,6.931222,-8.283479,-8.856862,-3.229262,-6.599184,-5.233008,-9.495672,4.534374,3.809691,8.682907,-8.223775,-8.300069,-3.201615,-3.300925,5.004955,1.077495,7.265090,7.369260,-9.328208,-9.309834,-0.512929,5.185217,-0.612842,3.816544,-3.501006,6.810359,3.109443,-2.996302,0.222077,9.601707,4.690508,5.001059,0.319006,-5.949657,-6.289848,-5.140979,0.847365,-4.263708,-0.323929,1.745372,-3.027945,-0.414099,9.794185,-2.192619,5.243801,2.047397,-9.308881,-8.019088,5.555952,-1.572432,9.036296,-7.075688,-9.352711,-7.987085,-1.938105,1.269753,-0.867619,-4.558379,-0.049870,-4.764010,5.379448,-2.469670,-7.079182,1.082141,8.983469,-0.582438,-0.898848,1.795261,1.660261,-6.508566,-5.557603,-7.369477,2.387920,-6.229284,8.728137,2.244367,-7.530740,1.146030,-6.366534,-0.330614,-6.886215,-2.404560,3.977664,6.112355,4.609978,-4.969793,5.729995,-1.072977,8.222739,-9.379840,8.396398,4.741989,-0.241949,4.098236,0.770277,-0.642164,-1.045324,8.857734,3.312187,-9.474766,-4.349601,-3.502646,3.372227,-2.646264,3.954747,-8.988992,-5.119744,-3.741793,-8.936695,-2.438440,1.117456,0.887148,7.159611,7.852549,2.848533,-6.518989,-7.894177,3.449079,7.171675,-2.348427,-0.873434,-2.276629,4.921752,6.870724,-7.351996,7.504451,8.727174,7.403150,8.175603,2.802305,-4.639686,-5.796238,-8.313943,-1.062947,8.422314,-5.532114,3.164350,9.453007,8.233617,-6.965720,-7.166926,9.097728,-8.457642,-6.878296,1.011822,-4.944878,3.909907,-8.857393,-4.646688,-6.065956,1.980153,-2.815540,0.499572,6.079104,-3.053925,-7.419524,-3.165580,-4.897152,-9.361929,-8.789686,-8.089129,4.897768,-3.497258,6.926821,-4.446237,-7.421709,-1.073703,8.205967,-6.326588,-8.208419,-6.371086,8.231091,-4.173765,-7.196146,3.096145,-3.204087,1.444325,2.892926,4.649093,2.458758,-1.427883,-9.412756,-4.941587,-4.344715,-9.769058,0.310869,8.161580,0.726440,4.224759,-5.376723,7.570095,-7.848922,-1.823471,-5.514695,1.228368,-8.191934,6.537852,-3.369058,-1.009460,0.470692,-0.856488,6.642273,4.854051,4.003101,-8.707577,7.913413,7.441466,0.900012,-5.898568,3.689664,9.488688,8.758128,-1.315904,-7.072411,3.919942,-2.858646,-2.376411,7.984392,-7.555087,-7.031488,7.278960,-6.158149,-3.580215,-0.389795,7.483837,-7.392290,8.421375,-0.574757,4.221747,-1.573687,-5.908343,-5.244967,1.870440,-4.271403,9.528881,-2.953513,7.271490,3.738876,-3.975332,-3.969063,8.026579,-1.526613,-6.884845,4.487247,0.915742,-0.087799,-9.323776,7.754309,5.501113,0.136246,-9.595399,7.241275,1.723491,6.625021,-1.061562,5.612823,-6.733819,6.754136,-5.378623,6.653206,-2.633355,6.507045,-2.697832,-9.528884,9.357540,-5.571852,-9.889644,8.663395,-9.044449,4.458356,-5.460308,0.891728,5.620081,9.470654,5.048722,1.588281,0.484342,-7.941955,0.400807,2.775044,-2.402114,4.157958,0.269601,-0.601044,0.441973,-8.858472,3.038116,1.916347,-0.349846,-7.267655,1.420097,-3.179285,0.252709,-3.250418,2.281101,3.518549,-3.284277,-4.903577,1.075955,1.283710,2.586854,-3.907032,5.781564,8.496241,-4.031893,8.018500,0.093534,-9.095509,-7.507780,-8.544501,-9.066810,-0.647955,-7.010732,-8.357647,0.127721,-3.356220,-6.166950,1.062554,-4.816718,9.860830,7.116287,-2.705308,-2.331657,5.552714,-3.161947,5.593966,9.822978,6.312936,-5.544328,4.262551,1.609116,-5.999318,-8.328942,-5.676627,-4.725061,0.930362,-8.008509,4.198851,9.852161,-4.178050,-7.502209,-7.673189,9.553427,5.786525,-0.606519,1.880521,-7.396364,1.938732,-7.167980,-9.186123,2.249603,-9.214550,4.112880,0.991736,-8.398783,-7.354136,3.513926,-3.567108,-3.388574,-5.313659,-0.706019,0.896104,-1.462036,0.835884,-1.400605,2.329996,6.798429,5.068811,1.239579,0.730346,-2.660990,-1.572787,1.650263,-9.405030,-7.818632,-5.411572,2.624509,-8.156974,-8.932945,-4.932340,6.716814,-4.570824,5.068456,3.421919,-7.764889,-8.840555,4.395058,-8.505635,6.276111,-1.556312,-9.620428,-9.298719,-0.224242,7.643902,-9.586290,4.771541,1.949261,-4.931583,-6.277497,-5.984294,0.268707,8.637440,0.602408,0.607771,0.319655,3.568782,-5.859361,3.430840,-1.536525,5.941530,-9.800655,-9.824941,-1.822226,-4.671161,-4.671006,-4.511947,2.952697,-8.155681,6.651498,0.125359,-4.686897,-0.863826,-6.602082,2.447307,-6.738967,8.119189,-2.697155,6.834042,-0.198901,6.627566,-8.210047,-2.711834,1.825401,-9.896480,-9.625120,5.178936,-6.724092,6.066264,9.032769,2.800252,3.673553,-2.058434,-9.469850,7.886497,1.139102,-4.669879,-5.614627,9.137265,7.835240,-9.208525,2.551431,-3.346101,-5.521082,-4.555443,5.950070,4.877008,-9.627437,-2.559212,6.187499,-7.553191,-8.282160,-7.498142,0.283820,-0.530652,-1.383235,2.144217,3.487128,0.637878,4.634527,0.973092,-4.684721,-5.199950,0.944890,3.845182,-1.586046,7.943480,-8.106309,8.303407,-1.128796,0.286943,-2.190611,-7.888849,-7.787355,0.154898,-2.928946,-8.166211,-8.371996,8.590914,2.495248,-6.574468,-7.880435,-1.712526,-0.095702,4.183163,-6.440909,0.059125,4.176190,-5.902199,2.753665,7.435787,-3.389419,-4.934730,-8.123695,-8.749687,6.957347,9.260480,8.049965,-2.814018,4.399598,-7.684743,-4.217790,3.490393,3.216591,-5.099377,5.023758,-1.368592,5.768275,-0.799758,7.612947,-0.252583,-3.165610,-5.058108,2.212003,2.911345,-7.869719,-1.532101,6.983700,-1.570527,4.999271,7.217006,5.223326,2.193325,7.963472,-6.569115,-2.408408,8.164285,3.857162,-9.222203,-4.964693,2.977961,9.592210,-3.678512,2.035073,-5.594094,1.204403,-5.297935,8.052293,2.006741,2.240321,2.803543,-9.403059,-4.483358,4.931104,3.535395,-7.821745,-7.693038,-5.754840,-8.015875,-6.305387,9.135643,0.685119,-2.014809,6.249533,1.240258,3.139477,-2.371550,3.127445,3.947024,-0.033060,-9.821331,-6.760704,-9.567189,6.328118,-9.742320,7.407321,1.925146,7.716031,-5.446967,-5.288145,-7.959594,-3.784895,3.807873,6.620026,-0.522005,2.219562,4.997183,-2.810160,8.168620,-6.296029,6.635811,9.706048,-7.315261,-6.739171,7.457799,-6.264750,-2.038724,-9.569790,-8.899572,3.481835,4.169451,-5.660866,-9.482267,1.175417,-6.323885,0.687356,3.057983,8.585998,-9.319956,-6.734715,-2.552111,9.362368,-3.009693,-6.180768,3.555887,0.352511,2.922870,3.901505,-0.864610,1.262286,1.149138,-6.968087,7.579035,-1.513036,8.066331,6.446562,-0.609656,8.723544,-3.898022,3.561261,2.305643,4.860460,-7.065280,-2.946479,8.512833,-7.024329,-6.732766,3.412260,-5.780011,2.438810,4.354194,0.222313,8.471591,-3.240435,-0.040829,-8.814126,-6.541115,-0.597045,-1.055123,-4.437612,-7.405285,-6.609015,3.829906,-6.460321,-1.702826,-4.475029,-4.323735,3.329793,-5.710703,-8.865148,1.733448,-9.983515,-5.956242,6.187203,8.601277,-2.804059,-6.736848,-6.029362,-7.611457,0.956831,9.766324,-3.479450,0.932423,5.040554,0.001371,-1.483582,-3.204665,7.637712,-7.616266,-4.891075,-5.689223,5.805054,5.096702,-7.805521,9.915002,-0.738325,6.990266,-3.585953,-0.158755,-6.965392,5.535461,0.318678,7.969075,-4.230126,6.498770,3.599740,3.224179,-4.788865,4.369075,6.642947,-5.648259,4.010999,-0.931914,-8.501268,9.371158,9.490014,0.454445,9.239756,8.919159,-4.316251,-7.199262,-2.934333,6.166139,-0.687713,4.470887,4.235304,-9.211465,-8.985271,-7.805150,2.898474,2.006624,6.260297,9.074256,-4.823387,-7.742423,5.398165,-0.711256,1.892248,-2.852980,-6.733046,5.077680,7.246433,-2.690711,-3.532061,-6.008038,1.185243,-5.704494,5.420771,8.314235,-2.300373,-2.210065,-4.712109,0.680271,-3.588020,7.267706,-6.702595,-3.844332,-7.284444,7.867125,-7.120844,4.038102,6.057715,-4.107773,8.906252,-7.162260,6.885722,-9.108298,-6.821989,4.708627,0.899298,0.172874,0.692106,-2.834825,8.471841,1.895427,6.248164,1.813689,-8.936777,9.955762,9.442897,-6.254691,7.238068,-4.978183,-5.670404,-5.438327,-3.153450,8.879598,-6.811289,-6.777221,6.429588,7.450967,-7.976429,-8.337030,-3.665049,-1.636526,0.558525,-4.192815,4.462956,-7.198650,8.987514,-3.529980,0.601326,4.059808,8.612888,1.821589,3.066503,3.459161,9.528785,5.660568,-9.393097,7.464242,-1.980799,-5.731004,-0.685559,2.288702,8.345754,8.947602,-1.478278,-5.431976,-6.865821,-0.153889,-9.782692,6.122823,4.928804,2.462344,1.090414,-6.298851,8.502314,4.594035,4.960527,2.776148,-0.108892,5.419260,1.391614,-2.550513,4.187038,-1.261380,3.842180,9.818017,-5.778123,-9.103143,4.575239,4.971012,4.759145,-5.660678,9.434737,3.666315,7.334677,-8.741031,1.858666,-9.249010,-0.345466,-1.921561,3.634555,-3.817945,8.297978,0.446760,8.661297,3.072549,9.632033,-4.470530,5.253162,2.954898,-2.582791,2.004606,-6.428397,0.785563,-2.133287,-4.438256,5.677875,0.875973,3.906306,-1.737566,4.516842,5.674106,2.893132,-2.347132,-4.034567,6.356707,6.477204,-4.126311,8.805848,-4.210428,3.225404,0.368209,-9.906645,4.203012,1.260638,-6.130005,3.053698,2.670513,0.581981,8.731666,1.702761,5.508766,-2.295417,8.748110,5.642457,2.390669,-4.966899,5.642772,-0.828730,1.629055,-5.755260,-6.410074,9.359957,9.273932,2.395722,-8.643508,8.414632,-7.949832,1.854067,2.669730,2.579772,-4.561276,2.179580,-8.884708,-1.365139,8.863946,-0.286591,0.035533,-1.907106,-8.943316,4.030959,-8.080457,-1.790602,-3.332777,-8.927774,-8.227866,9.341182,-8.708918,8.924514,-3.820342,-5.819683,-1.470324,5.203706,-8.157156,-3.318963,-7.364541,-0.435977,4.611192,3.909405,-8.394986,2.277553,9.152152,6.463108,-6.807511,3.844963,7.766437,-3.601101,-8.292669,8.281435,0.989092,5.768587,1.853811,1.283343,0.564744,1.788110,-5.657129,-8.301341,1.480723,7.074361,-3.595786,-0.453371,-2.475366,-9.166104,-6.856102,-4.079312,1.090852,0.383813,2.175304,6.248949,6.893250,-7.044549,-1.387023,-9.143123,8.759776,3.057144,-9.432846,1.042634,-3.583255,1.594790,1.516855,7.392208,6.995014,1.254112,3.240183,8.709408,4.769305,-2.683171,2.077225,3.867292,7.143341,-2.154153,-5.832255,-7.131849,3.810456,-4.986339,5.051532,-7.610571,-6.585172,9.597214,-4.454780,8.307081,5.468030,4.614744,-5.188153,2.386494,8.147779,8.444913,1.717743,4.491965,6.822555,1.374868,7.900036,8.085072,8.509824,5.113839,-9.700244,-6.696426,-4.140068,-3.966902,-6.597602,-4.785523,7.037270,-4.276876,-0.042212,-5.108979,3.990538,-2.913311,1.453862,-7.693549,0.044456,-0.404382,-0.405629,1.982398,4.750495,6.885246,3.134460,3.086969,5.990381,5.181401,1.806292,8.061017,7.291536,3.755307,-5.984279,8.472028,2.085319,8.186718,-6.375849,3.563567,-9.715521,-8.298821,-3.575620,-7.009583,4.855659,5.970409,9.317548,0.041605,7.497462,3.207729,-9.508613,7.845089,1.046084,-7.104453,6.517053,8.921323,-3.013527,4.463992,7.437273,1.786547,3.649185,-9.266135,6.007383,2.914135,-5.814589,-4.897329,1.273197,8.899960,-2.633807,2.988612,6.045733,9.154094,-4.369305,-6.924781,9.348231,-4.121516,6.711725,3.936851,-6.502589,4.254776,-9.392566,9.416292,0.881964,-9.703949,-6.716664,1.335968,-4.377300,-5.400702,9.762459,-7.033915,-9.557566,8.475531,0.498925,-7.333031,1.244832,3.485118,-5.636077,6.561996,2.372428,8.554135,6.120876,7.535030,-6.133070,-6.762784,-4.585176,-0.147430,5.642135,-4.192122,-0.844692,-5.951999,-9.152063,5.657379,4.745550,-0.947154,-6.869974,-2.054604,-9.551456,0.721197,0.529563,-3.147132,5.829109,-3.654659,-4.265829,1.844028,-2.276472,-9.598385,7.791672,8.328763,9.592528,7.774893,7.849928,5.581446,1.626396,-8.333505,4.897096,1.231004,9.919247,0.436971,-2.742096,3.866373,6.140035,-6.260854,2.985640,3.628342,7.527855,4.072066,-4.947248,4.745280,4.597370,3.843943,-9.657083,5.241244,-5.026038,-7.547790,-2.226027,2.980622,4.326563,-9.712617,2.806214,5.901520,8.703569,-6.371609,-7.178781,0.931041,7.805919,-7.805369,5.118805,-2.129999,-7.086578,4.630242,-5.955958,-8.957542,-1.172291,-5.208208,-3.005016,-7.989353,-5.675971,-5.073615,-8.380217,0.036805,-6.622949,-2.730160,9.941415,3.249429,7.923262,-0.272984,-1.551179,8.352456,-6.454261,-4.333086,-1.074776,-8.082025,8.008950,8.753759,-8.726327,-2.943364,-5.607310,0.607171,4.203956,9.755316,7.772052,-0.034099,9.150824,-6.419408,4.300794,-4.690330,9.188755,1.797586,0.962709,8.029181,6.184054,-9.545753,-1.501806,7.358678,1.122117,-1.582455,1.451509,-4.754417,-4.134969,-1.922828,6.549039,4.405857,4.256905,-4.224168,9.730942,-6.295812,0.764694,-6.852419,-7.860474,9.336964,6.802847,-5.520333,-9.450393,4.460945,9.154101,-1.164243,-0.144905,-8.673684,-1.528831,1.129291,-4.951881,-3.379975,-6.046322,1.301291,3.910807,-7.675725,-4.723385,5.375533,8.343307,3.202319,-0.631549,-8.603572,-7.138493,-4.333260,6.988649,-0.359080,3.492458,6.826227,-6.780282,4.770075,6.427760,-3.344300,-4.290336,-4.392063,-3.911197,6.843139,7.587849,2.128352,-8.767598,2.115695,0.725910,1.398352,-9.166280,8.952267,8.348244,-6.585906,-1.031871,-8.586984,-2.340561,8.620484,-8.254867,9.380851,-6.536945,0.750244,-7.540554,-4.680276,3.706291,2.292722,-1.141637,-4.101293,5.309650,-1.444023,9.395684,-6.961816,0.977141,-1.574957,-3.951588,4.828049,-4.125753,9.841957,3.668109,9.980724,9.803012,0.900668,7.342355,9.578760,-9.651642,-3.170640,-9.313197,-2.301786,-4.195983,-4.384324,-7.060241,7.497167,-3.454109,-8.721798,-6.151074,-4.743034,-4.889611,7.967391,7.353780,-1.854681,-4.745298,2.315026,6.784853,-4.935231,-2.128137,2.992363,6.675863,-1.897234,8.871565,0.134632,-9.383011,-3.522810,5.056419,-8.846598,-5.266947,1.787126,5.170847,-6.480249,-5.981243,6.575181,2.451605,9.703135,6.605379,-7.587541,-8.398477,9.740622,-5.433128,0.482026,5.515586,-2.947690,-2.651176,0.480631,9.851623,6.455365,-6.476551,-0.859877,4.654165,-0.077034,6.522402,5.030988,3.560405,-9.528758,-2.341767,2.194072,6.246302,-9.419467,4.799313,-6.902289,3.373723,-1.258992,-3.766511,0.307635,7.199569,-1.778107,-5.244065,-7.022953,-8.080373,9.973397,0.050658,5.915133,4.770485,-3.595222,3.369771,4.653930,-0.570287,-9.876941,-6.891204,-1.311790,-6.129213,9.831996,8.417267,-9.690864,-7.883986,-6.817213,-9.908292,7.679339,0.558790,9.960064,-3.430977,2.109735,-9.212287,3.024358,1.748341,-0.439930,-0.965166,2.197427,-3.411336,-7.193301,3.039261,-0.147512,-2.285211,2.098815,3.413972,-0.653856,7.736430,3.726121,2.720663,2.901143,-4.755293,-7.676823,2.799729,-3.797551,9.361226,-7.411441,-5.747971,8.054607,-6.264319,-1.695337,1.885793,0.784178,5.396383,-0.814775,5.975579,3.578790,-5.206559,8.209876,9.066571,5.375971,-6.228962,-4.006804,-0.917847,1.236774,-3.011327,-7.165176,-6.342642,8.676645,-7.915730,-0.231246,2.223843,-4.219909,-9.857718,7.582314,0.928000,-2.147416,-4.341606,-7.925566,-3.699807,-2.243540,-2.034328,-9.268679,-0.516354,-6.153940,-4.596470,3.067030,-5.996887,7.467635,8.457575,0.896742,1.876621,-1.252416,-6.665969,-9.998189,-0.766040,1.303746,6.135681,8.366040,3.898811,7.602619,-4.617345,7.786881,-1.450288,6.974179,7.559058,-9.792050,8.728274,9.865003,-7.697509,-7.170374,-1.607951,9.243797,-3.170335,1.731253,-5.604486,8.799018,4.106659,6.254343,4.763633,3.012884,8.856011,4.341021,-7.076686,-1.036347,-4.177123,1.979915,4.752187,-0.606235,1.264467,8.436971,-4.767572,9.276747,-8.827784,6.581287,1.911053,-4.600561,8.682555,6.104903,-2.248572,-5.527679,9.731943,7.705274,-3.730517,-4.477556,-2.775091,2.106908,-8.709088,-6.374840,0.829089,-2.364589,0.090593,-9.710047,-7.960801,-1.842112,5.162047,6.085170,6.112424,4.220520,-2.713324,4.363105,-7.489488,-6.261337,3.883224,7.478936,-2.786892,-2.468008,-1.757038,-9.070028,-4.591974,-0.432169,7.171736,-1.603391,-2.644104,-1.713132,8.635839,3.219239,-2.723613,-8.556762,2.688548,8.673162,9.325759,5.067780,-0.441113,-7.252067,-6.495168,-3.314608,-7.236595,-9.652310,7.541384,-8.891687,6.366815,-7.728887,2.586423,0.747055,-2.094816,-8.116271,-0.621343,1.080172,-5.855718,-4.335987,-8.758769,-8.246070,6.860891,-4.374069,-9.059868,-2.079485,-3.342352,5.090642,2.609436,-1.821096,1.486380,-7.300697,-8.468548,-8.973197,9.914225,-9.370343,-5.383295,9.254323,6.628927,-4.866746,-6.858468,4.678101,5.218244,-1.754765,-2.254857,-1.698499,3.580888,0.886955,-8.555416,-1.454980,-8.216451,-4.397803,-1.258979,8.511839,5.580737,1.312699,-3.802386,-8.899696,2.133829,-3.461384,-2.583444,-5.271766,5.557163,8.631588,2.365907,-3.544805,-7.374031,-5.334262,-1.607990,4.222877,6.730008,8.585693,3.468850,9.367735,-0.227677,-6.632392,-4.012629,-4.879435,6.846346,-4.979404,-3.566984,-1.126363,3.621253,5.974099,-8.431821,9.253020,4.311151,9.224959,-0.331254,8.265227,8.021776,6.423391,-3.432416,0.121068,-8.461812,0.417565,-1.813127,9.804659,-2.553528,4.938292,8.799536,5.031123,5.215728,-6.583162,0.064065,-8.280070,7.002004,1.164060,-5.854332,8.537675,-8.052573,5.499355,3.293630,-4.115530,7.895710,-6.847753,-0.143805,4.788462,4.088652,2.630781,4.033827,0.233901,-7.957800,0.362404,5.470044,0.552733,7.653122,2.116123,2.458332,-6.435109,4.554930,-4.843874,-5.631976,-2.077653,0.148796,0.915355,9.546450,8.690088,6.312250,-7.847560,-4.254384,-9.931581,-7.447417,-8.933250,2.222551,-9.674981,0.637029,-8.666057,-6.762704,5.075882,-9.290476,0.346352,7.793800,8.298369,8.580342,-7.594755,2.538884,9.239607,-1.961385,-6.105589,-9.266192,-4.251987,9.362546,-4.960957,6.490355,7.135545,-2.074303,-4.074173,2.716966,-8.807697,3.667435,-6.718046,9.338368,8.158757,0.317431,7.548583,-1.238880,-5.492886,-8.734739,-7.303846,-2.679518,3.095763,-3.547299,8.021214,-2.855691,-9.910093,-5.989907,-4.174947,-6.082059,7.131753,7.181815,7.612165,-3.491615,9.613738,-0.643376,6.167489,8.498614], dtype = "float64")#candidate|10741|(2025,)|const|float64
call_10739 = relay.TupleGetItem(func_2220_call(relay.reshape(const_10740.astype('float32'), [15, 10, 2]), relay.reshape(const_10741.astype('float64'), [2025,]), ), 2)
call_10742 = relay.TupleGetItem(func_2223_call(relay.reshape(const_10740.astype('float32'), [15, 10, 2]), relay.reshape(const_10741.astype('float64'), [2025,]), ), 2)
output = relay.Tuple([call_10701,call_10703,call_10709,call_10730,call_10736,var_10737,call_10739,const_10740,const_10741,])
output2 = relay.Tuple([call_10702,call_10704,call_10710,call_10731,call_10738,var_10737,call_10742,const_10740,const_10741,])
func_10775 = relay.Function([var_10737,], output)
mod['func_10775'] = func_10775
mod = relay.transform.InferType()(mod)
var_10776 = relay.var("var_10776", dtype = "float32", shape = (1320,))#candidate|10776|(1320,)|var|float32
output = func_10775(var_10776)
func_10777 = relay.Function([var_10776], output)
mutated_mod['func_10777'] = func_10777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3130_call = mutated_mod.get_global_var('func_3130')
call_10844 = relay.TupleGetItem(func_3129_call(), 0)
call_10845 = relay.TupleGetItem(func_3130_call(), 0)
output = call_10844
output2 = call_10845
func_10846 = relay.Function([], output)
mod['func_10846'] = func_10846
mod = relay.transform.InferType()(mod)
output = func_10846()
func_10847 = relay.Function([], output)
mutated_mod['func_10847'] = func_10847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5710_call = mod.get_global_var('func_5710')
func_5712_call = mutated_mod.get_global_var('func_5712')
call_10853 = relay.TupleGetItem(func_5710_call(), 0)
call_10854 = relay.TupleGetItem(func_5712_call(), 0)
func_1359_call = mod.get_global_var('func_1359')
func_1362_call = mutated_mod.get_global_var('func_1362')
const_10861 = relay.const(6.564032, dtype = "float32")#candidate|10861|()|const|float32
var_10862 = relay.var("var_10862", dtype = "float32", shape = (256,))#candidate|10862|(256,)|var|float32
call_10860 = relay.TupleGetItem(func_1359_call(relay.reshape(const_10861.astype('float32'), []), relay.reshape(var_10862.astype('float32'), [256,]), ), 1)
call_10863 = relay.TupleGetItem(func_1362_call(relay.reshape(const_10861.astype('float32'), []), relay.reshape(var_10862.astype('float32'), [256,]), ), 1)
func_9171_call = mod.get_global_var('func_9171')
func_9173_call = mutated_mod.get_global_var('func_9173')
call_10866 = relay.TupleGetItem(func_9171_call(), 0)
call_10867 = relay.TupleGetItem(func_9173_call(), 0)
output = relay.Tuple([call_10853,call_10860,const_10861,var_10862,call_10866,])
output2 = relay.Tuple([call_10854,call_10863,const_10861,var_10862,call_10867,])
func_10891 = relay.Function([var_10862,], output)
mod['func_10891'] = func_10891
mod = relay.transform.InferType()(mod)
var_10892 = relay.var("var_10892", dtype = "float32", shape = (256,))#candidate|10892|(256,)|var|float32
output = func_10891(var_10892)
func_10893 = relay.Function([var_10892], output)
mutated_mod['func_10893'] = func_10893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8492_call = mod.get_global_var('func_8492')
func_8494_call = mutated_mod.get_global_var('func_8494')
call_10935 = relay.TupleGetItem(func_8492_call(), 4)
call_10936 = relay.TupleGetItem(func_8494_call(), 4)
output = call_10935
output2 = call_10936
func_10942 = relay.Function([], output)
mod['func_10942'] = func_10942
mod = relay.transform.InferType()(mod)
mutated_mod['func_10942'] = func_10942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10942_call = mutated_mod.get_global_var('func_10942')
call_10943 = func_10942_call()
output = call_10943
func_10944 = relay.Function([], output)
mutated_mod['func_10944'] = func_10944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4906_call = mod.get_global_var('func_4906')
func_4907_call = mutated_mod.get_global_var('func_4907')
call_10969 = relay.TupleGetItem(func_4906_call(), 0)
call_10970 = relay.TupleGetItem(func_4907_call(), 0)
func_6199_call = mod.get_global_var('func_6199')
func_6201_call = mutated_mod.get_global_var('func_6201')
call_10977 = relay.TupleGetItem(func_6199_call(), 1)
call_10978 = relay.TupleGetItem(func_6201_call(), 1)
func_8218_call = mod.get_global_var('func_8218')
func_8221_call = mutated_mod.get_global_var('func_8221')
const_10980 = relay.const([8.571074,-4.648074,5.895832,-4.480230,2.549894,-9.896412,3.132154,3.531643,3.557433,-8.393123,3.539376,7.123353,-5.018313,-4.271280,0.627236,-7.104903,6.515704,5.428797,8.905684,-1.408050,7.534439,-6.329236,-3.686436,0.211089,-9.469965,0.918306,-4.953935,-5.348876,-5.617617,-0.270439,-4.890889,-1.863013,-1.321090,-3.980311,4.076214,-5.535896,7.018751,5.499184,-7.585059,6.673899,-7.071562,-3.863151,0.334116,0.249478,9.557025,-5.988385,2.982785,-7.211154], dtype = "float32")#candidate|10980|(48,)|const|float32
var_10981 = relay.var("var_10981", dtype = "float64", shape = (1386,))#candidate|10981|(1386,)|var|float64
call_10979 = relay.TupleGetItem(func_8218_call(relay.reshape(const_10980.astype('float32'), [16, 3, 1]), relay.reshape(var_10981.astype('float64'), [1386,]), ), 5)
call_10982 = relay.TupleGetItem(func_8221_call(relay.reshape(const_10980.astype('float32'), [16, 3, 1]), relay.reshape(var_10981.astype('float64'), [1386,]), ), 5)
func_1946_call = mod.get_global_var('func_1946')
func_1947_call = mutated_mod.get_global_var('func_1947')
call_10986 = func_1946_call()
call_10987 = func_1946_call()
func_4287_call = mod.get_global_var('func_4287')
func_4288_call = mutated_mod.get_global_var('func_4288')
call_10994 = relay.TupleGetItem(func_4287_call(), 1)
call_10995 = relay.TupleGetItem(func_4288_call(), 1)
func_5542_call = mod.get_global_var('func_5542')
func_5544_call = mutated_mod.get_global_var('func_5544')
call_11004 = relay.TupleGetItem(func_5542_call(), 0)
call_11005 = relay.TupleGetItem(func_5544_call(), 0)
output = relay.Tuple([call_10969,call_10977,call_10979,const_10980,var_10981,call_10986,call_10994,call_11004,])
output2 = relay.Tuple([call_10970,call_10978,call_10982,const_10980,var_10981,call_10987,call_10995,call_11005,])
func_11009 = relay.Function([var_10981,], output)
mod['func_11009'] = func_11009
mod = relay.transform.InferType()(mod)
var_11010 = relay.var("var_11010", dtype = "float64", shape = (1386,))#candidate|11010|(1386,)|var|float64
output = func_11009(var_11010)
func_11011 = relay.Function([var_11010], output)
mutated_mod['func_11011'] = func_11011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1532_call = mod.get_global_var('func_1532')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_11050 = func_1532_call()
call_11051 = func_1532_call()
output = relay.Tuple([call_11050,])
output2 = relay.Tuple([call_11051,])
func_11061 = relay.Function([], output)
mod['func_11061'] = func_11061
mod = relay.transform.InferType()(mod)
mutated_mod['func_11061'] = func_11061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11061_call = mutated_mod.get_global_var('func_11061')
call_11062 = func_11061_call()
output = call_11062
func_11063 = relay.Function([], output)
mutated_mod['func_11063'] = func_11063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7338_call = mod.get_global_var('func_7338')
func_7340_call = mutated_mod.get_global_var('func_7340')
call_11085 = func_7338_call()
call_11086 = func_7338_call()
output = call_11085
output2 = call_11086
func_11138 = relay.Function([], output)
mod['func_11138'] = func_11138
mod = relay.transform.InferType()(mod)
mutated_mod['func_11138'] = func_11138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11138_call = mutated_mod.get_global_var('func_11138')
call_11139 = func_11138_call()
output = call_11139
func_11140 = relay.Function([], output)
mutated_mod['func_11140'] = func_11140
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11146 = relay.var("var_11146", dtype = "int32", shape = (9, 14, 9))#candidate|11146|(9, 14, 9)|var|int32
const_11147 = relay.const([[[4,-10,9,5,-7,6,-4,-4,1],[3,6,3,-3,5,8,-1,-7,1],[8,-9,6,-2,-4,5,2,3,1],[3,4,-5,3,3,9,-5,-9,2],[2,8,-2,9,-2,-1,10,-4,2],[-5,5,5,1,1,-4,9,-10,-2],[-9,-6,7,3,5,-2,-7,2,-6],[-6,-6,-10,1,-10,6,3,5,6],[1,9,-7,3,-1,-5,-1,-7,7],[1,7,-9,3,8,-3,2,-6,-10],[-6,-4,-7,4,-10,-6,8,-5,1],[10,7,-6,4,6,10,2,6,-3],[-5,-2,-9,1,8,-4,3,-4,4],[3,-7,10,3,-3,6,-4,4,5]],[[4,1,-4,-10,-9,-7,6,2,9],[3,2,2,2,10,-2,9,2,8],[5,5,6,-8,4,-6,-10,2,4],[9,-2,4,-5,-9,-3,5,7,-3],[-3,-7,-8,7,-3,7,7,-5,-6],[-10,-2,-8,-8,-2,-4,-9,-5,-4],[-9,-1,4,-10,-6,7,-4,3,-7],[-10,3,-9,-8,-3,-5,5,2,4],[6,4,-9,-3,9,8,6,-9,1],[-7,-6,-1,9,-5,-4,6,5,3],[2,-8,4,7,5,9,5,4,-8],[4,-2,8,-10,-9,6,-10,10,1],[5,3,3,-5,-10,2,3,-3,5],[-3,8,1,-6,4,10,-7,1,-4]],[[-4,5,-5,9,-2,-4,-8,3,1],[-1,4,10,-1,6,8,8,-8,-5],[-1,2,-9,-10,5,2,-7,2,8],[-3,2,-1,-1,2,4,-4,-4,-8],[-5,9,-2,-6,1,8,2,8,-3],[4,-8,3,6,6,-4,-2,-1,-8],[1,3,2,1,5,7,8,9,-10],[7,2,7,-6,-6,1,1,6,3],[-7,3,4,7,-3,-8,-3,-10,-8],[10,7,10,-9,-9,-7,4,-5,-4],[-7,2,1,5,-5,-6,4,-7,-3],[-9,10,-7,10,-10,8,-5,9,7],[5,2,6,3,6,-1,6,9,-9],[2,-8,4,10,-3,7,7,-9,-6]],[[-10,5,8,5,7,2,2,5,8],[-8,-1,7,8,-3,-4,-3,7,-10],[-5,1,-3,-8,-6,-7,-4,-5,7],[-6,6,3,8,4,-8,-2,-3,5],[-5,3,5,10,-6,-6,-6,7,4],[4,9,-9,4,8,-4,3,5,5],[-7,-1,9,-5,2,9,-3,-7,-10],[-9,-8,4,-1,5,5,6,-4,-7],[6,10,-6,-5,-9,-3,-1,-5,-1],[-4,10,-8,9,8,-1,-8,9,-7],[6,-5,-4,-6,-3,5,4,6,-9],[10,8,-3,3,8,-1,6,-8,-4],[9,9,-5,-8,4,-2,10,-2,9],[9,-9,3,-3,9,10,-4,-5,3]],[[-9,-8,6,-7,1,-5,7,4,5],[7,-6,1,-10,-7,10,-5,-2,4],[-3,4,-2,-6,-7,6,8,1,-10],[2,-9,-2,-2,8,10,-1,2,-10],[-8,-5,9,-6,5,-2,10,-2,4],[8,3,-9,-7,-7,-8,5,-3,9],[-10,-8,-4,9,-4,-3,-4,-4,6],[-9,4,3,-5,7,9,-10,3,-5],[10,-3,2,5,-6,3,2,8,-10],[-9,-9,2,2,-8,-4,4,-6,10],[-4,4,-4,3,-2,2,-3,-6,-7],[2,-4,8,3,2,10,7,-7,-3],[9,6,8,5,1,4,2,9,6],[4,1,1,7,5,-1,4,-6,-3]],[[-10,-4,10,9,3,5,-7,-3,6],[10,-1,7,3,4,-4,4,3,-3],[7,4,1,-1,10,-7,-7,-10,-1],[-2,10,6,3,6,-7,1,-2,-3],[-4,-1,8,1,-2,4,7,10,4],[-1,-5,4,-7,-7,8,2,-4,-8],[-9,-8,9,-6,1,-6,-3,1,6],[-1,8,2,8,10,4,-4,7,8],[5,-4,2,-1,-7,-3,8,3,-2],[4,8,-3,1,7,-1,-4,9,-5],[8,-5,8,7,2,4,7,-5,3],[7,-5,-4,9,5,7,-10,5,9],[3,-3,-8,-2,-6,-7,-5,5,-9],[8,-8,-10,4,10,-3,-5,5,-5]],[[5,-7,4,-10,-10,-1,-3,-1,-4],[3,-8,7,2,-2,-2,-3,2,-9],[-5,5,5,6,-5,-6,7,6,4],[9,-9,-6,-7,9,-8,4,-9,-1],[-5,2,-4,-10,2,8,-1,-4,9],[-3,-7,-6,3,10,-10,-8,-6,4],[9,-2,-10,-6,9,-3,-10,-7,-1],[3,2,9,2,7,-8,-1,7,-9],[-6,-9,-5,-7,3,3,6,9,1],[2,-5,-3,-1,9,10,6,3,4],[10,-4,-5,6,-4,9,-4,9,9],[-2,8,10,-9,5,2,1,-9,4],[1,5,-6,3,7,-9,5,9,-1],[1,-5,-4,-6,-10,8,-10,5,-8]],[[-4,-1,2,9,9,3,9,2,2],[3,-8,4,-7,7,-4,1,6,8],[9,-7,5,10,6,10,-7,8,5],[1,8,4,-3,-7,6,-8,3,5],[5,-4,7,-1,-8,-10,-10,-5,-9],[10,3,-2,5,5,-5,-7,-8,-3],[4,1,-10,-5,2,-1,-10,-6,10],[-3,9,-4,10,5,10,-7,2,8],[-7,-2,-4,1,-4,6,-6,-1,-7],[-9,6,-7,4,5,-1,7,6,8],[-2,2,7,-4,-7,6,-1,10,-1],[-6,-10,8,-1,-9,4,-7,-8,6],[8,-6,4,6,-7,3,-3,2,9],[5,4,-9,3,9,-6,5,-5,-9]],[[-3,6,-1,-9,-9,10,-2,10,-10],[6,-6,3,2,-5,10,-9,1,6],[-6,10,7,-5,-6,-5,-5,-10,-10],[2,4,10,-5,7,-6,-10,8,-2],[-10,2,-4,-2,9,-10,8,10,3],[-6,-1,-4,5,-9,-2,8,8,7],[8,-2,3,8,8,-5,-10,-9,3],[-5,-5,-3,-7,-10,2,8,-7,9],[-2,3,-6,1,1,-4,3,-5,6],[-7,7,-10,5,9,8,-3,-6,2],[-7,6,3,4,-1,-6,5,2,3],[10,-9,9,8,8,10,-4,3,5],[-1,-5,8,-9,-7,4,2,9,5],[-7,-3,5,-6,-10,-10,-6,6,5]]], dtype = "int32")#candidate|11147|(9, 14, 9)|const|int32
bop_11148 = relay.bitwise_or(var_11146.astype('int32'), relay.reshape(const_11147.astype('int32'), relay.shape_of(var_11146))) # shape=(9, 14, 9)
output = bop_11148
output2 = bop_11148
func_11155 = relay.Function([var_11146,], output)
mod['func_11155'] = func_11155
mod = relay.transform.InferType()(mod)
var_11156 = relay.var("var_11156", dtype = "int32", shape = (9, 14, 9))#candidate|11156|(9, 14, 9)|var|int32
output = func_11155(var_11156)
func_11157 = relay.Function([var_11156], output)
mutated_mod['func_11157'] = func_11157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9282_call = mod.get_global_var('func_9282')
func_9284_call = mutated_mod.get_global_var('func_9284')
call_11274 = func_9282_call()
call_11275 = func_9282_call()
output = relay.Tuple([call_11274,])
output2 = relay.Tuple([call_11275,])
func_11278 = relay.Function([], output)
mod['func_11278'] = func_11278
mod = relay.transform.InferType()(mod)
output = func_11278()
func_11279 = relay.Function([], output)
mutated_mod['func_11279'] = func_11279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3803_call = mod.get_global_var('func_3803')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_11304 = func_3803_call()
call_11305 = func_3803_call()
output = relay.Tuple([call_11304,])
output2 = relay.Tuple([call_11305,])
func_11337 = relay.Function([], output)
mod['func_11337'] = func_11337
mod = relay.transform.InferType()(mod)
output = func_11337()
func_11338 = relay.Function([], output)
mutated_mod['func_11338'] = func_11338
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11362 = relay.var("var_11362", dtype = "float32", shape = (12, 15, 6))#candidate|11362|(12, 15, 6)|var|float32
uop_11363 = relay.exp(var_11362.astype('float32')) # shape=(12, 15, 6)
output = uop_11363
output2 = uop_11363
func_11372 = relay.Function([var_11362,], output)
mod['func_11372'] = func_11372
mod = relay.transform.InferType()(mod)
var_11373 = relay.var("var_11373", dtype = "float32", shape = (12, 15, 6))#candidate|11373|(12, 15, 6)|var|float32
output = func_11372(var_11373)
func_11374 = relay.Function([var_11373], output)
mutated_mod['func_11374'] = func_11374
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11414 = relay.const([[[5,4,2,-3,-3,7,-5,-8,-3,1,3,-5],[3,8,9,1,6,5,7,8,-7,3,-3,7],[7,5,-9,5,-2,-9,-2,6,6,-3,-9,2]],[[-5,8,-7,3,-4,-6,-1,-7,3,-3,-8,3],[10,8,7,7,-6,-2,-1,-9,-7,8,-5,10],[-10,-4,-4,4,-3,5,-2,-5,-9,-1,6,-3]],[[-6,-1,-5,2,-6,6,3,5,-10,-9,-3,1],[3,-2,4,2,-6,5,-5,-7,-1,-10,4,-2],[6,-9,4,-2,-3,-8,8,9,2,-5,8,8]],[[8,-6,3,-7,7,-9,5,10,4,5,7,-7],[-9,-5,-6,-8,3,5,2,-5,7,2,5,-9],[1,10,9,8,-10,7,-6,-10,-9,-4,-8,-1]],[[-5,6,6,-9,-1,-4,8,10,-5,-4,2,-1],[-9,-5,6,-2,9,-8,-5,-2,8,1,-10,-4],[8,5,3,4,-10,7,-2,-6,-8,6,3,-2]],[[-5,-9,-3,-7,4,-2,9,7,2,-7,4,5],[-10,-7,-8,6,-3,-8,9,-7,9,-9,3,2],[-1,-10,-4,9,6,9,-7,9,1,6,3,4]],[[-3,4,9,1,-7,-7,6,7,5,7,-2,-2],[4,-4,3,10,-2,-10,-10,-3,4,6,-7,1],[8,4,4,4,5,-4,-7,-2,9,-2,-7,-4]]], dtype = "int32")#candidate|11414|(7, 3, 12)|const|int32
var_11415 = relay.var("var_11415", dtype = "int32", shape = (7, 3, 12))#candidate|11415|(7, 3, 12)|var|int32
bop_11416 = relay.not_equal(const_11414.astype('bool'), relay.reshape(var_11415.astype('bool'), relay.shape_of(const_11414))) # shape=(7, 3, 12)
bop_11424 = relay.floor_mod(bop_11416.astype('float64'), relay.reshape(var_11415.astype('float64'), relay.shape_of(bop_11416))) # shape=(7, 3, 12)
output = bop_11424
output2 = bop_11424
func_11428 = relay.Function([var_11415,], output)
mod['func_11428'] = func_11428
mod = relay.transform.InferType()(mod)
var_11429 = relay.var("var_11429", dtype = "int32", shape = (7, 3, 12))#candidate|11429|(7, 3, 12)|var|int32
output = func_11428(var_11429)
func_11430 = relay.Function([var_11429], output)
mutated_mod['func_11430'] = func_11430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6271_call = mod.get_global_var('func_6271')
func_6273_call = mutated_mod.get_global_var('func_6273')
call_11462 = relay.TupleGetItem(func_6271_call(), 0)
call_11463 = relay.TupleGetItem(func_6273_call(), 0)
output = relay.Tuple([call_11462,])
output2 = relay.Tuple([call_11463,])
func_11476 = relay.Function([], output)
mod['func_11476'] = func_11476
mod = relay.transform.InferType()(mod)
mutated_mod['func_11476'] = func_11476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11476_call = mutated_mod.get_global_var('func_11476')
call_11477 = func_11476_call()
output = call_11477
func_11478 = relay.Function([], output)
mutated_mod['func_11478'] = func_11478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7731_call = mod.get_global_var('func_7731')
func_7733_call = mutated_mod.get_global_var('func_7733')
call_11479 = relay.TupleGetItem(func_7731_call(), 1)
call_11480 = relay.TupleGetItem(func_7733_call(), 1)
func_8018_call = mod.get_global_var('func_8018')
func_8019_call = mutated_mod.get_global_var('func_8019')
call_11481 = relay.TupleGetItem(func_8018_call(), 2)
call_11482 = relay.TupleGetItem(func_8019_call(), 2)
output = relay.Tuple([call_11479,call_11481,])
output2 = relay.Tuple([call_11480,call_11482,])
func_11484 = relay.Function([], output)
mod['func_11484'] = func_11484
mod = relay.transform.InferType()(mod)
mutated_mod['func_11484'] = func_11484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11484_call = mutated_mod.get_global_var('func_11484')
call_11485 = func_11484_call()
output = call_11485
func_11486 = relay.Function([], output)
mutated_mod['func_11486'] = func_11486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6573_call = mod.get_global_var('func_6573')
func_6574_call = mutated_mod.get_global_var('func_6574')
call_11622 = relay.TupleGetItem(func_6573_call(), 0)
call_11623 = relay.TupleGetItem(func_6574_call(), 0)
uop_11624 = relay.atanh(call_11622.astype('float32')) # shape=(2, 16, 4)
uop_11626 = relay.atanh(call_11623.astype('float32')) # shape=(2, 16, 4)
output = uop_11624
output2 = uop_11626
func_11644 = relay.Function([], output)
mod['func_11644'] = func_11644
mod = relay.transform.InferType()(mod)
mutated_mod['func_11644'] = func_11644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11644_call = mutated_mod.get_global_var('func_11644')
call_11645 = func_11644_call()
output = call_11645
func_11646 = relay.Function([], output)
mutated_mod['func_11646'] = func_11646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8711_call = mod.get_global_var('func_8711')
func_8713_call = mutated_mod.get_global_var('func_8713')
call_11727 = relay.TupleGetItem(func_8711_call(), 0)
call_11728 = relay.TupleGetItem(func_8713_call(), 0)
func_1532_call = mod.get_global_var('func_1532')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_11744 = func_1532_call()
call_11745 = func_1532_call()
output = relay.Tuple([call_11727,call_11744,])
output2 = relay.Tuple([call_11728,call_11745,])
func_11761 = relay.Function([], output)
mod['func_11761'] = func_11761
mod = relay.transform.InferType()(mod)
mutated_mod['func_11761'] = func_11761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11761_call = mutated_mod.get_global_var('func_11761')
call_11762 = func_11761_call()
output = call_11762
func_11763 = relay.Function([], output)
mutated_mod['func_11763'] = func_11763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7435_call = mod.get_global_var('func_7435')
func_7437_call = mutated_mod.get_global_var('func_7437')
call_11793 = relay.TupleGetItem(func_7435_call(), 0)
call_11794 = relay.TupleGetItem(func_7437_call(), 0)
output = call_11793
output2 = call_11794
func_11800 = relay.Function([], output)
mod['func_11800'] = func_11800
mod = relay.transform.InferType()(mod)
mutated_mod['func_11800'] = func_11800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11800_call = mutated_mod.get_global_var('func_11800')
call_11801 = func_11800_call()
output = call_11801
func_11802 = relay.Function([], output)
mutated_mod['func_11802'] = func_11802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11800_call = mod.get_global_var('func_11800')
func_11802_call = mutated_mod.get_global_var('func_11802')
call_11805 = func_11800_call()
call_11806 = func_11800_call()
func_8928_call = mod.get_global_var('func_8928')
func_8929_call = mutated_mod.get_global_var('func_8929')
call_11821 = relay.TupleGetItem(func_8928_call(), 0)
call_11822 = relay.TupleGetItem(func_8929_call(), 0)
func_11138_call = mod.get_global_var('func_11138')
func_11140_call = mutated_mod.get_global_var('func_11140')
call_11829 = func_11138_call()
call_11830 = func_11138_call()
output = relay.Tuple([call_11805,call_11821,call_11829,])
output2 = relay.Tuple([call_11806,call_11822,call_11830,])
func_11831 = relay.Function([], output)
mod['func_11831'] = func_11831
mod = relay.transform.InferType()(mod)
mutated_mod['func_11831'] = func_11831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11831_call = mutated_mod.get_global_var('func_11831')
call_11832 = func_11831_call()
output = call_11832
func_11833 = relay.Function([], output)
mutated_mod['func_11833'] = func_11833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4045_call = mod.get_global_var('func_4045')
func_4047_call = mutated_mod.get_global_var('func_4047')
call_11919 = func_4045_call()
call_11920 = func_4045_call()
output = call_11919
output2 = call_11920
func_11925 = relay.Function([], output)
mod['func_11925'] = func_11925
mod = relay.transform.InferType()(mod)
output = func_11925()
func_11926 = relay.Function([], output)
mutated_mod['func_11926'] = func_11926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6939_call = mod.get_global_var('func_6939')
func_6941_call = mutated_mod.get_global_var('func_6941')
call_11967 = func_6939_call()
call_11968 = func_6939_call()
func_8492_call = mod.get_global_var('func_8492')
func_8494_call = mutated_mod.get_global_var('func_8494')
call_11976 = relay.TupleGetItem(func_8492_call(), 4)
call_11977 = relay.TupleGetItem(func_8494_call(), 4)
func_2459_call = mod.get_global_var('func_2459')
func_2462_call = mutated_mod.get_global_var('func_2462')
const_11980 = relay.const([10,1,5,9,7,2,-7,-10,-7,-5,4,-10,5,2,-5,-7,4,-9,3,-10,6,-8,-2,-2,-1,-3,-6,-3,-2,-7,8,4,-6,-1,-10,7,1,-9,-6,-2,-9,-1,10,8,-10,1,-10,2,-5,-5,1,3,9,-7,-4,-1,5,-7,-5,9,9,5,-2,-7,9,-5,4,-4,-9,-6,-1,-5,-9,3,7,-9,-9,-8,-3,-1,-5,-3,-4,1,-10,-8,6,-7,-6,-8,10,1,-4,-4,4,-9,10,9,1,-7,7,-1,-9,-7,-9,-7,-4,2,-7,-7,10,9,8,-3,-8,-1,8,-7,2,-1,8,-2,8,2,-10,6,5,-1,-5,-1,7,-7,3,1,7,6,1,10,4,7,-1,6,-2,8,-9,8,2,-10,-9,-10,-2,2,6,7,5,4,8,-3,-4,8,1,-1,1,-8,2,-7,-4,-2,-2,-10,4,5,3,2,1,3,6,-5,-7,7,10,-8,4,7,-8,5,3,3,9,3,7,-2,-2,-2,-1,-10,5,-7,7,-7,1,4,3,9,-5,4,10,7,-4,-3,-7,7,-1,3,8,-3,-3,4,6,-9,-8,5,10,2,-10,-10,9,1,2,10,-5,1,-9,5,6,10,-1,-2,6,7,-10,-5,6,1,-1,8,-3,7,1,1,7,3,-6,-9,10,8,-4,-1,10,-8,4,-8,-2,2,6,5,5,-1,3,-1,7,5,4,-2,9,-5,4,3,-8,-3,8,-8,-4,-4,-9,3,6,-7,-5,5,7,-8,-3,8,6,6,9,-9,-2,-3,-9,9,4,8,-5,5,4,4,6,9,-5,-8,-8,7,-1,3,7,-7,-7,4,9,3,-5,-1,9,3,-4,8,1,1,8,-1,-5,-7,5,-4,1,8,-6,-6,-8,9,-3,5,2,5,-10,-4,5,9,5,4,5,-3,-10,6,-2,-1,1,9,2,5,10,-8,3,7,-3,3,1,-8,6,1,10,3,8,7,7,3,-1,4,-10,-1,2,-2,-9,5,4,-3,8,8,-9,-7,6,6,10,-3,-3,-3,8,9,6,5,10,6,6,-5,8,-3,-9,-4,-1,9,-1,10,-8,9,2,3,1,-9,3,2,-3,8,4,-3,10,10,4,3,8,7,-5,2,-2,-1,-3,6,7,-10,-7,5,-4,-1,6,2,7,4,10,9,4,-6,-2,3,-8,10,5,-3,2,-7,9,2,1,-9,1,4,8,4,-4,-1,9,8,-9,-3,4,-9,1,8,-7,-4,4,4,10,2,-5,8,4,-10,-6,4,-4,4,4,9,10,-10,3,-6,3,7,-1,-4,1,-8,8,9,-4,-1,-7,-10,4,-1,5,10,-5,8,9,1,-7,-7], dtype = "uint16")#candidate|11980|(520,)|const|uint16
var_11981 = relay.var("var_11981", dtype = "float32", shape = ())#candidate|11981|()|var|float32
call_11979 = relay.TupleGetItem(func_2459_call(relay.reshape(const_11980.astype('uint16'), [8, 13, 5]), relay.reshape(var_11981.astype('float32'), []), ), 2)
call_11982 = relay.TupleGetItem(func_2462_call(relay.reshape(const_11980.astype('uint16'), [8, 13, 5]), relay.reshape(var_11981.astype('float32'), []), ), 2)
output = relay.Tuple([call_11967,call_11976,call_11979,const_11980,var_11981,])
output2 = relay.Tuple([call_11968,call_11977,call_11982,const_11980,var_11981,])
func_11987 = relay.Function([var_11981,], output)
mod['func_11987'] = func_11987
mod = relay.transform.InferType()(mod)
var_11988 = relay.var("var_11988", dtype = "float32", shape = ())#candidate|11988|()|var|float32
output = func_11987(var_11988)
func_11989 = relay.Function([var_11988], output)
mutated_mod['func_11989'] = func_11989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4906_call = mod.get_global_var('func_4906')
func_4907_call = mutated_mod.get_global_var('func_4907')
call_11991 = relay.TupleGetItem(func_4906_call(), 0)
call_11992 = relay.TupleGetItem(func_4907_call(), 0)
func_4790_call = mod.get_global_var('func_4790')
func_4792_call = mutated_mod.get_global_var('func_4792')
call_12010 = relay.TupleGetItem(func_4790_call(), 0)
call_12011 = relay.TupleGetItem(func_4792_call(), 0)
func_6615_call = mod.get_global_var('func_6615')
func_6619_call = mutated_mod.get_global_var('func_6619')
const_12019 = relay.const([2.499957,7.944477,-0.521774,4.147406,-3.438419,5.996463,-3.941546,4.511080,-9.624862,-5.604331,-6.208351,1.248249], dtype = "float64")#candidate|12019|(12,)|const|float64
var_12020 = relay.var("var_12020", dtype = "float64", shape = (48,))#candidate|12020|(48,)|var|float64
call_12018 = relay.TupleGetItem(func_6615_call(relay.reshape(const_12019.astype('float64'), [12,]), relay.reshape(var_12020.astype('float64'), [48,]), ), 0)
call_12021 = relay.TupleGetItem(func_6619_call(relay.reshape(const_12019.astype('float64'), [12,]), relay.reshape(var_12020.astype('float64'), [48,]), ), 0)
output = relay.Tuple([call_11991,call_12010,call_12018,const_12019,var_12020,])
output2 = relay.Tuple([call_11992,call_12011,call_12021,const_12019,var_12020,])
func_12033 = relay.Function([var_12020,], output)
mod['func_12033'] = func_12033
mod = relay.transform.InferType()(mod)
mutated_mod['func_12033'] = func_12033
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12034 = relay.var("var_12034", dtype = "float64", shape = (48,))#candidate|12034|(48,)|var|float64
func_12033_call = mutated_mod.get_global_var('func_12033')
call_12035 = func_12033_call(var_12034)
output = call_12035
func_12036 = relay.Function([var_12034], output)
mutated_mod['func_12036'] = func_12036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4790_call = mod.get_global_var('func_4790')
func_4792_call = mutated_mod.get_global_var('func_4792')
call_12068 = relay.TupleGetItem(func_4790_call(), 1)
call_12069 = relay.TupleGetItem(func_4792_call(), 1)
output = relay.Tuple([call_12068,])
output2 = relay.Tuple([call_12069,])
func_12097 = relay.Function([], output)
mod['func_12097'] = func_12097
mod = relay.transform.InferType()(mod)
output = func_12097()
func_12098 = relay.Function([], output)
mutated_mod['func_12098'] = func_12098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5933_call = mod.get_global_var('func_5933')
func_5935_call = mutated_mod.get_global_var('func_5935')
call_12109 = func_5933_call()
call_12110 = func_5933_call()
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_12124 = func_6154_call()
call_12125 = func_6154_call()
func_4195_call = mod.get_global_var('func_4195')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_12154 = func_4195_call(relay.reshape(call_12124.astype('uint64'), [2, 16, 4]))
call_12155 = func_4195_call(relay.reshape(call_12124.astype('uint64'), [2, 16, 4]))
output = relay.Tuple([call_12109,call_12124,call_12154,])
output2 = relay.Tuple([call_12110,call_12125,call_12155,])
func_12161 = relay.Function([], output)
mod['func_12161'] = func_12161
mod = relay.transform.InferType()(mod)
mutated_mod['func_12161'] = func_12161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12161_call = mutated_mod.get_global_var('func_12161')
call_12162 = func_12161_call()
output = call_12162
func_12163 = relay.Function([], output)
mutated_mod['func_12163'] = func_12163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1295_call = mod.get_global_var('func_1295')
func_1296_call = mutated_mod.get_global_var('func_1296')
call_12166 = func_1295_call()
call_12167 = func_1295_call()
output = call_12166
output2 = call_12167
func_12170 = relay.Function([], output)
mod['func_12170'] = func_12170
mod = relay.transform.InferType()(mod)
mutated_mod['func_12170'] = func_12170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12170_call = mutated_mod.get_global_var('func_12170')
call_12171 = func_12170_call()
output = call_12171
func_12172 = relay.Function([], output)
mutated_mod['func_12172'] = func_12172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10527_call = mod.get_global_var('func_10527')
func_10528_call = mutated_mod.get_global_var('func_10528')
call_12264 = relay.TupleGetItem(func_10527_call(), 0)
call_12265 = relay.TupleGetItem(func_10528_call(), 0)
func_9328_call = mod.get_global_var('func_9328')
func_9329_call = mutated_mod.get_global_var('func_9329')
call_12287 = relay.TupleGetItem(func_9328_call(), 0)
call_12288 = relay.TupleGetItem(func_9329_call(), 0)
output = relay.Tuple([call_12264,call_12287,])
output2 = relay.Tuple([call_12265,call_12288,])
func_12296 = relay.Function([], output)
mod['func_12296'] = func_12296
mod = relay.transform.InferType()(mod)
output = func_12296()
func_12297 = relay.Function([], output)
mutated_mod['func_12297'] = func_12297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10319_call = mod.get_global_var('func_10319')
func_10320_call = mutated_mod.get_global_var('func_10320')
call_12311 = func_10319_call()
call_12312 = func_10319_call()
func_4045_call = mod.get_global_var('func_4045')
func_4047_call = mutated_mod.get_global_var('func_4047')
call_12326 = func_4045_call()
call_12327 = func_4045_call()
output = relay.Tuple([call_12311,call_12326,])
output2 = relay.Tuple([call_12312,call_12327,])
func_12336 = relay.Function([], output)
mod['func_12336'] = func_12336
mod = relay.transform.InferType()(mod)
mutated_mod['func_12336'] = func_12336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12336_call = mutated_mod.get_global_var('func_12336')
call_12337 = func_12336_call()
output = call_12337
func_12338 = relay.Function([], output)
mutated_mod['func_12338'] = func_12338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10942_call = mod.get_global_var('func_10942')
func_10944_call = mutated_mod.get_global_var('func_10944')
call_12349 = func_10942_call()
call_12350 = func_10942_call()
func_380_call = mod.get_global_var('func_380')
func_383_call = mutated_mod.get_global_var('func_383')
var_12354 = relay.var("var_12354", dtype = "float32", shape = ())#candidate|12354|()|var|float32
var_12355 = relay.var("var_12355", dtype = "float32", shape = (256,))#candidate|12355|(256,)|var|float32
call_12353 = relay.TupleGetItem(func_380_call(relay.reshape(var_12354.astype('float32'), []), relay.reshape(var_12355.astype('float32'), [8, 32]), ), 1)
call_12356 = relay.TupleGetItem(func_383_call(relay.reshape(var_12354.astype('float32'), []), relay.reshape(var_12355.astype('float32'), [8, 32]), ), 1)
output = relay.Tuple([call_12349,call_12353,var_12354,var_12355,])
output2 = relay.Tuple([call_12350,call_12356,var_12354,var_12355,])
func_12364 = relay.Function([var_12354,var_12355,], output)
mod['func_12364'] = func_12364
mod = relay.transform.InferType()(mod)
mutated_mod['func_12364'] = func_12364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12364_call = mutated_mod.get_global_var('func_12364')
var_12366 = relay.var("var_12366", dtype = "float32", shape = ())#candidate|12366|()|var|float32
var_12367 = relay.var("var_12367", dtype = "float32", shape = (256,))#candidate|12367|(256,)|var|float32
call_12365 = func_12364_call(var_12366,var_12367,)
output = call_12365
func_12368 = relay.Function([var_12366,var_12367,], output)
mutated_mod['func_12368'] = func_12368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5710_call = mod.get_global_var('func_5710')
func_5712_call = mutated_mod.get_global_var('func_5712')
call_12425 = relay.TupleGetItem(func_5710_call(), 0)
call_12426 = relay.TupleGetItem(func_5712_call(), 0)
func_4195_call = mod.get_global_var('func_4195')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_12427 = func_4195_call(relay.reshape(call_12425.astype('uint64'), [2, 16, 4]))
call_12428 = func_4195_call(relay.reshape(call_12425.astype('uint64'), [2, 16, 4]))
output = relay.Tuple([call_12425,call_12427,])
output2 = relay.Tuple([call_12426,call_12428,])
func_12450 = relay.Function([], output)
mod['func_12450'] = func_12450
mod = relay.transform.InferType()(mod)
output = func_12450()
func_12451 = relay.Function([], output)
mutated_mod['func_12451'] = func_12451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10139_call = mod.get_global_var('func_10139')
func_10141_call = mutated_mod.get_global_var('func_10141')
call_12486 = func_10139_call()
call_12487 = func_10139_call()
func_4045_call = mod.get_global_var('func_4045')
func_4047_call = mutated_mod.get_global_var('func_4047')
call_12491 = func_4045_call()
call_12492 = func_4045_call()
func_7731_call = mod.get_global_var('func_7731')
func_7733_call = mutated_mod.get_global_var('func_7733')
call_12503 = relay.TupleGetItem(func_7731_call(), 0)
call_12504 = relay.TupleGetItem(func_7733_call(), 0)
output = relay.Tuple([call_12486,call_12491,call_12503,])
output2 = relay.Tuple([call_12487,call_12492,call_12504,])
func_12505 = relay.Function([], output)
mod['func_12505'] = func_12505
mod = relay.transform.InferType()(mod)
mutated_mod['func_12505'] = func_12505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12505_call = mutated_mod.get_global_var('func_12505')
call_12506 = func_12505_call()
output = call_12506
func_12507 = relay.Function([], output)
mutated_mod['func_12507'] = func_12507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8335_call = mod.get_global_var('func_8335')
func_8336_call = mutated_mod.get_global_var('func_8336')
call_12528 = relay.TupleGetItem(func_8335_call(), 0)
call_12529 = relay.TupleGetItem(func_8336_call(), 0)
func_2733_call = mod.get_global_var('func_2733')
func_2734_call = mutated_mod.get_global_var('func_2734')
call_12542 = relay.TupleGetItem(func_2733_call(), 0)
call_12543 = relay.TupleGetItem(func_2734_call(), 0)
func_4806_call = mod.get_global_var('func_4806')
func_4807_call = mutated_mod.get_global_var('func_4807')
call_12548 = func_4806_call()
call_12549 = func_4806_call()
output = relay.Tuple([call_12528,call_12542,call_12548,])
output2 = relay.Tuple([call_12529,call_12543,call_12549,])
func_12550 = relay.Function([], output)
mod['func_12550'] = func_12550
mod = relay.transform.InferType()(mod)
mutated_mod['func_12550'] = func_12550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12550_call = mutated_mod.get_global_var('func_12550')
call_12551 = func_12550_call()
output = call_12551
func_12552 = relay.Function([], output)
mutated_mod['func_12552'] = func_12552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4959_call = mod.get_global_var('func_4959')
func_4960_call = mutated_mod.get_global_var('func_4960')
call_12558 = relay.TupleGetItem(func_4959_call(), 0)
call_12559 = relay.TupleGetItem(func_4960_call(), 0)
func_9486_call = mod.get_global_var('func_9486')
func_9488_call = mutated_mod.get_global_var('func_9488')
var_12561 = relay.var("var_12561", dtype = "int8", shape = (50, 6))#candidate|12561|(50, 6)|var|int8
call_12560 = func_9486_call(relay.reshape(var_12561.astype('int8'), [2, 10, 15]))
call_12562 = func_9486_call(relay.reshape(var_12561.astype('int8'), [2, 10, 15]))
func_2426_call = mod.get_global_var('func_2426')
func_2428_call = mutated_mod.get_global_var('func_2428')
var_12569 = relay.var("var_12569", dtype = "float64", shape = (2025,))#candidate|12569|(2025,)|var|float64
call_12568 = relay.TupleGetItem(func_2426_call(relay.reshape(var_12569.astype('float64'), [2025,])), 4)
call_12570 = relay.TupleGetItem(func_2428_call(relay.reshape(var_12569.astype('float64'), [2025,])), 4)
output = relay.Tuple([call_12558,call_12560,var_12561,call_12568,var_12569,])
output2 = relay.Tuple([call_12559,call_12562,var_12561,call_12570,var_12569,])
func_12571 = relay.Function([var_12561,var_12569,], output)
mod['func_12571'] = func_12571
mod = relay.transform.InferType()(mod)
mutated_mod['func_12571'] = func_12571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12571_call = mutated_mod.get_global_var('func_12571')
var_12573 = relay.var("var_12573", dtype = "int8", shape = (50, 6))#candidate|12573|(50, 6)|var|int8
var_12574 = relay.var("var_12574", dtype = "float64", shape = (2025,))#candidate|12574|(2025,)|var|float64
call_12572 = func_12571_call(var_12573,var_12574,)
output = call_12572
func_12575 = relay.Function([var_12573,var_12574,], output)
mutated_mod['func_12575'] = func_12575
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12616 = relay.var("var_12616", dtype = "float64", shape = (12, 12, 13))#candidate|12616|(12, 12, 13)|var|float64
uop_12617 = relay.rsqrt(var_12616.astype('float64')) # shape=(12, 12, 13)
output = uop_12617
output2 = uop_12617
func_12619 = relay.Function([var_12616,], output)
mod['func_12619'] = func_12619
mod = relay.transform.InferType()(mod)
mutated_mod['func_12619'] = func_12619
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12620 = relay.var("var_12620", dtype = "float64", shape = (12, 12, 13))#candidate|12620|(12, 12, 13)|var|float64
func_12619_call = mutated_mod.get_global_var('func_12619')
call_12621 = func_12619_call(var_12620)
output = call_12621
func_12622 = relay.Function([var_12620], output)
mutated_mod['func_12622'] = func_12622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7521_call = mod.get_global_var('func_7521')
func_7523_call = mutated_mod.get_global_var('func_7523')
call_12632 = relay.TupleGetItem(func_7521_call(), 1)
call_12633 = relay.TupleGetItem(func_7523_call(), 1)
output = relay.Tuple([call_12632,])
output2 = relay.Tuple([call_12633,])
func_12636 = relay.Function([], output)
mod['func_12636'] = func_12636
mod = relay.transform.InferType()(mod)
mutated_mod['func_12636'] = func_12636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12636_call = mutated_mod.get_global_var('func_12636')
call_12637 = func_12636_call()
output = call_12637
func_12638 = relay.Function([], output)
mutated_mod['func_12638'] = func_12638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12450_call = mod.get_global_var('func_12450')
func_12451_call = mutated_mod.get_global_var('func_12451')
call_12684 = relay.TupleGetItem(func_12450_call(), 0)
call_12685 = relay.TupleGetItem(func_12451_call(), 0)
output = relay.Tuple([call_12684,])
output2 = relay.Tuple([call_12685,])
func_12686 = relay.Function([], output)
mod['func_12686'] = func_12686
mod = relay.transform.InferType()(mod)
mutated_mod['func_12686'] = func_12686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12686_call = mutated_mod.get_global_var('func_12686')
call_12687 = func_12686_call()
output = call_12687
func_12688 = relay.Function([], output)
mutated_mod['func_12688'] = func_12688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6759_call = mod.get_global_var('func_6759')
func_6761_call = mutated_mod.get_global_var('func_6761')
call_12703 = func_6759_call()
call_12704 = func_6759_call()
func_5529_call = mod.get_global_var('func_5529')
func_5531_call = mutated_mod.get_global_var('func_5531')
const_12709 = relay.const([5.079558,2.082050,-5.734304,-6.402700,7.014766,2.470868,4.588105,-2.486286,-1.047012,-1.280390,-3.066041,8.042467,-2.592899,5.202661,-2.507254,4.452932,-7.227541,-3.627647,6.749265,-0.355406,-0.114533,-0.258363,-4.863965,3.327116,-6.035748,1.058242,-4.803115,1.788909,-8.607398,9.832394,9.471631,-3.188048,2.834777,-6.173143,4.891576,-2.485318,-8.042480,3.483162,5.973437,8.874296,-6.859113,-0.834761,1.576649,9.778303,-6.407191,-2.964381,1.496862,4.329188,3.353520,-1.655971,-0.477535,-2.386710,0.105787,-2.025408,-1.323958,-7.523288,-5.805463,-3.832787,5.453789,8.228050,-9.512662,2.521625,-1.981175,-6.671339,-9.375761,-8.987430,1.398441,0.932305,-1.891814,1.976493,7.090776,0.821342,-4.322702,5.105499,-7.175807,-9.551114,-5.179563,-9.754943,-3.194958,1.335083,0.006240,-2.536316,-0.912642,-9.797033,6.459280,-7.360165,2.326108,-4.672951,2.293319,3.490656,7.177812,-9.321631,1.883298,-4.171536,4.669726,-1.080186,-8.979895,-9.166912,-9.831585,0.594239,-6.218158,-9.614473,-4.587140,-9.121521,-9.132051,9.840910,2.993808,-4.192205,-2.283012,-4.415828,-4.301918,2.231354,7.437471,7.378385,-5.707177,0.154350,-5.914955,-9.657062,6.048852,-9.582803,5.356491,8.343391,6.010849,1.749085,-0.663493,-5.614923,4.748106,9.073371,4.243493,-6.992645,-9.659105,-9.408383,-2.349345,3.377599,7.720734,3.511952,7.834481,7.762845,-7.527840,-0.574115,4.571950,4.649578,-1.196510,0.082645,-3.898483,6.267505,-8.654143,4.277545,0.145279,-5.822942,0.676484,5.701507,-3.194178,8.020352,4.040493,4.285209,-3.097135,7.255330,-1.689972,-7.777720,2.987591,9.107049,-4.708918,-9.029904,7.260324,-6.152802,-4.616924,3.284705,7.350913,-3.280203,-2.887898,5.751774,-1.040756,-2.488069,4.877246,3.297691,-9.891673,-8.674789,-6.581151,-3.017426,0.213194,-0.882912,-5.028559,-0.873338,-3.637286,7.326547,7.137343,-3.211432,5.434790,-6.047320,4.713320,8.531494,-5.997943,-9.875077,-3.531010,-8.222296,-0.137773,-9.427123,-0.617369,-4.786298,0.021854,0.701922,-1.501402,-8.646145,-2.923673,-9.876873,0.963497,-8.620923,-9.454806,-4.796359,9.199733,-9.230025,9.432587,4.500025,-3.674260,-8.866838,8.286309,-9.049961,7.610558,2.582641,7.867752,-5.562999,-2.253300,-8.877397,3.489933,3.619011,4.141374,-6.023500,-5.760081,-7.922673,4.843057,-0.722381,-9.224574,-7.309486,-9.241002,-4.275969,-4.468481,-0.085781,7.147293,0.656907,7.337035,7.918969,-0.615516,5.197582,6.642874,9.108042,-4.998738,0.424168,-5.207731,2.716216,-9.924228,-2.382405,-3.791485,1.223377,8.877832,-4.182885,9.049541,9.555599,-4.503318,5.238078,-9.679857,-0.075429,-2.184762,-1.292167,-4.873745,6.089799,6.813256,9.374890,-1.950778,7.621935,4.486393,-5.167470,7.725209,-6.356710,-3.458786,-5.707341,2.334509,-9.931384,-9.029565,-5.348036,-0.580550,3.897929,-8.047589,1.721591,2.799674,-8.389763,-2.080841,-2.216948,8.433953,2.188347,-8.867280,-7.933387,7.392658,7.653302,1.844317,-6.650459,-6.233984,5.207918,-7.729989,4.627886,3.638075,-9.895813,3.290765,-9.472257,2.469754,-7.127594,9.505481,3.389903,2.512248,-3.614609,3.644652,-5.753822,5.725833,-5.290041,-7.374313,2.978718,1.402986,-4.080473,-7.937193,6.134792,-4.672503,7.848547,8.545560,-0.247297,-1.772566,5.878033,6.022105,8.385575,-1.783362,-1.071328,3.156033,-2.825584,5.100434,0.747328,4.899564,-6.895668,4.407713,6.790003,-0.115296,3.031810,7.937940,-8.197716,4.703695,6.529293,9.708618,-5.920888,4.101968,-0.673794,3.230466,7.605627,-1.066319,4.217186,4.494097,-7.472980,-2.740277,-9.843321,0.717886,8.725298,-8.216502,-9.731006,-4.616165,2.496727,3.098687,2.805312,1.769610,-4.154706,-6.063721,9.510648,-5.077873,8.797343,-8.161419,-8.271244,5.615826,-2.183089,-5.980743,9.857697,4.216696,5.177141,-1.424495,-7.264222,6.013686,-7.050593,-3.630055,5.548646,0.158157,4.916827,6.869998,1.546838,5.356202,-8.752085,-5.934005,9.300812,-4.535979,9.102601,6.658457,6.700665,-7.072791,-5.359676,3.900702,9.770099,-1.430650,-2.637583,1.751547,-5.777577,4.780789,-4.788702,1.252963,-3.051694,-6.296060,-7.759583,1.040520,-4.238301,8.818049,-7.276943,1.547885,-9.507952,-2.913473,0.374959,-2.848929,0.021235,-7.314059,-4.115526,5.823042,-3.809799,-0.745377,4.339653,-6.926609,3.230175,-1.097245,-1.391516,3.824626,0.334262,-9.462768,0.028178,8.210395,-6.451721,1.966129,2.543040,1.798860,-3.635187,-7.600951,1.169789,-8.478907,8.128812,-8.277924,-1.508903,-1.028179,-0.681828,-2.029602,5.717467,-6.071344,2.632880,-9.431967,-6.915511,-6.808394,5.024801,-7.156611,6.054323,2.375547,3.866814,1.687383,-0.621097,8.558116,-9.301143,-4.830757,3.675519,4.900589,-4.496262,2.652712,-0.097642,-9.379570,6.665166,-3.360965,5.216032,5.237903,-0.188542,-5.242755,-3.956521,1.477280,2.331231,-1.289861,-0.276237,8.516951,-8.293684,4.012747,3.009217,-7.997237,-2.141495,9.191084,0.751821,-2.839031,2.497996,-0.576284,-3.492598,-3.037666,0.527240,5.311011,1.029278,5.583959,6.420924,-5.519235,-9.617448,9.047366,5.977162,-6.614646,3.188982,-4.092614,7.541216,-8.588513,-2.049112,5.542398,-5.467326,4.654229,4.948522,6.391827,8.963349,0.004591,-3.000412,-5.755273,-3.544442,-0.738214,7.471842,-1.368369,4.226226,8.700064,-5.755888,-3.675402,5.930059,-4.445959,-0.565089,7.622899,6.159408,4.060261,-6.142016,8.732873,-7.580592,-1.259934,9.770052,-5.294751,-2.243159,-0.219603,-7.089514,0.653204,5.123312,-1.011429,1.108067,5.689404,3.089376,-3.796050,5.188551,-2.392660,-6.644296,8.705485,3.738363,-4.053263,6.663068,-6.589631,1.311987,2.158455,9.136679,-5.774785,-2.862031,6.958692,-8.462484,0.012359,-0.434087,1.227557,-2.397584,-4.735713,-7.910149,3.240524,0.136116,3.599220,3.604960,6.316993,5.798546,4.045536,-4.613361,8.275841,4.490227,-9.562399,-1.601729,-5.760854,-5.636439,-6.651203,2.741519,5.867755,-6.082207,-2.692179,2.896810,-1.536889,5.947147,-7.821547,6.587658,4.453445,-9.825946,-0.898731,3.001969,-7.676234,6.847146,3.222742,-2.626955,4.779290,6.581919,8.824510,-1.741562,9.690853,6.152233,2.681104,8.387338,7.451623,-0.163422,-4.575856,-4.403648,7.302304,-8.589970,7.675995,1.620834,1.710940,-5.182054,-6.316763,-9.112778,-9.669911,6.632780,-2.146001,-1.366546,1.129534,9.317577,9.333007,-2.661985,5.986761,2.015409,2.322708,-5.833223,2.085534,2.148653,7.974186,-8.748311,-9.201880,3.489231,-7.821029,-3.843768,-6.622972,-7.436622,-7.486018,-2.138904,6.021141,-1.724513,1.954430,7.042300,1.469296,-2.275224,-9.749796,-0.372230,-5.148306,-9.329888,-2.976656,-6.993162,-0.273974,-0.849940,0.699010,3.168611,-3.269499,-9.122843,-6.198328,-4.855664,-9.954993,-0.555406,1.438339,1.183271,-6.221542,3.051412,4.719691,4.908457,-8.470185,-2.941953,-5.690734,-5.119090,5.417089,-8.977304,-3.741909,5.968743,5.536755,2.266619,-6.658368,6.058210,-6.921727,4.983190,-0.717023,-6.234731,-7.879406,9.376491,-4.080774,0.982653,-3.204200,4.943519,4.839527,6.925513,-8.342697,0.952824,-1.589816,4.190619,3.171380,-8.724607,6.080832,-5.119183,2.118530,-4.251629,6.386332,7.248039,-0.955197,-3.191514,9.238310,-7.636723,9.598459,-1.716223,-8.848709,-7.033640,3.550774,-6.925840,5.381461,-2.271501,-0.887193,-5.367963,3.209305,7.653223,-8.881043,8.157220,9.630812,2.795479,9.719155,-7.622933,8.495155,-4.740971,5.130391,5.349162,9.048074,7.327242,0.670068,-9.324180,1.335699,-8.477047,6.509890,4.837381,9.507348,5.698177,5.686721,5.748392,7.307265,9.770388,-2.242942,9.278830,-4.049672,3.864992,8.896989,-1.398635,3.071169,-9.100553,-2.618661,1.560826,0.059953,4.768600,6.936845,1.167518,-0.972267,3.616987,-5.404311,-5.009479,-2.903374,-3.826010,6.154938,-8.332434,4.831064,-7.146938,6.845929,3.828609,-5.600286,8.690356,5.536634,-4.989155,8.257183,-4.362661,7.503948,-7.192403,-3.079143,5.882702,-4.083138,-0.833876,-3.454744,2.129376,8.551783,-7.793318,0.149457,1.110640,3.586834,-8.169494,8.221667,-2.218228,-3.331353,-6.086318,1.619707,-5.526759,-4.600149,5.917822,2.586738,-3.549416,8.017483,3.384413,-3.864926,-8.154197,-4.318046,-2.108430,6.279896,-2.461650,5.157178,0.744948,-0.543046,-1.843377,-8.804367,-1.839103,0.198402,-6.303119,2.384358,1.927563,-5.030999,4.879608,7.856966,5.069678,-0.794223,-7.551072,-0.522351,-8.648495,4.543833,9.636430,-5.344527,-8.318597,-7.382878,4.772705,-9.033751,3.212455,-0.513922,6.000036,-5.669469,-4.830195,8.316998,0.704720,-1.906608,-2.026230,-8.385769,-4.289638,6.548602,-5.146566,5.997085,-6.714138,2.230514,1.086102,-7.213431,5.330185,0.440746,-0.523845,-0.148645,-5.188065,6.857520,-2.937815,7.999964,0.422846,5.698237,-0.475229,8.988150,-4.084594,5.154143,-1.254993,8.303274,-9.317097,2.495817,8.532775,-3.474278,8.595718,-0.599866,-1.227117,-5.030881,0.156982,1.895981,-5.677047,-2.311516,5.502277,-0.153096,7.470840,3.419071,-8.685454,-2.417223,-6.018234,-4.315112,4.431147,-6.221922,-5.459619,5.361682,-5.502516,8.523096,7.234540,-8.137063,4.124659,-0.882381,-2.500618,2.652115,-0.515734,-3.903809,-1.912702,-2.591885,5.416734,3.710239,8.425970,9.184639,-7.568677,9.166866,-3.611731,-8.585092,-9.168508,3.045936,6.662297,-4.951749,-5.234792,-1.904244,3.754879,-3.898605,2.310685,-0.577720,-6.887481,6.048345,-7.968205,-3.972073,-5.135661,0.469620,8.097714,2.794326,9.516740,0.331885,-6.082011,-8.100069,-9.311470,-2.359177,2.291218,3.183423,0.655110,-7.339794,2.655872,-2.608353,0.499763,-5.370098,-2.771343,8.605112,0.493433,-7.953509,6.089752,1.305924,3.949382,7.320192,-4.006292,9.679661,0.582412,-0.349964,-8.076906,-9.210170,-8.218011,8.797631,-4.610710,-3.467456,0.592680,3.471173,5.539898,-1.535932,0.069537,0.800948,-0.224295,6.568718,-3.168811,-2.048197,-8.166443,7.266114,-1.468964,-9.655347,1.381552,-3.433341,9.411426,1.205359,2.693873,1.984479,-5.238539,-1.049581,7.140534,-4.187633,4.771310,2.124134,-9.802080,-5.310489,2.164899,2.756413,3.670046,6.790685,-9.862359,-2.662141,-2.542856,-2.290211,-7.787513,-7.793253,-7.150060,-5.512247,1.642264,1.139033,-0.299972,-8.480605,-8.234037,-0.074335,-9.866145,-1.815242,0.925309,-5.860602,8.160217,-2.949608,6.387064,1.495538,5.128413,-6.951857,9.919642,-5.185877,2.976212,7.912971,7.382505,-2.974021,7.906682,-0.926220,3.707605,2.672692,2.593433,-6.701842,-0.042852,-0.717973,1.072431,-0.717133,-3.780240,-9.190844,-2.106907,-3.344562,-7.114618,0.114321,9.798894,-7.084923,-9.057695,8.957908,1.533902,-9.776130,-8.357155,3.119729,7.744226,-2.801215,1.834221,-2.262943,6.117052,5.597678,2.999621,1.008376,-0.547537,7.445814,6.928515,-6.496549,-3.750926,-2.681782,0.643918,0.590220,-7.845362,-2.540087,-7.937775,1.652900,9.363473,1.214269,6.140119,-7.710107,-9.392943,-7.172471,-9.400025,-4.148271,9.397806,5.404229,1.697776,-6.960391,3.583132,5.870685,9.215931,1.304459,5.654779,1.609805,0.709849,-5.318077,3.870459,-6.321337,0.424749,-1.693569,2.959873,4.163467,-0.401379,-3.780718,-9.399714,-5.839923,-9.090840,9.140990,-9.769043,-1.225252,-9.600040,-5.174295,7.216161,8.290633,6.437797,-9.077450,-1.574154,2.135385,6.254014,-6.027198,3.713478,1.187854,-6.630841,4.286098,4.356269,-5.874656,-7.470501,1.096378,2.700066,-7.484537,-2.099659,-6.208229,-1.221822,-4.077959,7.643274,-7.296504,2.909374,8.274504,-7.858058,-1.983849,-5.311170,1.293557,6.384661,8.953985,4.696738,-1.834092,-8.223405,-3.666594,-4.189294,-8.534576,7.902975,4.511948,-7.404049,-0.716728,4.600664,-0.506065,-7.808075,2.484490,-6.404881,-1.760238,-2.323336,5.025004,3.198191,-3.872471,-6.569479,-1.184774,9.151756,-4.046539,-2.712354,-6.542144,-7.965877,5.931827,-5.903333,-0.905930,2.192764,-7.295199,3.620648,-2.092644,-4.552549,5.071495,9.355600,-2.480320,4.236912,-4.373081,-7.338031,7.298442,7.458678,2.762969,4.257920,-7.902964,-1.875860,9.523523,8.092880,0.232985,-5.608568,-8.602704,-8.312053,-3.776324,-5.458014,3.134756,1.141384,8.692127,7.539249,-9.556045,-6.142281,-3.233910,2.500769,0.399952,7.152135,-5.500722,2.859207,-6.785462,-9.709667,6.128629,0.308617,3.790951,2.168173,-4.513122,6.701408,-2.259822,5.527817,-6.192654,-7.683777,1.706259,-2.188226,0.292881,8.818194,0.573615,-1.276598,-3.058025,9.566656,-4.063608,-2.921919,-9.631936,4.208288,9.646438,9.332526,1.454330,9.559720,2.599876,1.633601,1.154765,-5.917529,-6.907353,8.596287,9.689951,-6.091757,-9.945110,-4.547291,-4.405508,2.512133,-2.510517,7.899897,-4.733647,2.016332,1.514411,-4.852958,8.185003,9.147693,8.940093,-2.938090,-4.025853,-8.872142,7.375673,3.854498,-3.057229,3.989417,8.262672,-6.147632,-2.742308,9.288447,-0.682183,-1.433995,7.876987,0.800489,7.710078,1.672725,-7.131433,-3.876614,-6.419562,9.976118,-0.506234,1.249456,-6.653652,4.588511,1.025370,-6.108651,-2.193485,9.731335,-5.403424,-6.351641,-4.723309,3.781037,2.792561,-9.538078,8.953157,-1.047046,9.164663,5.130700,6.901167,-3.328224,-0.260660,1.378204,1.625456,-8.720637,1.443743,0.166881,-7.017817,1.687029,-5.573976,0.579913,1.374653,4.849384,3.121065,-1.529651,9.275412,-3.536660,1.391665,-8.236310,-4.858105,2.158576,3.569262,-4.392931], dtype = "float32")#candidate|12709|(1320,)|const|float32
call_12708 = relay.TupleGetItem(func_5529_call(relay.reshape(const_12709.astype('float32'), [6, 220])), 0)
call_12710 = relay.TupleGetItem(func_5531_call(relay.reshape(const_12709.astype('float32'), [6, 220])), 0)
output = relay.Tuple([call_12703,call_12708,const_12709,])
output2 = relay.Tuple([call_12704,call_12710,const_12709,])
func_12715 = relay.Function([], output)
mod['func_12715'] = func_12715
mod = relay.transform.InferType()(mod)
mutated_mod['func_12715'] = func_12715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12715_call = mutated_mod.get_global_var('func_12715')
call_12716 = func_12715_call()
output = call_12716
func_12717 = relay.Function([], output)
mutated_mod['func_12717'] = func_12717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6199_call = mod.get_global_var('func_6199')
func_6201_call = mutated_mod.get_global_var('func_6201')
call_12726 = relay.TupleGetItem(func_6199_call(), 1)
call_12727 = relay.TupleGetItem(func_6201_call(), 1)
func_1639_call = mod.get_global_var('func_1639')
func_1642_call = mutated_mod.get_global_var('func_1642')
const_12740 = relay.const([-8.461733,9.300232,-4.929731,2.823584,-7.451615,7.640887,3.174189,-1.888811,-5.617241,7.539087,6.966184,9.266464,1.518924,2.802770,-3.764733,-9.430644,-5.291040,8.958514,-6.106698,1.395060,-1.436142,7.229886,7.951302,5.430712,-4.629691,0.404788,2.992616,-2.199843,-8.418853,6.531205,-0.184883,7.795901,8.353946,4.089943,-0.876240,-5.765066,-6.279586,-0.821308,-8.387008,3.212676,5.156284,-5.652050,3.302130,8.764899,-3.148991,4.972687,5.120380,9.482264,9.444958,-6.703274,2.907144,-4.518188,-6.123596,8.916190,-0.550064,0.479724,-7.743579,-8.146177,1.987796,2.205714,0.132419,-2.298421,3.531155,2.664102,1.218059,-2.909088,4.951337,-2.101965,-4.176446,-2.289126,-6.894239,-9.183101,6.361928,-9.946891,-7.256883,-0.925553,-0.279115,-6.442163,6.614381,7.018306,-7.166282,0.441005,-6.588313,4.388338,-2.320240,-6.190718,-9.020084,2.158305,5.320219,-0.238769,2.038210,2.460590,4.961617,3.338957,-4.220720,2.723145,0.499488,-2.450869,-0.457840,-5.846419,9.571686,5.899311,3.736425,4.493322,0.386800,-3.528510,-2.680962,-6.912750,-4.616170,-2.918468,-4.749968,1.412324,0.877633,-2.760737,0.792996,-7.245525,9.808352,-7.039663,-0.258836,7.177134,2.655951,-9.430912,-6.710690,-4.430142,-7.247328,8.649897,-7.336994,-8.820543,-2.279461,-4.447239,6.866313,-0.996963,-0.802052,2.927107,-3.640135,-5.820099,8.256558,1.241273,-3.417859,-7.728004,8.142873,6.587394,-3.750592,6.391488,-9.700339,-2.052002,-2.472974,-2.142615,-2.537769,6.255227,3.603517,-0.627171,-0.651971,-0.851798,1.838761,2.649530,-3.863904,3.962506,0.236224,5.627722,-1.396992,5.158977,-7.988731,3.355386,-2.082631,0.171624,7.712213,-5.501376,9.385477,-6.129585,0.091516,5.962241,-2.757604,-3.589288,6.316564,-2.791153,5.564799,-9.894088,8.138054,-0.975702,-1.108032,3.081106,-9.830956,8.982266,-9.457939,-4.917337,-6.553716,3.741285,-1.838421,-4.454198,0.272616,3.595355,-9.138213,-5.453633,-0.634959,3.081202,-9.932709,-0.089030,-2.001530,9.898444,2.542352,-5.815903,9.926516,-0.038497,4.373640,-8.160930,2.503719,-0.243069,4.820632,-1.801177,5.588532,4.560642,-2.721425,-4.193117,2.649174,-3.907724,-9.300373,-6.413586,-0.709849,4.793720,3.972528,1.872792,-3.445913,9.685450,-3.668139,9.941709,4.143209,-2.947524,-0.207867,6.036956,-4.257284,-7.812009,-7.138102,-0.973494,0.520068,5.619071,2.344903,-9.360764,-1.851084,-2.002508,4.396686,-9.812272,-6.359360,-2.099020,-8.332950,-6.951062,5.813198,0.364304,-5.147378,9.591444,8.309436,-2.128846,9.821034,-7.007935,-5.179109,-6.244600,-2.249853,8.332667,4.891564,5.355107,1.846224,-3.972810,-7.662887,-1.135657,-6.881126,0.634900,-5.103168,-6.555685,-3.173170,1.079042,8.686625,-4.090644,4.261353,-7.626197,3.035016,-7.603432,-5.845326,-4.356715,-8.495825,0.444043,-4.003192,-5.353887,-5.391522,-5.099306,-0.139505,-1.324661,1.754175,7.338790,-8.401876,-4.135130,-8.963914,-0.901450,9.702535,1.627892,5.338913,-9.759767,9.631736,9.130074,-1.711881,-8.762808,1.799245,-9.696419,2.283649,8.460030,-2.037712,-1.727747,-1.141317,8.076026,5.437699,6.995958,1.861090,-7.655111,6.423350,-5.163318,5.731079,-4.667989,6.030195,2.570791,-2.919047,-6.550918,-6.512830,2.415306,1.933731,8.749880,-9.439066,-4.922184,-5.355241,-0.200828,-6.901612,7.578506,-4.370299,-7.426357,3.566672,-7.686298,2.656860,-7.660603,3.248249,-3.635432,-3.199786,0.564604,7.994435,-4.664352,-9.500445,5.683601,8.005373,-7.030006,-7.171351,-5.039967,1.426251,9.365248,3.222644,-1.298168,-0.605369,-6.270901,-5.114514,3.407366,3.440677,-4.997046,-4.774053,-1.289389,-9.536405,6.198182,8.521011,-0.948907,1.380234,2.710543,7.229001,2.729467,5.406807,-1.331078,-8.097943,0.853514,6.109999,7.470094,7.849064,-5.048961,8.055684,-2.801993,1.663676,2.239732,-8.455137,3.257976,-2.676637,2.362301,-1.302585,-8.310004,6.153421,-0.215935,2.257503,5.172411,2.809031,-7.102933,7.270094,-1.367573,-0.295032,0.060011,-8.825967,-1.795300,-6.254802,-6.965914,-3.521775,7.958628,-4.224054,-3.949044,6.989825,-5.911237,4.454567,7.138626,5.405926,8.934112,5.189226,2.593057,-3.478465,9.900990,5.000431,4.194984,-0.975705,-5.769771,6.073574,-3.924047,-5.600438,5.668034,6.474107,-2.388602,-1.008679,-3.246474,7.950389,-6.193306,-5.019276,-2.454826,2.715741,3.058590,-8.892756,4.101716,-5.066482,-8.021934,-8.419510,8.712263,7.795786,6.033463,4.672815,6.003049,1.329571,-6.528586,6.696350,0.018074,8.689597,-8.719182,-3.673040,5.736844,0.457693,6.698287,6.469499,-9.862438,7.071623,1.466073,3.343154,1.639709,-4.237052,-0.220434,-9.921091,-1.590419,-5.057130,8.600717,-8.027946,-5.888889,-3.205261,-4.600496,-0.054577,-5.175928,-6.718043,-0.864274,1.424599,-9.460712,-5.041721,6.893859,-8.157043,-9.135458,6.516038,-3.487846,-2.729136,7.436472,-7.473049,-4.716464,-5.156627,-0.686630,-1.448344,2.429177,-6.325110,2.413753,-7.139381,7.640027,8.938826,-2.653503,1.332764,-0.829197,4.117123,4.950780,5.429333,-9.647450,-4.529948,-0.052139,5.119525,-2.803445,2.442321,-7.731748,5.515616,3.193605,1.985768,8.027743,-6.858343,-1.066933,4.785462,1.860943,-6.591391,9.353110,7.919554,1.490109,2.051519,-8.119075,-5.581663,-0.820919,3.396732,-5.105538,8.542874,2.147946,8.581786,6.184890,4.232277,-2.768071,-7.090793,4.076957,6.429735,2.923170,-6.669679,-6.477357,-3.899396,-3.790657,-7.832582,8.001960,-6.960867,8.030629,-3.598310,7.486713,5.498951,4.624219,0.660210,9.976553,-0.619692,4.229045,7.532059,0.410498,-1.287013,7.569360,-5.044139,2.216096,0.325422,-3.850518,0.837286,-1.719031,6.546847,7.315607,-1.646945,-2.519317,8.284350,7.319123,9.201885,-0.336809,0.303086,-9.823317,-0.269408,-7.210784,-1.241519,-9.762375,-8.288859,-9.353366,-7.873868,-0.447025,6.657193,8.415489,-4.393337,0.767089,9.354426,-5.501186,4.007011,-8.685489,-9.896837,8.658665,-1.745865,-9.784887,-3.873552,-0.797245,-0.199547,0.515979,9.020281,-1.042839,-5.139453,6.642107,-9.632455,-2.749818,-2.854044,2.589518,9.124940,6.528381,-2.428854,2.039835,8.181260,-3.628906,-5.319317,3.815826,-9.905407,-0.741450,3.957422,5.681024,1.574800,3.242007,-4.409828,-7.156997,1.377149,9.784652,2.023559,6.192730,8.725570,7.016924,9.978541,0.012421,-8.154866,-2.652655,-1.426150,5.674519,5.009999,3.631291,-1.287216,-3.845726,-0.925956,7.706699,-8.765551,-1.706320,-5.817898,9.940924,-6.177582,-8.251750,-3.157117,-9.823826,-2.129824,-9.136204,-9.474593,2.372006,3.928142,-8.545900,-9.838292,-7.043575,-1.850547,-3.247194,-1.246875,7.854681,-3.643784,8.987618,-9.552778,1.628628,-7.974219,6.899716,-4.848667,9.010852,-2.611846,4.246389,3.004361,4.925483,-3.390987,4.092236,4.714417,9.363157,-1.412719,2.897581,-5.836186,2.998190,-8.633936,9.544535,7.703430,2.552097,-7.509710,-9.815467,-9.696748,-7.855009,4.731490,9.301564,-4.208139,1.571619,3.896090,6.581061,8.653577,-1.960486,1.466166,-6.334950,-1.908256,-1.081436,-3.145836,8.546967,-9.649483,7.172738,1.877927,6.932953,6.377344,-3.792332,6.768404,-3.479744,-8.776212,-5.226220,-3.495136,-9.873048,-6.730623,-7.829334,-9.763441,1.311599,8.613741,-1.621180,8.635204,-2.240896,-6.288554,-4.529586,-1.287675,8.589408,8.562494,6.825746,-7.511893,3.042831,-7.643084,-3.320898,4.369927,-7.973513,-1.423403,5.532517,-8.907058,7.681801,-6.157781,-6.334882,-5.870610,5.567020,0.776795,-8.011531,-6.220639,8.389632,7.984223,9.426582,2.470558,3.721782,9.618898,-3.581080,-0.705958,-5.496437,6.417756,5.919883,-6.875931,6.975773,9.871811,-5.864660,7.016067,6.239020,4.512875,5.950285,-0.736921,-0.582098,3.145277,1.463941,-7.935673,-6.908056,-0.600944,-2.310921,-2.995985,-6.311865,3.826458,-9.317445,-5.048593,6.290026,-0.430343,2.917287,0.352236,-1.464276,-7.195007,-8.736146,-3.751177,-7.783471,-8.627748,6.986763,-9.804811,9.666289,-7.290876,3.489882,2.688642,-5.719817,7.752627,-1.392265,-6.531454,-6.506351,-4.856187,3.397791,9.499685,1.371165,-2.303492,9.924410,-0.130457,-8.862727,-3.769071,-0.238555,-2.365563,3.917833,-2.559014,-7.226811,8.684850,9.802589,4.839362,-5.949222,-5.922170,1.032252,-6.573855,1.818552,1.382284,-7.528665,9.390588,3.843867,7.962798,-0.423925,-9.118260,-3.067409,1.984931,7.350382,2.850711,4.955821,1.416555,-4.079379,4.150534,-8.528437,-9.383875,-1.341593,9.905437,8.749850,4.396209,-0.542717,8.597074,1.679862,-6.962470,6.246201,-6.244530,3.063348,7.314674,5.110787,-4.550734,9.854047,-6.503271,-0.077916,9.685775,3.148734,0.657133,-6.692530,-5.740997,0.620628,-8.780576,-4.212540,-2.383378,-5.045020,-3.486761,-6.998402,-3.450103,2.094807,-0.148467,-9.257737,8.187405,-6.170545,-6.914500,4.646081,-2.802374,8.037512,-4.956339,3.355785,-0.969748,-4.972581,1.082561,4.374722,6.327603,2.815408,-3.925086,2.997204,6.879394,2.587598,4.370667,-0.977183,2.022412,-9.407351,-4.995057,-6.711604,-9.171896,7.920559,-2.426231,9.517796,9.527057,6.583796,-9.066202,1.092949,-4.631271,1.053040,-9.377577,5.440660,-0.558824,5.822751,3.980762,7.017043,-2.189970,9.923450,4.992372,-6.787247,0.438898,-8.956399,4.162567,4.494821,-4.485021,9.959589,8.691454,4.824140,-7.604404,-4.999127,-7.847026,1.217364,-2.187867,3.100170,6.013731,-7.640408,6.138760,8.852687,-7.639859,-4.534788,6.761582,2.109083,-2.058406,-2.855986,8.197996,-3.577253,-7.164252,3.794755,9.008018,-9.458019,-2.653398,8.412199,-5.816856,-5.764027,-6.784481,7.406924,-6.416651,-8.940598,1.765020,-1.753828,6.377323,8.242654,-0.543492,-6.459487,8.631299,7.195399,7.683821,-5.411265,9.764759,-8.731112,2.548477,5.770144,4.792388,2.695679,7.540315,3.048109,-9.362642,-6.678390,4.863355,-5.682506,-3.667293,6.840141,0.293068,8.488275,-4.833739,-7.394608,9.931821,-7.191415,6.126317,-5.416498,3.450755,9.631516,-7.696169,-6.100922,-5.660064,-2.168522,-0.982896,-4.070054,0.101041,-1.716293,5.452734,-6.196204,5.873164,9.808243,-6.648470,7.674248,-9.702899,5.212736,-1.991487,-7.342403,0.534934,3.169957,-9.209749,1.346133,9.411779,-4.685041,-2.696801,-2.712923,8.932006,-7.220980,8.425199,1.720551,-1.531772,-0.557020,-6.472651,8.674336,7.034106,-3.679582,-0.014722,-6.045267,3.079568,-9.119886,9.632716,7.129638,9.096027,-0.635466,1.681427,-4.655946,-1.683655,1.089027,2.529706,-2.382455,7.954755,6.809494,-7.064626,-2.365080,-9.094503,1.098527,5.522442,-1.202722,-4.040296,1.884216,-3.545847,3.565975,-7.725552,6.049594,3.370561,-3.549522,-8.963394,-8.987771,4.759003,1.976086,-0.377519,9.681632,0.305394,-0.574281,-9.366080,-5.982057,5.459258,-1.263217,-6.286124,7.497881,5.701723,-5.943354,4.632224,9.777603,4.202831,-8.962215,0.057164,3.599956,8.296210,6.769950,4.035902,-9.096060,8.637692,-5.408196,9.765175,-6.462824,-8.221173,-0.018951,7.046262,-5.802079,-5.738695,-3.387777,7.552849,5.334624,3.708014,-1.217148,-3.771885,7.909891,1.107001,3.664877,-8.951950,-9.612742,-8.217433,-9.250321,-2.049481,0.683616,-0.236731,-4.137305,3.634008,-0.325627,-5.144981,-5.177880,-0.289329,6.605950,0.629951,-5.992785,-6.019134,-8.475585,2.006084,-2.403434,-0.665478,5.940024,-0.217503,-1.519949,1.187678,-8.692847,7.564545,-5.386942,3.879231,-2.731053,-7.013871,-9.762784,4.467874,6.936695,0.117084,-8.514891,5.878165,-8.215756,8.474990,-7.639972,-4.494784,7.324218,8.915249,9.349117,5.664468,0.780605,-9.495992,-8.239966,7.962867,-6.623149,2.458163,-7.390260,-7.887535,-7.630728,2.434634,-8.840530,-6.336334,1.173728,8.374449,-8.293632,-7.058616,-7.297644,2.244664,-6.324310,7.205689,0.097899,0.840927,0.768405,6.099736,-4.102134,-2.946834,-4.232824,-3.769807,-9.664523,-1.041513,-8.054144,7.361626,1.674159,8.128125,7.009121,-7.730519,0.179366,-1.595726,-4.049096,0.714367,-0.073878,0.956517,-6.398102,-5.683256,-4.039694,3.723812,-2.683959,7.169149,7.722080,7.403601,4.973425,8.013312,-6.879426,-0.770903,1.501755,9.914497,6.628857,-0.781393,-7.054526,8.358244,7.020659,6.225027,3.393155,6.373624,5.323387,0.555788,9.063344,6.842079,-4.249450,-9.417189,7.297664,5.160563,-2.927024,-1.584489,-6.376807,0.185196,-9.420878,7.608050,-7.777106,-4.142183,-9.713681,-8.643174,6.911746,9.692164,2.808394,3.792464,4.701954,-5.299280,2.994884,-0.031671,-4.997093,3.375028,-2.273873,-3.202964,-2.699459,-6.173621,-4.881289,-6.516001,-8.842782,4.563538,5.867190,2.913809,5.271370,-5.264230,-9.379514,-4.777786,0.084883,-4.522306,4.359315,-4.921976,3.584768,-4.741260,1.002371,7.347264,-0.991263,-1.822110,-7.875306,-8.753063,5.927934,-8.494602,4.943990,-6.548134,-2.880493,-3.503356,9.393041,5.129756,9.996184,-6.809690,-8.371793,-3.202636,-6.946687,-0.232324,-9.641508,-6.768761,-7.970958,-0.228445,5.195736,-9.397021,5.875542,5.491158,9.334828,4.721386,-6.408011,6.315357,-4.243019,6.540181,-6.241352,8.628597,-2.449207,-8.181041,-4.608049,-8.334766,6.249965,2.232396,1.300453,1.439051,-5.380512,1.746913,-0.930864,2.990897,0.007378,9.421338,5.725074,-6.143753,-9.723126,-2.179742,0.108271,3.245153,1.155411,4.104789,7.712317,5.225414,-6.998595,1.279241,7.174141,8.519732,7.239745,9.640531,4.054686,8.297767,-4.072137,-1.929932,-1.402394,1.489886,-1.713538,6.342251,1.154680,0.309990,5.861168,1.482737,-1.166063,9.513472,3.617825,-2.648642,1.975206,7.535524,8.947232,2.244569,2.008133,2.317948,-6.761641,3.918609,8.206075,8.401946,9.836902,8.184508,0.777755,-8.280306,0.370589,0.107994,-1.202316,6.577812,-1.323646,7.472137,0.423677,0.918265,1.761050,5.970863,-0.442178,-9.228864,6.805158,1.128318,-2.291956,-8.591979,-1.992095,-3.189178,-3.738760,-1.993665,8.058117,-3.150297,-9.527349,-0.576515,-0.156426,-8.013217,-7.150841,4.022864,-7.988101,-4.241742,-2.210188,8.703939,-4.978404,1.606053,2.855932,8.180754,8.227765,3.216036,6.544351,-3.803729,8.851439,-5.502242,2.707618,-5.083624,-8.148618,-1.478663,5.189173,3.060315,-6.737912,-0.623170,-6.935112,-0.946704,0.856839,6.585201,1.220662,-2.165525,-9.513252,-4.815971,-1.713579,-1.955795,1.898036,8.547826,-4.116488,-1.449448,2.699950,-6.413264,-5.810336,-7.931010,-9.184885,-7.061938,6.769854,-9.473923,-5.399958,1.244342,8.329979,6.616625,-0.109437,2.269869,-3.220563,9.573826,-2.824633,0.616756,-5.449382,-1.643660,-3.645947,-9.798426,-5.404712,7.812836,8.975834,7.335714,-5.607781,3.780675,-2.521548,4.546205,-1.800457,-3.481426,-2.308875,9.754093,3.550950,2.027046,6.743964,3.153158,6.623433,-8.604061,7.714132,1.469604,-3.196337,2.019901,-9.967941,5.382210,9.612799,1.506610,-6.478251,3.004875,1.026147,9.727295,-8.582359,-1.184237,8.738038,7.057643,-5.197678,3.170962,1.907991,5.271179,5.810598,5.593701,1.588513,2.263878,9.793777,8.680624,1.595830,4.239680,-7.244634,6.168841,-9.019371,-8.059577,-4.643709,-6.994570,-9.844532,5.341059,-6.035178,2.079053,7.303602,1.461033,1.432856,8.999345,3.534542,-3.315574,-7.441510,-3.851732,-2.948721,-4.602546,-8.779808,9.116811,-9.004741,-8.590108,0.319817,-0.297854,-9.250961,3.935159,3.328393,1.489688,-8.831029,-3.634507,9.950860,8.240586,3.183297,-8.197909,-9.493391,0.430694,-6.830775,-0.100016,4.486085,2.605598,-7.085630,8.418226,7.649465,3.736715,-5.540019,9.118410,-3.303972,-2.062222,-2.748997,9.775475,-2.366420,1.690208,-0.642677,-3.264131,8.745589,-8.510713,-2.056000,8.648631,-6.208475,5.467590,-5.194332,-8.246436,-0.855869,-2.197933,-9.698247,4.914747,-5.613229,7.908782,-3.854056,-9.850909,2.196124,-5.380126,-4.501721,-5.321541,-4.752422,-6.107346,-4.608939,5.676906,4.814574,0.179987,8.861334,-3.715951,9.091918,-0.688388,4.345263,4.420413,9.780150,-8.778525,2.284453,-7.557476,4.509212,-0.545004,-0.847486,-8.700831,-4.715891,9.300186,-4.029913,4.195324,7.354324,-1.298456,1.640958,-4.144073,5.838615,-3.929616,1.228654,-3.589580,7.028844,-3.565833,-2.118149,0.896173,-4.870290,-5.644790,-0.608719,-7.601261,7.720570,-3.498811,2.838944,-1.565500,-4.071359,6.969117,1.886090,-2.857418,4.118573,-6.908111,1.349692,-8.583683,-2.302438,-5.266512,-4.106483,4.876350,9.372350,-4.613302,-6.855813,5.746685,-1.726421,-6.955039,-4.649385,-8.995495,1.193318,9.149334,6.453567,-5.905651,-4.587990,-7.207819,3.314880,9.295845,-8.032375,7.386756,-3.400968,1.931574,-3.114414,-5.199081,-8.695102,-7.190625,-2.242704,-0.401130,1.937491,6.409458,0.019426,-7.809466,3.162572,-6.091112,-6.430848,-8.560800,-9.798308,2.451323,4.895110,-7.274588,-9.519854,4.561818,-8.388484,-6.071830,-4.370581,-9.956668,-4.266871,2.735728,-1.102088,7.103826,2.124245,6.988916,1.675400,-7.874677,-9.203086,-1.642551,1.185302,2.712841,9.962222,9.132418,-6.825105,0.257523,5.047611,-8.193835,-7.497053,-3.458192,-2.082258,-8.932443,-4.907594,-7.172503,5.062941,7.368222,0.351885,-0.868508,2.249949,-1.654421,1.542211,-0.048480,-6.537865,-6.524164,-1.220169,9.439375,-8.758059,-6.232081,-0.234256,-3.119930,8.575854,6.556354,-1.847952,7.657086,1.716830,1.823411,0.680418,4.247361,1.936744,6.436127,-4.107490,-0.951001,-6.631921,8.858040,1.719411,-4.451834,-8.949206,1.216538,4.032522,-2.867730,0.634232,-0.192782,6.785689,-5.931259,2.988156,-2.413376,-0.199215,9.304404,9.316465,-3.128283,-2.172903,5.700792,-3.856713,9.438360,0.912900,-3.328793,-0.370656,4.827569,2.960587,-6.602769,3.379070,-9.235522,2.578482,-2.502474,0.676900,9.842667,3.132169,-8.637817,-5.038801,-7.107855,8.908928,-2.193047,2.299822,1.153431,1.205315,2.651864,-4.927539,9.606469,5.873342,-1.842729,-4.447580,-5.359626,-6.384738,6.956248,8.246334,-8.146531,-4.670087,-9.157384,-3.234283,-9.171175,7.384272,5.898179,-6.375025,5.627078,-8.259311,-4.641240,2.366366,6.342888,3.194304,-1.744405,-4.574752,2.203977,7.272353,-8.812673,8.839145,-2.027264,-5.389821,-5.605466,-3.049749,3.456104,4.597893,8.744019,-2.653253,-9.777702,7.370489,-2.086714,2.073257,-9.615264,6.633615,-6.098063,-8.527241,3.963999,-2.603662,8.527056,2.356832,-4.681152,-2.064971,-9.249330,-9.157152,-3.846050,7.838279,7.716110,-1.779000,-5.351299,-1.203475,-8.370883,9.857184,2.699318,6.852560,-5.064725,0.441910,4.941837,-1.219997,6.604769,-3.039514,-8.684857,-3.172448,-8.927404,7.994345,1.469363,0.266334,-9.519034,3.945785,9.814921,-2.847813,-3.321523,-8.069003,6.941100,7.783212,8.920330,-7.665714,7.044326,7.662514,2.900325,-2.424932,-0.460514,-4.172768,-8.846018,-6.388456,-1.869466,0.182782,0.646773,-1.282828,-5.329627,8.758990,9.230404,5.369833,-1.106541,-1.527636,-4.308532,-3.121703,4.972939,4.096692,0.094081,1.276499,6.116565,-9.126781,-4.265421,0.249511,-7.808381,-0.767682,5.546999,-0.331783,-1.223603,9.201410,-9.003888,1.368773,9.810267,2.353582,-1.724348,-8.908580,-0.216223,-8.032302,-0.522470,3.236882,-2.102082,-1.851598,-9.083061,-3.232546,-0.402097,1.514637,5.648348,-8.877332,8.629506,0.167298,-6.094926,4.907281,-7.550936,8.574673,-5.256337,0.629469,-2.912847,-0.045751,6.780639,2.320878,-7.058836,-4.065787,2.150635,-0.038178,-0.633450,-8.842077,-4.158861,3.977013,-2.008627,1.799708,-8.485461,3.116597,-2.720115,9.252468,-7.303676,1.856706,3.190288,1.441020,-7.641394,3.391660,0.609298,9.930589,-9.944011,4.872570,6.162555,9.764790,9.274628,-5.594833,-5.665243,3.871766,-9.529487,3.625955,-7.678025,-5.558004,0.882201,-5.182424,-7.683939,-8.336850,-0.978140,5.311161,-8.348756,0.425197,0.721419,0.644253,8.877258,2.174022,-2.164694,2.874671,7.733836,2.407011,-9.400571,5.157073,-7.881926,0.490109,6.366035,-6.535208,2.538848,-4.130960,-7.145376,-2.239427,-6.263928,0.475770,-8.056531,-1.506443,0.473622,-7.907686,0.053286,-3.049481,2.957065,-0.343885,-9.570383,-9.727908,6.827442,-5.826703,2.658723,3.296360,-9.332099,-0.505098,-0.866274,-6.905724,-8.095323,7.368247,3.256525,5.050683,3.859062,9.849675,5.456938,9.919630,-6.837569,-9.753329,-2.323661,-1.165923,-7.479324,2.829445,7.663697,-7.895054,3.384025,0.189402,0.958446,8.690248,-4.713319,-3.143381,1.922849,-3.494185,-4.973884,9.070543,7.872168,1.077063,-2.887699,-2.886171,4.945603,7.393766,-1.146113,3.323465,-0.449188,-2.733449,8.838524,-8.455889,-1.683025,0.532020,8.543981,1.579971,-5.524829,-9.681440,5.599772,-5.722695,-4.631479], dtype = "float64")#candidate|12740|(2025,)|const|float64
call_12739 = relay.TupleGetItem(func_1639_call(relay.reshape(const_12740.astype('float64'), [2025,])), 3)
call_12741 = relay.TupleGetItem(func_1642_call(relay.reshape(const_12740.astype('float64'), [2025,])), 3)
func_4906_call = mod.get_global_var('func_4906')
func_4907_call = mutated_mod.get_global_var('func_4907')
call_12746 = relay.TupleGetItem(func_4906_call(), 0)
call_12747 = relay.TupleGetItem(func_4907_call(), 0)
uop_12754 = relay.exp(call_12739.astype('float32')) # shape=(7, 15, 3)
uop_12756 = relay.exp(call_12741.astype('float32')) # shape=(7, 15, 3)
func_3755_call = mod.get_global_var('func_3755')
func_3757_call = mutated_mod.get_global_var('func_3757')
call_12763 = relay.TupleGetItem(func_3755_call(), 0)
call_12764 = relay.TupleGetItem(func_3757_call(), 0)
output = relay.Tuple([call_12726,const_12740,call_12746,uop_12754,call_12763,])
output2 = relay.Tuple([call_12727,const_12740,call_12747,uop_12756,call_12764,])
func_12795 = relay.Function([], output)
mod['func_12795'] = func_12795
mod = relay.transform.InferType()(mod)
mutated_mod['func_12795'] = func_12795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12795_call = mutated_mod.get_global_var('func_12795')
call_12796 = func_12795_call()
output = call_12796
func_12797 = relay.Function([], output)
mutated_mod['func_12797'] = func_12797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5242_call = mod.get_global_var('func_5242')
func_5244_call = mutated_mod.get_global_var('func_5244')
call_12807 = relay.TupleGetItem(func_5242_call(), 1)
call_12808 = relay.TupleGetItem(func_5244_call(), 1)
func_2190_call = mod.get_global_var('func_2190')
func_2193_call = mutated_mod.get_global_var('func_2193')
const_12829 = relay.const([[-1.411878,1.401853,-5.918605,-8.294555,-9.840994,-9.085935,9.611239,-7.173694,-6.761087,-9.976754,7.623986,-3.908330,-1.877389,-0.924167,-4.205962,-4.580921,6.984221,-8.906902,-5.913137,-3.745121,5.289919,3.143140,4.287221,-8.639781,2.393714,-7.310219,-3.786845,-6.614326,-4.899195,2.033843,6.614922,9.189348,2.238271,3.514319,-0.399487,-2.468754,-5.146786,-0.095981,-4.153321,-6.995605,1.264982,-4.380463,7.533741,-2.825699,-1.058050,-1.146563,3.510936,-3.349501,3.670970,0.708405,9.783907,5.329804,1.529040,4.743743,-7.535946,-2.732306,-9.549191,7.708475,1.575325,4.125967,-7.444732,-6.938808,1.370649,-5.745185,-4.115152,6.656646,-8.912198,4.995338,-1.622862,6.588832,-9.262331,3.564641,-5.770367,-4.712991,-3.727836],[0.882249,-0.032680,3.851990,-5.749003,-9.678404,3.552995,2.737726,7.730157,6.893593,4.758061,-9.474549,-7.404647,9.053149,7.228836,7.076720,3.628729,-4.398632,-8.963746,-1.533370,1.784904,5.689733,-8.964233,-1.791402,2.742317,2.470579,-1.875387,2.059965,8.722619,-3.051009,-3.603529,4.600529,-2.590388,0.561733,4.580238,-5.426199,3.851042,5.384592,-7.997364,3.465628,2.316129,-0.157443,-9.831763,2.495397,-1.606073,-7.603398,2.707045,9.019045,1.968810,-9.229294,-7.672669,-8.230344,-4.286533,4.603258,5.491714,-6.534297,2.316661,1.993586,-0.878091,-5.087668,-4.375177,-4.443809,-3.660539,9.940216,-2.880925,-2.672483,-2.470434,-3.481094,-6.521737,4.722250,-0.915956,-1.026215,1.163500,-7.111267,-1.772793,-4.826792],[3.065575,-1.624792,-6.451324,-7.588636,3.994035,0.106856,3.682181,-0.560602,1.718734,9.978834,-5.396415,-2.216831,1.582250,8.785486,0.154312,-2.357071,-0.457185,-5.045135,5.127986,-2.471687,7.933414,-9.749058,1.654005,-8.249278,9.943157,6.469348,0.099360,7.996597,-1.349195,9.055686,-1.929203,-3.137343,-1.508614,-6.837242,5.787775,6.298854,-5.157886,7.674830,-2.903739,2.693675,-0.809789,1.529062,-4.017559,-8.127117,-3.896750,-3.700739,-1.568235,4.598885,6.570389,-8.162153,-3.959309,4.678285,4.339651,0.253668,-9.621243,4.142458,3.525378,-8.482706,0.253067,-3.203884,-4.156070,1.035294,1.681067,-5.079226,-0.284957,-9.225287,-1.971637,4.502485,-8.542509,3.874295,0.133019,8.847471,-4.521228,-9.536766,3.437515],[1.865549,3.808176,-8.088734,0.523697,3.072454,7.985321,0.765431,2.690095,4.400534,4.481679,-8.576304,-4.679474,1.014793,-2.509680,-0.273933,-2.338385,7.240680,-2.943454,-7.064218,-1.568617,2.285957,8.917127,0.889037,-1.406527,6.728667,-1.029972,-7.705048,7.298284,2.188721,-1.360100,5.545199,6.838017,-3.765192,-4.134715,6.101046,8.903337,-2.113408,8.105220,3.760276,4.420294,4.197725,1.232708,-5.282907,3.712076,-2.655091,0.268091,-4.954825,-7.553410,0.215843,-5.029325,-3.100860,6.940503,-4.242328,-9.846923,-1.730129,-8.031146,8.951217,-3.563607,9.914837,1.715426,8.014516,4.029762,6.882364,-3.409349,1.390630,-3.631844,-5.112033,-4.216983,-3.044667,6.251269,-0.890897,6.025717,9.116332,1.289051,7.601930],[-4.944944,-6.270396,8.272984,7.655878,-7.044786,-0.238589,-2.396945,-8.243056,6.410567,-4.107147,-9.007607,9.218677,-8.518538,2.203910,0.480939,1.817256,0.727130,2.823495,4.725743,-4.103133,1.364780,-1.243069,-7.217927,7.623892,-5.849529,-2.289704,-0.541259,-8.779664,-8.818831,2.105630,-7.058503,4.041820,-7.897942,-3.693540,6.689651,1.160324,1.662706,7.004596,-6.514510,-3.936864,-3.384162,7.260953,-3.660791,9.434542,3.811891,-6.903969,2.707983,4.347685,-7.813860,-3.678361,4.021981,0.290111,5.724750,-4.025594,6.386610,-2.100391,4.150250,-8.730703,1.290910,-1.307115,-2.048518,3.874189,-1.435965,8.582315,-1.100358,-8.447798,1.220651,6.629663,-5.028614,8.377297,-1.480503,8.296813,9.082108,6.354665,-7.219795],[-0.223502,-5.383866,-3.001814,-9.875674,0.292212,3.474434,-7.657243,2.655446,-6.132448,3.222106,1.189102,3.317303,2.407315,9.220122,-6.057231,-4.059779,-9.058809,-3.927704,5.987545,7.233564,5.766211,7.917228,7.553256,8.351299,-7.145658,7.938858,-7.716652,3.785233,-4.028101,-0.588173,-5.105920,9.225516,2.903409,2.226789,-7.291564,-6.469412,-3.458873,-5.585581,-0.106449,7.937989,-3.617676,5.078934,4.974911,0.975072,3.041229,-4.040379,-0.436868,-3.068139,6.570421,1.345946,-6.864232,-4.824846,2.322410,8.119094,-5.753435,-6.309091,7.517518,-3.075674,-9.825764,-6.478260,5.826432,0.898535,-6.931460,-2.795054,-0.776392,-9.383240,9.912354,0.144594,0.873020,-4.656186,5.631596,-5.125473,-4.097488,9.019635,-3.166814],[-9.894558,9.660637,-7.477312,-6.577400,3.482517,-9.095148,7.153689,-7.658458,-9.126972,2.924986,-6.471021,5.408410,-7.892099,4.951846,3.360784,3.220691,8.742320,8.946368,5.904267,-6.713492,-8.956718,-3.186642,-7.843321,-0.560801,-0.623335,-8.636203,-9.218264,3.621207,8.239426,9.317612,8.701727,3.790956,6.528749,-1.429186,-5.357472,7.887119,0.646963,-9.476060,8.288762,-5.000847,9.702302,-5.355429,-6.523573,-6.406041,-2.677134,-4.055945,-2.845151,-0.769058,6.476637,-8.131586,-4.874924,-0.549772,3.989226,3.342957,-0.143474,-4.554424,-7.379630,7.431337,3.988694,7.445987,4.920719,9.478601,9.079141,7.547005,-0.821267,-9.548151,-8.527159,-8.778430,2.910393,-7.090224,7.910903,2.616223,9.670638,-3.717914,-8.939574],[-5.467391,-5.213860,-5.119598,6.589000,-6.209847,5.723563,-4.418237,3.059004,-1.204030,8.504264,-1.372244,2.647821,-6.317749,4.272519,8.903084,-1.363035,6.924758,6.401005,-7.783658,-5.166002,-9.403260,0.171672,9.043799,5.508746,-1.744264,-9.701500,0.501867,-9.091369,-8.051239,4.671103,-7.922779,9.168711,-6.604520,1.395784,6.344902,3.861302,5.602616,1.184370,9.332980,-6.709520,5.598218,2.549646,6.295471,-2.716271,3.599571,4.056181,-0.307121,8.320317,-9.414058,3.112702,-5.560360,1.796918,-1.239643,-3.075347,-5.651646,0.336738,2.335640,-5.779925,-4.169605,-8.118394,-5.463409,8.195501,-3.253445,4.959895,8.366841,1.204430,9.561826,-8.286933,0.712919,-3.940608,1.699477,9.236159,-2.035625,1.923231,-2.126665],[-1.774376,-6.827433,4.499366,-8.906742,5.980033,-9.589362,-1.028464,2.738251,7.881576,9.949692,-7.260249,2.776147,-1.712525,-2.599105,-3.332767,8.620940,2.806826,7.411561,3.966713,-2.656152,7.041974,3.113486,-0.027350,-5.112573,6.640872,8.304648,8.774105,3.248387,-3.856052,7.934254,-6.791388,5.739852,-7.514859,9.243483,2.225164,-7.057527,-3.110072,-8.173211,0.842088,-9.961284,-1.223313,-5.930755,-5.445191,1.370278,8.636818,8.467776,-4.702415,-2.696584,5.104911,-6.493683,2.589293,-8.778698,-2.766825,-4.475135,4.233830,-7.367092,2.153060,8.042889,-9.380880,-4.943614,-0.769709,6.702667,3.092658,8.665784,0.762613,6.422840,2.576531,-9.488791,-8.049778,4.730316,3.446548,1.294578,-0.180740,-0.357244,-3.553892],[0.384065,9.963592,5.601032,-9.872471,5.173528,-8.441495,-1.663848,-8.546547,4.905650,4.136104,6.378820,-2.084063,2.841779,7.108307,8.386325,3.678955,-6.390053,4.817498,6.401779,2.145632,-8.760185,5.734857,6.938215,1.378444,-1.517697,5.619549,-3.948491,-5.671526,-5.518029,3.304311,0.355831,-0.108671,0.978881,3.204111,2.660109,-7.483848,-9.674148,-5.492943,0.546008,-2.256154,3.602868,6.481850,4.888268,0.789595,-4.110514,5.967926,9.391672,3.221473,-8.367828,1.346542,7.962667,7.392358,7.724834,8.591089,7.638563,-5.317286,6.437869,-2.913592,-7.924330,3.544434,2.633157,-3.105190,-1.305265,3.995404,6.944533,6.209155,-8.512244,-4.981185,-5.834327,9.347487,-5.603714,-4.743670,0.708970,-3.689333,6.147127],[-9.317838,3.967690,4.618818,2.213025,-7.428876,-3.510753,9.117555,-5.669064,-2.573725,-1.209663,-3.043743,-7.733529,-2.462661,-2.232607,9.604057,-5.741096,-1.666815,-2.807773,-0.557572,-0.128022,-2.971847,-1.351214,-8.806270,-4.671806,1.065600,-4.639864,6.908878,0.342824,-0.975053,-1.638235,7.161327,-5.458212,-1.456003,9.368530,-6.503372,6.287597,-7.092320,-9.535702,-9.351118,-0.135197,6.084098,-9.671213,5.001428,0.632459,7.177292,8.308130,-6.891570,-2.654621,-8.427263,5.299248,4.910835,-8.489199,-7.583307,-1.206856,3.780131,1.933694,0.116335,5.908181,7.066435,3.965964,-7.323940,5.958795,-4.739081,-4.323666,0.742074,6.606160,-4.299616,7.150314,-2.392773,-6.286368,-7.898102,6.853085,4.009086,-5.950905,3.966784],[1.435390,-5.016997,-2.401415,-6.646143,5.536229,4.140795,-6.348214,-9.123235,-8.414525,-8.152864,-5.881186,-6.600934,-3.858556,-4.618047,-0.165150,-4.921216,-2.026851,-3.445287,0.788360,6.129961,3.730905,1.061842,-4.843111,3.491156,9.954132,9.515741,-7.643683,9.549332,7.511513,8.692451,0.023619,0.001050,-6.024958,-2.294405,-7.094581,-8.185171,-0.701070,-4.178463,-0.460498,-6.525389,3.345870,6.652430,0.786598,-4.500809,1.331711,0.754157,-6.945255,-3.615162,-3.527702,-5.619358,-3.205970,-3.697060,7.782487,7.919228,-5.795996,5.199578,-0.430283,5.541626,2.596980,-9.084846,6.719932,9.426575,8.840335,-0.860877,-0.726314,-6.593935,-2.491881,-1.870492,9.133388,2.142281,2.336571,4.822319,8.074626,0.859173,3.820895],[7.350965,1.263423,-2.221804,-6.517407,1.511633,3.435323,9.438743,-4.759277,4.339227,-5.679452,-9.616848,6.527702,4.808726,-3.111194,0.922012,-0.189589,7.839017,5.435256,-6.006826,-2.699823,2.409855,-2.319569,0.599239,-6.636746,-0.529065,5.324208,-6.580798,8.737434,-8.609520,-4.471908,8.303155,-6.648274,4.451703,-4.535409,-9.785385,5.993347,-4.292825,-4.396417,-9.791200,8.625895,5.197709,8.410801,3.393715,4.700585,4.195172,-1.271140,5.285423,5.062843,-4.125728,-8.231898,-2.128966,-2.261930,6.238875,7.964956,9.346250,8.966758,6.324758,-9.280939,5.477188,-2.229988,-3.841968,5.700096,-4.364004,-1.571908,-9.687684,5.455008,-5.118314,8.839051,-0.301431,7.644686,4.346216,7.420244,-2.968147,-0.471503,6.043111],[-3.583921,4.416787,8.714626,-3.477016,-5.381497,9.828206,2.198397,-2.396851,8.878238,6.611783,-4.320530,8.255640,-5.256648,-3.950961,2.187890,9.881104,2.452770,9.497498,-1.902475,-8.514699,-2.921083,-3.494500,7.691247,6.982437,-9.240628,4.666613,5.018963,-6.355416,-3.119425,-7.248845,-8.187298,5.082984,-0.457061,4.057500,-0.843039,-9.447460,9.567590,7.714530,4.790881,9.786827,4.035673,-6.673027,-7.053355,-6.109448,4.820325,-2.635042,9.419325,4.353729,5.710099,-8.949325,-0.851496,-6.297211,-8.873580,-4.150450,-3.369906,8.191322,5.297157,7.429344,-0.082488,-9.387161,-1.135915,8.808538,0.721141,-9.971218,7.058468,-9.689036,4.039990,3.995256,-2.259971,8.874147,-9.261321,2.948898,-3.923470,8.436387,-2.648260],[6.118590,-2.609524,-5.274299,2.661323,-7.647841,-7.184071,4.952240,-6.048428,3.620271,-0.497581,0.608001,1.830412,-4.619804,0.633918,-4.533074,-2.840006,2.585500,-5.552695,-5.841582,-8.658135,4.436898,0.464350,-4.343276,8.110642,7.868233,-6.744062,-9.041990,2.686751,0.143612,-8.191274,-5.848211,6.661764,-3.301247,-6.353930,-9.577107,0.305457,5.917379,-5.065003,-6.967578,9.002977,8.383860,8.694230,3.842333,3.953952,1.483603,-4.081143,-9.861467,3.117876,8.946502,4.513789,-9.193602,1.748105,6.532075,8.276105,-6.490637,4.379592,-6.221125,7.167865,6.384004,9.534791,4.908147,2.167911,9.048494,-1.324037,-1.755596,-3.920020,-3.519574,-6.140119,5.406087,-0.241205,-3.985122,-0.266136,-1.788444,-3.886873,-7.536689],[-0.856262,5.127345,9.711923,0.194971,6.579853,5.695926,-3.533609,-2.916951,3.527785,5.773493,3.028223,-5.373925,-9.136647,3.414671,-1.509153,-1.226287,2.341820,-5.823134,2.911285,-6.521758,9.614724,-2.511421,-0.877747,-3.869377,6.460501,1.257849,4.333902,-0.578797,-3.305270,-7.459521,6.119221,0.890068,-5.098164,2.057261,4.206323,2.938596,2.037323,6.233919,-3.060509,1.204230,4.512294,-9.420564,-3.231477,-9.586352,-3.795729,-7.455948,-6.564036,7.136320,3.565976,-4.073371,-4.854430,-5.366955,0.013128,0.532432,7.451732,6.485939,7.993072,-7.958511,-3.264115,-4.114415,8.053764,-9.620071,8.790850,7.061936,-7.413897,7.163334,2.721994,-9.040503,3.291891,-3.486354,4.586249,3.758463,7.105651,-6.708203,1.563042],[-6.271665,8.989977,-6.657888,-0.738021,-5.466208,5.458882,-9.020217,7.468035,4.170487,-0.335542,3.655256,-9.471476,7.235479,-2.612476,1.740773,-4.349545,3.921948,8.368976,-8.027509,5.561961,-7.821554,8.484784,7.786533,-3.909761,8.309938,-9.060735,-3.194869,-1.887801,-8.402236,5.273492,-8.129703,9.362082,-3.229273,6.296162,8.945435,0.843130,7.182951,-2.334504,7.112673,3.210691,0.344289,6.927624,-6.894032,2.066652,0.060947,8.636769,3.500497,1.789640,7.153155,-2.412483,9.374350,-4.778780,-6.279804,1.940338,9.952159,4.097428,-1.352952,-8.969130,-9.440007,7.794300,8.934806,8.321036,0.432452,-4.843362,9.648250,3.753043,-4.767803,3.980815,-2.522583,-9.063913,3.235941,8.672734,-6.857632,9.134207,2.287577],[-3.967101,3.059965,0.199603,-4.071500,1.499527,6.267556,-0.953806,-0.814678,-1.548674,-9.777112,2.572012,-0.854003,9.139178,-3.261267,6.256697,9.190845,-7.785333,0.661174,-3.776710,5.078805,7.701383,-1.213975,-6.130500,2.679625,-3.412532,9.569646,-4.115532,-6.823188,4.680515,-3.560628,-7.995104,-0.542336,-8.624674,3.897229,-4.222683,-9.370794,0.300501,3.233242,7.922408,-9.627439,7.027061,4.488631,-3.264698,4.590896,5.317558,-5.567267,-4.298630,-5.950316,5.959542,8.285885,7.793168,6.387442,-0.759552,-9.228649,-1.216994,4.590751,7.609826,6.580701,-2.946904,7.979965,-5.237374,-7.431954,-7.164989,6.361200,-3.304643,0.203144,-8.741303,-9.233102,-5.838661,-5.717850,5.964904,-7.170425,6.243202,-7.795307,-7.545274],[5.710813,-5.366991,9.622610,-1.572503,-8.983575,7.840631,-3.264276,-1.736246,6.814918,-6.674179,8.956532,4.078439,-5.098115,8.715115,8.374518,-2.747044,-7.354315,-3.372313,4.646075,-9.475484,8.574352,-0.293793,8.690282,-4.017760,6.065331,4.128163,-1.554136,-2.951019,8.286224,-0.949111,5.904119,4.169006,3.130868,-4.879857,-7.596036,-4.309010,-6.498064,-9.935481,8.283393,-5.358725,9.449372,-9.146014,1.232239,-6.099149,-9.039213,0.089553,3.023962,-5.503022,-8.812914,0.060437,8.197401,-9.308029,-6.795287,-9.825552,9.280437,-1.398536,-5.804998,-3.051942,1.065578,-9.578710,4.917595,-4.758302,-0.947010,5.001738,6.807755,5.688196,-5.012754,-7.343672,-1.322894,7.279061,-4.884469,-6.901427,-7.257249,-4.266234,5.330190],[0.840745,-3.079035,1.052572,-7.455624,3.944324,-2.078614,1.317249,-0.054282,0.617246,-9.262264,-4.578123,5.044932,4.360559,6.478030,5.707469,-3.249686,-7.084150,-3.253074,4.745818,-8.195709,-3.119936,4.455002,-6.002575,-5.145975,1.716734,-4.120897,9.851386,-3.862649,1.649471,-7.612024,1.327374,9.958816,2.294507,5.320132,8.588509,2.615607,-1.883022,3.844712,-6.909805,4.556535,-2.356639,5.617695,9.613397,-8.922190,0.635736,4.548592,7.187994,-8.111258,5.595956,4.573953,-5.215607,-9.865202,9.513391,8.992205,1.650345,2.530131,-6.106200,6.325660,1.151679,-6.342060,-4.835629,1.758876,-0.723996,-4.514545,7.790300,-2.287283,-5.718173,2.908683,-9.810480,1.317040,4.581321,0.212247,2.465775,0.186861,-2.435943],[-7.992283,3.798980,-2.958014,4.039480,2.995528,-1.017850,-3.384081,2.210292,0.835921,-8.482168,1.998652,1.912630,6.745302,-1.357683,2.281069,-1.530711,0.960922,2.279050,-5.857456,9.131605,-8.619816,0.311303,-5.129140,-9.321908,0.575352,6.169297,-1.302113,4.751626,6.141739,-6.481877,5.854452,-4.266681,-9.581750,-9.723204,9.928412,0.385300,-0.444892,-8.766152,1.049534,-2.661347,-5.507004,1.236078,-4.187593,-5.784647,-6.170798,8.521711,-8.737714,0.438650,5.392906,0.066265,4.774664,-8.246825,8.805960,-8.557023,7.655866,9.832611,-3.590856,-6.028029,-3.697054,2.188496,4.903359,-4.208827,-6.900524,4.238188,5.101773,-8.490371,6.446180,-0.871608,-8.539784,0.160293,3.363015,2.203137,0.618863,4.863796,-2.907080],[8.102027,3.011932,8.465257,5.502430,8.204493,1.920316,5.441761,4.600629,-2.981906,-9.076729,8.711806,-3.483340,-7.591388,1.832229,4.691469,-7.424308,0.023460,-1.961281,4.613582,5.589034,6.094669,1.175706,3.399363,-3.361507,-5.673818,9.846306,8.249048,-0.058422,-0.513587,8.001038,5.696085,-3.920431,7.283487,-5.526943,-3.773481,5.875643,-2.203847,-0.663913,4.155066,6.662627,9.521888,-1.523225,5.715566,-9.193713,-8.104506,4.643785,2.886373,-9.781385,2.123439,-4.322600,2.856282,6.804860,-5.660380,6.517737,-7.793225,7.351316,-7.628445,-6.882939,-6.615353,7.840178,-0.975994,-1.455410,-3.958163,-7.468852,4.339577,7.883903,4.747277,7.502927,-9.547814,0.220839,5.070326,-5.222632,-0.283028,9.454945,-9.348292],[7.924870,-3.543350,-8.209105,7.508933,-7.208613,0.203121,6.756416,-3.111255,-1.237994,2.760345,7.885186,-5.384608,-5.852669,5.742247,6.144814,-0.057534,-2.423527,5.140368,2.903194,-2.924586,1.905742,8.005927,-5.991529,4.609997,-1.916453,-2.533379,-6.790711,-0.267429,-4.650012,-6.197280,0.083542,-8.539669,5.661483,-6.595955,-1.636713,-8.528313,9.728886,-6.289314,0.005054,-4.824009,6.188668,-5.344835,-2.453068,-3.729186,-6.026442,-6.794151,-9.682079,5.965575,-1.399811,-3.218967,-5.753256,4.839621,9.945862,4.764347,0.371210,-1.963606,5.737362,-8.068884,7.752517,-5.731968,-4.726793,1.503208,1.555461,-8.493658,8.849089,1.781811,-5.204514,5.149578,-3.145539,-0.959629,-2.796193,-2.405921,3.299496,1.665671,-1.155096],[-6.343429,9.270173,4.685620,1.209414,-5.425796,-6.742417,-5.521600,-0.267269,-4.502947,6.731758,8.387557,-9.482754,0.179180,-1.260247,-6.958043,-9.264484,7.298917,4.944640,-9.858059,1.388434,3.528734,-8.572337,-8.308014,4.808110,-9.623850,5.054017,-5.372592,9.111064,-2.234445,5.047380,-6.445636,1.663973,6.607271,-0.620636,6.004262,-1.019010,-3.539514,8.695565,-5.775401,4.894772,1.384005,-8.922125,-1.292081,5.799420,9.403374,-5.088723,-2.719120,-7.018164,-1.371427,2.775194,-6.467028,-6.302808,1.099658,0.381528,-3.076020,-0.316631,1.982688,5.182582,-7.813736,-6.848508,5.909999,-3.185966,9.369358,7.168557,5.445080,1.168756,3.762556,-9.413939,5.667285,-4.640479,4.360000,0.067220,1.115435,-1.342584,7.992560],[6.628575,7.218870,-9.985475,-6.626965,-6.989579,7.430189,9.614486,4.523538,7.292362,4.408534,-1.904575,-9.536140,-4.330060,3.563499,3.223651,6.182228,8.356508,-2.150281,4.674723,-9.900782,4.240932,-3.636026,-9.776287,-1.201631,-5.106660,7.731325,-2.971301,0.354175,3.768811,-8.535231,3.470596,4.103621,-7.470250,3.877129,8.746155,-4.925709,0.319523,7.686506,-5.496258,7.315508,-9.133699,-5.681915,-6.997000,0.779236,-0.210049,-2.578898,2.891894,-1.552125,-7.321314,-7.124829,2.979910,-3.153431,9.624260,-3.811113,5.361497,-0.903202,-3.004754,7.217831,-5.253166,-6.263406,-6.789207,0.366360,9.806657,5.192189,6.954378,9.539138,-7.329799,1.734767,5.250195,-6.003655,3.377073,-4.596965,3.375260,-2.741661,-7.573926],[-5.934399,8.988475,9.325386,3.916118,-4.206217,-6.451961,-8.211442,5.903587,-3.933314,4.258983,-8.119031,4.503864,3.024071,-8.133844,1.083743,-9.216531,9.809155,5.534064,-3.901764,4.048200,7.004874,-7.432790,5.814910,2.896056,8.161610,-2.645414,2.021415,-3.743324,-2.173656,-3.429688,-1.573958,2.349924,-9.693342,-5.453614,9.405717,-1.263772,9.820386,-9.468985,-3.146727,-5.324298,9.173642,0.279833,-3.531337,5.647338,-9.679125,-4.866657,-7.483669,-3.880436,-1.082081,-9.930346,3.017324,-5.080907,9.806402,6.013350,-8.464734,7.500956,-9.828429,-9.906239,7.250110,2.677966,2.179458,-3.863486,7.505322,5.125288,7.009918,6.618589,-5.637471,0.468386,3.978811,4.423864,-3.481194,8.385505,-8.912310,2.770553,7.449076],[6.948818,9.424417,-1.457484,4.380582,-6.191654,5.522280,1.109882,-9.034478,-3.679156,2.254732,7.985695,-9.828353,-9.377277,5.486203,-5.468555,-3.683663,0.469710,8.061582,-1.173019,4.416968,9.750523,-1.269467,-3.087430,6.956562,-6.642290,3.316767,-2.032554,-5.645892,-4.634411,1.543109,-7.608563,-2.715510,9.462649,-4.207796,-9.994115,-2.452999,-5.552428,-1.085973,4.457940,4.781272,-5.335154,-2.773080,1.180426,6.011933,-0.700901,-2.938304,-9.076962,-5.485516,5.948274,2.675853,7.320402,7.745054,1.169907,-5.580394,-2.640817,-2.831720,-9.385712,3.409775,-5.725204,2.413536,9.926136,6.948846,4.746287,5.367114,-8.698922,-0.631641,8.294654,-1.309219,-4.392605,7.773167,-9.325355,3.807021,-4.536928,-2.889142,-4.753931]], dtype = "float64")#candidate|12829|(27, 75)|const|float64
const_12830 = relay.const([[2.488162],[-3.652840],[-4.830325],[8.462886],[-0.448970],[-8.254732],[-3.184332],[8.032015],[1.101096],[-6.351122],[-2.538189],[-1.419523],[-0.790759],[-5.915682],[2.545554],[-2.405172],[6.248107],[-4.172826],[-1.943694],[6.605744],[6.691202],[9.055495],[2.776235],[4.637837],[5.042328],[3.618821],[-3.617339],[-6.801942],[2.973087],[1.840581],[7.383967],[5.922298],[-5.073409],[-3.039794],[3.924548],[-5.474581],[5.545929],[3.738610],[-6.557446],[7.103352],[-0.378235],[2.132167],[6.366281],[5.659113],[4.392792],[7.959553],[3.395284],[2.695401],[-3.854413],[-5.319860],[2.509474],[9.775620],[-1.690804],[6.471141],[5.912707],[-9.407591],[0.559711],[-5.989189],[-5.182754],[-4.408480],[0.268726],[-0.094670],[-8.665823],[-9.409632],[9.103777],[9.822806],[6.734460],[0.161298],[3.697541],[2.073476],[0.617950],[-0.818482],[8.097180],[3.841063],[-9.479795],[7.178770],[2.104557],[-4.547373],[5.360256],[9.106211],[5.905505],[4.349424],[0.581438],[-9.572556],[-2.215660],[4.570584],[-4.979434],[-9.828506],[-1.122497],[5.840820],[3.232470],[-0.511274],[-4.762946],[9.212735],[-5.139567],[-2.222589],[7.277641],[-0.844254],[-3.471801],[5.177610],[-5.765095],[-4.437118],[-5.794835],[9.171738],[4.857908],[1.616868],[8.321642],[3.590485],[1.974295],[-3.949248],[6.249418],[3.704102],[-0.878130],[1.329226],[4.088447],[3.311959],[8.477338],[-9.470796],[0.022672],[8.401647],[-1.488649],[4.427563],[-2.639495],[9.553739],[2.379934],[2.447756],[-0.108596],[9.584265],[8.803579],[7.847297],[9.083244],[-0.894281],[-0.176419],[-0.921713],[-8.773825],[-2.620965],[3.988748],[2.035027],[2.333861],[0.652999],[-0.381269],[9.191730],[7.175447],[3.501441],[-5.561793],[5.151087],[-5.146059],[-3.276799],[-7.431968],[-2.263822],[-4.429344],[3.228118],[-1.874266],[-5.297700],[8.784280],[4.777325],[-1.852244],[-1.149684],[4.802436],[-5.265015],[-4.454461],[-0.199662],[-6.941621],[-3.067045],[5.746184],[6.289309],[9.178065],[7.162356],[5.304624],[2.690010],[3.281119],[-6.060479],[-4.396052],[-4.886216],[7.158933],[4.253329],[-9.405742],[-5.183260],[-4.660899],[-3.231308],[0.437872],[-1.773377],[-9.542115],[-1.789244],[9.268238],[1.913831],[-9.268201],[-9.357842],[-4.106107],[1.634900],[-6.698961],[-7.955978],[-3.365327],[7.896585],[4.062217],[-3.826999],[6.474230],[4.375376],[2.807918],[-7.761458],[-0.066530],[6.276837],[7.917927],[4.369354],[-6.107696],[4.136381],[9.645443],[-7.494523],[-9.246090],[-0.539372],[1.906436],[-9.358565],[8.030401],[-8.863373],[-1.903948],[6.093675],[-5.367010],[2.862183],[3.339845],[-1.960147],[8.221623],[-2.956758],[7.504714],[-6.949651],[-2.954705],[3.090351],[-7.637583],[-3.143496],[4.969698],[-0.999299],[9.216446],[-7.470486],[-2.749777],[-4.095757],[-4.483659],[-3.665951],[-2.816444],[-6.326540],[9.300522],[-2.592245],[-9.114100],[2.777798],[5.918010],[-5.028973],[-2.341059],[-7.205650],[9.744067],[-7.153462],[5.111649],[7.995560],[5.337516],[5.709018],[-3.569404],[9.132245],[7.345868],[9.037835],[9.408243],[-8.589918],[-9.902331],[9.137360],[7.528761],[0.057589],[3.658591],[-3.885848],[-2.959148],[-4.091979],[8.338591],[9.663416],[-4.250716],[4.964516],[-5.483044],[3.052194],[6.714099],[4.233408],[-6.773545],[8.075802],[-6.147779],[-2.204701],[-6.289048],[-9.419722],[-6.936962],[-5.350843],[3.801144],[8.241830],[-7.495382],[3.459514],[2.642429],[-4.965217],[-3.988382],[0.613259],[-6.086719],[-1.474723],[8.280278],[-8.491706],[0.753083],[-0.972271],[-9.843130],[-5.348899],[-2.529883],[2.508019],[-4.713242],[-8.938336],[8.491004],[9.821950],[-6.718877],[-6.391491],[8.503941],[8.100582],[-4.106633],[-0.268746],[4.658176],[7.494776],[2.873440],[3.645163],[-1.473468]], dtype = "float32")#candidate|12830|(315, 1)|const|float32
call_12828 = relay.TupleGetItem(func_2190_call(relay.reshape(const_12829.astype('float64'), [2025,]), relay.reshape(const_12830.astype('float32'), [315,]), ), 4)
call_12831 = relay.TupleGetItem(func_2193_call(relay.reshape(const_12829.astype('float64'), [2025,]), relay.reshape(const_12830.astype('float32'), [315,]), ), 4)
output = relay.Tuple([call_12807,call_12828,const_12829,const_12830,])
output2 = relay.Tuple([call_12808,call_12831,const_12829,const_12830,])
func_12832 = relay.Function([], output)
mod['func_12832'] = func_12832
mod = relay.transform.InferType()(mod)
mutated_mod['func_12832'] = func_12832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12832_call = mutated_mod.get_global_var('func_12832')
call_12833 = func_12832_call()
output = call_12833
func_12834 = relay.Function([], output)
mutated_mod['func_12834'] = func_12834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2708_call = mod.get_global_var('func_2708')
func_2709_call = mutated_mod.get_global_var('func_2709')
call_12841 = func_2708_call()
call_12842 = func_2708_call()
output = call_12841
output2 = call_12842
func_12850 = relay.Function([], output)
mod['func_12850'] = func_12850
mod = relay.transform.InferType()(mod)
mutated_mod['func_12850'] = func_12850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12850_call = mutated_mod.get_global_var('func_12850')
call_12851 = func_12850_call()
output = call_12851
func_12852 = relay.Function([], output)
mutated_mod['func_12852'] = func_12852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7790_call = mod.get_global_var('func_7790')
func_7792_call = mutated_mod.get_global_var('func_7792')
call_12869 = relay.TupleGetItem(func_7790_call(), 0)
call_12870 = relay.TupleGetItem(func_7792_call(), 0)
func_6271_call = mod.get_global_var('func_6271')
func_6273_call = mutated_mod.get_global_var('func_6273')
call_12886 = relay.TupleGetItem(func_6271_call(), 0)
call_12887 = relay.TupleGetItem(func_6273_call(), 0)
output = relay.Tuple([call_12869,call_12886,])
output2 = relay.Tuple([call_12870,call_12887,])
func_12898 = relay.Function([], output)
mod['func_12898'] = func_12898
mod = relay.transform.InferType()(mod)
mutated_mod['func_12898'] = func_12898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12898_call = mutated_mod.get_global_var('func_12898')
call_12899 = func_12898_call()
output = call_12899
func_12900 = relay.Function([], output)
mutated_mod['func_12900'] = func_12900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_12978 = func_6154_call()
call_12979 = func_6154_call()
func_7790_call = mod.get_global_var('func_7790')
func_7792_call = mutated_mod.get_global_var('func_7792')
call_13011 = relay.TupleGetItem(func_7790_call(), 0)
call_13012 = relay.TupleGetItem(func_7792_call(), 0)
output = relay.Tuple([call_12978,call_13011,])
output2 = relay.Tuple([call_12979,call_13012,])
func_13022 = relay.Function([], output)
mod['func_13022'] = func_13022
mod = relay.transform.InferType()(mod)
mutated_mod['func_13022'] = func_13022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13022_call = mutated_mod.get_global_var('func_13022')
call_13023 = func_13022_call()
output = call_13023
func_13024 = relay.Function([], output)
mutated_mod['func_13024'] = func_13024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4834_call = mod.get_global_var('func_4834')
func_4835_call = mutated_mod.get_global_var('func_4835')
call_13042 = func_4834_call()
call_13043 = func_4834_call()
func_1653_call = mod.get_global_var('func_1653')
func_1655_call = mutated_mod.get_global_var('func_1655')
call_13044 = relay.TupleGetItem(func_1653_call(), 0)
call_13045 = relay.TupleGetItem(func_1655_call(), 0)
func_4978_call = mod.get_global_var('func_4978')
func_4980_call = mutated_mod.get_global_var('func_4980')
call_13057 = relay.TupleGetItem(func_4978_call(), 1)
call_13058 = relay.TupleGetItem(func_4980_call(), 1)
func_6724_call = mod.get_global_var('func_6724')
func_6727_call = mutated_mod.get_global_var('func_6727')
const_13061 = relay.const([[0.684557],[3.020676],[-2.879863],[5.814160],[-5.047663],[2.943477],[6.467728],[-8.001237],[8.974859],[1.815419],[-7.266397],[1.572981],[-9.017976],[-9.849423],[9.182050],[-9.836026],[-5.997100],[5.111255],[2.138562],[-8.153939],[-4.543326],[-6.453748],[1.119450],[-0.176598],[3.788302],[-9.338329],[9.167953],[-4.308279],[-8.252371],[-9.762484],[-2.135862],[-3.163416],[-3.248434],[8.164992],[-3.316822],[-6.579336],[1.245192],[-5.015639],[6.279808],[9.334741],[8.604303],[-8.053070],[2.277777],[-0.152575],[9.375123],[-8.889501],[1.556091],[-4.856834],[-2.484315],[3.592735],[4.157215],[5.278017],[-2.678719],[-4.439707],[-3.128917],[-8.490314],[8.021985],[-7.492688],[-8.507868],[-9.746073],[8.234368],[9.064454],[0.484037],[-1.268450],[7.282271],[-0.200260],[4.532497],[4.136741],[-2.955684],[5.179732],[9.867409],[-8.014494],[-1.909760],[-5.028097],[5.334080],[-7.226214],[3.777642],[0.557233],[-3.788843],[-6.951896],[-8.690520],[-6.079874],[-1.267166],[1.022907],[4.391462],[5.226052],[6.867410],[2.947788],[-6.954003],[-7.280335],[-7.280201],[-0.126532],[-7.805675],[-7.309069],[5.364349],[-2.731115],[-0.901802],[-3.571620],[-7.876880],[7.620780],[-9.522404],[-3.076864],[-3.957547],[-1.077491],[5.522265],[-1.071709],[1.538204],[5.379639],[-5.589483],[-6.361887],[-7.659413],[2.147606],[-0.251680],[8.942083],[-4.250682],[-4.544595],[9.228105],[-9.367343],[3.024101],[-5.675788],[8.932166],[-8.207408],[2.785624],[-1.618979],[-4.374728],[-4.653940],[3.007221],[9.532419],[4.966414],[-1.424766],[9.452960],[-9.504289],[0.416898],[-2.174915],[6.450068],[-4.471144],[0.467685],[-7.526229],[-1.907033],[-1.665671],[1.746402],[-0.507496],[7.631773],[-2.872546],[-7.629792],[-3.112769],[-4.532441],[6.666192],[2.322694],[-8.352470],[-1.044586],[9.470402],[8.576067],[3.691428],[-3.129660],[-3.329756],[-0.461261],[-9.760926],[-9.129283],[-7.024644],[3.852788],[-0.110113],[8.513187],[5.855835],[2.749223],[-1.389507],[-8.132426],[3.731041],[3.663757],[-6.168950],[7.565265],[5.886926],[8.651511],[0.236743],[6.004211],[-3.454338],[-6.690810],[-4.785680],[-3.649520],[-8.178050],[1.189975],[-5.347148],[-2.018101],[6.173578],[-2.425801],[8.398590],[5.088941],[0.467124],[-9.448379],[-6.164804],[-4.296973],[-3.949264],[-2.064492],[-1.865279],[-3.074380],[-1.220909],[2.605429],[-4.444458],[5.625364],[0.987588],[2.772898],[8.665305],[-0.946864],[6.656498],[7.327076],[-1.408764],[-9.028670],[-4.165255],[9.490365],[-9.642889],[5.483137],[1.650769],[9.828655],[-7.172301],[8.410230],[-1.553209],[-0.581287],[1.097331],[-9.994795],[9.207023],[6.178161],[0.602229],[-0.276626],[-0.560646],[-2.701479],[9.543028],[1.992828],[1.771284],[-3.071595],[3.472521],[1.509003],[-3.311213],[4.172518],[-8.624672],[-4.567127],[5.382781],[6.990038],[-2.165744],[-5.647320],[6.259508],[2.623913],[-7.446014],[1.249742],[8.573559],[0.051097],[-3.267653],[-3.170143],[-3.935927],[-4.549167],[3.540538],[-3.480705],[-8.008357],[1.411157],[7.261722],[7.826845],[-0.146335],[-0.264526],[-3.432709],[-2.089806],[3.691473],[-5.631215],[1.155526],[0.122538],[1.847298],[-1.524009],[-0.262188],[9.365572],[0.157990],[3.467821],[5.778560],[6.823667],[7.680697],[-9.365081],[-5.633021],[8.748397],[5.945746],[4.651138],[-2.321420],[-2.025166],[-5.771902],[-2.702014],[-8.915428],[-0.945909],[-1.908455],[-7.782185],[-3.386121],[-7.758458],[1.016626],[2.778080],[9.016839],[-4.944620],[6.394435],[9.927075],[-1.466819],[4.847850],[7.220795],[3.850681],[8.632938],[1.827536],[-3.444526],[1.333377],[6.422918],[-0.168833],[8.098980],[-2.311092],[5.144853],[6.393801],[-9.135555],[-7.717420],[-6.232366],[-9.157737],[-3.839813],[3.030712],[3.097213],[4.493579],[6.646736],[-3.548324],[-0.734996],[5.130159],[9.461668],[0.118958],[-3.686558],[2.823373],[4.495886],[3.722365],[4.722634],[4.752744],[-6.338771],[1.002481],[8.508340],[2.983376],[-5.393629],[-5.219657],[-2.856976],[-4.570427],[0.390264],[-4.548644],[-8.703258]], dtype = "float32")#candidate|13061|(338, 1)|const|float32
call_13060 = relay.TupleGetItem(func_6724_call(relay.reshape(const_13061.astype('float32'), [13, 2, 13])), 0)
call_13062 = relay.TupleGetItem(func_6727_call(relay.reshape(const_13061.astype('float32'), [13, 2, 13])), 0)
output = relay.Tuple([call_13042,call_13044,call_13057,call_13060,const_13061,])
output2 = relay.Tuple([call_13043,call_13045,call_13058,call_13062,const_13061,])
func_13065 = relay.Function([], output)
mod['func_13065'] = func_13065
mod = relay.transform.InferType()(mod)
mutated_mod['func_13065'] = func_13065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13065_call = mutated_mod.get_global_var('func_13065')
call_13066 = func_13065_call()
output = call_13066
func_13067 = relay.Function([], output)
mutated_mod['func_13067'] = func_13067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3391_call = mod.get_global_var('func_3391')
func_3393_call = mutated_mod.get_global_var('func_3393')
call_13073 = func_3391_call()
call_13074 = func_3391_call()
func_11278_call = mod.get_global_var('func_11278')
func_11279_call = mutated_mod.get_global_var('func_11279')
call_13103 = relay.TupleGetItem(func_11278_call(), 0)
call_13104 = relay.TupleGetItem(func_11279_call(), 0)
func_8518_call = mod.get_global_var('func_8518')
func_8519_call = mutated_mod.get_global_var('func_8519')
call_13107 = relay.TupleGetItem(func_8518_call(), 0)
call_13108 = relay.TupleGetItem(func_8519_call(), 0)
output = relay.Tuple([call_13073,call_13103,call_13107,])
output2 = relay.Tuple([call_13074,call_13104,call_13108,])
func_13112 = relay.Function([], output)
mod['func_13112'] = func_13112
mod = relay.transform.InferType()(mod)
mutated_mod['func_13112'] = func_13112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13112_call = mutated_mod.get_global_var('func_13112')
call_13113 = func_13112_call()
output = call_13113
func_13114 = relay.Function([], output)
mutated_mod['func_13114'] = func_13114
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13144 = relay.var("var_13144", dtype = "uint32", shape = (3, 7, 16))#candidate|13144|(3, 7, 16)|var|uint32
var_13145 = relay.var("var_13145", dtype = "uint32", shape = (3, 7, 16))#candidate|13145|(3, 7, 16)|var|uint32
bop_13146 = relay.bitwise_xor(var_13144.astype('uint32'), relay.reshape(var_13145.astype('uint32'), relay.shape_of(var_13144))) # shape=(3, 7, 16)
uop_13151 = relay.sinh(var_13145.astype('float64')) # shape=(3, 7, 16)
uop_13153 = relay.sigmoid(uop_13151.astype('float32')) # shape=(3, 7, 16)
func_5820_call = mod.get_global_var('func_5820')
func_5821_call = mutated_mod.get_global_var('func_5821')
call_13157 = func_5820_call()
call_13158 = func_5820_call()
output = relay.Tuple([bop_13146,uop_13153,call_13157,])
output2 = relay.Tuple([bop_13146,uop_13153,call_13158,])
func_13161 = relay.Function([var_13144,var_13145,], output)
mod['func_13161'] = func_13161
mod = relay.transform.InferType()(mod)
var_13162 = relay.var("var_13162", dtype = "uint32", shape = (3, 7, 16))#candidate|13162|(3, 7, 16)|var|uint32
var_13163 = relay.var("var_13163", dtype = "uint32", shape = (3, 7, 16))#candidate|13163|(3, 7, 16)|var|uint32
output = func_13161(var_13162,var_13163,)
func_13164 = relay.Function([var_13162,var_13163,], output)
mutated_mod['func_13164'] = func_13164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4035_call = mod.get_global_var('func_4035')
func_4036_call = mutated_mod.get_global_var('func_4036')
call_13169 = func_4035_call()
call_13170 = func_4035_call()
func_2634_call = mod.get_global_var('func_2634')
func_2637_call = mutated_mod.get_global_var('func_2637')
var_13175 = relay.var("var_13175", dtype = "float64", shape = (48,))#candidate|13175|(48,)|var|float64
call_13174 = func_2634_call(relay.reshape(var_13175.astype('float64'), [2, 3, 8]))
call_13176 = func_2634_call(relay.reshape(var_13175.astype('float64'), [2, 3, 8]))
output = relay.Tuple([call_13169,call_13174,var_13175,])
output2 = relay.Tuple([call_13170,call_13176,var_13175,])
func_13181 = relay.Function([var_13175,], output)
mod['func_13181'] = func_13181
mod = relay.transform.InferType()(mod)
var_13182 = relay.var("var_13182", dtype = "float64", shape = (48,))#candidate|13182|(48,)|var|float64
output = func_13181(var_13182)
func_13183 = relay.Function([var_13182], output)
mutated_mod['func_13183'] = func_13183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9328_call = mod.get_global_var('func_9328')
func_9329_call = mutated_mod.get_global_var('func_9329')
call_13258 = relay.TupleGetItem(func_9328_call(), 0)
call_13259 = relay.TupleGetItem(func_9329_call(), 0)
func_3803_call = mod.get_global_var('func_3803')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_13262 = func_3803_call()
call_13263 = func_3803_call()
func_12795_call = mod.get_global_var('func_12795')
func_12797_call = mutated_mod.get_global_var('func_12797')
call_13273 = relay.TupleGetItem(func_12795_call(), 0)
call_13274 = relay.TupleGetItem(func_12797_call(), 0)
output = relay.Tuple([call_13258,call_13262,call_13273,])
output2 = relay.Tuple([call_13259,call_13263,call_13274,])
func_13289 = relay.Function([], output)
mod['func_13289'] = func_13289
mod = relay.transform.InferType()(mod)
output = func_13289()
func_13290 = relay.Function([], output)
mutated_mod['func_13290'] = func_13290
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13314 = relay.const([[[5.815377,-6.385832,-5.307827,8.545216,3.628314]],[[1.143313,3.886423,1.455346,6.007057,2.365888]],[[-1.768759,-8.323842,0.463991,-1.641145,-9.946710]],[[4.353978,-3.081616,2.951301,-5.902833,-8.539695]],[[1.832180,9.149358,9.061081,7.711531,2.653960]],[[3.607689,-9.342007,-4.625381,5.916501,-1.349728]],[[-2.597544,-7.500756,7.370429,7.132032,-8.054321]],[[4.091235,-2.976085,-0.478734,1.668675,-9.838098]],[[-8.489178,-9.023929,-1.056745,-3.888905,-0.929550]],[[4.149334,-8.663689,7.958615,0.626488,-9.188143]],[[5.517979,3.048279,-2.798675,9.404746,2.949589]],[[-2.967992,-2.711220,-1.243439,-8.297311,-1.267088]],[[1.595081,2.254845,9.971601,4.983553,-6.550282]],[[3.165952,-9.223041,0.609767,-8.856231,-1.492423]]], dtype = "float64")#candidate|13314|(14, 1, 5)|const|float64
uop_13315 = relay.cos(const_13314.astype('float64')) # shape=(14, 1, 5)
output = relay.Tuple([uop_13315,])
output2 = relay.Tuple([uop_13315,])
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
