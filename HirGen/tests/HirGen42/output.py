import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_49 = relay.var("var_49", dtype = "float32", shape = (13, 13, 4))#candidate|49|(13, 13, 4)|var|float32
uop_50 = relay.sinh(var_49.astype('float32')) # shape=(13, 13, 4)
uop_52 = relay.sigmoid(uop_50.astype('float32')) # shape=(13, 13, 4)
output = relay.Tuple([uop_52,])
output2 = relay.Tuple([uop_52,])
func_60 = relay.Function([var_49,], output)
mod['func_60'] = func_60
mod = relay.transform.InferType()(mod)
mutated_mod['func_60'] = func_60
mutated_mod = relay.transform.InferType()(mutated_mod)
var_61 = relay.var("var_61", dtype = "float32", shape = (13, 13, 4))#candidate|61|(13, 13, 4)|var|float32
func_60_call = mutated_mod.get_global_var('func_60')
call_62 = func_60_call(var_61)
output = call_62
func_63 = relay.Function([var_61], output)
mutated_mod['func_63'] = func_63
mutated_mod = relay.transform.InferType()(mutated_mod)
var_270 = relay.var("var_270", dtype = "float32", shape = (1, 12, 5))#candidate|270|(1, 12, 5)|var|float32
const_271 = relay.const([[[-6.221556,9.148860,6.027681,9.205912,9.047352],[-3.547802,5.476695,-7.528533,3.938905,-6.738088],[-9.047243,4.516022,1.990441,-1.716914,-1.495710],[5.770027,4.228500,0.927010,3.568660,3.525887],[7.619400,8.539672,6.042185,-0.895495,-5.696011],[2.899756,0.792938,8.390128,2.369960,-0.670061],[6.551489,-2.949281,-8.040731,4.218912,-4.959174],[-1.196852,-2.945494,2.910256,-8.196683,6.292305],[-6.209839,7.011185,3.795934,-8.039645,-9.381305],[-1.527049,-3.934476,0.563411,8.061733,3.150449],[2.711910,1.662409,4.427718,-3.146638,4.741858],[-4.477675,-7.872469,3.576757,-4.671593,-7.956842]],[[1.853520,-0.529081,-1.421725,-9.731070,-8.559260],[7.646316,-8.531139,-8.844799,9.460689,8.734373],[-7.818502,-0.508844,5.814432,-7.580443,-0.861951],[6.918757,7.982312,9.760469,2.298972,5.653982],[3.704766,4.259537,-7.543058,7.928808,-9.046095],[-8.009375,7.710047,-2.483834,-6.166306,-3.735116],[0.473132,-3.926270,-4.929076,-0.673879,-0.573193],[7.494408,4.001789,0.882152,-6.352062,2.477448],[7.678969,3.550508,7.292878,0.336488,-5.497428],[-4.879075,4.018384,6.549643,-2.980091,0.986794],[9.085265,9.292159,-1.471660,-6.230049,1.066929],[3.987538,6.308039,5.886965,-4.937789,7.832806]],[[0.029305,7.043851,-0.720435,-7.335910,-2.861268],[3.857031,-9.368233,-9.079430,0.976716,-2.637651],[7.661844,0.412244,-3.204252,6.363521,-7.089658],[-2.755110,-0.401514,-0.141403,-2.247531,2.520121],[4.654984,-9.311221,5.488094,-1.454732,-8.929262],[-4.261103,-7.780510,-7.395976,-7.624361,-1.341112],[-1.871509,-6.043471,-9.565492,-9.714754,8.738447],[9.976336,-2.928127,7.877999,6.711052,2.203172],[-9.775403,3.886106,7.236186,6.228747,7.899092],[-3.451258,-9.495353,-6.544371,-6.932102,3.869767],[-2.794057,-0.724842,1.865853,5.000922,7.240604],[-1.673210,-9.633690,-2.657169,0.359085,4.019818]],[[5.364286,0.698585,3.686515,-5.562026,-1.031915],[8.881615,7.675334,6.551170,7.755858,9.331135],[9.719519,-5.727230,1.572372,-7.493084,4.490906],[9.953270,5.083598,-1.623887,-1.806930,-4.850779],[7.756018,4.839378,4.607452,7.822210,1.735183],[2.904712,-3.408820,-2.926142,6.698253,-7.014229],[4.876155,8.398314,-3.167763,7.369729,1.339947],[1.748697,8.690401,5.151555,-4.791348,-0.209517],[0.241912,-0.528762,7.724176,4.775646,3.742050],[4.852125,4.677200,-6.127795,8.949548,-8.224687],[8.036187,1.650295,-7.925390,-8.899760,1.844982],[8.852308,-9.543699,-8.900092,-6.963116,-9.603848]],[[0.632624,-8.182073,0.094014,6.465263,-6.444984],[7.839744,9.594318,5.991078,2.399844,-0.872914],[-2.094440,9.335531,-2.341219,-7.408650,1.434523],[-2.921743,1.805337,1.440630,3.962896,1.987154],[-3.988410,-8.331719,0.438115,1.272365,3.071166],[8.110602,2.220651,-7.808211,-8.583183,4.327590],[-5.549423,-9.973015,-8.216853,-1.170846,-5.620413],[-8.899761,-4.710511,5.664012,-5.960366,-1.864191],[-6.534146,9.727383,-3.497222,9.677751,-9.206404],[-0.212312,2.679988,-0.233030,-9.146867,2.607485],[-6.577695,6.936419,-6.542875,-7.760486,8.954029],[-9.333082,-2.639450,-0.045343,-7.367534,0.754425]],[[-5.288979,4.813820,0.276700,5.483682,-9.208505],[-7.589069,-6.591188,6.832766,-9.884879,8.556745],[-1.019773,-4.828859,7.540944,4.918074,-8.082440],[9.837263,-4.919205,-2.829369,-2.029211,4.752933],[6.273965,-1.897275,5.105734,-5.798786,2.317191],[4.407014,-1.599400,4.123852,-0.361117,2.573495],[3.816737,4.040277,6.727100,9.302256,-1.865084],[-2.825105,6.574971,6.577506,-9.820850,-0.274113],[-9.173081,3.354450,3.256939,-7.992623,8.982252],[4.605149,-4.554329,-2.881675,-9.053367,-8.703210],[-5.821926,-1.724500,9.361681,-7.245730,-0.873512],[5.102934,-8.692163,9.102357,7.720289,-2.351011]],[[6.810031,-1.719092,-7.243581,8.979463,-1.673351],[8.617014,-7.154619,-1.579312,-9.186279,9.788077],[-2.615190,1.530254,1.659484,-8.107110,-1.009086],[8.908616,-2.227592,-1.632490,-3.396481,-5.791170],[3.865599,1.621956,0.056581,5.270275,-4.371587],[-0.316748,7.894900,2.118907,-2.853405,-1.795735],[-3.996334,-5.823144,2.436237,-3.490001,-8.929890],[-3.900813,-4.769204,5.754389,-5.344735,8.280829],[6.465568,9.275085,5.430282,0.945250,-3.712297],[8.606637,6.829733,-6.806661,-5.326138,-6.694990],[7.142455,-3.864179,-6.549198,9.029723,-2.145336],[8.497901,6.962159,-2.274280,-5.409678,-1.023783]],[[8.609313,1.738561,-2.013543,8.005941,-6.927665],[8.280154,3.363342,-2.193970,-4.302845,-6.596426],[-8.936250,-9.035738,-7.878836,6.424291,2.153193],[6.932788,1.203603,6.672558,-0.968605,-3.257251],[3.495623,-4.979283,7.389702,-5.640386,4.840682],[-9.784832,1.750859,0.326069,6.920959,-0.854733],[-5.999353,-7.006720,-2.061080,2.004879,-8.513535],[-8.654021,-3.020386,-1.920296,7.590451,3.538463],[2.064581,-8.383385,-2.451837,-5.608185,-0.799757],[-2.212254,7.364579,-9.595103,7.073373,-6.037948],[9.140762,2.756478,-4.877420,7.414462,-0.919825],[-3.366184,-0.472570,-6.188039,-2.149055,1.756919]],[[8.013870,9.320019,-4.791812,3.282228,-6.667928],[0.609255,-9.171676,8.688341,6.631986,-5.958118],[0.685696,0.525254,2.044502,-2.877386,0.145029],[8.152394,-0.229907,6.963597,-7.724612,-8.262885],[-6.002262,8.682910,-3.038938,9.514223,2.805220],[2.347923,-1.221681,7.666391,5.961287,1.429125],[1.307099,2.923348,-5.341575,-2.429560,0.625959],[3.159372,-3.660074,-7.573913,9.762906,-4.132297],[2.701344,0.095262,6.513436,-0.577112,-3.849518],[3.227235,-7.832134,7.808838,2.201223,0.508741],[-9.159292,-5.829709,1.497752,6.122757,9.582099],[-0.012317,-3.293274,-7.733633,-5.432246,-8.870322]],[[7.219129,-8.559135,-2.497179,-2.188857,7.248197],[6.300421,-6.003267,-2.107352,-0.755141,-2.903220],[-2.893529,0.147291,-1.496805,-8.047412,-1.057989],[4.878345,-6.387714,6.674901,-9.236152,-5.415038],[3.047581,3.700632,5.493741,-2.757556,-6.766471],[4.950253,5.725557,0.567555,4.049983,-6.877198],[-8.789812,4.678360,3.910790,0.080997,-2.113977],[1.001143,8.278768,2.632795,-4.513461,7.790047],[-0.501454,2.811247,1.920195,5.868261,-0.274982],[-3.938839,1.006785,1.262480,-5.225911,-3.816937],[-6.651792,-1.793155,0.400046,0.695630,5.091060],[-4.653877,8.367502,0.587123,-1.375105,0.305435]],[[-9.723846,9.646506,4.018659,-4.085784,9.960997],[-4.707642,-2.755890,-3.000139,-1.202387,-5.728893],[-2.548766,8.599203,-3.283141,-0.689886,1.229771],[-7.088621,9.136233,-2.181220,-1.051461,-2.342575],[1.326974,-2.680592,0.489071,5.292494,-3.265368],[-9.476235,-4.584152,-4.629494,-6.665305,8.387933],[4.044104,-5.235091,5.438246,5.280675,8.897349],[-2.660277,7.196879,7.575951,6.349751,-0.121008],[-5.941835,-4.095222,8.592060,1.823614,1.686779],[5.357329,-7.248913,1.592646,-3.580047,-0.335410],[-9.078289,5.492600,9.880481,-8.313401,9.434312],[-3.794607,3.442697,1.042793,2.463695,6.955741]],[[8.917738,6.217326,-4.609160,-1.310432,-6.818037],[-3.156607,8.423611,-1.788108,-1.269575,4.743695],[1.635986,3.788294,-6.350295,5.672601,-6.838078],[-2.156876,-6.745546,7.787263,-7.918637,0.947329],[-5.037557,0.663111,8.465934,-1.183367,-3.094644],[-6.641268,1.731545,9.247697,-8.940870,-7.987902],[8.562620,-7.427851,-7.606336,-2.830105,8.758979],[8.576264,6.782236,1.512256,-4.075566,4.700043],[6.737833,3.147611,4.044345,-9.327049,7.087452],[-8.193793,2.896912,-9.474232,8.994563,-4.882931],[2.376415,-1.977618,-8.794236,3.535596,-8.438569],[-1.239212,-9.104433,-1.031680,-3.474160,4.665465]],[[3.900874,-6.030751,2.013078,3.725798,4.981585],[3.343700,0.943885,7.738632,-0.384735,2.261653],[0.985024,-9.160718,9.673804,-0.087359,-0.554475],[1.465269,0.570265,-7.931334,9.256832,1.609564],[-8.006942,3.938362,6.103742,6.683138,1.153061],[-1.183530,-1.347462,4.645908,7.122118,2.777062],[6.751814,-7.383902,-1.576194,7.557603,-6.066376],[-8.548899,-4.727415,-5.845585,4.113037,8.516210],[-2.701079,1.920251,-3.260297,-7.421986,-2.611510],[2.334754,8.986966,0.292656,7.172935,4.033266],[8.309763,-4.858467,9.056867,0.586662,-9.406212],[8.699829,-4.489098,-6.409581,5.181150,5.176996]],[[-3.885204,-0.207687,-5.732597,-6.556494,-3.569658],[9.045987,0.319894,8.705954,-5.312206,0.381271],[5.497459,-4.007510,-6.115367,5.938067,5.537545],[3.455981,1.774657,9.520158,5.138896,7.450530],[4.359812,-5.548338,-1.833163,0.129923,-3.874711],[-0.555029,-7.647430,-0.039885,7.480698,-5.017030],[-7.223155,-2.841343,9.238144,0.136977,1.791476],[7.816267,2.978005,-5.908562,5.493004,-9.730010],[-0.200996,-9.490948,5.332373,4.063109,-1.648163],[-0.386848,-7.308589,-6.554080,-9.406008,-6.923459],[7.174974,2.985501,4.815878,-9.301929,6.331581],[4.377962,1.350223,-0.523269,-6.541616,0.387533]],[[-9.439528,3.422235,8.967565,-1.641088,0.126372],[6.061912,-4.944920,5.221502,-3.815385,8.271446],[-4.352662,-5.740122,-3.169797,9.740876,-3.033263],[8.971482,-9.978666,8.733064,-4.444513,1.102362],[4.604300,-4.347027,3.816052,3.275811,-6.291911],[-1.670487,9.611204,-1.971634,6.668804,-5.581372],[1.231561,-2.756003,-6.555085,6.874097,-7.116486],[-7.036962,2.737894,2.412897,-5.031788,5.751062],[0.522154,-4.410376,-6.160567,-5.506077,-7.612443],[5.962818,-3.747717,7.235037,-4.664505,-0.490415],[2.209966,-4.299931,7.906803,-1.223912,-2.889799],[-3.864716,5.349804,7.001466,-7.133403,7.133034]],[[-0.538664,-5.104857,1.634707,-1.847816,-4.183094],[-6.894689,7.873513,-8.523653,-9.457646,0.512317],[-7.106013,6.825125,-0.126045,1.916117,-7.514624],[7.656357,-5.758718,-5.777612,0.126723,9.238786],[3.327235,3.765603,-0.601219,2.857834,-7.726808],[7.049960,6.930248,-9.867028,4.092844,-4.926681],[0.326208,2.913009,5.734730,2.976029,-6.153488],[-0.310392,-1.176919,-6.944662,1.310215,1.026279],[-3.045521,7.767275,4.206110,0.333106,5.922210],[9.388479,8.839278,-5.025159,-1.260348,2.898458],[-1.512273,-2.108497,-6.458478,4.614366,-3.667638],[0.661679,-7.844352,-7.571860,6.437539,-0.766311]]], dtype = "float32")#candidate|271|(16, 12, 5)|const|float32
bop_272 = relay.greater(var_270.astype('bool'), const_271.astype('bool')) # shape=(16, 12, 5)
uop_276 = relay.rsqrt(bop_272.astype('float32')) # shape=(16, 12, 5)
output = uop_276
output2 = uop_276
func_278 = relay.Function([var_270,], output)
mod['func_278'] = func_278
mod = relay.transform.InferType()(mod)
mutated_mod['func_278'] = func_278
mutated_mod = relay.transform.InferType()(mutated_mod)
var_279 = relay.var("var_279", dtype = "float32", shape = (1, 12, 5))#candidate|279|(1, 12, 5)|var|float32
func_278_call = mutated_mod.get_global_var('func_278')
call_280 = func_278_call(var_279)
output = call_280
func_281 = relay.Function([var_279], output)
mutated_mod['func_281'] = func_281
mutated_mod = relay.transform.InferType()(mutated_mod)
const_368 = relay.const([[[1,10,5,-1,3,4,8,7],[1,1,2,-9,10,3,-3,-5],[-1,6,-1,4,4,-10,-3,4]],[[-4,1,8,8,4,-7,8,-3],[8,-4,-10,-5,-6,5,-3,-1],[-5,-6,-4,2,-8,9,2,5]],[[-3,3,7,6,-2,-3,1,5],[-8,-8,5,-4,-10,9,5,5],[2,1,-3,-5,9,1,1,5]],[[-7,6,2,5,3,5,-7,-5],[-6,10,-3,-6,2,10,5,5],[-8,-4,-10,-4,4,-10,2,1]]], dtype = "int64")#candidate|368|(4, 3, 8)|const|int64
var_369 = relay.var("var_369", dtype = "int64", shape = (4, 3, 8))#candidate|369|(4, 3, 8)|var|int64
bop_370 = relay.left_shift(const_368.astype('int64'), relay.reshape(var_369.astype('int64'), relay.shape_of(const_368))) # shape=(4, 3, 8)
output = bop_370
output2 = bop_370
func_383 = relay.Function([var_369,], output)
mod['func_383'] = func_383
mod = relay.transform.InferType()(mod)
mutated_mod['func_383'] = func_383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_384 = relay.var("var_384", dtype = "int64", shape = (4, 3, 8))#candidate|384|(4, 3, 8)|var|int64
func_383_call = mutated_mod.get_global_var('func_383')
call_385 = func_383_call(var_384)
output = call_385
func_386 = relay.Function([var_384], output)
mutated_mod['func_386'] = func_386
mutated_mod = relay.transform.InferType()(mutated_mod)
var_396 = relay.var("var_396", dtype = "float32", shape = (13, 3, 11))#candidate|396|(13, 3, 11)|var|float32
uop_397 = relay.atanh(var_396.astype('float32')) # shape=(13, 3, 11)
func_60_call = mod.get_global_var('func_60')
func_63_call = mutated_mod.get_global_var('func_63')
var_404 = relay.var("var_404", dtype = "float32", shape = (676,))#candidate|404|(676,)|var|float32
call_403 = relay.TupleGetItem(func_60_call(relay.reshape(var_404.astype('float32'), [13, 13, 4])), 0)
call_405 = relay.TupleGetItem(func_63_call(relay.reshape(var_404.astype('float32'), [13, 13, 4])), 0)
output = relay.Tuple([uop_397,call_403,var_404,])
output2 = relay.Tuple([uop_397,call_405,var_404,])
func_408 = relay.Function([var_396,var_404,], output)
mod['func_408'] = func_408
mod = relay.transform.InferType()(mod)
var_409 = relay.var("var_409", dtype = "float32", shape = (13, 3, 11))#candidate|409|(13, 3, 11)|var|float32
var_410 = relay.var("var_410", dtype = "float32", shape = (676,))#candidate|410|(676,)|var|float32
output = func_408(var_409,var_410,)
func_411 = relay.Function([var_409,var_410,], output)
mutated_mod['func_411'] = func_411
mutated_mod = relay.transform.InferType()(mutated_mod)
var_516 = relay.var("var_516", dtype = "float32", shape = (4, 11, 16))#candidate|516|(4, 11, 16)|var|float32
uop_517 = relay.cosh(var_516.astype('float32')) # shape=(4, 11, 16)
output = relay.Tuple([uop_517,])
output2 = relay.Tuple([uop_517,])
func_529 = relay.Function([var_516,], output)
mod['func_529'] = func_529
mod = relay.transform.InferType()(mod)
var_530 = relay.var("var_530", dtype = "float32", shape = (4, 11, 16))#candidate|530|(4, 11, 16)|var|float32
output = func_529(var_530)
func_531 = relay.Function([var_530], output)
mutated_mod['func_531'] = func_531
mutated_mod = relay.transform.InferType()(mutated_mod)
var_555 = relay.var("var_555", dtype = "uint64", shape = (8, 4, 5))#candidate|555|(8, 4, 5)|var|uint64
var_556 = relay.var("var_556", dtype = "uint64", shape = (8, 4, 5))#candidate|556|(8, 4, 5)|var|uint64
bop_557 = relay.greater_equal(var_555.astype('bool'), relay.reshape(var_556.astype('bool'), relay.shape_of(var_555))) # shape=(8, 4, 5)
func_278_call = mod.get_global_var('func_278')
func_281_call = mutated_mod.get_global_var('func_281')
var_564 = relay.var("var_564", dtype = "float32", shape = (60,))#candidate|564|(60,)|var|float32
call_563 = func_278_call(relay.reshape(var_564.astype('float32'), [1, 12, 5]))
call_565 = func_278_call(relay.reshape(var_564.astype('float32'), [1, 12, 5]))
output = relay.Tuple([bop_557,call_563,var_564,])
output2 = relay.Tuple([bop_557,call_565,var_564,])
func_571 = relay.Function([var_555,var_556,var_564,], output)
mod['func_571'] = func_571
mod = relay.transform.InferType()(mod)
mutated_mod['func_571'] = func_571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_571_call = mutated_mod.get_global_var('func_571')
var_573 = relay.var("var_573", dtype = "uint64", shape = (8, 4, 5))#candidate|573|(8, 4, 5)|var|uint64
var_574 = relay.var("var_574", dtype = "uint64", shape = (8, 4, 5))#candidate|574|(8, 4, 5)|var|uint64
var_575 = relay.var("var_575", dtype = "float32", shape = (60,))#candidate|575|(60,)|var|float32
call_572 = func_571_call(var_573,var_574,var_575,)
output = call_572
func_576 = relay.Function([var_573,var_574,var_575,], output)
mutated_mod['func_576'] = func_576
mutated_mod = relay.transform.InferType()(mutated_mod)
var_615 = relay.var("var_615", dtype = "float32", shape = (4, 8, 12))#candidate|615|(4, 8, 12)|var|float32
var_616 = relay.var("var_616", dtype = "float32", shape = (4, 8, 12))#candidate|616|(4, 8, 12)|var|float32
bop_617 = relay.mod(var_615.astype('float32'), relay.reshape(var_616.astype('float32'), relay.shape_of(var_615))) # shape=(4, 8, 12)
output = relay.Tuple([bop_617,])
output2 = relay.Tuple([bop_617,])
func_620 = relay.Function([var_615,var_616,], output)
mod['func_620'] = func_620
mod = relay.transform.InferType()(mod)
var_621 = relay.var("var_621", dtype = "float32", shape = (4, 8, 12))#candidate|621|(4, 8, 12)|var|float32
var_622 = relay.var("var_622", dtype = "float32", shape = (4, 8, 12))#candidate|622|(4, 8, 12)|var|float32
output = func_620(var_621,var_622,)
func_623 = relay.Function([var_621,var_622,], output)
mutated_mod['func_623'] = func_623
mutated_mod = relay.transform.InferType()(mutated_mod)
var_637 = relay.var("var_637", dtype = "float32", shape = (15, 10, 11))#candidate|637|(15, 10, 11)|var|float32
var_638 = relay.var("var_638", dtype = "float32", shape = (15, 10, 11))#candidate|638|(15, 10, 11)|var|float32
bop_639 = relay.less(var_637.astype('bool'), relay.reshape(var_638.astype('bool'), relay.shape_of(var_637))) # shape=(15, 10, 11)
func_383_call = mod.get_global_var('func_383')
func_386_call = mutated_mod.get_global_var('func_386')
var_647 = relay.var("var_647", dtype = "int64", shape = (48, 2))#candidate|647|(48, 2)|var|int64
call_646 = func_383_call(relay.reshape(var_647.astype('int64'), [4, 3, 8]))
call_648 = func_383_call(relay.reshape(var_647.astype('int64'), [4, 3, 8]))
func_571_call = mod.get_global_var('func_571')
func_576_call = mutated_mod.get_global_var('func_576')
var_664 = relay.var("var_664", dtype = "uint64", shape = (160,))#candidate|664|(160,)|var|uint64
const_665 = relay.const([[4.530882,-1.201349],[3.830265,-5.136576],[-4.326420,6.560143],[-9.795551,8.367302],[-5.627185,1.879703],[1.997356,-6.924378],[2.938843,3.666268],[1.669778,4.697502],[-0.206569,9.868256],[-6.706282,8.514435],[-5.233476,0.034475],[-6.093349,3.002767],[-7.265292,3.383125],[-4.513805,-3.866581],[6.402183,-3.013218],[-6.904366,2.304782],[5.219564,-2.306505],[-4.618525,-1.662066],[-1.234723,0.612871],[-7.802478,9.091312],[-8.190720,-9.899457],[-8.343501,-4.045320],[-8.205214,6.995357],[-9.662375,-7.431537],[7.411478,-0.474684],[-7.669331,-6.029795],[-7.850966,3.250773],[-5.305415,-7.213377],[2.622152,-1.418180],[3.333729,-5.945923]], dtype = "float32")#candidate|665|(30, 2)|const|float32
call_663 = relay.TupleGetItem(func_571_call(relay.reshape(var_664.astype('uint64'), [8, 4, 5]), relay.reshape(var_664.astype('uint64'), [8, 4, 5]), relay.reshape(const_665.astype('float32'), [60,]), ), 1)
call_666 = relay.TupleGetItem(func_576_call(relay.reshape(var_664.astype('uint64'), [8, 4, 5]), relay.reshape(var_664.astype('uint64'), [8, 4, 5]), relay.reshape(const_665.astype('float32'), [60,]), ), 1)
output = relay.Tuple([bop_639,call_646,var_647,call_663,var_664,const_665,])
output2 = relay.Tuple([bop_639,call_648,var_647,call_666,var_664,const_665,])
func_670 = relay.Function([var_637,var_638,var_647,var_664,], output)
mod['func_670'] = func_670
mod = relay.transform.InferType()(mod)
var_671 = relay.var("var_671", dtype = "float32", shape = (15, 10, 11))#candidate|671|(15, 10, 11)|var|float32
var_672 = relay.var("var_672", dtype = "float32", shape = (15, 10, 11))#candidate|672|(15, 10, 11)|var|float32
var_673 = relay.var("var_673", dtype = "int64", shape = (48, 2))#candidate|673|(48, 2)|var|int64
var_674 = relay.var("var_674", dtype = "uint64", shape = (160,))#candidate|674|(160,)|var|uint64
output = func_670(var_671,var_672,var_673,var_674,)
func_675 = relay.Function([var_671,var_672,var_673,var_674,], output)
mutated_mod['func_675'] = func_675
mutated_mod = relay.transform.InferType()(mutated_mod)
var_759 = relay.var("var_759", dtype = "int64", shape = ())#candidate|759|()|var|int64
var_760 = relay.var("var_760", dtype = "int64", shape = (11, 16, 15))#candidate|760|(11, 16, 15)|var|int64
bop_761 = relay.less_equal(var_759.astype('bool'), var_760.astype('bool')) # shape=(11, 16, 15)
func_60_call = mod.get_global_var('func_60')
func_63_call = mutated_mod.get_global_var('func_63')
var_772 = relay.var("var_772", dtype = "float32", shape = (676,))#candidate|772|(676,)|var|float32
call_771 = relay.TupleGetItem(func_60_call(relay.reshape(var_772.astype('float32'), [13, 13, 4])), 0)
call_773 = relay.TupleGetItem(func_63_call(relay.reshape(var_772.astype('float32'), [13, 13, 4])), 0)
output = relay.Tuple([bop_761,call_771,var_772,])
output2 = relay.Tuple([bop_761,call_773,var_772,])
func_776 = relay.Function([var_759,var_760,var_772,], output)
mod['func_776'] = func_776
mod = relay.transform.InferType()(mod)
var_777 = relay.var("var_777", dtype = "int64", shape = ())#candidate|777|()|var|int64
var_778 = relay.var("var_778", dtype = "int64", shape = (11, 16, 15))#candidate|778|(11, 16, 15)|var|int64
var_779 = relay.var("var_779", dtype = "float32", shape = (676,))#candidate|779|(676,)|var|float32
output = func_776(var_777,var_778,var_779,)
func_780 = relay.Function([var_777,var_778,var_779,], output)
mutated_mod['func_780'] = func_780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_805 = relay.var("var_805", dtype = "float32", shape = (10, 3, 6))#candidate|805|(10, 3, 6)|var|float32
uop_806 = relay.log10(var_805.astype('float32')) # shape=(10, 3, 6)
bop_808 = relay.not_equal(var_805.astype('bool'), relay.reshape(uop_806.astype('bool'), relay.shape_of(var_805))) # shape=(10, 3, 6)
output = bop_808
output2 = bop_808
func_814 = relay.Function([var_805,], output)
mod['func_814'] = func_814
mod = relay.transform.InferType()(mod)
var_815 = relay.var("var_815", dtype = "float32", shape = (10, 3, 6))#candidate|815|(10, 3, 6)|var|float32
output = func_814(var_815)
func_816 = relay.Function([var_815], output)
mutated_mod['func_816'] = func_816
mutated_mod = relay.transform.InferType()(mutated_mod)
var_922 = relay.var("var_922", dtype = "uint64", shape = (2, 3, 14))#candidate|922|(2, 3, 14)|var|uint64
var_923 = relay.var("var_923", dtype = "uint64", shape = (2, 3, 14))#candidate|923|(2, 3, 14)|var|uint64
bop_924 = relay.add(var_922.astype('uint64'), relay.reshape(var_923.astype('uint64'), relay.shape_of(var_922))) # shape=(2, 3, 14)
var_928 = relay.var("var_928", dtype = "uint64", shape = (2, 3, 14))#candidate|928|(2, 3, 14)|var|uint64
bop_929 = relay.equal(var_923.astype('bool'), relay.reshape(var_928.astype('bool'), relay.shape_of(var_923))) # shape=(2, 3, 14)
func_670_call = mod.get_global_var('func_670')
func_675_call = mutated_mod.get_global_var('func_675')
var_938 = relay.var("var_938", dtype = "float32", shape = (1650,))#candidate|938|(1650,)|var|float32
const_939 = relay.const([-1,-10,-2,-8,-1,-5,-1,-2,-10,10,3,-1,7,5,1,9,-7,-7,-3,5,5,8,6,8,2,-6,-6,-3,3,4,-4,-6,-3,9,7,9,-1,-1,-4,7,-5,-2,-1,3,-2,6,9,6,-4,-7,8,-4,-2,10,-1,3,-1,6,-9,-4,5,9,-1,-7,2,5,-1,-9,-5,10,-5,2,9,7,-9,9,2,-10,-4,9,1,6,-6,-5,-5,5,-10,-7,8,-5,7,-1,-3,-6,-7,3], dtype = "int64")#candidate|939|(96,)|const|int64
const_940 = relay.const([[6,-6,9,2,10,-5,8,-6,-7,4,2,2,1,-1,-9,1,-4,-2,10,-10],[-3,-1,-7,5,-7,-1,-4,8,3,6,-10,-7,-5,-5,2,-7,4,-8,-4,-5],[4,9,3,5,-9,-7,-9,3,-3,1,8,10,6,3,1,-1,5,2,9,3],[-8,7,5,3,10,3,4,8,-1,1,8,-4,-4,-1,4,1,4,-9,-9,7],[6,7,-3,-9,-5,-4,-4,8,-5,-3,4,-8,3,7,10,1,-4,-8,-3,-9],[9,3,-2,-5,1,5,-3,4,-2,10,-7,-2,9,-7,-8,3,2,3,9,10],[-6,-7,-1,9,-4,-9,-1,-3,10,-3,6,4,-3,1,-4,4,-7,-1,4,4],[-8,-10,-2,9,10,-10,9,-6,2,-4,8,6,-1,-6,8,4,10,5,4,6]], dtype = "uint64")#candidate|940|(8, 20)|const|uint64
call_937 = relay.TupleGetItem(func_670_call(relay.reshape(var_938.astype('float32'), [15, 10, 11]), relay.reshape(var_938.astype('float32'), [15, 10, 11]), relay.reshape(const_939.astype('int64'), [48, 2]), relay.reshape(const_940.astype('uint64'), [160,]), ), 2)
call_941 = relay.TupleGetItem(func_675_call(relay.reshape(var_938.astype('float32'), [15, 10, 11]), relay.reshape(var_938.astype('float32'), [15, 10, 11]), relay.reshape(const_939.astype('int64'), [48, 2]), relay.reshape(const_940.astype('uint64'), [160,]), ), 2)
uop_946 = relay.acos(bop_924.astype('float32')) # shape=(2, 3, 14)
var_949 = relay.var("var_949", dtype = "float32", shape = (1650,))#candidate|949|(1650,)|var|float32
bop_950 = relay.divide(var_938.astype('float64'), relay.reshape(var_949.astype('float64'), relay.shape_of(var_938))) # shape=(1650,)
output = relay.Tuple([bop_929,call_937,const_939,const_940,uop_946,bop_950,])
output2 = relay.Tuple([bop_929,call_941,const_939,const_940,uop_946,bop_950,])
func_967 = relay.Function([var_922,var_923,var_928,var_938,var_949,], output)
mod['func_967'] = func_967
mod = relay.transform.InferType()(mod)
var_968 = relay.var("var_968", dtype = "uint64", shape = (2, 3, 14))#candidate|968|(2, 3, 14)|var|uint64
var_969 = relay.var("var_969", dtype = "uint64", shape = (2, 3, 14))#candidate|969|(2, 3, 14)|var|uint64
var_970 = relay.var("var_970", dtype = "uint64", shape = (2, 3, 14))#candidate|970|(2, 3, 14)|var|uint64
var_971 = relay.var("var_971", dtype = "float32", shape = (1650,))#candidate|971|(1650,)|var|float32
var_972 = relay.var("var_972", dtype = "float32", shape = (1650,))#candidate|972|(1650,)|var|float32
output = func_967(var_968,var_969,var_970,var_971,var_972,)
func_973 = relay.Function([var_968,var_969,var_970,var_971,var_972,], output)
mutated_mod['func_973'] = func_973
mutated_mod = relay.transform.InferType()(mutated_mod)
const_975 = relay.const([[[True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True],[True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False],[False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True],[True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,True],[False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False],[True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True],[False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True],[True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True],[False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False],[True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,True],[True,False,True,True,True,True,True,False,False,False,False,True,False,False,True,True],[True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True],[True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,False],[False,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False],[True,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False]],[[False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False],[True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True],[False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False],[True,False,True,True,True,True,True,False,True,False,True,False,False,False,False,False],[True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False],[True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False],[False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True],[False,False,True,False,True,False,True,False,True,True,True,False,True,False,False,True],[False,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False],[False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True],[False,False,True,True,True,True,False,False,False,True,False,True,True,False,True,True],[False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True],[True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False],[False,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True],[True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False]],[[True,False,True,True,True,True,False,True,True,True,False,True,False,False,False,True],[False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False],[True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False],[False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True],[False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False],[False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True],[True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True],[False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True],[True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True],[True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False],[False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True],[True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True],[False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False],[False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True],[False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,True]],[[False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False],[True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,False],[False,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True],[True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,True],[True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True],[True,False,False,True,True,True,True,True,False,True,True,True,False,False,False,True],[False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False],[True,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True],[True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True],[False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True],[True,False,True,True,False,True,True,True,False,True,True,False,False,True,True,True],[False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False],[True,False,True,True,True,True,False,False,False,True,False,True,False,False,False,False],[True,False,True,True,True,False,False,False,True,True,True,False,False,True,True,True],[True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False]],[[True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False],[False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,True],[False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,True],[False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True],[False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False],[False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False],[False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True],[True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False],[False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True],[True,False,False,False,True,False,False,False,False,False,False,True,True,False,True,True],[True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False],[True,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False],[True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False],[True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True],[False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,True]],[[True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False],[True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,True],[True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False],[False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True],[True,False,True,True,False,True,True,True,False,True,True,True,False,False,True,True],[True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True],[False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False],[False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True],[True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False],[False,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True],[True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True],[True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False],[False,False,True,False,False,True,False,True,True,False,True,False,False,False,True,False],[True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True],[True,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False]],[[True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True],[False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,False],[True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True],[True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True],[True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,True],[False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True],[False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,True],[True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,True],[True,True,False,False,False,True,False,False,False,True,True,True,False,False,False,False],[False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False],[True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,True],[True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True],[True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True],[True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True],[True,False,True,False,True,True,True,True,True,True,True,True,True,False,True,False]],[[False,True,True,True,False,False,False,True,True,False,True,False,False,True,True,True],[False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True],[False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False],[False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True],[False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False],[False,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True],[True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,True],[False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True],[False,False,True,False,False,True,False,True,True,False,True,True,False,False,False,False],[True,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False],[False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False],[True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,True],[False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False],[True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False],[False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,True]],[[True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True],[True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True],[True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False],[False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,True],[True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True],[False,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False],[True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True],[False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True],[True,True,False,True,False,False,False,True,True,False,True,False,True,False,True,False],[False,True,False,False,True,True,False,True,False,False,True,False,True,True,True,True],[False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False],[False,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True],[False,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True],[True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,False],[True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False]],[[False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False],[False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False],[True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False],[False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True],[False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True],[True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,False],[False,False,True,False,False,True,False,True,True,True,False,True,True,True,False,False],[True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True],[False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,True],[True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True],[True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True],[False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False],[False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,True],[False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True],[False,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False]],[[True,False,True,True,False,False,False,False,False,False,False,False,False,True,True,False],[True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True],[True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False],[False,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False],[True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False],[True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True],[False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False],[False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False],[False,True,False,False,False,True,True,False,False,False,True,True,True,True,False,True],[True,True,True,True,True,True,True,False,False,False,True,False,False,False,False,False],[True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False],[True,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False],[False,True,True,False,True,True,False,False,False,False,False,True,False,True,True,True],[False,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True],[True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False]],[[False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False],[False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False],[True,True,False,False,False,False,False,False,False,True,True,True,True,True,True,True],[False,True,False,False,False,True,True,False,False,False,True,False,True,True,True,False],[False,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False],[True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,False],[False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False],[True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,False],[False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False],[True,True,False,False,True,True,True,True,True,True,False,True,False,True,True,False],[True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False],[False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False],[False,True,True,False,True,False,False,False,True,True,True,False,False,True,False,False],[True,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True],[False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False]],[[False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,False],[False,True,False,True,True,False,True,False,False,True,False,True,True,True,True,True],[False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True],[True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False],[False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False],[True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True],[True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False],[False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False],[False,True,True,False,False,False,True,True,False,False,False,True,False,True,False,False],[False,True,False,True,True,False,True,True,False,False,False,True,True,True,True,False],[False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,True],[False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,False],[True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,False],[False,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False],[False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True]],[[True,True,False,True,True,True,False,True,True,True,False,True,False,True,True,False],[True,False,False,False,False,True,False,False,True,False,True,False,True,True,False,True],[False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True],[True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False],[True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,False],[False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,True],[True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False],[False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True],[True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False],[False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False],[False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False],[True,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False],[False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False],[False,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True],[True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True]],[[True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False],[False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True],[True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True],[True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False],[True,True,False,False,True,False,False,False,False,False,True,False,False,False,True,True],[False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,False],[False,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True],[False,True,True,True,False,True,False,True,False,True,True,True,False,True,True,False],[False,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False],[False,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True],[False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True],[True,True,False,True,False,False,True,True,True,False,True,False,False,True,True,True],[True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False],[False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False],[False,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True]]], dtype = "bool")#candidate|975|(15, 15, 16)|const|bool
const_976 = relay.const([[[False,True,True,False,False,False,True,True,False,False,False,True,False,True,True,False],[False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True],[True,True,True,False,True,False,True,True,False,True,False,False,False,True,True,True],[False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False],[True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False],[False,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False],[True,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False],[False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True],[True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True],[True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,True],[False,True,False,True,True,False,True,False,False,True,True,True,True,False,False,False],[False,True,True,False,True,False,False,False,True,True,True,True,True,False,False,True],[False,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True],[True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,False],[True,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True]],[[True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False],[False,True,False,True,False,True,True,False,False,False,True,False,False,False,True,True],[False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True],[True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True],[True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False],[True,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True],[False,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False],[False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True],[False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,False],[True,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True],[True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True],[False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True],[True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False],[True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False],[False,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False]],[[False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True],[True,True,True,True,False,False,True,False,True,True,True,False,False,False,True,False],[False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False],[False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False],[True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False],[True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True],[True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,True],[True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False],[True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True],[False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False],[True,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False],[False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True],[False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True],[False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False],[True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True]],[[False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False],[True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,True,True,False,False,False,True,False,False,False],[True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False],[True,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False],[False,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True],[True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True],[True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,True],[False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True],[True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True],[False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,False],[False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False],[False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True],[True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,False],[False,False,False,True,False,False,True,True,False,False,False,False,False,False,True,True]],[[True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False],[True,True,True,True,True,True,False,True,True,True,True,True,True,True,False,False],[True,False,False,False,True,True,False,True,True,True,True,False,False,False,False,True],[True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,True],[False,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True],[True,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False],[True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True],[True,True,True,False,True,True,False,False,False,True,True,True,True,False,True,True],[True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False],[False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True],[True,False,False,False,True,True,False,True,False,False,True,True,True,True,False,False],[True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True],[True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True],[False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,False],[False,False,True,True,True,False,True,True,True,True,False,False,True,True,True,False]],[[False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False],[False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False],[True,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True],[False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True],[False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False],[False,True,False,False,True,False,False,False,False,False,True,True,True,False,False,True],[False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True],[False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False],[False,False,False,False,True,True,False,False,True,True,True,False,False,True,False,False],[False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True],[False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True],[False,True,True,False,True,True,True,True,False,False,True,False,True,True,True,True],[False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,True],[False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True],[False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True]],[[True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False],[True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,True],[True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,True],[True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True],[False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False],[False,True,False,False,False,True,True,False,False,False,True,False,False,True,True,False],[True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,False],[False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True],[False,False,False,True,True,True,False,True,True,False,False,True,True,True,True,False],[True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,False],[False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False],[True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False],[False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True],[True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True],[True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True]],[[True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True],[False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True],[False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True],[False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True],[False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,True],[True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False],[True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False],[True,True,False,False,False,True,False,False,False,True,False,False,False,False,False,True],[False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True],[False,False,True,False,True,True,True,False,False,True,False,False,True,True,True,False],[True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False],[False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,False],[False,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False],[True,False,False,False,False,False,True,True,True,True,True,False,True,False,True,True],[True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False]],[[False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True],[True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False],[True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True],[False,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True],[False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,False],[False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False],[True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False],[True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True],[False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True],[False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False],[True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False],[True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,False],[True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,False],[False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,False],[False,True,True,True,True,False,True,False,True,False,True,True,False,True,True,False]],[[True,False,True,False,False,False,True,True,False,True,False,True,False,False,True,False],[True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True],[False,False,True,True,False,False,False,False,True,False,True,False,False,False,False,False],[True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,True],[False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,False],[True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True],[True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False],[True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True],[True,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False],[False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True],[False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,False],[True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False],[False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False],[False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True],[True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False]],[[True,False,True,True,True,True,False,True,False,False,False,False,False,False,True,True],[False,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False],[False,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True],[True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False],[True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True],[False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False],[True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,False],[True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,False],[False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,True],[False,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False],[False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,True],[True,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False],[False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,True],[True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False],[False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False]],[[False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True],[False,False,False,False,True,False,False,True,True,True,False,False,False,True,True,True],[True,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False],[True,True,False,False,False,True,True,True,False,False,False,True,True,True,False,False],[True,False,False,False,True,True,False,False,True,True,True,True,False,False,False,True],[False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,False],[True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True],[False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True],[False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True],[True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,False],[True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False],[False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True],[False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False],[False,True,True,False,False,False,True,False,False,True,True,False,False,True,True,False],[True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True]],[[False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True],[True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True],[False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False],[True,False,False,False,True,False,False,False,True,False,False,False,False,False,True,False],[False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False],[False,False,False,True,False,True,False,True,True,False,True,True,False,False,False,True],[True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False],[False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False],[False,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True],[True,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True],[False,False,False,True,True,False,False,False,True,True,True,True,False,True,False,False],[True,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False],[True,False,True,False,False,True,False,False,True,True,True,True,True,True,True,False],[True,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True],[False,False,True,False,False,True,False,True,True,True,False,False,True,False,False,False]],[[False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False],[True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True],[True,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True],[True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False],[True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False],[False,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True],[False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True],[False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True],[False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True],[False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False],[True,True,True,False,True,True,True,True,True,True,False,False,False,True,False,True],[False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,True],[True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True],[False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,True],[False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False]],[[True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,True],[True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True],[False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True],[False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True],[True,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False],[False,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True],[False,False,True,False,True,True,False,False,True,False,True,False,True,False,False,True],[False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False],[True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,False],[True,False,True,False,False,True,True,True,True,False,False,True,True,False,True,False],[False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False],[False,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False],[True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,False],[True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True],[True,True,True,False,True,True,True,True,True,True,False,True,True,True,True,False]]], dtype = "bool")#candidate|976|(15, 15, 16)|const|bool
bop_977 = relay.logical_or(const_975.astype('bool'), relay.reshape(const_976.astype('bool'), relay.shape_of(const_975))) # shape=(15, 15, 16)
func_571_call = mod.get_global_var('func_571')
func_576_call = mutated_mod.get_global_var('func_576')
const_983 = relay.const([-2,10,5,-2,6,-9,2,7,3,7,-8,9,-5,8,-5,-7,-9,-8,2,-9,-5,-9,2,-10,-5,8,8,-9,-10,-5,10,-3,9,-7,-3,-1,3,-7,8,-2,6,8,9,9,4,6,5,5,1,7,6,-4,2,8,9,-2,-1,-9,8,10,1,6,-3,10,-4,-10,8,1,-3,9,10,7,2,2,3,1,-5,-9,-9,6,7,4,-10,-5,-6,7,4,7,-9,5,10,7,5,6,5,5,-8,7,-6,10,-7,-7,-10,-6,-5,2,-8,-1,-3,7,8,1,-3,-1,1,2,-10,-8,5,-1,6,6,-10,-7,3,-2,7,5,2,-10,9,2,1,2,-5,-6,6,-6,-8,-9,8,10,-5,-5,10,1,-5,1,-2,-2,7,7,-10,10,-6,7,-2,-9,-3,-5], dtype = "uint64")#candidate|983|(160,)|const|uint64
const_984 = relay.const([-0.425760,-6.781861,-6.723552,4.841009,4.637942,2.977660,-8.905025,-1.160172,-8.362092,-5.312687,-9.849272,-1.451831,2.899336,-3.422414,1.440261,-2.149847,9.256876,-0.013702,-6.650820,9.827610,-0.977127,0.833742,-1.671837,1.325534,1.587131,0.630840,-4.812501,-9.360344,-4.323578,-0.486557,-5.067292,3.655417,-0.641185,0.899032,5.631467,-0.596444,-7.533839,-2.913185,-4.729996,4.097367,-6.905016,4.751071,-4.641191,-9.227605,-2.135338,-9.671806,2.094858,-9.125870,7.416088,-1.844464,5.341287,-9.717448,-0.158613,-0.429902,5.819020,-4.825605,-8.964113,-2.188781,-5.740871,6.836752], dtype = "float32")#candidate|984|(60,)|const|float32
call_982 = relay.TupleGetItem(func_571_call(relay.reshape(const_983.astype('uint64'), [8, 4, 5]), relay.reshape(const_983.astype('uint64'), [8, 4, 5]), relay.reshape(const_984.astype('float32'), [60,]), ), 1)
call_985 = relay.TupleGetItem(func_576_call(relay.reshape(const_983.astype('uint64'), [8, 4, 5]), relay.reshape(const_983.astype('uint64'), [8, 4, 5]), relay.reshape(const_984.astype('float32'), [60,]), ), 1)
output = relay.Tuple([bop_977,call_982,const_983,const_984,])
output2 = relay.Tuple([bop_977,call_985,const_983,const_984,])
func_989 = relay.Function([], output)
mod['func_989'] = func_989
mod = relay.transform.InferType()(mod)
mutated_mod['func_989'] = func_989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mutated_mod.get_global_var('func_989')
call_990 = func_989_call()
output = call_990
func_991 = relay.Function([], output)
mutated_mod['func_991'] = func_991
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1017 = relay.const([[[-9.029766,-8.492979,-7.979509,7.900641,-1.943631,-3.528876,-0.121005,5.724180,-5.750714,-3.681526,-4.196827,9.221625,3.134035,-9.692865,3.903263,6.793450],[4.740629,-6.079527,-1.320868,-9.697004,9.726888,6.066461,-1.762922,1.130939,-1.020273,3.943133,-4.064324,-7.766891,4.143062,-7.479856,8.599528,4.995408],[2.999546,-8.318983,8.775002,-7.945667,-1.189634,-8.089754,7.359314,2.950111,-2.851826,-8.185579,-1.265045,-9.920609,5.585436,-3.295605,-4.046803,4.874267],[5.194883,9.563805,-1.482931,0.501061,0.427540,-3.355917,2.582940,-4.135499,-7.097635,-5.061201,3.913736,-5.391313,7.225564,4.286487,-5.288042,-8.745468],[9.730273,-8.277529,1.095918,-4.737925,-0.563765,6.997422,-9.018038,5.522500,-8.044392,8.083003,-6.092484,-6.913036,-9.349149,6.714140,-0.732240,-8.913555],[3.900002,-2.481190,-1.084088,2.143880,9.612602,-3.024286,-1.885737,-2.645701,-8.174180,-0.115071,4.316065,-0.109544,5.995545,9.375856,6.919295,5.358718],[-0.084788,-9.625702,-6.468574,1.124409,-4.489835,0.720366,4.519489,-7.545092,-7.893854,-7.268346,5.164205,7.150307,-5.197445,7.584416,1.462453,-1.734924]]], dtype = "float64")#candidate|1017|(1, 7, 16)|const|float64
uop_1018 = relay.acosh(const_1017.astype('float64')) # shape=(1, 7, 16)
output = uop_1018
output2 = uop_1018
func_1021 = relay.Function([], output)
mod['func_1021'] = func_1021
mod = relay.transform.InferType()(mod)
mutated_mod['func_1021'] = func_1021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mutated_mod.get_global_var('func_1021')
call_1022 = func_1021_call()
output = call_1022
func_1023 = relay.Function([], output)
mutated_mod['func_1023'] = func_1023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mod.get_global_var('func_1021')
func_1023_call = mutated_mod.get_global_var('func_1023')
call_1047 = func_1021_call()
call_1048 = func_1021_call()
output = call_1047
output2 = call_1048
func_1075 = relay.Function([], output)
mod['func_1075'] = func_1075
mod = relay.transform.InferType()(mod)
mutated_mod['func_1075'] = func_1075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mutated_mod.get_global_var('func_1075')
call_1076 = func_1075_call()
output = call_1076
func_1077 = relay.Function([], output)
mutated_mod['func_1077'] = func_1077
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1091 = relay.var("var_1091", dtype = "float32", shape = (15, 3, 2))#candidate|1091|(15, 3, 2)|var|float32
uop_1092 = relay.log10(var_1091.astype('float32')) # shape=(15, 3, 2)
func_383_call = mod.get_global_var('func_383')
func_386_call = mutated_mod.get_global_var('func_386')
var_1099 = relay.var("var_1099", dtype = "int64", shape = (96,))#candidate|1099|(96,)|var|int64
call_1098 = func_383_call(relay.reshape(var_1099.astype('int64'), [4, 3, 8]))
call_1100 = func_383_call(relay.reshape(var_1099.astype('int64'), [4, 3, 8]))
func_814_call = mod.get_global_var('func_814')
func_816_call = mutated_mod.get_global_var('func_816')
const_1102 = relay.const([7.911035,-8.515110,-0.219519,0.537891,-8.118927,2.870665,-2.222829,6.470539,-1.327369,-8.228678,1.227037,7.333904,7.798379,-7.647945,-5.329084,2.245933,4.159854,-6.885621,1.633694,-6.707858,-9.134081,0.364367,8.492404,9.043374,6.358575,8.952233,-5.415130,-5.819867,-3.410996,-6.593133,-5.731647,-3.130254,2.520812,1.776567,-1.947653,-6.421747,1.840401,3.569884,-7.732461,5.872682,7.140452,5.836293,5.541479,0.849211,-1.567153,-5.629013,2.677453,-4.268127,5.811159,7.726257,4.218092,-2.087242,-6.968505,-7.544036,-6.728819,-5.952568,-9.108250,-3.689782,7.578881,0.659606,7.028010,-5.715885,-7.116072,-5.552364,-5.109855,2.076384,5.984348,6.271062,2.420422,8.434370,4.454894,3.240948,5.939068,6.722952,-6.659935,-0.679128,-4.324078,-1.674553,-1.396437,5.997903,1.479768,-2.241533,-5.376180,-5.431753,5.364885,-0.994766,2.071689,-4.694904,2.437731,-2.217065,-9.413391,5.650484,3.928070,3.195717,-9.295115,7.708255,7.165425,4.335069,1.032384,-2.513731,6.091947,3.110332,-9.104053,6.623268,6.626683,1.283699,-9.908836,-2.913576,4.952048,5.488827,-9.778439,6.633732,0.136892,-5.161067,-5.432908,3.300438,2.348688,-5.052244,1.873291,5.579667,6.981450,-0.680845,5.383585,-3.837372,8.579874,1.561903,-0.993718,8.938690,5.054513,-3.937074,-8.203437,4.539827,-7.110611,-5.987287,9.949504,-7.239143,-1.050823,-6.059814,3.873738,-1.579630,5.089139,2.348128,-5.562555,2.257311,-6.871801,6.017039,4.868632,-9.418469,1.662171,9.051031,-8.534452,5.950053,3.104238,-9.740980,-0.426037,1.769919,-6.035885,9.262878,3.076413,-3.679457,-7.024280,0.779229,-2.225548,9.650335,-7.634760,-9.922215,-7.868316,9.627799,-0.313639,2.611678,4.289133,-2.505318,1.689540,-5.913304,-2.178495,-0.694778,4.096126,-8.300407,1.395397,5.900367], dtype = "float32")#candidate|1102|(180,)|const|float32
call_1101 = func_814_call(relay.reshape(const_1102.astype('float32'), [10, 3, 6]))
call_1103 = func_814_call(relay.reshape(const_1102.astype('float32'), [10, 3, 6]))
bop_1105 = relay.subtract(uop_1092.astype('float64'), relay.reshape(var_1091.astype('float64'), relay.shape_of(uop_1092))) # shape=(15, 3, 2)
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
var_1125 = relay.var("var_1125", dtype = "float32", shape = (429,))#candidate|1125|(429,)|var|float32
const_1126 = relay.const([5.121114,-5.609256,7.562108,2.495260,9.139748,-9.032046,-2.692097,2.339880,-4.764085,0.127932,-6.479349,1.876600,-5.185504,-8.049524,-8.567942,8.494294,6.261915,-0.708058,1.094085,-6.166416,0.354771,6.405509,-8.995261,9.949319,-0.457332,9.228480,-4.216214,1.936653,9.537249,-1.725801,9.085469,-5.616125,8.226231,-1.218870,-1.339767,8.023871,5.844513,-9.009269,7.173274,-3.461611,-7.281140,-4.775902,-6.763142,7.884387,8.756245,-6.037064,-3.995050,4.759558,2.004510,-1.718394,-0.003852,6.472794,7.691303,5.720053,-7.371316,-5.671835,3.168067,7.765208,9.393303,-9.290440,-9.488811,2.449122,3.364055,4.687849,-6.700171,-9.585933,2.265321,-7.172415,8.690978,-5.731917,8.154241,-5.110989,5.414710,4.340355,6.713165,-5.993332,-0.803547,-0.804336,-9.245246,-8.915822,0.080556,-6.249625,6.274841,1.595991,-3.731816,-0.064058,2.554030,1.298781,-9.694768,2.690865,-4.135424,7.324175,1.902624,-0.979475,1.143467,4.888676,7.438913,-5.089618,-2.995846,-2.528324,6.828350,8.280198,7.639478,2.507897,9.095881,0.184748,-1.729234,-4.596105,-6.372511,-5.629088,2.330380,7.314139,1.005107,9.118550,8.881652,-7.992379,-8.599649,1.016448,-2.710659,6.113982,8.188131,8.708331,-7.006695,-2.208871,-8.684623,-4.701933,-3.350496,8.819062,1.521291,1.507994,-8.176815,3.139221,6.713516,-8.887900,-9.562094,9.359225,9.317497,2.553272,-3.691188,-4.821861,-0.552870,6.017291,-7.617360,-5.832931,2.730614,1.584921,-9.483859,5.172326,4.525608,8.091701,8.831807,-3.178102,-8.324298,-0.496742,5.394646,8.075906,-4.277312,-5.796414,8.468808,-4.039428,-2.816790,-7.095606,9.313317,3.424937,-4.407627,-1.759603,3.476229,-1.303104,-0.501188,2.772227,3.482135,-7.192863,6.181349,6.689425,2.051946,0.482942,7.310112,-6.332460,4.466399,1.824320,7.386843,-4.314824,-3.405148,-0.445513,9.539850,-4.937074,-8.143444,-6.974451,2.024278,6.637615,-9.115002,7.749528,-4.902476,-0.681362,7.959733,5.353803,5.941556,4.113539,-7.931990,-4.790811,4.019477,9.299125,3.688222,3.423471,2.969000,-7.239625,-3.646359,7.477123,0.965498,-6.035029,5.667560,0.491037,4.184073,4.123339,-4.227741,-7.010705,-5.143864,-1.712535,7.320115,8.318925,-2.630587,-9.554995,7.429921,3.644549,1.541699,1.579158,-6.923070,7.031660,4.684317,6.763906,3.012041,-9.740792,7.918392,5.274347,-0.121453,1.204827,-8.296044,5.014322,0.468335,3.950391,9.316276,-6.708418,7.080512,8.205260,-2.463917,2.124229,-0.777421,8.861363,-1.118071,6.231792,4.536607,6.229803,-7.076398,7.796431,3.693782,6.763075,9.699133,-7.197298,9.165126,-9.032070,7.286926,6.129132,2.930221,2.097697,-4.454135,-1.269917,-1.767691,6.045397,4.287067,-1.411251,8.939473,7.116665,9.798816,-5.468032,3.027460,-4.621380,-9.575151,3.198286,8.563430,2.516445,8.410164,8.454977,0.615142,-9.257922,-6.920110,3.846889,-0.384530,-3.089032,2.356606,7.201065,2.742589,2.898896,8.155455,5.459673,6.739785,-1.148554,7.383876,-2.342335,1.846541,7.733048,-6.155310,7.877890,2.532302,-8.564740,-0.656342,6.411797,-6.613387,9.992505,7.520247,-3.894844,2.900005,1.788339,-3.413862,2.704213,8.869631,0.898849,-9.409457,-3.386353,7.749917,-5.619894,-4.721623,6.123026,-5.922938,0.265260,-8.658581,-6.982708,-6.546940,-4.382934,-9.665928,-9.057104,-3.949583,7.249087,8.024234,-1.408232,-0.970250,-1.347620,-2.695011,8.858313,8.482632,5.458197,-1.220283,6.374643,4.138327,-4.405872,-3.526427,5.310949,-0.821147,6.726769,5.346968,-5.915381,-4.849815,-1.544841,3.558337,4.046127,-8.801454,-1.391301,-8.885004,-2.393969,8.656763,5.582603,2.533394,-1.366551,8.062652,9.427932,2.801857,7.259977,9.037413,-9.691144,5.485009,2.315158,-4.497704,4.640880,8.511456,2.895660,-1.327943,-6.557488,9.461835,1.289763,-3.873915,3.001046,5.380660,8.589160,2.535779,0.193901,7.357774,-0.626663,-1.629100,5.386552,3.058750,-0.423695,2.392618,-3.181723,8.220240,-5.550057,-6.525034,3.664399,-0.886756,-0.766003,-8.609338,-4.438878,-4.223642,-4.937441,-3.324709,9.825845,-3.633793,8.391278,-9.145363,-7.288597,-8.243211,-7.441669,5.599673,-4.227133,-8.185291,8.106939,-3.953242,9.765008,-1.413433,0.988382,2.832505,0.197198,-8.990241,9.171078,-5.195323,-5.222377,-7.603291,8.621868,-2.694044,6.950733,7.863537,9.799800,4.021941,-6.866086,-5.483725,-7.821535,-7.173329,2.173995,3.894620,-3.501388,0.276422,-9.368145,2.149487,9.861846,3.851252,-6.476345,5.793676,-9.514205,-2.728286,-9.279924,-9.234323,-7.126532,-9.880286,6.195818,2.738316,4.720895,-8.325756,-9.834109,-8.956204,0.647650,1.366300,-8.392054,1.165201,4.233706,0.670146,0.195109,-8.494805,1.445959,0.193936,-0.093495,-8.032926,7.676859,2.663293,-9.301144,0.426076,8.797501,6.324228,2.191836,-4.964331,0.432784,7.967193,8.137365,-9.693211,-4.079610,5.780449,-7.856595,2.379757,-2.901838,-0.646230,-7.155216,-6.929274,-7.301730,1.633164,5.603767,-2.329190,9.386688,4.607494,2.818011,2.857751,6.936051,8.568421,-7.244199,-7.535596,9.481140,6.487780,-3.755806,-9.743887,-4.284541,6.340299,2.917418,-2.544303,9.800206,-3.388491,4.290844,-2.889387,-1.398059,2.734165,-9.920482,-2.696152,-6.250887,0.885343,3.326428,2.040176,8.779608,0.803733,-5.466887,-0.660275,6.737088,-9.666423,-9.841191,-4.083917,-9.033924,-9.965395,7.607183,1.930098,-8.782437,-5.714266,-4.891731,3.359511,-5.944042,-4.869035,-5.808941,-4.244502,1.778830,5.409401,-0.448267,2.795921,0.997539,8.677082,-4.164861,-1.336942,-6.993487,-7.966707,-5.724670,-7.754791,7.037646,9.476098,5.784783,5.810752,-5.981368,2.809767,-5.906688,-2.168170,-3.250386,-9.802112,-8.443210,9.209830,-3.075788,1.871056,-2.358822,6.324829,-3.210673,6.144318,8.200131,7.847685,1.598816,-1.097971,3.569222,9.382400,-4.415616,-9.234466,-6.892400,4.165410,3.704642,1.858861,2.383397,0.267698,7.912772,9.914529,-6.699907,8.408814,0.882648,7.961093,-9.205605,-8.654327,5.370846,7.280418,6.727734,-8.180732,5.906568,-4.316274,-3.554872,-1.593802,-6.729222,-5.821393,-2.672190,9.627741,8.215191,-0.563332,1.105504,1.652799,7.542804,4.646326,2.966883,-0.540056,7.779714,1.125436,-9.695084,-7.883648,-0.379244,7.370937,-5.550338,-9.202951,-7.136801,4.444749,-0.791480,-9.695627,4.585562,-5.599647,8.639204,3.848753,6.170583,-1.475284,-1.461793,-5.045915,-2.575850,-5.897228,-2.010307,-2.383749,2.115746,6.322702,-0.958256,-7.015913,8.976074,3.497792,2.370143,4.724212,9.608505,-4.331743,-8.513510,-9.331247,9.462219,4.158559,-6.751924,-1.178202,6.167492,0.714269,8.589955,5.300029,-7.418301,5.566011,7.733943,-3.114666,-0.871101,3.764787,2.343752,0.315269,-3.073568,5.649336,1.476946,-9.291468,2.079144,-7.975761,4.779547,7.480140,-4.810205,1.880534,6.315185], dtype = "float32")#candidate|1126|(676,)|const|float32
call_1124 = relay.TupleGetItem(func_408_call(relay.reshape(var_1125.astype('float32'), [13, 3, 11]), relay.reshape(const_1126.astype('float32'), [676,]), ), 0)
call_1127 = relay.TupleGetItem(func_411_call(relay.reshape(var_1125.astype('float32'), [13, 3, 11]), relay.reshape(const_1126.astype('float32'), [676,]), ), 0)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_1133 = relay.TupleGetItem(func_989_call(), 2)
call_1134 = relay.TupleGetItem(func_991_call(), 2)
output = relay.Tuple([call_1098,var_1099,call_1101,const_1102,bop_1105,call_1124,var_1125,const_1126,call_1133,])
output2 = relay.Tuple([call_1100,var_1099,call_1103,const_1102,bop_1105,call_1127,var_1125,const_1126,call_1134,])
func_1138 = relay.Function([var_1091,var_1099,var_1125,], output)
mod['func_1138'] = func_1138
mod = relay.transform.InferType()(mod)
mutated_mod['func_1138'] = func_1138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1138_call = mutated_mod.get_global_var('func_1138')
var_1140 = relay.var("var_1140", dtype = "float32", shape = (15, 3, 2))#candidate|1140|(15, 3, 2)|var|float32
var_1141 = relay.var("var_1141", dtype = "int64", shape = (96,))#candidate|1141|(96,)|var|int64
var_1142 = relay.var("var_1142", dtype = "float32", shape = (429,))#candidate|1142|(429,)|var|float32
call_1139 = func_1138_call(var_1140,var_1141,var_1142,)
output = call_1139
func_1143 = relay.Function([var_1140,var_1141,var_1142,], output)
mutated_mod['func_1143'] = func_1143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mod.get_global_var('func_1021')
func_1023_call = mutated_mod.get_global_var('func_1023')
call_1167 = func_1021_call()
call_1168 = func_1021_call()
uop_1171 = relay.rsqrt(call_1167.astype('float64')) # shape=(1, 7, 16)
uop_1173 = relay.rsqrt(call_1168.astype('float64')) # shape=(1, 7, 16)
func_967_call = mod.get_global_var('func_967')
func_973_call = mutated_mod.get_global_var('func_973')
var_1183 = relay.var("var_1183", dtype = "uint64", shape = (84,))#candidate|1183|(84,)|var|uint64
var_1184 = relay.var("var_1184", dtype = "float32", shape = (1, 1650))#candidate|1184|(1, 1650)|var|float32
call_1182 = relay.TupleGetItem(func_967_call(relay.reshape(var_1183.astype('uint64'), [2, 3, 14]), relay.reshape(var_1183.astype('uint64'), [2, 3, 14]), relay.reshape(var_1183.astype('uint64'), [2, 3, 14]), relay.reshape(var_1184.astype('float32'), [1650,]), relay.reshape(var_1184.astype('float32'), [1650,]), ), 4)
call_1185 = relay.TupleGetItem(func_973_call(relay.reshape(var_1183.astype('uint64'), [2, 3, 14]), relay.reshape(var_1183.astype('uint64'), [2, 3, 14]), relay.reshape(var_1183.astype('uint64'), [2, 3, 14]), relay.reshape(var_1184.astype('float32'), [1650,]), relay.reshape(var_1184.astype('float32'), [1650,]), ), 4)
func_529_call = mod.get_global_var('func_529')
func_531_call = mutated_mod.get_global_var('func_531')
const_1189 = relay.const([[-5.899244,-9.894204,4.050575,7.994483,1.860247,-4.127667,1.562230,-0.713531,-9.304165,-4.123279,9.107929,8.095796,-3.722901,0.459666,-1.082744,3.845837,-5.251651,-1.202490,-0.633186,-6.839377,-4.212060,0.777021,8.773445,-5.904286,-9.146075,-3.244817,2.548850,2.154145,-3.708625,6.259429,-2.475962,6.888090,-1.416530,5.714345,-5.136875,-5.742992,-6.409076,-2.747609,6.743092,-4.199817,-0.071446,7.913183,-8.418450,3.695417,3.150210,5.885027,7.455131,-0.412750,6.049697,-1.048359,9.094594,-9.542931,4.809162,6.935658,-2.825283,-0.742387,-3.807690,-3.917265,-1.715807,5.053024,-6.828488,-4.402233,-7.379894,6.642414,-6.796298,0.507976,-9.757063,3.744961,-5.745416,-2.195035,-1.878829,9.999676,-1.987699,-3.955153,8.848197,-3.176888,-0.458752,4.312998,-4.636278,-8.854059,8.124947,-5.895100,-6.928572,7.757799,7.477579,1.408583,-9.476716,-3.208411],[-8.792057,2.958353,7.564848,-6.181028,-1.746562,-7.162123,-0.388174,3.526399,-1.863976,-6.812142,-5.909379,2.687581,3.087765,0.615328,-0.124020,3.988616,-0.732334,-2.906398,-8.827809,-8.304870,7.133341,7.505307,6.364019,3.067171,3.937475,-8.990377,7.630371,0.942408,-4.175306,-8.556959,-6.360451,-6.668395,-9.225530,-0.097063,1.903280,-3.062897,7.001701,-9.995184,-3.973445,-6.305204,2.485621,5.166498,4.101434,-1.634975,-6.589161,-7.869998,-6.288489,6.650539,7.226804,6.335744,-8.982911,1.550375,-0.033023,5.393753,9.728151,-9.399565,-4.269516,2.591245,-2.421288,-5.764704,-7.673541,1.274339,2.619082,-2.946960,6.048810,4.710240,3.976467,8.805735,-7.571111,-3.759911,4.893810,2.606073,5.747132,9.794403,-8.077307,-2.973452,-1.412927,4.081761,-8.665315,-5.793088,7.585218,-4.649007,7.838698,-8.314012,-2.213525,0.613812,3.138506,2.777626],[-7.555797,-8.083226,-2.492934,5.457765,4.225876,-5.949790,-6.772108,2.507128,-1.387911,-9.916723,3.237723,-0.290908,-4.720244,6.314737,-5.580498,-0.226601,1.580417,8.869277,7.151196,-8.383407,3.410332,-0.393661,-8.082285,4.149543,8.047241,-6.903459,6.158847,-8.744990,-9.806692,6.651805,5.944903,9.875661,3.355390,-5.217196,-0.243321,6.741465,-2.239684,2.194543,5.925178,1.965013,7.883213,3.316208,-4.629035,-8.642097,-7.238751,4.696097,5.806734,-5.111456,9.051745,4.516376,-1.541487,7.430131,-5.452299,6.541007,-8.017943,2.924225,-3.135054,-0.128722,-0.649584,1.341542,-9.582882,-9.156586,-6.112796,-3.097746,-2.293316,7.841177,-1.855171,8.670682,7.891971,-8.229172,9.044744,4.801647,4.926078,3.158578,-2.114206,-2.549939,9.912970,-8.737083,1.564600,-1.795141,-9.021682,-6.125064,-9.311323,-1.243627,-5.153648,8.443561,-0.686043,5.197354],[-1.600288,0.318893,-4.107264,-9.886153,0.191827,3.760749,0.714545,-6.276357,3.921680,7.384390,-5.004854,4.824996,-5.026519,-2.148667,-6.034317,-1.694519,-3.854267,6.160341,7.017004,8.553738,0.775901,-8.950634,-8.898508,-6.369884,8.163173,0.835606,2.070753,3.692999,-2.464786,-1.462053,5.478196,5.132819,7.969061,-1.716636,-3.917471,8.497532,-4.710073,1.292741,-6.988501,-8.952817,3.135452,7.282570,7.988991,-2.423189,-3.488017,-5.589984,-8.277161,-5.896166,-3.502097,-4.544943,-1.769644,-5.280260,9.712874,6.214827,-4.591376,-5.196876,2.101146,-2.455884,-8.603370,-1.249535,-6.856254,-1.626557,2.468474,-0.622553,-5.267279,-3.738805,-2.275569,7.628612,-7.186447,6.560653,0.142313,-9.037243,8.635724,7.737269,-4.164603,-3.821363,-9.292546,2.522742,9.364201,1.213268,-4.740923,-8.552099,0.528575,1.577270,-1.845067,-3.602529,-1.311868,3.148324],[7.466130,8.411106,-3.802940,-4.548397,-3.382377,-1.147477,9.905292,6.402004,-7.802929,-8.335330,-4.920328,3.279004,-1.209664,-4.041730,7.363568,-0.461999,-6.979038,-7.284596,-2.745202,1.924452,-6.831614,-8.701530,8.957665,4.646897,-1.306483,9.404461,7.291425,0.385436,-8.457460,-6.293065,0.574117,1.198254,-6.862831,3.599672,-7.507234,-9.540597,-2.443621,3.411802,-4.584061,4.340923,-4.710462,3.853452,-0.347583,-2.730722,-9.914404,-6.063354,5.889659,3.913715,0.897739,-8.006460,5.173065,-1.571302,-8.817307,-2.745661,-2.909437,4.238418,-2.279039,4.534922,0.502096,-5.179310,-6.279763,-4.237919,-5.490273,-4.287384,-3.421906,9.266505,5.212066,8.410282,7.279484,-9.010203,-8.317132,5.027096,8.870103,3.544342,-4.605666,-0.356419,-9.644490,-7.422733,3.264339,-8.801259,-0.643478,3.079643,9.605469,3.114397,-3.924016,-8.181680,8.706651,-3.863326],[-0.285610,1.392986,5.352546,-2.991876,-6.489453,-5.347622,8.671236,5.284460,-3.816295,6.833212,-3.361244,0.158037,-5.337738,8.706359,4.969839,-6.227552,4.337600,-2.640741,-5.439412,-9.500892,2.499559,-5.985018,2.519787,-3.142612,-3.334814,8.338424,-9.880952,-5.546789,-6.576690,-2.244875,8.456509,-9.101776,6.154501,9.335046,5.250281,-9.051924,-3.635083,0.943606,8.001051,4.522192,1.942595,-6.906669,1.876614,-0.160050,-7.084120,3.565981,-3.563990,-9.543749,-3.834664,1.369816,5.549543,6.872747,-4.156991,6.475123,-5.930100,5.005959,8.470387,-2.630638,-3.898267,-9.546850,1.225049,-8.204396,5.092008,0.891057,-4.713080,0.190200,3.459295,1.521486,9.296148,3.403864,-6.387673,3.533780,-5.516309,-5.741623,6.465315,0.915825,2.504766,-1.737343,-7.269598,-4.865834,-9.771133,-6.966916,-7.323245,6.218539,-2.853035,-4.358109,4.692542,-6.107563],[8.455797,6.686482,5.434527,6.782890,-5.608315,-5.014421,-3.335625,-9.182568,-8.599091,-7.237414,-5.542902,4.812439,-7.378432,2.652139,4.469204,7.225641,9.413914,9.793534,0.232129,0.397028,-2.195962,-0.959007,-6.301525,3.300857,2.514692,-2.455633,6.845728,-0.123175,0.821966,-6.556056,1.697400,7.712315,-7.391318,2.172545,3.283875,3.532297,-5.317606,-4.606958,-7.671038,-0.609967,7.597839,-2.796760,-3.561396,-9.432320,-2.064465,-6.832462,-1.924938,-2.727670,5.828476,-0.365817,-5.852937,-5.919318,5.383470,-7.812123,0.611718,0.223581,9.087190,5.626384,-2.325608,2.292150,-6.639024,-9.063852,2.102416,7.866602,7.350329,2.794318,-8.274834,-6.199859,0.357661,2.055899,7.828099,6.114582,-4.069009,-0.927440,7.158096,-6.573399,-3.538815,-9.190803,8.539594,-5.100693,-8.424643,6.392086,4.108782,-3.167226,-0.768203,8.396599,4.471146,-0.650098],[-3.657171,-8.709771,-3.762926,3.876896,-5.434020,-2.276481,-9.370375,-7.864593,-9.130069,6.507472,9.279248,-1.067818,8.644990,-8.976797,0.926935,6.583138,5.371211,9.923992,-5.657131,-0.257837,-6.529337,-7.810980,7.132311,6.242841,-9.024336,-9.949010,9.099859,3.010899,-5.319181,0.595788,-5.228214,6.506741,-1.035134,8.779412,-3.012553,4.416774,-1.736272,8.874642,-9.633246,-4.873205,9.776432,4.079922,7.270071,8.158166,-8.289674,6.370444,7.803889,-7.168594,6.763745,-8.381858,-2.212431,1.243607,-8.311322,-9.584257,7.968978,8.783926,0.945136,9.719273,-1.444507,9.553323,5.168000,6.440554,6.798156,4.233319,-2.277253,-9.021245,7.616686,1.217062,-2.273054,9.340800,-1.229164,-5.230554,5.928756,9.608628,2.587108,-7.459270,0.959086,1.211253,4.056665,-5.845250,2.014864,-9.269885,-9.822527,-7.546067,-7.802902,-6.909366,-9.495197,-7.706806]], dtype = "float32")#candidate|1189|(8, 88)|const|float32
call_1188 = relay.TupleGetItem(func_529_call(relay.reshape(const_1189.astype('float32'), [4, 11, 16])), 0)
call_1190 = relay.TupleGetItem(func_531_call(relay.reshape(const_1189.astype('float32'), [4, 11, 16])), 0)
func_620_call = mod.get_global_var('func_620')
func_623_call = mutated_mod.get_global_var('func_623')
var_1201 = relay.var("var_1201", dtype = "float32", shape = (384,))#candidate|1201|(384,)|var|float32
call_1200 = relay.TupleGetItem(func_620_call(relay.reshape(var_1201.astype('float32'), [4, 8, 12]), relay.reshape(var_1201.astype('float32'), [4, 8, 12]), ), 0)
call_1202 = relay.TupleGetItem(func_623_call(relay.reshape(var_1201.astype('float32'), [4, 8, 12]), relay.reshape(var_1201.astype('float32'), [4, 8, 12]), ), 0)
func_1138_call = mod.get_global_var('func_1138')
func_1143_call = mutated_mod.get_global_var('func_1143')
const_1216 = relay.const([-5.913100,-2.997538,-2.508283,7.647916,1.699369,5.050819,-4.754727,1.804852,-9.914813,-1.275017,0.469986,2.297012,1.551332,-2.489215,-1.251956,0.802378,3.133261,-5.899448,-7.632330,-1.353618,9.314843,0.398353,-1.921693,7.116258,-0.249613,-9.159986,-4.781977,-0.744959,8.662509,-4.728955,1.090369,-8.464335,1.495835,-3.984056,5.633375,-0.924477,2.989489,-4.949625,-8.887013,-8.561760,4.117502,-2.430362,-3.194897,-2.881718,-1.206986,9.776242,-2.341548,-8.273977,6.178642,3.506056,7.103890,4.497145,-4.601495,-4.113531,-2.101659,3.517469,6.390479,1.313819,-9.930943,-4.839127,-2.825614,-6.830223,2.346723,3.146588,-7.897881,2.834027,-1.439459,-9.438293,8.464695,8.942482,2.677656,8.891755,-2.158000,6.935820,-0.978504,4.148563,3.330241,3.247269,-5.198733,8.891633,-9.005687,-4.492350,-0.158166,4.353056,4.971891,0.939419,3.381810,-9.564727,5.038703,-5.389451], dtype = "float32")#candidate|1216|(90,)|const|float32
const_1217 = relay.const([[-1],[-8],[5],[8],[-4],[-9],[2],[-8],[9],[-7],[6],[-7],[-9],[-4],[8],[-5],[-3],[9],[-9],[-10],[-4],[3],[-10],[-8],[2],[8],[-1],[-2],[7],[-3],[6],[-1],[-3],[8],[9],[-4],[-6],[-10],[-9],[7],[-6],[-9],[9],[5],[-9],[-10],[10],[-7],[4],[-4],[3],[8],[4],[8],[-8],[7],[10],[-9],[9],[-7],[-6],[-5],[-8],[9],[8],[-7],[-9],[4],[2],[-1],[9],[-4],[-3],[-9],[9],[-3],[1],[-1],[-2],[5],[2],[-3],[-6],[8],[-9],[8],[-6],[6],[-5],[6],[-9],[1],[6],[-2],[-10],[8]], dtype = "int64")#candidate|1217|(96, 1)|const|int64
var_1218 = relay.var("var_1218", dtype = "float32", shape = (39, 11))#candidate|1218|(39, 11)|var|float32
call_1215 = relay.TupleGetItem(func_1138_call(relay.reshape(const_1216.astype('float32'), [15, 3, 2]), relay.reshape(const_1217.astype('int64'), [96,]), relay.reshape(var_1218.astype('float32'), [429,]), ), 3)
call_1219 = relay.TupleGetItem(func_1143_call(relay.reshape(const_1216.astype('float32'), [15, 3, 2]), relay.reshape(const_1217.astype('int64'), [96,]), relay.reshape(var_1218.astype('float32'), [429,]), ), 3)
output = relay.Tuple([uop_1171,call_1182,var_1183,var_1184,call_1188,const_1189,call_1200,var_1201,call_1215,const_1216,const_1217,var_1218,])
output2 = relay.Tuple([uop_1173,call_1185,var_1183,var_1184,call_1190,const_1189,call_1202,var_1201,call_1219,const_1216,const_1217,var_1218,])
func_1223 = relay.Function([var_1183,var_1184,var_1201,var_1218,], output)
mod['func_1223'] = func_1223
mod = relay.transform.InferType()(mod)
var_1224 = relay.var("var_1224", dtype = "uint64", shape = (84,))#candidate|1224|(84,)|var|uint64
var_1225 = relay.var("var_1225", dtype = "float32", shape = (1, 1650))#candidate|1225|(1, 1650)|var|float32
var_1226 = relay.var("var_1226", dtype = "float32", shape = (384,))#candidate|1226|(384,)|var|float32
var_1227 = relay.var("var_1227", dtype = "float32", shape = (39, 11))#candidate|1227|(39, 11)|var|float32
output = func_1223(var_1224,var_1225,var_1226,var_1227,)
func_1228 = relay.Function([var_1224,var_1225,var_1226,var_1227,], output)
mutated_mod['func_1228'] = func_1228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_1251 = func_1075_call()
call_1252 = func_1075_call()
output = relay.Tuple([call_1251,])
output2 = relay.Tuple([call_1252,])
func_1265 = relay.Function([], output)
mod['func_1265'] = func_1265
mod = relay.transform.InferType()(mod)
output = func_1265()
func_1266 = relay.Function([], output)
mutated_mod['func_1266'] = func_1266
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1280 = relay.var("var_1280", dtype = "float64", shape = (16, 12, 8))#candidate|1280|(16, 12, 8)|var|float64
uop_1281 = relay.cos(var_1280.astype('float64')) # shape=(16, 12, 8)
uop_1292 = relay.log(uop_1281.astype('float32')) # shape=(16, 12, 8)
var_1298 = relay.var("var_1298", dtype = "float64", shape = (16, 12, 8))#candidate|1298|(16, 12, 8)|var|float64
bop_1299 = relay.maximum(uop_1281.astype('int32'), relay.reshape(var_1298.astype('int32'), relay.shape_of(uop_1281))) # shape=(16, 12, 8)
func_571_call = mod.get_global_var('func_571')
func_576_call = mutated_mod.get_global_var('func_576')
var_1305 = relay.var("var_1305", dtype = "uint64", shape = (2, 80))#candidate|1305|(2, 80)|var|uint64
var_1306 = relay.var("var_1306", dtype = "float32", shape = (60,))#candidate|1306|(60,)|var|float32
call_1304 = relay.TupleGetItem(func_571_call(relay.reshape(var_1305.astype('uint64'), [8, 4, 5]), relay.reshape(var_1305.astype('uint64'), [8, 4, 5]), relay.reshape(var_1306.astype('float32'), [60,]), ), 1)
call_1307 = relay.TupleGetItem(func_576_call(relay.reshape(var_1305.astype('uint64'), [8, 4, 5]), relay.reshape(var_1305.astype('uint64'), [8, 4, 5]), relay.reshape(var_1306.astype('float32'), [60,]), ), 1)
bop_1309 = relay.power(uop_1292.astype('float64'), relay.reshape(bop_1299.astype('float64'), relay.shape_of(uop_1292))) # shape=(16, 12, 8)
uop_1314 = relay.atanh(uop_1281.astype('float32')) # shape=(16, 12, 8)
bop_1318 = relay.multiply(bop_1309.astype('int64'), relay.reshape(uop_1292.astype('int64'), relay.shape_of(bop_1309))) # shape=(16, 12, 8)
output = relay.Tuple([call_1304,var_1305,var_1306,uop_1314,bop_1318,])
output2 = relay.Tuple([call_1307,var_1305,var_1306,uop_1314,bop_1318,])
func_1328 = relay.Function([var_1280,var_1298,var_1305,var_1306,], output)
mod['func_1328'] = func_1328
mod = relay.transform.InferType()(mod)
mutated_mod['func_1328'] = func_1328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1328_call = mutated_mod.get_global_var('func_1328')
var_1330 = relay.var("var_1330", dtype = "float64", shape = (16, 12, 8))#candidate|1330|(16, 12, 8)|var|float64
var_1331 = relay.var("var_1331", dtype = "float64", shape = (16, 12, 8))#candidate|1331|(16, 12, 8)|var|float64
var_1332 = relay.var("var_1332", dtype = "uint64", shape = (2, 80))#candidate|1332|(2, 80)|var|uint64
var_1333 = relay.var("var_1333", dtype = "float32", shape = (60,))#candidate|1333|(60,)|var|float32
call_1329 = func_1328_call(var_1330,var_1331,var_1332,var_1333,)
output = call_1329
func_1334 = relay.Function([var_1330,var_1331,var_1332,var_1333,], output)
mutated_mod['func_1334'] = func_1334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1348 = relay.var("var_1348", dtype = "float32", shape = (4, 8, 11))#candidate|1348|(4, 8, 11)|var|float32
const_1349 = relay.const([[[-6.852448,3.693095,-6.147599,6.014431,-4.520280,1.632227,1.808522,-9.483299,-7.335578,-9.647602,-7.214887],[-9.142000,-2.519001,6.414507,4.763979,-1.271194,-4.303570,9.856235,5.547938,2.925621,-8.174139,3.289079],[-3.743789,4.933979,-3.180157,4.882803,-3.527103,1.807284,9.366825,1.394126,-7.193135,-0.768935,1.495020],[0.233341,-3.023685,-1.773027,9.995324,-1.288992,-6.488818,-5.725475,-9.994149,0.407743,5.954293,2.713199],[0.077607,-9.047787,-1.489067,-0.607548,-1.574263,2.629276,-5.171543,9.517721,2.431913,3.884586,1.358032],[-8.308029,2.780341,5.350981,-5.101518,8.287048,2.513001,4.355953,6.513246,7.988300,5.343080,-9.222180],[9.045624,8.866895,-1.751563,-7.544840,2.735616,2.358889,-2.400401,5.394297,3.287616,-6.356297,-1.737501],[-3.824043,1.801961,-0.656785,-1.023434,-8.881894,-9.728354,-4.765969,-7.803849,3.481559,5.562815,-6.867747]],[[2.979238,6.199918,-3.632460,4.003261,2.090571,-3.034174,9.251309,-1.289236,-8.924823,9.649673,-4.255780],[6.407263,-6.734056,-5.873143,7.415729,1.343937,6.786096,7.896915,-3.661321,-2.191454,-6.738655,-6.195508],[3.867895,-6.940778,3.663963,1.135798,2.303083,-8.897925,7.899642,-9.931182,4.988836,5.994832,-2.086478],[7.912092,2.481425,-0.007407,-5.097564,9.074309,3.916458,0.662702,-1.557560,4.189719,6.275413,2.575064],[-5.377392,1.701043,-6.734970,-9.178507,9.930987,0.184130,-9.732741,9.399918,0.341309,-2.689360,-6.946883],[4.066119,-2.764699,-9.460241,4.681617,-6.633852,2.347290,9.790236,-9.896788,-9.427741,5.940858,-5.119882],[-6.193766,7.325114,1.508642,-4.634037,4.557552,-9.716322,-7.229348,-4.183283,-4.448556,-0.829083,-9.517655],[1.600610,9.359120,3.421768,-8.690527,-6.062210,3.452324,-2.766632,-7.135951,-6.759746,-6.686422,4.614175]],[[1.940293,-3.205773,6.362100,-8.225858,8.117283,-6.220134,5.768093,8.125259,-3.978721,-9.825331,8.346863],[-6.253711,-8.639513,-0.263921,0.426783,0.919156,3.304695,-9.510132,-9.653649,-7.678913,4.514395,7.326158],[-1.834798,-4.859276,-8.198094,-0.795969,8.827428,8.336293,6.753367,-9.646511,-0.540997,-2.789155,-5.341400],[-2.619589,9.077594,-0.813364,4.107742,9.796353,-7.610860,-5.625427,4.692298,5.058596,4.640545,-4.119239],[-4.233254,1.455237,-3.743360,-2.942835,8.953551,-1.160556,6.099226,0.820982,-2.337088,5.938572,-0.630852],[4.494334,-8.683649,-6.439557,-3.813732,9.618574,0.920339,4.449620,-3.627260,-4.864102,-3.921760,-8.364945],[3.698582,-5.672727,-4.179151,9.316897,-6.392317,-2.348475,7.667921,-1.374348,4.368727,-2.938307,3.912148],[4.221592,4.409805,5.471809,-4.904495,4.277847,9.771289,6.328543,6.930535,-7.729533,2.245450,6.219058]],[[0.525681,-3.399091,1.484855,5.131140,-4.875994,-5.925928,4.326510,8.784234,9.712803,9.563982,7.648769],[-0.453343,6.456269,-2.415934,-1.943283,8.707055,9.394038,-2.165450,-5.471444,9.755631,-0.622750,-8.689149],[9.688125,9.402088,7.458562,6.060849,1.509321,2.920659,-8.936566,-5.753889,4.441033,-6.345862,5.888923],[0.550693,6.950627,0.880789,-9.299631,4.515642,4.762582,-0.449469,1.394373,5.965359,-1.615233,-3.149406],[-1.377909,4.357467,-0.919870,5.321240,-2.798689,-8.976469,5.098219,-6.140396,0.106054,-9.310683,-8.915719],[0.190413,-7.280349,0.315453,-2.907453,-7.750012,-2.375252,-2.418081,1.201715,-9.762153,8.036588,8.918667],[-3.600427,-0.217513,7.088122,7.754184,-5.545108,-7.332649,4.304375,8.436025,4.042069,3.448537,1.455198],[-6.727663,7.441843,-5.060964,5.491532,9.702088,5.937135,-7.662203,-3.553206,7.260879,-9.538985,-2.792328]]], dtype = "float32")#candidate|1349|(4, 8, 11)|const|float32
bop_1350 = relay.power(var_1348.astype('float32'), relay.reshape(const_1349.astype('float32'), relay.shape_of(var_1348))) # shape=(4, 8, 11)
output = bop_1350
output2 = bop_1350
func_1356 = relay.Function([var_1348,], output)
mod['func_1356'] = func_1356
mod = relay.transform.InferType()(mod)
mutated_mod['func_1356'] = func_1356
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1357 = relay.var("var_1357", dtype = "float32", shape = (4, 8, 11))#candidate|1357|(4, 8, 11)|var|float32
func_1356_call = mutated_mod.get_global_var('func_1356')
call_1358 = func_1356_call(var_1357)
output = call_1358
func_1359 = relay.Function([var_1357], output)
mutated_mod['func_1359'] = func_1359
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1459 = relay.var("var_1459", dtype = "int16", shape = (15, 9, 2))#candidate|1459|(15, 9, 2)|var|int16
var_1460 = relay.var("var_1460", dtype = "int16", shape = (15, 9, 2))#candidate|1460|(15, 9, 2)|var|int16
bop_1461 = relay.subtract(var_1459.astype('int16'), relay.reshape(var_1460.astype('int16'), relay.shape_of(var_1459))) # shape=(15, 9, 2)
output = bop_1461
output2 = bop_1461
func_1466 = relay.Function([var_1459,var_1460,], output)
mod['func_1466'] = func_1466
mod = relay.transform.InferType()(mod)
mutated_mod['func_1466'] = func_1466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1466_call = mutated_mod.get_global_var('func_1466')
var_1468 = relay.var("var_1468", dtype = "int16", shape = (15, 9, 2))#candidate|1468|(15, 9, 2)|var|int16
var_1469 = relay.var("var_1469", dtype = "int16", shape = (15, 9, 2))#candidate|1469|(15, 9, 2)|var|int16
call_1467 = func_1466_call(var_1468,var_1469,)
output = call_1467
func_1470 = relay.Function([var_1468,var_1469,], output)
mutated_mod['func_1470'] = func_1470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_1474 = relay.TupleGetItem(func_989_call(), 2)
call_1475 = relay.TupleGetItem(func_991_call(), 2)
output = call_1474
output2 = call_1475
func_1503 = relay.Function([], output)
mod['func_1503'] = func_1503
mod = relay.transform.InferType()(mod)
mutated_mod['func_1503'] = func_1503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1503_call = mutated_mod.get_global_var('func_1503')
call_1504 = func_1503_call()
output = call_1504
func_1505 = relay.Function([], output)
mutated_mod['func_1505'] = func_1505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_1516 = relay.TupleGetItem(func_989_call(), 1)
call_1517 = relay.TupleGetItem(func_991_call(), 1)
output = call_1516
output2 = call_1517
func_1523 = relay.Function([], output)
mod['func_1523'] = func_1523
mod = relay.transform.InferType()(mod)
mutated_mod['func_1523'] = func_1523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1523_call = mutated_mod.get_global_var('func_1523')
call_1524 = func_1523_call()
output = call_1524
func_1525 = relay.Function([], output)
mutated_mod['func_1525'] = func_1525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_1551 = relay.TupleGetItem(func_989_call(), 3)
call_1552 = relay.TupleGetItem(func_991_call(), 3)
output = relay.Tuple([call_1551,])
output2 = relay.Tuple([call_1552,])
func_1553 = relay.Function([], output)
mod['func_1553'] = func_1553
mod = relay.transform.InferType()(mod)
output = func_1553()
func_1554 = relay.Function([], output)
mutated_mod['func_1554'] = func_1554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1265_call = mod.get_global_var('func_1265')
func_1266_call = mutated_mod.get_global_var('func_1266')
call_1621 = relay.TupleGetItem(func_1265_call(), 0)
call_1622 = relay.TupleGetItem(func_1266_call(), 0)
func_1223_call = mod.get_global_var('func_1223')
func_1228_call = mutated_mod.get_global_var('func_1228')
var_1633 = relay.var("var_1633", dtype = "uint64", shape = (84,))#candidate|1633|(84,)|var|uint64
const_1634 = relay.const([[8.001333,-6.741288,6.100181],[-7.114482,2.834133,-1.297056],[3.131552,-5.465886,4.182496],[0.300475,9.928490,-3.211853],[-1.281406,4.069425,3.248139],[7.233376,3.652893,-5.073536],[-6.145896,7.914411,1.587313],[-7.523768,3.234360,5.156241],[-0.016447,-7.461700,2.156560],[0.444513,-4.555984,-4.386845],[-4.940947,-6.744530,8.657070],[-9.932365,7.175705,-1.844567],[3.881867,-6.215691,5.057814],[-6.488763,-5.885445,4.370443],[4.494664,2.494854,-0.850165],[6.471187,-5.939544,-4.040546],[3.967396,8.149937,-5.504781],[3.257382,7.436416,-9.620200],[3.269772,-5.078196,-1.974023],[9.341624,-7.981026,0.541140],[8.734825,7.752054,4.791731],[3.941170,-5.273517,1.107216],[-0.397595,5.145726,-1.561716],[7.060174,-9.028963,-1.477397],[0.011604,-2.747138,-3.158765],[-3.648706,7.922111,0.880625],[0.248957,0.368441,-4.147493],[1.607933,7.419122,-5.394079],[-5.576437,4.104379,3.526729],[2.439969,-6.584920,-3.986895],[-9.208273,-1.795394,5.378356],[-2.471222,-9.725635,-9.274750],[-0.274561,-1.445074,-8.221347],[-6.032457,-8.998108,0.325158],[4.112915,-7.932904,3.008240],[-6.646615,-2.882250,0.445827],[1.467128,-5.493347,2.031602],[-9.776345,-9.859741,5.726377],[4.570231,-6.600151,5.425034],[0.695431,-5.064082,-2.628609],[-8.955332,1.195117,3.289700],[-7.210752,-4.391526,7.224572],[-9.324183,-6.522699,-8.062288],[1.053867,0.712381,7.570374],[-0.560786,6.089716,-6.390627],[-9.703139,-1.109490,4.462419],[-5.786189,-2.306784,8.978009],[-1.052070,2.387216,-2.249912],[-4.972677,3.440224,6.143899],[-7.833672,4.966927,0.655804],[-3.064503,0.653657,4.720415],[-0.391037,-6.311483,1.267247],[-5.750092,4.614862,-6.231004],[5.623280,-1.401570,-1.460931],[2.182747,2.178450,-8.397350],[4.479974,-1.209909,2.343223],[7.084042,0.454897,2.258255],[4.209887,-3.331203,7.218171],[7.209306,5.356803,-8.804007],[3.624468,-0.914874,-8.995536],[5.128141,1.715383,-2.021920],[-5.845246,8.660077,-9.655375],[-9.132993,-9.303102,-3.293719],[5.190009,1.255095,7.904375],[-6.041758,2.268049,3.730301],[5.582804,7.419995,-4.515707],[8.210072,-8.308483,-4.133615],[7.113844,-8.927458,5.637991],[-7.469389,-8.484189,9.163346],[0.858425,6.645234,9.616258],[-3.112356,0.431982,8.572516],[-5.026623,-9.900858,0.244218],[1.098267,9.154125,0.593462],[-9.008505,9.515471,3.877158],[3.828554,-3.454104,0.896540],[8.130252,-4.984583,-6.792579],[2.252150,2.428176,2.086701],[-4.450064,2.904661,-0.208893],[2.139485,-4.506974,-4.724105],[2.480656,-0.502245,-4.741005],[4.500854,-9.454029,-7.021506],[-5.888974,5.606236,-4.249495],[-7.872293,3.049386,-0.495220],[-5.049286,-7.385486,3.536641],[-7.370566,-3.354276,-7.623531],[6.383815,4.554751,-1.962916],[-8.353663,5.527621,-6.384753],[-0.714965,-5.190422,-1.255771],[3.772388,-6.659275,-8.947266],[-8.143696,3.024417,0.779851],[1.056185,3.975960,-2.943822],[6.580964,-4.303486,-6.599476],[-7.311343,-4.988323,-0.100129],[4.630210,7.642131,-6.316424],[0.319593,4.908908,2.446939],[4.419971,1.753473,2.711898],[-6.479461,-4.048144,8.095345],[1.933645,9.430068,0.776038],[-3.384545,9.720489,-0.174609],[0.008449,3.865934,-8.941462],[-2.879588,2.643319,4.503161],[8.216696,1.605211,-3.367462],[1.073484,-2.514027,5.655753],[-4.995598,6.358051,-2.008240],[5.948650,6.158861,-2.024046],[-9.845667,5.102643,-8.596800],[-5.910154,-2.434878,1.018299],[3.795413,-7.825194,2.341325],[5.245969,-1.761811,8.572896],[-9.914745,-3.379553,7.253577],[-8.569690,1.862733,-3.457793],[-0.848030,-4.145492,-8.987976],[1.589366,-4.487139,-5.960995],[-9.998514,7.158692,-6.759548],[0.919115,-8.529083,-1.960198],[-6.602897,8.311302,0.746081],[0.876027,-7.798876,-7.885883],[2.339732,-5.019414,-9.166835],[2.141809,-9.224072,2.945347],[2.188346,-1.615318,-1.070500],[-4.701820,9.833675,4.002879],[4.748938,-7.223571,-5.526958],[-0.125127,-7.805537,2.869347],[7.740504,9.872642,0.299479],[-5.147497,5.314107,-0.573870],[-4.477684,-6.810071,-9.928154],[-9.349820,-5.801940,-3.457778],[2.034760,-2.325916,6.330396],[-9.454251,-7.161074,1.667829],[-4.245948,8.926124,-3.743051],[-6.608244,-8.927475,-1.086289],[-9.318889,-2.014518,1.439272],[6.407089,7.182445,-4.371555],[3.130375,-0.095692,5.793525],[2.603956,6.139458,0.073318],[2.401390,-2.307648,8.933749],[-5.192985,2.358801,-4.408636],[9.863321,-7.653951,-9.073655],[-7.408813,7.039067,3.131883],[-3.155645,1.013582,8.671582],[1.997858,-8.159635,-6.276674],[-5.740044,3.593993,4.436523],[-0.161711,4.093732,-6.993518],[1.319470,2.841510,9.280150],[4.811128,2.063632,6.422118],[-7.229754,2.365563,4.477556],[-3.843946,7.383459,3.161097],[8.176161,6.675965,-6.024731],[-2.868385,-1.291979,2.443780],[7.844066,1.913773,5.451191],[6.892635,3.926148,-9.732895],[5.917989,-8.416924,-5.396946],[7.017667,6.082205,-1.856689],[-2.777941,-3.785870,-1.818975],[-9.039908,-7.118201,-4.754782],[5.036445,9.490272,6.221355],[7.559271,-4.307857,6.374837],[1.390167,5.880208,4.558549],[5.169255,-6.813628,4.121664],[3.721920,-5.400662,8.580851],[3.381299,2.727868,-3.049165],[-2.440337,0.713000,9.633272],[9.240734,3.757526,-2.615016],[-2.743895,9.152103,8.291603],[8.246465,-2.095547,-4.797086],[-3.976198,-6.770855,0.033933],[-3.776100,-5.363207,-0.355210],[-2.031101,7.206364,-0.527399],[8.570319,9.407563,-7.557313],[5.570427,5.016541,1.840085],[4.203682,4.965821,3.472704],[-8.091026,-7.531003,5.323565],[2.775536,-5.376942,-1.586227],[-5.279036,2.721860,-3.820738],[-1.881197,1.096750,5.307228],[5.197594,-6.843805,4.033350],[9.444201,-8.611413,-6.690639],[7.935861,3.273182,-4.890998],[-3.248325,9.298306,-2.721452],[7.710844,0.413093,-5.184978],[-2.317891,-0.693819,-0.516458],[-8.403871,1.546053,9.394819],[3.232908,6.281794,-7.535739],[-4.113299,-6.818614,-0.752876],[1.137863,1.041334,-4.513866],[5.989957,-5.110937,-7.424551],[3.721858,-5.321017,3.019579],[8.759618,-1.799363,4.450346],[-9.186880,-6.442256,-7.035104],[-1.257302,-8.824690,-1.281884],[9.811604,5.726626,3.369454],[9.572869,0.442603,-6.323181],[7.205061,2.496408,-5.759841],[5.625010,-2.257993,-5.545890],[-5.591967,-6.369647,-4.493878],[-6.992002,-5.562593,3.562296],[6.748965,0.891111,8.953408],[2.632989,7.475555,-6.388390],[5.867208,-4.035193,8.293642],[-4.434446,4.012359,4.114093],[-0.735181,-1.906847,2.061714],[-7.158008,-6.288739,7.475382],[9.806286,-4.431278,4.561897],[2.032219,-6.053151,-9.917344],[-1.810113,-4.685072,3.320210],[0.494114,2.174779,1.627528],[-3.766768,4.723938,1.532815],[-0.055608,8.604898,3.560242],[8.336121,0.267191,-6.426163],[-6.378953,5.815414,3.862621],[-2.693927,-3.678195,-1.424613],[-9.900606,3.394729,5.147205],[3.105950,-7.308783,-5.746142],[8.205115,-8.385168,-7.251703],[5.352434,4.374653,7.096865],[7.822431,7.254946,4.681523],[7.805090,-4.040124,6.684933],[2.514272,2.963650,0.271115],[8.898014,-1.045834,2.160858],[9.148908,5.288620,4.140044],[1.462240,-3.923486,-6.679225],[-2.679759,8.893998,9.741618],[-4.576179,2.450944,-3.594192],[5.720053,-5.611045,1.971646],[-3.528961,-8.550108,4.877540],[-1.488938,-7.162501,0.997956],[-3.503712,1.278467,9.899939],[-3.020521,0.051151,4.973304],[-0.222622,-4.639590,-3.418730],[5.733174,-2.285374,-2.921546],[4.844065,-7.300254,6.340796],[2.196638,4.252338,-6.571088],[6.078191,-3.387816,-9.689181],[-4.696109,-3.643417,9.535965],[-8.011575,-4.282079,-0.878110],[-9.752172,4.944363,-6.786739],[-5.727593,8.480433,-8.999157],[-6.542440,-8.681009,-7.226655],[6.417831,-1.832394,5.356247],[-7.091962,-5.324485,-6.994968],[-3.871657,-2.642440,1.142704],[-9.276609,-5.042809,3.002935],[9.038949,-2.080292,-3.471548],[8.476461,2.712031,-6.473333],[2.893837,-9.081258,3.029604],[4.832435,9.769856,9.061620],[-8.214667,4.607562,9.620472],[0.850792,-9.034531,0.187928],[-9.454602,-1.299000,-9.612680],[4.922050,-5.997785,0.536621],[-6.866912,7.521009,-6.914418],[6.965540,-7.512024,-2.948732],[9.052663,1.633435,8.006320],[0.038639,1.814650,-7.546214],[-3.291554,3.526643,8.894981],[-5.912827,2.212390,-1.456921],[-6.600484,-0.925012,-7.154338],[6.498389,-9.456021,0.737987],[8.949451,-0.646732,7.757514],[-0.804857,-0.498957,-4.816056],[-2.054828,7.698221,-8.555848],[4.107233,3.613996,1.963899],[-5.129290,-6.482897,4.028019],[3.596447,-3.009221,8.554551],[-8.414218,8.945201,-4.761053],[-9.615994,-1.971086,-9.774857],[0.251365,7.253520,-9.712017],[-6.831054,4.629841,6.241869],[4.305538,0.899191,-4.044627],[3.625568,-5.222324,2.964902],[-7.299188,2.520032,-3.117346],[8.881476,-2.676502,-2.517007],[4.088219,7.183099,0.184652],[-1.428665,8.558774,-8.442886],[-6.395043,-6.280878,-8.690306],[9.524656,-4.515988,1.583008],[5.321098,-4.459609,-7.752446],[-3.202283,-8.375581,-5.433055],[-8.967615,-5.036555,4.184337],[-1.890677,-3.232486,-2.736520],[-3.567030,7.433922,1.503490],[3.221380,7.467978,-7.945080],[8.099395,1.349779,-2.395657],[2.317019,-6.303260,5.686159],[8.025565,-2.354021,-9.712980],[-8.967609,-3.487877,0.842298],[4.628984,-1.250910,9.731426],[-1.405971,9.070493,-9.472633],[1.696647,5.358376,6.306439],[9.614374,-6.496444,-6.744254],[9.403593,9.250393,-7.668492],[1.818677,-0.287336,-8.328646],[-1.967100,-0.528992,-2.613489],[8.260242,-3.062867,-5.620716],[6.491495,-7.776754,0.014940],[4.202223,-7.883949,-4.481545],[5.351873,-3.917850,-3.444006],[0.828189,4.833236,-1.268872],[-7.859994,5.033750,-6.097360],[-6.116635,-0.164882,4.005195],[8.009503,-0.506310,-4.839830],[-3.401203,-5.384011,7.147697],[1.970598,6.599112,-6.089333],[4.328208,6.987007,6.488752],[-5.171545,-9.154286,6.633223],[-1.290482,-5.505729,-4.860079],[2.250181,-9.024266,6.072866],[-5.831296,7.059711,9.360070],[-5.958617,-6.069804,6.173604],[3.959280,-4.697984,-7.354023],[-5.102350,-2.416239,4.514421],[7.097423,-7.620312,-3.656915],[5.939336,-2.282207,-5.852612],[-1.477190,-9.970978,0.118722],[-3.251665,6.900195,-1.130711],[-4.939552,-7.266615,8.350581],[4.999460,9.943158,-0.642466],[9.347054,-2.198217,-2.261222],[7.870947,1.908634,-8.638311],[-1.523066,-3.120814,4.624091],[7.447124,4.248472,-6.539852],[-4.823067,8.631862,4.137431],[7.908830,5.960377,0.333284],[7.147963,-6.873520,-7.631607],[5.421446,2.077788,5.161079],[-2.596926,7.164266,-8.871501],[-0.540763,2.126895,-8.060487],[5.441186,-5.067805,-8.406796],[8.161309,-0.044376,-6.514087],[-8.626886,0.264932,6.591552],[-2.437463,-2.948957,6.616132],[0.719023,3.196496,8.677228],[-0.122477,6.715649,2.859050],[-1.974219,0.615863,-7.586208],[1.240619,8.755284,8.885295],[2.295510,-2.487002,7.383324],[2.837724,0.789094,5.026927],[-2.622369,-4.571470,-2.607599],[1.363763,-2.003326,-8.304494],[7.783278,7.032251,-2.971892],[2.330672,-8.220276,0.121088],[-7.174989,-5.212715,8.878432],[-8.572626,6.343838,-5.295440],[0.617820,-9.542877,-1.737968],[-6.954387,9.895973,4.886529],[-3.027703,5.854237,-0.303430],[-9.804304,7.166537,9.343599],[0.700564,0.496015,-2.299439],[-9.636226,9.144435,1.952363],[3.361838,7.739508,2.331319],[0.020790,-5.582746,-6.878146],[1.223975,5.564762,8.690452],[-8.986923,-3.545112,-8.824718],[3.954992,-9.738249,9.941451],[-8.891525,-2.853230,2.562192],[-0.086854,0.076563,-8.429899],[-9.712887,1.704201,-9.200579],[-3.946674,1.678497,-2.113880],[3.349449,-0.298670,6.792970],[9.611181,4.525010,7.605505],[6.509252,4.372778,-3.622611],[-2.525776,7.069526,-5.468198],[-5.936317,-7.556541,-4.420263],[2.515270,-3.257537,4.457685],[-8.341030,-3.472339,-2.206585],[-3.421218,1.572953,0.588276],[7.336552,-4.666042,8.046436],[2.567646,4.778559,6.691514],[-7.284889,1.843474,-3.640325],[-5.808284,0.226017,-9.619519],[2.277743,0.739929,-9.796971],[-7.485186,-3.536014,6.373497],[-7.564041,-9.186907,-6.221175],[9.141621,-0.166191,-6.914073],[5.640815,5.186175,1.992872],[5.778190,2.892643,1.207680],[1.952022,1.213462,7.742718],[1.169786,4.100115,9.990198],[6.976318,7.029693,-7.235183],[-4.745211,-0.662973,-0.175142],[-9.831340,-8.222503,7.122616],[5.931412,-8.662824,-7.082391],[3.627658,1.963599,7.974028],[1.808405,7.224556,0.110758],[-0.265325,3.572451,3.011645],[-3.832332,0.246534,1.243948],[-6.920537,9.621524,-8.619337],[-5.496320,3.668886,-7.549688],[7.100654,9.205415,-6.952420],[-8.584858,7.509403,-2.877874],[0.481573,-4.900462,2.507362],[7.707409,-7.797871,-8.681959],[8.788987,6.905196,-9.166247],[0.869232,2.758601,-0.806167],[7.132792,-0.165125,7.258033],[-6.199402,9.980770,6.373809],[-8.522273,-2.736183,-4.064718],[1.864457,-9.377705,-8.682129],[3.233283,-4.534935,0.547956],[-5.393139,4.272458,8.430421],[4.949468,0.846717,-2.439654],[-3.157346,-5.467711,4.892223],[1.424446,-4.999821,5.598009],[8.728747,-9.740253,7.891307],[-6.402463,4.122495,-1.195998],[-3.908694,-0.081925,-2.560464],[4.181971,3.894550,-1.942968],[-1.079007,-7.824926,1.368466],[4.119679,-0.524294,-4.705199],[2.498201,4.019231,-9.142454],[2.018032,-4.615764,-1.889122],[-4.731076,8.854186,8.505249],[2.649075,2.050948,-0.402312],[2.750458,7.162462,-7.604391],[-8.085567,4.074747,-8.896262],[3.348827,-4.688949,5.917936],[4.735888,-1.515643,8.946733],[-3.743297,5.569214,-3.333588],[-7.231884,-8.504766,4.201885],[0.794648,-6.473942,-2.765758],[-6.909699,1.393548,6.657179],[3.468154,-3.547833,6.897778],[-0.132144,-4.454148,8.997921],[8.009401,0.573585,-7.394277],[-1.900264,-4.101018,-3.100162],[9.628343,-1.884890,7.240786],[1.446909,-7.356864,9.805381],[-3.782616,8.596947,9.313895],[6.690951,-6.396318,-1.805159],[-2.037188,-0.010448,-0.150144],[6.715264,3.489720,-0.802708],[7.475140,-4.936178,8.922714],[4.002776,8.534571,2.965487],[2.503234,9.517123,6.325907],[-6.820227,1.146994,-8.321488],[8.207372,6.548537,4.976431],[-3.097519,-5.803916,2.555915],[-3.247580,7.148691,0.283409],[-1.868664,4.111451,7.958120],[-2.257288,-3.013099,-8.470754],[1.436534,-8.553867,1.928758],[-7.097285,-2.680750,-6.705042],[-9.432840,-3.592766,-8.933264],[-7.776574,0.984541,-0.434066],[-0.701149,-5.542778,-8.493995],[6.922806,1.808808,5.201241],[-5.813018,-8.824022,-5.620758],[-8.236308,7.768657,-0.744709],[-4.460308,-2.405046,-0.006478],[-0.005137,3.819498,-0.510172],[-8.449075,0.323082,7.735981],[-9.598990,-1.566729,2.258040],[0.393864,-6.569009,-1.232342],[-8.872014,3.565842,-5.394773],[5.654975,9.109776,-1.334883],[6.174836,1.264842,-1.557629],[3.618603,-4.245351,1.160548],[-7.912392,6.431274,3.963070],[8.019197,2.996309,-3.244393],[-2.099179,-6.882696,3.247502],[8.375596,5.767656,0.945119],[-4.427873,-0.281139,4.163269],[-0.792301,-2.365330,-9.681773],[4.695376,4.714933,-6.582938],[7.024235,-6.644695,-2.910724],[-3.939738,-5.186431,7.815586],[0.657761,-1.174846,-3.373158],[9.449774,3.916835,8.322828],[9.596320,1.776277,1.507221],[-0.114843,-3.737837,-7.384293],[-4.572997,3.105764,5.534325],[1.587420,-8.227538,-4.132247],[3.591040,4.680280,-3.362547],[-0.594396,0.229618,-4.163753],[0.751204,5.917956,2.018175],[8.189723,-1.943267,-5.012152],[9.377639,-6.649359,9.434852],[-1.775555,-1.873857,9.533499],[-4.903002,-5.452083,3.733839],[-1.889317,-6.166756,9.123163],[-4.845094,2.834743,6.701314],[-7.622409,7.214849,-2.796698],[4.498253,7.004271,-8.151190],[-8.743531,-8.634466,-7.342359],[-1.843617,8.029022,5.138975],[-4.819915,1.010936,-9.716062],[-3.237307,0.564976,-3.750537],[-0.894399,-6.387417,3.270851],[5.336841,-0.341910,7.135437],[1.006234,3.880775,-3.154121],[8.593049,-1.370963,-7.318837],[7.473739,7.010993,2.361810],[-3.141881,-6.892513,8.877000],[3.107934,5.647743,4.315857],[2.573567,-5.948357,7.754203],[1.302544,-0.585177,0.503159],[-7.954626,8.930000,9.440469],[5.093363,-8.183695,-2.905040],[-7.468986,-5.100094,4.401990],[-8.163651,8.750175,-4.882021],[3.898697,7.307155,7.345453],[-5.376933,-2.700402,-7.275433],[-7.123587,4.821962,6.930990],[6.745196,-0.056012,2.252730],[7.208476,-2.569960,9.362547],[0.167047,-8.482073,-1.101541],[4.385429,8.182548,-9.175245],[4.340714,-8.753870,2.607610],[-8.026259,0.079847,2.130687],[3.241129,-4.829258,6.506817],[-0.349316,-9.622773,3.522483],[-8.961573,6.362274,-3.767588],[0.504398,3.018464,9.205703],[5.044513,5.212014,-8.816339],[-9.593165,0.517214,4.931867],[-0.676130,2.643260,-8.578593],[0.644623,5.705895,-6.265553],[-0.282656,1.282565,5.630495],[-6.861016,-0.540622,4.557326],[-2.805987,-8.924483,-3.465747],[-7.764674,3.002849,7.421720],[7.825454,2.152681,-0.221369],[-5.965578,2.669280,-5.497902],[-3.181018,-4.156367,-3.493092],[2.709867,2.513283,-6.069535],[0.949536,-4.081663,-7.052536],[-4.195651,-4.370286,-2.140920],[-5.861033,1.971776,-8.815354],[-5.594248,-4.750364,1.852045],[3.868976,-4.106152,0.300852],[-3.279062,4.919446,0.125806],[0.077973,1.797727,9.856617],[-5.414439,3.594307,-4.257465],[5.603259,-6.046826,4.502702],[-8.573789,4.375426,7.043401],[4.866234,0.861520,-7.052865],[-1.148854,1.749456,8.258852],[3.446761,-1.459187,6.542209],[-2.634347,4.693152,-0.001200],[-1.471415,6.958774,9.207635],[-8.047188,2.446945,-4.478350],[2.221128,7.808685,-1.488227],[9.409607,-2.690859,-0.592005],[-6.403093,-3.637656,-4.090006],[-4.302275,3.061831,-6.013624],[-7.759795,1.975395,-2.205560],[0.084632,-1.299762,-9.921532],[3.501709,-0.450898,1.794666],[4.572132,4.896524,-6.897307],[8.472253,-0.903617,-7.067134]], dtype = "float32")#candidate|1634|(550, 3)|const|float32
const_1635 = relay.const([[-3.349063,-8.460935,-4.471198,-6.372167,-6.562034,1.842753,6.348825,-6.643476],[-0.109156,-2.046316,9.501186,-8.815775,7.502333,1.431849,-0.178379,4.854986],[8.691807,5.997483,-4.201180,-9.314187,-0.181809,3.470192,-6.695008,-5.151013],[-8.451220,-3.503588,-1.485570,6.129295,3.614831,5.713741,2.013322,-1.617098],[-6.803244,-3.377800,1.941374,8.960741,9.346007,-5.035600,-2.865533,-7.768349],[6.367651,5.700941,-0.570165,-8.656264,8.349982,6.198471,-2.950182,9.956040],[-9.631292,5.696504,-4.870022,0.213183,5.197720,-4.542507,6.453083,-3.627862],[8.110220,-0.183142,2.851471,5.634136,-1.698803,2.385553,6.968540,4.527672],[-7.748789,4.063825,6.658292,-1.310647,-5.648192,4.894296,-2.528162,5.450823],[0.909021,6.895960,-6.702942,2.415436,7.145708,7.201674,6.922121,-6.728373],[5.702098,2.908368,9.767499,-0.705635,-8.272863,3.737612,4.115981,-7.855081],[-3.251126,2.853503,8.540847,7.457877,3.628143,5.418891,7.264064,0.053579],[1.513859,9.667944,-2.918002,1.288215,3.685759,3.352501,1.038515,0.246857],[7.128098,-4.987290,8.829076,-0.146348,-8.113193,-8.806773,6.729890,-9.516193],[-9.155855,9.021318,9.504530,4.286451,0.540482,-6.335742,-5.546131,-9.370571],[-6.861320,-2.155341,-6.282068,2.087704,-1.768536,-5.326657,4.596128,9.097818],[5.939926,-6.509422,9.593999,4.791754,2.258503,0.236106,-4.369465,5.809182],[-9.267823,-2.838233,-6.811041,2.976686,9.343901,3.693788,-0.983269,-5.875474],[7.383902,9.569006,-3.269488,-8.651879,-9.835158,-9.401956,6.782292,7.316663],[7.626787,6.187056,7.163136,8.596048,-2.205634,2.850075,0.163745,-9.200077],[9.294578,1.710345,6.591369,1.612096,9.402240,-7.236797,3.819250,-2.309605],[8.035540,3.912574,-1.805712,-7.353302,7.204694,4.966689,6.697000,1.904377],[7.707327,8.259240,-0.340324,-2.815471,-2.107157,0.709217,9.881397,-3.829567],[6.655200,5.969005,-5.523763,-0.828280,-1.388164,-3.703951,-3.237058,-9.915681],[-5.151934,-1.232450,-7.626908,-4.247850,9.437655,-4.387590,0.580840,4.259561],[-7.438948,-7.662953,-7.883575,-6.761934,9.731586,0.264789,7.131419,7.810767],[2.690724,-4.166212,7.318975,-9.068163,-6.773981,5.179741,7.114348,-6.706548],[9.482567,5.471636,-0.337827,-1.396831,-5.638683,5.003883,9.701763,-7.374166],[-5.243696,-1.356035,0.614616,-0.215142,-7.606834,-5.271403,-1.095317,3.404513],[5.882451,-1.670660,8.498414,0.044782,-5.055358,7.342723,-7.326602,-9.024303],[-4.401888,-3.543825,7.657040,-7.953994,-6.312724,5.693757,8.637693,-7.222250],[1.959087,-5.133504,-9.959208,5.055081,-9.686789,-6.778089,-9.823359,9.405720],[-3.591128,-9.950826,-5.469896,6.371562,6.530635,-4.233167,5.972941,-2.114822],[0.959372,7.859593,-7.708865,-8.419376,1.618232,2.187834,1.404014,3.700008],[-7.346381,8.168007,-4.960011,2.985807,7.707730,-1.083241,8.628272,-7.886684],[-3.143377,-8.077924,-5.550910,6.884109,3.542246,7.664582,-1.268586,-1.677594],[-5.999448,3.633459,-9.398396,9.639400,-7.384633,9.780823,-9.983619,-8.798897],[6.359160,8.470703,3.198780,-9.323109,-2.169681,6.676097,-7.771755,1.366469],[9.219654,8.337897,-0.394386,-9.054121,-2.986075,-4.940658,4.465269,6.649813],[7.069163,-0.605085,-8.617284,0.306961,-3.161268,8.963517,7.632384,6.829247],[7.932301,-0.214938,1.211391,6.787559,-6.533457,-8.184899,-3.305418,8.293205],[6.769315,7.165290,-2.167418,-4.630641,0.759316,3.587954,-2.615101,-1.887705],[9.599479,2.181617,1.554476,-6.788769,-5.658634,9.006385,4.871001,-6.313740],[-2.595860,-4.796080,7.037627,1.660257,-8.313777,5.971302,3.108720,-7.567000],[-5.164076,-6.532049,-4.801454,-0.578691,7.746338,-5.518512,-7.338607,1.693916],[-9.865721,0.673036,-1.292312,-0.419889,9.155148,-4.140305,4.024573,0.897299],[-9.959613,9.508486,-3.647792,-0.653933,2.752377,-0.609314,5.197434,-4.765506],[8.141851,6.122578,-3.404200,-7.632767,1.080124,3.491492,-1.644724,5.556760]], dtype = "float32")#candidate|1635|(48, 8)|const|float32
var_1636 = relay.var("var_1636", dtype = "float32", shape = (429,))#candidate|1636|(429,)|var|float32
call_1632 = relay.TupleGetItem(func_1223_call(relay.reshape(var_1633.astype('uint64'), [84,]), relay.reshape(const_1634.astype('float32'), [1, 1650]), relay.reshape(const_1635.astype('float32'), [384,]), relay.reshape(var_1636.astype('float32'), [39, 11]), ), 11)
call_1637 = relay.TupleGetItem(func_1228_call(relay.reshape(var_1633.astype('uint64'), [84,]), relay.reshape(const_1634.astype('float32'), [1, 1650]), relay.reshape(const_1635.astype('float32'), [384,]), relay.reshape(var_1636.astype('float32'), [39, 11]), ), 11)
func_1356_call = mod.get_global_var('func_1356')
func_1359_call = mutated_mod.get_global_var('func_1359')
var_1643 = relay.var("var_1643", dtype = "float32", shape = (352,))#candidate|1643|(352,)|var|float32
call_1642 = func_1356_call(relay.reshape(var_1643.astype('float32'), [4, 8, 11]))
call_1644 = func_1356_call(relay.reshape(var_1643.astype('float32'), [4, 8, 11]))
func_1328_call = mod.get_global_var('func_1328')
func_1334_call = mutated_mod.get_global_var('func_1334')
var_1647 = relay.var("var_1647", dtype = "float64", shape = (1536,))#candidate|1647|(1536,)|var|float64
var_1648 = relay.var("var_1648", dtype = "uint64", shape = (160,))#candidate|1648|(160,)|var|uint64
const_1649 = relay.const([[5.307471],[-6.346535],[-9.280875],[-3.097427],[-5.531740],[-6.376148],[0.703287],[-6.253964],[4.566053],[-7.195944],[6.503189],[-9.997745],[4.603230],[-5.114558],[-4.589713],[-6.243779],[3.679675],[3.016620],[-3.748988],[7.318001],[8.397389],[-8.317916],[-8.779252],[5.911565],[7.134526],[-1.658490],[-0.504405],[-3.316783],[-7.338220],[-1.693678],[-1.737295],[7.134089],[1.153124],[6.172141],[-4.742665],[6.998768],[-6.649295],[-5.456615],[-9.517046],[-1.221786],[2.640078],[-8.796137],[-3.197196],[-4.059778],[5.553841],[8.708631],[0.405013],[-2.615199],[8.321376],[-5.330393],[-1.917405],[-0.224467],[3.479513],[9.207417],[-8.597683],[6.135789],[-0.333648],[3.266661],[-4.491846],[-7.184737]], dtype = "float32")#candidate|1649|(60, 1)|const|float32
call_1646 = relay.TupleGetItem(func_1328_call(relay.reshape(var_1647.astype('float64'), [16, 12, 8]), relay.reshape(var_1647.astype('float64'), [16, 12, 8]), relay.reshape(var_1648.astype('uint64'), [2, 80]), relay.reshape(const_1649.astype('float32'), [60,]), ), 3)
call_1650 = relay.TupleGetItem(func_1334_call(relay.reshape(var_1647.astype('float64'), [16, 12, 8]), relay.reshape(var_1647.astype('float64'), [16, 12, 8]), relay.reshape(var_1648.astype('uint64'), [2, 80]), relay.reshape(const_1649.astype('float32'), [60,]), ), 3)
func_776_call = mod.get_global_var('func_776')
func_780_call = mutated_mod.get_global_var('func_780')
const_1652 = relay.const(6, dtype = "int64")#candidate|1652|()|const|int64
const_1653 = relay.const([-4,-3,-7,5,1,8,-3,10,4,-2,2,9,-10,-7,2,7,8,-4,1,5,-3,9,3,6,5,-8,-7,3,5,-2,-2,4,10,-5,7,-10,2,6,9,3,-1,-3,9,6,9,-2,8,1,5,-9,-5,-3,-10,-2,-1,5,5,10,5,9,-5,-5,6,1,1,4,-10,-2,-3,7,1,-6,1,2,2,-10,-2,-10,-10,-2,2,8,10,-10,6,9,-1,-6,2,10,1,1,-4,4,3,-8,9,-6,-8,3,8,-3,-8,-3,9,4,-3,3,-7,3,10,-6,-9,-1,-1,-3,8,-7,-7,5,-2,-3,-4,-4,3,1,-1,6,9,7,2,8,5,6,-6,5,-10,2,-7,2,-4,-5,10,-4,-9,-1,-10,10,-4,7,-7,-7,3,8,-8,9,-5,-8,8,-6,-5,-5,-5,2,1,-1,-2,-5,10,6,-6,-3,-1,-10,4,-3,4,-8,5,10,9,-6,10,7,-7,-9,8,-7,-2,8,-2,7,-1,7,-4,5,8,6,5,7,8,6,-9,-7,-10,7,7,10,-8,5,-3,7,4,-9,-9,-2,6,5,10,4,-6,-2,6,3,8,-8,-10,4,10,-4,4,8,-3,5,4,3,-2,-4,-8,4,7,-9,-9,-1,-8,10,3,2,-10,9,-6,-5,-9,7,-6,-3,5,9,7,-4,9,9,-3,-7,-9,8,-1,6,-2,7,-5,2,-4,-3,5,8,-5,-5,9,3,10,-5,-4,1,3,-5,-8,-10,10,-3,-3,8,-7,8,4,-4,-3,-5,8,-5,6,3,9,-8,7,5,-4,9,5,-7,-9,3,-10,10,-6,10,5,8,7,4,-9,7,1,5,5,4,3,-5,8,10,10,-8,5,10,3,-5,4,-6,-8,-10,-4,-7,6,1,-9,9,-3,8,-4,10,-4,-10,9,-1,6,9,10,9,2,-9,1,4,-7,-1,-1,-8,8,-1,-3,-3,8,9,10,1,7,2,-9,1,-9,9,-3,-4,5,7,10,7,2,5,5,3,-7,8,-1,4,-3,-1,1,9,-1,-4,-4,10,-8,-7,2,-2,5,6,3,8,-4,2,4,-1,-8,7,-5,-10,-3,-7,7,3,1,9,-1,10,8,9,5,-7,5,9,-3,7,5,3,3,-5,-7,-10,1,-4,-4,-1,4,-2,-3,1,9,4,-9,-8,-4,9,-5,-2,9,-7,2,1,-3,-7,3,2,5,8,4,-10,-8,2,8,-2,-3,-1,7,2,-5,8,-6,-2,8,-9,-7,-3,-8,10,10,-4,-3,9,-6,-9,8,9,-10,9,2,-10,-6,3,7,-1,-5,1,1,7,-9,-8,-4,2,-1,-1,8,-3,-4,10,10,-10,8,5,9,9,-8,6,-8,-7,-1,2,-2,4,1,-7,7,10,-9,7,6,-8,4,10,4,1,-8,3,-7,-5,-4,3,-2,-9,7,8,3,-2,8,1,3,-7,4,-2,8,-1,-2,4,-7,-2,8,-10,6,9,5,-7,-1,-9,4,-6,-9,-7,-3,-4,3,-5,-7,-3,10,-8,2,-5,-10,8,8,-8,-4,9,-5,6,-2,-8,-9,-4,5,-5,-7,-1,-5,-1,-4,-1,4,-6,4,7,-4,-6,8,-3,4,-9,6,-8,-9,-5,9,-1,-5,-2,-10,4,-3,-8,-2,3,7,-7,-10,-6,-5,3,-7,9,-1,3,-7,5,9,1,4,-7,4,6,8,-4,-6,-1,1,-7,8,-6,-6,6,-6,-9,9,-3,-8,10,4,-1,2,1,1,-8,9,5,-8,-3,8,-7,7,-1,-1,-3,4,3,-7,9,-6,6,-4,-1,3,-9,5,7,9,9,8,5,7,10,-6,-1,-10,8,-9,6,-2,-1,4,2,-6,3,2,-10,8,2,-10,8,9,4,4,10,-7,-6,-8,2,9,2,3,-10,-1,-9,-5,-1,-3,-2,4,-7,-4,-2,1,-8,9,-2,3,7,4,7,1,4,4,4,-2,1,-4,-8,-8,7,-8,4,-3,-7,5,8,5,-1,-2,7,6,7,2,6,4,1,-4,-5,-4,-6,10,6,-8,4,-1,-1,10,8,-5,-4,-8,3,10,1,-2,-2,2,10,6,-9,5,-6,10,-9,-8,4,-9,-10,-4,-2,9,-1,-3,-1,2,-8,10,4,-5,2,7,1,-2,-5,-3,3,3,3,2,7,-3,-5,-6,-2,-1,6,10,-5,8,9,7,3,5,-7,1,-2,-6,7,5,5,-4,5,-8,-8,-10,-8,-8,-8,9,9,9,6,8,9,3,-9,-7,-2,-5,-1,-7,4,4,-6,7,-4,-7,-4,-4,-6,9,3,-10,-10,5,-9,-2,6,5,10,-9,10,5,-9,-9,5,2,3,-2,6,6,-10,10,-4,-1,-7,-9,4,-3,2,-2,9,4,8,6,-5,-1,1,-4,6,-1,4,4,-3,-5,-10,-1,-10,2,3,2,-8,-5,-4,-4,-2,5,-5,6,-5,-3,7,-3,-1,5,-3,-3,1,10,7,-8,-8,-9,-4,-1,7,6,-9,10,-6,-3,-3,-1,-6,-10,6,-6,-2,7,9,7,-3,-9,-1,-2,8,-7,-4,5,-9,3,-2,-10,-3,2,-7,9,1,-4,-10,3,-4,7,9,7,7,-3,-10,-7,2,-6,-10,10,-4,-6,-1,-2,-9,2,-1,6,-1,-8,2,6,5,-2,9,-6,6,-9,3,1,-10,-10,4,-8,-4,5,-2,-1,-5,1,5,-8,9,10,-7,-4,6,8,9,-4,-4,3,2,-2,7,2,9,6,5,2,7,-1,-9,2,4,-2,-6,4,-9,6,8,-9,-6,-6,1,5,3,10,2,9,7,-6,-6,-1,-5,-10,-5,-1,-6,-3,7,4,3,-4,-5,3,-6,-4,-7,7,4,-4,-6,1,4,-8,4,-2,7,2,-9,-3,5,-9,-4,6,-2,8,-5,-2,5,-1,4,-5,-7,5,3,-5,7,3,-8,1,9,-10,8,-5,-3,-1,-8,-10,-3,-5,2,7,1,1,6,9,-1,10,-2,2,1,-6,10,-6,-10,-1,8,-4,-7,6,8,9,-8,-9,-3,-8,6,3,-10,1,7,-4,10,-2,6,-10,-7,4,-7,-6,5,3,7,-7,5,9,-10,5,-3,-6,-6,3,-5,-9,-9,-3,10,-6,-3,6,-1,-10,-9,8,3,-3,2,4,-3,2,-7,-8,2,-6,7,5,-8,-6,9,9,9,10,-7,9,-7,-2,7,-3,-4,-5,2,6,2,-5,7,2,-5,7,9,2,8,-10,3,-3,-4,-5,-6,-4,-4,-1,4,-5,10,-1,-10,2,-6,-1,10,4,-2,-8,-2,1,3,7,9,-6,-5,-5,9,-1,4,2,7,5,6,2,-10,-4,-6,10,-2,-4,3,-10,-9,-5,-4,-6,-2,-2,6,6,8,-9,-10,10,5,-7,-3,1,9,-4,3,-3,1,-5,1,5,3,4,4,3,7,-10,-8,-2,-6,-9,-6,-8,-10,-6,-6,10,4,1,9,-1,-6,7,-3,3,5,10,4,6,3,-7,-2,8,-3,8,-5,-8,-2,-6,-4,-4,-1,-8,-6,-1,8,-8,6,-8,5,3,-5,-10,8,1,5,10,-4,2,-7,-7,-2,-7,10,-9,1,4,5,-2,8,-4,9,-10,6,-2,-5,-8,-5,7,-2,2,-10,-9,8,7,-5,10,9,-8,2,-8,1,7,-2,-1,3,-8,-10,8,-10,-6,10,-2,8,3,-10,-8,-8,-6,1,5,-3,-7,-9,2,3,-6,-6,3,-6,5,-9,8,-9,-10,-6,-4,-7,5,-7,-7,5,-5,-10,8,-5,6,7,3,-2,8,-7,8,-5,-4,-10,-5,4,7,-8,-2,9,9,3,5,7,3,6,-2,4,5,6,-8,-8,4,1,1,5,-7,-3,4,-6,6,8,-4,3,-6,-7,-9,1,-3,3,-2,3,7,-2,8,9,9,-3,4,2,6,4,4,-1,8,10,-2,-9,-1,-3,-6,-2,-2,10,2,5,1,5,5,-4,-10,2,9,5,2,-6,8,5,-4,7,-9,4,-2,-5,5,-1,-6,-10,-6,-3,-1,-9,9,-1,1,9,-10,9,-3,10,-6,6,-8,4,-1,2,-6,-3,7,9,3,7,2,5,2,5,8,9,10,-10,10,1,5,4,7,9,1,3,-1,1,6,9,-9,-2,2,8,-7,2,4,-1,7,-2,5,-4,-6,10,-2,9,-9,-10,6,5,-10,5,-2,6,-6,10,6,8,8,5,8,1,7,-8,-3,6,1,9,8,3,-4,7,-8,3,4,-5,-5,10,2,-7,-3,10,6,7,3,-10,-6,10,-4,9,-2,-4,5,-1,4,-3,2,-2,1,2,1,4,9,-1,-8,4,-7,8,-2,10,-6,-4,-6,-7,-8,-2,1,8,1,-6,2,-10,-8,-2,7,8,-2,-4,-1,-5,1,9,7,-3,-7,-9,9,-7,-10,-9,10,4,4,-10,10,3,7,3,-9,4,5,4,-5,-3,1,-5,3,-3,-7,1,10,-1,8,-1,-2,3,-10,-3,10,-3,-2,-2,-6,-2,-7,4,-9,-6,-1,-3,4,2,3,-1,5,-5,-2,2,1,-3,-10,-8,4,-7,-1,-9,6,-8,-9,3,-5,-1,-7,-5,8,9,-6,9,2,-4,6,-9,7,3,-8,-9,7,10,-2,2,-2,10,-9,8,4,-6,5,5,3,-7,-6,-6,4,-7,-10,8,10,-9,-6,-2,-9,3,2,-6,-9,9,-9,10,-2,2,6,3,-8,8,-1,4,-7,-4,6,7,4,1,-1,-9,-10,5,10,3,-2,2,1,3,-7,-6,-8,-10,-9,8,-4,2,-9,-9,7,-7,-2,4,6,-1,6,-6,10,-9,-7,-8,-5,2,-9,2,-2,7,-9,7,-8,-8,6,9,10,-7,-8,-7,-7,-8,9,-4,-1,4,10,5,10,4,-7,-3,2,3,7,2,8,-2,-2,-7,7,-2,3,-7,-1,10,-4,7,3,6,10,5,10,5,4,-4,3,8,-5,10,5,-8,-3,5,-4,7,10,4,-9,-3,-10,4,5,1,6,-8,9,10,-10,9,7,-10,8,-9,2,10,9,7,-5,-5,-8,-1,-10,1,7,6,6,3,9,-10,3,2,3,7,-6,8,7,2,-2,9,-5,-3,10,-4,5,-7,4,-2,7,-5,-2,-8,4,-6,5,4,-10,-8,3,9,-7,-8,-6,-8,-8,7,-9,8,-4,-10,2,8,2,-4,9,-3,-2,7,-9,-2,-1,-8,-5,-4,5,-10,9,-10,-4,-6,-10,1,-9,-1,-5,-9,3,9,-6,-8,6,-9,-6,5,-5,-4,9,-8,-4,-1,1,7,7,-1,8,3,7,-10,3,2,-6,5,-2,6,-2,-6,4,5,9,6,5,-3,3,5,9,-4,-4,10,1,-3,-2,-4,-2,10,6,1,5,-2,-7,4,4,9,-6,3,5,-10,5,-5,-4,-10,-1,10,5,4,-10,-6,-6,-2,5,10,1,1,6,3,-1,8,4,-9,1,10,2,6,4,2,1,-1,4,10,-8,-7,8,2,-5,-2,4,8,10,6,1,-5,-2,7,-8,5,4,6,9,-5,-9,-3,-10,9,-6,-6,-6,9,7,5,7,-3,2,-2,-7,9,3,-9,4,5,-6,7,9,-2,-6,-2,-5,-1,-6,1,-9,1,2,-6,-1,-6,-9,-9,-3,-5,-7,9,3,10,2,-3,2,2,6,-8,-9,4,-9,8,-5,10,-1,-4,6,4,-7,-8,2,1,-2,-7,-7,-8,-5,8,-9,-3,-7,5,-3,3,7,-9,5,-7,10,7,4,-4,4,-10,-2,3,10,-5,8,-4,-1,-2,-4,-3,-4,2,6,8,1,2,10,7,7,6,-9,-8,3,9,2,2,10,3,-3,7,10,-9,9,2,-7,-9,9,9,1,9,-7,9,-4,-7,-5,3,6,-8,8,-10,10,-3,9,1,9,-3,-1,-8,-7,4,-1,-7,-8,1,5,-3,3,6,-10,-3,-8,-7,-1,6,10,-9,-8,10,-3,4,-4,-5,-4,8,7,-3,8,-4,3,-6,-1,-5,-1,-6,6,2,-8,-7,-7,6,-8,7,-7,4,10,-4,-5,1,-4,2,-9,-1,3,-9,7,-2,-4,-1,-1,-2,7,1,7,-9,9,2,-8,-4,3,1,1,-4,-4,8,10,-6,6,-8,-9,3,-8,3,7,7,1,1,3,6,8,3,-4,4,6,4,-9,-3,-1,5,4,-10,-1,-8,4,-4,-8,10,-7,3,-6,-9,3,4,-8,3,-2,-8,4,9,-8,2,-1,-9,1,-10,-8,-4,10,-4,-8,10,-2,6,2,7,8,7,4,-6,7,-3,-6,5,-4,2,-8,5,9,-7,7,-3,3,-6,6,-3,-9,-8,-1,9,-4,1,-5,3,8,-7,3,-9,9,-5,-7,-8,3,1,10,3,-5,9,1,-4,-3,-5,10,-5,1,-2,8,-7,7,-9,10,-3,6,-4,4,-7,10,3,6,-7,-8,5,10,-9,2,1,9,8,6,4,2,6,3,-10,-7,-8,-7,-3,5,-3,9,8,10,3,7,-3,-7,9,-8,1,-5,2,-1,8,-8,-4,4,5,7,-9,3,3,3,-2,-10,-8,-3,8,7,2,8,-4,-8,-8,5,9,-1,8,4,-5,-6,-9,5,-2,5,10,2,8,3,4,3,-5,-6,8,-6,4,8,-10,-3,7,-8,5,-3,9,1,3,7,-8,-3,-4,-1,-1,-2,-2,-3,6,10,-3,-6,-8,-6,-1,-10,-7,-7,-2,-7,-9,-1,-7,2,8,-7,-4,3,-8,-2,1,7,-5,-7,5,7,5,5,-4,7,8,5,7,-3,-7,5,8,-4,-10,-9,6,-9,6,5,2,4,-10,-3,6,-3,2,1,-3,5,7,-8,-10,6,-10,5,-6,3,9,2,-3,-10,-6,7,7,3,-3,-7,-6,8,5,-10,-4,7,-9,1,-6,7,4,-1,5], dtype = "int64")#candidate|1653|(2640,)|const|int64
const_1654 = relay.const([4.728904,9.322813,9.706881,-3.255505,-5.005151,-2.909945,-3.121697,-9.464649,-7.477554,9.984885,3.490169,-9.196951,9.598593,2.131708,-0.294033,4.697519,3.562103,-5.181619,2.282613,-6.661306,0.142282,0.220891,-5.275449,-7.855477,7.614368,8.124040,-4.591461,0.853180,8.136925,-1.893732,-1.749110,5.172936,-4.636684,-5.918050,-8.184985,9.059085,1.016043,-8.919505,-6.301250,8.834548,-5.029036,-0.969188,-7.859997,-4.114773,5.101147,6.753973,-3.817845,4.756921,-6.641431,9.138597,-8.457992,-0.670748,7.718915,2.909683,-3.817550,-9.208917,1.173738,8.242113,-4.097436,-3.208864,-0.091823,1.149486,-0.011589,1.766099,-4.924680,-7.744327,0.499239,9.918508,1.587408,-1.046744,0.749011,-3.051648,9.911013,-8.503944,-6.641040,2.124910,-7.013036,3.358533,0.790812,1.658301,8.032505,-2.766251,-4.440528,-0.254376,3.956349,3.476073,6.890984,1.118806,5.925089,-6.081233,-4.886194,-7.118835,0.543111,-8.815324,-9.500992,-5.121164,3.629096,-3.067975,-9.976104,1.642357,9.508795,-4.520181,-3.092215,-9.335864,8.597504,1.379651,-5.567886,-3.595864,-6.445529,0.926920,-6.598253,-1.344400,-8.381323,-9.897257,8.648250,-1.963116,-7.858177,0.845734,2.777649,9.447011,9.600515,-0.699781,-4.825267,1.968547,7.410555,-5.090447,-4.788934,0.142802,1.216452,-6.245607,5.645692,-2.690701,9.761425,4.337866,8.376045,-4.118327,2.912376,-5.671732,2.383742,-7.002272,-5.209755,8.950738,-2.740762,-2.723510,-9.485180,-5.470110,5.801749,6.360131,0.629752,7.172452,5.872403,0.795698,0.220431,3.687352,0.123045,8.692786,-7.034231,-2.415885,-1.011298,-7.390438,6.597942,-6.908068,5.518626,-0.708681,-7.544326,6.707039,8.227342,7.436821,7.274682,4.118465,-3.028355,-0.553946,1.096599,3.680636,4.246164,-0.373716,8.327109,-2.307795,0.072546,0.001332,-7.887309,2.301273,4.670862,-8.489184,6.771459,0.060861,6.796108,-6.693207,-3.224406,-9.531497,-7.165248,2.183882,1.876320,-2.366464,-7.782721,4.220892,2.930160,-8.875963,1.030316,5.052317,-0.355299,-2.141534,-4.293360,6.474315,3.138551,7.686532,-6.403447,0.591808,-4.247478,-4.671402,9.453411,4.804547,4.759494,3.114084,2.997206,5.380205,0.589496,6.147281,9.757949,-1.228540,-8.850970,-0.125128,-1.241267,-6.254333,6.245115,9.302998,-0.103361,5.471863,-9.628461,-2.645593,2.434581,-8.386050,-6.152816,7.785706,-3.509713,-1.318816,3.436341,4.049650,-2.002714,-2.658613,2.630211,-3.942115,-4.963460,0.019386,-2.304297,-0.368185,3.930112,-7.549267,-0.775590,1.532992,1.242188,7.012055,-2.014734,4.489146,2.425558,1.065623,2.235840,-1.223081,1.492917,7.360834,-3.197838,-2.033761,-2.599367,0.148502,-1.106176,1.944657,-6.992275,-0.229215,6.052294,3.785782,3.229972,6.102876,-7.123279,-4.300866,5.116879,0.987209,-9.504432,-9.227167,-1.992626,0.806307,-3.364579,-7.845532,-3.104871,-5.453858,-4.805446,-5.010335,-3.100622,7.605001,3.044248,-6.657980,4.391176,-6.375333,3.509510,-6.758806,-8.678101,-4.292923,-9.414614,5.634408,5.286047,-1.646281,3.470998,4.924973,4.370532,-9.755260,6.971826,1.197930,-4.636592,-0.020977,-4.480337,9.913806,-6.514771,-0.477826,1.408925,2.327845,5.403804,-7.263899,-0.954113,-1.521444,-2.709524,9.434927,7.402151,-9.339020,-1.557631,-2.062444,7.099745,-5.505979,9.229032,-7.749460,-2.750464,-2.608307,-7.193895,8.621318,-3.860323,-1.997960,-1.994089,-2.338543,-8.256030,-4.368453,6.358651,-0.328490,-3.585120,3.445553,4.624689,-3.689729,6.374102,4.347044,-8.387687,8.510053,-3.342525,9.613107,3.942785,-9.372474,8.013264,-6.623609,7.123200,8.998033,8.436724,-0.547576,7.487936,0.124634,2.923001,-5.421135,8.967869,-5.535702,8.882320,-4.940543,-3.027863,-4.085235,3.224765,-8.025878,7.562281,3.429024,-3.701455,6.163256,-7.691775,4.923384,8.217490,7.637047,1.573693,-0.016820,-8.182606,1.465474,-4.103569,-8.245248,-4.366092,-9.628271,-9.544870,9.903742,7.000900,-2.426676,0.071419,3.931313,2.453560,1.262350,7.341474,4.806235,-9.520118,-9.985621,1.032487,3.617770,3.566766,8.671385,9.358800,1.475272,-5.976124,-5.330294,4.584424,-8.453689,2.134256,5.529687,-1.923107,-5.879828,8.888690,3.789903,0.077648,-9.658951,-5.168558,-2.189888,-1.880436,6.704419,-4.075710,-8.494027,3.636704,-7.587180,-6.890362,6.273703,7.269878,-9.738883,-1.277588,3.993122,-3.896687,1.363180,4.657749,-4.888854,6.583545,-0.960752,2.931004,1.936503,-5.641032,8.331222,0.724144,3.675731,-8.601899,4.028886,5.247939,-9.466021,-2.487682,-3.607277,-0.691741,-7.174177,-6.851567,8.726310,5.526218,3.300318,-8.592762,7.476127,9.015008,-1.962448,-2.205807,4.310459,-4.260135,7.332683,0.484099,5.532437,-4.864246,8.971726,-5.789220,-2.727228,2.537162,5.213771,8.148501,6.554730,4.716428,-0.095489,8.312358,7.955053,-8.274991,-4.293408,0.376491,2.046661,6.500805,-8.138276,7.790497,-0.901499,-0.630876,-6.750655,-1.806920,2.730645,-3.744919,0.736108,4.428525,7.459709,4.630333,1.547448,2.513195,-0.206738,4.498928,9.141087,6.295370,3.660328,5.368738,5.620871,2.759683,-7.580480,6.396210,2.237245,-3.520105,-4.043167,-7.003948,-3.591785,-9.724659,9.257228,-7.286570,-5.279735,-9.743096,1.208649,4.562813,4.860374,1.363919,-4.915340,9.548320,0.777068,1.098830,6.551384,9.055741,4.847761,-0.127907,2.562643,6.382873,-4.150389,6.287262,-9.523600,7.238836,6.201539,7.488965,8.219538,3.596187,-0.642559,-7.089497,9.264757,-8.822100,6.127630,6.105974,9.428800,-7.522219,-2.995944,1.513454,-0.623722,-5.574928,-5.647016,-4.903369,-1.313686,-6.183839,-4.330997,-2.949474,9.770348,-4.188604,7.651284,1.959921,9.611946,-6.739150,-3.353071,-4.916776,-7.049155,-6.292252,-2.731101,-9.228930,4.672339,2.927536,8.203471,1.327538,-3.739338,3.332649,2.833909,-9.964078,-3.884033,-8.668510,5.669422,-9.206717,8.807611,-2.779690,4.771860,-1.721181,8.993917,-8.167662,6.753183,3.600880,6.695472,4.986912,-4.582294,6.632101,-6.501492,5.214680,-7.931470,-0.608936,-6.932599,6.860612,1.549217,-0.239771,-0.589950,-7.018728,-7.887362,8.516773,-0.770903,-4.859647,4.251414,-8.515325,7.618173,7.138437,3.389147,4.731379,-5.846655,1.127798,-9.690367,-2.641188,-3.165148,-6.142965,5.163917,-3.415420,-2.686377,-3.485146,9.062089,-1.736960,-0.374516,-4.484876,3.634835,2.545891,4.138538,5.372141,6.818067,-2.650734,-8.379116,-3.704669,-4.981624,-4.972796,-4.510002,-9.994979,5.047963,-3.657944,-6.782715,7.637951,0.599592,7.786960,8.111151,-6.072216,4.863959,-7.186434,-8.113656,4.075529,9.097586,0.802116,-9.743946,6.311905,-7.055317,4.421917,4.984151,-6.386190,9.558061,3.431445,8.530365,6.271666,-8.493575,-5.915176,1.288260,7.068034,4.253008,-8.328740,8.152436,9.036406,8.061149,-8.605698,0.045323,6.974713,3.624468,7.919887,5.936080], dtype = "float32")#candidate|1654|(676,)|const|float32
call_1651 = relay.TupleGetItem(func_776_call(relay.reshape(const_1652.astype('int64'), []), relay.reshape(const_1653.astype('int64'), [11, 16, 15]), relay.reshape(const_1654.astype('float32'), [676,]), ), 2)
call_1655 = relay.TupleGetItem(func_780_call(relay.reshape(const_1652.astype('int64'), []), relay.reshape(const_1653.astype('int64'), [11, 16, 15]), relay.reshape(const_1654.astype('float32'), [676,]), ), 2)
bop_1657 = relay.divide(const_1649.astype('float32'), const_1653.astype('float32')) # shape=(60, 2640)
bop_1670 = relay.bitwise_or(const_1652.astype('uint16'), call_1642.astype('uint16')) # shape=(4, 8, 11)
bop_1673 = relay.bitwise_or(const_1652.astype('uint16'), call_1644.astype('uint16')) # shape=(4, 8, 11)
bop_1679 = relay.less(var_1647.astype('bool'), const_1649.astype('bool')) # shape=(60, 1536)
output = relay.Tuple([call_1621,call_1632,var_1633,const_1634,const_1635,var_1636,var_1643,call_1646,var_1648,call_1651,const_1654,bop_1657,bop_1670,bop_1679,])
output2 = relay.Tuple([call_1622,call_1637,var_1633,const_1634,const_1635,var_1636,var_1643,call_1650,var_1648,call_1655,const_1654,bop_1657,bop_1673,bop_1679,])
func_1685 = relay.Function([var_1633,var_1636,var_1643,var_1647,var_1648,], output)
mod['func_1685'] = func_1685
mod = relay.transform.InferType()(mod)
mutated_mod['func_1685'] = func_1685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1685_call = mutated_mod.get_global_var('func_1685')
var_1687 = relay.var("var_1687", dtype = "uint64", shape = (84,))#candidate|1687|(84,)|var|uint64
var_1688 = relay.var("var_1688", dtype = "float32", shape = (429,))#candidate|1688|(429,)|var|float32
var_1689 = relay.var("var_1689", dtype = "float32", shape = (352,))#candidate|1689|(352,)|var|float32
var_1690 = relay.var("var_1690", dtype = "float64", shape = (1536,))#candidate|1690|(1536,)|var|float64
var_1691 = relay.var("var_1691", dtype = "uint64", shape = (160,))#candidate|1691|(160,)|var|uint64
call_1686 = func_1685_call(var_1687,var_1688,var_1689,var_1690,var_1691,)
output = call_1686
func_1692 = relay.Function([var_1687,var_1688,var_1689,var_1690,var_1691,], output)
mutated_mod['func_1692'] = func_1692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_1721 = func_1075_call()
call_1722 = func_1075_call()
output = call_1721
output2 = call_1722
func_1733 = relay.Function([], output)
mod['func_1733'] = func_1733
mod = relay.transform.InferType()(mod)
output = func_1733()
func_1734 = relay.Function([], output)
mutated_mod['func_1734'] = func_1734
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1778 = relay.var("var_1778", dtype = "float64", shape = (2, 6, 8))#candidate|1778|(2, 6, 8)|var|float64
uop_1779 = relay.erf(var_1778.astype('float64')) # shape=(2, 6, 8)
uop_1781 = relay.log10(uop_1779.astype('float32')) # shape=(2, 6, 8)
func_1503_call = mod.get_global_var('func_1503')
func_1505_call = mutated_mod.get_global_var('func_1505')
call_1785 = func_1503_call()
call_1786 = func_1503_call()
func_1223_call = mod.get_global_var('func_1223')
func_1228_call = mutated_mod.get_global_var('func_1228')
const_1791 = relay.const([7,7,-6,1,-2,-2,-1,1,1,8,8,-8,2,6,-3,4,-9,-7,-9,-4,5,3,2,-1,1,10,-1,4,6,-3,-3,2,10,-8,8,-10,-8,10,7,3,-9,1,1,3,-5,8,-5,-9,-10,4,9,-10,6,-8,-1,5,4,-10,-9,-4,-1,-2,5,-3,-10,-2,10,-7,3,-1,8,2,2,-9,-5,5,7,4,3,-6,2,-2,-1,-1], dtype = "uint64")#candidate|1791|(84,)|const|uint64
var_1792 = relay.var("var_1792", dtype = "float32", shape = (1650,))#candidate|1792|(1650,)|var|float32
const_1793 = relay.const([-0.030196,-9.635666,-6.190191,2.953628,2.542285,-5.909045,-3.503198,1.750520,-0.444739,1.851213,0.816109,-5.416978,7.707165,4.405231,6.336936,4.191747,0.851459,-4.617099,-7.852472,-5.387898,2.807111,2.583191,3.179480,8.627857,8.073178,6.691868,-7.889268,-7.702029,-4.713044,-0.712140,1.216407,4.452170,-7.893433,0.796122,3.770646,-5.454785,-2.746415,-6.362748,-2.728283,7.692602,-5.812214,-9.212038,2.356109,-3.728189,-9.229325,6.236025,-5.202965,-5.640377,-2.164644,-3.321034,-2.710561,-6.835524,-9.985316,-8.770945,9.613323,-1.565324,9.495622,-2.032997,-4.888290,-0.075097,-0.007897,-3.627839,-6.177617,6.577964,-0.839180,-4.024578,-5.221747,-3.283431,5.685191,6.214475,-0.569566,1.671989,-6.248679,-9.476335,-2.139422,-1.796053,-0.687109,-4.086225,8.960823,-5.437941,5.416415,-2.268560,6.485682,-1.549045,-6.382295,1.332350,-3.066497,-2.516284,2.417606,5.974278,0.392688,-6.178754,-6.945662,-8.156877,-0.852508,-7.541003,8.086949,5.942828,1.406676,0.907153,2.770314,-3.469476,4.541221,-5.201136,-5.016241,8.574158,2.668214,1.950074,-5.116096,-7.102274,-6.693837,-9.085652,6.678080,6.533323,1.580472,-4.339580,6.881972,-9.490052,3.387792,7.502556,-7.506065,2.469274,-2.158209,-2.284372,-8.601258,8.176484,3.629308,-2.008710,2.140493,5.028538,8.161726,5.955101,-4.771860,6.024937,4.571493,6.615681,3.673638,0.786171,-3.409826,-6.588338,-2.690843,2.531663,9.104626,8.762713,3.369980,-8.477367,-6.482033,-5.302718,8.237781,2.324365,-8.284689,5.579888,3.581110,-6.875691,-8.472088,1.688609,-8.360665,-8.106198,-0.831826,4.406672,-1.102625,-6.029586,2.429196,7.623253,0.467977,9.868288,-9.865620,9.644335,-8.158575,1.793384,9.956328,0.144260,1.994435,7.233286,1.085065,-6.651701,-1.617917,5.150732,7.945619,7.535994,4.964588,-5.419481,5.650199,1.023297,9.002152,-2.325865,5.266099,4.881547,1.309740,7.371614,9.724372,-1.544442,-7.021476,2.611022,-6.940711,-1.371168,-1.300295,6.761108,7.312294,1.520120,6.918503,9.037715,2.241839,-6.488285,6.172347,-3.795866,9.861347,5.493003,-2.963828,0.049669,6.909953,-2.547095,-3.666171,6.994983,-7.588959,2.665180,-3.746185,7.460258,7.261264,-4.079079,3.089147,6.503027,8.029663,-9.753454,2.844191,-3.223993,-8.714095,-7.876646,6.458152,-8.642360,-5.389707,6.642210,-6.366513,8.154605,-3.079094,-5.651751,-1.234843,-9.482065,-1.496789,0.675380,-7.027081,-6.048474,-9.916026,-8.091214,-0.524262,5.931508,-2.248923,7.805934,7.084837,-6.046994,-9.325858,2.891870,-8.021452,-0.337019,3.741337,-2.278067,-4.858252,-6.974082,-0.461302,-9.391988,6.275272,9.608394,-5.864643,-7.959485,9.885366,-3.691487,5.676807,-5.652588,0.077671,8.898480,-6.674054,1.478126,-5.707741,3.730090,-4.806329,-6.658074,-5.683103,9.366414,-4.811534,-7.938955,-5.474013,-2.073358,2.444425,6.509477,7.719296,1.448945,-0.056534,-1.483263,-3.821758,5.918634,3.187291,-7.322647,-9.655415,4.323593,2.626944,-0.791716,-4.696718,0.711605,-1.222919,-3.450005,5.542402,3.607317,-8.287265,3.752907,-6.822636,6.314612,-2.369808,8.110336,3.084161,2.399507,-5.837263,-6.657659,-8.181079,-0.904973,-1.090417,4.804486,-4.689831,-1.831699,-9.718642,9.329501,-9.039856,0.722180,-9.478990,7.855134,0.170295,-4.893692,8.187520,-8.399359,9.733928,-7.897291,3.225620,3.308602,-1.761817,6.167209,4.998751,9.541931,0.779167,-5.651839,0.552492,-6.470849,5.035880,7.388783,9.721691,-2.942611,-7.879146,2.449671,-8.721096,-2.336227,-4.381309,-9.753811,-6.754366,9.448263,-4.430472,-3.727998,-3.928168,-1.006739,1.748572,-5.479239,3.896309,6.149892,2.249168,3.980984,-0.079703,-6.845350,3.653412,-7.270053,2.615586,-7.431766,-6.877924,2.921026,4.317831,-5.302695,7.095023,6.566482,7.648783,9.902082,2.234581,1.594205,-0.201182,-6.778455,-8.292967,2.299845,8.601577,3.110632], dtype = "float32")#candidate|1793|(384,)|const|float32
var_1794 = relay.var("var_1794", dtype = "float32", shape = (429,))#candidate|1794|(429,)|var|float32
call_1790 = relay.TupleGetItem(func_1223_call(relay.reshape(const_1791.astype('uint64'), [84,]), relay.reshape(var_1792.astype('float32'), [1, 1650]), relay.reshape(const_1793.astype('float32'), [384,]), relay.reshape(var_1794.astype('float32'), [39, 11]), ), 5)
call_1795 = relay.TupleGetItem(func_1228_call(relay.reshape(const_1791.astype('uint64'), [84,]), relay.reshape(var_1792.astype('float32'), [1, 1650]), relay.reshape(const_1793.astype('float32'), [384,]), relay.reshape(var_1794.astype('float32'), [39, 11]), ), 5)
func_620_call = mod.get_global_var('func_620')
func_623_call = mutated_mod.get_global_var('func_623')
call_1802 = relay.TupleGetItem(func_620_call(relay.reshape(const_1793.astype('float32'), [4, 8, 12]), relay.reshape(const_1793.astype('float32'), [4, 8, 12]), ), 0)
call_1803 = relay.TupleGetItem(func_623_call(relay.reshape(const_1793.astype('float32'), [4, 8, 12]), relay.reshape(const_1793.astype('float32'), [4, 8, 12]), ), 0)
output = relay.Tuple([uop_1781,call_1785,call_1790,const_1791,var_1792,const_1793,var_1794,call_1802,])
output2 = relay.Tuple([uop_1781,call_1786,call_1795,const_1791,var_1792,const_1793,var_1794,call_1803,])
func_1806 = relay.Function([var_1778,var_1792,var_1794,], output)
mod['func_1806'] = func_1806
mod = relay.transform.InferType()(mod)
mutated_mod['func_1806'] = func_1806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1806_call = mutated_mod.get_global_var('func_1806')
var_1808 = relay.var("var_1808", dtype = "float64", shape = (2, 6, 8))#candidate|1808|(2, 6, 8)|var|float64
var_1809 = relay.var("var_1809", dtype = "float32", shape = (1650,))#candidate|1809|(1650,)|var|float32
var_1810 = relay.var("var_1810", dtype = "float32", shape = (429,))#candidate|1810|(429,)|var|float32
call_1807 = func_1806_call(var_1808,var_1809,var_1810,)
output = call_1807
func_1811 = relay.Function([var_1808,var_1809,var_1810,], output)
mutated_mod['func_1811'] = func_1811
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1882 = relay.var("var_1882", dtype = "float64", shape = (3, 3, 2))#candidate|1882|(3, 3, 2)|var|float64
const_1883 = relay.const([[[-0.560942,5.414887],[-0.401374,-6.020730],[-9.564119,8.646238]],[[-6.489838,6.427858],[7.255828,4.158870],[-7.393325,-6.189736]],[[-7.013337,-3.927342],[-1.401282,-3.212372],[-4.640074,4.062036]]], dtype = "float64")#candidate|1883|(3, 3, 2)|const|float64
bop_1884 = relay.floor_divide(var_1882.astype('float64'), relay.reshape(const_1883.astype('float64'), relay.shape_of(var_1882))) # shape=(3, 3, 2)
func_278_call = mod.get_global_var('func_278')
func_281_call = mutated_mod.get_global_var('func_281')
const_1893 = relay.const([[5.245442,8.132544,4.503322,3.869472,-4.265097,-1.949892,-4.019548,4.982037,2.756630,-7.544318,-5.817080,-9.856692,6.998724,-7.613793,-2.950233,8.003052,-6.116665,-4.069980,0.689288,8.954491],[0.985932,-0.246393,-8.550089,5.768645,-7.497480,8.155035,8.832103,7.947992,6.759769,6.958702,-0.834757,3.059645,4.393280,9.608330,9.616386,-4.675187,-2.866184,3.464790,9.339804,8.158811],[-6.032275,-8.863343,-7.566313,-8.143999,8.487478,4.267247,4.660045,-4.300381,3.527020,4.067307,-4.072868,3.659155,5.723375,-5.821987,-4.038863,-5.707433,-9.171421,-7.398901,-9.603351,-2.850939]], dtype = "float32")#candidate|1893|(3, 20)|const|float32
call_1892 = func_278_call(relay.reshape(const_1893.astype('float32'), [1, 12, 5]))
call_1894 = func_278_call(relay.reshape(const_1893.astype('float32'), [1, 12, 5]))
func_383_call = mod.get_global_var('func_383')
func_386_call = mutated_mod.get_global_var('func_386')
var_1899 = relay.var("var_1899", dtype = "int64", shape = (96,))#candidate|1899|(96,)|var|int64
call_1898 = func_383_call(relay.reshape(var_1899.astype('int64'), [4, 3, 8]))
call_1900 = func_383_call(relay.reshape(var_1899.astype('int64'), [4, 3, 8]))
output = relay.Tuple([bop_1884,call_1892,const_1893,call_1898,var_1899,])
output2 = relay.Tuple([bop_1884,call_1894,const_1893,call_1900,var_1899,])
func_1908 = relay.Function([var_1882,var_1899,], output)
mod['func_1908'] = func_1908
mod = relay.transform.InferType()(mod)
mutated_mod['func_1908'] = func_1908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1908_call = mutated_mod.get_global_var('func_1908')
var_1910 = relay.var("var_1910", dtype = "float64", shape = (3, 3, 2))#candidate|1910|(3, 3, 2)|var|float64
var_1911 = relay.var("var_1911", dtype = "int64", shape = (96,))#candidate|1911|(96,)|var|int64
call_1909 = func_1908_call(var_1910,var_1911,)
output = call_1909
func_1912 = relay.Function([var_1910,var_1911,], output)
mutated_mod['func_1912'] = func_1912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_1978 = relay.TupleGetItem(func_989_call(), 3)
call_1979 = relay.TupleGetItem(func_991_call(), 3)
func_620_call = mod.get_global_var('func_620')
func_623_call = mutated_mod.get_global_var('func_623')
var_1990 = relay.var("var_1990", dtype = "float32", shape = (384,))#candidate|1990|(384,)|var|float32
call_1989 = relay.TupleGetItem(func_620_call(relay.reshape(var_1990.astype('float32'), [4, 8, 12]), relay.reshape(var_1990.astype('float32'), [4, 8, 12]), ), 0)
call_1991 = relay.TupleGetItem(func_623_call(relay.reshape(var_1990.astype('float32'), [4, 8, 12]), relay.reshape(var_1990.astype('float32'), [4, 8, 12]), ), 0)
output = relay.Tuple([call_1978,call_1989,var_1990,])
output2 = relay.Tuple([call_1979,call_1991,var_1990,])
func_1997 = relay.Function([var_1990,], output)
mod['func_1997'] = func_1997
mod = relay.transform.InferType()(mod)
mutated_mod['func_1997'] = func_1997
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1998 = relay.var("var_1998", dtype = "float32", shape = (384,))#candidate|1998|(384,)|var|float32
func_1997_call = mutated_mod.get_global_var('func_1997')
call_1999 = func_1997_call(var_1998)
output = call_1999
func_2000 = relay.Function([var_1998], output)
mutated_mod['func_2000'] = func_2000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1503_call = mod.get_global_var('func_1503')
func_1505_call = mutated_mod.get_global_var('func_1505')
call_2004 = func_1503_call()
call_2005 = func_1503_call()
output = call_2004
output2 = call_2005
func_2041 = relay.Function([], output)
mod['func_2041'] = func_2041
mod = relay.transform.InferType()(mod)
mutated_mod['func_2041'] = func_2041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2041_call = mutated_mod.get_global_var('func_2041')
call_2042 = func_2041_call()
output = call_2042
func_2043 = relay.Function([], output)
mutated_mod['func_2043'] = func_2043
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2087 = relay.var("var_2087", dtype = "float32", shape = (16, 1, 7))#candidate|2087|(16, 1, 7)|var|float32
uop_2088 = relay.atanh(var_2087.astype('float32')) # shape=(16, 1, 7)
bop_2090 = relay.bitwise_and(var_2087.astype('int32'), relay.reshape(uop_2088.astype('int32'), relay.shape_of(var_2087))) # shape=(16, 1, 7)
func_1075_call = mod.get_global_var('func_1075')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_2100 = func_1075_call()
call_2101 = func_1075_call()
func_529_call = mod.get_global_var('func_529')
func_531_call = mutated_mod.get_global_var('func_531')
const_2104 = relay.const([-5.894694,-5.491870,8.867286,-8.770829,0.408573,-4.282220,-2.534376,-0.742029,1.159820,7.418073,7.867752,-6.054665,-1.677423,-8.868511,-2.346645,-2.641527,-1.054878,-5.603769,5.939983,-1.959654,-8.598921,3.002037,1.064253,3.903298,-2.668428,-6.660267,-8.008489,8.676206,2.010306,-5.495561,-6.529700,-7.270279,6.285035,7.593482,2.257337,6.541339,-8.416014,-1.456018,-2.622545,-3.643558,0.443195,-9.970929,7.584699,-6.330203,6.656834,3.016234,4.194726,-0.598736,-6.489976,9.738036,-3.265166,5.072822,-3.589840,-2.133308,5.484037,7.655431,9.210196,-2.380223,-4.485605,4.342754,4.906422,4.453826,8.765800,2.306430,7.090004,2.726857,-6.159351,2.750088,2.884287,7.368568,-0.667895,0.498987,4.957020,3.440316,-4.797652,8.997613,4.675246,5.479213,6.979445,-6.280413,6.662298,-0.065498,8.090319,-7.029422,9.784507,5.347363,5.066587,0.593742,3.902185,-4.413197,9.774699,1.245729,-7.884827,2.188655,-4.389045,7.693242,-9.156307,1.038061,4.493505,-5.629888,5.967157,-9.272610,-1.863229,9.543191,-2.000759,2.222483,-8.377619,-0.575261,2.471859,-2.577846,-4.959542,-2.923786,2.156973,-6.010907,2.554964,3.532142,-8.669604,5.556500,6.397287,-9.278220,-9.404077,5.860179,9.391384,-7.968426,-6.192754,-9.610598,-9.937135,8.308117,-1.918142,-4.572483,-7.400554,-8.090452,6.997356,2.925993,0.387150,2.820519,6.078863,-1.956408,-9.214772,-0.615216,0.441339,6.279146,6.949039,8.340145,-3.788530,0.945723,8.359951,-8.272933,-3.579374,8.822597,7.917680,0.236732,4.878850,8.061464,-4.152256,-1.451595,-2.970440,1.402076,-4.329945,5.263557,-4.356081,5.781109,7.440882,0.403914,9.298143,4.461526,2.796731,-4.482140,-2.883958,-6.332225,1.164653,-1.345211,8.208073,3.606297,-1.589550,-5.697406,9.153951,-8.241905,8.386832,-1.343782,-9.290998,-8.996972,1.325331,-2.016440,-8.103579,-2.904750,-9.082496,-5.346817,6.258364,2.409435,-1.197240,-8.173101,-2.371053,-3.727535,-1.344621,-1.999370,-9.161756,-4.790062,1.805189,7.030033,-3.330373,9.406205,-6.917390,-0.541484,5.953470,3.873729,4.467100,-0.809123,-8.614677,-2.274839,4.215773,1.288697,3.307196,8.570774,4.638789,-7.164773,5.403075,-2.863925,5.165180,7.490826,-2.635308,5.343110,-2.193122,9.114075,-0.774759,-5.025741,4.931694,-7.917888,7.416351,0.736239,-2.214358,-3.249270,-0.233879,-3.264134,8.594280,-1.552597,-6.055928,-6.901304,6.826540,-7.390360,5.620727,-0.101947,-8.375941,0.400815,-1.733151,-3.889535,-9.764700,-4.429582,0.750741,8.727543,-2.285562,0.561316,0.746419,-4.952398,1.319484,-8.930460,4.722192,7.010094,3.236668,6.986749,-2.127308,3.312158,1.487761,2.970815,-3.566267,0.065569,-3.303452,2.057268,-0.747741,0.078158,-0.858725,-2.983171,-1.268142,-1.707530,-9.849776,3.742725,3.871694,-3.947121,6.950934,-8.452559,-2.153771,-1.563942,-6.319610,-5.832105,2.863674,-0.711810,3.250933,4.825553,1.101958,-5.850123,-1.451229,-5.058713,-5.753969,-5.417135,-4.682336,0.917331,-2.445265,6.707961,6.011311,-1.457797,1.904466,7.689465,6.060789,-2.173292,-7.254541,3.538282,9.071196,-5.718224,-2.549275,1.016563,2.598212,2.242561,-0.455600,-2.146782,-8.686315,9.505362,-2.205255,-3.675929,5.956296,-1.780905,2.571758,-0.012621,9.830805,-4.219421,6.300616,-1.024829,-8.450207,1.808370,-1.113259,0.603386,-3.200137,9.828707,6.519520,-2.345487,-2.874343,-0.675558,-3.338373,-7.259384,0.286049,4.842955,-0.561067,-6.943924,4.432037,-2.136014,8.050474,-9.748652,-5.217879,-3.595985,-2.146398,-6.268184,8.460142,-3.836769,-1.414207,4.989642,-0.437311,-8.026108,-2.233290,7.275167,-1.286916,-7.593316,9.082512,0.432261,-3.629306,0.328669,1.725390,2.207144,-4.600642,-7.680925,9.686334,4.096962,6.618525,-3.354410,-0.988427,7.264391,1.601454,-5.252733,2.040496,-4.382207,-8.138259,-8.417301,-4.703859,-2.874170,1.871855,8.993357,6.884754,-1.698194,-6.928802,-9.187876,4.481450,-1.166281,2.091136,5.588386,-8.824294,-5.010282,-5.271910,-4.233550,4.789077,0.330838,-1.493040,1.075531,6.438403,-9.661479,-6.650042,-9.298160,-7.984749,4.575058,-9.108754,-7.244737,-0.460813,8.927412,5.001588,2.998122,-1.875254,-7.773979,4.479569,-8.075807,0.113199,0.218183,-5.242909,4.625452,-1.359574,-8.188672,-6.079571,2.090258,-5.389391,9.521553,7.147916,-0.444894,9.570191,-7.349929,-8.333974,-1.737539,1.780290,0.596168,2.448308,-2.350602,3.301684,-2.428879,-5.492102,0.516997,-4.509205,-1.266448,7.170247,-5.329073,1.524232,-0.125001,1.787791,-5.876645,-2.828593,-4.475300,-6.646465,5.631146,-3.212009,9.991038,2.573991,6.761529,5.204209,8.487770,-0.805096,-3.768361,-9.197913,7.123913,2.687953,-8.674781,1.008024,5.699943,-8.765124,-3.733778,0.099963,2.387010,-4.478074,-4.829660,-0.266508,-1.910900,1.912077,7.050969,4.557019,-9.111696,-1.594005,-6.573040,6.503053,3.830970,-1.680525,-3.135490,-5.735499,7.299374,-7.562243,-5.536242,3.483330,9.416244,3.256256,4.594216,3.765296,8.688362,-5.831589,-5.907457,-4.628804,7.039293,2.068364,-7.640388,2.468665,-4.663676,1.053538,4.138724,2.290626,-5.705844,9.737400,-6.100572,7.861715,-3.159080,3.071785,8.959783,-3.721879,9.197544,4.559478,4.354007,3.087315,-1.509675,0.019476,0.480474,9.375317,2.858092,7.823150,7.081024,-4.058885,1.779959,-0.489839,9.826314,4.441453,-2.840068,-6.742135,-9.376183,8.390037,-4.891094,-7.324161,-7.017198,7.034693,-6.425674,3.110223,7.286739,5.114758,0.399683,-3.979848,-0.517124,5.052100,-0.694149,7.670942,7.143612,3.904556,4.401766,-4.436585,5.881726,2.081610,-9.389037,-3.696919,-0.278268,-4.120980,4.318366,-2.134325,5.833066,1.208714,5.936475,-4.167953,8.341680,7.162739,1.580548,-0.753281,0.570548,-6.986377,-2.792289,-3.225761,-7.351966,7.193393,4.762383,4.950343,2.664825,-6.228815,9.147622,-7.635909,-5.854037,8.567705,0.155513,7.061943,-2.947364,-0.810809,-7.387772,4.249133,-9.604633,-5.290472,5.939883,-7.023529,-1.196728,4.128647,7.792726,9.161655,1.085762,4.402442,-1.707056,-9.057119,-6.313805,-7.861165,2.843013,1.186810,-2.084999,7.970758,4.294006,-1.253378,-1.615450,-0.851768,8.748917,6.912910,-7.459692,4.864134,9.444199,5.772059,1.882620,-6.770374,-4.911864,-1.180037,-9.759566,-1.657109,1.797806,6.422831,-8.640621,5.304779,4.531483,0.568860,4.855662,8.769319,-4.492996,-9.868716,-8.187605,-0.258532,-1.418578,7.852986,-3.658869,-9.411451,-9.844968,9.471766,3.202949,9.156813,5.071261,4.946292,3.854135,-6.318653,1.589904,0.091303,4.913328,-2.875446,-5.102647,-1.799831,1.710315,-6.180596,5.667791,9.786928,-9.257953,0.105684,1.709542,-7.605633,7.185907,-1.443732,7.184273,-0.002166,6.672787,-4.374446,-4.681533,-6.231162,-2.293329,-5.029199,-5.316505,-4.859165,-8.520216,-9.826591,-4.555157,-0.323014,0.667901,8.634334,8.403563,-0.916784,-3.653692,-4.167207,1.174899,8.064682,-0.348613,2.640572,6.022851,5.218919,-8.652932,4.119880,8.297663,-5.562597,-6.327909,7.817965,-0.374520,-7.848167,7.442140,4.622198,4.928704,-6.867746,-6.121376,-1.126273,6.098740,0.628530,2.804231], dtype = "float32")#candidate|2104|(704,)|const|float32
call_2103 = relay.TupleGetItem(func_529_call(relay.reshape(const_2104.astype('float32'), [4, 11, 16])), 0)
call_2105 = relay.TupleGetItem(func_531_call(relay.reshape(const_2104.astype('float32'), [4, 11, 16])), 0)
bop_2127 = relay.subtract(uop_2088.astype('float32'), relay.reshape(var_2087.astype('float32'), relay.shape_of(uop_2088))) # shape=(16, 1, 7)
func_1265_call = mod.get_global_var('func_1265')
func_1266_call = mutated_mod.get_global_var('func_1266')
call_2137 = relay.TupleGetItem(func_1265_call(), 0)
call_2138 = relay.TupleGetItem(func_1266_call(), 0)
uop_2140 = relay.rsqrt(bop_2090.astype('float64')) # shape=(16, 1, 7)
uop_2142 = relay.exp(var_2087.astype('float64')) # shape=(16, 1, 7)
bop_2144 = relay.equal(uop_2140.astype('bool'), relay.reshape(uop_2142.astype('bool'), relay.shape_of(uop_2140))) # shape=(16, 1, 7)
var_2154 = relay.var("var_2154", dtype = "int32", shape = (16, 13, 7))#candidate|2154|(16, 13, 7)|var|int32
bop_2155 = relay.add(bop_2090.astype('int8'), var_2154.astype('int8')) # shape=(16, 13, 7)
uop_2166 = relay.sinh(bop_2127.astype('float64')) # shape=(16, 1, 7)
output = relay.Tuple([call_2100,call_2103,const_2104,call_2137,bop_2144,bop_2155,uop_2166,])
output2 = relay.Tuple([call_2101,call_2105,const_2104,call_2138,bop_2144,bop_2155,uop_2166,])
func_2169 = relay.Function([var_2087,var_2154,], output)
mod['func_2169'] = func_2169
mod = relay.transform.InferType()(mod)
var_2170 = relay.var("var_2170", dtype = "float32", shape = (16, 1, 7))#candidate|2170|(16, 1, 7)|var|float32
var_2171 = relay.var("var_2171", dtype = "int32", shape = (16, 13, 7))#candidate|2171|(16, 13, 7)|var|int32
output = func_2169(var_2170,var_2171,)
func_2172 = relay.Function([var_2170,var_2171,], output)
mutated_mod['func_2172'] = func_2172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mod.get_global_var('func_1021')
func_1023_call = mutated_mod.get_global_var('func_1023')
call_2203 = func_1021_call()
call_2204 = func_1021_call()
func_571_call = mod.get_global_var('func_571')
func_576_call = mutated_mod.get_global_var('func_576')
var_2220 = relay.var("var_2220", dtype = "uint64", shape = (160,))#candidate|2220|(160,)|var|uint64
const_2221 = relay.const([-5.192559,0.703491,-5.468269,-4.952029,1.109217,-4.055623,9.449087,-4.021759,-0.472440,7.718746,3.993811,-1.495147,-1.146210,-5.403510,-7.322230,-8.063825,-7.175842,9.068249,-9.414525,7.177358,8.046743,4.784004,2.276198,1.906279,-6.032845,-1.831421,-6.206826,-9.239650,0.365180,5.772705,-3.599462,-8.246442,3.734373,-5.848467,7.676444,9.072176,6.885932,5.027852,9.721185,2.187665,1.489715,4.343223,-1.940415,5.519965,-8.106347,2.260795,-7.912411,8.510282,-0.437235,-9.532808,8.577802,-4.606021,-8.817836,3.800305,-5.546980,5.880836,6.349229,-1.339553,7.295050,9.568464], dtype = "float32")#candidate|2221|(60,)|const|float32
call_2219 = relay.TupleGetItem(func_571_call(relay.reshape(var_2220.astype('uint64'), [8, 4, 5]), relay.reshape(var_2220.astype('uint64'), [8, 4, 5]), relay.reshape(const_2221.astype('float32'), [60,]), ), 1)
call_2222 = relay.TupleGetItem(func_576_call(relay.reshape(var_2220.astype('uint64'), [8, 4, 5]), relay.reshape(var_2220.astype('uint64'), [8, 4, 5]), relay.reshape(const_2221.astype('float32'), [60,]), ), 1)
output = relay.Tuple([call_2203,call_2219,var_2220,const_2221,])
output2 = relay.Tuple([call_2204,call_2222,var_2220,const_2221,])
func_2246 = relay.Function([var_2220,], output)
mod['func_2246'] = func_2246
mod = relay.transform.InferType()(mod)
var_2247 = relay.var("var_2247", dtype = "uint64", shape = (160,))#candidate|2247|(160,)|var|uint64
output = func_2246(var_2247)
func_2248 = relay.Function([var_2247], output)
mutated_mod['func_2248'] = func_2248
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2300 = relay.var("var_2300", dtype = "float64", shape = (5, 13, 16))#candidate|2300|(5, 13, 16)|var|float64
uop_2301 = relay.sqrt(var_2300.astype('float64')) # shape=(5, 13, 16)
uop_2303 = relay.sigmoid(var_2300.astype('float32')) # shape=(5, 13, 16)
bop_2309 = relay.bitwise_xor(uop_2303.astype('uint16'), relay.reshape(uop_2301.astype('uint16'), relay.shape_of(uop_2303))) # shape=(5, 13, 16)
var_2326 = relay.var("var_2326", dtype = "float32", shape = (5, 13, 16))#candidate|2326|(5, 13, 16)|var|float32
bop_2327 = relay.floor_divide(uop_2303.astype('float64'), relay.reshape(var_2326.astype('float64'), relay.shape_of(uop_2303))) # shape=(5, 13, 16)
output = relay.Tuple([bop_2309,bop_2327,])
output2 = relay.Tuple([bop_2309,bop_2327,])
func_2342 = relay.Function([var_2300,var_2326,], output)
mod['func_2342'] = func_2342
mod = relay.transform.InferType()(mod)
var_2343 = relay.var("var_2343", dtype = "float64", shape = (5, 13, 16))#candidate|2343|(5, 13, 16)|var|float64
var_2344 = relay.var("var_2344", dtype = "float32", shape = (5, 13, 16))#candidate|2344|(5, 13, 16)|var|float32
output = func_2342(var_2343,var_2344,)
func_2345 = relay.Function([var_2343,var_2344,], output)
mutated_mod['func_2345'] = func_2345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1523_call = mod.get_global_var('func_1523')
func_1525_call = mutated_mod.get_global_var('func_1525')
call_2398 = func_1523_call()
call_2399 = func_1523_call()
func_2246_call = mod.get_global_var('func_2246')
func_2248_call = mutated_mod.get_global_var('func_2248')
const_2412 = relay.const([5,-3,-3,-9,-1,4,6,-2,-7,-8,-6,7,-1,9,9,6,-5,1,5,5,-9,-10,4,-7,-2,10,-1,9,7,-2,1,10,-6,4,-5,7,-1,-6,-10,6,8,-7,2,1,-5,6,10,2,1,7,-8,-9,-3,1,-7,-3,-2,-6,-8,6,1,-9,-1,6,8,7,10,-2,10,4,2,-4,10,1,-6,-3,-2,-5,5,5,7,-9,6,9,9,-5,3,-5,7,2,6,8,10,-9,7,8,5,-2,-1,9,6,-10,3,-3,5,4,3,-9,7,7,3,-9,-3,1,4,5,-4,-9,2,9,-1,1,5,8,8,-10,-1,9,-2,9,10,5,10,-3,8,-2,-5,3,-2,5,-6,-3,4,10,-4,-3,4,-10,-2,9,-5,8,-5,-1,4,7,9,-7,-3,10], dtype = "uint64")#candidate|2412|(160,)|const|uint64
call_2411 = relay.TupleGetItem(func_2246_call(relay.reshape(const_2412.astype('uint64'), [160,])), 1)
call_2413 = relay.TupleGetItem(func_2248_call(relay.reshape(const_2412.astype('uint64'), [160,])), 1)
output = relay.Tuple([call_2398,call_2411,const_2412,])
output2 = relay.Tuple([call_2399,call_2413,const_2412,])
func_2416 = relay.Function([], output)
mod['func_2416'] = func_2416
mod = relay.transform.InferType()(mod)
mutated_mod['func_2416'] = func_2416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2416_call = mutated_mod.get_global_var('func_2416')
call_2417 = func_2416_call()
output = call_2417
func_2418 = relay.Function([], output)
mutated_mod['func_2418'] = func_2418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1553_call = mod.get_global_var('func_1553')
func_1554_call = mutated_mod.get_global_var('func_1554')
call_2436 = relay.TupleGetItem(func_1553_call(), 0)
call_2437 = relay.TupleGetItem(func_1554_call(), 0)
output = relay.Tuple([call_2436,])
output2 = relay.Tuple([call_2437,])
func_2439 = relay.Function([], output)
mod['func_2439'] = func_2439
mod = relay.transform.InferType()(mod)
output = func_2439()
func_2440 = relay.Function([], output)
mutated_mod['func_2440'] = func_2440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_2451 = func_1075_call()
call_2452 = func_1075_call()
output = relay.Tuple([call_2451,])
output2 = relay.Tuple([call_2452,])
func_2458 = relay.Function([], output)
mod['func_2458'] = func_2458
mod = relay.transform.InferType()(mod)
output = func_2458()
func_2459 = relay.Function([], output)
mutated_mod['func_2459'] = func_2459
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2551 = relay.const([[[-2.091233,1.366139,-7.648090,-9.692892,0.529968,8.628349,-9.841208,-6.586788,-6.173250,-6.379005,-4.899954,-3.153492],[3.295478,-8.506790,3.761131,4.282761,-1.145561,-9.122941,3.492806,1.381893,-2.919434,3.653220,2.619491,-6.371022],[1.032503,3.807782,4.763508,0.130281,-7.637768,-8.127124,7.928330,9.745401,1.305307,-9.240296,1.464976,5.476272],[-1.824829,-8.321237,-5.781739,-7.500612,1.224781,-3.443924,9.960458,-7.326589,2.953755,3.887058,-7.382020,9.492060],[-2.066068,-8.312619,7.999506,-3.955754,-2.698858,6.024947,5.813067,3.866221,-5.519707,9.871760,9.934820,5.800713],[2.901201,-9.646783,9.001216,0.559266,8.962767,1.968069,1.081654,0.247497,-9.456994,1.551041,-8.251350,9.571609],[-7.861798,-9.312778,-9.379315,-9.528001,3.509604,8.689917,-3.165912,-9.810637,-8.219145,9.905530,0.551852,-1.161082],[0.040539,1.247541,-1.887356,-7.323419,-5.016884,-7.240549,-8.213112,-9.815842,8.736734,1.081638,-8.687367,-3.736678],[1.025430,-5.129658,-0.362613,2.307152,-0.419034,0.002625,3.115532,6.687156,-2.964810,-3.101350,3.947533,-8.935797],[-8.357229,-9.349280,-7.462825,9.716958,-0.438541,-4.468724,-8.507052,4.854040,3.516589,5.386058,-3.991472,-7.707133],[9.548746,-7.387691,3.841222,2.320612,-7.273850,-4.007802,-4.514624,-8.663621,7.239501,6.389009,-8.868621,1.523549]]], dtype = "float64")#candidate|2551|(1, 11, 12)|const|float64
uop_2552 = relay.exp(const_2551.astype('float64')) # shape=(1, 11, 12)
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
var_2558 = relay.var("var_2558", dtype = "float32", shape = (429,))#candidate|2558|(429,)|var|float32
var_2559 = relay.var("var_2559", dtype = "float32", shape = (676,))#candidate|2559|(676,)|var|float32
call_2557 = relay.TupleGetItem(func_408_call(relay.reshape(var_2558.astype('float32'), [13, 3, 11]), relay.reshape(var_2559.astype('float32'), [676,]), ), 0)
call_2560 = relay.TupleGetItem(func_411_call(relay.reshape(var_2558.astype('float32'), [13, 3, 11]), relay.reshape(var_2559.astype('float32'), [676,]), ), 0)
bop_2561 = relay.bitwise_and(uop_2552.astype('int64'), relay.reshape(const_2551.astype('int64'), relay.shape_of(uop_2552))) # shape=(1, 11, 12)
bop_2572 = relay.add(var_2558.astype('int64'), relay.reshape(call_2557.astype('int64'), relay.shape_of(var_2558))) # shape=(429,)
bop_2575 = relay.add(var_2558.astype('int64'), relay.reshape(call_2560.astype('int64'), relay.shape_of(var_2558))) # shape=(429,)
bop_2579 = relay.greater(uop_2552.astype('bool'), relay.reshape(bop_2561.astype('bool'), relay.shape_of(uop_2552))) # shape=(1, 11, 12)
func_967_call = mod.get_global_var('func_967')
func_973_call = mutated_mod.get_global_var('func_973')
var_2588 = relay.var("var_2588", dtype = "uint64", shape = (84,))#candidate|2588|(84,)|var|uint64
var_2589 = relay.var("var_2589", dtype = "float32", shape = (1650,))#candidate|2589|(1650,)|var|float32
call_2587 = relay.TupleGetItem(func_967_call(relay.reshape(var_2588.astype('uint64'), [2, 3, 14]), relay.reshape(var_2588.astype('uint64'), [2, 3, 14]), relay.reshape(var_2588.astype('uint64'), [2, 3, 14]), relay.reshape(var_2589.astype('float32'), [1650,]), relay.reshape(var_2589.astype('float32'), [1650,]), ), 2)
call_2590 = relay.TupleGetItem(func_973_call(relay.reshape(var_2588.astype('uint64'), [2, 3, 14]), relay.reshape(var_2588.astype('uint64'), [2, 3, 14]), relay.reshape(var_2588.astype('uint64'), [2, 3, 14]), relay.reshape(var_2589.astype('float32'), [1650,]), relay.reshape(var_2589.astype('float32'), [1650,]), ), 2)
bop_2591 = relay.divide(bop_2561.astype('float64'), relay.reshape(const_2551.astype('float64'), relay.shape_of(bop_2561))) # shape=(1, 11, 12)
output = relay.Tuple([var_2559,bop_2572,bop_2579,call_2587,var_2588,var_2589,bop_2591,])
output2 = relay.Tuple([var_2559,bop_2575,bop_2579,call_2590,var_2588,var_2589,bop_2591,])
func_2601 = relay.Function([var_2558,var_2559,var_2588,var_2589,], output)
mod['func_2601'] = func_2601
mod = relay.transform.InferType()(mod)
mutated_mod['func_2601'] = func_2601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2601_call = mutated_mod.get_global_var('func_2601')
var_2603 = relay.var("var_2603", dtype = "float32", shape = (429,))#candidate|2603|(429,)|var|float32
var_2604 = relay.var("var_2604", dtype = "float32", shape = (676,))#candidate|2604|(676,)|var|float32
var_2605 = relay.var("var_2605", dtype = "uint64", shape = (84,))#candidate|2605|(84,)|var|uint64
var_2606 = relay.var("var_2606", dtype = "float32", shape = (1650,))#candidate|2606|(1650,)|var|float32
call_2602 = func_2601_call(var_2603,var_2604,var_2605,var_2606,)
output = call_2602
func_2607 = relay.Function([var_2603,var_2604,var_2605,var_2606,], output)
mutated_mod['func_2607'] = func_2607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mod.get_global_var('func_1021')
func_1023_call = mutated_mod.get_global_var('func_1023')
call_2665 = func_1021_call()
call_2666 = func_1021_call()
var_2668 = relay.var("var_2668", dtype = "float64", shape = (8, 7, 16))#candidate|2668|(8, 7, 16)|var|float64
bop_2669 = relay.divide(call_2665.astype('float64'), var_2668.astype('float64')) # shape=(8, 7, 16)
bop_2672 = relay.divide(call_2666.astype('float64'), var_2668.astype('float64')) # shape=(8, 7, 16)
output = relay.Tuple([bop_2669,])
output2 = relay.Tuple([bop_2672,])
func_2674 = relay.Function([var_2668,], output)
mod['func_2674'] = func_2674
mod = relay.transform.InferType()(mod)
mutated_mod['func_2674'] = func_2674
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2675 = relay.var("var_2675", dtype = "float64", shape = (8, 7, 16))#candidate|2675|(8, 7, 16)|var|float64
func_2674_call = mutated_mod.get_global_var('func_2674')
call_2676 = func_2674_call(var_2675)
output = call_2676
func_2677 = relay.Function([var_2675], output)
mutated_mod['func_2677'] = func_2677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2458_call = mod.get_global_var('func_2458')
func_2459_call = mutated_mod.get_global_var('func_2459')
call_2757 = relay.TupleGetItem(func_2458_call(), 0)
call_2758 = relay.TupleGetItem(func_2459_call(), 0)
output = relay.Tuple([call_2757,])
output2 = relay.Tuple([call_2758,])
func_2767 = relay.Function([], output)
mod['func_2767'] = func_2767
mod = relay.transform.InferType()(mod)
mutated_mod['func_2767'] = func_2767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2767_call = mutated_mod.get_global_var('func_2767')
call_2768 = func_2767_call()
output = call_2768
func_2769 = relay.Function([], output)
mutated_mod['func_2769'] = func_2769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1503_call = mod.get_global_var('func_1503')
func_1505_call = mutated_mod.get_global_var('func_1505')
call_2811 = func_1503_call()
call_2812 = func_1503_call()
output = call_2811
output2 = call_2812
func_2813 = relay.Function([], output)
mod['func_2813'] = func_2813
mod = relay.transform.InferType()(mod)
mutated_mod['func_2813'] = func_2813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mutated_mod.get_global_var('func_2813')
call_2814 = func_2813_call()
output = call_2814
func_2815 = relay.Function([], output)
mutated_mod['func_2815'] = func_2815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1523_call = mod.get_global_var('func_1523')
func_1525_call = mutated_mod.get_global_var('func_1525')
call_2826 = func_1523_call()
call_2827 = func_1523_call()
uop_2828 = relay.atanh(call_2826.astype('float64')) # shape=(16, 12, 5)
uop_2830 = relay.atanh(call_2827.astype('float64')) # shape=(16, 12, 5)
bop_2838 = relay.less(uop_2828.astype('bool'), relay.reshape(call_2826.astype('bool'), relay.shape_of(uop_2828))) # shape=(16, 12, 5)
bop_2841 = relay.less(uop_2830.astype('bool'), relay.reshape(call_2827.astype('bool'), relay.shape_of(uop_2830))) # shape=(16, 12, 5)
bop_2843 = relay.left_shift(bop_2838.astype('uint32'), relay.reshape(uop_2828.astype('uint32'), relay.shape_of(bop_2838))) # shape=(16, 12, 5)
bop_2846 = relay.left_shift(bop_2841.astype('uint32'), relay.reshape(uop_2830.astype('uint32'), relay.shape_of(bop_2841))) # shape=(16, 12, 5)
func_1733_call = mod.get_global_var('func_1733')
func_1734_call = mutated_mod.get_global_var('func_1734')
call_2855 = func_1733_call()
call_2856 = func_1733_call()
output = relay.Tuple([bop_2843,call_2855,])
output2 = relay.Tuple([bop_2846,call_2856,])
func_2867 = relay.Function([], output)
mod['func_2867'] = func_2867
mod = relay.transform.InferType()(mod)
output = func_2867()
func_2868 = relay.Function([], output)
mutated_mod['func_2868'] = func_2868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2416_call = mod.get_global_var('func_2416')
func_2418_call = mutated_mod.get_global_var('func_2418')
call_2891 = relay.TupleGetItem(func_2416_call(), 0)
call_2892 = relay.TupleGetItem(func_2418_call(), 0)
output = call_2891
output2 = call_2892
func_2896 = relay.Function([], output)
mod['func_2896'] = func_2896
mod = relay.transform.InferType()(mod)
output = func_2896()
func_2897 = relay.Function([], output)
mutated_mod['func_2897'] = func_2897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1503_call = mod.get_global_var('func_1503')
func_1505_call = mutated_mod.get_global_var('func_1505')
call_2914 = func_1503_call()
call_2915 = func_1503_call()
const_2939 = relay.const([-4,-5,-1,1,-1,1,3,5,10,9,5,-2,10,7,-7,1,3,6,-10,9,-8,-9,10,1,8,-8,2,1,4,-5,-2,-6,6,-8,7,-10,-10,3,4,10,4,6,7,-7,7,4,2,-4,-2,-5,-10,5,5,-1,-2,1,-6,1,4,6,3,1,-2,2,-5,-6,-3,8,6,4,-8,-5,2,10,5,-7,8,4,3,5,-4,-5,-9,-4,2,-7,5,-7,-8,-4,4,3,-1,3,2,2,-8,-2,9,4,-8,-2,-2,1,-9,-5,8,7,3,-1,-8,1,-9,-3,-3,-10,9,-5,2,-3,10,-5,5,8,-2,5,4,-5,10,-1,-6,-3,4,6,-3,8,8,-2,7,-3,10,8,5,-7,1,10,-1,-2,3,3,-10,9,-6,1,2,-2,-5,8,-2,-4], dtype = "uint64")#candidate|2939|(160,)|const|uint64
bop_2940 = relay.logical_xor(call_2914.astype('int8'), relay.reshape(const_2939.astype('int8'), relay.shape_of(call_2914))) # shape=(160,)
bop_2943 = relay.logical_xor(call_2915.astype('int8'), relay.reshape(const_2939.astype('int8'), relay.shape_of(call_2915))) # shape=(160,)
func_1356_call = mod.get_global_var('func_1356')
func_1359_call = mutated_mod.get_global_var('func_1359')
var_2960 = relay.var("var_2960", dtype = "float32", shape = (352,))#candidate|2960|(352,)|var|float32
call_2959 = func_1356_call(relay.reshape(var_2960.astype('float32'), [4, 8, 11]))
call_2961 = func_1356_call(relay.reshape(var_2960.astype('float32'), [4, 8, 11]))
uop_2966 = relay.sigmoid(var_2960.astype('float64')) # shape=(352,)
output = relay.Tuple([bop_2940,call_2959,uop_2966,])
output2 = relay.Tuple([bop_2943,call_2961,uop_2966,])
func_2975 = relay.Function([var_2960,], output)
mod['func_2975'] = func_2975
mod = relay.transform.InferType()(mod)
var_2976 = relay.var("var_2976", dtype = "float32", shape = (352,))#candidate|2976|(352,)|var|float32
output = func_2975(var_2976)
func_2977 = relay.Function([var_2976], output)
mutated_mod['func_2977'] = func_2977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1503_call = mod.get_global_var('func_1503')
func_1505_call = mutated_mod.get_global_var('func_1505')
call_3001 = func_1503_call()
call_3002 = func_1503_call()
func_2169_call = mod.get_global_var('func_2169')
func_2172_call = mutated_mod.get_global_var('func_2172')
const_3016 = relay.const([-7.197982,-4.749639,-3.868651,-8.177194,-0.505009,-2.748849,3.835130,7.373400,2.034633,2.127587,-2.605557,4.069276,1.598760,-8.338027,-5.684835,-0.537424,5.690038,-5.617565,-9.438303,0.515470,7.747863,3.926848,-2.104593,8.528379,-7.581446,5.938644,4.217000,1.607077,-4.801095,7.270156,3.256796,6.574723,-9.291135,-0.259751,-9.780612,8.325899,-7.574192,9.033120,2.244358,-5.519180,0.775499,-5.502145,-7.785694,0.386755,-9.853405,7.234591,4.737598,-8.564582,-5.785660,-1.960880,-8.913352,-3.760857,-9.442101,6.900403,1.351894,1.065626,4.351878,0.594796,9.463318,-5.313938,8.606178,8.202829,-8.644496,-9.111871,2.534550,-8.858358,9.170510,-1.575181,-4.978572,0.541786,5.901283,-8.868578,1.335021,-2.560061,2.380213,-6.455879,9.505625,4.045086,8.691920,-9.075765,-0.701778,-7.801601,-4.850541,4.080385,-0.712827,-5.573481,6.704262,0.285042,-8.856677,4.035149,-6.427982,-3.103226,1.709242,-4.986595,2.444801,8.070447,5.476939,5.313440,-5.200503,-8.020402,-5.933338,-1.017360,7.171465,-3.389185,-3.285935,3.442679,3.723223,-6.159820,4.546163,4.690525,5.787898,-6.877501], dtype = "float32")#candidate|3016|(112,)|const|float32
var_3017 = relay.var("var_3017", dtype = "int32", shape = (1456,))#candidate|3017|(1456,)|var|int32
call_3015 = relay.TupleGetItem(func_2169_call(relay.reshape(const_3016.astype('float32'), [16, 1, 7]), relay.reshape(var_3017.astype('int32'), [16, 13, 7]), ), 2)
call_3018 = relay.TupleGetItem(func_2172_call(relay.reshape(const_3016.astype('float32'), [16, 1, 7]), relay.reshape(var_3017.astype('int32'), [16, 13, 7]), ), 2)
func_2439_call = mod.get_global_var('func_2439')
func_2440_call = mutated_mod.get_global_var('func_2440')
call_3048 = relay.TupleGetItem(func_2439_call(), 0)
call_3049 = relay.TupleGetItem(func_2440_call(), 0)
output = relay.Tuple([call_3001,call_3015,const_3016,var_3017,call_3048,])
output2 = relay.Tuple([call_3002,call_3018,const_3016,var_3017,call_3049,])
func_3050 = relay.Function([var_3017,], output)
mod['func_3050'] = func_3050
mod = relay.transform.InferType()(mod)
var_3051 = relay.var("var_3051", dtype = "int32", shape = (1456,))#candidate|3051|(1456,)|var|int32
output = func_3050(var_3051)
func_3052 = relay.Function([var_3051], output)
mutated_mod['func_3052'] = func_3052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2416_call = mod.get_global_var('func_2416')
func_2418_call = mutated_mod.get_global_var('func_2418')
call_3065 = relay.TupleGetItem(func_2416_call(), 2)
call_3066 = relay.TupleGetItem(func_2418_call(), 2)
func_814_call = mod.get_global_var('func_814')
func_816_call = mutated_mod.get_global_var('func_816')
var_3068 = relay.var("var_3068", dtype = "float32", shape = (180,))#candidate|3068|(180,)|var|float32
call_3067 = func_814_call(relay.reshape(var_3068.astype('float32'), [10, 3, 6]))
call_3069 = func_814_call(relay.reshape(var_3068.astype('float32'), [10, 3, 6]))
output = relay.Tuple([call_3065,call_3067,var_3068,])
output2 = relay.Tuple([call_3066,call_3069,var_3068,])
func_3070 = relay.Function([var_3068,], output)
mod['func_3070'] = func_3070
mod = relay.transform.InferType()(mod)
var_3071 = relay.var("var_3071", dtype = "float32", shape = (180,))#candidate|3071|(180,)|var|float32
output = func_3070(var_3071)
func_3072 = relay.Function([var_3071], output)
mutated_mod['func_3072'] = func_3072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1523_call = mod.get_global_var('func_1523')
func_1525_call = mutated_mod.get_global_var('func_1525')
call_3079 = func_1523_call()
call_3080 = func_1523_call()
func_1733_call = mod.get_global_var('func_1733')
func_1734_call = mutated_mod.get_global_var('func_1734')
call_3083 = func_1733_call()
call_3084 = func_1733_call()
func_2813_call = mod.get_global_var('func_2813')
func_2815_call = mutated_mod.get_global_var('func_2815')
call_3085 = func_2813_call()
call_3086 = func_2813_call()
func_2041_call = mod.get_global_var('func_2041')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_3096 = func_2041_call()
call_3097 = func_2041_call()
func_1806_call = mod.get_global_var('func_1806')
func_1811_call = mutated_mod.get_global_var('func_1811')
var_3106 = relay.var("var_3106", dtype = "float64", shape = (96,))#candidate|3106|(96,)|var|float64
var_3107 = relay.var("var_3107", dtype = "float32", shape = (1650, 1))#candidate|3107|(1650, 1)|var|float32
var_3108 = relay.var("var_3108", dtype = "float32", shape = (429,))#candidate|3108|(429,)|var|float32
call_3105 = relay.TupleGetItem(func_1806_call(relay.reshape(var_3106.astype('float64'), [2, 6, 8]), relay.reshape(var_3107.astype('float32'), [1650,]), relay.reshape(var_3108.astype('float32'), [429,]), ), 6)
call_3109 = relay.TupleGetItem(func_1811_call(relay.reshape(var_3106.astype('float64'), [2, 6, 8]), relay.reshape(var_3107.astype('float32'), [1650,]), relay.reshape(var_3108.astype('float32'), [429,]), ), 6)
output = relay.Tuple([call_3079,call_3083,call_3085,call_3096,call_3105,var_3106,var_3107,var_3108,])
output2 = relay.Tuple([call_3080,call_3084,call_3086,call_3097,call_3109,var_3106,var_3107,var_3108,])
func_3115 = relay.Function([var_3106,var_3107,var_3108,], output)
mod['func_3115'] = func_3115
mod = relay.transform.InferType()(mod)
var_3116 = relay.var("var_3116", dtype = "float64", shape = (96,))#candidate|3116|(96,)|var|float64
var_3117 = relay.var("var_3117", dtype = "float32", shape = (1650, 1))#candidate|3117|(1650, 1)|var|float32
var_3118 = relay.var("var_3118", dtype = "float32", shape = (429,))#candidate|3118|(429,)|var|float32
output = func_3115(var_3116,var_3117,var_3118,)
func_3119 = relay.Function([var_3116,var_3117,var_3118,], output)
mutated_mod['func_3119'] = func_3119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1523_call = mod.get_global_var('func_1523')
func_1525_call = mutated_mod.get_global_var('func_1525')
call_3155 = func_1523_call()
call_3156 = func_1523_call()
output = relay.Tuple([call_3155,])
output2 = relay.Tuple([call_3156,])
func_3179 = relay.Function([], output)
mod['func_3179'] = func_3179
mod = relay.transform.InferType()(mod)
mutated_mod['func_3179'] = func_3179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3179_call = mutated_mod.get_global_var('func_3179')
call_3180 = func_3179_call()
output = call_3180
func_3181 = relay.Function([], output)
mutated_mod['func_3181'] = func_3181
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3216 = relay.var("var_3216", dtype = "bool", shape = (14, 1, 13))#candidate|3216|(14, 1, 13)|var|bool
const_3217 = relay.const([[[True,False,False,True,False,False,False,False,True,False,False,False,True],[True,False,True,True,False,True,False,True,True,True,False,False,False],[False,False,False,False,False,False,False,False,True,False,False,False,False],[False,False,True,False,True,False,False,True,True,True,False,False,False],[True,True,False,True,False,False,False,False,False,False,False,True,True],[False,True,True,False,False,True,False,True,False,False,True,False,True],[False,True,True,False,False,True,False,False,False,False,True,False,False],[True,True,True,False,False,True,False,True,True,False,True,True,True],[True,True,False,True,False,False,True,False,True,True,True,True,True]],[[True,True,False,False,True,False,True,False,False,True,True,False,False],[False,False,True,False,True,False,True,True,False,False,False,True,False],[True,False,True,False,True,False,True,False,False,False,False,True,True],[False,False,False,True,True,True,True,False,True,True,True,False,False],[True,False,False,False,False,True,False,True,True,True,False,False,True],[False,True,True,False,False,False,False,False,True,True,True,False,False],[False,True,True,True,False,False,True,False,False,False,False,False,True],[True,True,True,False,True,False,True,False,False,True,False,False,True],[True,False,True,False,False,True,True,True,False,True,True,False,False]],[[True,False,False,True,True,True,False,True,True,True,True,False,False],[True,True,False,True,True,False,True,False,False,True,True,True,False],[False,True,True,False,True,False,False,True,True,True,False,False,False],[False,True,True,False,True,False,False,False,False,True,False,True,True],[False,True,False,True,True,False,False,True,False,True,True,False,False],[True,False,True,True,False,True,False,False,True,False,False,True,False],[False,False,False,False,True,False,True,False,True,False,False,False,True],[True,True,True,True,False,False,True,True,True,False,False,True,False],[True,True,False,True,True,True,True,True,True,True,True,False,True]],[[True,False,True,True,False,False,False,True,False,False,True,True,True],[False,True,True,True,True,True,True,False,False,False,True,True,False],[False,False,True,False,True,False,False,True,True,False,True,False,True],[True,False,False,True,False,False,False,True,False,False,False,True,False],[False,True,True,False,True,True,False,True,True,False,True,True,True],[True,False,False,True,True,False,True,False,True,True,False,True,True],[False,True,True,True,True,False,True,False,False,False,True,False,True],[False,False,True,False,True,False,False,False,True,True,False,False,True],[True,False,False,False,True,False,False,False,False,True,False,True,False]],[[False,True,True,True,True,False,True,False,False,True,False,False,True],[True,True,True,True,True,False,True,True,False,False,True,False,True],[True,False,True,False,False,False,False,True,True,True,True,False,True],[True,True,True,True,False,False,True,True,True,False,True,True,True],[False,True,False,False,False,False,False,False,False,False,False,False,False],[True,True,True,True,False,True,True,True,False,True,True,True,True],[True,True,False,False,False,False,True,True,True,False,True,True,False],[True,False,False,False,False,True,True,True,False,False,False,True,True],[True,True,True,False,False,False,False,False,False,False,True,True,True]],[[False,True,False,True,True,False,True,True,False,True,False,True,True],[True,True,True,False,True,False,True,False,True,True,False,True,False],[False,True,True,True,True,True,True,True,False,False,True,False,False],[True,True,False,True,False,True,False,False,False,True,False,True,True],[True,True,True,False,True,True,False,False,True,True,True,False,False],[True,False,False,True,False,True,True,True,False,True,False,True,True],[False,False,False,False,False,True,True,True,False,False,True,False,False],[False,True,True,False,True,False,False,True,False,True,True,True,False],[True,False,False,False,False,True,True,False,True,True,True,False,False]],[[True,False,True,True,False,True,False,True,True,False,True,False,True],[True,True,False,False,True,False,True,True,False,True,False,True,True],[True,False,False,True,True,False,True,False,True,True,False,False,False],[True,False,False,True,True,True,False,False,False,True,False,True,True],[False,False,True,False,True,True,False,True,False,True,True,False,False],[True,True,False,True,False,True,True,False,True,False,True,True,False],[True,True,False,False,False,True,False,True,True,True,False,True,True],[True,True,False,True,True,True,False,True,False,False,False,True,False],[True,False,False,True,False,True,False,True,False,False,False,False,True]],[[True,False,False,False,True,True,True,True,False,False,True,False,True],[True,True,False,True,True,True,True,True,False,True,True,False,False],[True,False,False,True,False,True,True,False,False,False,True,True,False],[True,False,True,True,True,False,False,True,True,False,True,False,True],[True,False,False,False,False,True,False,True,True,False,False,False,False],[False,True,True,False,True,False,False,False,False,True,False,False,True],[False,False,False,False,False,True,False,False,True,True,False,False,False],[True,False,False,True,True,True,False,False,True,True,True,True,True],[True,False,False,True,True,False,False,True,False,False,True,True,False]],[[False,False,False,False,False,True,True,False,True,False,True,True,False],[False,True,True,True,False,False,False,False,False,True,False,False,True],[True,False,False,False,False,False,False,True,True,False,False,False,False],[True,False,False,True,False,False,False,False,False,False,False,False,True],[False,True,True,False,False,False,False,False,False,True,True,False,False],[False,False,False,False,True,False,False,True,True,False,True,True,False],[True,True,True,True,False,True,True,False,False,True,False,False,False],[True,True,True,True,True,True,False,False,True,True,False,True,False],[True,True,True,False,False,True,True,True,False,False,False,True,False]],[[False,True,False,True,True,True,False,False,True,False,True,True,False],[False,False,False,True,False,True,False,True,True,False,False,False,True],[True,False,False,False,False,False,True,True,True,False,False,False,False],[True,False,True,False,False,True,False,False,False,False,True,True,False],[False,True,False,False,True,True,True,True,False,True,True,True,False],[True,False,True,True,False,False,True,False,True,True,True,True,True],[False,False,False,True,False,False,False,False,False,True,False,True,False],[False,True,False,True,True,True,True,False,False,False,True,True,False],[False,False,True,True,True,True,True,True,False,True,True,True,False]],[[True,False,False,True,True,False,False,True,True,True,False,True,False],[False,True,True,True,True,True,True,False,False,False,False,False,True],[False,True,False,True,True,True,False,True,False,True,True,False,False],[True,False,False,False,False,False,True,True,True,False,False,False,False],[False,False,False,False,True,True,False,True,False,True,False,False,True],[True,True,False,True,True,True,True,True,True,True,True,False,False],[False,False,False,False,True,True,False,True,True,True,False,True,False],[True,True,True,True,False,False,True,False,True,False,False,True,False],[True,False,True,False,True,False,False,True,False,True,False,True,True]],[[False,False,True,True,True,False,False,False,False,False,False,True,True],[True,True,True,False,True,False,True,True,False,False,True,True,True],[True,False,False,False,True,False,True,True,True,False,True,False,False],[True,False,False,False,True,True,False,False,False,True,True,True,False],[True,True,True,False,False,True,True,False,True,False,False,False,True],[False,False,True,False,False,False,False,False,True,False,False,True,False],[False,False,True,True,True,True,False,False,True,False,True,False,True],[True,True,True,True,False,True,False,True,True,False,False,False,True],[True,False,True,False,False,True,False,False,False,True,True,False,False]],[[False,False,True,True,True,False,False,True,False,False,False,False,False],[False,False,False,False,True,True,False,False,True,False,True,True,False],[True,True,True,True,True,False,False,False,True,True,True,True,False],[True,True,True,True,True,True,True,True,True,True,False,True,True],[True,True,True,True,False,False,False,True,False,True,True,False,True],[False,True,False,True,False,True,True,True,False,False,False,False,False],[True,True,False,False,False,False,True,True,True,True,False,True,True],[False,False,False,False,True,True,True,False,False,True,True,True,False],[False,False,False,False,False,True,True,False,True,True,False,True,True]],[[True,False,True,False,True,True,False,False,True,False,True,False,False],[True,False,True,True,False,True,True,True,True,True,False,False,True],[False,False,False,True,True,True,True,False,False,True,True,False,True],[False,False,False,False,False,True,False,False,False,True,True,True,False],[True,False,False,True,False,False,True,False,True,False,True,True,False],[True,False,True,False,True,True,False,True,False,True,False,False,True],[True,True,False,False,True,True,True,False,True,True,False,False,True],[False,True,False,True,True,False,True,True,False,False,False,False,True],[False,True,True,True,False,False,False,True,True,False,False,False,False]]], dtype = "bool")#candidate|3217|(14, 9, 13)|const|bool
bop_3218 = relay.logical_and(var_3216.astype('bool'), const_3217.astype('bool')) # shape=(14, 9, 13)
bop_3230 = relay.greater(bop_3218.astype('bool'), relay.reshape(const_3217.astype('bool'), relay.shape_of(bop_3218))) # shape=(14, 9, 13)
output = relay.Tuple([bop_3230,])
output2 = relay.Tuple([bop_3230,])
func_3244 = relay.Function([var_3216,], output)
mod['func_3244'] = func_3244
mod = relay.transform.InferType()(mod)
var_3245 = relay.var("var_3245", dtype = "bool", shape = (14, 1, 13))#candidate|3245|(14, 1, 13)|var|bool
output = func_3244(var_3245)
func_3246 = relay.Function([var_3245], output)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2416_call = mod.get_global_var('func_2416')
func_2418_call = mutated_mod.get_global_var('func_2418')
call_3275 = relay.TupleGetItem(func_2416_call(), 1)
call_3276 = relay.TupleGetItem(func_2418_call(), 1)
output = call_3275
output2 = call_3276
func_3277 = relay.Function([], output)
mod['func_3277'] = func_3277
mod = relay.transform.InferType()(mod)
output = func_3277()
func_3278 = relay.Function([], output)
mutated_mod['func_3278'] = func_3278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_3287 = func_1075_call()
call_3288 = func_1075_call()
output = call_3287
output2 = call_3288
func_3294 = relay.Function([], output)
mod['func_3294'] = func_3294
mod = relay.transform.InferType()(mod)
output = func_3294()
func_3295 = relay.Function([], output)
mutated_mod['func_3295'] = func_3295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3296 = relay.var("var_3296", dtype = "float32", shape = (12, 3, 6))#candidate|3296|(12, 3, 6)|var|float32
uop_3297 = relay.acos(var_3296.astype('float32')) # shape=(12, 3, 6)
output = relay.Tuple([uop_3297,])
output2 = relay.Tuple([uop_3297,])
func_3300 = relay.Function([var_3296,], output)
mod['func_3300'] = func_3300
mod = relay.transform.InferType()(mod)
mutated_mod['func_3300'] = func_3300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3301 = relay.var("var_3301", dtype = "float32", shape = (12, 3, 6))#candidate|3301|(12, 3, 6)|var|float32
func_3300_call = mutated_mod.get_global_var('func_3300')
call_3302 = func_3300_call(var_3301)
output = call_3302
func_3303 = relay.Function([var_3301], output)
mutated_mod['func_3303'] = func_3303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_3305 = relay.TupleGetItem(func_989_call(), 0)
call_3306 = relay.TupleGetItem(func_991_call(), 0)
output = relay.Tuple([call_3305,])
output2 = relay.Tuple([call_3306,])
func_3318 = relay.Function([], output)
mod['func_3318'] = func_3318
mod = relay.transform.InferType()(mod)
mutated_mod['func_3318'] = func_3318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3318_call = mutated_mod.get_global_var('func_3318')
call_3319 = func_3318_call()
output = call_3319
func_3320 = relay.Function([], output)
mutated_mod['func_3320'] = func_3320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2896_call = mod.get_global_var('func_2896')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_3330 = func_2896_call()
call_3331 = func_2896_call()
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
const_3333 = relay.const([-5.909998,-3.789576,-3.719623,2.049923,5.915295,-5.207790,4.600492,0.604867,2.263103,-5.763997,5.240513,7.092023,7.505405,-7.159123,-2.486476,6.866658,-3.553341,-3.848106,3.633500,9.557998,4.294550,-5.251629,-5.477453,-9.277480,2.166293,6.101422,8.762098,4.434719,-1.184229,2.684304,-9.736025,1.303419,0.881864,7.620484,-8.699802,0.426267,-3.005306,-2.838245,-1.879676,-7.263672,3.049842,-7.691851,4.802504,7.419684,1.437752,-6.152243,-5.895960,7.406097,-9.546446,-8.763851,2.669313,-0.823350,4.644220,-9.445105,5.479859,-1.270005,7.657316,-3.495442,-3.184927,-9.395064,-4.884612,8.892949,1.058998,-6.302405,1.239742,-5.915109,2.636972,-1.639783,4.470226,-0.359926,-7.732728,0.093665,1.857647,-2.594388,5.845070,-5.219848,4.962551,-2.987704,-3.600481,-5.714474,6.072436,-9.289282,3.840147,-5.461606,1.801488,-4.497611,3.863645,7.232128,9.483022,-4.093850,6.948897,-4.422259,2.114874,4.050568,-6.410692,3.278010,-9.426932,-6.995801,0.892414,-3.805033,3.957960,-4.399232,-4.388006,9.008863,1.508487,-5.825678,-7.543144,1.050220,-5.268128,4.285045,5.403737,-8.047580,-6.161488,5.782566,2.808024,8.771774,-2.216279,9.042430,7.023270,-3.721164,3.856697,9.128128,-1.555747,8.785148,8.389546,7.513366,3.907380,-3.146173,-9.974564,2.810963,2.531504,-5.209794,-0.716628,-1.720239,-7.972825,-4.246228,-5.361073,-3.408849,8.248060,0.882284,-9.798196,2.870970,-0.508389,-1.686678,1.298597,4.836141,-7.083830,0.831807,6.014371,-2.338515,-6.583863,9.761291,4.808851,6.995616,0.939489,6.098770,7.483511,-0.032103,3.066955,-0.500359,-0.670023,0.687834,6.283713,-0.482889,6.592142,7.984806,2.851618,-9.000273,-8.679013,4.328861,-8.278563,3.650907,2.913833,4.184273,-7.016137,-6.285982,0.477659,1.875868,-6.956869,-3.368475,7.776612,2.602027,-9.614742,4.189400,-4.648625,8.194559,9.282899,-5.209432,-3.976651,9.819192,-6.169893,2.891261,-4.371116,-6.757078,-5.306874,-3.528590,-3.783242,6.779708,5.583195,7.967493,2.916730,-1.754753,-6.199966,-8.572216,-1.625785,1.087760,9.264679,3.211601,-5.202262,-6.802090,-7.935947,-4.781193,-2.886194,8.259478,-0.727049,9.614883,0.377108,-2.888347,0.859305,-6.665646,0.898004,-3.165360,7.447932,-1.186745,5.065185,-0.194120,5.692020,9.213590,-8.302040,3.280924,6.854131,9.204020,-6.436305,-9.299754,-7.242113,8.197137,0.317535,-8.720431,0.064572,-3.194473,1.077713,-9.138522,4.217316,-2.549876,9.165368,-3.192327,0.920588,1.782484,0.472890,1.944845,2.548399,3.067272,-7.958735,0.008772,-0.004635,-3.442095,-8.501254,-4.333748,-4.938916,-5.849744,-6.391533,7.323465,-0.642310,6.543442,-4.693161,5.213411,-8.624102,-9.577919,-6.399026,-7.402633,4.331805,-4.711562,-9.500602,7.597746,9.589935,-0.193574,-6.281479,0.041529,-2.160821,0.590405,2.540289,-9.340522,8.571975,-7.896278,-2.546986,8.386604,-7.385574,-6.729368,-0.211897,5.178884,9.826176,-5.111868,4.721588,-0.979067,-4.022569,3.465121,-2.588662,2.998452,-2.351733,7.943504,5.060448,2.741016,-5.861063,-3.331983,9.610037,-3.134393,4.367693,5.103751,2.293239,-3.610231,9.970732,4.313329,-8.169381,5.140111,5.073396,1.182195,1.410646,-9.142020,-8.493931,6.714401,-0.028543,-7.062071,-6.945100,9.020749,6.122487,1.850711,6.023690,-0.672098,-1.274608,-0.730915,-3.704107,-7.260813,-7.275246,8.179542,6.781286,6.195350,3.000672,2.497429,7.856960,6.883533,-1.134499,7.096169,9.385385,1.068932,0.695471,7.661625,-2.572356,-7.933856,-0.707271,8.422530,-1.586856,-2.343544,6.410128,4.335132,-2.054985,3.113696,0.576428,-1.121930,0.790180,-6.221927,5.297206,-2.213751,6.384645,1.552512,5.496236,5.705980,3.655700,0.469803,7.511369,6.945138,6.351467,9.345802,0.711350,9.744235,5.573332,1.317275,-0.333508,-4.514829,-6.171431,9.685390,6.891445,8.479187,-6.909325,3.059016,3.366419,1.423938,5.248351,-4.313198,-0.375983,6.927149,1.691469,0.232833,4.904001,-4.414906,2.079589,9.355358,-3.247468,4.719833,1.643093,6.624427,6.705920,6.654375,9.310143,3.938079,0.314350,9.890145,3.869198,-2.509661,4.528462,6.601347,4.746682,0.324510,2.043738,-1.734762,2.443380,-4.692032,7.389596,5.241455,8.487791,-7.843276,-8.712650,5.702750,-7.580981,-4.319226,-3.395832,-7.490628,-8.867534,-5.335932,-0.339143], dtype = "float32")#candidate|3333|(429,)|const|float32
var_3334 = relay.var("var_3334", dtype = "float32", shape = (676,))#candidate|3334|(676,)|var|float32
call_3332 = relay.TupleGetItem(func_408_call(relay.reshape(const_3333.astype('float32'), [13, 3, 11]), relay.reshape(var_3334.astype('float32'), [676,]), ), 1)
call_3335 = relay.TupleGetItem(func_411_call(relay.reshape(const_3333.astype('float32'), [13, 3, 11]), relay.reshape(var_3334.astype('float32'), [676,]), ), 1)
uop_3340 = relay.acosh(call_3332.astype('float32')) # shape=(13, 13, 4)
uop_3342 = relay.acosh(call_3335.astype('float32')) # shape=(13, 13, 4)
func_2439_call = mod.get_global_var('func_2439')
func_2440_call = mutated_mod.get_global_var('func_2440')
call_3346 = relay.TupleGetItem(func_2439_call(), 0)
call_3347 = relay.TupleGetItem(func_2440_call(), 0)
uop_3353 = relay.tan(call_3346.astype('float32')) # shape=(60,)
uop_3355 = relay.tan(call_3347.astype('float32')) # shape=(60,)
output = relay.Tuple([call_3330,const_3333,var_3334,uop_3340,uop_3353,])
output2 = relay.Tuple([call_3331,const_3333,var_3334,uop_3342,uop_3355,])
func_3362 = relay.Function([var_3334,], output)
mod['func_3362'] = func_3362
mod = relay.transform.InferType()(mod)
var_3363 = relay.var("var_3363", dtype = "float32", shape = (676,))#candidate|3363|(676,)|var|float32
output = func_3362(var_3363)
func_3364 = relay.Function([var_3363], output)
mutated_mod['func_3364'] = func_3364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2867_call = mod.get_global_var('func_2867')
func_2868_call = mutated_mod.get_global_var('func_2868')
call_3387 = relay.TupleGetItem(func_2867_call(), 0)
call_3388 = relay.TupleGetItem(func_2868_call(), 0)
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
const_3399 = relay.const([4.797070,9.520938,4.402515,-6.250888,-4.145987,8.985723,-7.744037,4.986263,-9.874429,1.857194,-8.663557,4.388399,7.378087,-6.099228,5.131867,-9.973912,0.617177,-7.661718,2.095991,-9.901810,9.845330,2.189288,-2.613965,-4.099896,9.069213,0.848326,-1.119866,-5.358813,-3.020807,-0.884071,-2.007580,-1.448118,-8.489760,-3.655442,2.198984,-5.580235,3.409048,4.645356,-7.952260,-7.100370,4.470164,-3.253350,-7.327497,7.037045,0.728462,-4.049712,6.888626,7.959137,-0.152875,8.485462,5.497812,-0.847062,9.402249,-1.430539,3.511412,-7.910408,-1.627258,-5.462538,8.328741,-9.692385,1.096461,-6.547279,4.383998,0.279054,-9.786560,-6.795261,-4.136580,-2.809086,-5.607038,2.713428,7.519311,-4.042308,-9.151430,0.141596,-2.529932,8.425867,-5.105807,-8.534288,9.705339,1.618157,8.143532,9.706117,-3.753392,2.051388,0.218805,-2.511669,-9.118936,-0.509665,6.492632,9.685585,4.932374,-3.756059,-1.930194,-1.633806,-2.405315,7.338361,0.080818,4.328171,-9.765466,-1.586843,3.190912,6.540877,7.630046,6.236473,2.147567,-0.493823,7.216752,-9.503786,-0.822443,8.197240,9.107637,-2.051625,-0.344949,-4.609997,-3.987839,-0.266658,-8.703112,-3.497754,7.423511,-4.222297,-3.446771,-7.032170,5.719186,8.997513,7.465415,-7.710712,-1.602428,2.660778,-1.486055,6.663526,-8.573873,9.236154,3.678408,-8.150231,4.842336,1.150147,8.081458,8.773787,5.597869,-7.667469,6.518560,8.032875,9.917578,-7.914036,-4.062514,3.027339,7.209445,1.152552,-1.550289,-8.894041,3.545042,2.469803,8.745128,0.181520,8.054023,9.745591,4.655190,-6.419696,9.316086,-0.592171,6.594372,-7.604043,-8.522014,7.166318,2.363255,-2.566516,-0.959811,4.099647,-5.893776,-3.919108,8.971847,6.869307,-2.428558,4.666842,-1.474161,8.212547,8.530409,1.862328,-7.852146,-5.903883,-7.741140,-9.655735,-6.408945,-8.340062,-5.736003,7.278570,-3.867968,-1.287173,-2.861106,-7.572980,-1.573693,-9.881830,1.460772,5.484244,5.297536,9.122661,7.804126,-1.051383,5.000000,-7.430180,5.108487,3.675878,-6.543810,-2.117990,-8.169264,-1.639554,-6.947103,-7.029052,-1.002208,5.604861,-6.606753,6.090491,-4.272428,9.807690,-2.168068,-8.267674,4.333324,7.095239,7.827116,8.830706,-7.981574,-9.450020,-4.545858,-3.685532,2.958227,-7.638342,-5.996084,4.200764,1.155015,-0.249615,-9.105572,2.744556,9.977920,-8.796678,-4.920228,-8.458902,9.112227,-7.024731,1.870604,-1.119209,-2.290423,-6.891522,-7.087103,-8.079941,3.593228,1.819695,7.367039,2.986661,9.995995,9.505737,4.983868,-8.190512,9.755772,9.323174,3.694724,2.242919,-3.912654,-3.815597,7.282446,3.803590,0.746145,-3.938034,7.095770,3.960784,7.095715,8.602397,-3.424256,4.622093,-6.698695,8.658097,-8.326728,9.264748,-3.888715,6.882883,-4.100625,-2.818776,5.063797,-7.317464,9.753813,8.228730,6.774464,9.840019,-0.646841,9.367552,2.547891,-6.941269,8.517135,1.284749,3.641873,1.526580,9.078332,-2.901702,-1.188445,7.763940,-3.472205,1.396107,9.782934,-3.520105,4.442988,-5.647187,-9.702396,5.482520,2.989912,9.399870,6.369622,-2.229267,2.189913,-8.960661,-1.218715,5.102366,-7.141339,-0.107443,4.409020,-6.990806,-2.137737,-3.124093,1.445613,-7.529444,-2.843607,-6.335671,-0.251774,-0.128810,5.122533,4.022808,-4.038065,-0.333804,2.920723,8.002083,9.267070,-1.203195,-7.075089,-9.667259,-2.091138,-8.112731,1.034785,-4.043786,-5.264503,0.825272,1.515373,3.401327,8.133229,4.751159,-7.174568,4.168419,-8.143184,7.047418,-3.498221,-2.825674,-5.542281,7.314242,2.977573,4.054856,-1.053416,1.292203,1.200210,-5.301756,9.705095,-1.884392,-4.015544,0.951655,3.507257,5.854125,4.372201,-1.973862,2.272466,6.495215,9.252975,-8.583589,1.014617,-7.417709,-6.201127,4.782719,-8.067075,3.139160,7.588225,1.246145,2.849392,5.033604,-3.362138,-4.466311,5.024320,6.284251,-7.123283,8.167146,5.616725,-0.517000,-8.961567,0.126353,6.198804,4.833576,-6.041191,2.688065,1.405922,-8.671994,-0.037295,2.435218,-9.548108,7.844610,-6.677210,-5.192750,-2.666862,9.234144,-9.229355,1.286285,1.596864,-2.728772,8.483252,1.519531,-6.809906,-3.405150,-1.644192,1.723610,-6.127480,7.790807,9.654647,5.132974,2.266927,-2.457712,7.811917,6.746546,-1.671030,-1.744034,-4.817694,-3.052797,3.033284,5.828146,6.133976,-6.322963,5.899989], dtype = "float32")#candidate|3399|(429,)|const|float32
var_3400 = relay.var("var_3400", dtype = "float32", shape = (676,))#candidate|3400|(676,)|var|float32
call_3398 = relay.TupleGetItem(func_408_call(relay.reshape(const_3399.astype('float32'), [13, 3, 11]), relay.reshape(var_3400.astype('float32'), [676,]), ), 0)
call_3401 = relay.TupleGetItem(func_411_call(relay.reshape(const_3399.astype('float32'), [13, 3, 11]), relay.reshape(var_3400.astype('float32'), [676,]), ), 0)
output = relay.Tuple([call_3387,call_3398,const_3399,var_3400,])
output2 = relay.Tuple([call_3388,call_3401,const_3399,var_3400,])
func_3405 = relay.Function([var_3400,], output)
mod['func_3405'] = func_3405
mod = relay.transform.InferType()(mod)
var_3406 = relay.var("var_3406", dtype = "float32", shape = (676,))#candidate|3406|(676,)|var|float32
output = func_3405(var_3406)
func_3407 = relay.Function([var_3406], output)
mutated_mod['func_3407'] = func_3407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1021_call = mod.get_global_var('func_1021')
func_1023_call = mutated_mod.get_global_var('func_1023')
call_3447 = func_1021_call()
call_3448 = func_1021_call()
func_2246_call = mod.get_global_var('func_2246')
func_2248_call = mutated_mod.get_global_var('func_2248')
var_3460 = relay.var("var_3460", dtype = "uint64", shape = (160,))#candidate|3460|(160,)|var|uint64
call_3459 = relay.TupleGetItem(func_2246_call(relay.reshape(var_3460.astype('uint64'), [160,])), 3)
call_3461 = relay.TupleGetItem(func_2248_call(relay.reshape(var_3460.astype('uint64'), [160,])), 3)
const_3493 = relay.const([[[-2.573935,4.704233,8.705985,1.908300,-1.919202,2.882181,6.748316,-8.686059,-4.359370,-1.623241,8.587915,1.565303,-2.506117,9.797428,-6.331281,1.279267],[9.328945,0.583356,3.173042,-0.057819,-8.490639,6.882294,-0.171664,-8.055401,5.489763,8.403452,3.825941,7.019742,9.227739,5.088587,2.305390,-9.372977],[1.771187,7.716421,-1.959523,-1.663929,-1.451606,3.946082,-1.979662,9.446303,-7.886360,-0.620502,2.297352,7.857817,-6.107999,4.801896,8.429209,8.664940],[3.886936,3.625682,-5.409873,-3.554619,-0.606164,-2.032227,4.045829,-3.477801,-7.689769,-0.166105,-3.012382,-7.702850,-9.322430,-1.655453,0.143914,-1.954696],[5.277116,9.808236,0.971540,-6.608573,0.454644,-7.932353,-9.364915,-9.973746,-3.113530,7.417526,5.715576,0.620980,7.287469,1.683934,7.496183,1.049787],[-6.547032,1.328570,3.113859,2.272934,-3.411116,6.660555,-9.813879,1.074573,-6.371747,-9.811056,-5.951444,2.264759,7.120777,-9.421942,-3.062652,5.645098],[-5.289593,8.654184,-2.223506,-6.366798,-0.313161,-3.963583,-6.419128,8.955605,-9.456113,-3.457324,-9.777363,-0.603470,-1.481427,-2.732195,-8.859511,1.508831]],[[-8.397394,-6.641190,8.762424,1.546265,5.121727,8.614538,1.200677,-6.614833,-6.953006,-6.326048,1.212809,-4.409324,-7.358383,-9.784281,4.493431,8.551920],[-8.681172,-1.051772,7.458000,-7.768495,9.097902,-6.849274,-5.896584,-6.035350,6.687996,8.480988,7.938830,-7.804224,3.281624,5.402304,9.406834,-4.251968],[-2.117666,2.301775,5.500810,-4.307084,0.528459,3.017455,-9.961538,-6.405556,4.744903,-4.603754,-7.477894,-4.547542,3.786245,-6.537382,-5.678514,8.842308],[9.481050,-0.794491,-0.403353,-5.713081,6.358970,5.278105,0.918590,8.302134,-6.057652,-3.265468,5.488516,-9.089137,-6.324301,0.534574,2.794429,3.606332],[8.237901,4.521254,0.948776,-9.871746,-8.141850,-7.955344,6.195291,-8.000338,4.308676,-8.492388,6.170504,5.096703,1.735943,-9.379521,1.445441,-5.839513],[-7.728041,-4.983534,7.850348,-9.034947,1.545529,1.911021,9.523041,-2.970749,-6.782411,5.143432,6.853474,8.787523,7.227265,9.079967,-4.117659,4.245582],[-6.765239,-1.638284,-0.441542,6.313204,2.764420,1.298407,-6.262392,2.999884,-1.282415,-7.562351,8.481229,8.328496,9.822316,-2.060122,-6.547610,-0.250154]],[[7.185464,-4.477802,-7.148374,5.085381,-1.009207,-9.044222,-3.251358,-9.072063,-8.913979,-2.401270,-4.055685,-2.683048,8.252327,8.400049,-9.840457,-4.813991],[-3.860796,-1.957212,-4.543217,-7.950105,-2.736624,9.742349,-7.876777,7.771983,-8.175738,9.750316,7.554920,-9.694268,-1.572951,-9.091145,-3.077201,-9.732179],[2.462193,2.521655,7.180458,9.308303,-4.734482,-8.315956,-0.065676,4.130005,-6.598935,4.760432,-1.976170,-7.116660,-4.012145,2.574128,3.606531,7.417605],[-4.945377,-4.655707,5.402829,5.990214,-2.344317,-2.539647,-0.003627,8.351013,-1.361540,-7.546043,-1.966717,8.796012,-3.116409,8.400783,6.202359,-2.972891],[6.919759,3.339078,-2.522948,-1.621388,-6.764616,4.387822,-2.367303,3.752801,-9.086286,1.566996,-0.443559,1.794424,-6.247152,-8.136048,1.756900,8.123882],[9.547949,8.120608,-4.053815,-4.263645,4.995699,5.583113,-8.060872,-8.303458,-0.915671,-4.305461,7.437785,1.111257,-3.312643,0.264735,2.140963,6.415370],[7.653893,-7.057768,-2.541337,-1.257684,9.136801,-9.442773,8.468982,-5.441458,-2.952186,-5.433847,-9.022563,7.610006,-4.420287,-3.663134,-1.343100,-8.743569]],[[2.655514,7.376513,-7.038407,2.276270,3.640856,7.404194,-5.359289,-4.735406,-7.871539,-3.012258,9.490010,-3.464344,-8.871129,3.952963,-0.181783,-9.160318],[-3.225199,4.359718,-3.797974,-0.254603,-5.581472,-9.671853,9.111028,-2.269396,0.901219,-2.676934,-1.391232,-4.648677,-1.884141,0.588836,-8.429247,-5.445714],[6.230158,8.210279,-4.694572,1.950264,9.047174,1.263313,3.072216,3.862118,0.829642,5.416745,-5.039142,-2.736585,8.712752,8.286048,-3.303916,-0.729411],[8.529752,5.865039,-9.116833,3.315813,-2.007159,-3.747407,-2.482017,-9.416670,-5.177382,1.764479,-6.916306,9.832476,-5.969646,9.653229,-2.405865,-8.640839],[3.385054,1.724630,7.879141,6.062321,2.163698,0.632420,4.944997,2.675220,0.972185,-7.474817,3.395248,6.172851,-0.126899,-7.706142,-6.211749,3.805206],[-5.457394,2.007935,0.183719,0.058969,7.500003,-1.655287,-2.863906,-3.502771,-4.767021,8.384129,-2.013086,6.988106,9.242890,0.696390,3.150538,3.708075],[7.096974,7.702830,-7.954207,5.899848,7.917406,-2.913393,-9.063193,0.441929,-8.524237,-3.967961,3.562659,1.268836,9.657193,-8.485970,6.581770,-7.612442]],[[2.222173,4.838749,-7.262626,6.033308,-4.665344,4.810566,-6.716240,-4.244766,-1.628409,9.586717,-7.835229,-1.357666,1.308078,-8.963069,1.182550,1.100484],[-6.590363,-6.146845,0.858759,-1.341938,3.189266,-6.643656,-9.891443,-1.234373,0.042693,-9.605515,9.349812,5.076569,-8.857221,1.520525,-8.642060,-8.614919],[-0.813708,6.847335,-9.271613,9.367073,-3.370547,4.018601,-4.031452,0.618170,5.145115,-2.246145,-9.342888,0.234712,0.379972,-0.719653,3.887400,1.289205],[1.400397,5.170854,-3.430427,-3.595330,1.943220,-4.997066,7.348730,2.035591,7.963972,4.254055,-1.700030,-6.203356,-4.106665,6.045358,5.614854,6.607312],[-7.204260,-6.985350,9.538123,5.244817,-9.038833,8.469946,8.906663,-6.900835,-1.026899,-7.030012,-5.448627,-7.875177,-6.913005,-2.978596,-9.653691,-2.617546],[8.962664,-9.643951,4.156043,4.210058,6.956433,-5.017596,1.076376,7.109564,-9.983023,-2.253262,3.961698,3.764347,5.901015,3.672230,9.897610,-2.523579],[7.576718,-2.180717,-5.970300,-8.688351,-3.050102,-3.196111,-1.756474,5.541090,1.931441,7.166809,-2.059949,-0.411307,6.997928,-4.401687,-8.396290,0.514559]],[[0.712520,-7.077323,5.768140,4.453235,1.242550,6.285244,4.353637,1.196496,8.169835,7.639054,4.856498,8.360593,-9.844776,-6.622793,-1.887822,-3.475633],[6.031936,7.597447,7.632527,-3.172916,-4.135791,-0.645887,-2.834646,-8.054243,7.983569,2.454797,-0.477781,7.115874,-3.529929,6.836643,1.756167,-8.427819],[-5.776124,8.984985,-9.554971,8.010913,0.393260,9.493147,7.699627,5.401164,0.472109,0.291850,9.168277,-3.708547,-2.622618,-5.491452,4.024188,-7.622489],[-8.926566,-2.767625,5.643126,7.379863,2.268533,-5.672980,6.217788,8.367624,9.632522,-2.204936,6.959532,-9.171250,-1.209225,7.883047,-5.544486,7.614840],[5.363842,7.400918,9.964834,-7.902193,1.146509,1.882776,-7.050690,-4.221555,-2.813218,3.595200,5.151567,1.085791,-3.850960,-0.732849,8.355881,-3.834287],[5.111084,1.674220,-4.760031,6.546336,0.755046,-1.832609,-8.257673,5.514442,8.925483,-1.199651,-1.650402,-1.527305,7.899272,0.160598,5.779354,8.341063],[-8.137991,5.394636,-2.500642,-6.403826,-0.824702,-5.845577,5.176013,7.614576,-7.480786,-6.576197,5.472896,9.321360,8.016966,2.568590,-3.202254,3.423691]],[[-9.593575,-3.139193,9.309581,-7.966872,1.454360,-0.886944,-4.644929,-5.164357,-0.731628,8.815934,5.888607,-5.106787,-3.867438,8.376907,-4.286728,9.096764],[-8.350286,-8.777768,-0.281479,2.287211,1.081955,9.295717,8.748072,-0.692241,-7.963396,5.946165,-3.855555,-9.638006,-0.139474,-3.577300,-4.680088,6.954688],[2.296624,-2.583720,-7.665369,3.753216,-6.016179,4.213314,-2.059429,0.919000,5.637503,5.702148,-1.157408,-8.024498,7.676641,1.983822,-7.445530,-2.395282],[-3.088189,-3.191891,-8.177458,-3.931403,-5.817810,-9.774015,5.620371,7.234715,7.398060,0.437125,-8.712723,-5.697011,-1.324979,8.306450,-6.393706,-9.096177],[-1.940578,0.028476,-5.997454,4.436084,5.917931,-3.495494,6.263333,6.301310,-3.522202,-8.147445,3.785562,-3.500629,5.219252,-7.116413,-5.480369,-3.918202],[4.629654,4.782210,-8.800612,-9.941027,2.233481,-4.695743,-2.733942,6.178641,-2.807990,8.687373,-0.072297,8.388081,2.556750,8.763819,-3.268341,1.533146],[7.361066,-2.403160,0.122071,6.250608,6.214065,-4.861568,2.731784,-5.437377,4.034910,5.847083,3.793471,2.267510,2.674406,-3.291678,3.375732,9.791635]],[[2.351833,-5.943606,0.158303,2.153318,0.582980,-3.366443,2.605634,4.280481,5.150426,-2.574838,6.196272,7.874845,-4.457159,7.731468,5.558385,-5.011857],[-6.418682,-3.025797,-4.639645,-7.821836,1.144448,-8.452521,9.582113,7.230028,1.484327,3.457126,-6.259770,6.711128,8.039034,-0.681261,6.597600,6.745644],[9.899792,3.831145,4.040418,5.669899,8.338893,1.756197,1.215953,8.813062,-3.051047,-0.296296,5.463158,3.358937,-1.353778,-7.421235,-2.976653,6.463761],[6.839300,5.889194,-8.018392,7.337518,-6.428552,-4.497099,6.540098,-2.145452,-9.702053,-9.959925,-9.950457,-7.343150,2.049048,4.512856,-5.263787,4.653066],[8.860751,-2.747611,-2.584762,8.770970,-3.739823,-4.042350,0.361569,1.057567,3.047628,-2.711161,7.441260,-6.674010,6.448593,-1.411957,-7.023725,0.281758],[-7.638744,4.039152,7.105639,-0.448285,-6.421039,9.128264,0.405185,-0.022502,9.351697,5.086627,2.300341,4.545755,3.116292,9.935238,-1.590702,2.507462],[-6.152508,1.436217,-1.042846,-0.840018,-0.081540,-5.948305,-4.687643,0.391417,3.973521,0.844879,-6.538572,5.209260,-2.214413,-8.323374,9.358725,-1.089307]],[[-2.556929,8.173040,3.900643,-4.976806,-8.261235,1.589125,8.031222,-3.073664,3.680053,3.805753,-1.093087,3.177161,0.574600,8.410206,-3.612616,3.833503],[0.700695,5.643177,-1.225155,8.035052,-3.741495,1.510492,8.702592,4.886826,2.777110,-1.215034,2.656004,9.937331,5.219057,-7.635573,-4.622073,6.391924],[-2.846950,-2.465636,-2.736938,6.349444,-7.879023,-2.662449,-4.508079,1.684656,-8.368243,-9.526899,6.681115,3.410570,-2.415807,-5.582493,5.912101,6.114412],[-8.854438,-3.842943,6.242990,-3.481728,-0.943037,5.596533,-0.776023,3.582385,-3.464147,-7.722559,0.341752,7.434101,6.606961,-4.850367,6.930677,4.951816],[2.320483,-3.265554,4.638078,-0.277973,0.685066,2.695873,-1.965104,-5.460702,-4.453710,7.811573,-6.567401,6.008870,-9.662424,-8.977286,2.760123,-1.186075],[9.235274,2.205298,2.403211,9.104817,2.908988,-7.276884,5.237926,0.877697,6.823128,7.511466,2.028431,-6.307748,-0.863873,9.271712,-3.229532,-9.846464],[-8.552813,-0.112609,9.339788,-2.275100,-9.952046,8.897585,8.157026,6.304316,7.715829,2.959431,-0.358510,-4.750662,-4.923041,-9.711605,4.623742,3.824079]],[[5.008026,6.208981,8.516399,2.102755,-2.552695,2.203474,2.626535,3.984494,4.520498,4.724571,-4.391188,-5.639137,2.468115,2.639748,8.420462,-3.162985],[-2.739136,9.061333,3.083532,-6.244005,9.665921,-1.220389,-4.868880,2.859973,-5.803437,1.468497,9.679225,7.824627,2.692762,9.686912,2.339754,0.628448],[-2.238256,1.655574,6.653707,4.487381,8.274350,-1.265608,2.902488,4.750334,-1.009225,-3.273578,-6.562100,0.704215,-1.858540,-3.861492,-1.872736,-5.724428],[2.979736,7.843264,7.658859,3.139597,-9.107736,-9.714770,-4.362831,0.589848,6.911712,-6.257791,3.167692,6.360076,-5.634308,-5.061532,0.563841,3.369782],[-5.110976,4.183995,-0.113890,3.597562,-3.933914,-2.488809,8.716338,-9.349007,-7.134910,9.549039,-9.472553,4.453063,-0.003953,7.025132,-7.062802,-7.570296],[2.235348,-6.682481,1.532232,-6.042171,-3.655650,-4.188096,-5.410698,-7.460577,4.947105,2.963807,-8.291695,-3.710757,-6.324225,-4.455200,1.671678,1.096126],[-3.265636,-0.040762,1.691474,-3.370692,5.812435,-6.350038,3.660238,-9.997655,-5.415598,-3.516934,0.240955,9.808318,-7.745417,-8.733039,7.532941,3.530453]],[[-2.951354,2.778404,-4.896383,0.014852,-9.301852,-8.512374,-3.752216,-7.978427,-1.524472,6.641542,1.476616,5.319805,-7.226550,4.405429,3.389163,8.086330],[-7.311680,-3.233411,-6.766535,6.240377,1.437508,-7.925964,-9.678372,-6.131959,3.694933,-6.880482,-3.897668,3.305230,-2.135117,-6.079515,1.786926,3.666540],[-7.996198,-3.670318,5.295794,5.491960,2.608560,-9.763533,-4.140737,-9.971645,-9.862152,6.352712,-3.591759,6.619408,0.808264,2.483073,0.417793,1.697816],[-4.452139,1.387149,3.299229,-4.890983,-3.780042,-1.824544,6.866433,6.929038,-3.689175,-7.219359,4.088718,0.642739,-4.753367,7.348839,9.480488,2.949824],[-8.958515,9.729139,-2.994834,6.456681,-8.443698,4.417254,-1.240994,1.485376,1.098300,-6.292838,5.079304,-3.009735,-2.608391,3.122445,-7.255382,2.526198],[1.872166,-1.946747,-4.462151,0.775099,6.421146,-8.654896,0.083071,-0.374451,2.848054,2.537733,-2.522472,-8.276101,8.871647,-5.140980,4.972891,-5.661305],[-5.085581,-5.550362,-1.848160,5.719224,-4.713315,-4.379070,8.989917,2.893144,7.987512,3.883793,-2.607204,-8.273711,-9.066599,2.465781,-3.887759,-8.586254]],[[-2.761043,4.664396,-6.447349,-6.170372,-5.926164,-9.785715,-6.577682,-0.399227,-4.253072,8.964158,-2.177726,-8.541175,2.887796,-1.906199,-1.365825,-0.574724],[4.556545,3.650238,1.668578,-4.840942,-7.663805,5.762004,-0.873881,-7.314669,-7.804750,3.376175,7.400845,0.009846,1.817113,-8.971992,-5.446389,-4.457116],[-3.229028,-1.625959,-4.146899,5.332096,8.679343,1.158573,2.682140,0.584679,4.799027,-2.808951,-1.661011,3.559287,0.105252,1.997666,4.645679,6.144515],[-2.635504,9.378484,-2.372553,9.673094,7.526402,-1.254701,6.010553,-2.330582,-7.145004,4.491512,-2.608021,5.353427,0.455553,-9.455378,-0.719731,-8.651242],[3.251423,3.044461,5.850909,2.792278,9.318455,9.644375,4.627498,-8.739116,-2.402925,1.830054,-4.129020,-6.010335,3.635409,-5.608254,-7.111666,-7.063019],[-0.350319,9.060008,1.895760,6.467503,-0.362813,6.177915,-2.024907,-4.134108,5.180711,-6.293679,-6.764624,6.057162,2.707694,7.471864,6.744577,4.283241],[-0.929053,7.075206,4.947135,-9.547218,2.979573,-7.848753,0.907897,-9.105513,-0.373134,4.481755,9.409978,-7.107815,-2.248374,-6.740999,-2.482775,-5.416670]]], dtype = "float64")#candidate|3493|(12, 7, 16)|const|float64
bop_3494 = relay.power(call_3447.astype('float64'), const_3493.astype('float64')) # shape=(12, 7, 16)
bop_3497 = relay.power(call_3448.astype('float64'), const_3493.astype('float64')) # shape=(12, 7, 16)
output = relay.Tuple([call_3459,var_3460,bop_3494,])
output2 = relay.Tuple([call_3461,var_3460,bop_3497,])
func_3503 = relay.Function([var_3460,], output)
mod['func_3503'] = func_3503
mod = relay.transform.InferType()(mod)
var_3504 = relay.var("var_3504", dtype = "uint64", shape = (160,))#candidate|3504|(160,)|var|uint64
output = func_3503(var_3504)
func_3505 = relay.Function([var_3504], output)
mutated_mod['func_3505'] = func_3505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3277_call = mod.get_global_var('func_3277')
func_3278_call = mutated_mod.get_global_var('func_3278')
call_3535 = func_3277_call()
call_3536 = func_3277_call()
var_3551 = relay.var("var_3551", dtype = "float32", shape = (16, 12, 5))#candidate|3551|(16, 12, 5)|var|float32
bop_3552 = relay.subtract(call_3535.astype('uint16'), relay.reshape(var_3551.astype('uint16'), relay.shape_of(call_3535))) # shape=(16, 12, 5)
bop_3555 = relay.subtract(call_3536.astype('uint16'), relay.reshape(var_3551.astype('uint16'), relay.shape_of(call_3536))) # shape=(16, 12, 5)
output = relay.Tuple([bop_3552,])
output2 = relay.Tuple([bop_3555,])
func_3572 = relay.Function([var_3551,], output)
mod['func_3572'] = func_3572
mod = relay.transform.InferType()(mod)
var_3573 = relay.var("var_3573", dtype = "float32", shape = (16, 12, 5))#candidate|3573|(16, 12, 5)|var|float32
output = func_3572(var_3573)
func_3574 = relay.Function([var_3573], output)
mutated_mod['func_3574'] = func_3574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2767_call = mod.get_global_var('func_2767')
func_2769_call = mutated_mod.get_global_var('func_2769')
call_3576 = relay.TupleGetItem(func_2767_call(), 0)
call_3577 = relay.TupleGetItem(func_2769_call(), 0)
output = relay.Tuple([call_3576,])
output2 = relay.Tuple([call_3577,])
func_3580 = relay.Function([], output)
mod['func_3580'] = func_3580
mod = relay.transform.InferType()(mod)
output = func_3580()
func_3581 = relay.Function([], output)
mutated_mod['func_3581'] = func_3581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2896_call = mod.get_global_var('func_2896')
func_2897_call = mutated_mod.get_global_var('func_2897')
call_3601 = func_2896_call()
call_3602 = func_2896_call()
output = relay.Tuple([call_3601,])
output2 = relay.Tuple([call_3602,])
func_3606 = relay.Function([], output)
mod['func_3606'] = func_3606
mod = relay.transform.InferType()(mod)
output = func_3606()
func_3607 = relay.Function([], output)
mutated_mod['func_3607'] = func_3607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2867_call = mod.get_global_var('func_2867')
func_2868_call = mutated_mod.get_global_var('func_2868')
call_3611 = relay.TupleGetItem(func_2867_call(), 1)
call_3612 = relay.TupleGetItem(func_2868_call(), 1)
output = relay.Tuple([call_3611,])
output2 = relay.Tuple([call_3612,])
func_3619 = relay.Function([], output)
mod['func_3619'] = func_3619
mod = relay.transform.InferType()(mod)
output = func_3619()
func_3620 = relay.Function([], output)
mutated_mod['func_3620'] = func_3620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1553_call = mod.get_global_var('func_1553')
func_1554_call = mutated_mod.get_global_var('func_1554')
call_3713 = relay.TupleGetItem(func_1553_call(), 0)
call_3714 = relay.TupleGetItem(func_1554_call(), 0)
func_3277_call = mod.get_global_var('func_3277')
func_3278_call = mutated_mod.get_global_var('func_3278')
call_3762 = func_3277_call()
call_3763 = func_3277_call()
var_3766 = relay.var("var_3766", dtype = "float32", shape = (16, 12, 5))#candidate|3766|(16, 12, 5)|var|float32
bop_3767 = relay.greater_equal(call_3762.astype('bool'), relay.reshape(var_3766.astype('bool'), relay.shape_of(call_3762))) # shape=(16, 12, 5)
bop_3770 = relay.greater_equal(call_3763.astype('bool'), relay.reshape(var_3766.astype('bool'), relay.shape_of(call_3763))) # shape=(16, 12, 5)
output = relay.Tuple([call_3713,bop_3767,])
output2 = relay.Tuple([call_3714,bop_3770,])
func_3771 = relay.Function([var_3766,], output)
mod['func_3771'] = func_3771
mod = relay.transform.InferType()(mod)
var_3772 = relay.var("var_3772", dtype = "float32", shape = (16, 12, 5))#candidate|3772|(16, 12, 5)|var|float32
output = func_3771(var_3772)
func_3773 = relay.Function([var_3772], output)
mutated_mod['func_3773'] = func_3773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2041_call = mod.get_global_var('func_2041')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_3783 = func_2041_call()
call_3784 = func_2041_call()
output = call_3783
output2 = call_3784
func_3821 = relay.Function([], output)
mod['func_3821'] = func_3821
mod = relay.transform.InferType()(mod)
output = func_3821()
func_3822 = relay.Function([], output)
mutated_mod['func_3822'] = func_3822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2458_call = mod.get_global_var('func_2458')
func_2459_call = mutated_mod.get_global_var('func_2459')
call_3925 = relay.TupleGetItem(func_2458_call(), 0)
call_3926 = relay.TupleGetItem(func_2459_call(), 0)
output = call_3925
output2 = call_3926
func_3935 = relay.Function([], output)
mod['func_3935'] = func_3935
mod = relay.transform.InferType()(mod)
output = func_3935()
func_3936 = relay.Function([], output)
mutated_mod['func_3936'] = func_3936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3606_call = mod.get_global_var('func_3606')
func_3607_call = mutated_mod.get_global_var('func_3607')
call_3982 = relay.TupleGetItem(func_3606_call(), 0)
call_3983 = relay.TupleGetItem(func_3607_call(), 0)
output = relay.Tuple([call_3982,])
output2 = relay.Tuple([call_3983,])
func_3991 = relay.Function([], output)
mod['func_3991'] = func_3991
mod = relay.transform.InferType()(mod)
output = func_3991()
func_3992 = relay.Function([], output)
mutated_mod['func_3992'] = func_3992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2041_call = mod.get_global_var('func_2041')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_4033 = func_2041_call()
call_4034 = func_2041_call()
var_4035 = relay.var("var_4035", dtype = "uint64", shape = (160,))#candidate|4035|(160,)|var|uint64
bop_4036 = relay.floor_divide(call_4033.astype('float64'), relay.reshape(var_4035.astype('float64'), relay.shape_of(call_4033))) # shape=(160,)
bop_4039 = relay.floor_divide(call_4034.astype('float64'), relay.reshape(var_4035.astype('float64'), relay.shape_of(call_4034))) # shape=(160,)
output = bop_4036
output2 = bop_4039
func_4043 = relay.Function([var_4035,], output)
mod['func_4043'] = func_4043
mod = relay.transform.InferType()(mod)
mutated_mod['func_4043'] = func_4043
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4044 = relay.var("var_4044", dtype = "uint64", shape = (160,))#candidate|4044|(160,)|var|uint64
func_4043_call = mutated_mod.get_global_var('func_4043')
call_4045 = func_4043_call(var_4044)
output = call_4045
func_4046 = relay.Function([var_4044], output)
mutated_mod['func_4046'] = func_4046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3580_call = mod.get_global_var('func_3580')
func_3581_call = mutated_mod.get_global_var('func_3581')
call_4100 = relay.TupleGetItem(func_3580_call(), 0)
call_4101 = relay.TupleGetItem(func_3581_call(), 0)
uop_4103 = relay.log2(call_4100.astype('float64')) # shape=(1, 7, 16)
uop_4105 = relay.log2(call_4101.astype('float64')) # shape=(1, 7, 16)
output = relay.Tuple([uop_4103,])
output2 = relay.Tuple([uop_4105,])
func_4144 = relay.Function([], output)
mod['func_4144'] = func_4144
mod = relay.transform.InferType()(mod)
output = func_4144()
func_4145 = relay.Function([], output)
mutated_mod['func_4145'] = func_4145
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4149 = relay.var("var_4149", dtype = "float32", shape = (5, 1, 16))#candidate|4149|(5, 1, 16)|var|float32
uop_4150 = relay.asinh(var_4149.astype('float32')) # shape=(5, 1, 16)
output = uop_4150
output2 = uop_4150
func_4166 = relay.Function([var_4149,], output)
mod['func_4166'] = func_4166
mod = relay.transform.InferType()(mod)
var_4167 = relay.var("var_4167", dtype = "float32", shape = (5, 1, 16))#candidate|4167|(5, 1, 16)|var|float32
output = func_4166(var_4167)
func_4168 = relay.Function([var_4167], output)
mutated_mod['func_4168'] = func_4168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2439_call = mod.get_global_var('func_2439')
func_2440_call = mutated_mod.get_global_var('func_2440')
call_4257 = relay.TupleGetItem(func_2439_call(), 0)
call_4258 = relay.TupleGetItem(func_2440_call(), 0)
output = relay.Tuple([call_4257,])
output2 = relay.Tuple([call_4258,])
func_4267 = relay.Function([], output)
mod['func_4267'] = func_4267
mod = relay.transform.InferType()(mod)
mutated_mod['func_4267'] = func_4267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4267_call = mutated_mod.get_global_var('func_4267')
call_4268 = func_4267_call()
output = call_4268
func_4269 = relay.Function([], output)
mutated_mod['func_4269'] = func_4269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3619_call = mod.get_global_var('func_3619')
func_3620_call = mutated_mod.get_global_var('func_3620')
call_4336 = relay.TupleGetItem(func_3619_call(), 0)
call_4337 = relay.TupleGetItem(func_3620_call(), 0)
output = call_4336
output2 = call_4337
func_4343 = relay.Function([], output)
mod['func_4343'] = func_4343
mod = relay.transform.InferType()(mod)
output = func_4343()
func_4344 = relay.Function([], output)
mutated_mod['func_4344'] = func_4344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_4351 = func_1075_call()
call_4352 = func_1075_call()
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
const_4358 = relay.const([[False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False]], dtype = "bool")#candidate|4358|(1, 182)|const|bool
call_4357 = relay.TupleGetItem(func_3244_call(relay.reshape(const_4358.astype('bool'), [14, 1, 13])), 0)
call_4359 = relay.TupleGetItem(func_3246_call(relay.reshape(const_4358.astype('bool'), [14, 1, 13])), 0)
const_4360 = relay.const([[True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,True],[False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,True],[True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False],[False,False,True,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,True],[True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,True],[True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,True,True],[True,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,False],[False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False],[False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True],[False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True],[False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True]], dtype = "bool")#candidate|4360|(11, 182)|const|bool
bop_4361 = relay.divide(const_4358.astype('float64'), const_4360.astype('float64')) # shape=(11, 182)
var_4378 = relay.var("var_4378", dtype = "float64", shape = (2, 7, 16))#candidate|4378|(2, 7, 16)|var|float64
bop_4379 = relay.power(call_4351.astype('float64'), var_4378.astype('float64')) # shape=(2, 7, 16)
bop_4382 = relay.power(call_4352.astype('float64'), var_4378.astype('float64')) # shape=(2, 7, 16)
func_3179_call = mod.get_global_var('func_3179')
func_3181_call = mutated_mod.get_global_var('func_3181')
call_4388 = relay.TupleGetItem(func_3179_call(), 0)
call_4389 = relay.TupleGetItem(func_3181_call(), 0)
output = relay.Tuple([call_4357,bop_4361,bop_4379,call_4388,])
output2 = relay.Tuple([call_4359,bop_4361,bop_4382,call_4389,])
func_4396 = relay.Function([var_4378,], output)
mod['func_4396'] = func_4396
mod = relay.transform.InferType()(mod)
var_4397 = relay.var("var_4397", dtype = "float64", shape = (2, 7, 16))#candidate|4397|(2, 7, 16)|var|float64
output = func_4396(var_4397)
func_4398 = relay.Function([var_4397], output)
mutated_mod['func_4398'] = func_4398
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4419 = relay.var("var_4419", dtype = "uint16", shape = (2, 12, 2))#candidate|4419|(2, 12, 2)|var|uint16
var_4420 = relay.var("var_4420", dtype = "uint16", shape = (2, 12, 2))#candidate|4420|(2, 12, 2)|var|uint16
bop_4421 = relay.less_equal(var_4419.astype('bool'), relay.reshape(var_4420.astype('bool'), relay.shape_of(var_4419))) # shape=(2, 12, 2)
bop_4440 = relay.logical_xor(var_4420.astype('int8'), relay.reshape(var_4419.astype('int8'), relay.shape_of(var_4420))) # shape=(2, 12, 2)
output = relay.Tuple([bop_4421,bop_4440,])
output2 = relay.Tuple([bop_4421,bop_4440,])
func_4448 = relay.Function([var_4419,var_4420,], output)
mod['func_4448'] = func_4448
mod = relay.transform.InferType()(mod)
mutated_mod['func_4448'] = func_4448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4448_call = mutated_mod.get_global_var('func_4448')
var_4450 = relay.var("var_4450", dtype = "uint16", shape = (2, 12, 2))#candidate|4450|(2, 12, 2)|var|uint16
var_4451 = relay.var("var_4451", dtype = "uint16", shape = (2, 12, 2))#candidate|4451|(2, 12, 2)|var|uint16
call_4449 = func_4448_call(var_4450,var_4451,)
output = call_4449
func_4452 = relay.Function([var_4450,var_4451,], output)
mutated_mod['func_4452'] = func_4452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3935_call = mod.get_global_var('func_3935')
func_3936_call = mutated_mod.get_global_var('func_3936')
call_4526 = func_3935_call()
call_4527 = func_3935_call()
output = relay.Tuple([call_4526,])
output2 = relay.Tuple([call_4527,])
func_4545 = relay.Function([], output)
mod['func_4545'] = func_4545
mod = relay.transform.InferType()(mod)
mutated_mod['func_4545'] = func_4545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4545_call = mutated_mod.get_global_var('func_4545')
call_4546 = func_4545_call()
output = call_4546
func_4547 = relay.Function([], output)
mutated_mod['func_4547'] = func_4547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2041_call = mod.get_global_var('func_2041')
func_2043_call = mutated_mod.get_global_var('func_2043')
call_4577 = func_2041_call()
call_4578 = func_2041_call()
output = relay.Tuple([call_4577,])
output2 = relay.Tuple([call_4578,])
func_4599 = relay.Function([], output)
mod['func_4599'] = func_4599
mod = relay.transform.InferType()(mod)
output = func_4599()
func_4600 = relay.Function([], output)
mutated_mod['func_4600'] = func_4600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_4608 = relay.TupleGetItem(func_4144_call(), 0)
call_4609 = relay.TupleGetItem(func_4145_call(), 0)
func_2416_call = mod.get_global_var('func_2416')
func_2418_call = mutated_mod.get_global_var('func_2418')
call_4625 = relay.TupleGetItem(func_2416_call(), 2)
call_4626 = relay.TupleGetItem(func_2418_call(), 2)
output = relay.Tuple([call_4608,call_4625,])
output2 = relay.Tuple([call_4609,call_4626,])
func_4634 = relay.Function([], output)
mod['func_4634'] = func_4634
mod = relay.transform.InferType()(mod)
output = func_4634()
func_4635 = relay.Function([], output)
mutated_mod['func_4635'] = func_4635
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4648 = relay.const([[-2.437596,2.495793,-6.698673,-4.376899],[-4.309928,1.667759,6.027850,5.878469],[5.488613,-8.884994,3.826055,5.196394],[7.319482,-1.714758,-3.323987,9.338054],[-6.477595,-5.621816,-7.345957,-7.055144],[5.051463,-3.356112,-2.293257,3.107054],[3.810612,-9.135894,2.655041,-4.745641],[-7.896523,0.205074,-2.543689,-7.308459],[2.276851,-3.137105,0.820648,-8.966447]], dtype = "float64")#candidate|4648|(9, 4)|const|float64
uop_4649 = relay.asin(const_4648.astype('float64')) # shape=(9, 4)
output = uop_4649
output2 = uop_4649
func_4656 = relay.Function([], output)
mod['func_4656'] = func_4656
mod = relay.transform.InferType()(mod)
mutated_mod['func_4656'] = func_4656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4656_call = mutated_mod.get_global_var('func_4656')
call_4657 = func_4656_call()
output = call_4657
func_4658 = relay.Function([], output)
mutated_mod['func_4658'] = func_4658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2416_call = mod.get_global_var('func_2416')
func_2418_call = mutated_mod.get_global_var('func_2418')
call_4680 = relay.TupleGetItem(func_2416_call(), 1)
call_4681 = relay.TupleGetItem(func_2418_call(), 1)
func_776_call = mod.get_global_var('func_776')
func_780_call = mutated_mod.get_global_var('func_780')
var_4687 = relay.var("var_4687", dtype = "int64", shape = ())#candidate|4687|()|var|int64
const_4688 = relay.const([-7,-7,-2,-8,-7,1,5,-6,5,9,-2,-9,9,-2,-7,10,-7,8,9,-6,9,8,1,6,-5,-6,-4,-7,-6,-9,7,-7,-6,6,3,10,9,-5,-3,8,7,-6,-8,-4,-1,7,2,-4,9,2,10,-3,3,1,10,-3,-3,8,1,8,-4,-1,9,7,-5,-9,2,-6,-1,-10,-6,9,-3,3,-10,-7,5,3,3,-1,8,5,-5,6,6,8,10,-3,8,-6,-8,5,2,7,-9,-4,-2,8,10,3,9,-9,-1,-1,-10,-7,1,-2,-9,8,9,6,3,-9,7,8,-5,6,-1,5,5,10,6,-1,-2,5,-3,5,5,6,5,-10,10,4,-3,3,-5,-6,-6,5,5,1,9,1,-9,-7,-2,-3,-1,4,-8,-1,-1,-3,3,-6,6,-6,3,-10,-6,-7,4,-1,-6,8,-3,6,-8,-2,7,-1,5,-1,-7,-3,9,-3,7,-7,-10,-9,-6,10,6,-8,8,-5,9,3,6,-10,5,8,-9,5,10,6,-8,1,-6,6,-8,-9,6,4,-10,-9,-10,-7,1,-10,-5,-6,-1,-7,-6,3,4,3,-5,-4,-3,-10,-1,2,8,-1,-6,-7,4,6,-7,-3,10,-2,3,2,10,-9,-8,3,2,-10,-10,7,-1,5,-1,-8,4,-8,6,5,1,-7,4,8,3,-6,4,-9,8,10,2,-2,8,7,9,9,5,-2,7,7,-7,7,8,-4,-9,6,2,10,-8,-3,-9,1,-2,5,3,3,6,-1,3,-1,-10,4,2,4,-10,-9,1,3,2,-5,1,-7,6,-1,3,-3,-8,-7,-2,-2,-7,-1,2,-6,-3,1,8,1,4,-7,6,10,-9,-8,-7,7,-3,6,4,2,-2,-1,9,-6,-6,1,-3,7,9,6,6,-4,2,6,2,3,-1,4,-6,4,-3,5,-8,-9,8,5,-1,-4,-8,10,8,-4,8,8,10,8,-9,-1,-5,-3,8,-6,-4,-1,-3,-4,4,10,8,10,2,-3,-10,5,5,-8,-6,1,7,4,-2,-2,6,2,2,4,-1,2,-9,7,-6,8,-1,2,2,-9,4,-3,-3,-6,9,8,7,1,10,-4,3,8,1,-2,-8,7,2,4,-9,2,-4,-9,-2,-9,-8,-9,-4,-5,-7,-10,-9,6,-9,7,-5,-7,1,10,-6,-6,-1,-7,9,2,2,10,-8,-3,9,6,-10,10,1,-3,-8,-5,-3,4,6,-8,7,-10,-4,-2,4,6,-3,3,6,-4,6,-3,-2,3,-2,-8,8,-2,2,5,5,8,-8,3,1,-8,7,-8,-8,-8,-9,-7,-4,-1,-6,2,10,1,-5,3,2,-2,3,-9,-10,-9,-3,8,-9,6,9,-7,10,-8,2,10,1,6,-2,4,2,-1,-2,-2,9,-6,-6,7,1,-10,5,9,-1,-1,-10,5,10,4,-6,-1,-6,3,-2,-7,-6,-5,6,10,-1,-2,-7,2,4,7,4,-5,7,-2,8,1,8,-6,4,-4,8,7,-3,-3,6,-7,2,-3,-9,7,6,-1,5,-1,-3,5,2,-7,2,-4,-1,-9,2,-1,6,-8,7,-9,7,5,-4,3,2,-3,-3,-3,7,-9,-3,-1,10,3,9,2,-9,-9,-7,3,6,6,-2,-6,-10,-9,3,3,-9,1,-8,7,-9,-4,-9,-8,10,4,2,4,-5,6,-5,1,7,4,-6,5,-5,4,6,1,-5,-10,7,8,7,9,-4,7,-4,-7,2,-6,10,3,1,2,2,-4,7,2,5,-7,-4,10,-5,-8,8,-4,-5,4,2,3,-9,-5,-8,-2,10,2,4,-10,9,-4,4,-5,6,7,7,-3,7,-5,-7,-8,6,9,-3,9,-8,1,2,1,7,-5,5,3,8,-7,-4,-9,6,-4,-8,-3,7,-6,-1,-6,-4,3,1,-3,3,-3,6,1,2,3,8,4,-9,4,-9,8,-3,5,6,-4,-10,6,-1,-8,-2,-2,-6,-4,9,6,-8,3,5,7,8,8,10,-3,-3,-3,3,-7,-4,-7,9,-10,8,-10,3,-2,-9,-10,8,-10,-6,8,-8,10,6,-4,-1,-5,2,-1,3,8,6,2,1,5,-5,-9,-9,-7,-8,-1,-9,-9,-2,-6,6,10,1,-7,4,-2,-6,5,3,2,7,2,2,5,-4,2,4,-3,3,-9,-4,7,-3,-7,8,-10,5,-9,7,-4,6,2,-7,4,5,-9,6,8,10,-8,5,3,3,-10,7,-9,9,2,-6,-7,2,1,2,7,-5,2,4,3,-7,-6,-6,-7,8,-10,-8,7,-3,-7,-8,-8,-1,6,-6,-3,-1,-7,-5,9,-6,10,-7,1,7,-4,-2,9,-3,-9,3,3,-2,-8,-7,-4,7,-6,-3,4,-6,-5,3,2,-9,6,-4,4,9,4,-1,10,2,-4,-4,-5,9,9,-5,7,-3,-6,1,-4,5,10,-6,-6,6,-3,2,-1,1,-2,-2,-2,3,-3,-9,-7,-4,-10,7,1,10,6,-4,-3,-6,1,8,-2,-1,-5,1,-5,-1,9,5,-5,-4,6,-7,-4,8,8,9,4,4,-10,-3,2,-4,-6,-1,-3,-2,-4,10,10,1,3,-10,10,8,1,-9,-7,-5,1,6,10,4,6,10,-3,6,3,-3,-1,4,-2,6,3,4,9,9,5,3,-7,-9,-8,-6,-2,3,-8,5,8,-1,5,9,3,-3,-9,-2,-3,-1,-6,9,6,1,-1,-5,-10,-1,2,-10,8,-7,-4,-7,10,6,-5,-3,-1,4,-3,-10,-7,-9,-3,-6,-4,7,-10,5,-2,-7,9,5,-4,-9,-10,-1,2,-8,1,-3,6,5,6,-7,10,-3,-4,9,9,-7,7,-8,8,-3,9,-3,9,1,7,-4,-2,8,-5,-5,4,-5,-8,1,10,-4,-1,-4,-7,6,4,3,-4,3,-7,-6,-8,4,-6,3,-1,7,-8,-2,7,-6,-7,9,9,5,-10,-9,-3,-6,7,9,8,10,8,-8,-2,-7,5,-2,-10,2,-9,-6,-3,-5,4,8,9,-8,4,1,-4,6,-6,6,7,-4,9,9,4,2,-8,-2,2,2,-7,1,3,1,-8,-3,-6,-1,1,-7,-6,5,-3,10,6,-1,-7,4,-4,7,-3,6,1,4,-9,-9,4,-10,-2,2,2,-2,-8,9,5,-3,-10,8,8,3,7,-4,-7,-7,5,-8,-3,-6,-7,4,-2,-10,7,4,-4,-5,-1,1,3,9,-7,5,-5,4,7,-6,6,1,-8,1,4,-4,-4,4,-4,3,10,-5,8,-9,-7,4,-4,9,2,3,-3,-2,3,4,1,-9,5,5,3,-10,10,-6,-1,-6,4,-10,6,3,7,5,5,8,9,-7,7,5,-1,4,7,-4,9,7,3,-3,9,10,-5,6,-2,-8,-8,10,7,1,4,-4,-7,-6,-5,3,-10,-6,3,-1,-4,-8,4,-2,-2,5,-8,6,-4,-6,-3,10,3,-10,-9,3,-10,6,9,-4,-2,-6,10,4,4,2,10,-5,-8,-9,-6,2,3,1,-7,2,6,8,10,9,-3,-3,2,5,-5,-9,-9,10,-1,4,7,-7,-6,10,-10,-9,-9,5,-2,-3,5,9,-5,5,-9,-3,-9,-9,7,8,-8,10,3,1,4,-2,8,-2,-10,10,-8,-6,-5,-1,-6,-2,7,-6,-5,-6,2,9,-1,4,10,1,-7,6,-3,6,5,6,8,-10,8,6,-6,-2,8,8,-10,-7,-5,-10,-7,8,4,3,5,-9,-1,-2,9,-4,2,6,-1,10,7,4,8,-7,-7,8,-6,-4,-9,-4,2,7,1,5,-10,8,7,-1,-6,-1,9,-5,-4,1,-9,4,-6,5,-8,-7,-7,6,-7,-1,7,7,1,10,3,9,-10,-3,-7,4,-3,4,8,-6,-8,9,10,1,8,-5,7,-2,10,-5,-6,-2,10,8,7,4,-10,-1,8,10,-7,6,-10,3,4,6,-7,-6,6,6,8,9,4,8,5,-8,4,6,-4,3,7,7,-8,10,7,-7,5,-2,-7,-10,10,-5,-6,8,10,-8,-3,-2,8,-6,7,1,-9,-2,3,1,2,8,6,7,-9,4,8,4,-7,2,-4,-7,-3,-1,1,-2,7,10,-7,-9,2,10,-9,-7,-5,-2,1,3,-8,-2,6,3,-7,-7,2,3,-9,-5,7,7,-2,-2,6,-6,-10,5,-6,1,3,-8,-6,-8,-3,-3,8,4,-9,-2,-10,1,-9,-9,-5,6,10,3,-4,1,8,8,4,-4,6,7,-4,-9,-5,6,1,-7,8,7,3,-9,-1,-6,9,-9,-8,3,7,5,-10,-3,6,2,-2,-6,-4,-7,-2,-2,-3,-5,9,4,-2,7,1,5,-2,1,-5,-10,-2,5,-9,4,-10,-4,-9,-5,5,-4,-4,4,-5,9,-2,10,5,5,-4,6,7,3,6,6,-1,-10,9,-10,-10,6,-9,3,4,6,8,2,-9,1,4,-1,-8,-2,6,3,5,8,-6,6,1,-7,-3,4,5,-9,1,-6,10,5,-3,4,8,10,2,-3,7,2,9,3,-1,3,-2,-10,10,-10,6,9,-5,7,4,-2,9,2,-2,-2,-7,5,-5,-4,2,7,10,-3,4,4,-1,-10,4,8,7,1,4,-3,-10,-5,-5,-4,6,-9,9,-10,-2,1,-2,-4,-7,-3,10,10,-5,4,-7,4,-8,-6,8,7,4,-8,5,3,6,4,2,-5,9,8,10,1,-4,-4,1,-2,7,1,-1,-5,10,2,3,2,9,-10,-9,6,8,-6,1,-3,-8,-2,7,-8,7,3,-1,6,3,10,8,5,-8,-4,1,-7,10,-9,-7,5,9,7,-1,10,8,-7,-6,2,-5,2,4,4,9,10,-10,-1,5,7,-1,-1,6,7,2,9,8,5,1,5,-3,-7,1,10,-5,3,7,-5,4,7,3,-3,-7,2,-8,-7,1,-1,-1,-10,1,2,-9,-1,1,7,5,-5,-10,10,6,-8,3,-1,2,3,-7,1,4,-7,9,-10,-5,7,-4,5,8,8,3,-6,-3,8,3,-5,1,-3,5,-7,2,10,-2,-7,6,-2,5,4,8,-5,3,-10,-2,-7,10,-1,-9,-8,4,3,-1,9,-2,1,6,1,-7,-4,-5,8,-4,-6,8,5,-1,1,1,7,4,-5,5,-10,8,3,-4,7,-10,2,-8,1,3,-1,-4,10,-6,8,3,-6,-9,-2,-8,2,3,5,1,3,7,-8,10,-1,-5,10,5,6,-2,9,-9,-7,5,6,-9,-7,10,-9,7,9,-7,9,4,7,8,-6,-7,1,-7,5,3,4,1,-8,-1,2,7,-1,-9,-6,4,-3,-7,2,-1,-1,1,10,9,2,-4,-10,-6,-9,-9,3,7,4,-2,9,3,8,5,10,3,-4,6,7,6,8,-10,-1,-7,-2,-1,-2,5,2,5,6,4,6,-5,-4,6,-6,-3,5,2,-10,-2,-1,2,7,-5,-7,2,-1,-6,-7,6,-1,2,10,-5,9,5,-4,-3,-6,3,-7,7,-3,-2,-5,8,1,4,-4,-4,-8,-2,5,3,-2,-5,5,-9,-4,1,-3,-7,-6,6,10,4,-8,-10,10,6,-4,-2,-2,-7,6,-8,-4,-1,-6,2,-6,5,3,-7,-1,-6,4,3,-3,-2,6,-5,-7,-5,-3,10,-5,3,2,-10,5,-9,-8,-2,-3,-7,6,-1,8,5,-7,1,2,10,6,-1,10,7,-2,-6,-7,4,-4,-6,5,6,-10,3,-2,8,-5,-6,-8,-2,4,-5,-2,6,-6,-10,6,2,-6,-8,8,-6,-6,9,-9,-4,8,6,10,7,4,8,5,8,5,-10,3,-9,2,2,-8,4,8,7,10,8,1,-6,6,-10,9,7,9,2,1,-1,-4,4,-5,-2,4,10,5,-4,9,5,5,1,-5,5,9,-6,1,5,-10,-10,8,-2,4,-6,-1,1,1,9,-7,4,10,-10,-10,6,3,-8,4,4,5,2,-8,-1,-7,7,-7,-3,-10,10,8,-2,10,2,10,-5,-5,-1,10,-4,-6,-4,-1,-2,9,-3,-7,-10,4,2,-9,9,2,10,5,2,6,-4,2,-10,-7,-10,7,-1,3,5,10,9,-5,7,-3,-1,4,6,3,-9,-8,-7,10,-5,3,6,-5,9,-3,2,-5,5,-10,7,10,6,-4,2,-2,6,9,1,6,6,8,7,2,-5,6,6,8,1,-6,8,2,-1,8,6,4,5,-1,5,6,-8,10,6,7,-1,-2,8,5,-6,-5,-10,6,1,10,5,-6,8,-8,-5,4,7,-7,2,6,8,2,-2,-5,-8,-9,-1,-3,-10,-3,-5,10,-3,-8,-2,2,-8,8,-3,-3,8,-3,4,7,-8,-6,5,6,5,-2,-8,7,-1,8,-7,-6,-10,3,-6,5,-1,6,10,-6,5,4,-4,-1,-5,2,9,-7,6,2,-2,-5,-9,9,-4,4,4,-3,8,-5,5,5,5,3,-3,5,-2,-8,-3,8,-3,5,10,-8,-3,1,2,2,-9,-1,7,-2,6,10,9,5,2,-1,-9,3,4,10,2,-1,8,-7,-8,6,9,1,5,1,-7,4,-3,-8,2,3,1,-9,6,3,-3,7,-4,1,8,9,-8,1,-9,-10,-6,-7,7,-5,-9,8,-9,5,7,3,2,9,4,-3,9,-3,6,-4,-3,-7,-9,-6,2,-4,-1,-4,-8,3,5,4,-9,8,7,8,3,4,-2,10,4,-5,-10,10,-4,-3,-8,4,4,-3,-6,-8,-6,-10,-3,-4,-4,-5,-10,6,7,4,6,5,1,-8,-8,-3,1,5,-4,4,-10,6,-2,-3,-2,6,-6,-8,8,-4,-4,-3,2,10,6,6,3,-5,6,5,6,8,2,-1,-1,5,3,2,-5,-1,-8,-9,1,-5,-4], dtype = "int64")#candidate|4688|(2640,)|const|int64
const_4689 = relay.const([-8.742641,-7.950128,-3.514683,3.515330,-6.537485,-8.330521,-2.641934,-9.885720,0.964149,-8.229948,-0.771640,3.127824,-3.905617,-5.661926,5.756423,-5.123617,8.909680,-0.768289,-1.811673,-9.395563,0.866231,-5.388552,-0.812066,2.285789,-4.116890,-8.254953,7.991689,4.587430,8.792130,0.656997,-0.251573,-3.870167,-3.255760,9.440315,8.482101,6.237145,-6.720240,-0.970255,-1.843723,-1.765917,-6.751142,-9.593950,-1.821296,0.969757,0.205357,7.929737,1.237634,0.883812,-1.538978,-6.609096,-9.394685,-7.026684,5.182797,5.304600,6.906340,-7.969234,1.521196,5.582783,0.634287,5.325546,0.633537,-4.808095,8.283615,-1.593076,-3.933094,6.004295,-2.570996,4.326526,-4.713608,7.645490,-7.948478,1.906085,-6.247579,1.654252,-5.971339,-8.251007,5.747771,-9.036388,-2.327810,-5.883852,4.568008,-1.495762,-8.325176,6.908270,-0.496822,-1.758659,-8.880348,-4.172751,-4.707983,-8.173748,9.728118,-7.489473,6.176896,6.035784,4.513888,-2.480334,4.006730,-3.573370,-7.176823,-3.198149,-9.661452,8.361021,8.869514,-0.966178,-5.470159,-0.576104,3.908231,-6.744044,4.202240,7.700165,-8.442545,7.442227,-2.784898,9.246517,2.907580,8.349184,-7.669780,-6.413394,5.566073,1.647159,-7.472990,3.674506,-8.728463,-9.311638,6.961431,-2.778333,-5.116902,3.040783,6.420570,0.785801,-0.168136,-6.047441,-8.734252,-1.246688,5.396790,1.379262,4.658614,-6.043510,-1.674537,7.181981,-1.566258,7.278590,1.419130,2.257570,3.662807,5.714350,6.393506,-2.182661,5.293487,0.364261,-7.589113,-7.807146,2.051070,6.626864,9.919666,3.234608,-1.230652,-0.567913,5.449385,-3.638263,5.851272,1.502551,-3.902485,-0.353518,-8.140445,-8.455453,-8.747255,2.115180,9.014825,8.670117,0.601907,-2.697251,-1.477589,-3.269740,-3.588634,-4.469992,-6.414124,5.330420,-7.277046,-8.448652,5.735875,3.440860,1.379738,-4.047241,-9.974815,-5.705117,-0.365279,1.511585,9.052377,0.266669,7.036347,3.933164,2.245836,-2.011772,-1.804405,-5.733452,2.990263,9.177639,-4.462610,-0.315846,-5.180095,3.637028,7.607864,5.557921,-3.765528,8.511432,-5.291146,9.072999,1.737049,1.871145,5.826499,6.833650,-6.439865,8.758865,-9.004146,7.800931,-7.130345,-5.068163,9.196428,6.386927,-3.431066,6.737180,7.771894,-6.962468,-1.318704,2.835197,9.012953,1.436158,2.351128,1.669438,-7.352213,-1.639878,8.590726,-1.162469,-5.623499,-1.647895,-6.392873,-5.106268,-6.594827,-9.585144,-6.644468,-5.908333,6.845024,0.682946,1.689736,-2.208689,4.712622,-9.668147,9.607824,-9.305554,-3.360965,-6.207835,-9.038219,5.389606,0.262618,-3.439790,7.056162,-7.121213,-1.589664,3.882684,-2.456849,3.997520,8.093777,-9.975796,-2.106267,-0.381758,7.407212,-0.513470,0.924486,-8.566716,5.305906,8.524870,-0.852014,6.288623,0.709869,-9.762500,7.298389,-2.530508,5.214028,7.906526,4.040811,2.794071,2.131492,-4.751357,1.184610,7.266745,8.771091,2.059910,-9.521122,-6.554247,0.097098,1.587290,-0.821183,1.280053,-4.317712,-7.705992,2.807553,-9.974660,1.332426,4.965681,-6.957332,1.742164,9.595411,4.589239,-5.665826,-8.226430,-8.449436,-7.668450,0.993086,-1.804375,-9.950415,8.234438,-0.961847,-4.667056,-3.906967,-5.444765,7.274280,5.529864,-7.767090,-2.235000,-9.702035,3.795441,6.314179,-2.445119,1.491590,-5.214874,7.565844,8.424181,-8.201346,9.572542,-8.610683,3.722778,8.456147,-4.725943,3.228028,-3.962190,1.099080,-2.426936,4.996435,2.709555,7.147597,4.826586,4.911895,9.456478,-9.671325,8.368793,-9.441761,-8.974480,9.884751,-9.078100,-1.256351,-1.614521,-6.602579,-8.108856,6.159588,-9.951674,6.603201,9.542023,5.679075,-1.133451,6.524273,-9.382987,-9.869127,-3.983696,8.484975,-4.336868,8.528705,-8.414205,5.374783,-5.994119,-0.920029,-1.501155,-1.125352,5.867442,-2.964321,8.446239,7.780324,5.351883,7.167355,1.219356,-6.466988,-8.944814,-8.040562,3.919857,8.815979,1.929714,7.750941,4.195885,1.908635,4.811898,0.002545,-7.311150,-7.701786,-4.607430,7.422707,-1.571444,-2.758161,8.837323,7.489744,-3.744313,-0.347834,3.455800,5.449920,5.676653,9.373049,-1.459514,-8.802244,4.561365,5.091102,-6.087846,9.214877,-2.414902,8.521268,-7.181732,3.097105,4.190298,-4.414491,5.987801,8.682460,7.297222,9.246703,9.454471,-0.076576,-4.386577,6.104901,-7.081683,1.141144,-0.028795,-6.169959,-9.250254,3.628422,-3.188410,-4.006172,-6.692356,-7.431758,-8.662742,4.841503,0.298107,-9.863821,6.123005,-8.052066,-4.173089,0.244596,-1.493019,6.029900,5.274230,-4.478272,8.988960,6.570897,0.858992,5.956423,5.020884,2.189229,-6.348608,-5.180219,1.245642,7.994136,-9.841922,-5.345893,-1.932689,1.420145,5.972780,1.014236,-5.996609,-3.802861,9.939155,4.883180,-6.264062,0.395851,-3.112418,8.213723,2.928568,2.846528,0.645837,-9.889016,-7.335425,5.115292,-6.983574,-6.570874,9.715785,-3.643835,-0.935095,0.611688,-0.837617,1.530918,-5.909233,6.691906,3.256899,0.155173,-7.357587,-9.296826,-5.091528,-7.324042,6.573333,3.163384,4.686082,8.803777,-0.095109,2.967994,8.512436,8.895095,9.546581,4.583782,-5.113082,3.316985,3.935467,7.878523,9.738909,-4.498845,-4.779545,1.239930,1.702548,1.156960,1.570410,-1.951072,4.511335,-5.548556,-2.538010,7.877545,-7.725424,-2.701823,-7.432386,3.512030,7.582009,-4.558104,-5.489193,-4.006521,-3.686550,0.878696,-5.231746,8.304992,3.662997,-2.668590,3.666170,-9.413873,-6.463570,2.850622,-1.234192,-7.131959,-1.082929,4.292453,-2.762249,-6.975917,4.995437,-6.446222,-5.873539,8.424152,8.397995,3.601374,9.956369,-2.790347,-8.342486,4.654441,7.772924,1.716434,-2.078920,-9.573073,-6.670622,-4.332955,-3.624719,0.873928,-5.447409,-7.131710,-7.360720,-4.351519,-9.633604,8.453362,8.344696,6.228814,-9.764009,-0.779198,-2.329595,2.392918,-9.783928,-1.569796,-0.003743,8.952321,3.423409,-3.882072,8.301942,5.753520,9.772627,5.999559,6.756944,1.340096,8.509500,3.013422,-7.696876,-7.211269,-5.004222,1.495936,-5.799344,1.927756,9.975946,7.587404,-2.561430,-7.230366,6.095043,-6.108111,-4.771592,-0.504130,-0.704611,0.637833,-6.063938,9.004262,7.196165,6.763779,0.103409,4.431694,-9.762134,3.954976,0.599251,-1.583200,3.023204,-4.294497,7.040785,8.027401,-1.428798,-6.991985,-7.527191,1.862907,4.742441,4.727412,6.452673,4.521559,6.135741,-7.983520,-2.174469,7.690433,-7.423480,2.578819,-5.900849,7.623726,-5.087445,5.948608,2.119747,-5.539611,6.314479,6.289260,-9.377445,-8.376372,3.355876,-2.397010,-6.536723,-1.236966,1.619774,-6.823183,-9.958321,-7.411849,6.827307,-7.858664,-3.045215,6.685196,-9.435911,-4.424252,6.205975,8.619362,-1.691933,-5.136284,4.401660,5.498192,2.975086,3.329539,0.587048,-9.903116,8.522885,8.912437,2.825846,-6.122684,2.507955,-7.138058,7.854878,4.687809,4.025864,-3.525908,-5.644732], dtype = "float32")#candidate|4689|(676,)|const|float32
call_4686 = relay.TupleGetItem(func_776_call(relay.reshape(var_4687.astype('int64'), []), relay.reshape(const_4688.astype('int64'), [11, 16, 15]), relay.reshape(const_4689.astype('float32'), [676,]), ), 2)
call_4690 = relay.TupleGetItem(func_780_call(relay.reshape(var_4687.astype('int64'), []), relay.reshape(const_4688.astype('int64'), [11, 16, 15]), relay.reshape(const_4689.astype('float32'), [676,]), ), 2)
bop_4697 = relay.less(const_4689.astype('bool'), relay.reshape(call_4686.astype('bool'), relay.shape_of(const_4689))) # shape=(676,)
bop_4700 = relay.less(const_4689.astype('bool'), relay.reshape(call_4690.astype('bool'), relay.shape_of(const_4689))) # shape=(676,)
uop_4701 = relay.cosh(call_4680.astype('float32')) # shape=(16, 12, 5)
uop_4703 = relay.cosh(call_4681.astype('float32')) # shape=(16, 12, 5)
uop_4719 = relay.asinh(uop_4701.astype('float32')) # shape=(16, 12, 5)
uop_4721 = relay.asinh(uop_4703.astype('float32')) # shape=(16, 12, 5)
func_1503_call = mod.get_global_var('func_1503')
func_1505_call = mutated_mod.get_global_var('func_1505')
call_4725 = func_1503_call()
call_4726 = func_1503_call()
func_1075_call = mod.get_global_var('func_1075')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_4734 = func_1075_call()
call_4735 = func_1075_call()
output = relay.Tuple([var_4687,const_4688,bop_4697,uop_4719,call_4725,call_4734,])
output2 = relay.Tuple([var_4687,const_4688,bop_4700,uop_4721,call_4726,call_4735,])
func_4738 = relay.Function([var_4687,], output)
mod['func_4738'] = func_4738
mod = relay.transform.InferType()(mod)
mutated_mod['func_4738'] = func_4738
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4739 = relay.var("var_4739", dtype = "int64", shape = ())#candidate|4739|()|var|int64
func_4738_call = mutated_mod.get_global_var('func_4738')
call_4740 = func_4738_call(var_4739)
output = call_4740
func_4741 = relay.Function([var_4739], output)
mutated_mod['func_4741'] = func_4741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4599_call = mod.get_global_var('func_4599')
func_4600_call = mutated_mod.get_global_var('func_4600')
call_4766 = relay.TupleGetItem(func_4599_call(), 0)
call_4767 = relay.TupleGetItem(func_4600_call(), 0)
output = relay.Tuple([call_4766,])
output2 = relay.Tuple([call_4767,])
func_4772 = relay.Function([], output)
mod['func_4772'] = func_4772
mod = relay.transform.InferType()(mod)
output = func_4772()
func_4773 = relay.Function([], output)
mutated_mod['func_4773'] = func_4773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3821_call = mod.get_global_var('func_3821')
func_3822_call = mutated_mod.get_global_var('func_3822')
call_4779 = func_3821_call()
call_4780 = func_3821_call()
func_1021_call = mod.get_global_var('func_1021')
func_1023_call = mutated_mod.get_global_var('func_1023')
call_4786 = func_1021_call()
call_4787 = func_1021_call()
func_2169_call = mod.get_global_var('func_2169')
func_2172_call = mutated_mod.get_global_var('func_2172')
const_4791 = relay.const([[4,5,4,-9,-7,-2,6,-2,-3,-6,5,-4,7,7,-5,-6,-2,-1,1,9,-8,-7,-2,9,-9,-10,5,9,9,8,4,-3,5,5,3,-5,4,-7,10,10,3,4,-5,1,-1,-7,5,3,3,5,1,9,2,10,4,-3,-1,6,-2,-1,8,-7,-8,-2,-8,9,8,5,-5,-4,-6,-7,-4,6,-2,8,-4,4,5,5,4,3,1,2,4,5,2,10,5,-3,-2,8,4,-10,-9,-2,-10,-2,2,6,-9,7,-3,9,-2,6,1,-10,7,4,8,8,1,-8,6,-1,5,6,7,-5,-8,-3,-6,-6,4,10,5,7,-9,-1,8,-2,3,10,-5,-7,5,-2,2,3,-7,7,10,10,-10,6,6,-3,-6,-7,6,-4,5,-2,-5,2,-6,5,-4,5,9,-3,7,-2,-9,-4,4,-5,-5,5,-2,1,7,-5,-5,8,-2,-9,-9,4,1,-2,-7,3,6,9,6,-7,7,7,-2,6,-7,5,-5,1,-8,-10,-10,6,-2,3,6,-2,-1,5,-3,7,5,6,-2,3,-10,6,7,-7,6,6,1,5,8,-3,-2,-2,2,-4,-7,-6,-3,8,-4,-8,6,-2,-3,-8,10,5,-4,8,5,10,-2,-8,9,-2,2,3,5,8,4,-10,-9,-6,-2,-9,-8,-10,5,3,5,-5,7,-8,3,10,-1,-4,7,-3,6,-9,-1,5,6,-8,-3,-9,-2,3,-2,7,-5,-4,-2,-5,-9,5,3,5,-7,-4,9,1,10,-9,6,8,6,6,-10,-10,-5,-10,4,2,10,10,-9,3,6,4,7,-5,-3,-2,-2,-4,7,7,-9,1,-5,1,3,-3,-5,10,8,-4,6,6,8,7,3,-5,5,4,-8,-1,-8,-9,-3,4,4,-4,3,10,-1,-5,3,7,-5,-7,7,-3,6,7,-2,-9,-8,-1,-5,10,-8,-10,-6,-10,-7,5,8,-8,-1,2,-7,-4,-5,6,5,-6,3,-5,-3,10,-5,6,5,8,3,3,-2,-5,-1,-9,-8,-9,-2,-10,1,-7,-6,-10,8,-9,9,-1,9,9,8,6,4,-7,-2,-1,8,1,-8,-7,10,-7,7,1,-3,-6,8,-7,7,-9,2,4,-8,5,10,4,9,-9,9,-4,10,-3,2,-3,3,-10,3,-4,2,7,-3,-2,-10,1,-10,-2,-5,-1,7,7,-7,5,-4,-1,2,8,8,-8,-10,-10,3,1,6,-8,7,3,4,-5,10,-5,-5,8,3,-2,6,-3,1,-1,-7,2,-4,-9,-6,9,2,10,8,-1,-5,-2,-2,-4,-9,1,-3,2,-1,-6,-9,3,-8,9,3,7,-2,1,-3,6,-9,10,2,-9,-4,10,-9,-5,7,3,5,-10,-8,-8,5,5,-2,5,-8,9,-9,-5,3,5,5,2,9,-6,4,-8,-7,2,-9,-5,1,-10,4,-1,7,-1,-6,-4,-6,10,4,6,4,-3,6,1,-4,10,-8,7,8,10,10,7,-4,-5,-8,2,-10,4,-2,7,-7,4,-9,3,-8,9,8,-3,4,3,-10,3,-9,-7,-3,-7,-3,-6,-3,-8,-3,-8,-7,-3,10,5,8,-1,7,8,-6,10,9,10,6,-4,8,-10,-4,6,-9,-7,8,-4,9,5,-8,-3,-3,-8,4,10,3,-7,-4,-4,-3,-10,8,-4,-7,-10,-3,3,-7,-9,-2,-1,10,5,-10,-7,-7,-3,-2,-1,7,-3,4,8,-6,2,-5,-6,-2,1,7,4,4,10,-6,4,-2,-4,2,8,1,9,-5,-3,5,1,-1,-7,-4,-10,7,4,2,6,1,3,5,10,-6,-9,6,-2,-4,-1,-5,9,-6,9,-2,-1,8,5,-7,-3,7,-1,-1,9,3,6,-2,9,-9,-7,5,3,3,7,10,-2],[-4,-9,7,2,7,-7,6,-8,-6,5,-4,-5,4,-6,5,-3,-10,-6,8,8,-8,6,-3,-9,1,2,-2,-2,-10,3,6,-4,6,-5,8,2,10,-1,4,4,4,1,-3,-2,-1,8,-9,-4,-10,9,-2,-7,-1,-5,-6,2,-5,6,6,-10,-3,4,1,-4,7,-1,6,-3,-4,-2,9,4,7,-3,8,-1,2,-10,5,3,1,3,4,4,6,10,-10,-1,-4,1,8,2,9,-2,-10,-8,-3,-8,-7,-4,-8,10,1,-4,-6,7,-1,3,-5,-6,-3,3,3,10,-4,7,-1,8,10,6,-1,7,6,-3,6,3,2,-5,9,-9,2,-5,-4,-6,8,-8,7,-2,7,1,5,-5,3,-3,5,-7,9,1,-6,-8,7,3,5,-6,-1,8,-2,-4,-10,9,-1,2,10,-5,-10,-1,3,10,1,10,2,9,-10,-1,2,-8,10,-6,5,9,6,-2,-5,-5,-8,-2,3,-8,-6,5,-3,-2,-3,3,10,1,1,-7,6,5,-8,-8,-10,-6,-7,6,-2,-1,7,-4,6,-6,-1,-5,4,-2,-7,-3,-7,3,10,4,-10,-8,10,5,-7,5,4,4,-8,-10,9,3,-4,1,-8,7,-9,4,-7,7,9,-4,2,3,-6,-6,-8,-2,7,-6,6,2,8,-7,6,9,-8,10,-2,-9,-6,3,3,-4,-9,-7,4,10,-7,7,3,-9,-10,10,-10,10,3,9,1,8,6,4,-7,1,3,7,5,-8,5,-7,-6,-10,-4,-5,-2,6,-2,-7,-7,3,6,8,6,-6,-4,5,-2,9,3,1,-10,-3,-7,9,9,-4,4,6,-7,-10,-3,-3,9,1,7,-9,-10,7,-5,3,-10,6,-8,3,-5,10,-7,5,4,-2,-9,-8,-5,8,3,3,10,-7,-4,-6,5,-6,-1,-10,6,-6,5,6,10,2,-7,9,4,6,8,6,-9,6,5,5,-10,-8,8,6,10,-3,3,-4,8,7,-3,-7,-7,-4,-3,-6,3,-9,-8,1,3,4,-4,4,-8,7,-4,-8,9,5,-5,6,-5,-1,10,-10,5,-10,2,-2,5,-4,4,-1,-7,7,-9,2,-8,4,6,-2,8,2,5,10,5,-8,9,-4,-8,-8,3,-9,-10,8,9,-9,-3,-6,-6,8,-4,10,8,10,2,10,-6,6,-4,-6,-6,1,-5,-8,7,4,-4,7,-8,-7,4,6,8,10,8,-6,-10,-4,6,-7,9,6,-6,7,-9,4,6,7,-4,8,4,6,3,-8,3,-3,7,-8,-4,6,-3,-9,2,3,-5,-10,4,-3,-8,-7,-6,-5,-2,5,10,-9,4,10,-8,-2,3,-1,9,-6,-5,-10,-5,-4,-8,3,2,10,4,2,2,-4,-7,4,1,5,-2,6,9,-6,-1,-6,-5,-9,-6,-8,6,-5,-6,-10,-8,-2,-9,-10,8,-7,9,4,-10,10,5,-8,1,-7,-2,-4,2,-3,-6,-3,-10,-5,-4,10,1,1,1,8,-3,-9,-2,7,10,-8,2,-1,4,9,5,3,3,-4,5,6,-9,-5,9,8,4,6,-7,-8,2,-8,-9,3,-7,6,-10,-10,-7,-9,-10,6,3,10,8,3,-7,9,4,-10,8,10,8,7,8,-4,5,10,1,-9,10,-10,-3,-3,-10,7,-8,-6,-1,-4,10,-5,7,2,7,-6,3,2,-5,-4,-7,-3,-10,-3,-3,-9,-4,-8,2,-6,1,-6,10,-10,-4,-9,5,-7,-2,-5,-5,8,1,-10,-5,-3,-10,9,-10,6,1,-6,7,1,-4,-2,5,10,-5,-10,-7,-5,6,9,-2,2,8,10,-1,-7,-1,6,9,1,-6,-6,-8,10,-4,-9,-3,2,9,9,4,7,-4,-9,-8,-9,-3,-7,-6,4,7,-8,6,-2]], dtype = "int32")#candidate|4791|(2, 728)|const|int32
call_4790 = relay.TupleGetItem(func_2169_call(relay.reshape(call_4786.astype('float32'), [16, 1, 7]), relay.reshape(const_4791.astype('int32'), [16, 13, 7]), ), 3)
call_4792 = relay.TupleGetItem(func_2172_call(relay.reshape(call_4786.astype('float32'), [16, 1, 7]), relay.reshape(const_4791.astype('int32'), [16, 13, 7]), ), 3)
func_4599_call = mod.get_global_var('func_4599')
func_4600_call = mutated_mod.get_global_var('func_4600')
call_4797 = relay.TupleGetItem(func_4599_call(), 0)
call_4798 = relay.TupleGetItem(func_4600_call(), 0)
bop_4824 = relay.multiply(call_4786.astype('float64'), relay.reshape(call_4790.astype('float64'), relay.shape_of(call_4786))) # shape=(1, 7, 16)
bop_4827 = relay.multiply(call_4787.astype('float64'), relay.reshape(call_4792.astype('float64'), relay.shape_of(call_4787))) # shape=(1, 7, 16)
bop_4835 = relay.mod(call_4790.astype('float32'), relay.reshape(call_4786.astype('float32'), relay.shape_of(call_4790))) # shape=(1, 7, 16)
bop_4838 = relay.mod(call_4792.astype('float32'), relay.reshape(call_4787.astype('float32'), relay.shape_of(call_4792))) # shape=(1, 7, 16)
bop_4849 = relay.bitwise_and(call_4790.astype('uint64'), relay.reshape(bop_4835.astype('uint64'), relay.shape_of(call_4790))) # shape=(1, 7, 16)
bop_4852 = relay.bitwise_and(call_4792.astype('uint64'), relay.reshape(bop_4838.astype('uint64'), relay.shape_of(call_4792))) # shape=(1, 7, 16)
var_4870 = relay.var("var_4870", dtype = "int32", shape = (2, 728))#candidate|4870|(2, 728)|var|int32
bop_4871 = relay.right_shift(const_4791.astype('uint16'), relay.reshape(var_4870.astype('uint16'), relay.shape_of(const_4791))) # shape=(2, 728)
func_3362_call = mod.get_global_var('func_3362')
func_3364_call = mutated_mod.get_global_var('func_3364')
const_4886 = relay.const([-7.130921,2.606932,-5.756312,-6.913021,5.427855,3.859689,-2.931553,6.366805,-0.613461,8.297304,2.106723,4.063705,-8.276200,-5.938984,0.564748,2.477426,-4.189058,-0.906172,-6.188272,6.113693,-7.706678,8.703915,-2.023667,5.341474,8.137224,4.121360,4.165231,-4.923123,4.922417,-5.662735,0.874475,3.415286,-9.993902,8.670474,-2.126233,-7.870234,4.747890,9.719288,-4.813986,-4.577363,5.510547,-7.650868,3.868237,-0.480028,5.656391,1.942805,-3.340934,-4.927497,-0.385515,7.029199,-8.856503,3.056952,-1.312747,-2.578792,-3.450593,-6.046126,-2.633645,-2.637875,1.993313,4.375976,8.945567,2.026261,6.106358,-4.305571,5.936786,-6.756902,1.620698,0.076856,-1.321188,-0.410995,5.441217,-3.800329,2.871745,8.506433,-4.504362,-3.566375,7.775339,0.474793,4.127653,-4.943159,-3.721973,6.333202,-2.278375,2.852716,-0.673569,0.612312,-8.486770,3.885349,6.436018,-2.697409,7.968103,3.688468,-6.470050,2.939501,9.166391,3.246165,-0.891342,4.216198,0.861754,4.289435,3.321059,1.342043,3.946137,7.189965,7.122064,-3.584944,-6.201703,4.231367,-9.002249,6.505665,-3.787921,2.407691,6.057194,-1.535661,4.349323,-6.880032,-4.466844,-6.751609,-5.884862,-9.135141,4.364518,6.472681,2.788993,8.899088,9.121313,1.031739,6.544859,7.227262,2.744930,4.049911,3.413232,2.537751,-9.738663,8.837571,-1.051938,-5.496655,-0.775053,5.508379,5.547507,-4.724117,9.113507,-3.921469,-7.031370,5.021286,0.191349,5.545890,-7.933423,8.735205,-6.544661,-9.683638,-1.800110,5.371107,-5.886655,-8.197390,9.972850,-5.389423,-6.337795,8.283719,-1.672956,5.720356,8.532639,7.936026,5.349150,-4.278606,2.448752,-2.256656,-2.030535,9.475122,0.855627,-5.252840,-0.540866,6.172029,4.016796,2.941508,-7.120135,-1.988639,7.557270,0.584146,-5.229958,9.976272,-7.503965,4.175109,9.710854,5.181127,8.183476,9.933466,7.910487,-3.596423,7.253938,-7.494945,-6.010749,5.579284,-4.057832,1.326443,7.282608,5.447529,-6.886960,-0.808907,6.997664,-0.846861,4.628335,-8.265790,9.371830,7.857596,-4.616094,-2.935451,-0.516498,6.569615,-8.486375,0.404043,3.049170,-3.892184,-8.189204,3.937214,-5.524520,-2.408544,0.812532,-0.998375,9.963921,4.096264,-3.603808,1.217515,3.134244,6.900020,4.820098,7.095965,6.416829,-0.183984,-4.254914,0.970308,-7.325394,-0.269581,-3.613673,-5.843965,4.978843,-6.142149,4.529739,-0.163569,-8.003676,-8.660856,8.919824,-5.366159,8.201722,-7.282704,-3.415484,1.645204,9.803060,-9.930988,-2.995760,8.002213,-7.692919,0.417361,0.875816,-2.347841,-8.473427,1.355420,9.608363,-4.312933,2.149952,-8.598537,4.610311,-6.146139,-5.707151,-5.698409,2.156092,-4.064767,6.648919,1.901016,9.672954,-3.863732,-0.678046,1.974183,4.195866,6.817416,-0.634230,-2.382984,7.354605,-7.785402,3.109574,-5.119314,4.044765,-0.862400,3.111575,7.332526,-8.889083,-8.954368,-2.075824,-6.359101,8.980260,-8.426394,6.902115,7.618674,5.444165,-3.932526,9.953149,4.424360,8.809422,5.905636,2.082615,-1.579974,1.226926,-2.167389,-9.948374,5.440027,-7.360931,-1.435418,5.805940,-7.247433,2.673041,2.396534,-3.862283,1.831240,3.053456,-9.965866,-2.386076,-6.317539,9.252663,5.909342,5.174246,7.730632,-1.808806,4.680907,-4.570482,-7.823280,7.470762,-7.606475,-2.432122,5.757612,-1.518192,-7.431516,-6.678497,-9.088548,7.371924,-0.594696,2.254516,3.693155,3.332556,6.989772,-9.133032,8.656048,4.583960,7.144886,-5.614936,7.989106,-9.404653,0.719811,-4.417745,-8.512047,3.338997,-5.649946,2.793129,-7.742331,0.093387,-6.911935,5.856774,2.810012,7.171917,-6.130690,8.497058,-0.674518,0.919238,1.191083,-1.249528,1.138459,-4.716022,-5.051332,1.815832,-6.909564,-9.824907,4.774831,-8.551580,-6.640893,0.670782,4.094907,6.890265,3.177630,5.632526,-7.661620,-8.199359,6.464120,-4.998981,-8.768024,-8.889255,-5.998320,6.829831,-7.226752,-6.532567,1.228907,7.857687,-7.784326,2.765969,1.504470,-2.594935,-7.527125,-5.700640,0.598869,6.920551,-2.932059,-3.051206,-9.257929,-4.728901,-7.732445,5.595968,0.366831,-0.002767,3.457435,9.325353,6.588298,5.871037,-9.218621,5.378085,-4.768120,-8.129811,9.342972,6.634107,-2.075797,-4.679939,-1.652123,2.640283,9.860179,6.618336,2.390400,1.142854,4.348489,-2.917242,-1.406804,3.380563,-8.121513,-6.603476,1.260705,3.428614,2.060892,-5.166090,6.832356,7.721846,0.528999,-7.239464,7.327712,8.036188,-7.731506,9.499267,-2.115862,3.441001,-6.034263,-0.748979,1.618719,4.840920,0.699608,-1.667543,6.649897,3.402849,-5.592879,9.076781,-7.971621,-7.249635,-0.632436,7.376395,6.003914,6.110015,-6.179445,9.684151,0.238158,8.808616,-5.839306,-6.575429,3.047394,-7.789521,2.362379,-7.454917,6.876195,-1.786112,-2.639108,-3.560713,-3.170877,3.541651,8.711063,-3.826683,4.716865,1.264350,3.586069,-7.143061,-5.719458,-2.661127,-9.166411,5.093434,-2.951785,-0.645855,0.535049,-9.625355,-1.248056,6.731961,-0.870027,4.252659,1.999509,5.386829,-4.281267,9.758807,-2.676542,-0.866138,-0.226297,-3.177847,3.387406,1.575626,8.397586,-2.033672,5.976477,7.195862,5.388208,-9.169145,-0.656965,2.508886,6.909441,2.407937,-4.995258,-8.505776,8.990291,4.444212,3.280422,2.219331,-7.018976,5.470410,7.907494,8.079531,4.995966,7.144892,5.963898,-1.071893,-8.483576,3.907402,1.510304,7.113871,-1.686937,5.410397,-5.245848,3.112887,-9.178142,-3.378904,4.656327,-9.879020,1.292221,-5.119031,-1.649322,3.944946,-2.179926,3.566825,1.577455,-3.208133,-5.051076,0.341133,1.100569,2.433687,8.793723,1.799180,-7.427248,4.072558,-9.199965,-1.627213,-7.472692,5.169953,-8.265205,-1.305608,7.344477,-6.683707,-8.131686,-1.018864,-4.851497,1.581671,-2.891461,-9.327394,-7.860947,-2.327585,-7.714311,8.414625,5.891381,4.235189,-5.532412,9.202118,8.559656,9.911539,0.612620,1.249412,4.456376,-7.287390,6.886419,-7.068488,-8.189665,-9.857474,-1.813277,-6.651369,-7.242918,8.053993,3.597241,8.549656,-2.143459,2.226180,-2.600807,8.962585,1.600033,1.122215,6.908783,7.945192,4.788233,-9.085318,2.732398,9.694990,-5.338200,-4.971313,4.301950,-3.860903,-2.537001,3.987547,-1.679685,6.768504,-9.556348,8.622442,-0.560975,-8.921162,-6.810050,4.893750,1.027746,-0.440480,-4.285115,6.112806,-3.328282,2.090818,5.222115,9.141526,-7.063870,-4.179713,-2.131802,-5.640790,-2.629952,-2.520434,8.428081,-1.831733,-6.679266,-3.670335,-3.459327,-4.024917,-5.514869,3.227313,-9.997952,7.277070,6.597178,-9.233516,4.287612,2.976365,9.559221,1.862823,7.593814,4.506955,-0.496147,-4.013628,2.513685,5.004388,4.091591,-3.787565,0.448849,-5.010302,4.750410,-9.865297,7.747951,-9.906331,1.035308,9.587375,6.093689,-6.362378,-9.409897,-8.740593,7.617206,2.577694,5.499680,1.900918,-3.272146,1.523833,-9.009382], dtype = "float32")#candidate|4886|(676,)|const|float32
call_4885 = relay.TupleGetItem(func_3362_call(relay.reshape(const_4886.astype('float32'), [676,])), 1)
call_4887 = relay.TupleGetItem(func_3364_call(relay.reshape(const_4886.astype('float32'), [676,])), 1)
func_1075_call = mod.get_global_var('func_1075')
func_1077_call = mutated_mod.get_global_var('func_1077')
call_4888 = func_1075_call()
call_4889 = func_1075_call()
uop_4890 = relay.log(call_4885.astype('float32')) # shape=(429,)
uop_4892 = relay.log(call_4887.astype('float32')) # shape=(429,)
func_1503_call = mod.get_global_var('func_1503')
func_1505_call = mutated_mod.get_global_var('func_1505')
call_4899 = func_1503_call()
call_4900 = func_1503_call()
uop_4909 = relay.sqrt(uop_4890.astype('float64')) # shape=(429,)
uop_4911 = relay.sqrt(uop_4892.astype('float64')) # shape=(429,)
output = relay.Tuple([call_4779,call_4797,bop_4824,bop_4849,bop_4871,const_4886,call_4888,call_4899,uop_4909,])
output2 = relay.Tuple([call_4780,call_4798,bop_4827,bop_4852,bop_4871,const_4886,call_4889,call_4900,uop_4911,])
func_4912 = relay.Function([var_4870,], output)
mod['func_4912'] = func_4912
mod = relay.transform.InferType()(mod)
var_4913 = relay.var("var_4913", dtype = "int32", shape = (2, 728))#candidate|4913|(2, 728)|var|int32
output = func_4912(var_4913)
func_4914 = relay.Function([var_4913], output)
mutated_mod['func_4914'] = func_4914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3619_call = mod.get_global_var('func_3619')
func_3620_call = mutated_mod.get_global_var('func_3620')
call_5049 = relay.TupleGetItem(func_3619_call(), 0)
call_5050 = relay.TupleGetItem(func_3620_call(), 0)
func_3362_call = mod.get_global_var('func_3362')
func_3364_call = mutated_mod.get_global_var('func_3364')
var_5062 = relay.var("var_5062", dtype = "float32", shape = (676,))#candidate|5062|(676,)|var|float32
call_5061 = relay.TupleGetItem(func_3362_call(relay.reshape(var_5062.astype('float32'), [676,])), 0)
call_5063 = relay.TupleGetItem(func_3364_call(relay.reshape(var_5062.astype('float32'), [676,])), 0)
func_1523_call = mod.get_global_var('func_1523')
func_1525_call = mutated_mod.get_global_var('func_1525')
call_5064 = func_1523_call()
call_5065 = func_1523_call()
var_5068 = relay.var("var_5068", dtype = "float64", shape = (6, 7, 16))#candidate|5068|(6, 7, 16)|var|float64
bop_5069 = relay.not_equal(call_5049.astype('bool'), var_5068.astype('bool')) # shape=(6, 7, 16)
bop_5072 = relay.not_equal(call_5050.astype('bool'), var_5068.astype('bool')) # shape=(6, 7, 16)
uop_5091 = relay.tan(call_5061.astype('float32')) # shape=(16, 12, 5)
uop_5093 = relay.tan(call_5063.astype('float32')) # shape=(16, 12, 5)
const_5095 = relay.const([[[-2.186604,-2.976867,-8.488503,-0.115157,1.719067],[6.289358,-6.306440,-2.447374,-7.574074,0.010064],[-8.348939,-0.282362,3.963523,-8.669552,-0.681987],[7.842765,3.519804,6.104595,-4.227029,-6.769487],[0.818281,5.673481,0.664284,9.974167,-0.049456],[9.029577,3.601417,-6.952910,5.075200,-0.565214],[-2.284408,5.721157,3.353937,1.019641,-1.547387],[9.943722,-8.660470,0.078482,7.625402,5.533376],[8.940795,-3.162498,-9.964011,4.567299,-3.167445],[4.060872,6.937033,-0.341118,-0.420628,2.151528],[4.780512,-8.612422,7.001953,-2.234675,-4.660775],[-8.537914,-1.451242,1.732458,0.478208,0.103387]],[[-8.117350,4.275243,2.489089,5.184196,6.089530],[-1.244264,3.858891,-4.346841,8.642764,5.645255],[-1.287763,7.760071,9.281174,-0.550715,-3.212801],[-0.185195,-9.680980,-9.629726,2.206814,0.877896],[-8.113353,-3.406715,-6.081348,-4.027322,4.080092],[-5.754797,0.856291,-9.397989,-5.088198,-3.073747],[-8.197615,8.397415,-2.115783,-9.329974,4.490566],[-2.619639,-2.713992,-4.093033,-5.170723,-1.415137],[-2.654801,5.334372,-4.109866,-7.110619,-1.666483],[3.900761,9.942589,-8.045610,9.022835,-0.396530],[-5.144119,-7.109442,4.499649,-3.501916,-7.974289],[4.095347,1.181608,-9.090538,-2.699846,-3.879897]],[[2.693024,-8.776643,-3.998426,-7.544271,6.536978],[5.818022,-0.084184,-4.512039,-5.972275,9.209136],[4.396298,5.443262,7.890899,8.426611,4.025410],[0.067009,2.286577,9.238442,-7.117920,4.426048],[-3.262227,5.412777,1.779995,-8.619519,-9.638095],[-6.816983,-6.567410,-9.595495,6.753412,-1.618134],[1.463516,-2.515404,4.700444,9.866892,9.082531],[8.909332,8.588441,-7.380288,5.063295,-4.382105],[-0.968725,2.653259,-8.211208,6.272355,4.995898],[-8.567308,1.609040,-7.118912,6.293225,-1.678936],[-3.502889,-7.418648,-5.730693,-8.773120,-9.670629],[-0.934553,0.740576,3.525924,5.190674,-7.449908]],[[-1.813357,-4.177147,5.099150,-6.537878,-6.908143],[1.888871,5.915914,-8.417117,3.917239,0.489953],[7.165710,-1.500118,1.241540,-4.621222,-3.676636],[-8.025604,-0.938421,-0.092697,7.855689,-1.350817],[5.574768,-5.656584,9.581275,7.255936,-3.774512],[-3.545119,-3.827236,-7.980744,3.445224,-0.193221],[1.543269,-2.810995,4.027607,7.441629,-7.685962],[-3.212294,-1.579643,-5.717786,6.875724,-0.953982],[-6.462309,8.740273,2.240020,-6.019545,2.791063],[3.544980,0.412873,-0.893365,-3.239792,0.485484],[2.831449,6.918467,3.746597,6.833447,2.096230],[-0.142783,8.218167,-5.998559,8.390888,3.048508]],[[5.298511,-2.900802,-6.366539,-6.209696,-1.973402],[1.682877,1.352637,7.993500,-6.562038,-6.580428],[-6.295770,8.466489,-3.846701,8.498925,6.499787],[-4.900040,9.318910,6.553884,8.040708,-1.447266],[-0.013389,1.857232,-4.952605,-2.170938,-4.995257],[-5.682797,5.457044,-4.551408,6.623245,3.984546],[-0.655076,-4.865484,-5.357040,1.698348,4.755740],[-7.842661,-2.303560,9.607587,-5.902931,3.370259],[-3.305195,-8.370216,-9.767323,-2.256502,-5.925069],[-4.230796,2.364386,-6.542459,-2.518910,-0.531185],[4.034453,5.069578,-9.496432,8.007119,-5.800711],[8.617844,-6.561645,-0.649032,-2.265173,6.630189]],[[0.319768,9.198451,-6.673412,-3.486583,-7.401887],[-7.223647,1.219944,7.710538,-3.516996,4.440762],[1.235060,-1.247325,-7.821077,-1.801196,6.715985],[6.932328,8.632065,4.479686,-6.053674,4.619619],[-5.799484,-0.325834,1.584775,-7.575917,-3.244748],[2.431267,-0.540796,-8.314537,-5.861775,-3.066138],[-0.099685,-8.164031,-3.455186,3.702826,-9.398710],[3.346157,-2.437674,-7.890390,2.702413,6.897486],[-0.470603,-6.881504,-0.330597,6.816114,8.376942],[-1.860353,8.307118,-4.549247,9.612394,-9.580999],[-6.500171,-3.541850,-2.754842,-7.981936,6.628007],[6.667817,-8.572106,2.142320,-9.099506,-0.800679]],[[-7.977726,5.447955,4.609786,5.490486,6.626747],[-2.551331,-9.240421,-7.323945,-3.740259,-9.678575],[9.868601,3.721192,8.281809,-3.698525,-7.818977],[-3.520973,-7.474802,-8.322280,8.341616,-5.738007],[-1.764212,-7.211941,0.156279,5.709842,8.241013],[-5.489084,3.006487,7.963112,-6.605670,4.732502],[-8.352474,9.387205,7.599289,-4.241844,5.471485],[-0.120035,-9.586241,-8.851831,5.774832,9.134851],[-2.845374,9.440281,7.521429,-2.564771,4.160856],[-7.294740,1.021519,-4.915731,-0.808838,9.623200],[9.204376,0.031043,-5.187002,2.441899,0.393243],[1.557821,-3.013432,9.134013,9.454561,1.449707]],[[7.859043,-5.906475,6.412661,-3.946124,7.976055],[-0.588466,8.489046,-1.384956,0.774543,9.507992],[-4.469008,-3.786703,-1.832664,9.660925,-1.751532],[-8.640481,-7.024470,-4.439436,7.743972,4.834114],[5.556307,4.441221,6.886675,-9.541848,3.594769],[6.810131,-2.089219,5.667491,-9.525655,-3.053578],[5.143420,-9.859118,8.787266,-7.938201,5.851863],[-4.713593,8.705964,0.256029,7.980243,1.702693],[-0.062396,2.255407,3.811187,2.251483,2.495778],[-4.892315,-8.860437,-2.740980,8.382000,-9.170888],[9.715851,2.233521,-9.107558,4.286950,8.390219],[-4.955618,-5.106306,-1.373764,-6.528990,0.770767]],[[-8.074161,7.519481,-1.165170,-5.099065,-8.056803],[9.561770,8.402430,-9.395186,8.686226,-1.681311],[-2.899546,-7.999461,-9.319171,-0.200489,-4.314646],[-7.749711,5.080062,6.975667,2.500240,-2.338924],[-8.395593,3.141056,-0.392748,7.336743,-7.767660],[-2.966113,3.387134,4.651745,-0.782769,-1.826155],[5.089771,9.459636,-8.643958,-6.681920,-0.077001],[7.157589,-9.976289,3.727490,-3.096083,5.565386],[-5.273997,-8.374307,-6.236349,0.614511,4.756201],[-9.944259,-2.030290,-0.221170,-8.979478,-8.954385],[2.627087,-2.791544,1.798637,-5.003700,-0.621847],[-2.097731,-0.701061,-5.377342,-7.734179,7.536016]],[[-0.083537,-8.033522,3.809235,0.248676,5.880364],[-3.638469,-8.383019,7.946380,-1.537227,1.352079],[9.302038,5.089584,-3.636796,-4.612793,7.936674],[0.602592,6.805838,-1.673060,-3.466682,0.955539],[-8.403002,-3.007106,-8.232214,-1.907599,2.919196],[1.197821,8.077345,-1.734680,4.688874,-1.417442],[-5.554887,-4.111755,7.447334,-3.801192,-5.768053],[1.464531,-4.976718,0.325880,0.340420,0.066820],[-1.842393,4.177876,-1.661549,8.630359,5.335810],[-4.504891,7.749033,6.211462,-8.420026,-0.185930],[1.052630,4.959310,7.728911,-1.363253,-6.383864],[-6.415744,9.069792,-8.119176,3.923459,1.576358]],[[3.110761,8.634596,-7.694205,6.524564,-4.686487],[7.878292,0.344462,2.752504,-2.829441,-8.187104],[-9.611024,8.284926,-1.748255,2.305426,4.241257],[-4.322179,-0.653966,-1.124053,8.570635,7.943487],[8.978458,0.197374,1.450560,-4.890337,8.682120],[-8.795921,0.991120,0.881863,1.403543,0.712393],[8.488490,3.429923,1.423701,-8.785067,6.265429],[4.502871,-7.005215,-0.336450,8.840024,0.785310],[8.171766,-2.599030,9.181904,-2.051166,-6.696735],[-4.596216,-2.301495,-7.849060,8.972219,-6.690292],[-4.769461,9.904269,-3.044935,8.086729,-4.024695],[-7.583496,-0.943330,-2.480548,-6.669110,4.696215]],[[4.837248,-3.526418,9.863486,6.864814,7.245616],[-9.242778,1.435941,5.829160,2.024358,-0.824539],[2.811887,9.369788,6.004409,-8.899916,-2.500100],[0.661961,6.097915,7.100170,-8.714668,5.953500],[-2.162330,7.956332,7.063100,-7.176186,9.575627],[5.772771,0.052514,9.494597,-0.073561,2.177244],[5.495085,-0.388959,-0.886607,9.965619,0.355178],[6.182005,-7.667976,1.441706,8.871451,-5.757463],[-8.467781,3.680958,-3.724665,9.332111,-6.658032],[-5.400777,1.573566,-8.408590,-8.162273,-9.241598],[-3.023295,-2.022807,-5.286774,8.972657,8.340064],[3.693679,7.667918,0.716647,3.073975,-8.317478]],[[7.795057,6.762207,-6.705595,4.964007,2.758996],[-0.102614,8.861887,0.849327,-8.397158,3.721568],[-3.122102,-2.733370,9.427670,-8.259608,-8.510915],[2.890308,8.281186,-8.298194,-8.237818,-8.867269],[0.824776,-2.722259,3.356149,-6.700635,-5.776600],[7.841981,-6.565138,-7.981492,-8.838269,-6.619297],[0.449951,-5.345015,-3.932286,-2.795144,-1.761391],[6.024758,7.211849,-5.367420,0.297304,6.832744],[-3.131716,-7.607277,-1.516299,8.143177,2.063995],[5.291601,5.020509,7.506975,-8.358354,-3.232072],[6.331736,-8.292137,1.808816,9.333465,0.206152],[-5.363352,-7.800760,4.716612,6.890044,7.364803]],[[-8.126195,-1.791672,-6.484434,-4.826601,0.624133],[-5.897885,-5.944162,-4.432846,3.930394,-1.363933],[-4.349733,4.158327,1.541841,3.819478,8.267513],[-6.904106,6.387196,2.741784,-1.997558,-4.910082],[-0.561197,-6.113486,2.335680,1.822221,9.611333],[9.205318,-6.182353,-6.709493,4.533264,6.038636],[-7.909805,5.852574,-6.130164,1.089502,-5.856054],[-9.043533,-2.138441,6.651391,6.423106,7.319108],[-4.247086,-1.735932,3.932897,-2.367783,-3.772629],[3.987042,6.637131,-3.895071,1.141068,5.228381],[3.969020,-9.148479,-7.478622,3.824344,-9.091635],[-2.543663,-4.885373,-0.277586,9.909379,-4.049803]],[[-1.578471,-3.863271,-5.837792,7.839826,3.105337],[6.244314,-1.889401,-9.242307,5.302266,9.686289],[-7.855880,-7.441573,-7.509605,-9.599164,-8.758805],[-0.973210,-1.504550,-4.793449,2.674706,-9.188386],[-2.782327,-5.379645,-7.168419,-1.061858,-0.113135],[5.528210,8.724677,2.134853,-2.997174,-5.905330],[2.481455,7.984164,0.377313,-4.422990,1.318596],[6.777426,2.175536,3.668403,9.878270,0.127116],[7.375582,-6.255727,6.078293,-2.821228,-2.175639],[-9.787046,6.926615,7.469881,5.636578,-1.767293],[1.551043,9.501924,3.520821,-3.907202,-2.009526],[-2.301893,-6.856680,-7.343929,0.138071,-8.442961]],[[3.402005,7.846392,-3.004990,-4.611024,-6.606639],[4.197305,-1.137216,-5.395093,8.379453,-8.984825],[5.001956,1.140746,-7.253467,9.799097,-7.515440],[7.221825,-5.809865,7.145254,3.262339,-9.167446],[-7.179207,8.929133,-1.955304,-6.582314,-1.735282],[2.107856,9.604411,-8.996259,9.821338,9.615957],[4.597758,0.457054,2.750518,-3.313954,-3.919300],[4.371378,-5.925444,-6.518129,-7.722206,-0.885963],[9.839363,-1.559106,-7.723219,-7.372888,-5.720210],[-2.158687,-0.286772,6.436243,-0.046471,4.751227],[3.988735,9.036663,7.946459,-2.214454,-7.412436],[9.214168,7.426486,-0.120113,-6.169433,1.540946]]], dtype = "float32")#candidate|5095|(16, 12, 5)|const|float32
bop_5096 = relay.floor_divide(uop_5091.astype('float64'), relay.reshape(const_5095.astype('float64'), relay.shape_of(uop_5091))) # shape=(16, 12, 5)
bop_5099 = relay.floor_divide(uop_5093.astype('float64'), relay.reshape(const_5095.astype('float64'), relay.shape_of(uop_5093))) # shape=(16, 12, 5)
bop_5105 = relay.logical_xor(bop_5096.astype('uint8'), relay.reshape(uop_5091.astype('uint8'), relay.shape_of(bop_5096))) # shape=(16, 12, 5)
bop_5108 = relay.logical_xor(bop_5099.astype('uint8'), relay.reshape(uop_5093.astype('uint8'), relay.shape_of(bop_5099))) # shape=(16, 12, 5)
output = relay.Tuple([var_5062,call_5064,bop_5069,bop_5105,])
output2 = relay.Tuple([var_5062,call_5065,bop_5072,bop_5108,])
func_5112 = relay.Function([var_5062,var_5068,], output)
mod['func_5112'] = func_5112
mod = relay.transform.InferType()(mod)
var_5113 = relay.var("var_5113", dtype = "float32", shape = (676,))#candidate|5113|(676,)|var|float32
var_5114 = relay.var("var_5114", dtype = "float64", shape = (6, 7, 16))#candidate|5114|(6, 7, 16)|var|float64
output = func_5112(var_5113,var_5114,)
func_5115 = relay.Function([var_5113,var_5114,], output)
mutated_mod['func_5115'] = func_5115
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5128 = relay.var("var_5128", dtype = "int16", shape = (4, 3, 5))#candidate|5128|(4, 3, 5)|var|int16
var_5129 = relay.var("var_5129", dtype = "int16", shape = (4, 3, 5))#candidate|5129|(4, 3, 5)|var|int16
bop_5130 = relay.add(var_5128.astype('int16'), relay.reshape(var_5129.astype('int16'), relay.shape_of(var_5128))) # shape=(4, 3, 5)
func_4043_call = mod.get_global_var('func_4043')
func_4046_call = mutated_mod.get_global_var('func_4046')
var_5134 = relay.var("var_5134", dtype = "uint64", shape = (160,))#candidate|5134|(160,)|var|uint64
call_5133 = func_4043_call(relay.reshape(var_5134.astype('uint64'), [160,]))
call_5135 = func_4043_call(relay.reshape(var_5134.astype('uint64'), [160,]))
uop_5140 = relay.acosh(var_5129.astype('float64')) # shape=(4, 3, 5)
uop_5145 = relay.erf(var_5129.astype('float32')) # shape=(4, 3, 5)
output = relay.Tuple([bop_5130,call_5133,var_5134,uop_5140,uop_5145,])
output2 = relay.Tuple([bop_5130,call_5135,var_5134,uop_5140,uop_5145,])
func_5147 = relay.Function([var_5128,var_5129,var_5134,], output)
mod['func_5147'] = func_5147
mod = relay.transform.InferType()(mod)
var_5148 = relay.var("var_5148", dtype = "int16", shape = (4, 3, 5))#candidate|5148|(4, 3, 5)|var|int16
var_5149 = relay.var("var_5149", dtype = "int16", shape = (4, 3, 5))#candidate|5149|(4, 3, 5)|var|int16
var_5150 = relay.var("var_5150", dtype = "uint64", shape = (160,))#candidate|5150|(160,)|var|uint64
output = func_5147(var_5148,var_5149,var_5150,)
func_5151 = relay.Function([var_5148,var_5149,var_5150,], output)
mutated_mod['func_5151'] = func_5151
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5166 = relay.const([[[10,-3],[9,3],[1,-7],[8,-8],[-6,7],[-7,6],[8,-2],[-2,2]],[[-2,-9],[6,2],[-3,-10],[-8,-6],[-3,2],[4,3],[-8,4],[3,-2]],[[-1,-9],[2,-6],[-10,-8],[7,3],[-8,1],[2,6],[10,10],[8,-10]],[[2,7],[1,-8],[10,-9],[1,8],[-6,-3],[-2,8],[1,-5],[9,-7]],[[7,4],[-5,-10],[10,3],[-1,1],[9,-6],[3,5],[2,-2],[-7,2]],[[10,3],[10,-2],[1,4],[-8,9],[-10,-2],[-9,-6],[7,9],[-6,-8]]], dtype = "int32")#candidate|5166|(6, 8, 2)|const|int32
var_5167 = relay.var("var_5167", dtype = "int32", shape = (6, 8, 2))#candidate|5167|(6, 8, 2)|var|int32
bop_5168 = relay.subtract(const_5166.astype('int32'), relay.reshape(var_5167.astype('int32'), relay.shape_of(const_5166))) # shape=(6, 8, 2)
bop_5175 = relay.greater(bop_5168.astype('bool'), relay.reshape(var_5167.astype('bool'), relay.shape_of(bop_5168))) # shape=(6, 8, 2)
uop_5178 = relay.acosh(bop_5168.astype('float32')) # shape=(6, 8, 2)
func_2975_call = mod.get_global_var('func_2975')
func_2977_call = mutated_mod.get_global_var('func_2977')
var_5181 = relay.var("var_5181", dtype = "float32", shape = (4, 88))#candidate|5181|(4, 88)|var|float32
call_5180 = relay.TupleGetItem(func_2975_call(relay.reshape(var_5181.astype('float32'), [352,])), 1)
call_5182 = relay.TupleGetItem(func_2977_call(relay.reshape(var_5181.astype('float32'), [352,])), 1)
func_3771_call = mod.get_global_var('func_3771')
func_3773_call = mutated_mod.get_global_var('func_3773')
const_5185 = relay.const([-6.312415,-9.463181,1.277737,9.950266,3.674615,8.406694,-1.765714,-6.233028,-0.109528,-1.709480,0.505150,5.090594,-3.748623,3.213599,-4.133162,-1.113457,-4.427509,4.101295,7.745188,7.571966,-1.572717,-5.473061,-0.641168,-8.680132,-2.787635,-3.982184,7.358107,8.533380,-3.732238,9.792735,4.717880,-7.363444,8.572148,4.211258,-7.575316,0.650307,0.270546,7.195801,-3.693158,8.565107,-7.239953,1.493924,2.995729,-3.217492,7.678506,7.368476,9.161919,5.845929,6.298108,2.606155,7.410585,-1.458790,-4.336427,-9.817570,2.728527,3.384785,4.700749,2.329404,4.092572,4.790058,-6.603102,7.789985,-9.102568,-5.821447,8.889381,7.562001,-9.514144,-6.506060,7.349412,-0.198209,-5.960113,-9.413870,-3.067995,-7.559279,5.282878,-7.545747,-0.691534,8.457852,-2.746975,-4.745280,9.387509,1.561237,9.102336,-4.216080,-6.883557,7.009654,8.923883,7.778571,-8.116858,3.311204,0.074809,7.482280,-0.760638,-2.400528,-0.154092,-4.900737,-4.997191,7.474430,2.366779,-1.594429,-1.126409,-8.370247,5.374320,8.172101,-4.895579,-7.432618,5.432777,0.740325,-8.971811,-6.021124,5.506532,5.378510,-6.903383,7.448146,-7.036054,-7.173842,-8.507143,-1.247613,-0.404080,7.868077,1.250692,-6.043055,0.037759,-9.646722,5.507569,-2.612825,1.928638,-6.098750,-7.779143,-7.335168,2.496501,-4.155739,0.666445,3.440158,-6.216720,-3.951910,-1.776238,-3.412778,1.473823,-9.308169,-4.425557,6.483682,-5.390289,4.659797,3.664076,8.278082,-6.741649,-6.183703,2.808179,7.190194,-3.974871,1.380825,-8.832665,-9.469728,-9.836630,-0.619125,1.328502,-2.627116,8.428301,2.355483,5.364199,4.515708,-8.926522,-7.054189,-7.880411,2.310927,6.447835,3.843031,2.788985,5.949431,-2.249736,-7.102750,0.292781,7.327287,-6.741054,-5.366041,-4.629635,-3.201623,8.073562,-4.417682,-0.654492,2.221056,-3.782079,-1.840999,-4.362011,9.542485,7.388209,9.764569,-2.917632,-6.467765,9.061696,6.011813,-0.565765,-6.265677,-4.451387,8.026254,-0.052201,-3.562039,-9.892384,-8.777367,9.786867,0.362913,8.873772,1.801245,-4.444237,2.443509,-8.717153,4.331408,-5.598774,6.668773,-7.546682,5.367191,5.561349,1.246912,-6.286763,-3.347876,1.128115,6.988863,-3.874184,-4.312075,-3.198168,-4.990481,-8.717751,1.531077,4.875434,5.383175,-7.994156,6.055201,5.828178,2.212336,-9.540883,2.526152,5.506861,2.528958,2.290936,-5.919758,4.093804,0.616297,-1.799360,-4.246459,1.744562,7.885429,-9.696189,5.175006,3.621258,-0.128547,-1.430761,3.684385,-9.891494,-6.236368,5.482053,5.078067,1.053834,-5.694140,6.642370,-6.147869,4.537089,-9.675614,-8.509882,4.746503,-5.859639,2.400069,0.536831,1.824941,7.224311,4.909763,-5.154278,0.308438,7.528100,-2.831239,-6.028297,9.471185,-4.559337,-1.605246,9.766864,7.284053,1.313114,3.921009,3.687528,-3.273386,-3.917853,0.581312,-3.420226,-1.791732,0.454129,-5.130643,0.257322,1.799694,-6.134482,-3.503291,6.515600,8.599178,2.069916,2.773096,6.500773,7.291536,0.778096,4.443330,-9.563984,-3.951184,-2.962855,1.021980,-6.549133,9.471209,-5.426062,6.663125,3.529628,-2.209450,7.343463,-1.350372,4.360995,-8.857287,-9.468273,-0.305454,8.595364,-3.186633,-4.543152,-9.802195,-9.338513,9.818458,9.278825,-0.074664,3.622895,9.109027,-0.020548,-6.997684,-6.554977,2.675569,-9.552665,8.479439,-0.988522,7.692327,9.051400,0.778037,7.340121,1.010178,1.449230,-3.063076,-5.713195,6.567125,0.696675,3.020723,-8.135223,-0.319167,-7.821487,5.184354,-0.566364,4.621132,-2.461666,3.562036,3.093464,-3.879215,1.767754,-0.807906,5.003407,-4.865121,6.662761,-2.663885,-1.157063,-8.482801,-9.645797,3.922079,-9.948022,-6.291053,-3.968444,-8.444664,-3.521851,-7.026500,7.932375,-0.151150,7.961070,4.822942,-1.222620,-2.395494,9.952531,6.640047,-3.208257,-7.831144,-0.314203,6.623871,-8.643520,-2.994620,4.522051,-4.031550,0.512864,8.168512,-1.554993,5.576565,-0.700855,7.198691,-9.291122,6.476245,-1.062533,5.352212,-9.911952,3.223221,5.342068,-1.111916,-9.577445,9.908624,2.756825,-2.025253,-5.920433,-7.379011,-6.648570,-7.295927,-2.978944,9.058177,0.504421,7.870763,-6.352286,-9.137228,3.445445,-8.070665,-8.185560,3.492522,-4.600881,3.435517,-9.728802,2.476110,8.917842,3.225193,1.777069,-1.108446,-8.290267,-6.526003,-2.453134,-2.956510,3.349767,-0.913835,-1.469038,7.399006,3.993752,2.070013,-9.353030,-5.387132,-0.555743,-1.035648,2.309661,-3.835088,-0.890295,-5.079776,-9.271456,-1.589711,0.630535,7.819538,2.584585,-1.799404,6.986124,-5.942473,-2.622436,5.126175,-8.517825,-6.145145,9.994773,2.750469,1.594621,-4.050128,-2.008702,-8.568680,4.496932,-9.586458,-6.930064,-1.066658,-2.035105,-5.742478,8.858629,-0.309369,2.126264,8.934016,9.270468,-7.081813,-6.862511,-8.963294,-4.609094,-1.813482,-5.393021,-6.918562,5.491717,-1.657250,2.346627,-6.054168,8.635741,-5.027743,0.810815,5.533621,1.344207,-5.948684,-8.383565,-7.703904,5.847081,3.622024,9.548939,-9.569597,-4.072062,8.825764,6.498808,-5.635696,-2.973674,8.314459,3.032656,-6.720556,9.434419,-3.960484,-0.464504,-6.908337,-5.164697,7.011844,0.666408,-4.562107,9.042291,1.332616,-7.882735,0.325811,-8.878514,-9.516296,2.176936,-3.804112,6.683693,-8.181329,-1.768973,9.939330,-6.914958,-3.040269,7.511727,8.431102,-4.461047,7.488121,8.355311,3.460223,-4.145017,7.369758,1.842292,-6.877422,-7.969989,-0.315415,6.418794,5.163774,-6.910503,8.313917,1.726513,-3.587144,8.324031,-4.505513,-4.734008,-1.004599,2.566918,-2.081736,-2.367332,-2.540207,-3.366110,6.449295,-2.125805,4.584965,-3.365879,-2.633524,-4.708558,-6.764429,2.533825,-6.692788,-2.620384,-3.500412,-2.191680,-6.872733,5.172249,8.636775,1.920761,3.232411,-7.839811,1.691920,9.084577,-9.274712,-4.076621,8.423056,7.513939,-0.272730,-5.435952,6.687701,0.402121,4.981255,-4.693346,-9.382964,1.262209,-9.363906,1.728931,6.699166,2.721031,-0.423594,-3.345648,6.397805,9.624569,0.821693,-5.665478,-4.109392,3.522949,-2.077015,-7.971870,4.570011,-8.243690,4.259570,2.452790,-3.573282,-0.373782,1.923896,-2.189013,-8.398277,-3.403343,-9.757779,1.996276,-3.833728,-9.482190,-7.923480,-1.216784,7.102718,2.869091,-4.467134,6.942529,-9.617701,7.142134,-8.824704,-7.154403,1.648633,-0.423235,-6.603494,-3.657965,-6.925097,8.863991,6.516226,8.348494,2.599539,-3.929340,3.770626,-1.061022,9.936442,1.732017,-1.300069,1.569558,-3.431629,6.068629,6.526697,-7.119624,-7.787107,-9.106272,2.410784,-4.242077,7.920496,-1.311958,-3.740597,-5.597615,-4.226988,1.646111,1.151649,-5.955066,2.699733,-7.543321,7.718076,-8.046395,4.250981,5.396206,-8.550402,1.049324,-3.250673,6.674668,-2.262801,1.090812,7.352747,3.428615,2.087293,2.948120,8.698807,2.488126,-0.058820,8.546336,-8.850092,-0.676849,-0.654047,-3.463524,7.236821,-5.676003,3.773931,-3.049915,-9.096717,-0.213991,1.816310,-0.370950,7.121720,2.688674,-0.792290,3.465478,8.527527,9.554582,6.610911,2.967272,5.122811,8.615176,1.198963,-6.423695,3.461416,9.062078,-7.902327,-0.673316,4.695519,1.297312,-2.498527,-9.462760,-2.088253,2.713640,-5.599676,-7.579342,-1.143212,-0.597579,0.002995,-7.654224,2.219514,6.877014,7.477763,-3.077852,6.658922,-2.269212,-3.455232,8.763500,6.150980,2.401254,4.667360,9.348090,3.423299,7.959668,-7.069887,2.661521,4.616724,0.232588,-6.408958,7.130626,3.654731,9.267154,4.372401,-8.933650,-1.373535,-0.009005,3.400355,7.926818,9.729710,5.995250,-0.726698,-7.344629,5.199866,1.786661,6.176549,8.985664,-0.606505,-8.714620,-9.374911,-4.272024,-0.650955,-1.308059,9.625074,-8.259168,5.815265,-9.554291,8.527757,6.417616,1.596046,-2.119314,-5.573003,2.392409,9.362941,-2.959057,8.074406,-5.867270,1.527860,2.124144,-8.607455,4.775358,-6.551276,-7.680556,-4.107748,-9.305985,-6.968371,-2.596777,6.301796,3.344394,-9.951940,-7.799140,0.001682,8.902060,0.373407,6.906200,5.023267,3.324419,-6.749078,3.031358,-4.008178,-7.372068,-4.957877,5.716345,0.701836,-8.554241,-4.005674,2.902234,9.720210,-4.320599,3.713339,5.504004,-6.504333,-7.677526,-8.747113,-4.802588,-1.519418,4.534188,2.113844,-2.092767,6.818814,-6.780272,2.866597,9.722315,2.220049,0.549234,5.545480,3.013282,-7.482916,0.590676,2.643675,5.699701,-2.336689,-9.055502,7.955265,-6.855214,-8.325519,-3.612182,-8.276913,-4.477214,6.172575,7.048766,-0.979187,-1.365033,-9.434174,4.294659,7.144735,2.652839,4.568392,-2.043848,-5.206396,-8.554129,9.459379,-0.854724,-5.131265,2.770521,6.770152,6.002294,0.555081,-8.988655,5.681012,6.163336,-6.495825,-1.186223,9.695214,-4.505100,-8.429469,-3.595824,7.176589,7.991798,7.778013,5.964208,8.749267,5.757250,-3.950722,3.226667,0.525542,8.241318,3.272361,-8.893092,-4.445162,5.052537,9.256968,-0.130255,-4.780378,-5.871938,5.337842,-7.035682,-8.332997,1.612244,6.991322,-5.409110,-9.175037,-8.353010,-4.394994,-7.746559,3.518162,9.311112,7.882888,2.987468,2.198918,7.772239,8.692297,-8.432715,7.978182,9.696420,-5.772163,-5.037572,1.637939,-2.876127,9.838770,-3.272274,-9.874345,9.918954,7.638180,-6.338445,-3.379299,1.627573,3.481549,-4.535561,-3.054441,-8.601979,1.160336,7.445163,7.519123,-5.982467,-8.915289,-3.908378,-5.551174,-9.629833,-7.918487,5.383906,-2.588994,2.368735,-6.709085,8.473068,2.416301,8.091042,-7.135156,1.757163,-5.040332,-1.370711,-4.491883,-1.270647,-2.780183,-1.787234,7.387395,0.678392,4.769517,9.931654,-8.830655,-1.299441,-1.112215,3.325380,-3.843623,8.108234,-5.418613,5.761384,-6.608043,-7.777247,-5.137679,6.873334,-7.241267,3.267954,4.992868,6.054824,6.134191,5.914079,4.115028], dtype = "float32")#candidate|5185|(960,)|const|float32
call_5184 = relay.TupleGetItem(func_3771_call(relay.reshape(const_5185.astype('float32'), [16, 12, 5])), 0)
call_5186 = relay.TupleGetItem(func_3773_call(relay.reshape(const_5185.astype('float32'), [16, 12, 5])), 0)
output = relay.Tuple([bop_5175,uop_5178,call_5180,var_5181,call_5184,const_5185,])
output2 = relay.Tuple([bop_5175,uop_5178,call_5182,var_5181,call_5186,const_5185,])
func_5198 = relay.Function([var_5167,var_5181,], output)
mod['func_5198'] = func_5198
mod = relay.transform.InferType()(mod)
mutated_mod['func_5198'] = func_5198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5198_call = mutated_mod.get_global_var('func_5198')
var_5200 = relay.var("var_5200", dtype = "int32", shape = (6, 8, 2))#candidate|5200|(6, 8, 2)|var|int32
var_5201 = relay.var("var_5201", dtype = "float32", shape = (4, 88))#candidate|5201|(4, 88)|var|float32
call_5199 = func_5198_call(var_5200,var_5201,)
output = call_5199
func_5202 = relay.Function([var_5200,var_5201,], output)
mutated_mod['func_5202'] = func_5202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3606_call = mod.get_global_var('func_3606')
func_3607_call = mutated_mod.get_global_var('func_3607')
call_5204 = relay.TupleGetItem(func_3606_call(), 0)
call_5205 = relay.TupleGetItem(func_3607_call(), 0)
uop_5206 = relay.erf(call_5204.astype('float64')) # shape=(16, 12, 5)
uop_5208 = relay.erf(call_5205.astype('float64')) # shape=(16, 12, 5)
bop_5228 = relay.floor_mod(uop_5206.astype('float32'), relay.reshape(call_5204.astype('float32'), relay.shape_of(uop_5206))) # shape=(16, 12, 5)
bop_5231 = relay.floor_mod(uop_5208.astype('float32'), relay.reshape(call_5205.astype('float32'), relay.shape_of(uop_5208))) # shape=(16, 12, 5)
var_5237 = relay.var("var_5237", dtype = "float64", shape = (16, 12, 5))#candidate|5237|(16, 12, 5)|var|float64
bop_5238 = relay.add(uop_5206.astype('int32'), relay.reshape(var_5237.astype('int32'), relay.shape_of(uop_5206))) # shape=(16, 12, 5)
bop_5241 = relay.add(uop_5208.astype('int32'), relay.reshape(var_5237.astype('int32'), relay.shape_of(uop_5208))) # shape=(16, 12, 5)
func_4912_call = mod.get_global_var('func_4912')
func_4914_call = mutated_mod.get_global_var('func_4914')
var_5252 = relay.var("var_5252", dtype = "int32", shape = (56, 26))#candidate|5252|(56, 26)|var|int32
call_5251 = relay.TupleGetItem(func_4912_call(relay.reshape(var_5252.astype('int32'), [2, 728])), 4)
call_5253 = relay.TupleGetItem(func_4914_call(relay.reshape(var_5252.astype('int32'), [2, 728])), 4)
output = relay.Tuple([bop_5228,bop_5238,call_5251,var_5252,])
output2 = relay.Tuple([bop_5231,bop_5241,call_5253,var_5252,])
func_5262 = relay.Function([var_5237,var_5252,], output)
mod['func_5262'] = func_5262
mod = relay.transform.InferType()(mod)
var_5263 = relay.var("var_5263", dtype = "float64", shape = (16, 12, 5))#candidate|5263|(16, 12, 5)|var|float64
var_5264 = relay.var("var_5264", dtype = "int32", shape = (56, 26))#candidate|5264|(56, 26)|var|int32
output = func_5262(var_5263,var_5264,)
func_5265 = relay.Function([var_5263,var_5264,], output)
mutated_mod['func_5265'] = func_5265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2439_call = mod.get_global_var('func_2439')
func_2440_call = mutated_mod.get_global_var('func_2440')
call_5375 = relay.TupleGetItem(func_2439_call(), 0)
call_5376 = relay.TupleGetItem(func_2440_call(), 0)
uop_5393 = relay.erf(call_5375.astype('float64')) # shape=(60,)
uop_5395 = relay.erf(call_5376.astype('float64')) # shape=(60,)
func_4599_call = mod.get_global_var('func_4599')
func_4600_call = mutated_mod.get_global_var('func_4600')
call_5403 = relay.TupleGetItem(func_4599_call(), 0)
call_5404 = relay.TupleGetItem(func_4600_call(), 0)
output = relay.Tuple([uop_5393,call_5403,])
output2 = relay.Tuple([uop_5395,call_5404,])
func_5408 = relay.Function([], output)
mod['func_5408'] = func_5408
mod = relay.transform.InferType()(mod)
output = func_5408()
func_5409 = relay.Function([], output)
mutated_mod['func_5409'] = func_5409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4599_call = mod.get_global_var('func_4599')
func_4600_call = mutated_mod.get_global_var('func_4600')
call_5441 = relay.TupleGetItem(func_4599_call(), 0)
call_5442 = relay.TupleGetItem(func_4600_call(), 0)
func_3050_call = mod.get_global_var('func_3050')
func_3052_call = mutated_mod.get_global_var('func_3052')
const_5455 = relay.const([-9,-3,9,-9,-10,2,-6,-9,-8,3,-7,-2,-6,-6,-10,-8,9,6,-3,-8,1,-8,-3,-2,-3,8,1,-2,9,-5,6,-10,9,4,2,-4,6,-9,-8,1,-5,3,9,2,3,6,5,6,-3,-5,-4,7,-10,10,-9,-3,-10,-2,-2,-6,4,-4,-10,-4,-1,-8,-7,-5,-3,-8,6,9,-8,6,5,-4,-5,-1,-7,8,3,2,-2,10,-4,8,-10,7,-9,-7,-4,-7,-7,6,3,-3,1,-8,-4,6,7,-1,4,6,-10,10,-3,-5,-5,-8,4,-5,-7,-7,1,1,9,6,10,7,-4,6,-5,-2,1,-9,1,1,6,1,1,-5,3,-4,-3,3,-9,7,-9,4,-10,8,-6,-9,4,10,-3,-6,6,9,2,-7,10,-6,-2,2,3,3,-6,-2,4,8,6,-4,-5,-2,-5,-1,-2,6,9,-7,-8,4,5,-6,9,-8,9,9,-3,10,-1,-2,8,-8,8,1,-8,-1,2,-3,3,-6,-3,6,-8,-3,7,-4,5,-4,-9,-8,10,9,-7,3,-6,-2,-5,-5,7,4,5,-1,-1,-3,1,-5,-1,3,9,-9,6,-3,10,-6,8,-10,-1,7,-7,-10,4,-9,4,-2,-7,-9,2,6,2,8,-5,6,1,-5,4,7,5,-10,10,-3,4,-2,3,-10,-9,6,-1,9,4,2,-1,3,-7,-4,-8,5,-8,10,-4,-6,-1,8,-5,-3,1,8,-4,-8,5,-9,-9,-6,-1,8,-7,10,-9,7,3,6,5,6,4,-4,7,3,-8,-3,-5,4,-7,9,1,3,-8,-10,2,6,-1,6,-2,4,-10,-8,-7,-9,7,2,8,3,-6,-10,-10,-6,-5,-9,-3,-8,9,2,-8,-2,-2,2,2,5,10,-6,-4,-1,7,9,-2,-5,-10,-7,-9,-5,5,-1,5,-7,-5,-7,-5,9,8,-4,-4,-1,7,5,7,8,-9,1,9,1,10,3,6,-9,-2,7,3,10,-6,-7,5,6,-6,-10,-6,-9,8,-4,-5,-3,8,-1,-5,-1,6,-5,3,6,10,-4,-4,-5,-2,1,5,-4,-1,4,-6,1,2,4,9,5,-4,8,-10,2,-3,1,6,-1,-10,5,9,-9,-1,-6,-1,-10,8,2,-2,-1,-9,10,-8,2,-5,6,-6,7,-6,-8,4,1,-7,-1,1,-3,-4,6,4,-2,9,-7,2,2,6,6,-9,3,2,-6,-8,3,-2,8,9,8,-7,-2,-8,-5,-4,4,10,3,5,-4,8,9,-10,-9,6,-8,-10,-9,5,-3,-7,-6,8,8,9,-8,-1,9,5,-10,-5,1,-1,4,-6,-6,-7,7,-4,-9,-7,9,6,-1,8,-2,-2,-8,3,10,10,10,10,3,4,-6,10,1,5,-9,-7,-6,1,-1,-6,2,7,-5,1,1,-1,6,-2,9,1,10,8,7,10,4,1,5,-9,-8,-8,6,6,1,9,7,8,9,5,-5,-6,-2,6,6,8,6,3,-7,3,8,10,3,-3,5,-8,5,-1,2,4,3,-4,-2,-2,-5,-9,-9,8,-8,-6,-1,3,-10,-2,-2,-2,10,5,-10,-1,3,10,10,8,9,10,8,-5,-8,3,-5,4,-9,-9,7,6,1,-6,3,6,-7,3,10,6,-5,7,-1,7,-3,1,-6,1,-2,-8,-10,9,1,-5,-2,-8,-1,8,9,4,-2,1,9,-7,9,-9,2,-8,-2,3,-5,10,9,8,5,-7,4,-7,9,7,1,-9,-4,5,2,-9,-10,-5,-8,4,-4,10,-8,2,-3,5,4,7,3,-5,10,5,4,-1,-10,6,8,3,-3,3,-5,7,4,-9,-6,5,-10,-9,8,-7,-5,-4,8,-10,4,4,4,9,7,-9,4,-2,2,-9,1,3,-8,10,-4,-7,-4,8,-4,7,4,-4,-10,3,8,-4,-9,-7,-4,4,-7,-8,2,10,10,-7,5,-5,10,7,-1,8,-8,8,2,-9,3,-2,3,2,1,-10,-5,-1,4,-4,9,-4,9,-10,-3,9,-8,2,-5,5,-6,-4,1,-5,-3,9,-2,-10,6,-1,-9,-7,-5,8,-7,-6,7,5,5,-2,-10,-10,-5,-5,-10,-2,-9,8,9,-4,7,9,-1,-2,4,-5,-5,9,7,3,-2,-10,3,7,-4,-10,2,-6,4,1,2,-6,-3,8,-1,-9,3,4,-7,-10,1,-3,9,-7,-9,-3,-6,-9,6,-1,8,7,-1,-9,-1,9,-9,6,4,-1,4,6,-4,3,4,-6,3,-4,-6,3,10,-1,8,6,-5,-7,-4,-10,-9,8,-6,4,8,6,-8,3,-4,-10,-4,-4,-5,7,-3,-10,2,6,4,9,-9,-8,-5,7,-5,-2,3,-7,7,10,3,-4,9,4,1,5,-10,7,4,-7,-2,8,-4,-8,9,3,-7,8,9,9,-5,2,-9,-3,4,2,10,5,-2,-7,10,-4,8,-5,4,-1,-2,4,-1,-4,8,4,5,2,-2,-10,-10,9,4,7,10,7,-10,-3,10,9,-5,-6,2,-8,6,5,2,-3,10,4,-9,-3,-4,3,8,-3,-5,-3,-6,9,1,-9,-2,9,4,3,6,6,6,5,-1,9,9,1,5,9,-8,6,1,-1,9,-10,-3,5,6,-5,10,1,6,-5,5,-4,2,-2,-5,10,8,9,6,1,3,7,8,1,1,4,1,9,-7,-6,4,6,-6,3,8,4,-10,7,2,-1,-5,8,-2,-7,8,1,1,-1,-4,-9,-8,6,-7,-5,10,-1,-2,10,8,5,3,5,5,1,10,-6,6,-8,4,1,1,2,2,9,1,3,10,-10,-6,8,2,6,-5,-10,-8,-6,4,6,10,-6,-1,-5,-7,-8,5,-10,-10,-6,1,-6,8,1,10,9,-5,8,-4,-7,-9,5,-2,2,3,7,-5,-4,6,8,5,3,2,3,6,8,-4,-9,10,-8,-1,-5,-9,3,6,-1,-9,-10,8,7,-3,9,-8,4,2,-8,-7,1,-6,3,-8,-3,-9,-5,6,2,7,-7,-10,2,2,-6,5,-9,4,2,-6,-8,-10,3,7,5,7,-10,4,-2,3,7,7,-10,-8,2,9,-1,5,7,1,3,-6,8,4,-6,8,-7,-9,-8,9,-3,2,-9,9,-6,-10,10,-3,-5,10,5,7,5,-7,5,6,6,1,4,3,-10,-2,-8,1,-5,-9,9,2,-3,8,7,-3,2,10,4,8,8,-6,-7,4,-8,-2,-8,-10,3,9,9,-5,-6,7,-10,-5,6,-5,-6,5,-1,-10,1,-9,7,-6,-8,7,8,5,10,-6,-1,1,1,3,5,10,3,-4,-5,-7,3,-10,-2,9,-7,10,10,-5,-9,3,-2,-4,2,5,8,4,-8,2,-9,1,10,4,-5,10,-7,-2,6,2,-3,7,9,-3,-6,-6,-10,3,-10,-7,-5,-3,-10,9,-10,-5,-10,-4,-4,9,-4,6,-3,3,5,-2,-8,3,7,-7,-5,-10,5,-7,3,-10,10,-2,-5,10,-6,2,-5,-4,-7,1,-3,10,-5,6,2,6,2,-8,-2,6,-9,3,-3,8,10,-5,-10,-1,-3,-4,5,-8,-7,-3,-3,8,7,-5,8,2,3,-1,2,10,8,-10,-4,-9,5,2,1,1,9,10,-1,5,2,7,-7,9,10,8,10,-7,-9,4,-8,8,2,7,2,7,10,-8,-10,-2,-6,6,-10,-2,1,7,-2,-9,4,-8,-9,-8,1,-6,3,-1,2,7,-10,1,7,-3,4,5,-7,4,-10,-5,-10,-1,-10,-4,-10,6,-9,3,6,7,7,8], dtype = "int32")#candidate|5455|(1456,)|const|int32
call_5454 = relay.TupleGetItem(func_3050_call(relay.reshape(const_5455.astype('int32'), [1456,])), 2)
call_5456 = relay.TupleGetItem(func_3052_call(relay.reshape(const_5455.astype('int32'), [1456,])), 2)
output = relay.Tuple([call_5441,call_5454,const_5455,])
output2 = relay.Tuple([call_5442,call_5456,const_5455,])
func_5474 = relay.Function([], output)
mod['func_5474'] = func_5474
mod = relay.transform.InferType()(mod)
output = func_5474()
func_5475 = relay.Function([], output)
mutated_mod['func_5475'] = func_5475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3318_call = mod.get_global_var('func_3318')
func_3320_call = mutated_mod.get_global_var('func_3320')
call_5515 = relay.TupleGetItem(func_3318_call(), 0)
call_5516 = relay.TupleGetItem(func_3320_call(), 0)
const_5531 = relay.const([[[False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,False],[False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False],[False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False],[True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True],[False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True],[False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,False],[False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False],[False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False],[True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True],[True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,False],[False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True],[False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False],[True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True],[False,False,False,False,True,False,False,True,False,False,False,False,False,True,False,False],[True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False]],[[True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False],[False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True],[True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False],[True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,False],[True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False],[True,True,True,True,True,True,True,True,False,True,False,True,False,True,True,True],[True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True],[False,False,False,True,True,True,False,True,False,False,False,False,True,True,True,False],[True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,True],[False,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False],[True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False],[False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True],[True,True,False,True,False,True,True,True,True,True,False,True,False,True,True,False],[False,False,False,True,True,False,False,False,True,True,True,True,True,False,False,False],[True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False]],[[True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False],[True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False],[True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False],[False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False],[False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False],[False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False],[False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False],[True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,False],[True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False],[False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True],[False,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True],[True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False],[True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True],[True,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True],[True,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False]],[[True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True],[False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True],[False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True],[True,False,True,False,False,False,False,True,True,True,False,True,True,False,False,True],[True,True,False,True,False,False,True,True,False,True,False,False,False,False,True,True],[False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False],[True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False],[True,True,True,True,True,True,True,False,False,True,False,True,False,True,True,True],[True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False],[False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,False],[True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True],[True,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False],[False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False],[False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,False],[False,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True]],[[False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False],[True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True],[True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True],[True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False],[True,True,False,False,True,False,True,True,True,False,True,True,True,True,False,False],[False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False],[True,False,False,False,True,True,True,False,True,False,True,False,True,True,True,True],[False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False],[True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True],[True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True],[True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True],[True,True,True,True,False,True,True,True,True,True,False,True,True,False,False,True],[True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True],[True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False],[True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True]],[[False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False],[False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False],[False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False],[False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True],[False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True],[False,False,True,True,True,True,True,False,False,True,False,True,True,True,True,False],[False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,True],[False,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False],[False,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False],[True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,True],[True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True],[True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,True],[True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True],[False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,False],[False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False]],[[True,False,True,True,False,False,False,True,False,True,False,True,True,True,True,True],[True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,True],[True,False,False,True,True,False,True,True,True,True,False,False,False,True,True,True],[False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False],[False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False],[False,False,True,False,False,False,False,False,True,False,False,False,False,True,False,True],[False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,False],[False,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True],[True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True],[False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True],[True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,True],[True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False],[True,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True],[False,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False],[False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False]],[[True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False],[True,True,True,True,False,True,False,True,True,True,True,True,False,True,False,True],[False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False],[True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True],[True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True],[True,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True],[False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,True],[False,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False],[False,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False],[True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,False],[False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True],[False,False,True,False,False,False,False,False,True,True,True,True,False,True,False,False],[False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,True],[True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False],[True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False]],[[False,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True],[False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True],[False,False,False,False,True,False,True,True,True,True,False,True,False,True,True,False],[False,False,False,False,False,False,True,False,True,True,True,True,True,False,False,True],[False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True],[False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False],[True,True,False,False,True,True,False,False,True,False,True,True,False,False,False,True],[True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True],[False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True],[True,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True],[False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True],[False,True,False,False,True,True,True,False,True,True,False,False,False,True,True,False],[False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False],[False,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False],[False,False,False,True,True,True,False,False,False,True,False,True,False,False,True,False]],[[False,True,True,True,False,False,False,False,False,False,False,False,True,False,True,True],[True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True],[True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False],[False,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True],[False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False],[True,False,False,False,True,True,True,False,False,False,True,True,True,False,False,True],[False,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False],[True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True],[False,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False],[True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False],[True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False],[False,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True],[False,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True],[False,True,False,False,False,False,True,True,True,True,False,True,True,True,True,True],[True,False,True,True,False,True,True,False,True,False,False,False,False,False,True,False]],[[True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False],[True,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True],[True,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False],[True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False],[False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False],[False,False,True,False,True,True,True,True,True,True,False,False,False,True,False,False],[True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,False],[False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,False],[False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,False],[False,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True],[False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True],[True,True,True,True,True,True,True,False,True,True,True,False,True,True,True,False],[True,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False],[True,False,False,False,False,True,False,True,True,False,True,False,True,False,False,False],[True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,False]],[[True,True,True,True,True,True,False,False,True,True,False,False,False,True,False,True],[False,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True],[False,False,True,True,False,True,True,True,True,False,False,True,True,False,False,True],[True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True],[True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True],[False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,True],[True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,True],[False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True],[True,True,True,False,True,False,False,False,True,False,False,False,False,False,True,False],[False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True],[False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False],[True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False],[False,True,True,True,True,True,False,True,True,True,False,True,True,True,True,False],[True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True],[True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False]],[[False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,False],[True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False],[True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False],[True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True],[True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,True],[False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True],[False,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True],[False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,False],[True,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True],[False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True],[False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True],[False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False],[True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False],[True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True],[False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True]],[[True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True],[True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False],[True,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False],[True,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False],[True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False],[True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,False],[False,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False],[True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False],[True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False],[True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False],[False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False],[False,True,False,True,True,True,False,True,False,False,False,True,True,False,True,True],[True,True,True,True,False,True,True,True,False,True,True,True,True,True,False,False],[True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False],[False,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False]],[[True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True],[True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True],[False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False],[True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False],[True,True,False,True,True,False,False,True,True,True,False,False,False,True,False,True],[False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True],[False,True,True,True,True,True,False,True,False,True,True,False,False,True,True,False],[True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False],[True,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True],[False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True],[False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False],[False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False],[True,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False],[False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False],[True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True]]], dtype = "bool")#candidate|5531|(15, 15, 16)|const|bool
bop_5532 = relay.floor_mod(call_5515.astype('float64'), relay.reshape(const_5531.astype('float64'), relay.shape_of(call_5515))) # shape=(15, 15, 16)
bop_5535 = relay.floor_mod(call_5516.astype('float64'), relay.reshape(const_5531.astype('float64'), relay.shape_of(call_5516))) # shape=(15, 15, 16)
func_5198_call = mod.get_global_var('func_5198')
func_5202_call = mutated_mod.get_global_var('func_5202')
var_5545 = relay.var("var_5545", dtype = "int32", shape = (16, 6))#candidate|5545|(16, 6)|var|int32
const_5546 = relay.const([-7.092607,-7.543800,6.172037,-5.774757,8.521216,-7.605978,-9.153644,4.075642,1.873479,1.310965,1.927031,-5.970117,0.261433,-4.116159,-3.397803,-5.066008,2.387373,-3.438938,0.812496,-3.250024,1.264394,0.336905,-0.601090,7.865144,0.013299,-0.177386,-3.443317,-8.576352,2.539534,-4.515907,-3.062213,2.935532,-9.054440,-8.336532,-5.308176,-9.436205,2.570968,6.005279,4.645146,1.339036,-7.084525,1.648962,8.118431,-2.072845,-3.640202,-3.643041,0.315810,-6.946101,5.184442,0.650908,-4.879397,0.733091,0.827513,5.869734,1.195454,5.183911,0.435486,4.579166,-0.581555,3.152039,-2.498129,-6.729809,4.198300,5.558501,9.904926,4.549281,8.131402,-0.884281,1.183911,1.262791,-6.742698,-6.021285,5.970703,-7.055896,3.266134,-4.367356,6.740753,4.386308,6.039412,5.595402,0.424590,-6.615107,-2.932997,5.488906,9.942892,-2.833590,3.609734,4.564769,-6.431824,7.147766,6.284803,-8.724139,-8.306158,-0.864769,-1.715049,-3.947845,-5.599157,-1.395086,7.252458,-4.667721,-9.864535,9.444261,-2.570406,-6.806598,-2.162682,-8.997529,3.624749,8.514875,6.023296,-5.615838,1.789748,8.499277,6.874748,-2.873879,-6.090286,3.071801,-6.356494,-8.201888,7.655609,3.326125,-6.801745,-6.240842,-8.730159,5.860794,7.471773,-9.612921,9.687569,-9.012652,2.545271,2.252438,9.557184,5.913007,0.984063,-9.835511,-0.652185,7.991547,-1.877388,7.322626,9.326282,-6.636638,-3.655953,0.517213,-4.635260,-1.467148,7.427008,0.407750,5.189575,-5.887457,5.962130,9.257875,-2.247303,-9.777520,-6.141316,-3.822630,3.246629,-7.108649,9.710867,5.872743,2.952805,6.506088,2.629004,-8.726176,4.134694,-7.611101,7.941475,4.916605,-5.898760,-7.104140,2.729724,-1.539446,4.377296,-7.737794,-1.414900,4.452182,3.148562,-9.077749,9.095809,6.932786,1.234862,7.904059,-8.109572,8.073383,8.330244,0.168850,-2.459063,1.385046,8.705025,-0.786064,3.503950,6.849213,-9.217080,6.177355,-2.738535,0.350040,-5.876104,8.678333,8.465682,0.861360,-6.433319,8.995706,-2.079323,4.290228,-3.961887,-2.250874,7.651258,-3.417904,5.539796,7.004463,5.359185,-4.150308,-9.897453,-5.650625,-3.993446,-9.850370,-5.256242,3.319562,-7.545041,-1.768234,-3.023153,-2.867121,3.226493,0.180189,-8.406200,-8.564300,3.801668,-0.982255,-4.055451,8.711574,-2.028967,-2.158025,6.607184,-0.941112,-3.795357,-2.666168,3.876728,-4.463952,-6.246500,0.574540,-4.319187,-3.257664,-4.028704,4.447701,4.641569,7.181249,-0.140311,-8.171910,6.292876,1.000746,-7.432239,-8.210429,-7.796231,-7.725198,8.797866,-4.275981,3.215672,6.263466,4.283448,7.824727,-3.982693,-1.317305,-8.469081,-2.420697,8.561386,9.994021,-8.887767,1.386122,-6.270523,9.931072,-5.984336,1.041848,-3.227310,6.801778,-0.972834,-0.718816,-4.885129,3.321134,8.290415,-0.553839,-2.904272,-9.523610,-9.961336,5.988566,0.346413,-7.166858,-2.360421,-2.601325,-6.752924,-5.185161,-1.741364,6.174955,-1.726419,2.823796,5.362011,-5.203765,1.751631,-8.297589,1.181658,-2.236332,-5.089859,-4.665529,-3.462191,1.093742,-3.140127,8.100320,-6.830130,2.296473,-2.391577,-2.351515,3.177542,5.865124,-9.556843,-3.182082,6.192445,-3.928246,7.943763,9.679459,1.259105,-0.882789,-5.313041,-7.434531,0.561213,5.011247,-2.883383,5.446211,9.221013,-9.744033,-6.151725,7.668423,3.150056,8.852827,-5.738511,0.975255,4.177428,5.147079,5.800719,-0.225323,-7.051325,-4.437576,4.235534,-3.447811,-0.169089,-6.900383,4.948184,0.550970,-0.402402,5.567987,7.849917,-6.063105,-5.844598,-5.292431,-3.924725,-1.953084], dtype = "float32")#candidate|5546|(352,)|const|float32
call_5544 = relay.TupleGetItem(func_5198_call(relay.reshape(var_5545.astype('int32'), [6, 8, 2]), relay.reshape(const_5546.astype('float32'), [4, 88]), ), 0)
call_5547 = relay.TupleGetItem(func_5202_call(relay.reshape(var_5545.astype('int32'), [6, 8, 2]), relay.reshape(const_5546.astype('float32'), [4, 88]), ), 0)
func_3294_call = mod.get_global_var('func_3294')
func_3295_call = mutated_mod.get_global_var('func_3295')
call_5551 = func_3294_call()
call_5552 = func_3294_call()
output = relay.Tuple([bop_5532,call_5544,var_5545,const_5546,call_5551,])
output2 = relay.Tuple([bop_5535,call_5547,var_5545,const_5546,call_5552,])
func_5555 = relay.Function([var_5545,], output)
mod['func_5555'] = func_5555
mod = relay.transform.InferType()(mod)
var_5556 = relay.var("var_5556", dtype = "int32", shape = (16, 6))#candidate|5556|(16, 6)|var|int32
output = func_5555(var_5556)
func_5557 = relay.Function([var_5556], output)
mutated_mod['func_5557'] = func_5557
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5562 = relay.var("var_5562", dtype = "float64", shape = (9, 4, 1))#candidate|5562|(9, 4, 1)|var|float64
uop_5563 = relay.log10(var_5562.astype('float64')) # shape=(9, 4, 1)
output = uop_5563
output2 = uop_5563
F = relay.Function([var_5562,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5562,], output2)
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
