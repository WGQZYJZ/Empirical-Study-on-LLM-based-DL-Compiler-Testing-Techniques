import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_307 = relay.const([[[7.584689,3.223852,6.938982,0.776772,-6.222531,1.271558,-7.879909,5.646302,4.675234],[-5.996928,-8.141429,9.747645,-6.734782,2.153471,3.972809,-9.477537,-6.395046,-1.009890],[-2.770503,-4.487100,8.073048,-9.686780,-7.820388,-6.166524,-1.915094,-8.713685,-9.427765],[1.949888,-4.262941,-0.993103,4.999656,-7.166331,-5.897414,1.238794,-8.526442,3.972661],[3.515557,3.544808,-3.023083,3.980166,-3.607263,9.214135,3.445059,7.065251,2.789375]]], dtype = "float64")#candidate|307|(1, 5, 9)|const|float64
const_308 = relay.const([[[-9.252552,-3.331790,-4.750265,6.307561,-4.963692,6.392130,7.922402,-1.784449,1.354642],[-8.662836,7.130714,2.423303,-7.060605,-3.601682,9.079037,2.980150,-3.238699,0.395190],[6.669064,-2.294733,5.499515,1.695011,0.007187,2.910678,4.220078,1.279692,7.157492],[3.507581,4.113225,8.951471,0.456707,0.525141,-7.120204,-3.232373,6.285324,1.022178],[9.667174,4.579612,-1.009681,9.070347,4.468379,-0.446397,7.348185,-5.952247,-8.966236]]], dtype = "float64")#candidate|308|(1, 5, 9)|const|float64
bop_309 = relay.power(const_307.astype('float64'), relay.reshape(const_308.astype('float64'), relay.shape_of(const_307))) # shape=(1, 5, 9)
output = bop_309
output2 = bop_309
func_314 = relay.Function([], output)
mod['func_314'] = func_314
mod = relay.transform.InferType()(mod)
output = func_314()
func_315 = relay.Function([], output)
mutated_mod['func_315'] = func_315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_338 = func_314_call()
call_339 = func_314_call()
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_353 = func_314_call()
call_354 = func_314_call()
bop_369 = relay.logical_xor(call_353.astype('uint64'), relay.reshape(call_338.astype('uint64'), relay.shape_of(call_353))) # shape=(1, 5, 9)
bop_372 = relay.logical_xor(call_354.astype('uint64'), relay.reshape(call_339.astype('uint64'), relay.shape_of(call_354))) # shape=(1, 5, 9)
bop_375 = relay.right_shift(bop_369.astype('uint64'), relay.reshape(call_353.astype('uint64'), relay.shape_of(bop_369))) # shape=(1, 5, 9)
bop_378 = relay.right_shift(bop_372.astype('uint64'), relay.reshape(call_354.astype('uint64'), relay.shape_of(bop_372))) # shape=(1, 5, 9)
output = bop_375
output2 = bop_378
func_380 = relay.Function([], output)
mod['func_380'] = func_380
mod = relay.transform.InferType()(mod)
output = func_380()
func_381 = relay.Function([], output)
mutated_mod['func_381'] = func_381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_448 = func_380_call()
call_449 = func_380_call()
output = relay.Tuple([call_448,])
output2 = relay.Tuple([call_449,])
func_454 = relay.Function([], output)
mod['func_454'] = func_454
mod = relay.transform.InferType()(mod)
mutated_mod['func_454'] = func_454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mutated_mod.get_global_var('func_454')
call_455 = func_454_call()
output = call_455
func_456 = relay.Function([], output)
mutated_mod['func_456'] = func_456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_478 = func_380_call()
call_479 = func_380_call()
output = call_478
output2 = call_479
func_480 = relay.Function([], output)
mod['func_480'] = func_480
mod = relay.transform.InferType()(mod)
mutated_mod['func_480'] = func_480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mutated_mod.get_global_var('func_480')
call_481 = func_480_call()
output = call_481
func_482 = relay.Function([], output)
mutated_mod['func_482'] = func_482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_501 = relay.var("var_501", dtype = "float64", shape = (3, 2, 8))#candidate|501|(3, 2, 8)|var|float64
var_502 = relay.var("var_502", dtype = "float64", shape = (3, 2, 8))#candidate|502|(3, 2, 8)|var|float64
bop_503 = relay.mod(var_501.astype('float64'), relay.reshape(var_502.astype('float64'), relay.shape_of(var_501))) # shape=(3, 2, 8)
output = relay.Tuple([bop_503,])
output2 = relay.Tuple([bop_503,])
func_506 = relay.Function([var_501,var_502,], output)
mod['func_506'] = func_506
mod = relay.transform.InferType()(mod)
var_507 = relay.var("var_507", dtype = "float64", shape = (3, 2, 8))#candidate|507|(3, 2, 8)|var|float64
var_508 = relay.var("var_508", dtype = "float64", shape = (3, 2, 8))#candidate|508|(3, 2, 8)|var|float64
output = func_506(var_507,var_508,)
func_509 = relay.Function([var_507,var_508,], output)
mutated_mod['func_509'] = func_509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_559 = func_380_call()
call_560 = func_380_call()
output = relay.Tuple([call_559,])
output2 = relay.Tuple([call_560,])
func_564 = relay.Function([], output)
mod['func_564'] = func_564
mod = relay.transform.InferType()(mod)
mutated_mod['func_564'] = func_564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_564_call = mutated_mod.get_global_var('func_564')
call_565 = func_564_call()
output = call_565
func_566 = relay.Function([], output)
mutated_mod['func_566'] = func_566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_572 = func_480_call()
call_573 = func_480_call()
uop_577 = relay.acosh(call_572.astype('float64')) # shape=(1, 5, 9)
uop_579 = relay.acosh(call_573.astype('float64')) # shape=(1, 5, 9)
func_564_call = mod.get_global_var('func_564')
func_566_call = mutated_mod.get_global_var('func_566')
call_584 = relay.TupleGetItem(func_564_call(), 0)
call_585 = relay.TupleGetItem(func_566_call(), 0)
output = relay.Tuple([uop_577,call_584,])
output2 = relay.Tuple([uop_579,call_585,])
func_592 = relay.Function([], output)
mod['func_592'] = func_592
mod = relay.transform.InferType()(mod)
mutated_mod['func_592'] = func_592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_592_call = mutated_mod.get_global_var('func_592')
call_593 = func_592_call()
output = call_593
func_594 = relay.Function([], output)
mutated_mod['func_594'] = func_594
mutated_mod = relay.transform.InferType()(mutated_mod)
var_684 = relay.var("var_684", dtype = "int32", shape = ())#candidate|684|()|var|int32
var_685 = relay.var("var_685", dtype = "int32", shape = (7, 1, 10))#candidate|685|(7, 1, 10)|var|int32
bop_686 = relay.less(var_684.astype('bool'), var_685.astype('bool')) # shape=(7, 1, 10)
output = relay.Tuple([bop_686,])
output2 = relay.Tuple([bop_686,])
func_689 = relay.Function([var_684,var_685,], output)
mod['func_689'] = func_689
mod = relay.transform.InferType()(mod)
var_690 = relay.var("var_690", dtype = "int32", shape = ())#candidate|690|()|var|int32
var_691 = relay.var("var_691", dtype = "int32", shape = (7, 1, 10))#candidate|691|(7, 1, 10)|var|int32
output = func_689(var_690,var_691,)
func_692 = relay.Function([var_690,var_691,], output)
mutated_mod['func_692'] = func_692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
call_698 = relay.TupleGetItem(func_592_call(), 1)
call_699 = relay.TupleGetItem(func_594_call(), 1)
output = relay.Tuple([call_698,])
output2 = relay.Tuple([call_699,])
func_704 = relay.Function([], output)
mod['func_704'] = func_704
mod = relay.transform.InferType()(mod)
mutated_mod['func_704'] = func_704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_704_call = mutated_mod.get_global_var('func_704')
call_705 = func_704_call()
output = call_705
func_706 = relay.Function([], output)
mutated_mod['func_706'] = func_706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_789 = func_480_call()
call_790 = func_480_call()
output = call_789
output2 = call_790
func_791 = relay.Function([], output)
mod['func_791'] = func_791
mod = relay.transform.InferType()(mod)
output = func_791()
func_792 = relay.Function([], output)
mutated_mod['func_792'] = func_792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_704_call = mod.get_global_var('func_704')
func_706_call = mutated_mod.get_global_var('func_706')
call_929 = relay.TupleGetItem(func_704_call(), 0)
call_930 = relay.TupleGetItem(func_706_call(), 0)
output = relay.Tuple([call_929,])
output2 = relay.Tuple([call_930,])
func_935 = relay.Function([], output)
mod['func_935'] = func_935
mod = relay.transform.InferType()(mod)
mutated_mod['func_935'] = func_935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mutated_mod.get_global_var('func_935')
call_936 = func_935_call()
output = call_936
func_937 = relay.Function([], output)
mutated_mod['func_937'] = func_937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mod.get_global_var('func_935')
func_937_call = mutated_mod.get_global_var('func_937')
call_965 = relay.TupleGetItem(func_935_call(), 0)
call_966 = relay.TupleGetItem(func_937_call(), 0)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_976 = func_380_call()
call_977 = func_380_call()
func_454_call = mod.get_global_var('func_454')
func_456_call = mutated_mod.get_global_var('func_456')
call_983 = relay.TupleGetItem(func_454_call(), 0)
call_984 = relay.TupleGetItem(func_456_call(), 0)
uop_988 = relay.acos(call_976.astype('float32')) # shape=(1, 5, 9)
uop_990 = relay.acos(call_977.astype('float32')) # shape=(1, 5, 9)
func_564_call = mod.get_global_var('func_564')
func_566_call = mutated_mod.get_global_var('func_566')
call_1008 = relay.TupleGetItem(func_564_call(), 0)
call_1009 = relay.TupleGetItem(func_566_call(), 0)
output = relay.Tuple([call_965,call_983,uop_988,call_1008,])
output2 = relay.Tuple([call_966,call_984,uop_990,call_1009,])
func_1024 = relay.Function([], output)
mod['func_1024'] = func_1024
mod = relay.transform.InferType()(mod)
mutated_mod['func_1024'] = func_1024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1024_call = mutated_mod.get_global_var('func_1024')
call_1025 = func_1024_call()
output = call_1025
func_1026 = relay.Function([], output)
mutated_mod['func_1026'] = func_1026
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1051 = relay.var("var_1051", dtype = "int32", shape = (14, 3, 8))#candidate|1051|(14, 3, 8)|var|int32
var_1052 = relay.var("var_1052", dtype = "int32", shape = (14, 3, 8))#candidate|1052|(14, 3, 8)|var|int32
bop_1053 = relay.subtract(var_1051.astype('int32'), relay.reshape(var_1052.astype('int32'), relay.shape_of(var_1051))) # shape=(14, 3, 8)
var_1073 = relay.var("var_1073", dtype = "int32", shape = (14, 3, 8))#candidate|1073|(14, 3, 8)|var|int32
bop_1074 = relay.right_shift(var_1052.astype('int16'), relay.reshape(var_1073.astype('int16'), relay.shape_of(var_1052))) # shape=(14, 3, 8)
output = relay.Tuple([bop_1053,bop_1074,])
output2 = relay.Tuple([bop_1053,bop_1074,])
func_1077 = relay.Function([var_1051,var_1052,var_1073,], output)
mod['func_1077'] = func_1077
mod = relay.transform.InferType()(mod)
var_1078 = relay.var("var_1078", dtype = "int32", shape = (14, 3, 8))#candidate|1078|(14, 3, 8)|var|int32
var_1079 = relay.var("var_1079", dtype = "int32", shape = (14, 3, 8))#candidate|1079|(14, 3, 8)|var|int32
var_1080 = relay.var("var_1080", dtype = "int32", shape = (14, 3, 8))#candidate|1080|(14, 3, 8)|var|int32
output = func_1077(var_1078,var_1079,var_1080,)
func_1081 = relay.Function([var_1078,var_1079,var_1080,], output)
mutated_mod['func_1081'] = func_1081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_1097 = func_314_call()
call_1098 = func_314_call()
output = call_1097
output2 = call_1098
func_1124 = relay.Function([], output)
mod['func_1124'] = func_1124
mod = relay.transform.InferType()(mod)
mutated_mod['func_1124'] = func_1124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1124_call = mutated_mod.get_global_var('func_1124')
call_1125 = func_1124_call()
output = call_1125
func_1126 = relay.Function([], output)
mutated_mod['func_1126'] = func_1126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
call_1145 = relay.TupleGetItem(func_592_call(), 1)
call_1146 = relay.TupleGetItem(func_594_call(), 1)
func_1124_call = mod.get_global_var('func_1124')
func_1126_call = mutated_mod.get_global_var('func_1126')
call_1177 = func_1124_call()
call_1178 = func_1124_call()
const_1191 = relay.const([[[1.572455,-2.641756,7.108347,-3.834810,-9.981513,1.715070,-3.422050,7.525482,6.041522],[2.886347,-7.918827,7.190582,-6.366533,-6.948836,6.278414,-2.313939,5.230053,-0.865093],[2.879630,6.234253,3.932014,-1.269592,-6.843298,-6.966772,-1.897608,8.564705,4.911368],[0.509021,6.242107,7.668715,-5.063435,-1.358745,8.105586,-6.395275,8.101059,-6.832309],[-0.854087,-5.284802,-6.294352,-7.232333,7.563799,4.039253,3.728527,-5.572985,-4.292621]],[[7.238181,-0.798734,-1.399647,5.067769,-0.954487,1.591254,4.498349,1.882202,-1.405368],[-8.169427,2.689947,5.824832,-4.136952,1.172794,5.758297,9.144929,-5.967483,-8.776682],[4.798459,8.792886,4.684618,-7.769631,-8.846620,-4.310919,8.702863,-0.100535,-7.999496],[7.434054,-7.924032,-6.444214,-5.104299,-5.688713,3.774113,4.998907,-6.684297,-2.991749],[2.818631,-7.274156,-6.845437,3.724585,-9.732319,-5.550136,2.607336,2.569348,4.301144]],[[5.946056,9.771909,-8.271014,6.912868,9.044596,2.649544,9.239331,-1.669054,-7.353971],[-3.712283,-1.326762,7.804913,-4.662164,-6.908816,-8.104495,5.714056,0.086279,-9.662712],[6.359669,-8.533990,1.252574,-7.845445,-6.219373,1.056503,4.002335,-8.371460,-4.894279],[0.952307,-6.605840,-9.754387,9.595920,4.877581,4.926339,-9.297064,8.435605,3.781609],[-6.860539,9.854523,0.379689,-7.036184,-3.120885,-7.031635,-6.372544,4.742644,-2.319087]],[[-7.429396,4.465672,-8.336004,4.758216,6.308759,0.028560,1.576717,-7.860286,6.175722],[0.149719,2.757352,-8.732374,-6.570549,9.171189,-2.149404,-5.022716,4.228220,-5.755806],[-5.263105,-5.905534,-6.966788,-5.555798,-1.729019,-1.190323,-6.736432,5.052650,3.016905],[-4.631544,-3.838694,-7.417511,5.946000,5.594708,-7.780117,-0.730343,0.048135,0.472173],[8.130974,-7.714623,-5.088742,4.055597,-8.388675,-5.330179,-8.943902,-3.094691,-6.237676]],[[3.397984,1.312438,-6.780191,-9.772539,-2.168946,-7.679201,9.845347,0.266163,3.070381],[-3.831421,2.162767,2.443055,0.238219,-9.706774,-9.154602,-1.481716,-5.663812,2.116320],[5.004506,5.413196,8.057791,9.132234,9.068611,-9.790707,6.661962,4.171098,-8.783760],[-5.507453,4.880017,4.627648,-7.723496,7.383267,1.143487,0.885367,1.501284,-9.458988],[-3.205222,5.650039,-6.555501,-3.260131,4.476899,-3.210788,-9.562788,6.572434,1.432432]],[[-3.255603,-7.016039,-8.814632,-3.362366,-8.255246,0.633001,-4.444343,5.149388,8.271305],[-4.935534,6.106568,-9.966110,5.710498,-8.473936,-0.653953,2.829030,3.250545,-6.062106],[5.943108,-4.232336,-4.581308,-0.757753,1.759330,1.298287,8.477158,8.716210,6.974492],[1.750563,-2.427958,3.721990,4.899896,0.577134,-5.661743,0.427508,-9.948918,3.271988],[0.554395,-7.314417,4.260047,1.728882,6.283005,9.460006,-7.021193,0.914161,7.873909]],[[1.186413,9.406479,5.850212,1.856503,6.855930,-1.897393,-4.797354,-2.067305,0.910913],[-0.471242,-1.304761,3.044748,-5.400461,-7.822144,-1.178655,-8.114661,7.682156,1.065451],[7.240379,8.724857,-0.978858,-2.653059,3.809096,6.584141,-8.650578,8.542833,2.695804],[8.771416,2.871445,8.248227,8.680482,0.935911,8.371147,5.980149,2.402835,0.883055],[5.506793,1.980483,-4.465534,9.698114,-8.059660,-8.756694,2.617051,-2.467703,1.417870]],[[-6.139941,5.907298,9.409274,-8.899171,-5.569781,7.294484,-4.428297,0.181043,2.827243],[-5.093509,-7.644518,-7.017206,5.769394,-1.880669,-8.599124,8.378189,-8.861399,-1.767233],[-1.713808,1.124351,5.904238,-7.795486,5.911578,9.106605,-4.288783,8.116276,-4.833621],[4.969090,0.430488,2.612162,9.320791,-3.901851,-6.271020,-9.345431,-8.809833,9.221482],[-1.145964,2.707934,3.781384,4.177928,-7.637311,-4.596655,-4.563639,-9.531029,-0.641497]],[[2.036280,2.414299,6.216303,-0.784914,-9.498280,6.859033,-5.828160,9.708332,9.222159],[-8.372789,-0.830131,0.479759,-6.168416,-2.541718,1.227600,-9.986759,8.748475,9.247310],[1.497836,-8.203304,-8.101925,8.693360,1.684713,-5.802433,8.139687,8.182991,5.737195],[8.669924,-8.425717,4.897485,-4.846446,-1.498603,1.670317,-8.999631,-7.869366,-4.852994],[5.876315,8.049048,-7.989359,1.666112,6.090268,-5.483870,-9.727872,-6.144433,0.187594]]], dtype = "float64")#candidate|1191|(9, 5, 9)|const|float64
bop_1192 = relay.greater_equal(call_1177.astype('bool'), const_1191.astype('bool')) # shape=(9, 5, 9)
bop_1195 = relay.greater_equal(call_1178.astype('bool'), const_1191.astype('bool')) # shape=(9, 5, 9)
bop_1209 = relay.less(bop_1192.astype('bool'), relay.reshape(const_1191.astype('bool'), relay.shape_of(bop_1192))) # shape=(9, 5, 9)
bop_1212 = relay.less(bop_1195.astype('bool'), relay.reshape(const_1191.astype('bool'), relay.shape_of(bop_1195))) # shape=(9, 5, 9)
func_704_call = mod.get_global_var('func_704')
func_706_call = mutated_mod.get_global_var('func_706')
call_1213 = relay.TupleGetItem(func_704_call(), 0)
call_1214 = relay.TupleGetItem(func_706_call(), 0)
func_1077_call = mod.get_global_var('func_1077')
func_1081_call = mutated_mod.get_global_var('func_1081')
var_1222 = relay.var("var_1222", dtype = "int32", shape = (336,))#candidate|1222|(336,)|var|int32
call_1221 = relay.TupleGetItem(func_1077_call(relay.reshape(var_1222.astype('int32'), [14, 3, 8]), relay.reshape(var_1222.astype('int32'), [14, 3, 8]), relay.reshape(var_1222.astype('int32'), [14, 3, 8]), ), 1)
call_1223 = relay.TupleGetItem(func_1081_call(relay.reshape(var_1222.astype('int32'), [14, 3, 8]), relay.reshape(var_1222.astype('int32'), [14, 3, 8]), relay.reshape(var_1222.astype('int32'), [14, 3, 8]), ), 1)
output = relay.Tuple([call_1145,bop_1209,call_1213,call_1221,var_1222,])
output2 = relay.Tuple([call_1146,bop_1212,call_1214,call_1223,var_1222,])
func_1232 = relay.Function([var_1222,], output)
mod['func_1232'] = func_1232
mod = relay.transform.InferType()(mod)
mutated_mod['func_1232'] = func_1232
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1233 = relay.var("var_1233", dtype = "int32", shape = (336,))#candidate|1233|(336,)|var|int32
func_1232_call = mutated_mod.get_global_var('func_1232')
call_1234 = func_1232_call(var_1233)
output = call_1234
func_1235 = relay.Function([var_1233], output)
mutated_mod['func_1235'] = func_1235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mod.get_global_var('func_935')
func_937_call = mutated_mod.get_global_var('func_937')
call_1295 = relay.TupleGetItem(func_935_call(), 0)
call_1296 = relay.TupleGetItem(func_937_call(), 0)
output = relay.Tuple([call_1295,])
output2 = relay.Tuple([call_1296,])
func_1307 = relay.Function([], output)
mod['func_1307'] = func_1307
mod = relay.transform.InferType()(mod)
output = func_1307()
func_1308 = relay.Function([], output)
mutated_mod['func_1308'] = func_1308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_1309 = func_480_call()
call_1310 = func_480_call()
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_1334 = func_380_call()
call_1335 = func_380_call()
output = relay.Tuple([call_1309,call_1334,])
output2 = relay.Tuple([call_1310,call_1335,])
func_1336 = relay.Function([], output)
mod['func_1336'] = func_1336
mod = relay.transform.InferType()(mod)
mutated_mod['func_1336'] = func_1336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1336_call = mutated_mod.get_global_var('func_1336')
call_1337 = func_1336_call()
output = call_1337
func_1338 = relay.Function([], output)
mutated_mod['func_1338'] = func_1338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
call_1377 = relay.TupleGetItem(func_592_call(), 0)
call_1378 = relay.TupleGetItem(func_594_call(), 0)
uop_1399 = relay.asin(call_1377.astype('float64')) # shape=(1, 5, 9)
uop_1401 = relay.asin(call_1378.astype('float64')) # shape=(1, 5, 9)
var_1416 = relay.var("var_1416", dtype = "float64", shape = (9, 5, 9))#candidate|1416|(9, 5, 9)|var|float64
bop_1417 = relay.add(call_1377.astype('int64'), var_1416.astype('int64')) # shape=(9, 5, 9)
bop_1420 = relay.add(call_1378.astype('int64'), var_1416.astype('int64')) # shape=(9, 5, 9)
uop_1422 = relay.cosh(uop_1399.astype('float64')) # shape=(1, 5, 9)
uop_1424 = relay.cosh(uop_1401.astype('float64')) # shape=(1, 5, 9)
output = relay.Tuple([bop_1417,uop_1422,])
output2 = relay.Tuple([bop_1420,uop_1424,])
func_1431 = relay.Function([var_1416,], output)
mod['func_1431'] = func_1431
mod = relay.transform.InferType()(mod)
var_1432 = relay.var("var_1432", dtype = "float64", shape = (9, 5, 9))#candidate|1432|(9, 5, 9)|var|float64
output = func_1431(var_1432)
func_1433 = relay.Function([var_1432], output)
mutated_mod['func_1433'] = func_1433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_1458 = func_314_call()
call_1459 = func_314_call()
func_1307_call = mod.get_global_var('func_1307')
func_1308_call = mutated_mod.get_global_var('func_1308')
call_1467 = relay.TupleGetItem(func_1307_call(), 0)
call_1468 = relay.TupleGetItem(func_1308_call(), 0)
output = relay.Tuple([call_1458,call_1467,])
output2 = relay.Tuple([call_1459,call_1468,])
func_1469 = relay.Function([], output)
mod['func_1469'] = func_1469
mod = relay.transform.InferType()(mod)
output = func_1469()
func_1470 = relay.Function([], output)
mutated_mod['func_1470'] = func_1470
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1490 = relay.var("var_1490", dtype = "float32", shape = (10, 9, 11))#candidate|1490|(10, 9, 11)|var|float32
uop_1491 = relay.asin(var_1490.astype('float32')) # shape=(10, 9, 11)
output = uop_1491
output2 = uop_1491
func_1515 = relay.Function([var_1490,], output)
mod['func_1515'] = func_1515
mod = relay.transform.InferType()(mod)
var_1516 = relay.var("var_1516", dtype = "float32", shape = (10, 9, 11))#candidate|1516|(10, 9, 11)|var|float32
output = func_1515(var_1516)
func_1517 = relay.Function([var_1516], output)
mutated_mod['func_1517'] = func_1517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_1564 = relay.TupleGetItem(func_1336_call(), 1)
call_1565 = relay.TupleGetItem(func_1338_call(), 1)
output = relay.Tuple([call_1564,])
output2 = relay.Tuple([call_1565,])
func_1567 = relay.Function([], output)
mod['func_1567'] = func_1567
mod = relay.transform.InferType()(mod)
output = func_1567()
func_1568 = relay.Function([], output)
mutated_mod['func_1568'] = func_1568
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1585 = relay.var("var_1585", dtype = "float32", shape = (7, 3, 3))#candidate|1585|(7, 3, 3)|var|float32
uop_1586 = relay.atan(var_1585.astype('float32')) # shape=(7, 3, 3)
func_1469_call = mod.get_global_var('func_1469')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_1592 = relay.TupleGetItem(func_1469_call(), 1)
call_1593 = relay.TupleGetItem(func_1470_call(), 1)
output = relay.Tuple([uop_1586,call_1592,])
output2 = relay.Tuple([uop_1586,call_1593,])
func_1594 = relay.Function([var_1585,], output)
mod['func_1594'] = func_1594
mod = relay.transform.InferType()(mod)
mutated_mod['func_1594'] = func_1594
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1595 = relay.var("var_1595", dtype = "float32", shape = (7, 3, 3))#candidate|1595|(7, 3, 3)|var|float32
func_1594_call = mutated_mod.get_global_var('func_1594')
call_1596 = func_1594_call(var_1595)
output = call_1596
func_1597 = relay.Function([var_1595], output)
mutated_mod['func_1597'] = func_1597
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1690 = relay.var("var_1690", dtype = "float32", shape = (3, 12, 8))#candidate|1690|(3, 12, 8)|var|float32
uop_1691 = relay.cos(var_1690.astype('float32')) # shape=(3, 12, 8)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_1697 = func_380_call()
call_1698 = func_380_call()
func_935_call = mod.get_global_var('func_935')
func_937_call = mutated_mod.get_global_var('func_937')
call_1700 = relay.TupleGetItem(func_935_call(), 0)
call_1701 = relay.TupleGetItem(func_937_call(), 0)
bop_1703 = relay.bitwise_xor(uop_1691.astype('uint32'), relay.reshape(var_1690.astype('uint32'), relay.shape_of(uop_1691))) # shape=(3, 12, 8)
output = relay.Tuple([call_1697,call_1700,bop_1703,])
output2 = relay.Tuple([call_1698,call_1701,bop_1703,])
func_1706 = relay.Function([var_1690,], output)
mod['func_1706'] = func_1706
mod = relay.transform.InferType()(mod)
var_1707 = relay.var("var_1707", dtype = "float32", shape = (3, 12, 8))#candidate|1707|(3, 12, 8)|var|float32
output = func_1706(var_1707)
func_1708 = relay.Function([var_1707], output)
mutated_mod['func_1708'] = func_1708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_1717 = func_480_call()
call_1718 = func_480_call()
uop_1725 = relay.erf(call_1717.astype('float64')) # shape=(1, 5, 9)
uop_1727 = relay.erf(call_1718.astype('float64')) # shape=(1, 5, 9)
uop_1729 = relay.sigmoid(uop_1725.astype('float32')) # shape=(1, 5, 9)
uop_1731 = relay.sigmoid(uop_1727.astype('float32')) # shape=(1, 5, 9)
func_454_call = mod.get_global_var('func_454')
func_456_call = mutated_mod.get_global_var('func_456')
call_1732 = relay.TupleGetItem(func_454_call(), 0)
call_1733 = relay.TupleGetItem(func_456_call(), 0)
output = relay.Tuple([uop_1729,call_1732,])
output2 = relay.Tuple([uop_1731,call_1733,])
func_1737 = relay.Function([], output)
mod['func_1737'] = func_1737
mod = relay.transform.InferType()(mod)
mutated_mod['func_1737'] = func_1737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1737_call = mutated_mod.get_global_var('func_1737')
call_1738 = func_1737_call()
output = call_1738
func_1739 = relay.Function([], output)
mutated_mod['func_1739'] = func_1739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1024_call = mod.get_global_var('func_1024')
func_1026_call = mutated_mod.get_global_var('func_1026')
call_1765 = relay.TupleGetItem(func_1024_call(), 0)
call_1766 = relay.TupleGetItem(func_1026_call(), 0)
func_1077_call = mod.get_global_var('func_1077')
func_1081_call = mutated_mod.get_global_var('func_1081')
const_1773 = relay.const([-2,-4,-7,-10,-4,-10,2,1,-8,-6,8,-7,9,7,-1,-5,-5,2,8,6,-10,1,6,-9,-7,-1,8,-8,-9,9,9,3,-5,-4,6,6,-6,-9,9,9,2,8,6,-9,5,7,5,6,4,4,-1,7,5,2,-3,-9,10,4,-5,5,4,2,3,-9,9,10,-4,-7,-4,-3,1,3,-9,-9,2,4,5,5,-5,6,8,4,-2,8,-2,-2,-3,2,4,6,-5,-1,-4,10,-1,-3,-4,-10,8,2,-1,10,-1,-3,6,-10,8,3,6,-3,-4,5,-3,-4,-2,-10,-5,6,5,-1,-9,-3,-2,2,4,6,-4,-5,5,10,10,-10,-2,-10,-6,-7,-4,5,-9,-4,4,2,-3,9,-8,5,10,-2,-4,9,-5,-6,-1,3,-9,4,8,-3,2,-1,10,-10,-3,-5,5,8,2,-9,6,2,10,7,1,1,2,6,7,-4,-8,-9,3,-5,3,6,5,-5,4,-2,-3,-8,4,7,-8,4,-10,-1,10,5,-9,3,1,-8,9,9,5,-7,9,-2,4,5,9,-4,3,2,-2,-5,-2,-7,-2,-1,2,-6,1,-10,-4,-9,-2,-1,4,-4,-8,-9,-1,-1,3,-8,1,5,-1,-7,9,-9,-2,-5,-4,5,9,4,2,-3,-9,-7,-6,-2,-9,-4,-6,-1,-3,-5,7,-3,-5,6,-4,2,1,-4,4,-6,7,-1,-2,3,9,4,-9,-2,-4,2,1,-1,-5,-9,-1,2,-6,-2,5,6,3,-2,7,-7,-6,8,6,10,-4,-10,6,4,-7,10,2,-8,6,-7,5,5,-6,-7,-4,-4,5,-7,8,-3,-8,8,1,-4,5,-1,7,10,-10,-6,5,7,3,-3,3,-5,10,-10], dtype = "int32")#candidate|1773|(336,)|const|int32
call_1772 = relay.TupleGetItem(func_1077_call(relay.reshape(const_1773.astype('int32'), [14, 3, 8]), relay.reshape(const_1773.astype('int32'), [14, 3, 8]), relay.reshape(const_1773.astype('int32'), [14, 3, 8]), ), 0)
call_1774 = relay.TupleGetItem(func_1081_call(relay.reshape(const_1773.astype('int32'), [14, 3, 8]), relay.reshape(const_1773.astype('int32'), [14, 3, 8]), relay.reshape(const_1773.astype('int32'), [14, 3, 8]), ), 0)
func_454_call = mod.get_global_var('func_454')
func_456_call = mutated_mod.get_global_var('func_456')
call_1780 = relay.TupleGetItem(func_454_call(), 0)
call_1781 = relay.TupleGetItem(func_456_call(), 0)
output = relay.Tuple([call_1765,call_1772,const_1773,call_1780,])
output2 = relay.Tuple([call_1766,call_1774,const_1773,call_1781,])
func_1791 = relay.Function([], output)
mod['func_1791'] = func_1791
mod = relay.transform.InferType()(mod)
mutated_mod['func_1791'] = func_1791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1791_call = mutated_mod.get_global_var('func_1791')
call_1792 = func_1791_call()
output = call_1792
func_1793 = relay.Function([], output)
mutated_mod['func_1793'] = func_1793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_704_call = mod.get_global_var('func_704')
func_706_call = mutated_mod.get_global_var('func_706')
call_1794 = relay.TupleGetItem(func_704_call(), 0)
call_1795 = relay.TupleGetItem(func_706_call(), 0)
output = call_1794
output2 = call_1795
func_1803 = relay.Function([], output)
mod['func_1803'] = func_1803
mod = relay.transform.InferType()(mod)
mutated_mod['func_1803'] = func_1803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1803_call = mutated_mod.get_global_var('func_1803')
call_1804 = func_1803_call()
output = call_1804
func_1805 = relay.Function([], output)
mutated_mod['func_1805'] = func_1805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
call_1843 = relay.TupleGetItem(func_592_call(), 0)
call_1844 = relay.TupleGetItem(func_594_call(), 0)
output = call_1843
output2 = call_1844
func_1845 = relay.Function([], output)
mod['func_1845'] = func_1845
mod = relay.transform.InferType()(mod)
output = func_1845()
func_1846 = relay.Function([], output)
mutated_mod['func_1846'] = func_1846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1469_call = mod.get_global_var('func_1469')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_1964 = relay.TupleGetItem(func_1469_call(), 1)
call_1965 = relay.TupleGetItem(func_1470_call(), 1)
func_1124_call = mod.get_global_var('func_1124')
func_1126_call = mutated_mod.get_global_var('func_1126')
call_1973 = func_1124_call()
call_1974 = func_1124_call()
func_564_call = mod.get_global_var('func_564')
func_566_call = mutated_mod.get_global_var('func_566')
call_1982 = relay.TupleGetItem(func_564_call(), 0)
call_1983 = relay.TupleGetItem(func_566_call(), 0)
output = relay.Tuple([call_1964,call_1973,call_1982,])
output2 = relay.Tuple([call_1965,call_1974,call_1983,])
func_1985 = relay.Function([], output)
mod['func_1985'] = func_1985
mod = relay.transform.InferType()(mod)
mutated_mod['func_1985'] = func_1985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1985_call = mutated_mod.get_global_var('func_1985')
call_1986 = func_1985_call()
output = call_1986
func_1987 = relay.Function([], output)
mutated_mod['func_1987'] = func_1987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
call_2025 = relay.TupleGetItem(func_592_call(), 0)
call_2026 = relay.TupleGetItem(func_594_call(), 0)
func_1232_call = mod.get_global_var('func_1232')
func_1235_call = mutated_mod.get_global_var('func_1235')
var_2055 = relay.var("var_2055", dtype = "int32", shape = (336,))#candidate|2055|(336,)|var|int32
call_2054 = relay.TupleGetItem(func_1232_call(relay.reshape(var_2055.astype('int32'), [336,])), 3)
call_2056 = relay.TupleGetItem(func_1235_call(relay.reshape(var_2055.astype('int32'), [336,])), 3)
var_2057 = relay.var("var_2057", dtype = "float64", shape = (5, 5, 9))#candidate|2057|(5, 5, 9)|var|float64
bop_2058 = relay.logical_or(call_2025.astype('bool'), var_2057.astype('bool')) # shape=(5, 5, 9)
bop_2061 = relay.logical_or(call_2026.astype('bool'), var_2057.astype('bool')) # shape=(5, 5, 9)
func_1024_call = mod.get_global_var('func_1024')
func_1026_call = mutated_mod.get_global_var('func_1026')
call_2079 = relay.TupleGetItem(func_1024_call(), 0)
call_2080 = relay.TupleGetItem(func_1026_call(), 0)
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_2084 = relay.TupleGetItem(func_1336_call(), 0)
call_2085 = relay.TupleGetItem(func_1338_call(), 0)
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
call_2087 = relay.TupleGetItem(func_592_call(), 0)
call_2088 = relay.TupleGetItem(func_594_call(), 0)
output = relay.Tuple([call_2054,var_2055,bop_2058,call_2079,call_2084,call_2087,])
output2 = relay.Tuple([call_2056,var_2055,bop_2061,call_2080,call_2085,call_2088,])
func_2089 = relay.Function([var_2055,var_2057,], output)
mod['func_2089'] = func_2089
mod = relay.transform.InferType()(mod)
mutated_mod['func_2089'] = func_2089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2089_call = mutated_mod.get_global_var('func_2089')
var_2091 = relay.var("var_2091", dtype = "int32", shape = (336,))#candidate|2091|(336,)|var|int32
var_2092 = relay.var("var_2092", dtype = "float64", shape = (5, 5, 9))#candidate|2092|(5, 5, 9)|var|float64
call_2090 = func_2089_call(var_2091,var_2092,)
output = call_2090
func_2093 = relay.Function([var_2091,var_2092,], output)
mutated_mod['func_2093'] = func_2093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1469_call = mod.get_global_var('func_1469')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_2124 = relay.TupleGetItem(func_1469_call(), 0)
call_2125 = relay.TupleGetItem(func_1470_call(), 0)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
var_2133 = relay.var("var_2133", dtype = "float64", shape = (405,))#candidate|2133|(405,)|var|float64
call_2132 = relay.TupleGetItem(func_1431_call(relay.reshape(var_2133.astype('float64'), [9, 5, 9])), 0)
call_2134 = relay.TupleGetItem(func_1433_call(relay.reshape(var_2133.astype('float64'), [9, 5, 9])), 0)
output = relay.Tuple([call_2124,call_2132,var_2133,])
output2 = relay.Tuple([call_2125,call_2134,var_2133,])
func_2140 = relay.Function([var_2133,], output)
mod['func_2140'] = func_2140
mod = relay.transform.InferType()(mod)
mutated_mod['func_2140'] = func_2140
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2141 = relay.var("var_2141", dtype = "float64", shape = (405,))#candidate|2141|(405,)|var|float64
func_2140_call = mutated_mod.get_global_var('func_2140')
call_2142 = func_2140_call(var_2141)
output = call_2142
func_2143 = relay.Function([var_2141], output)
mutated_mod['func_2143'] = func_2143
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2167 = relay.var("var_2167", dtype = "bool", shape = (15, 5, 9))#candidate|2167|(15, 5, 9)|var|bool
var_2168 = relay.var("var_2168", dtype = "bool", shape = (15, 5, 9))#candidate|2168|(15, 5, 9)|var|bool
bop_2169 = relay.logical_or(var_2167.astype('bool'), relay.reshape(var_2168.astype('bool'), relay.shape_of(var_2167))) # shape=(15, 5, 9)
output = relay.Tuple([bop_2169,])
output2 = relay.Tuple([bop_2169,])
func_2180 = relay.Function([var_2167,var_2168,], output)
mod['func_2180'] = func_2180
mod = relay.transform.InferType()(mod)
var_2181 = relay.var("var_2181", dtype = "bool", shape = (15, 5, 9))#candidate|2181|(15, 5, 9)|var|bool
var_2182 = relay.var("var_2182", dtype = "bool", shape = (15, 5, 9))#candidate|2182|(15, 5, 9)|var|bool
output = func_2180(var_2181,var_2182,)
func_2183 = relay.Function([var_2181,var_2182,], output)
mutated_mod['func_2183'] = func_2183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_2275 = func_1803_call()
call_2276 = func_1803_call()
output = call_2275
output2 = call_2276
func_2290 = relay.Function([], output)
mod['func_2290'] = func_2290
mod = relay.transform.InferType()(mod)
output = func_2290()
func_2291 = relay.Function([], output)
mutated_mod['func_2291'] = func_2291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_2339 = func_314_call()
call_2340 = func_314_call()
func_704_call = mod.get_global_var('func_704')
func_706_call = mutated_mod.get_global_var('func_706')
call_2365 = relay.TupleGetItem(func_704_call(), 0)
call_2366 = relay.TupleGetItem(func_706_call(), 0)
var_2372 = relay.var("var_2372", dtype = "uint64", shape = (13, 5, 9))#candidate|2372|(13, 5, 9)|var|uint64
bop_2373 = relay.logical_and(call_2365.astype('bool'), var_2372.astype('bool')) # shape=(13, 5, 9)
bop_2376 = relay.logical_and(call_2366.astype('bool'), var_2372.astype('bool')) # shape=(13, 5, 9)
func_1594_call = mod.get_global_var('func_1594')
func_1597_call = mutated_mod.get_global_var('func_1597')
var_2389 = relay.var("var_2389", dtype = "float32", shape = (1, 63))#candidate|2389|(1, 63)|var|float32
call_2388 = relay.TupleGetItem(func_1594_call(relay.reshape(var_2389.astype('float32'), [7, 3, 3])), 1)
call_2390 = relay.TupleGetItem(func_1597_call(relay.reshape(var_2389.astype('float32'), [7, 3, 3])), 1)
output = relay.Tuple([call_2339,bop_2373,call_2388,var_2389,])
output2 = relay.Tuple([call_2340,bop_2376,call_2390,var_2389,])
func_2392 = relay.Function([var_2372,var_2389,], output)
mod['func_2392'] = func_2392
mod = relay.transform.InferType()(mod)
mutated_mod['func_2392'] = func_2392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2392_call = mutated_mod.get_global_var('func_2392')
var_2394 = relay.var("var_2394", dtype = "uint64", shape = (13, 5, 9))#candidate|2394|(13, 5, 9)|var|uint64
var_2395 = relay.var("var_2395", dtype = "float32", shape = (1, 63))#candidate|2395|(1, 63)|var|float32
call_2393 = func_2392_call(var_2394,var_2395,)
output = call_2393
func_2396 = relay.Function([var_2394,var_2395,], output)
mutated_mod['func_2396'] = func_2396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_2566 = func_791_call()
call_2567 = func_791_call()
output = call_2566
output2 = call_2567
func_2582 = relay.Function([], output)
mod['func_2582'] = func_2582
mod = relay.transform.InferType()(mod)
mutated_mod['func_2582'] = func_2582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2582_call = mutated_mod.get_global_var('func_2582')
call_2583 = func_2582_call()
output = call_2583
func_2584 = relay.Function([], output)
mutated_mod['func_2584'] = func_2584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_2630 = relay.TupleGetItem(func_1336_call(), 0)
call_2631 = relay.TupleGetItem(func_1338_call(), 0)
uop_2632 = relay.rsqrt(call_2630.astype('float32')) # shape=(1, 5, 9)
uop_2634 = relay.rsqrt(call_2631.astype('float32')) # shape=(1, 5, 9)
func_506_call = mod.get_global_var('func_506')
func_509_call = mutated_mod.get_global_var('func_509')
const_2639 = relay.const([[9.853509,-9.823282],[-1.377939,4.722719],[1.184858,6.364011],[-8.533842,6.216864],[-7.842537,-9.147809],[-2.732585,-6.140678],[-3.766247,-5.036223],[6.316389,2.891262],[1.035739,-0.470478],[-8.860340,8.726297],[6.730812,-1.540034],[7.651227,-4.599278],[4.503977,-5.015966],[9.435314,8.959438],[7.025487,-1.135230],[-2.002523,5.880813],[-0.025551,7.715867],[-7.678274,-8.473836],[3.841850,5.544236],[-5.899529,-5.351293],[-2.813857,9.072866],[-7.169261,-0.351272],[-2.727646,-6.298484],[-4.015342,-9.945598]], dtype = "float64")#candidate|2639|(24, 2)|const|float64
call_2638 = relay.TupleGetItem(func_506_call(relay.reshape(const_2639.astype('float64'), [3, 2, 8]), relay.reshape(const_2639.astype('float64'), [3, 2, 8]), ), 0)
call_2640 = relay.TupleGetItem(func_509_call(relay.reshape(const_2639.astype('float64'), [3, 2, 8]), relay.reshape(const_2639.astype('float64'), [3, 2, 8]), ), 0)
output = relay.Tuple([uop_2632,call_2638,const_2639,])
output2 = relay.Tuple([uop_2634,call_2640,const_2639,])
func_2643 = relay.Function([], output)
mod['func_2643'] = func_2643
mod = relay.transform.InferType()(mod)
output = func_2643()
func_2644 = relay.Function([], output)
mutated_mod['func_2644'] = func_2644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_2676 = func_480_call()
call_2677 = func_480_call()
output = relay.Tuple([call_2676,])
output2 = relay.Tuple([call_2677,])
func_2680 = relay.Function([], output)
mod['func_2680'] = func_2680
mod = relay.transform.InferType()(mod)
output = func_2680()
func_2681 = relay.Function([], output)
mutated_mod['func_2681'] = func_2681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1124_call = mod.get_global_var('func_1124')
func_1126_call = mutated_mod.get_global_var('func_1126')
call_2700 = func_1124_call()
call_2701 = func_1124_call()
var_2705 = relay.var("var_2705", dtype = "float64", shape = (8, 5, 9))#candidate|2705|(8, 5, 9)|var|float64
bop_2706 = relay.right_shift(call_2700.astype('uint8'), var_2705.astype('uint8')) # shape=(8, 5, 9)
bop_2709 = relay.right_shift(call_2701.astype('uint8'), var_2705.astype('uint8')) # shape=(8, 5, 9)
func_1124_call = mod.get_global_var('func_1124')
func_1126_call = mutated_mod.get_global_var('func_1126')
call_2714 = func_1124_call()
call_2715 = func_1124_call()
output = relay.Tuple([bop_2706,call_2714,])
output2 = relay.Tuple([bop_2709,call_2715,])
func_2747 = relay.Function([var_2705,], output)
mod['func_2747'] = func_2747
mod = relay.transform.InferType()(mod)
var_2748 = relay.var("var_2748", dtype = "float64", shape = (8, 5, 9))#candidate|2748|(8, 5, 9)|var|float64
output = func_2747(var_2748)
func_2749 = relay.Function([var_2748], output)
mutated_mod['func_2749'] = func_2749
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2771 = relay.var("var_2771", dtype = "uint32", shape = (12, 10, 12))#candidate|2771|(12, 10, 12)|var|uint32
var_2772 = relay.var("var_2772", dtype = "uint32", shape = (12, 10, 12))#candidate|2772|(12, 10, 12)|var|uint32
bop_2773 = relay.left_shift(var_2771.astype('uint32'), relay.reshape(var_2772.astype('uint32'), relay.shape_of(var_2771))) # shape=(12, 10, 12)
func_2392_call = mod.get_global_var('func_2392')
func_2396_call = mutated_mod.get_global_var('func_2396')
const_2789 = relay.const([-1,-2,5,-3,7,3,8,8,2,-5,4,-2,-1,8,7,1,2,-10,-9,9,5,-8,7,2,-7,-2,8,5,10,-5,7,-6,1,-7,-1,6,8,8,9,7,-8,9,10,-5,9,9,10,-8,3,1,2,1,-3,-5,8,10,-10,-2,-5,3,1,-2,9,-1,-3,-10,2,-5,8,-7,4,4,8,-6,-7,7,-3,6,-8,8,-1,-8,-8,6,-7,-4,-2,-6,-6,-3,1,10,10,-8,5,2,2,7,-7,6,7,4,10,-2,-2,1,7,-7,-9,7,-1,-10,-1,3,-1,1,-8,-9,-4,-7,8,-2,-1,-3,-6,-6,9,9,4,-7,8,-7,2,-9,9,-5,-5,-3,7,-7,-6,9,-1,-5,-10,-2,-2,-7,4,-3,1,1,6,-4,-2,6,-6,-3,-3,1,-5,-2,-1,1,6,-10,3,-2,-9,-10,9,-9,10,9,-4,-9,-3,-6,-1,-2,3,3,-7,-3,-3,-7,10,5,-10,5,7,3,-4,-6,7,1,2,-6,-1,5,-1,-4,10,2,8,-6,-1,4,-7,2,8,4,9,9,8,-2,10,-1,-9,-2,10,9,6,-9,-4,9,-4,2,-2,3,-8,-2,-5,9,-5,1,9,-9,3,-10,-8,-9,-1,-8,-3,-4,8,-1,8,-4,-1,2,-7,6,6,-9,2,-7,-10,-7,-5,-5,-10,3,6,-3,-6,-8,-4,3,8,-6,-9,-7,-7,-5,7,7,-8,-5,2,1,5,-9,4,10,-3,6,1,-2,-8,-3,6,-4,2,9,1,2,-3,-6,-2,-1,-5,8,10,6,-8,7,-1,-10,-2,7,-3,9,9,-3,4,-7,-2,-4,-8,2,-9,1,10,3,2,-7,-8,-9,2,1,7,-4,4,1,6,7,4,5,9,10,-7,-4,-3,-5,4,-10,3,-10,-10,8,-8,-1,-1,8,4,1,5,10,8,-3,-1,-5,-5,-1,6,2,4,-8,-2,7,4,-1,1,7,7,4,-2,-4,4,3,7,-5,1,-6,-10,10,10,5,5,3,-1,-1,5,-2,-1,8,10,-6,7,-3,6,-10,-7,10,-6,-3,1,2,9,5,-8,-5,8,-9,-7,9,8,-2,4,-8,-4,-7,-6,10,-2,-3,-10,7,2,-1,8,2,1,2,7,-4,-10,-5,10,2,-2,2,-5,-10,-5,-8,2,1,-6,-9,-3,-4,-7,-9,-6,-9,-8,-2,2,-10,2,-9,7,-2,-3,4,5,8,8,-9,10,5,-2,9,-7,-8,8,-7,-9,8,9,7,1,-8,-5,-3,8,5,5,2,4,2,9,-6,6,10,9,1,-7,1,5,-8,-4,-3,-6,10,4,3,1,4,5,-5,5,4,-3,3,9,-3,4,-1,-10,2,2,1,-5,1,1,6,-1,6,-7,6,-2,-10,-6,7,-1,1,-6,-7,9,3,-5,6,1,-2,2,-6,-8,9,7,-9,8,-2,-4,5,8,-3,-9,10,2,-8,-1,-9,1,2,-5,-6,3,-7,-6,2,2,-8,-8,-1,-2,5,5,6,-1,6,1], dtype = "uint64")#candidate|2789|(585,)|const|uint64
var_2790 = relay.var("var_2790", dtype = "float32", shape = (63,))#candidate|2790|(63,)|var|float32
call_2788 = relay.TupleGetItem(func_2392_call(relay.reshape(const_2789.astype('uint64'), [13, 5, 9]), relay.reshape(var_2790.astype('float32'), [1, 63]), ), 3)
call_2791 = relay.TupleGetItem(func_2396_call(relay.reshape(const_2789.astype('uint64'), [13, 5, 9]), relay.reshape(var_2790.astype('float32'), [1, 63]), ), 3)
func_1737_call = mod.get_global_var('func_1737')
func_1739_call = mutated_mod.get_global_var('func_1739')
call_2795 = relay.TupleGetItem(func_1737_call(), 0)
call_2796 = relay.TupleGetItem(func_1739_call(), 0)
var_2797 = relay.var("var_2797", dtype = "uint32", shape = (12, 10, 12))#candidate|2797|(12, 10, 12)|var|uint32
bop_2798 = relay.bitwise_or(bop_2773.astype('int16'), relay.reshape(var_2797.astype('int16'), relay.shape_of(bop_2773))) # shape=(12, 10, 12)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_2801 = func_314_call()
call_2802 = func_314_call()
func_1985_call = mod.get_global_var('func_1985')
func_1987_call = mutated_mod.get_global_var('func_1987')
call_2805 = relay.TupleGetItem(func_1985_call(), 1)
call_2806 = relay.TupleGetItem(func_1987_call(), 1)
func_454_call = mod.get_global_var('func_454')
func_456_call = mutated_mod.get_global_var('func_456')
call_2841 = relay.TupleGetItem(func_454_call(), 0)
call_2842 = relay.TupleGetItem(func_456_call(), 0)
output = relay.Tuple([call_2788,const_2789,var_2790,call_2795,bop_2798,call_2801,call_2805,call_2841,])
output2 = relay.Tuple([call_2791,const_2789,var_2790,call_2796,bop_2798,call_2802,call_2806,call_2842,])
func_2849 = relay.Function([var_2771,var_2772,var_2790,var_2797,], output)
mod['func_2849'] = func_2849
mod = relay.transform.InferType()(mod)
mutated_mod['func_2849'] = func_2849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2849_call = mutated_mod.get_global_var('func_2849')
var_2851 = relay.var("var_2851", dtype = "uint32", shape = (12, 10, 12))#candidate|2851|(12, 10, 12)|var|uint32
var_2852 = relay.var("var_2852", dtype = "uint32", shape = (12, 10, 12))#candidate|2852|(12, 10, 12)|var|uint32
var_2853 = relay.var("var_2853", dtype = "float32", shape = (63,))#candidate|2853|(63,)|var|float32
var_2854 = relay.var("var_2854", dtype = "uint32", shape = (12, 10, 12))#candidate|2854|(12, 10, 12)|var|uint32
call_2850 = func_2849_call(var_2851,var_2852,var_2853,var_2854,)
output = call_2850
func_2855 = relay.Function([var_2851,var_2852,var_2853,var_2854,], output)
mutated_mod['func_2855'] = func_2855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1124_call = mod.get_global_var('func_1124')
func_1126_call = mutated_mod.get_global_var('func_1126')
call_2868 = func_1124_call()
call_2869 = func_1124_call()
output = call_2868
output2 = call_2869
func_2872 = relay.Function([], output)
mod['func_2872'] = func_2872
mod = relay.transform.InferType()(mod)
mutated_mod['func_2872'] = func_2872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2872_call = mutated_mod.get_global_var('func_2872')
call_2873 = func_2872_call()
output = call_2873
func_2874 = relay.Function([], output)
mutated_mod['func_2874'] = func_2874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1567_call = mod.get_global_var('func_1567')
func_1568_call = mutated_mod.get_global_var('func_1568')
call_2929 = relay.TupleGetItem(func_1567_call(), 0)
call_2930 = relay.TupleGetItem(func_1568_call(), 0)
func_1469_call = mod.get_global_var('func_1469')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_2941 = relay.TupleGetItem(func_1469_call(), 0)
call_2942 = relay.TupleGetItem(func_1470_call(), 0)
output = relay.Tuple([call_2929,call_2941,])
output2 = relay.Tuple([call_2930,call_2942,])
func_2943 = relay.Function([], output)
mod['func_2943'] = func_2943
mod = relay.transform.InferType()(mod)
output = func_2943()
func_2944 = relay.Function([], output)
mutated_mod['func_2944'] = func_2944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mod.get_global_var('func_935')
func_937_call = mutated_mod.get_global_var('func_937')
call_2951 = relay.TupleGetItem(func_935_call(), 0)
call_2952 = relay.TupleGetItem(func_937_call(), 0)
output = relay.Tuple([call_2951,])
output2 = relay.Tuple([call_2952,])
func_2958 = relay.Function([], output)
mod['func_2958'] = func_2958
mod = relay.transform.InferType()(mod)
output = func_2958()
func_2959 = relay.Function([], output)
mutated_mod['func_2959'] = func_2959
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2978 = relay.var("var_2978", dtype = "float64", shape = (11, 16, 15))#candidate|2978|(11, 16, 15)|var|float64
uop_2979 = relay.cos(var_2978.astype('float64')) # shape=(11, 16, 15)
output = relay.Tuple([uop_2979,])
output2 = relay.Tuple([uop_2979,])
func_2982 = relay.Function([var_2978,], output)
mod['func_2982'] = func_2982
mod = relay.transform.InferType()(mod)
var_2983 = relay.var("var_2983", dtype = "float64", shape = (11, 16, 15))#candidate|2983|(11, 16, 15)|var|float64
output = func_2982(var_2983)
func_2984 = relay.Function([var_2983], output)
mutated_mod['func_2984'] = func_2984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_3028 = func_480_call()
call_3029 = func_480_call()
func_1232_call = mod.get_global_var('func_1232')
func_1235_call = mutated_mod.get_global_var('func_1235')
const_3031 = relay.const([9,-2,-2,2,2,-7,1,7,-10,1,-1,-10,6,3,1,1,-5,5,-1,1,4,-6,7,-6,-4,-5,-1,9,-8,3,6,9,8,1,2,3,-10,-3,-4,-4,-6,-3,-5,6,-7,-3,4,-6,-6,4,-9,-6,-3,5,-7,-6,-7,-2,3,6,-9,-5,-10,7,-8,-6,5,-5,2,-8,7,4,4,6,5,9,8,-7,5,-6,3,9,7,-8,1,8,9,2,7,1,8,6,-2,-6,-4,-9,8,7,-9,2,9,8,9,1,7,-8,2,3,-6,2,-3,9,8,-7,-10,-8,9,9,7,-6,2,1,9,-9,-5,6,-3,-3,2,-9,-9,3,3,7,-2,6,10,-9,5,7,2,-10,-10,-5,3,7,10,-1,2,5,-5,-9,10,6,-7,-5,-6,-5,10,-1,5,-6,-5,-8,-6,-10,-3,8,6,-7,6,-3,7,-1,9,9,-7,7,-9,-1,-7,8,8,1,9,-9,10,-9,2,-3,1,3,4,-2,-4,-9,-3,-10,4,-9,1,-8,-9,-7,7,10,-9,-8,4,7,-4,-10,7,2,-1,-2,8,-3,-7,8,10,1,-4,4,8,5,-2,-1,-4,8,-1,-10,-2,-5,-3,4,4,5,-4,-5,10,6,-2,-1,-9,4,9,10,6,2,-2,-5,2,4,6,-2,-9,10,-7,-10,10,-8,-7,-2,-4,4,-9,-4,-6,-8,-10,-1,-9,2,2,4,-7,10,-9,-9,-5,2,-2,6,5,-2,-4,-1,6,1,-7,-9,-7,8,-9,10,-2,1,-9,3,3,-6,-10,4,-2,5,1,-4,3,4,-9,-8,-9,4,-8,-1,-2,-9,-5,2,7,-7,-1,5,-2,-8,5,3,-6,3,4,4,8,10,-6,3], dtype = "int32")#candidate|3031|(336,)|const|int32
call_3030 = relay.TupleGetItem(func_1232_call(relay.reshape(const_3031.astype('int32'), [336,])), 3)
call_3032 = relay.TupleGetItem(func_1235_call(relay.reshape(const_3031.astype('int32'), [336,])), 3)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_3059 = func_1803_call()
call_3060 = func_1803_call()
output = relay.Tuple([call_3028,call_3030,const_3031,call_3059,])
output2 = relay.Tuple([call_3029,call_3032,const_3031,call_3060,])
func_3069 = relay.Function([], output)
mod['func_3069'] = func_3069
mod = relay.transform.InferType()(mod)
output = func_3069()
func_3070 = relay.Function([], output)
mutated_mod['func_3070'] = func_3070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_3100 = func_380_call()
call_3101 = func_380_call()
var_3109 = relay.var("var_3109", dtype = "uint64", shape = (5, 5, 9))#candidate|3109|(5, 5, 9)|var|uint64
bop_3110 = relay.not_equal(call_3100.astype('bool'), var_3109.astype('bool')) # shape=(5, 5, 9)
bop_3113 = relay.not_equal(call_3101.astype('bool'), var_3109.astype('bool')) # shape=(5, 5, 9)
output = relay.Tuple([bop_3110,])
output2 = relay.Tuple([bop_3113,])
func_3115 = relay.Function([var_3109,], output)
mod['func_3115'] = func_3115
mod = relay.transform.InferType()(mod)
var_3116 = relay.var("var_3116", dtype = "uint64", shape = (5, 5, 9))#candidate|3116|(5, 5, 9)|var|uint64
output = func_3115(var_3116)
func_3117 = relay.Function([var_3116], output)
mutated_mod['func_3117'] = func_3117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1469_call = mod.get_global_var('func_1469')
func_1470_call = mutated_mod.get_global_var('func_1470')
call_3146 = relay.TupleGetItem(func_1469_call(), 1)
call_3147 = relay.TupleGetItem(func_1470_call(), 1)
output = call_3146
output2 = call_3147
func_3155 = relay.Function([], output)
mod['func_3155'] = func_3155
mod = relay.transform.InferType()(mod)
output = func_3155()
func_3156 = relay.Function([], output)
mutated_mod['func_3156'] = func_3156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_3210 = func_791_call()
call_3211 = func_791_call()
output = call_3210
output2 = call_3211
func_3214 = relay.Function([], output)
mod['func_3214'] = func_3214
mod = relay.transform.InferType()(mod)
output = func_3214()
func_3215 = relay.Function([], output)
mutated_mod['func_3215'] = func_3215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3214_call = mod.get_global_var('func_3214')
func_3215_call = mutated_mod.get_global_var('func_3215')
call_3245 = func_3214_call()
call_3246 = func_3214_call()
output = relay.Tuple([call_3245,])
output2 = relay.Tuple([call_3246,])
func_3247 = relay.Function([], output)
mod['func_3247'] = func_3247
mod = relay.transform.InferType()(mod)
output = func_3247()
func_3248 = relay.Function([], output)
mutated_mod['func_3248'] = func_3248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1737_call = mod.get_global_var('func_1737')
func_1739_call = mutated_mod.get_global_var('func_1739')
call_3297 = relay.TupleGetItem(func_1737_call(), 1)
call_3298 = relay.TupleGetItem(func_1739_call(), 1)
output = relay.Tuple([call_3297,])
output2 = relay.Tuple([call_3298,])
func_3299 = relay.Function([], output)
mod['func_3299'] = func_3299
mod = relay.transform.InferType()(mod)
mutated_mod['func_3299'] = func_3299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3299_call = mutated_mod.get_global_var('func_3299')
call_3300 = func_3299_call()
output = call_3300
func_3301 = relay.Function([], output)
mutated_mod['func_3301'] = func_3301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_3330 = func_380_call()
call_3331 = func_380_call()
const_3364 = relay.const([[[-8,2,-4,-6,-5,-3,-9,-9,6],[1,1,4,5,-4,2,10,4,6],[5,2,-10,-2,-6,6,-9,5,-4],[-2,3,-6,3,-8,6,-7,-6,10],[6,5,-2,-3,7,-3,-8,-10,8]]], dtype = "uint64")#candidate|3364|(1, 5, 9)|const|uint64
bop_3365 = relay.bitwise_xor(call_3330.astype('uint8'), relay.reshape(const_3364.astype('uint8'), relay.shape_of(call_3330))) # shape=(1, 5, 9)
bop_3368 = relay.bitwise_xor(call_3331.astype('uint8'), relay.reshape(const_3364.astype('uint8'), relay.shape_of(call_3331))) # shape=(1, 5, 9)
uop_3393 = relay.log2(const_3364.astype('float64')) # shape=(1, 5, 9)
output = relay.Tuple([bop_3365,uop_3393,])
output2 = relay.Tuple([bop_3368,uop_3393,])
func_3398 = relay.Function([], output)
mod['func_3398'] = func_3398
mod = relay.transform.InferType()(mod)
mutated_mod['func_3398'] = func_3398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3398_call = mutated_mod.get_global_var('func_3398')
call_3399 = func_3398_call()
output = call_3399
func_3400 = relay.Function([], output)
mutated_mod['func_3400'] = func_3400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3069_call = mod.get_global_var('func_3069')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_3472 = relay.TupleGetItem(func_3069_call(), 2)
call_3473 = relay.TupleGetItem(func_3070_call(), 2)
func_704_call = mod.get_global_var('func_704')
func_706_call = mutated_mod.get_global_var('func_706')
call_3494 = relay.TupleGetItem(func_704_call(), 0)
call_3495 = relay.TupleGetItem(func_706_call(), 0)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_3496 = func_1845_call()
call_3497 = func_1845_call()
output = relay.Tuple([call_3472,call_3494,call_3496,])
output2 = relay.Tuple([call_3473,call_3495,call_3497,])
func_3523 = relay.Function([], output)
mod['func_3523'] = func_3523
mod = relay.transform.InferType()(mod)
mutated_mod['func_3523'] = func_3523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3523_call = mutated_mod.get_global_var('func_3523')
call_3524 = func_3523_call()
output = call_3524
func_3525 = relay.Function([], output)
mutated_mod['func_3525'] = func_3525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3523_call = mod.get_global_var('func_3523')
func_3525_call = mutated_mod.get_global_var('func_3525')
call_3575 = relay.TupleGetItem(func_3523_call(), 2)
call_3576 = relay.TupleGetItem(func_3525_call(), 2)
output = call_3575
output2 = call_3576
func_3586 = relay.Function([], output)
mod['func_3586'] = func_3586
mod = relay.transform.InferType()(mod)
output = func_3586()
func_3587 = relay.Function([], output)
mutated_mod['func_3587'] = func_3587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_3701 = func_1803_call()
call_3702 = func_1803_call()
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
const_3706 = relay.const([3.632020,-8.050772,-7.712212,0.410366,-1.698797,7.991405,-3.342946,8.536550,9.508661,-0.283087,1.763636,-4.562451,-1.533369,7.107120,9.079497,-3.301638,-1.695861,-7.752031,-3.725771,3.800160,-7.493734,9.266805,-8.417980,7.222383,5.458674,-8.723972,-3.030967,-9.409952,-2.029636,-4.117101,4.107391,-0.012457,7.245956,-3.678129,-1.550469,9.517534,-8.296465,9.697565,8.304898,5.988733,-8.945343,6.144562,-7.125080,-2.856534,3.196100,-2.824964,9.545181,-3.454367,-8.654523,-0.107263,-7.226813,3.868179,-4.264002,-0.552686,6.948242,6.774216,9.198308,-8.917382,-0.856628,-2.577882,1.467349,-4.543795,1.445874,-8.130108,5.101625,-2.599266,-0.629377,9.792491,-2.354250,-8.821954,1.218952,-7.127073,-1.890583,-8.322907,5.844404,-1.035167,3.210389,3.340918,-3.943892,-9.714318,2.162053,5.226710,-4.190902,-1.464599,-9.485976,-6.863271,-5.662793,-9.318143,2.820322,6.455796,9.527535,-7.544818,-6.282603,3.166835,7.986149,4.915726,-9.954704,-8.509183,8.630665,-3.010502,7.524436,2.148468,3.889357,-7.083046,-1.836953,4.586448,6.898058,-2.109397,9.502605,-0.863513,-3.572039,7.483278,8.843855,8.831478,8.697725,-3.005693,9.049022,-5.549875,-4.813498,5.738894,8.034200,-7.729721,-4.809220,-9.255262,2.081496,-5.354115,-4.902108,-6.920842,8.597893,-5.686508,0.234203,9.287923,-3.611193,3.549670,-2.203732,9.794010,8.855150,3.015765,6.492308,-3.217090,-4.488704,-3.008685,-1.084809,-6.232805,-5.635329,-9.517682,-2.819286,-0.111736,-1.007529,2.388012,3.825978,-8.624894,-3.817534,-8.249661,5.440460,-8.862984,-7.151307,5.610390,-6.661848,-2.641390,-6.174722,-8.195019,2.267883,-9.212858,3.674327,-2.001023,-2.498704,0.756352,-2.234705,-7.001184,-9.299266,-7.821906,8.329627,-3.366655,4.577925,3.296930,3.423514,-4.763097,-9.015376,-4.274068,-0.080161,-7.428415,1.532788,-4.387300,-2.279319,-4.753779,6.689748,9.031047,-9.874980,-2.187263,-3.264275,2.964648,-4.898746,-7.659474,-9.481071,-2.550940,-6.956993,-7.473772,-8.258822,0.989569,3.238299,-9.844607,-7.812361,-4.572061,4.284800,6.929871,-2.824445,6.768799,-8.910949,0.088238,2.225515,-0.549231,4.399306,6.349359,0.581546,-3.121972,-7.170521,0.914198,-3.038874,0.289666,1.721012,4.113800,-8.925348,-1.816422,3.878011,7.003214,6.493081,-1.498278,-8.186411,-3.605602,-0.501261,2.337182,5.204172,-1.886600,-3.055539,3.778753,-3.443973,1.552439,-8.094356,6.790300,9.952127,-5.482106,-9.775976,4.418195,-4.475697,-1.784407,-4.202328,-3.850343,9.111529,5.278130,-3.021127,6.861376,-8.979669,5.573560,-0.803277,-1.249578,-4.883428,-3.580334,3.824859,8.089013,5.426493,-0.691035,5.484051,-4.925542,8.908212,-4.334458,-4.110706,-9.352639,-3.922015,0.373117,0.912649,5.118626,-3.661195,-7.725632,3.652851,-1.889903,-3.545723,2.731867,1.554877,-0.145290,8.799016,-0.853930,-1.724021,-1.290656,0.681995,0.746237,8.630759,-7.278968,-6.917325,5.742823,-7.558894,-4.120390,3.781278,3.873459,3.590140,6.196521,-6.395001,8.353020,8.430410,-2.473325,0.014084,4.042667,-1.856325,4.450841,-2.994942,-8.094785,-9.266883,3.830744,-1.433040,-8.977372,-8.652308,0.516478,5.069605,3.991414,-6.092950,7.998736,5.529518,0.271600,-4.767603,-7.109415,9.005047,-6.411900,-2.740293,7.733453,-6.222107,-7.098158,-6.384154,1.252806,-2.938530,-2.214466,-8.677295,0.459157,-3.791370,4.552868,5.166658,3.216924,4.592236,-6.118823,-0.226224,-9.816854,5.826422,8.250589,-9.008939,3.704800,-5.957260,-7.772384,-5.108796,-4.695952,-9.780271,9.850162,-0.181130,-6.142342,-4.983317,9.882005,8.584725,7.924919,-4.015768,-5.615608,-5.390691,-3.643226,5.846265,6.082002,-7.637317,-4.204393,-4.798194,-9.023692,-6.247481,-3.362717,2.089280,3.621379,0.670951,2.198044,-4.362114,0.261986,0.663218,5.954404,-3.760755,-4.771645,-7.461181,5.010362,8.571049,8.127497,-7.533127,-6.357149,0.236528,-7.901000,8.299231,0.415670,2.314506,-3.159515,-5.722407,1.882666,-8.593718,1.399559,-9.922700,3.580556,-2.967376,-6.683373,-5.666579,-5.626567,-8.969601,7.651909,-5.994736,1.143704,1.948392], dtype = "float64")#candidate|3706|(405,)|const|float64
call_3705 = relay.TupleGetItem(func_1431_call(relay.reshape(const_3706.astype('float64'), [9, 5, 9])), 0)
call_3707 = relay.TupleGetItem(func_1433_call(relay.reshape(const_3706.astype('float64'), [9, 5, 9])), 0)
uop_3708 = relay.sigmoid(const_3706.astype('float64')) # shape=(405,)
func_2089_call = mod.get_global_var('func_2089')
func_2093_call = mutated_mod.get_global_var('func_2093')
const_3719 = relay.const([-3,7,-8,-4,-5,-3,-3,-5,2,-9,-10,-3,-7,-9,9,7,10,-4,1,1,3,5,4,-4,2,3,10,-6,1,3,-3,5,-8,-4,-9,7,8,9,3,-8,9,-9,-9,5,2,3,-2,-1,-7,1,9,-7,-1,-10,-10,-3,2,-7,9,-3,1,6,-4,4,-1,5,-3,8,-9,-10,7,-7,7,1,3,5,-2,7,-10,-7,-6,-3,-7,2,-9,4,-8,-6,2,-1,3,-10,8,3,8,1,4,-2,-4,6,9,-1,10,3,5,10,-9,5,8,5,7,2,9,10,-8,-9,8,-5,-5,4,-10,10,-7,-5,2,-2,6,-10,-8,10,-9,-3,9,7,4,-8,6,-4,-4,9,-10,6,-5,-3,-7,10,-4,-2,1,-10,1,-1,-7,-1,3,8,-10,-1,1,9,9,-3,-10,-9,-4,-8,-9,5,4,-9,-5,2,3,10,7,3,7,-8,-3,-10,6,-6,-8,10,-5,1,-6,-5,6,5,5,9,6,-10,6,7,-9,6,-2,-9,5,-8,3,-4,-9,4,8,7,-5,-2,9,3,-10,5,-7,-8,-6,-7,-2,-10,9,6,-9,1,1,5,1,-10,-10,3,-1,2,-9,-6,2,-3,-2,-8,1,-7,3,4,3,-4,-1,10,2,-9,3,-4,-3,-7,4,-6,-7,1,8,-3,-9,1,6,2,-5,8,6,4,9,-4,7,1,-6,1,6,-2,2,5,-7,7,5,2,9,3,-7,10,1,-7,4,1,-5,4,-8,-7,-5,-1,-10,-6,-10,7,-7,3,-10,7,2,3,10,-3,8,5,4,4,8,-3,10,-8,-8,-7,3,2,1,-1,5,-1,-5,4,4,-5,9,-3,-9,8,-3,-6,8,-10,-3,3], dtype = "int32")#candidate|3719|(336,)|const|int32
var_3720 = relay.var("var_3720", dtype = "float64", shape = (75, 3))#candidate|3720|(75, 3)|var|float64
call_3718 = relay.TupleGetItem(func_2089_call(relay.reshape(const_3719.astype('int32'), [336,]), relay.reshape(var_3720.astype('float64'), [5, 5, 9]), ), 4)
call_3721 = relay.TupleGetItem(func_2093_call(relay.reshape(const_3719.astype('int32'), [336,]), relay.reshape(var_3720.astype('float64'), [5, 5, 9]), ), 4)
func_2180_call = mod.get_global_var('func_2180')
func_2183_call = mutated_mod.get_global_var('func_2183')
var_3723 = relay.var("var_3723", dtype = "bool", shape = (675,))#candidate|3723|(675,)|var|bool
call_3722 = relay.TupleGetItem(func_2180_call(relay.reshape(var_3723.astype('bool'), [15, 5, 9]), relay.reshape(var_3723.astype('bool'), [15, 5, 9]), ), 0)
call_3724 = relay.TupleGetItem(func_2183_call(relay.reshape(var_3723.astype('bool'), [15, 5, 9]), relay.reshape(var_3723.astype('bool'), [15, 5, 9]), ), 0)
output = relay.Tuple([call_3701,call_3705,uop_3708,call_3718,const_3719,var_3720,call_3722,var_3723,])
output2 = relay.Tuple([call_3702,call_3707,uop_3708,call_3721,const_3719,var_3720,call_3724,var_3723,])
func_3728 = relay.Function([var_3720,var_3723,], output)
mod['func_3728'] = func_3728
mod = relay.transform.InferType()(mod)
var_3729 = relay.var("var_3729", dtype = "float64", shape = (75, 3))#candidate|3729|(75, 3)|var|float64
var_3730 = relay.var("var_3730", dtype = "bool", shape = (675,))#candidate|3730|(675,)|var|bool
output = func_3728(var_3729,var_3730,)
func_3731 = relay.Function([var_3729,var_3730,], output)
mutated_mod['func_3731'] = func_3731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3155_call = mod.get_global_var('func_3155')
func_3156_call = mutated_mod.get_global_var('func_3156')
call_3763 = func_3155_call()
call_3764 = func_3155_call()
var_3775 = relay.var("var_3775", dtype = "uint64", shape = (1, 5, 9))#candidate|3775|(1, 5, 9)|var|uint64
bop_3776 = relay.floor_divide(call_3763.astype('float64'), relay.reshape(var_3775.astype('float64'), relay.shape_of(call_3763))) # shape=(1, 5, 9)
bop_3779 = relay.floor_divide(call_3764.astype('float64'), relay.reshape(var_3775.astype('float64'), relay.shape_of(call_3764))) # shape=(1, 5, 9)
output = bop_3776
output2 = bop_3779
func_3780 = relay.Function([var_3775,], output)
mod['func_3780'] = func_3780
mod = relay.transform.InferType()(mod)
mutated_mod['func_3780'] = func_3780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3781 = relay.var("var_3781", dtype = "uint64", shape = (1, 5, 9))#candidate|3781|(1, 5, 9)|var|uint64
func_3780_call = mutated_mod.get_global_var('func_3780')
call_3782 = func_3780_call(var_3781)
output = call_3782
func_3783 = relay.Function([var_3781], output)
mutated_mod['func_3783'] = func_3783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mod.get_global_var('func_935')
func_937_call = mutated_mod.get_global_var('func_937')
call_3871 = relay.TupleGetItem(func_935_call(), 0)
call_3872 = relay.TupleGetItem(func_937_call(), 0)
const_3875 = relay.const([[[4,-3,9,-10,8,10,4,4,8],[-1,6,8,8,3,6,6,-7,-6],[-4,-5,10,-4,9,-8,-4,1,-5],[-5,10,-9,-2,-6,-7,9,-7,-4],[2,-1,-10,9,8,-3,10,5,3]],[[-6,-2,8,-7,9,-1,-2,2,5],[4,5,5,-4,5,-7,-5,5,-9],[7,8,-1,10,6,-9,-6,-7,5],[-9,9,10,2,10,5,8,5,-9],[-9,-10,-4,5,9,1,6,-5,-3]],[[2,10,-1,-3,-8,-9,5,-7,10],[-3,1,9,-8,-1,-1,-5,8,-8],[4,-1,2,-1,-5,-3,2,-4,-9],[-7,9,9,-2,4,4,2,5,-2],[1,-5,6,5,-5,-2,-3,3,-7]],[[-1,-9,-9,-9,2,-4,3,8,4],[-8,-3,-10,-9,-2,-3,7,7,1],[10,9,-3,6,8,6,9,3,-8],[5,-3,2,-7,2,-6,2,-2,-7],[1,3,-7,-1,2,6,-6,9,-9]],[[7,-1,-10,1,-2,2,-10,-3,4],[1,-8,-1,4,7,-7,6,4,3],[4,-5,-9,-8,-2,9,4,-3,-4],[7,2,-3,2,-4,-7,-10,3,9],[-4,10,-9,4,-2,6,-3,-3,-8]],[[-5,8,-7,-8,-7,-4,-4,3,-6],[6,6,9,3,-6,9,5,-6,-3],[7,2,4,-10,6,-6,-8,4,-8],[5,-5,10,-6,-7,-7,5,-4,9],[3,-8,-3,-1,5,-4,-8,-6,1]],[[-8,10,-7,-6,2,9,7,1,9],[10,-4,5,9,8,-8,-3,5,-2],[2,-7,9,8,-8,-3,-6,8,7],[-9,-9,-4,-7,5,-10,-6,-6,-9],[-9,-3,9,-3,-9,4,-6,-2,1]]], dtype = "uint64")#candidate|3875|(7, 5, 9)|const|uint64
bop_3876 = relay.right_shift(call_3871.astype('uint16'), const_3875.astype('uint16')) # shape=(7, 5, 9)
bop_3879 = relay.right_shift(call_3872.astype('uint16'), const_3875.astype('uint16')) # shape=(7, 5, 9)
output = bop_3876
output2 = bop_3879
func_3883 = relay.Function([], output)
mod['func_3883'] = func_3883
mod = relay.transform.InferType()(mod)
output = func_3883()
func_3884 = relay.Function([], output)
mutated_mod['func_3884'] = func_3884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3155_call = mod.get_global_var('func_3155')
func_3156_call = mutated_mod.get_global_var('func_3156')
call_3917 = func_3155_call()
call_3918 = func_3155_call()
func_3586_call = mod.get_global_var('func_3586')
func_3587_call = mutated_mod.get_global_var('func_3587')
call_3927 = func_3586_call()
call_3928 = func_3586_call()
output = relay.Tuple([call_3917,call_3927,])
output2 = relay.Tuple([call_3918,call_3928,])
func_3942 = relay.Function([], output)
mod['func_3942'] = func_3942
mod = relay.transform.InferType()(mod)
output = func_3942()
func_3943 = relay.Function([], output)
mutated_mod['func_3943'] = func_3943
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3944 = relay.const([[[6.105146,5.023444,7.890479,4.267124,-6.898363,2.247813,9.586320,-7.878515,1.134713,5.947254,7.456360,4.468818,-4.967039,7.441478,9.266134],[-6.879424,-1.279026,9.427370,-1.022048,-0.529629,1.032061,0.908999,-6.238775,-8.079768,7.184977,-3.719292,2.326121,1.853905,-0.656648,0.829193],[-8.778723,-4.368428,3.275991,-9.725144,-4.312401,-6.882074,9.097375,-4.675570,-5.244708,9.739171,-1.440410,-3.570631,2.643835,1.055157,6.901673],[2.664194,-9.242765,-6.610822,2.746884,2.146618,7.328649,4.920980,8.269450,3.076595,-5.136478,2.195376,-2.673019,-0.664310,-9.429237,8.789734],[-6.067739,6.030685,-6.685293,-2.391711,-5.345127,5.415426,5.757182,-7.505304,-3.635873,-5.928043,-1.799022,-2.130433,-2.239497,-7.248684,-2.823774],[-8.107219,-9.537181,-8.216422,6.187680,-7.483107,-3.632761,-6.178339,-1.169497,0.939370,-3.965745,4.575882,0.815604,6.282647,-3.436430,-6.565436],[-5.019677,0.092038,-0.442315,4.161834,-3.434350,-4.371883,-0.496407,8.661802,1.072063,7.097877,-2.242100,4.872028,-9.697120,2.925073,-2.746594],[-6.322163,-5.634798,-7.891660,3.610441,0.902538,0.425272,-7.437524,-3.696271,0.183521,-8.765703,2.484059,8.502323,7.837490,1.737686,0.702440],[-2.567696,-8.402788,0.209832,-1.928143,0.194722,8.061041,8.209427,-1.953146,6.078257,7.892531,-8.329525,-7.193801,5.017031,-8.192846,0.555749],[2.682264,1.393753,-0.145694,-2.398493,2.530662,-4.182392,-6.095397,-5.009408,5.375664,-1.815557,-3.664523,3.562557,8.356750,-6.754332,-1.193065],[0.242816,1.197069,7.987995,4.814699,-5.787981,2.927647,5.894200,-8.598236,-3.404800,7.800771,6.143425,-5.463928,9.424062,4.535925,0.753847],[8.957934,2.724926,9.021672,-6.819952,-0.220887,2.993696,-6.237667,-8.433932,-2.974396,-9.573465,8.199714,9.058602,0.467182,2.895129,-9.324677],[-4.169278,3.915491,8.933194,-2.241164,-3.479474,-6.422498,2.156952,-8.847778,-4.495874,-6.403464,8.236666,-5.723810,6.913577,9.370272,-7.300337],[2.414763,7.085336,5.736164,9.643280,-7.033363,-4.360010,8.205483,9.465916,5.184288,5.154698,5.706812,-3.971788,6.949512,1.667841,-9.792730]],[[9.536955,-0.928135,7.777940,9.222878,9.484910,-2.741441,-8.572562,9.270264,2.269413,9.401384,5.676434,0.311280,-5.378356,9.962199,2.257675],[-9.623085,-0.753134,7.415011,-1.355416,-6.680100,9.742037,5.329010,1.816724,8.787437,-6.454262,9.477393,3.329350,9.070656,5.175733,2.687171],[-0.635762,8.204001,-5.825886,-1.488191,3.653174,5.707250,0.668854,6.539108,2.381267,-6.501913,2.339047,3.972736,-0.469039,7.678014,-8.294583],[2.816552,-5.011934,3.455623,6.586690,7.164712,-3.603682,4.513174,1.909592,-2.669423,-9.248725,-7.411763,-9.677127,-1.062957,-9.057267,4.745150],[5.885081,-5.907358,9.085974,-3.765483,0.760996,-3.050793,-9.888823,-2.119529,-5.788482,5.572499,5.510321,-0.291990,4.459813,-7.521589,-3.696408],[-3.090854,-6.078019,6.515087,-7.185195,6.229036,8.481040,-0.277435,7.906281,-1.858438,4.606796,-4.298107,0.886327,3.293709,-7.950587,3.618768],[9.271709,-2.837953,-8.717142,7.773982,1.519772,-1.942688,-5.147232,8.206812,5.883672,4.333018,8.942668,2.185164,9.348098,6.127195,7.825451],[-6.144061,3.712398,-1.656899,5.840919,-3.682242,-8.556305,4.327095,0.202359,2.421045,-5.010895,-3.768273,-4.877594,1.797018,-7.841550,5.017296],[5.720198,-2.558833,-2.128883,-5.383658,-6.745342,4.145360,1.173003,-9.185565,1.448694,-1.192907,-1.956178,3.274376,-3.413169,-3.501190,6.010268],[-6.699766,-7.581176,1.554222,-7.312411,-4.830285,8.376521,2.235364,-6.230697,2.428600,4.419616,-2.239207,-3.278349,4.379414,-1.430330,6.658062],[7.244860,-8.500915,-6.643497,0.724387,1.184480,-9.482281,9.897723,4.322881,5.728624,9.503612,-4.586709,-2.697232,0.720571,-4.980628,-6.987431],[8.224347,4.629350,8.807290,-7.185909,-6.708739,-1.222061,-9.322201,2.269584,2.004540,-4.829153,3.972756,-2.726154,-8.434153,6.996487,5.342165],[-3.521979,-0.272998,-1.926808,-7.196444,-9.982169,-7.450852,1.118655,-2.570978,9.611247,7.502345,-3.650697,-5.673994,-8.499298,-4.202288,0.722480],[5.167813,-6.068050,-0.963745,2.935847,8.147134,0.638828,-8.531764,-3.157242,4.497459,4.467277,-5.233018,-3.646616,-1.848784,8.226570,-5.998940]],[[9.733102,-4.372072,1.710887,-2.849102,8.004627,-2.932699,-1.827486,3.127993,5.723505,-0.667132,7.857292,-5.480772,2.116206,5.252438,5.884525],[-4.091964,5.551224,3.729442,2.037974,-6.174239,1.191810,0.756777,1.888422,3.652075,-9.046822,1.761167,-3.508632,3.391820,4.038278,-4.898411],[-0.380575,7.609068,7.359055,7.941083,-8.619817,-6.878752,-4.054399,1.736383,-1.885936,3.914147,-4.156073,6.353498,-0.293798,9.478248,0.674359],[5.584303,-4.374691,3.856066,6.044900,-6.599180,-8.945468,1.139015,-0.057943,4.798171,6.197334,2.711576,1.062454,-1.078101,5.295694,2.765482],[6.046540,0.032594,2.869370,-9.613896,6.333113,1.079996,5.649243,-0.163979,8.876364,-4.828488,-0.820631,6.402190,-4.787282,-0.670062,0.383292],[-6.451091,-4.576458,-1.356145,3.603143,-9.499147,5.420181,-5.323717,-6.501340,-8.592387,-7.051683,6.955262,8.032482,4.391525,-1.249783,1.806986],[0.660321,6.391223,6.463638,-9.718684,-8.691930,1.280682,-6.483248,-4.430001,3.149283,-3.239857,1.822589,-9.202268,-0.763402,1.237937,4.013965],[-2.202963,-4.969221,-2.146380,2.272065,-8.252836,1.112968,9.987193,-1.643163,7.589547,0.590859,2.241650,5.823427,6.300350,2.018711,-5.482160],[0.353739,-1.300808,-2.450634,-9.271868,2.701185,6.474020,-1.308903,-5.640080,-9.422789,-6.359220,3.084469,8.032272,-9.658062,1.752620,2.878857],[-6.209588,-0.715118,-6.401231,-7.579424,1.939988,-9.341071,-8.059151,2.680771,8.969651,-9.964546,1.399775,5.082532,-8.174514,9.480306,-9.359711],[-9.291287,-0.256430,9.311091,4.407404,8.945257,3.059351,-9.185184,-5.286377,-2.821345,7.286961,-5.283360,-0.719940,4.365893,9.491887,-5.870686],[4.158469,-2.694187,-9.591787,2.231906,8.363093,-9.240873,-6.275882,8.509529,-2.740206,-3.990621,-0.490188,3.487626,-1.827217,-1.260855,1.709704],[2.017139,3.012788,-8.706939,5.565523,6.163262,-4.460258,3.694573,-8.021296,-5.368274,-7.985375,4.648860,3.215646,-2.597704,5.241617,1.537770],[9.221707,-6.942292,-0.688864,-0.254205,-3.685037,9.799791,8.235634,0.490107,6.120316,9.466979,-2.943066,-9.942339,8.711628,5.159018,2.182642]],[[7.157625,-9.818958,3.001323,2.684716,-2.352941,-1.386221,-1.718224,1.522339,6.365482,8.699403,-7.298084,5.870892,9.177262,4.264342,-6.201582],[6.651460,-6.407948,6.750752,5.991434,4.654367,-3.606079,3.610379,-5.460865,-4.662936,0.477058,-1.237914,6.791505,-2.252193,-6.811055,2.006024],[2.853260,-5.154358,-5.339072,2.684214,-7.581563,-8.989844,-1.803221,-4.418382,-8.251957,2.783169,-9.197491,4.345730,7.464522,0.575124,-3.986642],[-2.790651,4.840008,9.244953,-6.107376,8.689285,6.979115,4.234057,7.873806,-1.472582,-7.891760,9.999201,4.397756,-9.690119,8.758760,-5.806199],[0.095718,1.912230,-5.093609,-6.158104,6.265525,4.517368,0.698463,3.117112,-2.039352,-2.227117,9.309224,-4.310458,6.626554,0.494210,-7.832273],[-8.603711,9.263011,-5.686004,-0.151805,-3.394141,1.567919,-0.977952,0.403610,1.897498,-8.738277,-1.945590,-1.446532,-8.078980,-2.302741,-5.455687],[-3.115295,-4.651196,-4.758507,5.672496,1.908009,-1.579587,9.960952,-2.553347,-4.906598,8.322297,7.735615,-1.100449,-6.186506,5.905845,4.671821],[0.600046,-8.824781,5.257036,-3.009544,1.218936,-5.096189,-8.450799,2.218776,-0.745803,9.344437,-8.262700,-6.866730,-0.427212,3.830180,5.856162],[0.853474,-2.871354,-7.836092,-0.877265,-2.122682,-1.028520,4.665824,1.296057,8.481632,1.888464,9.476433,-3.176728,-4.866187,-3.906887,-1.830941],[-3.270996,-0.341464,-3.163421,-9.732335,2.400220,-2.526787,-4.603117,9.174954,-4.112766,2.697701,0.584052,6.950251,-2.894307,-2.779627,-0.781323],[-8.071820,-0.480502,3.475112,2.961904,3.196774,8.102958,5.204401,4.162176,8.855954,2.827859,1.928817,5.723839,-8.726225,4.499773,-1.888822],[-2.593757,-9.010954,0.617183,5.612869,-4.110734,3.322557,-1.453634,4.822339,5.706410,-7.194415,0.498514,0.013230,-2.226732,6.419369,-8.868494],[5.881408,-9.427132,3.047320,-2.540008,2.844835,3.895121,-7.153883,5.284446,-1.328315,-9.557690,1.080452,-3.684836,-6.235211,7.549180,-2.190817],[1.645486,-0.378138,-1.635329,7.052124,-7.306038,5.237022,9.016061,6.310491,4.961085,-5.683781,-5.868737,1.688703,-9.232060,-6.570171,0.761284]],[[-6.301832,-3.610591,4.544014,-1.364302,6.639188,5.188658,0.828398,-8.518674,0.311516,-8.038753,6.457276,5.359563,8.452017,-2.469182,6.313476],[9.740129,-1.515031,-6.071059,-6.801299,-4.888434,6.967731,-6.535630,5.332224,-0.575035,-8.472138,-4.746227,6.752481,-1.433160,9.691527,-1.700588],[7.070057,-2.506058,-8.700421,9.058968,-6.645908,-0.816577,6.189743,-4.350787,-8.737811,6.865711,4.332338,-7.914544,7.510803,1.071182,-5.300254],[-0.515532,4.368029,5.419061,9.751680,-4.580870,4.695650,-4.295274,2.604120,3.999321,5.457451,-8.663112,-9.263862,9.405725,-8.179718,-3.777488],[1.494998,-3.591618,-7.694797,-9.856098,-7.663007,5.682370,8.706401,-4.410141,-7.597433,-5.425432,-3.429523,-7.640030,-4.551322,-0.956497,-1.478629],[1.089133,2.211164,4.326144,8.995552,-6.353245,-6.364474,9.027038,9.887276,5.869048,8.279499,9.597138,-8.732276,-7.677725,5.404378,5.598804],[-9.452051,9.659310,-8.261740,4.569497,-6.632927,2.489585,2.479108,8.827255,-9.677583,-3.505235,-8.037338,1.506568,9.309408,1.458393,4.930818],[-9.770565,6.515419,8.586513,-0.639744,-1.203264,-2.058867,-1.308774,-4.854183,-0.054096,-3.122879,8.150311,-7.003584,8.462685,-8.455287,8.872262],[-2.935831,6.439834,6.193343,9.472944,5.877718,1.046003,-6.023852,7.235089,9.495303,1.365481,-3.466212,-8.741495,-2.255301,-5.522631,5.282772],[-4.286380,-2.192542,6.386783,-8.700350,1.332684,-6.937129,-7.325383,-2.133529,-3.936819,3.054687,4.696364,-9.986017,2.144831,-0.459604,1.693858],[3.856071,2.725049,-2.110254,5.645939,4.917164,-9.003362,2.584450,-9.080902,8.708245,0.468281,8.693453,-3.470087,0.655678,-6.646949,-0.547087],[9.398197,2.373092,1.381288,4.768221,-4.867107,5.976317,9.207336,6.875296,8.539956,-9.644975,-3.745967,2.986947,0.556920,-6.207009,-1.265452],[3.517898,-5.845401,-6.948519,-4.420145,-4.241305,0.209996,-7.716245,8.646672,-6.247605,-2.267920,3.986407,-3.872111,1.278374,7.636348,0.494538],[-2.527937,5.955255,2.709057,-4.662498,-8.234474,5.116256,3.127379,-5.867497,7.456583,6.644214,2.622792,-1.211756,5.963251,2.431332,5.755122]],[[9.956460,1.520851,-4.476725,-4.150177,1.191603,-0.721955,-6.674509,-5.317031,-6.098642,-5.657744,4.158680,-3.448351,2.509266,1.356437,8.781909],[-3.534951,1.061133,8.210186,-6.186518,-7.784082,-8.462403,-3.906658,-4.750341,5.046798,4.301841,-8.268985,9.026013,-0.339822,5.370561,9.152440],[8.039329,2.663659,-7.729245,-1.951054,-3.826525,-1.729012,2.180238,-8.816184,4.860729,-0.094249,8.184085,9.844369,-4.223942,4.466391,5.642050],[-0.828585,-0.372060,8.743493,-1.345153,-3.540780,6.730474,-7.085518,9.254850,-4.803211,-4.385189,3.443405,-1.066185,9.908764,3.097555,-9.180332],[8.595139,5.813944,-0.801439,-0.623729,-7.167069,0.977531,6.647648,2.325118,-1.120962,9.229231,-0.870083,-7.945628,6.843616,9.084769,9.564329],[-0.052120,-1.383922,-4.190363,-0.821035,-1.082719,5.452593,-4.825490,7.425992,-8.007331,-5.997309,-9.464893,-7.680637,5.965997,-6.001332,-9.554988],[-1.415151,0.699070,-0.007724,5.641093,-1.099007,-2.893523,1.738185,1.515936,-6.409254,8.989401,7.741052,4.278429,-7.633896,-2.818666,-6.056956],[-4.926107,0.271014,4.897783,-1.959402,-2.966524,-4.121174,-6.006149,-7.455168,-4.407386,7.120424,2.144950,-6.143182,6.367563,9.491469,3.594361],[-7.858245,-3.123530,6.537284,-8.351790,-0.601448,5.194613,5.463448,-6.973920,3.445055,-0.537332,-9.780842,8.940625,-2.824102,-1.433458,-1.881808],[1.718699,4.322855,-9.627221,-5.815683,-2.074875,-3.070237,2.178325,-5.802854,3.315062,1.434153,-9.638389,9.656611,-3.484810,-4.917965,0.833134],[-3.503236,-6.342635,-5.352565,0.366869,4.072824,6.684682,9.407460,3.600247,-7.772977,5.071020,-9.057709,-3.890694,5.212007,9.610719,1.834237],[4.622853,-3.967726,1.735498,-2.942977,5.821097,3.309267,6.213563,0.146310,-7.007687,5.329034,3.608690,9.239830,3.597939,-3.982052,0.323217],[1.844058,-7.950661,-0.005230,-4.891205,-1.204078,-6.225071,-7.356828,-3.135254,-5.934479,-7.211914,-0.608348,2.650937,5.812313,-0.128011,8.888382],[8.441078,-7.561255,-0.031395,6.433436,-5.103042,-6.886172,4.084936,-4.352201,2.423771,-5.753666,1.682002,2.121617,3.462300,1.791091,0.560719]],[[0.542765,-0.338673,-7.729456,-7.772703,5.378464,3.989410,8.636915,0.388827,-9.916044,-5.003455,-9.943300,9.721398,-4.628820,-6.737829,-3.419026],[-2.468097,-1.911165,-7.365475,-5.067548,-3.747941,7.458123,8.912313,6.540963,-3.329932,4.802900,-0.019312,-1.208525,-0.765196,-4.492715,3.093943],[-5.483674,-4.486644,-9.780924,1.275111,1.076399,-9.327894,9.439018,8.870207,-1.905635,-5.608536,-2.445706,2.527535,-0.482776,9.811828,-5.537601],[3.040614,6.219940,7.290049,-8.761562,-2.734773,9.539076,-7.130130,-5.600303,0.797004,-4.013899,6.987788,-2.634481,5.643988,-9.033517,-8.272417],[7.400735,3.362410,3.229000,-6.162901,1.760247,-9.141332,-9.547245,7.941560,-4.098310,0.386092,-9.051150,-3.239433,-5.805079,1.761754,-8.459185],[5.163092,8.239194,-1.294874,-2.978361,5.645564,1.045056,-4.194399,-0.353424,3.449968,-8.068877,2.520211,7.383231,9.406683,-4.495053,-5.772561],[-8.680911,-1.358686,-3.642944,3.309054,-3.502213,-5.129053,-9.804994,7.786313,-5.009784,4.010947,1.538565,6.292612,-7.146796,-2.949325,8.071757],[-2.781440,2.063032,1.494199,7.347383,-6.728163,1.064315,-9.093146,0.673698,0.362988,-6.954207,-9.433321,1.851959,-4.290541,-9.749151,-8.733582],[7.316793,-1.403420,-0.155891,-1.028963,-2.254959,6.317605,6.318674,2.056458,9.204174,-1.394232,2.044740,7.333964,-1.134686,0.290931,0.331760],[-6.250891,-4.317367,5.663435,-2.271707,-6.667216,-0.767408,9.880219,4.292438,-9.588726,0.765765,-6.327752,5.224349,0.392591,7.033088,-9.359380],[6.261059,6.150477,5.398491,-8.369287,-8.715318,-6.829545,-8.031333,-6.033045,-3.790070,-0.633086,8.867679,6.171524,-5.525409,-3.727677,1.943229],[-0.181078,5.639626,-6.856532,-8.503987,5.690675,9.925448,6.182906,4.895065,-4.176918,-7.300684,3.436897,1.277155,-2.239988,2.145816,-1.786760],[-0.515004,9.236441,-3.618505,-0.984741,-8.611705,-5.259971,-1.232077,0.653121,8.436829,2.482295,-9.350633,-9.239871,1.873288,-6.014475,5.857398],[9.623931,3.693448,-3.865220,-6.135076,0.565267,-6.867992,5.034260,4.330059,-6.796730,-1.612084,2.005256,-2.894064,-2.815235,-0.417755,-2.568719]],[[1.152300,9.336068,2.838821,2.864517,8.245323,-6.357451,-1.148374,-7.667381,2.682622,-2.447765,-4.471189,-9.447783,7.379483,0.291474,4.809171],[-6.729664,3.259976,-3.432057,2.353442,0.823577,-5.603429,-3.179992,7.568724,-2.938868,2.756330,-1.275771,-5.403558,-4.087749,8.859067,-3.199384],[8.580649,-6.699250,-1.200767,5.774309,-0.393394,-0.997070,7.361124,0.380566,5.976581,9.863162,-8.621445,6.450462,-5.275111,0.897857,9.584706],[1.429657,-9.694819,3.485495,-4.461666,-5.218990,1.087202,4.788483,8.352967,3.131588,-1.113927,8.633537,-0.871786,-1.003294,-8.777419,6.302845],[2.870952,-5.812115,-5.107403,-2.569442,0.418288,0.659439,-4.672201,0.758700,5.006564,-1.821652,2.938430,-6.793577,-3.247934,-4.618269,-9.476456],[-9.241467,-3.467673,5.482638,0.456972,7.617049,-5.404675,0.208954,3.268155,-4.985923,-3.290410,1.272847,-2.354983,9.658348,-4.347328,2.090873],[7.208812,-1.342466,6.580931,-6.882033,1.928769,7.556049,-4.780681,-9.562684,1.748173,-2.065649,-6.633114,7.457060,-4.359180,7.709626,-0.183668],[7.974084,3.942588,-1.230679,-9.692304,8.811967,-2.587263,4.645847,0.871331,5.047394,7.537329,-2.023517,7.948359,-5.247182,8.451685,-5.604696],[8.253019,4.612086,5.035028,6.892070,1.794380,9.413219,2.081456,-8.463606,8.996750,9.203059,-8.432338,-2.952798,7.323916,4.166546,-5.067118],[-8.974573,7.085854,-0.200422,0.632711,-6.833979,-0.258621,7.461721,8.463411,4.279056,7.330875,0.751353,-0.961484,8.978105,-6.608005,-4.145094],[-6.021478,-8.653041,0.482348,-3.015229,-1.276448,2.767180,-5.730999,-6.874535,-8.135485,-3.763830,-4.104041,8.568578,6.317380,-3.624490,9.076303],[3.399608,-2.482273,-9.997658,-3.288881,-0.667573,3.241631,-1.251936,-3.147645,8.117399,-6.198648,-5.276125,3.904001,3.682712,-3.325804,9.330534],[8.381545,0.123037,-8.648418,7.491677,-3.916777,-5.018243,4.394291,-8.859561,3.974987,-0.378338,5.963173,7.111085,9.404899,-9.940233,-9.674650],[6.211971,-7.528777,6.003520,-7.125189,3.891587,0.896998,8.658023,-4.901468,-8.934503,1.583931,7.129627,-7.173699,-6.064283,-7.717853,4.859181]],[[-4.360590,-9.768735,-4.504616,0.315012,-4.336019,2.289725,-5.532140,-3.296083,-8.986198,8.975297,7.392273,7.900223,2.676634,0.589619,-9.789141],[-8.895262,-8.935823,3.039037,1.751396,0.180278,8.255909,8.357163,5.342583,6.690378,-4.262640,-3.764205,4.915488,7.514926,1.585649,-2.479889],[-0.452971,-2.232740,5.757441,8.545918,-8.705053,-2.805207,2.113659,-3.883949,1.490394,3.221434,-5.256939,-1.636542,0.540686,-3.377593,-2.707623],[-2.946459,2.679221,8.533207,-3.511285,1.709341,-1.458117,-3.370594,3.209441,-2.648785,-0.501612,1.131094,3.205713,4.874704,3.480058,0.686870],[-7.894549,-1.768174,-7.664038,2.602698,-0.056084,-7.750814,-2.069880,5.744849,5.809132,7.439951,1.800831,-1.066727,-4.700416,7.242359,4.268292],[2.198233,-9.748866,7.857840,-5.253799,7.222797,-8.146612,4.655094,-9.454888,-2.410947,-3.842537,-4.949758,-6.907519,1.965759,-6.411404,0.604162],[5.004793,8.349295,-7.941000,6.191701,7.884681,-3.065113,-6.931580,3.679895,-2.704456,-0.556454,5.690317,-9.624967,8.502492,-3.881103,-7.984549],[1.665260,-1.727370,9.389130,3.102740,8.674686,8.125201,-7.322409,9.594293,-9.627588,-0.321785,7.022182,9.663054,4.444044,2.662839,-4.162932],[3.517066,0.509945,8.127737,1.677876,1.552615,2.361537,-1.638600,-0.078494,2.620299,5.726075,0.801298,1.969544,-7.092568,0.308560,-5.555492],[3.310047,5.660310,-3.602199,5.697713,-4.398244,-6.307333,7.893513,8.539744,9.586256,-9.398169,-5.803680,6.536287,2.648837,4.250167,3.578289],[-3.720849,9.664364,7.712893,-7.789543,2.415354,-2.814997,5.745813,-0.352829,1.485681,0.008923,-7.700082,-5.043152,-2.233133,5.828438,-6.028185],[6.577072,1.009582,9.587618,-3.563248,8.970678,-3.171401,-1.668295,4.075148,-6.255273,-5.679285,6.464312,-2.568931,-4.563429,3.410181,-1.547993],[-4.683204,-5.314352,-2.970842,-0.805087,-6.027638,3.897149,8.039697,-3.222398,-2.151432,-2.102016,-1.000279,-2.155845,1.704941,6.236278,-5.914271],[-8.868988,-4.409759,0.036097,-5.409693,6.581899,8.886031,8.754673,-3.464183,-0.713499,0.279113,5.576490,-2.437357,-4.416970,-6.387768,-1.361116]],[[0.562522,0.867163,9.743830,-0.166131,2.346196,-2.077810,-0.166655,3.237317,6.253265,-8.951660,-2.170153,3.052165,3.117307,-5.189643,4.171843],[-4.761303,-0.024472,-6.100976,-7.585926,6.846838,9.845015,6.623582,-5.573765,-1.214591,-2.432545,-6.839301,1.458428,0.800216,9.049521,-8.678093],[-2.800386,7.358431,7.062681,-6.437177,-1.445748,4.680947,-0.318935,-9.317894,8.118754,-5.164888,9.880272,5.709839,-0.679332,5.257252,-2.007497],[2.928010,-6.420417,6.987669,-1.227896,-0.217091,-4.967833,-5.711593,-2.325881,0.315770,-0.244490,7.004593,-9.990232,-6.497674,2.650128,-2.481335],[2.976195,-8.195750,-8.708452,4.896948,0.131433,4.119024,9.030159,-4.842054,-8.629349,-0.630580,-3.414805,-8.860265,-3.041122,8.834948,-3.822427],[1.175624,4.209937,-7.767480,-8.952096,5.075579,3.364747,0.825092,-1.259157,-7.194047,1.162080,6.606828,-3.543557,-1.198348,-2.828395,-6.984814],[4.468683,7.970501,7.442258,-3.881511,8.073506,6.221742,-9.540295,-5.362642,7.107515,-5.546748,9.881563,-2.219421,6.562706,-9.151580,-3.828421],[5.215628,-9.900552,7.155877,-8.229053,8.966295,8.863379,-2.707297,6.441201,-1.803367,5.102340,5.424095,5.737999,-7.541767,-0.990491,-8.434243],[9.919066,-5.642501,-4.250288,2.463860,7.515175,6.655846,7.219923,3.662831,-4.461419,8.645447,-8.577070,-8.304177,-4.712665,-7.426095,1.213429],[-7.823391,-5.270165,-9.215147,-5.916802,5.855960,8.844822,-5.591570,-1.009160,3.352856,8.898321,-8.522154,-4.513699,3.366351,4.233454,7.700257],[3.014019,1.558185,0.192904,-0.847509,1.175854,0.257164,-1.092431,-3.477150,2.137427,1.756119,-1.431366,-5.325495,-8.488467,-8.986327,-1.943336],[-7.861323,3.385351,7.812293,-4.659463,-8.827307,-2.194189,-8.150294,2.221875,4.512540,-0.408114,7.887415,6.143255,5.898703,-9.589511,5.466475],[-8.895765,-6.633823,-6.759739,-5.098065,7.181737,-0.059529,-9.969360,1.844516,9.448248,3.188175,1.784274,1.645845,-2.567787,2.635670,-5.805564],[6.105308,-4.748932,-5.143449,-1.475055,6.895842,7.344923,2.965201,-6.951230,9.232361,3.209194,-3.176836,7.737283,6.516003,-7.145818,-5.973296]],[[-9.210948,9.259720,7.261569,4.820153,-0.471292,-5.223235,-2.240659,-6.540569,-0.797230,9.698754,-8.046985,-7.597224,5.094469,4.804549,-2.534815],[-0.071203,-3.622413,-2.547985,8.946169,1.166792,-8.659634,7.322466,6.205411,-2.369300,0.141972,7.675612,1.656256,0.173537,-7.275801,-3.804466],[6.770104,6.126457,8.451729,6.499302,6.566774,-0.018324,-8.159805,-2.483976,6.341922,1.232663,-9.148691,-4.962380,9.906765,-7.722690,6.554381],[-6.946276,2.158965,-9.818195,9.022508,0.752456,-9.941051,1.900759,2.969303,-0.378797,-0.559984,8.285649,-9.550803,-3.653335,-3.120065,4.283986],[4.968758,-7.537647,8.062773,7.347315,-0.409095,3.446073,2.559753,-6.898182,5.600361,1.763869,-0.460755,-9.989976,9.368352,-5.728824,-1.432139],[4.090829,-8.783742,-6.115192,-4.552844,-6.546873,1.932812,2.812021,-8.759762,0.127798,-3.497558,0.727892,-9.067262,6.791984,-5.977302,4.287626],[-5.595270,3.696199,-9.450834,-1.188160,2.468321,8.531142,5.231923,5.281572,-2.513705,9.691766,-5.677941,-5.814315,-1.103409,-8.984244,7.252366],[5.037487,-3.036572,-4.903722,9.770246,5.918771,-8.882657,8.909754,5.788930,3.680115,5.578436,-8.123683,-0.546236,-0.915158,-5.476504,3.117206],[-8.477394,8.505821,4.925570,3.361155,6.147371,-0.164832,-1.692399,5.087929,-1.153392,6.477870,6.511724,9.182389,-4.709713,-4.234878,-0.493008],[0.546096,9.275892,3.233631,-7.845245,8.518679,5.105767,5.932266,9.279746,8.070541,-4.164434,4.416867,-0.836926,9.553295,2.464158,-5.573991],[4.147914,-4.717992,-7.868498,-3.012999,6.141027,-4.528655,3.869735,-3.309203,-7.546237,-7.014512,-0.765663,-6.113207,5.136489,-1.734937,-9.466638],[-7.548909,-5.917707,-6.071050,6.437363,3.527972,-4.109063,5.535922,-0.568955,-1.797192,-3.676889,5.523988,-9.741197,4.498332,6.143532,-7.247296],[-3.036535,7.016917,-0.198349,-1.664345,-7.362253,-6.210088,3.351136,-3.191006,8.089091,5.078622,-4.609900,-5.094982,-8.240511,-4.235415,2.196402],[8.881455,0.072932,-3.779641,-2.745690,2.783255,9.580505,4.750869,-2.187884,-7.948012,-5.019078,9.406379,-5.091510,-2.535480,0.754313,-5.713697]]], dtype = "float64")#candidate|3944|(11, 14, 15)|const|float64
var_3945 = relay.var("var_3945", dtype = "float64", shape = (11, 14, 15))#candidate|3945|(11, 14, 15)|var|float64
bop_3946 = relay.power(const_3944.astype('float64'), relay.reshape(var_3945.astype('float64'), relay.shape_of(const_3944))) # shape=(11, 14, 15)
func_3523_call = mod.get_global_var('func_3523')
func_3525_call = mutated_mod.get_global_var('func_3525')
call_3950 = relay.TupleGetItem(func_3523_call(), 0)
call_3951 = relay.TupleGetItem(func_3525_call(), 0)
output = relay.Tuple([bop_3946,call_3950,])
output2 = relay.Tuple([bop_3946,call_3951,])
func_4020 = relay.Function([var_3945,], output)
mod['func_4020'] = func_4020
mod = relay.transform.InferType()(mod)
var_4021 = relay.var("var_4021", dtype = "float64", shape = (11, 14, 15))#candidate|4021|(11, 14, 15)|var|float64
output = func_4020(var_4021)
func_4022 = relay.Function([var_4021], output)
mutated_mod['func_4022'] = func_4022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2643_call = mod.get_global_var('func_2643')
func_2644_call = mutated_mod.get_global_var('func_2644')
call_4106 = relay.TupleGetItem(func_2643_call(), 0)
call_4107 = relay.TupleGetItem(func_2644_call(), 0)
uop_4112 = relay.asinh(call_4106.astype('float64')) # shape=(1, 5, 9)
uop_4114 = relay.asinh(call_4107.astype('float64')) # shape=(1, 5, 9)
output = relay.Tuple([uop_4112,])
output2 = relay.Tuple([uop_4114,])
func_4118 = relay.Function([], output)
mod['func_4118'] = func_4118
mod = relay.transform.InferType()(mod)
output = func_4118()
func_4119 = relay.Function([], output)
mutated_mod['func_4119'] = func_4119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_380_call = mod.get_global_var('func_380')
func_381_call = mutated_mod.get_global_var('func_381')
call_4139 = func_380_call()
call_4140 = func_380_call()
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
call_4146 = relay.TupleGetItem(func_592_call(), 1)
call_4147 = relay.TupleGetItem(func_594_call(), 1)
output = relay.Tuple([call_4139,call_4146,])
output2 = relay.Tuple([call_4140,call_4147,])
func_4160 = relay.Function([], output)
mod['func_4160'] = func_4160
mod = relay.transform.InferType()(mod)
mutated_mod['func_4160'] = func_4160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4160_call = mutated_mod.get_global_var('func_4160')
call_4161 = func_4160_call()
output = call_4161
func_4162 = relay.Function([], output)
mutated_mod['func_4162'] = func_4162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_4184 = func_314_call()
call_4185 = func_314_call()
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
var_4194 = relay.var("var_4194", dtype = "float64", shape = (405,))#candidate|4194|(405,)|var|float64
call_4193 = relay.TupleGetItem(func_1431_call(relay.reshape(var_4194.astype('float64'), [9, 5, 9])), 0)
call_4195 = relay.TupleGetItem(func_1433_call(relay.reshape(var_4194.astype('float64'), [9, 5, 9])), 0)
output = relay.Tuple([call_4184,call_4193,var_4194,])
output2 = relay.Tuple([call_4185,call_4195,var_4194,])
func_4198 = relay.Function([var_4194,], output)
mod['func_4198'] = func_4198
mod = relay.transform.InferType()(mod)
var_4199 = relay.var("var_4199", dtype = "float64", shape = (405,))#candidate|4199|(405,)|var|float64
output = func_4198(var_4199)
func_4200 = relay.Function([var_4199], output)
mutated_mod['func_4200'] = func_4200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_4204 = func_791_call()
call_4205 = func_791_call()
output = call_4204
output2 = call_4205
func_4215 = relay.Function([], output)
mod['func_4215'] = func_4215
mod = relay.transform.InferType()(mod)
mutated_mod['func_4215'] = func_4215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4215_call = mutated_mod.get_global_var('func_4215')
call_4216 = func_4215_call()
output = call_4216
func_4217 = relay.Function([], output)
mutated_mod['func_4217'] = func_4217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mod.get_global_var('func_935')
func_937_call = mutated_mod.get_global_var('func_937')
call_4227 = relay.TupleGetItem(func_935_call(), 0)
call_4228 = relay.TupleGetItem(func_937_call(), 0)
func_2982_call = mod.get_global_var('func_2982')
func_2984_call = mutated_mod.get_global_var('func_2984')
const_4238 = relay.const([[-0.705254,-7.035055,5.786936,-7.086502],[5.737656,8.272885,-7.675275,3.439454],[7.564762,-0.609799,-2.013450,2.526551],[-2.008198,-0.466429,9.251715,8.022243],[-2.873650,-2.186923,-4.442288,4.998882],[-9.409170,-8.268454,1.292450,8.465753],[2.719791,7.238807,-9.467058,-2.970709],[-4.605479,-6.257044,2.831928,0.238513],[5.615526,1.185193,-2.993987,4.673591],[-4.076743,0.224568,5.633654,-2.027893],[2.491880,-8.933428,-2.870099,-6.279627],[9.258387,6.007772,-6.404794,-4.388686],[-4.980556,-0.264255,-7.635471,5.074739],[5.553798,-6.575215,6.881051,-3.602910],[4.345328,-9.231249,9.011637,-3.683999],[7.482582,1.244822,-9.019717,-5.817033],[4.383621,4.926177,-6.080965,-8.384762],[-7.344960,5.883338,-5.084820,-5.942500],[-9.558854,9.647575,3.018995,4.510093],[4.136222,-0.537808,-5.329921,-7.158524],[7.578835,-8.119322,-4.350047,-0.821144],[7.467357,-3.411250,4.958187,1.126311],[-8.118112,5.172296,-1.210526,-6.364676],[2.940770,7.052794,8.813211,9.122822],[-5.704957,6.905097,8.266020,4.804973],[6.323468,-3.114196,-7.068549,-1.928282],[-1.038503,-7.492917,-0.284020,3.783949],[7.698602,-5.943592,-9.040516,-0.112103],[9.698779,-5.359766,9.489329,7.701713],[8.235497,0.234868,-1.522403,-3.675977],[6.358248,1.966110,-2.811486,2.940875],[-7.271522,-3.303142,6.072176,8.359838],[-7.570827,9.567311,1.288752,-2.966831],[-6.077115,-3.722851,-7.832515,-2.515560],[1.946402,5.718052,-4.349064,3.041045],[-7.688856,5.256796,-9.473294,-9.266255],[-6.196925,-5.034680,9.458596,9.408177],[-9.315725,-3.303585,-6.908781,-1.213851],[-1.469457,4.583023,-5.471697,5.531843],[2.322346,2.796782,6.204461,-6.654481],[0.523732,9.197771,-6.359422,9.403809],[-0.005540,8.342913,-0.808829,-4.094528],[0.581145,6.291320,3.336276,5.726551],[3.640804,-3.161039,-4.147705,0.037565],[-4.127560,-1.449258,5.921470,0.349787],[6.040309,-0.576690,6.864541,6.138699],[7.030658,-8.128923,3.729768,4.047961],[-3.032862,-4.447968,-2.300432,9.731105],[-4.431334,3.346841,5.748152,-6.686115],[0.202975,-3.858737,0.326816,-4.548244],[-1.374158,1.707980,-1.015897,-0.237303],[4.314384,5.016992,-7.933149,-9.723148],[8.643466,-7.699536,-6.323166,4.424286],[-0.546173,-6.527022,4.772038,-4.051075],[-1.361195,-9.494927,-4.039552,4.507753],[2.663013,1.687734,8.275619,-3.070473],[-5.130014,8.022141,9.048662,-4.287853],[-0.159433,-1.862912,3.771581,8.467912],[-9.470147,-5.169096,6.620687,-6.127806],[6.420927,-9.188852,7.685026,7.961026],[-6.951080,9.234340,3.585716,9.977016],[-3.387625,-0.014840,-8.559208,5.476884],[7.508689,5.529640,-3.895053,3.920258],[3.037130,-4.406212,-0.516485,-6.381504],[6.556431,5.288918,-2.424919,-5.975987],[-8.213537,-1.448648,6.789409,4.669715],[-3.473798,0.034041,0.203848,-5.172437],[-3.730851,7.251976,-4.439679,2.252172],[5.271577,-7.523150,9.507774,3.651732],[8.003094,-7.363864,2.895642,1.300600],[-5.739924,-5.288525,9.466779,3.817008],[-2.391417,3.561569,-1.124736,-5.061993],[1.481052,9.419049,7.460194,-9.546901],[7.595195,4.032412,-3.981489,-2.311564],[1.524856,-5.752691,6.634867,9.388401],[5.096186,-9.671166,2.149950,2.581591],[0.774997,-8.729912,6.122977,-1.686876],[1.670773,-0.578115,-3.507588,5.611750],[9.713480,3.689030,7.244759,-0.916487],[2.716716,-1.774238,1.399674,7.220708],[3.262003,-9.793999,-9.466629,5.531123],[-1.538709,0.554000,-0.886859,9.867008],[3.667756,-0.993304,1.864134,0.634508],[3.286350,2.034074,7.558553,7.207398],[-0.608573,-0.142593,-0.219970,3.129447],[8.914269,-1.650625,0.456912,8.526287],[-9.045589,4.214259,8.168432,-3.090992],[-6.204667,8.054240,-3.566796,-8.552932],[-1.181896,2.866330,-1.814436,-9.550815],[0.714414,2.247280,-7.246901,9.213777],[-5.018997,-1.411867,5.516099,-6.335940],[-4.931004,-6.028165,0.106965,-1.049246],[4.049028,-8.260852,-2.807887,8.266113],[3.803057,-4.261401,1.339547,-6.941138],[-1.868501,9.132968,2.470035,1.909847],[-6.948070,-8.928539,9.604091,1.137570],[-0.765751,-9.051780,-1.476425,3.920608],[0.679812,1.529145,3.729203,-2.134984],[-3.239708,-7.914972,-2.066042,-6.291569],[2.603601,-4.596837,3.351531,1.799495],[5.090203,-3.613678,4.214246,-5.704775],[4.869733,8.008164,2.541622,-8.122973],[-6.841623,-9.313159,-7.004865,7.877033],[0.069184,-7.613534,3.936076,9.043390],[-4.564311,3.402546,2.480556,-4.186421],[8.769019,1.629030,7.152545,2.721410],[-4.856087,-7.703935,-0.110224,-9.711609],[3.761507,-8.838916,-4.842150,-2.746514],[8.752970,-5.574225,6.151522,2.860916],[8.253563,3.416224,-4.367371,-7.871885],[-4.800891,5.750692,-3.084895,5.596708],[6.453921,-7.960739,8.312596,-5.392791],[-6.087691,3.080242,7.830626,2.652954],[3.901531,5.645383,0.057500,7.738263],[8.381509,-7.482513,-6.261399,9.438932],[2.027989,-8.045428,-9.235233,2.936633],[7.363724,-9.224393,2.813703,8.661983],[1.345345,-7.182650,-4.743647,-2.738782],[-1.388690,8.802247,-6.995770,-0.395548],[0.162916,-9.421597,9.847948,-4.848788],[-7.101435,9.610247,-3.276529,0.723434],[-1.118237,-0.125511,4.126116,-7.274505],[0.447451,-9.647858,-8.749692,6.491266],[3.524057,-0.201654,2.723881,-1.610256],[0.552972,7.988873,-0.349569,3.659014],[-5.198321,-6.761988,5.899570,-6.985055],[-8.693144,-8.205696,4.082209,-0.011030],[-2.664027,-6.101356,-9.277912,6.679034],[-6.132296,1.856133,9.643701,1.968041],[0.215489,5.878150,-8.618433,0.279660],[1.513837,-2.527844,-7.616820,1.540123],[3.716964,-1.779002,-6.142861,1.502419],[4.578166,-6.169022,-3.122752,-3.948546],[2.012135,-7.198105,5.427601,-6.731260],[5.660880,-6.902399,-6.986189,-0.860367],[8.223453,8.187125,1.908449,-5.170301],[8.521720,0.085575,8.210177,3.748512],[-1.128290,-0.194573,-5.293007,-9.591835],[1.019031,7.609204,-8.829664,7.276478],[-0.382325,-8.720333,-7.149935,-9.406961],[8.849051,3.408202,-5.217018,0.145174],[-6.969887,-9.295038,-6.925102,-7.999726],[4.414939,4.710351,-4.546369,1.312824],[4.986563,-7.388117,1.365725,-3.780897],[-3.289515,4.499416,-1.111038,5.643431],[-3.364702,3.813127,-3.564877,5.861288],[7.708534,-2.346708,5.705650,7.570840],[3.144112,-6.876142,-0.798729,3.970085],[-6.908464,4.809815,7.106705,6.322454],[5.803652,-1.356719,4.512238,0.391158],[6.157743,-4.100111,-3.799883,0.590923],[3.768921,-9.259627,-3.306226,-7.047076],[-3.937992,-2.575045,1.551483,1.265187],[-9.906285,-3.066815,6.350786,6.163544],[3.173892,-3.214225,3.473920,3.479298],[3.315948,-2.025025,3.800015,4.696802],[4.791847,3.514070,8.884844,9.142059],[9.510740,4.240327,6.910447,7.176776],[-0.816548,-0.300661,8.487196,-7.601403],[8.330950,9.540694,-4.117383,-2.683842],[-2.199577,-9.481770,1.494603,3.874411],[7.734572,2.449330,7.112790,-2.831197],[-4.764279,1.332361,-7.612964,4.269461],[8.925910,6.671887,9.469828,7.079533],[6.999759,9.580773,8.025530,8.857452],[-5.780722,9.104461,2.608110,6.239080],[3.467936,-9.356077,2.887765,0.392695],[-1.738591,-1.220709,1.853568,0.490684],[6.123779,9.951246,8.349407,9.309587],[0.642892,-0.815589,-9.486694,1.229580],[-4.855981,-6.783697,5.255446,-5.678884],[-5.072838,2.464313,-2.169506,-8.729337],[0.692063,-2.785110,6.737362,-9.063132],[3.230135,8.194145,3.647148,9.194955],[-7.215767,5.220156,5.122988,6.264079],[-2.956549,7.308433,5.916479,-4.903329],[4.654783,-4.156264,-2.491531,-8.456572],[5.616641,-6.969512,-9.288534,-0.594188],[9.554820,-9.583847,-4.442894,-7.848125],[-5.175675,6.784085,8.990087,-7.120617],[3.161439,4.283533,-7.170350,5.265617],[-2.812987,-6.384730,9.398914,7.915361],[-7.168248,6.882693,-9.239117,0.037538],[-6.081609,-4.230603,-4.065252,-7.729626],[6.167856,7.969216,8.642820,2.585024],[-0.179198,-5.060403,7.313159,-4.209022],[9.610533,-2.087290,0.403492,-2.560081],[-8.779988,-8.461622,-6.794388,-6.493667],[-4.618765,8.560801,-3.565097,7.128388],[-4.080321,-7.385440,-0.429611,1.279276],[8.745917,2.263251,7.274545,-2.912070],[-5.523704,-9.780137,2.758071,2.896234],[-7.690717,-1.310233,8.262297,-0.623535],[1.494711,1.398848,9.913562,-5.221158],[-0.952013,-3.889138,3.300220,-3.734372],[0.181088,-0.562534,9.186541,-7.708685],[-7.401022,1.438303,6.034812,2.422801],[-0.282090,-1.393404,0.940513,-6.573220],[-4.743874,6.183019,2.799570,1.028095],[-0.778695,-4.188306,4.101337,-4.877260],[1.424097,-8.937330,9.725152,1.819499],[-7.294352,0.823804,-9.863189,-0.782172],[-5.309956,6.773041,0.127259,-9.979795],[-9.088923,4.902164,-1.150914,-4.970409],[4.477141,-0.612582,-2.896353,9.557182],[1.396255,3.570674,-2.352189,-0.196454],[0.649742,8.119889,-5.879937,7.617650],[-7.304001,5.044587,-8.928380,-2.030595],[-5.321893,-3.625178,-0.132292,8.087750],[-5.804108,-6.755868,-2.545415,-7.989077],[-5.061652,-7.854018,3.307312,7.151052],[0.677724,-7.642329,-3.709777,2.545626],[5.041205,-1.121779,5.347120,7.202621],[-8.145226,5.579342,-8.282635,-3.560834],[9.823695,-8.688568,-1.615734,-7.051024],[-7.298797,8.114737,2.528154,1.505548],[-1.389105,-3.918892,9.490341,-7.829322],[7.940009,1.969260,4.071495,-1.765820],[-0.216066,6.219338,0.781893,-4.550430],[0.893493,-2.290141,3.263597,2.192104],[7.327605,9.614712,-5.870097,-3.387972],[3.673122,8.740078,-2.541769,4.955014],[-5.496441,0.971160,-2.320000,4.702618],[-0.223949,-9.463150,9.595063,8.407779],[-9.179883,-1.300115,-8.215372,-1.786550],[-7.023386,-6.006505,-3.629698,9.083741],[0.816607,-5.378964,8.419869,8.796078],[7.073551,0.179968,6.583724,-9.916927],[2.363307,-4.108070,1.125057,-8.878821],[1.998578,-5.393583,-1.638724,-4.981147],[4.644813,-6.677278,7.913736,-8.251635],[8.831557,4.602999,-8.366459,-7.564439],[-9.581111,-2.438464,-1.207301,4.724140],[7.131973,7.331067,-3.539001,0.767057],[-8.891578,-5.316544,2.197471,-1.999064],[-9.348271,-7.235641,1.451157,-4.257039],[4.637469,-3.204742,1.920778,8.765557],[8.260574,5.697318,1.883421,4.584311],[-7.547174,9.776706,-6.098506,-9.781824],[6.025481,-8.144850,-8.660828,3.403356],[1.109223,4.158283,4.441460,7.907962],[6.554011,-3.926003,-8.664579,-1.355144],[8.407982,-5.547930,6.241226,-3.992385],[7.106399,-5.525754,-8.011300,-1.117472],[7.717421,-0.204446,-5.560924,3.389873],[-5.615962,-8.037223,-9.254158,8.544142],[-8.155401,8.964133,2.618928,7.821835],[-8.367644,-9.456206,5.770137,-9.306634],[-8.503868,7.126264,1.457831,-8.879337],[6.548444,-4.067035,3.557530,3.610432],[5.124921,7.975078,9.618231,-9.020721],[-8.838161,-8.249973,3.256879,-2.473088],[9.672444,-3.321379,1.621116,6.584847],[-5.799367,-0.612859,6.189499,2.148011],[-4.938076,9.615695,3.387556,-5.925404],[-4.708531,8.159905,4.364402,7.705970],[-8.732979,9.680613,-4.572740,-8.351606],[-4.498855,-7.265929,-1.265257,8.420634],[5.646435,-7.432651,-4.342830,-7.457597],[7.118890,-2.911791,-6.701011,-8.959006],[2.684215,-2.397767,-0.339673,-2.766793],[4.433408,-4.701247,6.137841,-2.426237],[2.407669,8.260442,6.420731,-2.346907],[-9.167941,-2.128484,4.461666,5.059860],[-2.510066,-0.522265,-9.192859,-6.887148],[-1.655896,9.161753,-7.666199,-9.559517],[2.867829,1.645104,5.258487,0.410430],[-3.816869,-8.938744,-0.129336,-3.527884],[1.795317,3.863271,-3.800705,1.376111],[6.490895,-3.686782,1.094895,8.460922],[-6.925582,5.138771,-0.220284,2.523913],[-2.332452,-7.427205,5.106513,-9.175860],[-6.377770,-7.684741,4.167448,9.686816],[0.165664,-9.173488,-6.517674,0.844932],[-0.134133,-4.978041,9.972074,7.392795],[-4.884824,9.260962,-8.503125,-7.994636],[0.077088,9.087584,8.989536,1.637312],[-0.342164,4.236095,9.445426,-2.170344],[9.194996,1.232082,-9.275109,4.923485],[-9.252203,2.669067,-5.057116,6.481325],[-8.884577,-9.292860,3.638727,-7.932122],[1.095988,-8.285121,-9.896539,-6.939166],[-7.670070,4.262368,-9.319898,2.553055],[9.974383,3.513088,-8.370983,3.303963],[-6.044544,-3.514104,-8.391395,3.662371],[-1.710347,-9.610321,-4.389388,8.846094],[-6.353688,-1.030469,9.678463,-0.586424],[-4.563277,-0.204771,-1.814371,2.635538],[5.060609,7.809978,7.344913,4.525638],[-0.413506,-3.988231,-0.528747,7.740531],[-4.946551,9.372372,6.676409,-3.618771],[5.212899,9.587514,1.222823,-5.646576],[-9.624344,-9.207099,1.031059,-6.657666],[9.360377,-5.145962,-4.004491,1.788547],[2.238467,-5.208413,-7.745202,-5.387358],[4.348985,9.364990,4.051669,1.314876],[1.164617,2.543384,0.402634,3.803406],[-7.037397,-4.179591,9.612001,-0.311275],[-1.990259,-0.523908,5.921089,-4.937492],[-5.880099,8.814125,-4.971535,3.402988],[-9.609015,-1.285375,-4.343995,4.394096],[1.413692,6.722507,1.184957,-1.359752],[-8.940389,-4.142690,8.098601,-7.486352],[-4.623745,7.782764,-3.652160,4.025079],[2.039593,-9.054368,1.790846,1.423381],[8.680284,6.447605,-0.190353,-6.531503],[-0.042679,-9.037723,-5.119751,7.565893],[3.145963,4.869398,-8.628114,-4.953136],[-6.856031,0.606151,-6.114904,-1.406057],[-3.737954,-2.086416,9.403931,2.735458],[2.705060,-3.553469,7.640908,0.686521],[-4.942403,-5.129728,7.009961,0.478085],[-3.496479,7.857372,5.987754,-0.571583],[6.114248,-4.766599,-7.022212,8.202438],[7.654071,2.586484,7.489090,5.755317],[3.339479,-8.288309,2.789345,-7.444543],[8.886723,-6.096016,6.223081,-1.651767],[-1.583301,-5.764407,-2.940305,-3.552833],[8.316509,-6.422589,-3.956553,-7.857081],[-3.243834,-8.759820,-6.042767,6.256297],[-0.065268,-2.153837,-0.969867,8.679025],[4.048252,4.543067,5.297839,-7.847634],[6.082173,9.338611,-0.936842,5.637637],[5.684803,-4.698426,-7.811601,8.372998],[-1.278760,2.692772,-4.463077,7.647877],[-7.863633,8.925721,-1.968482,-7.503291],[8.553223,-3.181207,6.434229,-9.736232],[4.476167,4.296687,-4.319600,7.618412],[-1.885403,3.430907,2.170654,3.576501],[-9.192546,0.355797,-1.487747,-4.687270],[5.759536,6.145542,7.777616,6.765550],[5.825234,-1.754392,7.278476,-7.227155],[-3.782564,-2.766816,-8.022968,0.806037],[4.739318,1.384929,-9.619260,6.389304],[-0.093632,0.758437,-2.366619,8.022229],[8.298918,3.598920,8.148998,-5.011238],[3.482898,5.699329,-0.880060,-5.374466],[2.920334,6.338055,-0.905531,4.486056],[-3.915973,-8.532397,-1.573562,-0.426755],[8.073204,-1.841920,4.545559,3.029439],[-8.722018,-0.437374,8.703906,-4.422394],[-0.351032,5.377051,-6.558253,-6.690696],[0.569907,3.718870,-4.770351,9.157744],[7.363060,-5.450899,-9.895922,0.226141],[-2.446547,-0.030288,1.147277,-8.455461],[-0.012472,-4.885789,-6.540133,6.228789],[1.246661,2.490881,-2.497890,6.904663],[2.266254,-1.518197,6.667367,-9.467219],[0.001261,-5.199703,3.020578,3.655168],[-4.901797,-8.262904,-9.154654,-6.475877],[-1.709401,4.237794,-8.137418,-5.699927],[-5.049696,2.944734,-4.153372,7.807948],[-5.405482,-0.989119,-5.299448,-5.945072],[1.022160,5.995801,-1.192548,2.015548],[-7.628359,-6.532316,-4.042628,-3.560494],[1.406786,-6.596783,8.830243,-8.004064],[7.723872,5.601088,-9.281075,-2.990314],[-0.431800,6.964654,2.674231,2.834450],[3.602160,-5.243984,-4.818319,-0.857454],[3.889986,7.386887,-4.716150,-5.063630],[5.451993,5.504332,7.115208,1.777382],[3.228691,6.670275,-7.662906,-4.897918],[-6.384888,1.907670,9.358820,-0.912794],[-1.839383,9.576117,4.907465,4.242975],[5.182359,-6.118507,-2.590629,-3.296513],[-4.672961,8.537067,-5.590427,-2.182752],[-6.382531,0.112525,9.677060,-0.586524],[-2.139103,-3.026372,-1.095729,-4.503696],[-7.561731,-4.673164,-4.935557,0.171362],[-3.451531,9.373271,-5.797733,6.511744],[6.512124,8.884112,9.209779,4.453956],[4.115175,8.420977,1.617666,-2.727997],[2.163484,-2.811253,1.275000,-0.832011],[-9.028404,6.130848,-3.181600,-9.572322],[1.604309,-4.731759,7.750309,-4.242626],[-6.012138,-9.743676,1.794175,4.359499],[-5.372310,0.967357,7.396969,7.501212],[6.177739,0.738794,-3.567507,-5.437386],[9.096321,-2.668199,-5.758445,8.761894],[-4.242622,-2.606687,-9.411352,-7.067207],[6.312450,3.566003,-5.228371,5.003036],[6.107897,3.023139,-9.872967,7.466247],[-0.400264,-4.888948,7.017222,2.068220],[-6.016216,3.912289,-0.301912,9.131477],[6.322311,-1.416432,4.661385,-0.705413],[-8.781872,-4.301094,6.173192,-6.535451],[1.032493,-8.955493,0.545216,8.080967],[5.915529,-2.019988,-4.745538,2.594036],[-0.797287,2.186933,9.069221,-7.172434],[6.423453,-2.712578,0.900796,7.953147],[-8.842442,5.272934,5.585608,9.709983],[8.503290,-4.063251,6.643587,-0.268150],[-9.021499,5.791471,0.895239,0.433304],[7.622603,2.505603,8.842787,1.017994],[-3.083214,9.231601,1.661173,-6.496892],[-1.626876,3.556509,-2.769804,-2.527114],[8.865949,4.558820,4.284852,-8.438616],[-0.247267,6.280400,-2.004594,9.020390],[8.840602,-5.321126,0.850170,-4.489189],[-8.288439,1.639597,1.557247,0.426925],[-5.758005,3.367736,2.049299,-1.042330],[5.039073,2.180942,-9.100375,-0.841494],[3.947789,2.562773,8.776569,6.990160],[9.443984,-4.313995,-2.272408,4.491514],[-6.411421,-1.478345,-9.349350,-7.176876],[7.723938,5.589487,-8.269906,7.445191],[3.794950,6.520583,-8.360131,-6.128204],[5.370558,-0.841048,-6.729668,-3.258830],[-8.924852,-1.981437,7.873516,-7.562715],[8.164844,8.857654,2.470409,5.585166],[4.037671,1.847803,1.074508,8.762514],[3.652691,-5.515483,3.623698,-5.884723],[-0.883861,3.319716,6.219018,-3.133841],[7.107748,6.040855,-9.577223,2.549098],[4.068560,-2.669572,-8.801986,4.866534],[7.039082,2.587734,9.311091,5.017671],[7.395373,7.650093,-3.857658,9.788674],[2.068386,7.592283,2.066510,1.258820],[5.620174,-3.321655,0.092594,8.037767],[6.034451,-4.894655,1.070655,-5.311361],[-8.933044,3.890303,5.651086,-4.199505],[6.979920,7.097594,1.682745,7.381528],[-6.618241,-0.691180,-3.386003,-9.185301],[0.879421,-4.065034,-0.373159,0.691033],[-2.453283,-1.283739,2.146744,5.641801],[-3.638949,0.240827,8.838388,-7.204189],[-2.632124,-4.739707,8.759082,3.549731],[8.201889,1.154251,-0.288883,-1.206384],[8.717233,4.107218,4.494760,-4.180781],[7.438806,3.225858,-5.960899,-4.953808],[3.684101,0.004799,0.532151,1.598458],[-7.347970,9.584964,0.995497,-9.785226],[-2.499309,8.466769,-5.667241,3.713266],[6.445908,-2.412557,-7.536598,0.930777],[4.015770,-0.573356,0.707892,2.613046],[-1.201819,-4.422883,-9.030999,6.992630],[-9.157188,7.129162,-4.747401,-7.903564],[7.527255,2.088034,9.072469,8.351913],[-9.227956,-5.779666,5.308347,3.151008],[-2.522349,6.057437,-4.893005,3.527077],[1.223531,6.008676,9.903198,-8.135092],[5.985606,-3.576849,-2.504495,1.966626],[-9.540598,-8.616927,-2.114762,6.053114],[8.751584,6.556774,7.993043,7.611435],[4.322053,-2.043277,-2.433394,-3.525443],[6.158594,5.991672,-3.947627,-2.577655],[-8.920234,7.634892,-5.593189,4.706880],[6.883435,-3.298401,1.825493,-2.642395],[-4.684946,3.896057,0.635441,-2.390392],[-7.611059,-9.362274,4.947342,1.266000],[2.408390,-8.181802,-7.124177,6.268966],[-2.392226,-4.901700,4.516631,7.013486],[-4.610528,6.961908,-7.133344,-5.465545],[1.924598,2.434321,2.178018,-1.147049],[7.989399,-1.286443,-4.831133,-9.862400],[3.352800,-2.900175,2.511309,1.697158],[-6.994839,9.786796,-0.489608,0.064185],[-7.581781,-9.630193,-0.929886,-0.541569],[5.155485,5.467968,-9.667876,7.372702],[-2.660003,9.243481,4.362164,0.900478],[5.728065,-6.683628,-5.289918,3.210904],[-4.914328,-0.498021,-2.109843,9.544317],[-7.230629,0.706767,-4.231023,-4.547141],[-1.098186,-0.275990,-4.878316,4.793945],[-0.167907,-8.643672,1.817549,0.326791],[6.266376,-7.694481,-7.585207,-9.583493],[-9.670876,0.200197,-6.352803,-0.857337],[6.219905,-0.820334,-2.315173,5.400431],[1.481527,-9.633783,5.675067,-3.825902],[1.201514,-5.566126,-4.810433,-1.748963],[-0.362683,1.460588,-9.023348,4.702489],[-3.719326,9.350395,5.810285,4.329641],[-2.657931,-2.155686,6.080222,7.891912],[6.473753,-5.271201,-4.795217,4.896215],[6.151730,0.903602,-8.233475,8.361136],[-4.915728,8.238791,-1.082933,-1.329260],[-5.551628,-2.743033,3.624161,8.194572],[-8.387023,0.034838,-1.032808,4.617959],[1.650526,5.568407,-3.864131,4.365531],[-3.132150,-9.995557,7.542593,1.164124],[2.991183,-9.733720,0.104370,-4.865151],[8.985364,-9.545900,-4.248315,1.592439],[-0.988991,8.817013,-7.779131,6.537955],[9.857963,1.747720,-3.748954,7.072980],[-9.631349,4.692178,3.412851,2.757271],[0.432901,-4.317635,-0.999481,4.636765],[3.560835,1.167857,1.847138,-3.137155],[-0.352190,-5.172396,-9.844611,4.682133],[4.600483,8.270060,-3.402246,7.703859],[-5.386138,0.493511,-6.388038,-6.799738],[5.268753,2.148229,-7.174634,1.224274],[7.141497,-0.688591,0.465971,-6.660164],[-3.763589,2.385484,9.717690,-4.785242],[5.445655,-0.172435,-3.363353,5.950167],[-3.153484,3.597777,-0.130420,7.444182],[-0.979195,5.628813,4.981521,-0.917530],[2.133508,-4.136780,-7.099377,6.114879],[-7.624268,2.919025,-8.017603,-9.819249],[0.984037,6.643152,5.244691,5.560828],[-7.916603,8.779241,9.254050,2.764175],[-6.554631,4.526188,-8.485238,-1.668759],[-2.984574,-9.640119,-4.944156,1.028238],[-3.366032,9.180460,8.354281,5.306573],[6.037090,-9.055293,-0.582192,-2.465943],[2.185380,8.136345,-2.902385,2.485442],[-9.633513,6.433889,-4.485461,-0.127306],[8.751188,-3.188178,8.144278,6.763206],[0.359262,7.400488,0.960371,-5.214471],[9.088384,6.947586,9.312493,-9.721238],[-7.258702,-2.477207,-4.148884,9.308877],[-4.374850,-8.454073,1.177179,-1.785724],[9.814496,-7.583559,5.286968,-4.992913],[-6.099952,-1.213881,-4.156089,9.687356],[-3.469389,3.908520,7.469235,1.840692],[1.030734,6.088665,0.488064,1.863543],[5.625677,1.679546,-2.860618,7.494987],[9.350454,-7.386692,-2.708057,-6.260387],[0.480769,5.300733,-9.444090,-1.973056],[-6.672414,-1.875987,5.707157,4.484781],[5.564853,-2.466510,-6.636684,6.912263],[3.679751,1.452381,7.385118,8.922645],[7.341285,0.835377,5.872713,6.431558],[4.859546,0.683010,5.877254,8.276701],[9.073692,-7.880566,1.852065,-3.464510],[2.006700,-1.504070,7.244563,3.899307],[-3.572326,0.117174,-5.406372,-6.010802],[-7.877784,5.252515,-9.592832,6.463514],[-9.340864,3.464823,8.567474,-4.808107],[8.974200,1.710549,-0.545603,3.781407],[-0.941751,-1.111505,-5.234430,-5.771626],[-2.385593,-5.497436,9.759003,0.033155],[-8.180169,5.842596,-5.799718,-9.384487],[6.666733,-1.452554,9.473990,-0.995123],[-7.120895,-1.752721,9.351405,-2.111085],[-3.677028,-5.629620,-0.139498,1.530386],[-5.653623,-6.477558,4.163040,-2.700294],[-5.475883,-4.245407,1.231994,4.152370],[-7.463465,-0.495531,9.465594,6.891867],[2.100450,3.048871,7.815443,-9.893649],[3.300668,-3.903044,-6.853749,3.891300],[-0.052326,-8.355477,1.247717,0.230469],[3.268045,4.585312,-7.020373,1.561751],[0.136616,2.525955,3.372265,-0.494072],[-6.669580,8.332992,-4.093622,-5.806882],[1.045986,-5.345688,-5.897888,-9.271155],[7.214445,-1.091878,-0.193857,8.111267],[-5.221156,6.552613,9.254131,0.625302],[-6.345296,-9.511849,7.083120,2.265436],[4.758022,6.775159,-6.501722,3.351543],[-4.849635,9.322014,4.804095,-2.701828],[-7.045814,-8.541321,2.397683,1.961994],[-3.170776,-7.992625,-7.281895,-4.761813],[5.666127,-8.417051,1.869471,3.827249],[0.988878,0.497356,-9.929221,8.583341],[2.291947,-2.827758,3.377309,-5.050262],[9.666692,1.967363,3.881979,6.298205],[-5.048629,-4.785434,9.347690,2.045783],[-3.243181,-2.995352,-8.458692,5.261798],[1.126655,-5.565777,-4.240526,-1.784389],[-0.243528,7.954758,-2.487468,-5.151914],[-1.668249,-6.756039,6.957181,9.045880],[-7.235972,-6.945848,2.443118,-9.378835],[3.290267,3.747730,-1.310494,8.449669],[7.384614,-4.611497,6.345840,-2.635389],[8.206986,6.641664,-6.314113,-7.790459],[-3.210480,9.082216,9.960122,-6.326246],[8.598858,-3.760468,-4.505473,-8.382857],[-2.177934,5.305875,9.433016,-2.706453],[-0.899731,3.558338,-9.087906,-3.245085],[-5.274632,-1.625090,2.839048,-0.625587],[-3.321354,-4.780048,-0.984713,-9.897808],[3.602222,-5.089451,-8.841971,1.229326],[6.783663,4.834934,9.382701,-2.026068],[-4.453475,4.225119,-9.769008,-5.961696],[-1.290066,6.500095,5.543133,4.238409],[9.013364,7.508862,-1.533361,-0.152636],[-7.645784,2.756432,3.346042,9.800160],[-3.921226,-1.146438,5.678521,2.449123],[5.246784,-2.279902,4.371781,-9.141110],[-6.773693,-0.579917,-3.148920,-9.841728],[-3.753700,-7.738903,2.433554,7.160341],[-1.090169,-0.596337,-4.829410,1.465879],[-5.523842,-8.646081,-7.080080,-5.499591],[4.364991,4.606597,-2.109658,-2.104944],[-7.333663,-0.552896,-1.640933,2.010382],[1.047912,-2.231994,-5.011192,-7.869011],[-9.222203,-2.328972,3.641410,2.121641],[8.172252,-3.529950,-6.542950,-2.808471],[-3.437970,-3.315481,1.219512,7.636886],[-1.540045,-9.666101,-0.375660,3.227921],[-5.909429,5.296467,6.078516,-8.299603],[6.854905,-6.090548,4.831476,-5.657696],[5.659253,-6.858778,7.397088,-6.348913],[-6.194757,-9.428180,3.103531,6.436408],[3.540011,1.091703,4.392291,4.774124],[-0.268808,-2.422438,-1.902450,0.832521],[1.358801,-4.618125,-2.955618,-3.246599],[-7.763715,3.228534,2.801406,1.762308],[3.025810,2.161898,-8.855768,5.091554],[-3.049170,-9.245003,5.779309,-1.041480],[7.440363,2.807746,8.290307,-0.381272],[-5.986168,8.872977,-9.532548,-1.469957],[7.802399,-6.213243,-6.699312,3.266293],[0.458881,3.150407,3.638487,-5.384023],[1.719047,-9.594332,3.606578,-7.366812],[-1.063544,1.192886,-7.986846,-5.598769],[9.953031,9.281279,4.184070,-4.495030],[-3.050250,8.717539,-2.380360,-0.244679],[1.284985,-8.211319,-0.868501,-3.463275],[6.520623,1.342561,1.972592,0.550191],[2.217955,-0.680568,0.849808,2.592517],[-0.119777,-7.061051,-3.361522,-1.899175],[6.648898,9.068013,0.252478,3.094917],[1.350908,-1.432332,-0.444032,-2.397706],[-1.709714,-4.402959,6.930860,0.069090],[-8.304342,-4.397863,5.820671,-5.257525],[-8.832012,-9.476127,4.335513,-1.093274],[-6.331033,3.441370,-7.704636,-6.311936],[-5.828195,6.554855,8.469319,-3.838294],[-9.211862,-0.012556,8.070886,-8.898135],[-7.057633,-3.922250,-7.578345,7.267606],[9.747412,-3.701641,-6.856935,5.924002],[6.132794,-0.258206,6.821145,1.051397],[-8.045377,6.703631,-2.741947,3.308635],[-2.999279,1.829953,-8.987039,-8.935105],[7.336192,2.755230,3.838987,0.667966],[6.973423,4.992902,-8.788491,-1.831504],[3.992187,-1.515303,-1.953865,-9.103019],[4.481416,5.844206,-4.821009,-9.423686],[-6.323623,2.594116,-1.926079,0.153342],[6.138668,-4.753525,2.494964,-2.224863],[6.193887,-7.046665,-4.412233,-2.525685],[-2.083125,5.712212,7.456873,6.542033],[8.946024,-8.396200,4.701615,-3.424149],[-0.541194,-7.039007,1.733608,-2.938091],[9.568176,-0.180648,-4.849145,-5.633659],[8.692341,7.211911,7.220855,-6.008804],[-6.729348,-3.770165,-5.201656,-6.737582],[9.365703,-4.231682,6.148003,6.621643],[-5.938790,-7.976502,7.168814,0.019348],[-8.943550,4.700115,0.718908,-0.890808],[-7.935858,6.684244,1.290400,-2.600230],[-0.102498,-7.100242,6.863183,9.999032],[9.921401,-4.247030,-8.361972,3.139228],[3.922031,-4.261696,6.692246,-2.671963],[5.778710,-2.663115,6.020209,2.848213],[-2.007068,8.385268,-6.963929,5.510836],[-5.874243,-1.387399,6.478509,7.078524],[-5.207902,-9.475059,-3.440804,-0.630036],[-5.536859,8.313455,2.134283,-3.035059],[-3.224774,4.895165,-5.813390,-1.113814],[6.707826,1.618551,6.827836,2.715267],[-1.295331,4.286512,-6.789875,-0.682107],[-1.854064,-6.586262,-5.738486,0.376479],[-6.134150,0.590152,2.924639,3.900664],[-5.247576,-7.360759,5.869709,-0.453046],[2.827314,-5.797554,9.666438,-0.022668],[-9.511972,5.820203,1.522582,1.959672],[9.399581,-0.695628,9.155439,8.440250],[-6.749213,6.074300,0.450192,9.004332]], dtype = "float64")#candidate|4238|(660, 4)|const|float64
call_4237 = relay.TupleGetItem(func_2982_call(relay.reshape(const_4238.astype('float64'), [11, 16, 15])), 0)
call_4239 = relay.TupleGetItem(func_2984_call(relay.reshape(const_4238.astype('float64'), [11, 16, 15])), 0)
func_4215_call = mod.get_global_var('func_4215')
func_4217_call = mutated_mod.get_global_var('func_4217')
call_4261 = func_4215_call()
call_4262 = func_4215_call()
func_1307_call = mod.get_global_var('func_1307')
func_1308_call = mutated_mod.get_global_var('func_1308')
call_4263 = relay.TupleGetItem(func_1307_call(), 0)
call_4264 = relay.TupleGetItem(func_1308_call(), 0)
output = relay.Tuple([call_4227,call_4237,const_4238,call_4261,call_4263,])
output2 = relay.Tuple([call_4228,call_4239,const_4238,call_4262,call_4264,])
func_4270 = relay.Function([], output)
mod['func_4270'] = func_4270
mod = relay.transform.InferType()(mod)
mutated_mod['func_4270'] = func_4270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4270_call = mutated_mod.get_global_var('func_4270')
call_4271 = func_4270_call()
output = call_4271
func_4272 = relay.Function([], output)
mutated_mod['func_4272'] = func_4272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1567_call = mod.get_global_var('func_1567')
func_1568_call = mutated_mod.get_global_var('func_1568')
call_4337 = relay.TupleGetItem(func_1567_call(), 0)
call_4338 = relay.TupleGetItem(func_1568_call(), 0)
uop_4355 = relay.log(call_4337.astype('float32')) # shape=(1, 5, 9)
uop_4357 = relay.log(call_4338.astype('float32')) # shape=(1, 5, 9)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_4359 = func_1845_call()
call_4360 = func_1845_call()
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_4369 = func_480_call()
call_4370 = func_480_call()
func_454_call = mod.get_global_var('func_454')
func_456_call = mutated_mod.get_global_var('func_456')
call_4382 = relay.TupleGetItem(func_454_call(), 0)
call_4383 = relay.TupleGetItem(func_456_call(), 0)
func_4118_call = mod.get_global_var('func_4118')
func_4119_call = mutated_mod.get_global_var('func_4119')
call_4386 = relay.TupleGetItem(func_4118_call(), 0)
call_4387 = relay.TupleGetItem(func_4119_call(), 0)
bop_4390 = relay.less_equal(uop_4355.astype('bool'), relay.reshape(call_4369.astype('bool'), relay.shape_of(uop_4355))) # shape=(1, 5, 9)
bop_4393 = relay.less_equal(uop_4357.astype('bool'), relay.reshape(call_4370.astype('bool'), relay.shape_of(uop_4357))) # shape=(1, 5, 9)
output = relay.Tuple([call_4359,call_4382,call_4386,bop_4390,])
output2 = relay.Tuple([call_4360,call_4383,call_4387,bop_4393,])
func_4411 = relay.Function([], output)
mod['func_4411'] = func_4411
mod = relay.transform.InferType()(mod)
mutated_mod['func_4411'] = func_4411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4411_call = mutated_mod.get_global_var('func_4411')
call_4412 = func_4411_call()
output = call_4412
func_4413 = relay.Function([], output)
mutated_mod['func_4413'] = func_4413
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4457 = relay.var("var_4457", dtype = "float32", shape = (10, 2, 6))#candidate|4457|(10, 2, 6)|var|float32
var_4458 = relay.var("var_4458", dtype = "float32", shape = (10, 2, 6))#candidate|4458|(10, 2, 6)|var|float32
bop_4459 = relay.mod(var_4457.astype('float32'), relay.reshape(var_4458.astype('float32'), relay.shape_of(var_4457))) # shape=(10, 2, 6)
func_3942_call = mod.get_global_var('func_3942')
func_3943_call = mutated_mod.get_global_var('func_3943')
call_4467 = relay.TupleGetItem(func_3942_call(), 1)
call_4468 = relay.TupleGetItem(func_3943_call(), 1)
uop_4471 = relay.sinh(var_4458.astype('float64')) # shape=(10, 2, 6)
uop_4476 = relay.sigmoid(uop_4471.astype('float32')) # shape=(10, 2, 6)
bop_4482 = relay.subtract(uop_4476.astype('int16'), relay.reshape(uop_4471.astype('int16'), relay.shape_of(uop_4476))) # shape=(10, 2, 6)
output = relay.Tuple([bop_4459,call_4467,bop_4482,])
output2 = relay.Tuple([bop_4459,call_4468,bop_4482,])
func_4490 = relay.Function([var_4457,var_4458,], output)
mod['func_4490'] = func_4490
mod = relay.transform.InferType()(mod)
var_4491 = relay.var("var_4491", dtype = "float32", shape = (10, 2, 6))#candidate|4491|(10, 2, 6)|var|float32
var_4492 = relay.var("var_4492", dtype = "float32", shape = (10, 2, 6))#candidate|4492|(10, 2, 6)|var|float32
output = func_4490(var_4491,var_4492,)
func_4493 = relay.Function([var_4491,var_4492,], output)
mutated_mod['func_4493'] = func_4493
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4535 = relay.const(4.236214, dtype = "float64")#candidate|4535|()|const|float64
const_4536 = relay.const([[[-5.802275,9.677369,3.990662],[-8.801680,-8.038154,7.809104],[-8.285290,2.805849,0.089796],[7.520000,-9.413924,-1.728783],[2.960862,6.369089,6.759178],[-0.689549,-3.543496,9.291322],[1.186877,-2.004703,9.929469],[9.214559,-6.513306,8.081217],[3.597048,-1.149027,-7.958728],[8.045615,-0.158662,-1.127345],[-9.532571,2.995566,8.681574],[-1.056031,-0.576213,-8.859190],[3.941582,8.734431,5.986649],[5.759926,8.390161,-8.086447]],[[1.775934,-0.651200,-5.805972],[0.029466,8.077013,3.114417],[-9.382350,3.288225,-4.541597],[-0.391053,-9.935040,0.359837],[8.851661,-1.018606,5.407215],[-5.376578,9.827686,-6.116798],[-3.744742,-9.030154,-9.034665],[-8.130751,9.285273,-4.528185],[9.830044,5.450012,-5.078047],[6.816415,-1.367762,4.185048],[-3.405427,-4.831041,-5.066200],[-3.788739,-6.187976,-3.285646],[-7.916169,1.402133,-6.014068],[-7.450353,2.700710,6.206785]],[[-8.601720,1.885360,5.130920],[-8.006302,-4.441305,2.464284],[5.547066,6.020858,-9.156843],[6.436862,-5.605279,-1.115624],[-7.348971,9.503052,3.126246],[7.821533,3.203546,-2.382729],[5.429679,9.704100,1.530943],[-5.399581,-4.853054,-3.834648],[8.732045,3.371422,4.908747],[9.946495,-2.520918,9.982773],[9.005681,-0.619184,9.046778],[7.449823,1.821896,-1.836446],[5.042843,-0.445122,6.278340],[-3.440824,-1.298144,-4.591769]],[[-1.338783,7.598986,-6.107040],[-0.595460,1.207827,6.093459],[9.350723,-6.379465,7.827002],[8.888823,5.656026,-1.404861],[-4.050562,-1.344973,-6.749421],[-8.394634,-2.002302,-9.551067],[-1.591847,-8.687510,5.986550],[-9.869230,6.312101,1.250389],[-5.997562,8.380967,-7.842708],[-8.816017,5.665783,8.370542],[1.691774,-2.895914,7.315280],[3.955752,5.687765,-8.038908],[6.598071,5.210994,5.641484],[4.888465,3.343347,6.522337]],[[-2.034974,-2.578807,-9.557841],[6.889295,-5.472367,5.027255],[-9.626269,8.454680,9.189233],[-8.246715,7.818960,8.576189],[1.550345,-9.082870,5.723092],[-3.160674,6.377405,2.231993],[6.340707,8.143217,-3.532981],[9.251436,0.622636,-3.737413],[-9.633304,5.120302,-2.450731],[-7.175706,1.522220,-4.617717],[9.038379,-4.947007,-2.151283],[-7.919439,6.130538,8.319274],[7.121321,-7.163469,7.667960],[3.625350,-9.408344,3.243283]],[[1.421125,-9.488410,-0.609277],[1.492342,8.454613,-8.874328],[-6.702717,3.631967,3.563768],[5.395207,-5.027115,1.796140],[0.627223,3.517082,-4.735462],[-9.133148,0.217839,-3.809292],[-0.224960,2.519089,-0.008976],[2.043820,-7.054647,-8.176569],[1.386958,-0.766517,2.955535],[7.946600,-1.704194,-4.448741],[-6.303019,-5.672483,1.648951],[2.272623,2.760178,-1.013166],[2.945895,-6.390475,-0.461181],[6.970162,-8.538839,9.999529]],[[2.331936,-8.138719,-1.357285],[-1.188351,-2.723249,-3.008870],[-7.290956,0.745647,-8.464721],[8.183500,8.790874,4.080234],[-9.606705,9.850975,7.453317],[-5.994452,3.534404,-2.500371],[-8.736762,-6.910108,-8.620019],[-5.677447,0.934992,-2.104079],[5.868920,9.623926,0.867551],[6.771031,3.536661,-0.149772],[4.502734,4.823224,-7.205216],[-6.500211,0.831644,9.044857],[6.459152,-4.823539,1.172412],[-1.909145,-9.520067,0.384097]],[[2.854781,2.991456,4.687954],[7.143556,-1.864524,9.705941],[-5.097589,7.933965,3.699143],[5.750068,3.816898,1.819517],[-9.027942,1.707088,2.684311],[-6.562493,8.610078,3.921905],[-1.696248,-1.089978,2.219005],[6.633717,2.002128,2.830498],[3.049211,-9.528122,-4.285230],[1.935761,7.789440,7.847549],[6.411530,9.548316,0.268643],[3.512134,6.451731,8.195868],[6.403044,1.256096,3.633539],[6.093711,7.507140,7.439972]],[[9.239337,8.814031,-7.525457],[9.562551,-5.230552,-9.630953],[2.853352,9.796421,7.667177],[-5.739862,9.759305,-5.785465],[-2.845996,1.696384,8.608053],[-9.161064,8.564327,9.599166],[-3.447893,6.152949,-5.990442],[4.774635,8.329489,-6.561009],[9.614768,-2.293224,-6.960715],[6.991336,-4.473317,3.783583],[-0.849938,1.483029,3.274539],[5.922332,4.035018,-5.392939],[-5.815590,-7.264589,0.583972],[5.931864,3.936351,8.552922]],[[-1.155678,-5.887035,-0.679631],[-2.443668,0.663421,-7.418349],[-5.259009,1.230771,9.232181],[8.857919,1.367871,9.670476],[3.555339,8.083923,-5.310561],[-7.082447,5.399164,-9.281306],[-2.454920,-3.589431,-7.358481],[-3.096256,-3.123531,-7.878173],[-5.976057,-0.778331,6.098140],[-4.689562,-4.129349,0.605337],[-5.341671,1.490963,5.286696],[4.987349,-0.812815,6.121007],[9.307636,5.428030,7.135719],[5.592868,-8.323873,5.213049]],[[5.932510,-9.865216,1.631162],[2.810178,3.364589,-3.527089],[-7.891127,9.008509,9.113213],[8.296945,-3.905056,9.208137],[-5.701497,1.830108,-8.729483],[2.498269,-9.250592,6.041737],[3.656990,-9.560015,5.103574],[4.694513,-1.197261,-0.503404],[-6.766108,-5.406776,-4.078316],[-2.101391,-8.734765,8.222025],[9.754325,1.573021,-6.031396],[5.079264,6.577204,3.860698],[-3.283258,-7.592445,1.870544],[1.901063,-0.932960,-2.164291]],[[3.885955,6.799671,3.771234],[-6.525263,0.455894,-1.317550],[-0.501499,-1.850946,4.254737],[-4.289881,-4.165153,7.709651],[0.051956,5.932519,-8.474581],[-0.958631,3.343042,-1.741783],[0.367666,9.448469,-3.664123],[-3.972107,5.330351,-9.042094],[-8.624769,7.474918,0.176051],[-4.472127,9.090584,-3.398954],[-4.622601,5.250652,-7.304769],[-1.803383,-1.372112,1.760375],[2.023569,5.309363,-8.713621],[-8.410022,-8.221445,4.563861]],[[-3.025020,-8.277202,-0.617926],[8.634701,6.794165,-3.080748],[-5.901899,0.871281,-4.038687],[5.214801,2.820360,-2.325615],[-9.847983,-0.287699,-2.399393],[-8.575434,-2.408830,-6.065299],[6.228707,1.198106,-3.480007],[5.059442,-4.340413,9.352487],[1.937498,-2.247224,7.750128],[-2.397313,3.459367,-3.692192],[-3.852255,-3.834450,4.750821],[8.695935,8.808307,-4.341276],[-9.109489,-8.357617,-2.162513],[4.832815,0.004351,-2.270107]]], dtype = "float64")#candidate|4536|(13, 14, 3)|const|float64
bop_4537 = relay.power(const_4535.astype('float64'), const_4536.astype('float64')) # shape=(13, 14, 3)
output = bop_4537
output2 = bop_4537
func_4543 = relay.Function([], output)
mod['func_4543'] = func_4543
mod = relay.transform.InferType()(mod)
mutated_mod['func_4543'] = func_4543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4543_call = mutated_mod.get_global_var('func_4543')
call_4544 = func_4543_call()
output = call_4544
func_4545 = relay.Function([], output)
mutated_mod['func_4545'] = func_4545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_4548 = relay.TupleGetItem(func_2943_call(), 0)
call_4549 = relay.TupleGetItem(func_2944_call(), 0)
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_4550 = relay.TupleGetItem(func_1336_call(), 1)
call_4551 = relay.TupleGetItem(func_1338_call(), 1)
uop_4552 = relay.log10(call_4548.astype('float64')) # shape=(1, 5, 9)
uop_4554 = relay.log10(call_4549.astype('float64')) # shape=(1, 5, 9)
output = relay.Tuple([call_4550,uop_4552,])
output2 = relay.Tuple([call_4551,uop_4554,])
func_4557 = relay.Function([], output)
mod['func_4557'] = func_4557
mod = relay.transform.InferType()(mod)
output = func_4557()
func_4558 = relay.Function([], output)
mutated_mod['func_4558'] = func_4558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_4562 = relay.TupleGetItem(func_2943_call(), 1)
call_4563 = relay.TupleGetItem(func_2944_call(), 1)
func_2872_call = mod.get_global_var('func_2872')
func_2874_call = mutated_mod.get_global_var('func_2874')
call_4582 = func_2872_call()
call_4583 = func_2872_call()
bop_4595 = relay.not_equal(call_4562.astype('bool'), relay.reshape(call_4582.astype('bool'), relay.shape_of(call_4562))) # shape=(1, 5, 9)
bop_4598 = relay.not_equal(call_4563.astype('bool'), relay.reshape(call_4583.astype('bool'), relay.shape_of(call_4563))) # shape=(1, 5, 9)
func_2180_call = mod.get_global_var('func_2180')
func_2183_call = mutated_mod.get_global_var('func_2183')
const_4603 = relay.const([[True,True,False,True,False,True,False,True,False],[False,False,True,False,False,False,False,False,False],[False,True,False,False,True,False,True,False,True],[False,False,False,False,True,True,False,True,False],[True,True,True,False,True,True,True,False,True],[True,False,True,True,True,False,True,True,False],[False,False,False,True,True,False,False,True,True],[True,True,False,True,True,True,True,True,True],[False,False,True,False,True,True,True,False,False],[False,True,False,False,True,False,False,True,True],[False,True,False,True,False,False,False,False,True],[True,True,False,False,True,False,True,True,True],[True,True,True,True,True,False,True,True,False],[False,True,True,True,True,False,False,False,False],[False,False,False,True,False,True,True,False,True],[True,False,False,False,True,True,True,False,False],[True,False,True,True,False,False,False,True,True],[False,True,False,True,True,False,True,False,False],[True,True,True,False,False,True,False,False,False],[False,True,False,False,True,False,False,False,False],[False,True,False,False,True,True,False,False,True],[False,False,True,True,True,True,False,True,True],[True,True,False,True,True,True,True,False,False],[False,False,True,False,False,False,False,False,True],[False,False,False,True,True,False,False,False,True],[True,False,False,True,True,True,True,False,True],[False,True,True,True,True,True,False,False,True],[False,False,False,True,False,False,True,True,True],[True,False,True,False,True,True,False,False,False],[False,True,False,True,False,False,False,True,True],[True,True,True,False,True,False,False,False,False],[True,False,False,False,True,False,False,False,True],[True,False,False,False,False,True,False,True,True],[False,True,False,False,False,True,True,True,False],[True,True,True,False,False,True,False,True,False],[False,True,False,True,False,True,True,False,True],[True,True,True,False,True,False,True,True,True],[False,True,False,True,False,True,False,False,False],[True,False,True,True,False,False,False,False,False],[True,True,True,False,False,False,True,True,True],[False,False,True,True,False,False,True,True,False],[False,True,True,False,False,True,True,False,False],[True,False,False,False,True,True,True,True,False],[True,True,True,False,True,True,True,False,True],[True,True,True,False,True,False,True,False,True],[False,True,True,False,True,True,False,True,False],[False,False,True,False,True,False,True,True,True],[False,True,True,True,False,False,False,False,False],[True,True,False,False,False,True,True,False,False],[False,True,True,False,True,True,True,True,False],[False,False,False,True,False,True,True,True,True],[True,False,False,True,True,True,True,True,True],[True,False,False,True,False,True,True,False,False],[False,True,True,True,True,True,True,True,True],[False,False,False,True,True,False,True,True,True],[True,False,False,False,True,False,False,True,False],[True,False,False,True,False,False,False,True,True],[True,False,False,False,False,False,True,False,False],[True,True,True,True,False,True,True,True,True],[False,True,False,False,True,False,True,False,False],[True,True,False,False,False,False,True,True,True],[True,False,True,True,True,False,False,False,True],[False,False,False,True,False,True,True,False,False],[True,True,True,True,False,False,True,True,False],[False,False,True,True,True,True,False,True,True],[False,True,True,True,True,True,True,False,True],[True,True,False,True,False,True,False,False,False],[False,True,True,True,True,True,False,False,False],[False,False,True,True,True,True,False,False,False],[False,False,True,True,True,False,True,False,True],[True,True,True,True,True,False,False,False,False],[True,True,False,True,True,True,True,False,False],[False,False,False,False,False,False,True,False,True],[False,True,False,True,False,True,False,True,False],[False,True,True,False,False,False,True,False,True]], dtype = "bool")#candidate|4603|(75, 9)|const|bool
call_4602 = relay.TupleGetItem(func_2180_call(relay.reshape(const_4603.astype('bool'), [15, 5, 9]), relay.reshape(const_4603.astype('bool'), [15, 5, 9]), ), 0)
call_4604 = relay.TupleGetItem(func_2183_call(relay.reshape(const_4603.astype('bool'), [15, 5, 9]), relay.reshape(const_4603.astype('bool'), [15, 5, 9]), ), 0)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_4609 = func_791_call()
call_4610 = func_791_call()
func_3523_call = mod.get_global_var('func_3523')
func_3525_call = mutated_mod.get_global_var('func_3525')
call_4613 = relay.TupleGetItem(func_3523_call(), 0)
call_4614 = relay.TupleGetItem(func_3525_call(), 0)
output = relay.Tuple([bop_4595,call_4602,const_4603,call_4609,call_4613,])
output2 = relay.Tuple([bop_4598,call_4604,const_4603,call_4610,call_4614,])
func_4624 = relay.Function([], output)
mod['func_4624'] = func_4624
mod = relay.transform.InferType()(mod)
output = func_4624()
func_4625 = relay.Function([], output)
mutated_mod['func_4625'] = func_4625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1737_call = mod.get_global_var('func_1737')
func_1739_call = mutated_mod.get_global_var('func_1739')
call_4626 = relay.TupleGetItem(func_1737_call(), 1)
call_4627 = relay.TupleGetItem(func_1739_call(), 1)
output = relay.Tuple([call_4626,])
output2 = relay.Tuple([call_4627,])
func_4650 = relay.Function([], output)
mod['func_4650'] = func_4650
mod = relay.transform.InferType()(mod)
output = func_4650()
func_4651 = relay.Function([], output)
mutated_mod['func_4651'] = func_4651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3214_call = mod.get_global_var('func_3214')
func_3215_call = mutated_mod.get_global_var('func_3215')
call_4656 = func_3214_call()
call_4657 = func_3214_call()
output = relay.Tuple([call_4656,])
output2 = relay.Tuple([call_4657,])
func_4675 = relay.Function([], output)
mod['func_4675'] = func_4675
mod = relay.transform.InferType()(mod)
mutated_mod['func_4675'] = func_4675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4675_call = mutated_mod.get_global_var('func_4675')
call_4676 = func_4675_call()
output = call_4676
func_4677 = relay.Function([], output)
mutated_mod['func_4677'] = func_4677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3398_call = mod.get_global_var('func_3398')
func_3400_call = mutated_mod.get_global_var('func_3400')
call_4731 = relay.TupleGetItem(func_3398_call(), 0)
call_4732 = relay.TupleGetItem(func_3400_call(), 0)
output = relay.Tuple([call_4731,])
output2 = relay.Tuple([call_4732,])
func_4737 = relay.Function([], output)
mod['func_4737'] = func_4737
mod = relay.transform.InferType()(mod)
mutated_mod['func_4737'] = func_4737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4737_call = mutated_mod.get_global_var('func_4737')
call_4738 = func_4737_call()
output = call_4738
func_4739 = relay.Function([], output)
mutated_mod['func_4739'] = func_4739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3069_call = mod.get_global_var('func_3069')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_4740 = relay.TupleGetItem(func_3069_call(), 1)
call_4741 = relay.TupleGetItem(func_3070_call(), 1)
func_1594_call = mod.get_global_var('func_1594')
func_1597_call = mutated_mod.get_global_var('func_1597')
var_4743 = relay.var("var_4743", dtype = "float32", shape = (63,))#candidate|4743|(63,)|var|float32
call_4742 = relay.TupleGetItem(func_1594_call(relay.reshape(var_4743.astype('float32'), [7, 3, 3])), 0)
call_4744 = relay.TupleGetItem(func_1597_call(relay.reshape(var_4743.astype('float32'), [7, 3, 3])), 0)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_4745 = func_1845_call()
call_4746 = func_1845_call()
const_4768 = relay.const([[[9.607385,3.231272,-3.825245,-1.330455,2.440640,2.576267,3.680807,3.685276,-4.942943],[-1.897653,-1.120171,-1.366302,-4.975050,-5.035745,3.163924,-4.676678,-9.572797,-6.750963],[5.925396,-0.842267,9.023864,-6.959628,7.040388,-9.283500,-6.120517,6.636140,7.291917],[4.733447,8.162451,-6.315917,1.300018,5.366859,-2.652299,-5.738279,-5.577435,0.621469],[-9.375710,-6.866549,7.789827,-8.992675,3.625576,8.783928,0.799595,9.519303,-0.776188]],[[1.081713,-9.970609,-2.978430,-0.795047,3.567353,2.978958,-5.120903,-1.586974,5.446148],[9.810318,0.007992,8.490088,1.785255,1.726924,3.793184,-7.260000,0.280619,7.354962],[-7.032017,-6.510256,-9.991326,-8.981107,-9.601353,-1.274464,-6.646303,9.851360,-8.630113],[-1.326174,6.611048,-9.320382,-4.269746,7.800694,-6.623280,5.368093,-7.957886,-2.988795],[0.754451,9.872643,7.852533,-1.853098,-2.436899,0.983246,-9.416800,-2.076200,1.261090]],[[0.277647,-0.660599,9.186783,0.236123,5.566495,-4.146093,7.160574,-0.038561,0.180757],[-8.272987,5.623304,5.891320,3.824910,2.683366,4.232966,8.694112,-8.177498,0.442986],[-4.981874,-6.526441,-9.189678,1.826238,-5.367198,0.202959,6.419985,1.745486,-4.703972],[4.211879,9.674266,7.110162,3.769980,1.426909,-8.251116,3.395546,8.833450,-6.129772],[-9.688781,5.984916,2.333316,1.796704,-2.844073,-0.967723,1.382066,8.034264,-6.884566]],[[-7.306346,3.953303,5.493906,-5.996877,-7.339833,-6.390269,-3.113926,-8.000242,4.619707],[-4.757068,-8.509993,-0.643900,4.987533,-6.614697,-6.852241,5.544262,-9.361054,-2.510742],[0.386059,-0.587180,-0.201338,-7.874976,1.257485,3.608171,8.412437,8.077719,-3.573786],[-5.961887,-6.685641,-4.422048,3.091577,2.574444,-8.922742,9.759364,-3.684339,4.232121],[-0.481179,1.795738,-1.300741,-0.013384,-9.054052,1.364195,0.747536,-4.202769,-7.667070]],[[-5.276621,2.561265,3.291865,3.640038,7.514021,-1.054552,9.867434,-2.598097,6.864778],[1.046480,-6.217229,2.060495,-8.366920,1.363683,-5.816349,-0.342997,2.561741,-9.682262],[7.960276,5.427728,-3.441017,-1.456485,-8.172872,-0.004924,4.209208,-0.521431,-1.533094],[-3.745711,-6.174592,4.963030,5.683175,-0.109483,3.627058,-1.805651,-9.943028,0.899732],[5.460958,-0.840707,5.281492,3.916789,-6.122530,-0.615265,-8.790270,-4.988329,7.352651]],[[0.218961,8.534466,0.461974,6.429179,6.740491,-2.536285,-7.865019,-1.877541,2.854483],[4.622312,8.151676,-6.049608,-7.742434,-6.366858,-6.243822,4.276507,-6.731674,1.059584],[1.180891,6.887513,-6.058723,-8.954791,-0.713597,-9.581000,-6.633972,-0.570276,7.258136],[5.712364,4.350895,-8.105534,2.601053,-5.863494,-0.718324,-0.106413,-9.576853,5.829900],[9.931321,5.271533,-6.269721,7.519903,5.259908,-7.944688,0.651848,4.762027,1.803520]],[[-7.327136,2.303307,9.932762,-8.166719,0.685096,5.314172,4.130991,-1.786513,-7.892278],[-0.519958,2.139944,-2.405715,5.128265,-4.832217,-2.742814,-2.664528,-2.381378,0.954559],[-0.733671,6.315751,-1.005166,-5.424318,5.850609,-3.998375,6.162428,-6.940747,7.863672],[7.060283,-0.485746,2.111210,6.389253,2.079488,8.747574,9.030571,-7.548337,0.817368],[-4.605248,-1.088478,8.940157,6.882428,-2.440257,8.669093,-2.136068,-2.967379,-1.037435]],[[-9.973817,8.877780,-8.975660,-6.934366,-3.278544,-5.566590,-3.104125,5.068520,3.888643],[3.587821,-1.972450,-8.753908,6.951735,-1.934557,3.188998,0.120472,-1.353769,6.153255],[7.903264,8.951627,-8.118961,-7.561943,-1.767159,0.344467,-3.757832,-2.033625,-9.692613],[-5.712892,-6.045725,2.929861,-2.023737,9.355630,-4.531805,1.447203,-6.247230,0.961967],[-9.654388,0.730706,-3.125893,-4.750114,-0.014649,9.953145,8.254641,-9.970416,-8.256911]],[[8.033507,3.612069,9.972238,7.942485,8.463180,2.988564,-2.958205,-6.000063,-2.922195],[9.343087,9.582389,-6.850273,-4.514104,1.804520,0.471727,6.953331,-4.594063,0.575905],[-4.120829,-6.408649,-0.042812,-7.873895,4.361536,6.359771,1.946321,1.272283,-1.309084],[6.069661,9.745241,3.388548,-5.826789,-9.847510,6.992987,0.238645,-4.013148,-3.186431],[2.387887,-9.764956,5.846867,8.563804,-8.653844,-6.324666,-3.041795,8.938404,-3.041413]],[[-5.295621,6.779495,2.731662,-0.981692,-2.677566,-1.565126,9.935692,-7.978038,-9.678870],[5.569868,-6.297665,-5.304752,-0.026301,3.002650,9.704826,6.205617,-7.857842,-7.277960],[7.777721,-6.873827,6.920088,-6.873494,6.523769,-8.199357,6.015735,6.942654,0.980874],[-6.708431,-4.387411,-6.853493,9.222723,7.992793,-0.065097,7.785188,-6.296283,-0.793477],[-2.437963,-3.470299,3.755376,1.886545,9.201300,-6.287427,8.137670,-7.789501,-8.882883]],[[4.521655,-4.847008,-6.758991,-5.432146,3.537863,0.052967,-7.563285,-0.704388,5.430482],[-5.715801,-8.974373,8.396098,-8.725942,4.366328,-0.096424,0.906679,4.547178,-3.792116],[6.780666,2.069142,4.052162,-3.895094,-3.455932,2.240064,-7.106325,5.717201,6.375863],[8.709567,8.874712,-0.860932,9.132393,3.343062,-3.156322,-5.293830,-0.395758,-2.311219],[-6.665301,6.128323,5.062586,1.924906,-5.832364,5.261316,1.678749,-2.270086,5.423586]],[[9.792120,-5.175731,-7.316126,-8.637248,-2.094631,-9.206246,7.193596,2.364087,-1.201150],[2.503985,-6.931107,-3.838345,5.779892,2.514637,-5.726825,-9.016630,4.684475,-6.898502],[4.439710,-5.243129,4.568146,-9.927916,3.025452,5.258853,4.747534,1.824196,3.809789],[8.663983,-9.976677,-5.023648,2.635646,-3.881966,8.465357,-4.583827,2.938640,6.369463],[-7.225421,9.654528,8.723370,0.945007,1.612369,4.112596,-1.222700,1.229983,8.562340]],[[5.504458,8.827709,1.697906,-0.008186,8.174962,-8.226912,-5.548807,9.992402,-6.062462],[-2.569703,9.589214,4.186936,-3.633915,7.642100,-9.118648,0.376401,0.287620,1.385194],[-6.516382,5.390323,1.210546,-3.299767,-7.749815,-0.475696,-4.846786,-0.937112,-6.550476],[-5.972707,0.751833,1.673753,-4.041438,3.378667,2.840028,-9.084023,-6.422696,4.027423],[1.206853,9.881809,2.210058,8.631684,-9.890855,2.255821,3.963744,-7.036394,3.215775]],[[-5.733031,-2.779285,-8.461602,-5.691848,0.267918,-9.148267,-4.150000,-0.458013,9.753589],[0.905168,-6.533491,-7.982116,5.852247,9.992117,-2.825907,1.274107,4.010582,-7.502208],[2.558956,-9.880061,0.673946,1.214882,2.095435,1.225937,-3.584420,5.115071,-6.587530],[-3.383702,6.717420,9.640880,4.894726,-1.749960,3.649639,-8.938465,7.784236,1.018348],[9.277146,-1.879823,4.582776,5.237065,9.355478,-4.207044,-9.261152,5.079683,-3.721096]],[[3.786205,5.185044,-0.416308,-3.075915,9.788591,-7.240780,-1.816988,2.106541,-9.234241],[-5.746840,-7.577405,-9.876586,0.817294,-7.958751,-8.614386,-0.245970,-2.250599,6.476999],[-8.634304,2.918313,0.230454,-9.709778,4.797153,-7.933405,-0.722905,6.794332,-9.465028],[2.023746,-7.613640,-3.284717,6.419866,-1.973314,-3.851682,-5.824244,6.694962,-6.705830],[5.394878,-3.193820,6.447265,-1.105816,7.414884,-3.609102,8.170731,4.267141,4.818284]],[[-5.317190,-5.967511,-2.941728,-9.687231,1.926116,-7.891726,-8.923898,5.164149,-2.798622],[-9.979565,-5.740009,-4.723546,5.822143,5.526678,3.006874,8.069991,5.862591,-2.477626],[-9.737365,-4.421882,-6.115222,-9.068331,5.243524,3.353030,-7.119508,-1.432834,9.598277],[9.184765,8.880169,-5.269763,-2.128125,-9.449824,2.471952,8.942975,-1.403140,-2.114144],[6.201354,9.641473,-5.232724,-7.958191,-7.186012,9.938805,-7.498444,4.633321,3.382630]]], dtype = "float64")#candidate|4768|(16, 5, 9)|const|float64
bop_4769 = relay.bitwise_or(call_4745.astype('int64'), const_4768.astype('int64')) # shape=(16, 5, 9)
bop_4772 = relay.bitwise_or(call_4746.astype('int64'), const_4768.astype('int64')) # shape=(16, 5, 9)
output = relay.Tuple([call_4740,call_4742,var_4743,bop_4769,])
output2 = relay.Tuple([call_4741,call_4744,var_4743,bop_4772,])
func_4773 = relay.Function([var_4743,], output)
mod['func_4773'] = func_4773
mod = relay.transform.InferType()(mod)
mutated_mod['func_4773'] = func_4773
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4774 = relay.var("var_4774", dtype = "float32", shape = (63,))#candidate|4774|(63,)|var|float32
func_4773_call = mutated_mod.get_global_var('func_4773')
call_4775 = func_4773_call(var_4774)
output = call_4775
func_4776 = relay.Function([var_4774], output)
mutated_mod['func_4776'] = func_4776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_4783 = func_791_call()
call_4784 = func_791_call()
output = relay.Tuple([call_4783,])
output2 = relay.Tuple([call_4784,])
func_4785 = relay.Function([], output)
mod['func_4785'] = func_4785
mod = relay.transform.InferType()(mod)
mutated_mod['func_4785'] = func_4785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4785_call = mutated_mod.get_global_var('func_4785')
call_4786 = func_4785_call()
output = call_4786
func_4787 = relay.Function([], output)
mutated_mod['func_4787'] = func_4787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4557_call = mod.get_global_var('func_4557')
func_4558_call = mutated_mod.get_global_var('func_4558')
call_4813 = relay.TupleGetItem(func_4557_call(), 0)
call_4814 = relay.TupleGetItem(func_4558_call(), 0)
output = call_4813
output2 = call_4814
func_4823 = relay.Function([], output)
mod['func_4823'] = func_4823
mod = relay.transform.InferType()(mod)
output = func_4823()
func_4824 = relay.Function([], output)
mutated_mod['func_4824'] = func_4824
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4843 = relay.var("var_4843", dtype = "float32", shape = (12, 3, 14))#candidate|4843|(12, 3, 14)|var|float32
const_4844 = relay.const([[[-1.789989,3.606433,-9.065962,1.224205,6.028442,4.928126,5.974600,-8.367950,-6.466391,-5.959109,3.203757,-8.397339,3.734734,-4.452576],[-5.181218,-8.990055,-6.519715,4.772405,-7.391110,-4.499742,3.992969,4.988510,9.237365,-5.339278,-3.261767,-9.162674,3.061504,6.345383],[6.393883,-1.131510,6.566484,-6.992288,-8.617985,-9.014805,1.919147,-6.550307,-4.876881,8.075679,-4.443130,1.377767,-8.587115,-8.129536]],[[7.139180,-7.301808,4.130395,-1.181767,2.902737,-4.068991,-2.479173,0.027351,-1.499072,3.542513,3.450186,-0.112517,-0.493458,1.990821],[8.074285,-0.119418,1.697303,2.691354,-3.383669,6.847738,-7.689483,8.551658,6.781483,-3.512860,6.853025,-3.931925,0.769521,-5.123677],[5.277445,-3.281774,3.311291,2.232430,-1.746707,-3.193710,-1.092105,-9.467425,8.721463,3.290739,-1.813014,-7.359192,6.108440,4.405929]],[[0.873354,-7.802284,1.816497,3.922253,-9.636033,4.305907,3.205386,8.946246,5.217604,5.119349,0.362109,9.206791,-7.525604,2.105384],[5.686079,-0.962090,-6.152354,3.992004,-4.381297,3.910722,9.283430,4.960594,-1.849621,-4.827246,-6.062849,-0.768218,-7.777777,-3.545102],[-0.777616,8.447151,-0.740573,-3.876126,-7.361944,-2.673260,7.767991,2.238526,-4.266193,9.296631,5.424968,-3.336990,4.596907,-9.360153]],[[8.365836,0.653837,-4.381631,1.468317,-8.818298,-9.080958,9.005618,8.429402,-7.507044,7.977252,0.500273,1.855551,-4.378286,1.033269],[-8.217493,3.051535,-3.121647,5.192694,1.442751,2.421221,5.265195,4.548043,-9.565295,9.837665,9.097499,0.509890,3.131687,-3.747815],[-1.546106,-1.596995,0.560692,-0.571477,-3.361155,-9.967828,-2.058125,5.792731,3.530558,-9.136471,-3.256074,-1.932447,-4.480353,-6.613011]],[[-6.490219,2.944537,-1.996966,-6.104787,-3.164053,6.988903,-0.910707,-4.046046,1.914426,-6.667554,-5.478713,-8.644922,-2.226200,0.268004],[-8.386630,4.591195,-2.365263,-7.828412,-3.881015,-4.466938,2.273611,4.192310,4.388272,8.183617,4.697392,-8.716402,-8.532786,-1.211265],[5.425404,-4.846224,-5.137141,1.733753,-1.749481,7.327538,-0.793696,1.952664,-6.636365,3.926241,8.685965,-6.845520,2.872329,-0.523043]],[[-3.315867,-0.108540,-0.417518,5.770316,-4.353067,8.259223,-6.180279,8.163853,-3.199457,3.334743,7.882770,6.427849,4.910332,-7.257556],[-2.273499,-8.785003,2.313792,-6.692530,3.823985,-3.194778,-2.982052,4.091283,8.790016,0.799150,3.862842,-4.418677,-9.587383,8.076692],[4.444613,-5.932003,6.010635,-3.487348,5.438214,-5.664267,9.595675,4.700405,8.233186,-8.426835,3.933534,-2.794357,-3.546399,-9.038667]],[[-1.898936,-0.258530,4.722151,7.021393,-1.578410,3.414852,2.292543,-8.788567,4.337778,-4.170790,-1.632838,3.875079,4.946757,5.843543],[-0.269988,-4.136541,8.917419,-0.048662,6.659218,8.313755,-7.848929,0.503920,7.565850,-1.071128,5.619343,9.886804,5.983460,-1.744036],[-5.326327,4.495493,0.850004,-8.267897,-8.776354,5.236674,-1.145056,2.951215,1.668720,-3.830244,0.569761,4.083480,-4.241318,-0.278209]],[[8.463496,-9.885601,-7.576644,-4.410654,4.625427,0.501482,-8.048560,2.308371,1.341332,5.971847,6.447672,9.322478,-9.660964,-4.674348],[7.673604,-2.586135,0.979394,5.511820,-3.782635,1.717228,-5.568343,-6.692726,7.133613,3.808289,-9.098739,2.741135,8.717868,-9.289524],[-2.014145,-3.760844,-3.752256,-8.795926,7.831909,4.099912,-5.379432,8.416611,1.105390,2.804504,0.849700,-4.367972,5.467909,3.506458]],[[-1.604058,-8.088404,-6.185339,8.597958,9.890962,-7.547305,3.297948,5.153639,-0.969526,-9.031122,-8.974538,-0.478365,-6.330668,3.754500],[3.649543,-9.614992,0.452442,-8.146420,6.922934,-0.506260,9.954607,7.477366,-8.973902,-5.801609,7.710994,2.775718,-7.634515,6.743597],[-1.466411,-5.774435,-2.464476,8.315189,6.917832,2.632531,5.960632,-5.297878,8.335346,8.767479,-8.132934,-7.186713,-6.216534,0.089312]],[[-8.516508,-9.506817,7.476528,-3.034614,1.100513,0.213083,1.841450,-0.324647,-1.797208,9.104526,-5.775592,-9.179552,7.661401,4.528242],[-3.400278,-1.841164,7.417866,2.063409,-4.544602,-2.659409,9.611888,-1.891445,6.433577,-1.440082,5.262035,4.383711,-3.438901,-3.471283],[-1.034163,-9.540657,-2.258181,8.861991,2.541137,3.750977,-7.704040,2.804876,7.625213,-6.818011,-1.861459,2.296859,4.970448,-8.512801]],[[-3.195083,5.473049,-9.243483,6.954766,-0.792732,-7.769613,1.484809,4.292882,-3.422388,4.573901,1.048336,-7.706283,-5.902017,3.900070],[-7.388992,-9.269471,6.385164,4.259323,4.140956,-2.791399,-2.254270,5.713589,-0.030683,7.508300,6.284627,5.384961,6.109526,0.553373],[6.272383,7.643831,-2.869609,-9.510012,1.855796,1.195043,-6.327029,-7.283027,-5.140704,-3.243829,1.880633,5.441768,-6.862392,5.985713]],[[-7.531127,-2.535156,8.550651,5.307961,8.629880,3.016641,-4.495848,7.345920,3.314473,1.856874,1.212015,-6.468659,1.042019,1.717330],[-4.862297,1.952947,5.632066,-8.211162,2.802329,-7.503573,3.252929,9.517978,-1.263487,-7.246657,8.825758,-2.321016,4.916160,1.332519],[-5.629661,3.206969,1.178816,-8.860234,-0.577057,9.571284,-7.676695,-1.893175,-4.326038,7.931277,-4.970245,-4.886531,6.395040,-3.949650]]], dtype = "float32")#candidate|4844|(12, 3, 14)|const|float32
bop_4845 = relay.mod(var_4843.astype('float32'), relay.reshape(const_4844.astype('float32'), relay.shape_of(var_4843))) # shape=(12, 3, 14)
func_3214_call = mod.get_global_var('func_3214')
func_3215_call = mutated_mod.get_global_var('func_3215')
call_4848 = func_3214_call()
call_4849 = func_3214_call()
output = relay.Tuple([bop_4845,call_4848,])
output2 = relay.Tuple([bop_4845,call_4849,])
func_4850 = relay.Function([var_4843,], output)
mod['func_4850'] = func_4850
mod = relay.transform.InferType()(mod)
var_4851 = relay.var("var_4851", dtype = "float32", shape = (12, 3, 14))#candidate|4851|(12, 3, 14)|var|float32
output = func_4850(var_4851)
func_4852 = relay.Function([var_4851], output)
mutated_mod['func_4852'] = func_4852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mod.get_global_var('func_454')
func_456_call = mutated_mod.get_global_var('func_456')
call_4911 = relay.TupleGetItem(func_454_call(), 0)
call_4912 = relay.TupleGetItem(func_456_call(), 0)
output = call_4911
output2 = call_4912
func_4924 = relay.Function([], output)
mod['func_4924'] = func_4924
mod = relay.transform.InferType()(mod)
mutated_mod['func_4924'] = func_4924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4924_call = mutated_mod.get_global_var('func_4924')
call_4925 = func_4924_call()
output = call_4925
func_4926 = relay.Function([], output)
mutated_mod['func_4926'] = func_4926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3586_call = mod.get_global_var('func_3586')
func_3587_call = mutated_mod.get_global_var('func_3587')
call_5026 = func_3586_call()
call_5027 = func_3586_call()
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_5049 = func_480_call()
call_5050 = func_480_call()
output = relay.Tuple([call_5026,call_5049,])
output2 = relay.Tuple([call_5027,call_5050,])
func_5071 = relay.Function([], output)
mod['func_5071'] = func_5071
mod = relay.transform.InferType()(mod)
mutated_mod['func_5071'] = func_5071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5071_call = mutated_mod.get_global_var('func_5071')
call_5072 = func_5071_call()
output = call_5072
func_5073 = relay.Function([], output)
mutated_mod['func_5073'] = func_5073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_564_call = mod.get_global_var('func_564')
func_566_call = mutated_mod.get_global_var('func_566')
call_5084 = relay.TupleGetItem(func_564_call(), 0)
call_5085 = relay.TupleGetItem(func_566_call(), 0)
func_2943_call = mod.get_global_var('func_2943')
func_2944_call = mutated_mod.get_global_var('func_2944')
call_5101 = relay.TupleGetItem(func_2943_call(), 0)
call_5102 = relay.TupleGetItem(func_2944_call(), 0)
output = relay.Tuple([call_5084,call_5101,])
output2 = relay.Tuple([call_5085,call_5102,])
func_5110 = relay.Function([], output)
mod['func_5110'] = func_5110
mod = relay.transform.InferType()(mod)
output = func_5110()
func_5111 = relay.Function([], output)
mutated_mod['func_5111'] = func_5111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1737_call = mod.get_global_var('func_1737')
func_1739_call = mutated_mod.get_global_var('func_1739')
call_5130 = relay.TupleGetItem(func_1737_call(), 1)
call_5131 = relay.TupleGetItem(func_1739_call(), 1)
output = relay.Tuple([call_5130,])
output2 = relay.Tuple([call_5131,])
func_5135 = relay.Function([], output)
mod['func_5135'] = func_5135
mod = relay.transform.InferType()(mod)
mutated_mod['func_5135'] = func_5135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5135_call = mutated_mod.get_global_var('func_5135')
call_5136 = func_5135_call()
output = call_5136
func_5137 = relay.Function([], output)
mutated_mod['func_5137'] = func_5137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4118_call = mod.get_global_var('func_4118')
func_4119_call = mutated_mod.get_global_var('func_4119')
call_5138 = relay.TupleGetItem(func_4118_call(), 0)
call_5139 = relay.TupleGetItem(func_4119_call(), 0)
output = call_5138
output2 = call_5139
func_5144 = relay.Function([], output)
mod['func_5144'] = func_5144
mod = relay.transform.InferType()(mod)
mutated_mod['func_5144'] = func_5144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5144_call = mutated_mod.get_global_var('func_5144')
call_5145 = func_5144_call()
output = call_5145
func_5146 = relay.Function([], output)
mutated_mod['func_5146'] = func_5146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4160_call = mod.get_global_var('func_4160')
func_4162_call = mutated_mod.get_global_var('func_4162')
call_5177 = relay.TupleGetItem(func_4160_call(), 1)
call_5178 = relay.TupleGetItem(func_4162_call(), 1)
output = call_5177
output2 = call_5178
func_5195 = relay.Function([], output)
mod['func_5195'] = func_5195
mod = relay.transform.InferType()(mod)
mutated_mod['func_5195'] = func_5195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5195_call = mutated_mod.get_global_var('func_5195')
call_5196 = func_5195_call()
output = call_5196
func_5197 = relay.Function([], output)
mutated_mod['func_5197'] = func_5197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3883_call = mod.get_global_var('func_3883')
func_3884_call = mutated_mod.get_global_var('func_3884')
call_5216 = func_3883_call()
call_5217 = func_3883_call()
output = call_5216
output2 = call_5217
func_5231 = relay.Function([], output)
mod['func_5231'] = func_5231
mod = relay.transform.InferType()(mod)
output = func_5231()
func_5232 = relay.Function([], output)
mutated_mod['func_5232'] = func_5232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_5237 = func_480_call()
call_5238 = func_480_call()
output = relay.Tuple([call_5237,])
output2 = relay.Tuple([call_5238,])
func_5240 = relay.Function([], output)
mod['func_5240'] = func_5240
mod = relay.transform.InferType()(mod)
output = func_5240()
func_5241 = relay.Function([], output)
mutated_mod['func_5241'] = func_5241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1791_call = mod.get_global_var('func_1791')
func_1793_call = mutated_mod.get_global_var('func_1793')
call_5276 = relay.TupleGetItem(func_1791_call(), 2)
call_5277 = relay.TupleGetItem(func_1793_call(), 2)
output = call_5276
output2 = call_5277
func_5324 = relay.Function([], output)
mod['func_5324'] = func_5324
mod = relay.transform.InferType()(mod)
mutated_mod['func_5324'] = func_5324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5324_call = mutated_mod.get_global_var('func_5324')
call_5325 = func_5324_call()
output = call_5325
func_5326 = relay.Function([], output)
mutated_mod['func_5326'] = func_5326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5324_call = mod.get_global_var('func_5324')
func_5326_call = mutated_mod.get_global_var('func_5326')
call_5330 = func_5324_call()
call_5331 = func_5324_call()
output = call_5330
output2 = call_5331
func_5351 = relay.Function([], output)
mod['func_5351'] = func_5351
mod = relay.transform.InferType()(mod)
mutated_mod['func_5351'] = func_5351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5351_call = mutated_mod.get_global_var('func_5351')
call_5352 = func_5351_call()
output = call_5352
func_5353 = relay.Function([], output)
mutated_mod['func_5353'] = func_5353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3586_call = mod.get_global_var('func_3586')
func_3587_call = mutated_mod.get_global_var('func_3587')
call_5457 = func_3586_call()
call_5458 = func_3586_call()
output = relay.Tuple([call_5457,])
output2 = relay.Tuple([call_5458,])
func_5461 = relay.Function([], output)
mod['func_5461'] = func_5461
mod = relay.transform.InferType()(mod)
output = func_5461()
func_5462 = relay.Function([], output)
mutated_mod['func_5462'] = func_5462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5351_call = mod.get_global_var('func_5351')
func_5353_call = mutated_mod.get_global_var('func_5353')
call_5578 = func_5351_call()
call_5579 = func_5351_call()
output = call_5578
output2 = call_5579
func_5583 = relay.Function([], output)
mod['func_5583'] = func_5583
mod = relay.transform.InferType()(mod)
output = func_5583()
func_5584 = relay.Function([], output)
mutated_mod['func_5584'] = func_5584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_935_call = mod.get_global_var('func_935')
func_937_call = mutated_mod.get_global_var('func_937')
call_5588 = relay.TupleGetItem(func_935_call(), 0)
call_5589 = relay.TupleGetItem(func_937_call(), 0)
output = relay.Tuple([call_5588,])
output2 = relay.Tuple([call_5589,])
func_5597 = relay.Function([], output)
mod['func_5597'] = func_5597
mod = relay.transform.InferType()(mod)
mutated_mod['func_5597'] = func_5597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5597_call = mutated_mod.get_global_var('func_5597')
call_5598 = func_5597_call()
output = call_5598
func_5599 = relay.Function([], output)
mutated_mod['func_5599'] = func_5599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3155_call = mod.get_global_var('func_3155')
func_3156_call = mutated_mod.get_global_var('func_3156')
call_5718 = func_3155_call()
call_5719 = func_3155_call()
uop_5723 = relay.sinh(call_5718.astype('float64')) # shape=(1, 5, 9)
uop_5725 = relay.sinh(call_5719.astype('float64')) # shape=(1, 5, 9)
output = relay.Tuple([uop_5723,])
output2 = relay.Tuple([uop_5725,])
func_5726 = relay.Function([], output)
mod['func_5726'] = func_5726
mod = relay.transform.InferType()(mod)
mutated_mod['func_5726'] = func_5726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5726_call = mutated_mod.get_global_var('func_5726')
call_5727 = func_5726_call()
output = call_5727
func_5728 = relay.Function([], output)
mutated_mod['func_5728'] = func_5728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4118_call = mod.get_global_var('func_4118')
func_4119_call = mutated_mod.get_global_var('func_4119')
call_5734 = relay.TupleGetItem(func_4118_call(), 0)
call_5735 = relay.TupleGetItem(func_4119_call(), 0)
output = call_5734
output2 = call_5735
func_5744 = relay.Function([], output)
mod['func_5744'] = func_5744
mod = relay.transform.InferType()(mod)
mutated_mod['func_5744'] = func_5744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5744_call = mutated_mod.get_global_var('func_5744')
call_5745 = func_5744_call()
output = call_5745
func_5746 = relay.Function([], output)
mutated_mod['func_5746'] = func_5746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5144_call = mod.get_global_var('func_5144')
func_5146_call = mutated_mod.get_global_var('func_5146')
call_5773 = func_5144_call()
call_5774 = func_5144_call()
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_5777 = func_1845_call()
call_5778 = func_1845_call()
func_3523_call = mod.get_global_var('func_3523')
func_3525_call = mutated_mod.get_global_var('func_3525')
call_5786 = relay.TupleGetItem(func_3523_call(), 0)
call_5787 = relay.TupleGetItem(func_3525_call(), 0)
func_5231_call = mod.get_global_var('func_5231')
func_5232_call = mutated_mod.get_global_var('func_5232')
call_5808 = func_5231_call()
call_5809 = func_5231_call()
output = relay.Tuple([call_5773,call_5777,call_5786,call_5808,])
output2 = relay.Tuple([call_5774,call_5778,call_5787,call_5809,])
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
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_5825 = relay.TupleGetItem(func_1336_call(), 0)
call_5826 = relay.TupleGetItem(func_1338_call(), 0)
var_5848 = relay.var("var_5848", dtype = "uint64", shape = (14, 5, 9))#candidate|5848|(14, 5, 9)|var|uint64
bop_5849 = relay.equal(call_5825.astype('bool'), var_5848.astype('bool')) # shape=(14, 5, 9)
bop_5852 = relay.equal(call_5826.astype('bool'), var_5848.astype('bool')) # shape=(14, 5, 9)
output = bop_5849
output2 = bop_5852
func_5853 = relay.Function([var_5848,], output)
mod['func_5853'] = func_5853
mod = relay.transform.InferType()(mod)
mutated_mod['func_5853'] = func_5853
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5854 = relay.var("var_5854", dtype = "uint64", shape = (14, 5, 9))#candidate|5854|(14, 5, 9)|var|uint64
func_5853_call = mutated_mod.get_global_var('func_5853')
call_5855 = func_5853_call(var_5854)
output = call_5855
func_5856 = relay.Function([var_5854], output)
mutated_mod['func_5856'] = func_5856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5597_call = mod.get_global_var('func_5597')
func_5599_call = mutated_mod.get_global_var('func_5599')
call_5909 = relay.TupleGetItem(func_5597_call(), 0)
call_5910 = relay.TupleGetItem(func_5599_call(), 0)
func_1515_call = mod.get_global_var('func_1515')
func_1517_call = mutated_mod.get_global_var('func_1517')
const_5912 = relay.const([7.514388,-8.834919,9.557112,-2.703925,0.680123,-5.824897,7.689670,5.033418,-7.010380,9.749285,-6.044594,9.236146,-0.203486,4.141359,-7.292842,-1.077034,9.597892,-8.166222,-4.647334,4.780125,-9.260425,3.287307,-1.141135,4.065332,4.471990,-9.310289,-5.436090,3.591076,8.096161,-6.922846,7.129373,-4.960189,2.189677,1.700322,5.673364,7.945107,1.732075,1.199908,1.868744,-5.494149,6.193338,2.597576,-5.954180,-1.267729,0.235415,7.817300,-1.487381,0.991104,-0.492154,7.035127,-6.456892,5.684897,-1.966806,6.120982,0.663193,-0.344905,1.262440,-2.113697,-6.719502,6.869368,9.014715,-3.454105,-3.423712,0.571320,-9.914161,-6.426495,-8.893294,-1.961949,-5.815304,-1.335599,5.221999,4.824933,-2.539438,-8.977747,-3.286558,7.544645,3.417688,5.481072,5.657576,-1.492761,-0.479680,-2.920657,9.356442,2.962911,1.692109,9.210449,-1.975248,9.905520,8.424168,2.046338,5.690874,6.469643,-2.242381,0.073682,-0.920124,4.996231,-8.788168,0.408824,3.029767,-3.885836,-1.828156,2.332440,-5.232259,-0.360805,3.242783,3.969536,-0.358105,3.526919,-8.018940,-5.025063,-9.722994,8.374677,-7.431547,-8.835648,4.727959,-8.447474,5.021466,-2.012096,-6.490663,8.911074,-9.298136,-3.715008,3.123308,1.164460,-4.090696,-3.756850,9.975129,-8.660518,-3.169904,0.673742,8.796170,-3.794228,-7.674917,-0.610736,2.573690,-0.404582,-6.532973,-3.201867,-8.827709,4.779320,9.115351,7.299993,7.217864,-4.647059,7.124229,5.456071,3.178169,6.538051,-2.258587,-7.947469,5.346600,6.807780,-7.300107,5.126629,8.757753,5.554365,7.681592,-9.622431,-3.425822,-1.292962,-2.400984,-4.179018,3.581403,1.752239,8.887777,7.979281,-9.822557,1.124128,-6.790474,9.144652,6.408660,9.335821,-7.163675,-2.435000,-7.679503,-9.666708,-0.956098,4.506355,-6.446507,-2.578541,-2.848717,-5.451677,-5.756645,5.332402,-4.583056,9.714046,-6.832636,-2.184412,-9.747086,0.452686,-1.982477,8.290284,0.608779,-6.707924,-8.573195,0.144837,4.595079,1.991021,4.826006,-6.926294,-2.496924,-9.118269,-9.250711,4.278437,9.895078,-5.729056,-4.880407,-1.511944,-1.971629,6.331948,8.514158,3.262740,-5.709098,8.029740,-3.428785,3.016497,1.081521,9.257708,9.264561,-8.878008,5.306614,-4.864039,-8.895422,4.431545,0.413749,5.529499,-0.684588,5.934923,-9.470006,-3.205082,2.053396,7.423673,9.676113,-3.145332,4.978076,7.603773,4.492633,-7.992055,0.428260,-4.706567,-7.819396,0.777669,3.603524,3.643173,4.825673,-8.940308,0.990988,9.982910,-2.580553,3.105851,-8.675397,-7.247028,-1.243058,-4.606933,2.933959,4.602869,-6.594080,-0.798870,2.970118,8.397805,7.574385,5.468810,0.405988,-8.237028,5.992199,0.014693,-3.816604,5.187999,-0.710457,-4.061045,4.426071,1.857465,5.093357,2.289184,9.955743,6.800941,-7.694681,-5.649542,-4.993519,2.824792,-9.888818,7.558234,-5.173906,-0.465331,-7.645249,-9.304948,-0.761474,-8.733228,5.937958,-2.365332,-7.025449,-3.744761,4.355808,9.356273,9.226596,8.906487,9.778849,-2.097980,8.629123,3.855946,-5.804693,8.796108,8.361222,-3.881327,6.700071,-4.954995,-2.123363,-7.365138,2.500969,9.387282,-1.946846,-9.248953,-5.329976,-3.410341,2.000242,8.318594,9.725042,-3.632028,-2.702708,-4.049757,-0.102481,-9.780711,9.937856,-9.218299,-7.643891,3.426923,-1.406384,-9.204148,-9.305665,-0.473571,-4.495482,4.813882,4.825140,2.817850,-6.972041,2.149118,-7.441400,-2.991966,8.763761,-4.557182,-6.500991,-7.747953,0.688482,2.038015,2.736592,-0.277431,-7.108340,-0.523614,0.773510,0.105815,3.643202,-8.482382,-0.379146,6.662986,0.872732,0.895633,5.202316,-4.309624,2.363914,-9.840397,-9.812215,-5.415512,0.785676,-7.754729,-4.447412,-8.998941,-5.252675,4.745965,9.993678,-9.038245,-7.348058,2.521535,-5.431325,3.345648,1.141486,-1.698959,-4.496888,-0.087228,9.586422,-5.749558,5.458036,8.864702,-4.517084,-3.288805,6.659815,-8.355786,9.288252,1.069172,-3.341318,2.292391,5.492234,6.359501,-7.523825,0.461525,-2.164813,-6.507162,-4.135662,4.677567,-9.734190,9.064023,9.427511,-3.068159,3.719863,-3.052692,-3.403835,7.273399,8.781609,4.968062,3.124843,-7.434208,-0.993357,8.665001,-3.428798,3.914242,-8.556044,0.394444,4.874710,-7.555079,3.923886,-8.334888,-3.731018,7.021902,-4.402643,-9.371239,0.182842,8.640010,0.624211,6.449728,9.063115,-9.020573,3.936904,0.007790,4.499731,6.856851,-8.939015,-2.696341,8.030137,2.310231,-2.434559,4.068697,-6.972285,-4.387215,5.452495,8.984376,-3.738490,6.592243,5.602519,-3.703230,-1.495338,-4.699248,3.237973,-5.789236,-1.061068,-6.701581,7.525251,3.798307,-2.917328,9.789443,7.147408,2.458882,-0.963995,0.228489,0.781491,7.874667,2.953296,0.711024,-9.287480,9.339877,3.553873,-1.139139,-2.475188,-0.011358,6.241003,-4.806791,-9.602138,-2.404789,-0.630606,9.862102,-5.908556,-4.675446,-9.885907,-7.276245,4.612878,9.030367,-2.550645,0.459791,9.121953,5.415504,9.575854,8.607516,2.470058,-6.644327,6.281481,-2.987751,-8.037512,9.192100,-4.143503,-2.959554,-7.212330,-3.550707,5.065802,5.953403,6.376484,2.206491,-3.040777,-5.400296,-7.387110,-3.580275,-2.464332,3.655415,8.801382,3.789511,6.271036,2.601460,-0.085266,-7.056858,3.964346,-6.813022,-0.356449,8.098309,4.960915,4.193948,-8.641560,0.309330,-2.651316,-3.449206,-2.225689,8.438810,5.274376,5.211606,-5.994559,0.405979,1.974698,-0.100525,1.861371,-1.320669,2.223453,-8.919970,1.469707,9.532429,4.389275,7.541450,6.144088,0.745713,1.354976,-6.943732,-1.500328,5.302915,-6.044702,1.517206,0.921714,-4.210697,4.191326,5.580877,-8.213910,-3.765767,-7.564458,6.028081,-9.710646,-8.968776,8.009133,4.225314,-2.730249,4.523822,-6.654948,-6.200199,3.014241,8.455280,9.387760,1.087920,5.950600,7.568057,-3.848981,4.607858,1.932575,-7.162204,3.185414,-0.180338,8.575532,-2.685259,3.874405,5.344128,7.484370,6.343493,1.729816,-2.677474,1.911168,-7.089439,2.577021,-6.217823,5.673613,5.951503,0.865447,-8.900609,-7.168403,-3.803369,3.046587,-3.451797,-3.168007,-3.255032,-6.047870,-8.986732,-1.036251,7.085199,6.965944,3.221740,7.148588,8.318497,-6.376587,6.129443,-4.583608,-5.936623,1.822423,-9.996411,1.759360,-3.577450,0.280608,2.080970,8.955958,4.221656,-6.160187,-9.149198,-3.333292,-8.261814,1.331444,7.788252,-9.252983,-9.307911,-3.163682,6.750401,4.159851,4.077935,9.150659,-8.900036,-9.517777,6.723451,-0.976740,-3.713846,0.370094,-6.207884,-8.840431,-4.947550,6.010387,-7.592820,5.703397,9.365137,3.848054,2.378138,0.656924,-3.955971,-0.466116,4.530053,5.094022,3.467641,-8.777365,5.531836,2.827813,8.583435,-8.711527,-8.443088,-5.995480,-1.761951,-4.592401,-7.317707,-3.208165,2.644330,-8.752883,2.006376,-2.285100,-8.937805,-2.927898,5.353892,6.377187,1.479848,2.890474,3.659000,3.436635,8.338886,0.454836,-3.203948,-5.750841,-1.751386,-0.650856,-9.572482,-0.473118,2.794350,1.010470,-8.801813,-5.131281,-6.967512,9.681781,7.341163,-5.400016,4.325944,-3.057263,5.810819,0.367288,1.309294,5.013367,7.293823,-6.806254,5.248415,3.702931,-5.183658,5.348652,5.000559,-9.240789,2.238905,-6.024825,-5.934733,-0.360022,6.997040,-5.892844,5.965605,0.866635,7.597802,-2.686897,0.256897,4.322845,6.464392,-2.362147,2.988790,7.892012,8.662261,6.311775,-2.325868,2.565000,-2.011851,-7.317311,-6.870978,-4.951591,2.341747,-5.949003,-5.376826,-3.967527,-4.417159,7.945627,0.454386,-6.183098,-2.600779,-0.793550,-7.474613,-3.727625,5.513370,-4.730368,-9.479584,-6.765364,6.753001,-3.609088,-4.677364,4.117022,-6.055644,-4.128271,7.684711,-2.204069,5.685042,-2.526747,8.598112,-8.599861,3.378804,-5.027017,3.718581,2.253344,4.736364,-9.828911,-8.359890,-7.283477,-5.388809,-8.141386,0.185701,2.318961,-4.730853,-5.293336,4.039454,-9.278890,-0.662645,-1.073913,0.108892,-4.035413,-2.246812,-7.117637,8.580060,9.221185,-2.551928,5.400993,-9.233967,-3.706850,3.217484,-5.149343,8.068595,0.714576,1.563576,8.690205,-2.620923,8.567097,-4.250724,0.959780,-4.961669,-9.679121,1.852159,2.979455,-8.849660,-6.971452,-5.904672,-8.068963,0.941885,1.283022,-1.397728,-6.721761,2.505653,2.169915,2.814470,2.560974,1.561782,-3.513945,1.644530,-7.474909,8.425112,4.511507,-6.552921,7.350513,-0.292340,-5.070171,3.745656,2.467447,7.765887,0.487914,4.260361,-7.399590,-5.042604,1.006879,-7.679227,9.852502,-5.728630,-2.518878,8.208493,3.525749,-7.221672,-5.035418,-5.713513,-7.596627,-0.210735,-2.863628,-2.997134,-6.773742,-3.724886,5.312250,3.357507,-5.549821,6.376235,-0.316514,3.912617,-2.157635,-8.231195,0.941185,-7.834472,-1.784842,1.341953,4.837014,2.955563,-5.517066,9.925618,4.278412,4.000156,0.848194,-2.087128,7.320538,0.143911,9.112822,-8.768128,-2.100990,2.557159,4.315442,8.686141,-9.312965,-1.420202,-9.230941,-1.132866,-0.954095,-5.453534,0.105454,-6.411891,-7.704243,-9.129181,9.494619,-1.138995,-5.664560,-4.711006,7.164145,-6.434590,-7.278874,-0.875025,-2.384092,-4.005551,-1.960091,-1.108090,3.044831,-9.028296,-9.703452,-8.729896,2.059714,2.858597,-1.410961,9.314185,-9.791552,6.603228,-8.432210,8.253213,1.136936,-0.657095,-3.645553,3.642066,2.000080,0.460117,-5.229797,5.622250,0.553982,4.559227,-4.760284,7.707280,-9.009086,0.556958,-0.937267,-0.835290,3.296498,-9.033826,8.182503,8.896237,1.173050,9.364794,-9.006692,-7.197524,6.110641,6.327581,-0.028521,-3.950690,-5.157217,-8.450192,3.869687,-5.903135,0.939389,-2.559556,-4.727318,0.763474,9.711735,9.091803,0.736322,7.425434,-9.503961,-0.823788,1.840970,6.333548,-6.743096,-5.760027,-4.251139,-7.534628,5.302981,5.986237,7.328731,-6.255156,6.479783,-5.376013,7.409012,0.187620,9.783132,-0.207733,4.428323,-1.987707,2.001680,7.056373,3.948105,8.090169,-1.553181,-3.693396,8.971680,-7.544064,-9.252281,6.094643,-9.161488,1.486584,-6.636575,-8.910283,-4.891588,-1.543295,-1.652628,9.009617,9.383079,-7.114805,4.339954,1.902133], dtype = "float32")#candidate|5912|(990,)|const|float32
call_5911 = func_1515_call(relay.reshape(const_5912.astype('float32'), [10, 9, 11]))
call_5913 = func_1515_call(relay.reshape(const_5912.astype('float32'), [10, 9, 11]))
func_2392_call = mod.get_global_var('func_2392')
func_2396_call = mutated_mod.get_global_var('func_2396')
var_5917 = relay.var("var_5917", dtype = "uint64", shape = (585,))#candidate|5917|(585,)|var|uint64
var_5918 = relay.var("var_5918", dtype = "float32", shape = (63,))#candidate|5918|(63,)|var|float32
call_5916 = relay.TupleGetItem(func_2392_call(relay.reshape(var_5917.astype('uint64'), [13, 5, 9]), relay.reshape(var_5918.astype('float32'), [1, 63]), ), 2)
call_5919 = relay.TupleGetItem(func_2396_call(relay.reshape(var_5917.astype('uint64'), [13, 5, 9]), relay.reshape(var_5918.astype('float32'), [1, 63]), ), 2)
output = relay.Tuple([call_5909,call_5911,const_5912,call_5916,var_5917,var_5918,])
output2 = relay.Tuple([call_5910,call_5913,const_5912,call_5919,var_5917,var_5918,])
func_5937 = relay.Function([var_5917,var_5918,], output)
mod['func_5937'] = func_5937
mod = relay.transform.InferType()(mod)
mutated_mod['func_5937'] = func_5937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5937_call = mutated_mod.get_global_var('func_5937')
var_5939 = relay.var("var_5939", dtype = "uint64", shape = (585,))#candidate|5939|(585,)|var|uint64
var_5940 = relay.var("var_5940", dtype = "float32", shape = (63,))#candidate|5940|(63,)|var|float32
call_5938 = func_5937_call(var_5939,var_5940,)
output = call_5938
func_5941 = relay.Function([var_5939,var_5940,], output)
mutated_mod['func_5941'] = func_5941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_6004 = func_1845_call()
call_6005 = func_1845_call()
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_6027 = func_1845_call()
call_6028 = func_1845_call()
func_2849_call = mod.get_global_var('func_2849')
func_2855_call = mutated_mod.get_global_var('func_2855')
var_6030 = relay.var("var_6030", dtype = "uint32", shape = (1440,))#candidate|6030|(1440,)|var|uint32
var_6031 = relay.var("var_6031", dtype = "float32", shape = (63,))#candidate|6031|(63,)|var|float32
call_6029 = relay.TupleGetItem(func_2849_call(relay.reshape(var_6030.astype('uint32'), [12, 10, 12]), relay.reshape(var_6030.astype('uint32'), [12, 10, 12]), relay.reshape(var_6031.astype('float32'), [63,]), relay.reshape(var_6030.astype('uint32'), [12, 10, 12]), ), 1)
call_6032 = relay.TupleGetItem(func_2855_call(relay.reshape(var_6030.astype('uint32'), [12, 10, 12]), relay.reshape(var_6030.astype('uint32'), [12, 10, 12]), relay.reshape(var_6031.astype('float32'), [63,]), relay.reshape(var_6030.astype('uint32'), [12, 10, 12]), ), 1)
output = relay.Tuple([call_6004,call_6027,call_6029,var_6030,var_6031,])
output2 = relay.Tuple([call_6005,call_6028,call_6032,var_6030,var_6031,])
func_6038 = relay.Function([var_6030,var_6031,], output)
mod['func_6038'] = func_6038
mod = relay.transform.InferType()(mod)
var_6039 = relay.var("var_6039", dtype = "uint32", shape = (1440,))#candidate|6039|(1440,)|var|uint32
var_6040 = relay.var("var_6040", dtype = "float32", shape = (63,))#candidate|6040|(63,)|var|float32
output = func_6038(var_6039,var_6040,)
func_6041 = relay.Function([var_6039,var_6040,], output)
mutated_mod['func_6041'] = func_6041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3155_call = mod.get_global_var('func_3155')
func_3156_call = mutated_mod.get_global_var('func_3156')
call_6066 = func_3155_call()
call_6067 = func_3155_call()
func_3780_call = mod.get_global_var('func_3780')
func_3783_call = mutated_mod.get_global_var('func_3783')
call_6068 = func_3780_call(relay.reshape(call_6066.astype('uint64'), [1, 5, 9]))
call_6069 = func_3780_call(relay.reshape(call_6066.astype('uint64'), [1, 5, 9]))
func_3299_call = mod.get_global_var('func_3299')
func_3301_call = mutated_mod.get_global_var('func_3301')
call_6079 = relay.TupleGetItem(func_3299_call(), 0)
call_6080 = relay.TupleGetItem(func_3301_call(), 0)
output = relay.Tuple([call_6066,call_6068,call_6079,])
output2 = relay.Tuple([call_6067,call_6069,call_6080,])
func_6087 = relay.Function([], output)
mod['func_6087'] = func_6087
mod = relay.transform.InferType()(mod)
mutated_mod['func_6087'] = func_6087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6087_call = mutated_mod.get_global_var('func_6087')
call_6088 = func_6087_call()
output = call_6088
func_6089 = relay.Function([], output)
mutated_mod['func_6089'] = func_6089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6090 = relay.var("var_6090", dtype = "float32", shape = (16, 16, 14))#candidate|6090|(16, 16, 14)|var|float32
uop_6091 = relay.atanh(var_6090.astype('float32')) # shape=(16, 16, 14)
output = relay.Tuple([uop_6091,])
output2 = relay.Tuple([uop_6091,])
func_6093 = relay.Function([var_6090,], output)
mod['func_6093'] = func_6093
mod = relay.transform.InferType()(mod)
mutated_mod['func_6093'] = func_6093
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6094 = relay.var("var_6094", dtype = "float32", shape = (16, 16, 14))#candidate|6094|(16, 16, 14)|var|float32
func_6093_call = mutated_mod.get_global_var('func_6093')
call_6095 = func_6093_call(var_6094)
output = call_6095
func_6096 = relay.Function([var_6094], output)
mutated_mod['func_6096'] = func_6096
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6113 = relay.var("var_6113", dtype = "float64", shape = ())#candidate|6113|()|var|float64
var_6114 = relay.var("var_6114", dtype = "float64", shape = (6, 14, 14))#candidate|6114|(6, 14, 14)|var|float64
bop_6115 = relay.minimum(var_6113.astype('float64'), var_6114.astype('float64')) # shape=(6, 14, 14)
bop_6141 = relay.add(var_6113.astype('float64'), bop_6115.astype('float64')) # shape=(6, 14, 14)
output = bop_6141
output2 = bop_6141
func_6157 = relay.Function([var_6113,var_6114,], output)
mod['func_6157'] = func_6157
mod = relay.transform.InferType()(mod)
var_6158 = relay.var("var_6158", dtype = "float64", shape = ())#candidate|6158|()|var|float64
var_6159 = relay.var("var_6159", dtype = "float64", shape = (6, 14, 14))#candidate|6159|(6, 14, 14)|var|float64
output = func_6157(var_6158,var_6159,)
func_6160 = relay.Function([var_6158,var_6159,], output)
mutated_mod['func_6160'] = func_6160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5461_call = mod.get_global_var('func_5461')
func_5462_call = mutated_mod.get_global_var('func_5462')
call_6209 = relay.TupleGetItem(func_5461_call(), 0)
call_6210 = relay.TupleGetItem(func_5462_call(), 0)
func_4823_call = mod.get_global_var('func_4823')
func_4824_call = mutated_mod.get_global_var('func_4824')
call_6222 = func_4823_call()
call_6223 = func_4823_call()
output = relay.Tuple([call_6209,call_6222,])
output2 = relay.Tuple([call_6210,call_6223,])
func_6224 = relay.Function([], output)
mod['func_6224'] = func_6224
mod = relay.transform.InferType()(mod)
mutated_mod['func_6224'] = func_6224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6224_call = mutated_mod.get_global_var('func_6224')
call_6225 = func_6224_call()
output = call_6225
func_6226 = relay.Function([], output)
mutated_mod['func_6226'] = func_6226
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6266 = relay.var("var_6266", dtype = "float32", shape = (2, 10, 4))#candidate|6266|(2, 10, 4)|var|float32
var_6267 = relay.var("var_6267", dtype = "float32", shape = (2, 10, 4))#candidate|6267|(2, 10, 4)|var|float32
bop_6268 = relay.mod(var_6266.astype('float32'), relay.reshape(var_6267.astype('float32'), relay.shape_of(var_6266))) # shape=(2, 10, 4)
func_5110_call = mod.get_global_var('func_5110')
func_5111_call = mutated_mod.get_global_var('func_5111')
call_6274 = relay.TupleGetItem(func_5110_call(), 1)
call_6275 = relay.TupleGetItem(func_5111_call(), 1)
uop_6284 = relay.asin(bop_6268.astype('float64')) # shape=(2, 10, 4)
output = relay.Tuple([call_6274,uop_6284,])
output2 = relay.Tuple([call_6275,uop_6284,])
func_6289 = relay.Function([var_6266,var_6267,], output)
mod['func_6289'] = func_6289
mod = relay.transform.InferType()(mod)
var_6290 = relay.var("var_6290", dtype = "float32", shape = (2, 10, 4))#candidate|6290|(2, 10, 4)|var|float32
var_6291 = relay.var("var_6291", dtype = "float32", shape = (2, 10, 4))#candidate|6291|(2, 10, 4)|var|float32
output = func_6289(var_6290,var_6291,)
func_6292 = relay.Function([var_6290,var_6291,], output)
mutated_mod['func_6292'] = func_6292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6087_call = mod.get_global_var('func_6087')
func_6089_call = mutated_mod.get_global_var('func_6089')
call_6296 = relay.TupleGetItem(func_6087_call(), 1)
call_6297 = relay.TupleGetItem(func_6089_call(), 1)
func_5853_call = mod.get_global_var('func_5853')
func_5856_call = mutated_mod.get_global_var('func_5856')
const_6299 = relay.const([[1,-2,-1,6,-8,-3,6,7,-3,7,-2,5,6,1,-1,10,6,-10,1,-6,-8,3,-6,10,-1,-9,5,1,7,9,-8,1,1,2,5,10,-6,-7,-3,-2,-6,-9,7,4,-3,-2,-4,-6,4,8,5,5,2,4,1,-10,-8,-7,1,9,-6,9,-5,6,5,1,3,1,-9,3,-10,-4,3,5,5,-10,-6,3,-5,5,3,10,-3,3,6,10,8,4,7,7,-3,3,5,-5,4,-10,5,5,1,-9,-6,10,-5,7,-6,-4,-1,-10,-4,9,-4,-7,9,6,1,-6,4,-1,4,1,-2,9,-1,-10,-6,2],[-9,9,-10,9,-10,-8,-3,-3,9,-5,8,-4,6,7,4,4,-8,-1,-7,2,5,4,-1,3,3,-2,-3,-4,-2,-3,-10,-10,-9,9,-1,-5,-10,-4,-8,-2,-6,-3,-1,-10,-8,1,-9,6,-4,-5,-3,3,1,-4,-4,-1,-1,1,-3,-8,3,9,-2,1,-2,-1,9,10,-1,1,3,6,-8,7,-10,-2,-4,-7,8,10,-6,-6,-5,5,1,1,-1,5,8,1,-6,-10,-8,5,-5,-7,-8,-6,-7,10,10,-1,2,10,-9,5,6,6,-4,-1,7,-2,10,9,10,5,-3,-10,-2,3,1,-7,-5,10,-3,8],[10,-7,7,-8,-5,8,-9,3,7,5,5,-5,-4,-2,8,10,-2,-8,5,8,9,8,-2,-1,8,-9,7,-5,-10,9,1,-8,8,-1,-2,-3,-5,-8,3,-10,-3,-3,-4,3,-9,4,4,2,9,-3,4,-1,8,-10,7,9,8,4,2,7,-10,9,6,7,7,-6,7,-2,7,3,1,-5,4,2,-7,-7,-2,2,-10,-1,9,7,-7,9,8,-7,4,9,-3,5,-10,8,9,-9,-9,7,10,-5,3,-8,-8,2,-8,1,2,1,6,-3,9,7,4,7,-8,-10,6,1,-4,-5,4,6,-10,9,8,5,5,5],[-6,3,7,-4,-1,7,8,10,8,1,2,-7,1,8,-6,7,-9,7,-4,-9,5,-10,9,-6,-5,6,6,-10,7,-5,4,6,-2,9,3,-3,-3,-1,5,1,6,-9,-3,1,8,-5,-10,8,-4,-10,-5,5,-5,2,6,10,-1,4,10,3,1,-2,1,-3,-7,1,-5,9,3,-10,5,10,-10,7,10,-10,10,-2,-4,-5,9,2,-2,-3,-4,-5,4,-2,-2,6,1,-4,8,1,4,-2,9,6,4,-10,4,-7,3,-5,-2,-8,5,-3,2,4,7,-9,-9,-2,6,-3,-5,3,2,2,6,-7,4,7,-4,-9],[6,-1,-5,-10,-3,5,3,-8,3,1,2,4,7,-9,2,-6,-8,-5,-8,-5,-8,-10,6,8,-10,3,-6,-7,8,-8,7,-1,8,7,-3,-8,-3,-5,-8,2,-3,-9,4,4,5,-2,-3,-5,-3,9,-7,10,-5,2,-8,-3,-1,-10,10,7,-3,8,-4,-10,-7,4,6,-7,6,6,6,-5,-2,2,-8,-9,-7,-10,10,-7,-9,-3,4,-7,1,-6,-5,-6,7,-10,6,-9,-6,4,-9,5,4,4,-9,-10,-6,-9,-7,-9,2,1,-9,-1,-9,3,7,-7,-5,1,-4,6,7,-3,8,-1,1,8,-4,7,3,-3]], dtype = "uint64")#candidate|6299|(5, 126)|const|uint64
call_6298 = func_5853_call(relay.reshape(const_6299.astype('uint64'), [14, 5, 9]))
call_6300 = func_5853_call(relay.reshape(const_6299.astype('uint64'), [14, 5, 9]))
output = relay.Tuple([call_6296,call_6298,const_6299,])
output2 = relay.Tuple([call_6297,call_6300,const_6299,])
func_6303 = relay.Function([], output)
mod['func_6303'] = func_6303
mod = relay.transform.InferType()(mod)
mutated_mod['func_6303'] = func_6303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6303_call = mutated_mod.get_global_var('func_6303')
call_6304 = func_6303_call()
output = call_6304
func_6305 = relay.Function([], output)
mutated_mod['func_6305'] = func_6305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4411_call = mod.get_global_var('func_4411')
func_4413_call = mutated_mod.get_global_var('func_4413')
call_6436 = relay.TupleGetItem(func_4411_call(), 1)
call_6437 = relay.TupleGetItem(func_4413_call(), 1)
output = relay.Tuple([call_6436,])
output2 = relay.Tuple([call_6437,])
func_6469 = relay.Function([], output)
mod['func_6469'] = func_6469
mod = relay.transform.InferType()(mod)
output = func_6469()
func_6470 = relay.Function([], output)
mutated_mod['func_6470'] = func_6470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3214_call = mod.get_global_var('func_3214')
func_3215_call = mutated_mod.get_global_var('func_3215')
call_6513 = func_3214_call()
call_6514 = func_3214_call()
func_5351_call = mod.get_global_var('func_5351')
func_5353_call = mutated_mod.get_global_var('func_5353')
call_6524 = func_5351_call()
call_6525 = func_5351_call()
func_1985_call = mod.get_global_var('func_1985')
func_1987_call = mutated_mod.get_global_var('func_1987')
call_6533 = relay.TupleGetItem(func_1985_call(), 2)
call_6534 = relay.TupleGetItem(func_1987_call(), 2)
output = relay.Tuple([call_6513,call_6524,call_6533,])
output2 = relay.Tuple([call_6514,call_6525,call_6534,])
func_6540 = relay.Function([], output)
mod['func_6540'] = func_6540
mod = relay.transform.InferType()(mod)
output = func_6540()
func_6541 = relay.Function([], output)
mutated_mod['func_6541'] = func_6541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4270_call = mod.get_global_var('func_4270')
func_4272_call = mutated_mod.get_global_var('func_4272')
call_6564 = relay.TupleGetItem(func_4270_call(), 4)
call_6565 = relay.TupleGetItem(func_4272_call(), 4)
func_935_call = mod.get_global_var('func_935')
func_937_call = mutated_mod.get_global_var('func_937')
call_6571 = relay.TupleGetItem(func_935_call(), 0)
call_6572 = relay.TupleGetItem(func_937_call(), 0)
bop_6576 = relay.bitwise_or(call_6564.astype('uint16'), relay.reshape(call_6571.astype('uint16'), relay.shape_of(call_6564))) # shape=(1, 5, 9)
bop_6579 = relay.bitwise_or(call_6565.astype('uint16'), relay.reshape(call_6572.astype('uint16'), relay.shape_of(call_6565))) # shape=(1, 5, 9)
func_5937_call = mod.get_global_var('func_5937')
func_5941_call = mutated_mod.get_global_var('func_5941')
const_6587 = relay.const([-2,-5,-7,-1,-2,1,-7,-10,9,6,-2,-6,-6,4,-7,7,2,-2,-8,1,7,1,2,6,1,-1,-5,-1,-9,-10,-8,8,9,-10,-5,7,4,-10,1,-10,-6,-5,-5,-1,3,-1,-8,-10,10,-6,-2,-9,-2,3,-4,6,-1,10,9,-10,-5,-1,1,4,1,8,-2,10,-5,7,-5,9,6,-3,5,5,-6,6,8,-9,-9,-4,4,-5,6,-10,5,-8,3,3,-5,-9,-7,-8,-3,5,6,3,3,10,-9,2,-4,-6,2,-4,-10,-9,5,1,6,2,-3,-1,2,-6,4,7,-10,2,2,8,8,-8,-5,-5,-5,1,1,-6,3,-7,2,2,7,-4,1,-3,-1,6,-2,-7,5,6,-1,-10,-6,1,1,10,1,-10,-7,-3,-4,4,-7,4,8,1,-6,-4,-10,-10,10,10,7,-6,-3,-1,-10,-4,6,1,1,3,-3,-10,4,5,-4,-5,-4,-3,2,5,-1,-8,-10,2,1,9,-4,8,-10,2,-7,-3,10,8,-2,-3,-4,1,-2,-3,8,-8,2,-10,8,-4,-1,-7,-3,-6,-10,9,9,-5,-2,-5,-4,-3,-8,7,-5,2,10,-10,6,9,4,-9,-7,-6,-7,-9,4,5,5,10,7,-7,-3,9,2,5,-7,2,1,2,9,-6,3,4,7,7,8,-8,-2,2,6,-1,4,-8,-9,2,2,-10,-3,-3,10,2,-4,1,-9,10,-4,10,-4,4,1,-3,8,-9,10,9,4,10,-4,-5,-5,10,-8,9,3,7,-1,-6,-6,10,-9,-7,-2,2,-7,-9,-2,4,-3,3,-6,9,-1,-6,10,-2,-5,-3,-6,-3,1,-7,-2,4,4,3,-6,-9,7,-3,-3,7,3,-5,4,4,-1,-8,-2,2,10,9,-8,-4,-4,-4,-3,7,3,-9,-1,2,-1,-6,-5,-2,2,10,10,6,4,-2,-3,4,-10,-2,-5,-2,-7,1,5,-6,5,-8,1,-10,4,-1,-9,-2,10,-10,10,-1,-10,-8,6,-3,-9,7,-7,-4,-6,-9,-2,6,4,-8,9,3,2,6,5,-10,-4,-6,-1,-3,7,-6,4,-2,-9,5,10,9,7,-1,-9,-9,-9,4,-5,-8,1,-1,5,3,6,6,-4,-9,2,-5,2,-4,9,2,6,-6,6,-4,-5,-7,-7,-8,-7,3,-8,2,4,-2,5,9,-5,-10,6,-2,-3,3,-1,2,-9,-9,5,10,7,-6,-7,-6,2,1,-2,-9,1,6,3,2,-2,1,-2,9,-3,4,10,4,5,-9,10,3,-10,-5,-8,-4,-8,8,-6,-1,-3,-2,-4,6,10,8,5,-1,-2,-7,3,-1,-6,3,7,2,-9,-5,-9,-2,-8,10,2,8,2,-6,-7,-8,-7,5,-4,-6,-3,6,3,4,-8,5,-10,6,8,-6,9,6,-4,-10,1,-1,-8,-10,-5,-4,-3,-3,-2,4,10,-5,-6,5,-3,10,2,2,-10,-2,-9,8,-5,-4,9,-7,1,-8,-4,-1,-9,-2,-4,-2,9,9,-8,1,-7], dtype = "uint64")#candidate|6587|(585,)|const|uint64
var_6588 = relay.var("var_6588", dtype = "float32", shape = (63,))#candidate|6588|(63,)|var|float32
call_6586 = relay.TupleGetItem(func_5937_call(relay.reshape(const_6587.astype('uint64'), [585,]), relay.reshape(var_6588.astype('float32'), [63,]), ), 1)
call_6589 = relay.TupleGetItem(func_5941_call(relay.reshape(const_6587.astype('uint64'), [585,]), relay.reshape(var_6588.astype('float32'), [63,]), ), 1)
output = relay.Tuple([bop_6576,call_6586,const_6587,var_6588,])
output2 = relay.Tuple([bop_6579,call_6589,const_6587,var_6588,])
func_6599 = relay.Function([var_6588,], output)
mod['func_6599'] = func_6599
mod = relay.transform.InferType()(mod)
mutated_mod['func_6599'] = func_6599
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6600 = relay.var("var_6600", dtype = "float32", shape = (63,))#candidate|6600|(63,)|var|float32
func_6599_call = mutated_mod.get_global_var('func_6599')
call_6601 = func_6599_call(var_6600)
output = call_6601
func_6602 = relay.Function([var_6600], output)
mutated_mod['func_6602'] = func_6602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5726_call = mod.get_global_var('func_5726')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_6614 = relay.TupleGetItem(func_5726_call(), 0)
call_6615 = relay.TupleGetItem(func_5728_call(), 0)
func_3069_call = mod.get_global_var('func_3069')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_6618 = relay.TupleGetItem(func_3069_call(), 1)
call_6619 = relay.TupleGetItem(func_3070_call(), 1)
func_4557_call = mod.get_global_var('func_4557')
func_4558_call = mutated_mod.get_global_var('func_4558')
call_6625 = relay.TupleGetItem(func_4557_call(), 1)
call_6626 = relay.TupleGetItem(func_4558_call(), 1)
func_1737_call = mod.get_global_var('func_1737')
func_1739_call = mutated_mod.get_global_var('func_1739')
call_6630 = relay.TupleGetItem(func_1737_call(), 0)
call_6631 = relay.TupleGetItem(func_1739_call(), 0)
func_3069_call = mod.get_global_var('func_3069')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_6637 = relay.TupleGetItem(func_3069_call(), 1)
call_6638 = relay.TupleGetItem(func_3070_call(), 1)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_6640 = func_791_call()
call_6641 = func_791_call()
output = relay.Tuple([call_6614,call_6618,call_6625,call_6630,call_6637,call_6640,])
output2 = relay.Tuple([call_6615,call_6619,call_6626,call_6631,call_6638,call_6641,])
func_6642 = relay.Function([], output)
mod['func_6642'] = func_6642
mod = relay.transform.InferType()(mod)
output = func_6642()
func_6643 = relay.Function([], output)
mutated_mod['func_6643'] = func_6643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3883_call = mod.get_global_var('func_3883')
func_3884_call = mutated_mod.get_global_var('func_3884')
call_6722 = func_3883_call()
call_6723 = func_3883_call()
func_5597_call = mod.get_global_var('func_5597')
func_5599_call = mutated_mod.get_global_var('func_5599')
call_6725 = relay.TupleGetItem(func_5597_call(), 0)
call_6726 = relay.TupleGetItem(func_5599_call(), 0)
func_5817_call = mod.get_global_var('func_5817')
func_5819_call = mutated_mod.get_global_var('func_5819')
call_6730 = relay.TupleGetItem(func_5817_call(), 2)
call_6731 = relay.TupleGetItem(func_5819_call(), 2)
output = relay.Tuple([call_6722,call_6725,call_6730,])
output2 = relay.Tuple([call_6723,call_6726,call_6731,])
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
func_1791_call = mod.get_global_var('func_1791')
func_1793_call = mutated_mod.get_global_var('func_1793')
call_6738 = relay.TupleGetItem(func_1791_call(), 3)
call_6739 = relay.TupleGetItem(func_1793_call(), 3)
func_454_call = mod.get_global_var('func_454')
func_456_call = mutated_mod.get_global_var('func_456')
call_6767 = relay.TupleGetItem(func_454_call(), 0)
call_6768 = relay.TupleGetItem(func_456_call(), 0)
bop_6775 = relay.floor_mod(call_6738.astype('float32'), relay.reshape(call_6767.astype('float32'), relay.shape_of(call_6738))) # shape=(1, 5, 9)
bop_6778 = relay.floor_mod(call_6739.astype('float32'), relay.reshape(call_6768.astype('float32'), relay.shape_of(call_6739))) # shape=(1, 5, 9)
func_5110_call = mod.get_global_var('func_5110')
func_5111_call = mutated_mod.get_global_var('func_5111')
call_6780 = relay.TupleGetItem(func_5110_call(), 0)
call_6781 = relay.TupleGetItem(func_5111_call(), 0)
func_5324_call = mod.get_global_var('func_5324')
func_5326_call = mutated_mod.get_global_var('func_5326')
call_6784 = func_5324_call()
call_6785 = func_5324_call()
func_689_call = mod.get_global_var('func_689')
func_692_call = mutated_mod.get_global_var('func_692')
var_6790 = relay.var("var_6790", dtype = "int32", shape = ())#candidate|6790|()|var|int32
const_6791 = relay.const([[7],[7],[8],[-1],[6],[10],[-7],[8],[-5],[10],[4],[10],[3],[-9],[3],[-8],[-7],[-10],[-6],[-10],[4],[-4],[8],[8],[-3],[-7],[-2],[-6],[10],[10],[3],[4],[4],[-7],[-7],[-3],[-6],[-4],[1],[8],[-8],[-2],[9],[-5],[-5],[2],[4],[-10],[-2],[-9],[3],[-1],[-10],[-3],[-7],[-4],[5],[7],[-4],[-3],[-9],[7],[-3],[-10],[-3],[5],[2],[4],[3],[3]], dtype = "int32")#candidate|6791|(70, 1)|const|int32
call_6789 = relay.TupleGetItem(func_689_call(relay.reshape(var_6790.astype('int32'), []), relay.reshape(const_6791.astype('int32'), [7, 1, 10]), ), 0)
call_6792 = relay.TupleGetItem(func_692_call(relay.reshape(var_6790.astype('int32'), []), relay.reshape(const_6791.astype('int32'), [7, 1, 10]), ), 0)
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
call_6793 = relay.TupleGetItem(func_592_call(), 1)
call_6794 = relay.TupleGetItem(func_594_call(), 1)
output = relay.Tuple([bop_6775,call_6780,call_6784,call_6789,var_6790,const_6791,call_6793,])
output2 = relay.Tuple([bop_6778,call_6781,call_6785,call_6792,var_6790,const_6791,call_6794,])
func_6799 = relay.Function([var_6790,], output)
mod['func_6799'] = func_6799
mod = relay.transform.InferType()(mod)
var_6800 = relay.var("var_6800", dtype = "int32", shape = ())#candidate|6800|()|var|int32
output = func_6799(var_6800)
func_6801 = relay.Function([var_6800], output)
mutated_mod['func_6801'] = func_6801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4215_call = mod.get_global_var('func_4215')
func_4217_call = mutated_mod.get_global_var('func_4217')
call_6851 = func_4215_call()
call_6852 = func_4215_call()
func_1567_call = mod.get_global_var('func_1567')
func_1568_call = mutated_mod.get_global_var('func_1568')
call_6860 = relay.TupleGetItem(func_1567_call(), 0)
call_6861 = relay.TupleGetItem(func_1568_call(), 0)
func_1124_call = mod.get_global_var('func_1124')
func_1126_call = mutated_mod.get_global_var('func_1126')
call_6863 = func_1124_call()
call_6864 = func_1124_call()
func_506_call = mod.get_global_var('func_506')
func_509_call = mutated_mod.get_global_var('func_509')
var_6868 = relay.var("var_6868", dtype = "float64", shape = (48,))#candidate|6868|(48,)|var|float64
call_6867 = relay.TupleGetItem(func_506_call(relay.reshape(var_6868.astype('float64'), [3, 2, 8]), relay.reshape(var_6868.astype('float64'), [3, 2, 8]), ), 0)
call_6869 = relay.TupleGetItem(func_509_call(relay.reshape(var_6868.astype('float64'), [3, 2, 8]), relay.reshape(var_6868.astype('float64'), [3, 2, 8]), ), 0)
output = relay.Tuple([call_6851,call_6860,call_6863,call_6867,var_6868,])
output2 = relay.Tuple([call_6852,call_6861,call_6864,call_6869,var_6868,])
func_6907 = relay.Function([var_6868,], output)
mod['func_6907'] = func_6907
mod = relay.transform.InferType()(mod)
var_6908 = relay.var("var_6908", dtype = "float64", shape = (48,))#candidate|6908|(48,)|var|float64
output = func_6907(var_6908)
func_6909 = relay.Function([var_6908], output)
mutated_mod['func_6909'] = func_6909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1567_call = mod.get_global_var('func_1567')
func_1568_call = mutated_mod.get_global_var('func_1568')
call_6942 = relay.TupleGetItem(func_1567_call(), 0)
call_6943 = relay.TupleGetItem(func_1568_call(), 0)
func_3247_call = mod.get_global_var('func_3247')
func_3248_call = mutated_mod.get_global_var('func_3248')
call_6953 = relay.TupleGetItem(func_3247_call(), 0)
call_6954 = relay.TupleGetItem(func_3248_call(), 0)
output = relay.Tuple([call_6942,call_6953,])
output2 = relay.Tuple([call_6943,call_6954,])
func_6964 = relay.Function([], output)
mod['func_6964'] = func_6964
mod = relay.transform.InferType()(mod)
output = func_6964()
func_6965 = relay.Function([], output)
mutated_mod['func_6965'] = func_6965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6303_call = mod.get_global_var('func_6303')
func_6305_call = mutated_mod.get_global_var('func_6305')
call_6966 = relay.TupleGetItem(func_6303_call(), 0)
call_6967 = relay.TupleGetItem(func_6305_call(), 0)
output = call_6966
output2 = call_6967
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
func_5195_call = mod.get_global_var('func_5195')
func_5197_call = mutated_mod.get_global_var('func_5197')
call_7003 = func_5195_call()
call_7004 = func_5195_call()
output = relay.Tuple([call_7003,])
output2 = relay.Tuple([call_7004,])
func_7008 = relay.Function([], output)
mod['func_7008'] = func_7008
mod = relay.transform.InferType()(mod)
output = func_7008()
func_7009 = relay.Function([], output)
mutated_mod['func_7009'] = func_7009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4823_call = mod.get_global_var('func_4823')
func_4824_call = mutated_mod.get_global_var('func_4824')
call_7016 = func_4823_call()
call_7017 = func_4823_call()
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_7024 = relay.TupleGetItem(func_1336_call(), 0)
call_7025 = relay.TupleGetItem(func_1338_call(), 0)
func_5817_call = mod.get_global_var('func_5817')
func_5819_call = mutated_mod.get_global_var('func_5819')
call_7037 = relay.TupleGetItem(func_5817_call(), 3)
call_7038 = relay.TupleGetItem(func_5819_call(), 3)
output = relay.Tuple([call_7016,call_7024,call_7037,])
output2 = relay.Tuple([call_7017,call_7025,call_7038,])
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
var_7075 = relay.var("var_7075", dtype = "int16", shape = (14, 9, 10))#candidate|7075|(14, 9, 10)|var|int16
const_7076 = relay.const([[[-7,5,9,6,-1,5,3,-4,-4,3],[-9,2,6,-8,-1,5,7,3,3,6],[-6,9,6,8,-8,-1,-10,6,7,9],[9,7,3,6,1,9,10,9,-3,-9],[8,8,10,-5,10,-6,-9,6,5,7],[3,-3,6,-10,-9,-8,8,-6,-1,-9],[9,9,10,-10,-7,-9,5,-5,4,-9],[-6,-9,-4,5,7,4,9,2,9,4],[-10,-8,5,-5,-1,-3,3,3,6,-3]],[[-2,-9,-2,-2,-4,9,-9,9,2,-4],[-10,2,-8,3,3,-9,4,-7,10,7],[4,-7,5,-9,-2,2,10,7,8,-4],[-5,5,-10,6,-2,3,1,10,-6,4],[2,1,-9,1,-8,8,7,-3,-10,6],[-3,9,-9,-1,8,4,-1,-1,3,10],[9,5,5,-3,-6,-6,-8,-5,4,1],[-9,-1,9,-3,-5,4,-2,10,-6,10],[-1,-2,-1,-7,1,6,-4,2,-10,8]],[[9,9,-10,7,-3,-7,-3,-5,-6,-9],[2,-8,-2,-10,7,-8,-9,-6,-8,-4],[-9,-5,-1,-9,5,-3,3,1,-2,-6],[10,-3,-10,9,-1,-9,7,-7,6,-5],[-3,-6,-10,2,2,8,1,-3,10,9],[9,4,-3,4,6,-8,10,7,-3,-9],[-6,-6,-10,-8,-3,4,6,-7,10,6],[-3,-6,10,-2,-10,-9,9,3,-6,-10],[7,-2,1,-2,3,6,4,-10,5,9]],[[-2,-4,-8,10,8,-5,-3,8,8,-4],[7,10,2,-6,-1,-4,5,-8,5,-9],[10,-7,-2,-7,-4,3,1,-3,-5,-1],[5,-3,-3,5,9,-10,7,1,4,-2],[-9,10,-10,4,-1,2,-2,8,6,-5],[7,-3,5,-6,2,-7,-4,-2,1,10],[4,-10,6,4,-1,-6,-6,-3,-5,-2],[-8,9,-10,-4,10,5,-5,10,2,3],[3,-4,-10,-4,7,-3,6,4,-2,7]],[[4,6,8,1,10,-5,-5,5,-5,2],[4,-6,-7,8,-1,-3,-8,4,-7,-6],[-1,3,10,-3,5,-9,-3,1,7,9],[-4,-5,-3,8,4,-8,-7,-10,7,1],[3,2,7,3,-3,-6,-9,1,1,-4],[5,1,5,6,7,5,-9,5,2,-2],[2,-6,-8,-5,-6,6,-2,-3,6,-8],[-9,4,-4,6,7,-3,-7,-2,-5,5],[-7,-5,6,6,7,7,-1,-6,10,-10]],[[-3,5,-1,-4,-5,8,-10,3,-10,7],[4,-5,-7,-9,4,-3,10,6,7,8],[1,-6,-10,6,-9,-9,-1,8,-7,4],[-4,-10,-6,-8,10,-7,-3,-3,-1,4],[4,-2,10,-2,9,-10,-4,1,-1,-5],[4,-2,-6,-1,6,8,1,-6,2,-9],[7,-7,-2,-2,-7,3,-10,10,4,2],[7,1,-10,10,-6,-6,-10,3,-1,-6],[4,10,8,10,1,1,2,7,-8,7]],[[-8,6,-7,-4,4,7,-1,1,-6,1],[-3,-5,-6,-10,-1,-10,-1,9,-5,-6],[-4,8,9,7,10,-3,4,-1,-10,5],[-9,2,-1,-8,5,7,9,7,7,-5],[3,2,-8,8,-6,-1,7,-5,-4,7],[8,-9,1,7,1,5,-4,1,-1,-9],[-1,-2,-4,9,1,-7,1,-8,-3,10],[-10,8,-1,-3,-10,-1,-5,-1,1,8],[7,-3,-3,-1,-5,-2,6,-9,9,-1]],[[-8,-1,-9,-3,4,4,-7,2,-7,10],[-3,-9,10,-8,-1,9,-5,-2,1,-7],[-7,8,10,-5,2,1,8,6,9,9],[3,7,6,-4,-5,4,2,5,2,8],[-7,-9,10,-3,7,7,7,10,3,4],[5,-7,2,8,4,-5,-7,-4,-10,-4],[-6,-9,-6,8,-4,-7,-2,5,-8,5],[-1,1,-5,-2,1,-1,8,-3,10,-6],[-6,1,-7,10,-1,7,5,7,4,-6]],[[7,5,-7,2,10,2,-10,1,-1,-5],[6,-4,2,5,-1,5,8,5,-8,5],[-6,-1,-9,-8,-5,-5,-6,6,-8,-8],[-1,9,2,-7,5,-8,10,-1,-4,-1],[1,2,5,-9,-8,-4,-9,10,-8,-4],[2,8,-3,-1,6,-8,8,-8,7,-5],[-2,5,3,5,-4,-6,8,8,-3,-8],[1,-7,5,1,1,-8,7,6,-1,-3],[7,3,3,9,-10,-4,5,9,9,4]],[[10,-4,-5,8,1,-1,1,8,-5,10],[5,4,9,10,7,-9,5,-3,4,-6],[-1,5,-1,5,-9,-1,1,4,1,10],[-7,-5,10,3,-9,3,6,-1,-3,4],[3,8,-1,6,6,9,2,-8,-2,-10],[-1,-1,3,3,8,7,3,7,-8,5],[8,-1,-10,5,-1,-2,-8,-7,-5,-6],[-10,-4,8,4,-4,-4,-6,3,2,-7],[2,5,-10,-10,5,-8,9,-5,-5,7]],[[-9,-2,-3,-1,4,10,-7,6,7,2],[4,-6,-6,-1,1,2,8,7,10,8],[5,-10,5,10,3,-4,4,9,-1,2],[-8,-2,-10,-10,6,-4,10,-1,-9,-6],[3,-9,-2,-10,7,-4,6,-3,-4,9],[-5,-9,7,9,-1,10,7,-4,8,-1],[-5,1,-1,-10,-1,3,1,10,-3,6],[4,-9,-7,-9,4,9,-4,-1,-7,8],[-9,2,4,-6,1,-1,9,-5,1,-1]],[[-3,-4,-1,2,7,3,-2,4,9,2],[-3,6,-3,10,6,-10,-2,-5,-1,-10],[-6,4,10,-5,7,10,2,-4,6,10],[-7,-10,-7,1,-4,6,-4,10,-8,2],[2,-7,-7,-9,9,4,10,-3,2,4],[-5,-8,3,-2,4,-8,7,1,10,-6],[1,-3,7,-7,3,5,-4,-6,2,9],[5,2,-5,-5,-5,4,-4,-9,6,-10],[-9,-7,-9,-1,-3,8,-10,-10,-5,3]],[[-8,8,-5,-1,-2,10,-5,6,1,6],[10,2,6,8,-6,3,-8,-6,-9,6],[7,5,-2,-5,-10,7,-6,-1,-10,6],[-8,2,2,-8,4,-4,-9,-2,-10,6],[-9,-2,-1,-9,-10,10,4,5,-7,-8],[-9,1,-1,-1,-9,5,-7,5,7,-2],[9,-8,-2,-10,8,-2,-10,4,-6,-6],[-9,5,7,-7,-7,3,1,-8,6,3],[-6,10,-10,9,9,-2,-6,6,8,8]],[[-4,-1,4,-7,-7,-6,-7,-9,1,2],[-3,8,-1,3,-2,7,3,9,7,-10],[8,7,2,-4,-2,-3,-3,4,-9,-7],[9,-5,4,-2,1,7,-9,5,-8,6],[-9,7,-2,-8,-10,-2,-1,-1,-10,-5],[-4,10,-7,-5,-8,-5,10,9,-4,4],[1,1,10,4,5,-3,-4,-2,-10,3],[8,4,-3,3,-7,-9,1,-10,-2,-5],[8,5,2,10,-4,9,5,3,6,3]]], dtype = "int16")#candidate|7076|(14, 9, 10)|const|int16
bop_7077 = relay.greater(var_7075.astype('bool'), relay.reshape(const_7076.astype('bool'), relay.shape_of(var_7075))) # shape=(14, 9, 10)
output = relay.Tuple([bop_7077,])
output2 = relay.Tuple([bop_7077,])
func_7081 = relay.Function([var_7075,], output)
mod['func_7081'] = func_7081
mod = relay.transform.InferType()(mod)
mutated_mod['func_7081'] = func_7081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7082 = relay.var("var_7082", dtype = "int16", shape = (14, 9, 10))#candidate|7082|(14, 9, 10)|var|int16
func_7081_call = mutated_mod.get_global_var('func_7081')
call_7083 = func_7081_call(var_7082)
output = call_7083
func_7084 = relay.Function([var_7082], output)
mutated_mod['func_7084'] = func_7084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1307_call = mod.get_global_var('func_1307')
func_1308_call = mutated_mod.get_global_var('func_1308')
call_7097 = relay.TupleGetItem(func_1307_call(), 0)
call_7098 = relay.TupleGetItem(func_1308_call(), 0)
func_5110_call = mod.get_global_var('func_5110')
func_5111_call = mutated_mod.get_global_var('func_5111')
call_7100 = relay.TupleGetItem(func_5110_call(), 1)
call_7101 = relay.TupleGetItem(func_5111_call(), 1)
output = relay.Tuple([call_7097,call_7100,])
output2 = relay.Tuple([call_7098,call_7101,])
func_7109 = relay.Function([], output)
mod['func_7109'] = func_7109
mod = relay.transform.InferType()(mod)
output = func_7109()
func_7110 = relay.Function([], output)
mutated_mod['func_7110'] = func_7110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4270_call = mod.get_global_var('func_4270')
func_4272_call = mutated_mod.get_global_var('func_4272')
call_7137 = relay.TupleGetItem(func_4270_call(), 0)
call_7138 = relay.TupleGetItem(func_4272_call(), 0)
output = relay.Tuple([call_7137,])
output2 = relay.Tuple([call_7138,])
func_7148 = relay.Function([], output)
mod['func_7148'] = func_7148
mod = relay.transform.InferType()(mod)
mutated_mod['func_7148'] = func_7148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7148_call = mutated_mod.get_global_var('func_7148')
call_7149 = func_7148_call()
output = call_7149
func_7150 = relay.Function([], output)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1336_call = mod.get_global_var('func_1336')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_7160 = relay.TupleGetItem(func_1336_call(), 0)
call_7161 = relay.TupleGetItem(func_1338_call(), 0)
output = relay.Tuple([call_7160,])
output2 = relay.Tuple([call_7161,])
func_7167 = relay.Function([], output)
mod['func_7167'] = func_7167
mod = relay.transform.InferType()(mod)
mutated_mod['func_7167'] = func_7167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7167_call = mutated_mod.get_global_var('func_7167')
call_7168 = func_7167_call()
output = call_7168
func_7169 = relay.Function([], output)
mutated_mod['func_7169'] = func_7169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4675_call = mod.get_global_var('func_4675')
func_4677_call = mutated_mod.get_global_var('func_4677')
call_7307 = relay.TupleGetItem(func_4675_call(), 0)
call_7308 = relay.TupleGetItem(func_4677_call(), 0)
output = relay.Tuple([call_7307,])
output2 = relay.Tuple([call_7308,])
func_7310 = relay.Function([], output)
mod['func_7310'] = func_7310
mod = relay.transform.InferType()(mod)
mutated_mod['func_7310'] = func_7310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7310_call = mutated_mod.get_global_var('func_7310')
call_7311 = func_7310_call()
output = call_7311
func_7312 = relay.Function([], output)
mutated_mod['func_7312'] = func_7312
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7333 = relay.var("var_7333", dtype = "int64", shape = (16, 7, 10))#candidate|7333|(16, 7, 10)|var|int64
var_7334 = relay.var("var_7334", dtype = "int64", shape = (16, 7, 10))#candidate|7334|(16, 7, 10)|var|int64
bop_7335 = relay.bitwise_or(var_7333.astype('int64'), relay.reshape(var_7334.astype('int64'), relay.shape_of(var_7333))) # shape=(16, 7, 10)
output = bop_7335
output2 = bop_7335
func_7338 = relay.Function([var_7333,var_7334,], output)
mod['func_7338'] = func_7338
mod = relay.transform.InferType()(mod)
mutated_mod['func_7338'] = func_7338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7338_call = mutated_mod.get_global_var('func_7338')
var_7340 = relay.var("var_7340", dtype = "int64", shape = (16, 7, 10))#candidate|7340|(16, 7, 10)|var|int64
var_7341 = relay.var("var_7341", dtype = "int64", shape = (16, 7, 10))#candidate|7341|(16, 7, 10)|var|int64
call_7339 = func_7338_call(var_7340,var_7341,)
output = call_7339
func_7342 = relay.Function([var_7340,var_7341,], output)
mutated_mod['func_7342'] = func_7342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5240_call = mod.get_global_var('func_5240')
func_5241_call = mutated_mod.get_global_var('func_5241')
call_7422 = relay.TupleGetItem(func_5240_call(), 0)
call_7423 = relay.TupleGetItem(func_5241_call(), 0)
output = call_7422
output2 = call_7423
func_7427 = relay.Function([], output)
mod['func_7427'] = func_7427
mod = relay.transform.InferType()(mod)
mutated_mod['func_7427'] = func_7427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7427_call = mutated_mod.get_global_var('func_7427')
call_7428 = func_7427_call()
output = call_7428
func_7429 = relay.Function([], output)
mutated_mod['func_7429'] = func_7429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3299_call = mod.get_global_var('func_3299')
func_3301_call = mutated_mod.get_global_var('func_3301')
call_7453 = relay.TupleGetItem(func_3299_call(), 0)
call_7454 = relay.TupleGetItem(func_3301_call(), 0)
output = relay.Tuple([call_7453,])
output2 = relay.Tuple([call_7454,])
func_7462 = relay.Function([], output)
mod['func_7462'] = func_7462
mod = relay.transform.InferType()(mod)
mutated_mod['func_7462'] = func_7462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7462_call = mutated_mod.get_global_var('func_7462')
call_7463 = func_7462_call()
output = call_7463
func_7464 = relay.Function([], output)
mutated_mod['func_7464'] = func_7464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4624_call = mod.get_global_var('func_4624')
func_4625_call = mutated_mod.get_global_var('func_4625')
call_7469 = relay.TupleGetItem(func_4624_call(), 1)
call_7470 = relay.TupleGetItem(func_4625_call(), 1)
func_4737_call = mod.get_global_var('func_4737')
func_4739_call = mutated_mod.get_global_var('func_4739')
call_7483 = relay.TupleGetItem(func_4737_call(), 0)
call_7484 = relay.TupleGetItem(func_4739_call(), 0)
output = relay.Tuple([call_7469,call_7483,])
output2 = relay.Tuple([call_7470,call_7484,])
func_7489 = relay.Function([], output)
mod['func_7489'] = func_7489
mod = relay.transform.InferType()(mod)
mutated_mod['func_7489'] = func_7489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7489_call = mutated_mod.get_global_var('func_7489')
call_7490 = func_7489_call()
output = call_7490
func_7491 = relay.Function([], output)
mutated_mod['func_7491'] = func_7491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5583_call = mod.get_global_var('func_5583')
func_5584_call = mutated_mod.get_global_var('func_5584')
call_7509 = func_5583_call()
call_7510 = func_5583_call()
func_506_call = mod.get_global_var('func_506')
func_509_call = mutated_mod.get_global_var('func_509')
var_7516 = relay.var("var_7516", dtype = "float64", shape = (48,))#candidate|7516|(48,)|var|float64
call_7515 = relay.TupleGetItem(func_506_call(relay.reshape(var_7516.astype('float64'), [3, 2, 8]), relay.reshape(var_7516.astype('float64'), [3, 2, 8]), ), 0)
call_7517 = relay.TupleGetItem(func_509_call(relay.reshape(var_7516.astype('float64'), [3, 2, 8]), relay.reshape(var_7516.astype('float64'), [3, 2, 8]), ), 0)
func_3069_call = mod.get_global_var('func_3069')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_7520 = relay.TupleGetItem(func_3069_call(), 1)
call_7521 = relay.TupleGetItem(func_3070_call(), 1)
func_2958_call = mod.get_global_var('func_2958')
func_2959_call = mutated_mod.get_global_var('func_2959')
call_7529 = relay.TupleGetItem(func_2958_call(), 0)
call_7530 = relay.TupleGetItem(func_2959_call(), 0)
output = relay.Tuple([call_7509,call_7515,var_7516,call_7520,call_7529,])
output2 = relay.Tuple([call_7510,call_7517,var_7516,call_7521,call_7530,])
func_7533 = relay.Function([var_7516,], output)
mod['func_7533'] = func_7533
mod = relay.transform.InferType()(mod)
var_7534 = relay.var("var_7534", dtype = "float64", shape = (48,))#candidate|7534|(48,)|var|float64
output = func_7533(var_7534)
func_7535 = relay.Function([var_7534], output)
mutated_mod['func_7535'] = func_7535
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7581 = relay.const([[[6.842626,-9.488838],[0.312219,9.615870],[-1.247217,9.366457],[7.892766,7.106990],[9.018323,8.850871],[2.857841,3.275290],[8.533970,-7.995440]],[[-4.149076,-9.285754],[3.789362,-2.709808],[3.454545,-0.300023],[7.796312,5.022876],[7.243082,-7.752216],[2.930952,-4.394788],[-3.587921,5.745688]],[[-7.033484,0.690101],[-0.157207,-3.713114],[-5.449612,-1.033876],[1.697690,-1.558542],[0.266086,8.176541],[-3.366107,8.451392],[0.406803,-5.293145]],[[4.835330,-4.818018],[-7.021428,-5.635428],[5.435304,-2.081570],[-0.205977,0.329238],[4.372070,-2.063584],[-8.801294,9.076775],[9.861392,-2.336109]],[[-0.763662,-2.447125],[6.332180,5.506570],[8.837948,-0.187880],[4.736537,-7.171632],[8.070033,0.637611],[5.259704,6.911295],[9.745949,7.998907]],[[1.573215,-7.879120],[-0.463272,-2.064944],[7.314753,9.477710],[7.313349,7.202838],[-9.514777,-9.609003],[-1.359536,-0.061673],[2.129921,0.870292]],[[8.261164,-2.703227],[-9.234951,-4.047411],[1.442893,-5.091517],[3.930379,5.118212],[7.210843,4.867551],[2.718715,-9.837450],[6.261794,5.868556]],[[-9.317678,2.121373],[1.214217,4.217736],[-4.936143,3.467107],[-7.515512,-8.285452],[2.592051,-2.356862],[8.920129,0.826444],[-1.470883,-1.180730]],[[-2.741290,-4.952909],[-2.867090,-5.394910],[3.532210,9.280660],[-4.550074,-6.712307],[3.705715,-4.438752],[-5.570127,0.103883],[-0.190821,-0.801539]],[[-4.940881,-5.070298],[7.703292,-1.828171],[-7.175028,9.215465],[-9.147509,-8.612974],[8.888427,1.042395],[0.328846,-3.853722],[-6.836108,7.032481]],[[-0.726230,2.581609],[-5.528088,9.739500],[9.719265,6.790267],[8.209862,8.223413],[-3.614569,-5.248792],[-5.291922,-6.209005],[6.205558,-1.727102]]], dtype = "float64")#candidate|7581|(11, 7, 2)|const|float64
var_7582 = relay.var("var_7582", dtype = "float64", shape = (11, 7, 2))#candidate|7582|(11, 7, 2)|var|float64
bop_7583 = relay.floor_mod(const_7581.astype('float64'), relay.reshape(var_7582.astype('float64'), relay.shape_of(const_7581))) # shape=(11, 7, 2)
uop_7591 = relay.atanh(bop_7583.astype('float32')) # shape=(11, 7, 2)
func_4160_call = mod.get_global_var('func_4160')
func_4162_call = mutated_mod.get_global_var('func_4162')
call_7598 = relay.TupleGetItem(func_4160_call(), 1)
call_7599 = relay.TupleGetItem(func_4162_call(), 1)
var_7600 = relay.var("var_7600", dtype = "float32", shape = (11, 7, 2))#candidate|7600|(11, 7, 2)|var|float32
bop_7601 = relay.logical_xor(uop_7591.astype('int16'), relay.reshape(var_7600.astype('int16'), relay.shape_of(uop_7591))) # shape=(11, 7, 2)
output = relay.Tuple([call_7598,bop_7601,])
output2 = relay.Tuple([call_7599,bop_7601,])
func_7622 = relay.Function([var_7582,var_7600,], output)
mod['func_7622'] = func_7622
mod = relay.transform.InferType()(mod)
mutated_mod['func_7622'] = func_7622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7622_call = mutated_mod.get_global_var('func_7622')
var_7624 = relay.var("var_7624", dtype = "float64", shape = (11, 7, 2))#candidate|7624|(11, 7, 2)|var|float64
var_7625 = relay.var("var_7625", dtype = "float32", shape = (11, 7, 2))#candidate|7625|(11, 7, 2)|var|float32
call_7623 = func_7622_call(var_7624,var_7625,)
output = call_7623
func_7626 = relay.Function([var_7624,var_7625,], output)
mutated_mod['func_7626'] = func_7626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6303_call = mod.get_global_var('func_6303')
func_6305_call = mutated_mod.get_global_var('func_6305')
call_7628 = relay.TupleGetItem(func_6303_call(), 2)
call_7629 = relay.TupleGetItem(func_6305_call(), 2)
output = call_7628
output2 = call_7629
func_7645 = relay.Function([], output)
mod['func_7645'] = func_7645
mod = relay.transform.InferType()(mod)
output = func_7645()
func_7646 = relay.Function([], output)
mutated_mod['func_7646'] = func_7646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_7647 = func_791_call()
call_7648 = func_791_call()
func_5853_call = mod.get_global_var('func_5853')
func_5856_call = mutated_mod.get_global_var('func_5856')
const_7650 = relay.const([-6,2,-6,-6,10,10,7,-5,-5,-9,4,-3,10,-10,-9,-7,-3,8,-9,-8,10,1,6,-8,-10,9,2,-2,2,-5,6,7,-2,-9,-9,8,-7,-5,-4,-5,3,-10,-5,-7,-4,-7,6,-8,-1,9,-5,9,7,6,-8,-10,4,6,-2,-8,7,7,-1,4,-3,4,-2,-10,7,-10,7,-8,10,2,-8,10,-8,-9,-3,3,-5,-4,1,6,9,5,-6,9,-6,9,5,-9,6,2,-10,5,-3,4,2,2,-6,9,1,-9,3,2,7,9,-9,3,9,9,-7,-5,-1,-10,7,8,-7,4,-4,8,-8,-7,9,8,-7,9,8,-1,-5,7,-10,8,3,-9,-8,10,-5,3,-6,1,8,9,6,-8,-3,-2,1,2,4,2,-10,10,-9,1,-5,-1,4,2,10,-2,-4,-5,6,8,-3,-6,3,10,2,-9,6,2,2,10,4,4,-8,-3,-10,-8,3,6,1,-10,-9,-10,1,-5,-5,-6,8,-7,10,-5,-10,3,-7,1,-7,1,-2,-1,2,-7,-2,6,-2,8,-2,4,6,-7,-8,-10,-9,-3,3,-3,9,-4,10,2,-4,6,5,-7,-1,3,5,6,-4,3,2,-2,6,3,7,-10,6,-6,9,-2,-10,-10,8,-8,-5,-10,7,-8,-10,-10,6,10,7,-5,-1,-7,-1,5,2,-4,4,-6,7,-5,6,-6,5,-6,-3,-9,9,-5,-2,2,6,3,-9,3,4,3,-5,-2,-8,-5,9,-3,-7,-1,-1,-4,-8,-8,-5,-2,-1,9,-7,-8,-9,-4,-6,-9,7,3,4,6,-4,10,5,10,-9,2,2,-1,-5,-1,1,-8,-3,-8,-10,-10,7,6,4,-8,5,-8,-1,9,-3,-1,-2,5,-9,2,-7,4,2,8,3,8,-7,8,5,-6,-8,3,5,5,10,1,-10,5,-2,8,8,-7,10,5,-1,-4,-9,10,4,5,-3,-5,-3,4,1,3,6,8,-5,3,-5,6,-5,-7,-2,-7,1,7,-10,9,3,-5,-4,-6,6,-7,-8,5,1,-4,-4,-9,3,-7,9,6,-10,10,4,2,-5,10,-2,-9,-9,-8,-4,-6,-7,1,10,7,-8,3,4,3,2,5,10,-1,-6,2,7,8,2,1,7,-4,-6,-9,2,-2,-5,2,-10,4,1,-8,3,-4,5,9,-3,9,3,2,7,-2,10,8,7,3,-8,-8,-7,8,-8,-8,-3,2,4,-9,-9,-5,-5,6,7,-9,2,-5,-10,5,-1,10,-9,-8,-8,3,-10,-6,-1,6,-6,2,2,9,2,9,4,-7,-4,5,4,1,8,10,4,9,2,-7,1,-6,7,-6,9,-5,6,6,10,5,-9,-9,-10,-10,-2,-7,-1,5,2,-1,3,-5,8,1,1,7,-1,-10,9,-5,6,-1,7,-9,7,4,-7,-9,10,-2,7,2,10,-9,3,7,6,-8,-5,-5,-6,10,-8,8,-10,1,-4,5,5,10,-10,7,6,-10,-2,-3,6,4,6,-3,4,4,-7,9,-5,-1,-7,-10,6,8,-6,8,6,-7,-4,9,-6,-6,-1,6,6,-10,6,10,1,9,8,-3,-9,-5,3,-1,-6,-2,1,-7,-7,-2,9,6,7,-1,-5,7,5,9,9,-6,6,-4], dtype = "uint64")#candidate|7650|(630,)|const|uint64
call_7649 = func_5853_call(relay.reshape(const_7650.astype('uint64'), [14, 5, 9]))
call_7651 = func_5853_call(relay.reshape(const_7650.astype('uint64'), [14, 5, 9]))
func_5110_call = mod.get_global_var('func_5110')
func_5111_call = mutated_mod.get_global_var('func_5111')
call_7652 = relay.TupleGetItem(func_5110_call(), 1)
call_7653 = relay.TupleGetItem(func_5111_call(), 1)
output = relay.Tuple([call_7647,call_7649,const_7650,call_7652,])
output2 = relay.Tuple([call_7648,call_7651,const_7650,call_7653,])
func_7656 = relay.Function([], output)
mod['func_7656'] = func_7656
mod = relay.transform.InferType()(mod)
output = func_7656()
func_7657 = relay.Function([], output)
mutated_mod['func_7657'] = func_7657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4411_call = mod.get_global_var('func_4411')
func_4413_call = mutated_mod.get_global_var('func_4413')
call_7677 = relay.TupleGetItem(func_4411_call(), 2)
call_7678 = relay.TupleGetItem(func_4413_call(), 2)
func_1307_call = mod.get_global_var('func_1307')
func_1308_call = mutated_mod.get_global_var('func_1308')
call_7684 = relay.TupleGetItem(func_1307_call(), 0)
call_7685 = relay.TupleGetItem(func_1308_call(), 0)
output = relay.Tuple([call_7677,call_7684,])
output2 = relay.Tuple([call_7678,call_7685,])
func_7687 = relay.Function([], output)
mod['func_7687'] = func_7687
mod = relay.transform.InferType()(mod)
output = func_7687()
func_7688 = relay.Function([], output)
mutated_mod['func_7688'] = func_7688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5583_call = mod.get_global_var('func_5583')
func_5584_call = mutated_mod.get_global_var('func_5584')
call_7759 = func_5583_call()
call_7760 = func_5583_call()
func_2392_call = mod.get_global_var('func_2392')
func_2396_call = mutated_mod.get_global_var('func_2396')
const_7775 = relay.const([[8,9,-6],[4,-4,-5],[-1,-8,4],[-4,4,9],[-2,-2,7],[-5,3,-8],[-4,-8,1],[-9,-8,-1],[-10,3,10],[-8,3,3],[1,4,1],[2,-8,6],[-6,2,-4],[8,7,10],[1,10,-9],[3,-10,-3],[-3,-10,9],[-10,1,-1],[-6,10,8],[3,-7,7],[-5,-5,9],[9,7,3],[-5,1,7],[-4,-10,-8],[-4,10,-3],[7,-7,-6],[4,-10,-7],[7,6,-10],[9,-5,6],[-7,-6,2],[-6,-9,3],[1,1,8],[-4,9,-4],[-2,3,-2],[-5,-1,-10],[10,4,-10],[7,6,-5],[-7,1,9],[-7,8,2],[-10,1,-8],[8,8,9],[1,-1,3],[1,-7,6],[-8,8,-2],[6,-7,-7],[9,-5,7],[6,10,-5],[5,3,-2],[7,3,-6],[8,-8,8],[-2,-3,5],[-2,10,-2],[7,4,-1],[-10,-4,6],[7,-1,-8],[2,-7,8],[-7,-7,-2],[-1,-6,8],[9,6,10],[-5,-5,-4],[7,-3,-3],[10,-1,6],[-6,2,-1],[-1,-8,-6],[-10,-7,-7],[-6,-1,1],[-9,-5,-6],[6,7,3],[-8,-6,1],[9,3,6],[9,6,-2],[5,6,4],[10,-3,7],[2,-2,4],[-2,-7,-8],[-7,-5,-10],[-10,10,4],[9,3,-8],[-9,6,1],[-7,4,8],[-6,-3,-7],[-10,8,2],[-4,-6,4],[7,-6,-7],[6,10,7],[-2,-4,-8],[7,-8,7],[-7,-3,-10],[-8,-2,-4],[1,-10,-10],[10,4,6],[-5,-7,8],[-4,-7,-9],[-6,5,-1],[-5,-9,-5],[6,10,7],[9,10,6],[-1,4,-9],[-6,8,-3],[10,-1,-6],[7,-2,-1],[2,-3,-7],[-2,-9,-8],[-7,-5,8],[6,-9,9],[5,-7,-3],[-10,-10,7],[3,-8,6],[-3,2,10],[8,-2,-4],[2,6,-8],[10,6,-2],[7,-2,8],[-1,-1,-8],[7,-10,1],[-9,-5,4],[6,3,6],[-6,-1,-10],[-6,-1,-7],[1,-3,2],[-5,10,-8],[5,-10,7],[-6,-1,-1],[7,3,6],[4,-2,6],[-4,-5,-1],[1,-8,-4],[9,7,-6],[-2,-6,8],[-4,9,1],[2,-6,-2],[-1,-5,-3],[5,9,-3],[-10,8,1],[10,-10,3],[-6,-9,-3],[1,3,4],[-5,2,-9],[-8,2,-9],[-4,8,9],[5,8,8],[-6,-5,5],[9,-6,-3],[-5,-6,-7],[-8,3,4],[9,7,-5],[9,6,-4],[-3,10,-1],[-8,3,3],[-10,-10,-9],[7,6,-5],[9,-6,-10],[-5,-3,-4],[-5,3,8],[-10,7,1],[6,5,-2],[-5,-6,5],[1,-1,-4],[-9,9,8],[5,4,-8],[9,-3,-6],[-7,-5,1],[-1,1,-5],[8,5,-3],[5,-3,-2],[-5,6,5],[2,-4,7],[6,-8,-9],[-3,8,-4],[-3,10,7],[-8,5,10],[-8,4,-9],[9,-6,-2],[9,-1,3],[7,4,3],[-1,6,7],[-6,10,8],[10,3,-2],[2,-2,10],[10,-5,-7],[10,1,4],[3,2,-9],[-1,6,4],[2,-1,10],[-4,-1,5],[-7,-5,-2],[-6,-8,-10],[-1,-5,-6],[-6,4,-7],[-1,5,9],[-7,6,5],[-1,-2,-1],[8,-5,8],[-2,2,-2],[-2,-9,4]], dtype = "uint64")#candidate|7775|(195, 3)|const|uint64
var_7776 = relay.var("var_7776", dtype = "float32", shape = (63,))#candidate|7776|(63,)|var|float32
call_7774 = relay.TupleGetItem(func_2392_call(relay.reshape(const_7775.astype('uint64'), [13, 5, 9]), relay.reshape(var_7776.astype('float32'), [1, 63]), ), 3)
call_7777 = relay.TupleGetItem(func_2396_call(relay.reshape(const_7775.astype('uint64'), [13, 5, 9]), relay.reshape(var_7776.astype('float32'), [1, 63]), ), 3)
uop_7792 = relay.tan(const_7775.astype('float64')) # shape=(195, 3)
uop_7796 = relay.asin(uop_7792.astype('float64')) # shape=(195, 3)
uop_7799 = relay.acos(uop_7792.astype('float64')) # shape=(195, 3)
uop_7801 = relay.sin(uop_7799.astype('float32')) # shape=(195, 3)
bop_7806 = relay.equal(uop_7799.astype('bool'), relay.reshape(uop_7796.astype('bool'), relay.shape_of(uop_7799))) # shape=(195, 3)
func_5240_call = mod.get_global_var('func_5240')
func_5241_call = mutated_mod.get_global_var('func_5241')
call_7812 = relay.TupleGetItem(func_5240_call(), 0)
call_7813 = relay.TupleGetItem(func_5241_call(), 0)
uop_7818 = relay.log(uop_7801.astype('float64')) # shape=(195, 3)
func_3398_call = mod.get_global_var('func_3398')
func_3400_call = mutated_mod.get_global_var('func_3400')
call_7828 = relay.TupleGetItem(func_3398_call(), 1)
call_7829 = relay.TupleGetItem(func_3400_call(), 1)
var_7831 = relay.var("var_7831", dtype = "float32", shape = (195, 3))#candidate|7831|(195, 3)|var|float32
bop_7832 = relay.mod(uop_7801.astype('float64'), relay.reshape(var_7831.astype('float64'), relay.shape_of(uop_7801))) # shape=(195, 3)
bop_7847 = relay.bitwise_or(bop_7832.astype('int8'), relay.reshape(const_7775.astype('int8'), relay.shape_of(bop_7832))) # shape=(195, 3)
output = relay.Tuple([call_7759,call_7774,var_7776,bop_7806,call_7812,uop_7818,call_7828,bop_7847,])
output2 = relay.Tuple([call_7760,call_7777,var_7776,bop_7806,call_7813,uop_7818,call_7829,bop_7847,])
func_7855 = relay.Function([var_7776,var_7831,], output)
mod['func_7855'] = func_7855
mod = relay.transform.InferType()(mod)
var_7856 = relay.var("var_7856", dtype = "float32", shape = (63,))#candidate|7856|(63,)|var|float32
var_7857 = relay.var("var_7857", dtype = "float32", shape = (195, 3))#candidate|7857|(195, 3)|var|float32
output = func_7855(var_7856,var_7857,)
func_7858 = relay.Function([var_7856,var_7857,], output)
mutated_mod['func_7858'] = func_7858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5583_call = mod.get_global_var('func_5583')
func_5584_call = mutated_mod.get_global_var('func_5584')
call_7865 = func_5583_call()
call_7866 = func_5583_call()
output = call_7865
output2 = call_7866
func_7882 = relay.Function([], output)
mod['func_7882'] = func_7882
mod = relay.transform.InferType()(mod)
mutated_mod['func_7882'] = func_7882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7882_call = mutated_mod.get_global_var('func_7882')
call_7883 = func_7882_call()
output = call_7883
func_7884 = relay.Function([], output)
mutated_mod['func_7884'] = func_7884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3247_call = mod.get_global_var('func_3247')
func_3248_call = mutated_mod.get_global_var('func_3248')
call_7888 = relay.TupleGetItem(func_3247_call(), 0)
call_7889 = relay.TupleGetItem(func_3248_call(), 0)
output = call_7888
output2 = call_7889
func_7890 = relay.Function([], output)
mod['func_7890'] = func_7890
mod = relay.transform.InferType()(mod)
output = func_7890()
func_7891 = relay.Function([], output)
mutated_mod['func_7891'] = func_7891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5597_call = mod.get_global_var('func_5597')
func_5599_call = mutated_mod.get_global_var('func_5599')
call_7923 = relay.TupleGetItem(func_5597_call(), 0)
call_7924 = relay.TupleGetItem(func_5599_call(), 0)
func_689_call = mod.get_global_var('func_689')
func_692_call = mutated_mod.get_global_var('func_692')
const_7946 = relay.const(-9, dtype = "int32")#candidate|7946|()|const|int32
var_7947 = relay.var("var_7947", dtype = "int32", shape = (70,))#candidate|7947|(70,)|var|int32
call_7945 = relay.TupleGetItem(func_689_call(relay.reshape(const_7946.astype('int32'), []), relay.reshape(var_7947.astype('int32'), [7, 1, 10]), ), 0)
call_7948 = relay.TupleGetItem(func_692_call(relay.reshape(const_7946.astype('int32'), []), relay.reshape(var_7947.astype('int32'), [7, 1, 10]), ), 0)
func_4850_call = mod.get_global_var('func_4850')
func_4852_call = mutated_mod.get_global_var('func_4852')
var_7956 = relay.var("var_7956", dtype = "float32", shape = (6, 84))#candidate|7956|(6, 84)|var|float32
call_7955 = relay.TupleGetItem(func_4850_call(relay.reshape(var_7956.astype('float32'), [12, 3, 14])), 1)
call_7957 = relay.TupleGetItem(func_4852_call(relay.reshape(var_7956.astype('float32'), [12, 3, 14])), 1)
func_7489_call = mod.get_global_var('func_7489')
func_7491_call = mutated_mod.get_global_var('func_7491')
call_7964 = relay.TupleGetItem(func_7489_call(), 1)
call_7965 = relay.TupleGetItem(func_7491_call(), 1)
func_4624_call = mod.get_global_var('func_4624')
func_4625_call = mutated_mod.get_global_var('func_4625')
call_7970 = relay.TupleGetItem(func_4624_call(), 1)
call_7971 = relay.TupleGetItem(func_4625_call(), 1)
output = relay.Tuple([call_7923,call_7945,const_7946,var_7947,call_7955,var_7956,call_7964,call_7970,])
output2 = relay.Tuple([call_7924,call_7948,const_7946,var_7947,call_7957,var_7956,call_7965,call_7971,])
func_7981 = relay.Function([var_7947,var_7956,], output)
mod['func_7981'] = func_7981
mod = relay.transform.InferType()(mod)
var_7982 = relay.var("var_7982", dtype = "int32", shape = (70,))#candidate|7982|(70,)|var|int32
var_7983 = relay.var("var_7983", dtype = "float32", shape = (6, 84))#candidate|7983|(6, 84)|var|float32
output = func_7981(var_7982,var_7983,)
func_7984 = relay.Function([var_7982,var_7983,], output)
mutated_mod['func_7984'] = func_7984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7687_call = mod.get_global_var('func_7687')
func_7688_call = mutated_mod.get_global_var('func_7688')
call_8069 = relay.TupleGetItem(func_7687_call(), 0)
call_8070 = relay.TupleGetItem(func_7688_call(), 0)
output = call_8069
output2 = call_8070
func_8081 = relay.Function([], output)
mod['func_8081'] = func_8081
mod = relay.transform.InferType()(mod)
mutated_mod['func_8081'] = func_8081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8081_call = mutated_mod.get_global_var('func_8081')
call_8082 = func_8081_call()
output = call_8082
func_8083 = relay.Function([], output)
mutated_mod['func_8083'] = func_8083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7687_call = mod.get_global_var('func_7687')
func_7688_call = mutated_mod.get_global_var('func_7688')
call_8095 = relay.TupleGetItem(func_7687_call(), 1)
call_8096 = relay.TupleGetItem(func_7688_call(), 1)
func_3398_call = mod.get_global_var('func_3398')
func_3400_call = mutated_mod.get_global_var('func_3400')
call_8099 = relay.TupleGetItem(func_3398_call(), 1)
call_8100 = relay.TupleGetItem(func_3400_call(), 1)
output = relay.Tuple([call_8095,call_8099,])
output2 = relay.Tuple([call_8096,call_8100,])
func_8103 = relay.Function([], output)
mod['func_8103'] = func_8103
mod = relay.transform.InferType()(mod)
mutated_mod['func_8103'] = func_8103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8103_call = mutated_mod.get_global_var('func_8103')
call_8104 = func_8103_call()
output = call_8104
func_8105 = relay.Function([], output)
mutated_mod['func_8105'] = func_8105
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8164 = relay.var("var_8164", dtype = "float32", shape = (15, 16, 8))#candidate|8164|(15, 16, 8)|var|float32
var_8165 = relay.var("var_8165", dtype = "float32", shape = (15, 16, 8))#candidate|8165|(15, 16, 8)|var|float32
bop_8166 = relay.divide(var_8164.astype('float32'), relay.reshape(var_8165.astype('float32'), relay.shape_of(var_8164))) # shape=(15, 16, 8)
func_6303_call = mod.get_global_var('func_6303')
func_6305_call = mutated_mod.get_global_var('func_6305')
call_8179 = relay.TupleGetItem(func_6303_call(), 2)
call_8180 = relay.TupleGetItem(func_6305_call(), 2)
output = relay.Tuple([bop_8166,call_8179,])
output2 = relay.Tuple([bop_8166,call_8180,])
func_8190 = relay.Function([var_8164,var_8165,], output)
mod['func_8190'] = func_8190
mod = relay.transform.InferType()(mod)
mutated_mod['func_8190'] = func_8190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8190_call = mutated_mod.get_global_var('func_8190')
var_8192 = relay.var("var_8192", dtype = "float32", shape = (15, 16, 8))#candidate|8192|(15, 16, 8)|var|float32
var_8193 = relay.var("var_8193", dtype = "float32", shape = (15, 16, 8))#candidate|8193|(15, 16, 8)|var|float32
call_8191 = func_8190_call(var_8192,var_8193,)
output = call_8191
func_8194 = relay.Function([var_8192,var_8193,], output)
mutated_mod['func_8194'] = func_8194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3155_call = mod.get_global_var('func_3155')
func_3156_call = mutated_mod.get_global_var('func_3156')
call_8217 = func_3155_call()
call_8218 = func_3155_call()
var_8234 = relay.var("var_8234", dtype = "uint64", shape = (2, 5, 9))#candidate|8234|(2, 5, 9)|var|uint64
bop_8235 = relay.greater(call_8217.astype('bool'), var_8234.astype('bool')) # shape=(2, 5, 9)
bop_8238 = relay.greater(call_8218.astype('bool'), var_8234.astype('bool')) # shape=(2, 5, 9)
func_1024_call = mod.get_global_var('func_1024')
func_1026_call = mutated_mod.get_global_var('func_1026')
call_8249 = relay.TupleGetItem(func_1024_call(), 0)
call_8250 = relay.TupleGetItem(func_1026_call(), 0)
func_7067_call = mod.get_global_var('func_7067')
func_7069_call = mutated_mod.get_global_var('func_7069')
call_8251 = relay.TupleGetItem(func_7067_call(), 0)
call_8252 = relay.TupleGetItem(func_7069_call(), 0)
output = relay.Tuple([bop_8235,call_8249,call_8251,])
output2 = relay.Tuple([bop_8238,call_8250,call_8252,])
func_8255 = relay.Function([var_8234,], output)
mod['func_8255'] = func_8255
mod = relay.transform.InferType()(mod)
var_8256 = relay.var("var_8256", dtype = "uint64", shape = (2, 5, 9))#candidate|8256|(2, 5, 9)|var|uint64
output = func_8255(var_8256)
func_8257 = relay.Function([var_8256], output)
mutated_mod['func_8257'] = func_8257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3398_call = mod.get_global_var('func_3398')
func_3400_call = mutated_mod.get_global_var('func_3400')
call_8268 = relay.TupleGetItem(func_3398_call(), 0)
call_8269 = relay.TupleGetItem(func_3400_call(), 0)
output = relay.Tuple([call_8268,])
output2 = relay.Tuple([call_8269,])
func_8285 = relay.Function([], output)
mod['func_8285'] = func_8285
mod = relay.transform.InferType()(mod)
mutated_mod['func_8285'] = func_8285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8285_call = mutated_mod.get_global_var('func_8285')
call_8286 = func_8285_call()
output = call_8286
func_8287 = relay.Function([], output)
mutated_mod['func_8287'] = func_8287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5144_call = mod.get_global_var('func_5144')
func_5146_call = mutated_mod.get_global_var('func_5146')
call_8305 = func_5144_call()
call_8306 = func_5144_call()
func_4675_call = mod.get_global_var('func_4675')
func_4677_call = mutated_mod.get_global_var('func_4677')
call_8340 = relay.TupleGetItem(func_4675_call(), 0)
call_8341 = relay.TupleGetItem(func_4677_call(), 0)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_8345 = func_791_call()
call_8346 = func_791_call()
output = relay.Tuple([call_8305,call_8340,call_8345,])
output2 = relay.Tuple([call_8306,call_8341,call_8346,])
func_8349 = relay.Function([], output)
mod['func_8349'] = func_8349
mod = relay.transform.InferType()(mod)
mutated_mod['func_8349'] = func_8349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8349_call = mutated_mod.get_global_var('func_8349')
call_8350 = func_8349_call()
output = call_8350
func_8351 = relay.Function([], output)
mutated_mod['func_8351'] = func_8351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3942_call = mod.get_global_var('func_3942')
func_3943_call = mutated_mod.get_global_var('func_3943')
call_8357 = relay.TupleGetItem(func_3942_call(), 0)
call_8358 = relay.TupleGetItem(func_3943_call(), 0)
output = relay.Tuple([call_8357,])
output2 = relay.Tuple([call_8358,])
func_8374 = relay.Function([], output)
mod['func_8374'] = func_8374
mod = relay.transform.InferType()(mod)
mutated_mod['func_8374'] = func_8374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8374_call = mutated_mod.get_global_var('func_8374')
call_8375 = func_8374_call()
output = call_8375
func_8376 = relay.Function([], output)
mutated_mod['func_8376'] = func_8376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5231_call = mod.get_global_var('func_5231')
func_5232_call = mutated_mod.get_global_var('func_5232')
call_8545 = func_5231_call()
call_8546 = func_5231_call()
func_6732_call = mod.get_global_var('func_6732')
func_6734_call = mutated_mod.get_global_var('func_6734')
call_8555 = relay.TupleGetItem(func_6732_call(), 0)
call_8556 = relay.TupleGetItem(func_6734_call(), 0)
func_7081_call = mod.get_global_var('func_7081')
func_7084_call = mutated_mod.get_global_var('func_7084')
var_8574 = relay.var("var_8574", dtype = "int16", shape = (1260,))#candidate|8574|(1260,)|var|int16
call_8573 = relay.TupleGetItem(func_7081_call(relay.reshape(var_8574.astype('int16'), [14, 9, 10])), 0)
call_8575 = relay.TupleGetItem(func_7084_call(relay.reshape(var_8574.astype('int16'), [14, 9, 10])), 0)
output = relay.Tuple([call_8545,call_8555,call_8573,var_8574,])
output2 = relay.Tuple([call_8546,call_8556,call_8575,var_8574,])
func_8577 = relay.Function([var_8574,], output)
mod['func_8577'] = func_8577
mod = relay.transform.InferType()(mod)
var_8578 = relay.var("var_8578", dtype = "int16", shape = (1260,))#candidate|8578|(1260,)|var|int16
output = func_8577(var_8578)
func_8579 = relay.Function([var_8578], output)
mutated_mod['func_8579'] = func_8579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7890_call = mod.get_global_var('func_7890')
func_7891_call = mutated_mod.get_global_var('func_7891')
call_8592 = func_7890_call()
call_8593 = func_7890_call()
func_1706_call = mod.get_global_var('func_1706')
func_1708_call = mutated_mod.get_global_var('func_1708')
const_8598 = relay.const([-9.202942,0.686116,2.019520,-2.911509,-7.361717,-0.706323,-5.007509,-6.018270,-9.892606,-9.319567,-6.108152,8.430243,-7.534515,-1.042574,-4.823506,5.886453,-6.028437,6.811724,7.584328,-6.914865,8.964753,0.912922,4.449159,-3.446202,-7.098500,0.898321,6.668655,9.993202,5.784042,-9.259292,-5.271299,-4.701726,-6.486346,-2.660896,2.609200,-4.428059,-9.414969,4.854279,2.621910,4.513968,-2.021856,-4.851603,-1.817581,3.915082,-4.546701,3.614775,9.609841,0.435373,6.100527,5.275746,-3.815026,1.165680,-2.215888,-9.287217,-5.599494,3.369594,-5.505491,6.451533,2.378730,-8.830845,-3.472707,-0.717155,-9.290186,8.754268,-7.227242,-3.840232,-4.940791,8.613211,-2.365017,5.107040,6.197651,3.931994,-8.800826,-7.511642,-3.194934,7.892817,-6.577552,-0.365422,1.894268,-3.283026,9.549445,0.138057,1.153930,-8.106942,-8.041730,-6.670890,-3.469488,-0.197707,-8.074571,7.345245,9.242654,0.546354,-8.693749,-2.307429,-9.695215,0.691246,-7.250970,6.404085,6.184436,1.139244,9.861706,-3.173720,-7.312126,5.516116,4.109544,1.734076,9.244612,6.457840,-6.638070,-9.521955,-2.607289,-4.301191,-7.726910,-2.920959,4.050333,3.745061,-2.905426,1.945757,-7.662813,7.386748,5.344427,9.246915,-4.350265,-8.648633,-4.132014,6.410720,4.237885,8.406265,0.193952,1.149461,-2.777469,-3.533775,-6.867906,6.484678,-3.458906,0.469121,3.481331,-1.942203,5.010114,-5.657855,0.901546,-0.834126,-1.345919,-4.816868,-8.877050,-3.446831,4.603317,8.469593,-1.192452,-4.964251,4.848869,-6.165681,-2.370883,-1.721209,-6.739041,-6.014879,-7.459263,-9.972499,-8.094765,7.646527,-1.931426,4.384681,-3.800137,-6.625743,2.129005,1.273715,-6.076696,9.730119,-7.581627,-9.420413,9.221680,6.978840,0.591629,-4.830039,-2.088991,-0.512412,6.917052,-7.367413,-0.768575,5.219072,-4.271936,9.334694,-5.746564,7.988107,-6.522349,2.547594,-7.625329,-6.048853,-6.464463,-2.300027,-1.012397,-9.878985,-6.900826,1.026958,8.873141,1.175158,7.659975,-2.275966,4.642387,-2.288547,8.583376,9.583868,-8.595231,7.709379,-8.128766,-5.097355,4.274365,8.736751,1.468988,-6.366181,7.033290,-7.293745,-8.312598,-1.875720,7.578875,-8.158163,2.588399,-8.873017,0.497523,-6.152664,8.728450,-7.032968,6.169558,6.323265,-6.865224,4.207158,3.561960,-6.283562,-6.859471,7.701986,1.632506,-7.108095,-7.313681,2.225937,2.178690,2.405624,-9.009808,8.697758,4.899909,-9.921618,-4.103960,7.834242,-8.474016,-0.822235,0.140983,-8.113659,1.235897,2.296723,2.652725,7.349152,-3.762941,-3.213692,-4.502536,9.669233,-1.536052,1.542003,1.487063,-3.442853,-2.724222,7.526030,-1.816849,-8.449639,-8.126856,2.307088,-8.034235,-0.048265,-1.896527,2.403172,-6.706540,-9.582023,9.824913,-4.344214,3.439146,-9.886963,4.078638,0.136917,9.620265,4.242933,7.084603,5.025055,5.102475,-0.044715,-3.023218,-0.475841,-7.726615,5.891579,-6.621534,5.191713], dtype = "float32")#candidate|8598|(288,)|const|float32
call_8597 = relay.TupleGetItem(func_1706_call(relay.reshape(const_8598.astype('float32'), [3, 12, 8])), 0)
call_8599 = relay.TupleGetItem(func_1708_call(relay.reshape(const_8598.astype('float32'), [3, 12, 8])), 0)
func_935_call = mod.get_global_var('func_935')
func_937_call = mutated_mod.get_global_var('func_937')
call_8603 = relay.TupleGetItem(func_935_call(), 0)
call_8604 = relay.TupleGetItem(func_937_call(), 0)
func_7687_call = mod.get_global_var('func_7687')
func_7688_call = mutated_mod.get_global_var('func_7688')
call_8605 = relay.TupleGetItem(func_7687_call(), 0)
call_8606 = relay.TupleGetItem(func_7688_call(), 0)
output = relay.Tuple([call_8592,call_8597,const_8598,call_8603,call_8605,])
output2 = relay.Tuple([call_8593,call_8599,const_8598,call_8604,call_8606,])
func_8633 = relay.Function([], output)
mod['func_8633'] = func_8633
mod = relay.transform.InferType()(mod)
output = func_8633()
func_8634 = relay.Function([], output)
mutated_mod['func_8634'] = func_8634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5135_call = mod.get_global_var('func_5135')
func_5137_call = mutated_mod.get_global_var('func_5137')
call_8764 = relay.TupleGetItem(func_5135_call(), 0)
call_8765 = relay.TupleGetItem(func_5137_call(), 0)
func_454_call = mod.get_global_var('func_454')
func_456_call = mutated_mod.get_global_var('func_456')
call_8769 = relay.TupleGetItem(func_454_call(), 0)
call_8770 = relay.TupleGetItem(func_456_call(), 0)
func_1594_call = mod.get_global_var('func_1594')
func_1597_call = mutated_mod.get_global_var('func_1597')
const_8776 = relay.const([3.469228,0.315036,5.500177,1.648339,7.809512,0.150052,6.038174,9.794817,1.359018,1.037393,-4.948124,3.986775,7.737796,2.218625,9.503774,-6.921350,-9.554004,-4.783171,7.504622,8.651833,7.522223,2.962174,0.383896,-7.269472,-6.987641,4.399442,-7.769254,7.035912,-8.978293,0.167946,2.907401,0.764700,9.194170,4.426700,5.923467,7.263578,-8.214764,-5.047552,8.099956,-1.028879,-1.266070,-0.004515,-2.849961,-7.171784,6.976311,6.053246,4.693686,-5.210317,-9.761825,0.991089,-5.604133,-5.266628,1.807122,-7.150381,0.445182,-3.422225,4.477223,9.689339,7.101668,-1.806388,5.666796,1.144811,-7.280301], dtype = "float32")#candidate|8776|(63,)|const|float32
call_8775 = relay.TupleGetItem(func_1594_call(relay.reshape(const_8776.astype('float32'), [7, 3, 3])), 1)
call_8777 = relay.TupleGetItem(func_1597_call(relay.reshape(const_8776.astype('float32'), [7, 3, 3])), 1)
func_7855_call = mod.get_global_var('func_7855')
func_7858_call = mutated_mod.get_global_var('func_7858')
var_8796 = relay.var("var_8796", dtype = "float32", shape = (585,))#candidate|8796|(585,)|var|float32
call_8795 = relay.TupleGetItem(func_7855_call(relay.reshape(const_8776.astype('float32'), [63,]), relay.reshape(var_8796.astype('float32'), [195, 3]), ), 3)
call_8797 = relay.TupleGetItem(func_7858_call(relay.reshape(const_8776.astype('float32'), [63,]), relay.reshape(var_8796.astype('float32'), [195, 3]), ), 3)
output = relay.Tuple([call_8764,call_8769,call_8775,const_8776,call_8795,var_8796,])
output2 = relay.Tuple([call_8765,call_8770,call_8777,const_8776,call_8797,var_8796,])
func_8806 = relay.Function([var_8796,], output)
mod['func_8806'] = func_8806
mod = relay.transform.InferType()(mod)
mutated_mod['func_8806'] = func_8806
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8807 = relay.var("var_8807", dtype = "float32", shape = (585,))#candidate|8807|(585,)|var|float32
func_8806_call = mutated_mod.get_global_var('func_8806')
call_8808 = func_8806_call(var_8807)
output = call_8808
func_8809 = relay.Function([var_8807], output)
mutated_mod['func_8809'] = func_8809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7109_call = mod.get_global_var('func_7109')
func_7110_call = mutated_mod.get_global_var('func_7110')
call_8887 = relay.TupleGetItem(func_7109_call(), 0)
call_8888 = relay.TupleGetItem(func_7110_call(), 0)
output = call_8887
output2 = call_8888
func_8898 = relay.Function([], output)
mod['func_8898'] = func_8898
mod = relay.transform.InferType()(mod)
output = func_8898()
func_8899 = relay.Function([], output)
mutated_mod['func_8899'] = func_8899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8285_call = mod.get_global_var('func_8285')
func_8287_call = mutated_mod.get_global_var('func_8287')
call_8912 = relay.TupleGetItem(func_8285_call(), 0)
call_8913 = relay.TupleGetItem(func_8287_call(), 0)
func_5461_call = mod.get_global_var('func_5461')
func_5462_call = mutated_mod.get_global_var('func_5462')
call_8922 = relay.TupleGetItem(func_5461_call(), 0)
call_8923 = relay.TupleGetItem(func_5462_call(), 0)
func_6224_call = mod.get_global_var('func_6224')
func_6226_call = mutated_mod.get_global_var('func_6226')
call_8953 = relay.TupleGetItem(func_6224_call(), 0)
call_8954 = relay.TupleGetItem(func_6226_call(), 0)
bop_8955 = relay.add(call_8912.astype('float32'), relay.reshape(call_8922.astype('float32'), relay.shape_of(call_8912))) # shape=(1, 5, 9)
bop_8958 = relay.add(call_8913.astype('float32'), relay.reshape(call_8923.astype('float32'), relay.shape_of(call_8913))) # shape=(1, 5, 9)
output = relay.Tuple([call_8953,bop_8955,])
output2 = relay.Tuple([call_8954,bop_8958,])
func_8970 = relay.Function([], output)
mod['func_8970'] = func_8970
mod = relay.transform.InferType()(mod)
output = func_8970()
func_8971 = relay.Function([], output)
mutated_mod['func_8971'] = func_8971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3247_call = mod.get_global_var('func_3247')
func_3248_call = mutated_mod.get_global_var('func_3248')
call_9145 = relay.TupleGetItem(func_3247_call(), 0)
call_9146 = relay.TupleGetItem(func_3248_call(), 0)
output = call_9145
output2 = call_9146
func_9188 = relay.Function([], output)
mod['func_9188'] = func_9188
mod = relay.transform.InferType()(mod)
output = func_9188()
func_9189 = relay.Function([], output)
mutated_mod['func_9189'] = func_9189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5583_call = mod.get_global_var('func_5583')
func_5584_call = mutated_mod.get_global_var('func_5584')
call_9193 = func_5583_call()
call_9194 = func_5583_call()
output = call_9193
output2 = call_9194
func_9202 = relay.Function([], output)
mod['func_9202'] = func_9202
mod = relay.transform.InferType()(mod)
mutated_mod['func_9202'] = func_9202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9202_call = mutated_mod.get_global_var('func_9202')
call_9203 = func_9202_call()
output = call_9203
func_9204 = relay.Function([], output)
mutated_mod['func_9204'] = func_9204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2290_call = mod.get_global_var('func_2290')
func_2291_call = mutated_mod.get_global_var('func_2291')
call_9205 = func_2290_call()
call_9206 = func_2290_call()
var_9218 = relay.var("var_9218", dtype = "uint64", shape = (11, 5, 9))#candidate|9218|(11, 5, 9)|var|uint64
bop_9219 = relay.divide(call_9205.astype('float32'), var_9218.astype('float32')) # shape=(11, 5, 9)
bop_9222 = relay.divide(call_9206.astype('float32'), var_9218.astype('float32')) # shape=(11, 5, 9)
output = bop_9219
output2 = bop_9222
func_9227 = relay.Function([var_9218,], output)
mod['func_9227'] = func_9227
mod = relay.transform.InferType()(mod)
mutated_mod['func_9227'] = func_9227
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9228 = relay.var("var_9228", dtype = "uint64", shape = (11, 5, 9))#candidate|9228|(11, 5, 9)|var|uint64
func_9227_call = mutated_mod.get_global_var('func_9227')
call_9229 = func_9227_call(var_9228)
output = call_9229
func_9230 = relay.Function([var_9228], output)
mutated_mod['func_9230'] = func_9230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5110_call = mod.get_global_var('func_5110')
func_5111_call = mutated_mod.get_global_var('func_5111')
call_9265 = relay.TupleGetItem(func_5110_call(), 1)
call_9266 = relay.TupleGetItem(func_5111_call(), 1)
uop_9281 = relay.tan(call_9265.astype('float32')) # shape=(1, 5, 9)
uop_9283 = relay.tan(call_9266.astype('float32')) # shape=(1, 5, 9)
const_9288 = relay.const([[[-6.286043,-2.385548,-5.203707,5.008685,8.599157,-4.165676,1.710229,-3.435803,-8.539883],[9.284848,3.349407,4.828668,-6.884207,0.872345,-8.673968,1.748324,-0.456789,5.884581],[-0.446494,0.734324,-2.043967,-9.992289,8.292518,2.324258,1.427262,-3.232493,-3.660613],[2.920324,-2.210880,5.818295,0.945541,-8.010037,7.687320,-6.448510,-7.027762,7.268703],[-5.105158,-3.616448,4.666084,7.459753,-0.358228,5.503611,1.510680,-0.527434,7.357742]],[[0.710059,-9.204657,-6.686284,0.959008,1.417007,-7.717041,-8.527756,-6.027316,-4.184391],[5.989946,-6.428997,1.788929,-1.409979,3.824527,1.965796,-4.098325,6.747320,-6.804143],[-9.187769,2.662707,9.598118,3.700433,-0.815035,-3.990732,8.931150,-2.031804,-1.445469],[9.902402,7.422740,8.532869,-9.792197,0.804308,-2.355448,3.427454,8.720663,-2.197245],[7.251962,-8.948860,5.512498,-1.566084,-4.863940,8.915425,6.557892,5.293541,9.072496]],[[4.159851,9.490974,1.931487,-3.028849,-5.211660,4.041677,-0.491123,-6.249754,-8.055251],[4.766061,-5.749033,-8.076063,-3.069331,9.260761,-4.136573,-1.181766,-7.002277,-3.173130],[8.375847,-9.434804,-4.379075,-3.700782,-5.388449,6.388645,5.537667,-7.082610,2.202813],[6.207291,-5.344643,4.182279,6.634537,-7.024382,5.227051,5.973595,2.056336,2.651063],[-9.373658,-4.326434,-0.930362,1.197692,-5.930446,-8.524581,-4.363035,-0.009401,-3.084504]],[[6.708127,9.581461,3.388684,-1.020718,-6.180723,-0.944064,1.122934,0.309147,-8.283489],[-7.585999,2.818445,7.846645,-9.355940,2.574664,-4.448043,-6.910990,2.050604,2.730777],[8.769934,-7.147593,8.721744,4.759861,3.997845,-3.070104,-7.075285,9.624079,5.885214],[5.421853,6.273857,-7.735725,-2.486232,4.946669,6.213050,-9.840525,6.163351,-3.173837],[-5.319964,1.652520,-2.355289,1.211408,-5.365866,7.052125,9.484764,4.836837,2.384735]],[[-8.039938,0.562276,-5.717864,-0.281197,2.937353,3.311131,-6.518739,1.108580,9.389636],[4.297806,-4.699527,1.369701,9.464424,4.865405,5.974188,9.191853,-7.367706,-1.577084],[4.563835,-8.238162,-4.861235,-0.979194,4.918332,-0.062290,1.809333,9.014040,-6.148470],[1.442198,1.719822,-9.502948,-5.725370,-7.010700,-1.286782,5.531088,7.693794,-5.332807],[6.233192,-7.292493,-1.772414,0.533947,-2.222142,-3.438507,7.621447,-0.338668,-0.084213]],[[-2.967572,-8.835416,0.261360,3.970573,-7.926432,-1.527356,-0.698849,8.406842,-0.401625],[1.977827,-8.849984,-4.892525,-9.255958,-5.093856,-6.213656,-3.111314,6.528671,0.124550],[9.134406,0.293005,4.526402,3.304105,3.702926,-4.216154,-8.427360,5.731589,1.136591],[4.111472,-3.860267,9.246163,-4.543039,1.949617,-5.740502,4.115221,4.058981,-6.308396],[-3.994115,-8.309138,-2.575480,-1.358635,-6.764889,1.014006,4.700562,-6.754301,0.749874]],[[1.875756,8.487515,8.557085,8.995003,6.671901,-8.633237,-4.820295,2.486109,-0.624298],[5.962185,7.412949,2.606244,-5.286127,0.976888,-9.123990,-4.176701,2.439092,-8.664219],[2.483552,7.792653,-4.981638,-4.931866,-2.239207,3.003394,-0.299287,2.451857,-5.389498],[-1.756484,-7.802222,7.198847,-0.764064,-2.640935,9.972342,2.958926,-3.312887,-8.106122],[-4.208988,8.667556,-1.657768,9.973917,-1.172593,-2.851873,3.219522,8.001419,7.658182]],[[-7.248254,-8.132239,5.229658,5.513230,-6.064903,3.611611,-2.173449,-5.864406,-2.648987],[-8.311160,5.863691,9.114223,-8.009554,-0.862856,-9.177547,-7.668043,-8.883065,3.295313],[6.758349,-6.626086,-7.014792,-7.797456,6.078838,0.247643,2.657457,6.236232,-2.526438],[9.015402,-4.717503,-5.677999,0.525193,0.277908,9.609087,4.035811,-8.103030,-7.870038],[7.844064,7.530527,8.004622,-1.710975,5.651386,7.480126,-1.401765,-5.220451,4.379365]],[[1.605177,4.290705,-9.477501,9.218445,7.599280,7.966692,8.715591,-8.466682,8.914326],[5.783143,9.393322,1.857345,-5.662902,4.976726,-5.175897,9.186796,9.789545,1.533320],[4.767116,5.718392,-0.291907,-2.226287,3.987057,-7.799035,3.631928,-7.880021,-6.897554],[8.396977,-7.758821,3.313079,9.404495,-8.626295,-5.682696,-9.057723,8.394972,-2.882479],[-1.460719,6.055040,-9.686841,-5.908429,2.095704,-4.146115,1.223357,-5.927412,-5.138765]],[[-3.199734,-5.018968,-6.205956,-5.386469,-5.389846,-9.534269,7.545368,0.573542,-2.834521],[1.415802,7.355672,4.882941,-8.344616,-2.778516,-7.043398,0.074120,-8.435792,-5.062518],[-3.315811,-2.831491,-6.864586,2.350988,3.159157,-5.423158,-9.891883,1.530793,-8.049547],[2.280656,6.499933,1.895078,-3.880465,-1.856699,-9.229246,0.267017,-7.063697,3.226401],[-8.771172,-3.590391,3.219920,3.643010,-0.691894,-0.819756,-8.967775,-2.687756,6.500769]]], dtype = "float32")#candidate|9288|(10, 5, 9)|const|float32
bop_9289 = relay.left_shift(uop_9281.astype('uint32'), const_9288.astype('uint32')) # shape=(10, 5, 9)
bop_9292 = relay.left_shift(uop_9283.astype('uint32'), const_9288.astype('uint32')) # shape=(10, 5, 9)
output = relay.Tuple([bop_9289,])
output2 = relay.Tuple([bop_9292,])
func_9298 = relay.Function([], output)
mod['func_9298'] = func_9298
mod = relay.transform.InferType()(mod)
mutated_mod['func_9298'] = func_9298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9298_call = mutated_mod.get_global_var('func_9298')
call_9299 = func_9298_call()
output = call_9299
func_9300 = relay.Function([], output)
mutated_mod['func_9300'] = func_9300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4624_call = mod.get_global_var('func_4624')
func_4625_call = mutated_mod.get_global_var('func_4625')
call_9376 = relay.TupleGetItem(func_4624_call(), 4)
call_9377 = relay.TupleGetItem(func_4625_call(), 4)
output = call_9376
output2 = call_9377
func_9384 = relay.Function([], output)
mod['func_9384'] = func_9384
mod = relay.transform.InferType()(mod)
mutated_mod['func_9384'] = func_9384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9384_call = mutated_mod.get_global_var('func_9384')
call_9385 = func_9384_call()
output = call_9385
func_9386 = relay.Function([], output)
mutated_mod['func_9386'] = func_9386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2958_call = mod.get_global_var('func_2958')
func_2959_call = mutated_mod.get_global_var('func_2959')
call_9465 = relay.TupleGetItem(func_2958_call(), 0)
call_9466 = relay.TupleGetItem(func_2959_call(), 0)
func_7656_call = mod.get_global_var('func_7656')
func_7657_call = mutated_mod.get_global_var('func_7657')
call_9474 = relay.TupleGetItem(func_7656_call(), 1)
call_9475 = relay.TupleGetItem(func_7657_call(), 1)
func_4160_call = mod.get_global_var('func_4160')
func_4162_call = mutated_mod.get_global_var('func_4162')
call_9488 = relay.TupleGetItem(func_4160_call(), 0)
call_9489 = relay.TupleGetItem(func_4162_call(), 0)
output = relay.Tuple([call_9465,call_9474,call_9488,])
output2 = relay.Tuple([call_9466,call_9475,call_9489,])
func_9515 = relay.Function([], output)
mod['func_9515'] = func_9515
mod = relay.transform.InferType()(mod)
output = func_9515()
func_9516 = relay.Function([], output)
mutated_mod['func_9516'] = func_9516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_704_call = mod.get_global_var('func_704')
func_706_call = mutated_mod.get_global_var('func_706')
call_9628 = relay.TupleGetItem(func_704_call(), 0)
call_9629 = relay.TupleGetItem(func_706_call(), 0)
func_3299_call = mod.get_global_var('func_3299')
func_3301_call = mutated_mod.get_global_var('func_3301')
call_9669 = relay.TupleGetItem(func_3299_call(), 0)
call_9670 = relay.TupleGetItem(func_3301_call(), 0)
func_4215_call = mod.get_global_var('func_4215')
func_4217_call = mutated_mod.get_global_var('func_4217')
call_9673 = func_4215_call()
call_9674 = func_4215_call()
func_7687_call = mod.get_global_var('func_7687')
func_7688_call = mutated_mod.get_global_var('func_7688')
call_9678 = relay.TupleGetItem(func_7687_call(), 0)
call_9679 = relay.TupleGetItem(func_7688_call(), 0)
output = relay.Tuple([call_9628,call_9669,call_9673,call_9678,])
output2 = relay.Tuple([call_9629,call_9670,call_9674,call_9679,])
func_9687 = relay.Function([], output)
mod['func_9687'] = func_9687
mod = relay.transform.InferType()(mod)
output = func_9687()
func_9688 = relay.Function([], output)
mutated_mod['func_9688'] = func_9688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3586_call = mod.get_global_var('func_3586')
func_3587_call = mutated_mod.get_global_var('func_3587')
call_9756 = func_3586_call()
call_9757 = func_3586_call()
func_7109_call = mod.get_global_var('func_7109')
func_7110_call = mutated_mod.get_global_var('func_7110')
call_9760 = relay.TupleGetItem(func_7109_call(), 1)
call_9761 = relay.TupleGetItem(func_7110_call(), 1)
output = relay.Tuple([call_9756,call_9760,])
output2 = relay.Tuple([call_9757,call_9761,])
func_9764 = relay.Function([], output)
mod['func_9764'] = func_9764
mod = relay.transform.InferType()(mod)
output = func_9764()
func_9765 = relay.Function([], output)
mutated_mod['func_9765'] = func_9765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_9776 = func_480_call()
call_9777 = func_480_call()
func_4924_call = mod.get_global_var('func_4924')
func_4926_call = mutated_mod.get_global_var('func_4926')
call_9780 = func_4924_call()
call_9781 = func_4924_call()
func_1567_call = mod.get_global_var('func_1567')
func_1568_call = mutated_mod.get_global_var('func_1568')
call_9791 = relay.TupleGetItem(func_1567_call(), 0)
call_9792 = relay.TupleGetItem(func_1568_call(), 0)
output = relay.Tuple([call_9776,call_9780,call_9791,])
output2 = relay.Tuple([call_9777,call_9781,call_9792,])
func_9794 = relay.Function([], output)
mod['func_9794'] = func_9794
mod = relay.transform.InferType()(mod)
output = func_9794()
func_9795 = relay.Function([], output)
mutated_mod['func_9795'] = func_9795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7008_call = mod.get_global_var('func_7008')
func_7009_call = mutated_mod.get_global_var('func_7009')
call_9841 = relay.TupleGetItem(func_7008_call(), 0)
call_9842 = relay.TupleGetItem(func_7009_call(), 0)
func_3155_call = mod.get_global_var('func_3155')
func_3156_call = mutated_mod.get_global_var('func_3156')
call_9858 = func_3155_call()
call_9859 = func_3155_call()
func_8103_call = mod.get_global_var('func_8103')
func_8105_call = mutated_mod.get_global_var('func_8105')
call_9878 = relay.TupleGetItem(func_8103_call(), 0)
call_9879 = relay.TupleGetItem(func_8105_call(), 0)
output = relay.Tuple([call_9841,call_9858,call_9878,])
output2 = relay.Tuple([call_9842,call_9859,call_9879,])
func_9884 = relay.Function([], output)
mod['func_9884'] = func_9884
mod = relay.transform.InferType()(mod)
output = func_9884()
func_9885 = relay.Function([], output)
mutated_mod['func_9885'] = func_9885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7462_call = mod.get_global_var('func_7462')
func_7464_call = mutated_mod.get_global_var('func_7464')
call_9901 = relay.TupleGetItem(func_7462_call(), 0)
call_9902 = relay.TupleGetItem(func_7464_call(), 0)
func_6157_call = mod.get_global_var('func_6157')
func_6160_call = mutated_mod.get_global_var('func_6160')
var_9905 = relay.var("var_9905", dtype = "float64", shape = ())#candidate|9905|()|var|float64
var_9906 = relay.var("var_9906", dtype = "float64", shape = (1176,))#candidate|9906|(1176,)|var|float64
call_9904 = func_6157_call(relay.reshape(var_9905.astype('float64'), []), relay.reshape(var_9906.astype('float64'), [6, 14, 14]), )
call_9907 = func_6157_call(relay.reshape(var_9905.astype('float64'), []), relay.reshape(var_9906.astype('float64'), [6, 14, 14]), )
uop_9910 = relay.sqrt(var_9906.astype('float64')) # shape=(1176,)
output = relay.Tuple([call_9901,call_9904,var_9905,uop_9910,])
output2 = relay.Tuple([call_9902,call_9907,var_9905,uop_9910,])
func_9915 = relay.Function([var_9905,var_9906,], output)
mod['func_9915'] = func_9915
mod = relay.transform.InferType()(mod)
mutated_mod['func_9915'] = func_9915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9915_call = mutated_mod.get_global_var('func_9915')
var_9917 = relay.var("var_9917", dtype = "float64", shape = ())#candidate|9917|()|var|float64
var_9918 = relay.var("var_9918", dtype = "float64", shape = (1176,))#candidate|9918|(1176,)|var|float64
call_9916 = func_9915_call(var_9917,var_9918,)
output = call_9916
func_9919 = relay.Function([var_9917,var_9918,], output)
mutated_mod['func_9919'] = func_9919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5231_call = mod.get_global_var('func_5231')
func_5232_call = mutated_mod.get_global_var('func_5232')
call_9929 = func_5231_call()
call_9930 = func_5231_call()
var_9933 = relay.var("var_9933", dtype = "uint16", shape = (7, 5, 9))#candidate|9933|(7, 5, 9)|var|uint16
bop_9934 = relay.bitwise_and(call_9929.astype('int64'), relay.reshape(var_9933.astype('int64'), relay.shape_of(call_9929))) # shape=(7, 5, 9)
bop_9937 = relay.bitwise_and(call_9930.astype('int64'), relay.reshape(var_9933.astype('int64'), relay.shape_of(call_9930))) # shape=(7, 5, 9)
bop_9940 = relay.mod(bop_9934.astype('float64'), relay.reshape(call_9929.astype('float64'), relay.shape_of(bop_9934))) # shape=(7, 5, 9)
bop_9943 = relay.mod(bop_9937.astype('float64'), relay.reshape(call_9930.astype('float64'), relay.shape_of(bop_9937))) # shape=(7, 5, 9)
output = relay.Tuple([bop_9940,])
output2 = relay.Tuple([bop_9943,])
func_9945 = relay.Function([var_9933,], output)
mod['func_9945'] = func_9945
mod = relay.transform.InferType()(mod)
mutated_mod['func_9945'] = func_9945
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9946 = relay.var("var_9946", dtype = "uint16", shape = (7, 5, 9))#candidate|9946|(7, 5, 9)|var|uint16
func_9945_call = mutated_mod.get_global_var('func_9945')
call_9947 = func_9945_call(var_9946)
output = call_9947
func_9948 = relay.Function([var_9946], output)
mutated_mod['func_9948'] = func_9948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4737_call = mod.get_global_var('func_4737')
func_4739_call = mutated_mod.get_global_var('func_4739')
call_9968 = relay.TupleGetItem(func_4737_call(), 0)
call_9969 = relay.TupleGetItem(func_4739_call(), 0)
output = call_9968
output2 = call_9969
func_9974 = relay.Function([], output)
mod['func_9974'] = func_9974
mod = relay.transform.InferType()(mod)
output = func_9974()
func_9975 = relay.Function([], output)
mutated_mod['func_9975'] = func_9975
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9984 = relay.var("var_9984", dtype = "float64", shape = (15, 6, 16))#candidate|9984|(15, 6, 16)|var|float64
var_9985 = relay.var("var_9985", dtype = "float64", shape = (15, 6, 16))#candidate|9985|(15, 6, 16)|var|float64
bop_9986 = relay.mod(var_9984.astype('float64'), relay.reshape(var_9985.astype('float64'), relay.shape_of(var_9984))) # shape=(15, 6, 16)
output = relay.Tuple([bop_9986,])
output2 = relay.Tuple([bop_9986,])
func_9990 = relay.Function([var_9984,var_9985,], output)
mod['func_9990'] = func_9990
mod = relay.transform.InferType()(mod)
var_9991 = relay.var("var_9991", dtype = "float64", shape = (15, 6, 16))#candidate|9991|(15, 6, 16)|var|float64
var_9992 = relay.var("var_9992", dtype = "float64", shape = (15, 6, 16))#candidate|9992|(15, 6, 16)|var|float64
output = func_9990(var_9991,var_9992,)
func_9993 = relay.Function([var_9991,var_9992,], output)
mutated_mod['func_9993'] = func_9993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5597_call = mod.get_global_var('func_5597')
func_5599_call = mutated_mod.get_global_var('func_5599')
call_10023 = relay.TupleGetItem(func_5597_call(), 0)
call_10024 = relay.TupleGetItem(func_5599_call(), 0)
func_6303_call = mod.get_global_var('func_6303')
func_6305_call = mutated_mod.get_global_var('func_6305')
call_10057 = relay.TupleGetItem(func_6303_call(), 1)
call_10058 = relay.TupleGetItem(func_6305_call(), 1)
func_2140_call = mod.get_global_var('func_2140')
func_2143_call = mutated_mod.get_global_var('func_2143')
const_10060 = relay.const([5.835984,0.064949,9.814980,4.671908,-8.572773,0.602693,-0.650742,-7.082764,-3.547570,1.044462,8.385303,-8.005643,0.528231,0.687437,-5.163165,7.184050,-8.231498,-4.612296,-1.926335,1.134152,-7.966621,-4.404697,8.456255,-8.932911,0.195262,4.393386,2.477750,5.494482,5.742498,-6.922100,-2.444710,3.353885,-8.565616,-7.440956,7.379791,-5.901592,6.046757,-1.556101,9.697139,-9.525162,-7.365933,0.498046,6.805549,-4.477837,-1.834717,5.652762,-6.579432,4.985804,-2.477486,9.399084,3.028333,7.652709,-4.073045,5.939545,-2.957405,-6.547257,-5.197949,8.146362,-6.312009,-7.099872,-0.552360,7.939187,-8.768714,8.773347,0.062435,-6.201164,-7.252019,5.184720,1.539064,-7.192506,-4.456336,-7.323436,9.977184,0.133650,7.173533,-7.727876,8.307679,-6.103053,-7.473338,-7.067204,9.208628,-4.699617,-7.971148,-9.458465,-2.060404,-7.800137,-1.646330,0.724666,-7.876762,2.687640,-5.528379,9.113280,-8.282648,4.159953,5.556998,-8.347275,-9.165220,0.174078,-8.198792,-6.332932,-2.948775,7.487030,0.778806,-0.091431,2.372848,8.350909,0.424662,5.637269,8.447916,-5.074872,-4.346512,0.232887,8.513528,-4.557859,-6.484609,2.214194,7.920398,3.103905,4.030376,-2.304941,-1.395725,0.853717,-9.067264,8.675462,8.219599,-8.082381,-7.399844,6.169205,-9.118714,1.420448,-6.857071,-3.001572,7.715806,7.839791,0.371579,-6.571505,8.177935,-5.450756,-9.880616,9.117661,7.049579,-8.305323,2.940591,-2.877989,6.790359,5.924837,-8.272981,3.365390,2.803956,-7.253305,-7.264209,-1.345854,-8.973562,4.303546,-6.627219,2.304915,-8.176131,2.728018,6.104383,-3.048772,7.653527,-7.692020,9.304448,-2.549182,-8.844918,7.527178,7.776584,6.119426,-0.878856,-4.439582,4.720017,6.151192,6.648372,-0.633802,-9.098119,2.678427,-1.377688,8.807754,0.418664,-8.571240,-3.337641,-1.724914,-5.346822,-8.509638,-3.655075,1.766288,-4.142180,-0.260020,-5.101512,-6.723491,6.523323,-8.586811,9.852100,1.901587,4.477670,7.490567,3.369859,5.901339,1.168380,9.520869,0.636863,2.766296,7.161798,3.218265,-4.686466,-9.178992,-3.548102,7.063365,-6.099825,-3.748805,0.653372,6.528802,-8.749816,-4.841855,-0.485484,7.463017,-6.237357,8.520964,-7.615192,1.915783,-1.503990,-2.710302,5.193075,1.963261,-5.455142,6.600659,5.629607,5.225778,-0.658945,0.089176,5.140652,-0.068049,2.145931,4.632810,-5.798521,7.506955,-2.248217,0.679684,1.102100,2.109646,1.188157,6.742315,9.390921,-2.808674,-0.350284,2.427159,-3.460529,-7.391399,7.250405,-5.122577,-1.377031,6.915566,3.682119,-4.665426,2.291253,6.882092,9.561365,7.326075,8.268133,-7.436364,6.147573,4.323945,0.918737,9.661218,5.209073,-4.757483,0.020600,-5.646224,2.669024,-6.137866,-0.432244,6.967765,-4.126308,-2.120044,-8.536129,-4.563803,-9.941266,5.354736,2.066918,1.360054,-2.097604,-6.984047,1.019032,6.420642,-7.060842,2.413623,6.753203,-2.126341,7.655984,8.700768,2.841463,2.220915,3.456028,1.149332,4.629996,6.295979,-6.033723,-2.084671,-0.975347,-9.774762,6.452439,2.229047,-9.991785,-8.098156,-6.397632,0.357623,2.058345,-0.198763,-1.992646,8.385556,-3.726687,0.971113,1.896959,-8.669288,4.204487,-3.858095,-2.735468,8.153176,0.600375,-7.261530,7.129700,7.736362,-1.667582,4.275826,6.556553,-5.467224,6.786351,-4.025149,0.793183,-4.088326,-2.488724,9.835199,-8.610552,6.840221,4.494476,-5.248010,-8.034622,1.304700,1.802234,5.380236,-8.191359,-7.832252,7.663329,-4.751994,0.201515,-0.033305,6.199493,-9.244279,-6.872206,7.292281,8.079236,1.867353,0.998824,-5.347279,6.639670,3.528742,7.104428,-2.208315,-5.052364,-2.101200,4.208189,3.297179,-7.770447,2.358769,-8.254628,-9.590198,-1.470264,5.752940,8.155838,-6.883388,5.046966,-4.726436,7.706263,7.007673,9.712126,9.566281,-1.879255,5.622664,-2.905906,-3.095106,1.027397,-7.195965,-7.749899,8.099697,6.675894,-2.296738,0.184483,4.726095,6.400612,-5.928737,-1.118756,-3.150937,1.492372,-6.160788,-2.792802,-2.426645,3.350034,8.983015,-6.354443,4.709142,-7.468685,-6.214421,-9.015937,-4.610252,-5.706905], dtype = "float64")#candidate|10060|(405,)|const|float64
call_10059 = relay.TupleGetItem(func_2140_call(relay.reshape(const_10060.astype('float64'), [405,])), 1)
call_10061 = relay.TupleGetItem(func_2143_call(relay.reshape(const_10060.astype('float64'), [405,])), 1)
func_7338_call = mod.get_global_var('func_7338')
func_7342_call = mutated_mod.get_global_var('func_7342')
var_10063 = relay.var("var_10063", dtype = "int64", shape = (56, 20))#candidate|10063|(56, 20)|var|int64
call_10062 = func_7338_call(relay.reshape(var_10063.astype('int64'), [16, 7, 10]), relay.reshape(var_10063.astype('int64'), [16, 7, 10]), )
call_10064 = func_7338_call(relay.reshape(var_10063.astype('int64'), [16, 7, 10]), relay.reshape(var_10063.astype('int64'), [16, 7, 10]), )
bop_10071 = relay.floor_mod(call_10059.astype('float64'), relay.reshape(const_10060.astype('float64'), relay.shape_of(call_10059))) # shape=(9, 5, 9)
bop_10074 = relay.floor_mod(call_10061.astype('float64'), relay.reshape(const_10060.astype('float64'), relay.shape_of(call_10061))) # shape=(9, 5, 9)
const_10083 = relay.const([[-10,8,5,-5,-6,-6,3,5,-3,2,8,6,2,10,2,-5,-6,-10,-5,-7],[10,-6,-7,6,8,6,6,8,3,-5,10,7,4,-1,2,10,3,-6,-6,2],[10,10,1,7,7,-9,3,7,5,6,5,-1,1,1,-2,1,-1,10,-10,6],[-1,8,-2,3,2,7,5,-6,-5,-4,-9,9,-8,2,9,7,4,6,-10,-5],[8,10,10,-10,4,-2,-10,3,-1,8,-6,2,10,-7,-6,-5,-4,8,10,1],[-1,-6,-5,9,-5,-5,-1,10,4,-6,-10,5,-5,-10,-10,-10,3,3,7,3],[10,3,-7,-7,-10,3,3,8,2,4,8,-2,1,10,-9,8,-2,-1,5,4],[-10,-7,-7,-2,2,1,-1,2,10,8,6,-9,10,-9,-9,-10,2,-3,-2,-7],[10,-4,-3,-2,2,-10,-9,-7,8,-2,1,-5,9,3,2,6,10,-4,-8,-3],[10,9,2,-6,3,7,-2,-10,-2,-2,5,-8,-8,9,3,-8,-7,10,-2,2],[-8,3,3,1,-6,-10,3,-7,2,-8,-8,-8,1,6,8,-1,9,6,-9,9],[-2,-8,9,-5,-1,-8,7,-6,3,4,-10,-8,2,10,3,-7,-10,-1,10,2],[8,2,3,6,10,9,-6,8,1,9,7,10,-1,-6,6,4,-7,1,-4,8],[-6,3,-4,-2,-1,10,5,7,2,8,-3,-3,-9,-10,9,9,5,-9,-5,5],[-10,-3,-6,4,6,-5,2,-1,2,4,-1,9,4,-6,-9,-4,5,-7,-10,8],[-10,-6,3,-5,-9,6,-1,8,3,6,-7,2,-8,5,-9,-5,-6,-3,-10,-3],[7,-1,-6,-6,4,-2,2,5,2,-9,2,10,-7,-8,1,-6,-5,-9,-7,-2],[6,-4,-8,10,10,1,-7,4,3,-1,-5,5,5,3,-8,4,10,4,-10,10],[-6,-6,3,9,1,-2,-8,-10,-10,8,9,6,2,9,-6,6,9,7,9,8],[5,-10,-7,-9,-3,-7,-8,2,-2,-6,8,-4,-1,1,-6,-3,8,-7,2,-4],[-10,-7,-3,-10,8,5,7,6,-10,-9,-5,1,-6,2,2,-4,4,-5,-10,2],[-1,5,6,-8,-8,5,1,-1,-4,-6,-7,-1,4,8,10,-4,-6,-1,-2,-1],[5,-8,-3,3,3,4,-4,3,-10,3,-2,3,10,4,-2,-4,2,1,-2,3],[-8,5,3,-9,2,4,-1,-4,2,2,-3,-1,10,-10,-8,8,-1,7,5,-6],[-10,-1,-1,3,-2,-7,3,10,10,6,5,4,-8,-8,7,-8,-8,9,3,-3],[6,10,8,3,-1,5,-2,2,2,-3,-7,7,9,3,9,-8,5,-6,-9,-8],[7,-10,6,9,3,-8,-4,-4,-4,-6,2,-8,4,-10,3,5,5,1,7,-9],[3,-9,-6,-9,-1,-3,-10,1,-7,7,9,3,9,-5,-3,7,6,2,-10,-2],[7,5,8,-1,7,6,4,-9,-3,-9,1,-2,-3,-6,-9,-7,6,4,-8,-1],[-7,-2,-6,3,-7,8,10,2,-6,8,1,-2,7,-2,-4,-3,-10,3,-8,-9],[-9,-3,-7,-4,-7,8,10,-4,-7,6,-9,-4,4,9,4,-6,-5,3,6,-4],[-2,1,-4,10,3,-5,-5,-3,6,10,2,-4,7,-6,7,-5,4,-10,3,2],[-8,-8,5,1,-7,-3,8,-5,-5,9,-5,-8,2,-7,-1,-1,-5,-1,4,4],[-2,-2,4,-9,-10,-8,3,-4,-7,-2,-10,-7,-3,7,-8,-9,-10,5,8,-3],[-2,-3,-9,2,8,4,4,-2,8,4,-4,10,-4,10,-9,-2,5,6,2,2],[9,-5,7,-1,1,-5,-10,9,-10,-8,3,9,-5,6,2,-7,-3,-3,-2,-7],[2,7,7,-8,8,-5,7,-1,-9,-2,-4,-2,-1,-7,-1,-7,-6,-7,-4,-9],[2,-3,8,-1,-10,9,-2,-1,8,-8,-2,-4,-1,9,-5,-6,-2,5,-5,-8],[3,-9,10,8,7,7,-2,6,-1,9,-3,4,-5,5,9,-5,3,-5,-5,9],[10,-1,-6,-8,-4,-4,5,2,6,2,-3,8,-2,-8,-10,10,4,4,2,8],[2,-5,-7,7,-6,-1,-5,-6,-3,-5,-3,5,-10,-9,3,-6,-7,-2,-10,2],[-7,5,-3,2,-7,-1,3,10,-4,-4,8,2,3,-2,2,-8,-8,-2,6,-8],[-10,-5,-4,-6,8,7,-2,-1,-2,7,-6,2,10,4,-7,-10,3,10,2,8],[-8,6,-4,6,-10,10,9,-2,6,-4,-2,10,10,3,-9,-4,3,-8,6,3],[-8,4,4,6,-5,5,-5,-1,6,-8,2,-2,3,4,-4,7,-1,-9,8,7],[6,-1,8,7,-5,-10,1,3,-2,5,-5,7,-3,3,2,7,3,-2,-7,6],[7,8,-8,2,-8,-7,9,-9,2,4,-3,5,-6,-6,7,-6,9,-10,6,8],[-1,9,1,-10,9,9,6,7,-1,8,8,-2,-9,4,6,-1,9,7,-7,4],[-3,-7,7,3,-10,7,5,3,-2,9,-8,-7,10,6,-10,-3,-5,2,-6,-1],[-5,4,-8,2,-3,9,1,8,-9,9,9,2,2,-6,-10,5,-7,-3,-6,-6],[8,-10,-3,-2,-7,2,1,-7,-10,1,10,-3,-7,-2,3,-9,5,-10,10,-1],[-3,10,-8,8,2,8,-9,8,9,-6,2,-3,-7,-5,7,5,-10,-5,-3,-6],[4,6,-7,7,6,10,1,5,8,-6,-10,6,-5,8,-6,3,-10,-3,-5,5],[-6,-1,8,-8,10,5,6,-9,4,10,-4,10,-4,-3,5,-10,4,-1,-9,-1],[2,6,7,8,-5,-3,-1,-6,-8,-4,8,-6,-5,-5,6,3,3,-8,7,4],[-6,2,10,4,7,-2,2,-7,7,-3,-7,-2,8,-1,-8,6,1,-1,7,8]], dtype = "int64")#candidate|10083|(56, 20)|const|int64
bop_10084 = relay.add(var_10063.astype('uint8'), relay.reshape(const_10083.astype('uint8'), relay.shape_of(var_10063))) # shape=(56, 20)
uop_10091 = relay.log(const_10060.astype('float64')) # shape=(405,)
func_564_call = mod.get_global_var('func_564')
func_566_call = mutated_mod.get_global_var('func_566')
call_10094 = relay.TupleGetItem(func_564_call(), 0)
call_10095 = relay.TupleGetItem(func_566_call(), 0)
bop_10096 = relay.divide(uop_10091.astype('float64'), relay.reshape(call_10059.astype('float64'), relay.shape_of(uop_10091))) # shape=(405,)
bop_10099 = relay.divide(uop_10091.astype('float64'), relay.reshape(call_10061.astype('float64'), relay.shape_of(uop_10091))) # shape=(405,)
func_7981_call = mod.get_global_var('func_7981')
func_7984_call = mutated_mod.get_global_var('func_7984')
const_10120 = relay.const([9,-3,7,-5,7,-6,-3,7,-7,1,-4,-3,2,1,5,3,-7,8,-2,10,-4,-10,-5,-9,9,-10,-10,7,5,3,-5,3,-7,-6,5,-10,2,5,6,2,4,2,5,8,-7,-1,9,4,6,-5,-8,7,3,-7,-6,8,-3,5,-10,-7,4,-1,3,-9,7,-7,8,-5,5,-2], dtype = "int32")#candidate|10120|(70,)|const|int32
const_10121 = relay.const([-7.855080,9.834603,-7.930468,9.511163,6.706446,5.831827,-1.003752,7.181545,4.619477,2.354154,1.934740,0.161286,7.878630,0.897710,4.670879,9.716027,-4.930552,-1.798829,8.056713,-9.790583,5.820190,-5.149008,-3.542397,9.180993,-1.673808,-3.471302,-0.172166,6.702850,-9.807238,-3.826542,4.245532,7.479708,-6.351476,7.352691,1.733877,-3.630068,3.494742,0.182396,-2.203565,7.292577,2.553603,-5.877477,-6.157604,8.497097,-3.737477,-2.179479,7.918258,9.046673,6.547193,7.825667,-3.134643,-7.308390,9.375094,2.599723,-9.474094,-9.862398,-4.934649,4.532800,-5.528549,7.702376,-5.065072,-8.289941,-7.526658,3.010232,-5.702573,-5.757862,-1.901891,2.381603,-9.048334,5.654601,8.908244,3.339025,-5.823096,-5.936144,4.107162,3.939968,-2.252717,-9.475827,6.986720,-3.207365,-6.998389,-0.678094,5.087338,-4.077003,-7.101863,9.870076,4.231862,-7.686625,3.845027,-7.391206,-5.943780,0.607416,-3.641496,9.653364,9.404081,9.364258,5.085100,7.815827,5.811702,-8.966970,8.902664,-6.669565,-5.372666,3.536659,0.628884,9.217642,6.342245,-9.372586,-3.849972,-1.655733,-2.628043,6.530487,3.716518,-5.209407,7.421644,2.401138,-6.482669,2.952687,-3.803843,1.877101,1.288718,0.342014,2.231656,-2.615663,-6.985180,6.114618,-6.693900,-1.601654,0.270253,0.203812,0.123958,-8.548782,-1.735062,0.343387,-2.566691,-4.664664,5.269659,-3.457187,-7.679195,-9.347532,3.339558,1.474922,-7.649992,-0.476231,-7.241922,-1.954771,-7.581817,-1.261739,8.080489,7.538361,-4.221667,8.378876,1.814645,-0.366239,-3.192949,-1.740765,-2.792447,5.618885,3.041560,4.595608,5.569839,-5.449896,-8.686309,-8.457873,-3.397016,8.236748,-8.514707,-3.746960,-5.563305,0.519838,5.908733,9.777116,0.194192,-1.956194,-9.856404,-7.802247,-1.390241,4.579784,8.797267,-8.349217,2.509076,-7.312989,-9.548304,9.338891,4.578514,2.973002,0.652538,6.515828,1.214717,8.836754,5.972083,-2.260393,-2.433306,-5.639630,4.352621,7.691817,-0.110886,-2.129956,-9.477817,9.146319,-8.503640,-6.752478,6.216741,-6.718684,-1.660961,-6.619895,-1.744796,1.419464,-9.989298,-1.809185,-5.818022,-6.618804,-4.821463,8.990832,9.539660,-2.095731,9.718856,0.694330,-5.023651,7.418302,0.796437,-2.620417,-0.119820,9.646199,2.907546,0.747845,7.989770,-6.956414,-5.036405,1.332886,9.357384,-3.258724,-0.661305,2.015410,0.386180,5.471577,5.794820,-7.365109,2.735754,-0.888095,-8.535026,-9.387364,-2.723812,4.247009,-4.960977,-2.381752,-0.581128,-0.572499,-6.977062,-8.795045,0.278853,-6.207687,6.357035,-3.556118,-0.766599,-7.301757,-9.523851,7.135419,4.718332,-7.311977,7.925838,2.213132,0.841610,-5.740745,-1.197016,3.907913,6.731385,-1.712717,7.892281,3.908515,5.171380,-7.854575,1.087962,-2.262025,-7.327769,-6.874807,4.927473,0.817868,-5.089580,-0.140433,-4.674379,-5.923200,-4.859598,5.896656,6.364933,4.927096,-9.996070,4.433813,9.934912,-6.959991,-4.196416,2.914398,0.364179,-0.677704,5.728727,-8.275136,-2.138703,8.953107,3.696157,-5.227262,0.406232,0.348798,7.581772,4.868141,5.177321,-9.107995,2.579133,1.523502,5.487706,-6.217303,7.251756,-9.975681,6.637078,-7.811951,-2.359255,7.553611,-2.630528,9.068250,5.308354,6.262003,9.748053,-5.454028,8.003259,4.769033,8.745757,8.296477,-1.568160,8.422263,6.230401,-1.427152,-6.051872,-9.289320,-9.283220,2.401823,-8.826092,-0.554449,-7.546168,-2.884277,7.517961,-8.405623,4.991778,6.353618,-9.026436,6.211211,-8.522206,8.439515,-5.179856,6.873730,-7.261774,-7.600214,8.455403,-1.681210,-5.769077,-6.403620,-3.305010,-5.350278,-0.648057,1.478520,-8.155796,3.399799,-0.320259,-5.807787,-4.747719,0.218015,-2.292981,2.571357,3.667061,0.087795,8.975278,7.347691,4.138625,7.497024,5.316474,-4.430744,-2.669592,-5.449268,-3.037208,0.801280,-4.240493,5.769816,-1.144619,7.865123,-2.747183,2.598934,-0.007490,2.209473,2.302697,3.712166,1.588420,-2.154927,0.793411,-2.737444,1.224748,-2.843537,5.413054,-7.997523,8.713491,0.322075,4.502840,9.327213,5.668818,1.096475,1.688809,1.617159,-6.459456,-1.629155,-3.810900,8.212328,-9.949369,8.472544,-1.281934,-7.197214,0.785905,6.479396,-5.775743,-1.308098,-1.741585,-5.693381,9.003381,-3.864231,-3.118339,8.235051,-7.163705,-2.985261,3.657858,-8.035245,-5.242552,9.577286,-2.667415,-5.907892,6.477707,-6.783966,-6.813110,3.561387,-2.955979,0.178212,3.962664,7.516355,6.442909,-4.794627,9.512695,-5.332388,4.044492,-8.404487,2.541484,0.286342,9.787924,-3.739563,-3.825945,3.374038,1.590147,1.274935,-1.842586,-6.842767,5.903025,-3.035828,0.847483,-8.733174,-2.610369,-6.937509,6.899708,-5.342604,3.927542,-5.786674,-7.162181,-7.593458,-0.466824,-5.423770,-4.182023,-1.996448,-5.240670,3.984256,-6.994315,-1.490906,-0.657482,-2.021769,-0.201539,-8.297832,8.355277,-9.134566,7.826051,9.853749,-2.037363,-4.490541,1.427302,-5.361009,2.469477,2.840441,6.729442,-9.752725,7.859303,6.883074,4.099710,4.602338,-9.586663,-9.038374,1.223729,5.574243,-8.898871,-8.062272,7.427921,0.411454,-8.987877,-6.803970], dtype = "float32")#candidate|10121|(504,)|const|float32
call_10119 = relay.TupleGetItem(func_7981_call(relay.reshape(const_10120.astype('int32'), [70,]), relay.reshape(const_10121.astype('float32'), [6, 84]), ), 3)
call_10122 = relay.TupleGetItem(func_7984_call(relay.reshape(const_10120.astype('int32'), [70,]), relay.reshape(const_10121.astype('float32'), [6, 84]), ), 3)
output = relay.Tuple([call_10023,call_10057,call_10062,bop_10071,bop_10084,call_10094,bop_10096,call_10119,const_10120,const_10121,])
output2 = relay.Tuple([call_10024,call_10058,call_10064,bop_10074,bop_10084,call_10095,bop_10099,call_10122,const_10120,const_10121,])
func_10123 = relay.Function([var_10063,], output)
mod['func_10123'] = func_10123
mod = relay.transform.InferType()(mod)
mutated_mod['func_10123'] = func_10123
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10124 = relay.var("var_10124", dtype = "int64", shape = (56, 20))#candidate|10124|(56, 20)|var|int64
func_10123_call = mutated_mod.get_global_var('func_10123')
call_10125 = func_10123_call(var_10124)
output = call_10125
func_10126 = relay.Function([var_10124], output)
mutated_mod['func_10126'] = func_10126
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10131 = relay.const([[[-4.114881,8.729054,3.985823,-1.132432,-5.778896,-7.360729,-3.935823,9.379295,2.550568,-1.933790,1.605949,6.625228,0.329904,-6.025193,3.203851,-7.114252],[-4.256182,-6.759184,-4.137067,-0.609025,-6.404701,-8.863305,-2.662121,3.979674,8.661512,8.263916,-0.994030,-2.379828,-1.544439,-6.084868,-4.080282,7.780624]],[[-7.355178,-7.671203,-8.269755,3.585655,0.252025,-6.849832,1.794157,-2.484105,8.071736,7.377568,-2.092180,7.690285,-4.868290,-6.125296,-9.893686,2.023247],[3.529633,9.952958,-1.588137,-3.517584,-5.164031,-7.657873,8.683695,-1.624295,-2.973172,-2.593202,1.440451,2.043533,4.965093,-4.426316,7.814442,-2.091519]],[[2.527784,-7.302602,5.764125,-7.736870,6.661741,4.048163,9.546496,7.453395,-5.926315,-5.416828,-0.125618,7.757163,-0.755607,3.465011,-9.053628,-8.666789],[-4.051849,1.733036,-7.845826,2.822156,-2.241753,-0.819667,3.739590,2.784749,2.016010,6.148489,8.510587,-8.079916,6.928009,7.631913,3.271881,9.134430]],[[5.737932,7.165305,-2.844699,9.345902,-9.488056,-5.691964,-8.758480,2.115212,-9.681091,1.410065,6.496054,3.504099,1.189617,-5.913864,-6.033757,-9.985582],[1.058466,4.579499,4.879510,-9.054802,-5.628091,6.825579,2.573054,0.478197,8.883913,0.314689,-8.513526,8.983807,-7.966299,-8.667193,-8.150588,-0.822866]],[[3.617561,3.802417,-8.162485,-7.082667,9.959652,7.000719,-2.655651,-8.802770,8.333423,-6.118943,-2.204909,-1.149413,-2.201853,8.176486,5.394155,-8.387988],[-6.702264,3.572060,0.174904,3.850043,0.419146,6.295530,6.503977,-0.589732,-9.450116,-3.981620,-7.059029,3.208756,-4.788340,4.085040,-7.053181,-7.702179]],[[-4.973931,5.419145,6.786844,-5.079373,-3.028728,-4.173221,9.139362,-6.466315,9.241546,-8.867618,5.885210,-4.533213,-2.491257,-8.003764,7.643105,2.980070],[-1.256400,-6.947418,-8.960934,4.111471,-8.239134,-8.304650,-0.948339,8.482764,-6.670952,3.662881,6.465806,7.032286,-1.494002,-4.656795,-7.059659,8.478888]],[[0.177280,-3.964015,-7.490980,-8.064939,0.087012,-7.869488,0.616753,0.083342,7.995459,-4.965089,1.318850,-2.053422,7.501030,5.388396,4.983080,-5.192942],[-2.053205,-7.358618,-5.220289,-3.596176,7.996651,3.850692,-5.644353,-7.243563,-3.462803,6.933240,-8.323192,3.408481,-3.240828,9.543043,7.991744,-5.497180]],[[-7.190742,-2.927226,8.731447,-8.643469,3.862231,-6.975043,4.108378,5.713033,8.537841,0.278967,-6.166387,5.092780,0.991093,-9.108757,-3.222811,2.908486],[7.462385,-3.778704,-7.884543,-3.665500,-5.263475,1.530942,3.836267,3.216983,5.834044,5.204802,4.206774,0.593749,7.676892,7.513117,-9.413320,8.786792]],[[-6.011419,0.069149,-3.430987,-4.881630,-3.343850,-2.492176,-3.518882,-6.274935,-0.457161,-5.713557,-0.970532,6.065877,3.582110,6.121597,2.767276,-8.582796],[-6.719923,-8.494333,6.122016,-1.494503,-1.354169,3.891862,-8.341959,3.828693,9.058731,5.192247,8.462681,-3.457513,0.806161,-7.315073,-4.329428,8.025056]],[[-1.689931,9.845328,-3.488782,6.947260,3.360957,-8.675491,-5.720001,-0.320067,6.822220,1.355114,-0.231909,7.157361,-4.828491,-4.239040,-8.517290,5.769083],[5.581773,-0.871517,-6.894529,0.485806,9.212819,-8.793387,3.836808,4.452372,-1.878462,1.180804,-0.363022,-6.778938,-7.126184,3.060982,-6.668797,-3.458835]]], dtype = "float64")#candidate|10131|(10, 2, 16)|const|float64
uop_10132 = relay.asin(const_10131.astype('float64')) # shape=(10, 2, 16)
output = relay.Tuple([uop_10132,])
output2 = relay.Tuple([uop_10132,])
func_10135 = relay.Function([], output)
mod['func_10135'] = func_10135
mod = relay.transform.InferType()(mod)
mutated_mod['func_10135'] = func_10135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10135_call = mutated_mod.get_global_var('func_10135')
call_10136 = func_10135_call()
output = call_10136
func_10137 = relay.Function([], output)
mutated_mod['func_10137'] = func_10137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3069_call = mod.get_global_var('func_3069')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_10160 = relay.TupleGetItem(func_3069_call(), 2)
call_10161 = relay.TupleGetItem(func_3070_call(), 2)
output = relay.Tuple([call_10160,])
output2 = relay.Tuple([call_10161,])
func_10162 = relay.Function([], output)
mod['func_10162'] = func_10162
mod = relay.transform.InferType()(mod)
mutated_mod['func_10162'] = func_10162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10162_call = mutated_mod.get_global_var('func_10162')
call_10163 = func_10162_call()
output = call_10163
func_10164 = relay.Function([], output)
mutated_mod['func_10164'] = func_10164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4675_call = mod.get_global_var('func_4675')
func_4677_call = mutated_mod.get_global_var('func_4677')
call_10193 = relay.TupleGetItem(func_4675_call(), 0)
call_10194 = relay.TupleGetItem(func_4677_call(), 0)
output = call_10193
output2 = call_10194
func_10202 = relay.Function([], output)
mod['func_10202'] = func_10202
mod = relay.transform.InferType()(mod)
mutated_mod['func_10202'] = func_10202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10202_call = mutated_mod.get_global_var('func_10202')
call_10203 = func_10202_call()
output = call_10203
func_10204 = relay.Function([], output)
mutated_mod['func_10204'] = func_10204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7656_call = mod.get_global_var('func_7656')
func_7657_call = mutated_mod.get_global_var('func_7657')
call_10221 = relay.TupleGetItem(func_7656_call(), 1)
call_10222 = relay.TupleGetItem(func_7657_call(), 1)
func_4924_call = mod.get_global_var('func_4924')
func_4926_call = mutated_mod.get_global_var('func_4926')
call_10228 = func_4924_call()
call_10229 = func_4924_call()
output = relay.Tuple([call_10221,call_10228,])
output2 = relay.Tuple([call_10222,call_10229,])
func_10230 = relay.Function([], output)
mod['func_10230'] = func_10230
mod = relay.transform.InferType()(mod)
output = func_10230()
func_10231 = relay.Function([], output)
mutated_mod['func_10231'] = func_10231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4557_call = mod.get_global_var('func_4557')
func_4558_call = mutated_mod.get_global_var('func_4558')
call_10237 = relay.TupleGetItem(func_4557_call(), 0)
call_10238 = relay.TupleGetItem(func_4558_call(), 0)
output = relay.Tuple([call_10237,])
output2 = relay.Tuple([call_10238,])
func_10242 = relay.Function([], output)
mod['func_10242'] = func_10242
mod = relay.transform.InferType()(mod)
mutated_mod['func_10242'] = func_10242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10242_call = mutated_mod.get_global_var('func_10242')
call_10243 = func_10242_call()
output = call_10243
func_10244 = relay.Function([], output)
mutated_mod['func_10244'] = func_10244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8349_call = mod.get_global_var('func_8349')
func_8351_call = mutated_mod.get_global_var('func_8351')
call_10258 = relay.TupleGetItem(func_8349_call(), 0)
call_10259 = relay.TupleGetItem(func_8351_call(), 0)
output = relay.Tuple([call_10258,])
output2 = relay.Tuple([call_10259,])
func_10274 = relay.Function([], output)
mod['func_10274'] = func_10274
mod = relay.transform.InferType()(mod)
output = func_10274()
func_10275 = relay.Function([], output)
mutated_mod['func_10275'] = func_10275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9188_call = mod.get_global_var('func_9188')
func_9189_call = mutated_mod.get_global_var('func_9189')
call_10284 = func_9188_call()
call_10285 = func_9188_call()
func_5324_call = mod.get_global_var('func_5324')
func_5326_call = mutated_mod.get_global_var('func_5326')
call_10299 = func_5324_call()
call_10300 = func_5324_call()
func_7656_call = mod.get_global_var('func_7656')
func_7657_call = mutated_mod.get_global_var('func_7657')
call_10305 = relay.TupleGetItem(func_7656_call(), 1)
call_10306 = relay.TupleGetItem(func_7657_call(), 1)
output = relay.Tuple([call_10284,call_10299,call_10305,])
output2 = relay.Tuple([call_10285,call_10300,call_10306,])
func_10323 = relay.Function([], output)
mod['func_10323'] = func_10323
mod = relay.transform.InferType()(mod)
output = func_10323()
func_10324 = relay.Function([], output)
mutated_mod['func_10324'] = func_10324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9202_call = mod.get_global_var('func_9202')
func_9204_call = mutated_mod.get_global_var('func_9204')
call_10336 = func_9202_call()
call_10337 = func_9202_call()
func_4850_call = mod.get_global_var('func_4850')
func_4852_call = mutated_mod.get_global_var('func_4852')
var_10342 = relay.var("var_10342", dtype = "float32", shape = (36, 14))#candidate|10342|(36, 14)|var|float32
call_10341 = relay.TupleGetItem(func_4850_call(relay.reshape(var_10342.astype('float32'), [12, 3, 14])), 0)
call_10343 = relay.TupleGetItem(func_4852_call(relay.reshape(var_10342.astype('float32'), [12, 3, 14])), 0)
func_3155_call = mod.get_global_var('func_3155')
func_3156_call = mutated_mod.get_global_var('func_3156')
call_10345 = func_3155_call()
call_10346 = func_3155_call()
output = relay.Tuple([call_10336,call_10341,var_10342,call_10345,])
output2 = relay.Tuple([call_10337,call_10343,var_10342,call_10346,])
func_10347 = relay.Function([var_10342,], output)
mod['func_10347'] = func_10347
mod = relay.transform.InferType()(mod)
var_10348 = relay.var("var_10348", dtype = "float32", shape = (36, 14))#candidate|10348|(36, 14)|var|float32
output = func_10347(var_10348)
func_10349 = relay.Function([var_10348], output)
mutated_mod['func_10349'] = func_10349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7067_call = mod.get_global_var('func_7067')
func_7069_call = mutated_mod.get_global_var('func_7069')
call_10376 = relay.TupleGetItem(func_7067_call(), 0)
call_10377 = relay.TupleGetItem(func_7069_call(), 0)
output = call_10376
output2 = call_10377
func_10393 = relay.Function([], output)
mod['func_10393'] = func_10393
mod = relay.transform.InferType()(mod)
output = func_10393()
func_10394 = relay.Function([], output)
mutated_mod['func_10394'] = func_10394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7882_call = mod.get_global_var('func_7882')
func_7884_call = mutated_mod.get_global_var('func_7884')
call_10412 = func_7882_call()
call_10413 = func_7882_call()
func_7890_call = mod.get_global_var('func_7890')
func_7891_call = mutated_mod.get_global_var('func_7891')
call_10438 = func_7890_call()
call_10439 = func_7890_call()
func_6289_call = mod.get_global_var('func_6289')
func_6292_call = mutated_mod.get_global_var('func_6292')
const_10452 = relay.const([-1.243872,-4.886333,7.430494,3.307082,-7.353463,9.420292,-8.844652,-5.685024,6.447052,-2.730349,-7.771824,4.383853,-9.952551,-9.996325,-8.427702,0.294138,-2.009180,-5.489755,-4.320372,-3.685271,0.848613,7.272168,-3.559596,0.310705,-4.504231,6.651382,-5.325094,3.651958,6.269212,-9.774570,-9.096063,-0.338850,8.403809,-6.904352,-9.370667,-4.849142,-2.794170,2.538516,6.036670,-1.178690,5.992282,4.237550,-0.315371,-6.836882,-9.224211,0.531249,-1.960988,3.482625,-2.777978,9.330685,-4.505727,-8.273191,-9.884910,9.693177,-9.478940,2.818922,8.113757,8.608873,-5.179884,5.173360,-6.195726,7.879396,-5.702348,-0.294025,4.217774,-1.357708,7.967772,-2.120507,-9.462549,-4.864230,-0.592417,-2.779686,-4.618134,5.086756,1.875931,2.570296,-5.411681,5.223858,2.555578,2.046223], dtype = "float32")#candidate|10452|(80,)|const|float32
call_10451 = relay.TupleGetItem(func_6289_call(relay.reshape(const_10452.astype('float32'), [2, 10, 4]), relay.reshape(const_10452.astype('float32'), [2, 10, 4]), ), 0)
call_10453 = relay.TupleGetItem(func_6292_call(relay.reshape(const_10452.astype('float32'), [2, 10, 4]), relay.reshape(const_10452.astype('float32'), [2, 10, 4]), ), 0)
func_791_call = mod.get_global_var('func_791')
func_792_call = mutated_mod.get_global_var('func_792')
call_10489 = func_791_call()
call_10490 = func_791_call()
func_6289_call = mod.get_global_var('func_6289')
func_6292_call = mutated_mod.get_global_var('func_6292')
call_10493 = relay.TupleGetItem(func_6289_call(relay.reshape(const_10452.astype('float32'), [2, 10, 4]), relay.reshape(const_10452.astype('float32'), [2, 10, 4]), ), 1)
call_10494 = relay.TupleGetItem(func_6292_call(relay.reshape(const_10452.astype('float32'), [2, 10, 4]), relay.reshape(const_10452.astype('float32'), [2, 10, 4]), ), 1)
func_4924_call = mod.get_global_var('func_4924')
func_4926_call = mutated_mod.get_global_var('func_4926')
call_10497 = func_4924_call()
call_10498 = func_4924_call()
bop_10503 = relay.multiply(call_10489.astype('uint64'), relay.reshape(call_10451.astype('uint64'), relay.shape_of(call_10489))) # shape=(1, 5, 9)
bop_10506 = relay.multiply(call_10490.astype('uint64'), relay.reshape(call_10453.astype('uint64'), relay.shape_of(call_10490))) # shape=(1, 5, 9)
output = relay.Tuple([call_10412,call_10438,const_10452,call_10493,call_10497,bop_10503,])
output2 = relay.Tuple([call_10413,call_10439,const_10452,call_10494,call_10498,bop_10506,])
func_10517 = relay.Function([], output)
mod['func_10517'] = func_10517
mod = relay.transform.InferType()(mod)
mutated_mod['func_10517'] = func_10517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10517_call = mutated_mod.get_global_var('func_10517')
call_10518 = func_10517_call()
output = call_10518
func_10519 = relay.Function([], output)
mutated_mod['func_10519'] = func_10519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10202_call = mod.get_global_var('func_10202')
func_10204_call = mutated_mod.get_global_var('func_10204')
call_10545 = func_10202_call()
call_10546 = func_10202_call()
func_10202_call = mod.get_global_var('func_10202')
func_10204_call = mutated_mod.get_global_var('func_10204')
call_10555 = func_10202_call()
call_10556 = func_10202_call()
var_10560 = relay.var("var_10560", dtype = "uint64", shape = (6, 5, 9))#candidate|10560|(6, 5, 9)|var|uint64
bop_10561 = relay.floor_mod(call_10545.astype('float64'), var_10560.astype('float64')) # shape=(6, 5, 9)
bop_10564 = relay.floor_mod(call_10546.astype('float64'), var_10560.astype('float64')) # shape=(6, 5, 9)
bop_10570 = relay.greater_equal(call_10545.astype('bool'), var_10560.astype('bool')) # shape=(6, 5, 9)
bop_10573 = relay.greater_equal(call_10546.astype('bool'), var_10560.astype('bool')) # shape=(6, 5, 9)
uop_10581 = relay.asinh(bop_10561.astype('float32')) # shape=(6, 5, 9)
uop_10583 = relay.asinh(bop_10564.astype('float32')) # shape=(6, 5, 9)
func_10123_call = mod.get_global_var('func_10123')
func_10126_call = mutated_mod.get_global_var('func_10126')
var_10585 = relay.var("var_10585", dtype = "int64", shape = (1120,))#candidate|10585|(1120,)|var|int64
call_10584 = relay.TupleGetItem(func_10123_call(relay.reshape(var_10585.astype('int64'), [56, 20])), 8)
call_10586 = relay.TupleGetItem(func_10126_call(relay.reshape(var_10585.astype('int64'), [56, 20])), 8)
uop_10589 = relay.exp(uop_10581.astype('float64')) # shape=(6, 5, 9)
uop_10591 = relay.exp(uop_10583.astype('float64')) # shape=(6, 5, 9)
func_8806_call = mod.get_global_var('func_8806')
func_8809_call = mutated_mod.get_global_var('func_8809')
var_10627 = relay.var("var_10627", dtype = "float32", shape = (585,))#candidate|10627|(585,)|var|float32
call_10626 = relay.TupleGetItem(func_8806_call(relay.reshape(var_10627.astype('float32'), [585,])), 5)
call_10628 = relay.TupleGetItem(func_8809_call(relay.reshape(var_10627.astype('float32'), [585,])), 5)
output = relay.Tuple([call_10555,bop_10570,call_10584,var_10585,uop_10589,call_10626,var_10627,])
output2 = relay.Tuple([call_10556,bop_10573,call_10586,var_10585,uop_10591,call_10628,var_10627,])
func_10636 = relay.Function([var_10560,var_10585,var_10627,], output)
mod['func_10636'] = func_10636
mod = relay.transform.InferType()(mod)
mutated_mod['func_10636'] = func_10636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10636_call = mutated_mod.get_global_var('func_10636')
var_10638 = relay.var("var_10638", dtype = "uint64", shape = (6, 5, 9))#candidate|10638|(6, 5, 9)|var|uint64
var_10639 = relay.var("var_10639", dtype = "int64", shape = (1120,))#candidate|10639|(1120,)|var|int64
var_10640 = relay.var("var_10640", dtype = "float32", shape = (585,))#candidate|10640|(585,)|var|float32
call_10637 = func_10636_call(var_10638,var_10639,var_10640,)
output = call_10637
func_10641 = relay.Function([var_10638,var_10639,var_10640,], output)
mutated_mod['func_10641'] = func_10641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3523_call = mod.get_global_var('func_3523')
func_3525_call = mutated_mod.get_global_var('func_3525')
call_10673 = relay.TupleGetItem(func_3523_call(), 0)
call_10674 = relay.TupleGetItem(func_3525_call(), 0)
output = call_10673
output2 = call_10674
func_10713 = relay.Function([], output)
mod['func_10713'] = func_10713
mod = relay.transform.InferType()(mod)
mutated_mod['func_10713'] = func_10713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10713_call = mutated_mod.get_global_var('func_10713')
call_10714 = func_10713_call()
output = call_10714
func_10715 = relay.Function([], output)
mutated_mod['func_10715'] = func_10715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1307_call = mod.get_global_var('func_1307')
func_1308_call = mutated_mod.get_global_var('func_1308')
call_10779 = relay.TupleGetItem(func_1307_call(), 0)
call_10780 = relay.TupleGetItem(func_1308_call(), 0)
func_1515_call = mod.get_global_var('func_1515')
func_1517_call = mutated_mod.get_global_var('func_1517')
var_10810 = relay.var("var_10810", dtype = "float32", shape = (990,))#candidate|10810|(990,)|var|float32
call_10809 = func_1515_call(relay.reshape(var_10810.astype('float32'), [10, 9, 11]))
call_10811 = func_1515_call(relay.reshape(var_10810.astype('float32'), [10, 9, 11]))
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_10812 = func_1803_call()
call_10813 = func_1803_call()
output = relay.Tuple([call_10779,call_10809,var_10810,call_10812,])
output2 = relay.Tuple([call_10780,call_10811,var_10810,call_10813,])
func_10821 = relay.Function([var_10810,], output)
mod['func_10821'] = func_10821
mod = relay.transform.InferType()(mod)
mutated_mod['func_10821'] = func_10821
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10822 = relay.var("var_10822", dtype = "float32", shape = (990,))#candidate|10822|(990,)|var|float32
func_10821_call = mutated_mod.get_global_var('func_10821')
call_10823 = func_10821_call(var_10822)
output = call_10823
func_10824 = relay.Function([var_10822], output)
mutated_mod['func_10824'] = func_10824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1737_call = mod.get_global_var('func_1737')
func_1739_call = mutated_mod.get_global_var('func_1739')
call_10846 = relay.TupleGetItem(func_1737_call(), 1)
call_10847 = relay.TupleGetItem(func_1739_call(), 1)
var_10848 = relay.var("var_10848", dtype = "uint64", shape = (6, 5, 9))#candidate|10848|(6, 5, 9)|var|uint64
bop_10849 = relay.minimum(call_10846.astype('uint32'), var_10848.astype('uint32')) # shape=(6, 5, 9)
bop_10852 = relay.minimum(call_10847.astype('uint32'), var_10848.astype('uint32')) # shape=(6, 5, 9)
output = bop_10849
output2 = bop_10852
func_10853 = relay.Function([var_10848,], output)
mod['func_10853'] = func_10853
mod = relay.transform.InferType()(mod)
var_10854 = relay.var("var_10854", dtype = "uint64", shape = (6, 5, 9))#candidate|10854|(6, 5, 9)|var|uint64
output = func_10853(var_10854)
func_10855 = relay.Function([var_10854], output)
mutated_mod['func_10855'] = func_10855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9794_call = mod.get_global_var('func_9794')
func_9795_call = mutated_mod.get_global_var('func_9795')
call_10869 = relay.TupleGetItem(func_9794_call(), 2)
call_10870 = relay.TupleGetItem(func_9795_call(), 2)
output = call_10869
output2 = call_10870
func_10879 = relay.Function([], output)
mod['func_10879'] = func_10879
mod = relay.transform.InferType()(mod)
output = func_10879()
func_10880 = relay.Function([], output)
mutated_mod['func_10880'] = func_10880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1845_call = mod.get_global_var('func_1845')
func_1846_call = mutated_mod.get_global_var('func_1846')
call_10916 = func_1845_call()
call_10917 = func_1845_call()
output = relay.Tuple([call_10916,])
output2 = relay.Tuple([call_10917,])
func_10920 = relay.Function([], output)
mod['func_10920'] = func_10920
mod = relay.transform.InferType()(mod)
mutated_mod['func_10920'] = func_10920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10920_call = mutated_mod.get_global_var('func_10920')
call_10921 = func_10920_call()
output = call_10921
func_10922 = relay.Function([], output)
mutated_mod['func_10922'] = func_10922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5071_call = mod.get_global_var('func_5071')
func_5073_call = mutated_mod.get_global_var('func_5073')
call_10983 = relay.TupleGetItem(func_5071_call(), 0)
call_10984 = relay.TupleGetItem(func_5073_call(), 0)
output = call_10983
output2 = call_10984
func_10994 = relay.Function([], output)
mod['func_10994'] = func_10994
mod = relay.transform.InferType()(mod)
output = func_10994()
func_10995 = relay.Function([], output)
mutated_mod['func_10995'] = func_10995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2958_call = mod.get_global_var('func_2958')
func_2959_call = mutated_mod.get_global_var('func_2959')
call_11018 = relay.TupleGetItem(func_2958_call(), 0)
call_11019 = relay.TupleGetItem(func_2959_call(), 0)
output = call_11018
output2 = call_11019
func_11034 = relay.Function([], output)
mod['func_11034'] = func_11034
mod = relay.transform.InferType()(mod)
mutated_mod['func_11034'] = func_11034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11034_call = mutated_mod.get_global_var('func_11034')
call_11035 = func_11034_call()
output = call_11035
func_11036 = relay.Function([], output)
mutated_mod['func_11036'] = func_11036
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11081 = relay.var("var_11081", dtype = "float32", shape = (15, 14, 11))#candidate|11081|(15, 14, 11)|var|float32
uop_11082 = relay.exp(var_11081.astype('float32')) # shape=(15, 14, 11)
func_10123_call = mod.get_global_var('func_10123')
func_10126_call = mutated_mod.get_global_var('func_10126')
var_11086 = relay.var("var_11086", dtype = "int64", shape = (1120,))#candidate|11086|(1120,)|var|int64
call_11085 = relay.TupleGetItem(func_10123_call(relay.reshape(var_11086.astype('int64'), [56, 20])), 7)
call_11087 = relay.TupleGetItem(func_10126_call(relay.reshape(var_11086.astype('int64'), [56, 20])), 7)
func_8190_call = mod.get_global_var('func_8190')
func_8194_call = mutated_mod.get_global_var('func_8194')
const_11089 = relay.const([[-1.975009,1.860554,7.743242,0.550745,3.253885,-5.269636,1.677536,-0.607577,-2.035402,2.674643,-1.003953,-1.408792,9.383261,0.297527,-5.227797,-9.373925,-7.848205,-5.130691,0.678010,6.566785],[-9.005210,-0.197063,1.648857,1.954412,-5.912141,-3.239293,-2.458378,6.802581,0.066087,8.674439,4.416100,-6.188669,-2.595420,0.972681,-8.055455,-8.497658,3.558061,4.309443,2.470387,-5.664068],[2.946105,-8.289892,4.563874,2.582839,9.486629,-1.514715,-7.650972,-1.774782,-7.732175,-6.192031,-5.073568,8.325791,0.951047,-5.090433,4.013562,-9.074239,-7.235638,-8.925732,7.535976,-3.857215],[-3.286875,7.317003,3.352922,1.661690,-1.673311,3.686123,-3.001138,-6.773396,1.628607,4.121312,9.018915,4.067044,-1.156841,2.932187,-1.971421,-2.425105,-3.158743,7.048095,9.039712,5.107889],[3.096492,8.646762,9.533645,7.049705,-6.507779,8.281088,2.970072,0.309147,-0.118937,2.297035,-6.462660,-9.809249,6.179364,3.366091,-5.413854,-5.068407,0.327566,-4.329790,1.972335,6.613090],[-3.996837,7.661046,7.254715,2.511152,0.539612,-8.320910,8.570169,8.992447,8.501079,5.970571,6.201090,9.080695,6.928172,-4.518438,4.385242,7.611057,-6.250232,5.610354,1.942549,-5.743902],[7.628313,3.752685,3.390301,-7.584266,3.853233,-4.766007,4.414749,3.670713,8.778468,-2.919733,0.376499,-8.095415,-1.219846,2.867187,1.984932,6.525012,5.406913,4.578448,9.806731,0.956822],[3.803530,7.070878,0.805705,-8.733123,-3.644365,9.481259,-5.937077,-5.577067,-4.091860,-7.920922,6.781391,-7.751101,-0.867680,1.301896,2.234530,-6.115738,-5.878728,-3.749958,-1.090981,6.583466],[3.482301,-3.722535,-0.314548,-9.413695,3.138642,-5.073189,-5.316407,9.290362,-3.248136,-2.041546,2.638979,5.950288,5.757440,1.226395,-0.710155,-5.811986,6.289662,2.808114,9.440341,-7.704522],[-0.706862,4.224837,-0.100407,-9.609117,5.349340,-2.980665,4.439295,0.890233,9.976574,6.761264,5.415198,0.222850,-0.517574,-3.678152,9.344227,-0.398594,-2.785786,-1.069971,-6.141446,8.267959],[-4.012446,-5.609110,2.374082,-7.988834,-2.112162,-2.191291,6.170590,5.571608,-2.760779,-1.861183,-2.771332,-6.148399,-5.708097,9.369416,6.025373,9.305391,7.237133,4.280037,8.719603,4.752114],[2.375619,8.158001,-9.875106,3.025167,-7.597477,-1.252144,-7.518511,4.534166,2.442990,-1.132666,-6.968453,-3.888612,6.165316,-9.721505,5.890930,8.419576,-5.346861,-0.888014,8.256926,1.541885],[0.881011,-6.740435,-7.072208,-7.934798,5.852022,-1.247202,-1.203199,8.688073,1.988569,-3.217461,8.688574,2.511941,-0.927665,-5.346680,1.145672,-1.544523,8.549537,1.058736,-9.458382,-2.094438],[-8.666734,9.693097,0.947909,-6.909495,3.149102,-8.575679,-6.479774,-4.569847,1.444644,-0.573704,-6.328589,5.825047,-8.202071,-5.396365,-8.925631,-5.853233,4.387125,-7.156908,-0.562639,6.776470],[9.782172,-2.744917,-4.975633,3.377938,-0.532191,-8.966234,-7.407526,-6.713902,-7.304062,8.576107,1.863705,8.170813,-3.581200,-6.538834,6.328049,-2.858743,9.706732,-2.060702,0.210837,7.721241],[-0.634163,-3.793895,4.751325,3.618679,2.843052,-9.883827,-0.826116,-7.879347,8.103722,2.707808,-1.599013,-3.300814,-2.489607,3.725799,-9.101904,6.644907,0.479492,0.938367,3.396975,-4.143012],[1.925653,9.309539,2.239957,-0.629745,-9.598859,8.408476,4.245822,-6.583388,-4.138709,9.952472,-6.135556,1.333322,8.694983,-1.696482,9.546262,9.787102,-4.018095,-6.731186,-4.305234,-6.473425],[-7.237624,-8.750726,9.817527,-8.596924,-1.884400,-6.219265,-8.254889,-2.136733,-9.933110,-0.894043,-1.179871,8.070602,7.604951,-3.405870,-1.782952,-7.784157,-3.459697,2.002193,-2.818684,5.920562],[1.984126,5.380880,-5.245370,6.709912,8.998253,-1.383243,-6.644318,-4.570853,-5.796596,9.387809,7.253053,8.993001,-5.985366,-0.004918,-8.004782,-3.582369,8.621249,-5.815146,0.055654,1.503376],[1.447714,-8.244531,7.408714,4.783158,2.048770,-1.074646,8.232232,-4.732939,-6.474924,-3.812125,5.078344,1.347748,-4.612947,-0.965463,4.673672,-9.139610,8.330168,-9.180052,4.058201,-8.099365],[2.510897,-4.498451,6.973006,-2.897409,1.864397,-6.002037,0.323508,2.363946,9.675544,-7.134360,9.054490,-0.475865,8.081178,2.895913,-2.418847,-8.300932,2.088432,-9.315305,2.511560,-4.227452],[5.249955,6.435732,-9.651313,2.008390,-5.479498,7.484063,-4.267235,7.865757,-2.908385,1.666301,-0.539014,-8.683802,-1.381805,-3.772633,-2.883118,-1.298296,-0.855360,-6.670533,-0.353790,-8.505449],[6.823564,0.169041,3.532843,-0.180595,5.927347,7.725105,6.487058,4.536275,-6.964488,4.782301,8.013787,5.541171,-6.127454,-4.661975,7.401754,0.349057,-1.359134,-0.490360,5.373429,-3.537536],[-1.858053,8.250109,4.597137,8.054696,-9.712047,-6.437833,-1.135807,6.480243,-8.451166,-8.350830,9.465253,-7.229820,-5.164704,5.597419,8.183788,-3.915017,2.934632,1.311624,3.106376,3.197858],[-8.565278,2.667654,4.586552,9.922336,-1.481265,3.064646,5.450246,-5.265653,-1.873116,-4.800908,3.219189,-2.082941,-9.126930,6.554350,-5.083230,0.587428,0.218787,-2.169834,-1.706549,-3.270107],[5.239874,-8.897241,5.459439,-0.838923,-6.220276,-4.049379,3.252856,4.881576,-5.250034,7.285440,9.797246,2.806825,1.360439,5.197770,9.759560,7.091850,6.637219,-0.990796,-9.964545,-6.031021],[6.224564,-7.512759,5.617551,-7.585119,-7.089506,8.865169,-1.064851,-0.831102,-5.715002,8.459909,5.376559,-4.941795,-4.728488,-7.868634,2.882683,-7.473081,2.492598,1.959022,-5.527644,-5.367829],[-5.510148,-9.965795,9.570371,-1.895126,-9.948096,0.301109,-8.946965,-4.911909,-8.968118,2.124586,3.648905,-6.483083,-1.409153,-2.734397,7.993572,-2.059813,-0.075245,5.511291,0.256668,1.960818],[3.365942,-0.356951,-9.622089,5.029297,4.588741,-6.935075,-9.112346,5.288219,-2.357836,3.867145,-7.763878,4.353980,-9.941995,-9.456208,7.809010,9.820062,2.969998,-8.457252,-2.319252,-3.098116],[8.830893,-6.342675,-2.046435,-6.020104,2.079821,-2.095770,1.280300,-1.001835,-9.356618,-6.085710,-3.384340,6.396825,2.606451,6.823482,4.103304,6.310773,-6.048403,-2.018431,9.346745,-0.031710],[-6.875100,-5.615055,-6.899606,4.497586,-5.150651,-7.012119,0.868906,-3.695962,-0.595779,-9.060161,0.972572,-7.895674,0.402726,-9.303258,0.707746,-3.380506,-7.141345,-0.544257,8.248222,4.144313],[9.331627,3.154407,3.530725,2.368915,2.107998,4.315514,6.539761,0.255875,-5.898896,4.533483,-6.597156,5.976661,-0.143709,6.786723,0.488761,6.229015,8.172810,1.652409,-2.745928,-0.579968],[-1.879107,1.673666,6.687343,0.800374,-0.487660,8.889586,-8.654627,0.016656,-0.759609,-9.452576,-0.027079,-5.981310,-0.361488,-7.100147,-0.474895,3.997588,4.910455,-9.445461,1.915922,-8.353456],[-3.579653,-9.553529,3.899359,-3.657231,-0.993456,3.570106,-5.157533,-7.155230,-2.542631,-7.160856,8.497920,2.797419,-9.103713,0.381444,5.846212,8.612155,-3.912674,-5.920199,-3.098314,5.608626],[-7.078870,8.127026,8.819226,1.904280,-7.436054,-7.182017,5.602112,-5.113734,-9.548306,5.311821,-4.110630,7.314991,-0.615268,-0.148175,-9.432800,-3.096269,-7.453220,-1.755871,2.229951,5.758019],[5.595543,-6.182944,-3.931704,-8.518961,-0.392394,-0.347887,-5.858266,7.266737,-5.407811,9.981534,-4.554587,5.658543,2.054308,-7.579164,9.128150,9.181313,4.109255,-1.541433,-8.296694,-7.694041],[-1.333471,2.783517,6.783091,-3.542321,-3.598359,-7.055052,7.903820,-5.674177,5.428815,3.838709,-1.846211,3.404007,-0.108802,1.724452,-0.685898,-0.848671,7.665256,-1.097555,-3.597855,-2.631526],[-4.156295,5.488298,-5.451429,4.035339,-8.046571,-6.430904,3.378860,9.833226,6.834279,-5.188631,-8.253497,2.923983,6.719844,-1.230228,-5.841762,-4.617097,-7.882462,-0.955770,4.899971,-9.893188],[-1.698840,7.430803,6.084557,-4.142861,4.474110,-4.700514,8.474931,4.087987,2.476631,-9.855786,-5.467348,8.275865,3.598170,5.184303,8.275236,-1.830028,0.103024,7.367060,-9.119672,4.245512],[-3.043426,-4.386965,3.793603,-3.672302,0.461549,-4.411689,-0.454876,-3.520633,3.888881,-3.792565,-4.814563,6.452983,-8.634093,-2.975369,-1.750839,8.894504,7.101532,-4.614097,4.231034,-6.032752],[6.146526,8.079222,-3.014182,0.529308,7.237559,-9.813061,5.636903,2.480644,-1.172153,-2.507051,-0.379546,9.284000,2.332581,-6.362218,7.801054,-6.849212,-1.076093,-1.684381,3.026230,-2.770380],[3.536299,-8.502677,-2.791062,1.478557,6.193600,8.483588,3.820438,-3.750138,-1.052650,3.156710,6.224157,8.834295,5.840486,-9.723872,8.988713,-7.190456,3.177388,4.029367,-2.184295,-6.407366],[0.745113,5.548479,-1.110900,3.931545,1.525714,-6.339990,-1.371369,-1.065798,8.407757,3.567040,7.807744,-5.511324,-1.517133,6.718056,-9.724861,3.955741,9.533995,-4.934460,-7.047750,2.011432],[-3.463683,-0.486426,5.947965,7.091647,5.736523,0.531805,-3.025332,5.914168,-5.262171,4.881810,-8.745028,-2.821652,-9.468397,0.378715,-3.891334,-9.877573,3.557018,-8.070573,8.924751,6.873694],[-4.256938,5.870154,-9.544950,5.304816,3.462468,0.809482,4.282453,-4.026455,-8.162525,-9.637683,-4.220938,-9.199238,2.024855,-2.380573,-7.243021,2.583931,-5.207762,7.660680,3.926934,5.732395],[5.588816,-6.590605,-4.555851,-5.045568,5.588680,-8.321084,7.345638,6.793931,5.402205,5.865404,9.611718,-7.531219,-3.950049,9.182941,-2.536952,-1.826145,6.942825,7.802466,4.120434,5.698680],[-4.712840,-9.326044,-3.453112,8.489226,1.603647,8.319119,6.012641,7.513174,8.138272,-9.847943,6.241305,4.114986,6.190345,7.062872,6.687792,8.714474,-3.368547,4.704387,8.272094,-4.279977],[-0.810682,-6.871419,2.521739,6.867671,-2.507350,-6.410305,-8.334121,-9.715123,-4.856907,3.953540,-1.461858,-1.026015,-6.664103,6.147569,-2.843329,0.607063,1.634781,-6.883715,8.310197,5.897551],[1.621305,2.771865,-5.664922,-3.780076,7.517936,-2.533337,-8.501246,-5.931375,-6.041602,2.822511,5.062800,4.866826,-5.972274,0.810688,1.370362,3.242411,2.098286,0.573146,-3.563122,-8.804304],[4.697521,-2.305140,1.039400,-7.304276,-4.188781,-3.441854,-4.715995,6.784616,-0.654369,-5.438875,8.954786,-8.820970,6.434386,-8.258965,2.743594,2.381636,7.686138,3.449776,0.305574,8.264597],[0.267745,7.494258,0.141033,-0.242373,-6.370863,-5.646243,-8.454844,-1.422602,-4.032789,3.787586,1.202382,-5.218971,-4.379536,-3.565824,2.691383,-9.151452,4.287565,7.059282,-5.238632,-1.387806],[-2.653699,-2.013728,-9.115876,-1.662010,-6.066111,-9.233975,5.430392,-3.594674,-0.918817,7.894822,-7.266279,-4.024573,8.234172,7.586529,1.476887,-6.221295,-8.392980,-6.293249,2.220851,0.066254],[0.982718,-1.511184,-8.138775,-6.261541,9.502882,-6.535769,3.126632,1.274424,-0.216189,-1.273383,6.136071,-8.213338,-2.265284,-7.412380,3.147925,6.188444,2.408625,0.371047,-3.233777,9.488421],[5.528096,-2.836661,-9.193115,-4.616454,-4.516776,9.589894,0.423222,0.801123,-0.821701,-2.828667,0.258845,-6.921258,0.439203,-6.320776,-6.287581,4.621261,2.738323,-4.325438,3.090622,0.448000],[-9.542200,2.512062,-0.093980,1.757834,-8.587984,-4.120897,8.677016,9.267807,4.189415,-6.427760,3.840144,7.132849,1.864157,-0.386168,-4.164327,-6.510376,-9.303512,0.843444,-6.605301,-6.057398],[-1.094490,-7.052171,7.069891,-2.043262,7.814759,-3.453483,-6.926624,-5.347817,-0.020683,-0.510814,-3.340258,7.087766,2.561448,8.864553,9.343768,-2.885443,-3.290385,0.861649,-3.893759,-1.905990],[-7.489377,-1.507314,3.468199,8.702454,-7.342621,-5.613276,-5.601419,9.184956,-1.457159,-5.796442,-6.032662,8.783046,7.567003,8.955672,-1.290107,-0.655590,-6.136848,8.741564,4.605102,1.173614],[4.715906,-4.335058,5.778938,7.070483,-3.170915,3.116767,-3.685541,5.030344,0.675135,-3.438570,7.924791,4.497851,6.142377,5.880583,2.301791,-7.832672,-0.906540,-8.127040,5.370027,-9.107463],[9.565270,-1.719060,-7.835621,-2.972872,-6.293760,-1.750997,4.463820,-0.670950,-3.926546,0.195561,-2.851059,-7.687853,-1.103849,8.868273,-2.226887,1.975930,0.368080,-4.714040,4.362242,-0.313369],[5.787644,2.812416,-4.260966,1.786900,6.245194,-2.173510,4.264605,3.986272,5.518374,5.099021,-5.763185,-3.628226,-4.932155,6.048082,0.839597,-9.788943,-7.246237,8.730392,2.497862,-1.643136],[1.634368,-0.910620,0.294182,-5.013635,-0.917492,5.520465,-8.674765,7.756611,-0.007521,-1.265045,-9.246126,-2.923836,4.337331,0.105314,-2.669599,6.908769,-9.275369,-3.800484,8.065564,-8.283418],[-0.859617,-3.639196,9.476875,-9.313181,5.756571,4.104541,4.274293,-3.725456,4.220792,3.966011,9.998654,3.880458,-8.478990,-3.744086,-3.234364,-9.461617,-1.214416,9.309531,-7.938269,5.120715],[5.492943,5.774754,-9.143740,5.449538,2.925032,2.595029,7.810918,-1.255745,2.008753,-0.188569,8.353553,-2.213641,1.080969,-3.254485,8.939329,1.633417,-7.160599,0.595781,6.710689,3.681162],[1.042903,1.733651,2.029253,9.975497,-0.110811,7.070188,-9.255261,6.328580,6.121354,3.931531,0.579607,4.569561,5.778100,-6.285311,1.473051,0.465623,7.313685,-0.406656,-2.480282,2.589621],[2.205430,-6.858880,-5.197732,3.520768,3.338792,2.339860,-8.885941,5.613753,8.662733,-8.473233,5.799122,-3.626893,-4.716829,9.188265,-9.457704,-8.180343,4.388972,1.259173,-2.576776,-8.414691],[9.838680,1.237980,-2.327205,3.119407,-2.639747,9.553871,8.100454,-8.431576,-3.021088,-4.951301,-8.584893,-3.408433,3.839555,-7.027091,-0.613245,-7.668097,-1.181305,6.782990,-5.890086,-1.458749],[-9.111541,-1.379225,1.680106,-1.922567,-2.997811,-5.153639,0.030548,2.718973,-2.789630,-0.726260,-0.319783,-9.442033,-6.954676,8.228036,-5.966499,-5.762854,7.620153,-3.121891,3.350393,-1.150867],[4.297486,0.318830,0.421514,-1.532267,-2.164868,2.267672,0.865278,7.866878,6.029090,-4.393632,-8.406011,8.002939,1.577470,1.679675,-6.489980,-4.735247,-5.650056,-0.558640,-6.872332,-8.472191],[0.566096,7.145597,1.960463,0.508066,-6.423626,1.153022,-1.713459,-0.684028,-4.696214,-4.740168,-7.336519,4.545415,-0.694709,-5.070410,-5.185372,1.555385,-9.374278,-4.135738,0.093229,6.813931],[5.821108,5.852177,4.150763,5.345635,5.149368,-3.690484,-6.191594,-4.337915,1.904627,-8.307538,1.735725,2.300975,-7.236755,-5.260022,3.651475,1.374996,-1.825617,-9.725132,8.827084,2.631074],[-8.905026,-2.525018,7.625358,2.725166,6.307692,-5.832434,-6.744067,8.030691,1.134990,-0.038301,1.570768,4.050749,-4.434483,0.060229,1.185890,-4.363710,-6.511467,5.710336,-3.886128,-9.141289],[-2.135674,-7.229580,-0.725647,6.482666,9.696078,4.079291,-3.519946,-2.409881,-0.687169,-0.155044,8.982234,0.340320,5.555692,5.012613,-3.314098,2.963254,2.743554,8.816350,9.680848,1.064586],[-6.840432,6.958771,-0.650939,-3.744525,7.016940,-3.390277,4.310403,-8.758474,-2.198697,-7.330538,5.706729,4.798466,-4.625229,9.440585,-8.699488,-5.069435,0.342483,2.966931,-6.677263,-9.525432],[-4.026545,-9.124409,6.985404,-9.676758,-0.238217,-9.482086,-9.502509,-4.089853,-2.056937,4.397561,3.157962,5.929707,9.447284,-9.984331,-6.665819,-8.006740,2.246285,5.839214,3.980823,2.585429],[-7.910625,-7.241883,3.046247,8.264550,-7.172888,-0.084881,0.839195,-2.938295,-7.779023,-6.898562,2.474854,8.831391,5.233128,0.782788,-9.861477,-8.161085,-6.925553,-1.219319,-5.722908,0.256564],[-3.214872,-1.622387,-9.763143,-1.767560,6.179836,1.565247,0.699181,9.441065,8.993491,-6.230988,9.728195,2.852316,7.512265,-3.089674,6.822606,-4.459097,4.601868,6.756516,8.870012,9.068887],[-3.780662,5.290745,8.344003,-1.208062,-6.486936,9.385970,-6.925907,5.310999,-3.447382,5.227346,-9.393343,8.127066,-3.913847,6.201678,-8.434344,-8.508187,0.893080,4.697534,-0.574272,-3.568340],[-8.687858,9.311094,-0.578697,-3.536525,-5.738599,-4.313185,6.416596,-7.744531,1.746561,9.561928,-7.810050,-2.395624,7.462505,7.132542,-7.307787,-6.746732,3.911262,3.275959,0.025641,-7.228150],[7.300755,-4.563973,-0.937493,-1.899077,-7.681626,9.470597,2.336163,-2.020519,5.918559,-4.333741,2.362815,-7.473309,-4.565071,-1.318073,4.085835,7.783974,-0.897751,8.536810,1.619078,-4.647626],[1.812362,-3.155543,0.921988,-6.688586,-9.308155,-8.366794,9.162825,-9.817579,-2.470248,8.674569,0.909369,-1.338719,-4.049920,-8.105634,0.323432,8.646330,0.667716,9.553590,2.321788,5.734279],[1.213389,9.336156,7.230741,-3.144668,1.441375,8.892125,2.638335,-9.787309,-5.248268,5.266521,0.544746,-9.806879,-1.864666,7.593601,3.777210,-1.765426,1.911658,-6.372310,7.769110,-8.537725],[-9.749635,-2.862032,-1.699868,-2.520122,2.737524,-6.752312,-0.423768,3.667066,8.766700,-3.811800,-9.618233,3.984787,2.931676,-6.021222,-9.291309,8.210668,-0.594333,-0.157590,-3.162634,7.514110],[-5.105183,-5.083303,8.208788,-2.156279,-5.925436,6.728814,4.682610,-9.857935,-4.153101,3.250302,-5.701549,-8.446810,-9.423778,5.803306,7.430580,9.931260,-3.615029,-8.068386,5.420170,-6.091732],[-5.592831,-0.499140,-9.006781,-3.537982,3.625777,-6.621620,-1.019902,4.883330,9.600984,0.447068,0.632722,0.304997,-3.589988,1.487716,-1.211887,6.176970,-1.834522,-2.754710,5.135726,4.563684],[-3.552462,-2.341763,-3.192498,-8.830218,-6.753283,-9.862225,-1.093808,2.848407,-6.845183,-5.817578,3.715025,4.703062,-0.259554,-0.022218,-4.092071,-4.948093,8.377575,1.548077,-3.891278,-3.409776],[2.636381,9.955328,-0.922803,-0.355308,5.445655,3.071321,-0.048758,-5.138305,-3.036725,-4.828570,7.556845,4.628049,2.259773,-7.269431,-3.237855,-8.078626,-4.512019,5.129703,4.285392,1.061677],[3.905348,8.264399,7.417884,-1.168834,-8.695143,-0.731070,9.202359,4.679855,-7.777942,7.363921,-1.629848,-6.731767,5.219542,8.011606,6.561825,4.355529,8.189728,-4.337726,2.873407,-9.093775],[-6.538005,9.914510,-0.116081,-9.052445,-0.045756,-1.558307,-5.580137,2.365319,-8.408607,-5.191195,7.967033,-3.425647,-2.765460,3.755447,0.451517,8.052277,-2.029777,-6.162115,3.158430,8.407876],[-2.353283,-8.527538,-9.387866,-0.046824,-3.959164,-5.635695,-9.217015,-8.074769,-4.353787,-0.163341,9.031231,4.541549,-2.049584,7.308741,-6.839684,-7.901267,-1.737846,7.116392,-6.287323,6.209549],[-9.387208,0.820068,4.432264,1.209628,9.319854,0.053703,-0.242509,6.859960,-9.119411,-8.088985,7.661168,2.473937,-1.584878,3.667148,-4.792604,5.336274,-1.158670,-3.057762,1.962462,5.144415],[7.422504,2.182536,5.495142,1.016070,1.341819,6.528523,-6.898559,-3.277445,9.776632,5.206134,4.389900,3.785756,4.762997,6.207233,6.429373,-0.638505,9.267031,-4.126522,-8.767507,7.988537],[-9.400498,-2.361535,6.415163,9.407762,-1.667933,4.277926,7.349912,-9.089746,-4.613090,7.084017,-3.026621,-9.268885,-1.565445,5.856403,-5.484691,-1.782591,7.258774,0.446885,-0.149233,1.225395],[-5.849813,-5.659364,1.141367,-7.400579,-7.517602,-0.471877,2.558703,-1.760023,9.933748,-6.409352,-9.022487,-6.635506,-7.169766,3.257018,-8.254534,9.886982,0.543940,5.863546,-8.687476,-9.741967],[2.147668,-3.058607,9.427880,-4.260216,-0.234776,7.757649,-0.238448,-2.459067,8.276713,6.028449,-7.593929,-6.150076,-4.574585,5.327961,-5.177135,9.723506,-3.915782,-0.441015,-9.480731,-2.838499],[-5.460064,-9.318845,-1.062558,4.684374,-6.146525,0.828565,5.086151,-5.663340,0.193354,4.349351,6.051853,-8.639641,-2.062012,2.611341,3.128054,1.806347,1.386253,-7.914263,-4.372457,-5.624371],[-7.272124,5.984603,3.503050,9.894337,3.011367,-9.429171,3.385400,-9.898293,-4.958092,5.149554,-0.815981,0.159485,-6.161393,0.994018,5.872029,5.462209,1.456035,6.228216,-9.078831,-4.710574]], dtype = "float32")#candidate|11089|(96, 20)|const|float32
call_11088 = relay.TupleGetItem(func_8190_call(relay.reshape(const_11089.astype('float32'), [15, 16, 8]), relay.reshape(const_11089.astype('float32'), [15, 16, 8]), ), 1)
call_11090 = relay.TupleGetItem(func_8194_call(relay.reshape(const_11089.astype('float32'), [15, 16, 8]), relay.reshape(const_11089.astype('float32'), [15, 16, 8]), ), 1)
func_7855_call = mod.get_global_var('func_7855')
func_7858_call = mutated_mod.get_global_var('func_7858')
var_11095 = relay.var("var_11095", dtype = "float32", shape = (63,))#candidate|11095|(63,)|var|float32
const_11096 = relay.const([[5.507378,5.076396,9.491890,-4.124920,6.306870,9.547692,-0.637284,8.904812,3.893880,0.415886,-9.540199,-9.611622,-8.642489,-8.162402,8.395095,-5.621046,5.539635,0.063290,-6.615144,2.866163,8.363136,0.848789,-1.431197,-9.907446,-1.268409,-7.954118,-7.754562,7.666882,2.164528,9.913322,0.832324,9.966088,7.946976,2.606760,4.718708,8.400186,9.971003,-1.832277,0.416401,-3.612896,4.363879,6.713719,5.835289,-7.377200,-8.359551,1.656616,0.821963,-0.090069,6.834913,-6.191464,-2.912443,-2.384124,-4.043094,-9.756016,6.560538,-4.134636,5.659696,-5.825120,-6.428422,4.223623,-5.490254,7.017191,-7.738245,-5.876370,4.629089,-5.273638,-1.200690,-6.099775,9.304169,6.395437,3.129075,1.608058,5.992352,6.224391,1.667653,-7.192914,3.898375,5.236578,-2.043283,-0.634685,7.038780,6.608728,6.141034,-2.282369,-2.073142,0.152806,7.304120,3.727158,4.401411,2.133632,0.168496,-5.174413,7.779706,-4.605027,-8.133611,9.258219,5.072592,6.426243,-3.973242,-1.693502,0.117282,-3.036471,-6.626790,9.504876,-0.176773,-5.897769,8.276482,9.974112,6.913368,-4.216861,-0.379678,8.851022,-3.823884,-4.925822,-0.052789,-9.974231,-8.649471,1.584836,-5.088156,-9.825737,8.880078,-9.179238,-5.192086,2.244289,-7.157331,1.645101,3.868934,-6.246551,7.248077,3.344421,4.535353,-6.037885,-9.640911,9.924772,-9.122140,-5.050552,-7.017645,-3.064901,-0.013560,-9.481684,6.971107,1.193130,-5.202491,6.094798,-6.592656,-4.635875,-2.196846,4.673190,-2.692699,4.476839,6.349913,-4.919045,-9.032135,-0.239492,-2.289307,8.492568,-0.112419,-1.586523,8.758257,-2.518315,-9.409687,8.775586,6.145164,-2.577117,3.588937,1.692116,6.540960,8.234443,-8.784009,-0.449851,-9.924361,0.236966,-4.912935,-8.701414,7.154951,6.674666,4.496759,-8.179022,7.470308,-8.717590,-6.911298,5.853855,2.495502,4.725399,-4.547205,-1.085962,-6.889252,8.971111,4.136133,-8.963896,1.598405,7.581330,-8.971341,9.582756,-4.029983,0.289435,3.376515,-7.249251,9.734156,3.831486,4.559098,-7.628040,7.555502,-9.304243,3.399369,6.767431,-6.717656,7.464046,-3.532817,-2.672155,-7.513726,3.732033,8.965892,-5.417167,6.768638,-4.287961,6.686245,-5.270382,0.864135,-5.525063,8.062639,8.130472,-6.078868,2.628490,1.140352,9.483509,0.429312,-8.039915,-6.549550,2.644898,-0.988691,-2.986844,-0.802891,-9.135936,7.054182,0.530271,-8.624514,-8.576118,6.857697,6.171831,6.108940,6.040580,1.508867,0.756903,-0.424094,9.549020,5.607462,1.980588,7.725482,4.473678,-4.579449,5.809730,3.434576,8.538179,4.914904,7.553402,8.611422,5.919771,-3.832307,-2.943290,1.128186,3.877550,7.610154,8.347834,-5.076926,8.043267,7.514423,9.701975,-8.222642,9.274453,8.943961,-8.424310,2.034836,7.245325,3.737767,0.878406,-7.420029,8.011078,6.522532,-7.162264,4.898541,-1.911462,-5.504684,6.171492,-1.702967,1.977662,0.414856,-4.565832,5.986962,1.001427,1.774268,-7.004292,1.807078,7.064597,-3.257107,7.882603,2.620061,-5.887510,5.578701,-7.842972,-1.430186,-8.137508,7.506103,4.937954,-7.629390,9.070287,3.971040,2.337070,6.427859,4.308701,-8.000834,9.929381,-3.596283,-7.324582,2.845751,6.715633,-1.018156,-6.532277,-1.293500,-4.542791,-2.541738,-2.499526,5.196760,-9.746041,-7.260566,-6.780229,-8.811431,-2.529162,3.593836,7.721961,1.396878,1.869715,-6.340619,7.831738,2.719487,1.696435,-5.110601,9.733389,-8.610554,-4.650443,9.523284,9.764032,5.541248,-5.496955,-4.162310,5.225584,-3.011432,9.303867,-0.801209,4.120821,3.700964,2.844985,-9.023192,1.131095,0.923705,0.969263,3.379534,-9.186553,-4.869216,6.765401,-5.414999,-5.893517,1.753806,5.538590,-2.823870,5.069539,-7.399838,3.688327,8.600004,9.117510,8.651700,7.942369,5.612077,9.516946,-2.491737,2.654911,3.662422,7.045792,0.757948,6.880816,4.022914,7.941712,7.901929,-9.247494,-0.269964,0.401571,-5.019539,-0.626311,9.153693,1.497239,-3.663025,-7.296950,-9.203134,6.964564,6.085903,-4.528772,4.618864,-3.200260,-7.641899,-1.089562,-7.405339,-1.921754,-1.248795,-1.378827,-0.262425,-0.221240,-0.706954,1.744231,-7.786483,3.417214,6.444194,9.871171,8.969924,1.183647,-2.282805,-2.553576,-2.621993,-0.815106,8.188018,-9.472443,-4.425277,2.775970,3.063160,-5.565645,7.531767,8.703061,6.674179,9.259843,-9.572113,-7.056937,-4.048107,3.842156,-5.051591,-9.147970,5.624010,3.982363,3.206637,-4.336311,0.749167,-9.059948,-1.549152,3.501416,-5.041972,4.880989,-0.100750,-1.263966,-0.468359,5.106317,1.284120,2.100239,-4.171451,-2.652039,4.390648,-9.136575,0.541851,1.672839,1.786404,8.763207,0.913374,-0.741746,2.063430,3.613208,5.872097,-3.786326,-7.939846,6.161373,-5.083549,-5.484204,-0.113639,6.777349,4.272480,-5.597449,4.005865,9.430674,-6.768900,-1.480372,-4.808147,2.079005,-3.214903,-1.796247,0.166286,4.905595,7.583608,8.137327,2.594953,-0.949675,0.045728,7.597280,-7.640113,-1.048704,-8.092874,-2.017585,-2.272451,-0.209077,3.896568,8.299163,-9.971102,8.833615,-4.662628,-2.772871,2.420175,-9.620580,2.345430,1.986541,-8.271661,-3.345569,0.059768,1.859852,-9.192908,-3.345572,-8.065701,0.512088,7.858152,4.560004,0.888002,8.602004,-6.364031,-4.961742,7.078560,7.205386,9.065634,-6.159787,6.797334,-8.684442,-5.417201,6.980073,-9.810665,8.697226,3.299342,2.487228,-1.329043,7.161613,-2.807699,-6.405951,-8.597382,-4.361308,2.450237,-1.440027,-4.202047,8.466732,9.317595,-4.247779,5.409566,9.598938,-1.247043,3.044339,1.934738,9.935421,-0.466716,1.374419,9.059942,-6.529876,1.042487,2.308101,5.450172,-6.435062,-7.763974,-5.702036,-8.300491,-2.099199,-3.037137,-1.887689,0.675032,-1.805594,6.791415,-8.849015,2.282256,-6.330316,9.807523,-5.467651,-6.068356,3.959504,8.000172,-5.816489,-3.715862,-5.260814,-8.345468,-3.561855,-1.356689,-6.874089,1.050006,0.126252,6.529729,7.736366,2.775928]], dtype = "float32")#candidate|11096|(1, 585)|const|float32
call_11094 = relay.TupleGetItem(func_7855_call(relay.reshape(var_11095.astype('float32'), [63,]), relay.reshape(const_11096.astype('float32'), [195, 3]), ), 2)
call_11097 = relay.TupleGetItem(func_7858_call(relay.reshape(var_11095.astype('float32'), [63,]), relay.reshape(const_11096.astype('float32'), [195, 3]), ), 2)
uop_11109 = relay.sin(uop_11082.astype('float64')) # shape=(15, 14, 11)
bop_11120 = relay.power(uop_11109.astype('float32'), relay.reshape(var_11081.astype('float32'), relay.shape_of(uop_11109))) # shape=(15, 14, 11)
output = relay.Tuple([call_11085,var_11086,call_11088,const_11089,call_11094,var_11095,const_11096,bop_11120,])
output2 = relay.Tuple([call_11087,var_11086,call_11090,const_11089,call_11097,var_11095,const_11096,bop_11120,])
func_11123 = relay.Function([var_11081,var_11086,var_11095,], output)
mod['func_11123'] = func_11123
mod = relay.transform.InferType()(mod)
mutated_mod['func_11123'] = func_11123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11123_call = mutated_mod.get_global_var('func_11123')
var_11125 = relay.var("var_11125", dtype = "float32", shape = (15, 14, 11))#candidate|11125|(15, 14, 11)|var|float32
var_11126 = relay.var("var_11126", dtype = "int64", shape = (1120,))#candidate|11126|(1120,)|var|int64
var_11127 = relay.var("var_11127", dtype = "float32", shape = (63,))#candidate|11127|(63,)|var|float32
call_11124 = func_11123_call(var_11125,var_11126,var_11127,)
output = call_11124
func_11128 = relay.Function([var_11125,var_11126,var_11127,], output)
mutated_mod['func_11128'] = func_11128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4624_call = mod.get_global_var('func_4624')
func_4625_call = mutated_mod.get_global_var('func_4625')
call_11305 = relay.TupleGetItem(func_4624_call(), 2)
call_11306 = relay.TupleGetItem(func_4625_call(), 2)
func_2747_call = mod.get_global_var('func_2747')
func_2749_call = mutated_mod.get_global_var('func_2749')
var_11322 = relay.var("var_11322", dtype = "float64", shape = (360,))#candidate|11322|(360,)|var|float64
call_11321 = relay.TupleGetItem(func_2747_call(relay.reshape(var_11322.astype('float64'), [8, 5, 9])), 0)
call_11323 = relay.TupleGetItem(func_2749_call(relay.reshape(var_11322.astype('float64'), [8, 5, 9])), 0)
output = relay.Tuple([call_11305,call_11321,var_11322,])
output2 = relay.Tuple([call_11306,call_11323,var_11322,])
func_11326 = relay.Function([var_11322,], output)
mod['func_11326'] = func_11326
mod = relay.transform.InferType()(mod)
mutated_mod['func_11326'] = func_11326
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11327 = relay.var("var_11327", dtype = "float64", shape = (360,))#candidate|11327|(360,)|var|float64
func_11326_call = mutated_mod.get_global_var('func_11326')
call_11328 = func_11326_call(var_11327)
output = call_11328
func_11329 = relay.Function([var_11327], output)
mutated_mod['func_11329'] = func_11329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4270_call = mod.get_global_var('func_4270')
func_4272_call = mutated_mod.get_global_var('func_4272')
call_11337 = relay.TupleGetItem(func_4270_call(), 1)
call_11338 = relay.TupleGetItem(func_4272_call(), 1)
output = call_11337
output2 = call_11338
func_11352 = relay.Function([], output)
mod['func_11352'] = func_11352
mod = relay.transform.InferType()(mod)
output = func_11352()
func_11353 = relay.Function([], output)
mutated_mod['func_11353'] = func_11353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8970_call = mod.get_global_var('func_8970')
func_8971_call = mutated_mod.get_global_var('func_8971')
call_11365 = relay.TupleGetItem(func_8970_call(), 1)
call_11366 = relay.TupleGetItem(func_8971_call(), 1)
output = relay.Tuple([call_11365,])
output2 = relay.Tuple([call_11366,])
func_11369 = relay.Function([], output)
mod['func_11369'] = func_11369
mod = relay.transform.InferType()(mod)
mutated_mod['func_11369'] = func_11369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11369_call = mutated_mod.get_global_var('func_11369')
call_11370 = func_11369_call()
output = call_11370
func_11371 = relay.Function([], output)
mutated_mod['func_11371'] = func_11371
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11374 = relay.var("var_11374", dtype = "uint64", shape = (6, 1, 12))#candidate|11374|(6, 1, 12)|var|uint64
const_11375 = relay.const([[[-5,4,9,-3,8,8,2,7,-7,-5,-6,-6]],[[10,8,-1,-5,-6,-6,8,-9,-5,-6,-6,-3]],[[1,4,6,6,3,9,8,10,-4,-10,-8,-1]],[[-7,-4,-1,4,4,9,-7,8,-8,-3,3,-4]],[[-2,1,5,-6,6,-3,-6,9,6,-2,3,-2]],[[8,-1,1,-10,-10,-6,1,-5,-10,6,-7,6]]], dtype = "uint64")#candidate|11375|(6, 1, 12)|const|uint64
bop_11376 = relay.right_shift(var_11374.astype('uint64'), relay.reshape(const_11375.astype('uint64'), relay.shape_of(var_11374))) # shape=(6, 1, 12)
func_4020_call = mod.get_global_var('func_4020')
func_4022_call = mutated_mod.get_global_var('func_4022')
var_11382 = relay.var("var_11382", dtype = "float64", shape = (14, 165))#candidate|11382|(14, 165)|var|float64
call_11381 = relay.TupleGetItem(func_4020_call(relay.reshape(var_11382.astype('float64'), [11, 14, 15])), 1)
call_11383 = relay.TupleGetItem(func_4022_call(relay.reshape(var_11382.astype('float64'), [11, 14, 15])), 1)
var_11398 = relay.var("var_11398", dtype = "float64", shape = (14, 165))#candidate|11398|(14, 165)|var|float64
bop_11399 = relay.mod(var_11382.astype('float32'), relay.reshape(var_11398.astype('float32'), relay.shape_of(var_11382))) # shape=(14, 165)
output = relay.Tuple([bop_11376,call_11381,bop_11399,])
output2 = relay.Tuple([bop_11376,call_11383,bop_11399,])
func_11402 = relay.Function([var_11374,var_11382,var_11398,], output)
mod['func_11402'] = func_11402
mod = relay.transform.InferType()(mod)
mutated_mod['func_11402'] = func_11402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11402_call = mutated_mod.get_global_var('func_11402')
var_11404 = relay.var("var_11404", dtype = "uint64", shape = (6, 1, 12))#candidate|11404|(6, 1, 12)|var|uint64
var_11405 = relay.var("var_11405", dtype = "float64", shape = (14, 165))#candidate|11405|(14, 165)|var|float64
var_11406 = relay.var("var_11406", dtype = "float64", shape = (14, 165))#candidate|11406|(14, 165)|var|float64
call_11403 = func_11402_call(var_11404,var_11405,var_11406,)
output = call_11403
func_11407 = relay.Function([var_11404,var_11405,var_11406,], output)
mutated_mod['func_11407'] = func_11407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5351_call = mod.get_global_var('func_5351')
func_5353_call = mutated_mod.get_global_var('func_5353')
call_11484 = func_5351_call()
call_11485 = func_5351_call()
func_6799_call = mod.get_global_var('func_6799')
func_6801_call = mutated_mod.get_global_var('func_6801')
var_11500 = relay.var("var_11500", dtype = "int32", shape = ())#candidate|11500|()|var|int32
call_11499 = relay.TupleGetItem(func_6799_call(relay.reshape(var_11500.astype('int32'), [])), 5)
call_11501 = relay.TupleGetItem(func_6801_call(relay.reshape(var_11500.astype('int32'), [])), 5)
output = relay.Tuple([call_11484,call_11499,var_11500,])
output2 = relay.Tuple([call_11485,call_11501,var_11500,])
func_11523 = relay.Function([var_11500,], output)
mod['func_11523'] = func_11523
mod = relay.transform.InferType()(mod)
mutated_mod['func_11523'] = func_11523
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11524 = relay.var("var_11524", dtype = "int32", shape = ())#candidate|11524|()|var|int32
func_11523_call = mutated_mod.get_global_var('func_11523')
call_11525 = func_11523_call(var_11524)
output = call_11525
func_11526 = relay.Function([var_11524], output)
mutated_mod['func_11526'] = func_11526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2290_call = mod.get_global_var('func_2290')
func_2291_call = mutated_mod.get_global_var('func_2291')
call_11607 = func_2290_call()
call_11608 = func_2290_call()
output = call_11607
output2 = call_11608
func_11610 = relay.Function([], output)
mod['func_11610'] = func_11610
mod = relay.transform.InferType()(mod)
output = func_11610()
func_11611 = relay.Function([], output)
mutated_mod['func_11611'] = func_11611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4924_call = mod.get_global_var('func_4924')
func_4926_call = mutated_mod.get_global_var('func_4926')
call_11622 = func_4924_call()
call_11623 = func_4924_call()
func_9384_call = mod.get_global_var('func_9384')
func_9386_call = mutated_mod.get_global_var('func_9386')
call_11636 = func_9384_call()
call_11637 = func_9384_call()
func_4118_call = mod.get_global_var('func_4118')
func_4119_call = mutated_mod.get_global_var('func_4119')
call_11641 = relay.TupleGetItem(func_4118_call(), 0)
call_11642 = relay.TupleGetItem(func_4119_call(), 0)
func_2643_call = mod.get_global_var('func_2643')
func_2644_call = mutated_mod.get_global_var('func_2644')
call_11659 = relay.TupleGetItem(func_2643_call(), 0)
call_11660 = relay.TupleGetItem(func_2644_call(), 0)
output = relay.Tuple([call_11622,call_11636,call_11641,call_11659,])
output2 = relay.Tuple([call_11623,call_11637,call_11642,call_11660,])
func_11663 = relay.Function([], output)
mod['func_11663'] = func_11663
mod = relay.transform.InferType()(mod)
mutated_mod['func_11663'] = func_11663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11663_call = mutated_mod.get_global_var('func_11663')
call_11664 = func_11663_call()
output = call_11664
func_11665 = relay.Function([], output)
mutated_mod['func_11665'] = func_11665
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11679 = relay.var("var_11679", dtype = "int8", shape = ())#candidate|11679|()|var|int8
const_11680 = relay.const([[[8,7,8],[6,5,7],[-8,4,5],[-5,10,-8],[7,5,8],[7,-1,9],[8,7,7],[1,-7,7],[10,9,-1],[8,-6,1],[-9,1,1],[-9,7,-4]],[[2,-10,-10],[-2,-10,-10],[-7,-10,1],[8,-8,-2],[-9,9,1],[-10,9,-3],[-8,1,8],[-8,-2,-8],[10,5,-5],[8,-1,9],[2,-4,-9],[2,-4,5]],[[6,6,4],[1,8,-5],[-4,-6,-9],[7,-2,2],[10,9,9],[-5,-9,-1],[3,-8,-9],[-5,-5,-7],[5,6,5],[-1,4,-8],[-3,-7,3],[5,1,8]],[[-6,10,3],[-6,1,8],[-3,-2,8],[-1,-2,3],[-6,1,2],[5,4,1],[-5,8,2],[4,4,2],[6,2,2],[3,-4,3],[-6,5,-6],[-7,-3,6]],[[2,1,-6],[7,8,1],[-5,-6,-1],[-4,-7,-6],[3,-3,8],[-2,-9,-6],[7,8,7],[3,-4,-2],[8,-1,-4],[10,-10,-8],[2,1,-2],[-6,-4,-4]],[[4,4,6],[2,-1,1],[-9,5,-5],[10,-2,1],[-9,4,-3],[-4,-6,4],[4,6,-10],[1,1,1],[-10,3,3],[7,-3,5],[1,-3,-10],[7,-5,-9]],[[1,4,-5],[-7,-5,8],[-6,-10,-8],[-3,8,4],[-2,-2,-5],[10,9,7],[9,1,-4],[-4,4,7],[10,-10,5],[6,6,-2],[7,6,-8],[-1,5,-2]],[[3,-1,-9],[10,10,8],[4,3,-10],[-9,-1,-4],[-8,-5,-9],[3,-3,10],[3,-1,-9],[-8,-3,-5],[10,-1,-10],[9,1,10],[10,-5,-8],[-7,6,5]],[[9,10,-8],[8,-8,-8],[-5,6,-10],[-10,-10,5],[10,2,-2],[-1,10,-6],[8,-6,-2],[-5,-9,4],[9,-10,-7],[-8,9,-2],[7,-5,-7],[-7,2,1]],[[8,-2,9],[6,10,-9],[-3,5,-7],[4,-10,-2],[9,-4,-1],[-6,3,7],[5,-1,1],[1,7,9],[-3,-7,-1],[2,6,-10],[10,-7,-5],[-6,8,-5]],[[-7,7,2],[-7,7,8],[3,-10,5],[-10,-8,-10],[3,-5,-3],[-2,-5,-4],[2,-2,5],[9,-1,1],[-10,2,7],[-3,8,-1],[-8,-1,9],[2,7,2]],[[-5,4,-3],[3,-3,3],[9,-10,4],[9,-4,5],[-8,-7,-10],[-8,4,-2],[-4,-8,1],[9,-9,-8],[10,-5,8],[8,-8,10],[5,-6,10],[6,2,-3]],[[5,-3,-10],[-7,8,5],[-5,-9,-1],[4,7,-7],[-5,-10,-6],[2,-6,-6],[-7,7,9],[1,-8,-9],[-9,4,-3],[2,-1,7],[-7,9,-3],[2,-1,5]],[[-2,6,-7],[6,9,4],[9,10,-10],[7,5,3],[-2,9,-3],[-1,-1,6],[1,-3,-1],[2,3,-2],[-10,-4,-7],[-4,1,10],[8,-10,8],[6,-7,-2]],[[6,-2,8],[5,3,3],[-4,8,-10],[1,10,6],[9,-9,-9],[-9,-5,-7],[5,10,-9],[9,-2,3],[3,-10,7],[-1,6,-7],[1,3,6],[-8,9,-8]],[[-3,-4,-2],[-6,2,8],[-10,8,-6],[-2,-2,2],[4,-7,-10],[-3,-2,7],[-5,8,7],[-7,-2,-4],[1,-5,2],[8,-7,-8],[2,9,8],[7,-9,9]]], dtype = "int8")#candidate|11680|(16, 12, 3)|const|int8
bop_11681 = relay.less(var_11679.astype('bool'), const_11680.astype('bool')) # shape=(16, 12, 3)
output = relay.Tuple([bop_11681,])
output2 = relay.Tuple([bop_11681,])
func_11685 = relay.Function([var_11679,], output)
mod['func_11685'] = func_11685
mod = relay.transform.InferType()(mod)
mutated_mod['func_11685'] = func_11685
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11686 = relay.var("var_11686", dtype = "int8", shape = ())#candidate|11686|()|var|int8
func_11685_call = mutated_mod.get_global_var('func_11685')
call_11687 = func_11685_call(var_11686)
output = call_11687
func_11688 = relay.Function([var_11686], output)
mutated_mod['func_11688'] = func_11688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6976_call = mod.get_global_var('func_6976')
func_6978_call = mutated_mod.get_global_var('func_6978')
call_11692 = func_6976_call()
call_11693 = func_6976_call()
output = relay.Tuple([call_11692,])
output2 = relay.Tuple([call_11693,])
func_11710 = relay.Function([], output)
mod['func_11710'] = func_11710
mod = relay.transform.InferType()(mod)
output = func_11710()
func_11711 = relay.Function([], output)
mutated_mod['func_11711'] = func_11711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3883_call = mod.get_global_var('func_3883')
func_3884_call = mutated_mod.get_global_var('func_3884')
call_11740 = func_3883_call()
call_11741 = func_3883_call()
output = call_11740
output2 = call_11741
func_11774 = relay.Function([], output)
mod['func_11774'] = func_11774
mod = relay.transform.InferType()(mod)
mutated_mod['func_11774'] = func_11774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11774_call = mutated_mod.get_global_var('func_11774')
call_11775 = func_11774_call()
output = call_11775
func_11776 = relay.Function([], output)
mutated_mod['func_11776'] = func_11776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7687_call = mod.get_global_var('func_7687')
func_7688_call = mutated_mod.get_global_var('func_7688')
call_11799 = relay.TupleGetItem(func_7687_call(), 0)
call_11800 = relay.TupleGetItem(func_7688_call(), 0)
output = relay.Tuple([call_11799,])
output2 = relay.Tuple([call_11800,])
func_11836 = relay.Function([], output)
mod['func_11836'] = func_11836
mod = relay.transform.InferType()(mod)
mutated_mod['func_11836'] = func_11836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11836_call = mutated_mod.get_global_var('func_11836')
call_11837 = func_11836_call()
output = call_11837
func_11838 = relay.Function([], output)
mutated_mod['func_11838'] = func_11838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10393_call = mod.get_global_var('func_10393')
func_10394_call = mutated_mod.get_global_var('func_10394')
call_11859 = func_10393_call()
call_11860 = func_10393_call()
func_4543_call = mod.get_global_var('func_4543')
func_4545_call = mutated_mod.get_global_var('func_4545')
call_11864 = func_4543_call()
call_11865 = func_4543_call()
output = relay.Tuple([call_11859,call_11864,])
output2 = relay.Tuple([call_11860,call_11865,])
func_11896 = relay.Function([], output)
mod['func_11896'] = func_11896
mod = relay.transform.InferType()(mod)
output = func_11896()
func_11897 = relay.Function([], output)
mutated_mod['func_11897'] = func_11897
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11898 = relay.var("var_11898", dtype = "bool", shape = (11, 9, 3))#candidate|11898|(11, 9, 3)|var|bool
const_11899 = relay.const([[[True,True,False],[True,False,False],[False,False,True],[True,False,True],[False,True,False],[False,False,False],[False,False,True],[True,False,False],[False,True,False]],[[False,True,False],[True,False,True],[True,True,True],[True,True,False],[True,False,False],[False,True,True],[True,True,True],[True,True,True],[False,False,True]],[[False,True,False],[True,True,False],[True,False,False],[False,False,False],[True,True,True],[True,False,False],[False,True,True],[True,False,False],[True,True,True]],[[False,True,False],[False,True,True],[False,False,False],[False,True,True],[True,True,True],[True,True,False],[False,False,True],[False,False,False],[True,False,False]],[[True,True,True],[True,True,False],[True,True,True],[False,False,False],[False,False,True],[True,True,True],[False,False,False],[True,True,False],[False,True,True]],[[False,True,True],[False,False,False],[True,True,True],[True,False,True],[False,False,True],[False,True,True],[False,False,True],[True,True,True],[True,False,False]],[[True,False,False],[False,False,True],[True,False,True],[True,True,True],[True,False,True],[False,False,False],[True,True,True],[False,True,True],[True,False,False]],[[True,True,False],[True,False,False],[True,True,False],[False,False,False],[False,False,True],[True,True,True],[False,True,False],[False,False,True],[True,False,False]],[[True,False,False],[True,True,True],[False,False,True],[False,False,False],[True,False,True],[True,False,True],[True,True,False],[False,False,True],[False,False,True]],[[True,False,True],[True,True,True],[True,False,False],[False,False,True],[False,True,True],[False,False,True],[True,True,False],[False,False,True],[False,True,True]],[[True,True,False],[False,True,False],[False,False,True],[True,False,True],[False,False,False],[True,False,True],[False,True,True],[True,False,False],[True,True,True]]], dtype = "bool")#candidate|11899|(11, 9, 3)|const|bool
bop_11900 = relay.logical_or(var_11898.astype('bool'), relay.reshape(const_11899.astype('bool'), relay.shape_of(var_11898))) # shape=(11, 9, 3)
func_2958_call = mod.get_global_var('func_2958')
func_2959_call = mutated_mod.get_global_var('func_2959')
call_11903 = relay.TupleGetItem(func_2958_call(), 0)
call_11904 = relay.TupleGetItem(func_2959_call(), 0)
output = relay.Tuple([bop_11900,call_11903,])
output2 = relay.Tuple([bop_11900,call_11904,])
func_11911 = relay.Function([var_11898,], output)
mod['func_11911'] = func_11911
mod = relay.transform.InferType()(mod)
var_11912 = relay.var("var_11912", dtype = "bool", shape = (11, 9, 3))#candidate|11912|(11, 9, 3)|var|bool
output = func_11911(var_11912)
func_11913 = relay.Function([var_11912], output)
mutated_mod['func_11913'] = func_11913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7656_call = mod.get_global_var('func_7656')
func_7657_call = mutated_mod.get_global_var('func_7657')
call_11962 = relay.TupleGetItem(func_7656_call(), 1)
call_11963 = relay.TupleGetItem(func_7657_call(), 1)
func_10517_call = mod.get_global_var('func_10517')
func_10519_call = mutated_mod.get_global_var('func_10519')
call_11969 = relay.TupleGetItem(func_10517_call(), 5)
call_11970 = relay.TupleGetItem(func_10519_call(), 5)
output = relay.Tuple([call_11962,call_11969,])
output2 = relay.Tuple([call_11963,call_11970,])
func_11971 = relay.Function([], output)
mod['func_11971'] = func_11971
mod = relay.transform.InferType()(mod)
mutated_mod['func_11971'] = func_11971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11971_call = mutated_mod.get_global_var('func_11971')
call_11972 = func_11971_call()
output = call_11972
func_11973 = relay.Function([], output)
mutated_mod['func_11973'] = func_11973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7882_call = mod.get_global_var('func_7882')
func_7884_call = mutated_mod.get_global_var('func_7884')
call_12051 = func_7882_call()
call_12052 = func_7882_call()
output = relay.Tuple([call_12051,])
output2 = relay.Tuple([call_12052,])
func_12054 = relay.Function([], output)
mod['func_12054'] = func_12054
mod = relay.transform.InferType()(mod)
mutated_mod['func_12054'] = func_12054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12054_call = mutated_mod.get_global_var('func_12054')
call_12055 = func_12054_call()
output = call_12055
func_12056 = relay.Function([], output)
mutated_mod['func_12056'] = func_12056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_564_call = mod.get_global_var('func_564')
func_566_call = mutated_mod.get_global_var('func_566')
call_12099 = relay.TupleGetItem(func_564_call(), 0)
call_12100 = relay.TupleGetItem(func_566_call(), 0)
output = call_12099
output2 = call_12100
func_12103 = relay.Function([], output)
mod['func_12103'] = func_12103
mod = relay.transform.InferType()(mod)
output = func_12103()
func_12104 = relay.Function([], output)
mutated_mod['func_12104'] = func_12104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7687_call = mod.get_global_var('func_7687')
func_7688_call = mutated_mod.get_global_var('func_7688')
call_12155 = relay.TupleGetItem(func_7687_call(), 1)
call_12156 = relay.TupleGetItem(func_7688_call(), 1)
func_8806_call = mod.get_global_var('func_8806')
func_8809_call = mutated_mod.get_global_var('func_8809')
const_12187 = relay.const([[-6.925854,3.399464,-6.621414,7.020527,-3.043216,-1.282610,-4.699555,-6.276786,-9.558910,6.165854,-6.597350,-3.892251,-2.066486,-7.700023,-8.418998,-4.128677,9.802782,-7.381658,-1.749571,-4.173912,2.796572,6.301080,-2.499459,-9.778556,4.740141,-0.103729,8.201927,-6.539192,-4.409339,3.750040,-3.702237,9.849446,5.604677,-6.941103,-3.727185,2.626509,9.138552,4.156204,-1.973704,5.943965,2.529370,3.311006,-3.598241,8.846904,-0.793476,8.842866,-5.316972,-1.373694,-8.840521,1.480879,-5.272979,-1.072569,-6.874786,3.915449,9.403998,-8.946491,-2.221139,-2.091799,3.952116,-0.509781,-6.702601,-8.830182,-2.719849,-4.583180,0.861602,5.557014,-0.019428,-1.641301,-1.284222,1.934688,-1.325828,-4.592741,-5.960422,1.679745,-6.726877,3.400209,6.114223,9.527814,6.508129,-8.476029,-7.818817,-9.395950,-7.843250,7.059705,-7.972932,-5.821979,-1.213186,1.204214,8.240723,-3.543869,-8.824744,-3.227098,3.242430,-5.204013,-2.556839,-1.634363,-7.911512,1.045309,2.401779,1.592614,-1.672690,-6.016180,1.765509,9.351646,-0.418292,-9.939604,0.936253,-2.489922,6.910851,8.022299,8.941695,-1.475254,-1.330023,-5.271312,-8.014210,2.710294,-1.454561],[2.610080,-7.543154,-7.017079,-7.517839,0.346449,-6.059800,-4.398722,-7.047648,6.403424,5.468675,-1.925466,7.640133,4.898199,-9.997653,-1.637820,-4.716354,-7.201035,-9.993169,2.380798,-3.144065,9.868867,-0.663055,-1.300283,4.998328,4.838331,1.453019,5.235730,-6.413102,-6.997058,6.714589,4.413859,-4.767979,-3.533231,0.492713,2.685591,1.654632,-4.121898,-3.934843,-9.569454,-0.146960,7.431895,2.731735,-9.969367,5.627715,9.348456,-5.750373,4.591994,-6.725065,5.820500,4.322397,6.604415,5.363177,6.614672,-2.570161,-6.453726,4.920178,-9.597773,-9.449656,-6.751549,5.262557,-8.975470,9.508618,-0.233386,-5.067933,7.445975,-8.332760,-5.894329,-4.896706,-9.363962,8.372835,4.385409,-0.901928,-6.257165,-5.030530,-9.113115,-0.448978,0.100810,-2.730293,3.367018,-3.455312,9.819627,-0.697178,-1.273831,9.804922,1.359499,8.615876,1.826749,5.895717,-2.646642,-6.297590,6.869968,-8.493126,-1.821665,4.225204,1.151278,-9.443870,-5.807299,-5.244994,8.401970,8.610638,-3.797302,5.475169,-8.027301,4.909763,6.656352,-5.424191,-8.979558,3.926335,8.976197,3.602379,-1.326723,3.015270,-9.560051,-1.983930,1.974845,-6.051643,-2.975501],[8.755126,-1.977122,-1.979296,5.514396,3.226123,6.092869,-8.858134,1.681899,6.625558,-0.635760,-1.270983,-6.563113,-1.708302,3.986662,9.046084,2.564146,-8.071244,-1.732418,8.333812,0.919972,0.158788,3.334453,-1.922212,3.966084,3.993292,-3.923208,-4.781352,-2.348320,3.401632,-1.473324,4.723311,4.441793,3.091299,-0.156996,9.849824,4.585825,-4.343598,1.018269,0.497113,-2.042436,-2.331571,8.279630,4.060107,3.136690,1.206139,-5.367144,5.815459,-0.781444,9.533130,3.768654,1.220364,2.522303,-4.446463,-9.249192,-8.643948,-6.634192,5.844808,8.934688,3.541382,9.909813,-6.144334,3.687320,-2.533365,3.675122,8.190303,-3.550079,5.633810,-6.821327,-1.415133,-4.902042,-9.516177,0.657210,-4.605663,-8.009699,-7.013104,-0.805975,3.501938,-8.289260,8.705485,1.584422,1.846397,9.274177,-2.520143,-2.800934,-6.242493,5.678526,6.341376,4.363515,0.552541,4.927108,5.507246,6.696395,3.592788,-7.922263,7.389433,8.541955,-6.771132,9.211183,8.275634,1.220821,-8.017724,-9.700222,-4.153315,5.944806,3.438649,8.370097,-4.201450,-5.346835,-4.964060,2.157624,-6.821071,-5.098598,3.241675,9.904819,9.252365,7.728286,7.267933],[0.958692,7.973697,-1.113889,9.064867,4.105096,-9.607697,-3.002167,7.647932,-2.077474,-5.553222,-1.982117,-2.564206,-9.169728,-3.278732,-1.636384,1.979523,7.697959,-1.213939,-2.947871,9.126196,-7.301405,7.571661,4.281362,-9.027693,-7.093681,-3.634360,-9.143688,1.972414,2.322615,-4.416677,8.634862,6.591224,-6.817068,-5.725504,-2.891426,2.434560,9.434866,0.195410,0.511770,-4.857255,-9.906928,-8.575472,-2.756381,-1.790466,9.527781,7.369086,-2.596176,-2.144157,-9.212853,1.348027,-0.699941,2.242638,4.426439,-5.664402,-5.827651,5.497466,-3.026065,-3.913896,6.967141,-1.773391,9.574153,0.683845,-4.782097,6.905846,7.153514,6.560894,0.477195,8.496788,0.929864,4.616209,6.307072,1.351480,-5.620560,-3.792975,-4.580394,-3.291837,-9.412603,3.220872,5.783191,2.235961,-6.962721,1.828761,-5.171371,-6.096964,-9.044658,5.164030,-7.442815,3.401279,-1.073956,-6.348456,-3.094187,9.878379,7.989010,-5.779342,7.300001,4.691713,-8.148549,9.171937,8.219272,6.095290,3.535664,1.570639,7.787876,-3.875920,-5.280733,-2.529036,0.895034,3.814527,-8.869889,-9.464265,-1.985996,1.434637,-1.867590,4.954913,2.698429,1.938653,4.143190],[-5.551021,-4.023448,0.052750,-8.002964,8.001191,2.989610,-3.104483,-5.184056,9.754986,-5.762291,-3.421520,0.400407,-8.013206,-5.302123,9.825123,4.595932,-0.171271,-0.218148,-9.848266,9.881840,-0.671818,5.176194,-7.641769,6.873251,-7.507510,0.521717,-8.914262,-0.277747,9.899111,8.770904,-9.702815,-8.441766,-2.020790,-7.300426,8.335664,-6.575511,-9.460290,-0.792559,-9.419750,-2.175346,0.726475,9.531255,-0.205765,9.161126,-4.518120,-2.086594,2.815612,6.154563,0.627937,-1.475878,8.228182,8.810606,-3.896192,-3.047157,7.960940,1.321595,-2.057815,9.926474,-4.608919,-9.090910,3.854150,-7.456876,-5.009513,-8.194904,9.342667,-7.259638,6.655124,0.872913,-0.043507,-7.980550,-8.829389,-6.249391,-6.978842,-3.552924,-5.516123,5.920309,4.298040,-7.742947,3.136074,-7.550325,-2.788400,2.095949,-2.629894,7.377551,5.368934,-1.651778,-4.707981,-6.087979,-7.424942,4.564367,-6.258589,-2.525715,-7.413080,1.292579,5.147997,8.274837,-7.454955,-4.242073,8.054416,9.599454,0.500940,-6.722401,3.417162,8.984147,3.443644,-7.412640,0.755459,-7.010948,-9.944935,-0.362655,5.529943,4.755265,-3.760980,-5.304047,2.977199,-8.403543,9.126853]], dtype = "float32")#candidate|12187|(5, 117)|const|float32
call_12186 = relay.TupleGetItem(func_8806_call(relay.reshape(const_12187.astype('float32'), [585,])), 1)
call_12188 = relay.TupleGetItem(func_8809_call(relay.reshape(const_12187.astype('float32'), [585,])), 1)
var_12189 = relay.var("var_12189", dtype = "float32", shape = (5, 117))#candidate|12189|(5, 117)|var|float32
bop_12190 = relay.not_equal(const_12187.astype('bool'), relay.reshape(var_12189.astype('bool'), relay.shape_of(const_12187))) # shape=(5, 117)
output = relay.Tuple([call_12155,call_12186,bop_12190,])
output2 = relay.Tuple([call_12156,call_12188,bop_12190,])
func_12195 = relay.Function([var_12189,], output)
mod['func_12195'] = func_12195
mod = relay.transform.InferType()(mod)
mutated_mod['func_12195'] = func_12195
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12196 = relay.var("var_12196", dtype = "float32", shape = (5, 117))#candidate|12196|(5, 117)|var|float32
func_12195_call = mutated_mod.get_global_var('func_12195')
call_12197 = func_12195_call(var_12196)
output = call_12197
func_12198 = relay.Function([var_12196], output)
mutated_mod['func_12198'] = func_12198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10517_call = mod.get_global_var('func_10517')
func_10519_call = mutated_mod.get_global_var('func_10519')
call_12203 = relay.TupleGetItem(func_10517_call(), 3)
call_12204 = relay.TupleGetItem(func_10519_call(), 3)
uop_12207 = relay.log2(call_12203.astype('float32')) # shape=(2, 10, 4)
uop_12209 = relay.log2(call_12204.astype('float32')) # shape=(2, 10, 4)
bop_12210 = relay.right_shift(call_12203.astype('uint64'), relay.reshape(uop_12207.astype('uint64'), relay.shape_of(call_12203))) # shape=(2, 10, 4)
bop_12213 = relay.right_shift(call_12204.astype('uint64'), relay.reshape(uop_12209.astype('uint64'), relay.shape_of(call_12204))) # shape=(2, 10, 4)
output = relay.Tuple([bop_12210,])
output2 = relay.Tuple([bop_12213,])
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
	relay.transform.ToBasicBlockNormalForm(),
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
