import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_574 = relay.var("var_574", dtype = "float64", shape = (2, 15, 3))#candidate|574|(2, 15, 3)|var|float64
uop_575 = relay.asinh(var_574.astype('float64')) # shape=(2, 15, 3)
uop_579 = relay.log2(uop_575.astype('float64')) # shape=(2, 15, 3)
uop_581 = relay.sinh(uop_575.astype('float64')) # shape=(2, 15, 3)
output = relay.Tuple([uop_579,uop_581,])
output2 = relay.Tuple([uop_579,uop_581,])
func_584 = relay.Function([var_574,], output)
mod['func_584'] = func_584
mod = relay.transform.InferType()(mod)
var_585 = relay.var("var_585", dtype = "float64", shape = (2, 15, 3))#candidate|585|(2, 15, 3)|var|float64
output = func_584(var_585)
func_586 = relay.Function([var_585], output)
mutated_mod['func_586'] = func_586
mutated_mod = relay.transform.InferType()(mutated_mod)
const_613 = relay.const([[[7.557375,-1.962241,-0.975891,1.629021,-7.968471,9.731696,-6.114676,6.814289,-1.941895,5.662135,6.204181,0.797267,-5.069981],[-1.832609,-0.912313,-3.536851,8.780045,-8.051977,0.522532,-2.180287,0.598289,8.527581,-9.826598,5.364333,-6.265391,5.718618],[-3.902079,-4.552147,-3.715179,-5.306777,-1.803309,-0.492348,-0.888696,9.156246,0.532571,9.020181,-3.287991,-3.345105,9.619223],[1.330263,-8.468780,3.792630,-7.552655,-3.977327,-0.835143,9.141203,5.134998,3.154584,-5.508508,3.865496,-6.884794,1.686677],[-1.695709,1.344427,1.341829,2.552923,7.288258,-6.940686,-2.370346,8.965564,-0.750265,7.245296,-3.898386,5.116793,-0.785962],[-6.059966,0.761343,6.433638,-1.541978,0.162452,7.674623,1.948158,3.661446,-5.038710,-1.088458,6.603229,-6.516730,-6.090937],[7.693164,-7.844717,7.326008,-5.764166,-8.759461,-7.604652,5.215646,-4.575363,-6.857755,9.369423,2.189801,-4.253132,1.054891],[-4.706912,-0.883569,5.416407,-3.378593,8.197083,-8.436304,-1.259186,7.226229,2.757784,-8.615527,-0.715454,-4.193260,0.223598],[3.321568,8.032514,6.270328,7.329832,9.114765,8.107261,-2.362604,1.020157,-6.638668,3.930253,-0.003221,-8.609193,-9.733916],[1.719486,0.034445,-9.077911,-1.001514,3.996697,-2.615084,-7.038017,8.994476,1.191276,-6.027170,3.584552,0.954086,2.904910],[8.611571,-9.345978,-9.709500,-3.646479,-8.435091,-6.655441,3.642687,-8.828611,-2.746246,6.133683,-8.274707,8.392677,2.982541],[-4.049374,6.678317,-2.625835,6.179539,-6.328046,-1.286637,3.132720,-2.383475,-5.014726,-5.916242,4.961412,1.875328,-6.683673]],[[6.882297,-6.056116,-9.436438,3.550726,-2.254948,4.357472,9.051532,3.982442,-3.437142,-3.596399,6.244690,-7.236778,-9.455121],[-7.576270,-9.491279,2.532250,4.763642,-6.271928,-4.058401,3.076246,7.353501,6.360085,2.791088,1.403105,7.439016,-4.247203],[-4.652897,-9.733973,-9.368891,-7.515339,-7.672130,-8.129322,7.268056,0.355790,5.312763,9.812419,8.115539,2.628072,3.234007],[1.673955,-3.865208,9.943463,-7.998074,0.566418,5.693582,-1.300075,-4.614409,0.146644,2.194031,4.489804,1.044507,-3.225438],[4.534683,1.487411,-1.466342,-5.243709,-6.717971,7.952295,1.484279,2.235741,-2.130888,-7.679698,3.894866,-3.886834,6.791373],[1.372589,-3.965958,9.651502,9.689445,1.439397,8.391983,-8.075853,5.440700,8.977213,2.181493,7.150036,-4.364369,-1.279168],[9.698441,-2.273514,-2.242652,-8.952693,9.116709,1.026295,-4.806195,-3.330026,-8.069268,-2.473613,-0.493925,-8.654289,-5.859779],[5.824099,-6.723656,-7.238609,5.331496,-2.811428,-7.541480,-5.573686,-6.313617,-4.498810,-4.604750,7.903542,-9.726623,3.321383],[3.573536,-6.543861,4.918339,-3.964797,8.092061,-7.095616,9.735472,-2.642218,1.260940,-6.633453,-7.456318,-2.168139,3.081432],[6.772552,8.274991,9.548491,7.564633,5.743404,4.496260,-9.720220,-5.052758,5.929583,6.958230,-5.620935,9.098573,-4.202966],[2.037200,-7.082484,-9.351705,-7.994651,-9.704449,-6.262479,6.926140,2.173235,0.187496,9.334999,-1.908982,-7.054999,6.021769],[-5.450217,1.980769,-4.348963,8.502384,8.081540,3.671187,-5.641298,1.786472,1.671164,-0.627270,-4.495665,-2.184147,0.902826]]], dtype = "float32")#candidate|613|(2, 12, 13)|const|float32
uop_614 = relay.cos(const_613.astype('float32')) # shape=(2, 12, 13)
output = uop_614
output2 = uop_614
func_634 = relay.Function([], output)
mod['func_634'] = func_634
mod = relay.transform.InferType()(mod)
mutated_mod['func_634'] = func_634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mutated_mod.get_global_var('func_634')
call_635 = func_634_call()
output = call_635
func_636 = relay.Function([], output)
mutated_mod['func_636'] = func_636
mutated_mod = relay.transform.InferType()(mutated_mod)
var_685 = relay.var("var_685", dtype = "float32", shape = (7, 10, 7))#candidate|685|(7, 10, 7)|var|float32
uop_686 = relay.tan(var_685.astype('float32')) # shape=(7, 10, 7)
output = relay.Tuple([uop_686,])
output2 = relay.Tuple([uop_686,])
func_689 = relay.Function([var_685,], output)
mod['func_689'] = func_689
mod = relay.transform.InferType()(mod)
var_690 = relay.var("var_690", dtype = "float32", shape = (7, 10, 7))#candidate|690|(7, 10, 7)|var|float32
output = func_689(var_690)
func_691 = relay.Function([var_690], output)
mutated_mod['func_691'] = func_691
mutated_mod = relay.transform.InferType()(mutated_mod)
var_744 = relay.var("var_744", dtype = "int64", shape = ())#candidate|744|()|var|int64
var_745 = relay.var("var_745", dtype = "int64", shape = (6, 6, 11))#candidate|745|(6, 6, 11)|var|int64
bop_746 = relay.bitwise_and(var_744.astype('int64'), var_745.astype('int64')) # shape=(6, 6, 11)
uop_752 = relay.acos(var_745.astype('float32')) # shape=(6, 6, 11)
func_584_call = mod.get_global_var('func_584')
func_586_call = mutated_mod.get_global_var('func_586')
const_761 = relay.const([4.979085,9.972418,-2.675838,-7.706289,-5.687708,0.720136,-0.913838,-0.432822,-1.404460,3.702685,-3.841326,-1.307560,2.597221,8.527862,-5.643606,3.992050,4.949465,-8.285395,2.727003,5.162903,-7.845283,1.590334,-8.370985,-9.919623,0.156929,9.573197,-8.519467,-8.927925,-5.596390,2.123254,4.960643,-7.197225,7.198675,-0.601744,4.039831,-8.028877,-3.827320,-1.793612,-4.101069,1.252322,-0.457729,1.825157,2.663528,-2.358440,2.907631,-0.147791,-6.998646,2.201457,5.262433,2.290562,-5.165074,1.049092,8.085203,8.779948,-6.665621,4.867844,9.157586,9.088554,7.133797,-1.578136,4.755506,9.769165,8.966649,7.845193,-4.293490,1.668080,7.331813,2.981914,-3.658785,-6.243432,2.456970,8.760241,-4.888516,3.363317,-6.922310,-8.670934,7.964840,-1.941291,-4.348827,4.315917,-8.981652,1.873926,6.172096,-6.935309,-9.967219,-8.591044,-3.703396,-8.931282,9.286454,-8.676737], dtype = "float64")#candidate|761|(90,)|const|float64
call_760 = relay.TupleGetItem(func_584_call(relay.reshape(const_761.astype('float64'), [2, 15, 3])), 1)
call_762 = relay.TupleGetItem(func_586_call(relay.reshape(const_761.astype('float64'), [2, 15, 3])), 1)
bop_764 = relay.mod(var_745.astype('float64'), relay.reshape(bop_746.astype('float64'), relay.shape_of(var_745))) # shape=(6, 6, 11)
uop_768 = relay.tan(uop_752.astype('float32')) # shape=(6, 6, 11)
bop_774 = relay.right_shift(uop_768.astype('int64'), relay.reshape(bop_764.astype('int64'), relay.shape_of(uop_768))) # shape=(6, 6, 11)
output = relay.Tuple([call_760,const_761,bop_774,])
output2 = relay.Tuple([call_762,const_761,bop_774,])
func_785 = relay.Function([var_744,var_745,], output)
mod['func_785'] = func_785
mod = relay.transform.InferType()(mod)
mutated_mod['func_785'] = func_785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_785_call = mutated_mod.get_global_var('func_785')
var_787 = relay.var("var_787", dtype = "int64", shape = ())#candidate|787|()|var|int64
var_788 = relay.var("var_788", dtype = "int64", shape = (6, 6, 11))#candidate|788|(6, 6, 11)|var|int64
call_786 = func_785_call(var_787,var_788,)
output = call_786
func_789 = relay.Function([var_787,var_788,], output)
mutated_mod['func_789'] = func_789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_809 = func_634_call()
call_810 = func_634_call()
output = relay.Tuple([call_809,])
output2 = relay.Tuple([call_810,])
func_812 = relay.Function([], output)
mod['func_812'] = func_812
mod = relay.transform.InferType()(mod)
output = func_812()
func_813 = relay.Function([], output)
mutated_mod['func_813'] = func_813
mutated_mod = relay.transform.InferType()(mutated_mod)
var_864 = relay.var("var_864", dtype = "uint8", shape = (5, 8, 2))#candidate|864|(5, 8, 2)|var|uint8
const_865 = relay.const([[[2,-1],[-2,9],[-7,7],[-7,-2],[-7,8],[-6,-3],[-9,8],[3,-7]],[[-5,-1],[-7,8],[-1,-2],[2,-7],[-6,-2],[-3,-7],[3,10],[-7,-2]],[[5,9],[4,-6],[2,5],[-3,-2],[-7,-1],[-9,-3],[-4,-10],[-1,-3]],[[-6,8],[2,6],[5,6],[4,-7],[2,1],[8,4],[8,3],[6,6]],[[8,3],[2,-2],[1,-3],[7,5],[-9,9],[-2,-9],[6,-2],[8,6]]], dtype = "uint8")#candidate|865|(5, 8, 2)|const|uint8
bop_866 = relay.subtract(var_864.astype('uint8'), relay.reshape(const_865.astype('uint8'), relay.shape_of(var_864))) # shape=(5, 8, 2)
bop_869 = relay.mod(const_865.astype('float32'), relay.reshape(bop_866.astype('float32'), relay.shape_of(const_865))) # shape=(5, 8, 2)
bop_872 = relay.left_shift(var_864.astype('uint16'), relay.reshape(bop_869.astype('uint16'), relay.shape_of(var_864))) # shape=(5, 8, 2)
uop_882 = relay.asinh(bop_869.astype('float64')) # shape=(5, 8, 2)
output = relay.Tuple([bop_872,uop_882,])
output2 = relay.Tuple([bop_872,uop_882,])
func_886 = relay.Function([var_864,], output)
mod['func_886'] = func_886
mod = relay.transform.InferType()(mod)
var_887 = relay.var("var_887", dtype = "uint8", shape = (5, 8, 2))#candidate|887|(5, 8, 2)|var|uint8
output = func_886(var_887)
func_888 = relay.Function([var_887], output)
mutated_mod['func_888'] = func_888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_812_call = mod.get_global_var('func_812')
func_813_call = mutated_mod.get_global_var('func_813')
call_890 = relay.TupleGetItem(func_812_call(), 0)
call_891 = relay.TupleGetItem(func_813_call(), 0)
const_897 = relay.const([[[2.687262,-0.099242,-8.095436,0.310320,-2.930792,4.984650,-4.648840,8.913006,3.845202,7.950762,7.337029,8.440610,4.157795],[-4.797243,2.716947,7.457579,-8.729205,-8.435500,-2.765921,3.627303,0.106899,8.578932,-2.163134,2.045033,1.662970,2.684943],[5.913352,7.362733,-6.881012,-3.889981,0.459872,1.231557,6.494541,-5.920638,0.290278,-7.927150,-4.427474,3.677036,-3.354916],[9.715510,8.199292,6.337805,4.850473,7.253705,-5.898690,7.400298,8.775253,5.036586,-4.716419,1.439307,2.507214,-6.235068],[8.311252,0.491939,-0.193552,-1.962830,1.404461,0.021855,-4.000478,-3.892809,-1.210423,-1.447025,-1.335797,-9.661806,-8.995741],[5.749443,1.059827,3.328507,9.857626,-0.550354,4.136888,3.211506,-3.177266,4.551574,4.314730,2.149610,4.018215,-2.773210],[6.823447,-0.457610,-2.230428,-2.652215,9.951409,-2.081133,-8.427461,6.200610,0.427143,-7.681350,2.624390,-9.556270,7.049882],[-4.637691,-6.674231,2.678138,0.583165,4.222289,1.619320,0.325922,7.680824,8.168225,-2.210419,-8.817888,1.375793,-7.218520],[-0.280149,0.998718,-4.985241,1.635170,-7.500982,9.556046,-8.784757,9.546578,-8.751512,2.470043,0.608626,3.714117,9.972302],[8.775305,-0.196214,6.899108,6.521499,-4.053401,-5.920220,-4.378414,-7.806016,-5.453091,-9.313596,-5.008532,-1.217845,-5.334123],[-1.060034,0.495064,1.315844,-4.805907,-1.011278,7.417222,2.271599,-8.574475,3.338860,-0.570328,-1.105511,-6.133410,6.467429],[5.958463,-2.583166,5.511511,2.143942,-9.679752,1.202152,-5.296015,-2.988786,3.604682,0.191358,0.780588,-8.695618,5.123461]],[[-9.267475,3.761283,-4.713822,9.121440,1.627195,-6.938225,-9.383752,7.769099,3.473805,0.486632,4.333433,3.827636,-6.649321],[3.740957,5.008417,5.675205,2.127103,5.711011,6.582925,-1.566043,1.494083,5.872830,-5.492295,1.080535,-2.768433,9.508395],[-0.512341,3.030029,-7.621704,0.234200,0.169109,3.261436,-0.938704,-4.613181,-9.205111,-9.776592,8.684133,0.415541,-9.610742],[-5.163811,5.419249,0.668031,-2.815239,9.476117,5.540993,-3.003266,6.665653,7.752348,-9.325930,-5.072614,3.141707,-3.629778],[-3.192864,-4.632336,5.307877,-4.457516,-2.440887,-3.075184,-3.673650,2.638975,-4.501259,-1.879614,-6.995681,2.832983,2.483512],[6.158266,-8.730655,-8.379278,8.706645,-3.857448,2.684006,2.071329,-7.331880,-1.042055,2.069099,-5.085547,-1.671587,-9.628484],[8.294690,5.796640,4.523377,5.337369,0.743750,-3.020419,-8.169214,3.630253,6.839239,9.664240,-3.374234,-7.598679,-1.008306],[9.854855,5.496433,3.735369,-5.697390,-1.500195,6.570403,4.750927,6.056260,9.449313,-5.347594,7.349181,3.891503,9.382855],[-6.702840,-8.736918,0.870943,8.714449,9.214223,5.975765,-8.592106,9.626017,8.029249,-9.750569,-4.961852,-3.120116,-7.405364],[8.794387,-6.419913,5.006166,-0.701761,6.801316,2.512653,8.672607,0.603681,-2.082102,-7.143232,8.302827,7.044776,-0.796717],[6.493462,-4.044396,-1.320882,-1.950632,6.228161,5.138370,9.584350,0.625974,-6.670377,1.251535,1.675126,1.912479,8.961554],[2.528339,-1.499430,-1.782351,-6.043558,8.547070,-1.484956,4.903856,1.329310,-4.024861,-9.912901,0.723423,-2.185195,-0.479250]]], dtype = "float32")#candidate|897|(2, 12, 13)|const|float32
bop_898 = relay.power(call_890.astype('float64'), relay.reshape(const_897.astype('float64'), relay.shape_of(call_890))) # shape=(2, 12, 13)
bop_901 = relay.power(call_891.astype('float64'), relay.reshape(const_897.astype('float64'), relay.shape_of(call_891))) # shape=(2, 12, 13)
func_689_call = mod.get_global_var('func_689')
func_691_call = mutated_mod.get_global_var('func_691')
var_910 = relay.var("var_910", dtype = "float32", shape = (490,))#candidate|910|(490,)|var|float32
call_909 = relay.TupleGetItem(func_689_call(relay.reshape(var_910.astype('float32'), [7, 10, 7])), 0)
call_911 = relay.TupleGetItem(func_691_call(relay.reshape(var_910.astype('float32'), [7, 10, 7])), 0)
var_912 = relay.var("var_912", dtype = "float64", shape = (2, 12, 13))#candidate|912|(2, 12, 13)|var|float64
bop_913 = relay.add(bop_898.astype('float32'), relay.reshape(var_912.astype('float32'), relay.shape_of(bop_898))) # shape=(2, 12, 13)
bop_916 = relay.add(bop_901.astype('float32'), relay.reshape(var_912.astype('float32'), relay.shape_of(bop_901))) # shape=(2, 12, 13)
uop_941 = relay.atanh(call_890.astype('float32')) # shape=(2, 12, 13)
uop_943 = relay.atanh(call_891.astype('float32')) # shape=(2, 12, 13)
var_951 = relay.var("var_951", dtype = "float32", shape = (7, 10, 7))#candidate|951|(7, 10, 7)|var|float32
bop_952 = relay.not_equal(call_909.astype('bool'), relay.reshape(var_951.astype('bool'), relay.shape_of(call_909))) # shape=(7, 10, 7)
bop_955 = relay.not_equal(call_911.astype('bool'), relay.reshape(var_951.astype('bool'), relay.shape_of(call_911))) # shape=(7, 10, 7)
output = relay.Tuple([var_910,bop_913,uop_941,bop_952,])
output2 = relay.Tuple([var_910,bop_916,uop_943,bop_955,])
func_971 = relay.Function([var_910,var_912,var_951,], output)
mod['func_971'] = func_971
mod = relay.transform.InferType()(mod)
mutated_mod['func_971'] = func_971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mutated_mod.get_global_var('func_971')
var_973 = relay.var("var_973", dtype = "float32", shape = (490,))#candidate|973|(490,)|var|float32
var_974 = relay.var("var_974", dtype = "float64", shape = (2, 12, 13))#candidate|974|(2, 12, 13)|var|float64
var_975 = relay.var("var_975", dtype = "float32", shape = (7, 10, 7))#candidate|975|(7, 10, 7)|var|float32
call_972 = func_971_call(var_973,var_974,var_975,)
output = call_972
func_976 = relay.Function([var_973,var_974,var_975,], output)
mutated_mod['func_976'] = func_976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_994 = func_634_call()
call_995 = func_634_call()
uop_1007 = relay.erf(call_994.astype('float64')) # shape=(2, 12, 13)
uop_1009 = relay.erf(call_995.astype('float64')) # shape=(2, 12, 13)
bop_1013 = relay.greater(uop_1007.astype('bool'), relay.reshape(call_994.astype('bool'), relay.shape_of(uop_1007))) # shape=(2, 12, 13)
bop_1016 = relay.greater(uop_1009.astype('bool'), relay.reshape(call_995.astype('bool'), relay.shape_of(uop_1009))) # shape=(2, 12, 13)
output = bop_1013
output2 = bop_1016
func_1023 = relay.Function([], output)
mod['func_1023'] = func_1023
mod = relay.transform.InferType()(mod)
output = func_1023()
func_1024 = relay.Function([], output)
mutated_mod['func_1024'] = func_1024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_1078 = func_1023_call()
call_1079 = func_1023_call()
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
const_1082 = relay.const([-8,-8,4,1,4,-10,3,-1,2,3,7,4,-8,7,1,-9,-8,-5,-1,-10,10,-5,3,-2,-8,-7,-5,-1,5,10,-8,6,7,8,-8,4,-10,2,5,-10,-3,7,7,-10,6,8,-10,-9,4,5,-8,1,-8,-3,9,5,10,1,-10,8,10,9,10,4,-5,-7,10,3,3,10,-9,5,6,5,-6,3,2,-5,-10,-10], dtype = "uint8")#candidate|1082|(80,)|const|uint8
call_1081 = relay.TupleGetItem(func_886_call(relay.reshape(const_1082.astype('uint8'), [5, 8, 2])), 0)
call_1083 = relay.TupleGetItem(func_888_call(relay.reshape(const_1082.astype('uint8'), [5, 8, 2])), 0)
output = relay.Tuple([call_1078,call_1081,const_1082,])
output2 = relay.Tuple([call_1079,call_1083,const_1082,])
func_1088 = relay.Function([], output)
mod['func_1088'] = func_1088
mod = relay.transform.InferType()(mod)
mutated_mod['func_1088'] = func_1088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1088_call = mutated_mod.get_global_var('func_1088')
call_1089 = func_1088_call()
output = call_1089
func_1090 = relay.Function([], output)
mutated_mod['func_1090'] = func_1090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1111 = relay.var("var_1111", dtype = "int64", shape = (10, 3, 6))#candidate|1111|(10, 3, 6)|var|int64
var_1112 = relay.var("var_1112", dtype = "int64", shape = (10, 3, 6))#candidate|1112|(10, 3, 6)|var|int64
bop_1113 = relay.less(var_1111.astype('bool'), relay.reshape(var_1112.astype('bool'), relay.shape_of(var_1111))) # shape=(10, 3, 6)
output = relay.Tuple([bop_1113,])
output2 = relay.Tuple([bop_1113,])
func_1116 = relay.Function([var_1111,var_1112,], output)
mod['func_1116'] = func_1116
mod = relay.transform.InferType()(mod)
var_1117 = relay.var("var_1117", dtype = "int64", shape = (10, 3, 6))#candidate|1117|(10, 3, 6)|var|int64
var_1118 = relay.var("var_1118", dtype = "int64", shape = (10, 3, 6))#candidate|1118|(10, 3, 6)|var|int64
output = func_1116(var_1117,var_1118,)
func_1119 = relay.Function([var_1117,var_1118,], output)
mutated_mod['func_1119'] = func_1119
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1123 = relay.var("var_1123", dtype = "float64", shape = (16, 15, 11))#candidate|1123|(16, 15, 11)|var|float64
uop_1124 = relay.erf(var_1123.astype('float64')) # shape=(16, 15, 11)
bop_1126 = relay.floor_mod(var_1123.astype('float64'), relay.reshape(uop_1124.astype('float64'), relay.shape_of(var_1123))) # shape=(16, 15, 11)
bop_1136 = relay.equal(bop_1126.astype('bool'), relay.reshape(uop_1124.astype('bool'), relay.shape_of(bop_1126))) # shape=(16, 15, 11)
output = bop_1136
output2 = bop_1136
func_1146 = relay.Function([var_1123,], output)
mod['func_1146'] = func_1146
mod = relay.transform.InferType()(mod)
var_1147 = relay.var("var_1147", dtype = "float64", shape = (16, 15, 11))#candidate|1147|(16, 15, 11)|var|float64
output = func_1146(var_1147)
func_1148 = relay.Function([var_1147], output)
mutated_mod['func_1148'] = func_1148
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1224 = relay.var("var_1224", dtype = "float64", shape = (4, 1, 16))#candidate|1224|(4, 1, 16)|var|float64
uop_1225 = relay.cos(var_1224.astype('float64')) # shape=(4, 1, 16)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
const_1234 = relay.const([-6,7,-6,-2,-10,-6,4,-9,3,7,-3,-2,-4,5,-5,-3,1,-8,10,3,8,8,-9,7,2,-3,4,6,-6,-2,-3,-4,7,-1,-2,9,-6,-2,-6,8,-2,-3,-4,6,1,-3,-3,1,8,8,-8,10,6,10,10,9,9,-8,-4,5,2,-2,-4,6,-6,-2,1,-8,-3,-10,8,-4,-3,10,-9,-5,-2,10,1,-7], dtype = "uint8")#candidate|1234|(80,)|const|uint8
call_1233 = relay.TupleGetItem(func_886_call(relay.reshape(const_1234.astype('uint8'), [5, 8, 2])), 1)
call_1235 = relay.TupleGetItem(func_888_call(relay.reshape(const_1234.astype('uint8'), [5, 8, 2])), 1)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_1243 = relay.TupleGetItem(func_1088_call(), 1)
call_1244 = relay.TupleGetItem(func_1090_call(), 1)
uop_1246 = relay.log2(uop_1225.astype('float32')) # shape=(4, 1, 16)
bop_1248 = relay.logical_and(uop_1246.astype('bool'), relay.reshape(uop_1225.astype('bool'), relay.shape_of(uop_1246))) # shape=(4, 1, 16)
func_971_call = mod.get_global_var('func_971')
func_976_call = mutated_mod.get_global_var('func_976')
const_1259 = relay.const([8.789014,9.894341,-6.382492,-6.123095,3.158946,2.361849,5.245004,9.049258,-5.000631,-3.662711,-7.042886,9.388307,3.288588,3.737763,-4.364367,2.586465,-4.918504,-8.053799,-2.959450,-5.327192,7.844566,6.195702,1.009853,1.468221,-2.964811,-1.507492,-4.864702,-5.956863,8.576122,-6.222263,-0.816989,-3.417715,2.391580,1.851352,9.886875,3.596197,1.570501,-9.439705,-4.964412,5.370490,2.461977,6.558225,1.928240,9.737407,-6.570410,6.387981,-9.118361,6.112448,-6.588933,0.361646,-0.164182,7.454727,4.453739,-0.596336,3.347297,-3.449978,-9.534015,7.157502,9.804652,-2.809934,-2.404501,-4.957028,0.356078,-5.242085,-2.087032,-0.759740,1.239953,4.819199,7.157730,-2.025694,3.850431,8.928235,-9.812021,5.369185,8.450592,7.911667,1.448979,-8.361562,-5.686793,3.230452,-1.477453,7.800501,6.529407,-2.001432,4.270238,5.261007,-0.093403,-7.584237,1.782566,-1.780592,3.596050,1.362325,-1.854643,-2.367355,-0.948558,6.310948,5.462214,-4.488003,4.473914,4.566566,5.657227,4.714115,1.050030,9.747654,-1.825052,9.822073,4.358494,-1.357003,6.687342,-1.842731,-4.493357,-2.126597,6.883386,-2.836395,-2.579497,5.474852,8.751814,4.000598,-6.218184,2.548668,-5.662192,-7.431168,4.390486,2.445670,7.493538,0.085794,-0.427400,9.962286,-3.928876,-5.286909,4.547525,4.669670,4.603322,1.528722,5.627548,-8.988831,-5.480915,3.507809,1.823321,-7.266497,6.204362,2.432657,7.490466,6.459583,-9.003361,-0.518067,9.697087,-9.919227,-0.986845,-0.040773,9.362867,-5.823969,8.291364,1.336596,-5.317653,-0.437961,7.989899,1.995797,-6.880552,4.725621,1.207721,2.444001,9.462394,5.812057,1.434782,9.729544,-5.259439,-4.322683,1.974615,-8.073120,3.394666,1.631224,-5.025771,-3.598221,1.183784,-9.983150,1.890592,8.604911,7.670635,9.382969,-7.245297,2.468995,-2.260316,6.346781,-8.801770,5.279932,-9.263678,-6.061702,-1.116973,7.020210,-0.856648,-2.775974,9.702703,-2.599047,-9.643301,-3.334446,-9.161375,9.866571,5.879804,9.437363,-0.111253,-6.619279,6.893333,-0.954767,2.431727,-6.078391,5.123001,1.145473,-5.830564,4.279480,2.298776,-7.001980,-2.476810,-0.190061,-4.575029,4.111564,6.410719,5.174952,-6.856051,-4.685013,0.284445,-1.023762,6.116656,-5.539381,4.306770,-1.829551,7.757431,7.541638,-0.838120,8.561795,0.500395,3.271719,-1.492551,2.775575,-1.682991,-8.009533,-8.352466,-0.011074,9.779952,-2.630953,3.220519,1.100604,7.500695,-4.562072,3.857803,-7.681323,-5.684034,1.064500,-5.678765,2.901359,-9.619547,-9.347807,-2.945971,-3.773474,0.227717,5.990248,4.022786,9.701866,8.777891,-3.874112,-3.363355,2.490253,-8.771025,7.074882,7.279361,-3.837755,1.976543,8.214693,6.932276,8.650172,-6.453860,5.438028,6.000816,-6.255255,-4.021324,2.256002,1.555412,4.793050,3.707617,-3.828851,-6.636709,-7.323377,3.485780,0.900836,4.680147,-0.010933,2.606083,3.391460,-0.715817,9.843931,-9.916224,3.763071,8.148044,-4.193259,-8.482583,-4.899063,2.777254,-9.429150,-2.595198,4.929129,-3.926074,8.095857,-6.102407,-6.537944,-7.576950,5.330139,7.647323,-4.939246,-7.184886,1.805316,4.441347,1.251922,2.677771,8.860976,1.775106,2.985889,-6.123782,-6.792253,-5.663261,-2.324484,-0.078069,7.386758,-5.282823,8.487448,-5.449175,8.318120,-9.617384,-7.608369,-4.159853,6.815540,9.880649,8.555816,8.017028,-6.561746,9.237016,-1.422917,-9.113649,1.349302,4.866091,4.303824,1.629765,0.424190,4.158124,3.162291,6.943376,-5.774884,-0.384146,3.364962,8.014725,5.176353,-6.418654,-2.953190,8.744425,3.412765,-2.055455,8.587868,-2.878739,2.954951,-3.954375,3.357982,6.328981,-7.383216,-3.312660,3.250640,1.410851,-5.277149,-6.816358,9.905016,-6.774847,-8.527269,3.274881,-4.620942,-7.525333,-8.989861,0.301893,5.593828,2.765189,-8.828900,8.396474,1.035157,-1.123996,-3.943524,-0.352617,-7.560858,-4.884038,-7.969677,-1.597552,5.900067,-9.745645,-6.039941,-4.886842,4.532591,2.691299,9.962639,0.959742,-3.620962,-7.746005,4.591922,-3.783012,8.210537,-6.560055,-6.395764,-0.821662,-9.848237,8.845292,-8.373615,-8.352454,5.127401,4.692854,-0.329417,5.704958,-9.836694,7.258989,1.049530,-3.783180,-0.860183,-0.042245,9.833984,6.507264,4.473404,-0.937449,-8.819497,4.934525,2.912739,-8.173661,-0.292649,-6.975713,0.312545,-9.611892,2.831240,1.733509,1.744129,-7.114833,-0.018268,-6.909853,0.930789,-3.979601,5.848779,9.080567,-8.434324,-7.111314,-9.632653,-4.575381,-5.424519,-9.844618,4.654872,-2.683123,4.792161,4.981868,-8.895163,9.948281,5.923473,8.365068,-9.819791,1.169491,-9.920733,4.690677,-0.338341,-3.640370,-8.509495,-8.175081,-2.171875,-8.396049,4.247434,4.488080,-9.493822,2.372999,-3.124532,-9.286545,-6.704764,-7.194082,-2.328477,6.124829,3.984526,6.503994,-7.691530,8.673614,-5.273548,-9.503051,4.059763,1.679098,-5.129075,4.828158,1.998327,5.305892,1.002919,-2.852465,6.629519,-8.367009,0.639118], dtype = "float32")#candidate|1259|(490,)|const|float32
var_1260 = relay.var("var_1260", dtype = "float64", shape = (312,))#candidate|1260|(312,)|var|float64
call_1258 = relay.TupleGetItem(func_971_call(relay.reshape(const_1259.astype('float32'), [490,]), relay.reshape(var_1260.astype('float64'), [2, 12, 13]), relay.reshape(const_1259.astype('float32'), [7, 10, 7]), ), 3)
call_1261 = relay.TupleGetItem(func_976_call(relay.reshape(const_1259.astype('float32'), [490,]), relay.reshape(var_1260.astype('float64'), [2, 12, 13]), relay.reshape(const_1259.astype('float32'), [7, 10, 7]), ), 3)
bop_1263 = relay.logical_or(uop_1246.astype('bool'), relay.reshape(uop_1225.astype('bool'), relay.shape_of(uop_1246))) # shape=(4, 1, 16)
bop_1266 = relay.bitwise_and(uop_1225.astype('uint16'), relay.reshape(bop_1248.astype('uint16'), relay.shape_of(uop_1225))) # shape=(4, 1, 16)
output = relay.Tuple([call_1233,const_1234,call_1243,call_1258,const_1259,var_1260,bop_1263,bop_1266,])
output2 = relay.Tuple([call_1235,const_1234,call_1244,call_1261,const_1259,var_1260,bop_1263,bop_1266,])
func_1271 = relay.Function([var_1224,var_1260,], output)
mod['func_1271'] = func_1271
mod = relay.transform.InferType()(mod)
mutated_mod['func_1271'] = func_1271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1271_call = mutated_mod.get_global_var('func_1271')
var_1273 = relay.var("var_1273", dtype = "float64", shape = (4, 1, 16))#candidate|1273|(4, 1, 16)|var|float64
var_1274 = relay.var("var_1274", dtype = "float64", shape = (312,))#candidate|1274|(312,)|var|float64
call_1272 = func_1271_call(var_1273,var_1274,)
output = call_1272
func_1275 = relay.Function([var_1273,var_1274,], output)
mutated_mod['func_1275'] = func_1275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_1302 = func_1023_call()
call_1303 = func_1023_call()
var_1306 = relay.var("var_1306", dtype = "bool", shape = (2, 12, 13))#candidate|1306|(2, 12, 13)|var|bool
bop_1307 = relay.less(call_1302.astype('bool'), relay.reshape(var_1306.astype('bool'), relay.shape_of(call_1302))) # shape=(2, 12, 13)
bop_1310 = relay.less(call_1303.astype('bool'), relay.reshape(var_1306.astype('bool'), relay.shape_of(call_1303))) # shape=(2, 12, 13)
output = relay.Tuple([bop_1307,])
output2 = relay.Tuple([bop_1310,])
func_1316 = relay.Function([var_1306,], output)
mod['func_1316'] = func_1316
mod = relay.transform.InferType()(mod)
mutated_mod['func_1316'] = func_1316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1317 = relay.var("var_1317", dtype = "bool", shape = (2, 12, 13))#candidate|1317|(2, 12, 13)|var|bool
func_1316_call = mutated_mod.get_global_var('func_1316')
call_1318 = func_1316_call(var_1317)
output = call_1318
func_1319 = relay.Function([var_1317], output)
mutated_mod['func_1319'] = func_1319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_1326 = relay.TupleGetItem(func_1088_call(), 0)
call_1327 = relay.TupleGetItem(func_1090_call(), 0)
func_689_call = mod.get_global_var('func_689')
func_691_call = mutated_mod.get_global_var('func_691')
var_1335 = relay.var("var_1335", dtype = "float32", shape = (490,))#candidate|1335|(490,)|var|float32
call_1334 = relay.TupleGetItem(func_689_call(relay.reshape(var_1335.astype('float32'), [7, 10, 7])), 0)
call_1336 = relay.TupleGetItem(func_691_call(relay.reshape(var_1335.astype('float32'), [7, 10, 7])), 0)
output = relay.Tuple([call_1326,call_1334,var_1335,])
output2 = relay.Tuple([call_1327,call_1336,var_1335,])
func_1340 = relay.Function([var_1335,], output)
mod['func_1340'] = func_1340
mod = relay.transform.InferType()(mod)
var_1341 = relay.var("var_1341", dtype = "float32", shape = (490,))#candidate|1341|(490,)|var|float32
output = func_1340(var_1341)
func_1342 = relay.Function([var_1341], output)
mutated_mod['func_1342'] = func_1342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_1440 = func_634_call()
call_1441 = func_634_call()
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_1444 = func_1023_call()
call_1445 = func_1023_call()
output = relay.Tuple([call_1440,call_1444,])
output2 = relay.Tuple([call_1441,call_1445,])
func_1448 = relay.Function([], output)
mod['func_1448'] = func_1448
mod = relay.transform.InferType()(mod)
output = func_1448()
func_1449 = relay.Function([], output)
mutated_mod['func_1449'] = func_1449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_1456 = func_1023_call()
call_1457 = func_1023_call()
output = call_1456
output2 = call_1457
func_1459 = relay.Function([], output)
mod['func_1459'] = func_1459
mod = relay.transform.InferType()(mod)
mutated_mod['func_1459'] = func_1459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1459_call = mutated_mod.get_global_var('func_1459')
call_1460 = func_1459_call()
output = call_1460
func_1461 = relay.Function([], output)
mutated_mod['func_1461'] = func_1461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_1475 = func_1023_call()
call_1476 = func_1023_call()
var_1501 = relay.var("var_1501", dtype = "bool", shape = (2, 12, 13))#candidate|1501|(2, 12, 13)|var|bool
bop_1502 = relay.maximum(call_1475.astype('float32'), relay.reshape(var_1501.astype('float32'), relay.shape_of(call_1475))) # shape=(2, 12, 13)
bop_1505 = relay.maximum(call_1476.astype('float32'), relay.reshape(var_1501.astype('float32'), relay.shape_of(call_1476))) # shape=(2, 12, 13)
var_1506 = relay.var("var_1506", dtype = "bool", shape = (2, 12, 13))#candidate|1506|(2, 12, 13)|var|bool
bop_1507 = relay.bitwise_or(var_1501.astype('int64'), relay.reshape(var_1506.astype('int64'), relay.shape_of(var_1501))) # shape=(2, 12, 13)
uop_1523 = relay.asin(bop_1507.astype('float64')) # shape=(2, 12, 13)
output = relay.Tuple([bop_1502,uop_1523,])
output2 = relay.Tuple([bop_1505,uop_1523,])
func_1530 = relay.Function([var_1501,var_1506,], output)
mod['func_1530'] = func_1530
mod = relay.transform.InferType()(mod)
mutated_mod['func_1530'] = func_1530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1530_call = mutated_mod.get_global_var('func_1530')
var_1532 = relay.var("var_1532", dtype = "bool", shape = (2, 12, 13))#candidate|1532|(2, 12, 13)|var|bool
var_1533 = relay.var("var_1533", dtype = "bool", shape = (2, 12, 13))#candidate|1533|(2, 12, 13)|var|bool
call_1531 = func_1530_call(var_1532,var_1533,)
output = call_1531
func_1534 = relay.Function([var_1532,var_1533,], output)
mutated_mod['func_1534'] = func_1534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1448_call = mod.get_global_var('func_1448')
func_1449_call = mutated_mod.get_global_var('func_1449')
call_1546 = relay.TupleGetItem(func_1448_call(), 0)
call_1547 = relay.TupleGetItem(func_1449_call(), 0)
uop_1550 = relay.sqrt(call_1546.astype('float64')) # shape=(2, 12, 13)
uop_1552 = relay.sqrt(call_1547.astype('float64')) # shape=(2, 12, 13)
func_1530_call = mod.get_global_var('func_1530')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_1564 = relay.TupleGetItem(func_1530_call(relay.reshape(uop_1550.astype('bool'), [2, 12, 13]), relay.reshape(uop_1550.astype('bool'), [2, 12, 13]), ), 1)
call_1565 = relay.TupleGetItem(func_1534_call(relay.reshape(uop_1550.astype('bool'), [2, 12, 13]), relay.reshape(uop_1550.astype('bool'), [2, 12, 13]), ), 1)
func_1530_call = mod.get_global_var('func_1530')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_1567 = relay.TupleGetItem(func_1530_call(relay.reshape(call_1564.astype('bool'), [2, 12, 13]), relay.reshape(call_1546.astype('bool'), [2, 12, 13]), ), 0)
call_1568 = relay.TupleGetItem(func_1534_call(relay.reshape(call_1564.astype('bool'), [2, 12, 13]), relay.reshape(call_1546.astype('bool'), [2, 12, 13]), ), 0)
func_1271_call = mod.get_global_var('func_1271')
func_1275_call = mutated_mod.get_global_var('func_1275')
const_1571 = relay.const([8.366899,4.416499,0.605004,-4.237246,-5.382969,-7.590983,-8.917042,8.841073,-9.468578,9.061604,-8.597992,-8.571186,7.536623,5.812031,1.244751,-8.953028,-4.131903,5.651542,-8.601424,6.024623,-7.869535,6.414368,-6.917404,-0.445739,-5.607034,-2.211032,-8.174625,-0.870821,-4.043471,-4.868649,-0.177919,-7.185808,-3.439061,-9.792873,1.564466,0.885118,8.991976,-3.227538,-1.664974,-4.047666,-4.697518,9.343725,8.799000,-6.638715,-4.261021,2.265122,0.745216,4.863426,-6.784648,4.419494,5.179027,3.987558,7.846712,-2.199701,-0.651189,-0.840554,-0.662686,-9.550565,5.810731,5.759081,5.910348,-6.769987,-5.594172,6.231944], dtype = "float64")#candidate|1571|(64,)|const|float64
call_1570 = relay.TupleGetItem(func_1271_call(relay.reshape(const_1571.astype('float64'), [4, 1, 16]), relay.reshape(call_1546.astype('float64'), [312,]), ), 1)
call_1572 = relay.TupleGetItem(func_1275_call(relay.reshape(const_1571.astype('float64'), [4, 1, 16]), relay.reshape(call_1546.astype('float64'), [312,]), ), 1)
func_584_call = mod.get_global_var('func_584')
func_586_call = mutated_mod.get_global_var('func_586')
const_1574 = relay.const([1.852109,-9.985309,0.657797,2.195283,6.240205,-2.696200,-7.553928,1.196779,-5.606909,0.468814,2.495039,7.983499,7.141197,5.414064,-1.185335,3.540919,-8.841999,9.128342,-4.799106,-8.206882,3.289276,-2.476424,0.411611,-0.690860,-3.944660,2.805034,2.229388,9.442831,-5.908573,9.499019,-1.481024,-6.249400,-0.209424,-8.554192,-1.342200,-5.200454,5.147563,0.867243,1.377098,1.943719,8.176384,1.697776,6.999744,-2.534736,-7.892430,-3.122489,-6.289892,1.247226,0.525846,4.652340,9.339422,8.496772,-7.081525,7.521664,4.817603,-3.965886,-9.405994,5.239707,-5.352399,8.053498,-3.489263,5.997380,-6.060420,0.841507,8.963648,0.997165,3.187008,6.577854,-7.484554,5.097036,7.686452,-9.954481,9.339294,8.877216,8.838540,-6.643999,1.232830,-5.525959,5.355574,6.588524,-6.784244,2.238137,0.093342,-6.030274,5.197637,9.551930,2.675475,-0.968063,-9.175894,-9.306245], dtype = "float64")#candidate|1574|(90,)|const|float64
call_1573 = relay.TupleGetItem(func_584_call(relay.reshape(const_1574.astype('float64'), [2, 15, 3])), 0)
call_1575 = relay.TupleGetItem(func_586_call(relay.reshape(const_1574.astype('float64'), [2, 15, 3])), 0)
func_689_call = mod.get_global_var('func_689')
func_691_call = mutated_mod.get_global_var('func_691')
const_1585 = relay.const([2.346957,-5.416263,-4.719444,-1.243026,-3.364819,4.453898,-0.598279,9.373584,2.861125,-7.909850,1.009914,-3.694252,5.255453,0.970247,5.557303,-2.868314,4.316671,-0.913400,-3.907789,-4.766031,3.298680,-4.107225,7.922366,5.115220,3.235656,-9.301792,4.208449,0.047965,-4.364696,5.201585,-4.507134,4.471818,8.884828,3.977660,-9.586435,-6.662279,4.460779,-4.688141,-4.542006,2.150775,4.095164,-2.441041,0.812692,-3.256923,-5.910363,6.874308,4.891270,-5.096424,-4.548396,-5.012819,8.401526,-4.254834,-9.456779,-1.013291,-2.932395,-3.305599,2.169720,6.839906,-5.733420,3.305159,5.029099,4.599904,4.736035,8.729279,-3.145439,-4.359719,-5.967608,-9.533845,2.559396,1.266246,4.571180,-6.613770,-1.539919,6.386632,8.943243,-5.205472,0.658377,3.748696,6.735516,-9.616610,-1.550929,-9.689184,-4.765527,3.779009,3.787048,1.482901,-0.129008,7.829241,7.991224,9.516439,3.878364,-2.070829,-7.990200,4.330308,-5.252986,3.030465,6.193619,-4.065655,-1.888609,2.626999,-1.208115,-2.133579,-9.447518,-9.095741,-5.478513,-3.183456,9.374664,-5.973293,-5.060349,9.148461,-1.434135,-5.419259,-0.903213,5.937315,-3.824384,-8.946855,2.231048,-7.881472,8.166074,-8.666071,-8.005191,5.364833,9.666110,5.630878,-3.578792,-9.543708,7.317772,-1.181751,5.504009,6.192928,-5.255118,6.922207,-5.888520,-9.249772,-8.849317,-2.884434,3.123059,-3.689839,9.714456,8.951595,-9.378856,-5.343627,-0.876296,-6.634681,-1.442637,4.811439,9.661760,3.908179,-7.772038,9.996845,-1.010176,-8.231920,-8.437006,-6.159272,-8.686745,8.573276,1.401054,1.450555,-5.325515,-3.346726,9.114167,1.100359,-7.192208,-1.173381,-4.831049,4.193989,8.324975,7.174789,-0.519674,-2.924278,9.249315,9.541147,0.423541,-6.741978,-9.282634,9.399250,-2.758452,2.608155,6.844515,-4.749188,7.139873,-1.313176,5.984314,-6.722932,4.795100,-6.096459,-4.034242,2.505835,-8.454034,2.444029,-1.472134,-6.756934,-0.488906,6.383940,-0.089152,3.304750,9.398363,-8.005226,4.321456,-4.454024,8.922423,3.416671,3.128118,-3.538388,-9.051280,-4.495940,-9.081516,-8.780999,-3.776882,-1.456844,7.562346,7.213598,8.622781,2.535328,-6.758392,3.912147,-5.609780,-4.369913,5.214986,-3.892185,-1.494567,7.878840,6.329902,4.848996,3.075986,-7.041212,-0.280456,-1.405677,-2.765596,-5.019301,6.836875,-0.696663,2.385933,9.778194,5.058957,-5.511742,9.674886,-5.011554,0.949977,-5.243148,5.935147,9.365092,-6.689771,9.398135,6.732690,-1.553219,3.991279,3.130158,4.195500,-9.351099,-9.865679,-5.689855,-9.309789,-4.195527,6.433929,-4.010719,-4.842879,-6.871628,7.469897,0.739906,9.029636,-0.317744,-2.812017,0.396408,-2.438099,0.214264,6.116334,-0.538983,-5.241859,4.277910,-0.648611,1.570787,-0.525808,4.235638,6.663568,-4.692335,-3.514724,-3.417717,-4.088053,-0.963258,3.925371,2.614194,-7.384759,-2.950573,6.835878,-7.170908,8.928258,-5.186640,9.003112,-4.090726,-8.352609,3.986784,2.735641,0.430496,-4.777158,-1.279231,3.942268,-2.665437,-1.772691,3.517330,-3.936577,0.099642,9.379271,8.528271,4.886388,5.477340,5.711347,9.903022,-8.971735,-4.114351,-2.624479,-9.971295,7.506133,2.842681,7.186061,5.964292,-1.900871,-7.725895,-5.233505,-1.624207,5.245785,5.388554,8.417311,0.978728,2.683110,-3.012788,-2.061610,-4.956260,4.917045,5.692371,-2.778194,-2.705401,0.418607,-9.055396,9.461263,-9.655297,-6.137775,3.378954,-5.885705,-8.293293,-7.521597,5.228669,2.499326,-9.774226,-1.349010,-8.628356,-0.935561,8.463439,4.227659,6.072547,3.396792,6.191912,1.293683,6.261171,2.881378,-7.515784,-5.710223,-7.513271,6.271313,-5.101568,9.830216,-9.309186,1.326775,1.852901,5.646696,8.016025,-7.281610,-0.284883,7.672793,6.692509,8.177977,8.064695,-4.435276,-2.607024,-6.842979,5.053836,1.618636,-4.785068,0.130137,8.025456,-4.145698,0.989924,5.660803,8.303040,9.611009,3.827968,-5.085516,-5.491924,-9.392536,-7.833869,4.227973,-9.660124,2.425981,-8.429477,7.609112,2.597944,-3.242546,-6.854897,-2.337912,5.655018,0.147872,4.729758,8.407358,-9.188726,-3.357009,-7.575953,-2.046049,-9.421688,7.788400,-9.818899,-1.679446,5.558127,6.957589,-3.240348,2.869603,8.917707,-3.559967,-2.424342,6.806894,5.315176,3.636192,9.866150,0.926403,6.631909,-7.190808,7.946719,6.817394,-6.221550,-0.027894,-5.023530,-4.706237,-4.136489,-9.302059,-0.274000,4.445048,3.236136,8.522860,-0.504249,-1.844274,-5.391543,-6.077277,7.864145,-9.277604,-0.741589,-9.857739,-3.751202,-6.722813,2.753665,3.817440,-8.653045,-7.633006,0.323248,4.126335,-0.617501,0.260875,-2.928433,-3.580989,7.994489,3.537300,5.372853,-3.645964,-6.859378,8.665014,-7.879143,7.115705,8.037741,-7.725837,-6.162675,2.447149,-3.335092,0.032751,-6.575266,-6.300973,-0.020663,4.135783,-5.643148,1.200062,-1.057937,-5.800482,8.984176,-1.590891,4.282278,5.630459,-2.882374,-3.322127,5.237326,9.110642,6.043502,3.263447,-6.569267], dtype = "float32")#candidate|1585|(490,)|const|float32
call_1584 = relay.TupleGetItem(func_689_call(relay.reshape(const_1585.astype('float32'), [7, 10, 7])), 0)
call_1586 = relay.TupleGetItem(func_691_call(relay.reshape(const_1585.astype('float32'), [7, 10, 7])), 0)
func_1116_call = mod.get_global_var('func_1116')
func_1119_call = mutated_mod.get_global_var('func_1119')
var_1600 = relay.var("var_1600", dtype = "int64", shape = (180,))#candidate|1600|(180,)|var|int64
call_1599 = relay.TupleGetItem(func_1116_call(relay.reshape(var_1600.astype('int64'), [10, 3, 6]), relay.reshape(var_1600.astype('int64'), [10, 3, 6]), ), 0)
call_1601 = relay.TupleGetItem(func_1119_call(relay.reshape(var_1600.astype('int64'), [10, 3, 6]), relay.reshape(var_1600.astype('int64'), [10, 3, 6]), ), 0)
output = relay.Tuple([uop_1550,call_1564,call_1567,call_1570,const_1571,call_1573,const_1574,call_1584,const_1585,call_1599,var_1600,])
output2 = relay.Tuple([uop_1552,call_1565,call_1568,call_1572,const_1571,call_1575,const_1574,call_1586,const_1585,call_1601,var_1600,])
func_1602 = relay.Function([var_1600,], output)
mod['func_1602'] = func_1602
mod = relay.transform.InferType()(mod)
var_1603 = relay.var("var_1603", dtype = "int64", shape = (180,))#candidate|1603|(180,)|var|int64
output = func_1602(var_1603)
func_1604 = relay.Function([var_1603], output)
mutated_mod['func_1604'] = func_1604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_1629 = func_1023_call()
call_1630 = func_1023_call()
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_1643 = func_1023_call()
call_1644 = func_1023_call()
output = relay.Tuple([call_1629,call_1643,])
output2 = relay.Tuple([call_1630,call_1644,])
func_1648 = relay.Function([], output)
mod['func_1648'] = func_1648
mod = relay.transform.InferType()(mod)
mutated_mod['func_1648'] = func_1648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1648_call = mutated_mod.get_global_var('func_1648')
call_1649 = func_1648_call()
output = call_1649
func_1650 = relay.Function([], output)
mutated_mod['func_1650'] = func_1650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_1719 = relay.TupleGetItem(func_1088_call(), 0)
call_1720 = relay.TupleGetItem(func_1090_call(), 0)
uop_1722 = relay.exp(call_1719.astype('float64')) # shape=(2, 12, 13)
uop_1724 = relay.exp(call_1720.astype('float64')) # shape=(2, 12, 13)
output = uop_1722
output2 = uop_1724
func_1730 = relay.Function([], output)
mod['func_1730'] = func_1730
mod = relay.transform.InferType()(mod)
mutated_mod['func_1730'] = func_1730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1730_call = mutated_mod.get_global_var('func_1730')
call_1731 = func_1730_call()
output = call_1731
func_1732 = relay.Function([], output)
mutated_mod['func_1732'] = func_1732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_1767 = relay.TupleGetItem(func_1648_call(), 1)
call_1768 = relay.TupleGetItem(func_1650_call(), 1)
const_1775 = relay.const([[[True,True,False,True,False,True,False,False,True,True,True,True,False],[False,False,True,True,True,False,False,True,True,False,True,True,False],[True,True,True,True,False,False,True,False,False,True,False,False,True],[True,True,False,False,True,True,True,False,False,False,False,True,True],[True,True,False,True,True,False,False,False,True,False,True,False,True],[True,False,True,True,True,False,False,False,False,True,True,True,True],[True,True,True,False,True,False,True,True,True,False,True,False,True],[True,False,False,True,True,True,True,False,False,True,False,False,True],[True,True,False,False,False,True,False,True,False,True,True,True,False],[True,False,False,True,True,True,True,True,False,True,False,False,True],[False,True,False,False,False,True,True,False,True,True,True,True,False],[True,False,True,True,True,False,True,True,True,False,False,True,True]],[[False,False,True,False,True,True,True,True,True,True,False,False,True],[False,True,True,True,True,False,False,False,True,True,True,False,False],[False,False,False,True,True,False,True,False,True,True,True,False,False],[False,False,True,False,True,True,True,False,False,False,True,False,True],[False,True,False,True,True,False,True,True,False,True,False,True,True],[True,False,True,True,True,True,True,False,False,True,True,True,True],[True,False,False,False,True,True,True,True,False,True,True,True,False],[True,False,False,True,False,True,True,True,True,False,False,False,False],[False,True,True,False,True,True,False,True,True,True,False,False,False],[False,True,True,False,False,True,False,False,False,False,False,True,True],[True,False,False,True,False,False,True,False,False,False,True,False,True],[False,True,False,False,True,False,False,True,False,False,False,True,False]]], dtype = "bool")#candidate|1775|(2, 12, 13)|const|bool
bop_1776 = relay.greater_equal(call_1767.astype('bool'), relay.reshape(const_1775.astype('bool'), relay.shape_of(call_1767))) # shape=(2, 12, 13)
bop_1779 = relay.greater_equal(call_1768.astype('bool'), relay.reshape(const_1775.astype('bool'), relay.shape_of(call_1768))) # shape=(2, 12, 13)
func_689_call = mod.get_global_var('func_689')
func_691_call = mutated_mod.get_global_var('func_691')
var_1785 = relay.var("var_1785", dtype = "float32", shape = (490,))#candidate|1785|(490,)|var|float32
call_1784 = relay.TupleGetItem(func_689_call(relay.reshape(var_1785.astype('float32'), [7, 10, 7])), 0)
call_1786 = relay.TupleGetItem(func_691_call(relay.reshape(var_1785.astype('float32'), [7, 10, 7])), 0)
bop_1793 = relay.logical_and(call_1784.astype('bool'), relay.reshape(var_1785.astype('bool'), relay.shape_of(call_1784))) # shape=(7, 10, 7)
bop_1796 = relay.logical_and(call_1786.astype('bool'), relay.reshape(var_1785.astype('bool'), relay.shape_of(call_1786))) # shape=(7, 10, 7)
output = relay.Tuple([bop_1776,bop_1793,])
output2 = relay.Tuple([bop_1779,bop_1796,])
func_1807 = relay.Function([var_1785,], output)
mod['func_1807'] = func_1807
mod = relay.transform.InferType()(mod)
var_1808 = relay.var("var_1808", dtype = "float32", shape = (490,))#candidate|1808|(490,)|var|float32
output = func_1807(var_1808)
func_1809 = relay.Function([var_1808], output)
mutated_mod['func_1809'] = func_1809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1819 = relay.var("var_1819", dtype = "float32", shape = (11, 2, 6))#candidate|1819|(11, 2, 6)|var|float32
uop_1820 = relay.sigmoid(var_1819.astype('float32')) # shape=(11, 2, 6)
bop_1825 = relay.right_shift(var_1819.astype('int32'), relay.reshape(uop_1820.astype('int32'), relay.shape_of(var_1819))) # shape=(11, 2, 6)
output = bop_1825
output2 = bop_1825
func_1831 = relay.Function([var_1819,], output)
mod['func_1831'] = func_1831
mod = relay.transform.InferType()(mod)
var_1832 = relay.var("var_1832", dtype = "float32", shape = (11, 2, 6))#candidate|1832|(11, 2, 6)|var|float32
output = func_1831(var_1832)
func_1833 = relay.Function([var_1832], output)
mutated_mod['func_1833'] = func_1833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1730_call = mod.get_global_var('func_1730')
func_1732_call = mutated_mod.get_global_var('func_1732')
call_1840 = func_1730_call()
call_1841 = func_1730_call()
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
var_1843 = relay.var("var_1843", dtype = "uint8", shape = (80,))#candidate|1843|(80,)|var|uint8
call_1842 = relay.TupleGetItem(func_886_call(relay.reshape(var_1843.astype('uint8'), [5, 8, 2])), 1)
call_1844 = relay.TupleGetItem(func_888_call(relay.reshape(var_1843.astype('uint8'), [5, 8, 2])), 1)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_1848 = relay.TupleGetItem(func_886_call(relay.reshape(var_1843.astype('uint8'), [5, 8, 2])), 0)
call_1849 = relay.TupleGetItem(func_888_call(relay.reshape(var_1843.astype('uint8'), [5, 8, 2])), 0)
bop_1857 = relay.not_equal(call_1848.astype('bool'), relay.reshape(call_1842.astype('bool'), relay.shape_of(call_1848))) # shape=(5, 8, 2)
bop_1860 = relay.not_equal(call_1849.astype('bool'), relay.reshape(call_1844.astype('bool'), relay.shape_of(call_1849))) # shape=(5, 8, 2)
output = relay.Tuple([call_1840,var_1843,bop_1857,])
output2 = relay.Tuple([call_1841,var_1843,bop_1860,])
func_1863 = relay.Function([var_1843,], output)
mod['func_1863'] = func_1863
mod = relay.transform.InferType()(mod)
var_1864 = relay.var("var_1864", dtype = "uint8", shape = (80,))#candidate|1864|(80,)|var|uint8
output = func_1863(var_1864)
func_1865 = relay.Function([var_1864], output)
mutated_mod['func_1865'] = func_1865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1448_call = mod.get_global_var('func_1448')
func_1449_call = mutated_mod.get_global_var('func_1449')
call_1900 = relay.TupleGetItem(func_1448_call(), 1)
call_1901 = relay.TupleGetItem(func_1449_call(), 1)
output = call_1900
output2 = call_1901
func_1914 = relay.Function([], output)
mod['func_1914'] = func_1914
mod = relay.transform.InferType()(mod)
output = func_1914()
func_1915 = relay.Function([], output)
mutated_mod['func_1915'] = func_1915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_1930 = relay.TupleGetItem(func_1088_call(), 1)
call_1931 = relay.TupleGetItem(func_1090_call(), 1)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_1948 = func_1023_call()
call_1949 = func_1023_call()
output = relay.Tuple([call_1930,call_1948,])
output2 = relay.Tuple([call_1931,call_1949,])
func_1953 = relay.Function([], output)
mod['func_1953'] = func_1953
mod = relay.transform.InferType()(mod)
output = func_1953()
func_1954 = relay.Function([], output)
mutated_mod['func_1954'] = func_1954
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1975 = relay.var("var_1975", dtype = "int32", shape = (9, 15, 7))#candidate|1975|(9, 15, 7)|var|int32
const_1976 = relay.const([[[-8,-8,-4,-6,-1,-6,8],[-3,8,9,-1,-4,2,-8],[6,1,-6,-10,-10,-1,-7],[-10,-5,-7,10,-4,5,-1],[8,9,1,9,-9,-8,-5],[1,-7,6,6,7,-9,7],[7,-2,1,-2,-9,2,7],[-8,10,-4,-4,1,6,-6],[-8,-1,-2,1,-2,6,3],[-3,7,-3,-3,-5,1,-7],[-5,2,-7,-10,5,2,6],[3,5,10,-7,10,1,-9],[5,-9,-10,-6,5,-3,9],[10,-5,-3,-8,4,-7,7],[2,-8,1,-7,-8,5,-9]],[[6,6,-3,8,1,10,-1],[-2,5,-2,10,10,-4,2],[-6,10,1,5,-6,2,8],[5,-9,8,10,6,-3,9],[9,-9,-6,-6,-6,5,-5],[-1,10,-2,2,2,-10,-2],[-7,2,-4,-2,1,-9,6],[-1,10,-3,10,9,5,-4],[10,-10,8,-6,5,5,3],[-5,8,1,1,-10,1,-3],[-1,-3,-4,1,-7,2,-2],[-9,3,-5,3,-10,-9,-5],[10,-7,6,5,3,10,2],[3,1,8,-10,-4,8,-7],[-6,9,2,-10,-6,-8,10]],[[10,-4,-5,-4,10,7,-7],[9,4,-8,-3,9,-1,-6],[-5,-1,-8,9,-1,-8,9],[4,-2,1,6,1,2,-3],[-6,-3,5,9,8,-7,-10],[-9,-2,-4,4,10,-5,-1],[2,1,3,2,-10,1,8],[-9,5,-5,1,-9,5,6],[4,-10,-1,8,-6,2,-1],[8,-1,8,-6,-2,4,-3],[5,-2,9,7,2,-4,6],[-8,8,-8,4,-6,-1,-9],[-2,-8,4,-5,-2,2,6],[6,-1,10,-2,-8,-4,-9],[3,-4,2,1,1,-8,-6]],[[1,-4,5,3,5,-2,4],[-9,5,-4,-6,-8,-4,-3],[-6,-3,-3,5,-4,-3,-4],[2,-3,2,3,-4,4,-6],[-4,1,7,6,10,-8,-10],[1,-8,-3,-6,-8,10,-7],[-5,-3,3,-9,-5,-2,8],[7,-3,-1,3,-9,-8,-9],[-8,-5,1,-3,1,5,-1],[-10,9,5,8,-10,-2,4],[-7,-10,-9,-1,2,-7,8],[-8,-8,-5,8,8,10,10],[8,-1,7,1,6,-8,-6],[1,6,-2,-10,3,1,-7],[-9,2,-3,6,4,-7,1]],[[-9,10,-2,9,-3,3,8],[-5,-6,4,-6,10,-4,-9],[-3,6,-7,1,-3,3,3],[9,-1,-8,3,-4,-6,8],[9,3,-6,-5,5,2,8],[3,-1,-5,-1,9,5,-10],[8,-3,5,-10,-4,6,10],[-9,-3,-2,-9,7,1,3],[-1,-9,2,5,-7,-10,9],[2,4,-10,6,-1,2,-2],[-6,-9,9,-4,-9,8,-6],[-8,-4,4,2,7,9,-10],[8,4,-8,-8,2,-7,3],[-10,4,3,8,10,-5,-7],[-4,7,-2,5,5,-8,5]],[[1,-1,-8,9,-4,1,7],[10,-2,3,-6,2,5,-5],[6,8,-8,8,-3,7,2],[-1,8,2,-6,9,8,-5],[9,-7,10,2,-6,1,-5],[-9,8,7,3,-6,-2,3],[8,-6,8,4,1,-5,6],[8,-6,-10,9,2,7,-3],[5,-3,-3,-2,2,-10,-1],[10,1,-1,-9,5,10,-1],[5,6,-7,-5,-7,5,4],[-2,10,-4,-4,-10,-10,10],[-2,7,-3,9,1,4,4],[7,5,-5,-3,-8,6,9],[-4,-5,8,-6,-4,-2,-1]],[[-5,6,-3,1,-7,-8,3],[-4,-1,-9,-7,-6,-9,7],[7,8,3,4,-6,-5,-1],[-10,7,7,4,-4,-5,3],[-3,5,-8,-2,8,8,-10],[9,-4,-8,-4,-8,-2,-1],[-3,3,5,-7,-3,-6,4],[-5,7,-8,2,1,-2,4],[3,3,10,-1,-3,1,-7],[5,3,6,5,-10,-1,-2],[-1,-10,-2,10,8,10,-2],[-5,10,-10,3,2,3,4],[-2,-8,-3,-9,1,10,3],[-1,10,3,10,-2,1,-9],[-5,-10,-9,2,-7,10,10]],[[-7,9,7,-6,1,6,-8],[-9,-1,10,-3,-10,-5,-8],[8,5,1,5,-7,-8,6],[-4,-1,1,-9,-5,-4,-7],[-5,3,3,9,6,-3,5],[-3,-5,3,-2,-8,-7,-3],[-10,-9,-7,6,-2,7,-9],[1,10,-2,3,-1,-4,-7],[-5,-2,-5,10,3,4,-3],[3,9,-3,-10,-8,-4,9],[9,7,-8,-9,-9,-3,-6],[-10,-9,-8,-9,-9,-8,1],[5,10,-5,10,-7,4,-9],[-10,7,-4,3,5,5,-10],[-3,6,10,-4,2,-8,-2]],[[-5,-3,-3,-5,7,1,9],[-5,10,9,-6,2,5,5],[-1,8,-5,8,-3,7,10],[-9,-5,-9,4,8,6,3],[4,-7,-2,-10,7,-9,3],[-10,5,4,-6,2,1,-4],[-2,10,-3,-10,3,-4,-7],[1,-10,-3,-10,4,7,8],[7,-5,-6,-6,2,-6,3],[-5,10,10,-7,-4,9,-5],[-3,4,-6,1,-6,3,-3],[4,8,10,-7,9,-3,-5],[10,-1,-4,4,-6,3,4],[-1,-6,6,-6,1,7,9],[2,4,-3,-4,-10,8,7]]], dtype = "int32")#candidate|1976|(9, 15, 7)|const|int32
bop_1977 = relay.greater(var_1975.astype('bool'), relay.reshape(const_1976.astype('bool'), relay.shape_of(var_1975))) # shape=(9, 15, 7)
output = bop_1977
output2 = bop_1977
func_1983 = relay.Function([var_1975,], output)
mod['func_1983'] = func_1983
mod = relay.transform.InferType()(mod)
var_1984 = relay.var("var_1984", dtype = "int32", shape = (9, 15, 7))#candidate|1984|(9, 15, 7)|var|int32
output = func_1983(var_1984)
func_1985 = relay.Function([var_1984], output)
mutated_mod['func_1985'] = func_1985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_2064 = relay.TupleGetItem(func_1088_call(), 2)
call_2065 = relay.TupleGetItem(func_1090_call(), 2)
output = call_2064
output2 = call_2065
func_2082 = relay.Function([], output)
mod['func_2082'] = func_2082
mod = relay.transform.InferType()(mod)
output = func_2082()
func_2083 = relay.Function([], output)
mutated_mod['func_2083'] = func_2083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1459_call = mod.get_global_var('func_1459')
func_1461_call = mutated_mod.get_global_var('func_1461')
call_2104 = func_1459_call()
call_2105 = func_1459_call()
output = relay.Tuple([call_2104,])
output2 = relay.Tuple([call_2105,])
func_2108 = relay.Function([], output)
mod['func_2108'] = func_2108
mod = relay.transform.InferType()(mod)
mutated_mod['func_2108'] = func_2108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2108_call = mutated_mod.get_global_var('func_2108')
call_2109 = func_2108_call()
output = call_2109
func_2110 = relay.Function([], output)
mutated_mod['func_2110'] = func_2110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2122 = func_1914_call()
call_2123 = func_1914_call()
uop_2136 = relay.acos(call_2122.astype('float64')) # shape=(2, 12, 13)
uop_2138 = relay.acos(call_2123.astype('float64')) # shape=(2, 12, 13)
bop_2141 = relay.floor_mod(uop_2136.astype('float64'), relay.reshape(call_2122.astype('float64'), relay.shape_of(uop_2136))) # shape=(2, 12, 13)
bop_2144 = relay.floor_mod(uop_2138.astype('float64'), relay.reshape(call_2123.astype('float64'), relay.shape_of(uop_2138))) # shape=(2, 12, 13)
var_2145 = relay.var("var_2145", dtype = "float64", shape = (2, 12, 13))#candidate|2145|(2, 12, 13)|var|float64
bop_2146 = relay.mod(bop_2141.astype('float64'), relay.reshape(var_2145.astype('float64'), relay.shape_of(bop_2141))) # shape=(2, 12, 13)
bop_2149 = relay.mod(bop_2144.astype('float64'), relay.reshape(var_2145.astype('float64'), relay.shape_of(bop_2144))) # shape=(2, 12, 13)
func_1530_call = mod.get_global_var('func_1530')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_2155 = relay.TupleGetItem(func_1530_call(relay.reshape(var_2145.astype('bool'), [2, 12, 13]), relay.reshape(bop_2141.astype('bool'), [2, 12, 13]), ), 1)
call_2156 = relay.TupleGetItem(func_1534_call(relay.reshape(var_2145.astype('bool'), [2, 12, 13]), relay.reshape(bop_2141.astype('bool'), [2, 12, 13]), ), 1)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_2174 = func_1023_call()
call_2175 = func_1023_call()
output = relay.Tuple([bop_2146,call_2155,call_2174,])
output2 = relay.Tuple([bop_2149,call_2156,call_2175,])
func_2198 = relay.Function([var_2145,], output)
mod['func_2198'] = func_2198
mod = relay.transform.InferType()(mod)
var_2199 = relay.var("var_2199", dtype = "float64", shape = (2, 12, 13))#candidate|2199|(2, 12, 13)|var|float64
output = func_2198(var_2199)
func_2200 = relay.Function([var_2199], output)
mutated_mod['func_2200'] = func_2200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1448_call = mod.get_global_var('func_1448')
func_1449_call = mutated_mod.get_global_var('func_1449')
call_2208 = relay.TupleGetItem(func_1448_call(), 0)
call_2209 = relay.TupleGetItem(func_1449_call(), 0)
output = call_2208
output2 = call_2209
func_2210 = relay.Function([], output)
mod['func_2210'] = func_2210
mod = relay.transform.InferType()(mod)
output = func_2210()
func_2211 = relay.Function([], output)
mutated_mod['func_2211'] = func_2211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_2268 = func_1023_call()
call_2269 = func_1023_call()
func_2082_call = mod.get_global_var('func_2082')
func_2083_call = mutated_mod.get_global_var('func_2083')
call_2273 = func_2082_call()
call_2274 = func_2082_call()
func_1953_call = mod.get_global_var('func_1953')
func_1954_call = mutated_mod.get_global_var('func_1954')
call_2275 = relay.TupleGetItem(func_1953_call(), 1)
call_2276 = relay.TupleGetItem(func_1954_call(), 1)
output = relay.Tuple([call_2268,call_2273,call_2275,])
output2 = relay.Tuple([call_2269,call_2274,call_2276,])
func_2277 = relay.Function([], output)
mod['func_2277'] = func_2277
mod = relay.transform.InferType()(mod)
output = func_2277()
func_2278 = relay.Function([], output)
mutated_mod['func_2278'] = func_2278
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2341 = relay.var("var_2341", dtype = "float32", shape = (16, 2, 14))#candidate|2341|(16, 2, 14)|var|float32
uop_2342 = relay.cosh(var_2341.astype('float32')) # shape=(16, 2, 14)
output = relay.Tuple([uop_2342,])
output2 = relay.Tuple([uop_2342,])
func_2346 = relay.Function([var_2341,], output)
mod['func_2346'] = func_2346
mod = relay.transform.InferType()(mod)
var_2347 = relay.var("var_2347", dtype = "float32", shape = (16, 2, 14))#candidate|2347|(16, 2, 14)|var|float32
output = func_2346(var_2347)
func_2348 = relay.Function([var_2347], output)
mutated_mod['func_2348'] = func_2348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_2360 = func_634_call()
call_2361 = func_634_call()
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_2376 = relay.TupleGetItem(func_1088_call(), 1)
call_2377 = relay.TupleGetItem(func_1090_call(), 1)
output = relay.Tuple([call_2360,call_2376,])
output2 = relay.Tuple([call_2361,call_2377,])
func_2378 = relay.Function([], output)
mod['func_2378'] = func_2378
mod = relay.transform.InferType()(mod)
mutated_mod['func_2378'] = func_2378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2378_call = mutated_mod.get_global_var('func_2378')
call_2379 = func_2378_call()
output = call_2379
func_2380 = relay.Function([], output)
mutated_mod['func_2380'] = func_2380
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2387 = relay.var("var_2387", dtype = "float64", shape = (4, 5, 8))#candidate|2387|(4, 5, 8)|var|float64
uop_2388 = relay.log(var_2387.astype('float64')) # shape=(4, 5, 8)
uop_2395 = relay.atan(uop_2388.astype('float64')) # shape=(4, 5, 8)
bop_2407 = relay.greater_equal(uop_2395.astype('bool'), relay.reshape(var_2387.astype('bool'), relay.shape_of(uop_2395))) # shape=(4, 5, 8)
output = relay.Tuple([bop_2407,])
output2 = relay.Tuple([bop_2407,])
func_2415 = relay.Function([var_2387,], output)
mod['func_2415'] = func_2415
mod = relay.transform.InferType()(mod)
mutated_mod['func_2415'] = func_2415
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2416 = relay.var("var_2416", dtype = "float64", shape = (4, 5, 8))#candidate|2416|(4, 5, 8)|var|float64
func_2415_call = mutated_mod.get_global_var('func_2415')
call_2417 = func_2415_call(var_2416)
output = call_2417
func_2418 = relay.Function([var_2416], output)
mutated_mod['func_2418'] = func_2418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2423 = func_1914_call()
call_2424 = func_1914_call()
func_2277_call = mod.get_global_var('func_2277')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_2429 = relay.TupleGetItem(func_2277_call(), 1)
call_2430 = relay.TupleGetItem(func_2278_call(), 1)
output = relay.Tuple([call_2423,call_2429,])
output2 = relay.Tuple([call_2424,call_2430,])
func_2438 = relay.Function([], output)
mod['func_2438'] = func_2438
mod = relay.transform.InferType()(mod)
output = func_2438()
func_2439 = relay.Function([], output)
mutated_mod['func_2439'] = func_2439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1459_call = mod.get_global_var('func_1459')
func_1461_call = mutated_mod.get_global_var('func_1461')
call_2454 = func_1459_call()
call_2455 = func_1459_call()
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_2460 = func_634_call()
call_2461 = func_634_call()
func_1459_call = mod.get_global_var('func_1459')
func_1461_call = mutated_mod.get_global_var('func_1461')
call_2463 = func_1459_call()
call_2464 = func_1459_call()
bop_2477 = relay.equal(call_2460.astype('bool'), relay.reshape(call_2463.astype('bool'), relay.shape_of(call_2460))) # shape=(2, 12, 13)
bop_2480 = relay.equal(call_2461.astype('bool'), relay.reshape(call_2464.astype('bool'), relay.shape_of(call_2461))) # shape=(2, 12, 13)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_2487 = relay.TupleGetItem(func_1088_call(), 0)
call_2488 = relay.TupleGetItem(func_1090_call(), 0)
func_785_call = mod.get_global_var('func_785')
func_789_call = mutated_mod.get_global_var('func_789')
var_2490 = relay.var("var_2490", dtype = "int64", shape = ())#candidate|2490|()|var|int64
const_2491 = relay.const([8,3,10,-2,7,9,-7,-3,5,7,8,10,-4,1,-5,-3,4,-1,-9,3,9,8,-2,3,8,1,-5,9,6,-1,8,-6,-3,9,7,10,5,4,-8,5,6,-3,8,2,1,7,-9,-2,-9,4,4,-2,9,-6,-2,2,-8,-8,-8,4,-6,-1,-5,7,5,-8,3,-5,7,-1,6,-6,10,-3,-8,8,-10,-1,1,7,-9,-2,-6,-9,2,-3,-3,3,4,-2,4,8,-8,-9,7,4,2,10,-6,-10,-7,7,3,-5,-7,-9,6,3,6,-4,7,-1,-7,6,10,-2,-10,-8,10,-9,-10,-5,8,2,-1,7,4,6,8,5,-9,-6,-7,-1,-10,3,9,-8,-10,-10,-5,-9,-6,-10,-9,4,-3,7,7,-10,-6,-4,-3,-3,3,3,2,-6,-9,3,-5,-3,9,10,-8,10,-5,1,9,10,5,9,-5,6,-5,-1,-7,-9,-6,2,-1,-8,-9,4,-10,9,10,-5,-4,1,1,8,-6,-4,-7,-6,9,5,-2,-7,3,-2,-3,-10,-7,6,10,-5,2,1,-8,-6,-1,-6,-9,-7,-8,-7,-5,1,5,9,-3,6,-6,5,-3,2,1,9,2,6,5,4,-10,2,-10,5,-5,-1,7,4,4,-6,-7,-8,-10,-10,8,5,-7,-7,7,-2,-2,-5,6,9,-7,-8,-9,-3,1,-6,-7,8,9,3,-7,10,8,8,-5,8,3,8,2,-3,-5,1,1,6,-5,9,3,-3,7,7,-10,5,8,-5,5,5,-8,-3,-6,-2,7,-2,1,1,7,-9,2,-2,9,3,7,5,-4,4,-9,-10,-8,-9,10,-8,-2,5,2,4,-7,5,-5,-7,1,9,-10,10,-3,-8,1,-1,-2,6,-6,-5,-7,4,1,3,7,-3,10,6,2,-8,9,-7,6,6,4,-6,2,-7,3,6,-1,-8,2,-6,-7,7,-4,8,-8,3,-8,4,-8,4,10,-3,8,-2,3,-3,2,6,-6,5,1,-9,6,-10,4,-8,-3,-5,-2,1,7,-8,6,5], dtype = "int64")#candidate|2491|(396,)|const|int64
call_2489 = relay.TupleGetItem(func_785_call(relay.reshape(var_2490.astype('int64'), []), relay.reshape(const_2491.astype('int64'), [6, 6, 11]), ), 0)
call_2492 = relay.TupleGetItem(func_789_call(relay.reshape(var_2490.astype('int64'), []), relay.reshape(const_2491.astype('int64'), [6, 6, 11]), ), 0)
const_2496 = relay.const([[[-7.124348,-7.936120,2.713654],[-1.146297,-9.777590,4.384141],[7.564785,5.350181,-8.167363],[-0.892431,-3.644504,-2.001121],[-6.859465,6.649971,0.757027],[6.286285,2.291080,-2.371168],[4.829226,4.819605,-8.852195],[-1.064950,9.871725,-0.946459],[3.661489,-2.021540,-7.352831],[3.900624,-3.945002,-4.105255],[-4.671356,8.218166,-8.025268],[-5.739376,-4.629386,4.121170],[-7.496538,-1.044378,-9.740109],[2.146100,4.372184,6.676207],[0.126876,5.186207,9.278784]],[[5.705313,2.635583,8.665318],[-4.545501,0.954417,-5.052495],[6.863240,7.211363,-8.405882],[-4.106212,9.442473,3.836069],[-5.829292,-6.421362,-9.483023],[5.418385,3.646025,-2.858652],[-1.738869,-1.444217,-4.288430],[3.971894,0.610188,4.679212],[-3.182906,9.641142,-8.021801],[-8.448589,1.965169,-6.929752],[-8.365892,6.453712,-0.269556],[5.010773,-3.928014,3.725674],[-9.681056,6.736331,9.769862],[5.374654,-3.143943,2.716114],[6.249364,5.849932,-1.009047]]], dtype = "float64")#candidate|2496|(2, 15, 3)|const|float64
bop_2497 = relay.logical_xor(call_2489.astype('int8'), relay.reshape(const_2496.astype('int8'), relay.shape_of(call_2489))) # shape=(2, 15, 3)
bop_2500 = relay.logical_xor(call_2492.astype('int8'), relay.reshape(const_2496.astype('int8'), relay.shape_of(call_2492))) # shape=(2, 15, 3)
func_689_call = mod.get_global_var('func_689')
func_691_call = mutated_mod.get_global_var('func_691')
var_2504 = relay.var("var_2504", dtype = "float32", shape = (490,))#candidate|2504|(490,)|var|float32
call_2503 = relay.TupleGetItem(func_689_call(relay.reshape(var_2504.astype('float32'), [7, 10, 7])), 0)
call_2505 = relay.TupleGetItem(func_691_call(relay.reshape(var_2504.astype('float32'), [7, 10, 7])), 0)
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_2506 = func_634_call()
call_2507 = func_634_call()
bop_2511 = relay.less(const_2491.astype('bool'), var_2490.astype('bool')) # shape=(396,)
output = relay.Tuple([call_2454,bop_2477,call_2487,bop_2497,call_2503,var_2504,call_2506,bop_2511,])
output2 = relay.Tuple([call_2455,bop_2480,call_2488,bop_2500,call_2505,var_2504,call_2507,bop_2511,])
func_2514 = relay.Function([var_2490,var_2504,], output)
mod['func_2514'] = func_2514
mod = relay.transform.InferType()(mod)
mutated_mod['func_2514'] = func_2514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2514_call = mutated_mod.get_global_var('func_2514')
var_2516 = relay.var("var_2516", dtype = "int64", shape = ())#candidate|2516|()|var|int64
var_2517 = relay.var("var_2517", dtype = "float32", shape = (490,))#candidate|2517|(490,)|var|float32
call_2515 = func_2514_call(var_2516,var_2517,)
output = call_2515
func_2518 = relay.Function([var_2516,var_2517,], output)
mutated_mod['func_2518'] = func_2518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2210_call = mod.get_global_var('func_2210')
func_2211_call = mutated_mod.get_global_var('func_2211')
call_2533 = func_2210_call()
call_2534 = func_2210_call()
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_2535 = func_1023_call()
call_2536 = func_1023_call()
bop_2537 = relay.logical_or(call_2535.astype('bool'), relay.reshape(call_2533.astype('bool'), relay.shape_of(call_2535))) # shape=(2, 12, 13)
bop_2540 = relay.logical_or(call_2536.astype('bool'), relay.reshape(call_2534.astype('bool'), relay.shape_of(call_2536))) # shape=(2, 12, 13)
func_1983_call = mod.get_global_var('func_1983')
func_1985_call = mutated_mod.get_global_var('func_1985')
var_2546 = relay.var("var_2546", dtype = "int32", shape = (945,))#candidate|2546|(945,)|var|int32
call_2545 = func_1983_call(relay.reshape(var_2546.astype('int32'), [9, 15, 7]))
call_2547 = func_1983_call(relay.reshape(var_2546.astype('int32'), [9, 15, 7]))
func_1448_call = mod.get_global_var('func_1448')
func_1449_call = mutated_mod.get_global_var('func_1449')
call_2548 = relay.TupleGetItem(func_1448_call(), 0)
call_2549 = relay.TupleGetItem(func_1449_call(), 0)
const_2559 = relay.const([[[-5.898162,1.870240,7.554897,1.036853,6.840496,-6.915717,-5.543855,9.335750,5.966642,-7.764487,-0.272553,1.999372,-4.037810],[4.520552,0.284667,8.747597,0.481412,-9.310609,6.196799,-0.262697,-4.483435,2.583715,3.680586,-3.419380,8.076447,0.204205],[-4.321853,3.153694,-4.571879,-1.233011,-3.805808,4.035493,-2.509789,-9.249948,7.180950,-0.129638,-7.352784,-8.456744,-9.927639],[-4.085114,-7.516040,0.357286,-8.819979,1.926116,1.010730,-6.231510,0.892404,4.710674,2.390033,-1.278275,7.558745,-6.280925],[-0.320383,3.952981,2.045172,3.072701,-9.977126,-6.957737,4.661697,1.076342,8.201201,-4.660239,7.054423,-1.473891,-4.566529],[-4.669235,4.666385,8.876684,0.493788,1.663137,-7.616784,-4.617431,3.703897,8.799815,-5.085341,-2.091487,-9.207727,9.647707],[-9.986664,-1.053767,-4.752701,-8.728697,7.102767,0.124053,1.892791,1.323428,3.537211,-8.801369,-2.953651,-2.058311,-4.269250],[-7.253089,7.015423,-3.907204,5.759506,-7.407850,8.331130,5.461314,-8.059159,-6.183036,5.297363,5.046320,5.070016,-1.634376],[3.172115,7.292864,3.624823,-2.216975,5.532091,-5.124942,1.302583,-6.957789,-7.218169,5.252101,-0.094057,-6.257826,3.669262],[9.690563,3.823605,-9.693341,-6.765530,-9.483251,3.425361,-5.821929,9.961930,5.625516,-0.746784,-3.970298,-7.460346,1.741982],[6.257183,-1.528964,-9.196060,7.088875,0.971165,-7.659890,0.126119,1.139270,-7.120517,2.209523,8.488379,-9.550789,-9.283721],[-7.154578,4.554303,-6.364192,7.109449,5.611747,-1.044601,1.779627,8.737015,2.170515,-2.803607,6.173669,-3.899586,-4.018058]],[[-1.446605,1.634362,7.726408,5.605416,-0.004907,5.007765,-3.758484,0.904487,-9.587499,2.804510,-8.235289,-8.195670,0.183051],[8.118059,3.389679,3.734411,1.951666,-4.553502,-0.808570,2.038421,5.732542,-4.988741,7.376559,-5.914641,-1.353613,2.573735],[-8.691002,5.524322,-5.735579,-5.818014,9.891191,6.828644,-1.533779,0.672841,7.225080,2.929231,-8.079834,-9.119261,0.992704],[2.323949,-3.934748,9.426273,-6.315770,0.741327,1.758814,-0.622144,5.466510,3.942975,-5.530769,2.064352,3.673261,-7.343208],[-2.756854,-4.309253,-6.610332,-8.796504,-1.447854,0.975404,-8.738426,7.672316,-6.798620,-5.429667,5.624138,-9.972977,7.845414],[8.478822,-7.986430,-9.124046,7.345166,6.619423,-6.926008,-6.414237,0.674343,5.199170,-7.938257,5.118080,3.470890,0.512689],[-4.839355,-4.797492,7.790706,-5.269434,4.781100,-0.049342,9.872072,-4.438695,1.478900,9.937249,3.950117,7.391353,1.776883],[-9.504790,-5.041269,-2.958752,7.012156,-0.589523,-1.584445,5.254246,0.750149,-0.529240,1.633765,-0.896066,-7.344210,8.419247],[9.845726,1.544251,5.500132,6.866413,3.175219,-6.233574,-7.047762,2.178356,-4.201176,-1.490975,1.911101,-1.150989,-9.772278],[9.650801,-2.985669,-9.225870,9.592011,8.374757,9.437604,1.119506,-1.140785,-3.821113,-9.308030,9.924180,-6.418845,0.805256],[7.582641,-2.321534,-2.177651,-4.117778,-3.085062,-7.580435,-0.378020,-4.399946,-5.017415,2.777318,-2.900157,6.898582,3.060240],[6.606914,4.424760,9.864354,-3.596820,-8.493847,-5.026488,-4.948517,6.992147,-2.953334,-3.083970,2.190829,-6.017130,6.968046]]], dtype = "float32")#candidate|2559|(2, 12, 13)|const|float32
bop_2560 = relay.multiply(call_2533.astype('int64'), relay.reshape(const_2559.astype('int64'), relay.shape_of(call_2533))) # shape=(2, 12, 13)
bop_2563 = relay.multiply(call_2534.astype('int64'), relay.reshape(const_2559.astype('int64'), relay.shape_of(call_2534))) # shape=(2, 12, 13)
func_1807_call = mod.get_global_var('func_1807')
func_1809_call = mutated_mod.get_global_var('func_1809')
var_2575 = relay.var("var_2575", dtype = "float32", shape = (490,))#candidate|2575|(490,)|var|float32
call_2574 = relay.TupleGetItem(func_1807_call(relay.reshape(var_2575.astype('float32'), [490,])), 1)
call_2576 = relay.TupleGetItem(func_1809_call(relay.reshape(var_2575.astype('float32'), [490,])), 1)
func_1530_call = mod.get_global_var('func_1530')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_2578 = relay.TupleGetItem(func_1530_call(relay.reshape(call_2535.astype('bool'), [2, 12, 13]), relay.reshape(call_2548.astype('bool'), [2, 12, 13]), ), 0)
call_2579 = relay.TupleGetItem(func_1534_call(relay.reshape(call_2535.astype('bool'), [2, 12, 13]), relay.reshape(call_2548.astype('bool'), [2, 12, 13]), ), 0)
var_2581 = relay.var("var_2581", dtype = "float32", shape = (490,))#candidate|2581|(490,)|var|float32
bop_2582 = relay.less(var_2575.astype('bool'), relay.reshape(var_2581.astype('bool'), relay.shape_of(var_2575))) # shape=(490,)
bop_2599 = relay.logical_or(var_2581.astype('bool'), relay.reshape(bop_2582.astype('bool'), relay.shape_of(var_2581))) # shape=(490,)
output = relay.Tuple([bop_2537,call_2545,var_2546,call_2548,bop_2560,call_2574,call_2578,bop_2599,])
output2 = relay.Tuple([bop_2540,call_2547,var_2546,call_2549,bop_2563,call_2576,call_2579,bop_2599,])
func_2607 = relay.Function([var_2546,var_2575,var_2581,], output)
mod['func_2607'] = func_2607
mod = relay.transform.InferType()(mod)
var_2608 = relay.var("var_2608", dtype = "int32", shape = (945,))#candidate|2608|(945,)|var|int32
var_2609 = relay.var("var_2609", dtype = "float32", shape = (490,))#candidate|2609|(490,)|var|float32
var_2610 = relay.var("var_2610", dtype = "float32", shape = (490,))#candidate|2610|(490,)|var|float32
output = func_2607(var_2608,var_2609,var_2610,)
func_2611 = relay.Function([var_2608,var_2609,var_2610,], output)
mutated_mod['func_2611'] = func_2611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1448_call = mod.get_global_var('func_1448')
func_1449_call = mutated_mod.get_global_var('func_1449')
call_2652 = relay.TupleGetItem(func_1448_call(), 1)
call_2653 = relay.TupleGetItem(func_1449_call(), 1)
output = relay.Tuple([call_2652,])
output2 = relay.Tuple([call_2653,])
func_2683 = relay.Function([], output)
mod['func_2683'] = func_2683
mod = relay.transform.InferType()(mod)
mutated_mod['func_2683'] = func_2683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2683_call = mutated_mod.get_global_var('func_2683')
call_2684 = func_2683_call()
output = call_2684
func_2685 = relay.Function([], output)
mutated_mod['func_2685'] = func_2685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2082_call = mod.get_global_var('func_2082')
func_2083_call = mutated_mod.get_global_var('func_2083')
call_2699 = func_2082_call()
call_2700 = func_2082_call()
func_785_call = mod.get_global_var('func_785')
func_789_call = mutated_mod.get_global_var('func_789')
const_2711 = relay.const(7, dtype = "int64")#candidate|2711|()|const|int64
const_2712 = relay.const([[2,-7,5,6,-3,6,4,8,6,-4,8,-8,-3,6,9,-10,-7,1,6,9,-2,7,10,2,3,10,4,-2,3,6,-7,4,-5,5,2,3,8,4,5,-7,-9,-2,3,9,1,9,-6,-1,7,4,-1,-5,-9,10,-2,2,1,4,7,1,3,-5,2,9,5,9,2,-8,3,-7,-4,6,-5,1,-6,-2,-4,-7,5,4,-1,8,8,-6,-4,4,2,-5,-10,10,1,-4,-9,1,-7,5,-9,1,1,-6,10,2,10,10,-6,-8,4,-3,-3,8,9,-5,-10,-6,4,5,4,8,7,-7,-10,-3,7,9,10,9,3,-10,2,4,-1,-2],[8,-10,7,9,2,-2,-6,8,-8,-7,-3,-4,4,1,-8,-2,-10,-9,-10,4,10,1,-5,-4,-8,-6,10,5,9,-1,8,1,-4,7,-1,-7,7,7,-9,-8,1,-9,3,7,10,1,9,-8,-4,-10,7,6,-7,9,5,4,-9,-9,5,-8,-3,-4,1,-7,8,10,5,9,-2,-8,6,-4,-5,1,10,8,6,-6,-4,2,2,-5,-1,-9,-5,-9,-10,-7,-8,8,10,9,-6,3,-10,9,-8,-9,3,1,6,10,-2,3,-7,-6,-7,-3,2,2,-4,3,9,2,-1,-9,-2,7,8,-4,10,-4,-8,1,-6,1,-6,-1,-8,7,5,-10],[-7,-2,4,-1,-9,3,-3,-5,-7,-8,-3,-8,-3,2,-10,-6,-7,1,-6,8,-9,-1,7,-3,4,-7,-10,10,9,1,2,6,6,3,-4,-7,3,-7,-6,5,10,9,-7,3,-8,-7,2,2,-3,-1,-7,1,-6,10,-7,-4,-9,8,1,-3,-6,3,-6,-7,9,7,6,-6,6,-6,3,1,2,-9,3,-6,-6,8,-4,-10,-4,-1,-7,-5,-4,-8,-3,-10,-10,-10,5,-1,-4,1,-7,3,10,-4,-2,9,-1,3,-6,9,-4,-9,4,9,1,6,-3,-9,-4,1,3,-9,7,-10,-9,-8,-9,-3,1,1,-4,-1,-9,-1,5,-6,-1,7]], dtype = "int64")#candidate|2712|(3, 132)|const|int64
call_2710 = relay.TupleGetItem(func_785_call(relay.reshape(const_2711.astype('int64'), []), relay.reshape(const_2712.astype('int64'), [6, 6, 11]), ), 2)
call_2713 = relay.TupleGetItem(func_789_call(relay.reshape(const_2711.astype('int64'), []), relay.reshape(const_2712.astype('int64'), [6, 6, 11]), ), 2)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_2725 = relay.TupleGetItem(func_886_call(relay.reshape(call_2699.astype('uint8'), [5, 8, 2])), 0)
call_2726 = relay.TupleGetItem(func_888_call(relay.reshape(call_2699.astype('uint8'), [5, 8, 2])), 0)
bop_2728 = relay.logical_xor(call_2710.astype('uint64'), relay.reshape(const_2712.astype('uint64'), relay.shape_of(call_2710))) # shape=(6, 6, 11)
bop_2731 = relay.logical_xor(call_2713.astype('uint64'), relay.reshape(const_2712.astype('uint64'), relay.shape_of(call_2713))) # shape=(6, 6, 11)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_2734 = relay.TupleGetItem(func_2683_call(), 0)
call_2735 = relay.TupleGetItem(func_2685_call(), 0)
output = relay.Tuple([call_2699,const_2711,call_2725,bop_2728,call_2734,])
output2 = relay.Tuple([call_2700,const_2711,call_2726,bop_2731,call_2735,])
func_2745 = relay.Function([], output)
mod['func_2745'] = func_2745
mod = relay.transform.InferType()(mod)
output = func_2745()
func_2746 = relay.Function([], output)
mutated_mod['func_2746'] = func_2746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_812_call = mod.get_global_var('func_812')
func_813_call = mutated_mod.get_global_var('func_813')
call_2749 = relay.TupleGetItem(func_812_call(), 0)
call_2750 = relay.TupleGetItem(func_813_call(), 0)
func_1807_call = mod.get_global_var('func_1807')
func_1809_call = mutated_mod.get_global_var('func_1809')
var_2768 = relay.var("var_2768", dtype = "float32", shape = (490,))#candidate|2768|(490,)|var|float32
call_2767 = relay.TupleGetItem(func_1807_call(relay.reshape(var_2768.astype('float32'), [490,])), 1)
call_2769 = relay.TupleGetItem(func_1809_call(relay.reshape(var_2768.astype('float32'), [490,])), 1)
output = relay.Tuple([call_2749,call_2767,var_2768,])
output2 = relay.Tuple([call_2750,call_2769,var_2768,])
func_2773 = relay.Function([var_2768,], output)
mod['func_2773'] = func_2773
mod = relay.transform.InferType()(mod)
var_2774 = relay.var("var_2774", dtype = "float32", shape = (490,))#candidate|2774|(490,)|var|float32
output = func_2773(var_2774)
func_2775 = relay.Function([var_2774], output)
mutated_mod['func_2775'] = func_2775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2833 = func_1914_call()
call_2834 = func_1914_call()
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_2840 = func_634_call()
call_2841 = func_634_call()
output = relay.Tuple([call_2833,call_2840,])
output2 = relay.Tuple([call_2834,call_2841,])
func_2842 = relay.Function([], output)
mod['func_2842'] = func_2842
mod = relay.transform.InferType()(mod)
output = func_2842()
func_2843 = relay.Function([], output)
mutated_mod['func_2843'] = func_2843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_2865 = func_1023_call()
call_2866 = func_1023_call()
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_2869 = relay.TupleGetItem(func_2683_call(), 0)
call_2870 = relay.TupleGetItem(func_2685_call(), 0)
output = relay.Tuple([call_2865,call_2869,])
output2 = relay.Tuple([call_2866,call_2870,])
func_2877 = relay.Function([], output)
mod['func_2877'] = func_2877
mod = relay.transform.InferType()(mod)
mutated_mod['func_2877'] = func_2877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2877_call = mutated_mod.get_global_var('func_2877')
call_2878 = func_2877_call()
output = call_2878
func_2879 = relay.Function([], output)
mutated_mod['func_2879'] = func_2879
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2890 = relay.const([[[-4.464959,7.582457,5.962168,-4.429465,-0.217219,-6.929871],[0.771708,-6.910772,-4.007918,3.476494,3.040972,-9.129919],[6.144887,-6.390627,-5.213004,4.413815,2.875112,-7.054585],[7.647965,5.899319,-9.113174,1.725865,-3.086226,-7.894037],[3.655343,-8.246658,-8.996719,8.676883,1.599992,4.695883],[9.375261,-3.333046,-9.155015,-5.194133,-4.192578,3.234055],[0.401426,-2.433086,-1.484074,-4.965733,5.953589,-6.582943],[4.464049,1.346601,9.023058,2.476436,7.917072,8.788033],[-7.300738,1.401059,-5.618686,4.937245,-9.556657,0.441199],[1.424280,-9.804112,-7.258357,-5.009843,-0.998708,9.059006],[-1.654135,2.022668,-5.595270,3.955656,-8.745524,6.588092],[7.235874,-1.523614,7.719838,3.031068,5.475380,2.959502]],[[-0.695457,-3.853523,6.494958,1.031811,-8.280729,-4.404923],[5.378652,4.047394,-2.863016,-9.859757,-6.240984,9.730382],[-5.240434,-9.331961,-5.541361,-5.116456,3.169851,-2.270254],[-7.528410,-2.521619,-8.614391,9.985723,4.320594,1.387736],[-2.979472,9.757708,-9.669423,-9.397261,2.668711,-3.714574],[-4.518826,3.014844,9.339641,-8.318196,6.974472,-7.216061],[7.789504,8.426593,8.165401,4.380224,1.768971,-9.041777],[5.789588,-0.671052,1.283960,2.347259,0.619621,7.841921],[-8.798804,-7.075968,-5.251457,1.188160,8.190867,-0.155321],[1.112232,-0.512518,1.294126,-8.303782,9.482898,1.896391],[0.750582,-0.978305,3.444132,-6.130116,3.699970,7.568850],[9.830579,-6.294009,-1.679133,4.943656,-4.270323,-6.855650]],[[-3.452196,-2.455349,7.061747,-4.815332,-3.328079,-9.030219],[-5.268253,1.313666,6.826941,-8.468457,6.570755,7.196701],[6.363065,8.822785,-7.591002,8.214935,-7.595389,-5.903503],[-4.870030,8.688332,4.853208,-5.164143,-5.757422,-8.558365],[9.213845,-4.047657,4.194305,-6.681116,8.407966,-4.605397],[1.645199,-4.033503,2.538396,6.345045,-6.337088,8.308133],[-9.157273,2.500055,2.631520,9.669545,-1.017699,-9.446128],[4.723743,5.692190,-4.826905,9.882318,7.079597,-6.484692],[-6.436165,-1.827750,-3.794653,0.993098,-2.434794,3.314622],[-7.292461,-3.045173,-9.978430,-3.154729,4.912643,-0.240786],[9.203472,7.621037,-8.077216,4.911028,7.320910,1.731201],[1.025621,9.351384,0.922646,-1.788742,9.915244,7.429796]],[[2.390744,5.477664,7.138791,-3.678390,3.880444,4.432666],[4.579047,1.367088,0.706213,-9.065244,0.540904,-0.911196],[-6.432904,-5.123928,0.727117,-0.749662,0.395321,8.662817],[9.880766,1.961268,0.443927,-3.217825,6.778591,8.206041],[-4.252572,-5.463290,8.252106,6.039399,8.933201,1.233461],[4.831077,7.200604,-2.390995,5.306782,-9.363951,-2.417444],[4.504879,1.662515,-5.888123,7.191053,-5.401304,-9.566195],[-9.670921,-6.108437,3.840513,-7.597800,3.922417,2.378283],[-0.989268,0.139010,5.523107,-5.470983,9.789071,-6.938061],[8.648068,-6.555517,1.105822,5.149497,-8.409076,5.688226],[-2.700449,-1.803531,7.252022,1.576188,-1.068854,-5.450342],[-6.355398,1.188677,-1.274294,-7.411952,0.531205,-1.098632]],[[5.894717,7.749367,4.723596,-8.341813,-8.198648,6.635813],[-9.347419,-0.564902,2.375063,8.909834,4.708063,3.121837],[-4.125738,0.531295,5.387612,-6.000055,-9.183369,-6.605958],[-5.558046,3.043036,-0.849296,-7.272347,5.609893,2.126579],[2.013898,-9.187185,2.330459,4.827312,5.762593,-7.678841],[-7.809401,-5.380637,-5.963795,-2.523741,7.484047,7.004331],[-1.050151,-8.692625,-6.131279,-6.353371,-9.056763,8.700717],[3.345069,5.205107,8.255407,6.343367,-1.697284,-3.573207],[-6.196357,2.104824,-5.669051,9.389674,-6.494630,-3.753338],[-8.874207,8.258632,-0.342857,-6.400174,3.529121,-7.440742],[1.699920,-9.358044,9.925123,-7.629416,9.720318,8.327531],[0.456733,-8.694605,8.042341,-0.305324,6.433028,-4.515769]],[[-0.412731,1.049678,7.637836,7.672559,4.280844,-2.567953],[-5.280695,0.833364,3.445019,-1.460243,1.128840,-8.110528],[8.190446,-1.800993,-2.284111,-3.916016,-9.190479,-9.974729],[-6.351376,-1.340128,1.462033,-2.610285,-7.732762,9.658431],[6.344982,-6.379381,-0.166144,3.408029,9.443493,9.960616],[-5.716393,6.403060,1.812533,-7.009191,3.234415,-0.646342],[-9.592382,-5.783165,-9.873945,-9.079995,1.584694,-0.274045],[0.813967,-1.855574,-5.050607,5.443266,3.453065,9.506781],[-4.562969,-2.991896,-7.464900,3.677987,-2.256229,6.763505],[1.629304,-7.910535,-5.359596,8.711345,-9.368433,7.190314],[9.753682,0.440791,8.621347,7.267890,8.728518,3.008119],[-2.111125,-1.829340,-9.374384,4.890366,7.470845,4.268040]],[[8.921757,1.832182,-9.756158,-7.479967,7.688439,-9.589804],[-8.870408,9.986837,-4.143586,4.345005,3.563220,6.881117],[-9.796917,8.040531,-7.151864,6.253996,1.876778,2.425720],[4.314517,0.672269,7.502102,4.914756,-1.552316,9.803932],[5.578538,3.081673,-8.636221,9.623678,-5.552365,-1.783389],[3.959501,-3.091996,3.954308,-3.326746,1.827279,4.589903],[3.473864,-6.769336,2.044666,-9.227845,-8.671136,5.900195],[-5.240050,1.982032,-7.348698,3.352557,-2.028881,-7.653360],[2.776938,-1.922268,6.413186,-4.033765,1.071083,-7.571224],[-1.241998,3.132670,-2.504632,-3.945114,3.517457,8.585334],[0.526066,5.494464,-8.625277,2.741780,-7.792692,-3.232465],[-7.596142,6.167706,1.334528,-1.686781,-3.563603,2.230074]],[[3.818945,-4.153132,5.510668,-1.041778,-6.120943,-7.341015],[9.867075,1.641410,-8.585058,7.247217,-8.348241,-9.797510],[-0.637582,3.042727,-4.196923,-7.451613,-4.648157,1.295120],[-3.026850,5.545795,9.041118,-0.316000,0.771356,5.362075],[8.320779,-9.311629,5.132565,-0.643331,-0.285922,-5.537360],[-1.413632,-0.278039,3.971945,-0.324307,9.712130,3.600981],[-5.297211,6.867768,9.538119,6.051844,-9.236241,-5.966794],[-7.329180,2.603867,-8.650311,3.227308,-2.825339,-8.106027],[3.233228,-8.992703,-0.436628,-3.935730,7.413668,-7.241229],[-6.378448,3.564849,-7.230838,-0.465138,-0.428286,9.501944],[1.176124,3.805608,-9.024445,-9.544375,7.282983,-8.749732],[-5.732273,-6.284565,-9.156776,-4.790952,-5.433430,0.970160]],[[4.563770,1.106415,-5.853921,-1.597948,3.494492,8.135606],[0.038663,-6.215105,-4.817777,-4.363572,7.597161,-8.622618],[-3.872791,-8.570738,8.269258,0.454103,0.289001,-9.248401],[6.617137,9.714541,4.200766,-0.881403,-0.693178,7.247561],[0.970980,1.172344,-4.715675,-9.313904,-3.110845,4.059275],[8.174408,-8.261280,8.617360,-7.589631,-2.266687,3.437338],[-8.736462,-3.371569,-8.653305,-9.082920,-0.456137,-2.510883],[3.314817,5.783486,9.928335,2.548112,1.569556,2.193851],[8.592423,1.681244,-6.125678,5.696459,-5.221818,1.012366],[0.893057,-9.197177,-0.909025,-5.842373,8.397981,9.993660],[-1.054079,5.119150,1.591417,-3.286033,-6.852988,-2.387062],[-2.238312,-8.060691,2.496047,-2.787760,8.671822,-9.836224]]], dtype = "float64")#candidate|2890|(9, 12, 6)|const|float64
uop_2891 = relay.erf(const_2890.astype('float64')) # shape=(9, 12, 6)
func_2346_call = mod.get_global_var('func_2346')
func_2348_call = mutated_mod.get_global_var('func_2348')
var_2908 = relay.var("var_2908", dtype = "float32", shape = (448,))#candidate|2908|(448,)|var|float32
call_2907 = relay.TupleGetItem(func_2346_call(relay.reshape(var_2908.astype('float32'), [16, 2, 14])), 0)
call_2909 = relay.TupleGetItem(func_2348_call(relay.reshape(var_2908.astype('float32'), [16, 2, 14])), 0)
uop_2920 = relay.atanh(const_2890.astype('float32')) # shape=(9, 12, 6)
func_1831_call = mod.get_global_var('func_1831')
func_1833_call = mutated_mod.get_global_var('func_1833')
const_2926 = relay.const([[1.506979,-3.199444,4.141614,9.970150],[4.726923,-0.426939,6.492031,7.193643],[-1.220587,4.465669,7.190919,1.703965],[-8.310491,-0.023394,-3.659755,-4.423832],[5.830772,-5.889766,-9.190822,-8.716700],[6.719126,-9.138579,-7.584006,3.474488],[7.573703,6.407193,4.520739,-1.762062],[3.476589,-9.534484,2.037620,7.789254],[8.410477,8.236953,7.760059,-0.348054],[-8.672829,-0.977089,-4.311413,1.740200],[-5.936768,-2.498240,7.847220,2.147561],[8.322056,-7.425236,0.010095,-9.413492],[-9.862847,-8.961708,5.915497,-9.261555],[-0.752756,-1.330712,8.754740,-9.266435],[-1.697322,6.478038,7.316024,5.709936],[-4.604371,5.696542,8.176654,-2.260091],[-7.504414,-3.160122,6.180201,1.603356],[7.736446,-2.329740,-2.491386,-1.050361],[-2.690513,-0.642660,8.233456,-3.444369],[-8.292299,1.170977,9.563815,3.462258],[-5.890054,2.396495,-0.723298,1.976472],[8.861406,-8.635875,-3.693371,-4.623602],[-6.760556,-3.199758,-9.031322,4.723930],[4.703221,5.254950,2.057727,-8.851879],[-1.135717,4.862307,-7.702836,-4.421697],[7.774228,9.654381,6.052294,-1.792215],[6.244760,0.187272,9.826908,-9.778297],[8.724627,-8.396232,-2.749019,2.192843],[-8.068806,8.334845,7.919207,-7.299362],[5.178166,0.442429,-1.246071,-5.834870],[-5.700827,1.497335,2.616860,-7.210462],[5.056827,2.952788,0.219208,-5.087697],[4.616260,9.703403,1.963431,5.441753]], dtype = "float32")#candidate|2926|(33, 4)|const|float32
call_2925 = func_1831_call(relay.reshape(const_2926.astype('float32'), [11, 2, 6]))
call_2927 = func_1831_call(relay.reshape(const_2926.astype('float32'), [11, 2, 6]))
bop_2939 = relay.subtract(call_2925.astype('float64'), relay.reshape(const_2926.astype('float64'), relay.shape_of(call_2925))) # shape=(11, 2, 6)
bop_2942 = relay.subtract(call_2927.astype('float64'), relay.reshape(const_2926.astype('float64'), relay.shape_of(call_2927))) # shape=(11, 2, 6)
func_2773_call = mod.get_global_var('func_2773')
func_2775_call = mutated_mod.get_global_var('func_2775')
const_2948 = relay.const([[-0.259715,0.660160,9.887971,-3.053831,-5.911877,-2.774207,-4.828803,4.687762,-7.255547,-4.784308,5.997051,1.277830,-3.153802,6.117927,5.685423,9.825948,2.328757,5.139014,-1.354354,6.999739,-7.726514,7.979495,9.926013,-4.059638,-0.693551,6.815060,0.188342,0.232329,6.324962,-3.920444,-1.768599,-0.543231,-5.255697,-4.012852,-9.221451,9.985955,-2.070015,4.671589,2.378180,3.491894,9.792930,9.828938,8.329451,-8.839384,8.557224,4.175800,-6.012931,-6.939524,8.494883,9.174837,-3.706601,-6.759536,8.410571,-1.455931,1.489589,2.362159,-1.232054,0.463616,9.179388,-7.245355,-3.510284,-6.812961,-2.354583,-3.599811,3.361774,5.432041,-9.982083,-5.815047,4.999245,7.026936],[-6.791933,3.854914,6.721512,-4.155284,-7.200372,-8.004373,1.081352,-6.220739,6.445274,4.160750,-6.405986,-9.385697,5.993508,1.404192,-3.696476,0.910449,0.242763,6.316376,-2.181977,4.960262,8.604896,9.026256,-3.374517,-6.047647,-7.769100,-8.021311,-4.282495,-9.725755,-6.067608,-5.358631,-9.852479,9.623970,5.309594,-5.328296,4.639134,-9.063360,7.277129,1.263180,3.283628,1.046198,5.633985,1.640817,7.851768,6.586317,1.840076,-9.643456,-7.777830,4.614552,-4.775862,2.464771,7.634726,-8.597596,4.719634,-2.328946,6.370757,6.289389,2.264434,-9.004652,-8.011145,-0.635361,-1.154493,7.541217,2.117196,-3.500831,-9.235561,5.199605,0.019606,5.532599,1.182664,-6.734519],[2.167143,6.519136,-4.701185,7.872825,-9.529760,-0.596919,-4.123695,3.200135,-2.765869,-7.935881,0.925422,-2.302063,8.805865,3.642348,8.954710,-4.598630,9.557558,4.184610,4.856288,-1.217128,8.078453,-7.018869,-2.433615,6.655407,2.779540,-6.045497,9.646429,-8.715495,-5.900557,9.403807,1.394677,-9.705384,1.212851,-8.228365,3.625749,-8.403017,3.716038,-0.204524,-3.915441,-8.008754,6.965731,-4.967130,2.786004,-8.213368,3.622147,4.931414,6.926034,3.872829,2.370944,0.896773,6.255738,7.664255,1.478060,-3.460392,5.975334,8.748085,4.848735,1.865873,-1.678514,-9.248900,5.207806,-4.315283,-5.455617,-7.623076,9.765151,-0.186718,0.237737,4.536464,5.722482,9.122894],[-0.657996,-4.094288,-8.758659,-4.143382,7.086166,-9.936303,-8.501551,0.239589,7.707515,1.818568,7.562909,0.519664,4.334107,1.554111,-4.097083,-4.260181,-9.713864,3.929901,-6.099841,0.399052,-1.397643,5.021927,5.192323,3.451143,-3.429139,4.998560,-1.123367,-1.235647,-1.745666,0.630868,-5.234135,4.094453,-9.805140,-2.533728,4.601931,-0.609478,4.797811,-7.306560,-2.405089,1.507739,-9.636193,-3.771159,5.346051,8.234143,9.167581,1.924887,-5.962211,-6.653825,6.103270,8.614821,-4.241969,-1.326457,8.157395,-0.833971,9.693932,-5.916920,2.225052,-5.521900,-5.113110,-8.063760,-6.754177,6.048030,-1.115417,5.765113,-2.723358,-4.200774,-0.987358,8.833041,-6.668855,9.284137],[9.442415,8.399082,4.931085,-1.007124,6.724543,0.082217,-2.806502,-4.685155,-5.253946,-1.658982,3.986540,4.840727,1.554814,9.333609,2.474734,5.951803,0.718163,7.831618,4.159115,-5.315942,-8.335055,-6.319457,-2.842009,7.851160,7.296085,-1.236455,6.867991,-8.104262,-0.321135,-7.069271,0.582799,-9.694745,-7.727441,7.339515,2.512830,9.288426,2.590282,-7.511581,-4.493793,-7.007495,1.585670,-2.035903,-8.561151,-0.462749,9.907922,-1.341486,-5.074101,2.350919,-5.088272,-4.455513,-3.322541,8.044503,-1.102535,1.265068,-3.009107,-4.499311,-8.012717,-6.333943,8.506698,3.610242,8.795830,0.303484,9.179818,-7.474843,3.580681,1.825222,-8.222789,3.778620,4.138161,-5.198105],[-0.458566,1.687935,8.721292,-8.467837,-5.532067,3.658723,8.045746,-8.586928,4.266077,5.426227,0.988224,-3.120210,9.410692,-1.040938,3.404449,-8.470928,9.766730,-0.452792,2.385308,-8.099540,1.409164,8.205190,-1.129839,4.329434,4.880223,6.142482,1.925205,-4.210241,4.703466,0.223769,4.888413,5.276215,-2.569325,-4.398630,-3.738354,7.428180,-9.456091,-8.496377,-3.372605,2.072117,-9.939888,2.335824,-4.216613,6.145692,-7.508735,-8.452866,-6.391730,5.389489,-5.316608,0.654091,-9.672658,-3.625987,3.723176,2.609448,-2.808239,0.996024,5.396799,-2.549070,6.869623,-4.956433,6.398440,1.362297,-7.247950,-6.436609,-8.301417,5.023260,-2.694920,-2.720508,-5.251077,-4.343678],[-6.667326,-7.234239,-2.139448,8.132125,-6.758932,9.735789,4.127659,4.881198,6.032454,-5.646418,6.120843,-8.015133,4.459615,-2.136765,7.758622,-2.468570,-9.711599,8.577743,7.591495,-0.534523,-3.885632,9.946449,8.993590,7.061123,-4.041356,-4.546992,0.284082,-6.136942,9.139594,5.141105,8.500909,-7.176853,-5.476863,-2.060139,6.394453,6.551576,-4.921374,3.306537,8.928549,7.279248,-1.396839,-9.364867,-1.506709,-0.893982,5.554236,-3.571938,5.087894,-4.615268,1.821445,6.722367,-9.444678,-5.527584,-0.093246,-5.621317,1.067528,9.090150,9.862086,6.335908,-5.100158,-0.876453,9.600787,-5.772056,4.624317,-8.058989,5.013045,4.859082,-0.716220,9.694810,0.171553,5.676189]], dtype = "float32")#candidate|2948|(7, 70)|const|float32
call_2947 = relay.TupleGetItem(func_2773_call(relay.reshape(const_2948.astype('float32'), [490,])), 0)
call_2949 = relay.TupleGetItem(func_2775_call(relay.reshape(const_2948.astype('float32'), [490,])), 0)
output = relay.Tuple([uop_2891,call_2907,var_2908,uop_2920,bop_2939,call_2947,const_2948,])
output2 = relay.Tuple([uop_2891,call_2909,var_2908,uop_2920,bop_2942,call_2949,const_2948,])
func_2950 = relay.Function([var_2908,], output)
mod['func_2950'] = func_2950
mod = relay.transform.InferType()(mod)
var_2951 = relay.var("var_2951", dtype = "float32", shape = (448,))#candidate|2951|(448,)|var|float32
output = func_2950(var_2951)
func_2952 = relay.Function([var_2951], output)
mutated_mod['func_2952'] = func_2952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2082_call = mod.get_global_var('func_2082')
func_2083_call = mutated_mod.get_global_var('func_2083')
call_2981 = func_2082_call()
call_2982 = func_2082_call()
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_2989 = relay.TupleGetItem(func_2683_call(), 0)
call_2990 = relay.TupleGetItem(func_2685_call(), 0)
output = relay.Tuple([call_2981,call_2989,])
output2 = relay.Tuple([call_2982,call_2990,])
func_3002 = relay.Function([], output)
mod['func_3002'] = func_3002
mod = relay.transform.InferType()(mod)
output = func_3002()
func_3003 = relay.Function([], output)
mutated_mod['func_3003'] = func_3003
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3007 = relay.var("var_3007", dtype = "float64", shape = (8, 13, 13))#candidate|3007|(8, 13, 13)|var|float64
uop_3008 = relay.sinh(var_3007.astype('float64')) # shape=(8, 13, 13)
func_2210_call = mod.get_global_var('func_2210')
func_2211_call = mutated_mod.get_global_var('func_2211')
call_3011 = func_2210_call()
call_3012 = func_2210_call()
var_3016 = relay.var("var_3016", dtype = "float64", shape = (8, 13, 13))#candidate|3016|(8, 13, 13)|var|float64
bop_3017 = relay.multiply(uop_3008.astype('int8'), relay.reshape(var_3016.astype('int8'), relay.shape_of(uop_3008))) # shape=(8, 13, 13)
output = relay.Tuple([call_3011,bop_3017,])
output2 = relay.Tuple([call_3012,bop_3017,])
func_3021 = relay.Function([var_3007,var_3016,], output)
mod['func_3021'] = func_3021
mod = relay.transform.InferType()(mod)
var_3022 = relay.var("var_3022", dtype = "float64", shape = (8, 13, 13))#candidate|3022|(8, 13, 13)|var|float64
var_3023 = relay.var("var_3023", dtype = "float64", shape = (8, 13, 13))#candidate|3023|(8, 13, 13)|var|float64
output = func_3021(var_3022,var_3023,)
func_3024 = relay.Function([var_3022,var_3023,], output)
mutated_mod['func_3024'] = func_3024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2378_call = mod.get_global_var('func_2378')
func_2380_call = mutated_mod.get_global_var('func_2380')
call_3032 = relay.TupleGetItem(func_2378_call(), 1)
call_3033 = relay.TupleGetItem(func_2380_call(), 1)
func_971_call = mod.get_global_var('func_971')
func_976_call = mutated_mod.get_global_var('func_976')
const_3035 = relay.const([[-4.661597,9.189595,-8.591241,6.088972,3.315299,4.755632,-9.671311,1.213761,3.556810,-2.173205,5.980999,-1.525893,0.033889,8.085507,-4.570380,6.882595,-9.285232,-7.988680,4.514970,7.877002,-6.419194,0.534521,-7.144117,-2.394996,-6.255844,7.140530,-4.110550,5.822402,9.036142,2.070266,-3.052200,-1.873154,0.195528,-1.130965,-9.068302,-9.771036,-5.139749,-6.289632,-6.396775,-6.536823,7.886741,-0.089266,6.979541,-8.661366,-1.352951,-1.224191,-6.792361,5.696739,2.226180,-7.618055,-2.201604,-7.897869,-3.972281,1.282957,-2.800552,-5.658013,0.402710,1.950401,-5.394231,7.760111,2.847496,9.447101,1.627866,9.214864,-6.191787,-2.209137,-9.928809,3.980807,0.145253,-5.902313],[5.548212,-8.270900,2.241970,1.793697,0.297963,9.227085,3.806661,-4.004740,1.021106,2.753668,2.393180,-4.422095,5.934515,7.880918,-2.669672,-0.107317,-9.732897,-8.209662,-3.619892,8.617057,3.729646,-4.000775,4.581861,3.291989,-0.674495,4.371999,-8.066616,-5.885107,5.105300,2.848679,1.350326,3.593858,-1.800504,8.196171,-3.442060,-4.637505,6.389142,-8.589800,9.041410,-7.010639,-2.126976,9.780613,9.418594,-3.461570,3.351032,4.543531,3.056028,-2.722728,-4.048849,-9.600649,-2.099094,-9.643233,6.271809,8.154251,-9.919706,6.543520,0.694324,-2.821023,-6.551038,6.992371,-9.344329,-9.366266,-7.818751,6.457330,-8.106675,2.885304,-8.857898,8.714214,-9.684748,-8.047311],[-4.794941,1.577014,-7.188325,-0.857495,4.007029,4.774329,-7.594973,0.982200,-0.156432,-9.872843,8.344448,-5.987203,8.822564,9.926527,-4.147206,1.546036,6.687845,-8.066915,-6.889003,-4.045564,-1.772671,9.693294,0.746138,7.641474,0.158408,3.534074,9.714815,-5.765316,2.368344,-5.830803,1.881503,-5.146195,3.257959,-2.001528,0.753059,3.012830,-8.777201,9.538573,9.704298,-0.363848,-8.300104,8.694999,6.293898,-7.865035,-2.034266,-3.643232,-5.413442,-9.434946,7.264796,1.451885,-1.697818,-3.077812,1.202309,-1.026257,3.135034,0.999563,-7.026893,5.765876,-1.942659,-0.283881,3.114061,-2.044770,0.354693,8.815891,-3.776736,-6.271530,8.567671,2.563387,-1.532062,9.900085],[-8.827178,9.742791,-2.978588,-3.153470,-6.206613,6.875849,1.893907,-5.165119,-2.581982,8.908218,-8.928076,0.330298,7.784462,5.898525,4.043933,7.225504,2.473357,-6.036180,3.336672,3.706316,-4.696780,1.064770,-3.443058,-9.154888,2.203678,5.104099,7.317946,3.844285,-4.325759,-5.084293,-2.028043,7.638394,-1.624194,5.500265,3.457022,-0.102286,6.565733,7.984959,8.230740,-5.479942,-0.622660,-6.085622,7.703755,-1.472470,-9.518890,8.064396,-4.904870,1.918508,-2.667386,-9.264152,1.603453,6.196362,8.621682,-0.734866,7.660277,6.981902,0.624744,6.205048,-2.549236,-3.209630,4.096711,7.186617,-4.681518,-5.706680,7.256547,-2.318999,6.532766,1.567665,8.774813,7.207689],[-0.937430,-2.331372,5.836331,-4.111101,8.894472,-5.271804,-2.469885,-4.687486,-6.129209,-6.990685,6.121138,-4.620149,-3.274588,2.921516,-5.266778,-4.980155,-7.949081,-3.581628,8.554004,2.555614,9.055204,3.137417,5.117251,-6.390630,-2.464476,2.414908,-4.476293,0.637219,4.117376,-3.176521,6.577766,-1.881300,1.543134,5.066928,-4.697148,3.052528,2.664167,8.154427,-4.589790,-3.828645,-7.581861,-3.996578,-5.163101,-9.244123,9.544779,8.938388,6.629857,-1.547668,-3.146856,8.861472,-5.365685,-9.942892,6.763929,-1.587461,6.763203,1.420559,-1.074729,-3.534558,4.753829,-7.394495,2.150500,5.104617,5.147467,1.813272,-5.158553,-6.864327,9.696769,-0.180394,6.495582,-9.433536],[1.173610,-9.564994,-1.868105,-5.490041,9.665198,-7.217196,-2.760571,-8.583543,9.024324,1.507327,-5.559534,-1.278942,-8.251739,6.154241,1.030601,7.312623,2.830862,-2.110227,-3.657813,9.964293,2.780791,5.787881,8.924080,1.384532,2.833639,-0.302692,8.927328,-0.427481,7.112307,2.355740,4.454403,-6.817617,-9.311268,-6.541480,7.396182,5.263483,5.534481,0.643607,-5.018231,0.503896,6.010714,0.590011,-6.211452,9.352444,4.430489,-0.376293,5.115556,8.300928,5.885416,-7.678142,8.616983,0.644175,-9.314594,-2.997622,-0.934500,2.429780,0.805943,-6.834239,-5.975673,-2.710666,-1.825579,-5.455112,0.824962,2.131157,-8.207266,3.100474,2.106404,-3.948081,9.681444,-4.000181],[2.114616,-1.523195,5.714133,-4.247702,-7.579918,9.973763,-9.375554,-3.495058,-1.215041,-0.768964,2.658857,-9.808516,0.366802,7.389230,8.435710,-3.647054,0.788509,-1.849352,7.326454,-8.868493,4.826215,-3.076044,4.691661,3.556965,-0.365194,-5.560258,0.529372,5.634506,-4.913481,-3.286766,-5.045891,-5.035761,8.627882,-7.099519,7.963240,-3.929035,7.039005,-7.711285,1.019059,-7.651583,-0.538617,2.554041,8.595129,-5.709238,4.646594,-6.393317,2.467896,4.123096,9.664431,9.332567,-2.752007,2.698569,-2.072117,9.253772,4.184349,9.462661,-2.114097,5.942788,6.223952,6.140961,-6.645481,8.168673,-9.406661,-2.550215,-2.732475,4.212716,7.186189,-4.461905,-2.172403,4.639264]], dtype = "float32")#candidate|3035|(7, 70)|const|float32
const_3036 = relay.const([-5.016157,-5.241705,-0.832955,-1.485043,6.845315,-9.103235,0.355981,7.889577,-6.670214,-4.770353,9.182792,6.148229,-8.291277,5.095943,-9.389323,-8.955929,2.726371,-2.459535,-7.189377,7.783775,-6.261156,-7.291880,-3.523099,-9.405248,-1.009860,4.072424,4.905099,0.907682,3.146682,-3.783411,-9.907620,-5.387401,0.782485,6.030223,-4.115299,3.658228,6.051187,-7.598081,1.599616,-7.314864,5.250667,8.509720,4.932793,9.178614,5.261964,-3.350823,-2.726725,1.177649,4.938309,0.510833,4.414384,4.256312,-6.113042,6.937643,-0.790233,8.792490,0.842213,-9.897231,-2.545367,6.851977,5.193156,2.101412,4.605203,7.429499,0.152414,-1.536615,3.927372,1.526383,1.058151,4.403619,2.140757,6.371144,0.384642,7.665046,7.279859,8.647074,-0.295341,-6.050475,-8.419913,-5.950921,5.254236,-9.428273,-5.110812,-0.632491,-3.580333,9.468245,1.567703,-1.503038,7.753090,-7.286435,7.645739,9.397407,-3.533674,2.499068,-0.821461,-8.396046,-3.541671,-9.722274,1.612565,-6.416696,8.476709,5.123298,-7.695537,9.382419,0.923197,1.239489,-8.547340,-2.082926,-2.405733,1.346405,2.036042,-1.357260,-4.657869,8.503167,-0.261705,-4.493824,8.404888,-0.782388,4.793790,0.699310,6.369245,5.570450,-4.632490,-1.295433,8.328418,4.596844,7.516860,-3.058817,-0.733278,2.962650,0.087691,-4.075844,1.974569,0.227263,0.670794,4.936204,7.730556,-7.323460,-9.603396,-6.797550,-8.893924,1.570687,-1.436818,4.689432,0.876018,7.265224,-6.357449,8.879533,-8.270358,7.201159,-4.121505,-9.331820,2.777674,3.575476,4.386893,-1.583111,6.355838,2.788856,7.928338,-3.021133,-5.111216,-8.632915,-7.615691,-6.615828,-7.525489,-7.003289,3.914981,-3.641626,6.739698,-3.982796,0.990780,-9.984911,-7.744274,-8.528866,-2.350674,-8.806099,-0.516185,-7.032480,0.041214,4.300838,-3.990517,-0.917250,-1.385624,-4.002718,-0.457811,-1.679631,8.617104,-1.729439,9.351238,-2.587377,9.338980,-1.378533,5.855063,-9.324983,0.532510,-1.986433,4.272669,7.254875,6.025936,5.590091,8.891070,9.594049,-2.218472,-6.108221,1.976264,-8.271584,-5.465133,-2.510686,8.946431,-4.137489,4.386270,-5.043878,0.669021,-7.967135,4.995525,-4.490471,-0.874190,-1.240072,9.198397,-8.966538,1.035344,7.183537,7.333118,8.264754,7.843063,9.853517,-2.757071,4.414538,-1.195500,-3.140911,-8.531076,-6.055366,-6.993126,4.048279,2.003435,-5.263775,-0.384692,-1.946325,-4.759881,-7.035645,2.134609,-2.228422,0.358307,3.370485,8.651655,-2.522022,-1.195266,-2.202003,7.817424,-8.871834,5.639692,9.814084,9.535107,1.380708,0.613217,7.741671,-1.679879,-5.549575,7.547357,3.385562,8.048993,-8.824340,-6.483796,-2.296402,2.741258,-6.074398,-9.009556,-3.120593,-5.075422,0.737787,-8.068074,-5.014673,-6.999880,-4.060265,0.980441,-0.980069,3.791201,-6.001487,-3.985964,5.910098,-9.770225,-1.450297,6.269623,-3.764975,0.603697,0.908584,-7.628856,-6.479032,-9.224011,-6.540179,-6.100951,-4.873106,-4.907388,5.666709,-8.053128,-5.487761,-7.870121,1.536606,8.920435,4.613227,5.557778,-9.947996,3.736550,-3.127189,-9.620463,7.471473,0.614788,-4.062179,-4.373187,-2.088523,5.648298,1.805393], dtype = "float64")#candidate|3036|(312,)|const|float64
call_3034 = relay.TupleGetItem(func_971_call(relay.reshape(const_3035.astype('float32'), [490,]), relay.reshape(const_3036.astype('float64'), [2, 12, 13]), relay.reshape(const_3035.astype('float32'), [7, 10, 7]), ), 2)
call_3037 = relay.TupleGetItem(func_976_call(relay.reshape(const_3035.astype('float32'), [490,]), relay.reshape(const_3036.astype('float64'), [2, 12, 13]), relay.reshape(const_3035.astype('float32'), [7, 10, 7]), ), 2)
output = relay.Tuple([call_3032,call_3034,const_3035,const_3036,])
output2 = relay.Tuple([call_3033,call_3037,const_3035,const_3036,])
func_3038 = relay.Function([], output)
mod['func_3038'] = func_3038
mod = relay.transform.InferType()(mod)
output = func_3038()
func_3039 = relay.Function([], output)
mutated_mod['func_3039'] = func_3039
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3057 = relay.const([[[1.534910,9.680195,2.789984],[-8.049827,-6.866738,-2.350358],[-8.889510,-5.130980,2.099701],[3.845549,-3.643874,3.371042],[6.414009,-1.598375,-0.101883],[-7.911505,-2.073413,-0.334954],[-9.642904,8.911559,-8.473045],[-8.815948,8.975295,-4.477408]],[[-3.304077,-9.175457,2.347809],[3.529673,-9.690432,4.197880],[6.895197,-2.089721,5.277415],[0.861780,9.086394,-6.220611],[3.263064,6.858496,3.398376],[7.760790,2.690037,-3.782938],[4.839980,1.529322,4.943717],[1.662707,9.073881,0.265611]],[[-0.612481,-7.419606,5.184519],[1.549484,4.146749,8.771849],[-7.899886,-5.523368,8.370118],[5.319677,-8.324036,-4.765986],[7.380281,0.315911,0.092411],[-2.684778,9.512043,9.582571],[4.596423,8.722497,8.288728],[-8.916738,-6.105578,-0.953097]],[[6.809452,-4.313605,-3.411423],[-8.869146,-9.377271,-5.123738],[-3.540218,-4.066137,6.266539],[-6.585047,-9.458596,6.272530],[8.479249,-7.318611,7.942746],[7.090902,-8.774241,-8.142574],[-0.980003,-0.391684,-3.124183],[-7.109352,9.789696,8.098434]],[[-0.192106,-2.539386,5.108723],[4.802599,0.978958,-1.063234],[-6.526390,2.314082,-8.408139],[8.649077,-7.201700,0.003931],[1.811222,5.746423,-0.130531],[7.201588,4.059379,-0.042555],[-8.290055,4.309148,3.245134],[-5.402628,5.570536,-7.556077]],[[5.339891,-6.001002,0.920988],[6.982255,3.100468,-0.419351],[7.695149,-1.646757,1.547372],[9.266008,-3.607261,7.899788],[4.529632,7.027601,7.311792],[-9.813968,-6.253075,3.559061],[-9.779018,-2.369549,5.470223],[-4.652293,-8.613533,2.992189]],[[4.040617,7.254243,5.624475],[3.859610,-0.422562,9.801061],[-7.928033,0.470875,-8.909891],[-5.708684,4.994515,-1.183416],[7.247904,6.965366,-2.390649],[2.737077,4.392712,0.957285],[7.948326,2.150792,-9.211157],[-2.210926,-4.676874,1.758511]],[[-7.968462,-1.225033,-1.855981],[-7.653087,4.925835,9.331610],[8.758376,6.410333,-3.512625],[6.634251,0.128540,7.681414],[-6.194071,-4.136106,1.604581],[7.619604,4.487601,3.167660],[1.709414,-4.123792,0.515173],[-1.036648,-9.784071,-5.674459]],[[-7.695619,4.289071,-7.360079],[2.512988,-2.940457,-7.132324],[7.513775,4.047267,7.504381],[-6.296853,-1.410664,2.495795],[9.248682,-1.154783,8.077190],[-6.701014,5.337041,7.917516],[-2.377160,-4.165019,-8.597610],[6.942620,-0.120723,-1.162737]],[[4.935410,-6.215906,1.782991],[-7.178296,4.653411,9.159624],[5.509686,3.784678,2.220202],[-4.558111,3.618896,-8.654688],[6.922986,-7.844550,-7.051950],[6.588671,8.912789,8.764877],[5.494961,3.257078,9.748998],[4.808458,-2.222078,4.258597]],[[5.435887,-6.785725,-7.517248],[-9.620031,-7.767964,7.794099],[-1.564889,-2.794086,7.627512],[-3.243029,5.114548,3.278616],[-8.392441,4.515636,7.646340],[-6.882250,1.885755,-5.455659],[8.187145,8.014433,4.374206],[-7.488153,-7.658984,2.770891]],[[3.215690,-9.464637,-4.535621],[2.282071,0.526692,6.211734],[4.659413,2.120764,-0.575297],[-2.383236,8.838823,6.791284],[-3.701877,-0.757377,7.126475],[-4.712840,3.465894,2.605810],[1.143163,9.647486,-1.401998],[1.253272,-4.213810,-5.239324]],[[-1.354090,2.604055,-2.479040],[-5.846558,-3.331074,9.790612],[3.536972,-7.943790,4.805967],[-0.130070,-2.695865,9.662668],[-7.345428,-6.472575,1.105008],[-3.927289,6.965123,2.073472],[-7.733206,8.183252,-0.514832],[-3.621342,-6.984002,1.206016]],[[2.260944,-3.352317,0.883713],[-6.201346,2.854921,-7.460454],[2.050172,-9.294615,-5.934529],[-6.237438,-8.688531,-8.870130],[4.846940,-0.937336,3.919765],[0.012520,9.055987,6.585984],[1.195224,-5.545095,-0.340361],[6.534241,6.016545,0.975351]],[[-5.332064,9.407854,6.894359],[7.256458,-2.641341,-9.490597],[0.275700,-6.227940,-6.297470],[6.748474,4.349112,-9.047230],[0.413073,2.529211,3.422502],[-1.025643,9.225556,-6.871321],[5.283327,9.286134,6.058652],[-3.926637,7.287792,3.751504]]], dtype = "float32")#candidate|3057|(15, 8, 3)|const|float32
uop_3058 = relay.asinh(const_3057.astype('float32')) # shape=(15, 8, 3)
func_1863_call = mod.get_global_var('func_1863')
func_1865_call = mutated_mod.get_global_var('func_1865')
const_3065 = relay.const([[7,-1],[8,-8],[-10,7],[7,5],[-1,-10],[-7,-8],[1,2],[7,10],[-1,-8],[9,-6],[-5,2],[4,1],[-6,-6],[-6,-7],[-2,-10],[5,4],[-3,3],[-10,-10],[3,-8],[-9,-10],[-10,9],[3,-2],[5,5],[-2,-5],[5,6],[8,-10],[-9,-8],[7,-7],[-8,-2],[2,-7],[8,6],[5,6],[1,3],[9,10],[6,-10],[10,10],[4,1],[8,3],[-2,-5],[-2,6]], dtype = "uint8")#candidate|3065|(40, 2)|const|uint8
call_3064 = relay.TupleGetItem(func_1863_call(relay.reshape(const_3065.astype('uint8'), [80,])), 2)
call_3066 = relay.TupleGetItem(func_1865_call(relay.reshape(const_3065.astype('uint8'), [80,])), 2)
output = relay.Tuple([uop_3058,call_3064,const_3065,])
output2 = relay.Tuple([uop_3058,call_3066,const_3065,])
func_3069 = relay.Function([], output)
mod['func_3069'] = func_3069
mod = relay.transform.InferType()(mod)
output = func_3069()
func_3070 = relay.Function([], output)
mutated_mod['func_3070'] = func_3070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_3095 = func_1023_call()
call_3096 = func_1023_call()
func_1983_call = mod.get_global_var('func_1983')
func_1985_call = mutated_mod.get_global_var('func_1985')
const_3113 = relay.const([4,2,-8,-6,-10,9,2,-2,8,10,-8,-1,-2,-1,-9,-4,6,8,-7,-5,1,-4,-1,8,8,5,8,1,3,3,-6,6,-2,-8,-1,7,6,3,-8,9,8,3,9,9,8,5,6,-6,6,-9,-6,8,-8,9,3,-1,1,-8,8,4,9,1,-3,-6,-2,5,-1,-10,-6,-6,-7,10,1,-10,-5,-6,-6,-2,6,9,4,6,8,6,-2,-3,-9,9,-10,8,7,-2,1,-3,3,-4,7,4,-3,9,3,6,-2,-2,8,-10,6,-10,-9,3,-5,10,-7,7,-5,5,6,-1,-10,5,-5,-3,-8,-7,3,8,6,-10,-4,-3,3,8,1,10,-4,-9,9,-7,4,3,-3,7,-10,-4,-4,-3,7,6,3,-1,-2,-4,-2,-7,7,6,-2,-1,10,7,4,-10,-3,9,2,-1,-10,-5,-7,1,-6,-4,-9,-3,10,-10,-9,-5,7,-6,-4,5,-3,-10,-7,-2,7,-1,1,-5,1,-5,-8,-3,-4,5,-8,-4,3,1,5,10,9,10,3,-1,3,-7,4,-5,10,6,10,-1,4,-2,-5,-4,-4,-4,-10,-3,9,-3,1,3,7,1,9,-2,-2,-5,7,-1,6,9,-10,-8,-4,4,-8,-9,6,4,-10,2,1,8,9,-10,-5,-10,3,4,10,5,6,-4,-3,-2,7,4,-5,7,-4,-10,7,-3,-9,-2,-8,-8,-10,-1,-3,8,10,7,6,9,2,-8,1,-9,-2,-9,7,-7,10,-4,10,4,-3,5,-6,9,6,-4,9,-5,-6,1,2,2,5,-6,7,-5,10,10,-6,1,-4,-9,10,-6,-10,10,7,5,-10,-5,8,7,-1,3,4,9,1,-5,-2,7,-9,6,-1,-6,-10,9,-2,-8,-3,-10,7,7,7,-8,4,-3,-4,-1,-7,-5,-1,-9,-1,7,9,1,7,5,3,-3,1,-1,2,-10,-10,-8,-1,5,-3,6,-8,-2,-6,-8,-2,-7,4,10,10,7,-6,3,3,9,-8,1,-1,-2,-10,7,1,7,-2,3,6,3,8,-9,-6,8,3,-2,2,3,-6,4,-4,5,9,-9,-10,8,10,1,-6,-10,8,-3,-9,2,7,-3,8,-7,3,-1,8,-3,9,-6,2,-3,-9,-3,-3,4,-3,-10,-2,-8,-3,-2,-10,-1,8,5,-5,-2,-7,3,-2,-1,-3,-5,-8,-1,-6,3,-5,-7,4,-5,-10,-3,4,8,-2,-8,-10,9,-8,10,-1,-9,9,-1,8,10,-5,-7,-9,-2,4,6,-4,1,-3,-7,-3,-5,4,5,-4,-2,-8,-7,-3,-7,-10,8,-6,-8,-1,-7,5,7,10,1,-9,-2,-1,-3,9,-1,1,-2,10,9,-9,6,-10,3,-6,-3,-9,-1,3,7,2,-10,-7,3,4,-9,-10,-7,7,-10,4,8,-8,4,-3,-3,6,9,6,3,7,3,6,-10,9,9,-3,5,-8,-3,7,-5,1,-10,-9,9,4,3,-3,6,3,3,2,9,6,-10,-10,-8,2,-8,-1,-7,8,-7,-3,2,6,-3,-1,8,-6,10,3,7,-8,-6,-3,-3,3,3,-3,-1,8,7,8,-9,-4,-10,-1,-4,-3,7,3,8,-10,-3,6,9,-10,7,4,2,-9,4,-9,-6,-1,10,-2,2,-1,-4,1,-5,2,10,-10,-3,-3,6,5,6,-6,10,5,2,8,-5,9,-9,1,-8,-2,-7,-6,-8,-6,9,-9,2,2,9,7,-9,3,-1,9,-3,-8,7,5,9,8,-3,-6,2,-6,9,7,4,-10,-2,4,-2,-8,-8,-2,4,4,10,2,-9,-5,6,10,1,6,-9,-1,-3,-9,1,8,3,5,-2,-5,7,-1,1,-2,-9,8,-9,8,7,2,9,5,2,7,-7,4,4,7,-7,10,9,6,6,-9,3,2,3,-6,-7,8,-5,8,-10,-7,-5,-4,4,4,6,-2,7,3,-1,-5,-1,-4,7,-8,-8,7,1,-10,3,-4,7,2,-9,-4,-1,9,-3,-10,5,-1,-2,-10,10,-7,-6,-6,6,9,-10,-4,-1,6,-7,6,4,-9,-6,9,-9,-10,9,7,3,-9,-8,-5,9,3,-8,10,-6,8,5,7,6,-6,3,-10,-9,9,-3,6,-8,8,10,5,6,-10,-3,-5,-6,3,6,8,-4,3,-3,-9,-10,4,6,5,-5,3,4,8,-10,-9,-6,-2,-4,-8,-5,-6,8,2,1,6,-6,5,-8,8,-4,4,2,10,2,2,7,-10,-10,-8,4,1,4,8,9,-2,2,2,-2,1,10,-1,3,-9,4,8,-1,7,-4,-9,-10,-5,9,-8,8,6,3,5,7,-3,-1,-10,-9,-10,-10,6,-2,-2,-8,1,-10,-4,-4,-2,-2,3,-5,8,2,5,-6,3,1,8,-8,5,-8,2,9,3,9,5,-1,-8,-10,4,-5,6,2,7,-5,-9,-3,-2,-7,4,-3,9,-1,-6,1,6], dtype = "int32")#candidate|3113|(945,)|const|int32
call_3112 = func_1983_call(relay.reshape(const_3113.astype('int32'), [9, 15, 7]))
call_3114 = func_1983_call(relay.reshape(const_3113.astype('int32'), [9, 15, 7]))
func_3021_call = mod.get_global_var('func_3021')
func_3024_call = mutated_mod.get_global_var('func_3024')
const_3118 = relay.const([-0.195651,-6.069045,-5.317381,-3.483161,7.527348,7.780088,-3.641912,0.866797,-3.529122,4.127731,-8.173344,4.147897,6.864258,1.964208,8.175617,-6.389441,-9.331634,-6.731895,3.054064,3.879011,-6.667804,5.319023,-1.587683,-5.037856,1.384092,-9.073413,7.584921,-7.737924,1.123375,0.332309,-6.412754,-2.281031,-7.032457,2.669007,8.558274,-1.059237,8.339645,-7.193932,-2.445715,1.257699,-7.430174,5.353759,7.806677,-8.038722,-5.058570,7.473904,-7.174871,5.201616,7.812508,-5.553827,4.525793,-8.502474,-7.944138,-1.969503,1.648330,-9.171454,2.625586,-9.409973,-7.363321,8.804478,-5.550833,5.186367,7.152529,-2.703946,9.515850,2.373451,2.475740,-1.657414,6.505551,2.925240,-2.009219,-4.008072,2.840903,-4.032931,-9.464533,-2.074213,-8.905219,5.369321,-7.814357,-7.271357,-1.142019,-4.575487,4.344674,-6.443562,2.557361,-2.735057,6.001673,4.639182,0.146611,-3.375418,-1.584300,-2.599053,-0.583485,-0.641115,7.496797,9.637479,-5.948029,-5.794454,-1.889373,-2.571496,-3.252109,0.879928,-4.622815,-7.023523,-8.813677,9.522355,-8.558994,6.280154,4.456275,5.304405,8.214074,-5.196094,8.542189,7.806835,0.441417,2.580991,-2.946336,-5.662956,-0.840155,-5.727663,8.399251,0.625902,-2.569903,5.711004,-8.955900,-7.167387,1.050821,9.428711,2.167146,-1.745685,3.595650,-2.768128,-5.210253,-9.151157,-0.737101,3.432253,-7.152743,6.708196,9.037375,-4.898885,1.741542,7.356229,9.545034,3.843645,-5.235631,-5.058656,-6.994605,5.226723,5.457206,5.883855,7.438329,9.651203,2.783046,-8.904241,0.244796,-9.329100,1.027188,9.870179,-1.026676,-6.696185,-5.052959,-8.702486,1.931706,4.124820,6.205172,-8.094764,9.829705,-8.187089,-4.584252,-9.560431,2.068151,7.946177,-5.170996,-3.215012,7.150405,9.261079,5.625897,-6.051275,-1.234036,2.238673,-7.762218,-8.628510,1.598040,-9.633418,0.347652,-7.440395,7.519618,7.528277,-8.230409,1.787284,-9.448624,-5.520561,-5.658745,9.387395,-0.516501,0.494519,-1.435542,4.902218,-7.876765,-0.461295,-0.162166,6.153492,-4.409352,1.158436,-3.257951,-8.950630,-9.076787,-1.297922,-0.730720,2.018818,-7.766798,9.713476,-1.508279,-1.720757,8.755101,-4.026595,8.336458,5.006960,-5.873955,0.936186,1.768315,-9.079664,-0.122858,5.934148,-3.660836,1.320489,8.014172,9.709464,1.069989,-2.633202,-0.932563,-7.743304,-1.812682,3.124128,1.092229,6.552729,2.580855,-5.596348,-5.625339,-9.194430,-5.718926,8.120413,-1.316920,8.972918,9.864935,-9.216240,-5.432800,9.273505,6.554558,7.150799,6.975464,5.529705,-3.697347,-3.578676,5.781845,0.103239,7.749451,3.633964,-1.596559,7.675310,7.632477,8.735390,0.181946,-7.811924,-6.231682,6.599056,3.597026,-4.984677,-2.514175,-9.909077,0.572847,2.336524,9.827674,-9.471476,9.572259,5.289029,-2.486117,-3.242399,0.579227,-8.440813,-0.839685,-7.998529,-6.132774,-7.754603,1.120828,4.297045,-0.993240,0.049063,2.112432,8.163371,-4.267048,6.001945,-5.814650,-4.001370,6.590684,0.732683,-1.226158,4.675618,-7.421599,4.501590,-2.011728,-1.184923,0.790741,-2.039796,1.258630,2.019412,-7.318464,-8.645741,-7.149858,6.436717,2.370282,1.610902,-1.081624,5.424234,-0.252861,-5.170250,9.595119,-1.249205,8.986965,1.275454,-4.649276,-1.915071,-2.905592,4.959060,8.943425,-2.251661,3.312332,-2.287107,-6.584774,-3.803474,-6.191651,9.425493,5.700599,-9.445917,3.080370,-4.887899,-5.531903,-1.059448,6.282902,0.692983,-6.210685,-3.399871,8.734905,7.564585,-7.514900,4.720044,2.864633,-1.292534,-8.175739,0.179250,-1.084655,7.275995,-8.204014,7.366081,-2.956596,-7.565033,-7.652235,-3.560111,7.008336,0.010856,-8.579378,-4.808209,-5.803159,-6.827032,1.170424,-9.532905,1.027234,-0.473108,8.890061,-4.355151,-0.204186,5.230319,9.418880,-5.077876,6.237165,-1.477361,-4.827356,3.388174,8.491731,7.336382,8.687391,-3.271110,-4.151116,-0.441011,0.393466,4.336074,7.762788,-9.071529,-4.836402,5.375787,8.356384,2.828479,-0.343874,-5.900576,6.844487,-6.629226,3.028177,2.188628,3.246697,3.931198,-8.692914,-1.276575,5.968137,-5.408503,-4.365454,-9.231073,9.036707,8.928641,-9.363626,2.988008,-0.267735,1.488814,6.175222,8.217252,-3.827976,4.369899,3.250221,8.110195,-0.213770,-3.861133,6.333059,-2.314186,3.502022,9.112641,1.371251,5.042176,-5.273550,7.736273,1.126742,7.184493,-5.403505,4.146486,-1.305495,-0.060197,-2.411001,3.901232,9.461077,8.901480,-5.298199,9.476789,4.761294,0.547095,1.345919,4.583993,0.689342,-7.803075,7.840565,6.284665,-5.246321,6.540539,-0.990654,1.640239,-6.266284,-0.760358,7.151342,7.148288,-0.618445,-6.116340,6.219548,2.886497,-1.513117,-3.990187,4.852668,-7.904752,-3.435677,-2.239736,-1.888783,-4.180958,-5.849285,2.486884,-7.663273,6.820005,1.477324,-9.951192,2.325323,5.993795,-5.745161,-7.660143,1.566366,5.016625,-6.604579,6.104164,1.609216,2.896650,-8.510274,5.923548,4.069928,-3.835213,1.896889,-4.631882,-1.913650,-7.351556,1.167115,-9.827474,6.383278,-4.867297,3.036533,6.554392,-1.306538,1.400405,2.610571,3.624765,2.272089,-4.658651,9.505471,3.452324,-8.804116,-0.389889,-3.717437,1.294685,-7.294619,2.620327,8.415758,9.946137,-1.955967,-7.219645,4.626372,-0.160944,0.870794,7.244680,7.201191,-3.935164,0.822117,-4.030936,9.081211,6.058710,8.995536,-1.327375,0.301917,-0.990630,-6.248906,-3.482751,0.862507,-3.287758,2.457822,2.960858,-3.349894,-0.649757,-0.271735,-0.585170,-0.097314,3.440545,-6.819933,-5.490469,7.614548,7.399426,-3.566425,-8.138458,9.372030,-4.008066,-5.651554,8.306229,-1.973601,-1.419853,-2.133188,-1.550326,0.358558,7.074851,0.741306,5.921741,-6.931160,-9.783945,-6.096630,-8.149434,6.002161,-2.766123,-9.785860,6.640881,-9.054379,1.807397,-5.897277,3.976879,-2.905730,5.431665,5.167539,-7.146686,-7.596227,-4.991981,0.648958,-8.663026,7.756607,1.762976,-1.524040,-0.039554,-8.748418,-3.355043,-3.868304,-8.117009,-2.906558,-5.304147,9.843372,9.687051,-4.261349,-9.792930,4.567518,-8.113931,-4.597148,-8.945737,-2.543263,4.317007,4.220074,3.232968,7.143535,-3.960627,-9.774850,4.154215,1.960984,6.554891,-8.027765,-0.333185,-4.319879,3.306492,-4.055201,1.136771,-7.013071,6.374316,-3.046911,3.111786,3.202157,6.214566,0.894917,0.863743,-6.586237,-2.984899,-7.895546,-7.030495,5.032860,3.639044,4.955219,1.290916,7.682682,0.719109,7.227236,-3.214449,-2.480338,-6.977778,-3.167740,5.493357,-0.831721,-5.883327,-4.411516,5.932348,-6.458333,0.299798,-5.454542,1.285025,0.538919,5.627249,-4.242711,0.770370,-7.860107,-2.282148,5.018965,6.337021,6.315152,1.180238,-4.083314,2.002340,1.075177,-7.430561,4.779637,-4.894521,5.307394,-2.382864,9.027668,-4.506429,1.046338,-9.159449,-0.201230,7.509861,0.756776,8.271046,2.289278,-8.695219,3.050653,-8.522789,6.048786,-7.909716,9.903737,-7.603591,-5.481722,-2.631678,2.858106,0.174519,-1.920561,6.983366,0.283644,8.759361,2.925947,4.072127,-8.093401,-7.758592,-2.464363,-3.808834,3.089983,-6.229511,-2.849098,6.628831,-5.509935,2.583709,9.149153,-1.534230,-4.051058,-0.887785,-6.090605,-7.954212,3.892075,-6.526945,4.053557,1.735628,5.161792,9.688970,-1.972552,8.400235,0.904161,4.653685,4.425887,2.413163,9.814939,2.202252,6.859361,8.642553,-4.901039,4.709074,-4.413484,-6.434206,-2.532826,8.204941,3.112894,4.694932,-8.462239,9.688017,3.662007,0.637166,-3.566715,-8.556185,-0.742728,7.633272,6.366923,0.942537,1.943411,0.808359,4.889338,5.694072,0.640943,0.654400,8.426957,9.277819,5.077516,-3.977801,5.890221,6.386123,-8.258366,2.887889,8.459749,0.440567,-6.851196,4.494009,-3.865925,-2.813320,9.886966,5.655494,6.051165,2.065761,3.558155,-1.782243,-4.596552,-2.424643,-3.356283,-8.087359,-2.111103,4.366618,-6.470761,-7.998423,0.959197,-2.742250,-9.491332,5.934474,-6.013444,-5.136631,-6.744884,6.799088,4.257910,8.814978,3.682158,4.821537,-8.041958,-0.435631,0.841201,3.087732,-0.121917,-6.772223,5.030859,-2.720729,-8.984409,8.693964,8.847187,-5.924407,-6.843921,8.478311,1.445621,-5.101658,4.376123,9.841278,9.984525,6.457169,-0.528811,8.722601,3.149344,-1.467800,-5.307582,6.749230,-7.974609,-9.094055,9.853251,-0.083873,7.808479,-5.107952,2.942227,1.997458,-6.441429,-3.539340,-3.114006,-2.824622,3.935083,-1.030919,-0.390519,-9.378943,7.148457,-2.062611,-1.145470,6.043180,3.924509,-6.222008,5.028691,9.566723,-7.506489,8.956962,5.327941,-3.011545,-3.470888,1.735846,-3.512216,1.390369,-7.910295,6.682546,-4.464700,-8.515053,-3.157619,-2.187852,3.879343,-8.531012,-2.054027,-6.697437,0.378452,-0.966188,7.541453,5.490509,8.170099,3.438971,-2.994922,-0.647763,-4.616649,-6.516583,9.135936,-5.181332,-4.995684,-5.818789,-2.556031,9.258398,-0.292165,2.688949,9.006622,5.758621,1.710924,-2.560251,5.697209,-4.540944,-6.777806,8.886737,-9.301753,-6.122015,-2.098801,9.158588,2.995121,-4.943151,-4.547486,-1.084855,-1.394116,8.027461,-0.475568,9.823811,-6.488084,8.712361,-3.130110,0.156986,4.866729,-1.414863,-3.151062,-3.172810,-3.670237,2.554332,9.935427,-7.310787,-0.806573,3.827806,4.332796,-5.200066,9.922892,-6.426303,-1.089013,-1.406727,5.780987,6.211168,-7.047630,-3.387480,5.217234,7.447313,4.419049,-4.596416,6.761148,-6.794048,8.429499,7.106839,9.942815,-8.909108,3.626009,1.459349,5.535142,-5.410640,-7.010526,-9.435508,1.658084,-8.201790,2.238207,-9.494222,7.372875,-0.860936,1.634627,3.989938,0.872065,1.471895,-6.374485,-6.735263,5.607670,7.125613,4.938531,5.475247,3.160967,6.324367,5.222654,-4.724926,-3.046829,6.520868,-5.666675,-8.680713,-2.312812,-0.456945,-7.479426,0.351075,7.654364,-4.665765,-3.401179,0.014606,6.307776,3.276542,-4.312909,9.603527,-0.991137,4.317375,2.647955,-2.334407,4.161222,-9.235967,6.913371,2.857339,-9.415913,6.696649,-4.133853,3.075547,8.085053,-7.584721,-1.812387,1.517242,-5.081246,9.844303,-7.720252,6.871062,-8.266876,-6.445569,3.244283,-9.312258,8.452346,3.717900,1.850916,2.924646,9.354605,-1.646743,-7.579226,-6.224717,-2.463985,-5.184129,0.308909,-1.789289,-7.879493,-7.931092,0.703858,6.902453,-1.294725,-6.841612,0.389448,8.971820,0.219245,-2.598609,9.065832,-0.674811,-5.818345,-0.344703,-9.858743,3.257425,9.518251,0.238036,4.288264,6.221797,7.093072,0.495724,-9.316690,4.789816,-3.248702,1.666040,-0.403628,-1.930447,-8.923568,-9.309766,2.239128,1.712718,2.850995,7.131810,-1.021690,6.492856,-4.493924,-5.504936,3.987366,-1.799876,-4.633134,9.809435,8.818778,0.148024,-4.352147,3.225079,-2.486437,1.645124,1.423197,-1.772661,3.456925,0.586388,-4.721681,-4.010080,6.817876,9.705747,-7.013060,-0.010927,-7.256277,-0.414750,6.532288,9.776092,-9.250200,-7.261737,8.069344,8.103863,-3.454054,5.291185,5.167416,-0.785409,-2.458213,-1.104417,-6.161342,4.868162,-4.806988,3.714623,6.789148,4.079966,5.135403,0.304614,-9.193738,-7.925147,1.999046,2.637033,8.710938,6.929620,-9.269116,6.269362,-6.359317,9.834687,-2.354479,-4.566219,3.413796,6.266080,4.437399,-1.844444,-8.426355,-1.754654,-6.102554,-1.924226,4.718401,6.898021,1.283130,-4.925606,1.338154,-2.231571,5.907850,8.065508,8.076003,3.889712,3.946422,-5.454038,-8.407746,3.675859,7.606596,0.341863,0.606354,-6.073048,3.183707,-1.840707,-7.114122,-8.750610,-8.132084,0.098336,-6.831919,-4.344570,-6.785721,4.970367,-0.472557,7.913249,-8.633054,-2.665240,7.105160,-8.683305,-6.453083,-9.387627,-5.144925,-5.930258,-3.050607,-0.106714,-1.046451,5.146111,9.778395,-8.709759,9.677182,8.898119,-2.756821,-3.963761,-4.515622,-6.410343,9.244221,-6.498290,1.161037,-2.306329,-4.893549,-1.803464,-7.412449,6.106664,5.697114,1.664987,9.673050,-2.880745,-5.156045,4.807571,-5.323834,2.100614,-9.009803,3.619091,-7.186111,-5.869251,-0.494053,-5.495344,-4.891225,-2.129250,1.270887,-2.260213,4.221263,-1.719264,8.540745,-8.546727,7.707428,-8.878437,3.005461,2.041859,6.489905,-0.378730,-2.105460,-9.557057,-2.726368,-9.676092,-9.306361,-4.271742,-6.854309,-6.618589,4.215792,2.061403,-2.306878,-3.197508,3.848922,-7.813983,6.271720,-1.815516,9.163788,-3.593009,9.026255,5.857712,-8.125244,3.595660,-9.491674,-3.228719,6.923778,-3.552025,0.015840,2.470982,-7.969539,-5.840955,4.476963,9.686415,4.281428,-1.930462,0.753762,5.374179,-7.884524,-4.488439,-3.194410,-8.034718,-1.346620,9.436118,4.427792,-9.030324,-5.889334,-4.695303,5.434490,-4.169437,6.293310,6.812416,-8.444715,-2.958391,-4.026181,6.397839,-9.228848,-8.474460,-3.126523,-6.494696,-2.172095,5.648439,6.550866,-0.686008,-4.988928,-9.287772,-7.379928,-0.689426,-6.491143,5.941771,5.816453,3.047227,-1.639667,-7.161692,3.422226,-9.264771,1.701203,1.423284,8.283139,4.068879,-4.441913,-9.087318,2.100474,-6.975034,2.049450,-7.323186,-0.641932,-0.318035,6.113181,-5.732959,-2.763980,1.252977,-2.950157,-8.631511,-9.894315,2.935595,0.200135,9.518804,-8.945828,-1.139327,5.102074,-1.731823,-5.106276,-5.069549,0.714831,4.664792,-3.543748,8.346471,6.630011,-7.889557,5.659477,-1.534654,0.542962,-2.827650,7.001578,-4.766329,7.497527,5.476252,0.556431,-3.671019,-9.581811,-2.972029,-0.776167,0.826901,-0.778621,9.512267,-5.164188,-2.496590,-7.782000,9.177447,-0.085816,-0.932849,7.977058,2.796503,-5.311427,5.133900,0.372382,8.261122,-8.441808,8.695930,-4.460225,-9.309208,2.159632,9.800965,7.380306,8.895962,-1.923119,-0.794048,2.501909,-8.404837,1.531084,-3.457269,-2.107664,-7.205527,9.264337,9.653920,-2.982127,-6.426445,-3.186634,1.251244,-7.845252,9.181579,6.349311,-3.540745], dtype = "float64")#candidate|3118|(1352,)|const|float64
call_3117 = relay.TupleGetItem(func_3021_call(relay.reshape(const_3118.astype('float64'), [8, 13, 13]), relay.reshape(const_3118.astype('float64'), [8, 13, 13]), ), 1)
call_3119 = relay.TupleGetItem(func_3024_call(relay.reshape(const_3118.astype('float64'), [8, 13, 13]), relay.reshape(const_3118.astype('float64'), [8, 13, 13]), ), 1)
output = relay.Tuple([call_3095,call_3112,const_3113,call_3117,const_3118,])
output2 = relay.Tuple([call_3096,call_3114,const_3113,call_3119,const_3118,])
func_3129 = relay.Function([], output)
mod['func_3129'] = func_3129
mod = relay.transform.InferType()(mod)
mutated_mod['func_3129'] = func_3129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mutated_mod.get_global_var('func_3129')
call_3130 = func_3129_call()
output = call_3130
func_3131 = relay.Function([], output)
mutated_mod['func_3131'] = func_3131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3038_call = mod.get_global_var('func_3038')
func_3039_call = mutated_mod.get_global_var('func_3039')
call_3135 = relay.TupleGetItem(func_3038_call(), 3)
call_3136 = relay.TupleGetItem(func_3039_call(), 3)
func_1863_call = mod.get_global_var('func_1863')
func_1865_call = mutated_mod.get_global_var('func_1865')
var_3138 = relay.var("var_3138", dtype = "uint8", shape = (80,))#candidate|3138|(80,)|var|uint8
call_3137 = relay.TupleGetItem(func_1863_call(relay.reshape(var_3138.astype('uint8'), [80,])), 2)
call_3139 = relay.TupleGetItem(func_1865_call(relay.reshape(var_3138.astype('uint8'), [80,])), 2)
bop_3141 = relay.bitwise_or(var_3138.astype('int8'), relay.reshape(call_3137.astype('int8'), relay.shape_of(var_3138))) # shape=(80,)
bop_3144 = relay.bitwise_or(var_3138.astype('int8'), relay.reshape(call_3139.astype('int8'), relay.shape_of(var_3138))) # shape=(80,)
output = relay.Tuple([call_3135,bop_3141,])
output2 = relay.Tuple([call_3136,bop_3144,])
func_3147 = relay.Function([var_3138,], output)
mod['func_3147'] = func_3147
mod = relay.transform.InferType()(mod)
mutated_mod['func_3147'] = func_3147
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3148 = relay.var("var_3148", dtype = "uint8", shape = (80,))#candidate|3148|(80,)|var|uint8
func_3147_call = mutated_mod.get_global_var('func_3147')
call_3149 = func_3147_call(var_3148)
output = call_3149
func_3150 = relay.Function([var_3148], output)
mutated_mod['func_3150'] = func_3150
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3162 = relay.var("var_3162", dtype = "float32", shape = (10, 4, 5))#candidate|3162|(10, 4, 5)|var|float32
uop_3163 = relay.asinh(var_3162.astype('float32')) # shape=(10, 4, 5)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3167 = relay.TupleGetItem(func_3129_call(), 1)
call_3168 = relay.TupleGetItem(func_3131_call(), 1)
output = relay.Tuple([uop_3163,call_3167,])
output2 = relay.Tuple([uop_3163,call_3168,])
func_3171 = relay.Function([var_3162,], output)
mod['func_3171'] = func_3171
mod = relay.transform.InferType()(mod)
var_3172 = relay.var("var_3172", dtype = "float32", shape = (10, 4, 5))#candidate|3172|(10, 4, 5)|var|float32
output = func_3171(var_3172)
func_3173 = relay.Function([var_3172], output)
mutated_mod['func_3173'] = func_3173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2842_call = mod.get_global_var('func_2842')
func_2843_call = mutated_mod.get_global_var('func_2843')
call_3179 = relay.TupleGetItem(func_2842_call(), 0)
call_3180 = relay.TupleGetItem(func_2843_call(), 0)
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_3183 = relay.TupleGetItem(func_2198_call(relay.reshape(call_3179.astype('float64'), [2, 12, 13])), 2)
call_3184 = relay.TupleGetItem(func_2200_call(relay.reshape(call_3179.astype('float64'), [2, 12, 13])), 2)
func_2108_call = mod.get_global_var('func_2108')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_3188 = relay.TupleGetItem(func_2108_call(), 0)
call_3189 = relay.TupleGetItem(func_2110_call(), 0)
func_3171_call = mod.get_global_var('func_3171')
func_3173_call = mutated_mod.get_global_var('func_3173')
var_3191 = relay.var("var_3191", dtype = "float32", shape = (1, 200))#candidate|3191|(1, 200)|var|float32
call_3190 = relay.TupleGetItem(func_3171_call(relay.reshape(var_3191.astype('float32'), [10, 4, 5])), 1)
call_3192 = relay.TupleGetItem(func_3173_call(relay.reshape(var_3191.astype('float32'), [10, 4, 5])), 1)
uop_3194 = relay.sigmoid(call_3190.astype('float64')) # shape=(9, 15, 7)
uop_3196 = relay.sigmoid(call_3192.astype('float64')) # shape=(9, 15, 7)
output = relay.Tuple([call_3179,call_3183,call_3188,var_3191,uop_3194,])
output2 = relay.Tuple([call_3180,call_3184,call_3189,var_3191,uop_3196,])
func_3204 = relay.Function([var_3191,], output)
mod['func_3204'] = func_3204
mod = relay.transform.InferType()(mod)
mutated_mod['func_3204'] = func_3204
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3205 = relay.var("var_3205", dtype = "float32", shape = (1, 200))#candidate|3205|(1, 200)|var|float32
func_3204_call = mutated_mod.get_global_var('func_3204')
call_3206 = func_3204_call(var_3205)
output = call_3206
func_3207 = relay.Function([var_3205], output)
mutated_mod['func_3207'] = func_3207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1953_call = mod.get_global_var('func_1953')
func_1954_call = mutated_mod.get_global_var('func_1954')
call_3280 = relay.TupleGetItem(func_1953_call(), 1)
call_3281 = relay.TupleGetItem(func_1954_call(), 1)
output = call_3280
output2 = call_3281
func_3284 = relay.Function([], output)
mod['func_3284'] = func_3284
mod = relay.transform.InferType()(mod)
mutated_mod['func_3284'] = func_3284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3284_call = mutated_mod.get_global_var('func_3284')
call_3285 = func_3284_call()
output = call_3285
func_3286 = relay.Function([], output)
mutated_mod['func_3286'] = func_3286
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3304 = relay.var("var_3304", dtype = "float32", shape = (2, 9, 5))#candidate|3304|(2, 9, 5)|var|float32
uop_3305 = relay.erf(var_3304.astype('float32')) # shape=(2, 9, 5)
func_3069_call = mod.get_global_var('func_3069')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_3330 = relay.TupleGetItem(func_3069_call(), 0)
call_3331 = relay.TupleGetItem(func_3070_call(), 0)
output = relay.Tuple([uop_3305,call_3330,])
output2 = relay.Tuple([uop_3305,call_3331,])
func_3335 = relay.Function([var_3304,], output)
mod['func_3335'] = func_3335
mod = relay.transform.InferType()(mod)
var_3336 = relay.var("var_3336", dtype = "float32", shape = (2, 9, 5))#candidate|3336|(2, 9, 5)|var|float32
output = func_3335(var_3336)
func_3337 = relay.Function([var_3336], output)
mutated_mod['func_3337'] = func_3337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_3360 = func_1023_call()
call_3361 = func_1023_call()
uop_3364 = relay.sigmoid(call_3360.astype('float32')) # shape=(2, 12, 13)
uop_3366 = relay.sigmoid(call_3361.astype('float32')) # shape=(2, 12, 13)
func_2277_call = mod.get_global_var('func_2277')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_3367 = relay.TupleGetItem(func_2277_call(), 2)
call_3368 = relay.TupleGetItem(func_2278_call(), 2)
uop_3384 = relay.cosh(uop_3364.astype('float32')) # shape=(2, 12, 13)
uop_3386 = relay.cosh(uop_3366.astype('float32')) # shape=(2, 12, 13)
var_3387 = relay.var("var_3387", dtype = "float32", shape = (2, 12, 13))#candidate|3387|(2, 12, 13)|var|float32
bop_3388 = relay.not_equal(uop_3384.astype('bool'), relay.reshape(var_3387.astype('bool'), relay.shape_of(uop_3384))) # shape=(2, 12, 13)
bop_3391 = relay.not_equal(uop_3386.astype('bool'), relay.reshape(var_3387.astype('bool'), relay.shape_of(uop_3386))) # shape=(2, 12, 13)
func_2277_call = mod.get_global_var('func_2277')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_3392 = relay.TupleGetItem(func_2277_call(), 0)
call_3393 = relay.TupleGetItem(func_2278_call(), 0)
func_1316_call = mod.get_global_var('func_1316')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_3400 = relay.TupleGetItem(func_1316_call(relay.reshape(var_3387.astype('bool'), [2, 12, 13])), 0)
call_3401 = relay.TupleGetItem(func_1319_call(relay.reshape(var_3387.astype('bool'), [2, 12, 13])), 0)
output = relay.Tuple([call_3367,bop_3388,call_3392,call_3400,])
output2 = relay.Tuple([call_3368,bop_3391,call_3393,call_3401,])
func_3410 = relay.Function([var_3387,], output)
mod['func_3410'] = func_3410
mod = relay.transform.InferType()(mod)
mutated_mod['func_3410'] = func_3410
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3411 = relay.var("var_3411", dtype = "float32", shape = (2, 12, 13))#candidate|3411|(2, 12, 13)|var|float32
func_3410_call = mutated_mod.get_global_var('func_3410')
call_3412 = func_3410_call(var_3411)
output = call_3412
func_3413 = relay.Function([var_3411], output)
mutated_mod['func_3413'] = func_3413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_3450 = relay.TupleGetItem(func_1648_call(), 1)
call_3451 = relay.TupleGetItem(func_1650_call(), 1)
func_1116_call = mod.get_global_var('func_1116')
func_1119_call = mutated_mod.get_global_var('func_1119')
var_3464 = relay.var("var_3464", dtype = "int64", shape = (180,))#candidate|3464|(180,)|var|int64
call_3463 = relay.TupleGetItem(func_1116_call(relay.reshape(var_3464.astype('int64'), [10, 3, 6]), relay.reshape(var_3464.astype('int64'), [10, 3, 6]), ), 0)
call_3465 = relay.TupleGetItem(func_1119_call(relay.reshape(var_3464.astype('int64'), [10, 3, 6]), relay.reshape(var_3464.astype('int64'), [10, 3, 6]), ), 0)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_3473 = relay.TupleGetItem(func_1088_call(), 1)
call_3474 = relay.TupleGetItem(func_1090_call(), 1)
func_2108_call = mod.get_global_var('func_2108')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_3488 = relay.TupleGetItem(func_2108_call(), 0)
call_3489 = relay.TupleGetItem(func_2110_call(), 0)
output = relay.Tuple([call_3450,call_3463,var_3464,call_3473,call_3488,])
output2 = relay.Tuple([call_3451,call_3465,var_3464,call_3474,call_3489,])
func_3496 = relay.Function([var_3464,], output)
mod['func_3496'] = func_3496
mod = relay.transform.InferType()(mod)
var_3497 = relay.var("var_3497", dtype = "int64", shape = (180,))#candidate|3497|(180,)|var|int64
output = func_3496(var_3497)
func_3498 = relay.Function([var_3497], output)
mutated_mod['func_3498'] = func_3498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1459_call = mod.get_global_var('func_1459')
func_1461_call = mutated_mod.get_global_var('func_1461')
call_3506 = func_1459_call()
call_3507 = func_1459_call()
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_3513 = relay.TupleGetItem(func_1648_call(), 1)
call_3514 = relay.TupleGetItem(func_1650_call(), 1)
output = relay.Tuple([call_3506,call_3513,])
output2 = relay.Tuple([call_3507,call_3514,])
func_3520 = relay.Function([], output)
mod['func_3520'] = func_3520
mod = relay.transform.InferType()(mod)
mutated_mod['func_3520'] = func_3520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3520_call = mutated_mod.get_global_var('func_3520')
call_3521 = func_3520_call()
output = call_3521
func_3522 = relay.Function([], output)
mutated_mod['func_3522'] = func_3522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2210_call = mod.get_global_var('func_2210')
func_2211_call = mutated_mod.get_global_var('func_2211')
call_3528 = func_2210_call()
call_3529 = func_2210_call()
func_1648_call = mod.get_global_var('func_1648')
func_1650_call = mutated_mod.get_global_var('func_1650')
call_3530 = relay.TupleGetItem(func_1648_call(), 1)
call_3531 = relay.TupleGetItem(func_1650_call(), 1)
func_2415_call = mod.get_global_var('func_2415')
func_2418_call = mutated_mod.get_global_var('func_2418')
var_3547 = relay.var("var_3547", dtype = "float64", shape = (160,))#candidate|3547|(160,)|var|float64
call_3546 = relay.TupleGetItem(func_2415_call(relay.reshape(var_3547.astype('float64'), [4, 5, 8])), 0)
call_3548 = relay.TupleGetItem(func_2418_call(relay.reshape(var_3547.astype('float64'), [4, 5, 8])), 0)
func_812_call = mod.get_global_var('func_812')
func_813_call = mutated_mod.get_global_var('func_813')
call_3555 = relay.TupleGetItem(func_812_call(), 0)
call_3556 = relay.TupleGetItem(func_813_call(), 0)
func_3069_call = mod.get_global_var('func_3069')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_3566 = relay.TupleGetItem(func_3069_call(), 0)
call_3567 = relay.TupleGetItem(func_3070_call(), 0)
output = relay.Tuple([call_3528,call_3530,call_3546,var_3547,call_3555,call_3566,])
output2 = relay.Tuple([call_3529,call_3531,call_3548,var_3547,call_3556,call_3567,])
func_3569 = relay.Function([var_3547,], output)
mod['func_3569'] = func_3569
mod = relay.transform.InferType()(mod)
mutated_mod['func_3569'] = func_3569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3570 = relay.var("var_3570", dtype = "float64", shape = (160,))#candidate|3570|(160,)|var|float64
func_3569_call = mutated_mod.get_global_var('func_3569')
call_3571 = func_3569_call(var_3570)
output = call_3571
func_3572 = relay.Function([var_3570], output)
mutated_mod['func_3572'] = func_3572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2082_call = mod.get_global_var('func_2082')
func_2083_call = mutated_mod.get_global_var('func_2083')
call_3612 = func_2082_call()
call_3613 = func_2082_call()
func_2210_call = mod.get_global_var('func_2210')
func_2211_call = mutated_mod.get_global_var('func_2211')
call_3623 = func_2210_call()
call_3624 = func_2210_call()
func_1316_call = mod.get_global_var('func_1316')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_3626 = relay.TupleGetItem(func_1316_call(relay.reshape(call_3623.astype('bool'), [2, 12, 13])), 0)
call_3627 = relay.TupleGetItem(func_1319_call(relay.reshape(call_3623.astype('bool'), [2, 12, 13])), 0)
func_2277_call = mod.get_global_var('func_2277')
func_2278_call = mutated_mod.get_global_var('func_2278')
call_3631 = relay.TupleGetItem(func_2277_call(), 0)
call_3632 = relay.TupleGetItem(func_2278_call(), 0)
func_2378_call = mod.get_global_var('func_2378')
func_2380_call = mutated_mod.get_global_var('func_2380')
call_3638 = relay.TupleGetItem(func_2378_call(), 1)
call_3639 = relay.TupleGetItem(func_2380_call(), 1)
func_3335_call = mod.get_global_var('func_3335')
func_3337_call = mutated_mod.get_global_var('func_3337')
var_3641 = relay.var("var_3641", dtype = "float32", shape = (3, 30))#candidate|3641|(3, 30)|var|float32
call_3640 = relay.TupleGetItem(func_3335_call(relay.reshape(var_3641.astype('float32'), [2, 9, 5])), 1)
call_3642 = relay.TupleGetItem(func_3337_call(relay.reshape(var_3641.astype('float32'), [2, 9, 5])), 1)
const_3647 = relay.const([[-6.519353,-7.503125,-7.022793,5.566403,6.990020,-1.296446,4.671699,8.378401,-6.970274,8.883504,-3.462302,8.966251,-6.565669,2.123600,-0.272657,-0.065701,-0.901248,-3.832404,-7.222749,-2.710090,-3.934730,5.189802,5.323106,7.439673,8.795521,-5.919410,1.253622,-9.421525,-9.182096,-4.088218],[-2.439760,0.034599,1.445506,3.666699,-0.777943,-7.570485,5.116117,-0.829289,-6.501767,-6.507199,6.939176,6.154009,3.217286,-9.463946,-7.735172,-4.353281,8.179383,7.398887,4.659886,8.657572,1.897899,-5.241597,6.978998,4.460717,-0.851058,-7.101878,-2.336465,-7.815499,3.607360,8.843676],[3.934093,1.695768,-3.679743,-6.727178,2.699528,9.590414,2.235211,3.444238,-5.039551,-7.965573,4.730477,-9.173964,-5.546935,1.200976,3.733439,6.000853,-0.304287,-1.208999,-2.857407,-6.865041,-6.952403,-0.401550,2.093125,-9.170765,-8.592099,-8.080190,2.532685,3.918369,1.849651,-2.101790]], dtype = "float32")#candidate|3647|(3, 30)|const|float32
bop_3648 = relay.left_shift(var_3641.astype('int32'), relay.reshape(const_3647.astype('int32'), relay.shape_of(var_3641))) # shape=(3, 30)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3656 = relay.TupleGetItem(func_3129_call(), 3)
call_3657 = relay.TupleGetItem(func_3131_call(), 3)
output = relay.Tuple([call_3612,call_3623,call_3626,call_3631,call_3638,call_3640,bop_3648,call_3656,])
output2 = relay.Tuple([call_3613,call_3624,call_3627,call_3632,call_3639,call_3642,bop_3648,call_3657,])
func_3672 = relay.Function([var_3641,], output)
mod['func_3672'] = func_3672
mod = relay.transform.InferType()(mod)
var_3673 = relay.var("var_3673", dtype = "float32", shape = (3, 30))#candidate|3673|(3, 30)|var|float32
output = func_3672(var_3673)
func_3674 = relay.Function([var_3673], output)
mutated_mod['func_3674'] = func_3674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3520_call = mod.get_global_var('func_3520')
func_3522_call = mutated_mod.get_global_var('func_3522')
call_3699 = relay.TupleGetItem(func_3520_call(), 1)
call_3700 = relay.TupleGetItem(func_3522_call(), 1)
func_1730_call = mod.get_global_var('func_1730')
func_1732_call = mutated_mod.get_global_var('func_1732')
call_3701 = func_1730_call()
call_3702 = func_1730_call()
func_2842_call = mod.get_global_var('func_2842')
func_2843_call = mutated_mod.get_global_var('func_2843')
call_3707 = relay.TupleGetItem(func_2842_call(), 0)
call_3708 = relay.TupleGetItem(func_2843_call(), 0)
output = relay.Tuple([call_3699,call_3701,call_3707,])
output2 = relay.Tuple([call_3700,call_3702,call_3708,])
func_3712 = relay.Function([], output)
mod['func_3712'] = func_3712
mod = relay.transform.InferType()(mod)
output = func_3712()
func_3713 = relay.Function([], output)
mutated_mod['func_3713'] = func_3713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2210_call = mod.get_global_var('func_2210')
func_2211_call = mutated_mod.get_global_var('func_2211')
call_3738 = func_2210_call()
call_3739 = func_2210_call()
uop_3744 = relay.log(call_3738.astype('float32')) # shape=(2, 12, 13)
uop_3746 = relay.log(call_3739.astype('float32')) # shape=(2, 12, 13)
func_2210_call = mod.get_global_var('func_2210')
func_2211_call = mutated_mod.get_global_var('func_2211')
call_3766 = func_2210_call()
call_3767 = func_2210_call()
func_1983_call = mod.get_global_var('func_1983')
func_1985_call = mutated_mod.get_global_var('func_1985')
var_3774 = relay.var("var_3774", dtype = "int32", shape = (945,))#candidate|3774|(945,)|var|int32
call_3773 = func_1983_call(relay.reshape(var_3774.astype('int32'), [9, 15, 7]))
call_3775 = func_1983_call(relay.reshape(var_3774.astype('int32'), [9, 15, 7]))
output = relay.Tuple([uop_3744,call_3766,call_3773,var_3774,])
output2 = relay.Tuple([uop_3746,call_3767,call_3775,var_3774,])
func_3807 = relay.Function([var_3774,], output)
mod['func_3807'] = func_3807
mod = relay.transform.InferType()(mod)
var_3808 = relay.var("var_3808", dtype = "int32", shape = (945,))#candidate|3808|(945,)|var|int32
output = func_3807(var_3808)
func_3809 = relay.Function([var_3808], output)
mutated_mod['func_3809'] = func_3809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1730_call = mod.get_global_var('func_1730')
func_1732_call = mutated_mod.get_global_var('func_1732')
call_3857 = func_1730_call()
call_3858 = func_1730_call()
output = call_3857
output2 = call_3858
func_3867 = relay.Function([], output)
mod['func_3867'] = func_3867
mod = relay.transform.InferType()(mod)
mutated_mod['func_3867'] = func_3867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3867_call = mutated_mod.get_global_var('func_3867')
call_3868 = func_3867_call()
output = call_3868
func_3869 = relay.Function([], output)
mutated_mod['func_3869'] = func_3869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1914_call = mod.get_global_var('func_1914')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_3870 = func_1914_call()
call_3871 = func_1914_call()
output = relay.Tuple([call_3870,])
output2 = relay.Tuple([call_3871,])
func_3872 = relay.Function([], output)
mod['func_3872'] = func_3872
mod = relay.transform.InferType()(mod)
mutated_mod['func_3872'] = func_3872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3872_call = mutated_mod.get_global_var('func_3872')
call_3873 = func_3872_call()
output = call_3873
func_3874 = relay.Function([], output)
mutated_mod['func_3874'] = func_3874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2210_call = mod.get_global_var('func_2210')
func_2211_call = mutated_mod.get_global_var('func_2211')
call_3901 = func_2210_call()
call_3902 = func_2210_call()
func_634_call = mod.get_global_var('func_634')
func_636_call = mutated_mod.get_global_var('func_636')
call_3908 = func_634_call()
call_3909 = func_634_call()
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_3912 = relay.TupleGetItem(func_3129_call(), 0)
call_3913 = relay.TupleGetItem(func_3131_call(), 0)
output = relay.Tuple([call_3901,call_3908,call_3912,])
output2 = relay.Tuple([call_3902,call_3909,call_3913,])
func_3919 = relay.Function([], output)
mod['func_3919'] = func_3919
mod = relay.transform.InferType()(mod)
output = func_3919()
func_3920 = relay.Function([], output)
mutated_mod['func_3920'] = func_3920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_3933 = relay.TupleGetItem(func_3712_call(), 2)
call_3934 = relay.TupleGetItem(func_3713_call(), 2)
output = relay.Tuple([call_3933,])
output2 = relay.Tuple([call_3934,])
func_3935 = relay.Function([], output)
mod['func_3935'] = func_3935
mod = relay.transform.InferType()(mod)
mutated_mod['func_3935'] = func_3935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3935_call = mutated_mod.get_global_var('func_3935')
call_3936 = func_3935_call()
output = call_3936
func_3937 = relay.Function([], output)
mutated_mod['func_3937'] = func_3937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2082_call = mod.get_global_var('func_2082')
func_2083_call = mutated_mod.get_global_var('func_2083')
call_3985 = func_2082_call()
call_3986 = func_2082_call()
output = relay.Tuple([call_3985,])
output2 = relay.Tuple([call_3986,])
func_3987 = relay.Function([], output)
mod['func_3987'] = func_3987
mod = relay.transform.InferType()(mod)
mutated_mod['func_3987'] = func_3987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3987_call = mutated_mod.get_global_var('func_3987')
call_3988 = func_3987_call()
output = call_3988
func_3989 = relay.Function([], output)
mutated_mod['func_3989'] = func_3989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1459_call = mod.get_global_var('func_1459')
func_1461_call = mutated_mod.get_global_var('func_1461')
call_3990 = func_1459_call()
call_3991 = func_1459_call()
func_1863_call = mod.get_global_var('func_1863')
func_1865_call = mutated_mod.get_global_var('func_1865')
const_3995 = relay.const([[-5,-10,9,2,9,-4,-6,-9,-7,7,-7,-10,7,-2,6,-5,8,7,-3,-1,-4,5,1,-7,7,2,8,-6,5,-1,3,3,1,-9,8,-9,4,6,-8,-6],[6,10,1,8,-3,7,5,7,2,2,-7,6,-5,-7,-5,9,-10,-5,2,-8,-4,-2,7,-7,-5,-2,-2,-4,-1,1,5,-9,-6,7,-8,6,10,-1,5,-9]], dtype = "uint8")#candidate|3995|(2, 40)|const|uint8
call_3994 = relay.TupleGetItem(func_1863_call(relay.reshape(const_3995.astype('uint8'), [80,])), 2)
call_3996 = relay.TupleGetItem(func_1865_call(relay.reshape(const_3995.astype('uint8'), [80,])), 2)
output = relay.Tuple([call_3990,call_3994,const_3995,])
output2 = relay.Tuple([call_3991,call_3996,const_3995,])
func_4002 = relay.Function([], output)
mod['func_4002'] = func_4002
mod = relay.transform.InferType()(mod)
mutated_mod['func_4002'] = func_4002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4002_call = mutated_mod.get_global_var('func_4002')
call_4003 = func_4002_call()
output = call_4003
func_4004 = relay.Function([], output)
mutated_mod['func_4004'] = func_4004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_4005 = relay.TupleGetItem(func_3129_call(), 2)
call_4006 = relay.TupleGetItem(func_3131_call(), 2)
func_1316_call = mod.get_global_var('func_1316')
func_1319_call = mutated_mod.get_global_var('func_1319')
const_4010 = relay.const([[False,True,False,False],[False,True,True,True],[False,False,True,True],[True,True,True,False],[True,True,True,True],[True,True,True,True],[True,False,True,False],[True,False,True,True],[True,True,False,False],[False,True,True,False],[False,False,False,True],[True,True,True,False],[True,False,False,False],[False,True,True,True],[True,False,True,False],[True,False,False,False],[True,False,False,False],[True,True,False,True],[False,False,False,True],[False,False,False,True],[False,False,True,False],[True,True,False,False],[True,True,True,False],[False,True,True,True],[True,True,True,False],[True,False,False,True],[False,False,False,False],[False,False,True,True],[False,True,True,True],[False,True,False,True],[True,True,False,True],[False,True,False,True],[False,False,True,True],[False,True,False,False],[False,True,True,False],[True,False,True,False],[True,True,True,True],[False,True,True,True],[False,True,False,False],[False,True,True,False],[True,True,False,True],[False,False,True,False],[True,False,True,True],[True,False,True,False],[True,False,False,False],[False,True,True,False],[False,False,True,False],[True,False,False,False],[True,False,True,False],[True,False,False,False],[True,True,True,False],[False,False,False,True],[True,False,True,True],[True,True,True,True],[True,False,True,False],[True,False,False,False],[False,True,False,True],[True,True,False,False],[False,True,False,False],[False,True,False,True],[True,True,False,True],[False,True,False,True],[False,False,True,True],[False,True,True,False],[False,False,False,False],[True,False,False,True],[True,True,False,True],[False,False,False,True],[True,False,False,False],[False,True,True,False],[True,True,True,True],[False,False,True,True],[False,True,True,True],[True,True,True,True],[False,True,False,False],[True,True,False,False],[True,False,False,True],[True,False,True,False]], dtype = "bool")#candidate|4010|(78, 4)|const|bool
call_4009 = relay.TupleGetItem(func_1316_call(relay.reshape(const_4010.astype('bool'), [2, 12, 13])), 0)
call_4011 = relay.TupleGetItem(func_1319_call(relay.reshape(const_4010.astype('bool'), [2, 12, 13])), 0)
var_4028 = relay.var("var_4028", dtype = "int32", shape = (945,))#candidate|4028|(945,)|var|int32
bop_4029 = relay.floor_divide(call_4005.astype('float64'), relay.reshape(var_4028.astype('float64'), relay.shape_of(call_4005))) # shape=(945,)
bop_4032 = relay.floor_divide(call_4006.astype('float64'), relay.reshape(var_4028.astype('float64'), relay.shape_of(call_4006))) # shape=(945,)
output = relay.Tuple([call_4009,const_4010,bop_4029,])
output2 = relay.Tuple([call_4011,const_4010,bop_4032,])
func_4040 = relay.Function([var_4028,], output)
mod['func_4040'] = func_4040
mod = relay.transform.InferType()(mod)
var_4041 = relay.var("var_4041", dtype = "int32", shape = (945,))#candidate|4041|(945,)|var|int32
output = func_4040(var_4041)
func_4042 = relay.Function([var_4041], output)
mutated_mod['func_4042'] = func_4042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2438_call = mod.get_global_var('func_2438')
func_2439_call = mutated_mod.get_global_var('func_2439')
call_4056 = relay.TupleGetItem(func_2438_call(), 0)
call_4057 = relay.TupleGetItem(func_2439_call(), 0)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_4086 = relay.TupleGetItem(func_1088_call(), 2)
call_4087 = relay.TupleGetItem(func_1090_call(), 2)
output = relay.Tuple([call_4056,call_4086,])
output2 = relay.Tuple([call_4057,call_4087,])
func_4093 = relay.Function([], output)
mod['func_4093'] = func_4093
mod = relay.transform.InferType()(mod)
output = func_4093()
func_4094 = relay.Function([], output)
mutated_mod['func_4094'] = func_4094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1953_call = mod.get_global_var('func_1953')
func_1954_call = mutated_mod.get_global_var('func_1954')
call_4161 = relay.TupleGetItem(func_1953_call(), 1)
call_4162 = relay.TupleGetItem(func_1954_call(), 1)
func_3171_call = mod.get_global_var('func_3171')
func_3173_call = mutated_mod.get_global_var('func_3173')
var_4165 = relay.var("var_4165", dtype = "float32", shape = (200,))#candidate|4165|(200,)|var|float32
call_4164 = relay.TupleGetItem(func_3171_call(relay.reshape(var_4165.astype('float32'), [10, 4, 5])), 0)
call_4166 = relay.TupleGetItem(func_3173_call(relay.reshape(var_4165.astype('float32'), [10, 4, 5])), 0)
var_4187 = relay.var("var_4187", dtype = "float32", shape = (10, 4, 5))#candidate|4187|(10, 4, 5)|var|float32
bop_4188 = relay.power(call_4164.astype('float64'), relay.reshape(var_4187.astype('float64'), relay.shape_of(call_4164))) # shape=(10, 4, 5)
bop_4191 = relay.power(call_4166.astype('float64'), relay.reshape(var_4187.astype('float64'), relay.shape_of(call_4166))) # shape=(10, 4, 5)
func_4093_call = mod.get_global_var('func_4093')
func_4094_call = mutated_mod.get_global_var('func_4094')
call_4226 = relay.TupleGetItem(func_4093_call(), 1)
call_4227 = relay.TupleGetItem(func_4094_call(), 1)
func_1807_call = mod.get_global_var('func_1807')
func_1809_call = mutated_mod.get_global_var('func_1809')
const_4230 = relay.const([-7.132552,9.495486,5.478787,2.481633,5.456829,-6.408346,6.508858,-9.582780,-9.128710,6.593041,-2.449062,-5.683001,-5.730965,4.300386,-9.142137,-8.636125,3.125504,4.495713,-4.167591,8.722480,-1.458508,9.695772,0.003295,-5.901823,-7.516105,-2.368366,-8.418895,-4.422340,8.056754,-3.225847,-7.921943,-2.234259,-3.867983,-6.128185,-9.602911,-7.082826,-5.203849,8.375537,2.714041,5.201350,4.524898,-5.122217,-9.248359,9.658382,-4.641038,2.091075,-5.861603,1.822546,5.321674,1.012312,5.955019,3.354604,8.760216,1.723562,-8.554893,2.986502,-1.681936,0.513672,-5.930611,-8.885642,-0.645719,-7.685285,8.688584,4.924950,9.367422,4.684289,-3.916075,-5.686706,6.325899,4.047208,-5.272005,3.450220,-5.736057,4.244665,6.239313,-0.194254,7.626153,4.279819,-0.968978,-4.974124,7.527811,-7.072631,-9.216240,-9.303663,-0.472866,7.690472,-2.785028,2.822605,-6.116289,6.190074,6.939891,0.192554,-9.177729,6.484480,-0.227265,5.474180,4.555250,1.071780,-5.988358,4.771710,2.622631,-4.614475,-4.830490,5.277431,-0.409335,-2.502637,-3.086377,4.037067,-5.613751,8.423278,-1.159914,9.390447,-9.963722,5.630774,-7.759013,0.295971,0.344287,1.428828,1.786375,-0.154930,4.716940,2.886293,4.018500,2.788269,-5.236696,-2.207271,0.928062,-0.032943,-4.599460,-9.621052,7.444167,1.243520,9.047389,-2.184933,1.467161,1.974160,7.613394,-7.232425,6.698847,4.324570,-2.353920,-4.518390,6.050363,6.955984,-1.777824,-4.961157,6.181698,-2.420249,-8.319522,5.687587,-8.800387,-1.070412,-1.819216,-7.995882,-7.864824,9.452611,0.551331,-0.368307,-2.031055,-1.388196,-4.640712,-5.727772,-2.384221,-1.169881,1.512920,-9.635380,-6.916847,-1.480577,7.401542,-2.948932,-1.508363,-5.095222,5.476928,-8.686691,-5.231478,-2.199484,3.059019,-4.289879,-9.647598,-9.946558,0.631760,7.179356,5.567456,-9.383284,-0.154602,6.314107,-0.824668,-3.932613,-2.466382,9.740990,1.565462,9.220708,1.488827,2.003189,8.001181,8.853525,-4.057500,-1.175332,-5.440137,8.266575,-9.544839,9.172763,-5.888660,-2.284449,-4.449344,-4.657049,-0.589411,-6.823548,4.729065,3.167610,6.350622,9.838600,9.052736,-5.443944,-4.131709,-0.710000,-7.263105,9.155483,4.112163,3.791655,-7.645094,3.194238,-8.940264,-4.964707,9.201992,-2.643912,-5.780037,0.849700,2.907611,-6.828907,6.661699,-0.794733,-8.716603,-7.042796,-4.336428,-8.616847,1.793325,4.567958,9.477841,-4.649431,2.251823,-8.163964,-8.833113,0.491408,4.661723,-8.263551,-1.525607,-9.898746,-6.296671,-3.939489,-9.875499,7.838814,-3.151856,4.878119,-0.109977,2.959680,-2.573060,-6.808246,9.558566,8.364299,8.931145,6.158904,-8.553782,-7.135475,-7.679992,0.373459,6.438544,7.527141,1.640631,-6.299057,-8.641985,0.788214,7.007245,1.286488,2.219901,3.182091,-5.348781,-7.032830,-5.540464,-6.892201,0.275837,3.186037,-7.897404,3.891765,-1.078206,-8.214522,4.602154,0.536211,8.593223,9.973995,1.575734,3.781810,4.543763,3.704319,-7.560294,-3.357348,2.228406,3.496483,-2.232338,-0.543476,-3.669965,1.174086,-3.723480,-3.933423,-3.830123,6.959069,-6.139902,7.277685,-1.577865,8.863333,-1.441270,5.717706,2.582788,-9.303276,1.800678,-9.082527,3.222479,3.386102,0.373101,7.203282,7.585350,9.318159,7.797606,4.037215,7.169903,-1.858408,-9.745730,-6.225928,-3.580768,-9.987704,9.414750,7.696864,-5.243507,-6.371805,-3.265182,9.025814,-0.346432,9.535765,-0.548019,-7.404193,4.538219,3.520333,-5.777911,-0.401562,-5.830513,-7.985445,4.947525,-2.915720,-8.389186,2.677410,-1.541474,-8.105738,-8.942538,-3.195260,-7.032969,-3.872034,-7.681601,2.329428,9.905658,5.352114,-7.763532,2.434181,-8.211376,-5.318471,5.680570,1.851808,-4.353297,-6.490338,-4.312585,7.517269,0.733093,-9.999262,-9.514022,-7.094920,4.057435,8.564566,2.049479,-6.824568,2.915630,-8.942009,-9.563326,-4.244447,4.821150,0.275709,-1.265250,-8.582777,6.305693,3.126335,4.407548,8.984277,9.400393,-4.714078,-2.888770,-2.364305,3.127742,-6.601455,9.194253,2.006710,2.902125,-3.033836,8.650432,-0.602355,6.406503,-3.560456,0.536576,-8.626953,2.357116,-0.369050,0.641166,3.199077,5.548441,-3.289607,-4.032158,-6.157412,2.140086,7.533547,0.686205,8.191380,3.105355,0.187157,3.515578,-5.690280,6.787892,-7.728401,8.370660,4.707705,8.789556,8.325768,6.940920,-9.670645,-5.257386,-5.477350,2.658016,1.572722,9.656696,5.605059,-8.764420,2.748887,-9.777815,-7.985675,9.655921,6.119468,7.629996,4.423436,-3.232076,9.607861,0.089079,-7.725322,6.042272,-8.585595,7.949159,-1.091577,4.211245,8.637328,6.839227,2.636743,2.711877,-0.732077,-8.985834,-9.816850,8.288413,3.050430,8.862062,4.048472,3.904973,6.214837,4.381314,-5.219346,-2.501293,4.672549,4.324817,-6.273293,1.156553,-7.013658,-0.879959,-8.700562,-4.738955,8.411525,3.666091,7.817362,-5.130631,1.767548,-6.283812,-1.680055,6.131500,-7.049955,-9.724580,-6.149503,1.463575,6.666762], dtype = "float32")#candidate|4230|(490,)|const|float32
call_4229 = relay.TupleGetItem(func_1807_call(relay.reshape(const_4230.astype('float32'), [490,])), 0)
call_4231 = relay.TupleGetItem(func_1809_call(relay.reshape(const_4230.astype('float32'), [490,])), 0)
bop_4233 = relay.divide(var_4165.astype('float32'), relay.reshape(var_4187.astype('float32'), relay.shape_of(var_4165))) # shape=(200,)
output = relay.Tuple([call_4161,bop_4188,call_4226,call_4229,const_4230,bop_4233,])
output2 = relay.Tuple([call_4162,bop_4191,call_4227,call_4231,const_4230,bop_4233,])
func_4239 = relay.Function([var_4165,var_4187,], output)
mod['func_4239'] = func_4239
mod = relay.transform.InferType()(mod)
mutated_mod['func_4239'] = func_4239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4239_call = mutated_mod.get_global_var('func_4239')
var_4241 = relay.var("var_4241", dtype = "float32", shape = (200,))#candidate|4241|(200,)|var|float32
var_4242 = relay.var("var_4242", dtype = "float32", shape = (10, 4, 5))#candidate|4242|(10, 4, 5)|var|float32
call_4240 = func_4239_call(var_4241,var_4242,)
output = call_4240
func_4243 = relay.Function([var_4241,var_4242,], output)
mutated_mod['func_4243'] = func_4243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3038_call = mod.get_global_var('func_3038')
func_3039_call = mutated_mod.get_global_var('func_3039')
call_4257 = relay.TupleGetItem(func_3038_call(), 3)
call_4258 = relay.TupleGetItem(func_3039_call(), 3)
func_2108_call = mod.get_global_var('func_2108')
func_2110_call = mutated_mod.get_global_var('func_2110')
call_4274 = relay.TupleGetItem(func_2108_call(), 0)
call_4275 = relay.TupleGetItem(func_2110_call(), 0)
output = relay.Tuple([call_4257,call_4274,])
output2 = relay.Tuple([call_4258,call_4275,])
func_4277 = relay.Function([], output)
mod['func_4277'] = func_4277
mod = relay.transform.InferType()(mod)
output = func_4277()
func_4278 = relay.Function([], output)
mutated_mod['func_4278'] = func_4278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_4281 = relay.TupleGetItem(func_1088_call(), 1)
call_4282 = relay.TupleGetItem(func_1090_call(), 1)
var_4283 = relay.var("var_4283", dtype = "uint16", shape = (5, 8, 2))#candidate|4283|(5, 8, 2)|var|uint16
bop_4284 = relay.bitwise_and(call_4281.astype('uint16'), relay.reshape(var_4283.astype('uint16'), relay.shape_of(call_4281))) # shape=(5, 8, 2)
bop_4287 = relay.bitwise_and(call_4282.astype('uint16'), relay.reshape(var_4283.astype('uint16'), relay.shape_of(call_4282))) # shape=(5, 8, 2)
func_1146_call = mod.get_global_var('func_1146')
func_1148_call = mutated_mod.get_global_var('func_1148')
const_4298 = relay.const([[-0.534830],[-6.714061],[9.190628],[7.226370],[-4.261268],[-8.445569],[-8.831064],[9.648819],[2.525908],[2.683327],[9.951029],[-9.560757],[8.355898],[-3.594133],[-8.033526],[-5.930163],[-7.240624],[-6.478451],[-9.226054],[-0.438193],[-7.085294],[6.649556],[5.385317],[2.044915],[4.752613],[6.825758],[3.009148],[-5.476474],[2.245173],[-6.142421],[6.404304],[-5.575562],[8.535121],[8.318133],[-8.822138],[-2.590176],[-9.892300],[-1.271726],[4.242462],[5.390913],[-8.627434],[0.533837],[-7.201079],[-6.590509],[5.164081],[4.256439],[7.603080],[-7.727363],[-7.811728],[5.992131],[-2.627276],[1.985283],[4.555542],[-3.369875],[5.111426],[0.517937],[-5.481812],[7.549156],[-7.392385],[-4.065360],[-6.834242],[-4.420356],[3.583621],[7.434659],[-9.167869],[-2.147818],[-9.778279],[-3.374708],[3.934675],[-3.229546],[-7.433717],[4.232595],[0.881476],[3.535314],[-9.857979],[2.785106],[6.522734],[0.552879],[-5.414426],[-8.024440],[9.609947],[2.565839],[-6.985040],[7.358363],[-4.915070],[5.824733],[1.499861],[0.239774],[9.658792],[3.798163],[-4.044384],[6.313274],[-9.044779],[-4.905112],[9.184179],[-0.102488],[-7.270704],[-1.064708],[5.361200],[-6.508951],[-0.929187],[-2.388537],[-7.141742],[-2.002159],[-5.757262],[-6.218925],[-2.292327],[-3.611939],[-7.357088],[9.501717],[6.233782],[-9.606419],[-1.880319],[-5.532981],[-0.219891],[1.780775],[-3.657360],[-2.160108],[-9.996609],[7.578258],[-6.577206],[6.417733],[9.162209],[-4.153502],[2.120344],[1.173370],[9.585357],[-8.336965],[-1.646308],[3.925251],[3.794452],[8.019602],[-8.387251],[0.093666],[-8.127078],[1.756416],[-3.052268],[5.350216],[-9.832490],[8.882358],[-7.979689],[-9.726189],[-6.912334],[3.262596],[8.289871],[6.702391],[2.973383],[4.955774],[-0.528271],[-6.299007],[0.511762],[-7.795083],[8.910651],[1.743598],[4.356253],[6.901626],[0.346454],[6.474975],[-9.706998],[-4.305544],[7.640410],[-5.189467],[5.668959],[-8.813734],[-8.099278],[-8.520665],[-9.823349],[2.232235],[5.140106],[0.715734],[9.001677],[-5.696046],[-8.998026],[-3.148898],[-8.433540],[-2.765983],[-0.764294],[-7.908949],[-6.750636],[-5.225481],[-4.111603],[-8.074585],[3.527378],[-4.328745],[-0.592662],[8.753424],[-0.586629],[-5.677652],[6.102523],[3.095888],[-5.289540],[6.736765],[-3.720891],[-2.752245],[-5.394740],[-3.132034],[7.493773],[0.275381],[-5.246228],[3.886642],[1.115873],[6.432469],[-9.381046],[-1.083373],[-4.006284],[3.615807],[8.613349],[-7.417748],[8.626122],[4.204135],[6.265432],[-0.218940],[-2.193653],[4.618659],[0.425119],[-5.839252],[8.892504],[-1.819690],[7.916985],[5.748895],[-3.840049],[-1.612657],[1.866067],[6.120170],[6.645612],[-7.269438],[-4.917548],[-5.380385],[-3.545679],[-0.548759],[-1.276794],[-4.961754],[-2.954980],[-9.224432],[1.728650],[3.360524],[-7.035808],[2.212851],[-9.575951],[-4.421920],[9.023664],[-3.188248],[1.364714],[0.121030],[-2.262780],[8.711585],[-6.276793],[-3.385094],[-2.443459],[-9.782441],[-0.716127],[4.627997],[-6.246392],[-2.901598],[-2.774295],[-7.078378],[0.886178],[2.487442],[6.858549],[-5.792099],[-9.469938],[5.276442],[6.558112],[8.330222],[-8.142580],[8.132756],[-9.780850],[3.862235],[-2.163563],[9.847947],[4.201350],[-9.413040],[1.117167],[0.198560],[-0.056979],[-1.672895],[-2.482160],[6.552133],[-5.104209],[3.729182],[1.067689],[4.952946],[-0.087953],[-6.617459],[4.328846],[2.427018],[0.089076],[9.689009],[3.974119],[-5.175153],[2.367501],[7.199377],[-7.330604],[8.472578],[3.373938],[8.187994],[-0.216291],[-8.966420],[3.579760],[0.552760],[6.082151],[3.589601],[-9.425815],[1.884142],[-3.553892],[-2.643669],[-7.643109],[7.579678],[-9.888595],[1.610370],[2.542497],[-4.099228],[-6.062849],[-1.771040],[1.365486],[-6.035750],[-5.547663],[-3.713975],[-1.021686],[3.764830],[6.635302],[-4.691012],[8.054326],[-2.512831],[1.852417],[5.020389],[-0.468030],[-3.661657],[6.962677],[-0.132449],[-1.084302],[3.467059],[5.097596],[3.206757],[5.613855],[-3.836684],[-4.284691],[-1.346555],[-7.551333],[-2.264881],[1.619149],[-7.099394],[8.078369],[-6.629576],[-4.863924],[-5.637058],[2.039871],[1.288066],[6.947964],[-5.135141],[1.269441],[5.817908],[-5.784898],[6.672193],[-1.841362],[-5.241515],[-4.357794],[0.312949],[9.802360],[-5.979069],[-0.556738],[-8.535645],[-9.705671],[-0.815637],[-9.801714],[-4.904574],[5.050551],[-2.189393],[4.539690],[-4.952568],[7.759208],[5.655152],[-9.595300],[9.124431],[-0.124920],[3.657054],[-0.961503],[-2.306412],[2.930491],[-1.577687],[-3.164265],[-8.293995],[-8.376571],[2.007848],[-6.123011],[5.066282],[-4.162754],[9.689164],[5.573277],[-1.992434],[-2.660868],[5.878048],[5.779853],[8.678803],[-4.117255],[-8.225101],[-5.377402],[5.427405],[6.774061],[2.250310],[-6.585558],[2.490319],[2.681185],[0.893274],[-9.480501],[0.570171],[9.743837],[1.078773],[-8.894824],[-4.472343],[6.332382],[4.497177],[5.517660],[-6.632338],[0.708967],[-3.052285],[6.481914],[-5.080897],[7.817798],[3.533111],[7.856190],[-5.442323],[4.393957],[1.535775],[4.829475],[8.279505],[8.667012],[-2.707672],[4.853233],[4.205639],[-5.744697],[-2.066784],[-3.207238],[7.923226],[2.702284],[4.273324],[9.378691],[0.489241],[8.540478],[-6.457082],[-5.099892],[6.347605],[0.787676],[-4.807712],[1.533757],[4.665246],[-4.898291],[9.128370],[2.871237],[-0.169611],[2.717743],[2.098303],[4.999605],[-4.446326],[-8.288797],[1.679880],[-9.203781],[-2.233124],[2.796139],[-2.371186],[-1.457300],[-6.977989],[4.891154],[5.403657],[-8.065968],[3.654659],[0.357473],[-3.444673],[-8.335567],[-5.353067],[-7.127204],[9.072786],[-4.467812],[-2.677915],[5.696390],[-1.705909],[-8.584466],[-7.491892],[-5.881199],[-4.341965],[5.359369],[7.011852],[5.274144],[3.701353],[-7.387382],[-5.772991],[-4.448675],[1.862799],[7.800116],[-4.476131],[-7.351700],[-0.684133],[9.251355],[-0.271162],[7.978808],[9.297223],[0.716162],[8.548643],[-1.153699],[-4.937333],[-5.321546],[8.998220],[-2.211723],[-7.873928],[-8.660927],[-8.375369],[5.862206],[-5.097217],[3.158887],[0.165232],[3.657107],[5.274248],[4.292017],[2.637130],[-1.128077],[-7.192572],[-6.378750],[9.169897],[-1.573618],[-0.372996],[-7.780151],[8.154676],[-2.192955],[-5.366358],[-7.463419],[-1.201451],[-9.622288],[-6.489577],[-9.308837],[-0.748999],[3.145929],[-3.304080],[-7.039919],[9.671887],[1.229439],[-5.272539],[-7.178055],[2.457741],[3.442996],[7.226566],[4.185429],[8.015333],[9.143962],[3.785319],[-8.248935],[-7.548910],[-0.766034],[4.308440],[-4.481382],[2.891209],[4.995002],[2.561645],[0.927130],[-3.910501],[3.132171],[3.831387],[8.950208],[-0.143864],[-6.623908],[-5.967248],[0.013567],[2.577012],[7.302130],[3.818349],[2.171726],[1.729836],[-4.398284],[-5.136119],[-0.255748],[-9.917343],[-1.263422],[-5.700311],[-3.804266],[4.934613],[5.934714],[7.418991],[-9.833168],[-8.831032],[-4.988954],[-2.807139],[5.243851],[-7.966153],[-4.744985],[1.665259],[9.790808],[-8.461568],[9.748343],[2.638921],[-7.903719],[7.870059],[-0.956747],[-3.349175],[4.321568],[5.351798],[-9.412771],[7.224646],[4.043442],[4.105826],[-4.274635],[-5.091753],[-5.513713],[-6.981837],[-8.904213],[-6.926221],[-5.633717],[-2.956982],[-3.290008],[9.854688],[0.294700],[9.811179],[-8.849030],[3.354119],[-3.729385],[-8.286563],[-7.774836],[-9.854924],[0.572120],[-0.537339],[-6.247732],[-0.742627],[-5.452323],[-6.153425],[-0.165733],[-4.702198],[-2.381588],[4.168516],[-6.722069],[-4.945502],[-8.019191],[-8.251783],[-1.462570],[8.768520],[9.702334],[4.549085],[-4.929455],[-1.583913],[-7.483733],[-6.492033],[-6.174723],[-3.317742],[-3.859493],[-0.475596],[5.711879],[-2.773357],[9.182286],[-2.400750],[0.138191],[4.728355],[7.557785],[9.302853],[5.080442],[4.736957],[-3.839526],[-7.494420],[-4.706357],[0.642661],[-5.830506],[-7.399724],[-0.996112],[0.320633],[6.437203],[6.584762],[-5.146336],[3.357216],[9.822937],[9.131093],[-3.623523],[-5.500074],[-8.981685],[1.042150],[-7.952983],[-6.793440],[-0.264966],[-1.764229],[6.675180],[-1.740879],[6.267157],[4.145855],[5.108752],[2.377929],[8.944981],[6.828301],[6.336131],[-0.964161],[-2.113410],[8.690925],[-4.698508],[8.745693],[-3.911284],[-3.770973],[-4.369484],[-6.414616],[-0.442160],[8.536212],[-5.110646],[2.388924],[7.115170],[8.654902],[-6.768756],[9.311915],[4.719598],[9.065472],[-3.691083],[1.387967],[-2.547670],[-8.945329],[-3.713118],[-7.888298],[-5.649386],[-8.074294],[1.179198],[6.763692],[-4.251508],[9.026507],[-2.954342],[0.459842],[7.267758],[-0.083714],[-2.415269],[-5.607761],[8.203663],[1.012941],[6.806108],[-9.459770],[8.185137],[-2.709712],[-6.621837],[2.166431],[-6.702548],[-0.612023],[1.932539],[5.604954],[-4.482400],[-8.701537],[4.114334],[-8.435884],[2.949811],[-8.710606],[3.927696],[6.409452],[-9.743745],[9.557078],[8.640145],[1.917044],[-3.719737],[-9.439042],[-9.345926],[-1.695353],[2.279234],[0.675772],[-6.828730],[2.133624],[4.234881],[-2.270747],[2.421975],[4.181106],[-2.325764],[-6.062313],[7.124107],[0.016293],[7.607809],[-8.362299],[3.376554],[6.405757],[7.701730],[8.357101],[-5.736171],[-0.098878],[9.752721],[-0.408567],[-4.091681],[-5.162224],[3.520941],[-2.637495],[-3.762759],[-5.233039],[1.543123],[9.528894],[9.797754],[-7.899303],[8.642872],[-2.697544],[-8.131436],[9.092556],[-4.542966],[-0.631694],[5.163427],[3.349369],[-1.913750],[-3.382525],[8.112210],[-0.232064],[7.302632],[-8.477766],[-9.335783],[2.699867],[-4.546926],[8.509826],[-3.634343],[-4.310998],[1.210180],[7.061017],[7.681746],[9.561407],[-0.409720],[1.664811],[-5.938732],[7.315401],[2.502726],[-8.726480],[-2.105986],[-4.744905],[-6.737806],[5.709097],[-0.277890],[2.712482],[7.321903],[2.210094],[3.940910],[-3.274881],[-7.132482],[1.270678],[7.676567],[-9.749280],[-2.461638],[2.149264],[-3.646889],[-3.595626],[4.484375],[-6.580510],[9.716207],[3.917084],[-5.512083],[-7.831484],[1.963007],[-7.965218],[-0.817488],[-2.884699],[-2.417933],[-0.219631],[-1.176483],[8.719850],[9.976425],[4.013823],[6.968280],[6.705234],[2.182774],[6.198181],[1.164786],[6.842706],[-7.954695],[-2.714491],[6.090955],[7.305789],[4.940933],[3.608437],[3.344775],[-7.308132],[-1.769056],[3.471039],[1.407028],[-6.684780],[-7.955008],[6.375947],[8.147407],[-1.032873],[-5.311421],[-9.544939],[-8.072436],[5.515388],[-2.113498],[9.363470],[1.348242],[-7.253937],[1.322088],[3.408529],[-6.226144],[6.134869],[-8.116923],[-4.413609],[6.982931],[5.502914],[7.336823],[6.146617],[1.336605],[0.295269],[0.770061],[2.438691],[3.545270],[-2.127890],[-6.938890],[2.358656],[-7.335532],[3.267031],[8.446449],[-8.001199],[-0.390726],[-3.462925],[-0.985340],[3.344524],[-8.475795],[0.425664],[9.487570],[-3.365055],[-0.469918],[1.359845],[4.639151],[-5.146999],[0.866007],[-4.277688],[0.976423],[4.981693],[-3.586924],[-4.110064],[-6.051949],[7.423655],[-9.202517],[-8.116646],[5.801368],[-5.329170],[-8.764942],[-4.505919],[4.672223],[8.092354],[-8.468521],[0.143245],[-4.209997],[-0.328406],[3.570671],[3.794691],[-1.325765],[-6.541203],[9.191899],[5.889391],[-7.526213],[5.006321],[4.938718],[-2.910090],[-2.324791],[-8.356592],[2.797038],[-8.164611],[-6.810052],[-0.215937],[8.583560],[9.896101],[-7.623040],[1.987073],[0.799953],[0.728388],[-8.358663],[-9.976309],[-2.251190],[-6.398408],[-2.595351],[-3.401120],[1.857588],[2.545368],[6.010356],[2.912728],[-6.035398],[-2.912721],[-3.719263],[-2.222095],[-2.421712],[4.857869],[-4.249530],[9.975574],[-0.546153],[3.979838],[-0.228809],[-1.096477],[9.557277],[9.130953],[-6.244193],[9.844958],[-9.280675],[5.317115],[4.379740],[-6.029084],[9.445123],[1.181873],[1.684204],[3.572456],[-1.858035],[-8.930979],[-2.452417],[-2.099325],[-0.306705],[-0.044420],[-5.207015],[7.121460],[2.323060],[-7.070487],[8.037427],[9.405164],[-1.635695],[-9.774504],[4.776330],[-6.190551],[6.718940],[-3.333335],[1.412620],[4.865310],[-6.026789],[-2.208447],[1.990646],[6.119063],[4.829225],[-0.911550],[-8.180968],[3.485336],[-8.754079],[-0.355309],[6.668562],[4.564949],[2.247153],[-7.307849],[9.113894],[1.817226],[6.403911],[-5.771452],[0.305122],[-3.237378],[0.775420],[5.996683],[-5.586835],[6.258577],[7.947229],[-0.605875],[-8.881295],[4.041797],[3.696948],[-5.081530],[7.819479],[-3.758833],[-3.811018],[3.018184],[5.484362],[-0.330129],[-3.082304],[-9.668255],[-0.389056],[1.695370],[-9.483093],[4.230654],[-0.423072],[-2.895529],[-1.966560],[-4.887210],[-6.999921],[3.878406],[7.726283],[4.980852],[-9.541788],[-6.550187],[9.312370],[5.390421],[-4.325750],[4.830300],[-9.780696],[1.925003],[3.980791],[-5.616479],[-0.524990],[6.415229],[3.977373],[5.385541],[-7.703063],[3.648588],[-4.658899],[3.093153],[3.302883],[-9.310409],[-3.538983],[-5.611911],[-1.439330],[0.762221],[0.665205],[5.546615],[-8.850261],[6.567498],[3.947968],[-5.474133],[2.580232],[-1.300154],[2.722857],[4.353390],[-9.925304],[-1.828610],[-3.576972],[0.555856],[-6.251829],[-8.779363],[-8.776599],[-7.891484],[6.583573],[5.062347],[-0.967402],[-1.675711],[8.337153],[-6.704290],[-4.349660],[7.211772],[8.455409],[4.770380],[-9.293921],[-8.493722],[5.376249],[4.347974],[-4.876074],[-9.467574],[3.634824],[1.180967],[-7.161074],[8.565012],[-2.310924],[-1.401824],[0.960771],[-2.743428],[-9.871486],[-0.033785],[-0.717705],[1.303943],[-0.798747],[-6.723220],[-6.589754],[-8.052527],[-2.589569],[-5.459162],[6.165895],[-6.901998],[0.537392],[-2.948272],[2.927094],[0.657237],[3.223082],[-5.984394],[-6.489670],[2.078655],[-7.636200],[2.722657],[7.698563],[-0.267222],[6.373186],[-3.267307],[-6.097060],[6.281741],[4.260543],[4.587446],[-3.731032],[-4.460782],[-5.954781],[3.674747],[7.598271],[2.938261],[-7.618556],[-2.033644],[-6.717907],[4.563190],[9.087060],[-1.375838],[9.189137],[0.734532],[-6.474022],[9.445500],[5.167316],[-8.925712],[-5.049797],[-5.678432],[-4.925950],[-0.224887],[2.065193],[-1.061054],[3.300124],[3.049814],[1.719370],[8.824683],[1.434788],[-8.863881],[0.521682],[-6.562727],[9.882237],[-6.449789],[9.296102],[1.369932],[8.085809],[-5.561467],[5.091485],[-3.046543],[0.322423],[1.265112],[-9.427517],[9.313269],[-9.134625],[4.403847],[9.447678],[-7.455287],[-7.030163],[-8.470560],[-2.934117],[6.535004],[3.271433],[-7.388916],[3.302763],[-9.778313],[-4.227155],[8.600690],[-6.371427],[0.686911],[-4.876512],[-0.028630],[-4.169391],[6.915051],[5.101582],[-5.436287],[5.453379],[1.506849],[-3.862347],[6.433099],[3.392958],[-4.506496],[-0.324233],[-6.932888],[-0.229973],[8.935784],[-9.552523],[-9.546304],[-7.005297],[2.817641],[7.215771],[9.241384],[3.482915],[-4.392538],[-4.837252],[5.504997],[1.569071],[-7.537343],[-3.832495],[-3.791226],[-3.054638],[8.921781],[7.104252],[7.072387],[1.601550],[5.430521],[1.308937],[-7.181892],[-1.511980],[-4.477096],[-4.967062],[-5.722727],[8.523956],[8.217879],[1.595838],[-9.234085],[4.438538],[-4.178599],[0.047064],[5.304058],[-9.794474],[6.935241],[8.565787],[-8.275373],[-5.369312],[1.343942],[1.437258],[-3.325728],[-9.380235],[-6.940773],[2.764038],[2.802424],[-4.416367],[2.548708],[4.261216],[0.929523],[-6.324058],[2.773038],[-8.823915],[7.449615],[-4.303521],[7.043062],[-7.336601],[-6.283029],[-5.022899],[-4.420499],[6.722328],[-6.365915],[0.533909],[2.073270],[-9.467881],[-7.162558],[-4.948580],[3.184287],[0.725023],[7.795154],[3.443515],[9.564791],[9.640579],[-3.666373],[-4.075938],[7.919149],[-1.219738],[-9.666575],[-1.409615],[-9.230541],[-6.965540],[5.517155],[9.931518],[7.201804],[9.638077],[-6.570810],[7.315848],[-6.401482],[-4.958692],[-0.307414],[7.250375],[-3.394908],[-3.461985],[2.104109],[2.988523],[4.067403],[-5.548315],[-3.435437],[6.741476],[-7.899980],[-7.193045],[2.996603],[9.974090],[-0.240819],[-8.016693],[-1.161089],[9.324581],[6.060648],[3.013042],[-5.687124],[3.440294],[-6.641846],[-4.427246],[6.009078],[-8.877412],[-7.852784],[-4.362587],[4.652193],[0.352895],[8.885000],[-5.645564],[6.472012],[9.319898],[9.679730],[6.716907],[2.624049],[-0.156212],[-4.427486],[-0.469330],[-9.696713],[7.248803],[4.989367],[0.739362],[7.118615],[0.001973],[-7.543524],[9.543426],[5.753558],[2.577140],[8.594781],[-9.063329],[3.590634],[1.840388],[1.794816],[5.897474],[-9.969105],[-4.594106],[-8.519060],[-3.464642],[-2.060684],[3.516722],[-2.541325],[-2.537893],[4.777154],[-4.571005],[-9.819672],[1.804129],[0.862349],[2.949457],[-6.001739],[6.016394],[0.685729],[-6.786644],[6.996828],[-1.770678],[-8.139124],[-1.689313],[-1.010737],[-5.867539],[-5.004152],[-4.152716],[0.470169],[-5.253626],[-4.699503],[2.837700],[-2.516506],[-8.687192],[-0.750756],[-8.367281],[8.147061],[3.350245],[-9.450832],[-2.018261],[-0.631756],[-1.293361],[-6.258330],[8.375309],[-2.661741],[-4.395744],[8.579457],[6.580876],[-0.380413],[-5.057236],[-7.036137],[-9.481578],[8.163982],[-4.536123],[-2.292739],[-7.946907],[3.039008],[4.066403],[7.891110],[-7.058974],[0.408378],[3.564739],[-7.626525],[-7.265428],[-1.579416],[-1.630539],[1.481510],[-8.406552],[-6.056500],[-7.134594],[-9.000522],[-3.209371],[1.834167],[0.143875],[-1.169606],[-4.585028],[-6.413175],[0.395801],[-1.125614],[-5.429706],[-8.050313],[-3.060930],[2.952394],[-7.252560],[7.590444],[-0.974305],[8.772390],[8.185076],[8.191886],[5.836595],[-1.408475],[9.245777],[7.119418],[-7.438446],[-4.336257],[-2.540618],[4.709652],[5.553075],[-5.882798],[-2.865860],[-6.021014],[6.390250],[9.950572],[0.477129],[0.012677],[8.255722],[-3.496845],[-1.319518],[6.177670],[-9.162059],[6.788301],[-7.468260],[6.463273],[-0.225763],[8.315492],[5.622060],[2.757503],[8.099023],[2.489649],[1.424648],[3.723725],[9.011290],[4.080646],[-8.554850],[-3.404615],[4.993509],[4.859587],[-1.700236],[5.757961],[-6.515123],[2.825652],[-8.630132],[-7.433827],[-7.059632],[-0.144125],[-6.123015],[-0.984517],[-4.609525],[-1.819497],[-6.202549],[0.864928],[-6.172071],[6.790590],[9.733533],[2.014616],[4.942815],[3.289946],[-2.621324],[0.632163],[1.023671],[-8.606482],[0.393672],[4.171196],[7.623601],[-2.867847],[-9.836311],[3.253076],[0.765773],[1.658594],[3.431903],[-7.545085],[-5.667255],[-5.233424],[-2.089421],[0.043883],[-8.426480],[9.538743],[-8.534775],[7.587190],[-8.061052],[5.442076],[7.903463],[-0.625286],[5.592694],[0.184680],[-9.591349],[0.952728],[2.235258],[8.998303],[4.596319],[5.097422],[1.810374],[6.422912],[-6.317401],[0.070101],[7.167744],[7.739292],[8.658415],[8.537483],[-6.815201],[7.778719],[-5.936628],[4.924745],[-6.584627],[7.462117],[2.163769],[2.588839],[-4.676165],[-7.912298],[2.413984],[9.003235],[-8.024838],[5.959059],[-1.222996],[-1.117867],[4.954228],[-7.442010],[-2.060506],[6.109156],[-5.594088],[-9.917478],[-1.527709],[-4.937886],[-5.844105],[4.178698],[-2.119982],[-5.227257],[8.056701],[-5.137482],[-7.737728],[-3.598138],[-7.181943],[-1.861235],[-0.450274],[-0.514279],[-5.275103],[-3.465994],[-2.956017],[4.980295],[3.754821],[4.995343],[-4.475865],[-2.217823],[7.568809],[4.552054],[7.345652],[-4.243591],[-0.561411],[-8.687174],[-8.759049],[-3.061809],[0.359167],[4.915598],[8.794242],[9.311821],[0.120694],[7.825014],[-0.904992],[-7.522156],[-5.312860],[-8.459139],[2.102810],[-4.728725],[9.740389],[2.843500],[0.015025],[-3.020152],[-6.806096],[-9.268248],[3.369512],[4.682319],[-1.819463],[-1.331439],[-1.343100],[3.185597],[-3.652402],[1.666896],[-9.591583],[-6.168612],[-2.906358],[6.151347],[8.165404],[7.471322],[-7.851883],[8.946397],[0.803606],[-0.900430],[6.261595],[-3.222490],[8.721131],[0.864796],[8.436910],[-3.972763],[-2.485728],[1.996825],[-8.133009],[-2.051693],[7.597132],[3.502479],[9.799613],[6.459183],[0.075253],[7.440921],[-5.288996],[7.516193],[1.151856],[2.336308],[7.203449],[-2.412791],[-1.249578],[-1.988274],[-3.462126],[-8.593259],[-1.835891],[4.921105],[9.667887],[-7.394601],[2.616706],[0.470643],[-5.548365],[8.093933],[3.785328],[-2.008357],[-9.992416],[-1.375743],[4.393418],[4.849816],[8.691447],[2.776907],[-2.802764],[-8.437682],[0.057262],[-2.120276],[-3.020388],[-6.098544],[-4.025033],[-1.751592],[-8.080617],[-4.110638],[0.576837],[-2.935578],[-0.978367],[-0.943279],[5.302020],[5.994480],[4.186694],[8.057854],[0.359106],[6.865319],[-0.410311],[-5.042171],[8.079258],[-3.003490],[4.570010],[7.702617],[-4.288986],[8.155743],[2.650048],[-0.448294],[0.708985],[-9.162757],[9.407680],[2.766916],[-3.616786],[-4.476802],[-2.310949],[2.130516],[6.976780],[-4.443086],[9.525741],[1.884867],[4.630037],[-5.521324],[3.329367],[6.713455],[-3.596818],[9.450977],[-1.068322],[-1.175600],[3.338322],[9.449422],[3.461571],[5.728393],[-5.218552],[-6.022507],[4.594025],[9.494635],[-8.767895],[-5.630219],[9.322944],[8.551640],[3.516322],[0.398533],[3.143496],[-7.901400],[6.939518],[1.937884],[1.749065],[0.235649],[-4.504615],[8.374169],[-2.355631],[-8.994039],[-3.638809],[-4.654959],[-7.710719],[1.858829],[-5.345467],[4.535106],[0.070081],[-6.218924],[3.201879],[5.341366],[-4.778780],[3.524528],[-7.924710],[6.187582],[6.772690],[-2.158535],[-4.517067],[3.907935],[-1.278770],[-5.864207],[-4.156353],[-8.966284],[-0.943414],[-8.353491],[-8.524717],[-9.712840],[-2.999358],[3.947402],[-2.264988],[8.203005],[-8.924145],[3.976571],[-0.726390],[-3.607536],[1.526180],[4.201043],[-4.509823],[7.735382],[-5.287194],[6.182171],[-6.605324],[-2.007950],[0.081367],[9.102296],[-3.771331],[0.565226],[-3.122446],[5.099399],[-6.894612],[7.255850],[-4.187297],[5.905032],[4.476666],[6.341031],[-6.466537],[-2.938704],[-9.402262],[0.180437],[5.311914],[6.688206],[-1.820433],[-6.654479],[6.797679],[9.282161],[2.332046],[-3.604545],[-8.780785],[3.996796],[-8.904101],[0.768528],[3.442276],[2.222735],[-2.272938],[8.339510],[-8.904421],[1.758970],[5.355655],[5.552220],[8.661863],[-0.628313],[-8.056755],[6.813629],[-8.838281],[-4.107060],[1.681233],[0.882895],[5.277481],[6.887980],[-1.129792],[6.667039],[8.681183],[7.214493],[0.687625],[-5.213074],[5.752620],[3.996092],[8.441328],[-7.065014],[1.392525],[-0.281645],[2.507969],[7.563962],[4.977877],[-7.359882],[7.550255],[-6.338917],[0.713753],[-4.588845],[-1.433338],[3.985361],[5.769507],[3.602580],[8.045996],[5.008418],[-5.720979],[-8.788015],[2.427684],[2.975209],[-8.774793],[-9.049739],[9.425149],[-5.124619],[-2.389396],[7.871863],[2.679041],[6.217024],[-8.925135],[4.283029],[-0.980556],[-5.731180],[1.533315],[-5.261322],[2.635413],[4.662098],[-9.966010],[2.880091],[-4.260148],[-5.971384],[-9.831427],[5.230856],[-4.029034],[4.536779],[-9.841667],[7.058985],[2.588991],[9.155394],[-3.243609],[5.694935],[9.541796],[0.174059],[4.743236],[-9.313796],[-2.451604],[-4.766693],[-4.109183],[5.793103],[-4.437361],[5.072576],[8.275120],[-0.637673],[3.391343],[5.314737],[9.133375],[5.448524],[1.124649],[-2.152862],[9.609323],[-8.006901],[0.254531],[2.794073],[0.758986],[4.818201],[5.106206],[-7.667893],[4.894527],[2.863888],[-6.028217],[-6.027993],[8.840695],[6.088217],[-9.342891],[9.773372],[-5.226071],[6.577010],[3.661211],[9.193988],[2.453854],[-3.638698],[-6.913462],[-3.880101],[1.157906],[-6.096977],[-4.610083],[-5.141581],[-1.642259],[6.509194],[9.970768],[-7.726506],[-0.136261],[-1.845646],[-5.496191],[-2.922528],[-6.756852],[-8.395899],[2.828564],[-1.226137],[-5.371182],[9.558266],[2.116822],[2.715575],[5.673912],[-1.171872],[5.419666],[-8.208891],[-3.278508],[7.933628],[-7.904823],[6.891085],[3.262029],[1.221398],[-3.878045],[9.542794],[-1.471269],[1.764485],[-8.469373],[0.679564],[2.649032],[6.285657],[2.905519],[1.641365],[-8.790212],[-7.096976],[-4.650241],[4.345722],[-3.313562],[2.271333],[-7.157415],[2.068767],[2.283605],[-6.739187],[2.854923],[7.769593],[2.257970],[-5.401141],[-7.580061],[-1.374202],[-5.549368],[9.987758],[-0.815449],[-8.541816],[-1.677191],[2.394086],[8.369186],[9.067427],[-0.737273],[-0.103760],[-3.919915],[-7.537063],[-7.793705],[-5.298107],[-0.436216],[1.585044],[3.180622],[-2.918847],[8.470344],[-5.040745],[-1.983793],[-3.796670],[4.123100],[-8.049438],[4.248955],[9.118604],[-9.199165],[3.478302],[-7.830787],[5.496756],[7.832731],[-7.772114],[8.444517],[-2.778960],[1.098971],[-6.063209],[5.034075],[6.491402],[6.838301],[-9.451950],[3.287809],[-9.601786],[6.047986],[-4.486623],[1.765948],[9.836546],[4.826195],[5.430234],[-1.618309],[2.327173],[6.748158],[3.839531],[0.465072],[2.078212],[-9.690207],[6.909314],[5.760297],[3.499970],[-2.505167],[9.252873],[5.203667],[-0.853562],[-5.102695],[6.128629],[6.711698],[-1.951921],[2.587713],[1.507923],[6.318578],[1.892855],[-8.777534],[3.647922],[-8.353593],[6.168278],[-8.099289],[-0.077865],[7.280717],[-5.106927],[-0.454904],[-0.338692],[6.588391],[-3.066992],[-2.039228],[7.335414],[-5.272382],[7.449398],[3.714172],[5.534745],[7.136818],[-5.725982],[6.815369],[5.293781],[2.629761],[-3.760134],[4.509704],[-5.678405],[0.709416],[3.712138],[-7.903842],[1.314401],[4.166175],[-2.505487],[7.273455],[-2.485165],[-8.918747],[9.802414],[5.923242],[-8.999901],[-9.271244],[7.107225],[2.053025],[-4.080907],[-4.120677],[-3.202778],[-9.650940],[-9.422282],[-6.056564],[3.476678],[-6.766034],[-2.486336],[-0.785976],[-8.650157],[-9.660078],[4.378877],[8.622453],[-5.351313],[-3.820831],[8.966535],[2.294351],[4.703109],[-5.718210],[8.284087],[-5.067969],[-9.208593],[8.423705],[1.609878],[-3.265528],[6.811931],[-7.242711],[-2.789067],[5.259087],[-4.930591],[3.188292],[6.156526],[5.614497],[5.370846],[-9.428231],[-0.568494],[4.227686],[3.565304],[3.186746],[-2.672817],[-6.613381],[-2.040552],[-4.201742],[-2.182888],[-7.067964],[9.057495],[-7.313444],[-5.775340],[-7.124072],[8.782429],[-7.875460],[1.016615],[4.956901],[-0.418359],[-5.867347],[-0.466188],[0.050630],[6.590772],[8.488427],[0.443764],[7.554569],[-8.544970],[3.773053],[3.834439],[-2.701244],[-1.964129],[7.223383],[-6.756267],[-9.729677],[3.523342],[7.657527],[7.746452],[2.346821],[4.616392],[-7.042532],[-5.161274],[7.397823],[-4.966133],[8.305152],[-3.454872],[-3.052411],[-3.346991],[4.040809],[-1.229585],[-5.130958],[-5.505374],[-0.361626],[-2.695154],[-4.352437],[-5.670370],[-3.895807],[-1.577516],[5.815123],[7.318638],[5.378749],[-6.689555],[-8.419901],[8.774056],[8.170728],[-7.388117],[4.522263],[-4.892249],[-2.137674],[8.716857],[-6.873376],[-5.166469],[-8.090158],[-8.926097],[6.368416],[-1.211546],[-9.558070],[-7.643516],[-5.907424],[-0.497256],[-5.675805],[7.026752],[4.213564],[8.332286],[-1.146515],[-1.495470],[-1.532583],[2.854926],[-4.669730],[5.196656],[7.859184],[-1.602686],[-9.814910],[7.418778],[-7.120165],[5.778432],[-2.699295],[-4.836671],[-5.651737],[8.751883],[3.337928],[1.960649],[-6.461544],[-4.813040],[-1.457502],[-2.648279],[-2.255604],[1.943639],[-0.350491],[1.132932],[-6.730212],[9.946178],[7.767586],[-2.898746],[4.433819],[-8.522080],[-5.527389],[-0.091657],[-3.505549],[6.849279],[-1.518017],[2.535752],[-9.437202],[-1.970283],[9.505169],[6.533777],[-6.358590],[-1.445576],[-6.030093],[5.959092],[-3.413603],[-3.878875],[7.136557],[-6.748572],[-0.565342],[-6.020140],[2.505311],[3.596732],[4.668916],[-5.715906],[6.275056],[-5.363202],[-6.041874],[2.576543],[-0.329113],[-1.266494],[-5.403930],[2.897919],[-4.235767],[6.149988],[3.466641],[8.398988],[3.601287],[-1.171112],[-3.229199],[6.304086],[-1.234592],[8.126012],[-5.063577],[2.452684],[7.848525],[-8.456054],[3.031575],[7.145637],[4.127140],[-3.965559],[6.286895],[9.279914],[-8.132783],[8.557873],[7.546713],[-0.285839],[-2.519212],[-8.947931],[-7.984591],[6.965862],[-9.363544],[2.214211],[3.316668],[5.597112],[5.671804],[6.253032],[9.124020],[-6.579382],[-9.644260],[2.492249],[-4.196068],[4.103643],[0.992394],[-8.914860],[-5.010446],[-1.021500],[2.279885],[-3.931330],[-1.799861],[6.226301],[1.319930],[-8.077885],[1.619304],[-8.987336],[-8.833134],[4.154681],[6.603974],[-7.428467],[7.402335],[-1.475279],[-9.232060],[-3.577759],[-3.555599],[2.187353],[-1.244916],[-3.758043],[2.099135],[-2.510655],[3.728040],[8.717568],[-3.430101],[3.933208],[0.064263],[9.671362],[-9.540158],[-9.135624],[-2.636438],[-5.738177],[8.542689],[7.474591],[-4.953191],[5.265977],[3.745662],[-9.856314],[-0.367003],[-7.496324],[0.751792],[-1.141158],[0.339055],[4.545300],[9.204784],[0.542382],[-8.560769],[-5.730737],[1.666200],[3.911229],[-2.588735],[7.887360],[-0.846120],[-8.231743],[8.206362],[-3.050135],[-5.338729],[-5.514584],[-9.046190],[5.790146],[9.333029],[5.366218],[-7.438885],[-4.035426],[9.234994],[9.931980],[-4.219705],[6.593068],[4.924342],[-5.400522],[6.209520],[7.157214],[9.988768],[5.198938],[4.583491],[-0.084889],[2.614594],[-9.845886],[4.151484],[9.770164],[-2.468300],[-7.165360],[-6.483038],[6.898391],[-6.558284],[-5.317873],[-7.650431],[5.167887],[4.498285],[3.947488],[-0.482957],[-9.928549],[4.959213],[2.219439],[6.810982],[-0.128638],[-3.144924],[-9.115530],[-2.334067],[-2.581428],[5.032970],[-3.746829],[-7.743754],[-9.754181],[7.789955],[-1.354550],[7.215992],[3.431973],[9.363476],[0.475427],[-6.295022],[-5.147390],[9.648475],[1.603388],[-5.483564],[-3.759438],[-1.971836],[-9.560147],[-6.125721],[5.640432],[-9.833159],[5.104181],[-2.310003],[5.201143],[-9.744310],[-3.727994],[-5.196492],[1.819453],[7.577109],[8.769045],[-9.203540],[-9.788063],[6.950670],[2.388807],[6.531904],[0.450275],[-9.483880],[3.188957],[3.362359],[-1.095947],[7.291671],[-4.726154],[6.508813],[6.493038],[-5.210818],[-2.894570],[-7.704516],[-6.527593],[1.912364],[-5.287422],[-3.725375],[3.357462],[-5.143937],[9.510879],[9.135627],[0.108640],[-2.339095],[-9.421652],[7.905469],[-0.550022],[-0.707274],[-6.849197],[6.854223],[-4.743620],[-4.470197],[4.514722],[-9.252486],[3.976331],[2.260883],[1.914477],[-8.465865],[-1.243983],[-3.629195],[-0.983124],[-3.688984],[-4.364593],[-3.426709],[-7.968554],[2.171648],[-2.121179],[8.066938],[-2.064830],[-3.358994],[-9.544952],[-8.180223],[-3.885032],[9.911611],[8.238797],[3.617179],[5.029118],[-0.129570],[5.462156],[3.145331],[4.000947],[-0.473585],[-1.634905],[1.177188],[-5.442808],[3.505493],[-6.417182],[-4.329552],[-0.931360],[5.774245],[7.618383],[-4.966814],[-0.441481],[-9.409576],[8.795437],[1.635922],[-9.816971],[-0.572340],[9.781008],[2.206971],[-8.624453],[1.379879],[-1.164037],[7.791924],[7.497628],[-0.175679],[-0.423942],[2.356721],[-7.368600],[-8.005058],[3.421285],[-2.308824],[6.488819],[7.941840],[-9.312670],[-1.692845],[4.564459],[6.337587],[0.611935],[-4.059451],[1.580782],[-1.543802],[3.785864],[7.640955],[5.008293],[6.873208],[9.477017],[1.751630],[6.356525],[-4.090256],[1.269124],[-4.998416],[-6.925921],[0.270451],[-1.686467],[-2.689269],[-7.659300],[0.719800],[-6.227221],[0.515919],[-9.860366],[2.967326],[-6.928148],[6.495614],[5.091381],[-0.516152],[-1.386112],[3.970864],[-0.605119],[3.205667],[-3.817970],[4.936803],[-4.112638],[5.458052],[4.265045],[-9.406427],[9.330972],[0.674799],[-2.393268],[7.135378],[-0.128134],[8.311670],[-6.619284],[5.372088],[0.177453],[-8.978272],[-8.061589],[-4.177317],[-9.914368],[-1.264836],[3.451437],[-7.702491],[-8.270456],[-6.033519],[-6.940237],[-3.464969],[9.971949],[6.084377],[-6.710184],[0.238563],[3.991046]], dtype = "float64")#candidate|4298|(2640, 1)|const|float64
call_4297 = func_1146_call(relay.reshape(const_4298.astype('float64'), [16, 15, 11]))
call_4299 = func_1146_call(relay.reshape(const_4298.astype('float64'), [16, 15, 11]))
bop_4300 = relay.bitwise_xor(const_4298.astype('int32'), relay.reshape(call_4297.astype('int32'), relay.shape_of(const_4298))) # shape=(2640, 1)
bop_4303 = relay.bitwise_xor(const_4298.astype('int32'), relay.reshape(call_4299.astype('int32'), relay.shape_of(const_4298))) # shape=(2640, 1)
uop_4313 = relay.sqrt(bop_4284.astype('float64')) # shape=(5, 8, 2)
uop_4315 = relay.sqrt(bop_4287.astype('float64')) # shape=(5, 8, 2)
func_2378_call = mod.get_global_var('func_2378')
func_2380_call = mutated_mod.get_global_var('func_2380')
call_4318 = relay.TupleGetItem(func_2378_call(), 1)
call_4319 = relay.TupleGetItem(func_2380_call(), 1)
bop_4323 = relay.floor_divide(bop_4284.astype('float64'), relay.reshape(call_4318.astype('float64'), relay.shape_of(bop_4284))) # shape=(5, 8, 2)
bop_4326 = relay.floor_divide(bop_4287.astype('float64'), relay.reshape(call_4319.astype('float64'), relay.shape_of(bop_4287))) # shape=(5, 8, 2)
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_4328 = relay.TupleGetItem(func_3712_call(), 1)
call_4329 = relay.TupleGetItem(func_3713_call(), 1)
func_3672_call = mod.get_global_var('func_3672')
func_3674_call = mutated_mod.get_global_var('func_3674')
var_4349 = relay.var("var_4349", dtype = "float32", shape = (90,))#candidate|4349|(90,)|var|float32
call_4348 = relay.TupleGetItem(func_3672_call(relay.reshape(var_4349.astype('float32'), [3, 30])), 1)
call_4350 = relay.TupleGetItem(func_3674_call(relay.reshape(var_4349.astype('float32'), [3, 30])), 1)
uop_4354 = relay.cosh(const_4298.astype('float32')) # shape=(2640, 1)
func_3069_call = mod.get_global_var('func_3069')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_4358 = relay.TupleGetItem(func_3069_call(), 0)
call_4359 = relay.TupleGetItem(func_3070_call(), 0)
func_689_call = mod.get_global_var('func_689')
func_691_call = mutated_mod.get_global_var('func_691')
const_4361 = relay.const([0.083665,8.381051,8.319651,-1.019156,-8.168062,3.845775,-2.901582,6.231348,-2.745795,3.492506,-5.567274,-7.288787,0.059812,-9.316091,-7.371622,-9.399014,-8.999446,5.665748,6.464507,-3.212678,7.091925,-9.861047,-7.354486,-1.541042,5.553922,-5.817570,-8.215959,5.178567,-7.842313,-5.024988,7.817491,-9.162051,-3.766967,0.580095,-9.865138,2.637512,3.746588,4.871913,-1.056486,1.893110,1.965814,0.637164,-8.742205,-6.237551,-9.916491,4.905003,5.918040,6.941009,0.812010,7.127931,-6.631543,-6.185076,6.664144,-9.753258,3.211135,9.117371,2.362223,-5.736990,7.498859,-1.844923,0.044216,5.124158,-8.515476,-2.545228,5.488069,9.427733,4.587328,6.921295,7.196735,-7.898021,1.905414,-8.977824,-3.889567,-8.730709,3.563799,8.251542,8.633612,0.994632,8.578964,4.622636,-7.268763,-2.561188,-4.333379,-7.959995,7.991010,-7.578667,-3.293193,7.369741,6.821163,-7.208852,5.624342,1.833054,-7.553355,-2.732143,4.361117,-9.475904,-8.169236,8.194947,-8.224252,-8.711512,-2.334697,8.299984,9.500591,3.473452,-3.396937,6.526498,3.818343,-5.681112,-9.315674,3.474813,7.557389,3.171600,-2.056432,-9.813749,-7.676871,5.984149,-5.597765,7.147622,7.374181,-6.753846,-5.082407,4.044724,5.251337,1.550245,-8.696127,2.150248,-7.970906,2.854721,0.151893,2.976746,9.140029,-5.166499,9.778748,8.681049,-8.923011,6.137539,-3.172185,-1.929635,-4.421393,9.965387,-4.529758,-7.629261,0.376376,2.815550,-8.755016,-9.772482,0.168965,7.364526,-7.989006,-8.652024,-2.700951,2.650229,-7.230575,-0.805012,0.605861,-3.433045,-0.917535,-1.817440,-4.343625,-8.880115,-0.885207,-2.264090,3.456244,6.412880,7.001992,-1.095271,7.414628,-3.793033,5.665727,-2.411904,-9.824650,-8.191438,-3.662260,-5.842778,3.356988,6.428364,4.310665,3.352110,4.622062,-7.984081,-3.666391,-8.595608,-8.706369,-4.898391,-5.096313,-6.381719,7.128471,2.298174,1.826619,-9.924781,2.708085,-1.432766,-5.380647,9.150644,-6.664755,-3.340781,6.838908,-7.282351,6.427741,5.212157,-0.268488,-2.537603,9.993921,9.917932,1.264291,5.993337,4.677473,7.559971,7.648357,1.254108,-9.757041,0.128726,-9.080472,7.525754,-7.527002,4.460999,-4.961257,-3.839789,-6.648352,-5.603175,4.072681,-3.961197,0.767317,-2.312895,-5.443153,7.160825,4.077684,-1.515333,-9.719256,1.206407,6.028440,9.887440,-1.486970,0.172558,5.717761,-0.376813,0.899526,6.496158,-9.326064,5.371729,7.937071,0.715547,0.556421,1.679369,6.719372,-3.631322,0.022330,-4.056603,5.360824,-1.081385,2.042230,-2.833478,0.338276,-2.134041,6.987910,0.510483,-4.580649,-7.744655,-3.504523,8.450454,-6.031755,-4.866767,-7.675024,-5.502285,-7.298353,-1.482723,5.024314,-9.450384,7.597429,0.120093,8.265099,5.076611,4.510028,6.386662,4.472834,-4.622905,5.190611,-2.499469,4.663425,1.403159,1.609100,-4.715643,-0.875949,-2.015961,4.136203,1.876651,-9.767582,-3.521681,-0.278989,0.264473,-2.217598,6.120643,6.447911,8.674123,-8.560581,-9.235059,2.523768,1.802155,-2.908263,6.334289,4.903473,-8.799010,0.984530,0.536876,-7.548722,-7.964068,-7.141085,-0.008621,2.911151,1.143156,1.468450,0.777775,-4.113368,-3.706066,-1.586073,-2.374201,-2.831851,4.252841,6.418221,1.534344,-5.386316,-4.431984,-6.351282,-1.247900,5.236454,1.737124,2.043757,5.459745,9.774744,-5.058150,8.688722,5.663096,9.502608,1.788247,-5.788953,3.136619,-1.496480,2.486003,-8.098506,-8.239512,4.085025,-6.402925,0.052831,-9.791867,-7.989591,-1.454934,6.461542,7.336088,0.118306,1.286193,-3.212556,-4.254413,4.906216,6.471883,5.395943,4.281893,6.226903,6.967375,6.574044,-4.883589,0.299148,8.785179,-6.265863,2.763111,6.206052,2.758341,9.216512,8.095136,-8.948360,5.602396,-5.127086,-9.282785,-7.981861,-8.697445,-3.857436,7.238625,-7.582999,-5.714129,-5.490303,-5.107888,6.650520,6.079711,8.531426,3.265084,2.645860,7.727414,8.261711,9.143631,7.382117,8.613590,-9.230093,4.905615,5.574236,-7.714549,-2.027213,3.864448,-9.814808,-0.512355,3.219746,9.717044,-2.838391,8.577922,4.552769,-7.873135,-2.664963,-7.131261,-6.960735,5.027283,9.215408,2.207693,-2.115938,4.098966,8.195464,-7.959185,3.951670,0.460300,-3.639439,6.675506,-2.343561,1.928045,2.650804,8.737492,2.691359,7.472290,-9.457701,-2.077387,-3.704349,-0.673690,-2.197682,-8.102623,-2.468761,8.745072,-4.918562,-1.670365,-9.062103,-6.051678,2.555969,-9.204494,-1.347679,-9.520492,-5.079353,-5.130057,-3.103867,5.898119,7.815715,4.601640,8.941326,2.962516,4.399218,-2.947717,2.460469,-1.110738,3.008946,0.855042,-3.242039,-5.806722,2.967793,3.537937,6.340162,-0.727080,8.739324,7.429968,-4.500034,-1.106082,-8.091996,-2.710448,4.563000,6.980889,8.169923,9.833243,-9.317922,-9.326788,-4.890640,3.700958,-6.204151,-1.688427,2.750972,4.602260,-9.783585,-0.263683,-1.556527,-9.866081,2.395728,-4.613406,6.284988,-3.809118,-9.229544,8.830550,1.709197,-2.842811], dtype = "float32")#candidate|4361|(490,)|const|float32
call_4360 = relay.TupleGetItem(func_689_call(relay.reshape(const_4361.astype('float32'), [7, 10, 7])), 0)
call_4362 = relay.TupleGetItem(func_691_call(relay.reshape(const_4361.astype('float32'), [7, 10, 7])), 0)
output = relay.Tuple([bop_4300,uop_4313,bop_4323,call_4328,call_4348,var_4349,uop_4354,call_4358,call_4360,const_4361,])
output2 = relay.Tuple([bop_4303,uop_4315,bop_4326,call_4329,call_4350,var_4349,uop_4354,call_4359,call_4362,const_4361,])
func_4363 = relay.Function([var_4283,var_4349,], output)
mod['func_4363'] = func_4363
mod = relay.transform.InferType()(mod)
mutated_mod['func_4363'] = func_4363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4363_call = mutated_mod.get_global_var('func_4363')
var_4365 = relay.var("var_4365", dtype = "uint16", shape = (5, 8, 2))#candidate|4365|(5, 8, 2)|var|uint16
var_4366 = relay.var("var_4366", dtype = "float32", shape = (90,))#candidate|4366|(90,)|var|float32
call_4364 = func_4363_call(var_4365,var_4366,)
output = call_4364
func_4367 = relay.Function([var_4365,var_4366,], output)
mutated_mod['func_4367'] = func_4367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4277_call = mod.get_global_var('func_4277')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_4385 = relay.TupleGetItem(func_4277_call(), 1)
call_4386 = relay.TupleGetItem(func_4278_call(), 1)
var_4395 = relay.var("var_4395", dtype = "bool", shape = (2, 12, 13))#candidate|4395|(2, 12, 13)|var|bool
bop_4396 = relay.less_equal(call_4385.astype('bool'), relay.reshape(var_4395.astype('bool'), relay.shape_of(call_4385))) # shape=(2, 12, 13)
bop_4399 = relay.less_equal(call_4386.astype('bool'), relay.reshape(var_4395.astype('bool'), relay.shape_of(call_4386))) # shape=(2, 12, 13)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
const_4401 = relay.const([4,8,6,-9,-4,-1,-3,-10,3,-4,-6,10,-3,-6,-8,6,8,-8,-5,-5,-5,-2,1,5,-9,1,-3,-5,-5,7,-1,7,-9,4,-4,-3,-5,5,4,-2,-8,10,-3,2,-7,-5,-4,-8,7,-6,-8,8,-5,-9,-7,-4,3,8,9,8,-9,-2,3,-5,-1,1,-2,-5,4,-6,7,5,3,10,5,10,2,6,-4,-6,-2,4,-6,10,5,2,-7,-5,-2,4,4,-1,6,2,8,4,-4,3,9,3,-1,-7,-4,9,-7,5,-7,-8,4,2,7,-2,-4,3,10,9,-3,-10,-9,4,1,9,-6,2,8,-1,-10,10,-2,9,-10,-5,-5,9,3,-1,-1,-4,-1,6,-10,6,2,6,-8,-5,-3,1,-3,-3,-2,-3,-7,9,-5,9,1,-7,-1,6,10,-10,-10,-1,3,-3,8,-7,5,3,2,3,-7,-6,-5,-10,4,6,-4,10], dtype = "int64")#candidate|4401|(180,)|const|int64
call_4400 = relay.TupleGetItem(func_1602_call(relay.reshape(const_4401.astype('int64'), [180,])), 10)
call_4402 = relay.TupleGetItem(func_1604_call(relay.reshape(const_4401.astype('int64'), [180,])), 10)
func_1730_call = mod.get_global_var('func_1730')
func_1732_call = mutated_mod.get_global_var('func_1732')
call_4412 = func_1730_call()
call_4413 = func_1730_call()
output = relay.Tuple([bop_4396,call_4400,const_4401,call_4412,])
output2 = relay.Tuple([bop_4399,call_4402,const_4401,call_4413,])
func_4423 = relay.Function([var_4395,], output)
mod['func_4423'] = func_4423
mod = relay.transform.InferType()(mod)
mutated_mod['func_4423'] = func_4423
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4424 = relay.var("var_4424", dtype = "bool", shape = (2, 12, 13))#candidate|4424|(2, 12, 13)|var|bool
func_4423_call = mutated_mod.get_global_var('func_4423')
call_4425 = func_4423_call(var_4424)
output = call_4425
func_4426 = relay.Function([var_4424], output)
mutated_mod['func_4426'] = func_4426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_4436 = relay.TupleGetItem(func_3129_call(), 2)
call_4437 = relay.TupleGetItem(func_3131_call(), 2)
output = relay.Tuple([call_4436,])
output2 = relay.Tuple([call_4437,])
func_4448 = relay.Function([], output)
mod['func_4448'] = func_4448
mod = relay.transform.InferType()(mod)
output = func_4448()
func_4449 = relay.Function([], output)
mutated_mod['func_4449'] = func_4449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4093_call = mod.get_global_var('func_4093')
func_4094_call = mutated_mod.get_global_var('func_4094')
call_4471 = relay.TupleGetItem(func_4093_call(), 1)
call_4472 = relay.TupleGetItem(func_4094_call(), 1)
func_3021_call = mod.get_global_var('func_3021')
func_3024_call = mutated_mod.get_global_var('func_3024')
const_4494 = relay.const([-7.489787,0.951562,1.615830,5.252738,-9.848489,1.779774,7.702498,-8.317213,-5.656286,8.513245,0.238575,6.659759,2.695929,8.508412,4.027814,4.566268,-3.187155,-1.747173,-1.691301,-5.280245,4.956128,-2.296804,-6.350052,6.522739,4.100662,6.184020,-3.379958,4.901225,4.170740,-7.404564,0.376048,-9.790453,-5.708072,-0.704182,-4.732103,-6.154291,-4.212904,6.384191,8.383704,5.388467,8.513060,2.894936,0.171630,7.506272,4.312985,1.580744,2.461146,-9.252807,9.863716,-8.630526,3.797056,1.139721,2.884218,8.258801,2.557205,2.009131,2.647553,-6.971224,-5.054660,-3.718802,7.354945,-2.575462,6.788477,8.460709,0.123091,0.544855,-4.237872,-2.397877,2.097973,-0.632676,-8.407285,0.338533,5.530925,2.743940,9.909874,4.774317,6.501673,-4.997899,5.789664,8.415270,4.920100,8.778608,0.832326,-6.155509,3.661544,-4.234161,-4.774914,-0.355018,1.485176,1.399281,4.132602,-0.363030,8.838687,2.121091,-2.205093,5.581427,0.900399,3.600717,7.828595,5.473962,-4.418030,-0.512007,4.921957,-9.499994,-3.325725,-2.584026,3.003581,6.890539,7.667193,9.975860,8.852720,5.065474,3.832788,-0.120714,-9.932998,-5.539980,4.926942,-1.817357,2.646610,9.727165,-6.959479,4.497084,-3.437391,-5.930391,6.288233,9.520816,2.117698,-4.415939,3.864940,3.190655,-5.455280,3.920118,-8.501919,4.599965,-7.590225,-8.381428,-7.931702,-0.860417,-5.038553,-4.251808,-7.724781,-8.239812,-4.336155,4.692090,3.986480,-8.169932,-6.236895,7.258030,9.191631,-2.722617,-3.107711,-2.591876,-8.169401,1.752782,-3.947102,-0.443740,-5.942513,-9.934182,5.632909,-7.878685,-2.191327,5.453778,-0.990483,3.929772,6.787226,-1.512041,-7.562234,-9.745701,5.914227,5.737405,6.816716,0.242086,4.189536,-8.614567,1.540402,9.906926,2.325768,-0.162056,-1.997627,2.961135,2.106176,5.294518,4.415441,-4.178713,3.106011,-2.412932,6.186297,-5.310836,3.569391,-7.816521,-9.667396,-1.086969,-8.513465,7.941031,-2.262769,-6.610757,-1.847832,-6.399728,1.302741,3.263980,-2.371929,0.286672,5.386521,-1.922665,-7.327250,7.130994,5.501242,0.116856,-2.440818,-8.623033,8.726887,-8.168075,-2.829980,8.883713,2.610605,-3.332063,-5.565636,9.420321,-9.448595,-7.689969,-2.990856,6.095646,2.139847,9.087765,2.623547,9.595853,-6.025429,0.266116,-7.092890,-6.108333,3.802356,8.274571,-4.124792,0.856837,7.635319,-4.282293,6.817788,3.283712,-3.403183,-4.442721,-3.531398,-4.989405,3.087019,9.293429,1.764212,9.932569,-2.751071,-2.840320,3.300294,0.147047,-4.897064,5.964077,2.965730,-2.472368,4.719863,-6.154992,-3.587849,1.547630,-0.273313,5.235701,-0.242989,-9.110656,-9.736678,-3.567576,-9.289298,-6.791034,0.268270,-2.727102,-9.459673,-8.512186,8.869543,8.998056,4.591889,7.235474,4.498737,1.418012,1.813867,-9.722016,3.024851,8.176110,8.204700,-0.200599,7.544958,0.436433,3.175068,-5.101639,-8.750967,8.031463,-0.957743,2.573455,2.848334,9.405111,-6.019865,-4.332581,-0.910881,9.217102,2.373473,-0.943093,-9.837618,-5.582687,3.508584,-9.794199,-3.665097,-4.582071,-1.454227,-8.056915,-9.373535,-3.503253,-1.860318,-4.981095,7.698457,-7.641164,3.497900,4.314343,-8.354790,-5.862800,-3.240550,-4.660538,-7.638315,4.272537,-0.870470,-4.716561,-8.825235,-8.995404,-5.060844,1.598333,-7.363129,-6.188492,5.875165,-9.995193,-9.583642,8.847194,2.382716,4.318806,-7.460035,1.782044,9.378170,-2.227501,-6.937260,-6.854436,1.755010,-2.119132,4.080110,-6.889589,2.562365,-3.092699,1.272278,-0.372151,1.738952,-4.132407,0.301223,2.435123,7.040536,-2.265406,-5.378291,-3.505220,-5.009779,4.288468,-1.321854,-9.721920,-0.048663,6.864571,0.303690,4.032423,3.789731,-0.903969,1.267457,3.223263,8.423349,-2.229059,-7.139096,-0.790869,-1.434848,-4.520187,8.334924,-7.610789,-2.880977,3.780933,1.778062,-2.820047,-1.608251,4.859349,-3.017651,-6.252207,-2.630061,4.816605,-2.056129,-3.066840,-5.284941,6.243482,3.353559,3.925856,5.356034,9.279973,0.209425,7.779065,6.544833,8.908501,-6.684565,5.246718,1.340884,2.709767,-9.347303,-8.201382,2.915246,-9.183139,0.362702,-5.907285,-6.394870,1.555741,7.057888,3.490928,-7.413185,1.324754,5.246639,4.655912,0.624504,-1.479740,-7.297628,-6.552791,-6.989496,0.352042,2.117540,-0.288813,6.946061,5.381237,-1.754778,4.530218,-2.420446,7.951549,-0.928703,-2.046752,-9.753528,5.199513,0.480474,-5.044302,3.610600,0.688073,1.744348,-2.274710,3.549236,2.873797,6.714400,-9.289715,1.146562,0.386303,5.545918,-5.518817,-8.703328,-4.843549,1.183776,3.547059,-0.132721,9.905558,-5.153295,8.166458,-0.867946,4.607294,2.815522,4.317331,-8.899794,-4.870318,-6.719447,4.413268,4.509566,-8.954961,-3.870514,3.663834,-3.016794,-3.984994,-0.093374,-4.360557,-6.404012,-9.728722,-7.270600,5.201054,-1.605434,-3.171225,-8.362409,0.675535,6.895916,-2.336727,5.399077,5.711866,2.655609,-9.086864,1.286958,-4.949705,1.500615,9.246802,-4.930418,-2.318625,4.152191,7.842287,-2.143518,2.449429,-8.823639,5.036439,4.171166,2.600901,-2.060981,-1.402749,-3.782444,8.237570,-3.340185,3.614169,0.450630,5.533989,-3.041233,-2.710052,-2.399962,8.269977,-8.980822,-1.697473,1.612245,-6.143260,-8.832082,5.010989,4.864881,-6.976109,3.212748,-3.022121,1.542602,1.168710,-8.622177,-3.952079,1.022702,9.200155,-6.231886,0.382457,7.322609,5.106682,8.748786,-5.638191,5.352167,-7.706502,0.077669,-2.176745,-7.966609,-2.071939,5.550710,9.692165,-4.711801,-9.275040,2.487614,-2.932453,1.449786,-1.985265,-6.512372,4.012549,1.059351,3.868597,-5.561797,3.835952,3.145170,7.276961,-0.213516,-8.334788,5.349538,6.652007,-8.900461,2.836012,5.399482,-8.509615,0.853932,4.238265,7.442574,6.839085,-9.005030,9.583787,-4.027392,3.635319,3.660680,-3.569506,-6.457901,5.980701,8.739804,8.745982,-2.581195,0.719560,2.763335,-5.697279,2.959110,5.878653,-2.133099,3.862269,5.699724,4.729017,-1.980959,-3.876602,8.056161,-9.537918,-2.988393,4.129625,0.441116,-8.016995,-8.345969,-3.674596,-2.140639,4.442574,-7.790131,-2.152648,5.738871,-6.630316,8.860500,5.689292,6.873675,8.923696,9.399781,-6.388989,4.238695,6.158631,-5.458871,4.914247,2.289204,1.952120,-6.044409,-1.004194,-5.357134,5.327322,2.480256,-2.796951,-5.552667,-3.264323,5.239243,6.834979,-1.529676,-7.174743,-4.300443,5.351816,-0.188639,4.540587,-3.884187,1.640691,-3.789228,-9.122255,4.796591,-3.476071,5.748294,5.656978,-7.589273,6.460792,3.181952,9.053551,-5.743050,-4.603815,3.118218,2.012403,0.397505,-7.715605,2.516716,7.515969,-0.467144,7.941590,-5.921960,-9.862787,1.039123,5.621831,2.460378,-9.654561,-6.903739,-6.949165,-9.224004,9.952544,-7.677496,9.527223,8.320726,-4.397529,3.871256,7.602921,-8.224955,-3.655763,6.398821,0.286920,-2.987530,-9.289798,-9.758075,-7.867078,-6.275303,-6.647690,-0.104790,0.100017,-4.436764,7.392224,2.931712,8.482152,-0.689926,7.384656,-7.863864,-5.318459,-0.282621,8.250807,8.645589,3.330723,6.755241,4.927724,7.494981,5.050212,-8.469082,9.781710,3.987234,-1.879065,-9.655012,-9.209938,-0.484788,5.821760,5.785215,3.852672,4.806858,5.347412,-4.578834,-9.635704,6.779287,0.891239,-3.969897,1.781777,2.805471,1.725328,6.363439,-5.655386,-1.813929,-1.575737,-5.708864,-4.979808,-4.573937,7.124133,-6.747525,-4.788684,1.629539,-7.731748,7.799409,-6.640030,3.393814,-9.572762,4.493895,-4.898450,7.451601,6.511561,-0.176488,6.884098,3.571420,9.449784,-8.300959,8.702421,0.024243,0.066820,5.970457,9.432595,8.372342,0.073439,1.841923,-4.963294,-7.993133,-9.942275,7.359734,7.080651,-4.780876,7.467287,3.815074,5.603149,-5.726692,8.092275,-5.691167,-8.618266,-2.152692,-2.723815,8.243522,-7.972918,-0.907230,-5.059103,-1.976613,4.944224,-6.470230,8.650069,9.190485,-8.418485,3.471813,-2.509095,-0.095292,4.105667,-8.274268,-1.045753,-4.444819,-1.553374,-1.045440,1.811029,-8.972866,9.287993,4.711352,-0.800742,0.502285,-8.100433,-9.348377,-8.823090,6.846566,-4.306777,2.055340,6.696769,9.202286,8.069571,-0.376234,5.695285,1.984078,5.442941,5.359724,8.874391,-9.168317,-6.884216,-3.486259,5.700384,-7.546843,-7.222433,9.503597,-0.526984,2.546770,-7.174745,-6.391978,-6.294215,-5.840782,-9.743683,-7.912208,8.137187,8.165039,3.033383,-2.106940,8.999178,-1.302831,7.350136,5.314582,6.755639,0.532307,-8.074364,6.227653,8.998489,-4.343694,1.977206,8.946724,5.784770,-2.605908,5.949353,9.589637,-0.091327,-1.721437,6.001441,8.934201,-2.048939,-3.800228,-4.726688,0.310891,-1.095572,5.351737,-5.292313,-1.658495,9.893663,3.975723,2.368380,7.451204,-1.395259,4.864789,1.059367,-1.540220,8.957658,-5.875756,-8.671723,5.463207,9.689214,2.066561,-6.549438,7.102014,-7.918619,-1.309555,2.161606,5.489958,5.669763,-5.229092,2.204854,-8.554275,3.279180,-0.027100,-4.139202,-6.844096,-9.906512,-4.123650,7.354260,-7.828940,-6.719441,-5.370223,-2.454029,1.110038,-9.689329,-5.415793,8.485244,9.404646,2.266822,-6.795782,6.609922,3.143198,-9.881597,-6.058207,8.274880,-9.440501,2.554494,-7.900189,-7.589877,6.564809,6.786292,2.080838,-6.025384,1.597172,-6.520904,-3.752096,0.325826,-9.281763,3.903551,6.172348,7.368754,-5.415855,-5.402073,6.501218,-0.877942,-7.122964,-3.113272,-5.209122,-9.505239,1.807288,-1.000887,-0.086717,9.967982,1.477512,-7.023901,-2.248678,-4.708546,-9.973212,8.917164,-1.137917,2.909163,3.139175,-2.458210,-7.901012,6.369216,0.468888,0.937686,1.902902,-3.643473,4.140676,-2.794532,4.415331,-0.316207,8.891643,9.814754,-8.344793,-4.456091,-4.596760,8.389221,7.737793,-5.295017,-4.729118,0.718551,0.316627,4.842209,-3.836179,-3.401882,-2.392304,1.881717,-1.388437,9.899968,5.913003,-5.409921,-9.803147,1.793892,-8.675889,2.134554,1.963181,5.900593,-0.775457,-7.504911,-7.388372,-4.109052,5.941054,-7.402386,-8.028800,-9.869189,-0.673856,-2.309144,6.251669,-4.453861,9.543480,-7.580595,-4.479827,7.344567,-2.085609,6.947975,-0.263443,-0.693500,-5.590461,6.352197,-5.019059,-2.116466,-2.900448,-2.837066,-1.015931,-6.806246,-5.808282,1.921212,-5.193431,2.542768,-9.086565,6.129029,7.777931,-4.618874,-3.250834,-8.904696,-6.541213,1.604542,2.652026,-8.821425,0.611532,-4.552336,6.471199,-9.018190,-7.871921,2.808751,0.614400,-9.767398,-0.893554,-5.276407,-6.100453,2.710999,3.270041,-1.693259,-8.735937,9.704018,4.895235,8.379780,9.445343,-7.261522,-9.126922,-6.241451,-5.093857,-2.158171,5.860722,7.129445,7.433838,-0.183149,-2.905409,-8.075591,2.003833,-4.557915,0.713221,-7.166301,4.576703,-1.706799,-0.101315,6.483415,0.786482,4.830294,-6.600115,8.086621,5.298366,5.653245,-3.749934,4.203793,0.800068,-8.627377,1.566339,9.634835,0.228652,-5.085959,-1.960824,-7.378099,4.124789,-0.323300,-8.192379,-8.664704,-4.106222,4.755070,0.173104,-1.607153,-9.059808,9.196665,8.182482,3.784960,-6.034019,-8.736227,4.792734,1.895308,-8.905310,8.183743,1.176215,1.948779,0.781731,-0.798918,0.078590,7.414739,6.009473,0.644341,4.429566,4.237428,7.119588,-0.197631,-0.888589,5.232755,9.089327,2.197620,-4.670900,-0.076235,-5.278340,-7.464168,-4.042673,9.742954,-8.032973,-0.733666,2.264682,-6.065860,-6.925115,-0.142640,-0.671158,1.584743,-1.781217,-9.232318,1.027180,-7.758860,8.618671,7.958379,-6.786929,2.382781,-9.108794,-9.523929,0.536366,-6.695684,6.440098,-3.727949,-4.455818,4.089604,-8.989743,-6.777693,9.815446,7.338588,4.399754,-7.445884,-9.269280,9.195617,3.369324,-7.286263,-6.354842,-6.995676,0.585242,7.011817,2.381216,-9.948383,-6.106716,7.620718,1.313601,-6.230060,-5.957615,-1.355720,-2.484006,0.730370,2.228331,-0.753228,-0.014080,9.433526,6.457022,8.751932,-1.345693,-6.064806,-4.081119,-0.681546,2.158880,0.177759,0.699866,-1.280317,9.339854,4.622937,5.574421,-9.469346,0.410486,-8.647374,-0.572374,8.924762,8.404463,7.234963,0.055407,-8.472635,-5.737431,-8.166168,9.528469,0.870618,-5.847385,-2.755544,-6.549989,7.542254,-1.069390,-5.836618,-8.620887,2.329049,9.201574,0.786104,-6.730892,1.276851,5.311132,-1.434712,-9.312067,2.532800,4.676932,1.854589,-5.177637,5.875330,-0.648250,1.247853,7.823899,-0.737699,6.099878,9.830986,7.497540,-2.914692,2.266542,-9.840302,-5.712516,-6.038031,0.812919,3.813733,1.555044,-5.015590,-4.265258,-1.241377,2.991939,1.459101,-3.658118,-2.626377,0.792115,0.639398,-7.595772,0.357740,7.312488,-5.256638,1.883330,2.284852,-2.476766,-1.361919,1.457468,-8.057999,4.558173,-0.353857,-5.154766,-9.703409,1.355377,-9.102348,0.691343,0.037790,-0.393782,7.472674,2.214397,-2.945272,-9.709156,4.141677,3.580684,-9.698522,1.018436,-8.077868,-8.227678,8.272601,-5.438277,8.544338,7.480281,5.365247,-5.895460,1.395457,2.641175,0.460539,-7.136406,9.812624,-1.787284,3.071106,-9.954718,0.220940,-3.376026,3.839044,6.441417,-2.660437,9.469480,-4.391359,-1.191451,6.847638,9.643753,4.779386,3.502358,6.313666,7.677041,0.851989,-1.607401,-0.967908,-6.495845,-4.359852,-5.539498,-3.457979,-5.083508,5.567506,0.527894,-7.933100,1.912605,-1.872842,-5.102111,-5.539392,-8.269238,-3.592594,-6.516249,8.407691,-3.296375,-7.305772,-7.833071,-5.508506,9.784812,4.372345,-4.548723,0.906064,-9.695874,7.971562,6.906476,-9.676052,0.004941,4.843531,3.989280,-0.648087,-4.981786,-9.948929,-1.112841,9.979516,-7.886142,-5.203349,-4.595416,-2.945256,6.524629,2.060220,5.095123,5.394817,-1.196892,-4.030882,5.437068,3.336643,-8.816298,7.675682,-6.868505,-9.614541,8.223916,-8.038583,0.946990,-9.129628,-2.317036,1.907270,0.290268,-3.015970], dtype = "float64")#candidate|4494|(1352,)|const|float64
call_4493 = relay.TupleGetItem(func_3021_call(relay.reshape(const_4494.astype('float64'), [8, 13, 13]), relay.reshape(const_4494.astype('float64'), [8, 13, 13]), ), 0)
call_4495 = relay.TupleGetItem(func_3024_call(relay.reshape(const_4494.astype('float64'), [8, 13, 13]), relay.reshape(const_4494.astype('float64'), [8, 13, 13]), ), 0)
uop_4543 = relay.asin(const_4494.astype('float64')) # shape=(1352,)
output = relay.Tuple([call_4471,call_4493,uop_4543,])
output2 = relay.Tuple([call_4472,call_4495,uop_4543,])
func_4548 = relay.Function([], output)
mod['func_4548'] = func_4548
mod = relay.transform.InferType()(mod)
mutated_mod['func_4548'] = func_4548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4548_call = mutated_mod.get_global_var('func_4548')
call_4549 = func_4548_call()
output = call_4549
func_4550 = relay.Function([], output)
mutated_mod['func_4550'] = func_4550
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4560 = relay.var("var_4560", dtype = "int64", shape = (5, 3, 1))#candidate|4560|(5, 3, 1)|var|int64
var_4561 = relay.var("var_4561", dtype = "int64", shape = (5, 3, 10))#candidate|4561|(5, 3, 10)|var|int64
bop_4562 = relay.maximum(var_4560.astype('int64'), var_4561.astype('int64')) # shape=(5, 3, 10)
func_584_call = mod.get_global_var('func_584')
func_586_call = mutated_mod.get_global_var('func_586')
const_4566 = relay.const([0.824939,-6.296420,-3.600508,6.979717,4.668093,-4.906950,-7.715368,6.322618,-9.507138,-4.635854,8.388501,5.851362,9.243962,-1.171690,0.917381,3.555080,9.455445,7.451130,-1.961688,7.392192,-1.566494,-3.027490,-3.796147,8.522940,-7.573374,-9.077187,9.067619,-7.809635,-4.637451,4.867624,1.620171,2.657221,-3.810582,-3.714656,7.681460,9.593018,1.228225,-6.514604,6.464173,-5.572442,-1.535823,-2.020896,-6.479552,-1.774538,5.877221,7.731982,-2.835333,4.095434,3.366047,3.225078,2.243687,-3.214878,-0.539350,2.604758,4.383513,0.200849,-9.728867,4.405137,6.891435,3.613757,3.651226,3.954961,0.879820,2.205073,-9.839159,-5.258161,3.734923,6.933840,1.685145,6.150174,-2.068557,-7.886382,-0.747295,-1.261581,0.239302,7.195265,-8.535643,-4.679824,0.512319,-2.194421,-2.071486,-8.157861,-7.547550,-2.364364,-8.426480,-8.215199,-9.854215,9.190073,-5.107216,-1.248796], dtype = "float64")#candidate|4566|(90,)|const|float64
call_4565 = relay.TupleGetItem(func_584_call(relay.reshape(const_4566.astype('float64'), [2, 15, 3])), 0)
call_4567 = relay.TupleGetItem(func_586_call(relay.reshape(const_4566.astype('float64'), [2, 15, 3])), 0)
func_1340_call = mod.get_global_var('func_1340')
func_1342_call = mutated_mod.get_global_var('func_1342')
var_4569 = relay.var("var_4569", dtype = "float32", shape = (490,))#candidate|4569|(490,)|var|float32
call_4568 = relay.TupleGetItem(func_1340_call(relay.reshape(var_4569.astype('float32'), [490,])), 1)
call_4570 = relay.TupleGetItem(func_1342_call(relay.reshape(var_4569.astype('float32'), [490,])), 1)
var_4576 = relay.var("var_4576", dtype = "int64", shape = (5, 3, 10))#candidate|4576|(5, 3, 10)|var|int64
bop_4577 = relay.minimum(var_4561.astype('float32'), relay.reshape(var_4576.astype('float32'), relay.shape_of(var_4561))) # shape=(5, 3, 10)
func_4423_call = mod.get_global_var('func_4423')
func_4426_call = mutated_mod.get_global_var('func_4426')
const_4581 = relay.const([False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,True,True], dtype = "bool")#candidate|4581|(312,)|const|bool
call_4580 = relay.TupleGetItem(func_4423_call(relay.reshape(const_4581.astype('bool'), [2, 12, 13])), 3)
call_4582 = relay.TupleGetItem(func_4426_call(relay.reshape(const_4581.astype('bool'), [2, 12, 13])), 3)
output = relay.Tuple([bop_4562,call_4565,const_4566,call_4568,var_4569,bop_4577,call_4580,const_4581,])
output2 = relay.Tuple([bop_4562,call_4567,const_4566,call_4570,var_4569,bop_4577,call_4582,const_4581,])
func_4603 = relay.Function([var_4560,var_4561,var_4569,var_4576,], output)
mod['func_4603'] = func_4603
mod = relay.transform.InferType()(mod)
var_4604 = relay.var("var_4604", dtype = "int64", shape = (5, 3, 1))#candidate|4604|(5, 3, 1)|var|int64
var_4605 = relay.var("var_4605", dtype = "int64", shape = (5, 3, 10))#candidate|4605|(5, 3, 10)|var|int64
var_4606 = relay.var("var_4606", dtype = "float32", shape = (490,))#candidate|4606|(490,)|var|float32
var_4607 = relay.var("var_4607", dtype = "int64", shape = (5, 3, 10))#candidate|4607|(5, 3, 10)|var|int64
output = func_4603(var_4604,var_4605,var_4606,var_4607,)
func_4608 = relay.Function([var_4604,var_4605,var_4606,var_4607,], output)
mutated_mod['func_4608'] = func_4608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2378_call = mod.get_global_var('func_2378')
func_2380_call = mutated_mod.get_global_var('func_2380')
call_4630 = relay.TupleGetItem(func_2378_call(), 1)
call_4631 = relay.TupleGetItem(func_2380_call(), 1)
func_1116_call = mod.get_global_var('func_1116')
func_1119_call = mutated_mod.get_global_var('func_1119')
var_4638 = relay.var("var_4638", dtype = "int64", shape = (180,))#candidate|4638|(180,)|var|int64
call_4637 = relay.TupleGetItem(func_1116_call(relay.reshape(var_4638.astype('int64'), [10, 3, 6]), relay.reshape(var_4638.astype('int64'), [10, 3, 6]), ), 0)
call_4639 = relay.TupleGetItem(func_1119_call(relay.reshape(var_4638.astype('int64'), [10, 3, 6]), relay.reshape(var_4638.astype('int64'), [10, 3, 6]), ), 0)
uop_4642 = relay.acosh(call_4630.astype('float32')) # shape=(5, 8, 2)
uop_4644 = relay.acosh(call_4631.astype('float32')) # shape=(5, 8, 2)
uop_4646 = relay.sigmoid(uop_4642.astype('float64')) # shape=(5, 8, 2)
uop_4648 = relay.sigmoid(uop_4644.astype('float64')) # shape=(5, 8, 2)
output = relay.Tuple([call_4637,var_4638,uop_4646,])
output2 = relay.Tuple([call_4639,var_4638,uop_4648,])
func_4656 = relay.Function([var_4638,], output)
mod['func_4656'] = func_4656
mod = relay.transform.InferType()(mod)
mutated_mod['func_4656'] = func_4656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4657 = relay.var("var_4657", dtype = "int64", shape = (180,))#candidate|4657|(180,)|var|int64
func_4656_call = mutated_mod.get_global_var('func_4656')
call_4658 = func_4656_call(var_4657)
output = call_4658
func_4659 = relay.Function([var_4657], output)
mutated_mod['func_4659'] = func_4659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2745_call = mod.get_global_var('func_2745')
func_2746_call = mutated_mod.get_global_var('func_2746')
call_4668 = relay.TupleGetItem(func_2745_call(), 3)
call_4669 = relay.TupleGetItem(func_2746_call(), 3)
func_3520_call = mod.get_global_var('func_3520')
func_3522_call = mutated_mod.get_global_var('func_3522')
call_4689 = relay.TupleGetItem(func_3520_call(), 1)
call_4690 = relay.TupleGetItem(func_3522_call(), 1)
uop_4697 = relay.asinh(call_4668.astype('float32')) # shape=(6, 6, 11)
uop_4699 = relay.asinh(call_4669.astype('float32')) # shape=(6, 6, 11)
uop_4703 = relay.log10(uop_4697.astype('float64')) # shape=(6, 6, 11)
uop_4705 = relay.log10(uop_4699.astype('float64')) # shape=(6, 6, 11)
func_4363_call = mod.get_global_var('func_4363')
func_4367_call = mutated_mod.get_global_var('func_4367')
var_4724 = relay.var("var_4724", dtype = "uint16", shape = (1, 80))#candidate|4724|(1, 80)|var|uint16
const_4725 = relay.const([6.644942,9.191401,5.422234,2.236684,6.899402,4.153034,4.021052,-4.439601,-2.393140,-0.864598,-1.796792,0.852378,-4.453474,-9.885662,-4.387767,9.321225,-5.678729,0.856945,-3.611657,-4.985099,-7.736395,-3.596711,-5.938013,8.403696,6.320290,-2.772003,-3.924324,-7.878797,2.292391,-4.577795,-6.441883,6.999482,1.321289,9.097325,5.240548,1.578734,0.175013,-6.399478,-9.650256,4.172582,7.927339,-3.160132,5.196250,1.589643,8.734240,-8.733002,9.829060,-5.173993,1.649873,-2.747692,1.327881,-5.656573,7.620083,-5.456685,-4.954635,9.738407,-0.185589,2.281203,7.633910,-7.789120,8.608098,-0.173397,-9.694318,6.626632,-2.675408,4.512274,4.487822,0.634879,-8.045386,-4.889034,0.274207,-1.983220,2.448427,4.957221,-0.042162,2.134611,4.959978,-6.981531,9.228749,2.177635,3.668436,0.238729,-3.046200,-5.534185,8.739029,-6.025297,-8.651008,-7.504644,-8.205809,-5.672296], dtype = "float32")#candidate|4725|(90,)|const|float32
call_4723 = relay.TupleGetItem(func_4363_call(relay.reshape(var_4724.astype('uint16'), [5, 8, 2]), relay.reshape(const_4725.astype('float32'), [90,]), ), 6)
call_4726 = relay.TupleGetItem(func_4367_call(relay.reshape(var_4724.astype('uint16'), [5, 8, 2]), relay.reshape(const_4725.astype('float32'), [90,]), ), 6)
func_3919_call = mod.get_global_var('func_3919')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_4735 = relay.TupleGetItem(func_3919_call(), 1)
call_4736 = relay.TupleGetItem(func_3920_call(), 1)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_4741 = relay.TupleGetItem(func_2683_call(), 0)
call_4742 = relay.TupleGetItem(func_2685_call(), 0)
func_1983_call = mod.get_global_var('func_1983')
func_1985_call = mutated_mod.get_global_var('func_1985')
const_4754 = relay.const([-1,-6,8,-8,-2,-3,-5,8,-5,-7,9,1,-10,-7,-9,2,5,-10,9,1,3,8,7,1,6,5,8,5,4,-8,2,-4,-8,-2,-10,-10,7,2,1,5,3,-5,7,-8,3,3,8,2,2,4,-7,7,-2,9,2,3,4,-6,-7,4,-2,5,4,7,1,10,-6,3,5,1,6,5,-1,2,7,10,-3,-9,-2,5,-8,5,-3,3,-10,7,10,9,5,1,-9,1,-8,1,7,-7,-10,-10,-1,-10,1,9,1,3,1,-6,-7,-2,-7,6,6,10,6,-10,-5,7,10,-5,6,-5,-6,-7,9,-9,-10,-2,-10,6,-2,-10,7,-1,7,-7,8,10,-4,8,-8,-4,1,7,-10,-7,9,9,7,2,8,5,-1,9,-5,1,-3,2,-2,-7,-1,-3,2,-6,-2,10,-6,-7,3,-2,-2,-2,7,10,2,-10,-2,3,4,2,8,9,1,8,-1,-2,1,-1,7,-8,1,-2,-10,8,6,2,-3,5,7,10,4,-3,6,-5,-7,4,10,10,2,-6,9,-2,10,-8,3,-5,10,5,-3,-2,5,8,-1,5,-6,2,10,-10,3,7,8,4,3,-5,-2,-7,-3,2,3,7,-10,-7,-5,1,6,8,10,-3,3,-9,5,10,3,1,-1,7,9,2,-2,-6,8,4,5,-3,5,1,-8,-9,-7,8,1,9,-1,8,3,4,5,1,5,-8,6,2,2,-6,6,-7,1,-8,9,6,9,5,-1,-4,2,9,-1,3,-6,4,-5,8,-9,8,4,9,-7,-9,-1,-5,3,3,6,-9,7,4,-6,-9,3,-4,3,-4,8,-9,4,-3,9,-3,2,-9,5,2,-10,-8,-10,1,6,4,-7,-4,-8,-10,-5,-3,-4,7,-10,5,-9,2,-5,-3,-10,-4,1,-10,7,7,2,8,-4,9,5,3,-7,3,10,3,-6,-7,-5,7,6,3,-6,7,-7,4,-2,-5,-2,3,8,-9,2,-9,-4,8,-2,9,-1,6,7,-1,-6,2,-7,-7,-10,7,-4,-9,-5,-8,8,-3,-8,-1,10,5,-8,-4,-3,-10,-1,7,5,4,2,7,3,-1,10,5,-3,7,-9,-6,6,-5,3,2,7,8,-10,-1,6,4,-5,-7,3,-10,7,-5,4,-9,4,-4,7,-2,8,10,7,-3,4,3,-6,-10,-10,5,6,2,-5,-1,-10,-9,-6,6,2,-8,-9,-4,5,-7,8,1,-8,-4,-9,5,-9,10,3,1,-3,-4,1,7,-1,-2,-8,2,4,-9,2,2,8,7,6,-1,-8,-1,-4,-4,5,-5,-9,-1,3,-5,5,6,-9,-9,2,6,-6,8,7,6,-10,-9,7,1,1,7,-5,-1,10,1,-9,-2,6,-4,4,7,2,4,-5,1,10,1,-3,-2,-2,4,10,4,-8,8,-2,-7,-10,-4,-5,-2,5,2,8,2,7,-9,2,2,4,1,5,-10,10,-10,9,9,7,-1,-5,3,8,8,5,-9,8,-5,-1,-7,-7,3,-9,1,4,-9,6,9,-3,-4,-7,-5,7,9,5,7,3,9,4,7,1,-5,9,-10,2,-9,9,5,6,-3,8,-4,-2,2,-2,-4,-7,9,-4,6,-5,7,1,-9,4,9,-2,4,5,-1,-6,-1,1,-9,-10,-3,2,-8,-9,-1,7,-8,2,-4,-7,7,8,-6,-9,-6,-10,6,6,-4,-9,10,4,6,10,-6,-4,2,-10,-3,-3,-7,-9,-4,7,1,-2,3,-1,-5,-2,1,1,-10,-4,-9,-5,2,1,8,-6,5,4,-6,-10,9,2,-8,5,-6,-2,-8,3,-8,5,-4,8,1,-9,8,-7,-9,-7,2,6,1,-2,2,6,-2,9,6,-7,-1,3,4,-4,-9,-2,3,8,6,10,7,-2,-8,7,10,10,-10,9,-3,9,-6,-6,10,10,5,-6,5,-3,10,-9,-6,2,-2,-10,-7,-10,3,-9,-9,1,-8,-8,6,8,-3,-8,7,-5,-2,5,-5,10,10,-2,-10,-3,-7,-3,-2,1,-9,-4,-9,-5,-5,2,-5,9,4,4,-2,2,6,4,-6,3,4,-2,-6,5,7,-3,-2,10,4,1,9,-9,9,-4,10,2,7,-8,1,6,3,-2,4,2,-6,-7,-6,-1,-10,4,4,-6,10,-4,9,2,-9,-8,8,2,5,-8,-6,10,6,7,-7,-1,-7,9,4,10,8,8,-2,-8,2,1,-7,-5,2,4,-5,8,9,9,-1,-7,-9,-4,7,-9,2,-8,-1,-3,-3,4,-2,-9,2,-4,-7,3,-8,-10,-1,-8,10,-3,9,4,2,9,10,7,-7,6,-6,3,-8,-10,3,3,4,-4,1,-4,-6,9,4,-8,8,5,5,-9,3,1,9,-7,7,5,-1,-10,-3,-3,-6,-8,-6,-10,2,-3,9,1,7,1,1,-1,7,9,4,-9,-2,-7,-9,-9,-8,-8,-6,7], dtype = "int32")#candidate|4754|(945,)|const|int32
call_4753 = func_1983_call(relay.reshape(const_4754.astype('int32'), [9, 15, 7]))
call_4755 = func_1983_call(relay.reshape(const_4754.astype('int32'), [9, 15, 7]))
uop_4774 = relay.log(var_4724.astype('float32')) # shape=(1, 80)
output = relay.Tuple([call_4689,uop_4703,call_4723,const_4725,call_4735,call_4741,call_4753,const_4754,uop_4774,])
output2 = relay.Tuple([call_4690,uop_4705,call_4726,const_4725,call_4736,call_4742,call_4755,const_4754,uop_4774,])
func_4784 = relay.Function([var_4724,], output)
mod['func_4784'] = func_4784
mod = relay.transform.InferType()(mod)
var_4785 = relay.var("var_4785", dtype = "uint16", shape = (1, 80))#candidate|4785|(1, 80)|var|uint16
output = func_4784(var_4785)
func_4786 = relay.Function([var_4785], output)
mutated_mod['func_4786'] = func_4786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_4809 = func_1023_call()
call_4810 = func_1023_call()
uop_4823 = relay.log2(call_4809.astype('float64')) # shape=(2, 12, 13)
uop_4825 = relay.log2(call_4810.astype('float64')) # shape=(2, 12, 13)
uop_4842 = relay.rsqrt(uop_4823.astype('float64')) # shape=(2, 12, 13)
uop_4844 = relay.rsqrt(uop_4825.astype('float64')) # shape=(2, 12, 13)
output = uop_4842
output2 = uop_4844
func_4859 = relay.Function([], output)
mod['func_4859'] = func_4859
mod = relay.transform.InferType()(mod)
output = func_4859()
func_4860 = relay.Function([], output)
mutated_mod['func_4860'] = func_4860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2877_call = mod.get_global_var('func_2877')
func_2879_call = mutated_mod.get_global_var('func_2879')
call_4938 = relay.TupleGetItem(func_2877_call(), 1)
call_4939 = relay.TupleGetItem(func_2879_call(), 1)
output = relay.Tuple([call_4938,])
output2 = relay.Tuple([call_4939,])
func_4946 = relay.Function([], output)
mod['func_4946'] = func_4946
mod = relay.transform.InferType()(mod)
output = func_4946()
func_4947 = relay.Function([], output)
mutated_mod['func_4947'] = func_4947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1023_call = mod.get_global_var('func_1023')
func_1024_call = mutated_mod.get_global_var('func_1024')
call_4992 = func_1023_call()
call_4993 = func_1023_call()
output = call_4992
output2 = call_4993
func_4999 = relay.Function([], output)
mod['func_4999'] = func_4999
mod = relay.transform.InferType()(mod)
mutated_mod['func_4999'] = func_4999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4999_call = mutated_mod.get_global_var('func_4999')
call_5000 = func_4999_call()
output = call_5000
func_5001 = relay.Function([], output)
mutated_mod['func_5001'] = func_5001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1088_call = mod.get_global_var('func_1088')
func_1090_call = mutated_mod.get_global_var('func_1090')
call_5099 = relay.TupleGetItem(func_1088_call(), 1)
call_5100 = relay.TupleGetItem(func_1090_call(), 1)
var_5109 = relay.var("var_5109", dtype = "uint16", shape = (5, 8, 2))#candidate|5109|(5, 8, 2)|var|uint16
bop_5110 = relay.add(call_5099.astype('float32'), relay.reshape(var_5109.astype('float32'), relay.shape_of(call_5099))) # shape=(5, 8, 2)
bop_5113 = relay.add(call_5100.astype('float32'), relay.reshape(var_5109.astype('float32'), relay.shape_of(call_5100))) # shape=(5, 8, 2)
func_2082_call = mod.get_global_var('func_2082')
func_2083_call = mutated_mod.get_global_var('func_2083')
call_5116 = func_2082_call()
call_5117 = func_2082_call()
output = relay.Tuple([bop_5110,call_5116,])
output2 = relay.Tuple([bop_5113,call_5117,])
func_5124 = relay.Function([var_5109,], output)
mod['func_5124'] = func_5124
mod = relay.transform.InferType()(mod)
var_5125 = relay.var("var_5125", dtype = "uint16", shape = (5, 8, 2))#candidate|5125|(5, 8, 2)|var|uint16
output = func_5124(var_5125)
func_5126 = relay.Function([var_5125], output)
mutated_mod['func_5126'] = func_5126
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5170 = relay.const([[[-2,1,-6,6],[9,6,-9,-7],[-3,-2,-10,7],[2,-6,-2,9]],[[9,-9,-10,-8],[2,-8,1,9],[10,8,2,6],[3,-3,8,10]],[[-1,-4,-3,-9],[-10,-5,4,5],[-5,-6,10,-3],[5,1,-7,3]],[[-9,8,-1,8],[-5,2,-9,7],[-2,3,4,9],[3,5,1,7]],[[-6,4,3,9],[-7,9,-10,9],[9,5,9,5],[4,-1,9,-4]],[[4,-4,-10,-7],[8,10,-2,9],[3,5,10,6],[-9,8,5,-4]],[[-8,8,-3,-4],[10,-8,-2,-2],[-5,-1,-6,-10],[3,4,9,-9]],[[-8,6,3,-4],[-3,7,-3,2],[-7,-2,9,-9],[-9,-2,-3,-7]],[[1,4,-3,-9],[5,2,5,4],[9,5,8,-2],[-7,5,-5,-10]],[[-6,-2,-7,3],[-5,9,-9,3],[9,-5,2,-3],[-2,-8,3,-5]],[[6,-5,-6,-4],[3,2,6,-9],[-3,-3,-2,5],[-7,2,3,-6]],[[-3,-2,1,-2],[1,8,1,-6],[2,3,-6,-9],[-1,4,8,-3]],[[-2,4,4,10],[3,-5,-5,-1],[10,2,-2,10],[6,5,5,7]]], dtype = "uint8")#candidate|5170|(13, 4, 4)|const|uint8
var_5171 = relay.var("var_5171", dtype = "uint8", shape = (13, 4, 4))#candidate|5171|(13, 4, 4)|var|uint8
bop_5172 = relay.add(const_5170.astype('uint8'), relay.reshape(var_5171.astype('uint8'), relay.shape_of(const_5170))) # shape=(13, 4, 4)
output = relay.Tuple([bop_5172,])
output2 = relay.Tuple([bop_5172,])
func_5175 = relay.Function([var_5171,], output)
mod['func_5175'] = func_5175
mod = relay.transform.InferType()(mod)
var_5176 = relay.var("var_5176", dtype = "uint8", shape = (13, 4, 4))#candidate|5176|(13, 4, 4)|var|uint8
output = func_5175(var_5176)
func_5177 = relay.Function([var_5176], output)
mutated_mod['func_5177'] = func_5177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mod.get_global_var('func_3129')
func_3131_call = mutated_mod.get_global_var('func_3131')
call_5193 = relay.TupleGetItem(func_3129_call(), 1)
call_5194 = relay.TupleGetItem(func_3131_call(), 1)
output = call_5193
output2 = call_5194
func_5197 = relay.Function([], output)
mod['func_5197'] = func_5197
mod = relay.transform.InferType()(mod)
output = func_5197()
func_5198 = relay.Function([], output)
mutated_mod['func_5198'] = func_5198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4946_call = mod.get_global_var('func_4946')
func_4947_call = mutated_mod.get_global_var('func_4947')
call_5215 = relay.TupleGetItem(func_4946_call(), 0)
call_5216 = relay.TupleGetItem(func_4947_call(), 0)
output = relay.Tuple([call_5215,])
output2 = relay.Tuple([call_5216,])
func_5229 = relay.Function([], output)
mod['func_5229'] = func_5229
mod = relay.transform.InferType()(mod)
output = func_5229()
func_5230 = relay.Function([], output)
mutated_mod['func_5230'] = func_5230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1448_call = mod.get_global_var('func_1448')
func_1449_call = mutated_mod.get_global_var('func_1449')
call_5266 = relay.TupleGetItem(func_1448_call(), 1)
call_5267 = relay.TupleGetItem(func_1449_call(), 1)
output = call_5266
output2 = call_5267
func_5282 = relay.Function([], output)
mod['func_5282'] = func_5282
mod = relay.transform.InferType()(mod)
output = func_5282()
func_5283 = relay.Function([], output)
mutated_mod['func_5283'] = func_5283
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5298 = relay.const([[[-6,2,-9,-8,-6],[5,2,-9,3,-10],[-6,-7,-7,-8,-1],[-8,9,8,-8,-1],[7,-6,-5,8,2],[6,10,-5,-10,-9],[-1,-8,1,-10,-2],[3,8,-6,6,-1],[-1,-8,-10,-10,-5],[-3,-8,-7,-9,-7],[-8,10,-10,9,2],[6,-8,-8,1,-1],[7,-3,7,1,6],[6,-8,2,-7,-6],[2,4,-10,10,-8]],[[-6,-5,9,10,9],[-10,4,3,8,6],[9,-5,9,5,7],[-2,-10,3,-10,-9],[-10,4,-7,-9,-9],[8,-6,4,10,-7],[-5,-9,6,4,8],[-7,-2,-4,9,5],[-10,-7,8,4,-1],[5,1,-10,-10,5],[8,6,-2,-1,4],[1,9,-2,9,6],[-8,7,7,-8,-2],[2,-4,9,7,-9],[8,-4,-7,-5,-4]],[[-10,2,-2,5,-3],[-5,-6,-3,9,7],[-10,-7,3,3,-2],[-10,9,-10,-8,-3],[1,-8,-10,-3,1],[-4,-6,-7,5,-10],[-7,1,-10,-7,5],[3,-1,-2,10,-8],[9,3,-3,6,-8],[-8,5,-1,8,7],[-9,9,9,-8,9],[1,-8,-3,5,-2],[8,-10,-9,9,-8],[-3,5,6,5,5],[2,2,-2,-4,8]],[[2,5,-8,10,4],[-4,-6,8,4,-7],[-7,-7,-10,8,6],[9,-10,9,-9,-3],[-6,9,-5,5,10],[8,-3,-8,6,7],[10,1,2,-5,-6],[5,7,-5,1,-2],[1,8,-7,-9,10],[6,-3,9,-4,8],[5,5,9,6,1],[1,-10,-8,-5,9],[-2,-7,-1,-2,-1],[6,-8,-9,2,-7],[3,-6,6,9,10]],[[7,4,-9,-10,-9],[-5,-10,7,-8,-7],[1,2,3,1,9],[2,5,2,1,7],[5,-5,5,-4,-3],[9,-1,3,-8,7],[-8,-5,-7,7,1],[7,7,10,-6,-8],[-5,10,7,9,-10],[3,9,8,-9,1],[-2,5,-10,5,9],[-4,-8,10,10,1],[8,-5,-3,3,2],[1,4,-5,-1,2],[-2,4,-1,-5,6]],[[8,-9,-2,-7,-4],[1,-3,3,1,8],[6,10,-2,-6,1],[-3,5,3,4,-4],[-9,6,-10,-1,3],[-4,1,-8,-6,-8],[-6,7,2,-1,-10],[-7,-10,4,-3,10],[-6,4,-2,-10,9],[-5,-8,-8,-2,9],[4,4,10,-3,-5],[-9,-1,10,-7,2],[-6,-1,-9,9,8],[7,3,-5,3,5],[2,1,-9,7,-9]],[[2,-5,-2,-3,-10],[-8,-2,-10,3,6],[-1,4,-2,-1,8],[7,7,-6,8,1],[-10,-7,-9,9,10],[2,4,3,8,6],[-6,-6,6,-4,-1],[4,-2,-4,-8,5],[-10,1,-2,9,-2],[5,-7,3,-5,10],[9,-7,-3,-4,-6],[10,7,-10,-8,10],[-6,-8,-8,-8,7],[8,10,-9,-8,7],[-3,10,8,10,8]]], dtype = "uint8")#candidate|5298|(7, 15, 5)|const|uint8
var_5299 = relay.var("var_5299", dtype = "uint8", shape = (7, 15, 5))#candidate|5299|(7, 15, 5)|var|uint8
bop_5300 = relay.less(const_5298.astype('bool'), relay.reshape(var_5299.astype('bool'), relay.shape_of(const_5298))) # shape=(7, 15, 5)
output = bop_5300
output2 = bop_5300
func_5322 = relay.Function([var_5299,], output)
mod['func_5322'] = func_5322
mod = relay.transform.InferType()(mod)
var_5323 = relay.var("var_5323", dtype = "uint8", shape = (7, 15, 5))#candidate|5323|(7, 15, 5)|var|uint8
output = func_5322(var_5323)
func_5324 = relay.Function([var_5323], output)
mutated_mod['func_5324'] = func_5324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5371 = relay.var("var_5371", dtype = "float32", shape = (6, 14, 3))#candidate|5371|(6, 14, 3)|var|float32
uop_5372 = relay.tan(var_5371.astype('float32')) # shape=(6, 14, 3)
bop_5377 = relay.left_shift(uop_5372.astype('uint8'), relay.reshape(var_5371.astype('uint8'), relay.shape_of(uop_5372))) # shape=(6, 14, 3)
bop_5387 = relay.divide(uop_5372.astype('float32'), relay.reshape(bop_5377.astype('float32'), relay.shape_of(uop_5372))) # shape=(6, 14, 3)
func_3520_call = mod.get_global_var('func_3520')
func_3522_call = mutated_mod.get_global_var('func_3522')
call_5404 = relay.TupleGetItem(func_3520_call(), 1)
call_5405 = relay.TupleGetItem(func_3522_call(), 1)
bop_5410 = relay.mod(uop_5372.astype('float32'), relay.reshape(bop_5377.astype('float32'), relay.shape_of(uop_5372))) # shape=(6, 14, 3)
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_5419 = relay.TupleGetItem(func_3712_call(), 0)
call_5420 = relay.TupleGetItem(func_3713_call(), 0)
bop_5421 = relay.floor_divide(bop_5377.astype('float64'), relay.reshape(var_5371.astype('float64'), relay.shape_of(bop_5377))) # shape=(6, 14, 3)
uop_5424 = relay.log(uop_5372.astype('float64')) # shape=(6, 14, 3)
var_5428 = relay.var("var_5428", dtype = "float32", shape = (6, 14, 3))#candidate|5428|(6, 14, 3)|var|float32
bop_5429 = relay.logical_and(uop_5372.astype('bool'), relay.reshape(var_5428.astype('bool'), relay.shape_of(uop_5372))) # shape=(6, 14, 3)
output = relay.Tuple([bop_5387,call_5404,bop_5410,call_5419,bop_5421,uop_5424,bop_5429,])
output2 = relay.Tuple([bop_5387,call_5405,bop_5410,call_5420,bop_5421,uop_5424,bop_5429,])
F = relay.Function([var_5371,var_5428,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5371,var_5428,], output2)
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
