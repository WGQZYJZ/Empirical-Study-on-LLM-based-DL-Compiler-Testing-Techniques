import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_71 = relay.var("var_71", dtype = "float32", shape = (4, 1, 6))#candidate|71|(4, 1, 6)|var|float32
uop_72 = relay.atan(var_71.astype('float32')) # shape=(4, 1, 6)
bop_82 = relay.add(uop_72.astype('int32'), relay.reshape(var_71.astype('int32'), relay.shape_of(uop_72))) # shape=(4, 1, 6)
uop_93 = relay.sqrt(uop_72.astype('float64')) # shape=(4, 1, 6)
bop_115 = relay.minimum(uop_93.astype('int8'), relay.reshape(var_71.astype('int8'), relay.shape_of(uop_93))) # shape=(4, 1, 6)
output = relay.Tuple([bop_82,bop_115,])
output2 = relay.Tuple([bop_82,bop_115,])
func_126 = relay.Function([var_71,], output)
mod['func_126'] = func_126
mod = relay.transform.InferType()(mod)
mutated_mod['func_126'] = func_126
mutated_mod = relay.transform.InferType()(mutated_mod)
var_127 = relay.var("var_127", dtype = "float32", shape = (4, 1, 6))#candidate|127|(4, 1, 6)|var|float32
func_126_call = mutated_mod.get_global_var('func_126')
call_128 = func_126_call(var_127)
output = call_128
func_129 = relay.Function([var_127], output)
mutated_mod['func_129'] = func_129
mutated_mod = relay.transform.InferType()(mutated_mod)
var_204 = relay.var("var_204", dtype = "float32", shape = (3, 13, 14))#candidate|204|(3, 13, 14)|var|float32
uop_205 = relay.rsqrt(var_204.astype('float32')) # shape=(3, 13, 14)
func_126_call = mod.get_global_var('func_126')
func_129_call = mutated_mod.get_global_var('func_129')
var_208 = relay.var("var_208", dtype = "float32", shape = (6, 4))#candidate|208|(6, 4)|var|float32
call_207 = relay.TupleGetItem(func_126_call(relay.reshape(var_208.astype('float32'), [4, 1, 6])), 1)
call_209 = relay.TupleGetItem(func_129_call(relay.reshape(var_208.astype('float32'), [4, 1, 6])), 1)
func_126_call = mod.get_global_var('func_126')
func_129_call = mutated_mod.get_global_var('func_129')
call_219 = relay.TupleGetItem(func_126_call(relay.reshape(call_207.astype('float32'), [4, 1, 6])), 1)
call_220 = relay.TupleGetItem(func_129_call(relay.reshape(call_207.astype('float32'), [4, 1, 6])), 1)
func_126_call = mod.get_global_var('func_126')
func_129_call = mutated_mod.get_global_var('func_129')
call_222 = relay.TupleGetItem(func_126_call(relay.reshape(var_208.astype('float32'), [4, 1, 6])), 0)
call_223 = relay.TupleGetItem(func_129_call(relay.reshape(var_208.astype('float32'), [4, 1, 6])), 0)
var_224 = relay.var("var_224", dtype = "int8", shape = (4, 8, 6))#candidate|224|(4, 8, 6)|var|int8
bop_225 = relay.mod(call_207.astype('float32'), var_224.astype('float32')) # shape=(4, 8, 6)
bop_228 = relay.mod(call_209.astype('float32'), var_224.astype('float32')) # shape=(4, 8, 6)
func_126_call = mod.get_global_var('func_126')
func_129_call = mutated_mod.get_global_var('func_129')
call_242 = relay.TupleGetItem(func_126_call(relay.reshape(call_219.astype('float32'), [4, 1, 6])), 1)
call_243 = relay.TupleGetItem(func_129_call(relay.reshape(call_219.astype('float32'), [4, 1, 6])), 1)
uop_245 = relay.log10(uop_205.astype('float64')) # shape=(3, 13, 14)
output = relay.Tuple([var_208,call_219,call_222,bop_225,call_242,uop_245,])
output2 = relay.Tuple([var_208,call_220,call_223,bop_228,call_243,uop_245,])
func_247 = relay.Function([var_204,var_208,var_224,], output)
mod['func_247'] = func_247
mod = relay.transform.InferType()(mod)
mutated_mod['func_247'] = func_247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_247_call = mutated_mod.get_global_var('func_247')
var_249 = relay.var("var_249", dtype = "float32", shape = (3, 13, 14))#candidate|249|(3, 13, 14)|var|float32
var_250 = relay.var("var_250", dtype = "float32", shape = (6, 4))#candidate|250|(6, 4)|var|float32
var_251 = relay.var("var_251", dtype = "int8", shape = (4, 8, 6))#candidate|251|(4, 8, 6)|var|int8
call_248 = func_247_call(var_249,var_250,var_251,)
output = call_248
func_252 = relay.Function([var_249,var_250,var_251,], output)
mutated_mod['func_252'] = func_252
mutated_mod = relay.transform.InferType()(mutated_mod)
var_757 = relay.var("var_757", dtype = "float64", shape = (16, 2, 3))#candidate|757|(16, 2, 3)|var|float64
uop_758 = relay.atanh(var_757.astype('float64')) # shape=(16, 2, 3)
func_247_call = mod.get_global_var('func_247')
func_252_call = mutated_mod.get_global_var('func_252')
var_790 = relay.var("var_790", dtype = "float32", shape = (546,))#candidate|790|(546,)|var|float32
var_791 = relay.var("var_791", dtype = "float32", shape = (12, 2))#candidate|791|(12, 2)|var|float32
var_792 = relay.var("var_792", dtype = "int8", shape = (192,))#candidate|792|(192,)|var|int8
call_789 = relay.TupleGetItem(func_247_call(relay.reshape(var_790.astype('float32'), [3, 13, 14]), relay.reshape(var_791.astype('float32'), [6, 4]), relay.reshape(var_792.astype('int8'), [4, 8, 6]), ), 3)
call_793 = relay.TupleGetItem(func_252_call(relay.reshape(var_790.astype('float32'), [3, 13, 14]), relay.reshape(var_791.astype('float32'), [6, 4]), relay.reshape(var_792.astype('int8'), [4, 8, 6]), ), 3)
func_247_call = mod.get_global_var('func_247')
func_252_call = mutated_mod.get_global_var('func_252')
call_812 = relay.TupleGetItem(func_247_call(relay.reshape(var_790.astype('float32'), [3, 13, 14]), relay.reshape(var_791.astype('float32'), [6, 4]), relay.reshape(var_792.astype('int8'), [4, 8, 6]), ), 0)
call_813 = relay.TupleGetItem(func_252_call(relay.reshape(var_790.astype('float32'), [3, 13, 14]), relay.reshape(var_791.astype('float32'), [6, 4]), relay.reshape(var_792.astype('int8'), [4, 8, 6]), ), 0)
output = relay.Tuple([uop_758,call_789,var_790,var_791,var_792,call_812,])
output2 = relay.Tuple([uop_758,call_793,var_790,var_791,var_792,call_813,])
func_842 = relay.Function([var_757,var_790,var_791,var_792,], output)
mod['func_842'] = func_842
mod = relay.transform.InferType()(mod)
mutated_mod['func_842'] = func_842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_842_call = mutated_mod.get_global_var('func_842')
var_844 = relay.var("var_844", dtype = "float64", shape = (16, 2, 3))#candidate|844|(16, 2, 3)|var|float64
var_845 = relay.var("var_845", dtype = "float32", shape = (546,))#candidate|845|(546,)|var|float32
var_846 = relay.var("var_846", dtype = "float32", shape = (12, 2))#candidate|846|(12, 2)|var|float32
var_847 = relay.var("var_847", dtype = "int8", shape = (192,))#candidate|847|(192,)|var|int8
call_843 = func_842_call(var_844,var_845,var_846,var_847,)
output = call_843
func_848 = relay.Function([var_844,var_845,var_846,var_847,], output)
mutated_mod['func_848'] = func_848
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1110 = relay.var("var_1110", dtype = "bool", shape = ())#candidate|1110|()|var|bool
const_1111 = relay.const([[True,True,False,False]], dtype = "bool")#candidate|1111|(1, 4)|const|bool
bop_1112 = relay.logical_and(var_1110.astype('bool'), const_1111.astype('bool')) # shape=(1, 4)
output = relay.Tuple([bop_1112,])
output2 = relay.Tuple([bop_1112,])
func_1118 = relay.Function([var_1110,], output)
mod['func_1118'] = func_1118
mod = relay.transform.InferType()(mod)
mutated_mod['func_1118'] = func_1118
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1119 = relay.var("var_1119", dtype = "bool", shape = ())#candidate|1119|()|var|bool
func_1118_call = mutated_mod.get_global_var('func_1118')
call_1120 = func_1118_call(var_1119)
output = call_1120
func_1121 = relay.Function([var_1119], output)
mutated_mod['func_1121'] = func_1121
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1222 = relay.const([[[9.263600,4.884834,8.007147,-4.210908,-2.912614,5.935059,0.725148,0.750335,0.581798,-8.170309,8.340260,4.398744,-9.251519],[-1.185351,-6.145782,-0.010167,0.350250,-8.764635,8.960431,-6.332300,-6.912986,2.645657,-7.042793,-4.704967,0.348889,2.087947],[7.773556,-7.763157,-7.353715,6.926747,-3.321180,-4.353819,-2.632700,-9.467443,-9.063051,3.359276,-2.327829,-5.617292,-8.758697],[-1.254943,3.531886,-3.235816,-4.933828,-0.308597,5.611852,-4.962253,-3.595047,5.035901,9.249947,-6.726119,5.216063,4.304561],[0.134795,-5.043986,-2.178754,3.265563,-2.085999,-6.428246,-8.413309,-2.263661,-8.015175,-7.310959,4.798541,5.428411,0.348110],[-8.791245,-2.455065,6.855988,9.393974,6.591851,-3.056886,1.279535,-0.123566,-5.271502,9.613971,-1.959862,5.263225,-4.285093],[-4.940753,1.993377,7.485338,-1.340962,3.965657,6.115861,1.479791,-8.221859,-9.723189,8.015403,2.421663,3.295742,-8.200515],[1.557763,-2.277881,-5.689327,8.826825,8.382676,-1.552365,-5.012619,1.164359,-3.351268,-7.413146,-0.816149,7.869903,2.531481],[0.445840,0.332765,-7.257749,4.721080,-4.552039,-5.955224,-9.865641,-1.194764,1.686057,-5.894047,9.743814,-8.860095,-8.272694],[-4.551650,-7.879316,-4.328116,-4.159688,7.997520,-2.129796,-2.873031,-1.649692,6.019761,-6.006909,8.955503,-9.512152,-7.481572]],[[7.892908,-6.659437,1.610848,8.647360,-3.496736,-1.235069,4.087541,-7.966581,-3.981533,-6.042291,1.700095,7.918842,4.749026],[3.602410,8.573347,2.499670,-8.728096,-9.678714,-2.692155,3.927179,5.020332,-1.862398,0.627860,4.261263,5.420957,0.740750],[3.807861,-8.793474,0.401651,-6.418297,6.887764,4.945700,5.068821,4.893614,5.720095,7.901586,-4.442875,0.337534,-3.394063],[-5.842983,-0.735509,-9.897489,-8.585907,4.276250,-9.987853,-0.232069,1.585250,-7.503363,4.812784,7.724002,-7.696615,-5.643538],[-3.835957,3.975382,-5.469998,-4.965482,2.033276,-4.322092,9.040664,9.740456,5.779211,3.313498,-3.937907,-5.568028,9.630664],[-9.088465,-6.639372,4.075075,9.702171,2.456615,-3.813168,-8.877474,-7.734581,6.355359,-4.782693,3.842594,4.174116,5.658439],[-1.904973,8.508482,5.526397,-1.617366,-8.483353,-4.184413,-2.189638,9.762018,7.951118,-6.309811,-6.911801,6.297921,-7.289913],[3.029176,6.632628,6.457720,-8.120951,8.224826,6.625930,3.206254,8.633324,9.267033,0.737476,-4.400187,-9.907273,-2.704471],[9.668551,-1.765201,-9.651005,7.146090,-9.467197,-3.678349,3.095265,-6.479228,0.272440,5.092905,3.358088,-0.726955,9.575212],[1.049561,4.210348,1.292289,6.316481,-1.662990,9.971280,6.741569,9.652133,-0.719504,5.157636,5.069045,-0.568521,-6.563956]],[[3.909402,-3.835139,9.751568,-7.050879,4.845232,6.946530,8.907163,-0.586411,8.212323,-2.396140,1.198023,-9.585699,1.252213],[1.348159,-0.685150,0.653385,-6.937156,-2.609863,7.838082,-3.592986,-5.613150,7.642840,-4.652380,-0.692078,7.300058,-4.095385],[4.545723,-5.913564,-8.275132,-2.735921,0.068331,-9.261549,4.718400,9.121154,0.385854,6.646716,-4.745803,-7.377493,0.719008],[-2.248457,7.787001,3.108081,9.813865,-5.353539,-5.586084,-5.156181,-9.081864,6.174075,-1.914831,9.957158,2.621486,1.072983],[1.091262,-4.046124,8.177621,-3.727912,8.696246,1.607319,5.154405,-3.459859,0.529639,1.871132,6.087804,5.293960,1.561811],[4.316178,-9.956416,-1.626373,-5.249978,-3.794287,-5.585038,9.086954,-3.068972,-5.763787,-0.526464,2.291450,-4.288838,7.179460],[-4.952965,0.918427,2.772114,-9.378285,0.620364,-0.934930,1.671113,6.309982,2.117771,6.225019,-2.759676,3.055001,-0.611132],[-8.588890,4.166221,-0.247108,-1.418073,9.599473,-8.772910,5.903908,6.895857,-2.746288,-7.775662,-1.345489,-3.096945,-3.424634],[8.816220,2.480082,-2.656117,-6.813085,7.731477,8.798492,-3.622978,-3.877541,-9.637092,5.745429,8.068681,-6.331914,0.422510],[5.520632,-6.302858,-8.508349,9.992034,3.627282,9.174965,1.571719,-5.992761,9.498434,8.490287,-4.925810,2.254195,4.308890]],[[2.598084,8.657531,-5.792274,-3.853836,-8.253101,7.113155,-0.115798,8.331841,-5.575298,-0.366730,-7.767524,-4.477532,1.022366],[6.396901,-7.133357,2.394163,9.144044,-0.350167,7.909051,-6.872056,-2.175762,0.281360,6.675487,-0.297427,0.779386,-8.067397],[-1.044051,-5.643052,8.148912,9.033009,-3.235908,2.095871,8.527431,-5.128344,-7.059320,-8.619992,-7.613978,8.545973,-3.839483],[7.067530,2.983536,8.409404,-2.542335,3.926386,-8.842881,6.190096,-8.263901,-0.142767,2.015290,-7.549799,1.678286,-2.294583],[8.738379,6.853867,4.500042,4.968611,4.983842,1.427941,-5.012163,3.344957,2.914257,-0.308894,-2.543975,6.789276,9.891926],[2.104273,-7.877030,-5.669047,-0.054721,0.959316,-9.388937,-3.705813,-2.647207,-7.829110,-0.175788,2.440459,-4.978184,1.722500],[-2.077574,-1.611433,6.004423,-8.990400,9.244882,4.240568,9.959508,-9.581484,4.818113,9.636743,-7.793019,7.254531,5.432520],[-4.263214,-2.446840,-6.845479,-9.133823,-9.846617,5.445170,4.513693,5.752249,-5.805175,9.180578,-3.691918,3.679886,-0.558936],[3.044861,-6.029728,-7.036949,8.356679,4.534943,5.971947,-3.625761,8.965227,8.732792,1.188323,2.547780,3.918717,-2.103026],[6.474182,6.104136,7.436195,1.767981,6.788197,-9.439672,-4.814843,7.608046,5.366516,7.796770,2.202515,4.864617,1.336239]],[[-6.655754,5.309372,2.992590,-1.084373,3.718157,1.133820,6.472215,-0.604699,1.238489,3.300687,5.959651,4.417153,8.913819],[0.190715,5.145876,6.020650,9.699375,-2.408145,-9.509601,3.718652,-3.500807,-3.132625,4.991464,9.790237,-2.240567,9.034531],[6.793821,-2.697106,4.740966,5.991641,4.268112,-6.390577,4.548836,8.624598,2.195317,9.652783,6.670370,-8.812407,5.319409],[-6.259921,-6.925392,8.996320,-9.074020,6.045809,3.001612,-7.665613,3.749266,5.594975,8.256879,-8.282602,9.520759,-4.736161],[-7.840358,5.271646,-3.858348,9.226675,-5.958836,-1.632022,-4.267553,-8.488762,-1.348546,-3.509542,-1.257238,-6.364484,-6.708280],[-1.975065,5.449645,1.610100,4.030475,9.638857,-1.608063,0.810297,7.286951,0.352636,1.263689,7.407209,-3.164716,7.046797],[3.698812,-4.032667,2.713086,7.745068,2.881299,-5.169106,9.249294,-0.098508,-0.247156,-3.729726,8.972084,4.251291,-1.116173],[-2.919984,1.131057,3.964146,2.965471,-2.877946,-9.947910,1.927368,-9.092555,4.639767,8.007293,5.648934,1.104836,3.354269],[3.402954,7.974437,1.785094,-1.643566,9.105933,0.804105,2.712636,7.335300,7.651881,8.491438,-5.272659,-3.934110,-4.945742],[7.110590,0.607651,-9.798979,-4.534302,-5.475905,2.296342,-3.269464,-9.769045,-5.732703,6.407719,-9.480104,-1.154782,6.306059]],[[-3.479224,7.151172,9.898584,-0.310518,1.331397,-9.258111,-3.265045,-3.118978,6.121259,-4.828525,-8.681747,-0.590951,4.529338],[0.508226,-0.388420,-7.691129,-1.360750,-1.630805,4.398462,-7.172762,7.705065,-9.143286,-0.350534,-5.766912,3.101566,7.493155],[5.598975,3.570386,-2.955264,-7.196647,5.322855,8.084505,-2.214246,-2.746504,-0.596417,9.885295,3.250440,8.273707,-8.452075],[7.713950,3.911711,9.550407,-0.539912,6.688149,3.745311,-0.271539,-3.389302,-5.102266,2.851237,-6.311933,-6.537626,4.551566],[4.264688,1.120751,-7.536106,6.928036,7.115496,-6.929702,-8.958504,6.161278,-7.854777,-3.254417,7.033703,9.502374,8.498390],[5.259274,1.201384,1.330161,3.538729,-5.933312,-5.817960,8.657681,3.288928,1.596849,1.008345,3.032704,-9.087832,9.837013],[0.408446,-7.285739,-6.543516,-5.273751,5.329138,9.979892,-0.661499,-0.329283,9.218749,-6.229834,-6.698044,-2.375072,-7.796021],[2.128043,-4.919824,5.623608,8.460896,-3.820117,9.278171,-5.508955,9.390544,9.494838,2.608518,-4.886582,-5.862736,0.679503],[-1.082322,-6.023231,-7.248998,-8.342724,-4.177231,-9.022867,2.603429,-2.730998,5.337038,5.681694,-4.684877,-6.112424,8.667726],[-7.344943,7.754025,-2.027095,-8.767967,3.300562,-9.361357,3.191957,0.597613,-5.715033,-1.061264,6.416947,5.659000,-5.270696]],[[1.532444,-8.322138,8.289073,-0.662813,-0.709260,0.222025,-6.564006,1.845083,-8.490868,7.012606,-1.909002,-1.160357,-8.878542],[-3.631547,4.315296,1.618682,5.688935,0.460550,4.806909,-3.314688,-2.666947,-8.345449,-5.347240,9.533689,-9.626720,-1.086186],[-5.743944,7.328905,-0.144088,6.597830,4.218535,-3.365572,-3.814265,3.940508,-0.826969,4.575948,8.376504,0.888761,-2.812405],[-7.063275,8.235842,6.428090,-5.567222,5.354523,8.222364,-1.942459,1.203256,9.605250,-1.021290,3.362602,-7.086792,7.160543],[-9.355097,6.883042,1.446251,7.145085,-6.633952,-3.672112,-9.352742,7.023537,-1.073205,-1.812305,8.630447,2.662607,-2.558768],[-3.406299,-1.875757,2.989675,-6.004891,5.016997,-0.072350,-0.723295,8.118263,2.227957,-3.340762,4.830152,-8.056359,5.251369],[-8.525094,9.300529,6.724793,6.496429,5.629507,6.451534,-6.147655,7.332151,7.199131,0.250751,9.691206,-8.857641,-9.325773],[-0.507853,9.291669,-6.927957,7.797896,5.261783,2.404746,-2.525614,0.265282,-9.215287,-3.018652,-6.116009,6.591402,-4.580808],[5.332769,7.152934,3.952479,-1.222296,2.004301,-5.408771,1.574363,9.111757,-6.486034,8.441865,4.358905,0.192063,-6.129432],[-9.678677,-4.125278,-1.410802,7.044372,4.324460,6.564817,-8.493404,-6.492791,5.684581,-4.495099,-4.694125,-3.380780,-1.555541]]], dtype = "float32")#candidate|1222|(7, 10, 13)|const|float32
uop_1223 = relay.asin(const_1222.astype('float32')) # shape=(7, 10, 13)
output = relay.Tuple([uop_1223,])
output2 = relay.Tuple([uop_1223,])
func_1232 = relay.Function([], output)
mod['func_1232'] = func_1232
mod = relay.transform.InferType()(mod)
mutated_mod['func_1232'] = func_1232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mutated_mod.get_global_var('func_1232')
call_1233 = func_1232_call()
output = call_1233
func_1234 = relay.Function([], output)
mutated_mod['func_1234'] = func_1234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_1277 = relay.TupleGetItem(func_1232_call(), 0)
call_1278 = relay.TupleGetItem(func_1234_call(), 0)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_1297 = relay.TupleGetItem(func_1232_call(), 0)
call_1298 = relay.TupleGetItem(func_1234_call(), 0)
output = relay.Tuple([call_1277,call_1297,])
output2 = relay.Tuple([call_1278,call_1298,])
func_1318 = relay.Function([], output)
mod['func_1318'] = func_1318
mod = relay.transform.InferType()(mod)
output = func_1318()
func_1319 = relay.Function([], output)
mutated_mod['func_1319'] = func_1319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_1340 = relay.TupleGetItem(func_1318_call(), 1)
call_1341 = relay.TupleGetItem(func_1319_call(), 1)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_1347 = relay.TupleGetItem(func_1232_call(), 0)
call_1348 = relay.TupleGetItem(func_1234_call(), 0)
output = relay.Tuple([call_1340,call_1347,])
output2 = relay.Tuple([call_1341,call_1348,])
func_1369 = relay.Function([], output)
mod['func_1369'] = func_1369
mod = relay.transform.InferType()(mod)
mutated_mod['func_1369'] = func_1369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1369_call = mutated_mod.get_global_var('func_1369')
call_1370 = func_1369_call()
output = call_1370
func_1371 = relay.Function([], output)
mutated_mod['func_1371'] = func_1371
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1399 = relay.var("var_1399", dtype = "float64", shape = (8, 16, 9))#candidate|1399|(8, 16, 9)|var|float64
uop_1400 = relay.log2(var_1399.astype('float64')) # shape=(8, 16, 9)
output = uop_1400
output2 = uop_1400
func_1403 = relay.Function([var_1399,], output)
mod['func_1403'] = func_1403
mod = relay.transform.InferType()(mod)
var_1404 = relay.var("var_1404", dtype = "float64", shape = (8, 16, 9))#candidate|1404|(8, 16, 9)|var|float64
output = func_1403(var_1404)
func_1405 = relay.Function([var_1404], output)
mutated_mod['func_1405'] = func_1405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1369_call = mod.get_global_var('func_1369')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1418 = relay.TupleGetItem(func_1369_call(), 0)
call_1419 = relay.TupleGetItem(func_1371_call(), 0)
func_1118_call = mod.get_global_var('func_1118')
func_1121_call = mutated_mod.get_global_var('func_1121')
const_1421 = relay.const(True, dtype = "bool")#candidate|1421|()|const|bool
call_1420 = relay.TupleGetItem(func_1118_call(relay.reshape(const_1421.astype('bool'), [])), 0)
call_1422 = relay.TupleGetItem(func_1121_call(relay.reshape(const_1421.astype('bool'), [])), 0)
output = relay.Tuple([call_1418,call_1420,const_1421,])
output2 = relay.Tuple([call_1419,call_1422,const_1421,])
func_1426 = relay.Function([], output)
mod['func_1426'] = func_1426
mod = relay.transform.InferType()(mod)
mutated_mod['func_1426'] = func_1426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mutated_mod.get_global_var('func_1426')
call_1427 = func_1426_call()
output = call_1427
func_1428 = relay.Function([], output)
mutated_mod['func_1428'] = func_1428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_1455 = relay.TupleGetItem(func_1426_call(), 1)
call_1456 = relay.TupleGetItem(func_1428_call(), 1)
output = relay.Tuple([call_1455,])
output2 = relay.Tuple([call_1456,])
func_1458 = relay.Function([], output)
mod['func_1458'] = func_1458
mod = relay.transform.InferType()(mod)
output = func_1458()
func_1459 = relay.Function([], output)
mutated_mod['func_1459'] = func_1459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_1485 = relay.TupleGetItem(func_1232_call(), 0)
call_1486 = relay.TupleGetItem(func_1234_call(), 0)
uop_1496 = relay.atanh(call_1485.astype('float64')) # shape=(7, 10, 13)
uop_1498 = relay.atanh(call_1486.astype('float64')) # shape=(7, 10, 13)
output = relay.Tuple([uop_1496,])
output2 = relay.Tuple([uop_1498,])
func_1502 = relay.Function([], output)
mod['func_1502'] = func_1502
mod = relay.transform.InferType()(mod)
mutated_mod['func_1502'] = func_1502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mutated_mod.get_global_var('func_1502')
call_1503 = func_1502_call()
output = call_1503
func_1504 = relay.Function([], output)
mutated_mod['func_1504'] = func_1504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1369_call = mod.get_global_var('func_1369')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1642 = relay.TupleGetItem(func_1369_call(), 1)
call_1643 = relay.TupleGetItem(func_1371_call(), 1)
var_1646 = relay.var("var_1646", dtype = "float32", shape = (7, 10, 13))#candidate|1646|(7, 10, 13)|var|float32
bop_1647 = relay.bitwise_xor(call_1642.astype('int16'), relay.reshape(var_1646.astype('int16'), relay.shape_of(call_1642))) # shape=(7, 10, 13)
bop_1650 = relay.bitwise_xor(call_1643.astype('int16'), relay.reshape(var_1646.astype('int16'), relay.shape_of(call_1643))) # shape=(7, 10, 13)
uop_1654 = relay.log(bop_1647.astype('float64')) # shape=(7, 10, 13)
uop_1656 = relay.log(bop_1650.astype('float64')) # shape=(7, 10, 13)
output = relay.Tuple([uop_1654,])
output2 = relay.Tuple([uop_1656,])
func_1657 = relay.Function([var_1646,], output)
mod['func_1657'] = func_1657
mod = relay.transform.InferType()(mod)
mutated_mod['func_1657'] = func_1657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1658 = relay.var("var_1658", dtype = "float32", shape = (7, 10, 13))#candidate|1658|(7, 10, 13)|var|float32
func_1657_call = mutated_mod.get_global_var('func_1657')
call_1659 = func_1657_call(var_1658)
output = call_1659
func_1660 = relay.Function([var_1658], output)
mutated_mod['func_1660'] = func_1660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_1684 = relay.TupleGetItem(func_1426_call(), 2)
call_1685 = relay.TupleGetItem(func_1428_call(), 2)
output = call_1684
output2 = call_1685
func_1694 = relay.Function([], output)
mod['func_1694'] = func_1694
mod = relay.transform.InferType()(mod)
output = func_1694()
func_1695 = relay.Function([], output)
mutated_mod['func_1695'] = func_1695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_1696 = relay.TupleGetItem(func_1502_call(), 0)
call_1697 = relay.TupleGetItem(func_1504_call(), 0)
output = call_1696
output2 = call_1697
func_1704 = relay.Function([], output)
mod['func_1704'] = func_1704
mod = relay.transform.InferType()(mod)
output = func_1704()
func_1705 = relay.Function([], output)
mutated_mod['func_1705'] = func_1705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_1744 = relay.TupleGetItem(func_1426_call(), 2)
call_1745 = relay.TupleGetItem(func_1428_call(), 2)
func_1657_call = mod.get_global_var('func_1657')
func_1660_call = mutated_mod.get_global_var('func_1660')
const_1751 = relay.const([-6.009401,5.560884,0.140795,-1.024628,9.272021,-9.806571,7.876090,-6.031437,0.734672,8.680049,-1.996533,-6.734895,3.779864,7.005672,-0.224412,2.401082,-5.723833,6.635727,-9.419033,7.249527,6.063354,9.848816,-9.556723,5.723669,-8.556918,4.171772,-8.143116,-8.024638,-3.158671,-8.809504,-8.340905,-0.251765,-5.955414,-1.612499,5.109476,-1.814750,7.999985,-4.099753,1.968204,3.297516,-6.550864,-4.642638,-6.684292,-5.627422,-1.579319,-5.643424,6.016366,2.605174,-0.544982,-2.431301,-9.885102,-7.543322,-6.569577,8.931666,-9.271959,5.859739,2.233774,2.547590,-9.165998,6.507635,-3.842692,1.882047,-7.731142,-1.471248,-0.637873,-0.806764,3.300289,4.159996,8.193556,-1.527095,1.684290,-8.119687,8.905868,9.399271,-6.260339,8.278514,-3.018005,-8.029813,7.125098,6.859710,3.217680,-5.043110,-6.841514,-8.362399,-5.613165,-0.776237,-3.127757,7.558908,-9.712125,-4.060927,6.360462,-3.811974,-2.114773,-8.040429,2.458630,-2.007964,8.740851,2.313133,-4.101044,-7.407731,-3.140575,-9.404144,7.962560,4.038772,-9.202760,-4.214531,0.305782,6.395675,6.067026,9.052984,5.421188,3.883458,7.036294,3.184601,-0.952811,-2.639025,-9.538605,-7.772755,-2.779170,0.191372,2.648954,-9.379132,-8.605875,-0.634244,9.513081,-6.908531,1.258381,-5.037898,0.009960,-3.933235,7.107975,-0.413208,-0.772009,2.010943,-4.476829,6.588994,1.200765,-4.543195,-1.674871,0.876242,8.904270,-5.293037,-7.353427,5.977354,-5.545836,9.639242,-4.423835,0.638639,-9.499816,-3.406176,-9.952127,-3.871809,3.336238,3.890031,-8.662320,-6.550046,1.008317,-8.718560,8.975735,0.265848,-8.536382,1.179742,-4.746772,5.230042,1.193015,-7.798476,4.026303,0.104631,6.928470,-7.962479,-8.000910,7.449965,-3.240076,8.768067,6.903882,3.003611,3.334048,0.789368,-5.942010,9.418016,-1.617110,4.198365,-7.220498,-1.374297,0.156875,7.485355,2.595461,3.447828,2.765452,9.975798,1.909736,-4.147520,1.233564,7.310047,-8.787894,-1.899599,-0.085390,-1.874166,-4.035929,-4.579854,-1.902369,3.531599,5.246184,6.605079,0.935836,6.726613,5.288853,-5.959226,9.065663,-3.132439,-2.066472,-6.249555,-6.017984,6.147407,-6.592670,3.472551,-0.837146,-0.327832,4.426981,-3.279285,1.578668,-8.749658,8.336812,4.473065,-0.240383,-6.318612,-3.112224,3.589397,7.658166,-5.140740,-3.637204,-4.858076,-2.484288,-0.885602,-0.285754,6.904340,6.735152,7.669675,-0.925621,8.425069,-0.424616,0.665341,6.612926,-0.710375,3.289772,-3.988172,-9.019044,-4.737965,6.473280,-8.795225,8.702478,1.400208,2.859509,9.616157,-4.678344,-8.055496,-3.485846,2.949751,-8.197160,8.289144,-5.715003,-3.429022,-9.658246,-8.679330,6.858938,-8.191834,-2.632438,7.336387,-6.456131,0.438469,-9.273529,1.451133,7.096955,-5.671440,-0.487370,1.489930,3.025658,2.638650,0.897333,9.697996,8.555270,6.249452,-0.068026,6.793761,-9.071589,1.291999,8.227115,8.170988,1.316608,-2.390132,0.965702,4.765161,0.645562,7.281701,-4.878507,-8.345905,-8.885551,5.340509,-2.403173,7.673256,6.254369,9.617480,9.343992,0.814918,-3.346631,7.677299,5.660925,-5.184647,8.465037,1.962472,3.887303,3.119938,-9.522674,-0.293209,-7.113480,2.376058,-4.716667,-5.488528,4.864565,-8.370775,9.780520,-7.884454,-3.053760,-0.506172,-0.938181,8.189052,3.200183,4.431156,7.442265,-1.462017,6.370548,8.580908,1.002931,1.892936,8.924549,-5.980859,5.442703,-1.736484,-1.616122,-3.981592,-3.550269,-8.334602,-6.481259,6.960902,8.032736,1.125761,9.543150,-6.082782,-8.190828,-6.906666,1.530556,0.587668,8.653562,3.424065,-8.487520,-3.067987,0.630198,-3.185623,-2.123105,-5.627388,5.952913,-7.615475,-0.447171,4.447261,-6.437162,2.209864,9.034036,8.893112,-1.090021,-1.393347,-1.865444,5.763750,5.418020,2.119832,-8.711781,4.566825,-6.205193,-3.933130,-8.735940,4.909500,8.528410,-7.645001,7.599524,4.506574,-9.008819,-4.158244,-6.559779,3.522184,2.662959,4.619969,-1.697631,-3.632629,-4.805417,0.401707,-5.434009,-6.144999,4.514770,-3.705473,-5.340661,-8.411676,3.160160,7.569334,0.691279,4.468453,0.617026,-8.871104,9.008229,-2.827030,0.136044,-5.239402,2.323359,-4.177225,-3.984241,7.322771,-0.713571,5.736935,7.934506,-6.557031,8.940909,1.509366,-1.965755,-8.428189,-6.091081,-2.340883,1.323303,-3.626495,4.237396,2.419812,6.510674,-9.832634,7.139734,-1.648303,-5.413150,6.957977,-7.479683,-4.496683,-8.840802,8.591921,-8.283671,-2.918725,-7.074497,-3.529360,8.532662,9.067764,-0.193420,5.379511,-5.967832,-0.247541,-1.843260,-0.039284,7.771525,7.806683,-0.257564,-8.211714,-7.076798,-4.568245,5.762080,-6.794792,-9.538519,-7.036633,1.267448,-2.094671,1.816658,-5.005278,-9.720452,-6.441878,-0.077225,3.104271,-2.618716,0.432907,8.128591,-4.731104,-9.834787,7.020151,-1.489961,0.249658,4.086432,7.157070,3.416366,-2.548914,1.420781,6.866448,5.310816,-8.550282,-4.590591,-7.630046,3.895928,9.327494,-3.316434,-8.007475,-7.562751,-9.760779,-4.322073,-9.641602,-4.039113,4.546554,3.402713,9.527753,-0.013538,4.298360,3.555296,-2.111898,-0.415990,-9.476754,-6.719435,5.443202,-3.704072,7.135441,-7.580523,-4.999145,-7.454918,-4.190280,-0.294097,-8.563293,6.707835,-7.519634,-3.584149,6.152052,-4.213960,4.768141,-0.191035,6.669169,-5.273473,8.456236,-6.858866,2.728307,-8.141011,-8.220368,6.978319,5.655689,-5.961161,9.481397,-4.649534,5.231582,-4.329340,6.254084,-4.250186,-0.815422,5.685517,8.177698,9.188838,0.265736,-7.565274,1.679446,-1.392924,-9.118522,-7.364701,8.251795,-8.638508,5.059155,9.762412,6.437199,1.282864,7.278019,-8.320237,-2.693006,8.478009,0.123487,4.099651,-5.866332,5.447552,1.448851,-2.562151,-2.127336,8.633462,-9.437183,-4.431388,-6.057483,0.805790,0.417196,-2.612176,3.273112,6.010582,3.379340,2.461666,-0.904311,-6.066528,-9.209993,5.165824,8.109946,-6.006022,3.073859,-7.349033,-4.755466,1.309062,6.673426,8.589936,-7.030128,2.349634,-9.521261,2.865314,7.978091,-5.898381,-9.698972,-3.378233,-0.580665,7.110693,0.058168,-2.406244,3.145759,7.488110,8.062610,-5.422175,3.754290,-6.653892,-9.219781,6.935367,2.447024,-7.106205,4.100755,-3.582810,3.842552,2.805720,1.589357,0.390524,-2.457594,7.702528,7.347018,1.594778,1.949235,-8.294798,8.017164,1.857586,4.464790,-9.480774,-2.056800,2.259452,7.686081,-5.232178,-5.049250,6.904050,3.554237,-2.595612,-3.154241,7.945740,2.908989,-6.399930,6.340142,-0.802145,9.000093,4.485704,5.443588,1.636261,-0.698929,4.535000,2.109155,9.785583,0.355639,-7.675074,0.984617,8.810773,3.197756,9.172487,0.541149,-0.820093,-6.447988,-7.554624,-7.752751,-0.520355,7.612943,0.416035,7.940435,6.481047,-5.242663,-5.503835,-0.881832,3.212048,0.386130,-4.578414,-5.389814,7.524288,7.912824,-0.102377,-5.742062,-0.119231,-3.085075,-1.171389,-3.542104,-1.534305,5.982488,-5.904940,-0.704206,-1.903926,-8.076460,-3.816992,9.259235,3.374952,8.929213,-2.134366,2.561349,6.232399,-8.956532,7.907126,-2.907993,3.794828,-5.570661,2.522392,2.479943,9.286344,-0.583317,-4.493339,6.543047,-2.277631,1.939021,-7.997744,7.648024,-0.488145,-2.819928,-6.423544,0.066296,-1.022708,2.508116,-4.249689,6.209481,-4.112208,9.213337,8.657005,5.312154,7.629162,-1.091945,8.524163,-7.155216,2.974486,3.617999,9.222945,-1.534226,-0.734369,9.501624,-6.556917,-0.271754,-6.635321,-4.506328,8.123809,-4.246322,-1.373869,-8.800616,-6.167464,-9.716203,5.023003,-4.041385,-4.789566,3.441885,-4.860792,-0.109581,1.902829,-6.091090,-9.696208,-2.777038,-9.350482,8.306039,8.378097,-3.466066,-4.661026,-2.333561,-8.809484,-1.924152,5.791950,0.095333,-7.968932,-5.081975,3.089214,9.643795,0.076612,3.859512,-6.469319,8.649182,-8.544107,-7.479753,-7.549650,1.406956,6.346237,1.761213,3.356026,-9.145822,-8.307819,8.499286,3.577931,-3.839427,-9.151063,-3.965978,-5.344899,6.231762,1.419564,2.619042,-6.679355,-0.955894,-5.804071,-6.389053,8.182644,9.995593,9.227960,9.158505,2.933390,-3.855861,7.430001,4.918579,-1.656021,-5.330440,-3.916905,7.729988,-6.149550,-0.110994,4.788724,-6.091826,1.194923,2.465860,5.358475,-7.958272,-1.006151,-7.853846,8.607080,6.472147,-9.639148,-1.398178,4.541086,9.399705,8.741606,-0.622750,-9.121511,1.601814,-4.146895,7.543721,6.456224,-5.132233,-7.270450,2.016176,-2.793742,5.436459,5.174194,3.719964,5.935946,-5.427138,-5.599018,9.550925,-2.374500,2.417603,3.173678,-4.758629,-7.999136,-6.433453,6.076489,-7.011875,-3.855078,2.644807,6.678664,-3.123413,2.079899,-3.915026,4.233753,2.090279,-1.030312,-9.216291,8.590762,7.643261,-4.721300,-2.415224,1.781614,8.280915,-0.731845,6.869012,-0.262192,-2.865551,2.444208,4.229915,-1.639801,-4.755247,6.663642,7.949494,1.218124,-1.546964,-0.719235,9.034308,-7.014641,-6.565463,7.247459,-6.060076,8.462087,-0.944318,7.133880,-3.286813,-8.959689,0.213841,2.729627,-7.620854,9.574575,-9.663355,5.440485,3.063428,0.763901,-5.443946,-4.248840,-4.455277,1.029180,-9.528801,-0.618806,-1.210850,0.188623,3.262333,-5.144634,6.218806,-8.906675,-9.492249,2.862522,9.896268,3.236159,-2.164918,0.828096,7.562069,2.601591,0.145146], dtype = "float32")#candidate|1751|(910,)|const|float32
call_1750 = relay.TupleGetItem(func_1657_call(relay.reshape(const_1751.astype('float32'), [7, 10, 13])), 0)
call_1752 = relay.TupleGetItem(func_1660_call(relay.reshape(const_1751.astype('float32'), [7, 10, 13])), 0)
output = relay.Tuple([call_1744,call_1750,const_1751,])
output2 = relay.Tuple([call_1745,call_1752,const_1751,])
func_1761 = relay.Function([], output)
mod['func_1761'] = func_1761
mod = relay.transform.InferType()(mod)
output = func_1761()
func_1762 = relay.Function([], output)
mutated_mod['func_1762'] = func_1762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_1791 = func_1704_call()
call_1792 = func_1704_call()
output = relay.Tuple([call_1791,])
output2 = relay.Tuple([call_1792,])
func_1797 = relay.Function([], output)
mod['func_1797'] = func_1797
mod = relay.transform.InferType()(mod)
output = func_1797()
func_1798 = relay.Function([], output)
mutated_mod['func_1798'] = func_1798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1797_call = mod.get_global_var('func_1797')
func_1798_call = mutated_mod.get_global_var('func_1798')
call_1849 = relay.TupleGetItem(func_1797_call(), 0)
call_1850 = relay.TupleGetItem(func_1798_call(), 0)
func_1369_call = mod.get_global_var('func_1369')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1854 = relay.TupleGetItem(func_1369_call(), 0)
call_1855 = relay.TupleGetItem(func_1371_call(), 0)
output = relay.Tuple([call_1849,call_1854,])
output2 = relay.Tuple([call_1850,call_1855,])
func_1858 = relay.Function([], output)
mod['func_1858'] = func_1858
mod = relay.transform.InferType()(mod)
output = func_1858()
func_1859 = relay.Function([], output)
mutated_mod['func_1859'] = func_1859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_1891 = func_1704_call()
call_1892 = func_1704_call()
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_1896 = func_1704_call()
call_1897 = func_1704_call()
output = relay.Tuple([call_1891,call_1896,])
output2 = relay.Tuple([call_1892,call_1897,])
func_1916 = relay.Function([], output)
mod['func_1916'] = func_1916
mod = relay.transform.InferType()(mod)
output = func_1916()
func_1917 = relay.Function([], output)
mutated_mod['func_1917'] = func_1917
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1937 = relay.var("var_1937", dtype = "float32", shape = (5, 5, 12))#candidate|1937|(5, 5, 12)|var|float32
uop_1938 = relay.acos(var_1937.astype('float32')) # shape=(5, 5, 12)
func_126_call = mod.get_global_var('func_126')
func_129_call = mutated_mod.get_global_var('func_129')
var_1941 = relay.var("var_1941", dtype = "float32", shape = (24,))#candidate|1941|(24,)|var|float32
call_1940 = relay.TupleGetItem(func_126_call(relay.reshape(var_1941.astype('float32'), [4, 1, 6])), 0)
call_1942 = relay.TupleGetItem(func_129_call(relay.reshape(var_1941.astype('float32'), [4, 1, 6])), 0)
func_1916_call = mod.get_global_var('func_1916')
func_1917_call = mutated_mod.get_global_var('func_1917')
call_1953 = relay.TupleGetItem(func_1916_call(), 1)
call_1954 = relay.TupleGetItem(func_1917_call(), 1)
output = relay.Tuple([uop_1938,call_1940,var_1941,call_1953,])
output2 = relay.Tuple([uop_1938,call_1942,var_1941,call_1954,])
func_1956 = relay.Function([var_1937,var_1941,], output)
mod['func_1956'] = func_1956
mod = relay.transform.InferType()(mod)
var_1957 = relay.var("var_1957", dtype = "float32", shape = (5, 5, 12))#candidate|1957|(5, 5, 12)|var|float32
var_1958 = relay.var("var_1958", dtype = "float32", shape = (24,))#candidate|1958|(24,)|var|float32
output = func_1956(var_1957,var_1958,)
func_1959 = relay.Function([var_1957,var_1958,], output)
mutated_mod['func_1959'] = func_1959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_1969 = relay.TupleGetItem(func_1761_call(), 0)
call_1970 = relay.TupleGetItem(func_1762_call(), 0)
output = relay.Tuple([call_1969,])
output2 = relay.Tuple([call_1970,])
func_1975 = relay.Function([], output)
mod['func_1975'] = func_1975
mod = relay.transform.InferType()(mod)
output = func_1975()
func_1976 = relay.Function([], output)
mutated_mod['func_1976'] = func_1976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_1997 = relay.TupleGetItem(func_1858_call(), 0)
call_1998 = relay.TupleGetItem(func_1859_call(), 0)
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_2009 = func_1694_call()
call_2010 = func_1694_call()
uop_2014 = relay.log10(call_1997.astype('float64')) # shape=(7, 10, 13)
uop_2016 = relay.log10(call_1998.astype('float64')) # shape=(7, 10, 13)
output = relay.Tuple([call_2009,uop_2014,])
output2 = relay.Tuple([call_2010,uop_2016,])
func_2026 = relay.Function([], output)
mod['func_2026'] = func_2026
mod = relay.transform.InferType()(mod)
output = func_2026()
func_2027 = relay.Function([], output)
mutated_mod['func_2027'] = func_2027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_2034 = relay.TupleGetItem(func_1232_call(), 0)
call_2035 = relay.TupleGetItem(func_1234_call(), 0)
func_1657_call = mod.get_global_var('func_1657')
func_1660_call = mutated_mod.get_global_var('func_1660')
call_2036 = relay.TupleGetItem(func_1657_call(relay.reshape(call_2034.astype('float32'), [7, 10, 13])), 0)
call_2037 = relay.TupleGetItem(func_1660_call(relay.reshape(call_2034.astype('float32'), [7, 10, 13])), 0)
output = relay.Tuple([call_2034,call_2036,])
output2 = relay.Tuple([call_2035,call_2037,])
func_2048 = relay.Function([], output)
mod['func_2048'] = func_2048
mod = relay.transform.InferType()(mod)
mutated_mod['func_2048'] = func_2048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2048_call = mutated_mod.get_global_var('func_2048')
call_2049 = func_2048_call()
output = call_2049
func_2050 = relay.Function([], output)
mutated_mod['func_2050'] = func_2050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2069 = relay.var("var_2069", dtype = "uint8", shape = ())#candidate|2069|()|var|uint8
var_2070 = relay.var("var_2070", dtype = "uint8", shape = (7, 5, 12))#candidate|2070|(7, 5, 12)|var|uint8
bop_2071 = relay.multiply(var_2069.astype('uint8'), var_2070.astype('uint8')) # shape=(7, 5, 12)
func_2026_call = mod.get_global_var('func_2026')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_2076 = relay.TupleGetItem(func_2026_call(), 0)
call_2077 = relay.TupleGetItem(func_2027_call(), 0)
bop_2078 = relay.bitwise_and(var_2069.astype('uint16'), var_2070.astype('uint16')) # shape=(7, 5, 12)
func_842_call = mod.get_global_var('func_842')
func_848_call = mutated_mod.get_global_var('func_848')
const_2092 = relay.const([5.046403,9.240465,4.754336,-4.061708,-6.085633,-6.069992,4.723295,4.939207,-1.419166,2.550572,-9.647349,-2.071848,-9.315048,5.820598,4.703458,-9.179996,3.786179,7.974981,3.602897,-1.819348,2.493631,-6.294347,-2.049149,6.407785,-5.799711,0.793216,-0.413277,0.700883,2.959485,-3.679648,6.759920,0.692885,-8.590426,9.258108,-6.468825,-1.984711,-1.858142,-5.216243,-2.826051,-2.211464,-7.858985,7.948817,2.065577,-8.253713,7.600672,7.240427,7.275248,3.771205,-7.978280,2.771097,8.854567,-4.427984,-4.682605,-8.048020,-9.253928,-3.060365,-0.726285,6.237731,-9.819349,-7.872480,7.390999,-5.551063,-9.753176,-9.082970,-7.005630,2.328524,6.317816,-3.747362,2.280116,-1.776658,6.638519,-8.304876,5.994595,3.435933,4.321821,9.663172,-0.335351,-1.930918,-5.638376,4.890546,-9.955370,-6.075519,-0.911800,-1.078269,4.905285,7.000895,3.437726,-3.336766,-1.522063,-0.590638,-7.622213,-6.671876,4.624268,6.890964,6.726315,-7.506606], dtype = "float64")#candidate|2092|(96,)|const|float64
var_2093 = relay.var("var_2093", dtype = "float32", shape = (1, 546))#candidate|2093|(1, 546)|var|float32
var_2094 = relay.var("var_2094", dtype = "float32", shape = (24,))#candidate|2094|(24,)|var|float32
const_2095 = relay.const([-3,-6,3,3,-2,4,-8,3,-1,-4,6,-3,-2,8,6,5,-2,-4,-4,-4,7,-8,6,2,-8,-6,-10,3,-9,3,8,5,-9,-6,7,1,9,10,3,-5,-8,7,10,-9,5,-6,-2,-5,-9,5,-3,9,-6,-7,1,-3,-5,-7,2,-5,8,10,-10,10,-7,5,-1,-2,-3,9,-3,1,1,-2,-3,-10,6,-10,4,-8,-5,3,-7,-7,3,4,-6,-3,-2,10,2,8,-9,-6,8,-5,9,3,2,6,-5,3,-5,8,1,-5,-9,3,-9,4,5,4,-7,9,8,7,6,-3,-6,8,-3,2,-4,-4,6,-2,-7,-4,-7,6,-8,7,2,-3,-4,-10,2,9,-9,-8,-10,5,-1,2,1,1,10,3,9,4,7,-10,-6,-4,3,9,6,-9,-2,-5,10,2,6,-5,1,10,-1,-6,9,-1,2,6,-3,-5,9,-8,5,-10,-7,-8,2,8,-8,2,2,2,3,-2,-2,-1,-6,-9], dtype = "int8")#candidate|2095|(192,)|const|int8
call_2091 = relay.TupleGetItem(func_842_call(relay.reshape(const_2092.astype('float64'), [16, 2, 3]), relay.reshape(var_2093.astype('float32'), [546,]), relay.reshape(var_2094.astype('float32'), [12, 2]), relay.reshape(const_2095.astype('int8'), [192,]), ), 1)
call_2096 = relay.TupleGetItem(func_848_call(relay.reshape(const_2092.astype('float64'), [16, 2, 3]), relay.reshape(var_2093.astype('float32'), [546,]), relay.reshape(var_2094.astype('float32'), [12, 2]), relay.reshape(const_2095.astype('int8'), [192,]), ), 1)
bop_2098 = relay.bitwise_xor(var_2093.astype('int32'), call_2076.astype('int32')) # shape=(1, 546)
bop_2101 = relay.bitwise_xor(var_2093.astype('int32'), call_2077.astype('int32')) # shape=(1, 546)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_2120 = relay.TupleGetItem(func_1426_call(), 2)
call_2121 = relay.TupleGetItem(func_1428_call(), 2)
func_1657_call = mod.get_global_var('func_1657')
func_1660_call = mutated_mod.get_global_var('func_1660')
const_2138 = relay.const([-5.301663,-8.766921,-1.715673,3.969706,-6.651673,2.642243,0.614916,-4.136367,-5.411958,8.616372,-6.603975,-0.051143,-9.719108,8.079151,8.549976,1.099833,-5.792832,7.484303,-3.725614,-4.376509,6.174307,9.266699,-6.015478,0.603471,-8.384671,9.774040,4.157766,9.300446,4.168021,2.853236,-4.327687,-6.779469,-0.230126,6.627366,-1.146386,7.976561,3.931430,1.286278,1.751651,4.856724,2.157137,-2.846941,-4.644617,6.066482,-6.992749,-9.118320,9.494882,6.719181,-0.382076,-7.593665,-8.241664,3.158173,2.044863,5.365572,0.808755,-5.870423,1.437356,5.585296,0.517207,5.412024,7.616219,-1.651303,-1.369467,-4.885936,-8.424036,-7.790129,3.214458,1.863445,-6.470028,9.831149,3.088901,-6.283179,-1.394415,-0.218878,-9.949137,0.310497,1.303259,-9.876497,3.378753,7.116637,-5.469669,-8.826394,1.456676,-4.581453,-9.839672,5.875909,6.120027,9.414381,-5.750501,7.721763,1.836839,-2.930832,-9.959066,5.918545,-8.892728,-2.795322,-6.777952,-6.461506,-7.920185,5.744500,-1.518995,-5.547717,-5.320073,6.573443,2.341020,-0.246124,5.429105,6.896511,2.775020,0.824732,1.335170,-0.225177,-9.864592,6.536555,9.322113,3.920632,-4.234557,-5.394004,9.976290,2.458183,-4.972990,-3.051062,-4.251250,-3.117928,-6.041198,8.984652,1.808697,3.465588,-0.123765,-2.806957,8.180884,3.876364,8.695713,-4.754631,0.258717,3.146998,7.834266,6.768211,8.771383,-8.479888,8.384995,-2.402253,1.172216,-5.418290,-2.321796,-3.968060,3.716341,6.167862,1.190606,7.204267,1.705701,-0.834677,-0.184389,8.212509,7.633680,9.767574,4.918396,0.991906,4.052957,4.599085,-6.065849,9.699981,8.555313,-8.785710,6.451068,-4.644153,-9.669224,5.589304,-8.793028,0.019839,-0.775071,3.969339,-5.098852,0.517476,-1.129796,8.473454,-5.866660,-3.220695,-3.488487,-9.693399,6.937314,-6.557595,7.746346,-6.403051,-8.646070,-7.271752,4.708707,3.377256,-2.413634,3.032258,6.242453,-2.083230,-7.883986,6.809152,0.975978,-7.748078,-6.256976,6.385273,-5.091778,-5.252911,3.220600,-0.421971,-3.215346,-5.783064,-1.701971,8.059137,-9.721673,8.637088,5.629701,0.220436,-7.860544,8.576775,6.815648,-4.371405,-2.969682,-3.614763,3.962390,-5.502875,-8.245223,7.609338,9.511926,-8.103695,-1.454677,-4.189283,4.085842,-6.495789,9.048800,-1.589231,-7.068843,-1.918018,1.698919,-3.959052,9.632376,-6.507431,3.272927,-8.109230,9.269313,7.660263,-4.639961,1.832521,6.210949,4.603930,1.008377,5.868153,2.336442,-4.584065,3.577524,8.195531,-7.122652,-6.365978,3.074956,-2.021196,-2.697699,-2.529393,0.490682,-2.954714,-9.071601,7.415734,3.845146,5.578611,-9.959350,-7.665601,0.278369,1.705578,5.453863,1.014397,-9.445027,5.514227,1.434487,-6.863883,5.254795,-1.061778,-5.739663,9.928147,-2.104065,-5.610701,8.256647,-0.975836,2.397507,-0.616794,-6.637366,2.312355,3.484139,1.426011,5.537110,3.937134,-0.086618,-4.906100,3.044410,-0.933400,-6.427601,-4.235130,9.240863,-1.335894,-5.636251,-8.918850,2.395886,-6.821550,-7.181189,0.762266,2.196448,8.966116,-5.740037,-1.761541,1.447357,-4.877963,-5.738052,6.772981,9.709149,-8.530381,-0.529703,-8.484760,-5.335873,-6.870200,-1.059113,-8.205836,-6.751130,9.591985,9.661216,-9.414540,1.595822,5.668901,-0.934493,9.613229,-1.330979,8.252279,-3.686500,-3.298275,-6.586460,-3.882524,3.655090,-6.587470,-8.746692,-2.120196,-1.032266,-8.677405,9.553580,4.905914,5.375348,-8.832081,-1.443898,-1.247460,3.984488,0.952873,-6.851489,3.988528,1.618911,8.771149,3.072526,6.385339,3.543644,0.314403,3.017947,-6.199088,-5.799279,5.744895,-7.464334,9.543520,-1.562785,-4.088736,-4.038470,-0.721916,1.559646,8.338330,-9.939511,-1.906222,8.985226,-2.244667,-6.245383,2.105974,7.696850,4.043808,-7.802731,-8.808350,-8.567291,0.902237,-8.166257,-6.520172,-0.412869,-9.532595,-0.651801,-3.963651,2.227439,6.787305,1.138755,-5.465916,1.744150,-3.586243,-4.151744,-6.745142,8.754970,-2.356698,-2.636958,-9.183092,-7.592271,8.545958,1.175511,-9.009179,-8.171804,2.793829,-3.064960,3.681596,3.071959,-2.605797,-7.625821,-1.750146,-1.735104,1.714111,7.878980,8.790351,-0.373975,7.677503,-8.173357,-0.400834,8.393608,-6.698041,0.487459,9.344163,-3.233291,8.850326,-9.314741,-5.422769,-6.510175,2.667584,1.748568,7.580535,0.574846,-4.433415,8.023030,1.612428,-5.948307,-3.612553,0.039986,-2.832245,3.959831,-9.804315,-7.531161,3.222397,-4.527204,-6.879358,5.648175,6.200391,-8.910754,8.238818,8.064318,-6.809831,-6.212684,7.302648,-4.471212,1.737670,3.959606,-9.092786,7.479710,-4.403467,-5.435397,4.320824,4.959551,5.850646,-7.540896,3.794400,0.407905,5.306635,-6.337057,2.526540,7.945787,0.082693,-2.918643,-3.347558,7.582927,4.100135,8.445249,4.823017,0.943251,3.209463,6.273706,2.954195,-8.997192,0.981598,-6.709684,-2.994517,1.863390,-7.329948,9.760584,9.491678,-0.045394,-1.094149,-8.886155,-3.926358,-0.420407,5.693046,-8.610330,-0.693342,-2.674817,4.756969,-8.951298,-5.545034,6.724799,0.537620,6.754030,6.662709,7.030971,4.640551,-0.853353,-3.822987,4.563922,-3.083898,-1.790730,3.809025,-3.122329,8.939406,-0.510661,4.279567,4.201822,-7.424959,2.703924,-4.301083,5.358143,-9.160181,5.024578,6.175778,2.550293,-9.450767,-2.578870,-3.282121,-1.808932,-0.896609,9.847552,1.492645,-1.082617,2.419434,3.368794,7.776080,8.570158,-8.997942,-0.494733,-9.092576,-0.063006,3.876630,-9.448306,2.643027,-1.252931,0.817357,2.241092,-1.518689,-1.308325,-6.854128,4.800558,-4.091097,1.891003,7.351674,-9.662070,6.802039,-8.642367,-7.612219,-7.327740,1.030165,0.029831,-3.115106,4.568604,-2.504759,-5.154412,-9.349221,-2.035840,9.344731,2.887015,1.026815,-1.216329,-7.528068,-9.883776,4.924657,0.841602,5.840638,0.965195,8.153859,-9.805490,-0.017866,-8.841684,-2.136363,5.045733,1.462459,-2.950437,8.230461,4.423774,7.815819,-6.826326,5.527894,4.599734,-6.889775,-0.501636,-9.642570,7.036038,-7.449674,0.890788,4.185061,-5.895111,8.308442,1.233827,0.692947,6.146144,-1.350923,9.237235,3.438882,-1.091262,8.477605,9.556016,8.112544,-8.748244,6.884173,-4.416765,-9.715068,4.218386,2.263496,-8.110986,7.992127,8.198055,8.748026,4.860606,-4.593328,-4.574908,6.919644,6.388836,0.745382,-6.037991,3.974379,9.636160,6.931585,6.485678,1.855023,6.667586,6.067570,1.974436,3.208150,4.103183,-8.485878,8.374208,-3.279028,9.571327,-7.482817,-7.766099,-2.469404,3.636596,-6.634369,7.843047,4.929417,-7.792369,7.472295,8.905843,7.039620,-5.033237,4.039214,3.587646,-7.700482,1.474045,-1.465172,-7.764389,5.467008,-5.664316,7.480453,3.609743,-5.748375,8.981433,1.416067,-9.858738,-2.675114,3.677524,-6.765564,0.960466,1.804888,1.997800,-8.167790,-0.766992,4.967694,9.595002,-7.012525,7.302634,-9.311507,3.703917,-5.007255,-2.063208,-6.046352,-4.772395,-0.295911,-3.206288,-2.634585,1.722913,8.880731,-4.318741,-2.462416,1.969109,-8.480726,4.421859,-7.767010,8.117282,-6.517992,7.654200,9.375096,5.761082,5.736667,0.507354,5.110622,-4.869160,-5.789307,-8.718785,-2.676284,-8.927424,-4.725968,8.602480,-0.761108,0.158694,2.443146,8.946902,-9.756023,-0.668328,-8.067277,9.113168,5.871891,0.591964,-8.916408,-7.775557,9.318381,-1.661962,1.896572,-7.376236,-0.999584,-3.990750,-0.886175,-8.177634,2.201562,-4.545917,-2.620501,7.297117,7.189302,2.517091,-3.114603,-0.142077,-7.269442,-6.848141,6.121976,2.460149,-1.026637,2.459306,-1.850261,-8.441761,-0.880139,1.472392,-8.320419,-0.796808,9.656475,-3.761496,-6.027336,-8.972860,0.309062,-7.999825,2.950105,-0.399767,1.024423,4.645778,4.040004,1.743551,-1.479061,-8.961865,-7.696921,1.072305,-7.888341,7.309417,-5.115409,-3.598155,-9.728795,-8.111899,-2.914982,-6.905491,-3.130753,6.704879,2.160711,-2.264339,-7.896753,-6.689376,2.479720,-7.750247,1.216358,-3.212111,7.875219,4.611700,6.103481,-3.146720,-8.862081,-0.892461,-7.025686,-1.002461,-1.254144,7.644387,5.530630,9.606503,3.858825,4.225006,-1.002540,3.901826,-6.757418,2.797396,-1.923286,5.974580,-1.019140,-6.705472,-2.156816,-6.130467,0.394977,9.105976,-3.102809,5.371719,-4.541426,-4.648468,1.242539,1.513724,8.509002,2.284336,-4.359348,-1.544195,-2.652972,6.277467,-8.519679,-6.950407,6.426589,-3.204895,-8.041145,-0.469602,-1.960717,7.773465,-0.583619,6.771726,-3.204940,0.112498,-7.373291,6.592785,-0.096849,4.099554,8.686505,-4.514583,8.375366,-5.425645,3.005872,-7.859903,6.085500,9.326765,-9.157077,8.068691,2.624076,2.614588,3.382887,3.937279,4.470174,-5.177895,-3.806746,-8.279480,1.829544,1.055348,2.972873,8.988936,-4.091084,-2.731453,2.628160,8.209646,-9.904033,-0.636286,8.029051,-5.622906,-6.255570,6.569312,3.660954,-3.012789,-3.888664,6.077591,-7.807237,0.890380,7.008063,2.619813,5.273986,-4.372854,-2.720100,5.520212,-9.776821,-2.950398,-3.413573,2.017960,7.712330,5.427962,2.145724,7.067707,5.871255,-2.486407,-0.824340,4.328477,-1.743996,-8.124870,3.708056,7.156452,8.547656,-9.419439,4.771938,5.005644,-7.240835,8.196796,-9.737273,2.338894,7.685708,-8.425336,2.731715,5.695632,5.373577,-4.569113,-8.113566], dtype = "float32")#candidate|2138|(910,)|const|float32
call_2137 = relay.TupleGetItem(func_1657_call(relay.reshape(const_2138.astype('float32'), [7, 10, 13])), 0)
call_2139 = relay.TupleGetItem(func_1660_call(relay.reshape(const_2138.astype('float32'), [7, 10, 13])), 0)
output = relay.Tuple([bop_2071,bop_2078,call_2091,const_2092,var_2094,const_2095,bop_2098,call_2120,call_2137,const_2138,])
output2 = relay.Tuple([bop_2071,bop_2078,call_2096,const_2092,var_2094,const_2095,bop_2101,call_2121,call_2139,const_2138,])
func_2145 = relay.Function([var_2069,var_2070,var_2093,var_2094,], output)
mod['func_2145'] = func_2145
mod = relay.transform.InferType()(mod)
mutated_mod['func_2145'] = func_2145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mutated_mod.get_global_var('func_2145')
var_2147 = relay.var("var_2147", dtype = "uint8", shape = ())#candidate|2147|()|var|uint8
var_2148 = relay.var("var_2148", dtype = "uint8", shape = (7, 5, 12))#candidate|2148|(7, 5, 12)|var|uint8
var_2149 = relay.var("var_2149", dtype = "float32", shape = (1, 546))#candidate|2149|(1, 546)|var|float32
var_2150 = relay.var("var_2150", dtype = "float32", shape = (24,))#candidate|2150|(24,)|var|float32
call_2146 = func_2145_call(var_2147,var_2148,var_2149,var_2150,)
output = call_2146
func_2151 = relay.Function([var_2147,var_2148,var_2149,var_2150,], output)
mutated_mod['func_2151'] = func_2151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_2168 = relay.TupleGetItem(func_1318_call(), 0)
call_2169 = relay.TupleGetItem(func_1319_call(), 0)
var_2174 = relay.var("var_2174", dtype = "float32", shape = (7, 10, 13))#candidate|2174|(7, 10, 13)|var|float32
bop_2175 = relay.greater_equal(call_2168.astype('bool'), relay.reshape(var_2174.astype('bool'), relay.shape_of(call_2168))) # shape=(7, 10, 13)
bop_2178 = relay.greater_equal(call_2169.astype('bool'), relay.reshape(var_2174.astype('bool'), relay.shape_of(call_2169))) # shape=(7, 10, 13)
func_1403_call = mod.get_global_var('func_1403')
func_1405_call = mutated_mod.get_global_var('func_1405')
const_2186 = relay.const([-6.644289,-5.211809,5.357894,2.942116,4.902244,-6.094415,-9.029526,-1.095704,3.669912,-3.262687,-4.283287,-1.919769,-8.960436,7.820311,9.306757,-2.850140,8.651028,2.656195,-1.389001,-0.659441,4.501504,-3.855122,-2.675154,2.431274,-5.302770,-6.055794,-9.949685,-1.448290,9.168078,-4.298966,-7.897967,9.530967,8.705828,8.686534,4.469294,5.623940,-3.367010,0.578028,-3.261544,1.122315,-3.937101,-0.538489,-5.323507,4.818458,-5.278055,-4.084223,2.837398,-6.863701,3.815971,-2.798638,9.748779,5.403064,-6.493772,-7.906895,7.513996,8.855232,3.958070,-7.450380,-0.208387,-4.663058,-3.703819,-6.508903,-1.606523,-7.644624,-7.434623,-9.353618,1.137385,6.504515,-0.448934,-1.641602,5.299612,-5.588480,0.191655,-7.595156,-3.583761,9.163160,-5.887735,-8.250513,-2.836088,-5.447420,-5.267229,6.358778,-1.109862,8.801441,-1.883146,-7.884417,8.507461,1.419794,2.542874,1.407159,-4.718131,-6.050171,-1.625462,2.119863,-8.342408,7.280142,-6.275357,-2.714717,9.468811,-6.243428,0.886438,-8.971001,7.743368,-3.773527,9.956793,-6.327376,-5.092486,-0.759220,-0.641309,6.870123,6.342189,2.906363,2.666726,-8.793508,8.228626,7.674731,8.429444,6.606179,3.861369,-0.642003,2.011728,-0.724934,0.223389,-6.364200,-0.211688,-0.415685,-2.066174,8.723008,7.905362,4.727978,-9.654736,-5.765600,-2.233059,-6.228763,0.330177,-0.319763,-7.918027,-9.343965,-1.036344,2.259115,-1.879462,-8.749595,8.188135,1.122011,-7.185289,6.550254,4.691360,-4.184968,0.132266,2.585174,4.113643,-7.391628,-2.093429,-1.572324,9.345644,1.302110,9.984930,1.080567,6.832496,-8.809193,2.221383,1.996716,3.122161,-0.761917,-5.705891,4.308627,8.760298,5.960537,-4.148456,-6.444324,9.334742,4.416241,-7.363883,9.606280,2.745893,4.169449,9.511544,2.147985,-0.169840,-2.984985,3.763009,0.062367,4.120025,-2.397836,-4.445732,7.021904,-8.499109,-2.637807,4.033949,5.404454,4.165564,2.762711,8.683482,5.316296,-1.269087,-4.706177,5.944506,4.813195,2.496525,-1.164503,-9.189862,4.855155,1.746324,4.887937,-7.317847,4.045303,7.430416,-6.637177,-9.684844,8.621263,6.750445,-7.002547,9.517205,4.890322,-5.790410,-9.097766,-4.242071,7.205493,1.132152,-3.423460,5.588043,-9.720799,2.258542,8.015397,-8.439945,-9.537356,2.595522,4.077084,-6.428478,5.273183,-1.932777,-0.145220,3.330972,-8.626983,-8.381131,-1.101616,2.115064,0.701949,-4.235417,-1.625633,9.543349,-1.821554,3.628954,5.720204,6.282299,-2.409769,-0.570514,-3.410693,1.064127,-2.234682,3.290782,9.779089,8.990934,7.397549,-3.090201,7.241776,4.320771,-3.418705,0.339313,-0.167557,-6.951568,-9.520677,1.784208,-1.043028,-1.251323,4.831448,-0.464124,-0.582826,5.965615,8.299948,1.690265,0.686780,-4.153287,6.300757,2.097216,-1.755286,9.956620,-4.220881,2.461785,1.816740,8.505915,-2.125971,6.792193,-1.476751,-6.781024,-5.541987,-5.506263,-5.960180,7.236357,-7.082569,-1.288348,-0.064490,9.510492,-1.717720,-8.604052,-4.973172,-3.141262,0.850976,8.481459,-7.754998,4.199053,7.126455,-7.319938,-8.088627,-5.046213,-7.969908,-8.842246,-4.915321,8.271689,-1.218634,-8.743778,-4.103283,7.817052,-4.416991,6.768761,1.250499,-2.050735,-2.879976,-8.839418,-1.972603,1.686476,2.472284,-2.801879,2.432994,7.619134,5.726493,2.718674,-2.895145,0.972961,4.522560,-6.171342,9.714976,-7.924869,2.534441,-1.284087,6.502459,5.794099,9.230532,-4.946408,5.298575,2.638952,4.570898,-6.983425,5.227592,-9.425549,-3.565763,9.278017,1.939932,8.812799,0.401870,6.930889,9.110787,7.585353,-0.482888,-6.791036,9.282672,-9.180596,-9.994430,9.884752,-4.996074,-9.593325,-5.258104,-8.818035,4.521829,-5.505743,9.523288,0.778663,-8.064323,-1.370755,-7.632131,4.228869,-6.185961,-9.031094,-7.305866,-4.018205,-5.049004,-4.790102,8.943088,-8.052796,-2.533743,3.276139,-1.212876,6.791088,7.675636,1.591417,-4.077205,-0.951215,-4.690642,0.373099,-7.869461,9.683005,-8.731584,1.420029,-2.619385,8.192158,-1.685840,2.687259,9.242219,-2.034098,-4.501662,5.335081,-6.507728,6.774431,-0.254999,0.156712,-0.820093,5.008387,-4.416346,-4.048834,8.034857,-3.931949,-2.578588,-6.940567,-1.569204,9.124076,9.996203,0.693703,-0.109842,-4.429125,2.491611,8.964635,4.925318,-1.159700,4.379364,-5.463103,-6.529536,-9.531652,-4.586112,8.792080,8.670787,2.946299,8.576288,-0.528816,8.524682,-0.726266,8.288944,4.287865,8.828758,-1.796002,-1.047649,8.856749,1.151348,-9.324071,-5.527421,-5.664224,-9.769986,-5.551656,-8.082814,3.678093,-2.977937,-5.129426,3.078531,-0.625225,-4.118078,7.717731,2.359561,5.442535,-1.625168,0.796559,2.200689,8.616010,7.226193,6.022387,-3.630630,-1.052266,2.626670,-5.720048,-1.694125,3.497227,-8.101595,9.936439,2.973118,-0.773606,-9.273952,-9.062877,-7.264375,3.864519,-6.117057,5.198181,1.200417,7.319783,4.782804,1.817303,-5.552425,-1.377952,7.984702,-9.874285,-4.675239,9.884514,-1.502394,2.692747,4.426844,4.696144,6.510492,-8.595573,-2.590078,6.379662,-5.954964,4.016070,8.505747,5.012943,8.040587,3.364582,-1.233166,8.993333,2.758956,3.840406,0.761318,-4.560580,-9.270242,-8.892500,-5.267079,-7.167422,-8.091715,1.899178,9.819344,3.705346,-6.930976,-8.184327,1.453321,-7.165258,-6.488909,2.198535,-8.860569,3.204261,-8.973208,7.447099,3.961702,3.320273,3.193539,-1.735928,5.253404,8.661392,-6.894242,2.868502,2.474718,-0.674371,7.628773,-2.039564,8.759728,-9.910338,0.610578,-3.131683,8.465690,-0.192564,-9.083395,9.432137,-9.246194,-5.038579,0.203446,-1.565821,9.744834,-7.601923,-2.624709,-0.443976,-1.482160,-4.407416,-9.779280,6.836611,-4.941322,-3.669507,-6.874097,8.919601,-8.486330,9.289432,1.330808,6.980139,1.357119,7.434138,-7.825398,4.604198,5.937218,-1.999990,3.245561,5.571506,3.823724,-1.375191,-8.246437,0.071502,8.617950,-5.758442,-5.274303,2.192793,5.227530,-3.864617,-8.753345,9.204386,6.934819,6.942937,0.851904,-6.424484,-7.124638,-3.827105,-4.447721,-9.500318,-6.073568,-5.595530,-1.473348,-3.712976,4.067346,7.206819,7.695318,4.686892,-5.394458,5.757845,7.466450,-5.423786,-3.970937,-3.250591,-4.804737,7.234421,7.405557,-1.564984,8.331373,-2.608221,3.686429,1.068673,-5.766287,4.671988,9.111836,-9.205972,-2.729006,0.222617,5.098877,-8.315436,-6.109245,-2.471109,8.191102,7.332702,-3.287847,9.829465,4.739662,-2.833431,5.211181,-9.249391,-2.006025,-6.603857,4.602301,7.220393,8.395442,7.879600,5.064766,-3.451107,-7.604101,-9.390312,3.213351,-1.842148,-1.304499,-9.027029,-3.603603,-7.477709,6.843873,4.646760,-2.107628,3.873265,-7.822644,8.912336,-0.675443,2.007996,8.068285,7.037089,1.941683,0.651033,-8.296520,-1.779526,-2.850647,8.158992,0.804913,7.932352,-3.333297,3.289836,6.388021,-3.141715,-6.397979,-8.460019,1.761762,-6.547705,7.257961,-3.433681,9.342995,-4.057509,-0.477283,1.726913,-2.093594,8.723703,2.487837,-3.268247,-1.157594,2.753121,-8.050141,-8.926618,1.557760,-7.145096,8.041729,3.316867,5.813880,-9.533437,1.517542,4.519450,-9.602869,-9.225491,-9.292990,-2.864688,-2.679051,7.580560,7.812765,-4.467211,7.759243,6.762377,-4.666140,7.379767,-6.908363,3.577702,-1.183027,-1.097092,1.914817,-2.347135,9.976847,-7.176148,-3.188785,-2.654097,-0.560601,4.108024,4.818279,-9.565806,2.139498,-8.882788,5.081088,5.166760,-4.705324,4.988295,6.024382,7.348141,-5.869988,-1.200761,-5.239105,1.454510,4.433696,-2.887114,7.377594,-2.739417,-1.229878,8.318174,-5.201361,3.609452,-8.820380,8.969997,4.902761,-4.068109,-0.030646,-0.971337,1.834747,9.505117,-7.036391,2.057670,-6.164005,-7.168392,-5.589432,5.250940,0.358808,-1.970731,9.878399,4.681038,-9.751034,-1.743243,-2.767359,2.179338,-6.610325,-8.015870,-4.420004,2.875735,-7.597193,-3.141268,4.873720,4.962535,-6.991949,-2.666034,5.016796,-3.863317,9.492647,6.575696,-2.931822,0.222160,4.126210,0.014056,1.509697,6.647672,0.119983,7.899391,3.276784,9.705126,-5.813799,4.007614,3.133918,3.532476,-9.748380,-4.038108,-6.740907,-4.554198,3.369450,4.624351,-9.286773,-9.414626,-3.643884,-2.251450,6.339706,-0.964923,9.743295,2.546148,3.053484,7.334458,8.904793,-0.701285,0.302859,-0.354879,7.959180,8.109961,-5.152351,9.528858,4.746573,-7.914614,2.897288,-7.317484,-9.669520,9.259057,1.070608,5.250367,-2.374083,-5.240324,-2.460453,-2.529467,-2.246100,3.689983,-8.217908,-1.484298,-4.179452,-5.719475,1.311485,-0.716049,-1.918283,7.812948,-3.533614,6.403903,8.034205,-5.643021,-4.790403,8.362262,6.011932,1.956441,1.932845,6.067678,-4.530130,3.714389,5.350140,5.238377,2.362413,3.048716,7.000903,-2.718933,-1.195651,9.477539,8.117650,9.767017,2.737797,-3.375717,-7.837348,9.499328,9.292399,-9.583300,-6.800070,1.119812,5.325597,-7.988434,0.929754,9.430249,3.176063,-5.358697,9.148335,0.688152,-2.791175,8.202465,-0.542852,4.609460,4.848528,-8.435358,6.227882,0.980569,-4.764042,8.073796,-6.317199,3.543290,1.864478,-7.528795,3.579416,-7.529873,-2.303026,6.412176,-6.962031,-3.315995,-6.613386,9.179575,-7.818848,-7.022699,-6.885256,-8.666814,-0.321832,5.917059,4.666479,-3.587331,4.729215,-3.241323,-0.282970,-5.465808,-4.037160,-0.350285,6.897803,-8.314946,-0.633264,-5.957226,4.422863,4.881517,-2.086066,3.196916,6.232328,7.756338,-2.370324,-2.569808,3.627350,3.301432,6.283778,-2.755745,-0.854588,3.428538,-4.176818,6.341703,-9.426141,3.745654,7.838764,1.524934,6.131438,-2.321629,-5.580507,-4.422829,8.640826,-0.687443,-7.597742,-7.237788,5.131598,7.293828,6.222046,0.440837,-8.151729,8.777749,-1.384241,-9.813305,7.619252,1.739650,3.433547,6.160699,-8.714504,8.710137,-1.697449,2.941168,0.099766,1.402957,0.301977,1.809167,-4.543064,-2.677349,3.311078,-0.067722,2.717804,-5.936571,1.835447,7.289698,5.723232,-0.477018,-5.162213,-1.322402,9.513488,3.181813,-6.338519,-7.243536,8.027102,0.468464,7.754664,4.290191,-5.623221,2.595170,4.531744,6.086874,3.029104,-9.533841,8.674405,-9.495924,1.144325,8.581358,-9.433726,-8.572796,-2.785792,-2.177788,2.429129,-8.656108,4.342796,8.155280,9.302124,-2.314588,1.609642,-8.031940,0.046522,6.862100,-2.589562,-6.245761,-0.387833,-3.734022,4.027817,-7.339836,-7.243705,-0.242498,-4.466999,-2.842960,-1.507743,-6.925830,-0.813153,-1.148042,5.932945,-8.407057,-9.774170,-1.042271,0.536523,-1.015760,1.192144,2.457943,5.673854,-4.000810,2.558244,5.745234,2.569056,4.502303,8.566474,5.759280,4.322834,-9.978203,-5.258876,-7.511648,-5.945865,-0.791996,8.508775,5.032911,0.672754,-4.219283,3.923498,-4.026541,-8.294495,-6.986072,1.613848,-8.985202,4.055876,5.120093,-5.509626,2.137029,-7.956173,-0.468851,3.013378,-7.393673,4.086917,4.762706,0.266901,2.183182,-5.237574,5.242338,8.361656,-2.663619,-8.328010,0.985110,-9.145985,6.469020,-3.527490,-0.741135,-5.120057,1.233906,-6.889467,-8.745272,-9.202199,6.262516,0.179688,8.358062,-4.714430,6.518986,0.019094,3.480976,2.302516,-4.289898,9.730527,3.805390,7.780094,3.012351,6.067860,3.409197,-2.049103,-6.522279,6.541561,-9.844536,-3.888115,2.804128,-0.302283,5.719684,6.764960,-4.102280,-2.031823,-6.871081,-8.258658,8.470958,5.825648,2.416422,6.566815,3.374505,3.378698,5.132580,8.463900,3.743656,9.830665,5.380762,-2.756850,9.084240,3.916839,5.660637,-3.804042,-6.232949,8.629336,4.077002,8.613719,-1.420560,-0.273391,-9.386991,-1.221995,-0.847542,-4.379203,-9.065244,9.515279,-7.872543,-4.791767,-8.600858,-0.944429,-3.395151,-5.519022,5.949586,2.427532,2.993242,0.499140,1.401446,5.537232], dtype = "float64")#candidate|2186|(1152,)|const|float64
call_2185 = func_1403_call(relay.reshape(const_2186.astype('float64'), [8, 16, 9]))
call_2187 = func_1403_call(relay.reshape(const_2186.astype('float64'), [8, 16, 9]))
output = relay.Tuple([bop_2175,call_2185,const_2186,])
output2 = relay.Tuple([bop_2178,call_2187,const_2186,])
func_2202 = relay.Function([var_2174,], output)
mod['func_2202'] = func_2202
mod = relay.transform.InferType()(mod)
mutated_mod['func_2202'] = func_2202
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2203 = relay.var("var_2203", dtype = "float32", shape = (7, 10, 13))#candidate|2203|(7, 10, 13)|var|float32
func_2202_call = mutated_mod.get_global_var('func_2202')
call_2204 = func_2202_call(var_2203)
output = call_2204
func_2205 = relay.Function([var_2203], output)
mutated_mod['func_2205'] = func_2205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_2254 = relay.TupleGetItem(func_1975_call(), 0)
call_2255 = relay.TupleGetItem(func_1976_call(), 0)
output = call_2254
output2 = call_2255
func_2272 = relay.Function([], output)
mod['func_2272'] = func_2272
mod = relay.transform.InferType()(mod)
mutated_mod['func_2272'] = func_2272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2272_call = mutated_mod.get_global_var('func_2272')
call_2273 = func_2272_call()
output = call_2273
func_2274 = relay.Function([], output)
mutated_mod['func_2274'] = func_2274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1369_call = mod.get_global_var('func_1369')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_2281 = relay.TupleGetItem(func_1369_call(), 0)
call_2282 = relay.TupleGetItem(func_1371_call(), 0)
func_2026_call = mod.get_global_var('func_2026')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_2287 = relay.TupleGetItem(func_2026_call(), 0)
call_2288 = relay.TupleGetItem(func_2027_call(), 0)
output = relay.Tuple([call_2281,call_2287,])
output2 = relay.Tuple([call_2282,call_2288,])
func_2292 = relay.Function([], output)
mod['func_2292'] = func_2292
mod = relay.transform.InferType()(mod)
mutated_mod['func_2292'] = func_2292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2292_call = mutated_mod.get_global_var('func_2292')
call_2293 = func_2292_call()
output = call_2293
func_2294 = relay.Function([], output)
mutated_mod['func_2294'] = func_2294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2357 = relay.var("var_2357", dtype = "float64", shape = (14, 15, 16))#candidate|2357|(14, 15, 16)|var|float64
uop_2358 = relay.log(var_2357.astype('float64')) # shape=(14, 15, 16)
func_1956_call = mod.get_global_var('func_1956')
func_1959_call = mutated_mod.get_global_var('func_1959')
var_2387 = relay.var("var_2387", dtype = "float32", shape = (50, 6))#candidate|2387|(50, 6)|var|float32
var_2388 = relay.var("var_2388", dtype = "float32", shape = (24,))#candidate|2388|(24,)|var|float32
call_2386 = relay.TupleGetItem(func_1956_call(relay.reshape(var_2387.astype('float32'), [5, 5, 12]), relay.reshape(var_2388.astype('float32'), [24,]), ), 3)
call_2389 = relay.TupleGetItem(func_1959_call(relay.reshape(var_2387.astype('float32'), [5, 5, 12]), relay.reshape(var_2388.astype('float32'), [24,]), ), 3)
output = relay.Tuple([uop_2358,call_2386,var_2387,var_2388,])
output2 = relay.Tuple([uop_2358,call_2389,var_2387,var_2388,])
func_2402 = relay.Function([var_2357,var_2387,var_2388,], output)
mod['func_2402'] = func_2402
mod = relay.transform.InferType()(mod)
var_2403 = relay.var("var_2403", dtype = "float64", shape = (14, 15, 16))#candidate|2403|(14, 15, 16)|var|float64
var_2404 = relay.var("var_2404", dtype = "float32", shape = (50, 6))#candidate|2404|(50, 6)|var|float32
var_2405 = relay.var("var_2405", dtype = "float32", shape = (24,))#candidate|2405|(24,)|var|float32
output = func_2402(var_2403,var_2404,var_2405,)
func_2406 = relay.Function([var_2403,var_2404,var_2405,], output)
mutated_mod['func_2406'] = func_2406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_2508 = relay.TupleGetItem(func_1426_call(), 0)
call_2509 = relay.TupleGetItem(func_1428_call(), 0)
output = relay.Tuple([call_2508,])
output2 = relay.Tuple([call_2509,])
func_2530 = relay.Function([], output)
mod['func_2530'] = func_2530
mod = relay.transform.InferType()(mod)
mutated_mod['func_2530'] = func_2530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2530_call = mutated_mod.get_global_var('func_2530')
call_2531 = func_2530_call()
output = call_2531
func_2532 = relay.Function([], output)
mutated_mod['func_2532'] = func_2532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_2563 = func_1694_call()
call_2564 = func_1694_call()
output = relay.Tuple([call_2563,])
output2 = relay.Tuple([call_2564,])
func_2572 = relay.Function([], output)
mod['func_2572'] = func_2572
mod = relay.transform.InferType()(mod)
output = func_2572()
func_2573 = relay.Function([], output)
mutated_mod['func_2573'] = func_2573
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2576 = relay.const(5.831923, dtype = "float32")#candidate|2576|()|const|float32
var_2577 = relay.var("var_2577", dtype = "float32", shape = (8, 7, 5))#candidate|2577|(8, 7, 5)|var|float32
bop_2578 = relay.mod(const_2576.astype('float32'), var_2577.astype('float32')) # shape=(8, 7, 5)
bop_2581 = relay.logical_xor(var_2577.astype('int16'), relay.reshape(bop_2578.astype('int16'), relay.shape_of(var_2577))) # shape=(8, 7, 5)
func_1369_call = mod.get_global_var('func_1369')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_2584 = relay.TupleGetItem(func_1369_call(), 1)
call_2585 = relay.TupleGetItem(func_1371_call(), 1)
func_842_call = mod.get_global_var('func_842')
func_848_call = mutated_mod.get_global_var('func_848')
const_2588 = relay.const([9.150277,-3.304895,-4.028124,0.774945,-7.920104,-8.193155,-5.746392,0.026445,-6.005617,0.327725,9.532042,-4.891830,-0.660305,0.008111,4.626900,-7.134324,9.333485,4.971187,-6.363712,9.289373,-5.235627,-4.238642,5.374350,-5.188359,1.277882,7.190183,2.104292,5.861005,-9.434684,7.406638,5.367759,-3.042800,8.610599,-2.269696,9.752128,-2.529452,-0.184197,-9.280322,8.685298,2.402598,-6.979726,7.885940,-2.600145,8.102177,1.789980,6.167320,-5.785601,7.051257,1.779646,-0.327881,1.469322,-6.043422,6.866005,-4.941719,1.080340,7.644059,-6.083905,1.100184,4.351009,1.282098,1.133549,3.598377,1.214695,8.652744,-2.628209,9.215047,4.519992,0.175689,-2.831929,4.265815,-3.947929,-7.283217,6.163262,1.427774,-7.571868,7.518287,0.108373,-6.211428,-6.264542,6.253378,3.275704,-1.881845,-1.325892,0.354559,9.396407,-2.225448,4.419406,-1.374161,-1.658094,3.811967,5.968310,9.115270,0.188727,5.722120,8.382671,-3.329286], dtype = "float64")#candidate|2588|(96,)|const|float64
const_2589 = relay.const([6.758863,-0.093869,9.564567,-4.121335,3.609883,9.582254,-7.131303,6.593520,-8.000647,4.861001,-4.355983,8.774895,5.160675,-4.961502,-6.328678,0.716985,-5.140125,2.991503,-2.161295,-8.914914,-5.121293,-4.028712,-9.801465,-7.565028,-5.110733,-2.945994,-7.473125,-9.609934,6.477308,-6.084849,7.211097,5.568293,-9.325956,4.090020,-5.682395,-8.728536,-1.193926,-9.943914,-9.422284,6.251611,-8.553137,5.607242,6.551031,-6.059946,-0.065667,-2.172399,-1.929439,0.962867,-0.267363,-0.162150,-6.720083,-8.880234,3.597232,8.215874,3.863321,-7.437338,-3.855693,8.744238,2.755450,6.672805,-4.056545,3.277677,6.252506,1.524471,-9.557318,6.232181,7.179946,1.055731,-7.363608,-6.759209,7.067889,6.244767,3.767904,8.331755,-9.028041,-7.367939,-0.717783,-0.539061,4.690228,-2.589424,6.773357,-2.786936,0.760121,4.997675,2.434154,5.418446,-0.531541,-9.134447,7.691121,-3.813189,-8.040023,5.167612,4.189910,6.839410,2.013716,-9.503127,0.087081,0.236025,-9.065348,-5.734380,2.692050,-3.992064,-7.848668,3.020885,-3.635371,7.761701,-9.049005,3.586555,-6.721647,-5.790902,-8.957971,-2.307434,-2.121361,-8.005738,-0.520770,-7.188935,5.744892,7.136166,7.188864,9.424199,5.476263,3.474899,5.724470,0.034131,9.744285,-0.488222,-1.237011,3.352901,-1.569346,3.269604,-1.156406,-8.450379,-6.089067,1.207781,-5.184421,5.752008,2.547399,-5.452676,0.596994,1.379263,0.813871,3.340115,-1.661623,-2.256649,-6.577796,-7.105056,8.345499,-3.575941,-8.000648,-9.844690,9.123211,-8.147778,-5.787336,5.583887,-9.052989,-3.426339,-5.060926,4.471678,-5.370248,-4.112151,1.726819,1.155816,2.683054,-1.967666,6.000032,4.092785,-3.140372,3.219432,-6.416686,3.742103,8.706814,-9.806957,2.246086,0.093672,-2.220567,-6.055359,-1.732737,-5.104163,-3.789895,7.407404,4.823426,-3.852126,7.816564,-2.490985,-2.273846,-4.411042,4.422125,-1.187681,9.556007,-2.527469,7.709020,7.859243,-1.770050,5.192001,9.688598,-2.347726,8.474902,-5.847909,5.090510,-2.504886,-3.697056,3.563549,-6.823327,-7.494130,4.913210,8.952102,-8.957918,-4.762308,-7.844613,3.204903,7.947169,0.562244,-1.241095,8.245224,-8.066235,6.646768,-9.976612,4.608180,-6.106597,-7.215861,-4.256545,-0.338168,7.592871,-7.522748,7.748665,5.788529,6.782567,9.854743,-1.764400,8.481125,2.676653,-7.439491,-7.938008,-5.840517,6.667016,-7.889757,-7.086488,-2.109622,-4.676361,4.525142,-1.641363,-6.105325,5.436482,8.711141,-7.094070,5.841267,-4.284137,3.181704,4.797797,8.507004,5.240039,-8.642657,5.785322,1.630095,3.685778,0.838348,8.748866,-8.797858,7.918606,-8.173167,-5.104557,1.974881,0.356730,4.822959,-5.012310,-5.835114,7.316530,5.362228,7.482957,-9.131814,-4.017634,2.553930,3.096321,-1.148126,4.750966,-3.276892,-5.741121,-7.006832,-6.526320,-8.905014,8.597913,-6.380706,-7.393392,0.723348,-5.372346,-8.026353,8.984805,-5.323989,6.342479,9.503555,-1.682531,3.992656,-6.754121,-6.246692,3.099065,1.149926,8.742727,3.926204,-9.130865,-7.394955,-9.601518,1.488219,-2.545270,-0.422798,-1.902553,-8.906445,4.765118,-0.672684,-7.444731,2.458253,9.431414,-7.557905,-8.125609,-8.506608,-3.419122,-4.742687,-4.702191,-6.723399,2.627685,-2.525797,-6.754621,-9.993691,-8.061297,6.377132,-7.060558,5.626237,-9.406990,-4.698668,3.680054,9.091846,2.708045,7.831824,3.066646,-2.086656,-1.015890,-6.691777,-6.455694,0.737211,1.276472,2.800202,4.964942,-5.763511,-7.477063,-8.248446,0.265254,4.431492,6.584234,-1.991700,-8.166745,-4.259648,-9.463358,4.881557,0.364659,2.872742,-7.458957,-4.810514,1.374976,7.990022,-9.649906,-3.952039,8.241249,-2.594991,-9.294519,6.075563,-1.244773,8.669857,-6.700590,6.761320,4.160456,0.421526,3.596584,8.481943,-8.019398,-1.238288,6.183543,-1.978710,-1.949447,8.344590,-6.057647,6.943063,-0.614763,6.346448,0.853728,6.019831,0.725813,-2.228329,-1.274044,-0.376173,-3.614197,4.465583,4.233655,-2.494008,8.774776,-3.480366,-9.860218,-9.528060,-9.375484,-8.068280,-3.939871,3.771136,-3.597197,-8.450031,7.181926,7.433024,4.742635,9.704147,-6.734985,-2.209247,-0.886501,3.367317,-3.372933,2.636118,9.023619,-8.939323,8.513936,-0.149903,-3.249777,9.575327,8.849311,7.345928,5.000495,9.795930,8.234775,5.955052,-2.696306,-1.903279,-8.932058,3.781584,7.486315,7.772168,1.055724,-2.354635,-1.685127,-3.358840,-2.644643,-0.348186,-8.746236,-1.876975,2.606717,4.036052,-0.423223,-3.899228,-4.420062,6.499485,-2.833017,-4.623587,-1.634859,1.864528,-1.580154,-6.012663,0.461581,1.983438,-7.269676,0.567568,3.981383,5.580426,4.281247,5.399994,3.006310,9.431368,8.399189,-9.353130,5.513517,2.666718,8.457075,-7.460466,-1.322387,-0.207868,1.914266,1.134338,5.897894,2.210892,-4.088857,-0.303148,5.342552,3.216605,8.079495,-4.636457,6.126321,1.820742,1.082272,-2.956808,8.846932,-2.863657,-1.545561,0.101380,-7.526137,-2.269459,1.301023,-0.534412,3.876342,-4.795481,8.992212,9.806727,-9.027589,2.470489,-2.891711,3.015940,4.204535,0.391289,1.752309,0.068168,6.997708,0.502566,-0.126085,5.297053,5.510228,-6.555840,-7.203265,-1.769590,-0.957202,-2.842337,8.976206,-6.003525,4.994719,-2.013064,6.063282,-8.844199,-5.424412,9.276194,2.346918,-9.372830,-4.962614,-3.508515,-6.306217,1.599769,-8.757299,2.254432,-2.647996,-2.033759,4.619407,-7.778106,-4.101223,8.788746,-0.234400,9.033877,0.137228,6.790575,2.144799,-5.751542,-5.315639,-2.923567,5.301671,-9.857366,-9.111840,7.929082], dtype = "float32")#candidate|2589|(546,)|const|float32
const_2590 = relay.const([[-6.132245,-5.863969,2.136889,3.914610],[-0.516106,-3.855247,-8.354668,-0.883936],[6.119298,2.602543,2.876735,5.542107],[7.054550,1.957222,-4.180082,-9.260566],[-1.898807,6.308729,-8.967127,-9.491964],[0.957977,-6.349364,9.073883,-0.429568]], dtype = "float32")#candidate|2590|(6, 4)|const|float32
var_2591 = relay.var("var_2591", dtype = "int8", shape = (24, 8))#candidate|2591|(24, 8)|var|int8
call_2587 = relay.TupleGetItem(func_842_call(relay.reshape(const_2588.astype('float64'), [16, 2, 3]), relay.reshape(const_2589.astype('float32'), [546,]), relay.reshape(const_2590.astype('float32'), [12, 2]), relay.reshape(var_2591.astype('int8'), [192,]), ), 3)
call_2592 = relay.TupleGetItem(func_848_call(relay.reshape(const_2588.astype('float64'), [16, 2, 3]), relay.reshape(const_2589.astype('float32'), [546,]), relay.reshape(const_2590.astype('float32'), [12, 2]), relay.reshape(var_2591.astype('int8'), [192,]), ), 3)
func_842_call = mod.get_global_var('func_842')
func_848_call = mutated_mod.get_global_var('func_848')
call_2606 = relay.TupleGetItem(func_842_call(relay.reshape(const_2588.astype('float64'), [16, 2, 3]), relay.reshape(const_2589.astype('float32'), [546,]), relay.reshape(const_2590.astype('float32'), [12, 2]), relay.reshape(var_2591.astype('int8'), [192,]), ), 3)
call_2607 = relay.TupleGetItem(func_848_call(relay.reshape(const_2588.astype('float64'), [16, 2, 3]), relay.reshape(const_2589.astype('float32'), [546,]), relay.reshape(const_2590.astype('float32'), [12, 2]), relay.reshape(var_2591.astype('int8'), [192,]), ), 3)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_2608 = relay.TupleGetItem(func_1232_call(), 0)
call_2609 = relay.TupleGetItem(func_1234_call(), 0)
output = relay.Tuple([bop_2581,call_2584,call_2587,const_2588,const_2589,const_2590,var_2591,call_2606,call_2608,])
output2 = relay.Tuple([bop_2581,call_2585,call_2592,const_2588,const_2589,const_2590,var_2591,call_2607,call_2609,])
func_2620 = relay.Function([var_2577,var_2591,], output)
mod['func_2620'] = func_2620
mod = relay.transform.InferType()(mod)
mutated_mod['func_2620'] = func_2620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2620_call = mutated_mod.get_global_var('func_2620')
var_2622 = relay.var("var_2622", dtype = "float32", shape = (8, 7, 5))#candidate|2622|(8, 7, 5)|var|float32
var_2623 = relay.var("var_2623", dtype = "int8", shape = (24, 8))#candidate|2623|(24, 8)|var|int8
call_2621 = func_2620_call(var_2622,var_2623,)
output = call_2621
func_2624 = relay.Function([var_2622,var_2623,], output)
mutated_mod['func_2624'] = func_2624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_2631 = relay.TupleGetItem(func_1502_call(), 0)
call_2632 = relay.TupleGetItem(func_1504_call(), 0)
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_2638 = relay.TupleGetItem(func_1761_call(), 1)
call_2639 = relay.TupleGetItem(func_1762_call(), 1)
func_2272_call = mod.get_global_var('func_2272')
func_2274_call = mutated_mod.get_global_var('func_2274')
call_2655 = func_2272_call()
call_2656 = func_2272_call()
bop_2660 = relay.divide(call_2638.astype('float64'), call_2655.astype('float64')) # shape=(7, 10, 13)
bop_2663 = relay.divide(call_2639.astype('float64'), call_2656.astype('float64')) # shape=(7, 10, 13)
func_2402_call = mod.get_global_var('func_2402')
func_2406_call = mutated_mod.get_global_var('func_2406')
var_2687 = relay.var("var_2687", dtype = "float64", shape = (840, 4))#candidate|2687|(840, 4)|var|float64
const_2688 = relay.const([[0.650260,2.079251,0.568387,-6.843176,5.428883,-2.395110,4.090273,-0.868243,-1.639567,2.991584,9.040460,-7.759788,7.828813,2.288056,7.243614,6.742129,1.380538,-5.352187,-1.491940,5.745531,-5.711911,1.069828,7.882661,-0.192234,1.506399,-9.070800,7.901919,-8.101895,-8.783086,0.424865],[-4.819145,-3.968400,2.391648,9.863628,3.080715,1.321865,-0.890024,-4.010206,0.542823,-4.489589,-0.709356,1.135534,6.560580,-2.535271,3.726097,3.204107,6.271319,4.063220,-8.164403,-3.959831,1.877552,9.874146,-4.925562,4.424728,1.025367,4.739291,-5.912878,0.889222,-7.074390,6.267112],[3.334132,1.079146,-7.052505,-2.618725,3.186443,7.110409,-0.957439,1.028594,-9.105935,-6.452352,-3.141368,3.093585,8.028666,-5.472677,-6.992614,3.426611,6.046854,-6.146059,-3.024462,-1.595802,8.052618,-4.108302,1.296737,5.770819,2.847466,5.134910,2.464247,-5.638309,7.153991,-7.771401],[9.646640,-9.913342,-2.267695,-9.214475,9.758343,8.699492,-0.637774,-6.244657,4.104489,4.809632,-7.226708,-6.330491,1.096717,-7.317359,9.539043,2.483322,-0.739603,5.603173,-4.167551,2.671500,3.738079,0.706276,8.516049,2.448241,3.537630,4.788580,1.369995,5.385370,-6.296897,7.810581],[-8.757736,-7.114042,-9.427036,0.917531,-5.268430,-9.930430,2.003256,5.703082,-2.781692,9.741141,-2.430061,5.383021,-3.977798,-0.661166,-7.474792,9.326954,-8.185236,5.958168,0.008987,-2.773671,-8.214586,7.724794,-0.556922,-3.575381,6.046175,-7.296804,-3.153138,9.040889,-7.213387,5.296500],[-8.987268,3.644093,6.651746,6.033978,9.373187,-3.881894,4.145587,-9.301619,-5.403313,-2.650260,-2.498023,1.288056,-3.724510,-6.525737,2.910167,1.707500,-2.334287,-7.160545,8.314021,-4.985883,8.499003,-9.104230,3.937615,-6.436291,0.644394,9.792826,1.642935,-5.311568,-3.366357,-3.429753],[6.916544,8.680058,-3.678552,2.251073,8.296628,7.862605,-8.501505,3.055175,-3.467761,6.008843,-8.585736,3.427819,-6.302672,7.001431,-9.944767,-3.599750,4.740910,7.302611,1.761522,-7.925822,9.053637,-0.224001,5.333440,1.372726,6.124725,-0.108016,4.709113,-0.927578,4.212539,-0.640676],[7.379352,2.819645,-8.828678,8.631730,7.205948,4.781367,0.212241,-1.965219,7.639006,-0.115359,6.938948,5.805614,-2.109779,-5.562633,9.306449,-8.878117,7.826915,-2.789721,-0.943635,5.208379,9.340087,-0.234143,-0.675159,6.523244,-0.817355,0.248892,-4.970537,2.313714,-9.688030,1.801377],[-5.445832,-1.040552,3.914231,-4.917336,-1.622641,-7.270787,-0.875863,-4.655622,5.755476,-3.728576,2.458096,1.724296,-8.528841,0.345438,-3.057936,9.731440,-8.312542,-7.727546,-9.504146,3.774507,3.269574,-0.947943,0.785274,-1.072901,-7.626282,-5.156295,-2.555598,-1.630270,-0.632063,0.665671],[-6.757343,-9.831015,7.527066,-0.556414,0.762468,-3.847208,6.240569,-0.938989,-6.627993,-4.144965,5.595276,-4.543355,-0.327789,2.333039,-8.469797,-4.232740,7.672944,3.900925,7.175033,-0.773192,-3.845967,0.547279,9.555324,-9.392347,6.325861,-2.087142,8.168317,-0.025573,3.304183,7.735774]], dtype = "float32")#candidate|2688|(10, 30)|const|float32
const_2689 = relay.const([[4.343178],[-0.262028],[-3.980282],[-1.020949],[-2.278936],[8.872481],[3.086444],[4.138216],[0.123134],[3.018874],[0.142854],[0.405393],[-1.709469],[-0.544315],[6.687269],[4.106565],[-2.395559],[-6.179897],[-3.677677],[6.502031],[-1.112764],[8.199870],[3.330585],[-2.185729]], dtype = "float32")#candidate|2689|(24, 1)|const|float32
call_2686 = relay.TupleGetItem(func_2402_call(relay.reshape(var_2687.astype('float64'), [14, 15, 16]), relay.reshape(const_2688.astype('float32'), [50, 6]), relay.reshape(const_2689.astype('float32'), [24,]), ), 2)
call_2690 = relay.TupleGetItem(func_2406_call(relay.reshape(var_2687.astype('float64'), [14, 15, 16]), relay.reshape(const_2688.astype('float32'), [50, 6]), relay.reshape(const_2689.astype('float32'), [24,]), ), 2)
func_2145_call = mod.get_global_var('func_2145')
func_2151_call = mutated_mod.get_global_var('func_2151')
const_2720 = relay.const([6,9,-6,-1,-3,7,-1,-10,2,10,-1,-2,1,-4,6,3,7,-5,4,-10,-3,6,3,-4,3,-8,2,-5,-5,2,-10,3,-5,-10,4,-8,6,-2,-10,-6,10,-7,4,-5,-1,-10,2,-8,-4,7,-8,-7,-9,-5,-7,1,-5,-10,-10,-7,2,2,3,-2,-8,-6,-6,-3,4,-5,7,6,4,-10,-1,-5,-6,-6,7,-7,8,3,6,10,-2,-1,-1,-2,3,9,-8,-6,1,3,-1,-5,4,7,-2,10,-4,-4,7,9,-7,-5,-5,9,-6,-4,-3,-10,-4,6,3,-1,-8,3,-2,-7,-3,6,-7,1,-9,2,5,2,-6,9,-6,-8,5,10,-4,-8,1,-4,-1,4,4,-6,8,10,6,-5,10,-5,-5,-4,-1,-7,-8,-3,-7,-1,-2,10,6,-4,-9,-5,2,-4,4,-9,10,-1,8,7,10,-6,6,-2,8,-5,5,-8,9,-6,-9,9,-1,-10,-4,-6,-7,-9,-10,5,7,7,-9,6,8,-10,9,8,2,10,-7,4,-9,-6,4,-9,1,-10,2,8,-2,-6,-2,10,4,-3,4,-4,-10,4,-2,-6,10,5,4,1,-6,4,3,3,1,8,-3,10,1,-1,6,9,-1,-7,10,10,7,3,9,-7,1,-8,6,-2,-4,3,8,6,-6,6,-3,3,4,9,-1,-4,2,1,-1,-8,-3,3,-2,-5,-3,6,9,7,-5,-7,-7,-1,2,-8,2,-6,-6,10,-9,6,-6,-2,-2,-10,-7,1,7,-2,3,-2,3,-2,8,-7,-7,-10,7,-7,1,4,-4,4,9,10,6,-9,-9,-10,-4,-5,1,-3,-9,5,-8,10,6,-5,9,-8,-7,-6,9,3,-4,-4,6,-3,-8,7,-9,-1,-2,-1,10,-8,6,3,-1,-9,-7,-9,-2,9,3,7,-2,7,5,-5,-7,1,-6,-1,3,3,4,-4,-6,-6,7,-1,4,-3,7,-3,8,8,-10,-2,-8,2,6,-8,-9,9,10,6,-9,-2,-4,1,-8,-7,-7,-1,3,8,-1,10,-3,-9,1,6,4,-4,-2,2,3,10,10,8,-7,3,-5,2,-5,10,6,-6,1,-1,-7,2], dtype = "uint8")#candidate|2720|(420,)|const|uint8
var_2721 = relay.var("var_2721", dtype = "float32", shape = (546,))#candidate|2721|(546,)|var|float32
call_2719 = relay.TupleGetItem(func_2145_call(relay.reshape(call_2655.astype('uint8'), []), relay.reshape(const_2720.astype('uint8'), [7, 5, 12]), relay.reshape(var_2721.astype('float32'), [1, 546]), relay.reshape(const_2689.astype('float32'), [24,]), ), 7)
call_2722 = relay.TupleGetItem(func_2151_call(relay.reshape(call_2655.astype('uint8'), []), relay.reshape(const_2720.astype('uint8'), [7, 5, 12]), relay.reshape(var_2721.astype('float32'), [1, 546]), relay.reshape(const_2689.astype('float32'), [24,]), ), 7)
func_842_call = mod.get_global_var('func_842')
func_848_call = mutated_mod.get_global_var('func_848')
var_2741 = relay.var("var_2741", dtype = "float64", shape = (96,))#candidate|2741|(96,)|var|float64
const_2742 = relay.const([[6,7,-9,-6,8,-5,7,2],[10,-1,-6,4,7,10,6,7],[10,-10,2,8,-9,1,-6,3],[-8,9,-1,-1,7,-10,-9,-6],[10,-10,1,2,-2,6,-8,6],[-5,-10,-9,5,-2,10,-1,-10],[2,3,7,-1,-10,7,-6,-4],[9,7,6,-6,6,-10,4,-8],[-10,-10,-8,-8,-10,6,7,6],[7,5,-5,2,1,-10,1,-3],[-1,-10,6,9,2,-1,-7,-6],[-2,8,4,-9,-9,9,-9,3],[-5,-10,10,8,-5,2,8,6],[10,5,1,8,5,2,-2,-3],[-7,-2,2,-8,9,-7,-7,-4],[7,3,-5,10,2,5,4,-3],[-1,-7,-2,-10,-4,-5,1,9],[1,8,5,-6,-9,-1,9,5],[8,4,6,3,2,2,-9,3],[-5,6,8,-8,-4,-1,4,6],[-5,-4,-6,-2,6,4,-5,5],[-8,1,-6,-5,8,5,10,-6],[4,8,8,10,4,-9,-1,-10],[-9,4,-1,-6,-5,-3,-2,1]], dtype = "int8")#candidate|2742|(24, 8)|const|int8
call_2740 = relay.TupleGetItem(func_842_call(relay.reshape(var_2741.astype('float64'), [16, 2, 3]), relay.reshape(var_2721.astype('float32'), [546,]), relay.reshape(const_2689.astype('float32'), [12, 2]), relay.reshape(const_2742.astype('int8'), [192,]), ), 5)
call_2743 = relay.TupleGetItem(func_848_call(relay.reshape(var_2741.astype('float64'), [16, 2, 3]), relay.reshape(var_2721.astype('float32'), [546,]), relay.reshape(const_2689.astype('float32'), [12, 2]), relay.reshape(const_2742.astype('int8'), [192,]), ), 5)
func_1657_call = mod.get_global_var('func_1657')
func_1660_call = mutated_mod.get_global_var('func_1660')
call_2747 = relay.TupleGetItem(func_1657_call(relay.reshape(bop_2660.astype('float32'), [7, 10, 13])), 0)
call_2748 = relay.TupleGetItem(func_1660_call(relay.reshape(bop_2660.astype('float32'), [7, 10, 13])), 0)
func_2026_call = mod.get_global_var('func_2026')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_2751 = relay.TupleGetItem(func_2026_call(), 0)
call_2752 = relay.TupleGetItem(func_2027_call(), 0)
output = relay.Tuple([call_2631,bop_2660,call_2686,var_2687,const_2688,const_2689,call_2719,const_2720,var_2721,call_2740,var_2741,const_2742,call_2747,call_2751,])
output2 = relay.Tuple([call_2632,bop_2663,call_2690,var_2687,const_2688,const_2689,call_2722,const_2720,var_2721,call_2743,var_2741,const_2742,call_2748,call_2752,])
func_2754 = relay.Function([var_2687,var_2721,var_2741,], output)
mod['func_2754'] = func_2754
mod = relay.transform.InferType()(mod)
mutated_mod['func_2754'] = func_2754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2754_call = mutated_mod.get_global_var('func_2754')
var_2756 = relay.var("var_2756", dtype = "float64", shape = (840, 4))#candidate|2756|(840, 4)|var|float64
var_2757 = relay.var("var_2757", dtype = "float32", shape = (546,))#candidate|2757|(546,)|var|float32
var_2758 = relay.var("var_2758", dtype = "float64", shape = (96,))#candidate|2758|(96,)|var|float64
call_2755 = func_2754_call(var_2756,var_2757,var_2758,)
output = call_2755
func_2759 = relay.Function([var_2756,var_2757,var_2758,], output)
mutated_mod['func_2759'] = func_2759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1797_call = mod.get_global_var('func_1797')
func_1798_call = mutated_mod.get_global_var('func_1798')
call_2782 = relay.TupleGetItem(func_1797_call(), 0)
call_2783 = relay.TupleGetItem(func_1798_call(), 0)
output = relay.Tuple([call_2782,])
output2 = relay.Tuple([call_2783,])
func_2787 = relay.Function([], output)
mod['func_2787'] = func_2787
mod = relay.transform.InferType()(mod)
mutated_mod['func_2787'] = func_2787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2787_call = mutated_mod.get_global_var('func_2787')
call_2788 = func_2787_call()
output = call_2788
func_2789 = relay.Function([], output)
mutated_mod['func_2789'] = func_2789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_2888 = relay.TupleGetItem(func_1318_call(), 1)
call_2889 = relay.TupleGetItem(func_1319_call(), 1)
uop_2891 = relay.atan(call_2888.astype('float32')) # shape=(7, 10, 13)
uop_2893 = relay.atan(call_2889.astype('float32')) # shape=(7, 10, 13)
uop_2894 = relay.acosh(uop_2891.astype('float64')) # shape=(7, 10, 13)
uop_2896 = relay.acosh(uop_2893.astype('float64')) # shape=(7, 10, 13)
func_1458_call = mod.get_global_var('func_1458')
func_1459_call = mutated_mod.get_global_var('func_1459')
call_2898 = relay.TupleGetItem(func_1458_call(), 0)
call_2899 = relay.TupleGetItem(func_1459_call(), 0)
output = relay.Tuple([uop_2894,call_2898,])
output2 = relay.Tuple([uop_2896,call_2899,])
func_2912 = relay.Function([], output)
mod['func_2912'] = func_2912
mod = relay.transform.InferType()(mod)
output = func_2912()
func_2913 = relay.Function([], output)
mutated_mod['func_2913'] = func_2913
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2954 = relay.var("var_2954", dtype = "uint32", shape = ())#candidate|2954|()|var|uint32
const_2955 = relay.const([[[-1,2,-3,4,4,-2],[6,6,-7,-8,10,9],[-3,-4,-4,-8,5,-3],[-8,8,5,-4,-10,-10],[-1,2,-10,5,9,-4],[6,-6,-1,7,-7,3],[9,-2,-10,-3,-3,-2],[3,-10,9,-5,-3,-3],[-1,-6,-9,2,-8,4],[9,9,-2,8,-2,-10],[-2,5,-6,-10,1,9],[4,-8,8,-10,-1,2]],[[2,1,-8,-5,5,-6],[8,-2,-3,-1,-4,9],[4,10,8,9,4,4],[-10,-4,8,-8,7,7],[8,-9,6,-6,-7,6],[-10,7,-6,8,9,10],[2,-4,-5,9,9,-8],[7,-7,-10,-10,-9,-6],[10,-8,-4,8,6,4],[-3,5,-10,8,6,-2],[8,7,-10,2,-5,-1],[-1,-4,1,6,-1,-5]],[[-3,10,10,-6,-7,8],[5,7,10,-10,7,8],[4,-1,5,7,10,-9],[-3,-9,-9,-6,-6,-6],[-5,9,-2,7,9,2],[5,-3,-9,3,9,-10],[10,-3,-3,5,5,9],[9,5,5,5,9,2],[2,9,1,8,-9,8],[-9,-1,6,-2,-5,6],[-6,-9,9,-2,1,4],[3,3,-4,8,-3,8]],[[9,6,-8,-6,-3,7],[8,-7,-1,9,3,-7],[-3,8,4,-7,5,8],[8,-8,-9,-5,2,-4],[-10,-8,6,-10,2,7],[4,-8,-7,-2,2,-8],[-5,-8,4,2,6,1],[-5,9,8,3,9,-1],[-2,3,-5,5,-3,-6],[4,5,8,-9,6,10],[5,-6,-9,-3,3,2],[-9,7,9,-3,1,-2]],[[3,-2,3,-2,9,5],[6,8,-7,5,-9,-10],[-6,-1,10,-6,7,1],[-3,-8,-1,-2,-2,4],[3,5,-4,2,7,-6],[7,9,1,-3,3,1],[-6,-10,-5,10,-8,2],[2,-9,-7,4,-9,7],[-3,8,-4,1,-2,-10],[7,-3,-7,-6,-8,7],[-2,-9,-4,-2,-9,-2],[-7,-2,-3,-4,-2,-7]],[[3,-9,-10,8,7,-2],[-4,-7,-3,5,-1,-9],[-9,7,1,2,9,6],[-8,-1,2,4,-6,-10],[-10,-10,-1,-5,3,2],[8,-9,7,-6,2,8],[1,-1,-4,7,-7,5],[8,-8,4,5,6,-10],[-9,-8,6,-4,-9,-5],[9,7,10,6,1,-9],[6,8,-5,-6,7,-7],[9,9,10,3,5,-5]],[[-9,3,7,-5,-3,6],[1,6,6,-8,-5,-7],[10,-4,9,8,-2,-9],[2,-3,-7,4,-3,-6],[2,-5,5,-1,1,8],[7,-7,-8,10,-10,-4],[2,-7,-8,3,10,-8],[10,-10,7,1,7,-2],[6,-4,3,-7,7,9],[8,-5,1,-5,-5,2],[-2,-3,-4,-3,-5,9],[8,4,-10,1,6,-8]]], dtype = "uint32")#candidate|2955|(7, 12, 6)|const|uint32
bop_2956 = relay.left_shift(var_2954.astype('uint32'), const_2955.astype('uint32')) # shape=(7, 12, 6)
output = bop_2956
output2 = bop_2956
func_2960 = relay.Function([var_2954,], output)
mod['func_2960'] = func_2960
mod = relay.transform.InferType()(mod)
var_2961 = relay.var("var_2961", dtype = "uint32", shape = ())#candidate|2961|()|var|uint32
output = func_2960(var_2961)
func_2962 = relay.Function([var_2961], output)
mutated_mod['func_2962'] = func_2962
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2990 = relay.var("var_2990", dtype = "float32", shape = (11, 7, 13))#candidate|2990|(11, 7, 13)|var|float32
uop_2991 = relay.exp(var_2990.astype('float32')) # shape=(11, 7, 13)
output = relay.Tuple([uop_2991,])
output2 = relay.Tuple([uop_2991,])
func_3004 = relay.Function([var_2990,], output)
mod['func_3004'] = func_3004
mod = relay.transform.InferType()(mod)
mutated_mod['func_3004'] = func_3004
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3005 = relay.var("var_3005", dtype = "float32", shape = (11, 7, 13))#candidate|3005|(11, 7, 13)|var|float32
func_3004_call = mutated_mod.get_global_var('func_3004')
call_3006 = func_3004_call(var_3005)
output = call_3006
func_3007 = relay.Function([var_3005], output)
mutated_mod['func_3007'] = func_3007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_3081 = relay.TupleGetItem(func_1502_call(), 0)
call_3082 = relay.TupleGetItem(func_1504_call(), 0)
func_126_call = mod.get_global_var('func_126')
func_129_call = mutated_mod.get_global_var('func_129')
var_3089 = relay.var("var_3089", dtype = "float32", shape = (24,))#candidate|3089|(24,)|var|float32
call_3088 = relay.TupleGetItem(func_126_call(relay.reshape(var_3089.astype('float32'), [4, 1, 6])), 1)
call_3090 = relay.TupleGetItem(func_129_call(relay.reshape(var_3089.astype('float32'), [4, 1, 6])), 1)
func_2620_call = mod.get_global_var('func_2620')
func_2624_call = mutated_mod.get_global_var('func_2624')
var_3097 = relay.var("var_3097", dtype = "float32", shape = (280,))#candidate|3097|(280,)|var|float32
const_3098 = relay.const([6,-8,8,1,-1,-3,6,2,3,-3,-10,-5,4,7,-10,7,4,4,-9,1,2,1,-2,-1,-4,4,-7,-9,10,10,8,5,5,5,-4,5,2,6,-10,3,-1,-8,-5,-1,4,-5,1,6,9,1,10,9,-4,8,-4,-8,5,5,-2,6,-10,-10,-3,6,-8,5,-6,9,-1,-6,7,2,-9,-3,3,-6,-4,-3,-3,-9,7,10,-10,3,-6,-8,2,-5,7,1,1,3,6,-2,-5,1,-5,-5,-9,-6,-7,6,-4,-10,2,9,9,-1,-9,3,4,-8,-6,-3,3,-8,4,2,8,7,1,5,9,4,-7,-4,4,9,8,3,-1,-6,8,3,7,-7,-5,10,-8,-5,-5,7,4,-9,8,-6,6,2,-9,9,-4,-8,-7,-6,-5,2,-2,9,-5,-8,2,-9,-7,10,7,-4,6,-9,-2,-9,-6,7,10,-3,6,-5,5,-7,-7,10,8,3,8,8,9,-7,8,4,-1,2,-8,10], dtype = "int8")#candidate|3098|(192,)|const|int8
call_3096 = relay.TupleGetItem(func_2620_call(relay.reshape(var_3097.astype('float32'), [8, 7, 5]), relay.reshape(const_3098.astype('int8'), [24, 8]), ), 6)
call_3099 = relay.TupleGetItem(func_2624_call(relay.reshape(var_3097.astype('float32'), [8, 7, 5]), relay.reshape(const_3098.astype('int8'), [24, 8]), ), 6)
uop_3108 = relay.erf(call_3096.astype('float32')) # shape=(24, 8)
uop_3110 = relay.erf(call_3099.astype('float32')) # shape=(24, 8)
bop_3123 = relay.less(call_3088.astype('bool'), relay.reshape(var_3089.astype('bool'), relay.shape_of(call_3088))) # shape=(4, 1, 6)
bop_3126 = relay.less(call_3090.astype('bool'), relay.reshape(var_3089.astype('bool'), relay.shape_of(call_3090))) # shape=(4, 1, 6)
output = relay.Tuple([call_3081,var_3097,const_3098,uop_3108,bop_3123,])
output2 = relay.Tuple([call_3082,var_3097,const_3098,uop_3110,bop_3126,])
func_3129 = relay.Function([var_3089,var_3097,], output)
mod['func_3129'] = func_3129
mod = relay.transform.InferType()(mod)
mutated_mod['func_3129'] = func_3129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3129_call = mutated_mod.get_global_var('func_3129')
var_3131 = relay.var("var_3131", dtype = "float32", shape = (24,))#candidate|3131|(24,)|var|float32
var_3132 = relay.var("var_3132", dtype = "float32", shape = (280,))#candidate|3132|(280,)|var|float32
call_3130 = func_3129_call(var_3131,var_3132,)
output = call_3130
func_3133 = relay.Function([var_3131,var_3132,], output)
mutated_mod['func_3133'] = func_3133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_3181 = relay.TupleGetItem(func_1761_call(), 0)
call_3182 = relay.TupleGetItem(func_1762_call(), 0)
output = call_3181
output2 = call_3182
func_3186 = relay.Function([], output)
mod['func_3186'] = func_3186
mod = relay.transform.InferType()(mod)
output = func_3186()
func_3187 = relay.Function([], output)
mutated_mod['func_3187'] = func_3187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2272_call = mod.get_global_var('func_2272')
func_2274_call = mutated_mod.get_global_var('func_2274')
call_3214 = func_2272_call()
call_3215 = func_2272_call()
output = call_3214
output2 = call_3215
func_3230 = relay.Function([], output)
mod['func_3230'] = func_3230
mod = relay.transform.InferType()(mod)
mutated_mod['func_3230'] = func_3230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3230_call = mutated_mod.get_global_var('func_3230')
call_3231 = func_3230_call()
output = call_3231
func_3232 = relay.Function([], output)
mutated_mod['func_3232'] = func_3232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_3410 = relay.TupleGetItem(func_1858_call(), 1)
call_3411 = relay.TupleGetItem(func_1859_call(), 1)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_3458 = relay.TupleGetItem(func_1318_call(), 0)
call_3459 = relay.TupleGetItem(func_1319_call(), 0)
func_2048_call = mod.get_global_var('func_2048')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_3462 = relay.TupleGetItem(func_2048_call(), 0)
call_3463 = relay.TupleGetItem(func_2050_call(), 0)
func_2754_call = mod.get_global_var('func_2754')
func_2759_call = mutated_mod.get_global_var('func_2759')
var_3485 = relay.var("var_3485", dtype = "float64", shape = (420, 8))#candidate|3485|(420, 8)|var|float64
var_3486 = relay.var("var_3486", dtype = "float32", shape = (546,))#candidate|3486|(546,)|var|float32
var_3487 = relay.var("var_3487", dtype = "float64", shape = (96,))#candidate|3487|(96,)|var|float64
call_3484 = relay.TupleGetItem(func_2754_call(relay.reshape(var_3485.astype('float64'), [840, 4]), relay.reshape(var_3486.astype('float32'), [546,]), relay.reshape(var_3487.astype('float64'), [96,]), ), 5)
call_3488 = relay.TupleGetItem(func_2759_call(relay.reshape(var_3485.astype('float64'), [840, 4]), relay.reshape(var_3486.astype('float32'), [546,]), relay.reshape(var_3487.astype('float64'), [96,]), ), 5)
func_2572_call = mod.get_global_var('func_2572')
func_2573_call = mutated_mod.get_global_var('func_2573')
call_3506 = relay.TupleGetItem(func_2572_call(), 0)
call_3507 = relay.TupleGetItem(func_2573_call(), 0)
func_3129_call = mod.get_global_var('func_3129')
func_3133_call = mutated_mod.get_global_var('func_3133')
const_3514 = relay.const([-4.621572,9.917699,-3.152646,7.685093,-0.307661,-3.898032,-5.151757,0.050902,-2.703862,4.328533,8.908674,4.742833,5.798559,-1.188056,5.396176,-2.407132,5.095933,7.105860,-0.796364,6.999282,9.630624,-2.763990,-6.715487,-8.877629,5.892992,0.846594,-5.898338,7.926197,3.437262,-3.912292,7.206609,-0.304360,-5.154304,-2.430528,-7.383532,-8.625857,3.417417,1.165659,-3.736817,-1.867453,7.111898,-1.153748,-9.930686,-4.867427,8.854015,-3.302489,3.675445,5.511239,-7.638228,-4.211238,-1.950149,-9.921723,0.994066,0.139894,-7.789292,0.156097,-8.545312,8.765089,4.504224,-2.504266,-8.456078,2.368291,-4.311589,-8.774485,-3.315642,3.529560,8.639652,-5.878840,-5.787491,-9.035391,2.429536,-0.169428,3.104901,5.685709,0.758522,-0.752751,-7.811259,0.504341,-6.321770,-0.216498,-2.333895,1.501735,2.688196,-9.825420,-1.871052,-6.625858,6.782594,6.871428,-3.891851,1.833713,-1.751081,-9.766224,-0.661612,7.820438,9.439063,9.374530,-2.983728,7.626179,1.112986,2.368758,-7.866673,4.197093,-2.597695,-5.505102,3.813247,2.958276,3.565198,4.258543,6.210583,7.549187,-7.822862,0.731040,6.832890,-9.410645,-6.772587,-2.821556,-7.546653,-3.633816,-0.701457,7.133694,6.580921,-2.390801,-3.586816,-5.995919,-0.998286,-7.197506,-1.982437,6.937983,-1.282123,-7.108735,1.060318,8.636180,9.100951,4.086221,0.474792,7.558332,8.146793,1.002938,9.924270,8.997358,5.558027,-5.616602,2.095418,-4.442939,-1.687731,1.941481,8.790981,6.703153,-2.537955,8.442099,7.782549,-5.760668,-9.686900,8.275263,9.664686,2.214365,-1.495637,4.394465,-3.852797,-4.571974,-8.849259,-2.081419,-4.237908,-1.282039,-6.938828,-8.735779,5.463504,-5.394585,9.186425,4.897888,4.723813,5.348944,4.446234,0.802075,-6.016489,-5.098182,1.173959,1.222491,-6.210387,6.332800,6.005395,-7.245101,-0.840852,-3.232698,-4.249310,2.394322,-4.131959,-8.659702,8.937460,3.328106,7.965091,-2.020132,2.747700,-8.295133,-5.354727,-0.934585,-2.495755,-3.919571,-1.403878,-3.711178,-5.519150,-9.412969,-3.739744,-2.778018,-6.104221,-8.815612,4.821427,8.101655,-7.521557,-5.423264,1.806459,-7.352929,-0.671440,-0.571236,6.116617,9.872039,-1.475686,-7.024983,-9.521801,-8.426617,7.539065,-5.771447,-8.974629,6.912199,-0.854039,3.862602,-4.135005,8.532207,-3.296781,6.177481,-9.798254,4.735316,-5.705100,0.456269,8.792462,-0.977957,-8.152105,9.546920,-0.101318,6.544563,5.589558,-6.790087,-4.449114,-2.711893,6.141691,-9.858025,-7.185876,8.816800,-0.293246,-3.335849,-4.157559,-4.156958,7.409084,6.722917,-6.238008,-8.162573,5.805708,3.328869,-0.055748,-9.361117,-0.798910,2.660892,6.257565,1.125675,-4.475307,1.478732,-6.383595,0.544472,7.509991,6.734620,-6.923444,2.811190,-7.427979,0.113312,-1.115473,1.410945,8.673170,-1.103281,7.574913,-2.014035], dtype = "float32")#candidate|3514|(280,)|const|float32
call_3513 = relay.TupleGetItem(func_3129_call(relay.reshape(call_3484.astype('float32'), [24,]), relay.reshape(const_3514.astype('float32'), [280,]), ), 0)
call_3515 = relay.TupleGetItem(func_3133_call(relay.reshape(call_3484.astype('float32'), [24,]), relay.reshape(const_3514.astype('float32'), [280,]), ), 0)
output = relay.Tuple([call_3410,call_3458,call_3462,call_3484,var_3485,var_3486,var_3487,call_3506,call_3513,const_3514,])
output2 = relay.Tuple([call_3411,call_3459,call_3463,call_3488,var_3485,var_3486,var_3487,call_3507,call_3515,const_3514,])
func_3518 = relay.Function([var_3485,var_3486,var_3487,], output)
mod['func_3518'] = func_3518
mod = relay.transform.InferType()(mod)
mutated_mod['func_3518'] = func_3518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3518_call = mutated_mod.get_global_var('func_3518')
var_3520 = relay.var("var_3520", dtype = "float64", shape = (420, 8))#candidate|3520|(420, 8)|var|float64
var_3521 = relay.var("var_3521", dtype = "float32", shape = (546,))#candidate|3521|(546,)|var|float32
var_3522 = relay.var("var_3522", dtype = "float64", shape = (96,))#candidate|3522|(96,)|var|float64
call_3519 = func_3518_call(var_3520,var_3521,var_3522,)
output = call_3519
func_3523 = relay.Function([var_3520,var_3521,var_3522,], output)
mutated_mod['func_3523'] = func_3523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mod.get_global_var('func_2572')
func_2573_call = mutated_mod.get_global_var('func_2573')
call_3634 = relay.TupleGetItem(func_2572_call(), 0)
call_3635 = relay.TupleGetItem(func_2573_call(), 0)
func_126_call = mod.get_global_var('func_126')
func_129_call = mutated_mod.get_global_var('func_129')
const_3643 = relay.const([5.786513,-2.549132,-4.505118,-3.383283,-2.523791,-5.317516,0.624828,4.658331,-8.131001,6.200639,-1.865227,1.954582,3.181582,2.442112,7.409272,-5.016451,7.929328,-7.949643,-9.809271,-3.818792,-5.048032,-2.577088,0.083403,-4.561993], dtype = "float32")#candidate|3643|(24,)|const|float32
call_3642 = relay.TupleGetItem(func_126_call(relay.reshape(const_3643.astype('float32'), [4, 1, 6])), 1)
call_3644 = relay.TupleGetItem(func_129_call(relay.reshape(const_3643.astype('float32'), [4, 1, 6])), 1)
func_2530_call = mod.get_global_var('func_2530')
func_2532_call = mutated_mod.get_global_var('func_2532')
call_3649 = relay.TupleGetItem(func_2530_call(), 0)
call_3650 = relay.TupleGetItem(func_2532_call(), 0)
func_2048_call = mod.get_global_var('func_2048')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_3660 = relay.TupleGetItem(func_2048_call(), 0)
call_3661 = relay.TupleGetItem(func_2050_call(), 0)
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_3666 = relay.TupleGetItem(func_1761_call(), 2)
call_3667 = relay.TupleGetItem(func_1762_call(), 2)
output = relay.Tuple([call_3634,call_3642,const_3643,call_3649,call_3660,call_3666,])
output2 = relay.Tuple([call_3635,call_3644,const_3643,call_3650,call_3661,call_3667,])
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
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_3724 = func_1694_call()
call_3725 = func_1694_call()
func_2787_call = mod.get_global_var('func_2787')
func_2789_call = mutated_mod.get_global_var('func_2789')
call_3735 = relay.TupleGetItem(func_2787_call(), 0)
call_3736 = relay.TupleGetItem(func_2789_call(), 0)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_3739 = func_1704_call()
call_3740 = func_1704_call()
func_842_call = mod.get_global_var('func_842')
func_848_call = mutated_mod.get_global_var('func_848')
const_3763 = relay.const([[-5.858018,7.183517,-7.816725,-5.595900,5.439522,-8.204488,8.558831,7.293733,0.552036,-1.389194,-9.663344,-5.077637,6.261949,-7.884980,-0.930319,-4.382068,-3.487828,8.904023,-1.489630,0.397537,-3.366307,7.922439,1.104083,7.967363],[6.208135,5.052951,2.930976,-1.706996,5.636952,-9.148429,3.725363,-6.061549,-7.525573,5.153782,3.225304,-9.798195,-2.666690,0.610369,6.341097,-2.830958,-0.203544,-8.999974,9.123974,-3.785188,0.176490,8.075326,1.555980,3.307171],[6.936492,1.095686,6.683750,-3.350573,1.804806,5.982033,-9.131321,7.321464,4.337034,-3.422714,-1.426739,8.313739,-6.509272,8.173667,-5.096325,5.849074,2.269843,1.073207,0.249991,-4.069641,6.487101,3.486749,8.338601,7.991773],[-7.524656,-9.056690,-5.799685,-9.308572,-6.280984,1.121866,-5.922875,-9.012270,2.064183,6.075064,4.852779,2.648413,1.812533,6.097917,0.592122,-9.470257,-6.696326,-0.418090,-7.037923,3.412059,-4.025332,-4.395347,-2.678801,-8.191732]], dtype = "float64")#candidate|3763|(4, 24)|const|float64
var_3764 = relay.var("var_3764", dtype = "float32", shape = (546,))#candidate|3764|(546,)|var|float32
const_3765 = relay.const([-4.655367,-8.881271,-8.818961,9.571834,2.125945,-9.854803,-4.658337,-9.675037,-2.782186,-3.061812,5.475940,-8.718229,-4.126278,3.140672,-0.190078,-6.037740,2.715238,-7.968529,6.683186,6.409748,5.859359,3.102809,3.680772,8.972277], dtype = "float32")#candidate|3765|(24,)|const|float32
var_3766 = relay.var("var_3766", dtype = "int8", shape = (48, 4))#candidate|3766|(48, 4)|var|int8
call_3762 = relay.TupleGetItem(func_842_call(relay.reshape(const_3763.astype('float64'), [16, 2, 3]), relay.reshape(var_3764.astype('float32'), [546,]), relay.reshape(const_3765.astype('float32'), [12, 2]), relay.reshape(var_3766.astype('int8'), [192,]), ), 1)
call_3767 = relay.TupleGetItem(func_848_call(relay.reshape(const_3763.astype('float64'), [16, 2, 3]), relay.reshape(var_3764.astype('float32'), [546,]), relay.reshape(const_3765.astype('float32'), [12, 2]), relay.reshape(var_3766.astype('int8'), [192,]), ), 1)
func_2048_call = mod.get_global_var('func_2048')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_3777 = relay.TupleGetItem(func_2048_call(), 0)
call_3778 = relay.TupleGetItem(func_2050_call(), 0)
func_3230_call = mod.get_global_var('func_3230')
func_3232_call = mutated_mod.get_global_var('func_3232')
call_3783 = func_3230_call()
call_3784 = func_3230_call()
output = relay.Tuple([call_3724,call_3735,call_3739,call_3762,const_3763,var_3764,const_3765,var_3766,call_3777,call_3783,])
output2 = relay.Tuple([call_3725,call_3736,call_3740,call_3767,const_3763,var_3764,const_3765,var_3766,call_3778,call_3784,])
func_3792 = relay.Function([var_3764,var_3766,], output)
mod['func_3792'] = func_3792
mod = relay.transform.InferType()(mod)
var_3793 = relay.var("var_3793", dtype = "float32", shape = (546,))#candidate|3793|(546,)|var|float32
var_3794 = relay.var("var_3794", dtype = "int8", shape = (48, 4))#candidate|3794|(48, 4)|var|int8
output = func_3792(var_3793,var_3794,)
func_3795 = relay.Function([var_3793,var_3794,], output)
mutated_mod['func_3795'] = func_3795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2272_call = mod.get_global_var('func_2272')
func_2274_call = mutated_mod.get_global_var('func_2274')
call_3805 = func_2272_call()
call_3806 = func_2272_call()
output = call_3805
output2 = call_3806
func_3809 = relay.Function([], output)
mod['func_3809'] = func_3809
mod = relay.transform.InferType()(mod)
mutated_mod['func_3809'] = func_3809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mutated_mod.get_global_var('func_3809')
call_3810 = func_3809_call()
output = call_3810
func_3811 = relay.Function([], output)
mutated_mod['func_3811'] = func_3811
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3812 = relay.var("var_3812", dtype = "uint64", shape = (10, 6, 6))#candidate|3812|(10, 6, 6)|var|uint64
var_3813 = relay.var("var_3813", dtype = "uint64", shape = (10, 6, 6))#candidate|3813|(10, 6, 6)|var|uint64
bop_3814 = relay.less_equal(var_3812.astype('bool'), relay.reshape(var_3813.astype('bool'), relay.shape_of(var_3812))) # shape=(10, 6, 6)
bop_3831 = relay.floor_divide(var_3813.astype('float32'), relay.reshape(var_3812.astype('float32'), relay.shape_of(var_3813))) # shape=(10, 6, 6)
func_2272_call = mod.get_global_var('func_2272')
func_2274_call = mutated_mod.get_global_var('func_2274')
call_3837 = func_2272_call()
call_3838 = func_2272_call()
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_3852 = relay.TupleGetItem(func_1858_call(), 0)
call_3853 = relay.TupleGetItem(func_1859_call(), 0)
func_2960_call = mod.get_global_var('func_2960')
func_2962_call = mutated_mod.get_global_var('func_2962')
call_3869 = func_2960_call(relay.reshape(call_3837.astype('uint32'), []))
call_3870 = func_2960_call(relay.reshape(call_3837.astype('uint32'), []))
uop_3873 = relay.acos(call_3869.astype('float64')) # shape=(7, 12, 6)
uop_3875 = relay.acos(call_3870.astype('float64')) # shape=(7, 12, 6)
output = relay.Tuple([bop_3814,bop_3831,call_3837,call_3852,uop_3873,])
output2 = relay.Tuple([bop_3814,bop_3831,call_3838,call_3853,uop_3875,])
func_3894 = relay.Function([var_3812,var_3813,], output)
mod['func_3894'] = func_3894
mod = relay.transform.InferType()(mod)
mutated_mod['func_3894'] = func_3894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3894_call = mutated_mod.get_global_var('func_3894')
var_3896 = relay.var("var_3896", dtype = "uint64", shape = (10, 6, 6))#candidate|3896|(10, 6, 6)|var|uint64
var_3897 = relay.var("var_3897", dtype = "uint64", shape = (10, 6, 6))#candidate|3897|(10, 6, 6)|var|uint64
call_3895 = func_3894_call(var_3896,var_3897,)
output = call_3895
func_3898 = relay.Function([var_3896,var_3897,], output)
mutated_mod['func_3898'] = func_3898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_3937 = relay.TupleGetItem(func_3682_call(), 0)
call_3938 = relay.TupleGetItem(func_3684_call(), 0)
func_2048_call = mod.get_global_var('func_2048')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_3942 = relay.TupleGetItem(func_2048_call(), 1)
call_3943 = relay.TupleGetItem(func_2050_call(), 1)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_3946 = relay.TupleGetItem(func_1318_call(), 1)
call_3947 = relay.TupleGetItem(func_1319_call(), 1)
output = relay.Tuple([call_3937,call_3942,call_3946,])
output2 = relay.Tuple([call_3938,call_3943,call_3947,])
func_3950 = relay.Function([], output)
mod['func_3950'] = func_3950
mod = relay.transform.InferType()(mod)
mutated_mod['func_3950'] = func_3950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3950_call = mutated_mod.get_global_var('func_3950')
call_3951 = func_3950_call()
output = call_3951
func_3952 = relay.Function([], output)
mutated_mod['func_3952'] = func_3952
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3953 = relay.var("var_3953", dtype = "uint8", shape = (2, 9, 11))#candidate|3953|(2, 9, 11)|var|uint8
var_3954 = relay.var("var_3954", dtype = "uint8", shape = (2, 9, 11))#candidate|3954|(2, 9, 11)|var|uint8
bop_3955 = relay.left_shift(var_3953.astype('uint8'), relay.reshape(var_3954.astype('uint8'), relay.shape_of(var_3953))) # shape=(2, 9, 11)
uop_3961 = relay.log10(bop_3955.astype('float32')) # shape=(2, 9, 11)
uop_3965 = relay.sqrt(uop_3961.astype('float64')) # shape=(2, 9, 11)
output = uop_3965
output2 = uop_3965
func_3968 = relay.Function([var_3953,var_3954,], output)
mod['func_3968'] = func_3968
mod = relay.transform.InferType()(mod)
var_3969 = relay.var("var_3969", dtype = "uint8", shape = (2, 9, 11))#candidate|3969|(2, 9, 11)|var|uint8
var_3970 = relay.var("var_3970", dtype = "uint8", shape = (2, 9, 11))#candidate|3970|(2, 9, 11)|var|uint8
output = func_3968(var_3969,var_3970,)
func_3971 = relay.Function([var_3969,var_3970,], output)
mutated_mod['func_3971'] = func_3971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_3990 = relay.TupleGetItem(func_1502_call(), 0)
call_3991 = relay.TupleGetItem(func_1504_call(), 0)
output = relay.Tuple([call_3990,])
output2 = relay.Tuple([call_3991,])
func_4002 = relay.Function([], output)
mod['func_4002'] = func_4002
mod = relay.transform.InferType()(mod)
output = func_4002()
func_4003 = relay.Function([], output)
mutated_mod['func_4003'] = func_4003
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4053 = relay.var("var_4053", dtype = "int64", shape = (16, 5, 12))#candidate|4053|(16, 5, 12)|var|int64
var_4054 = relay.var("var_4054", dtype = "int64", shape = (16, 5, 12))#candidate|4054|(16, 5, 12)|var|int64
bop_4055 = relay.greater_equal(var_4053.astype('bool'), relay.reshape(var_4054.astype('bool'), relay.shape_of(var_4053))) # shape=(16, 5, 12)
var_4075 = relay.var("var_4075", dtype = "int64", shape = (16, 5, 12))#candidate|4075|(16, 5, 12)|var|int64
bop_4076 = relay.minimum(var_4053.astype('uint16'), relay.reshape(var_4075.astype('uint16'), relay.shape_of(var_4053))) # shape=(16, 5, 12)
func_2572_call = mod.get_global_var('func_2572')
func_2573_call = mutated_mod.get_global_var('func_2573')
call_4081 = relay.TupleGetItem(func_2572_call(), 0)
call_4082 = relay.TupleGetItem(func_2573_call(), 0)
output = relay.Tuple([bop_4055,bop_4076,call_4081,])
output2 = relay.Tuple([bop_4055,bop_4076,call_4082,])
func_4083 = relay.Function([var_4053,var_4054,var_4075,], output)
mod['func_4083'] = func_4083
mod = relay.transform.InferType()(mod)
var_4084 = relay.var("var_4084", dtype = "int64", shape = (16, 5, 12))#candidate|4084|(16, 5, 12)|var|int64
var_4085 = relay.var("var_4085", dtype = "int64", shape = (16, 5, 12))#candidate|4085|(16, 5, 12)|var|int64
var_4086 = relay.var("var_4086", dtype = "int64", shape = (16, 5, 12))#candidate|4086|(16, 5, 12)|var|int64
output = func_4083(var_4084,var_4085,var_4086,)
func_4087 = relay.Function([var_4084,var_4085,var_4086,], output)
mutated_mod['func_4087'] = func_4087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3811_call = mutated_mod.get_global_var('func_3811')
call_4095 = func_3809_call()
call_4096 = func_3809_call()
output = call_4095
output2 = call_4096
func_4112 = relay.Function([], output)
mod['func_4112'] = func_4112
mod = relay.transform.InferType()(mod)
output = func_4112()
func_4113 = relay.Function([], output)
mutated_mod['func_4113'] = func_4113
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4139 = relay.var("var_4139", dtype = "bool", shape = ())#candidate|4139|()|var|bool
var_4140 = relay.var("var_4140", dtype = "bool", shape = (1, 4, 4))#candidate|4140|(1, 4, 4)|var|bool
bop_4141 = relay.logical_or(var_4139.astype('bool'), var_4140.astype('bool')) # shape=(1, 4, 4)
func_3004_call = mod.get_global_var('func_3004')
func_3007_call = mutated_mod.get_global_var('func_3007')
const_4146 = relay.const([-7.626678,-1.535971,4.376095,8.364149,-5.558504,0.428571,-8.944931,-4.027525,-3.566658,1.578882,8.896408,1.886763,5.611391,-2.736829,7.767841,4.250923,-2.644988,0.964385,-1.149721,9.312665,-0.620995,-8.921539,2.590133,-4.719190,8.433240,0.312731,-8.157344,4.261176,-1.700377,-2.513261,4.220640,0.667337,0.147058,4.278654,7.299991,5.754277,2.163018,6.165173,-1.057523,-0.015491,0.528605,-7.357450,-2.250010,4.376133,-4.214594,-9.795353,-9.267005,3.392642,4.933940,3.116130,7.687557,-2.421831,6.289998,-6.262672,2.306033,7.884273,-6.554303,-3.158702,2.692135,-2.048557,8.682268,8.397431,-5.523098,5.364556,4.629265,6.940704,3.989829,7.515829,7.143844,0.461849,2.814601,2.031963,-5.069124,-4.052506,0.963177,0.050611,-4.582365,-1.560667,6.511705,-5.065818,4.741780,-8.713924,5.251512,0.136354,2.334054,9.236784,9.094330,-2.726113,-4.150355,2.555630,2.894159,-2.246554,-3.119775,9.814964,-7.719973,-4.195227,2.252800,5.232046,0.433359,3.576055,4.884623,0.092209,4.552853,-7.418709,-2.948006,7.159355,5.892927,4.153755,7.226453,4.613666,-1.217681,6.504274,-1.571544,-8.510721,1.201487,-3.797496,-6.699190,3.322669,-4.733579,9.217965,7.617754,-7.846551,-0.184555,-5.876440,-8.241070,-9.196737,-4.603823,-8.303469,-6.883549,-1.595437,-0.603404,-0.923101,-4.021110,-8.929988,1.558533,0.732860,4.965476,8.240862,-9.328928,6.024239,-5.576030,8.749818,9.972512,4.399043,3.239047,3.845220,6.160653,-9.269409,6.319535,-8.702634,6.954882,8.414769,2.972380,-4.402766,3.304478,9.895361,2.109938,-0.573202,-3.297661,-0.832486,7.472294,-0.377647,7.306121,-9.234499,9.817319,-0.427097,-2.438692,2.751213,-1.504588,3.079166,1.506976,2.186522,-1.022907,1.616440,-8.731573,-1.524408,0.488620,-0.967572,7.021207,2.260537,8.813686,7.571661,-1.774528,3.334446,0.123827,-9.281564,5.539843,0.683748,6.620921,0.052563,2.926621,8.493609,-3.243065,3.411572,-8.256833,-2.255666,-8.757161,8.276483,2.155015,-9.860132,-8.640357,5.311914,-9.645892,4.017215,-9.218461,5.730358,-3.997591,-6.050795,-9.527343,-8.868114,5.830337,-0.026902,5.537995,-5.478148,7.395514,3.225673,1.097097,5.543221,2.830735,8.163965,8.479625,1.257719,5.090959,-1.552476,-8.780866,-1.371862,-6.131409,7.201366,-9.481654,-1.535106,-0.018467,3.560677,-3.359728,-9.499697,4.904684,2.144998,-6.014496,-6.408041,3.370492,-1.242636,-2.913201,5.233355,9.753621,-7.702376,-6.271678,2.629173,-7.322589,-3.295614,-7.038161,-3.099394,-7.358069,-5.359179,5.638992,-2.142355,-9.215631,-8.338273,1.211841,8.876719,-6.967498,-4.918693,-5.272383,-0.887062,0.527678,8.227800,3.413974,6.971201,-4.032848,-3.873178,9.673239,-4.694716,0.463932,-0.972926,-5.834664,-2.418271,7.176070,5.016357,-7.079293,-8.481600,-5.367038,3.251549,9.552390,8.976193,1.480327,1.114410,-8.630281,-2.531597,-9.087292,-8.950022,-0.375415,-5.490367,4.488675,5.473376,2.117058,7.553742,2.667691,8.982140,-9.498312,-0.891099,-1.476883,-6.330419,7.816542,4.843256,0.365536,-5.697661,-7.481046,8.715933,-4.986261,0.064782,-4.755708,8.670494,-0.919610,-5.919778,4.650532,-2.665502,5.016793,-2.261437,3.452105,-6.060303,7.482691,-5.262031,2.279647,-3.193221,-8.429329,6.609027,-7.804565,-2.702274,4.866723,2.983847,-3.241233,3.532489,-1.581052,-0.261019,1.727504,-4.379663,-3.788872,-0.287388,-0.536556,0.789746,-4.515010,3.269777,-1.986035,3.226005,8.999743,-7.198422,-6.291246,5.727040,-3.622460,-2.163858,-2.657653,-8.478233,6.829608,4.572867,9.484281,-9.245565,0.009416,1.912527,-1.785014,-9.045681,5.162627,3.313658,-8.296387,2.426056,-3.591983,-4.511052,-6.034102,8.365816,5.097809,-9.661461,-9.149966,-1.567035,-8.535279,2.876349,5.421481,-0.058510,-4.511981,-3.987926,-7.484169,4.595667,-3.742328,-0.516004,9.767685,-6.044693,-2.699856,9.979062,-3.586823,-1.952729,7.194239,1.351279,6.776502,-3.504531,1.363459,-2.339714,-3.907580,-4.134159,8.923694,8.461935,4.081068,6.191977,-2.105269,-6.752637,7.220243,-9.413854,-0.483289,5.976881,5.482453,2.320956,-3.437562,4.945745,-9.068174,4.819948,-4.744346,-3.134670,4.274292,5.740441,-9.360381,-9.217901,-6.349252,2.116538,-5.076433,3.448016,-2.740840,-8.803887,-8.842277,9.015111,5.047168,9.596594,3.337707,0.871616,0.648205,2.347996,-2.778277,0.805355,-0.196100,8.710564,1.006634,-1.469451,-7.754877,5.775403,-2.681140,3.796886,7.986997,8.766863,-1.511781,8.395976,2.729643,0.194534,-9.917681,7.296909,7.686673,5.108313,6.320803,-6.456100,-7.638513,-0.238399,-6.687660,7.812535,-0.752974,2.957016,2.869406,1.973052,4.604230,3.993968,2.758715,-2.413785,8.694499,-4.278519,2.377514,-5.298497,-2.967517,1.426978,-3.333515,-6.381513,6.981759,7.354937,3.441422,-0.089935,-6.541583,-5.048205,-4.169478,-0.492152,5.282941,-1.782169,-0.999402,-1.157383,2.104411,0.323025,-0.003181,0.377896,0.563833,6.830971,8.941315,0.611640,7.165760,2.529860,-8.752671,2.990204,-0.985556,7.023337,8.318213,7.845634,2.077710,-4.645788,6.677065,0.409729,2.421562,3.792752,-9.829028,-2.089882,-9.807736,0.838676,2.126946,-8.672801,-8.162830,-3.955494,-2.398739,6.884946,6.509298,1.792703,8.748900,2.985069,9.348581,9.737120,-1.818144,5.386248,6.225544,2.364461,-2.005940,9.099953,4.995950,-2.902384,0.483484,3.447252,8.455646,4.495896,-4.719802,2.396753,8.221641,7.700027,-9.589937,0.749020,-8.195446,4.078193,-8.413259,5.929214,-1.187581,7.799639,7.879414,-0.509867,-9.193451,4.994592,2.325852,-6.310294,8.384851,-8.363220,7.711239,-3.752125,-2.735106,-8.741937,-5.895089,1.659348,4.417350,-3.322771,7.082370,3.832852,8.647996,-5.437082,-2.553603,3.104367,1.765663,6.113873,3.517787,-1.340314,4.822250,7.450217,-3.353169,0.078520,0.214949,0.562509,-4.854031,-3.133876,3.875297,-9.370246,-2.787293,-9.028633,1.652219,-8.768785,5.215600,8.757988,7.063367,-1.918862,4.300341,6.675552,0.242796,0.614603,6.252801,3.674457,9.702981,-8.459702,-3.152486,9.054786,7.588417,-1.052999,-2.120930,8.465806,-9.176596,1.432298,0.515657,2.258643,7.992538,4.217097,-0.849249,-8.113815,-9.844682,2.199917,1.968046,6.817246,-2.555193,2.932048,6.310279,-5.217291,-3.773080,3.914242,-1.948730,-7.877749,2.064174,1.108598,4.398533,1.942169,-4.097738,-8.481864,1.346915,-0.076915,4.183567,-5.342357,2.002680,7.522894,5.807123,1.301496,6.293407,1.576994,1.145215,-1.803324,-0.099143,9.847781,1.818560,-7.169164,2.896535,-5.739592,-8.569807,7.236892,-0.292294,5.017127,9.991785,6.111616,0.426391,5.845157,4.378740,9.305186,-0.816544,2.250728,-0.366325,-6.184890,-5.391005,-3.269127,-7.541161,-5.810210,-1.921507,-0.194597,2.191357,-7.173151,-7.428087,6.687466,-8.974585,-2.510248,1.598482,-8.131357,3.631047,3.626606,8.238290,7.562149,3.756296,-7.136260,0.560765,2.781935,2.660998,9.627491,-7.781511,8.677799,5.659522,9.283627,3.111775,-4.369613,-0.596578,0.701035,-8.600717,0.773206,-6.677149,1.971053,-8.780051,-5.947924,9.782498,-0.546180,6.941214,-8.936114,2.217773,8.503654,5.550290,3.097783,-6.267218,6.507442,8.707030,-2.629477,3.373516,-4.920544,8.105791,0.629895,-8.462653,-6.408226,4.933121,5.798672,-2.499004,-3.578388,-9.313841,2.939386,-2.422242,9.665386,-5.927814,1.979271,-4.575455,8.338561,2.010356,-0.918671,-8.858770,8.301679,9.429099,-5.110921,0.485843,5.658955,4.462722,-4.069493,0.097980,9.463134,-5.674149,8.287749,-5.356167,-0.110601,5.764269,-4.640533,6.732674,-1.844509,-4.463114,-1.756507,4.098068,4.414736,-2.518523,-7.606877,-3.403820,7.562541,-1.430154,4.849000,-4.022822,-9.519704,-4.386665,6.521004,-9.176914,-4.689608,5.849788,9.035612,-1.161925,1.464366,-9.123835,-9.759507,5.825796,7.079743,9.883694,1.560850,-7.569853,2.938024,-4.871227,-2.661928,-4.716607,8.727813,7.327866,-3.714815,8.987772,5.546666,9.733339,-3.247466,1.260457,7.870656,-0.852198,-7.155583,-3.764466,9.287854,8.446569,-1.120176,-9.748255,3.280152,-5.594016,7.500068,5.303214,5.775018,4.005517,8.904432,-3.923250,5.931867,3.588643,6.921675,9.221695,-1.312405,0.985439,9.778336,-6.144514,6.649779,-5.807000,4.078634,5.428994,9.406717,-8.586859,-4.403488,4.048153,-2.360221,8.337024,-4.152105,-4.690363,4.017437,7.104492,-0.128219,1.839222,-1.211478,-8.250371,5.854968,4.042529,-5.951800,-6.277145,-5.796798,-0.852901,-9.211450,-2.446624,5.559220,-4.307384,-9.968859,8.287632,3.904449,1.358411,-6.446811,2.356741,1.319274,-1.582275,0.586398,-0.995872,-4.458589,-2.114887,8.817047,-5.186911,7.704526,1.836266,-2.078348,-5.588557,-2.087693,-1.966369,-6.224267,-4.840024,-5.297177,6.510940,7.113271,9.991717,5.533572,2.274779,-5.354455,3.974620,-2.161676,-0.855177,5.095275,-4.538800,-2.804791,-0.556086,1.140500,-1.391797,-5.739491,7.727002,-5.054816,1.580529,-2.248939,-9.706000,-6.405148,-9.014635,-0.774089,-5.482013,-0.964675,7.864585,6.423447,5.108368,5.342151,-8.318954,1.578077,2.044681,-8.726059,4.499377,7.560195,5.900413,9.189969,-4.356740,-1.054324,7.266618,-2.339960,9.931018,0.385540,-7.307060,1.823196,-7.347963,-4.264397,-9.082377,-1.309309,7.978770,5.822865,-1.008091,-1.446056,-4.616296,8.279773,3.332501,5.884265,2.721364,0.954138,2.883528,-4.870475,-9.211906,5.901827,1.682435,-0.989220,-9.906971,5.667615,7.127239,0.338970,1.956530,4.545286,-5.830088,3.348599,2.875187,7.452123,0.420517,-6.000919,-0.254685,-3.013698,-4.019246,-6.913811,-1.780381,1.718433,-7.059722,-6.816280,2.342178,-5.680037,-6.460766,9.358154,8.273022,-9.468899,-4.969155,-7.672610,-6.928542,-1.108409,8.428685,1.520662,-9.950370,9.824831,-5.954082,-7.847182,-5.907971,9.944988,4.605585,-7.297975,-7.393613,2.939285,-2.766695,9.841546,9.144900,0.118685,4.973187,-4.684318,9.918876,-1.752512,3.679908,4.700049,2.045976,-1.303690,6.850859,9.394910,9.691239,-3.462476,-2.066277,0.557154,6.368136,7.063340,4.324028,-9.464619,5.011665,-0.950006,-8.939699,-9.788801,2.260009,-0.605962,-7.255006], dtype = "float32")#candidate|4146|(1001,)|const|float32
call_4145 = relay.TupleGetItem(func_3004_call(relay.reshape(const_4146.astype('float32'), [11, 7, 13])), 0)
call_4147 = relay.TupleGetItem(func_3007_call(relay.reshape(const_4146.astype('float32'), [11, 7, 13])), 0)
output = relay.Tuple([bop_4141,call_4145,const_4146,])
output2 = relay.Tuple([bop_4141,call_4147,const_4146,])
func_4153 = relay.Function([var_4139,var_4140,], output)
mod['func_4153'] = func_4153
mod = relay.transform.InferType()(mod)
var_4154 = relay.var("var_4154", dtype = "bool", shape = ())#candidate|4154|()|var|bool
var_4155 = relay.var("var_4155", dtype = "bool", shape = (1, 4, 4))#candidate|4155|(1, 4, 4)|var|bool
output = func_4153(var_4154,var_4155,)
func_4156 = relay.Function([var_4154,var_4155,], output)
mutated_mod['func_4156'] = func_4156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_4162 = relay.TupleGetItem(func_2912_call(), 1)
call_4163 = relay.TupleGetItem(func_2913_call(), 1)
output = relay.Tuple([call_4162,])
output2 = relay.Tuple([call_4163,])
func_4196 = relay.Function([], output)
mod['func_4196'] = func_4196
mod = relay.transform.InferType()(mod)
output = func_4196()
func_4197 = relay.Function([], output)
mutated_mod['func_4197'] = func_4197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_4224 = relay.TupleGetItem(func_3682_call(), 3)
call_4225 = relay.TupleGetItem(func_3684_call(), 3)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_4226 = relay.TupleGetItem(func_1232_call(), 0)
call_4227 = relay.TupleGetItem(func_1234_call(), 0)
func_247_call = mod.get_global_var('func_247')
func_252_call = mutated_mod.get_global_var('func_252')
var_4231 = relay.var("var_4231", dtype = "float32", shape = (546,))#candidate|4231|(546,)|var|float32
const_4232 = relay.const([7.376374,-4.674830,-1.024290,5.649080,-9.437966,-3.835961,-0.843864,8.765694,4.286148,-0.044639,-4.618192,8.285661,3.191502,-4.026252,4.011098,0.316260,-2.132858,-7.611893,8.338468,-7.251826,-5.552321,0.208601,-7.689063,7.770303], dtype = "float32")#candidate|4232|(24,)|const|float32
var_4233 = relay.var("var_4233", dtype = "int8", shape = (192,))#candidate|4233|(192,)|var|int8
call_4230 = relay.TupleGetItem(func_247_call(relay.reshape(var_4231.astype('float32'), [3, 13, 14]), relay.reshape(const_4232.astype('float32'), [6, 4]), relay.reshape(var_4233.astype('int8'), [4, 8, 6]), ), 3)
call_4234 = relay.TupleGetItem(func_252_call(relay.reshape(var_4231.astype('float32'), [3, 13, 14]), relay.reshape(const_4232.astype('float32'), [6, 4]), relay.reshape(var_4233.astype('int8'), [4, 8, 6]), ), 3)
output = relay.Tuple([call_4224,call_4226,call_4230,var_4231,const_4232,var_4233,])
output2 = relay.Tuple([call_4225,call_4227,call_4234,var_4231,const_4232,var_4233,])
func_4236 = relay.Function([var_4231,var_4233,], output)
mod['func_4236'] = func_4236
mod = relay.transform.InferType()(mod)
var_4237 = relay.var("var_4237", dtype = "float32", shape = (546,))#candidate|4237|(546,)|var|float32
var_4238 = relay.var("var_4238", dtype = "int8", shape = (192,))#candidate|4238|(192,)|var|int8
output = func_4236(var_4237,var_4238,)
func_4239 = relay.Function([var_4237,var_4238,], output)
mutated_mod['func_4239'] = func_4239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2026_call = mod.get_global_var('func_2026')
func_2027_call = mutated_mod.get_global_var('func_2027')
call_4267 = relay.TupleGetItem(func_2026_call(), 1)
call_4268 = relay.TupleGetItem(func_2027_call(), 1)
output = call_4267
output2 = call_4268
func_4277 = relay.Function([], output)
mod['func_4277'] = func_4277
mod = relay.transform.InferType()(mod)
output = func_4277()
func_4278 = relay.Function([], output)
mutated_mod['func_4278'] = func_4278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mod.get_global_var('func_2572')
func_2573_call = mutated_mod.get_global_var('func_2573')
call_4288 = relay.TupleGetItem(func_2572_call(), 0)
call_4289 = relay.TupleGetItem(func_2573_call(), 0)
output = relay.Tuple([call_4288,])
output2 = relay.Tuple([call_4289,])
func_4312 = relay.Function([], output)
mod['func_4312'] = func_4312
mod = relay.transform.InferType()(mod)
mutated_mod['func_4312'] = func_4312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4312_call = mutated_mod.get_global_var('func_4312')
call_4313 = func_4312_call()
output = call_4313
func_4314 = relay.Function([], output)
mutated_mod['func_4314'] = func_4314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2272_call = mod.get_global_var('func_2272')
func_2274_call = mutated_mod.get_global_var('func_2274')
call_4351 = func_2272_call()
call_4352 = func_2272_call()
output = relay.Tuple([call_4351,])
output2 = relay.Tuple([call_4352,])
func_4357 = relay.Function([], output)
mod['func_4357'] = func_4357
mod = relay.transform.InferType()(mod)
mutated_mod['func_4357'] = func_4357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4357_call = mutated_mod.get_global_var('func_4357')
call_4358 = func_4357_call()
output = call_4358
func_4359 = relay.Function([], output)
mutated_mod['func_4359'] = func_4359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2530_call = mod.get_global_var('func_2530')
func_2532_call = mutated_mod.get_global_var('func_2532')
call_4370 = relay.TupleGetItem(func_2530_call(), 0)
call_4371 = relay.TupleGetItem(func_2532_call(), 0)
func_1657_call = mod.get_global_var('func_1657')
func_1660_call = mutated_mod.get_global_var('func_1660')
call_4388 = relay.TupleGetItem(func_1657_call(relay.reshape(call_4370.astype('float32'), [7, 10, 13])), 0)
call_4389 = relay.TupleGetItem(func_1660_call(relay.reshape(call_4370.astype('float32'), [7, 10, 13])), 0)
uop_4399 = relay.log2(call_4370.astype('float64')) # shape=(7, 10, 13)
uop_4401 = relay.log2(call_4371.astype('float64')) # shape=(7, 10, 13)
output = relay.Tuple([call_4388,uop_4399,])
output2 = relay.Tuple([call_4389,uop_4401,])
func_4407 = relay.Function([], output)
mod['func_4407'] = func_4407
mod = relay.transform.InferType()(mod)
output = func_4407()
func_4408 = relay.Function([], output)
mutated_mod['func_4408'] = func_4408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_4442 = relay.TupleGetItem(func_3682_call(), 4)
call_4443 = relay.TupleGetItem(func_3684_call(), 4)
func_4153_call = mod.get_global_var('func_4153')
func_4156_call = mutated_mod.get_global_var('func_4156')
const_4445 = relay.const(False, dtype = "bool")#candidate|4445|()|const|bool
var_4446 = relay.var("var_4446", dtype = "bool", shape = (16,))#candidate|4446|(16,)|var|bool
call_4444 = relay.TupleGetItem(func_4153_call(relay.reshape(const_4445.astype('bool'), []), relay.reshape(var_4446.astype('bool'), [1, 4, 4]), ), 2)
call_4447 = relay.TupleGetItem(func_4156_call(relay.reshape(const_4445.astype('bool'), []), relay.reshape(var_4446.astype('bool'), [1, 4, 4]), ), 2)
output = relay.Tuple([call_4442,call_4444,const_4445,var_4446,])
output2 = relay.Tuple([call_4443,call_4447,const_4445,var_4446,])
func_4458 = relay.Function([var_4446,], output)
mod['func_4458'] = func_4458
mod = relay.transform.InferType()(mod)
mutated_mod['func_4458'] = func_4458
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4459 = relay.var("var_4459", dtype = "bool", shape = (16,))#candidate|4459|(16,)|var|bool
func_4458_call = mutated_mod.get_global_var('func_4458')
call_4460 = func_4458_call(var_4459)
output = call_4460
func_4461 = relay.Function([var_4459], output)
mutated_mod['func_4461'] = func_4461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_4482 = relay.TupleGetItem(func_1858_call(), 1)
call_4483 = relay.TupleGetItem(func_1859_call(), 1)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_4486 = relay.TupleGetItem(func_1502_call(), 0)
call_4487 = relay.TupleGetItem(func_1504_call(), 0)
bop_4488 = relay.bitwise_and(call_4482.astype('uint8'), relay.reshape(call_4486.astype('uint8'), relay.shape_of(call_4482))) # shape=(7, 10, 13)
bop_4491 = relay.bitwise_and(call_4483.astype('uint8'), relay.reshape(call_4487.astype('uint8'), relay.shape_of(call_4483))) # shape=(7, 10, 13)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_4497 = relay.TupleGetItem(func_1426_call(), 1)
call_4498 = relay.TupleGetItem(func_1428_call(), 1)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_4527 = relay.TupleGetItem(func_3950_call(), 1)
call_4528 = relay.TupleGetItem(func_3952_call(), 1)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_4534 = relay.TupleGetItem(func_1502_call(), 0)
call_4535 = relay.TupleGetItem(func_1504_call(), 0)
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_4568 = relay.TupleGetItem(func_1761_call(), 2)
call_4569 = relay.TupleGetItem(func_1762_call(), 2)
func_1657_call = mod.get_global_var('func_1657')
func_1660_call = mutated_mod.get_global_var('func_1660')
call_4581 = relay.TupleGetItem(func_1657_call(relay.reshape(call_4527.astype('float32'), [7, 10, 13])), 0)
call_4582 = relay.TupleGetItem(func_1660_call(relay.reshape(call_4527.astype('float32'), [7, 10, 13])), 0)
output = relay.Tuple([bop_4488,call_4497,call_4527,call_4534,call_4568,call_4581,])
output2 = relay.Tuple([bop_4491,call_4498,call_4528,call_4535,call_4569,call_4582,])
func_4588 = relay.Function([], output)
mod['func_4588'] = func_4588
mod = relay.transform.InferType()(mod)
mutated_mod['func_4588'] = func_4588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4588_call = mutated_mod.get_global_var('func_4588')
call_4589 = func_4588_call()
output = call_4589
func_4590 = relay.Function([], output)
mutated_mod['func_4590'] = func_4590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_4614 = relay.TupleGetItem(func_3950_call(), 2)
call_4615 = relay.TupleGetItem(func_3952_call(), 2)
func_3186_call = mod.get_global_var('func_3186')
func_3187_call = mutated_mod.get_global_var('func_3187')
call_4623 = func_3186_call()
call_4624 = func_3186_call()
uop_4642 = relay.tan(call_4614.astype('float64')) # shape=(7, 10, 13)
uop_4644 = relay.tan(call_4615.astype('float64')) # shape=(7, 10, 13)
output = relay.Tuple([call_4623,uop_4642,])
output2 = relay.Tuple([call_4624,uop_4644,])
func_4659 = relay.Function([], output)
mod['func_4659'] = func_4659
mod = relay.transform.InferType()(mod)
mutated_mod['func_4659'] = func_4659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4659_call = mutated_mod.get_global_var('func_4659')
call_4660 = func_4659_call()
output = call_4660
func_4661 = relay.Function([], output)
mutated_mod['func_4661'] = func_4661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_4689 = func_1704_call()
call_4690 = func_1704_call()
output = call_4689
output2 = call_4690
func_4701 = relay.Function([], output)
mod['func_4701'] = func_4701
mod = relay.transform.InferType()(mod)
output = func_4701()
func_4702 = relay.Function([], output)
mutated_mod['func_4702'] = func_4702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_4703 = func_1694_call()
call_4704 = func_1694_call()
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_4735 = relay.TupleGetItem(func_1232_call(), 0)
call_4736 = relay.TupleGetItem(func_1234_call(), 0)
output = relay.Tuple([call_4703,call_4735,])
output2 = relay.Tuple([call_4704,call_4736,])
func_4754 = relay.Function([], output)
mod['func_4754'] = func_4754
mod = relay.transform.InferType()(mod)
mutated_mod['func_4754'] = func_4754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4754_call = mutated_mod.get_global_var('func_4754')
call_4755 = func_4754_call()
output = call_4755
func_4756 = relay.Function([], output)
mutated_mod['func_4756'] = func_4756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2530_call = mod.get_global_var('func_2530')
func_2532_call = mutated_mod.get_global_var('func_2532')
call_4768 = relay.TupleGetItem(func_2530_call(), 0)
call_4769 = relay.TupleGetItem(func_2532_call(), 0)
func_4112_call = mod.get_global_var('func_4112')
func_4113_call = mutated_mod.get_global_var('func_4113')
call_4770 = func_4112_call()
call_4771 = func_4112_call()
func_3518_call = mod.get_global_var('func_3518')
func_3523_call = mutated_mod.get_global_var('func_3523')
var_4774 = relay.var("var_4774", dtype = "float64", shape = (2, 1680))#candidate|4774|(2, 1680)|var|float64
var_4775 = relay.var("var_4775", dtype = "float32", shape = (546,))#candidate|4775|(546,)|var|float32
var_4776 = relay.var("var_4776", dtype = "float64", shape = (96,))#candidate|4776|(96,)|var|float64
call_4773 = relay.TupleGetItem(func_3518_call(relay.reshape(var_4774.astype('float64'), [420, 8]), relay.reshape(var_4775.astype('float32'), [546,]), relay.reshape(var_4776.astype('float64'), [96,]), ), 3)
call_4777 = relay.TupleGetItem(func_3523_call(relay.reshape(var_4774.astype('float64'), [420, 8]), relay.reshape(var_4775.astype('float32'), [546,]), relay.reshape(var_4776.astype('float64'), [96,]), ), 3)
output = relay.Tuple([call_4768,call_4770,call_4773,var_4774,var_4775,var_4776,])
output2 = relay.Tuple([call_4769,call_4771,call_4777,var_4774,var_4775,var_4776,])
func_4779 = relay.Function([var_4774,var_4775,var_4776,], output)
mod['func_4779'] = func_4779
mod = relay.transform.InferType()(mod)
mutated_mod['func_4779'] = func_4779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4779_call = mutated_mod.get_global_var('func_4779')
var_4781 = relay.var("var_4781", dtype = "float64", shape = (2, 1680))#candidate|4781|(2, 1680)|var|float64
var_4782 = relay.var("var_4782", dtype = "float32", shape = (546,))#candidate|4782|(546,)|var|float32
var_4783 = relay.var("var_4783", dtype = "float64", shape = (96,))#candidate|4783|(96,)|var|float64
call_4780 = func_4779_call(var_4781,var_4782,var_4783,)
output = call_4780
func_4784 = relay.Function([var_4781,var_4782,var_4783,], output)
mutated_mod['func_4784'] = func_4784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4277_call = mod.get_global_var('func_4277')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_4803 = func_4277_call()
call_4804 = func_4277_call()
output = relay.Tuple([call_4803,])
output2 = relay.Tuple([call_4804,])
func_4807 = relay.Function([], output)
mod['func_4807'] = func_4807
mod = relay.transform.InferType()(mod)
mutated_mod['func_4807'] = func_4807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4807_call = mutated_mod.get_global_var('func_4807')
call_4808 = func_4807_call()
output = call_4808
func_4809 = relay.Function([], output)
mutated_mod['func_4809'] = func_4809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4810 = relay.var("var_4810", dtype = "float64", shape = (10, 16, 3))#candidate|4810|(10, 16, 3)|var|float64
uop_4811 = relay.acos(var_4810.astype('float64')) # shape=(10, 16, 3)
output = uop_4811
output2 = uop_4811
func_4815 = relay.Function([var_4810,], output)
mod['func_4815'] = func_4815
mod = relay.transform.InferType()(mod)
mutated_mod['func_4815'] = func_4815
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4816 = relay.var("var_4816", dtype = "float64", shape = (10, 16, 3))#candidate|4816|(10, 16, 3)|var|float64
func_4815_call = mutated_mod.get_global_var('func_4815')
call_4817 = func_4815_call(var_4816)
output = call_4817
func_4818 = relay.Function([var_4816], output)
mutated_mod['func_4818'] = func_4818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4196_call = mod.get_global_var('func_4196')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_4841 = relay.TupleGetItem(func_4196_call(), 0)
call_4842 = relay.TupleGetItem(func_4197_call(), 0)
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_4846 = relay.TupleGetItem(func_1761_call(), 0)
call_4847 = relay.TupleGetItem(func_1762_call(), 0)
output = relay.Tuple([call_4841,call_4846,])
output2 = relay.Tuple([call_4842,call_4847,])
func_4848 = relay.Function([], output)
mod['func_4848'] = func_4848
mod = relay.transform.InferType()(mod)
output = func_4848()
func_4849 = relay.Function([], output)
mutated_mod['func_4849'] = func_4849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_4850 = relay.TupleGetItem(func_1318_call(), 1)
call_4851 = relay.TupleGetItem(func_1319_call(), 1)
func_1403_call = mod.get_global_var('func_1403')
func_1405_call = mutated_mod.get_global_var('func_1405')
var_4863 = relay.var("var_4863", dtype = "float64", shape = (2, 576))#candidate|4863|(2, 576)|var|float64
call_4862 = func_1403_call(relay.reshape(var_4863.astype('float64'), [8, 16, 9]))
call_4864 = func_1403_call(relay.reshape(var_4863.astype('float64'), [8, 16, 9]))
func_3894_call = mod.get_global_var('func_3894')
func_3898_call = mutated_mod.get_global_var('func_3898')
const_4883 = relay.const([7,-10,10,-3,8,1,9,4,-5,8,-3,4,1,5,1,7,-1,2,-2,4,-5,6,9,8,8,-9,2,-4,5,1,9,-5,8,-2,10,-2,10,-9,-8,5,4,-7,-7,-1,2,10,1,2,1,-10,1,-8,-10,10,-3,-1,6,3,-1,-8,6,4,1,7,-3,5,-8,3,-9,3,-7,-8,6,-8,6,2,4,-9,4,-9,4,-1,8,-10,8,-8,2,1,9,-5,-5,-7,2,4,-4,5,8,10,-1,-2,6,5,7,-5,5,-1,8,-1,-6,8,-9,-5,10,-2,8,9,7,-3,10,-1,2,5,-2,10,-1,-5,5,7,7,-8,7,-10,-1,-9,5,-6,-3,-6,-9,-2,-9,1,9,9,1,-3,-5,3,10,-9,-3,3,-7,-3,-7,9,6,-10,-9,-2,-6,-9,10,9,5,6,-4,-5,7,-9,7,-10,7,-7,-9,-9,4,6,-1,5,-4,5,9,10,10,-8,-7,-9,8,-3,4,10,1,5,2,9,2,-3,-5,-5,-2,3,1,6,-9,6,2,-3,-1,-4,-10,-6,-6,-1,2,6,-1,5,-1,3,1,-3,-3,-3,-7,-9,1,-9,-4,8,8,-2,-2,-1,10,-5,1,-4,-6,-1,8,-2,-5,6,3,9,-7,-8,-10,4,-3,2,6,-10,-7,-7,-1,3,-2,-9,-2,-6,-9,-10,5,8,-2,4,8,-2,7,9,-10,5,-9,5,-3,10,7,-1,-5,-2,1,9,-10,-4,10,-4,-6,-2,-5,8,-10,-8,-10,9,7,-4,-7,-10,4,5,-7,-6,-10,-10,5,-3,-8,-4,-1,4,4,8,3,-10,2,-2,-4,4,9,1,3,1,-6,-10,7,6,-3,5,-2,2,-2,-5,-5,4,-6,-9,10,10,4,2,-3,-5,3,-10,-6,-1,9,7,-8,9,6,2,-8,2,10,5,2,-10], dtype = "uint64")#candidate|4883|(360,)|const|uint64
call_4882 = relay.TupleGetItem(func_3894_call(relay.reshape(const_4883.astype('uint64'), [10, 6, 6]), relay.reshape(const_4883.astype('uint64'), [10, 6, 6]), ), 2)
call_4884 = relay.TupleGetItem(func_3898_call(relay.reshape(const_4883.astype('uint64'), [10, 6, 6]), relay.reshape(const_4883.astype('uint64'), [10, 6, 6]), ), 2)
output = relay.Tuple([call_4850,call_4862,var_4863,call_4882,const_4883,])
output2 = relay.Tuple([call_4851,call_4864,var_4863,call_4884,const_4883,])
func_4899 = relay.Function([var_4863,], output)
mod['func_4899'] = func_4899
mod = relay.transform.InferType()(mod)
mutated_mod['func_4899'] = func_4899
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4900 = relay.var("var_4900", dtype = "float64", shape = (2, 576))#candidate|4900|(2, 576)|var|float64
func_4899_call = mutated_mod.get_global_var('func_4899')
call_4901 = func_4899_call(var_4900)
output = call_4901
func_4902 = relay.Function([var_4900], output)
mutated_mod['func_4902'] = func_4902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_4926 = func_1694_call()
call_4927 = func_1694_call()
output = call_4926
output2 = call_4927
func_4928 = relay.Function([], output)
mod['func_4928'] = func_4928
mod = relay.transform.InferType()(mod)
mutated_mod['func_4928'] = func_4928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4928_call = mutated_mod.get_global_var('func_4928')
call_4929 = func_4928_call()
output = call_4929
func_4930 = relay.Function([], output)
mutated_mod['func_4930'] = func_4930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4277_call = mod.get_global_var('func_4277')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_4959 = func_4277_call()
call_4960 = func_4277_call()
func_3129_call = mod.get_global_var('func_3129')
func_3133_call = mutated_mod.get_global_var('func_3133')
var_4967 = relay.var("var_4967", dtype = "float32", shape = (2, 12))#candidate|4967|(2, 12)|var|float32
var_4968 = relay.var("var_4968", dtype = "float32", shape = (70, 4))#candidate|4968|(70, 4)|var|float32
call_4966 = relay.TupleGetItem(func_3129_call(relay.reshape(var_4967.astype('float32'), [24,]), relay.reshape(var_4968.astype('float32'), [280,]), ), 1)
call_4969 = relay.TupleGetItem(func_3133_call(relay.reshape(var_4967.astype('float32'), [24,]), relay.reshape(var_4968.astype('float32'), [280,]), ), 1)
bop_4985 = relay.right_shift(var_4968.astype('uint16'), relay.reshape(call_4966.astype('uint16'), relay.shape_of(var_4968))) # shape=(70, 4)
bop_4988 = relay.right_shift(var_4968.astype('uint16'), relay.reshape(call_4969.astype('uint16'), relay.shape_of(var_4968))) # shape=(70, 4)
output = relay.Tuple([call_4959,var_4967,bop_4985,])
output2 = relay.Tuple([call_4960,var_4967,bop_4988,])
func_4998 = relay.Function([var_4967,var_4968,], output)
mod['func_4998'] = func_4998
mod = relay.transform.InferType()(mod)
var_4999 = relay.var("var_4999", dtype = "float32", shape = (2, 12))#candidate|4999|(2, 12)|var|float32
var_5000 = relay.var("var_5000", dtype = "float32", shape = (70, 4))#candidate|5000|(70, 4)|var|float32
output = func_4998(var_4999,var_5000,)
func_5001 = relay.Function([var_4999,var_5000,], output)
mutated_mod['func_5001'] = func_5001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4701_call = mod.get_global_var('func_4701')
func_4702_call = mutated_mod.get_global_var('func_4702')
call_5006 = func_4701_call()
call_5007 = func_4701_call()
output = relay.Tuple([call_5006,])
output2 = relay.Tuple([call_5007,])
func_5010 = relay.Function([], output)
mod['func_5010'] = func_5010
mod = relay.transform.InferType()(mod)
mutated_mod['func_5010'] = func_5010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5010_call = mutated_mod.get_global_var('func_5010')
call_5011 = func_5010_call()
output = call_5011
func_5012 = relay.Function([], output)
mutated_mod['func_5012'] = func_5012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3230_call = mod.get_global_var('func_3230')
func_3232_call = mutated_mod.get_global_var('func_3232')
call_5075 = func_3230_call()
call_5076 = func_3230_call()
output = relay.Tuple([call_5075,])
output2 = relay.Tuple([call_5076,])
func_5099 = relay.Function([], output)
mod['func_5099'] = func_5099
mod = relay.transform.InferType()(mod)
mutated_mod['func_5099'] = func_5099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5099_call = mutated_mod.get_global_var('func_5099')
call_5100 = func_5099_call()
output = call_5100
func_5101 = relay.Function([], output)
mutated_mod['func_5101'] = func_5101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_5133 = relay.TupleGetItem(func_1858_call(), 0)
call_5134 = relay.TupleGetItem(func_1859_call(), 0)
func_4357_call = mod.get_global_var('func_4357')
func_4359_call = mutated_mod.get_global_var('func_4359')
call_5145 = relay.TupleGetItem(func_4357_call(), 0)
call_5146 = relay.TupleGetItem(func_4359_call(), 0)
func_3518_call = mod.get_global_var('func_3518')
func_3523_call = mutated_mod.get_global_var('func_3523')
const_5163 = relay.const([-6.653017,5.219105,4.976038,-5.753226,6.760704,-0.709708,8.776324,-4.701761,-9.928122,3.394284,-1.387230,3.809544,5.104690,-1.215889,-6.548005,5.477360,5.992775,-4.801948,3.093557,-9.234996,6.943190,-6.955919,-7.374295,-9.661485,-8.748698,0.695750,4.467953,-3.901322,9.689182,-3.969937,3.568979,9.895019,-5.638077,0.002648,-7.994916,-5.470316,-1.909668,8.513402,3.871880,-0.810484,0.549159,-8.761244,-1.932121,-8.230438,6.795803,2.198897,-9.983397,4.872414,-5.454772,7.759326,-8.347536,-0.471454,-1.384944,-3.099403,0.700307,5.052499,-9.892612,-5.399505,-1.076774,4.421874,3.598523,6.940392,6.917568,-5.250742,0.088323,-3.650085,5.582023,7.267639,-6.641530,1.718841,-8.771676,8.667004,-0.695806,8.246221,-7.383433,-0.284582,8.403021,3.149538,7.557172,-0.976468,8.564068,-1.628318,5.594775,2.085570,5.989581,-1.630532,4.118336,0.464371,9.682487,7.716646,4.558710,2.880023,0.782797,2.869282,-8.089126,8.241961,-2.589996,-8.864716,1.739917,-6.924642,-1.251019,-2.326025,-9.236513,9.588896,-9.596022,2.951830,-5.615521,-8.711615,7.389440,-6.695969,0.554906,-0.032395,-9.421334,-7.160624,-3.615396,-7.633570,6.746512,-6.076812,-3.074369,9.802892,-9.260616,-8.353214,0.887228,-3.401448,-8.149535,-2.652596,0.583764,-4.366328,2.856515,6.485744,9.614793,-4.108559,1.804911,-7.000132,-7.557831,-4.460941,-1.641914,6.158673,-8.869352,-6.380460,6.877311,-4.130339,9.867283,-9.776168,7.119498,-2.206798,0.846944,3.749009,-9.829242,5.129775,4.333708,9.416467,-6.134974,8.164355,5.870930,-2.944587,-9.206929,6.486792,1.152898,-1.896481,7.239546,9.653020,6.611764,2.041159,-9.622347,-9.251622,8.376794,9.077760,4.704380,-2.958789,-6.232442,9.614876,0.642338,2.402023,-8.899273,-1.978139,-4.431583,-7.538082,-8.455658,6.468231,-0.145431,8.505864,-5.214205,-4.080180,7.033474,-6.146408,8.456383,6.976069,-9.100331,4.392965,-6.543819,-0.703128,6.436419,3.841866,0.043475,-5.514648,-1.374884,3.996535,-9.155724,-9.435179,-7.378789,0.217292,-9.881437,-9.705713,0.708995,5.310340,3.624381,6.131408,1.292112,3.730228,3.748409,-7.571617,6.802495,-2.971266,4.002178,8.216831,9.380554,0.181366,3.382691,-0.322723,2.929969,2.415297,-6.701115,9.500558,9.899689,-1.933753,-8.440157,-3.414537,-4.229810,5.803139,-9.120974,5.164181,-6.484648,8.188667,-4.463583,-6.316171,-9.504277,7.901443,-9.152780,-2.502790,3.805946,5.952689,4.995075,4.770780,-1.661463,-5.515770,5.946560,2.081857,-1.942948,-6.527695,-9.674200,9.102220,-8.352012,7.168529,6.315780,-5.478648,-9.461852,2.996515,3.325805,9.998321,5.477599,-0.697955,2.382526,-9.044414,5.637348,6.931501,-0.393568,-7.251086,8.482661,0.804542,2.044384,2.375473,4.204372,7.261185,7.175852,7.729841,-2.354461,8.160512,4.230919,-7.247259,-4.263532,-4.476063,-1.395698,0.148925,1.071881,-5.917389,-3.030509,-1.419591,-3.892389,7.324263,1.667966,5.027928,-1.001086,2.977094,-2.975607,-9.014222,4.335971,5.826239,5.450312,2.887505,-3.767867,7.584129,1.134238,-3.164972,-4.539294,9.753982,-7.926037,7.720217,-1.592216,-4.440491,-7.076197,4.108576,-5.198714,8.842963,-6.149789,-7.889265,6.026163,2.766775,5.399259,-7.608495,4.739385,7.006455,-5.488755,2.013068,-1.699958,-9.853343,-7.026590,-6.695486,-3.438932,1.188294,4.557822,7.410000,9.709631,7.796680,8.746318,-8.154202,-9.753041,-1.651386,0.893487,9.148362,-5.271451,-8.882669,7.439443,8.199219,7.843645,-7.215494,-4.364263,2.040803,5.932455,-7.576055,-6.693470,0.447006,2.282442,-0.195799,4.627144,-4.305282,5.378784,8.894293,7.096252,-8.798231,1.918761,3.139910,0.436472,6.933295,-7.135737,1.148758,7.203325,7.298704,-2.517137,2.420177,0.114476,6.502410,-9.984653,4.470482,5.027330,-6.516901,5.443626,-9.211064,-2.668413,0.909581,-9.928119,-2.020919,2.641242,-2.050390,7.115790,-4.733071,2.973658,3.201498,-6.853878,2.228909,-7.074056,-7.862258,-7.892710,-7.261243,-2.238758,2.253422,-6.451671,-1.472930,1.347067,-7.196188,-2.563537,7.721612,-5.014186,-6.486181,1.285200,3.785906,8.192041,3.642570,-0.590628,5.702298,7.426536,9.533704,-6.415614,-5.500884,-6.198530,-4.591613,5.078299,-9.690176,-6.905235,-5.512258,2.320399,5.618165,4.639580,-6.593968,6.816035,-7.905585,-0.681431,-3.590054,-8.078881,-3.359892,9.276823,4.716120,-3.121575,1.481411,-0.045451,-5.334462,9.879503,1.083495,1.846472,-5.243603,1.495816,6.645808,5.891603,-9.771242,-8.806940,-2.863581,7.703746,-7.605514,-1.649595,-0.228631,4.814082,-3.979530,-0.076141,6.296046,3.167590,-4.334173,5.151958,-0.702996,-1.718077,-3.432379,0.920149,-9.785068,-2.397647,-0.839989,-8.439266,-3.234369,6.378208,-8.842864,-1.346728,0.386522,-7.080913,-8.634767,-8.785965,-1.551042,7.588401,7.402568,6.857442,1.560879,8.754345,-0.212231,-3.597393,0.916823,2.285815,2.150521,-7.257209,1.666055,7.746541,-5.045957,-3.801760,-9.156187,3.195112,-4.496240,6.382927,-1.639018,0.381481,1.523658,6.634069,-6.275234,-3.585780,-4.706211,-0.068422,1.607642,2.718623,3.941073,-5.743923,8.084676,-1.170962,7.430746,1.494659,-0.250878,-5.497232,-3.069533,-3.686228,4.953061,9.767150,0.338537,8.316721,0.889307,-1.593126,0.741116,-1.448824,-2.849017,-9.907839,-1.556261,-2.222721,7.407523,-7.819501,-8.083278,-6.179987,-0.208575,-9.947515,1.584678,-7.319624,-3.938063,-6.274267,-6.034614,1.986122,7.118351,-1.865977,2.631503,-1.405878,8.985907,2.454102,5.429279,4.015664,5.160126,-8.972526,-7.594119,4.949357,9.576667,-4.428158,-7.196428,3.053290,5.524534,7.235167,-9.200606,6.135164,4.889025,4.642906,-5.443748,-1.321525,-6.406783,1.533050,7.382652,-8.597999,-0.224195,-9.835520,-3.532278,-0.346195,6.942067,-1.806806,1.017491,-6.166457,-1.463388,5.269475,-0.262454,-8.666790,-9.566123,7.201280,-0.663285,8.945118,-9.494910,7.512118,4.252908,7.557370,-8.274849,-9.948729,4.793997,-5.810654,-4.221216,2.213384,0.298886,-9.337996,9.416983,4.556880,9.472224,-5.369001,1.410566,-3.552664,0.408997,9.615940,3.249486,4.027618,-2.532510,6.108698,6.216287,-7.781571,-5.288138,7.726715,-7.550268,-5.332150,2.774406,-4.045362,-6.174069,1.779695,-4.016986,8.699172,-6.424020,-9.663142,-7.010309,6.685273,-3.893733,-3.739025,-2.905240,-5.533369,4.148496,-4.700031,0.682840,6.170843,6.715519,1.608307,8.665294,-9.954307,7.058734,2.342821,-0.781985,-5.413608,-0.199916,5.665897,-1.672390,0.108910,-5.072923,-9.251397,-6.852294,-4.636545,-3.034222,3.480859,-1.645681,1.856722,7.681756,-5.532339,9.207773,-0.763830,3.656278,1.240662,-1.956817,1.405544,-5.346427,-9.106860,0.282194,2.790702,2.513710,-9.443547,-2.194347,9.187344,-1.104715,8.099693,-7.961453,7.235703,8.159357,2.141169,4.697016,6.700403,-9.485845,8.500213,-3.305187,6.545002,5.480981,5.721833,1.435092,3.916077,-1.993896,-4.195730,9.478917,8.304503,-8.745847,-4.062051,3.568035,0.876307,6.188059,-0.632611,5.921482,3.434561,0.713203,-3.056081,-8.516177,-5.254115,-9.037026,2.030693,-1.251232,6.437793,-5.732907,-2.002681,8.762244,9.911050,-8.577815,-9.979353,-8.347976,0.932920,-4.324963,-0.711153,8.707655,-4.847177,1.372588,7.514345,-6.203924,-0.826731,-2.458473,-2.296244,4.729944,8.601843,2.201930,6.847736,6.220117,7.490871,4.813352,-8.883928,-0.974928,-6.859118,2.061899,2.377458,-5.570645,-8.496506,4.889048,-4.406668,-0.972602,-4.756884,7.177523,3.870665,-5.969334,5.745586,8.572574,6.929483,-3.788154,9.461165,7.140419,1.961732,4.320650,9.252177,-5.606828,2.070986,6.476162,3.340876,7.314552,3.718389,0.978817,3.552028,4.203612,0.728710,8.435011,5.493197,4.557986,-1.063693,-1.885633,4.526259,-3.889443,0.490848,4.669812,-5.048796,-4.354780,-5.589968,-1.679415,-7.788137,-3.516031,3.937635,-2.997371,9.839125,9.263770,-6.146692,8.223592,2.402714,-7.457484,4.100284,9.319101,8.621526,9.461168,6.027382,4.211026,6.446931,0.429731,0.785171,6.887258,-5.885685,7.245464,-8.427713,-9.937783,-4.164229,3.890858,-7.923239,6.804002,-8.851944,-1.046029,7.599790,1.457964,5.840098,5.778428,-3.618805,3.488951,-8.953414,-1.887961,7.562172,-9.174854,9.142561,5.053125,-3.820317,4.149058,-5.723709,-9.604620,-0.215026,-7.378885,0.579909,-1.246321,3.630402,-8.661474,-7.126122,-0.813051,5.554700,3.938653,-3.164108,9.932382,-5.445821,3.788896,-0.148045,-2.375061,5.112026,-0.273560,-5.460649,1.843031,9.031870,8.604127,-4.800403,7.707388,-4.490081,-3.871851,-2.899761,1.770790,3.601179,3.445177,6.534878,-6.571032,-8.808447,2.602895,2.108375,-0.717056,-6.733610,7.780975,-0.359581,-8.007348,3.411467,9.440519,-6.541499,-7.320187,-3.783145,0.344122,4.669116,-9.504627,8.177842,3.317705,-7.945299,4.693316,6.974489,2.708461,0.305749,1.492748,2.329112,-2.563666,6.398638,5.577092,-7.443478,8.063925,-4.606343,-7.177831,9.074388,-4.343717,0.738253,-6.414585,-3.320455,-6.009831,-4.311788,7.609104,4.898649,5.479215,-8.857746,-8.044900,-9.711477,9.866175,4.520125,-9.829760,5.507711,6.635761,-7.170189,4.974520,9.255980,-7.403238,0.393476,3.631105,-3.251246,-7.461940,1.788355,9.435498,-2.666044,-9.196438,-8.983076,5.712611,-9.527758,1.124840,-8.547600,4.074080,-5.003021,4.406962,5.391526,-6.658618,-6.726016,7.993796,9.724796,6.419364,8.293724,-3.244631,-8.512549,3.735039,-5.953496,9.944314,9.625512,-7.949542,-9.395454,-0.442170,0.974461,1.188317,4.107167,4.207423,-6.980389,-3.705358,9.887894,4.929401,-3.339029,-5.833498,1.635015,-7.271211,-4.453224,7.693756,-8.195758,9.052143,-5.285449,2.708093,0.953062,4.515825,1.979099,7.143725,-6.241944,-2.763425,6.371515,2.704567,-2.720088,1.349298,-2.860081,-0.238091,-3.736355,-3.424549,-8.210161,-0.064518,4.642893,7.968081,-6.234938,1.423059,-7.222018,8.371502,-4.171241,-1.040682,-4.481057,5.939798,-4.584583,-0.101979,5.952630,-7.647631,-7.217683,3.628110,-2.211414,9.626199,5.803552,9.312757,-5.491188,2.281104,4.967951,-1.299727,-2.023601,-1.081595,7.681085,0.121559,-9.167346,-7.588772,6.232691,-9.608096,5.570781,-4.231924,-6.412030,-5.197949,-4.163168,4.085731,2.295073,-9.063272,4.259688,0.537105,0.764231,-8.435996,-3.973359,-5.687294,-0.805765,3.523128,-6.493490,2.306171,1.290912,-3.469613,5.398722,5.967977,3.024598,-6.308405,-3.235931,9.784191,5.821833,5.165555,-1.862221,8.523249,-9.361992,-6.884601,-4.033859,8.372920,7.293162,4.435701,6.836983,-0.033074,-7.485911,-3.658094,-4.594935,-1.164006,0.211309,1.741055,-7.880346,-7.191486,5.148849,0.537579,-7.131033,2.197821,-9.339700,9.973561,1.905738,-9.973692,-5.397965,-5.580130,-2.647228,-0.368241,8.405546,-0.761106,-3.349453,-7.846287,1.122433,3.475544,3.082954,-4.992347,-0.226971,7.449241,5.790075,4.188482,-4.928355,-3.411954,4.073534,-9.492737,-7.452904,-3.662584,-0.234190,-6.772204,-8.796114,5.528480,-3.977104,-5.513901,8.330511,-2.691808,5.953712,8.453389,6.829300,5.640497,-6.187099,3.681896,-3.011250,-5.628892,2.881731,-0.671901,-8.090094,7.616925,3.005612,2.617463,2.134968,4.471438,-1.829478,3.237212,-5.507689,-0.684485,-2.910085,4.926400,2.299349,9.216202,-9.826994,-7.796975,-8.445714,8.145323,9.900788,-4.800694,-4.097189,-1.599135,-0.908245,8.717786,-3.935044,-9.941025,8.644046,4.787841,8.560554,5.811648,-6.254379,-1.182087,6.428387,6.708434,1.150708,-7.900313,5.382236,-1.320796,-1.476410,8.257318,9.114770,0.319629,8.277229,4.142752,-8.093160,3.229971,-0.830255,5.539252,1.299703,3.916991,-2.372409,3.493935,-2.575029,-5.060873,5.261273,7.008342,5.308434,6.974676,8.883849,9.592721,-6.847052,-1.120080,-3.193374,-6.487164,-1.089072,-1.362789,2.101634,5.516449,8.781757,-0.473755,7.192157,4.684802,5.989956,9.109185,4.402971,-3.385776,4.920641,6.242841,-4.234742,-9.730087,1.897036,4.548702,-0.840839,-9.322217,-9.848941,-1.010737,-8.375892,-6.111077,-9.486923,-3.220560,-7.479230,1.750198,5.272162,-1.829589,3.758663,7.287900,1.399954,6.722299,9.647141,-8.475159,3.968232,8.371615,-5.860501,7.721492,4.771947,4.138331,-6.730319,-2.805883,4.343911,3.930612,6.808888,4.451325,1.167486,-6.905824,-9.982415,9.248145,7.589708,5.858359,-2.373348,-6.061924,-5.038167,-7.902346,7.714969,-9.642510,7.348678,6.869961,-6.203305,2.507626,0.725549,-0.554068,-5.222322,2.257320,-6.420741,-5.893567,7.357696,6.600983,-4.611965,-6.853037,-2.919441,-6.184090,-3.675696,-8.298747,-3.707434,1.213366,0.823778,2.990092,2.902205,1.467240,7.553611,-6.158402,-9.619765,-4.180758,3.751752,-0.690935,1.467318,9.372887,-4.796536,9.409443,-2.011093,7.745438,-2.629022,5.861812,0.809684,-1.885378,-5.577966,-5.846345,-2.794922,6.719594,5.336940,8.213577,-2.144515,9.036084,-7.741839,8.882922,8.031784,-6.938628,2.001873,6.545800,-3.823898,3.351891,-0.323492,4.258716,-0.251544,8.033328,9.710976,7.986055,5.809250,-3.344015,8.353744,-2.642833,-6.833252,-6.442095,9.112224,6.832189,0.871869,-2.475003,-7.959766,-5.365296,2.624714,-7.928735,-2.035763,-0.007044,-6.340336,2.821016,2.188526,-6.553230,-8.114988,6.585234,-5.887275,8.826446,-5.411044,-3.542844,-3.274435,1.887056,-7.404785,-6.635102,4.580835,-7.077558,3.041693,7.992282,-7.710735,6.332903,3.597348,-1.048356,4.504833,1.063923,6.948913,-0.108331,9.418983,2.838260,6.990514,-8.167412,9.408956,9.375893,8.591758,1.711300,-8.180032,-7.321309,2.054872,-1.597875,4.590035,-7.449956,2.151265,-5.289718,9.200392,-0.945712,2.342152,9.850102,6.742094,4.783112,-6.824502,-4.552035,4.771947,-0.530806,3.695926,8.437470,-0.963108,-2.154941,-1.829812,-2.697501,-5.679738,1.967643,-7.025234,-5.780061,0.757669,-2.901207,-4.126233,-3.896648,9.347241,6.433955,8.664515,7.911606,-9.908740,9.891220,-7.621319,-3.164719,-1.566580,-7.108029,5.228021,1.611610,6.633178,-7.780441,-8.664974,9.120440,3.776190,2.360593,-1.470783,-0.168967,-4.629825,7.378167,-7.493778,4.264192,3.615052,4.012540,1.590235,1.281296,-0.650664,-3.162847,5.436081,-2.940031,-1.779279,2.952588,7.827446,-5.380348,-4.869198,-5.017901,6.424970,0.333295,-1.975980,3.405418,6.895687,-6.315375,-1.610361,8.613543,-5.658930,-3.598928,2.454800,7.669794,-7.299610,-9.893558,-3.996369,9.990159,-3.436394,-1.975580,6.896940,-4.987921,0.055405,-9.142169,-9.056324,5.449596,6.979511,1.125948,3.499121,2.910638,-6.152224,-3.632694,7.154150,8.198048,5.031562,-9.455669,1.035785,0.557259,3.669111,1.019673,9.678473,-0.790952,-9.077445,9.500487,2.723554,2.033080,-2.069160,-5.174957,4.353876,-1.028427,4.736943,6.686491,7.764607,7.191831,-1.254201,-7.193369,7.055565,0.458794,2.808843,-9.690098,8.842928,-9.107296,0.074966,3.389395,-0.475388,8.461540,-3.490727,8.269553,-6.525154,-7.741385,9.517029,-2.181682,-5.110927,-7.336766,8.174411,-9.970353,6.499282,-3.900060,6.194352,6.753318,5.069914,3.651377,-8.600146,-1.703846,-9.994478,6.486950,4.717180,-6.334548,9.694340,3.523005,0.393585,-5.604909,2.408887,-0.234143,-9.742127,-0.324283,-9.839061,-2.729870,-0.842356,0.699435,9.153018,-2.497852,2.379552,-0.301039,-3.433742,3.665120,8.407196,-1.789635,-8.854140,1.568338,-5.671361,5.132451,-6.452011,8.399688,-9.683427,5.803210,-4.967339,-2.797863,-6.582475,-5.368505,7.644283,2.056808,8.945003,3.019514,-9.908011,5.138359,-7.626668,9.640348,-6.587323,-5.777719,-7.553436,-0.834977,0.477087,-6.232061,-9.206369,-7.363115,-7.504043,-0.731222,6.575497,7.103702,4.853333,6.655367,1.491682,-1.514470,0.421209,-0.490620,-6.430948,-9.331043,-1.588321,4.656416,-3.626650,-8.320023,5.634733,-7.196289,-9.424608,-0.915891,-4.616044,9.244150,7.056136,0.785027,-7.709146,-2.719305,9.781407,9.759849,7.724599,-3.440849,-4.223699,-4.027652,2.651249,0.262370,-5.090406,7.536252,8.104021,4.980011,-7.233865,8.207686,-4.790089,3.112907,5.258346,8.655508,-6.215942,-3.657399,-6.426090,-7.303314,3.211707,8.954222,-2.699198,4.562259,-3.969126,-8.171974,4.809613,1.626960,2.701713,7.749647,2.592131,7.385938,-1.486962,1.634278,-0.293500,2.828417,4.830771,2.858433,1.711824,0.016325,5.938580,4.397210,6.334999,2.751020,3.630444,6.314054,4.157741,-1.546456,-8.170269,6.762896,-6.949714,6.310102,6.262937,2.328069,3.741774,-3.333497,-9.502226,8.576427,8.470826,-7.980645,-1.801193,8.816137,-1.845238,1.210732,6.550896,3.980661,7.146349,8.720825,5.264676,-8.670205,4.086664,-6.016614,-9.281801,-5.808704,-7.744672,-6.589195,-5.388201,-3.534521,-4.333097,-9.095654,-9.974419,6.669862,-1.177710,3.697961,4.060986,-9.583917,-0.151503,-9.171411,-3.941143,-3.360741,1.485863,8.888109,3.097959,-2.131805,-5.581907,8.349150,-9.381012,-6.222522,-2.344385,-0.106133,7.700082,-6.269564,3.831544,-1.791341,2.078313,-5.604951,-7.494319,0.146668,-6.425666,6.332558,-2.466760,7.083726,7.371911,0.894675,5.823211,2.501932,-8.099962,7.058392,-0.981185,6.007647,-8.938189,-0.857471,-9.948369,-9.978183,9.621979,0.553056,7.388085,-5.695883,-3.365917,-8.080096,2.917375,6.434808,7.012032,-2.618258,-1.061821,-1.544819,1.492498,5.451678,-3.913933,-3.675834,1.179475,7.035296,0.101420,3.836630,6.583929,6.732066,3.209732,-2.324126,2.357078,-0.930008,-5.073682,3.674704,3.724830,1.601001,-6.004250,7.005713,7.503890,-9.581705,-9.047647,4.607843,4.837637,3.665514,3.926546,-9.748655,-4.800547,-4.208522,0.054511,-9.865764,7.499970,-6.659874,-4.701258,5.724969,-6.063637,-8.111992,-3.867154,-5.386807,-8.483601,-3.204717,8.396608,6.928970,-9.083251,-2.614502,4.313049,-6.688915,4.625952,-1.523451,1.083523,2.510900,-5.142078,-9.560488,6.651407,-4.631047,-4.302806,9.334990,8.826350,3.638350,1.028496,0.568750,6.020270,5.174891,-5.431379,-0.867511,2.655396,9.418684,1.589612,-1.614656,-9.974003,-9.479826,-4.047853,-2.848733,-1.656821,8.611846,-3.583951,-4.820475,-4.530522,-4.211355,-1.305307,-6.260895,-4.350560,5.874898,-7.199857,3.476687,-1.893452,8.932183,0.264866,4.724363,-1.687206,8.746759,5.628664,-0.214748,8.441639,2.767892,4.138666,-2.066997,5.983479,4.159688,9.547313,8.326474,-0.835503,-3.017547,-5.833083,-8.708653,-4.936472,1.412302,8.552278,-2.799734,-4.305799,-6.647513,6.715022,-2.025772,-3.592687,-5.020989,-5.099486,-6.494429,1.950050,-8.231773,-0.271870,-3.703560,9.618668,-0.260834,2.455561,3.763292,-8.196669,4.001621,-1.547715,4.498534,4.437232,4.264093,3.453663,-9.113506,-8.735710,-0.202538,0.489209,-0.729384,5.142097,-5.116541,4.131182,-6.017821,5.248379,3.795186,8.935241,7.827285,2.382769,-3.807493,-0.310399,7.078288,-3.766718,3.795864,-7.566567,-5.286434,-0.168577,-1.720889,-8.654557,-6.344256,-0.639430,-4.827355,-7.155754,-7.643969,-4.877109,-0.798355,0.320030,4.064780,3.841768,-6.983128,-8.507261,0.073282,0.643627,-6.361437,9.105402,5.858769,4.187792,5.946271,2.496864,4.470600,9.280565,-8.496044,6.653321,-4.713054,-2.312723,-3.786750,1.599327,-5.629851,1.710114,-4.124536,9.480312,-6.294504,7.250772,-9.301326,7.456853,-3.274784,3.417990,5.389027,4.718130,4.136594,-3.135561,-3.295357,-5.275124,-8.010993,-9.068549,-1.198343,8.792917,-7.622571,-4.339822,4.277625,-0.570979,-6.965730,3.711365,-2.456151,4.882750,-7.531031,7.295975,6.665144,2.481657,1.714691,0.468775,4.760643,-0.161208,4.149786,-5.202380,-6.510861,9.083675,-5.830947,-5.328578,5.016716,0.895004,-0.891144,-6.105367,-3.443471,9.465044,6.334062,3.495082,4.032724,-8.910945,-1.262488,-7.077065,7.502504,-0.851669,-1.847252,-8.137177,-7.179391,2.521759,-9.036199,6.955164,-8.507155,-7.726541,5.364607,-3.292211,8.359984,3.852334,-2.044380,-8.958310,8.996313,4.174543,-8.945033,3.834414,4.645695,0.890320,1.231887,-3.426128,7.996667,2.074557,-6.664181,-3.497572,0.307355,-6.747473,4.224737,7.975666,6.538849,-0.147071,5.523895,-4.178914,-5.607927,-1.627832,-6.146189,3.329476,-2.655501,-8.321802,8.246319,-5.700920,7.864774,-9.497579,-0.982105,2.548886,-3.532536,5.706074,-4.131146,8.121100,0.085452,-3.552337,-7.127289,1.585519,-1.285619,-5.770181,-8.387946,-5.508394,1.692191,-4.398263,8.313217,9.708868,3.499874,9.461420,-5.287008,5.427466,-2.320011,-5.761843,8.394264,4.914964,2.894855,0.130059,4.851176,6.576521,-2.627900,-0.470930,-1.338863,-7.536289,-7.811818,7.854874,-4.023688,-9.123583,-8.723636,8.976558,-7.762556,1.027541,-6.968517,-0.429137,3.551733,-1.497517,3.970366,7.695010,-9.912427,-6.741193,8.022736,-1.286422,-0.672750,-7.190157,5.467191,-7.687354,4.705420,6.148637,7.945081,6.123935,-8.390846,-4.187523,-6.820733,8.188297,2.610001,7.393560,7.390706,-9.045346,-3.698952,-9.859159,7.687765,6.888629,-4.444472,-9.880454,-3.409468,-4.334050,-6.148500,4.552279,-9.668118,2.419470,-7.265461,-8.025840,-7.295148,8.131548,-7.748204,-4.511885,-9.698047,-9.445016,4.340005,-2.822830,-4.977401,-0.412704,-9.545873,7.527339,-2.858210,-5.167101,6.492390,-6.415605,-6.889376,-0.800700,9.199744,-1.522331,-9.162923,-7.928585,0.336956,-2.995002,-6.319503,-9.002195,-0.049112,2.555844,1.475111,7.743166,0.412822,-2.754657,5.849404,-2.945979,-4.825502,-0.602913,3.799199,-2.426639,-5.466221,-4.864867,5.763516,5.600413,-2.158959,-4.478192,-1.896524,-9.175270,6.319333,4.671569,0.227322,6.027707,-8.907475,-0.915703,-4.477954,2.673527,5.432673,0.934293,-4.004735,-8.075550,-8.867297,-4.606202,-2.392148,-1.267587,-0.275883,-7.427246,9.980585,3.265006,-6.270184,2.328269,-1.433385,6.815509,-6.429422,-8.257788,6.268157,1.083223,0.200692,-2.831624,-9.555870,7.803411,2.043429,-3.104457,2.417420,-8.054922,2.070396,-4.582603,-8.155940,-0.479314,1.870599,-1.952272,2.458499,-6.273605,6.702248,2.997759,1.643878,-8.755382,-5.412300,4.392738,-6.241872,2.507398,5.107820,4.774889,6.722219,-6.271963,-7.970989,3.976773,-1.777725,-4.879289,2.352800,3.202998,-3.598855,3.467055,-5.919047,-7.385312,-0.042439,-0.203711,-3.561895,-9.435816,5.797177,-6.023373,2.173363,-1.054610,0.082469,3.637016,-9.274643,4.249341,8.445988,2.001754,5.879821,-7.787414,-6.413391,9.456838,3.633307,-6.155915,-4.132005,-3.031306,8.174777,1.495138,-4.812804,0.643134,3.099493,6.563347,7.408905,-7.529118,8.351241,-6.805447,1.285932,-6.014282,2.700383,-2.072803,0.124997,8.253618,7.513593,2.623781,-7.902740,-6.115504,5.994234,-3.022572,-3.742812,2.946298,7.735903,4.520460,4.822728,3.338168,4.212243,-9.036458,7.390016,9.492617,-7.326066,-7.631233,0.258850,-8.968728,-9.340012,6.989191,5.421506,-9.251887,-0.958601,8.587506,4.528426,0.033325,-4.347402,5.608041,5.570348,-1.674625,2.332733,-0.906926,1.663556,7.395894,2.980605,8.765534,7.338295,-7.885231,6.257464,8.338448,-9.927447,8.354870,-1.487645,-6.896176,1.533290,5.919432,6.023972,2.228950,-0.631480,0.400691,9.980309,-8.404554,-9.526913,3.901454,6.480370,0.331826,5.215234,-2.292751,9.785051,6.626998,-6.097607,-0.802395,2.438708,-2.481787,-8.823340,0.515228,-2.385485,8.139228,-9.344780,5.696086,9.150303,-6.054615,1.862087,3.298800,2.876719,-9.294520,5.895457,-4.106965,-9.831924,3.544889,-1.988535,8.251012,-0.141533,1.944834,1.120593,-4.663609,9.149513,2.255888,-3.489832,-7.442699,5.428747,8.571389,8.766641,7.933047,-7.893650,-2.862235,-1.233467,-9.719986,-6.826580,3.253525,-8.211242,9.295340,-9.067637,-0.541508,9.767356,5.414790,2.899916,3.951916,-3.260867,9.256368,0.621854,5.383968,3.263896,3.032793,2.125296,6.282646,-4.602220,-6.060508,7.719438,0.964738,9.740619,1.362657,6.728042,4.748625,-7.599004,2.869295,-0.217739,1.481848,-4.173647,-8.187073,2.333987,0.715769,-2.452322,9.592895,-3.572502,-4.970910,7.060216,0.462056,-7.385119,-3.264701,1.892264,5.484861,-3.731410,5.359177,8.444762,-7.581320,0.148430,-1.072616,2.117795,1.348194,8.922675,5.524074,9.334084,0.496555,3.810521,-0.155120,3.611527,8.667792,-0.929188,-1.045412,-0.172313,6.630388,-8.024965,8.709269,7.391841,-4.245428,-9.607312,1.379377,-0.409008,2.046512,-5.092933,-5.682435,1.708491,3.019024,-4.364887,1.886259,-9.986243,-0.043799,6.807035,3.148904,-9.707535,1.298963,3.559333,-2.951495,3.543947,-2.306446,-6.590267,-8.683469,-6.076256,5.383609,8.552082,5.933158,0.127756,7.566009,3.696074,1.638254,-0.828574,-2.821267,9.742100,4.455962,-3.879308,-8.264507,-4.535478,5.552960,-4.901177,9.207323,7.386874,-3.474165,-0.550435,7.124798,-8.836027,4.298549,1.946442,-3.931097,-8.427308,-9.089698,4.760717,1.358603,5.523314,-8.554923,-8.786024,8.158286,-9.404348,-0.236475,1.673551,-2.182775,8.490634,-9.799855,3.356254,9.703992,-3.525016,4.514549,9.745324,2.307438,1.803521,-0.129782,8.080807,6.821906,2.041584,-5.841751,-4.493861,-9.057054,-5.197448,-8.513997,-0.429425,-2.923649,9.574631,-8.443130,-7.058048,4.657509,-8.206295,5.227993,-8.093273,4.355041,3.603780,-3.006941,5.513087,5.474300,-5.581532,8.844158,8.709326,9.721769,7.946938,7.213989,-7.925183,1.261613,2.980384,-8.855486,-3.487040,3.838969,-9.126196,4.264234,9.012307,6.848975,-3.979421,-5.098364,-6.853507,6.734731,7.704281,-1.293677,4.968576,-4.971627,-6.110632,-3.558760,5.964713,-6.707128,-8.925212,9.295194,-1.854388,5.182246,9.280078,2.817920,8.125084,-1.384568,4.720156,-5.986596,-1.206876,3.420030,-3.365963,9.969250,-2.004474,4.926688,7.995642,-2.728300,2.558417,9.595307,8.860685,8.624408,1.386989,9.170938,-4.851992,7.547812,9.765572,0.751772,0.685769,8.169269,9.110111,-3.456402,1.394668,-7.407902,-2.020083,4.184652,-6.852461,-2.713706,-8.090114,8.296913,-0.342371,-3.535802,5.051622,9.981679,-4.424079,-9.247832,0.179806,7.907396,7.901838,4.272489,7.273502,1.691037,6.257041,1.155790,-9.667342,-8.223400,6.366027,-2.287851,4.118824,9.599618,-2.706813,4.426479,-5.736593,-6.563129,-9.758726,6.952363,-4.256288,-8.396925,9.239386,-2.606107,-8.721327,-0.992773,6.172848,-3.301371,-5.602066,-1.022871,-0.629622,-6.626092,-8.996046,-0.358463,-6.471204,-4.074265,6.157844,6.574785,-6.030504,-4.501117,-8.909289,0.909705,1.815640,-4.291015,3.490480,-5.272486,-2.840008,1.246573,2.978322,-6.452379,5.596629,-7.501108,5.112231,3.394332,4.099501,-7.990377,-8.693492,8.834637,2.331659,3.674144,5.822499,-8.725563,-0.164554,-2.682222,-6.553739,-1.238498,-8.305054,-4.484853,-4.893240,9.397394,6.624134,1.989186,8.159400,2.445209,1.851419,-3.035160,-0.227361,-2.807201,-5.681591,-4.793112,7.713964,-4.759161,1.040139,5.131735,0.036849,-9.374670,-9.775268,-8.432308,-3.181647,7.660345,0.424212,-5.873812,-2.281664,-6.100579,-9.141068,0.828156,1.504212,1.641934,-4.061976,-6.988484,7.950072,-2.390020,4.677634,-5.588722,-5.644708,0.916902,4.024281,9.279836,-7.248055,-3.661536,-0.503646,0.703996,5.165773,7.607770,2.399911,3.699334,-3.433167,9.234157,1.595177,2.953223,2.747326,0.482205,2.251016,-8.678925,-7.759969,-0.152471,7.780305,6.984131,-9.837237,-6.203837,-0.152816,-2.927099,-7.443563,-3.257714,3.574135,3.985541,-2.132593,7.861676,-6.862788,-2.266067,-8.344133,8.993962,-0.416345,5.693643,6.807912,-9.981686,2.062377,-6.866488,-4.916188,2.704560,8.671138,-2.197268,4.622667,7.816652,-8.484055,8.276734,-5.972010,-5.493891,2.679774,8.594239,1.149599,-9.573673,-8.396933,-7.461835,-2.280430,5.423458,8.738416,9.764446,0.975913,-4.494168,-4.343053,6.784882,-0.213452,8.169593,2.749547,8.319892,2.749491,7.399545,-8.039541,-9.829600,-8.150861,-1.343170,-5.952159,-6.638880,-1.514171,0.322514,-0.261606,4.432945,-9.112908,-8.181144,7.985642,-7.326512,-3.927422,3.493202,-6.226746,6.130407,3.707760,-6.379098,1.308787,7.772063,6.896067,8.632475,1.061538,-0.992652,8.067066,1.745124,-0.393284,7.625148,-9.337110,-5.747321,0.369342,3.264990,6.637974,-5.794292,-8.951215,2.347192,-1.062383,-7.008456,4.764391,5.535066,1.265229,-2.567412,-7.046613,-0.762978,-5.206705,6.049947,-8.320470,-2.908520,-4.764721,7.417623,-5.158035,-0.704223,8.361214,9.341021,-7.699267,1.306427,1.979524,1.428965,-8.081523,-3.444227,-8.064014,-8.887132,-1.841629,7.012684,1.081543,-3.973522,7.204069,-3.721801,9.916572,5.816981,-2.956784,4.259950,-2.003009,1.046108,0.571041,6.303475,-7.609655,-9.744632,-6.667266,2.983386,-2.910032,-3.958173,7.738477,-4.699232,-4.347973,-4.568040,3.426423,-9.369848,-4.404710,-7.000888,-6.625754,-6.356755,6.007287,2.027002,-2.421462,1.029939,-5.104808,-3.407438,-7.779090,-3.414876,-4.640382,3.949414,6.074782,-7.376755,7.182457,8.440069,-1.920964,-3.200979,-6.882982,-8.846414,3.849047,-6.391139,2.226864,9.615093,0.626581,-0.418052,-7.431650,9.270512,6.270161,6.676457,-7.019128,-1.619798,-9.344634,-9.063674,4.607327,9.560347,-8.536166,-0.992313,-3.615675,1.286793,-4.445966,-2.728235,6.667655,-1.973543,8.015297,-8.722581,-2.851498,-1.075773,6.948559,8.583384,9.633684,7.244082,-0.731356,8.224829,6.389024,6.070124,-6.280000,-9.786884,1.453692,3.955784,1.865639,7.641209,-1.354481,-2.134514,-1.061852,-1.532587,3.157891,-6.967204,-9.986944,-3.528643,-7.756115,5.951770,9.188404,0.826547,-5.340456,5.692160,-1.203697,6.646978,2.768731,-6.230098,1.383746,9.184128,5.705045,3.715540,-7.217474,3.990010,4.651631,3.638475,8.360457,5.105455,1.671994,1.180083,9.519172,9.998730,-1.244849,4.101946,-1.580183,-7.215470,-2.139376,9.727951,-9.707002,0.357388,2.388802,-4.667466,3.410537,-6.117568,1.563178,-0.402623,-4.903962,1.845026,-1.467617,5.842760,2.309944,-6.114729,8.776251,-2.719778,-7.365607,3.463062,7.288537,-9.687275,4.008342,8.014186,-4.501389,-6.578784,3.650803,-0.499970,-8.164285,4.658080,4.495285,8.243377,5.459385,-2.066267,2.068988,-1.724756,-1.198736,-7.649074,4.240844,-7.014048,2.257955,2.414032,-9.699202,-9.921954,0.125633,-4.206852,9.218095,0.834997,-0.331449,7.238526,8.679662,-0.708555,-9.751826,0.777992,-7.890555,-7.299550,-4.702923,2.819230,1.865408,6.568994,5.679994,4.049163,9.691324,7.737012,9.707307,-9.002614,-5.842599,-3.961086,8.777765,5.031062,7.830449,2.828473,4.418018,-2.449715,2.494710,0.064277,4.210626,9.801202,3.424985,-4.087995,2.414295,8.739559,2.419428,9.965787,3.094631,3.603150,-6.542586,5.450033,5.563181,-5.863929,8.575244,5.903774,-5.219076,-4.897050,1.646931,-4.765273,9.387739,1.445664,6.921240,4.331286,2.923276,6.228449,2.114122,8.754294,-4.668868,2.195275,2.274050,4.997009,-6.180027,4.797950,-9.185480,-6.097388,6.156863,2.037685,-4.037072,9.636782,4.131408,6.068107,0.902369,7.932827,-3.375037,-1.001899,7.229840,-1.943801,0.663759,6.372008,2.807408,9.579022,3.921184,-5.780871,8.539244,9.024382,-6.555807,7.688490,1.666272,-1.116034,-2.055400,3.040616,-6.266113,1.203346,9.863941,3.473124,-5.342138,3.629500,0.549853,-5.346466,-0.517317,6.751969,-9.763232,-4.049872,0.388403,-1.121650,9.227730,9.365336,6.785507,8.417789,-6.106597,4.919107,2.323464,-4.809837,-6.051341,0.039801,8.135127,-5.287733,-5.106366,7.747482,5.977727,5.415765,-7.870727,-0.958615,9.955546,-8.995299,-4.688641,-0.048766,3.103126,3.059439,5.544801,-0.168838,0.716795,0.794839,1.227471,-8.151081,-1.237513,-4.417345,-5.595850,-5.975608,-9.651221,6.818551,-7.245605,4.561693,2.285234,-4.951745,7.509566,5.331370,1.565529,-5.180714,8.765062,7.115851,-3.188156,-2.735924,-3.599012,-8.139296,-5.629469,3.490776,-0.852362,-3.396212,3.803565,-4.051951,2.981127,-8.817493,-9.112049,7.558821,4.735703,7.245005,-8.965337,-8.021323,-5.736290,-5.148508,1.418127,-2.178825,-3.430701,7.127500,7.833171,-6.542547,8.948379,5.720301,-1.721889,2.072748,3.185422,6.482188,4.261222,-2.378672,0.665271,-6.484438,-7.582055,-7.290180,9.778308,6.288860,6.924145,6.342614,-5.092827,0.683237,0.239057,-2.272427,4.774820,9.578615,8.141226,1.006498,-5.235700,4.255939,-8.704676,7.723958,9.972755,-4.332315,-2.621799,0.871026,-2.227116,3.047679,-7.832176,-9.023142,-0.003859,-7.740238,2.400538,-9.939649,6.023552,-2.464334,8.966252,9.397023,-3.443865,9.294782,7.972050,1.822581,4.918415,0.989419,-4.565576,-9.524766,2.142562,5.258454,-6.426602,-2.946629,4.092384,2.304205,-8.846021,-0.078621,-1.804657,-7.058097,-9.118588,3.468484,-5.315475,4.645321,-7.720453,6.762599,-0.788286,-1.291057,-2.326208,-4.552184,3.588752,-8.927387,-1.015227,4.834928,9.048642,-3.289673,4.460149,3.902702,3.044899,2.806522,-8.482923,2.870038,7.965675,0.392240,1.264643,2.153542,0.033247,-1.590804,-7.942782,-4.878018,5.592173,-4.203547,-1.762814,0.186495,-0.737058,1.123205,7.001502,-0.919383,-6.755287,7.036244,7.657020,7.012625,-3.364844,1.839944,5.292852,-6.172031,-0.340736,3.918641,2.977685,-5.347353,7.168694,-2.242620,7.437608,9.123621,4.368776,6.672813,-5.756534,3.235426,-2.567108,8.377766,5.257577,1.702346,-8.847211,-3.693533,8.092953,-4.408831,2.866607,3.981657,8.178086,-9.830459,8.840002,4.368488,-0.686557,0.318317,0.471957,-2.934141,-5.249345,6.154921,5.053667,-0.503791,-1.017139,9.931392,-4.274848,-4.296566,-2.812812,-9.473829,-1.298002,6.870319,-1.486467,-7.026368,9.650819,-0.613654,-1.182609,3.594950,-6.300912,-0.109176,-5.695368,-7.504830,-5.698138,-0.263574,9.602230,6.771169,-9.750899,3.548398,5.020862,4.294723,-0.657147,-0.038405,3.032964,-9.606819,-9.292083,-0.569889,0.435555,1.972382,-4.834791,-3.190759,-0.132382,5.615476,-4.559864,0.644880,-1.465123,-1.436781,9.529378,8.435723,-8.114845,-0.243679,-8.054127,2.790467,5.355018,-3.144132,-6.077809,2.381990,-2.956476,-7.063206,2.729464,-0.731215,-2.906597,6.619637,8.455465,-4.542150,-2.050954,-0.695465,3.408062,-5.406433,-5.115723,-8.267460,3.709160,7.406501,7.491343,-8.115915,-2.247195,-0.468415,-4.625317,-2.365341,3.791724], dtype = "float64")#candidate|5163|(3360,)|const|float64
const_5164 = relay.const([-8.703837,-0.376173,4.747333,6.895652,7.626405,4.505686,-9.271031,-1.797620,-0.155855,5.975966,8.107518,-9.219034,-9.896506,-3.587206,2.953146,0.308664,7.770127,7.718018,1.128060,-7.952920,9.495452,6.717546,-2.880063,0.651823,-2.352272,-9.830082,-6.883059,7.977483,-5.444155,-3.527247,7.954601,6.468265,6.835559,3.179803,-3.972786,-7.631934,-5.719770,1.320203,2.107058,9.794151,-5.038343,-9.187813,-8.806772,0.301074,9.969466,-8.444518,3.297000,0.117499,-6.359104,6.201177,9.498841,8.075030,-0.450871,-5.329168,2.027838,6.227873,1.086481,-0.088542,-6.622381,-6.896830,7.287290,-7.447303,8.993256,-8.322142,6.859801,-6.213081,9.075782,-0.061410,-3.243645,0.833504,-1.949061,1.544724,-5.637207,0.414067,1.674219,5.016007,-9.842072,-5.482246,9.634165,-2.780706,-7.615181,7.613923,-9.091057,4.061024,3.934300,-6.084359,-0.449868,1.524251,8.053180,9.170839,2.621309,3.887796,-6.849390,3.755680,-3.576406,-4.532768,-7.129195,-9.136026,1.681115,1.516326,4.725095,-0.824340,-3.387955,-9.814712,-7.739769,-0.544430,-3.441392,-1.634011,4.711674,8.178175,6.332273,1.489574,6.643095,-4.262107,4.571864,7.193911,7.668947,-6.131677,-0.589982,7.801966,-5.003259,-5.795437,8.445462,-1.137995,-1.080930,9.788797,6.143136,3.004604,-0.463436,-1.868146,5.522723,-5.057620,4.465483,-6.465711,-1.345202,3.712979,-7.567699,0.639778,-6.063120,-8.741641,0.522503,-0.084590,-9.201108,-2.067271,9.342003,2.889712,-8.421837,4.115295,-3.059406,6.059718,7.168972,-0.717440,-9.626392,1.494241,2.302465,1.207705,7.655599,2.520385,1.269620,0.109401,-5.735247,-8.373615,-2.376232,7.331267,5.543748,3.379399,5.693439,-6.644464,-1.151935,-7.446182,-3.951345,-8.992243,7.331048,4.704642,4.322943,3.488897,5.189276,7.761399,4.541814,4.153950,4.998720,2.060454,-7.631545,3.614898,2.342630,-3.015949,0.662489,-0.248244,-2.236564,-7.083787,-6.372737,-8.971252,0.513228,5.792667,-0.949232,9.952866,-9.630449,-3.708610,0.767602,4.366066,5.454909,-9.201726,-3.961308,6.592130,-7.936497,3.682696,8.055104,4.374231,1.879882,6.095947,8.478579,1.337787,2.475387,-0.115867,2.226121,3.718560,6.129311,-3.893421,-1.253253,-4.266982,9.894215,2.935964,9.486148,6.964325,-8.944355,-9.802286,9.657463,8.898499,6.331765,8.478211,3.087627,7.949831,-4.074953,-4.521350,9.349654,-3.999319,-9.232816,1.811633,-3.357805,-0.974477,3.910912,-6.074412,2.501147,6.927927,4.592480,4.313621,-1.316400,8.172982,-9.161593,8.599882,-7.746535,-4.166454,-8.094422,6.142343,-9.244370,4.096125,-0.374669,7.702734,6.699548,2.033611,6.439027,3.494065,8.105764,2.626146,-4.778631,-8.414369,-2.640852,-6.304173,-0.189782,3.317824,3.618311,2.234699,-7.118634,7.654519,5.420368,-1.179511,-4.210696,-4.120349,-7.738798,5.039463,9.676584,1.598222,0.710578,-9.816055,0.679669,-7.100210,-0.219056,0.765767,-5.056538,-8.330212,8.056043,0.318626,-5.660181,2.224607,8.754233,5.833857,-0.615179,-5.429493,-2.131415,-4.970904,-1.176956,2.630154,-9.161432,4.221251,7.826701,-6.231625,-4.349881,-9.153795,-3.593481,1.484131,5.259106,-3.723805,0.506561,9.827781,3.262242,-3.469699,-6.859754,-3.326072,-5.666816,-2.431615,2.825257,-7.373660,-0.527924,-6.584655,-7.623403,-2.135162,-9.439404,-8.410694,7.884028,-2.897136,5.872059,-3.297974,-2.738397,-7.611273,-6.457307,-0.551181,2.142275,3.501901,-4.202257,-2.959196,6.369456,-2.148124,9.026249,7.434569,-5.563826,9.753625,-6.606104,6.540179,-1.479938,4.270065,-4.661561,-3.555422,-4.450039,1.083475,1.713916,-4.868813,-8.414919,7.899975,9.403355,-0.259254,-9.926264,0.913779,1.473380,9.246757,-8.932359,-3.591971,-3.397623,-6.076911,-5.467677,4.162323,-2.519080,-7.988758,-4.927531,-4.580338,1.710928,8.813247,7.825817,-4.189008,-3.944279,-1.512197,8.446970,5.290826,-7.704006,-6.827544,-4.479340,-5.248137,1.329532,5.617214,-4.367601,2.215171,4.437191,6.624669,5.909456,3.119245,1.671974,-4.074464,7.388174,6.153986,-8.753643,-8.311337,9.771338,8.103298,-9.207863,4.041792,-5.559998,-4.764402,1.329975,-7.550618,4.757494,-2.497751,-2.603339,0.801815,5.486244,6.059597,4.789375,-5.683607,-6.669501,3.299521,-3.058877,-1.102728,-7.008943,-9.256220,-1.210622,-4.582992,5.486328,6.164519,-5.956553,6.769152,0.885650,6.477218,-4.660382,5.469450,3.533958,7.045872,3.301649,-9.040612,-5.787686,-7.045864,-0.181358,0.692136,4.415567,7.845605,4.529446,0.848523,5.435151,5.397431,-1.473244,-6.497424,-8.131161,-5.536720,9.880212,5.546333,8.192582,0.584961,-4.883412,4.470354,3.125784,4.476641,7.670150,0.618463,6.713272,5.215280,9.246447,8.697592,3.628892,-3.065462,3.428301,7.032918,5.458178,-9.696611,5.201567,9.481657,-7.536403,5.996650,-5.055441,-7.134361,-2.164574,1.499749,1.073988,9.282108,-4.212587,-0.544236,0.367785,2.116599,-0.509480,-2.051105,0.187550,-5.493265,2.206488,-5.731617,-4.101359,2.311094,-8.273813,-4.706231,-7.906846,-0.953437,5.048121,-8.018534,-7.427315,7.852979,0.340770,-2.221285,-5.438125,-9.798379,5.749441,5.947368,4.428850,-2.640754,7.964382,6.242689,-5.168370,1.732801,-5.773789,-9.059444,8.052288,3.514951,3.396187,6.054290,-1.827247,8.173281,-7.679053,5.890439,-8.256578,7.216556,6.825374,7.822508,7.176321,3.521036,-3.210971,-0.084846,-7.551289,-4.172131,-7.575251,0.982655,7.951201,-2.262416,8.883154,4.437848,1.208714,6.757640,2.248727,-0.670585,2.261911,8.349384,7.244406,3.911616], dtype = "float32")#candidate|5164|(546,)|const|float32
const_5165 = relay.const([-0.997123,2.623576,-2.018003,2.070345,4.201435,6.637291,-6.347500,3.297074,4.306139,-9.901457,-0.573450,-9.255810,2.256394,6.735573,6.048163,-4.161137,4.045596,6.921926,4.266106,4.030923,5.079295,2.513219,1.718875,3.734555,-7.411622,-2.141470,1.114475,-1.865009,-7.304710,-6.903000,3.502300,7.338953,-0.830612,-7.719277,-5.903812,-2.064620,-2.344567,2.339688,4.535187,-0.536541,-0.721525,-9.718233,7.166722,-5.170637,-5.873435,9.368501,-7.769534,-9.385225,4.527983,-6.237403,-3.952474,9.230225,4.710749,-4.060245,3.854382,-7.708335,9.173004,-8.684418,-9.903729,7.390887,0.946286,-8.007002,0.474033,-7.320374,5.395400,-1.897841,2.605676,-4.647938,-4.545989,2.178856,9.981462,0.592832,-6.294111,8.920865,6.399751,9.697632,4.046932,-8.393766,-2.868712,4.490220,2.189473,1.532205,4.127381,8.846824,4.333486,6.936032,2.707984,2.234757,-4.281027,-9.902415,6.694091,-8.227503,1.910656,-2.973091,5.864250,1.522282], dtype = "float64")#candidate|5165|(96,)|const|float64
call_5162 = relay.TupleGetItem(func_3518_call(relay.reshape(const_5163.astype('float64'), [420, 8]), relay.reshape(const_5164.astype('float32'), [546,]), relay.reshape(const_5165.astype('float64'), [96,]), ), 6)
call_5166 = relay.TupleGetItem(func_3523_call(relay.reshape(const_5163.astype('float64'), [420, 8]), relay.reshape(const_5164.astype('float32'), [546,]), relay.reshape(const_5165.astype('float64'), [96,]), ), 6)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_5167 = relay.TupleGetItem(func_1502_call(), 0)
call_5168 = relay.TupleGetItem(func_1504_call(), 0)
output = relay.Tuple([call_5133,call_5145,call_5162,const_5163,const_5164,const_5165,call_5167,])
output2 = relay.Tuple([call_5134,call_5146,call_5166,const_5163,const_5164,const_5165,call_5168,])
func_5177 = relay.Function([], output)
mod['func_5177'] = func_5177
mod = relay.transform.InferType()(mod)
output = func_5177()
func_5178 = relay.Function([], output)
mutated_mod['func_5178'] = func_5178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2272_call = mod.get_global_var('func_2272')
func_2274_call = mutated_mod.get_global_var('func_2274')
call_5236 = func_2272_call()
call_5237 = func_2272_call()
output = relay.Tuple([call_5236,])
output2 = relay.Tuple([call_5237,])
func_5245 = relay.Function([], output)
mod['func_5245'] = func_5245
mod = relay.transform.InferType()(mod)
mutated_mod['func_5245'] = func_5245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5245_call = mutated_mod.get_global_var('func_5245')
call_5246 = func_5245_call()
output = call_5246
func_5247 = relay.Function([], output)
mutated_mod['func_5247'] = func_5247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1458_call = mod.get_global_var('func_1458')
func_1459_call = mutated_mod.get_global_var('func_1459')
call_5260 = relay.TupleGetItem(func_1458_call(), 0)
call_5261 = relay.TupleGetItem(func_1459_call(), 0)
func_4407_call = mod.get_global_var('func_4407')
func_4408_call = mutated_mod.get_global_var('func_4408')
call_5285 = relay.TupleGetItem(func_4407_call(), 0)
call_5286 = relay.TupleGetItem(func_4408_call(), 0)
func_2402_call = mod.get_global_var('func_2402')
func_2406_call = mutated_mod.get_global_var('func_2406')
const_5288 = relay.const([-5.878126,1.661793,7.390112,6.195257,8.487457,6.983157,3.449847,4.982768,-5.988760,8.228775,0.667949,6.909005,3.016290,-4.293577,8.849249,-0.182164,3.263178,0.399740,3.826162,-2.305503,9.020481,-8.380771,-5.384949,-2.781349,2.658551,4.812027,9.547680,-9.629767,1.468355,-6.435917,-9.677319,-9.574111,-1.412181,3.587664,-5.935462,-8.600422,1.903339,3.589017,3.995293,8.509194,4.778239,1.900113,6.372266,4.309168,-7.006779,8.991511,-4.594440,-0.073250,-1.851806,-1.468875,-4.164904,-3.991608,-3.433904,3.749399,2.683684,-6.391867,3.441295,-6.424174,0.478028,-9.991604,1.559666,-5.924738,6.396697,-6.929350,-9.513266,3.099033,-3.868199,8.338243,4.277111,-0.926606,5.897486,8.547005,-1.717481,7.626877,1.483295,7.457917,-0.754028,-1.263963,4.062996,8.870630,-1.378503,-9.144741,-4.155044,9.416437,-5.562089,1.751998,-0.471365,0.355495,-6.640631,-2.065364,-2.971638,-1.443685,0.748475,-2.296978,8.605041,0.439779,-3.812236,-8.418319,2.487809,-9.918592,2.748233,8.198870,-1.243002,-3.843495,2.911076,-0.479065,3.155102,-6.317915,-0.862813,3.167490,-7.585999,1.548211,-7.738750,-6.746940,3.400585,0.423729,-3.421368,-9.936499,4.900382,2.373827,3.986569,-3.761140,-8.294050,8.847729,-0.270779,-6.911004,0.925716,7.075929,-5.716679,3.520952,2.138818,-0.376634,2.099202,-9.929416,-3.880249,-6.012716,-9.779035,-4.981682,1.900544,6.552489,-5.284272,5.144714,8.005911,3.323534,-9.073047,8.415213,1.942277,5.624888,-9.170629,-3.123821,9.407007,-5.278222,0.997626,-3.615884,-5.879460,-7.611611,8.671743,0.977286,9.018293,-7.397397,5.539127,8.820764,-2.742199,-6.164297,-4.960627,5.175101,7.961413,9.253421,-9.038473,8.213404,2.998954,2.565686,1.873176,5.701427,2.030800,-4.069970,9.710597,9.850678,-0.666759,-3.893369,-4.026656,-2.874047,6.038158,1.182637,6.120112,4.116888,-0.523994,-4.999011,5.209763,-9.515219,1.125672,6.900437,-8.137904,-8.507434,-5.701295,-4.194422,-9.823003,-3.815432,-9.422717,6.621874,3.218322,3.735073,6.330477,5.071143,5.083875,0.780646,9.845714,-2.973492,-9.997943,-5.776706,0.349694,4.581262,-7.418586,-2.363372,5.212736,-3.712973,-9.361135,4.215335,5.908044,-7.064344,-4.286434,-8.759009,-3.229122,-6.715728,1.838713,-3.039219,2.019455,3.341618,2.938264,-1.685447,5.905179,1.217623,-2.863846,-9.945834,-4.458643,9.442830,-7.492390,-9.566077,-5.983939,6.043772,0.614421,-8.914576,-5.672274,-6.718403,5.453237,-0.789712,-6.191950,-7.248918,-8.053022,-7.469389,8.857827,-1.673176,9.544291,8.386865,2.627062,-9.056173,-0.680377,5.437112,-2.182006,-1.667081,-2.614924,-5.688968,5.257955,-6.534640,8.257278,-8.702459,-7.089018,4.720156,4.030208,0.735538,2.432918,1.858131,-8.396428,-3.675301,8.469018,6.798874,-1.340741,-4.398000,-2.381006,0.067425,4.157805,3.279499,-1.984571,-7.771888,8.225188,-4.691895,0.940943,-2.828320,-0.787123,-8.942277,5.470118,-1.975344,3.612182,9.966549,7.032110,-3.727678,-1.345552,-2.793526,-4.319046,-0.097725,-6.625362,-0.437598,2.043151,8.711807,-7.848266,3.934070,9.430399,6.841311,-9.537023,0.848125,4.499192,-7.646935,4.658357,3.920186,1.265550,6.015433,-2.076904,4.165618,-5.554483,-0.280452,-3.485121,-4.753212,1.379982,1.333049,5.202807,0.097978,-5.094825,-8.515013,-1.875008,8.230535,-7.500606,9.547230,-0.726682,-2.136180,2.826511,2.143650,-1.351191,-0.119301,0.841057,1.694516,-7.409206,-8.937692,-8.798749,-3.031439,-5.462869,6.650574,-7.498887,9.078292,7.615040,4.615140,-2.465947,5.613674,-8.752827,-5.610263,7.578206,-1.243067,-2.735296,-3.706782,-2.498638,0.560091,-5.475016,0.814215,9.756584,7.636100,-3.938728,-6.170691,-0.716524,5.205322,0.645223,-3.975009,7.808323,-9.625707,5.205354,-1.039679,9.210794,-1.002431,-7.133082,-1.887612,1.041263,5.655457,-3.927065,-6.341592,0.813138,8.901769,-1.993316,1.918078,0.540955,2.246965,-3.404717,-9.422729,-7.229664,3.434292,-3.458674,-9.724880,7.524763,8.085771,0.313926,-6.903607,5.241489,3.543996,-3.946338,8.361230,-7.308855,-7.256140,-9.712341,-1.009458,-7.164028,-1.747267,0.287669,-5.701209,-5.284187,-9.224029,3.702985,-9.463501,6.862287,-4.512007,-1.214402,9.426840,0.257208,4.298274,-9.323019,-5.555737,6.920110,3.624950,4.458804,0.580521,9.882554,-7.984767,4.756177,7.856557,-5.528513,-0.349391,8.291471,-8.932354,7.545186,-7.373869,5.675304,-4.974442,3.410816,-0.138395,9.859163,-6.410412,8.859282,-6.167568,1.575543,8.429357,9.523311,-4.599165,4.277792,8.228572,-5.574887,-4.178126,-2.137978,-6.909864,-9.277160,2.875705,1.486642,-9.360410,-9.633762,0.880474,-9.616559,4.995160,-8.097702,-8.578723,-2.011291,-5.760268,-8.852059,5.735736,-7.669593,-3.958164,-1.227973,-3.385619,-5.936336,-3.272103,4.726186,-6.967569,3.849327,-3.941130,-1.313037,8.342133,-3.739544,7.438152,0.651502,-4.664641,1.487085,-3.613167,-9.211014,3.614120,-9.420053,8.763498,3.854959,8.211475,2.913976,-1.087128,9.124186,8.003603,5.771818,-1.291910,4.594133,-7.398126,4.339531,-6.264491,-8.994904,-4.851719,9.760869,-1.906870,-5.836654,6.894630,9.661437,1.990093,-0.138276,0.441729,1.235361,-1.914668,-0.716922,0.874325,5.918595,5.936717,6.629287,-6.378162,0.138572,4.604801,7.431009,5.116734,-2.672803,7.112613,9.694879,0.684088,-0.142283,4.145740,-7.680942,-1.002087,-4.225067,8.152356,-0.015407,8.764335,9.397031,3.546314,0.789097,1.855757,4.465682,-1.713724,3.961720,3.096122,6.564437,-4.798133,-2.192617,-9.906564,-6.896620,-2.079476,9.123389,-9.577136,7.447099,0.874479,7.513763,-4.346710,1.669816,6.320255,-2.980406,-4.092025,-0.652657,-7.575702,-8.234127,6.878487,-8.169310,4.117828,6.212405,-7.987151,3.670315,-6.929081,5.201219,3.358924,2.862438,3.233139,8.837044,-1.041053,8.348929,-1.566985,1.425416,-6.985897,-9.194547,6.869240,-8.655125,-5.193313,-0.283187,-0.896195,0.736753,-8.746014,-8.416981,9.399070,-5.530211,3.871764,-6.128940,6.416471,-5.474609,0.645855,8.290737,-2.127744,9.198787,4.540516,9.894618,9.020988,5.686056,-2.646163,3.515914,4.174863,7.671436,6.180894,2.087561,1.243480,6.382841,-9.020801,7.722882,-7.273011,4.006811,-1.730637,5.166766,7.057259,-3.617100,-7.128558,5.335556,2.942924,4.621288,-1.318977,2.623753,-1.718189,4.674312,4.773008,5.421374,4.279452,4.672066,-8.392272,3.697031,0.325474,4.818144,4.995372,8.019723,7.902374,-0.799034,9.831184,1.070891,-9.151286,-8.177381,8.904633,7.242042,-5.628199,4.578902,2.130290,5.456652,-7.078227,-5.086600,7.823981,-0.738421,-4.075224,0.322901,-5.982137,5.292620,6.174158,-5.134526,-7.995298,6.374313,-1.162156,5.307830,3.779361,-8.050533,9.278227,2.389546,-4.922555,1.373016,-1.633878,7.642744,3.345028,1.385744,-8.261703,7.160657,5.493765,-9.836928,3.382287,7.431317,-0.399465,-4.149988,1.635380,-6.695319,8.751339,-3.263803,-1.456492,-0.032439,3.042545,-5.857053,6.848994,-5.501587,-9.502392,-0.577502,-5.915805,-9.063360,8.875855,-4.188876,4.664521,8.006087,-8.071953,-9.301926,0.779112,-0.917839,5.982105,-3.004910,-3.410707,9.099468,3.464095,5.836865,-4.322718,-6.012805,-8.745067,-5.267987,-4.783371,9.196840,2.622539,0.814240,-6.934511,4.456383,1.779263,6.372080,-6.694777,-8.103909,-6.984681,6.586690,-2.056378,2.534151,-9.429218,-2.119665,8.216013,3.747307,3.061564,4.276229,-4.909669,1.123636,-7.896395,-2.579720,-7.226615,1.928415,-1.952892,7.049128,-8.137444,1.568341,-0.180509,6.515628,7.786303,-4.569151,-7.780127,6.491889,6.585248,-3.738010,5.643153,-7.270231,2.943807,-3.957099,2.703726,-4.842321,-9.804977,-1.860804,8.850173,-1.970590,0.616890,-8.628278,-5.042091,-6.083568,-5.375600,-0.317968,2.301557,7.786769,-0.586270,-6.748504,6.344829,8.612215,4.279404,-3.824938,-2.987613,1.255922,-3.389855,5.622341,3.939768,-4.290774,-1.697699,5.557504,1.757783,-2.751725,3.232222,6.693252,-3.867562,-8.158527,8.646178,-1.555771,-7.248049,0.385036,3.380183,4.666226,-4.464445,5.600907,-1.816790,0.987400,9.401387,1.710342,-0.340631,-9.839863,-1.061701,-0.526057,1.208715,4.503428,2.200260,-5.772894,8.138508,3.278733,3.604496,-4.549785,-2.703621,-4.930013,8.754364,-2.611151,-9.334702,-7.937606,0.836533,-6.069110,-7.197408,-4.132800,-8.179611,-5.660532,2.780014,-5.400490,-5.316958,-3.594585,-9.128322,6.124624,9.620352,2.995440,-7.345652,-5.071916,9.484331,-6.138298,-4.456805,8.877965,-5.482317,-8.624846,0.091333,-6.535950,5.573920,-1.708217,1.730400,7.291618,5.408727,6.629139,4.300094,-9.944114,-6.812690,-5.333323,7.460108,-1.098768,1.399895,0.276540,0.653321,6.866268,6.334911,-4.747744,4.239153,7.197112,-6.593831,-4.185901,-3.199580,-6.929041,2.257495,6.457113,-2.379792,-3.286929,-3.333443,0.389545,-4.185987,-4.971751,-4.712608,-5.379572,-5.558549,2.768050,-0.422779,-9.310298,-6.034311,-3.688823,2.308387,-4.655632,2.550761,-2.905567,4.258485,4.153424,-1.357592,4.923697,-7.910416,-7.083263,0.951334,1.431698,3.327169,-6.364249,8.251232,1.588101,-9.839058,-4.799238,0.632958,3.586463,-8.391130,-0.176867,-3.326571,-9.472347,5.477754,1.348462,-5.099555,3.420107,5.367149,4.176332,-0.152543,9.970667,-5.924502,-7.953727,-7.171790,-7.946357,-0.984095,3.153237,-9.832999,3.162875,-8.655393,-3.713469,1.967403,-9.529871,1.988510,6.684748,9.539781,-2.545171,1.662296,1.575488,-6.895716,-5.933426,-3.617689,4.430208,3.967221,-0.165262,-5.650250,-0.128618,-1.096972,-4.249250,-0.032620,1.939468,-8.491456,-0.880874,-0.396695,-1.198784,8.420832,8.084039,-6.741708,1.984029,4.132451,-9.700531,-5.361310,-3.092290,8.261821,3.229139,-4.512242,0.051005,-7.567750,-7.727972,6.383193,-1.125730,-5.229970,-2.089300,-6.162069,-8.311286,-5.315249,9.138195,-2.103041,6.740841,-8.276259,9.270880,-7.679151,-4.772622,-6.162740,7.416016,9.572583,3.654678,-4.834957,-0.965910,9.304405,-5.701138,6.360252,-4.056141,5.233716,-9.218848,-2.011374,7.585425,-0.923838,-3.936867,-8.737764,0.353896,2.928769,5.722011,-7.115271,-6.020066,1.487339,9.005878,6.192456,-3.510968,-7.064359,-5.045237,-3.239421,8.182681,3.323768,-7.001180,7.145121,8.377222,-9.807880,-1.415473,6.819693,-3.558617,-5.950059,1.110328,5.841017,-4.474641,-4.951300,3.674492,-1.011990,-2.288178,-9.521358,-1.087404,-9.376095,-0.030118,-1.031279,7.329235,3.418326,-1.625063,-7.223305,5.564480,3.295735,2.512530,6.428211,4.400176,8.828465,4.825841,-9.702348,8.386376,-6.443652,5.514970,8.425563,-7.894463,-3.248284,-7.301328,-8.048738,-0.037311,0.204563,-4.221824,-0.526378,0.887009,5.875047,1.238889,-7.786814,-4.853458,-8.042083,2.317701,-7.589814,8.331122,2.644726,6.940148,7.273407,5.769525,1.363583,7.382716,2.067264,6.284709,-0.637275,-2.609736,-3.726517,8.464441,-9.541620,-2.470192,-6.376731,4.148033,4.291936,1.430248,0.266997,9.031170,-4.676111,-4.634025,0.371270,-0.217448,2.701995,-9.887148,0.744597,-2.780203,7.480945,7.857015,-8.085676,3.746643,8.792569,5.204397,2.228884,-8.440088,9.614714,-9.188983,-8.348653,-9.067083,0.552864,6.473241,-7.133467,4.110673,-0.096980,0.736118,6.001202,-6.871523,-2.698313,2.482074,1.403515,7.876600,4.159381,2.106471,4.961095,4.678915,8.533598,3.959865,-2.079255,0.094664,9.195274,-3.685494,2.573122,-1.014244,-1.816414,2.263919,6.287001,-5.440596,-8.211986,-7.113130,-2.445257,6.521334,6.324326,6.912137,2.211051,-1.017425,-6.135359,0.967110,-6.731712,3.133159,-6.665421,-8.753465,1.537701,-0.103619,-8.189182,9.233847,-7.375935,-4.531474,-0.743914,2.001650,-1.234823,-6.784706,-5.330729,-8.162723,8.919240,9.541047,9.426326,1.235106,4.976474,-6.587171,0.787301,-5.946312,-9.823663,0.372671,-6.380119,-4.392315,-1.975297,2.065088,6.438589,1.363383,7.548902,-8.609482,-5.276521,-2.953261,3.686697,-8.714209,-2.506019,-9.858336,2.502939,1.316784,-0.136682,9.820115,5.040724,-6.317611,-6.301972,3.452868,-3.042151,-0.461145,-6.682097,-5.812667,-2.770621,-7.212731,9.245896,7.158422,-7.463125,5.912677,7.596443,7.334896,1.590019,6.185796,-5.569106,-4.465474,-2.372919,7.848910,5.668161,-1.961024,-2.311918,-6.954368,1.251605,5.811287,7.923063,-9.899506,1.472542,7.488221,2.087169,-3.876809,9.277307,1.252434,-5.826711,-0.938032,-2.433082,3.262549,8.529249,9.912382,4.886847,-0.710216,1.143357,6.596812,4.399751,6.742333,9.668815,-3.194805,-6.403869,-9.911074,-1.505484,-0.432091,1.265568,-7.115998,-5.783239,1.836175,-0.741011,-5.056617,7.543798,-9.007048,-6.847017,6.535506,2.565999,-7.262555,6.891507,-0.971183,-0.487096,4.610637,-0.466923,-0.172186,9.618292,4.455727,-7.974881,4.659176,2.138788,-5.003010,0.072413,-1.911996,4.970027,8.202029,6.907555,-3.683722,-3.383791,-1.196708,7.733358,7.278882,-9.528187,-4.138428,-7.242092,-4.925436,0.284469,7.618233,3.340289,-7.333063,4.388884,9.158590,0.708799,-6.906311,8.647526,8.843734,3.057752,9.759645,3.791559,-0.749842,8.011377,5.269786,1.168842,-2.735634,-4.061424,6.476248,-7.183661,5.988440,2.521889,2.940994,-6.209181,7.192669,-5.844453,7.989637,1.127190,1.454499,6.592820,3.979340,-6.055874,1.044722,-4.388745,-4.931189,9.769714,1.550140,3.154713,-5.834012,6.224041,5.825877,-2.405946,9.338410,9.130079,4.056980,1.996742,9.443063,-6.404259,9.293017,-7.097734,1.115696,9.037074,-2.423001,0.338626,-3.096263,-4.698036,-2.183076,-4.813465,-6.038439,6.884313,-5.345128,3.611458,-6.656206,-0.936964,-8.656076,2.589294,5.598374,-9.961361,5.317818,-2.647315,-3.013348,8.086896,0.507683,-7.272220,8.979907,1.550058,8.425840,-1.357152,-1.791066,8.690156,0.985167,-3.270001,7.870448,-8.562766,5.875918,-4.449892,9.190915,-1.143379,0.432927,3.201643,-6.342914,6.002255,3.465441,8.997186,-1.165677,-0.364730,4.931893,-6.671168,-0.088045,9.416443,4.005599,3.153489,-9.582732,-8.545286,6.531241,-2.499726,-5.328100,2.142868,5.722892,-6.451982,7.492741,9.444418,9.805112,3.315386,-0.697763,9.006865,-3.171908,6.121954,0.861662,-2.107170,8.917049,-6.978328,-8.402824,7.944855,2.485740,-7.007192,-3.272879,7.388841,5.312378,9.721336,-8.832731,-4.440454,-0.796414,6.953447,8.417559,-3.074188,-2.715412,-5.062692,-2.439481,4.120087,2.223962,-5.385487,2.956178,-8.835265,-7.808160,2.719127,-3.849843,4.108356,5.227534,-4.725735,-3.828209,3.773676,-0.543564,-7.000600,3.688925,-6.113119,0.356812,-1.795373,-8.945866,7.947068,3.526978,5.900125,-7.772498,-0.363298,8.822452,-0.290720,1.192883,8.965042,-3.116162,-3.912924,0.860620,-6.921931,4.537803,8.981398,3.383969,-6.539706,0.135752,7.438785,-8.932435,8.822800,-6.891568,4.840910,7.364482,7.566115,-0.461328,8.840070,-3.926142,-8.330448,3.136375,-4.315693,9.566252,4.620458,-9.517473,-5.882068,-6.429211,2.122122,-1.207522,-6.055815,8.837886,3.532415,7.798768,4.112756,-1.842959,7.911365,5.626121,4.133470,-2.407063,-7.214085,1.778052,5.866739,-4.783645,-4.666718,5.879612,0.014196,8.932204,3.141915,8.991974,-2.984890,-3.312716,5.178010,8.026942,-0.735629,1.397177,0.162973,-7.339639,-4.436635,7.872823,6.955769,4.561017,0.878975,2.754907,7.492032,6.586024,-0.717429,1.173536,9.776861,-6.652431,-6.816368,-3.010846,-8.966219,-0.572577,-0.987571,-5.968610,8.734346,-2.324088,-0.403349,1.599651,-2.269059,0.954890,-2.094392,1.775054,-3.681318,-5.535621,0.653110,-8.479943,0.425468,7.314731,-6.477359,0.325692,0.398845,-8.428722,2.819342,-5.936217,-0.019342,-9.392209,-3.635559,-2.406827,-6.720424,-7.792101,-3.543990,0.198362,6.949107,2.896159,-3.585342,1.526168,-2.859761,8.556529,4.261763,3.828191,-4.054664,2.150403,1.168926,2.359512,-0.029668,-4.621934,-6.255405,-1.340760,-5.006960,8.186309,-9.830277,-7.949453,-0.344695,-2.264752,7.052289,2.559500,0.548231,3.820133,-9.034000,-0.717203,-5.613005,6.339522,4.266893,-4.782582,5.181378,-6.880180,6.211110,-4.906734,3.056497,5.457231,7.619373,-5.561168,3.228484,0.864457,-6.210870,-2.555264,-4.994162,4.324785,5.678276,7.499604,1.800594,-7.664171,9.633391,-4.411798,4.335034,9.655159,-0.104653,-2.416422,3.454164,2.977527,0.225755,-7.265922,-3.243022,6.485788,-5.712495,-6.537219,7.746963,-6.961632,-5.291359,0.503271,-7.971306,-7.071523,-8.513951,3.896787,-4.323794,9.693841,-1.960220,-2.214766,0.040504,0.801538,-3.503711,9.179838,-2.034061,-5.825924,-4.820890,6.625489,4.148229,7.172912,-4.084763,0.718031,4.844169,-1.222007,1.407370,-7.347047,4.106389,-9.313971,-2.513630,3.406209,3.392754,9.764423,9.602378,-3.581612,-8.328474,-4.204164,-1.588604,6.284134,-6.018222,-2.832988,-5.402838,-3.128404,-6.910551,-5.270901,-2.638841,2.203790,5.672316,0.192614,0.793997,4.875828,1.847850,-4.652387,-8.932024,8.714799,-6.777171,-5.146157,9.852244,-3.134893,0.285409,-4.571669,-1.839646,7.855708,-9.336715,-7.985991,-3.892624,9.379515,9.886808,-1.696850,7.750826,-7.772105,0.999289,2.095723,3.278503,-1.052627,-3.326077,-1.949580,-2.815872,-9.987473,-9.118931,0.936152,3.233390,-8.446866,-6.241770,-7.254550,-7.537027,7.974618,5.724552,-0.677161,-5.671176,4.994187,3.310955,4.547849,5.949478,-5.578920,-4.175513,-0.536170,-5.052422,-0.215692,1.042392,1.244949,6.482479,3.943408,7.901608,7.712961,-8.083831,-1.514674,-2.782297,-8.738990,9.164936,4.946441,-2.841454,5.999056,-9.359378,8.869110,-1.067333,-2.791926,-0.637613,-0.215141,1.174619,6.291838,-9.252708,-3.340409,-6.203355,-1.348748,1.558754,8.132529,-6.955871,8.827548,5.120958,-9.269458,9.288399,9.271226,7.864098,5.463985,-6.878024,-0.327461,-8.835852,6.272353,9.250881,-1.644712,-5.626477,-5.574085,2.562426,5.651306,6.815548,-6.768867,-8.938968,-8.793401,-8.286489,2.386828,-2.507074,4.447423,-9.028683,7.537296,8.858345,-9.297289,-8.458665,-4.069305,-3.548859,-8.969601,5.382917,-9.790290,-9.024109,2.625016,-9.128348,8.596393,8.321970,9.575835,-6.027809,3.819643,1.046581,8.783960,1.915658,4.802597,7.414143,9.303376,-8.603807,8.838954,-7.407803,9.311056,0.667424,7.330223,-6.270693,-4.430056,-0.639317,-0.236520,4.285644,5.723715,6.178956,6.834208,-8.009162,5.763093,-0.027390,3.370274,-8.083001,-4.622003,-4.166052,-3.756108,-5.083538,3.115787,-5.598613,-2.337338,3.160588,-7.471106,-4.088904,8.242902,-4.343777,-1.549664,8.040912,3.392113,-2.327840,8.854554,-1.123833,5.014781,-0.312790,9.218358,-5.164548,2.013278,3.181661,-5.905331,8.784599,-9.061229,3.741316,-9.105997,-6.422976,-3.328350,1.471976,0.696885,3.531909,7.318033,2.653092,-8.238319,-1.506982,9.975624,-8.984235,-3.998284,-5.229231,1.288921,3.399577,-5.625669,-3.068057,-3.117377,2.978993,0.973602,0.051864,-5.012920,3.239699,-1.160134,-7.292434,1.918376,-7.807850,-1.204405,-1.012294,-6.807495,-3.026790,1.947411,1.853576,-9.402868,-4.211904,3.171376,-3.106481,-7.240941,-0.369362,-2.084838,7.574751,3.566327,1.080481,-5.023934,-1.654741,2.877057,3.775675,4.021985,-0.907845,7.227434,8.958722,-6.553731,7.562602,4.445766,-1.682967,-3.060036,7.966191,8.836878,-9.393616,-4.741508,-8.881526,8.234479,-1.072838,-9.077442,-3.001261,2.880317,-9.909222,-8.899504,4.449440,0.021423,0.669831,0.111886,-9.870035,7.004656,-1.365263,1.933519,1.439721,-3.259416,7.286240,-0.370137,8.836434,9.712360,-3.169096,0.772003,8.276127,4.479978,-3.639456,6.111527,3.002678,1.692939,-0.006851,-4.380450,9.887232,0.489942,6.315416,5.627771,-8.559654,-2.641647,-7.670813,-1.643926,-1.694279,-5.880136,-2.221185,2.329510,-0.018136,8.181792,2.335625,-8.545399,-3.994258,8.867963,9.129890,-4.335284,0.114443,-8.738368,-1.281708,4.356532,-5.573557,-6.462984,5.732254,-9.520938,-4.466353,-0.996082,4.282844,2.575442,3.241418,1.384282,9.216120,-3.063375,-1.481788,-0.295028,5.995397,-9.849629,2.425297,-2.282209,-9.495896,-1.450178,-8.226076,8.891812,4.288502,5.031397,9.559905,9.643882,4.043277,-0.522185,0.417542,-3.224877,-7.231767,-8.821371,5.008298,1.465314,-7.310052,4.332657,-9.432462,-5.608831,2.555461,-9.999398,7.657028,3.718498,5.427270,-3.434895,-0.701155,3.699649,7.630964,-8.442740,-1.884992,7.827762,2.433276,4.830481,7.067857,0.890232,-6.293596,0.827433,0.182878,-6.560443,-1.945332,1.629212,2.319344,-9.185363,6.785704,-9.317229,-8.692610,-1.100555,-5.262908,2.290685,9.826133,-5.294533,7.543031,3.407803,-4.289023,0.004099,3.300128,9.505140,-9.963612,3.180350,-7.863353,5.892276,2.633059,-2.600489,-4.062954,8.059126,-2.861878,6.107850,-7.956555,-9.806670,-6.929478,9.314366,0.354868,-6.755154,-8.780687,8.598350,3.339686,3.740483,-5.504920,-5.040247,-1.724651,-3.706115,1.340415,-1.434954,6.051315,-0.620912,-6.917222,7.361976,-3.856359,7.228558,3.550128,9.051665,-6.362955,-7.462845,-3.152549,2.341016,-1.657118,7.428760,3.054497,7.203285,0.082190,-1.616828,-9.279125,7.488617,4.150558,0.140897,5.816568,-4.530220,-9.319166,-1.838864,6.249201,6.075717,3.878844,-1.934207,-4.392370,7.430057,5.286677,7.717293,0.285252,9.384161,-4.324435,-5.277240,0.650066,0.732132,7.764798,2.785923,8.245616,-1.020502,5.578692,8.360311,1.273958,4.029930,-9.036631,-2.867429,7.894078,-0.401208,-3.172079,4.595283,3.599214,6.345869,-0.740576,-9.818595,5.256083,0.478976,3.279723,-5.598644,1.496437,1.827908,8.392214,-5.019854,2.671583,-9.010938,7.937051,-6.814811,-9.655552,7.926689,-0.610402,-0.176076,-0.854327,-7.000265,-0.490634,-2.282629,6.413614,8.769849,0.654786,2.420897,-7.984760,1.566102,-3.810147,2.443166,4.243854,6.668963,-4.927961,-5.590672,1.193982,-1.119040,5.905863,-8.134932,-8.912962,9.203433,1.466757,3.752728,-9.543264,0.738011,-1.821651,6.131071,0.710179,7.662529,-4.152186,-3.660014,-7.433367,4.662398,-6.058033,-4.834461,5.550299,-1.171752,5.115278,5.282183,-5.154616,-7.821429,0.072087,5.384836,-3.637998,-3.804593,-5.960970,6.459621,6.984121,-4.754746,-6.182350,-0.521201,3.708160,-8.847881,-1.458634,-9.118358,-7.519189,0.034192,6.348559,-3.882100,2.619021,-2.801133,1.019440,6.774422,7.299671,-9.702434,-5.118877,5.402169,-2.853941,-4.422193,8.487557,9.109008,1.949521,4.407478,1.654685,9.681519,-5.268303,-2.726835,2.964508,-8.652018,-5.100289,-9.575275,-9.280527,-2.451116,1.462246,6.697119,2.805566,-4.923648,-3.274954,5.069693,0.973295,-2.990882,0.943897,1.402817,-9.374426,4.725503,4.695791,-1.749552,7.928008,-5.035982,6.400400,-0.284770,-3.202215,-5.219066,-5.090382,5.629210,-9.825230,-6.642466,-4.510034,-4.722814,8.145036,1.032866,9.289787,-9.963569,-3.369017,5.780422,2.854997,3.076409,-1.145313,-4.234504,6.507493,-7.954132,2.439965,6.602850,-2.070945,5.738383,7.781406,-2.588676,-0.466218,-5.318415,6.543089,-2.159407,8.670282,0.335463,8.805695,-1.051688,0.582433,-4.169284,3.496312,-5.913812,5.976442,-9.622772,4.639237,2.298048,1.528433,-6.275122,6.455200,2.774041,-8.478284,-1.908618,-1.391799,2.958497,8.855799,4.670449,9.687962,5.329603,3.539165,-7.020186,-8.909887,-8.192732,1.778004,8.542499,5.972154,5.458319,6.476036,-3.757901,-7.598562,6.205284,6.369547,3.237242,-2.715268,-6.403195,-8.807306,-7.888129,-8.959448,-5.825524,-8.171649,0.986984,3.435840,5.684791,-8.286497,-3.560355,0.001621,7.034146,-5.548284,-1.372540,4.156424,-4.809184,2.426449,-8.004545,8.624668,1.073974,-6.113971,-2.743134,3.569634,-8.973253,6.132892,-7.396036,-8.362877,7.622350,-8.372876,-2.891850,-7.964480,1.080819,5.812975,-1.647311,6.659044,-6.574606,-9.866648,3.725626,7.709211,2.219542,-8.973278,4.179764,8.275972,-8.758119,-1.063611,8.052998,0.513955,-4.444718,8.815515,-7.772663,-7.265412,-5.239912,6.704549,-7.063802,-3.488372,2.067616,-9.947670,0.231067,1.301976,6.792928,-4.586530,0.294135,-8.274099,8.730947,-7.631585,-4.469934,-0.770859,5.456547,-5.041776,-2.542394,6.006999,6.066915,7.286472,-8.355548,-5.824382,-9.288027,-7.198508,9.006859,-0.247243,-5.793484,-8.677810,1.565742,-1.397567,-8.142580,4.558142,5.021646,-8.385762,-2.904325,4.849074,-6.366175,-1.617241,7.476272,-0.026411,2.574447,1.336734,0.196799,-1.554385,-7.624664,6.668684,9.449626,-2.360017,-3.821339,-8.165226,-7.016661,8.041786,1.804462,4.910490,-1.970765,9.037442,-2.906181,-0.276297,-3.442390,6.713197,6.090812,0.293832,0.815252,2.493599,-3.625726,-6.218143,2.986568,-0.907833,0.881975,8.248724,7.307896,-7.210549,3.409682,-0.132017,0.051489,4.942440,-0.698112,-6.562307,-1.878613,7.865412,3.796829,1.532039,8.737525,0.984634,3.742751,9.418419,-2.785985,3.841694,-1.010308,7.684222,5.049656,-5.370269,-4.325823,7.030207,-5.161660,7.991165,-1.355689,-5.051432,-7.661509,-1.392923,9.789446,3.590186,5.858562,2.704078,-9.626275,-0.753590,3.855243,0.475659,6.722145,-4.027359,-1.199564,7.207959,-6.859931,-6.874706,9.233266,9.904770,-6.059588,-4.244242,6.542663,4.549627,3.314418,6.252732,-1.387143,-3.732228,0.123716,3.624871,-4.285995,-9.458225,3.713419,-1.903392,9.330292,2.108806,-1.804670,-4.722922,8.618593,5.474262,3.983065,-3.466457,4.906242,0.108263,5.315576,-0.538818,2.414791,4.349414,-8.718915,2.187418,4.520531,7.724442,8.849608,0.675825,-9.331885,7.129350,5.088032,0.762812,-5.152132,9.258650,-5.138709,5.177259,-5.948631,-3.036230,-8.152302,-7.098173,-4.534699,2.280308,5.250062,-3.816233,9.717160,5.365183,9.479789,-4.357275,8.760082,-9.122063,9.174828,6.769625,-5.659730,-9.651103,-7.256625,-0.404573,5.732890,-4.412853,-1.310021,-7.577419,-2.415389,-3.601285,-7.286597,3.769413,-4.538953,1.163397,5.385227,7.751078,-2.461403,3.942451,-8.040867,2.049504,9.271354,3.942048,1.106235,-7.802682,6.835591,5.849276,3.657039,-5.564614,-1.112144,2.054441,-3.915738,6.377672,6.306706,7.299744,-4.346373,5.313996,-0.015079,4.040602,-0.093087,8.990591,-4.947350,4.852732,6.075088,8.423553,-2.509233,-3.045862,7.017863,4.340405,-0.759529,8.462919,-7.609067,-4.559079,4.835786,-5.074897,7.250782,5.898306,-6.756378,3.991863,-6.003396,-9.785124,-3.423048,-8.041044,-3.696961,-7.010942,-5.150768,-5.437314,-4.215748,-1.425112,-2.769730,8.457002,-5.141076,-5.069390,9.868977,0.682767,-8.805048,-4.081041,-2.841307,6.511146,9.847088,8.806920,4.093128,-0.305576,-5.664492,0.203872,8.791362,2.536410,5.844690,-1.704993,2.304548,2.506366,4.926992,-2.909916,-4.141063,2.313489,0.070044,1.011388,-6.606904,-5.466844,-3.478207,9.758338,-9.629980,-0.477138,-4.873124,3.265309,-2.453977,-2.489882,-0.678965,5.729695,-4.596145,-1.878414,9.006996,-1.637799,2.448507,-3.816696,-5.044383,7.974464,-2.346008,-9.075026,7.993469,4.774560,-2.504612,6.646800,-8.098752,7.317754,8.787928,5.574911,-5.437146,-1.669483,-0.103882,3.534395,4.492151,-6.160525,-5.396768,-9.001531,-1.544771,4.084156,1.689285,2.746257,1.315959,-1.396375,8.568175,5.983718,5.781539,3.156894,6.745406,-1.439317,-2.049273,-0.635317,-1.555047,-7.188589,-3.195326,1.165964,-3.639548,-0.640094,-2.867351,2.231303,-3.391612,9.659678,-2.017034,2.732194,4.506928,-9.521158,-4.924193,0.399850,-1.310753,0.675178,9.407310,-0.310056,-3.600851,-8.763498,-3.538542,-3.393227,-5.729983,-6.104282,-6.462909,-2.479915,-5.563866,9.238712,-6.029726,6.559519,-5.716594,9.669217,4.783314,-3.733352,-0.404049,-5.424267,-0.526065,1.853953,-2.824223,5.494070,-3.144590,0.785218,3.051335,9.534833,1.994709,-1.032817,-7.805913,7.214726,3.824098,9.383582,-2.037106,-5.979146,-9.066290,-5.405937,-6.383055,8.259134,9.186901,7.081773,-9.206031,-5.319518,6.579908,1.791676,1.087752,2.245124,-0.627821,-3.285333,5.410910,3.334176,5.515154,-5.335075,-8.858679,-1.949449,-0.091661,-8.966917,-9.940628,-6.936226,3.923419,8.985093,1.012775,8.349633,5.060811,-0.655190,0.452156,-3.199179,1.178577,-5.230408,4.289557,-5.294729,-4.448130,-0.625753,0.787556,-7.730660,-2.941590,7.854246,-5.584750,-0.204133,5.946538,-9.007770,-7.811998,6.644737,-6.009886,7.540285,-7.829864,5.972645,-1.394311,8.639084,9.624562,-1.725581,-8.667946,2.293541,0.428884,-7.665282,-8.852677,2.072234,-6.605176,1.638557,-2.647936,-2.462830,-2.401177,2.337749,8.625051,-3.456772,-8.476510,-7.045182,7.236984,8.216446,5.962379,1.548953,5.708221,8.438359,6.491336,-9.113233,6.924823,-2.406986,-3.818793,7.028240,-7.009612,-3.342753,-7.801271,3.988615,-2.656393,-6.931429,4.887089,-1.857940,-1.384301,-6.965396,-2.694009,7.610460,5.523641,2.511826,9.054147,5.143619,-7.142607,-8.571205,-7.025822,-0.475182,7.390648,8.496040,-1.714262,2.850393,7.770707,-1.874755,-8.033160,9.836772,1.386420,4.601238,9.420624,4.834490,0.889164,1.161177,0.429091,-9.011316,-5.477825,9.773310,0.977718,-2.158774,-1.630649,-4.769386,-6.025754,-5.631858,-7.679509,0.962265,-3.879759,-9.799048,-3.354025,-1.675878,7.861082,-0.124895,-3.246891,1.839661,-3.049812,-3.249716,-8.952518,1.112081,-3.509142,0.826751,-1.123962,0.092118,0.834063,-2.695659,9.042250,2.729699,6.191758,-6.719575,-8.529862,-6.695548,4.384092,9.659005,8.731784,5.892159,9.585717,1.186543,1.386951,-6.166743,-4.521479,-9.336732,3.545064,-5.160249,-5.933391,-9.311682,-7.674660,5.855949,2.362399,-5.899360,-2.584206,9.098362,-6.840149,1.743241,4.486340,-2.366612,-3.707546,4.412677,-9.200158,-3.791719,-5.700553,1.672901,3.944847,2.732420,-6.158778,-5.054194,0.983831,-5.418056,-3.606818,1.318743,3.901464,5.672190,-3.925509,-7.540335,-4.948586,3.529195,8.508976,-8.869256,-0.405401,-0.458188,9.453236,1.636627,-5.841808,-6.767490,5.987004,-8.786623,6.852226,-9.507792,-0.166985,-6.404465,7.440284,4.424470,1.729931,-8.330042,1.418622,-2.622583,6.974221,6.132510,3.690657,-7.221502,4.344094,3.777175,-8.667984,8.567147,-7.188072,7.674878,3.921696,0.274648,-6.108019,-5.110485,-3.707657,-1.177742,-1.189244,6.306435,2.774269,-9.104399,-0.900141,4.891559,5.068287,9.749059,3.422840,-4.871804,0.468091,7.628492,1.400707,-4.009580,-6.596753,0.163172,-3.996688,-4.550143,-6.923524,7.221945,-4.962239,4.708072,7.391500,-9.023950,3.266172,7.420683,-0.874843,9.413009,4.168616,2.521477,-7.906706,-1.337879,9.623254,5.520597,-4.708143,-6.107708,6.938383,-7.360958,-1.959686,0.336680,5.399565,-9.159432,0.262600,2.400879,4.704978,-9.364954,1.816573,0.914973,6.303500,-0.195790,6.633884,2.853112,-7.180869,5.607005,-8.418310,4.345885,1.308204,7.838549,3.685344,7.893375,2.341442,-4.676944,0.501998,6.579417,-7.104054,-8.989952,-2.958062,7.318287,7.784017,9.121586,2.684075,-4.449005,-8.509790,-3.270555,-6.377976,9.048579,1.075965,2.101703,3.053614,-9.776566,-7.415473,1.189193,-2.663471,-1.757099,6.943407,5.726658,-8.403879,0.138501,1.394573,-1.979089,-7.625725,2.545449,4.565425,-6.279014,4.562181,8.112017,2.031179,-9.461568,3.886331,3.488734,-7.181783,1.019438,-8.779318,4.747671,-1.276214,-3.772710,7.514292,1.692797,-2.861313,7.127992,-3.106107,7.793573,7.396721,6.598285,-9.454237,9.635223,9.677916,9.086915,-6.539608,2.417104,-4.308430,8.895413,9.947586,2.741668,-2.427024,7.921858,7.660459,-1.739261,-5.032097,4.655945,-9.969944,5.416291,9.563643,-5.233890,7.130017,3.550539,8.558020,-0.238409,2.584198,-5.665655,-2.631637,-6.815348,-2.976640,8.670750,-0.416567,-8.672165,1.484916,-1.305765,-2.251292,-0.837694,-9.965127,-7.305317,-7.106455,-3.003598,-4.192723,7.820167,-3.017966,-2.401019,-5.283077,9.077150,-0.378932,-3.527647,0.297141,-7.419001,0.129076,5.047076,-7.712809,4.532138,-2.443190,-1.310948,-0.637682,-6.295446,7.654170,4.395889,-6.737489,-8.273982,-9.929353,-8.601189,1.857143,-1.778005,-8.045606,-9.558476,0.392365,7.725669,7.266541,-8.014481,-4.542810,-5.251751,1.919419,6.829488,-3.683902,-6.691054,-5.704474,-8.369428,4.258128,-0.472938,9.499527,7.334633,-8.468906,-2.312743,-2.040906,7.024995,4.783256,7.764712,-7.893778,-9.541698,-2.198668,2.487258,-1.102366,1.998692,-6.737347,6.278158,-4.125107,-6.485422,2.054068,4.481804,5.561318,-2.792238,-9.031878,9.424833,3.049756,-5.974601,-1.991930,-7.176110,8.198013,4.092561,-2.238247,1.755587,4.581007,6.087645,4.839870,-5.595816,-4.436257,9.116210,-4.518072,3.816461,3.096673,-1.810780,4.097876,-5.633727,-6.537606,1.136381,-3.662823,0.662724,-8.085015,-2.525206,5.431103,1.193833,-5.574384,7.172720,5.388616,-0.274395,-6.775471,0.157228,1.456735,-0.791599,8.570154,-4.734675,0.361759,3.604539,1.535716,8.199377,-3.316983,-5.146530,0.686001,-2.403291,-7.080658,7.673117,6.693044,-3.949672,-1.713435,-7.794445,-6.597159,0.296678,-9.130034,-4.990778,8.515084,5.646376,-1.272822,-4.565931,8.815909,-9.012766,4.098751,-8.753459,-7.919822,5.493209,9.716749,-1.097960,5.991817,0.773654,-1.382170,2.825711,7.351700,-5.902813,-7.394773,-8.751145,3.047911,2.101979,-3.984720,5.217646,-1.682601,-8.207778,-8.609795,-1.485209,-7.602677,0.332744,1.830447,-8.934373,8.111134,-6.550865,9.724032,6.063642,2.306542,5.716850,-0.113368,6.731121,-0.821926,7.911123,-5.288045,-8.461912,8.803058,-3.487696,-4.453322,-8.075120,9.086806,1.901252,4.724044,2.164183,7.555430,-6.340632,1.874072,-8.922940,9.921758,-1.120872,8.677465,8.789874,-1.147277,4.948564,-5.402767,4.766727,-7.738321,7.338233,0.856887,8.091052,3.921716,0.014066,9.610962,-3.507324,6.001475,-7.867419,1.262689,6.929881,4.291865,-4.897860,-1.683155,1.489084,-3.362516,-3.717046,1.949301,-4.134615,-0.850604,7.480673,-9.509851,-4.377441,-0.432837,-5.923780,-3.269114,-2.518494,7.410471,-6.025020,-1.384267,-4.661637,-3.035617,-6.451421,-2.642999,-1.504275,-5.792654,-1.892108,-5.284067,-2.925831,-6.621538,-5.985332,0.167774,-5.367799,-4.614379,-3.084918,5.352894,8.195452,-9.375429,8.458966,8.117696,3.662415,-4.939684,-2.383111,-1.600511,9.650401], dtype = "float64")#candidate|5288|(3360,)|const|float64
const_5289 = relay.const([[6.249855],[0.356394],[7.286204],[4.986281],[-4.094125],[0.799491],[-8.186188],[9.877475],[-8.541216],[-4.732053],[-9.498861],[-9.836026],[4.849379],[-8.920677],[-3.979473],[-8.721237],[2.815801],[3.363854],[-7.756991],[4.973703],[-8.362657],[1.286283],[8.583977],[-3.779203],[-4.929515],[-9.065765],[-9.031327],[-2.992219],[2.566707],[6.526711],[-3.731971],[7.742965],[0.883228],[-5.288479],[2.951051],[-0.888288],[-8.405480],[0.932044],[-0.643734],[-1.658090],[-9.312228],[-7.977237],[1.561834],[-2.060210],[6.365396],[-0.802544],[1.879200],[7.124802],[-8.005524],[5.734368],[7.591577],[-5.959675],[0.929746],[-6.765343],[4.622705],[-4.159068],[1.927581],[-9.153917],[7.738845],[2.741226],[-3.030197],[-1.714875],[-9.602024],[-7.930388],[-1.198400],[-9.469146],[5.079248],[5.192515],[-2.963386],[5.964455],[-6.375756],[2.284799],[-1.868697],[-1.959397],[-2.206036],[-6.191455],[8.046205],[4.584858],[-7.081837],[9.254084],[0.436348],[-3.270956],[-1.923592],[5.193600],[7.510308],[-5.982407],[-2.584301],[-7.710838],[-1.667127],[-2.323743],[-3.617599],[8.492527],[-5.764197],[3.003592],[5.592676],[2.887791],[5.506974],[4.639851],[1.754391],[-8.165104],[7.815644],[8.241128],[1.411951],[-6.311879],[-4.953946],[-2.493532],[9.514046],[7.967102],[-6.412296],[-5.137465],[4.327886],[-8.460433],[-6.012163],[-8.010475],[-9.900121],[-2.673395],[2.465914],[9.691181],[2.094173],[-6.609765],[5.647842],[3.847918],[9.552012],[-6.532769],[1.000780],[5.596349],[-9.565748],[6.006611],[2.828155],[-1.462157],[6.958082],[-3.114921],[-1.741041],[6.133800],[8.919429],[-6.459682],[-6.142139],[-4.086569],[-1.706619],[-3.270794],[4.855068],[-2.228144],[0.183716],[-2.474987],[3.138196],[3.478472],[-5.968123],[1.269457],[2.614779],[-2.143206],[0.635876],[7.045610],[-5.607018],[0.911504],[-3.733934],[4.190117],[0.512352],[1.763413],[9.988473],[3.684902],[9.177405],[3.546838],[-8.650281],[-0.021983],[2.955514],[9.766353],[5.049113],[8.096188],[-1.434560],[-1.707223],[-4.131932],[-4.273674],[0.152891],[-9.209237],[-2.542467],[8.070392],[-0.759677],[9.586511],[-3.141821],[4.250783],[-6.844743],[-4.271677],[9.686473],[-5.459231],[-1.572628],[4.941811],[-5.470320],[-6.086559],[7.025644],[-0.198307],[-7.190672],[7.238908],[9.431463],[-6.069580],[7.048692],[8.892930],[-0.561259],[7.319591],[8.182200],[2.820615],[9.580072],[-8.472482],[-8.732404],[2.954334],[-9.910511],[5.656948],[-4.301433],[8.162182],[5.055341],[8.843894],[5.510814],[8.843728],[-5.440442],[-6.311755],[-1.821470],[6.559144],[-5.656143],[2.595359],[-6.691629],[-0.712633],[-1.316058],[6.850830],[5.794440],[-2.618519],[-3.089322],[9.490645],[8.690764],[3.658078],[3.145014],[1.829533],[7.246327],[6.639818],[8.116502],[5.467119],[-5.047168],[-0.618613],[6.652163],[0.337626],[-8.690304],[-8.997755],[1.777799],[9.657517],[-0.180903],[-4.732714],[-9.545533],[1.133827],[-4.555300],[8.385084],[8.125870],[7.093192],[-8.787127],[-1.125043],[1.394785],[-7.665794],[-4.802022],[1.084213],[-4.376040],[-4.686121],[3.273248],[2.921503],[-1.806829],[-0.037222],[2.050503],[-8.945904],[-1.283536],[-0.752847],[7.619569],[-2.212937],[-2.406223],[7.525045],[1.292703],[-8.208531],[9.146127],[-7.939631],[4.134665],[-7.080882],[-1.525257],[-2.362574],[-2.877915],[-0.030355],[-6.103784],[5.713556],[-3.454175],[0.038163],[2.296915],[5.551172],[9.806943],[-6.147683],[-5.150551],[0.005124],[-8.246630],[0.600579],[-0.460692],[8.566190],[3.285352],[2.824151],[-2.129462],[2.156966],[7.786667],[-5.379168]], dtype = "float32")#candidate|5289|(300, 1)|const|float32
const_5290 = relay.const([7.947512,6.537703,5.371097,-0.182562,-0.642264,-1.552843,1.284638,6.240733,-4.374293,2.937267,-2.556652,5.170154,1.942985,-9.478082,0.495562,2.984498,6.677072,-7.579065,5.431312,0.824755,-9.387010,0.134557,3.494817,-1.105241], dtype = "float32")#candidate|5290|(24,)|const|float32
call_5287 = relay.TupleGetItem(func_2402_call(relay.reshape(const_5288.astype('float64'), [14, 15, 16]), relay.reshape(const_5289.astype('float32'), [50, 6]), relay.reshape(const_5290.astype('float32'), [24,]), ), 0)
call_5291 = relay.TupleGetItem(func_2406_call(relay.reshape(const_5288.astype('float64'), [14, 15, 16]), relay.reshape(const_5289.astype('float32'), [50, 6]), relay.reshape(const_5290.astype('float32'), [24,]), ), 0)
output = relay.Tuple([call_5260,call_5285,call_5287,const_5288,const_5289,const_5290,])
output2 = relay.Tuple([call_5261,call_5286,call_5291,const_5288,const_5289,const_5290,])
func_5294 = relay.Function([], output)
mod['func_5294'] = func_5294
mod = relay.transform.InferType()(mod)
output = func_5294()
func_5295 = relay.Function([], output)
mutated_mod['func_5295'] = func_5295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5301 = relay.var("var_5301", dtype = "float32", shape = (3, 4, 3))#candidate|5301|(3, 4, 3)|var|float32
var_5302 = relay.var("var_5302", dtype = "float32", shape = (3, 4, 3))#candidate|5302|(3, 4, 3)|var|float32
bop_5303 = relay.power(var_5301.astype('float32'), relay.reshape(var_5302.astype('float32'), relay.shape_of(var_5301))) # shape=(3, 4, 3)
output = bop_5303
output2 = bop_5303
func_5313 = relay.Function([var_5301,var_5302,], output)
mod['func_5313'] = func_5313
mod = relay.transform.InferType()(mod)
var_5314 = relay.var("var_5314", dtype = "float32", shape = (3, 4, 3))#candidate|5314|(3, 4, 3)|var|float32
var_5315 = relay.var("var_5315", dtype = "float32", shape = (3, 4, 3))#candidate|5315|(3, 4, 3)|var|float32
output = func_5313(var_5314,var_5315,)
func_5316 = relay.Function([var_5314,var_5315,], output)
mutated_mod['func_5316'] = func_5316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_5321 = relay.TupleGetItem(func_1858_call(), 1)
call_5322 = relay.TupleGetItem(func_1859_call(), 1)
uop_5335 = relay.cos(call_5321.astype('float32')) # shape=(7, 10, 13)
uop_5337 = relay.cos(call_5322.astype('float32')) # shape=(7, 10, 13)
output = relay.Tuple([uop_5335,])
output2 = relay.Tuple([uop_5337,])
func_5340 = relay.Function([], output)
mod['func_5340'] = func_5340
mod = relay.transform.InferType()(mod)
output = func_5340()
func_5341 = relay.Function([], output)
mutated_mod['func_5341'] = func_5341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4407_call = mod.get_global_var('func_4407')
func_4408_call = mutated_mod.get_global_var('func_4408')
call_5386 = relay.TupleGetItem(func_4407_call(), 1)
call_5387 = relay.TupleGetItem(func_4408_call(), 1)
output = call_5386
output2 = call_5387
func_5421 = relay.Function([], output)
mod['func_5421'] = func_5421
mod = relay.transform.InferType()(mod)
output = func_5421()
func_5422 = relay.Function([], output)
mutated_mod['func_5422'] = func_5422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_5469 = relay.TupleGetItem(func_1502_call(), 0)
call_5470 = relay.TupleGetItem(func_1504_call(), 0)
output = call_5469
output2 = call_5470
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
func_5177_call = mod.get_global_var('func_5177')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_5537 = relay.TupleGetItem(func_5177_call(), 3)
call_5538 = relay.TupleGetItem(func_5178_call(), 3)
const_5549 = relay.const([-4.337531,-3.329813,-4.939833,-7.311093,-2.708642,-4.312064,-2.584512,9.915038,6.901984,-4.713674,1.879752,-0.709502,0.897769,2.912642,9.688343,-9.266897,-0.530851,5.937080,9.126131,-1.245602,4.793998,3.410658,-1.879417,9.012477,-3.367766,-7.490302,-8.290523,-5.192013,5.537685,2.053314,-3.550265,-4.118316,9.302338,2.831049,9.596601,-5.615768,-2.423713,-8.931942,-8.176841,-5.870097,2.427590,-8.189182,-6.876635,-4.835344,-0.248203,-4.509232,5.702473,4.767086,3.274784,9.669297,2.560271,8.767356,-4.747175,-7.312303,-3.146222,2.274126,0.005947,6.778961,-7.037761,8.793539,-3.703261,8.362328,-1.859595,-9.384076,5.156253,-9.020348,2.550158,6.836779,7.471310,-3.528943,-4.413816,-6.073197,9.272894,4.068708,2.217935,6.074895,6.047176,1.966154,8.625140,4.944375,7.755922,0.311993,1.403210,-7.424831,6.029273,-7.144560,7.359006,1.911166,4.682237,-6.750327,-2.196986,-9.314092,0.328081,3.921534,7.035244,7.462237,3.313212,0.265830,5.192729,5.365284,-2.638023,5.620749,-5.546228,-5.723220,8.575268,-8.409579,-2.038700,5.444511,-8.853839,1.868972,9.980564,4.923593,0.108730,-2.059582,-3.187993,4.570702,5.146768,-2.248733,-2.506337,6.695972,-0.829151,6.561294,-4.831103,-2.823468,9.049386,-8.249615,-3.364950,4.355734,-2.165458,4.391561,-6.043732,1.939117,3.914188,2.474865,3.268699,6.621790,9.369195,-4.496891,-0.633424,-2.371221,-4.516149,-6.970215,-9.312787,7.022942,5.032965,-3.241845,1.725465,-4.544410,6.319224,-1.077846,-2.854050,-3.884153,-2.608590,-7.128755,9.062590,4.331765,7.394582,9.379299,3.442873,9.164044,3.592558,-0.781077,8.958404,9.171331,7.522393,9.547695,6.921119,1.929037,1.556646,-9.474710,-0.222714,-1.180994,-2.361883,-9.129321,-6.276665,-0.113180,7.433118,8.536306,0.742702,4.067091,-2.223615,2.048559,4.975271,-1.096760,-0.305933,3.679664,-7.033167,-0.364622,3.817162,-9.165936,-0.060859,2.874429,-4.188873,9.034268,7.940318,-1.752776,5.262778,-8.259971,-1.438219,3.647130,1.441816,3.054286,6.484370,-0.498336,-1.658795,-0.944924,-3.330168,-9.190923,-8.611530,-4.114816,8.969306,-2.911120,-4.792978,5.646438,2.658737,1.170757,8.488920,-2.198045,6.451675,-7.087274,0.422076,-2.635580,-7.803800,-1.986693,-5.103690,2.523653,0.936063,9.555046,-1.518142,-1.586072,8.354738,-9.094573,9.903072,9.218252,-8.289508,-2.935813,2.629257,7.655919,-5.701869,-5.908294,-1.944089,-2.561485,9.342744,-8.675735,-6.588798,1.870500,-6.981886,-4.067859,-3.665676,-8.524307,5.326059,1.987473,-5.833094,9.605155,-3.181099,4.821172,0.007389,9.971771,0.659101,-9.675260,-3.014719,-3.790988,3.065571,-9.421891,-3.762755,-7.213778,-3.618518,-5.045637,-6.011281,8.418818,-0.045701,-6.464020,-8.063564,-1.888087,0.378271,8.563116,4.630763,-9.013405,-8.124093,-7.205029,-0.014813,4.602877,-9.193500,7.162956,5.981449,-5.063931,0.221334,9.012271,-1.714233,-3.211936,-0.436719,3.154207,3.665324,-4.189702,2.649158,-1.296557,-1.333411,-0.927742,-7.458307,8.025372,-8.409904,5.641793,-9.360683,9.527002,-7.994877,-4.909168,0.785159,-0.914794,-1.111943,-7.590908,-5.426677,6.594193,-7.789035,8.094323,5.394235,-9.621610,-2.107600,4.031600,-8.549485,3.704561,-8.093096,8.480629,-5.088392,-3.814498,2.863880,-9.040892,-4.742007,-6.322058,9.705565,9.025866,-1.148664,-0.961714,9.643993,-3.469394,-8.290771,-4.283837,4.026223,-2.933293,-6.334679,-9.015268,7.699639,9.937444,-8.537934,6.701045,9.607949,-5.952802,-8.401676,7.980209,7.287080,-0.044119,7.266143,-2.844433,-1.247292,-1.194571,-9.870232,-9.120304,0.901237,1.587653,4.717272,0.781409,5.689335,7.631034,-0.768545,8.408196,-1.962612,4.189058,-8.487171,-9.672572,-0.801684,5.042555,-8.032731,4.069050,7.549099,3.558151,8.478518,-1.209494,7.722099,-9.912626,-8.019016,7.187564,8.061529,-3.025439,-0.782318,1.280332,-2.421943,4.590435,-8.133302,-5.493337,2.540632,4.860300,3.351269,8.907653,6.770677,-7.612027,5.417310,-6.398818,8.337133,5.678687,9.879366,-7.131206,0.704270,-7.783133,-8.209512,-3.839013,4.751998,-5.876550,9.305023,8.546448,-3.502117,-8.505827,3.787083,-1.017567,1.100086,-3.740218,-9.155299,-3.022198,8.435073,-3.051680,-3.593290,9.750192,-6.047080,-5.980099,-7.721493,-7.037523,7.164744,-1.804176,0.045411,2.330910,-0.276037,6.480819,9.235741,7.403617,3.475390,-6.386670,-5.295253,2.443822,-6.305257,-7.934185,4.947363,3.422981,1.619899,7.376072,-9.902207,7.729193,-5.231617,-1.781013,7.945340,-6.479468,8.410140,-5.067358,0.342123,-6.167829,6.652906,-5.073919,1.606631,9.190938,1.534980,0.167579,-9.788690,4.407617,7.482800,-7.396785,0.850763,9.666779,3.514928,-2.150489,4.330452,-9.843522,8.710418,6.478128,-2.131451,8.103430,8.318657,-1.811456,9.057552,0.427878,4.472162,4.723526,-7.094569,5.011598,-6.094229,-8.418060,-2.858829,-4.445803,0.207496,-1.620191,5.325109,-5.481872,-7.861461,-9.011633,-6.509704,-1.585556,1.805045,-9.176480,9.168021,9.987374,3.925921,5.789738,3.854830,8.282371,-3.556765,-1.843553,5.878809,-9.756040,0.862195,7.595628,-1.863118,0.538080,-6.078842,-3.375439,6.725982,9.099179,2.188084,-7.935938,6.772035,-5.183951,0.174578,8.263955,7.534265,-6.783994,-3.896708,-4.947875,-8.456153,-7.483472,1.648045,-0.930588,-1.069561,9.020168,-9.899638,-8.282261,9.929884,4.748274,-6.456733,5.401412,5.651655,-9.892240,5.504880,-0.149516,9.204550,-9.423654,9.546563,0.405535,0.526190,-6.203389,1.519978,6.525209,4.855256,1.087297,9.495489,5.675166,9.226424,-9.305074,-2.502451,-3.900223,0.470670,-8.944201,9.112450,-8.417998,-9.621659,-4.928221,-5.593655,-3.230039,3.587471,4.182638,-4.910640,3.901750,-7.599960,-2.965095,-7.956577,-6.410940,-8.137998,6.790444,1.658569,-4.342250,-8.508376,1.158881,-6.617751,-0.096308,6.220708,-7.446562,-1.947318,6.662469,1.906774,3.020098,-5.361338,5.013693,-0.678595,-5.197822,-1.066618,6.421936,-7.795938,8.252298,-4.049821,-6.798098,4.686649,4.408526,-0.401381,6.903923,-5.092973,6.483913,-4.801344,7.357349,1.483006,-7.568737,-4.182923,-5.762286,-1.853767,7.523693,9.436020,9.297996,-9.308126,-9.343528,8.860190,-4.847365,-9.588756,4.084175,-8.678591,3.650301,-0.865032,-3.548184,8.771884,7.221411,-6.287716,-9.096626,-3.450980,9.916476,-3.497499,1.893208,3.162783,-2.216165,-5.212225,-3.370273,-6.056775,-1.896172,-8.577677,-0.653138,-3.314842,1.829525,-6.546062,-9.304775,6.455691,-4.688022,-0.639816,-1.676375,6.215810,6.973749,-6.432279,2.110565,-0.881022,3.847835,-6.372389,-8.478074,-4.354366,6.994276,-7.182241,7.276284,8.682941,9.209594,-2.600580,8.917854,-5.726426,6.883941,2.929866,-9.555953,-7.697787,-9.786782,1.339078,8.887506,-9.565474,-8.657342,0.285659,6.282560,7.602999,-7.664800,-4.978435,-4.544471,-4.423415,0.316992,-6.059567,2.990291,0.242534,9.700347,3.511593,-4.367777,8.020569,-0.011253,4.902830,-1.322169,-8.186822,-5.822403,-1.992453,-7.854073,-6.201302,-4.397779,6.284845,4.376883,9.045129,0.890371,-6.616439,6.831897,-8.774297,-1.065066,4.651666,2.905955,2.904258,-7.534515,-5.226759,-9.982891,-2.181889,2.877541,3.462837,-7.540659,0.043939,7.920433,-5.608237,1.149861,-5.218832,-5.164521,-3.122153,5.414538,2.472836,-3.481013,-6.091105,-2.587265,7.151357,-8.863295,-0.586899,-1.142119,-2.131396,3.755052,-6.391276,-9.265948,-4.732084,-6.495623,-8.603780,-2.779939,7.382439,3.625136,-7.763849,-8.509925,7.520035,-8.303290,0.459411,3.207786,-6.519647,-6.331532,6.551927,5.509900,3.486896,0.439804,6.857188,9.823072,-0.589169,0.988220,-7.374005,-0.200358,-8.941648,-0.966863,9.837979,-1.184267,-3.723690,-7.219468,2.205033,-3.356181,9.319292,-9.836567,4.869954,6.406275,-6.711332,-8.870353,-0.665121,-0.545884,5.004082,5.639091,-8.975962,-0.426239,-2.373246,-3.628667,-6.555458,1.805027,-4.964875,4.361075,2.865557,4.020279,4.752169,3.948643,8.064249,-8.175851,-7.249854,2.227831,3.047223,9.010608,3.562807,2.153056,-9.846489,7.868104,-3.494142,8.947705,-9.637073,4.238750,-2.537384,9.204320,-5.130571,7.744977,7.095454,1.226289,-4.210182,0.397707,4.501543,-5.648180,3.015490,-6.903041,-0.244255,8.586112,0.454327,-9.399798,2.726481,2.471771,6.497085,-2.387021,2.760306,-3.057148,6.573623,2.537327,-1.107284,-8.593995,-9.558202,-1.332982,-3.465083,8.232757,-3.005782,-1.697683,4.131117,-7.140618,-8.395343,-1.483032,-0.623115,4.235558,-3.851619,-8.175988,-7.257003,-0.918978,-9.614825,6.139596,-3.221989,-5.177097,-1.114637,1.495213,-9.813830,5.689869,-9.045501,-3.599998,-4.585304,-2.166665,9.791315,8.236988,-5.145818,-2.843503,-6.698288,3.082024,-4.999736,-7.797686,-8.150998,-5.829362,2.339856,6.341535,4.051005,-0.695369,-8.614786,-1.838275,-3.703372,8.529572,3.712394,9.005520,-4.345378,9.727275,-1.590785,9.679569,5.385369,4.384109,3.569015,-9.664727,-6.290762,-4.351265,-4.477535,-1.130452,0.929689,2.694570,6.213124,-8.648498,9.965774,-4.871706,3.426156,4.383686,-9.535666,7.228060,7.636793,-1.076150,3.189165,-2.106235,-6.248683,-3.550204,9.952315,-6.335379,-7.830076,-0.318454,-6.962853,9.456567,-1.026596,-7.582123,0.796808,1.211037,-3.389560,-2.888220,-1.181501,9.153601,-3.623939,-8.524755,3.327883,-1.473281,-2.433769,3.253994,-6.463314,-5.889846,6.541568,7.523565,9.919260,-6.651824,-7.813685,0.837663,3.943449,1.125576,-0.399540,5.361345,6.677909,7.112442,-7.532459,-6.368690,4.299147,-9.685041,-9.502387,4.290349,-9.586883,5.040669,-5.030184,8.344561,8.090849,5.346690,3.290970,5.412039,1.208999,-4.708061,1.188791,-3.661714,6.861163,-6.984874,-3.393368,0.140744,6.146567,6.795354,3.065674,3.830214,-0.412931,-4.762600,-5.456192,-1.574264,-3.108542,2.710135,2.182663,-1.162062,-3.546803,-6.322122,-9.228525,9.047932,-0.387961,-3.319155,-6.862503,-8.517339,-4.886732,-2.304080,-7.299491,-7.310404,4.374683,8.601032,0.994946,5.666099,-6.774757,-8.465591,-6.644476,-8.498415,5.863834,-9.430482,-0.619118,-7.409301,-0.260944,2.071679,5.042789,2.572067,-5.292197,8.748106,2.831848,1.480489,3.781112,-6.656495,-9.213505,-7.381076,9.323573,5.259096,-1.591046,2.721717,-8.439326,2.955694,-2.101916,-5.561465,2.820540,9.666977,-9.297635,-9.619850,-1.563377,7.279684,3.039640,-9.362050,3.603808,3.774216,9.649353,-6.767775,2.597193,0.173891,-0.313740,-2.027583,-9.290792,-0.028564,8.311888,-2.039849,-6.449827,-7.298116,6.626034,-5.393774,-2.164626,-8.868585,-2.027419,3.155908,2.683586,-8.179561,-4.130669,6.842441,-6.574049,0.888236,9.840436,6.506271,-1.799806,9.765858,4.087364,-3.287198,2.293363,5.594682,4.693609,-6.791276,-8.312203,-3.240720,5.082860,5.759963,-7.493133,2.424476,-2.774186,7.017446,-7.546014,-2.221917,-3.859036,0.694398,-1.558540,-0.090669,1.690435,-4.583922,6.762117,-1.732989,-2.990362,-1.295294,1.425993,-8.046481,-0.288821,-9.704409,6.851320,-5.872204,7.039863,0.649152,5.958692,3.154076,-6.325123,-6.172909,-9.290425,2.942142,-3.944721,3.438240,1.644210,4.619850,6.400862,9.514657,-4.015647,2.492511,1.027645,2.690907,-0.293417,-1.825923,-3.304065,-7.538348,4.040706,-6.060909,1.582392,7.901933,6.420588,-5.044158,-6.217538,7.165491,-1.620422,-0.904955,-9.724849,-5.032541,-2.217746,4.633509,0.200281,-1.959627,7.411718,-1.406653,-4.729559,-9.682083,-2.606485,5.630130,-9.844468,6.737776,0.262618,-6.490941,-6.949860,-5.716377,3.191476,3.974568,0.100627,-5.412331,-6.230092,9.047450,-3.606409,8.984966,-4.345684,-1.257477,5.199855,9.473558,6.363126,-4.187731,-2.044658,3.650674,7.587455,-2.260612,-1.608246,2.968966,8.840994,2.332411,-0.912754,-0.435103,6.874953,0.004208,3.073158,3.515007,2.628527,-3.581684,-1.910045,4.133413,-1.165902,-1.810725,-7.031462,-4.488753,-4.201938,-7.627987,-7.757785,-1.819905,8.353920,-6.594571,-4.599364,0.817488,-1.726343,-8.345486,2.693182,-0.719710,8.223939,-2.009016,-9.207707,-6.740762,5.828853,-2.941324,5.280673,8.625371,-4.290076,0.775329,-0.793071,-2.762457,-0.177150,0.961760,4.424885,-7.163391,1.201176,-8.054590,1.357404,-9.934840,9.362077,-0.176384,1.608578,7.583435,1.528850,4.113840,-9.927906,-4.622411,-4.492483,-1.198621,7.085317,-3.848229,-3.031707,1.999460,2.681300,-3.837914,-1.773165,-7.985449,-8.792944,2.561409,-2.559792,4.084729,3.339040,-9.955955,-2.664278,5.467868,4.075411,-2.576336,-4.312549,1.015757,1.567812,4.967633,-6.074396,-7.510945,8.204203,-4.968865,-3.639959,-8.719099,-7.353041,7.925441,-4.406585,-5.427571,-7.428479,2.902283,-6.045487,7.084482,-0.016412,0.485874,-4.191481,8.689413,-3.600063,2.112337,-9.102735,-0.282164,-7.497877,7.421296,-6.666059,-5.450738,-5.118518,6.085117,-5.934797,-9.896985,9.471780,5.514716,1.807651,-3.446739,8.843016,-7.901903,3.241512,-3.074670,-0.926184,-0.423835,5.929022,-4.516005,-2.618357,3.359193,-4.953359,1.253269,8.252706,0.098345,-5.280458,-7.949593,0.318778,6.395638,8.614380,9.435898,0.928528,-6.413830,-5.188132,-3.614312,6.540748,-0.422150,1.776254,4.228260,-2.326517,-3.890244,-6.607191,-9.182172,5.383065,6.025040,9.630788,1.779387,-2.979505,-4.641415,-2.754433,-2.632525,-7.994545,2.042497,-4.544644,-7.621477,4.778859,5.239452,-1.542658,6.142792,8.330324,-6.254650,1.537048,0.296127,-2.267402,0.341703,-0.985368,-3.562999,-6.738334,5.016204,-5.378487,2.767123,-5.390876,-6.330056,0.346505,-1.575650,-9.726076,0.538349,-5.338809,3.558598,-4.591907,9.291048,-1.672924,1.633474,0.577333,-9.862449,3.782381,0.913680,-8.742746,-0.347413,-1.929720,0.362315,4.293232,-6.501756,8.271836,-8.757107,-1.730184,6.474048,0.210702,5.144970,1.413144,8.996935,-0.562052,-9.279440,-8.880844,-4.400963,1.725328,9.705232,-9.906128,4.589654,0.827969,-6.995149,9.479461,2.141218,-2.321101,-7.317104,-0.782701,-5.195074,-0.122827,2.995645,8.368865,5.437268,3.278926,-7.252619,8.308529,-9.413859,7.581629,-9.060541,-7.072217,-7.049066,6.699823,-2.138906,-3.651529,-9.459373,4.639536,4.805354,5.979993,5.642160,6.271872,-9.338999,9.308671,9.924381,6.744842,-3.578845,9.830273,5.527174,5.645583,-2.871406,-9.383922,-3.189974,8.737882,4.128420,0.482385,6.801595,-5.367096,2.566922,-6.573250,-4.464029,-2.756464,3.394419,6.600423,-3.313306,-4.250136,-3.313432,4.876827,-3.616489,-1.298785,3.435476,8.874936,-1.420824,5.318461,2.208678,9.122891,6.326159,-2.146566,9.402382,8.889645,-7.729036,1.218858,8.153335,-9.470200,3.254374,2.014856,-5.024984,7.530875,-2.479397,-3.604339,6.672041,2.988922,5.740031,6.123363,-0.112309,2.279199,0.827721,2.448146,8.836704,-1.372025,7.970688,-0.630313,-5.257681,-9.048485,-4.684668,5.594510,-6.287266,-2.733686,-3.650427,6.554297,5.430889,-4.011913,0.513347,6.566894,0.055123,1.077252,9.664784,-0.808920,2.852066,-0.471298,0.855865,6.216990,-6.400763,8.470366,-2.843904,7.863404,7.358311,-8.418036,-8.156435,-0.705768,9.742461,-5.896702,8.520112,9.691623,5.658681,-1.680949,6.413997,0.760522,3.780559,-3.149941,8.360491,2.868485,6.588473,8.106687,4.119973,7.127930,8.601643,8.888415,-0.440562,6.569337,-7.396183,-6.284089,-1.314890,-7.321081,8.396955,6.151909,-9.766274,2.318007,-5.070741,1.469459,-3.031721,-3.041146,-2.492801,-0.929674,-8.473207,8.790489,8.437491,-1.582887,6.747937,-8.310058,-0.855595,1.828292,-7.212334,-4.437820,5.778312,8.959835,2.266614,8.165371,4.686089,-0.883227,5.134676,5.992126,-3.364575,-0.959367,-4.871387,-3.160397,-3.988102,2.002896,-3.457511,5.724010,-6.339340,-9.951311,3.316272,8.804977,7.647626,-9.632022,9.702072,-6.364813,-6.159935,9.921310,6.370670,7.928616,3.092167,-9.765833,-6.159219,9.483083,-1.955065,-2.012336,8.356311,9.927880,-2.499702,-3.260817,9.140010,6.329767,3.964557,-4.580506,-6.313729,9.509612,-8.524593,4.582085,1.173923,5.499015,-7.114346,1.420281,-5.624025,4.719222,2.025919,-4.495202,-4.821296,-0.250657,7.202629,-2.030496,-7.976774,0.019861,4.339258,4.603038,-8.542103,9.713903,2.430714,-5.113439,8.355421,-9.369254,5.114296,4.910790,-1.391708,-8.471005,-3.114758,1.358260,-2.513248,0.221491,3.251805,-2.678854,-0.370509,0.400032,3.099186,6.156787,7.583746,8.969534,-7.906795,-7.360019,-0.184859,-6.768445,2.413570,8.329027,7.484425,0.344990,7.361385,-8.515081,9.796603,3.707417,9.164167,7.049581,-0.764494,-1.044993,1.584461,3.337820,2.522334,-1.993891,6.347978,-5.689402,1.020040,-5.816183,9.486366,-6.119112,-2.635305,0.150638,-9.037456,-6.999795,1.651667,9.743178,3.233546,-7.392579,5.034488,3.774770,-9.507839,3.589317,8.441420,3.894647,-8.225031,-7.946550,4.584108,-6.202491,-3.761289,2.330836,6.335000,2.087668,9.725353,4.796246,-6.261646,-8.646328,-6.927438,-8.513982,7.182406,8.457773,1.794465,-1.736317,0.329513,-7.512251,4.604627,-5.330290,1.066155,3.783671,0.544697,2.204319,5.161739,7.290455,9.925880,7.611190,3.720254,-2.546190,-2.602435,5.200152,8.626031,-0.017418,1.757716,-7.913725,-2.932425,-9.376310,-2.815063,9.691747,0.927993,-7.921416,8.902798,7.546658,-0.181786,8.678056,-6.141399,-9.441854,8.313833,-3.902792,6.383315,2.274761,-2.217697,-4.293499,3.791559,-2.206528,-7.119699,2.064890,-4.453950,-9.549149,-6.487915,-4.101773,-8.613167,-8.449906,3.251407,1.347452,7.652763,-9.767157,-4.040115,3.263156,-3.818502,-9.700912,-3.649659,-8.454920,-0.575588,4.895086,7.158775,8.344616,-5.690324,3.259474,-8.107035,5.959037,4.889235,9.867173,-0.148994,6.306231,-7.249984,5.159975,4.648592,8.846269,-3.214820,-0.317032,-1.193202,6.311079,9.167604,-5.239158,4.638067,-3.032966,6.081598,-1.616638,-1.880036,4.791548,7.988569,5.023258,-3.566216,-2.300365,7.901354,-9.359933,-1.736205,-0.498173,-7.282930,9.986174,-4.660213,-2.443304,7.456638,2.859281,-0.995814,-5.174489,6.886304,-4.434433,1.216015,-5.095184,5.434749,-3.814811,0.428387,-0.326033,-4.876471,2.348632,9.398235,-0.066430,4.614561,-2.712325,-4.665023,0.405744,-6.179187,-7.136909,0.466963,-7.371588,1.227760,-8.302634,8.673690,0.807981,3.161143,7.870157,-3.527086,2.719341,8.152982,-3.519734,8.810055,-7.883386,6.873524,4.586385,8.642668,-4.272455,-9.843603,2.371690,8.099701,7.138000,-2.261693,4.090217,7.492472,-2.290374,-2.983086,-9.731241,-4.824472,0.007214,4.866890,-8.506178,-5.654545,-2.052702,-4.107613,-9.067615,-2.961122,-1.604583,-4.287968,8.958549,-5.973273,0.899803,-6.192716,-7.791126,-0.906241,0.558582,-9.947531,-4.724426,-7.790706,-6.369128,3.658201,-2.111933,-5.903046,-1.016041,-0.490900,-2.921581,2.805943,4.937275,-4.894162,-7.699792,6.437855,-1.671836,-0.758123,-9.792675,3.231773,1.109334,1.878730,-2.286253,-5.259934,1.675184,7.513338,6.436322,3.183950,-5.915168,0.935949,-4.764247,-6.422780,-5.262317,8.292490,1.471202,2.575163,4.653299,-2.434751,4.138919,-7.779212,3.191003,-4.091668,-6.250253,2.891340,2.346877,-9.960280,3.076413,8.437699,4.479890,-5.917850,8.208132,9.890681,1.425483,1.890921,-9.311101,8.286315,7.955673,-2.662767,6.991131,-5.471733,-5.962274,-5.700284,-0.012856,-5.828342,-0.180198,-4.020480,-3.847188,9.015246,-7.212930,-9.435366,-0.432590,-8.147282,-5.554713,-0.633446,2.348473,-6.379944,4.601317,6.859595,-2.879752,0.864206,9.464857,8.939812,3.035198,8.690918,1.923836,-0.928151,5.025502,2.029278,1.295954,9.989937,-7.546457,2.170299,-5.373319,3.953666,-7.286280,6.432127,8.120943,3.749813,8.104172,-9.917045,0.151398,4.294674,5.580468,-6.460899,-7.532829,0.790545,5.228914,-9.452023,-8.295955,8.062907,-8.386969,-8.647369,9.679330,-6.437288,-8.061594,3.291744,1.541404,-3.247025,1.202611,4.545275,-4.822077,-8.128119,9.465762,9.692781,1.081377,-9.892809,8.098708,5.103635,6.985033,-0.177085,-0.535122,1.063467,-6.378842,-0.918533,-2.022778,7.054577,0.400640,-9.747072,-6.888166,-1.414143,-7.345038,2.271419,9.503355,-0.410599,-8.660301,-9.906845,-1.028054,-6.272340,9.870505,-7.725752,-3.962824,-0.013102,-6.229863,7.496574,-4.050101,-0.806867,-5.409357,-9.405149,-6.005187,-6.889652,7.006001,9.642926,-9.790066,-9.708892,-8.872938,1.961301,-2.990942,-6.954572,7.330091,1.560301,7.850922,-3.236385,5.757781,9.121619,-3.240051,-1.828483,-7.450696,0.771071,7.611683,-2.533829,6.387413,3.086137,0.443944,-4.436399,0.015970,-3.806247,6.533242,-0.782760,-7.023573,-2.865982,-1.831878,-4.014622,-4.850901,7.336458,-4.423197,3.416519,-9.039293,0.542681,6.764011,-1.333378,-7.742993,6.684256,5.677792,-2.429704,-1.664532,-6.984488,-1.960819,5.408413,0.681281,-2.111899,4.675330,0.800968,-7.596640,5.698361,-5.327724,-6.654009,6.024494,-4.794951,-8.548769,-6.322963,5.046197,9.615455,5.565775,-0.261454,1.843012,-7.872210,-9.646549,-8.891476,0.649635,-4.587430,4.047140,-6.887187,0.364880,-1.350656,8.694345,-5.327760,5.121074,-8.018011,-3.510275,1.831731,-9.818713,-8.872968,8.451743,9.281764,2.586515,-3.983620,7.193418,2.056829,1.333997,-7.984893,-6.935964,3.586269,-6.816890,-5.547102,-5.939383,-6.595482,-5.489703,-8.643113,-6.917188,-8.457406,2.732365,-3.124028,9.806549,1.444065,9.955261,7.497084,-6.896234,-6.395435,8.168663,-7.133878,-5.174500,-3.848450,4.688062,8.201893,-8.173395,6.707210,-3.663050,-7.645618,4.441253,5.577715,2.249477,-9.311146,3.655897,-9.806711,-3.214480,8.612092,-0.297278,2.560708,-5.569049,7.639413,-4.332503,-8.232703,-0.828988,-4.277214,9.432310,2.301378,-8.161755,-4.080485,-9.710053,-1.848560,3.939892,6.886117,9.029992,-7.673110,0.331430,0.088099,-8.419761,3.231847,-0.238998,1.047139,5.428123,4.306377,-6.543269,4.822699,-0.568103,4.165802,4.567873,1.853886,3.454735,-6.332817,9.298825,-3.636824,-3.420249,1.365941,9.364674,-7.574769,5.818554,2.166076,0.882848,-6.160452,-2.271125,-5.648244,-0.764741,6.758940,4.578101,1.755251,8.919379,-3.844303,9.398000,-1.684605,-9.963280,2.416974,-1.462878,-5.968791,3.177339,-3.595375,-3.940572,-5.454048,-4.802682,8.891636,1.233662,9.253694,-6.332311,-5.472162,2.961020,9.372528,6.173311,3.121779,1.762897,-8.613464,-2.441470,-7.093126,2.593377,8.267129,-7.717978,0.208021,0.445536,-3.773863,-6.616489,7.619828,-4.919924,-0.942619,4.237494,4.757444,6.342820,-3.875631,-1.314302,-4.695861,5.546586,-6.983679,-9.798249,9.532409,-3.213867,-7.109259,4.844416,-1.523185,-1.978823,0.160132,-2.981500,-2.456584,-1.521275,6.477137,4.282643,-7.356100,3.508169,9.394430,-3.582177,-3.250371,-1.810230,-0.024337,-9.680401,2.881533,8.839891,0.979407,-7.356594,7.304648,-9.343037,5.251938,-1.280477,-1.373312,-4.930956,-6.132064,-7.477612,4.754831,7.708551,-5.649155,-6.685793,-1.021873,8.087397,0.988493,0.528163,-5.334767,7.699406,3.536516,-4.273186,-2.923483,5.411079,7.792833,0.283624,3.325954,-3.651807,-6.092242,6.808785,-9.509350,-4.154516,-1.955767,-8.780730,3.782453,5.793450,-6.751450,-0.047894,-7.041730,2.708380,-7.706333,1.950995,6.208008,5.605353,-3.281668,-6.106845,0.154285,1.173042,-9.769836,5.882311,0.308082,-3.670702,-3.533815,-2.611507,9.317108,-1.459241,-5.285763,8.964135,-9.202705,-9.266317,5.139751,7.928223,6.588206,9.260429,1.414917,-8.057726,0.844728,-2.535876,4.828813,-1.350689,-6.116461,-5.083020,-9.158513,-0.444740,7.933637,-1.053058,7.485722,7.948233,-0.959408,-1.641550,9.814155,-7.226120,0.485198,-2.528369,-2.225248,5.369774,-6.226773,9.045239,6.986435,7.707236,-4.279675,-0.347908,9.736103,7.288023,-2.453578,2.858825,-3.722224,-5.983973,-2.554863,-7.604906,2.098671,9.138108,-7.338379,4.385791,-6.613701,-9.811291,-9.950468,-8.243683,-4.553134,6.598174,0.186399,2.973494,-9.141438,-4.045159,-8.683187,1.506264,-3.873376,4.503045,-7.705628,4.840597,4.927469,7.684952,-1.176740,-8.762691,0.771432,4.613799,-0.349006,-1.018452,-7.204082,-0.697569,-4.677473,-6.038709,-1.726712,2.504892,-3.260511,-5.544513,-0.401836,4.535695,5.227037,0.083468,1.621306,-4.399857,7.141145,9.166673,4.949346,6.165460,3.880243,-1.309386,3.119261,-2.354442,-4.777465,-0.803113,9.485575,9.994855,5.242816,4.292215,8.865813,-1.960582,3.731983,-2.420025,5.524386,-4.362544,-8.118980,0.656620,-4.450687,4.191172,-3.061270,7.749110,-6.156945,-6.131376,3.095272,-5.640234,1.771686,-2.284643,-5.611900,1.395944,-9.459722,4.127892,1.609246,-0.994815,-0.349450,-7.429977,2.247979,-5.292022,2.490949,1.641631,1.513397,9.429296,3.184706,1.997226,0.057437,6.963574,-0.428088,-8.932538,9.272812,9.805741,-8.141682,-9.830508,3.635302,0.673827,-8.231694,1.044894,6.260926,-0.680427,-5.361833,-8.103184,0.357326,9.523002,-0.290319,1.574971,2.108961,-4.823625,-3.830859,2.145903,2.151797,-6.765374,-1.743452,3.905284,3.635295,-0.937636,3.430656,6.246433,-3.357014,-0.388139,-6.546012,1.162948,-6.826686,8.853614,-4.310718,-2.235564,-9.091769,9.165752,8.641116,-3.037352,9.076734,-3.873150,8.806051,2.380217,5.974493,1.104030,9.528920,8.068658,-5.441263,-2.481926,9.847706,-8.420550,-6.774754,-8.317973,7.172611,-2.318524,9.493677,0.847623,-8.224562,9.367464,0.689077,4.584526,3.960596,-4.683055,4.180699,-6.942129,-6.399011,-6.154499,6.225988,-2.582028,1.859732,4.080245,9.192423,-4.985046,4.669886,6.180158,-6.721804,8.064432,7.900243,4.427091,-5.496370,-6.824758,-5.362968,5.716321,1.162536,-1.516710,-1.413113,-6.793782,9.927901,0.648014,-1.729784,1.103354,3.127930,-5.746321,-7.235472,-2.461703,6.539469,9.152017,8.403334,4.749446,-7.093381,-2.204351,7.814781,5.385690,1.020873,4.852162,9.959959,-7.551732,0.971516,-8.550266,-2.965218,2.227355,9.694877,9.328935,8.514231,6.092545,2.450263,7.545384,-9.569948,1.275292,5.266734,1.240441,1.519156,-4.672965,-0.324573,-0.701234,6.532745,8.369893,5.749752,6.833290,0.712157,-8.892489,-0.916627,-6.112994,-4.616014,-9.750546,-8.558247,2.176303,0.161339,6.435282,-0.637618,-0.878425,5.019106,-4.340538,9.721714,9.958148,-8.435007,0.521912,9.522669,-2.445759,0.732483,-6.904731,-6.002393,5.512059,9.941197,-4.480407,-6.558330,7.731759,-2.126173,-9.185768,6.133173,-2.730056,-1.872579,9.493079,8.775441,7.668760,-9.477306,9.832707,3.304161,5.371415,5.325443,-3.488580,-2.930656,3.048639,9.038490,-0.460386,2.138186,1.798159,-4.601793,-0.959125,-7.525937,-0.411135,1.426949,2.939673,-3.563869,1.656593,-3.261161,-8.394256,4.162001,0.101995,2.233222,4.039690,4.586508,-7.634547,3.063243,2.527190,6.008569,2.308685,2.012900,1.902479,2.895342,2.745821,2.713865,-8.398154,6.742803,3.252541,-2.306760,-9.420024,7.640145,6.925871,4.999543,-9.501836,7.327844,2.289839,7.201341,-4.566489,9.519708,-8.542520,0.027183,6.696770,8.647063,-7.640981,0.824630,4.472630,5.923387,-1.105236,9.370088,2.936017,-3.055340,-1.629950,-4.999019,-2.929404,-6.084466,-2.433076,0.288001,1.445543,-7.286198,-8.310193,-3.843444,2.699000,4.020730,-3.504157,-3.309183,9.767952,-8.238467,-9.380185,-8.677176,-0.154973,-2.059080,0.397322,-6.498703,-4.273151,-2.335641,-9.000923,-7.327930,-3.100713,7.296484,-4.243747,9.825108,-7.336457,5.672903,-4.216841,8.275343,3.564594,2.883934,-8.732224,0.844957,-9.487679,0.708596,-6.173473,-0.146078,2.758197,1.242585,-0.441587,2.521063,-5.541376,8.085975,3.515272,4.454408,-1.843633,5.301105,-5.927340,2.152177,-0.913742,7.459874,-4.177580,5.078516,-0.349854,-8.696879,5.786025,4.072238,-7.067502,-4.413375,-4.203414,-9.518855,-3.460008,8.765562,-0.250364,-9.460106,4.237676,7.218315,8.356893,-7.214817,8.648201,-8.028158,-1.522156,-2.191861,6.858851,-4.756670,-9.616548,-6.893368,-2.046978,0.920135,0.693863,3.622049,-4.624211,-1.600136,-9.833310,6.727353,6.513814,-5.694378,0.046440,9.903778,-2.515551,-8.971255,-7.087239,6.971963,-1.203520,-6.956762,-5.290680,7.319459,-0.847056,0.840834,-1.467210,6.168418,-1.149065,1.145540,-8.838550,-4.706626,5.229283,-5.810326,-5.404710,-2.924564,-0.007301,-2.319546,6.762567,3.746463,8.172285,-3.029215,9.087959,-9.814774,3.815569,-6.520666,-8.276120,-2.963651,9.270132,1.020182,1.335108,5.411157,-9.008754,-7.895481,4.646659,-3.109239,-8.513123,-7.239356,-0.307530,-2.567264,-7.109617,3.309231,2.050284,-4.542412,-2.690111,-6.361097,-8.709238,-2.188637,0.710201,-6.992598,-5.132962,-5.097554,5.677528,1.664374,5.670603,4.543356,-6.507578,-6.493340,8.395993,-8.504728,-2.603294,8.173097,-3.651299,-2.772310,-7.793056,-9.747018,9.001708,-8.093189,5.001700,-4.484548,7.851631,7.297361,-7.643787,7.525321,-3.412063,-4.674308,9.068392,9.455462,0.349134,4.438490,-8.582883,-8.634728,-5.455398,-2.076807,-6.800589,-8.876049,2.243144,0.351331,7.847332,1.934363,6.449112,2.899634,9.065410,-5.698453,-3.367240,-6.183685,-1.994216,-9.474899,8.205739,-5.041148,2.398125,8.530679,-0.169651,-4.058878,-3.276885,-8.987853,6.519803,-8.188487,-7.755445,4.618021,-3.341535,-7.100990,7.563677,-9.803003,6.519495,-5.711862,4.601625,0.224519,6.864003,-0.706826,9.175050,6.689793,-5.759918,8.968947,-0.991985,9.327867,3.635951,2.999957,-9.908680,1.347097,9.880500,-5.916737,-6.475185,-7.726305,4.383072,3.237150,3.659597,-5.178989,-2.852878,4.960349,-1.986901,3.933317,-6.489351,-4.366490,-1.723320,-8.643824,-6.742114,7.004612,9.608361,-5.171013,-6.247265,6.164843,-0.224942,5.225728,-8.599817,2.068630,2.544333,-3.433280,-4.127013,-2.178246,-2.797496,-1.076014,9.798512,7.896478,9.211760,7.015941,5.052741,-4.790602,-5.529274,-2.685222,-9.703578,-7.792380,9.227404,2.513341,6.914949,-0.991676,-8.195844,-3.500560,-8.676365,-9.332288,9.332787,5.787931,0.028047,-1.721317,7.783600,-6.539108,7.522230,2.108858,0.443290,-5.024378,-5.682847,-2.640634,7.228154,-0.125000,2.739756,7.589141,9.580943,3.848027,-1.198448,-4.590965,9.360799,5.343170,5.135716,3.011063,9.214609,-1.259955,-0.813784,4.633462,0.302271,-2.644106,-9.771965,-2.361295,-0.171842,-7.092277,3.425219,7.768117,8.550956,5.201608,0.396545,5.015126,-1.276926,3.863585,7.094100,-8.660164,-2.053245,4.155918,9.538541,-2.208672,0.842618,-7.115369,-5.089350,6.736893,8.029728,-8.276388,1.674231,1.133208,1.482263,0.899734,6.627792,-1.540966,-6.238351,1.657532,4.983436,1.558576,-8.606666,6.156962,7.963085,3.380250,-0.577387,-6.763245,0.236721,7.880673,-2.380148,6.945932,7.840939,2.350823,5.578277,4.451311,7.009625,-4.096048,-9.114086,-7.104544,-1.815269,-9.474395,6.257720,8.438647,1.314812,-8.693185,9.468058,0.403825,0.612194,-6.664215,9.112872,8.679182,-4.214705,4.089689,6.260001,1.524453,8.697191,-6.827226,-2.405750,2.370655,2.159468,2.041978,-0.827095,6.128688,2.290952,-9.627811,0.420602,3.372474,9.260840,-9.305651,-0.171100,0.498366,-1.826876,1.632672,8.390960,-9.999943,-6.787363,3.942558,-1.388985,-0.103865,-1.951555,9.315191,-8.721399,9.088432,8.229515,-5.432721,8.753297,6.142508,-5.555953,-8.806990,5.562471,-3.373445,-7.500462,-0.713364,-2.227729,4.449143,-5.940930,-4.468022,1.359366,-6.308600,7.947210,5.100025,-0.205310,-2.993613,8.257106,-3.494677,8.028331,-7.896462,-3.848127,9.147502,9.895517,8.099679,8.676815,-0.241709,-9.530626,0.010275,8.351874,-2.492107,7.066622,-3.580782,-2.238925,6.135598,0.006165,3.397151,4.949777,-2.955880,4.246152,-9.609966,7.352186,-9.915747,1.111721,-1.015587,-2.005940,0.906342,8.606445,-4.922391,-7.910164,-5.979435,5.338858,-9.792026,-1.642829,9.825855,-3.446334,-4.251592,-0.309501,0.814344,-2.048331,-8.952799,4.176622,-5.346165,-2.213349,-3.511243,-9.538122,-4.390742,-6.584376,-8.482934,-6.936863,6.965434,0.813316,-1.821064,-1.109014,-9.057628,5.779690,9.065168,-4.110827,-8.591656,-0.037502,4.730635,1.188543,-5.902757,-8.314785,-1.470380,-8.345869,-2.388336,4.022847,7.134599,-1.416400,-5.794040,-2.582957,-0.831004,6.363795,2.369816,6.191052,-7.342199,3.803609,1.459578,-8.876452,-8.374390,1.923374,-3.599922,3.392500,-0.721726,7.985589,-4.757589,-8.520183,-7.482739,3.175143,2.035553,3.460272,0.566887,-7.807627,-6.695763,-3.641463,2.785500,0.207413,-2.308697,9.114208,3.527784,0.651520,-5.377926,-7.617745,3.373594,7.941602,1.914547,-4.095932,7.327851,6.475591,5.713521,-9.865505,8.227789,0.643472,-4.467026,-9.303926,3.162231,4.592766,2.172690,4.638098,5.358660,8.119814,7.067639,9.241510,-1.515902,-6.219411,-7.500152,-3.288127,1.805478,8.995929,-1.563083,1.501699,9.645683,9.857236,-1.156450,8.541477,4.543509,-0.080642,7.258624,0.535988,-5.528915,1.279341,-6.955329,-2.787238,7.722784,-7.399695,5.218801,-2.225450,-2.651055,7.256242,-0.949549,1.432660,4.725186,-7.233717,1.309801,-9.972881,8.675024,3.658793,4.828955,8.252014,4.285988,-9.069332,2.166238,-8.795802,1.867733,2.123580,-3.252154,9.700669,-1.110224,-3.259774,-2.860453,-6.321210,4.689107,3.021644,4.796263,8.204943,-9.729061,-9.930030,-8.980118,-5.057392,-8.962913,5.003209,-5.290034,1.517811,-0.380983,-9.576940,-1.528482,7.779805,-7.480792,3.994768,3.138477,2.399287,-8.812255,-7.855050,-5.334177,-9.252261,-1.845462,2.714798,7.521961,3.032060,2.549873,-5.499230,-0.056828,0.981180,-6.965386,3.626840,1.054537,-1.097775,-3.556499,8.231618,7.439625,6.859136,2.041542,-0.269960,1.746675,9.980060,0.746273,0.794586,3.817626,3.048069,7.751545,7.504340,1.606981,-1.029989,-0.961924,-1.372625,-1.357057,5.614861,-0.194800,-5.625726,-3.222469,-1.187095,7.472306,1.836745,-8.286471,-5.668046,7.084759,3.982405,9.130697,-1.195140,9.045319,1.492915,9.058569,9.732493,-9.389021,7.082227,6.171912,3.076699,1.294547,5.974305,1.315462,1.801825,-4.729628,0.788294,4.302687,4.170131,-5.665652,-7.264655,-1.364115,4.327676,9.525699,1.196348,3.596347,8.934370,6.833523,-8.501946,-4.077063,-2.023598,-6.057523,5.199446,5.314251,-4.868022,7.125282], dtype = "float64")#candidate|5549|(3360,)|const|float64
bop_5550 = relay.logical_and(call_5537.astype('bool'), relay.reshape(const_5549.astype('bool'), relay.shape_of(call_5537))) # shape=(3360,)
bop_5553 = relay.logical_and(call_5538.astype('bool'), relay.reshape(const_5549.astype('bool'), relay.shape_of(call_5538))) # shape=(3360,)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_5555 = relay.TupleGetItem(func_1858_call(), 0)
call_5556 = relay.TupleGetItem(func_1859_call(), 0)
func_4002_call = mod.get_global_var('func_4002')
func_4003_call = mutated_mod.get_global_var('func_4003')
call_5563 = relay.TupleGetItem(func_4002_call(), 0)
call_5564 = relay.TupleGetItem(func_4003_call(), 0)
func_4779_call = mod.get_global_var('func_4779')
func_4784_call = mutated_mod.get_global_var('func_4784')
var_5568 = relay.var("var_5568", dtype = "float32", shape = (546,))#candidate|5568|(546,)|var|float32
var_5569 = relay.var("var_5569", dtype = "float64", shape = (8, 12))#candidate|5569|(8, 12)|var|float64
call_5567 = relay.TupleGetItem(func_4779_call(relay.reshape(call_5537.astype('float64'), [2, 1680]), relay.reshape(var_5568.astype('float32'), [546,]), relay.reshape(var_5569.astype('float64'), [96,]), ), 1)
call_5570 = relay.TupleGetItem(func_4784_call(relay.reshape(call_5537.astype('float64'), [2, 1680]), relay.reshape(var_5568.astype('float32'), [546,]), relay.reshape(var_5569.astype('float64'), [96,]), ), 1)
func_842_call = mod.get_global_var('func_842')
func_848_call = mutated_mod.get_global_var('func_848')
const_5582 = relay.const([-9.390679,-8.354042,-2.697447,-1.375700,-8.250172,-8.405247,2.446848,5.005209,-0.377904,-9.644661,5.947608,1.545703,4.703766,6.832845,0.305140,4.125562,4.441373,1.113644,-3.133217,-6.479857,-0.992893,-5.367305,-4.228007,-8.726764], dtype = "float32")#candidate|5582|(24,)|const|float32
const_5583 = relay.const([[5,2,6,8,4,-2,6,4,-1,3,5,-10,-6,-5,4,7,-5,9,-8,-9,-3,-1,2,10],[-4,-9,2,-2,-6,7,2,9,4,1,7,4,3,-10,-1,-8,3,4,9,-4,-4,-6,4,6],[-5,9,8,-3,9,6,2,-4,5,10,5,10,-2,6,2,-5,-10,9,10,-7,-3,-10,10,2],[4,-7,6,6,4,6,-5,-2,-7,-3,3,5,-4,5,-9,-9,-10,9,6,6,9,-5,-4,1],[10,-6,3,-10,-6,-3,5,9,-10,1,-6,-3,8,-1,-7,-4,8,1,-3,10,-8,-6,7,-8],[4,3,6,-6,6,-7,-2,9,2,1,10,5,-6,-3,-4,2,-10,-7,10,1,1,-10,-2,2],[10,-7,5,-10,-1,-8,4,3,4,2,-3,4,2,6,-3,-8,-2,-3,7,9,-8,4,-8,8],[9,10,3,-8,5,1,-2,3,3,2,1,9,10,-3,-2,-2,1,5,-3,-2,-6,-8,-3,-4]], dtype = "int8")#candidate|5583|(8, 24)|const|int8
call_5581 = relay.TupleGetItem(func_842_call(relay.reshape(var_5569.astype('float64'), [16, 2, 3]), relay.reshape(var_5568.astype('float32'), [546,]), relay.reshape(const_5582.astype('float32'), [12, 2]), relay.reshape(const_5583.astype('int8'), [192,]), ), 1)
call_5584 = relay.TupleGetItem(func_848_call(relay.reshape(var_5569.astype('float64'), [16, 2, 3]), relay.reshape(var_5568.astype('float32'), [546,]), relay.reshape(const_5582.astype('float32'), [12, 2]), relay.reshape(const_5583.astype('int8'), [192,]), ), 1)
output = relay.Tuple([bop_5550,call_5555,call_5563,call_5567,var_5568,var_5569,call_5581,const_5582,const_5583,])
output2 = relay.Tuple([bop_5553,call_5556,call_5564,call_5570,var_5568,var_5569,call_5584,const_5582,const_5583,])
func_5589 = relay.Function([var_5568,var_5569,], output)
mod['func_5589'] = func_5589
mod = relay.transform.InferType()(mod)
var_5590 = relay.var("var_5590", dtype = "float32", shape = (546,))#candidate|5590|(546,)|var|float32
var_5591 = relay.var("var_5591", dtype = "float64", shape = (8, 12))#candidate|5591|(8, 12)|var|float64
output = func_5589(var_5590,var_5591,)
func_5592 = relay.Function([var_5590,var_5591,], output)
mutated_mod['func_5592'] = func_5592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_5599 = relay.TupleGetItem(func_1858_call(), 0)
call_5600 = relay.TupleGetItem(func_1859_call(), 0)
output = relay.Tuple([call_5599,])
output2 = relay.Tuple([call_5600,])
func_5608 = relay.Function([], output)
mod['func_5608'] = func_5608
mod = relay.transform.InferType()(mod)
output = func_5608()
func_5609 = relay.Function([], output)
mutated_mod['func_5609'] = func_5609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mod.get_global_var('func_2572')
func_2573_call = mutated_mod.get_global_var('func_2573')
call_5620 = relay.TupleGetItem(func_2572_call(), 0)
call_5621 = relay.TupleGetItem(func_2573_call(), 0)
output = relay.Tuple([call_5620,])
output2 = relay.Tuple([call_5621,])
func_5628 = relay.Function([], output)
mod['func_5628'] = func_5628
mod = relay.transform.InferType()(mod)
mutated_mod['func_5628'] = func_5628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5628_call = mutated_mod.get_global_var('func_5628')
call_5629 = func_5628_call()
output = call_5629
func_5630 = relay.Function([], output)
mutated_mod['func_5630'] = func_5630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_5653 = func_1704_call()
call_5654 = func_1704_call()
func_4407_call = mod.get_global_var('func_4407')
func_4408_call = mutated_mod.get_global_var('func_4408')
call_5690 = relay.TupleGetItem(func_4407_call(), 0)
call_5691 = relay.TupleGetItem(func_4408_call(), 0)
output = relay.Tuple([call_5653,call_5690,])
output2 = relay.Tuple([call_5654,call_5691,])
func_5696 = relay.Function([], output)
mod['func_5696'] = func_5696
mod = relay.transform.InferType()(mod)
output = func_5696()
func_5697 = relay.Function([], output)
mutated_mod['func_5697'] = func_5697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2530_call = mod.get_global_var('func_2530')
func_2532_call = mutated_mod.get_global_var('func_2532')
call_5770 = relay.TupleGetItem(func_2530_call(), 0)
call_5771 = relay.TupleGetItem(func_2532_call(), 0)
output = relay.Tuple([call_5770,])
output2 = relay.Tuple([call_5771,])
func_5818 = relay.Function([], output)
mod['func_5818'] = func_5818
mod = relay.transform.InferType()(mod)
output = func_5818()
func_5819 = relay.Function([], output)
mutated_mod['func_5819'] = func_5819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4312_call = mod.get_global_var('func_4312')
func_4314_call = mutated_mod.get_global_var('func_4314')
call_5820 = relay.TupleGetItem(func_4312_call(), 0)
call_5821 = relay.TupleGetItem(func_4314_call(), 0)
output = relay.Tuple([call_5820,])
output2 = relay.Tuple([call_5821,])
func_5839 = relay.Function([], output)
mod['func_5839'] = func_5839
mod = relay.transform.InferType()(mod)
mutated_mod['func_5839'] = func_5839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5839_call = mutated_mod.get_global_var('func_5839')
call_5840 = func_5839_call()
output = call_5840
func_5841 = relay.Function([], output)
mutated_mod['func_5841'] = func_5841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5421_call = mod.get_global_var('func_5421')
func_5422_call = mutated_mod.get_global_var('func_5422')
call_5884 = func_5421_call()
call_5885 = func_5421_call()
output = call_5884
output2 = call_5885
func_5901 = relay.Function([], output)
mod['func_5901'] = func_5901
mod = relay.transform.InferType()(mod)
output = func_5901()
func_5902 = relay.Function([], output)
mutated_mod['func_5902'] = func_5902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_5906 = func_1704_call()
call_5907 = func_1704_call()
output = call_5906
output2 = call_5907
func_5917 = relay.Function([], output)
mod['func_5917'] = func_5917
mod = relay.transform.InferType()(mod)
mutated_mod['func_5917'] = func_5917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5917_call = mutated_mod.get_global_var('func_5917')
call_5918 = func_5917_call()
output = call_5918
func_5919 = relay.Function([], output)
mutated_mod['func_5919'] = func_5919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_6002 = relay.TupleGetItem(func_1502_call(), 0)
call_6003 = relay.TupleGetItem(func_1504_call(), 0)
output = relay.Tuple([call_6002,])
output2 = relay.Tuple([call_6003,])
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
func_4754_call = mod.get_global_var('func_4754')
func_4756_call = mutated_mod.get_global_var('func_4756')
call_6020 = relay.TupleGetItem(func_4754_call(), 1)
call_6021 = relay.TupleGetItem(func_4756_call(), 1)
func_5177_call = mod.get_global_var('func_5177')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_6031 = relay.TupleGetItem(func_5177_call(), 1)
call_6032 = relay.TupleGetItem(func_5178_call(), 1)
output = relay.Tuple([call_6020,call_6031,])
output2 = relay.Tuple([call_6021,call_6032,])
func_6039 = relay.Function([], output)
mod['func_6039'] = func_6039
mod = relay.transform.InferType()(mod)
mutated_mod['func_6039'] = func_6039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6039_call = mutated_mod.get_global_var('func_6039')
call_6040 = func_6039_call()
output = call_6040
func_6041 = relay.Function([], output)
mutated_mod['func_6041'] = func_6041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_6042 = relay.TupleGetItem(func_1426_call(), 2)
call_6043 = relay.TupleGetItem(func_1428_call(), 2)
output = relay.Tuple([call_6042,])
output2 = relay.Tuple([call_6043,])
func_6063 = relay.Function([], output)
mod['func_6063'] = func_6063
mod = relay.transform.InferType()(mod)
mutated_mod['func_6063'] = func_6063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6063_call = mutated_mod.get_global_var('func_6063')
call_6064 = func_6063_call()
output = call_6064
func_6065 = relay.Function([], output)
mutated_mod['func_6065'] = func_6065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4407_call = mod.get_global_var('func_4407')
func_4408_call = mutated_mod.get_global_var('func_4408')
call_6087 = relay.TupleGetItem(func_4407_call(), 0)
call_6088 = relay.TupleGetItem(func_4408_call(), 0)
output = call_6087
output2 = call_6088
func_6091 = relay.Function([], output)
mod['func_6091'] = func_6091
mod = relay.transform.InferType()(mod)
output = func_6091()
func_6092 = relay.Function([], output)
mutated_mod['func_6092'] = func_6092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2787_call = mod.get_global_var('func_2787')
func_2789_call = mutated_mod.get_global_var('func_2789')
call_6133 = relay.TupleGetItem(func_2787_call(), 0)
call_6134 = relay.TupleGetItem(func_2789_call(), 0)
output = call_6133
output2 = call_6134
func_6153 = relay.Function([], output)
mod['func_6153'] = func_6153
mod = relay.transform.InferType()(mod)
output = func_6153()
func_6154 = relay.Function([], output)
mutated_mod['func_6154'] = func_6154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mod.get_global_var('func_2572')
func_2573_call = mutated_mod.get_global_var('func_2573')
call_6157 = relay.TupleGetItem(func_2572_call(), 0)
call_6158 = relay.TupleGetItem(func_2573_call(), 0)
func_3230_call = mod.get_global_var('func_3230')
func_3232_call = mutated_mod.get_global_var('func_3232')
call_6160 = func_3230_call()
call_6161 = func_3230_call()
func_5608_call = mod.get_global_var('func_5608')
func_5609_call = mutated_mod.get_global_var('func_5609')
call_6165 = relay.TupleGetItem(func_5608_call(), 0)
call_6166 = relay.TupleGetItem(func_5609_call(), 0)
func_4196_call = mod.get_global_var('func_4196')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_6182 = relay.TupleGetItem(func_4196_call(), 0)
call_6183 = relay.TupleGetItem(func_4197_call(), 0)
func_4153_call = mod.get_global_var('func_4153')
func_4156_call = mutated_mod.get_global_var('func_4156')
var_6191 = relay.var("var_6191", dtype = "bool", shape = (16,))#candidate|6191|(16,)|var|bool
call_6190 = relay.TupleGetItem(func_4153_call(relay.reshape(call_6160.astype('bool'), []), relay.reshape(var_6191.astype('bool'), [1, 4, 4]), ), 1)
call_6192 = relay.TupleGetItem(func_4156_call(relay.reshape(call_6160.astype('bool'), []), relay.reshape(var_6191.astype('bool'), [1, 4, 4]), ), 1)
func_2960_call = mod.get_global_var('func_2960')
func_2962_call = mutated_mod.get_global_var('func_2962')
call_6193 = func_2960_call(relay.reshape(call_6160.astype('uint32'), []))
call_6194 = func_2960_call(relay.reshape(call_6160.astype('uint32'), []))
output = relay.Tuple([call_6157,call_6160,call_6165,call_6182,call_6190,var_6191,call_6193,])
output2 = relay.Tuple([call_6158,call_6161,call_6166,call_6183,call_6192,var_6191,call_6194,])
func_6203 = relay.Function([var_6191,], output)
mod['func_6203'] = func_6203
mod = relay.transform.InferType()(mod)
mutated_mod['func_6203'] = func_6203
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6204 = relay.var("var_6204", dtype = "bool", shape = (16,))#candidate|6204|(16,)|var|bool
func_6203_call = mutated_mod.get_global_var('func_6203')
call_6205 = func_6203_call(var_6204)
output = call_6205
func_6206 = relay.Function([var_6204], output)
mutated_mod['func_6206'] = func_6206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4312_call = mod.get_global_var('func_4312')
func_4314_call = mutated_mod.get_global_var('func_4314')
call_6224 = relay.TupleGetItem(func_4312_call(), 0)
call_6225 = relay.TupleGetItem(func_4314_call(), 0)
output = relay.Tuple([call_6224,])
output2 = relay.Tuple([call_6225,])
func_6229 = relay.Function([], output)
mod['func_6229'] = func_6229
mod = relay.transform.InferType()(mod)
output = func_6229()
func_6230 = relay.Function([], output)
mutated_mod['func_6230'] = func_6230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4277_call = mod.get_global_var('func_4277')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_6234 = func_4277_call()
call_6235 = func_4277_call()
func_3968_call = mod.get_global_var('func_3968')
func_3971_call = mutated_mod.get_global_var('func_3971')
const_6246 = relay.const([-6,1,7,3,-2,1,4,-6,-8,-7,6,-1,10,-9,6,-5,2,10,-7,-1,-7,-4,10,9,-5,-6,8,7,7,5,8,6,5,9,-8,-10,3,-7,-4,-2,-3,-1,-8,-9,4,8,5,4,-9,-9,-5,5,-4,2,-9,8,3,-2,-10,3,6,-8,7,-10,-4,5,-9,7,3,1,4,-1,-1,-5,4,6,1,-1,-5,5,10,-9,2,-2,7,-6,-3,7,10,4,2,-5,4,-3,7,-8,-2,7,5,9,-3,5,2,1,-6,9,6,2,10,-9,-3,-7,6,-9,5,6,-2,5,3,-7,2,-6,10,10,-1,-8,-8,1,10,6,7,3,-3,5,-8,-4,10,1,-7,-9,-10,7,1,1,-8,-7,8,-6,2,-8,6,1,3,-6,-4,1,4,-1,7,-8,-10,-2,7,-1,3,-9,1,-7,-3,5,9,-1,-5,8,8,-7,-1,7,10,8,5,-2,-7,-1,3,-10,-1,3,-7,7,9,2,-4,-9,-6,8,2,10], dtype = "uint8")#candidate|6246|(198,)|const|uint8
call_6245 = func_3968_call(relay.reshape(const_6246.astype('uint8'), [2, 9, 11]), relay.reshape(const_6246.astype('uint8'), [2, 9, 11]), )
call_6247 = func_3968_call(relay.reshape(const_6246.astype('uint8'), [2, 9, 11]), relay.reshape(const_6246.astype('uint8'), [2, 9, 11]), )
output = relay.Tuple([call_6234,call_6245,const_6246,])
output2 = relay.Tuple([call_6235,call_6247,const_6246,])
func_6248 = relay.Function([], output)
mod['func_6248'] = func_6248
mod = relay.transform.InferType()(mod)
output = func_6248()
func_6249 = relay.Function([], output)
mutated_mod['func_6249'] = func_6249
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6276 = relay.const([[[4.414093,8.339505,3.858934,4.526243,9.015338,3.808521,7.419700,-7.276051,3.495708,9.526500,-2.821271,-0.296521,4.227021,0.282425,2.943696,5.245442],[1.015672,8.510872,1.898323,9.670387,-6.600736,-0.915832,0.717077,7.073042,6.360806,5.027560,-1.238773,-5.383889,0.223560,-5.388927,3.422694,9.267654],[-5.615398,8.311576,5.396997,-4.408013,2.822031,3.487098,9.662247,8.142978,-6.702076,3.824564,-4.017532,-8.146553,5.214253,-9.458789,-2.340177,-6.713074],[2.078290,-3.894155,-9.633937,-0.834544,0.873966,7.093955,-4.812030,-1.928600,0.393441,5.575389,9.344395,6.182906,-4.172307,7.359826,9.687268,7.942112],[1.831825,5.708627,1.557088,6.330946,-6.047760,6.502037,0.816977,2.763555,7.464832,-6.926548,-2.280814,-1.153514,-9.431950,4.418573,2.920837,-5.484943]],[[-4.318282,-8.309065,3.493588,4.958593,-2.573797,-3.433046,-1.977146,-8.677125,-9.791878,-1.120248,-1.056110,-0.853667,0.501036,-7.300479,-5.656133,6.421649],[8.691846,-5.554384,-5.308986,-6.685923,1.805566,-2.163066,-2.814971,3.868869,-1.792465,0.366016,-3.212057,4.421777,2.701870,-8.154646,-4.542993,-9.770233],[-3.533527,-0.284056,-8.969978,5.505545,4.095708,3.435949,2.276983,-0.553101,6.278915,-0.657901,8.737993,2.370813,-8.306612,2.576096,2.110760,-1.804010],[-2.893755,-5.766475,5.035077,-6.462824,-7.280369,-9.862758,6.362324,5.447118,-2.719986,-9.671390,4.417697,-6.065106,-0.408722,-1.904751,4.717077,4.147040],[6.983328,1.975015,2.536927,4.653716,3.104087,2.060885,-1.264495,0.575606,6.099396,9.309627,9.756796,-4.625882,4.414362,-8.519035,8.578459,-2.302103]]], dtype = "float32")#candidate|6276|(2, 5, 16)|const|float32
const_6277 = relay.const([[[7.587162,-2.668180,-4.194348,-1.696701,-0.543649,-1.115586,1.665676,0.540782,-9.535099,-2.124055,-1.788595,8.269105,-7.462452,-4.383654,2.059444,-8.656676],[5.271176,1.448995,2.154170,9.785611,4.971130,3.678618,6.067357,3.203726,-3.072024,-2.732513,1.648596,8.502240,-5.747945,-5.767768,2.044329,-9.244809],[0.248654,2.439253,5.801387,-9.350906,-4.836426,0.986797,0.140092,-3.255598,-4.326237,-4.424558,-1.484382,-1.698576,-2.716131,7.811398,1.363853,-4.327598],[1.935928,8.732671,-5.527288,9.520876,-8.102382,7.327145,0.427429,1.956852,-8.382449,4.949649,3.639728,-5.343286,5.823931,9.355895,7.295239,1.711580],[0.883295,-6.928209,4.924131,3.330090,-2.878905,1.232658,-3.772380,-3.688936,-4.119458,1.769316,6.048051,3.512684,1.006401,8.192661,-4.477387,-4.775065]],[[-5.300288,-3.258026,-0.788814,8.828334,-8.549137,7.442477,1.386492,1.678231,8.267565,1.248367,-8.615003,8.692487,1.988810,1.958793,-0.339450,-0.049712],[-1.817455,-7.945625,-2.317565,1.188926,-7.662753,7.602512,-5.397338,0.594731,4.663940,-6.278881,-4.472206,-7.450374,1.968355,7.709996,9.542619,-5.551366],[-2.329309,-2.646018,-3.752328,4.733161,-5.977672,-9.078564,-9.884533,7.103220,-4.472084,3.006486,8.356510,-1.492863,5.159005,-4.454212,5.326607,-0.737283],[8.596951,-4.319392,1.693012,-9.777495,-8.063868,-1.666743,2.607384,2.359297,-6.097432,-1.723618,-2.504385,-2.636360,-4.102085,-2.263251,2.609471,-6.933449],[3.943071,-5.168716,-4.881290,7.488204,4.800580,4.466322,5.562999,-4.639869,-4.617192,1.360543,9.797867,-8.773465,1.521606,-5.043418,-2.369000,6.217579]]], dtype = "float32")#candidate|6277|(2, 5, 16)|const|float32
bop_6278 = relay.subtract(const_6276.astype('float32'), relay.reshape(const_6277.astype('float32'), relay.shape_of(const_6276))) # shape=(2, 5, 16)
const_6282 = relay.const([[[-1.145979,4.102728,-9.432343,-6.121073,0.969788,-7.719265,-8.459335,9.533809,6.816651,7.419898,-6.415520,-3.339737,5.672628,-7.412843,2.200996,-9.064184],[-8.342206,4.203580,3.568409,-1.776680,9.128563,1.343885,-6.748906,7.428771,5.122280,1.311384,-7.806975,2.260986,-2.147987,-8.931151,-2.524590,4.892982],[6.907677,5.104368,-2.493287,6.823041,9.786608,-9.863465,-4.103955,3.545655,-1.494034,8.846959,-8.991880,-2.411922,-7.417106,-3.012436,5.646836,9.293341],[2.988019,4.841302,4.428876,2.804382,-7.559748,-9.264226,-4.865974,-2.980174,5.363891,0.165434,-7.241773,-6.613732,2.598979,0.682775,-3.043826,1.242842],[-8.339367,-6.465045,2.112269,-2.778024,4.966756,-4.861656,-0.297757,-9.772265,-8.784687,-4.645389,-6.603725,7.062472,5.579731,-8.988855,-9.056113,1.544174]],[[2.030508,-8.576439,-0.123614,-0.537273,1.367202,0.593710,7.186702,4.819673,8.610466,-9.584225,-5.792106,9.687562,3.286848,-2.566105,0.373066,-8.631246],[5.162675,-7.696305,7.234895,1.162714,4.245880,-6.821549,-8.870356,4.362638,6.901797,9.753959,2.507228,-9.411493,4.196527,-6.443677,-8.125385,2.932588],[4.867243,0.780268,-1.878012,-9.217830,4.691830,-2.446877,-4.462825,-7.823539,7.862279,-6.588505,-6.619953,5.379994,6.995009,3.761667,-3.552444,7.325112],[-1.377398,-2.622791,5.632304,-6.480539,-2.137644,-7.783520,-7.663596,-9.502483,0.877716,2.576160,4.730851,0.528030,-0.168555,6.949343,4.275692,7.124440],[3.848511,-7.357447,-2.230911,-2.786749,9.369405,3.495205,5.006988,8.980761,-3.458305,-9.454828,-9.262599,-8.247856,-1.478538,8.036895,-0.189551,3.297739]]], dtype = "float32")#candidate|6282|(2, 5, 16)|const|float32
bop_6283 = relay.mod(const_6276.astype('float32'), relay.reshape(const_6282.astype('float32'), relay.shape_of(const_6276))) # shape=(2, 5, 16)
output = relay.Tuple([bop_6278,bop_6283,])
output2 = relay.Tuple([bop_6278,bop_6283,])
func_6287 = relay.Function([], output)
mod['func_6287'] = func_6287
mod = relay.transform.InferType()(mod)
output = func_6287()
func_6288 = relay.Function([], output)
mutated_mod['func_6288'] = func_6288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6229_call = mod.get_global_var('func_6229')
func_6230_call = mutated_mod.get_global_var('func_6230')
call_6334 = relay.TupleGetItem(func_6229_call(), 0)
call_6335 = relay.TupleGetItem(func_6230_call(), 0)
func_4998_call = mod.get_global_var('func_4998')
func_5001_call = mutated_mod.get_global_var('func_5001')
var_6346 = relay.var("var_6346", dtype = "float32", shape = (6, 4))#candidate|6346|(6, 4)|var|float32
var_6347 = relay.var("var_6347", dtype = "float32", shape = (280,))#candidate|6347|(280,)|var|float32
call_6345 = relay.TupleGetItem(func_4998_call(relay.reshape(var_6346.astype('float32'), [2, 12]), relay.reshape(var_6347.astype('float32'), [70, 4]), ), 0)
call_6348 = relay.TupleGetItem(func_5001_call(relay.reshape(var_6346.astype('float32'), [2, 12]), relay.reshape(var_6347.astype('float32'), [70, 4]), ), 0)
func_5839_call = mod.get_global_var('func_5839')
func_5841_call = mutated_mod.get_global_var('func_5841')
call_6354 = relay.TupleGetItem(func_5839_call(), 0)
call_6355 = relay.TupleGetItem(func_5841_call(), 0)
output = relay.Tuple([call_6334,call_6345,var_6346,var_6347,call_6354,])
output2 = relay.Tuple([call_6335,call_6348,var_6346,var_6347,call_6355,])
func_6375 = relay.Function([var_6346,var_6347,], output)
mod['func_6375'] = func_6375
mod = relay.transform.InferType()(mod)
mutated_mod['func_6375'] = func_6375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6375_call = mutated_mod.get_global_var('func_6375')
var_6377 = relay.var("var_6377", dtype = "float32", shape = (6, 4))#candidate|6377|(6, 4)|var|float32
var_6378 = relay.var("var_6378", dtype = "float32", shape = (280,))#candidate|6378|(280,)|var|float32
call_6376 = func_6375_call(var_6377,var_6378,)
output = call_6376
func_6379 = relay.Function([var_6377,var_6378,], output)
mutated_mod['func_6379'] = func_6379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4196_call = mod.get_global_var('func_4196')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_6454 = relay.TupleGetItem(func_4196_call(), 0)
call_6455 = relay.TupleGetItem(func_4197_call(), 0)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_6469 = relay.TupleGetItem(func_1426_call(), 1)
call_6470 = relay.TupleGetItem(func_1428_call(), 1)
func_5818_call = mod.get_global_var('func_5818')
func_5819_call = mutated_mod.get_global_var('func_5819')
call_6487 = relay.TupleGetItem(func_5818_call(), 0)
call_6488 = relay.TupleGetItem(func_5819_call(), 0)
output = relay.Tuple([call_6454,call_6469,call_6487,])
output2 = relay.Tuple([call_6455,call_6470,call_6488,])
func_6503 = relay.Function([], output)
mod['func_6503'] = func_6503
mod = relay.transform.InferType()(mod)
mutated_mod['func_6503'] = func_6503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6503_call = mutated_mod.get_global_var('func_6503')
call_6504 = func_6503_call()
output = call_6504
func_6505 = relay.Function([], output)
mutated_mod['func_6505'] = func_6505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4407_call = mod.get_global_var('func_4407')
func_4408_call = mutated_mod.get_global_var('func_4408')
call_6535 = relay.TupleGetItem(func_4407_call(), 1)
call_6536 = relay.TupleGetItem(func_4408_call(), 1)
func_5177_call = mod.get_global_var('func_5177')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_6542 = relay.TupleGetItem(func_5177_call(), 4)
call_6543 = relay.TupleGetItem(func_5178_call(), 4)
func_126_call = mod.get_global_var('func_126')
func_129_call = mutated_mod.get_global_var('func_129')
const_6551 = relay.const([-3.568722,1.077228,-0.255663,-5.134940,-2.492685,-3.101639,-9.807631,5.467966,-8.168174,8.986352,-0.807866,2.191376,-6.378930,3.650991,-8.778690,3.103840,-6.613656,7.738444,-9.152330,-7.893111,1.130405,5.104348,5.637587,7.700619], dtype = "float32")#candidate|6551|(24,)|const|float32
call_6550 = relay.TupleGetItem(func_126_call(relay.reshape(const_6551.astype('float32'), [4, 1, 6])), 0)
call_6552 = relay.TupleGetItem(func_129_call(relay.reshape(const_6551.astype('float32'), [4, 1, 6])), 0)
func_5313_call = mod.get_global_var('func_5313')
func_5316_call = mutated_mod.get_global_var('func_5316')
var_6554 = relay.var("var_6554", dtype = "float32", shape = (3, 12))#candidate|6554|(3, 12)|var|float32
call_6553 = func_5313_call(relay.reshape(var_6554.astype('float32'), [3, 4, 3]), relay.reshape(var_6554.astype('float32'), [3, 4, 3]), )
call_6555 = func_5313_call(relay.reshape(var_6554.astype('float32'), [3, 4, 3]), relay.reshape(var_6554.astype('float32'), [3, 4, 3]), )
func_5177_call = mod.get_global_var('func_5177')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_6557 = relay.TupleGetItem(func_5177_call(), 0)
call_6558 = relay.TupleGetItem(func_5178_call(), 0)
output = relay.Tuple([call_6535,call_6542,call_6550,const_6551,call_6553,var_6554,call_6557,])
output2 = relay.Tuple([call_6536,call_6543,call_6552,const_6551,call_6555,var_6554,call_6558,])
func_6564 = relay.Function([var_6554,], output)
mod['func_6564'] = func_6564
mod = relay.transform.InferType()(mod)
var_6565 = relay.var("var_6565", dtype = "float32", shape = (3, 12))#candidate|6565|(3, 12)|var|float32
output = func_6564(var_6565)
func_6566 = relay.Function([var_6565], output)
mutated_mod['func_6566'] = func_6566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_6619 = relay.TupleGetItem(func_2912_call(), 1)
call_6620 = relay.TupleGetItem(func_2913_call(), 1)
func_4848_call = mod.get_global_var('func_4848')
func_4849_call = mutated_mod.get_global_var('func_4849')
call_6621 = relay.TupleGetItem(func_4848_call(), 1)
call_6622 = relay.TupleGetItem(func_4849_call(), 1)
output = relay.Tuple([call_6619,call_6621,])
output2 = relay.Tuple([call_6620,call_6622,])
func_6633 = relay.Function([], output)
mod['func_6633'] = func_6633
mod = relay.transform.InferType()(mod)
output = func_6633()
func_6634 = relay.Function([], output)
mutated_mod['func_6634'] = func_6634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6229_call = mod.get_global_var('func_6229')
func_6230_call = mutated_mod.get_global_var('func_6230')
call_6696 = relay.TupleGetItem(func_6229_call(), 0)
call_6697 = relay.TupleGetItem(func_6230_call(), 0)
output = call_6696
output2 = call_6697
func_6714 = relay.Function([], output)
mod['func_6714'] = func_6714
mod = relay.transform.InferType()(mod)
mutated_mod['func_6714'] = func_6714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6714_call = mutated_mod.get_global_var('func_6714')
call_6715 = func_6714_call()
output = call_6715
func_6716 = relay.Function([], output)
mutated_mod['func_6716'] = func_6716
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6731 = relay.var("var_6731", dtype = "float64", shape = (9, 14, 3))#candidate|6731|(9, 14, 3)|var|float64
uop_6732 = relay.log10(var_6731.astype('float64')) # shape=(9, 14, 3)
uop_6737 = relay.sigmoid(var_6731.astype('float64')) # shape=(9, 14, 3)
func_5245_call = mod.get_global_var('func_5245')
func_5247_call = mutated_mod.get_global_var('func_5247')
call_6739 = relay.TupleGetItem(func_5245_call(), 0)
call_6740 = relay.TupleGetItem(func_5247_call(), 0)
bop_6745 = relay.right_shift(uop_6732.astype('uint32'), call_6739.astype('uint32')) # shape=(9, 14, 3)
bop_6748 = relay.right_shift(uop_6732.astype('uint32'), call_6740.astype('uint32')) # shape=(9, 14, 3)
func_3809_call = mod.get_global_var('func_3809')
func_3811_call = mutated_mod.get_global_var('func_3811')
call_6752 = func_3809_call()
call_6753 = func_3809_call()
uop_6760 = relay.asinh(var_6731.astype('float32')) # shape=(9, 14, 3)
output = relay.Tuple([uop_6737,bop_6745,call_6752,uop_6760,])
output2 = relay.Tuple([uop_6737,bop_6748,call_6753,uop_6760,])
func_6775 = relay.Function([var_6731,], output)
mod['func_6775'] = func_6775
mod = relay.transform.InferType()(mod)
mutated_mod['func_6775'] = func_6775
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6776 = relay.var("var_6776", dtype = "float64", shape = (9, 14, 3))#candidate|6776|(9, 14, 3)|var|float64
func_6775_call = mutated_mod.get_global_var('func_6775')
call_6777 = func_6775_call(var_6776)
output = call_6777
func_6778 = relay.Function([var_6776], output)
mutated_mod['func_6778'] = func_6778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4928_call = mod.get_global_var('func_4928')
func_4930_call = mutated_mod.get_global_var('func_4930')
call_6856 = func_4928_call()
call_6857 = func_4928_call()
output = call_6856
output2 = call_6857
func_6859 = relay.Function([], output)
mod['func_6859'] = func_6859
mod = relay.transform.InferType()(mod)
mutated_mod['func_6859'] = func_6859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6859_call = mutated_mod.get_global_var('func_6859')
call_6860 = func_6859_call()
output = call_6860
func_6861 = relay.Function([], output)
mutated_mod['func_6861'] = func_6861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_6972 = relay.TupleGetItem(func_1426_call(), 0)
call_6973 = relay.TupleGetItem(func_1428_call(), 0)
output = relay.Tuple([call_6972,])
output2 = relay.Tuple([call_6973,])
func_6975 = relay.Function([], output)
mod['func_6975'] = func_6975
mod = relay.transform.InferType()(mod)
mutated_mod['func_6975'] = func_6975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6975_call = mutated_mod.get_global_var('func_6975')
call_6976 = func_6975_call()
output = call_6976
func_6977 = relay.Function([], output)
mutated_mod['func_6977'] = func_6977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_7001 = relay.TupleGetItem(func_1232_call(), 0)
call_7002 = relay.TupleGetItem(func_1234_call(), 0)
func_2145_call = mod.get_global_var('func_2145')
func_2151_call = mutated_mod.get_global_var('func_2151')
var_7017 = relay.var("var_7017", dtype = "uint8", shape = ())#candidate|7017|()|var|uint8
var_7018 = relay.var("var_7018", dtype = "uint8", shape = (420,))#candidate|7018|(420,)|var|uint8
var_7019 = relay.var("var_7019", dtype = "float32", shape = (91, 6))#candidate|7019|(91, 6)|var|float32
var_7020 = relay.var("var_7020", dtype = "float32", shape = (24,))#candidate|7020|(24,)|var|float32
call_7016 = relay.TupleGetItem(func_2145_call(relay.reshape(var_7017.astype('uint8'), []), relay.reshape(var_7018.astype('uint8'), [7, 5, 12]), relay.reshape(var_7019.astype('float32'), [1, 546]), relay.reshape(var_7020.astype('float32'), [24,]), ), 1)
call_7021 = relay.TupleGetItem(func_2151_call(relay.reshape(var_7017.astype('uint8'), []), relay.reshape(var_7018.astype('uint8'), [7, 5, 12]), relay.reshape(var_7019.astype('float32'), [1, 546]), relay.reshape(var_7020.astype('float32'), [24,]), ), 1)
output = relay.Tuple([call_7001,call_7016,var_7017,var_7018,var_7019,var_7020,])
output2 = relay.Tuple([call_7002,call_7021,var_7017,var_7018,var_7019,var_7020,])
func_7043 = relay.Function([var_7017,var_7018,var_7019,var_7020,], output)
mod['func_7043'] = func_7043
mod = relay.transform.InferType()(mod)
var_7044 = relay.var("var_7044", dtype = "uint8", shape = ())#candidate|7044|()|var|uint8
var_7045 = relay.var("var_7045", dtype = "uint8", shape = (420,))#candidate|7045|(420,)|var|uint8
var_7046 = relay.var("var_7046", dtype = "float32", shape = (91, 6))#candidate|7046|(91, 6)|var|float32
var_7047 = relay.var("var_7047", dtype = "float32", shape = (24,))#candidate|7047|(24,)|var|float32
output = func_7043(var_7044,var_7045,var_7046,var_7047,)
func_7048 = relay.Function([var_7044,var_7045,var_7046,var_7047,], output)
mutated_mod['func_7048'] = func_7048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5245_call = mod.get_global_var('func_5245')
func_5247_call = mutated_mod.get_global_var('func_5247')
call_7068 = relay.TupleGetItem(func_5245_call(), 0)
call_7069 = relay.TupleGetItem(func_5247_call(), 0)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_7073 = relay.TupleGetItem(func_3950_call(), 2)
call_7074 = relay.TupleGetItem(func_3952_call(), 2)
func_2530_call = mod.get_global_var('func_2530')
func_2532_call = mutated_mod.get_global_var('func_2532')
call_7085 = relay.TupleGetItem(func_2530_call(), 0)
call_7086 = relay.TupleGetItem(func_2532_call(), 0)
func_4153_call = mod.get_global_var('func_4153')
func_4156_call = mutated_mod.get_global_var('func_4156')
const_7093 = relay.const([[False,False,False,True],[True,True,True,False],[True,False,True,False],[False,True,False,False]], dtype = "bool")#candidate|7093|(4, 4)|const|bool
call_7092 = relay.TupleGetItem(func_4153_call(relay.reshape(call_7068.astype('bool'), []), relay.reshape(const_7093.astype('bool'), [1, 4, 4]), ), 2)
call_7094 = relay.TupleGetItem(func_4156_call(relay.reshape(call_7068.astype('bool'), []), relay.reshape(const_7093.astype('bool'), [1, 4, 4]), ), 2)
output = relay.Tuple([call_7068,call_7073,call_7085,call_7092,const_7093,])
output2 = relay.Tuple([call_7069,call_7074,call_7086,call_7094,const_7093,])
func_7097 = relay.Function([], output)
mod['func_7097'] = func_7097
mod = relay.transform.InferType()(mod)
output = func_7097()
func_7098 = relay.Function([], output)
mutated_mod['func_7098'] = func_7098
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7133 = relay.var("var_7133", dtype = "uint64", shape = (1, 4, 3))#candidate|7133|(1, 4, 3)|var|uint64
const_7134 = relay.const([[[2,2,6],[-8,-8,-4],[-4,-4,-2],[8,5,6]]], dtype = "uint64")#candidate|7134|(1, 4, 3)|const|uint64
bop_7135 = relay.equal(var_7133.astype('bool'), relay.reshape(const_7134.astype('bool'), relay.shape_of(var_7133))) # shape=(1, 4, 3)
func_5696_call = mod.get_global_var('func_5696')
func_5697_call = mutated_mod.get_global_var('func_5697')
call_7149 = relay.TupleGetItem(func_5696_call(), 1)
call_7150 = relay.TupleGetItem(func_5697_call(), 1)
bop_7152 = relay.not_equal(var_7133.astype('bool'), relay.reshape(bop_7135.astype('bool'), relay.shape_of(var_7133))) # shape=(1, 4, 3)
func_4848_call = mod.get_global_var('func_4848')
func_4849_call = mutated_mod.get_global_var('func_4849')
call_7155 = relay.TupleGetItem(func_4848_call(), 1)
call_7156 = relay.TupleGetItem(func_4849_call(), 1)
bop_7157 = relay.logical_or(bop_7152.astype('bool'), call_7155.astype('bool')) # shape=(1, 4, 3)
bop_7160 = relay.logical_or(bop_7152.astype('bool'), call_7156.astype('bool')) # shape=(1, 4, 3)
output = relay.Tuple([call_7149,bop_7157,])
output2 = relay.Tuple([call_7150,bop_7160,])
func_7162 = relay.Function([var_7133,], output)
mod['func_7162'] = func_7162
mod = relay.transform.InferType()(mod)
mutated_mod['func_7162'] = func_7162
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7163 = relay.var("var_7163", dtype = "uint64", shape = (1, 4, 3))#candidate|7163|(1, 4, 3)|var|uint64
func_7162_call = mutated_mod.get_global_var('func_7162')
call_7164 = func_7162_call(var_7163)
output = call_7164
func_7165 = relay.Function([var_7163], output)
mutated_mod['func_7165'] = func_7165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6063_call = mod.get_global_var('func_6063')
func_6065_call = mutated_mod.get_global_var('func_6065')
call_7172 = relay.TupleGetItem(func_6063_call(), 0)
call_7173 = relay.TupleGetItem(func_6065_call(), 0)
func_5010_call = mod.get_global_var('func_5010')
func_5012_call = mutated_mod.get_global_var('func_5012')
call_7191 = relay.TupleGetItem(func_5010_call(), 0)
call_7192 = relay.TupleGetItem(func_5012_call(), 0)
func_842_call = mod.get_global_var('func_842')
func_848_call = mutated_mod.get_global_var('func_848')
var_7213 = relay.var("var_7213", dtype = "float64", shape = (8, 12))#candidate|7213|(8, 12)|var|float64
const_7214 = relay.const([[9.820142,0.308511,3.996198,-1.551490,4.548559,-5.820283],[3.256341,-8.290240,-6.524752,-2.275813,-9.881735,-3.240635],[-9.125157,-9.599993,5.512734,-8.377090,3.084620,-7.911573],[6.199885,-5.076767,1.912854,7.435941,-9.276338,4.123321],[-2.569980,3.154273,9.440649,7.172826,5.864571,-9.434533],[0.096521,1.770695,2.313392,4.441557,-5.141016,8.425898],[-0.005884,-7.386330,-4.690680,-0.645609,4.247064,-9.114108],[5.124294,-3.862922,9.708208,3.991979,2.501493,-6.333632],[0.135363,7.618881,8.175907,0.467854,-4.516489,-3.832898],[-4.234477,3.877440,-2.561172,-7.797738,9.980745,-0.558855],[1.533574,5.683075,-1.454024,1.538462,1.502686,-1.798811],[5.738090,1.705356,1.426543,9.802027,-9.293534,-0.337350],[-1.173227,-4.608971,7.260098,-3.700208,7.345342,-4.235594],[4.023019,7.510566,-2.665837,-7.670108,9.280566,2.229023],[4.614483,-6.012782,3.267857,2.993319,8.954435,-2.156321],[-5.586897,-4.636073,-7.437035,-1.266526,-0.297520,1.775984],[2.763060,7.908102,9.448789,2.084104,6.019616,-6.103700],[-5.506315,-9.899522,6.632332,0.359197,8.824235,2.215835],[-1.569365,-6.913051,8.685771,4.326916,1.308166,-2.117549],[-8.817828,4.186230,4.558039,-1.239503,4.638808,-3.447504],[8.508992,4.097447,3.538107,7.397773,-8.696643,-5.482719],[8.793016,-6.603606,-4.662303,9.496083,-0.293675,-6.199641],[-9.303411,-1.862287,9.274588,-9.561312,-2.707765,-2.693891],[8.045489,5.743107,7.986962,6.855272,0.610438,7.467285],[-2.590059,-7.783343,8.740908,3.678149,-3.528479,-9.176844],[-3.642272,-0.675535,-6.446105,-9.037290,-9.168007,1.242119],[8.611315,-1.207882,-6.065110,2.151118,-1.831309,4.544088],[-0.431752,3.571307,-6.659225,3.487321,2.986781,7.855656],[-4.297495,7.014252,3.913690,-8.611588,6.511888,-3.953328],[-7.612474,4.954333,4.399129,-4.103979,1.526146,-5.368273],[9.859032,-8.982607,-8.163306,-9.516065,8.857968,3.890835],[-8.411251,0.705052,7.263209,5.682221,8.716579,-8.792363],[-7.563862,8.797540,9.462274,6.212459,7.520138,2.444211],[-4.162435,-9.604854,7.544624,-2.316795,0.245188,5.741409],[7.697210,-7.384591,3.246523,-9.979631,3.374698,2.146372],[7.930233,-9.149188,-5.364196,-4.603066,6.239285,-1.331582],[7.006627,1.669855,6.691934,9.519439,4.513617,8.051743],[-1.875762,-3.820280,0.178892,-6.875351,6.929956,2.999450],[-9.547665,-2.700445,-0.522021,-9.970901,2.591120,-5.467343],[7.407808,-6.256635,2.654507,0.470261,5.736912,-3.922903],[-4.489030,1.819399,8.090229,8.003125,0.165951,2.769518],[6.141374,3.759899,3.669234,4.008416,2.556954,-7.369010],[8.980962,-7.871681,1.359304,-9.019927,-4.243191,3.362005],[-4.690184,7.229413,-7.258984,-0.503251,4.517813,5.021428],[5.745984,7.413968,-7.115350,-8.737545,4.148575,-6.628815],[9.069779,-5.518973,-4.129210,2.323258,0.454416,-3.666012],[6.813800,9.632024,-4.256133,-5.881303,9.116195,-0.710995],[5.478855,1.963988,-1.030868,9.110453,-1.640841,2.922867],[-6.748477,-4.745461,4.211119,0.897604,0.395846,0.058358],[8.955144,2.687846,3.256544,-0.407833,-0.757048,-2.397746],[6.775687,-0.695668,8.333837,9.809143,-3.745507,1.915253],[-9.075152,2.369168,6.692738,-6.502008,-1.198531,9.820917],[4.241739,-1.362008,-1.360029,-8.119293,-3.092081,3.456322],[-8.637319,0.350719,-1.819504,2.645665,-8.211175,-6.193583],[5.106247,-3.377476,9.804635,-7.684867,-1.760599,-9.434849],[6.792436,-9.611692,-8.731815,7.088574,-9.527546,8.516175],[-1.069848,-2.714438,9.691483,-7.475117,0.617448,-2.649373],[3.442609,3.559982,7.767320,-8.116369,6.608660,1.438859],[-1.209224,-1.835178,9.132158,-7.294389,-7.643986,-9.524767],[4.791228,2.009934,-4.873799,5.686242,-6.834712,5.983244],[4.846314,-0.703523,-9.556536,-1.609340,-3.928708,-5.406447],[-5.012271,4.199742,2.294388,5.612713,4.522658,7.605657],[-3.905023,7.799422,1.788390,0.112389,-9.548548,4.775719],[3.943445,8.420718,3.061069,3.646465,-6.948689,-6.773952],[9.366248,1.619582,-6.420584,-1.039364,9.830873,7.248430],[-0.887711,5.541019,-1.957348,8.403710,-0.215582,-5.591810],[-2.888972,-8.970091,-4.079316,-2.519451,-2.223711,-7.872766],[-3.379059,3.077369,-6.794404,9.102786,8.901541,1.374343],[6.805216,7.867559,-9.823543,4.985977,-0.169280,0.161040],[7.733353,-9.902953,4.814829,-7.735009,2.008715,-1.998293],[0.431404,-6.754478,-5.099655,-7.453171,-5.760687,-7.930355],[6.796590,-4.448594,1.110895,5.876697,7.059498,-2.368616],[-1.328651,5.452468,-9.612481,-0.424108,4.589962,0.524860],[-4.204162,7.928600,7.662146,2.582975,-6.309777,-8.406932],[-0.942039,-0.965083,9.651944,-2.349667,8.772310,1.145252],[9.240458,0.324828,-0.003629,1.085745,1.532939,-2.940136],[-1.016913,6.250461,1.125338,-6.685598,6.258788,8.325861],[5.748696,0.080110,7.023047,-5.924063,-8.489927,8.757638],[-3.211560,7.436530,-2.403569,0.613934,-6.083762,5.513120],[-2.790349,3.011988,-6.159263,1.650347,-5.512160,-6.666290],[4.446957,4.324316,4.232459,9.974054,3.115689,8.659442],[-0.154909,-4.608889,4.811146,-6.441609,7.915281,-4.431128],[-4.996455,9.248048,-6.834725,3.913249,-5.960968,7.229168],[8.311608,-0.637827,5.151459,-8.787646,-9.565169,-6.522054],[-1.241960,6.405035,-8.507242,3.617192,0.352670,-7.761457],[9.543999,-6.955794,-1.957317,3.248281,-0.215345,-2.326504],[6.710013,6.486629,7.457280,3.129424,-7.714222,5.859013],[-5.647704,1.059010,5.068693,9.331611,5.119863,-0.570855],[1.240532,-3.316310,5.949603,-4.619570,9.327741,-6.979650],[5.562046,0.343386,8.114919,9.135371,5.056343,9.410455],[-4.559165,0.035424,-1.038697,3.627943,7.892881,3.504716]], dtype = "float32")#candidate|7214|(91, 6)|const|float32
var_7215 = relay.var("var_7215", dtype = "float32", shape = (24,))#candidate|7215|(24,)|var|float32
const_7216 = relay.const([-2,10,-7,10,-7,-2,9,-9,9,8,4,6,-5,-2,-7,-1,-4,-6,7,6,-5,4,8,-4,9,-4,9,9,-1,2,-9,-4,3,3,6,-6,8,4,-3,-2,2,5,8,-5,4,4,10,8,9,-5,-1,-5,9,4,10,4,3,-1,-5,9,-6,5,-2,1,-4,-8,5,5,-5,-8,6,6,1,-2,6,6,-6,-9,-3,2,5,4,3,6,8,-4,-3,-8,10,3,-3,9,9,10,8,-1,3,-3,-5,-6,-2,-9,-1,-1,7,8,-2,-9,-4,-5,2,5,9,4,6,7,2,-3,3,5,-8,9,-1,1,9,10,-1,-9,-3,-4,-4,-9,9,9,-9,-3,7,-7,2,6,3,7,10,-4,-10,6,-1,8,10,-3,2,-4,-8,9,-8,-3,10,-4,-7,-5,-7,9,-7,-2,-4,6,1,-7,2,2,1,-2,7,-3,-4,-9,1,-3,-5,-7,-9,7,4,2,-9,7,-2,-3,5,-1,-8,4], dtype = "int8")#candidate|7216|(192,)|const|int8
call_7212 = relay.TupleGetItem(func_842_call(relay.reshape(var_7213.astype('float64'), [16, 2, 3]), relay.reshape(const_7214.astype('float32'), [546,]), relay.reshape(var_7215.astype('float32'), [12, 2]), relay.reshape(const_7216.astype('int8'), [192,]), ), 4)
call_7217 = relay.TupleGetItem(func_848_call(relay.reshape(var_7213.astype('float64'), [16, 2, 3]), relay.reshape(const_7214.astype('float32'), [546,]), relay.reshape(var_7215.astype('float32'), [12, 2]), relay.reshape(const_7216.astype('int8'), [192,]), ), 4)
output = relay.Tuple([call_7172,call_7191,call_7212,var_7213,const_7214,var_7215,const_7216,])
output2 = relay.Tuple([call_7173,call_7192,call_7217,var_7213,const_7214,var_7215,const_7216,])
func_7221 = relay.Function([var_7213,var_7215,], output)
mod['func_7221'] = func_7221
mod = relay.transform.InferType()(mod)
var_7222 = relay.var("var_7222", dtype = "float64", shape = (8, 12))#candidate|7222|(8, 12)|var|float64
var_7223 = relay.var("var_7223", dtype = "float32", shape = (24,))#candidate|7223|(24,)|var|float32
output = func_7221(var_7222,var_7223,)
func_7224 = relay.Function([var_7222,var_7223,], output)
mutated_mod['func_7224'] = func_7224
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7268 = relay.var("var_7268", dtype = "float64", shape = (3, 14, 16))#candidate|7268|(3, 14, 16)|var|float64
uop_7269 = relay.sigmoid(var_7268.astype('float64')) # shape=(3, 14, 16)
func_4815_call = mod.get_global_var('func_4815')
func_4818_call = mutated_mod.get_global_var('func_4818')
const_7275 = relay.const([-7.675540,0.883115,-9.469547,1.503871,6.492559,-8.134018,-2.979640,-8.502198,-7.796670,-8.950334,3.804506,-7.864491,7.748116,5.819506,8.269749,8.351674,-4.338772,-6.299031,-7.637894,5.162875,-7.788997,3.623215,7.499255,-1.249092,8.388201,3.205934,-1.439794,8.091479,-3.644950,4.760686,8.387591,4.139074,2.699628,-3.764317,2.338729,5.896616,4.237998,-7.505922,-9.505040,9.432008,5.067772,7.761542,-2.136187,7.631780,7.084148,8.912257,-6.309241,-8.123922,-2.627340,9.434651,9.805107,1.470138,9.140052,3.601424,-8.352357,7.031918,6.277068,-4.842443,4.608308,-6.329045,-1.664616,7.675742,-8.361011,-0.392569,2.393789,-0.598515,8.600006,2.907802,7.617598,-4.819745,3.157729,1.269745,-1.774856,9.636699,2.306967,-2.315322,5.604000,-5.505020,-3.635465,-2.199411,1.514868,-0.358650,-2.400265,5.056925,-5.818482,-1.098388,-3.312479,-8.114838,8.466377,-9.895044,5.113883,-9.037065,7.591991,-8.581854,9.840282,6.606422,7.294598,0.762815,0.373668,2.805879,2.580314,-1.196416,0.644438,-9.096025,-3.025638,1.804712,-6.834041,-6.756032,1.620189,6.397787,6.851835,1.502270,-0.362919,-3.005716,9.084838,4.446034,8.131982,-6.917608,-2.811803,4.416966,-9.872508,-9.848451,-5.234701,-2.201312,7.699701,1.758462,-6.421776,6.427636,6.620950,-5.974242,8.984760,2.628884,6.474720,3.616750,8.323987,-3.304698,0.527160,-9.387891,0.621014,9.918162,-7.128057,2.006223,4.409418,0.568162,8.049401,-9.409421,1.692086,1.976018,9.771121,-1.054216,-1.547598,-0.649997,7.779673,2.789344,5.122696,9.628114,0.955560,-1.675321,1.168584,-8.200466,-2.303522,9.773536,-4.118183,-8.057238,4.898315,-9.032329,-7.498368,3.326932,3.791357,-4.244215,-1.375932,-5.236072,6.823705,-3.361247,-6.165837,8.148126,4.170000,-6.976006,7.550864,-0.856827,4.011940,-0.760984,6.653545,1.186298,2.274407,-4.880836,7.027757,3.282476,8.147291,3.627810,-2.788492,-3.399901,8.544931,-2.807978,-0.963008,9.291912,9.033261,2.360086,-2.243168,-4.511694,-8.680467,1.881644,4.511668,-5.317643,-1.726556,0.521073,-4.001227,9.692532,-3.989876,9.342855,-9.404404,2.745505,-7.858235,-1.657386,9.670865,-8.640243,5.164898,-5.119523,8.732994,-3.676826,-4.827999,-8.412877,7.775905,2.498927,6.336674,-6.078307,1.106151,-1.185444,-2.134228,-7.476032,7.508136,-4.659545,-6.647055,1.064946,2.019236,-8.722745,7.370545,5.693988,-4.067736,3.065917,8.009945,5.107016,5.504182,-8.494732,-2.179940,8.556698,-2.910701,2.054022,-9.780212,-0.359644,-2.557085,-0.189208,8.334030,-5.053966,-8.607757,-0.429002,-1.425538,-5.347541,1.399358,7.447151,-6.662928,6.890918,-9.112048,6.656324,5.025110,3.114016,-9.265963,-5.388080,5.074398,9.220881,-1.577168,5.877850,4.113891,-4.287597,-2.993418,4.960608,-5.322440,6.285616,0.751566,-9.408690,-7.435134,-9.443361,5.586468,3.736888,6.151352,-2.063633,-1.413260,-5.553829,2.620872,-3.386234,2.539578,-4.601890,-5.470651,-9.161289,4.891727,-4.863198,-7.022574,-4.020834,1.328884,-5.887986,5.524244,-2.146001,-1.931704,5.659362,8.171648,-3.392790,1.799776,1.756749,-4.941165,7.445159,-4.704906,-2.196352,-2.050553,-5.201053,-1.644502,7.185601,7.777878,6.624883,-8.903350,4.797271,-4.865816,-6.778749,1.918520,9.270803,-9.700149,2.208677,-5.860246,8.542935,-8.132977,8.983158,6.216907,-2.302506,-7.860060,-7.283469,6.993696,8.565200,7.565889,2.194994,8.720263,0.215922,-3.496404,-2.076021,-1.107217,3.498871,5.880762,9.979718,3.955332,4.112173,2.498375,9.408869,7.007218,-9.292250,-6.541540,0.483468,-0.269577,7.187881,9.602222,0.636401,-5.053781,4.879128,1.900166,-3.931243,-4.357841,3.043560,9.463866,-9.533165,8.158842,-5.439417,7.849897,2.538950,-8.521704,-8.204062,-4.035630,7.733013,-9.398393,-3.436561,8.920421,9.280675,-8.085144,4.720882,0.485681,-1.329357,-9.764718,-2.662776,4.240580,6.359934,4.764656,3.974065,1.628423,-9.744374,7.009352,-4.088609,1.124213,4.211639,-5.267180,8.499751,-1.826709,-8.464692,-0.814685,-9.851909,-0.621891,2.070972,3.421770,0.296248,3.984241,1.091549,-6.253701,8.295784,4.731203,9.011306,7.738350,2.547393,-7.763816,-6.150638,-3.540043,-6.095408,-5.800813,-2.557357,0.867398,8.042399,1.065841,3.884665,-3.636781,5.289972,4.466465,3.548429,-2.463793,5.998611,-5.812360,8.029023,-6.121386,4.630856,-4.039150,1.465505,0.130613,-0.954905,4.644608,-0.894483,7.887509,6.659572,-8.165802,6.300199,4.757952,8.222869,7.603864,-9.073649,5.288010,-5.527254,-8.623098,7.393257,-0.588708,-4.334867,2.992612,5.716673,2.812954,-4.273463,1.972031,-8.879912,-8.246089,-6.429848,-7.962586,8.519757,-4.279557,5.046908,4.868135,-9.130666,1.955265,8.749648,4.359011,4.197097,6.130010,-6.705871,7.549745,1.742297,4.458602,7.803429,6.687779,3.938435,0.769423,-8.869671], dtype = "float64")#candidate|7275|(480,)|const|float64
call_7274 = func_4815_call(relay.reshape(const_7275.astype('float64'), [10, 16, 3]))
call_7276 = func_4815_call(relay.reshape(const_7275.astype('float64'), [10, 16, 3]))
bop_7280 = relay.floor_divide(uop_7269.astype('float64'), relay.reshape(var_7268.astype('float64'), relay.shape_of(uop_7269))) # shape=(3, 14, 16)
output = relay.Tuple([call_7274,const_7275,bop_7280,])
output2 = relay.Tuple([call_7276,const_7275,bop_7280,])
func_7287 = relay.Function([var_7268,], output)
mod['func_7287'] = func_7287
mod = relay.transform.InferType()(mod)
var_7288 = relay.var("var_7288", dtype = "float64", shape = (3, 14, 16))#candidate|7288|(3, 14, 16)|var|float64
output = func_7287(var_7288)
func_7289 = relay.Function([var_7288], output)
mutated_mod['func_7289'] = func_7289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5839_call = mod.get_global_var('func_5839')
func_5841_call = mutated_mod.get_global_var('func_5841')
call_7299 = relay.TupleGetItem(func_5839_call(), 0)
call_7300 = relay.TupleGetItem(func_5841_call(), 0)
output = call_7299
output2 = call_7300
func_7307 = relay.Function([], output)
mod['func_7307'] = func_7307
mod = relay.transform.InferType()(mod)
output = func_7307()
func_7308 = relay.Function([], output)
mutated_mod['func_7308'] = func_7308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4277_call = mod.get_global_var('func_4277')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_7381 = func_4277_call()
call_7382 = func_4277_call()
func_5608_call = mod.get_global_var('func_5608')
func_5609_call = mutated_mod.get_global_var('func_5609')
call_7397 = relay.TupleGetItem(func_5608_call(), 0)
call_7398 = relay.TupleGetItem(func_5609_call(), 0)
output = relay.Tuple([call_7381,call_7397,])
output2 = relay.Tuple([call_7382,call_7398,])
func_7423 = relay.Function([], output)
mod['func_7423'] = func_7423
mod = relay.transform.InferType()(mod)
output = func_7423()
func_7424 = relay.Function([], output)
mutated_mod['func_7424'] = func_7424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6287_call = mod.get_global_var('func_6287')
func_6288_call = mutated_mod.get_global_var('func_6288')
call_7428 = relay.TupleGetItem(func_6287_call(), 0)
call_7429 = relay.TupleGetItem(func_6288_call(), 0)
func_6633_call = mod.get_global_var('func_6633')
func_6634_call = mutated_mod.get_global_var('func_6634')
call_7459 = relay.TupleGetItem(func_6633_call(), 1)
call_7460 = relay.TupleGetItem(func_6634_call(), 1)
func_6203_call = mod.get_global_var('func_6203')
func_6206_call = mutated_mod.get_global_var('func_6206')
var_7462 = relay.var("var_7462", dtype = "bool", shape = (16,))#candidate|7462|(16,)|var|bool
call_7461 = relay.TupleGetItem(func_6203_call(relay.reshape(var_7462.astype('bool'), [16,])), 0)
call_7463 = relay.TupleGetItem(func_6206_call(relay.reshape(var_7462.astype('bool'), [16,])), 0)
output = relay.Tuple([call_7428,call_7459,call_7461,var_7462,])
output2 = relay.Tuple([call_7429,call_7460,call_7463,var_7462,])
func_7481 = relay.Function([var_7462,], output)
mod['func_7481'] = func_7481
mod = relay.transform.InferType()(mod)
var_7482 = relay.var("var_7482", dtype = "bool", shape = (16,))#candidate|7482|(16,)|var|bool
output = func_7481(var_7482)
func_7483 = relay.Function([var_7482], output)
mutated_mod['func_7483'] = func_7483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4407_call = mod.get_global_var('func_4407')
func_4408_call = mutated_mod.get_global_var('func_4408')
call_7561 = relay.TupleGetItem(func_4407_call(), 1)
call_7562 = relay.TupleGetItem(func_4408_call(), 1)
output = relay.Tuple([call_7561,])
output2 = relay.Tuple([call_7562,])
func_7563 = relay.Function([], output)
mod['func_7563'] = func_7563
mod = relay.transform.InferType()(mod)
output = func_7563()
func_7564 = relay.Function([], output)
mutated_mod['func_7564'] = func_7564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_7643 = relay.TupleGetItem(func_1318_call(), 0)
call_7644 = relay.TupleGetItem(func_1319_call(), 0)
func_5839_call = mod.get_global_var('func_5839')
func_5841_call = mutated_mod.get_global_var('func_5841')
call_7654 = relay.TupleGetItem(func_5839_call(), 0)
call_7655 = relay.TupleGetItem(func_5841_call(), 0)
func_4807_call = mod.get_global_var('func_4807')
func_4809_call = mutated_mod.get_global_var('func_4809')
call_7657 = relay.TupleGetItem(func_4807_call(), 0)
call_7658 = relay.TupleGetItem(func_4809_call(), 0)
output = relay.Tuple([call_7643,call_7654,call_7657,])
output2 = relay.Tuple([call_7644,call_7655,call_7658,])
func_7667 = relay.Function([], output)
mod['func_7667'] = func_7667
mod = relay.transform.InferType()(mod)
output = func_7667()
func_7668 = relay.Function([], output)
mutated_mod['func_7668'] = func_7668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_7689 = relay.TupleGetItem(func_1502_call(), 0)
call_7690 = relay.TupleGetItem(func_1504_call(), 0)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_7713 = relay.TupleGetItem(func_3950_call(), 1)
call_7714 = relay.TupleGetItem(func_3952_call(), 1)
func_7043_call = mod.get_global_var('func_7043')
func_7048_call = mutated_mod.get_global_var('func_7048')
const_7717 = relay.const(-4, dtype = "uint8")#candidate|7717|()|const|uint8
const_7718 = relay.const([6,-2,-9,1,3,9,6,8,-4,9,-4,9,-3,1,-3,-5,-8,-4,-3,-2,-6,10,10,3,5,-1,4,10,-4,5,3,-8,6,-7,-4,7,1,-3,-5,5,6,-6,8,8,-7,9,2,3,9,8,9,5,-3,3,3,-8,5,-3,-10,-5,3,-6,-9,-2,-9,2,-6,-9,5,8,1,-1,8,9,5,4,8,-3,-9,5,-7,-7,6,-3,8,-1,7,-7,-7,4,2,10,-10,-7,9,-8,-1,-1,-8,9,8,-9,3,-4,2,-2,6,4,-4,6,3,4,-6,10,-1,-4,-9,8,8,-4,-7,-5,-8,-2,10,-8,1,-4,6,3,-2,-8,9,-5,-7,-7,5,9,3,-6,9,-3,-7,-7,2,2,-6,-5,8,2,-8,2,-3,7,-2,8,-6,-2,-9,-7,9,-4,-4,2,8,-9,-2,-2,-2,10,9,-7,-10,-1,10,-9,9,-3,-2,-5,8,-9,-3,-7,9,10,7,4,-8,8,4,4,1,-4,-4,-5,3,5,8,-2,1,-4,1,8,4,-7,3,10,1,-9,5,7,2,7,-4,-5,-2,5,-9,-3,9,1,-1,6,-9,9,10,5,8,2,-10,8,7,5,8,-9,8,-9,-5,3,3,-7,7,-7,-3,-8,-5,4,2,10,-7,-7,10,-6,-4,-8,-2,-9,8,-8,4,-1,4,3,-5,6,-1,-9,-10,8,5,-8,-3,-7,-1,-2,-1,-4,-8,-1,-9,7,1,-4,10,-4,10,-1,8,-5,-3,6,10,10,-8,-1,9,8,3,-2,6,5,7,2,-3,4,2,1,9,-9,2,5,-7,3,7,-2,-1,-2,2,2,8,3,-6,-1,-4,4,-2,9,-2,-1,8,-3,-10,-7,-6,8,-5,-4,-5,-7,-9,7,10,1,10,10,-5,7,5,-6,3,4,4,10,-7,10,-10,5,3,-9,-10,-1,1,10,3,8,1,5,-2,-7,-4,4,4,-1,7,-9,10,-4,9,-8,2,-8,7,-10,-8,7,6,5,3,4,-7,-9,-3,1,-8,4,-4,5,-6,2,6,6,-3,9,-7,7,7,3,10,-4,3,-10,-8,2,-4,8,6,-9,6,-4], dtype = "uint8")#candidate|7718|(420,)|const|uint8
var_7719 = relay.var("var_7719", dtype = "float32", shape = (546,))#candidate|7719|(546,)|var|float32
const_7720 = relay.const([7.469231,3.109925,1.620742,-5.428367,8.268979,-3.180641,8.608944,9.193863,-0.055538,8.922824,1.023929,-3.904476,-3.033979,-1.187768,-5.826837,1.271287,4.081247,5.254825,8.813094,-4.784476,6.053400,0.452663,7.548991,1.871137], dtype = "float32")#candidate|7720|(24,)|const|float32
call_7716 = relay.TupleGetItem(func_7043_call(relay.reshape(const_7717.astype('uint8'), []), relay.reshape(const_7718.astype('uint8'), [420,]), relay.reshape(var_7719.astype('float32'), [91, 6]), relay.reshape(const_7720.astype('float32'), [24,]), ), 1)
call_7721 = relay.TupleGetItem(func_7048_call(relay.reshape(const_7717.astype('uint8'), []), relay.reshape(const_7718.astype('uint8'), [420,]), relay.reshape(var_7719.astype('float32'), [91, 6]), relay.reshape(const_7720.astype('float32'), [24,]), ), 1)
func_1797_call = mod.get_global_var('func_1797')
func_1798_call = mutated_mod.get_global_var('func_1798')
call_7740 = relay.TupleGetItem(func_1797_call(), 0)
call_7741 = relay.TupleGetItem(func_1798_call(), 0)
func_5589_call = mod.get_global_var('func_5589')
func_5592_call = mutated_mod.get_global_var('func_5592')
var_7766 = relay.var("var_7766", dtype = "float64", shape = (96,))#candidate|7766|(96,)|var|float64
call_7765 = relay.TupleGetItem(func_5589_call(relay.reshape(var_7719.astype('float32'), [546,]), relay.reshape(var_7766.astype('float64'), [8, 12]), ), 4)
call_7767 = relay.TupleGetItem(func_5592_call(relay.reshape(var_7719.astype('float32'), [546,]), relay.reshape(var_7766.astype('float64'), [8, 12]), ), 4)
output = relay.Tuple([call_7689,call_7713,call_7716,const_7717,const_7718,var_7719,const_7720,call_7740,call_7765,var_7766,])
output2 = relay.Tuple([call_7690,call_7714,call_7721,const_7717,const_7718,var_7719,const_7720,call_7741,call_7767,var_7766,])
func_7769 = relay.Function([var_7719,var_7766,], output)
mod['func_7769'] = func_7769
mod = relay.transform.InferType()(mod)
mutated_mod['func_7769'] = func_7769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7769_call = mutated_mod.get_global_var('func_7769')
var_7771 = relay.var("var_7771", dtype = "float32", shape = (546,))#candidate|7771|(546,)|var|float32
var_7772 = relay.var("var_7772", dtype = "float64", shape = (96,))#candidate|7772|(96,)|var|float64
call_7770 = func_7769_call(var_7771,var_7772,)
output = call_7770
func_7773 = relay.Function([var_7771,var_7772,], output)
mutated_mod['func_7773'] = func_7773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6503_call = mod.get_global_var('func_6503')
func_6505_call = mutated_mod.get_global_var('func_6505')
call_7817 = relay.TupleGetItem(func_6503_call(), 2)
call_7818 = relay.TupleGetItem(func_6505_call(), 2)
output = call_7817
output2 = call_7818
func_7819 = relay.Function([], output)
mod['func_7819'] = func_7819
mod = relay.transform.InferType()(mod)
output = func_7819()
func_7820 = relay.Function([], output)
mutated_mod['func_7820'] = func_7820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6633_call = mod.get_global_var('func_6633')
func_6634_call = mutated_mod.get_global_var('func_6634')
call_7837 = relay.TupleGetItem(func_6633_call(), 1)
call_7838 = relay.TupleGetItem(func_6634_call(), 1)
func_3968_call = mod.get_global_var('func_3968')
func_3971_call = mutated_mod.get_global_var('func_3971')
const_7849 = relay.const([4,-9,-7,2,4,6,-4,6,-3,3,6,2,8,7,3,-9,1,7,-10,-4,8,4,10,-9,10,1,-1,8,-2,-7,6,-3,3,4,8,6,7,-8,-2,4,-1,10,7,1,4,8,3,-6,9,10,8,-3,-7,-6,2,-3,-4,-4,10,2,-3,-5,-10,-5,-10,8,2,-5,-4,2,-10,10,-7,-4,-10,-2,-7,-9,7,-7,10,7,9,-5,-2,1,-1,5,-5,-8,5,6,-6,-8,3,-1,3,7,9,-6,-10,-2,-8,-10,6,-6,7,-1,-10,-7,8,-6,-6,-4,-6,6,9,-6,5,-10,5,9,1,-4,-3,-4,10,4,4,1,-10,7,-4,-6,2,-9,-5,6,2,-7,-2,8,10,6,-9,5,3,-9,-6,8,-3,2,9,4,-9,-8,1,-10,7,-6,-4,-8,-4,6,3,7,-4,6,8,-5,-10,-7,-9,1,-5,-2,9,-6,8,4,-9,-9,-3,-4,-2,7,2,-2,-10,-6,-3,4,10,-4,3,10,-10,-2], dtype = "uint8")#candidate|7849|(198,)|const|uint8
call_7848 = func_3968_call(relay.reshape(const_7849.astype('uint8'), [2, 9, 11]), relay.reshape(const_7849.astype('uint8'), [2, 9, 11]), )
call_7850 = func_3968_call(relay.reshape(const_7849.astype('uint8'), [2, 9, 11]), relay.reshape(const_7849.astype('uint8'), [2, 9, 11]), )
output = relay.Tuple([call_7837,call_7848,const_7849,])
output2 = relay.Tuple([call_7838,call_7850,const_7849,])
func_7855 = relay.Function([], output)
mod['func_7855'] = func_7855
mod = relay.transform.InferType()(mod)
mutated_mod['func_7855'] = func_7855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7855_call = mutated_mod.get_global_var('func_7855')
call_7856 = func_7855_call()
output = call_7856
func_7857 = relay.Function([], output)
mutated_mod['func_7857'] = func_7857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6063_call = mod.get_global_var('func_6063')
func_6065_call = mutated_mod.get_global_var('func_6065')
call_7860 = relay.TupleGetItem(func_6063_call(), 0)
call_7861 = relay.TupleGetItem(func_6065_call(), 0)
func_4112_call = mod.get_global_var('func_4112')
func_4113_call = mutated_mod.get_global_var('func_4113')
call_7870 = func_4112_call()
call_7871 = func_4112_call()
output = relay.Tuple([call_7860,call_7870,])
output2 = relay.Tuple([call_7861,call_7871,])
func_7872 = relay.Function([], output)
mod['func_7872'] = func_7872
mod = relay.transform.InferType()(mod)
mutated_mod['func_7872'] = func_7872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7872_call = mutated_mod.get_global_var('func_7872')
call_7873 = func_7872_call()
output = call_7873
func_7874 = relay.Function([], output)
mutated_mod['func_7874'] = func_7874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_7883 = relay.TupleGetItem(func_3682_call(), 5)
call_7884 = relay.TupleGetItem(func_3684_call(), 5)
output = relay.Tuple([call_7883,])
output2 = relay.Tuple([call_7884,])
func_7899 = relay.Function([], output)
mod['func_7899'] = func_7899
mod = relay.transform.InferType()(mod)
output = func_7899()
func_7900 = relay.Function([], output)
mutated_mod['func_7900'] = func_7900
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7911 = relay.const([[[-9.726609,9.008119,3.808495,-6.447258,-6.507722,-4.043952,3.818026,5.804923,9.804543],[7.219216,5.907389,-1.257518,-9.054234,-3.434345,-0.511544,2.053185,-2.367154,1.082316],[-7.417916,0.683762,5.581111,3.290439,-3.551064,-9.632706,7.288429,2.371646,5.942542],[0.731812,-3.637242,-1.006518,8.624534,3.486511,-7.699226,2.138443,6.929555,3.881043],[2.079264,4.630394,2.265387,0.111383,8.475964,-8.667315,-3.119349,-1.922748,0.786935],[6.355098,-3.369150,-4.244529,-7.947624,-5.244017,9.241392,-6.356117,-7.954402,-9.427581],[1.590217,-3.653361,-4.161968,-9.583472,-0.614723,4.182328,7.991032,2.858422,-3.818886],[-0.423841,1.725869,-1.099571,8.900963,3.068787,-5.772854,4.059895,1.184567,-5.818276],[-0.009241,-5.302278,2.278583,-6.057218,7.697498,9.127990,-9.348645,-6.661857,-1.858375],[-9.343543,2.380645,3.147180,6.117580,-5.492967,7.524709,-6.892606,3.110626,-0.213921],[0.528967,5.858972,-6.638598,-3.054940,-7.339645,8.483675,6.622927,-3.443829,9.806737],[-9.541647,0.302640,-2.137809,2.879700,-8.200860,1.257210,3.135871,-5.644919,1.888423],[1.134353,7.655671,-1.984163,-9.707498,-4.894830,2.951322,9.078924,-0.517667,-2.035718],[6.548494,9.418845,-9.379360,-4.018715,7.573703,-1.680790,-7.141395,-9.598425,1.584550],[-7.393138,-5.973740,1.099857,-8.400307,4.830180,4.612773,7.014500,1.491578,-3.668855]],[[-9.821400,-0.601492,6.110323,-2.716386,-9.146032,5.432892,-3.647016,-3.290724,-8.223966],[-3.118463,-1.348561,1.726237,7.352395,-5.558382,-3.141333,-3.404336,2.676473,-9.244016],[4.394517,-1.194673,-4.084732,0.586822,4.534863,0.585008,2.885815,4.738532,-9.617603],[6.051691,9.552549,-3.081117,8.154453,-0.930679,9.201577,7.690600,-9.990160,4.350109],[-2.461297,3.752166,-8.193077,9.025861,-0.198100,0.417275,-2.687597,-3.587457,-7.114789],[6.437069,4.903314,-6.119111,-4.952799,5.122320,-2.365972,9.318124,1.775818,-1.005853],[-7.648708,-2.681773,-8.940820,5.009378,-3.561687,7.407627,-3.508353,-6.750379,-4.749840],[2.756909,6.271239,5.243873,5.261441,-5.752994,3.500613,-4.273335,-2.964505,-9.253621],[-7.415824,6.753311,4.172627,9.057351,6.702666,8.947847,-3.566407,9.659127,9.063944],[4.531445,4.915139,-3.431163,5.843438,-7.006782,5.580677,-4.111890,-0.072443,-8.557573],[-4.924572,-6.565329,-6.918134,-5.033198,-8.338284,-6.832793,-5.510149,-8.596313,6.833079],[9.753218,6.926013,-6.926625,-3.801621,-8.032383,0.643006,9.579443,-3.945303,7.800166],[6.587710,5.339967,1.225260,-2.339425,-8.575927,-0.507879,8.098146,-8.954623,1.277916],[7.263493,7.013093,3.678849,-3.574853,9.593811,-5.069077,7.912122,-0.398117,8.930533],[-8.417925,3.354780,-3.786568,-1.962018,7.620013,-2.944122,-9.525781,1.387445,8.688806]],[[-2.343132,2.696390,-8.182371,-1.846963,9.221522,-1.374063,7.580159,-7.805975,5.705238],[-3.649053,-7.754278,-8.437234,-4.710193,-2.741171,0.810786,-6.968133,-1.657415,7.330161],[8.767292,-7.732177,-2.751247,7.903876,-5.395748,-6.633660,-4.628447,2.758297,8.007422],[2.236151,-9.773805,1.437732,5.957037,9.594924,1.825896,-2.170892,0.475819,6.079446],[-9.386968,5.086353,7.638200,-2.390657,-4.595901,-8.129928,-1.753718,3.231548,-7.509045],[-2.055906,3.983663,1.353916,-6.977543,3.145200,-1.943361,2.469015,-8.206985,2.805262],[-7.444012,0.804360,-9.949582,-4.164744,-2.209584,9.244676,-6.171337,-5.288492,-6.646671],[-2.847961,-1.235362,-4.769787,8.071466,4.699904,-0.742161,1.228242,-8.334589,2.184439],[-9.051318,0.106611,2.094985,5.468380,-7.186261,0.083493,0.154899,6.002355,-5.788834],[3.864174,4.421444,2.748174,0.296440,6.396371,7.259598,-4.066890,-2.543297,-3.910870],[9.291974,-7.333869,-7.270256,-3.730624,5.064297,6.921414,8.434265,3.156260,7.613065],[-2.713359,2.149909,-8.933440,-4.312243,5.934905,0.267602,-6.651341,5.714782,-8.745796],[8.855534,-5.865778,2.191804,-0.043919,-5.691554,6.300156,-2.063688,-7.471143,5.413275],[-6.914740,-7.620553,0.811323,-6.370214,-7.846032,-6.894863,2.042978,6.423161,-9.207277],[2.948122,1.118027,3.120916,2.193741,-3.596635,2.584180,-2.235360,7.137298,9.544938]],[[-9.027622,-2.959920,-1.980892,-2.913866,-5.060488,4.213359,-8.416946,1.884136,-0.331380],[-3.767259,-8.120465,2.643640,3.942329,-5.301011,-6.566298,0.846106,1.763539,1.698710],[-6.534912,7.448046,2.015761,9.287468,5.483411,8.173334,0.889042,6.079053,-6.769736],[-0.587314,-0.054839,-7.809125,-9.766209,-9.150136,-9.510254,9.285857,1.655000,9.636670],[3.704103,-2.799005,-2.330881,-0.297492,0.980177,4.658598,4.248864,9.246349,-7.122702],[-7.054974,4.979338,-1.097194,1.855865,-5.539327,-4.665985,4.831433,9.507756,-7.585830],[-5.888637,8.693525,-9.805560,6.762623,-7.545938,-5.329169,9.071629,-4.331581,4.404762],[-3.622106,-7.454571,1.537292,-6.927223,3.087668,-4.538214,1.487746,-8.857894,-3.875781],[-2.146533,-7.128985,4.352951,0.014164,-2.143419,6.504349,3.208597,-5.175209,9.440906],[-4.896919,-7.638235,1.917046,-5.692097,5.472199,6.373949,2.229191,-1.227760,8.219437],[-0.565677,-9.381554,-2.028993,-2.532983,5.088284,9.021541,-9.984906,-4.931766,6.968125],[3.771792,7.800795,9.482867,9.875035,-4.968691,-7.504017,3.656047,-6.607368,7.018318],[2.162631,-7.324308,-5.493836,4.818846,-7.726465,-8.981683,9.342872,5.370925,-2.797704],[-5.346602,2.952690,1.380585,-9.205722,8.147913,-7.522508,3.300068,-6.818432,-6.753370],[0.382372,-4.461480,-9.486859,-1.893079,-2.613063,-6.938484,-9.738006,-3.828400,1.650735]],[[9.366381,-9.461617,-8.398472,-2.438449,5.222313,-7.870684,2.138462,5.468723,2.188594],[-6.306541,-0.575652,6.817029,-4.215889,4.995112,3.357994,-5.488059,-7.302082,0.463278],[-4.117131,-4.106081,4.483576,2.622330,-5.345971,-5.359782,-5.051645,8.873288,9.397865],[2.455922,-6.356222,9.314884,5.540947,6.616003,-5.525734,0.932739,-7.870938,-7.173559],[-3.412321,-3.827106,5.839095,-2.392287,-3.137639,-8.379993,-1.713255,1.265430,-6.658748],[-8.286514,-1.283377,5.377785,0.578754,1.100565,-7.555114,6.486690,-3.921812,7.761797],[-3.093118,9.458214,-9.858473,-4.654957,-1.576354,7.046057,-6.711665,-2.025531,8.831697],[-1.891907,-1.687750,-1.329463,3.566959,4.495806,-4.627307,8.217672,-6.164811,3.696176],[-9.066878,8.830791,0.740286,1.208255,7.358520,-2.492841,0.784047,2.076886,8.558971],[-5.520541,7.794930,-8.138548,0.466381,-1.470077,-4.212295,-7.059225,1.789123,9.669758],[-5.175113,0.253087,4.381366,8.292404,-9.931757,-7.244236,-8.678894,-2.012193,6.447324],[4.852543,5.936864,-5.917623,3.343557,-7.738873,4.570189,1.230547,2.769722,9.058238],[7.492915,3.853195,9.778477,2.319832,0.104408,8.040896,-9.989685,2.279161,-9.557588],[9.313010,-0.867083,-8.590633,-4.059657,0.268327,-0.152803,-0.465220,3.873615,4.206614],[3.923720,8.141431,3.669428,8.714676,2.551526,8.680267,5.938366,-3.739237,-8.624034]],[[1.236019,-8.687182,-4.623480,5.714314,-8.503821,1.856729,8.829320,-0.887883,6.608489],[6.370955,1.032287,0.196580,-6.006442,-6.380456,-8.655248,1.304234,0.276800,-3.209256],[0.066666,-5.506437,7.571910,5.838180,-0.578092,1.497233,6.278854,2.300106,5.866889],[7.051166,1.663566,-5.008782,4.874792,9.203953,-6.793318,-6.890331,9.076604,6.026223],[-2.314140,4.202992,7.140521,-5.834911,3.681067,9.852020,-5.778298,-8.721111,-1.411287],[3.242723,-9.170350,-5.396106,2.196497,-2.355052,2.347141,8.260586,4.345563,9.302750],[1.941337,9.109704,3.026853,2.643436,-1.118964,5.921825,3.296491,-8.429274,9.990922],[-3.153757,0.920388,8.697518,-4.750048,3.621116,1.390011,-3.932649,-6.365759,2.179846],[3.732913,-5.455691,-2.513577,-5.055223,-1.964715,3.948103,-3.672383,-0.102975,6.418540],[-8.919400,-4.075004,3.112404,-1.885889,-4.027897,4.173148,-5.436416,4.993907,-7.484683],[-5.685940,2.450880,0.939042,-5.931093,-5.870229,-8.067592,-8.140065,7.348161,-1.492687],[-5.912854,4.029163,8.359215,-3.882640,7.734766,-3.282687,5.804437,-1.638302,-2.426816],[-0.274432,7.939191,1.296746,-6.295555,4.037566,9.644586,-0.401035,-2.406400,-1.776020],[-9.131491,-8.101074,-0.927681,-0.955979,9.506220,-5.756930,-7.297484,5.848278,5.260332],[9.413838,-9.166135,-6.166344,-7.177473,-4.747461,-7.826154,5.514649,8.069408,-4.131967]],[[-0.244245,-8.377431,9.201806,6.337162,0.176192,-6.583350,-1.934550,-5.587202,-4.376499],[-2.231277,7.859146,0.708299,3.467574,-9.407087,-7.980445,1.079974,2.527132,2.259141],[-3.705136,7.157129,4.512787,7.760950,2.011095,-1.002420,-4.724687,6.348679,0.973210],[2.857746,4.315311,-6.464430,-9.362966,-4.889054,3.133314,-0.725174,4.998048,6.808162],[2.498626,-5.497909,-9.057713,-6.003695,8.647550,-3.057462,7.450147,9.460817,7.315210],[-5.904909,8.815106,-0.946465,-3.461562,0.697367,-6.699355,-4.698178,0.695983,-9.297465],[-5.530109,-8.427718,-5.574982,-4.508917,-7.814308,-7.206222,8.017179,7.220078,-2.331121],[6.046476,-6.053290,-9.978956,6.012875,4.543619,7.197227,-8.448102,-5.369110,3.630821],[7.580044,-0.722558,0.796492,-5.659089,-6.893512,-9.449540,0.655258,0.200552,-5.974692],[-4.552244,7.033142,-9.924043,9.507756,-3.944770,1.195881,6.881021,8.040239,-9.199892],[-0.675151,-7.925742,-0.356252,2.261263,-8.026032,5.347348,-0.832978,9.546284,8.893324],[-5.759430,-0.045945,6.194504,-1.249624,6.890514,-2.838583,1.571931,-4.228910,1.667262],[-1.526792,-1.964538,-0.552819,4.786203,7.241876,-6.061717,-9.372105,8.572999,9.712251],[-5.598874,9.925659,5.254528,7.071398,4.750403,-7.058064,-3.140611,8.731395,-6.579175],[-1.343958,7.989291,-2.002092,6.994905,-6.607988,9.625573,0.778047,-5.171513,7.286136]],[[-8.200054,-2.358317,-5.482017,6.859813,4.987552,9.646679,-4.872351,9.601360,7.176558],[5.443971,-0.175005,-1.615455,6.128806,1.044353,-1.625687,4.155492,4.410084,-1.823549],[7.191690,-2.721620,6.834216,-1.078840,8.450868,2.621921,9.900393,5.844898,-8.236699],[1.510171,5.104680,0.841705,-5.403837,7.320309,-2.838456,3.262519,0.789733,-3.515588],[-5.006505,-2.951509,-6.168041,-2.102640,-4.277127,9.902257,6.330590,-3.700310,8.368147],[6.295082,-3.353130,0.077721,-1.694402,-1.269346,-3.607158,-2.702606,0.041087,1.148029],[-4.607135,6.401637,2.779835,-3.335561,-4.111088,-9.021688,-1.863671,1.703166,-9.013344],[-7.005280,6.987074,-9.861323,1.035623,-0.954229,4.754682,1.165454,-2.510771,-9.432868],[5.704090,-4.058756,5.153132,-4.846489,-1.267073,-7.257789,-6.175059,-2.596691,-7.497852],[-1.643203,9.610908,-9.114221,-3.171778,0.394200,9.103017,-8.879783,-5.127064,-7.976156],[6.133652,6.265458,-5.030327,-4.741966,-5.970458,-1.333001,9.932538,7.636583,-1.995454],[2.897391,6.159361,6.251500,-2.164600,8.849681,-7.258295,-0.439836,-0.663279,-1.523466],[-8.797877,-9.981116,9.242392,9.100422,2.388598,9.234319,-7.460221,-4.530896,1.024890],[-4.198694,0.910841,-1.471851,0.481494,-3.309794,7.865301,-2.718300,7.915798,-6.452447],[-7.690058,-4.966031,-9.250440,8.017222,-4.182825,-6.864851,1.507626,-2.379984,9.637971]],[[-2.329794,2.827226,-4.319487,5.126703,-0.260450,9.799087,1.486669,-9.089581,3.511234],[-4.101203,-3.281157,-8.824297,-4.055401,1.074463,4.497984,-9.661250,-3.107350,-8.471523],[-1.752528,8.529579,-3.223211,5.315734,-1.814473,7.574744,0.595035,-0.799635,6.145029],[-0.919999,-5.918163,-6.287781,-6.926813,-1.946841,-4.404379,-9.839502,-3.977013,-4.163001],[-4.581547,2.833140,3.253513,2.837402,-1.220904,-8.163725,-6.775022,5.207663,9.670015],[-6.446169,-3.591269,-2.536177,7.968471,5.212030,-9.698073,7.035494,-1.345043,-5.199560],[3.048332,-1.061625,6.399579,6.597238,5.571341,7.513448,-5.490392,8.073714,-2.826418],[-9.932401,-1.985198,6.338526,5.457436,2.389375,8.998666,7.482908,6.596032,-0.053526],[8.597571,3.272529,5.582221,1.229725,-0.226840,-9.355928,-5.384899,6.113909,9.797543],[3.360517,1.478319,-5.878989,-9.242338,0.644855,6.452721,8.666409,-2.872516,6.419215],[4.274481,7.071321,9.288608,-0.726680,-2.124070,-5.154123,-7.305129,-0.236872,8.876032],[7.615209,1.444104,5.437497,-4.665668,9.507652,7.251136,-2.123893,9.203992,7.165070],[-1.191927,-5.802318,9.892835,-1.815140,-2.644331,1.499001,1.195332,-3.991034,8.011698],[0.699164,-6.754995,-9.240410,9.163515,-2.956231,8.635992,-7.432594,2.514321,-9.048242],[7.457297,-4.347098,-0.652446,9.970566,-3.044093,-1.102834,-8.974866,-5.841082,-9.930959]],[[-2.629605,1.243810,-6.268409,-4.719062,-5.689539,0.905164,-1.705118,0.551893,-4.521816],[-7.816059,5.764888,5.560940,9.042649,6.256494,-6.374601,-6.315848,-3.339334,0.020914],[-2.668164,3.226914,3.692354,-2.877906,6.334981,7.314729,1.447171,-2.987138,-4.701603],[-6.292430,7.560662,7.962105,9.605562,-5.131631,-8.394388,-3.096282,-2.155802,8.446092],[-1.092513,7.016727,-8.932610,5.138046,7.485219,-2.214214,-2.257795,1.567747,9.489763],[7.351796,-6.886073,-0.313415,-5.233713,-3.462048,-9.600629,-7.672097,3.710260,-7.676660],[-6.737034,9.145977,2.610214,-8.433993,-9.571018,0.426971,-7.947342,-3.384077,0.629029],[3.193422,3.893458,-6.427743,-9.174202,-6.040806,-5.094270,3.853440,-9.486770,-4.171009],[-6.104022,8.843985,-5.989378,-0.025451,-1.075475,-0.840590,5.386859,1.405645,1.866621],[-4.506123,-2.672774,5.471454,-7.389183,-6.781757,9.048593,-8.787651,5.653147,-5.353843],[9.697289,-3.444787,6.398518,8.248748,0.144297,5.089801,-6.985369,-6.829995,-8.850572],[2.230264,-1.740993,6.211938,5.896929,9.555861,-3.758685,-1.230252,0.378262,9.489455],[5.674685,2.651115,2.693228,5.014170,0.448654,-5.015583,1.749531,-7.836353,3.351968],[4.302753,2.839614,6.527563,-0.671168,6.194693,9.364227,-5.854372,8.637550,5.781750],[-7.894662,-2.848756,-3.581054,4.055425,4.552123,4.468327,-7.958197,1.326612,2.271812]],[[5.047682,-6.747702,9.676136,0.670369,6.786042,-9.380422,8.854823,0.591537,-5.638897],[-6.833088,-1.952918,2.495977,3.234456,-5.223779,7.365500,0.906618,-3.851883,-5.788271],[4.766127,2.998513,-2.345292,4.282878,9.388938,-0.710823,-2.136911,6.663673,-3.197206],[-6.904439,-7.127962,-7.216355,7.164424,-6.962658,6.512202,5.332600,-8.848884,7.667332],[-1.877827,-0.479351,-0.216623,0.311436,-0.869343,8.476356,2.783991,-9.841274,-0.466504],[-5.394412,-5.105353,6.657419,8.748792,4.757144,-9.629538,-7.065471,1.874564,-0.117300],[8.446139,7.746215,-7.998346,-0.095970,-6.069431,-1.769280,8.181851,-8.851600,6.105039],[-5.781272,5.995836,9.496072,-9.158581,-7.476201,-5.574596,0.001256,5.695057,3.702434],[8.828647,6.460855,-3.816737,4.027059,-2.808862,-3.647582,2.317586,-6.359180,-4.774248],[-2.922087,-6.540960,-7.676953,5.081090,-5.729383,-5.459848,3.035518,-9.287785,-6.843364],[-0.766567,-7.534623,9.237748,-1.461367,5.750909,2.187538,-7.945261,6.114023,1.220295],[-2.728672,4.940807,1.539911,-0.127454,-2.937374,5.404104,-1.396556,-1.275850,2.974219],[7.189738,-0.125058,-3.538421,-9.368464,-0.116900,2.017737,1.538564,-5.950378,7.965068],[5.278017,-8.766144,-3.933526,-6.494855,4.095404,6.172925,-5.370018,6.000236,-8.787483],[0.805741,-9.297939,-8.486559,3.331948,5.903882,-1.711130,2.564937,9.660444,0.319770]]], dtype = "float32")#candidate|7911|(11, 15, 9)|const|float32
uop_7912 = relay.asin(const_7911.astype('float32')) # shape=(11, 15, 9)
func_5480_call = mod.get_global_var('func_5480')
func_5482_call = mutated_mod.get_global_var('func_5482')
call_7918 = func_5480_call()
call_7919 = func_5480_call()
output = relay.Tuple([uop_7912,call_7918,])
output2 = relay.Tuple([uop_7912,call_7919,])
func_7920 = relay.Function([], output)
mod['func_7920'] = func_7920
mod = relay.transform.InferType()(mod)
output = func_7920()
func_7921 = relay.Function([], output)
mutated_mod['func_7921'] = func_7921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5608_call = mod.get_global_var('func_5608')
func_5609_call = mutated_mod.get_global_var('func_5609')
call_8051 = relay.TupleGetItem(func_5608_call(), 0)
call_8052 = relay.TupleGetItem(func_5609_call(), 0)
output = call_8051
output2 = call_8052
func_8058 = relay.Function([], output)
mod['func_8058'] = func_8058
mod = relay.transform.InferType()(mod)
mutated_mod['func_8058'] = func_8058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8058_call = mutated_mod.get_global_var('func_8058')
call_8059 = func_8058_call()
output = call_8059
func_8060 = relay.Function([], output)
mutated_mod['func_8060'] = func_8060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_8131 = relay.TupleGetItem(func_1318_call(), 1)
call_8132 = relay.TupleGetItem(func_1319_call(), 1)
func_7423_call = mod.get_global_var('func_7423')
func_7424_call = mutated_mod.get_global_var('func_7424')
call_8143 = relay.TupleGetItem(func_7423_call(), 0)
call_8144 = relay.TupleGetItem(func_7424_call(), 0)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_8145 = relay.TupleGetItem(func_1502_call(), 0)
call_8146 = relay.TupleGetItem(func_1504_call(), 0)
func_5628_call = mod.get_global_var('func_5628')
func_5630_call = mutated_mod.get_global_var('func_5630')
call_8159 = relay.TupleGetItem(func_5628_call(), 0)
call_8160 = relay.TupleGetItem(func_5630_call(), 0)
func_4815_call = mod.get_global_var('func_4815')
func_4818_call = mutated_mod.get_global_var('func_4818')
const_8163 = relay.const([-1.379483,7.652263,-4.411706,-9.838925,8.210403,8.928710,-2.886501,-9.326703,3.693555,4.014937,3.826832,0.730015,-9.180708,6.496322,3.976450,6.382066,5.899432,6.147061,-1.818883,7.818322,-8.885956,-9.514570,9.235530,-3.112000,5.020915,-2.722486,9.249970,-7.066215,-5.883698,2.898322,-4.948704,5.087859,-5.706440,6.318205,9.860807,-8.721828,1.995400,-6.466094,4.320403,9.337475,-6.433514,7.809004,6.773367,-9.027967,-5.599611,9.031623,-4.127134,-7.825222,-5.461379,4.519052,-5.048392,8.963074,-8.486015,-7.040137,4.024215,-1.292569,1.682093,4.111883,8.288835,5.989123,0.342457,-6.754059,9.008912,-0.760042,-2.598614,6.024554,-6.852407,-3.275941,5.408737,-3.768092,-3.166612,-2.570947,1.756203,4.950422,4.388192,-6.671054,4.494073,-5.580969,2.860671,-0.986479,-1.336247,-6.116097,9.652132,4.627440,-2.626276,0.642944,3.192063,-6.071708,6.070786,0.192412,-7.798423,5.603153,1.284630,9.988098,8.350153,-6.184569,3.774630,-4.471382,-8.367713,0.898025,0.645398,3.209529,5.699359,9.706485,5.547725,5.148077,-9.216134,-5.542159,7.067527,-7.690584,1.489284,-6.642557,-3.095121,4.972293,7.304618,9.525265,2.593583,0.759102,-0.051022,2.355967,4.880450,-0.106337,-3.272544,5.588369,-5.774905,-5.029952,8.690434,-7.943630,0.613903,-5.486123,4.792872,2.256402,-0.444750,0.986742,-5.962182,8.743512,4.187925,6.963453,-9.626470,0.839502,7.976531,-5.017601,9.419078,-5.130787,9.430876,2.535881,-2.207133,2.864067,5.304646,6.438139,-9.677369,0.419508,-5.651618,1.067247,-3.987942,0.395699,-0.397107,-6.192709,1.037130,-1.581171,8.964956,3.686806,-8.338631,-3.863079,6.971335,5.155827,-7.447346,2.182333,-8.380006,8.814069,-3.743727,-7.282130,3.102183,-0.156094,7.817605,2.055022,-6.816707,-6.488693,2.027133,-9.721300,-3.577026,-5.262454,-3.281726,-8.004531,-7.458258,0.103819,-0.428686,5.184486,-7.781929,-2.740543,-3.026117,-3.688382,-6.950903,-0.624968,-1.984987,-3.831716,-9.842723,7.900313,5.612346,2.165373,-4.627315,-0.282894,-7.334427,-3.827977,7.255807,-4.627864,-0.124837,-4.192819,9.012951,-3.223687,6.204808,3.313440,-5.500745,-0.818908,-2.115186,1.558626,6.915963,8.624912,-1.041001,-1.553900,3.238526,2.273392,-7.346162,-7.803431,-7.042840,8.711884,-8.778110,-9.726448,2.612254,-9.749809,-4.282165,-6.440308,0.676088,-0.115311,7.528109,3.273168,8.149808,-6.165733,-0.988932,-5.046731,-7.768693,-6.092775,-3.634248,3.510065,5.727374,1.658694,6.899789,3.211466,5.914850,-1.849207,9.552258,1.290711,8.901056,-8.107961,2.043239,-2.189543,-2.868792,-3.023100,7.431305,-2.311331,2.858941,1.221060,-2.931695,5.929008,-3.415524,-8.929843,1.938462,-6.186628,-8.695085,-1.687800,3.047793,7.930852,1.038522,-8.776497,5.270730,1.591746,-7.325048,7.727787,-1.429316,0.034972,1.509915,-3.647446,7.291107,3.291677,6.130401,7.909321,-0.717105,-0.463422,-1.448557,9.001483,3.612103,-4.990168,9.651808,-6.350450,-0.910879,-9.282341,-3.498849,-3.197896,0.649161,8.559502,0.152490,-7.354063,3.190606,3.753306,7.698721,5.168130,-9.415133,6.509018,9.461758,0.225303,8.948342,4.136603,-6.086491,9.032398,4.775804,-4.577931,-8.375664,7.473651,6.860898,2.935197,2.600593,3.573357,9.416961,3.031657,2.442085,-5.252227,-3.929971,-4.176681,-6.398028,-8.475871,-7.356700,-7.230031,8.574704,-1.830488,2.039636,-6.340493,-4.524131,-7.691012,-1.627042,-9.831192,-8.037374,-4.194627,5.172689,1.993053,-1.566218,1.470077,-7.117085,0.048309,7.867517,-6.701479,-9.986782,6.768169,-9.991318,-3.601694,5.077800,-6.686200,9.182298,-1.521014,0.807194,-6.552521,-8.515610,-4.079737,-3.960084,-4.737670,2.114386,-0.980273,3.700899,-5.184568,7.480380,-8.398003,-7.777038,-6.271702,9.462977,-7.619767,-7.589059,3.462350,-8.718123,0.146330,3.624599,1.838290,-1.775758,-9.178896,1.208657,6.032556,5.492152,-2.686562,2.070467,-4.860147,6.140408,9.399448,3.840742,-6.154058,8.766661,-1.220464,-9.680783,4.502075,6.240094,-7.350340,3.967157,4.079431,-2.286626,-6.215604,-0.646669,-9.413715,6.511205,4.712185,-0.196421,-9.947748,9.551654,6.327574,-9.190220,-1.869897,-7.280702,6.319007,8.206976,0.606249,-5.518536,8.049541,-8.539364,-0.573555,5.180149,-0.834056,-3.042464,6.651782,-1.669205,7.830579,-1.896101,-9.469914,-9.595003,-2.747406,4.546267,0.197266,4.787035,-4.448714,1.052488,1.172591,0.379488,-4.523190,-7.757307,8.429601,-7.497890,-3.554245,9.170303,-8.563285,-6.920518,4.851980,-0.070504,1.601407,8.737435,5.001147,-9.537838,4.396358,-2.174582,8.947710,-6.646588,0.253443,6.280078,2.710907,1.512854,8.476489,-3.036312,0.848844,2.899170,-6.684114,-8.009120,3.572895,-7.549979,-6.963453,1.237316,5.713198,9.906458,-1.686373,-5.018769,5.154133,8.903211,6.606257,5.814651,-9.964965,7.747249,1.404738], dtype = "float64")#candidate|8163|(480,)|const|float64
call_8162 = func_4815_call(relay.reshape(const_8163.astype('float64'), [10, 16, 3]))
call_8164 = func_4815_call(relay.reshape(const_8163.astype('float64'), [10, 16, 3]))
func_2272_call = mod.get_global_var('func_2272')
func_2274_call = mutated_mod.get_global_var('func_2274')
call_8169 = func_2272_call()
call_8170 = func_2272_call()
output = relay.Tuple([call_8131,call_8143,call_8145,call_8159,call_8162,const_8163,call_8169,])
output2 = relay.Tuple([call_8132,call_8144,call_8146,call_8160,call_8164,const_8163,call_8170,])
func_8179 = relay.Function([], output)
mod['func_8179'] = func_8179
mod = relay.transform.InferType()(mod)
mutated_mod['func_8179'] = func_8179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8179_call = mutated_mod.get_global_var('func_8179')
call_8180 = func_8179_call()
output = call_8180
func_8181 = relay.Function([], output)
mutated_mod['func_8181'] = func_8181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4588_call = mod.get_global_var('func_4588')
func_4590_call = mutated_mod.get_global_var('func_4590')
call_8213 = relay.TupleGetItem(func_4588_call(), 3)
call_8214 = relay.TupleGetItem(func_4590_call(), 3)
func_6203_call = mod.get_global_var('func_6203')
func_6206_call = mutated_mod.get_global_var('func_6206')
const_8230 = relay.const([False,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True], dtype = "bool")#candidate|8230|(16,)|const|bool
call_8229 = relay.TupleGetItem(func_6203_call(relay.reshape(const_8230.astype('bool'), [16,])), 6)
call_8231 = relay.TupleGetItem(func_6206_call(relay.reshape(const_8230.astype('bool'), [16,])), 6)
output = relay.Tuple([call_8213,call_8229,const_8230,])
output2 = relay.Tuple([call_8214,call_8231,const_8230,])
func_8238 = relay.Function([], output)
mod['func_8238'] = func_8238
mod = relay.transform.InferType()(mod)
output = func_8238()
func_8239 = relay.Function([], output)
mutated_mod['func_8239'] = func_8239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6063_call = mod.get_global_var('func_6063')
func_6065_call = mutated_mod.get_global_var('func_6065')
call_8280 = relay.TupleGetItem(func_6063_call(), 0)
call_8281 = relay.TupleGetItem(func_6065_call(), 0)
output = call_8280
output2 = call_8281
func_8286 = relay.Function([], output)
mod['func_8286'] = func_8286
mod = relay.transform.InferType()(mod)
mutated_mod['func_8286'] = func_8286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8286_call = mutated_mod.get_global_var('func_8286')
call_8287 = func_8286_call()
output = call_8287
func_8288 = relay.Function([], output)
mutated_mod['func_8288'] = func_8288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5177_call = mod.get_global_var('func_5177')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_8298 = relay.TupleGetItem(func_5177_call(), 2)
call_8299 = relay.TupleGetItem(func_5178_call(), 2)
func_1657_call = mod.get_global_var('func_1657')
func_1660_call = mutated_mod.get_global_var('func_1660')
const_8348 = relay.const([8.875606,-6.349403,-3.888985,8.913384,-9.517080,2.811938,-0.173279,6.991837,-0.103611,0.284711,2.071920,-6.869834,9.384719,7.366731,0.375884,-9.980081,-0.268689,0.666158,3.113874,-9.809063,6.659114,-9.123002,0.190915,-9.796617,-7.776679,8.170807,-4.688016,-3.603195,4.498592,-2.016436,-5.364887,7.570941,0.272653,8.844133,9.928915,-5.834525,8.598145,-5.367094,7.861682,-0.313168,3.553300,7.416675,-6.529418,6.751904,-9.328654,-2.045267,1.603843,5.742406,-3.748868,0.757183,-1.200098,-1.759167,0.324923,5.825180,0.569371,-5.368391,2.599610,-9.063197,6.521875,8.334841,9.700248,6.447041,-8.135723,2.319080,7.032089,-1.523116,5.668104,-4.518036,-7.454756,0.605229,6.903011,-3.956818,2.120244,-8.576965,-5.103526,-6.910681,-4.596562,-4.142429,-2.094176,4.183559,6.338253,-5.323117,6.222721,1.207129,-9.886381,3.316148,-3.851412,-4.973295,5.797352,5.664159,6.763886,5.782220,8.951845,-1.869231,-4.806644,3.299261,3.034903,-3.185682,-2.698327,-6.421159,-3.474702,8.459442,5.453924,-7.002190,-0.684641,4.280177,-9.173891,1.144965,-1.782532,8.929622,-0.752242,-9.576855,-1.067497,-3.762913,-6.897778,3.319153,-4.038022,-5.544464,2.065995,-0.041197,-9.731845,2.900442,6.767656,-7.936451,-7.217994,-4.034285,-1.221413,-7.131599,7.966911,-9.049426,-4.787973,-5.691807,-3.516558,-7.824006,9.844927,3.527286,-4.610770,-9.159692,-2.613357,-1.854055,9.187507,1.557957,9.434823,-2.838110,-1.091316,1.932593,1.956646,2.145834,-7.842911,8.577861,6.635561,2.808844,1.943143,7.456606,-3.863976,-2.668328,-3.274529,6.299065,2.648830,-1.962237,-0.716106,-7.210234,1.614883,2.867790,-7.778241,6.457114,-9.987064,1.077089,0.121809,1.264039,-9.365012,3.599834,6.064665,7.108608,-6.135143,-9.414547,0.698691,-6.124556,-4.263033,-2.985354,-2.520321,-7.364463,-5.977373,-0.155510,-7.582589,6.887725,7.397761,7.583728,0.459906,-6.388628,-4.562394,5.856257,1.600521,-2.111888,5.407045,-6.813525,1.251509,-7.951450,1.997823,2.175085,-6.656908,-4.582480,0.951329,-9.062227,-5.622080,-1.023514,1.596642,-3.543735,-9.648231,5.787495,0.300151,1.442025,-8.129759,-2.136516,1.510806,-9.172439,-6.529591,4.113867,-5.150085,0.406718,-6.500313,-0.718262,0.801494,4.842490,2.082596,1.237703,-5.427028,5.264975,1.148586,-0.363035,2.104318,-3.645316,-3.615812,7.023295,-1.564712,4.624524,0.310041,-5.681740,3.707645,-0.898147,-2.607970,0.860120,-5.536944,-6.280861,3.695280,-9.965878,7.237654,-1.696235,4.544049,-6.626523,-1.755672,-8.695918,2.471995,-4.603070,-0.367968,-7.067648,7.510559,-2.545396,-6.496752,3.577868,9.847764,6.011617,-4.681773,-1.453379,9.730548,1.540752,3.795351,4.383052,7.456305,4.200757,-4.210305,-6.846040,4.168942,-7.557263,6.293492,9.541303,2.234588,5.187574,3.445279,9.674628,0.350772,-0.619155,5.409368,6.051472,-0.186408,-7.816822,-1.008143,-3.741418,6.740852,-7.588493,-9.294138,-3.111535,-7.079204,9.783341,4.910474,-3.801048,-4.511119,8.560442,6.803805,-1.739759,1.410252,-8.902554,9.771015,-5.988464,4.549466,-5.842094,-2.417177,-3.445558,-0.495137,-5.105740,-6.894561,-1.225361,-1.247180,-0.076864,5.717914,5.243654,-8.600311,-8.688509,-5.308310,-8.635314,7.802763,2.204464,2.936764,-2.432499,8.861837,-2.618040,-8.387270,-5.207694,-5.850918,-3.240753,6.766007,4.730320,3.406297,-0.326840,-4.522134,-2.262640,0.702871,1.064285,2.797644,-2.835086,3.175209,-9.116470,-2.597428,-3.933111,-2.363483,-6.014238,-9.232258,1.161955,4.748269,5.404442,-0.744954,-0.295891,0.653943,1.510023,7.142304,8.658033,-1.102344,-7.562420,8.893412,1.101431,6.595378,4.994692,2.085284,-5.605976,-1.871905,-6.491576,4.483510,-2.725523,2.996359,8.577379,-5.105160,0.037039,-8.126899,5.947984,-4.909267,0.055258,-5.486837,4.821696,5.893948,-7.368806,0.917510,7.017471,0.302985,5.513788,3.412273,-3.264861,9.816187,-8.894176,1.909193,5.519231,-9.583987,-5.577543,-2.191770,5.147457,9.175802,8.437955,-6.612215,0.113383,4.463515,-2.749497,8.857058,-8.397983,-6.145319,-6.893206,-7.085767,6.529757,0.659667,5.672980,0.289559,5.477433,-6.821967,2.910941,3.304123,7.620231,6.983015,6.239792,-5.089722,-0.495543,-5.991439,-9.106473,-5.315876,-5.448114,8.163063,0.255060,-3.891726,9.860000,-3.730223,4.828194,7.199264,-2.169795,5.475857,3.172465,1.261581,-2.938332,0.269384,-1.673629,4.449034,2.591933,-0.344325,7.305857,9.022680,6.131621,-4.281092,-2.321961,2.674581,-5.037469,-3.305947,-2.732478,0.761969,-7.515868,-5.530658,2.828083,1.834602,-8.378087,8.888638,-4.311572,5.834558,-3.126599,-3.006724,9.355376,0.892615,-9.566441,-3.899114,1.712108,-6.814936,-5.513097,-7.561079,-8.346119,-9.348418,1.941741,-7.085040,-2.338194,-4.287729,4.974121,6.024895,-9.482736,2.041442,9.946825,-2.229179,2.925542,-9.725655,3.181821,1.827348,-7.630116,-5.997032,-4.412076,3.124032,-7.031612,6.354720,-6.356893,7.947619,-7.950445,-7.210199,-9.967412,-4.629227,6.532942,7.607256,-2.509014,-7.216449,-5.811320,-1.895317,7.113654,6.563756,6.612236,-1.197066,-9.389836,6.598605,-5.450005,-7.279544,-7.999612,-9.918839,6.737507,-6.633064,4.339748,-4.618997,9.272409,-5.566006,-2.597703,8.079689,-1.201725,0.205956,4.122707,1.921599,-2.096840,-3.249113,1.033167,-8.649950,-7.637938,-7.212302,8.411777,3.251764,7.069761,-0.954330,9.789420,-2.134482,2.026466,-7.977295,-5.223701,-9.462438,7.911672,9.777933,0.127861,2.684985,-6.316466,8.218428,-8.961720,-9.917004,-3.495599,9.287828,-9.115755,-9.155847,-6.396756,-4.278858,-3.563381,2.763844,9.600741,-7.974861,0.566887,-1.530315,8.136134,5.868716,-1.891913,-4.904593,-0.330408,9.496675,2.025746,-0.299735,-5.894823,-0.704688,4.597078,2.369502,-5.561198,-2.580161,7.807422,3.464195,-3.694838,9.412523,-1.830354,-4.041364,5.286691,-0.996521,6.717164,-0.589766,5.856951,-2.909393,4.197926,-6.755330,-3.791097,9.883590,6.628983,-5.500362,0.525279,3.493994,3.410599,5.941390,9.259294,0.843623,-6.092765,-0.272866,-0.001724,9.886277,-3.805569,7.063792,-9.812083,4.679877,6.751506,6.184478,5.518136,2.843268,-1.556656,3.428186,-5.703896,-1.798790,5.725212,-4.556605,-1.399101,4.678120,3.482461,5.535318,5.871436,-0.679553,-4.987306,4.832139,-5.333338,9.582754,5.766783,-8.503908,5.073561,9.409600,2.594428,4.461582,8.891529,8.197378,1.205519,-8.541380,5.061239,-2.603821,-5.770600,8.783253,-4.760262,-8.691808,2.692122,5.082926,2.943237,2.162145,-0.624865,-3.751325,3.707351,9.868492,-2.189199,7.617674,-0.636409,-7.890396,-5.221305,4.746868,-4.969570,-4.134954,-2.832184,-2.449677,-9.281959,-3.813694,-5.640212,-3.423252,-7.163053,6.747527,3.189524,-6.561706,-0.737996,6.595381,-1.208240,6.070023,-2.425123,6.394931,8.890782,-8.808224,4.580657,-7.425822,-9.564905,-0.428877,-3.107147,6.799590,-8.972933,3.929818,-3.000096,0.359489,0.940271,9.248439,4.632342,-0.014709,0.328464,-6.070429,-0.274921,-5.538523,-1.019963,5.592369,-7.898752,-3.450235,4.383975,0.465207,-5.663222,-6.471148,3.058288,1.851926,-0.603899,1.922066,0.764795,0.232289,0.280959,-6.903830,-7.459961,-4.754724,-3.190582,9.195139,4.492132,-9.200092,-2.069367,3.820350,-0.553321,-0.439117,2.610021,-8.549184,7.025745,-5.741182,-7.089563,-2.632929,-6.958065,4.013169,-4.546063,-8.573875,-5.002844,2.097908,-3.993125,-9.785441,-4.544014,0.540520,7.585587,-8.646976,0.398895,4.758787,1.017916,-9.642794,-0.165154,-4.486585,7.101339,-3.011985,2.182843,-9.379681,0.017188,1.234827,2.462143,5.337028,-8.584577,6.442805,-5.317651,4.846881,2.696333,4.486083,-4.732431,-0.694748,9.573748,4.452053,-3.243108,-8.225761,-5.902475,5.179678,-6.476437,-3.159687,-0.551847,5.548588,-4.135061,-2.726222,-3.746071,-0.087959,-8.897429,-5.569235,6.177452,-3.987296,7.910293,7.353147,-6.775754,0.230900,1.886923,-2.925387,-1.206115,-7.526550,-4.497744,-5.219434,2.215678,4.675735,9.861968,7.677956,3.177667,-2.747559,-2.853139,5.343391,4.478950,9.263166,-4.604062,-8.427493,4.531227,-6.000526,-9.721162,6.013119,9.050824,0.646092,-4.110522,7.186996,-7.567162,1.148921,-0.047436,-2.437429,7.634650,-4.490760,4.115971,-4.977653,-4.783544,-8.455853,9.423640,-2.486706,5.079312,7.518089,-9.884863,2.727781,5.092420,8.277451,7.105132,1.061129,0.047264,5.295613,-7.423217,-7.885104,-5.944540,3.731492,-3.841928,-9.063271,7.628873,6.747024,-9.925744,5.701195,0.628613,5.892356,-6.789516,-4.146111,4.493461,-8.808052,4.677538,-8.992933,3.734032,-3.593313,3.813824,2.387622,-1.868900,-4.591097,-1.001608,-8.925717,-3.589001,-0.279317,-5.924668,-9.638319,-6.025172,-0.053783,0.243535,2.787761,-2.438567,-3.633517,-6.397628,9.712743,1.329938,-5.990357,1.722712,0.451548,-8.504501,-2.987898,-7.958229,-0.161404,7.798039,6.690133,3.791797,3.661600,-5.544404,4.125109,-6.073983,1.069857,-3.900036,9.237012,5.468160,9.499474,-7.467319,-0.450926,5.272867,-5.988439,4.054007,9.889279,-8.039538,1.232276,3.145833,-9.020029,8.857876,2.482077,8.457503,6.614959,2.902471,-3.965170,-2.312196,4.464967,-4.013801,-5.899012,9.598436,-3.276051,-8.585175], dtype = "float32")#candidate|8348|(910,)|const|float32
call_8347 = relay.TupleGetItem(func_1657_call(relay.reshape(const_8348.astype('float32'), [7, 10, 13])), 0)
call_8349 = relay.TupleGetItem(func_1660_call(relay.reshape(const_8348.astype('float32'), [7, 10, 13])), 0)
output = relay.Tuple([call_8298,call_8347,const_8348,])
output2 = relay.Tuple([call_8299,call_8349,const_8348,])
func_8355 = relay.Function([], output)
mod['func_8355'] = func_8355
mod = relay.transform.InferType()(mod)
output = func_8355()
func_8356 = relay.Function([], output)
mutated_mod['func_8356'] = func_8356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7667_call = mod.get_global_var('func_7667')
func_7668_call = mutated_mod.get_global_var('func_7668')
call_8468 = relay.TupleGetItem(func_7667_call(), 1)
call_8469 = relay.TupleGetItem(func_7668_call(), 1)
func_5294_call = mod.get_global_var('func_5294')
func_5295_call = mutated_mod.get_global_var('func_5295')
call_8478 = relay.TupleGetItem(func_5294_call(), 2)
call_8479 = relay.TupleGetItem(func_5295_call(), 2)
output = relay.Tuple([call_8468,call_8478,])
output2 = relay.Tuple([call_8469,call_8479,])
func_8483 = relay.Function([], output)
mod['func_8483'] = func_8483
mod = relay.transform.InferType()(mod)
output = func_8483()
func_8484 = relay.Function([], output)
mutated_mod['func_8484'] = func_8484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mod.get_global_var('func_5818')
func_5819_call = mutated_mod.get_global_var('func_5819')
call_8529 = relay.TupleGetItem(func_5818_call(), 0)
call_8530 = relay.TupleGetItem(func_5819_call(), 0)
output = relay.Tuple([call_8529,])
output2 = relay.Tuple([call_8530,])
func_8531 = relay.Function([], output)
mod['func_8531'] = func_8531
mod = relay.transform.InferType()(mod)
output = func_8531()
func_8532 = relay.Function([], output)
mutated_mod['func_8532'] = func_8532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5696_call = mod.get_global_var('func_5696')
func_5697_call = mutated_mod.get_global_var('func_5697')
call_8543 = relay.TupleGetItem(func_5696_call(), 0)
call_8544 = relay.TupleGetItem(func_5697_call(), 0)
func_4815_call = mod.get_global_var('func_4815')
func_4818_call = mutated_mod.get_global_var('func_4818')
var_8547 = relay.var("var_8547", dtype = "float64", shape = (2, 240))#candidate|8547|(2, 240)|var|float64
call_8546 = func_4815_call(relay.reshape(var_8547.astype('float64'), [10, 16, 3]))
call_8548 = func_4815_call(relay.reshape(var_8547.astype('float64'), [10, 16, 3]))
func_7872_call = mod.get_global_var('func_7872')
func_7874_call = mutated_mod.get_global_var('func_7874')
call_8556 = relay.TupleGetItem(func_7872_call(), 1)
call_8557 = relay.TupleGetItem(func_7874_call(), 1)
func_1369_call = mod.get_global_var('func_1369')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_8566 = relay.TupleGetItem(func_1369_call(), 0)
call_8567 = relay.TupleGetItem(func_1371_call(), 0)
func_4196_call = mod.get_global_var('func_4196')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_8573 = relay.TupleGetItem(func_4196_call(), 0)
call_8574 = relay.TupleGetItem(func_4197_call(), 0)
output = relay.Tuple([call_8543,call_8546,var_8547,call_8556,call_8566,call_8573,])
output2 = relay.Tuple([call_8544,call_8548,var_8547,call_8557,call_8567,call_8574,])
func_8580 = relay.Function([var_8547,], output)
mod['func_8580'] = func_8580
mod = relay.transform.InferType()(mod)
var_8581 = relay.var("var_8581", dtype = "float64", shape = (2, 240))#candidate|8581|(2, 240)|var|float64
output = func_8580(var_8581)
func_8582 = relay.Function([var_8581], output)
mutated_mod['func_8582'] = func_8582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_8613 = func_1694_call()
call_8614 = func_1694_call()
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_8631 = relay.TupleGetItem(func_1502_call(), 0)
call_8632 = relay.TupleGetItem(func_1504_call(), 0)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_8653 = func_1704_call()
call_8654 = func_1704_call()
output = relay.Tuple([call_8613,call_8631,call_8653,])
output2 = relay.Tuple([call_8614,call_8632,call_8654,])
func_8657 = relay.Function([], output)
mod['func_8657'] = func_8657
mod = relay.transform.InferType()(mod)
output = func_8657()
func_8658 = relay.Function([], output)
mutated_mod['func_8658'] = func_8658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6063_call = mod.get_global_var('func_6063')
func_6065_call = mutated_mod.get_global_var('func_6065')
call_8700 = relay.TupleGetItem(func_6063_call(), 0)
call_8701 = relay.TupleGetItem(func_6065_call(), 0)
func_7097_call = mod.get_global_var('func_7097')
func_7098_call = mutated_mod.get_global_var('func_7098')
call_8723 = relay.TupleGetItem(func_7097_call(), 3)
call_8724 = relay.TupleGetItem(func_7098_call(), 3)
bop_8726 = relay.logical_or(call_8723.astype('bool'), call_8700.astype('bool')) # shape=(1001,)
bop_8729 = relay.logical_or(call_8724.astype('bool'), call_8701.astype('bool')) # shape=(1001,)
bop_8732 = relay.minimum(bop_8726.astype('uint32'), call_8700.astype('uint32')) # shape=(1001,)
bop_8735 = relay.minimum(bop_8729.astype('uint32'), call_8701.astype('uint32')) # shape=(1001,)
output = relay.Tuple([bop_8732,])
output2 = relay.Tuple([bop_8735,])
func_8743 = relay.Function([], output)
mod['func_8743'] = func_8743
mod = relay.transform.InferType()(mod)
output = func_8743()
func_8744 = relay.Function([], output)
mutated_mod['func_8744'] = func_8744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3230_call = mod.get_global_var('func_3230')
func_3232_call = mutated_mod.get_global_var('func_3232')
call_8758 = func_3230_call()
call_8759 = func_3230_call()
func_2530_call = mod.get_global_var('func_2530')
func_2532_call = mutated_mod.get_global_var('func_2532')
call_8766 = relay.TupleGetItem(func_2530_call(), 0)
call_8767 = relay.TupleGetItem(func_2532_call(), 0)
func_5421_call = mod.get_global_var('func_5421')
func_5422_call = mutated_mod.get_global_var('func_5422')
call_8772 = func_5421_call()
call_8773 = func_5421_call()
output = relay.Tuple([call_8758,call_8766,call_8772,])
output2 = relay.Tuple([call_8759,call_8767,call_8773,])
func_8785 = relay.Function([], output)
mod['func_8785'] = func_8785
mod = relay.transform.InferType()(mod)
mutated_mod['func_8785'] = func_8785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8785_call = mutated_mod.get_global_var('func_8785')
call_8786 = func_8785_call()
output = call_8786
func_8787 = relay.Function([], output)
mutated_mod['func_8787'] = func_8787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4754_call = mod.get_global_var('func_4754')
func_4756_call = mutated_mod.get_global_var('func_4756')
call_8797 = relay.TupleGetItem(func_4754_call(), 1)
call_8798 = relay.TupleGetItem(func_4756_call(), 1)
func_3230_call = mod.get_global_var('func_3230')
func_3232_call = mutated_mod.get_global_var('func_3232')
call_8820 = func_3230_call()
call_8821 = func_3230_call()
output = relay.Tuple([call_8797,call_8820,])
output2 = relay.Tuple([call_8798,call_8821,])
func_8838 = relay.Function([], output)
mod['func_8838'] = func_8838
mod = relay.transform.InferType()(mod)
mutated_mod['func_8838'] = func_8838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8838_call = mutated_mod.get_global_var('func_8838')
call_8839 = func_8838_call()
output = call_8839
func_8840 = relay.Function([], output)
mutated_mod['func_8840'] = func_8840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4312_call = mod.get_global_var('func_4312')
func_4314_call = mutated_mod.get_global_var('func_4314')
call_8854 = relay.TupleGetItem(func_4312_call(), 0)
call_8855 = relay.TupleGetItem(func_4314_call(), 0)
output = relay.Tuple([call_8854,])
output2 = relay.Tuple([call_8855,])
func_8887 = relay.Function([], output)
mod['func_8887'] = func_8887
mod = relay.transform.InferType()(mod)
output = func_8887()
func_8888 = relay.Function([], output)
mutated_mod['func_8888'] = func_8888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_8903 = relay.TupleGetItem(func_1318_call(), 1)
call_8904 = relay.TupleGetItem(func_1319_call(), 1)
func_3129_call = mod.get_global_var('func_3129')
func_3133_call = mutated_mod.get_global_var('func_3133')
var_8907 = relay.var("var_8907", dtype = "float32", shape = (24,))#candidate|8907|(24,)|var|float32
var_8908 = relay.var("var_8908", dtype = "float32", shape = (280,))#candidate|8908|(280,)|var|float32
call_8906 = relay.TupleGetItem(func_3129_call(relay.reshape(var_8907.astype('float32'), [24,]), relay.reshape(var_8908.astype('float32'), [280,]), ), 4)
call_8909 = relay.TupleGetItem(func_3133_call(relay.reshape(var_8907.astype('float32'), [24,]), relay.reshape(var_8908.astype('float32'), [280,]), ), 4)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_8912 = func_1704_call()
call_8913 = func_1704_call()
output = relay.Tuple([call_8903,call_8906,var_8907,var_8908,call_8912,])
output2 = relay.Tuple([call_8904,call_8909,var_8907,var_8908,call_8913,])
func_8926 = relay.Function([var_8907,var_8908,], output)
mod['func_8926'] = func_8926
mod = relay.transform.InferType()(mod)
mutated_mod['func_8926'] = func_8926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8926_call = mutated_mod.get_global_var('func_8926')
var_8928 = relay.var("var_8928", dtype = "float32", shape = (24,))#candidate|8928|(24,)|var|float32
var_8929 = relay.var("var_8929", dtype = "float32", shape = (280,))#candidate|8929|(280,)|var|float32
call_8927 = func_8926_call(var_8928,var_8929,)
output = call_8927
func_8930 = relay.Function([var_8928,var_8929,], output)
mutated_mod['func_8930'] = func_8930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5839_call = mod.get_global_var('func_5839')
func_5841_call = mutated_mod.get_global_var('func_5841')
call_8946 = relay.TupleGetItem(func_5839_call(), 0)
call_8947 = relay.TupleGetItem(func_5841_call(), 0)
func_7872_call = mod.get_global_var('func_7872')
func_7874_call = mutated_mod.get_global_var('func_7874')
call_8948 = relay.TupleGetItem(func_7872_call(), 0)
call_8949 = relay.TupleGetItem(func_7874_call(), 0)
output = relay.Tuple([call_8946,call_8948,])
output2 = relay.Tuple([call_8947,call_8949,])
func_8971 = relay.Function([], output)
mod['func_8971'] = func_8971
mod = relay.transform.InferType()(mod)
mutated_mod['func_8971'] = func_8971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8971_call = mutated_mod.get_global_var('func_8971')
call_8972 = func_8971_call()
output = call_8972
func_8973 = relay.Function([], output)
mutated_mod['func_8973'] = func_8973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mod.get_global_var('func_5818')
func_5819_call = mutated_mod.get_global_var('func_5819')
call_9080 = relay.TupleGetItem(func_5818_call(), 0)
call_9081 = relay.TupleGetItem(func_5819_call(), 0)
func_4807_call = mod.get_global_var('func_4807')
func_4809_call = mutated_mod.get_global_var('func_4809')
call_9121 = relay.TupleGetItem(func_4807_call(), 0)
call_9122 = relay.TupleGetItem(func_4809_call(), 0)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_9143 = relay.TupleGetItem(func_2912_call(), 1)
call_9144 = relay.TupleGetItem(func_2913_call(), 1)
output = relay.Tuple([call_9080,call_9121,call_9143,])
output2 = relay.Tuple([call_9081,call_9122,call_9144,])
func_9160 = relay.Function([], output)
mod['func_9160'] = func_9160
mod = relay.transform.InferType()(mod)
output = func_9160()
func_9161 = relay.Function([], output)
mutated_mod['func_9161'] = func_9161
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9254 = relay.var("var_9254", dtype = "uint32", shape = (7, 4, 3))#candidate|9254|(7, 4, 3)|var|uint32
var_9255 = relay.var("var_9255", dtype = "uint32", shape = (7, 4, 3))#candidate|9255|(7, 4, 3)|var|uint32
bop_9256 = relay.subtract(var_9254.astype('uint32'), relay.reshape(var_9255.astype('uint32'), relay.shape_of(var_9254))) # shape=(7, 4, 3)
output = bop_9256
output2 = bop_9256
func_9259 = relay.Function([var_9254,var_9255,], output)
mod['func_9259'] = func_9259
mod = relay.transform.InferType()(mod)
mutated_mod['func_9259'] = func_9259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9259_call = mutated_mod.get_global_var('func_9259')
var_9261 = relay.var("var_9261", dtype = "uint32", shape = (7, 4, 3))#candidate|9261|(7, 4, 3)|var|uint32
var_9262 = relay.var("var_9262", dtype = "uint32", shape = (7, 4, 3))#candidate|9262|(7, 4, 3)|var|uint32
call_9260 = func_9259_call(var_9261,var_9262,)
output = call_9260
func_9263 = relay.Function([var_9261,var_9262,], output)
mutated_mod['func_9263'] = func_9263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8531_call = mod.get_global_var('func_8531')
func_8532_call = mutated_mod.get_global_var('func_8532')
call_9287 = relay.TupleGetItem(func_8531_call(), 0)
call_9288 = relay.TupleGetItem(func_8532_call(), 0)
func_5294_call = mod.get_global_var('func_5294')
func_5295_call = mutated_mod.get_global_var('func_5295')
call_9289 = relay.TupleGetItem(func_5294_call(), 5)
call_9290 = relay.TupleGetItem(func_5295_call(), 5)
func_8238_call = mod.get_global_var('func_8238')
func_8239_call = mutated_mod.get_global_var('func_8239')
call_9323 = relay.TupleGetItem(func_8238_call(), 1)
call_9324 = relay.TupleGetItem(func_8239_call(), 1)
output = relay.Tuple([call_9287,call_9289,call_9323,])
output2 = relay.Tuple([call_9288,call_9290,call_9324,])
func_9329 = relay.Function([], output)
mod['func_9329'] = func_9329
mod = relay.transform.InferType()(mod)
mutated_mod['func_9329'] = func_9329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9329_call = mutated_mod.get_global_var('func_9329')
call_9330 = func_9329_call()
output = call_9330
func_9331 = relay.Function([], output)
mutated_mod['func_9331'] = func_9331
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9332 = relay.const(-5, dtype = "int16")#candidate|9332|()|const|int16
const_9333 = relay.const([[[-10,-9,-1],[-1,-2,10],[-10,9,-4],[1,10,-5],[-4,-1,8]],[[-10,4,-5],[-10,3,9],[-4,-4,-6],[-3,-8,-5],[-5,-5,3]],[[4,-2,-7],[-5,-5,1],[-4,5,-7],[8,10,-10],[-10,1,1]],[[9,-9,6],[-7,-5,1],[-6,-10,-5],[-4,6,1],[-6,-2,6]],[[-2,1,-7],[-1,7,-9],[-1,-5,8],[7,-3,5],[-10,-4,-9]],[[-6,-9,-6],[3,3,1],[-10,8,3],[-5,7,5],[1,4,-8]],[[8,-6,8],[-3,9,-2],[-7,5,10],[-1,-2,3],[2,-3,-1]],[[-9,-2,6],[-9,2,5],[2,-8,9],[-7,-1,3],[-6,-9,-1]],[[-9,-1,-9],[4,6,-8],[2,4,7],[6,-8,-2],[-2,-5,-9]],[[-3,-9,1],[1,-8,1],[-7,5,3],[-7,-7,5],[-5,8,-9]],[[-6,-5,-9],[5,-2,-7],[6,-8,-7],[5,9,10],[-1,-2,-3]],[[-6,-5,6],[-7,-4,-1],[-6,6,9],[6,-1,6],[-10,6,-6]],[[4,10,2],[3,-4,-10],[7,3,9],[-9,8,1],[-1,2,4]],[[-8,9,6],[-3,-1,-6],[-1,7,8],[-10,1,9],[5,-5,-9]],[[5,5,-5],[-7,2,5],[-1,2,-2],[3,1,1],[8,-2,-3]]], dtype = "int16")#candidate|9333|(15, 5, 3)|const|int16
bop_9334 = relay.bitwise_xor(const_9332.astype('int16'), const_9333.astype('int16')) # shape=(15, 5, 3)
output = bop_9334
output2 = bop_9334
func_9338 = relay.Function([], output)
mod['func_9338'] = func_9338
mod = relay.transform.InferType()(mod)
output = func_9338()
func_9339 = relay.Function([], output)
mutated_mod['func_9339'] = func_9339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4277_call = mod.get_global_var('func_4277')
func_4278_call = mutated_mod.get_global_var('func_4278')
call_9417 = func_4277_call()
call_9418 = func_4277_call()
output = call_9417
output2 = call_9418
func_9437 = relay.Function([], output)
mod['func_9437'] = func_9437
mod = relay.transform.InferType()(mod)
mutated_mod['func_9437'] = func_9437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9437_call = mutated_mod.get_global_var('func_9437')
call_9438 = func_9437_call()
output = call_9438
func_9439 = relay.Function([], output)
mutated_mod['func_9439'] = func_9439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9461 = relay.var("var_9461", dtype = "int16", shape = (1, 13, 13))#candidate|9461|(1, 13, 13)|var|int16
var_9462 = relay.var("var_9462", dtype = "int16", shape = (9, 13, 13))#candidate|9462|(9, 13, 13)|var|int16
bop_9463 = relay.multiply(var_9461.astype('int16'), var_9462.astype('int16')) # shape=(9, 13, 13)
uop_9469 = relay.atan(var_9461.astype('float64')) # shape=(1, 13, 13)
bop_9471 = relay.divide(uop_9469.astype('float32'), relay.reshape(var_9461.astype('float32'), relay.shape_of(uop_9469))) # shape=(1, 13, 13)
output = relay.Tuple([bop_9463,bop_9471,])
output2 = relay.Tuple([bop_9463,bop_9471,])
func_9483 = relay.Function([var_9461,var_9462,], output)
mod['func_9483'] = func_9483
mod = relay.transform.InferType()(mod)
mutated_mod['func_9483'] = func_9483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9483_call = mutated_mod.get_global_var('func_9483')
var_9485 = relay.var("var_9485", dtype = "int16", shape = (1, 13, 13))#candidate|9485|(1, 13, 13)|var|int16
var_9486 = relay.var("var_9486", dtype = "int16", shape = (9, 13, 13))#candidate|9486|(9, 13, 13)|var|int16
call_9484 = func_9483_call(var_9485,var_9486,)
output = call_9484
func_9487 = relay.Function([var_9485,var_9486,], output)
mutated_mod['func_9487'] = func_9487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8483_call = mod.get_global_var('func_8483')
func_8484_call = mutated_mod.get_global_var('func_8484')
call_9504 = relay.TupleGetItem(func_8483_call(), 0)
call_9505 = relay.TupleGetItem(func_8484_call(), 0)
output = call_9504
output2 = call_9505
func_9512 = relay.Function([], output)
mod['func_9512'] = func_9512
mod = relay.transform.InferType()(mod)
output = func_9512()
func_9513 = relay.Function([], output)
mutated_mod['func_9513'] = func_9513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3186_call = mod.get_global_var('func_3186')
func_3187_call = mutated_mod.get_global_var('func_3187')
call_9528 = func_3186_call()
call_9529 = func_3186_call()
output = call_9528
output2 = call_9529
func_9538 = relay.Function([], output)
mod['func_9538'] = func_9538
mod = relay.transform.InferType()(mod)
mutated_mod['func_9538'] = func_9538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9538_call = mutated_mod.get_global_var('func_9538')
call_9539 = func_9538_call()
output = call_9539
func_9540 = relay.Function([], output)
mutated_mod['func_9540'] = func_9540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5917_call = mod.get_global_var('func_5917')
func_5919_call = mutated_mod.get_global_var('func_5919')
call_9559 = func_5917_call()
call_9560 = func_5917_call()
func_5901_call = mod.get_global_var('func_5901')
func_5902_call = mutated_mod.get_global_var('func_5902')
call_9574 = func_5901_call()
call_9575 = func_5901_call()
func_4779_call = mod.get_global_var('func_4779')
func_4784_call = mutated_mod.get_global_var('func_4784')
const_9580 = relay.const([1.821141,-7.300354,6.222222,-6.720140,-1.429866,0.871650,-9.640243,7.752152,9.889903,8.371505,4.096259,9.722660,-6.919633,8.624345,7.828816,3.441567,5.774363,-1.209828,7.131115,1.872902,-6.766304,-3.830183,-6.616070,-4.259158,0.790177,8.032648,5.477279,1.343555,0.217598,-2.383724,-0.218070,3.602816,2.609696,-1.874722,-9.114148,-9.679268,5.618179,6.192454,2.016438,4.188788,5.746117,1.481242,8.805740,5.417464,-7.514188,0.333239,9.451352,-4.418296,0.472821,1.520287,-2.742321,-5.420859,-2.297487,1.368730,-4.826073,-4.958075,8.172675,-4.569609,7.410693,6.987079,0.190362,-5.999686,2.697566,-1.145989,-6.365158,-5.704000,7.750288,-2.586734,-4.606995,7.940834,-5.906610,7.714004,-3.399375,-6.347928,1.449699,5.380405,8.463390,0.646630,-8.582596,0.404146,9.136768,1.034716,-3.673760,-2.215341,2.198587,3.090865,-9.523870,3.928027,0.023533,-1.151496,-1.829163,9.017912,2.457137,-8.985714,-2.339408,-8.876273,-5.765178,9.495359,6.277907,5.250530,4.288041,-5.893500,1.327921,-3.365376,-8.380213,3.859365,-1.154578,-4.036207,4.901088,2.886600,-6.663332,0.649613,0.737856,5.714143,8.896071,1.797166,-7.550227,-8.872621,-1.285920,-6.754630,8.682408,3.593560,-4.248211,6.795877,-2.313209,-7.303233,5.111978,8.550837,-9.416065,2.827446,-3.699371,-6.868652,5.968192,-2.015662,-2.124803,-1.012466,1.686566,4.635568,2.163365,3.024455,-6.750371,-2.959717,-7.185954,-9.651357,-2.697945,-8.549916,3.394201,7.210722,7.008961,-0.529528,-9.718926,9.014263,-9.664394,-9.897204,0.650031,3.342338,8.300856,4.562029,-4.382305,-4.946123,-0.434940,2.429668,0.924421,-0.100225,-7.010077,-4.434147,9.961759,-6.475413,5.518156,5.580984,4.412289,-7.463371,-5.635006,-5.582625,4.430881,1.738795,5.016226,8.478388,-9.963442,6.125115,-3.501826,7.882637,5.553799,6.543605,-3.560272,3.491800,-3.436361,-1.222642,-2.072315,9.820264,5.474349,1.131529,8.756073,-5.719125,-1.517279,-2.762000,7.222366,-7.762237,-8.004379,7.118532,-7.235636,-8.484069,-2.328390,4.876939,8.927113,8.461766,5.260398,2.589729,3.509720,-4.567049,7.618189,4.101098,0.888237,7.986088,8.756361,-6.276089,2.523698,-9.926389,-2.225673,-3.226845,-4.089622,-9.561707,-9.515134,-4.791874,8.228691,3.643062,-6.623764,-7.004417,-7.090585,0.655654,-4.878225,3.790575,-2.609779,-2.198349,1.353757,-5.641414,-0.162602,-0.015244,-3.452424,-8.133409,3.024915,-3.398749,-5.097723,5.801248,-8.180279,7.203542,6.378583,-0.410845,-6.934420,-7.414745,-3.497344,-0.501947,9.821555,2.970312,3.030922,-4.721812,-1.247816,-8.853798,6.567311,7.215693,-5.139110,-2.331228,-6.265903,6.251641,5.279429,-5.179030,-9.549199,-7.659323,2.602849,2.859083,-2.849908,-7.109349,-8.585872,4.071696,-4.945579,3.020252,9.086944,-9.720365,8.106462,2.326570,7.186713,-5.629351,-7.070392,-8.927070,-6.590150,-1.023916,9.604016,3.445292,-3.850751,7.885116,-9.837205,3.416955,-0.369574,7.726862,-5.486056,0.937394,-7.824274,6.764467,-2.156147,8.327433,-4.436131,1.622876,-6.684543,5.439349,-6.285453,8.360000,-2.233735,-0.137636,4.883130,-8.313552,-3.785526,4.510597,9.460024,3.209626,-4.716823,-3.814160,0.838691,-8.334099,5.167325,-0.404991,-2.869992,-6.211776,-6.974639,-8.286512,-9.163609,4.022175,-2.653356,0.929689,-7.695377,1.567349,7.302207,8.011399,-4.963010,-4.503457,9.075561,0.474563,7.050929,-6.747381,-4.962368,3.821219,2.606441,-4.410599,8.655817,0.700101,-7.772379,7.048963,2.193610,-2.583758,-1.483614,8.082969,0.775431,-8.206695,-5.283209,2.175049,2.670138,7.709689,2.794599,-1.272029,1.599203,-7.087557,-2.759367,-2.132550,-8.198363,9.552306,1.601040,8.309637,6.589350,7.823638,-3.448303,3.338386,7.418797,9.713094,-6.557155,-8.973904,4.973258,6.899264,-6.566712,9.213485,2.570629,4.211813,7.732800,6.637161,-2.955077,-3.167729,0.482833,-9.787067,-5.660741,-0.381605,6.536713,2.062033,9.541991,4.089811,-9.406797,3.134308,4.403045,-6.008423,3.899265,-5.369453,9.906555,-3.207400,-5.874143,2.335994,-1.890757,0.657425,-5.387948,8.256856,9.274106,9.406467,8.018568,1.794148,-4.569645,-9.373933,-2.466277,6.434032,0.189821,-5.048605,2.900121,1.591172,9.922522,4.281870,5.808437,-9.085973,9.917609,-4.957081,-0.445038,-4.711872,7.244604,-8.239580,8.908809,1.778933,5.944728,-5.817718,-3.978429,8.366137,-0.413534,4.929596,4.147561,-9.974246,-6.681092,2.376851,9.096087,0.429767,-8.380231,-0.205371,1.978003,1.629192,9.643049,1.984758,1.042071,-7.079461,-8.841969,2.512312,8.585640,-8.944005,-9.982287,-1.935688,0.250932,-7.941322,3.190651,2.615450,2.553029,1.859562,-4.354704,-6.818886,9.285584,3.754557,-1.701186,0.187099,4.049443,6.092071,-0.185823,4.213501,6.314424,8.690578,-6.556142,-0.040732,4.466878,-2.383160,-9.570985,1.419734,3.732451,5.692481,2.143771,0.649979,3.057968,-7.557833,-8.184073,0.127186,-6.932791,-2.726354,-7.235657,-1.529974,3.936396,3.030696,6.607242,9.665086,-4.417725,-3.315076,-0.386871,-1.741631,7.751950,2.124893,-6.868538,7.489874,6.263676,0.583045,-6.155458,-9.003752,-6.939995,-3.956370,-3.693408,2.415297,-8.983431,3.612487,6.231470,-1.132440,-4.861450,1.202334,9.955875,6.231439,-9.143319,-9.037420,-7.141427,-0.477984,-0.721274,-7.317928,2.923445,6.162480,-9.978326,-7.825790,-1.068045,-2.127208,-7.309639,5.495976,-6.714970,-4.164470,7.816665,-4.270355,4.763262,4.423241,9.941746,8.085162,2.740557,-3.880413,6.787348,5.317884,-5.805731,-7.576212,2.720659,-2.565934,0.280596,1.907442,6.205233,-8.037164,-0.801609,-5.573895,-5.580297,-5.519935,9.725063,6.222898,7.545458,-3.700376,-3.384459,-1.117336,8.017306,2.571970,-2.544209,4.985960,-9.709946,-5.481679,2.632336,-9.596258,-5.724909,5.610783,-0.612854,-7.626799,-6.182627,0.848116,-0.190431,-1.577270,-0.800216,-2.569380,-3.418372,-1.160921,6.398323,-3.215674,1.980567,-6.690794,8.457046,5.473199,-9.249837,-9.550761,7.712183,7.130659,7.952927,1.910838,-1.338691,-2.648532,5.680354,5.772160,-0.006766,-1.802212,6.958201,2.322703,-2.921014,-6.054370,5.340142,0.305039,-7.498720,-1.148280,9.664978,1.332193,1.570700,-4.552946,-3.874796,9.764956,4.346726,-5.604145,6.668518,-3.707817,5.218004,-6.552043,9.026253,5.549900,7.991704,7.523110,3.865162,-0.143984,3.605790,2.087456,-9.688837,-3.735232,-2.919812,-4.120835,-4.588928,-4.131120,9.141337,-7.025984,-5.985607,-1.402820,3.656195,-5.228412,-4.129350,7.500957,-0.508206,3.027660,-0.964345,-5.133639,8.139851,-5.952465,4.417192,4.171263,5.854728,2.632731,6.600426,0.233587,-9.700706,9.755657,-1.542807,-7.849487,7.869738,-7.612193,8.486400,8.006918,6.510876,-9.471883,-1.682360,-8.749024,-3.853043,9.921414,7.995406,-3.265058,3.369677,3.893182,6.565907,-8.460916,4.233055,-2.016840,4.369192,6.523101,9.225515,-8.227556,9.457436,2.744385,-5.923568,7.456089,-7.735158,7.395147,2.688037,5.990706,-8.646608,-0.457817,-0.252268,-3.874001,-8.695330,5.147454,-2.463396,4.578153,-5.020081,3.556359,0.764569,-2.261913,-2.344098,3.515176,-4.063215,-5.779620,-7.443604,3.401595,7.833070,2.357421,0.720507,2.227690,-4.437284,-2.746932,-3.546219,1.437777,-1.235698,3.707572,-4.316561,8.041837,5.377897,2.790519,-8.117409,8.224343,7.128046,9.368011,6.830398,-0.442073,8.078833,-0.306490,-8.618364,0.093759,0.554086,5.504838,-6.419870,2.091605,2.410236,9.209387,8.078362,3.353021,9.916859,3.541522,-3.157876,-2.507876,-0.932490,9.733996,4.193604,-4.985233,9.241768,-5.082957,-1.244342,2.739501,-4.220226,6.838842,6.659088,-8.238945,6.505277,4.811484,6.731087,9.608849,-5.673335,-9.724481,1.780278,6.539497,5.597973,-2.107142,0.728139,9.467779,3.150198,5.128820,8.257606,2.330647,7.403246,-5.913837,1.336874,9.595565,-5.671792,2.354221,-7.232970,-6.120164,-3.336556,3.301502,0.522030,7.274647,6.057686,1.399586,5.999327,9.392252,-2.368481,2.356080,0.281471,4.310987,1.491586,2.197908,5.345784,1.199146,4.065156,3.191256,0.190534,9.842741,6.555603,5.201982,2.136800,-3.078802,7.065263,8.495098,-2.910285,-3.005811,2.497230,4.265096,-2.561420,-0.350388,6.631722,-7.353771,3.264039,5.444068,-2.408738,7.599006,4.053220,4.566536,1.740225,9.569698,-3.834708,6.236573,4.738140,-2.690380,8.577210,8.452635,4.494256,8.874756,0.292408,6.893456,-6.158072,-1.373670,-2.836141,-5.608450,-1.152434,9.043290,8.288581,4.120704,7.229619,-0.950876,-9.355757,3.118113,8.818790,-6.966048,7.058003,1.771190,-6.846837,4.154091,5.338318,6.886578,1.455807,-2.930158,0.152746,-3.710114,-5.824975,-5.239299,-7.497794,-1.916042,-4.453574,6.489679,-1.169488,7.005530,-8.468691,-3.443528,-1.598505,8.071659,-6.516802,1.184064,9.830488,5.348060,-1.302653,6.926497,3.956813,9.167815,-8.794264,-4.010763,7.593228,-8.612998,-2.446224,0.276777,-9.263272,5.491542,0.106426,-4.767559,-4.386270,-9.113284,7.716720,0.269645,0.544577,1.217716,4.830670,-6.389291,3.533694,-2.071128,5.831997,8.685079,1.232044,2.510083,3.994809,7.565514,2.778589,-4.147466,4.103799,6.540214,-0.405297,4.825955,-1.415694,-2.632741,-9.467157,-8.495868,9.387042,3.796460,-1.852571,3.526420,-6.145928,0.307309,-6.017342,8.839732,5.017236,-1.478188,0.189705,-3.559563,6.744524,4.114218,6.509691,-1.565996,4.523720,2.252069,-0.187343,5.909026,-3.380380,-9.587979,1.527721,-2.385089,-2.813469,-1.618648,-3.850564,-6.282448,-1.829327,9.549487,7.014275,-6.044284,5.622707,-4.968770,-4.115788,9.574034,-6.854979,8.605405,0.271912,-3.837550,-9.707830,7.680227,6.614156,-8.937309,9.384559,-9.121224,1.065335,-2.344990,-0.609344,-3.154070,-7.905486,3.577085,8.234777,-3.916467,6.684718,4.451111,-1.676704,-0.205860,-9.455518,4.475757,3.372648,-2.888777,-1.107602,8.809033,4.987461,8.870346,2.180273,-7.701365,1.202544,3.995960,3.373367,-5.704566,2.648488,-6.870247,1.571107,-7.615174,3.322249,-8.169491,1.067920,-0.913686,2.306478,-3.206198,2.512618,-3.600473,-6.780132,4.355227,-6.826058,6.421894,-7.543661,2.519620,8.557278,-6.547208,-0.564435,-0.389360,6.697680,-2.369831,-9.949530,2.969094,2.560635,-3.953445,-8.708586,0.486906,5.426288,-2.705804,-1.217303,3.015945,7.239033,-3.310696,-0.635978,1.691210,-8.872226,2.344835,5.955832,-6.676799,-3.915093,-9.460280,-7.779505,1.438939,-9.256306,7.853790,0.143297,-4.576546,3.886634,-7.074737,4.886030,7.789669,7.219374,-4.372177,6.825345,8.795362,0.600010,-6.341284,7.540466,0.308215,-5.031557,4.812110,8.935275,-2.957097,-7.684266,8.777845,2.043146,9.748596,8.506617,6.978081,-8.206775,-3.948189,-6.181411,9.978038,-6.311461,0.058059,-7.492425,-6.749430,-7.577639,-2.028414,7.381140,-0.298291,-9.253709,3.620717,6.539036,-6.635326,1.867335,1.480690,-9.667298,1.334929,9.604175,0.026404,3.172947,1.171019,-0.270249,2.605531,5.366252,-5.146463,4.997715,6.103999,-5.011192,1.645575,-6.063278,5.701913,9.955928,8.771078,0.436140,-4.672378,-0.904472,-7.779467,4.109587,-8.575280,3.974696,-9.972922,-8.440442,4.368027,-5.551938,-8.414744,6.403808,1.097082,1.779256,6.372606,5.701945,2.942766,-9.003753,-3.274780,3.529775,-6.697111,-4.979813,-2.444305,2.616664,6.928241,-1.072857,-5.646215,-2.199823,-7.135520,8.044422,-0.986195,-6.792493,-3.373540,-2.779908,-2.441867,-8.708493,-4.710510,-0.452680,1.514780,7.041020,0.765445,6.728688,6.669237,8.176872,3.931155,-4.916055,1.719469,2.791318,0.493796,-1.728712,-1.008743,-5.812921,3.994442,1.850414,-7.677443,-6.258122,-6.343462,-7.157564,3.471352,7.574731,-0.815548,-2.616253,-7.049933,0.092734,2.806382,-7.214966,-3.038088,4.069620,6.618885,9.252556,2.771281,4.690953,8.666310,0.163118,3.052843,7.562954,-2.531492,2.438988,1.422419,-2.716421,-5.607623,-1.461266,-7.057349,7.347516,-3.982515,7.912969,-3.324758,1.618943,-9.727686,-8.532801,-9.362591,5.806699,0.818417,5.027450,-6.816107,-9.269429,-2.980410,8.486940,-7.558505,-5.494427,3.479338,-0.029378,-8.545897,4.190291,-8.424716,-7.589457,7.414921,-1.155330,-6.471779,-3.095250,9.732614,-8.825933,4.809899,-8.120324,-9.762686,8.504353,5.758219,6.107314,3.467309,-5.107427,-6.899051,-4.646826,4.694490,-9.543515,5.847320,-3.250866,3.119379,-6.398806,-9.778532,-6.502330,-6.635002,3.709041,0.256529,0.648776,6.599967,3.856987,2.586064,-9.082776,-7.825607,-4.973833,5.545384,-7.017219,5.678932,5.383321,-6.083882,-6.647210,1.905953,-1.788047,-6.463271,-4.535215,4.728444,1.070670,3.195745,9.703265,3.255393,2.117706,-2.355664,5.922079,5.159397,-6.301323,5.020126,-7.357380,-2.193644,4.910538,-4.527548,-4.234774,0.024418,-5.217358,4.022228,-8.791208,-9.873698,5.846254,-2.945657,-0.298735,-8.505394,9.649611,-1.287811,-4.711877,-0.208621,2.275503,2.140918,-6.334679,-6.226238,-6.383482,7.890365,-5.209159,-6.533846,-0.833989,-5.711895,-9.258282,5.315630,-9.050352,4.799571,-4.385119,4.931387,5.611231,-5.875050,1.104282,-5.010171,-9.895128,6.241126,6.464758,8.136612,-7.191613,8.693822,-0.463030,-3.294106,-6.255941,3.446047,2.108307,-2.665166,-4.895009,-3.016255,0.186501,9.273796,-0.675484,-8.841170,-4.177421,-5.680764,-6.976604,-7.852287,-3.983959,7.833387,-7.956979,-6.112298,3.501602,-6.838161,3.669133,-2.243505,-0.310442,-0.420640,-1.122007,-8.761337,-1.939950,0.406301,-0.760443,3.109573,-4.035753,2.568915,-9.052612,-4.273365,6.233168,5.172611,6.644874,3.625476,1.664689,4.936485,0.211179,-9.760844,-4.624706,-8.414805,1.247210,9.184023,-4.544947,8.465032,-1.186157,7.786367,-6.671580,-8.097557,-4.378183,2.949837,-4.672171,2.759654,0.249680,9.593550,3.244729,-2.345461,-2.902306,-1.332049,6.880656,1.504041,8.024975,8.722885,9.737396,7.842894,0.694954,3.759263,7.181432,6.844816,-0.971784,-2.766725,-1.509467,6.217664,5.031402,-8.373218,1.543267,-0.410229,-8.804974,-7.516347,-4.384175,0.791852,5.497102,3.244514,4.736519,6.723059,8.906257,3.689693,-6.041790,-5.205494,-6.893353,-6.262959,-4.915647,-8.178703,-1.457032,-5.334477,-2.586098,6.204233,-4.138792,8.687956,4.538012,-9.092676,-8.930180,6.006210,-2.338333,-6.752956,-1.155962,-8.938352,-7.588932,3.580137,6.695268,3.714510,6.533138,1.913194,3.026144,5.406834,2.527987,1.778702,7.101931,4.812335,3.765728,-7.154310,-1.070675,-7.488791,3.023800,-5.422628,-2.178390,-9.658276,-0.693725,4.954444,-5.635924,-1.480896,-2.674407,-4.827681,-2.075047,9.625121,3.979660,7.452093,-9.184349,-7.373320,4.957772,2.142782,-5.525131,5.279397,1.549330,-2.903540,8.956996,-6.052468,7.034465,0.360973,-5.455641,6.428829,-8.251660,5.176200,-0.901047,-0.411291,-5.630761,5.067034,-1.736439,0.604055,-6.661746,5.024248,2.465424,6.945729,-6.749575,-3.867177,-6.244907,3.049652,6.538437,9.003271,-0.284713,6.105927,2.245608,-5.038581,-0.901071,-4.302572,3.006479,-0.784094,9.327349,8.275578,0.134742,-0.040872,2.359926,-0.099627,-6.039728,2.277039,-6.077504,-2.816091,3.107560,7.980521,-9.488669,-0.417095,4.398102,-8.087203,7.950802,5.672140,-4.314882,-2.879812,2.074772,-4.527843,-6.383250,-0.423094,-1.188560,2.889207,8.370746,8.351211,-1.452927,-2.777980,4.654747,-3.109448,-0.861412,6.597911,4.662585,7.637379,-1.708156,-3.659034,9.018044,3.291325,6.953978,9.823493,5.035316,2.773573,7.170328,-4.679653,-4.636221,9.089674,-6.518056,7.630242,-1.508978,-1.686569,-9.386562,0.428841,9.514063,-4.073498,6.591752,-5.526108,-4.885533,-8.390356,0.447003,-3.097328,5.695917,-5.757255,-6.629190,0.262306,-2.444038,-1.133470,7.181162,-5.083664,-6.380025,5.239863,2.950637,0.822033,7.711228,1.080025,-9.814381,8.620828,2.854129,7.153462,2.231521,-8.246151,-5.541948,1.388855,-5.300247,-4.881935,-4.854647,8.025549,6.850203,3.086454,-2.372481,2.200686,1.171924,2.605922,5.427140,-9.295087,3.451711,-7.797269,8.098074,3.352205,-7.793792,8.195195,-9.831298,-4.351360,5.986787,-6.604324,-0.857169,-3.761940,-4.075317,-2.203922,-9.505430,1.640303,0.468936,2.093177,4.570214,-9.037121,-0.115025,-9.320612,-6.167010,0.463325,-8.548172,-6.160931,6.832057,-7.632540,-2.266377,0.639440,-4.466992,-2.990526,2.877249,-3.268501,8.186403,-3.962583,-7.684702,-7.028979,6.528611,-0.918185,9.684151,-1.655449,3.896910,1.908073,4.700717,-6.764760,5.555696,5.014630,-4.696561,4.195703,-1.384941,-8.535137,-2.654192,-8.996066,-9.592341,4.983825,6.467136,-7.949955,7.735873,-9.025244,0.047594,-5.634902,2.772671,3.586004,2.030983,2.395506,-1.745233,9.352775,-6.783770,-0.257070,-6.625787,0.616596,4.557851,2.884977,7.524022,9.680809,-5.203968,7.642991,7.668872,-2.808337,1.543308,-9.035755,5.108308,-0.303518,3.904148,-0.544550,-4.742234,0.769109,9.143484,-8.364641,-7.971430,5.799082,3.510463,2.708228,5.080236,-8.921499,8.207369,-5.803758,-4.340642,2.265263,5.528042,4.105000,1.916371,6.796669,9.317273,1.753140,5.545338,7.405758,5.009939,8.969510,-5.994341,7.425879,9.749842,-0.639343,-5.706894,2.206522,4.928149,0.238895,-6.593235,2.926914,0.414055,1.811074,-8.640411,9.874388,7.234882,-0.478289,-1.895603,-5.039952,-3.624973,3.643475,-0.475811,-8.613061,-1.872753,-7.479401,5.761969,-5.106212,-1.432446,8.145201,-6.357992,-9.255323,-6.654438,7.381085,-3.694218,-2.743024,-4.258324,4.877562,-3.224082,-7.722684,0.049652,7.452929,1.102184,2.816993,-3.468429,-2.202471,-4.390123,-9.313357,5.289227,3.672366,6.973813,-5.194109,-6.305910,-4.447339,-6.284534,2.393071,5.144039,-5.881412,-5.546659,-8.279998,-8.399070,-7.481639,8.108977,1.225129,-7.752145,-1.549547,-4.690535,-0.161953,-0.108589,-1.951240,8.828903,5.712236,-1.253577,4.292256,0.494005,6.821857,-9.307729,-2.415030,5.758384,5.134621,3.520386,8.519996,-5.949136,-7.786405,8.776722,1.622710,-4.645018,6.474405,-0.395838,4.333775,5.435414,-4.258374,-2.054953,7.559225,-6.756544,-3.000061,3.226532,-6.527085,3.282053,-7.613057,7.859788,4.044869,-9.520089,-3.067954,-9.410351,2.837713,3.320849,0.816020,-2.561807,8.759340,7.758204,-9.953315,3.942518,8.308109,5.299863,6.889541,1.020322,-5.473013,-7.887383,4.752819,6.411925,-3.050600,-4.898581,-0.279035,-6.889223,5.197839,7.182852,-3.362801,-9.250929,7.888920,-9.949728,-5.209162,-2.088539,8.572086,-8.974242,1.327071,0.484838,-8.020487,4.830944,5.472589,-8.265834,-9.739499,-9.740128,-2.039342,-4.240656,5.987994,9.093367,-8.155992,-8.350290,-1.161380,-4.694233,-4.494056,7.107507,4.278256,-3.378088,-6.839269,-5.430996,-1.331576,-8.796321,8.984941,8.297038,1.671847,4.445592,-5.929965,4.184704,-0.303153,-9.570675,-4.172911,2.920146,-3.824688,-4.671938,-3.139631,2.113804,6.853003,0.659787,-3.707311,1.176764,9.040902,-0.849784,2.475754,-7.596030,8.563455,-6.577684,-0.727289,-0.944121,8.240841,-0.219061,0.110547,8.869626,8.761473,1.792834,7.397716,1.152703,9.666847,-6.932019,4.170606,-3.888892,1.463929,-9.076559,-7.837093,-3.490604,5.536895,0.945210,7.619978,-5.524707,-0.597403,-9.155143,-0.381202,-4.486630,4.103933,-0.494119,-4.087090,-2.496305,-8.011741,8.053724,8.090870,-0.941822,-5.163979,7.665133,-9.971478,-4.100389,7.304717,-0.302294,-8.076241,-9.303110,0.983518,5.486664,1.167223,1.627314,-9.305971,7.842480,8.629757,5.464017,2.834879,0.486638,-6.681068,-4.742364,-6.087655,9.528821,-8.665429,3.412052,1.527861,4.181580,-9.679152,-5.788995,3.302976,-7.359127,1.314901,5.246647,-5.166058,2.560224,-7.103767,-5.472073,-6.381764,-2.452816,2.946409,4.072736,-3.034389,-2.774085,7.914201,6.927770,-0.008704,6.074686,4.469943,-0.326804,6.690477,-6.803528,-8.148132,5.594268,0.438923,3.914163,4.453407,4.928933,4.252347,-4.866830,-6.401691,3.686252,6.230371,-0.251545,2.848033,-3.406843,-6.172444,9.967107,9.474856,-6.101993,-4.341419,-3.483096,-8.819967,6.652163,6.121743,-8.204123,6.156789,-7.941955,4.611023,-6.485388,2.950539,0.136640,9.083149,-4.014737,6.137073,9.846864,-4.038949,5.600507,4.029935,-6.920455,-5.825301,-9.692890,5.923411,-4.913367,-3.711848,6.066403,8.700809,9.395738,8.529804,-6.451430,-0.041150,-0.778668,9.728689,0.245070,-8.254423,4.104543,8.705464,9.818623,-1.258036,3.911991,-2.779498,-9.709116,8.491305,-8.015494,-3.994018,-5.151338,4.994895,5.065719,-4.746491,5.949254,8.150186,-2.981859,0.669061,4.216926,9.792511,-5.275017,8.771732,-0.889509,-5.972453,-6.997016,8.826841,-5.776633,6.334763,4.363172,-6.898549,3.642819,8.057564,-3.347388,8.238886,-7.302876,-4.723035,-6.262271,4.811587,7.998653,1.608069,-4.975112,-9.114314,4.590195,0.160401,1.575414,-0.433967,9.660385,-6.627859,-0.332618,5.172454,5.719064,7.641980,2.984279,-4.193379,-9.402239,-9.054986,-7.977775,1.166234,4.281526,-8.383807,0.508639,9.637015,-0.634203,-6.693307,3.758394,4.317317,-2.771979,-2.150451,6.205949,-5.460949,-1.230708,1.585218,6.333407,5.551657,2.086951,7.422727,-3.465014,5.908477,4.854944,0.905761,0.737968,1.324208,8.241566,4.755260,-9.193432,-8.857503,3.224336,9.270347,9.505264,6.228997,-3.419887,1.417037,2.863453,9.920117,-5.814839,1.614021,4.314268,2.993098,-4.909958,0.947802,-9.136854,9.676364,7.609150,-5.834404,1.885292,2.432516,7.587260,-4.974876,2.999462,3.723172,-0.428569,5.288927,8.369154,-8.479874,-1.675614,-0.011814,-3.164656,-2.395445,-2.184384,-6.885177,-5.361462,9.696783,-5.221698,-4.199948,5.919501,3.694981,-0.745993,4.475841,-0.859959,2.401945,1.644803,7.407378,5.183988,-7.560523,4.439641,-8.944459,-0.846039,1.326286,1.881862,4.482373,7.927343,3.575093,1.031361,9.114012,-2.499219,-0.929038,-8.905220,9.000028,1.450708,5.408390,-4.655155,-1.953204,1.975390,4.725503,6.578666,5.103528,-9.821743,-5.981635,2.184461,8.261345,-9.173363,1.259566,2.165801,2.475591,-8.325453,0.244829,-5.475309,-1.663204,6.384538,-8.515444,-6.944183,8.914095,-8.204841,-6.632344,3.751269,-0.554078,-8.727351,-5.547336,-7.150934,-5.013550,-4.853393,-0.722456,-4.960228,-4.332203,-8.364039,-9.179228,-5.596218,9.761002,-3.573757,-4.376703,8.486920,8.136207,5.962366,-6.582169,1.348765,-6.578069,-0.031051,-9.047007,2.714778,5.714998,-9.304860,-3.967226,5.512086,1.688641,-9.321246,-5.916754,-6.098499,3.064696,6.372336,-6.634638,-8.206726,7.566856,7.013053,0.058672,-1.884986,-5.737632,4.391155,-2.286643,7.589966,-7.775766,4.242961,6.018879,-4.059659,5.188812,-4.851115,2.136158,7.641237,-0.345474,-0.979333,3.763042,-8.722627,0.615753,5.346731,-3.778073,-4.894757,-7.775330,2.382807,8.939732,-3.661174,-9.563299,-2.574751,3.817614,-3.083193,-7.983367,-2.683075,0.658578,-3.774428,-5.269069,-5.119012,-8.270542,4.140979,9.169752,-6.981262,-0.718573,0.214928,-6.401578,-5.933078,3.613728,9.983477,-5.336491,-4.110587,-8.559508,-4.961564,-3.742210,7.323056,1.560228,3.868306,-8.156152,-4.543735,-6.052837,0.292858,6.183608,-6.433639,-5.016020,4.127410,6.472423,-6.996607,-7.308754,-7.422663,-1.593203,6.869466,-1.826373,-8.364125,-4.027790,-8.784562,-4.489889,3.941047,3.769871,8.871837,6.632516,-6.297059,-0.254961,-0.615751,-9.076227,2.110955,7.969540,-1.722516,0.221231,-0.157248,3.619143,-0.697398,-1.444983,-0.205664,9.907191,4.568463,-0.110468,-1.665163,-3.711805,2.751663,0.519355,0.292878,5.998536,2.840640,-2.465376,-0.322740,-8.335149,-7.196668,6.797929,-6.609301,-4.929690,1.799242,-6.494214,2.044580,4.075057,3.076438,0.968484,6.334697,-8.311278,3.291831,-0.947314,3.231230,-0.047075,7.303489,-3.420085,-0.055875,2.477756,8.674339,7.237921,-3.357311,7.386507,-3.958691,4.617953,8.765097,-7.595740,-5.159598,-6.050218,6.715640,1.372244,-2.664787,-5.803640,-9.514104,4.532008,7.499131,-7.425585,6.488116,6.789025,-4.750002,4.430160,8.319315,-4.920672,-4.069266,8.775756,8.645126,-4.246112,-4.385660,1.607122,-0.849643,-6.809848,2.191156,4.396278,-3.563866,-2.107510,9.080082,-3.424104,2.998085,5.608456,9.660894,8.446870,8.617229,0.189963,8.691852,1.469465,8.192306,6.949810,-1.938692,4.461306,-7.767398,-8.199124,7.664619,-5.555806,1.097938,-8.394268,-1.517302,-0.334739,8.909813,1.001239,-4.813933,-1.935514,-4.166415,-3.485540,-1.399077,9.091971,-8.795301,2.849241,-7.163226,-8.238680,1.395398,-8.706996,0.790938,3.382039,-3.705856,3.623174,5.442288,-8.314923,1.098336,6.086212,-4.959943,-1.395514,-8.970406,-0.053799,2.760761,-2.617563,1.223922,-4.612674,8.848981,0.750921,-0.719396,-4.489184,-8.121974,0.860444,-7.066184,-6.753341,2.438822,8.242818,-8.206681,-1.879842,-2.905953,-3.668527,-8.800555,-4.200169,-3.937945,3.782192,-9.517946,1.048115,2.910346,3.128497,7.628205,-5.347800,-6.961820,-1.531541,-9.633997,6.634688,3.076459,-0.141956,-2.473469,-0.619363,5.184419,-1.096478,3.936773,-2.890669,-1.695546,-5.663862,0.845246,9.920312,-2.418541,-3.163881,-0.196419,-2.130080,4.822960,9.018769,0.548325,2.256021,-4.963770,0.470137,1.562547,-4.402048,0.719622,5.965152,3.658316,-7.638517,-2.831167,-5.221570,-7.039295,-0.502662,-2.244966,-0.727965,8.581122,-9.511462,0.728902,-6.286959,6.141817,-7.272028,4.832839,-5.491830,-0.847543,2.187032,7.944656,-1.962463,-1.726539,-5.694354,-5.476010,-9.437921,-6.345733,3.472743,-3.612186,-9.675749,-3.656804,-6.742212,-1.724228,0.578929,-2.276845,2.312872,-3.976250,5.988883,-9.854732,8.888648,-2.516307,9.041583,-8.316735,-1.695779,-9.831083,0.617185,-4.802048,-0.068242,-8.951935,6.748286,-7.844926,-8.148102,-7.953355,7.269186,0.168665,-6.646022,5.755063,-6.795012,-8.341119,-1.569905,5.374219,-4.009051,-4.634099,-5.032256,-4.367200,4.947203,-6.350247,6.094756,6.797097,-0.074936,-4.818882,2.202896,-7.687406,6.568896,-2.014377,9.051225,3.236408,3.447903,-8.787117,-0.757234,-5.426804,-4.894012,-5.143230,2.334992,-4.350215,-6.930954,-5.764671,-6.553028,-5.737863,-4.680363,-4.427318,-1.256788,6.426875,2.557525,-8.256607,-5.846419,6.544941,8.593657,-6.478594,0.321989,-2.499093,0.776885,7.104143,0.851619,-9.574537,2.718814,0.308862,-3.039417,7.237275,9.926620,-5.705659,-0.054937,-2.214776,3.731112,4.522621,6.487727,-5.578601,-9.333697,7.201721,2.008083,3.135582,-8.844971,7.188364,9.201196,-2.999600,-8.965447,-5.718899,-0.136968,-5.009603,-0.115337,-5.517327,-3.223119,-2.862701,3.069047,-8.076088,6.879778,6.562578,2.258820,2.243159,3.125251,1.986490,-8.409946,9.601705,-1.436289,-4.536009,5.847441,-9.325922,3.676168,-7.193929,-3.482197,-3.758597,0.912364,2.347756,-5.628777,8.425520,-7.333316,7.928694,2.144593,7.786872,-6.952518,-0.002893,6.912022,4.495299,5.222187,7.535341,7.525710,-2.289295,3.864219,8.338484,-7.636322,3.198051,1.380935,2.441299,4.272252,-3.578460,-0.191945,4.287141,0.896059,-6.397583,4.552600,9.010346,7.021346,3.227978,4.887079,-2.205094,4.727673,2.898244,-2.154491,1.622357,1.187454,-2.311094,-5.906059,8.428939,-3.956415,7.516105,8.136828,-3.204124,-1.828164,3.915387,-9.991141,3.929027,-0.530936,-3.400779,8.060824,-8.071051,5.445458,-6.201171,3.279269,-3.979279,8.463810,8.179298,-6.411765,-1.877771,5.805269,-8.739264,9.400264,6.506908,-2.199841,3.092352,-8.062097,5.514626,-0.154406,4.256830,9.789647,4.150069,5.747801,-4.229911,7.823889,-8.204401,-7.278857,-0.474938,-7.293779,2.904205,-3.262572,-5.367903,7.847485,-0.130818,3.259387,5.004945,9.288339,-1.576002,0.363010,-7.281145,2.007878,2.569210,-4.469374,3.605541,6.172064,4.514836,9.667756,-7.907879,7.989004,-6.878539,4.941357,-0.106829,7.129796,5.940587,8.715746,4.956911,3.714943,-5.841208,-6.252948,-5.470296,1.771687,8.262005,-3.734374,5.958622,3.260005,-0.413481,0.870338,0.710260,6.641420,0.732242,9.812528,3.404154,3.556279,-2.131504,-3.963962,1.959157,-6.376864,-6.481416,3.528301,5.211770,-5.167108,9.090574,-8.015824,-6.299255,8.413863,-3.041391,-3.888218,0.123549,3.529102,6.945442,7.301995,6.190188,-3.236352,-3.748386,4.787829,-2.236382,6.081413,7.338087,-7.567102,-9.337164,8.747963,-0.062866,-8.543317,9.426404,8.941923,4.389939,-2.270861,9.172089,5.076584,-6.548325,9.175544,-4.619260,-4.297252,-6.408399,4.036253,-4.524902,5.509893,-6.071345,6.420311,8.819895,-6.194473,9.339643,-4.466119,6.923950,-0.406553,-4.766608,-7.045814,-0.517486,5.725330,-3.541524,2.046014,4.929755,3.864125,4.664552,-5.770927,-5.204503,4.056064,7.714650,-4.253225,6.791731,-9.268538,-6.231654,-5.748362,8.537248,1.371459,-9.799457,-2.029737,2.445663,2.317923,-0.090323,6.676929,7.597273,-0.229904,-7.769773,7.169691,9.223009,-1.941541,6.912849,4.284966,-2.954147,-2.372235,3.360563,-6.341051,-6.928190,5.533528,0.738206,6.315753,-7.224015,9.143913,-2.562511,-3.232154,-2.554063,0.400799,-7.750216,-8.307442,5.589796,9.414013,-7.712041,3.634615,-1.146794,8.288474,-0.430390,-1.556139,5.863063,8.160968,-1.420672,8.344673,-0.732374,-5.372085,6.767203,9.724069,5.872324,-4.573717,0.982184,2.809501,-4.677474,4.243086,4.891782,1.063742,-3.222578,1.706138,5.474026,9.997310,5.594698,-4.922748,7.931978,-9.440813,-2.468369,-6.481007,-3.879066,0.476719,-5.290187,9.194891,-5.543325,-9.729073,-2.665062,-4.971738,3.571252,8.397388,9.178956,0.188122,-9.288311,-1.289357,-6.883954,-2.987524,-4.696395,-5.523968,-6.934179,-6.962147,-5.489810,0.445530,-2.573431,-2.227771,-2.922267,3.111315,7.041605,-0.625931,-6.256537,4.100649,2.218093,5.822905,5.390815,-5.847042,-4.311809,6.290640,-0.908038,2.797643,-1.957513,-9.100397,5.093012,-8.388377,-0.075739,-6.699509,8.518868,-2.406030,9.777533,-8.423492,7.572051,8.174557,-1.270636,-4.725688,9.133278,2.590148,-5.258426,-5.101658,0.744760,-9.732844,7.142615,-4.253237,-5.176002,3.900749,8.552542,3.179680,0.440933,-5.814118,9.962277,-5.199931,-4.955186,-5.030730,0.815371,-1.160968,3.510016,-2.763560,-1.866388,-8.392545,8.477839,-6.603392,1.358749,5.393297,-1.652530,-4.981251,8.583391,7.399444,6.296399,-5.629022,-3.872029,3.563834,0.782512,6.825718,9.268145,9.671895,3.547099,9.741067,7.282204,0.819811,-6.773037,7.464245,-4.974627,0.436129,-7.074753,-8.839378,-9.477073,-9.973997,-2.391392,1.464673,7.118923,-7.428691,1.705250,-8.998227,6.969211,-0.349942,2.436138,0.712245,-0.287405,6.391132,-4.166899,-9.738813,-3.742165,-4.601566,-7.731449,-0.628889,-8.712102,-3.308736,-0.664394,-0.167091,7.691762,8.556845,-4.282931,-8.045914,1.236766,2.151283,-1.684689,-7.557342,5.372262,1.020371,4.190271,3.947358,-3.300661,2.500767,-0.564116,-5.121248,-3.721025,5.273211,-9.580254,-4.200658,1.785999,0.858078,1.465347,-4.477769,3.989574,-2.004063,4.745755,-6.552187,9.267280,-5.742686,-3.216196,3.023848,-2.196537,3.209836,6.134229,-0.387954,-9.038019,-2.778565,-6.662304,-1.427854,-5.698605,-9.567776,-2.848979,1.011137,-3.429498,-9.473622,0.339957,7.821905,-6.274486,-3.007189,-0.889279,-6.274929,6.871308,-6.596196,-9.429367,8.529426,0.425520,-9.755577,-3.441112,-7.425978,-7.921987,2.220201,-4.890604,1.531021,-0.100561,-1.217716,4.939209,8.581262,0.411068,-7.612157,-4.976032,-9.658358,6.611267,1.842062,4.937934,-6.045059,-4.420943,1.180117,-9.202336,1.655742,-7.926920,-8.630946,4.242376,-8.545673,8.858362,-7.020850,-4.390525,-6.931989,8.042511,-4.760637,9.126890,-5.566564,-4.368990,-8.498334,1.430827,2.893942,-7.599275,7.763062,2.387504,-3.400709,-8.350526,-3.073844,-4.629511,-9.797002,1.642515,-2.662495,2.210115,-2.910119,-2.835227,-5.832133,9.777258,8.876438,1.439771,3.252599,3.295971,-5.351851,-0.885554,-0.815252,5.863793,-4.666622,5.502896,1.756146,-7.243750,3.161928,-4.140832,-2.325722,0.559442,8.283147,-3.434712,-2.524637,1.611880,8.455671,9.993294,-9.130982,-3.543735,1.046362,9.791815,-0.105200,9.041828,-5.343133,5.152051,2.751795,-7.847160,-0.974202,7.230564,-1.914761,9.294120,-2.736788,-0.524198,9.760265,8.211176,-6.849356,0.267295,-7.178175,-7.517275,-2.486710,2.875755,1.649359,1.093504,-3.449911,-2.584058,8.565875,-8.564126,-9.974067,-2.547794,4.676394,3.611890,-3.495983,-4.425330,7.083834,0.800692,1.250648,5.252738,-7.439428,-4.818510,3.807482,-1.008005,-4.566704,-2.072278,0.792577,-8.001942,-1.573733,-7.769693,-3.761373,-6.080559,-2.583364,9.257683,-2.741552,-1.297964,8.189644,-4.481746,7.173036,1.064616,7.496751,-1.599836,-6.727236,-0.816418,-4.026550,8.797590,2.783268,-1.052457,3.821409,3.545360,-2.405289,2.005104,-6.627612,-4.295063,-4.439788,6.602144,6.264430,-2.089381,-8.843097,2.296518,9.642300,4.019720,-7.377156,-4.244798,-7.632600,7.061776,5.040013,-3.985942,-3.486559,5.506758,2.408504,7.664063,6.623875,-0.099164,-7.575281,-3.873851,8.811507,-3.929896,-1.973444,5.167210,7.221876,7.811149,4.031998,-5.184439,1.557456,-4.223753,0.914803,5.539541,9.432649,-8.374016,0.427489,-3.293818,2.921477,-1.146346,4.946562,-1.857406,6.336615,-6.397025,5.224208,-0.708912,-9.254889,7.602460,-9.469937,-2.927003,2.575367,2.622126,-3.992511,6.077995,3.140635,8.625682,8.448558,2.349186,3.828594,-4.070533,-7.315305,9.376674,4.019133,-5.084955,-4.810502,-4.254522,-9.083810,-6.580826,3.390882,-9.556075,-2.493126,0.861836,9.391304,-2.184523,-9.058143,2.093835,9.094405,-3.663045,-4.150192,1.501367,6.576243,-6.221291,6.071675,-8.545814,-1.063629,8.349722,-6.260037,-0.986276,9.521524,7.697598,7.227104,0.674011,6.033434,-5.208347,-2.651224,-3.966046,7.692749,2.924843,-5.085070,2.999862,-8.851408,0.747797,5.444902,-3.899300,-6.314642,6.085449,9.900616,-7.045859,-4.457460,-6.490394,-3.954882,-1.526612,0.498709,6.643295,-8.004873,-2.678268,6.386916,7.697456,6.886055,-4.827756,0.281400,-5.798452,-4.636519,-3.608653,4.151887,8.066464,1.714367,6.856611,-7.434931,-7.105305,2.691441,3.223324,-7.994256,2.679916,6.000999], dtype = "float64")#candidate|9580|(3360,)|const|float64
const_9581 = relay.const([8.669467,9.430254,-2.817628,-4.751083,-0.940818,-4.107476,-8.898019,-8.298661,7.313977,5.444666,6.885331,8.705258,9.993754,-3.263572,-0.854054,-6.079204,8.177301,8.227985,-9.781316,8.974747,1.652955,-5.236629,-9.043575,2.548405,-0.616837,4.599219,-8.392492,9.588936,1.211430,2.548343,5.942424,1.322984,7.416378,1.380640,-5.546813,-1.744394,-5.430475,3.510536,-6.489810,-3.374911,9.639907,-7.330540,-7.544398,0.785281,3.411050,4.065126,7.310137,6.163156,9.741966,-1.720045,9.528331,-3.490870,-1.770912,7.538418,-6.395283,3.088028,4.337718,5.896223,2.627204,0.435502,4.633289,-6.989282,2.614695,5.660126,-1.014712,-1.924767,6.030195,1.006119,-1.718379,-1.026220,-2.127115,-8.460418,8.996927,4.315610,-2.914503,2.021483,-2.680040,-6.318877,6.130416,-0.013798,-4.062917,8.307554,7.241326,8.199572,1.801599,-1.312162,5.763824,5.813488,8.389737,-8.739614,7.066930,7.468355,8.533367,2.539944,-0.158166,-9.370191,-8.683556,-3.728553,-0.307288,5.273094,0.855719,3.468641,-6.135824,1.153325,1.482083,-3.314952,8.395448,-9.440773,0.184524,5.150087,-2.417832,-3.059667,0.853476,-3.386413,-3.872815,-7.129305,-5.740286,1.734823,-9.972558,-3.544657,-6.311698,3.363927,-0.256236,-6.688800,7.131085,6.877714,9.117218,6.233977,-0.525944,-9.010261,2.339190,-0.979767,-9.844765,8.178982,-0.112405,-5.516157,-0.557597,-0.006212,-6.104722,-3.818859,-2.072298,7.149835,-4.051553,1.191242,-1.785851,1.185011,-8.630459,5.985550,4.604563,2.365415,-8.970943,-3.332426,5.801771,-0.591366,3.207426,-9.934802,-5.954747,4.313311,-9.051269,-9.368239,-6.015005,-9.207467,6.646796,2.465040,-3.617145,5.008231,3.204064,0.995974,-3.109464,-5.517167,6.034054,-1.502951,-5.555317,-9.462401,-4.461453,5.978062,-9.721293,0.349702,-5.836329,3.910423,7.353413,7.079883,-7.978532,-0.900953,-8.503423,5.686136,7.117869,-1.158099,6.623158,-8.234600,9.063791,0.434699,8.739928,4.740202,6.624129,4.019880,9.022199,8.167728,5.007014,6.357177,-4.899495,5.727741,-9.414379,0.038032,-2.433527,4.333735,-2.399732,-5.576338,4.896205,2.124783,-5.545253,2.932563,2.360806,6.543708,-4.617877,1.348761,8.537324,-3.787464,-9.032217,-5.291456,7.962245,-8.546434,-0.501255,-3.820887,-6.851230,-4.570494,-6.097376,7.891187,8.720105,-9.336055,6.862306,-7.846051,9.047874,-2.015436,8.445971,-1.009705,-3.298310,-9.162337,8.096113,-0.708619,-4.642058,-4.380719,-5.675721,-3.856361,5.006365,-6.309122,-0.226047,8.311662,7.552574,6.915155,-0.072321,-3.088022,-5.427614,2.975947,2.667404,-8.299116,9.587472,-0.303975,-3.937765,9.018263,6.619941,-7.083751,-2.345185,4.211925,5.539446,-4.494271,7.915222,-3.290647,4.342196,3.756976,8.958160,-4.444219,0.834929,-3.117172,-6.263488,7.159399,9.957512,4.657709,1.639915,-3.456448,-2.020186,3.990560,5.837716,5.214636,0.799316,8.324035,-4.160073,6.905018,-5.736797,8.961653,0.233857,-2.801252,-0.782308,7.933094,8.554212,-9.530175,-1.883901,0.147234,8.064411,0.462102,3.332328,0.102667,-0.127473,7.770149,1.133795,1.179346,9.792131,1.524023,-1.557140,-9.991795,-9.182441,5.810859,-2.769556,-8.379488,9.176862,-9.375654,-0.454348,7.908886,5.648554,1.923442,2.850423,7.246207,6.397194,0.702867,4.191536,9.781947,-7.889934,4.644484,6.165658,8.142201,5.884321,5.679398,8.220949,-7.197185,-6.933625,0.685789,2.252017,-2.529193,-4.616842,-1.364405,2.318910,6.496756,-2.375058,-4.739481,7.225817,-1.295445,-8.139243,-4.370763,-5.740343,-3.035889,9.132866,4.445356,-1.538650,4.912316,3.189575,8.745532,8.366072,-1.941019,8.329230,6.745625,-0.579895,2.251641,4.127624,1.817257,-6.632377,-0.433166,3.020333,-7.492100,-2.030394,-2.992092,2.936406,-3.625460,9.783942,-7.969622,-6.898804,7.071046,-8.286374,5.580118,-5.389685,8.313562,-0.775314,-7.368041,5.757253,2.864345,-2.454018,7.406282,5.136418,-4.673022,2.620477,8.298962,-8.114919,-9.758275,4.961555,9.202328,-6.289655,0.913953,-2.734133,7.513497,-8.733530,1.554432,-7.262526,9.661669,6.838743,-1.351285,-9.728319,-7.275240,-1.984279,7.445785,-6.121864,-4.500472,-6.309323,4.263806,8.863005,-6.533980,5.734930,8.895568,7.322597,-5.067524,-2.105145,9.505086,-2.749400,-4.241601,-5.369371,3.726524,-2.451041,-2.791774,2.987205,8.156592,-1.921886,-3.433449,-4.278312,1.646249,-0.779028,-1.369349,3.414770,-8.333607,0.393897,-8.474048,-7.478725,-3.167854,8.714757,4.480266,-9.970281,-8.276961,8.296212,-0.565512,-9.137648,7.548474,4.524164,8.393014,9.144670,7.192752,-6.800929,-6.901023,2.904967,6.360175,0.515006,4.699436,-5.455275,-4.240967,-4.392194,7.765110,1.794294,-2.446820,-7.196892,4.561963,1.241053,-7.892944,-2.498068,-7.960013,0.501054,1.385306,4.622669,-4.249618,-6.954735,4.283008,1.345962,8.092900,0.869373,-2.140646,8.141760,1.670915,-8.817424,4.785138,-5.588863,-4.966589,3.814803,3.155640,-1.579561,-6.864068,-5.176670,9.495487,-0.605324,-7.498298,-0.335114,8.968058,-4.170628,-3.449650,-5.359481,-7.576757,-1.346005,-2.911965,-0.611519,-9.006422,5.104386,2.513099,-4.985044,-7.975414,8.821487,-9.531206,3.650895,3.607377,-9.504267,-1.819483,6.373032,8.454222,1.239071,-0.741333,2.594058,-5.281245,7.192030,4.531393,-6.202445,5.831359,-9.661131,-1.174388,0.988516,-2.230233,1.904648,2.314232,9.167454,-6.120114,-0.596969,-9.383368,2.773279,8.450854,-3.318875,-5.769389,-0.920202,-4.185574,1.618840,-2.784391,-3.689782,-5.649875,7.016715,4.750240], dtype = "float32")#candidate|9581|(546,)|const|float32
const_9582 = relay.const([-0.291019,3.739491,-5.241308,-3.157590,5.896786,4.997721,-8.889050,1.145265,-3.280436,2.268212,-8.205917,1.752362,9.106285,-4.274558,-6.118817,-6.046445,1.060656,5.331806,-6.245086,-6.973137,-2.218529,9.341108,7.490403,9.551972,-6.055014,-2.270745,-8.854170,-9.796485,-5.442670,-8.307197,-6.150588,5.115880,7.553354,3.134172,2.090267,1.460879,-9.386777,-7.404740,6.765885,9.990994,-3.938013,-6.649320,7.216587,-2.647321,7.935216,6.982900,-5.785184,9.256789,6.118320,6.658383,-4.658265,-3.574992,-9.301197,-9.912974,-1.867234,9.695344,-9.415604,-8.874299,2.601639,7.728095,9.510711,-1.722764,-0.659182,6.052931,6.587430,-7.074938,-6.916299,-1.806503,5.936609,-3.965562,-5.007567,3.253256,-5.461245,3.384868,-2.434070,-8.458152,7.246458,2.521187,7.808505,4.871746,-9.878136,-1.106061,-7.428157,5.529662,-5.135515,-4.389274,6.014628,2.678519,4.617450,8.790869,5.929399,2.929937,4.818077,-1.469395,-1.944556,1.122051], dtype = "float64")#candidate|9582|(96,)|const|float64
call_9579 = relay.TupleGetItem(func_4779_call(relay.reshape(const_9580.astype('float64'), [2, 1680]), relay.reshape(const_9581.astype('float32'), [546,]), relay.reshape(const_9582.astype('float64'), [96,]), ), 3)
call_9583 = relay.TupleGetItem(func_4784_call(relay.reshape(const_9580.astype('float64'), [2, 1680]), relay.reshape(const_9581.astype('float32'), [546,]), relay.reshape(const_9582.astype('float64'), [96,]), ), 3)
output = relay.Tuple([call_9559,call_9574,call_9579,const_9580,const_9581,const_9582,])
output2 = relay.Tuple([call_9560,call_9575,call_9583,const_9580,const_9581,const_9582,])
func_9585 = relay.Function([], output)
mod['func_9585'] = func_9585
mod = relay.transform.InferType()(mod)
mutated_mod['func_9585'] = func_9585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9585_call = mutated_mod.get_global_var('func_9585')
call_9586 = func_9585_call()
output = call_9586
func_9587 = relay.Function([], output)
mutated_mod['func_9587'] = func_9587
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9591 = relay.var("var_9591", dtype = "float64", shape = (3, 9, 11))#candidate|9591|(3, 9, 11)|var|float64
var_9592 = relay.var("var_9592", dtype = "float64", shape = (3, 9, 11))#candidate|9592|(3, 9, 11)|var|float64
bop_9593 = relay.divide(var_9591.astype('float64'), relay.reshape(var_9592.astype('float64'), relay.shape_of(var_9591))) # shape=(3, 9, 11)
func_6714_call = mod.get_global_var('func_6714')
func_6716_call = mutated_mod.get_global_var('func_6716')
call_9599 = func_6714_call()
call_9600 = func_6714_call()
uop_9606 = relay.rsqrt(bop_9593.astype('float32')) # shape=(3, 9, 11)
output = relay.Tuple([call_9599,uop_9606,])
output2 = relay.Tuple([call_9600,uop_9606,])
func_9621 = relay.Function([var_9591,var_9592,], output)
mod['func_9621'] = func_9621
mod = relay.transform.InferType()(mod)
mutated_mod['func_9621'] = func_9621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9621_call = mutated_mod.get_global_var('func_9621')
var_9623 = relay.var("var_9623", dtype = "float64", shape = (3, 9, 11))#candidate|9623|(3, 9, 11)|var|float64
var_9624 = relay.var("var_9624", dtype = "float64", shape = (3, 9, 11))#candidate|9624|(3, 9, 11)|var|float64
call_9622 = func_9621_call(var_9623,var_9624,)
output = call_9622
func_9625 = relay.Function([var_9623,var_9624,], output)
mutated_mod['func_9625'] = func_9625
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9660 = relay.const([[[6.011264,9.043449,-5.818042,-9.356685,3.427509,6.660695,5.708030,7.267953,-9.007520,-5.437932,4.873841,2.845495],[3.160563,-6.440953,-1.392384,-5.987171,0.150060,-5.559876,9.138539,8.202125,-5.441195,3.103369,-2.121036,4.727808],[3.189890,4.666992,-5.740612,-4.905039,9.704629,0.163321,-4.286295,3.325856,-1.399551,-3.883799,-6.442388,-5.651881]],[[-7.916948,8.438757,-2.176180,0.781563,-9.172743,-9.314673,-2.706845,-8.108910,8.275626,6.533040,6.901010,-1.577254],[-7.314309,-0.638962,-7.148795,-0.482980,-1.579137,-3.510024,-2.752188,-7.187086,-2.571303,-8.801283,-6.201268,-9.107756],[-7.296830,9.400573,-2.490248,2.739496,-9.724041,-2.147821,-5.917043,-2.699124,-9.158191,6.599971,-6.932430,1.572331]],[[-5.957635,1.176854,-4.092125,6.327991,-2.309640,6.257414,-2.405476,5.031261,-0.401759,8.999692,-2.759212,3.065294],[-7.035746,-9.807688,9.239143,3.902823,1.359272,-1.796084,-3.835143,-0.603953,-8.615235,-1.478983,4.615918,-8.461337],[6.712358,-1.339380,2.001117,-3.258503,5.194372,-9.247858,-0.687871,-5.185044,9.023192,1.499517,-8.016469,-5.623665]],[[9.274154,8.045826,-9.735536,-8.362492,-8.914408,-2.337491,0.995453,3.524928,0.094123,4.978505,-5.068838,6.336910],[-5.476931,8.776501,-0.522055,0.627515,-3.442513,-9.039298,-6.830506,-2.271768,-5.694537,-4.226519,9.946748,-5.976136],[-9.592666,-2.997921,3.249812,-2.198829,7.850834,9.549076,0.896774,5.574276,2.827598,-7.371478,6.788394,-0.308653]],[[6.724153,3.907661,9.272507,3.165018,0.100737,-2.766869,5.826236,-8.169479,-2.497958,4.235617,-8.143908,-3.918930],[-3.160636,-7.691327,5.506665,1.739361,1.295522,-4.769875,-1.321097,-0.327943,6.084961,1.260928,8.168354,6.088098],[5.658417,2.011884,-2.139390,6.614337,3.633521,-5.978128,6.530763,1.406548,-1.619963,8.258743,-9.982274,-7.300586]],[[-3.023351,-4.154895,9.039695,2.393704,-4.248555,-3.487432,-6.296655,-0.911419,5.692762,0.346673,-4.353412,-9.908353],[-5.454534,-2.195944,3.147426,-6.655692,-6.452646,-0.184307,0.445186,-3.322880,-6.735740,-3.263068,-6.212884,-8.826575],[4.018253,-2.378335,7.811249,-9.520456,-6.835462,-2.982570,8.851713,9.171371,1.269113,8.362530,-4.561504,5.055361]],[[-9.256119,0.489078,-9.336723,2.025133,9.286128,5.500290,-8.767243,-5.183883,-1.975395,-8.770662,-8.450270,1.815967],[0.748418,-4.107540,-8.622545,0.776576,6.632870,-4.790790,-7.515620,2.404607,1.295116,-8.738379,-0.500108,0.023321],[3.056610,-6.217572,2.300978,-3.762805,-3.015213,-1.124754,-4.352236,8.494398,5.335597,6.628190,9.119177,5.112461]],[[1.208375,-8.009552,6.073544,3.604446,-0.119138,-9.959799,6.571364,-6.385187,5.587302,9.983683,-6.187814,2.546929],[-7.491771,-4.855008,3.114569,-5.774975,1.513013,-5.097203,-8.223868,-1.182036,2.244325,7.592913,9.778751,-4.432535],[-2.304802,-4.345218,-6.259746,-6.542490,-4.484049,0.147231,3.548954,-9.705333,-0.282994,0.247814,-0.302684,0.575024]],[[-8.331676,3.832209,1.702926,-6.200603,2.762139,-1.714958,-2.014790,-8.868853,7.295957,-3.992494,7.651162,-7.294753],[0.250162,5.573128,3.177824,4.572837,3.257359,1.644212,-9.260511,-6.539565,-5.071170,5.357709,-5.864302,2.144307],[5.124005,-5.344573,-6.828142,5.238224,-0.889652,-8.452324,9.418811,4.954205,-4.020130,8.684541,-8.710730,-6.679096]],[[8.862728,1.245661,3.303547,3.633592,-6.062897,7.954023,-4.774951,-2.329265,2.539701,-1.947723,-4.233840,3.191376],[-6.410619,0.982859,8.112861,5.645248,5.364335,-1.162825,5.741996,-1.213795,9.082921,6.052157,-5.966205,-7.307165],[-7.078295,-7.061055,-4.966011,7.459586,4.047050,2.571579,-6.871610,1.782786,4.169361,-8.698157,5.957931,-3.691535]],[[-0.991996,1.752622,2.735492,1.847331,-2.690356,-1.633897,6.215816,-8.284266,-7.607009,8.993578,-0.253901,-3.182303],[-9.537321,3.016429,4.784266,-8.721488,4.267067,-2.851543,5.307729,-9.115900,-6.838642,-0.474854,-4.352339,-0.412021],[-3.143940,9.761404,-0.282253,-8.499605,-7.275808,-4.495187,3.964586,1.421456,-5.190777,6.063409,9.508072,-7.862618]],[[-0.071417,-0.794861,0.663787,1.021039,-6.221917,-6.087934,0.071785,-0.842030,-3.598964,6.283717,7.923706,-9.511010],[1.464955,-0.837434,0.028178,-5.364763,8.292871,-2.903095,9.225955,0.896463,-0.064857,-7.696138,-3.194316,8.033650],[9.522495,2.050538,-0.080196,6.075530,2.496024,-4.999105,-6.763303,1.781683,9.307712,-1.533106,4.827947,9.023366]],[[5.036749,0.940872,-2.717691,9.028552,-7.066828,-9.951843,-3.035913,-3.791058,8.018880,2.550764,7.071823,-1.281977],[-4.929892,3.521061,-5.379830,-1.393633,-6.513574,6.652306,-9.160786,-1.182750,9.828178,0.174627,-7.631382,-2.094818],[4.302567,2.894244,-8.591260,0.813168,-4.880138,-2.510542,9.804991,6.500211,1.398279,-4.645902,9.775881,-1.924925]],[[-1.731745,-9.582010,8.634363,-7.271535,-0.350970,7.000511,8.349184,-9.163046,5.412634,-1.689290,9.108530,-8.569619],[6.231568,-8.735181,5.026413,5.560487,8.130272,4.114269,-8.357934,4.876585,5.782089,7.478817,9.373820,7.386850],[8.011965,-3.215743,4.887075,8.333029,0.678518,5.485968,-1.052033,-7.400627,-9.639430,-3.656641,-8.245079,-6.378596]],[[-6.769812,-6.720140,4.941586,-8.054823,-7.597835,6.177325,4.289112,-0.222879,-1.011293,5.619326,-2.650405,-6.636807],[9.703475,-2.571750,-3.556368,-2.462454,-6.769112,3.087993,-3.213969,-5.996938,-3.874706,-0.492498,-0.115279,-1.390590],[-5.187954,2.487332,-5.378405,2.669889,-6.397973,4.067638,-0.644761,7.936086,-6.579678,-5.853710,-0.473987,5.453647]],[[-1.816855,-6.485683,-2.069949,-8.076005,1.796571,-9.443504,1.386233,6.753537,1.634767,6.649351,-6.286615,-1.478699],[7.701918,2.009204,-8.925883,-4.449327,-1.238153,4.103770,4.628792,5.736599,-3.711007,-5.972817,-2.370525,3.035082],[-8.593387,7.501600,-2.002143,-8.608857,5.908637,3.954994,-0.338489,-8.300016,0.278745,-4.690319,6.205812,1.140734]]], dtype = "float64")#candidate|9660|(16, 3, 12)|const|float64
uop_9661 = relay.atan(const_9660.astype('float64')) # shape=(16, 3, 12)
uop_9663 = relay.sinh(uop_9661.astype('float64')) # shape=(16, 3, 12)
func_5340_call = mod.get_global_var('func_5340')
func_5341_call = mutated_mod.get_global_var('func_5341')
call_9665 = relay.TupleGetItem(func_5340_call(), 0)
call_9666 = relay.TupleGetItem(func_5341_call(), 0)
func_6775_call = mod.get_global_var('func_6775')
func_6778_call = mutated_mod.get_global_var('func_6778')
var_9668 = relay.var("var_9668", dtype = "float64", shape = (378,))#candidate|9668|(378,)|var|float64
call_9667 = relay.TupleGetItem(func_6775_call(relay.reshape(var_9668.astype('float64'), [9, 14, 3])), 0)
call_9669 = relay.TupleGetItem(func_6778_call(relay.reshape(var_9668.astype('float64'), [9, 14, 3])), 0)
func_9437_call = mod.get_global_var('func_9437')
func_9439_call = mutated_mod.get_global_var('func_9439')
call_9670 = func_9437_call()
call_9671 = func_9437_call()
func_4407_call = mod.get_global_var('func_4407')
func_4408_call = mutated_mod.get_global_var('func_4408')
call_9675 = relay.TupleGetItem(func_4407_call(), 0)
call_9676 = relay.TupleGetItem(func_4408_call(), 0)
func_5608_call = mod.get_global_var('func_5608')
func_5609_call = mutated_mod.get_global_var('func_5609')
call_9694 = relay.TupleGetItem(func_5608_call(), 0)
call_9695 = relay.TupleGetItem(func_5609_call(), 0)
uop_9703 = relay.sin(uop_9663.astype('float32')) # shape=(16, 3, 12)
bop_9705 = relay.greater(uop_9663.astype('bool'), relay.reshape(uop_9703.astype('bool'), relay.shape_of(uop_9663))) # shape=(16, 3, 12)
output = relay.Tuple([call_9665,call_9667,var_9668,call_9670,call_9675,call_9694,bop_9705,])
output2 = relay.Tuple([call_9666,call_9669,var_9668,call_9671,call_9676,call_9695,bop_9705,])
func_9719 = relay.Function([var_9668,], output)
mod['func_9719'] = func_9719
mod = relay.transform.InferType()(mod)
mutated_mod['func_9719'] = func_9719
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9720 = relay.var("var_9720", dtype = "float64", shape = (378,))#candidate|9720|(378,)|var|float64
func_9719_call = mutated_mod.get_global_var('func_9719')
call_9721 = func_9719_call(var_9720)
output = call_9721
func_9722 = relay.Function([var_9720], output)
mutated_mod['func_9722'] = func_9722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3811_call = mutated_mod.get_global_var('func_3811')
call_9748 = func_3809_call()
call_9749 = func_3809_call()
output = relay.Tuple([call_9748,])
output2 = relay.Tuple([call_9749,])
func_9759 = relay.Function([], output)
mod['func_9759'] = func_9759
mod = relay.transform.InferType()(mod)
mutated_mod['func_9759'] = func_9759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9759_call = mutated_mod.get_global_var('func_9759')
call_9760 = func_9759_call()
output = call_9760
func_9761 = relay.Function([], output)
mutated_mod['func_9761'] = func_9761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5177_call = mod.get_global_var('func_5177')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_9801 = relay.TupleGetItem(func_5177_call(), 6)
call_9802 = relay.TupleGetItem(func_5178_call(), 6)
func_9719_call = mod.get_global_var('func_9719')
func_9722_call = mutated_mod.get_global_var('func_9722')
const_9804 = relay.const([-6.514262,9.145364,3.706243,7.810812,-6.685376,-1.635145,-4.204543,1.005462,2.867413,2.170878,1.518204,-8.879934,0.860333,9.779188,8.153571,-4.205860,7.825555,-5.835639,-3.987718,2.750578,7.904390,3.963675,2.066079,2.530280,-4.718538,3.675191,4.370022,-6.762031,-5.447752,-7.671292,-9.926939,5.032694,-7.306021,-0.135514,-1.492424,3.589364,4.075930,5.721330,4.569756,2.647249,-1.880662,9.749688,2.535133,-9.490305,-1.890637,2.560381,-8.992200,-4.918113,-8.338835,3.449273,-6.105740,-5.303207,3.161301,-5.645274,8.274799,8.539188,-0.194596,6.654771,-3.887757,-7.805007,-6.113125,7.148206,-0.566034,-5.109880,4.110086,7.858856,-4.755221,7.128958,-8.202733,5.241120,-7.155039,0.109470,6.205386,-5.805367,-2.080599,-5.378678,-2.013732,0.733458,3.686855,-7.118216,-8.068852,5.519976,8.062111,-8.282146,-3.904302,7.810913,-0.694466,-2.904599,-8.453558,-0.467477,5.465234,6.574441,-1.210883,-4.115865,-7.801697,-9.480714,2.847857,-4.820708,3.383955,-7.128663,-6.978987,-2.437260,-3.198623,-8.715776,3.660014,4.050135,-6.256086,-6.570159,-6.105330,-7.726951,1.288668,8.961992,-7.607206,-9.806694,-9.844798,-4.729145,-9.067349,-2.009478,0.945511,6.199589,0.858652,1.526126,-4.256203,-9.654434,-2.319068,6.209224,-7.218851,-2.379451,-8.674312,-1.469670,4.008564,6.174522,9.803877,-7.549446,2.646915,9.002069,0.779533,-7.066481,-7.938848,-1.327055,1.061152,7.112682,-6.440898,2.328206,-0.274660,5.005659,-8.870955,7.473740,-1.478628,-9.686852,-9.381789,-5.009532,-7.306342,1.150908,-9.363636,5.292430,7.056293,6.740710,5.957655,6.782251,-3.229483,2.559245,4.796712,-2.338209,7.119452,0.306668,-3.973904,6.278949,-8.357196,0.086571,-2.820184,7.990746,4.327455,1.505907,5.980865,-0.212962,0.620938,-6.645192,2.813838,0.722640,0.180264,-5.692440,-4.065603,-6.759820,-1.580333,4.883280,-4.900921,-5.917434,1.495758,-1.268104,-1.626019,-0.148698,7.043686,1.241745,9.920480,1.467725,6.724354,-9.979165,7.168485,2.076858,7.236138,-3.667175,4.395571,2.261855,-5.739621,2.940825,0.665350,-3.450769,-4.529098,8.314061,-2.592312,-8.901176,-1.762211,-3.051705,7.826616,9.689941,-0.118779,-9.528274,-1.132701,4.624759,-0.906928,-1.506430,-6.092440,-6.236641,-9.359057,2.604318,-8.911897,-8.653182,-8.752761,-4.452553,-2.376653,-4.356569,4.103119,-6.716371,6.633516,-4.501467,-4.380241,9.832116,9.310212,4.946340,8.554711,6.388033,-6.149374,-4.790629,-2.366657,-0.479327,-2.207580,9.622511,-0.091007,2.443202,0.566378,8.996211,-9.656618,4.115887,-9.325655,6.809511,0.755111,0.912261,6.332402,-3.261777,-6.631231,-8.821637,-1.280125,-3.197374,-9.181946,-8.300569,0.696006,1.736986,-5.118547,5.834423,-8.940640,-0.741297,5.295501,1.807558,7.658990,-0.586928,4.723586,-4.215074,5.692656,-2.598293,-4.959620,3.924904,-3.055406,-7.823601,5.466250,8.233990,-6.323855,6.097787,7.004220,-8.406569,2.085917,-2.265858,-5.211043,-5.859121,9.318602,5.029897,6.981154,3.044085,2.102643,-8.123830,5.846559,-2.724471,8.073009,-7.611469,5.374172,7.709620,0.476889,7.544152,-3.829416,2.233059,-2.628179,9.079319,-5.814427,7.178054,-5.246495,-6.917019,6.764681,-6.746874,8.259677,9.250221,8.054366,2.801276,-9.159639,-0.663981,-2.087170,-2.780206,-5.628520,-4.898242,-5.203703,6.170373,8.686146,-7.943811,-8.395782,3.430451,6.737713,-7.449728,3.067253,-7.658390,-2.302252,-8.623976,-6.141845,0.117035,-6.814801,7.392375,0.793277,-2.540781,1.680113,8.495428,6.292991,1.286563,3.828607,5.881951,1.138012,-3.111774,0.811885,-5.676544,8.420653,-5.601033,8.219268,-0.847750,-6.326241,9.878186,-4.477855,-5.414747,7.318390,-6.938772,4.816159,5.543522,1.402160,2.335729,-1.213045,6.091343,2.748431,0.404587,0.675297,-2.571191,-3.217610,5.512099], dtype = "float64")#candidate|9804|(378,)|const|float64
call_9803 = relay.TupleGetItem(func_9719_call(relay.reshape(const_9804.astype('float64'), [378,])), 5)
call_9805 = relay.TupleGetItem(func_9722_call(relay.reshape(const_9804.astype('float64'), [378,])), 5)
func_2620_call = mod.get_global_var('func_2620')
func_2624_call = mutated_mod.get_global_var('func_2624')
var_9827 = relay.var("var_9827", dtype = "float32", shape = (280,))#candidate|9827|(280,)|var|float32
var_9828 = relay.var("var_9828", dtype = "int8", shape = (192,))#candidate|9828|(192,)|var|int8
call_9826 = relay.TupleGetItem(func_2620_call(relay.reshape(var_9827.astype('float32'), [8, 7, 5]), relay.reshape(var_9828.astype('int8'), [24, 8]), ), 6)
call_9829 = relay.TupleGetItem(func_2624_call(relay.reshape(var_9827.astype('float32'), [8, 7, 5]), relay.reshape(var_9828.astype('int8'), [24, 8]), ), 6)
func_3230_call = mod.get_global_var('func_3230')
func_3232_call = mutated_mod.get_global_var('func_3232')
call_9835 = func_3230_call()
call_9836 = func_3230_call()
func_3894_call = mod.get_global_var('func_3894')
func_3898_call = mutated_mod.get_global_var('func_3898')
var_9841 = relay.var("var_9841", dtype = "uint64", shape = (360,))#candidate|9841|(360,)|var|uint64
call_9840 = relay.TupleGetItem(func_3894_call(relay.reshape(var_9841.astype('uint64'), [10, 6, 6]), relay.reshape(var_9841.astype('uint64'), [10, 6, 6]), ), 2)
call_9842 = relay.TupleGetItem(func_3898_call(relay.reshape(var_9841.astype('uint64'), [10, 6, 6]), relay.reshape(var_9841.astype('uint64'), [10, 6, 6]), ), 2)
output = relay.Tuple([call_9801,call_9803,const_9804,call_9826,var_9827,var_9828,call_9835,call_9840,var_9841,])
output2 = relay.Tuple([call_9802,call_9805,const_9804,call_9829,var_9827,var_9828,call_9836,call_9842,var_9841,])
func_9843 = relay.Function([var_9827,var_9828,var_9841,], output)
mod['func_9843'] = func_9843
mod = relay.transform.InferType()(mod)
var_9844 = relay.var("var_9844", dtype = "float32", shape = (280,))#candidate|9844|(280,)|var|float32
var_9845 = relay.var("var_9845", dtype = "int8", shape = (192,))#candidate|9845|(192,)|var|int8
var_9846 = relay.var("var_9846", dtype = "uint64", shape = (360,))#candidate|9846|(360,)|var|uint64
output = func_9843(var_9844,var_9845,var_9846,)
func_9847 = relay.Function([var_9844,var_9845,var_9846,], output)
mutated_mod['func_9847'] = func_9847
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9864 = relay.const([[[-5,-7,3,7,5,-6],[-6,-5,8,-4,7,-8],[3,9,4,-1,4,-6],[-7,2,-4,8,-9,-10],[3,7,1,8,3,-7],[7,-5,-7,9,-5,-7],[-1,-10,-8,-7,-8,10],[-10,-5,-8,-1,2,7],[9,3,-8,5,-5,-10],[-9,3,1,-7,6,7],[4,-8,-4,-6,-2,6],[-1,-9,-10,-1,-8,-6],[-2,4,-7,-9,-7,-9],[-1,-3,-6,-2,2,5]],[[-4,2,-1,-3,-3,10],[-7,1,5,4,-5,-8],[8,9,-3,1,-1,1],[3,-4,2,6,-2,-3],[7,2,6,4,-1,-3],[7,4,-9,9,-1,-8],[-8,2,1,6,5,-1],[-9,-5,8,-7,-4,-5],[7,6,-9,-1,-7,9],[-8,-6,-5,4,-2,4],[-8,6,-3,-8,-5,8],[-7,2,-2,1,-8,-5],[-4,6,-9,-7,-5,-3],[-6,-9,-3,6,8,3]],[[-9,-1,1,-1,-6,-10],[-9,-4,-2,3,7,-10],[8,2,3,7,-10,-10],[-6,-6,8,-7,-7,-1],[7,-8,5,5,-1,1],[-10,8,9,-3,-7,-7],[-8,-1,-5,-5,-6,5],[8,-5,4,-5,-4,-8],[-8,-8,-1,1,-9,-6],[7,-5,2,-4,-1,-9],[5,-1,6,-10,2,1],[-2,5,-5,4,-10,-4],[-10,-3,7,5,-8,1],[-8,8,8,5,2,-9]],[[-9,-8,3,-3,2,3],[-10,1,7,-1,2,6],[9,-10,-9,7,-4,-9],[8,-2,-10,2,-3,7],[7,-6,-7,1,-4,-4],[-3,-3,7,6,5,-10],[2,4,-4,-7,1,2],[-6,4,5,2,-1,5],[-8,5,-8,10,-6,-7],[-7,3,-8,4,9,3],[-5,2,-2,6,-9,-3],[8,10,8,-4,10,3],[-4,1,4,-5,-10,7],[-5,2,-5,-4,-8,7]],[[-10,3,10,-9,4,6],[-5,-8,-10,-7,-1,-3],[-3,1,1,-1,1,-2],[-1,-5,-2,-2,-6,2],[-7,-2,-7,5,4,-3],[-4,-8,8,7,-5,-4],[-5,-4,9,6,-4,-4],[-7,-10,7,-8,10,7],[7,9,6,9,-10,-4],[-8,4,-3,2,9,1],[-7,-8,-4,-5,9,-3],[7,-10,-4,5,5,1],[-10,-7,6,5,-4,2],[-8,-1,1,5,5,-7]]], dtype = "int32")#candidate|9864|(5, 14, 6)|const|int32
var_9865 = relay.var("var_9865", dtype = "int32", shape = (5, 14, 6))#candidate|9865|(5, 14, 6)|var|int32
bop_9866 = relay.left_shift(const_9864.astype('int32'), relay.reshape(var_9865.astype('int32'), relay.shape_of(const_9864))) # shape=(5, 14, 6)
output = relay.Tuple([bop_9866,])
output2 = relay.Tuple([bop_9866,])
func_9876 = relay.Function([var_9865,], output)
mod['func_9876'] = func_9876
mod = relay.transform.InferType()(mod)
mutated_mod['func_9876'] = func_9876
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9877 = relay.var("var_9877", dtype = "int32", shape = (5, 14, 6))#candidate|9877|(5, 14, 6)|var|int32
func_9876_call = mutated_mod.get_global_var('func_9876')
call_9878 = func_9876_call(var_9877)
output = call_9878
func_9879 = relay.Function([var_9877], output)
mutated_mod['func_9879'] = func_9879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7872_call = mod.get_global_var('func_7872')
func_7874_call = mutated_mod.get_global_var('func_7874')
call_9891 = relay.TupleGetItem(func_7872_call(), 1)
call_9892 = relay.TupleGetItem(func_7874_call(), 1)
output = relay.Tuple([call_9891,])
output2 = relay.Tuple([call_9892,])
func_9895 = relay.Function([], output)
mod['func_9895'] = func_9895
mod = relay.transform.InferType()(mod)
output = func_9895()
func_9896 = relay.Function([], output)
mutated_mod['func_9896'] = func_9896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8355_call = mod.get_global_var('func_8355')
func_8356_call = mutated_mod.get_global_var('func_8356')
call_9911 = relay.TupleGetItem(func_8355_call(), 0)
call_9912 = relay.TupleGetItem(func_8356_call(), 0)
output = call_9911
output2 = call_9912
func_9915 = relay.Function([], output)
mod['func_9915'] = func_9915
mod = relay.transform.InferType()(mod)
mutated_mod['func_9915'] = func_9915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9915_call = mutated_mod.get_global_var('func_9915')
call_9916 = func_9915_call()
output = call_9916
func_9917 = relay.Function([], output)
mutated_mod['func_9917'] = func_9917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_9938 = relay.TupleGetItem(func_1761_call(), 1)
call_9939 = relay.TupleGetItem(func_1762_call(), 1)
func_3230_call = mod.get_global_var('func_3230')
func_3232_call = mutated_mod.get_global_var('func_3232')
call_9940 = func_3230_call()
call_9941 = func_3230_call()
func_3968_call = mod.get_global_var('func_3968')
func_3971_call = mutated_mod.get_global_var('func_3971')
var_9950 = relay.var("var_9950", dtype = "uint8", shape = (99, 2))#candidate|9950|(99, 2)|var|uint8
call_9949 = func_3968_call(relay.reshape(var_9950.astype('uint8'), [2, 9, 11]), relay.reshape(var_9950.astype('uint8'), [2, 9, 11]), )
call_9951 = func_3968_call(relay.reshape(var_9950.astype('uint8'), [2, 9, 11]), relay.reshape(var_9950.astype('uint8'), [2, 9, 11]), )
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_9965 = relay.TupleGetItem(func_3682_call(), 2)
call_9966 = relay.TupleGetItem(func_3684_call(), 2)
func_8743_call = mod.get_global_var('func_8743')
func_8744_call = mutated_mod.get_global_var('func_8744')
call_9974 = relay.TupleGetItem(func_8743_call(), 0)
call_9975 = relay.TupleGetItem(func_8744_call(), 0)
func_9329_call = mod.get_global_var('func_9329')
func_9331_call = mutated_mod.get_global_var('func_9331')
call_9983 = relay.TupleGetItem(func_9329_call(), 1)
call_9984 = relay.TupleGetItem(func_9331_call(), 1)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_9985 = relay.TupleGetItem(func_1318_call(), 1)
call_9986 = relay.TupleGetItem(func_1319_call(), 1)
var_10028 = relay.var("var_10028", dtype = "float32", shape = (24,))#candidate|10028|(24,)|var|float32
bop_10029 = relay.bitwise_xor(call_9965.astype('int8'), relay.reshape(var_10028.astype('int8'), relay.shape_of(call_9965))) # shape=(24,)
bop_10032 = relay.bitwise_xor(call_9966.astype('int8'), relay.reshape(var_10028.astype('int8'), relay.shape_of(call_9966))) # shape=(24,)
output = relay.Tuple([call_9938,call_9940,call_9949,var_9950,call_9974,call_9983,call_9985,bop_10029,])
output2 = relay.Tuple([call_9939,call_9941,call_9951,var_9950,call_9975,call_9984,call_9986,bop_10032,])
func_10054 = relay.Function([var_9950,var_10028,], output)
mod['func_10054'] = func_10054
mod = relay.transform.InferType()(mod)
var_10055 = relay.var("var_10055", dtype = "uint8", shape = (99, 2))#candidate|10055|(99, 2)|var|uint8
var_10056 = relay.var("var_10056", dtype = "float32", shape = (24,))#candidate|10056|(24,)|var|float32
output = func_10054(var_10055,var_10056,)
func_10057 = relay.Function([var_10055,var_10056,], output)
mutated_mod['func_10057'] = func_10057
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10069 = relay.var("var_10069", dtype = "int32", shape = (14, 4, 3))#candidate|10069|(14, 4, 3)|var|int32
var_10070 = relay.var("var_10070", dtype = "int32", shape = (14, 4, 3))#candidate|10070|(14, 4, 3)|var|int32
bop_10071 = relay.add(var_10069.astype('int32'), relay.reshape(var_10070.astype('int32'), relay.shape_of(var_10069))) # shape=(14, 4, 3)
func_2787_call = mod.get_global_var('func_2787')
func_2789_call = mutated_mod.get_global_var('func_2789')
call_10077 = relay.TupleGetItem(func_2787_call(), 0)
call_10078 = relay.TupleGetItem(func_2789_call(), 0)
func_8657_call = mod.get_global_var('func_8657')
func_8658_call = mutated_mod.get_global_var('func_8658')
call_10089 = relay.TupleGetItem(func_8657_call(), 1)
call_10090 = relay.TupleGetItem(func_8658_call(), 1)
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_10095 = relay.TupleGetItem(func_1761_call(), 2)
call_10096 = relay.TupleGetItem(func_1762_call(), 2)
output = relay.Tuple([bop_10071,call_10077,call_10089,call_10095,])
output2 = relay.Tuple([bop_10071,call_10078,call_10090,call_10096,])
func_10099 = relay.Function([var_10069,var_10070,], output)
mod['func_10099'] = func_10099
mod = relay.transform.InferType()(mod)
var_10100 = relay.var("var_10100", dtype = "int32", shape = (14, 4, 3))#candidate|10100|(14, 4, 3)|var|int32
var_10101 = relay.var("var_10101", dtype = "int32", shape = (14, 4, 3))#candidate|10101|(14, 4, 3)|var|int32
output = func_10099(var_10100,var_10101,)
func_10102 = relay.Function([var_10100,var_10101,], output)
mutated_mod['func_10102'] = func_10102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5608_call = mod.get_global_var('func_5608')
func_5609_call = mutated_mod.get_global_var('func_5609')
call_10135 = relay.TupleGetItem(func_5608_call(), 0)
call_10136 = relay.TupleGetItem(func_5609_call(), 0)
func_7899_call = mod.get_global_var('func_7899')
func_7900_call = mutated_mod.get_global_var('func_7900')
call_10145 = relay.TupleGetItem(func_7899_call(), 0)
call_10146 = relay.TupleGetItem(func_7900_call(), 0)
func_4153_call = mod.get_global_var('func_4153')
func_4156_call = mutated_mod.get_global_var('func_4156')
const_10165 = relay.const(True, dtype = "bool")#candidate|10165|()|const|bool
var_10166 = relay.var("var_10166", dtype = "bool", shape = (1, 16))#candidate|10166|(1, 16)|var|bool
call_10164 = relay.TupleGetItem(func_4153_call(relay.reshape(const_10165.astype('bool'), []), relay.reshape(var_10166.astype('bool'), [1, 4, 4]), ), 0)
call_10167 = relay.TupleGetItem(func_4156_call(relay.reshape(const_10165.astype('bool'), []), relay.reshape(var_10166.astype('bool'), [1, 4, 4]), ), 0)
output = relay.Tuple([call_10135,call_10145,call_10164,const_10165,var_10166,])
output2 = relay.Tuple([call_10136,call_10146,call_10167,const_10165,var_10166,])
func_10197 = relay.Function([var_10166,], output)
mod['func_10197'] = func_10197
mod = relay.transform.InferType()(mod)
mutated_mod['func_10197'] = func_10197
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10198 = relay.var("var_10198", dtype = "bool", shape = (1, 16))#candidate|10198|(1, 16)|var|bool
func_10197_call = mutated_mod.get_global_var('func_10197')
call_10199 = func_10197_call(var_10198)
output = call_10199
func_10200 = relay.Function([var_10198], output)
mutated_mod['func_10200'] = func_10200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3186_call = mod.get_global_var('func_3186')
func_3187_call = mutated_mod.get_global_var('func_3187')
call_10272 = func_3186_call()
call_10273 = func_3186_call()
output = call_10272
output2 = call_10273
func_10290 = relay.Function([], output)
mod['func_10290'] = func_10290
mod = relay.transform.InferType()(mod)
output = func_10290()
func_10291 = relay.Function([], output)
mutated_mod['func_10291'] = func_10291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10294 = relay.var("var_10294", dtype = "uint8", shape = (5, 4, 5))#candidate|10294|(5, 4, 5)|var|uint8
var_10295 = relay.var("var_10295", dtype = "uint8", shape = (5, 4, 5))#candidate|10295|(5, 4, 5)|var|uint8
bop_10296 = relay.subtract(var_10294.astype('uint8'), relay.reshape(var_10295.astype('uint8'), relay.shape_of(var_10294))) # shape=(5, 4, 5)
output = bop_10296
output2 = bop_10296
func_10316 = relay.Function([var_10294,var_10295,], output)
mod['func_10316'] = func_10316
mod = relay.transform.InferType()(mod)
var_10317 = relay.var("var_10317", dtype = "uint8", shape = (5, 4, 5))#candidate|10317|(5, 4, 5)|var|uint8
var_10318 = relay.var("var_10318", dtype = "uint8", shape = (5, 4, 5))#candidate|10318|(5, 4, 5)|var|uint8
output = func_10316(var_10317,var_10318,)
func_10319 = relay.Function([var_10317,var_10318,], output)
mutated_mod['func_10319'] = func_10319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5294_call = mod.get_global_var('func_5294')
func_5295_call = mutated_mod.get_global_var('func_5295')
call_10332 = relay.TupleGetItem(func_5294_call(), 4)
call_10333 = relay.TupleGetItem(func_5295_call(), 4)
output = call_10332
output2 = call_10333
func_10350 = relay.Function([], output)
mod['func_10350'] = func_10350
mod = relay.transform.InferType()(mod)
mutated_mod['func_10350'] = func_10350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10350_call = mutated_mod.get_global_var('func_10350')
call_10351 = func_10350_call()
output = call_10351
func_10352 = relay.Function([], output)
mutated_mod['func_10352'] = func_10352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_10474 = relay.TupleGetItem(func_2912_call(), 1)
call_10475 = relay.TupleGetItem(func_2913_call(), 1)
output = relay.Tuple([call_10474,])
output2 = relay.Tuple([call_10475,])
func_10485 = relay.Function([], output)
mod['func_10485'] = func_10485
mod = relay.transform.InferType()(mod)
output = func_10485()
func_10486 = relay.Function([], output)
mutated_mod['func_10486'] = func_10486
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10538 = relay.var("var_10538", dtype = "float64", shape = (1, 12, 4))#candidate|10538|(1, 12, 4)|var|float64
var_10539 = relay.var("var_10539", dtype = "float64", shape = (14, 12, 4))#candidate|10539|(14, 12, 4)|var|float64
bop_10540 = relay.mod(var_10538.astype('float64'), var_10539.astype('float64')) # shape=(14, 12, 4)
uop_10551 = relay.acosh(var_10539.astype('float32')) # shape=(14, 12, 4)
uop_10560 = relay.atan(var_10539.astype('float32')) # shape=(14, 12, 4)
bop_10567 = relay.greater_equal(uop_10560.astype('bool'), relay.reshape(uop_10551.astype('bool'), relay.shape_of(uop_10560))) # shape=(14, 12, 4)
output = relay.Tuple([bop_10540,bop_10567,])
output2 = relay.Tuple([bop_10540,bop_10567,])
func_10570 = relay.Function([var_10538,var_10539,], output)
mod['func_10570'] = func_10570
mod = relay.transform.InferType()(mod)
mutated_mod['func_10570'] = func_10570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10570_call = mutated_mod.get_global_var('func_10570')
var_10572 = relay.var("var_10572", dtype = "float64", shape = (1, 12, 4))#candidate|10572|(1, 12, 4)|var|float64
var_10573 = relay.var("var_10573", dtype = "float64", shape = (14, 12, 4))#candidate|10573|(14, 12, 4)|var|float64
call_10571 = func_10570_call(var_10572,var_10573,)
output = call_10571
func_10574 = relay.Function([var_10572,var_10573,], output)
mutated_mod['func_10574'] = func_10574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5010_call = mod.get_global_var('func_5010')
func_5012_call = mutated_mod.get_global_var('func_5012')
call_10586 = relay.TupleGetItem(func_5010_call(), 0)
call_10587 = relay.TupleGetItem(func_5012_call(), 0)
func_8580_call = mod.get_global_var('func_8580')
func_8582_call = mutated_mod.get_global_var('func_8582')
var_10613 = relay.var("var_10613", dtype = "float64", shape = (480,))#candidate|10613|(480,)|var|float64
call_10612 = relay.TupleGetItem(func_8580_call(relay.reshape(var_10613.astype('float64'), [2, 240])), 1)
call_10614 = relay.TupleGetItem(func_8582_call(relay.reshape(var_10613.astype('float64'), [2, 240])), 1)
bop_10640 = relay.less(call_10612.astype('bool'), relay.reshape(var_10613.astype('bool'), relay.shape_of(call_10612))) # shape=(10, 16, 3)
bop_10643 = relay.less(call_10614.astype('bool'), relay.reshape(var_10613.astype('bool'), relay.shape_of(call_10614))) # shape=(10, 16, 3)
output = relay.Tuple([call_10586,bop_10640,])
output2 = relay.Tuple([call_10587,bop_10643,])
func_10646 = relay.Function([var_10613,], output)
mod['func_10646'] = func_10646
mod = relay.transform.InferType()(mod)
var_10647 = relay.var("var_10647", dtype = "float64", shape = (480,))#candidate|10647|(480,)|var|float64
output = func_10646(var_10647)
func_10648 = relay.Function([var_10647], output)
mutated_mod['func_10648'] = func_10648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7872_call = mod.get_global_var('func_7872')
func_7874_call = mutated_mod.get_global_var('func_7874')
call_10681 = relay.TupleGetItem(func_7872_call(), 0)
call_10682 = relay.TupleGetItem(func_7874_call(), 0)
output = call_10681
output2 = call_10682
func_10688 = relay.Function([], output)
mod['func_10688'] = func_10688
mod = relay.transform.InferType()(mod)
output = func_10688()
func_10689 = relay.Function([], output)
mutated_mod['func_10689'] = func_10689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7423_call = mod.get_global_var('func_7423')
func_7424_call = mutated_mod.get_global_var('func_7424')
call_10746 = relay.TupleGetItem(func_7423_call(), 1)
call_10747 = relay.TupleGetItem(func_7424_call(), 1)
output = call_10746
output2 = call_10747
func_10771 = relay.Function([], output)
mod['func_10771'] = func_10771
mod = relay.transform.InferType()(mod)
output = func_10771()
func_10772 = relay.Function([], output)
mutated_mod['func_10772'] = func_10772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5099_call = mod.get_global_var('func_5099')
func_5101_call = mutated_mod.get_global_var('func_5101')
call_10804 = relay.TupleGetItem(func_5099_call(), 0)
call_10805 = relay.TupleGetItem(func_5101_call(), 0)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_10810 = relay.TupleGetItem(func_1858_call(), 1)
call_10811 = relay.TupleGetItem(func_1859_call(), 1)
output = relay.Tuple([call_10804,call_10810,])
output2 = relay.Tuple([call_10805,call_10811,])
func_10812 = relay.Function([], output)
mod['func_10812'] = func_10812
mod = relay.transform.InferType()(mod)
output = func_10812()
func_10813 = relay.Function([], output)
mutated_mod['func_10813'] = func_10813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_10832 = relay.TupleGetItem(func_3950_call(), 2)
call_10833 = relay.TupleGetItem(func_3952_call(), 2)
func_9843_call = mod.get_global_var('func_9843')
func_9847_call = mutated_mod.get_global_var('func_9847')
var_10835 = relay.var("var_10835", dtype = "float32", shape = (280,))#candidate|10835|(280,)|var|float32
const_10836 = relay.const([6,-9,-3,5,7,-9,5,5,6,4,2,-4,-1,-7,2,9,1,-6,2,-4,-3,-5,-7,-6,8,-6,1,-1,1,-3,1,-4,-9,-7,-4,-1,-5,7,-9,-9,-5,9,5,10,7,-10,7,-3,4,9,-2,-7,7,3,7,2,4,-9,1,-4,5,9,8,8,1,-10,-6,-9,10,-8,1,10,1,-4,-3,3,4,9,5,4,7,-8,-10,7,-1,7,-4,9,8,-10,-4,8,6,-8,7,6,5,-8,-10,-6,-9,-3,2,10,5,-9,-10,7,-6,-6,8,-6,5,1,-8,-8,-10,10,3,1,8,1,7,-6,4,6,4,-6,-6,4,-5,-1,-3,6,10,8,-7,8,6,9,-7,-3,-6,2,7,8,-8,7,-9,-1,-10,7,-7,-1,2,-2,-4,-2,3,6,1,10,-10,-3,9,8,-3,7,1,-3,-10,1,-10,-6,-8,3,-6,-9,1,7,-5,9,9,10,-4,2,9,-7,8,-4,-8,6], dtype = "int8")#candidate|10836|(192,)|const|int8
const_10837 = relay.const([2,8,-5,-4,3,-2,5,7,1,-1,-9,-6,7,-1,9,7,-9,3,-10,-10,-2,7,2,5,3,4,6,4,-5,4,8,-5,8,3,-5,-2,-9,6,-4,5,-6,-9,2,-4,8,-10,3,5,5,9,3,7,-10,-1,4,2,-8,2,4,-4,-8,-9,2,-10,10,-7,3,-2,8,9,-3,4,2,9,4,8,-2,10,-9,-10,-4,-1,-10,-9,-10,2,1,-5,2,1,-1,-7,-4,-6,-9,-3,3,9,-10,-4,1,4,-10,7,6,7,4,2,-4,2,-5,8,10,-1,-8,-9,-1,-10,-5,-2,-4,-10,-6,8,-1,3,7,3,-9,-6,-9,7,-1,10,6,8,-4,8,-1,8,-9,7,2,-3,-4,9,5,5,5,-1,1,10,-10,-3,-9,2,-2,3,-8,-5,7,-10,-2,-8,4,9,-1,-9,1,1,-3,-5,-1,-10,-7,5,-1,-6,-4,1,4,-3,10,5,4,-9,-8,-5,-7,9,-10,-9,1,-5,10,3,7,-8,-8,8,8,10,-4,-4,-9,-6,-9,-3,10,7,5,3,-6,1,-5,-7,-8,10,1,4,9,3,5,-2,4,-5,1,-3,1,2,-2,-9,-5,2,-3,8,-8,-3,4,8,-5,9,10,-3,-5,-7,2,-5,4,-3,-6,2,3,-7,-9,7,9,-9,7,10,-7,-6,4,5,3,-7,-10,-2,-2,-10,-3,6,4,-1,-5,2,9,-10,1,10,-5,2,-8,10,3,-3,-8,8,-2,2,1,1,4,-2,-9,1,-1,-1,7,-9,3,9,-10,-3,6,-2,-1,-7,-4,-2,-3,-9,5,-3,3,-5,5,10,-10,8,10,1,2,-6,8,3,10,6,-4,-8,-5,7,-6,5,-8,2,-4,-9,2,5,3,9,-10,9,-6,-4,9,-10,6,10,2,-4,-4,3,8,6,-5,-7,10,10], dtype = "uint64")#candidate|10837|(360,)|const|uint64
call_10834 = relay.TupleGetItem(func_9843_call(relay.reshape(var_10835.astype('float32'), [280,]), relay.reshape(const_10836.astype('int8'), [192,]), relay.reshape(const_10837.astype('uint64'), [360,]), ), 4)
call_10838 = relay.TupleGetItem(func_9847_call(relay.reshape(var_10835.astype('float32'), [280,]), relay.reshape(const_10836.astype('int8'), [192,]), relay.reshape(const_10837.astype('uint64'), [360,]), ), 4)
output = relay.Tuple([call_10832,call_10834,var_10835,const_10836,const_10837,])
output2 = relay.Tuple([call_10833,call_10838,var_10835,const_10836,const_10837,])
func_10854 = relay.Function([var_10835,], output)
mod['func_10854'] = func_10854
mod = relay.transform.InferType()(mod)
mutated_mod['func_10854'] = func_10854
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10855 = relay.var("var_10855", dtype = "float32", shape = (280,))#candidate|10855|(280,)|var|float32
func_10854_call = mutated_mod.get_global_var('func_10854')
call_10856 = func_10854_call(var_10855)
output = call_10856
func_10857 = relay.Function([var_10855], output)
mutated_mod['func_10857'] = func_10857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10350_call = mod.get_global_var('func_10350')
func_10352_call = mutated_mod.get_global_var('func_10352')
call_10937 = func_10350_call()
call_10938 = func_10350_call()
func_6039_call = mod.get_global_var('func_6039')
func_6041_call = mutated_mod.get_global_var('func_6041')
call_10939 = relay.TupleGetItem(func_6039_call(), 1)
call_10940 = relay.TupleGetItem(func_6041_call(), 1)
output = relay.Tuple([call_10937,call_10939,])
output2 = relay.Tuple([call_10938,call_10940,])
func_10951 = relay.Function([], output)
mod['func_10951'] = func_10951
mod = relay.transform.InferType()(mod)
output = func_10951()
func_10952 = relay.Function([], output)
mutated_mod['func_10952'] = func_10952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9895_call = mod.get_global_var('func_9895')
func_9896_call = mutated_mod.get_global_var('func_9896')
call_10981 = relay.TupleGetItem(func_9895_call(), 0)
call_10982 = relay.TupleGetItem(func_9896_call(), 0)
output = relay.Tuple([call_10981,])
output2 = relay.Tuple([call_10982,])
func_10987 = relay.Function([], output)
mod['func_10987'] = func_10987
mod = relay.transform.InferType()(mod)
output = func_10987()
func_10988 = relay.Function([], output)
mutated_mod['func_10988'] = func_10988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_11004 = relay.TupleGetItem(func_3950_call(), 2)
call_11005 = relay.TupleGetItem(func_3952_call(), 2)
func_2292_call = mod.get_global_var('func_2292')
func_2294_call = mutated_mod.get_global_var('func_2294')
call_11025 = relay.TupleGetItem(func_2292_call(), 1)
call_11026 = relay.TupleGetItem(func_2294_call(), 1)
func_3186_call = mod.get_global_var('func_3186')
func_3187_call = mutated_mod.get_global_var('func_3187')
call_11034 = func_3186_call()
call_11035 = func_3186_call()
output = relay.Tuple([call_11004,call_11025,call_11034,])
output2 = relay.Tuple([call_11005,call_11026,call_11035,])
func_11037 = relay.Function([], output)
mod['func_11037'] = func_11037
mod = relay.transform.InferType()(mod)
output = func_11037()
func_11038 = relay.Function([], output)
mutated_mod['func_11038'] = func_11038
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11065 = relay.var("var_11065", dtype = "float32", shape = (15, 7, 11))#candidate|11065|(15, 7, 11)|var|float32
const_11066 = relay.const([[[0.187046,4.426837,-7.940663,9.401545,4.142546,7.197772,-1.674706,-3.392558,-3.900937,3.779150,0.811244],[5.409656,-7.052942,-1.798096,-1.755872,-8.340806,-0.123531,1.994214,5.429695,2.695971,1.779815,-1.972938],[-0.836677,-7.887563,5.754617,9.783397,-8.803560,3.487327,-3.089244,5.895430,-9.986532,-9.773507,-2.980345],[1.149265,-5.509772,-7.659074,-4.521326,-3.366457,1.761988,6.782015,-5.168938,4.338837,-2.396523,3.712676],[5.530344,8.390231,-6.473947,-8.185630,-4.962231,8.107316,-4.913128,-9.400131,-2.836294,7.204644,-1.765120],[-2.176415,-2.989839,0.998519,-5.917639,7.325788,-0.885741,9.290874,-9.475756,7.608361,-6.350254,-8.089357],[-7.596854,4.640027,9.969460,7.490585,7.732736,-2.062340,2.802106,-3.824818,9.124703,8.565947,2.047028]],[[-1.360954,8.890864,-3.484797,-2.269475,-9.422897,9.114573,3.296789,5.694111,-2.347013,-8.544327,-3.982022],[8.043267,-6.073487,-5.364956,-9.127772,-3.185675,8.283340,-4.274554,3.998866,-5.604422,4.910043,6.868170],[-7.215687,3.991621,-3.941161,-4.885390,-9.796030,6.559112,-3.130245,-5.472536,9.010381,8.246354,-2.935819],[-7.625485,1.405751,-9.973222,9.650175,1.495009,-2.554638,-9.408874,7.930052,1.787823,-8.727135,-3.165275],[-0.031264,4.962207,7.156629,-3.666277,-2.886770,-0.898254,-8.480154,3.860954,-1.318846,1.770159,6.810733],[6.530589,-5.512595,-6.466143,-8.765427,6.294827,-9.971052,-6.877523,-6.126327,1.545926,-6.039265,-6.885483],[-4.889639,-0.065306,-7.428085,8.455612,2.621930,-6.560219,6.287732,4.138566,8.260258,-8.201329,8.401172]],[[-1.290460,-0.947049,8.715116,9.123661,9.533838,5.744849,-0.478604,9.482343,6.661494,5.299434,9.190395],[2.550861,-9.499020,5.937612,-0.464181,5.665621,-4.760825,-7.221614,-5.211411,6.282851,-1.570108,8.850797],[7.758897,-1.033473,-0.693835,-3.772399,4.602361,-8.459855,5.282375,-5.201102,-3.810572,-0.750693,6.084789],[-7.383245,-1.508731,3.126396,-3.806879,7.997621,-6.318175,8.975216,8.531751,-0.060149,5.563083,-1.669799],[-8.044312,-1.944974,1.129758,-4.114081,4.884982,-4.993630,-6.765141,-7.366665,7.004504,-3.317902,-3.864806],[-6.856653,-5.451735,-6.798897,5.554470,-9.017754,5.134296,-2.062018,7.452171,-5.526779,-7.642767,-9.737692],[-5.295349,7.964074,-8.165303,8.833847,5.397003,5.243949,-5.808894,5.755996,-9.666723,-8.175150,-9.637298]],[[-1.831883,1.298290,9.195620,-2.247892,-2.739924,-7.720967,-0.874567,-0.491182,8.556302,4.297141,9.700289],[-6.783577,7.412476,-4.375171,1.088446,-4.730491,-5.613718,-0.755498,8.591041,4.746638,4.392032,-6.262626],[-9.711172,-3.502428,-9.605098,-9.366677,7.900952,9.307085,-2.969140,-1.927087,-9.964179,2.631449,-6.769012],[-2.733730,-4.620896,-9.645671,-9.457292,0.322497,6.771152,-6.205775,8.231627,0.522445,-4.958115,1.032285],[-7.412792,-1.656248,1.625999,2.068726,2.751569,3.126873,6.338891,8.997660,-0.442092,-5.718271,-9.917934],[-4.185359,-5.876226,8.933174,-5.503245,9.413332,-6.064284,6.971656,7.265720,-2.415578,4.013572,1.351446],[5.813148,-8.939277,9.537942,4.219654,7.165238,-4.037329,5.397570,-4.892941,-7.060594,-7.015854,3.079786]],[[-3.378487,-9.301489,8.116202,4.261135,-0.165163,-8.610189,-4.166310,3.028114,8.139325,3.526997,-8.381507],[6.794338,-1.149651,-9.823231,9.629102,2.870246,1.449841,-8.140363,7.931564,0.315301,-5.051607,-8.610343],[9.525184,-0.060017,-7.825013,-0.237331,-6.300550,-2.920574,-1.077167,2.572185,-3.814441,4.188464,-5.244943],[8.112940,5.145434,6.594406,-5.782256,1.606260,7.567826,-9.283360,3.702439,7.335635,5.836402,1.256403],[-1.782449,6.565205,3.617320,-6.133754,-2.731724,6.180865,-1.015227,7.970068,-2.667959,4.915315,-4.800664],[5.422489,-3.315254,0.453403,-0.056243,0.419407,0.725217,-8.125420,-1.675095,-5.979826,-5.049514,-5.541747],[-1.030649,7.859246,-2.034858,-2.495375,-8.737110,8.687324,-6.935484,-3.871867,2.679821,-2.147050,-5.527786]],[[2.462618,4.858730,9.461501,3.509459,0.253175,5.577359,-1.950053,5.341860,-3.872846,-1.654975,-6.933961],[-3.520192,-7.484880,9.946744,-0.340123,6.564637,-6.510639,2.412677,-3.779230,0.595694,-4.298284,-4.377536],[5.435251,-5.552389,1.431494,4.166715,2.788955,9.790454,4.489685,-7.301458,-1.687594,8.355567,8.250473],[8.085536,2.163655,7.305049,0.119039,-5.941031,1.225343,5.711383,2.655212,-6.801086,-5.130013,-6.829240],[-3.743585,-6.497046,-2.058783,3.821730,-1.473579,7.824573,-9.258786,-3.783241,-3.788744,-4.836263,2.069303],[1.095102,-1.151873,6.939297,8.691529,-7.722651,4.594934,-7.046276,-5.154542,0.010217,-5.235350,-6.015385],[6.701664,2.408804,3.554873,5.815531,6.714293,9.575435,-3.582266,-3.502754,4.509165,-5.059604,6.291117]],[[-9.181899,-8.866157,6.332088,9.577343,0.224541,-8.915323,-4.647672,-4.931401,-3.163193,-3.150221,9.992858],[-4.380243,-6.373684,-6.045883,-1.207775,-2.086230,9.368561,-1.862244,7.160457,-6.537019,-8.502133,7.864174],[-9.791285,-7.414972,0.851594,7.273064,-4.550311,1.898630,4.227591,0.566025,5.670948,-7.110471,-6.372706],[0.455406,-0.980752,1.421611,-6.703347,-0.553098,-3.372198,9.664722,8.455061,1.551023,0.192797,8.885288],[-5.328781,-1.508538,-4.826407,3.200380,-4.503741,-6.599469,-7.782641,6.742209,1.880068,-0.225438,5.668647],[6.506021,-1.331196,-9.304217,1.733898,-1.885239,-0.131310,-8.804847,6.914896,8.692518,-6.715640,1.073335],[4.728220,-3.114308,-3.267531,6.186942,-4.846903,-3.284333,8.023536,-8.261916,-5.466436,-0.738175,-6.820530]],[[2.247312,-5.765394,8.535616,8.399406,-7.703498,5.379097,8.727060,4.475178,4.934889,3.313546,-3.452048],[-8.962643,-0.773434,9.620598,8.196380,0.002222,5.079932,-4.715603,-7.340764,6.598707,-6.430484,3.865798],[-3.898178,-4.627151,0.621918,-0.449114,-2.962627,-2.901253,1.302840,-0.414588,9.485000,-9.452484,0.432976],[4.173030,-3.403657,-4.906951,-8.837979,-3.806175,-2.086047,-1.450554,-6.839466,9.883749,-3.591517,7.386565],[0.987466,-7.390303,0.247109,-5.780762,7.134685,8.954325,-8.550710,5.141269,5.746583,-8.905974,-0.724967],[8.479271,2.072531,-9.437256,1.985861,0.280814,8.809288,7.167755,-6.712459,2.757914,-1.798243,4.570287],[0.152366,7.758287,-5.433307,-4.723678,-6.245632,-1.493429,8.585177,5.512163,-3.453604,8.106503,1.019391]],[[5.350591,-3.006756,1.972549,5.413166,-0.480668,3.691629,3.241540,5.058079,3.983843,-0.319352,7.536245],[-2.541764,-5.084925,1.675325,-5.851012,-3.906480,9.101517,-4.958066,0.589482,2.577537,-3.011863,1.131315],[6.999121,-1.282010,2.556228,-0.293269,-5.223227,0.798318,7.691696,-0.300784,9.364486,0.775220,-8.951586],[-6.690272,6.707389,3.962244,-6.361702,-0.619251,7.552300,-8.825046,6.995344,0.753565,3.822164,-9.507280],[5.050889,-1.696880,6.178182,4.965009,-5.027548,-2.552742,-2.907387,1.774562,-8.948602,-5.457084,-1.944913],[-0.122377,0.606085,5.472133,5.731778,4.513870,3.882484,4.755846,-7.178511,-8.458304,-1.320496,-4.091901],[-1.444073,-9.157550,7.466104,-3.595489,8.523491,2.200520,-6.979294,-8.248231,-9.368475,-0.895840,0.939446]],[[9.991388,5.482032,-5.816655,-0.974143,-6.274741,3.327897,0.771829,0.805902,-5.360009,3.616119,8.640240],[4.450055,5.020174,0.459320,1.349136,0.662197,-7.323958,-5.278255,6.200435,-0.790754,1.348268,-1.148582],[-5.349311,-0.871289,-6.854336,9.101701,9.147340,7.981585,-4.819073,-7.567244,-7.188178,-5.108746,-4.185984],[0.254244,7.760686,2.889327,0.959290,-9.256855,8.804263,2.222591,-8.313002,5.956043,1.245781,-0.267213],[-8.523083,4.535655,-5.083044,2.905622,-1.461740,-8.603258,-5.293272,-7.236528,8.683187,-4.553037,6.283685],[2.074434,-6.109160,3.145131,9.635692,8.515721,-0.141203,-5.596917,2.010094,-0.506478,7.119190,8.712127],[-0.783831,1.121225,-4.919735,1.766181,0.268043,4.891194,7.278313,1.297519,-5.651131,-3.435132,9.840468]],[[-7.199141,6.905898,-1.412856,4.628574,-4.753660,9.701005,-5.379565,6.747833,9.469052,-2.602120,-5.488320],[3.057810,-6.146229,5.338005,0.114796,-2.486451,6.569929,-4.865132,-1.805704,5.954135,1.367069,-1.520987],[4.761693,0.005712,5.664734,9.438651,-1.106583,7.367147,9.018071,7.107785,-7.732611,-6.951237,9.967026],[9.642202,-5.158120,6.005914,-3.754993,0.684077,1.900161,-4.485526,-6.055989,2.860224,8.544713,-4.109571],[9.339839,1.139978,1.374118,9.619425,-0.929233,-0.774379,0.951026,-2.307561,1.930420,5.820438,3.190968],[5.610994,-6.247125,-2.482167,-6.682102,-7.466872,-2.003475,3.134500,6.753155,2.563611,5.255390,-5.597775],[6.125637,-5.306488,2.913118,5.072334,-7.269432,-7.374634,8.994943,-5.530521,7.115449,2.492188,-0.373248]],[[5.952533,1.807526,6.169863,-0.311181,-3.584573,-3.460534,0.653409,-2.610936,-2.479921,9.400354,8.898267],[9.188316,-2.238469,-4.947549,3.419220,-3.374808,-9.171737,1.491919,4.854996,-8.441140,2.794616,-0.277739],[-2.177886,5.667705,4.351118,4.349054,-8.623724,-8.295997,-7.347271,-1.075028,9.027760,-6.298365,6.323888],[4.594048,-8.842249,-4.417964,6.091916,-5.198623,6.988522,-5.995572,-7.964580,-7.723196,1.431547,-3.438594],[4.665300,4.877019,0.174930,8.193104,6.315315,1.199424,-6.104172,1.383737,1.463189,7.919564,5.437777],[4.615262,2.861371,-9.638530,8.810506,-5.422593,-2.283868,3.112503,-8.316158,-8.101054,-9.266156,5.043364],[2.487333,-6.996991,-7.056444,8.367765,2.151153,8.021016,-1.776669,8.124533,-8.733350,7.946788,2.910435]],[[6.211378,0.455846,5.964022,8.953952,-1.748365,3.771781,9.883106,-0.719057,-7.673373,-5.733143,-0.683915],[9.311504,-3.361488,-5.799913,-9.843754,-1.702363,8.892189,8.041905,8.581460,5.175942,6.523803,-1.704294],[-7.405486,-0.811139,9.658035,-7.660146,2.873474,2.810760,-0.501966,8.445850,-5.390780,-3.667273,3.593139],[-5.571883,-3.688155,-7.238377,4.126369,7.241031,2.652798,-7.849547,-1.871151,1.357162,-4.318710,3.148850],[-5.197739,-5.358213,-6.965103,-3.545070,-3.450452,3.387077,-6.844813,6.951428,-4.739187,1.671851,-2.041978],[-8.845357,-5.935542,-3.510642,6.066005,4.504739,0.071249,-4.770794,-8.397046,0.068680,5.205392,-7.893970],[9.234949,9.894292,-7.290976,3.736797,-9.358062,6.631247,0.348394,-1.742385,3.084799,-7.585245,0.409513]],[[-3.846207,7.312381,-5.484366,-4.598820,-5.963059,-9.735289,-6.257768,-8.256708,1.151408,7.370021,-0.779693],[4.188108,4.764915,-5.790685,1.992465,-2.719451,-8.702594,6.239777,6.135639,6.388776,6.241122,6.896051],[-3.970025,-6.762682,9.802428,-9.820066,-5.517184,-9.285168,-5.725196,-5.603646,-3.892169,6.400666,-4.233901],[1.728427,7.799442,-6.511147,4.276561,-9.677132,2.599143,3.831983,-1.614044,-2.439254,0.294069,3.916175],[-0.157378,2.897245,-8.552441,8.615738,-7.215244,-0.432029,5.336179,-0.089909,8.583969,-0.774103,4.591625],[3.064996,2.150641,1.785949,-6.368773,-4.855183,-4.662524,3.657277,-0.808806,0.523224,4.241189,-7.674607],[-0.229237,3.323731,7.294698,1.063586,-2.882838,3.258321,-5.778049,-9.961704,1.038611,3.146329,8.986834]],[[-0.267973,2.173265,-2.925304,-6.419629,2.417973,5.070806,-1.811373,-4.631045,-3.426431,-1.944941,-6.353216],[-2.953387,6.576610,4.412139,4.144756,0.647303,6.483067,4.927602,6.161763,-1.385145,3.973280,-3.581180],[1.602175,4.064412,7.571691,1.153166,-6.844002,-2.201655,9.005329,6.196309,-7.200976,-6.402049,4.592786],[6.625388,2.525312,-9.285051,-2.464053,-8.849867,7.916525,9.903771,2.741665,9.587916,-6.221833,5.788606],[2.078435,-8.975626,7.696336,1.295371,-5.871151,-6.835979,2.422237,-6.050941,5.483855,5.317426,-5.568191],[2.785939,0.810133,-7.183015,-0.225800,7.470212,-8.318226,-4.415586,-8.926050,-0.910253,-8.524846,9.320091],[7.984995,2.955290,-5.350987,-5.670652,7.620005,1.706701,-0.592645,-0.667940,7.734633,-5.945032,1.781771]]], dtype = "float32")#candidate|11066|(15, 7, 11)|const|float32
bop_11067 = relay.less_equal(var_11065.astype('bool'), relay.reshape(const_11066.astype('bool'), relay.shape_of(var_11065))) # shape=(15, 7, 11)
func_2530_call = mod.get_global_var('func_2530')
func_2532_call = mutated_mod.get_global_var('func_2532')
call_11076 = relay.TupleGetItem(func_2530_call(), 0)
call_11077 = relay.TupleGetItem(func_2532_call(), 0)
bop_11080 = relay.left_shift(var_11065.astype('int16'), relay.reshape(const_11066.astype('int16'), relay.shape_of(var_11065))) # shape=(15, 7, 11)
uop_11097 = relay.asin(bop_11067.astype('float32')) # shape=(15, 7, 11)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_11110 = func_1704_call()
call_11111 = func_1704_call()
bop_11114 = relay.add(const_11066.astype('float64'), relay.reshape(bop_11080.astype('float64'), relay.shape_of(const_11066))) # shape=(15, 7, 11)
uop_11121 = relay.atanh(uop_11097.astype('float32')) # shape=(15, 7, 11)
output = relay.Tuple([call_11076,call_11110,bop_11114,uop_11121,])
output2 = relay.Tuple([call_11077,call_11111,bop_11114,uop_11121,])
func_11135 = relay.Function([var_11065,], output)
mod['func_11135'] = func_11135
mod = relay.transform.InferType()(mod)
var_11136 = relay.var("var_11136", dtype = "float32", shape = (15, 7, 11))#candidate|11136|(15, 7, 11)|var|float32
output = func_11135(var_11136)
func_11137 = relay.Function([var_11136], output)
mutated_mod['func_11137'] = func_11137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_11165 = relay.TupleGetItem(func_1761_call(), 2)
call_11166 = relay.TupleGetItem(func_1762_call(), 2)
func_2202_call = mod.get_global_var('func_2202')
func_2205_call = mutated_mod.get_global_var('func_2205')
call_11168 = relay.TupleGetItem(func_2202_call(relay.reshape(call_11165.astype('float32'), [7, 10, 13])), 0)
call_11169 = relay.TupleGetItem(func_2205_call(relay.reshape(call_11165.astype('float32'), [7, 10, 13])), 0)
output = relay.Tuple([call_11165,call_11168,])
output2 = relay.Tuple([call_11166,call_11169,])
func_11175 = relay.Function([], output)
mod['func_11175'] = func_11175
mod = relay.transform.InferType()(mod)
output = func_11175()
func_11176 = relay.Function([], output)
mutated_mod['func_11176'] = func_11176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5099_call = mod.get_global_var('func_5099')
func_5101_call = mutated_mod.get_global_var('func_5101')
call_11198 = relay.TupleGetItem(func_5099_call(), 0)
call_11199 = relay.TupleGetItem(func_5101_call(), 0)
func_8887_call = mod.get_global_var('func_8887')
func_8888_call = mutated_mod.get_global_var('func_8888')
call_11206 = relay.TupleGetItem(func_8887_call(), 0)
call_11207 = relay.TupleGetItem(func_8888_call(), 0)
output = relay.Tuple([call_11198,call_11206,])
output2 = relay.Tuple([call_11199,call_11207,])
func_11213 = relay.Function([], output)
mod['func_11213'] = func_11213
mod = relay.transform.InferType()(mod)
mutated_mod['func_11213'] = func_11213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11213_call = mutated_mod.get_global_var('func_11213')
call_11214 = func_11213_call()
output = call_11214
func_11215 = relay.Function([], output)
mutated_mod['func_11215'] = func_11215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4112_call = mod.get_global_var('func_4112')
func_4113_call = mutated_mod.get_global_var('func_4113')
call_11239 = func_4112_call()
call_11240 = func_4112_call()
func_7920_call = mod.get_global_var('func_7920')
func_7921_call = mutated_mod.get_global_var('func_7921')
call_11250 = relay.TupleGetItem(func_7920_call(), 0)
call_11251 = relay.TupleGetItem(func_7921_call(), 0)
func_10812_call = mod.get_global_var('func_10812')
func_10813_call = mutated_mod.get_global_var('func_10813')
call_11265 = relay.TupleGetItem(func_10812_call(), 0)
call_11266 = relay.TupleGetItem(func_10813_call(), 0)
output = relay.Tuple([call_11239,call_11250,call_11265,])
output2 = relay.Tuple([call_11240,call_11251,call_11266,])
func_11267 = relay.Function([], output)
mod['func_11267'] = func_11267
mod = relay.transform.InferType()(mod)
output = func_11267()
func_11268 = relay.Function([], output)
mutated_mod['func_11268'] = func_11268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3682_call = mod.get_global_var('func_3682')
func_3684_call = mutated_mod.get_global_var('func_3684')
call_11292 = relay.TupleGetItem(func_3682_call(), 2)
call_11293 = relay.TupleGetItem(func_3684_call(), 2)
func_10350_call = mod.get_global_var('func_10350')
func_10352_call = mutated_mod.get_global_var('func_10352')
call_11295 = func_10350_call()
call_11296 = func_10350_call()
uop_11301 = relay.cos(call_11295.astype('float64')) # shape=(300, 1)
uop_11303 = relay.cos(call_11296.astype('float64')) # shape=(300, 1)
output = relay.Tuple([call_11292,uop_11301,])
output2 = relay.Tuple([call_11293,uop_11303,])
func_11304 = relay.Function([], output)
mod['func_11304'] = func_11304
mod = relay.transform.InferType()(mod)
output = func_11304()
func_11305 = relay.Function([], output)
mutated_mod['func_11305'] = func_11305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mod.get_global_var('func_5818')
func_5819_call = mutated_mod.get_global_var('func_5819')
call_11312 = relay.TupleGetItem(func_5818_call(), 0)
call_11313 = relay.TupleGetItem(func_5819_call(), 0)
output = call_11312
output2 = call_11313
func_11324 = relay.Function([], output)
mod['func_11324'] = func_11324
mod = relay.transform.InferType()(mod)
output = func_11324()
func_11325 = relay.Function([], output)
mutated_mod['func_11325'] = func_11325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7423_call = mod.get_global_var('func_7423')
func_7424_call = mutated_mod.get_global_var('func_7424')
call_11380 = relay.TupleGetItem(func_7423_call(), 0)
call_11381 = relay.TupleGetItem(func_7424_call(), 0)
func_6503_call = mod.get_global_var('func_6503')
func_6505_call = mutated_mod.get_global_var('func_6505')
call_11389 = relay.TupleGetItem(func_6503_call(), 0)
call_11390 = relay.TupleGetItem(func_6505_call(), 0)
output = relay.Tuple([call_11380,call_11389,])
output2 = relay.Tuple([call_11381,call_11390,])
func_11424 = relay.Function([], output)
mod['func_11424'] = func_11424
mod = relay.transform.InferType()(mod)
mutated_mod['func_11424'] = func_11424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11424_call = mutated_mod.get_global_var('func_11424')
call_11425 = func_11424_call()
output = call_11425
func_11426 = relay.Function([], output)
mutated_mod['func_11426'] = func_11426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9538_call = mod.get_global_var('func_9538')
func_9540_call = mutated_mod.get_global_var('func_9540')
call_11466 = func_9538_call()
call_11467 = func_9538_call()
func_6633_call = mod.get_global_var('func_6633')
func_6634_call = mutated_mod.get_global_var('func_6634')
call_11505 = relay.TupleGetItem(func_6633_call(), 1)
call_11506 = relay.TupleGetItem(func_6634_call(), 1)
output = relay.Tuple([call_11466,call_11505,])
output2 = relay.Tuple([call_11467,call_11506,])
func_11509 = relay.Function([], output)
mod['func_11509'] = func_11509
mod = relay.transform.InferType()(mod)
output = func_11509()
func_11510 = relay.Function([], output)
mutated_mod['func_11510'] = func_11510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7920_call = mod.get_global_var('func_7920')
func_7921_call = mutated_mod.get_global_var('func_7921')
call_11520 = relay.TupleGetItem(func_7920_call(), 1)
call_11521 = relay.TupleGetItem(func_7921_call(), 1)
func_9915_call = mod.get_global_var('func_9915')
func_9917_call = mutated_mod.get_global_var('func_9917')
call_11538 = func_9915_call()
call_11539 = func_9915_call()
output = relay.Tuple([call_11520,call_11538,])
output2 = relay.Tuple([call_11521,call_11539,])
func_11579 = relay.Function([], output)
mod['func_11579'] = func_11579
mod = relay.transform.InferType()(mod)
mutated_mod['func_11579'] = func_11579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11579_call = mutated_mod.get_global_var('func_11579')
call_11580 = func_11579_call()
output = call_11580
func_11581 = relay.Function([], output)
mutated_mod['func_11581'] = func_11581
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11587 = relay.var("var_11587", dtype = "float32", shape = (7, 10, 3))#candidate|11587|(7, 10, 3)|var|float32
uop_11588 = relay.asinh(var_11587.astype('float32')) # shape=(7, 10, 3)
output = relay.Tuple([uop_11588,])
output2 = relay.Tuple([uop_11588,])
func_11602 = relay.Function([var_11587,], output)
mod['func_11602'] = func_11602
mod = relay.transform.InferType()(mod)
var_11603 = relay.var("var_11603", dtype = "float32", shape = (7, 10, 3))#candidate|11603|(7, 10, 3)|var|float32
output = func_11602(var_11603)
func_11604 = relay.Function([var_11603], output)
mutated_mod['func_11604'] = func_11604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10485_call = mod.get_global_var('func_10485')
func_10486_call = mutated_mod.get_global_var('func_10486')
call_11681 = relay.TupleGetItem(func_10485_call(), 0)
call_11682 = relay.TupleGetItem(func_10486_call(), 0)
func_9437_call = mod.get_global_var('func_9437')
func_9439_call = mutated_mod.get_global_var('func_9439')
call_11690 = func_9437_call()
call_11691 = func_9437_call()
func_5294_call = mod.get_global_var('func_5294')
func_5295_call = mutated_mod.get_global_var('func_5295')
call_11696 = relay.TupleGetItem(func_5294_call(), 2)
call_11697 = relay.TupleGetItem(func_5295_call(), 2)
output = relay.Tuple([call_11681,call_11690,call_11696,])
output2 = relay.Tuple([call_11682,call_11691,call_11697,])
func_11701 = relay.Function([], output)
mod['func_11701'] = func_11701
mod = relay.transform.InferType()(mod)
output = func_11701()
func_11702 = relay.Function([], output)
mutated_mod['func_11702'] = func_11702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7097_call = mod.get_global_var('func_7097')
func_7098_call = mutated_mod.get_global_var('func_7098')
call_11724 = relay.TupleGetItem(func_7097_call(), 1)
call_11725 = relay.TupleGetItem(func_7098_call(), 1)
func_8887_call = mod.get_global_var('func_8887')
func_8888_call = mutated_mod.get_global_var('func_8888')
call_11754 = relay.TupleGetItem(func_8887_call(), 0)
call_11755 = relay.TupleGetItem(func_8888_call(), 0)
output = relay.Tuple([call_11724,call_11754,])
output2 = relay.Tuple([call_11725,call_11755,])
func_11760 = relay.Function([], output)
mod['func_11760'] = func_11760
mod = relay.transform.InferType()(mod)
mutated_mod['func_11760'] = func_11760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11760_call = mutated_mod.get_global_var('func_11760')
call_11761 = func_11760_call()
output = call_11761
func_11762 = relay.Function([], output)
mutated_mod['func_11762'] = func_11762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_11766 = relay.TupleGetItem(func_1318_call(), 0)
call_11767 = relay.TupleGetItem(func_1319_call(), 0)
func_6063_call = mod.get_global_var('func_6063')
func_6065_call = mutated_mod.get_global_var('func_6065')
call_11778 = relay.TupleGetItem(func_6063_call(), 0)
call_11779 = relay.TupleGetItem(func_6065_call(), 0)
output = relay.Tuple([call_11766,call_11778,])
output2 = relay.Tuple([call_11767,call_11779,])
func_11798 = relay.Function([], output)
mod['func_11798'] = func_11798
mod = relay.transform.InferType()(mod)
output = func_11798()
func_11799 = relay.Function([], output)
mutated_mod['func_11799'] = func_11799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6975_call = mod.get_global_var('func_6975')
func_6977_call = mutated_mod.get_global_var('func_6977')
call_11946 = relay.TupleGetItem(func_6975_call(), 0)
call_11947 = relay.TupleGetItem(func_6977_call(), 0)
output = call_11946
output2 = call_11947
func_11951 = relay.Function([], output)
mod['func_11951'] = func_11951
mod = relay.transform.InferType()(mod)
output = func_11951()
func_11952 = relay.Function([], output)
mutated_mod['func_11952'] = func_11952
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11953 = relay.var("var_11953", dtype = "float64", shape = (1, 5, 11))#candidate|11953|(1, 5, 11)|var|float64
var_11954 = relay.var("var_11954", dtype = "float64", shape = (14, 5, 11))#candidate|11954|(14, 5, 11)|var|float64
bop_11955 = relay.power(var_11953.astype('float64'), var_11954.astype('float64')) # shape=(14, 5, 11)
func_6287_call = mod.get_global_var('func_6287')
func_6288_call = mutated_mod.get_global_var('func_6288')
call_11965 = relay.TupleGetItem(func_6287_call(), 1)
call_11966 = relay.TupleGetItem(func_6288_call(), 1)
bop_11974 = relay.not_equal(var_11953.astype('bool'), var_11954.astype('bool')) # shape=(14, 5, 11)
output = relay.Tuple([bop_11955,call_11965,bop_11974,])
output2 = relay.Tuple([bop_11955,call_11966,bop_11974,])
func_11977 = relay.Function([var_11953,var_11954,], output)
mod['func_11977'] = func_11977
mod = relay.transform.InferType()(mod)
var_11978 = relay.var("var_11978", dtype = "float64", shape = (1, 5, 11))#candidate|11978|(1, 5, 11)|var|float64
var_11979 = relay.var("var_11979", dtype = "float64", shape = (14, 5, 11))#candidate|11979|(14, 5, 11)|var|float64
output = func_11977(var_11978,var_11979,)
func_11980 = relay.Function([var_11978,var_11979,], output)
mutated_mod['func_11980'] = func_11980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5839_call = mod.get_global_var('func_5839')
func_5841_call = mutated_mod.get_global_var('func_5841')
call_11991 = relay.TupleGetItem(func_5839_call(), 0)
call_11992 = relay.TupleGetItem(func_5841_call(), 0)
output = relay.Tuple([call_11991,])
output2 = relay.Tuple([call_11992,])
func_11998 = relay.Function([], output)
mod['func_11998'] = func_11998
mod = relay.transform.InferType()(mod)
mutated_mod['func_11998'] = func_11998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11998_call = mutated_mod.get_global_var('func_11998')
call_11999 = func_11998_call()
output = call_11999
func_12000 = relay.Function([], output)
mutated_mod['func_12000'] = func_12000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3186_call = mod.get_global_var('func_3186')
func_3187_call = mutated_mod.get_global_var('func_3187')
call_12035 = func_3186_call()
call_12036 = func_3186_call()
func_1761_call = mod.get_global_var('func_1761')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_12066 = relay.TupleGetItem(func_1761_call(), 0)
call_12067 = relay.TupleGetItem(func_1762_call(), 0)
func_11760_call = mod.get_global_var('func_11760')
func_11762_call = mutated_mod.get_global_var('func_11762')
call_12075 = relay.TupleGetItem(func_11760_call(), 1)
call_12076 = relay.TupleGetItem(func_11762_call(), 1)
output = relay.Tuple([call_12035,call_12066,call_12075,])
output2 = relay.Tuple([call_12036,call_12067,call_12076,])
func_12087 = relay.Function([], output)
mod['func_12087'] = func_12087
mod = relay.transform.InferType()(mod)
output = func_12087()
func_12088 = relay.Function([], output)
mutated_mod['func_12088'] = func_12088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4312_call = mod.get_global_var('func_4312')
func_4314_call = mutated_mod.get_global_var('func_4314')
call_12092 = relay.TupleGetItem(func_4312_call(), 0)
call_12093 = relay.TupleGetItem(func_4314_call(), 0)
func_3792_call = mod.get_global_var('func_3792')
func_3795_call = mutated_mod.get_global_var('func_3795')
var_12102 = relay.var("var_12102", dtype = "float32", shape = (546,))#candidate|12102|(546,)|var|float32
const_12103 = relay.const([[-8],[8],[9],[9],[-7],[-6],[1],[9],[10],[6],[1],[-7],[-2],[-4],[6],[7],[-9],[5],[3],[10],[9],[5],[8],[9],[7],[-9],[5],[-3],[-2],[7],[-3],[10],[-1],[9],[-9],[6],[-7],[-9],[6],[-4],[-5],[3],[-8],[8],[3],[5],[-10],[-7],[-10],[-5],[-7],[8],[-3],[-8],[6],[3],[-4],[5],[3],[9],[-9],[-4],[-9],[-1],[9],[-9],[-6],[-10],[-7],[5],[-2],[-7],[5],[6],[5],[7],[-2],[-4],[4],[-2],[-1],[9],[10],[-4],[10],[2],[-10],[-8],[-3],[6],[-2],[4],[6],[6],[5],[-2],[9],[-4],[3],[-7],[9],[-4],[-10],[-7],[-9],[-3],[-6],[4],[8],[1],[-8],[-10],[4],[-7],[1],[-1],[5],[3],[-10],[-2],[-3],[-7],[-3],[10],[-2],[3],[-4],[6],[-6],[-7],[7],[9],[-5],[-1],[3],[1],[8],[5],[-10],[-3],[8],[4],[-10],[1],[3],[2],[8],[-4],[-4],[-6],[-6],[-2],[-7],[-6],[-6],[1],[4],[7],[4],[-7],[-8],[9],[-10],[6],[7],[2],[-9],[8],[3],[-2],[2],[4],[-9],[-7],[1],[-3],[4],[-6],[4],[10],[-4],[-5],[-7],[10],[8],[1],[-7],[3],[6],[-2],[5],[-7]], dtype = "int8")#candidate|12103|(192, 1)|const|int8
call_12101 = relay.TupleGetItem(func_3792_call(relay.reshape(var_12102.astype('float32'), [546,]), relay.reshape(const_12103.astype('int8'), [48, 4]), ), 9)
call_12104 = relay.TupleGetItem(func_3795_call(relay.reshape(var_12102.astype('float32'), [546,]), relay.reshape(const_12103.astype('int8'), [48, 4]), ), 9)
output = relay.Tuple([call_12092,call_12101,var_12102,const_12103,])
output2 = relay.Tuple([call_12093,call_12104,var_12102,const_12103,])
func_12108 = relay.Function([var_12102,], output)
mod['func_12108'] = func_12108
mod = relay.transform.InferType()(mod)
mutated_mod['func_12108'] = func_12108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12109 = relay.var("var_12109", dtype = "float32", shape = (546,))#candidate|12109|(546,)|var|float32
func_12108_call = mutated_mod.get_global_var('func_12108')
call_12110 = func_12108_call(var_12109)
output = call_12110
func_12111 = relay.Function([var_12109], output)
mutated_mod['func_12111'] = func_12111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4588_call = mod.get_global_var('func_4588')
func_4590_call = mutated_mod.get_global_var('func_4590')
call_12166 = relay.TupleGetItem(func_4588_call(), 5)
call_12167 = relay.TupleGetItem(func_4590_call(), 5)
func_5608_call = mod.get_global_var('func_5608')
func_5609_call = mutated_mod.get_global_var('func_5609')
call_12168 = relay.TupleGetItem(func_5608_call(), 0)
call_12169 = relay.TupleGetItem(func_5609_call(), 0)
func_7287_call = mod.get_global_var('func_7287')
func_7289_call = mutated_mod.get_global_var('func_7289')
var_12179 = relay.var("var_12179", dtype = "float64", shape = (672,))#candidate|12179|(672,)|var|float64
call_12178 = relay.TupleGetItem(func_7287_call(relay.reshape(var_12179.astype('float64'), [3, 14, 16])), 2)
call_12180 = relay.TupleGetItem(func_7289_call(relay.reshape(var_12179.astype('float64'), [3, 14, 16])), 2)
func_8483_call = mod.get_global_var('func_8483')
func_8484_call = mutated_mod.get_global_var('func_8484')
call_12181 = relay.TupleGetItem(func_8483_call(), 0)
call_12182 = relay.TupleGetItem(func_8484_call(), 0)
output = relay.Tuple([call_12166,call_12168,call_12178,var_12179,call_12181,])
output2 = relay.Tuple([call_12167,call_12169,call_12180,var_12179,call_12182,])
func_12190 = relay.Function([var_12179,], output)
mod['func_12190'] = func_12190
mod = relay.transform.InferType()(mod)
mutated_mod['func_12190'] = func_12190
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12191 = relay.var("var_12191", dtype = "float64", shape = (672,))#candidate|12191|(672,)|var|float64
func_12190_call = mutated_mod.get_global_var('func_12190')
call_12192 = func_12190_call(var_12191)
output = call_12192
func_12193 = relay.Function([var_12191], output)
mutated_mod['func_12193'] = func_12193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1458_call = mod.get_global_var('func_1458')
func_1459_call = mutated_mod.get_global_var('func_1459')
call_12220 = relay.TupleGetItem(func_1458_call(), 0)
call_12221 = relay.TupleGetItem(func_1459_call(), 0)
output = call_12220
output2 = call_12221
func_12239 = relay.Function([], output)
mod['func_12239'] = func_12239
mod = relay.transform.InferType()(mod)
output = func_12239()
func_12240 = relay.Function([], output)
mutated_mod['func_12240'] = func_12240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9895_call = mod.get_global_var('func_9895')
func_9896_call = mutated_mod.get_global_var('func_9896')
call_12241 = relay.TupleGetItem(func_9895_call(), 0)
call_12242 = relay.TupleGetItem(func_9896_call(), 0)
func_4083_call = mod.get_global_var('func_4083')
func_4087_call = mutated_mod.get_global_var('func_4087')
const_12247 = relay.const([-8,-6,-8,-4,-8,-7,6,5,8,-4,-3,5,-7,5,3,-10,7,-2,5,-5,6,1,1,-2,7,7,4,-10,-9,2,-9,1,-6,-2,-8,-5,9,10,3,-7,10,2,6,-7,-5,6,-1,1,-3,8,9,8,1,-8,-2,7,-8,9,3,10,-5,3,5,-3,8,-10,7,7,-7,-4,-9,-2,4,-3,-7,4,-7,-8,-2,3,-2,-8,-2,-7,-9,10,6,7,5,-4,10,4,6,2,-3,-9,-7,-4,-2,-9,-3,-1,5,8,7,-2,-1,-6,10,-6,-4,-8,2,1,-2,-6,-1,6,4,-6,8,-10,6,-8,4,9,-7,-9,8,2,2,9,-5,-9,-10,4,5,-1,-7,-9,-2,-1,7,7,-1,7,9,7,2,-6,5,2,-1,-2,1,1,4,-2,3,-6,10,-8,-9,4,-2,-4,8,6,-9,10,-4,5,3,6,-9,-10,6,-10,4,-6,4,-3,8,-4,10,8,6,-1,-1,7,-1,-10,5,-4,6,5,-2,4,10,6,3,5,7,10,-4,9,4,-4,9,-7,-10,5,-5,-1,-9,8,-2,3,10,9,-8,1,8,-10,3,-2,-4,-4,-5,5,-3,8,-5,-5,4,-10,4,4,-7,9,-6,5,-5,8,-6,-4,7,4,-2,-8,3,-9,-9,9,9,-6,-8,-2,9,-4,6,-6,9,4,9,8,-8,-8,-9,-3,-4,1,9,6,-7,5,-8,4,-8,-1,-10,8,-5,7,3,2,8,-1,1,4,-8,1,7,5,4,2,-6,-4,-7,7,-10,9,-4,-2,10,5,5,5,-1,-7,6,-1,-10,-5,5,-8,1,-10,2,4,-7,1,2,4,-6,-8,-2,7,3,2,-4,-10,10,3,-3,-5,3,4,9,9,-1,-8,-6,-7,-6,7,-9,-6,7,2,-6,10,-2,7,2,-7,-4,8,-1,-1,5,-9,-4,-7,4,-3,-6,-2,-7,10,-6,4,1,2,-8,10,-2,10,-4,9,6,-2,2,1,-4,1,-7,10,7,-1,-6,8,10,3,5,-3,3,3,9,7,6,-3,-2,-2,-8,6,4,1,-4,-7,8,9,-5,-7,10,-8,-3,-9,6,8,4,8,-7,-1,7,9,-8,-7,5,-7,-1,1,-8,10,2,7,-1,-4,-4,-1,-3,-6,-3,5,-8,-10,9,-2,-2,10,2,1,-10,4,-10,-7,-9,7,8,9,6,5,-1,-2,-1,6,-8,7,-2,6,-7,-8,-7,-10,6,-3,7,8,4,2,2,7,4,10,6,-1,-10,-1,3,4,-1,4,2,7,-1,1,6,3,-3,-10,-10,4,-10,-9,-6,-4,7,-4,-9,-6,9,-4,-9,-9,-2,3,-7,-4,-2,2,5,7,-6,-10,4,-7,-5,-10,-2,7,7,7,-7,-3,-5,8,-4,1,-8,9,7,6,9,-6,-6,-6,-1,9,6,-6,10,3,9,-6,-5,10,10,-5,6,1,-2,-7,10,2,9,-8,-2,-2,3,1,-4,-1,8,5,-7,8,-1,-6,-10,-6,-6,9,-3,10,-1,-5,1,9,-4,-5,-9,2,-5,-1,-7,-5,1,-3,-5,2,4,-10,5,-6,2,-2,4,10,-4,-6,10,-6,-5,7,1,-7,7,4,5,-3,-1,7,-8,-5,-10,3,-4,10,9,-1,-7,7,-4,-7,1,7,4,-7,2,5,5,-1,9,8,1,8,6,3,4,-10,-2,7,10,8,-8,-4,-1,1,8,-7,7,-6,-9,-6,9,-10,-2,8,-2,5,-9,2,6,9,-1,3,-2,-4,8,-7,-5,-9,-5,2,-3,-7,8,2,3,1,8,3,-3,-2,-8,-9,8,-1,-6,10,9,-10,7,4,3,-3,9,2,4,4,-5,-4,-2,-5,7,8,1,7,-1,-7,6,7,5,-7,7,10,4,-4,10,-5,-5,6,-10,-5,4,5,-1,3,-4,-4,10,5,-9,-2,-10,-7,-9,-2,-6,2,-8,-7,-3,-4,1,-10,-3,6,-1,10,-7,-6,-10,7,-5,5,10,-4,-2,-10,6,5,2,-1,2,-6,-10,7,-1,5,7,-1,2,8,4,9,7,-1,-7,-3,4,10,-2,-4,-3,-10,1,-7,-7,-8,-4,-2,1,9,-6,7,-4,3,-5,-8,8,-9,1,3,-1,-8,-6,-6,-6,4,-9,-1,7,-8,5,-1,6,-3,3,5,-4,9,-5,-6,-9,-2,-9,-9,1,1,5,-8,-1,8,-4,10,-5,-8,1,5,2,8,2,-2,-7,6,6,-1,-4,2,1,6,8,-10,7,1,-3,-5,-6,-8,1,-5,10,3,-4,-2,7,-2,-3,6,-8,-1,3,7,-4,-4,-1,-1,4,6,9,4,-7,10,1,-10,-2,1,7,-7,-3,6,-2,6,3,8,10,-9,-10,-7,-5,-1,5,2,-10,-5,-4,8,7,3,-5,-3,3,-4,-1,6,-5,4,-1,-2,-7,-3,-7,6,4,-6,-10,-6,3,6,8,-1,-8,-2,1,-9,2,-3,4,5,-1,-9,-1,2,4,9,9,-4,5,6], dtype = "int64")#candidate|12247|(960,)|const|int64
call_12246 = relay.TupleGetItem(func_4083_call(relay.reshape(const_12247.astype('int64'), [16, 5, 12]), relay.reshape(const_12247.astype('int64'), [16, 5, 12]), relay.reshape(const_12247.astype('int64'), [16, 5, 12]), ), 2)
call_12248 = relay.TupleGetItem(func_4087_call(relay.reshape(const_12247.astype('int64'), [16, 5, 12]), relay.reshape(const_12247.astype('int64'), [16, 5, 12]), relay.reshape(const_12247.astype('int64'), [16, 5, 12]), ), 2)
output = relay.Tuple([call_12241,call_12246,const_12247,])
output2 = relay.Tuple([call_12242,call_12248,const_12247,])
func_12254 = relay.Function([], output)
mod['func_12254'] = func_12254
mod = relay.transform.InferType()(mod)
mutated_mod['func_12254'] = func_12254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12254_call = mutated_mod.get_global_var('func_12254')
call_12255 = func_12254_call()
output = call_12255
func_12256 = relay.Function([], output)
mutated_mod['func_12256'] = func_12256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6714_call = mod.get_global_var('func_6714')
func_6716_call = mutated_mod.get_global_var('func_6716')
call_12257 = func_6714_call()
call_12258 = func_6714_call()
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_12265 = func_1704_call()
call_12266 = func_1704_call()
func_4848_call = mod.get_global_var('func_4848')
func_4849_call = mutated_mod.get_global_var('func_4849')
call_12289 = relay.TupleGetItem(func_4848_call(), 1)
call_12290 = relay.TupleGetItem(func_4849_call(), 1)
output = relay.Tuple([call_12257,call_12265,call_12289,])
output2 = relay.Tuple([call_12258,call_12266,call_12290,])
func_12293 = relay.Function([], output)
mod['func_12293'] = func_12293
mod = relay.transform.InferType()(mod)
output = func_12293()
func_12294 = relay.Function([], output)
mutated_mod['func_12294'] = func_12294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12312 = relay.var("var_12312", dtype = "float64", shape = (6, 6, 3))#candidate|12312|(6, 6, 3)|var|float64
var_12313 = relay.var("var_12313", dtype = "float64", shape = (6, 6, 3))#candidate|12313|(6, 6, 3)|var|float64
bop_12314 = relay.floor_mod(var_12312.astype('float64'), relay.reshape(var_12313.astype('float64'), relay.shape_of(var_12312))) # shape=(6, 6, 3)
func_4153_call = mod.get_global_var('func_4153')
func_4156_call = mutated_mod.get_global_var('func_4156')
const_12325 = relay.const(False, dtype = "bool")#candidate|12325|()|const|bool
const_12326 = relay.const([[True,False],[False,False],[True,True],[True,True],[False,True],[False,True],[True,True],[False,True]], dtype = "bool")#candidate|12326|(8, 2)|const|bool
call_12324 = relay.TupleGetItem(func_4153_call(relay.reshape(const_12325.astype('bool'), []), relay.reshape(const_12326.astype('bool'), [1, 4, 4]), ), 2)
call_12327 = relay.TupleGetItem(func_4156_call(relay.reshape(const_12325.astype('bool'), []), relay.reshape(const_12326.astype('bool'), [1, 4, 4]), ), 2)
func_10854_call = mod.get_global_var('func_10854')
func_10857_call = mutated_mod.get_global_var('func_10857')
var_12337 = relay.var("var_12337", dtype = "float32", shape = (280,))#candidate|12337|(280,)|var|float32
call_12336 = relay.TupleGetItem(func_10854_call(relay.reshape(var_12337.astype('float32'), [280,])), 3)
call_12338 = relay.TupleGetItem(func_10857_call(relay.reshape(var_12337.astype('float32'), [280,])), 3)
func_6564_call = mod.get_global_var('func_6564')
func_6566_call = mutated_mod.get_global_var('func_6566')
const_12340 = relay.const([4.319596,-9.759317,5.063264,-5.503813,-5.352510,7.586320,-4.935128,5.515831,2.549485,-7.446610,3.598687,-9.505395,-4.761034,2.927830,2.972856,-1.400821,3.568348,7.260971,0.501600,-9.380966,2.567709,-1.276583,0.266743,-2.478025,1.753685,5.947016,-4.987834,-4.871146,-8.327796,-5.396707,-0.630046,-9.278342,0.827920,-2.092094,1.152836,6.941104], dtype = "float32")#candidate|12340|(36,)|const|float32
call_12339 = relay.TupleGetItem(func_6564_call(relay.reshape(const_12340.astype('float32'), [3, 12])), 0)
call_12341 = relay.TupleGetItem(func_6566_call(relay.reshape(const_12340.astype('float32'), [3, 12])), 0)
var_12353 = relay.var("var_12353", dtype = "float32", shape = (1001,))#candidate|12353|(1001,)|var|float32
bop_12354 = relay.greater(call_12324.astype('bool'), relay.reshape(var_12353.astype('bool'), relay.shape_of(call_12324))) # shape=(1001,)
bop_12357 = relay.greater(call_12327.astype('bool'), relay.reshape(var_12353.astype('bool'), relay.shape_of(call_12327))) # shape=(1001,)
func_4458_call = mod.get_global_var('func_4458')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_12358 = relay.TupleGetItem(func_4458_call(relay.reshape(const_12326.astype('bool'), [16,])), 0)
call_12359 = relay.TupleGetItem(func_4461_call(relay.reshape(const_12326.astype('bool'), [16,])), 0)
output = relay.Tuple([bop_12314,const_12325,const_12326,call_12336,var_12337,call_12339,const_12340,bop_12354,call_12358,])
output2 = relay.Tuple([bop_12314,const_12325,const_12326,call_12338,var_12337,call_12341,const_12340,bop_12357,call_12359,])
func_12361 = relay.Function([var_12312,var_12313,var_12337,var_12353,], output)
mod['func_12361'] = func_12361
mod = relay.transform.InferType()(mod)
mutated_mod['func_12361'] = func_12361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12361_call = mutated_mod.get_global_var('func_12361')
var_12363 = relay.var("var_12363", dtype = "float64", shape = (6, 6, 3))#candidate|12363|(6, 6, 3)|var|float64
var_12364 = relay.var("var_12364", dtype = "float64", shape = (6, 6, 3))#candidate|12364|(6, 6, 3)|var|float64
var_12365 = relay.var("var_12365", dtype = "float32", shape = (280,))#candidate|12365|(280,)|var|float32
var_12366 = relay.var("var_12366", dtype = "float32", shape = (1001,))#candidate|12366|(1001,)|var|float32
call_12362 = func_12361_call(var_12363,var_12364,var_12365,var_12366,)
output = call_12362
func_12367 = relay.Function([var_12363,var_12364,var_12365,var_12366,], output)
mutated_mod['func_12367'] = func_12367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11760_call = mod.get_global_var('func_11760')
func_11762_call = mutated_mod.get_global_var('func_11762')
call_12429 = relay.TupleGetItem(func_11760_call(), 0)
call_12430 = relay.TupleGetItem(func_11762_call(), 0)
func_7819_call = mod.get_global_var('func_7819')
func_7820_call = mutated_mod.get_global_var('func_7820')
call_12431 = func_7819_call()
call_12432 = func_7819_call()
output = relay.Tuple([call_12429,call_12431,])
output2 = relay.Tuple([call_12430,call_12432,])
func_12447 = relay.Function([], output)
mod['func_12447'] = func_12447
mod = relay.transform.InferType()(mod)
mutated_mod['func_12447'] = func_12447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12447_call = mutated_mod.get_global_var('func_12447')
call_12448 = func_12447_call()
output = call_12448
func_12449 = relay.Function([], output)
mutated_mod['func_12449'] = func_12449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8286_call = mod.get_global_var('func_8286')
func_8288_call = mutated_mod.get_global_var('func_8288')
call_12495 = func_8286_call()
call_12496 = func_8286_call()
func_1318_call = mod.get_global_var('func_1318')
func_1319_call = mutated_mod.get_global_var('func_1319')
call_12524 = relay.TupleGetItem(func_1318_call(), 1)
call_12525 = relay.TupleGetItem(func_1319_call(), 1)
output = relay.Tuple([call_12495,call_12524,])
output2 = relay.Tuple([call_12496,call_12525,])
func_12536 = relay.Function([], output)
mod['func_12536'] = func_12536
mod = relay.transform.InferType()(mod)
mutated_mod['func_12536'] = func_12536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12536_call = mutated_mod.get_global_var('func_12536')
call_12537 = func_12536_call()
output = call_12537
func_12538 = relay.Function([], output)
mutated_mod['func_12538'] = func_12538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9338_call = mod.get_global_var('func_9338')
func_9339_call = mutated_mod.get_global_var('func_9339')
call_12569 = func_9338_call()
call_12570 = func_9338_call()
func_4236_call = mod.get_global_var('func_4236')
func_4239_call = mutated_mod.get_global_var('func_4239')
var_12572 = relay.var("var_12572", dtype = "float32", shape = (546,))#candidate|12572|(546,)|var|float32
var_12573 = relay.var("var_12573", dtype = "int8", shape = (48, 4))#candidate|12573|(48, 4)|var|int8
call_12571 = relay.TupleGetItem(func_4236_call(relay.reshape(var_12572.astype('float32'), [546,]), relay.reshape(var_12573.astype('int8'), [192,]), ), 2)
call_12574 = relay.TupleGetItem(func_4239_call(relay.reshape(var_12572.astype('float32'), [546,]), relay.reshape(var_12573.astype('int8'), [192,]), ), 2)
bop_12590 = relay.maximum(var_12573.astype('int8'), relay.reshape(call_12571.astype('int8'), relay.shape_of(var_12573))) # shape=(48, 4)
bop_12593 = relay.maximum(var_12573.astype('int8'), relay.reshape(call_12574.astype('int8'), relay.shape_of(var_12573))) # shape=(48, 4)
output = relay.Tuple([call_12569,var_12572,bop_12590,])
output2 = relay.Tuple([call_12570,var_12572,bop_12593,])
func_12598 = relay.Function([var_12572,var_12573,], output)
mod['func_12598'] = func_12598
mod = relay.transform.InferType()(mod)
mutated_mod['func_12598'] = func_12598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12598_call = mutated_mod.get_global_var('func_12598')
var_12600 = relay.var("var_12600", dtype = "float32", shape = (546,))#candidate|12600|(546,)|var|float32
var_12601 = relay.var("var_12601", dtype = "int8", shape = (48, 4))#candidate|12601|(48, 4)|var|int8
call_12599 = func_12598_call(var_12600,var_12601,)
output = call_12599
func_12602 = relay.Function([var_12600,var_12601,], output)
mutated_mod['func_12602'] = func_12602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1975_call = mod.get_global_var('func_1975')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_12604 = relay.TupleGetItem(func_1975_call(), 0)
call_12605 = relay.TupleGetItem(func_1976_call(), 0)
output = call_12604
output2 = call_12605
func_12606 = relay.Function([], output)
mod['func_12606'] = func_12606
mod = relay.transform.InferType()(mod)
output = func_12606()
func_12607 = relay.Function([], output)
mutated_mod['func_12607'] = func_12607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8355_call = mod.get_global_var('func_8355')
func_8356_call = mutated_mod.get_global_var('func_8356')
call_12646 = relay.TupleGetItem(func_8355_call(), 0)
call_12647 = relay.TupleGetItem(func_8356_call(), 0)
output = call_12646
output2 = call_12647
func_12657 = relay.Function([], output)
mod['func_12657'] = func_12657
mod = relay.transform.InferType()(mod)
output = func_12657()
func_12658 = relay.Function([], output)
mutated_mod['func_12658'] = func_12658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9538_call = mod.get_global_var('func_9538')
func_9540_call = mutated_mod.get_global_var('func_9540')
call_12716 = func_9538_call()
call_12717 = func_9538_call()
func_8657_call = mod.get_global_var('func_8657')
func_8658_call = mutated_mod.get_global_var('func_8658')
call_12732 = relay.TupleGetItem(func_8657_call(), 2)
call_12733 = relay.TupleGetItem(func_8658_call(), 2)
func_12606_call = mod.get_global_var('func_12606')
func_12607_call = mutated_mod.get_global_var('func_12607')
call_12740 = func_12606_call()
call_12741 = func_12606_call()
uop_12744 = relay.sinh(call_12732.astype('float64')) # shape=(7, 10, 13)
uop_12746 = relay.sinh(call_12733.astype('float64')) # shape=(7, 10, 13)
func_9329_call = mod.get_global_var('func_9329')
func_9331_call = mutated_mod.get_global_var('func_9331')
call_12756 = relay.TupleGetItem(func_9329_call(), 1)
call_12757 = relay.TupleGetItem(func_9331_call(), 1)
output = relay.Tuple([call_12716,call_12740,uop_12744,call_12756,])
output2 = relay.Tuple([call_12717,call_12741,uop_12746,call_12757,])
func_12770 = relay.Function([], output)
mod['func_12770'] = func_12770
mod = relay.transform.InferType()(mod)
mutated_mod['func_12770'] = func_12770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12770_call = mutated_mod.get_global_var('func_12770')
call_12771 = func_12770_call()
output = call_12771
func_12772 = relay.Function([], output)
mutated_mod['func_12772'] = func_12772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1426_call = mod.get_global_var('func_1426')
func_1428_call = mutated_mod.get_global_var('func_1428')
call_12781 = relay.TupleGetItem(func_1426_call(), 0)
call_12782 = relay.TupleGetItem(func_1428_call(), 0)
func_7899_call = mod.get_global_var('func_7899')
func_7900_call = mutated_mod.get_global_var('func_7900')
call_12785 = relay.TupleGetItem(func_7899_call(), 0)
call_12786 = relay.TupleGetItem(func_7900_call(), 0)
func_5294_call = mod.get_global_var('func_5294')
func_5295_call = mutated_mod.get_global_var('func_5295')
call_12791 = relay.TupleGetItem(func_5294_call(), 1)
call_12792 = relay.TupleGetItem(func_5295_call(), 1)
func_6248_call = mod.get_global_var('func_6248')
func_6249_call = mutated_mod.get_global_var('func_6249')
call_12802 = relay.TupleGetItem(func_6248_call(), 2)
call_12803 = relay.TupleGetItem(func_6249_call(), 2)
output = relay.Tuple([call_12781,call_12785,call_12791,call_12802,])
output2 = relay.Tuple([call_12782,call_12786,call_12792,call_12803,])
func_12821 = relay.Function([], output)
mod['func_12821'] = func_12821
mod = relay.transform.InferType()(mod)
output = func_12821()
func_12822 = relay.Function([], output)
mutated_mod['func_12822'] = func_12822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9915_call = mod.get_global_var('func_9915')
func_9917_call = mutated_mod.get_global_var('func_9917')
call_12837 = func_9915_call()
call_12838 = func_9915_call()
output = call_12837
output2 = call_12838
func_12854 = relay.Function([], output)
mod['func_12854'] = func_12854
mod = relay.transform.InferType()(mod)
output = func_12854()
func_12855 = relay.Function([], output)
mutated_mod['func_12855'] = func_12855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9915_call = mod.get_global_var('func_9915')
func_9917_call = mutated_mod.get_global_var('func_9917')
call_12861 = func_9915_call()
call_12862 = func_9915_call()
func_6153_call = mod.get_global_var('func_6153')
func_6154_call = mutated_mod.get_global_var('func_6154')
call_12863 = func_6153_call()
call_12864 = func_6153_call()
output = relay.Tuple([call_12861,call_12863,])
output2 = relay.Tuple([call_12862,call_12864,])
func_12891 = relay.Function([], output)
mod['func_12891'] = func_12891
mod = relay.transform.InferType()(mod)
output = func_12891()
func_12892 = relay.Function([], output)
mutated_mod['func_12892'] = func_12892
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12915 = relay.const([[[-9,-1,4,-3,-3,10,-4,-2,-6,-1,-3],[1,8,10,-10,-9,-6,7,4,-6,5,-8],[3,-1,-4,3,-9,-3,-6,5,1,-4,-6],[-7,-3,7,1,6,-5,4,7,-5,2,5],[10,-4,4,10,-9,10,1,9,-3,7,1],[-7,7,-7,1,-6,4,4,6,-7,2,-10],[-5,7,3,3,-5,2,-4,10,-1,-6,6]],[[2,-5,-8,6,-2,-6,-8,4,5,-4,3],[6,-1,2,3,-7,-10,5,1,-8,4,-3],[5,4,9,6,5,-7,-10,-4,-7,-9,-3],[-6,6,7,-8,-2,8,-2,3,-8,2,5],[-6,-7,7,-9,10,5,1,-8,10,3,-6],[-6,-5,-7,2,10,-10,1,5,-10,-7,-3],[-4,-9,-10,6,-9,5,7,-4,-6,6,-3]],[[3,-9,3,7,6,4,8,10,-10,-6,-5],[-10,3,3,-2,-8,-4,-8,-5,-10,8,10],[10,2,9,6,1,10,2,3,2,10,10],[-1,-5,-8,9,-9,-8,-8,8,-8,1,-5],[3,-6,-1,1,4,-8,4,-2,-6,9,-3],[-8,2,4,-5,-6,-8,5,9,-3,-7,6],[9,-4,10,-6,4,-5,-1,2,7,6,10]],[[-5,9,-6,8,-10,9,-1,-9,3,10,-2],[7,7,-1,7,8,2,1,6,9,8,1],[-8,-6,-8,9,7,1,9,-9,-3,10,4],[5,-5,-7,-4,-4,-3,-3,7,8,-9,-6],[-10,7,-9,1,2,-3,-10,-2,1,7,4],[-2,6,-5,-10,5,5,5,1,-9,-10,10],[7,4,-7,1,-3,-4,-2,3,-9,1,-10]],[[-2,-2,4,5,4,7,9,9,5,2,10],[-8,5,-1,3,-5,-2,6,-9,-3,3,2],[-4,-2,4,10,-8,-7,6,-1,1,4,5],[1,-10,-8,4,7,-1,-9,-2,1,7,-3],[7,-4,4,-4,-5,-2,9,8,-9,3,1],[-7,9,3,7,1,-3,-4,10,-5,-3,9],[-6,7,-1,5,10,-7,1,7,7,2,10]],[[9,4,-6,-1,-8,2,-10,6,7,9,-7],[3,8,1,-3,6,4,6,-4,4,1,1],[-1,1,5,9,2,-9,5,10,2,10,5],[-5,-10,-5,7,6,-3,5,9,-1,7,3],[9,-9,-1,-8,-2,7,5,7,-6,-1,2],[-6,-1,3,-8,-1,-10,-9,-9,7,-1,5],[6,8,-5,-10,5,7,4,4,-6,8,-5]],[[-9,3,8,-2,-10,5,10,-8,-8,-8,-1],[-6,-4,-1,-10,-9,-3,-7,-6,3,7,7],[9,-8,10,-3,8,-5,-2,5,5,1,6],[-8,-6,10,1,1,-3,-7,6,-4,-9,-7],[9,3,5,1,-3,-6,2,-4,-5,2,-5],[3,-1,6,-9,-1,4,-2,9,4,4,10],[-8,-10,-9,-3,3,6,4,-6,-6,1,2]],[[-10,-7,-4,4,9,-10,5,3,-4,3,-2],[3,-3,-4,8,8,-10,4,-7,10,8,-7],[7,-2,-6,-4,-3,-4,-5,-1,-8,-3,-5],[2,3,10,-10,-8,-6,-2,5,-9,-3,5],[3,3,6,-8,10,2,2,9,-8,-10,5],[-7,8,-9,8,8,-1,-1,-6,-7,-8,2],[-3,-3,7,-7,5,-5,7,3,7,5,4]],[[-4,-6,7,-9,6,-1,3,10,2,-4,-8],[10,-6,-3,-4,10,7,8,10,4,-1,2],[-5,-4,8,6,10,-7,3,-1,7,7,-5],[-8,6,10,-7,9,-5,-10,4,-10,2,-1],[7,1,3,-6,7,-3,5,8,6,-5,4],[-7,-1,-1,4,7,-5,-7,-10,-9,8,8],[5,-7,-5,5,10,-6,-9,-6,-2,-6,3]],[[7,6,-10,8,-8,-4,-8,-7,-8,3,8],[4,6,-6,5,6,3,-8,6,9,-2,9],[3,1,1,-9,7,-2,1,5,-7,6,3],[-1,1,-5,6,-3,9,4,9,10,7,10],[10,-2,6,-5,5,2,-7,-10,-10,-1,8],[-9,-9,4,-1,-3,-10,5,6,-9,-7,8],[-7,-6,3,5,5,10,-5,9,1,-8,-1]]], dtype = "int8")#candidate|12915|(10, 7, 11)|const|int8
var_12916 = relay.var("var_12916", dtype = "int8", shape = (10, 7, 11))#candidate|12916|(10, 7, 11)|var|int8
bop_12917 = relay.not_equal(const_12915.astype('bool'), relay.reshape(var_12916.astype('bool'), relay.shape_of(const_12915))) # shape=(10, 7, 11)
uop_12920 = relay.acosh(bop_12917.astype('float32')) # shape=(10, 7, 11)
output = uop_12920
output2 = uop_12920
func_12934 = relay.Function([var_12916,], output)
mod['func_12934'] = func_12934
mod = relay.transform.InferType()(mod)
var_12935 = relay.var("var_12935", dtype = "int8", shape = (10, 7, 11))#candidate|12935|(10, 7, 11)|var|int8
output = func_12934(var_12935)
func_12936 = relay.Function([var_12935], output)
mutated_mod['func_12936'] = func_12936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7920_call = mod.get_global_var('func_7920')
func_7921_call = mutated_mod.get_global_var('func_7921')
call_12944 = relay.TupleGetItem(func_7920_call(), 1)
call_12945 = relay.TupleGetItem(func_7921_call(), 1)
output = call_12944
output2 = call_12945
func_12946 = relay.Function([], output)
mod['func_12946'] = func_12946
mod = relay.transform.InferType()(mod)
output = func_12946()
func_12947 = relay.Function([], output)
mutated_mod['func_12947'] = func_12947
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12961 = relay.const([[[6,10,6,-4,9,1,-8],[6,-2,-9,4,-10,-8,2],[-2,-6,6,-4,1,9,9],[-1,-6,10,-4,4,10,-1],[-4,2,5,-4,5,3,7],[5,-1,-2,5,-4,1,-7],[5,-1,10,-5,-1,-7,-7],[2,10,8,4,-10,-2,-8],[-4,3,-2,8,-8,-8,-2],[-5,3,10,5,-9,-10,7],[-5,4,-9,-1,-3,-2,2],[10,-5,2,4,-3,4,7],[-1,3,-9,-5,5,-9,5],[-9,-3,2,6,6,-9,-9],[3,4,-10,1,-5,-8,-4]],[[-9,8,7,-7,-7,-4,4],[-6,-4,-1,-6,-9,-2,5],[5,5,-8,1,4,4,-4],[-6,10,3,2,4,9,-5],[8,-3,7,8,-2,-9,-1],[-6,1,-3,-6,7,-4,-6],[-6,6,-10,8,6,3,7],[2,6,2,4,8,-4,7],[-8,3,-3,8,5,-3,2],[-10,-1,-4,2,4,-1,-3],[-9,-5,3,-1,-6,-2,-6],[5,-10,-6,7,7,6,-5],[-6,-6,-1,4,-10,2,5],[-10,-6,9,-9,-8,3,-6],[-9,-9,-9,1,-5,-4,1]],[[2,10,7,6,4,8,-10],[7,1,-6,10,5,-7,-8],[5,9,-5,9,4,5,9],[-2,-4,6,7,-8,-7,-10],[-1,-5,8,-6,-2,-5,10],[-6,3,9,-9,5,-5,6],[-3,-6,7,-3,-7,9,3],[8,4,-4,4,-4,-6,-2],[9,-5,-4,-7,6,7,-10],[-7,-8,6,-10,9,-4,10],[10,-3,10,3,2,-7,1],[-4,-10,-4,7,-2,-10,1],[-2,6,-5,-4,8,8,-7],[-10,9,-1,-6,-7,5,-10],[-8,1,-3,5,5,-10,-5]],[[4,-3,4,8,-1,10,-7],[-5,2,-7,-7,-1,8,-10],[-10,9,10,-10,-6,-10,5],[4,5,-1,5,3,10,-4],[1,-7,10,-8,-9,-7,-7],[9,6,-5,3,1,4,9],[9,10,-9,2,-4,2,-9],[6,5,-7,9,4,-8,1],[7,5,5,-6,4,-4,10],[-4,4,-6,-7,9,-7,-9],[6,-6,-10,-10,6,-9,-8],[1,-8,7,-4,8,8,-7],[-8,9,-4,8,-3,1,6],[2,-3,-2,-7,-3,-3,-2],[8,-5,6,4,-6,8,-1]],[[-1,-8,-1,-7,4,-1,6],[-7,5,2,6,2,9,-10],[-9,5,10,-6,-4,3,8],[-4,9,7,-9,-4,6,-2],[-5,-2,-7,-8,-10,-9,9],[4,-7,-4,-2,-2,7,-7],[-3,-7,-3,-7,-6,9,-1],[-2,-2,8,7,-8,2,-1],[8,-3,6,3,1,-2,-5],[4,-1,6,3,3,-5,-10],[-10,5,8,1,8,-5,-2],[-7,-10,-4,-9,2,-4,3],[-5,4,3,-3,7,-5,6],[5,7,-6,7,9,10,-10],[-8,4,6,-9,9,-10,-8]],[[3,-4,-5,-4,-9,-2,-5],[-2,9,-7,-3,2,4,8],[8,-6,1,1,1,6,4],[-10,2,-3,-2,-3,5,-9],[-7,-10,2,-5,-8,-8,10],[10,-3,5,2,6,10,1],[5,2,-8,4,-10,4,5],[-8,-5,1,9,-3,3,5],[9,7,-7,-3,-5,4,9],[-3,9,1,10,-3,-7,-9],[6,-4,-9,6,-3,-8,9],[4,-1,2,10,5,-5,-8],[5,-5,-1,-5,-1,6,-3],[10,8,7,3,-9,-3,3],[-3,2,-6,10,-7,8,7]],[[2,10,-9,8,-10,-7,3],[3,10,7,-5,-3,2,9],[8,6,7,5,-6,4,-5],[-5,3,-4,-4,-8,-6,4],[-1,-8,1,2,-1,4,10],[-5,10,-3,10,9,8,2],[8,-2,1,1,-7,9,-10],[7,-2,-4,4,7,-5,-7],[6,9,-7,5,10,-9,-9],[-4,3,10,6,8,-3,6],[-3,-3,6,3,10,3,-5],[8,3,6,7,-9,-10,-5],[-6,-1,3,10,-3,-3,2],[-6,8,-5,-7,-5,7,-7],[5,-9,2,9,-5,7,3]],[[-2,7,6,-3,-6,-9,5],[9,2,4,4,-5,-3,4],[-10,-1,-4,2,4,8,-4],[-3,5,-10,5,-2,2,-1],[-8,9,2,10,-8,3,-8],[4,-1,2,10,-7,-8,3],[8,8,-9,-6,7,-6,-10],[9,-3,9,-3,-2,-5,-7],[1,4,3,5,-9,2,9],[-4,-8,-7,7,5,-9,2],[-9,6,8,7,-1,5,5],[9,7,3,6,8,-7,5],[1,9,-6,-8,-4,10,-1],[-9,-4,10,-2,9,-4,3],[-10,-9,-8,1,-5,10,5]],[[-9,5,-3,-6,10,-8,8],[-6,5,-1,-6,-5,3,-5],[-1,3,5,6,6,-10,2],[7,-2,-8,8,-5,8,-9],[-10,-4,-5,1,-8,7,-8],[2,9,-9,4,-9,-9,-7],[4,8,10,-7,2,4,-4],[3,2,-4,-5,-1,10,-1],[4,-6,4,6,-7,-9,-2],[6,-6,10,4,-6,-4,-10],[-6,-5,-7,-3,-4,-4,-4],[9,-6,2,6,9,-5,-1],[-1,-5,-1,9,1,10,-1],[-6,9,-2,2,6,-5,8],[-9,1,1,7,8,4,6]],[[-7,-8,5,-10,-2,-1,10],[3,-8,-8,-2,-6,-5,-3],[-6,-10,-9,5,8,8,-6],[10,9,-6,8,7,-5,1],[9,-6,4,-5,-8,6,4],[8,5,7,-3,-10,-7,3],[1,-1,-7,-5,-6,-3,-1],[-10,4,-4,-6,-2,4,-10],[-2,2,-6,-4,-3,-3,9],[1,6,2,9,-9,-9,-4],[7,-3,-6,2,9,4,-5],[8,4,2,3,9,4,-9],[-1,7,8,6,-6,-5,-4],[-6,5,-3,-5,8,-10,4],[-5,8,-7,-5,-4,8,-1]],[[4,3,8,-4,-6,7,1],[-10,-3,9,4,-8,-2,2],[-2,-4,-2,-6,4,3,-3],[3,-10,-10,-8,6,-6,1],[-5,-7,-9,5,7,-4,-3],[10,-5,-9,-5,-10,7,-5],[8,-8,-10,-2,-7,10,8],[6,1,7,-8,3,-5,-6],[-6,-3,8,1,-8,7,-2],[1,3,1,-3,9,3,7],[-4,-10,6,7,7,-2,-1],[-2,9,2,1,5,-2,-5],[8,-4,-7,-5,10,-8,1],[5,2,6,-3,1,-4,5],[-3,-2,4,-5,2,5,3]],[[-8,5,10,-1,9,7,-7],[6,-6,4,-2,-3,3,-7],[7,4,-8,-9,6,-5,5],[5,-2,3,2,5,10,-10],[-5,-1,-9,-8,-4,5,10],[-7,1,-8,-4,8,-2,1],[5,3,10,-2,9,-6,-10],[4,-1,6,4,-3,-7,-6],[8,-9,1,-10,-5,10,4],[-6,-6,-4,-1,7,4,-4],[2,10,-9,10,-10,-9,-7],[-9,-4,5,5,-7,4,10],[5,-1,-3,-7,-9,-2,-9],[3,1,-7,9,7,5,-10],[9,7,3,-2,-6,-1,-8]]], dtype = "int64")#candidate|12961|(12, 15, 7)|const|int64
var_12962 = relay.var("var_12962", dtype = "int64", shape = (12, 15, 7))#candidate|12962|(12, 15, 7)|var|int64
bop_12963 = relay.logical_xor(const_12961.astype('int64'), relay.reshape(var_12962.astype('int64'), relay.shape_of(const_12961))) # shape=(12, 15, 7)
uop_12980 = relay.sqrt(bop_12963.astype('float64')) # shape=(12, 15, 7)
func_842_call = mod.get_global_var('func_842')
func_848_call = mutated_mod.get_global_var('func_848')
var_12995 = relay.var("var_12995", dtype = "float64", shape = (96,))#candidate|12995|(96,)|var|float64
const_12996 = relay.const([4.090067,3.622849,-1.885458,-5.804252,5.218365,1.366648,-4.688888,3.231451,8.353565,8.437094,-5.410897,2.975030,-0.121121,-9.731156,9.703110,0.381506,0.134484,0.624007,-4.357377,2.422919,-8.472701,-1.710033,2.541610,2.291616,-2.052741,4.516629,9.216315,-6.550099,8.990641,1.019412,-0.311908,2.430478,-0.990108,-3.790453,-8.124177,-6.626825,-9.713662,4.243007,-3.692201,-6.555190,-2.789319,-8.887247,-8.680753,8.196915,3.165077,-4.110398,9.803627,3.398036,9.937844,3.984297,8.993400,-7.571369,-8.334197,8.677194,-5.707554,7.447176,-6.656090,2.557782,-1.612751,-3.683133,7.950470,-4.057521,-2.501652,-4.586300,3.439973,3.103974,0.633875,-5.679864,6.025206,0.618632,3.910268,-0.468011,-2.703910,-0.943562,-0.177259,-5.692937,4.999363,9.610811,1.070414,2.033077,8.804267,5.477722,-4.499532,-1.148943,-8.014749,-4.668842,-0.370899,0.652081,-7.756471,-0.839085,-3.806759,-3.907868,5.353021,8.320568,-0.575134,2.772289,4.943508,-7.912741,-4.957705,4.596705,-0.247541,-2.009464,2.463792,8.961713,9.823372,-6.023978,4.351802,3.268389,-4.513311,5.502042,-9.412751,-0.070010,2.614490,4.697431,8.896203,-8.314808,-8.486108,0.869938,-3.539779,8.553558,-8.736946,3.675472,1.658867,-7.138289,6.811754,-0.850013,-1.787986,5.267900,0.889721,8.239224,-5.565566,2.317043,-8.758869,-6.923080,6.350628,-3.026271,0.777517,1.724499,-5.594411,3.417728,3.467571,4.717938,-1.048341,-6.435668,-4.921000,5.818550,0.663524,8.451454,4.132242,1.005112,-4.459560,-6.616966,5.298659,-7.559718,8.091047,-3.285988,6.126789,-2.455864,-8.641394,9.426563,-3.583809,1.511558,8.441195,2.806807,-3.976243,-8.595306,-6.133248,6.236633,-1.466162,5.598565,6.773385,7.430920,-5.089542,-0.964141,-4.572171,1.798940,-7.233908,-7.891909,7.482227,-2.934350,-5.827437,-4.989407,7.299003,2.030529,9.791758,2.176613,-5.042450,4.831745,-6.924317,5.724597,-0.619358,9.255451,-8.753620,-0.954438,7.640385,5.026400,4.441279,-8.398762,2.567368,8.309984,6.127996,4.626700,2.363316,-8.201623,1.633993,-6.959163,-1.126495,-3.655283,4.225137,-9.999727,-4.538211,7.448238,-4.009971,-4.789026,6.786128,-1.926208,3.158474,-2.836722,6.102485,-2.521451,-1.287998,-0.961836,1.057766,5.609041,9.629619,5.947216,-0.044446,-2.066605,6.961089,-6.684650,-1.343091,3.046783,8.073479,-9.758173,-1.440689,3.771255,3.784340,2.941582,-3.037460,4.811949,-7.180301,8.500731,7.865819,2.359033,6.609295,8.885678,8.673139,4.885199,-5.931314,4.097109,-3.185360,-1.644537,-8.550390,-9.874892,-9.780613,-5.131624,3.990504,9.888613,5.199447,4.123703,9.187324,-8.963697,1.348734,2.105150,6.716661,-2.228048,2.240197,7.892735,-9.232906,-4.460356,-8.663944,2.558256,8.695201,-5.390616,-4.733499,4.521164,1.293977,-6.218419,4.616852,-2.827263,-4.769692,-3.885386,9.596621,6.180423,-8.116394,3.850331,-4.893994,-4.246547,2.799231,9.142820,-9.945860,8.382248,-6.764640,-9.035968,9.866299,9.222185,0.882419,9.031830,5.474833,-7.848105,9.099258,-7.785384,-1.682759,0.728761,-3.696764,9.356372,4.871055,-9.718205,-3.261911,0.763692,5.506835,3.996355,-4.305836,-1.850082,3.963903,0.981609,-6.075754,8.384494,-6.944237,-8.851244,9.352233,2.952017,4.047796,-8.274036,-8.785528,7.097442,-0.744729,-1.470264,-4.400961,1.588932,0.940121,-7.835519,-6.793880,8.544684,-1.739231,8.335144,8.237155,-5.691455,-1.550124,5.950936,-5.719116,0.384583,0.030088,9.229686,-2.647436,-0.296593,-0.475433,4.510765,-2.361402,2.271639,-6.283662,-7.024873,-2.974183,-2.932966,7.611577,2.128104,7.897645,7.375661,9.612620,-5.982376,6.974834,6.625345,7.999704,-4.880935,3.789272,-5.183215,7.848373,-1.781294,3.066586,-3.750434,-6.553862,-5.188973,-4.007992,-6.879911,-2.040899,5.037973,8.678270,2.150553,3.345541,-8.778892,-2.057549,7.513521,1.981626,9.012143,-8.055093,-7.195106,4.714857,-5.206066,-5.061697,8.439609,6.756281,-2.626611,-0.107263,9.043868,5.071622,-4.234024,-8.541559,2.288921,8.118559,-9.669919,6.293650,-4.317405,3.797024,-0.159340,-6.035343,1.614078,7.659438,-2.817083,2.389904,3.146979,-4.514601,-9.818920,3.732941,-7.945515,-1.584714,3.715412,6.021849,9.964824,-0.788082,-9.789474,0.007079,9.514020,7.440756,-0.357048,6.211345,-7.453815,-7.568846,7.679477,-5.750083,-5.318886,-3.631316,-2.723999,-7.275161,4.078274,-7.198995,3.617175,3.308603,-1.253953,-3.084965,3.609023,-2.614631,5.169780,0.235859,4.623621,1.256930,-4.187528,5.842548,1.373214,-8.532643,-9.897031,6.724787,6.639757,-4.671335,8.180481,-5.192944,1.676992,-6.980068,2.331468,8.940592,-6.433894,0.340678,-9.149266,1.591797,-6.654074,-9.651697,-0.541307,-2.102911,-3.474797,2.623510,6.321895,0.885707,8.995640,-4.203455,6.716125,2.903110,-2.504681,-1.771354,7.485390,-8.506549,-9.513165,-8.548458,-9.433133,-1.750163,-6.042859,2.914399,2.047738,-9.215245,-9.600070,-7.626779,-5.142210,5.170167,-8.942404,2.244743,-0.860501,8.168156,6.748929,9.867726,-9.255396,-0.141641,-1.402668,-0.169079,-4.800655,-5.023179,3.598612,-2.650892,-4.955363,-8.405713,-3.707204,-2.879962,-4.291904,5.014788,2.348873,3.195399,-3.849370,-1.436224,2.051496,-1.291035,8.874233,7.612799,8.443689,-3.467594,6.289337,-3.934844,0.303563,-2.764559,-4.275893,1.111951,9.157550,4.857112,-7.933508,-4.345431,4.308261,-3.294005,7.720345,6.659793,1.256306,-3.132561,6.021991,-2.523099,2.924144,-4.331740,-5.015452,7.485207,-6.272091,9.320984,0.272010], dtype = "float32")#candidate|12996|(546,)|const|float32
const_12997 = relay.const([9.369811,5.503914,1.593427,7.890803,1.438261,3.155888,7.776102,9.149439,-9.202546,0.981264,4.927710,5.210115,-1.016833,-9.180687,8.808948,3.417004,-9.694535,7.268249,-5.730995,6.275569,5.309959,3.365483,7.493927,-8.949654], dtype = "float32")#candidate|12997|(24,)|const|float32
const_12998 = relay.const([2,-3,-1,-6,-4,-10,6,-8,9,5,-8,8,-4,-3,8,1,4,-10,8,9,-10,-4,7,3,-4,10,7,5,4,6,-4,1,-3,-2,6,-5,-2,-5,1,-5,-6,6,-2,7,-6,8,-2,-7,8,7,1,-2,-1,4,-5,-6,5,-6,-10,4,8,6,-9,-6,-2,-4,-3,10,3,5,-4,-1,-2,7,-2,7,-3,1,-8,10,7,5,-10,5,10,3,10,4,-1,-3,-1,2,-5,-5,-7,5,1,-6,-6,4,1,-1,-1,5,7,6,10,2,-10,-2,-2,-5,-8,3,3,1,5,9,8,-10,1,1,-6,1,-9,-5,10,3,-2,-2,-4,-1,7,-6,3,10,-4,7,3,7,1,-5,3,-6,4,10,-3,10,-10,-6,4,8,6,-9,-3,1,8,4,-5,6,10,-9,8,4,-8,10,-6,-2,-4,-9,7,3,-9,-7,-7,4,-9,-10,-4,7,-7,-4,5,-3,-6,8,-6,9,5,-8,8,-10], dtype = "int8")#candidate|12998|(192,)|const|int8
call_12994 = relay.TupleGetItem(func_842_call(relay.reshape(var_12995.astype('float64'), [16, 2, 3]), relay.reshape(const_12996.astype('float32'), [546,]), relay.reshape(const_12997.astype('float32'), [12, 2]), relay.reshape(const_12998.astype('int8'), [192,]), ), 0)
call_12999 = relay.TupleGetItem(func_848_call(relay.reshape(var_12995.astype('float64'), [16, 2, 3]), relay.reshape(const_12996.astype('float32'), [546,]), relay.reshape(const_12997.astype('float32'), [12, 2]), relay.reshape(const_12998.astype('int8'), [192,]), ), 0)
func_7872_call = mod.get_global_var('func_7872')
func_7874_call = mutated_mod.get_global_var('func_7874')
call_13003 = relay.TupleGetItem(func_7872_call(), 0)
call_13004 = relay.TupleGetItem(func_7874_call(), 0)
uop_13021 = relay.exp(const_12961.astype('float64')) # shape=(12, 15, 7)
func_3129_call = mod.get_global_var('func_3129')
func_3133_call = mutated_mod.get_global_var('func_3133')
var_13024 = relay.var("var_13024", dtype = "float32", shape = (280,))#candidate|13024|(280,)|var|float32
call_13023 = relay.TupleGetItem(func_3129_call(relay.reshape(const_12997.astype('float32'), [24,]), relay.reshape(var_13024.astype('float32'), [280,]), ), 1)
call_13025 = relay.TupleGetItem(func_3133_call(relay.reshape(const_12997.astype('float32'), [24,]), relay.reshape(var_13024.astype('float32'), [280,]), ), 1)
output = relay.Tuple([uop_12980,call_12994,var_12995,const_12996,const_12997,const_12998,call_13003,uop_13021,call_13023,var_13024,])
output2 = relay.Tuple([uop_12980,call_12999,var_12995,const_12996,const_12997,const_12998,call_13004,uop_13021,call_13025,var_13024,])
func_13027 = relay.Function([var_12962,var_12995,var_13024,], output)
mod['func_13027'] = func_13027
mod = relay.transform.InferType()(mod)
var_13028 = relay.var("var_13028", dtype = "int64", shape = (12, 15, 7))#candidate|13028|(12, 15, 7)|var|int64
var_13029 = relay.var("var_13029", dtype = "float64", shape = (96,))#candidate|13029|(96,)|var|float64
var_13030 = relay.var("var_13030", dtype = "float32", shape = (280,))#candidate|13030|(280,)|var|float32
output = func_13027(var_13028,var_13029,var_13030,)
func_13031 = relay.Function([var_13028,var_13029,var_13030,], output)
mutated_mod['func_13031'] = func_13031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4701_call = mod.get_global_var('func_4701')
func_4702_call = mutated_mod.get_global_var('func_4702')
call_13118 = func_4701_call()
call_13119 = func_4701_call()
output = relay.Tuple([call_13118,])
output2 = relay.Tuple([call_13119,])
func_13122 = relay.Function([], output)
mod['func_13122'] = func_13122
mod = relay.transform.InferType()(mod)
mutated_mod['func_13122'] = func_13122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13122_call = mutated_mod.get_global_var('func_13122')
call_13123 = func_13122_call()
output = call_13123
func_13124 = relay.Function([], output)
mutated_mod['func_13124'] = func_13124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6975_call = mod.get_global_var('func_6975')
func_6977_call = mutated_mod.get_global_var('func_6977')
call_13138 = relay.TupleGetItem(func_6975_call(), 0)
call_13139 = relay.TupleGetItem(func_6977_call(), 0)
func_9719_call = mod.get_global_var('func_9719')
func_9722_call = mutated_mod.get_global_var('func_9722')
var_13170 = relay.var("var_13170", dtype = "float64", shape = (378,))#candidate|13170|(378,)|var|float64
call_13169 = relay.TupleGetItem(func_9719_call(relay.reshape(var_13170.astype('float64'), [378,])), 2)
call_13171 = relay.TupleGetItem(func_9722_call(relay.reshape(var_13170.astype('float64'), [378,])), 2)
func_1502_call = mod.get_global_var('func_1502')
func_1504_call = mutated_mod.get_global_var('func_1504')
call_13180 = relay.TupleGetItem(func_1502_call(), 0)
call_13181 = relay.TupleGetItem(func_1504_call(), 0)
func_6564_call = mod.get_global_var('func_6564')
func_6566_call = mutated_mod.get_global_var('func_6566')
const_13196 = relay.const([-7.434885,8.883587,2.090591,3.795672,2.996845,-3.683383,-5.422237,4.688017,-2.139475,-6.483405,6.619931,-4.784254,-5.113649,5.312914,-2.157013,7.479161,-5.835595,3.830109,9.844173,-8.914683,-2.041142,-9.021820,0.227706,-2.426777,7.303469,-2.873812,-0.144592,-9.394591,0.881564,0.061585,3.087974,-5.156904,6.949223,5.302495,-0.184667,-5.775904], dtype = "float32")#candidate|13196|(36,)|const|float32
call_13195 = relay.TupleGetItem(func_6564_call(relay.reshape(const_13196.astype('float32'), [3, 12])), 6)
call_13197 = relay.TupleGetItem(func_6566_call(relay.reshape(const_13196.astype('float32'), [3, 12])), 6)
output = relay.Tuple([call_13138,call_13169,var_13170,call_13180,call_13195,const_13196,])
output2 = relay.Tuple([call_13139,call_13171,var_13170,call_13181,call_13197,const_13196,])
func_13208 = relay.Function([var_13170,], output)
mod['func_13208'] = func_13208
mod = relay.transform.InferType()(mod)
mutated_mod['func_13208'] = func_13208
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13209 = relay.var("var_13209", dtype = "float64", shape = (378,))#candidate|13209|(378,)|var|float64
func_13208_call = mutated_mod.get_global_var('func_13208')
call_13210 = func_13208_call(var_13209)
output = call_13210
func_13211 = relay.Function([var_13209], output)
mutated_mod['func_13211'] = func_13211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7855_call = mod.get_global_var('func_7855')
func_7857_call = mutated_mod.get_global_var('func_7857')
call_13246 = relay.TupleGetItem(func_7855_call(), 1)
call_13247 = relay.TupleGetItem(func_7857_call(), 1)
uop_13259 = relay.tan(call_13246.astype('float64')) # shape=(2, 9, 11)
uop_13261 = relay.tan(call_13247.astype('float64')) # shape=(2, 9, 11)
output = relay.Tuple([uop_13259,])
output2 = relay.Tuple([uop_13261,])
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
