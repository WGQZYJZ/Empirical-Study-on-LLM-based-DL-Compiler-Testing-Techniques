import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_397 = relay.var("var_397", dtype = "uint64", shape = (13, 7, 5))#candidate|397|(13, 7, 5)|var|uint64
var_398 = relay.var("var_398", dtype = "uint64", shape = (13, 7, 5))#candidate|398|(13, 7, 5)|var|uint64
bop_399 = relay.multiply(var_397.astype('uint64'), relay.reshape(var_398.astype('uint64'), relay.shape_of(var_397))) # shape=(13, 7, 5)
output = relay.Tuple([bop_399,])
output2 = relay.Tuple([bop_399,])
func_424 = relay.Function([var_397,var_398,], output)
mod['func_424'] = func_424
mod = relay.transform.InferType()(mod)
mutated_mod['func_424'] = func_424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_424_call = mutated_mod.get_global_var('func_424')
var_426 = relay.var("var_426", dtype = "uint64", shape = (13, 7, 5))#candidate|426|(13, 7, 5)|var|uint64
var_427 = relay.var("var_427", dtype = "uint64", shape = (13, 7, 5))#candidate|427|(13, 7, 5)|var|uint64
call_425 = func_424_call(var_426,var_427,)
output = call_425
func_428 = relay.Function([var_426,var_427,], output)
mutated_mod['func_428'] = func_428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_485 = relay.var("var_485", dtype = "float32", shape = (4, 5, 5))#candidate|485|(4, 5, 5)|var|float32
var_486 = relay.var("var_486", dtype = "float32", shape = (4, 5, 5))#candidate|486|(4, 5, 5)|var|float32
bop_487 = relay.floor_mod(var_485.astype('float32'), relay.reshape(var_486.astype('float32'), relay.shape_of(var_485))) # shape=(4, 5, 5)
bop_492 = relay.greater_equal(var_485.astype('bool'), relay.reshape(bop_487.astype('bool'), relay.shape_of(var_485))) # shape=(4, 5, 5)
uop_500 = relay.exp(bop_492.astype('float32')) # shape=(4, 5, 5)
bop_508 = relay.logical_or(uop_500.astype('bool'), relay.reshape(bop_492.astype('bool'), relay.shape_of(uop_500))) # shape=(4, 5, 5)
output = relay.Tuple([bop_508,])
output2 = relay.Tuple([bop_508,])
func_524 = relay.Function([var_485,var_486,], output)
mod['func_524'] = func_524
mod = relay.transform.InferType()(mod)
var_525 = relay.var("var_525", dtype = "float32", shape = (4, 5, 5))#candidate|525|(4, 5, 5)|var|float32
var_526 = relay.var("var_526", dtype = "float32", shape = (4, 5, 5))#candidate|526|(4, 5, 5)|var|float32
output = func_524(var_525,var_526,)
func_527 = relay.Function([var_525,var_526,], output)
mutated_mod['func_527'] = func_527
mutated_mod = relay.transform.InferType()(mutated_mod)
const_718 = relay.const([[[9.655690,-7.682518,-3.392226,-5.405470,-1.185455,-9.756915,2.257547,4.655029,4.395804,3.024293,-1.058300,4.387641,2.381124,0.985476,2.508915,5.907568],[4.477459,0.047061,3.725343,5.191466,-6.212521,0.654822,3.243086,-3.219054,-2.845003,-4.564344,5.490338,-3.894900,9.346357,-6.479396,-9.147366,6.867739],[4.939918,9.963194,-4.129897,0.644415,4.998619,-4.758898,8.018083,3.153816,-6.481184,-7.886805,0.254476,-6.092141,4.888984,5.322069,8.813477,4.619299],[-3.720926,0.995795,0.536278,9.468907,9.883012,-9.931423,-0.249613,7.940421,4.191187,-2.883739,-7.654271,6.577184,4.661803,9.794151,4.700475,9.270092],[1.695561,-2.125800,9.752406,1.617924,9.613395,-6.013738,7.413288,-3.700414,7.666021,1.235878,-1.708076,0.992223,-0.529712,-5.573419,-5.948109,0.665863],[-5.538501,-5.491668,1.356979,-8.491011,7.717729,-8.739107,-3.853712,-2.505793,0.898789,4.064254,-4.786837,3.512033,8.200088,3.389623,0.146001,-6.730395],[-0.953340,-3.859487,-8.618374,7.241837,4.601958,6.163718,-2.770837,3.473977,9.866838,2.311167,-0.379431,-7.528758,-2.941078,5.315347,-7.672459,5.530436],[-6.726271,-0.343057,9.170287,2.203856,7.316575,-8.845254,-6.508094,8.780950,0.777144,2.378158,6.630534,2.801218,5.781952,-5.625991,-5.291730,3.082895],[6.293908,-4.754720,3.188928,5.351062,-7.907218,-6.296695,0.684616,-3.922834,0.778258,-0.219368,-6.831813,-5.209683,-6.983976,0.142462,6.725224,-4.530661],[2.425478,8.544747,-7.738819,8.663554,-5.151039,6.521243,-1.019245,-2.014607,5.647349,-3.651140,9.530783,-1.039151,3.807430,-5.972373,-1.465490,6.940568],[7.135990,-8.248798,8.949023,-4.485696,2.471079,-5.122086,-5.440123,1.009021,2.806665,9.425192,0.396147,4.325595,6.641736,9.077114,-6.728312,9.172977],[2.964706,1.818540,-9.297806,-4.472086,9.120945,9.200116,-0.179369,0.146977,-5.651128,-1.322434,-9.758797,3.045834,7.592391,4.186864,2.115153,-6.894203],[-6.031846,-5.058610,2.730972,8.145136,5.240030,-0.259219,7.054425,9.963949,-0.684956,7.581456,7.228523,9.636921,0.081949,-6.183268,7.526453,8.282827],[-0.884215,-5.629252,1.562109,-3.364080,-6.219014,-9.171571,3.235824,-6.512058,7.726792,-9.786384,-8.638685,3.336758,5.107785,-8.476494,-8.074840,-0.803487],[8.726193,3.241671,-3.010178,2.133592,-3.533065,2.949594,-4.260027,-9.917909,0.886712,-2.423157,-0.888604,-5.979405,-4.272774,-7.025258,-0.627618,2.960648]],[[-8.893709,-9.160117,5.395850,3.310980,2.408764,1.074120,-9.622665,3.381156,-9.024735,3.751267,-3.325057,-0.807565,6.828050,7.559107,-6.906625,2.034628],[4.952762,3.564545,-0.751681,1.919658,6.870403,1.905056,-3.001392,-6.845146,-2.444241,8.292817,4.278367,1.852305,-7.358486,-6.321694,-1.374781,0.849280],[-1.588275,-1.661524,-2.662619,-6.112562,-9.712713,2.938057,1.256970,6.531486,-1.423412,-4.809113,9.269561,-0.007619,-3.341815,-0.707194,-4.572814,6.636743],[-5.722354,8.633563,8.690655,0.800927,0.281958,-3.130160,-6.973654,2.384137,-5.121018,-6.226063,6.825814,0.963724,3.507827,-6.484168,-1.929809,-0.807801],[9.694709,5.856549,-0.284349,-7.437772,6.546813,-2.551438,8.189029,-3.552526,1.781064,4.155111,7.980492,-5.014108,-4.301292,3.785116,-8.768537,2.433977],[3.356851,-4.698543,4.942312,-0.719561,5.184113,-8.690242,-2.285848,-2.724598,2.175524,-4.180018,2.663205,-9.060767,-7.709828,-6.652797,2.948783,-8.865261],[-9.275770,-8.268854,-3.465743,-2.274646,2.304266,-8.917259,-5.781935,1.995655,-4.559004,-8.670548,9.268611,2.208821,-4.149410,-4.590801,1.575956,0.354122],[-5.052468,-4.492793,-2.100693,-9.631806,6.249990,8.638853,-4.194118,-8.665812,-5.577920,-6.757179,2.333426,0.333719,1.702188,2.098624,4.315382,-2.010862],[9.667187,-3.642116,2.816024,0.563333,5.772386,-4.646963,-2.935526,-6.857670,-2.361722,-3.453976,-0.297572,4.966141,6.510612,-2.922170,0.113263,-0.111835],[9.798917,-2.496911,-6.966402,-1.159518,-6.721004,6.710926,0.357019,-1.093434,-2.561121,8.623971,-3.714232,-4.254445,8.865959,-1.762284,8.324101,0.660882],[8.053082,1.939809,-8.035388,5.135936,0.715417,2.147434,-1.980175,-9.037657,-4.179603,0.087663,-4.383653,-4.896328,9.254949,0.154419,-9.436229,1.694341],[-4.749315,8.478816,-8.828281,-9.616443,2.295746,-0.726896,9.447326,-8.686160,-8.649763,-2.059757,2.008423,5.315929,-4.024573,1.865468,4.395444,-5.683788],[9.255125,-9.468024,1.833952,6.615428,-1.294516,-7.463863,-7.324297,5.645843,1.172746,-2.834016,8.250166,7.058091,-5.485373,-6.493172,3.844999,0.517821],[-2.989893,1.539912,-9.496157,-1.465035,-7.332143,-9.465837,8.450337,-4.366991,-7.673832,3.916566,-3.235888,8.687573,4.137191,-4.141080,-1.474678,0.778604],[-3.847500,-7.736770,-9.841882,5.362294,-4.365779,3.468572,-3.928405,-0.706411,-1.947902,-6.001398,-0.883556,6.311474,4.100403,-6.441352,-5.111949,-6.752271]],[[-3.084715,5.293802,7.936516,-1.309740,2.543191,4.423355,2.832328,-8.891266,2.176270,-3.048365,-0.999249,4.325372,5.534954,7.166967,6.857314,-2.133499],[9.467279,-7.976767,3.795722,-0.756098,0.355438,-8.245714,4.294497,-2.223993,3.144517,-7.321892,2.238812,9.463135,4.340406,-1.365976,-9.786837,7.057088],[-7.380774,-2.448436,-7.495881,-0.336029,-8.832931,-9.477005,5.221757,-9.243928,2.498505,-3.120890,-8.762657,4.363294,0.930266,-4.195390,2.096514,0.908725],[-6.383180,6.869989,-8.168117,-4.851965,-3.099694,-1.642380,8.862973,-5.456484,4.153868,6.463493,-1.666680,5.603169,-7.847527,0.219358,6.289700,-5.741091],[-4.069598,-3.509006,8.327372,1.086870,1.524599,-5.873616,-1.544213,6.164848,2.835081,3.094391,-8.093892,2.489409,-8.525579,-3.850055,1.158965,6.905285],[-6.937108,-5.695969,-1.615681,0.681884,7.506139,0.141716,-3.634122,1.118116,1.804943,8.912618,-9.383979,0.782385,0.470489,-6.464933,-3.384646,-4.502165],[-7.250143,-0.112364,-8.289347,-3.212720,2.800670,1.925041,6.276716,-3.375739,5.955750,-8.670589,-7.689146,-0.140238,1.262238,7.449370,5.256498,-9.671508],[-1.080409,-6.798142,-0.829855,0.630875,-3.758982,5.101256,3.550953,1.527363,3.006104,-1.622914,5.939296,7.426829,-7.084033,-1.156895,-0.443377,5.803297],[5.970808,6.359690,-6.761267,-5.355541,8.047525,-8.584495,8.451230,1.657733,0.765511,-3.334427,-5.204665,0.090063,-6.285122,-6.134719,-1.141448,-9.472066],[-0.838786,2.334418,-4.487329,6.128768,6.317248,-6.722212,3.304055,6.325081,-1.465734,0.193269,8.244633,8.315117,-2.446528,-9.456497,0.069139,4.378451],[-4.361602,-2.962345,-9.446540,-3.155424,-2.518760,-7.111750,-2.539246,-8.843559,8.744675,-5.493749,6.905779,5.079613,1.998007,-1.327306,-8.844881,-0.331680],[4.132763,6.212274,6.559884,3.225976,-3.535570,6.380470,-6.226043,7.479801,-9.779505,-8.184611,6.997262,6.441604,-8.667444,3.854736,1.774902,7.981798],[5.717563,-8.857031,9.164573,-5.358247,3.371260,-9.470217,5.259251,-8.996370,5.244969,6.197504,-3.918062,-8.610660,0.080090,5.662372,8.500353,0.410322],[4.825799,6.913701,5.364250,-1.689883,-6.019415,-6.913081,2.172434,5.971577,-4.611542,0.810149,5.287097,2.710677,-0.482206,-0.290043,0.177244,-2.716747],[9.272207,1.456813,8.991005,-2.966247,0.142780,0.944037,1.391637,0.465813,-3.160275,-2.271384,-5.781580,-8.517264,-0.555071,4.244207,-0.123588,-3.868748]],[[1.699626,-3.467582,4.554412,-9.979959,-4.382348,4.411875,-9.663439,5.546057,-5.333883,3.573767,2.653496,6.309222,-5.596943,8.673305,-4.100130,-3.638278],[-1.190184,-7.202547,3.322163,-1.519466,-0.494382,2.434977,-0.185130,6.257613,-8.849638,-5.006074,-4.738489,9.907454,-4.713685,5.249355,-9.265644,-3.621184],[2.920932,8.535785,-8.160367,-4.145093,5.632375,7.116404,-4.175239,-5.381190,8.477928,-9.459834,-5.415989,-8.971121,-1.736577,7.232362,-7.650852,0.586796],[-9.549552,-6.330694,-5.633750,-2.149262,6.350444,-6.375687,-5.661094,-6.514180,0.800495,-6.860122,1.448898,-8.538983,-2.175181,-5.232578,2.758213,-6.647203],[-6.571369,-6.046538,9.506745,9.539338,1.139869,-6.388548,-8.393242,1.292398,5.017655,-7.694411,5.615958,4.551685,-6.584313,-1.569193,6.584739,-0.102123],[1.316908,4.915826,9.329705,6.895434,-9.963105,-9.434782,4.803049,-5.066389,5.975383,7.219283,6.393010,4.609793,-4.743161,1.773105,-2.951275,-1.201788],[6.050995,6.686091,-2.320121,3.627012,-6.420719,4.013390,5.764706,5.096029,-0.635663,4.944815,3.317180,-0.632045,-4.610603,7.912474,4.651323,0.873459],[2.984748,5.417524,8.856949,-2.462282,-2.301307,9.923289,3.885799,4.418012,1.666318,1.358393,1.199564,6.000559,-3.661639,-7.971882,-5.375501,-7.910130],[-0.299424,0.842841,-5.935252,-1.173281,4.126600,-0.697627,-9.399227,7.419176,0.474115,-8.717166,-6.610907,-1.936230,-6.472147,-4.181653,-0.044836,8.893426],[-0.766238,5.776353,-6.395578,4.228707,8.081929,5.709502,7.348762,-5.318187,1.175603,8.485042,-1.180288,-2.368298,6.416618,4.254702,9.790986,-5.091891],[9.460102,-0.777268,1.523168,5.010292,-5.209525,-9.766330,7.052795,-8.795015,6.831243,-4.056643,4.972352,9.935195,1.838988,8.223949,1.428681,-3.015128],[9.234575,-5.324450,9.999968,6.665762,-3.534327,3.245537,-2.956087,1.927713,-1.181203,7.931342,-5.193208,-2.090721,5.197369,5.737315,5.571912,3.213946],[-4.757444,-0.913303,-0.769792,1.060265,1.712361,-2.223606,-3.077412,-7.209524,-6.953339,3.690436,-1.300780,-9.949663,1.281103,-7.436498,-1.038699,7.180369],[9.482833,-4.844803,2.294516,9.256787,-8.486742,6.091585,7.874355,5.959539,9.637427,-1.754784,-3.134759,-6.513210,-4.429722,7.400395,-4.881740,-9.658838],[-7.826857,8.975468,-3.846696,-9.194923,3.632162,-6.310383,2.743376,-6.157759,-2.364236,-3.645514,3.338643,-2.743094,4.482534,-0.622544,-6.239792,-9.509056]]], dtype = "float32")#candidate|718|(4, 15, 16)|const|float32
uop_719 = relay.log2(const_718.astype('float32')) # shape=(4, 15, 16)
func_524_call = mod.get_global_var('func_524')
func_527_call = mutated_mod.get_global_var('func_527')
var_722 = relay.var("var_722", dtype = "float32", shape = (50, 2))#candidate|722|(50, 2)|var|float32
call_721 = relay.TupleGetItem(func_524_call(relay.reshape(var_722.astype('float32'), [4, 5, 5]), relay.reshape(var_722.astype('float32'), [4, 5, 5]), ), 0)
call_723 = relay.TupleGetItem(func_527_call(relay.reshape(var_722.astype('float32'), [4, 5, 5]), relay.reshape(var_722.astype('float32'), [4, 5, 5]), ), 0)
bop_729 = relay.maximum(var_722.astype('uint64'), relay.reshape(call_721.astype('uint64'), relay.shape_of(var_722))) # shape=(50, 2)
bop_732 = relay.maximum(var_722.astype('uint64'), relay.reshape(call_723.astype('uint64'), relay.shape_of(var_722))) # shape=(50, 2)
func_524_call = mod.get_global_var('func_524')
func_527_call = mutated_mod.get_global_var('func_527')
call_738 = relay.TupleGetItem(func_524_call(relay.reshape(bop_729.astype('float32'), [4, 5, 5]), relay.reshape(var_722.astype('float32'), [4, 5, 5]), ), 0)
call_739 = relay.TupleGetItem(func_527_call(relay.reshape(bop_729.astype('float32'), [4, 5, 5]), relay.reshape(var_722.astype('float32'), [4, 5, 5]), ), 0)
output = relay.Tuple([uop_719,bop_729,call_738,])
output2 = relay.Tuple([uop_719,bop_732,call_739,])
func_740 = relay.Function([var_722,], output)
mod['func_740'] = func_740
mod = relay.transform.InferType()(mod)
mutated_mod['func_740'] = func_740
mutated_mod = relay.transform.InferType()(mutated_mod)
var_741 = relay.var("var_741", dtype = "float32", shape = (50, 2))#candidate|741|(50, 2)|var|float32
func_740_call = mutated_mod.get_global_var('func_740')
call_742 = func_740_call(var_741)
output = call_742
func_743 = relay.Function([var_741], output)
mutated_mod['func_743'] = func_743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_783 = relay.var("var_783", dtype = "float32", shape = (9, 9, 8))#candidate|783|(9, 9, 8)|var|float32
uop_784 = relay.atan(var_783.astype('float32')) # shape=(9, 9, 8)
uop_798 = relay.asinh(uop_784.astype('float32')) # shape=(9, 9, 8)
func_740_call = mod.get_global_var('func_740')
func_743_call = mutated_mod.get_global_var('func_743')
const_805 = relay.const([6.087875,0.636847,-3.173252,-5.138159,5.895610,-8.493513,0.071061,5.528616,-1.643070,3.505633,1.234160,-3.634030,-0.338072,-2.976957,2.749790,2.313498,4.377562,-5.872691,2.889130,1.553975,8.400928,2.010488,0.500230,2.033376,5.185088,-5.283177,9.871261,9.277808,-5.829840,-7.114405,-1.161500,-1.803522,-4.315611,5.513436,1.672171,-4.863651,-6.124922,6.339516,-5.476598,2.503197,5.808211,-3.302714,9.033617,4.794005,1.012177,4.173224,9.859993,3.676406,-5.313068,-4.914200,7.240628,-8.944923,-1.308698,6.692171,-4.320343,-9.015399,-0.393818,7.792726,-1.532515,-8.039883,-6.896678,8.297880,8.829446,8.248942,-1.835122,-7.612877,-2.729664,5.945297,-2.229147,8.509177,-2.531068,9.364125,-4.613358,-1.902527,1.336086,-9.813136,-0.702643,3.671699,-5.247535,4.001858,-4.110187,-5.030724,-2.700725,4.446748,-2.885953,-4.098243,8.527357,-4.080895,-8.037795,-6.041204,0.396010,3.286365,4.626786,8.375653,5.503242,-5.197637,-5.696164,-7.362991,-1.627391,-6.201125], dtype = "float32")#candidate|805|(100,)|const|float32
call_804 = relay.TupleGetItem(func_740_call(relay.reshape(const_805.astype('float32'), [50, 2])), 2)
call_806 = relay.TupleGetItem(func_743_call(relay.reshape(const_805.astype('float32'), [50, 2])), 2)
output = relay.Tuple([uop_798,call_804,const_805,])
output2 = relay.Tuple([uop_798,call_806,const_805,])
func_809 = relay.Function([var_783,], output)
mod['func_809'] = func_809
mod = relay.transform.InferType()(mod)
mutated_mod['func_809'] = func_809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_810 = relay.var("var_810", dtype = "float32", shape = (9, 9, 8))#candidate|810|(9, 9, 8)|var|float32
func_809_call = mutated_mod.get_global_var('func_809')
call_811 = func_809_call(var_810)
output = call_811
func_812 = relay.Function([var_810], output)
mutated_mod['func_812'] = func_812
mutated_mod = relay.transform.InferType()(mutated_mod)
var_996 = relay.var("var_996", dtype = "float32", shape = (3, 15, 4))#candidate|996|(3, 15, 4)|var|float32
uop_997 = relay.tan(var_996.astype('float32')) # shape=(3, 15, 4)
output = relay.Tuple([uop_997,])
output2 = relay.Tuple([uop_997,])
func_1017 = relay.Function([var_996,], output)
mod['func_1017'] = func_1017
mod = relay.transform.InferType()(mod)
mutated_mod['func_1017'] = func_1017
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1018 = relay.var("var_1018", dtype = "float32", shape = (3, 15, 4))#candidate|1018|(3, 15, 4)|var|float32
func_1017_call = mutated_mod.get_global_var('func_1017')
call_1019 = func_1017_call(var_1018)
output = call_1019
func_1020 = relay.Function([var_1018], output)
mutated_mod['func_1020'] = func_1020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1065 = relay.var("var_1065", dtype = "int32", shape = (3, 9, 5))#candidate|1065|(3, 9, 5)|var|int32
const_1066 = relay.const([[[-8,-9,7,-6,-6],[5,-5,-7,8,-8],[-6,8,9,3,-3],[3,3,4,8,10],[-4,7,1,-8,1],[1,1,5,1,-10],[-8,-6,5,-10,1],[8,-6,-5,-10,8],[-9,7,10,1,-1]],[[6,4,-8,-1,5],[-8,-9,5,-3,-7],[6,-2,5,6,3],[-9,-7,-10,-3,3],[7,8,-6,-10,-9],[10,2,-8,-3,-4],[-2,-7,5,3,-10],[-5,-8,1,-7,-4],[7,-4,7,-7,-8]],[[9,4,-10,3,9],[2,10,-9,5,-1],[4,5,8,-4,4],[-6,4,9,10,-1],[-5,3,2,-8,7],[6,-9,3,-2,-10],[9,-9,7,8,2],[-6,-2,-4,-10,1],[-2,-1,7,8,-9]]], dtype = "int32")#candidate|1066|(3, 9, 5)|const|int32
bop_1067 = relay.subtract(var_1065.astype('int32'), relay.reshape(const_1066.astype('int32'), relay.shape_of(var_1065))) # shape=(3, 9, 5)
var_1078 = relay.var("var_1078", dtype = "int32", shape = (3, 9, 5))#candidate|1078|(3, 9, 5)|var|int32
bop_1079 = relay.divide(const_1066.astype('float32'), relay.reshape(var_1078.astype('float32'), relay.shape_of(const_1066))) # shape=(3, 9, 5)
uop_1083 = relay.cos(bop_1079.astype('float32')) # shape=(3, 9, 5)
output = relay.Tuple([bop_1067,uop_1083,])
output2 = relay.Tuple([bop_1067,uop_1083,])
func_1089 = relay.Function([var_1065,var_1078,], output)
mod['func_1089'] = func_1089
mod = relay.transform.InferType()(mod)
mutated_mod['func_1089'] = func_1089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1089_call = mutated_mod.get_global_var('func_1089')
var_1091 = relay.var("var_1091", dtype = "int32", shape = (3, 9, 5))#candidate|1091|(3, 9, 5)|var|int32
var_1092 = relay.var("var_1092", dtype = "int32", shape = (3, 9, 5))#candidate|1092|(3, 9, 5)|var|int32
call_1090 = func_1089_call(var_1091,var_1092,)
output = call_1090
func_1093 = relay.Function([var_1091,var_1092,], output)
mutated_mod['func_1093'] = func_1093
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1312 = relay.const([[[8.058725],[6.525802],[0.356270],[-0.440622]],[[3.277334],[7.082997],[9.782565],[3.136104]]], dtype = "float32")#candidate|1312|(2, 4, 1)|const|float32
uop_1313 = relay.asinh(const_1312.astype('float32')) # shape=(2, 4, 1)
output = uop_1313
output2 = uop_1313
func_1316 = relay.Function([], output)
mod['func_1316'] = func_1316
mod = relay.transform.InferType()(mod)
mutated_mod['func_1316'] = func_1316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mutated_mod.get_global_var('func_1316')
call_1317 = func_1316_call()
output = call_1317
func_1318 = relay.Function([], output)
mutated_mod['func_1318'] = func_1318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_1337 = func_1316_call()
call_1338 = func_1316_call()
output = relay.Tuple([call_1337,])
output2 = relay.Tuple([call_1338,])
func_1339 = relay.Function([], output)
mod['func_1339'] = func_1339
mod = relay.transform.InferType()(mod)
mutated_mod['func_1339'] = func_1339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1339_call = mutated_mod.get_global_var('func_1339')
call_1340 = func_1339_call()
output = call_1340
func_1341 = relay.Function([], output)
mutated_mod['func_1341'] = func_1341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_1403 = relay.TupleGetItem(func_1339_call(), 0)
call_1404 = relay.TupleGetItem(func_1341_call(), 0)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_1405 = func_1316_call()
call_1406 = func_1316_call()
func_524_call = mod.get_global_var('func_524')
func_527_call = mutated_mod.get_global_var('func_527')
const_1410 = relay.const([[-3.772228,-8.554747,-7.481395,-1.192872],[1.336085,2.947758,-4.447293,-5.998660],[7.058907,8.316059,5.623907,-0.597114],[9.127773,-2.799165,2.317127,3.027476],[5.968889,-6.310946,5.494704,1.126631],[-1.623615,-5.073463,5.845728,-5.654755],[1.114831,-4.142564,7.874278,-6.379154],[-5.107936,-9.909669,-9.210588,6.372425],[5.574864,3.332494,-8.020244,3.523258],[-9.411426,-8.790948,-3.533917,-8.848208],[-5.975644,-7.383791,6.560843,-3.028196],[2.997545,5.004079,8.197757,0.804503],[7.314503,5.762096,-1.126353,-4.774712],[-3.488596,-5.461502,9.655189,-0.825469],[4.327290,7.352288,-4.908026,-6.830322],[-0.228152,9.436469,-5.352023,-5.075344],[-4.348503,1.723185,-3.052167,1.930528],[-2.838010,4.256665,-3.148210,-6.738584],[-5.045187,-0.637634,5.240821,-7.137965],[-7.423701,2.590599,-4.919397,-3.748219],[3.978557,8.770107,6.501298,-0.102164],[-1.725463,0.755249,-2.868618,-2.173433],[0.583016,2.080161,2.577289,-5.765328],[1.061048,-6.357755,3.928195,-9.532840],[6.476162,-2.552723,-4.392499,-0.610037]], dtype = "float32")#candidate|1410|(25, 4)|const|float32
call_1409 = relay.TupleGetItem(func_524_call(relay.reshape(const_1410.astype('float32'), [4, 5, 5]), relay.reshape(const_1410.astype('float32'), [4, 5, 5]), ), 0)
call_1411 = relay.TupleGetItem(func_527_call(relay.reshape(const_1410.astype('float32'), [4, 5, 5]), relay.reshape(const_1410.astype('float32'), [4, 5, 5]), ), 0)
output = relay.Tuple([call_1403,call_1405,call_1409,const_1410,])
output2 = relay.Tuple([call_1404,call_1406,call_1411,const_1410,])
func_1415 = relay.Function([], output)
mod['func_1415'] = func_1415
mod = relay.transform.InferType()(mod)
mutated_mod['func_1415'] = func_1415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1415_call = mutated_mod.get_global_var('func_1415')
call_1416 = func_1415_call()
output = call_1416
func_1417 = relay.Function([], output)
mutated_mod['func_1417'] = func_1417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_1440 = func_1316_call()
call_1441 = func_1316_call()
func_524_call = mod.get_global_var('func_524')
func_527_call = mutated_mod.get_global_var('func_527')
var_1452 = relay.var("var_1452", dtype = "float32", shape = (100,))#candidate|1452|(100,)|var|float32
call_1451 = relay.TupleGetItem(func_524_call(relay.reshape(var_1452.astype('float32'), [4, 5, 5]), relay.reshape(var_1452.astype('float32'), [4, 5, 5]), ), 0)
call_1453 = relay.TupleGetItem(func_527_call(relay.reshape(var_1452.astype('float32'), [4, 5, 5]), relay.reshape(var_1452.astype('float32'), [4, 5, 5]), ), 0)
output = relay.Tuple([call_1440,call_1451,var_1452,])
output2 = relay.Tuple([call_1441,call_1453,var_1452,])
func_1454 = relay.Function([var_1452,], output)
mod['func_1454'] = func_1454
mod = relay.transform.InferType()(mod)
var_1455 = relay.var("var_1455", dtype = "float32", shape = (100,))#candidate|1455|(100,)|var|float32
output = func_1454(var_1455)
func_1456 = relay.Function([var_1455], output)
mutated_mod['func_1456'] = func_1456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_1465 = func_1316_call()
call_1466 = func_1316_call()
func_740_call = mod.get_global_var('func_740')
func_743_call = mutated_mod.get_global_var('func_743')
const_1471 = relay.const([1.506313,1.731930,-7.256419,-8.400173,-6.542105,4.660876,0.125234,2.051141,-3.975574,8.452385,6.801727,6.457263,9.862145,-0.471334,-1.993830,5.941681,8.049049,7.302488,-9.980765,5.331271,3.335180,6.275686,-9.507129,-0.865835,-8.908232,-7.880588,0.267098,-2.448050,-1.407748,0.248749,-8.202170,-6.185034,-2.069324,-1.333070,-9.580987,6.410444,-8.757825,-9.163721,8.242618,8.157376,9.116687,7.894031,0.428852,7.681238,4.949740,-1.766508,2.285832,0.833382,7.248982,8.038945,6.140007,3.238625,0.807047,8.044144,4.421411,-0.362261,-6.387281,8.139973,5.211043,0.137504,2.218062,-3.764399,4.424156,-5.234695,4.546771,-6.601910,2.766430,-0.583333,3.968638,5.962904,4.872921,9.334502,-6.493119,1.698413,0.454499,-6.285922,0.566502,-3.485205,-0.063733,6.113846,-5.417392,-9.206769,8.507743,-1.210140,-9.418446,6.207939,1.862715,9.019685,9.178567,5.993615,-8.115272,-4.537234,-6.216859,-8.152073,3.486589,2.151181,6.418738,3.195548,-5.342293,5.034652], dtype = "float32")#candidate|1471|(100,)|const|float32
call_1470 = relay.TupleGetItem(func_740_call(relay.reshape(const_1471.astype('float32'), [50, 2])), 2)
call_1472 = relay.TupleGetItem(func_743_call(relay.reshape(const_1471.astype('float32'), [50, 2])), 2)
uop_1474 = relay.cos(call_1465.astype('float64')) # shape=(2, 4, 1)
uop_1476 = relay.cos(call_1466.astype('float64')) # shape=(2, 4, 1)
output = relay.Tuple([call_1470,const_1471,uop_1474,])
output2 = relay.Tuple([call_1472,const_1471,uop_1476,])
func_1489 = relay.Function([], output)
mod['func_1489'] = func_1489
mod = relay.transform.InferType()(mod)
output = func_1489()
func_1490 = relay.Function([], output)
mutated_mod['func_1490'] = func_1490
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1535 = relay.var("var_1535", dtype = "uint64", shape = (7, 16, 5))#candidate|1535|(7, 16, 5)|var|uint64
var_1536 = relay.var("var_1536", dtype = "uint64", shape = (7, 16, 5))#candidate|1536|(7, 16, 5)|var|uint64
bop_1537 = relay.bitwise_or(var_1535.astype('uint64'), relay.reshape(var_1536.astype('uint64'), relay.shape_of(var_1535))) # shape=(7, 16, 5)
uop_1542 = relay.log(var_1536.astype('float64')) # shape=(7, 16, 5)
bop_1548 = relay.bitwise_xor(uop_1542.astype('int64'), relay.reshape(var_1535.astype('int64'), relay.shape_of(uop_1542))) # shape=(7, 16, 5)
output = relay.Tuple([bop_1537,bop_1548,])
output2 = relay.Tuple([bop_1537,bop_1548,])
func_1559 = relay.Function([var_1535,var_1536,], output)
mod['func_1559'] = func_1559
mod = relay.transform.InferType()(mod)
mutated_mod['func_1559'] = func_1559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1559_call = mutated_mod.get_global_var('func_1559')
var_1561 = relay.var("var_1561", dtype = "uint64", shape = (7, 16, 5))#candidate|1561|(7, 16, 5)|var|uint64
var_1562 = relay.var("var_1562", dtype = "uint64", shape = (7, 16, 5))#candidate|1562|(7, 16, 5)|var|uint64
call_1560 = func_1559_call(var_1561,var_1562,)
output = call_1560
func_1563 = relay.Function([var_1561,var_1562,], output)
mutated_mod['func_1563'] = func_1563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_1629 = func_1316_call()
call_1630 = func_1316_call()
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_1631 = func_1316_call()
call_1632 = func_1316_call()
func_1415_call = mod.get_global_var('func_1415')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_1644 = relay.TupleGetItem(func_1415_call(), 3)
call_1645 = relay.TupleGetItem(func_1417_call(), 3)
output = relay.Tuple([call_1629,call_1631,call_1644,])
output2 = relay.Tuple([call_1630,call_1632,call_1645,])
func_1647 = relay.Function([], output)
mod['func_1647'] = func_1647
mod = relay.transform.InferType()(mod)
mutated_mod['func_1647'] = func_1647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1647_call = mutated_mod.get_global_var('func_1647')
call_1648 = func_1647_call()
output = call_1648
func_1649 = relay.Function([], output)
mutated_mod['func_1649'] = func_1649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_1671 = relay.TupleGetItem(func_1339_call(), 0)
call_1672 = relay.TupleGetItem(func_1341_call(), 0)
uop_1689 = relay.asin(call_1671.astype('float64')) # shape=(2, 4, 1)
uop_1691 = relay.asin(call_1672.astype('float64')) # shape=(2, 4, 1)
func_1559_call = mod.get_global_var('func_1559')
func_1563_call = mutated_mod.get_global_var('func_1563')
const_1706 = relay.const([10,-3,2,3,-5,6,7,-5,8,1,-7,1,-10,-9,-2,5,4,10,8,-10,2,-2,-3,-5,-8,-8,-9,-1,5,7,-6,9,2,8,3,-2,5,6,-5,-8,9,10,-5,5,10,-9,-6,-8,6,-8,-3,3,-8,-7,-10,-6,3,7,6,7,-5,2,-5,-2,4,9,4,-7,-1,-5,-1,1,8,1,-9,-8,7,8,10,-2,-1,2,-2,-10,-5,-3,-8,2,2,8,4,-8,7,4,5,10,4,3,-4,9,8,8,4,-1,-5,-8,6,1,-1,9,-10,3,-4,2,-9,-7,-2,-2,7,5,-4,-5,8,-4,-1,-6,-3,-7,-7,-4,9,-5,8,-7,1,-9,4,5,-9,2,1,3,9,2,-8,-4,10,5,-9,7,4,-6,9,10,-10,2,-10,-7,6,7,-8,10,-2,-7,9,10,-9,2,8,10,4,-9,-6,3,6,7,-3,-3,3,-6,4,-8,4,3,-3,10,-4,2,-5,-5,7,6,-8,-6,1,-5,-10,9,6,6,6,5,-2,3,3,2,-7,-9,9,6,-9,-2,8,3,-3,3,2,1,-6,3,10,9,-4,-2,6,-1,-1,-4,-6,2,3,-1,5,10,6,-1,1,-4,8,7,4,-7,-3,-3,-7,2,-2,6,7,-9,9,1,-7,4,1,-9,1,1,8,-5,-10,-4,10,-10,-6,-9,-6,-7,-5,10,4,4,-9,7,2,-2,-9,-5,-8,7,3,-1,8,3,10,-3,7,8,-4,-3,9,9,4,8,-8,-6,-10,-1,4,4,-9,8,2,-4,-3,3,4,1,-3,-10,3,-5,4,3,-9,-1,2,6,5,2,-9,-9,4,-9,-8,-1,6,8,-1,-7,8,1,-7,-7,1,10,4,-10,-9,7,-9,-10,4,6,-1,-8,-1,10,-9,2,-6,-7,4,-9,8,2,-4,-4,-10,-6,3,9,-4,-4,6,1,2,2,-7,9,-7,-3,-3,1,-7,-4,10,4,4,5,8,4,7,-4,-9,8,-3,-6,7,-10,2,-5,-9,6,-9,-3,-10,6,7,10,4,9,-8,-4,2,-9,7,-9,-3,8,-8,10,2,-3,-8,4,-2,7,-9,7,4,8,-10,-8,1,-6,8,7,3,-8,7,-1,6,9,1,-7,-1,-6,1,5,-9,3,6,9,1,10,-1,5,9,3,1,4,-4,-5,6,6,-1,-7,8,8,-7,-7,9,6,-9,7,8,4,-6,6,10,-1,3,-10,4,-2,8,9,-1,-5,-5,-10,8,6,4,-7,-8,-7,-6,3,9,-3,5,4,9,6,-4,1,-2,-5,3,-5,10,-1,9,8,-7,4,-3,8,8,9,4,-1,9,7,7,2,-1,8,4,9,7,5,-2,5,1,-9,4,-3,5,4,9,-3,-8,4,5,5,-7,-3,7,8,-1,-5,6,-7,-8,-4,6,9,6,-6,-7,6,-5,-2,6,2,-6,2], dtype = "uint64")#candidate|1706|(560,)|const|uint64
call_1705 = relay.TupleGetItem(func_1559_call(relay.reshape(const_1706.astype('uint64'), [7, 16, 5]), relay.reshape(const_1706.astype('uint64'), [7, 16, 5]), ), 0)
call_1707 = relay.TupleGetItem(func_1563_call(relay.reshape(const_1706.astype('uint64'), [7, 16, 5]), relay.reshape(const_1706.astype('uint64'), [7, 16, 5]), ), 0)
bop_1720 = relay.floor_divide(uop_1689.astype('float32'), const_1706.astype('float32')) # shape=(2, 4, 560)
bop_1723 = relay.floor_divide(uop_1691.astype('float32'), const_1706.astype('float32')) # shape=(2, 4, 560)
func_524_call = mod.get_global_var('func_524')
func_527_call = mutated_mod.get_global_var('func_527')
var_1727 = relay.var("var_1727", dtype = "float32", shape = (100,))#candidate|1727|(100,)|var|float32
call_1726 = relay.TupleGetItem(func_524_call(relay.reshape(var_1727.astype('float32'), [4, 5, 5]), relay.reshape(var_1727.astype('float32'), [4, 5, 5]), ), 0)
call_1728 = relay.TupleGetItem(func_527_call(relay.reshape(var_1727.astype('float32'), [4, 5, 5]), relay.reshape(var_1727.astype('float32'), [4, 5, 5]), ), 0)
bop_1735 = relay.multiply(uop_1689.astype('uint64'), const_1706.astype('uint64')) # shape=(2, 4, 560)
bop_1738 = relay.multiply(uop_1691.astype('uint64'), const_1706.astype('uint64')) # shape=(2, 4, 560)
output = relay.Tuple([call_1705,bop_1720,call_1726,var_1727,bop_1735,])
output2 = relay.Tuple([call_1707,bop_1723,call_1728,var_1727,bop_1738,])
func_1740 = relay.Function([var_1727,], output)
mod['func_1740'] = func_1740
mod = relay.transform.InferType()(mod)
mutated_mod['func_1740'] = func_1740
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1741 = relay.var("var_1741", dtype = "float32", shape = (100,))#candidate|1741|(100,)|var|float32
func_1740_call = mutated_mod.get_global_var('func_1740')
call_1742 = func_1740_call(var_1741)
output = call_1742
func_1743 = relay.Function([var_1741], output)
mutated_mod['func_1743'] = func_1743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_1752 = relay.TupleGetItem(func_1489_call(), 0)
call_1753 = relay.TupleGetItem(func_1490_call(), 0)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_1762 = relay.TupleGetItem(func_1454_call(relay.reshape(call_1752.astype('float32'), [100,])), 1)
call_1763 = relay.TupleGetItem(func_1456_call(relay.reshape(call_1752.astype('float32'), [100,])), 1)
func_1415_call = mod.get_global_var('func_1415')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_1765 = relay.TupleGetItem(func_1415_call(), 2)
call_1766 = relay.TupleGetItem(func_1417_call(), 2)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_1771 = relay.TupleGetItem(func_1339_call(), 0)
call_1772 = relay.TupleGetItem(func_1341_call(), 0)
output = relay.Tuple([call_1752,call_1762,call_1765,call_1771,])
output2 = relay.Tuple([call_1753,call_1763,call_1766,call_1772,])
func_1776 = relay.Function([], output)
mod['func_1776'] = func_1776
mod = relay.transform.InferType()(mod)
mutated_mod['func_1776'] = func_1776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1776_call = mutated_mod.get_global_var('func_1776')
call_1777 = func_1776_call()
output = call_1777
func_1778 = relay.Function([], output)
mutated_mod['func_1778'] = func_1778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1776_call = mod.get_global_var('func_1776')
func_1778_call = mutated_mod.get_global_var('func_1778')
call_1828 = relay.TupleGetItem(func_1776_call(), 0)
call_1829 = relay.TupleGetItem(func_1778_call(), 0)
func_1776_call = mod.get_global_var('func_1776')
func_1778_call = mutated_mod.get_global_var('func_1778')
call_1834 = relay.TupleGetItem(func_1776_call(), 1)
call_1835 = relay.TupleGetItem(func_1778_call(), 1)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_1837 = relay.TupleGetItem(func_1454_call(relay.reshape(call_1834.astype('float32'), [100,])), 0)
call_1838 = relay.TupleGetItem(func_1456_call(relay.reshape(call_1834.astype('float32'), [100,])), 0)
uop_1841 = relay.tan(call_1837.astype('float64')) # shape=(2, 4, 1)
uop_1843 = relay.tan(call_1838.astype('float64')) # shape=(2, 4, 1)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_1846 = func_1316_call()
call_1847 = func_1316_call()
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_1848 = relay.TupleGetItem(func_1647_call(), 0)
call_1849 = relay.TupleGetItem(func_1649_call(), 0)
output = relay.Tuple([call_1828,call_1834,uop_1841,call_1846,call_1848,])
output2 = relay.Tuple([call_1829,call_1835,uop_1843,call_1847,call_1849,])
func_1850 = relay.Function([], output)
mod['func_1850'] = func_1850
mod = relay.transform.InferType()(mod)
output = func_1850()
func_1851 = relay.Function([], output)
mutated_mod['func_1851'] = func_1851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_1858 = relay.TupleGetItem(func_1489_call(), 2)
call_1859 = relay.TupleGetItem(func_1490_call(), 2)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_1878 = relay.TupleGetItem(func_1339_call(), 0)
call_1879 = relay.TupleGetItem(func_1341_call(), 0)
uop_1880 = relay.sigmoid(call_1858.astype('float64')) # shape=(2, 4, 1)
uop_1882 = relay.sigmoid(call_1859.astype('float64')) # shape=(2, 4, 1)
output = relay.Tuple([call_1878,uop_1880,])
output2 = relay.Tuple([call_1879,uop_1882,])
func_1891 = relay.Function([], output)
mod['func_1891'] = func_1891
mod = relay.transform.InferType()(mod)
output = func_1891()
func_1892 = relay.Function([], output)
mutated_mod['func_1892'] = func_1892
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1904 = relay.const([[[6.829684,-7.859325,-1.564864,2.180141,7.095681,2.171575,-8.245452],[2.594228,7.185408,4.665942,7.096792,-2.426191,0.616779,7.309105],[9.953901,9.336645,8.738579,-4.065664,8.535139,-7.229377,5.364724]]], dtype = "float64")#candidate|1904|(1, 3, 7)|const|float64
var_1905 = relay.var("var_1905", dtype = "float64", shape = (13, 3, 7))#candidate|1905|(13, 3, 7)|var|float64
bop_1906 = relay.power(const_1904.astype('float64'), var_1905.astype('float64')) # shape=(13, 3, 7)
uop_1910 = relay.sqrt(bop_1906.astype('float32')) # shape=(13, 3, 7)
func_424_call = mod.get_global_var('func_424')
func_428_call = mutated_mod.get_global_var('func_428')
const_1918 = relay.const([[2,-1,4,-3,9,-7,-2],[-9,-1,6,-10,-7,10,3],[7,2,-3,-10,-6,-1,3],[-10,-5,1,6,6,-8,8],[4,-6,7,10,10,10,5],[2,1,2,1,-10,5,-10],[2,1,-1,8,-6,9,10],[-1,-1,4,-5,8,2,-10],[7,-9,9,-4,8,8,10],[-9,9,9,5,3,-10,5],[-10,-10,-6,-3,-1,-3,1],[-5,1,3,-6,-9,6,10],[-3,-1,-1,-8,-9,1,-10],[-1,8,-1,-9,-8,-9,-5],[-6,-4,-1,2,3,6,10],[4,-4,2,2,-10,10,-6],[-2,7,-8,-9,-3,1,-10],[1,-6,4,1,-1,-9,-2],[8,1,10,2,-6,-9,3],[-6,8,-4,2,4,4,-6],[8,-6,-7,10,5,-7,2],[-10,7,9,5,10,3,-3],[-1,2,7,8,4,-3,-10],[10,10,9,7,-1,-1,-2],[-4,1,-3,7,-10,-6,-4],[5,-1,10,-4,9,6,6],[10,4,-2,-3,8,7,-6],[-6,3,-8,4,-6,-6,-2],[4,2,3,-1,-10,1,4],[-8,10,3,-5,8,9,-10],[10,7,-7,1,2,-6,-4],[-10,7,-1,4,-2,4,-8],[5,-6,-9,10,-2,7,-3],[-8,-10,-7,6,5,1,9],[-7,-6,7,9,7,-2,-10],[-4,-2,2,-1,-10,-5,9],[2,1,6,-4,-1,1,-2],[-8,-3,-7,-5,8,6,-4],[-3,-8,10,-4,9,1,1],[-8,6,7,-10,-4,-1,-10],[-8,-9,7,6,9,6,-10],[-7,-1,-3,-3,-6,-5,8],[3,-3,2,2,3,9,-1],[-9,-5,1,-3,5,-7,9],[-3,7,6,-5,-6,-10,-8],[-1,5,10,-6,8,-9,5],[5,-7,-2,-2,-6,9,-7],[-1,7,4,3,3,-6,1],[3,-1,-4,7,-5,-4,-8],[-3,1,10,7,1,-9,-1],[5,-8,10,7,10,-9,4],[5,8,9,-3,9,-2,-2],[-5,5,7,-8,-5,-2,-2],[-7,6,-8,-10,-6,-5,-5],[-5,9,-9,10,8,-4,5],[-5,7,-3,3,-9,-10,8],[-8,-2,7,3,-6,4,2],[-6,-4,-6,-4,-5,-2,-2],[7,-8,10,-10,-3,-4,9],[-2,8,10,10,4,-4,-3],[-3,-1,-4,9,-10,2,3],[2,-8,3,-4,-9,-8,10],[-3,-2,-9,-9,1,8,7],[5,-8,4,-3,1,1,-4],[4,-2,-7,5,7,-9,-4]], dtype = "uint64")#candidate|1918|(65, 7)|const|uint64
call_1917 = relay.TupleGetItem(func_424_call(relay.reshape(const_1918.astype('uint64'), [13, 7, 5]), relay.reshape(const_1918.astype('uint64'), [13, 7, 5]), ), 0)
call_1919 = relay.TupleGetItem(func_428_call(relay.reshape(const_1918.astype('uint64'), [13, 7, 5]), relay.reshape(const_1918.astype('uint64'), [13, 7, 5]), ), 0)
uop_1920 = relay.log10(uop_1910.astype('float64')) # shape=(13, 3, 7)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
var_1923 = relay.var("var_1923", dtype = "float32", shape = (100,))#candidate|1923|(100,)|var|float32
call_1922 = relay.TupleGetItem(func_1454_call(relay.reshape(var_1923.astype('float32'), [100,])), 1)
call_1924 = relay.TupleGetItem(func_1456_call(relay.reshape(var_1923.astype('float32'), [100,])), 1)
func_524_call = mod.get_global_var('func_524')
func_527_call = mutated_mod.get_global_var('func_527')
call_1931 = relay.TupleGetItem(func_524_call(relay.reshape(var_1923.astype('float32'), [4, 5, 5]), relay.reshape(var_1923.astype('float32'), [4, 5, 5]), ), 0)
call_1932 = relay.TupleGetItem(func_527_call(relay.reshape(var_1923.astype('float32'), [4, 5, 5]), relay.reshape(var_1923.astype('float32'), [4, 5, 5]), ), 0)
func_1776_call = mod.get_global_var('func_1776')
func_1778_call = mutated_mod.get_global_var('func_1778')
call_1936 = relay.TupleGetItem(func_1776_call(), 2)
call_1937 = relay.TupleGetItem(func_1778_call(), 2)
func_1017_call = mod.get_global_var('func_1017')
func_1020_call = mutated_mod.get_global_var('func_1020')
const_1942 = relay.const([-0.717056,2.866526,-7.115764,-8.355264,1.119719,0.474027,1.100221,-6.493323,5.905201,8.040515,2.742057,-6.057810,9.591652,-3.777513,8.057394,-7.506975,-4.565079,-7.508407,-6.130281,5.812898,9.433737,-9.148579,4.594545,0.733312,7.129201,0.793696,-9.244565,-0.064395,3.697024,-6.062876,-4.022792,-9.189229,-3.533872,6.212504,9.706252,5.764422,8.282215,-4.853894,-1.884890,-8.910138,-2.108040,-8.881528,1.125968,5.051714,1.151940,5.649992,-7.990052,-8.798875,-6.705399,-7.924910,-7.370893,6.947529,6.502131,7.683110,8.772341,1.301174,4.707952,-3.597161,-0.260762,5.355360,-1.993569,-2.090500,-3.886336,3.704784,-2.945988,-6.933016,1.101810,3.407170,9.978411,-9.123984,-2.227828,8.068697,1.871716,-1.659204,5.252225,4.144587,9.000506,-4.375500,3.667936,-1.345711,1.699918,-2.914382,-9.150025,3.325250,-6.202077,-6.901293,-9.444480,-9.267569,-7.274044,4.074403,-9.479934,3.320921,-2.741039,1.347219,4.771885,-4.081836,7.113972,-1.735132,-8.458526,8.943753,1.081366,1.021935,4.026316,-0.467773,-2.721899,5.792673,-4.444611,-5.606630,1.797202,-2.165015,-2.393255,3.623381,-7.963157,3.024957,-6.149109,3.716570,3.115791,3.649101,9.550780,-1.944760,3.920535,-4.708217,-9.092269,1.938712,1.066238,-8.627014,-1.008499,1.236943,1.675934,2.106357,3.171153,-2.535673,3.423416,-2.076535,8.047870,-7.219293,-1.876314,-3.789517,-0.468018,-7.468133,-8.970926,6.815287,3.957324,2.671816,6.808122,-3.381915,3.131010,3.230586,-8.727474,3.425648,-9.357707,-0.676345,8.480009,3.179369,-0.079712,3.289996,3.072918,7.787599,3.298768,9.435975,4.528942,0.390238,-1.358009,6.537662,-6.745975,-9.594107,8.812246,-3.688117,-9.057951,-8.303301,9.099575,5.324320,-7.096547,0.382193,8.596969,-4.686279,-7.238258,5.265158,0.971338,1.795801], dtype = "float32")#candidate|1942|(180,)|const|float32
call_1941 = relay.TupleGetItem(func_1017_call(relay.reshape(const_1942.astype('float32'), [3, 15, 4])), 0)
call_1943 = relay.TupleGetItem(func_1020_call(relay.reshape(const_1942.astype('float32'), [3, 15, 4])), 0)
func_1415_call = mod.get_global_var('func_1415')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_1952 = relay.TupleGetItem(func_1415_call(), 3)
call_1953 = relay.TupleGetItem(func_1417_call(), 3)
func_1017_call = mod.get_global_var('func_1017')
func_1020_call = mutated_mod.get_global_var('func_1020')
call_1963 = relay.TupleGetItem(func_1017_call(relay.reshape(call_1941.astype('float32'), [3, 15, 4])), 0)
call_1964 = relay.TupleGetItem(func_1020_call(relay.reshape(call_1941.astype('float32'), [3, 15, 4])), 0)
func_424_call = mod.get_global_var('func_424')
func_428_call = mutated_mod.get_global_var('func_428')
call_1965 = relay.TupleGetItem(func_424_call(relay.reshape(call_1917.astype('uint64'), [13, 7, 5]), relay.reshape(call_1917.astype('uint64'), [13, 7, 5]), ), 0)
call_1966 = relay.TupleGetItem(func_428_call(relay.reshape(call_1917.astype('uint64'), [13, 7, 5]), relay.reshape(call_1917.astype('uint64'), [13, 7, 5]), ), 0)
func_1559_call = mod.get_global_var('func_1559')
func_1563_call = mutated_mod.get_global_var('func_1563')
const_1969 = relay.const([8,5,7,2,-5,-9,3,-7,4,6,9,-1,3,6,-5,10,-2,-1,-2,4,8,-2,-9,-3,-9,3,9,6,3,-7,4,6,-4,-4,8,4,1,8,-4,-3,10,-2,9,-4,-7,-5,-10,-6,5,-1,-10,-10,10,3,9,-1,-9,1,-1,4,-5,1,-7,-10,-1,-7,5,-3,5,2,-9,4,-6,-10,7,-6,-3,8,4,-4,8,-5,9,1,-4,-10,6,1,-9,10,6,-10,3,-1,-3,-1,6,-5,5,-3,-9,-2,-6,-10,5,-5,-5,10,-1,4,-3,7,4,8,-10,-8,3,7,-2,-6,-6,-6,4,-9,-4,-10,-2,10,-3,-5,9,-3,3,2,6,10,9,-2,-3,-9,-6,8,8,-3,-6,5,4,-8,7,-2,-7,4,10,8,-7,-10,8,10,-6,8,-5,-9,-10,-6,6,9,-10,-9,6,-4,6,5,-4,1,-2,-3,-3,-6,7,9,7,7,8,-8,5,9,-7,-7,-1,-2,9,-10,8,-5,-5,8,-2,-1,-3,7,2,3,-2,2,-1,6,10,4,9,2,-4,8,-7,8,-10,10,-1,-3,3,6,-10,6,10,7,-9,-5,-9,-9,-4,6,2,-7,-9,7,8,6,8,9,9,-7,-2,1,7,-8,7,-4,2,-1,2,2,1,-9,9,-7,1,-7,8,6,8,-4,-8,3,10,10,1,-3,10,-1,9,7,4,2,-4,5,2,8,-10,1,-4,-5,3,-7,-9,3,-6,7,-6,2,-7,1,-8,1,-1,-9,3,2,-1,10,9,7,4,7,-5,10,-6,3,-2,-2,-5,10,3,4,2,4,-7,-7,9,1,-3,-7,-1,-2,3,8,5,7,-9,-1,-5,2,-10,-3,3,2,-4,-4,7,10,10,-9,-5,2,-7,6,-2,4,-7,10,2,7,-2,10,7,-1,-5,1,-9,5,9,-8,10,-4,10,1,7,7,-1,9,5,6,-4,-4,-3,9,-10,5,-2,9,5,5,9,1,6,-9,-4,5,-3,9,7,10,-6,7,3,9,7,-10,-5,-8,3,-4,-2,4,-7,3,-2,1,-7,-5,6,6,7,2,7,3,-5,6,5,5,3,-5,-3,3,5,-8,-2,-4,2,-3,6,-10,4,-10,-8,-2,-5,5,3,5,8,9,-2,10,-9,-3,-10,5,9,-2,2,-9,1,4,4,10,-7,-1,-1,10,-4,4,8,-8,7,-5,2,-6,7,-6,1,2,-4,6,-4,7,1,-1,-1,5,9,-6,3,-5,-2,-1,5,-1,-6,6,3,-7,-5,3,-9,5,-8,10,-3,-10,-4,-7,6,-9,5,2,9,4,10,-9,4,7,-4,-3,-10,1,-8,4,-10,-4,-8,-5,-6,10,-4,4,-4,-4,-8,5,-2,1,-9,-1,7,4,-4,2,-7,5,-3,3,-8,4,-4,3,9,5,8,-9,-5,-2,-3,8,-7,5,-10,7,-5,-5,4,-6], dtype = "uint64")#candidate|1969|(560,)|const|uint64
call_1968 = relay.TupleGetItem(func_1559_call(relay.reshape(const_1969.astype('uint64'), [7, 16, 5]), relay.reshape(const_1969.astype('uint64'), [7, 16, 5]), ), 0)
call_1970 = relay.TupleGetItem(func_1563_call(relay.reshape(const_1969.astype('uint64'), [7, 16, 5]), relay.reshape(const_1969.astype('uint64'), [7, 16, 5]), ), 0)
func_524_call = mod.get_global_var('func_524')
func_527_call = mutated_mod.get_global_var('func_527')
call_1975 = relay.TupleGetItem(func_524_call(relay.reshape(var_1923.astype('float32'), [4, 5, 5]), relay.reshape(call_1952.astype('float32'), [4, 5, 5]), ), 0)
call_1976 = relay.TupleGetItem(func_527_call(relay.reshape(var_1923.astype('float32'), [4, 5, 5]), relay.reshape(call_1952.astype('float32'), [4, 5, 5]), ), 0)
uop_1992 = relay.tan(uop_1920.astype('float64')) # shape=(13, 3, 7)
func_1776_call = mod.get_global_var('func_1776')
func_1778_call = mutated_mod.get_global_var('func_1778')
call_2001 = relay.TupleGetItem(func_1776_call(), 2)
call_2002 = relay.TupleGetItem(func_1778_call(), 2)
bop_2003 = relay.logical_and(uop_1920.astype('bool'), relay.reshape(bop_1906.astype('bool'), relay.shape_of(uop_1920))) # shape=(13, 3, 7)
bop_2006 = relay.maximum(bop_2003.astype('uint32'), relay.reshape(uop_1920.astype('uint32'), relay.shape_of(bop_2003))) # shape=(13, 3, 7)
output = relay.Tuple([call_1917,const_1918,call_1922,var_1923,call_1931,call_1936,call_1941,const_1942,call_1952,call_1963,call_1965,call_1968,const_1969,call_1975,uop_1992,call_2001,bop_2006,])
output2 = relay.Tuple([call_1919,const_1918,call_1924,var_1923,call_1932,call_1937,call_1943,const_1942,call_1953,call_1964,call_1966,call_1970,const_1969,call_1976,uop_1992,call_2002,bop_2006,])
func_2011 = relay.Function([var_1905,var_1923,], output)
mod['func_2011'] = func_2011
mod = relay.transform.InferType()(mod)
mutated_mod['func_2011'] = func_2011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2011_call = mutated_mod.get_global_var('func_2011')
var_2013 = relay.var("var_2013", dtype = "float64", shape = (13, 3, 7))#candidate|2013|(13, 3, 7)|var|float64
var_2014 = relay.var("var_2014", dtype = "float32", shape = (100,))#candidate|2014|(100,)|var|float32
call_2012 = func_2011_call(var_2013,var_2014,)
output = call_2012
func_2015 = relay.Function([var_2013,var_2014,], output)
mutated_mod['func_2015'] = func_2015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_2020 = relay.TupleGetItem(func_1489_call(), 1)
call_2021 = relay.TupleGetItem(func_1490_call(), 1)
func_809_call = mod.get_global_var('func_809')
func_812_call = mutated_mod.get_global_var('func_812')
const_2028 = relay.const([-9.007498,8.817208,-6.768728,-8.727894,-4.184459,-3.496907,2.144062,-0.323523,6.306748,7.041329,-6.625327,5.853187,-5.245678,8.167649,7.499302,-2.654974,0.270754,5.351190,2.601261,0.076462,-2.601827,-2.005804,0.662959,0.135639,7.671915,-4.686202,4.569016,3.929629,-3.647767,-6.608510,9.714226,6.182546,-1.064107,-5.646963,-5.754103,8.980263,-4.690090,-6.435853,4.695463,-9.133589,6.740368,-1.455977,-3.361887,-4.877484,-9.534494,-0.978361,1.230767,5.283874,8.261486,-2.856749,1.735838,-8.735041,4.765097,9.253474,-9.837133,-7.247828,3.097329,-2.071780,-3.723881,-4.192484,6.243719,-5.207043,5.186184,-8.588851,-2.141500,-6.504162,7.010031,9.851055,-2.707648,3.314602,-1.767751,-4.845849,-7.540467,-2.807628,1.783122,-8.555386,5.861499,-0.472197,-8.463879,7.120972,3.563333,-4.391955,-7.821419,3.805085,-6.812179,0.465166,-2.653715,-3.871151,3.319242,5.121830,-7.392133,7.666697,3.039425,-7.081111,3.200834,-2.269450,7.205028,1.140911,-7.653511,-3.680052,4.204127,0.097798,9.173323,-5.489668,-4.645390,-4.363347,0.028033,0.172797,1.897285,-9.129601,7.554066,6.875617,7.167574,3.989236,2.693046,5.602130,1.718376,1.613191,-6.204672,5.652438,7.859083,0.661967,-8.937657,9.182830,-9.171551,-6.624896,-1.334495,3.477159,-8.720945,5.332093,-2.711439,-8.894866,-0.219260,9.671639,2.113068,8.025683,-3.420210,-7.758960,8.368970,-0.016999,4.458917,-8.159311,-0.216101,-8.735650,-5.587002,-1.038997,-2.837414,-1.400663,-2.695064,0.639239,3.615556,8.214820,-8.968915,-6.578374,5.342081,7.226935,2.529425,0.263289,9.483134,-3.106522,4.715489,7.461118,0.221472,-4.272798,2.078900,9.527150,2.408205,-2.582374,-4.902078,2.228567,2.800969,8.961983,-8.187842,-2.903533,-8.715257,5.398850,7.020381,8.805523,3.312828,7.469597,0.390534,4.542126,8.642884,-2.746157,-5.601588,6.385432,0.540185,-1.607880,3.895713,7.903391,4.988360,-6.277524,4.579945,8.927809,4.870846,6.819609,7.513713,3.288291,-2.033875,6.857156,-8.862887,-1.978387,8.005743,1.793589,0.315064,-5.671037,-0.367921,-7.883326,-2.403695,-9.541047,-2.695621,-4.109407,-4.270896,-6.073574,-8.314268,4.997932,-9.188306,-0.308188,-4.511906,6.034738,-2.423598,-7.258277,-2.602295,3.072064,-0.522795,-0.537037,4.073610,-6.043396,3.483753,8.461744,-6.965832,-4.557605,-4.772859,-9.254517,-8.644986,3.935731,4.832322,7.541145,-3.092453,-5.685382,-4.025448,2.746560,-0.984057,9.904232,-0.231924,7.919155,3.512732,5.342096,-5.565360,-8.939512,1.718810,1.875826,0.280275,-5.114087,7.842715,-3.745574,-8.573609,-0.726745,-4.970134,-4.862335,-3.127130,6.763156,7.672021,0.447469,2.184810,-3.757779,2.634164,4.633940,8.571978,-0.387612,9.926534,-5.408977,-4.314161,-1.964414,7.490474,3.732893,-7.389350,7.319909,-2.489640,4.457555,1.588635,-7.814698,7.566319,6.842941,-3.709816,-4.572353,5.579324,5.252947,8.059753,-6.971230,-0.835472,-5.127582,-9.368998,-1.355816,-7.026072,-2.181721,1.501671,6.069323,9.681811,5.942220,-8.310682,0.016949,3.848284,-8.674783,-0.476337,9.823240,-6.782583,4.456892,3.454447,8.172631,2.399111,9.791222,7.721096,9.532858,-6.645794,-3.555892,-3.257662,-5.572474,-2.114603,-7.406681,6.147036,1.067205,5.169456,-2.159709,-2.429378,6.719272,-3.232124,-2.382764,4.959984,-8.957955,8.207572,-0.773716,-9.274378,0.434666,1.701269,4.059669,8.061627,7.492486,0.625118,1.447392,7.693973,3.630935,-1.996726,4.326356,5.691433,7.423708,-5.550824,9.525928,-2.828024,7.022788,-3.875291,-8.858234,1.584154,6.332812,3.211601,-7.516044,4.810859,-7.316488,-8.268032,3.762208,0.520989,-8.447302,-0.455068,-8.390246,-3.558382,8.915533,-0.445354,-7.622524,4.286118,-5.872293,-2.726748,2.093616,-8.510376,0.559321,-4.061835,2.191500,5.616389,5.657132,3.795640,-3.999843,-6.167657,-6.277465,6.281636,-7.640077,-3.979583,-5.925592,-1.268973,-6.770471,4.156352,7.473183,-7.533083,-3.587489,-9.895458,-5.409871,2.525636,0.504721,-7.152533,9.409941,-5.542876,-9.193533,-4.512186,3.315342,-8.598210,-9.345309,-5.255019,8.063580,-1.013186,-6.767254,-0.519625,-5.674901,-9.705882,2.437736,1.104716,-0.536855,-2.176859,6.124388,1.352306,9.589935,-1.386602,-2.522497,2.934840,-2.760370,2.875992,-5.616668,1.771820,0.797415,-6.853580,-3.762906,2.620226,1.877454,8.745145,1.258085,-1.815708,-1.129005,-2.816767,7.129150,1.998401,9.206564,-0.046452,-1.980063,-9.398701,2.758151,-5.810138,-7.445210,9.064693,8.672260,-2.058352,8.698681,-2.571619,-8.559002,-7.576537,-8.780328,4.466392,-2.475568,-0.797574,3.491043,7.067996,7.175992,-0.530477,5.101658,-5.422883,-3.548462,3.109005,2.454507,0.895056,-9.662894,4.455599,7.308703,-1.644945,-5.384348,-9.566937,4.331184,8.925705,4.121118,3.192961,5.524682,-1.208893,-5.304151,9.621074,9.399214,3.157406,9.834675,-5.308758,4.580720,-5.665029,2.556802,7.590064,-8.942170,-0.288555,-8.401600,0.002782,8.446072,3.929467,7.789446,1.322579,-4.119267,6.044241,1.998656,-3.123986,-1.058237,-3.619520,-1.472784,6.080096,-1.237076,-2.704557,6.285760,-9.302373,4.785288,-7.560466,2.140997,8.645160,3.081404,6.271524,6.230008,5.506970,-0.197097,4.729186,-2.051154,-2.935054,-4.356202,1.722482,-7.393599,-2.004917,-3.319065,-4.663746,-7.235065,4.099531,-4.585349,-5.505542,-4.694946,-1.451771,-8.360101,6.769479,-9.013851,8.579950,8.822484,-6.098612,4.446132,1.759795,2.251215,9.763812,-8.995532,1.455249,3.848233,-1.130877,-4.275637,-4.237456,-2.533725,9.502789,9.407846,-1.798378,5.104349,-7.786479,8.895062,-5.502699,-1.002008,7.342008,-2.786304,4.270324,-0.346178,-7.194026,-5.101307,7.021702,-2.900067,6.542645,-2.114844,-1.650494,-7.517513,-1.658838,6.012696,1.251892,-5.859919,-8.955157,8.102806,-1.512098,2.247736,-9.992996,4.131558,-8.925859,-2.942299,-1.217596,1.534358,7.187479,6.106915,-1.657186,-6.236799,-2.385083,-3.177925,-4.281178,8.197946,2.995890,0.996083,-5.505124,-9.892937,-8.346208,1.606162,0.055697,-8.657354,-3.722646,-3.319314,-9.854413,-1.608681,0.288916,4.065703,6.462602,-0.533385,6.984412,-4.957342,-9.767655,-9.166933,-8.360857,2.790327,7.498959,-2.394879,-2.885702,-0.608272,8.060527,5.424983,8.701626,-5.797389,7.740347,0.243087,-2.024681,3.427568,-2.335282,-5.055033,9.285783,-5.862693,2.945094,-6.212808,6.798266,-1.408188,-9.101274,9.341173,-9.261763,-0.609099,-4.074756,-0.489014,6.451716,-5.763736,5.601165,-4.406653,-0.741885,1.722490,1.901109,1.550365,-7.997336,-5.532205], dtype = "float32")#candidate|2028|(648,)|const|float32
call_2027 = relay.TupleGetItem(func_809_call(relay.reshape(const_2028.astype('float32'), [9, 9, 8])), 0)
call_2029 = relay.TupleGetItem(func_812_call(relay.reshape(const_2028.astype('float32'), [9, 9, 8])), 0)
output = relay.Tuple([call_2020,call_2027,const_2028,])
output2 = relay.Tuple([call_2021,call_2029,const_2028,])
func_2030 = relay.Function([], output)
mod['func_2030'] = func_2030
mod = relay.transform.InferType()(mod)
output = func_2030()
func_2031 = relay.Function([], output)
mutated_mod['func_2031'] = func_2031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_2062 = relay.TupleGetItem(func_1647_call(), 2)
call_2063 = relay.TupleGetItem(func_1649_call(), 2)
const_2065 = relay.const([[1.397925,9.494542,-7.756688,5.868678],[3.336569,-2.860747,-3.695059,-4.384073],[9.210120,-0.866949,5.625433,7.720464],[-7.076257,-3.387009,-3.592310,3.347398],[3.624098,4.626509,3.140884,-9.066428],[5.072401,2.957555,-0.729881,2.008478],[7.814302,-7.260321,6.952259,3.195081],[-1.151506,-7.275693,1.194827,-4.289455],[-4.747678,2.772753,-2.171735,-3.308042],[-9.798930,-1.474756,8.061151,7.962584],[5.404587,8.769210,6.792658,-0.824176],[7.201121,-1.532160,5.442127,1.929045],[-1.385046,1.594132,-5.463756,-3.691235],[1.949204,0.620163,-1.146271,5.348493],[-5.772100,7.225156,6.025183,-9.522697],[-8.363596,-5.000777,9.414160,4.176380],[-2.493526,5.621524,8.721840,2.404252],[-7.286557,6.673912,7.569254,-2.847867],[-8.281872,1.786696,-7.132044,-7.365805],[2.509072,-6.819304,-3.102966,-5.176441],[-2.206170,-7.886170,-9.945539,-3.472825],[-8.387337,4.355481,-5.775559,-9.045233],[4.714681,-7.322456,2.423347,-6.499928],[3.388697,7.284321,2.235040,-4.452788],[1.546588,2.279591,8.189068,-6.828663]], dtype = "float32")#candidate|2065|(25, 4)|const|float32
bop_2066 = relay.mod(call_2062.astype('float64'), relay.reshape(const_2065.astype('float64'), relay.shape_of(call_2062))) # shape=(25, 4)
bop_2069 = relay.mod(call_2063.astype('float64'), relay.reshape(const_2065.astype('float64'), relay.shape_of(call_2063))) # shape=(25, 4)
output = bop_2066
output2 = bop_2069
func_2074 = relay.Function([], output)
mod['func_2074'] = func_2074
mod = relay.transform.InferType()(mod)
mutated_mod['func_2074'] = func_2074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2074_call = mutated_mod.get_global_var('func_2074')
call_2075 = func_2074_call()
output = call_2075
func_2076 = relay.Function([], output)
mutated_mod['func_2076'] = func_2076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2074_call = mod.get_global_var('func_2074')
func_2076_call = mutated_mod.get_global_var('func_2076')
call_2126 = func_2074_call()
call_2127 = func_2074_call()
func_2074_call = mod.get_global_var('func_2074')
func_2076_call = mutated_mod.get_global_var('func_2076')
call_2144 = func_2074_call()
call_2145 = func_2074_call()
func_2030_call = mod.get_global_var('func_2030')
func_2031_call = mutated_mod.get_global_var('func_2031')
call_2148 = relay.TupleGetItem(func_2030_call(), 2)
call_2149 = relay.TupleGetItem(func_2031_call(), 2)
var_2165 = relay.var("var_2165", dtype = "float64", shape = (25, 4))#candidate|2165|(25, 4)|var|float64
bop_2166 = relay.greater_equal(call_2144.astype('bool'), relay.reshape(var_2165.astype('bool'), relay.shape_of(call_2144))) # shape=(25, 4)
bop_2169 = relay.greater_equal(call_2145.astype('bool'), relay.reshape(var_2165.astype('bool'), relay.shape_of(call_2145))) # shape=(25, 4)
func_1089_call = mod.get_global_var('func_1089')
func_1093_call = mutated_mod.get_global_var('func_1093')
var_2174 = relay.var("var_2174", dtype = "int32", shape = (135,))#candidate|2174|(135,)|var|int32
call_2173 = relay.TupleGetItem(func_1089_call(relay.reshape(var_2174.astype('int32'), [3, 9, 5]), relay.reshape(var_2174.astype('int32'), [3, 9, 5]), ), 1)
call_2175 = relay.TupleGetItem(func_1093_call(relay.reshape(var_2174.astype('int32'), [3, 9, 5]), relay.reshape(var_2174.astype('int32'), [3, 9, 5]), ), 1)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_2176 = relay.TupleGetItem(func_1454_call(relay.reshape(call_2126.astype('float32'), [100,])), 1)
call_2177 = relay.TupleGetItem(func_1456_call(relay.reshape(call_2126.astype('float32'), [100,])), 1)
func_2011_call = mod.get_global_var('func_2011')
func_2015_call = mutated_mod.get_global_var('func_2015')
var_2186 = relay.var("var_2186", dtype = "float64", shape = (39, 7))#candidate|2186|(39, 7)|var|float64
call_2185 = relay.TupleGetItem(func_2011_call(relay.reshape(var_2186.astype('float64'), [13, 3, 7]), relay.reshape(call_2176.astype('float32'), [100,]), ), 7)
call_2187 = relay.TupleGetItem(func_2015_call(relay.reshape(var_2186.astype('float64'), [13, 3, 7]), relay.reshape(call_2176.astype('float32'), [100,]), ), 7)
uop_2194 = relay.sin(call_2126.astype('float32')) # shape=(25, 4)
uop_2196 = relay.sin(call_2127.astype('float32')) # shape=(25, 4)
output = relay.Tuple([call_2148,bop_2166,call_2173,var_2174,call_2176,call_2185,var_2186,uop_2194,])
output2 = relay.Tuple([call_2149,bop_2169,call_2175,var_2174,call_2177,call_2187,var_2186,uop_2196,])
func_2201 = relay.Function([var_2165,var_2174,var_2186,], output)
mod['func_2201'] = func_2201
mod = relay.transform.InferType()(mod)
mutated_mod['func_2201'] = func_2201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mutated_mod.get_global_var('func_2201')
var_2203 = relay.var("var_2203", dtype = "float64", shape = (25, 4))#candidate|2203|(25, 4)|var|float64
var_2204 = relay.var("var_2204", dtype = "int32", shape = (135,))#candidate|2204|(135,)|var|int32
var_2205 = relay.var("var_2205", dtype = "float64", shape = (39, 7))#candidate|2205|(39, 7)|var|float64
call_2202 = func_2201_call(var_2203,var_2204,var_2205,)
output = call_2202
func_2206 = relay.Function([var_2203,var_2204,var_2205,], output)
mutated_mod['func_2206'] = func_2206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_2217 = func_1316_call()
call_2218 = func_1316_call()
output = relay.Tuple([call_2217,])
output2 = relay.Tuple([call_2218,])
func_2238 = relay.Function([], output)
mod['func_2238'] = func_2238
mod = relay.transform.InferType()(mod)
output = func_2238()
func_2239 = relay.Function([], output)
mutated_mod['func_2239'] = func_2239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_2248 = relay.TupleGetItem(func_1850_call(), 2)
call_2249 = relay.TupleGetItem(func_1851_call(), 2)
output = call_2248
output2 = call_2249
func_2250 = relay.Function([], output)
mod['func_2250'] = func_2250
mod = relay.transform.InferType()(mod)
mutated_mod['func_2250'] = func_2250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2250_call = mutated_mod.get_global_var('func_2250')
call_2251 = func_2250_call()
output = call_2251
func_2252 = relay.Function([], output)
mutated_mod['func_2252'] = func_2252
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2309 = relay.var("var_2309", dtype = "float64", shape = (13, 10, 5))#candidate|2309|(13, 10, 5)|var|float64
uop_2310 = relay.sinh(var_2309.astype('float64')) # shape=(13, 10, 5)
output = relay.Tuple([uop_2310,])
output2 = relay.Tuple([uop_2310,])
func_2315 = relay.Function([var_2309,], output)
mod['func_2315'] = func_2315
mod = relay.transform.InferType()(mod)
mutated_mod['func_2315'] = func_2315
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2316 = relay.var("var_2316", dtype = "float64", shape = (13, 10, 5))#candidate|2316|(13, 10, 5)|var|float64
func_2315_call = mutated_mod.get_global_var('func_2315')
call_2317 = func_2315_call(var_2316)
output = call_2317
func_2318 = relay.Function([var_2316], output)
mutated_mod['func_2318'] = func_2318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2074_call = mod.get_global_var('func_2074')
func_2076_call = mutated_mod.get_global_var('func_2076')
call_2346 = func_2074_call()
call_2347 = func_2074_call()
func_2315_call = mod.get_global_var('func_2315')
func_2318_call = mutated_mod.get_global_var('func_2318')
const_2355 = relay.const([6.922078,7.706915,1.038522,4.459343,-3.052049,9.375541,0.812700,-9.386617,-6.814061,-4.345498,6.440845,-6.889479,8.622284,-5.097654,-1.168375,6.121585,-3.758153,7.147964,0.338233,9.976028,1.902538,-0.059955,5.150372,-5.276236,5.535273,5.187547,1.665528,-2.992023,-5.590983,8.208698,2.271616,-5.877338,4.202311,8.057028,-7.133196,-7.651596,-3.249714,9.812084,0.199233,2.970861,-6.187969,2.438778,-0.324993,-5.324881,4.069844,6.121671,4.801336,-2.230814,-9.221108,4.077234,-6.383885,-8.328761,2.748180,1.035083,1.400413,1.217371,7.362891,3.417063,4.936622,1.939995,4.350912,1.723004,-7.815610,-3.002384,-4.516064,-0.598184,9.116681,8.450859,-6.815929,-8.830124,0.806822,2.063614,-4.112012,6.061057,7.984199,-6.943366,5.289528,6.960062,-4.869177,-9.058171,4.284981,0.085803,5.070199,6.846201,9.830100,-2.246791,-3.445756,-9.925526,-6.246427,-5.199560,-4.829705,9.253356,-2.081860,7.329069,-9.802629,9.318633,-5.398297,-4.075229,9.856859,6.810250,9.620491,-4.510670,-8.469313,9.407217,-3.806509,-0.530728,-9.919572,-4.691689,-3.568976,6.132718,-8.041079,-8.156604,-3.313985,-7.603862,9.520365,-9.503256,6.286111,-3.297876,9.243440,9.959421,0.625736,-3.244363,2.191964,-3.979096,3.556740,-3.253111,6.874304,-6.372676,1.334974,3.503720,4.072131,-5.240277,-5.943737,-9.904272,-0.980496,0.228177,6.655976,3.692550,7.852335,-5.190170,-1.635683,-9.303830,8.406073,6.979660,6.386834,6.150308,-2.883545,-5.141745,-6.680435,9.183034,-9.692743,-1.593292,-5.348108,-4.511419,-5.998785,-9.770459,0.317477,-1.220407,-5.752490,5.482596,-2.910057,-4.691633,-9.313075,-8.405391,4.447569,1.011322,-4.732315,9.929026,-7.929751,-0.800489,-9.737997,5.722670,9.639159,-7.928038,2.996147,-6.584142,8.177470,-8.343597,6.043121,-3.575108,-7.641918,-1.388036,-9.470722,-3.838449,6.088289,9.295379,7.283935,1.011936,-7.489205,-6.473231,6.696783,3.513268,1.782268,0.414794,-0.063022,3.394655,4.644170,-6.978284,5.756973,-8.819247,7.113764,-9.985979,-5.180594,-7.300840,-5.099994,-5.394377,5.813596,-1.947669,-0.072415,9.909330,8.615181,1.423945,-5.774331,-6.601414,-7.083858,-8.651422,-0.022927,9.619044,-7.337529,1.693316,-8.184207,-4.414152,-5.241300,9.986409,-5.097034,1.418836,3.997295,8.071921,-9.179333,-5.381847,-8.782061,9.690041,0.791362,-3.858066,-1.665991,-9.336671,2.927034,-0.865957,3.256002,-9.310833,-9.349588,-9.397099,0.705965,1.524685,8.707452,-2.987887,-2.234387,2.140669,-3.528522,9.310512,0.717529,-3.887184,-1.040290,-7.479688,-2.331709,-5.121798,7.794162,-4.656156,-2.555838,-6.396114,2.195114,4.579620,-3.135640,-5.884905,-3.453650,8.364177,7.060504,2.005022,-6.367868,-6.877102,-1.858593,8.497709,5.856133,-4.797294,9.141385,2.258910,-1.452745,-6.746300,7.522710,0.527588,-2.094888,-2.888211,-0.347401,-9.805810,1.150231,3.192874,5.070489,6.792419,4.405980,-3.232305,8.538450,7.812908,-9.501290,-8.809067,-9.189962,-3.975978,1.380804,3.196929,-0.716880,-1.729245,-2.907376,4.601949,7.414046,-9.976048,9.996926,7.192825,-4.040026,-8.218182,4.759206,2.511871,-7.443719,-4.717963,-1.339669,-7.312934,7.396944,-6.568020,-5.691099,3.743785,9.541378,-5.270197,-1.532896,5.193524,0.148700,-5.193313,-1.894965,-3.487778,7.725334,-1.800395,-6.274297,-2.742716,-3.698222,4.519614,-9.929603,-9.617306,-0.783134,-6.927784,-6.874386,-1.248355,4.668651,-0.332749,-9.234566,2.991228,-9.641724,4.533669,-1.041769,-3.029170,-3.202457,3.653534,4.735397,-0.725031,7.298275,-8.943193,-0.710185,4.478867,3.009207,-7.884497,-5.185978,5.426315,0.002707,-2.180625,-6.773217,-3.591360,-9.646550,-2.510150,5.146705,-8.756435,6.156923,3.389468,9.633496,-6.147677,-6.787666,-4.573745,-6.717774,1.626957,-5.427322,5.463850,6.437393,7.864987,3.516767,2.436584,0.009198,6.640055,-6.969171,-9.830410,3.060479,5.933190,9.670208,2.819052,4.303362,-4.482678,-7.620495,9.558443,7.924691,6.971002,-6.163244,-1.584788,-2.139221,-7.003918,-9.971083,-6.047746,8.936139,1.098323,0.831778,-7.405438,-0.798108,-2.308400,-8.821664,-6.273281,4.229952,7.873663,-0.332534,8.931492,5.752929,2.514201,-6.042554,-8.711716,9.178078,7.145263,-6.054199,-9.599977,-7.778364,0.554171,-0.647374,-2.028742,6.431242,0.040333,1.614021,3.405624,-8.849403,-2.294762,-3.641874,9.211156,3.720146,7.960158,-2.369592,-8.884929,-2.544593,-4.127271,4.037350,-7.689961,-5.476534,-9.747497,-7.744853,-4.836138,-9.072635,-0.802201,1.082879,6.070309,-0.079909,-1.211120,-3.945818,1.363542,-5.083984,3.069803,-7.466948,0.764526,0.349740,5.469609,5.386309,-5.815797,-1.928364,-1.180133,-0.815129,-8.342519,-4.189860,-6.973325,8.144481,-5.649298,5.585812,7.071094,0.836176,-3.969679,-3.135748,2.811054,5.976960,-1.653568,-5.664694,-2.418123,-1.689005,0.535927,7.040614,3.017634,2.530791,7.665034,5.916147,-0.963380,5.343919,4.513335,-7.016799,4.699155,-9.708400,-3.589503,-3.299325,-6.552586,4.506085,-3.188561,4.533332,-5.770513,7.683171,4.241371,-7.291102,9.468136,-5.418170,-3.583628,3.204006,-1.372327,8.843606,-0.097846,2.989004,-8.414519,-3.111760,-9.479486,-1.657130,-5.957501,-5.262720,-1.721216,-3.027665,-7.549360,-4.506789,1.899233,-1.868159,8.536445,-9.185725,0.477311,-8.046968,3.333917,-0.501888,-2.108535,-5.803334,-4.191148,-0.252996,5.397455,0.528801,1.761153,-9.096825,3.665615,0.458060,-7.266272,9.286956,6.630418,3.252156,-2.702047,-4.745494,-9.746435,-8.500864,6.672953,3.803267,1.299250,-8.459359,-7.501045,9.233861,5.844017,7.154323,8.865295,-7.173767,-7.701155,7.889531,5.240967,-4.501799,-8.399277,2.896637,3.457470,-2.710476,8.055487,-5.431015,-6.836514,0.491861,-5.159254,8.564313,5.300301,-9.123939,-9.508293,3.976452,-2.363062,0.909206,-7.375408,-3.831072,-8.149884,-6.528667,-7.189896,2.097359,-9.640235,-9.422715,9.935856,-9.486983,0.651962,1.205965,-5.272194,-1.862215,-4.147493,6.143404,-1.093364,-6.938886,5.319204,-1.051577,1.063724,-1.434537,-1.651051,-9.107258,-9.834605,0.877251,-5.091768,8.089199,0.252386,6.464902,-5.446764,-8.106644,-5.141560,9.457046,5.873540,0.020170,6.464132,-9.339747,9.093935,-8.515246,-9.304833,6.848955,-5.310576,4.414689,-5.322566,6.286723,-3.995275,5.440266,-1.611687,-7.233436,-4.083032,5.462279,1.895242,-7.691693,-1.918007,-8.606878,-6.737269,8.034970,4.473662,-3.658552,0.694967,-0.541543,3.497834,5.463950,-9.359613,6.984229,5.244391,-7.799712,-3.685778,3.435273,6.641465,5.549310,-5.330985,-4.595079,-4.130708], dtype = "float64")#candidate|2355|(650,)|const|float64
call_2354 = relay.TupleGetItem(func_2315_call(relay.reshape(const_2355.astype('float64'), [13, 10, 5])), 0)
call_2356 = relay.TupleGetItem(func_2318_call(relay.reshape(const_2355.astype('float64'), [13, 10, 5])), 0)
output = relay.Tuple([call_2346,call_2354,const_2355,])
output2 = relay.Tuple([call_2347,call_2356,const_2355,])
func_2357 = relay.Function([], output)
mod['func_2357'] = func_2357
mod = relay.transform.InferType()(mod)
output = func_2357()
func_2358 = relay.Function([], output)
mutated_mod['func_2358'] = func_2358
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2365 = relay.var("var_2365", dtype = "uint16", shape = (14, 6, 7))#candidate|2365|(14, 6, 7)|var|uint16
var_2366 = relay.var("var_2366", dtype = "uint16", shape = (14, 6, 7))#candidate|2366|(14, 6, 7)|var|uint16
bop_2367 = relay.multiply(var_2365.astype('uint16'), relay.reshape(var_2366.astype('uint16'), relay.shape_of(var_2365))) # shape=(14, 6, 7)
func_1017_call = mod.get_global_var('func_1017')
func_1020_call = mutated_mod.get_global_var('func_1020')
var_2374 = relay.var("var_2374", dtype = "float32", shape = (180,))#candidate|2374|(180,)|var|float32
call_2373 = relay.TupleGetItem(func_1017_call(relay.reshape(var_2374.astype('float32'), [3, 15, 4])), 0)
call_2375 = relay.TupleGetItem(func_1020_call(relay.reshape(var_2374.astype('float32'), [3, 15, 4])), 0)
func_2315_call = mod.get_global_var('func_2315')
func_2318_call = mutated_mod.get_global_var('func_2318')
var_2379 = relay.var("var_2379", dtype = "float64", shape = (650,))#candidate|2379|(650,)|var|float64
call_2378 = relay.TupleGetItem(func_2315_call(relay.reshape(var_2379.astype('float64'), [13, 10, 5])), 0)
call_2380 = relay.TupleGetItem(func_2318_call(relay.reshape(var_2379.astype('float64'), [13, 10, 5])), 0)
bop_2382 = relay.multiply(var_2379.astype('uint16'), relay.reshape(call_2378.astype('uint16'), relay.shape_of(var_2379))) # shape=(650,)
bop_2385 = relay.multiply(var_2379.astype('uint16'), relay.reshape(call_2380.astype('uint16'), relay.shape_of(var_2379))) # shape=(650,)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_2390 = relay.TupleGetItem(func_1891_call(), 1)
call_2391 = relay.TupleGetItem(func_1892_call(), 1)
bop_2399 = relay.add(bop_2382.astype('int16'), call_2390.astype('int16')) # shape=(2, 4, 650)
bop_2402 = relay.add(bop_2385.astype('int16'), call_2391.astype('int16')) # shape=(2, 4, 650)
output = relay.Tuple([bop_2367,call_2373,var_2374,bop_2399,])
output2 = relay.Tuple([bop_2367,call_2375,var_2374,bop_2402,])
func_2408 = relay.Function([var_2365,var_2366,var_2374,var_2379,], output)
mod['func_2408'] = func_2408
mod = relay.transform.InferType()(mod)
var_2409 = relay.var("var_2409", dtype = "uint16", shape = (14, 6, 7))#candidate|2409|(14, 6, 7)|var|uint16
var_2410 = relay.var("var_2410", dtype = "uint16", shape = (14, 6, 7))#candidate|2410|(14, 6, 7)|var|uint16
var_2411 = relay.var("var_2411", dtype = "float32", shape = (180,))#candidate|2411|(180,)|var|float32
var_2412 = relay.var("var_2412", dtype = "float64", shape = (650,))#candidate|2412|(650,)|var|float64
output = func_2408(var_2409,var_2410,var_2411,var_2412,)
func_2413 = relay.Function([var_2409,var_2410,var_2411,var_2412,], output)
mutated_mod['func_2413'] = func_2413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_2465 = relay.TupleGetItem(func_1489_call(), 1)
call_2466 = relay.TupleGetItem(func_1490_call(), 1)
func_424_call = mod.get_global_var('func_424')
func_428_call = mutated_mod.get_global_var('func_428')
var_2468 = relay.var("var_2468", dtype = "uint64", shape = (455,))#candidate|2468|(455,)|var|uint64
call_2467 = relay.TupleGetItem(func_424_call(relay.reshape(var_2468.astype('uint64'), [13, 7, 5]), relay.reshape(var_2468.astype('uint64'), [13, 7, 5]), ), 0)
call_2469 = relay.TupleGetItem(func_428_call(relay.reshape(var_2468.astype('uint64'), [13, 7, 5]), relay.reshape(var_2468.astype('uint64'), [13, 7, 5]), ), 0)
func_424_call = mod.get_global_var('func_424')
func_428_call = mutated_mod.get_global_var('func_428')
call_2473 = relay.TupleGetItem(func_424_call(relay.reshape(call_2467.astype('uint64'), [13, 7, 5]), relay.reshape(var_2468.astype('uint64'), [13, 7, 5]), ), 0)
call_2474 = relay.TupleGetItem(func_428_call(relay.reshape(call_2467.astype('uint64'), [13, 7, 5]), relay.reshape(var_2468.astype('uint64'), [13, 7, 5]), ), 0)
func_1740_call = mod.get_global_var('func_1740')
func_1743_call = mutated_mod.get_global_var('func_1743')
call_2475 = relay.TupleGetItem(func_1740_call(relay.reshape(call_2465.astype('float32'), [100,])), 0)
call_2476 = relay.TupleGetItem(func_1743_call(relay.reshape(call_2465.astype('float32'), [100,])), 0)
output = relay.Tuple([call_2465,call_2467,var_2468,call_2473,call_2475,])
output2 = relay.Tuple([call_2466,call_2469,var_2468,call_2474,call_2476,])
func_2477 = relay.Function([var_2468,], output)
mod['func_2477'] = func_2477
mod = relay.transform.InferType()(mod)
var_2478 = relay.var("var_2478", dtype = "uint64", shape = (455,))#candidate|2478|(455,)|var|uint64
output = func_2477(var_2478)
func_2479 = relay.Function([var_2478], output)
mutated_mod['func_2479'] = func_2479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_2481 = func_1316_call()
call_2482 = func_1316_call()
output = call_2481
output2 = call_2482
func_2494 = relay.Function([], output)
mod['func_2494'] = func_2494
mod = relay.transform.InferType()(mod)
mutated_mod['func_2494'] = func_2494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2494_call = mutated_mod.get_global_var('func_2494')
call_2495 = func_2494_call()
output = call_2495
func_2496 = relay.Function([], output)
mutated_mod['func_2496'] = func_2496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_2510 = func_1316_call()
call_2511 = func_1316_call()
output = call_2510
output2 = call_2511
func_2526 = relay.Function([], output)
mod['func_2526'] = func_2526
mod = relay.transform.InferType()(mod)
output = func_2526()
func_2527 = relay.Function([], output)
mutated_mod['func_2527'] = func_2527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_2540 = func_1316_call()
call_2541 = func_1316_call()
output = relay.Tuple([call_2540,])
output2 = relay.Tuple([call_2541,])
func_2542 = relay.Function([], output)
mod['func_2542'] = func_2542
mod = relay.transform.InferType()(mod)
mutated_mod['func_2542'] = func_2542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2542_call = mutated_mod.get_global_var('func_2542')
call_2543 = func_2542_call()
output = call_2543
func_2544 = relay.Function([], output)
mutated_mod['func_2544'] = func_2544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_2545 = relay.TupleGetItem(func_1339_call(), 0)
call_2546 = relay.TupleGetItem(func_1341_call(), 0)
output = relay.Tuple([call_2545,])
output2 = relay.Tuple([call_2546,])
func_2555 = relay.Function([], output)
mod['func_2555'] = func_2555
mod = relay.transform.InferType()(mod)
mutated_mod['func_2555'] = func_2555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2555_call = mutated_mod.get_global_var('func_2555')
call_2556 = func_2555_call()
output = call_2556
func_2557 = relay.Function([], output)
mutated_mod['func_2557'] = func_2557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_2573 = relay.TupleGetItem(func_1339_call(), 0)
call_2574 = relay.TupleGetItem(func_1341_call(), 0)
func_2357_call = mod.get_global_var('func_2357')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_2583 = relay.TupleGetItem(func_2357_call(), 0)
call_2584 = relay.TupleGetItem(func_2358_call(), 0)
func_2555_call = mod.get_global_var('func_2555')
func_2557_call = mutated_mod.get_global_var('func_2557')
call_2588 = relay.TupleGetItem(func_2555_call(), 0)
call_2589 = relay.TupleGetItem(func_2557_call(), 0)
uop_2615 = relay.cosh(call_2583.astype('float32')) # shape=(25, 4)
uop_2617 = relay.cosh(call_2584.astype('float32')) # shape=(25, 4)
func_524_call = mod.get_global_var('func_524')
func_527_call = mutated_mod.get_global_var('func_527')
call_2623 = relay.TupleGetItem(func_524_call(relay.reshape(uop_2615.astype('float32'), [4, 5, 5]), relay.reshape(uop_2615.astype('float32'), [4, 5, 5]), ), 0)
call_2624 = relay.TupleGetItem(func_527_call(relay.reshape(uop_2615.astype('float32'), [4, 5, 5]), relay.reshape(uop_2615.astype('float32'), [4, 5, 5]), ), 0)
func_809_call = mod.get_global_var('func_809')
func_812_call = mutated_mod.get_global_var('func_812')
const_2655 = relay.const([-5.663070,-5.004687,-2.775334,-9.061430,-1.374225,5.462761,3.345645,-8.849291,1.224293,1.264667,0.042576,-1.248051,7.733880,-8.050880,5.827810,-9.825533,-7.990919,8.361912,1.157949,6.421971,8.929327,-3.192406,-1.466821,-1.849706,-2.730184,1.957543,-3.099954,4.188004,-0.903549,-0.531650,6.100698,5.374237,9.119297,1.180829,-3.099067,0.308855,6.534414,-4.137542,-5.812443,8.776245,2.658989,-6.401418,-1.626621,7.917005,-3.181807,-3.204572,0.220276,7.093971,8.908809,6.355469,4.354245,4.436140,-0.104915,2.596779,-3.738039,4.043146,1.009858,3.984615,-1.364675,4.069423,-9.927147,-2.924581,3.024856,2.825704,-1.810804,0.012366,1.538737,-0.678315,-8.876398,-7.002517,-8.548977,-7.967452,6.375515,8.778763,2.297129,-2.094143,8.122274,1.564308,3.104877,0.924479,7.135243,9.124541,3.557534,7.187146,9.266197,1.158451,6.730991,-5.734291,9.717735,-5.382515,-7.493554,0.010320,-7.991017,-2.129210,5.162931,0.059625,-2.474208,1.095677,1.987767,-3.748722,-0.907324,-4.148630,9.993755,-1.187511,3.976950,5.646198,-1.739140,6.450336,5.889346,-7.117972,2.012446,-3.300464,-3.210714,3.400379,-7.899287,8.163592,9.430172,-4.844690,-8.120044,-7.537374,-8.908609,3.817674,-1.153021,9.011060,-9.477654,-7.379978,6.936448,-7.050946,-7.924429,0.754305,2.671532,7.539949,4.721317,7.545533,-3.992041,0.858066,-1.897952,3.948745,9.068222,-4.439011,-2.313234,5.887430,7.766622,-0.307571,4.473810,-7.389735,-3.936335,-1.606080,-9.944360,7.995122,0.028639,1.581190,1.653466,-3.543213,7.195925,-7.203592,0.983717,9.031641,9.003387,-1.591784,-0.465597,4.283665,-4.888797,-8.747909,-8.885779,0.736613,-3.686541,5.940337,-4.641415,-0.814169,-1.213898,9.579587,-3.921374,3.104420,-4.913169,-4.312707,-2.624370,4.170409,0.165826,6.701695,5.748906,5.036602,9.152842,0.640484,-6.342614,9.383688,9.408917,-2.028633,-4.314876,1.739736,6.312767,5.954451,-1.898202,-3.280336,-7.714811,1.583236,5.311746,1.932475,3.792406,-1.937960,-7.660025,-6.003580,-2.455009,5.735726,-0.009762,-5.700145,-7.075041,-3.262812,-7.201999,3.971986,-3.427950,6.630806,3.281941,1.415189,1.355868,4.746071,9.675547,2.079462,-9.469347,-5.743585,-1.899199,1.506288,-4.871939,0.383296,-6.750976,6.985528,1.656304,-1.359161,1.731256,4.745080,1.025466,-1.943492,-8.365947,6.621779,-1.111396,-0.221544,-2.658903,-8.156539,9.878243,4.161035,-0.716820,-1.059428,2.433148,-1.221892,-2.144371,-9.713671,-1.499892,7.658407,-1.352982,-5.025918,-3.715325,8.857883,-9.108666,-1.628043,8.000379,1.468297,-7.498667,7.995188,6.279942,2.102462,8.969322,7.522127,-5.702839,1.518771,9.852160,-9.061292,-7.704103,-0.038868,3.622833,-5.539661,0.976644,-2.019827,7.565402,4.109706,8.802046,5.253387,-8.876628,0.813764,5.442664,-1.807830,-4.682104,-3.118834,-7.292936,9.078379,2.906095,0.195575,2.131442,0.657700,7.707552,5.484725,4.128078,-9.752764,-0.299898,-6.817024,-3.207035,-6.088207,1.399154,9.938058,-5.126255,4.955138,-6.722655,-5.286547,-5.175723,-0.524378,-2.555655,0.413466,-6.276731,-0.614575,6.107450,-2.520913,0.741887,-5.880129,-7.884559,-9.226861,-3.140758,-8.054516,-2.626660,-4.633614,-1.180863,4.449038,8.807264,-9.243911,-3.657913,-4.077458,-9.258365,0.085802,9.105564,-2.726805,7.887168,-6.547508,8.182557,-4.711644,9.561530,-1.183036,0.095250,3.621197,-1.564459,4.542018,-5.440442,-5.439815,-5.756390,-9.081754,6.395700,9.705644,0.034562,-9.916279,6.250349,8.169755,-0.113292,-2.632089,4.246791,-0.408108,-6.284914,-8.711692,2.952766,2.238799,-0.229972,7.831212,-4.038325,-5.682392,2.116276,-2.950711,1.729412,2.698289,-9.434609,2.755142,3.457399,7.362031,3.448086,-2.632475,3.401281,4.687891,5.951145,5.207745,7.990156,-5.348695,9.045319,5.951035,-4.975223,-1.307910,4.068395,-9.045871,5.737355,-9.373316,1.463778,2.280078,-6.561084,-2.385176,6.221888,2.719352,4.081087,2.510914,5.424508,9.674859,-3.428708,-8.806881,9.685175,-3.506230,-5.531691,-7.404640,-9.033384,-6.188630,-3.865915,-7.317973,3.936341,-9.390233,0.121522,8.314761,5.284214,-2.235107,-9.113713,5.008430,5.157133,-8.995139,-7.811444,5.704063,-9.699103,2.741800,-5.810769,-5.050955,7.792263,-1.396451,2.625949,0.480260,-9.133726,-3.636243,-3.699097,4.311111,1.649042,-6.147973,-7.196900,-0.598452,5.949566,6.181225,-4.377829,1.600035,-4.068303,-4.879553,8.808647,-7.632282,-5.515092,-5.177149,-9.645869,-4.873499,0.904438,7.730663,7.644486,-7.831155,8.224954,-1.296287,-4.504326,-5.633165,-1.166115,-3.743824,-5.147473,2.736717,9.787100,-0.023345,7.565498,4.801797,4.755050,-9.444532,7.458478,7.017091,-4.084434,-9.872851,-0.753377,-4.725659,1.097247,-2.229354,6.811531,-4.575093,-3.151171,1.190379,-7.467838,-4.088621,8.172046,-4.051449,-1.950403,-9.741943,4.550418,0.764383,2.289066,-5.550050,-7.510446,-1.560346,3.049101,-8.038540,0.333888,9.885460,-3.633073,2.658475,2.184643,-8.793851,-4.047439,-7.178850,4.107381,3.666894,7.986172,-2.097176,-4.024910,-7.918234,5.922545,7.267864,-2.555400,-9.377394,1.181717,-0.782671,4.262739,-7.791703,6.295750,-7.100561,-9.085550,0.762071,2.728570,2.798194,8.520433,3.792842,-5.388089,0.784176,-3.322785,0.609900,-6.795829,-0.116746,3.355119,5.745634,4.783000,9.688382,5.674987,-6.046678,-4.188776,-2.260701,1.112068,0.511215,9.265733,-0.348867,-1.462646,5.117777,2.888967,4.765445,-9.722696,-0.372713,-8.228439,7.683835,-6.669515,-9.503828,0.312842,-4.178771,8.301608,-7.041077,9.500266,-3.986887,-7.748474,-2.241123,7.935574,-4.602260,-1.957329,6.032643,7.043228,-9.922802,-1.832730,-2.990725,6.139013,-0.794318,-7.795051,1.121113,2.309779,-2.242111,6.197679,-6.403029,-9.632537,-1.791330,4.751295,1.438979,-1.727501,-3.320189,-8.010471,-3.331978,-4.398715,-8.290124,1.510226,-9.382192,1.220841,7.014669,9.528169,8.888702,-5.545959,-8.016401,-9.605501,-9.037293,8.532349,5.929281,-2.327401,8.773706,3.865742,9.832240,-0.151480,3.244566,-1.658000,-6.437279,-8.994181,2.322030,-8.595635,-3.543869,4.755767,4.077012,-9.779975,3.752317,3.641806,8.148436,-7.230010,2.698591,-8.090620,8.954149,8.481501,-7.478692,5.515367,3.065609,2.074540,-2.905533,-4.903715,1.281975,7.490168,9.789094,5.044643,4.652607,-8.982231,-6.354767,9.100698,0.093757,-6.191499,3.749196,-6.112907,1.047857,-4.485930,-5.059460,5.207567,9.409299,-5.318246,6.376348,7.458157,-4.869892,-3.888600,-8.549784,-4.381517,-6.772874,8.016808,-6.854831], dtype = "float32")#candidate|2655|(648,)|const|float32
call_2654 = relay.TupleGetItem(func_809_call(relay.reshape(const_2655.astype('float32'), [9, 9, 8])), 1)
call_2656 = relay.TupleGetItem(func_812_call(relay.reshape(const_2655.astype('float32'), [9, 9, 8])), 1)
output = relay.Tuple([call_2573,call_2588,uop_2615,call_2623,call_2654,const_2655,])
output2 = relay.Tuple([call_2574,call_2589,uop_2617,call_2624,call_2656,const_2655,])
func_2666 = relay.Function([], output)
mod['func_2666'] = func_2666
mod = relay.transform.InferType()(mod)
output = func_2666()
func_2667 = relay.Function([], output)
mutated_mod['func_2667'] = func_2667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2250_call = mod.get_global_var('func_2250')
func_2252_call = mutated_mod.get_global_var('func_2252')
call_2687 = func_2250_call()
call_2688 = func_2250_call()
var_2697 = relay.var("var_2697", dtype = "float64", shape = (2, 4, 15))#candidate|2697|(2, 4, 15)|var|float64
bop_2698 = relay.subtract(call_2687.astype('int16'), var_2697.astype('int16')) # shape=(2, 4, 15)
bop_2701 = relay.subtract(call_2688.astype('int16'), var_2697.astype('int16')) # shape=(2, 4, 15)
uop_2703 = relay.atan(bop_2698.astype('float32')) # shape=(2, 4, 15)
uop_2705 = relay.atan(bop_2701.astype('float32')) # shape=(2, 4, 15)
func_1776_call = mod.get_global_var('func_1776')
func_1778_call = mutated_mod.get_global_var('func_1778')
call_2718 = relay.TupleGetItem(func_1776_call(), 0)
call_2719 = relay.TupleGetItem(func_1778_call(), 0)
func_2666_call = mod.get_global_var('func_2666')
func_2667_call = mutated_mod.get_global_var('func_2667')
call_2740 = relay.TupleGetItem(func_2666_call(), 0)
call_2741 = relay.TupleGetItem(func_2667_call(), 0)
output = relay.Tuple([uop_2703,call_2718,call_2740,])
output2 = relay.Tuple([uop_2705,call_2719,call_2741,])
func_2742 = relay.Function([var_2697,], output)
mod['func_2742'] = func_2742
mod = relay.transform.InferType()(mod)
var_2743 = relay.var("var_2743", dtype = "float64", shape = (2, 4, 15))#candidate|2743|(2, 4, 15)|var|float64
output = func_2742(var_2743)
func_2744 = relay.Function([var_2743], output)
mutated_mod['func_2744'] = func_2744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_2784 = func_1316_call()
call_2785 = func_1316_call()
output = call_2784
output2 = call_2785
func_2807 = relay.Function([], output)
mod['func_2807'] = func_2807
mod = relay.transform.InferType()(mod)
mutated_mod['func_2807'] = func_2807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2807_call = mutated_mod.get_global_var('func_2807')
call_2808 = func_2807_call()
output = call_2808
func_2809 = relay.Function([], output)
mutated_mod['func_2809'] = func_2809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2555_call = mod.get_global_var('func_2555')
func_2557_call = mutated_mod.get_global_var('func_2557')
call_2884 = relay.TupleGetItem(func_2555_call(), 0)
call_2885 = relay.TupleGetItem(func_2557_call(), 0)
func_1017_call = mod.get_global_var('func_1017')
func_1020_call = mutated_mod.get_global_var('func_1020')
const_2898 = relay.const([5.518351,-8.845893,3.459217,-0.943990,-2.034342,-0.743983,8.248256,-1.369265,-4.661990,4.758866,-4.321533,0.768056,-6.895523,8.519189,8.598048,-8.400961,0.931004,-4.801631,-7.570863,8.322314,0.321951,-7.703752,-3.609070,4.833018,7.699503,5.573134,-2.003413,6.703428,-9.651390,7.801981,9.422688,-1.461852,-6.746160,9.281765,7.189566,0.537961,-3.798463,6.988834,7.074311,9.421975,-1.853932,-3.398149,4.390983,6.724162,-3.405936,8.183282,-0.282375,-6.272599,2.019596,5.403682,-2.591403,1.115817,-0.290129,5.945788,2.621816,-1.808334,4.609757,-5.831822,-8.834291,4.917838,-5.110052,-3.956150,-4.617144,-1.266895,-6.438939,7.656139,-6.236309,1.532538,2.284756,-5.281933,1.975651,-6.177980,5.392149,-6.712074,-7.493815,-8.267327,-2.317930,8.138359,7.105310,-9.416878,-2.409365,-2.378536,-3.846068,8.425688,6.472812,-2.117175,8.450103,7.732616,-8.614550,-7.058597,1.260453,0.945652,-7.390302,0.793481,-8.728589,1.030114,8.270502,-2.354954,-0.280162,2.367539,9.005171,-0.905967,0.771522,-8.384320,2.041695,-4.989066,0.984647,9.769153,6.795240,-3.346469,-3.254359,-5.135730,4.636339,-8.936436,-7.845323,3.095644,4.494220,-1.539412,-1.538919,-9.942720,-3.627355,-1.506254,3.416757,3.980140,-1.336963,-2.104622,5.168834,-9.503241,2.787728,-2.498920,1.716846,-6.176696,-5.599030,0.513208,1.592338,-6.137466,-1.991500,4.450469,-4.574730,-2.191927,-3.203204,-4.849500,3.719055,3.972671,1.615095,4.484701,0.941221,1.798342,-4.024590,-2.340377,4.012034,4.095504,-6.302791,4.566868,6.243707,5.537378,-7.386767,-3.633043,0.335170,3.614087,6.600042,7.556575,-7.986404,-2.584895,2.158193,-6.282607,-8.982398,-7.424487,-6.388255,3.807329,-6.604892,-2.629019,-3.654459,-0.527638,-9.484778,-5.796340,-7.096639,-7.831142,2.953029,-3.424709], dtype = "float32")#candidate|2898|(180,)|const|float32
call_2897 = relay.TupleGetItem(func_1017_call(relay.reshape(const_2898.astype('float32'), [3, 15, 4])), 0)
call_2899 = relay.TupleGetItem(func_1020_call(relay.reshape(const_2898.astype('float32'), [3, 15, 4])), 0)
output = relay.Tuple([call_2884,call_2897,const_2898,])
output2 = relay.Tuple([call_2885,call_2899,const_2898,])
func_2918 = relay.Function([], output)
mod['func_2918'] = func_2918
mod = relay.transform.InferType()(mod)
mutated_mod['func_2918'] = func_2918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2918_call = mutated_mod.get_global_var('func_2918')
call_2919 = func_2918_call()
output = call_2919
func_2920 = relay.Function([], output)
mutated_mod['func_2920'] = func_2920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2666_call = mod.get_global_var('func_2666')
func_2667_call = mutated_mod.get_global_var('func_2667')
call_2957 = relay.TupleGetItem(func_2666_call(), 1)
call_2958 = relay.TupleGetItem(func_2667_call(), 1)
output = relay.Tuple([call_2957,])
output2 = relay.Tuple([call_2958,])
func_2960 = relay.Function([], output)
mod['func_2960'] = func_2960
mod = relay.transform.InferType()(mod)
mutated_mod['func_2960'] = func_2960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2960_call = mutated_mod.get_global_var('func_2960')
call_2961 = func_2960_call()
output = call_2961
func_2962 = relay.Function([], output)
mutated_mod['func_2962'] = func_2962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2918_call = mod.get_global_var('func_2918')
func_2920_call = mutated_mod.get_global_var('func_2920')
call_2971 = relay.TupleGetItem(func_2918_call(), 2)
call_2972 = relay.TupleGetItem(func_2920_call(), 2)
output = relay.Tuple([call_2971,])
output2 = relay.Tuple([call_2972,])
func_2976 = relay.Function([], output)
mod['func_2976'] = func_2976
mod = relay.transform.InferType()(mod)
output = func_2976()
func_2977 = relay.Function([], output)
mutated_mod['func_2977'] = func_2977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2960_call = mod.get_global_var('func_2960')
func_2962_call = mutated_mod.get_global_var('func_2962')
call_3006 = relay.TupleGetItem(func_2960_call(), 0)
call_3007 = relay.TupleGetItem(func_2962_call(), 0)
func_1017_call = mod.get_global_var('func_1017')
func_1020_call = mutated_mod.get_global_var('func_1020')
const_3009 = relay.const([-0.277085,-2.805779,0.831864,-7.607742,3.122472,-3.403537,-0.179250,9.062145,-0.185653,4.934742,9.110540,8.152168,-9.234000,1.469436,2.419349,7.399996,8.140196,5.835003,-2.206711,1.995569,-4.729193,-3.458103,0.441804,5.170296,-5.946164,-5.366778,8.148260,4.248971,-1.901482,1.561651,-8.800217,9.360685,2.069259,-7.441518,-5.557124,5.860185,1.559129,7.796472,1.927418,-8.515133,-0.926543,3.187440,3.888054,2.872466,-9.341520,8.896657,4.805831,-7.199608,-5.533546,-6.617843,-3.752722,0.106156,2.890485,8.865357,8.088476,4.907762,-5.849807,9.392891,2.730254,2.562592,-0.451632,-7.246011,-9.092987,-7.317461,-9.079798,9.525374,-4.112205,-7.839445,-4.275447,-4.300444,-3.053805,6.057392,4.092808,-1.838390,2.473853,-3.623043,-6.156208,8.545539,5.881571,9.159752,-7.565606,1.757397,1.434875,-9.163010,2.954282,-8.789780,-8.940709,-1.092387,-3.538601,8.870170,2.162091,5.540862,-3.779948,-2.735559,-8.056447,1.358547,-6.091560,2.818377,9.930391,4.490665,5.719155,-0.195310,4.174402,0.719716,5.131947,9.200875,-0.609118,-2.526202,9.733932,-0.756330,1.894098,-2.455271,-8.990076,8.553217,-3.863711,-4.604775,-5.416044,0.878536,-1.721284,-1.431426,3.244701,-3.802904,-8.177092,9.800244,4.159929,-2.007480,0.778274,-1.428239,-0.746267,0.089934,3.120199,-6.194217,-3.288850,2.614786,-8.608678,-8.780721,-6.685710,9.645247,-6.685747,-5.474761,7.681287,-5.250941,-5.174280,-8.088495,-5.816982,7.746859,-5.722956,-9.966022,9.960971,3.208557,3.881851,-7.225605,-9.186345,-7.867094,-5.693641,-7.466474,3.004379,-5.838178,6.353904,3.556182,0.196760,8.587167,-6.760888,-6.096653,-5.797481,-1.322752,-4.451837,0.667106,-7.209312,5.538325,-5.647399,-7.256961,-1.877010,7.937296,-6.773061,2.378207,2.107326,4.742755,-3.286957,-2.437445], dtype = "float32")#candidate|3009|(180,)|const|float32
call_3008 = relay.TupleGetItem(func_1017_call(relay.reshape(const_3009.astype('float32'), [3, 15, 4])), 0)
call_3010 = relay.TupleGetItem(func_1020_call(relay.reshape(const_3009.astype('float32'), [3, 15, 4])), 0)
bop_3015 = relay.less_equal(const_3009.astype('bool'), call_3006.astype('bool')) # shape=(2, 4, 180)
bop_3018 = relay.less_equal(const_3009.astype('bool'), call_3007.astype('bool')) # shape=(2, 4, 180)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_3026 = relay.TupleGetItem(func_1891_call(), 1)
call_3027 = relay.TupleGetItem(func_1892_call(), 1)
output = relay.Tuple([call_3008,bop_3015,call_3026,])
output2 = relay.Tuple([call_3010,bop_3018,call_3027,])
func_3036 = relay.Function([], output)
mod['func_3036'] = func_3036
mod = relay.transform.InferType()(mod)
mutated_mod['func_3036'] = func_3036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mutated_mod.get_global_var('func_3036')
call_3037 = func_3036_call()
output = call_3037
func_3038 = relay.Function([], output)
mutated_mod['func_3038'] = func_3038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2960_call = mod.get_global_var('func_2960')
func_2962_call = mutated_mod.get_global_var('func_2962')
call_3045 = relay.TupleGetItem(func_2960_call(), 0)
call_3046 = relay.TupleGetItem(func_2962_call(), 0)
output = relay.Tuple([call_3045,])
output2 = relay.Tuple([call_3046,])
func_3057 = relay.Function([], output)
mod['func_3057'] = func_3057
mod = relay.transform.InferType()(mod)
mutated_mod['func_3057'] = func_3057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3057_call = mutated_mod.get_global_var('func_3057')
call_3058 = func_3057_call()
output = call_3058
func_3059 = relay.Function([], output)
mutated_mod['func_3059'] = func_3059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2542_call = mod.get_global_var('func_2542')
func_2544_call = mutated_mod.get_global_var('func_2544')
call_3124 = relay.TupleGetItem(func_2542_call(), 0)
call_3125 = relay.TupleGetItem(func_2544_call(), 0)
func_2960_call = mod.get_global_var('func_2960')
func_2962_call = mutated_mod.get_global_var('func_2962')
call_3128 = relay.TupleGetItem(func_2960_call(), 0)
call_3129 = relay.TupleGetItem(func_2962_call(), 0)
func_1559_call = mod.get_global_var('func_1559')
func_1563_call = mutated_mod.get_global_var('func_1563')
var_3132 = relay.var("var_3132", dtype = "uint64", shape = (560,))#candidate|3132|(560,)|var|uint64
call_3131 = relay.TupleGetItem(func_1559_call(relay.reshape(var_3132.astype('uint64'), [7, 16, 5]), relay.reshape(var_3132.astype('uint64'), [7, 16, 5]), ), 0)
call_3133 = relay.TupleGetItem(func_1563_call(relay.reshape(var_3132.astype('uint64'), [7, 16, 5]), relay.reshape(var_3132.astype('uint64'), [7, 16, 5]), ), 0)
uop_3158 = relay.log2(call_3124.astype('float32')) # shape=(2, 4, 1)
uop_3160 = relay.log2(call_3125.astype('float32')) # shape=(2, 4, 1)
output = relay.Tuple([call_3128,call_3131,var_3132,uop_3158,])
output2 = relay.Tuple([call_3129,call_3133,var_3132,uop_3160,])
func_3173 = relay.Function([var_3132,], output)
mod['func_3173'] = func_3173
mod = relay.transform.InferType()(mod)
mutated_mod['func_3173'] = func_3173
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3174 = relay.var("var_3174", dtype = "uint64", shape = (560,))#candidate|3174|(560,)|var|uint64
func_3173_call = mutated_mod.get_global_var('func_3173')
call_3175 = func_3173_call(var_3174)
output = call_3175
func_3176 = relay.Function([var_3174], output)
mutated_mod['func_3176'] = func_3176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2960_call = mod.get_global_var('func_2960')
func_2962_call = mutated_mod.get_global_var('func_2962')
call_3212 = relay.TupleGetItem(func_2960_call(), 0)
call_3213 = relay.TupleGetItem(func_2962_call(), 0)
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_3214 = relay.TupleGetItem(func_1850_call(), 3)
call_3215 = relay.TupleGetItem(func_1851_call(), 3)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_3218 = func_2494_call()
call_3219 = func_2494_call()
uop_3230 = relay.cosh(call_3218.astype('float32')) # shape=(2, 4, 1)
uop_3232 = relay.cosh(call_3219.astype('float32')) # shape=(2, 4, 1)
func_3173_call = mod.get_global_var('func_3173')
func_3176_call = mutated_mod.get_global_var('func_3176')
var_3243 = relay.var("var_3243", dtype = "uint64", shape = (560,))#candidate|3243|(560,)|var|uint64
call_3242 = relay.TupleGetItem(func_3173_call(relay.reshape(var_3243.astype('uint64'), [560,])), 2)
call_3244 = relay.TupleGetItem(func_3176_call(relay.reshape(var_3243.astype('uint64'), [560,])), 2)
bop_3245 = relay.equal(uop_3230.astype('bool'), relay.reshape(call_3218.astype('bool'), relay.shape_of(uop_3230))) # shape=(2, 4, 1)
bop_3248 = relay.equal(uop_3232.astype('bool'), relay.reshape(call_3219.astype('bool'), relay.shape_of(uop_3232))) # shape=(2, 4, 1)
output = relay.Tuple([call_3212,call_3214,call_3242,var_3243,bop_3245,])
output2 = relay.Tuple([call_3213,call_3215,call_3244,var_3243,bop_3248,])
func_3249 = relay.Function([var_3243,], output)
mod['func_3249'] = func_3249
mod = relay.transform.InferType()(mod)
mutated_mod['func_3249'] = func_3249
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3250 = relay.var("var_3250", dtype = "uint64", shape = (560,))#candidate|3250|(560,)|var|uint64
func_3249_call = mutated_mod.get_global_var('func_3249')
call_3251 = func_3249_call(var_3250)
output = call_3251
func_3252 = relay.Function([var_3250], output)
mutated_mod['func_3252'] = func_3252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3057_call = mod.get_global_var('func_3057')
func_3059_call = mutated_mod.get_global_var('func_3059')
call_3275 = relay.TupleGetItem(func_3057_call(), 0)
call_3276 = relay.TupleGetItem(func_3059_call(), 0)
output = call_3275
output2 = call_3276
func_3282 = relay.Function([], output)
mod['func_3282'] = func_3282
mod = relay.transform.InferType()(mod)
mutated_mod['func_3282'] = func_3282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3282_call = mutated_mod.get_global_var('func_3282')
call_3283 = func_3282_call()
output = call_3283
func_3284 = relay.Function([], output)
mutated_mod['func_3284'] = func_3284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2976_call = mod.get_global_var('func_2976')
func_2977_call = mutated_mod.get_global_var('func_2977')
call_3330 = relay.TupleGetItem(func_2976_call(), 0)
call_3331 = relay.TupleGetItem(func_2977_call(), 0)
output = call_3330
output2 = call_3331
func_3343 = relay.Function([], output)
mod['func_3343'] = func_3343
mod = relay.transform.InferType()(mod)
output = func_3343()
func_3344 = relay.Function([], output)
mutated_mod['func_3344'] = func_3344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2555_call = mod.get_global_var('func_2555')
func_2557_call = mutated_mod.get_global_var('func_2557')
call_3351 = relay.TupleGetItem(func_2555_call(), 0)
call_3352 = relay.TupleGetItem(func_2557_call(), 0)
func_2011_call = mod.get_global_var('func_2011')
func_2015_call = mutated_mod.get_global_var('func_2015')
var_3359 = relay.var("var_3359", dtype = "float64", shape = (1, 273))#candidate|3359|(1, 273)|var|float64
const_3360 = relay.const([-5.808105,4.094992,-1.683199,2.828186,9.298787,1.410659,9.078728,-4.988913,6.543411,-8.898871,-3.073249,7.230497,-5.417957,-6.735242,8.102482,2.543849,-9.798841,2.875435,-5.169631,-9.731081,-6.977463,-0.392847,3.086154,9.225913,-8.632811,-5.847908,-9.057795,6.983078,-0.080360,-2.922205,-8.427270,6.152583,-7.533654,6.389791,1.514117,8.327350,-4.445800,9.550823,-4.812591,-0.169253,-7.392327,8.582117,-4.891664,-8.641314,-6.160601,-1.289864,-0.804018,-2.728818,2.104935,6.977960,5.929581,-6.106652,3.910194,-5.166506,-7.748818,-9.404241,9.147519,8.340140,-0.303371,-0.759226,-5.622107,-3.456775,-1.746912,0.846887,-9.530486,4.069009,2.144520,4.456860,7.839099,-2.576290,-5.344158,5.512800,-7.083693,0.941997,-3.981077,-4.380161,7.247578,0.234618,5.316245,9.195372,9.694349,7.204884,-6.017400,4.812722,-5.446917,3.866875,-9.745055,-1.030056,2.730746,-3.202752,1.587440,-1.584362,0.892797,2.841112,-1.378290,-8.432029,3.910412,4.206549,9.275710,1.082197], dtype = "float32")#candidate|3360|(100,)|const|float32
call_3358 = relay.TupleGetItem(func_2011_call(relay.reshape(var_3359.astype('float64'), [13, 3, 7]), relay.reshape(const_3360.astype('float32'), [100,]), ), 8)
call_3361 = relay.TupleGetItem(func_2015_call(relay.reshape(var_3359.astype('float64'), [13, 3, 7]), relay.reshape(const_3360.astype('float32'), [100,]), ), 8)
func_1017_call = mod.get_global_var('func_1017')
func_1020_call = mutated_mod.get_global_var('func_1020')
const_3367 = relay.const([-0.597827,7.813671,0.523370,-8.761526,1.794090,-5.019915,1.442293,0.765062,2.034036,5.624339,8.056561,1.274575,1.611576,1.974359,5.353732,6.658114,-0.402739,8.404723,6.841476,6.611522,4.955212,4.565151,-5.097123,-4.801361,9.076538,-6.409814,1.032254,3.358751,5.394734,-2.488203,8.919021,5.386561,-6.303252,1.585773,-2.372847,-3.072533,-9.092368,-3.698067,-3.019106,0.772684,-8.999173,-9.278957,1.229785,-2.133574,-3.934136,4.641148,-8.097169,6.191902,3.477978,3.531589,0.451967,-0.856825,4.380275,-0.661777,4.715439,6.527659,9.565219,-6.822304,2.293516,-7.260862,2.630427,4.201234,-6.091991,-8.084639,6.062508,9.738484,-8.125675,9.017756,-3.248975,2.057844,2.263281,4.812544,9.747983,1.301550,-2.022494,-2.753735,5.356352,2.853581,3.401320,6.979672,4.471280,6.013968,-0.556168,3.391829,4.406571,0.092352,9.400156,2.625040,-4.283612,0.448211,-7.509697,-2.933059,3.012215,6.756462,1.496505,-1.534653,0.479182,-8.267864,-6.690883,-0.945478,2.144778,-8.371885,-7.841639,4.523985,-3.785950,3.342366,-6.276298,-9.263182,-8.786356,-8.240537,-7.814758,-3.765545,0.125958,-4.608577,1.774264,2.956815,-3.038954,3.908618,8.886023,1.037710,-5.765306,4.895137,-4.716786,-3.845410,2.307797,-9.213266,5.091829,-3.101243,-6.960943,-8.473119,3.416653,-3.990304,3.395317,8.862927,-5.375253,-7.058845,7.690248,6.795829,8.560358,-6.173661,0.325732,6.221855,-0.963461,7.565776,-3.216568,-6.911027,9.611925,7.921308,-8.098281,0.815708,7.620482,8.473614,0.452489,-3.352462,1.302043,-1.011813,9.276666,3.471667,6.859183,-2.008953,1.864827,7.101758,9.533361,2.940530,4.713581,-1.381158,2.087883,-9.047762,8.222895,0.859308,2.929340,5.646712,5.095874,-2.811160,5.390571,-1.776937,4.127634,4.453717,-6.586540,4.784702], dtype = "float32")#candidate|3367|(180,)|const|float32
call_3366 = relay.TupleGetItem(func_1017_call(relay.reshape(const_3367.astype('float32'), [3, 15, 4])), 0)
call_3368 = relay.TupleGetItem(func_1020_call(relay.reshape(const_3367.astype('float32'), [3, 15, 4])), 0)
var_3372 = relay.var("var_3372", dtype = "float64", shape = (3, 273))#candidate|3372|(3, 273)|var|float64
bop_3373 = relay.less_equal(var_3359.astype('bool'), var_3372.astype('bool')) # shape=(3, 273)
bop_3383 = relay.greater(call_3358.astype('bool'), relay.reshape(const_3360.astype('bool'), relay.shape_of(call_3358))) # shape=(25, 4)
bop_3386 = relay.greater(call_3361.astype('bool'), relay.reshape(const_3360.astype('bool'), relay.shape_of(call_3361))) # shape=(25, 4)
uop_3388 = relay.acosh(bop_3373.astype('float32')) # shape=(3, 273)
uop_3394 = relay.log(uop_3388.astype('float64')) # shape=(3, 273)
bop_3410 = relay.bitwise_xor(uop_3394.astype('uint32'), relay.reshape(uop_3388.astype('uint32'), relay.shape_of(uop_3394))) # shape=(3, 273)
const_3415 = relay.const([[-1,-5,-4,-9,-1,3,-3,-3,-5,1,-9,-3,2,-8,6,9,3,-10,-10,-9,-3,4,-9,2,7,9,6,5,-7,-5,2,-10,7,-4,-1,9,-5,2,7,-9,7,-10,-9,3,1,9,-3,8,1,6,-5,7,-7,6,-3,8,-5,5,5,-10,-5,10,9,7,-8,-3,-9,2,1,9,7,4,-10,-7,-8,-3,-7,-10,-9,-8,3,9,-2,-9,3,7,-7,-3,1,-2,-9,1,-8,-4,-1,3,2,7,4,-6,-3,-6,-5,7,-7,4,-6,3,9,10,-10,3,6,7,-5,-5,-8,-9,10,-1,-7,-4,-2,-4,6,3,6,9,8,-1,1,-1,9,-5,6,-5,-1,-5,-9,5,2,1,-6,9,8,-6,8,-1,-7,-5,2,-5,10,-5,-8,4,10,9,10,9,10,9,1,4,-8,-1,8,1,-6,8,-1,-6,-2,7,3,-9,1,10,10,2,-2,8,10,1,-10,-2,3,-1,2,-4,6,-9,-3,-1,-4,5,-7,-7,4,5,-7,4,6,3,-5,-5,2,8,-5,-2,-1,7,10,4,-2,-8,7,-8,-1,-3,10,7,-1,1,5,7,8,3,7,-2,6,9,5,-6,-8,3,6,2,-7,7,4,-8,-7,-2,8,-5,-7,-8,2,1,3,-8,5,10,10,-6,9,-1,-6,-5,1,9,-6,2,-2,-8,6,6,3,-5,-3,-1,6],[-1,5,7,7,3,2,1,-8,-1,-4,-6,-4,2,-2,10,-5,8,-8,-7,10,8,5,10,-10,-8,9,-1,-2,8,4,-10,10,8,-5,-3,-4,9,-2,-5,-9,5,6,10,-7,-4,8,-1,-3,6,-5,-5,10,10,-4,-2,-1,-10,3,7,-10,-2,-4,-7,-3,9,2,6,-9,-3,5,-5,-4,-3,6,-8,10,5,2,-3,6,10,-5,1,-5,8,-4,4,9,-5,-5,3,3,-9,1,10,5,7,-6,-5,-7,-1,-5,8,-2,3,6,-5,6,-5,-8,-6,5,-3,6,-4,-1,1,-1,2,-2,1,10,8,-9,-3,-8,-10,-4,7,-2,-2,-7,-1,-10,2,-7,-1,-10,-5,1,-10,8,-5,-4,4,-5,-1,7,-3,-4,-10,-1,-1,9,-1,-3,1,-10,6,1,2,-6,10,-4,2,-1,2,-3,-4,9,3,8,-5,-2,-4,1,-9,-10,2,-4,-1,-9,9,-6,-4,-8,-4,1,-7,-10,-6,-9,-2,5,-1,10,-6,-7,-3,-7,5,-4,-2,-10,-7,-9,5,-7,-7,1,-3,-1,10,-1,-10,-7,-4,8,5,-6,-10,7,-5,10,-9,9,2,9,10,4,-10,7,-4,-1,-2,-3,-4,-8,7,10,-1,-5,2,4,6,2,-10,10,-1,-5,8,3,-10,-10,1,10,2,4,1,-4,7,-3,-2,-3,3,-3,-5,2,9,2,-3,-1,-10],[-7,-2,-8,-6,6,-3,2,-4,-7,-3,-6,-3,2,3,-1,8,-3,-10,7,-3,5,-1,-4,-1,-6,9,9,-2,-8,-6,-7,-6,5,5,-3,7,6,4,-3,-10,1,2,-3,-1,-1,-9,-1,1,2,-10,-6,-4,6,-2,-5,9,6,-6,-8,-10,-3,-9,6,10,8,5,-10,-6,-7,7,-5,-9,-10,7,-9,-8,8,7,-7,-1,1,-1,-5,7,-7,5,1,-2,9,10,8,2,-3,-1,-8,-7,10,-1,-5,8,-5,6,9,8,9,7,3,-5,-8,9,1,-8,6,-6,10,-4,1,10,10,-9,5,10,5,6,-4,-3,5,-5,-1,-1,-7,5,-7,-7,2,-7,9,-6,-3,-10,-9,1,4,-4,-5,5,10,-9,4,5,1,4,-9,6,5,8,-9,-10,3,10,-1,-1,5,-7,7,7,-3,-9,3,4,-1,6,1,5,-3,1,9,2,-3,3,2,9,-2,10,2,-7,-6,5,10,1,-6,-5,6,1,10,-1,-5,-10,9,-4,5,5,6,-9,3,-10,-2,-4,-6,-10,-8,-1,-1,1,2,-2,7,-8,-9,-9,-7,-1,-6,7,-1,-8,-8,-3,-9,-1,-10,-8,2,9,-3,6,-9,-6,4,-7,-10,4,-4,-7,1,-4,2,-7,-7,8,7,9,10,1,1,-9,-2,9,9,-7,-5,-3,-4,-5,-1,3,8,-3,9,2,-1,1,5]], dtype = "uint32")#candidate|3415|(3, 273)|const|uint32
bop_3416 = relay.bitwise_and(bop_3410.astype('uint32'), relay.reshape(const_3415.astype('uint32'), relay.shape_of(bop_3410))) # shape=(3, 273)
func_1776_call = mod.get_global_var('func_1776')
func_1778_call = mutated_mod.get_global_var('func_1778')
call_3419 = relay.TupleGetItem(func_1776_call(), 0)
call_3420 = relay.TupleGetItem(func_1778_call(), 0)
func_2555_call = mod.get_global_var('func_2555')
func_2557_call = mutated_mod.get_global_var('func_2557')
call_3421 = relay.TupleGetItem(func_2555_call(), 0)
call_3422 = relay.TupleGetItem(func_2557_call(), 0)
bop_3424 = relay.power(bop_3416.astype('float64'), relay.reshape(bop_3410.astype('float64'), relay.shape_of(bop_3416))) # shape=(3, 273)
var_3431 = relay.var("var_3431", dtype = "uint32", shape = (3, 273))#candidate|3431|(3, 273)|var|uint32
bop_3432 = relay.logical_and(bop_3416.astype('bool'), relay.reshape(var_3431.astype('bool'), relay.shape_of(bop_3416))) # shape=(3, 273)
const_3435 = relay.const([[-10,10,5,8,8,-10,-1,-4,-1,-3,10,-8,-4,-2,-9,-4,5,10,-9,-1,10,-4,6,-2,-2,1,-4,8,7,-2,4,-5,9,1,6,7,-5,-8,10,7,4,5,-5,6,6,-10,4,-1,3,-3,6,-4,10,2,-2,1,7,6,10,7,1,-6,3,10,-1,-4,2,8,1,-1,8,-1,-9,-8,8,-2,-1,4,6,-1,-6,4,6,-1,1,-2,-5,6,9,-2,7,5,-2,5,2,5,-4,7,10,-7,-9,1,-9,9,-1,4,-3,-8,-8,5,1,-10,-8,3,5,8,-8,-10,-8,-4,8,-8,6,7,1,4,9,-6,-10,-4,10,9,-5,-4,7,-1,-5,5,-5,5,-4,9,-4,-2,-6,9,10,-4,6,7,6,-6,9,2,8,1,8,-9,4,7,10,6,2,7,9,-1,4,-6,3,-10,-7,2,2,8,-3,-6,8,2,-3,10,-5,-7,-2,-3,-4,5,3,-7,-1,10,7,-6,1,7,-9,6,-9,2,-9,-6,7,4,-1,6,5,5,-4,-9,10,-9,-2,-2,1,4,-10,-4,-2,-8,1,-4,-10,8,-1,-10,-2,10,5,7,-8,5,3,-5,-8,-9,-7,-5,3,4,10,-5,-3,8,-10,6,-8,-8,-10,8,-7,9,2,-2,7,9,10,-2,8,4,9,-8,9,-9,-8,-9,6,9,-1,-2,-9,-8,4,5,-1],[2,7,8,3,-6,-4,5,2,7,7,10,10,-6,-9,10,7,2,1,9,5,6,10,-1,-7,6,8,1,-5,6,-7,-3,-6,8,5,3,3,-1,-1,7,-9,-4,-10,-8,-2,-10,9,-3,8,-6,9,3,9,8,6,-9,-10,-3,8,7,6,-6,1,-3,3,4,-9,7,-10,-7,2,-3,-1,-3,10,8,7,2,-5,7,-4,-9,7,-10,-1,-5,-5,5,7,-4,8,-4,7,-1,10,-10,8,-7,5,5,-6,-1,1,8,2,4,3,-4,-3,-3,-2,9,-2,6,6,7,4,-3,-2,2,3,5,-3,8,-2,10,4,6,6,5,-5,-5,10,3,-9,7,10,-9,9,-8,-8,6,8,8,-6,-7,7,2,-10,-1,-2,2,-8,-5,-8,-7,3,-8,5,-6,-3,6,7,-9,-4,7,-7,-8,-1,2,-9,-8,10,3,4,-8,4,-6,1,7,6,-1,-4,9,-5,-7,-10,7,2,7,1,2,-9,-4,6,6,-5,6,-8,-5,6,7,6,5,-6,-4,8,-10,-8,5,-6,-7,-10,8,-8,2,4,1,3,-10,8,6,3,3,10,3,-1,-5,-3,-10,8,8,-3,-4,5,-7,-9,9,7,-3,-1,3,9,4,4,7,-6,-4,4,-7,-3,1,5,5,-3,-1,7,8,-5,-9,4,1,-1,-3,4,-3,2,8,-6,-1,3,5,9,5],[-6,3,10,-2,-10,3,4,-8,10,4,-10,8,9,3,-9,-4,-5,-4,2,4,-2,-5,-5,-3,-10,2,3,5,-1,2,9,4,-2,6,4,-5,1,1,2,8,10,-3,-7,-5,-9,10,-2,9,-3,-7,7,3,1,-3,-9,-8,-10,-4,-1,9,7,-5,6,-10,-1,7,-10,-7,6,5,-10,6,5,-8,10,-4,9,-5,-3,5,3,-3,2,-3,9,-6,2,8,-6,2,6,-3,5,-1,5,6,9,1,9,-2,4,7,1,-3,-2,3,3,4,-7,10,-2,-10,-4,-10,4,3,-9,-6,-4,9,6,-3,-1,-8,-1,-10,3,-1,10,-3,-5,-6,5,-7,3,-6,-10,-9,-7,9,7,10,-9,8,4,6,8,-6,-4,-3,-10,5,9,1,2,3,-9,-9,5,10,3,-1,-9,-5,1,-9,8,-3,9,2,-5,-1,9,5,-1,3,2,-4,-2,-6,-6,6,-1,10,2,-3,6,-1,8,-9,2,3,-8,7,-6,3,-9,6,5,-4,-8,3,-3,-1,10,-9,1,-6,-9,-7,7,-6,8,-8,8,1,1,9,8,-4,-7,-1,-7,7,2,-10,5,-7,8,7,9,1,2,3,-10,-8,-2,-7,-10,4,8,2,1,-6,9,6,-1,-8,-5,-5,-10,1,-4,10,3,-7,-7,6,-10,-9,-6,-7,-10,-2,-9,-9,1,-10,8,-8,-3,4,6]], dtype = "uint32")#candidate|3435|(3, 273)|const|uint32
bop_3436 = relay.greater_equal(bop_3416.astype('bool'), relay.reshape(const_3435.astype('bool'), relay.shape_of(bop_3416))) # shape=(3, 273)
func_1017_call = mod.get_global_var('func_1017')
func_1020_call = mutated_mod.get_global_var('func_1020')
call_3440 = relay.TupleGetItem(func_1017_call(relay.reshape(const_3367.astype('float32'), [3, 15, 4])), 0)
call_3441 = relay.TupleGetItem(func_1020_call(relay.reshape(const_3367.astype('float32'), [3, 15, 4])), 0)
output = relay.Tuple([call_3351,call_3366,const_3367,bop_3383,call_3419,call_3421,bop_3424,bop_3432,bop_3436,call_3440,])
output2 = relay.Tuple([call_3352,call_3368,const_3367,bop_3386,call_3420,call_3422,bop_3424,bop_3432,bop_3436,call_3441,])
func_3453 = relay.Function([var_3359,var_3372,var_3431,], output)
mod['func_3453'] = func_3453
mod = relay.transform.InferType()(mod)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3453_call = mutated_mod.get_global_var('func_3453')
var_3455 = relay.var("var_3455", dtype = "float64", shape = (1, 273))#candidate|3455|(1, 273)|var|float64
var_3456 = relay.var("var_3456", dtype = "float64", shape = (3, 273))#candidate|3456|(3, 273)|var|float64
var_3457 = relay.var("var_3457", dtype = "uint32", shape = (3, 273))#candidate|3457|(3, 273)|var|uint32
call_3454 = func_3453_call(var_3455,var_3456,var_3457,)
output = call_3454
func_3458 = relay.Function([var_3455,var_3456,var_3457,], output)
mutated_mod['func_3458'] = func_3458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_3476 = relay.TupleGetItem(func_1339_call(), 0)
call_3477 = relay.TupleGetItem(func_1341_call(), 0)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_3486 = relay.TupleGetItem(func_2238_call(), 0)
call_3487 = relay.TupleGetItem(func_2239_call(), 0)
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_3488 = relay.TupleGetItem(func_1647_call(), 0)
call_3489 = relay.TupleGetItem(func_1649_call(), 0)
uop_3491 = relay.sqrt(call_3488.astype('float64')) # shape=(2, 4, 1)
uop_3493 = relay.sqrt(call_3489.astype('float64')) # shape=(2, 4, 1)
func_3057_call = mod.get_global_var('func_3057')
func_3059_call = mutated_mod.get_global_var('func_3059')
call_3495 = relay.TupleGetItem(func_3057_call(), 0)
call_3496 = relay.TupleGetItem(func_3059_call(), 0)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_3501 = relay.TupleGetItem(func_1339_call(), 0)
call_3502 = relay.TupleGetItem(func_1341_call(), 0)
output = relay.Tuple([call_3476,call_3486,uop_3491,call_3495,call_3501,])
output2 = relay.Tuple([call_3477,call_3487,uop_3493,call_3496,call_3502,])
func_3514 = relay.Function([], output)
mod['func_3514'] = func_3514
mod = relay.transform.InferType()(mod)
mutated_mod['func_3514'] = func_3514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3514_call = mutated_mod.get_global_var('func_3514')
call_3515 = func_3514_call()
output = call_3515
func_3516 = relay.Function([], output)
mutated_mod['func_3516'] = func_3516
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3603 = relay.const([[[-4,6,5,-5,5,-8,-2,-2,8,9,-2,9,-1,8],[-1,-3,-1,4,-9,5,-4,-8,-9,-5,10,-7,6,-6],[-1,5,5,6,-9,5,1,9,-2,-10,-9,8,-10,2],[10,-2,-2,-2,-3,6,9,9,9,5,-6,2,9,-7],[-4,-4,-8,-7,3,9,8,-9,5,8,5,7,6,7],[1,6,-2,2,-9,10,10,10,-3,6,-5,5,-6,1],[4,-9,1,-10,10,-3,-3,-10,10,-1,-9,2,3,-5],[-2,3,4,8,-1,-10,-10,-9,4,6,-9,9,-5,-3],[-10,9,5,-7,6,-6,-2,6,-7,-5,-4,9,9,3],[-10,-4,5,4,5,-10,-5,-8,3,10,-8,-3,9,8],[-1,-4,7,3,3,-3,9,1,-10,-4,10,-4,-1,1],[-10,-8,9,-2,-3,-2,2,-7,1,-8,7,-5,-6,-7],[8,8,8,9,-9,-6,5,9,5,2,-5,8,-10,3],[4,4,-10,9,8,5,-10,10,-1,5,-8,-4,5,7],[5,-3,9,-10,-10,5,1,-5,-3,6,-7,-3,-8,-8]],[[-9,10,4,-4,3,-10,-4,-10,6,-6,4,4,5,-4],[4,-9,6,6,5,3,-3,10,9,-4,9,6,6,-3],[-5,5,1,-2,-3,1,8,5,-8,-3,-5,3,-9,-7],[9,5,9,5,5,-10,-8,6,4,9,4,-10,9,5],[4,-2,-2,-9,8,-2,1,-1,3,-5,9,-1,-6,-4],[-8,-2,8,5,10,2,10,-10,8,-2,-1,7,2,2],[1,-2,6,-1,-7,-6,-4,4,-4,7,-10,-2,7,-10],[9,7,-10,1,5,10,-10,-9,-7,-8,-1,-3,-5,1],[-4,1,3,-3,10,-10,-6,7,9,2,-2,8,-7,-4],[4,4,-6,-1,-4,-5,10,9,6,-4,3,4,8,1],[-1,-8,10,-4,7,-9,-2,3,-8,8,10,2,7,9],[7,1,-4,-4,-8,-5,4,6,-6,5,-3,9,-6,7],[8,9,7,-3,8,9,6,3,-6,3,1,-6,-3,-10],[-8,2,-4,-9,-2,5,-2,6,-6,7,1,6,9,6],[8,1,-2,2,-4,10,5,-6,8,6,-2,-10,4,2]],[[-7,-5,4,-1,-9,-4,-3,-8,10,9,5,-5,-8,-9],[8,-4,-2,10,-7,4,-3,8,5,-8,8,-4,-3,-2],[-4,1,-4,7,-6,-6,9,8,10,-1,9,-1,-7,2],[4,8,4,-9,6,8,4,-6,2,6,7,-9,7,5],[-5,-1,-10,-6,-10,-5,-1,-2,-5,-8,10,10,-1,6],[-9,1,8,2,3,-2,-10,-3,10,-8,2,1,-1,-3],[-2,-10,2,2,5,7,1,-3,8,2,1,-2,-5,9],[6,10,-3,-6,4,-4,-3,7,2,-4,7,-8,-5,3],[3,-10,4,-4,10,1,-1,3,7,5,1,10,7,-6],[6,6,1,-8,-4,1,6,8,-8,9,-10,-3,-6,-8],[-10,-7,4,-8,7,-2,-10,-5,-7,-4,-1,-8,-9,-1],[-5,10,-3,-4,8,2,9,6,-6,-6,3,8,4,6],[-1,10,6,-3,-7,-6,8,2,-1,-9,-9,-2,6,8],[-9,3,1,-6,-3,6,4,7,-1,3,7,-10,8,1],[-3,-4,-3,-2,2,1,-5,-5,10,-2,3,2,-7,8]],[[-6,9,-10,-2,2,9,-2,-7,-1,5,-6,-2,-2,1],[-7,-5,10,2,9,-4,10,4,8,-8,-6,8,-9,3],[5,5,2,6,-5,3,6,4,-3,-9,-10,9,9,-9],[10,-4,-7,8,8,-3,-4,-7,-6,-6,9,-1,2,6],[9,-2,9,-3,-4,8,-7,-2,-9,-1,2,-7,5,-10],[10,-10,1,-8,-9,-1,-4,-4,-1,-1,-7,-9,-4,-8],[6,7,3,-7,-1,-9,5,-5,8,-9,-6,-9,-7,-2],[5,-9,9,1,7,-10,-2,-1,8,6,-5,-3,5,4],[2,-2,-7,10,-9,9,8,6,-8,-4,3,10,-5,9],[-9,-2,10,-8,5,2,-10,1,2,-5,-4,-7,-1,5],[4,-3,-8,1,-9,4,8,1,8,-3,9,1,9,2],[-6,3,4,10,3,9,-10,-9,8,-6,1,-7,7,8],[7,-5,1,-3,-4,-5,6,-10,-7,-7,-8,-3,2,3],[-9,5,-1,9,8,4,-6,-10,5,9,10,10,8,-9],[3,-8,-1,8,-5,3,-10,-3,8,-7,5,8,3,-3]],[[1,-9,-4,-9,-2,-6,-6,8,7,-10,-7,1,-4,-7],[-9,6,-2,8,-4,8,6,2,-6,5,6,-2,4,-4],[4,-5,-10,5,-8,8,2,9,-4,9,3,-3,1,1],[9,-4,-7,-8,-4,10,9,-5,4,8,-6,7,-1,8],[8,-7,-5,1,-2,10,3,-9,8,3,9,-9,8,-4],[-8,3,10,-2,1,-6,4,10,-5,-2,-4,-4,-6,-7],[1,-5,4,5,-8,-8,2,-3,-1,8,3,-9,-4,-9],[6,-7,9,-5,8,6,9,-4,-1,1,-9,8,-6,-8],[-9,-1,6,3,-9,-8,-10,-4,10,2,-4,-3,-10,6],[9,-8,-4,-5,-6,6,9,-4,-10,-8,6,-2,-2,7],[8,-2,1,5,-1,-6,1,4,-7,8,7,-8,5,7],[-8,3,-10,-3,7,4,2,-6,-3,-2,-9,10,6,10],[1,-1,2,5,3,10,-7,7,-8,2,-3,4,5,-9],[3,2,-7,-2,-1,10,4,3,8,-3,-2,10,1,7],[-9,7,-6,-5,-6,-3,-4,10,-4,-1,2,1,-1,1]]], dtype = "int32")#candidate|3603|(5, 15, 14)|const|int32
var_3604 = relay.var("var_3604", dtype = "int32", shape = (5, 15, 14))#candidate|3604|(5, 15, 14)|var|int32
bop_3605 = relay.equal(const_3603.astype('bool'), relay.reshape(var_3604.astype('bool'), relay.shape_of(const_3603))) # shape=(5, 15, 14)
output = relay.Tuple([bop_3605,])
output2 = relay.Tuple([bop_3605,])
func_3609 = relay.Function([var_3604,], output)
mod['func_3609'] = func_3609
mod = relay.transform.InferType()(mod)
mutated_mod['func_3609'] = func_3609
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3610 = relay.var("var_3610", dtype = "int32", shape = (5, 15, 14))#candidate|3610|(5, 15, 14)|var|int32
func_3609_call = mutated_mod.get_global_var('func_3609')
call_3611 = func_3609_call(var_3610)
output = call_3611
func_3612 = relay.Function([var_3610], output)
mutated_mod['func_3612'] = func_3612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2250_call = mod.get_global_var('func_2250')
func_2252_call = mutated_mod.get_global_var('func_2252')
call_3723 = func_2250_call()
call_3724 = func_2250_call()
uop_3726 = relay.log(call_3723.astype('float64')) # shape=(2, 4, 1)
uop_3728 = relay.log(call_3724.astype('float64')) # shape=(2, 4, 1)
output = uop_3726
output2 = uop_3728
func_3742 = relay.Function([], output)
mod['func_3742'] = func_3742
mod = relay.transform.InferType()(mod)
output = func_3742()
func_3743 = relay.Function([], output)
mutated_mod['func_3743'] = func_3743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3742_call = mod.get_global_var('func_3742')
func_3743_call = mutated_mod.get_global_var('func_3743')
call_3754 = func_3742_call()
call_3755 = func_3742_call()
output = call_3754
output2 = call_3755
func_3762 = relay.Function([], output)
mod['func_3762'] = func_3762
mod = relay.transform.InferType()(mod)
output = func_3762()
func_3763 = relay.Function([], output)
mutated_mod['func_3763'] = func_3763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_3796 = relay.TupleGetItem(func_2238_call(), 0)
call_3797 = relay.TupleGetItem(func_2239_call(), 0)
output = call_3796
output2 = call_3797
func_3798 = relay.Function([], output)
mod['func_3798'] = func_3798
mod = relay.transform.InferType()(mod)
output = func_3798()
func_3799 = relay.Function([], output)
mutated_mod['func_3799'] = func_3799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_3802 = relay.TupleGetItem(func_2238_call(), 0)
call_3803 = relay.TupleGetItem(func_2239_call(), 0)
func_3249_call = mod.get_global_var('func_3249')
func_3252_call = mutated_mod.get_global_var('func_3252')
var_3808 = relay.var("var_3808", dtype = "uint64", shape = (560,))#candidate|3808|(560,)|var|uint64
call_3807 = relay.TupleGetItem(func_3249_call(relay.reshape(var_3808.astype('uint64'), [560,])), 2)
call_3809 = relay.TupleGetItem(func_3252_call(relay.reshape(var_3808.astype('uint64'), [560,])), 2)
func_3798_call = mod.get_global_var('func_3798')
func_3799_call = mutated_mod.get_global_var('func_3799')
call_3821 = func_3798_call()
call_3822 = func_3798_call()
bop_3826 = relay.logical_xor(call_3802.astype('int8'), var_3808.astype('int8')) # shape=(2, 4, 560)
bop_3829 = relay.logical_xor(call_3803.astype('int8'), var_3808.astype('int8')) # shape=(2, 4, 560)
output = relay.Tuple([call_3807,call_3821,bop_3826,])
output2 = relay.Tuple([call_3809,call_3822,bop_3829,])
func_3831 = relay.Function([var_3808,], output)
mod['func_3831'] = func_3831
mod = relay.transform.InferType()(mod)
var_3832 = relay.var("var_3832", dtype = "uint64", shape = (560,))#candidate|3832|(560,)|var|uint64
output = func_3831(var_3832)
func_3833 = relay.Function([var_3832], output)
mutated_mod['func_3833'] = func_3833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2976_call = mod.get_global_var('func_2976')
func_2977_call = mutated_mod.get_global_var('func_2977')
call_3835 = relay.TupleGetItem(func_2976_call(), 0)
call_3836 = relay.TupleGetItem(func_2977_call(), 0)
output = relay.Tuple([call_3835,])
output2 = relay.Tuple([call_3836,])
func_3837 = relay.Function([], output)
mod['func_3837'] = func_3837
mod = relay.transform.InferType()(mod)
output = func_3837()
func_3838 = relay.Function([], output)
mutated_mod['func_3838'] = func_3838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2960_call = mod.get_global_var('func_2960')
func_2962_call = mutated_mod.get_global_var('func_2962')
call_3880 = relay.TupleGetItem(func_2960_call(), 0)
call_3881 = relay.TupleGetItem(func_2962_call(), 0)
var_3899 = relay.var("var_3899", dtype = "float32", shape = (2, 4, 6))#candidate|3899|(2, 4, 6)|var|float32
bop_3900 = relay.add(call_3880.astype('int16'), var_3899.astype('int16')) # shape=(2, 4, 6)
bop_3903 = relay.add(call_3881.astype('int16'), var_3899.astype('int16')) # shape=(2, 4, 6)
output = bop_3900
output2 = bop_3903
func_3911 = relay.Function([var_3899,], output)
mod['func_3911'] = func_3911
mod = relay.transform.InferType()(mod)
var_3912 = relay.var("var_3912", dtype = "float32", shape = (2, 4, 6))#candidate|3912|(2, 4, 6)|var|float32
output = func_3911(var_3912)
func_3913 = relay.Function([var_3912], output)
mutated_mod['func_3913'] = func_3913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2074_call = mod.get_global_var('func_2074')
func_2076_call = mutated_mod.get_global_var('func_2076')
call_3937 = func_2074_call()
call_3938 = func_2074_call()
const_3943 = relay.const([[-3.819266,8.488176,8.382936,7.651582],[9.628914,-0.610638,9.904783,-5.548239],[-9.860736,1.359202,0.416224,9.336005],[5.648522,-3.742066,5.240958,3.871290],[-1.922343,3.126558,7.505458,7.256224],[-5.204821,5.296867,-0.981675,-2.108489],[-6.732383,-0.137542,-6.440259,0.167921],[-2.020359,9.840020,0.806915,2.025391],[-4.534080,-9.015674,-8.389703,-5.275705],[5.590145,-9.954215,2.642578,1.531719],[-9.915326,6.160391,2.021807,1.903623],[9.204007,5.207118,3.876614,-3.164965],[5.286261,8.252681,-3.642143,-9.833881],[4.429797,-2.172824,-3.999115,4.531877],[5.693446,7.085264,4.573755,-8.479320],[4.900249,-5.197499,6.083700,-6.076241],[4.043651,-9.878059,5.989849,9.552808],[5.400286,-0.644523,8.474931,5.592789],[-4.183511,5.424334,2.368134,-4.275311],[1.211525,7.242087,-7.247719,-8.683569],[7.542552,9.382197,1.717307,-6.234035],[-7.109319,-1.269700,-5.468024,3.583589],[-3.901565,-9.094791,-3.257978,2.456989],[2.575761,-3.769280,-4.359794,0.731087],[0.477765,9.783802,-2.789582,-3.923019]], dtype = "float64")#candidate|3943|(25, 4)|const|float64
bop_3944 = relay.logical_or(call_3937.astype('bool'), relay.reshape(const_3943.astype('bool'), relay.shape_of(call_3937))) # shape=(25, 4)
bop_3947 = relay.logical_or(call_3938.astype('bool'), relay.reshape(const_3943.astype('bool'), relay.shape_of(call_3938))) # shape=(25, 4)
output = bop_3944
output2 = bop_3947
func_3958 = relay.Function([], output)
mod['func_3958'] = func_3958
mod = relay.transform.InferType()(mod)
mutated_mod['func_3958'] = func_3958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3958_call = mutated_mod.get_global_var('func_3958')
call_3959 = func_3958_call()
output = call_3959
func_3960 = relay.Function([], output)
mutated_mod['func_3960'] = func_3960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3514_call = mod.get_global_var('func_3514')
func_3516_call = mutated_mod.get_global_var('func_3516')
call_3964 = relay.TupleGetItem(func_3514_call(), 1)
call_3965 = relay.TupleGetItem(func_3516_call(), 1)
func_809_call = mod.get_global_var('func_809')
func_812_call = mutated_mod.get_global_var('func_812')
const_3976 = relay.const([1.487787,8.884549,7.613241,3.001922,3.539698,-9.095885,3.180903,-7.305717,-5.110779,-6.933705,0.465365,0.996334,-7.691167,3.987011,7.580574,5.831143,8.917947,9.175907,0.583137,-1.955580,4.888193,-7.509870,-8.552044,2.274145,-4.898166,-5.941754,-3.159538,9.496528,-3.857841,-9.875354,9.310393,-2.521937,3.062707,-3.949387,-9.673980,5.314129,2.846101,-3.401075,-6.682217,-2.764695,3.264061,-7.255428,-0.817150,-6.085158,2.761295,-4.160209,-4.427653,7.275110,6.994539,-1.521381,-7.555745,4.319228,-3.826654,-9.091204,-8.823677,6.671894,2.965696,2.642885,9.269739,-8.345102,-8.591147,0.729848,5.854856,-1.176411,-2.663945,-6.718071,-6.124028,-1.245292,2.474998,-0.114306,6.826779,1.404726,1.410262,3.742625,-0.493629,0.873488,-2.801762,-6.106251,-7.907338,-1.169497,9.472397,1.076045,9.230322,-1.644700,-7.449301,-7.657399,-1.451394,-2.754982,-8.365512,-2.005565,4.506176,9.777468,8.489186,2.373652,6.628497,-5.945328,-5.780831,-1.871863,-6.861615,-8.673304,6.009330,-1.960502,-7.594716,-2.815529,-6.284649,-3.450759,-5.642666,-9.512628,6.788807,1.462022,4.884395,3.631401,-3.369327,4.506389,3.839595,8.421928,-7.980709,-6.043901,3.277521,4.087118,-8.413405,0.036126,-2.983379,-5.682543,-2.260187,-3.974533,3.836887,3.116864,8.757992,-4.321776,9.731790,-7.038461,-2.187335,-1.070806,9.312250,0.874863,1.799876,-0.547961,-6.397939,9.269278,2.445154,4.029418,-0.640207,-5.720696,1.596536,-0.600751,-9.322037,3.373675,6.472202,-8.612762,6.366646,-6.850566,3.722982,-1.760934,0.504094,-5.661035,8.071800,-3.334147,-3.222133,-4.638722,0.258820,-0.169672,5.985360,-8.266680,-6.718812,8.100862,8.622686,-2.825221,-7.845973,-0.011632,2.075526,-3.741061,-7.793078,-1.150354,7.922938,8.758154,4.316004,8.967524,0.312036,6.050188,-8.565255,9.635786,4.456440,-5.211338,5.454667,5.056979,9.261174,6.095398,-6.105361,6.364472,-5.714389,3.716188,-0.121012,-6.646178,-6.103993,0.459313,-3.557106,-4.420695,4.042496,-5.067691,-5.409808,6.589174,0.478066,2.137210,-6.383759,-5.244505,6.573507,-0.199423,-5.364640,8.310363,-0.278588,5.383276,-0.267912,-2.737205,7.584505,-0.615614,6.146036,7.164329,-5.119559,-4.216909,8.247912,-4.472672,-4.077700,7.121468,5.414891,-6.636660,1.054534,1.937873,3.159578,2.547033,-2.026196,-8.656183,7.198873,-8.716016,0.829793,-3.738978,6.726180,7.538367,8.648726,-8.611640,-2.704572,2.249674,7.552559,4.794284,-9.137626,8.444185,-0.345403,-2.272069,9.040491,2.071895,-4.389389,-4.303070,-0.735672,8.012820,-2.251625,5.055721,-7.785407,-8.027832,0.941897,4.579527,8.519989,-4.273163,-2.968852,0.618783,4.169888,-5.607856,9.728339,-8.419270,6.224553,2.636584,2.976706,-5.862961,4.834080,7.676254,-6.789459,0.427663,2.721802,2.567306,-5.744383,-5.925443,3.079826,6.149779,4.032897,7.373928,-4.040261,-4.248463,8.597168,8.021657,8.431694,1.431815,4.725246,1.785202,-7.368750,3.431572,-6.426069,-4.763564,-1.926889,-6.403971,5.545646,-7.182523,-9.803862,-2.240611,0.201214,6.625960,-1.072911,-0.560273,8.606292,9.312223,-7.048754,-0.625091,-0.663625,7.273467,2.496119,-1.040847,9.758618,-4.016926,5.400441,8.793774,-7.839036,5.013885,6.210571,5.317757,-5.692196,-7.830235,0.609365,7.678847,9.302362,-0.611020,-0.354129,-3.970108,-2.724893,1.916872,3.591042,-0.635251,1.063262,-8.910361,-4.222820,9.800187,-5.604556,0.247419,5.582737,0.547273,6.331382,0.587326,-9.035117,8.298905,-5.231868,-6.749810,1.234808,2.123373,1.065142,1.375924,1.432586,-0.221405,-1.331619,9.010933,-9.315379,4.745474,9.334039,8.371037,-0.832090,-3.359337,0.923382,-0.786351,6.303016,-3.464254,7.321908,-8.423641,-2.625061,8.076387,6.914026,-6.450291,4.040262,3.522098,-5.602903,8.930012,-7.489374,2.549459,-3.255617,-3.145686,-4.967031,-5.728499,9.130393,-7.646196,7.150593,-9.102159,2.907493,-5.764711,-8.189596,9.376951,-3.735707,3.174233,-5.614778,5.950391,-0.434118,-3.756213,-7.532443,3.480937,-1.952815,1.953130,8.971448,-2.281339,4.280145,6.946273,-1.586050,-6.490310,1.521449,9.384516,7.305608,0.778487,5.398672,-2.514014,-8.486753,2.473935,0.475545,1.173276,-7.611494,6.209455,-3.237105,-3.720853,7.115668,-2.974411,-5.053174,-3.130347,-8.608459,-7.246069,-4.541459,0.072074,-8.178414,0.634921,1.688821,-9.568031,-5.230264,7.251575,-2.152299,2.051164,7.210809,4.537361,-0.462084,3.119146,0.037849,-8.806957,-1.019503,-0.998510,-6.491685,-1.055501,-6.917964,9.405783,4.174822,-8.244489,-8.799709,1.244160,7.620388,-7.127632,0.262748,-3.981541,9.463375,-5.503818,-5.394796,-4.025656,-2.683529,-5.048349,7.039751,9.916585,9.818170,-5.179728,7.594465,0.417983,-8.970532,-2.872672,8.010136,-2.209274,1.165729,-6.646436,-1.228813,-1.809621,1.573475,8.801678,0.431091,4.415076,-7.060450,-0.361238,-5.541662,-5.809649,6.628016,-1.599121,8.613439,8.318402,4.846409,-6.338232,-1.395154,-1.547866,-4.338453,-5.538767,-0.447602,-6.285088,-0.996052,-0.915648,-3.338899,0.602035,-7.464988,-8.195146,5.123569,-5.874871,1.579069,-7.791005,-1.126018,2.173451,-3.826024,-6.617752,-7.462671,-1.990005,5.316050,8.055238,0.932326,-3.048081,-0.128964,-2.895783,-6.822626,-8.869306,2.959788,-5.182188,4.854802,-1.574854,4.064814,-5.446238,1.232361,-1.458965,1.159433,-8.248677,3.150594,-1.094803,6.024541,9.269078,-7.217381,9.564237,-4.027567,8.667216,-1.152204,6.816247,-8.369630,8.660277,-5.157705,-8.596299,0.898105,8.608387,4.706931,-7.923923,-8.362289,3.050765,5.331804,-4.071594,-0.419267,0.640197,-4.415927,-9.805902,-9.051132,-1.066779,-3.519854,-1.149319,-0.806596,-1.478237,-2.346815,-0.328266,-5.232196,4.440857,6.382089,6.857758,3.415319,-5.402263,6.589625,-9.490242,-2.559506,6.711380,5.051636,-6.649762,9.847487,-2.240713,1.153536,-0.317589,-5.482802,6.868248,8.550803,2.139443,5.009202,-3.576972,-4.739047,-6.955709,-8.346223,7.644684,0.157269,6.226610,-0.862050,-5.935608,-3.210022,0.458149,-7.053411,-6.470929,4.068051,-0.967166,1.688162,-0.736751,2.983551,-4.845141,-6.717294,-4.424921,9.467414,-6.929970,0.039223,5.123236,5.210070,-3.061322,8.359547,0.881719,-6.404181,7.460532,3.442161,2.584163,-4.465537,-8.637747,-9.173590,8.885982,-9.883844,8.842381,-4.395250,0.491980,-6.979374,-5.939323,1.695107,-3.494685,1.848367,9.017774,0.741264,-5.145623,3.037960,-4.020304,1.390480,0.678854,4.132485,6.195281,-1.890508,5.842602,-5.500056,-8.427118,-8.015817,6.080999,7.303029,-2.872363], dtype = "float32")#candidate|3976|(648,)|const|float32
call_3975 = relay.TupleGetItem(func_809_call(relay.reshape(const_3976.astype('float32'), [9, 9, 8])), 2)
call_3977 = relay.TupleGetItem(func_812_call(relay.reshape(const_3976.astype('float32'), [9, 9, 8])), 2)
output = relay.Tuple([call_3964,call_3975,const_3976,])
output2 = relay.Tuple([call_3965,call_3977,const_3976,])
func_3994 = relay.Function([], output)
mod['func_3994'] = func_3994
mod = relay.transform.InferType()(mod)
mutated_mod['func_3994'] = func_3994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3994_call = mutated_mod.get_global_var('func_3994')
call_3995 = func_3994_call()
output = call_3995
func_3996 = relay.Function([], output)
mutated_mod['func_3996'] = func_3996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2031_call = mutated_mod.get_global_var('func_2031')
call_4038 = relay.TupleGetItem(func_2030_call(), 1)
call_4039 = relay.TupleGetItem(func_2031_call(), 1)
output = relay.Tuple([call_4038,])
output2 = relay.Tuple([call_4039,])
func_4040 = relay.Function([], output)
mod['func_4040'] = func_4040
mod = relay.transform.InferType()(mod)
output = func_4040()
func_4041 = relay.Function([], output)
mutated_mod['func_4041'] = func_4041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4040_call = mod.get_global_var('func_4040')
func_4041_call = mutated_mod.get_global_var('func_4041')
call_4050 = relay.TupleGetItem(func_4040_call(), 0)
call_4051 = relay.TupleGetItem(func_4041_call(), 0)
output = relay.Tuple([call_4050,])
output2 = relay.Tuple([call_4051,])
func_4075 = relay.Function([], output)
mod['func_4075'] = func_4075
mod = relay.transform.InferType()(mod)
mutated_mod['func_4075'] = func_4075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4075_call = mutated_mod.get_global_var('func_4075')
call_4076 = func_4075_call()
output = call_4076
func_4077 = relay.Function([], output)
mutated_mod['func_4077'] = func_4077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_4081 = relay.TupleGetItem(func_3036_call(), 0)
call_4082 = relay.TupleGetItem(func_3038_call(), 0)
func_3173_call = mod.get_global_var('func_3173')
func_3176_call = mutated_mod.get_global_var('func_3176')
var_4097 = relay.var("var_4097", dtype = "uint64", shape = (560,))#candidate|4097|(560,)|var|uint64
call_4096 = relay.TupleGetItem(func_3173_call(relay.reshape(var_4097.astype('uint64'), [560,])), 2)
call_4098 = relay.TupleGetItem(func_3176_call(relay.reshape(var_4097.astype('uint64'), [560,])), 2)
func_2315_call = mod.get_global_var('func_2315')
func_2318_call = mutated_mod.get_global_var('func_2318')
const_4101 = relay.const([7.402132,5.156656,-0.731779,0.442841,5.144372,-4.866693,-8.303127,-7.684380,9.216824,-2.956971,5.683705,8.397191,4.290119,8.886772,-8.917882,-6.215627,-5.890498,-1.724624,3.703907,-6.633346,8.739982,4.033402,6.514774,-1.607224,1.944435,6.880536,-4.580351,-3.062167,0.868531,-2.353555,-9.856773,8.955088,-8.186003,2.836678,8.130358,-5.829905,-9.529014,9.550779,9.576104,0.422694,-2.645042,-8.717555,0.652433,1.524258,-4.193744,-4.733199,-6.257855,4.923644,9.852089,-5.758535,-9.026757,1.922485,-5.648584,7.597334,2.675702,-2.053741,3.414192,-2.958295,-9.917087,3.086989,7.806001,7.549385,4.734318,-4.689097,-3.931893,-8.946770,3.970063,7.068717,-9.771811,1.262145,4.372043,2.229169,-3.606753,-0.126336,5.649816,-0.756837,1.862593,-2.992890,-9.159598,-2.606583,-7.673388,-7.236073,-4.692800,1.478814,-9.250270,-5.492036,2.566243,-4.062578,0.123189,-3.226374,-4.661969,0.365050,-4.600708,-8.762664,-9.789625,0.941670,5.932911,-4.601410,-1.658565,-3.175238,0.820477,-0.773971,7.404899,-2.861551,1.022858,5.379638,3.370977,-8.093602,8.007205,5.251754,5.318486,-6.269995,-4.544497,-2.350902,-4.706823,8.001215,-7.112405,-9.291528,-9.878460,-9.896443,5.352217,7.740843,6.542327,8.412421,-3.868760,-1.325894,7.914264,8.506861,-6.279106,-4.277674,-4.317338,-7.870155,-8.808353,-3.001975,6.321058,-0.154703,9.076345,-0.929882,8.808490,8.047968,-8.492920,1.215342,-7.468384,9.447189,8.964107,0.351801,7.437213,-1.937210,3.124089,-8.798567,2.514634,1.218120,-4.978316,8.872168,1.386502,3.178722,2.619855,-9.340365,5.803941,-3.632163,5.848006,8.102466,5.407894,-7.607918,-0.582920,5.576879,-1.737429,-4.236956,-6.583649,-1.022311,-9.533840,7.606772,7.067638,9.698822,1.933273,0.738646,-8.022210,6.149653,-9.132446,-9.260818,-4.014126,-0.203462,-4.865222,7.663295,5.193775,4.452161,-8.350809,2.048977,-6.333611,-9.919039,-5.669634,-1.717659,-1.932490,-3.004795,-0.279223,-0.119450,-0.913629,6.414735,1.566295,-1.931821,-2.902343,8.133296,-1.985250,-1.684666,4.849322,6.898048,-3.202508,-8.905888,5.489840,1.333393,6.149841,5.441698,6.518561,3.918779,6.883073,5.938360,9.188348,-5.773192,6.227485,-6.765440,-3.445099,-8.493786,4.481165,2.921360,5.781389,-6.695159,-0.952541,-9.079805,-9.341758,3.199126,1.398514,-5.541509,9.614363,3.872069,8.011631,2.454525,4.073073,8.052568,7.461182,4.820697,5.159346,2.048938,5.851633,4.398867,0.143806,-0.752417,8.912559,6.012690,1.273498,4.328188,-6.013617,-2.885756,-3.031632,5.757972,9.341596,-0.437152,-5.503661,-1.515672,-3.837130,-8.875349,-9.273782,-4.792619,1.939505,-7.624165,-6.990555,7.238361,8.927063,-0.304517,3.791009,0.577111,1.849984,-9.256612,3.006582,4.831806,-9.386300,-1.989405,-1.135011,4.188049,-6.942208,5.470187,5.395837,-0.247681,-9.640148,1.538498,-9.610253,-6.718850,-9.013749,2.732267,-0.478036,1.925791,-5.167726,5.422825,0.128995,-0.711094,9.483563,-2.566708,0.839528,3.882726,-5.344371,0.754612,9.264522,-8.627588,-7.937871,4.555915,-2.083413,-4.881184,-8.436504,-2.613027,-6.779574,-0.538908,-0.886159,-1.154458,9.332449,3.036972,-7.528741,-3.722051,0.514704,-4.269115,-0.168378,-0.420742,-9.383125,-7.285777,-3.794877,-7.959670,2.149246,-1.300873,-6.448702,9.073559,-2.583346,7.943886,-8.836244,-6.249131,-5.673971,3.926911,7.590893,9.853097,-2.227102,-7.962030,-5.749916,7.168526,9.338609,9.072325,5.665909,6.614628,-0.463136,-2.675630,-1.523431,-8.701626,7.777454,-0.199580,4.947170,2.227123,8.521152,-5.081372,-0.291512,6.042799,-2.804967,7.615262,-9.384435,4.136327,8.673204,3.546490,4.003904,-5.191236,8.061975,0.510244,3.282547,1.775925,-0.856283,-5.366062,3.664370,6.337198,9.365363,5.423102,8.366360,-5.071052,5.352677,3.353450,9.957543,7.748358,-2.298895,4.545946,9.914164,-3.895436,-5.619952,4.273294,-8.709755,3.734594,6.270293,3.934044,-0.355298,-3.414290,2.710141,-8.413353,1.428723,-4.551962,-7.202537,6.488442,-4.078266,9.550408,9.060900,-5.307007,1.859656,4.746896,8.655922,-7.755784,-7.165359,6.157074,-5.256656,-9.621452,4.598381,3.932727,-2.811813,-1.589698,-1.060272,1.731548,-2.464876,2.705956,-7.363149,-8.846186,-2.621053,1.393956,3.263776,-3.644414,-5.175282,-8.401182,0.037300,7.999391,-0.695698,-9.109248,4.382429,-0.960497,-8.764588,-3.364762,-7.858556,-0.458011,4.159215,3.082894,-5.467012,-1.822229,-8.314841,-8.414001,-8.654498,8.611376,2.378649,5.814101,-9.771765,-6.407991,4.629491,0.245530,-1.102123,-0.943997,0.245899,-9.104410,-9.510374,-7.097384,3.253205,-9.260305,-8.270158,8.066155,-8.983987,-9.370208,-4.231405,7.813755,1.964437,-7.515052,-2.993683,6.983037,-2.613725,3.708347,-7.214610,-5.490254,-1.225004,3.069646,-8.348282,9.231600,5.901400,2.467383,-2.737861,-4.368238,5.245805,7.250597,8.068028,3.791596,8.408477,-9.459354,-1.746695,9.805172,-9.423138,0.561380,7.326735,4.715866,8.245576,9.871931,6.643071,7.829360,-9.280439,-7.284651,-0.237643,1.513030,-5.632707,2.543215,-6.926525,6.696168,-3.481936,-8.302328,0.576240,-5.593811,-6.488214,0.259289,3.239312,2.314253,2.326884,-7.383317,8.661572,2.808847,6.376084,2.102711,-4.246577,-4.229953,8.477810,-0.656214,-8.433166,5.881334,-5.633008,-7.546082,-7.177503,2.516392,6.136280,0.790688,-7.797065,-4.266174,8.954897,9.866985,8.292883,-7.331143,-7.025283,4.582386,-0.456888,-5.859853,2.613778,-5.155480,-8.131352,-2.040870,0.577769,-4.138698,-9.603296,-9.821032,-5.037471,7.852959,6.323818,5.445488,8.229274,3.460060,3.353025,-6.343063,-1.869617,-1.231730,8.229742,2.667746,-8.974167,-2.754426,-2.311288,1.076454,-1.755824,-4.332618,-1.850842,-0.033868,8.148149,6.148052,9.722489,8.080499,2.184398,-6.755212,-8.938206,2.477192,0.696761,-6.395848,-2.752481,4.639872,-9.682581,0.870798,5.780997,-2.982138,5.926672,1.199957,-8.158373,-0.957901,7.688933,-7.842423,-8.428984,-7.821848,7.465675,-8.150756,-8.696338,-0.003808,0.744019,-3.086136,9.901216,0.477479,-3.882749,3.688409,-7.444600,-1.089086,-2.436812,7.381495,8.639607,0.303575,-8.658503,-2.796471,8.776311,-6.077576,-1.978081,6.690671,8.873949,-6.465227,3.067055,-5.252292,-3.068999,2.296456,3.853640,4.241186,1.744325,0.925574,-1.606422,-9.149066,5.923580,6.343363,8.138941,2.329512,6.914278,5.795377,-9.223279,-4.693281,-1.920239,0.903693,0.569705,-1.176087,4.209204,-9.492678,-2.826096,9.134213,0.439424,8.043765,6.773672,-1.916844,4.845122,-1.519107,0.110881,-5.070176], dtype = "float64")#candidate|4101|(650,)|const|float64
call_4100 = relay.TupleGetItem(func_2315_call(relay.reshape(const_4101.astype('float64'), [13, 10, 5])), 0)
call_4102 = relay.TupleGetItem(func_2318_call(relay.reshape(const_4101.astype('float64'), [13, 10, 5])), 0)
func_2011_call = mod.get_global_var('func_2011')
func_2015_call = mutated_mod.get_global_var('func_2015')
const_4119 = relay.const([-9.924020,-0.415979,-6.045140,6.682267,-8.266683,-2.643407,-7.018241,-9.315881,1.672422,-7.486776,7.046252,8.718449,4.218863,-6.780335,-7.252386,8.161165,3.705047,0.086444,4.867388,-4.273469,6.476710,1.662903,-5.008166,3.361384,-2.076364,-5.701546,-8.821706,6.904710,7.968466,5.689715,-7.669595,-8.663474,-1.216253,-7.485128,9.506395,5.328720,0.114173,-1.265459,-1.851243,-3.452984,-2.350505,-9.690888,-9.277280,-6.287810,4.255271,5.588209,-6.980893,-6.546701,-2.017710,-9.991094,5.130768,-0.833381,-7.941119,-4.025112,-7.752101,2.503661,-9.259784,9.617366,8.483132,-5.617379,8.177727,2.753794,-9.890526,-0.571802,-1.479318,-4.564523,5.266975,-2.668528,6.094947,-8.223560,7.279839,-4.567041,-2.133917,0.375509,6.873518,-4.984607,7.873684,-0.343469,1.781186,-6.339925,0.482005,1.784624,8.429743,-8.669559,8.107804,-5.326438,-0.113546,-8.367356,5.301887,3.917628,7.161891,5.029877,2.214588,-0.393359,1.011503,-0.005498,7.395185,1.011955,8.270468,-1.489376,-0.088059,-8.801814,0.661781,3.938639,-7.720873,-0.745433,4.134287,-9.286466,0.893604,8.712273,-7.394062,-1.608176,-1.990402,-8.652670,7.910408,-5.517235,-3.892675,9.790084,2.143591,-9.326694,8.555771,8.021984,-4.547588,4.840626,2.040855,-4.296321,-7.651037,4.032958,-4.682370,-0.198394,-4.945198,-2.607787,4.782396,7.033857,-8.157842,-0.661107,-9.746156,-5.217741,-4.672719,-3.602244,9.857377,4.712400,6.004754,-5.788660,-8.422890,-7.225220,8.351927,4.973158,-3.099959,7.000688,-4.510292,-7.335165,5.635602,-9.005741,-1.378139,0.206924,5.841900,4.307193,-8.936975,6.484800,-8.557557,5.330660,-4.533166,5.220174,1.316595,0.228068,-2.056278,-5.750286,1.670015,3.579378,-7.332382,2.105311,4.775406,-8.447947,-7.846370,0.209220,6.136621,-5.938589,0.168290,-3.361024,-6.170183,3.223225,7.165647,-5.805558,-1.071039,-8.392090,1.147826,-0.551099,-8.513363,-1.167315,-8.704262,-6.838063,-7.420421,8.198276,-3.293370,7.086886,-2.784308,9.742403,-6.348065,-7.093273,-2.383975,5.298342,-1.786941,-3.961722,1.181299,0.707468,-9.294965,0.269777,-2.939599,7.464804,0.489310,4.455446,8.149398,6.430802,-4.758716,-2.450578,1.341529,-1.261566,4.658508,-2.685448,9.819200,5.534929,8.096892,3.889261,5.139377,-6.737613,1.991112,-9.060344,8.512961,-9.121640,2.889071,-7.729643,8.028441,-8.509419,1.145395,8.394449,-5.326710,0.292344,3.876850,6.345567,1.354656,0.727435,6.167760,8.606110,-1.476680,3.754035,-2.941539,-3.650567,-5.803310,-7.003985,2.066763,9.032684,-0.823024,-5.408101,8.600609,6.411169,5.607523,4.255517,-0.108276,9.044453,-7.560163,9.573493,-5.034464,-9.853476,-1.062388,7.602004,-3.059210,-8.612312,1.450335,9.623294,-2.682023,5.254222,8.167516], dtype = "float64")#candidate|4119|(273,)|const|float64
const_4120 = relay.const([-4.429429,7.518208,-5.225452,0.029398,-9.232705,5.832907,-0.820667,-5.215501,6.705204,3.541774,-8.728799,0.732568,9.652910,-6.871441,-4.814822,-7.564361,-4.288240,-2.525479,0.044961,1.717087,-6.395862,4.343349,1.004513,2.001980,2.682395,8.169465,-1.588541,1.046987,7.719681,-0.411678,9.046541,6.365504,-5.840624,-4.967582,0.852370,-4.473017,2.048682,-6.727055,0.880235,8.781624,-1.655142,8.519051,0.069321,8.166363,-0.235604,-0.798034,-0.011878,6.440994,-9.377411,-5.814525,-0.193536,2.940587,3.485303,-4.267971,1.377060,3.362144,-8.694348,-6.030310,-6.748912,-0.261778,-0.710373,-4.183498,-7.646262,8.387167,-2.367929,0.409006,-5.581580,-4.003016,-8.090462,5.017812,-4.801486,-7.686190,7.805036,-8.027524,-1.358289,-2.405552,2.231202,8.012133,8.767735,-6.802356,-5.757869,-1.561275,-8.459996,-6.862259,4.574832,-7.041937,0.267773,-3.813874,-5.072953,-0.499307,5.440944,1.375627,4.615127,1.888819,8.901678,-4.533239,1.188690,9.190209,4.328485,-7.632557], dtype = "float32")#candidate|4120|(100,)|const|float32
call_4118 = relay.TupleGetItem(func_2011_call(relay.reshape(const_4119.astype('float64'), [13, 3, 7]), relay.reshape(const_4120.astype('float32'), [100,]), ), 9)
call_4121 = relay.TupleGetItem(func_2015_call(relay.reshape(const_4119.astype('float64'), [13, 3, 7]), relay.reshape(const_4120.astype('float32'), [100,]), ), 9)
func_2201_call = mod.get_global_var('func_2201')
func_2206_call = mutated_mod.get_global_var('func_2206')
var_4128 = relay.var("var_4128", dtype = "int32", shape = (135,))#candidate|4128|(135,)|var|int32
call_4127 = relay.TupleGetItem(func_2201_call(relay.reshape(const_4120.astype('float64'), [25, 4]), relay.reshape(var_4128.astype('int32'), [135,]), relay.reshape(const_4119.astype('float64'), [39, 7]), ), 2)
call_4129 = relay.TupleGetItem(func_2206_call(relay.reshape(const_4120.astype('float64'), [25, 4]), relay.reshape(var_4128.astype('int32'), [135,]), relay.reshape(const_4119.astype('float64'), [39, 7]), ), 2)
var_4138 = relay.var("var_4138", dtype = "float32", shape = (100,))#candidate|4138|(100,)|var|float32
bop_4139 = relay.bitwise_or(const_4120.astype('int8'), relay.reshape(var_4138.astype('int8'), relay.shape_of(const_4120))) # shape=(100,)
output = relay.Tuple([call_4081,call_4096,var_4097,call_4100,const_4101,call_4118,const_4119,call_4127,var_4128,bop_4139,])
output2 = relay.Tuple([call_4082,call_4098,var_4097,call_4102,const_4101,call_4121,const_4119,call_4129,var_4128,bop_4139,])
func_4149 = relay.Function([var_4097,var_4128,var_4138,], output)
mod['func_4149'] = func_4149
mod = relay.transform.InferType()(mod)
mutated_mod['func_4149'] = func_4149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4149_call = mutated_mod.get_global_var('func_4149')
var_4151 = relay.var("var_4151", dtype = "uint64", shape = (560,))#candidate|4151|(560,)|var|uint64
var_4152 = relay.var("var_4152", dtype = "int32", shape = (135,))#candidate|4152|(135,)|var|int32
var_4153 = relay.var("var_4153", dtype = "float32", shape = (100,))#candidate|4153|(100,)|var|float32
call_4150 = func_4149_call(var_4151,var_4152,var_4153,)
output = call_4150
func_4154 = relay.Function([var_4151,var_4152,var_4153,], output)
mutated_mod['func_4154'] = func_4154
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4173 = relay.var("var_4173", dtype = "uint64", shape = ())#candidate|4173|()|var|uint64
var_4174 = relay.var("var_4174", dtype = "uint64", shape = (9, 16, 9))#candidate|4174|(9, 16, 9)|var|uint64
bop_4175 = relay.maximum(var_4173.astype('uint64'), var_4174.astype('uint64')) # shape=(9, 16, 9)
bop_4198 = relay.left_shift(var_4174.astype('uint64'), relay.reshape(bop_4175.astype('uint64'), relay.shape_of(var_4174))) # shape=(9, 16, 9)
const_4201 = relay.const([[[-3,-9,-6,-10,-4,4,9,9,-10],[10,4,7,2,7,-1,-9,1,-3],[-1,-6,10,-4,-1,-1,-7,-9,8],[10,1,-9,4,-9,8,-4,8,7],[-9,-9,5,3,2,2,9,-10,-9],[-5,9,-10,7,-9,3,3,6,-2],[3,-10,9,-6,5,-9,7,9,-7],[4,-4,-8,-8,1,-4,-4,8,1],[7,6,-3,6,8,-7,-8,-10,3],[-1,1,-6,5,-10,-3,8,10,2],[8,5,-5,2,3,-8,-2,-9,1],[7,-3,-6,-10,8,8,-5,-10,-4],[-3,10,10,2,7,6,7,3,-10],[6,-5,2,-6,2,9,1,-2,-8],[9,6,-1,3,6,8,6,10,10],[-7,-10,2,-4,-1,-6,-1,-1,10]],[[-9,-10,10,5,-5,9,6,4,6],[-5,-1,-9,7,9,-8,10,1,-4],[-9,6,3,-1,-3,5,9,4,-8],[6,-4,3,-1,1,4,-2,6,9],[5,-8,-3,2,5,-3,-10,10,3],[7,-6,-7,-8,5,8,5,4,-4],[6,-2,-1,-6,3,6,-9,9,3],[-8,-4,5,9,-5,-3,1,-6,-2],[7,9,-4,-5,8,-8,1,-2,-9],[6,8,10,-2,-3,-3,7,-3,-1],[3,-9,1,4,3,6,4,7,-5],[3,7,8,-1,1,3,-4,-7,7],[-10,9,-8,5,-7,4,-1,-9,-3],[8,2,-1,-1,-1,-7,6,1,3],[8,-1,-2,7,10,-4,3,-8,-3],[-7,-3,1,-9,9,10,-9,-10,5]],[[5,-7,-8,-9,-5,5,5,10,-2],[-8,-8,1,9,-10,2,2,7,-2],[2,-5,8,3,-2,1,-6,5,8],[-5,9,7,-1,9,-10,-3,2,-1],[8,4,-9,-3,6,2,-7,-10,-2],[-6,-5,1,7,10,-1,-2,7,8],[2,2,1,-1,-10,-3,-7,-5,5],[10,9,-1,-2,-9,8,-6,1,8],[3,10,-2,6,-3,4,9,10,-5],[-8,4,10,7,4,-4,-9,4,2],[2,7,-1,3,-6,-7,6,2,5],[3,7,-9,10,10,5,1,-10,-5],[3,10,-3,-4,2,-8,-7,-8,-6],[5,-3,1,-9,-7,5,9,-10,-7],[5,9,-5,-4,-7,7,9,3,-1],[2,-9,8,-1,-9,-7,3,8,-1]],[[10,-7,10,-2,10,-1,-10,-10,1],[2,-6,-2,-7,-6,8,10,-5,-5],[-1,-3,4,1,-6,4,6,7,7],[4,6,-1,-7,2,-5,6,6,8],[-1,6,7,-5,6,-6,3,8,-2],[-4,9,-1,-3,-4,-4,10,1,-5],[6,3,1,-4,9,-4,1,10,-3],[8,-7,8,-5,9,4,4,3,1],[-7,8,7,7,-1,-9,7,2,-2],[-7,1,-2,-1,5,2,-8,1,4],[-10,-7,9,5,5,-2,-10,-3,7],[5,2,2,8,-4,7,-8,-1,6],[-10,8,10,4,10,-10,3,-9,-7],[-8,2,-5,-9,6,5,2,4,-3],[-9,-6,-4,-10,-4,-1,-1,-6,-10],[1,-4,-3,-8,-8,-2,-7,-10,4]],[[1,-1,4,-6,1,-7,4,2,5],[-9,-10,-3,8,5,-5,1,6,9],[-4,-4,-8,7,9,2,-5,-6,7],[-7,-1,4,5,2,-7,-1,7,-5],[-8,-8,2,-2,-10,3,-8,-4,-7],[7,-4,-3,-9,2,-10,10,9,-7],[-6,9,-9,-5,5,8,-8,3,-1],[2,1,-3,-3,10,-10,5,8,-4],[-8,-4,10,4,6,-3,4,-8,-1],[7,-5,-8,-6,3,-8,-2,7,9],[9,-9,-5,-3,-8,-5,1,3,-10],[1,3,-1,10,-7,-1,-8,2,-5],[-10,5,9,-6,-1,-6,-1,7,10],[5,3,-9,-8,3,4,8,-8,9],[4,-10,6,6,-5,-1,2,7,8],[10,-4,-10,2,-2,3,-2,9,-2]],[[9,4,2,3,3,-9,-7,-9,-1],[1,8,-8,7,6,3,4,-5,-8],[-6,-10,10,-10,-8,1,-1,-5,-6],[-8,2,-2,1,6,4,2,6,9],[-1,6,1,1,8,8,10,10,9],[8,7,7,-2,3,1,6,2,-5],[7,-6,-3,-2,10,6,3,-3,-10],[2,-9,7,-7,-6,-3,4,7,7],[-4,-3,-1,8,-3,-4,9,-4,-1],[10,4,-10,5,10,-6,1,6,-6],[5,10,-5,10,10,-4,-6,2,-10],[-8,-8,8,5,-4,5,7,4,-9],[-2,4,-4,-7,-3,-8,-1,10,5],[3,-7,-1,7,-2,7,-3,-10,-3],[5,3,-8,5,-1,1,10,8,-1],[10,8,10,-3,4,-9,-10,-8,-6]],[[-5,-6,-5,4,10,-3,-10,-10,6],[4,4,5,-7,-2,7,1,-9,2],[-5,9,6,-8,-6,-7,-10,-2,-10],[-10,3,4,-9,5,2,-4,-2,2],[-7,-6,-9,-5,-5,3,-7,6,2],[9,-3,-9,-10,1,6,-1,6,-5],[-2,3,-1,-5,-9,6,1,3,2],[8,-7,-5,6,5,5,8,4,7],[10,-4,4,-2,-7,-8,9,2,-9],[-10,-3,9,-6,-7,10,8,7,9],[-1,-6,-6,-9,2,-2,8,-8,-6],[1,3,6,2,-3,3,-2,-3,-3],[5,-5,-3,10,10,4,-4,-9,3],[-8,9,-7,3,7,10,-6,-3,-3],[-1,-10,10,6,9,1,-3,10,-2],[4,-6,1,10,2,10,2,8,-2]],[[-5,2,-6,-7,-4,10,-4,1,-3],[8,2,9,-5,3,10,-2,4,9],[9,-8,5,-8,2,10,2,1,10],[-5,-8,8,4,4,-6,-7,-1,7],[-2,-4,2,10,-6,7,-10,10,-1],[-7,-8,2,-4,-8,-3,-10,10,9],[-7,-8,-9,-8,-7,6,-7,-2,4],[9,-4,-4,4,2,-5,7,-10,-7],[-2,-10,5,9,-9,-7,9,-4,6],[10,9,5,-2,9,9,-3,-3,4],[-8,-10,-5,3,-6,5,-4,-2,-6],[10,1,-2,-7,3,-9,-8,9,-6],[-8,6,-8,7,-5,-7,-8,-1,-6],[9,-1,3,-1,-8,10,3,-5,-3],[-2,-4,-9,-10,-8,8,-5,5,-1],[-7,-9,3,9,9,-6,6,5,7]],[[-3,-3,-9,2,7,-1,8,-1,2],[-8,9,-4,4,-5,2,-2,-10,-5],[-3,-6,-6,9,6,3,-3,9,-2],[8,-5,-2,-4,3,9,-6,6,-5],[10,8,-5,4,-4,9,-5,2,10],[8,-10,10,8,-6,-8,7,-6,-4],[8,10,-2,-9,-5,-9,-5,-1,-8],[6,6,2,-4,6,6,2,9,-7],[10,7,7,2,-3,-8,-3,8,-8],[-7,-1,-2,-2,-2,-6,-9,-7,2],[2,-5,-7,7,9,1,-10,-10,1],[10,8,-4,3,9,-2,1,6,-1],[10,5,5,-9,-4,6,2,-9,-7],[3,6,9,4,2,-9,5,10,9],[3,10,6,5,1,-8,-8,-10,4],[4,3,-8,-10,-2,-10,-6,8,4]]], dtype = "uint64")#candidate|4201|(9, 16, 9)|const|uint64
bop_4202 = relay.right_shift(bop_4175.astype('int64'), relay.reshape(const_4201.astype('int64'), relay.shape_of(bop_4175))) # shape=(9, 16, 9)
func_809_call = mod.get_global_var('func_809')
func_812_call = mutated_mod.get_global_var('func_812')
var_4206 = relay.var("var_4206", dtype = "float32", shape = (648,))#candidate|4206|(648,)|var|float32
call_4205 = relay.TupleGetItem(func_809_call(relay.reshape(var_4206.astype('float32'), [9, 9, 8])), 0)
call_4207 = relay.TupleGetItem(func_812_call(relay.reshape(var_4206.astype('float32'), [9, 9, 8])), 0)
output = relay.Tuple([bop_4198,bop_4202,call_4205,var_4206,])
output2 = relay.Tuple([bop_4198,bop_4202,call_4207,var_4206,])
func_4208 = relay.Function([var_4173,var_4174,var_4206,], output)
mod['func_4208'] = func_4208
mod = relay.transform.InferType()(mod)
var_4209 = relay.var("var_4209", dtype = "uint64", shape = ())#candidate|4209|()|var|uint64
var_4210 = relay.var("var_4210", dtype = "uint64", shape = (9, 16, 9))#candidate|4210|(9, 16, 9)|var|uint64
var_4211 = relay.var("var_4211", dtype = "float32", shape = (648,))#candidate|4211|(648,)|var|float32
output = func_4208(var_4209,var_4210,var_4211,)
func_4212 = relay.Function([var_4209,var_4210,var_4211,], output)
mutated_mod['func_4212'] = func_4212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1415_call = mod.get_global_var('func_1415')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_4216 = relay.TupleGetItem(func_1415_call(), 2)
call_4217 = relay.TupleGetItem(func_1417_call(), 2)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_4234 = relay.TupleGetItem(func_1454_call(relay.reshape(call_4216.astype('float32'), [100,])), 0)
call_4235 = relay.TupleGetItem(func_1456_call(relay.reshape(call_4216.astype('float32'), [100,])), 0)
func_2357_call = mod.get_global_var('func_2357')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_4251 = relay.TupleGetItem(func_2357_call(), 0)
call_4252 = relay.TupleGetItem(func_2358_call(), 0)
output = relay.Tuple([call_4216,call_4234,call_4251,])
output2 = relay.Tuple([call_4217,call_4235,call_4252,])
func_4269 = relay.Function([], output)
mod['func_4269'] = func_4269
mod = relay.transform.InferType()(mod)
mutated_mod['func_4269'] = func_4269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4269_call = mutated_mod.get_global_var('func_4269')
call_4270 = func_4269_call()
output = call_4270
func_4271 = relay.Function([], output)
mutated_mod['func_4271'] = func_4271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2807_call = mod.get_global_var('func_2807')
func_2809_call = mutated_mod.get_global_var('func_2809')
call_4309 = func_2807_call()
call_4310 = func_2807_call()
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_4319 = relay.TupleGetItem(func_1891_call(), 0)
call_4320 = relay.TupleGetItem(func_1892_call(), 0)
func_3762_call = mod.get_global_var('func_3762')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_4325 = func_3762_call()
call_4326 = func_3762_call()
output = relay.Tuple([call_4309,call_4319,call_4325,])
output2 = relay.Tuple([call_4310,call_4320,call_4326,])
func_4339 = relay.Function([], output)
mod['func_4339'] = func_4339
mod = relay.transform.InferType()(mod)
output = func_4339()
func_4340 = relay.Function([], output)
mutated_mod['func_4340'] = func_4340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_4408 = relay.TupleGetItem(func_3036_call(), 2)
call_4409 = relay.TupleGetItem(func_3038_call(), 2)
func_3343_call = mod.get_global_var('func_3343')
func_3344_call = mutated_mod.get_global_var('func_3344')
call_4424 = func_3343_call()
call_4425 = func_3343_call()
output = relay.Tuple([call_4408,call_4424,])
output2 = relay.Tuple([call_4409,call_4425,])
func_4433 = relay.Function([], output)
mod['func_4433'] = func_4433
mod = relay.transform.InferType()(mod)
mutated_mod['func_4433'] = func_4433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4433_call = mutated_mod.get_global_var('func_4433')
call_4434 = func_4433_call()
output = call_4434
func_4435 = relay.Function([], output)
mutated_mod['func_4435'] = func_4435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3762_call = mod.get_global_var('func_3762')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_4451 = func_3762_call()
call_4452 = func_3762_call()
func_4075_call = mod.get_global_var('func_4075')
func_4077_call = mutated_mod.get_global_var('func_4077')
call_4453 = relay.TupleGetItem(func_4075_call(), 0)
call_4454 = relay.TupleGetItem(func_4077_call(), 0)
output = relay.Tuple([call_4451,call_4453,])
output2 = relay.Tuple([call_4452,call_4454,])
func_4475 = relay.Function([], output)
mod['func_4475'] = func_4475
mod = relay.transform.InferType()(mod)
mutated_mod['func_4475'] = func_4475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4475_call = mutated_mod.get_global_var('func_4475')
call_4476 = func_4475_call()
output = call_4476
func_4477 = relay.Function([], output)
mutated_mod['func_4477'] = func_4477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3514_call = mod.get_global_var('func_3514')
func_3516_call = mutated_mod.get_global_var('func_3516')
call_4519 = relay.TupleGetItem(func_3514_call(), 4)
call_4520 = relay.TupleGetItem(func_3516_call(), 4)
output = call_4519
output2 = call_4520
func_4537 = relay.Function([], output)
mod['func_4537'] = func_4537
mod = relay.transform.InferType()(mod)
mutated_mod['func_4537'] = func_4537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mutated_mod.get_global_var('func_4537')
call_4538 = func_4537_call()
output = call_4538
func_4539 = relay.Function([], output)
mutated_mod['func_4539'] = func_4539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2250_call = mod.get_global_var('func_2250')
func_2252_call = mutated_mod.get_global_var('func_2252')
call_4596 = func_2250_call()
call_4597 = func_2250_call()
func_2315_call = mod.get_global_var('func_2315')
func_2318_call = mutated_mod.get_global_var('func_2318')
const_4637 = relay.const([-5.672262,2.181222,-9.601663,5.144086,1.728694,-8.047779,-2.994512,-1.081417,8.582109,-7.961846,-5.452386,1.704963,8.550876,-3.093299,6.904389,2.080853,1.735467,-6.564545,0.447233,-1.493604,4.356807,-9.377939,-6.865080,9.333361,4.258389,5.442112,-7.216448,5.965690,-4.907959,4.128836,8.363201,6.191464,3.025061,-9.974536,1.406208,-0.858731,2.458103,-4.125176,6.359493,-8.194405,9.811885,-0.421099,-9.577651,-7.577786,4.945626,-6.078120,-7.886289,2.077813,2.205995,-2.974744,-2.867923,8.350969,-4.352489,7.690716,8.824381,-1.273355,7.826233,-2.976200,6.323781,-7.740770,-0.111106,8.939024,2.357604,9.237155,-4.592559,5.688490,-2.371213,-5.971891,1.441160,-3.052691,5.564384,2.747225,0.026309,-3.912489,-2.504153,8.240460,1.868155,3.167876,1.204307,3.866777,0.976553,-4.156446,4.935338,-3.539014,-0.521492,9.698096,1.519139,-8.154948,7.973919,7.977421,0.390340,-5.760346,3.727155,0.372759,-6.616692,-2.179295,-8.838230,7.234317,-7.938470,-0.584704,-6.383955,-2.776147,-3.989812,-5.058806,-7.353667,-2.861115,-7.032619,-6.909720,-1.812861,-5.601928,9.197806,-0.365368,2.455022,2.892281,0.789335,-8.040393,-5.676527,-6.566773,9.869125,-2.211665,-2.801630,-4.993583,8.841920,0.452681,-2.368880,7.995808,-2.460159,4.721345,6.253107,7.961804,-4.437511,2.784064,1.380204,-1.697664,-0.125695,-4.299063,3.129379,-2.185917,8.249270,-1.505325,2.631297,3.639027,-3.731193,-0.970413,-6.412248,-2.472721,3.152003,1.331281,1.966653,-4.719059,-2.779674,4.606675,5.370298,-9.937388,8.058064,-3.653002,-5.654567,-3.635580,1.865455,1.505926,9.505637,-3.067783,6.537348,9.942728,8.076599,-9.653083,-1.686890,1.051721,8.152136,-8.138483,0.552241,-4.314210,0.743929,-2.106556,2.703471,-9.359624,1.950396,7.244804,-6.921361,-9.047865,-2.570686,5.501514,-5.301465,-6.224071,-9.856106,-4.212298,-9.742424,-5.100167,8.436135,-4.065332,-7.627657,6.343008,0.701677,-4.977851,4.153077,-4.879807,2.886084,-9.993633,-0.911326,-3.878259,-1.222296,-8.485887,8.942305,-7.524794,7.900461,2.475528,9.909129,-6.522144,0.801096,-9.121536,6.885542,8.744690,-6.166757,-8.624652,-4.784250,8.236350,6.532790,7.906905,-6.340556,9.778223,-0.629099,3.955273,-2.717430,3.868743,-0.836927,-8.795940,-2.008509,8.200316,-2.400887,8.363514,-7.361724,1.304473,0.357813,-7.630895,-1.935572,0.197380,-0.619827,-4.953799,-8.438530,-6.345824,0.228209,-8.955156,-3.743409,-3.921823,4.694911,-9.742690,-2.467955,0.460793,-6.721019,-4.482166,-9.122491,-4.281534,-8.057630,7.565897,-5.271200,-0.657925,-8.266396,8.568645,-5.618085,1.217766,9.403940,1.851264,0.965639,3.623636,-6.447206,-3.386712,-5.335966,4.155641,5.432883,3.491953,-2.429114,3.203446,6.235549,-2.598598,-4.612726,6.418417,9.839674,-4.784071,-9.217189,-8.464177,5.879248,5.484100,5.901264,-6.884415,1.120291,-4.100370,7.630425,-2.141355,-8.264773,-4.623989,9.890650,4.706534,-2.805791,5.926899,6.190084,6.614998,6.859489,-2.086758,0.686954,8.980650,7.399664,7.920003,-1.589155,6.524681,-0.708345,0.619489,3.401992,-9.978511,-8.947606,-9.172229,7.104047,-0.005583,-6.199514,-3.092622,-3.012159,-4.778274,1.323359,-8.351701,-5.569525,5.121591,-5.142672,-5.632798,1.531619,9.390102,-8.893922,7.011018,-1.830540,-6.939260,6.373296,-2.379624,5.539347,0.891168,-6.866224,-8.113125,8.565962,5.210270,-9.556438,4.426595,-9.298531,-4.921709,2.068547,1.242972,4.755938,-2.413241,-2.834866,-3.023100,-9.487527,-5.233354,-2.491104,4.381432,-4.786010,8.498120,-2.355019,-3.787914,8.601295,4.251429,4.883555,-9.665678,1.687182,1.036675,-3.331040,4.716307,3.941932,8.775899,-1.080815,7.845250,-7.210740,1.695485,9.735826,5.751577,-5.181688,0.467469,0.867062,9.156639,7.800019,-5.785293,-7.473472,-5.681237,-1.120308,1.488425,-7.662931,5.626133,1.940118,4.845303,4.424290,-4.117732,9.726278,5.449532,0.416351,9.576353,7.897244,-6.340176,7.269236,4.930987,8.512143,-1.333380,8.442430,-3.588868,5.682648,1.024133,-9.327548,-9.337494,-1.394138,2.236151,-1.207187,-2.980174,-0.665292,-7.986833,4.624292,9.549333,-9.186088,-9.573704,-1.302973,6.612511,-0.366646,-5.290522,-4.699633,-4.902746,-4.254947,-6.419499,7.127012,-7.002396,-7.533644,0.083458,-0.170049,-6.918167,2.480842,-4.506473,1.620193,8.293944,-4.545337,-8.040709,-9.333618,9.151501,-5.346912,-6.696442,-7.694407,-2.850639,2.937856,-9.129060,-2.962725,-2.754906,7.225880,2.705117,-7.313731,-2.750788,-4.215714,4.798284,-0.687561,5.473467,1.972959,-9.517112,-3.639138,-1.974980,-8.871323,5.986791,8.623141,-9.817307,-2.459261,2.001993,-3.405924,-5.314324,-3.496959,-2.263737,-7.814324,-9.204078,1.116902,-2.777977,1.854049,2.770545,6.961446,-7.655501,-7.385041,-1.221568,6.747140,-3.800571,0.399106,-8.725255,-7.722337,-7.833764,0.287189,-6.486608,5.771118,-3.376362,7.467980,6.526910,4.853227,9.878069,-1.036208,-4.448138,4.739493,-9.920660,8.274985,8.534707,1.320701,5.380914,-1.380324,7.702972,-0.674050,-8.358130,0.897493,-5.737213,4.043930,-0.443622,8.708027,7.862471,0.773201,-0.027004,8.962353,0.962878,6.275402,6.940068,-0.675434,-6.593450,-9.263844,4.991052,-4.891647,-0.550014,6.758269,4.856160,-6.083879,-9.910664,-2.552300,-5.221184,-7.701176,-6.220120,-9.870911,9.372530,-1.407441,2.171209,-1.098935,-3.220937,9.806594,-5.274289,-0.621442,1.969581,0.782598,-9.975951,-5.021480,9.470650,-6.957383,9.385182,8.692709,-6.879968,-0.543054,-2.360894,-6.926319,2.288372,-9.619326,-3.680360,7.288499,0.921974,0.464907,7.396772,-3.787705,-8.399213,-0.394963,-2.155176,-0.538449,-8.121537,-2.268831,8.004878,2.113151,-2.383899,1.201531,-8.707523,5.472400,2.209532,-4.024473,-0.779813,1.234995,2.112579,-2.796494,2.160539,-1.300259,3.166288,-6.337066,0.073641,1.779632,9.441941,9.658475,-4.563777,9.988616,5.446402,-1.003639,2.964289,2.631520,6.979147,-1.936750,-1.047457,-5.010784,7.334598,6.487870,1.491524,3.534376,6.497750,-0.779905,6.715016,2.967758,8.578423,-2.964401,6.381359,-0.986254,-2.500116,8.979748,5.174662,-1.438950,-2.225012,-5.221008,4.974603,0.723027,-9.236095,-3.534126,7.657521,-9.206368,2.787986,2.329172,-3.603107,2.012143,-7.705155,-0.171537,3.409262,7.313857,-6.824896,0.562848,6.942538,-7.898513,-1.223777,3.198920,-7.547838,2.611060,-3.559504,-0.766653,-7.886036,6.895074,-9.331216,-2.857969,2.535852,6.070827,1.351554,9.823416,6.198085,-3.386096,-0.923528,-6.745479,-3.515426,-9.678222,-9.607286,9.325676,-2.758059], dtype = "float64")#candidate|4637|(650,)|const|float64
call_4636 = relay.TupleGetItem(func_2315_call(relay.reshape(const_4637.astype('float64'), [13, 10, 5])), 0)
call_4638 = relay.TupleGetItem(func_2318_call(relay.reshape(const_4637.astype('float64'), [13, 10, 5])), 0)
bop_4643 = relay.mod(const_4637.astype('float32'), relay.reshape(call_4636.astype('float32'), relay.shape_of(const_4637))) # shape=(650,)
bop_4646 = relay.mod(const_4637.astype('float32'), relay.reshape(call_4638.astype('float32'), relay.shape_of(const_4637))) # shape=(650,)
func_809_call = mod.get_global_var('func_809')
func_812_call = mutated_mod.get_global_var('func_812')
const_4682 = relay.const([5.555949,2.147618,-6.742123,-3.525568,-3.479540,9.673377,5.065205,6.774631,3.081389,-3.613251,1.646980,3.714556,8.094397,-2.143338,-6.707884,2.583554,6.036784,-9.052268,-7.911054,-3.350281,1.018196,-1.688391,-8.676833,4.356186,9.259857,7.564002,6.509390,-6.929902,-4.781281,9.584050,0.690530,6.614155,0.952906,-3.342883,-6.977170,7.653345,-5.122397,-6.822372,1.406258,-7.766849,1.304156,-4.210002,-0.382772,5.391408,6.993809,2.182425,0.955870,5.872367,-8.893705,7.506612,3.785607,-1.618721,-9.410655,-7.298256,-7.892570,-6.515900,4.682137,-4.849857,2.772759,-5.401118,-1.119441,-4.237145,-8.583922,9.197873,6.261635,0.648586,8.821910,0.325951,-5.480523,0.321677,-7.017092,-6.597999,-1.861341,-3.425227,2.258588,-1.243740,-7.756769,8.466758,0.423930,-8.980991,7.412811,8.163470,3.061951,-8.247406,-2.433740,8.235859,2.136123,-3.224053,-6.747111,-9.858102,-1.772006,-8.537145,1.202935,8.477831,-3.133872,9.796397,-9.682277,-9.616374,9.102912,5.503918,-3.747470,1.120378,0.870485,-4.385700,-8.208861,7.234770,8.588782,7.218494,1.099560,1.509573,-5.226169,-3.497854,1.611540,2.985047,8.632967,2.719104,6.159422,-4.441180,-5.482509,-3.130525,9.621604,9.381139,7.230533,7.088654,-9.885673,-7.733437,9.134861,4.562185,0.019373,-7.123794,8.906340,8.050075,-5.789398,1.415653,-3.111385,8.027726,2.953284,-0.212661,9.007816,-6.221064,3.018858,8.882877,2.399221,8.434668,1.214860,8.218021,8.145683,3.625260,-1.646111,9.993950,-6.842057,-6.403820,2.377028,7.231700,-6.713497,-9.400257,-5.216597,9.967782,-8.624174,1.617385,-1.924465,1.885333,1.182421,8.990576,2.832547,-3.228573,7.144773,-4.812690,7.129682,1.427330,1.194073,5.505164,5.066826,4.007620,-0.899490,4.253340,3.954919,-0.979694,0.905788,1.321160,-2.550302,2.532311,-5.978180,6.045517,6.512919,-7.200341,-5.645898,-9.709884,-6.800994,-2.029635,-6.600975,6.214230,-5.168746,-8.726065,4.493562,-3.736850,3.848286,5.543837,9.507150,-5.987619,3.265727,8.887555,-4.417264,-4.022559,2.269779,6.270718,-2.211123,-0.236120,0.860611,8.241247,-3.333181,-9.484577,9.491969,0.061804,-9.699520,8.720821,-7.469515,-8.374201,-0.931070,4.314116,5.727186,-7.078934,8.399545,-2.634275,9.357555,2.449375,7.965795,-0.369396,9.244396,-7.799869,5.147480,-6.907145,-0.481522,-1.496015,7.585364,4.980979,8.846758,-8.011559,-8.259133,4.164576,-1.902310,0.462067,-0.941543,-7.906247,6.594008,-0.563046,-0.173952,0.603446,9.227256,-9.104646,9.916279,5.851059,8.177535,-2.592441,-8.597970,8.034970,-8.416722,-5.227482,-9.004254,6.611581,7.397817,-2.626151,-3.311890,1.661895,-3.627846,-8.617409,9.407719,-8.052902,9.098632,-5.700159,-9.676133,2.970737,-4.813401,7.165571,-8.615159,-7.750922,-4.818647,-3.616893,-4.040931,-3.136250,9.781082,8.387074,-0.575844,3.561184,-4.162006,7.594138,9.987823,1.478960,8.009089,1.311122,9.428507,5.513199,-7.307987,-1.801677,9.796988,4.551226,6.940034,0.847543,-4.678886,-6.834496,-6.776927,4.956876,-6.439551,1.152043,-3.724312,5.319448,9.865671,5.702688,-8.515611,-9.741494,6.916947,-7.367887,-9.255459,-8.526454,-7.954025,9.525238,1.295608,6.631598,-9.085712,2.606802,0.772033,-4.849101,9.335017,-6.027774,-5.068614,-8.323609,3.855068,-7.925313,-0.095485,-4.435571,5.378612,-5.252404,6.850175,-7.319061,-1.990740,-8.509450,4.215998,-1.051395,-3.462262,-8.984490,-6.630671,-3.105691,-9.194068,8.298068,-6.171829,3.905803,-3.883576,-1.256284,0.051369,6.515408,-3.487635,5.843996,-5.079932,-3.959023,8.055144,8.355395,5.237433,1.380495,0.946501,7.211057,-8.966831,2.213300,-6.771220,-0.714978,1.442321,5.970461,2.373519,8.643960,9.145095,5.513745,-0.044253,-6.044631,-5.837473,1.869950,-2.769958,8.050085,-3.466413,7.751058,-6.552746,-4.324164,5.264678,6.175246,9.030636,0.802992,7.112564,2.801547,5.990777,7.076840,5.577157,7.697850,8.456796,-3.319265,-4.264874,-5.873300,-6.075451,-9.978973,9.393420,-1.521715,-6.653752,0.114193,-8.782726,4.698821,-3.135405,-9.739317,-8.556898,3.127072,-4.896339,8.602679,-3.024544,-2.238008,-5.177936,-9.685959,-4.864582,-9.541626,-8.396748,-4.300674,-7.289105,2.478770,6.950160,-2.008449,7.455143,8.297241,-9.125947,-4.963433,3.139017,6.596988,7.728634,8.758247,-4.588150,-9.168975,6.731967,-7.472140,2.019918,-6.729687,6.230598,-6.035623,-4.112949,-9.134947,-3.367837,7.045901,1.924427,7.662019,4.274735,5.711464,2.475161,-8.304663,-4.536569,-3.255947,-5.997174,-8.289872,-4.069231,6.668115,7.322500,1.549745,-8.620563,8.105283,0.001706,6.008653,8.206651,-4.696535,-4.174476,1.533945,5.032930,-3.477433,-7.118804,6.714303,3.545653,1.316040,0.305214,-0.943024,-3.285888,3.222378,9.676006,-6.474407,5.176408,4.656165,8.219746,8.478383,-2.178876,0.240862,-3.787755,3.937793,4.888419,-1.615580,9.348976,-1.053069,-6.129545,2.967350,-8.673790,-7.371991,5.159690,-4.370180,-8.972354,1.570418,6.190343,3.747673,-7.707984,-3.150439,-9.631312,-9.442882,1.299786,6.127536,-2.654902,5.432719,-7.179596,2.567344,1.507028,-0.535057,1.087628,8.316477,-3.199515,-9.774245,8.397458,-7.998323,-2.831069,-7.776312,-8.753819,6.041142,-2.151848,4.341452,5.537205,-0.137315,-7.156951,-4.248546,4.139655,4.221028,6.744733,-7.424782,-6.294319,-1.409180,3.086326,-1.705092,-9.283786,-5.689080,7.783612,5.951756,-5.443736,2.282036,-3.530314,-1.495213,8.871142,-8.362524,-7.350199,-7.651854,1.930524,7.800562,1.123081,-4.757787,5.356301,-1.317771,9.613483,8.667849,-2.829322,-6.064264,7.385449,-2.009101,-8.641263,6.693466,6.003628,0.802550,-7.138333,8.600794,3.230335,4.173160,-1.871724,1.612467,7.526551,-1.609728,6.750098,-6.491105,1.285875,-1.508199,1.363586,-4.017879,3.149525,-9.594402,-8.926664,7.894897,4.752681,9.978441,-6.579311,5.354447,5.776125,1.182982,0.824350,3.037066,-2.087683,-4.892062,4.533237,-4.840635,9.465104,-2.895766,-5.267309,5.870511,-1.025145,-8.362059,3.511162,-8.941657,2.797733,4.605330,-4.347516,8.226240,-9.645234,-8.864121,4.642443,-4.305426,5.462265,-0.335399,-1.194589,-2.362243,-6.460762,-5.230237,-9.116116,7.676143,-4.737460,-5.563961,3.799075,-4.615256,-5.961142,-4.938637,8.399948,-9.458663,2.628009,7.411189,-1.358263,7.358531,-2.206852,-2.050979,-9.296235,-5.187453,-4.899919,1.558057,-8.295415,-1.505815,6.065083,-8.705266,9.459477,8.744007,-0.008811,8.966654,-2.813798,3.782857,-7.067110,-0.984871,6.028713,9.368647,0.247041,-8.806509], dtype = "float32")#candidate|4682|(648,)|const|float32
call_4681 = relay.TupleGetItem(func_809_call(relay.reshape(const_4682.astype('float32'), [9, 9, 8])), 2)
call_4683 = relay.TupleGetItem(func_812_call(relay.reshape(const_4682.astype('float32'), [9, 9, 8])), 2)
bop_4684 = relay.logical_and(call_4596.astype('bool'), const_4682.astype('bool')) # shape=(2, 4, 648)
bop_4687 = relay.logical_and(call_4597.astype('bool'), const_4682.astype('bool')) # shape=(2, 4, 648)
func_4537_call = mod.get_global_var('func_4537')
func_4539_call = mutated_mod.get_global_var('func_4539')
call_4688 = func_4537_call()
call_4689 = func_4537_call()
output = relay.Tuple([bop_4643,call_4681,bop_4684,call_4688,])
output2 = relay.Tuple([bop_4646,call_4683,bop_4687,call_4689,])
func_4695 = relay.Function([], output)
mod['func_4695'] = func_4695
mod = relay.transform.InferType()(mod)
mutated_mod['func_4695'] = func_4695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4695_call = mutated_mod.get_global_var('func_4695')
call_4696 = func_4695_call()
output = call_4696
func_4697 = relay.Function([], output)
mutated_mod['func_4697'] = func_4697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4339_call = mod.get_global_var('func_4339')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_4701 = relay.TupleGetItem(func_4339_call(), 0)
call_4702 = relay.TupleGetItem(func_4340_call(), 0)
func_3173_call = mod.get_global_var('func_3173')
func_3176_call = mutated_mod.get_global_var('func_3176')
const_4706 = relay.const([-8,10,-10,-10,-7,2,9,-6,3,-2,-10,7,-5,1,2,3,-5,-9,1,-4,6,-8,7,5,-2,8,8,-1,-4,-2,-2,-8,8,-4,9,-7,-3,10,-9,-1,10,4,-7,-2,-9,9,9,-2,5,6,-3,8,8,-5,-3,-1,-6,-2,1,-3,-8,6,8,-6,4,-8,7,-3,6,-3,4,3,-8,-2,10,-1,-8,8,5,-10,8,-7,5,-9,10,9,7,-6,8,-5,-5,-7,-3,8,8,8,5,-10,-5,-1,-10,-1,-2,-1,-6,9,5,2,-2,8,8,8,1,-4,-7,-1,7,4,-8,-2,-3,4,8,6,6,-1,-9,-10,7,7,10,10,10,7,-1,2,1,-4,4,10,-3,6,2,-4,-1,2,9,-1,8,-6,-8,-6,4,7,-7,2,7,-4,6,-7,-9,10,-5,-6,10,3,-10,-6,-7,6,9,-8,6,5,-1,8,-5,7,-1,2,-7,-9,4,-5,8,6,9,-6,-5,-6,-5,-6,5,10,-10,-7,-9,-6,-4,3,2,1,-5,-4,-8,-9,-7,5,10,-7,-10,-7,-5,-10,-4,10,6,5,10,4,-2,-3,7,10,-3,-6,-3,10,4,6,-6,-3,-10,4,10,8,-10,-10,8,2,8,4,1,-9,5,4,-4,4,7,-5,-7,-10,3,3,1,3,-3,1,3,8,7,-1,-1,4,4,-5,-2,7,-5,7,6,-3,8,-3,-4,-1,7,10,7,-3,5,4,-1,3,3,-1,-1,-10,-8,2,-7,1,-4,-9,-8,6,10,-1,2,6,5,6,2,6,8,2,-2,-9,-5,-1,-1,-8,-6,-2,2,-6,7,-4,-8,9,-8,-3,-5,9,9,4,-5,-10,1,1,-10,-2,-1,-6,-9,-6,9,9,2,-3,-6,-2,1,-5,-4,8,5,10,8,-6,-4,-6,-4,6,-3,-10,6,-3,3,-9,-4,2,-1,-7,10,-8,8,7,8,-9,-2,1,2,-7,2,4,7,7,-8,-6,10,3,5,1,5,4,10,7,9,-6,2,-7,6,4,2,2,-4,-1,7,2,-3,-1,-4,-4,-4,6,-2,6,10,-10,2,2,7,2,-7,-9,-5,-3,1,-3,-2,3,-3,10,1,-4,3,6,1,-5,-6,-9,5,9,-3,-2,-1,-7,-6,-6,10,-7,-7,-5,4,-7,6,-9,-1,-8,-1,9,5,-6,6,7,1,-7,8,-9,3,1,5,10,-10,-10,7,1,-7,5,9,7,8,2,-7,-8,-6,-8,1,-7,-4,-10,-6,7,9,7,5,-2,10,-7,-3,-7,-4,-2,-3,-5,-5,2,-9,-7,2,-8,7,-8,-2,-6,-9,-7,-8,-1,-7,-9,-3,-8,-1,-3,-10,-8,1,-6,2,-9,4,6,-5,2,3,-6,4,1,10,6,4,-7,-1,-9,4,4,6,-8,8,4,-3,10,-6,-3,-6,6,-5,7,5,-7,-6,5,-2,4,6,1,-2,-9], dtype = "uint64")#candidate|4706|(560,)|const|uint64
call_4705 = relay.TupleGetItem(func_3173_call(relay.reshape(const_4706.astype('uint64'), [560,])), 2)
call_4707 = relay.TupleGetItem(func_3176_call(relay.reshape(const_4706.astype('uint64'), [560,])), 2)
func_4269_call = mod.get_global_var('func_4269')
func_4271_call = mutated_mod.get_global_var('func_4271')
call_4733 = relay.TupleGetItem(func_4269_call(), 0)
call_4734 = relay.TupleGetItem(func_4271_call(), 0)
func_3173_call = mod.get_global_var('func_3173')
func_3176_call = mutated_mod.get_global_var('func_3176')
call_4739 = relay.TupleGetItem(func_3173_call(relay.reshape(call_4705.astype('uint64'), [560,])), 3)
call_4740 = relay.TupleGetItem(func_3176_call(relay.reshape(call_4705.astype('uint64'), [560,])), 3)
bop_4742 = relay.left_shift(call_4701.astype('int16'), call_4705.astype('int16')) # shape=(2, 4, 560)
bop_4745 = relay.left_shift(call_4702.astype('int16'), call_4707.astype('int16')) # shape=(2, 4, 560)
output = relay.Tuple([const_4706,call_4733,call_4739,bop_4742,])
output2 = relay.Tuple([const_4706,call_4734,call_4740,bop_4745,])
func_4775 = relay.Function([], output)
mod['func_4775'] = func_4775
mod = relay.transform.InferType()(mod)
output = func_4775()
func_4776 = relay.Function([], output)
mutated_mod['func_4776'] = func_4776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_4789 = func_2494_call()
call_4790 = func_2494_call()
var_4840 = relay.var("var_4840", dtype = "float32", shape = (2, 4, 12))#candidate|4840|(2, 4, 12)|var|float32
bop_4841 = relay.not_equal(call_4789.astype('bool'), var_4840.astype('bool')) # shape=(2, 4, 12)
bop_4844 = relay.not_equal(call_4790.astype('bool'), var_4840.astype('bool')) # shape=(2, 4, 12)
output = bop_4841
output2 = bop_4844
func_4846 = relay.Function([var_4840,], output)
mod['func_4846'] = func_4846
mod = relay.transform.InferType()(mod)
var_4847 = relay.var("var_4847", dtype = "float32", shape = (2, 4, 12))#candidate|4847|(2, 4, 12)|var|float32
output = func_4846(var_4847)
func_4848 = relay.Function([var_4847], output)
mutated_mod['func_4848'] = func_4848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_4923 = relay.TupleGetItem(func_1647_call(), 2)
call_4924 = relay.TupleGetItem(func_1649_call(), 2)
output = relay.Tuple([call_4923,])
output2 = relay.Tuple([call_4924,])
func_4950 = relay.Function([], output)
mod['func_4950'] = func_4950
mod = relay.transform.InferType()(mod)
output = func_4950()
func_4951 = relay.Function([], output)
mutated_mod['func_4951'] = func_4951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_5026 = relay.TupleGetItem(func_1339_call(), 0)
call_5027 = relay.TupleGetItem(func_1341_call(), 0)
func_3514_call = mod.get_global_var('func_3514')
func_3516_call = mutated_mod.get_global_var('func_3516')
call_5028 = relay.TupleGetItem(func_3514_call(), 3)
call_5029 = relay.TupleGetItem(func_3516_call(), 3)
uop_5039 = relay.rsqrt(call_5026.astype('float32')) # shape=(2, 4, 1)
uop_5041 = relay.rsqrt(call_5027.astype('float32')) # shape=(2, 4, 1)
bop_5043 = relay.floor_divide(uop_5039.astype('float32'), relay.reshape(call_5028.astype('float32'), relay.shape_of(uop_5039))) # shape=(2, 4, 1)
bop_5046 = relay.floor_divide(uop_5041.astype('float32'), relay.reshape(call_5029.astype('float32'), relay.shape_of(uop_5041))) # shape=(2, 4, 1)
output = bop_5043
output2 = bop_5046
func_5049 = relay.Function([], output)
mod['func_5049'] = func_5049
mod = relay.transform.InferType()(mod)
output = func_5049()
func_5050 = relay.Function([], output)
mutated_mod['func_5050'] = func_5050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2918_call = mod.get_global_var('func_2918')
func_2920_call = mutated_mod.get_global_var('func_2920')
call_5088 = relay.TupleGetItem(func_2918_call(), 2)
call_5089 = relay.TupleGetItem(func_2920_call(), 2)
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_5114 = relay.TupleGetItem(func_1647_call(), 2)
call_5115 = relay.TupleGetItem(func_1649_call(), 2)
func_2201_call = mod.get_global_var('func_2201')
func_2206_call = mutated_mod.get_global_var('func_2206')
var_5124 = relay.var("var_5124", dtype = "int32", shape = (135,))#candidate|5124|(135,)|var|int32
const_5125 = relay.const([4.185234,-3.664099,-0.360591,0.812519,5.040290,6.897701,-5.399801,1.919992,5.981140,-4.153380,2.708383,-4.719544,-6.779629,-3.948614,-2.843856,-0.576092,1.515516,-4.967060,9.329079,0.824912,0.531651,5.138433,7.944721,2.236581,7.253335,-9.354191,-4.433846,-0.269246,-6.054685,-6.061767,2.317526,4.620579,3.450304,-3.310346,8.810956,6.360337,-6.147176,-3.443005,-8.329639,2.561133,0.418010,-7.859586,-3.745245,-2.804758,8.311715,7.155840,-0.642147,7.905152,-2.869582,-5.537374,8.901524,9.033283,-5.636715,-2.643016,0.534499,3.712595,6.149604,-5.025719,-6.177007,-5.172897,-9.673306,-5.113261,-6.355490,-5.707352,-9.059298,-2.677842,9.179165,3.613123,-0.074556,-1.654471,4.507475,-7.135839,9.821318,-9.569938,-3.742083,2.130273,-1.936576,8.220246,-8.312972,-1.349647,-7.958513,-2.092554,-1.408113,-2.066366,9.264647,-3.072426,-2.927567,2.304485,7.999632,0.301869,0.332640,-1.876894,3.612667,-9.934060,-2.684741,-1.876047,-6.506630,-0.230932,-2.296052,4.690740,0.898860,9.244187,-7.077900,8.184398,-4.080914,8.746230,3.054627,-4.798654,5.581358,-5.923354,7.132634,5.885369,-6.248784,-8.309817,-3.690898,-5.975341,7.052152,8.426543,3.258109,9.563814,9.360793,2.913054,6.692455,6.179661,-0.531626,-9.232558,-7.581967,5.741212,4.432949,-1.045258,2.402912,4.289954,-5.949601,0.760076,1.072685,8.958106,8.293395,6.284731,-8.482721,-1.248010,7.728531,-7.811594,-6.758264,-8.714842,0.436212,2.395339,3.184136,2.383357,2.465162,2.648639,-8.026447,8.723870,9.018782,-8.960009,-7.758981,2.569120,6.419824,8.584244,2.799920,6.273755,-6.897224,-7.514132,7.535164,0.440996,-7.614492,8.122121,-2.526531,-6.154018,7.360679,7.151697,5.509086,9.385268,4.591816,-7.560018,-5.014224,7.709026,-3.940550,5.842959,-4.886993,-8.011074,8.124541,7.744248,6.544987,-4.171209,-5.702606,-2.740762,-3.413883,-7.053045,-4.340506,-3.322522,-2.974119,-9.834862,0.228546,-5.774354,-4.498143,-4.898831,-9.693116,0.730135,-8.556726,-2.862953,-5.215284,-9.768783,5.009120,-1.607098,-9.959335,-5.691547,-0.851317,6.209810,-0.037025,9.235305,9.735620,5.854605,5.170656,5.379022,-9.095620,-1.193745,-5.248163,5.474191,8.856543,7.544405,-4.248312,-9.763768,-3.690926,1.617673,7.122128,-9.710413,-0.293173,-3.479766,-9.251400,1.644262,-9.616836,1.703974,1.486921,-3.481094,-1.977225,-6.111918,9.546826,-3.005748,-8.368754,1.062183,-1.031690,-7.351381,1.367950,4.288745,-2.494316,-7.680711,-4.370035,4.012847,-9.379935,9.551877,-6.195105,3.014653,-1.767229,1.745830,0.402358,0.281381,-7.949345,2.387586,-7.647831,-0.394395,3.500329,4.450762,-9.189525,4.382163,-1.814597,-3.414360,-4.236148,6.964157,8.492731,-2.067991,9.910342,-7.964071,6.544532], dtype = "float64")#candidate|5125|(273,)|const|float64
call_5123 = relay.TupleGetItem(func_2201_call(relay.reshape(call_5114.astype('float64'), [25, 4]), relay.reshape(var_5124.astype('int32'), [135,]), relay.reshape(const_5125.astype('float64'), [39, 7]), ), 4)
call_5126 = relay.TupleGetItem(func_2206_call(relay.reshape(call_5114.astype('float64'), [25, 4]), relay.reshape(var_5124.astype('int32'), [135,]), relay.reshape(const_5125.astype('float64'), [39, 7]), ), 4)
output = relay.Tuple([call_5088,call_5114,call_5123,var_5124,const_5125,])
output2 = relay.Tuple([call_5089,call_5115,call_5126,var_5124,const_5125,])
func_5134 = relay.Function([var_5124,], output)
mod['func_5134'] = func_5134
mod = relay.transform.InferType()(mod)
var_5135 = relay.var("var_5135", dtype = "int32", shape = (135,))#candidate|5135|(135,)|var|int32
output = func_5134(var_5135)
func_5136 = relay.Function([var_5135], output)
mutated_mod['func_5136'] = func_5136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_5173 = relay.TupleGetItem(func_1891_call(), 0)
call_5174 = relay.TupleGetItem(func_1892_call(), 0)
output = relay.Tuple([call_5173,])
output2 = relay.Tuple([call_5174,])
func_5186 = relay.Function([], output)
mod['func_5186'] = func_5186
mod = relay.transform.InferType()(mod)
mutated_mod['func_5186'] = func_5186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5186_call = mutated_mod.get_global_var('func_5186')
call_5187 = func_5186_call()
output = call_5187
func_5188 = relay.Function([], output)
mutated_mod['func_5188'] = func_5188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2526_call = mod.get_global_var('func_2526')
func_2527_call = mutated_mod.get_global_var('func_2527')
call_5219 = func_2526_call()
call_5220 = func_2526_call()
output = relay.Tuple([call_5219,])
output2 = relay.Tuple([call_5220,])
func_5223 = relay.Function([], output)
mod['func_5223'] = func_5223
mod = relay.transform.InferType()(mod)
mutated_mod['func_5223'] = func_5223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mutated_mod.get_global_var('func_5223')
call_5224 = func_5223_call()
output = call_5224
func_5225 = relay.Function([], output)
mutated_mod['func_5225'] = func_5225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2666_call = mod.get_global_var('func_2666')
func_2667_call = mutated_mod.get_global_var('func_2667')
call_5255 = relay.TupleGetItem(func_2666_call(), 4)
call_5256 = relay.TupleGetItem(func_2667_call(), 4)
output = relay.Tuple([call_5255,])
output2 = relay.Tuple([call_5256,])
func_5265 = relay.Function([], output)
mod['func_5265'] = func_5265
mod = relay.transform.InferType()(mod)
mutated_mod['func_5265'] = func_5265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5265_call = mutated_mod.get_global_var('func_5265')
call_5266 = func_5265_call()
output = call_5266
func_5267 = relay.Function([], output)
mutated_mod['func_5267'] = func_5267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_5278 = relay.TupleGetItem(func_3036_call(), 1)
call_5279 = relay.TupleGetItem(func_3038_call(), 1)
output = relay.Tuple([call_5278,])
output2 = relay.Tuple([call_5279,])
func_5282 = relay.Function([], output)
mod['func_5282'] = func_5282
mod = relay.transform.InferType()(mod)
mutated_mod['func_5282'] = func_5282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5282_call = mutated_mod.get_global_var('func_5282')
call_5283 = func_5282_call()
output = call_5283
func_5284 = relay.Function([], output)
mutated_mod['func_5284'] = func_5284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_5308 = relay.TupleGetItem(func_1647_call(), 0)
call_5309 = relay.TupleGetItem(func_1649_call(), 0)
func_4269_call = mod.get_global_var('func_4269')
func_4271_call = mutated_mod.get_global_var('func_4271')
call_5313 = relay.TupleGetItem(func_4269_call(), 0)
call_5314 = relay.TupleGetItem(func_4271_call(), 0)
output = relay.Tuple([call_5308,call_5313,])
output2 = relay.Tuple([call_5309,call_5314,])
func_5336 = relay.Function([], output)
mod['func_5336'] = func_5336
mod = relay.transform.InferType()(mod)
output = func_5336()
func_5337 = relay.Function([], output)
mutated_mod['func_5337'] = func_5337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3994_call = mod.get_global_var('func_3994')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_5394 = relay.TupleGetItem(func_3994_call(), 0)
call_5395 = relay.TupleGetItem(func_3996_call(), 0)
uop_5397 = relay.sinh(call_5394.astype('float32')) # shape=(2, 4, 1)
uop_5399 = relay.sinh(call_5395.astype('float32')) # shape=(2, 4, 1)
func_2976_call = mod.get_global_var('func_2976')
func_2977_call = mutated_mod.get_global_var('func_2977')
call_5404 = relay.TupleGetItem(func_2976_call(), 0)
call_5405 = relay.TupleGetItem(func_2977_call(), 0)
output = relay.Tuple([uop_5397,call_5404,])
output2 = relay.Tuple([uop_5399,call_5405,])
func_5412 = relay.Function([], output)
mod['func_5412'] = func_5412
mod = relay.transform.InferType()(mod)
mutated_mod['func_5412'] = func_5412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5412_call = mutated_mod.get_global_var('func_5412')
call_5413 = func_5412_call()
output = call_5413
func_5414 = relay.Function([], output)
mutated_mod['func_5414'] = func_5414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_5415 = relay.TupleGetItem(func_3036_call(), 0)
call_5416 = relay.TupleGetItem(func_3038_call(), 0)
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_5441 = relay.TupleGetItem(func_1647_call(), 0)
call_5442 = relay.TupleGetItem(func_1649_call(), 0)
func_2918_call = mod.get_global_var('func_2918')
func_2920_call = mutated_mod.get_global_var('func_2920')
call_5443 = relay.TupleGetItem(func_2918_call(), 2)
call_5444 = relay.TupleGetItem(func_2920_call(), 2)
func_3911_call = mod.get_global_var('func_3911')
func_3913_call = mutated_mod.get_global_var('func_3913')
const_5447 = relay.const([2.928555,-0.270716,7.569716,1.431801,-8.723678,-0.022536,9.173688,3.710171,-4.832535,-7.799671,2.062048,-8.531214,-6.465857,-2.654533,1.115105,-4.187170,4.592522,-5.241979,1.469864,-7.673319,2.783768,-2.950285,0.536212,6.671976,-4.480357,-7.636349,-8.717182,-0.173108,9.089162,-0.667546,6.636986,-6.524598,-0.599557,0.197444,-2.680485,3.259982,0.681457,-7.973991,4.937087,-0.907802,7.541988,4.697128,5.563255,-9.627857,-0.297837,0.191908,-4.743374,4.879992], dtype = "float32")#candidate|5447|(48,)|const|float32
call_5446 = func_3911_call(relay.reshape(const_5447.astype('float32'), [2, 4, 6]))
call_5448 = func_3911_call(relay.reshape(const_5447.astype('float32'), [2, 4, 6]))
func_4695_call = mod.get_global_var('func_4695')
func_4697_call = mutated_mod.get_global_var('func_4697')
call_5450 = relay.TupleGetItem(func_4695_call(), 0)
call_5451 = relay.TupleGetItem(func_4697_call(), 0)
bop_5456 = relay.multiply(call_5450.astype('float32'), call_5441.astype('float32')) # shape=(2, 4, 650)
bop_5459 = relay.multiply(call_5451.astype('float32'), call_5442.astype('float32')) # shape=(2, 4, 650)
bop_5467 = relay.mod(const_5447.astype('float32'), call_5441.astype('float32')) # shape=(2, 4, 48)
bop_5470 = relay.mod(const_5447.astype('float32'), call_5442.astype('float32')) # shape=(2, 4, 48)
output = relay.Tuple([call_5415,call_5443,call_5446,bop_5456,bop_5467,])
output2 = relay.Tuple([call_5416,call_5444,call_5448,bop_5459,bop_5470,])
func_5480 = relay.Function([], output)
mod['func_5480'] = func_5480
mod = relay.transform.InferType()(mod)
mutated_mod['func_5480'] = func_5480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5480_call = mutated_mod.get_global_var('func_5480')
call_5481 = func_5480_call()
output = call_5481
func_5482 = relay.Function([], output)
mutated_mod['func_5482'] = func_5482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3837_call = mod.get_global_var('func_3837')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_5528 = relay.TupleGetItem(func_3837_call(), 0)
call_5529 = relay.TupleGetItem(func_3838_call(), 0)
output = call_5528
output2 = call_5529
func_5530 = relay.Function([], output)
mod['func_5530'] = func_5530
mod = relay.transform.InferType()(mod)
output = func_5530()
func_5531 = relay.Function([], output)
mutated_mod['func_5531'] = func_5531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2031_call = mutated_mod.get_global_var('func_2031')
call_5656 = relay.TupleGetItem(func_2030_call(), 2)
call_5657 = relay.TupleGetItem(func_2031_call(), 2)
output = relay.Tuple([call_5656,])
output2 = relay.Tuple([call_5657,])
func_5669 = relay.Function([], output)
mod['func_5669'] = func_5669
mod = relay.transform.InferType()(mod)
output = func_5669()
func_5670 = relay.Function([], output)
mutated_mod['func_5670'] = func_5670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1776_call = mod.get_global_var('func_1776')
func_1778_call = mutated_mod.get_global_var('func_1778')
call_5673 = relay.TupleGetItem(func_1776_call(), 3)
call_5674 = relay.TupleGetItem(func_1778_call(), 3)
func_4775_call = mod.get_global_var('func_4775')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_5679 = relay.TupleGetItem(func_4775_call(), 3)
call_5680 = relay.TupleGetItem(func_4776_call(), 3)
output = relay.Tuple([call_5673,call_5679,])
output2 = relay.Tuple([call_5674,call_5680,])
func_5681 = relay.Function([], output)
mod['func_5681'] = func_5681
mod = relay.transform.InferType()(mod)
output = func_5681()
func_5682 = relay.Function([], output)
mutated_mod['func_5682'] = func_5682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2250_call = mod.get_global_var('func_2250')
func_2252_call = mutated_mod.get_global_var('func_2252')
call_5724 = func_2250_call()
call_5725 = func_2250_call()
func_809_call = mod.get_global_var('func_809')
func_812_call = mutated_mod.get_global_var('func_812')
var_5729 = relay.var("var_5729", dtype = "float32", shape = (648,))#candidate|5729|(648,)|var|float32
call_5728 = relay.TupleGetItem(func_809_call(relay.reshape(var_5729.astype('float32'), [9, 9, 8])), 2)
call_5730 = relay.TupleGetItem(func_812_call(relay.reshape(var_5729.astype('float32'), [9, 9, 8])), 2)
output = relay.Tuple([call_5724,call_5728,var_5729,])
output2 = relay.Tuple([call_5725,call_5730,var_5729,])
func_5734 = relay.Function([var_5729,], output)
mod['func_5734'] = func_5734
mod = relay.transform.InferType()(mod)
var_5735 = relay.var("var_5735", dtype = "float32", shape = (648,))#candidate|5735|(648,)|var|float32
output = func_5734(var_5735)
func_5736 = relay.Function([var_5735], output)
mutated_mod['func_5736'] = func_5736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_5743 = func_1316_call()
call_5744 = func_1316_call()
func_3911_call = mod.get_global_var('func_3911')
func_3913_call = mutated_mod.get_global_var('func_3913')
var_5748 = relay.var("var_5748", dtype = "float32", shape = (48,))#candidate|5748|(48,)|var|float32
call_5747 = func_3911_call(relay.reshape(var_5748.astype('float32'), [2, 4, 6]))
call_5749 = func_3911_call(relay.reshape(var_5748.astype('float32'), [2, 4, 6]))
output = relay.Tuple([call_5743,call_5747,var_5748,])
output2 = relay.Tuple([call_5744,call_5749,var_5748,])
func_5774 = relay.Function([var_5748,], output)
mod['func_5774'] = func_5774
mod = relay.transform.InferType()(mod)
mutated_mod['func_5774'] = func_5774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5775 = relay.var("var_5775", dtype = "float32", shape = (48,))#candidate|5775|(48,)|var|float32
func_5774_call = mutated_mod.get_global_var('func_5774')
call_5776 = func_5774_call(var_5775)
output = call_5776
func_5777 = relay.Function([var_5775], output)
mutated_mod['func_5777'] = func_5777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_5788 = relay.TupleGetItem(func_1647_call(), 1)
call_5789 = relay.TupleGetItem(func_1649_call(), 1)
func_4695_call = mod.get_global_var('func_4695')
func_4697_call = mutated_mod.get_global_var('func_4697')
call_5790 = relay.TupleGetItem(func_4695_call(), 3)
call_5791 = relay.TupleGetItem(func_4697_call(), 3)
output = relay.Tuple([call_5788,call_5790,])
output2 = relay.Tuple([call_5789,call_5791,])
func_5802 = relay.Function([], output)
mod['func_5802'] = func_5802
mod = relay.transform.InferType()(mod)
mutated_mod['func_5802'] = func_5802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5802_call = mutated_mod.get_global_var('func_5802')
call_5803 = func_5802_call()
output = call_5803
func_5804 = relay.Function([], output)
mutated_mod['func_5804'] = func_5804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5669_call = mod.get_global_var('func_5669')
func_5670_call = mutated_mod.get_global_var('func_5670')
call_5879 = relay.TupleGetItem(func_5669_call(), 0)
call_5880 = relay.TupleGetItem(func_5670_call(), 0)
output = relay.Tuple([call_5879,])
output2 = relay.Tuple([call_5880,])
func_5948 = relay.Function([], output)
mod['func_5948'] = func_5948
mod = relay.transform.InferType()(mod)
mutated_mod['func_5948'] = func_5948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5948_call = mutated_mod.get_global_var('func_5948')
call_5949 = func_5948_call()
output = call_5949
func_5950 = relay.Function([], output)
mutated_mod['func_5950'] = func_5950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4339_call = mod.get_global_var('func_4339')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_5954 = relay.TupleGetItem(func_4339_call(), 2)
call_5955 = relay.TupleGetItem(func_4340_call(), 2)
const_5964 = relay.const([[[-5.237888,-5.500394,8.055867,9.418259],[3.641585,3.102241,6.374907,9.638096],[9.404577,-0.160986,-0.488026,-4.897081],[8.659542,-9.889860,5.392808,-8.462926]],[[5.747932,6.579799,-1.933782,4.550518],[1.123226,2.820006,-2.343067,-8.887983],[8.325160,2.956476,7.851276,-1.963207],[4.071447,-7.599347,2.296332,-3.370550]]], dtype = "float64")#candidate|5964|(2, 4, 4)|const|float64
bop_5965 = relay.bitwise_and(call_5954.astype('int64'), const_5964.astype('int64')) # shape=(2, 4, 4)
bop_5968 = relay.bitwise_and(call_5955.astype('int64'), const_5964.astype('int64')) # shape=(2, 4, 4)
func_3057_call = mod.get_global_var('func_3057')
func_3059_call = mutated_mod.get_global_var('func_3059')
call_5983 = relay.TupleGetItem(func_3057_call(), 0)
call_5984 = relay.TupleGetItem(func_3059_call(), 0)
output = relay.Tuple([bop_5965,call_5983,])
output2 = relay.Tuple([bop_5968,call_5984,])
func_6034 = relay.Function([], output)
mod['func_6034'] = func_6034
mod = relay.transform.InferType()(mod)
output = func_6034()
func_6035 = relay.Function([], output)
mutated_mod['func_6035'] = func_6035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4339_call = mod.get_global_var('func_4339')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_6041 = relay.TupleGetItem(func_4339_call(), 0)
call_6042 = relay.TupleGetItem(func_4340_call(), 0)
func_4339_call = mod.get_global_var('func_4339')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_6057 = relay.TupleGetItem(func_4339_call(), 1)
call_6058 = relay.TupleGetItem(func_4340_call(), 1)
bop_6060 = relay.bitwise_and(call_6057.astype('int64'), relay.reshape(call_6041.astype('int64'), relay.shape_of(call_6057))) # shape=(2, 4, 1)
bop_6063 = relay.bitwise_and(call_6058.astype('int64'), relay.reshape(call_6042.astype('int64'), relay.shape_of(call_6058))) # shape=(2, 4, 1)
func_3249_call = mod.get_global_var('func_3249')
func_3252_call = mutated_mod.get_global_var('func_3252')
var_6071 = relay.var("var_6071", dtype = "uint64", shape = (560,))#candidate|6071|(560,)|var|uint64
call_6070 = relay.TupleGetItem(func_3249_call(relay.reshape(var_6071.astype('uint64'), [560,])), 2)
call_6072 = relay.TupleGetItem(func_3252_call(relay.reshape(var_6071.astype('uint64'), [560,])), 2)
output = relay.Tuple([bop_6060,call_6070,var_6071,])
output2 = relay.Tuple([bop_6063,call_6072,var_6071,])
func_6078 = relay.Function([var_6071,], output)
mod['func_6078'] = func_6078
mod = relay.transform.InferType()(mod)
var_6079 = relay.var("var_6079", dtype = "uint64", shape = (560,))#candidate|6079|(560,)|var|uint64
output = func_6078(var_6079)
func_6080 = relay.Function([var_6079], output)
mutated_mod['func_6080'] = func_6080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2666_call = mod.get_global_var('func_2666')
func_2667_call = mutated_mod.get_global_var('func_2667')
call_6093 = relay.TupleGetItem(func_2666_call(), 5)
call_6094 = relay.TupleGetItem(func_2667_call(), 5)
func_2807_call = mod.get_global_var('func_2807')
func_2809_call = mutated_mod.get_global_var('func_2809')
call_6105 = func_2807_call()
call_6106 = func_2807_call()
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_6113 = relay.TupleGetItem(func_1647_call(), 1)
call_6114 = relay.TupleGetItem(func_1649_call(), 1)
output = relay.Tuple([call_6093,call_6105,call_6113,])
output2 = relay.Tuple([call_6094,call_6106,call_6114,])
func_6128 = relay.Function([], output)
mod['func_6128'] = func_6128
mod = relay.transform.InferType()(mod)
mutated_mod['func_6128'] = func_6128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6128_call = mutated_mod.get_global_var('func_6128')
call_6129 = func_6128_call()
output = call_6129
func_6130 = relay.Function([], output)
mutated_mod['func_6130'] = func_6130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3762_call = mod.get_global_var('func_3762')
func_3763_call = mutated_mod.get_global_var('func_3763')
call_6147 = func_3762_call()
call_6148 = func_3762_call()
func_2807_call = mod.get_global_var('func_2807')
func_2809_call = mutated_mod.get_global_var('func_2809')
call_6157 = func_2807_call()
call_6158 = func_2807_call()
func_4208_call = mod.get_global_var('func_4208')
func_4212_call = mutated_mod.get_global_var('func_4212')
const_6164 = relay.const(-2, dtype = "uint64")#candidate|6164|()|const|uint64
var_6165 = relay.var("var_6165", dtype = "uint64", shape = (1296,))#candidate|6165|(1296,)|var|uint64
const_6166 = relay.const([4.297379,-0.739188,3.012880,-7.987676,-6.281756,-7.726021,7.242141,-7.658814,6.706051,3.904268,5.882228,-2.168408,5.292243,-5.777747,0.736781,-8.793225,-6.374107,4.464313,-3.067620,7.262973,4.180774,6.922578,-1.389493,-1.503010,8.674739,-1.393560,4.403110,-5.791408,-1.524008,3.838290,-3.042088,-9.041074,-1.077622,-1.206611,-3.203317,1.985056,-6.170738,-9.889077,-9.020950,-8.433871,-6.867184,-6.191288,-7.986565,-5.885104,2.354280,-5.264039,0.305478,-0.642649,5.592614,-6.924265,3.633351,9.242504,-5.657604,-1.600668,-7.690129,2.940033,3.378811,-3.515780,-6.039646,8.886950,-9.838498,3.286320,-1.296261,6.185264,0.734549,9.116851,5.806951,-9.340880,-0.555980,-6.721276,4.563543,3.989708,6.419246,-8.882744,-3.631027,6.769333,-3.445397,6.191224,-6.064702,-2.918595,-5.390407,-5.915779,-6.452459,-8.087584,-5.972445,1.146370,-9.086848,-4.359655,-4.294452,6.273767,-7.345229,7.154249,-5.243812,-6.286928,1.228151,-6.112350,-3.862529,5.650334,3.563218,-0.751991,-7.621886,1.968855,-1.354846,-8.730486,1.161752,-0.528077,-4.764440,-0.861084,-2.094578,2.369091,5.025299,1.349300,5.282603,-8.852752,-4.430840,-6.176776,-5.745900,8.338993,4.220892,1.988315,-3.393836,9.654267,5.710019,0.929100,-2.572685,5.353285,-7.355544,5.694278,5.537251,-9.211843,-4.108165,-1.191453,-6.777283,-9.203627,1.772965,-4.968893,7.159862,-8.170234,7.491616,-1.594366,-8.617716,6.154939,-8.137635,-2.976052,-4.770701,-5.631222,5.474102,5.365658,-6.963392,-0.041603,0.147970,3.734339,-8.377733,4.238913,1.405358,2.348513,3.038154,-0.189036,7.640601,3.785230,2.906310,3.203379,-1.170145,7.616094,-6.883235,-7.768059,-4.733622,-4.977238,8.653094,7.757291,5.615554,8.726910,3.570592,-6.406123,-9.765398,5.228926,1.175425,6.346370,0.451263,9.622561,-7.097293,-5.297099,5.850672,3.756929,-2.164921,-1.578233,6.991273,9.484296,0.854610,6.844650,9.822528,-2.401693,5.453984,5.759546,-3.912792,-4.606389,-3.577290,3.445791,1.052766,5.171813,5.182480,1.444864,0.798800,-1.932342,0.046869,-3.985551,-6.373108,0.231617,-5.191877,-4.621099,0.729375,8.246965,7.234592,-6.043436,7.542528,3.356305,3.695103,7.090041,3.650242,0.531071,-8.601977,6.274557,-3.393100,-5.076005,1.510924,3.520815,-2.986295,9.148337,-8.673461,-1.378319,1.596430,-9.804963,2.757306,0.592180,0.345386,1.288101,-6.042194,-1.215763,4.459215,-4.321307,-7.176065,-3.675661,-1.101577,-7.587695,9.542102,4.564814,-9.049265,4.614113,7.790126,-4.509644,6.405212,-7.458453,1.575105,7.400147,-4.477385,3.749037,6.510706,7.340480,1.377557,-5.406898,-9.513516,4.501740,-3.311548,-2.834205,2.659497,-1.886419,-9.111942,5.183485,-2.007585,6.195117,-6.268883,9.847711,-8.292137,8.123482,-5.544150,-0.478547,7.781342,-9.106129,-1.640346,-3.739131,9.602892,-6.689304,4.860969,7.550043,-1.498632,-9.133452,-3.161527,2.580084,-2.919078,-0.468876,-1.113569,-0.480497,1.678442,2.153299,3.688670,3.219093,2.682862,3.772127,1.656521,-9.715255,0.684869,-2.473561,-8.902947,-0.987819,5.903003,4.970486,7.504415,0.187062,-5.054404,-3.204988,-6.007847,2.684885,3.177683,5.634261,7.038809,3.534821,-9.909262,-6.755405,1.165421,-1.696688,-2.416318,-8.340997,5.747501,-7.512893,5.584085,2.787365,-0.692440,7.381559,9.650263,2.228531,-5.346281,0.085968,-2.368452,3.406759,-5.248480,-4.489308,1.962039,-7.317441,8.312452,4.588361,8.097513,-3.655004,8.949638,-4.755955,-9.294285,1.163160,-2.479510,-9.999073,3.136228,-5.376538,3.874581,-9.093722,5.318045,4.428875,1.705722,7.086459,3.159568,-5.407538,5.778186,-5.768938,-3.847123,-6.618626,-9.182453,-9.087789,-9.794985,-3.660503,2.714585,1.170460,5.801070,9.452195,3.488218,-6.899057,7.055084,5.676682,5.065146,-7.678677,4.115386,-9.931867,7.717854,8.690369,7.412982,3.276254,-4.876102,8.212628,0.268506,-0.099021,-2.402853,-3.158753,-8.729551,-9.192563,1.664510,7.222631,-4.851325,-6.864801,-8.095458,0.105994,0.336571,5.150252,2.506963,-6.769376,3.616685,5.318739,0.700693,3.301067,5.504541,7.753898,1.669488,-2.540724,-0.101115,2.998352,-1.752325,-4.748433,-4.479456,-2.334199,-0.071596,-3.964569,3.831287,7.737842,1.076869,-6.541295,6.496521,1.478909,8.788637,-5.731791,3.737381,-1.796922,-5.916744,6.851846,-1.445284,8.222145,-2.659073,5.578284,6.215338,-6.044830,5.616991,-6.747253,-1.606718,2.445051,4.169026,6.464926,-7.640382,-1.922304,-1.233597,5.559218,4.290076,-9.603571,-4.766142,-9.995351,-0.280976,0.407747,1.731547,-3.139975,9.631911,9.959692,6.126209,7.707273,4.088424,7.538060,-4.962605,-5.754440,2.691318,0.758111,-0.939081,2.751960,6.680414,4.015790,-7.429415,-8.238540,7.203859,-2.592853,2.131118,-8.414173,-6.808363,-8.666931,-8.791374,-5.899098,5.408481,-4.033885,8.204869,2.878841,-2.218115,-4.742394,-5.511219,-5.060285,-6.736292,2.175929,6.973367,-7.742403,8.670438,-8.151933,-1.753507,4.146039,-8.052185,5.777930,7.400431,-0.781572,9.532568,8.803073,-5.647636,-6.770731,-8.511384,-7.614130,4.095311,9.925238,6.933583,0.634868,5.799620,-9.445440,-8.100112,7.495755,-6.658067,5.592881,-2.289819,9.614618,-8.801192,-9.109134,0.467593,-6.074844,1.356143,2.271374,3.053599,-4.892110,2.864444,6.658728,5.606497,-8.845781,-6.847528,4.762349,-1.764848,7.396040,-6.956240,2.537276,-3.536275,6.092507,-1.161718,3.666079,1.368810,-3.799422,-5.080923,-9.762751,-7.947664,6.539626,-1.913953,-5.797879,5.385692,4.807513,9.622893,-5.987688,9.942086,6.727958,-9.475005,4.800389,2.070999,8.250245,5.844326,1.205328,-7.392663,8.676277,6.789994,7.624487,8.944247,1.845108,2.817153,5.628947,0.650969,-6.206084,4.681580,4.742482,9.612382,-8.038604,-1.419685,5.270173,-4.129969,3.379999,-2.861445,-1.016367,8.514574,-9.894605,2.446760,3.722913,-4.458275,5.869878,-5.594632,-9.388811,0.844914,-2.697312,-1.395804,-6.120301,-4.481249,7.782240,-9.340209,1.271866,2.979506,-2.613470,6.585684,3.261046,-6.278818,0.356225,5.148761,-0.067448,-5.120916,-0.622479,-1.733962,3.342030,-4.998752,3.481582,-5.188275,-3.168447,-0.229388,0.457015,6.883369,-9.350670,4.859629,-2.834647,8.634201,4.370021,6.286696,2.036137,-5.080656,8.082749,9.114412,8.725418,1.498293,8.946472,-9.388557,0.489771,1.267470,1.246309,1.991613,4.261620,9.625439,-1.578320,-3.434888,-3.218358,-4.256881,5.913889,0.442058,9.554452,-2.185259,-9.476207,9.345795,-0.958633,2.460629,9.624002,6.447754,-5.163119,9.844357,-2.107733], dtype = "float32")#candidate|6166|(648,)|const|float32
call_6163 = relay.TupleGetItem(func_4208_call(relay.reshape(const_6164.astype('uint64'), []), relay.reshape(var_6165.astype('uint64'), [9, 16, 9]), relay.reshape(const_6166.astype('float32'), [648,]), ), 1)
call_6167 = relay.TupleGetItem(func_4212_call(relay.reshape(const_6164.astype('uint64'), []), relay.reshape(var_6165.astype('uint64'), [9, 16, 9]), relay.reshape(const_6166.astype('float32'), [648,]), ), 1)
func_2315_call = mod.get_global_var('func_2315')
func_2318_call = mutated_mod.get_global_var('func_2318')
const_6184 = relay.const([1.604232,-1.256291,0.407362,5.274805,-8.343361,-4.411703,3.433264,-8.891257,-5.022761,-4.534644,-3.009644,3.982357,-7.708908,-8.880381,9.821882,-9.683156,-5.498593,7.192959,-9.149601,-5.808080,-2.721976,2.575991,-5.448322,9.602996,5.234550,-8.125551,-6.732271,-1.791182,-6.482419,7.933457,7.429300,-5.263023,-9.160279,0.020543,7.976544,-3.593770,-9.279163,5.784720,6.808160,8.357589,-7.284204,-7.580630,8.807295,5.649893,9.190886,-7.282959,-6.134131,-4.661027,-0.836254,-2.479811,-5.830198,-0.294949,-6.041329,0.486651,-8.788956,3.002288,0.617042,-3.831637,-9.688067,-7.163420,-9.312484,-8.161846,3.041188,0.407880,-8.649828,7.864103,-1.069652,2.637571,5.132512,6.584140,-4.475687,-0.503146,-1.976467,-9.992074,4.969062,3.855511,9.286271,-4.954359,-1.793393,1.614471,2.065855,3.251055,-4.963326,0.872339,-9.333956,2.613427,0.500341,-3.300677,-2.007265,-6.294012,0.632976,3.524324,-6.395849,7.841389,-0.953125,9.157908,-8.407446,0.743569,-9.639233,-5.981960,1.315217,6.848240,-7.377081,8.811444,-7.299901,-6.000695,8.075793,3.011838,5.286018,-8.515610,4.721460,-5.785693,5.544041,-7.230947,-7.560332,-8.778491,-2.550909,-4.729504,9.655052,-2.621653,0.153258,5.129683,-9.321770,-7.038053,3.885594,0.389050,9.927958,-4.690682,-7.906602,-9.430457,-0.131461,-0.461493,-9.532613,8.256881,-2.642724,1.723662,-1.119315,-3.594670,6.341281,-2.677494,-7.489630,4.453779,4.179112,-5.159855,-4.803863,-8.390215,9.044842,-5.857036,0.491672,9.990604,2.722108,-3.059921,9.568902,-4.991455,2.547882,4.615912,2.889108,5.348252,7.492176,-3.025013,-3.795754,-1.170629,8.375004,5.473052,-9.507034,9.891175,-8.419800,0.116773,-3.506958,-4.213518,-9.665264,1.953677,9.257362,9.882935,-8.930311,-8.426336,-3.677566,-7.114246,8.575033,7.386359,-4.790544,8.351510,-2.511709,-6.447773,2.268474,-4.237143,2.205901,4.386354,5.143325,1.016018,-4.194175,-8.774317,-3.470317,-1.387372,6.447488,6.028624,-2.615302,-9.653455,9.845153,-0.800649,7.724547,-6.919542,-7.132306,4.544150,-1.026422,-2.031045,5.981353,-5.996823,1.425196,9.897734,-6.426121,3.379431,-4.430154,0.955280,-6.620301,-2.531034,-8.167845,-3.862710,-4.340076,-6.146330,-4.382912,1.658126,-0.646356,2.246741,-5.066311,-4.421411,2.767807,-6.575044,2.962805,5.319810,3.396752,5.141681,8.647675,-7.055379,-2.671982,-9.247096,9.309533,-1.517120,6.561016,-5.903796,-0.252456,-4.433707,-1.511473,4.875262,-6.394254,7.399837,-4.498958,-3.315311,4.864528,4.537112,5.151456,-4.271306,6.382932,-9.857400,1.979403,2.932665,8.851258,7.024921,-1.800673,0.168964,-7.869448,-9.478906,-3.075358,-7.542421,8.422134,4.661475,4.939755,-8.297950,-3.591649,-5.223042,6.352522,3.336131,8.046366,-8.271710,-2.987207,4.938947,-1.712865,4.327374,-7.878932,-4.753527,-1.820011,-8.774890,-4.320500,-1.403431,-9.939299,-7.410079,-9.585050,-6.315964,-5.574034,9.340575,8.969966,0.935424,-3.831836,-0.548877,-2.805724,5.279856,-5.795480,6.918104,-1.999660,5.670877,-3.990901,-2.141298,0.914969,-3.481725,9.195595,-3.550673,-5.263561,-9.729043,2.825519,7.157894,-7.735630,-0.503130,8.126086,2.179928,6.185382,-9.063390,-1.174382,3.566847,7.904468,9.676211,9.537370,8.099723,-2.448371,5.772389,-6.188445,8.877639,2.718822,6.776383,0.576259,-9.253730,4.056446,-9.917033,9.665253,-1.329957,-1.229567,3.735649,6.406324,7.866739,-6.627972,6.404541,-8.169704,8.286983,-0.123832,-4.720175,6.680015,5.917595,7.760600,-9.102625,6.594458,7.853619,3.573952,3.073480,-5.150464,-4.818008,9.904643,1.528069,-0.771246,6.885580,-0.309211,7.762814,-2.307048,-1.024194,-5.615151,-2.616331,4.908652,9.670464,-5.127608,-8.226811,-7.925249,-8.521173,-8.012935,9.165800,-9.134216,-5.668768,-8.761375,5.789981,-0.193464,-8.786036,-5.286350,-9.880446,-7.251025,-2.855176,-2.390960,0.740291,9.672393,3.879415,-2.418821,0.630482,9.914523,7.164598,4.545258,3.375070,-7.750107,-7.911426,-6.132961,8.529679,9.940557,-5.634458,-7.089869,-8.915890,6.868025,3.788690,-4.674824,-0.498109,-3.294981,4.276116,-3.479930,9.309858,-4.475186,-7.566242,-8.677778,9.349524,8.620700,-0.189689,-3.638309,-2.261330,-3.244086,4.771229,-5.896734,-5.684691,0.839633,-4.668995,-7.739930,-5.405271,9.122869,-1.099070,-6.775656,5.292667,3.910539,6.778044,-9.222378,2.875431,-2.542864,1.737071,-2.098680,7.249613,4.027097,-0.158050,-6.937801,-9.876867,4.831475,5.342059,2.879988,4.782451,-1.417420,-7.930122,-0.311374,8.719303,-7.832697,2.579672,6.040977,-0.945205,-5.484222,-3.162674,1.450324,2.533112,7.409718,4.807411,8.337623,2.033277,6.451166,4.532455,6.365888,-1.880607,3.978962,8.206762,7.805048,-6.423736,-0.055711,-8.155908,3.737699,-2.960849,-9.738917,0.144931,-6.687172,-6.866456,-8.508040,-4.138204,-4.286847,2.852798,-6.891888,-7.733887,-0.523661,-7.390564,-2.774940,6.134823,-0.790273,-4.600568,8.362955,-2.922978,1.360660,8.185880,-0.713148,4.474996,2.784963,9.374527,6.341238,0.351960,-5.231436,-0.173642,-4.333730,-1.676150,8.993298,9.298890,2.471334,4.024298,-2.610132,-7.929357,-9.865123,-0.317398,8.930968,8.022935,1.860831,-6.680971,-1.285405,-4.746058,-1.933524,4.520375,-1.294433,-8.119679,9.169108,-1.945621,9.376313,-3.984748,-1.796604,4.300772,-2.719547,2.734415,8.909823,7.205014,-9.089470,-4.726567,6.683354,0.799210,-2.827614,1.386881,4.370425,-9.160246,-8.534339,-8.158332,1.204426,-3.514230,-2.956239,0.591721,-7.469001,-6.134753,4.008615,2.445886,-6.952681,-6.604399,1.155337,-9.701801,4.059527,6.120413,-4.338429,-4.013666,3.554452,6.318478,-6.986234,9.847898,-3.943764,-7.706222,-5.337980,-4.043283,-9.539743,4.847776,-3.526894,-5.854414,-5.628375,9.624913,5.677162,-3.440671,7.252761,-2.708811,3.352403,-8.557029,5.291763,1.325755,-6.398555,4.380579,-4.228029,-6.087777,-0.809300,-0.388024,-6.324247,1.404806,8.113442,-3.278750,-3.845738,5.685923,-4.999170,2.398293,-7.362781,0.273692,-4.886303,4.287784,-8.337757,2.983698,-9.142785,5.295397,8.292598,-1.617353,2.413824,2.714418,3.245770,9.893982,-3.674010,-4.111950,5.793550,-2.634206,-5.432518,-2.774300,3.286491,6.758452,3.706351,3.070832,-7.531205,9.931877,-7.694136,9.714854,9.495931,-5.237156,0.413611,-5.483003,-8.437043,-8.122167,-3.308887,9.728607,-3.391881,7.777055,-6.950315,-4.057855,-3.846594,-1.263461,2.379401,1.594685,-7.022685,-1.207294,-1.713910,-5.634703,5.225028,3.025549,7.660611,-3.652274,2.622399,7.239052,-6.788432,-5.107841,6.028183,6.564916], dtype = "float64")#candidate|6184|(650,)|const|float64
call_6183 = relay.TupleGetItem(func_2315_call(relay.reshape(const_6184.astype('float64'), [13, 10, 5])), 0)
call_6185 = relay.TupleGetItem(func_2318_call(relay.reshape(const_6184.astype('float64'), [13, 10, 5])), 0)
func_5802_call = mod.get_global_var('func_5802')
func_5804_call = mutated_mod.get_global_var('func_5804')
call_6188 = relay.TupleGetItem(func_5802_call(), 1)
call_6189 = relay.TupleGetItem(func_5804_call(), 1)
output = relay.Tuple([call_6147,call_6157,call_6163,const_6164,var_6165,const_6166,call_6183,const_6184,call_6188,])
output2 = relay.Tuple([call_6148,call_6158,call_6167,const_6164,var_6165,const_6166,call_6185,const_6184,call_6189,])
func_6190 = relay.Function([var_6165,], output)
mod['func_6190'] = func_6190
mod = relay.transform.InferType()(mod)
mutated_mod['func_6190'] = func_6190
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6191 = relay.var("var_6191", dtype = "uint64", shape = (1296,))#candidate|6191|(1296,)|var|uint64
func_6190_call = mutated_mod.get_global_var('func_6190')
call_6192 = func_6190_call(var_6191)
output = call_6192
func_6193 = relay.Function([var_6191], output)
mutated_mod['func_6193'] = func_6193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3343_call = mod.get_global_var('func_3343')
func_3344_call = mutated_mod.get_global_var('func_3344')
call_6220 = func_3343_call()
call_6221 = func_3343_call()
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_6225 = func_1316_call()
call_6226 = func_1316_call()
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_6237 = func_2494_call()
call_6238 = func_2494_call()
func_5802_call = mod.get_global_var('func_5802')
func_5804_call = mutated_mod.get_global_var('func_5804')
call_6264 = relay.TupleGetItem(func_5802_call(), 1)
call_6265 = relay.TupleGetItem(func_5804_call(), 1)
output = relay.Tuple([call_6220,call_6225,call_6237,call_6264,])
output2 = relay.Tuple([call_6221,call_6226,call_6238,call_6265,])
func_6267 = relay.Function([], output)
mod['func_6267'] = func_6267
mod = relay.transform.InferType()(mod)
mutated_mod['func_6267'] = func_6267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6267_call = mutated_mod.get_global_var('func_6267')
call_6268 = func_6267_call()
output = call_6268
func_6269 = relay.Function([], output)
mutated_mod['func_6269'] = func_6269
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6297 = relay.const([[[-3.944991],[9.814262],[-0.058845],[6.062809],[-2.185175],[-3.260714],[3.294907],[1.002821],[4.294714],[-2.495794],[9.551275],[4.310141],[-4.951425],[3.039425],[7.188107]]], dtype = "float32")#candidate|6297|(1, 15, 1)|const|float32
uop_6298 = relay.sin(const_6297.astype('float32')) # shape=(1, 15, 1)
func_4775_call = mod.get_global_var('func_4775')
func_4776_call = mutated_mod.get_global_var('func_4776')
call_6300 = relay.TupleGetItem(func_4775_call(), 3)
call_6301 = relay.TupleGetItem(func_4776_call(), 3)
output = relay.Tuple([uop_6298,call_6300,])
output2 = relay.Tuple([uop_6298,call_6301,])
func_6350 = relay.Function([], output)
mod['func_6350'] = func_6350
mod = relay.transform.InferType()(mod)
mutated_mod['func_6350'] = func_6350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6350_call = mutated_mod.get_global_var('func_6350')
call_6351 = func_6350_call()
output = call_6351
func_6352 = relay.Function([], output)
mutated_mod['func_6352'] = func_6352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4695_call = mod.get_global_var('func_4695')
func_4697_call = mutated_mod.get_global_var('func_4697')
call_6400 = relay.TupleGetItem(func_4695_call(), 1)
call_6401 = relay.TupleGetItem(func_4697_call(), 1)
output = relay.Tuple([call_6400,])
output2 = relay.Tuple([call_6401,])
func_6415 = relay.Function([], output)
mod['func_6415'] = func_6415
mod = relay.transform.InferType()(mod)
mutated_mod['func_6415'] = func_6415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6415_call = mutated_mod.get_global_var('func_6415')
call_6416 = func_6415_call()
output = call_6416
func_6417 = relay.Function([], output)
mutated_mod['func_6417'] = func_6417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4040_call = mod.get_global_var('func_4040')
func_4041_call = mutated_mod.get_global_var('func_4041')
call_6421 = relay.TupleGetItem(func_4040_call(), 0)
call_6422 = relay.TupleGetItem(func_4041_call(), 0)
func_524_call = mod.get_global_var('func_524')
func_527_call = mutated_mod.get_global_var('func_527')
const_6426 = relay.const([-7.568255,6.534309,-3.375344,-3.514138,-4.076223,-1.011162,8.453893,-9.845492,-8.255798,2.732759,-1.910944,3.214877,4.869686,-7.318437,2.742662,0.115607,7.350279,5.273062,9.016653,-2.663000,-6.421303,4.646708,6.999673,-1.937951,1.648030,-6.480791,3.076979,-0.032505,9.349187,-3.486390,9.712563,1.260321,-5.486339,-9.841812,-5.865894,3.290549,0.589526,-3.103868,4.451194,-9.677025,-2.222818,-3.495794,1.034800,-7.880305,2.613122,2.991903,1.478731,-0.427294,5.796192,5.472855,5.274172,4.599488,-1.128264,8.224345,-1.929355,-6.210492,1.853660,2.978408,7.462912,4.189073,-2.428002,7.769652,5.544229,6.008441,-0.197741,-9.285065,-5.615171,-3.956547,-1.386319,-3.451218,-6.772332,7.698941,2.889007,-5.216291,4.450142,3.083947,-1.025417,8.184780,-3.891791,-8.672034,2.713191,-8.670785,-9.885122,-5.165455,4.919135,-8.749075,3.256103,3.125113,-4.208163,7.588677,2.024190,4.345039,2.950543,-9.779191,0.417333,-5.592456,1.474767,-6.284815,-1.402900,-8.317563], dtype = "float32")#candidate|6426|(100,)|const|float32
call_6425 = relay.TupleGetItem(func_524_call(relay.reshape(const_6426.astype('float32'), [4, 5, 5]), relay.reshape(const_6426.astype('float32'), [4, 5, 5]), ), 0)
call_6427 = relay.TupleGetItem(func_527_call(relay.reshape(const_6426.astype('float32'), [4, 5, 5]), relay.reshape(const_6426.astype('float32'), [4, 5, 5]), ), 0)
bop_6435 = relay.add(call_6425.astype('uint64'), relay.reshape(const_6426.astype('uint64'), relay.shape_of(call_6425))) # shape=(4, 5, 5)
bop_6438 = relay.add(call_6427.astype('uint64'), relay.reshape(const_6426.astype('uint64'), relay.shape_of(call_6427))) # shape=(4, 5, 5)
func_5802_call = mod.get_global_var('func_5802')
func_5804_call = mutated_mod.get_global_var('func_5804')
call_6442 = relay.TupleGetItem(func_5802_call(), 0)
call_6443 = relay.TupleGetItem(func_5804_call(), 0)
output = relay.Tuple([call_6421,bop_6435,call_6442,])
output2 = relay.Tuple([call_6422,bop_6438,call_6443,])
func_6460 = relay.Function([], output)
mod['func_6460'] = func_6460
mod = relay.transform.InferType()(mod)
mutated_mod['func_6460'] = func_6460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6460_call = mutated_mod.get_global_var('func_6460')
call_6461 = func_6460_call()
output = call_6461
func_6462 = relay.Function([], output)
mutated_mod['func_6462'] = func_6462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3282_call = mod.get_global_var('func_3282')
func_3284_call = mutated_mod.get_global_var('func_3284')
call_6471 = func_3282_call()
call_6472 = func_3282_call()
func_2477_call = mod.get_global_var('func_2477')
func_2479_call = mutated_mod.get_global_var('func_2479')
var_6477 = relay.var("var_6477", dtype = "uint64", shape = (455,))#candidate|6477|(455,)|var|uint64
call_6476 = relay.TupleGetItem(func_2477_call(relay.reshape(var_6477.astype('uint64'), [455,])), 0)
call_6478 = relay.TupleGetItem(func_2479_call(relay.reshape(var_6477.astype('uint64'), [455,])), 0)
output = relay.Tuple([call_6471,call_6476,var_6477,])
output2 = relay.Tuple([call_6472,call_6478,var_6477,])
func_6480 = relay.Function([var_6477,], output)
mod['func_6480'] = func_6480
mod = relay.transform.InferType()(mod)
var_6481 = relay.var("var_6481", dtype = "uint64", shape = (455,))#candidate|6481|(455,)|var|uint64
output = func_6480(var_6481)
func_6482 = relay.Function([var_6481], output)
mutated_mod['func_6482'] = func_6482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2031_call = mutated_mod.get_global_var('func_2031')
call_6494 = relay.TupleGetItem(func_2030_call(), 0)
call_6495 = relay.TupleGetItem(func_2031_call(), 0)
func_3911_call = mod.get_global_var('func_3911')
func_3913_call = mutated_mod.get_global_var('func_3913')
const_6497 = relay.const([9.346434,-6.814176,1.360401,1.111260,6.754399,1.893857,-3.054910,7.577867,6.815805,-6.251085,2.180047,-4.451983,-8.132344,6.400400,0.515701,9.590625,-3.687502,3.581200,-4.940050,-8.733133,6.740458,-6.565130,-0.476147,-3.785990,6.295664,7.158750,-7.350282,7.206868,-3.382908,-0.071422,7.610230,2.379179,-8.113547,-9.863414,3.657128,-9.716687,-2.741622,-3.151877,6.045138,-5.633997,-7.599107,4.832154,-4.420927,8.929693,5.280963,-9.247046,1.807124,-1.118243], dtype = "float32")#candidate|6497|(48,)|const|float32
call_6496 = func_3911_call(relay.reshape(const_6497.astype('float32'), [2, 4, 6]))
call_6498 = func_3911_call(relay.reshape(const_6497.astype('float32'), [2, 4, 6]))
output = relay.Tuple([call_6494,call_6496,const_6497,])
output2 = relay.Tuple([call_6495,call_6498,const_6497,])
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
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_6540 = func_1316_call()
call_6541 = func_1316_call()
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
call_6565 = func_2494_call()
call_6566 = func_2494_call()
output = relay.Tuple([call_6540,call_6565,])
output2 = relay.Tuple([call_6541,call_6566,])
func_6577 = relay.Function([], output)
mod['func_6577'] = func_6577
mod = relay.transform.InferType()(mod)
output = func_6577()
func_6578 = relay.Function([], output)
mutated_mod['func_6578'] = func_6578
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6604 = relay.var("var_6604", dtype = "float64", shape = (16, 3, 8))#candidate|6604|(16, 3, 8)|var|float64
uop_6605 = relay.acos(var_6604.astype('float64')) # shape=(16, 3, 8)
func_6190_call = mod.get_global_var('func_6190')
func_6193_call = mutated_mod.get_global_var('func_6193')
var_6609 = relay.var("var_6609", dtype = "uint64", shape = (1296,))#candidate|6609|(1296,)|var|uint64
call_6608 = relay.TupleGetItem(func_6190_call(relay.reshape(var_6609.astype('uint64'), [1296,])), 6)
call_6610 = relay.TupleGetItem(func_6193_call(relay.reshape(var_6609.astype('uint64'), [1296,])), 6)
func_2807_call = mod.get_global_var('func_2807')
func_2809_call = mutated_mod.get_global_var('func_2809')
call_6611 = func_2807_call()
call_6612 = func_2807_call()
uop_6615 = relay.sin(var_6604.astype('float32')) # shape=(16, 3, 8)
output = relay.Tuple([uop_6605,call_6608,var_6609,call_6611,uop_6615,])
output2 = relay.Tuple([uop_6605,call_6610,var_6609,call_6612,uop_6615,])
func_6618 = relay.Function([var_6604,var_6609,], output)
mod['func_6618'] = func_6618
mod = relay.transform.InferType()(mod)
var_6619 = relay.var("var_6619", dtype = "float64", shape = (16, 3, 8))#candidate|6619|(16, 3, 8)|var|float64
var_6620 = relay.var("var_6620", dtype = "uint64", shape = (1296,))#candidate|6620|(1296,)|var|uint64
output = func_6618(var_6619,var_6620,)
func_6621 = relay.Function([var_6619,var_6620,], output)
mutated_mod['func_6621'] = func_6621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5336_call = mod.get_global_var('func_5336')
func_5337_call = mutated_mod.get_global_var('func_5337')
call_6623 = relay.TupleGetItem(func_5336_call(), 0)
call_6624 = relay.TupleGetItem(func_5337_call(), 0)
func_4950_call = mod.get_global_var('func_4950')
func_4951_call = mutated_mod.get_global_var('func_4951')
call_6632 = relay.TupleGetItem(func_4950_call(), 0)
call_6633 = relay.TupleGetItem(func_4951_call(), 0)
func_4433_call = mod.get_global_var('func_4433')
func_4435_call = mutated_mod.get_global_var('func_4435')
call_6644 = relay.TupleGetItem(func_4433_call(), 1)
call_6645 = relay.TupleGetItem(func_4435_call(), 1)
uop_6646 = relay.log10(call_6632.astype('float32')) # shape=(25, 4)
uop_6648 = relay.log10(call_6633.astype('float32')) # shape=(25, 4)
bop_6669 = relay.right_shift(uop_6646.astype('int64'), relay.reshape(call_6632.astype('int64'), relay.shape_of(uop_6646))) # shape=(25, 4)
bop_6672 = relay.right_shift(uop_6648.astype('int64'), relay.reshape(call_6633.astype('int64'), relay.shape_of(uop_6648))) # shape=(25, 4)
bop_6676 = relay.less(bop_6669.astype('bool'), relay.reshape(call_6632.astype('bool'), relay.shape_of(bop_6669))) # shape=(25, 4)
bop_6679 = relay.less(bop_6672.astype('bool'), relay.reshape(call_6633.astype('bool'), relay.shape_of(bop_6672))) # shape=(25, 4)
const_6689 = relay.const([[[0.174283,8.621645,8.981071,-1.277424,0.738443,-1.106558,-3.759989,-8.845179,-2.941125,7.802772,-7.447342],[-5.094376,8.708791,-1.493341,6.058935,0.802862,6.457056,-3.482999,3.968832,0.877170,0.334415,1.291735],[5.727233,-2.207813,8.446191,-8.560504,4.689176,8.847321,-2.936315,-3.738361,4.529397,-2.831904,-7.546214],[5.399015,-8.352158,-4.410306,-6.861342,6.774285,2.638698,7.987151,0.774617,9.039367,-0.781391,3.813034]],[[-9.303113,1.039868,3.190518,-9.338651,-3.832245,6.408792,9.053889,-5.763597,3.699760,8.735341,-4.556745],[0.788471,-1.261849,-8.384502,8.553192,-6.371105,1.375244,4.666589,6.910476,-1.031964,-2.679335,-1.353730],[9.246399,2.109866,-8.084741,-8.481222,-2.413232,-4.967435,-6.988543,3.684295,-2.251988,7.961788,6.562340],[6.275934,9.553151,4.092369,0.784502,8.959148,-0.834572,-5.941055,3.356717,4.656294,-5.881380,7.970294]]], dtype = "float32")#candidate|6689|(2, 4, 11)|const|float32
bop_6690 = relay.bitwise_and(call_6623.astype('int8'), const_6689.astype('int8')) # shape=(2, 4, 11)
bop_6693 = relay.bitwise_and(call_6624.astype('int8'), const_6689.astype('int8')) # shape=(2, 4, 11)
output = relay.Tuple([call_6644,bop_6676,bop_6690,])
output2 = relay.Tuple([call_6645,bop_6679,bop_6693,])
func_6706 = relay.Function([], output)
mod['func_6706'] = func_6706
mod = relay.transform.InferType()(mod)
mutated_mod['func_6706'] = func_6706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6706_call = mutated_mod.get_global_var('func_6706')
call_6707 = func_6706_call()
output = call_6707
func_6708 = relay.Function([], output)
mutated_mod['func_6708'] = func_6708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3742_call = mod.get_global_var('func_3742')
func_3743_call = mutated_mod.get_global_var('func_3743')
call_6728 = func_3742_call()
call_6729 = func_3742_call()
func_3514_call = mod.get_global_var('func_3514')
func_3516_call = mutated_mod.get_global_var('func_3516')
call_6730 = relay.TupleGetItem(func_3514_call(), 0)
call_6731 = relay.TupleGetItem(func_3516_call(), 0)
func_5186_call = mod.get_global_var('func_5186')
func_5188_call = mutated_mod.get_global_var('func_5188')
call_6738 = relay.TupleGetItem(func_5186_call(), 0)
call_6739 = relay.TupleGetItem(func_5188_call(), 0)
output = relay.Tuple([call_6728,call_6730,call_6738,])
output2 = relay.Tuple([call_6729,call_6731,call_6739,])
func_6741 = relay.Function([], output)
mod['func_6741'] = func_6741
mod = relay.transform.InferType()(mod)
output = func_6741()
func_6742 = relay.Function([], output)
mutated_mod['func_6742'] = func_6742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3837_call = mod.get_global_var('func_3837')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_6748 = relay.TupleGetItem(func_3837_call(), 0)
call_6749 = relay.TupleGetItem(func_3838_call(), 0)
output = relay.Tuple([call_6748,])
output2 = relay.Tuple([call_6749,])
func_6752 = relay.Function([], output)
mod['func_6752'] = func_6752
mod = relay.transform.InferType()(mod)
output = func_6752()
func_6753 = relay.Function([], output)
mutated_mod['func_6753'] = func_6753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6267_call = mod.get_global_var('func_6267')
func_6269_call = mutated_mod.get_global_var('func_6269')
call_6779 = relay.TupleGetItem(func_6267_call(), 3)
call_6780 = relay.TupleGetItem(func_6269_call(), 3)
var_6791 = relay.var("var_6791", dtype = "float32", shape = (2, 4, 13))#candidate|6791|(2, 4, 13)|var|float32
bop_6792 = relay.logical_xor(call_6779.astype('uint16'), var_6791.astype('uint16')) # shape=(2, 4, 13)
bop_6795 = relay.logical_xor(call_6780.astype('uint16'), var_6791.astype('uint16')) # shape=(2, 4, 13)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_6796 = relay.TupleGetItem(func_1489_call(), 0)
call_6797 = relay.TupleGetItem(func_1490_call(), 0)
output = relay.Tuple([bop_6792,call_6796,])
output2 = relay.Tuple([bop_6795,call_6797,])
func_6799 = relay.Function([var_6791,], output)
mod['func_6799'] = func_6799
mod = relay.transform.InferType()(mod)
var_6800 = relay.var("var_6800", dtype = "float32", shape = (2, 4, 13))#candidate|6800|(2, 4, 13)|var|float32
output = func_6799(var_6800)
func_6801 = relay.Function([var_6800], output)
mutated_mod['func_6801'] = func_6801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3514_call = mod.get_global_var('func_3514')
func_3516_call = mutated_mod.get_global_var('func_3516')
call_6827 = relay.TupleGetItem(func_3514_call(), 4)
call_6828 = relay.TupleGetItem(func_3516_call(), 4)
func_2807_call = mod.get_global_var('func_2807')
func_2809_call = mutated_mod.get_global_var('func_2809')
call_6837 = func_2807_call()
call_6838 = func_2807_call()
output = relay.Tuple([call_6827,call_6837,])
output2 = relay.Tuple([call_6828,call_6838,])
func_6841 = relay.Function([], output)
mod['func_6841'] = func_6841
mod = relay.transform.InferType()(mod)
mutated_mod['func_6841'] = func_6841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6841_call = mutated_mod.get_global_var('func_6841')
call_6842 = func_6841_call()
output = call_6842
func_6843 = relay.Function([], output)
mutated_mod['func_6843'] = func_6843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_7045 = relay.TupleGetItem(func_1647_call(), 1)
call_7046 = relay.TupleGetItem(func_1649_call(), 1)
output = relay.Tuple([call_7045,])
output2 = relay.Tuple([call_7046,])
func_7069 = relay.Function([], output)
mod['func_7069'] = func_7069
mod = relay.transform.InferType()(mod)
output = func_7069()
func_7070 = relay.Function([], output)
mutated_mod['func_7070'] = func_7070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6267_call = mod.get_global_var('func_6267')
func_6269_call = mutated_mod.get_global_var('func_6269')
call_7137 = relay.TupleGetItem(func_6267_call(), 0)
call_7138 = relay.TupleGetItem(func_6269_call(), 0)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_7176 = relay.TupleGetItem(func_1891_call(), 0)
call_7177 = relay.TupleGetItem(func_1892_call(), 0)
output = relay.Tuple([call_7137,call_7176,])
output2 = relay.Tuple([call_7138,call_7177,])
func_7189 = relay.Function([], output)
mod['func_7189'] = func_7189
mod = relay.transform.InferType()(mod)
mutated_mod['func_7189'] = func_7189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7189_call = mutated_mod.get_global_var('func_7189')
call_7190 = func_7189_call()
output = call_7190
func_7191 = relay.Function([], output)
mutated_mod['func_7191'] = func_7191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3994_call = mod.get_global_var('func_3994')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_7244 = relay.TupleGetItem(func_3994_call(), 0)
call_7245 = relay.TupleGetItem(func_3996_call(), 0)
func_2030_call = mod.get_global_var('func_2030')
func_2031_call = mutated_mod.get_global_var('func_2031')
call_7249 = relay.TupleGetItem(func_2030_call(), 2)
call_7250 = relay.TupleGetItem(func_2031_call(), 2)
func_4846_call = mod.get_global_var('func_4846')
func_4848_call = mutated_mod.get_global_var('func_4848')
var_7255 = relay.var("var_7255", dtype = "float32", shape = (96,))#candidate|7255|(96,)|var|float32
call_7254 = func_4846_call(relay.reshape(var_7255.astype('float32'), [2, 4, 12]))
call_7256 = func_4846_call(relay.reshape(var_7255.astype('float32'), [2, 4, 12]))
bop_7270 = relay.divide(call_7244.astype('float64'), call_7249.astype('float64')) # shape=(2, 4, 648)
bop_7273 = relay.divide(call_7245.astype('float64'), call_7250.astype('float64')) # shape=(2, 4, 648)
uop_7280 = relay.exp(bop_7270.astype('float64')) # shape=(2, 4, 648)
uop_7282 = relay.exp(bop_7273.astype('float64')) # shape=(2, 4, 648)
func_2666_call = mod.get_global_var('func_2666')
func_2667_call = mutated_mod.get_global_var('func_2667')
call_7288 = relay.TupleGetItem(func_2666_call(), 2)
call_7289 = relay.TupleGetItem(func_2667_call(), 2)
output = relay.Tuple([call_7254,var_7255,uop_7280,call_7288,])
output2 = relay.Tuple([call_7256,var_7255,uop_7282,call_7289,])
func_7300 = relay.Function([var_7255,], output)
mod['func_7300'] = func_7300
mod = relay.transform.InferType()(mod)
mutated_mod['func_7300'] = func_7300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7301 = relay.var("var_7301", dtype = "float32", shape = (96,))#candidate|7301|(96,)|var|float32
func_7300_call = mutated_mod.get_global_var('func_7300')
call_7302 = func_7300_call(var_7301)
output = call_7302
func_7303 = relay.Function([var_7301], output)
mutated_mod['func_7303'] = func_7303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3798_call = mod.get_global_var('func_3798')
func_3799_call = mutated_mod.get_global_var('func_3799')
call_7308 = func_3798_call()
call_7309 = func_3798_call()
output = relay.Tuple([call_7308,])
output2 = relay.Tuple([call_7309,])
func_7330 = relay.Function([], output)
mod['func_7330'] = func_7330
mod = relay.transform.InferType()(mod)
mutated_mod['func_7330'] = func_7330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7330_call = mutated_mod.get_global_var('func_7330')
call_7331 = func_7330_call()
output = call_7331
func_7332 = relay.Function([], output)
mutated_mod['func_7332'] = func_7332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5530_call = mod.get_global_var('func_5530')
func_5531_call = mutated_mod.get_global_var('func_5531')
call_7359 = func_5530_call()
call_7360 = func_5530_call()
func_2408_call = mod.get_global_var('func_2408')
func_2413_call = mutated_mod.get_global_var('func_2413')
var_7383 = relay.var("var_7383", dtype = "uint16", shape = (588,))#candidate|7383|(588,)|var|uint16
var_7384 = relay.var("var_7384", dtype = "float64", shape = (650,))#candidate|7384|(650,)|var|float64
call_7382 = relay.TupleGetItem(func_2408_call(relay.reshape(var_7383.astype('uint16'), [14, 6, 7]), relay.reshape(var_7383.astype('uint16'), [14, 6, 7]), relay.reshape(call_7359.astype('float32'), [180,]), relay.reshape(var_7384.astype('float64'), [650,]), ), 1)
call_7385 = relay.TupleGetItem(func_2413_call(relay.reshape(var_7383.astype('uint16'), [14, 6, 7]), relay.reshape(var_7383.astype('uint16'), [14, 6, 7]), relay.reshape(call_7359.astype('float32'), [180,]), relay.reshape(var_7384.astype('float64'), [650,]), ), 1)
func_4339_call = mod.get_global_var('func_4339')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_7387 = relay.TupleGetItem(func_4339_call(), 2)
call_7388 = relay.TupleGetItem(func_4340_call(), 2)
func_4695_call = mod.get_global_var('func_4695')
func_4697_call = mutated_mod.get_global_var('func_4697')
call_7396 = relay.TupleGetItem(func_4695_call(), 1)
call_7397 = relay.TupleGetItem(func_4697_call(), 1)
bop_7401 = relay.minimum(var_7384.astype('uint16'), call_7387.astype('uint16')) # shape=(2, 4, 650)
bop_7404 = relay.minimum(var_7384.astype('uint16'), call_7388.astype('uint16')) # shape=(2, 4, 650)
uop_7411 = relay.cos(call_7396.astype('float32')) # shape=(100,)
uop_7413 = relay.cos(call_7397.astype('float32')) # shape=(100,)
func_4149_call = mod.get_global_var('func_4149')
func_4154_call = mutated_mod.get_global_var('func_4154')
var_7448 = relay.var("var_7448", dtype = "uint64", shape = (560,))#candidate|7448|(560,)|var|uint64
var_7449 = relay.var("var_7449", dtype = "int32", shape = (135,))#candidate|7449|(135,)|var|int32
call_7447 = relay.TupleGetItem(func_4149_call(relay.reshape(var_7448.astype('uint64'), [560,]), relay.reshape(var_7449.astype('int32'), [135,]), relay.reshape(call_7396.astype('float32'), [100,]), ), 6)
call_7450 = relay.TupleGetItem(func_4154_call(relay.reshape(var_7448.astype('uint64'), [560,]), relay.reshape(var_7449.astype('int32'), [135,]), relay.reshape(call_7396.astype('float32'), [100,]), ), 6)
output = relay.Tuple([call_7359,call_7382,var_7383,bop_7401,uop_7411,call_7447,var_7448,var_7449,])
output2 = relay.Tuple([call_7360,call_7385,var_7383,bop_7404,uop_7413,call_7450,var_7448,var_7449,])
func_7476 = relay.Function([var_7383,var_7384,var_7448,var_7449,], output)
mod['func_7476'] = func_7476
mod = relay.transform.InferType()(mod)
var_7477 = relay.var("var_7477", dtype = "uint16", shape = (588,))#candidate|7477|(588,)|var|uint16
var_7478 = relay.var("var_7478", dtype = "float64", shape = (650,))#candidate|7478|(650,)|var|float64
var_7479 = relay.var("var_7479", dtype = "uint64", shape = (560,))#candidate|7479|(560,)|var|uint64
var_7480 = relay.var("var_7480", dtype = "int32", shape = (135,))#candidate|7480|(135,)|var|int32
output = func_7476(var_7477,var_7478,var_7479,var_7480,)
func_7481 = relay.Function([var_7477,var_7478,var_7479,var_7480,], output)
mutated_mod['func_7481'] = func_7481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mod.get_global_var('func_4537')
func_4539_call = mutated_mod.get_global_var('func_4539')
call_7493 = func_4537_call()
call_7494 = func_4537_call()
func_2030_call = mod.get_global_var('func_2030')
func_2031_call = mutated_mod.get_global_var('func_2031')
call_7500 = relay.TupleGetItem(func_2030_call(), 2)
call_7501 = relay.TupleGetItem(func_2031_call(), 2)
uop_7508 = relay.atan(call_7500.astype('float64')) # shape=(648,)
uop_7510 = relay.atan(call_7501.astype('float64')) # shape=(648,)
func_1891_call = mod.get_global_var('func_1891')
func_1892_call = mutated_mod.get_global_var('func_1892')
call_7520 = relay.TupleGetItem(func_1891_call(), 0)
call_7521 = relay.TupleGetItem(func_1892_call(), 0)
output = relay.Tuple([call_7493,uop_7508,call_7520,])
output2 = relay.Tuple([call_7494,uop_7510,call_7521,])
func_7523 = relay.Function([], output)
mod['func_7523'] = func_7523
mod = relay.transform.InferType()(mod)
mutated_mod['func_7523'] = func_7523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mutated_mod.get_global_var('func_7523')
call_7524 = func_7523_call()
output = call_7524
func_7525 = relay.Function([], output)
mutated_mod['func_7525'] = func_7525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5530_call = mod.get_global_var('func_5530')
func_5531_call = mutated_mod.get_global_var('func_5531')
call_7582 = func_5530_call()
call_7583 = func_5530_call()
func_6706_call = mod.get_global_var('func_6706')
func_6708_call = mutated_mod.get_global_var('func_6708')
call_7585 = relay.TupleGetItem(func_6706_call(), 1)
call_7586 = relay.TupleGetItem(func_6708_call(), 1)
uop_7603 = relay.cos(call_7585.astype('float64')) # shape=(25, 4)
uop_7605 = relay.cos(call_7586.astype('float64')) # shape=(25, 4)
func_1647_call = mod.get_global_var('func_1647')
func_1649_call = mutated_mod.get_global_var('func_1649')
call_7607 = relay.TupleGetItem(func_1647_call(), 1)
call_7608 = relay.TupleGetItem(func_1649_call(), 1)
func_2477_call = mod.get_global_var('func_2477')
func_2479_call = mutated_mod.get_global_var('func_2479')
var_7614 = relay.var("var_7614", dtype = "uint64", shape = (455,))#candidate|7614|(455,)|var|uint64
call_7613 = relay.TupleGetItem(func_2477_call(relay.reshape(var_7614.astype('uint64'), [455,])), 4)
call_7615 = relay.TupleGetItem(func_2479_call(relay.reshape(var_7614.astype('uint64'), [455,])), 4)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_7621 = relay.TupleGetItem(func_6480_call(relay.reshape(var_7614.astype('uint64'), [455,])), 2)
call_7622 = relay.TupleGetItem(func_6482_call(relay.reshape(var_7614.astype('uint64'), [455,])), 2)
var_7623 = relay.var("var_7623", dtype = "float64", shape = (25, 4))#candidate|7623|(25, 4)|var|float64
bop_7624 = relay.left_shift(uop_7603.astype('int8'), relay.reshape(var_7623.astype('int8'), relay.shape_of(uop_7603))) # shape=(25, 4)
bop_7627 = relay.left_shift(uop_7605.astype('int8'), relay.reshape(var_7623.astype('int8'), relay.shape_of(uop_7605))) # shape=(25, 4)
bop_7628 = relay.floor_divide(uop_7603.astype('float32'), relay.reshape(bop_7624.astype('float32'), relay.shape_of(uop_7603))) # shape=(25, 4)
bop_7631 = relay.floor_divide(uop_7605.astype('float32'), relay.reshape(bop_7627.astype('float32'), relay.shape_of(uop_7605))) # shape=(25, 4)
func_1339_call = mod.get_global_var('func_1339')
func_1341_call = mutated_mod.get_global_var('func_1341')
call_7632 = relay.TupleGetItem(func_1339_call(), 0)
call_7633 = relay.TupleGetItem(func_1341_call(), 0)
output = relay.Tuple([call_7582,call_7607,call_7613,var_7614,call_7621,bop_7628,call_7632,])
output2 = relay.Tuple([call_7583,call_7608,call_7615,var_7614,call_7622,bop_7631,call_7633,])
func_7639 = relay.Function([var_7614,var_7623,], output)
mod['func_7639'] = func_7639
mod = relay.transform.InferType()(mod)
mutated_mod['func_7639'] = func_7639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7639_call = mutated_mod.get_global_var('func_7639')
var_7641 = relay.var("var_7641", dtype = "uint64", shape = (455,))#candidate|7641|(455,)|var|uint64
var_7642 = relay.var("var_7642", dtype = "float64", shape = (25, 4))#candidate|7642|(25, 4)|var|float64
call_7640 = func_7639_call(var_7641,var_7642,)
output = call_7640
func_7643 = relay.Function([var_7641,var_7642,], output)
mutated_mod['func_7643'] = func_7643
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7648 = relay.var("var_7648", dtype = "uint8", shape = (2, 5, 10))#candidate|7648|(2, 5, 10)|var|uint8
var_7649 = relay.var("var_7649", dtype = "uint8", shape = (2, 5, 10))#candidate|7649|(2, 5, 10)|var|uint8
bop_7650 = relay.greater_equal(var_7648.astype('bool'), relay.reshape(var_7649.astype('bool'), relay.shape_of(var_7648))) # shape=(2, 5, 10)
func_6190_call = mod.get_global_var('func_6190')
func_6193_call = mutated_mod.get_global_var('func_6193')
var_7654 = relay.var("var_7654", dtype = "uint64", shape = (1296,))#candidate|7654|(1296,)|var|uint64
call_7653 = relay.TupleGetItem(func_6190_call(relay.reshape(var_7654.astype('uint64'), [1296,])), 0)
call_7655 = relay.TupleGetItem(func_6193_call(relay.reshape(var_7654.astype('uint64'), [1296,])), 0)
func_2742_call = mod.get_global_var('func_2742')
func_2744_call = mutated_mod.get_global_var('func_2744')
const_7671 = relay.const([-4.091353,0.131876,-5.457572,4.770668,-0.285411,2.303736,5.610876,-7.251464,8.322770,-0.751659,-9.586890,-9.839639,-3.061402,0.342787,3.252043,0.545447,-3.169378,0.217864,2.031345,7.535991,3.702398,-8.374066,5.822891,-2.204476,4.334901,0.026289,-1.937865,-6.226555,-0.820479,-2.008014,1.616371,4.493439,6.355856,-8.219295,-8.100844,-9.678368,-4.614999,-6.111125,5.061831,-0.250669,-2.632546,-4.811151,7.796166,3.567869,-6.943795,-5.372882,3.753460,-8.658377,-3.850580,3.320916,-8.158695,-0.396048,-6.782023,3.656122,-0.115010,9.854811,7.202413,5.077548,-4.903789,9.306195,4.385396,-2.959269,9.449043,2.356670,3.007475,-8.002507,-9.238075,7.287143,-3.295207,-8.189529,-7.369371,0.914170,-5.085207,9.827358,5.483884,5.040796,-7.369921,8.744823,-0.835840,2.608236,-1.902212,-8.458823,-9.517275,9.200245,-5.681602,8.639884,4.695217,-6.170048,-8.485859,3.199627,-2.520429,-9.689448,-1.419058,4.367266,-7.564907,7.181050,-0.872203,9.636379,0.897336,7.402886,-7.326821,-2.216125,6.790914,8.608332,-0.194099,1.907157,-6.509115,4.639635,-6.147986,7.725524,5.855377,0.783829,-0.505880,1.212627,2.946716,9.649022,2.134478,-9.235304,1.382420,-3.098594], dtype = "float64")#candidate|7671|(120,)|const|float64
call_7670 = relay.TupleGetItem(func_2742_call(relay.reshape(const_7671.astype('float64'), [2, 4, 15])), 2)
call_7672 = relay.TupleGetItem(func_2744_call(relay.reshape(const_7671.astype('float64'), [2, 4, 15])), 2)
func_4475_call = mod.get_global_var('func_4475')
func_4477_call = mutated_mod.get_global_var('func_4477')
call_7674 = relay.TupleGetItem(func_4475_call(), 1)
call_7675 = relay.TupleGetItem(func_4477_call(), 1)
func_6267_call = mod.get_global_var('func_6267')
func_6269_call = mutated_mod.get_global_var('func_6269')
call_7694 = relay.TupleGetItem(func_6267_call(), 2)
call_7695 = relay.TupleGetItem(func_6269_call(), 2)
uop_7710 = relay.atanh(call_7674.astype('float32')) # shape=(9, 9, 8)
uop_7712 = relay.atanh(call_7675.astype('float32')) # shape=(9, 9, 8)
output = relay.Tuple([bop_7650,call_7653,var_7654,call_7670,const_7671,call_7694,uop_7710,])
output2 = relay.Tuple([bop_7650,call_7655,var_7654,call_7672,const_7671,call_7695,uop_7712,])
func_7715 = relay.Function([var_7648,var_7649,var_7654,], output)
mod['func_7715'] = func_7715
mod = relay.transform.InferType()(mod)
mutated_mod['func_7715'] = func_7715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7715_call = mutated_mod.get_global_var('func_7715')
var_7717 = relay.var("var_7717", dtype = "uint8", shape = (2, 5, 10))#candidate|7717|(2, 5, 10)|var|uint8
var_7718 = relay.var("var_7718", dtype = "uint8", shape = (2, 5, 10))#candidate|7718|(2, 5, 10)|var|uint8
var_7719 = relay.var("var_7719", dtype = "uint64", shape = (1296,))#candidate|7719|(1296,)|var|uint64
call_7716 = func_7715_call(var_7717,var_7718,var_7719,)
output = call_7716
func_7720 = relay.Function([var_7717,var_7718,var_7719,], output)
mutated_mod['func_7720'] = func_7720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5480_call = mod.get_global_var('func_5480')
func_5482_call = mutated_mod.get_global_var('func_5482')
call_7868 = relay.TupleGetItem(func_5480_call(), 0)
call_7869 = relay.TupleGetItem(func_5482_call(), 0)
func_5530_call = mod.get_global_var('func_5530')
func_5531_call = mutated_mod.get_global_var('func_5531')
call_7889 = func_5530_call()
call_7890 = func_5530_call()
func_5412_call = mod.get_global_var('func_5412')
func_5414_call = mutated_mod.get_global_var('func_5414')
call_7891 = relay.TupleGetItem(func_5412_call(), 1)
call_7892 = relay.TupleGetItem(func_5414_call(), 1)
func_3837_call = mod.get_global_var('func_3837')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_7897 = relay.TupleGetItem(func_3837_call(), 0)
call_7898 = relay.TupleGetItem(func_3838_call(), 0)
func_4208_call = mod.get_global_var('func_4208')
func_4212_call = mutated_mod.get_global_var('func_4212')
const_7909 = relay.const(-2, dtype = "uint64")#candidate|7909|()|const|uint64
var_7910 = relay.var("var_7910", dtype = "uint64", shape = (1296,))#candidate|7910|(1296,)|var|uint64
const_7911 = relay.const([0.563494,-1.180201,7.881208,-5.919503,7.109769,2.636509,2.759248,0.385492,-3.319526,-4.204617,-4.686096,-2.778077,-8.371217,1.612747,6.727188,-0.348909,-4.386393,-6.910739,-8.974645,7.619883,0.589209,5.278520,-9.231374,8.687575,4.774217,2.286744,8.824862,-4.702896,2.138129,7.464110,-8.421360,3.801055,-5.063871,-4.084361,-4.911410,3.187788,-5.437083,-8.277688,8.800804,-0.160485,5.341182,-1.548163,1.783196,3.245791,2.010907,6.149824,-7.394309,-3.198855,-5.955280,-1.071846,-4.301593,9.131663,-7.708018,3.744111,3.443421,-4.989264,-4.001144,4.057303,8.709242,-4.637939,0.084477,-1.661707,-1.234647,6.719740,-7.611343,3.362245,0.154479,7.082268,-1.655693,8.058293,-8.077008,6.691771,-8.705063,-7.767265,9.856358,-8.946898,9.290655,-0.888228,-0.695225,-5.647480,5.909108,1.266484,-9.286374,-6.395224,-5.385631,9.627078,1.113271,8.425905,4.131718,0.628838,-6.060907,-9.002639,1.624088,7.344927,-5.075778,-0.674384,1.371519,-4.132060,-0.389064,-7.761284,-5.589445,-9.713520,-2.034304,5.470801,9.186647,-2.320768,9.440619,7.350801,-5.657191,-6.464310,3.800416,-7.168085,-3.135622,-9.111476,-3.776285,7.970048,-5.002853,-6.837509,0.475914,9.499638,7.764712,-6.921328,-8.615549,5.725190,-1.317338,6.250353,-0.174790,-7.163218,-5.510675,1.670609,-3.677167,6.886817,-6.289219,8.030861,1.584141,6.221798,1.238119,3.657028,5.722685,-2.071073,-9.887355,5.937443,9.064135,-7.749478,4.129252,-2.653412,-6.326494,-0.094733,-5.111651,1.831856,-2.799353,-4.760351,-2.800700,7.532541,-4.841105,-3.767173,0.538093,0.210372,0.918603,-6.994684,4.510622,-0.158831,-8.589965,4.814720,8.270559,2.436341,2.390960,5.075046,2.164174,4.115695,-3.617090,5.934771,-5.074191,-7.842710,-6.723500,-8.039933,-8.151078,8.791046,2.615386,5.997001,1.868683,5.409748,-0.190565,2.471494,3.487215,3.859248,-5.127782,-0.263032,1.180344,-1.996776,9.138032,6.320514,-4.010708,2.042683,0.672320,-7.464740,6.586940,3.420545,-0.442843,8.937572,-4.442792,3.840880,0.953167,0.082854,-0.119710,-0.988968,-3.754087,8.232612,9.152173,-9.379932,5.146632,4.515986,-2.141604,-0.568148,6.034969,6.798994,-1.417290,-5.880515,-4.874655,-8.465005,-4.890999,-9.239886,9.467188,1.091957,-4.643611,6.564091,-9.517006,-2.795983,-6.896004,2.705490,7.909432,7.722206,3.708091,1.267780,7.114717,-2.236281,0.280888,-4.681188,6.386343,0.853418,8.573061,9.329832,1.974587,4.899224,3.144168,-4.935146,7.016947,-2.200637,5.099760,-1.526534,-8.596779,-8.052493,4.227996,-2.056057,-6.825032,0.696061,-8.082033,7.929097,-2.312508,2.049940,3.601818,-2.302460,2.735902,7.752903,5.849124,9.787388,3.862138,3.092972,-6.366966,5.199451,6.547243,4.744135,3.897230,9.274137,4.501117,1.006695,-3.632106,2.985767,7.520836,9.765205,-2.249307,-5.347362,-6.226716,-5.748334,2.771273,-3.515126,-6.132811,-6.130206,-9.999510,-8.457544,3.863335,9.718584,3.787758,2.725154,3.913184,3.429987,-5.224879,7.541792,7.633051,9.371041,4.300946,9.761995,1.040816,-0.374379,-0.679390,0.377921,-1.238127,6.809970,4.993343,-2.944651,7.433642,-8.332266,8.486326,0.696509,-8.286426,5.175569,-8.240393,1.029045,6.572083,2.166797,-3.972415,7.810536,4.817579,7.568625,6.367445,-9.505448,2.282091,-6.012904,-0.215602,-6.444700,8.561911,7.399494,-1.781454,6.987297,-3.220377,1.563620,-8.389926,5.645530,-0.009290,-4.453814,3.647287,-1.960012,-1.537022,0.842311,-0.645498,4.203567,-4.686322,9.133530,0.408978,-1.441719,-2.282109,6.197781,-5.524546,-6.391263,6.026086,-3.559065,1.656656,2.115554,-8.489371,5.304968,-3.689729,-3.225075,6.662137,-1.065761,-0.862231,-9.118101,-2.491994,9.832536,-6.763045,2.566999,1.398606,-4.904602,2.155222,-7.695858,7.069139,-4.423546,-2.084615,-2.824069,3.572159,-4.096275,5.944971,-2.052410,-0.625137,-0.396063,1.118431,-8.665604,7.205288,-2.055629,9.144464,-6.168466,-3.212862,-4.237133,5.445331,-5.591927,1.223958,2.831943,6.201857,4.056226,3.463442,-6.631290,3.370817,3.247102,-2.892579,1.705165,-0.453928,-3.084411,4.194748,1.530749,3.649540,6.206153,7.779800,6.414068,-9.571107,-4.069294,-3.296149,-3.654646,-3.606773,-8.645881,7.986743,-3.796433,-4.958100,-6.734494,5.613472,-4.241940,3.864722,-9.572465,-2.505160,5.351160,-2.011527,7.703512,1.327877,-2.362445,4.605028,-2.039124,5.815182,4.252889,1.264471,9.253471,1.991208,0.068149,0.639992,7.539432,4.646793,-6.926492,9.971946,-9.418286,3.635210,-6.956205,1.577243,-6.465323,9.000170,-3.338074,6.109449,2.127744,-7.760294,-5.558156,-0.813990,2.661478,-0.102099,6.362262,0.897436,-9.681256,0.096454,-3.331239,3.767320,9.576186,-9.126532,7.054992,7.931983,-6.186123,4.897932,0.855180,0.929683,6.357419,-0.804800,4.431332,-7.926814,-5.103273,-7.485375,2.752417,1.133660,-7.865130,-9.601251,-4.151781,-3.026493,8.227196,2.980882,-6.176286,-6.604448,-6.267607,-8.400318,-4.612975,-3.091433,-4.973285,7.930280,-2.441544,-6.724317,-8.267566,4.258318,-5.599550,-1.281438,1.081835,-2.093109,-6.403456,-2.185227,1.830100,-4.107649,7.772252,2.585978,3.777992,9.263174,7.812333,-6.233418,4.812292,-8.545339,7.029721,7.123980,-2.487818,-1.365613,-7.135835,-4.877662,-6.140779,-4.506779,7.761463,0.386365,-1.963819,-1.986165,8.966561,-2.242406,-1.426252,-0.045826,4.425798,6.454643,-5.311643,-8.183796,-4.887128,-2.416987,7.304870,-5.687082,-7.164503,2.761811,3.905532,5.293009,-7.091629,3.525258,-4.254124,-9.527042,2.781978,-5.185896,-3.259677,0.320503,3.873624,4.861542,-7.446768,8.241502,6.674069,6.643716,-1.291481,4.747779,-3.995682,-7.612005,3.525502,-5.089858,-9.496151,-2.501044,2.055591,0.441876,7.454346,8.754181,-8.850522,2.854058,7.335315,-9.806791,0.925437,-5.847932,-1.910746,-1.705700,-6.686887,7.052373,6.146970,9.990923,2.429228,0.524712,0.774350,-3.196346,8.733542,6.270474,-1.917061,7.603281,-4.000305,-0.279718,-7.684887,-7.418467,4.525093,6.105065,9.676744,-8.051426,8.078563,0.821016,-0.604682,-7.021325,7.687474,7.358718,-1.372352,0.827865,-6.681645,5.844024,2.984972,3.065873,5.527866,5.657401,0.526413,9.054889,-7.109500,5.536664,-7.186431,-3.237618,-8.176002,-3.067129,-3.982060,3.666442,1.264065,0.513936,-1.936298,0.252687,2.308210,-8.076213,-6.655612,1.310067,-5.059094,-8.740736,4.420060,1.444132,-8.665217,-7.452510,0.196444,5.986892,-3.253192,5.490519,-3.688492,8.537817,-2.953363,-0.809713,2.473777,2.205557,9.781869,7.199737,-4.417611], dtype = "float32")#candidate|7911|(648,)|const|float32
call_7908 = relay.TupleGetItem(func_4208_call(relay.reshape(const_7909.astype('uint64'), []), relay.reshape(var_7910.astype('uint64'), [9, 16, 9]), relay.reshape(const_7911.astype('float32'), [648,]), ), 2)
call_7912 = relay.TupleGetItem(func_4212_call(relay.reshape(const_7909.astype('uint64'), []), relay.reshape(var_7910.astype('uint64'), [9, 16, 9]), relay.reshape(const_7911.astype('float32'), [648,]), ), 2)
output = relay.Tuple([call_7868,call_7889,call_7891,call_7897,call_7908,const_7909,var_7910,const_7911,])
output2 = relay.Tuple([call_7869,call_7890,call_7892,call_7898,call_7912,const_7909,var_7910,const_7911,])
func_7922 = relay.Function([var_7910,], output)
mod['func_7922'] = func_7922
mod = relay.transform.InferType()(mod)
mutated_mod['func_7922'] = func_7922
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7923 = relay.var("var_7923", dtype = "uint64", shape = (1296,))#candidate|7923|(1296,)|var|uint64
func_7922_call = mutated_mod.get_global_var('func_7922')
call_7924 = func_7922_call(var_7923)
output = call_7924
func_7925 = relay.Function([var_7923], output)
mutated_mod['func_7925'] = func_7925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6460_call = mod.get_global_var('func_6460')
func_6462_call = mutated_mod.get_global_var('func_6462')
call_7985 = relay.TupleGetItem(func_6460_call(), 2)
call_7986 = relay.TupleGetItem(func_6462_call(), 2)
output = relay.Tuple([call_7985,])
output2 = relay.Tuple([call_7986,])
func_7987 = relay.Function([], output)
mod['func_7987'] = func_7987
mod = relay.transform.InferType()(mod)
mutated_mod['func_7987'] = func_7987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7987_call = mutated_mod.get_global_var('func_7987')
call_7988 = func_7987_call()
output = call_7988
func_7989 = relay.Function([], output)
mutated_mod['func_7989'] = func_7989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3036_call = mod.get_global_var('func_3036')
func_3038_call = mutated_mod.get_global_var('func_3038')
call_7990 = relay.TupleGetItem(func_3036_call(), 2)
call_7991 = relay.TupleGetItem(func_3038_call(), 2)
func_7639_call = mod.get_global_var('func_7639')
func_7643_call = mutated_mod.get_global_var('func_7643')
var_8019 = relay.var("var_8019", dtype = "uint64", shape = (65, 7))#candidate|8019|(65, 7)|var|uint64
const_8020 = relay.const([3.937305,3.511822,-9.593981,6.886411,3.908721,-9.525143,2.188670,1.119977,-7.829289,-8.424052,9.825687,-1.027493,3.672266,-4.767266,-6.065426,-4.980372,-6.477224,-8.469062,-3.275963,1.362177,1.655758,0.657520,-9.783328,-1.589710,7.236714,3.906149,5.851453,-4.633305,8.211185,-1.894049,8.167961,5.758526,-2.068616,9.873040,-8.895361,-4.203523,-7.967658,-1.280362,0.378120,-8.269303,4.187467,9.008315,8.243797,4.155610,-0.978696,3.022352,6.650191,3.099674,-1.014323,-3.047813,3.106063,7.132963,3.525100,-0.485987,-3.170560,9.037918,-5.710181,-7.681243,4.885329,1.586224,7.899003,3.129442,0.501393,8.565486,3.595777,-7.958677,-7.412975,0.430031,2.364556,-5.930944,-7.333094,5.579980,-5.035992,-2.755937,-6.800529,6.263921,-6.774276,-9.432121,-2.085822,-9.361987,7.854727,-4.129141,-4.575469,2.403073,-9.417905,0.344783,-9.673305,8.215200,-5.997466,-1.607664,7.137917,6.385296,-5.372049,-8.950359,8.527056,6.422674,2.129447,-3.454833,7.631034,-1.379642], dtype = "float64")#candidate|8020|(100,)|const|float64
call_8018 = relay.TupleGetItem(func_7639_call(relay.reshape(var_8019.astype('uint64'), [455,]), relay.reshape(const_8020.astype('float64'), [25, 4]), ), 6)
call_8021 = relay.TupleGetItem(func_7643_call(relay.reshape(var_8019.astype('uint64'), [455,]), relay.reshape(const_8020.astype('float64'), [25, 4]), ), 6)
output = relay.Tuple([call_7990,call_8018,var_8019,const_8020,])
output2 = relay.Tuple([call_7991,call_8021,var_8019,const_8020,])
func_8025 = relay.Function([var_8019,], output)
mod['func_8025'] = func_8025
mod = relay.transform.InferType()(mod)
mutated_mod['func_8025'] = func_8025
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8026 = relay.var("var_8026", dtype = "uint64", shape = (65, 7))#candidate|8026|(65, 7)|var|uint64
func_8025_call = mutated_mod.get_global_var('func_8025')
call_8027 = func_8025_call(var_8026)
output = call_8027
func_8028 = relay.Function([var_8026], output)
mutated_mod['func_8028'] = func_8028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4433_call = mod.get_global_var('func_4433')
func_4435_call = mutated_mod.get_global_var('func_4435')
call_8052 = relay.TupleGetItem(func_4433_call(), 0)
call_8053 = relay.TupleGetItem(func_4435_call(), 0)
const_8062 = relay.const([[[3.789285,4.139732,0.486100,-0.214141,-1.816882,9.225790,6.512100],[5.846504,-8.046916,2.438080,4.047018,-6.388070,3.650227,9.806956],[-0.689399,-0.110448,-6.176375,2.697149,5.851733,7.610003,-9.150312],[-3.522485,7.899976,0.869107,-1.729414,-0.634043,5.548318,8.953591]],[[8.299024,6.337056,5.196510,4.687685,-7.340169,9.587795,-7.562352],[8.787454,3.022202,-7.043540,5.798018,-7.645731,6.526997,-2.781987],[3.861386,1.055978,-3.425534,2.840380,-3.771527,6.155461,2.869169],[-7.104550,3.961187,8.043039,-1.239076,7.733185,8.994608,0.442945]]], dtype = "float64")#candidate|8062|(2, 4, 7)|const|float64
bop_8063 = relay.floor_divide(call_8052.astype('float32'), const_8062.astype('float32')) # shape=(2, 4, 7)
bop_8066 = relay.floor_divide(call_8053.astype('float32'), const_8062.astype('float32')) # shape=(2, 4, 7)
func_6741_call = mod.get_global_var('func_6741')
func_6742_call = mutated_mod.get_global_var('func_6742')
call_8069 = relay.TupleGetItem(func_6741_call(), 2)
call_8070 = relay.TupleGetItem(func_6742_call(), 2)
bop_8077 = relay.less_equal(call_8052.astype('bool'), const_8062.astype('bool')) # shape=(2, 4, 7)
bop_8080 = relay.less_equal(call_8053.astype('bool'), const_8062.astype('bool')) # shape=(2, 4, 7)
output = relay.Tuple([bop_8063,call_8069,bop_8077,])
output2 = relay.Tuple([bop_8066,call_8070,bop_8080,])
func_8087 = relay.Function([], output)
mod['func_8087'] = func_8087
mod = relay.transform.InferType()(mod)
mutated_mod['func_8087'] = func_8087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8087_call = mutated_mod.get_global_var('func_8087')
call_8088 = func_8087_call()
output = call_8088
func_8089 = relay.Function([], output)
mutated_mod['func_8089'] = func_8089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8135 = relay.var("var_8135", dtype = "float32", shape = ())#candidate|8135|()|var|float32
const_8136 = relay.const([[[-0.573009],[-2.633501],[-6.290929],[-4.577614],[-3.755958],[9.972080],[-7.205697],[7.793397],[0.324249],[-2.659346],[9.019301]],[[-5.571362],[1.967447],[7.200659],[-7.603163],[2.819829],[6.258218],[-9.347908],[-3.590213],[-6.808598],[6.661117],[4.802004]],[[-5.463603],[-6.442590],[4.732845],[6.776810],[1.114187],[4.666224],[-9.090144],[6.942566],[-3.983936],[7.363950],[-7.432695]],[[3.492858],[-2.866521],[2.886726],[0.121442],[5.696124],[7.800894],[1.206942],[-8.022161],[8.128628],[8.080077],[0.923180]],[[-4.937503],[-4.112016],[6.698799],[-4.736959],[6.330393],[-4.490506],[6.555351],[2.427794],[-0.015952],[-4.226857],[-8.954823]],[[6.708233],[6.665075],[-7.171978],[2.012217],[-8.623021],[4.211884],[-2.426957],[-6.108971],[-0.571976],[8.082008],[3.579738]],[[0.044031],[0.041437],[0.819923],[6.897339],[-1.852222],[-9.401838],[-1.040261],[-0.267697],[-0.025439],[7.479148],[4.296283]],[[6.956660],[-1.586270],[4.342825],[-0.790096],[0.001974],[-2.645010],[-4.678256],[-3.957236],[2.955024],[-6.863228],[-8.827174]],[[1.694641],[-6.767774],[0.701673],[9.644306],[-4.253912],[-2.339393],[-2.597684],[-4.845384],[-7.159577],[-7.566370],[-0.245938]],[[-3.234152],[4.947403],[9.840019],[-0.480358],[-7.311805],[-2.405134],[2.154875],[-6.790433],[-8.909837],[4.344890],[2.104826]],[[0.619421],[2.675811],[5.043780],[-7.433753],[-9.027444],[3.467008],[-2.361072],[2.922441],[-6.095583],[-0.639777],[-7.434731]],[[0.049282],[-2.220698],[4.544123],[-3.361520],[-9.190313],[-4.656042],[-6.494402],[8.873997],[-1.455571],[1.202209],[8.925136]],[[-1.733260],[-8.386473],[-8.735023],[-0.405044],[6.578593],[7.721477],[5.182707],[3.606635],[-3.418557],[6.640828],[9.133678]],[[-2.800851],[-8.779855],[-1.246203],[-1.675685],[-3.148215],[-5.842307],[-8.499798],[8.500113],[-6.232553],[-1.122176],[7.269016]],[[-2.299702],[4.521537],[-3.164180],[-4.924649],[-8.477212],[-3.783295],[6.364766],[8.414466],[0.133702],[-4.799631],[-6.198414]]], dtype = "float32")#candidate|8136|(15, 11, 1)|const|float32
bop_8137 = relay.not_equal(var_8135.astype('bool'), const_8136.astype('bool')) # shape=(15, 11, 1)
func_4537_call = mod.get_global_var('func_4537')
func_4539_call = mutated_mod.get_global_var('func_4539')
call_8142 = func_4537_call()
call_8143 = func_4537_call()
bop_8146 = relay.minimum(const_8136.astype('uint8'), var_8135.astype('uint8')) # shape=(15, 11, 1)
func_4475_call = mod.get_global_var('func_4475')
func_4477_call = mutated_mod.get_global_var('func_4477')
call_8149 = relay.TupleGetItem(func_4475_call(), 0)
call_8150 = relay.TupleGetItem(func_4477_call(), 0)
output = relay.Tuple([bop_8137,call_8142,bop_8146,call_8149,])
output2 = relay.Tuple([bop_8137,call_8143,bop_8146,call_8150,])
func_8152 = relay.Function([var_8135,], output)
mod['func_8152'] = func_8152
mod = relay.transform.InferType()(mod)
mutated_mod['func_8152'] = func_8152
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8153 = relay.var("var_8153", dtype = "float32", shape = ())#candidate|8153|()|var|float32
func_8152_call = mutated_mod.get_global_var('func_8152')
call_8154 = func_8152_call(var_8153)
output = call_8154
func_8155 = relay.Function([var_8153], output)
mutated_mod['func_8155'] = func_8155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2960_call = mod.get_global_var('func_2960')
func_2962_call = mutated_mod.get_global_var('func_2962')
call_8189 = relay.TupleGetItem(func_2960_call(), 0)
call_8190 = relay.TupleGetItem(func_2962_call(), 0)
func_6415_call = mod.get_global_var('func_6415')
func_6417_call = mutated_mod.get_global_var('func_6417')
call_8202 = relay.TupleGetItem(func_6415_call(), 0)
call_8203 = relay.TupleGetItem(func_6417_call(), 0)
output = relay.Tuple([call_8189,call_8202,])
output2 = relay.Tuple([call_8190,call_8203,])
func_8208 = relay.Function([], output)
mod['func_8208'] = func_8208
mod = relay.transform.InferType()(mod)
output = func_8208()
func_8209 = relay.Function([], output)
mutated_mod['func_8209'] = func_8209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6350_call = mod.get_global_var('func_6350')
func_6352_call = mutated_mod.get_global_var('func_6352')
call_8241 = relay.TupleGetItem(func_6350_call(), 1)
call_8242 = relay.TupleGetItem(func_6352_call(), 1)
uop_8244 = relay.sqrt(call_8241.astype('float32')) # shape=(2, 4, 560)
uop_8246 = relay.sqrt(call_8242.astype('float32')) # shape=(2, 4, 560)
bop_8251 = relay.not_equal(uop_8244.astype('bool'), relay.reshape(call_8241.astype('bool'), relay.shape_of(uop_8244))) # shape=(2, 4, 560)
bop_8254 = relay.not_equal(uop_8246.astype('bool'), relay.reshape(call_8242.astype('bool'), relay.shape_of(uop_8246))) # shape=(2, 4, 560)
func_4339_call = mod.get_global_var('func_4339')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_8260 = relay.TupleGetItem(func_4339_call(), 2)
call_8261 = relay.TupleGetItem(func_4340_call(), 2)
output = relay.Tuple([bop_8251,call_8260,])
output2 = relay.Tuple([bop_8254,call_8261,])
func_8262 = relay.Function([], output)
mod['func_8262'] = func_8262
mod = relay.transform.InferType()(mod)
mutated_mod['func_8262'] = func_8262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8262_call = mutated_mod.get_global_var('func_8262')
call_8263 = func_8262_call()
output = call_8263
func_8264 = relay.Function([], output)
mutated_mod['func_8264'] = func_8264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_8271 = func_1316_call()
call_8272 = func_1316_call()
output = call_8271
output2 = call_8272
func_8283 = relay.Function([], output)
mod['func_8283'] = func_8283
mod = relay.transform.InferType()(mod)
mutated_mod['func_8283'] = func_8283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8283_call = mutated_mod.get_global_var('func_8283')
call_8284 = func_8283_call()
output = call_8284
func_8285 = relay.Function([], output)
mutated_mod['func_8285'] = func_8285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_8297 = func_1316_call()
call_8298 = func_1316_call()
func_6577_call = mod.get_global_var('func_6577')
func_6578_call = mutated_mod.get_global_var('func_6578')
call_8334 = relay.TupleGetItem(func_6577_call(), 0)
call_8335 = relay.TupleGetItem(func_6578_call(), 0)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_8350 = relay.TupleGetItem(func_5223_call(), 0)
call_8351 = relay.TupleGetItem(func_5225_call(), 0)
output = relay.Tuple([call_8297,call_8334,call_8350,])
output2 = relay.Tuple([call_8298,call_8335,call_8351,])
func_8352 = relay.Function([], output)
mod['func_8352'] = func_8352
mod = relay.transform.InferType()(mod)
output = func_8352()
func_8353 = relay.Function([], output)
mutated_mod['func_8353'] = func_8353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2555_call = mod.get_global_var('func_2555')
func_2557_call = mutated_mod.get_global_var('func_2557')
call_8377 = relay.TupleGetItem(func_2555_call(), 0)
call_8378 = relay.TupleGetItem(func_2557_call(), 0)
output = relay.Tuple([call_8377,])
output2 = relay.Tuple([call_8378,])
func_8403 = relay.Function([], output)
mod['func_8403'] = func_8403
mod = relay.transform.InferType()(mod)
output = func_8403()
func_8404 = relay.Function([], output)
mutated_mod['func_8404'] = func_8404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1489_call = mod.get_global_var('func_1489')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_8411 = relay.TupleGetItem(func_1489_call(), 0)
call_8412 = relay.TupleGetItem(func_1490_call(), 0)
output = call_8411
output2 = call_8412
func_8419 = relay.Function([], output)
mod['func_8419'] = func_8419
mod = relay.transform.InferType()(mod)
mutated_mod['func_8419'] = func_8419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8419_call = mutated_mod.get_global_var('func_8419')
call_8420 = func_8419_call()
output = call_8420
func_8421 = relay.Function([], output)
mutated_mod['func_8421'] = func_8421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5265_call = mod.get_global_var('func_5265')
func_5267_call = mutated_mod.get_global_var('func_5267')
call_8437 = relay.TupleGetItem(func_5265_call(), 0)
call_8438 = relay.TupleGetItem(func_5267_call(), 0)
output = call_8437
output2 = call_8438
func_8441 = relay.Function([], output)
mod['func_8441'] = func_8441
mod = relay.transform.InferType()(mod)
mutated_mod['func_8441'] = func_8441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8441_call = mutated_mod.get_global_var('func_8441')
call_8442 = func_8441_call()
output = call_8442
func_8443 = relay.Function([], output)
mutated_mod['func_8443'] = func_8443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5225_call = mutated_mod.get_global_var('func_5225')
call_8481 = relay.TupleGetItem(func_5223_call(), 0)
call_8482 = relay.TupleGetItem(func_5225_call(), 0)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_8491 = func_1316_call()
call_8492 = func_1316_call()
func_2030_call = mod.get_global_var('func_2030')
func_2031_call = mutated_mod.get_global_var('func_2031')
call_8499 = relay.TupleGetItem(func_2030_call(), 1)
call_8500 = relay.TupleGetItem(func_2031_call(), 1)
func_7476_call = mod.get_global_var('func_7476')
func_7481_call = mutated_mod.get_global_var('func_7481')
const_8502 = relay.const([-4,9,-7,7,4,9,-4,-5,7,-6,-6,7,8,9,9,-3,7,4,10,1,1,-8,-3,10,6,-10,-6,-10,-8,-8,-2,-9,4,2,5,7,-1,1,-9,3,-10,8,2,10,6,7,8,7,-1,5,-4,2,-7,-1,-7,-10,9,-2,-5,-3,10,-10,-7,-10,8,6,8,-7,-2,-1,-3,7,2,-5,2,9,7,10,-8,4,-10,10,-8,-4,7,3,-10,-4,-10,9,-6,-3,10,8,-8,6,3,-5,-6,5,-6,-5,-9,-7,9,-10,-4,9,10,2,2,-5,5,-5,-9,-6,9,9,10,6,2,6,2,-10,5,-10,1,1,5,8,-6,-9,6,4,4,7,7,3,-1,2,4,-2,-7,-2,-8,-6,-5,-1,3,-8,5,-4,-9,2,10,5,-5,-1,-7,-3,-5,1,-2,-2,-8,-1,-4,-7,-1,-2,-2,5,3,8,-8,4,9,-5,8,7,6,10,4,4,6,-4,-2,-6,4,-6,8,-10,-5,-10,-2,10,-7,-9,-8,6,-10,6,1,8,9,-2,2,-4,6,-2,2,-8,2,2,2,-8,10,4,-8,-9,-4,2,4,5,-9,-10,-10,-2,8,4,3,2,-6,7,1,-8,8,3,3,1,8,3,-10,8,-8,-9,4,4,-10,-1,6,7,9,-7,-1,-4,-2,5,-1,-1,7,10,1,-1,-3,-3,-4,-7,2,5,4,10,-8,9,10,-10,2,-10,2,-6,-6,5,9,2,4,5,-9,-6,-10,8,-7,-8,-6,1,-2,2,6,-7,-9,-8,-6,-3,-8,4,3,9,-8,-6,7,-4,-6,6,-4,-9,-4,8,-2,7,-9,7,2,-2,2,7,-7,10,-5,-5,1,-4,3,-7,2,-4,-6,4,6,8,-6,-9,4,-8,6,-2,9,2,-7,-8,4,1,-2,7,1,-6,-10,1,2,7,-3,5,-2,-6,7,-9,6,2,-6,-4,8,-5,-2,-4,-6,-4,-7,-10,5,1,8,4,1,9,-9,-4,4,-5,6,3,-10,10,4,-10,4,3,-1,-5,7,8,9,-10,3,-1,7,-10,1,-8,-8,5,10,-5,7,1,-5,9,-5,9,6,-7,-4,-4,7,-9,10,8,-4,-9,2,-6,-3,3,3,3,1,-6,9,9,10,10,4,10,-10,10,10,-10,-10,-10,6,4,-5,4,10,7,-3,-10,6,6,8,9,1,-1,-4,-6,4,10,2,-3,-9,-2,9,1,3,-1,-1,-9,2,3,-2,-8,9,-8,-4,-3,1,-7,-9,-8,-4,-3,1,-9,-3,9,-3,4,5,-5,10,3,-5,-6,9,-9,2,9,-6,-6,-3,6,4,-2,-9,7,6,5,-2,-8,-2,3,-6,1,3,3,-4,5,-7,6,-3,7,5,-1,-10,8,-3,-10,-7,3,8,-7,-4,-10,-9,-9,1,2,-10,5,-3,6,7,-6,-6,-4,6,-9,-6,-3,5,-7,-10,4,-3,1,-1,-1,2,-3,-8,-3,10,5,10,1,2,4,9,1,9,8,-1,-8,-10,-1,10,3,7,4,-7,-5], dtype = "uint16")#candidate|8502|(588,)|const|uint16
var_8503 = relay.var("var_8503", dtype = "float64", shape = (650, 1))#candidate|8503|(650, 1)|var|float64
var_8504 = relay.var("var_8504", dtype = "uint64", shape = (40, 14))#candidate|8504|(40, 14)|var|uint64
const_8505 = relay.const([-7,7,-5,10,8,4,-7,-7,-8,-2,-7,4,7,-4,-9,2,-5,-1,-7,-6,2,2,8,4,2,10,4,-1,-2,-7,-4,-4,-1,-9,-7,3,6,1,-7,-9,2,8,-7,-8,-4,9,-6,-8,9,-5,-4,-6,-4,-4,1,-9,5,10,6,1,2,7,3,7,1,-8,2,5,2,-6,5,7,-5,-3,2,-9,4,-6,-9,10,-7,-7,4,-5,-1,1,-8,-5,-3,4,-2,4,6,6,-3,7,7,-6,-6,-9,-4,3,7,7,-6,-7,-1,-6,-1,6,9,3,-9,-6,2,4,-6,-9,6,-4,6,-3,-4,-6,1,8,-7,-7,10,1,-9,-7,3,9,-10], dtype = "int32")#candidate|8505|(135,)|const|int32
call_8501 = relay.TupleGetItem(func_7476_call(relay.reshape(const_8502.astype('uint16'), [588,]), relay.reshape(var_8503.astype('float64'), [650,]), relay.reshape(var_8504.astype('uint64'), [560,]), relay.reshape(const_8505.astype('int32'), [135,]), ), 2)
call_8506 = relay.TupleGetItem(func_7481_call(relay.reshape(const_8502.astype('uint16'), [588,]), relay.reshape(var_8503.astype('float64'), [650,]), relay.reshape(var_8504.astype('uint64'), [560,]), relay.reshape(const_8505.astype('int32'), [135,]), ), 2)
bop_8512 = relay.not_equal(const_8502.astype('bool'), call_8481.astype('bool')) # shape=(2, 4, 588)
bop_8515 = relay.not_equal(const_8502.astype('bool'), call_8482.astype('bool')) # shape=(2, 4, 588)
output = relay.Tuple([call_8491,call_8499,call_8501,var_8503,var_8504,const_8505,bop_8512,])
output2 = relay.Tuple([call_8492,call_8500,call_8506,var_8503,var_8504,const_8505,bop_8515,])
func_8518 = relay.Function([var_8503,var_8504,], output)
mod['func_8518'] = func_8518
mod = relay.transform.InferType()(mod)
var_8519 = relay.var("var_8519", dtype = "float64", shape = (650, 1))#candidate|8519|(650, 1)|var|float64
var_8520 = relay.var("var_8520", dtype = "uint64", shape = (40, 14))#candidate|8520|(40, 14)|var|uint64
output = func_8518(var_8519,var_8520,)
func_8521 = relay.Function([var_8519,var_8520,], output)
mutated_mod['func_8521'] = func_8521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3958_call = mod.get_global_var('func_3958')
func_3960_call = mutated_mod.get_global_var('func_3960')
call_8547 = func_3958_call()
call_8548 = func_3958_call()
func_6741_call = mod.get_global_var('func_6741')
func_6742_call = mutated_mod.get_global_var('func_6742')
call_8561 = relay.TupleGetItem(func_6741_call(), 1)
call_8562 = relay.TupleGetItem(func_6742_call(), 1)
func_4339_call = mod.get_global_var('func_4339')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_8590 = relay.TupleGetItem(func_4339_call(), 0)
call_8591 = relay.TupleGetItem(func_4340_call(), 0)
func_2201_call = mod.get_global_var('func_2201')
func_2206_call = mutated_mod.get_global_var('func_2206')
const_8609 = relay.const([-9,2,7,6,-3,8,-8,3,8,2,8,-1,9,6,-8,-8,5,9,-2,-9,10,7,10,7,9,-6,-7,-7,4,2,2,1,2,9,-2,10,-8,2,-6,-8,10,3,-2,-6,6,10,-7,-5,-10,-2,-5,-6,7,2,7,-8,5,4,6,8,7,-1,-9,-1,1,3,4,-8,5,4,-10,-7,-8,4,3,7,10,-2,4,-9,-7,-10,10,-3,6,7,2,10,-6,-5,6,9,-9,4,4,-8,-4,1,-4,10,-2,7,2,-7,4,9,3,6,9,-7,3,-6,-2,2,-3,-8,-9,10,-4,10,-10,-8,7,7,3,-2,7,-5,7,7,-10,-5,-1,2,4], dtype = "int32")#candidate|8609|(135,)|const|int32
const_8610 = relay.const([9.481877,-8.816228,3.205181,5.149985,-9.375743,3.567257,1.909191,1.636314,1.575651,-7.200049,-3.795538,-7.732306,4.022381,-6.779941,9.159329,5.259434,-3.830084,4.164396,4.443678,6.020069,-5.386604,2.623270,1.760840,7.316296,7.747662,-5.626938,3.488433,-5.402326,0.188121,5.508506,-2.755727,1.931319,9.950301,-3.258360,5.651088,-2.323191,-2.124745,2.549022,-5.387941,8.390474,-1.381221,8.586186,-8.065995,-6.395672,8.034507,-8.630234,-5.592934,-6.229264,3.754733,1.791361,9.041881,-8.813258,8.348319,1.998327,-1.841264,1.491524,-7.532749,-4.791185,-8.211094,-9.752603,4.168932,-5.399424,-9.944743,0.614089,5.359221,-4.899845,-8.628069,4.238682,-6.977475,-1.704866,4.613440,-3.335892,-0.407953,-9.611797,4.391284,-0.992996,0.439856,1.706722,-4.636078,3.276523,0.986400,-9.428477,6.822652,5.222846,-7.133815,-0.447901,-8.758143,4.621061,-5.002812,3.508544,3.984660,-1.814540,-6.706612,-0.786721,-6.180083,7.672154,-2.207546,8.706417,7.275677,2.863247,-2.469783,3.086970,-4.886909,-7.229380,-9.234442,1.786247,0.787222,-0.120315,2.804347,-7.569547,7.627909,1.990134,4.240042,4.276753,5.144854,-2.737667,-6.523581,-9.395798,7.129003,4.283120,0.644292,8.878279,-0.309158,-8.880269,-2.239531,5.118448,-5.489217,8.007896,-0.966749,-2.004531,-2.725367,8.299605,-2.442887,9.337844,-0.415557,3.531990,2.815415,6.828733,5.957298,3.398093,-8.260940,4.701452,4.602371,5.499274,7.775504,-2.065632,-9.528498,-0.140739,1.310655,-6.387508,5.067075,4.686506,-2.149256,-5.816562,9.047445,-5.167828,5.023614,-9.359861,-2.489206,-5.086214,-3.777978,3.283910,-0.846490,7.062125,-6.399320,-4.270336,-8.624571,-5.606135,-2.253814,-1.266869,5.140369,0.321129,-5.848751,7.636083,2.701131,-0.123345,-8.927849,9.727322,5.736084,4.840617,-5.127667,5.424801,8.289390,-6.530091,3.178841,7.339606,8.796986,9.166572,2.471307,-7.418122,-1.984750,-3.768571,3.650736,2.370176,-4.347036,-0.619463,-0.168424,5.194358,2.557631,3.040506,-2.803671,5.296594,-1.555421,1.989589,-5.269439,-1.273470,-2.653883,2.854090,-3.804532,5.177054,3.095046,-0.361393,5.736837,-1.651977,7.220582,9.496825,-1.684102,9.447260,6.719097,-2.843528,-3.842550,-3.814783,2.123630,-5.976843,9.156691,9.567777,3.223948,-9.237950,3.768952,-0.592102,2.315772,9.758825,-8.520451,-8.781031,9.213921,8.381004,6.072969,3.726912,-9.857130,8.104772,5.593362,-1.255521,-5.998939,3.228728,0.662637,-8.702341,-1.842314,1.457950,-1.430943,-1.549708,-7.141255,4.594842,-2.424188,5.280231,9.983477,-7.747652,9.736454,0.115399,3.169307,1.568831,-6.534004,1.432382,0.322076,-6.081921,-5.014931,-9.210775,-5.690908,6.724589,-4.803677,4.471929,7.233117,-9.249272,6.639894], dtype = "float64")#candidate|8610|(273,)|const|float64
call_8608 = relay.TupleGetItem(func_2201_call(relay.reshape(call_8547.astype('float64'), [25, 4]), relay.reshape(const_8609.astype('int32'), [135,]), relay.reshape(const_8610.astype('float64'), [39, 7]), ), 1)
call_8611 = relay.TupleGetItem(func_2206_call(relay.reshape(call_8547.astype('float64'), [25, 4]), relay.reshape(const_8609.astype('int32'), [135,]), relay.reshape(const_8610.astype('float64'), [39, 7]), ), 1)
const_8616 = relay.const([[False,False,True,False],[False,False,False,True],[True,True,True,False],[True,False,False,True],[False,True,True,True],[True,True,True,True],[False,True,False,True],[True,True,True,True],[True,False,False,False],[False,False,True,True],[True,True,True,True],[True,True,False,True],[False,False,True,True],[True,False,True,True],[True,True,False,True],[False,True,False,False],[True,False,False,True],[True,True,True,False],[False,False,True,False],[False,False,True,False],[False,False,False,True],[True,True,True,False],[False,True,True,True],[True,False,True,False],[False,True,False,True]], dtype = "bool")#candidate|8616|(25, 4)|const|bool
bop_8617 = relay.maximum(call_8547.astype('uint8'), relay.reshape(const_8616.astype('uint8'), relay.shape_of(call_8547))) # shape=(25, 4)
bop_8620 = relay.maximum(call_8548.astype('uint8'), relay.reshape(const_8616.astype('uint8'), relay.shape_of(call_8548))) # shape=(25, 4)
output = relay.Tuple([call_8561,call_8590,call_8608,const_8609,const_8610,bop_8617,])
output2 = relay.Tuple([call_8562,call_8591,call_8611,const_8609,const_8610,bop_8620,])
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
