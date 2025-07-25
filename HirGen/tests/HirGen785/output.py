import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_18 = relay.var("var_18", dtype = "float64", shape = (14, 5, 1))#candidate|18|(14, 5, 1)|var|float64
uop_19 = relay.erf(var_18.astype('float64')) # shape=(14, 5, 1)
bop_23 = relay.equal(uop_19.astype('bool'), relay.reshape(var_18.astype('bool'), relay.shape_of(uop_19))) # shape=(14, 5, 1)
const_30 = relay.const([[[-6.344156,3.020365,-3.076440,0.431859],[4.477889,-3.648174,-5.031824,4.341694],[-7.561052,9.327492,2.594446,-1.228088],[-2.967049,-0.174524,8.475357,-0.886454],[-0.288195,3.557080,-5.899682,6.342586]],[[2.809279,-9.061837,-7.021959,3.467877],[-0.614182,8.368933,-7.851511,5.853149],[4.363986,6.965925,8.520766,0.655085],[9.052155,-0.580034,4.254192,0.718856],[7.901902,-0.229766,3.035148,-1.308902]],[[-9.407764,9.675356,-2.468552,4.304213],[-1.864993,-4.531178,2.168632,-3.962649],[-8.911099,-6.415396,-3.496728,5.067744],[5.625260,8.379879,5.082339,-1.313000],[-7.593195,-7.029501,-5.603034,-7.679126]],[[-8.689268,-9.292730,-2.407831,0.812388],[8.378404,-5.330573,8.056986,-0.785333],[9.462358,-5.754957,1.158108,4.002568],[-2.485314,-6.508622,7.125008,-6.196868],[2.441788,6.910160,0.361874,7.515269]],[[-8.678595,-4.515766,2.568311,-3.086351],[9.034805,9.852964,5.593129,-9.227972],[-3.881490,-2.984711,1.697767,1.877910],[5.014753,2.370809,6.356372,-3.345946],[-1.317394,-2.264607,2.711433,5.064304]],[[7.544068,5.530121,4.428754,-8.375213],[0.811505,4.821550,0.966925,5.640796],[-1.646020,9.129589,7.158474,7.265529],[4.660930,8.976620,2.028742,7.258074],[1.408510,6.678807,-3.304191,-3.583461]],[[1.217581,-7.486755,1.996060,7.657269],[-7.517816,0.872510,-3.589887,-2.335450],[-8.577229,-7.253643,-0.256621,-2.539127],[5.710619,-1.334066,-7.948407,2.059923],[-6.268526,-2.027569,5.218403,6.058533]],[[7.607834,-6.055223,-4.423332,5.853727],[-1.683510,-2.283879,9.985694,3.310852],[-2.083767,-3.682297,-3.182252,-9.291815],[4.112815,-9.545527,6.888280,5.525336],[6.182412,-4.819518,-2.774063,-4.995021]],[[-1.676277,0.028179,-6.286641,-3.988586],[-8.291166,1.461734,-8.135562,2.027632],[-2.893877,-9.606377,-2.601060,-8.727905],[6.828532,6.028137,-1.992438,7.539296],[-3.240937,-0.798803,6.208786,6.822169]],[[7.931017,-3.279675,6.159604,-5.919223],[-2.262079,3.155644,-3.879406,-3.398599],[-4.071687,1.917576,7.530265,1.769751],[3.060850,-1.668006,-2.192444,-6.683584],[-5.072388,4.560024,-1.167905,-8.350152]],[[9.565211,1.553952,5.703392,9.854735],[0.876520,4.044800,7.207967,-5.292504],[-0.320270,5.602979,6.086143,9.897375],[8.275604,2.843489,-9.291497,-2.493449],[3.003119,6.704287,7.151994,-3.545558]],[[8.928866,5.050714,6.339295,0.904048],[6.761047,-4.015623,-7.684580,-0.119223],[7.254012,5.833560,3.718407,4.847574],[-1.945085,-6.583959,4.087276,-5.167016],[-9.550072,-7.041164,-1.463864,6.545695]],[[-8.842440,-7.125473,8.885143,-7.390921],[-9.443432,-5.991552,6.890441,-6.967532],[-3.075778,5.664791,6.903305,-1.614629],[-2.303901,3.531890,-7.352148,-2.320194],[7.633738,0.447377,5.739338,2.597292]],[[-5.561226,-0.052119,7.610579,8.797465],[6.325502,2.588522,-2.241336,-0.251634],[-6.281116,6.390646,-8.670490,-4.929016],[-4.584668,3.154887,1.433710,4.322587],[-3.631349,-5.924758,-3.879403,-2.134595]]], dtype = "float64")#candidate|30|(14, 5, 4)|const|float64
bop_31 = relay.greater(var_18.astype('bool'), const_30.astype('bool')) # shape=(14, 5, 4)
output = relay.Tuple([bop_23,bop_31,])
output2 = relay.Tuple([bop_23,bop_31,])
func_50 = relay.Function([var_18,], output)
mod['func_50'] = func_50
mod = relay.transform.InferType()(mod)
mutated_mod['func_50'] = func_50
mutated_mod = relay.transform.InferType()(mutated_mod)
var_51 = relay.var("var_51", dtype = "float64", shape = (14, 5, 1))#candidate|51|(14, 5, 1)|var|float64
func_50_call = mutated_mod.get_global_var('func_50')
call_52 = func_50_call(var_51)
output = call_52
func_53 = relay.Function([var_51], output)
mutated_mod['func_53'] = func_53
mutated_mod = relay.transform.InferType()(mutated_mod)
var_371 = relay.var("var_371", dtype = "float32", shape = (13, 12, 4))#candidate|371|(13, 12, 4)|var|float32
uop_372 = relay.acosh(var_371.astype('float32')) # shape=(13, 12, 4)
output = relay.Tuple([uop_372,])
output2 = relay.Tuple([uop_372,])
func_384 = relay.Function([var_371,], output)
mod['func_384'] = func_384
mod = relay.transform.InferType()(mod)
mutated_mod['func_384'] = func_384
mutated_mod = relay.transform.InferType()(mutated_mod)
var_385 = relay.var("var_385", dtype = "float32", shape = (13, 12, 4))#candidate|385|(13, 12, 4)|var|float32
func_384_call = mutated_mod.get_global_var('func_384')
call_386 = func_384_call(var_385)
output = call_386
func_387 = relay.Function([var_385], output)
mutated_mod['func_387'] = func_387
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1035 = relay.const([[[1.579011],[-8.947899],[-6.355490],[1.437131],[5.998047],[4.996811],[-8.406283],[-4.241218],[3.982766]]], dtype = "float32")#candidate|1035|(1, 9, 1)|const|float32
var_1036 = relay.var("var_1036", dtype = "float32", shape = (4, 9, 5))#candidate|1036|(4, 9, 5)|var|float32
bop_1037 = relay.floor_mod(const_1035.astype('float32'), var_1036.astype('float32')) # shape=(4, 9, 5)
uop_1058 = relay.sin(const_1035.astype('float32')) # shape=(1, 9, 1)
output = relay.Tuple([bop_1037,uop_1058,])
output2 = relay.Tuple([bop_1037,uop_1058,])
func_1061 = relay.Function([var_1036,], output)
mod['func_1061'] = func_1061
mod = relay.transform.InferType()(mod)
var_1062 = relay.var("var_1062", dtype = "float32", shape = (4, 9, 5))#candidate|1062|(4, 9, 5)|var|float32
output = func_1061(var_1062)
func_1063 = relay.Function([var_1062], output)
mutated_mod['func_1063'] = func_1063
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1118 = relay.var("var_1118", dtype = "uint64", shape = ())#candidate|1118|()|var|uint64
const_1119 = relay.const([[[2],[5],[-8],[-5],[2],[-7],[-4],[10]],[[6],[1],[-3],[-2],[-8],[-5],[9],[4]],[[-10],[3],[1],[5],[3],[-4],[5],[-3]],[[7],[6],[3],[-9],[2],[7],[-8],[5]],[[9],[-3],[8],[-8],[10],[-10],[-7],[-7]],[[-6],[-6],[-2],[-10],[-9],[-6],[-8],[-4]]], dtype = "uint64")#candidate|1119|(6, 8, 1)|const|uint64
bop_1120 = relay.bitwise_and(var_1118.astype('uint64'), const_1119.astype('uint64')) # shape=(6, 8, 1)
func_50_call = mod.get_global_var('func_50')
func_53_call = mutated_mod.get_global_var('func_53')
const_1139 = relay.const([0.226772,-0.691049,-7.430175,6.120701,-4.840152,3.332568,9.305228,-0.997288,-1.862469,-3.607100,-0.656338,-0.102664,5.333882,0.895057,8.097927,6.928839,-6.959427,3.786018,6.888802,1.843092,-7.132848,-2.637980,-4.870562,1.475076,-9.570799,-7.872786,-9.974150,-1.414197,0.586480,5.889128,-5.306430,3.206673,-4.763103,-0.447505,-2.468639,7.209726,-3.218247,-7.911243,4.573978,8.534376,8.563804,-0.888965,-2.350816,4.557578,-6.492536,-5.229863,9.624428,7.297145,-6.643706,-5.156909,-6.797877,3.186703,4.857184,5.913820,1.109710,-2.708278,9.359959,5.551141,1.769156,1.155179,7.985002,6.218903,5.349704,-7.967793,-1.113666,-2.138143,-0.902247,5.219937,9.739207,-3.228033], dtype = "float64")#candidate|1139|(70,)|const|float64
call_1138 = relay.TupleGetItem(func_50_call(relay.reshape(const_1139.astype('float64'), [14, 5, 1])), 0)
call_1140 = relay.TupleGetItem(func_53_call(relay.reshape(const_1139.astype('float64'), [14, 5, 1])), 0)
bop_1160 = relay.floor_divide(var_1118.astype('float32'), const_1119.astype('float32')) # shape=(6, 8, 1)
var_1174 = relay.var("var_1174", dtype = "bool", shape = (14, 5, 16))#candidate|1174|(14, 5, 16)|var|bool
bop_1175 = relay.mod(call_1138.astype('float32'), var_1174.astype('float32')) # shape=(14, 5, 16)
bop_1178 = relay.mod(call_1140.astype('float32'), var_1174.astype('float32')) # shape=(14, 5, 16)
output = relay.Tuple([bop_1120,const_1139,bop_1160,bop_1175,])
output2 = relay.Tuple([bop_1120,const_1139,bop_1160,bop_1178,])
func_1180 = relay.Function([var_1118,var_1174,], output)
mod['func_1180'] = func_1180
mod = relay.transform.InferType()(mod)
mutated_mod['func_1180'] = func_1180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1180_call = mutated_mod.get_global_var('func_1180')
var_1182 = relay.var("var_1182", dtype = "uint64", shape = ())#candidate|1182|()|var|uint64
var_1183 = relay.var("var_1183", dtype = "bool", shape = (14, 5, 16))#candidate|1183|(14, 5, 16)|var|bool
call_1181 = func_1180_call(var_1182,var_1183,)
output = call_1181
func_1184 = relay.Function([var_1182,var_1183,], output)
mutated_mod['func_1184'] = func_1184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2220 = relay.var("var_2220", dtype = "float64", shape = (11, 3, 16))#candidate|2220|(11, 3, 16)|var|float64
var_2221 = relay.var("var_2221", dtype = "float64", shape = (11, 3, 16))#candidate|2221|(11, 3, 16)|var|float64
bop_2222 = relay.divide(var_2220.astype('float64'), relay.reshape(var_2221.astype('float64'), relay.shape_of(var_2220))) # shape=(11, 3, 16)
func_384_call = mod.get_global_var('func_384')
func_387_call = mutated_mod.get_global_var('func_387')
var_2229 = relay.var("var_2229", dtype = "float32", shape = (624,))#candidate|2229|(624,)|var|float32
call_2228 = relay.TupleGetItem(func_384_call(relay.reshape(var_2229.astype('float32'), [13, 12, 4])), 0)
call_2230 = relay.TupleGetItem(func_387_call(relay.reshape(var_2229.astype('float32'), [13, 12, 4])), 0)
output = relay.Tuple([bop_2222,call_2228,var_2229,])
output2 = relay.Tuple([bop_2222,call_2230,var_2229,])
func_2250 = relay.Function([var_2220,var_2221,var_2229,], output)
mod['func_2250'] = func_2250
mod = relay.transform.InferType()(mod)
var_2251 = relay.var("var_2251", dtype = "float64", shape = (11, 3, 16))#candidate|2251|(11, 3, 16)|var|float64
var_2252 = relay.var("var_2252", dtype = "float64", shape = (11, 3, 16))#candidate|2252|(11, 3, 16)|var|float64
var_2253 = relay.var("var_2253", dtype = "float32", shape = (624,))#candidate|2253|(624,)|var|float32
output = func_2250(var_2251,var_2252,var_2253,)
func_2254 = relay.Function([var_2251,var_2252,var_2253,], output)
mutated_mod['func_2254'] = func_2254
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2582 = relay.var("var_2582", dtype = "float32", shape = ())#candidate|2582|()|var|float32
var_2583 = relay.var("var_2583", dtype = "float32", shape = (5, 1, 16))#candidate|2583|(5, 1, 16)|var|float32
bop_2584 = relay.equal(var_2582.astype('bool'), var_2583.astype('bool')) # shape=(5, 1, 16)
bop_2602 = relay.bitwise_and(var_2582.astype('uint64'), bop_2584.astype('uint64')) # shape=(5, 1, 16)
bop_2605 = relay.greater(bop_2584.astype('bool'), relay.reshape(var_2583.astype('bool'), relay.shape_of(bop_2584))) # shape=(5, 1, 16)
output = relay.Tuple([bop_2602,bop_2605,])
output2 = relay.Tuple([bop_2602,bop_2605,])
func_2614 = relay.Function([var_2582,var_2583,], output)
mod['func_2614'] = func_2614
mod = relay.transform.InferType()(mod)
mutated_mod['func_2614'] = func_2614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2614_call = mutated_mod.get_global_var('func_2614')
var_2616 = relay.var("var_2616", dtype = "float32", shape = ())#candidate|2616|()|var|float32
var_2617 = relay.var("var_2617", dtype = "float32", shape = (5, 1, 16))#candidate|2617|(5, 1, 16)|var|float32
call_2615 = func_2614_call(var_2616,var_2617,)
output = call_2615
func_2618 = relay.Function([var_2616,var_2617,], output)
mutated_mod['func_2618'] = func_2618
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2839 = relay.var("var_2839", dtype = "int16", shape = (13, 7, 1))#candidate|2839|(13, 7, 1)|var|int16
const_2840 = relay.const([[[-8],[-9],[-5],[-5],[-10],[-4],[-8]],[[-2],[9],[4],[-1],[3],[9],[3]],[[3],[-3],[7],[3],[7],[-10],[4]],[[3],[10],[-10],[7],[2],[4],[3]],[[-9],[9],[-10],[-6],[-4],[-1],[-7]],[[-5],[-5],[-5],[-4],[-4],[1],[-10]],[[-5],[-2],[9],[10],[-2],[6],[-5]],[[5],[8],[-5],[10],[7],[-8],[-6]],[[1],[6],[7],[2],[-9],[-5],[7]],[[5],[8],[6],[-1],[10],[4],[5]],[[8],[-1],[-7],[5],[-6],[10],[-9]],[[4],[-6],[-10],[2],[2],[-10],[5]],[[10],[5],[3],[-9],[6],[-4],[2]]], dtype = "int16")#candidate|2840|(13, 7, 1)|const|int16
bop_2841 = relay.bitwise_or(var_2839.astype('int16'), relay.reshape(const_2840.astype('int16'), relay.shape_of(var_2839))) # shape=(13, 7, 1)
output = bop_2841
output2 = bop_2841
func_2846 = relay.Function([var_2839,], output)
mod['func_2846'] = func_2846
mod = relay.transform.InferType()(mod)
var_2847 = relay.var("var_2847", dtype = "int16", shape = (13, 7, 1))#candidate|2847|(13, 7, 1)|var|int16
output = func_2846(var_2847)
func_2848 = relay.Function([var_2847], output)
mutated_mod['func_2848'] = func_2848
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2977 = relay.var("var_2977", dtype = "bool", shape = (9, 16, 5))#candidate|2977|(9, 16, 5)|var|bool
const_2978 = relay.const([[[True,False,True,False,True],[True,True,True,False,False],[False,False,True,False,True],[True,True,True,False,False],[True,False,True,True,True],[True,True,True,True,True],[True,False,True,False,True],[False,False,False,True,False],[False,True,False,True,False],[True,False,True,False,False],[False,False,False,True,True],[False,False,True,True,False],[False,False,False,False,False],[True,False,False,True,False],[False,True,True,False,False],[True,True,False,True,False]],[[True,True,False,True,False],[True,True,True,False,False],[True,True,False,True,True],[True,True,True,True,False],[True,False,False,True,False],[False,False,False,True,True],[False,False,False,False,True],[True,True,True,False,False],[True,True,True,False,False],[False,True,True,True,False],[False,True,False,False,False],[True,False,False,True,True],[False,True,True,False,True],[True,True,False,False,True],[False,True,False,True,True],[True,True,False,False,True]],[[True,False,False,True,False],[False,False,True,False,True],[False,False,False,False,True],[True,True,False,False,True],[False,False,False,False,False],[False,True,True,False,False],[False,True,False,False,True],[True,False,True,False,True],[True,False,True,True,False],[False,True,True,True,True],[False,True,True,True,True],[True,True,True,True,True],[True,True,True,True,False],[False,False,False,True,False],[True,False,True,True,False],[True,True,True,True,False]],[[False,True,True,True,False],[True,True,True,False,False],[True,True,True,False,False],[True,False,True,False,True],[True,True,False,False,False],[False,False,False,True,True],[False,True,False,False,False],[True,True,True,False,True],[True,True,False,True,True],[False,False,True,True,False],[True,True,False,True,True],[False,True,True,False,False],[False,True,True,True,True],[True,False,False,True,False],[True,False,False,True,True],[True,True,False,True,True]],[[False,False,False,False,True],[True,True,False,True,True],[False,True,False,True,False],[True,False,False,True,True],[True,False,False,True,True],[True,False,True,True,True],[False,False,True,False,False],[False,True,True,False,False],[True,False,False,True,True],[False,True,False,True,False],[True,False,True,True,True],[False,True,True,True,False],[True,True,False,False,True],[True,True,True,False,True],[True,True,False,True,True],[True,False,False,True,True]],[[False,True,True,True,False],[False,False,True,True,True],[False,False,True,False,True],[False,True,False,True,False],[True,True,True,True,False],[False,True,False,False,False],[True,True,True,False,False],[False,False,False,True,False],[False,True,False,True,False],[True,True,True,True,True],[True,True,False,True,False],[False,True,True,True,False],[False,False,True,True,True],[True,True,True,False,True],[True,False,False,False,True],[False,True,False,False,True]],[[True,True,False,True,False],[False,False,False,False,True],[False,False,True,True,True],[False,False,True,False,False],[False,True,False,False,True],[True,True,True,False,True],[False,True,False,False,True],[True,False,True,True,False],[False,True,False,True,False],[False,False,False,True,False],[True,True,True,True,True],[True,True,False,False,True],[True,False,False,False,False],[True,True,False,False,False],[True,False,True,True,False],[True,True,False,True,False]],[[False,False,True,True,False],[True,False,True,True,False],[False,True,False,False,True],[False,False,False,True,False],[False,False,True,True,True],[True,False,True,True,True],[True,True,False,True,False],[False,False,True,True,True],[True,True,False,False,True],[True,False,True,True,True],[False,True,True,True,False],[True,False,False,False,True],[False,True,False,False,False],[False,False,False,True,True],[False,True,False,False,True],[True,False,True,True,True]],[[True,True,True,False,False],[True,True,False,False,True],[True,False,True,True,False],[True,True,False,False,True],[True,False,False,True,False],[True,False,False,False,True],[False,True,False,True,False],[False,False,True,False,False],[True,True,False,False,False],[False,True,False,False,True],[True,True,True,True,False],[False,False,True,False,False],[False,False,False,True,True],[False,True,False,True,False],[False,False,True,True,False],[False,True,False,False,False]]], dtype = "bool")#candidate|2978|(9, 16, 5)|const|bool
bop_2979 = relay.logical_or(var_2977.astype('bool'), relay.reshape(const_2978.astype('bool'), relay.shape_of(var_2977))) # shape=(9, 16, 5)
uop_2983 = relay.sqrt(var_2977.astype('float32')) # shape=(9, 16, 5)
output = relay.Tuple([bop_2979,uop_2983,])
output2 = relay.Tuple([bop_2979,uop_2983,])
func_2996 = relay.Function([var_2977,], output)
mod['func_2996'] = func_2996
mod = relay.transform.InferType()(mod)
mutated_mod['func_2996'] = func_2996
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2997 = relay.var("var_2997", dtype = "bool", shape = (9, 16, 5))#candidate|2997|(9, 16, 5)|var|bool
func_2996_call = mutated_mod.get_global_var('func_2996')
call_2998 = func_2996_call(var_2997)
output = call_2998
func_2999 = relay.Function([var_2997], output)
mutated_mod['func_2999'] = func_2999
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3585 = relay.var("var_3585", dtype = "float64", shape = (14, 8, 13))#candidate|3585|(14, 8, 13)|var|float64
var_3586 = relay.var("var_3586", dtype = "float64", shape = (14, 8, 13))#candidate|3586|(14, 8, 13)|var|float64
bop_3587 = relay.floor_divide(var_3585.astype('float64'), relay.reshape(var_3586.astype('float64'), relay.shape_of(var_3585))) # shape=(14, 8, 13)
output = bop_3587
output2 = bop_3587
func_3593 = relay.Function([var_3585,var_3586,], output)
mod['func_3593'] = func_3593
mod = relay.transform.InferType()(mod)
var_3594 = relay.var("var_3594", dtype = "float64", shape = (14, 8, 13))#candidate|3594|(14, 8, 13)|var|float64
var_3595 = relay.var("var_3595", dtype = "float64", shape = (14, 8, 13))#candidate|3595|(14, 8, 13)|var|float64
output = func_3593(var_3594,var_3595,)
func_3596 = relay.Function([var_3594,var_3595,], output)
mutated_mod['func_3596'] = func_3596
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3763 = relay.var("var_3763", dtype = "uint32", shape = ())#candidate|3763|()|var|uint32
const_3764 = relay.const([[[-8,7],[10,-7],[-10,-9]],[[3,-6],[6,-6],[-1,-7]],[[-9,-1],[1,-8],[4,-2]],[[-9,-3],[-8,-7],[8,-3]],[[-9,-5],[8,-1],[6,-7]],[[3,7],[-1,4],[-2,9]]], dtype = "uint32")#candidate|3764|(6, 3, 2)|const|uint32
bop_3765 = relay.add(var_3763.astype('uint32'), const_3764.astype('uint32')) # shape=(6, 3, 2)
output = relay.Tuple([bop_3765,])
output2 = relay.Tuple([bop_3765,])
func_3768 = relay.Function([var_3763,], output)
mod['func_3768'] = func_3768
mod = relay.transform.InferType()(mod)
mutated_mod['func_3768'] = func_3768
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3769 = relay.var("var_3769", dtype = "uint32", shape = ())#candidate|3769|()|var|uint32
func_3768_call = mutated_mod.get_global_var('func_3768')
call_3770 = func_3768_call(var_3769)
output = call_3770
func_3771 = relay.Function([var_3769], output)
mutated_mod['func_3771'] = func_3771
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3773 = relay.var("var_3773", dtype = "float32", shape = (2, 4, 1))#candidate|3773|(2, 4, 1)|var|float32
uop_3774 = relay.acos(var_3773.astype('float32')) # shape=(2, 4, 1)
var_3784 = relay.var("var_3784", dtype = "float32", shape = (2, 4, 13))#candidate|3784|(2, 4, 13)|var|float32
bop_3785 = relay.equal(var_3773.astype('bool'), var_3784.astype('bool')) # shape=(2, 4, 13)
output = relay.Tuple([uop_3774,bop_3785,])
output2 = relay.Tuple([uop_3774,bop_3785,])
func_3789 = relay.Function([var_3773,var_3784,], output)
mod['func_3789'] = func_3789
mod = relay.transform.InferType()(mod)
mutated_mod['func_3789'] = func_3789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mutated_mod.get_global_var('func_3789')
var_3791 = relay.var("var_3791", dtype = "float32", shape = (2, 4, 1))#candidate|3791|(2, 4, 1)|var|float32
var_3792 = relay.var("var_3792", dtype = "float32", shape = (2, 4, 13))#candidate|3792|(2, 4, 13)|var|float32
call_3790 = func_3789_call(var_3791,var_3792,)
output = call_3790
func_3793 = relay.Function([var_3791,var_3792,], output)
mutated_mod['func_3793'] = func_3793
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4002 = relay.var("var_4002", dtype = "uint8", shape = (3, 6, 14))#candidate|4002|(3, 6, 14)|var|uint8
var_4003 = relay.var("var_4003", dtype = "uint8", shape = (3, 6, 14))#candidate|4003|(3, 6, 14)|var|uint8
bop_4004 = relay.subtract(var_4002.astype('uint8'), relay.reshape(var_4003.astype('uint8'), relay.shape_of(var_4002))) # shape=(3, 6, 14)
uop_4011 = relay.cosh(var_4003.astype('float32')) # shape=(3, 6, 14)
func_3768_call = mod.get_global_var('func_3768')
func_3771_call = mutated_mod.get_global_var('func_3771')
var_4019 = relay.var("var_4019", dtype = "uint32", shape = ())#candidate|4019|()|var|uint32
call_4018 = relay.TupleGetItem(func_3768_call(relay.reshape(var_4019.astype('uint32'), [])), 0)
call_4020 = relay.TupleGetItem(func_3771_call(relay.reshape(var_4019.astype('uint32'), [])), 0)
func_3768_call = mod.get_global_var('func_3768')
func_3771_call = mutated_mod.get_global_var('func_3771')
call_4046 = relay.TupleGetItem(func_3768_call(relay.reshape(var_4019.astype('uint32'), [])), 0)
call_4047 = relay.TupleGetItem(func_3771_call(relay.reshape(var_4019.astype('uint32'), [])), 0)
output = relay.Tuple([bop_4004,uop_4011,call_4018,var_4019,call_4046,])
output2 = relay.Tuple([bop_4004,uop_4011,call_4020,var_4019,call_4047,])
func_4050 = relay.Function([var_4002,var_4003,var_4019,], output)
mod['func_4050'] = func_4050
mod = relay.transform.InferType()(mod)
mutated_mod['func_4050'] = func_4050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4050_call = mutated_mod.get_global_var('func_4050')
var_4052 = relay.var("var_4052", dtype = "uint8", shape = (3, 6, 14))#candidate|4052|(3, 6, 14)|var|uint8
var_4053 = relay.var("var_4053", dtype = "uint8", shape = (3, 6, 14))#candidate|4053|(3, 6, 14)|var|uint8
var_4054 = relay.var("var_4054", dtype = "uint32", shape = ())#candidate|4054|()|var|uint32
call_4051 = func_4050_call(var_4052,var_4053,var_4054,)
output = call_4051
func_4055 = relay.Function([var_4052,var_4053,var_4054,], output)
mutated_mod['func_4055'] = func_4055
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4096 = relay.var("var_4096", dtype = "uint8", shape = (2, 11, 15))#candidate|4096|(2, 11, 15)|var|uint8
var_4097 = relay.var("var_4097", dtype = "uint8", shape = (2, 11, 15))#candidate|4097|(2, 11, 15)|var|uint8
bop_4098 = relay.bitwise_or(var_4096.astype('uint8'), relay.reshape(var_4097.astype('uint8'), relay.shape_of(var_4096))) # shape=(2, 11, 15)
func_50_call = mod.get_global_var('func_50')
func_53_call = mutated_mod.get_global_var('func_53')
const_4169 = relay.const([8.869343,-7.183851,1.666815,-1.311195,1.465802,-4.094927,0.203284,-0.857562,6.236250,1.828207,2.863810,4.681174,8.375233,6.344536,-1.112573,-0.144895,9.160107,0.089570,1.104159,-6.022120,4.799857,-7.702580,2.061003,4.237584,1.880547,9.187346,-2.804616,-4.503763,5.071280,-1.571395,1.093782,2.460565,5.154375,6.659656,4.507841,-7.272970,-4.494263,8.611442,9.315726,-1.352269,8.318502,1.869527,-9.475082,-9.698404,-5.406632,6.428769,4.145761,-3.527928,-2.210615,5.367713,-2.312137,-5.015953,1.842130,-0.689409,-9.124372,5.002835,-9.352871,1.012004,-4.729061,3.369662,3.188042,-9.162419,4.254365,7.086438,2.249905,2.351518,-0.039379,-4.090182,-0.519337,-5.288725], dtype = "float64")#candidate|4169|(70,)|const|float64
call_4168 = relay.TupleGetItem(func_50_call(relay.reshape(const_4169.astype('float64'), [14, 5, 1])), 0)
call_4170 = relay.TupleGetItem(func_53_call(relay.reshape(const_4169.astype('float64'), [14, 5, 1])), 0)
func_384_call = mod.get_global_var('func_384')
func_387_call = mutated_mod.get_global_var('func_387')
var_4174 = relay.var("var_4174", dtype = "float32", shape = (624,))#candidate|4174|(624,)|var|float32
call_4173 = relay.TupleGetItem(func_384_call(relay.reshape(var_4174.astype('float32'), [13, 12, 4])), 0)
call_4175 = relay.TupleGetItem(func_387_call(relay.reshape(var_4174.astype('float32'), [13, 12, 4])), 0)
func_4050_call = mod.get_global_var('func_4050')
func_4055_call = mutated_mod.get_global_var('func_4055')
const_4177 = relay.const([-8,-5,7,3,4,-1,-5,-5,10,-1,-8,-5,3,-1,2,9,8,6,1,-1,9,10,-6,2,-5,-8,-1,-2,-7,-1,8,-8,8,-4,-3,6,4,8,2,-9,5,8,4,-2,2,9,-5,-8,1,4,6,8,5,-3,-7,4,2,10,3,-7,7,-6,-1,7,-8,-7,-8,-6,10,2,2,9,-9,1,1,6,2,-10,8,-6,-6,-1,-8,9,-6,5,-8,-3,-3,8,2,2,6,8,9,10,-7,-2,-10,2,6,6,-4,-1,-5,1,-3,-1,4,6,-3,3,-9,-4,-9,-5,-6,9,1,-6,-10,-4,-9,5,6,1,10,-9,8,-8,-2,2,-5,7,-2,2,10,-9,3,-6,-7,-8,10,4,5,-5,-8,-6,-7,-8,-7,-4,-8,-8,9,10,3,-1,-7,1,10,8,2,-10,8,9,-2,-2,6,-3,-8,-10,-3,1,9,-2,7,-4,4,9,4,7,1,-6,3,-3,-2,-9,-6,-5,-4,4,4,2,4,2,-9,3,8,10,-9,-2,6,8,-4,6,7,-1,10,1,-5,1,1,8,5,3,-1,-9,-6,10,7,8,-8,6,-2,-1,1,-3,-7,-4,-8,-10,-1,5,-3,9,-3,-5,6,10,-10,7,4,-6,10,5,8,-7,4,8,7,1], dtype = "uint8")#candidate|4177|(252,)|const|uint8
var_4178 = relay.var("var_4178", dtype = "uint32", shape = ())#candidate|4178|()|var|uint32
call_4176 = relay.TupleGetItem(func_4050_call(relay.reshape(const_4177.astype('uint8'), [3, 6, 14]), relay.reshape(const_4177.astype('uint8'), [3, 6, 14]), relay.reshape(var_4178.astype('uint32'), []), ), 3)
call_4179 = relay.TupleGetItem(func_4055_call(relay.reshape(const_4177.astype('uint8'), [3, 6, 14]), relay.reshape(const_4177.astype('uint8'), [3, 6, 14]), relay.reshape(var_4178.astype('uint32'), []), ), 3)
output = relay.Tuple([bop_4098,call_4168,const_4169,call_4173,var_4174,call_4176,const_4177,var_4178,])
output2 = relay.Tuple([bop_4098,call_4170,const_4169,call_4175,var_4174,call_4179,const_4177,var_4178,])
func_4196 = relay.Function([var_4096,var_4097,var_4174,var_4178,], output)
mod['func_4196'] = func_4196
mod = relay.transform.InferType()(mod)
var_4197 = relay.var("var_4197", dtype = "uint8", shape = (2, 11, 15))#candidate|4197|(2, 11, 15)|var|uint8
var_4198 = relay.var("var_4198", dtype = "uint8", shape = (2, 11, 15))#candidate|4198|(2, 11, 15)|var|uint8
var_4199 = relay.var("var_4199", dtype = "float32", shape = (624,))#candidate|4199|(624,)|var|float32
var_4200 = relay.var("var_4200", dtype = "uint32", shape = ())#candidate|4200|()|var|uint32
output = func_4196(var_4197,var_4198,var_4199,var_4200,)
func_4201 = relay.Function([var_4197,var_4198,var_4199,var_4200,], output)
mutated_mod['func_4201'] = func_4201
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4649 = relay.var("var_4649", dtype = "int64", shape = (14, 15, 3))#candidate|4649|(14, 15, 3)|var|int64
var_4650 = relay.var("var_4650", dtype = "int64", shape = (14, 15, 3))#candidate|4650|(14, 15, 3)|var|int64
bop_4651 = relay.greater(var_4649.astype('bool'), relay.reshape(var_4650.astype('bool'), relay.shape_of(var_4649))) # shape=(14, 15, 3)
output = relay.Tuple([bop_4651,])
output2 = relay.Tuple([bop_4651,])
func_4654 = relay.Function([var_4649,var_4650,], output)
mod['func_4654'] = func_4654
mod = relay.transform.InferType()(mod)
mutated_mod['func_4654'] = func_4654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4654_call = mutated_mod.get_global_var('func_4654')
var_4656 = relay.var("var_4656", dtype = "int64", shape = (14, 15, 3))#candidate|4656|(14, 15, 3)|var|int64
var_4657 = relay.var("var_4657", dtype = "int64", shape = (14, 15, 3))#candidate|4657|(14, 15, 3)|var|int64
call_4655 = func_4654_call(var_4656,var_4657,)
output = call_4655
func_4658 = relay.Function([var_4656,var_4657,], output)
mutated_mod['func_4658'] = func_4658
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5095 = relay.const([[[5.990982,-5.537953,4.632001,-4.023398,-1.392387,-3.256230,5.318708,1.813156,-1.829813,3.258719,9.546526,-9.398016,-6.459408,4.119949,-0.621377],[5.392227,-9.673966,9.516751,1.802984,8.216246,4.777460,2.190173,-1.023578,-9.853696,9.932077,-9.730172,4.062973,8.464727,-9.605977,-4.087680],[9.291289,-5.098377,1.572679,7.545707,0.839802,-2.477712,4.341215,3.187391,1.666721,-7.928509,7.279912,4.323132,8.409986,-1.163668,5.437675],[-0.341667,2.759504,3.285324,-2.521344,5.779442,7.787097,-1.582137,8.769545,-9.756007,2.748813,5.229023,-1.369603,-0.008247,-3.417881,5.981323],[0.185926,-4.175626,-2.690145,1.374928,3.135282,-3.540119,-0.218779,3.624109,-3.722212,-1.025312,-9.181694,9.329699,-9.935842,-4.753188,-6.797563],[7.575650,3.451750,-9.266153,0.040157,-6.203398,-5.597565,9.739841,1.478803,4.888019,2.613408,7.291657,9.898964,-3.290800,-4.547637,-5.472632],[-1.354343,-2.158988,-3.007371,4.911010,-8.088252,-0.815407,-2.002547,-6.058615,-6.944496,5.137056,0.034049,4.723287,1.247700,4.672659,-1.262987],[8.835273,1.268926,-7.763724,-0.850678,4.503021,5.618115,-8.861690,6.856189,7.704249,-0.533729,2.030018,2.484038,-5.068681,-8.118285,2.457764]],[[-4.189947,7.070584,-5.194351,5.994235,1.067390,-9.968025,-3.739803,-9.426914,7.160610,6.295441,8.172723,9.556010,1.796066,1.412990,3.685548],[-2.717746,0.766670,8.437493,1.513407,8.206762,5.697161,2.946461,-7.717064,-6.493254,2.768349,3.528110,-2.859557,7.429652,-6.192750,-1.042936],[7.738091,2.414946,-3.600686,4.076057,5.579504,6.956327,-6.220256,-4.087668,-1.760901,-8.577017,-7.147021,-9.662641,-5.606336,-4.113527,0.481195],[4.942847,4.660931,9.661106,8.818024,2.094471,8.229587,-6.065105,8.896537,-0.050341,9.608516,0.221778,-1.180047,-4.746286,-1.128423,-3.379532],[6.511711,-5.875548,-5.521685,1.875467,-0.268380,2.864575,7.993689,9.026219,-4.919691,-8.167625,-6.260480,-7.957279,-1.636930,-2.797520,1.180012],[-6.895453,-1.309413,-0.079634,-9.060470,-6.877742,-7.929413,9.049474,3.974656,1.627365,-5.359137,2.775523,0.817625,-6.809170,4.354772,-4.278239],[1.442178,4.399493,-3.851138,-4.488993,0.296976,7.562693,-6.886981,4.166939,-6.863242,-3.390095,5.468581,0.581008,6.508578,-8.108346,-2.447807],[8.741454,4.854320,5.551592,-2.677936,-4.740137,3.102443,-5.222883,-1.694473,8.596506,-9.920893,-2.273746,-2.540168,-5.163501,5.706221,-1.563793]],[[-7.778244,0.965882,-0.378635,3.109899,-9.660054,3.440124,0.778009,-2.543237,2.346607,-0.111832,0.791460,8.319909,4.978483,3.696774,-1.034471],[-9.984240,1.985185,-5.412492,8.533792,9.443262,-5.764683,8.337002,-1.203136,0.090167,9.161540,2.964651,-7.092378,-0.816352,-0.148057,-5.180221],[5.124543,2.279525,-2.024596,9.259264,9.431668,-0.093304,4.648507,-2.459165,6.884355,1.249585,3.549019,2.747711,-5.072890,0.020981,8.791981],[4.145042,2.593244,6.130945,1.578716,8.382096,6.586997,-0.927216,8.053187,-0.659143,-7.243078,5.343465,-9.969178,-9.081774,6.158574,-3.900519],[4.590241,2.560998,-9.903159,7.537074,6.974656,6.738830,-1.672568,1.542112,-0.384459,-9.667308,-1.075280,-1.854498,-2.234964,5.444225,0.264663],[-3.656372,5.404238,4.064843,-2.256066,8.594037,3.553507,5.017650,-1.874924,4.966178,-6.570170,-7.397714,8.072069,-8.096793,8.402422,0.451191],[8.665558,9.394550,-2.766711,-0.735028,6.485232,-6.387528,-1.151596,-1.399995,8.143914,7.621911,8.412511,-8.121486,5.434863,-3.886532,-8.436436],[7.054188,6.347463,-4.000964,6.266153,8.654254,5.770667,9.603862,1.830605,-1.067569,0.922940,-8.937335,3.980857,9.544270,3.979836,8.214713]],[[-9.133036,0.155882,-0.387154,1.346033,8.516265,-5.571720,-5.854654,-6.816690,-3.700764,-6.241552,8.300294,-8.948026,0.371378,8.938010,-8.885473],[-9.341545,7.476080,-8.716235,-8.649023,0.402035,-7.209583,-7.754095,2.451801,-0.563891,6.035538,2.746731,-3.853740,-8.808640,7.283975,-3.881428],[-1.958545,-9.341375,7.666244,4.463018,-5.658943,2.715531,1.069133,-2.826458,-1.922963,-0.861470,9.001943,-4.827174,7.047506,-1.556403,-1.168227],[-8.852276,6.038760,-1.859707,-5.600936,-9.323980,-9.806766,6.853460,7.044459,-3.198406,5.074198,-0.609967,-4.949302,-9.429680,0.929583,6.543119],[4.862419,-4.488500,-2.243150,0.516691,7.350935,-8.954182,7.168646,4.065759,7.985114,8.760117,-7.981390,9.458638,-1.275821,-2.397686,-9.881422],[-7.354908,-4.293693,2.728961,8.122928,8.685586,-7.653393,8.382836,4.668861,9.242141,-7.269430,8.855416,-0.039032,-8.174547,-8.747922,-4.522114],[-3.414634,6.728858,4.678497,0.655393,0.053791,4.392267,-8.868449,-5.462450,2.410221,-4.007660,-9.129846,-0.996057,9.668623,0.642475,-5.143510],[-3.671157,-0.424376,4.605260,-4.642971,5.068343,3.690846,-1.028478,3.539926,0.630716,-8.726198,-2.731348,-0.279697,7.594280,1.034729,4.078685]],[[-1.605487,-7.373547,2.795844,-4.923433,0.125025,-9.716573,5.007929,-7.722633,8.075509,1.263753,-8.077695,-0.419784,0.527010,-1.192842,-4.643960],[-4.013869,2.712203,-8.131946,-0.401140,0.999473,-3.896965,-9.192883,-0.139779,-0.975940,-5.053343,6.102951,2.773164,2.162340,6.047525,-0.202357],[-7.378990,-8.678739,6.373041,-6.212830,3.355027,3.837369,9.313067,2.938606,2.640298,4.728280,-7.851827,-9.188168,-1.568780,-8.673008,6.126331],[-8.162301,9.873819,4.451118,8.175072,-0.433858,9.997758,-5.411525,5.312337,-6.261624,9.783604,-3.507326,-0.344589,1.820314,4.510842,-6.181922],[-9.497539,-4.735671,9.493915,8.699367,7.953435,-6.063309,1.574460,-8.322359,-5.841834,1.028800,-8.004953,1.790492,-3.598307,-2.388120,-2.958978],[-0.105955,0.715256,-5.730509,1.521398,8.043414,6.324453,1.382144,-7.492862,3.631396,9.310476,-8.538520,9.271445,-9.070201,-9.316391,8.778165],[-8.366849,-7.590104,-9.968536,-6.379869,-6.468544,-9.997987,6.824596,-7.670204,2.897030,0.400810,6.136206,7.997078,2.509517,-2.279859,-7.987020],[1.257487,-1.900498,-9.577582,-5.045179,-5.115351,-0.668585,8.270283,-8.259858,6.069267,5.963698,-3.159024,-9.051181,3.678545,-1.927450,9.768348]],[[2.237770,1.887762,-5.990793,-2.662369,-5.361970,3.445362,-5.792413,4.175810,5.726276,-0.930838,9.426868,9.586209,-4.098561,6.614966,-1.441940],[3.918506,1.720057,6.250268,-5.389676,9.256004,-4.851401,6.397008,5.576850,-8.405558,4.419117,1.443488,4.434138,-8.329622,-9.496943,-7.901123],[5.515856,-5.623978,-0.294203,-4.008864,-2.936601,-8.886207,9.242567,4.974974,-4.356401,7.781639,-2.917623,-4.243884,5.529452,-6.446941,-9.117269],[-8.667116,-3.658086,9.552407,9.352744,-8.150176,5.623405,-5.658292,-9.382976,1.565645,8.776442,1.579794,9.310380,-9.598725,-8.057869,-1.452017],[7.388089,-6.527685,-8.654782,3.148060,-9.347258,5.629647,-6.343185,-4.003597,7.383868,9.576875,-2.350199,-9.720454,-4.046215,-8.377037,6.636915],[8.257929,1.790397,4.474492,2.320695,4.250087,-6.920917,2.949890,7.276240,4.858746,4.484804,5.985531,7.540225,-1.072992,-7.102389,5.983910],[3.244427,9.499565,-9.943068,-3.302487,6.558419,6.407911,-6.719844,-8.457077,-6.794322,-1.051241,-6.884458,4.754995,-2.394746,7.712162,-7.502581],[-1.900118,5.872650,3.328248,-6.312663,-4.679705,8.767106,5.782607,-3.580062,0.908725,-6.889289,0.701126,-7.394047,-9.450204,-3.431554,3.050163]],[[-3.133765,-5.925590,1.041133,-4.823194,-8.653930,0.136913,-7.229670,9.465301,-4.020371,-9.508892,3.244179,5.656207,-6.551960,-4.620409,9.137637],[-3.932574,2.269059,-1.329484,-3.473994,2.259758,5.819886,-3.455928,5.769937,-8.952382,1.318343,-9.083546,-9.771260,-3.941575,-5.269578,4.756774],[-3.552813,0.186559,9.535724,6.695157,-1.225493,-3.417940,9.576415,-6.674881,-4.785153,1.801221,1.569500,-9.946301,0.633169,-9.531768,3.457715],[-4.385572,2.486882,-2.163051,9.067555,-0.875024,-1.891838,0.968419,-6.049552,-0.069986,-5.421937,-4.415491,-5.797825,-9.560629,4.882050,2.319825],[-9.029701,-2.947658,8.426710,-3.725996,-2.775581,4.263072,9.712785,7.853695,-1.899317,5.355192,5.888185,-4.028666,-8.536690,5.258795,5.062391],[4.906733,-8.767076,-5.706438,-9.242471,-7.841447,7.731736,0.603244,-9.778892,-7.882136,-6.914456,-0.133532,3.432813,3.488728,0.641866,5.830715],[4.072771,-0.627930,7.683036,-8.005059,-6.379367,-1.956078,-8.574600,-3.331202,-6.115013,5.291584,-3.625087,-9.382458,-3.436525,-6.401693,2.276087],[-4.897379,-3.296683,-6.315294,3.459089,3.956913,-6.100894,-1.075447,5.795834,2.454416,7.932427,-0.818624,-6.652262,-5.205414,7.056193,-4.970862]],[[-7.977921,2.869571,-6.945168,-0.629561,-8.702788,2.806867,-3.857942,5.839249,-6.646088,1.942915,3.562812,-5.985507,7.442832,-1.426518,8.293627],[5.969980,-8.634803,-8.032447,-4.003064,-1.152411,-5.860161,1.865666,9.843845,-7.053829,-0.705319,-0.389245,4.900256,3.053942,2.621770,9.119659],[4.055915,-3.957331,-8.072778,-6.304927,-2.964120,7.566645,-0.952021,4.560647,-5.149036,8.909056,2.759187,-4.318307,-6.764986,0.889351,-1.258532],[-9.742938,0.215470,3.644918,9.367531,0.501898,-7.840540,-1.268714,9.703226,2.981580,8.455432,-4.763350,-2.026162,-8.565288,5.120681,-6.479936],[-1.520964,1.824922,5.064958,3.320174,-3.037608,-3.220162,-0.817732,5.042246,-9.520116,4.888915,2.456618,5.941771,-7.680185,3.559172,3.497832],[9.810898,-2.540995,-4.517512,3.399437,4.928652,-9.484344,3.812665,-8.358396,-0.672209,8.811706,0.253603,-9.007802,-1.822434,-0.859771,-6.221560],[5.492673,0.197860,-6.198520,8.350243,-5.239512,5.885472,0.984249,3.197957,4.286935,-9.285992,5.190371,7.431568,-3.110869,-3.791835,6.205857],[3.814729,2.243241,9.759881,-8.417826,6.295290,6.645749,0.806818,7.853448,-9.418768,-4.378023,6.383677,-1.605052,4.522067,-0.006821,6.729777]],[[-8.703313,-1.808209,-6.762389,2.080077,9.520020,6.605169,3.327487,4.028087,2.015673,0.305403,-4.701646,6.059066,-6.511984,-3.777216,-1.164195],[-2.352926,-4.432361,-8.925059,-4.680045,1.696016,5.568687,-3.500733,1.722309,0.338491,-1.376649,-9.178508,-9.595213,3.324072,0.842287,2.181829],[-3.565937,-7.358273,1.689307,2.991473,8.032812,7.660169,2.914964,4.848840,1.693782,7.029055,-8.580745,-2.399579,9.660749,9.451493,8.844524],[-2.809271,-5.044079,-8.459156,-3.457136,-6.155818,-9.869615,-6.054215,7.494361,-9.888541,-4.620818,-5.106212,-2.340944,4.732575,8.769526,-4.194293],[-7.862505,-7.121348,3.882243,-0.474012,-1.965655,2.630132,-2.647789,-7.287281,-0.650085,-6.413567,-7.339182,8.981505,0.293361,-5.100776,6.362413],[-4.155556,2.300187,-3.190067,1.677885,-8.380676,5.474346,2.879347,2.120689,-4.280063,-9.093785,3.595745,3.912683,5.261091,7.586304,7.595205],[-9.395792,-4.882738,-6.157098,0.673073,1.357712,3.821934,7.548970,-1.095772,-7.185399,-2.417825,9.755845,7.647669,-4.517782,-5.787228,-4.807395],[-9.400003,7.490675,6.620756,-3.925466,9.040207,-5.539317,-0.532344,9.280345,4.537874,7.374402,2.292488,5.174670,-9.706135,0.803024,3.844132]],[[-8.213830,6.564117,9.353968,-3.665435,6.036240,0.728816,-6.849423,8.581796,2.857669,-6.643492,7.021160,2.720037,-8.058314,-6.264373,-6.706810],[-3.787732,-5.410605,-7.146486,-9.252372,8.276846,6.574344,4.768983,-7.387640,8.463846,7.604926,9.608155,6.223469,1.197659,-6.149531,-7.684966],[-3.203701,7.411888,-7.773484,-7.373025,-2.249904,-0.745042,-3.005865,-3.162741,-2.093117,-8.507938,1.191684,-1.779426,0.083061,-3.567094,-3.010941],[-0.278293,4.907425,1.505692,-0.173232,-1.572107,4.677766,-4.843604,7.042163,-3.175699,-3.404343,1.938594,-3.200542,7.264028,-9.970777,2.606544],[-1.532465,5.186066,-2.031748,9.321791,-3.435723,5.483170,-9.273415,5.839202,-6.739422,0.056502,0.980958,-9.698754,1.017154,1.485983,-2.751326],[-9.891802,-2.790423,-6.467450,-5.687322,6.337069,-1.275698,-0.880023,-0.247192,-8.075443,0.642246,-4.689633,-7.815351,0.884671,-0.186611,6.460180],[2.186359,5.806379,1.734772,-5.020003,6.459464,-1.608570,2.559033,-4.733980,3.446851,-5.705990,-8.359835,5.298263,-0.446654,-6.682619,3.135018],[4.375413,2.373705,-4.688619,-5.261771,-0.488618,3.251578,0.964407,7.219744,-7.974352,-3.110535,-2.763801,6.083655,-8.189008,-0.837071,-7.043519]],[[-7.174241,-4.669178,-0.573872,3.060321,-4.304225,-4.178214,-6.817348,-4.642091,7.414408,-7.275087,1.735362,0.032863,-1.069223,-8.267418,-5.420446],[-7.824150,-9.583865,3.737672,-2.014595,-9.600578,-4.045747,-2.905730,-1.666550,5.271099,6.164035,-7.306059,-8.408943,-3.091579,8.306956,3.117518],[5.707061,-6.974805,-8.467610,3.138363,-9.372213,5.260356,-1.875270,-5.830352,-1.472232,0.445865,3.032010,1.001349,5.480481,9.585809,-1.712338],[-8.720852,-2.996005,-4.097104,-1.246924,7.137851,7.212736,-7.059029,-8.667341,-6.771660,-4.159743,0.826426,2.433060,6.144721,-1.082692,4.766507],[5.520086,-7.098937,6.327167,-0.407885,-0.956906,-5.972970,8.922127,-0.758158,4.947316,-0.996243,-5.140505,-2.077274,-0.592812,-8.142517,-1.939207],[-5.864196,0.563557,7.875915,6.519718,9.595121,-4.784429,9.284855,-3.913703,1.148267,-9.276854,5.213626,2.401901,0.589148,2.831350,-0.066075],[3.257961,1.444419,-5.061785,7.027995,-8.893854,5.114171,7.286151,-1.862608,-7.294508,0.204010,-8.276197,1.384287,-2.630885,5.367443,-9.232636],[8.357499,-4.761109,2.901841,-0.089677,-4.783988,0.026969,0.571229,-7.493836,-2.172630,5.079835,-2.416998,-4.351152,-9.612561,-0.413810,-4.237317]],[[2.057424,-4.193434,-6.710709,-1.934168,5.378570,3.050156,6.391733,0.988503,0.515669,-3.436200,3.123812,-2.683983,2.516597,9.765880,-8.107903],[-9.875441,8.366681,-4.069172,-6.667985,-6.606427,2.886379,-6.950537,-7.539078,4.716322,8.187665,7.743154,-7.234564,-7.622432,-4.171852,4.520929],[4.356262,-6.136619,-1.861229,-2.831647,-7.371128,-2.485953,1.655198,-9.086962,-0.105957,4.520631,8.139578,5.321142,-0.967349,1.250666,4.999478],[3.426388,0.384719,4.713758,-7.622602,-5.817819,9.534803,5.086730,-3.697116,-3.936443,4.225674,-0.104493,-7.370474,-9.993462,-1.525906,5.411826],[-7.878845,-9.733738,3.875987,0.513921,-0.006511,-7.960378,6.802048,-0.360201,1.330187,-6.595276,-7.131092,7.204860,-8.498989,3.094366,-6.933419],[-3.299790,0.855664,-5.051585,6.043522,8.594489,3.888306,2.503637,7.879593,-4.140168,-1.541437,0.461793,-0.754707,-0.703425,-3.090441,2.613023],[-5.730133,1.557634,-2.596850,-8.720728,2.064181,1.879504,5.394327,7.573491,-7.828684,5.369546,3.496157,6.879362,-0.059838,-6.755324,1.376309],[9.851589,-9.052434,-3.661164,-7.897053,-4.695145,-4.572454,-4.881595,-7.316473,-0.659050,-1.394923,3.559146,-0.720224,3.166862,-3.396651,5.582705]],[[3.738151,-7.398167,9.783948,-6.017712,2.982600,5.747788,8.064727,-7.374780,-3.286056,-3.217206,-9.165703,-0.467509,6.557657,0.885244,4.605033],[8.404668,5.900480,-3.849269,-1.978528,-2.385070,0.342465,3.349852,-2.145562,-9.800575,-3.681322,8.321381,3.159071,1.742070,4.578691,-7.204025],[4.867006,7.810380,7.500950,2.216941,-6.581745,-6.665313,-0.304156,-6.940980,4.293960,1.555770,-2.571304,-9.322275,-8.117340,-5.003888,8.857523],[-7.136378,-9.710502,4.056534,-6.154127,-0.437938,6.249593,-2.500190,-0.453964,-5.496830,-0.100288,-9.278646,-9.990448,-7.175534,-0.238706,-8.634473],[1.987121,7.522777,-9.677864,-2.104055,7.104227,6.311224,9.086017,-4.220228,7.965777,3.401546,-4.516475,-4.377826,-6.665957,1.135249,7.082139],[-3.676488,1.188727,-5.960367,6.464345,-4.761351,8.842830,5.020228,7.673195,4.298583,-2.058701,-6.767428,-0.725926,5.773080,3.326659,5.673320],[-7.132801,-1.524505,2.280893,3.491411,5.103176,-8.201647,5.899003,0.195301,8.790096,2.154945,9.581889,8.163744,-1.412438,-1.534314,8.613532],[-7.470496,-7.218771,3.680198,-8.514841,-0.605776,-9.417663,-6.663445,-5.844774,4.909289,-5.015464,1.141346,-9.743506,3.880701,1.735190,1.403751]],[[-1.927756,-0.717590,-4.189090,-4.750591,-8.955509,-5.217603,9.460937,-8.684731,-2.264554,-1.202710,2.569472,-9.598651,-7.845409,-6.714885,1.631605],[-5.143063,-7.891670,-2.908476,8.117937,5.310625,5.548273,-7.780997,-7.574208,-4.388488,-1.300915,-1.950569,-7.940782,-1.489438,-8.314629,-6.142720],[-4.074421,2.639316,4.037551,3.223586,6.228422,-0.692746,-0.556618,9.399619,-6.846487,6.000546,-6.802461,-4.944490,-8.149105,2.640801,1.102083],[-3.190206,3.484808,-4.150428,-4.838424,2.579792,-2.727287,-9.259990,-2.409714,-5.403344,-0.381190,-9.119924,8.585145,8.065324,1.313119,-4.701940],[5.617359,-7.674017,4.741376,4.011317,-6.811232,3.187915,6.866129,3.064015,4.157157,-1.072159,2.595127,1.071598,8.996090,-7.007513,3.989389],[5.705068,4.575118,3.141225,6.358176,-2.348000,6.130254,-5.031155,-5.366421,2.111366,6.152632,1.887449,-6.584331,5.737758,8.391017,-8.523040],[6.353071,0.838611,4.139119,6.325619,-9.363115,-7.970324,7.527503,-9.457155,-4.146206,2.562888,4.896545,-4.136274,5.773614,6.159703,2.827474],[-7.439440,9.562192,6.199589,-1.765455,1.903431,3.838064,1.868095,3.137139,-3.323397,9.226376,1.941553,-0.916158,-8.409009,-2.185220,-7.809811]],[[9.631005,-7.203216,8.210990,4.927388,-7.639515,-0.552673,-5.350250,-1.508552,2.569098,3.176314,-3.130191,6.130310,-5.485571,5.762558,2.238236],[-3.281494,-4.361070,9.162228,-9.031970,0.406811,-4.312699,-9.423163,3.625428,-1.372477,0.767251,2.038626,-5.515150,-9.370054,-8.439077,3.659594],[-3.822311,-6.527735,-9.348848,-1.099976,-3.600594,8.427968,6.989802,1.176960,-2.032879,0.052826,8.127120,-8.319889,0.925560,-8.948213,-9.558497],[3.512420,3.221198,1.039310,3.352281,0.184676,0.893451,-4.013397,-1.615944,-5.365119,2.577810,4.340048,-8.054102,7.433281,-8.406600,-0.105895],[6.784408,9.682087,7.916902,9.184501,-4.367370,2.357474,3.323964,-0.663488,6.375495,1.606415,-2.647265,-3.659622,-6.032079,-6.931950,5.435634],[3.539593,-9.845303,-0.569486,7.829629,2.832186,-1.722951,2.336960,-4.725034,1.092827,-1.783666,1.420673,2.511003,-7.510248,5.352734,1.534389],[3.745538,4.662322,0.046069,8.598750,3.257573,4.486880,2.407986,-3.172054,-0.801199,-8.662069,-2.499570,-3.363747,3.059479,2.329729,0.288589],[0.398413,7.705088,0.895589,-6.154796,2.045683,6.184263,9.814410,0.237031,-5.350168,-9.604906,1.836863,-9.564199,-4.422981,-4.352606,-7.126103]]], dtype = "float64")#candidate|5095|(15, 8, 15)|const|float64
uop_5096 = relay.log10(const_5095.astype('float64')) # shape=(15, 8, 15)
output = relay.Tuple([uop_5096,])
output2 = relay.Tuple([uop_5096,])
func_5104 = relay.Function([], output)
mod['func_5104'] = func_5104
mod = relay.transform.InferType()(mod)
mutated_mod['func_5104'] = func_5104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mutated_mod.get_global_var('func_5104')
call_5105 = func_5104_call()
output = call_5105
func_5106 = relay.Function([], output)
mutated_mod['func_5106'] = func_5106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_5206 = relay.TupleGetItem(func_5104_call(), 0)
call_5207 = relay.TupleGetItem(func_5106_call(), 0)
func_1061_call = mod.get_global_var('func_1061')
func_1063_call = mutated_mod.get_global_var('func_1063')
var_5210 = relay.var("var_5210", dtype = "float32", shape = (90, 2))#candidate|5210|(90, 2)|var|float32
call_5209 = relay.TupleGetItem(func_1061_call(relay.reshape(var_5210.astype('float32'), [4, 9, 5])), 0)
call_5211 = relay.TupleGetItem(func_1063_call(relay.reshape(var_5210.astype('float32'), [4, 9, 5])), 0)
output = relay.Tuple([call_5206,call_5209,var_5210,])
output2 = relay.Tuple([call_5207,call_5211,var_5210,])
func_5221 = relay.Function([var_5210,], output)
mod['func_5221'] = func_5221
mod = relay.transform.InferType()(mod)
var_5222 = relay.var("var_5222", dtype = "float32", shape = (90, 2))#candidate|5222|(90, 2)|var|float32
output = func_5221(var_5222)
func_5223 = relay.Function([var_5222], output)
mutated_mod['func_5223'] = func_5223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_5264 = relay.TupleGetItem(func_5104_call(), 0)
call_5265 = relay.TupleGetItem(func_5106_call(), 0)
func_3768_call = mod.get_global_var('func_3768')
func_3771_call = mutated_mod.get_global_var('func_3771')
const_5267 = relay.const(-1, dtype = "uint32")#candidate|5267|()|const|uint32
call_5266 = relay.TupleGetItem(func_3768_call(relay.reshape(const_5267.astype('uint32'), [])), 0)
call_5268 = relay.TupleGetItem(func_3771_call(relay.reshape(const_5267.astype('uint32'), [])), 0)
func_1061_call = mod.get_global_var('func_1061')
func_1063_call = mutated_mod.get_global_var('func_1063')
const_5305 = relay.const([[-0.199821,-8.453305,6.306239,-1.093208,-3.388981,-5.997605],[-0.770272,3.428916,-1.480191,4.258695,0.443871,-1.249039],[-8.690940,9.109417,-0.162359,-9.951802,-1.114544,-8.593636],[5.246524,-4.547488,-0.868955,-9.110647,0.021273,9.418149],[6.179839,3.926079,6.484595,-2.205715,5.560859,-0.171476],[8.876002,-4.639324,0.721282,-8.540786,-3.707108,-4.658545],[8.453367,9.563322,-3.682130,9.150513,9.463928,0.071780],[-7.380865,3.200252,6.089958,7.884879,-4.528639,-1.231120],[-0.719192,-3.264696,6.825300,4.911541,-6.086441,7.052178],[6.374011,-7.875241,0.207585,3.638595,9.248235,7.635861],[-9.610396,4.618826,6.085560,-8.461281,-4.215679,-2.889795],[6.844463,6.719123,-1.388433,1.480812,0.956616,0.860504],[1.448466,-7.951083,4.103354,3.150536,9.903806,-6.263965],[-9.628407,-5.578942,-1.795458,-7.030284,8.939651,4.294097],[2.983440,1.584500,-7.178026,3.871864,-3.713738,-6.020437],[-5.404980,5.865496,-5.976586,-0.629222,5.774710,-1.310624],[8.675715,7.366520,-8.546731,-1.017754,4.773642,-5.541545],[-5.477373,2.472730,2.945276,-4.209426,2.696041,6.711446],[-7.384241,-8.336323,4.284041,3.327223,-0.642189,7.570078],[1.164108,-9.121970,0.410785,-1.457801,-5.257103,-6.825093],[5.508708,4.074773,9.487792,-8.932221,-1.520037,6.194673],[6.049079,-8.628109,0.213774,-5.827066,-7.462408,-3.136826],[1.516138,5.931774,-2.628864,-0.043184,5.123360,5.957432],[-0.745439,-3.273743,-2.777712,-0.074006,-0.829616,9.688340],[-2.827585,-4.882020,-0.408465,2.035590,8.972212,-3.427589],[-8.408346,9.096157,-2.507100,-2.686313,-1.364568,-1.771484],[-3.305433,9.239908,2.365568,7.565183,-9.160957,-5.689379],[-1.763234,7.597261,7.024501,6.288507,-7.664938,7.234954],[0.477637,6.278828,-0.077820,8.737407,6.754844,2.264776],[8.438637,-7.383533,-3.969657,9.637672,-7.184307,-2.007111]], dtype = "float32")#candidate|5305|(30, 6)|const|float32
call_5304 = relay.TupleGetItem(func_1061_call(relay.reshape(const_5305.astype('float32'), [4, 9, 5])), 1)
call_5306 = relay.TupleGetItem(func_1063_call(relay.reshape(const_5305.astype('float32'), [4, 9, 5])), 1)
bop_5313 = relay.divide(call_5266.astype('float64'), const_5267.astype('float64')) # shape=(6, 3, 2)
bop_5316 = relay.divide(call_5268.astype('float64'), const_5267.astype('float64')) # shape=(6, 3, 2)
func_4654_call = mod.get_global_var('func_4654')
func_4658_call = mutated_mod.get_global_var('func_4658')
var_5322 = relay.var("var_5322", dtype = "int64", shape = (630,))#candidate|5322|(630,)|var|int64
call_5321 = relay.TupleGetItem(func_4654_call(relay.reshape(var_5322.astype('int64'), [14, 15, 3]), relay.reshape(var_5322.astype('int64'), [14, 15, 3]), ), 0)
call_5323 = relay.TupleGetItem(func_4658_call(relay.reshape(var_5322.astype('int64'), [14, 15, 3]), relay.reshape(var_5322.astype('int64'), [14, 15, 3]), ), 0)
uop_5344 = relay.log(call_5264.astype('float32')) # shape=(15, 8, 15)
uop_5346 = relay.log(call_5265.astype('float32')) # shape=(15, 8, 15)
bop_5350 = relay.floor_mod(uop_5344.astype('float64'), const_5267.astype('float64')) # shape=(15, 8, 15)
bop_5353 = relay.floor_mod(uop_5346.astype('float64'), const_5267.astype('float64')) # shape=(15, 8, 15)
bop_5357 = relay.minimum(var_5322.astype('uint64'), call_5304.astype('uint64')) # shape=(1, 9, 630)
bop_5360 = relay.minimum(var_5322.astype('uint64'), call_5306.astype('uint64')) # shape=(1, 9, 630)
func_1180_call = mod.get_global_var('func_1180')
func_1184_call = mutated_mod.get_global_var('func_1184')
var_5369 = relay.var("var_5369", dtype = "bool", shape = (1120,))#candidate|5369|(1120,)|var|bool
call_5368 = relay.TupleGetItem(func_1180_call(relay.reshape(const_5267.astype('uint64'), []), relay.reshape(var_5369.astype('bool'), [14, 5, 16]), ), 3)
call_5370 = relay.TupleGetItem(func_1184_call(relay.reshape(const_5267.astype('uint64'), []), relay.reshape(var_5369.astype('bool'), [14, 5, 16]), ), 3)
func_3593_call = mod.get_global_var('func_3593')
func_3596_call = mutated_mod.get_global_var('func_3596')
var_5376 = relay.var("var_5376", dtype = "float64", shape = (1456,))#candidate|5376|(1456,)|var|float64
call_5375 = func_3593_call(relay.reshape(var_5376.astype('float64'), [14, 8, 13]), relay.reshape(var_5376.astype('float64'), [14, 8, 13]), )
call_5377 = func_3593_call(relay.reshape(var_5376.astype('float64'), [14, 8, 13]), relay.reshape(var_5376.astype('float64'), [14, 8, 13]), )
output = relay.Tuple([const_5305,bop_5313,call_5321,bop_5350,bop_5357,call_5368,var_5369,call_5375,var_5376,])
output2 = relay.Tuple([const_5305,bop_5316,call_5323,bop_5353,bop_5360,call_5370,var_5369,call_5377,var_5376,])
func_5378 = relay.Function([var_5322,var_5369,var_5376,], output)
mod['func_5378'] = func_5378
mod = relay.transform.InferType()(mod)
var_5379 = relay.var("var_5379", dtype = "int64", shape = (630,))#candidate|5379|(630,)|var|int64
var_5380 = relay.var("var_5380", dtype = "bool", shape = (1120,))#candidate|5380|(1120,)|var|bool
var_5381 = relay.var("var_5381", dtype = "float64", shape = (1456,))#candidate|5381|(1456,)|var|float64
output = func_5378(var_5379,var_5380,var_5381,)
func_5382 = relay.Function([var_5379,var_5380,var_5381,], output)
mutated_mod['func_5382'] = func_5382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_5409 = relay.TupleGetItem(func_5104_call(), 0)
call_5410 = relay.TupleGetItem(func_5106_call(), 0)
func_2250_call = mod.get_global_var('func_2250')
func_2254_call = mutated_mod.get_global_var('func_2254')
const_5429 = relay.const([-4.299291,0.941926,5.198725,-5.968001,-7.779099,0.776122,-8.113733,-5.666367,-0.431703,0.654183,8.181220,-7.227338,-1.887912,-0.331729,-1.815956,9.684074,1.076379,9.725042,8.861471,1.277564,1.596634,0.287283,6.009994,9.893334,-7.057894,8.403444,7.461551,-3.076568,-6.728077,0.605666,5.868205,-1.143774,1.202548,3.315510,1.020628,-0.026643,3.536144,-1.318575,-3.556452,2.531377,5.778953,-1.078838,-0.654818,-3.533881,1.930573,2.295176,-0.326084,3.651694,2.720301,-3.268430,6.502677,-0.339178,9.339678,-5.003575,-1.379994,-6.087686,-2.463399,-2.155106,9.192514,4.238995,6.690131,-3.218925,-8.539700,8.947824,-5.799651,-6.364827,3.519035,1.107074,-5.193512,-7.152806,7.405830,-8.284932,5.454729,-9.850317,3.916831,4.982956,-1.388526,-6.620746,5.777381,5.712538,0.366201,4.466246,-8.157191,5.041281,-2.656665,8.097409,8.678110,3.252854,6.682518,0.496281,-0.012686,7.835511,-5.481018,5.786531,4.374597,-8.610620,1.304250,0.527078,-6.848989,-9.003729,-9.244699,-4.611276,5.754636,-9.590218,9.575807,6.457313,-4.110259,-6.958912,-8.328387,-0.302733,-1.309587,-2.485257,5.634184,8.462861,9.342282,-5.747694,-0.049296,5.513139,2.817406,-5.087783,0.046568,-0.319544,-1.474089,4.701048,-7.493878,-7.864132,-2.550865,-4.356727,1.328249,3.405580,4.582164,-3.296052,-2.391384,0.073721,-8.533530,-0.764917,7.318054,6.468857,4.678549,-7.322030,5.542384,5.235482,-5.626751,4.612253,3.993486,-9.809318,-5.941774,-3.462227,-0.449695,-3.831742,5.285208,-2.322737,2.446677,-5.639565,-0.148300,0.206874,-5.129832,1.891425,-7.574812,-0.210756,3.915489,8.917119,0.294233,-2.714588,2.340111,-2.900702,7.918833,-9.358066,7.642796,-1.370263,6.571802,1.057188,-3.017522,-2.888544,6.046193,-0.286206,8.893851,-6.644874,-7.772381,-9.510130,-4.299905,-6.014213,-3.738914,-1.498333,-8.734131,1.665499,-6.326195,2.710958,-6.788656,-0.221011,-8.014130,-8.957365,-7.383033,-2.424465,-2.711492,-7.628157,-8.206063,-6.736616,1.842448,-4.968780,0.959172,-1.512981,-8.924523,-9.645402,2.472478,-2.798458,-6.257385,-6.446902,1.799398,3.168554,8.305942,-2.144767,-0.605408,-1.609135,-9.929850,3.661674,8.264798,4.632881,3.142638,-7.032229,-2.389558,-1.591985,8.758811,9.304266,-8.395431,-0.024840,3.727151,2.751175,-9.053734,4.419988,-2.635792,-4.965075,-0.726710,3.975406,-3.289683,5.652849,-8.022010,1.962212,-3.889338,-9.025728,5.318950,-2.402373,-3.603711,-2.739995,-0.860971,5.435570,0.980056,-8.891529,3.398193,7.802699,5.154662,2.628524,9.446775,1.490448,3.940156,-3.187393,6.553375,3.371689,-9.300560,-5.220789,-7.149974,6.829716,1.743232,5.574698,2.762359,-9.983531,5.629869,-6.126363,-8.189786,-0.975140,7.579585,-9.599328,-5.153762,-7.751240,-2.559355,8.464814,-8.957237,-2.362635,-2.289951,7.684948,-1.140789,-8.725806,2.945477,-6.210690,-5.539684,8.701797,3.479009,-6.320597,-2.752306,-9.544904,8.765345,0.537265,-8.184228,-3.304021,1.620357,-7.496153,2.402597,-6.570576,7.869048,3.124142,4.656425,-4.771029,-5.166423,-9.395059,3.859592,2.996829,-3.887889,3.499400,-6.821849,4.674767,6.432340,-5.474271,-2.072795,8.851328,9.308734,-9.328141,7.536576,-1.344966,6.254182,-8.548842,5.969682,-8.102174,-3.017707,6.123877,6.498371,3.087766,-6.042769,7.249993,-3.404235,3.943737,8.108807,-6.947383,-6.238629,1.478400,-4.333377,-9.398305,3.785157,0.440052,-8.849141,5.568129,-9.056394,-7.931179,-4.634127,3.635319,-8.931054,-7.827247,-5.924489,0.888090,5.124924,3.621291,-0.121119,-7.935282,-8.900854,-3.589536,-2.384730,-3.968654,-0.356450,5.738785,-3.606296,1.263062,0.532811,0.404183,-6.309621,-7.170702,5.066707,9.124670,-5.357025,5.838110,-4.119165,1.395093,8.051885,8.323810,9.198439,-2.039298,8.606326,-0.980480,-7.619436,5.512977,-7.891738,-5.395356,2.780769,-8.501885,7.780535,-6.666213,2.667532,-7.967110,3.340079,-8.834559,8.543694,-2.908657,-6.132916,3.945896,-8.392528,2.774254,9.860187,-2.020740,-0.385433,-4.158470,0.773268,1.906671,-7.351727,1.703667,7.596096,-2.478395,5.819446,2.485005,-8.456549,-1.867069,5.476801,7.864835,8.070948,8.307535,-1.182899,-8.970100,-4.832510,-4.196830,4.110744,-3.983718,3.933354,0.684934,-2.526317,-9.805355,-0.670096,0.866218,4.167382,-4.313559,5.841637,-0.318264,1.999141,1.004198,-4.260239,-4.009419,9.391292,-9.057434,-9.233899,2.976292,-1.964645,2.856817,-0.918196,1.088462,9.123413,0.741408,1.462877,8.694378,-8.095696,2.543740,-8.118839,-3.225634,-9.733283,7.304675,1.545842,4.289887,-2.521575,-9.332645,-5.634368,-5.200288,8.834949,-5.498835,3.937489,0.331350,-8.402780,-1.045974,-4.575327,-0.988636,7.853511,4.986042,5.121017,2.351018,9.258503,-8.090798,5.682064,-3.250774,-5.069410,8.119679,-2.308910,3.973917,3.024859,5.863151,8.392265,4.681378,3.425530,8.297260,2.292549,7.798816,-0.501628,-1.649412,-2.477335,-0.221096,6.106670,5.452616,-2.633473,-0.610472,-7.603825,9.901175,-4.681906,6.854611,-5.770673,-9.468706,5.060385,-6.546959,4.250305,6.588669,0.007226,3.890884,1.177480,-0.675687,1.357240,-9.692919,1.128138,5.731566,-8.181452,2.611325,3.994484,-8.933654,7.844623,-6.586784,-7.748304,7.264212,2.704988,-3.555334,9.671774,-0.632114,-8.035715,-1.358453,8.147883,4.845873,-3.899676,-0.067283], dtype = "float64")#candidate|5429|(528,)|const|float64
var_5430 = relay.var("var_5430", dtype = "float32", shape = (624,))#candidate|5430|(624,)|var|float32
call_5428 = relay.TupleGetItem(func_2250_call(relay.reshape(const_5429.astype('float64'), [11, 3, 16]), relay.reshape(const_5429.astype('float64'), [11, 3, 16]), relay.reshape(var_5430.astype('float32'), [624,]), ), 2)
call_5431 = relay.TupleGetItem(func_2254_call(relay.reshape(const_5429.astype('float64'), [11, 3, 16]), relay.reshape(const_5429.astype('float64'), [11, 3, 16]), relay.reshape(var_5430.astype('float32'), [624,]), ), 2)
output = relay.Tuple([call_5409,call_5428,const_5429,var_5430,])
output2 = relay.Tuple([call_5410,call_5431,const_5429,var_5430,])
func_5439 = relay.Function([var_5430,], output)
mod['func_5439'] = func_5439
mod = relay.transform.InferType()(mod)
mutated_mod['func_5439'] = func_5439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5440 = relay.var("var_5440", dtype = "float32", shape = (624,))#candidate|5440|(624,)|var|float32
func_5439_call = mutated_mod.get_global_var('func_5439')
call_5441 = func_5439_call(var_5440)
output = call_5441
func_5442 = relay.Function([var_5440], output)
mutated_mod['func_5442'] = func_5442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_5468 = relay.TupleGetItem(func_5104_call(), 0)
call_5469 = relay.TupleGetItem(func_5106_call(), 0)
func_1180_call = mod.get_global_var('func_1180')
func_1184_call = mutated_mod.get_global_var('func_1184')
var_5482 = relay.var("var_5482", dtype = "uint64", shape = ())#candidate|5482|()|var|uint64
var_5483 = relay.var("var_5483", dtype = "bool", shape = (1120,))#candidate|5483|(1120,)|var|bool
call_5481 = relay.TupleGetItem(func_1180_call(relay.reshape(var_5482.astype('uint64'), []), relay.reshape(var_5483.astype('bool'), [14, 5, 16]), ), 3)
call_5484 = relay.TupleGetItem(func_1184_call(relay.reshape(var_5482.astype('uint64'), []), relay.reshape(var_5483.astype('bool'), [14, 5, 16]), ), 3)
output = relay.Tuple([call_5468,call_5481,var_5482,var_5483,])
output2 = relay.Tuple([call_5469,call_5484,var_5482,var_5483,])
func_5490 = relay.Function([var_5482,var_5483,], output)
mod['func_5490'] = func_5490
mod = relay.transform.InferType()(mod)
var_5491 = relay.var("var_5491", dtype = "uint64", shape = ())#candidate|5491|()|var|uint64
var_5492 = relay.var("var_5492", dtype = "bool", shape = (1120,))#candidate|5492|(1120,)|var|bool
output = func_5490(var_5491,var_5492,)
func_5493 = relay.Function([var_5491,var_5492,], output)
mutated_mod['func_5493'] = func_5493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_5501 = relay.TupleGetItem(func_5104_call(), 0)
call_5502 = relay.TupleGetItem(func_5106_call(), 0)
func_2250_call = mod.get_global_var('func_2250')
func_2254_call = mutated_mod.get_global_var('func_2254')
const_5504 = relay.const([[-9.251373,8.781836,-6.182670,8.754783,5.393238,-9.032247,3.730005,-3.860304,0.424383,-6.362217,-2.460800,9.490501,-5.388051,-7.179809,5.324861,-8.332153,5.038931,-4.032652,-0.382436,-2.645841,-6.719480,4.547325,-8.850275,-4.926717,-4.042045,-7.080180,-6.291594,8.157189,2.861784,1.513045,3.021099,-9.283708,6.800322,-0.918093,0.388498,5.680245,0.387600,9.157427,-5.684756,7.604105,4.329186,-9.576936,2.196629,-2.420582,7.293793,4.199203,6.916603,0.143486,6.669276,4.556580,5.871902,-0.032102,7.803106,-1.167149,9.459485,-0.225662,2.465406,-3.479410,5.903314,2.012426,7.363714,0.773535,1.255215,7.741547,-6.752764,8.802187,-6.382427,3.644057,3.148221,0.878889,6.644277,4.546233,-6.256327,-1.289435,1.131181,-2.747426,-1.160316,7.170661,8.688717,-8.363268,3.403919,7.856294,-1.705184,-0.206841,-2.380436,-1.656266,3.985838,-4.739899,-8.039266,6.745677,1.495691,-4.346331,0.799092,7.620615,-2.465646,9.026013,2.927598,2.900260,2.762646,4.787072,-4.739528,7.669167,-9.026562,8.789331,-6.765389,-9.148455,6.510429,-6.524832,-3.613167,5.923273,4.128631,8.303857,3.693280,-2.386137,-7.217078,-7.368089,-0.762990,-8.540339,3.917643,8.314287,9.997103,6.181226,-8.651635,6.037968,9.341860,6.113748,3.680690,7.031287,-3.353467,7.763989,-0.386434,6.458846,-1.802514,5.607491,2.225578,2.148709,-4.969045,4.948109,-4.222213,1.873416,1.492522,8.933137,8.646004,2.492255,-4.240732,-2.369440,-3.383241,2.629099,-8.856898,7.831992,2.065674,-6.780141,3.202181,-4.045249,-3.129932,-1.890142,7.744305,6.718112,-6.713389,-8.190601,3.718812,1.586157,-9.362534,-1.826697,2.695564,-0.992154,7.658260,-3.404146,6.477451,-3.974775,5.919045,0.328175,-3.386843,2.716509,-2.786905,-1.457978,3.734771,5.830570,-4.033775,-2.550614,9.146462,6.256097,2.213058,-9.154603,-4.508286,-1.119971,9.964470,-8.667718,-8.334339,-4.562735,2.509420,6.583755,7.766969,-2.539294,-1.356553,6.698793,-8.140401,-8.708970,7.813433,-8.062784,-8.002556,6.189249,-4.652741,0.694037,5.828865,1.818824,-8.215047,6.951902,-2.484120,-2.348324,-6.412357,-6.467372,-2.101091,-7.167314,9.798010,9.955368,-6.803247,1.324592,6.816488,5.153154,6.195177,5.991515,6.239905,8.076181,5.685943,9.629308,1.809982,-5.175299,-9.303082,1.852029,7.635096,0.097558,6.694007,-6.670071,-2.440659,-3.493585,7.554814,6.583050,-6.960367,-2.902881,-0.952105,-4.581007,8.823671,7.657877,9.691461,-1.460765,-2.113335,-3.361546,-5.627863,-7.005782,9.523839,-7.273104,-6.171993,8.987071,-4.540589,-0.597180,3.652764,3.585922,1.849066,3.618885,6.762207,2.625279,0.637412,-3.220212,1.122921,-3.606689,1.801192,6.816200,8.358251,-8.341354,-6.952754,-3.962440,5.363739,-9.472597,2.228745,-6.014483,2.624458,-1.512706,7.837063,6.888859,1.574454,8.463784,-9.550334,-3.446098,-2.412049,-6.469088,-6.587933,-4.059749,-0.490956,-0.082957,-0.905713,-9.777386,4.796602,5.126184,3.569367,9.044260,-3.762654,0.164253,8.893947,-5.376624,9.587983,-7.531593,-3.365317,8.157662,8.539824,-6.558243,-9.376494,-3.903360,5.677902,1.715722,-8.300228,4.877163,1.668036,4.349142,-3.340499,-4.368846,-9.044730,5.507041,-2.431212,2.982924,8.568319,3.874009,1.479510,2.648651,1.360787,2.587474,9.852394,5.353093,-8.175365,3.063193,-1.271244,-7.973230,-4.142792,1.342643,-8.138633,-8.594802,-3.670364,-9.490813,0.898063,-4.297663,-8.530488,-5.567067,-8.488287,-3.984583,3.428863,-3.100809,-6.589698,-4.312796,-8.683585,7.654345,4.173730,-5.046372,7.526670,6.310443,-0.885608,-8.543353,9.647280,-2.507045,-2.299360,-9.607503,-0.608106,0.976762,2.905904,1.955918,-0.564505,9.657463,3.406844,4.559142,-6.564066,4.596174,9.318297,1.071897,6.136620,-2.932560,-5.739812,8.609707,2.927427,0.817525,-7.834790,6.588932,1.424826,-2.845702,-8.299983,-6.236333,-1.400389,-3.752758,7.945344,6.660638,3.259070,-9.264903,-8.296457,9.261275,-8.104475,3.050940,8.337940,2.578877,0.897779,0.718550,-1.695435,-0.825826,-8.179257,-1.128597,-6.484973,-3.657265,7.806422,0.399772,-4.080264,-5.555505,-5.327935,3.566080,-2.780866,-6.983313,8.821988,5.946480,9.603528,-0.244916,-3.049745,0.328181,-2.139531,7.690600,-5.619966,-2.391710,5.992674,-5.288577,-1.341140,8.506813,-0.860359,-8.484840,-5.267496,1.555669,6.640039,7.019797,-9.833247,-2.490859,-4.026520,3.079460,-7.038074,4.573965,-8.314624,5.260847,2.325174,4.553943,9.600599,3.416152,3.642658,8.940473,8.185673,9.914598,-7.590890,-2.806953,7.699142,7.125968,5.494817,9.113060,-1.699149,-6.967153,2.117038,-1.419498,7.622011,-9.805740,-8.728324,6.775295,-2.882493,-0.497598,-1.299524,9.668448,-5.698413,-8.765901,1.722686,2.238769,-6.741466,-9.664226,2.952169,-3.522942,-7.695247,5.227886,5.769848,-0.827288,4.120773,-8.192129,-6.252681,7.068515,-7.878845,-1.086346,3.182404,-7.309227,-0.955855,-6.350327,3.257333,-3.870832,9.942733,-7.246820,3.052366,3.822933,7.037684,-8.821457,6.504492,-8.185997,7.324236,-5.244798,-0.326272,4.439907,7.322862,-8.713588,-0.390546,-3.768151,9.431618,-8.615740,-3.950167,3.946861,7.126961,0.133908,-9.357328,2.035672,-9.281414,-2.403187,-8.626461,0.998174,6.712148,-9.387461,3.191360,-0.840521,9.281982,2.640542,-8.726588,-3.832173,-6.822652,-1.272841]], dtype = "float64")#candidate|5504|(1, 528)|const|float64
const_5505 = relay.const([8.321959,5.395666,2.494253,-5.718380,-9.185624,7.317031,-5.819058,-8.477972,-8.649233,6.167726,-9.422288,-2.010109,-9.073099,-8.811915,5.822307,3.395304,6.541864,-1.513246,-7.043475,-3.548891,-3.756071,6.419007,6.202723,-8.255972,-5.028080,-4.970756,2.138775,8.180582,-2.941750,3.380877,-8.741533,-4.916258,3.615000,-2.338319,-5.534565,3.659820,-6.624979,3.095758,-7.094837,4.808467,9.245543,3.776738,-3.647673,-6.877645,0.487825,7.799259,9.978524,2.822598,-0.671145,-0.998727,0.315282,6.453010,-3.433258,4.919747,-7.973689,4.872672,-0.512209,-9.445510,5.858488,4.574298,0.906874,-0.127493,9.065259,7.848380,-2.555572,-1.763945,3.970609,7.851803,-8.422651,-6.200036,-2.369694,7.600803,8.793101,9.292787,-9.821463,8.454872,9.150796,-5.826409,7.661590,-1.697095,1.511328,6.354279,-6.759187,-1.442773,3.350018,2.645533,-1.499033,-3.298500,4.252771,0.838232,7.840729,0.241585,-0.623544,3.751735,2.674004,3.818516,-7.464552,-3.938437,-7.725704,7.908644,7.095849,9.109186,6.465631,7.326543,3.676253,3.347150,1.012334,-2.615394,-9.477434,-2.420643,3.400572,7.368405,-9.978654,2.507086,-5.639478,2.269726,8.277019,-7.423952,-3.606439,3.659939,-4.418698,-6.159907,4.527487,1.776631,-1.186992,-6.516772,-9.656140,4.156080,6.812592,5.072278,-7.861687,8.498879,8.145019,-7.757548,-9.478175,0.911837,-2.427527,-7.115917,-0.252698,-1.140484,2.676806,1.150181,-0.996515,7.691180,4.643906,6.435590,4.359660,6.236826,-4.479564,-1.272709,-7.799844,7.451763,-5.952920,-2.868641,-4.235363,1.222506,1.080967,4.973381,-8.687287,4.710631,4.652908,2.463363,-6.852968,0.729425,-3.586087,5.568215,5.762805,-5.553668,-5.372347,3.158172,0.215159,4.359706,7.879501,-9.558899,4.470642,0.475433,-7.516654,2.790446,3.383543,-7.210582,-7.838238,-0.011797,-9.918778,1.003569,-5.670238,1.263921,-9.974054,-8.126533,2.596738,8.499969,3.077945,3.212514,2.517883,-0.122884,6.642755,-4.266805,-2.314112,-7.211958,2.043188,9.441632,-5.040983,5.224068,3.342728,-3.720729,-4.250225,5.636676,-3.171577,-7.405555,6.436607,-7.495879,1.371067,0.193352,-3.186543,-4.221739,5.187777,3.185201,5.710843,-6.233300,-3.138338,7.993320,-5.487299,-3.413268,-9.815441,-8.335554,2.883363,-2.298728,-8.681265,-5.322414,0.079956,-9.291436,0.964571,-9.198552,6.507604,0.661092,1.778378,-3.930813,-8.072079,-2.613661,4.240861,-6.590593,-0.211494,2.868767,-4.500163,8.392868,0.522111,4.216073,3.275078,1.405925,-1.057798,-5.497369,0.986787,-9.813248,-9.893668,-9.762902,0.024182,-4.120782,-0.776767,-7.873191,-1.605014,-3.823826,-2.392647,-7.626975,-4.988366,-4.525590,-0.798677,-2.407813,7.930989,4.022108,-3.249232,-1.424339,9.149638,8.893207,-9.434851,-2.761359,9.562177,-6.861452,-2.260104,7.560880,-6.329830,-1.471593,-3.871257,1.153084,5.478392,3.724021,-2.654212,2.599164,9.167275,5.263608,0.762691,-4.533013,8.147794,-8.304396,7.537405,-4.635260,2.335990,-0.379690,8.659943,4.772947,7.889810,-1.282711,-1.470540,1.633535,-5.020425,-3.907784,-3.170832,-8.304643,1.288363,-9.923586,-7.058071,6.025039,1.289930,-3.606275,9.732711,4.791309,-1.759703,-6.315895,1.835211,-4.264259,0.938342,2.705769,4.391208,3.020370,-6.295729,6.771552,-3.333788,-0.927775,7.798355,-9.056471,8.363475,8.023410,-4.493719,-3.273922,4.040182,1.292864,8.836037,-8.196898,0.135997,-5.035871,5.139112,-5.684898,-8.947789,6.525018,1.987143,-9.417732,4.003055,0.614101,3.455508,-3.915332,-9.855289,1.398672,-8.430563,2.063321,4.609926,-9.303518,3.697844,-9.775555,0.164187,4.755412,-2.003954,4.214625,9.425107,8.955094,9.245171,4.821015,2.327123,9.947122,1.620183,1.545501,-0.056716,3.402229,8.075166,2.211869,-0.592757,4.393136,-2.707283,-8.078219,9.048031,7.632639,4.620879,7.551452,1.510366,9.411645,0.239962,-4.985364,-4.503453,8.979739,4.002156,-0.413186,-2.630134,-0.995606,3.954877,-7.640481,-2.420316,9.697257,7.517705,3.244359,1.134806,7.902480,8.728689,5.409541,7.960091,1.497564,5.235368,-9.471377,-2.213503,2.434938,-7.003457,-8.458724,7.819043,-6.834775,-7.194823,7.873966,-3.119154,-2.353140,-8.063606,7.271697,8.203319,5.183329,5.141721,-4.549712,-9.637814,4.148573,5.132385,-8.961694,5.321528,8.422919,-0.710138,4.829629,9.823379,-9.908930,8.805458,-1.984874,8.714671,-1.778717,7.122565,-2.862059,-1.170816,-6.993662,9.777838,-3.942844,-8.258801,3.255222,-7.772598,3.657592,-9.466535,-5.633433,-2.400946,-0.895226,-8.662879,-1.924226,4.035194,8.402347,-7.661924,-8.162312,-4.477021,-7.927266,-6.512137,4.723899,-8.467512,8.189402,9.605674,9.999729,-4.923829,0.987265,-6.554074,-4.999072,-2.857699,1.178571,-3.223245,-5.637006,-4.342833,1.232311,-7.359150,6.963623,2.231948,-0.595839,-9.966031,-5.338376,3.989007,7.551686,9.681918,-1.422413,-6.522282,-1.995393,2.562036,5.481792,8.483720,-7.155054,-4.541430,5.381636,-6.095561,-5.674238,2.093895,7.435372,-5.628919,-9.404562,5.507234,2.673059,-4.822637,-3.079289,-3.169554,9.955598,-0.100220,-6.915332,6.237086,-3.679272,8.634526,3.996485,-4.851631,0.485308,4.838391,-2.933494,-6.775225,-6.212042,-6.688534,-7.358823,9.634854,-0.413054,-9.629025,-0.761125,-4.828950,1.203181,4.648714,-5.418905,-4.336271,-0.743241,0.588745,-8.024947,-0.613534,-2.828573,5.935704,3.187761,-8.192445,-6.331362,-4.036856,6.264799,1.235106,-9.801897,9.097288,-5.827651,1.816740,7.654340,-5.097068,-7.126250,6.731120,2.341914,-4.904932,1.704120,-6.322485,8.696489,-4.750942,-7.918932,7.431492,-3.354367,4.451701,-8.817007,5.363810,-7.856729,4.630126,-1.669199,0.616838,9.154003,-2.102131,6.368485,-6.426448,-3.614292,6.485762,0.837786,9.811422,3.031634,-5.390988,2.470071,2.239158,3.229514,6.651346,6.971568,2.362185,-9.132553,8.932363,6.998163,-5.790348,-2.183298,-9.692541,-5.250663,2.582713,-5.553169,-0.782187,6.754984,6.199266,-9.136384,-4.519802,-2.653496,5.760040,-3.148596,-9.053796,-7.927802,5.922115,-2.378789,-0.693585,8.557486,-9.102902,-2.300980,-8.719562,-7.487642,-9.733958,-8.553590,2.490026,4.316851,0.586494,6.595185,9.085509,-7.136235,0.073966,-7.918049,6.560813,6.687055,2.607863,-3.466845,-9.343759,-5.927429,-7.071045,8.526272,1.543795,-3.106314], dtype = "float32")#candidate|5505|(624,)|const|float32
call_5503 = relay.TupleGetItem(func_2250_call(relay.reshape(const_5504.astype('float64'), [11, 3, 16]), relay.reshape(const_5504.astype('float64'), [11, 3, 16]), relay.reshape(const_5505.astype('float32'), [624,]), ), 0)
call_5506 = relay.TupleGetItem(func_2254_call(relay.reshape(const_5504.astype('float64'), [11, 3, 16]), relay.reshape(const_5504.astype('float64'), [11, 3, 16]), relay.reshape(const_5505.astype('float32'), [624,]), ), 0)
output = relay.Tuple([call_5501,call_5503,const_5504,const_5505,])
output2 = relay.Tuple([call_5502,call_5506,const_5504,const_5505,])
func_5509 = relay.Function([], output)
mod['func_5509'] = func_5509
mod = relay.transform.InferType()(mod)
mutated_mod['func_5509'] = func_5509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mutated_mod.get_global_var('func_5509')
call_5510 = func_5509_call()
output = call_5510
func_5511 = relay.Function([], output)
mutated_mod['func_5511'] = func_5511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_5572 = relay.TupleGetItem(func_5104_call(), 0)
call_5573 = relay.TupleGetItem(func_5106_call(), 0)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_5574 = relay.TupleGetItem(func_5509_call(), 3)
call_5575 = relay.TupleGetItem(func_5511_call(), 3)
func_4050_call = mod.get_global_var('func_4050')
func_4055_call = mutated_mod.get_global_var('func_4055')
var_5577 = relay.var("var_5577", dtype = "uint8", shape = (252,))#candidate|5577|(252,)|var|uint8
const_5578 = relay.const(5, dtype = "uint32")#candidate|5578|()|const|uint32
call_5576 = relay.TupleGetItem(func_4050_call(relay.reshape(var_5577.astype('uint8'), [3, 6, 14]), relay.reshape(var_5577.astype('uint8'), [3, 6, 14]), relay.reshape(const_5578.astype('uint32'), []), ), 3)
call_5579 = relay.TupleGetItem(func_4055_call(relay.reshape(var_5577.astype('uint8'), [3, 6, 14]), relay.reshape(var_5577.astype('uint8'), [3, 6, 14]), relay.reshape(const_5578.astype('uint32'), []), ), 3)
output = relay.Tuple([call_5572,call_5574,call_5576,var_5577,const_5578,])
output2 = relay.Tuple([call_5573,call_5575,call_5579,var_5577,const_5578,])
func_5582 = relay.Function([var_5577,], output)
mod['func_5582'] = func_5582
mod = relay.transform.InferType()(mod)
var_5583 = relay.var("var_5583", dtype = "uint8", shape = (252,))#candidate|5583|(252,)|var|uint8
output = func_5582(var_5583)
func_5584 = relay.Function([var_5583], output)
mutated_mod['func_5584'] = func_5584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_5613 = relay.TupleGetItem(func_5104_call(), 0)
call_5614 = relay.TupleGetItem(func_5106_call(), 0)
uop_5615 = relay.erf(call_5613.astype('float32')) # shape=(15, 8, 15)
uop_5617 = relay.erf(call_5614.astype('float32')) # shape=(15, 8, 15)
func_2250_call = mod.get_global_var('func_2250')
func_2254_call = mutated_mod.get_global_var('func_2254')
const_5620 = relay.const([8.326087,7.299059,-6.289990,-3.031315,0.654815,0.550831,1.194405,-1.588160,6.375631,3.185631,2.372591,6.898530,7.770493,5.937246,7.358258,-4.100143,-3.344480,-5.503573,-4.884539,-5.841257,7.735034,-6.118472,0.360633,-8.835773,-9.628942,2.948427,3.330813,-3.256877,-6.747824,7.479896,3.274789,-0.123071,6.272332,-1.766085,-6.193135,7.207155,-3.560155,-6.008786,-2.876573,-9.812321,-6.836667,7.047528,-4.275146,-3.157915,8.076991,1.476325,4.492383,-2.015876,-6.659772,-0.361626,1.241398,-0.667792,3.365696,2.499846,-1.825958,8.696714,-0.146826,-1.808201,-1.481609,2.616735,-7.704509,-6.148922,-4.779678,0.602057,-4.680311,2.461396,0.175930,1.523271,-6.154197,0.450198,4.831723,8.693104,6.674281,-5.235649,-9.154454,3.815750,-7.297196,-3.294627,-2.613152,-2.542222,3.986661,9.536264,1.076909,-9.784536,6.831463,-8.673503,-3.373555,-4.720064,0.424298,9.986087,-7.301913,7.393440,0.806210,-7.715086,4.672233,-7.584806,-1.245322,5.461013,-4.963534,-3.930827,2.028245,-2.092641,-9.630460,3.127709,-6.060494,-1.614104,6.187588,7.935913,2.250252,3.405697,-9.827827,-0.069308,1.082451,9.579704,0.408507,0.738966,-3.923634,-1.229168,2.260862,1.831458,-5.459879,-3.212174,8.710811,-1.796413,7.521381,8.726624,4.084339,6.395678,1.226002,5.436896,-4.562486,-4.764609,-0.374660,6.842003,-7.987298,5.346523,-6.411624,9.413405,-1.599028,8.858373,6.245410,2.959707,-6.730787,9.720408,0.577599,-7.453515,9.986688,6.575589,9.625668,7.303938,9.756617,-6.891268,7.921311,1.470492,-8.278614,2.650778,8.097582,-3.393437,5.947145,2.241243,-5.030808,-0.756130,-4.407708,-1.821227,9.340383,-2.622714,-3.424867,-0.380035,-1.520576,4.790386,-9.322072,-3.419346,-4.880042,3.322973,-4.254605,-3.828935,-9.800133,-7.181909,-4.588660,-1.740597,8.814288,-5.444756,-4.172931,9.530044,-7.818688,0.231257,7.785412,-3.190762,-4.622967,-2.302374,8.462944,-5.006899,5.967912,-2.600106,5.261734,0.265768,6.962016,-3.199432,7.490276,-9.851383,6.518681,-3.716554,5.217175,-7.606024,9.446224,-2.804889,9.280806,-1.760487,-7.775121,4.275594,-2.740256,-1.884851,-0.739188,2.876986,-5.027091,-2.272478,7.465094,-9.840653,9.989648,-6.882085,8.333358,6.197671,0.287950,-5.838383,1.210781,8.998467,-5.505606,8.764709,9.098634,-2.248347,4.417525,8.278634,-3.675672,4.219117,-3.484784,-8.157346,7.596621,-0.199996,3.381674,-0.518256,-5.740100,-8.912886,3.522609,-4.840741,-7.208575,-5.911485,5.107381,-3.434228,2.237028,8.244273,-1.130174,-0.563483,-2.767031,-9.383387,4.595226,-9.406430,8.350819,-7.149555,-4.327677,3.076999,-9.749702,-6.311054,2.752560,1.652494,8.591814,-2.551717,-9.499336,7.334627,1.523631,-2.229875,-5.599104,3.564145,-0.132344,-6.479553,-9.323104,8.254057,8.533497,-7.056130,3.944984,4.991907,-6.224259,-2.373971,-8.681948,6.178975,6.702106,-4.757960,-8.033961,7.848295,-5.417115,-2.633179,3.928017,2.461090,8.658243,6.634983,6.969486,8.513835,-2.525898,-4.705391,2.141064,3.602080,0.477681,-1.623695,0.305819,-9.794228,9.923199,-7.656620,2.458404,7.708743,9.640210,8.858302,-5.689456,-6.287417,-1.519081,6.247975,8.584406,-7.994451,9.113759,-4.439884,0.264141,-5.495701,5.224243,6.485127,-0.450687,-7.118719,-9.154970,-2.912807,-4.838807,9.859881,8.173418,6.500429,0.029159,1.005597,-3.193951,2.086231,3.423799,7.443529,-8.351260,4.443481,3.663094,-4.095473,2.496332,-4.396084,-3.218132,-5.628080,5.480835,-5.724643,2.616567,6.667928,9.212921,2.286800,-0.391798,-2.656048,-2.794862,5.786746,9.455979,1.941555,-7.249009,-2.370415,5.509776,-7.325717,-0.698409,-0.867953,-8.692527,-4.204501,-1.907430,-3.374439,-4.396287,-8.186640,-6.028532,-7.834704,1.310498,-1.129444,-8.435989,-9.333638,0.089833,-3.708059,0.628324,-5.311819,-6.195400,-9.075267,-4.129451,9.578167,3.674065,8.369851,7.021993,5.754747,6.928136,-1.547733,-9.174763,-2.727653,2.791568,-3.621007,8.285953,-9.714892,6.236295,-6.393223,-2.429237,-1.932171,0.303632,2.153466,2.520389,-3.333727,8.511035,-9.302292,2.274828,0.013550,4.315068,-6.553023,-0.290124,-3.921348,4.096669,-5.355358,-3.624287,8.228489,-2.294158,-5.693363,4.580518,8.565447,4.426719,-4.664546,-9.651999,2.328811,5.997515,-6.627302,7.458720,8.851304,5.989892,-8.785781,-2.663060,-2.962115,-9.530689,9.954151,1.932651,-6.329947,-9.035555,0.265317,5.086267,7.572722,-4.766182,-3.648091,-3.454135,-7.086448,4.783470,-0.193365,-1.550607,8.557152,7.018651,-0.045131,8.208773,-0.764835,-6.439211,-2.402485,-4.866841,-8.768634,4.687139,-5.183228,7.834869,4.793579,4.553261,-4.706278,-3.728612,2.996101,-9.612136,-1.502743,-4.776749,-7.188919,5.583238,-3.325993,-7.590301,-2.952123,-1.754041,8.415382,-3.668869,-8.545799,-1.559459,0.965462,-1.457570,5.006413,0.031876,-1.902876,-3.064921,-5.440495,8.392223,9.154099,9.584721,0.125652,2.588574,3.827624,-5.870637,2.840516,4.510109,0.136269,4.891028,-4.896451,2.825060,4.747479,7.111744,1.234693,-2.624347,-7.074112,-2.930381,7.824298,6.514270,9.126519,0.293710,-9.630855,-7.347088,-7.733714,-6.307447,-4.745926,-9.792337,4.084399,0.026499,-9.872352,-6.775760,4.465404,1.885376,-9.696300,-3.156091,-7.586035,-5.415995,-1.833943,-3.075807,6.419117,8.188141,-2.899748,9.866169,-8.310177], dtype = "float64")#candidate|5620|(528,)|const|float64
var_5621 = relay.var("var_5621", dtype = "float32", shape = (624,))#candidate|5621|(624,)|var|float32
call_5619 = relay.TupleGetItem(func_2250_call(relay.reshape(const_5620.astype('float64'), [11, 3, 16]), relay.reshape(const_5620.astype('float64'), [11, 3, 16]), relay.reshape(var_5621.astype('float32'), [624,]), ), 2)
call_5622 = relay.TupleGetItem(func_2254_call(relay.reshape(const_5620.astype('float64'), [11, 3, 16]), relay.reshape(const_5620.astype('float64'), [11, 3, 16]), relay.reshape(var_5621.astype('float32'), [624,]), ), 2)
func_2996_call = mod.get_global_var('func_2996')
func_2999_call = mutated_mod.get_global_var('func_2999')
var_5626 = relay.var("var_5626", dtype = "bool", shape = (720,))#candidate|5626|(720,)|var|bool
call_5625 = relay.TupleGetItem(func_2996_call(relay.reshape(var_5626.astype('bool'), [9, 16, 5])), 1)
call_5627 = relay.TupleGetItem(func_2999_call(relay.reshape(var_5626.astype('bool'), [9, 16, 5])), 1)
output = relay.Tuple([uop_5615,call_5619,const_5620,var_5621,call_5625,var_5626,])
output2 = relay.Tuple([uop_5617,call_5622,const_5620,var_5621,call_5627,var_5626,])
func_5628 = relay.Function([var_5621,var_5626,], output)
mod['func_5628'] = func_5628
mod = relay.transform.InferType()(mod)
var_5629 = relay.var("var_5629", dtype = "float32", shape = (624,))#candidate|5629|(624,)|var|float32
var_5630 = relay.var("var_5630", dtype = "bool", shape = (720,))#candidate|5630|(720,)|var|bool
output = func_5628(var_5629,var_5630,)
func_5631 = relay.Function([var_5629,var_5630,], output)
mutated_mod['func_5631'] = func_5631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_5635 = relay.TupleGetItem(func_5509_call(), 1)
call_5636 = relay.TupleGetItem(func_5511_call(), 1)
output = call_5635
output2 = call_5636
func_5645 = relay.Function([], output)
mod['func_5645'] = func_5645
mod = relay.transform.InferType()(mod)
output = func_5645()
func_5646 = relay.Function([], output)
mutated_mod['func_5646'] = func_5646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_5713 = relay.TupleGetItem(func_5509_call(), 2)
call_5714 = relay.TupleGetItem(func_5511_call(), 2)
uop_5720 = relay.rsqrt(call_5713.astype('float32')) # shape=(1, 528)
uop_5722 = relay.rsqrt(call_5714.astype('float32')) # shape=(1, 528)
func_5221_call = mod.get_global_var('func_5221')
func_5223_call = mutated_mod.get_global_var('func_5223')
var_5724 = relay.var("var_5724", dtype = "float32", shape = (6, 30))#candidate|5724|(6, 30)|var|float32
call_5723 = relay.TupleGetItem(func_5221_call(relay.reshape(var_5724.astype('float32'), [90, 2])), 2)
call_5725 = relay.TupleGetItem(func_5223_call(relay.reshape(var_5724.astype('float32'), [90, 2])), 2)
func_5582_call = mod.get_global_var('func_5582')
func_5584_call = mutated_mod.get_global_var('func_5584')
const_5728 = relay.const([[10,6,-1,6,10,8,9,-10,-6,-3,8,-7,9,-7,-9,8,-7,9,3,-1,-9,1,-4,3,3,8,7,-4,9,3,-10,-9,-5,6,-2,-3,7,-1,4,1,-9,-1,-4,-7,6,-3,10,5,8,3,10,5,1,8,-7,3,10,6,-6,-7,2,-1,1,8,-7,3,1,5,-1,5,4,6,1,7,5,-2,-3,-9,-8,4,-2,-3,5,2,2,4,7,-9,-3,10,10,5,4,8,5,-7,10,-9,-9,9,-10,9,-4,-8,5,-5,7,-8,5,2,9,8,-1,-2,-8,6,-5,-5,-5,4,-8,-7,-10,-7,3,7,-1,9,10,4,4,3,-7,8,1,2,-2,6,3,7,7,6,-8,1,8,-5,-7,2,7,4,2,7,4,-8,-9,3,-8,5,3,4,-3,-4,9,4,3,-4,-5,-3,-6,-6,-5,-10,-7,10,1,3,-5,6,-10,10,10,2,-4,-6,3,5,10,-10,-2,-9,6,-9,-7,-5,-5,2,-8,3,-9,-4,1,-2,-7,-10,-5,-4,-10,-4,-9,-6,5,-2,-4,6,-3,8,10,-7,-4,-7,-3,-10,3,-2,2,-9,-7,1,-7,5,-7,-6,-4,-5,-7,7,-3,-4,2,1,3,-2,-10,-2,-8,-6,1,-4,-4,-5,-3,-2]], dtype = "uint8")#candidate|5728|(1, 252)|const|uint8
call_5727 = relay.TupleGetItem(func_5582_call(relay.reshape(const_5728.astype('uint8'), [252,])), 2)
call_5729 = relay.TupleGetItem(func_5584_call(relay.reshape(const_5728.astype('uint8'), [252,])), 2)
output = relay.Tuple([uop_5720,call_5723,var_5724,call_5727,const_5728,])
output2 = relay.Tuple([uop_5722,call_5725,var_5724,call_5729,const_5728,])
func_5730 = relay.Function([var_5724,], output)
mod['func_5730'] = func_5730
mod = relay.transform.InferType()(mod)
var_5731 = relay.var("var_5731", dtype = "float32", shape = (6, 30))#candidate|5731|(6, 30)|var|float32
output = func_5730(var_5731)
func_5732 = relay.Function([var_5731], output)
mutated_mod['func_5732'] = func_5732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_5809 = func_5645_call()
call_5810 = func_5645_call()
output = relay.Tuple([call_5809,])
output2 = relay.Tuple([call_5810,])
func_5816 = relay.Function([], output)
mod['func_5816'] = func_5816
mod = relay.transform.InferType()(mod)
mutated_mod['func_5816'] = func_5816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5816_call = mutated_mod.get_global_var('func_5816')
call_5817 = func_5816_call()
output = call_5817
func_5818 = relay.Function([], output)
mutated_mod['func_5818'] = func_5818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_5832 = relay.TupleGetItem(func_5509_call(), 3)
call_5833 = relay.TupleGetItem(func_5511_call(), 3)
output = call_5832
output2 = call_5833
func_5870 = relay.Function([], output)
mod['func_5870'] = func_5870
mod = relay.transform.InferType()(mod)
output = func_5870()
func_5871 = relay.Function([], output)
mutated_mod['func_5871'] = func_5871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_5922 = relay.TupleGetItem(func_5509_call(), 1)
call_5923 = relay.TupleGetItem(func_5511_call(), 1)
output = call_5922
output2 = call_5923
func_5932 = relay.Function([], output)
mod['func_5932'] = func_5932
mod = relay.transform.InferType()(mod)
mutated_mod['func_5932'] = func_5932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5932_call = mutated_mod.get_global_var('func_5932')
call_5933 = func_5932_call()
output = call_5933
func_5934 = relay.Function([], output)
mutated_mod['func_5934'] = func_5934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5870_call = mod.get_global_var('func_5870')
func_5871_call = mutated_mod.get_global_var('func_5871')
call_5950 = func_5870_call()
call_5951 = func_5870_call()
func_3789_call = mod.get_global_var('func_3789')
func_3793_call = mutated_mod.get_global_var('func_3793')
var_5954 = relay.var("var_5954", dtype = "float32", shape = (8, 1))#candidate|5954|(8, 1)|var|float32
const_5955 = relay.const([[2.835976,-1.112751],[4.921206,-2.003038],[3.082878,-6.187488],[4.318482,-6.970748],[8.935806,9.273540],[1.109903,9.030221],[2.239733,-9.937555],[-5.556505,7.246368],[-2.295145,-5.943214],[-6.848724,-2.777189],[6.543130,7.972490],[-4.718998,-3.876552],[-1.698521,-7.899982],[7.702188,6.116555],[-4.672949,2.697737],[8.733825,2.356488],[-0.856980,5.133105],[-7.563288,-5.399336],[8.795811,-9.274572],[8.045174,3.109956],[-1.433347,-4.900866],[-2.210912,8.186611],[4.983073,6.966050],[3.904485,-0.692219],[-6.045359,-0.432383],[9.743921,9.463805],[-4.688474,9.560390],[-4.366250,8.634659],[-8.544119,4.304670],[4.645559,8.961635],[6.292931,-8.171981],[9.376337,-7.831699],[-0.643428,-9.972713],[0.333896,-0.608659],[9.180807,8.694166],[9.536404,3.116181],[-7.656440,-2.893896],[9.738494,-9.523448],[-1.325719,7.885499],[6.789369,5.283190],[-0.282226,-6.149937],[7.776254,-4.445192],[-4.341732,0.231230],[-7.468074,8.261792],[3.197543,6.959290],[9.777104,3.066364],[-3.215789,-8.502846],[-0.309276,2.671124],[7.569906,-2.948821],[1.022337,-7.116987],[-3.206379,4.778736],[-9.545831,-3.452564]], dtype = "float32")#candidate|5955|(52, 2)|const|float32
call_5953 = relay.TupleGetItem(func_3789_call(relay.reshape(var_5954.astype('float32'), [2, 4, 1]), relay.reshape(const_5955.astype('float32'), [2, 4, 13]), ), 1)
call_5956 = relay.TupleGetItem(func_3793_call(relay.reshape(var_5954.astype('float32'), [2, 4, 1]), relay.reshape(const_5955.astype('float32'), [2, 4, 13]), ), 1)
output = relay.Tuple([call_5950,call_5953,var_5954,const_5955,])
output2 = relay.Tuple([call_5951,call_5956,var_5954,const_5955,])
func_5958 = relay.Function([var_5954,], output)
mod['func_5958'] = func_5958
mod = relay.transform.InferType()(mod)
mutated_mod['func_5958'] = func_5958
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5959 = relay.var("var_5959", dtype = "float32", shape = (8, 1))#candidate|5959|(8, 1)|var|float32
func_5958_call = mutated_mod.get_global_var('func_5958')
call_5960 = func_5958_call(var_5959)
output = call_5960
func_5961 = relay.Function([var_5959], output)
mutated_mod['func_5961'] = func_5961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5816_call = mod.get_global_var('func_5816')
func_5818_call = mutated_mod.get_global_var('func_5818')
call_5973 = relay.TupleGetItem(func_5816_call(), 0)
call_5974 = relay.TupleGetItem(func_5818_call(), 0)
output = relay.Tuple([call_5973,])
output2 = relay.Tuple([call_5974,])
func_5993 = relay.Function([], output)
mod['func_5993'] = func_5993
mod = relay.transform.InferType()(mod)
mutated_mod['func_5993'] = func_5993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5993_call = mutated_mod.get_global_var('func_5993')
call_5994 = func_5993_call()
output = call_5994
func_5995 = relay.Function([], output)
mutated_mod['func_5995'] = func_5995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_6007 = relay.TupleGetItem(func_5993_call(), 0)
call_6008 = relay.TupleGetItem(func_5995_call(), 0)
output = relay.Tuple([call_6007,])
output2 = relay.Tuple([call_6008,])
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
func_6009_call = mod.get_global_var('func_6009')
func_6011_call = mutated_mod.get_global_var('func_6011')
call_6105 = relay.TupleGetItem(func_6009_call(), 0)
call_6106 = relay.TupleGetItem(func_6011_call(), 0)
output = call_6105
output2 = call_6106
func_6126 = relay.Function([], output)
mod['func_6126'] = func_6126
mod = relay.transform.InferType()(mod)
mutated_mod['func_6126'] = func_6126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mutated_mod.get_global_var('func_6126')
call_6127 = func_6126_call()
output = call_6127
func_6128 = relay.Function([], output)
mutated_mod['func_6128'] = func_6128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5932_call = mod.get_global_var('func_5932')
func_5934_call = mutated_mod.get_global_var('func_5934')
call_6217 = func_5932_call()
call_6218 = func_5932_call()
func_5816_call = mod.get_global_var('func_5816')
func_5818_call = mutated_mod.get_global_var('func_5818')
call_6254 = relay.TupleGetItem(func_5816_call(), 0)
call_6255 = relay.TupleGetItem(func_5818_call(), 0)
func_4050_call = mod.get_global_var('func_4050')
func_4055_call = mutated_mod.get_global_var('func_4055')
const_6259 = relay.const([[-2,-6,5,-10,8,-6],[5,-9,8,-8,7,-6],[-6,4,-3,-2,-1,9],[-2,4,8,2,-3,-2],[3,9,7,-8,-10,-6],[-5,8,-9,-3,-4,2],[-6,-5,-5,1,6,-10],[9,7,10,-10,4,-4],[-5,-3,-5,-10,1,-1],[2,-6,4,-1,-4,2],[-4,3,-2,-10,-4,-3],[9,-10,-9,-7,-5,-7],[-1,-3,1,-10,-8,4],[10,7,8,-2,5,9],[3,3,1,8,-2,-8],[6,7,-1,-6,-6,4],[4,3,8,-1,10,-10],[8,4,10,-3,1,2],[3,-4,10,-1,4,4],[-5,-6,1,-7,-5,-8],[-4,1,1,7,1,10],[-1,-8,6,8,8,-8],[9,9,6,-9,8,-6],[-3,-4,-6,8,7,4],[-7,-9,-6,6,-2,-1],[2,-1,-2,-1,1,1],[-10,-5,-4,-4,-1,8],[10,5,8,-4,-8,3],[1,-6,1,-10,-6,-10],[3,-3,-7,-2,-4,-10],[-2,7,9,-1,5,-3],[-5,-7,-7,3,-1,4],[5,6,2,-6,-2,4],[2,-6,-3,3,-1,8],[7,9,8,-7,-9,4],[1,-6,4,8,5,3],[2,-5,8,2,7,-5],[-3,7,9,3,-3,5],[-1,3,7,-2,-6,4],[10,-1,-7,1,-1,4],[-2,-10,-8,-4,9,2],[5,-7,-3,-5,8,2]], dtype = "uint8")#candidate|6259|(42, 6)|const|uint8
var_6260 = relay.var("var_6260", dtype = "uint32", shape = ())#candidate|6260|()|var|uint32
call_6258 = relay.TupleGetItem(func_4050_call(relay.reshape(const_6259.astype('uint8'), [3, 6, 14]), relay.reshape(const_6259.astype('uint8'), [3, 6, 14]), relay.reshape(var_6260.astype('uint32'), []), ), 0)
call_6261 = relay.TupleGetItem(func_4055_call(relay.reshape(const_6259.astype('uint8'), [3, 6, 14]), relay.reshape(const_6259.astype('uint8'), [3, 6, 14]), relay.reshape(var_6260.astype('uint32'), []), ), 0)
func_5490_call = mod.get_global_var('func_5490')
func_5493_call = mutated_mod.get_global_var('func_5493')
const_6272 = relay.const([True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,True], dtype = "bool")#candidate|6272|(1120,)|const|bool
call_6271 = relay.TupleGetItem(func_5490_call(relay.reshape(var_6260.astype('uint64'), []), relay.reshape(const_6272.astype('bool'), [1120,]), ), 3)
call_6273 = relay.TupleGetItem(func_5493_call(relay.reshape(var_6260.astype('uint64'), []), relay.reshape(const_6272.astype('bool'), [1120,]), ), 3)
func_6126_call = mod.get_global_var('func_6126')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_6285 = func_6126_call()
call_6286 = func_6126_call()
func_5582_call = mod.get_global_var('func_5582')
func_5584_call = mutated_mod.get_global_var('func_5584')
call_6289 = relay.TupleGetItem(func_5582_call(relay.reshape(call_6258.astype('uint8'), [252,])), 3)
call_6290 = relay.TupleGetItem(func_5584_call(relay.reshape(call_6258.astype('uint8'), [252,])), 3)
func_4654_call = mod.get_global_var('func_4654')
func_4658_call = mutated_mod.get_global_var('func_4658')
var_6295 = relay.var("var_6295", dtype = "int64", shape = (630,))#candidate|6295|(630,)|var|int64
call_6294 = relay.TupleGetItem(func_4654_call(relay.reshape(var_6295.astype('int64'), [14, 15, 3]), relay.reshape(var_6295.astype('int64'), [14, 15, 3]), ), 0)
call_6296 = relay.TupleGetItem(func_4658_call(relay.reshape(var_6295.astype('int64'), [14, 15, 3]), relay.reshape(var_6295.astype('int64'), [14, 15, 3]), ), 0)
func_1061_call = mod.get_global_var('func_1061')
func_1063_call = mutated_mod.get_global_var('func_1063')
const_6304 = relay.const([[5.390228,5.155547,2.610912,-4.886648,-6.676447,-9.474960,-9.904451,4.199698,6.409144,5.962339,6.223131,1.305981,7.802630,-3.066007,-4.317618,-4.689984,-4.001501,-8.027081,-4.614369,6.702750,-1.443362,-6.228820,-2.079254,-8.942273,2.974193,3.396330,8.115941,-1.197377,3.940872,2.808421,5.055019,-4.521619,1.441223,-3.012735,9.851627,-8.917898,8.061540,-2.159493,2.910690,-9.044202,-0.204809,0.932870,-9.948401,-2.078839,-7.560329,7.602123,1.896848,-4.871139,6.296682,5.075269,-0.352660,-9.003346,-1.783290,0.456121,5.018486,4.238783,5.197669,-6.015457,-3.166271,-2.365156],[-5.259480,-2.868566,1.292559,-0.033512,8.181967,7.212330,-5.760439,-2.079564,-9.928465,-2.135940,0.838088,0.480914,-3.072909,-6.856875,-8.345821,-0.058926,3.800745,6.483418,3.887355,6.760378,2.739376,-1.310163,-5.998781,-8.896695,-2.275692,3.462993,-4.974587,-5.173974,-2.559848,2.685916,2.947082,2.775354,3.545208,5.812621,-4.653319,5.326020,4.707812,5.211272,-8.280345,-3.367674,-5.297449,-0.266117,-2.799159,-2.191110,-9.241798,-2.504785,7.564670,-6.739697,-0.096240,0.135226,-1.233700,-5.743796,-3.744245,5.697025,9.853062,5.949730,3.076694,8.714544,-5.316445,-9.467146],[7.016981,3.162739,-4.198508,4.553330,8.985978,-5.570209,-2.098120,-6.292371,-8.782523,9.280008,5.756370,-0.827066,6.771830,1.400443,5.913927,-9.590945,-9.469969,1.393828,5.814991,9.882904,2.354094,-6.693622,-8.693358,-7.443564,-9.998010,-3.014739,-0.285083,1.704986,-9.133098,3.773884,-3.961456,0.932277,5.090613,-3.748325,1.634272,-6.857295,7.802003,-7.845570,2.107992,-2.123249,1.421360,5.588295,3.413360,3.411877,7.526313,2.016414,-2.983366,-2.370995,5.519402,-6.808782,-9.062023,9.652597,1.178832,8.563439,-1.581115,-0.840295,4.694858,9.732267,-9.265505,-8.342357]], dtype = "float32")#candidate|6304|(3, 60)|const|float32
call_6303 = relay.TupleGetItem(func_1061_call(relay.reshape(const_6304.astype('float32'), [4, 9, 5])), 0)
call_6305 = relay.TupleGetItem(func_1063_call(relay.reshape(const_6304.astype('float32'), [4, 9, 5])), 0)
uop_6320 = relay.sigmoid(call_6294.astype('float64')) # shape=(14, 15, 3)
uop_6322 = relay.sigmoid(call_6296.astype('float64')) # shape=(14, 15, 3)
func_5958_call = mod.get_global_var('func_5958')
func_5961_call = mutated_mod.get_global_var('func_5961')
const_6329 = relay.const([[6.019495,-6.007081,-0.217550,5.623624,-9.743336,8.273022,-5.686995,-4.380970]], dtype = "float32")#candidate|6329|(1, 8)|const|float32
call_6328 = relay.TupleGetItem(func_5958_call(relay.reshape(const_6329.astype('float32'), [8, 1])), 2)
call_6330 = relay.TupleGetItem(func_5961_call(relay.reshape(const_6329.astype('float32'), [8, 1])), 2)
output = relay.Tuple([call_6217,call_6254,call_6258,const_6259,var_6260,call_6271,const_6272,call_6285,call_6289,var_6295,call_6303,const_6304,uop_6320,call_6328,const_6329,])
output2 = relay.Tuple([call_6218,call_6255,call_6261,const_6259,var_6260,call_6273,const_6272,call_6286,call_6290,var_6295,call_6305,const_6304,uop_6322,call_6330,const_6329,])
func_6331 = relay.Function([var_6260,var_6295,], output)
mod['func_6331'] = func_6331
mod = relay.transform.InferType()(mod)
var_6332 = relay.var("var_6332", dtype = "uint32", shape = ())#candidate|6332|()|var|uint32
var_6333 = relay.var("var_6333", dtype = "int64", shape = (630,))#candidate|6333|(630,)|var|int64
output = func_6331(var_6332,var_6333,)
func_6334 = relay.Function([var_6332,var_6333,], output)
mutated_mod['func_6334'] = func_6334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_6363 = func_5645_call()
call_6364 = func_5645_call()
output = call_6363
output2 = call_6364
func_6365 = relay.Function([], output)
mod['func_6365'] = func_6365
mod = relay.transform.InferType()(mod)
mutated_mod['func_6365'] = func_6365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6365_call = mutated_mod.get_global_var('func_6365')
call_6366 = func_6365_call()
output = call_6366
func_6367 = relay.Function([], output)
mutated_mod['func_6367'] = func_6367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_6379 = func_5645_call()
call_6380 = func_5645_call()
func_5730_call = mod.get_global_var('func_5730')
func_5732_call = mutated_mod.get_global_var('func_5732')
var_6386 = relay.var("var_6386", dtype = "float32", shape = (6, 30))#candidate|6386|(6, 30)|var|float32
call_6385 = relay.TupleGetItem(func_5730_call(relay.reshape(var_6386.astype('float32'), [6, 30])), 2)
call_6387 = relay.TupleGetItem(func_5732_call(relay.reshape(var_6386.astype('float32'), [6, 30])), 2)
output = relay.Tuple([call_6379,call_6385,var_6386,])
output2 = relay.Tuple([call_6380,call_6387,var_6386,])
func_6408 = relay.Function([var_6386,], output)
mod['func_6408'] = func_6408
mod = relay.transform.InferType()(mod)
mutated_mod['func_6408'] = func_6408
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6409 = relay.var("var_6409", dtype = "float32", shape = (6, 30))#candidate|6409|(6, 30)|var|float32
func_6408_call = mutated_mod.get_global_var('func_6408')
call_6410 = func_6408_call(var_6409)
output = call_6410
func_6411 = relay.Function([var_6409], output)
mutated_mod['func_6411'] = func_6411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5870_call = mod.get_global_var('func_5870')
func_5871_call = mutated_mod.get_global_var('func_5871')
call_6423 = func_5870_call()
call_6424 = func_5870_call()
output = call_6423
output2 = call_6424
func_6429 = relay.Function([], output)
mod['func_6429'] = func_6429
mod = relay.transform.InferType()(mod)
output = func_6429()
func_6430 = relay.Function([], output)
mutated_mod['func_6430'] = func_6430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_6449 = relay.TupleGetItem(func_5104_call(), 0)
call_6450 = relay.TupleGetItem(func_5106_call(), 0)
const_6457 = relay.const([[[-5.120803,2.850850,3.199945,4.701588,9.187528,6.215535,-6.237752,4.637275,-2.566616,8.236718,-1.374037,4.360508,8.381056,2.777215,-6.055983],[-8.971851,-1.457547,-6.036925,-0.834345,-4.515942,0.331791,-3.884105,-2.964023,-3.353983,-4.075458,7.804129,-3.625379,-2.059544,4.179278,-6.368397],[5.183574,-5.181636,4.257608,6.362682,-0.563304,0.670363,7.846760,-9.348533,6.486592,-7.927182,-4.964858,9.102587,-4.935063,-9.521090,3.812512],[-7.699337,2.143998,-8.208590,0.451452,9.825309,0.219129,-1.781205,-1.514972,2.652237,6.174373,1.245381,5.466598,-1.998674,9.334530,-4.172768],[-3.600411,4.554409,9.294993,-8.175629,7.724051,6.620373,-6.348201,8.442133,-4.516257,3.347538,0.618836,2.470078,0.858279,-0.127754,-0.985618],[5.046164,4.723516,-6.696403,-5.416794,-2.873877,-7.959590,1.132119,9.820825,0.848891,8.410994,4.352852,-7.778489,9.160050,-2.352761,-9.858005],[-9.879737,8.428673,-4.291493,8.428506,-5.227840,-9.296144,3.548332,-1.377055,-0.886098,-9.648768,-0.090500,-9.935179,-4.441095,-3.030741,-7.848367],[3.144527,-2.139154,-2.618748,-5.004669,6.953168,7.786668,-1.588640,5.025598,0.158212,-9.590847,2.907901,3.071641,2.429851,-2.670059,1.574373]],[[-8.353797,4.799447,8.809455,2.606064,4.298591,3.814163,-7.453494,3.336631,-8.182460,-5.147923,-0.707409,6.403136,9.289209,3.306650,-7.722611],[-8.092897,8.739300,3.893077,-4.454543,4.192128,6.199474,-1.316650,-2.927179,-3.574396,2.828632,4.897103,-5.609073,3.470142,-8.431218,2.818694],[8.216730,9.273569,-0.777607,-9.464955,-7.174713,-1.103951,-9.998754,7.982130,4.219355,7.299627,-5.703693,-8.529471,0.472336,9.343143,7.362640],[-6.323122,-7.153849,5.100262,-5.137407,0.967249,2.673378,-3.452306,1.189284,-2.741518,0.779663,4.977122,2.104778,2.063036,5.011668,-0.404489],[2.641988,-7.662096,-1.064114,-4.371832,9.234348,5.342696,-5.299823,-9.446258,-9.053655,-7.481188,-4.841341,7.956847,8.096154,-5.443897,9.556722],[8.063926,1.527874,5.136640,-6.662964,-3.187913,2.619934,-6.962888,5.852869,8.024133,-5.490940,-9.349690,4.681606,-7.861479,-5.209123,-4.277835],[5.986299,-8.799372,6.331798,-1.773916,-4.926670,9.256436,4.225712,6.395654,-7.978246,-4.020012,-0.103987,1.825580,-0.263153,-7.826730,-7.935852],[9.029532,4.561457,-3.770085,7.771584,-7.599352,5.356185,5.176190,9.490293,8.531807,-1.152238,-2.552013,-3.355155,-6.031763,8.544807,9.442681]],[[6.254996,9.063946,8.214747,2.659943,2.398089,-4.730541,7.676416,0.751722,-1.987935,-0.973091,-8.314885,7.569780,-4.034233,0.919117,-6.497422],[6.290163,7.242580,-4.659329,-3.914336,7.026868,3.988689,-7.431678,-6.669533,-8.449862,3.358484,3.758879,1.896161,-2.863570,-0.700578,-0.185047],[3.182144,8.256271,-3.861429,3.438521,3.994838,-7.417562,-2.751925,-3.095045,-2.354821,3.959501,6.527572,4.711377,4.182963,5.331122,-3.094482],[-2.794140,3.429285,-8.651716,-5.557270,5.933101,3.862033,-4.515841,-1.416453,-9.674979,4.757491,-2.774521,-2.985952,-9.713489,-9.260520,5.765137],[7.871217,-3.933335,3.251409,-1.055209,-2.940806,-0.083328,-9.051722,8.156001,9.286954,0.354232,1.325988,6.938791,-2.724170,2.787631,2.346090],[2.495629,-4.549654,-8.409866,-8.268335,4.515482,-8.976993,-6.740816,5.737961,4.562274,9.072550,0.095733,0.725721,-1.056178,-2.888316,-4.481012],[2.306052,-8.280976,1.291349,5.277780,-8.361712,-4.505032,-5.561859,2.755750,-2.731353,-7.795605,0.312401,-2.274928,7.133191,-2.759849,-0.618217],[7.449058,-6.505698,2.962265,-0.376325,-8.704137,-8.171018,2.273218,7.739945,-9.625607,-1.250892,-8.057242,-8.563632,-3.270875,4.609535,-7.039289]],[[4.974000,5.688934,8.882506,8.616922,-9.017025,-8.675048,-4.299529,7.984005,-8.622047,0.780265,8.145480,1.722129,-8.807483,0.030242,-5.252850],[0.565957,5.208640,-8.484445,1.436336,4.209266,6.283974,-9.711534,1.724849,1.231125,1.972935,-6.917851,-4.422373,4.478909,7.374769,4.956120],[-9.862037,9.463001,0.992142,-9.847711,6.628833,-5.185022,-1.535707,-0.769029,4.380905,0.752548,-4.099483,6.029611,1.587175,9.974962,6.942805],[4.698780,8.862360,9.685560,-6.786133,-5.027315,1.352143,-1.421816,0.106707,-8.584145,-9.786873,-2.081132,3.721675,-0.745618,-1.935205,-5.155368],[-1.052227,3.579043,-9.306221,-2.345646,-7.740662,6.334206,-7.136997,9.887032,-3.466888,-9.377839,-6.911844,-1.092646,-9.100012,-9.001846,-1.877765],[-3.478637,-2.526975,5.227750,-5.495770,0.403887,-8.404167,8.541164,-0.076769,-6.309012,-2.207086,-7.354595,2.764802,-5.098753,3.079492,-6.258836],[0.284488,-6.120108,-0.671399,1.880088,2.380433,-0.225702,4.665298,-0.115983,-5.971741,-1.252553,5.104307,2.996750,2.142666,-6.213544,6.938973],[4.630874,2.186634,-0.494106,9.182441,0.539062,9.316601,-2.155981,3.408041,-9.752650,0.273804,-2.066729,8.725465,-9.775338,5.220791,5.630602]],[[8.105526,-3.815184,-8.621407,4.365837,-5.549290,4.532077,-0.931660,-2.519773,-5.212055,8.307150,2.333805,0.072352,-7.479012,-1.447122,-6.349988],[-4.224747,-7.927513,8.898668,6.763671,-5.336204,7.029519,1.512004,0.561582,9.134666,6.012990,6.814505,-2.410160,4.055566,-7.630851,-5.417020],[-9.679989,7.135286,1.160936,9.517429,3.058043,-5.962673,8.200928,-9.337827,0.543634,6.429069,-1.849425,-8.936566,4.558602,6.175163,6.427062],[-7.348193,-7.787313,-0.308691,-3.460201,9.301911,5.172457,-7.638072,5.749497,9.675218,-2.761434,0.347697,9.475872,6.042156,-8.767747,0.987402],[7.033012,0.513514,2.284810,7.978805,7.477251,8.064013,1.259887,-2.645985,-7.753030,2.809561,-9.306249,6.292216,-2.308759,-8.692433,-1.753136],[-6.657268,2.384166,3.145890,6.501587,5.968811,9.408320,6.312678,-5.133607,-9.592663,5.293547,-3.918888,-0.542252,-4.339118,-5.670306,8.463141],[-8.303745,-2.728109,8.081387,-2.565033,2.008713,-4.713711,-2.900975,3.408386,8.775074,0.819768,4.172769,-5.449126,7.458868,1.625913,3.801079],[-3.057500,-8.401177,9.656100,8.386535,4.933952,6.933466,6.195002,2.007021,6.503610,-8.613487,-2.082297,-2.855958,-3.329056,0.253969,3.306742]],[[-8.692303,-3.260701,6.074038,9.354154,6.758081,7.734334,-7.355552,-1.629267,4.538860,-6.326556,-5.734872,9.553679,8.614407,-5.715832,2.479038],[0.416028,-7.485243,1.453322,9.680754,-0.334140,8.652611,-8.650116,-3.665278,8.937295,-3.819597,-3.099736,-6.623391,1.774736,3.914914,-3.731037],[5.854001,-5.206012,9.023209,4.886452,-3.409806,8.594316,9.513542,7.821959,-7.623843,4.154172,-4.630485,1.806137,-1.070097,-4.650007,1.363714],[-5.262200,-4.547086,-5.386577,-0.492517,3.667710,6.086414,-3.711332,-6.566561,-4.932473,4.121235,8.800645,5.998205,-4.314618,5.705068,8.200674],[-3.047883,8.028877,3.118301,-3.169459,-9.636196,-4.160911,6.685723,-6.851562,7.170354,-9.221673,9.211389,-4.392559,0.051399,-0.573098,-0.098091],[8.804188,9.610733,8.288895,-7.858130,9.377821,2.775687,-1.316594,-3.661411,-8.639077,8.181703,-3.824990,-0.327044,-9.293577,-9.786375,-8.359706],[-5.615469,3.596122,2.372100,-6.410376,-8.035836,-9.651214,-7.269559,-6.312029,4.995485,-4.023239,-1.329247,8.361616,8.116066,-5.758748,-2.394987],[-6.063803,-9.393320,0.116618,1.437604,4.015674,7.697390,5.390767,-3.045182,-0.557250,7.408647,-2.119217,-3.668788,-3.867786,6.838904,6.165574]],[[-8.225227,9.295375,5.931044,-3.159784,-7.623205,-7.953878,6.448878,1.224512,-4.799998,0.124313,-1.898346,4.533622,-5.693257,1.944875,-4.978435],[5.785569,-0.446963,6.073661,2.857150,-2.010366,1.731327,2.254982,0.104529,-6.881702,5.315128,9.765090,9.551475,-1.845220,-4.774182,-3.601510],[-5.267186,8.040379,-4.582869,-3.519689,-3.724632,4.239469,7.252595,-4.557950,-5.397287,-4.776671,0.447256,6.391773,-2.352084,-5.083545,8.510137],[9.991575,-1.561217,0.998434,0.219237,9.684707,-7.822462,5.080273,8.141223,-2.451339,-7.504738,5.832488,-7.798258,6.407952,-4.929093,-0.942544],[-5.711981,3.512601,-1.479413,1.057173,-5.432157,-1.920847,4.505915,3.671314,1.384426,-1.186650,-7.953627,6.553142,0.988433,-2.163512,-6.705511],[2.321453,-9.211923,-7.312518,9.248480,9.196231,-1.530526,0.868557,0.816113,-8.078985,-3.832541,9.947970,7.792365,-7.957322,6.578529,-4.794328],[7.487727,-5.631446,8.612039,-2.949011,-7.303191,-2.763187,2.177091,-8.300367,-6.104441,-9.760917,-6.665910,-1.974436,-0.157679,-7.763040,5.271235],[-8.866679,-6.755230,-2.365395,4.986955,2.098987,-4.989641,-0.244728,3.196501,0.131982,4.115235,-7.900600,4.209618,1.269766,0.721013,0.943354]],[[0.008036,6.020931,-6.700929,5.908090,5.044668,6.486463,-3.999012,3.162907,-5.492402,-5.811987,-9.793995,3.487845,7.485311,-1.877375,-1.014614],[8.213715,2.112908,-2.212351,-8.209339,6.082377,-0.471311,-7.945879,-2.954614,-8.441175,-1.347272,-3.130049,4.216277,-5.111330,0.782555,-2.847386],[-8.649377,1.079527,-3.158695,0.590086,5.651341,-1.133775,8.581068,-3.489874,9.208641,-4.218621,1.141456,-2.759504,6.253147,9.039154,8.135477],[-4.469781,2.319854,4.008241,8.184165,2.649531,1.010747,-2.848212,-1.307745,-6.458287,9.417465,6.759895,-5.210983,-2.845438,-2.995406,-1.223162],[6.223043,4.569932,-2.910007,-9.823922,4.501415,-2.915732,-8.848495,8.559113,9.506288,-3.402398,-0.392314,-8.508334,2.126419,-8.301398,-6.410860],[-4.988676,-4.544425,4.951039,-7.212673,-0.064333,2.303058,8.392289,-9.855662,-2.489973,-3.096422,-2.851057,-2.509145,5.797992,2.009003,4.918474],[-5.982300,8.062952,4.167403,6.174654,7.491135,6.022206,-3.022783,-3.997598,8.232489,2.188427,5.010991,-9.682015,-7.925500,1.609681,-5.823425],[6.123607,-6.220374,8.057290,4.950613,-4.816425,-7.435499,8.248286,-5.766360,2.603522,-2.723707,0.098490,0.167426,2.282220,-1.883433,9.669265]],[[7.682716,8.986583,-9.812648,3.200885,-6.891942,-8.062008,1.253338,9.533910,0.683054,0.584851,4.357360,0.804110,3.383515,-2.209937,5.772317],[-0.013813,0.308862,1.363501,-0.162947,8.244628,-7.429419,1.920786,-9.050549,7.467619,-0.613512,2.715546,3.344305,-9.197889,-4.094513,-8.144886],[-9.570126,-1.982182,9.826287,0.683012,1.660877,-5.832207,-5.297378,1.093875,-9.056818,-1.900219,-4.555399,2.593909,-7.371062,-0.184857,-9.332774],[1.358139,9.409694,-0.998525,7.554225,-1.778873,1.013995,-8.568234,-4.911308,-4.395121,-1.790148,8.837389,-8.811024,-4.089190,-1.264406,9.060344],[-5.973611,-1.962392,6.578441,-4.424249,-2.145685,7.835635,2.449063,-5.598481,3.484378,-8.270076,3.038868,-6.077341,-2.664652,4.493752,0.709326],[-4.009103,7.574391,3.495321,1.506348,1.504467,-0.086901,3.036991,-8.950571,-4.392049,-5.094548,0.021241,-5.125617,-3.886037,-0.109261,-8.818853],[-5.871765,3.118732,5.028340,-4.989903,-5.480977,-6.347331,-7.285883,-5.004406,3.636388,5.507735,-1.785386,-6.980095,-0.084985,5.536112,-6.460717],[0.415969,-7.798056,-6.999911,2.849468,0.287487,-3.064523,2.839006,0.408819,6.228342,-3.170099,6.403571,5.657214,2.980930,-7.451428,-3.662253]],[[-0.422097,9.354923,0.183827,-0.123469,1.057515,-9.964904,-3.985597,-8.893961,-5.676106,-1.300098,-0.848905,4.824927,0.171394,-7.594988,8.693279],[-0.378777,-6.647686,4.026722,8.340874,-8.099562,9.984755,-3.932455,-9.489640,4.587272,-5.149821,5.213195,0.458460,-7.944104,-9.954944,-1.251301],[-5.738082,6.214304,8.745660,-9.660830,3.837433,9.627021,3.557502,-0.618636,-2.572985,-8.147928,8.448831,-4.926351,-0.029550,-9.524570,6.423529],[2.305322,8.780274,-5.158293,7.840456,-7.074971,9.891494,3.579481,6.543605,6.180429,5.020834,3.662625,8.403253,-5.988358,-3.151047,-3.291686],[9.534651,9.850919,7.027183,9.563805,-2.977403,8.775358,2.770767,2.080811,-6.439565,0.659125,-7.280584,-2.746319,-9.648775,-7.362411,7.200853],[-8.951061,-5.411847,-3.437869,8.665968,-8.174330,7.338481,0.625135,-4.146775,2.522002,1.382585,-6.451778,2.979157,-7.975691,6.623565,8.572104],[3.473357,-0.970687,7.049421,5.115993,-8.715547,9.464077,5.220803,2.306921,6.143003,-8.522867,3.057967,-2.161614,-7.578960,-5.143042,9.810842],[-3.712972,8.557327,-1.410817,6.379928,0.633982,8.591092,9.347403,7.954677,-9.553509,-2.218551,-3.774172,-2.941228,-6.496171,2.882209,-3.684602]],[[-3.746579,4.222011,0.796613,3.562863,-3.881476,3.440664,7.529887,-5.790518,2.976750,6.099513,-0.006662,3.695982,-1.961517,7.116199,-0.232941],[2.676548,-1.179468,-0.621306,-3.822361,9.337834,-0.180017,6.343297,4.398529,-1.989946,-3.789002,-5.130110,6.564570,0.344959,-3.093818,0.790164],[9.471158,0.921585,-8.640616,8.612549,4.245977,6.845185,3.016733,2.202426,-0.605780,3.076774,6.224715,9.573183,7.206691,5.684527,0.395068],[-5.404512,3.924065,8.550946,4.224563,-0.159356,5.400011,-0.266999,-8.120086,8.047282,-9.727081,-1.868128,1.083692,-7.863316,-9.737288,-0.847712],[9.336757,-8.687858,-1.574967,-4.019993,7.620313,7.325298,-7.694353,2.211376,6.891231,1.110889,-0.414650,-4.102901,-5.933871,-0.778227,-2.807244],[-7.286276,-4.775647,-2.727250,-2.627887,-7.897947,2.127596,-6.303453,-9.300604,7.384426,3.938086,4.704348,-7.663908,4.536377,-7.360527,6.830690],[-4.289832,-0.389829,3.039534,8.836572,6.360253,9.598100,2.933514,-8.502738,0.969144,-7.917845,3.199227,-5.226402,9.198654,-3.442084,-2.308944],[-5.232620,6.100002,0.103906,4.948999,2.162063,-8.919702,4.267079,-3.529828,8.873391,3.647222,-0.829775,2.198620,-1.215892,-1.451948,1.360274]],[[5.668918,7.488861,-2.738455,8.242804,-4.349778,3.937933,7.085465,-3.673818,-3.789285,9.269862,6.377721,-6.490379,3.832796,2.441707,3.223845],[-2.859967,-9.943748,-1.931655,-3.831257,-0.326192,-1.026206,1.425474,4.932552,4.139301,-0.281585,5.757483,6.663408,-2.290793,1.069299,-1.676679],[-1.934131,8.454629,4.364522,-6.875263,4.638242,-0.782905,-2.644568,3.419158,0.387490,2.775534,1.804897,-1.452019,5.269317,7.237785,-0.686081],[3.757202,-3.709290,-9.933645,-0.946741,0.822058,8.581289,4.925615,-6.802395,3.097931,-2.656612,6.275582,-6.443508,-2.875048,-2.207185,-4.943317],[3.191240,-7.127369,-4.783301,6.628276,4.300841,-2.159767,-9.389856,-6.071308,-2.500969,3.016026,-7.976357,-4.888414,-9.276853,-6.431960,0.976285],[1.826580,6.797449,-6.121332,-5.422236,-4.012906,9.075617,1.070303,7.943027,-9.065445,2.034847,-0.671178,-4.244879,-8.263223,6.568140,6.484756],[4.670570,6.200270,-7.263442,-1.818806,-9.821358,-3.287546,4.482633,0.820899,4.595595,-4.518599,2.063276,1.321419,-4.410137,-6.715213,-8.879089],[-3.373384,6.719151,-7.998690,1.591549,-4.434199,-0.823930,8.929330,-8.674675,-2.155165,-1.291074,1.665087,3.014956,6.383581,-0.472199,7.550909]],[[-2.980898,0.351657,1.186838,6.282445,-8.893194,-7.115621,1.069473,7.015654,4.963416,3.923147,-5.259169,5.704330,6.317495,9.080949,1.617710],[3.664889,-5.829579,9.024975,-1.490641,5.603833,-7.158375,6.448049,0.027303,-2.490452,-4.484615,2.914052,-4.279522,-7.679776,1.944340,0.430088],[-2.456158,-5.938656,9.658126,0.421719,5.861440,5.920763,-7.980549,5.633442,4.038227,-6.304399,7.328291,-1.983585,9.617044,-2.731787,1.942845],[3.812417,-6.070090,-6.177399,7.958025,5.227216,-9.455044,-0.832241,-4.079540,7.267035,7.511598,0.805943,0.622965,-3.412641,6.985170,3.740865],[5.241863,-7.841535,0.450930,8.571620,-6.773641,5.693244,4.767181,-5.478308,9.631530,2.900890,2.519581,1.507609,3.105500,0.494075,-6.271641],[2.115834,8.493358,7.168558,-2.193220,9.349924,-4.569940,-4.429372,8.023309,6.460916,-5.367530,9.897910,7.636350,-8.694066,2.801124,4.691668],[-9.435286,9.489876,9.869011,-8.146938,5.115702,-7.192802,-8.330303,-1.482494,0.616880,-5.848366,-8.315028,-6.951633,6.939968,-6.439414,-2.875934],[-6.095200,-5.740887,3.524762,5.724116,-8.871537,6.472561,-1.989077,7.505860,2.173536,-5.830160,-8.322978,-1.490877,-4.615959,9.982117,-3.804795]],[[3.086363,-3.062975,-2.724361,1.750238,-2.054264,-8.253196,-2.661526,7.445971,0.002471,6.809491,5.301073,6.462657,-3.175888,8.465048,-3.797890],[4.061252,-9.434945,-0.344700,9.459400,-4.967941,5.934311,-8.768966,4.627643,9.744590,-5.554939,-4.823337,-9.811485,1.455303,-0.697477,-7.418437],[-0.480696,-5.023363,4.278745,8.737544,-7.223050,-7.589654,0.273825,0.251311,4.119434,8.804622,8.871035,2.069150,9.499865,-2.197531,5.108296],[9.999732,5.926890,-9.896726,-8.698527,9.843528,-5.660987,-2.043937,-8.843181,-6.255198,-4.103478,-3.661924,-4.228899,3.804418,-1.731654,7.117228],[-4.547288,-4.398087,-6.495427,-4.670275,-2.883875,4.428813,-0.429725,-0.723957,9.977924,-2.594004,2.395886,-3.241505,-7.802646,9.568943,8.932447],[-1.825748,9.896828,3.285305,0.322365,-3.572158,-9.707025,-1.576182,2.276388,3.881421,-5.234580,-3.780456,-5.976007,5.713519,-6.514139,-0.661956],[8.533589,6.696697,5.498906,-9.207525,6.034232,-4.368839,-9.277891,-6.328365,-7.452184,-4.143090,3.897604,-1.082382,1.465238,-8.309873,-3.064962],[-8.612927,6.438402,9.998704,-7.052985,6.123302,-9.921852,4.689430,2.401204,7.072136,-1.543536,-7.324652,-4.292526,9.215457,-5.942495,-7.292895]],[[-9.919436,-7.646316,-9.106626,-7.776213,7.616179,-0.984114,-2.546350,-8.818942,2.469443,3.192308,6.180272,3.974805,-6.755110,-3.731846,-2.784723],[3.016766,9.600612,-4.823966,0.429968,-8.285959,3.741587,0.844199,2.025224,2.277734,9.069934,-8.754623,-2.570615,-7.106329,-7.681587,5.255899],[8.786252,-9.443523,-0.269716,8.063117,3.634735,-2.552535,-7.822142,-1.371448,6.459956,6.599881,-2.546250,5.242418,7.857620,9.086328,-0.974997],[1.518883,-1.865062,-4.546800,-3.649581,-6.379434,-8.067070,-4.766814,-9.739037,-6.000691,-5.174636,-9.832507,8.086300,8.433811,-9.190307,-7.912069],[1.507048,-4.308247,4.258833,-8.219557,-4.451954,-4.470258,4.818810,-2.092918,8.620662,8.230950,-2.954909,4.760376,-9.717215,-3.547173,0.121034],[5.246675,-5.472531,-2.572565,9.427851,-5.316964,-7.213860,-8.364962,7.812515,6.803681,5.218141,4.129894,0.322397,0.393394,4.091784,-4.544413],[-9.046577,-2.060392,6.515504,1.743622,3.115398,2.701409,-6.042882,-2.699754,-4.357319,-1.747893,-2.005423,5.855910,-8.705008,6.767273,-4.067912],[7.475846,-2.400353,-5.058841,-6.301504,-2.670394,2.473734,8.427120,9.847850,1.300285,-7.102997,6.042746,4.292605,-6.147859,9.732816,-0.564834]]], dtype = "float64")#candidate|6457|(15, 8, 15)|const|float64
bop_6458 = relay.logical_or(call_6449.astype('bool'), relay.reshape(const_6457.astype('bool'), relay.shape_of(call_6449))) # shape=(15, 8, 15)
bop_6461 = relay.logical_or(call_6450.astype('bool'), relay.reshape(const_6457.astype('bool'), relay.shape_of(call_6450))) # shape=(15, 8, 15)
func_5958_call = mod.get_global_var('func_5958')
func_5961_call = mutated_mod.get_global_var('func_5961')
var_6469 = relay.var("var_6469", dtype = "float32", shape = (8,))#candidate|6469|(8,)|var|float32
call_6468 = relay.TupleGetItem(func_5958_call(relay.reshape(var_6469.astype('float32'), [8, 1])), 3)
call_6470 = relay.TupleGetItem(func_5961_call(relay.reshape(var_6469.astype('float32'), [8, 1])), 3)
output = relay.Tuple([bop_6458,call_6468,var_6469,])
output2 = relay.Tuple([bop_6461,call_6470,var_6469,])
func_6483 = relay.Function([var_6469,], output)
mod['func_6483'] = func_6483
mod = relay.transform.InferType()(mod)
mutated_mod['func_6483'] = func_6483
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6484 = relay.var("var_6484", dtype = "float32", shape = (8,))#candidate|6484|(8,)|var|float32
func_6483_call = mutated_mod.get_global_var('func_6483')
call_6485 = func_6483_call(var_6484)
output = call_6485
func_6486 = relay.Function([var_6484], output)
mutated_mod['func_6486'] = func_6486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6365_call = mod.get_global_var('func_6365')
func_6367_call = mutated_mod.get_global_var('func_6367')
call_6528 = func_6365_call()
call_6529 = func_6365_call()
func_384_call = mod.get_global_var('func_384')
func_387_call = mutated_mod.get_global_var('func_387')
const_6581 = relay.const([[7.348726,-3.032263,8.846181,6.501584,-0.643267,6.500248,8.572572,5.985160,7.023782,-2.546722,-7.752058,-8.841830,5.104869,-7.125685,-1.879506,0.970179,-2.243609,7.529655,-7.232818,8.782518,-8.451504,2.503778,4.217242,-2.833725,-1.282357,0.752959,-8.551144,8.864782,-7.247503,8.263483,8.819533,-5.669638,-7.345344,2.383857,6.500115,-3.975285,7.977019,3.320253,-2.541875,-5.244211,-3.879275,6.774717,1.155905,-2.147982,-6.836143,-7.039119,-7.505354,3.589463,-7.011069,0.373703,-7.397002,9.017500,2.494509,-7.879479,4.340074,4.003530,-1.063065,-1.507823,3.831546,7.744558,-6.627145,5.042342,6.471185,5.014017,2.952500,0.876487,-2.295212,8.346554,0.389506,-4.384934,-5.462489,-1.874880,-6.898574,-6.194757,4.558608,-7.972787,9.353914,-7.252448,-5.568334,-4.039809,-0.769642,8.511576,7.219897,9.472436,-6.265674,4.905081,3.747346,-6.937231,-1.407469,2.914573,-9.405531,8.725527,5.591037,-5.984644,6.815819,3.185989,-6.947400,5.792500,6.926004,-3.137365,-0.409223,7.983655,6.379508,6.706506,-9.122066,4.228130,-5.268427,8.978737,-4.117270,-9.299385,-6.689158,-2.015004,-6.429828,-2.447470,-3.031361,-0.976584,-6.693325,-0.253493,6.517868,5.939009,-8.410160,-5.218513,5.044425,-1.353367,-3.418278,-3.419080,-0.543205,7.626320,-8.733023,-6.776648,1.348514,4.596859,-0.149710,4.521536,1.075453,-1.751031,-9.769431,7.244952,-9.519843,2.272067,-7.945765,9.065442,-1.092860,0.139847,0.589875,5.765805,-8.827728,-3.888994,-7.039500,-7.691670,2.436563,6.397116,-4.091532,2.179883,-5.499534,7.633764,-7.208205,5.268267,9.849975,2.467936,6.292423,0.008427,0.956945,-5.729514,-6.162355,-1.163020,4.577526,7.237537,-8.774819,-6.752939,1.367942,3.154272,9.232183,3.311577,1.542420,7.992574,1.207681,8.298796,-7.251313,9.281875,-8.467575,-1.919706,2.033433,8.301095,2.468463,8.851645,7.964296,-9.404827,5.896237,-8.273650,8.257939,7.167946,-7.267994,9.111963,4.215559,0.074230,-0.467783,0.597802,8.058125,9.653019,8.564865,-8.586405,6.550102,2.234317,-2.537496,-1.580270,8.116733,-0.325035,-7.202361,-0.431698,-3.083192,4.003805,-5.045898,9.213204,-2.831559,-1.178399,1.066510,-3.671972,2.703801,7.234475,0.394209,0.284319,-6.439309,4.854711,-6.221669,-0.613930,3.848863,2.384325,-7.245394,-6.114138,-6.515653,-2.982124,6.661658,-5.720036,-8.555889,-7.422692,6.057589,-1.353294,6.728703,-8.663212,-1.621987,2.003507,1.955217,7.999657,4.137836,-8.483973,-9.164082,2.652213,8.238538,-5.444878,0.012070,-0.960145,3.968450,-8.539720,-5.741442,-4.212994,2.295075,-4.538822,-7.761122,9.117073,5.747357,4.002194,-2.112777,6.439752,2.150789,-4.355221,-6.852083,8.171795,0.499841,0.402521,4.388980,-7.696051,8.082818,8.595381,-5.146303,4.723248,-2.287845,3.899221,9.653502,-3.278931,0.376984,5.447329,7.701070,5.979526,6.897341,-9.693247,-7.483462,2.028404,-1.750317,9.812644,5.092387,-4.488787,-5.634462,5.703575,0.074508,-2.275258,-3.361522,-1.076541,-7.378865,-1.491953,-7.169325,-2.882526,-6.354826,-3.772704,-1.652476,2.735648,-5.024307,9.082732,-6.786348,-9.814236,5.338014,-9.384353,0.357778,4.024143,-8.936696,4.384617,0.658833,3.945563,6.750007,-8.772631,3.919783,-4.791623,8.384506,-6.793613,-2.134596,5.328491,7.220133,0.417487,1.750727,8.178690,-5.476985,-0.970184,-7.271799,5.434404,-8.576768,-0.198127,-5.239108,0.577203,-1.432581,9.696247,9.919971,-2.280337,-9.932739,6.544259,6.649012,8.677107,2.030200,6.856131,6.800594,1.454661,-6.545967,4.875752,-5.109441,-6.735527,4.071654,9.922875,4.097893,4.463906,4.705800,2.088688,6.175819,8.640044,-4.410690,9.875489,7.147820,8.457630,-3.742816,-2.013300,-7.319268,1.480605,-2.349797,-8.307000,8.538352,1.879588,-8.272885,2.174939,9.155740,-8.950381,3.567848,8.170235,-0.758850,-3.619701,-3.032652,-0.931005,8.238054,-8.464548,-9.789221,9.353469,-2.161919,5.137213,7.125439,5.597660,4.557734,9.745659,2.448493,6.696021,5.521505,-5.091432,3.044617,-3.146239,-8.572587,-5.395294,6.897171,-0.501975,9.382718,-2.405517,-0.441025,3.897788,7.091575,-4.735489,-3.104933,0.189483,6.412499,8.331661,-9.760763,-8.930340,-6.455255,1.373213,-1.307760,1.026914,0.665307,7.128772,1.031141,5.212172,9.213937,7.679609,-6.097858,0.638288,-1.858501,-9.097165,1.066496,-1.525705,2.319947,7.174071,0.508777,8.992718,2.225767,5.033035,-8.363426,2.213605,-4.019420,0.677971,7.077652,2.792754,5.089197,-7.301431,-7.967441,-5.918133,1.605700,0.348255,-7.590373,2.179656,7.724997,3.381523,-2.147828,1.019095,5.531002,6.132837,-1.257107,0.363849,-6.990477,-0.923921,-4.920082,-6.833316,-8.313122,-2.081103,6.620200,-6.370691,-8.115773,-8.062507,1.297113,-9.948695,-0.361416,2.608902,-4.343703,-7.576507,2.970698,4.538627,8.071665,7.339787,5.382332,-1.934996,0.913489,-5.901904,-2.727502,-5.304284,-0.047409,1.224987,-8.925427,6.123909,0.216004,8.385474,-0.872992,-3.137092,0.498945,-9.442561,8.600365,8.205522,8.010351,6.215621,-7.559942,6.289622,-2.938162,4.267564,-0.759980,9.523857,-5.677131,-8.653674,9.412918,-9.257430,-2.033383,3.182601,1.756407,-1.423336,-7.850327,5.781165,-1.057836,-5.499268,2.937004,3.757682,-8.406775,3.934563,-4.339304,-5.550689,-4.793187,-1.476075,7.145736,-5.655689,-6.776655,7.334185,-8.712523,8.944342,-6.772195,6.631440,1.192097,5.884714,0.343610,-9.892844,-4.993906,2.739704,4.919120,5.026659,-9.973354,5.283569,-3.163294,6.432234,4.425478,0.093400,-0.622831,4.069957,-2.205490,-5.695868,2.546982,8.762518,3.984217,-6.151231,-9.452126,4.726720,-3.658095,4.669180,8.150473,1.914481,0.269447,-8.660622,-7.811309,9.657412,-0.482495,-0.950039,-2.260702,3.289859,3.921923,-5.291269,1.272303,-1.723950,-0.947304,1.054153,-6.347185,6.005698,2.995320,-4.108976,0.679829,-6.966302,8.777170,-6.552843,-0.104217,5.068403,5.866666,7.003219,1.965309,-4.926748,8.307952,9.150447,3.457232,3.193585,0.623297,-6.406146,7.144559,-2.151382,0.668220,-6.488294,2.817133,4.161956,1.079436,6.732322,-9.395041,9.649637,1.662223,-5.768139,0.273902,-7.780221,7.476570,5.060303,9.912996,6.257099,-2.763127,6.171357,4.336694,5.102114,1.139731,3.393154,-6.079515,-0.152798,1.465444,-8.237088]], dtype = "float32")#candidate|6581|(1, 624)|const|float32
call_6580 = relay.TupleGetItem(func_384_call(relay.reshape(const_6581.astype('float32'), [13, 12, 4])), 0)
call_6582 = relay.TupleGetItem(func_387_call(relay.reshape(const_6581.astype('float32'), [13, 12, 4])), 0)
bop_6603 = relay.bitwise_xor(const_6581.astype('uint16'), relay.reshape(call_6580.astype('uint16'), relay.shape_of(const_6581))) # shape=(1, 624)
bop_6606 = relay.bitwise_xor(const_6581.astype('uint16'), relay.reshape(call_6582.astype('uint16'), relay.shape_of(const_6581))) # shape=(1, 624)
output = relay.Tuple([call_6528,bop_6603,])
output2 = relay.Tuple([call_6529,bop_6606,])
func_6611 = relay.Function([], output)
mod['func_6611'] = func_6611
mod = relay.transform.InferType()(mod)
output = func_6611()
func_6612 = relay.Function([], output)
mutated_mod['func_6612'] = func_6612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5816_call = mod.get_global_var('func_5816')
func_5818_call = mutated_mod.get_global_var('func_5818')
call_6621 = relay.TupleGetItem(func_5816_call(), 0)
call_6622 = relay.TupleGetItem(func_5818_call(), 0)
var_6634 = relay.var("var_6634", dtype = "float64", shape = (11, 3, 16))#candidate|6634|(11, 3, 16)|var|float64
bop_6635 = relay.subtract(call_6621.astype('int32'), relay.reshape(var_6634.astype('int32'), relay.shape_of(call_6621))) # shape=(11, 3, 16)
bop_6638 = relay.subtract(call_6622.astype('int32'), relay.reshape(var_6634.astype('int32'), relay.shape_of(call_6622))) # shape=(11, 3, 16)
uop_6640 = relay.cosh(var_6634.astype('float32')) # shape=(11, 3, 16)
uop_6650 = relay.sinh(uop_6640.astype('float32')) # shape=(11, 3, 16)
func_2614_call = mod.get_global_var('func_2614')
func_2618_call = mutated_mod.get_global_var('func_2618')
var_6657 = relay.var("var_6657", dtype = "float32", shape = ())#candidate|6657|()|var|float32
const_6658 = relay.const([[-0.306239,-3.751174,-0.035999,-8.677548,7.161408,2.765741,2.160016,4.239414,1.823806,1.222960,-5.693442,-3.009341,-3.437875,5.023483,-9.027227,-5.613277,-6.978057,-6.069815,-4.510571,6.009204,3.878472,-1.550761,9.419166,-4.675055,7.987703,3.895570,2.055784,-9.011554,3.890584,2.505324,-5.112722,1.974376,-4.313299,4.765988,-2.908290,1.345793,3.898085,-8.222704,9.740038,5.115205,-0.357466,1.740564,9.340818,1.690824,8.981036,-8.893206,-6.744553,6.013649,0.425901,-6.140450,7.905929,1.236368,4.530012,-2.741212,-0.665169,-2.605852,-4.455161,-3.247071,6.887542,6.489979,-2.097636,4.331717,7.697474,-9.966598,2.721915,-5.166939,-9.863129,-9.122087,6.228973,-2.446573,-4.407166,5.693522,-7.156567,-2.815452,1.017323,7.593378,9.416579,3.798949,3.153193,4.730305]], dtype = "float32")#candidate|6658|(1, 80)|const|float32
call_6656 = relay.TupleGetItem(func_2614_call(relay.reshape(var_6657.astype('float32'), []), relay.reshape(const_6658.astype('float32'), [5, 1, 16]), ), 1)
call_6659 = relay.TupleGetItem(func_2618_call(relay.reshape(var_6657.astype('float32'), []), relay.reshape(const_6658.astype('float32'), [5, 1, 16]), ), 1)
output = relay.Tuple([bop_6635,uop_6650,call_6656,var_6657,const_6658,])
output2 = relay.Tuple([bop_6638,uop_6650,call_6659,var_6657,const_6658,])
func_6663 = relay.Function([var_6634,var_6657,], output)
mod['func_6663'] = func_6663
mod = relay.transform.InferType()(mod)
var_6664 = relay.var("var_6664", dtype = "float64", shape = (11, 3, 16))#candidate|6664|(11, 3, 16)|var|float64
var_6665 = relay.var("var_6665", dtype = "float32", shape = ())#candidate|6665|()|var|float32
output = func_6663(var_6664,var_6665,)
func_6666 = relay.Function([var_6664,var_6665,], output)
mutated_mod['func_6666'] = func_6666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_6668 = relay.TupleGetItem(func_5104_call(), 0)
call_6669 = relay.TupleGetItem(func_5106_call(), 0)
uop_6671 = relay.exp(call_6668.astype('float32')) # shape=(15, 8, 15)
uop_6673 = relay.exp(call_6669.astype('float32')) # shape=(15, 8, 15)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_6688 = relay.TupleGetItem(func_5509_call(), 2)
call_6689 = relay.TupleGetItem(func_5511_call(), 2)
output = relay.Tuple([uop_6671,call_6688,])
output2 = relay.Tuple([uop_6673,call_6689,])
func_6713 = relay.Function([], output)
mod['func_6713'] = func_6713
mod = relay.transform.InferType()(mod)
output = func_6713()
func_6714 = relay.Function([], output)
mutated_mod['func_6714'] = func_6714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_6743 = relay.TupleGetItem(func_5104_call(), 0)
call_6744 = relay.TupleGetItem(func_5106_call(), 0)
output = call_6743
output2 = call_6744
func_6769 = relay.Function([], output)
mod['func_6769'] = func_6769
mod = relay.transform.InferType()(mod)
mutated_mod['func_6769'] = func_6769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6769_call = mutated_mod.get_global_var('func_6769')
call_6770 = func_6769_call()
output = call_6770
func_6771 = relay.Function([], output)
mutated_mod['func_6771'] = func_6771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6769_call = mod.get_global_var('func_6769')
func_6771_call = mutated_mod.get_global_var('func_6771')
call_6772 = func_6769_call()
call_6773 = func_6769_call()
output = relay.Tuple([call_6772,])
output2 = relay.Tuple([call_6773,])
func_6790 = relay.Function([], output)
mod['func_6790'] = func_6790
mod = relay.transform.InferType()(mod)
mutated_mod['func_6790'] = func_6790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6790_call = mutated_mod.get_global_var('func_6790')
call_6791 = func_6790_call()
output = call_6791
func_6792 = relay.Function([], output)
mutated_mod['func_6792'] = func_6792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6365_call = mod.get_global_var('func_6365')
func_6367_call = mutated_mod.get_global_var('func_6367')
call_6809 = func_6365_call()
call_6810 = func_6365_call()
output = relay.Tuple([call_6809,])
output2 = relay.Tuple([call_6810,])
func_6813 = relay.Function([], output)
mod['func_6813'] = func_6813
mod = relay.transform.InferType()(mod)
mutated_mod['func_6813'] = func_6813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6813_call = mutated_mod.get_global_var('func_6813')
call_6814 = func_6813_call()
output = call_6814
func_6815 = relay.Function([], output)
mutated_mod['func_6815'] = func_6815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mod.get_global_var('func_6126')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_6826 = func_6126_call()
call_6827 = func_6126_call()
func_5582_call = mod.get_global_var('func_5582')
func_5584_call = mutated_mod.get_global_var('func_5584')
const_6829 = relay.const([-8,-4,-2,-1,1,-5,-3,9,4,6,-10,-7,1,10,-6,-9,-1,-3,7,6,-5,-9,10,10,8,3,8,-2,2,3,7,4,-6,-1,-10,10,-9,-6,7,-4,-1,-6,9,-7,10,-8,-5,-6,-9,3,5,-5,-2,-3,8,-5,-4,-7,7,-5,6,-3,-8,-2,-6,-4,-8,-5,-1,-1,-8,7,7,7,8,2,-5,-6,4,8,3,-2,5,5,-8,7,5,7,8,8,6,-1,-7,-4,5,2,5,10,1,-8,-2,-4,8,10,5,-3,10,-2,3,9,-9,7,-6,6,2,8,-8,4,-4,-2,-4,2,9,2,-9,1,1,1,-4,-5,-10,4,-3,-4,3,-8,10,-3,-3,2,-6,-9,10,-4,-9,-5,-10,-9,-7,2,10,9,7,3,-8,1,8,1,-1,4,-2,9,8,-6,2,7,9,3,9,-5,1,-1,7,-6,-6,10,-9,-1,8,2,-7,-3,-6,-2,4,-3,5,-3,5,3,-2,-9,-2,8,8,-2,-8,1,1,8,-1,10,5,8,-5,-3,-6,7,-3,-9,-4,5,-6,-5,-10,-2,-4,-4,-6,-10,7,-7,6,-10,9,-1,10,5,4,3,-5,-2,-7,-7,-3,3,2,1,-4,-8,-2,-7,7,-8,-4,-5,-6,-7,5,6,-2,-8], dtype = "uint8")#candidate|6829|(252,)|const|uint8
call_6828 = relay.TupleGetItem(func_5582_call(relay.reshape(const_6829.astype('uint8'), [252,])), 0)
call_6830 = relay.TupleGetItem(func_5584_call(relay.reshape(const_6829.astype('uint8'), [252,])), 0)
output = relay.Tuple([call_6826,call_6828,const_6829,])
output2 = relay.Tuple([call_6827,call_6830,const_6829,])
func_6838 = relay.Function([], output)
mod['func_6838'] = func_6838
mod = relay.transform.InferType()(mod)
mutated_mod['func_6838'] = func_6838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6838_call = mutated_mod.get_global_var('func_6838')
call_6839 = func_6838_call()
output = call_6839
func_6840 = relay.Function([], output)
mutated_mod['func_6840'] = func_6840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6429_call = mod.get_global_var('func_6429')
func_6430_call = mutated_mod.get_global_var('func_6430')
call_6844 = func_6429_call()
call_6845 = func_6429_call()
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_6857 = relay.TupleGetItem(func_5104_call(), 0)
call_6858 = relay.TupleGetItem(func_5106_call(), 0)
func_6813_call = mod.get_global_var('func_6813')
func_6815_call = mutated_mod.get_global_var('func_6815')
call_6864 = relay.TupleGetItem(func_6813_call(), 0)
call_6865 = relay.TupleGetItem(func_6815_call(), 0)
output = relay.Tuple([call_6844,call_6857,call_6864,])
output2 = relay.Tuple([call_6845,call_6858,call_6865,])
func_6885 = relay.Function([], output)
mod['func_6885'] = func_6885
mod = relay.transform.InferType()(mod)
output = func_6885()
func_6886 = relay.Function([], output)
mutated_mod['func_6886'] = func_6886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5870_call = mod.get_global_var('func_5870')
func_5871_call = mutated_mod.get_global_var('func_5871')
call_6887 = func_5870_call()
call_6888 = func_5870_call()
func_5378_call = mod.get_global_var('func_5378')
func_5382_call = mutated_mod.get_global_var('func_5382')
var_6897 = relay.var("var_6897", dtype = "int64", shape = (630,))#candidate|6897|(630,)|var|int64
var_6898 = relay.var("var_6898", dtype = "bool", shape = (1120,))#candidate|6898|(1120,)|var|bool
var_6899 = relay.var("var_6899", dtype = "float64", shape = (1456,))#candidate|6899|(1456,)|var|float64
call_6896 = relay.TupleGetItem(func_5378_call(relay.reshape(var_6897.astype('int64'), [630,]), relay.reshape(var_6898.astype('bool'), [1120,]), relay.reshape(var_6899.astype('float64'), [1456,]), ), 2)
call_6900 = relay.TupleGetItem(func_5382_call(relay.reshape(var_6897.astype('int64'), [630,]), relay.reshape(var_6898.astype('bool'), [1120,]), relay.reshape(var_6899.astype('float64'), [1456,]), ), 2)
output = relay.Tuple([call_6887,call_6896,var_6897,var_6898,var_6899,])
output2 = relay.Tuple([call_6888,call_6900,var_6897,var_6898,var_6899,])
func_6908 = relay.Function([var_6897,var_6898,var_6899,], output)
mod['func_6908'] = func_6908
mod = relay.transform.InferType()(mod)
mutated_mod['func_6908'] = func_6908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6908_call = mutated_mod.get_global_var('func_6908')
var_6910 = relay.var("var_6910", dtype = "int64", shape = (630,))#candidate|6910|(630,)|var|int64
var_6911 = relay.var("var_6911", dtype = "bool", shape = (1120,))#candidate|6911|(1120,)|var|bool
var_6912 = relay.var("var_6912", dtype = "float64", shape = (1456,))#candidate|6912|(1456,)|var|float64
call_6909 = func_6908_call(var_6910,var_6911,var_6912,)
output = call_6909
func_6913 = relay.Function([var_6910,var_6911,var_6912,], output)
mutated_mod['func_6913'] = func_6913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6011_call = mutated_mod.get_global_var('func_6011')
call_6921 = relay.TupleGetItem(func_6009_call(), 0)
call_6922 = relay.TupleGetItem(func_6011_call(), 0)
output = call_6921
output2 = call_6922
func_6924 = relay.Function([], output)
mod['func_6924'] = func_6924
mod = relay.transform.InferType()(mod)
output = func_6924()
func_6925 = relay.Function([], output)
mutated_mod['func_6925'] = func_6925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6365_call = mod.get_global_var('func_6365')
func_6367_call = mutated_mod.get_global_var('func_6367')
call_6938 = func_6365_call()
call_6939 = func_6365_call()
uop_6953 = relay.log2(call_6938.astype('float32')) # shape=(11, 3, 16)
uop_6955 = relay.log2(call_6939.astype('float32')) # shape=(11, 3, 16)
func_5439_call = mod.get_global_var('func_5439')
func_5442_call = mutated_mod.get_global_var('func_5442')
var_6958 = relay.var("var_6958", dtype = "float32", shape = (624,))#candidate|6958|(624,)|var|float32
call_6957 = relay.TupleGetItem(func_5439_call(relay.reshape(var_6958.astype('float32'), [624,])), 0)
call_6959 = relay.TupleGetItem(func_5442_call(relay.reshape(var_6958.astype('float32'), [624,])), 0)
output = relay.Tuple([uop_6953,call_6957,var_6958,])
output2 = relay.Tuple([uop_6955,call_6959,var_6958,])
func_6979 = relay.Function([var_6958,], output)
mod['func_6979'] = func_6979
mod = relay.transform.InferType()(mod)
mutated_mod['func_6979'] = func_6979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6980 = relay.var("var_6980", dtype = "float32", shape = (624,))#candidate|6980|(624,)|var|float32
func_6979_call = mutated_mod.get_global_var('func_6979')
call_6981 = func_6979_call(var_6980)
output = call_6981
func_6982 = relay.Function([var_6980], output)
mutated_mod['func_6982'] = func_6982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6813_call = mod.get_global_var('func_6813')
func_6815_call = mutated_mod.get_global_var('func_6815')
call_7041 = relay.TupleGetItem(func_6813_call(), 0)
call_7042 = relay.TupleGetItem(func_6815_call(), 0)
output = call_7041
output2 = call_7042
func_7051 = relay.Function([], output)
mod['func_7051'] = func_7051
mod = relay.transform.InferType()(mod)
mutated_mod['func_7051'] = func_7051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7051_call = mutated_mod.get_global_var('func_7051')
call_7052 = func_7051_call()
output = call_7052
func_7053 = relay.Function([], output)
mutated_mod['func_7053'] = func_7053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6885_call = mod.get_global_var('func_6885')
func_6886_call = mutated_mod.get_global_var('func_6886')
call_7085 = relay.TupleGetItem(func_6885_call(), 2)
call_7086 = relay.TupleGetItem(func_6886_call(), 2)
output = relay.Tuple([call_7085,])
output2 = relay.Tuple([call_7086,])
func_7102 = relay.Function([], output)
mod['func_7102'] = func_7102
mod = relay.transform.InferType()(mod)
mutated_mod['func_7102'] = func_7102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7102_call = mutated_mod.get_global_var('func_7102')
call_7103 = func_7102_call()
output = call_7103
func_7104 = relay.Function([], output)
mutated_mod['func_7104'] = func_7104
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7116 = relay.var("var_7116", dtype = "int8", shape = (8, 9, 12))#candidate|7116|(8, 9, 12)|var|int8
const_7117 = relay.const([[[6,-10,-3,7,7,5,6,10,-4,1,4,-3],[-5,5,-7,-1,5,1,-6,3,-6,7,-8,-7],[-9,10,-10,-10,-1,5,7,9,7,9,-8,-9],[3,-8,4,-3,-6,6,5,2,-10,4,-5,9],[-4,-7,5,9,-3,-8,4,10,4,7,10,7],[-6,-9,-5,3,9,4,-8,-1,-1,10,10,-7],[-5,-6,-4,7,4,-9,4,-8,5,-4,-6,6],[4,5,5,8,8,7,9,-10,-7,3,4,-4],[-3,2,5,-9,3,3,-7,9,7,7,-7,-8]],[[-7,-8,2,10,2,7,9,4,-9,1,8,-3],[-6,-10,9,-9,-6,-7,-9,-4,-8,-8,-6,-8],[-9,-4,9,-3,-8,-9,-8,-3,-5,3,-7,7],[-9,-2,-7,-3,-1,5,-2,6,1,9,4,-6],[-4,5,7,9,-6,4,-3,-2,-1,4,-7,-5],[4,8,8,6,-2,-5,4,-8,7,6,6,-4],[-6,2,7,-2,3,-10,3,-5,9,-5,-6,-5],[-2,10,-10,-6,-3,10,6,-4,3,2,-9,2],[-8,1,9,-4,-9,-10,1,5,-4,5,-8,-1]],[[-2,-8,1,-9,6,-3,-7,7,-3,5,5,-9],[9,-1,2,10,4,-5,6,5,5,7,5,10],[-1,4,-8,-4,-9,-4,6,5,1,-8,5,1],[1,3,-1,6,1,9,6,-4,10,-6,-1,-10],[-2,-9,2,-8,-7,-9,-6,-4,8,6,-9,-7],[-8,9,5,-2,-8,3,-3,10,-1,-10,-5,-4],[10,-5,10,-9,-6,-8,8,5,10,-5,-6,-3],[-4,-4,9,-2,-7,9,-10,6,9,-4,-3,-4],[-6,6,-3,-8,3,-8,1,-3,-8,8,1,5]],[[-9,8,9,-6,10,-8,2,10,10,-2,-9,-1],[-7,6,-4,-9,-1,6,-10,4,4,-1,-7,-6],[10,-10,-2,5,-2,9,-1,9,-7,1,-7,7],[4,-2,10,10,5,-6,-2,8,1,8,-8,-5],[3,-2,10,4,7,7,-1,7,8,4,-4,4],[2,1,-10,-6,-4,-3,-10,-8,-2,-6,5,-10],[-7,-5,-7,-10,10,10,8,2,4,6,-2,-3],[-1,-7,2,-1,2,-10,4,1,-1,-3,4,-1],[-3,-4,-1,-9,-6,1,6,5,-10,10,-6,10]],[[-9,-6,-10,-5,4,-8,-6,9,7,-8,-4,10],[1,-7,-10,-4,-10,4,-1,-5,-8,-2,-1,-6],[1,-9,10,-8,-1,8,2,10,4,3,3,-10],[8,5,3,8,-7,8,8,8,10,3,-8,3],[-9,7,2,-2,9,10,3,7,-6,-7,2,-6],[-1,-2,3,1,10,3,5,-4,7,10,3,9],[-2,-4,4,-7,-10,-2,-4,5,10,8,7,4],[6,-3,-9,8,9,-8,-3,-7,-5,6,-1,7],[-10,9,-7,-1,-4,3,7,9,-7,-10,-3,5]],[[-6,-7,-3,10,-9,3,1,2,8,-3,1,2],[8,-8,1,-10,6,3,4,-5,4,1,-3,3],[2,-8,-7,-1,-4,-7,-2,-9,-4,8,-8,1],[2,-7,8,-6,-7,1,5,-10,-1,-2,-6,3],[-5,-10,-5,-7,6,2,8,-4,10,-9,-7,4],[10,3,6,7,-7,8,-1,-9,-1,-1,-8,-1],[10,3,-1,-9,2,-6,-8,-2,2,-6,-5,10],[-7,4,-5,4,-9,7,6,2,8,8,2,10],[2,-9,-3,4,1,7,-6,-3,10,4,6,5]],[[3,9,-3,-1,6,-3,-8,-1,6,-5,9,-7],[10,6,-7,-1,4,6,-8,4,7,-5,4,-4],[-3,5,6,2,3,-5,7,-3,-5,-8,-7,9],[10,9,-9,6,-1,-4,3,7,4,-8,-6,-1],[1,-6,-2,2,-8,-7,5,10,4,-5,10,1],[-3,-4,-10,-2,6,9,4,1,-6,10,2,9],[4,1,5,-9,-2,7,-1,5,6,5,-7,1],[-7,-5,1,-6,-8,-2,-10,-3,-5,6,-9,3],[-5,7,-7,3,9,6,10,8,9,-2,10,-3]],[[6,-3,10,-2,6,-5,6,-10,8,9,-6,-7],[-7,-3,-2,6,-4,3,-6,-9,2,7,5,-7],[1,-10,-4,-1,-4,2,1,-6,-8,10,-3,8],[4,7,3,2,-1,1,9,-6,6,-1,-5,-1],[7,7,-10,-7,-10,-6,6,7,8,3,-9,10],[-9,4,9,9,9,-6,-2,-5,-5,5,7,-1],[9,-2,-6,-8,5,-1,7,10,7,-5,7,3],[-9,5,2,10,-1,2,7,2,-1,-6,-2,-6],[-2,-2,-3,3,3,9,-4,-9,-3,2,-2,-10]]], dtype = "int8")#candidate|7117|(8, 9, 12)|const|int8
bop_7118 = relay.bitwise_and(var_7116.astype('int8'), relay.reshape(const_7117.astype('int8'), relay.shape_of(var_7116))) # shape=(8, 9, 12)
func_6908_call = mod.get_global_var('func_6908')
func_6913_call = mutated_mod.get_global_var('func_6913')
var_7124 = relay.var("var_7124", dtype = "int64", shape = (630,))#candidate|7124|(630,)|var|int64
var_7125 = relay.var("var_7125", dtype = "bool", shape = (1, 1120))#candidate|7125|(1, 1120)|var|bool
const_7126 = relay.const([[-2.905613,-7.514569,-0.270182,-1.073215,1.989392,8.883832,8.889054,-4.608951,5.817589,7.238511,-7.044688,9.396595,7.453751,-5.808547,3.565350,6.610331,3.371195,9.788462,0.317900,9.597126,-2.863668,4.468190,-4.154809,-4.168552,-0.476647,0.524869,7.052204,-3.315954,8.178646,-4.146176,8.648519,-3.761253,-0.333695,-6.924437,9.389204,-3.693150,3.132970,8.825981,2.813053,0.858668,-1.756495,-7.144344,9.127178,-4.560157,4.850505,-5.273707,-3.111998,4.913503,-9.560476,0.670963,-0.429172,6.483079,9.425578,3.535645,-5.805675,-6.292777,4.944089,1.646735,-6.447363,7.578266,-1.914534,-8.606080,-0.155277,5.685191,3.371953,9.011957,-6.376536,9.044326,9.733684,-8.857937,7.107439,-8.625631,-6.835693,-9.810606,-1.922015,-3.506577,1.088332,6.464654,8.231171,-5.870958,3.663826,-9.193456,-1.498584,-4.856831,-1.409621,-1.891656,5.642323,-1.986215,-7.241511,-4.652455,-6.862448,9.473603,0.360106,6.828958,-6.014158,-9.236511,0.079153,1.465655,-2.357324,-4.036929,5.967821,8.507478,7.105447,-9.414378,-1.573781,-3.082703,0.631743,-3.800701,6.532271,4.871505,3.819176,8.557637,-9.882417,-7.222908,-8.919781,7.159023,6.695878,0.862327,-1.374878,-2.475982,-1.166048,3.650788,2.168068,9.624801,-8.062678,-1.491455,-6.704910,-1.595341,-7.205175,8.702890,5.624155,-1.726745,6.525604,-3.628529,1.326649,-6.500721,2.258147,-8.881638,5.953647,1.474712,-5.938107,7.871737,-5.746471,-4.098762,3.579709,3.230454,-7.865982,3.566782,2.959702,-7.043121,8.871929,3.237946,-9.403379,6.082831,8.602224,1.190211,-4.214139,-4.687125,2.384755,8.855717,-5.902036,0.334903,9.011297,2.692641,-4.896193,0.290650,-6.398857,2.770657,-4.857740,2.786355,2.194289,-2.802494,7.567506,-5.243781,6.212321,1.910048,3.740558,-6.089640,-8.387737,0.649631,0.784392,-6.471649,2.532560,6.479536,-4.504730,8.831183,4.630332,1.747372,-2.751191,9.375448,9.637991,-6.001719,-9.167734,8.822729,-9.165820,4.654500,-6.983396,2.258649,3.713878,3.789399,8.037470,-0.976056,-1.066324,-6.427073,7.173749,-9.918380,-6.426619,9.074410,-6.730771,4.832702,-8.487115,-3.819533,-0.316955,-1.227535,-4.006590,5.748810,0.385240,2.442030,2.085767,-4.008643,1.569333,-9.241101,1.206377,-7.157722,-1.600227,-9.303993,7.511217,4.390682,3.761780,9.018330,-6.902294,9.160752,-7.662619,2.639468,-2.871201,3.134377,9.375600,-9.376119,4.075714,-6.631702,-3.006368,-9.298084,1.800183,-9.685494,-4.834622,0.472798,-3.340796,-2.452557,8.903495,5.691189,7.673603,5.733628,-8.641712,-4.969694,0.765200,8.287328,4.041791,0.514978,-8.470309,9.378881,7.735727,2.841193,-4.283339,9.711430,7.856345,8.251727,3.729305,2.062739,-1.615484,1.805181,-3.464304,-7.109521,9.447274,9.544217,9.097932,-1.628466,8.805816,-1.971063,1.235000,3.730463,-9.897447,0.486665,2.679576,9.167861,-1.832381,4.513943,-3.501046,6.435665,9.497051,6.350954,1.003321,-6.928505,0.787551,-0.828975,-0.523958,7.820451,5.478423,-2.015800,-1.658134,-0.640071,-3.266899,6.472111,8.649873,-7.674932,5.562947,0.727155,0.391809,3.733878,0.881358,2.798174,4.781104,-9.034494,-4.878248,-9.568425,4.621402,6.317928,-5.431231,-1.998369,7.644134,0.774274,-8.373775,-2.863866,-9.331154,-8.104254,3.841153,4.305188,-0.960861,3.453210,-0.506602,8.524656,2.781428,8.312800,-7.094262,2.395993,2.081731,-8.769086,-3.259804,4.417269,7.383337,-4.553564,-8.245489,4.223484,1.319419,8.593255,-4.330032,6.363387,8.739095,-9.458517,-3.645199,-0.483133,-0.796377,2.515177,9.557138,9.339397,-3.426128,1.653687,6.267511,-9.950660,-2.638117,-4.691606,-2.108272,-5.360941,-6.368470,3.280926],[-1.334560,-5.189800,4.215421,2.529798,2.481109,3.007272,-5.176180,-3.514507,6.988740,7.222696,-0.508675,4.717226,5.411089,-7.734215,-6.548479,9.654692,3.540338,4.230943,0.205623,1.843196,0.523749,4.882313,-4.440320,5.489140,-5.048841,2.654540,-0.406783,3.221421,-4.292309,5.279411,-8.141706,0.365500,1.682896,-6.450670,-3.424139,5.217082,-2.836784,2.357702,-5.702177,-6.492507,2.895209,4.688440,-5.014089,-8.138203,-9.541388,6.034955,-3.568004,0.866110,7.106309,-1.979264,2.522461,2.450078,-3.184408,-7.979995,9.272912,4.255064,-0.082130,-0.897838,-3.664855,3.032617,4.214703,3.793843,-8.445840,7.627822,-9.447559,5.622541,9.432127,1.312183,6.745830,-2.751148,-4.515202,-7.781232,-7.185206,-7.131984,0.426820,9.237418,-5.977832,-9.560032,3.439774,8.345066,1.094185,-9.670267,8.234848,3.001574,3.351229,-9.033718,8.798040,7.723259,2.088186,-8.185255,8.363638,7.013581,-1.309432,-5.668218,0.794968,9.644843,-6.286277,9.889816,4.753861,9.186664,-7.352349,6.620014,-6.723175,4.471427,-5.279850,-5.927721,-7.674187,6.461421,6.048636,-3.925100,3.774569,2.766660,0.625949,-1.855915,4.524526,-4.778988,4.391610,-2.267657,-3.416225,3.491797,0.231815,-9.957419,-0.318224,7.029087,-8.125162,-0.989970,2.707967,2.660359,4.029850,-9.753396,4.076742,-4.113637,-0.174408,-6.987577,7.455111,5.105282,0.778505,-6.705051,5.291017,9.352445,1.668606,-9.004719,-9.498179,-9.238216,5.311594,-7.604134,0.743657,6.449182,3.935447,-4.866344,0.622197,-3.552438,1.081843,-6.317226,-0.037447,-2.338540,-9.792772,-0.961571,8.173107,-1.477348,7.660213,8.274854,7.297419,-8.577132,9.468496,6.036881,-5.419364,6.759037,-0.875687,0.307760,-1.836248,1.690497,-8.312940,2.495891,-6.559223,-7.883663,-8.936044,-4.451062,-0.774785,3.193608,1.294732,-4.914431,-6.625441,7.487808,-3.465992,0.642969,9.962839,5.410395,-9.372054,9.813593,-8.786403,8.558718,8.153224,-0.257598,-1.446412,9.096552,2.697760,-3.533709,-3.993573,-5.235886,-4.304331,1.690046,-1.712145,7.748516,7.113364,5.815113,-3.499058,-1.638866,-7.204929,2.182992,-4.827550,-8.414430,-5.768664,9.311827,6.481870,3.567106,1.216534,0.652283,4.360642,3.765063,9.722950,-2.360559,7.324304,5.636019,-6.041122,-3.704060,-5.451501,-0.493956,7.445393,5.057652,6.624276,-1.103354,5.101255,6.592955,-7.177713,1.428509,6.086517,2.991268,-3.842911,2.202697,5.905781,-0.842403,-7.960422,8.230492,-1.480577,-8.174965,4.431421,2.660703,-3.938890,-3.711350,5.189927,-4.586575,0.280810,7.272724,7.762278,-6.457655,-6.380076,-2.430234,5.125082,6.602667,-6.580119,-5.359350,-5.535478,-2.027321,-3.472414,-8.529968,-3.558772,-6.314724,-0.916258,0.049533,-6.295699,5.117255,-0.196125,-3.444232,7.624262,-5.878191,6.679978,6.118228,-6.348192,8.303400,-2.150980,-8.766260,-3.824322,6.107420,-8.892392,-3.094336,-2.389590,8.784887,4.842646,3.372259,6.675574,-3.769631,-0.192872,3.249265,6.437426,0.382756,-3.372506,-0.787087,-9.549234,9.951340,2.379549,-4.179818,6.937379,-9.450285,5.530938,5.429683,9.045311,5.479720,-7.338824,-6.441988,3.497018,5.011295,9.899341,0.128922,2.280476,-9.213786,-6.179588,9.665061,8.616051,5.623665,6.914646,3.838478,-4.093460,-7.076594,1.494651,8.884854,-1.900394,-0.012606,-5.048210,7.612636,7.935922,-0.569756,-2.206346,2.084154,-4.343353,-2.716710,-8.257560,-7.592860,8.913480,2.165056,-3.061844,7.223062,0.834958,-1.432189,5.839399,-3.007542,-6.702772,1.253291,-3.744104,-2.237154,6.619162,-1.009604,-7.834467,-1.786888,3.180885,0.639302,-6.205110,-2.437748,-0.956361,-0.141764,-1.285438,-6.079197,2.425680,-6.680653],[3.080570,-1.106167,2.395325,-4.570207,-3.278172,5.566521,-6.511358,1.807317,-1.723587,-6.179127,-0.705321,-3.699129,3.173370,0.596086,-0.279264,-1.851625,-3.388009,-8.551196,1.626662,-3.655282,-7.627169,9.666325,-9.867045,8.544575,-4.099463,0.168516,-8.344466,-4.868266,0.871537,5.996297,4.448217,2.899135,-7.658367,0.440603,-9.818792,5.569858,-6.789891,3.824548,9.314957,6.619885,-0.124393,1.981349,-4.003719,7.556732,7.527616,-6.796870,-5.734160,0.218590,6.772706,6.820367,-2.077495,-3.643580,6.948506,8.380042,1.233325,2.745096,1.802321,-9.020616,-0.401153,6.649118,-8.608764,-5.368567,0.543844,-5.167056,-4.453600,-7.471496,-2.062333,1.961711,-9.227642,6.875334,9.428321,-1.778406,1.853099,8.947212,-1.793496,4.695077,-4.637480,3.966155,8.669797,-6.848478,1.232792,-4.949481,-9.447412,-1.959442,-2.180605,-4.496312,-7.067307,2.912113,1.820879,3.362574,4.335946,4.222420,-8.542336,-6.013261,-6.380429,2.095851,9.198030,4.385552,-9.838732,2.603689,8.260414,-4.259693,-0.474746,5.372434,-9.027796,8.406581,-3.124761,9.713290,8.604621,-9.171106,6.141013,-5.171983,-2.416918,-8.902036,3.775087,8.294684,2.516044,-5.641598,2.241759,5.190028,-6.657592,-7.040108,3.341317,9.888813,8.429140,-8.756617,3.103920,2.017323,7.923079,-5.173730,6.199215,0.680095,-1.082398,-5.790834,-8.132257,0.872951,-0.266633,2.503363,-0.482893,3.481361,-7.640499,-4.606100,-3.129420,2.770149,3.518501,-8.595323,-4.269103,1.294929,5.784022,-2.271263,5.769895,-9.307236,5.183237,-3.818119,-7.974545,5.628382,9.965622,-5.843670,-1.465188,8.798557,-0.097009,-0.013504,-6.002914,5.291932,-9.287342,0.353661,6.625045,5.544371,7.223278,-9.604231,5.035163,-7.043759,0.998747,-4.981798,1.878184,2.574755,7.496225,-1.516221,6.911131,3.191288,2.416172,-4.989412,-7.109117,-8.707792,9.015782,7.933939,-2.992938,0.045901,6.549638,6.345452,-0.877447,-6.196499,4.344024,9.479452,-9.370267,-8.753089,0.921988,-0.833467,-8.792434,0.685442,-8.187991,8.845773,-7.686177,-9.110145,-2.676618,-2.424025,5.492650,0.433508,5.811166,3.927147,1.745397,-3.312214,-6.940582,5.208700,6.365678,-0.104897,8.676619,-3.078413,2.333523,3.770844,5.907694,-3.519322,-0.673294,8.743297,-3.765478,2.698428,-9.211105,-3.725736,7.203952,1.232893,-1.482392,-1.614692,2.697512,7.749381,9.430914,5.862989,3.911874,9.618409,6.315833,6.580073,-3.793968,9.752222,-4.397949,9.356238,5.019022,-0.709212,2.369527,-9.791775,-7.846512,0.382474,-4.372798,-4.583194,-0.962988,-8.949695,-6.450970,9.883145,-5.439269,5.561558,-7.373285,-2.197504,7.571061,4.324633,5.568509,-1.828350,0.099782,-8.426978,-9.025661,2.385793,-9.616286,-9.539925,-1.566600,1.334302,-3.750249,1.108949,-9.783729,4.570988,9.081589,-7.281172,-3.055163,-6.947811,-8.910385,6.315468,7.166699,4.968948,-9.759523,-1.682460,2.305383,-0.187951,-8.766192,-3.831278,4.076771,-2.541576,-9.000167,-0.736161,2.556976,-5.474966,5.478318,-9.821515,6.657051,-3.494766,2.435752,-7.527745,2.093877,5.309851,-7.946684,-2.394482,3.353733,-1.557333,4.608204,-6.716253,7.395764,-9.567527,-6.690499,5.639504,-1.126321,-6.951223,-5.182644,-9.673081,9.292523,1.026816,3.982180,4.932264,8.229785,-2.406517,-3.655473,7.949874,5.035078,-5.200932,4.466624,5.751612,-4.210174,3.521935,-9.085397,-4.907525,0.508209,-3.037632,8.983156,8.840228,7.887226,4.275734,-5.952135,-9.294642,-2.267446,-8.433310,-8.212870,6.244798,6.212606,-2.417109,-1.614150,4.879398,-5.004196,-4.641615,4.056679,-8.437779,0.972140,7.328556,9.954290,7.569953,-1.432529,1.898843,-4.090558,2.126971,0.622810,5.111429],[-9.819797,-8.830375,-6.427011,-2.654768,-1.744107,0.236081,-8.769189,-4.406831,-0.418321,2.018022,4.079733,3.243325,5.391078,1.284298,-3.671912,-1.726928,6.761641,-4.814254,1.112842,5.664088,1.218107,9.109317,4.868573,1.170651,-7.685074,0.600918,4.174541,6.953641,8.581447,-8.800209,9.363740,8.520128,4.572808,2.288218,-8.133907,-8.333548,0.237200,-5.480359,9.406243,-7.024166,-5.536956,3.562781,-3.387530,3.349047,4.433999,-4.586209,-4.125535,0.323701,0.939541,2.189216,-8.325330,0.322616,3.383645,-1.262485,-7.799220,-0.021487,-6.559526,-4.403944,-2.901321,9.507435,3.863571,6.564706,4.506537,6.517587,6.256852,-2.625616,2.249461,0.808058,0.125638,9.969326,-7.170817,4.325316,-1.030159,1.680064,7.383600,-8.142975,-2.105910,-8.503585,9.707801,-2.282222,-5.235662,-5.136817,7.895981,3.445318,8.646146,-2.593773,-2.331832,9.277656,6.745599,-0.290004,0.625196,-0.893528,-1.247980,7.440830,-7.363277,-0.321658,-8.624210,-0.458422,-6.227395,6.385526,3.684995,7.019663,6.432973,-1.630264,3.271209,7.754869,9.980313,8.730639,-9.847054,3.409286,-3.395615,-8.763966,-4.951340,-3.324622,-6.912309,2.679386,6.884792,5.975565,4.657434,-3.964622,-5.528942,9.814114,8.009917,3.396754,4.874882,-0.848733,-6.579335,-4.645256,-1.125145,1.738300,-8.828724,-0.833672,1.772081,-5.682946,9.048328,-0.384826,-0.301842,0.177228,-9.213696,-3.727684,-9.823951,5.853184,1.146244,2.810928,2.658749,-7.961154,9.023587,6.340782,-2.471956,9.978514,-6.259121,-3.638484,6.832926,-8.216463,-2.352312,7.554451,-4.793233,-3.369244,9.599308,4.714142,-1.767629,-9.740026,-6.688769,9.040160,-7.736462,-9.348365,-1.462203,6.619295,-6.550909,2.074144,-1.813673,9.820408,2.968934,-5.930871,-4.516799,6.604111,5.727641,-3.023151,-1.864588,7.423368,6.900694,1.171584,-2.663007,2.730457,0.871381,0.671177,-3.575080,-8.300510,-1.379203,-7.693001,-3.279689,-2.413733,7.959372,2.496149,-6.629758,-1.869957,-3.071813,5.343308,8.350636,2.423017,1.621738,-7.027564,-0.589437,6.815029,-0.662076,4.577296,-3.565169,-7.125665,-6.131489,4.231764,-1.500150,-6.923319,5.098335,2.519031,3.249958,1.311675,-8.249811,-6.639327,-7.512356,5.672697,7.280782,1.633954,-9.036534,4.903386,9.585759,3.631444,5.361874,-7.966018,3.211970,9.493935,3.349423,9.144550,-3.496627,-6.894909,-5.548174,9.838596,-4.819642,4.407136,6.332575,3.528573,5.672632,-3.221912,8.193014,8.041738,9.692145,4.247220,-3.726992,-9.520301,-9.935830,7.841003,-4.963526,-2.020005,-7.792258,-1.091529,-3.168271,-5.984188,-1.046561,-8.465511,-8.447921,8.906354,-5.843383,-1.293399,0.177542,-8.245942,1.405450,-4.157139,-7.193500,-7.024114,-8.543625,-9.265831,-3.806258,-5.351629,-0.295594,-8.108083,9.683258,-7.908239,-7.578175,-5.479880,8.824855,2.284055,-0.431416,-5.443917,-1.240220,7.026187,6.386998,-3.316966,3.621209,6.081227,5.937506,-5.938983,4.190736,0.935058,2.621521,9.817463,-3.349193,9.735610,2.646044,4.321302,-4.247611,-8.062424,1.925767,7.965595,-6.527137,-9.647917,5.947688,-6.980758,6.378152,-8.510246,7.833869,8.436503,3.943334,-6.774534,-2.603742,-3.911742,9.213723,2.451299,8.986603,3.361028,5.653121,-3.197922,-9.258836,7.599271,-6.478267,-4.542471,9.171462,2.028253,-3.729397,0.346928,9.819072,7.189187,3.919342,8.659688,8.087040,-1.763359,-9.295523,2.628252,8.025533,-6.056186,2.227568,4.440536,-6.950051,6.803062,-2.904339,-9.922873,-5.807443,-9.188394,-9.284929,7.975017,-6.793381,-4.081618,-8.949592,9.102315,-8.191530,5.388821,-8.831793,-1.303631,7.922999,6.087501,7.059005,9.240032,4.561431,6.627598,-0.721351,-3.567984]], dtype = "float64")#candidate|7126|(4, 364)|const|float64
call_7123 = relay.TupleGetItem(func_6908_call(relay.reshape(var_7124.astype('int64'), [630,]), relay.reshape(var_7125.astype('bool'), [1120,]), relay.reshape(const_7126.astype('float64'), [1456,]), ), 4)
call_7127 = relay.TupleGetItem(func_6913_call(relay.reshape(var_7124.astype('int64'), [630,]), relay.reshape(var_7125.astype('bool'), [1120,]), relay.reshape(const_7126.astype('float64'), [1456,]), ), 4)
func_5221_call = mod.get_global_var('func_5221')
func_5223_call = mutated_mod.get_global_var('func_5223')
var_7129 = relay.var("var_7129", dtype = "float32", shape = (180,))#candidate|7129|(180,)|var|float32
call_7128 = relay.TupleGetItem(func_5221_call(relay.reshape(var_7129.astype('float32'), [90, 2])), 2)
call_7130 = relay.TupleGetItem(func_5223_call(relay.reshape(var_7129.astype('float32'), [90, 2])), 2)
output = relay.Tuple([bop_7118,call_7123,var_7124,var_7125,const_7126,call_7128,var_7129,])
output2 = relay.Tuple([bop_7118,call_7127,var_7124,var_7125,const_7126,call_7130,var_7129,])
func_7132 = relay.Function([var_7116,var_7124,var_7125,var_7129,], output)
mod['func_7132'] = func_7132
mod = relay.transform.InferType()(mod)
mutated_mod['func_7132'] = func_7132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7132_call = mutated_mod.get_global_var('func_7132')
var_7134 = relay.var("var_7134", dtype = "int8", shape = (8, 9, 12))#candidate|7134|(8, 9, 12)|var|int8
var_7135 = relay.var("var_7135", dtype = "int64", shape = (630,))#candidate|7135|(630,)|var|int64
var_7136 = relay.var("var_7136", dtype = "bool", shape = (1, 1120))#candidate|7136|(1, 1120)|var|bool
var_7137 = relay.var("var_7137", dtype = "float32", shape = (180,))#candidate|7137|(180,)|var|float32
call_7133 = func_7132_call(var_7134,var_7135,var_7136,var_7137,)
output = call_7133
func_7138 = relay.Function([var_7134,var_7135,var_7136,var_7137,], output)
mutated_mod['func_7138'] = func_7138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6838_call = mod.get_global_var('func_6838')
func_6840_call = mutated_mod.get_global_var('func_6840')
call_7140 = relay.TupleGetItem(func_6838_call(), 0)
call_7141 = relay.TupleGetItem(func_6840_call(), 0)
func_7051_call = mod.get_global_var('func_7051')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_7146 = func_7051_call()
call_7147 = func_7051_call()
output = relay.Tuple([call_7140,call_7146,])
output2 = relay.Tuple([call_7141,call_7147,])
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
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_7215 = relay.TupleGetItem(func_5104_call(), 0)
call_7216 = relay.TupleGetItem(func_5106_call(), 0)
output = relay.Tuple([call_7215,])
output2 = relay.Tuple([call_7216,])
func_7239 = relay.Function([], output)
mod['func_7239'] = func_7239
mod = relay.transform.InferType()(mod)
output = func_7239()
func_7240 = relay.Function([], output)
mutated_mod['func_7240'] = func_7240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5870_call = mod.get_global_var('func_5870')
func_5871_call = mutated_mod.get_global_var('func_5871')
call_7256 = func_5870_call()
call_7257 = func_5870_call()
func_7102_call = mod.get_global_var('func_7102')
func_7104_call = mutated_mod.get_global_var('func_7104')
call_7258 = relay.TupleGetItem(func_7102_call(), 0)
call_7259 = relay.TupleGetItem(func_7104_call(), 0)
func_5628_call = mod.get_global_var('func_5628')
func_5631_call = mutated_mod.get_global_var('func_5631')
var_7264 = relay.var("var_7264", dtype = "bool", shape = (720,))#candidate|7264|(720,)|var|bool
call_7263 = relay.TupleGetItem(func_5628_call(relay.reshape(call_7256.astype('float32'), [624,]), relay.reshape(var_7264.astype('bool'), [720,]), ), 5)
call_7265 = relay.TupleGetItem(func_5631_call(relay.reshape(call_7256.astype('float32'), [624,]), relay.reshape(var_7264.astype('bool'), [720,]), ), 5)
func_6924_call = mod.get_global_var('func_6924')
func_6925_call = mutated_mod.get_global_var('func_6925')
call_7303 = func_6924_call()
call_7304 = func_6924_call()
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_7305 = relay.TupleGetItem(func_5993_call(), 0)
call_7306 = relay.TupleGetItem(func_5995_call(), 0)
func_7239_call = mod.get_global_var('func_7239')
func_7240_call = mutated_mod.get_global_var('func_7240')
call_7320 = relay.TupleGetItem(func_7239_call(), 0)
call_7321 = relay.TupleGetItem(func_7240_call(), 0)
output = relay.Tuple([call_7256,call_7258,call_7263,var_7264,call_7303,call_7305,call_7320,])
output2 = relay.Tuple([call_7257,call_7259,call_7265,var_7264,call_7304,call_7306,call_7321,])
func_7328 = relay.Function([var_7264,], output)
mod['func_7328'] = func_7328
mod = relay.transform.InferType()(mod)
mutated_mod['func_7328'] = func_7328
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7329 = relay.var("var_7329", dtype = "bool", shape = (720,))#candidate|7329|(720,)|var|bool
func_7328_call = mutated_mod.get_global_var('func_7328')
call_7330 = func_7328_call(var_7329)
output = call_7330
func_7331 = relay.Function([var_7329], output)
mutated_mod['func_7331'] = func_7331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_7404 = relay.TupleGetItem(func_5993_call(), 0)
call_7405 = relay.TupleGetItem(func_5995_call(), 0)
output = relay.Tuple([call_7404,])
output2 = relay.Tuple([call_7405,])
func_7420 = relay.Function([], output)
mod['func_7420'] = func_7420
mod = relay.transform.InferType()(mod)
mutated_mod['func_7420'] = func_7420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7420_call = mutated_mod.get_global_var('func_7420')
call_7421 = func_7420_call()
output = call_7421
func_7422 = relay.Function([], output)
mutated_mod['func_7422'] = func_7422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_7459 = relay.TupleGetItem(func_5104_call(), 0)
call_7460 = relay.TupleGetItem(func_5106_call(), 0)
func_5221_call = mod.get_global_var('func_5221')
func_5223_call = mutated_mod.get_global_var('func_5223')
const_7465 = relay.const([-2.579837,4.311166,-5.602872,5.202827,-7.764803,-5.023333,5.006029,0.287083,8.388436,-6.490479,4.242289,0.603853,2.918324,1.476159,0.618627,-4.045633,-8.459192,-9.667341,9.465621,-7.610018,9.482797,-9.233147,0.932315,4.783882,-6.068545,-3.008244,-9.713500,-6.697125,7.840131,8.680479,-7.654076,6.010276,1.172177,7.771206,6.166858,6.296462,-7.779716,6.881799,4.429960,9.049676,-6.186872,-5.656648,2.539731,-6.511364,-6.964664,7.707340,6.056990,2.905294,-8.578691,-4.746381,-2.441121,-2.978350,3.305162,3.527279,5.435256,4.511834,-5.241448,-7.601823,-3.176607,2.379107,-4.596458,6.798272,0.962396,5.386369,5.356022,4.785429,5.806289,-8.594157,7.818536,2.434584,-3.100606,-4.093555,-3.011689,-7.479284,6.585565,2.578730,5.461969,9.299970,8.817312,-8.796960,-3.952164,3.504577,-8.213173,9.308664,5.484405,-5.997926,3.719767,-2.512985,6.495679,-6.874401,-0.824795,3.629611,-0.714029,-5.652004,9.417891,-8.307940,-8.417088,4.668135,5.226969,-3.953073,0.462000,5.860626,9.267516,4.051633,-1.644992,8.790369,8.626970,-8.712249,-7.416037,-1.487522,-2.940542,2.046616,-3.861531,7.076284,4.141975,-9.871377,-2.008235,0.414171,9.352697,-0.608793,-7.607364,8.878407,-7.736211,6.885255,-3.569287,-0.152441,-0.852438,-7.396671,-6.761263,9.401486,8.232941,6.140075,1.433121,-3.039415,9.226062,-2.908451,-0.551294,7.323674,-9.991529,3.438971,-8.368323,8.826905,-4.613532,5.569600,3.486836,-9.194926,-9.371444,-5.959774,3.574515,6.896515,2.550662,-1.170033,8.555070,6.645203,7.143874,-0.714836,-0.466552,-3.935084,5.893509,-4.822306,-8.640595,-5.284322,-1.194948,-9.164446,2.775474,-0.647050,-1.390854,-4.092011,-5.812309,8.516609,9.521777,-2.792923,2.014295,-8.582913,-2.950123,6.996961,7.251843,-5.120065,-8.304303,9.920972], dtype = "float32")#candidate|7465|(180,)|const|float32
call_7464 = relay.TupleGetItem(func_5221_call(relay.reshape(const_7465.astype('float32'), [90, 2])), 1)
call_7466 = relay.TupleGetItem(func_5223_call(relay.reshape(const_7465.astype('float32'), [90, 2])), 1)
func_6769_call = mod.get_global_var('func_6769')
func_6771_call = mutated_mod.get_global_var('func_6771')
call_7478 = func_6769_call()
call_7479 = func_6769_call()
func_4196_call = mod.get_global_var('func_4196')
func_4201_call = mutated_mod.get_global_var('func_4201')
const_7485 = relay.const([3,-9,-6,-3,-1,-5,8,8,9,8,3,-10,4,-7,8,-5,10,4,-4,8,-5,-10,7,5,-5,3,5,-6,1,-3,1,-9,-3,9,-1,5,-2,-1,2,-6,10,-7,-5,5,-8,4,-6,2,-8,-7,8,5,6,10,3,-4,-5,8,-6,5,-1,3,2,7,4,8,-7,-3,-10,-10,9,8,7,-6,-10,6,10,1,3,-1,-3,3,4,2,1,1,-7,5,-6,6,-2,9,2,-1,7,5,2,9,-6,-4,-2,6,-3,-5,2,4,6,3,3,-4,-7,-2,7,-7,-4,-9,-7,8,-7,-8,4,2,-5,-9,-10,-1,-4,-8,-6,-5,7,7,-8,-1,-9,4,2,5,-1,-6,-9,-10,9,5,2,-6,-3,-2,-9,8,3,-3,-7,2,3,1,-6,7,6,3,-2,-8,3,8,2,-1,-9,1,3,4,-1,9,5,-5,8,2,6,-8,9,-2,-3,7,7,8,9,-7,-8,-10,-2,7,-10,3,6,-6,9,-7,10,4,1,-9,-5,-5,-3,-7,7,-7,2,2,3,-4,-5,-5,-4,4,1,10,-10,-1,7,9,2,10,8,-2,1,3,7,-10,-9,8,8,7,2,-10,-6,2,7,-1,-5,7,-1,3,10,-10,-8,10,8,-5,-7,-1,5,2,5,-8,8,-8,6,8,-5,-7,-1,-10,-6,3,-1,6,-6,-10,2,3,3,-1,-3,7,1,2,10,-3,8,-2,10,6,6,7,4,-10,-3,6,-1,-5,-8,6,-10,6,7,-6,-6,1,2,10,9,-5,-10,-10,5,-3,2,-10,-10,-10,-4,2,-3,-2,2,-1,1,-7,6,-1,-5,-3,-6,1,7,1,-10,-1,-7,-7], dtype = "uint8")#candidate|7485|(330,)|const|uint8
const_7486 = relay.const([-9.390137,5.643119,-2.940558,0.496183,-5.842419,-4.798178,-5.932209,1.094254,-3.460737,2.130030,7.506854,4.855680,-3.487465,8.288164,-1.539155,-7.393524,0.653424,-3.404825,-7.442612,2.363508,9.175147,0.103792,-1.652048,-0.648342,2.644259,1.775052,-2.691741,-1.998971,6.881782,4.841039,3.433043,-6.779251,8.657417,-8.726153,6.455794,2.379732,4.276389,-0.485265,6.214061,-6.392650,-9.995136,-7.136991,-4.064896,8.601232,-3.954241,9.843769,-2.178508,-8.223410,-6.213732,-3.463357,7.494330,-7.586112,-6.424395,-8.804373,8.035883,9.590816,-6.455475,7.043832,-7.533496,-8.160970,8.049333,-1.012838,-6.983106,1.223375,0.380338,-4.461183,9.263109,6.795237,2.177031,-2.287372,-2.966483,-3.876334,1.293703,-5.074578,-4.144963,-9.361173,-8.902374,2.220369,1.760293,-8.975069,-5.166528,9.433521,5.897011,-4.760062,-7.290140,-6.303485,-4.825183,-8.958623,-9.446362,7.228134,7.889539,-7.806388,6.186477,-0.336767,-4.232037,5.073881,9.773882,3.865309,-3.852359,5.831669,-5.051972,6.884569,-4.262432,-0.057883,-9.179675,7.235460,9.772133,-6.791097,-4.167193,3.949726,2.548228,3.604865,-2.598283,5.326904,-7.705680,3.104702,-9.982887,2.785892,-6.142809,3.892389,-7.348772,8.318052,-0.255448,-5.953254,-5.396341,-4.325218,-3.094662,7.060902,-6.247297,0.369825,4.544422,5.087400,-3.502233,6.963069,-6.617710,6.741303,3.513864,-8.099586,-3.444120,-5.480379,-1.403241,-5.954975,5.362572,6.190671,4.088544,-2.886831,-5.017995,-8.748527,5.882189,2.384302,9.521725,-9.463354,3.236427,-6.407635,4.697730,9.295739,4.115613,-0.637194,4.578515,-8.374713,4.813122,1.874277,-4.642568,-5.381218,2.133078,2.570904,-8.176895,-2.823553,-1.022768,-8.004166,8.460105,-8.432364,8.717097,2.354134,-6.334075,0.983463,1.300708,5.816185,7.429969,9.364598,-5.187452,6.628384,-6.702654,-7.130813,-6.235646,-5.279917,-9.637337,3.247645,0.021247,-6.018561,-3.624123,1.504664,4.859186,-0.214694,-9.705001,0.783937,-3.582134,-3.796631,-1.128964,-9.850746,8.106765,0.966686,6.729132,6.837383,5.827250,-9.865837,-0.030303,0.032987,0.172845,-4.723120,5.469768,-7.541368,-5.118194,-4.199298,5.659817,6.977090,1.873327,6.275733,3.644221,-9.498100,-0.118060,1.379927,-8.272904,-3.782955,-6.644320,-7.561736,3.889614,0.960516,7.896277,-1.386494,-6.757749,3.003003,-1.452427,-1.168889,8.419333,1.829270,-7.847476,-8.856799,0.555274,-2.993545,9.955301,-7.645655,3.290022,-5.744779,4.742821,7.666402,3.325817,-4.498421,9.492621,5.198034,8.911964,3.813285,8.391715,-5.808450,-8.472014,-7.481012,5.727071,-3.052850,0.903494,0.363648,-1.175208,-3.189803,8.660059,6.883936,-3.234312,-3.981072,9.055309,7.098572,8.715169,-3.162385,-0.250467,-7.872035,6.127673,-6.196553,2.015679,7.455993,-4.054429,4.320913,-4.530550,3.058357,-8.699391,-0.005815,4.676125,-3.372409,-8.524456,-7.078489,-4.293160,-0.790549,-9.291990,-4.086305,4.012151,5.580881,3.199940,2.228850,1.264987,-2.911327,-3.478860,-4.952203,-5.966147,3.668704,8.418723,7.426471,-6.975572,2.570121,-2.778046,-3.695722,8.217271,-7.561666,3.306330,0.897293,-1.132436,-6.517126,-4.499196,-2.132148,6.790832,8.961724,5.418842,-9.243764,5.924479,-3.653046,3.582924,1.578526,-3.497248,-0.882273,9.932805,6.557961,4.744655,9.751267,-4.654193,4.014352,9.070174,-5.931178,6.738120,-5.933531,-4.723130,7.565431,8.466639,-6.260373,-5.694725,1.180117,-3.734856,2.440424,-7.671981,-2.303486,-6.908476,4.782802,-0.081120,-9.673391,-4.753445,-8.053912,-3.567306,1.477305,-4.957867,9.793614,-7.409924,0.594445,3.701651,-2.918500,0.872629,-3.239308,-3.152606,7.587760,0.876439,7.961831,-4.231697,-3.665161,2.428126,-2.424336,-4.412707,-6.617721,2.725156,9.303237,-5.069211,-7.988919,-9.754842,5.838457,-7.024398,-1.233862,-3.492883,-6.011822,6.736299,9.322213,-2.882789,8.758945,-6.243596,7.261941,0.506712,-7.457609,-3.422997,7.953881,-3.419940,-4.654248,4.025248,-4.235142,-1.074067,-8.765112,-1.219528,-4.886052,8.545795,2.483234,9.921687,6.480291,6.670383,-2.420329,9.448645,2.454124,-3.224525,-6.560001,-4.711380,7.499737,4.787519,-2.104388,-7.619787,-8.708258,-8.890561,0.126792,-4.287388,-5.293972,-1.164016,-7.316226,-7.197274,1.843139,1.405528,-8.150886,9.667537,-0.546412,4.092453,-8.925427,3.085839,-4.745717,-6.667784,2.691234,-0.963124,-6.034781,-3.198382,-8.811252,-2.628387,5.397097,-2.829614,5.726277,3.064409,-3.111436,2.269503,-8.934482,-8.915631,-8.687374,-7.557312,1.225073,-1.562171,-4.798340,-0.995821,7.191805,-4.144541,-9.339560,5.116952,-8.932336,9.861460,8.778885,8.038430,1.246866,-9.974875,-5.562334,5.983776,-4.142359,-7.673055,-6.243152,0.539678,1.811717,-6.193775,-7.689061,-2.850049,4.288088,-8.654919,-2.920390,-4.845061,4.515803,8.629050,-7.733253,2.824528,-4.237176,7.542845,7.736204,5.645683,-2.811701,-2.026064,8.022652,-9.385108,3.311018,6.450421,-0.390369,9.345524,4.859213,-8.974278,-3.378077,-9.809315,5.416476,6.131992,-0.755935,5.607664,9.015963,-1.454663,-5.343608,8.701175,6.472133,0.320674,-7.383860,4.475195,-8.597226,0.917057,3.784599,0.066221,6.862404,8.276727,5.119852,5.187172,3.756969,5.740741,-7.831066,7.119176,-0.995293,9.064480,6.659036,-6.057751,-1.005088,-3.910454,3.896128,-0.747278,9.404597,-1.400477,3.310481,1.950575,5.692462,-7.716220,7.876651,9.951311,9.499314,-4.706925,1.946710,-5.862049,8.639766,-3.610074,-1.380425,7.106022,-9.207707,8.706047,6.003373,-3.819611,9.537991,-1.132871,-6.922845,-6.955566,8.892846,2.217375,7.844178,-5.317295,-4.213143,5.539446,-5.116805,-8.797578,7.673856,-6.823130,-5.162371,7.583380,9.254839,-9.578786,-8.005441,2.192439,-8.900719,-9.889877,-9.847968,-2.522304,9.624752,-6.536704,-2.501004,4.233966,-1.051657,9.740408,-4.791732,-1.269152,-5.288814,-5.676360,-8.478425,-7.200353,-7.174265,-0.313176,-4.731614,9.670483,6.893253,1.955832,5.745647,2.086194,-7.671057,-7.917658,8.026518,-1.597834,-5.206902,-7.699007,6.240878,4.012511,-0.749815,-5.479518,-2.966728,-8.487198,7.212353,8.671241,-9.196520,-6.658242,8.953186,-9.604614,-9.525971,3.234724,7.098459,5.755900,-7.763338,-8.937903,-5.866962,8.516867,-7.372682,-8.851775,4.581158,-8.225607,-8.301839,-6.918699,-8.854842], dtype = "float32")#candidate|7486|(624,)|const|float32
const_7487 = relay.const(6, dtype = "uint32")#candidate|7487|()|const|uint32
call_7484 = relay.TupleGetItem(func_4196_call(relay.reshape(const_7485.astype('uint8'), [2, 11, 15]), relay.reshape(const_7485.astype('uint8'), [2, 11, 15]), relay.reshape(const_7486.astype('float32'), [624,]), relay.reshape(const_7487.astype('uint32'), []), ), 5)
call_7488 = relay.TupleGetItem(func_4201_call(relay.reshape(const_7485.astype('uint8'), [2, 11, 15]), relay.reshape(const_7485.astype('uint8'), [2, 11, 15]), relay.reshape(const_7486.astype('float32'), [624,]), relay.reshape(const_7487.astype('uint32'), []), ), 5)
func_5730_call = mod.get_global_var('func_5730')
func_5732_call = mutated_mod.get_global_var('func_5732')
call_7490 = relay.TupleGetItem(func_5730_call(relay.reshape(call_7464.astype('float32'), [6, 30])), 0)
call_7491 = relay.TupleGetItem(func_5732_call(relay.reshape(call_7464.astype('float32'), [6, 30])), 0)
func_2614_call = mod.get_global_var('func_2614')
func_2618_call = mutated_mod.get_global_var('func_2618')
const_7495 = relay.const([8.224603,-1.859700,6.998083,-1.454155,-7.024260,-7.409736,1.629830,-8.916214,9.857469,8.761661,3.012020,3.129552,-2.072417,0.650846,-0.150962,1.302333,1.528545,7.462222,-3.210615,2.187398,7.109730,-2.576020,-6.267131,8.486258,8.751165,-6.337343,-5.196570,6.265650,3.092806,-0.681170,8.125431,1.503162,-7.242179,8.736948,-4.781913,4.550543,1.942274,-3.290510,9.350744,4.880846,-4.245975,7.190941,6.415316,-5.936212,5.717194,-7.163119,-7.764827,9.278760,-4.603231,7.564755,3.878829,3.231917,-1.407279,8.611794,9.291654,-7.550890,-4.971928,-6.764319,3.668213,-0.836749,4.608902,5.439513,-3.771892,-3.749530,-5.705877,7.346950,4.074960,-4.618917,-7.301978,4.577845,-6.220803,-4.719489,9.839753,-8.127142,5.735943,-5.745630,6.328622,-4.894608,-1.935770,9.044210], dtype = "float32")#candidate|7495|(80,)|const|float32
call_7494 = relay.TupleGetItem(func_2614_call(relay.reshape(const_7487.astype('float32'), []), relay.reshape(const_7495.astype('float32'), [5, 1, 16]), ), 0)
call_7496 = relay.TupleGetItem(func_2618_call(relay.reshape(const_7487.astype('float32'), []), relay.reshape(const_7495.astype('float32'), [5, 1, 16]), ), 0)
output = relay.Tuple([call_7459,call_7464,const_7465,call_7478,call_7484,const_7485,const_7486,const_7487,call_7490,call_7494,const_7495,])
output2 = relay.Tuple([call_7460,call_7466,const_7465,call_7479,call_7488,const_7485,const_7486,const_7487,call_7491,call_7496,const_7495,])
func_7497 = relay.Function([], output)
mod['func_7497'] = func_7497
mod = relay.transform.InferType()(mod)
mutated_mod['func_7497'] = func_7497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7497_call = mutated_mod.get_global_var('func_7497')
call_7498 = func_7497_call()
output = call_7498
func_7499 = relay.Function([], output)
mutated_mod['func_7499'] = func_7499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7239_call = mod.get_global_var('func_7239')
func_7240_call = mutated_mod.get_global_var('func_7240')
call_7503 = relay.TupleGetItem(func_7239_call(), 0)
call_7504 = relay.TupleGetItem(func_7240_call(), 0)
func_5490_call = mod.get_global_var('func_5490')
func_5493_call = mutated_mod.get_global_var('func_5493')
var_7509 = relay.var("var_7509", dtype = "uint64", shape = ())#candidate|7509|()|var|uint64
const_7510 = relay.const([True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,False,False,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True], dtype = "bool")#candidate|7510|(1120,)|const|bool
call_7508 = relay.TupleGetItem(func_5490_call(relay.reshape(var_7509.astype('uint64'), []), relay.reshape(const_7510.astype('bool'), [1120,]), ), 0)
call_7511 = relay.TupleGetItem(func_5493_call(relay.reshape(var_7509.astype('uint64'), []), relay.reshape(const_7510.astype('bool'), [1120,]), ), 0)
func_7051_call = mod.get_global_var('func_7051')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_7512 = func_7051_call()
call_7513 = func_7051_call()
func_1061_call = mod.get_global_var('func_1061')
func_1063_call = mutated_mod.get_global_var('func_1063')
var_7524 = relay.var("var_7524", dtype = "float32", shape = (180,))#candidate|7524|(180,)|var|float32
call_7523 = relay.TupleGetItem(func_1061_call(relay.reshape(var_7524.astype('float32'), [4, 9, 5])), 0)
call_7525 = relay.TupleGetItem(func_1063_call(relay.reshape(var_7524.astype('float32'), [4, 9, 5])), 0)
func_2846_call = mod.get_global_var('func_2846')
func_2848_call = mutated_mod.get_global_var('func_2848')
const_7548 = relay.const([6,-7,7,-9,-4,7,-7,1,3,-2,6,-7,-5,-7,9,-2,-3,1,8,8,-10,10,-10,-3,-6,-9,2,-5,2,-8,5,3,1,-9,-6,3,-3,-5,-3,-8,-3,9,1,-2,9,4,-4,-3,5,-3,8,6,8,-6,10,-10,-1,8,-5,6,4,10,-7,2,3,-2,1,4,-1,-10,2,-4,9,6,-6,-9,-10,-8,-2,-8,6,-7,8,-8,-10,2,6,-7,-9,10,3], dtype = "int16")#candidate|7548|(91,)|const|int16
call_7547 = func_2846_call(relay.reshape(const_7548.astype('int16'), [13, 7, 1]))
call_7549 = func_2846_call(relay.reshape(const_7548.astype('int16'), [13, 7, 1]))
uop_7550 = relay.exp(call_7523.astype('float64')) # shape=(4, 9, 5)
uop_7552 = relay.exp(call_7525.astype('float64')) # shape=(4, 9, 5)
output = relay.Tuple([call_7503,call_7508,var_7509,const_7510,call_7512,var_7524,call_7547,const_7548,uop_7550,])
output2 = relay.Tuple([call_7504,call_7511,var_7509,const_7510,call_7513,var_7524,call_7549,const_7548,uop_7552,])
func_7554 = relay.Function([var_7509,var_7524,], output)
mod['func_7554'] = func_7554
mod = relay.transform.InferType()(mod)
mutated_mod['func_7554'] = func_7554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7554_call = mutated_mod.get_global_var('func_7554')
var_7556 = relay.var("var_7556", dtype = "uint64", shape = ())#candidate|7556|()|var|uint64
var_7557 = relay.var("var_7557", dtype = "float32", shape = (180,))#candidate|7557|(180,)|var|float32
call_7555 = func_7554_call(var_7556,var_7557,)
output = call_7555
func_7558 = relay.Function([var_7556,var_7557,], output)
mutated_mod['func_7558'] = func_7558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_7606 = relay.TupleGetItem(func_5104_call(), 0)
call_7607 = relay.TupleGetItem(func_5106_call(), 0)
output = call_7606
output2 = call_7607
func_7618 = relay.Function([], output)
mod['func_7618'] = func_7618
mod = relay.transform.InferType()(mod)
mutated_mod['func_7618'] = func_7618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7618_call = mutated_mod.get_global_var('func_7618')
call_7619 = func_7618_call()
output = call_7619
func_7620 = relay.Function([], output)
mutated_mod['func_7620'] = func_7620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_7633 = relay.TupleGetItem(func_5509_call(), 1)
call_7634 = relay.TupleGetItem(func_5511_call(), 1)
func_7618_call = mod.get_global_var('func_7618')
func_7620_call = mutated_mod.get_global_var('func_7620')
call_7644 = func_7618_call()
call_7645 = func_7618_call()
output = relay.Tuple([call_7633,call_7644,])
output2 = relay.Tuple([call_7634,call_7645,])
func_7646 = relay.Function([], output)
mod['func_7646'] = func_7646
mod = relay.transform.InferType()(mod)
output = func_7646()
func_7647 = relay.Function([], output)
mutated_mod['func_7647'] = func_7647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7497_call = mod.get_global_var('func_7497')
func_7499_call = mutated_mod.get_global_var('func_7499')
call_7686 = relay.TupleGetItem(func_7497_call(), 3)
call_7687 = relay.TupleGetItem(func_7499_call(), 3)
func_7132_call = mod.get_global_var('func_7132')
func_7138_call = mutated_mod.get_global_var('func_7138')
const_7689 = relay.const([-1,4,-6,4,9,3,6,-2,5,10,10,-10,-6,10,9,10,-8,9,-9,8,-7,-1,-8,8,9,-5,-7,-10,9,9,-1,-7,5,5,-8,-3,-5,-10,9,6,-5,-9,-7,5,8,3,3,10,-5,6,-9,10,5,-9,-5,-4,-8,-3,1,3,2,-9,-6,-4,8,-4,-1,5,4,10,-10,10,-7,-5,10,6,-3,-8,-7,-10,4,-4,-10,-9,-10,4,5,-10,-6,1,-2,-8,3,4,8,-7,-7,5,7,-4,7,8,1,-4,-4,10,3,1,-4,8,-8,-4,5,4,5,10,5,4,8,2,-5,10,-10,4,5,-6,6,-9,9,-2,1,-8,1,-2,-2,-3,-7,-2,5,3,-9,-4,-10,7,-6,6,2,6,8,2,-4,-6,9,10,-6,-3,-3,-2,-8,4,8,1,-6,3,5,-3,-2,10,8,5,-6,-1,-5,-3,9,-7,9,-9,7,10,-9,2,3,5,3,-7,8,7,-10,6,-10,-6,-3,6,7,1,-1,7,7,9,-2,9,4,-3,10,4,2,-9,-5,6,-2,-7,-2,-1,8,8,-6,-10,-7,-5,-10,-7,8,-1,2,4,4,9,8,2,-9,6,9,6,-8,-3,9,-5,5,-2,1,2,-9,-1,2,5,-6,-5,-8,3,3,6,-5,8,7,8,6,-3,-1,-4,-10,4,-1,-4,-1,6,-2,-3,5,8,3,-10,-4,-6,9,-7,10,-8,-10,1,-9,5,-3,-10,-2,-10,2,6,5,10,1,-7,-1,-1,7,-2,2,10,8,4,8,-6,6,-6,-1,8,-8,-2,-10,-1,6,-5,-3,-4,5,-10,1,-5,6,-9,10,1,-2,8,-8,1,2,-4,1,3,-5,-10,7,-3,-7,-1,2,6,7,-8,-10,-10,-2,-5,-2,8,-1,4,-4,-2,3,-9,-5,1,-8,8,-5,-10,5,-10,4,-8,8,5,-1,6,-10,1,9,-9,8,-5,-8,-9,-10,3,9,-1,3,3,-2,-10,-4,-10,-2,10,-8,2,-9,2,2,-3,7,9,1,8,1,-8,8,7,-10,-1,-1,-6,-5,-2,-6,-7,-1,6,8,-5,-1,-1,-2,-10,-7,-1,-1,-1,-7,-3,-7,9,7,-8,-9,-4,-6,9,5,-10,-8,1,8,-8,-4,-2,-1,7,-6,5,-9,-4,-5,-3,-10,-5,4,10,7,-8,8,1,9,-9,4,10,4,8,-7,-2,-6,7,-2,-1,-6,-1,9,6,-2,4,-1,-1,8,-4,4,4,-2,9,10,4,-1,2,9,-7,-5,8,3,10,-1,-6,2,-5,3,-2,-4,-10,-1,4,-10,-2,-1,-2,-2,-8,9,-7,6,-9,6,3,-8,-6,7,1,-10,-4,-5,-7,-9,7,-1,-2,8,7,3,-5,-4,9,8,1,-5,9,3,5,1,1,8,-8,-5,10,6,8,-6,-3,9,4,-1,3,1,6,-10,3,-2,-6,-5,-6,4,10,3,8,-9,5,7,4,6,9,6,-5,4,-5,10,1,7,5,7,1,6,-6,4,1,9,-7,6,5,-3,-1,4,-8,5,1,7,-10,8,3,7,3,6,4,1,-1,2,9,6,-8,-1,5,-9,-8,-2,-8,-7,-8,10,-6,-3,-7,-1,-2,-6,-5,7,4,6,2,6,-6,2,7,-6,-5,2,-4,10,7,6,2,4,1,1,6,7,10,8,5,2,4,4,4,-6,10,3,-7,-2,-6,4,-10,-6,10,10,7,-5,-6,9,-3,-1,6,8,2,2,5,-10,6,-5,-9,2,-9,-8,-8,-4,-1,7,-10,3,-7,10,10,6,5,2,6,-1,-5,-9,6,-5,10,-6,-6,-4,3,-4,-3,9,-2,3,9,5,1,-4,-9,5,10,10,2,1,-10,-10,-5,-1,4,-7,8,-4,5,-5,8,4,3,3,9,-5,-9,2,-6,1,8,4,9,4,-7,-10,1,10,-9,-1,7,9,-1,-9,5,8,7,9,9,2,2,-8,8,-7,10,-9,-2,-2,1,-9,-3,-2,-8,-8,6,-10,4,1,7,-10,6,6,8,-2,-1,-5,-9,-5,-2,5,-5,-6,4,-10,9,-7,-9,-4,3,6,-8,-8,-2,5,8,-1,4,1,-7,6,2,3,-6,-10,5,-5,-1,-2,-8,6,-7,-8,-4,-1,-1,-9,2,-8,-10,-9,6,-10,7,-9,-8,-10,2,10,-6,-9,7,1,1,-8,-8,6,1,1,7,-2,7,-4,7,-4,-2,-9,4,-8,9,-6,5,1,7,3,-3,10,4], dtype = "int8")#candidate|7689|(864,)|const|int8
var_7690 = relay.var("var_7690", dtype = "int64", shape = (1, 630))#candidate|7690|(1, 630)|var|int64
var_7691 = relay.var("var_7691", dtype = "bool", shape = (1120,))#candidate|7691|(1120,)|var|bool
var_7692 = relay.var("var_7692", dtype = "float32", shape = (180,))#candidate|7692|(180,)|var|float32
call_7688 = relay.TupleGetItem(func_7132_call(relay.reshape(const_7689.astype('int8'), [8, 9, 12]), relay.reshape(var_7690.astype('int64'), [630,]), relay.reshape(var_7691.astype('bool'), [1, 1120]), relay.reshape(var_7692.astype('float32'), [180,]), ), 0)
call_7693 = relay.TupleGetItem(func_7138_call(relay.reshape(const_7689.astype('int8'), [8, 9, 12]), relay.reshape(var_7690.astype('int64'), [630,]), relay.reshape(var_7691.astype('bool'), [1, 1120]), relay.reshape(var_7692.astype('float32'), [180,]), ), 0)
output = relay.Tuple([call_7686,call_7688,const_7689,var_7690,var_7691,var_7692,])
output2 = relay.Tuple([call_7687,call_7693,const_7689,var_7690,var_7691,var_7692,])
func_7704 = relay.Function([var_7690,var_7691,var_7692,], output)
mod['func_7704'] = func_7704
mod = relay.transform.InferType()(mod)
var_7705 = relay.var("var_7705", dtype = "int64", shape = (1, 630))#candidate|7705|(1, 630)|var|int64
var_7706 = relay.var("var_7706", dtype = "bool", shape = (1120,))#candidate|7706|(1120,)|var|bool
var_7707 = relay.var("var_7707", dtype = "float32", shape = (180,))#candidate|7707|(180,)|var|float32
output = func_7704(var_7705,var_7706,var_7707,)
func_7708 = relay.Function([var_7705,var_7706,var_7707,], output)
mutated_mod['func_7708'] = func_7708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6365_call = mod.get_global_var('func_6365')
func_6367_call = mutated_mod.get_global_var('func_6367')
call_7751 = func_6365_call()
call_7752 = func_6365_call()
func_2996_call = mod.get_global_var('func_2996')
func_2999_call = mutated_mod.get_global_var('func_2999')
var_7756 = relay.var("var_7756", dtype = "bool", shape = (720,))#candidate|7756|(720,)|var|bool
call_7755 = relay.TupleGetItem(func_2996_call(relay.reshape(var_7756.astype('bool'), [9, 16, 5])), 0)
call_7757 = relay.TupleGetItem(func_2999_call(relay.reshape(var_7756.astype('bool'), [9, 16, 5])), 0)
output = relay.Tuple([call_7751,call_7755,var_7756,])
output2 = relay.Tuple([call_7752,call_7757,var_7756,])
func_7766 = relay.Function([var_7756,], output)
mod['func_7766'] = func_7766
mod = relay.transform.InferType()(mod)
var_7767 = relay.var("var_7767", dtype = "bool", shape = (720,))#candidate|7767|(720,)|var|bool
output = func_7766(var_7767)
func_7768 = relay.Function([var_7767], output)
mutated_mod['func_7768'] = func_7768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6611_call = mod.get_global_var('func_6611')
func_6612_call = mutated_mod.get_global_var('func_6612')
call_7778 = relay.TupleGetItem(func_6611_call(), 0)
call_7779 = relay.TupleGetItem(func_6612_call(), 0)
func_6365_call = mod.get_global_var('func_6365')
func_6367_call = mutated_mod.get_global_var('func_6367')
call_7784 = func_6365_call()
call_7785 = func_6365_call()
output = relay.Tuple([call_7778,call_7784,])
output2 = relay.Tuple([call_7779,call_7785,])
func_7786 = relay.Function([], output)
mod['func_7786'] = func_7786
mod = relay.transform.InferType()(mod)
mutated_mod['func_7786'] = func_7786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7786_call = mutated_mod.get_global_var('func_7786')
call_7787 = func_7786_call()
output = call_7787
func_7788 = relay.Function([], output)
mutated_mod['func_7788'] = func_7788
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7789 = relay.var("var_7789", dtype = "float32", shape = (13, 1, 3))#candidate|7789|(13, 1, 3)|var|float32
uop_7790 = relay.acosh(var_7789.astype('float32')) # shape=(13, 1, 3)
output = relay.Tuple([uop_7790,])
output2 = relay.Tuple([uop_7790,])
func_7792 = relay.Function([var_7789,], output)
mod['func_7792'] = func_7792
mod = relay.transform.InferType()(mod)
var_7793 = relay.var("var_7793", dtype = "float32", shape = (13, 1, 3))#candidate|7793|(13, 1, 3)|var|float32
output = func_7792(var_7793)
func_7794 = relay.Function([var_7793], output)
mutated_mod['func_7794'] = func_7794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7497_call = mod.get_global_var('func_7497')
func_7499_call = mutated_mod.get_global_var('func_7499')
call_7796 = relay.TupleGetItem(func_7497_call(), 3)
call_7797 = relay.TupleGetItem(func_7499_call(), 3)
const_7837 = relay.const([[[1.660551,-2.409951,8.306874,-5.802519,6.830459,-2.393803,-6.441727,-9.244825,-3.288594,-6.125795,0.388923,6.493680,8.353684,-9.302103,-0.169734],[6.546474,9.742480,-9.764646,-2.719587,-0.730406,1.302748,-0.153306,-8.131022,-0.882789,7.892710,-1.125320,2.599455,-6.986279,-8.435972,8.114414],[2.178897,-7.822777,-3.913460,8.955812,5.265174,-9.761827,8.100027,6.969327,9.035218,-2.357942,-2.521963,-9.499291,7.583222,9.447878,3.596330],[-2.548395,9.685732,4.570665,-2.224574,2.370251,-3.547175,-4.863443,-8.213087,-0.912705,4.914304,-0.322217,2.511150,6.646089,4.830726,-0.157072],[0.322948,1.875452,-9.533375,-4.320601,-2.472454,-7.213481,9.497104,-3.417162,-7.827801,-0.489848,4.621189,-4.519433,9.474497,6.922712,-5.657328],[8.482731,5.002216,-4.017557,5.494616,-8.419383,-6.002984,-1.789718,6.842381,7.702403,0.509241,-9.409826,-9.072331,-7.069333,-0.985078,4.120082],[3.976262,9.414561,6.869414,-9.334122,-6.870310,-6.677074,-0.053384,8.718365,2.718786,6.268761,-1.105391,-3.251088,-5.977588,-4.585931,-9.617393],[1.878731,-4.338539,-7.513330,2.400162,-4.644468,0.635589,-6.919165,6.677748,-9.615474,0.222220,-6.286318,4.630603,-1.119363,9.164614,-3.755163]],[[-8.866429,9.986557,-2.245869,1.192951,0.046515,-2.444752,-6.876529,-8.943850,-8.984356,6.996551,-6.416984,7.645512,-2.592616,-7.491351,-4.698723],[3.092647,-4.100435,6.001718,0.503858,-9.286776,-1.988248,5.175259,-6.809126,-6.007940,-5.832397,-0.383538,4.918987,-8.115054,3.982430,5.539861],[-2.557614,7.185267,-9.375631,1.733324,9.952478,-9.027694,-6.740219,-3.619436,7.128103,2.835846,-6.992371,-3.786534,5.134932,5.413297,3.046499],[-7.465668,-1.747564,4.611570,-8.294835,-9.643706,-8.451889,5.121366,-5.852270,0.944905,0.862977,-4.316288,-4.636331,8.225056,9.412469,3.563531],[-2.280069,-0.699137,7.895533,4.615374,0.871791,7.932258,-0.125301,-7.841438,-0.603073,-4.984204,8.914812,-5.101858,8.500788,5.287100,-9.797389],[-5.590812,5.555182,1.872759,-8.528321,-5.581700,-5.501199,1.557313,0.057044,-0.383548,-7.174835,5.043411,7.754860,1.606083,4.395934,8.392901],[0.945308,-3.453758,4.561623,7.798140,-4.487204,6.631900,4.806243,0.776041,-2.888171,8.916879,-2.245450,-7.990308,-0.076734,2.836494,7.733729],[1.352083,-2.799829,3.830882,-7.421874,2.279282,-0.157887,3.104105,1.592745,-3.297601,-5.534116,-4.086662,-0.134315,-8.076729,7.801517,6.368045]],[[5.100594,5.862607,-9.487402,4.775326,-9.995111,-8.459909,9.252794,-0.353370,-9.851772,-2.185528,-7.678543,-8.045511,-7.898657,8.244069,-0.352784],[-1.463414,-2.720438,6.656897,-3.779306,9.881327,0.563228,9.676545,8.003685,2.805460,6.434233,2.715314,6.632696,-3.818296,-1.404784,5.840178],[-4.291807,-9.200725,8.194399,-5.161926,-8.536559,-8.334324,9.930823,-3.792641,-8.404101,-7.173361,-0.756292,9.030268,3.531238,9.021986,-6.299957],[-0.231196,-9.893691,4.898662,-9.124994,0.471137,4.878742,-8.780351,6.371702,7.256872,7.762397,2.070114,0.868829,5.453823,8.417385,3.297338],[6.201296,-2.577263,-6.487270,0.672930,3.679807,-4.958653,9.587703,5.329259,1.909494,-9.458894,9.856737,-1.737051,-9.520650,1.479043,-3.914154],[4.743917,1.996808,4.815637,6.169076,-7.853908,7.181774,8.938270,-2.666303,-3.095934,-6.923706,-8.004184,-5.923215,-1.668133,-5.201799,-5.199006],[-3.973969,-7.884137,-0.821918,-9.141666,-1.747101,-9.018873,4.845445,-2.688011,0.523990,5.881929,9.456041,9.283971,3.786612,3.304023,9.993359],[-0.792862,2.366256,8.927292,4.368126,-3.577577,9.139426,2.684800,-5.450616,-9.410772,-0.302600,2.368285,7.695023,-7.632717,5.645236,-5.669333]],[[0.414079,-7.581548,0.418643,-5.066512,5.363177,-6.246457,-9.442883,7.342548,-2.752572,-9.365631,-8.200477,-6.877266,-5.358308,-1.996636,-2.133287],[-1.182839,3.827993,8.160402,4.710611,3.241637,-5.370076,0.376166,-2.076122,9.039896,-0.870022,5.113772,-6.351419,-9.104446,-0.137218,-9.669547],[1.955572,2.401455,5.560662,7.747010,-4.850835,-0.324210,-3.317939,2.033155,-3.202946,7.486445,-1.058215,4.189758,8.026227,8.821966,-4.629446],[-2.921173,1.946272,2.123486,-3.143026,4.026625,4.362346,4.576750,7.375733,-9.493582,-4.844940,-3.884018,2.758518,1.049782,0.755561,-1.638777],[-6.893848,9.977924,-2.070528,-1.117644,9.629186,-2.791792,0.751633,-2.996330,-4.292697,0.805346,1.167498,-7.781841,4.197946,9.307141,-6.816617],[8.186584,-4.363794,-4.901500,1.856253,-8.909045,-1.209200,1.307102,-5.373257,-9.784147,0.016024,7.127116,9.697517,3.854517,1.427085,3.179290],[-4.203841,-7.875559,9.267944,-5.812929,-2.284155,1.862689,5.786328,-0.646688,0.645064,-3.536896,-2.481908,6.816411,1.064503,8.137642,3.791163],[9.325046,3.315103,-1.021854,-9.026791,6.248555,4.339735,-3.901175,3.246311,9.931455,0.149297,8.388599,6.186173,-7.009042,0.698188,-8.867867]],[[-5.166128,1.125024,2.594450,8.890064,-7.465103,-7.885897,4.138661,-3.542064,-6.342823,7.736261,8.925530,0.673327,3.085103,-6.085411,9.708709],[5.660012,-0.743253,6.882322,7.541857,0.338391,7.157964,1.882350,-2.914221,-6.535410,1.336993,3.751490,-4.303312,-1.878210,-1.454047,7.373897],[3.683062,9.216636,1.424420,1.382239,9.490489,-8.302393,8.111450,-1.209258,4.256283,-1.829996,-1.461800,8.954730,-3.597216,5.782382,-1.169027],[2.688937,0.278491,3.309010,8.820527,0.417776,-4.387592,-0.909711,-8.296103,7.815322,3.008839,-4.534772,5.324507,-7.785513,5.749784,-6.566905],[-2.515372,8.449876,6.065941,-4.046464,-9.526090,9.773991,9.250766,-6.056928,-4.307515,6.917291,2.464809,-2.571773,-0.493907,-0.860319,-3.435421],[1.885605,-4.682648,-3.720894,-3.885884,8.059205,3.335682,9.010886,-4.734269,-5.941462,4.776336,-2.944001,8.250036,-6.709091,2.841341,-2.017944],[1.248372,0.958814,-4.688063,7.213091,-6.593643,8.451737,-5.858727,3.993490,-9.585534,2.087686,5.759304,-2.068426,-0.948174,-6.891032,-2.680510],[5.660888,0.628486,0.668256,8.671474,-6.379127,1.030209,1.930631,-1.668071,-5.218809,-3.295892,-0.284566,5.151472,-7.349111,2.565027,-2.606435]],[[3.622743,-5.185807,-7.940868,3.024146,-5.096878,6.155721,4.704189,8.431317,4.744532,5.625023,-3.172886,-8.249793,-4.965260,0.998230,1.415612],[4.132729,-3.546046,6.434546,-5.898120,-3.990318,-6.794246,-4.366334,-8.327587,4.576984,-7.975054,8.874585,2.098986,-8.863849,-4.353555,6.535581],[1.049368,6.498617,-2.757234,-5.794497,9.437712,-2.246854,6.050919,5.933282,-0.316956,9.363837,8.514023,7.946153,-0.579428,0.895695,-8.304111],[7.578797,8.759953,8.090987,8.014816,-5.624168,-8.756317,7.807569,-5.131921,6.050606,0.576974,5.813432,9.897172,7.139873,-2.673603,-9.044885],[-8.632314,8.672597,-9.754996,4.855519,-9.522732,-5.666188,-7.405622,-2.365045,4.480043,-1.961795,7.280424,3.357331,-6.813464,-0.567399,9.721138],[4.169556,-8.407135,-0.755761,0.189062,1.995436,0.359471,-4.928199,1.646003,-7.909522,-7.137503,6.078216,-0.908493,-9.862428,-0.370771,-0.351590],[-5.565261,3.734524,-2.460031,2.787711,8.065694,6.517735,7.719334,7.820128,1.640400,6.286493,-1.552729,6.818526,6.083315,8.294520,-1.725351],[-9.882442,-6.184486,-1.826593,3.925116,-2.833388,-2.366711,9.995470,-9.979452,-2.800134,9.012249,6.508916,-5.951812,-4.895765,3.370315,1.230122]],[[7.999305,-4.254695,3.282213,-8.122989,-4.354921,-8.009859,7.727295,-4.065290,-7.329406,2.971246,-6.128370,1.008458,6.649491,8.859135,5.045047],[-2.756880,-1.486946,-2.278238,6.346092,-0.320577,-5.441750,-0.947959,-6.506812,3.230928,5.881335,-2.259771,0.003434,4.164193,-4.977446,9.983897],[2.809930,-7.416570,-2.953684,-3.825594,-5.157959,-6.004261,7.002585,-7.349603,0.908943,-0.685393,-6.088115,3.666932,-1.406075,-3.890279,8.111834],[-0.734584,7.057965,-3.949957,-0.688649,-8.627468,7.832720,3.663164,3.957529,-6.361581,7.710403,-9.645600,-9.722780,5.211508,-2.967949,0.798866],[-0.348722,-7.850100,-1.611232,7.394356,8.789324,5.473920,-4.509895,5.233887,-7.548046,9.749430,-3.086556,7.637728,6.394009,2.371945,-3.003190],[2.451802,3.197453,2.554559,-7.941890,-5.407847,-1.182108,-7.191364,-6.459440,-6.361915,0.455825,-8.677054,3.155938,-0.989474,-7.634237,-5.428109],[-9.672833,1.741151,-8.987954,-5.585744,-8.646065,-3.889412,-4.830548,4.866715,8.059005,-8.777108,8.172143,-2.918338,-8.217938,5.274898,5.819522],[-5.155438,5.518140,6.680375,-7.615270,-5.904432,-9.436846,8.268255,8.569486,8.146330,-0.556713,-4.032260,-3.710301,6.733259,3.859551,9.088635]],[[-5.554617,1.562929,-7.872119,3.576177,-4.731646,3.402967,9.905819,1.120536,4.676993,2.133721,-4.954101,-9.805139,-5.045435,-3.027781,-8.116958],[-2.156299,8.706854,8.035695,-8.686071,-4.351304,-6.704251,7.386918,-3.680875,5.818986,1.052099,0.526930,-1.340283,-2.301649,9.201015,-2.943170],[5.961948,7.333324,-0.767080,-0.149066,8.190226,6.142883,-7.937716,4.307854,-4.279266,-7.055973,6.783245,1.746491,9.684049,2.674779,-9.638063],[9.238005,-0.147344,-4.168536,8.071564,-8.904809,0.467852,-2.467622,-8.791994,-3.280621,-5.151742,0.226754,8.260620,6.795774,-1.326279,6.389192],[2.985114,-6.722484,5.587818,-4.330746,0.780670,-8.358477,1.458262,-1.180173,-8.322734,-7.962680,-8.616859,1.569465,-7.935674,-0.745179,4.006857],[-8.305082,-7.269425,-2.282678,7.714434,-8.075271,1.629925,-8.310427,-4.252335,6.371071,3.380945,7.159650,3.506365,4.590862,-7.236595,-1.612914],[-7.170969,-9.924755,-9.250457,-8.131946,4.524663,-8.017450,5.399161,8.763236,-6.447684,6.512900,-5.616470,6.920693,4.896599,-6.120051,-2.578991],[4.217603,0.389515,-9.639753,-3.450358,6.736961,2.037287,0.467587,-0.080980,-6.417945,1.533477,0.293961,9.422956,5.492619,6.522484,-3.753447]],[[-9.600716,-2.640380,4.431077,5.898711,-7.658418,4.812861,6.674887,-8.917720,-3.074841,-7.065505,-5.960748,0.155828,-7.931529,-5.815616,-2.290245],[0.436967,-6.786451,-9.969245,-7.550182,-2.013756,6.467678,8.041064,-8.980702,-6.333651,-6.411665,-6.587517,-0.105996,-5.562592,-5.205330,1.872672],[5.145706,7.242142,-1.664396,9.596067,-4.424028,1.431238,-5.888008,-1.171205,8.527118,7.440196,3.787110,-3.227464,9.705770,-6.161068,-3.570141],[2.651229,-8.218478,8.770277,-4.110752,-4.682938,-9.710021,-6.107983,-4.867127,4.284369,-3.615799,2.201383,-5.217309,6.685047,0.231948,7.574479],[9.492044,5.501128,-7.261372,4.415296,-8.165741,0.266887,8.287999,1.470235,-4.210103,3.465414,6.787727,-9.719753,0.785311,4.572156,5.208062],[-3.926093,3.293518,-9.730472,-2.920789,3.274995,3.262093,-7.060350,-0.773763,-1.409460,-6.146976,3.273542,5.806743,-9.804867,-4.865258,9.499094],[-0.937709,-5.808550,4.642785,2.887319,-1.400657,-9.804861,6.799838,6.396882,-5.344018,-1.885241,3.875854,-3.121486,3.671398,0.848234,6.406677],[7.143164,-0.477173,9.188441,9.030834,-9.383546,1.332450,1.923432,7.988614,6.410693,2.462492,-1.482403,9.409675,8.237333,8.778473,-2.311187]],[[7.534595,0.451152,-3.210964,3.079394,4.567119,7.401950,0.048555,-3.712609,4.655684,-4.294230,3.442183,-7.965412,-4.984818,-7.900669,-3.269786],[-5.211986,-0.454387,-5.215133,-2.545419,-8.231558,9.818001,6.481534,3.679976,2.899808,9.384195,5.562536,-1.023537,0.446057,4.758280,9.872698],[1.065621,6.814960,7.116723,-9.340620,7.185849,4.060362,-8.336143,4.846691,-8.208584,5.251460,3.506736,3.937207,-1.740604,-5.927992,-2.044186],[6.131920,4.216065,0.164812,-2.374834,-3.713379,7.737351,-8.534624,-3.399043,1.241639,-4.200952,-7.522769,1.645327,-8.460290,4.067313,6.068540],[-4.323503,6.971535,4.380888,-0.421733,-9.852783,5.609207,-8.325635,1.460233,-2.339727,-0.044021,5.350084,-4.272089,-2.129188,-0.643124,2.754013],[0.276459,4.087804,8.324842,9.797291,-9.084801,-3.668749,0.299382,-6.347097,-3.838769,8.953555,3.189739,1.193678,5.173997,-9.451718,9.557304],[4.401270,7.709511,2.129669,8.487122,-3.630977,-3.557687,-8.234239,-6.674123,2.762487,4.185533,8.729231,6.295469,-7.591229,-6.653678,2.207735],[-3.065454,-3.400197,9.167023,-0.052785,-9.859402,-6.247427,3.950005,4.671310,4.448874,-7.716069,5.210096,-9.531071,9.289535,-5.267267,3.615906]],[[6.417263,-7.126777,-1.830393,-0.144295,6.861367,3.539081,3.644078,-7.980042,-4.077389,6.521267,-6.793516,-4.272474,-5.379123,6.303807,6.275035],[-7.874436,-2.565925,-9.754332,-9.373244,4.244269,-0.904068,4.089060,2.804933,-3.405870,-1.295278,9.941475,-6.734158,3.873988,5.942722,7.495921],[2.017095,6.230295,2.758688,-6.335875,-3.431815,3.900427,1.951904,9.940795,-7.986079,-1.673576,1.464764,8.226157,-2.847470,-4.520733,3.798329],[-1.505976,4.981474,-7.887423,-7.912983,-6.193870,-4.958764,4.078803,2.925229,-3.798240,-8.166289,-5.777504,-8.744470,2.615697,-5.510251,-2.660006],[-8.356387,-6.700034,0.956075,-7.633259,-1.083774,-1.540851,-0.881048,-0.392233,-8.735596,6.683967,2.944329,8.343025,5.772265,-4.530886,-4.584002],[1.781574,-3.701812,1.024540,-7.939259,9.941953,-9.219454,7.300137,4.412278,-1.731990,-6.982712,-8.339333,8.655783,-4.940088,-2.666511,-2.180772],[2.169514,7.425922,-7.184518,6.352602,-3.575148,9.970149,0.254732,6.837635,-6.242978,-8.307539,8.523757,-8.420218,-1.806446,5.282394,-3.059277],[-9.171827,2.882686,5.546237,-7.690056,-5.085668,4.831591,3.270974,-4.177367,2.466116,2.943355,-7.668217,-4.029999,5.663903,5.151725,5.531214]],[[1.877050,6.270689,-5.382550,-0.991316,-5.447425,4.064875,-8.611837,-0.912030,-6.455933,8.708101,9.634789,-7.098363,-0.180061,1.800073,8.479308],[4.801155,-5.431184,9.035530,2.927346,1.256867,6.353430,2.814565,1.113648,-1.802564,0.971286,8.823962,1.882801,-8.757711,-1.232734,8.226207],[3.444472,-0.766348,-7.105818,-6.879217,6.471410,9.446446,-3.342717,-1.275280,-3.709880,5.184200,-2.614888,-5.455839,8.771824,3.541473,-7.534889],[8.981468,-3.590481,6.571699,3.684694,-8.478720,4.171807,2.454161,7.901626,-6.266367,4.717492,6.994879,-8.816597,1.784906,6.028386,9.158529],[-0.746562,6.925210,-2.168375,1.221892,-4.157519,-0.566564,4.306064,7.560106,7.855559,-6.972013,-8.980951,-3.513936,3.051399,-3.544546,9.350804],[1.033129,-4.985358,-0.408268,0.947120,-3.435556,5.206193,-1.983987,5.977852,8.975518,7.806110,1.142518,-8.446604,-5.663871,9.256702,-0.580858],[6.882771,-0.344060,-0.202090,-3.882170,-8.402278,1.113199,-0.272251,-4.839543,0.076900,-4.423590,7.347931,-2.476932,-4.379704,-9.425057,3.162098],[-9.307251,-3.289622,-2.094954,5.460992,-2.766182,-5.677845,4.699093,7.858614,-3.857108,-7.699352,3.208374,-8.515033,3.557053,9.915205,-9.312428]],[[-1.188543,0.309913,-4.171725,1.690039,-5.123599,1.812210,7.245555,9.931797,8.721517,4.139295,0.125501,2.048034,2.440840,-4.216883,-8.901825],[9.917351,7.672121,8.813627,9.158123,3.910647,8.279604,-1.706279,9.666081,6.138534,2.159673,-1.259694,-8.436702,-7.584386,-0.340224,-7.695523],[9.932450,3.576802,-3.308569,-6.138719,8.293862,6.878868,6.345055,6.254618,-7.636507,1.179987,-9.044692,-9.298763,3.822945,-5.118050,9.160793],[1.371974,-7.466213,9.062655,4.232695,-9.267328,8.115330,0.421829,7.746339,3.381392,-7.835437,5.723738,1.484632,9.755191,-5.715996,-9.978040],[-9.801249,4.204110,0.590790,6.296803,-0.424886,6.746961,0.093782,-3.712212,-1.019371,-4.207741,-3.369215,5.461731,8.126539,3.933097,-8.061086],[2.917534,8.769411,8.222015,9.965367,0.530753,0.327113,5.573804,-5.697265,5.526737,-7.323080,7.660698,-2.582081,-8.297394,1.866292,4.899774],[2.651511,-7.829719,6.021616,0.590946,-1.911766,0.528499,-3.489377,-8.681384,-8.922833,9.332263,-6.518425,-9.238880,9.569339,-9.388042,-8.295726],[-1.975568,6.139545,-2.809918,-2.077255,0.363851,-8.113750,-7.985648,-7.209029,1.979408,0.159785,0.336725,8.883839,-6.127688,-1.321729,4.583077]],[[-0.095372,-7.183165,-5.485299,0.391963,1.953100,4.062672,3.267010,-8.861181,0.058742,-3.155354,-1.739086,-4.568792,4.066323,-1.618209,5.772487],[-7.635147,2.763638,9.978412,6.099639,-8.915153,-7.383176,3.983735,-0.821124,7.678771,4.435656,-9.126562,0.715047,-1.257579,3.605412,-3.313571],[-2.124566,-1.586526,6.269442,-8.143552,-5.484965,8.892883,-4.986732,-9.667290,-7.344502,-4.158554,-9.332755,1.350760,3.049216,-1.726962,-6.157904],[-9.251039,-4.252882,-4.605348,-8.464643,-8.786972,-4.982765,4.801007,-6.515357,0.619123,3.842678,2.060171,-4.239273,9.091868,-9.455989,-2.216171],[-1.927185,2.704516,1.505823,2.062312,-3.117526,0.839097,0.434371,-9.547966,-2.544561,0.600958,7.506915,8.113486,9.956718,-1.977581,0.581345],[1.207722,9.629299,-1.773799,-4.945722,-8.357524,9.574731,4.560957,5.130777,2.828419,4.328752,2.008126,8.861035,-3.881997,-0.984071,-4.153134],[5.626944,3.391275,-4.031217,-8.064574,1.909953,-6.377393,-7.634268,-3.905395,1.543689,0.351065,-8.135244,5.628673,-5.287160,-3.396493,-5.934745],[-4.913666,-4.146870,-7.568976,4.323606,-9.530379,-9.788321,1.129362,-8.676773,-1.786823,9.782459,6.787287,-8.477756,4.947650,-8.864988,6.701139]],[[-6.205772,2.295731,-5.798661,-9.924951,-9.386657,-3.602086,2.149390,3.924535,1.622512,4.087303,9.355810,-8.877674,9.669070,-6.287051,-3.991006],[1.249805,5.136371,5.039469,-2.715603,5.109395,-6.271435,4.489903,-2.073554,-4.938952,-3.253554,-2.403749,-3.311243,-4.321414,5.403349,3.542861],[-6.791625,-2.946486,9.828347,8.985437,2.703007,-1.424308,1.505978,0.957257,-5.663141,7.863412,5.319040,3.433238,2.880835,-0.160869,-6.413052],[-3.203731,-0.295694,9.271163,-8.030982,8.628011,5.642633,-1.524652,-8.395299,-2.669050,0.580523,2.814479,-6.007028,-2.639753,-4.846824,-9.669853],[-1.492695,-9.088860,6.722888,9.653620,-3.757978,-6.044440,-5.963481,-8.514860,-6.219534,-3.019208,0.016771,9.686784,-7.754023,8.680611,-5.200622],[1.599293,-2.342440,9.356222,8.676553,3.177601,1.763226,-1.207568,-0.501246,-2.438739,4.822083,-4.754915,5.847813,-0.166335,1.068711,-7.906245],[3.666505,0.384006,9.773176,-6.210572,8.913008,4.742400,5.301001,-1.374606,-5.174729,-0.679348,1.563459,-0.176390,-2.097086,-3.858808,-8.615136],[8.743834,4.570864,0.900057,8.058683,3.038563,-7.811896,-4.147290,-3.764195,6.804199,9.777457,2.511094,3.315596,3.155384,-1.957554,6.390086]]], dtype = "float64")#candidate|7837|(15, 8, 15)|const|float64
bop_7838 = relay.maximum(call_7796.astype('int32'), relay.reshape(const_7837.astype('int32'), relay.shape_of(call_7796))) # shape=(15, 8, 15)
bop_7841 = relay.maximum(call_7797.astype('int32'), relay.reshape(const_7837.astype('int32'), relay.shape_of(call_7797))) # shape=(15, 8, 15)
output = relay.Tuple([bop_7838,])
output2 = relay.Tuple([bop_7841,])
func_7854 = relay.Function([], output)
mod['func_7854'] = func_7854
mod = relay.transform.InferType()(mod)
mutated_mod['func_7854'] = func_7854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7854_call = mutated_mod.get_global_var('func_7854')
call_7855 = func_7854_call()
output = call_7855
func_7856 = relay.Function([], output)
mutated_mod['func_7856'] = func_7856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7051_call = mod.get_global_var('func_7051')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_7902 = func_7051_call()
call_7903 = func_7051_call()
const_7917 = relay.const([[[-8.448727,1.515370,-7.286418,-6.870461,8.547325,-8.110801,6.430006,-6.313962,0.071648,0.153885,-7.456548,7.561710,2.421498,2.656387,-5.401059,-2.229843],[1.507007,-1.910441,-1.173148,8.791502,9.139872,-5.297103,-5.010445,0.904081,7.299863,-7.660519,-3.985639,-3.441850,-6.935199,3.037542,-3.622168,8.930576],[-9.165223,8.366744,-9.749029,-7.910543,-5.068454,-7.167687,0.543701,-2.148504,-8.729627,-1.806708,-3.823593,-1.843561,7.426406,-2.071317,3.183594,5.079828]],[[9.332693,-7.526486,7.198858,-4.710359,2.243881,-9.077254,-3.254565,-7.153458,3.417937,5.122780,0.409459,-2.911553,-0.699732,-0.598229,-8.874023,0.266999],[-4.034301,-6.785944,-3.383090,-6.978413,0.980499,-9.475320,6.287201,2.267825,5.564145,4.760463,-5.355128,3.282562,-6.614849,0.194451,4.170919,-2.865218],[-3.682886,1.940814,4.176913,7.910427,-0.878346,-8.068903,-2.534813,0.404387,9.817087,-8.802636,-1.897230,-7.901587,5.640223,-2.093552,-5.142234,-7.495110]],[[6.813474,0.283697,0.061468,8.699567,-2.371966,-7.916789,2.037665,-8.725728,-8.435934,7.416013,0.327194,6.634708,8.850367,7.193822,-8.471345,-3.166864],[-7.793407,6.601772,-8.026665,1.000548,-9.496242,9.795151,4.147254,-0.327171,-7.183071,1.549382,4.359434,-3.494810,-5.621996,-5.650969,-7.348019,-6.322499],[-3.683546,-6.250697,-5.939657,8.534366,1.111311,6.806041,9.954604,-7.501331,6.587056,8.840612,-3.117274,7.560499,3.700706,-0.110637,-7.726085,-5.592117]],[[-5.599466,-3.078072,3.789270,4.884776,-2.943984,0.736969,0.927601,-3.167028,2.328660,0.072881,0.092631,-7.918095,7.634200,-2.390568,3.285038,-1.159092],[-1.999957,1.185504,4.263310,-4.353793,3.011190,4.695191,-5.715579,6.160384,1.847469,1.265452,7.280619,5.778692,-7.796763,-6.363791,8.684196,9.153908],[1.277963,2.949700,-8.257428,7.992527,8.819428,-4.911642,-6.297005,-4.038635,-3.347952,-6.393379,3.534915,-2.061173,-8.825447,-6.223486,-0.159056,3.383456]],[[-8.465426,-5.110113,-2.556630,-7.458943,-1.787710,5.935023,-9.264473,-2.401945,-5.044280,-6.417744,-6.447232,1.574397,9.498361,-7.639342,-7.997438,-6.036628],[-3.790633,4.591389,-0.090002,9.113316,-3.393179,5.385230,-6.329475,8.343444,-4.538597,-1.090344,9.648801,4.801653,1.116158,-0.788638,8.516491,-6.524899],[4.351516,1.445429,4.321063,-8.250611,5.566376,-3.682761,3.107411,-8.731829,0.556969,-5.879267,4.568331,-7.521864,-0.869001,-5.191034,5.615361,9.811607]],[[-0.911106,-5.336118,5.025504,6.616482,-9.703195,-5.707955,0.131282,5.391034,-7.883537,9.178332,-6.549334,-4.364621,-7.839322,-2.360889,-1.502372,-4.004303],[-9.216869,-1.418683,1.039771,2.303073,-9.349816,9.234256,-2.412310,-5.115476,6.922720,-4.294080,8.024295,-8.953201,6.833657,3.604670,-4.627095,-2.717122],[-9.812698,5.396164,-9.336420,3.858744,-2.956934,8.697770,-2.704461,3.382136,0.346399,8.831921,0.755689,6.387572,-5.873052,-9.414011,-2.796493,-2.345829]],[[0.959872,8.652837,-7.299032,-7.206556,0.878319,9.656601,-8.727459,7.230390,4.406615,-2.222426,-2.978849,7.123485,0.678813,-6.152333,5.407025,-4.801698],[-5.160026,-1.448520,7.144351,4.246987,-3.016340,-1.338721,-2.630856,2.144591,-7.059533,-2.708593,5.082635,4.691277,8.565314,-3.043366,-5.977059,1.572884],[-9.483517,7.171125,4.141709,0.184086,-8.570306,-2.066869,1.625928,-9.456853,8.750084,6.034290,-2.896093,3.298723,-0.450357,-8.295112,3.633693,1.512209]],[[-8.168933,7.451829,2.178829,7.669671,-7.579181,-4.737170,6.563368,3.078140,1.615955,3.984835,8.312102,1.038187,5.395485,1.197304,-3.973414,-0.075430],[6.561748,-5.368811,-5.750349,-0.503719,9.317627,4.696752,1.648229,0.387456,6.144372,5.922141,-3.120654,-1.990210,-1.793746,-4.647953,-6.713521,6.045936],[-1.612170,-9.172633,-8.890976,3.491882,-6.693955,-8.312696,7.077801,-3.650480,4.858176,6.137552,4.288571,8.341977,9.357243,-9.246464,-1.843269,-8.352969]],[[6.722287,-4.255535,6.241687,2.167070,-0.815753,-4.997964,2.088416,-6.720925,-3.418304,-6.249523,9.356770,8.459254,1.761763,-4.291320,-3.114492,-1.734030],[0.742966,8.566154,-6.120249,-7.791692,-1.869858,-7.975986,-4.724399,-0.532517,7.110561,-8.419846,-6.540958,0.218499,7.591772,-0.696214,-5.218698,8.330470],[9.710521,4.617914,2.223442,-4.728882,-9.066995,7.402333,3.961540,1.843843,5.236054,9.235711,1.482640,2.021458,-8.494587,-1.356509,3.155905,-2.531635]],[[-1.675778,-5.888153,-3.880164,-3.110035,-6.625157,6.841900,4.684706,-0.038538,-7.128917,7.939196,-6.766433,-9.632336,-3.525609,-7.990903,-2.943965,-3.052040],[-6.412877,-8.269869,4.219314,9.460595,-6.540612,1.978071,3.940987,-3.276466,2.775837,7.689420,2.635711,-1.376231,3.616513,8.368024,9.999812,-5.234713],[-3.808427,-7.216121,9.377104,9.236492,-5.130620,-9.930768,-3.771362,6.149943,-5.703025,-1.251651,-4.104914,8.461900,9.722302,9.258375,-3.370007,-5.200098]],[[-4.070699,-1.977763,-0.423403,-8.484997,-4.604050,-3.494907,2.615680,-5.070736,-3.322135,3.351220,1.091531,-9.415488,8.891878,3.944012,-6.679423,3.513560],[5.665968,-1.444658,3.782223,-4.653708,7.062279,6.206366,5.429974,-9.769556,-9.385966,-9.899224,-0.775279,-0.188144,9.130152,3.792006,4.512690,-1.606182],[-1.018085,-2.143175,8.649609,1.076564,1.229462,-9.099936,-3.939496,-1.516268,-2.299009,-4.332562,-5.060540,6.793744,5.107007,6.605780,0.865567,8.864604]]], dtype = "float64")#candidate|7917|(11, 3, 16)|const|float64
bop_7918 = relay.not_equal(call_7902.astype('bool'), relay.reshape(const_7917.astype('bool'), relay.shape_of(call_7902))) # shape=(11, 3, 16)
bop_7921 = relay.not_equal(call_7903.astype('bool'), relay.reshape(const_7917.astype('bool'), relay.shape_of(call_7903))) # shape=(11, 3, 16)
uop_7924 = relay.atanh(const_7917.astype('float32')) # shape=(11, 3, 16)
output = relay.Tuple([bop_7918,uop_7924,])
output2 = relay.Tuple([bop_7921,uop_7924,])
func_7935 = relay.Function([], output)
mod['func_7935'] = func_7935
mod = relay.transform.InferType()(mod)
mutated_mod['func_7935'] = func_7935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7935_call = mutated_mod.get_global_var('func_7935')
call_7936 = func_7935_call()
output = call_7936
func_7937 = relay.Function([], output)
mutated_mod['func_7937'] = func_7937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7051_call = mod.get_global_var('func_7051')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_7993 = func_7051_call()
call_7994 = func_7051_call()
output = relay.Tuple([call_7993,])
output2 = relay.Tuple([call_7994,])
func_8000 = relay.Function([], output)
mod['func_8000'] = func_8000
mod = relay.transform.InferType()(mod)
mutated_mod['func_8000'] = func_8000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8000_call = mutated_mod.get_global_var('func_8000')
call_8001 = func_8000_call()
output = call_8001
func_8002 = relay.Function([], output)
mutated_mod['func_8002'] = func_8002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mod.get_global_var('func_6126')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_8037 = func_6126_call()
call_8038 = func_6126_call()
func_7051_call = mod.get_global_var('func_7051')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_8082 = func_7051_call()
call_8083 = func_7051_call()
const_8086 = relay.const([[[-0.294357,-5.536352,-0.125758,2.643771,2.382512,8.060098,-7.165479,3.856973,2.046158,-8.829354,-4.178038,7.080650,-6.692291,-9.924831,5.886334,-1.867989],[-8.053831,-9.498376,-7.661149,6.257230,9.487304,-5.890351,-1.002943,-8.665224,-1.310621,7.183086,6.546281,-1.130636,2.406918,5.238024,9.106322,-1.193479],[1.377392,-5.593625,4.403988,9.275570,3.970619,-5.003873,7.058658,6.090290,2.735050,-8.400225,4.513698,4.602383,-4.244232,7.225074,-2.571894,0.895542]],[[9.110298,1.495332,2.689920,5.003373,3.618539,-7.317737,-2.806652,-5.421748,-1.248837,-2.197103,3.442159,-4.653419,-3.582906,2.674156,-3.104762,-8.125671],[6.483452,-3.503089,-0.904158,6.067775,1.089171,4.370437,3.249806,-0.362900,-9.942953,6.767181,-8.732159,1.301208,4.612350,9.112018,9.167022,5.114845],[-3.863338,1.096594,8.589749,-1.246154,-2.725412,-4.708296,5.591364,-6.488210,9.498488,4.433089,7.770503,4.417227,-3.988914,-8.352009,-0.456973,-1.793497]],[[7.330190,-5.715832,-9.490993,-9.278074,-5.467914,-9.793735,1.465899,1.383199,-4.460973,-7.752355,-2.130619,-2.072200,-8.046853,-0.842256,7.236193,2.815676],[4.580524,8.117708,-1.187320,-4.212041,0.770287,-2.729975,8.810806,9.411363,6.661899,-9.597034,4.792802,-3.887965,4.987348,7.079775,4.011093,-6.642616],[-1.471548,-0.011574,8.350933,8.069712,2.642919,6.550930,1.077352,-9.722776,-5.665832,-5.002058,7.985304,0.602992,-7.238324,7.707198,-7.340144,-4.376766]],[[-4.532300,8.473657,2.824945,-1.922722,2.222968,-8.578975,-3.375506,6.091751,0.542365,2.446143,-7.103123,4.104264,4.059744,-5.794210,-4.831460,-1.282983],[7.117314,-3.102863,-1.582551,6.417424,-2.230765,-3.342153,-7.951211,5.796538,-0.801101,-2.324219,-8.154823,8.940014,2.995421,1.347285,-1.742846,-2.258363],[5.135278,-0.631092,4.535237,2.497870,2.688637,-6.475171,1.426739,5.493795,-7.017813,-1.419890,-4.406028,-2.017124,2.479030,5.287689,9.570893,9.162993]],[[7.707456,-6.481672,4.613064,-3.487784,-6.610913,-6.374599,4.024521,1.491081,-7.621367,-3.825214,4.748962,-0.911186,-1.208240,-9.763481,5.665592,-7.379746],[5.580533,9.408834,3.557719,-1.234582,-5.816431,8.137449,-9.665882,-8.732377,8.137974,5.873883,2.561352,2.970631,-9.895148,-0.102560,-0.790981,-7.731616],[1.417505,-2.106518,4.693094,-3.454348,-4.153364,1.018604,-8.687566,5.187219,-9.261699,-0.801019,-2.809618,9.777958,8.380604,-7.476481,1.373154,-0.128187]],[[-6.321902,2.891997,3.392953,1.028296,4.630757,-6.897348,-7.993415,7.947744,1.451693,4.586873,-5.586460,-4.971056,-3.128952,7.779860,6.658109,-5.171596],[-6.963693,6.955091,-1.296992,9.215366,-9.450809,7.485973,0.641816,4.103399,9.042975,-3.745193,-6.369789,4.061219,6.844732,-1.861429,-9.238054,-6.209682],[-3.135517,-0.234677,7.220756,-5.903117,-7.402693,-7.047876,1.517506,-5.567867,-5.958731,-5.159005,8.894559,7.357648,-3.776922,5.006180,6.667895,9.930875]],[[6.269586,-1.518027,-6.887081,-9.333041,-6.558102,-5.855304,6.698477,-3.186321,-7.301455,-9.278759,3.177937,-4.675414,4.090407,-5.684954,-6.086675,-4.095587],[-9.406072,-2.883659,3.400742,3.712823,6.856159,2.201099,-3.039487,3.410402,-9.041441,-1.216433,7.155606,1.432339,-8.698603,1.592137,-2.253065,-7.096064],[-8.245459,1.161512,-4.069599,-0.051066,-9.531432,-0.650723,9.168715,0.704324,5.989056,5.709926,0.549374,8.441871,0.131030,-1.154470,-2.048059,-7.717070]],[[1.545859,-0.312556,-2.884655,0.295318,2.417985,3.159996,9.888736,-9.173683,-4.467911,-9.381282,8.162562,2.955527,-7.427174,-5.819917,-9.575650,-0.239893],[-0.500006,3.741014,6.500078,7.890186,-7.223404,5.853725,-9.711402,-2.193649,-2.981587,-3.185476,-3.530087,-9.773233,3.508112,8.925423,5.164247,6.836714],[4.349137,-0.106517,2.690662,2.190491,-0.465462,-1.403808,-0.638776,0.088451,1.801659,-9.657723,8.969653,-8.003620,2.846426,-2.031894,4.164314,-4.040545]],[[0.415692,1.453804,4.950552,-5.009256,-1.498116,-5.848139,-8.492212,9.274356,1.587869,3.968224,-9.739428,0.491020,-6.681472,-6.523961,0.065471,-9.201427],[6.899712,2.841333,-8.519399,-1.135068,-9.833750,7.604955,-4.154711,-3.853391,6.662284,-0.558182,-5.115339,4.080587,8.431609,-1.171525,8.780553,6.059335],[8.796379,6.407591,1.699413,-8.403241,-8.918578,-2.497344,-2.854855,-8.475866,-1.030286,7.296742,-4.323452,4.611263,-9.820682,-4.678533,-1.592590,-8.223988]],[[-9.297414,3.808556,8.696375,-8.426987,-8.054017,-3.078401,3.527996,-3.214818,3.852631,-2.079684,-0.745240,4.249611,-7.595369,-6.105361,-2.582106,-9.285057],[-3.761474,-3.054348,2.243763,8.815483,0.473556,-4.940544,-2.736384,-8.760829,-9.000021,3.396178,7.822031,3.892951,-2.758203,-4.393916,-6.871274,-8.940340],[9.494390,-8.401787,2.945441,-4.110120,1.782368,5.075742,6.422218,8.221855,9.711105,-4.471650,7.380293,-7.736833,-0.296556,-4.767481,6.050347,5.020188]],[[9.931835,4.818749,-7.228830,9.236594,-9.845775,3.813755,8.202108,5.250057,-0.512936,4.075087,6.746391,1.079620,-7.259747,-2.694548,-1.196225,-5.615903],[6.514354,-4.241623,0.921469,9.414129,3.079958,0.549132,6.858892,6.318802,6.850355,2.247091,-6.713913,-6.984104,2.037169,-2.707834,-3.122551,4.698209],[-0.227604,0.895387,-6.747593,6.526572,-1.967958,-6.413421,3.080719,3.909778,-4.783280,0.652928,0.299085,0.186487,-2.721540,1.940672,2.056850,-3.556992]]], dtype = "float64")#candidate|8086|(11, 3, 16)|const|float64
bop_8087 = relay.power(call_8082.astype('float32'), relay.reshape(const_8086.astype('float32'), relay.shape_of(call_8082))) # shape=(11, 3, 16)
bop_8090 = relay.power(call_8083.astype('float32'), relay.reshape(const_8086.astype('float32'), relay.shape_of(call_8083))) # shape=(11, 3, 16)
bop_8099 = relay.logical_and(bop_8087.astype('bool'), relay.reshape(const_8086.astype('bool'), relay.shape_of(bop_8087))) # shape=(11, 3, 16)
bop_8102 = relay.logical_and(bop_8090.astype('bool'), relay.reshape(const_8086.astype('bool'), relay.shape_of(bop_8090))) # shape=(11, 3, 16)
func_7935_call = mod.get_global_var('func_7935')
func_7937_call = mutated_mod.get_global_var('func_7937')
call_8112 = relay.TupleGetItem(func_7935_call(), 0)
call_8113 = relay.TupleGetItem(func_7937_call(), 0)
func_6813_call = mod.get_global_var('func_6813')
func_6815_call = mutated_mod.get_global_var('func_6815')
call_8129 = relay.TupleGetItem(func_6813_call(), 0)
call_8130 = relay.TupleGetItem(func_6815_call(), 0)
output = relay.Tuple([call_8037,bop_8099,call_8112,call_8129,])
output2 = relay.Tuple([call_8038,bop_8102,call_8113,call_8130,])
func_8133 = relay.Function([], output)
mod['func_8133'] = func_8133
mod = relay.transform.InferType()(mod)
output = func_8133()
func_8134 = relay.Function([], output)
mutated_mod['func_8134'] = func_8134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mod.get_global_var('func_6126')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_8155 = func_6126_call()
call_8156 = func_6126_call()
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_8177 = relay.TupleGetItem(func_5993_call(), 0)
call_8178 = relay.TupleGetItem(func_5995_call(), 0)
output = relay.Tuple([call_8155,call_8177,])
output2 = relay.Tuple([call_8156,call_8178,])
func_8193 = relay.Function([], output)
mod['func_8193'] = func_8193
mod = relay.transform.InferType()(mod)
output = func_8193()
func_8194 = relay.Function([], output)
mutated_mod['func_8194'] = func_8194
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8201 = relay.var("var_8201", dtype = "float64", shape = (8, 7, 11))#candidate|8201|(8, 7, 11)|var|float64
uop_8202 = relay.rsqrt(var_8201.astype('float64')) # shape=(8, 7, 11)
output = relay.Tuple([uop_8202,])
output2 = relay.Tuple([uop_8202,])
func_8216 = relay.Function([var_8201,], output)
mod['func_8216'] = func_8216
mod = relay.transform.InferType()(mod)
var_8217 = relay.var("var_8217", dtype = "float64", shape = (8, 7, 11))#candidate|8217|(8, 7, 11)|var|float64
output = func_8216(var_8217)
func_8218 = relay.Function([var_8217], output)
mutated_mod['func_8218'] = func_8218
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8246 = relay.const([[[5.898764,-0.131001,4.136782,-6.325277,-1.039749,4.477273,9.671331,8.472376,-7.309720,-4.377526],[-3.373491,-4.601889,3.916477,-1.048632,1.439952,-0.200818,8.361583,5.368190,-4.433517,9.131670],[2.979059,-8.607138,8.302252,3.191616,-1.684093,9.291255,-9.220729,9.991826,-8.138253,5.349737],[1.048960,-5.461383,-0.560387,-9.054937,3.188302,9.705264,-6.866715,-5.042336,-4.591002,-9.570737],[0.124645,4.747796,5.410871,3.399876,-4.940386,3.883640,-8.371020,-6.011374,7.219267,0.920557],[-4.358293,3.429601,-6.443464,9.767457,7.831810,-5.777290,2.587656,-0.902679,-2.478117,-6.300276]],[[8.278938,1.179285,3.701622,-2.899875,-1.010936,1.051136,7.614480,6.284520,-7.558346,-5.377948],[-3.185778,-0.701231,-9.756535,-5.973036,-1.196086,5.812045,1.945045,0.154013,2.682198,1.629697],[-5.884181,-6.705476,-2.478268,7.092508,-6.161429,-2.533481,-0.503575,-9.884119,-3.080220,-8.109649],[8.479062,-3.582031,-2.170683,8.846443,8.910181,1.277058,-2.766308,7.678563,3.006695,6.510830],[-8.681907,6.647955,2.695771,8.556624,-7.755147,-9.613434,-5.094467,-6.632314,5.311486,-4.051373],[3.792073,-0.488924,3.719471,-4.918618,-2.576910,0.540103,0.543378,-4.358602,-2.838925,-3.195561]],[[6.922824,3.252211,7.262047,-7.295716,2.867362,-9.493794,-5.995890,-6.544554,-7.129964,-0.118162],[0.180059,-1.808135,-0.206896,8.744698,-2.239943,-7.889012,-2.506432,8.494129,1.572679,-4.737420],[-9.028561,8.782541,4.640662,7.859923,-0.417881,7.405411,6.134211,1.366165,-6.854237,-4.866084],[-7.927500,-3.300132,-0.535062,6.506553,4.031664,9.330371,-4.845268,-8.672534,-9.991975,5.356563],[0.612082,-9.038363,-7.720502,2.074587,-1.235493,-8.594293,-0.902139,-0.384328,-0.101564,-5.842927],[2.642135,-1.866952,3.246802,-9.411195,-2.863686,-2.260854,-2.418567,-4.707417,-9.712055,8.433463]],[[3.348050,-9.672034,-7.428447,3.052056,-8.427771,-1.861332,4.902619,7.691115,8.969202,-1.326283],[1.850355,6.685562,-1.189790,0.765392,0.864650,1.239259,-9.969742,-2.223225,-1.802972,5.030906],[-7.432267,8.005794,-9.004611,-5.809095,-7.992798,8.588404,3.247244,2.584776,-3.200802,4.285365],[3.820049,9.767528,-2.083515,-9.401167,2.343110,3.044292,7.166162,8.125197,1.818211,3.824581],[-6.684876,1.592509,3.750641,2.239773,9.177782,-8.691564,-8.816865,-2.462551,3.633233,6.902368],[9.786131,-5.776854,4.195725,-2.868509,0.642981,-1.593994,6.900242,-4.632281,-9.669581,-7.645616]],[[-5.122682,-0.795025,-2.012693,8.900952,0.988432,-3.367044,4.175856,3.412215,-5.392206,0.416592],[7.714455,-0.136737,9.908033,-8.885552,-0.506450,-8.628403,6.667864,5.319330,1.334503,4.391548],[-2.237012,6.734889,9.986991,-9.786475,8.977808,4.849129,-8.175573,4.321247,-2.612456,4.624613],[-7.995220,9.838522,9.038162,-5.382527,7.092305,9.488761,9.717081,6.063283,-0.685341,4.865090],[8.226307,-6.343604,-7.188612,-6.289042,7.089634,8.937101,8.498365,9.624384,-5.403543,2.471985],[-8.294963,1.266651,-4.137252,-6.023216,-3.212667,-3.828739,-2.579509,4.844944,-0.039032,-6.642312]],[[-5.791798,7.809927,-3.750665,-2.218047,-8.205019,4.685809,-1.205268,5.714140,2.790650,3.660325],[8.701667,-3.558775,2.367501,-1.095003,0.322778,3.446172,-2.050977,4.806933,-5.409688,7.492639],[9.859553,0.009813,7.347705,-7.467195,-6.227586,0.189640,8.741941,2.541856,2.999335,-8.857460],[-7.207584,-5.533368,7.978653,-3.272723,6.371003,-0.895468,-2.023093,9.762331,-1.048796,-3.186578],[7.461932,-3.737194,7.463223,3.222289,7.161309,2.141702,-2.867184,7.735234,8.182790,0.048528],[6.292309,-4.915211,9.566806,-1.218630,2.559475,-2.238526,-7.616417,-1.746020,-9.831736,-8.171703]],[[4.679649,-6.553530,-3.615148,3.859254,3.312139,-7.582595,9.158466,-0.697893,-9.958354,-3.184326],[3.246531,4.140693,-9.626585,-0.740465,9.463066,-7.685713,-6.842720,-4.650121,-7.917863,0.684879],[-2.928405,2.863070,-1.258243,-1.118679,-6.636701,-7.502432,4.460819,7.383346,5.820637,5.590038],[-8.566771,-1.261083,-2.006011,5.079528,-8.685814,-9.673621,6.403832,-1.761831,7.613454,-2.195292],[-6.711439,3.163465,-3.935810,3.562270,-5.939460,7.843147,-7.872012,-8.670125,-8.435923,-9.297202],[-1.395609,-0.646659,-8.229048,9.271860,0.325787,0.337005,-0.066088,-7.616488,3.001665,7.552678]],[[-5.307445,-4.809989,-0.720235,8.752392,4.542901,5.649884,-1.729843,6.107516,1.665666,-6.836965],[-2.351099,-0.033555,-0.389889,-0.134914,-0.100090,-1.662202,-2.851451,1.871086,1.886452,3.156496],[-5.100128,-5.902817,-8.639873,1.905919,-2.841095,3.410467,1.523390,9.092691,-1.222202,0.094252],[5.903935,6.704243,1.273030,-1.144633,1.525867,8.644521,8.808781,-7.158748,7.367081,0.034549],[8.510017,-1.661303,-9.474133,-4.393139,5.193824,3.447220,1.721201,-4.888954,0.615876,7.668749],[2.039950,7.774003,-1.692149,-2.329810,4.742416,5.712781,-8.582568,-4.405417,-0.234196,7.033416]],[[-3.499964,-6.370285,6.354062,-9.044213,-4.967271,1.694730,-0.124612,-5.189310,-4.608450,-6.058965],[-5.993079,-2.159328,-5.876904,9.097687,-7.082950,-8.456733,3.683643,-1.921538,-6.934001,4.792791],[4.773893,-9.046351,2.173279,-5.567186,9.122236,-5.151241,2.649321,2.485715,5.262446,-1.675422],[0.389500,-6.335395,0.513576,-1.000945,-7.836539,-9.940556,-8.197556,4.468012,0.329399,-2.339027],[7.643042,-3.199839,1.704605,-0.830581,-3.437208,-6.356557,2.456476,-7.984925,-4.831352,-5.466226],[4.164847,-1.271028,0.565097,3.711530,0.927348,-7.276346,-4.533669,9.480104,-4.068860,-7.503438]],[[-5.458804,-8.193970,-8.727188,8.036781,0.028945,5.962433,-6.820784,7.961887,7.085475,1.445224],[-1.344705,7.925009,-9.629994,-7.099869,-0.415544,-7.357016,-5.424388,1.672210,1.677925,9.742209],[-8.501151,4.778551,-0.548329,1.857312,-5.216273,-7.057326,-0.530943,2.845100,7.694732,3.958174],[5.829605,-5.563814,-3.546863,-5.383975,-8.059496,0.678179,-4.300902,-6.528888,7.825011,-2.002384],[-4.515924,-7.281329,9.315200,3.962862,9.650853,-6.297548,-1.671798,-3.582042,-2.164088,0.891465],[-1.259915,-5.047604,8.479797,3.097628,-7.198247,-2.728869,3.076374,2.932019,2.570614,0.147263]],[[5.221092,9.732061,-7.634618,-1.644052,-4.285956,-8.885472,-8.880288,5.351817,9.471701,-9.688855],[-9.241976,-9.544905,6.795861,-7.812051,-9.644672,-2.655251,-0.086771,-3.076708,4.888089,4.632109],[-2.958864,1.910736,-1.347219,-8.632592,3.929880,3.513769,-0.672917,2.398614,5.146367,-3.448483],[3.260129,2.532699,-2.490037,5.732284,0.372391,2.717192,-0.220331,-5.573202,1.051532,-3.605068],[-1.672768,-1.836035,0.729376,-9.113411,-4.194594,-4.974843,3.071083,9.512911,9.903940,-0.130949],[2.961057,-1.319824,-8.267736,3.739448,-4.008752,-3.136488,0.387645,0.497528,0.686441,-4.660444]],[[-6.717871,2.422061,-5.424486,9.918918,2.139645,-8.466505,1.642459,-5.329689,-0.250586,5.732753],[4.794913,1.976809,-7.744491,5.450540,-4.850052,1.810914,9.776703,7.968239,0.705943,1.375387],[-9.577860,-8.500995,4.363915,6.705262,-2.287391,-9.580157,-1.856344,-9.140860,-9.798368,-0.226920],[1.557250,7.587326,5.038304,3.289698,9.455508,5.399352,-6.866804,5.938633,7.397578,9.729981],[2.568815,4.451021,8.427994,-7.820096,-2.758167,5.948399,4.178634,-7.429937,0.691493,4.775235],[-5.558106,-3.550318,-6.501581,-7.943118,-3.020435,5.279369,0.083082,1.456147,6.486555,-5.360378]],[[5.831206,5.130095,-4.648026,8.130456,9.094329,-9.775323,1.560283,2.157208,-9.241640,2.318266],[1.405339,-5.306638,-7.772219,-3.676537,-3.388423,7.765798,-6.346365,-0.655722,-1.884966,-3.360860],[-5.238629,4.153929,5.052071,-8.728900,4.273867,-9.512104,-2.319403,4.524663,-4.785844,-0.924187],[2.331239,-8.035504,3.810359,-3.869241,-3.883988,8.516480,-6.362072,7.166832,7.039498,2.269717],[1.320728,-1.343568,4.058008,-9.722118,8.403978,-4.271965,-6.545942,-9.132817,9.816337,8.278066],[3.415483,-4.010251,-5.641780,9.133245,5.786862,-5.839142,-2.653132,1.589424,-6.527603,5.891699]],[[-7.807821,-5.258262,1.304042,-6.396457,-9.594370,-2.085433,8.273755,8.967423,-7.734124,0.881809],[5.844069,1.689207,-6.890446,6.132846,-2.140933,-5.165869,-4.576308,-5.762489,9.607906,-8.592180],[-4.683976,3.851375,-0.045488,8.798622,3.678366,-6.568635,-8.813524,-2.473593,-1.674123,-2.240526],[9.797280,-3.449163,9.998093,6.338340,1.530303,-2.184228,-6.191114,2.962727,-4.108614,-5.081617],[-6.466970,5.733514,-4.677817,2.835806,1.680368,4.140554,8.925599,6.511288,-8.958444,5.459114],[-2.850944,-5.529023,-6.045069,3.685233,-2.251341,-0.504436,6.923634,-9.218525,-0.587008,-1.263404]],[[0.168156,-4.478287,3.642719,2.999044,-3.696241,-7.475332,9.468855,9.402210,-1.113192,-7.362696],[-2.540637,7.550111,-4.593511,9.452931,-6.900751,6.981207,-9.271233,-3.235531,6.573769,4.043674],[-4.719371,-0.889283,-8.606659,4.735123,4.165794,-4.515953,8.296701,2.793334,9.584958,-7.969663],[-7.772412,5.776018,0.492757,3.698690,7.558442,-0.763418,-4.526382,3.765335,-6.262182,5.205603],[5.357536,-6.368901,-0.620597,-5.476568,-9.001790,9.383340,-2.245420,2.435904,-3.312377,-4.201113],[-2.858077,9.460932,-5.078134,5.954552,-7.821404,-5.600883,-8.710796,-1.942497,-0.943727,-4.790856]],[[7.955118,5.740501,-7.143140,8.642808,7.625963,0.085514,-7.521311,-3.787374,1.329092,0.235033],[6.826691,6.683533,-6.728113,-6.269746,1.137077,-9.206599,-9.177457,-3.325858,-9.316919,1.064560],[-3.427372,6.223085,1.432050,2.737449,-5.431479,-2.837288,-8.564155,3.068098,5.871475,8.642997],[3.253146,1.752569,2.892444,-9.730539,7.140450,-8.445750,-3.791416,-6.937428,0.467380,5.860317],[8.205741,2.752636,1.676379,-8.159592,-6.150288,2.744134,4.737819,4.480571,1.969071,8.190452],[6.572804,-8.347167,2.071559,-5.404458,-7.811092,-5.589824,9.856219,4.663441,5.699392,-1.207524]]], dtype = "float32")#candidate|8246|(16, 6, 10)|const|float32
uop_8247 = relay.sigmoid(const_8246.astype('float32')) # shape=(16, 6, 10)
func_7239_call = mod.get_global_var('func_7239')
func_7240_call = mutated_mod.get_global_var('func_7240')
call_8249 = relay.TupleGetItem(func_7239_call(), 0)
call_8250 = relay.TupleGetItem(func_7240_call(), 0)
func_7786_call = mod.get_global_var('func_7786')
func_7788_call = mutated_mod.get_global_var('func_7788')
call_8251 = relay.TupleGetItem(func_7786_call(), 1)
call_8252 = relay.TupleGetItem(func_7788_call(), 1)
output = relay.Tuple([uop_8247,call_8249,call_8251,])
output2 = relay.Tuple([uop_8247,call_8250,call_8252,])
func_8258 = relay.Function([], output)
mod['func_8258'] = func_8258
mod = relay.transform.InferType()(mod)
output = func_8258()
func_8259 = relay.Function([], output)
mutated_mod['func_8259'] = func_8259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6838_call = mod.get_global_var('func_6838')
func_6840_call = mutated_mod.get_global_var('func_6840')
call_8292 = relay.TupleGetItem(func_6838_call(), 0)
call_8293 = relay.TupleGetItem(func_6840_call(), 0)
func_5730_call = mod.get_global_var('func_5730')
func_5732_call = mutated_mod.get_global_var('func_5732')
var_8299 = relay.var("var_8299", dtype = "float32", shape = (180,))#candidate|8299|(180,)|var|float32
call_8298 = relay.TupleGetItem(func_5730_call(relay.reshape(var_8299.astype('float32'), [6, 30])), 3)
call_8300 = relay.TupleGetItem(func_5732_call(relay.reshape(var_8299.astype('float32'), [6, 30])), 3)
func_7854_call = mod.get_global_var('func_7854')
func_7856_call = mutated_mod.get_global_var('func_7856')
call_8316 = relay.TupleGetItem(func_7854_call(), 0)
call_8317 = relay.TupleGetItem(func_7856_call(), 0)
func_7766_call = mod.get_global_var('func_7766')
func_7768_call = mutated_mod.get_global_var('func_7768')
var_8321 = relay.var("var_8321", dtype = "bool", shape = (720,))#candidate|8321|(720,)|var|bool
call_8320 = relay.TupleGetItem(func_7766_call(relay.reshape(var_8321.astype('bool'), [720,])), 2)
call_8322 = relay.TupleGetItem(func_7768_call(relay.reshape(var_8321.astype('bool'), [720,])), 2)
output = relay.Tuple([call_8292,call_8298,var_8299,call_8316,call_8320,var_8321,])
output2 = relay.Tuple([call_8293,call_8300,var_8299,call_8317,call_8322,var_8321,])
func_8329 = relay.Function([var_8299,var_8321,], output)
mod['func_8329'] = func_8329
mod = relay.transform.InferType()(mod)
var_8330 = relay.var("var_8330", dtype = "float32", shape = (180,))#candidate|8330|(180,)|var|float32
var_8331 = relay.var("var_8331", dtype = "bool", shape = (720,))#candidate|8331|(720,)|var|bool
output = func_8329(var_8330,var_8331,)
func_8332 = relay.Function([var_8330,var_8331,], output)
mutated_mod['func_8332'] = func_8332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5932_call = mod.get_global_var('func_5932')
func_5934_call = mutated_mod.get_global_var('func_5934')
call_8369 = func_5932_call()
call_8370 = func_5932_call()
output = call_8369
output2 = call_8370
func_8371 = relay.Function([], output)
mod['func_8371'] = func_8371
mod = relay.transform.InferType()(mod)
mutated_mod['func_8371'] = func_8371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8371_call = mutated_mod.get_global_var('func_8371')
call_8372 = func_8371_call()
output = call_8372
func_8373 = relay.Function([], output)
mutated_mod['func_8373'] = func_8373
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8426 = relay.var("var_8426", dtype = "float32", shape = (1, 14, 7))#candidate|8426|(1, 14, 7)|var|float32
uop_8427 = relay.log(var_8426.astype('float32')) # shape=(1, 14, 7)
func_4196_call = mod.get_global_var('func_4196')
func_4201_call = mutated_mod.get_global_var('func_4201')
const_8432 = relay.const([[6,5,5,-1,-3,5,-4,2,8,8,-7,-3,-9,10,9,-9,-4,-4,10,-1,6,6,2,9,-1,7,-3,8,-3,10,-4,6,-3,-10,-6,7,-9,-3,10,-1,9,10,-8,6,7,-5,4,1,-2,2,4,-1,2,-1,5,5,2,8,4,-3,-9,-1,10,2,-5,-1,4,9,3,10,4,4,1,-7,-3,5,9,-4,-8,-2,-1,-1,2,-4,-9,-4,2,-10,7,7,10,-3,7,-7,-4,-7,9,-3,-7,-9,-1,-1,1,5,1,-2,-3,-9,4,5,-4,-4,-2,5,4,-6,-8,-8,-10,-1,-7,3,7,10,7,-1,8,5,4,9,-5,3,-4,4,-7,9,7,-4,4,-8,-7,-4,-4,-5,9,6,-9,-9,3,-8,-6,4,9,-8,10,-7,-4,-2,-10,-9,-2,-4,6,-5,5,-9,2,-4,1,-5,-7,8,3,-10,-8,3,3,-1,1,8,-3,8,-2,8,4,4,6,-1,-1,-4,-9,7,4,-1,-7,-10,-7,4,1,-5,-5,-6,-9,2,1,9,2,-2,-5,1,1,2,2,-1,10,-9,3,8,6,1,7,-7,-7,5,-9,4,2,2,-4,6,-7,8,4,-1,7,8,-4,-3,2,-3,-8,5,-4,1,-7,1,6,5,5,-10,2,6,-1,-6,-1,-5,7,9,6,9,-1,-1,-2,-6,-4,1,4,-9,10,-9,-6,10,-6,-5,10,-8,-6,7,5,7,10,3,-7,9,10,6,4,-7,6,-3,-8,7,-9,-4,-10,4,-8,5,9,-3,-4,5,7,-10,-6,9,-5,-7,-5,-1,-1,6,-1,-7,9,-1,8,-2,-10,8,-5,-7,7,7,7,6,4,-9,7,5]], dtype = "uint8")#candidate|8432|(1, 330)|const|uint8
var_8433 = relay.var("var_8433", dtype = "float32", shape = (624,))#candidate|8433|(624,)|var|float32
const_8434 = relay.const(2, dtype = "uint32")#candidate|8434|()|const|uint32
call_8431 = relay.TupleGetItem(func_4196_call(relay.reshape(const_8432.astype('uint8'), [2, 11, 15]), relay.reshape(const_8432.astype('uint8'), [2, 11, 15]), relay.reshape(var_8433.astype('float32'), [624,]), relay.reshape(const_8434.astype('uint32'), []), ), 4)
call_8435 = relay.TupleGetItem(func_4201_call(relay.reshape(const_8432.astype('uint8'), [2, 11, 15]), relay.reshape(const_8432.astype('uint8'), [2, 11, 15]), relay.reshape(var_8433.astype('float32'), [624,]), relay.reshape(const_8434.astype('uint32'), []), ), 4)
func_6885_call = mod.get_global_var('func_6885')
func_6886_call = mutated_mod.get_global_var('func_6886')
call_8443 = relay.TupleGetItem(func_6885_call(), 2)
call_8444 = relay.TupleGetItem(func_6886_call(), 2)
output = relay.Tuple([uop_8427,call_8431,const_8432,var_8433,const_8434,call_8443,])
output2 = relay.Tuple([uop_8427,call_8435,const_8432,var_8433,const_8434,call_8444,])
func_8451 = relay.Function([var_8426,var_8433,], output)
mod['func_8451'] = func_8451
mod = relay.transform.InferType()(mod)
var_8452 = relay.var("var_8452", dtype = "float32", shape = (1, 14, 7))#candidate|8452|(1, 14, 7)|var|float32
var_8453 = relay.var("var_8453", dtype = "float32", shape = (624,))#candidate|8453|(624,)|var|float32
output = func_8451(var_8452,var_8453,)
func_8454 = relay.Function([var_8452,var_8453,], output)
mutated_mod['func_8454'] = func_8454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6713_call = mod.get_global_var('func_6713')
func_6714_call = mutated_mod.get_global_var('func_6714')
call_8475 = relay.TupleGetItem(func_6713_call(), 1)
call_8476 = relay.TupleGetItem(func_6714_call(), 1)
func_6408_call = mod.get_global_var('func_6408')
func_6411_call = mutated_mod.get_global_var('func_6411')
var_8480 = relay.var("var_8480", dtype = "float32", shape = (180,))#candidate|8480|(180,)|var|float32
call_8479 = relay.TupleGetItem(func_6408_call(relay.reshape(var_8480.astype('float32'), [6, 30])), 2)
call_8481 = relay.TupleGetItem(func_6411_call(relay.reshape(var_8480.astype('float32'), [6, 30])), 2)
output = relay.Tuple([call_8475,call_8479,var_8480,])
output2 = relay.Tuple([call_8476,call_8481,var_8480,])
func_8486 = relay.Function([var_8480,], output)
mod['func_8486'] = func_8486
mod = relay.transform.InferType()(mod)
mutated_mod['func_8486'] = func_8486
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8487 = relay.var("var_8487", dtype = "float32", shape = (180,))#candidate|8487|(180,)|var|float32
func_8486_call = mutated_mod.get_global_var('func_8486')
call_8488 = func_8486_call(var_8487)
output = call_8488
func_8489 = relay.Function([var_8487], output)
mutated_mod['func_8489'] = func_8489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7854_call = mod.get_global_var('func_7854')
func_7856_call = mutated_mod.get_global_var('func_7856')
call_8549 = relay.TupleGetItem(func_7854_call(), 0)
call_8550 = relay.TupleGetItem(func_7856_call(), 0)
output = relay.Tuple([call_8549,])
output2 = relay.Tuple([call_8550,])
func_8556 = relay.Function([], output)
mod['func_8556'] = func_8556
mod = relay.transform.InferType()(mod)
output = func_8556()
func_8557 = relay.Function([], output)
mutated_mod['func_8557'] = func_8557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6769_call = mod.get_global_var('func_6769')
func_6771_call = mutated_mod.get_global_var('func_6771')
call_8619 = func_6769_call()
call_8620 = func_6769_call()
output = relay.Tuple([call_8619,])
output2 = relay.Tuple([call_8620,])
func_8625 = relay.Function([], output)
mod['func_8625'] = func_8625
mod = relay.transform.InferType()(mod)
output = func_8625()
func_8626 = relay.Function([], output)
mutated_mod['func_8626'] = func_8626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6924_call = mod.get_global_var('func_6924')
func_6925_call = mutated_mod.get_global_var('func_6925')
call_8656 = func_6924_call()
call_8657 = func_6924_call()
func_6813_call = mod.get_global_var('func_6813')
func_6815_call = mutated_mod.get_global_var('func_6815')
call_8671 = relay.TupleGetItem(func_6813_call(), 0)
call_8672 = relay.TupleGetItem(func_6815_call(), 0)
output = relay.Tuple([call_8656,call_8671,])
output2 = relay.Tuple([call_8657,call_8672,])
func_8686 = relay.Function([], output)
mod['func_8686'] = func_8686
mod = relay.transform.InferType()(mod)
mutated_mod['func_8686'] = func_8686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8686_call = mutated_mod.get_global_var('func_8686')
call_8687 = func_8686_call()
output = call_8687
func_8688 = relay.Function([], output)
mutated_mod['func_8688'] = func_8688
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8723 = relay.var("var_8723", dtype = "float32", shape = (1, 5, 11))#candidate|8723|(1, 5, 11)|var|float32
uop_8724 = relay.acos(var_8723.astype('float32')) # shape=(1, 5, 11)
output = uop_8724
output2 = uop_8724
func_8733 = relay.Function([var_8723,], output)
mod['func_8733'] = func_8733
mod = relay.transform.InferType()(mod)
var_8734 = relay.var("var_8734", dtype = "float32", shape = (1, 5, 11))#candidate|8734|(1, 5, 11)|var|float32
output = func_8733(var_8734)
func_8735 = relay.Function([var_8734], output)
mutated_mod['func_8735'] = func_8735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7051_call = mod.get_global_var('func_7051')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_8798 = func_7051_call()
call_8799 = func_7051_call()
output = call_8798
output2 = call_8799
func_8801 = relay.Function([], output)
mod['func_8801'] = func_8801
mod = relay.transform.InferType()(mod)
output = func_8801()
func_8802 = relay.Function([], output)
mutated_mod['func_8802'] = func_8802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_8807 = relay.TupleGetItem(func_5104_call(), 0)
call_8808 = relay.TupleGetItem(func_5106_call(), 0)
func_1061_call = mod.get_global_var('func_1061')
func_1063_call = mutated_mod.get_global_var('func_1063')
const_8825 = relay.const([2.359955,-8.464256,-2.939062,1.569582,-5.280629,-3.813310,9.609399,3.548110,-2.199285,5.825779,-6.610853,5.031694,8.431804,-0.002421,-0.225778,0.842125,-1.243670,-9.194811,5.827457,4.344021,4.415161,0.422199,-4.890065,-0.116328,4.371845,8.580244,-4.529493,-5.898390,9.250396,-7.391302,-4.635438,4.935406,7.860502,6.251221,1.059948,-9.372983,-3.835669,8.128612,5.464405,9.174992,-8.570188,-4.351653,-7.872963,-2.965980,-2.259541,6.578216,3.683139,0.695737,-3.417888,2.474392,9.176167,-0.319979,-3.368849,-8.923242,-0.302968,-7.596506,5.863547,4.935921,4.941031,8.167268,-3.911249,-8.429812,-7.822631,5.301016,-4.356033,-5.800825,-3.431139,7.193312,7.251689,-8.656447,-1.744434,-9.656337,-6.387639,8.702986,2.971066,0.657432,4.669554,6.304789,3.254261,9.155348,-1.211399,0.057118,-3.875525,9.337515,-7.841124,7.201449,-9.515474,-8.284678,7.543556,8.086477,0.841201,9.901939,-1.277159,-6.090614,4.893207,-7.402766,5.516641,-1.941000,-2.731674,5.539596,-9.322097,0.303560,-6.123168,2.562337,7.281367,6.930003,5.546347,-6.858907,7.994420,7.274430,-4.072074,-4.598438,5.276260,2.731876,-3.999568,-3.143255,-6.910835,-4.586306,-1.317024,-7.391075,-8.090695,-5.995626,-2.886022,7.086472,0.133520,-8.092576,-9.420987,4.241134,-2.032751,-7.995002,-4.312326,9.330817,-0.591399,2.069179,1.262007,8.864977,8.171953,7.236323,-2.164225,-8.321487,5.374599,8.693540,2.152406,7.471605,2.634166,2.153884,-8.798589,-4.671584,-8.716040,5.024253,-9.789960,0.727575,-5.220722,4.696740,1.058242,-6.285177,7.321448,6.830877,7.915831,-9.900620,-0.271130,-2.845648,-4.935390,1.573429,-1.484120,-1.825009,7.053297,7.168411,-9.452578,-0.241397,-0.064002,-8.705818,-9.046768,-0.821643,-7.787779,7.563757,-7.746816,6.175585,-9.195576,1.573103], dtype = "float32")#candidate|8825|(180,)|const|float32
call_8824 = relay.TupleGetItem(func_1061_call(relay.reshape(const_8825.astype('float32'), [4, 9, 5])), 0)
call_8826 = relay.TupleGetItem(func_1063_call(relay.reshape(const_8825.astype('float32'), [4, 9, 5])), 0)
output = relay.Tuple([call_8807,call_8824,const_8825,])
output2 = relay.Tuple([call_8808,call_8826,const_8825,])
func_8845 = relay.Function([], output)
mod['func_8845'] = func_8845
mod = relay.transform.InferType()(mod)
mutated_mod['func_8845'] = func_8845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8845_call = mutated_mod.get_global_var('func_8845')
call_8846 = func_8845_call()
output = call_8846
func_8847 = relay.Function([], output)
mutated_mod['func_8847'] = func_8847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7239_call = mod.get_global_var('func_7239')
func_7240_call = mutated_mod.get_global_var('func_7240')
call_8886 = relay.TupleGetItem(func_7239_call(), 0)
call_8887 = relay.TupleGetItem(func_7240_call(), 0)
output = relay.Tuple([call_8886,])
output2 = relay.Tuple([call_8887,])
func_8891 = relay.Function([], output)
mod['func_8891'] = func_8891
mod = relay.transform.InferType()(mod)
mutated_mod['func_8891'] = func_8891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8891_call = mutated_mod.get_global_var('func_8891')
call_8892 = func_8891_call()
output = call_8892
func_8893 = relay.Function([], output)
mutated_mod['func_8893'] = func_8893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_8899 = relay.TupleGetItem(func_5993_call(), 0)
call_8900 = relay.TupleGetItem(func_5995_call(), 0)
uop_8916 = relay.asinh(call_8899.astype('float64')) # shape=(11, 3, 16)
uop_8918 = relay.asinh(call_8900.astype('float64')) # shape=(11, 3, 16)
output = relay.Tuple([uop_8916,])
output2 = relay.Tuple([uop_8918,])
func_8919 = relay.Function([], output)
mod['func_8919'] = func_8919
mod = relay.transform.InferType()(mod)
mutated_mod['func_8919'] = func_8919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8919_call = mutated_mod.get_global_var('func_8919')
call_8920 = func_8919_call()
output = call_8920
func_8921 = relay.Function([], output)
mutated_mod['func_8921'] = func_8921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_8952 = func_5645_call()
call_8953 = func_5645_call()
output = call_8952
output2 = call_8953
func_8966 = relay.Function([], output)
mod['func_8966'] = func_8966
mod = relay.transform.InferType()(mod)
mutated_mod['func_8966'] = func_8966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8966_call = mutated_mod.get_global_var('func_8966')
call_8967 = func_8966_call()
output = call_8967
func_8968 = relay.Function([], output)
mutated_mod['func_8968'] = func_8968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5932_call = mod.get_global_var('func_5932')
func_5934_call = mutated_mod.get_global_var('func_5934')
call_8999 = func_5932_call()
call_9000 = func_5932_call()
output = call_8999
output2 = call_9000
func_9018 = relay.Function([], output)
mod['func_9018'] = func_9018
mod = relay.transform.InferType()(mod)
mutated_mod['func_9018'] = func_9018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9018_call = mutated_mod.get_global_var('func_9018')
call_9019 = func_9018_call()
output = call_9019
func_9020 = relay.Function([], output)
mutated_mod['func_9020'] = func_9020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9057 = relay.var("var_9057", dtype = "bool", shape = ())#candidate|9057|()|var|bool
var_9058 = relay.var("var_9058", dtype = "bool", shape = (16, 2, 1))#candidate|9058|(16, 2, 1)|var|bool
bop_9059 = relay.logical_and(var_9057.astype('bool'), var_9058.astype('bool')) # shape=(16, 2, 1)
bop_9064 = relay.less_equal(var_9058.astype('bool'), var_9057.astype('bool')) # shape=(16, 2, 1)
func_8000_call = mod.get_global_var('func_8000')
func_8002_call = mutated_mod.get_global_var('func_8002')
call_9070 = relay.TupleGetItem(func_8000_call(), 0)
call_9071 = relay.TupleGetItem(func_8002_call(), 0)
bop_9082 = relay.mod(var_9057.astype('float32'), bop_9059.astype('float32')) # shape=(16, 2, 1)
func_2614_call = mod.get_global_var('func_2614')
func_2618_call = mutated_mod.get_global_var('func_2618')
const_9086 = relay.const([[-3.721111,-6.867054,1.760018,-4.765379,-7.919332,4.938052,5.676353,-8.678309,-9.300491,9.046605,0.613862,-6.631411,9.378713,-6.074847,-5.954946,4.663256,9.550387,6.181113,-7.836230,8.563786],[2.573740,7.899269,-8.313311,-4.877433,-5.918547,-7.934644,-6.363865,-2.902537,9.401875,-9.074408,2.822566,-0.818717,2.567866,3.891334,-5.830952,0.258280,6.394713,-9.424340,-4.020082,-6.503478],[-3.076605,-7.686882,2.648933,1.618049,-0.432233,-2.404754,7.675191,-4.211075,-5.870354,-0.332869,-1.837073,-5.079442,-5.580171,-5.135956,4.547132,3.784682,9.926338,7.319738,-3.485739,4.290076],[-1.883235,-2.476211,0.055806,-4.483591,-5.428334,-9.924270,-2.586190,-1.335489,1.890413,1.144869,0.858507,7.812512,9.970539,-7.278591,7.006754,-4.679931,8.919966,4.017524,6.013583,5.377631]], dtype = "float32")#candidate|9086|(4, 20)|const|float32
call_9085 = relay.TupleGetItem(func_2614_call(relay.reshape(var_9057.astype('float32'), []), relay.reshape(const_9086.astype('float32'), [5, 1, 16]), ), 0)
call_9087 = relay.TupleGetItem(func_2618_call(relay.reshape(var_9057.astype('float32'), []), relay.reshape(const_9086.astype('float32'), [5, 1, 16]), ), 0)
func_8919_call = mod.get_global_var('func_8919')
func_8921_call = mutated_mod.get_global_var('func_8921')
call_9091 = relay.TupleGetItem(func_8919_call(), 0)
call_9092 = relay.TupleGetItem(func_8921_call(), 0)
bop_9094 = relay.greater_equal(call_9085.astype('bool'), var_9057.astype('bool')) # shape=(5, 1, 16)
bop_9097 = relay.greater_equal(call_9087.astype('bool'), var_9057.astype('bool')) # shape=(5, 1, 16)
bop_9112 = relay.multiply(bop_9059.astype('uint32'), relay.reshape(bop_9082.astype('uint32'), relay.shape_of(bop_9059))) # shape=(16, 2, 1)
func_7497_call = mod.get_global_var('func_7497')
func_7499_call = mutated_mod.get_global_var('func_7499')
call_9117 = relay.TupleGetItem(func_7497_call(), 8)
call_9118 = relay.TupleGetItem(func_7499_call(), 8)
bop_9119 = relay.power(bop_9112.astype('float32'), var_9057.astype('float32')) # shape=(16, 2, 1)
bop_9130 = relay.greater_equal(bop_9064.astype('bool'), var_9057.astype('bool')) # shape=(16, 2, 1)
func_6331_call = mod.get_global_var('func_6331')
func_6334_call = mutated_mod.get_global_var('func_6334')
const_9150 = relay.const([[2],[-1],[-8],[8],[-2],[-7],[-4],[-5],[6],[-3],[7],[-7],[10],[-7],[-6],[3],[8],[10],[3],[-8],[-10],[10],[-2],[4],[2],[-2],[1],[5],[9],[-2],[-5],[-4],[10],[-3],[-1],[-6],[7],[-8],[-2],[8],[-2],[-4],[2],[-2],[1],[8],[10],[-1],[8],[-3],[-4],[-4],[6],[10],[6],[1],[2],[1],[-5],[7],[-9],[-4],[-8],[7],[-8],[5],[-9],[2],[10],[-3],[-4],[4],[-10],[-10],[-10],[-4],[3],[-5],[-10],[7],[5],[1],[2],[1],[-7],[-10],[-9],[-7],[-3],[-7],[-5],[9],[-7],[-10],[-9],[9],[10],[9],[-3],[-8],[7],[3],[6],[6],[-10],[-2],[3],[2],[-8],[-9],[9],[10],[-7],[-5],[-1],[3],[3],[-3],[-8],[8],[-3],[-1],[-2],[6],[-7],[-6],[4],[8],[-6],[2],[-8],[-3],[-10],[9],[7],[-4],[-10],[7],[-1],[-9],[-10],[7],[-10],[7],[-9],[-3],[-3],[7],[-5],[1],[-6],[4],[-3],[-7],[4],[3],[2],[9],[-6],[-9],[-5],[-2],[-9],[2],[-9],[-9],[10],[-2],[-2],[7],[4],[1],[-1],[-9],[-7],[10],[9],[10],[2],[5],[5],[-8],[-7],[7],[-7],[7],[-4],[9],[-9],[10],[7],[5],[5],[5],[7],[1],[-3],[-6],[7],[-10],[-8],[8],[-5],[7],[7],[1],[-9],[-9],[2],[-2],[-5],[-3],[-1],[-1],[-4],[3],[-9],[-4],[-9],[-10],[10],[10],[8],[4],[3],[-2],[-10],[-9],[4],[9],[10],[-10],[4],[3],[6],[-2],[7],[-6],[1],[-8],[7],[-7],[5],[-9],[-3],[-6],[2],[-3],[-1],[2],[2],[-4],[7],[-5],[-9],[5],[2],[-4],[-7],[5],[1],[4],[-9],[-10],[3],[-10],[7],[5],[1],[4],[-2],[-7],[-10],[-1],[-1],[-8],[8],[-6],[9],[9],[-9],[9],[2],[-1],[6],[4],[-4],[-2],[1],[-3],[8],[5],[-3],[4],[6],[-6],[-2],[-2],[-8],[9],[8],[-2],[4],[9],[7],[-10],[-3],[-2],[-5],[-10],[2],[9],[-8],[-10],[5],[10],[5],[-8],[-8],[-6],[8],[2],[10],[-2],[4],[7],[6],[10],[6],[2],[-1],[7],[-6],[5],[-1],[-9],[-7],[-2],[8],[-2],[-6],[6],[7],[-7],[8],[-6],[-6],[5],[5],[8],[-2],[-7],[-9],[-4],[3],[-9],[6],[-10],[-3],[-6],[10],[2],[-3],[8],[8],[6],[-4],[-9],[-1],[1],[-10],[4],[8],[-9],[-3],[-4],[6],[-9],[-6],[9],[-4],[5],[9],[2],[-8],[8],[3],[-4],[-8],[-4],[7],[-5],[5],[-2],[-2],[6],[-9],[7],[-5],[-1],[-2],[-1],[-1],[-8],[9],[1],[7],[8],[10],[4],[4],[-2],[-10],[-4],[8],[8],[-6],[-4],[3],[7],[3],[7],[-2],[3],[-7],[-5],[-8],[-6],[4],[5],[-5],[1],[-3],[8],[9],[9],[1],[-2],[-3],[4],[4],[10],[6],[4],[6],[-3],[6],[10],[-1],[7],[-4],[-1],[-2],[-10],[10],[4],[-5],[9],[10],[1],[-5],[-7],[-8],[-10],[7],[-8],[4],[8],[4],[3],[-3],[-9],[-3],[10],[-2],[-1],[5],[5],[7],[2],[-3],[-5],[-10],[4],[-4],[-10],[-6],[-7],[-5],[-4],[8],[-3],[-3],[4],[-4],[-2],[-7],[-5],[-3],[-2],[8],[5],[-9],[4],[-7],[-3],[2],[-8],[4],[3],[-8],[-6],[-5],[3],[4],[4],[-7],[7],[-1],[-2],[-7],[-3],[-8],[-4],[-3],[-2],[-5],[8],[-1],[-7],[-6],[8],[-1],[-9],[-8],[-1],[5],[6],[7],[6],[10],[-2],[6],[4],[-3],[-4],[-3],[2],[9],[-4],[-4],[4],[1],[3],[-3],[-7],[-6],[-7],[-1],[2],[9],[2],[-2],[5],[8],[10],[6],[-1],[5],[2],[-2],[-8],[-8],[-5],[-3],[2],[4],[-5],[-8],[8],[2],[8],[-2],[-3],[-3],[-3],[-6],[5],[8],[-4],[6],[-5],[7],[7],[-2],[3],[-4],[2],[-10],[-3],[3],[-9],[-10],[2],[4],[-9],[9],[-3],[5],[4],[-8],[3],[-8],[8],[-1],[-2],[-10],[3],[5],[6],[-1],[-2],[-8],[-1],[-8],[4],[3],[-5],[-4],[2]], dtype = "int64")#candidate|9150|(630, 1)|const|int64
call_9149 = relay.TupleGetItem(func_6331_call(relay.reshape(var_9057.astype('uint32'), []), relay.reshape(const_9150.astype('int64'), [630,]), ), 6)
call_9151 = relay.TupleGetItem(func_6334_call(relay.reshape(var_9057.astype('uint32'), []), relay.reshape(const_9150.astype('int64'), [630,]), ), 6)
output = relay.Tuple([call_9070,const_9086,call_9091,bop_9094,call_9117,bop_9119,bop_9130,call_9149,const_9150,])
output2 = relay.Tuple([call_9071,const_9086,call_9092,bop_9097,call_9118,bop_9119,bop_9130,call_9151,const_9150,])
func_9156 = relay.Function([var_9057,var_9058,], output)
mod['func_9156'] = func_9156
mod = relay.transform.InferType()(mod)
mutated_mod['func_9156'] = func_9156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9156_call = mutated_mod.get_global_var('func_9156')
var_9158 = relay.var("var_9158", dtype = "bool", shape = ())#candidate|9158|()|var|bool
var_9159 = relay.var("var_9159", dtype = "bool", shape = (16, 2, 1))#candidate|9159|(16, 2, 1)|var|bool
call_9157 = func_9156_call(var_9158,var_9159,)
output = call_9157
func_9160 = relay.Function([var_9158,var_9159,], output)
mutated_mod['func_9160'] = func_9160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7102_call = mod.get_global_var('func_7102')
func_7104_call = mutated_mod.get_global_var('func_7104')
call_9187 = relay.TupleGetItem(func_7102_call(), 0)
call_9188 = relay.TupleGetItem(func_7104_call(), 0)
output = call_9187
output2 = call_9188
func_9193 = relay.Function([], output)
mod['func_9193'] = func_9193
mod = relay.transform.InferType()(mod)
output = func_9193()
func_9194 = relay.Function([], output)
mutated_mod['func_9194'] = func_9194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8133_call = mod.get_global_var('func_8133')
func_8134_call = mutated_mod.get_global_var('func_8134')
call_9306 = relay.TupleGetItem(func_8133_call(), 3)
call_9307 = relay.TupleGetItem(func_8134_call(), 3)
func_5958_call = mod.get_global_var('func_5958')
func_5961_call = mutated_mod.get_global_var('func_5961')
var_9315 = relay.var("var_9315", dtype = "float32", shape = (8,))#candidate|9315|(8,)|var|float32
call_9314 = relay.TupleGetItem(func_5958_call(relay.reshape(var_9315.astype('float32'), [8, 1])), 1)
call_9316 = relay.TupleGetItem(func_5961_call(relay.reshape(var_9315.astype('float32'), [8, 1])), 1)
output = relay.Tuple([call_9306,call_9314,var_9315,])
output2 = relay.Tuple([call_9307,call_9316,var_9315,])
func_9335 = relay.Function([var_9315,], output)
mod['func_9335'] = func_9335
mod = relay.transform.InferType()(mod)
var_9336 = relay.var("var_9336", dtype = "float32", shape = (8,))#candidate|9336|(8,)|var|float32
output = func_9335(var_9336)
func_9337 = relay.Function([var_9336], output)
mutated_mod['func_9337'] = func_9337
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9361 = relay.const([[[-8,-10,5,8,-7,-2,4,2,7,-5,-7,-9,-6],[4,-7,-3,-6,-7,-7,7,-3,-3,-2,-7,6,-7],[-2,3,-5,9,2,10,-5,8,-3,5,3,5,4],[4,3,-2,8,-4,4,6,7,5,2,-5,-8,2],[-2,-7,-10,-4,-2,7,4,2,7,6,-5,-8,-6],[-1,7,8,-2,-4,7,5,-6,9,4,-8,1,-4],[4,-3,-7,7,-2,3,-1,8,5,-7,-4,9,-2],[-8,2,1,-6,-8,-1,-8,7,6,-6,-6,-8,2],[-1,-1,-9,-8,-2,6,-1,2,-9,-4,-2,6,7],[-1,-7,6,-3,3,-5,-2,7,-7,-4,2,-9,-2]],[[1,1,10,-4,2,-4,-6,-8,5,-9,9,3,-5],[9,-3,7,6,3,-9,-2,-6,7,-3,-4,4,-3],[1,8,-2,2,-7,9,-8,-9,7,7,8,-5,6],[9,7,4,-9,4,3,-5,8,6,-8,2,-8,9],[10,7,7,7,-10,-2,5,-8,-3,-9,-9,-6,1],[2,-6,5,9,1,10,10,10,8,-7,6,-1,2],[1,9,-7,-1,-4,-8,-8,8,8,7,9,5,-4],[-3,-9,9,4,-4,-8,1,-1,6,-9,-9,-4,5],[4,7,-5,4,-7,4,8,-10,2,2,-10,5,3],[-6,-8,10,5,9,8,-1,-4,-6,-2,-3,-8,8]],[[-1,9,6,-3,-8,-6,10,10,1,-5,-8,-9,7],[-7,-7,7,7,-4,-3,7,1,4,-3,1,10,8],[7,8,-1,3,9,6,7,-1,8,-2,5,10,4],[1,7,10,9,10,-5,8,2,-4,-3,-9,-4,9],[9,-7,-9,5,-8,-2,6,-6,2,7,-7,2,7],[-2,2,-10,9,4,-6,7,-5,-10,8,4,-2,-5],[3,1,-9,-2,-4,-2,2,2,4,-1,-8,-1,-6],[6,7,7,9,1,10,-8,8,7,5,-5,1,-1],[-6,5,9,-2,-3,8,6,7,-5,-2,7,10,-3],[5,2,2,10,3,-9,8,1,-3,9,7,-6,-6]],[[10,-7,4,6,-7,5,-8,-9,-3,-8,-4,3,10],[7,9,-9,1,2,7,1,-8,1,7,4,6,-4],[2,4,-7,10,-6,7,-4,-3,8,-4,2,-4,-3],[7,-10,-10,8,6,6,-5,4,2,-2,-10,-8,-1],[-10,-9,5,10,7,-10,3,2,2,4,1,8,10],[6,-2,8,3,-5,-3,6,5,5,-1,-9,-4,1],[-8,9,-6,-4,5,10,-1,-6,2,-2,-7,-6,4],[1,8,-3,8,-2,8,-3,-2,-1,-10,7,1,8],[8,6,9,2,-9,6,7,-2,-8,6,-9,-2,5],[8,3,-4,10,-5,-7,-10,9,6,6,1,-4,-3]],[[-5,2,8,-6,8,2,-9,-10,-3,5,-6,8,-10],[5,7,6,5,-1,-10,4,6,7,-2,-6,-7,6],[3,-5,-6,-6,8,-6,2,8,6,-9,7,-10,2],[3,-8,-3,7,-5,-8,-6,4,1,-9,7,10,-8],[3,3,7,-7,7,7,7,6,4,4,-4,-4,-4],[8,9,1,7,1,10,-8,-7,-2,6,2,8,8],[2,6,-4,-2,-2,9,4,3,8,-4,6,-1,-2],[4,8,-3,-7,8,3,6,-10,-7,5,-10,-3,5],[-10,4,9,1,4,-10,3,2,-8,5,3,2,-2],[-8,9,-4,2,-1,8,2,8,-2,-2,8,3,7]],[[5,-6,6,-4,9,-5,6,6,8,5,-10,6,1],[1,9,-2,9,-3,-3,-1,-3,-5,-2,4,-7,-5],[-7,-10,-7,4,10,2,5,-4,10,-1,4,5,-7],[6,-9,-2,4,-7,-2,8,-1,1,6,6,-5,-1],[5,4,5,7,-3,-2,-2,1,-4,-7,-1,-10,-8],[-3,3,1,-1,9,5,10,6,8,-3,-3,-7,-1],[-1,-5,7,-9,3,-10,4,-8,5,8,2,-9,-2],[3,5,8,-4,2,-1,6,10,6,-5,-5,-6,2],[-9,-4,-7,2,10,-5,-3,10,9,-9,9,-5,4],[5,-2,-10,9,-4,3,-8,6,-9,-10,6,-2,10]],[[-2,6,-4,-6,9,9,-7,4,-9,-3,6,7,-1],[-5,7,6,10,-5,-4,-1,4,9,-3,3,7,-8],[-10,-1,7,3,3,3,-3,8,-7,8,-10,-3,4],[-4,2,6,-6,-2,-2,7,6,9,-6,7,-7,-5],[6,10,5,-2,6,8,4,-5,7,-2,-9,4,-9],[3,8,10,7,5,-4,9,-3,-3,9,3,-7,-8],[-7,6,-3,-1,8,-8,-1,-8,-8,-6,6,-9,-7],[-8,9,-3,-8,2,1,-4,-7,5,-5,-3,-10,5],[-10,10,7,2,-3,4,-5,3,-2,-4,-9,-6,-1],[-7,-10,6,7,5,-3,-1,3,8,-4,5,-9,-4]],[[7,-3,1,-9,4,-2,1,-6,6,3,-5,-7,-3],[6,1,-10,-1,7,7,-4,-1,-2,6,9,7,1],[-2,-2,1,8,-1,-2,-3,6,-5,9,-9,-8,-8],[6,8,9,6,-6,-1,-8,-3,5,-9,6,-3,10],[9,-6,-7,-4,10,7,-5,2,7,10,-2,8,6],[-5,-2,-1,-7,7,7,-10,-7,2,2,-9,6,1],[-4,9,-6,9,1,8,-6,1,8,-2,-10,6,8],[3,5,-2,-6,1,7,-9,-1,-6,1,2,-1,-4],[-9,-5,8,-5,-5,-3,7,-2,-3,3,-7,1,-8],[-9,7,2,-4,7,6,-6,-8,-1,-1,9,3,8]],[[-3,-7,-1,-10,8,6,-8,5,-4,4,-9,7,7],[6,10,-9,4,-1,-10,5,4,3,6,-7,-8,2],[-7,7,-7,-5,6,7,10,5,1,-10,-3,7,1],[-10,7,6,3,10,-6,-6,-1,-2,-2,-10,9,8],[-1,1,-8,-10,-5,1,-10,9,-9,8,-9,-8,-9],[4,6,-2,-6,10,-6,-1,9,-10,-6,-4,-5,3],[-5,2,1,2,7,-6,-8,7,9,6,1,-6,4],[-1,4,-2,-7,3,-2,5,10,2,-10,-2,6,-4],[4,3,-1,9,-8,-4,-7,3,3,-9,-9,-3,-8],[5,-4,3,2,10,-2,-7,-1,-7,10,-8,-6,-6]],[[-5,-6,-3,-1,2,7,-3,7,5,8,-7,-4,5],[-7,-8,7,-3,10,-4,5,6,1,-8,-5,-2,-10],[-7,5,-6,-2,7,-10,4,6,-1,-5,-2,4,-5],[-4,-1,-6,-9,-2,-3,-3,-6,1,-3,8,-10,2],[-9,4,7,-1,-4,-9,-7,-10,-5,-1,6,-3,-10],[6,3,-2,4,8,-3,2,-7,-10,1,-7,5,-9],[1,-1,-2,9,-4,-10,4,-10,1,4,-2,-4,-6],[-1,-8,-3,2,-8,-2,-10,7,-5,-1,9,6,10],[10,2,5,-9,4,4,6,10,10,-4,-1,-7,3],[-2,1,-10,-8,-9,6,7,-9,-5,2,3,-5,-6]],[[-8,-9,-9,2,5,-1,4,5,7,9,-3,-3,10],[-5,-4,3,4,-5,-5,4,-8,-2,-6,-4,8,-1],[8,6,-1,-4,1,-7,9,9,10,3,-2,-2,-1],[3,10,2,9,5,-6,7,6,2,7,-1,-9,-4],[-9,-1,-3,-2,10,8,-2,1,3,5,1,7,3],[4,-2,4,5,2,10,8,7,-3,-10,-9,2,2],[-3,3,9,-9,4,-10,9,-6,7,-10,3,-3,8],[5,6,-5,-10,-7,4,8,1,8,2,-8,-9,5],[-4,4,-10,3,-10,-9,5,-7,-3,-10,5,-2,-1],[7,-1,-1,-1,-8,-5,1,7,6,-5,4,10,-2]]], dtype = "int8")#candidate|9361|(11, 10, 13)|const|int8
var_9362 = relay.var("var_9362", dtype = "int8", shape = (11, 10, 13))#candidate|9362|(11, 10, 13)|var|int8
bop_9363 = relay.equal(const_9361.astype('bool'), relay.reshape(var_9362.astype('bool'), relay.shape_of(const_9361))) # shape=(11, 10, 13)
func_5816_call = mod.get_global_var('func_5816')
func_5818_call = mutated_mod.get_global_var('func_5818')
call_9379 = relay.TupleGetItem(func_5816_call(), 0)
call_9380 = relay.TupleGetItem(func_5818_call(), 0)
func_9018_call = mod.get_global_var('func_9018')
func_9020_call = mutated_mod.get_global_var('func_9020')
call_9383 = func_9018_call()
call_9384 = func_9018_call()
func_7132_call = mod.get_global_var('func_7132')
func_7138_call = mutated_mod.get_global_var('func_7138')
const_9390 = relay.const([-10,5,-3,-3,-1,3,-4,-5,-9,-9,9,7,10,-1,8,-4,-10,10,-10,-6,-3,2,-7,6,-8,-3,10,8,-1,4,-1,-6,7,-6,8,9,8,1,-8,3,1,-5,-10,-4,-4,-8,5,7,1,3,3,1,3,9,8,-7,10,1,-5,-10,-3,5,4,4,-5,-5,8,2,-7,-3,4,5,10,-5,10,5,4,3,-1,-3,3,5,-3,3,7,-6,-7,-7,6,-3,7,-2,-7,-1,4,-7,2,-8,-10,-5,-8,9,2,4,8,-6,5,-8,-5,-3,2,3,3,-9,4,-9,2,10,4,2,1,-6,6,-1,2,-7,3,8,-3,8,-8,-2,6,6,5,-1,8,5,3,4,-9,2,2,9,-7,-5,-5,-7,8,-9,3,-1,1,-4,1,2,10,-3,3,10,-8,-3,9,-4,-5,-1,-4,9,8,10,1,9,-5,4,4,-6,-8,-7,-2,5,3,6,-8,-3,-10,6,-6,-3,-7,8,2,8,-6,-8,-4,-6,8,-6,-8,-3,-3,-10,-3,-1,1,-4,7,4,6,4,2,9,-3,-6,-6,-9,-7,-10,-3,3,-2,10,10,3,-3,-6,-8,-7,-1,-3,-4,-8,3,-5,8,-2,-6,10,-6,2,1,-6,-4,-9,6,2,4,4,7,-6,5,7,-2,-7,-3,8,6,2,-7,-5,-5,-4,8,-8,5,-1,-6,4,-9,-6,2,6,-8,-10,-1,7,-5,-5,-6,9,1,-4,10,4,-2,2,4,4,6,4,-2,-3,9,7,5,1,-7,2,4,9,-4,-2,8,-10,-1,-4,-3,-7,9,2,-1,7,-7,-5,4,-8,4,-7,-5,9,-1,-8,-1,1,-8,-1,5,7,8,-4,8,1,4,-4,-6,5,-5,-4,-8,4,5,7,5,3,-9,-6,-2,7,-8,5,4,-1,-4,3,7,10,-5,3,4,-5,-4,-10,-1,-10,-9,-1,6,-2,-5,2,4,-4,-2,9,3,-1,-7,1,7,5,6,-9,-7,5,-5,6,1,-8,-6,-9,5,6,-10,-9,10,-2,-3,-1,3,-4,2,-8,9,8,-7,6,8,3,1,-4,8,-7,1,1,5,10,5,-2,8,-10,6,4,-8,-9,-10,9,-1,1,8,5,7,-1,-5,-5,-3,-7,-2,3,9,10,7,7,8,1,10,-1,3,-9,7,1,-2,-8,-1,-4,-5,2,-4,1,9,-1,-9,-5,-4,-1,2,-10,-4,7,-9,8,5,-7,8,-4,3,-5,-6,5,9,-1,-9,5,1,-1,-7,6,8,3,-1,-5,10,7,4,-8,-9,6,-1,-3,7,3,-2,5,2,8,-5,-10,-4,-1,-10,-3,-9,10,2,-2,-7,10,-4,1,-3,1,-3,2,-7,-10,-5,7,2,4,1,2,1,-1,-8,-2,3,-10,-4,8,9,-10,8,6,5,5,-8,-5,-8,-5,-9,9,10,-10,2,-8,3,5,3,3,-3,-3,-5,9,5,2,-1,-5,10,7,-3,-3,1,10,-9,-4,-3,-1,-7,6,4,-5,-10,-8,-6,-2,-2,-7,-5,8,2,-6,3,7,-10,4,-2,-1,-9,-3,-7,-6,-2,-1,2,2,-3,10,8,8,2,-5,10,9,8,6,8,2,7,-8,-3,2,1,-4,3,10,-3,-2,-3,-2,-4,4,-2,-6,10,-9,-6,-8,5,7,-1,5,-2,-7,-9,-3,9,9,-4,4,8,-6,4,-1,-6,-9,5,-3,1,9,-10,7,2,3,-10,9,-10,-10,8,5,10,-1,6,-2,-3,-8,-5,-4,-10,4,-6,8,7,2,1,-1,9,-8,5,3,2,3,-8,-6,-4,8,3,-5,6,-8,-5,10,1,9,7,-8,-3,6,-7,-10,1,2,6,6,7,8,3,5,5,3,-4,-1,-1,-8,7,1,8,2,3,3,-2,-1,1,10,-10,8,-4,-2,-3,-3,-8,10,10,-9,10,2,-5,8,8,1,-2,3,5,-1,6,1,-8,10,-3,-10,1,8,4,-1,5,-2,1,3,9,-6,-7,10,10,-5,9,7,-7,7,10,-8,1,3,5,10,1,-10,-5,-6,-10,-9,8,8,-10,1,-4,6,-8,7,-7,7,5,6,8,6,-5,-7,-10,10,-2,1,-9,1,-7,1,5,10,5,-9,-8,-1,9,-5,4,8,-6,10,-7,-1,1,-8,9,-6,4,9,2,4,-9,8,-6,-9,-7,-6,-2,-1,-10,-1,7,-7,-5,-2,10,8,-6,-5,7,5,-3,-10,-1,-9,-10,-1,-8,-7,-7,-1], dtype = "int8")#candidate|9390|(864,)|const|int8
var_9391 = relay.var("var_9391", dtype = "int64", shape = (630,))#candidate|9391|(630,)|var|int64
var_9392 = relay.var("var_9392", dtype = "bool", shape = (1120,))#candidate|9392|(1120,)|var|bool
var_9393 = relay.var("var_9393", dtype = "float32", shape = (180, 1))#candidate|9393|(180, 1)|var|float32
call_9389 = relay.TupleGetItem(func_7132_call(relay.reshape(const_9390.astype('int8'), [8, 9, 12]), relay.reshape(var_9391.astype('int64'), [630,]), relay.reshape(var_9392.astype('bool'), [1, 1120]), relay.reshape(var_9393.astype('float32'), [180,]), ), 3)
call_9394 = relay.TupleGetItem(func_7138_call(relay.reshape(const_9390.astype('int8'), [8, 9, 12]), relay.reshape(var_9391.astype('int64'), [630,]), relay.reshape(var_9392.astype('bool'), [1, 1120]), relay.reshape(var_9393.astype('float32'), [180,]), ), 3)
output = relay.Tuple([bop_9363,call_9379,call_9383,call_9389,const_9390,var_9391,var_9392,var_9393,])
output2 = relay.Tuple([bop_9363,call_9380,call_9384,call_9394,const_9390,var_9391,var_9392,var_9393,])
func_9396 = relay.Function([var_9362,var_9391,var_9392,var_9393,], output)
mod['func_9396'] = func_9396
mod = relay.transform.InferType()(mod)
mutated_mod['func_9396'] = func_9396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9396_call = mutated_mod.get_global_var('func_9396')
var_9398 = relay.var("var_9398", dtype = "int8", shape = (11, 10, 13))#candidate|9398|(11, 10, 13)|var|int8
var_9399 = relay.var("var_9399", dtype = "int64", shape = (630,))#candidate|9399|(630,)|var|int64
var_9400 = relay.var("var_9400", dtype = "bool", shape = (1120,))#candidate|9400|(1120,)|var|bool
var_9401 = relay.var("var_9401", dtype = "float32", shape = (180, 1))#candidate|9401|(180, 1)|var|float32
call_9397 = func_9396_call(var_9398,var_9399,var_9400,var_9401,)
output = call_9397
func_9402 = relay.Function([var_9398,var_9399,var_9400,var_9401,], output)
mutated_mod['func_9402'] = func_9402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6429_call = mod.get_global_var('func_6429')
func_6430_call = mutated_mod.get_global_var('func_6430')
call_9437 = func_6429_call()
call_9438 = func_6429_call()
output = relay.Tuple([call_9437,])
output2 = relay.Tuple([call_9438,])
func_9449 = relay.Function([], output)
mod['func_9449'] = func_9449
mod = relay.transform.InferType()(mod)
output = func_9449()
func_9450 = relay.Function([], output)
mutated_mod['func_9450'] = func_9450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9472 = relay.var("var_9472", dtype = "float64", shape = (14, 13, 6))#candidate|9472|(14, 13, 6)|var|float64
uop_9473 = relay.erf(var_9472.astype('float64')) # shape=(14, 13, 6)
func_8891_call = mod.get_global_var('func_8891')
func_8893_call = mutated_mod.get_global_var('func_8893')
call_9480 = relay.TupleGetItem(func_8891_call(), 0)
call_9481 = relay.TupleGetItem(func_8893_call(), 0)
bop_9488 = relay.left_shift(uop_9473.astype('uint64'), relay.reshape(var_9472.astype('uint64'), relay.shape_of(uop_9473))) # shape=(14, 13, 6)
output = relay.Tuple([call_9480,bop_9488,])
output2 = relay.Tuple([call_9481,bop_9488,])
func_9494 = relay.Function([var_9472,], output)
mod['func_9494'] = func_9494
mod = relay.transform.InferType()(mod)
var_9495 = relay.var("var_9495", dtype = "float64", shape = (14, 13, 6))#candidate|9495|(14, 13, 6)|var|float64
output = func_9494(var_9495)
func_9496 = relay.Function([var_9495], output)
mutated_mod['func_9496'] = func_9496
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9691 = relay.var("var_9691", dtype = "float64", shape = ())#candidate|9691|()|var|float64
const_9692 = relay.const([[[1.434855,-0.460000,9.757353,6.802131,-2.034872,9.948533,-9.148099,3.688743,-2.568347,8.752210,3.399630,-0.424200],[-2.291570,0.380747,-2.325543,4.883888,5.980989,-7.644480,3.279857,6.288468,-3.454038,-4.674978,4.999378,-5.943863],[-2.302777,1.609764,1.282451,6.666970,7.437731,-8.207754,8.816618,8.511549,7.885146,3.246933,5.904234,7.562843],[1.919642,-5.511378,9.632330,-3.828210,1.941650,-0.992589,-7.485849,-6.224131,-1.150406,3.999010,-0.780299,-8.104247],[-8.959993,-1.551856,-2.376275,0.429646,-0.481042,-5.874045,-3.221559,7.663082,-6.983696,4.120597,0.699393,-0.811538],[-0.354015,-8.002691,-2.063907,8.448501,-6.860787,2.193946,0.586194,0.625392,-7.940744,5.995985,-2.083111,-8.814946],[-5.299829,0.997425,0.439734,5.781716,4.319697,-6.558295,-1.222275,9.636115,-9.388714,5.445832,6.500903,3.312405],[-9.686969,9.642358,2.534581,8.143682,6.288960,-3.022629,-1.419398,-8.598547,9.769689,-8.795461,-7.573688,-0.367498],[-6.656555,-8.846946,-4.600313,2.501967,7.329796,-3.475723,8.036118,-4.877318,-3.964374,9.535782,8.770718,6.661882],[6.267225,-3.874342,6.477270,-2.690283,9.846308,5.335416,-7.834058,-7.880916,1.929729,-4.245157,1.022913,2.180435],[1.716451,-7.321139,5.870210,2.752759,8.064016,-9.872353,9.883670,-5.895733,-7.293575,-6.676462,7.065953,-0.874291],[4.216160,5.491180,9.272034,1.864542,9.087765,2.221662,4.495991,1.167703,3.383070,1.671611,-9.352308,1.677514],[4.422407,5.174443,-2.117706,-0.898453,0.646629,-2.733989,-1.572789,8.094788,-2.980539,-9.504176,-7.767814,-5.652850]]], dtype = "float64")#candidate|9692|(1, 13, 12)|const|float64
bop_9693 = relay.floor_divide(var_9691.astype('float64'), const_9692.astype('float64')) # shape=(1, 13, 12)
uop_9700 = relay.acosh(bop_9693.astype('float64')) # shape=(1, 13, 12)
output = uop_9700
output2 = uop_9700
func_9714 = relay.Function([var_9691,], output)
mod['func_9714'] = func_9714
mod = relay.transform.InferType()(mod)
var_9715 = relay.var("var_9715", dtype = "float64", shape = ())#candidate|9715|()|var|float64
output = func_9714(var_9715)
func_9716 = relay.Function([var_9715], output)
mutated_mod['func_9716'] = func_9716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_9754 = relay.TupleGetItem(func_5993_call(), 0)
call_9755 = relay.TupleGetItem(func_5995_call(), 0)
output = relay.Tuple([call_9754,])
output2 = relay.Tuple([call_9755,])
func_9773 = relay.Function([], output)
mod['func_9773'] = func_9773
mod = relay.transform.InferType()(mod)
output = func_9773()
func_9774 = relay.Function([], output)
mutated_mod['func_9774'] = func_9774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5932_call = mod.get_global_var('func_5932')
func_5934_call = mutated_mod.get_global_var('func_5934')
call_9974 = func_5932_call()
call_9975 = func_5932_call()
func_6813_call = mod.get_global_var('func_6813')
func_6815_call = mutated_mod.get_global_var('func_6815')
call_9976 = relay.TupleGetItem(func_6813_call(), 0)
call_9977 = relay.TupleGetItem(func_6815_call(), 0)
output = relay.Tuple([call_9974,call_9976,])
output2 = relay.Tuple([call_9975,call_9977,])
func_9979 = relay.Function([], output)
mod['func_9979'] = func_9979
mod = relay.transform.InferType()(mod)
mutated_mod['func_9979'] = func_9979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9979_call = mutated_mod.get_global_var('func_9979')
call_9980 = func_9979_call()
output = call_9980
func_9981 = relay.Function([], output)
mutated_mod['func_9981'] = func_9981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8891_call = mod.get_global_var('func_8891')
func_8893_call = mutated_mod.get_global_var('func_8893')
call_10007 = relay.TupleGetItem(func_8891_call(), 0)
call_10008 = relay.TupleGetItem(func_8893_call(), 0)
func_5104_call = mod.get_global_var('func_5104')
func_5106_call = mutated_mod.get_global_var('func_5106')
call_10010 = relay.TupleGetItem(func_5104_call(), 0)
call_10011 = relay.TupleGetItem(func_5106_call(), 0)
func_8556_call = mod.get_global_var('func_8556')
func_8557_call = mutated_mod.get_global_var('func_8557')
call_10017 = relay.TupleGetItem(func_8556_call(), 0)
call_10018 = relay.TupleGetItem(func_8557_call(), 0)
func_9449_call = mod.get_global_var('func_9449')
func_9450_call = mutated_mod.get_global_var('func_9450')
call_10019 = relay.TupleGetItem(func_9449_call(), 0)
call_10020 = relay.TupleGetItem(func_9450_call(), 0)
output = relay.Tuple([call_10007,call_10010,call_10017,call_10019,])
output2 = relay.Tuple([call_10008,call_10011,call_10018,call_10020,])
func_10022 = relay.Function([], output)
mod['func_10022'] = func_10022
mod = relay.transform.InferType()(mod)
output = func_10022()
func_10023 = relay.Function([], output)
mutated_mod['func_10023'] = func_10023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7854_call = mod.get_global_var('func_7854')
func_7856_call = mutated_mod.get_global_var('func_7856')
call_10068 = relay.TupleGetItem(func_7854_call(), 0)
call_10069 = relay.TupleGetItem(func_7856_call(), 0)
output = call_10068
output2 = call_10069
func_10085 = relay.Function([], output)
mod['func_10085'] = func_10085
mod = relay.transform.InferType()(mod)
mutated_mod['func_10085'] = func_10085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10085_call = mutated_mod.get_global_var('func_10085')
call_10086 = func_10085_call()
output = call_10086
func_10087 = relay.Function([], output)
mutated_mod['func_10087'] = func_10087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8258_call = mod.get_global_var('func_8258')
func_8259_call = mutated_mod.get_global_var('func_8259')
call_10186 = relay.TupleGetItem(func_8258_call(), 0)
call_10187 = relay.TupleGetItem(func_8259_call(), 0)
output = call_10186
output2 = call_10187
func_10188 = relay.Function([], output)
mod['func_10188'] = func_10188
mod = relay.transform.InferType()(mod)
mutated_mod['func_10188'] = func_10188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10188_call = mutated_mod.get_global_var('func_10188')
call_10189 = func_10188_call()
output = call_10189
func_10190 = relay.Function([], output)
mutated_mod['func_10190'] = func_10190
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10227 = relay.var("var_10227", dtype = "bool", shape = (6, 2, 11))#candidate|10227|(6, 2, 11)|var|bool
var_10228 = relay.var("var_10228", dtype = "bool", shape = (6, 2, 11))#candidate|10228|(6, 2, 11)|var|bool
bop_10229 = relay.logical_and(var_10227.astype('bool'), relay.reshape(var_10228.astype('bool'), relay.shape_of(var_10227))) # shape=(6, 2, 11)
output = bop_10229
output2 = bop_10229
func_10236 = relay.Function([var_10227,var_10228,], output)
mod['func_10236'] = func_10236
mod = relay.transform.InferType()(mod)
mutated_mod['func_10236'] = func_10236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10236_call = mutated_mod.get_global_var('func_10236')
var_10238 = relay.var("var_10238", dtype = "bool", shape = (6, 2, 11))#candidate|10238|(6, 2, 11)|var|bool
var_10239 = relay.var("var_10239", dtype = "bool", shape = (6, 2, 11))#candidate|10239|(6, 2, 11)|var|bool
call_10237 = func_10236_call(var_10238,var_10239,)
output = call_10237
func_10240 = relay.Function([var_10238,var_10239,], output)
mutated_mod['func_10240'] = func_10240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9193_call = mod.get_global_var('func_9193')
func_9194_call = mutated_mod.get_global_var('func_9194')
call_10263 = func_9193_call()
call_10264 = func_9193_call()
func_10022_call = mod.get_global_var('func_10022')
func_10023_call = mutated_mod.get_global_var('func_10023')
call_10266 = relay.TupleGetItem(func_10022_call(), 0)
call_10267 = relay.TupleGetItem(func_10023_call(), 0)
func_9773_call = mod.get_global_var('func_9773')
func_9774_call = mutated_mod.get_global_var('func_9774')
call_10268 = relay.TupleGetItem(func_9773_call(), 0)
call_10269 = relay.TupleGetItem(func_9774_call(), 0)
output = relay.Tuple([call_10263,call_10266,call_10268,])
output2 = relay.Tuple([call_10264,call_10267,call_10269,])
func_10278 = relay.Function([], output)
mod['func_10278'] = func_10278
mod = relay.transform.InferType()(mod)
output = func_10278()
func_10279 = relay.Function([], output)
mutated_mod['func_10279'] = func_10279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6611_call = mod.get_global_var('func_6611')
func_6612_call = mutated_mod.get_global_var('func_6612')
call_10298 = relay.TupleGetItem(func_6611_call(), 0)
call_10299 = relay.TupleGetItem(func_6612_call(), 0)
output = call_10298
output2 = call_10299
func_10300 = relay.Function([], output)
mod['func_10300'] = func_10300
mod = relay.transform.InferType()(mod)
output = func_10300()
func_10301 = relay.Function([], output)
mutated_mod['func_10301'] = func_10301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10022_call = mod.get_global_var('func_10022')
func_10023_call = mutated_mod.get_global_var('func_10023')
call_10312 = relay.TupleGetItem(func_10022_call(), 2)
call_10313 = relay.TupleGetItem(func_10023_call(), 2)
func_5582_call = mod.get_global_var('func_5582')
func_5584_call = mutated_mod.get_global_var('func_5584')
const_10333 = relay.const([-6,-4,10,2,-10,-2,-9,-6,-6,-6,10,10,2,-6,10,7,-6,-1,-5,-10,7,-6,8,5,-7,-10,3,-8,8,5,3,7,4,-6,3,4,10,10,9,4,6,-4,6,5,6,-5,3,8,2,-6,2,6,-9,-3,-2,6,-1,-1,10,2,-8,-5,-8,10,-7,-4,-6,2,-7,-4,2,-10,-10,-9,-7,-6,-7,-9,4,-3,-8,9,-7,1,-5,-6,-7,-9,7,7,10,-2,6,2,-1,-10,-1,-4,9,-4,-10,-1,-7,2,-10,-10,4,-7,-3,8,-1,-2,-7,-3,-2,3,5,9,-4,-6,1,5,9,-6,9,6,-2,4,-7,-8,-4,-10,-4,-3,-1,-5,6,-10,9,7,9,10,2,-3,-3,-7,-1,-5,6,-5,8,3,-9,-9,6,8,9,-9,6,-9,4,-5,1,-1,-10,7,-4,2,-1,2,8,7,10,8,9,-4,-1,9,8,2,4,-6,10,-2,2,10,-5,-7,2,-10,1,5,4,-6,2,2,7,-4,7,-8,1,-9,7,-3,9,2,-9,6,1,-6,9,-8,-8,-3,-2,4,-1,2,-6,8,10,9,-7,5,-6,10,10,4,-4,-3,-2,-2,7,-10,10,-2,8,-2,-8,-2,9,-2,9,7,4,2,6,-8,9,-9,8,9], dtype = "uint8")#candidate|10333|(252,)|const|uint8
call_10332 = relay.TupleGetItem(func_5582_call(relay.reshape(const_10333.astype('uint8'), [252,])), 2)
call_10334 = relay.TupleGetItem(func_5584_call(relay.reshape(const_10333.astype('uint8'), [252,])), 2)
func_5958_call = mod.get_global_var('func_5958')
func_5961_call = mutated_mod.get_global_var('func_5961')
var_10347 = relay.var("var_10347", dtype = "float32", shape = (4, 2))#candidate|10347|(4, 2)|var|float32
call_10346 = relay.TupleGetItem(func_5958_call(relay.reshape(var_10347.astype('float32'), [8, 1])), 0)
call_10348 = relay.TupleGetItem(func_5961_call(relay.reshape(var_10347.astype('float32'), [8, 1])), 0)
func_5730_call = mod.get_global_var('func_5730')
func_5732_call = mutated_mod.get_global_var('func_5732')
var_10351 = relay.var("var_10351", dtype = "float32", shape = (180,))#candidate|10351|(180,)|var|float32
call_10350 = relay.TupleGetItem(func_5730_call(relay.reshape(var_10351.astype('float32'), [6, 30])), 1)
call_10352 = relay.TupleGetItem(func_5732_call(relay.reshape(var_10351.astype('float32'), [6, 30])), 1)
bop_10367 = relay.bitwise_and(call_10350.astype('uint64'), relay.reshape(var_10351.astype('uint64'), relay.shape_of(call_10350))) # shape=(90, 2)
bop_10370 = relay.bitwise_and(call_10352.astype('uint64'), relay.reshape(var_10351.astype('uint64'), relay.shape_of(call_10352))) # shape=(90, 2)
output = relay.Tuple([call_10312,call_10332,const_10333,call_10346,var_10347,bop_10367,])
output2 = relay.Tuple([call_10313,call_10334,const_10333,call_10348,var_10347,bop_10370,])
func_10376 = relay.Function([var_10347,var_10351,], output)
mod['func_10376'] = func_10376
mod = relay.transform.InferType()(mod)
var_10377 = relay.var("var_10377", dtype = "float32", shape = (4, 2))#candidate|10377|(4, 2)|var|float32
var_10378 = relay.var("var_10378", dtype = "float32", shape = (180,))#candidate|10378|(180,)|var|float32
output = func_10376(var_10377,var_10378,)
func_10379 = relay.Function([var_10377,var_10378,], output)
mutated_mod['func_10379'] = func_10379
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10404 = relay.const(True, dtype = "bool")#candidate|10404|()|const|bool
const_10405 = relay.const([[[False,False,True,False,True,True,True,True,True],[False,False,False,True,False,True,True,True,False],[False,True,True,True,False,True,False,False,True],[False,True,True,False,True,True,True,True,False],[False,True,False,True,True,False,False,False,True],[True,True,False,True,False,True,False,True,False],[False,True,False,True,False,True,False,False,False],[True,False,False,True,False,True,True,False,False],[False,False,True,True,True,False,True,False,False],[True,False,False,True,False,True,True,True,True],[False,True,False,False,False,False,False,False,False],[True,True,False,False,True,False,True,False,True],[True,False,True,False,True,False,False,False,False],[True,True,False,True,True,True,True,True,False],[True,False,False,True,True,True,False,True,True],[False,False,True,False,False,True,True,False,False]]], dtype = "bool")#candidate|10405|(1, 16, 9)|const|bool
bop_10406 = relay.logical_or(const_10404.astype('bool'), const_10405.astype('bool')) # shape=(1, 16, 9)
output = relay.Tuple([bop_10406,])
output2 = relay.Tuple([bop_10406,])
func_10413 = relay.Function([], output)
mod['func_10413'] = func_10413
mod = relay.transform.InferType()(mod)
output = func_10413()
func_10414 = relay.Function([], output)
mutated_mod['func_10414'] = func_10414
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10477 = relay.var("var_10477", dtype = "float64", shape = (1, 10, 8))#candidate|10477|(1, 10, 8)|var|float64
uop_10478 = relay.exp(var_10477.astype('float64')) # shape=(1, 10, 8)
output = relay.Tuple([uop_10478,])
output2 = relay.Tuple([uop_10478,])
func_10480 = relay.Function([var_10477,], output)
mod['func_10480'] = func_10480
mod = relay.transform.InferType()(mod)
var_10481 = relay.var("var_10481", dtype = "float64", shape = (1, 10, 8))#candidate|10481|(1, 10, 8)|var|float64
output = func_10480(var_10481)
func_10482 = relay.Function([var_10481], output)
mutated_mod['func_10482'] = func_10482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6769_call = mod.get_global_var('func_6769')
func_6771_call = mutated_mod.get_global_var('func_6771')
call_10492 = func_6769_call()
call_10493 = func_6769_call()
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_10520 = relay.TupleGetItem(func_5993_call(), 0)
call_10521 = relay.TupleGetItem(func_5995_call(), 0)
func_8556_call = mod.get_global_var('func_8556')
func_8557_call = mutated_mod.get_global_var('func_8557')
call_10534 = relay.TupleGetItem(func_8556_call(), 0)
call_10535 = relay.TupleGetItem(func_8557_call(), 0)
func_6813_call = mod.get_global_var('func_6813')
func_6815_call = mutated_mod.get_global_var('func_6815')
call_10536 = relay.TupleGetItem(func_6813_call(), 0)
call_10537 = relay.TupleGetItem(func_6815_call(), 0)
output = relay.Tuple([call_10492,call_10520,call_10534,call_10536,])
output2 = relay.Tuple([call_10493,call_10521,call_10535,call_10537,])
func_10544 = relay.Function([], output)
mod['func_10544'] = func_10544
mod = relay.transform.InferType()(mod)
output = func_10544()
func_10545 = relay.Function([], output)
mutated_mod['func_10545'] = func_10545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7239_call = mod.get_global_var('func_7239')
func_7240_call = mutated_mod.get_global_var('func_7240')
call_10594 = relay.TupleGetItem(func_7239_call(), 0)
call_10595 = relay.TupleGetItem(func_7240_call(), 0)
output = relay.Tuple([call_10594,])
output2 = relay.Tuple([call_10595,])
func_10615 = relay.Function([], output)
mod['func_10615'] = func_10615
mod = relay.transform.InferType()(mod)
mutated_mod['func_10615'] = func_10615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10615_call = mutated_mod.get_global_var('func_10615')
call_10616 = func_10615_call()
output = call_10616
func_10617 = relay.Function([], output)
mutated_mod['func_10617'] = func_10617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7051_call = mod.get_global_var('func_7051')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_10681 = func_7051_call()
call_10682 = func_7051_call()
output = call_10681
output2 = call_10682
func_10708 = relay.Function([], output)
mod['func_10708'] = func_10708
mod = relay.transform.InferType()(mod)
output = func_10708()
func_10709 = relay.Function([], output)
mutated_mod['func_10709'] = func_10709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7786_call = mod.get_global_var('func_7786')
func_7788_call = mutated_mod.get_global_var('func_7788')
call_10728 = relay.TupleGetItem(func_7786_call(), 1)
call_10729 = relay.TupleGetItem(func_7788_call(), 1)
func_10022_call = mod.get_global_var('func_10022')
func_10023_call = mutated_mod.get_global_var('func_10023')
call_10735 = relay.TupleGetItem(func_10022_call(), 2)
call_10736 = relay.TupleGetItem(func_10023_call(), 2)
output = relay.Tuple([call_10728,call_10735,])
output2 = relay.Tuple([call_10729,call_10736,])
func_10742 = relay.Function([], output)
mod['func_10742'] = func_10742
mod = relay.transform.InferType()(mod)
output = func_10742()
func_10743 = relay.Function([], output)
mutated_mod['func_10743'] = func_10743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10750 = relay.var("var_10750", dtype = "uint64", shape = (16, 4, 13))#candidate|10750|(16, 4, 13)|var|uint64
const_10751 = relay.const([[[4,-9,3,7,-7,8,4,4,-7,6,3,7,-6],[8,8,9,-6,-4,6,4,6,-3,7,10,-10,-3],[10,-3,-9,-10,1,-1,-10,5,-8,-7,-10,-5,-8],[3,3,10,-8,-10,6,-3,1,-3,1,-5,6,5]],[[4,4,-5,1,5,-3,-4,9,3,6,-8,-3,6],[1,-1,5,6,-7,-8,-1,10,5,5,6,6,9],[1,-6,-1,-7,3,10,-5,10,-7,-6,3,3,-3],[-5,10,-6,8,-8,-9,3,-10,9,2,-7,-10,-8]],[[-4,2,-9,-8,-3,-10,6,-1,-6,5,1,-1,5],[4,3,-8,-10,-4,-9,7,-7,-4,6,6,-4,-10],[-6,8,3,7,-1,-2,-7,-1,1,8,-5,-10,10],[7,-10,-8,7,10,-7,5,1,-10,-6,-5,-9,6]],[[7,-6,-6,10,-9,-4,2,8,10,9,1,-10,-10],[-5,-7,-4,-8,1,3,-10,8,9,-8,1,-8,-9],[-10,9,3,-1,-6,-5,5,-8,7,-9,4,7,4],[-1,-8,3,-1,-10,-8,-5,5,-7,-7,-9,5,-9]],[[5,-4,-4,1,-5,-10,9,-1,10,-9,9,7,3],[10,3,8,5,-5,6,1,-2,-10,-10,8,-8,-8],[5,2,-1,-7,-2,-10,-8,6,-3,-7,-7,-10,9],[-10,6,-5,1,-10,-2,7,-5,-10,4,-9,4,-3]],[[-5,9,-10,-1,7,9,3,-2,-8,8,-6,8,-8],[-4,-5,5,-2,3,5,8,10,-2,9,-10,3,-2],[-10,-6,7,1,8,1,-2,2,8,9,-1,3,-5],[9,-4,-6,1,-1,1,-2,9,1,-8,9,6,6]],[[-1,7,5,-5,-5,1,2,-6,-5,-3,2,6,-8],[-7,-4,-2,-5,2,-5,7,9,-7,2,-3,-2,3],[-4,-5,5,9,-7,4,-9,2,-5,-3,-8,5,-4],[9,7,-9,5,5,7,9,4,8,2,-5,-10,3]],[[-9,-10,-7,8,-2,-8,4,-7,5,7,-1,-3,6],[2,-8,-3,-3,1,-1,7,7,-2,-7,2,-5,3],[5,-1,-4,4,-9,-1,8,-4,3,4,-7,1,-7],[7,-5,10,-4,10,5,4,-10,6,-6,-9,-2,-9]],[[1,-2,-6,-2,7,10,2,-3,-3,-1,-1,3,9],[-8,-8,1,-10,10,2,-8,2,4,9,3,4,7],[4,7,-3,-8,6,2,2,4,2,5,-2,-1,6],[-7,9,10,-5,1,-3,-10,-8,-5,-2,6,-2,9]],[[-2,7,4,2,9,1,8,1,-8,-2,-3,7,-7],[9,-6,3,9,-7,7,10,-9,7,10,-1,-1,5],[2,-9,-6,8,7,9,-5,-10,-6,-6,1,4,-5],[4,-10,10,-2,10,-7,2,-10,-3,7,-7,6,-8]],[[9,2,9,-10,4,2,10,6,10,5,-8,5,2],[10,5,6,-4,-8,4,-3,-9,-4,4,-10,7,4],[-4,3,-1,5,-3,-10,1,9,5,2,6,4,-6],[-6,-8,8,-1,9,4,-10,6,5,7,1,-7,-7]],[[-8,4,-5,-7,-3,6,-6,8,8,-8,-9,2,-8],[-9,5,-9,-8,7,5,8,-8,4,1,5,-1,4],[7,-5,8,-3,9,-5,5,10,-5,2,5,9,-9],[5,-9,-9,4,5,-7,4,10,-4,-1,-7,-5,2]],[[-6,-5,-7,-6,-9,7,8,-9,10,-2,3,5,2],[-10,2,8,3,4,4,-8,-2,10,9,-6,1,9],[-8,7,8,-9,-9,10,-2,6,4,-1,-1,8,-10],[-8,6,6,2,4,-3,4,-1,6,1,-1,5,1]],[[3,-5,4,6,1,-4,5,4,-2,-10,3,8,9],[8,3,2,-9,-9,-10,-2,6,5,5,-9,-6,-2],[8,-4,1,-1,-1,10,-9,2,-3,2,4,3,7],[-6,3,-5,-10,-8,-2,5,1,3,6,1,4,1]],[[3,7,5,4,-1,-1,-7,-2,-5,2,4,-5,-5],[-2,-4,-6,6,-10,7,1,2,-1,-8,-9,1,8],[-1,8,3,-4,10,7,-5,8,-10,2,-8,4,7],[10,7,3,-3,3,-8,5,6,5,9,-5,-2,-3]],[[-1,8,-10,-6,-6,-2,-10,7,1,8,-3,3,8],[-1,7,3,-8,-8,9,5,2,6,-4,2,4,5],[6,-1,5,7,5,4,8,4,-5,-5,-8,-3,-4],[8,-6,9,-10,-8,-4,9,-2,-7,-4,-10,-1,7]]], dtype = "uint64")#candidate|10751|(16, 4, 13)|const|uint64
bop_10752 = relay.less_equal(var_10750.astype('bool'), relay.reshape(const_10751.astype('bool'), relay.shape_of(var_10750))) # shape=(16, 4, 13)
uop_10758 = relay.asin(bop_10752.astype('float64')) # shape=(16, 4, 13)
bop_10764 = relay.bitwise_and(uop_10758.astype('int8'), relay.reshape(var_10750.astype('int8'), relay.shape_of(uop_10758))) # shape=(16, 4, 13)
func_8625_call = mod.get_global_var('func_8625')
func_8626_call = mutated_mod.get_global_var('func_8626')
call_10768 = relay.TupleGetItem(func_8625_call(), 0)
call_10769 = relay.TupleGetItem(func_8626_call(), 0)
output = relay.Tuple([bop_10764,call_10768,])
output2 = relay.Tuple([bop_10764,call_10769,])
func_10802 = relay.Function([var_10750,], output)
mod['func_10802'] = func_10802
mod = relay.transform.InferType()(mod)
var_10803 = relay.var("var_10803", dtype = "uint64", shape = (16, 4, 13))#candidate|10803|(16, 4, 13)|var|uint64
output = func_10802(var_10803)
func_10804 = relay.Function([var_10803], output)
mutated_mod['func_10804'] = func_10804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_10843 = relay.TupleGetItem(func_5509_call(), 0)
call_10844 = relay.TupleGetItem(func_5511_call(), 0)
output = relay.Tuple([call_10843,])
output2 = relay.Tuple([call_10844,])
func_10855 = relay.Function([], output)
mod['func_10855'] = func_10855
mod = relay.transform.InferType()(mod)
output = func_10855()
func_10856 = relay.Function([], output)
mutated_mod['func_10856'] = func_10856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mod.get_global_var('func_6126')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_10904 = func_6126_call()
call_10905 = func_6126_call()
func_6885_call = mod.get_global_var('func_6885')
func_6886_call = mutated_mod.get_global_var('func_6886')
call_10909 = relay.TupleGetItem(func_6885_call(), 1)
call_10910 = relay.TupleGetItem(func_6886_call(), 1)
output = relay.Tuple([call_10904,call_10909,])
output2 = relay.Tuple([call_10905,call_10910,])
func_10913 = relay.Function([], output)
mod['func_10913'] = func_10913
mod = relay.transform.InferType()(mod)
output = func_10913()
func_10914 = relay.Function([], output)
mutated_mod['func_10914'] = func_10914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6838_call = mod.get_global_var('func_6838')
func_6840_call = mutated_mod.get_global_var('func_6840')
call_10915 = relay.TupleGetItem(func_6838_call(), 2)
call_10916 = relay.TupleGetItem(func_6840_call(), 2)
func_10022_call = mod.get_global_var('func_10022')
func_10023_call = mutated_mod.get_global_var('func_10023')
call_10917 = relay.TupleGetItem(func_10022_call(), 3)
call_10918 = relay.TupleGetItem(func_10023_call(), 3)
func_10615_call = mod.get_global_var('func_10615')
func_10617_call = mutated_mod.get_global_var('func_10617')
call_10924 = relay.TupleGetItem(func_10615_call(), 0)
call_10925 = relay.TupleGetItem(func_10617_call(), 0)
var_10929 = relay.var("var_10929", dtype = "float64", shape = (15, 8, 15))#candidate|10929|(15, 8, 15)|var|float64
bop_10930 = relay.less_equal(call_10924.astype('bool'), relay.reshape(var_10929.astype('bool'), relay.shape_of(call_10924))) # shape=(15, 8, 15)
bop_10933 = relay.less_equal(call_10925.astype('bool'), relay.reshape(var_10929.astype('bool'), relay.shape_of(call_10925))) # shape=(15, 8, 15)
func_8371_call = mod.get_global_var('func_8371')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_10936 = func_8371_call()
call_10937 = func_8371_call()
output = relay.Tuple([call_10915,call_10917,bop_10930,call_10936,])
output2 = relay.Tuple([call_10916,call_10918,bop_10933,call_10937,])
func_10942 = relay.Function([var_10929,], output)
mod['func_10942'] = func_10942
mod = relay.transform.InferType()(mod)
var_10943 = relay.var("var_10943", dtype = "float64", shape = (15, 8, 15))#candidate|10943|(15, 8, 15)|var|float64
output = func_10942(var_10943)
func_10944 = relay.Function([var_10943], output)
mutated_mod['func_10944'] = func_10944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6365_call = mod.get_global_var('func_6365')
func_6367_call = mutated_mod.get_global_var('func_6367')
call_10994 = func_6365_call()
call_10995 = func_6365_call()
output = call_10994
output2 = call_10995
func_11007 = relay.Function([], output)
mod['func_11007'] = func_11007
mod = relay.transform.InferType()(mod)
output = func_11007()
func_11008 = relay.Function([], output)
mutated_mod['func_11008'] = func_11008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10300_call = mod.get_global_var('func_10300')
func_10301_call = mutated_mod.get_global_var('func_10301')
call_11009 = func_10300_call()
call_11010 = func_10300_call()
func_2846_call = mod.get_global_var('func_2846')
func_2848_call = mutated_mod.get_global_var('func_2848')
var_11017 = relay.var("var_11017", dtype = "int16", shape = (91,))#candidate|11017|(91,)|var|int16
call_11016 = func_2846_call(relay.reshape(var_11017.astype('int16'), [13, 7, 1]))
call_11018 = func_2846_call(relay.reshape(var_11017.astype('int16'), [13, 7, 1]))
output = relay.Tuple([call_11009,call_11016,var_11017,])
output2 = relay.Tuple([call_11010,call_11018,var_11017,])
func_11032 = relay.Function([var_11017,], output)
mod['func_11032'] = func_11032
mod = relay.transform.InferType()(mod)
var_11033 = relay.var("var_11033", dtype = "int16", shape = (91,))#candidate|11033|(91,)|var|int16
output = func_11032(var_11033)
func_11034 = relay.Function([var_11033], output)
mutated_mod['func_11034'] = func_11034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10544_call = mod.get_global_var('func_10544')
func_10545_call = mutated_mod.get_global_var('func_10545')
call_11076 = relay.TupleGetItem(func_10544_call(), 1)
call_11077 = relay.TupleGetItem(func_10545_call(), 1)
output = relay.Tuple([call_11076,])
output2 = relay.Tuple([call_11077,])
func_11078 = relay.Function([], output)
mod['func_11078'] = func_11078
mod = relay.transform.InferType()(mod)
output = func_11078()
func_11079 = relay.Function([], output)
mutated_mod['func_11079'] = func_11079
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11083 = relay.const([[[-9.059365,4.878235,-2.885355,-1.775486,-9.951412],[9.281594,3.927618,-6.384268,0.487848,4.012371],[-5.907937,7.953004,-0.542252,6.221826,1.674214],[0.012218,-2.255440,6.531027,-9.615369,2.462047],[6.262515,-0.294461,-1.340301,1.939133,5.050292],[-4.738483,-3.379993,-8.768569,1.552824,-4.458805],[-3.495390,-0.157693,-9.614926,4.460815,4.735016],[5.281992,8.339418,6.971582,7.479310,-8.161160],[-7.992037,-6.590615,-5.204842,9.755362,-0.211558],[-8.244144,5.704133,9.292745,-7.580214,-3.381515],[5.924300,-2.884213,-1.577225,-1.187088,-7.582687]],[[-8.690523,-4.425274,-3.488496,6.907900,-5.497500],[9.612671,9.574056,8.438181,9.607096,9.292749],[7.325733,7.858667,-3.777784,-3.196054,5.665297],[7.531187,9.485819,-8.604388,-6.386360,3.493651],[-6.732839,6.481577,6.673669,-5.109064,-2.039593],[8.836169,5.486009,1.155136,-3.401966,-0.448717],[-6.576863,0.335180,7.844098,7.904154,-3.537717],[-7.752578,-9.984241,-7.661517,-9.115827,-4.115319],[-6.625978,8.354223,-5.475368,8.825022,-5.414316],[7.919648,0.039017,-4.791531,-4.622084,-9.951141],[-5.641180,2.196561,-2.407336,-2.756510,7.312233]],[[5.966035,-5.007169,8.492465,5.202589,5.613297],[-3.371267,9.415077,-2.065578,9.416430,0.922917],[4.138522,-2.480408,-6.220588,-5.961772,-6.706440],[5.640854,1.323978,-2.994804,2.589488,-6.394915],[4.379864,7.014888,-8.396341,-1.567921,-4.837792],[-8.879528,8.533467,8.681992,4.296138,-2.663275],[0.639087,-5.749812,-6.078781,4.171073,-4.388011],[-9.592320,-8.445336,-3.238845,3.925786,-8.313955],[3.992475,9.086976,-8.461615,-2.658194,-4.221839],[9.038569,6.235249,6.265329,-8.894136,6.877079],[-3.656092,-9.244139,0.526582,8.513061,4.445787]],[[-7.673632,-5.188806,2.564689,-7.529851,6.463286],[-0.529866,-7.877139,-5.514893,1.673603,-3.982445],[3.777846,6.746855,-7.879462,4.415644,6.867534],[6.171943,4.289273,-2.753433,-2.935442,-1.122657],[1.620935,-1.265778,-6.002951,0.749570,5.913160],[-9.744321,-1.440335,-1.945548,-3.437715,4.878697],[-7.243124,-4.219254,-2.512591,-2.270186,7.777986],[-7.578795,-3.140419,5.439358,8.455586,-8.920134],[-3.071383,-1.774076,-6.451088,7.193112,-1.083424],[1.768431,-1.763701,-9.037211,-9.512402,3.975636],[4.581677,-1.070924,4.465730,2.816400,4.630148]],[[7.448336,-4.419092,-8.603101,5.120310,-5.465596],[-3.535950,-6.126831,6.034259,-3.002875,-1.684749],[7.899459,2.914409,0.114192,4.451145,-9.070773],[-2.224160,8.729199,8.700364,-6.475694,8.240613],[-3.563916,-1.145882,-2.435429,6.401455,8.783948],[0.150898,2.083010,-9.701365,4.710642,6.143308],[-0.169259,8.752303,9.454208,-4.738598,1.649905],[-9.387153,6.270542,5.279044,-0.483304,-0.296699],[-8.129360,-5.642598,3.994325,-8.551176,1.784344],[-0.447185,5.431410,6.386462,-3.470973,-2.074002],[1.804817,4.094903,4.700758,9.366599,2.928788]],[[0.335661,3.242997,8.293302,2.972851,0.575770],[-3.209058,-3.223425,5.727181,-1.721688,5.258359],[-2.262040,3.878215,-6.923216,-6.024595,-2.225351],[0.708515,8.429794,3.047560,2.243279,-4.956402],[4.016216,-3.594634,-0.365212,8.616409,7.817288],[-8.360357,-6.460743,7.916530,-5.816579,-4.451239],[3.657173,5.579804,-1.924491,-4.342285,7.820313],[-2.268705,5.705056,-0.688580,-3.054009,-7.953917],[1.107326,7.029235,-3.287145,-4.541656,-2.661853],[0.192679,-2.662753,-6.741776,7.909227,1.389110],[1.876536,-4.888638,-9.568201,2.541707,-4.504796]],[[8.646387,-5.747788,8.062792,1.121883,6.577820],[-3.052705,-1.312348,7.719717,5.706689,9.317705],[1.068976,-1.670750,5.979903,0.606071,-8.136952],[-4.780759,6.437411,-5.608454,5.873092,-4.440669],[-1.365289,0.294107,6.442954,0.205967,1.853421],[7.325310,-0.455387,-1.104652,4.468599,-9.056172],[-9.387933,4.617686,9.482646,-2.454220,8.852358],[0.385326,-5.757120,-2.852207,-5.659437,-1.085766],[-0.234789,-0.407944,-1.739416,-5.985159,-1.793708],[4.930180,6.649167,-3.246150,-4.365984,5.526840],[3.316113,3.334890,0.967824,-3.910686,-5.412025]],[[-9.728187,-7.477868,1.671112,9.679330,-3.212367],[-2.908951,-0.743141,-0.883711,-7.205218,-3.353406],[0.001176,-8.504604,4.289240,-3.994679,5.777488],[-7.261356,-4.004357,9.049222,3.181457,2.517047],[-9.817458,0.228134,-2.670384,-2.769990,9.402315],[-7.456936,-8.700793,1.450925,5.518775,7.360276],[-7.305018,-1.858089,4.993647,-8.821474,-2.255321],[-6.653583,0.575973,-2.754159,-4.290606,-8.058749],[9.499611,-3.394145,-0.679753,5.031007,5.216062],[-2.287130,-0.561201,-9.064880,-9.443900,1.657103],[2.369430,-5.913655,5.953835,-3.399810,4.762382]],[[1.203295,8.106247,-9.445905,-0.573922,6.822830],[7.773019,5.574508,-4.419355,0.001641,8.114422],[-3.823212,-9.381400,1.058659,6.054447,0.270348],[8.791141,2.798342,-3.670061,-2.737632,8.355784],[4.586635,7.431744,-4.149577,-2.296394,6.688319],[-8.090289,-7.739235,-7.601514,2.529509,4.283880],[-0.740657,8.662333,-3.662245,2.482701,-5.842841],[-7.368411,9.148530,8.656962,-5.092416,8.519667],[2.650414,5.523077,9.890391,7.569806,4.234404],[6.053869,5.568024,6.871362,1.159002,-5.795267],[7.066475,2.727507,5.008170,-9.151113,-3.348416]],[[9.648362,-7.796845,-0.074173,-4.904247,-2.163395],[-7.612532,2.269113,-7.901376,1.818304,1.573811],[-9.204151,5.323356,-7.153240,-6.303098,-4.935421],[-0.914698,-4.344306,-1.524119,-1.353196,-7.085271],[-5.129953,4.905941,6.024126,-0.814299,4.695378],[-5.388837,-3.743229,7.956884,-9.062169,7.211482],[-9.659896,-4.053559,-3.984900,9.024071,7.680800],[4.928922,0.839434,5.403498,6.530914,9.835996],[-9.992062,-3.634361,2.248875,6.989252,4.752825],[-2.200228,-1.293939,-6.962950,2.521701,-6.642509],[5.272947,-5.410310,-6.119867,9.955369,8.372371]],[[-8.399344,6.759353,-2.502931,-7.264917,-6.784871],[6.741818,9.998399,-5.835260,-9.306575,-5.817071],[-1.676742,3.190761,-6.299622,9.222170,4.717250],[-9.789499,-3.819958,-9.749465,8.484784,-8.429087],[-8.197285,-7.424353,5.162128,4.300620,7.842966],[-7.786390,4.875942,-8.099980,3.312979,-5.660963],[5.799557,-9.689392,-6.540538,-4.635894,9.630523],[6.949053,-3.038918,-8.365862,-0.016594,-2.139197],[6.292947,-1.394791,-7.171086,-7.523373,-2.417113],[-7.070107,5.529932,2.086549,6.530687,9.639551],[-1.120609,-5.932699,8.230373,-2.304060,-7.388559]]], dtype = "float64")#candidate|11083|(11, 11, 5)|const|float64
const_11084 = relay.const([[[-4.431560,-9.438012,-8.985738,-0.752191,7.310415],[-1.803894,-8.262599,-5.214625,-5.583581,-9.122599],[8.405843,3.268117,1.618086,-7.016345,-8.191851],[4.080838,2.669724,6.320360,-3.940142,-1.183232],[-4.837080,0.244034,-0.006081,-9.060374,6.594641],[9.773265,5.944615,4.843042,4.465061,-9.980956],[9.360650,-3.928381,-7.317671,0.725989,4.375469],[-2.886293,-1.228757,-6.743778,-1.158510,3.131264],[-2.461696,-1.784243,-6.531631,-1.221165,5.778625],[8.768579,3.579289,-8.861322,-6.184261,-4.086534],[5.887598,2.288808,-8.200461,1.693144,6.822982]],[[6.934078,0.124144,0.097026,2.258833,4.823850],[7.659504,-8.648777,-3.955718,-7.056614,-3.683456],[3.088864,8.333467,6.114140,-4.079503,-1.587435],[-0.898730,0.436681,5.920935,0.874642,4.474848],[-2.037608,6.659889,2.052389,1.488378,-4.619444],[-9.813073,8.429399,0.891913,-0.608135,1.912283],[2.498304,-8.265624,-1.904072,1.477641,-7.904522],[-2.740218,0.424171,6.224126,-3.348152,-6.189683],[-4.194881,-4.799637,4.095769,1.807883,0.374265],[-0.665289,-5.079214,-8.102062,1.882670,-3.599406],[-8.760945,-7.909786,-9.591946,-7.547071,-5.019630]],[[-9.896579,1.918503,-2.383911,-2.521825,-2.887979],[2.711171,-7.527698,9.380091,-4.043498,-3.091373],[2.701644,0.792714,7.865291,1.002010,-4.139123],[-6.607543,9.911867,3.421995,-9.545616,9.952671],[-3.801301,-1.582643,-0.991817,8.843283,-7.102897],[9.375129,-7.647692,4.316437,-2.929326,3.925904],[-9.398813,3.052883,5.644227,9.633447,-4.791046],[4.265267,1.900794,4.090241,4.263363,-5.517007],[8.463914,0.776221,9.984077,2.225029,-8.232320],[-3.897641,-3.128657,-5.977594,0.682966,-8.665634],[-4.914573,-7.563551,3.078807,4.015125,-7.954744]],[[-2.965366,6.038531,0.905025,-0.323300,-2.615631],[6.146509,0.188905,2.904715,7.428242,2.380730],[-1.390453,3.580206,-7.154899,1.044750,-9.609132],[1.361667,9.075728,-8.313798,7.505071,5.413269],[2.661324,1.063525,-0.179625,-4.555266,7.465531],[2.484683,6.713287,-8.495495,2.700075,5.660935],[4.984411,-2.846810,2.744327,0.479076,6.271498],[4.603030,9.620394,1.650895,7.069751,7.686224],[-0.419176,-8.754715,-8.615726,4.708698,-4.402184],[5.223250,9.218066,-7.396248,-4.733273,-5.287953],[-2.125437,8.340951,-8.331469,-1.950225,-3.646085]],[[-5.970390,-4.824856,3.688387,5.964062,7.499842],[4.492186,6.629005,-8.347690,-2.146794,8.846776],[2.836415,-8.415088,6.110603,2.497257,-3.029678],[5.794245,-7.112050,5.806652,-4.087904,-5.095169],[4.045593,-1.973562,3.790625,-8.968509,-4.952038],[-2.861543,-4.347049,-2.247738,9.045496,4.014201],[7.529901,-8.020035,-4.312239,9.032848,-1.888379],[-0.349327,-1.182129,-8.766147,-7.031935,9.133844],[-4.594554,-0.067097,-0.887408,-9.878039,-5.666656],[7.440364,-4.564405,-1.191637,5.497292,-4.420232],[3.184471,4.539703,7.621389,7.091645,9.547444]],[[-8.962786,-2.184018,-7.391661,1.428010,-5.642503],[-0.828235,-7.807607,9.497772,6.074108,-1.954197],[-8.350342,0.543520,6.884314,3.879721,-5.866557],[7.708785,-2.587943,8.140795,-3.891832,8.799846],[-0.485566,-4.211909,6.322640,9.996558,1.877757],[-4.936799,-5.362042,4.919239,-8.721536,-5.670140],[0.940227,-1.928803,-1.381581,-6.912002,-2.937505],[0.538734,8.707431,3.833483,-2.974439,-4.665361],[8.545772,2.793674,-2.509617,3.482904,-6.716443],[5.381508,-8.191887,2.017456,7.326139,2.412900],[-2.936107,-1.132608,4.380593,-1.341444,6.420110]],[[5.629555,1.379266,-4.960346,4.708653,-8.199989],[7.164024,-9.740945,9.813737,-0.644023,7.417841],[3.742293,6.823477,-3.486869,5.237464,-4.068316],[1.306605,0.761893,-0.329298,-5.300415,-5.612467],[1.621582,-4.576492,2.027371,-5.491966,-3.570255],[9.274244,9.386882,1.521232,9.286972,-7.461799],[3.813281,4.929798,-3.712154,-6.346418,-9.132194],[5.941437,8.072049,3.296990,-0.682093,-0.291767],[5.221634,-8.930159,-0.636398,-1.091656,-5.269778],[9.106123,-6.995768,1.351836,2.276083,5.469582],[-1.804733,6.165711,-4.044769,-2.804959,-4.308621]],[[2.054224,-8.780961,-5.888801,-9.323714,6.526525],[4.234310,-8.071572,5.831049,-9.441914,-8.274183],[-6.142668,4.240504,-4.246759,-1.814404,-8.256172],[3.432847,9.572369,4.660105,4.985067,-9.280370],[-6.084055,1.579244,-6.543098,-5.271042,7.631011],[-5.759522,0.769672,-4.642368,-1.782375,-5.513550],[5.750263,-7.107578,-9.027284,2.498908,9.714501],[-7.531724,1.227899,0.757982,-7.271594,8.112787],[-5.550607,-6.755666,1.317125,4.912463,2.962757],[-0.063219,6.126453,9.834500,-6.162759,4.362106],[7.318964,8.055249,-3.275798,-4.914342,7.549927]],[[-4.879923,4.444853,8.897628,6.348926,-2.514371],[8.177244,-0.161193,-2.564425,-4.675628,-4.388866],[-4.895563,2.880446,-1.961096,-4.380357,-6.361145],[-7.811108,5.671583,8.048510,-2.747432,8.203794],[-0.252335,7.488545,-7.766753,-7.656191,-9.692430],[-2.461561,-3.933090,2.080403,8.824262,3.243296],[5.507664,2.432397,-7.425204,3.548112,4.561707],[8.179473,8.496781,-1.850749,-4.088782,-2.848336],[4.477125,-0.301363,-0.547619,2.870538,4.371197],[-4.414013,-4.502888,-9.260134,-5.539395,-9.707620],[-1.838717,8.113532,-3.441263,6.698346,6.861904]],[[-2.895762,1.282031,-8.336431,-1.311439,0.010123],[6.069356,-0.855833,7.463538,-8.643784,-0.647696],[-7.010391,-7.745003,0.728642,1.322795,-4.000363],[-6.174142,-9.286787,9.200757,-8.648121,-1.305536],[7.589915,0.410733,2.325037,-8.824660,-7.442184],[-8.486754,-5.999845,7.935705,-4.974557,-2.214421],[0.097344,1.744771,-3.563333,-1.018389,-6.108612],[6.898552,-9.718857,1.826873,0.603843,9.140602],[-5.081935,-1.851431,3.309325,-1.284125,7.326516],[-8.003568,-1.158918,-3.322972,-4.773776,2.333170],[5.774107,-2.945667,8.002805,4.982199,-9.433271]],[[-3.985460,1.327295,2.055072,-2.023620,-4.193535],[-2.365190,-8.139789,-6.280339,-6.419282,-8.136431],[8.206339,-3.426282,5.712446,6.498412,-4.493969],[-2.447263,-3.157927,-5.964359,-4.789743,-9.262496],[-6.644762,5.975754,9.783454,9.864915,-3.271722],[3.435296,6.871295,9.258690,4.002875,9.234187],[-7.671940,-4.150832,0.101442,-2.753639,-2.355038],[-4.553860,-8.434603,5.718445,3.514371,9.091470],[-7.214014,4.817508,-7.844556,7.308339,0.058851],[5.373748,-0.328804,8.807723,-2.675180,4.385720],[-1.912684,8.494059,3.158423,-7.098102,9.515701]]], dtype = "float64")#candidate|11084|(11, 11, 5)|const|float64
bop_11085 = relay.floor_mod(const_11083.astype('float64'), relay.reshape(const_11084.astype('float64'), relay.shape_of(const_11083))) # shape=(11, 11, 5)
func_2846_call = mod.get_global_var('func_2846')
func_2848_call = mutated_mod.get_global_var('func_2848')
var_11100 = relay.var("var_11100", dtype = "int16", shape = (91,))#candidate|11100|(91,)|var|int16
call_11099 = func_2846_call(relay.reshape(var_11100.astype('int16'), [13, 7, 1]))
call_11101 = func_2846_call(relay.reshape(var_11100.astype('int16'), [13, 7, 1]))
output = relay.Tuple([bop_11085,call_11099,var_11100,])
output2 = relay.Tuple([bop_11085,call_11101,var_11100,])
func_11113 = relay.Function([var_11100,], output)
mod['func_11113'] = func_11113
mod = relay.transform.InferType()(mod)
mutated_mod['func_11113'] = func_11113
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11114 = relay.var("var_11114", dtype = "int16", shape = (91,))#candidate|11114|(91,)|var|int16
func_11113_call = mutated_mod.get_global_var('func_11113')
call_11115 = func_11113_call(var_11114)
output = call_11115
func_11116 = relay.Function([var_11114], output)
mutated_mod['func_11116'] = func_11116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7420_call = mod.get_global_var('func_7420')
func_7422_call = mutated_mod.get_global_var('func_7422')
call_11146 = relay.TupleGetItem(func_7420_call(), 0)
call_11147 = relay.TupleGetItem(func_7422_call(), 0)
func_3593_call = mod.get_global_var('func_3593')
func_3596_call = mutated_mod.get_global_var('func_3596')
const_11151 = relay.const([4.848993,-2.714062,-0.519947,0.649226,3.449609,-8.841479,-9.831591,-2.170424,6.952536,0.744111,-7.170214,-1.345932,1.015262,-3.680947,6.367596,-0.647741,-2.446408,-7.902514,7.379045,-4.864959,7.651663,-2.232794,2.154748,8.574154,-0.201101,-1.759283,-6.654100,-7.993823,-6.132810,4.363049,-0.301632,-0.283842,-7.460742,9.217363,-6.045981,-8.241572,-8.662547,9.858827,-8.459977,-2.569466,3.012174,3.249539,8.744416,3.823837,-4.252240,2.729612,-0.058324,-2.637873,9.211862,-5.249760,0.548651,3.115043,4.875698,2.885478,0.056283,-3.073884,-1.348661,-8.941049,2.791626,3.871872,-2.920071,8.153053,-0.616275,-6.196249,3.431969,-1.724631,5.841968,4.820857,-8.718895,-0.890918,-4.497663,8.118579,-9.299411,8.257662,5.330828,-3.685896,5.873511,1.106795,5.283453,6.400085,-7.750259,1.111156,7.135042,3.140152,6.754229,5.447491,-5.088712,-3.932246,0.311750,9.929222,6.172924,-4.643467,4.690247,-1.736536,5.293701,6.214809,9.704940,-6.136898,5.505781,1.053339,6.801154,1.605599,3.061730,9.393512,2.835010,3.295116,-8.949096,1.125457,0.749031,-5.457639,-4.863645,4.103170,-6.155528,-3.875087,6.140413,-1.996295,9.817672,-3.749843,6.927254,4.931543,-4.531938,8.746141,-1.878119,-4.760902,8.718790,9.985422,5.365838,6.510919,-7.998703,3.080055,1.845345,-3.066337,9.721103,8.096908,-4.632193,7.643939,-4.719487,8.197985,-2.617544,-9.254296,-7.749473,4.500938,-5.804877,3.700096,-0.319200,-9.208572,-1.727992,-8.668079,-6.094221,4.535042,-2.653164,4.880001,9.348605,-2.851141,9.475214,6.420098,-9.228991,2.391232,-7.090563,8.029044,6.400324,-8.715999,-3.530946,-7.002598,3.366731,-0.522419,-8.105726,-4.967320,-3.322905,8.868995,2.359928,-9.023395,2.816259,1.673501,-0.320264,4.170347,-6.926863,-5.849090,-8.448275,3.398901,-9.675120,-6.800937,-6.631592,-7.675296,0.222657,-6.010141,3.257974,-2.692224,-3.828538,-6.350137,-7.861345,-1.934474,7.531419,1.503104,8.972361,0.033968,-9.153868,8.728141,-1.816672,-4.353339,9.038662,4.735518,9.549051,-1.064991,9.988068,-8.861551,-8.690610,-1.841523,6.028770,3.419215,7.657128,-7.088958,-1.145574,-6.123843,-0.399411,-6.603012,9.164207,-7.900322,0.458510,-8.616446,9.265852,-2.845831,3.477208,4.697122,9.410842,-3.267715,-5.827845,-0.782862,-5.672267,6.968123,9.369351,-5.407463,3.087007,1.504471,1.351689,9.389739,1.996810,-8.275738,7.712941,2.409420,4.464755,4.984386,9.271030,-6.573609,-1.036599,-0.646423,-2.661440,-1.841522,1.118670,-9.213291,3.477349,1.123461,-3.449336,2.347863,9.417658,-3.288604,-5.147698,-9.785469,8.373632,2.719715,6.631861,-8.189366,2.202228,0.785654,-9.522471,7.166715,-9.281900,-7.921741,1.926820,-2.024263,9.700893,1.341546,-4.859742,5.977431,-2.054626,9.640411,-4.580805,5.100307,-0.477501,-0.017384,5.494502,-5.982256,-3.211149,-1.401653,-1.244863,-3.107806,3.973761,-8.166323,-1.751269,3.711049,-6.031740,-5.327230,-6.846947,-1.562281,-6.281417,-2.172866,0.347544,4.553072,9.958297,9.714760,-2.566190,4.869505,3.258169,5.761514,5.148989,-1.014460,2.156800,-8.996482,7.548421,-9.571686,8.832837,7.814804,3.412510,-2.127890,-1.740019,2.173189,-0.168117,-4.930694,-2.952324,2.831957,-8.750892,2.205034,-7.443121,-5.284355,3.845942,7.478564,6.533634,9.115184,-1.930664,3.950259,9.020211,6.877532,-2.153833,5.645376,-2.730407,-7.626772,-1.649073,-4.169368,-9.168148,-4.611351,-0.708631,-3.624516,-2.895577,-9.107175,-1.802547,5.143372,-7.267570,7.280795,-4.360509,5.838995,2.485028,-9.786335,-0.990225,-5.116873,8.150650,-9.259921,-1.665170,2.407039,-4.065406,6.758285,3.695569,-3.733092,-8.870342,-6.052310,-9.149082,8.812767,-3.565363,7.821765,-6.657725,9.916191,5.104264,2.346839,-0.404445,-0.477079,3.657101,8.928237,0.303270,-4.561056,8.927568,-9.213590,6.096189,5.763488,1.408559,-7.651441,-7.873956,8.467215,0.791480,-5.308769,3.388209,-5.436880,-6.353991,-6.901617,0.326344,9.540902,2.400489,-5.196630,8.392821,-0.081515,-3.031542,6.249340,-8.117451,-5.565449,3.298276,-4.232297,-1.708856,3.855843,-3.636136,-4.655223,9.045269,1.135374,2.168469,6.316959,2.705288,-0.723027,-0.315533,7.357872,-9.722861,-4.017403,-1.537068,1.151989,9.346099,9.860011,-5.280621,6.336378,-1.950929,-8.364000,-7.459394,-3.254713,-3.937660,4.497396,-6.025863,9.072416,7.750155,4.076102,-1.572575,-1.884165,7.742358,-8.583133,9.556446,2.366557,-1.648088,4.443590,8.943095,-1.504674,-1.381074,-9.827555,-8.770900,-3.956859,8.584311,2.422785,-2.716348,7.360451,-8.820929,0.858005,0.326636,3.181231,-9.423540,-5.452601,-2.531493,6.543594,2.181588,-9.613710,-9.207709,2.512826,-1.354959,2.547908,-4.344021,-1.614153,-5.167431,-9.386309,7.611155,3.732371,-7.187956,3.954954,5.692261,-5.085919,6.472371,-7.743179,9.855094,1.695839,2.051945,-4.173456,-6.006652,-3.996211,-1.051853,-8.353422,-0.989019,6.200831,-2.271049,1.295144,-9.647262,-1.005065,-1.812585,7.248688,-4.792069,9.893372,4.553231,5.667107,5.424428,9.184347,-3.299868,2.237653,1.517250,5.542745,9.391245,9.426001,-4.512888,9.020523,4.997964,-3.014583,-5.713957,6.519887,0.983395,5.850170,-8.139614,-9.156571,-4.202923,1.014777,3.852360,9.742678,3.121134,-1.117681,-4.656562,4.107724,-6.074318,6.942086,2.905241,-6.386324,5.191196,1.105988,-2.996221,-1.362943,4.283936,8.539526,1.633815,-2.421067,5.310115,-4.095145,-2.411980,5.513693,-6.351701,1.775936,6.415573,-8.341190,9.488706,-2.693337,-1.950197,3.542331,-3.181748,-0.578496,3.287456,3.509716,3.966561,6.587477,5.440278,-7.464552,5.188423,0.242952,1.416016,-3.003533,-0.010195,5.308241,6.250945,-8.745619,3.327175,0.830666,7.593390,2.052624,4.777360,5.598023,-8.614489,-7.736651,3.027570,-8.433781,7.910823,-3.514567,-4.657749,-3.729081,-3.601725,4.748921,0.938838,-3.363241,2.190150,6.386659,-4.724301,8.532963,-1.945581,1.487989,-8.547754,1.508931,-2.282025,8.531614,4.366470,-2.028628,-4.267233,4.917687,6.587208,6.480846,4.141600,2.475945,6.088351,-4.614150,-3.452980,3.641555,-9.820288,-7.559745,-8.969356,1.799049,-0.061073,7.304744,0.851182,-9.705681,3.182124,-7.642161,6.205272,-3.868800,-4.627402,-0.040715,-8.833808,2.834492,-2.635817,7.680284,6.292620,-7.694453,2.746666,2.067551,-6.070247,1.627136,6.473023,6.269778,2.750259,9.952147,-5.678658,-0.704446,0.235596,1.486566,4.530824,4.409665,4.755852,-5.904237,3.325103,-8.055476,-3.790180,8.642793,2.635740,-8.657538,7.804231,-7.259621,3.464958,-6.366434,3.463431,1.446690,2.863321,9.863206,-2.289537,7.714987,7.285471,-1.831247,9.439055,4.295135,-5.810789,4.084473,0.538461,0.833178,-1.945487,-1.898868,-2.576595,-2.015993,-0.819435,-6.427439,-9.804686,-2.452958,4.978521,8.405620,3.033818,3.342924,-3.648858,0.954140,4.334462,-3.627820,-7.330888,9.530981,-0.189419,-4.192223,0.848558,-4.497918,-4.180133,-0.630766,4.843111,-4.386436,-7.878782,-4.430967,-5.637001,0.841606,-4.590095,3.743678,-9.076714,3.978859,7.618444,2.570906,4.639470,-8.093879,-8.978252,6.477363,-7.472057,-0.547893,-0.257246,4.129597,-1.019748,-8.502851,-7.174762,-0.833165,-2.546310,-5.408010,7.400707,-2.673374,8.485295,2.036116,9.338479,6.520759,-4.879165,8.523264,-3.984318,-6.084893,1.622491,2.226437,-6.477353,-6.828294,-2.842792,-9.758779,-0.212202,-6.224439,6.607626,3.599317,-0.893200,-9.485053,8.253096,7.514455,-9.354021,-2.958704,-5.584801,-2.442121,8.476774,4.477121,7.126549,-7.418280,4.608360,3.781044,-8.805076,7.971660,0.169553,8.324980,4.159722,-0.968410,-0.896827,5.748519,-4.942058,-6.766487,-9.656340,3.181507,3.487184,5.038368,-3.779173,-1.387841,-1.524307,-7.812677,4.898092,-1.294210,-2.727984,7.199007,6.506443,-6.759972,-3.756485,-6.419547,-4.311994,-3.038801,0.914877,-4.226753,-8.031958,-4.959850,8.779559,-5.298234,-0.469210,5.630736,9.415330,-7.965249,-8.421465,-9.751144,6.158922,5.328292,5.910734,3.549268,-2.880154,-7.390377,-4.521433,2.856309,8.631596,5.079920,-4.847034,5.993124,6.225840,-0.501113,-9.171265,-8.994763,7.963342,6.326211,1.336694,0.312197,8.462622,-5.789628,-3.792055,7.339828,9.644486,-8.876167,6.511909,6.597800,8.252087,-3.049091,-4.410868,6.523841,0.224625,-1.927843,8.814206,-5.694148,-4.513282,1.865618,-2.536544,-0.622264,3.058212,1.940817,-8.039288,4.534506,-5.722358,0.890001,-9.582007,5.952271,-0.936587,-2.616770,6.156971,-1.486384,7.447582,0.162042,-5.057603,6.265135,-4.679636,-2.186314,2.005214,-4.572956,-8.162522,-3.106996,-8.128564,-4.741460,-1.281314,-8.288532,5.338577,7.299517,-2.474135,-4.560925,-8.929073,-6.935934,-1.832195,-8.889167,-2.581410,3.382674,-1.831249,2.649225,2.312265,3.214260,-9.366173,-6.308259,-4.477200,-6.153340,-1.024833,7.323078,-4.640721,4.558781,9.127573,-7.368850,-9.888574,-0.351752,-9.019498,0.452670,8.672286,7.638355,-1.510704,4.917986,5.990945,-5.650642,-0.955495,-5.663236,5.977940,3.421084,4.339446,3.277183,1.007721,0.604694,9.368062,-3.746267,2.186461,1.902000,2.425599,8.672035,-2.956319,-9.367661,9.530786,-7.710151,-5.369868,3.983036,3.576303,5.999490,-7.654919,-7.635989,3.976969,-2.283678,-6.541991,-0.679560,-7.034203,-2.119647,5.353202,2.210805,-1.202015,-6.249867,0.733638,-1.041284,-7.392242,-6.294365,-5.885446,-1.807544,4.080948,5.627284,-5.283549,9.039055,0.030929,-0.623470,-2.178623,8.048010,6.936355,6.378151,-2.785023,3.645334,1.738167,3.843915,7.736756,3.180242,3.900406,-9.368675,-3.011840,-2.766451,-1.912908,2.057335,2.040407,1.530516,-8.609193,2.873933,-0.568025,8.850973,-4.501526,-6.572594,-8.330701,-5.993282,-8.922317,-4.168046,-8.349667,-1.455085,8.467738,1.100503,-9.745224,6.427531,2.476708,6.856347,1.267089,5.979893,-8.037085,2.224232,7.079269,-7.966155,0.297373,2.557937,2.154910,-8.196476,4.440955,0.665923,-9.239338,-4.165384,-5.914288,7.047448,-5.815839,5.412946,-5.137287,6.102370,8.380174,1.530878,-5.086439,-4.966339,-4.539885,-1.781450,9.219913,-8.537860,-4.763506,8.391337,-0.176624,1.697231,-6.761049,3.790514,7.294606,-3.164278,-0.986770,1.998159,-0.056233,9.976999,-3.592223,-1.602077,4.192997,4.473852,4.681230,-1.833205,-0.969580,-9.541430,1.099761,0.570260,4.492343,6.163201,-2.532579,-8.403017,-1.035800,6.851231,-4.269252,-2.086754,-0.200716,3.579329,9.564725,-9.030479,7.403213,-7.027841,-9.525690,-9.911890,9.099576,-7.215244,-5.012744,3.534771,-9.349526,-7.238281,-5.843883,-1.211657,-3.911583,4.488949,-5.324279,0.843528,-5.377419,-6.190843,-8.329044,-2.842332,-0.884058,4.219378,-3.813960,7.625562,2.583433,3.321902,2.919197,6.661227,4.056846,4.055467,-4.072936,-9.892493,-3.995172,6.525772,7.466353,-9.896166,-2.255635,-1.131194,-0.850343,6.392160,7.971947,-3.937860,7.866941,1.513922,-0.189962,-6.888954,0.125532,5.396233,9.216763,-6.393300,2.808544,-6.013780,-5.813231,-6.490740,-6.170453,1.112623,-6.608093,-5.673413,3.836420,-5.834558,-3.122142,-6.902025,0.692483,5.836281,-7.968838,2.828520,7.161322,-4.471189,6.682478,-5.143559,-9.799952,5.115304,5.876699,-2.889871,0.999946,-5.597731,8.066051,-2.069584,7.685887,1.988046,6.046723,9.500496,-4.975557,5.970278,-4.643494,-2.532349,7.402883,1.247811,1.905893,0.376695,-9.108064,9.416838,-2.367492,3.315066,1.960081,2.083407,3.702648,5.088864,-5.850639,6.710556,3.994476,-7.709381,-6.214747,1.728124,1.512079,-6.034754,1.106091,-2.656188,6.235746,6.710141,-9.053642,-0.999369,6.108499,-2.472021,-0.976959,-7.175996,2.768049,-6.305933,-7.727042,6.036572,-1.231287,6.353048,8.742924,2.855921,3.682028,-5.980792,8.576113,-7.939377,-4.895306,9.281583,-2.117926,-8.240133,-5.323254,2.550056,9.304176,-3.780207,5.518862,5.990044,1.544647,4.030145,8.859445,5.022531,-1.662326,0.112998,-7.529677,0.857826,-4.380548,-7.250436,-6.351697,1.913516,-1.973738,6.517217,5.414267,5.766482,6.529162,-8.963505,-1.191317,-4.563419,7.862126,9.155421,-7.181119,-4.194464,2.046275,5.934466,2.627484,8.786170,-2.270193,9.759018,9.376960,0.426584,5.909662,5.930857,7.961966,7.123613,1.807626,-1.698379,3.172097,-9.874833,5.829839,7.848963,-3.602355,-2.420295,8.870772,-6.700562,-2.857412,-6.341487,5.214181,6.488820,6.921817,2.075384,-9.991157,-8.402816,9.444063,-9.246876,-0.908915,5.861607,-5.100564,3.447610,2.618521,-4.376852,6.970688,5.957303,-0.521117,8.805215,7.377171,-1.659110,-2.644500,-0.254762,3.352428,-9.538442,-0.079124,-0.746259,-2.320634,-7.189441,4.917411,1.921436,9.885907,-5.275950,-1.875188,9.994852,-0.360188,5.196650,-3.060951,-5.264395,-0.389163,0.550428,-4.655812,2.800260,-3.635823,-9.151694,-5.961070,-3.174158,3.784461,0.710037,4.830907,1.294173,-5.082947,-4.887748,-6.034321,-6.119014,-8.619094,1.206261,8.669796,1.877114,8.460272,5.703573,6.204047,6.310215,-2.997698,-7.555058,-2.613392,-9.549948,-5.578067,2.481565,8.397092,2.991861,-7.291565,4.615977,9.518169,0.166498,-2.995421,-8.797113,-0.856288,-2.884906,-4.555759,-1.196928,8.226886,5.260414,-3.398012,-4.910124,-7.807069,3.497502,8.328747,-7.588225,6.641495,4.643183,4.005807,2.855198,4.846554,-1.630998,3.206460,-4.347596,7.949974,-4.376273,1.371767,-5.919183,9.587020,-9.278744,-4.492595,8.736876,-7.047654,4.902262,4.945103,2.310974,6.212797,-5.749699,5.422336,2.692118,0.246632,-5.646136,-9.096918,-5.806869,-3.497221,-6.851382,-7.849902,-3.708485,-3.526370,-9.676810,-0.980813,4.014141,0.155387,-4.213840,-9.269105,-9.635571,-3.214175,-4.576498,5.607083,-1.264525,5.515497,-4.955765,-8.377603,-9.798503,-3.975884,-0.025408,8.786887,-2.798818,-5.194738,3.005283,-6.012089,-6.669457,-8.937286,-1.143396,5.978734,0.125895,5.190955,-5.567423,-6.999344,4.271761,1.899579,8.197778,2.107067,-8.797489,5.140502,-4.286813,4.152638,-9.878094,-7.538634,4.211502,2.795392,-2.790920,-6.637886,-7.685060,-7.044564,5.250045,-6.077242,-7.211916,9.438377,7.227547,-6.095187,-9.961193,-7.272230,0.362771,9.136866,-5.505296,4.271200,-8.662750,-7.415657,-1.985488,-9.087125,-2.134767,-5.452091,-1.392293,0.220044,-7.815125,3.000019,3.252579,5.419049,-5.184634,6.064217,1.921282,-4.686375,-8.348064,3.745287,9.276914,8.062435,-1.540319,-9.952960,3.010537,-9.162824,2.731609,-9.953444,2.344003,5.988590,3.991333,-4.028056,8.433083,-9.754770,5.533010,-4.086102,5.675644,2.419550,1.459665,-3.340673,6.990353,5.567351,-5.925101,-2.059842,6.718453,-3.188697,-1.397121,-5.863271,7.813418,-9.704967,-9.397293,7.618391,-9.448120,2.873436,-1.741255,-3.604937,-5.293810,-0.243379,4.312308,-5.706597,-7.577050], dtype = "float64")#candidate|11151|(1456,)|const|float64
call_11150 = func_3593_call(relay.reshape(const_11151.astype('float64'), [14, 8, 13]), relay.reshape(const_11151.astype('float64'), [14, 8, 13]), )
call_11152 = func_3593_call(relay.reshape(const_11151.astype('float64'), [14, 8, 13]), relay.reshape(const_11151.astype('float64'), [14, 8, 13]), )
output = relay.Tuple([call_11146,call_11150,const_11151,])
output2 = relay.Tuple([call_11147,call_11152,const_11151,])
func_11163 = relay.Function([], output)
mod['func_11163'] = func_11163
mod = relay.transform.InferType()(mod)
output = func_11163()
func_11164 = relay.Function([], output)
mutated_mod['func_11164'] = func_11164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7646_call = mod.get_global_var('func_7646')
func_7647_call = mutated_mod.get_global_var('func_7647')
call_11178 = relay.TupleGetItem(func_7646_call(), 1)
call_11179 = relay.TupleGetItem(func_7647_call(), 1)
func_5582_call = mod.get_global_var('func_5582')
func_5584_call = mutated_mod.get_global_var('func_5584')
const_11184 = relay.const([[-4,5,-9,4,-8,8,4,9,-4,7,-1,-4,-9,2,9,-2,-5,6,3,5,-6,5,8,-4,-10,2,4,-2,9,4,-9,2,-3,-9,-8,-2,-7,4,1,-6,9,-4,8,-5,3,-8,8,-8,10,-9,-4,-3,-8,-6,3,1,4,4,-5,-10,10,1,-7,9,6,6,-3,-1,-3,1,1,-9,-9,-8,4,3,7,4,-10,-3,-4,-8,-5,-7],[8,-6,2,-7,-10,7,4,-2,1,4,10,2,6,3,1,-2,8,1,5,10,2,1,-5,-6,8,2,9,4,-3,7,-6,6,-8,3,4,1,1,3,-5,-4,1,3,-9,-5,3,-8,-10,-3,3,6,-9,7,-10,-6,1,10,-6,-4,-9,9,9,-2,-4,-9,-3,6,1,2,6,-6,7,-1,-8,-10,-3,10,-10,3,9,3,-9,4,4,3],[3,7,7,5,-2,-2,-5,9,5,9,5,6,1,-6,-5,5,10,7,7,-3,-6,3,7,5,3,-6,6,-4,3,1,9,-5,5,6,-2,2,4,-7,9,-1,-8,1,-10,-10,-5,10,-9,4,-4,8,1,-4,-7,-6,-5,-9,5,-6,4,-9,-6,-2,-3,-1,-1,7,-10,7,-3,4,-9,10,2,10,-1,5,-7,4,-7,10,-5,8,-7,-5]], dtype = "uint8")#candidate|11184|(3, 84)|const|uint8
call_11183 = relay.TupleGetItem(func_5582_call(relay.reshape(const_11184.astype('uint8'), [252,])), 4)
call_11185 = relay.TupleGetItem(func_5584_call(relay.reshape(const_11184.astype('uint8'), [252,])), 4)
func_11113_call = mod.get_global_var('func_11113')
func_11116_call = mutated_mod.get_global_var('func_11116')
var_11209 = relay.var("var_11209", dtype = "int16", shape = (91, 1))#candidate|11209|(91, 1)|var|int16
call_11208 = relay.TupleGetItem(func_11113_call(relay.reshape(var_11209.astype('int16'), [91,])), 0)
call_11210 = relay.TupleGetItem(func_11116_call(relay.reshape(var_11209.astype('int16'), [91,])), 0)
bop_11216 = relay.multiply(call_11183.astype('float64'), const_11184.astype('float64')) # shape=(3, 84)
bop_11219 = relay.multiply(call_11185.astype('float64'), const_11184.astype('float64')) # shape=(3, 84)
output = relay.Tuple([call_11178,call_11208,var_11209,bop_11216,])
output2 = relay.Tuple([call_11179,call_11210,var_11209,bop_11219,])
func_11223 = relay.Function([var_11209,], output)
mod['func_11223'] = func_11223
mod = relay.transform.InferType()(mod)
mutated_mod['func_11223'] = func_11223
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11224 = relay.var("var_11224", dtype = "int16", shape = (91, 1))#candidate|11224|(91, 1)|var|int16
func_11223_call = mutated_mod.get_global_var('func_11223')
call_11225 = func_11223_call(var_11224)
output = call_11225
func_11226 = relay.Function([var_11224], output)
mutated_mod['func_11226'] = func_11226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6713_call = mod.get_global_var('func_6713')
func_6714_call = mutated_mod.get_global_var('func_6714')
call_11228 = relay.TupleGetItem(func_6713_call(), 0)
call_11229 = relay.TupleGetItem(func_6714_call(), 0)
output = relay.Tuple([call_11228,])
output2 = relay.Tuple([call_11229,])
func_11260 = relay.Function([], output)
mod['func_11260'] = func_11260
mod = relay.transform.InferType()(mod)
mutated_mod['func_11260'] = func_11260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11260_call = mutated_mod.get_global_var('func_11260')
call_11261 = func_11260_call()
output = call_11261
func_11262 = relay.Function([], output)
mutated_mod['func_11262'] = func_11262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_11277 = relay.TupleGetItem(func_5993_call(), 0)
call_11278 = relay.TupleGetItem(func_5995_call(), 0)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_11290 = relay.TupleGetItem(func_5509_call(), 1)
call_11291 = relay.TupleGetItem(func_5511_call(), 1)
func_9494_call = mod.get_global_var('func_9494')
func_9496_call = mutated_mod.get_global_var('func_9496')
const_11295 = relay.const([-2.939872,4.706171,4.835875,-4.433435,0.770659,-0.357891,-7.122553,7.253228,-8.061525,0.402651,-1.546902,4.021492,4.828480,8.967839,-1.967459,8.220970,6.111618,-2.314403,7.215108,7.785054,-0.665849,-4.393677,9.399938,-0.636739,-1.584972,-0.281912,7.787684,5.317403,-6.824994,0.412269,5.867649,5.452501,8.960804,5.827758,4.894026,5.139701,2.701532,-7.286078,6.929771,-8.680085,-4.777026,5.909139,0.423256,7.465074,5.460099,-6.403471,2.819375,-2.640922,3.769195,7.695169,-4.798028,7.182030,-8.622770,-7.000355,-4.987009,-1.618701,-8.690945,-9.840075,-0.513169,9.568367,-6.406864,-0.142493,2.292735,-6.205139,-2.186205,7.677298,1.878533,-7.865232,-5.509014,6.084579,-2.587670,-2.972184,2.186628,-3.131642,-6.575368,-9.250618,6.618748,-0.548222,7.276698,-1.701857,-1.579994,-1.324345,-2.647977,-5.527948,0.295520,9.229745,4.308271,-1.013686,6.931506,-7.641554,-8.152021,-3.289749,3.292739,9.228460,-0.170282,-9.703102,9.586904,-2.437990,-8.020059,2.882578,-7.689838,5.501461,-7.051234,1.229473,-1.050131,3.973038,-7.350549,-5.650743,-0.051981,-3.583405,9.225503,8.526966,2.544037,-0.477306,-9.921316,1.619516,1.257506,-5.775726,2.319633,2.888020,3.823545,-3.894691,-0.022044,4.305285,-2.373133,5.623401,7.206876,6.556278,-2.916411,-5.537399,7.958898,-4.940321,-1.141235,-3.073364,-3.260800,2.900128,-3.987826,4.471849,-2.067863,6.204218,-5.125442,8.792634,3.111956,-9.631726,-1.760755,6.788524,-5.301113,-8.529381,-0.895637,-4.722791,-6.033203,0.325865,-4.887465,-2.530847,1.685133,5.324978,-3.197346,2.922086,0.699440,-4.424769,-0.063012,6.550069,0.034774,4.275664,-0.141937,-1.970133,3.788511,7.945450,-7.221821,4.163738,6.966900,8.612771,9.494792,-7.445692,-9.911101,-7.727139,-8.966756,7.683161,-1.194817,9.084882,4.421358,5.198917,4.627555,-5.213263,-2.976960,-4.227658,-0.800046,-6.301778,-3.170707,7.462938,8.684560,-4.649310,1.326078,4.656946,-1.763106,3.963838,-4.359576,3.985740,7.279762,5.164783,9.620610,-7.123825,7.078824,8.138712,8.141773,-7.173353,-5.071255,-8.275776,-0.994269,9.525336,-6.564399,-8.594459,-8.624073,8.685032,8.275250,1.998109,-8.875060,2.132556,-2.721989,1.447955,3.967547,-8.608194,-4.056152,6.986671,-9.054240,-4.974584,0.747380,2.682848,-6.551785,-7.792355,2.028563,-0.305553,5.871111,3.090096,-4.598626,9.670585,-6.441798,2.293319,-9.483481,-5.499979,-2.826703,4.270375,8.455934,1.086953,7.663078,-9.092721,2.442554,-9.494004,-3.939444,3.541870,2.118550,-6.795096,-5.126277,-8.477595,-9.058374,-1.541976,4.827941,8.405250,-0.563624,-6.315008,-3.408516,1.210024,7.311917,-6.526368,0.256105,-3.436566,-4.337579,4.306901,5.298318,8.259323,-8.813694,-2.689229,8.642741,-3.277515,-4.095053,-3.872268,5.490290,-0.802025,6.465681,-3.459764,-5.383726,0.620804,0.795729,-5.807891,8.019275,6.063822,0.519451,5.617142,9.442958,-9.723070,9.526655,-2.575699,-3.780107,9.228018,2.226807,6.700381,9.708931,-7.245399,5.172508,3.569895,-4.068244,-5.634247,-1.163332,-8.304273,5.762466,4.620003,7.615555,-0.443214,-2.795381,-9.663837,8.397057,-1.709967,-5.643887,-2.679386,4.513768,-1.736940,-2.495716,3.726311,4.916463,-3.259101,-3.926393,3.260083,2.025770,-9.487071,3.365256,0.006182,-5.271694,6.688155,-6.925466,-9.870742,4.416590,5.325761,0.050162,-8.328197,-8.599520,0.569553,-7.686625,2.580658,-8.167971,-9.567498,-1.054812,3.241183,2.737128,7.060123,-8.020363,0.431642,5.152196,3.562181,0.416314,6.983055,-7.993447,-9.548196,6.127721,-0.650410,0.667865,6.464686,-9.499664,-9.669183,-6.516427,6.493400,5.043817,-1.123703,4.615268,2.524875,-6.428003,-5.690487,-8.532176,6.229931,-3.283661,8.576578,-2.775641,3.525950,6.172144,-7.872620,-5.963665,-7.642452,-7.445129,-1.131546,-2.309628,-3.247982,-1.810168,3.916407,-4.576533,-4.088069,-8.123287,-1.701380,-6.384504,8.004297,-5.232195,4.792501,1.580635,-6.223345,2.587315,9.196100,9.213219,-9.590225,2.470474,-1.497423,-1.236451,-0.846107,-1.378511,-1.863977,2.518752,7.075206,2.019037,-5.201432,-8.568824,2.251314,0.393278,-7.573615,-4.143194,-7.570982,-9.928183,9.771607,3.848222,-7.884563,0.080259,-6.016689,-0.087061,-8.060523,1.675602,6.374158,4.244308,3.962980,1.597872,7.836821,-3.391401,8.834523,-0.935425,3.041110,8.216249,-7.187628,-8.559215,0.540389,-0.609864,6.581775,-6.472926,1.083840,7.928404,-6.060872,-9.232594,-4.918706,2.843649,-0.920133,1.098557,4.576808,5.355569,5.291395,-2.228026,-6.713063,-0.237573,-0.493758,-3.082871,-7.102625,-3.812639,4.749994,8.826902,0.842937,5.898131,-9.599442,-8.775844,7.465069,3.271247,6.872666,7.710296,-8.316512,0.936969,-3.656557,8.723401,5.887064,4.804779,-4.254944,9.181604,0.978244,0.419347,2.726578,5.832599,7.018521,2.460088,9.649132,5.908799,-3.658690,-1.997871,-4.345573,2.676201,-9.120513,-8.565150,6.794882,-7.531606,7.534058,5.231549,0.650683,0.260930,7.015351,-6.520305,-8.930953,3.261131,-4.560022,1.900749,4.540475,5.095158,-0.698569,-7.232276,6.034474,-8.448597,3.957433,3.105714,6.185378,6.757384,8.954810,6.798476,7.995157,-7.213662,-6.636148,7.677132,-7.233110,8.885522,-5.056096,3.006722,3.462285,-1.717928,6.562756,9.701216,3.797824,4.036484,-9.936461,-1.578940,5.263463,-0.719297,-7.894640,9.805565,-2.284371,8.691520,9.329995,-2.849389,6.382565,8.357837,-8.090910,7.994664,3.740596,-1.689421,7.072081,-6.928566,6.732600,-7.872661,-6.135498,-2.351893,6.742852,4.382993,-5.332773,8.331280,8.527056,-1.609378,0.704475,3.113678,5.639967,6.901856,-4.688751,8.395906,-5.957374,4.473537,-1.145072,0.823524,-1.665929,-5.803418,-6.376456,-5.690838,-0.100868,9.756382,-7.631410,-5.430965,-6.806176,-9.624369,2.143752,-2.135129,6.178507,-4.921607,4.341129,2.449082,5.755786,5.776917,1.029914,8.896329,-8.562881,-1.952809,5.768405,-8.071219,-0.642072,-3.925303,2.273970,5.783200,-7.669410,-3.751245,3.093086,8.860853,8.150450,-4.220903,-2.862643,-5.985541,-9.791550,6.688720,1.604688,4.156086,-0.918212,-7.682570,-3.056953,9.354115,7.068661,-4.120646,5.967655,6.193480,-3.212546,-0.633555,0.130079,-3.803508,2.195035,7.097492,6.568413,-6.548950,-7.200614,8.256690,-4.012764,-8.996134,-3.438202,-7.780844,-2.645270,-1.184126,8.245564,-3.174867,7.620062,-8.306153,-4.962363,-6.947457,-5.927458,-1.673245,1.792575,2.168143,-1.387254,3.787578,-2.174001,-1.265104,-4.303531,-0.858366,2.038557,-5.625287,9.835088,5.201083,5.048296,7.923293,-7.408576,-4.543878,-7.547331,7.649142,9.223173,0.439319,-8.621792,0.675521,4.918015,-0.227741,-6.319689,0.544168,1.085858,2.116805,-8.853537,-2.877780,-5.284524,-9.779727,-6.548440,1.436000,5.647095,-7.200619,6.524021,-0.327339,5.186585,5.844811,1.461184,4.066727,-3.942384,9.479160,7.121967,3.370089,6.944873,-8.762073,-3.749743,5.151175,0.809974,5.529537,5.703672,3.895759,7.023805,-1.771391,9.032067,0.344798,1.069774,7.174801,8.120787,-1.751490,-2.639175,-6.532874,3.084386,-1.879486,4.365425,7.329830,5.260162,0.205062,1.332222,-4.248662,4.191255,-7.383545,-0.031224,-9.176251,7.218868,-0.987277,0.894727,-3.643788,2.022276,8.116636,-7.961318,3.396732,0.144212,-1.378857,8.076136,-9.002839,8.173129,8.310292,-3.500342,7.361868,-4.391124,6.967656,-3.083183,-4.315489,0.112603,8.608957,-0.466702,1.104409,9.893906,9.174029,-0.847724,-6.118095,-8.810388,-2.389182,5.151283,-9.568320,4.061567,9.120455,9.378436,9.652598,-6.672932,7.246129,-6.481383,-6.140116,-1.014786,-7.478398,0.084309,-2.055700,-4.261786,-4.650937,-7.538869,2.381513,2.505618,-1.423745,4.875797,0.895560,-8.967279,-5.302520,1.333980,-7.318658,-0.416376,8.387747,8.230002,-7.700128,-3.187739,6.661449,6.037348,-3.163253,-8.037714,-0.543852,7.448055,2.007818,-2.906418,-3.553577,-0.353056,0.821841,9.898977,2.046001,1.165042,-3.704161,-7.651850,-9.481294,-6.299994,-1.472445,6.650461,-2.352557,-5.129116,-1.374239,-5.741074,2.310504,-6.841499,4.568035,9.910305,-7.901433,-9.982456,-6.834806,4.479797,6.049007,1.627121,-7.300260,-5.415195,8.790211,-1.181276,5.092088,-6.694458,1.018157,7.576939,-5.982874,2.522620,4.219690,1.273463,3.758484,2.905149,5.891148,-8.011668,3.148810,-4.922055,-7.248660,2.415572,3.553157,-3.351583,-6.183160,-6.045146,-5.014481,3.121396,4.555797,3.178827,5.890261,3.262736,2.905090,-9.940625,-2.051566,-3.475912,4.432110,-4.337893,0.598767,-4.619962,5.644557,4.669789,-0.472986,7.184325,9.798187,-3.523506,6.767189,0.106865,-1.157893,-0.362199,1.695426,3.972515,-5.356492,2.928946,-0.360177,8.734814,-7.444295,5.511742,1.247023,1.509679,6.474457,-4.421701,3.071498,8.504091,5.925531,9.958130,-8.933069,-7.575344,-2.840773,9.358739,6.331930,-7.821137,4.569046,-7.466792,2.930175,7.216097,-1.221805,5.702201,-9.659840,9.286433,-2.366362,-6.150912,9.065265,7.246893,-8.303729,-8.531174,7.427921,-3.295322,-3.282668,-3.452159,-0.631183,-5.114685,4.447945,-1.082157,-8.515626,5.953184,-7.731383,-8.669601,-5.869856,-9.900768,-9.114832,-0.153916,3.373250,-9.965247,-5.987215,2.643449,-4.889275,1.249558,-7.063299,3.785876,2.892879,9.981711,-1.590356,6.386597,-2.083854,-6.303557,-6.184650,-0.607825,3.299356,0.891502,2.553500,-2.277441,-2.039630,4.642260,4.735146,9.359830,-2.665844,8.929736,-4.956780,3.991048,-7.511988,5.412027,7.623415,-7.182888,-3.080452,-5.874649,9.247080,-7.292370,-5.939306,-0.025622,-1.116356,-4.610871,-9.112336,-8.759003,-5.547912,8.798800,5.244682,6.850675,0.851552,7.435827,2.170878,2.663939,-5.010335,-8.570403,-6.908019,-4.546509,-6.085956,6.230749,-6.949028,-1.032009,3.729809,1.088227,-0.182795,9.690132,0.585751,-8.763781,-6.298462,5.594365,0.537941,6.938293,-0.300234,-7.319695,-6.077260,2.809841,1.286064,6.509411,-9.619647,0.593024,5.714503,-6.210327,8.873873,1.323095,-5.668157,-3.070134,-3.316315,7.630968,-7.785821,-2.911121,0.513701,8.405741,2.239790,-3.587227,-0.079217,-1.933534,-5.913105,-5.509516,4.480760,-9.363347,-2.830141,0.598442,-8.997871,9.914007,9.306854,-2.243341,6.546088,3.572134,-9.178873,-8.872584,-0.085922,8.443687,5.703716,-8.750216,1.355942,9.082610,-7.273363,7.560877,3.075876,1.864922,-6.170901,-2.745525,8.708176,-9.659815,2.342297,-5.434492,4.134154,-8.968598,5.439938,-4.977396,9.483535,-2.937790,-3.616570,7.148603,-2.918173,-2.711371,-0.599779,9.059539,9.385606,1.605296,-1.877273,-2.473127,2.316884,2.072693,6.777932,-8.689634,5.992711,-9.055618,-5.384246,2.241354,-0.734186,9.484348,-1.832994,1.804651,-4.737567,-7.448050,-6.850363,-9.219885,-7.118731,2.634760,9.303542,-1.261934,-6.649721,1.873448,-6.017041,-7.610460,-2.989393,6.473728,-6.137778,-2.484075,-6.545380,6.980764,5.494283,-2.032949,1.115959,-4.513770,5.180560,8.144975,7.566773,-0.025141,-0.489657,1.395534,-8.313593,7.520716,0.499977,0.178647,1.222580,-8.124509,8.254421,-4.184807], dtype = "float64")#candidate|11295|(1092,)|const|float64
call_11294 = relay.TupleGetItem(func_9494_call(relay.reshape(const_11295.astype('float64'), [14, 13, 6])), 1)
call_11296 = relay.TupleGetItem(func_9496_call(relay.reshape(const_11295.astype('float64'), [14, 13, 6])), 1)
func_10615_call = mod.get_global_var('func_10615')
func_10617_call = mutated_mod.get_global_var('func_10617')
call_11309 = relay.TupleGetItem(func_10615_call(), 0)
call_11310 = relay.TupleGetItem(func_10617_call(), 0)
output = relay.Tuple([call_11277,call_11290,call_11294,const_11295,call_11309,])
output2 = relay.Tuple([call_11278,call_11291,call_11296,const_11295,call_11310,])
func_11318 = relay.Function([], output)
mod['func_11318'] = func_11318
mod = relay.transform.InferType()(mod)
output = func_11318()
func_11319 = relay.Function([], output)
mutated_mod['func_11319'] = func_11319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8556_call = mod.get_global_var('func_8556')
func_8557_call = mutated_mod.get_global_var('func_8557')
call_11333 = relay.TupleGetItem(func_8556_call(), 0)
call_11334 = relay.TupleGetItem(func_8557_call(), 0)
output = call_11333
output2 = call_11334
func_11340 = relay.Function([], output)
mod['func_11340'] = func_11340
mod = relay.transform.InferType()(mod)
output = func_11340()
func_11341 = relay.Function([], output)
mutated_mod['func_11341'] = func_11341
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11366 = relay.var("var_11366", dtype = "uint16", shape = (5, 1, 2))#candidate|11366|(5, 1, 2)|var|uint16
var_11367 = relay.var("var_11367", dtype = "uint16", shape = (5, 1, 2))#candidate|11367|(5, 1, 2)|var|uint16
bop_11368 = relay.left_shift(var_11366.astype('uint16'), relay.reshape(var_11367.astype('uint16'), relay.shape_of(var_11366))) # shape=(5, 1, 2)
output = bop_11368
output2 = bop_11368
func_11396 = relay.Function([var_11366,var_11367,], output)
mod['func_11396'] = func_11396
mod = relay.transform.InferType()(mod)
mutated_mod['func_11396'] = func_11396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11396_call = mutated_mod.get_global_var('func_11396')
var_11398 = relay.var("var_11398", dtype = "uint16", shape = (5, 1, 2))#candidate|11398|(5, 1, 2)|var|uint16
var_11399 = relay.var("var_11399", dtype = "uint16", shape = (5, 1, 2))#candidate|11399|(5, 1, 2)|var|uint16
call_11397 = func_11396_call(var_11398,var_11399,)
output = call_11397
func_11400 = relay.Function([var_11398,var_11399,], output)
mutated_mod['func_11400'] = func_11400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10913_call = mod.get_global_var('func_10913')
func_10914_call = mutated_mod.get_global_var('func_10914')
call_11405 = relay.TupleGetItem(func_10913_call(), 0)
call_11406 = relay.TupleGetItem(func_10914_call(), 0)
output = call_11405
output2 = call_11406
func_11409 = relay.Function([], output)
mod['func_11409'] = func_11409
mod = relay.transform.InferType()(mod)
output = func_11409()
func_11410 = relay.Function([], output)
mutated_mod['func_11410'] = func_11410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7051_call = mod.get_global_var('func_7051')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_11419 = func_7051_call()
call_11420 = func_7051_call()
func_3789_call = mod.get_global_var('func_3789')
func_3793_call = mutated_mod.get_global_var('func_3793')
var_11437 = relay.var("var_11437", dtype = "float32", shape = (8,))#candidate|11437|(8,)|var|float32
const_11438 = relay.const([-3.747924,-0.579529,-4.676226,2.540489,-9.546704,4.686748,2.722531,-3.704126,8.472175,1.711451,-7.222808,4.449412,1.587088,1.791937,-1.260228,3.710655,-5.431107,-5.109997,-6.044830,-5.217706,-1.688376,-5.623349,1.224842,1.046155,1.200256,3.461040,5.040356,-0.852028,-4.398812,-3.062997,1.265172,2.700852,8.765986,-1.833672,7.631220,-0.777068,3.750093,-2.333399,-4.057910,7.754787,-3.384906,1.943396,6.134884,-9.034640,7.953307,8.904107,-0.427985,2.522700,-9.679472,6.352359,-3.736133,-3.263601,-6.070798,-2.429622,-4.388215,9.351451,-8.252173,-5.701778,-1.487188,-0.772916,3.799218,6.249531,-6.335977,5.916935,-7.870791,3.121709,5.253481,-1.483765,-2.336327,-1.337991,-2.819156,4.158904,-9.564802,4.295147,-9.645249,-2.708993,8.726870,-5.452732,-3.154151,-3.053506,-4.850898,-7.779152,0.910536,-3.481479,4.227435,-2.102118,-4.585496,9.834959,-7.037976,5.752376,-9.613207,-0.415498,1.774605,6.454095,7.870894,6.568863,4.122269,8.556864,-7.121118,-3.588896,-7.613200,-2.445491,-5.304931,3.092173], dtype = "float32")#candidate|11438|(104,)|const|float32
call_11436 = relay.TupleGetItem(func_3789_call(relay.reshape(var_11437.astype('float32'), [2, 4, 1]), relay.reshape(const_11438.astype('float32'), [2, 4, 13]), ), 0)
call_11439 = relay.TupleGetItem(func_3793_call(relay.reshape(var_11437.astype('float32'), [2, 4, 1]), relay.reshape(const_11438.astype('float32'), [2, 4, 13]), ), 0)
output = relay.Tuple([call_11419,call_11436,var_11437,const_11438,])
output2 = relay.Tuple([call_11420,call_11439,var_11437,const_11438,])
func_11449 = relay.Function([var_11437,], output)
mod['func_11449'] = func_11449
mod = relay.transform.InferType()(mod)
mutated_mod['func_11449'] = func_11449
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11450 = relay.var("var_11450", dtype = "float32", shape = (8,))#candidate|11450|(8,)|var|float32
func_11449_call = mutated_mod.get_global_var('func_11449')
call_11451 = func_11449_call(var_11450)
output = call_11451
func_11452 = relay.Function([var_11450], output)
mutated_mod['func_11452'] = func_11452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5816_call = mod.get_global_var('func_5816')
func_5818_call = mutated_mod.get_global_var('func_5818')
call_11512 = relay.TupleGetItem(func_5816_call(), 0)
call_11513 = relay.TupleGetItem(func_5818_call(), 0)
var_11524 = relay.var("var_11524", dtype = "float64", shape = (11, 3, 16))#candidate|11524|(11, 3, 16)|var|float64
bop_11525 = relay.multiply(call_11512.astype('uint64'), relay.reshape(var_11524.astype('uint64'), relay.shape_of(call_11512))) # shape=(11, 3, 16)
bop_11528 = relay.multiply(call_11513.astype('uint64'), relay.reshape(var_11524.astype('uint64'), relay.shape_of(call_11513))) # shape=(11, 3, 16)
output = relay.Tuple([bop_11525,])
output2 = relay.Tuple([bop_11528,])
func_11540 = relay.Function([var_11524,], output)
mod['func_11540'] = func_11540
mod = relay.transform.InferType()(mod)
var_11541 = relay.var("var_11541", dtype = "float64", shape = (11, 3, 16))#candidate|11541|(11, 3, 16)|var|float64
output = func_11540(var_11541)
func_11542 = relay.Function([var_11541], output)
mutated_mod['func_11542'] = func_11542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10544_call = mod.get_global_var('func_10544')
func_10545_call = mutated_mod.get_global_var('func_10545')
call_11565 = relay.TupleGetItem(func_10544_call(), 1)
call_11566 = relay.TupleGetItem(func_10545_call(), 1)
output = call_11565
output2 = call_11566
func_11574 = relay.Function([], output)
mod['func_11574'] = func_11574
mod = relay.transform.InferType()(mod)
output = func_11574()
func_11575 = relay.Function([], output)
mutated_mod['func_11575'] = func_11575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8625_call = mod.get_global_var('func_8625')
func_8626_call = mutated_mod.get_global_var('func_8626')
call_11593 = relay.TupleGetItem(func_8625_call(), 0)
call_11594 = relay.TupleGetItem(func_8626_call(), 0)
output = call_11593
output2 = call_11594
func_11595 = relay.Function([], output)
mod['func_11595'] = func_11595
mod = relay.transform.InferType()(mod)
output = func_11595()
func_11596 = relay.Function([], output)
mutated_mod['func_11596'] = func_11596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8891_call = mod.get_global_var('func_8891')
func_8893_call = mutated_mod.get_global_var('func_8893')
call_11615 = relay.TupleGetItem(func_8891_call(), 0)
call_11616 = relay.TupleGetItem(func_8893_call(), 0)
func_7554_call = mod.get_global_var('func_7554')
func_7558_call = mutated_mod.get_global_var('func_7558')
const_11623 = relay.const(-8, dtype = "uint64")#candidate|11623|()|const|uint64
var_11624 = relay.var("var_11624", dtype = "float32", shape = (180,))#candidate|11624|(180,)|var|float32
call_11622 = relay.TupleGetItem(func_7554_call(relay.reshape(const_11623.astype('uint64'), []), relay.reshape(var_11624.astype('float32'), [180,]), ), 2)
call_11625 = relay.TupleGetItem(func_7558_call(relay.reshape(const_11623.astype('uint64'), []), relay.reshape(var_11624.astype('float32'), [180,]), ), 2)
func_9773_call = mod.get_global_var('func_9773')
func_9774_call = mutated_mod.get_global_var('func_9774')
call_11627 = relay.TupleGetItem(func_9773_call(), 0)
call_11628 = relay.TupleGetItem(func_9774_call(), 0)
func_5870_call = mod.get_global_var('func_5870')
func_5871_call = mutated_mod.get_global_var('func_5871')
call_11634 = func_5870_call()
call_11635 = func_5870_call()
func_10188_call = mod.get_global_var('func_10188')
func_10190_call = mutated_mod.get_global_var('func_10190')
call_11646 = func_10188_call()
call_11647 = func_10188_call()
output = relay.Tuple([call_11615,call_11622,const_11623,var_11624,call_11627,call_11634,call_11646,])
output2 = relay.Tuple([call_11616,call_11625,const_11623,var_11624,call_11628,call_11635,call_11647,])
func_11650 = relay.Function([var_11624,], output)
mod['func_11650'] = func_11650
mod = relay.transform.InferType()(mod)
var_11651 = relay.var("var_11651", dtype = "float32", shape = (180,))#candidate|11651|(180,)|var|float32
output = func_11650(var_11651)
func_11652 = relay.Function([var_11651], output)
mutated_mod['func_11652'] = func_11652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8133_call = mod.get_global_var('func_8133')
func_8134_call = mutated_mod.get_global_var('func_8134')
call_11683 = relay.TupleGetItem(func_8133_call(), 2)
call_11684 = relay.TupleGetItem(func_8134_call(), 2)
output = relay.Tuple([call_11683,])
output2 = relay.Tuple([call_11684,])
func_11690 = relay.Function([], output)
mod['func_11690'] = func_11690
mod = relay.transform.InferType()(mod)
mutated_mod['func_11690'] = func_11690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11690_call = mutated_mod.get_global_var('func_11690')
call_11691 = func_11690_call()
output = call_11691
func_11692 = relay.Function([], output)
mutated_mod['func_11692'] = func_11692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8133_call = mod.get_global_var('func_8133')
func_8134_call = mutated_mod.get_global_var('func_8134')
call_11788 = relay.TupleGetItem(func_8133_call(), 0)
call_11789 = relay.TupleGetItem(func_8134_call(), 0)
func_11163_call = mod.get_global_var('func_11163')
func_11164_call = mutated_mod.get_global_var('func_11164')
call_11801 = relay.TupleGetItem(func_11163_call(), 0)
call_11802 = relay.TupleGetItem(func_11164_call(), 0)
output = relay.Tuple([call_11788,call_11801,])
output2 = relay.Tuple([call_11789,call_11802,])
func_11812 = relay.Function([], output)
mod['func_11812'] = func_11812
mod = relay.transform.InferType()(mod)
output = func_11812()
func_11813 = relay.Function([], output)
mutated_mod['func_11813'] = func_11813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6011_call = mutated_mod.get_global_var('func_6011')
call_11840 = relay.TupleGetItem(func_6009_call(), 0)
call_11841 = relay.TupleGetItem(func_6011_call(), 0)
output = relay.Tuple([call_11840,])
output2 = relay.Tuple([call_11841,])
func_11842 = relay.Function([], output)
mod['func_11842'] = func_11842
mod = relay.transform.InferType()(mod)
mutated_mod['func_11842'] = func_11842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11842_call = mutated_mod.get_global_var('func_11842')
call_11843 = func_11842_call()
output = call_11843
func_11844 = relay.Function([], output)
mutated_mod['func_11844'] = func_11844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9773_call = mod.get_global_var('func_9773')
func_9774_call = mutated_mod.get_global_var('func_9774')
call_11861 = relay.TupleGetItem(func_9773_call(), 0)
call_11862 = relay.TupleGetItem(func_9774_call(), 0)
func_8371_call = mod.get_global_var('func_8371')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_11863 = func_8371_call()
call_11864 = func_8371_call()
func_9494_call = mod.get_global_var('func_9494')
func_9496_call = mutated_mod.get_global_var('func_9496')
var_11877 = relay.var("var_11877", dtype = "float64", shape = (1092,))#candidate|11877|(1092,)|var|float64
call_11876 = relay.TupleGetItem(func_9494_call(relay.reshape(var_11877.astype('float64'), [14, 13, 6])), 0)
call_11878 = relay.TupleGetItem(func_9496_call(relay.reshape(var_11877.astype('float64'), [14, 13, 6])), 0)
func_6408_call = mod.get_global_var('func_6408')
func_6411_call = mutated_mod.get_global_var('func_6411')
var_11883 = relay.var("var_11883", dtype = "float32", shape = (180,))#candidate|11883|(180,)|var|float32
call_11882 = relay.TupleGetItem(func_6408_call(relay.reshape(var_11883.astype('float32'), [6, 30])), 2)
call_11884 = relay.TupleGetItem(func_6411_call(relay.reshape(var_11883.astype('float32'), [6, 30])), 2)
output = relay.Tuple([call_11861,call_11863,call_11876,var_11877,call_11882,var_11883,])
output2 = relay.Tuple([call_11862,call_11864,call_11878,var_11877,call_11884,var_11883,])
func_11892 = relay.Function([var_11877,var_11883,], output)
mod['func_11892'] = func_11892
mod = relay.transform.InferType()(mod)
var_11893 = relay.var("var_11893", dtype = "float64", shape = (1092,))#candidate|11893|(1092,)|var|float64
var_11894 = relay.var("var_11894", dtype = "float32", shape = (180,))#candidate|11894|(180,)|var|float32
output = func_11892(var_11893,var_11894,)
func_11895 = relay.Function([var_11893,var_11894,], output)
mutated_mod['func_11895'] = func_11895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_11906 = relay.TupleGetItem(func_5993_call(), 0)
call_11907 = relay.TupleGetItem(func_5995_call(), 0)
func_1061_call = mod.get_global_var('func_1061')
func_1063_call = mutated_mod.get_global_var('func_1063')
var_11909 = relay.var("var_11909", dtype = "float32", shape = (180,))#candidate|11909|(180,)|var|float32
call_11908 = relay.TupleGetItem(func_1061_call(relay.reshape(var_11909.astype('float32'), [4, 9, 5])), 1)
call_11910 = relay.TupleGetItem(func_1063_call(relay.reshape(var_11909.astype('float32'), [4, 9, 5])), 1)
func_11449_call = mod.get_global_var('func_11449')
func_11452_call = mutated_mod.get_global_var('func_11452')
const_11924 = relay.const([-8.867541,1.100122,-8.898885,3.138069,3.415556,0.880727,0.056188,2.273720], dtype = "float32")#candidate|11924|(8,)|const|float32
call_11923 = relay.TupleGetItem(func_11449_call(relay.reshape(const_11924.astype('float32'), [8,])), 1)
call_11925 = relay.TupleGetItem(func_11452_call(relay.reshape(const_11924.astype('float32'), [8,])), 1)
func_11318_call = mod.get_global_var('func_11318')
func_11319_call = mutated_mod.get_global_var('func_11319')
call_11953 = relay.TupleGetItem(func_11318_call(), 1)
call_11954 = relay.TupleGetItem(func_11319_call(), 1)
func_6979_call = mod.get_global_var('func_6979')
func_6982_call = mutated_mod.get_global_var('func_6982')
const_11957 = relay.const([[-4.418255],[-8.397789],[-4.464888],[-5.805112],[-6.460002],[0.449305],[-3.749447],[-2.477729],[-5.905479],[-1.942388],[2.215072],[-2.284751],[-6.577264],[1.482127],[1.681398],[-4.256080],[2.295988],[-3.155109],[5.361394],[-0.007419],[-4.249258],[-1.896969],[-6.224477],[2.297972],[2.379317],[-1.932971],[-4.125007],[2.798272],[-1.517553],[1.066400],[5.857499],[-2.067847],[6.324597],[-1.239555],[6.060442],[-3.397563],[-6.889668],[-2.034058],[2.874341],[-0.414289],[-4.643010],[-8.307315],[7.522745],[3.529009],[-1.072986],[-0.912947],[-2.700876],[-2.514405],[1.798457],[4.923702],[4.402355],[-6.417596],[-2.832372],[8.077679],[-9.741760],[-3.204914],[-4.568771],[7.309331],[-0.205758],[-0.688952],[6.517245],[-8.947161],[0.868396],[7.074987],[-0.431204],[6.171977],[-5.527461],[4.175261],[4.671403],[3.356129],[-1.390310],[-1.815402],[-1.396216],[8.461099],[-1.542397],[2.922249],[-8.529954],[-6.516279],[6.546073],[-2.365034],[-7.517786],[3.573723],[1.408252],[5.341528],[6.562538],[-3.905091],[-3.600471],[8.443559],[-0.305649],[9.929927],[-8.631740],[-8.438486],[-8.479528],[-6.700483],[4.914455],[2.363798],[-1.870944],[-4.504511],[-4.849879],[-6.577300],[-9.235294],[8.476352],[3.099906],[0.839154],[4.142264],[1.382171],[-8.269053],[-4.793950],[-8.300989],[-7.315370],[0.606089],[3.248274],[-8.606467],[4.831215],[4.076532],[2.393987],[-1.120101],[-9.266474],[8.260468],[2.582149],[-0.599087],[-9.659123],[0.551682],[5.071580],[4.178994],[0.396410],[-5.845965],[-1.343590],[-5.918872],[8.330318],[-0.309135],[-7.944027],[8.471501],[-2.525367],[-1.492122],[-4.325798],[-7.743548],[4.620458],[9.062772],[8.171672],[-3.999383],[-0.763555],[6.995462],[-9.877128],[-5.846597],[1.061089],[-3.617138],[-9.506438],[-4.421795],[-0.896768],[-1.038469],[6.388209],[5.991373],[-7.101562],[-9.075311],[5.095797],[-9.927578],[7.455078],[-1.708586],[-1.229918],[8.446276],[1.331966],[9.641592],[1.444176],[2.953660],[-9.544333],[-2.637395],[-5.393566],[9.940040],[6.075569],[4.946356],[-8.624384],[-2.128692],[1.546223],[6.187469],[1.201279],[-6.084554],[-4.506117],[-5.113126],[0.017782],[4.480479],[-0.226974],[-7.536207],[3.182420],[4.056267],[5.442510],[7.087217],[6.278242],[9.617150],[2.138300],[-3.870017],[7.772100],[8.349774],[-1.187657],[4.818689],[0.498023],[1.641619],[5.732088],[1.459260],[0.913065],[3.342082],[3.471183],[4.235459],[-0.535470],[3.504169],[3.617491],[-2.569479],[-9.944558],[6.991655],[-8.326314],[9.566831],[3.886938],[6.595776],[-1.583209],[-1.834513],[9.041619],[-6.507521],[-3.985962],[7.852135],[-4.952668],[-5.196343],[-3.821146],[-2.828654],[5.422421],[3.392442],[-6.389094],[9.616590],[-9.744893],[-0.218931],[1.846785],[-6.947108],[-7.728663],[6.541326],[-7.894157],[6.753917],[-5.526334],[7.793919],[6.817163],[6.567254],[6.071709],[-1.424989],[0.418966],[5.584578],[-3.084997],[-1.371907],[-0.856669],[-6.209131],[5.905226],[-9.631713],[2.575385],[-9.612086],[2.922680],[-3.210202],[8.076833],[6.328584],[2.530607],[4.541649],[-5.762289],[-4.966761],[-7.386465],[-1.372873],[0.809420],[-2.736968],[3.938015],[6.431558],[-3.099084],[-2.429684],[1.773176],[-7.009420],[-4.114850],[0.587675],[5.117761],[0.251699],[0.777270],[-7.047328],[-7.552609],[8.940455],[-2.540777],[3.001982],[-6.229274],[-2.073365],[-2.516256],[-8.493885],[3.559726],[1.075197],[8.011357],[7.971647],[3.018287],[-7.289379],[-7.122532],[-5.838779],[9.184627],[6.338833],[7.923280],[1.702250],[6.962085],[4.600523],[-3.730875],[3.826880],[-3.567121],[-8.699570],[5.737032],[2.303552],[-0.884332],[4.669846],[-3.461760],[8.497804],[7.355077],[7.996296],[3.387193],[-4.743391],[-0.868671],[2.728086],[-6.322246],[7.459203],[9.400609],[-9.772657],[3.417192],[3.637885],[2.592667],[4.714980],[-9.316015],[5.790208],[7.494877],[8.224182],[-9.395734],[0.006817],[4.933413],[0.304368],[0.540655],[-2.803813],[-2.129243],[7.173448],[-7.910820],[9.590138],[6.532222],[-3.868334],[-5.360095],[-1.729199],[-8.126425],[-0.677408],[2.468344],[-1.538295],[-6.056619],[-9.455625],[-3.680820],[-0.148099],[9.897337],[-3.401744],[-2.329873],[3.747820],[-4.348516],[-3.254868],[-3.258023],[-8.374503],[-3.840440],[8.448382],[-0.488330],[-5.949682],[5.971885],[-6.989213],[9.338776],[1.115972],[-1.686663],[5.925136],[0.188901],[9.596439],[-9.540211],[-8.754149],[-0.447494],[6.862673],[-7.748040],[-9.585540],[-4.775936],[0.599737],[-5.947220],[1.182136],[1.402015],[-6.805875],[7.324955],[-8.848050],[8.020799],[-1.205696],[8.795637],[-8.242620],[-3.015539],[-0.577566],[-1.225023],[0.767252],[1.363931],[-8.772404],[9.238364],[-8.295430],[-2.640753],[-2.775226],[-7.745182],[6.616841],[-8.675142],[7.856034],[-5.890400],[4.302081],[4.005650],[2.024639],[2.395037],[0.724074],[-5.346164],[-1.175698],[2.925983],[-1.495060],[9.763541],[3.725619],[3.812293],[2.862936],[2.454433],[-6.870932],[-9.521092],[-4.790204],[9.085886],[0.924883],[-0.426430],[-6.129151],[2.801145],[-3.565314],[8.344590],[-9.503014],[-6.451311],[-2.718381],[-0.663438],[9.546929],[-9.698753],[-0.697557],[-1.476762],[-5.226855],[-5.086018],[-7.728669],[-6.830837],[8.234675],[7.433451],[8.460745],[-8.334307],[3.310410],[9.128876],[4.027972],[-6.879703],[1.639508],[-9.396778],[8.919018],[-5.885518],[-9.823724],[-8.966764],[-2.726358],[2.182825],[-0.326728],[1.472388],[3.524242],[2.099909],[-9.150664],[-0.186329],[1.976231],[9.334813],[0.518746],[-1.404027],[-2.758414],[5.263458],[0.592236],[1.509680],[-2.631039],[-9.370974],[6.307951],[-8.231409],[0.898588],[2.030912],[9.641713],[5.519816],[-2.494808],[3.587278],[-9.354659],[8.766859],[8.217151],[-0.084936],[-8.215325],[-9.378925],[-9.050185],[7.144236],[-2.223120],[5.282562],[2.240196],[-0.988128],[-3.608449],[0.148545],[-6.225217],[2.490684],[-4.344271],[5.962638],[9.482445],[5.183071],[2.757807],[-3.883103],[-4.761392],[1.941323],[-4.555694],[-5.686515],[2.572973],[-7.978897],[6.277681],[7.309693],[-3.611008],[-8.550990],[8.485504],[-0.619565],[3.603540],[-0.335979],[0.312973],[2.574702],[-7.858918],[7.014773],[2.747520],[-4.681263],[-3.158775],[-7.669792],[2.350419],[9.782925],[-2.171629],[-0.561912],[9.559880],[-8.465900],[-8.537769],[5.609644],[-9.226752],[1.859169],[1.582669],[8.580049],[1.532588],[0.961898],[-6.626513],[9.925524],[0.542406],[1.829337],[-9.862499],[0.398642],[7.692733],[3.100379],[-6.291871],[3.091231],[1.092929],[5.099146],[3.530513],[7.340350],[0.524846],[-8.711862],[-1.539341],[0.386704],[-2.845258],[-9.159891],[-1.576890],[-9.079067],[4.604740],[-4.351131],[-5.162269],[-4.589845],[-2.525396],[-8.190692],[-3.725122],[-8.631747],[7.256456],[9.118934],[-4.151629],[4.346072],[-3.320812],[-0.561694],[-0.280709],[-7.890014],[-3.128211],[6.574371],[-4.896145],[-1.421409],[-8.554401],[4.541383],[-3.276776],[-3.674244],[-3.703346],[0.693017],[-6.756113],[-1.757246],[-0.879004],[1.091405],[5.823526],[7.849969],[-5.954697],[1.156547],[-7.544814],[-2.870733],[-5.920587],[-4.471888],[4.450395],[-0.960120],[-1.010634],[5.051956],[7.451468],[8.885475],[-8.684312],[-9.567409],[-7.261589],[7.010913],[-2.444572],[-1.076893],[-0.352808],[3.999384],[-1.261757],[6.974732],[-8.916322],[2.000045],[9.106938],[6.348454],[-3.511416],[4.526686],[-8.579807],[0.475066],[3.131120],[2.666602],[7.547055],[-2.102229],[-1.375387],[-8.975595]], dtype = "float32")#candidate|11957|(624, 1)|const|float32
call_11956 = relay.TupleGetItem(func_6979_call(relay.reshape(const_11957.astype('float32'), [624,])), 1)
call_11958 = relay.TupleGetItem(func_6982_call(relay.reshape(const_11957.astype('float32'), [624,])), 1)
output = relay.Tuple([call_11906,call_11908,var_11909,call_11923,const_11924,call_11953,call_11956,const_11957,])
output2 = relay.Tuple([call_11907,call_11910,var_11909,call_11925,const_11924,call_11954,call_11958,const_11957,])
func_11964 = relay.Function([var_11909,], output)
mod['func_11964'] = func_11964
mod = relay.transform.InferType()(mod)
mutated_mod['func_11964'] = func_11964
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11965 = relay.var("var_11965", dtype = "float32", shape = (180,))#candidate|11965|(180,)|var|float32
func_11964_call = mutated_mod.get_global_var('func_11964')
call_11966 = func_11964_call(var_11965)
output = call_11966
func_11967 = relay.Function([var_11965], output)
mutated_mod['func_11967'] = func_11967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11318_call = mod.get_global_var('func_11318')
func_11319_call = mutated_mod.get_global_var('func_11319')
call_11989 = relay.TupleGetItem(func_11318_call(), 2)
call_11990 = relay.TupleGetItem(func_11319_call(), 2)
var_11993 = relay.var("var_11993", dtype = "uint64", shape = (14, 13, 6))#candidate|11993|(14, 13, 6)|var|uint64
bop_11994 = relay.logical_and(call_11989.astype('bool'), relay.reshape(var_11993.astype('bool'), relay.shape_of(call_11989))) # shape=(14, 13, 6)
bop_11997 = relay.logical_and(call_11990.astype('bool'), relay.reshape(var_11993.astype('bool'), relay.shape_of(call_11990))) # shape=(14, 13, 6)
output = bop_11994
output2 = bop_11997
func_12017 = relay.Function([var_11993,], output)
mod['func_12017'] = func_12017
mod = relay.transform.InferType()(mod)
var_12018 = relay.var("var_12018", dtype = "uint64", shape = (14, 13, 6))#candidate|12018|(14, 13, 6)|var|uint64
output = func_12017(var_12018)
func_12019 = relay.Function([var_12018], output)
mutated_mod['func_12019'] = func_12019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11409_call = mod.get_global_var('func_11409')
func_11410_call = mutated_mod.get_global_var('func_11410')
call_12031 = func_11409_call()
call_12032 = func_11409_call()
func_10278_call = mod.get_global_var('func_10278')
func_10279_call = mutated_mod.get_global_var('func_10279')
call_12033 = relay.TupleGetItem(func_10278_call(), 2)
call_12034 = relay.TupleGetItem(func_10279_call(), 2)
func_7786_call = mod.get_global_var('func_7786')
func_7788_call = mutated_mod.get_global_var('func_7788')
call_12039 = relay.TupleGetItem(func_7786_call(), 1)
call_12040 = relay.TupleGetItem(func_7788_call(), 1)
output = relay.Tuple([call_12031,call_12033,call_12039,])
output2 = relay.Tuple([call_12032,call_12034,call_12040,])
func_12043 = relay.Function([], output)
mod['func_12043'] = func_12043
mod = relay.transform.InferType()(mod)
output = func_12043()
func_12044 = relay.Function([], output)
mutated_mod['func_12044'] = func_12044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10708_call = mod.get_global_var('func_10708')
func_10709_call = mutated_mod.get_global_var('func_10709')
call_12095 = func_10708_call()
call_12096 = func_10708_call()
output = relay.Tuple([call_12095,])
output2 = relay.Tuple([call_12096,])
func_12097 = relay.Function([], output)
mod['func_12097'] = func_12097
mod = relay.transform.InferType()(mod)
mutated_mod['func_12097'] = func_12097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12097_call = mutated_mod.get_global_var('func_12097')
call_12098 = func_12097_call()
output = call_12098
func_12099 = relay.Function([], output)
mutated_mod['func_12099'] = func_12099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8193_call = mod.get_global_var('func_8193')
func_8194_call = mutated_mod.get_global_var('func_8194')
call_12149 = relay.TupleGetItem(func_8193_call(), 0)
call_12150 = relay.TupleGetItem(func_8194_call(), 0)
output = call_12149
output2 = call_12150
func_12162 = relay.Function([], output)
mod['func_12162'] = func_12162
mod = relay.transform.InferType()(mod)
mutated_mod['func_12162'] = func_12162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12162_call = mutated_mod.get_global_var('func_12162')
call_12163 = func_12162_call()
output = call_12163
func_12164 = relay.Function([], output)
mutated_mod['func_12164'] = func_12164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8686_call = mod.get_global_var('func_8686')
func_8688_call = mutated_mod.get_global_var('func_8688')
call_12185 = relay.TupleGetItem(func_8686_call(), 1)
call_12186 = relay.TupleGetItem(func_8688_call(), 1)
func_10278_call = mod.get_global_var('func_10278')
func_10279_call = mutated_mod.get_global_var('func_10279')
call_12202 = relay.TupleGetItem(func_10278_call(), 0)
call_12203 = relay.TupleGetItem(func_10279_call(), 0)
func_7554_call = mod.get_global_var('func_7554')
func_7558_call = mutated_mod.get_global_var('func_7558')
var_12206 = relay.var("var_12206", dtype = "uint64", shape = ())#candidate|12206|()|var|uint64
var_12207 = relay.var("var_12207", dtype = "float32", shape = (180,))#candidate|12207|(180,)|var|float32
call_12205 = relay.TupleGetItem(func_7554_call(relay.reshape(var_12206.astype('uint64'), []), relay.reshape(var_12207.astype('float32'), [180,]), ), 3)
call_12208 = relay.TupleGetItem(func_7558_call(relay.reshape(var_12206.astype('uint64'), []), relay.reshape(var_12207.astype('float32'), [180,]), ), 3)
output = relay.Tuple([call_12185,call_12202,call_12205,var_12206,var_12207,])
output2 = relay.Tuple([call_12186,call_12203,call_12208,var_12206,var_12207,])
func_12230 = relay.Function([var_12206,var_12207,], output)
mod['func_12230'] = func_12230
mod = relay.transform.InferType()(mod)
mutated_mod['func_12230'] = func_12230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12230_call = mutated_mod.get_global_var('func_12230')
var_12232 = relay.var("var_12232", dtype = "uint64", shape = ())#candidate|12232|()|var|uint64
var_12233 = relay.var("var_12233", dtype = "float32", shape = (180,))#candidate|12233|(180,)|var|float32
call_12231 = func_12230_call(var_12232,var_12233,)
output = call_12231
func_12234 = relay.Function([var_12232,var_12233,], output)
mutated_mod['func_12234'] = func_12234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6924_call = mod.get_global_var('func_6924')
func_6925_call = mutated_mod.get_global_var('func_6925')
call_12253 = func_6924_call()
call_12254 = func_6924_call()
func_5932_call = mod.get_global_var('func_5932')
func_5934_call = mutated_mod.get_global_var('func_5934')
call_12271 = func_5932_call()
call_12272 = func_5932_call()
output = relay.Tuple([call_12253,call_12271,])
output2 = relay.Tuple([call_12254,call_12272,])
func_12273 = relay.Function([], output)
mod['func_12273'] = func_12273
mod = relay.transform.InferType()(mod)
output = func_12273()
func_12274 = relay.Function([], output)
mutated_mod['func_12274'] = func_12274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_12423 = relay.TupleGetItem(func_5509_call(), 3)
call_12424 = relay.TupleGetItem(func_5511_call(), 3)
func_10855_call = mod.get_global_var('func_10855')
func_10856_call = mutated_mod.get_global_var('func_10856')
call_12438 = relay.TupleGetItem(func_10855_call(), 0)
call_12439 = relay.TupleGetItem(func_10856_call(), 0)
var_12440 = relay.var("var_12440", dtype = "float64", shape = (15, 8, 15))#candidate|12440|(15, 8, 15)|var|float64
bop_12441 = relay.equal(call_12438.astype('bool'), relay.reshape(var_12440.astype('bool'), relay.shape_of(call_12438))) # shape=(15, 8, 15)
bop_12444 = relay.equal(call_12439.astype('bool'), relay.reshape(var_12440.astype('bool'), relay.shape_of(call_12439))) # shape=(15, 8, 15)
func_6769_call = mod.get_global_var('func_6769')
func_6771_call = mutated_mod.get_global_var('func_6771')
call_12452 = func_6769_call()
call_12453 = func_6769_call()
output = relay.Tuple([call_12423,bop_12441,call_12452,])
output2 = relay.Tuple([call_12424,bop_12444,call_12453,])
func_12455 = relay.Function([var_12440,], output)
mod['func_12455'] = func_12455
mod = relay.transform.InferType()(mod)
mutated_mod['func_12455'] = func_12455
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12456 = relay.var("var_12456", dtype = "float64", shape = (15, 8, 15))#candidate|12456|(15, 8, 15)|var|float64
func_12455_call = mutated_mod.get_global_var('func_12455')
call_12457 = func_12455_call(var_12456)
output = call_12457
func_12458 = relay.Function([var_12456], output)
mutated_mod['func_12458'] = func_12458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mod.get_global_var('func_5509')
func_5511_call = mutated_mod.get_global_var('func_5511')
call_12497 = relay.TupleGetItem(func_5509_call(), 0)
call_12498 = relay.TupleGetItem(func_5511_call(), 0)
uop_12503 = relay.sinh(call_12497.astype('float32')) # shape=(15, 8, 15)
uop_12505 = relay.sinh(call_12498.astype('float32')) # shape=(15, 8, 15)
output = relay.Tuple([uop_12503,])
output2 = relay.Tuple([uop_12505,])
func_12518 = relay.Function([], output)
mod['func_12518'] = func_12518
mod = relay.transform.InferType()(mod)
output = func_12518()
func_12519 = relay.Function([], output)
mutated_mod['func_12519'] = func_12519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9449_call = mod.get_global_var('func_9449')
func_9450_call = mutated_mod.get_global_var('func_9450')
call_12522 = relay.TupleGetItem(func_9449_call(), 0)
call_12523 = relay.TupleGetItem(func_9450_call(), 0)
output = call_12522
output2 = call_12523
func_12531 = relay.Function([], output)
mod['func_12531'] = func_12531
mod = relay.transform.InferType()(mod)
output = func_12531()
func_12532 = relay.Function([], output)
mutated_mod['func_12532'] = func_12532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8371_call = mod.get_global_var('func_8371')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_12536 = func_8371_call()
call_12537 = func_8371_call()
output = call_12536
output2 = call_12537
func_12557 = relay.Function([], output)
mod['func_12557'] = func_12557
mod = relay.transform.InferType()(mod)
mutated_mod['func_12557'] = func_12557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12557_call = mutated_mod.get_global_var('func_12557')
call_12558 = func_12557_call()
output = call_12558
func_12559 = relay.Function([], output)
mutated_mod['func_12559'] = func_12559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11812_call = mod.get_global_var('func_11812')
func_11813_call = mutated_mod.get_global_var('func_11813')
call_12587 = relay.TupleGetItem(func_11812_call(), 1)
call_12588 = relay.TupleGetItem(func_11813_call(), 1)
output = call_12587
output2 = call_12588
func_12589 = relay.Function([], output)
mod['func_12589'] = func_12589
mod = relay.transform.InferType()(mod)
mutated_mod['func_12589'] = func_12589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12589_call = mutated_mod.get_global_var('func_12589')
call_12590 = func_12589_call()
output = call_12590
func_12591 = relay.Function([], output)
mutated_mod['func_12591'] = func_12591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11340_call = mod.get_global_var('func_11340')
func_11341_call = mutated_mod.get_global_var('func_11341')
call_12627 = func_11340_call()
call_12628 = func_11340_call()
output = call_12627
output2 = call_12628
func_12635 = relay.Function([], output)
mod['func_12635'] = func_12635
mod = relay.transform.InferType()(mod)
mutated_mod['func_12635'] = func_12635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12635_call = mutated_mod.get_global_var('func_12635')
call_12636 = func_12635_call()
output = call_12636
func_12637 = relay.Function([], output)
mutated_mod['func_12637'] = func_12637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7854_call = mod.get_global_var('func_7854')
func_7856_call = mutated_mod.get_global_var('func_7856')
call_12638 = relay.TupleGetItem(func_7854_call(), 0)
call_12639 = relay.TupleGetItem(func_7856_call(), 0)
output = relay.Tuple([call_12638,])
output2 = relay.Tuple([call_12639,])
func_12654 = relay.Function([], output)
mod['func_12654'] = func_12654
mod = relay.transform.InferType()(mod)
mutated_mod['func_12654'] = func_12654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12654_call = mutated_mod.get_global_var('func_12654')
call_12655 = func_12654_call()
output = call_12655
func_12656 = relay.Function([], output)
mutated_mod['func_12656'] = func_12656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_12659 = func_5645_call()
call_12660 = func_5645_call()
output = call_12659
output2 = call_12660
func_12661 = relay.Function([], output)
mod['func_12661'] = func_12661
mod = relay.transform.InferType()(mod)
output = func_12661()
func_12662 = relay.Function([], output)
mutated_mod['func_12662'] = func_12662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mod.get_global_var('func_6126')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_12700 = func_6126_call()
call_12701 = func_6126_call()
output = call_12700
output2 = call_12701
func_12704 = relay.Function([], output)
mod['func_12704'] = func_12704
mod = relay.transform.InferType()(mod)
output = func_12704()
func_12705 = relay.Function([], output)
mutated_mod['func_12705'] = func_12705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12162_call = mod.get_global_var('func_12162')
func_12164_call = mutated_mod.get_global_var('func_12164')
call_12714 = func_12162_call()
call_12715 = func_12162_call()
func_7328_call = mod.get_global_var('func_7328')
func_7331_call = mutated_mod.get_global_var('func_7331')
var_12717 = relay.var("var_12717", dtype = "bool", shape = (720,))#candidate|12717|(720,)|var|bool
call_12716 = relay.TupleGetItem(func_7328_call(relay.reshape(var_12717.astype('bool'), [720,])), 1)
call_12718 = relay.TupleGetItem(func_7331_call(relay.reshape(var_12717.astype('bool'), [720,])), 1)
func_4196_call = mod.get_global_var('func_4196')
func_4201_call = mutated_mod.get_global_var('func_4201')
const_12725 = relay.const([4,-10,-4,-3,-6,6,-8,-2,-10,6,8,-2,-10,-1,-5,-1,-10,10,-3,10,-1,-1,3,-4,2,8,5,-7,5,1,4,8,5,8,3,9,-4,-5,-6,2,8,-9,2,-2,-4,6,7,4,4,-1,-1,10,-1,-4,3,-6,-8,6,1,-6,10,-4,5,-8,1,-5,10,-10,2,9,-2,8,9,9,-3,6,-4,-2,-8,8,-10,2,8,-10,-5,-8,3,6,-2,-4,7,-10,-10,-10,5,-6,10,-4,9,1,-4,-1,-4,8,2,-1,-2,10,5,8,7,-4,3,9,5,-8,-6,-5,5,-6,-5,-6,10,-7,-3,7,-1,10,3,8,9,5,4,-8,3,-8,3,-5,7,9,9,3,-9,5,-2,7,6,9,-4,-1,-2,-7,-10,-7,-4,-8,-2,-2,3,10,8,-1,3,-6,-8,6,-5,-3,5,3,-6,-4,-3,-9,4,6,-1,8,-8,3,-3,-5,3,-7,-10,10,3,-6,10,5,-9,8,9,-3,2,2,-8,6,-7,-2,3,-4,-7,5,8,-3,-2,-4,-7,-7,-7,-4,7,8,3,8,-3,-2,-3,-10,-8,5,-4,-2,-9,7,9,-3,-1,8,-1,10,1,6,3,-4,-1,-3,-1,3,6,-8,-3,-1,1,10,10,-6,6,-4,8,-9,8,-3,7,-10,5,-7,-8,5,-10,1,-5,-10,9,-7,1,-7,8,-9,-3,7,7,-8,-4,4,8,-3,-2,-3,6,-7,7,-7,3,9,7,6,4,10,-9,-2,-10,9,10,3,1,5,6,-3,10,-7,-10,10,8,-1,-4,3,10,8,-1,7,4,10,-6,1,4,10,10,7,-9,7,3,-1,-2,-4,1,7,-5,-7], dtype = "uint8")#candidate|12725|(330,)|const|uint8
const_12726 = relay.const([-9.743979,5.359684,8.637116,5.868958,-3.995018,1.252042,5.675611,6.234119,-3.262738,-0.409674,2.318835,-0.098941,6.892913,1.239570,-0.418311,-3.600679,-1.777833,-5.100499,-6.153918,-7.256516,-8.294430,-1.683277,-7.420339,-8.472003,-4.127073,1.570063,1.698506,-4.999713,1.489954,9.303078,4.552657,-4.233736,-6.479810,-8.426138,-8.071129,8.093983,-7.906002,9.488821,7.289058,7.280768,-5.011338,5.232514,-1.435909,-2.719571,-5.529413,-4.376881,-3.107656,4.982626,0.241743,7.424781,-8.751180,-9.251326,-2.090894,7.387576,-3.512752,5.968224,4.600091,-8.950781,-9.529287,2.856337,-4.975488,2.168940,6.134541,0.456078,-4.923410,-8.883655,-3.903595,8.129464,-6.582050,-4.652530,-9.078459,-1.788353,3.948620,0.098438,9.243296,-9.718398,-8.288396,-6.502150,-2.266607,-1.763353,-7.864635,-4.125953,-9.542562,4.093060,-0.782290,9.730263,-1.648046,7.331913,-7.554561,9.768894,8.430603,9.927440,9.769568,7.049116,-7.366889,-3.974304,9.679643,2.609796,6.597286,-3.123759,-8.755385,-8.629678,3.533265,-8.446223,-5.064631,-0.084824,9.738901,-3.863741,8.234129,9.108904,8.574946,3.108642,-1.824798,-9.355613,5.264316,1.298545,-6.070540,-3.646484,7.980597,7.900933,5.791216,-7.578414,-0.032503,6.304122,-9.428538,2.945872,9.812192,-3.566305,9.226413,3.146140,-8.164764,-7.875058,-6.259825,-5.940685,-0.626314,3.637910,8.807527,-5.262751,-8.961195,-9.060313,-6.719902,3.556260,-5.947347,5.191108,-2.630450,-3.297058,-5.392399,-4.452889,-2.783074,-9.454557,-7.299193,-9.637095,4.301634,2.856299,-4.930857,5.807815,3.795155,-4.555524,-1.126123,1.392055,-9.907354,1.470231,4.926625,6.613677,8.209919,-4.971570,-5.109773,5.119793,6.038329,2.304982,-7.880118,8.544529,3.445173,8.403465,1.542967,6.357588,6.710132,-3.671087,-2.862050,-9.591169,-4.530951,3.422541,9.722224,-5.654143,-9.475095,-2.259018,-1.765612,-7.058038,-8.058062,-4.641326,5.603928,4.665225,-7.634274,0.520749,-8.532367,-6.079034,-7.498356,4.782999,3.784426,-4.804896,8.630343,-3.205205,-9.209750,-5.297603,6.159586,7.395880,-1.552245,0.120119,-1.795598,0.145627,-0.406869,8.452976,7.305969,-5.994936,3.994404,-5.144666,0.507213,-2.071003,-1.717347,-9.511335,7.131029,-7.756820,1.333522,9.574074,-6.814541,-5.613046,-7.757712,6.406862,-5.082244,-0.532113,-2.300500,-4.538475,-0.508181,-4.272287,0.957694,-0.113691,-0.153757,-3.052908,-3.787750,5.558844,-0.379064,1.762488,-7.368643,0.398458,-0.757019,-9.710546,-1.975802,-0.770194,4.287072,7.070811,-0.726388,-8.881790,-7.991763,-7.884499,-6.455527,7.394311,7.014078,6.701369,3.131056,-8.649482,4.211557,5.636440,3.177442,-7.472018,-3.698571,-6.258001,6.468159,7.678749,7.833041,-4.487674,3.674310,9.451903,-0.131329,-9.960736,3.135260,5.943859,6.842453,-7.304154,-7.878881,-6.617753,3.470896,7.909200,9.362128,-2.755595,-6.591195,-7.134356,2.947686,-5.528366,-4.152587,1.303139,9.187855,-4.868596,3.621978,-4.887818,9.395211,-7.313121,7.903070,1.271274,-8.665467,5.545305,-4.108254,1.945890,7.920056,3.697218,-7.316692,4.667535,4.347357,0.508759,7.074900,8.149302,-5.673731,2.694045,3.035941,-5.977582,-3.088740,5.592942,8.039314,-7.467246,-4.504526,-2.487075,7.075084,7.130719,-2.004858,9.977188,-0.927526,-5.013020,0.109553,-6.188627,6.283083,-3.901006,-8.028420,-0.847003,-4.090911,8.343755,4.308168,-5.363887,9.432789,5.338675,-5.662604,0.874065,4.660038,6.605280,0.030539,-4.832549,-1.858954,6.077483,-6.327772,-3.817063,-9.641448,1.959491,9.234774,-1.472769,9.569422,-6.313235,2.170869,-0.082477,-5.742085,1.828319,4.057421,-1.661674,-5.001203,7.060316,6.189423,-1.259454,2.834612,4.967934,3.974577,2.579157,-6.708981,-2.668457,-4.355926,-1.750395,-4.416375,-6.478582,3.519466,8.976916,-4.284201,-6.951167,-9.208551,-3.203350,0.153486,-0.422643,4.621639,4.490188,-1.275539,8.412512,3.108515,9.515807,9.553002,7.908960,-7.717032,9.819912,2.758568,-5.378351,-8.721720,4.864298,3.368015,-7.672574,-8.679986,-5.873018,5.810756,4.976335,6.297587,-2.179702,-0.501671,-8.841736,-5.161133,-4.841724,4.894617,7.365797,8.079467,0.314764,-1.249523,7.360860,-5.774023,5.985685,-9.754630,-9.961230,6.437702,-7.378332,-7.053269,-2.490769,-2.369986,3.514376,-5.098193,2.232028,7.841415,-4.675270,-0.374692,-8.500545,5.741980,-8.231327,-6.811865,5.981982,7.011551,-0.029061,-5.030560,-9.623911,2.318902,0.072328,-3.823674,2.955682,3.593081,-9.375787,1.588999,-6.441727,-0.234680,-2.648476,7.471754,8.096156,-7.940028,6.836295,-5.898668,8.849529,0.050101,6.148864,-4.925492,6.848005,-4.869185,3.089696,3.841209,-3.453743,7.630316,-5.807721,6.281604,3.621420,1.650278,-2.238608,5.894658,0.273915,-8.124457,-9.366383,5.383285,0.129527,9.900819,-4.391707,-1.565147,6.822347,7.580564,0.390274,3.579885,-9.979833,5.556422,-2.523683,6.243988,9.790260,5.971681,-7.129776,2.902640,-0.485117,-4.508626,1.903324,-2.108159,-2.684533,9.824081,-4.305537,2.489176,2.803147,4.552842,4.972898,-7.911870,5.065530,-9.919525,-0.352742,2.255682,2.922649,9.686637,-4.951720,8.154175,-3.927853,-9.600743,1.603517,7.413420,-9.593454,-9.905787,8.544501,-8.021960,-9.848304,-1.922125,9.191728,-6.793145,-1.588218,8.973463,2.874363,2.925345,9.622715,-0.795346,3.287325,-0.894528,-5.360165,9.728166,2.863693,-6.868234,9.625426,-5.269254,-6.630909,6.159829,9.405603,-9.908443,4.929212,-5.317503,5.234907,7.919346,-1.779951,0.287017,-9.428942,3.235925,-8.725650,-8.237755,-5.924144,-7.182008,3.772077,7.088235,8.640837,3.383837,-7.823381,7.869182,-8.201172,-0.144250,-3.829314,6.903973,0.419304,-7.775512,9.691583,0.440014,-4.049430,-7.523034,6.678580,-5.753329,0.403621,3.331211,2.200542,-0.531628,4.571634,-0.230260,-2.747532,-0.537172,-4.831908,9.668744,0.948545,-6.948987,9.045894,0.870022,-2.043356,4.006048,6.668138,7.652106,0.960439,-7.422131,4.972137,5.442236,3.802596,2.464774,-9.865066,1.057666,8.893447,1.121699,-2.062999,4.155132,-2.960601,8.216201,4.440261,-2.497306,-6.736322,3.406733,-8.986861,7.610735,-7.916445,7.753674,9.132064,0.683263,-0.267392,5.025791,9.406981,-1.612711,8.309513,-3.357312,-2.985196,-2.284385,9.485594,-0.180329,-6.332853,5.766391,-2.616891], dtype = "float32")#candidate|12726|(624,)|const|float32
const_12727 = relay.const(-7, dtype = "uint32")#candidate|12727|()|const|uint32
call_12724 = relay.TupleGetItem(func_4196_call(relay.reshape(const_12725.astype('uint8'), [2, 11, 15]), relay.reshape(const_12725.astype('uint8'), [2, 11, 15]), relay.reshape(const_12726.astype('float32'), [624,]), relay.reshape(const_12727.astype('uint32'), []), ), 0)
call_12728 = relay.TupleGetItem(func_4201_call(relay.reshape(const_12725.astype('uint8'), [2, 11, 15]), relay.reshape(const_12725.astype('uint8'), [2, 11, 15]), relay.reshape(const_12726.astype('float32'), [624,]), relay.reshape(const_12727.astype('uint32'), []), ), 0)
func_7420_call = mod.get_global_var('func_7420')
func_7422_call = mutated_mod.get_global_var('func_7422')
call_12741 = relay.TupleGetItem(func_7420_call(), 0)
call_12742 = relay.TupleGetItem(func_7422_call(), 0)
output = relay.Tuple([call_12714,call_12716,var_12717,call_12724,const_12725,const_12726,const_12727,call_12741,])
output2 = relay.Tuple([call_12715,call_12718,var_12717,call_12728,const_12725,const_12726,const_12727,call_12742,])
func_12749 = relay.Function([var_12717,], output)
mod['func_12749'] = func_12749
mod = relay.transform.InferType()(mod)
var_12750 = relay.var("var_12750", dtype = "bool", shape = (720,))#candidate|12750|(720,)|var|bool
output = func_12749(var_12750)
func_12751 = relay.Function([var_12750], output)
mutated_mod['func_12751'] = func_12751
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12774 = relay.var("var_12774", dtype = "bool", shape = ())#candidate|12774|()|var|bool
var_12775 = relay.var("var_12775", dtype = "bool", shape = (8, 9, 10))#candidate|12775|(8, 9, 10)|var|bool
bop_12776 = relay.logical_and(var_12774.astype('bool'), var_12775.astype('bool')) # shape=(8, 9, 10)
output = bop_12776
output2 = bop_12776
func_12798 = relay.Function([var_12774,var_12775,], output)
mod['func_12798'] = func_12798
mod = relay.transform.InferType()(mod)
mutated_mod['func_12798'] = func_12798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12798_call = mutated_mod.get_global_var('func_12798')
var_12800 = relay.var("var_12800", dtype = "bool", shape = ())#candidate|12800|()|var|bool
var_12801 = relay.var("var_12801", dtype = "bool", shape = (8, 9, 10))#candidate|12801|(8, 9, 10)|var|bool
call_12799 = func_12798_call(var_12800,var_12801,)
output = call_12799
func_12802 = relay.Function([var_12800,var_12801,], output)
mutated_mod['func_12802'] = func_12802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7148_call = mod.get_global_var('func_7148')
func_7150_call = mutated_mod.get_global_var('func_7150')
call_12815 = relay.TupleGetItem(func_7148_call(), 1)
call_12816 = relay.TupleGetItem(func_7150_call(), 1)
func_7132_call = mod.get_global_var('func_7132')
func_7138_call = mutated_mod.get_global_var('func_7138')
var_12827 = relay.var("var_12827", dtype = "int8", shape = (864,))#candidate|12827|(864,)|var|int8
var_12828 = relay.var("var_12828", dtype = "int64", shape = (630,))#candidate|12828|(630,)|var|int64
var_12829 = relay.var("var_12829", dtype = "bool", shape = (8, 140))#candidate|12829|(8, 140)|var|bool
var_12830 = relay.var("var_12830", dtype = "float32", shape = (180,))#candidate|12830|(180,)|var|float32
call_12826 = relay.TupleGetItem(func_7132_call(relay.reshape(var_12827.astype('int8'), [8, 9, 12]), relay.reshape(var_12828.astype('int64'), [630,]), relay.reshape(var_12829.astype('bool'), [1, 1120]), relay.reshape(var_12830.astype('float32'), [180,]), ), 4)
call_12831 = relay.TupleGetItem(func_7138_call(relay.reshape(var_12827.astype('int8'), [8, 9, 12]), relay.reshape(var_12828.astype('int64'), [630,]), relay.reshape(var_12829.astype('bool'), [1, 1120]), relay.reshape(var_12830.astype('float32'), [180,]), ), 4)
output = relay.Tuple([call_12815,call_12826,var_12827,var_12828,var_12829,var_12830,])
output2 = relay.Tuple([call_12816,call_12831,var_12827,var_12828,var_12829,var_12830,])
func_12834 = relay.Function([var_12827,var_12828,var_12829,var_12830,], output)
mod['func_12834'] = func_12834
mod = relay.transform.InferType()(mod)
var_12835 = relay.var("var_12835", dtype = "int8", shape = (864,))#candidate|12835|(864,)|var|int8
var_12836 = relay.var("var_12836", dtype = "int64", shape = (630,))#candidate|12836|(630,)|var|int64
var_12837 = relay.var("var_12837", dtype = "bool", shape = (8, 140))#candidate|12837|(8, 140)|var|bool
var_12838 = relay.var("var_12838", dtype = "float32", shape = (180,))#candidate|12838|(180,)|var|float32
output = func_12834(var_12835,var_12836,var_12837,var_12838,)
func_12839 = relay.Function([var_12835,var_12836,var_12837,var_12838,], output)
mutated_mod['func_12839'] = func_12839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6429_call = mod.get_global_var('func_6429')
func_6430_call = mutated_mod.get_global_var('func_6430')
call_12877 = func_6429_call()
call_12878 = func_6429_call()
func_6790_call = mod.get_global_var('func_6790')
func_6792_call = mutated_mod.get_global_var('func_6792')
call_12881 = relay.TupleGetItem(func_6790_call(), 0)
call_12882 = relay.TupleGetItem(func_6792_call(), 0)
func_5958_call = mod.get_global_var('func_5958')
func_5961_call = mutated_mod.get_global_var('func_5961')
const_12919 = relay.const([[-8.860151,5.331828,-5.989193,1.641655,-9.886334,4.326213,-3.402750,1.423139]], dtype = "float32")#candidate|12919|(1, 8)|const|float32
call_12918 = relay.TupleGetItem(func_5958_call(relay.reshape(const_12919.astype('float32'), [8, 1])), 2)
call_12920 = relay.TupleGetItem(func_5961_call(relay.reshape(const_12919.astype('float32'), [8, 1])), 2)
func_8000_call = mod.get_global_var('func_8000')
func_8002_call = mutated_mod.get_global_var('func_8002')
call_12922 = relay.TupleGetItem(func_8000_call(), 0)
call_12923 = relay.TupleGetItem(func_8002_call(), 0)
output = relay.Tuple([call_12877,call_12881,call_12918,const_12919,call_12922,])
output2 = relay.Tuple([call_12878,call_12882,call_12920,const_12919,call_12923,])
func_12935 = relay.Function([], output)
mod['func_12935'] = func_12935
mod = relay.transform.InferType()(mod)
output = func_12935()
func_12936 = relay.Function([], output)
mutated_mod['func_12936'] = func_12936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7935_call = mod.get_global_var('func_7935')
func_7937_call = mutated_mod.get_global_var('func_7937')
call_12978 = relay.TupleGetItem(func_7935_call(), 0)
call_12979 = relay.TupleGetItem(func_7937_call(), 0)
output = call_12978
output2 = call_12979
func_12998 = relay.Function([], output)
mod['func_12998'] = func_12998
mod = relay.transform.InferType()(mod)
output = func_12998()
func_12999 = relay.Function([], output)
mutated_mod['func_12999'] = func_12999
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13012 = relay.var("var_13012", dtype = "int64", shape = ())#candidate|13012|()|var|int64
var_13013 = relay.var("var_13013", dtype = "int64", shape = (1, 13, 5))#candidate|13013|(1, 13, 5)|var|int64
bop_13014 = relay.bitwise_xor(var_13012.astype('int64'), var_13013.astype('int64')) # shape=(1, 13, 5)
output = relay.Tuple([bop_13014,])
output2 = relay.Tuple([bop_13014,])
func_13020 = relay.Function([var_13012,var_13013,], output)
mod['func_13020'] = func_13020
mod = relay.transform.InferType()(mod)
var_13021 = relay.var("var_13021", dtype = "int64", shape = ())#candidate|13021|()|var|int64
var_13022 = relay.var("var_13022", dtype = "int64", shape = (1, 13, 5))#candidate|13022|(1, 13, 5)|var|int64
output = func_13020(var_13021,var_13022,)
func_13023 = relay.Function([var_13021,var_13022,], output)
mutated_mod['func_13023'] = func_13023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8371_call = mod.get_global_var('func_8371')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_13053 = func_8371_call()
call_13054 = func_8371_call()
func_11690_call = mod.get_global_var('func_11690')
func_11692_call = mutated_mod.get_global_var('func_11692')
call_13055 = relay.TupleGetItem(func_11690_call(), 0)
call_13056 = relay.TupleGetItem(func_11692_call(), 0)
func_7051_call = mod.get_global_var('func_7051')
func_7053_call = mutated_mod.get_global_var('func_7053')
call_13058 = func_7051_call()
call_13059 = func_7051_call()
func_9773_call = mod.get_global_var('func_9773')
func_9774_call = mutated_mod.get_global_var('func_9774')
call_13064 = relay.TupleGetItem(func_9773_call(), 0)
call_13065 = relay.TupleGetItem(func_9774_call(), 0)
output = relay.Tuple([call_13053,call_13055,call_13058,call_13064,])
output2 = relay.Tuple([call_13054,call_13056,call_13059,call_13065,])
func_13076 = relay.Function([], output)
mod['func_13076'] = func_13076
mod = relay.transform.InferType()(mod)
output = func_13076()
func_13077 = relay.Function([], output)
mutated_mod['func_13077'] = func_13077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8258_call = mod.get_global_var('func_8258')
func_8259_call = mutated_mod.get_global_var('func_8259')
call_13115 = relay.TupleGetItem(func_8258_call(), 1)
call_13116 = relay.TupleGetItem(func_8259_call(), 1)
output = call_13115
output2 = call_13116
func_13132 = relay.Function([], output)
mod['func_13132'] = func_13132
mod = relay.transform.InferType()(mod)
mutated_mod['func_13132'] = func_13132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13132_call = mutated_mod.get_global_var('func_13132')
call_13133 = func_13132_call()
output = call_13133
func_13134 = relay.Function([], output)
mutated_mod['func_13134'] = func_13134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8891_call = mod.get_global_var('func_8891')
func_8893_call = mutated_mod.get_global_var('func_8893')
call_13185 = relay.TupleGetItem(func_8891_call(), 0)
call_13186 = relay.TupleGetItem(func_8893_call(), 0)
output = call_13185
output2 = call_13186
func_13195 = relay.Function([], output)
mod['func_13195'] = func_13195
mod = relay.transform.InferType()(mod)
mutated_mod['func_13195'] = func_13195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13195_call = mutated_mod.get_global_var('func_13195')
call_13196 = func_13195_call()
output = call_13196
func_13197 = relay.Function([], output)
mutated_mod['func_13197'] = func_13197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11318_call = mod.get_global_var('func_11318')
func_11319_call = mutated_mod.get_global_var('func_11319')
call_13207 = relay.TupleGetItem(func_11318_call(), 2)
call_13208 = relay.TupleGetItem(func_11319_call(), 2)
var_13218 = relay.var("var_13218", dtype = "uint64", shape = (14, 13, 6))#candidate|13218|(14, 13, 6)|var|uint64
bop_13219 = relay.floor_mod(call_13207.astype('float64'), relay.reshape(var_13218.astype('float64'), relay.shape_of(call_13207))) # shape=(14, 13, 6)
bop_13222 = relay.floor_mod(call_13208.astype('float64'), relay.reshape(var_13218.astype('float64'), relay.shape_of(call_13208))) # shape=(14, 13, 6)
output = bop_13219
output2 = bop_13222
func_13224 = relay.Function([var_13218,], output)
mod['func_13224'] = func_13224
mod = relay.transform.InferType()(mod)
var_13225 = relay.var("var_13225", dtype = "uint64", shape = (14, 13, 6))#candidate|13225|(14, 13, 6)|var|uint64
output = func_13224(var_13225)
func_13226 = relay.Function([var_13225], output)
mutated_mod['func_13226'] = func_13226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6365_call = mod.get_global_var('func_6365')
func_6367_call = mutated_mod.get_global_var('func_6367')
call_13228 = func_6365_call()
call_13229 = func_6365_call()
func_7704_call = mod.get_global_var('func_7704')
func_7708_call = mutated_mod.get_global_var('func_7708')
const_13237 = relay.const([-3,1,-8,5,5,2,-3,-10,9,-1,9,-3,9,-4,-1,-9,9,2,-9,5,-4,4,8,-2,-9,5,8,10,5,-2,-10,1,-1,9,1,-3,-10,4,10,-4,-8,-7,-9,4,5,-10,-9,6,-5,1,8,-3,-3,-6,-1,-4,-1,5,-9,4,7,1,-5,7,2,6,-3,10,-5,9,-9,7,3,10,3,6,-7,7,3,-2,3,7,-6,-10,-3,7,1,2,5,5,-7,7,9,-8,9,9,7,-10,3,1,10,-8,1,-2,-3,2,10,-7,-5,-3,-4,-10,8,-3,-9,-7,-2,9,-2,-8,10,6,-1,-10,8,5,-4,3,3,3,10,-3,2,8,3,-2,7,-4,10,9,5,-2,-6,-3,10,-5,5,-7,-9,4,2,-6,3,-9,4,-3,-1,10,-9,-10,-8,-1,4,3,-2,7,2,-5,5,-9,4,-10,6,-4,-4,4,-9,6,-5,-7,5,-3,7,-3,3,-3,-4,10,4,7,-8,9,-7,1,5,3,3,-8,-3,5,3,-1,-1,-8,-6,-3,7,-4,-1,8,-4,-8,6,-7,7,7,10,-10,2,5,5,2,4,-6,-10,10,7,1,4,-6,-10,2,2,10,-9,2,5,-4,10,3,-6,6,-1,-1,-6,5,-10,7,-6,-8,4,-7,-5,-9,2,-7,-6,-4,-3,-9,1,-7,10,7,-1,-1,4,-5,8,4,-5,-10,7,8,-10,8,-3,-6,-9,9,7,-4,-5,-10,2,-6,-4,-7,-2,-10,2,-6,1,7,7,9,-3,5,-3,-4,-6,1,7,-2,3,-3,-9,9,3,9,2,-3,2,-5,-10,9,9,7,-8,-7,2,5,9,1,-3,-3,10,-2,-2,9,-7,-8,-8,6,-8,6,-3,1,-8,5,5,-6,1,-9,-6,5,-7,-2,1,-3,-1,9,2,5,4,-3,5,6,-7,9,3,7,-10,-7,8,-10,-8,10,-10,-2,-2,-5,-4,5,4,-7,9,-1,4,9,-7,-9,-9,7,-6,6,-5,7,10,3,5,4,-3,-4,-2,-8,-4,-6,-8,2,5,3,9,-9,9,6,1,9,-3,-10,-6,6,5,-2,-6,-8,4,-8,9,-3,-1,-4,9,6,-6,6,5,1,3,-7,-8,7,6,7,7,6,1,10,-7,1,-5,7,-9,1,2,1,3,-3,7,4,2,-2,2,-10,-10,-4,7,4,10,10,-3,1,10,5,-4,1,-1,-6,5,-3,6,-10,7,-9,-1,-8,-9,-2,-4,6,6,-3,-8,-1,6,10,1,5,5,-4,10,-3,-2,-9,2,4,1,-6,-8,-4,10,8,-3,1,6,4,-9,6,2,8,1,3,-1,2,5,-8,1,8,9,-4,7,3,-5,-7,-4,-8,-9,6,-9,1,-6,2,-5,3,-2,-8,-3,4,10,4,8,-7,-4,-7,1,8,7,5,2,5,-3,4,-4,3,-10,5,10,5,5,6,1,3,5,9,6,-3,7,-4,-4,4,-5,-5,3,8,3,-5,-7,2,6,9,-5,10,8,2,2,-9,7,3,-4,-9,2,-3,2,-1,9,10,-10,8,4,-1,8,-5,-4,4,-7,6,6,-10,-5,7,-1,-9,-7,1,7,-8,-2,9,-9,-3,-5,-8,6,-9,1,6,3,2,-2,-9], dtype = "int64")#candidate|13237|(630,)|const|int64
const_13238 = relay.const([[True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False]], dtype = "bool")#candidate|13238|(1, 1120)|const|bool
const_13239 = relay.const([9.065649,7.919398,-3.687389,2.681880,-2.018212,8.918473,8.632682,-4.819432,-4.592469,-4.652312,-3.503839,1.131314,3.482998,-4.405729,5.172975,4.360452,-4.758422,-5.948400,-1.897564,9.667176,-5.505240,7.748588,-7.197330,-1.136169,0.700106,-0.100571,-6.259292,8.319476,-4.814882,-3.582639,-5.265374,-0.748945,-5.442280,6.350245,-7.607900,4.826366,-5.287495,2.776380,7.939160,1.822547,-9.199912,-6.547190,-2.890580,-3.717203,7.536525,-4.852597,6.334412,-7.075789,9.817530,-2.180889,4.671795,-7.609054,-4.529463,-2.710467,-7.868419,-1.675772,3.784671,9.829918,-5.636794,-0.552752,-8.791052,-8.048786,0.672315,0.636296,-4.115926,-5.900694,-0.454213,2.573954,-9.262175,-8.595307,-7.481933,-6.715595,9.393120,6.484547,5.698009,9.114484,-4.076802,2.261808,-9.195661,-8.303869,-9.062802,-9.849985,-5.713907,-5.186768,4.174868,6.585314,7.905860,6.343796,3.069554,4.075673,-4.255729,-3.341397,-7.200346,-1.310867,-7.594563,2.785588,-4.746921,6.515290,-9.279435,1.538428,-2.009399,0.538964,-1.883091,-9.265627,9.740331,6.803386,-9.848016,-2.414634,9.142889,-3.091725,4.671230,1.818146,8.112344,-0.405323,-6.045552,-6.841459,-9.487529,-8.834919,-6.719771,-0.359442,-1.094412,-6.423476,6.314458,4.649519,3.195540,7.034256,-1.112804,-8.155210,4.682477,7.404467,9.450292,7.015602,0.519148,-7.889344,-3.224967,5.752289,-8.765654,-6.084495,-6.101167,8.944340,1.733655,-7.979844,3.637839,9.503787,-2.913765,-7.461641,-0.334236,4.430805,5.409248,-9.279873,3.664069,4.391665,2.042767,0.135955,0.329940,6.849986,8.639673,-6.749653,3.596911,-6.197707,-3.563017,8.261162,-1.224203,-9.456238,-3.620097,8.783008,-4.681924,-3.731002,-9.481647,4.294861,-8.453900,-0.377541,1.986449,-6.716991,5.216323,-7.281329,7.571978,-9.471765,-9.482086,6.228989], dtype = "float32")#candidate|13239|(180,)|const|float32
call_13236 = relay.TupleGetItem(func_7704_call(relay.reshape(const_13237.astype('int64'), [1, 630]), relay.reshape(const_13238.astype('bool'), [1120,]), relay.reshape(const_13239.astype('float32'), [180,]), ), 0)
call_13240 = relay.TupleGetItem(func_7708_call(relay.reshape(const_13237.astype('int64'), [1, 630]), relay.reshape(const_13238.astype('bool'), [1120,]), relay.reshape(const_13239.astype('float32'), [180,]), ), 0)
func_7618_call = mod.get_global_var('func_7618')
func_7620_call = mutated_mod.get_global_var('func_7620')
call_13243 = func_7618_call()
call_13244 = func_7618_call()
func_6009_call = mod.get_global_var('func_6009')
func_6011_call = mutated_mod.get_global_var('func_6011')
call_13287 = relay.TupleGetItem(func_6009_call(), 0)
call_13288 = relay.TupleGetItem(func_6011_call(), 0)
func_12749_call = mod.get_global_var('func_12749')
func_12751_call = mutated_mod.get_global_var('func_12751')
const_13303 = relay.const([[True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False],[True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True,False,True,True],[False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False],[False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True],[False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True],[False,False,False,True,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False],[True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True],[True,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True],[True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False],[True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True],[True,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False],[False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True]], dtype = "bool")#candidate|13303|(12, 60)|const|bool
call_13302 = relay.TupleGetItem(func_12749_call(relay.reshape(const_13303.astype('bool'), [720,])), 7)
call_13304 = relay.TupleGetItem(func_12751_call(relay.reshape(const_13303.astype('bool'), [720,])), 7)
output = relay.Tuple([call_13228,call_13236,const_13237,const_13238,const_13239,call_13243,call_13287,call_13302,const_13303,])
output2 = relay.Tuple([call_13229,call_13240,const_13237,const_13238,const_13239,call_13244,call_13288,call_13304,const_13303,])
func_13308 = relay.Function([], output)
mod['func_13308'] = func_13308
mod = relay.transform.InferType()(mod)
mutated_mod['func_13308'] = func_13308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13308_call = mutated_mod.get_global_var('func_13308')
call_13309 = func_13308_call()
output = call_13309
func_13310 = relay.Function([], output)
mutated_mod['func_13310'] = func_13310
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13314 = relay.var("var_13314", dtype = "float32", shape = (4, 1, 12))#candidate|13314|(4, 1, 12)|var|float32
uop_13315 = relay.erf(var_13314.astype('float32')) # shape=(4, 1, 12)
output = relay.Tuple([uop_13315,])
output2 = relay.Tuple([uop_13315,])
func_13318 = relay.Function([var_13314,], output)
mod['func_13318'] = func_13318
mod = relay.transform.InferType()(mod)
var_13319 = relay.var("var_13319", dtype = "float32", shape = (4, 1, 12))#candidate|13319|(4, 1, 12)|var|float32
output = func_13318(var_13319)
func_13320 = relay.Function([var_13319], output)
mutated_mod['func_13320'] = func_13320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12531_call = mod.get_global_var('func_12531')
func_12532_call = mutated_mod.get_global_var('func_12532')
call_13332 = func_12531_call()
call_13333 = func_12531_call()
func_7497_call = mod.get_global_var('func_7497')
func_7499_call = mutated_mod.get_global_var('func_7499')
call_13353 = relay.TupleGetItem(func_7497_call(), 1)
call_13354 = relay.TupleGetItem(func_7499_call(), 1)
output = relay.Tuple([call_13332,call_13353,])
output2 = relay.Tuple([call_13333,call_13354,])
func_13355 = relay.Function([], output)
mod['func_13355'] = func_13355
mod = relay.transform.InferType()(mod)
mutated_mod['func_13355'] = func_13355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13355_call = mutated_mod.get_global_var('func_13355')
call_13356 = func_13355_call()
output = call_13356
func_13357 = relay.Function([], output)
mutated_mod['func_13357'] = func_13357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12557_call = mod.get_global_var('func_12557')
func_12559_call = mutated_mod.get_global_var('func_12559')
call_13362 = func_12557_call()
call_13363 = func_12557_call()
func_6408_call = mod.get_global_var('func_6408')
func_6411_call = mutated_mod.get_global_var('func_6411')
const_13365 = relay.const([1.941299,5.708306,8.195236,6.469348,-1.293253,-8.739934,-0.424983,2.114609,-6.761588,8.234164,-2.565179,2.395505,-3.175519,-9.845830,-2.036832,-3.809542,-4.906010,-6.983029,5.288068,7.553862,-1.267857,7.200231,-4.936450,7.276943,-9.648977,6.037382,3.092325,9.803302,-2.554916,6.049578,-6.353422,9.258014,-6.197670,4.727814,2.109383,6.225749,-1.912549,-5.151487,6.229774,2.693321,5.466521,-3.654448,7.829948,-4.374119,-7.789561,-6.297143,1.952047,4.881187,6.863973,1.881663,-8.713677,-9.728718,-8.503596,9.925129,-0.101359,3.157411,4.042851,-9.568794,6.763925,3.925337,3.663972,-5.659509,8.968709,-7.738863,-6.522991,2.744021,-7.859380,4.551330,-4.836728,9.028596,2.856375,-1.898932,-1.346599,2.904099,-3.378884,7.682257,-1.597385,-7.617515,-6.589949,-6.764005,2.946438,8.649611,5.356555,-7.873187,1.098630,-9.228502,-9.210477,-6.323154,-7.004376,-0.002682,-3.539441,-7.099115,5.731496,-0.033886,6.189098,8.983173,-5.685191,-2.074167,0.907736,6.159708,-9.378328,-4.507038,2.016059,-1.158301,-9.574181,-5.485449,-0.719558,-2.983147,1.620548,8.239207,1.767410,1.482880,8.914448,-7.277062,-7.832985,-1.229331,8.626818,2.622326,6.355685,-0.936114,-3.098086,-5.688898,3.710444,5.603222,1.916083,3.579790,1.228364,-4.502246,3.650024,6.260076,-8.540592,-2.762473,-0.547455,-5.508669,7.557002,-3.125112,9.519687,2.619692,7.552024,-7.717480,6.953060,2.962486,-9.115631,-1.698525,-2.722645,-2.224307,8.117931,4.626952,-1.083690,1.591601,-6.168862,-3.816550,-7.577541,8.873704,-9.360352,-7.322853,6.228742,-3.228623,5.250860,5.174444,-5.172287,-5.336784,3.705091,-3.682884,-5.749684,7.181634,2.084807,-8.499423,3.455862,6.424901,7.780584,-5.318269,0.507991,7.088205,7.096922,1.897693,-0.605518,1.141577,1.535673,9.073340], dtype = "float32")#candidate|13365|(180,)|const|float32
call_13364 = relay.TupleGetItem(func_6408_call(relay.reshape(const_13365.astype('float32'), [6, 30])), 2)
call_13366 = relay.TupleGetItem(func_6411_call(relay.reshape(const_13365.astype('float32'), [6, 30])), 2)
func_9449_call = mod.get_global_var('func_9449')
func_9450_call = mutated_mod.get_global_var('func_9450')
call_13371 = relay.TupleGetItem(func_9449_call(), 0)
call_13372 = relay.TupleGetItem(func_9450_call(), 0)
output = relay.Tuple([call_13362,call_13364,const_13365,call_13371,])
output2 = relay.Tuple([call_13363,call_13366,const_13365,call_13372,])
func_13380 = relay.Function([], output)
mod['func_13380'] = func_13380
mod = relay.transform.InferType()(mod)
mutated_mod['func_13380'] = func_13380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13380_call = mutated_mod.get_global_var('func_13380')
call_13381 = func_13380_call()
output = call_13381
func_13382 = relay.Function([], output)
mutated_mod['func_13382'] = func_13382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8919_call = mod.get_global_var('func_8919')
func_8921_call = mutated_mod.get_global_var('func_8921')
call_13394 = relay.TupleGetItem(func_8919_call(), 0)
call_13395 = relay.TupleGetItem(func_8921_call(), 0)
output = relay.Tuple([call_13394,])
output2 = relay.Tuple([call_13395,])
func_13405 = relay.Function([], output)
mod['func_13405'] = func_13405
mod = relay.transform.InferType()(mod)
mutated_mod['func_13405'] = func_13405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13405_call = mutated_mod.get_global_var('func_13405')
call_13406 = func_13405_call()
output = call_13406
func_13407 = relay.Function([], output)
mutated_mod['func_13407'] = func_13407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13380_call = mod.get_global_var('func_13380')
func_13382_call = mutated_mod.get_global_var('func_13382')
call_13413 = relay.TupleGetItem(func_13380_call(), 0)
call_13414 = relay.TupleGetItem(func_13382_call(), 0)
output = call_13413
output2 = call_13414
func_13435 = relay.Function([], output)
mod['func_13435'] = func_13435
mod = relay.transform.InferType()(mod)
mutated_mod['func_13435'] = func_13435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13435_call = mutated_mod.get_global_var('func_13435')
call_13436 = func_13435_call()
output = call_13436
func_13437 = relay.Function([], output)
mutated_mod['func_13437'] = func_13437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11260_call = mod.get_global_var('func_11260')
func_11262_call = mutated_mod.get_global_var('func_11262')
call_13450 = relay.TupleGetItem(func_11260_call(), 0)
call_13451 = relay.TupleGetItem(func_11262_call(), 0)
output = call_13450
output2 = call_13451
func_13464 = relay.Function([], output)
mod['func_13464'] = func_13464
mod = relay.transform.InferType()(mod)
mutated_mod['func_13464'] = func_13464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13464_call = mutated_mod.get_global_var('func_13464')
call_13465 = func_13464_call()
output = call_13465
func_13466 = relay.Function([], output)
mutated_mod['func_13466'] = func_13466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6769_call = mod.get_global_var('func_6769')
func_6771_call = mutated_mod.get_global_var('func_6771')
call_13499 = func_6769_call()
call_13500 = func_6769_call()
output = relay.Tuple([call_13499,])
output2 = relay.Tuple([call_13500,])
func_13529 = relay.Function([], output)
mod['func_13529'] = func_13529
mod = relay.transform.InferType()(mod)
output = func_13529()
func_13530 = relay.Function([], output)
mutated_mod['func_13530'] = func_13530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12097_call = mod.get_global_var('func_12097')
func_12099_call = mutated_mod.get_global_var('func_12099')
call_13560 = relay.TupleGetItem(func_12097_call(), 0)
call_13561 = relay.TupleGetItem(func_12099_call(), 0)
output = call_13560
output2 = call_13561
func_13568 = relay.Function([], output)
mod['func_13568'] = func_13568
mod = relay.transform.InferType()(mod)
mutated_mod['func_13568'] = func_13568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13568_call = mutated_mod.get_global_var('func_13568')
call_13569 = func_13568_call()
output = call_13569
func_13570 = relay.Function([], output)
mutated_mod['func_13570'] = func_13570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7935_call = mod.get_global_var('func_7935')
func_7937_call = mutated_mod.get_global_var('func_7937')
call_13580 = relay.TupleGetItem(func_7935_call(), 1)
call_13581 = relay.TupleGetItem(func_7937_call(), 1)
func_2250_call = mod.get_global_var('func_2250')
func_2254_call = mutated_mod.get_global_var('func_2254')
const_13584 = relay.const([9.627228,1.732731,-8.585531,-4.274835,1.511111,5.834525,-4.590854,9.017259,2.805215,-3.676305,-6.893418,4.058892,-7.551788,6.117873,1.720859,0.635384,-1.942910,6.966345,1.340623,-8.735363,6.992562,-7.699007,-5.063290,-4.539205,-0.189644,-5.907400,-9.778022,1.767973,-2.522373,-8.718547,-8.881946,-0.776748,0.650166,0.049931,-4.524737,0.483060,9.246815,7.586525,5.610007,8.412640,1.888154,-4.920941,-4.313133,-1.360414,4.426380,-6.823301,-4.890556,-6.461083,-8.518895,0.799804,0.035080,-0.600932,-4.997896,-2.417932,4.242349,8.003168,-6.538999,-9.858105,7.355042,1.640921,-7.630208,-5.633902,-6.727262,-4.197079,4.783000,1.525484,-2.319112,6.596655,-6.003996,-7.835996,-4.081493,-8.857195,-0.706538,6.599204,4.543937,-3.661842,-2.849714,-8.940445,8.483503,9.479271,-5.634749,-8.858347,-4.578444,1.215241,4.490007,-9.546336,6.813806,-6.641618,-2.785660,-8.143934,-3.275852,7.897740,4.563135,-9.282683,-5.700946,5.702495,-8.165854,4.174383,-6.897207,2.351080,-5.288550,3.483684,-1.969142,6.229660,3.774168,-7.763037,-5.963051,-6.779337,-4.525317,2.409164,-1.450026,8.647250,-2.054268,2.097432,-6.857705,-9.172472,-3.192952,-6.203022,-1.461790,6.398951,9.854444,4.146175,1.019478,-4.545032,-6.035744,-9.828090,-9.725318,-9.999127,-5.310938,7.772373,-9.286261,-7.859308,9.919939,-9.082713,-3.555111,6.470976,7.356277,-9.268407,-3.453236,-5.760584,-8.398754,9.896844,7.238366,8.948473,2.318057,-0.932201,-5.192872,9.011158,9.389911,1.727639,4.886222,-4.704792,-5.779109,-8.265559,6.283985,1.662911,1.414178,-2.639940,-3.112178,5.961448,4.194941,-1.560459,-5.086163,8.683732,9.230900,0.401794,-4.631234,5.461282,-7.859935,7.218489,7.217983,6.549140,-2.950251,8.209964,3.307741,-0.697275,-6.491703,4.382367,-7.975830,-5.486537,3.801208,9.499707,4.354761,-7.383231,-1.901803,3.815253,5.888387,-2.774289,9.056564,-9.818563,-9.972613,2.176050,8.285716,9.206915,9.440160,0.506958,-9.607484,-6.088202,-0.700642,9.877383,6.600974,-5.314849,-2.873915,-9.156262,-1.082577,-0.772877,5.599241,1.644264,-0.037427,4.981123,-5.871045,6.414888,1.345495,5.501878,-7.405451,-8.149025,3.889611,-9.031503,2.517035,4.455978,-7.642537,4.430396,2.837677,-3.716686,4.650315,-0.071013,9.708573,-1.238849,2.404241,-5.952551,4.351043,9.692349,0.487789,-5.299161,-9.262297,-7.665948,1.395406,4.752674,-3.017011,3.904684,2.725112,8.216527,3.162300,4.959988,6.757148,-0.266954,-9.466221,-7.932832,-1.872989,-2.597246,-4.742717,0.617638,-0.640866,4.361683,-4.878520,1.709592,-4.575319,-5.642263,-2.973003,-2.733592,2.680255,-6.596528,0.776839,7.731158,7.381331,-5.450080,-3.062970,-2.929810,-8.903270,6.701034,-1.916631,-3.009178,-7.137522,-4.034276,-9.625488,-2.116794,8.575597,0.270108,1.991655,-1.194300,9.939447,0.716674,-3.850087,-0.239395,0.343457,-8.665712,-3.646764,-3.498696,5.066110,-0.290440,3.123527,-5.019031,5.072310,4.621029,-3.309165,-4.971207,5.483177,-7.010399,5.842095,-1.187239,-8.029098,-5.435808,-3.718353,0.178854,6.451381,5.682830,6.731015,4.735482,-7.234541,9.313550,2.099963,-9.837140,6.542135,-3.618753,7.161662,4.184288,2.821930,0.224896,-9.395736,-7.303160,-5.160236,9.171501,2.507413,-3.213961,1.812176,-5.691883,5.009851,0.700624,1.886019,3.595733,4.679662,7.989332,-4.447411,-2.068741,4.847893,-6.335617,-7.958260,8.753800,3.265158,9.431928,-8.617823,4.560927,-6.256393,-3.235055,-2.999767,1.288714,1.485991,9.101624,4.912166,-5.567867,-4.244695,-8.512539,-7.484465,-7.183482,3.475393,9.969093,1.139561,-5.076434,8.536125,-5.711262,-0.766808,9.880248,-8.410325,-5.662069,-8.156056,-1.039892,8.182955,-7.891840,1.597675,6.151638,-3.106807,-3.280015,9.404854,-3.205631,9.900217,1.472669,-1.479113,0.009085,5.326797,-2.272359,8.149587,-6.490429,0.323318,-2.549348,9.180507,5.401441,-9.563928,0.317495,-0.272871,8.731679,-4.986087,-2.221986,3.897917,2.101892,7.832253,7.043324,2.045551,8.115501,-8.192360,6.436519,-2.937339,7.986370,-2.783049,-9.986139,-8.463020,-6.178771,-5.816849,7.206720,5.918062,-7.174083,-9.494938,5.742275,8.344785,-2.780538,-7.791066,1.079634,1.228125,-9.999475,-3.815265,-1.965444,-1.961674,6.644634,5.886928,-8.764672,-9.170102,7.787935,-1.977317,-2.951859,-3.579413,9.796432,-0.572103,2.545239,-8.328446,3.257249,-5.913252,4.012159,-3.204592,-9.104216,-6.624783,-7.955828,6.072854,3.131134,-1.771408,-1.211886,2.355486,-1.115543,-0.858491,9.988710,4.159800,2.659089,-0.429012,-9.394101,-1.850024,7.429864,3.229210,9.518353,4.005137,1.030631,-6.358967,-7.147605,6.022966,3.111608,-3.342387,-5.505204,6.164573,-8.088907,5.627018,-8.516295,7.535655,-8.667865,-0.783573,8.727639,-2.016573,3.876831,-3.783625,-8.578109,-7.037788,-9.772723,-7.525275,-9.607537,-5.871639,-8.204181,7.112102,7.622903,-9.886384,-4.383180,4.861518,-6.359229,-2.350268,-7.207032,-8.148621,-7.554222,-3.796936,9.220321,-5.526896,-7.549158,-3.941965,-7.718128,-1.891776,-5.535131,9.204554,3.600687,3.045724,-1.044065,7.373929,-7.548724,-8.490655,9.307160,0.171543,1.615578,-4.777615,7.786075,-0.068957,7.129559,0.122836,5.437440,-4.627205,-8.902375,3.393006,4.941959,4.903845,-5.730149,-8.135468,9.223262,-8.528547,0.692989,-2.807778,-3.327365,-7.383239,6.656645,1.211162,-5.764600,6.380699,6.871096,-3.721983,-3.755849,8.185284,2.712738,-1.064337,3.674058,9.861523,7.424993,7.007643,3.721680,9.259217,-8.821832,0.858185,-6.316508,3.807001,7.866325,-0.272817,3.778794,-7.110029,-4.132448,0.680975,-0.160894,-4.219146,5.155034,9.476735,-1.899633,9.822503,5.035394,8.194794,-1.902429,-4.032598,-6.959380,9.216693,-6.462946,-9.912288,-0.643941,-3.968626,9.187742,-7.572598,5.082375,7.645803,3.077650,-7.036027,8.291721,-6.125493,-4.418487,-2.541581,-0.583229,-5.086628,8.954223,3.531455,2.707818,-2.076300,-2.594735,2.524157,-4.076685,2.261512,9.062760,4.446568,-4.803109,-7.952888,-4.514411,8.803651,-5.978034,4.212812,4.441665,0.401640,-8.525591,6.148973,5.279254,-0.271247,1.557952,2.649181,7.250610,6.483600,-4.633442,-3.774952,-1.844359,9.330861,-0.894295,1.896777,6.041228,-4.518710,-2.218900,9.667252,-9.669330,-8.039561,2.916007,-9.997170,-5.033876], dtype = "float32")#candidate|13584|(624,)|const|float32
call_13583 = relay.TupleGetItem(func_2250_call(relay.reshape(call_13580.astype('float64'), [11, 3, 16]), relay.reshape(call_13580.astype('float64'), [11, 3, 16]), relay.reshape(const_13584.astype('float32'), [624,]), ), 1)
call_13585 = relay.TupleGetItem(func_2254_call(relay.reshape(call_13580.astype('float64'), [11, 3, 16]), relay.reshape(call_13580.astype('float64'), [11, 3, 16]), relay.reshape(const_13584.astype('float32'), [624,]), ), 1)
func_11650_call = mod.get_global_var('func_11650')
func_11652_call = mutated_mod.get_global_var('func_11652')
var_13588 = relay.var("var_13588", dtype = "float32", shape = (180,))#candidate|13588|(180,)|var|float32
call_13587 = relay.TupleGetItem(func_11650_call(relay.reshape(var_13588.astype('float32'), [180,])), 1)
call_13589 = relay.TupleGetItem(func_11652_call(relay.reshape(var_13588.astype('float32'), [180,])), 1)
func_7646_call = mod.get_global_var('func_7646')
func_7647_call = mutated_mod.get_global_var('func_7647')
call_13599 = relay.TupleGetItem(func_7646_call(), 0)
call_13600 = relay.TupleGetItem(func_7647_call(), 0)
func_11409_call = mod.get_global_var('func_11409')
func_11410_call = mutated_mod.get_global_var('func_11410')
call_13630 = func_11409_call()
call_13631 = func_11409_call()
func_11078_call = mod.get_global_var('func_11078')
func_11079_call = mutated_mod.get_global_var('func_11079')
call_13634 = relay.TupleGetItem(func_11078_call(), 0)
call_13635 = relay.TupleGetItem(func_11079_call(), 0)
func_7646_call = mod.get_global_var('func_7646')
func_7647_call = mutated_mod.get_global_var('func_7647')
call_13638 = relay.TupleGetItem(func_7646_call(), 1)
call_13639 = relay.TupleGetItem(func_7647_call(), 1)
output = relay.Tuple([call_13580,call_13583,const_13584,call_13587,var_13588,call_13599,call_13630,call_13634,call_13638,])
output2 = relay.Tuple([call_13581,call_13585,const_13584,call_13589,var_13588,call_13600,call_13631,call_13635,call_13639,])
func_13650 = relay.Function([var_13588,], output)
mod['func_13650'] = func_13650
mod = relay.transform.InferType()(mod)
var_13651 = relay.var("var_13651", dtype = "float32", shape = (180,))#candidate|13651|(180,)|var|float32
output = func_13650(var_13651)
func_13652 = relay.Function([var_13651], output)
mutated_mod['func_13652'] = func_13652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6790_call = mod.get_global_var('func_6790')
func_6792_call = mutated_mod.get_global_var('func_6792')
call_13686 = relay.TupleGetItem(func_6790_call(), 0)
call_13687 = relay.TupleGetItem(func_6792_call(), 0)
output = call_13686
output2 = call_13687
func_13690 = relay.Function([], output)
mod['func_13690'] = func_13690
mod = relay.transform.InferType()(mod)
mutated_mod['func_13690'] = func_13690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13690_call = mutated_mod.get_global_var('func_13690')
call_13691 = func_13690_call()
output = call_13691
func_13692 = relay.Function([], output)
mutated_mod['func_13692'] = func_13692
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13753 = relay.var("var_13753", dtype = "int16", shape = (10, 16, 8))#candidate|13753|(10, 16, 8)|var|int16
const_13754 = relay.const([[[-4,-3,2,-10,1,5,10,-3],[5,4,-7,-4,2,3,4,10],[-7,-1,-8,3,8,-9,4,-3],[1,6,4,1,4,5,-4,-10],[-9,3,1,9,5,-8,-1,7],[-10,9,5,-9,-4,8,3,-2],[-8,2,-10,-9,-8,-4,-9,2],[-6,-3,-9,-1,-1,2,9,-6],[8,8,-6,10,3,-4,7,-2],[-7,7,1,10,8,-4,7,-6],[6,10,1,8,6,-6,8,-9],[7,2,3,-8,5,2,1,-4],[3,1,-5,-8,2,5,4,-6],[9,8,9,7,-7,-3,-6,-7],[2,3,-8,-8,6,4,-9,-2],[-8,4,-4,1,-9,-10,-3,4]],[[-7,-3,-9,-7,6,7,-10,8],[7,5,-3,5,-3,7,-1,1],[1,3,7,-4,-1,-10,8,-1],[10,-8,-4,-4,-7,-3,5,8],[-10,-5,3,9,8,5,7,-5],[-3,9,6,-4,-6,5,3,-7],[-4,-1,2,1,1,-8,-3,5],[-5,-5,10,6,-6,-7,-4,-3],[7,-7,4,-10,5,3,-2,8],[-7,-8,2,-2,7,-9,-6,-3],[-6,3,-10,5,3,-7,-10,-2],[-8,3,8,-8,7,-8,-8,7],[1,4,-4,-1,10,-2,3,-9],[-6,-8,-8,-9,-2,9,10,-5],[-9,-4,-1,2,1,2,-9,4],[3,-10,-6,9,8,9,-5,8]],[[-5,-7,-7,8,2,-3,-2,8],[9,-8,1,-5,5,-8,10,6],[-10,2,1,-7,-1,-6,7,8],[-6,-1,4,-5,-1,3,8,-7],[-10,6,-2,-6,5,-5,10,8],[-10,10,-6,6,7,-9,7,-3],[-6,10,-4,-10,-10,3,8,5],[-2,-5,9,6,-9,1,10,4],[-3,-3,-3,-7,-9,5,2,7],[-3,2,2,-8,-10,8,10,-5],[8,-1,-4,4,-7,-1,8,-2],[-10,3,-10,-4,7,-10,8,4],[-7,7,-3,5,1,-10,-3,10],[-7,-7,3,9,7,-10,7,1],[9,5,2,-4,5,-3,-6,-2],[-5,10,-2,9,10,-2,-3,3]],[[4,6,10,-8,3,3,-4,2],[6,9,-5,-5,10,-4,-2,-7],[-6,2,-10,-1,4,2,-1,-9],[-10,-2,7,-10,7,-1,10,7],[8,2,-2,3,-8,-5,-1,5],[5,6,5,10,-9,-10,7,-3],[-7,-5,9,-6,-4,6,-7,1],[-8,-3,-3,4,-4,-1,4,-9],[8,-1,-3,3,-1,-5,8,2],[2,-9,-10,9,9,-6,3,-5],[9,-9,6,10,-1,-8,2,4],[-5,1,8,-7,9,4,-9,2],[-7,-10,2,-10,4,1,8,-10],[-10,6,10,-7,-9,10,9,3],[2,1,-3,7,1,-5,-3,9],[7,-3,1,5,-10,7,8,5]],[[5,-4,-9,8,-10,6,-10,-9],[10,-4,-2,2,-6,9,-9,4],[2,-2,10,8,5,-3,1,-9],[-4,4,4,5,-3,5,-1,-7],[8,6,9,10,-10,-8,7,-1],[-2,4,-1,5,-7,7,1,3],[-3,-1,-2,8,-4,-2,4,1],[-10,-2,-5,-6,-9,-10,-9,2],[-1,6,-4,5,1,-8,-1,-10],[5,2,9,4,-1,10,9,-1],[5,-4,-4,-6,8,-9,-4,-8],[1,8,-7,9,7,9,-3,8],[2,6,3,-8,-7,-10,7,9],[9,1,-2,-8,-2,-6,-9,-1],[-6,-4,1,2,2,9,9,9],[-7,-3,-3,-7,8,-9,8,10]],[[9,5,-10,7,6,-1,-6,-2],[-3,2,-8,10,-2,6,1,4],[-10,9,5,-1,-4,9,-5,2],[7,-5,-5,-2,-5,7,-4,3],[1,5,-10,10,-1,3,-7,5],[3,1,-6,-4,-1,5,1,9],[-2,9,-1,5,5,9,6,-8],[-5,-6,-1,-9,1,-8,-4,6],[3,7,4,7,1,-5,-1,8],[1,-6,4,9,-9,-8,5,-8],[-1,2,6,-7,7,-6,5,4],[-7,2,-8,-7,-7,-10,8,9],[-3,-7,2,8,7,8,9,10],[4,7,3,9,-6,-2,-6,-8],[-4,8,10,-3,-1,1,-3,-3],[-4,-9,4,-9,-6,9,-4,3]],[[-1,-3,-8,-7,7,6,-8,-1],[1,1,7,-8,-3,-6,-3,6],[-9,-4,-5,-5,-1,-6,-10,-3],[-6,-8,6,-7,2,-7,-4,6],[2,-10,3,1,6,4,4,-9],[-4,5,-1,-1,8,6,1,-5],[4,-9,-1,-2,8,3,3,-4],[8,-7,2,4,5,1,-3,-10],[2,-7,-10,9,5,3,5,5],[7,-4,1,10,-7,-6,5,-1],[-5,-9,-5,6,2,10,-7,3],[-8,-6,5,8,6,4,10,-8],[2,-2,8,9,-7,9,3,-9],[-9,3,-10,-5,7,-8,5,-3],[-5,-5,3,3,2,-6,-4,-9],[10,4,-3,6,10,-8,-2,-3]],[[-4,-10,-4,-6,4,3,-7,-10],[4,-8,-5,-8,10,10,-7,-9],[-1,7,-1,-2,-7,3,-7,2],[9,10,-6,-8,4,-10,-9,3],[5,5,-5,1,2,-7,-8,-10],[-8,-10,-9,-5,-6,-6,-4,-7],[1,7,7,-7,3,-9,2,8],[2,-8,-6,-5,-8,9,2,-2],[-8,-8,-6,-5,10,10,3,-3],[5,5,-4,6,-3,-5,3,-7],[-6,-5,1,-1,-5,-2,8,3],[-7,-7,-1,3,9,3,5,10],[-7,4,-6,9,-6,2,-6,-7],[5,2,-6,4,-2,5,6,-7],[-4,-1,5,-4,10,-5,10,9],[-4,3,-5,5,-1,5,10,10]],[[-4,-4,10,-2,-3,7,6,9],[7,2,-9,1,9,-7,9,-1],[-8,-4,5,9,2,1,1,10],[4,-2,-8,2,1,6,-7,-3],[-4,-7,2,6,3,-3,-9,-4],[6,-5,1,2,5,9,5,-10],[8,7,-3,-5,-2,3,-1,4],[3,2,5,5,1,5,-6,2],[-4,6,-2,6,-7,-5,5,8],[1,1,5,7,10,10,10,-1],[-3,-2,8,-10,6,-5,-7,9],[4,-3,6,5,-3,-5,8,-7],[-3,-7,6,7,-3,3,7,5],[1,-2,-9,6,-1,6,5,2],[2,-10,-9,2,-9,-3,6,10],[7,6,-9,7,-1,1,6,-7]],[[-7,7,-2,-9,4,9,-9,9],[3,1,6,-3,-10,-7,10,-7],[1,-2,-4,5,-10,-8,-5,4],[-2,1,-2,7,1,-2,-7,7],[-2,-10,9,-4,2,-9,-1,-9],[7,-1,6,-4,-5,7,3,10],[2,-2,7,-9,10,-10,-10,-1],[8,-7,3,1,-8,-10,2,-8],[1,-7,-8,9,-6,-8,-5,5],[-3,10,-6,4,9,6,-3,8],[-8,10,3,3,-8,6,-2,-9],[-5,-2,9,-4,-9,10,7,-6],[2,1,7,5,-9,-1,3,-7],[-8,-9,7,5,-6,-10,2,-9],[1,-2,-6,-6,-7,5,6,8],[10,-2,5,-5,-4,-5,8,-3]]], dtype = "int16")#candidate|13754|(10, 16, 8)|const|int16
bop_13755 = relay.not_equal(var_13753.astype('bool'), relay.reshape(const_13754.astype('bool'), relay.shape_of(var_13753))) # shape=(10, 16, 8)
uop_13758 = relay.log10(bop_13755.astype('float64')) # shape=(10, 16, 8)
bop_13777 = relay.left_shift(uop_13758.astype('int32'), relay.reshape(const_13754.astype('int32'), relay.shape_of(uop_13758))) # shape=(10, 16, 8)
output = bop_13777
output2 = bop_13777
func_13784 = relay.Function([var_13753,], output)
mod['func_13784'] = func_13784
mod = relay.transform.InferType()(mod)
var_13785 = relay.var("var_13785", dtype = "int16", shape = (10, 16, 8))#candidate|13785|(10, 16, 8)|var|int16
output = func_13784(var_13785)
func_13786 = relay.Function([var_13785], output)
mutated_mod['func_13786'] = func_13786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6813_call = mod.get_global_var('func_6813')
func_6815_call = mutated_mod.get_global_var('func_6815')
call_13890 = relay.TupleGetItem(func_6813_call(), 0)
call_13891 = relay.TupleGetItem(func_6815_call(), 0)
output = relay.Tuple([call_13890,])
output2 = relay.Tuple([call_13891,])
func_13907 = relay.Function([], output)
mod['func_13907'] = func_13907
mod = relay.transform.InferType()(mod)
mutated_mod['func_13907'] = func_13907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13907_call = mutated_mod.get_global_var('func_13907')
call_13908 = func_13907_call()
output = call_13908
func_13909 = relay.Function([], output)
mutated_mod['func_13909'] = func_13909
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13910 = relay.var("var_13910", dtype = "float32", shape = ())#candidate|13910|()|var|float32
var_13911 = relay.var("var_13911", dtype = "float32", shape = (15, 13, 7))#candidate|13911|(15, 13, 7)|var|float32
bop_13912 = relay.subtract(var_13910.astype('float32'), var_13911.astype('float32')) # shape=(15, 13, 7)
func_13529_call = mod.get_global_var('func_13529')
func_13530_call = mutated_mod.get_global_var('func_13530')
call_13933 = relay.TupleGetItem(func_13529_call(), 0)
call_13934 = relay.TupleGetItem(func_13530_call(), 0)
bop_13936 = relay.less(call_13933.astype('bool'), var_13910.astype('bool')) # shape=(15, 8, 15)
bop_13939 = relay.less(call_13934.astype('bool'), var_13910.astype('bool')) # shape=(15, 8, 15)
func_10085_call = mod.get_global_var('func_10085')
func_10087_call = mutated_mod.get_global_var('func_10087')
call_13966 = func_10085_call()
call_13967 = func_10085_call()
func_11078_call = mod.get_global_var('func_11078')
func_11079_call = mutated_mod.get_global_var('func_11079')
call_13978 = relay.TupleGetItem(func_11078_call(), 0)
call_13979 = relay.TupleGetItem(func_11079_call(), 0)
output = relay.Tuple([bop_13912,bop_13936,call_13966,call_13978,])
output2 = relay.Tuple([bop_13912,bop_13939,call_13967,call_13979,])
func_13989 = relay.Function([var_13910,var_13911,], output)
mod['func_13989'] = func_13989
mod = relay.transform.InferType()(mod)
mutated_mod['func_13989'] = func_13989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13989_call = mutated_mod.get_global_var('func_13989')
var_13991 = relay.var("var_13991", dtype = "float32", shape = ())#candidate|13991|()|var|float32
var_13992 = relay.var("var_13992", dtype = "float32", shape = (15, 13, 7))#candidate|13992|(15, 13, 7)|var|float32
call_13990 = func_13989_call(var_13991,var_13992,)
output = call_13990
func_13993 = relay.Function([var_13991,var_13992,], output)
mutated_mod['func_13993'] = func_13993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6885_call = mod.get_global_var('func_6885')
func_6886_call = mutated_mod.get_global_var('func_6886')
call_14083 = relay.TupleGetItem(func_6885_call(), 0)
call_14084 = relay.TupleGetItem(func_6886_call(), 0)
func_8625_call = mod.get_global_var('func_8625')
func_8626_call = mutated_mod.get_global_var('func_8626')
call_14091 = relay.TupleGetItem(func_8625_call(), 0)
call_14092 = relay.TupleGetItem(func_8626_call(), 0)
output = relay.Tuple([call_14083,call_14091,])
output2 = relay.Tuple([call_14084,call_14092,])
func_14130 = relay.Function([], output)
mod['func_14130'] = func_14130
mod = relay.transform.InferType()(mod)
mutated_mod['func_14130'] = func_14130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14130_call = mutated_mod.get_global_var('func_14130')
call_14131 = func_14130_call()
output = call_14131
func_14132 = relay.Function([], output)
mutated_mod['func_14132'] = func_14132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11574_call = mod.get_global_var('func_11574')
func_11575_call = mutated_mod.get_global_var('func_11575')
call_14139 = func_11574_call()
call_14140 = func_11574_call()
func_10085_call = mod.get_global_var('func_10085')
func_10087_call = mutated_mod.get_global_var('func_10087')
call_14146 = func_10085_call()
call_14147 = func_10085_call()
output = relay.Tuple([call_14139,call_14146,])
output2 = relay.Tuple([call_14140,call_14147,])
func_14148 = relay.Function([], output)
mod['func_14148'] = func_14148
mod = relay.transform.InferType()(mod)
output = func_14148()
func_14149 = relay.Function([], output)
mutated_mod['func_14149'] = func_14149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13308_call = mod.get_global_var('func_13308')
func_13310_call = mutated_mod.get_global_var('func_13310')
call_14150 = relay.TupleGetItem(func_13308_call(), 2)
call_14151 = relay.TupleGetItem(func_13310_call(), 2)
func_4654_call = mod.get_global_var('func_4654')
func_4658_call = mutated_mod.get_global_var('func_4658')
call_14178 = relay.TupleGetItem(func_4654_call(relay.reshape(call_14150.astype('int64'), [14, 15, 3]), relay.reshape(call_14150.astype('int64'), [14, 15, 3]), ), 0)
call_14179 = relay.TupleGetItem(func_4658_call(relay.reshape(call_14150.astype('int64'), [14, 15, 3]), relay.reshape(call_14150.astype('int64'), [14, 15, 3]), ), 0)
var_14198 = relay.var("var_14198", dtype = "bool", shape = (14, 15, 3))#candidate|14198|(14, 15, 3)|var|bool
bop_14199 = relay.logical_and(call_14178.astype('bool'), relay.reshape(var_14198.astype('bool'), relay.shape_of(call_14178))) # shape=(14, 15, 3)
bop_14202 = relay.logical_and(call_14179.astype('bool'), relay.reshape(var_14198.astype('bool'), relay.shape_of(call_14179))) # shape=(14, 15, 3)
func_11574_call = mod.get_global_var('func_11574')
func_11575_call = mutated_mod.get_global_var('func_11575')
call_14221 = func_11574_call()
call_14222 = func_11574_call()
func_13318_call = mod.get_global_var('func_13318')
func_13320_call = mutated_mod.get_global_var('func_13320')
const_14228 = relay.const([-1.476226,9.653077,-2.034155,-1.882115,-8.624889,-2.383044,-6.530394,0.010166,-4.369180,-7.858694,-6.766704,0.196515,1.398571,-2.264477,-9.063544,7.480711,-7.278037,5.710636,6.906126,-5.180921,-7.083532,-1.435771,3.497198,0.767540,-1.788928,8.368684,8.794146,-2.198288,8.459052,4.690028,2.752950,-8.851478,-5.237822,-8.133727,-7.868930,4.423429,4.839447,8.847332,1.518876,9.201494,-7.231977,-1.863254,0.171546,5.529024,6.010200,-8.329855,8.851893,-8.726019], dtype = "float32")#candidate|14228|(48,)|const|float32
call_14227 = relay.TupleGetItem(func_13318_call(relay.reshape(const_14228.astype('float32'), [4, 1, 12])), 0)
call_14229 = relay.TupleGetItem(func_13320_call(relay.reshape(const_14228.astype('float32'), [4, 1, 12])), 0)
func_10913_call = mod.get_global_var('func_10913')
func_10914_call = mutated_mod.get_global_var('func_10914')
call_14231 = relay.TupleGetItem(func_10913_call(), 1)
call_14232 = relay.TupleGetItem(func_10914_call(), 1)
output = relay.Tuple([call_14150,bop_14199,call_14221,call_14227,const_14228,call_14231,])
output2 = relay.Tuple([call_14151,bop_14202,call_14222,call_14229,const_14228,call_14232,])
func_14237 = relay.Function([var_14198,], output)
mod['func_14237'] = func_14237
mod = relay.transform.InferType()(mod)
mutated_mod['func_14237'] = func_14237
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14238 = relay.var("var_14238", dtype = "bool", shape = (14, 15, 3))#candidate|14238|(14, 15, 3)|var|bool
func_14237_call = mutated_mod.get_global_var('func_14237')
call_14239 = func_14237_call(var_14238)
output = call_14239
func_14240 = relay.Function([var_14238], output)
mutated_mod['func_14240'] = func_14240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8556_call = mod.get_global_var('func_8556')
func_8557_call = mutated_mod.get_global_var('func_8557')
call_14284 = relay.TupleGetItem(func_8556_call(), 0)
call_14285 = relay.TupleGetItem(func_8557_call(), 0)
func_13650_call = mod.get_global_var('func_13650')
func_13652_call = mutated_mod.get_global_var('func_13652')
var_14300 = relay.var("var_14300", dtype = "float32", shape = (180, 1))#candidate|14300|(180, 1)|var|float32
call_14299 = relay.TupleGetItem(func_13650_call(relay.reshape(var_14300.astype('float32'), [180,])), 2)
call_14301 = relay.TupleGetItem(func_13652_call(relay.reshape(var_14300.astype('float32'), [180,])), 2)
output = relay.Tuple([call_14284,call_14299,var_14300,])
output2 = relay.Tuple([call_14285,call_14301,var_14300,])
func_14321 = relay.Function([var_14300,], output)
mod['func_14321'] = func_14321
mod = relay.transform.InferType()(mod)
var_14322 = relay.var("var_14322", dtype = "float32", shape = (180, 1))#candidate|14322|(180, 1)|var|float32
output = func_14321(var_14322)
func_14323 = relay.Function([var_14322], output)
mutated_mod['func_14323'] = func_14323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8891_call = mod.get_global_var('func_8891')
func_8893_call = mutated_mod.get_global_var('func_8893')
call_14350 = relay.TupleGetItem(func_8891_call(), 0)
call_14351 = relay.TupleGetItem(func_8893_call(), 0)
func_14321_call = mod.get_global_var('func_14321')
func_14323_call = mutated_mod.get_global_var('func_14323')
var_14373 = relay.var("var_14373", dtype = "float32", shape = (6, 30))#candidate|14373|(6, 30)|var|float32
call_14372 = relay.TupleGetItem(func_14321_call(relay.reshape(var_14373.astype('float32'), [180, 1])), 1)
call_14374 = relay.TupleGetItem(func_14323_call(relay.reshape(var_14373.astype('float32'), [180, 1])), 1)
func_7786_call = mod.get_global_var('func_7786')
func_7788_call = mutated_mod.get_global_var('func_7788')
call_14389 = relay.TupleGetItem(func_7786_call(), 1)
call_14390 = relay.TupleGetItem(func_7788_call(), 1)
func_7148_call = mod.get_global_var('func_7148')
func_7150_call = mutated_mod.get_global_var('func_7150')
call_14391 = relay.TupleGetItem(func_7148_call(), 0)
call_14392 = relay.TupleGetItem(func_7150_call(), 0)
output = relay.Tuple([call_14350,call_14372,var_14373,call_14389,call_14391,])
output2 = relay.Tuple([call_14351,call_14374,var_14373,call_14390,call_14392,])
func_14398 = relay.Function([var_14373,], output)
mod['func_14398'] = func_14398
mod = relay.transform.InferType()(mod)
var_14399 = relay.var("var_14399", dtype = "float32", shape = (6, 30))#candidate|14399|(6, 30)|var|float32
output = func_14398(var_14399)
func_14400 = relay.Function([var_14399], output)
mutated_mod['func_14400'] = func_14400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8193_call = mod.get_global_var('func_8193')
func_8194_call = mutated_mod.get_global_var('func_8194')
call_14419 = relay.TupleGetItem(func_8193_call(), 0)
call_14420 = relay.TupleGetItem(func_8194_call(), 0)
output = call_14419
output2 = call_14420
func_14429 = relay.Function([], output)
mod['func_14429'] = func_14429
mod = relay.transform.InferType()(mod)
output = func_14429()
func_14430 = relay.Function([], output)
mutated_mod['func_14430'] = func_14430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13690_call = mod.get_global_var('func_13690')
func_13692_call = mutated_mod.get_global_var('func_13692')
call_14460 = func_13690_call()
call_14461 = func_13690_call()
func_5730_call = mod.get_global_var('func_5730')
func_5732_call = mutated_mod.get_global_var('func_5732')
const_14468 = relay.const([[5.681249,3.869382,5.528208,2.180102,-9.587023,-1.964989,6.082867,5.918563,8.069463,1.784299,3.951602,3.990046,-7.257061,5.371720,-1.399944,0.094179,5.516847,-6.834908,-3.388264,7.490286,9.205531,-6.441903,-6.783712,-8.476314,-1.713688,-0.751334,-1.842030,-8.138707,-3.499920,-0.052504],[-0.332092,6.792278,-6.693686,9.565359,1.600302,-1.081965,-7.855771,7.091630,-4.604073,-2.637036,2.264611,-6.651104,-9.417517,-4.857532,-8.455199,2.467992,9.314881,0.294453,6.593280,-7.584389,2.935070,8.721888,8.094101,-3.947710,-0.055074,-1.886489,-0.044377,-0.526555,7.373869,6.471711],[8.490606,5.572222,4.868274,-5.022960,8.367000,7.299087,7.791737,-9.360161,-7.058290,7.038711,9.307397,-3.123699,-0.699674,-5.038488,-8.186056,-0.340307,-4.380912,-2.581426,-3.756233,-6.256510,0.912357,-4.043682,9.767466,6.679228,0.872892,-4.985895,-7.327058,-8.966837,1.753957,-2.220889],[8.953292,2.435342,-2.478709,7.861314,1.110209,-0.364027,-7.220983,6.639401,6.811079,5.216183,0.392488,1.660235,-9.513110,2.448709,-3.276627,1.082651,-2.503987,-5.384949,-1.617702,6.968155,7.672623,-3.879057,-3.302231,2.530531,-7.209072,-5.438952,6.829358,1.303141,-7.991853,2.655520],[8.532166,-4.104250,-8.889273,-2.923126,-7.542977,-3.944931,-6.128707,7.240101,-2.360112,-7.625442,0.433068,3.365012,4.083317,6.755340,9.074126,-0.592496,2.157330,-6.497071,3.548464,6.107761,-5.010289,-3.032072,-2.644456,2.116372,-2.165245,-3.192985,-1.126713,-2.093335,-7.532339,3.668042],[3.336469,-9.611701,-0.452225,-3.013154,-3.677193,-9.366735,0.589171,0.446334,-0.282782,-6.480563,-5.971433,6.563532,-1.836354,-2.329032,8.693551,-4.157576,-2.660641,4.213307,1.442072,-9.011191,3.232662,-7.917505,0.317346,1.709670,-8.064099,5.727016,-0.803647,-7.958058,-4.864820,1.469417]], dtype = "float32")#candidate|14468|(6, 30)|const|float32
call_14467 = relay.TupleGetItem(func_5730_call(relay.reshape(const_14468.astype('float32'), [6, 30])), 3)
call_14469 = relay.TupleGetItem(func_5732_call(relay.reshape(const_14468.astype('float32'), [6, 30])), 3)
output = relay.Tuple([call_14460,call_14467,const_14468,])
output2 = relay.Tuple([call_14461,call_14469,const_14468,])
func_14482 = relay.Function([], output)
mod['func_14482'] = func_14482
mod = relay.transform.InferType()(mod)
mutated_mod['func_14482'] = func_14482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14482_call = mutated_mod.get_global_var('func_14482')
call_14483 = func_14482_call()
output = call_14483
func_14484 = relay.Function([], output)
mutated_mod['func_14484'] = func_14484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10413_call = mod.get_global_var('func_10413')
func_10414_call = mutated_mod.get_global_var('func_10414')
call_14488 = relay.TupleGetItem(func_10413_call(), 0)
call_14489 = relay.TupleGetItem(func_10414_call(), 0)
output = call_14488
output2 = call_14489
func_14499 = relay.Function([], output)
mod['func_14499'] = func_14499
mod = relay.transform.InferType()(mod)
mutated_mod['func_14499'] = func_14499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14499_call = mutated_mod.get_global_var('func_14499')
call_14500 = func_14499_call()
output = call_14500
func_14501 = relay.Function([], output)
mutated_mod['func_14501'] = func_14501
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14513 = relay.const([[[1.772494,-8.220477,3.203040,3.182366,-9.195271,-1.518892,-2.869235,1.848074,-5.110225,-9.122673,8.634954,1.697814,9.859282,9.732360,6.001439,2.212513],[-7.836559,8.366942,-6.453612,3.180827,1.106228,6.000478,-7.841717,-3.515982,-6.168696,6.581022,8.698041,5.231196,3.762079,-1.740296,4.506143,0.379996],[0.565240,8.301244,-8.240576,-8.304801,1.015616,1.310439,-3.232285,-9.830350,-6.909870,-1.804033,-7.555519,-4.036249,-6.604891,-7.959714,-2.828732,6.773974],[-8.415439,9.887917,8.559497,-9.771403,-0.415733,-2.967708,4.181782,8.315175,3.596137,4.934316,2.340520,9.235777,-7.648362,7.491385,-1.964716,-8.269267],[-7.832898,3.233967,4.129332,-9.408070,3.972107,6.997504,3.310023,-9.819407,-0.098551,-7.584640,0.485555,-2.807819,2.724681,-2.172337,-6.646241,-3.909578],[5.919451,5.445614,1.640909,-7.947549,-3.045986,-2.916595,-6.371855,-0.679659,-1.221910,0.489938,7.457395,-4.816659,6.416343,-7.829124,8.337440,-5.157527],[-6.861763,-5.787802,9.744050,-4.914271,-6.964690,5.990118,8.901242,8.633409,-3.288949,3.133755,-6.469932,-3.460404,-8.198015,-5.921618,5.641533,-4.633833],[-9.339626,-4.932164,6.270328,4.835221,1.550061,4.200138,0.048694,-5.949375,5.802902,1.623868,7.284941,2.222793,-4.178323,-1.813254,4.745020,5.187161],[7.268676,4.211477,-4.394115,-1.421085,-2.531565,-7.397544,-1.939724,5.028477,-3.545363,-0.682219,0.803424,3.816257,9.411363,2.592270,3.738736,-1.677385]]], dtype = "float32")#candidate|14513|(1, 9, 16)|const|float32
uop_14514 = relay.exp(const_14513.astype('float32')) # shape=(1, 9, 16)
output = relay.Tuple([uop_14514,])
output2 = relay.Tuple([uop_14514,])
func_14525 = relay.Function([], output)
mod['func_14525'] = func_14525
mod = relay.transform.InferType()(mod)
output = func_14525()
func_14526 = relay.Function([], output)
mutated_mod['func_14526'] = func_14526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13380_call = mod.get_global_var('func_13380')
func_13382_call = mutated_mod.get_global_var('func_13382')
call_14529 = relay.TupleGetItem(func_13380_call(), 0)
call_14530 = relay.TupleGetItem(func_13382_call(), 0)
func_13784_call = mod.get_global_var('func_13784')
func_13786_call = mutated_mod.get_global_var('func_13786')
const_14536 = relay.const([-7,6,3,-5,3,-10,8,4,-6,-8,6,-3,-10,3,7,6,2,-1,-10,-6,4,-1,-6,2,6,6,-1,6,-7,9,-10,7,-9,-7,-7,-3,2,3,-8,9,-4,7,-5,-9,3,-4,5,5,2,-4,-6,9,-10,6,-7,4,-10,-7,6,-7,5,2,-7,-5,-10,7,5,-3,-8,3,-4,7,7,-10,9,2,1,6,-10,6,-10,-5,10,-8,-9,-4,-7,8,4,-7,-5,8,2,3,-5,-1,3,7,-3,10,5,4,4,4,-2,-10,1,-5,2,-4,-9,9,10,-3,-1,5,-8,8,3,-9,-4,-1,9,-7,-6,-9,5,-6,5,7,6,-4,3,6,5,-2,-6,-5,1,-7,10,-3,-5,-7,2,-10,6,-1,-7,8,2,-4,-4,-3,-8,3,10,2,-9,-8,5,-9,4,-3,-9,-7,-10,9,-10,9,7,-6,2,-2,1,3,-2,8,-4,-8,-9,-4,-8,2,-9,7,-7,-3,-3,9,9,-9,-6,-6,5,1,-1,-4,10,-8,-9,5,8,-4,-4,-4,-6,-1,-9,1,3,9,-1,-4,10,-9,8,2,3,8,8,-10,6,-7,8,-8,-3,4,1,4,1,8,-7,-7,6,-6,9,1,7,10,-9,8,-5,-6,2,6,1,-5,6,-9,-1,-1,10,6,1,5,-4,3,-7,6,7,5,7,8,-3,-8,-1,5,-2,-3,6,-4,-2,10,6,-9,9,2,-3,1,-9,-2,-9,-6,-9,3,-6,6,4,9,3,2,1,9,-6,4,1,-6,3,9,-10,7,-9,-5,-10,-10,4,6,6,1,-8,-5,-9,7,-2,3,-9,9,-3,1,-1,-10,-3,-10,4,8,6,-10,6,-8,6,-2,4,-2,-8,-2,-2,-1,9,-3,-3,-6,8,-4,3,-7,-5,-3,2,6,8,6,10,-6,-9,3,-2,10,5,6,-8,-7,2,2,7,4,5,5,7,6,2,7,6,-4,3,-9,3,-4,9,-10,3,10,-2,-3,8,-5,9,-4,1,-6,-2,-7,-2,-1,-8,-7,-5,-9,4,7,1,4,-6,-3,-8,3,-5,-4,-3,9,-8,-2,-3,-3,1,3,-4,10,-7,8,5,5,4,-8,-8,8,-3,-10,-9,5,3,-2,5,8,6,-9,-7,-10,6,8,4,2,4,6,-7,3,-1,8,8,9,-1,-4,3,-1,-3,4,5,-5,-8,-4,3,6,4,-1,-9,6,-7,10,6,8,10,-5,8,6,2,-2,7,9,3,4,10,-3,10,-6,7,-6,-8,4,2,3,-9,-2,-4,-10,3,-10,-3,10,10,-2,4,8,10,9,3,7,-10,2,2,-2,5,-5,-8,-6,3,-7,-5,-8,-8,-6,-2,5,-3,-5,-9,9,-10,6,1,6,7,10,8,-8,8,9,10,9,3,10,10,7,6,-8,5,-1,-9,6,-3,-6,-10,-9,9,6,4,3,7,-6,5,-10,-9,-3,-3,8,7,7,8,-10,5,-8,-3,-5,-5,3,-6,-10,-5,-5,-6,-6,-6,-10,10,1,7,-6,-4,-1,3,-9,-1,6,-4,6,-4,2,-5,6,4,1,-9,-2,-8,-2,-10,-10,9,-7,-6,4,-3,-4,1,-2,-9,6,9,-1,-10,-10,3,1,5,-7,-1,3,-7,2,6,3,-8,3,7,-6,8,-7,-5,5,8,-3,2,3,-2,9,9,-3,-3,6,-4,-6,10,5,4,7,1,9,5,-5,6,-7,10,-4,10,-10,4,-7,1,-2,-2,-7,9,10,-9,-3,1,-10,1,3,-5,4,-10,4,4,6,-4,-1,-8,-9,6,-2,3,9,7,3,-6,1,-9,7,10,-9,8,-9,1,-5,-1,5,10,-6,-5,-3,8,-8,9,-10,1,-3,-1,5,-10,10,-9,3,-10,-10,-2,7,7,8,-1,2,10,-2,8,5,-10,-9,-4,10,-3,-1,3,6,-3,5,3,-9,3,-5,9,-8,9,-7,2,-6,-10,-2,5,5,2,-6,-7,9,-6,-2,-8,-3,-10,9,10,6,4,-4,-8,1,-9,5,1,8,10,-2,10,7,-4,1,6,5,-9,-1,8,-5,8,-2,7,8,-10,8,-4,10,-3,-3,2,9,6,6,-1,-2,-4,9,6,9,-8,6,3,-3,10,-5,5,-2,3,7,-1,-2,5,4,-1,-7,-1,-4,-10,-1,4,-1,-10,-9,10,-7,-5,4,2,-1,-3,3,-9,8,-3,-10,-3,-5,-5,-5,2,-4,1,-9,7,8,-8,4,10,-9,-9,2,-1,6,-3,8,1,4,-1,-6,3,-10,5,-10,-6,-9,-7,8,10,-3,4,-8,-5,-8,-7,7,-6,-3,-3,-7,-10,-5,-7,-7,6,10,9,-5,-2,3,7,9,8,-4,5,-1,8,-3,8,4,8,-4,-3,3,3,-5,7,2,6,-10,9,-7,7,4,10,9,-1,6,3,-7,7,-7,-6,4,6,6,-5,-2,2,6,-3,1,8,-8,-9,9,7,-2,4,-8,10,-6,6,5,-6,-2,-6,3,-2,-8,5,9,-1,6,9,-8,7,-3,-5,-3,-9,-8,-1,2,-9,6,-6,-8,8,-6,10,-5,9,-4,-6,5,-3,2,-3,9,5,-10,2,9,3,-8,-9,-2,3,-5,2,-6,-5,8,3,4,3,-8,-1,7,-4,7,-10,-6,-4,3,2,-10,8,-7,-7,10,4,-7,6,-6,-10,4,1,-4,10,8,7,-1,10,-7,-8,7,4,4,1,-10,3,3,-5,-7,-8,-9,7,-9,7,-3,2,4,5,6,9,9,2,-6,-10,-4,-1,3,-2,-4,10,-3,-7,-8,8,-10,-10,9,-10,-10,1,1,6,2,10,-8,-3,-5,-1,-5,-9,-6,-2,2,1,6,-4,5,-3,-10,3,3,1,6,-1,1,-4,8,3,1,1,-7,4,-7,-7,8,-6,-5,1,1,10,3,-8,-3,-2,-4,-2,8,-10,-1,-3,-8,3,6,-3,-5,8,1,8,6,8,3,-10,4,-7,9,-5,8,10,-2,-10,10,-5,-3,-6,-5,8,4,10,-10,-6,-6,7,1,-8,2,9,6,-4,-1,8,5,-3,-6,1,-9,-8,-10,-8,4,-1,4,10,-6,-8,3,2,-4,8,-7,9,-6,10,1,6,-2,2,8,5,-4,-4,1,-6,-2,-6,-5,-4,9,8,2,3,-2,-1,7,-6,-8,-10,6,-3,-10,7,1,6,-7,-8,-8,-2,-8,-1,-8,-7,-9,5,-3,-4,-5,-8,-4,6,1,-10,-9,-9,7,3,9,2,-5,3,-7,-2,-10,1,-7,5,3,6,10,-8,-5,2,8,-2,-3,2,-2,2,-3,5,-10,-7,-6,2,10,2,-8,9,-8,-1,-6,9,-5,9,4], dtype = "int16")#candidate|14536|(1280,)|const|int16
call_14535 = func_13784_call(relay.reshape(const_14536.astype('int16'), [10, 16, 8]))
call_14537 = func_13784_call(relay.reshape(const_14536.astype('int16'), [10, 16, 8]))
output = relay.Tuple([call_14529,call_14535,const_14536,])
output2 = relay.Tuple([call_14530,call_14537,const_14536,])
func_14552 = relay.Function([], output)
mod['func_14552'] = func_14552
mod = relay.transform.InferType()(mod)
output = func_14552()
func_14553 = relay.Function([], output)
mutated_mod['func_14553'] = func_14553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10188_call = mod.get_global_var('func_10188')
func_10190_call = mutated_mod.get_global_var('func_10190')
call_14559 = func_10188_call()
call_14560 = func_10188_call()
output = relay.Tuple([call_14559,])
output2 = relay.Tuple([call_14560,])
func_14561 = relay.Function([], output)
mod['func_14561'] = func_14561
mod = relay.transform.InferType()(mod)
mutated_mod['func_14561'] = func_14561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14561_call = mutated_mod.get_global_var('func_14561')
call_14562 = func_14561_call()
output = call_14562
func_14563 = relay.Function([], output)
mutated_mod['func_14563'] = func_14563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14499_call = mod.get_global_var('func_14499')
func_14501_call = mutated_mod.get_global_var('func_14501')
call_14622 = func_14499_call()
call_14623 = func_14499_call()
func_7646_call = mod.get_global_var('func_7646')
func_7647_call = mutated_mod.get_global_var('func_7647')
call_14647 = relay.TupleGetItem(func_7646_call(), 1)
call_14648 = relay.TupleGetItem(func_7647_call(), 1)
output = relay.Tuple([call_14622,call_14647,])
output2 = relay.Tuple([call_14623,call_14648,])
func_14674 = relay.Function([], output)
mod['func_14674'] = func_14674
mod = relay.transform.InferType()(mod)
output = func_14674()
func_14675 = relay.Function([], output)
mutated_mod['func_14675'] = func_14675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14482_call = mod.get_global_var('func_14482')
func_14484_call = mutated_mod.get_global_var('func_14484')
call_14684 = relay.TupleGetItem(func_14482_call(), 2)
call_14685 = relay.TupleGetItem(func_14484_call(), 2)
const_14692 = relay.const([[1.900990,5.363079,-9.753456,7.354815,-4.641791,-2.883713,-4.720451,5.550959,7.232400,-7.308559,-8.950761,-5.223586,9.104880,-1.873244,6.976134,-2.931555,6.297707,3.652693,9.522574,9.998638,-6.303485,5.989821,-3.822350,0.272859,1.119825,6.148605,-0.903200,-7.216517,-7.116709,2.772635],[-1.223064,-7.781322,-2.075921,-8.411750,-5.527661,1.818160,0.057890,5.211291,7.893445,8.104046,-0.531224,-1.227754,5.664533,-9.531276,0.988858,7.783864,-3.827922,-2.627880,7.183910,-2.781278,-5.862053,-6.581128,-5.697221,8.127002,-6.230175,-0.235838,0.416091,-4.651080,3.000017,-7.334801],[-6.646539,2.872131,1.161780,7.085854,-7.348509,-6.096265,-7.682612,-9.253952,-7.870166,-3.008790,0.154774,-3.828753,-1.865930,4.285313,5.823259,-6.410045,5.463064,-1.451550,3.977457,8.594664,6.509689,-5.727042,-1.628949,8.214135,3.738974,-3.753246,-6.130745,1.021442,9.913828,8.559762],[2.455336,-8.936745,7.233903,6.840358,0.419841,-5.291918,0.394519,-5.178170,1.916452,-3.159707,5.464524,1.215434,3.646264,-6.261056,5.253442,-6.378911,-1.453924,4.644265,0.897270,-5.371546,2.890058,-5.292121,-2.406771,4.495042,-8.833525,-8.162417,-4.816573,8.031337,-5.780746,-2.905339],[6.371951,-4.267324,0.584292,9.702969,9.620055,6.599912,-3.995253,9.136918,-2.443469,1.598065,-9.631209,9.802328,2.259458,4.635297,-6.119246,-0.031165,-1.525363,9.196770,-0.545710,-3.018083,1.993540,3.648025,3.057083,-8.120230,6.519191,-0.584068,3.393535,-5.709920,9.556421,-9.715238],[3.268082,2.918297,-3.300724,2.667982,-6.269497,-9.943654,-2.633088,1.717593,-9.937709,0.635618,6.424077,7.402261,7.709594,-8.973754,6.600171,4.431144,8.304283,-1.299661,5.190048,-7.871280,-3.495893,9.916943,-7.536066,-4.090044,-9.706424,-0.565887,-6.552319,-6.256077,8.644639,-3.184360]], dtype = "float32")#candidate|14692|(6, 30)|const|float32
bop_14693 = relay.less_equal(call_14684.astype('bool'), relay.reshape(const_14692.astype('bool'), relay.shape_of(call_14684))) # shape=(6, 30)
bop_14696 = relay.less_equal(call_14685.astype('bool'), relay.reshape(const_14692.astype('bool'), relay.shape_of(call_14685))) # shape=(6, 30)
func_12834_call = mod.get_global_var('func_12834')
func_12839_call = mutated_mod.get_global_var('func_12839')
var_14698 = relay.var("var_14698", dtype = "int8", shape = (864,))#candidate|14698|(864,)|var|int8
var_14699 = relay.var("var_14699", dtype = "int64", shape = (630,))#candidate|14699|(630,)|var|int64
var_14700 = relay.var("var_14700", dtype = "bool", shape = (1120,))#candidate|14700|(1120,)|var|bool
call_14697 = relay.TupleGetItem(func_12834_call(relay.reshape(var_14698.astype('int8'), [864,]), relay.reshape(var_14699.astype('int64'), [630,]), relay.reshape(var_14700.astype('bool'), [8, 140]), relay.reshape(bop_14693.astype('float32'), [180,]), ), 0)
call_14701 = relay.TupleGetItem(func_12839_call(relay.reshape(var_14698.astype('int8'), [864,]), relay.reshape(var_14699.astype('int64'), [630,]), relay.reshape(var_14700.astype('bool'), [8, 140]), relay.reshape(bop_14693.astype('float32'), [180,]), ), 0)
output = relay.Tuple([bop_14693,call_14697,var_14698,var_14699,var_14700,])
output2 = relay.Tuple([bop_14696,call_14701,var_14698,var_14699,var_14700,])
func_14708 = relay.Function([var_14698,var_14699,var_14700,], output)
mod['func_14708'] = func_14708
mod = relay.transform.InferType()(mod)
mutated_mod['func_14708'] = func_14708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14708_call = mutated_mod.get_global_var('func_14708')
var_14710 = relay.var("var_14710", dtype = "int8", shape = (864,))#candidate|14710|(864,)|var|int8
var_14711 = relay.var("var_14711", dtype = "int64", shape = (630,))#candidate|14711|(630,)|var|int64
var_14712 = relay.var("var_14712", dtype = "bool", shape = (1120,))#candidate|14712|(1120,)|var|bool
call_14709 = func_14708_call(var_14710,var_14711,var_14712,)
output = call_14709
func_14713 = relay.Function([var_14710,var_14711,var_14712,], output)
mutated_mod['func_14713'] = func_14713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11007_call = mod.get_global_var('func_11007')
func_11008_call = mutated_mod.get_global_var('func_11008')
call_14725 = func_11007_call()
call_14726 = func_11007_call()
uop_14792 = relay.cos(call_14725.astype('float32')) # shape=(11, 3, 16)
uop_14794 = relay.cos(call_14726.astype('float32')) # shape=(11, 3, 16)
func_12455_call = mod.get_global_var('func_12455')
func_12458_call = mutated_mod.get_global_var('func_12458')
const_14810 = relay.const([-2.726461,-8.480297,5.469905,-7.690159,7.771427,-8.607303,7.606923,9.768613,-0.329248,-5.845575,-2.961131,-4.320343,-8.811444,4.531516,-7.960629,-6.695422,-2.706741,3.425898,8.665130,-4.664440,-3.551444,1.240752,-3.303999,-0.223260,3.274810,3.027629,-5.569601,4.101169,-3.861840,0.666775,-8.967526,-1.082799,-8.561658,-9.801635,4.349745,6.584453,5.480947,6.590677,9.696457,8.202300,-9.805756,-0.877902,-7.349606,-7.550754,8.268265,4.043009,4.618375,-6.140325,4.447174,-0.502131,-3.563918,-4.562215,-6.001926,4.732829,-7.970959,-7.132229,-7.814376,6.526223,2.144340,0.113472,9.612256,-3.630855,-1.797978,3.855377,6.255803,-0.494555,0.241852,-5.104306,5.077324,2.576162,-5.607462,-1.849367,-3.719767,5.740688,3.077004,-2.115515,0.772589,-5.463132,-1.212776,3.375939,0.950324,3.702555,-1.892127,-3.844227,2.321288,3.223858,-3.129361,-9.802999,-8.286365,-7.594274,8.636561,-6.462260,6.747967,-5.315547,-2.842723,6.140895,-3.621872,-4.742717,-1.117738,-4.463663,-0.538041,0.390200,9.654459,-7.441836,2.253618,-8.285871,3.210695,0.715741,0.595107,-6.706702,3.630431,6.310432,-2.465601,5.444695,-8.377883,2.355469,8.874310,7.258283,-4.758596,-9.491689,-5.486087,-0.688394,-8.110590,-0.012901,-3.874688,8.095519,1.933118,7.391669,6.983477,-6.025315,-4.687795,-5.094751,8.540782,-4.678790,6.966519,1.402220,6.523250,-1.679135,-3.313036,6.322793,7.870764,-6.974534,1.768851,3.835724,-5.451337,6.815659,8.839025,0.241808,5.685119,-9.605281,-5.428918,3.059109,-0.649385,6.341183,-2.525769,4.280367,-9.760710,-1.201313,8.480904,-5.157002,-7.688406,-8.489243,3.712561,-6.126787,5.255235,-4.321443,-1.050082,-0.766602,7.449661,0.374268,-0.191982,8.821962,1.086732,4.581016,0.306348,-3.294446,8.080579,7.066616,-7.132284,3.529132,6.027207,-0.521478,6.880968,-4.776876,-4.925544,1.989551,-0.226764,0.986824,-6.126700,-9.411424,-0.537695,7.759335,4.403188,6.849658,-3.946626,8.887190,-5.375200,-0.289893,-3.351063,-4.223725,-3.088286,-6.797189,-8.186793,-9.695049,-6.579526,2.416278,-3.217985,-6.437890,5.997193,1.557855,-4.787621,9.089357,-7.034105,7.367393,-7.543852,-2.748517,3.874966,5.101890,-4.792172,-1.847065,-0.827204,-4.157427,3.369662,-8.734834,-6.249791,-0.863546,5.861142,8.990287,5.494913,-5.827085,-8.290517,7.480424,2.168984,7.009305,-7.478281,-0.191896,6.354842,3.779590,5.374593,-5.905822,-1.803395,3.488670,-9.518634,0.981476,4.422755,-2.659092,-6.813908,9.595288,-5.923539,-1.146099,-7.852047,-9.282854,9.767733,-4.993200,6.785679,-1.839903,-7.233069,3.880521,-8.537565,-6.145922,9.309358,6.162458,-7.669728,8.366788,4.400190,-9.395450,4.704262,-4.798840,-5.520926,5.355296,2.890866,7.279551,4.779232,-2.963049,-1.001066,9.466436,9.893369,6.181474,5.472091,9.178742,-5.560062,0.377850,-9.809734,-3.398635,-0.856012,-6.376699,7.554163,7.856520,6.304737,-6.854423,5.665000,3.988413,-8.825600,-6.255580,7.532078,9.199492,8.227538,7.432722,-1.767916,2.250834,-4.889688,-8.494369,8.261351,-1.797458,6.742178,-1.673758,5.442906,-7.744798,7.299707,9.216332,-6.361616,-6.139358,2.662335,7.978234,-0.966318,5.597823,-1.935744,-7.197161,5.288908,-0.353472,-8.719650,9.908573,-9.583488,5.865809,1.631240,5.717516,1.595708,7.335481,0.331845,-3.745677,0.464265,-5.764644,7.926596,-9.739685,-6.305533,-7.626938,6.146167,-4.554001,8.732501,2.063948,-5.871922,-5.372140,2.995511,0.534762,-1.215813,-0.927738,6.858181,6.776799,2.831700,4.723928,1.515556,-8.163137,-0.730795,-7.273683,9.623460,-2.649203,-5.748474,6.205165,-7.082010,1.648267,5.582902,3.373103,-0.158976,0.538028,-2.855195,7.506763,-3.964245,-0.741802,-7.569312,-0.604174,4.753801,-8.269231,7.796973,7.389693,-1.099489,-9.548802,-3.731308,-6.006598,8.270170,-6.826620,-3.597890,5.988487,-1.253489,8.192640,-2.608785,-1.034720,-8.498199,-9.340023,-5.898251,-1.636627,-8.374702,-1.418413,-9.687872,8.743868,3.310138,4.752003,-8.316294,-0.875780,-1.475110,7.815523,-4.286150,-1.708260,-7.720549,-0.382937,-1.798833,1.910432,-9.641803,2.310818,-2.723925,-8.076075,5.134333,-4.887728,-2.335926,-4.789881,-1.265710,4.010636,7.368762,-0.931996,-2.905694,-4.164979,3.345288,2.639996,-9.281191,-0.961942,-9.609154,-1.006405,-5.616398,8.497557,0.572067,8.049354,4.458233,-8.123453,5.433571,7.549045,-8.930761,-2.084376,4.193941,3.187001,9.312727,1.350630,-4.574726,2.013095,-9.812125,2.265279,-1.541642,7.612873,6.332529,-6.837252,-9.204339,3.696307,6.508555,-0.219920,5.794261,-4.365995,0.937339,-0.687522,4.411257,-3.006873,-7.620250,-5.359031,8.927740,4.407989,6.478026,0.366124,2.755715,-4.527189,-3.094068,6.698737,-8.035371,-7.672040,8.109338,2.933751,-0.972232,-2.403730,1.948782,5.086352,7.038771,-7.797867,-2.068264,-0.133790,-0.401566,6.140595,-4.298926,-1.918773,-8.198673,-7.643648,-6.611540,6.276067,-9.704848,0.840375,-9.060792,-0.569444,9.848157,-3.838482,-1.408084,5.906006,-8.381967,8.123548,-0.100116,9.714402,9.871337,-1.245437,-3.585012,-1.987492,-3.798898,-4.970634,1.209366,-8.748443,5.088873,-0.548480,6.672488,-6.571774,-2.559370,-0.987930,-5.713579,-5.147524,-6.353228,7.363063,-4.184580,0.964836,4.511306,9.786052,-6.220866,-6.353679,-8.712353,5.654063,-7.506066,2.108337,4.700637,2.515538,-1.119208,6.955682,6.750373,8.835428,5.051198,-8.176679,-4.999207,0.330041,5.386522,5.962492,-2.971372,8.413517,-0.003645,-2.877849,7.602562,5.979791,9.191250,-2.606686,2.861123,-3.715958,-3.154218,-5.528374,-2.482073,2.982247,9.723125,4.902699,4.216574,-5.764980,-0.912759,2.614025,6.835716,8.727672,-5.524857,0.515098,9.766146,-5.821518,-5.291046,-0.283315,-8.030530,-9.131579,-0.005257,6.797745,-1.954417,-8.304852,-3.915514,-4.325639,-3.028776,-7.034107,9.274602,4.810232,0.760750,-0.249567,-1.189119,-1.715500,-6.758990,-7.605710,4.202538,-8.472601,3.191140,-7.622137,4.125434,1.337196,-3.517638,-5.061850,7.784485,-7.250162,8.408081,-6.752103,5.458439,-7.127077,3.307412,9.268317,-2.318549,7.775073,-3.743519,-0.216587,-8.471935,0.352950,3.066885,2.889834,8.912074,-3.976911,-6.096610,-2.921461,9.747766,-3.536989,5.781393,1.794268,9.349942,-8.131928,-9.929054,7.886975,-7.985753,4.324847,-3.485932,8.395512,-2.744718,-0.324369,-0.621558,7.797340,3.857919,7.120642,7.348084,7.263409,6.707124,-1.104801,-0.946536,-6.649356,-9.120776,-4.777706,-6.141971,8.798555,9.460493,-0.883344,-4.430766,-4.004108,1.170598,6.203584,-6.180827,7.977732,-2.355584,-1.539578,-4.868976,8.622027,-2.411551,1.528761,5.628231,-7.549973,1.297108,1.721420,-7.131396,1.873843,9.040757,-2.953440,1.285196,7.069593,6.119821,-3.452898,-4.872739,-0.910395,-2.428369,-4.006909,-5.487830,-8.323544,3.656095,-5.029571,6.019197,5.170346,-3.304706,9.870008,4.613508,8.679361,-7.580466,-9.114100,9.541131,4.316403,1.794521,-9.459609,-5.421456,5.600998,-9.985991,5.415523,7.862770,-5.806181,-6.648958,-2.269085,-8.485940,-1.445234,6.285449,6.689368,-6.453982,-9.994434,-2.109905,5.577513,-2.296039,-9.705904,-3.228529,-6.904171,-2.301319,5.315755,-5.972305,9.759015,2.031668,3.995044,-0.724195,-8.740874,-0.306993,-3.686180,0.079307,9.641657,-4.806696,-0.396668,-3.106563,2.401596,9.768876,2.102608,-7.370594,-1.838150,9.436000,-5.493945,-9.544057,-5.560883,-9.737933,-8.465132,-8.279290,1.252078,4.885197,-3.421418,-8.709046,9.339884,-0.338771,-0.704414,9.399372,9.120692,-7.822345,-1.283290,-1.215952,1.861956,-3.721470,-7.055565,-6.128274,5.138884,2.947195,6.647960,0.468107,4.200193,7.648998,-4.204168,-3.335740,1.899477,-3.538995,7.199200,-7.586459,3.137073,-7.428654,-7.143372,5.951956,1.208732,2.981361,-1.656696,3.589659,-7.868339,7.464932,9.365895,-5.625578,1.183333,-9.168074,8.883078,4.099479,8.885305,-1.483630,-5.934773,-0.709053,-3.188677,-4.206402,-8.416190,-8.371339,5.507496,-2.423353,4.438464,9.248370,9.149914,-7.319379,7.062388,6.422495,2.639003,-4.716994,0.457806,1.055177,-8.601648,-3.485381,6.790023,1.885723,3.637741,5.953594,9.610925,6.042956,2.524061,1.821819,5.582319,9.184063,9.217359,0.676513,-8.231296,-7.041400,-5.884373,-8.076555,-5.513378,-8.266099,2.178492,-9.979767,6.223198,3.951238,4.267563,1.356258,4.325603,-1.497786,-9.526691,4.440465,-1.160177,2.263040,-3.238432,7.301139,8.321963,-3.377682,3.507963,5.534248,-3.699824,0.694694,-9.366985,8.852618,-2.183718,-8.601116,3.980244,6.393318,1.721526,-0.959762,-0.229597,-6.941346,-3.471953,-7.932713,-8.257135,-6.163828,-9.604202,-3.372034,-2.782072,-7.769883,5.449748,9.765781,-4.121918,1.745785,7.290399,-7.640912,9.294609,8.912245,3.198134,9.936147,-5.556257,3.734422,-1.642183,5.155429,6.234529,7.100383,-6.179156,3.096558,9.151515,-7.887115,-8.546437,4.797559,-5.376979,6.178601,-7.565821,9.939967,-9.429495,-1.826024,-2.985189,7.164039,9.933260,7.625806,6.403026,1.785315,6.515828,4.240070,-1.375384,1.582208,-4.430393,-7.541463,1.779360,4.992045,-2.275666,-0.338807,3.273754,-6.187382,-2.012592,-4.019604,-6.480257,3.685362,9.614414,-1.396497,1.198402,-8.743697,-9.720963,-2.171341,-1.631159,-4.438888,2.653546,-7.876448,-4.590054,-2.165005,-9.795027,0.827931,-3.637515,-8.280651,5.433099,7.262065,-9.819030,-4.019056,-4.776994,-6.019873,-5.576580,-2.413479,-0.963927,-4.213435,0.032480,6.648581,5.426983,2.998286,2.674023,-0.612677,-0.312091,0.329653,2.465269,1.735735,4.776770,7.435609,-6.477282,5.446900,-3.396808,-3.956406,-4.377550,6.494232,-1.780193,6.561749,-4.158812,-2.914604,9.175101,4.840444,-4.504985,2.999807,-5.581847,5.490927,-1.113422,1.753627,9.320548,-0.801529,-6.615363,8.146927,-4.896660,-9.777050,-4.777853,9.132884,3.631543,0.277838,-8.831162,9.917074,1.656942,5.106079,9.770888,-8.169552,-9.230870,2.635984,-8.349157,1.061994,5.058685,4.039583,7.085336,-3.459664,2.425569,-1.506651,-2.090390,-9.125179,-3.916495,5.906135,6.728236,-5.292332,-8.833746,-2.367091,5.646199,-1.869156,2.003360,-9.068285,-0.749298,8.531847,-9.364812,0.119966,1.544837,-8.453532,-0.415098,-4.629701,7.543577,8.907432,-6.926081,-3.610279,-8.196537,-8.017726,-5.941124,-6.950118,5.980264,-9.780768,9.309966,-4.638923,-8.876489,-4.598400,-5.711776,-4.260688,-1.334701,-1.640175,1.645079,-9.005002,9.125636,0.973323,7.504860,-5.576615,-1.479188,0.888768,7.849728,-6.385560,-4.559923,-0.020555,3.597629,7.503999,-1.292610,-9.502511,-1.415534,4.609295,-5.792228,-3.859603,-0.900619,-3.137485,1.866093,-9.300470,-2.599021,-3.537638,-9.780018,8.013279,8.875020,2.973818,-2.064444,6.844067,-3.044796,-0.061940,-0.433623,-8.260072,-8.280868,2.389168,-0.780985,-9.409430,-2.784114,-1.220836,3.074845,3.148614,-4.724447,-6.874711,-4.136266,2.645961,8.034193,6.783343,-9.333280,-7.384950,6.636448,3.219954,-2.380940,-1.056499,-8.753401,6.845680,-6.265840,0.890268,8.294677,-9.316643,0.295815,-4.191609,1.765196,-5.515824,2.415130,-6.095868,-0.564765,3.932688,3.383031,-1.438346,-4.599181,1.002439,-0.432078,7.947476,9.986413,0.317792,2.360869,8.436631,-8.527285,3.355675,-9.427721,-0.703971,5.854574,3.155634,8.044927,-1.208090,6.285277,-7.735904,-5.213217,0.159802,4.183559,6.600996,-4.849149,-6.862770,-3.345079,6.685116,7.268191,-5.914767,8.851626,-6.973900,2.795967,-1.819180,-6.750972,-7.127750,-8.139613,-8.591554,-8.699681,-9.178343,-2.806097,8.503936,-5.780275,-6.299670,-0.915117,-2.077429,-1.820115,-8.713285,-9.765284,4.176863,-6.660796,3.902176,7.891051,-7.075044,4.630761,9.917125,4.294206,9.911669,5.996501,-2.602324,-2.954768,8.306137,3.378884,-0.991011,-8.209715,-9.613309,4.728328,6.876621,-8.445860,-2.057029,-3.470350,1.437813,4.439512,-6.713081,-1.927112,-2.158798,1.477419,-2.107683,-8.604612,-0.820443,-9.959470,4.578218,7.840591,-3.276253,-3.333503,0.214622,-5.685989,4.171006,0.701609,-1.219092,-9.474429,-8.262580,-3.174400,-6.740563,6.692674,8.919259,4.765558,2.600700,5.942542,-6.397697,5.777229,2.779327,7.355165,9.517820,-6.843911,-4.814632,-3.483982,-6.912568,8.334690,7.988248,-6.076830,-9.032207,4.289728,-4.762512,-7.662603,1.577179,-7.736840,5.174962,2.850043,3.825812,5.049165,-9.580821,-1.869900,-5.418588,5.209143,4.157874,3.910047,4.639168,4.190945,3.675239,0.694923,6.644490,7.145090,6.631310,7.733940,-8.271129,-4.726056,4.287959,-7.770381,2.925104,9.001232,5.686149,-6.099926,-6.250295,-3.657256,3.433080,-9.713295,4.333924,-7.955698,-9.922806,7.152267,-2.343255,3.673729,4.447275,2.125889,3.516772,8.000371,8.795613,5.796377,0.124364,-7.642884,2.721829,-1.549790,-3.505333,9.868246,-2.320660,-8.789127,8.667200,-5.844042,9.915607,4.823895,3.745600,6.814017,-6.950552,-2.567256,-3.887486,9.670938,2.964736,-0.870246,-1.887577,-7.906316,8.759309,8.061138,-8.107087,2.820247,7.608691,-0.352858,7.018374,-7.290993,-6.425651,3.230973,6.250781,4.457967,-3.263671,-5.002947,2.495533,-1.476356,9.090624,5.708852,7.798957,8.857954,7.453697,1.621959,4.136492,9.092697,-7.003685,-8.046973,5.695697,-0.394668,-3.990184,-4.361854,3.292011,-4.960339,-2.636315,-0.846957,-0.242837,-3.144922,4.698492,-7.949162,8.480038,2.579620,-2.767212,6.167069,7.873492,-1.392744,1.778532,6.941909,3.706914,5.422409,-2.224502,7.832742,-0.899660,-7.576317,-0.611250,-0.553351,-4.088525,6.044705,-6.159769,-8.269755,3.264677,1.435631,6.563721,4.288188,-9.940351,-4.319880,6.288544,9.110692,-0.148608,2.421730,-3.514722,-3.124782,5.811272,1.658489,9.822618,2.520110,-4.694581,4.526593,-1.247009,-7.271599,7.144742,6.201382,2.968686,-3.528160,-9.603556,-6.015019,-7.392776,-8.671935,-8.945227,4.151440,9.344217,-9.008771,3.079359,-6.068568,8.389830,-1.097473,4.826655,5.379114,-6.981640,-5.779157,9.838065,5.377831,-0.900714,-1.919692,4.369185,-4.759971,-7.672251,7.863279,-0.378669,0.139068,-2.601291,-2.029198,2.962674,-3.251027,-8.924401,8.745181,5.243274,3.826540,-6.524100,0.425932,3.609446,-7.486844,-4.138186,2.418600,2.441189,-7.172040,-8.339397,-9.325017,-2.399173,2.035173,9.902772,6.126700,7.123338,-3.364844,-7.724135,3.311619,7.468940,9.826638,5.624611,-1.448599,-3.608444,1.987813,-3.264123,-0.300394,-4.362267,4.323262,-8.752855,0.697183,6.610485,8.892830,5.303477,5.358811,6.233366,-2.093630,6.171956,4.549050,-5.522267,-4.819679,-8.459929,6.680872,-4.749324,5.559774,0.565092,-4.806751,-4.998970,-7.887814,-9.504382,7.308067,0.810154,8.322981,-3.725915,-2.982944,5.191890,4.242590,9.027997,-7.002892,8.132447,3.196063,-9.651691,8.735099,3.827709,-7.139736,0.558012,7.763513,-6.384831,1.346870,-0.876686,2.651773,-2.779839,1.444390,3.481981,1.474953,3.733784,-9.251850,-2.124464,4.515357,1.501110,-2.953944,7.570201,4.989778,-7.909144,-0.491331,-2.317120,-4.967091,4.138999,7.803675,8.954506,3.398245,4.063882,9.495269,-0.418704,8.447981,-1.934432,-4.986564,-3.966185,0.765781,1.874045,2.970888,7.511299,-4.646795,6.199511,-7.478705,3.135507,-9.618617,8.991224,-3.471376,-7.226189,9.953160,9.053836,-6.491203,-3.895610,-9.111141,3.429415,8.311406,4.377898,0.413292,5.671074,-5.810794,-4.419869,3.389066,-8.911377,3.459082,-9.430417,1.123889,-5.552009,3.463953,-2.195361,-8.982062,4.006414,-2.640921,-9.174085,1.730434,5.572069,-2.495165,-5.971147,0.198222,6.182963,9.962633,-0.598492,-9.965970,-5.319450,5.096268,4.200890,3.901578,5.425318,-4.022042,7.780063,-6.297958,6.425520,-4.327785,-3.618921,-2.625443,-6.788639,3.592394,-2.257559,-7.995385,8.566759,2.976903,4.438558,1.471724,3.924528,-0.262214,-4.130749,1.333004,9.837879,9.932662,-6.785032,-9.788329,-0.820727,5.510267,2.825303,6.393015,0.492876,1.862004,8.827084,3.828717,-3.432213,-0.622278,-8.145431,-8.982471,0.384306,-6.218283,0.064633,0.180442,-0.942338,5.655878,-6.558478,4.057503,1.335045,-9.276783,4.894324,5.382060,-2.733715,-7.578950,-2.654288,-8.532658,6.332381,0.558019,4.905642,-7.084874,8.971521,2.177096,-6.298130,0.615747,-7.392046,3.934088,3.845628,5.613871,-5.017091,1.469268,7.658751,-9.352904,-5.993646,6.404923,-7.777889,5.791912,5.660228,5.375499,1.946319,-1.414567,1.375239,-7.870293,-8.914240,-4.242728,9.478677,1.118762,8.130099,5.073248,8.360091,-5.129284,-7.099259,7.447387,-9.340933,-8.941249,4.805597,5.554688,-3.093309,-7.330090,-5.391176,7.684465,-7.453458,-5.734285,-1.623318,0.922833,-1.147850,-0.102475,8.483436,1.924212,-6.552826,-5.861187,-8.489655,-6.678164,8.363893,3.664705,7.122992,5.157637,-6.306452,-4.905316,-1.408120,-9.870678,8.338642,8.797046,7.385881,-5.790703,-9.237839,2.455156,6.111970,7.968454,-0.931914,-9.727445,2.083394,1.303649,1.379812,0.382231,3.590362,-5.162034,-6.843386,-9.865039,-1.151956,5.148597,4.586962,9.720170,1.298936,5.137276,-1.944129,8.557720,3.754498,6.511325,-0.597440,-5.539386,-6.295939,-5.060800,0.682991,-6.703925,-3.482384,-1.460954,1.479703,-6.967772,6.337668,-6.285506,9.357479,5.706241,2.698290,1.054502,9.660763,5.510574,-6.186607,-9.525740,-7.151083,-7.095923,4.447555,-1.196597,-4.602014,8.639592,-3.915645,0.183946,0.580058,5.603710,1.786557,3.922159,-6.954567,0.105649,-4.524334,-5.891015,-9.973984,4.938799,-7.835953,-0.675776,-8.574127,-8.351803,-0.365988,-5.978213,-7.303674,-2.323968,-9.084526,5.471316,-4.382585,-1.101292,-8.520521,-9.690401,6.802933,-0.869681,2.341338,-4.164645,-2.730945,9.660110,7.402060,3.698148,9.694987,4.943101,1.501565,-9.161756,6.026530,-4.598683,-3.707543,6.081946,2.009870,6.235224,-5.710822,-7.814933,-5.458277,1.503416,-2.700544,4.375993,-1.474593,2.229627,5.414977,-9.829549,-8.284756,8.618847,8.101035,-9.816374,-5.716707,2.877843,-4.152578,-3.740139,0.462322,-9.136037,-4.815187,4.528549,-2.960232,-5.395806,4.617655,8.828225,2.578925,-2.597570,1.141088,5.820866,-6.862399,-6.277031,6.537196,2.008747,0.189265,-4.327468,0.680925,-7.057090,-1.476245,-2.940835,4.112289,-4.533745,-2.765891,2.099625,0.233971,1.670740], dtype = "float64")#candidate|14810|(1800,)|const|float64
call_14809 = relay.TupleGetItem(func_12455_call(relay.reshape(const_14810.astype('float64'), [15, 8, 15])), 2)
call_14811 = relay.TupleGetItem(func_12458_call(relay.reshape(const_14810.astype('float64'), [15, 8, 15])), 2)
func_9979_call = mod.get_global_var('func_9979')
func_9981_call = mutated_mod.get_global_var('func_9981')
call_14818 = relay.TupleGetItem(func_9979_call(), 0)
call_14819 = relay.TupleGetItem(func_9981_call(), 0)
func_11260_call = mod.get_global_var('func_11260')
func_11262_call = mutated_mod.get_global_var('func_11262')
call_14843 = relay.TupleGetItem(func_11260_call(), 0)
call_14844 = relay.TupleGetItem(func_11262_call(), 0)
output = relay.Tuple([uop_14792,call_14809,const_14810,call_14818,call_14843,])
output2 = relay.Tuple([uop_14794,call_14811,const_14810,call_14819,call_14844,])
func_14862 = relay.Function([], output)
mod['func_14862'] = func_14862
mod = relay.transform.InferType()(mod)
output = func_14862()
func_14863 = relay.Function([], output)
mutated_mod['func_14863'] = func_14863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13355_call = mod.get_global_var('func_13355')
func_13357_call = mutated_mod.get_global_var('func_13357')
call_14886 = relay.TupleGetItem(func_13355_call(), 1)
call_14887 = relay.TupleGetItem(func_13357_call(), 1)
func_11574_call = mod.get_global_var('func_11574')
func_11575_call = mutated_mod.get_global_var('func_11575')
call_14909 = func_11574_call()
call_14910 = func_11574_call()
output = relay.Tuple([call_14886,call_14909,])
output2 = relay.Tuple([call_14887,call_14910,])
func_14956 = relay.Function([], output)
mod['func_14956'] = func_14956
mod = relay.transform.InferType()(mod)
output = func_14956()
func_14957 = relay.Function([], output)
mutated_mod['func_14957'] = func_14957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7102_call = mod.get_global_var('func_7102')
func_7104_call = mutated_mod.get_global_var('func_7104')
call_14961 = relay.TupleGetItem(func_7102_call(), 0)
call_14962 = relay.TupleGetItem(func_7104_call(), 0)
output = call_14961
output2 = call_14962
func_14964 = relay.Function([], output)
mod['func_14964'] = func_14964
mod = relay.transform.InferType()(mod)
output = func_14964()
func_14965 = relay.Function([], output)
mutated_mod['func_14965'] = func_14965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12635_call = mod.get_global_var('func_12635')
func_12637_call = mutated_mod.get_global_var('func_12637')
call_15025 = func_12635_call()
call_15026 = func_12635_call()
output = relay.Tuple([call_15025,])
output2 = relay.Tuple([call_15026,])
func_15041 = relay.Function([], output)
mod['func_15041'] = func_15041
mod = relay.transform.InferType()(mod)
output = func_15041()
func_15042 = relay.Function([], output)
mutated_mod['func_15042'] = func_15042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7420_call = mod.get_global_var('func_7420')
func_7422_call = mutated_mod.get_global_var('func_7422')
call_15043 = relay.TupleGetItem(func_7420_call(), 0)
call_15044 = relay.TupleGetItem(func_7422_call(), 0)
func_11078_call = mod.get_global_var('func_11078')
func_11079_call = mutated_mod.get_global_var('func_11079')
call_15052 = relay.TupleGetItem(func_11078_call(), 0)
call_15053 = relay.TupleGetItem(func_11079_call(), 0)
func_6885_call = mod.get_global_var('func_6885')
func_6886_call = mutated_mod.get_global_var('func_6886')
call_15054 = relay.TupleGetItem(func_6885_call(), 0)
call_15055 = relay.TupleGetItem(func_6886_call(), 0)
output = relay.Tuple([call_15043,call_15052,call_15054,])
output2 = relay.Tuple([call_15044,call_15053,call_15055,])
func_15056 = relay.Function([], output)
mod['func_15056'] = func_15056
mod = relay.transform.InferType()(mod)
mutated_mod['func_15056'] = func_15056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15056_call = mutated_mod.get_global_var('func_15056')
call_15057 = func_15056_call()
output = call_15057
func_15058 = relay.Function([], output)
mutated_mod['func_15058'] = func_15058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8371_call = mod.get_global_var('func_8371')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_15062 = func_8371_call()
call_15063 = func_8371_call()
output = call_15062
output2 = call_15063
func_15101 = relay.Function([], output)
mod['func_15101'] = func_15101
mod = relay.transform.InferType()(mod)
mutated_mod['func_15101'] = func_15101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15101_call = mutated_mod.get_global_var('func_15101')
call_15102 = func_15101_call()
output = call_15102
func_15103 = relay.Function([], output)
mutated_mod['func_15103'] = func_15103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mod.get_global_var('func_6126')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_15116 = func_6126_call()
call_15117 = func_6126_call()
output = call_15116
output2 = call_15117
func_15125 = relay.Function([], output)
mod['func_15125'] = func_15125
mod = relay.transform.InferType()(mod)
mutated_mod['func_15125'] = func_15125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15125_call = mutated_mod.get_global_var('func_15125')
call_15126 = func_15125_call()
output = call_15126
func_15127 = relay.Function([], output)
mutated_mod['func_15127'] = func_15127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9193_call = mod.get_global_var('func_9193')
func_9194_call = mutated_mod.get_global_var('func_9194')
call_15128 = func_9193_call()
call_15129 = func_9193_call()
func_6429_call = mod.get_global_var('func_6429')
func_6430_call = mutated_mod.get_global_var('func_6430')
call_15130 = func_6429_call()
call_15131 = func_6429_call()
output = relay.Tuple([call_15128,call_15130,])
output2 = relay.Tuple([call_15129,call_15131,])
func_15151 = relay.Function([], output)
mod['func_15151'] = func_15151
mod = relay.transform.InferType()(mod)
output = func_15151()
func_15152 = relay.Function([], output)
mutated_mod['func_15152'] = func_15152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8133_call = mod.get_global_var('func_8133')
func_8134_call = mutated_mod.get_global_var('func_8134')
call_15196 = relay.TupleGetItem(func_8133_call(), 0)
call_15197 = relay.TupleGetItem(func_8134_call(), 0)
var_15199 = relay.var("var_15199", dtype = "float64", shape = (11, 3, 16))#candidate|15199|(11, 3, 16)|var|float64
bop_15200 = relay.mod(call_15196.astype('float32'), relay.reshape(var_15199.astype('float32'), relay.shape_of(call_15196))) # shape=(11, 3, 16)
bop_15203 = relay.mod(call_15197.astype('float32'), relay.reshape(var_15199.astype('float32'), relay.shape_of(call_15197))) # shape=(11, 3, 16)
func_14964_call = mod.get_global_var('func_14964')
func_14965_call = mutated_mod.get_global_var('func_14965')
call_15208 = func_14964_call()
call_15209 = func_14964_call()
output = relay.Tuple([bop_15200,call_15208,])
output2 = relay.Tuple([bop_15203,call_15209,])
func_15220 = relay.Function([var_15199,], output)
mod['func_15220'] = func_15220
mod = relay.transform.InferType()(mod)
var_15221 = relay.var("var_15221", dtype = "float64", shape = (11, 3, 16))#candidate|15221|(11, 3, 16)|var|float64
output = func_15220(var_15221)
func_15222 = relay.Function([var_15221], output)
mutated_mod['func_15222'] = func_15222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12654_call = mod.get_global_var('func_12654')
func_12656_call = mutated_mod.get_global_var('func_12656')
call_15267 = relay.TupleGetItem(func_12654_call(), 0)
call_15268 = relay.TupleGetItem(func_12656_call(), 0)
func_3593_call = mod.get_global_var('func_3593')
func_3596_call = mutated_mod.get_global_var('func_3596')
const_15278 = relay.const([0.386866,2.939927,4.436405,5.098268,-9.355673,8.509749,2.387176,7.752686,4.756586,0.553311,-9.856836,-9.393395,-4.319419,9.250477,-1.520773,-8.494721,-3.270623,-3.541820,6.280203,-3.835412,-0.404810,2.479053,-3.681368,5.270325,7.982172,-8.021463,-9.047212,5.012618,-5.643472,-1.821398,3.678499,3.084217,1.156439,3.822103,6.484932,-7.412943,-3.404287,8.367506,3.568303,-1.646245,8.786649,-1.792742,9.857248,-0.363600,3.360181,0.605296,3.737834,-2.645399,-6.700689,-0.033814,5.327273,8.762846,-6.449678,-7.164402,5.938072,-8.180042,-6.920975,5.995959,-3.331625,2.777168,-3.120603,-6.031792,0.366272,-5.660635,2.254355,7.615550,-0.638391,-2.932884,3.741184,-5.319366,9.414174,-5.737634,5.900234,8.094326,6.750267,3.802554,1.958555,-1.246940,-8.637981,-1.620996,1.206088,1.641010,-5.729514,-6.686966,-2.630757,8.930618,-9.918010,2.524408,7.877751,7.668127,-1.126896,-5.560988,6.110231,-5.980188,-3.724527,4.351908,5.816889,1.878647,-0.463854,0.103465,-6.882333,-5.762194,-5.893557,-2.857086,-8.865362,2.051019,7.621474,0.603394,-3.539645,-4.592370,-3.927706,-5.423952,-8.098261,-0.784346,2.398177,-1.679684,-3.918387,-3.583247,-6.050286,-4.037089,8.576930,3.064033,7.115556,9.630291,9.047704,-4.702940,9.062981,7.853897,-8.203226,-8.181252,3.864771,3.161085,3.846569,8.781843,6.770089,-9.671950,8.806421,8.357444,-0.258038,-6.916599,-9.335221,-3.235846,6.711341,-5.534072,7.390444,7.919751,8.336946,-8.123976,2.998440,-0.979965,9.157433,7.509626,5.370305,6.679867,6.214126,1.161955,1.775708,1.148164,9.742635,-3.724623,-7.738257,8.875642,2.168199,-7.393229,2.745899,5.206332,8.759071,4.009359,3.575529,9.216308,-4.908715,-3.636726,-2.745762,-4.382323,2.404562,-0.805204,1.538811,0.911371,6.032318,2.440266,8.912015,1.643184,7.379141,6.788542,8.111153,3.956221,4.560426,7.896586,9.079222,3.072993,6.015593,-9.687501,4.498689,0.585926,5.279873,-6.906773,8.896534,3.367139,-7.941781,0.510028,2.878160,-9.944853,-8.789315,-7.008615,6.315108,2.077091,1.309139,7.146204,6.734062,8.269803,4.010345,1.330998,5.530683,3.803650,3.149322,-7.826146,6.663557,6.507237,-8.006780,1.301066,7.945184,-2.572384,-9.782076,-2.762407,-9.106125,-2.915536,9.803842,-1.295874,0.858233,-0.111833,-1.380703,6.304245,9.839924,-5.014138,4.708537,-1.846126,-4.378682,7.738423,-4.022026,-2.793652,-3.225879,5.005926,9.621335,-5.168697,9.559690,3.716455,4.056618,-9.084763,-3.772666,0.535116,-3.386161,-7.987846,-0.011628,-6.912481,0.143872,-2.489652,8.158041,9.801187,8.891516,7.901189,1.941774,4.691999,-2.388245,5.508711,-8.422100,-6.140125,-9.512239,7.126171,-7.776265,-4.045711,-6.289536,3.686440,-1.245621,-9.157517,3.962497,-7.079709,8.415157,9.337515,8.514909,-7.060469,0.857049,8.142904,3.362680,7.231547,-8.649679,-3.777735,-9.478682,-9.435266,-6.584261,-0.042654,1.276681,-9.671468,-6.796300,-2.090527,9.930482,5.879688,5.915169,-2.600561,1.809447,-8.230327,3.863333,0.513520,2.602791,-8.512490,-8.659914,6.722428,-5.882674,-9.436715,4.344420,-6.679030,6.018492,-8.074867,-7.368656,-7.278038,-7.135361,8.132553,8.820825,1.082081,7.593482,-3.523465,-0.042025,9.351084,-8.195243,-9.911895,-0.818125,-9.516166,-8.380531,-6.795243,3.244620,1.294033,6.317465,-2.118882,6.722380,9.402688,0.192031,-5.577915,0.621341,-2.953343,-3.489518,-7.870453,-9.851083,-5.508145,9.194092,0.404382,1.184736,-9.976233,-6.474092,4.855456,-8.228314,-7.000201,3.623561,9.702632,-4.753246,-4.153523,-5.392734,0.558330,3.965886,-4.745475,-3.510705,3.749703,-2.287949,-8.065886,-8.381826,-5.912890,8.635068,2.096556,7.731126,8.058473,-0.863913,-6.526594,-2.624385,4.873085,-8.886573,-7.859676,-0.510042,-2.258158,7.139707,2.508845,5.723517,-1.939254,-1.829281,6.692007,0.695591,7.173883,-6.957852,-3.335900,3.465063,-5.924422,2.422038,-1.745589,-8.214193,-0.670528,8.827207,-9.327320,0.547423,1.263221,-9.593009,-6.214123,-3.952479,8.189434,9.301050,0.075819,-1.196554,-4.922447,3.092390,1.559341,-0.831871,8.585078,3.162510,-1.564987,4.637719,-3.425832,-8.716561,3.241810,-6.004501,4.831769,-0.678000,-5.125800,-3.525294,1.509576,1.566771,1.147890,-9.701281,3.428039,-7.501645,8.017182,-3.239006,9.119625,-5.593624,8.951996,-0.320185,-4.714932,5.938870,4.432817,-8.819008,8.115734,0.061177,5.813232,-3.796907,2.536911,-3.711394,-6.811553,-7.809902,1.952460,-1.040136,6.345199,4.526685,2.173663,-3.364509,-5.568181,3.401785,-3.291104,-6.173406,0.996183,-1.240507,-4.798927,1.219232,1.625090,-0.821040,-9.315841,3.647248,6.024102,2.045520,-6.121894,9.979875,-0.842138,-9.957130,6.620750,-7.776249,9.263045,1.559557,1.859436,-7.891430,-0.770427,9.924368,8.889525,-2.530755,2.165023,-2.185834,8.070126,-2.912996,-5.152616,-8.503935,-2.820094,-1.712911,-5.677318,6.540460,-8.550324,-9.538030,-2.685278,4.820236,5.326359,2.558111,-9.189960,-5.654563,2.878920,4.826683,5.038010,-9.993666,7.538487,-0.504803,-0.612185,0.601896,3.450654,-2.447811,-0.419626,-2.667762,8.988141,-1.585855,3.959773,-1.731749,-3.153378,-2.025450,7.886341,0.065243,-9.884588,-2.319820,0.691793,7.944327,-5.374301,-6.727385,-0.585635,-5.501513,-7.714569,6.074319,9.401106,8.506500,9.899492,5.368079,-9.076899,6.769845,-3.600884,5.324635,-7.793345,9.971140,-4.662582,4.480216,-6.541206,7.075603,-4.868840,-5.102443,-1.867964,1.154753,9.465110,-4.560852,7.526327,-1.468485,-3.612669,6.117424,3.490964,1.432008,6.306254,-5.130649,-1.574477,-4.830561,-2.319290,-5.808029,-3.061148,-2.259798,-9.887086,5.757798,6.499567,-6.684611,-7.033452,-7.496204,-3.619409,0.375397,-2.450791,7.325992,8.299791,5.168634,-4.831781,-3.543512,-6.544454,-3.393036,-1.958958,-2.007750,-8.892654,1.585134,4.363500,-5.497580,5.229839,6.832691,8.756924,-4.699975,-8.024573,-2.062566,1.666669,-6.871180,5.187387,-8.612306,-9.600752,7.718607,3.859245,1.832668,-4.011957,-2.555842,-2.861050,6.232563,-4.185455,-7.768808,-2.831480,7.723398,-6.611300,6.020797,6.168477,2.810593,-8.066656,-1.201047,4.349858,-1.607628,7.833213,2.828117,-5.195788,3.740690,-5.040498,-2.900976,-8.425250,-7.484519,8.744428,-1.661665,7.371458,-9.209712,5.758557,-8.902397,8.697907,-2.887981,1.837745,-4.691210,3.156672,8.490778,8.580933,-5.648660,4.698447,-0.785511,-0.273242,2.998067,-9.755706,9.154173,-3.241784,-3.556854,7.821005,-5.187813,-1.561738,-2.316284,-4.453847,6.246367,9.394929,1.157566,-5.981855,8.357055,7.208626,8.293368,3.467563,9.081164,-2.897612,2.920158,-8.556235,-9.987988,-5.675368,-3.857943,-2.238487,-4.597309,0.643411,5.686344,-7.247286,-1.156961,0.425764,7.724975,9.054470,3.376524,2.334531,4.799155,-8.967480,-0.356315,-8.133197,-2.955729,9.326801,2.265019,-9.620721,-1.730799,4.106686,-2.023551,-0.478744,8.850770,-8.251443,4.678618,6.989424,-1.383252,6.488959,-4.947400,1.523075,-4.009306,-5.338253,-9.823263,-5.959636,9.011674,5.096598,1.257478,7.371606,4.142554,3.440604,3.060638,6.223967,-5.270564,7.367937,8.518222,4.460314,8.596592,4.710598,1.884283,-5.488586,7.996138,-8.603557,-4.102816,-1.546509,-5.238146,-5.489088,-6.705724,0.771816,-1.484924,-8.557054,6.200396,-9.254885,7.250808,-5.161521,5.079576,8.335975,9.318816,9.128124,2.956349,0.842304,3.968712,-5.346734,-4.383598,0.428787,-6.420634,-3.959757,6.794174,-0.998321,-1.961539,9.666768,0.073747,-8.041827,6.601489,-2.648778,4.060362,-8.941924,-5.932751,6.301740,-9.021281,4.255157,-4.837290,-6.469763,-6.193214,-1.805766,-8.441328,8.756945,-6.360595,-5.300356,4.681751,-6.007899,-4.125518,-2.507723,7.480825,6.158597,-6.739265,-6.203331,-1.209153,-2.945002,1.396883,2.033451,8.933270,-1.575172,6.412400,2.061392,0.339067,0.967350,-8.742723,-1.281218,4.368125,9.543898,9.411821,-8.468935,-0.462447,-4.219396,7.705883,3.018924,-2.943435,-9.818130,-5.040972,2.410790,-9.194015,-3.335166,-5.011062,-9.311552,-3.069119,2.390149,-6.259109,-0.968769,-2.077399,-4.050429,-6.037561,-3.437077,3.691621,-0.679694,-2.819525,-8.875641,4.146853,0.249516,3.790458,4.412769,9.891448,8.271630,1.405699,3.216585,0.777689,0.253941,7.810473,-7.542230,6.565144,8.449882,-9.171765,-0.540533,-4.458469,9.896841,9.257653,8.620946,8.802794,-5.378684,-2.085251,8.820288,-9.838793,-8.694450,-0.576305,-0.435664,9.980440,-7.961495,5.479143,1.038654,-2.774851,-1.015237,-6.119382,7.201743,-6.335716,-7.578339,1.215727,-8.617804,-3.590493,7.497993,-7.533355,-2.003643,7.830669,2.182677,1.152255,-5.571089,-4.407479,-0.549542,8.146043,-7.250806,2.754721,-0.463214,-0.294712,-9.638886,6.870144,-9.442583,-0.487890,-9.554418,6.558027,-4.505493,-6.329088,-3.419729,3.045392,8.503244,-6.247722,0.685296,-2.652754,-3.971015,-4.179613,-8.644747,4.989238,2.568845,0.458505,9.514740,-1.360378,-4.457086,0.653428,8.648454,7.832481,2.200000,-0.580134,9.741991,-7.237283,-3.073113,4.607325,5.899620,2.732517,-1.104896,-0.707765,9.434483,4.057789,8.502059,-2.154528,-9.474182,-3.222572,-7.681729,-2.660518,3.181991,2.703354,5.345283,-0.428066,2.282692,-1.013638,9.470846,-5.336825,1.274327,-7.661376,-1.843768,4.598050,-0.071745,-7.846444,-3.385011,-3.118024,5.406222,4.800145,-1.955716,0.945143,5.507629,8.109833,-1.219999,5.199452,-2.761911,9.820835,6.900460,8.065862,-2.748741,-5.832190,-4.418131,-0.304888,-9.210917,-4.784613,-8.868788,6.462396,5.553103,-5.442899,-8.714162,2.624550,1.637461,6.886487,8.931848,-3.265848,-3.093448,9.787550,2.955139,-5.477755,6.653889,5.088692,1.754926,-8.948077,1.932780,-9.117110,-6.476495,-6.469965,-0.492676,-5.497520,-4.729590,2.298652,4.059226,9.923441,3.738701,1.020209,6.335293,-9.514812,9.715991,0.973495,4.922895,-6.305922,-1.542979,9.881660,-5.990120,-5.961714,-5.787884,4.746466,-0.304204,-1.309566,-4.816298,3.008174,-8.148550,-9.152445,-3.744228,9.572932,-1.337682,7.704158,-0.943077,5.917044,3.945346,-8.795565,-0.692572,5.472605,-2.755864,-6.265644,6.429264,-3.771082,7.348551,4.029017,2.475094,9.768183,-1.543511,-5.583880,6.970878,5.692073,5.478094,-7.678026,6.152992,7.331881,7.478874,2.949298,6.584762,4.820513,-1.874404,-2.725943,8.862212,0.236444,-8.778194,-4.164433,-4.211617,-0.070097,3.244362,8.907464,7.043882,2.120972,-1.219722,0.412867,-0.569068,-9.404901,-6.151814,-5.148847,-9.591767,6.426205,3.950295,-9.235720,-7.811189,-0.281452,0.949571,-7.331444,-4.477913,1.292244,-2.494353,-2.743321,4.330068,-8.751060,0.759060,4.808199,-7.160973,-6.373422,2.426531,0.317998,-0.524904,4.682137,1.868313,-8.512599,9.150001,-6.483424,-5.142712,4.144452,8.947758,5.035114,-7.553960,-1.076852,-8.905779,4.691742,7.423901,6.064262,-7.379934,3.917416,-5.340023,8.991256,-3.402837,-5.959585,-3.084506,-0.952538,9.526856,-0.433398,3.003256,-9.743428,9.015912,7.077839,6.823479,-3.586070,9.977261,1.366895,4.802593,-6.126374,4.367645,3.048920,-5.127055,5.165182,0.437849,1.353528,3.577794,-4.385428,4.092067,8.032521,-7.966192,-1.578201,-8.589435,-6.403262,-7.066703,9.311936,6.554289,7.022328,-6.603208,2.838175,-3.708469,-8.358209,-4.769769,6.445938,-1.595360,-1.940374,-5.252045,1.054418,5.912274,7.132834,-7.605032,8.612492,4.536057,7.344802,6.184845,3.310896,3.856957,5.024606,5.980721,-2.467962,-5.753635,-1.857619,4.472018,1.546894,9.447375,2.920051,7.264430,1.459546,7.599835,-3.701320,2.730077,6.715214,-4.677529,2.260810,3.024030,4.833021,-1.445550,-7.942538,7.708700,-2.716825,-0.345325,-1.042200,-9.336349,-6.329070,-8.226605,3.900702,7.317746,2.273048,1.918448,7.151713,-5.180115,-1.411365,-8.302338,-0.904428,-2.816377,9.155789,-7.821085,-7.168040,1.178603,1.805080,-2.011253,-3.638577,6.070102,9.999876,-4.049458,7.589289,0.662588,3.552955,-1.321171,-9.766959,0.305616,-2.482643,0.680919,-8.532608,3.815031,2.555961,-8.947991,0.963125,9.562626,1.335639,8.493538,-4.985103,-2.495478,5.852831,9.214170,-4.085187,9.065408,3.245949,2.392420,8.348970,1.865768,-9.652253,-3.392581,4.823765,-3.889837,2.603613,4.486245,5.466697,-4.969817,-5.164151,-8.500477,-8.119832,2.887693,-6.018269,7.061314,-1.534606,-7.171747,4.166268,-4.156047,-2.385476,1.792179,1.347660,4.430483,-6.123865,6.170033,-6.053094,6.028893,7.021854,-2.076682,-6.978683,1.417715,-5.932188,0.893246,9.610183,-4.589974,2.792354,4.958753,-1.470605,5.072348,-8.596036,7.223583,-3.224681,6.054876,-5.330779,1.414311,-5.153887,9.358783,8.641872,-6.684866,-7.679367,-2.679390,-2.749406,-2.519612,2.060049,0.810065,-8.768776,-6.607437,-6.588456,-8.439727,8.278105,6.238509,7.678022,-6.077658,2.344160,7.545315,2.942765,4.544325,4.228024,-1.310361,8.864770,9.524852,-3.462545,-9.576528,0.564628,3.051765,5.743961,-3.526045,6.129259,1.207427,4.910893,6.405538,-5.029501,-7.052198,-8.953867,-6.744806,4.830189,-4.798327,5.324249,-1.576837,0.893118,2.758627,-3.167752,5.496017,-5.543485,-5.643676,4.048244,-1.256425,9.831328,-2.294008,9.842845,1.306072,-6.255954,6.886721,6.221124,-1.925102,6.959831,5.234765,-8.177657,-1.156023,6.436262,-6.921034,-2.749839,-0.058161,-7.971479,1.706398,-5.612435,-6.470235,-2.369743,-9.884967,4.384314,8.289101,5.980617,-3.177417,1.818501,-4.620837,3.937477,-9.376121,-4.652212,9.720608,2.251037,-3.827027,-7.766751,-1.151422,-7.250313,-0.668780,7.902411,4.804753,-6.422144,-5.540117,-6.808569,-0.897357,-1.266762,3.487992,9.813034,4.983932,6.454552,-4.851296,-5.290852,4.732083,-3.558712,-7.072953,0.662298,-7.547603,6.228524,9.546276,3.225346,0.164494,-5.569869,-0.492219,-0.210206,-8.413707,-7.504833,5.080073,8.947307,9.809983,-0.852636,-9.353036,0.851314,5.452083,3.555736,-3.117412,-9.789690,-6.002659,-2.439315,-7.853620,-5.212681,5.819349,-3.167448,3.465458,9.344661,7.930388,-1.682251,8.637955,-6.980128,-5.709920,7.522577,-2.460494,4.550365,6.212358,-0.576346,-3.915708,-8.533836,5.480356,-9.267693,6.032846,6.532262,4.078713,-9.175119,-7.614771,7.293361,-0.092899,5.325361,-5.706448,-8.170338,5.833849,7.347235,1.342875,3.295313,-4.290900,-3.105197,0.762721,-8.290131,2.623711,8.579446,1.686857,6.609620,5.494316,4.221175,0.865484,9.385369,-0.392995,-0.130206,3.877126,-3.480261,7.252705,3.130970,-6.040105,3.701301,-4.566414,5.189524,9.998363,4.019385,-5.005459,-9.438186,-7.485910,-4.023736,-6.186366,1.202538,-9.981523,-7.696055,-5.148523,-1.695384,8.916926,-1.091098,-7.582341,-8.089395,-9.228613,-6.667308,-3.959507,-5.183732,1.135429,4.134200,0.158225], dtype = "float64")#candidate|15278|(1456,)|const|float64
call_15277 = func_3593_call(relay.reshape(const_15278.astype('float64'), [14, 8, 13]), relay.reshape(const_15278.astype('float64'), [14, 8, 13]), )
call_15279 = func_3593_call(relay.reshape(const_15278.astype('float64'), [14, 8, 13]), relay.reshape(const_15278.astype('float64'), [14, 8, 13]), )
output = relay.Tuple([call_15267,call_15277,const_15278,])
output2 = relay.Tuple([call_15268,call_15279,const_15278,])
func_15292 = relay.Function([], output)
mod['func_15292'] = func_15292
mod = relay.transform.InferType()(mod)
mutated_mod['func_15292'] = func_15292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15292_call = mutated_mod.get_global_var('func_15292')
call_15293 = func_15292_call()
output = call_15293
func_15294 = relay.Function([], output)
mutated_mod['func_15294'] = func_15294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12162_call = mod.get_global_var('func_12162')
func_12164_call = mutated_mod.get_global_var('func_12164')
call_15316 = func_12162_call()
call_15317 = func_12162_call()
output = call_15316
output2 = call_15317
func_15320 = relay.Function([], output)
mod['func_15320'] = func_15320
mod = relay.transform.InferType()(mod)
output = func_15320()
func_15321 = relay.Function([], output)
mutated_mod['func_15321'] = func_15321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8625_call = mod.get_global_var('func_8625')
func_8626_call = mutated_mod.get_global_var('func_8626')
call_15332 = relay.TupleGetItem(func_8625_call(), 0)
call_15333 = relay.TupleGetItem(func_8626_call(), 0)
func_6483_call = mod.get_global_var('func_6483')
func_6486_call = mutated_mod.get_global_var('func_6486')
const_15346 = relay.const([-5.370365,-3.725653,2.073935,-1.171324,-5.580406,-6.379382,7.242952,-5.570436], dtype = "float32")#candidate|15346|(8,)|const|float32
call_15345 = relay.TupleGetItem(func_6483_call(relay.reshape(const_15346.astype('float32'), [8,])), 0)
call_15347 = relay.TupleGetItem(func_6486_call(relay.reshape(const_15346.astype('float32'), [8,])), 0)
output = relay.Tuple([call_15332,call_15345,const_15346,])
output2 = relay.Tuple([call_15333,call_15347,const_15346,])
func_15364 = relay.Function([], output)
mod['func_15364'] = func_15364
mod = relay.transform.InferType()(mod)
mutated_mod['func_15364'] = func_15364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15364_call = mutated_mod.get_global_var('func_15364')
call_15365 = func_15364_call()
output = call_15365
func_15366 = relay.Function([], output)
mutated_mod['func_15366'] = func_15366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7646_call = mod.get_global_var('func_7646')
func_7647_call = mutated_mod.get_global_var('func_7647')
call_15384 = relay.TupleGetItem(func_7646_call(), 0)
call_15385 = relay.TupleGetItem(func_7647_call(), 0)
func_6790_call = mod.get_global_var('func_6790')
func_6792_call = mutated_mod.get_global_var('func_6792')
call_15391 = relay.TupleGetItem(func_6790_call(), 0)
call_15392 = relay.TupleGetItem(func_6792_call(), 0)
func_10802_call = mod.get_global_var('func_10802')
func_10804_call = mutated_mod.get_global_var('func_10804')
const_15396 = relay.const([6,2,4,-2,-4,-8,9,8,6,-9,2,1,-5,9,9,7,6,9,-1,-1,-7,-9,10,-4,5,9,7,-3,6,6,-4,3,10,-9,5,7,-6,-10,-6,-3,2,-10,1,3,-7,-3,2,10,9,5,9,10,10,6,-6,7,-10,-9,10,8,-1,-8,-8,4,-10,-3,-3,-8,3,-9,2,7,2,-3,-9,10,4,2,-8,9,-7,9,-5,3,1,-7,5,-7,1,9,-2,8,1,-8,-6,9,1,-3,6,-4,-7,2,-4,-1,10,3,-1,6,10,-2,-4,10,-2,-2,9,7,-9,-10,-1,-8,-10,-1,-3,-6,-2,3,-1,1,-6,-4,-1,2,4,-4,4,-4,-4,-9,1,-4,-4,-8,10,10,4,-2,5,-6,-10,3,-4,-8,9,7,-3,-4,-8,3,4,3,-9,3,-2,4,1,4,2,2,-9,3,2,10,10,7,9,9,6,2,3,8,1,9,-5,-5,2,8,-3,-3,2,-4,9,-6,7,4,2,-6,-3,-6,-6,5,-9,1,9,-5,-3,1,6,10,5,-5,-4,-10,6,7,7,1,5,7,5,7,5,-3,-5,-6,4,7,-4,9,3,5,10,-5,7,10,-8,-3,5,3,8,-10,3,-4,-2,-1,1,-4,-4,-7,-3,-7,4,-3,6,8,-7,10,-6,1,9,5,-9,-2,-8,-6,-4,9,10,6,7,-4,2,6,-10,8,-10,9,9,-2,8,7,10,-1,-7,-10,1,-1,-10,1,-6,9,-9,7,10,7,9,2,-10,-10,10,-3,4,1,5,-3,-10,-8,1,-9,7,8,7,-5,-5,-6,-7,-3,7,4,-8,4,9,7,9,10,-1,4,-10,-7,-8,-7,3,5,-6,3,-7,-1,1,6,-5,8,5,-6,-2,10,-7,4,-1,-10,-9,-10,-10,-5,-1,10,9,4,9,9,-4,-9,9,10,2,4,5,-2,-7,5,-1,-5,-3,4,-10,1,-3,-6,-6,10,-10,-1,-10,-1,1,-6,3,3,-2,-7,-10,-10,-1,-5,5,-6,2,10,-2,3,-7,8,-10,-5,5,-9,-2,-10,-3,1,10,3,-7,-8,-3,4,7,1,2,4,-10,4,9,-5,9,-2,-3,3,-7,-9,-9,4,7,-7,-3,-10,-1,-5,8,-5,-5,-6,-2,-10,-9,1,4,-5,-1,3,1,-7,6,3,1,3,-4,6,-7,5,7,-3,1,3,-10,4,-10,4,-2,-1,6,10,-2,-8,-3,4,-10,1,5,-3,-10,6,9,-7,-8,5,2,-8,10,-3,10,2,-4,-1,-7,-4,1,-9,2,1,-4,-8,2,9,1,-6,9,8,1,2,2,-8,-10,3,-3,-3,-3,-3,6,-6,6,-5,1,8,-1,-1,8,7,-8,-1,-7,10,-5,4,7,-6,3,7,5,8,-6,10,-10,-4,-9,9,-1,-5,-2,-8,10,-1,5,9,-1,-7,-5,3,-4,-4,-3,-9,2,1,-3,-2,-4,6,-10,1,-1,10,-5,-1,-1,-4,-6,1,4,-3,-4,2,7,-9,-2,-8,-1,8,3,-7,-2,1,1,-7,7,-4,4,-8,3,-10,10,-9,-8,6,-6,-6,-3,8,10,-3,-7,7,-2,-2,2,3,10,10,-10,-9,-1,-7,-1,-10,-2,7,9,-1,-7,-9,5,-1,-5,4,9,-2,-8,5,-5,10,6,-9,1,8,-2,-9,9,3,10,7,-3,-10,-1,-2,-9,-6,-2,-10,2,3,4,-1,1,-5,3,10,5,7,-2,10,3,-6,10,8,-5,6,-2,-2,-2,3,3,1,1,1,9,7,-9,7,-3,1,-7,-9,5,3,10,-3,9,-10,4,-8,-5,6,-9,3,-9,10,-3,-8,-10,-6,-9,5,2,2,5,10,-6,5,-1,-7,-7,10,-6,8,9,10,2,-10,9,2,-4,5,1,5,-10,-4,-1,-5,-3,5,-7,-2,8,-3,3,-2,-10,-7,7,-2,-4,4,-1,2,-3,7,-4,9,10,1,-9,-2,-8,-7,1,-3,-8,-2,-7,-4,-1,-10,-10,7,5,7,10,1,10,-4,1,-8,6,9,-4,4,4,2,-7,7,-6,-3,6,4,-6,-9,-8,8,-6,-7,-10,8,5,1,9,-3,2,3,2,4,-8,6,9,-9,-1,-7,-7,8,-5,3,6,-10,2,6,1,-5,-4,-4,-5,8,-1,-8,2,-2], dtype = "uint64")#candidate|15396|(832,)|const|uint64
call_15395 = relay.TupleGetItem(func_10802_call(relay.reshape(const_15396.astype('uint64'), [16, 4, 13])), 1)
call_15397 = relay.TupleGetItem(func_10804_call(relay.reshape(const_15396.astype('uint64'), [16, 4, 13])), 1)
func_13132_call = mod.get_global_var('func_13132')
func_13134_call = mutated_mod.get_global_var('func_13134')
call_15409 = func_13132_call()
call_15410 = func_13132_call()
output = relay.Tuple([call_15384,call_15391,call_15395,const_15396,call_15409,])
output2 = relay.Tuple([call_15385,call_15392,call_15397,const_15396,call_15410,])
func_15418 = relay.Function([], output)
mod['func_15418'] = func_15418
mod = relay.transform.InferType()(mod)
mutated_mod['func_15418'] = func_15418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15418_call = mutated_mod.get_global_var('func_15418')
call_15419 = func_15418_call()
output = call_15419
func_15420 = relay.Function([], output)
mutated_mod['func_15420'] = func_15420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6769_call = mod.get_global_var('func_6769')
func_6771_call = mutated_mod.get_global_var('func_6771')
call_15437 = func_6769_call()
call_15438 = func_6769_call()
output = relay.Tuple([call_15437,])
output2 = relay.Tuple([call_15438,])
func_15458 = relay.Function([], output)
mod['func_15458'] = func_15458
mod = relay.transform.InferType()(mod)
mutated_mod['func_15458'] = func_15458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15458_call = mutated_mod.get_global_var('func_15458')
call_15459 = func_15458_call()
output = call_15459
func_15460 = relay.Function([], output)
mutated_mod['func_15460'] = func_15460
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15465 = relay.var("var_15465", dtype = "float64", shape = (6, 10, 7))#candidate|15465|(6, 10, 7)|var|float64
uop_15466 = relay.asin(var_15465.astype('float64')) # shape=(6, 10, 7)
output = uop_15466
output2 = uop_15466
func_15474 = relay.Function([var_15465,], output)
mod['func_15474'] = func_15474
mod = relay.transform.InferType()(mod)
var_15475 = relay.var("var_15475", dtype = "float64", shape = (6, 10, 7))#candidate|15475|(6, 10, 7)|var|float64
output = func_15474(var_15475)
func_15476 = relay.Function([var_15475], output)
mutated_mod['func_15476'] = func_15476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8919_call = mod.get_global_var('func_8919')
func_8921_call = mutated_mod.get_global_var('func_8921')
call_15554 = relay.TupleGetItem(func_8919_call(), 0)
call_15555 = relay.TupleGetItem(func_8921_call(), 0)
output = call_15554
output2 = call_15555
func_15564 = relay.Function([], output)
mod['func_15564'] = func_15564
mod = relay.transform.InferType()(mod)
output = func_15564()
func_15565 = relay.Function([], output)
mutated_mod['func_15565'] = func_15565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15583 = relay.var("var_15583", dtype = "float64", shape = (12, 11, 14))#candidate|15583|(12, 11, 14)|var|float64
uop_15584 = relay.sigmoid(var_15583.astype('float64')) # shape=(12, 11, 14)
func_1180_call = mod.get_global_var('func_1180')
func_1184_call = mutated_mod.get_global_var('func_1184')
var_15587 = relay.var("var_15587", dtype = "uint64", shape = ())#candidate|15587|()|var|uint64
const_15588 = relay.const([False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,False], dtype = "bool")#candidate|15588|(1120,)|const|bool
call_15586 = relay.TupleGetItem(func_1180_call(relay.reshape(var_15587.astype('uint64'), []), relay.reshape(const_15588.astype('bool'), [14, 5, 16]), ), 1)
call_15589 = relay.TupleGetItem(func_1184_call(relay.reshape(var_15587.astype('uint64'), []), relay.reshape(const_15588.astype('bool'), [14, 5, 16]), ), 1)
func_5628_call = mod.get_global_var('func_5628')
func_5631_call = mutated_mod.get_global_var('func_5631')
const_15613 = relay.const([-1.132428,-4.663553,6.640012,-8.675301,9.661660,7.051729,4.441144,-0.632242,-9.096543,-8.473424,3.997602,-4.746661,4.962490,4.495454,7.852397,-0.621241,9.372441,9.408703,-4.177469,6.022120,-8.726236,-5.581325,0.704252,-2.049372,-6.182410,1.025555,-4.883625,-9.697234,7.104924,-9.514329,-3.459187,-8.849372,1.981582,-0.787650,7.117153,4.371614,0.019662,2.220867,-9.633286,-0.348304,-0.341024,-6.677658,-4.276581,9.512597,4.438191,-7.627892,-1.021244,4.712065,-4.985103,4.953427,1.939700,-3.546107,8.168341,1.877691,1.030423,-7.318026,7.913568,-2.900601,5.288761,2.246365,0.657766,-3.013707,-7.027100,-4.482615,-4.410125,1.567859,-1.341374,-0.168518,0.227953,-5.003207,4.850693,9.724701,7.015460,-6.186812,2.211865,1.767012,5.492086,-2.180574,1.855470,8.225425,5.974758,7.227139,-8.937192,7.570797,0.951444,-0.865968,-1.156002,1.359121,-9.977558,9.992581,0.225707,-8.094288,-8.270214,0.311888,6.883554,3.766515,8.285884,5.293115,-2.293355,7.588653,-1.310284,2.293289,0.683968,-8.273491,-9.418056,9.245603,5.577966,1.963125,5.082041,2.111181,8.235970,3.175428,-8.441344,-3.364194,4.312336,-0.299005,8.796578,-8.923968,8.964597,-6.183934,-0.827091,8.281373,-0.547209,-1.165477,2.958253,-3.768022,-1.074354,5.425415,-1.682167,-2.165235,-4.954046,5.450919,-9.744916,-8.371364,4.075785,8.798663,7.124877,9.161875,6.850543,0.998548,7.317605,9.784664,3.849588,-4.906904,-0.233846,9.102771,-6.108217,0.064988,-6.802320,-6.179321,-7.051113,-9.774331,-0.169217,4.750025,2.658202,4.186202,9.072488,-7.828739,5.556617,-1.611669,2.575845,-8.146776,4.062683,-8.352984,-2.375448,7.984577,6.848945,-8.121008,2.006969,2.137013,-7.681404,0.466754,-4.984824,-1.111127,2.233314,7.819187,-9.804883,-8.402796,8.990587,5.675093,1.253310,2.325643,-8.593719,-9.170249,7.901273,-5.120808,-9.263667,7.926789,-0.991144,1.079342,1.499994,-3.889511,-9.935887,7.156268,-6.426521,8.717354,3.254208,-7.266404,-0.345512,4.522309,-7.872633,5.031408,7.105053,2.071214,-4.647368,9.205962,-9.178988,0.303581,-5.418071,-3.767021,-4.410297,-3.528838,-7.201697,1.738018,-5.292649,7.586096,7.741670,4.806485,8.556626,-1.737686,2.138077,1.957919,5.041987,4.212588,8.314454,-8.387315,6.462182,9.865366,4.586152,9.427998,6.354465,0.876353,1.197424,-9.747168,2.783609,3.798425,-8.149075,-6.562768,9.236386,-2.446358,-8.667352,-0.115356,1.727540,2.344604,3.629747,-2.337381,0.734654,1.607908,8.633614,-0.448637,-9.657345,9.452805,-3.161486,-8.641875,3.218177,7.673674,-7.106247,-9.192305,1.058144,-4.398772,-0.238039,-4.088297,-1.515305,-9.440070,0.121566,0.151325,-6.808085,-0.437959,-3.358279,4.139016,4.361081,6.331343,-7.959663,-5.996186,-9.588570,-6.492010,8.310122,-8.049372,-4.330677,2.871398,9.063294,9.284184,-8.788920,8.222073,6.758807,-7.289692,2.698879,-5.868992,3.775819,0.118355,7.728780,-9.381122,-5.874054,7.790463,-5.442224,-7.219257,5.768317,1.075184,-5.139788,-3.977329,2.501174,-6.345261,7.968468,0.583020,5.344479,-0.165129,-8.903965,-8.188188,4.816082,-0.973801,-5.962887,-6.641791,-3.496667,9.163200,-1.545340,-4.376675,7.399152,-3.785885,4.226152,7.544397,-8.295238,-9.594767,3.108930,-4.049625,-4.242952,-6.964247,1.631065,-8.607731,-5.390521,-4.428060,0.549174,4.659185,-5.672258,9.740493,1.826577,-3.026336,-0.980716,-6.376425,2.775858,1.182183,0.753428,6.061597,-3.440831,8.570214,4.930005,6.114148,-0.488318,1.232430,-8.022234,7.746239,-9.454442,2.702178,-2.619730,-2.199217,-2.004600,6.008459,6.096377,3.107113,-3.478824,-4.992349,-4.082476,-7.025772,-1.238154,9.339337,7.102621,-1.824425,5.540697,-3.482996,-9.506152,3.305711,-4.124324,-7.236598,3.452672,8.290530,-1.455621,-7.022617,7.327198,-7.790700,-9.884718,-1.998656,-8.176951,0.066145,7.118728,9.465810,-8.594920,-7.719948,1.974751,-9.469312,-0.428049,-7.650278,-5.402413,-0.056055,3.178496,0.032462,-9.316376,1.213649,7.940065,-4.095835,1.813471,-3.642591,3.146404,-7.532827,1.814875,6.314534,4.456644,0.027871,-5.392056,8.509924,-1.208209,-4.644562,7.007531,8.388054,-0.965481,6.343266,4.634014,-4.843711,-5.951336,7.145806,8.860922,-5.195932,-5.004130,-5.803074,4.118602,-1.123932,0.095152,-4.974478,5.534234,9.275444,-9.464405,2.843508,-2.804302,-5.212411,-4.944974,-1.312620,-8.786540,-5.333043,-2.075090,-5.392298,5.820898,0.482256,7.102701,5.456492,3.797133,-5.025103,7.111328,8.751549,7.693867,-1.572974,5.555321,-8.555571,5.753289,-8.337858,6.839749,8.310074,-8.076204,9.924363,4.694808,-2.103331,3.389812,-4.497719,-6.488319,-8.884845,0.706830,0.533019,-8.539478,-0.028868,9.853559,6.070332,7.276699,9.986040,-6.362736,8.588435,3.241448,-4.571938,8.105096,6.139704,3.583562,2.044901,-9.013467,0.585067,-9.831016,7.123100,7.746807,9.028778,0.352583,-5.587532,8.168013,7.630998,5.950757,-8.098901,-8.517684,-6.493659,2.796918,-2.492067,-3.646876,-9.339646,-0.830528,-2.042454,9.223766,-0.795004,-3.803392,-5.152369,8.231240,-0.548230,4.117077,3.659699,-5.317737,5.506688,7.009157,-3.434908,-6.813955,6.775033,-0.514870,-9.007551,5.923921,-2.012170,4.904822,3.002118,2.466915,9.841595,-4.901444,-5.000828,-7.930534,4.588283,-3.579805,6.705022,-8.408785,0.299711,0.856275,-8.668464,-6.166068,-8.108198,8.884788,-9.624966,-5.240437,-3.452534,-9.826629,9.275210,-0.207928,4.752910,-7.196678,3.610941,3.597258,0.554417,-1.629838,7.117990,9.620229,-6.947069,0.386902,9.854477,-4.571198,4.290820,-8.174581,5.987011,2.606185,9.646104,-5.768020,-8.747732,8.047270,-5.875080,-7.698078,3.011470,8.666351,-2.366028,-2.218485,-3.761180,2.365433,-1.190881,5.669682,7.439833,-6.600367,-2.335872,4.992889,-3.830700,3.331906,6.667472,-8.957222,5.707709,-0.084713,-2.196103,5.039989,-8.290128,-2.750131,-4.619040,-3.442625,-5.017642,2.143808,8.030555,-2.892693,9.159142,-7.921709,8.469578,5.702199,9.743492,-7.286372,0.533742,-9.159909,6.709210,-8.614175,-1.738401,8.992692,8.832470,-4.281158,6.260108,-2.326309,-1.893600,6.130852,2.112828,-6.735097,6.260656,-1.715478,-5.794856,-9.475545,-3.506321,1.544245,2.017575,1.894564,9.658102,-1.639799,-4.979475,-5.543803,2.489885,-6.904912,-9.981256], dtype = "float32")#candidate|15613|(624,)|const|float32
const_15614 = relay.const([[False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False],[True,False,False,True,False,False,False,False,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True]], dtype = "bool")#candidate|15614|(2, 360)|const|bool
call_15612 = relay.TupleGetItem(func_5628_call(relay.reshape(const_15613.astype('float32'), [624,]), relay.reshape(const_15614.astype('bool'), [720,]), ), 2)
call_15615 = relay.TupleGetItem(func_5631_call(relay.reshape(const_15613.astype('float32'), [624,]), relay.reshape(const_15614.astype('bool'), [720,]), ), 2)
output = relay.Tuple([uop_15584,call_15586,var_15587,const_15588,call_15612,const_15613,const_15614,])
output2 = relay.Tuple([uop_15584,call_15589,var_15587,const_15588,call_15615,const_15613,const_15614,])
func_15620 = relay.Function([var_15583,var_15587,], output)
mod['func_15620'] = func_15620
mod = relay.transform.InferType()(mod)
mutated_mod['func_15620'] = func_15620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15620_call = mutated_mod.get_global_var('func_15620')
var_15622 = relay.var("var_15622", dtype = "float64", shape = (12, 11, 14))#candidate|15622|(12, 11, 14)|var|float64
var_15623 = relay.var("var_15623", dtype = "uint64", shape = ())#candidate|15623|()|var|uint64
call_15621 = func_15620_call(var_15622,var_15623,)
output = call_15621
func_15624 = relay.Function([var_15622,var_15623,], output)
mutated_mod['func_15624'] = func_15624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7497_call = mod.get_global_var('func_7497')
func_7499_call = mutated_mod.get_global_var('func_7499')
call_15639 = relay.TupleGetItem(func_7497_call(), 7)
call_15640 = relay.TupleGetItem(func_7499_call(), 7)
func_2250_call = mod.get_global_var('func_2250')
func_2254_call = mutated_mod.get_global_var('func_2254')
const_15685 = relay.const([[-8.259343],[8.306294],[-8.675432],[4.110457],[8.001771],[-0.725061],[5.275815],[-9.142535],[-1.123325],[-3.045749],[8.947903],[-1.321036],[-6.452604],[2.214576],[7.935769],[8.478767],[-3.917170],[-6.376219],[-1.530203],[-3.795931],[8.427063],[-3.226496],[-6.332877],[9.979455],[5.527109],[-0.084404],[5.455475],[2.386741],[-0.586235],[-0.190817],[5.591451],[-7.487186],[-0.632142],[7.870823],[-5.321087],[-0.807357],[-0.976205],[-5.009875],[0.798764],[8.996948],[-1.830969],[4.531898],[-8.394601],[2.704143],[2.601142],[4.613816],[8.992091],[7.285417],[-8.026925],[8.004068],[-1.863847],[-9.714962],[-2.516584],[0.529282],[9.694404],[-5.938158],[-5.099495],[3.282075],[-9.357176],[-4.662716],[-0.600155],[1.723093],[7.507409],[3.216439],[3.086442],[-5.961356],[-8.127865],[-7.100080],[2.540630],[-1.962596],[-3.256600],[-8.372123],[-6.247419],[-6.842134],[6.737525],[5.040983],[-5.721442],[0.756953],[2.707826],[9.030787],[3.600040],[-5.548091],[-0.688498],[-6.509859],[-3.559144],[-8.290636],[2.439351],[7.379939],[-6.977778],[5.063536],[-5.026562],[0.667678],[1.951673],[-9.571491],[6.218324],[8.742478],[0.027304],[-8.190908],[-4.318310],[-7.888612],[4.826041],[1.265630],[1.261455],[2.606632],[-8.839766],[3.486351],[3.720772],[8.977177],[-6.484881],[7.533704],[1.207309],[-9.166074],[-4.563546],[9.768551],[-2.103005],[0.156437],[-2.756695],[-1.240618],[4.034123],[-9.083114],[-1.351692],[6.808938],[-7.073609],[-3.651904],[-8.070794],[8.969351],[-9.911853],[1.818252],[-9.391489],[6.299233],[-9.183822],[5.574413],[-1.503028],[-1.689426],[9.572864],[8.090505],[6.200109],[9.176422],[-3.080408],[-0.802146],[7.464846],[-9.788913],[8.662695],[-8.531017],[-9.016369],[-7.959715],[-1.522191],[-0.364644],[-7.378357],[-7.110698],[0.231679],[8.409651],[-0.986217],[-1.244345],[1.092807],[-9.386514],[-3.211977],[-1.518041],[-4.065145],[-3.969109],[8.572275],[7.573399],[-6.170793],[-7.128472],[-8.133375],[-7.340740],[-2.543272],[-9.581264],[-4.196144],[8.349922],[4.056349],[-4.266651],[5.357917],[-3.139801],[5.279039],[-6.696339],[8.755706],[-0.988136],[2.537822],[-2.671475],[4.962984],[4.929582],[0.432286],[9.502010],[8.447891],[7.832029],[-5.234363],[-8.535239],[-4.586401],[4.448921],[5.955805],[-0.425460],[7.597853],[-1.195170],[3.421861],[-8.717532],[7.080461],[4.605778],[-5.385060],[-2.687285],[6.655476],[-5.932768],[9.409368],[2.666613],[4.186223],[8.367595],[0.914276],[-0.498967],[-3.865291],[1.319905],[3.615597],[9.485468],[-1.574690],[9.043717],[8.205057],[-4.720313],[1.729766],[-5.529263],[7.409057],[0.044914],[-6.760486],[-9.162704],[-0.432478],[-5.452214],[6.796803],[3.959292],[7.619692],[-0.899220],[7.531788],[-3.924754],[1.398762],[7.212266],[-2.389248],[-9.579498],[-7.247491],[-3.949456],[-0.886405],[-7.189218],[2.311669],[-4.298167],[-0.591240],[-7.004122],[-4.162458],[0.513500],[-2.972212],[-5.560856],[-0.922821],[2.200763],[4.483073],[6.383816],[0.209717],[-1.171685],[-3.470663],[-3.103451],[9.334459],[-9.941992],[-4.889618],[2.462296],[7.184655],[-1.818640],[9.384885],[-2.065630],[0.353598],[-6.029236],[8.391781],[-8.689455],[8.973738],[-6.761615],[7.253216],[-1.828230],[5.944594],[-1.502152],[3.880229],[-0.358173],[5.092972],[-8.946774],[5.222629],[-1.068871],[-1.940846],[3.548551],[-0.982836],[-9.253408],[-0.002295],[0.452171],[-5.963245],[-9.469104],[5.029478],[5.144531],[6.976273],[6.702759],[4.553965],[3.519043],[-3.254977],[3.871583],[-6.404989],[-8.441949],[-4.463148],[-8.029910],[-8.019177],[-9.529046],[4.758640],[-7.332455],[9.387822],[0.935950],[-9.139529],[6.649864],[8.142239],[-2.946962],[6.034929],[-7.966996],[2.600552],[-1.564986],[-8.199736],[-6.274941],[3.420094],[2.745608],[-1.976274],[3.925528],[0.950119],[-3.147494],[9.241329],[3.788423],[-3.276921],[9.710607],[7.705433],[9.781361],[-6.792328],[-1.134165],[-8.838364],[4.194823],[2.351943],[0.650516],[8.565604],[-6.574807],[1.093491],[-9.572883],[-6.440812],[8.786187],[9.460980],[-0.993617],[1.329221],[6.135795],[-3.608780],[-3.075921],[3.885733],[-6.831002],[-2.927595],[-7.815752],[-2.468881],[-9.852001],[0.231397],[-0.624243],[8.294257],[-9.075928],[-1.009731],[0.259358],[-4.083093],[-2.900013],[2.883420],[2.111960],[-9.004036],[3.168134],[0.519062],[-6.952774],[-8.943015],[-5.758906],[6.184664],[-2.030613],[-3.141927],[-3.431681],[1.199805],[-9.166979],[-7.162112],[-2.063485],[2.045126],[-4.638604],[4.882857],[-3.921575],[7.700405],[-1.060536],[-1.646725],[7.593596],[-1.845570],[-7.295180],[-4.347463],[2.324856],[-2.446537],[4.948310],[-4.988948],[-4.638286],[-9.270668],[-6.552990],[6.094189],[-0.478785],[7.786997],[-2.358908],[2.909371],[-6.392350],[4.876477],[5.721125],[3.344222],[-8.850179],[-4.256243],[-0.025247],[0.644159],[7.359134],[-5.457548],[-0.276337],[-2.713356],[-5.422449],[8.797639],[4.271362],[6.311881],[-2.735862],[-9.370286],[-3.349791],[4.526026],[-3.800527],[4.380713],[-0.187682],[5.219354],[-0.860954],[5.930153],[0.264068],[0.722466],[-2.050983],[7.226960],[-7.862297],[0.392280],[6.343327],[-1.970022],[6.240901],[-3.777026],[6.640264],[-6.386853],[5.233452],[7.001771],[4.185034],[-4.487236],[1.708976],[8.695655],[-5.609553],[5.468850],[9.621263],[-8.587476],[3.649674],[-7.095845],[-0.724041],[-0.210055],[-8.813985],[6.061699],[-6.215701],[8.341916],[-4.483377],[9.712893],[-8.452134],[6.893224],[5.758652],[0.513488],[9.522957],[0.366954],[-6.606001],[8.612569],[5.540757],[-8.522304],[-8.392798],[0.686422],[9.644094],[4.643651],[-1.099890],[7.167531],[7.966735],[2.602737],[3.501279],[8.025848],[-7.418649],[2.843088],[-3.379916],[4.874216],[-9.550327],[-2.889919],[-1.488303],[-1.767335],[-6.109770],[5.976348],[-4.412352],[8.823828],[9.676153],[-1.457625],[2.530391],[7.830541],[-7.443304],[-2.040209],[5.867961],[-1.622725],[-9.648957],[-8.597766],[-1.737561],[-6.785285],[-5.906960],[5.926728],[-2.429521],[-9.542758],[-4.733417],[-3.555311],[-0.358416],[1.637973],[9.418097],[-4.565041],[-6.316084],[-7.838226],[0.348832],[0.677940],[5.253194],[-1.526508],[8.869949],[-1.143909],[4.397294],[4.658891],[6.640729],[9.206270],[8.889929],[5.785821],[9.073321],[4.484871],[-1.429205],[-2.503532],[-9.061999]], dtype = "float64")#candidate|15685|(528, 1)|const|float64
const_15686 = relay.const([-6.403683,-5.823545,9.927468,2.742367,7.878148,9.094557,-6.623822,4.185205,-9.046146,0.554415,8.669168,-7.306377,1.998120,5.005087,1.081000,1.705769,4.254865,1.528777,6.428586,2.329880,-0.936041,0.335249,8.663171,-1.611651,2.934325,5.845398,5.816386,-9.384883,-0.184350,7.981054,6.347080,5.696994,-3.213119,-7.362253,-4.136220,-9.681411,-0.494572,3.213733,0.124809,7.769098,9.429570,8.666100,-9.245754,7.769467,4.312610,-6.713692,2.289295,1.348937,0.561656,5.367548,-7.418032,-7.106893,3.035377,-0.996318,7.706835,4.972161,-4.378111,1.107210,-0.605574,6.805209,6.521509,7.855443,-2.290621,-8.265693,-6.243753,1.094366,8.934768,4.419186,6.788911,6.945014,3.410881,4.983472,2.318125,-9.627834,4.112954,-4.857300,0.574204,7.298098,-3.838414,9.491190,4.983917,7.101358,-0.167108,8.773328,9.064772,-5.239618,3.855507,-9.173547,-7.346761,-1.128385,1.988581,-3.707953,-7.343407,-6.338403,9.662804,2.585326,-8.058982,-7.585463,7.926087,-6.073172,-1.252679,3.707933,-7.234287,1.815314,-7.308748,-4.041466,-1.785166,6.724325,-5.353868,1.570044,6.000999,-4.097959,-3.927919,3.618207,-7.543064,-9.499460,-2.043383,-1.371282,7.920958,-0.364438,2.333057,0.660064,6.962054,1.312876,-3.943207,-3.935557,9.879136,8.136763,3.383611,-2.920417,-2.267785,-5.679763,-3.763652,6.845362,-3.036075,-1.480078,-5.097556,0.030288,-3.294501,8.125717,-5.190691,-8.260553,-0.709018,5.008602,-0.722233,9.035263,-6.123154,-7.269787,-1.219338,-6.330101,4.506458,8.479463,2.584668,2.507907,9.038249,-2.207083,-5.138676,0.396022,8.491481,-3.106311,-9.038181,-4.660580,-9.486877,-3.214616,7.544410,8.070973,4.053364,-5.279396,-8.490057,-8.477278,1.743518,2.014687,9.387716,-7.101750,1.993726,7.652600,0.019915,-2.478742,-7.869152,-4.135874,0.284994,-3.083440,-3.217233,0.559694,-2.700142,-9.735805,1.150812,-5.164586,4.394854,5.232768,4.309979,-3.386934,-7.893820,-1.046627,4.081099,-1.306385,8.202405,8.372532,-9.661894,-1.703049,-8.776360,-5.861369,-2.072877,2.858795,8.898091,-7.597690,3.498960,5.466692,2.928437,-7.398448,6.839424,7.163203,9.794779,-0.048569,-6.829277,-8.942692,-1.129676,-6.072369,7.629996,-0.561635,-0.503256,-4.962767,5.975445,2.189213,2.449886,-5.042128,9.057404,7.001631,-0.398162,-3.620776,-1.163066,-2.374863,9.463060,6.423765,-6.826890,0.732837,-7.756510,-9.123435,-7.437307,-4.768258,3.798675,-3.288225,3.948838,5.675183,3.112610,-3.177250,-1.207610,-8.487180,5.673125,6.878567,5.461628,-2.083310,-0.180240,-7.479211,-0.202263,-0.371466,5.266488,-7.859792,7.671471,-1.894604,9.815994,-8.625019,8.147384,6.860798,6.949663,-2.036424,-7.074970,-6.904828,2.789672,9.078481,-3.036243,2.735130,-3.346582,-1.433120,4.777175,-8.868844,9.179258,2.015797,-4.921905,0.023729,7.391583,-0.047319,-2.469103,-1.622408,9.941496,6.258071,3.964100,6.928424,5.452011,3.254959,0.612634,5.459503,0.927840,3.331710,-1.824218,0.043488,8.871912,1.009069,-5.781783,6.834183,4.328891,7.781147,-8.951769,-2.718059,-4.230564,-1.325860,8.088365,-5.374916,-5.133865,-2.005165,-9.341562,-9.640522,-9.754712,6.060783,6.630053,-6.512577,-8.528571,-0.238537,3.996449,-3.595363,-2.502680,5.717354,-3.948926,-7.281342,3.128639,8.599375,-9.963017,7.383876,3.081294,-2.331243,-5.260983,9.455672,-7.465427,7.958810,-6.707577,-3.029784,-9.379098,4.830462,1.179573,-9.201425,-7.102134,7.772977,1.304711,2.285851,7.336310,-9.958635,0.070351,-1.281199,5.816260,8.090383,2.798913,-0.624226,8.780001,4.860277,-6.693449,4.627475,7.247263,4.069957,-6.637317,-1.735468,-6.900765,6.658411,-6.324103,-2.197078,3.971938,-5.525237,1.152637,-7.838370,-0.779983,1.330216,3.675082,0.514510,1.233292,-3.199847,-1.027855,-5.305935,1.628556,-2.928450,5.916733,9.615708,-8.612731,-6.356270,-0.292131,-1.724072,-3.237710,5.259530,-8.200294,-3.732917,-8.533334,7.567430,3.555539,7.342085,3.430667,2.406781,-8.986744,9.845303,-1.932498,-1.168045,8.770459,4.898898,8.168735,4.373568,2.368493,7.946347,-1.168290,-1.361042,-0.108026,-1.918483,4.634715,0.041761,-5.553512,-1.686284,-4.047715,-1.243767,4.883806,7.792873,-1.306847,4.412981,-8.457954,7.723432,6.800666,0.097027,-8.453794,-4.369584,9.222936,3.592339,-5.127936,-6.676954,6.136801,-7.696224,-8.113875,2.747660,9.997158,-2.113984,6.294671,-9.559589,-3.507076,4.839404,-6.012476,-1.238015,9.647224,5.662071,-5.884848,-7.692357,-9.542246,-7.139587,-3.759378,-6.997039,-9.388462,0.710580,-9.700509,9.462838,2.680181,3.240204,-9.042769,1.672950,-5.784948,0.592946,-2.132392,-9.733943,2.962431,4.929593,-2.384636,3.616822,3.920405,-7.558624,-3.983595,-2.866676,-2.039293,4.083857,4.528925,-9.164706,-7.866271,-0.160930,1.924626,5.911432,-3.424357,-8.116378,-6.370214,6.237671,4.621889,-9.995345,2.353504,5.653675,-9.580534,-2.816455,-5.888788,7.592345,5.317190,2.483083,-1.134488,4.722769,-8.784857,5.612436,9.692372,-5.633586,2.639907,-2.241771,6.535156,-4.513506,8.705637,7.499963,-8.424821,-3.531440,6.318129,-6.222923,-4.654249,-2.642716,-0.104912,-4.559939,-1.818832,-0.024192,8.881106,3.613312,-2.192266,-4.747139,-7.831436,6.361487,1.459394,-5.056874,-1.689668,-9.747742,-0.626769,4.156647,1.438346,-7.085659,-8.409763,3.200937,-9.049060,-7.082481,-7.299956,-7.236800,-2.720935,1.942726,1.911220,-7.306036,4.015177,-9.201153,9.243501,-1.747401,1.113479,0.336739,8.489355,1.687797,0.163608,-2.135836,2.758858,-0.289600,7.491908,4.537971,-2.076903,-5.929364,-3.992406,9.652914,-6.454975,-3.349194,8.983429,1.986017,-7.847186,-8.913659,-6.258364,-6.420044,8.694657,3.433893,-2.078274,6.516937,0.033859,-6.619029,-2.248147,6.205194,2.849540,2.442658,1.323616,8.555034,9.317412,4.483850,9.995113,8.314261,3.971107,2.287525,8.941722,-7.625554,-8.441032,6.059957,-8.900835,1.796822,-4.141733,-6.275893,6.490500,-0.218815,9.135394,-4.968003,1.000403,2.289805,-2.237870,-2.105088,7.938209,-1.205721,-6.333989,9.388235,8.634815,-2.694535,6.156934,0.971304,4.105826,5.818583,-5.738118,5.491701,-3.464010,-9.064906,9.348826,-4.823950,4.136307,-6.086145,-9.355427,-8.745393,-3.341100,-6.889969,-5.347104,-4.820304,3.531331,-2.578414,5.583134,5.427611], dtype = "float32")#candidate|15686|(624,)|const|float32
call_15684 = relay.TupleGetItem(func_2250_call(relay.reshape(const_15685.astype('float64'), [11, 3, 16]), relay.reshape(const_15685.astype('float64'), [11, 3, 16]), relay.reshape(const_15686.astype('float32'), [624,]), ), 0)
call_15687 = relay.TupleGetItem(func_2254_call(relay.reshape(const_15685.astype('float64'), [11, 3, 16]), relay.reshape(const_15685.astype('float64'), [11, 3, 16]), relay.reshape(const_15686.astype('float32'), [624,]), ), 0)
func_12097_call = mod.get_global_var('func_12097')
func_12099_call = mutated_mod.get_global_var('func_12099')
call_15704 = relay.TupleGetItem(func_12097_call(), 0)
call_15705 = relay.TupleGetItem(func_12099_call(), 0)
output = relay.Tuple([call_15639,call_15684,const_15685,const_15686,call_15704,])
output2 = relay.Tuple([call_15640,call_15687,const_15685,const_15686,call_15705,])
func_15713 = relay.Function([], output)
mod['func_15713'] = func_15713
mod = relay.transform.InferType()(mod)
output = func_15713()
func_15714 = relay.Function([], output)
mutated_mod['func_15714'] = func_15714
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15715 = relay.var("var_15715", dtype = "uint16", shape = (4, 4, 1))#candidate|15715|(4, 4, 1)|var|uint16
const_15716 = relay.const([[[5,5,-3,7,-9,-3,1,-6],[-2,9,-9,-6,4,-8,3,7],[8,-2,-10,-4,-7,3,1,-10],[-6,-4,3,-2,8,-2,-5,-7]],[[-10,7,-7,10,10,-3,-3,-5],[-9,5,-3,-1,-8,1,3,-10],[8,-4,8,10,-7,10,-3,2],[8,-6,-8,-1,3,2,2,10]],[[7,7,-9,-7,8,-10,-4,7],[-2,2,-1,4,7,-1,-8,-10],[-6,-2,4,3,7,-4,-6,3],[-3,5,2,-9,7,-9,-10,2]],[[6,9,5,1,-5,-5,4,-8],[4,3,5,4,-10,9,-2,4],[-4,7,8,1,2,4,-5,5],[8,-7,9,-6,-6,1,-5,7]]], dtype = "uint16")#candidate|15716|(4, 4, 8)|const|uint16
bop_15717 = relay.logical_xor(var_15715.astype('uint16'), const_15716.astype('uint16')) # shape=(4, 4, 8)
uop_15733 = relay.log(var_15715.astype('float32')) # shape=(4, 4, 1)
func_13650_call = mod.get_global_var('func_13650')
func_13652_call = mutated_mod.get_global_var('func_13652')
var_15736 = relay.var("var_15736", dtype = "float32", shape = (180,))#candidate|15736|(180,)|var|float32
call_15735 = relay.TupleGetItem(func_13650_call(relay.reshape(var_15736.astype('float32'), [180,])), 4)
call_15737 = relay.TupleGetItem(func_13652_call(relay.reshape(var_15736.astype('float32'), [180,])), 4)
func_13568_call = mod.get_global_var('func_13568')
func_13570_call = mutated_mod.get_global_var('func_13570')
call_15741 = func_13568_call()
call_15742 = func_13568_call()
func_8966_call = mod.get_global_var('func_8966')
func_8968_call = mutated_mod.get_global_var('func_8968')
call_15747 = func_8966_call()
call_15748 = func_8966_call()
output = relay.Tuple([bop_15717,uop_15733,call_15735,var_15736,call_15741,call_15747,])
output2 = relay.Tuple([bop_15717,uop_15733,call_15737,var_15736,call_15742,call_15748,])
func_15757 = relay.Function([var_15715,var_15736,], output)
mod['func_15757'] = func_15757
mod = relay.transform.InferType()(mod)
mutated_mod['func_15757'] = func_15757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15757_call = mutated_mod.get_global_var('func_15757')
var_15759 = relay.var("var_15759", dtype = "uint16", shape = (4, 4, 1))#candidate|15759|(4, 4, 1)|var|uint16
var_15760 = relay.var("var_15760", dtype = "float32", shape = (180,))#candidate|15760|(180,)|var|float32
call_15758 = func_15757_call(var_15759,var_15760,)
output = call_15758
func_15761 = relay.Function([var_15759,var_15760,], output)
mutated_mod['func_15761'] = func_15761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7646_call = mod.get_global_var('func_7646')
func_7647_call = mutated_mod.get_global_var('func_7647')
call_15844 = relay.TupleGetItem(func_7646_call(), 1)
call_15845 = relay.TupleGetItem(func_7647_call(), 1)
func_12661_call = mod.get_global_var('func_12661')
func_12662_call = mutated_mod.get_global_var('func_12662')
call_15848 = func_12661_call()
call_15849 = func_12661_call()
func_12798_call = mod.get_global_var('func_12798')
func_12802_call = mutated_mod.get_global_var('func_12802')
const_15858 = relay.const(False, dtype = "bool")#candidate|15858|()|const|bool
var_15859 = relay.var("var_15859", dtype = "bool", shape = (720,))#candidate|15859|(720,)|var|bool
call_15857 = func_12798_call(relay.reshape(const_15858.astype('bool'), []), relay.reshape(var_15859.astype('bool'), [8, 9, 10]), )
call_15860 = func_12798_call(relay.reshape(const_15858.astype('bool'), []), relay.reshape(var_15859.astype('bool'), [8, 9, 10]), )
func_13568_call = mod.get_global_var('func_13568')
func_13570_call = mutated_mod.get_global_var('func_13570')
call_15866 = func_13568_call()
call_15867 = func_13568_call()
output = relay.Tuple([call_15844,call_15848,call_15857,const_15858,var_15859,call_15866,])
output2 = relay.Tuple([call_15845,call_15849,call_15860,const_15858,var_15859,call_15867,])
func_15870 = relay.Function([var_15859,], output)
mod['func_15870'] = func_15870
mod = relay.transform.InferType()(mod)
mutated_mod['func_15870'] = func_15870
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15871 = relay.var("var_15871", dtype = "bool", shape = (720,))#candidate|15871|(720,)|var|bool
func_15870_call = mutated_mod.get_global_var('func_15870')
call_15872 = func_15870_call(var_15871)
output = call_15872
func_15873 = relay.Function([var_15871], output)
mutated_mod['func_15873'] = func_15873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5993_call = mod.get_global_var('func_5993')
func_5995_call = mutated_mod.get_global_var('func_5995')
call_15943 = relay.TupleGetItem(func_5993_call(), 0)
call_15944 = relay.TupleGetItem(func_5995_call(), 0)
output = relay.Tuple([call_15943,])
output2 = relay.Tuple([call_15944,])
func_15951 = relay.Function([], output)
mod['func_15951'] = func_15951
mod = relay.transform.InferType()(mod)
output = func_15951()
func_15952 = relay.Function([], output)
mutated_mod['func_15952'] = func_15952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8000_call = mod.get_global_var('func_8000')
func_8002_call = mutated_mod.get_global_var('func_8002')
call_15984 = relay.TupleGetItem(func_8000_call(), 0)
call_15985 = relay.TupleGetItem(func_8002_call(), 0)
func_15320_call = mod.get_global_var('func_15320')
func_15321_call = mutated_mod.get_global_var('func_15321')
call_15997 = func_15320_call()
call_15998 = func_15320_call()
func_12230_call = mod.get_global_var('func_12230')
func_12234_call = mutated_mod.get_global_var('func_12234')
var_16000 = relay.var("var_16000", dtype = "uint64", shape = ())#candidate|16000|()|var|uint64
var_16001 = relay.var("var_16001", dtype = "float32", shape = (180,))#candidate|16001|(180,)|var|float32
call_15999 = relay.TupleGetItem(func_12230_call(relay.reshape(var_16000.astype('uint64'), []), relay.reshape(var_16001.astype('float32'), [180,]), ), 4)
call_16002 = relay.TupleGetItem(func_12234_call(relay.reshape(var_16000.astype('uint64'), []), relay.reshape(var_16001.astype('float32'), [180,]), ), 4)
output = relay.Tuple([call_15984,call_15997,call_15999,var_16000,var_16001,])
output2 = relay.Tuple([call_15985,call_15998,call_16002,var_16000,var_16001,])
func_16013 = relay.Function([var_16000,var_16001,], output)
mod['func_16013'] = func_16013
mod = relay.transform.InferType()(mod)
mutated_mod['func_16013'] = func_16013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16013_call = mutated_mod.get_global_var('func_16013')
var_16015 = relay.var("var_16015", dtype = "uint64", shape = ())#candidate|16015|()|var|uint64
var_16016 = relay.var("var_16016", dtype = "float32", shape = (180,))#candidate|16016|(180,)|var|float32
call_16014 = func_16013_call(var_16015,var_16016,)
output = call_16014
func_16017 = relay.Function([var_16015,var_16016,], output)
mutated_mod['func_16017'] = func_16017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10413_call = mod.get_global_var('func_10413')
func_10414_call = mutated_mod.get_global_var('func_10414')
call_16152 = relay.TupleGetItem(func_10413_call(), 0)
call_16153 = relay.TupleGetItem(func_10414_call(), 0)
output = relay.Tuple([call_16152,])
output2 = relay.Tuple([call_16153,])
func_16193 = relay.Function([], output)
mod['func_16193'] = func_16193
mod = relay.transform.InferType()(mod)
mutated_mod['func_16193'] = func_16193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16193_call = mutated_mod.get_global_var('func_16193')
call_16194 = func_16193_call()
output = call_16194
func_16195 = relay.Function([], output)
mutated_mod['func_16195'] = func_16195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14148_call = mod.get_global_var('func_14148')
func_14149_call = mutated_mod.get_global_var('func_14149')
call_16224 = relay.TupleGetItem(func_14148_call(), 0)
call_16225 = relay.TupleGetItem(func_14149_call(), 0)
func_11812_call = mod.get_global_var('func_11812')
func_11813_call = mutated_mod.get_global_var('func_11813')
call_16233 = relay.TupleGetItem(func_11812_call(), 0)
call_16234 = relay.TupleGetItem(func_11813_call(), 0)
output = relay.Tuple([call_16224,call_16233,])
output2 = relay.Tuple([call_16225,call_16234,])
func_16235 = relay.Function([], output)
mod['func_16235'] = func_16235
mod = relay.transform.InferType()(mod)
mutated_mod['func_16235'] = func_16235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16235_call = mutated_mod.get_global_var('func_16235')
call_16236 = func_16235_call()
output = call_16236
func_16237 = relay.Function([], output)
mutated_mod['func_16237'] = func_16237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14561_call = mod.get_global_var('func_14561')
func_14563_call = mutated_mod.get_global_var('func_14563')
call_16248 = relay.TupleGetItem(func_14561_call(), 0)
call_16249 = relay.TupleGetItem(func_14563_call(), 0)
func_8258_call = mod.get_global_var('func_8258')
func_8259_call = mutated_mod.get_global_var('func_8259')
call_16266 = relay.TupleGetItem(func_8258_call(), 2)
call_16267 = relay.TupleGetItem(func_8259_call(), 2)
output = relay.Tuple([call_16248,call_16266,])
output2 = relay.Tuple([call_16249,call_16267,])
func_16273 = relay.Function([], output)
mod['func_16273'] = func_16273
mod = relay.transform.InferType()(mod)
mutated_mod['func_16273'] = func_16273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16273_call = mutated_mod.get_global_var('func_16273')
call_16274 = func_16273_call()
output = call_16274
func_16275 = relay.Function([], output)
mutated_mod['func_16275'] = func_16275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15418_call = mod.get_global_var('func_15418')
func_15420_call = mutated_mod.get_global_var('func_15420')
call_16404 = relay.TupleGetItem(func_15418_call(), 2)
call_16405 = relay.TupleGetItem(func_15420_call(), 2)
output = call_16404
output2 = call_16405
func_16406 = relay.Function([], output)
mod['func_16406'] = func_16406
mod = relay.transform.InferType()(mod)
mutated_mod['func_16406'] = func_16406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16406_call = mutated_mod.get_global_var('func_16406')
call_16407 = func_16406_call()
output = call_16407
func_16408 = relay.Function([], output)
mutated_mod['func_16408'] = func_16408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8371_call = mod.get_global_var('func_8371')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_16428 = func_8371_call()
call_16429 = func_8371_call()
output = relay.Tuple([call_16428,])
output2 = relay.Tuple([call_16429,])
func_16435 = relay.Function([], output)
mod['func_16435'] = func_16435
mod = relay.transform.InferType()(mod)
output = func_16435()
func_16436 = relay.Function([], output)
mutated_mod['func_16436'] = func_16436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12635_call = mod.get_global_var('func_12635')
func_12637_call = mutated_mod.get_global_var('func_12637')
call_16437 = func_12635_call()
call_16438 = func_12635_call()
func_13907_call = mod.get_global_var('func_13907')
func_13909_call = mutated_mod.get_global_var('func_13909')
call_16448 = relay.TupleGetItem(func_13907_call(), 0)
call_16449 = relay.TupleGetItem(func_13909_call(), 0)
func_9979_call = mod.get_global_var('func_9979')
func_9981_call = mutated_mod.get_global_var('func_9981')
call_16462 = relay.TupleGetItem(func_9979_call(), 0)
call_16463 = relay.TupleGetItem(func_9981_call(), 0)
output = relay.Tuple([call_16437,call_16448,call_16462,])
output2 = relay.Tuple([call_16438,call_16449,call_16463,])
func_16466 = relay.Function([], output)
mod['func_16466'] = func_16466
mod = relay.transform.InferType()(mod)
mutated_mod['func_16466'] = func_16466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16466_call = mutated_mod.get_global_var('func_16466')
call_16467 = func_16466_call()
output = call_16467
func_16468 = relay.Function([], output)
mutated_mod['func_16468'] = func_16468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12589_call = mod.get_global_var('func_12589')
func_12591_call = mutated_mod.get_global_var('func_12591')
call_16472 = func_12589_call()
call_16473 = func_12589_call()
func_13195_call = mod.get_global_var('func_13195')
func_13197_call = mutated_mod.get_global_var('func_13197')
call_16494 = func_13195_call()
call_16495 = func_13195_call()
output = relay.Tuple([call_16472,call_16494,])
output2 = relay.Tuple([call_16473,call_16495,])
func_16503 = relay.Function([], output)
mod['func_16503'] = func_16503
mod = relay.transform.InferType()(mod)
output = func_16503()
func_16504 = relay.Function([], output)
mutated_mod['func_16504'] = func_16504
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16511 = relay.var("var_16511", dtype = "float32", shape = (2, 4, 13))#candidate|16511|(2, 4, 13)|var|float32
uop_16512 = relay.rsqrt(var_16511.astype('float32')) # shape=(2, 4, 13)
func_9396_call = mod.get_global_var('func_9396')
func_9402_call = mutated_mod.get_global_var('func_9402')
var_16535 = relay.var("var_16535", dtype = "int8", shape = (1430,))#candidate|16535|(1430,)|var|int8
var_16536 = relay.var("var_16536", dtype = "int64", shape = (630,))#candidate|16536|(630,)|var|int64
const_16537 = relay.const([False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,True], dtype = "bool")#candidate|16537|(1120,)|const|bool
var_16538 = relay.var("var_16538", dtype = "float32", shape = (180,))#candidate|16538|(180,)|var|float32
call_16534 = relay.TupleGetItem(func_9396_call(relay.reshape(var_16535.astype('int8'), [11, 10, 13]), relay.reshape(var_16536.astype('int64'), [630,]), relay.reshape(const_16537.astype('bool'), [1120,]), relay.reshape(var_16538.astype('float32'), [180, 1]), ), 6)
call_16539 = relay.TupleGetItem(func_9402_call(relay.reshape(var_16535.astype('int8'), [11, 10, 13]), relay.reshape(var_16536.astype('int64'), [630,]), relay.reshape(const_16537.astype('bool'), [1120,]), relay.reshape(var_16538.astype('float32'), [180, 1]), ), 6)
uop_16542 = relay.atan(uop_16512.astype('float32')) # shape=(2, 4, 13)
func_11409_call = mod.get_global_var('func_11409')
func_11410_call = mutated_mod.get_global_var('func_11410')
call_16561 = func_11409_call()
call_16562 = func_11409_call()
output = relay.Tuple([call_16534,var_16535,var_16536,const_16537,var_16538,uop_16542,call_16561,])
output2 = relay.Tuple([call_16539,var_16535,var_16536,const_16537,var_16538,uop_16542,call_16562,])
func_16568 = relay.Function([var_16511,var_16535,var_16536,var_16538,], output)
mod['func_16568'] = func_16568
mod = relay.transform.InferType()(mod)
var_16569 = relay.var("var_16569", dtype = "float32", shape = (2, 4, 13))#candidate|16569|(2, 4, 13)|var|float32
var_16570 = relay.var("var_16570", dtype = "int8", shape = (1430,))#candidate|16570|(1430,)|var|int8
var_16571 = relay.var("var_16571", dtype = "int64", shape = (630,))#candidate|16571|(630,)|var|int64
var_16572 = relay.var("var_16572", dtype = "float32", shape = (180,))#candidate|16572|(180,)|var|float32
output = func_16568(var_16569,var_16570,var_16571,var_16572,)
func_16573 = relay.Function([var_16569,var_16570,var_16571,var_16572,], output)
mutated_mod['func_16573'] = func_16573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15458_call = mod.get_global_var('func_15458')
func_15460_call = mutated_mod.get_global_var('func_15460')
call_16781 = relay.TupleGetItem(func_15458_call(), 0)
call_16782 = relay.TupleGetItem(func_15460_call(), 0)
output = call_16781
output2 = call_16782
func_16788 = relay.Function([], output)
mod['func_16788'] = func_16788
mod = relay.transform.InferType()(mod)
output = func_16788()
func_16789 = relay.Function([], output)
mutated_mod['func_16789'] = func_16789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12518_call = mod.get_global_var('func_12518')
func_12519_call = mutated_mod.get_global_var('func_12519')
call_16811 = relay.TupleGetItem(func_12518_call(), 0)
call_16812 = relay.TupleGetItem(func_12519_call(), 0)
func_12635_call = mod.get_global_var('func_12635')
func_12637_call = mutated_mod.get_global_var('func_12637')
call_16818 = func_12635_call()
call_16819 = func_12635_call()
uop_16834 = relay.atanh(call_16818.astype('float64')) # shape=(15, 8, 15)
uop_16836 = relay.atanh(call_16819.astype('float64')) # shape=(15, 8, 15)
output = relay.Tuple([call_16811,uop_16834,])
output2 = relay.Tuple([call_16812,uop_16836,])
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
