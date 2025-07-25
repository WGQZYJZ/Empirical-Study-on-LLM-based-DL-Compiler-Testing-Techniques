import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_41 = relay.var("var_41", dtype = "float64", shape = (12, 2, 10))#candidate|41|(12, 2, 10)|var|float64
uop_42 = relay.atan(var_41.astype('float64')) # shape=(12, 2, 10)
bop_47 = relay.bitwise_or(var_41.astype('uint8'), relay.reshape(uop_42.astype('uint8'), relay.shape_of(var_41))) # shape=(12, 2, 10)
output = relay.Tuple([bop_47,])
output2 = relay.Tuple([bop_47,])
func_52 = relay.Function([var_41,], output)
mod['func_52'] = func_52
mod = relay.transform.InferType()(mod)
var_53 = relay.var("var_53", dtype = "float64", shape = (12, 2, 10))#candidate|53|(12, 2, 10)|var|float64
output = func_52(var_53)
func_54 = relay.Function([var_53], output)
mutated_mod['func_54'] = func_54
mutated_mod = relay.transform.InferType()(mutated_mod)
var_148 = relay.var("var_148", dtype = "bool", shape = ())#candidate|148|()|var|bool
const_149 = relay.const([[[False,True,True,True,False,False,True,False,True,True,False,True,False,False,False]],[[True,True,True,False,True,False,False,False,False,False,False,True,True,True,False]],[[True,True,True,False,False,True,False,True,True,False,False,True,True,False,True]],[[False,False,False,True,False,False,True,False,False,True,False,True,False,True,False]],[[False,False,True,True,True,True,False,True,False,True,True,False,False,True,True]],[[False,True,True,False,False,True,False,True,True,True,False,True,False,False,True]],[[False,True,True,True,False,False,False,True,False,False,False,True,False,True,False]]], dtype = "bool")#candidate|149|(7, 1, 15)|const|bool
bop_150 = relay.logical_or(var_148.astype('bool'), const_149.astype('bool')) # shape=(7, 1, 15)
output = relay.Tuple([bop_150,])
output2 = relay.Tuple([bop_150,])
func_174 = relay.Function([var_148,], output)
mod['func_174'] = func_174
mod = relay.transform.InferType()(mod)
var_175 = relay.var("var_175", dtype = "bool", shape = ())#candidate|175|()|var|bool
output = func_174(var_175)
func_176 = relay.Function([var_175], output)
mutated_mod['func_176'] = func_176
mutated_mod = relay.transform.InferType()(mutated_mod)
const_277 = relay.const([[[0.770825,-4.139753,7.159789,-0.211036,2.958456,-0.974999,1.387141,-9.426639,-6.564091,5.756467,7.006048,-6.517768,8.255631,9.535616,-4.590620]],[[6.509940,-8.368304,0.149079,1.873773,-3.311044,3.949612,1.348612,-1.024394,-1.960780,-3.425375,-3.516186,1.652798,0.329819,2.179490,-5.391520]],[[6.445916,1.190046,1.731112,6.769648,-1.809796,2.978772,-0.194913,-1.594494,-7.115550,-0.098657,4.013354,-0.210989,2.572294,9.252520,-3.102630]],[[-2.132207,-7.950455,5.350932,-0.799031,-3.287888,9.360270,-6.273070,-0.524440,-0.077530,-8.869243,4.398363,-4.643040,-2.678259,4.488774,-2.630793]],[[9.927504,-1.878118,-7.320110,-8.695971,-4.321778,6.557619,-1.648064,-3.386257,5.119124,-1.066619,4.489215,8.950435,3.694858,8.732719,1.734298]],[[8.027835,-4.835503,-1.528610,4.981519,0.903079,1.725249,5.717128,-1.521347,-1.149536,6.523520,6.927199,4.011944,-9.088792,9.221209,1.595594]],[[9.210228,9.052379,-8.030889,-1.740607,-0.324816,-9.698299,-0.203730,-3.551563,1.280720,-8.936647,3.930047,2.577389,-3.658233,1.803800,2.200456]],[[9.557480,1.592210,-7.340784,-6.809346,-6.377293,-0.257196,7.427236,-0.048320,7.098063,-1.736093,-4.399710,-5.991067,-5.149324,5.468841,-1.666371]],[[8.488254,2.514571,-5.367970,-2.098822,-0.909530,-7.265049,8.593269,-0.272457,9.260723,2.291171,5.926430,2.036931,0.296390,2.780421,8.519940]]], dtype = "float64")#candidate|277|(9, 1, 15)|const|float64
const_278 = relay.const([[[-7.735959,-8.686824,-2.805254,1.791574,7.966051,-6.797136,-3.220143,-5.344965,-6.507624,-7.448881,4.903121,2.226967,-0.557255,-5.806497,3.573967]],[[7.771448,6.724197,9.500737,-2.736771,-5.717155,6.793833,1.215864,-3.042045,-7.369857,-6.026698,-1.993631,-3.197575,-8.190157,4.318132,9.321953]],[[-4.514355,-8.685742,-4.409525,7.749306,-0.755333,0.693172,6.839211,5.120967,-6.467878,-9.804287,-1.517274,-6.006481,-6.398096,-4.759109,2.856391]],[[5.763333,-0.728624,8.452845,8.553654,9.955203,3.352401,6.821863,-1.403182,-8.961192,-6.843252,2.162901,-7.917237,-8.570823,-1.775259,-3.407024]],[[-7.488073,5.557659,2.529826,6.289512,0.301963,-0.690897,2.039598,2.229099,-6.505402,-1.953747,-6.344636,-0.892308,3.151936,-2.112895,1.407912]],[[8.604890,-2.371855,-9.036852,-9.844850,-6.854466,-0.873601,-8.049790,-3.713686,7.062115,3.731809,-6.510108,1.860100,-2.449675,9.944594,-9.318935]],[[0.754242,-9.443187,-5.683325,0.060521,-2.380023,0.555855,-6.705895,9.079108,0.528902,-3.676720,-3.539867,6.578531,2.295532,6.473260,-4.523749]],[[5.573228,7.500684,9.827986,-9.247003,-9.438202,-4.094587,4.617394,9.995879,3.198110,-2.284633,-0.419054,-2.094615,-0.054612,6.668316,-2.008243]],[[-1.060723,-4.265733,9.929354,7.683937,-0.424694,3.182081,6.319284,-3.684432,3.851930,-1.543581,9.415014,-1.958759,-5.317184,0.083520,-6.524390]]], dtype = "float64")#candidate|278|(9, 1, 15)|const|float64
bop_279 = relay.power(const_277.astype('float64'), relay.reshape(const_278.astype('float64'), relay.shape_of(const_277))) # shape=(9, 1, 15)
bop_282 = relay.greater_equal(bop_279.astype('bool'), relay.reshape(const_278.astype('bool'), relay.shape_of(bop_279))) # shape=(9, 1, 15)
func_52_call = mod.get_global_var('func_52')
func_54_call = mutated_mod.get_global_var('func_54')
const_290 = relay.const([8.105470,-4.302579,-4.556642,-0.097599,-4.250260,6.873684,1.998659,7.041375,-8.114501,8.296882,5.564362,6.288345,-7.825696,3.290960,-7.478162,5.664855,0.237613,0.010063,2.331434,-7.205214,-5.947539,-5.858686,7.253138,-4.934256,-1.059483,-5.458071,-6.826891,-5.509061,2.728121,-1.705189,-4.056081,2.803806,-9.975702,9.816015,5.670273,3.936491,-4.524149,8.561633,-2.897206,4.315267,9.005826,-5.233101,4.217271,-6.307277,-4.605464,-0.413969,-2.557788,6.195944,-2.413309,6.771509,-9.406295,0.707827,-9.891256,2.699986,8.122571,-1.113151,-0.171883,-3.125136,9.967795,3.495247,-1.033890,6.732485,5.048249,4.017364,3.368249,2.179943,3.917048,-3.824570,8.243549,-3.757077,6.117233,5.198885,9.470849,5.653308,-4.598091,9.784724,9.766667,-4.102022,6.271609,-4.639104,-4.009353,-7.689542,6.810490,4.394820,-9.870574,5.189505,-1.750379,-2.582443,-4.586229,8.051794,-2.111302,2.969262,9.186734,-9.560249,9.387954,4.945809,1.959631,-9.691355,3.022705,0.785979,4.553555,0.319191,-3.793030,-5.021999,3.257864,9.377106,-5.216236,2.129862,-6.638417,-3.065008,0.409848,2.353680,8.321802,2.402944,-7.247215,9.990022,2.399025,0.037159,-4.109723,-8.982604,0.839759,3.913417,7.762084,0.725082,-9.874978,3.667731,-6.664289,-9.104941,-6.104870,-3.539765,0.133257,0.494143,-8.163947,-6.283069,-6.746688,-4.246851,-4.352796,8.551860,1.141430,-9.238720,-8.158130,5.705096,-7.230726,-7.431139,4.366031,0.323643,-8.206649,9.490564,-8.694831,0.692670,-1.358385,-2.449090,7.279476,-4.142664,3.559701,3.872927,8.840876,-8.402095,-7.893887,-3.507904,5.861215,-1.594006,-4.620890,-5.033099,3.032109,6.998167,8.978036,6.202622,2.067627,8.370124,-8.099651,-8.698448,3.839125,0.042204,-1.089269,1.622966,-3.438842,6.228674,6.751824,0.303819,-5.578642,7.838466,-4.546597,-7.881195,-6.575148,-8.063007,-7.697553,-8.644968,8.567213,-8.024287,-0.167876,6.273880,0.785287,4.344552,-5.113235,-8.092663,-9.277010,4.889704,-6.948196,-4.288799,5.767893,3.586584,-2.762373,-2.877605,4.789869,2.411621,-7.827150,-2.452824,0.279418,4.715625,-5.071567,-2.133918,3.176321,-1.936724,-2.862147,-8.668755,5.118154,0.770677,-8.751025,-7.547524,-2.210817,8.418942,-8.438013,2.453150,5.108310,-0.887231,-2.907899,-4.077655,-6.220879,8.392680,-3.025206,-5.887768,8.293566,3.726819,8.761148,1.569086,7.599462,3.786091,8.211668,1.661751], dtype = "float64")#candidate|290|(240,)|const|float64
call_289 = relay.TupleGetItem(func_52_call(relay.reshape(const_290.astype('float64'), [12, 2, 10])), 0)
call_291 = relay.TupleGetItem(func_54_call(relay.reshape(const_290.astype('float64'), [12, 2, 10])), 0)
bop_299 = relay.logical_and(bop_282.astype('bool'), relay.reshape(bop_279.astype('bool'), relay.shape_of(bop_282))) # shape=(9, 1, 15)
output = relay.Tuple([call_289,const_290,bop_299,])
output2 = relay.Tuple([call_291,const_290,bop_299,])
func_303 = relay.Function([], output)
mod['func_303'] = func_303
mod = relay.transform.InferType()(mod)
output = func_303()
func_304 = relay.Function([], output)
mutated_mod['func_304'] = func_304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_305 = relay.TupleGetItem(func_303_call(), 2)
call_306 = relay.TupleGetItem(func_304_call(), 2)
const_317 = relay.const([[[True,True,False,True,True,True,False,False,True,True,True,False,True,True,True],[True,True,True,False,True,False,False,False,True,False,False,True,True,True,False],[True,False,True,False,False,False,True,False,True,False,True,False,False,True,False],[False,False,True,True,False,False,True,False,False,False,False,False,True,True,True],[False,True,False,True,True,False,False,False,False,True,True,False,True,True,True],[True,True,True,False,True,True,True,False,True,True,True,True,False,False,True],[True,False,False,True,False,True,True,False,True,False,True,False,False,False,False],[True,False,True,False,False,False,True,True,True,False,True,False,True,True,False],[False,False,True,False,False,True,True,True,True,True,True,False,True,True,False],[True,False,False,True,False,True,True,True,False,False,True,True,False,True,False],[True,True,True,False,False,True,True,True,False,False,False,False,False,False,True],[False,True,False,True,False,False,False,False,False,False,False,True,False,True,False]],[[False,False,False,True,False,False,False,True,True,True,True,False,True,True,False],[False,True,True,False,False,False,True,False,False,True,True,False,False,True,True],[True,True,True,True,True,True,True,True,False,False,False,True,False,True,False],[False,False,False,False,False,False,False,True,True,False,False,False,False,True,True],[False,False,False,True,True,True,True,False,True,True,False,True,True,True,True],[True,True,True,True,True,True,False,True,True,True,True,True,True,False,False],[False,False,False,False,True,True,False,False,True,True,False,False,False,True,True],[True,False,False,False,False,False,False,False,True,True,True,True,False,False,True],[True,False,True,True,False,False,True,False,True,False,True,True,False,False,False],[True,True,False,False,False,False,False,False,False,True,True,True,False,True,True],[True,False,True,False,False,False,True,True,False,False,True,False,True,False,False],[True,True,True,True,True,True,False,True,True,False,True,False,False,True,False]],[[True,True,False,True,True,False,True,False,True,True,False,True,True,True,True],[True,False,False,True,False,False,False,False,True,False,False,False,False,False,False],[False,False,True,True,True,False,True,False,True,True,True,True,False,True,True],[True,False,True,True,True,True,True,False,True,True,False,False,True,False,False],[True,True,False,False,False,True,True,True,True,False,False,True,True,False,False],[False,True,False,False,True,False,True,False,False,True,True,False,True,True,False],[True,False,True,False,True,True,True,False,True,True,False,True,False,True,False],[False,False,True,False,False,False,False,True,True,False,False,False,False,True,True],[True,True,False,False,True,True,False,False,True,True,True,True,False,True,False],[False,True,False,False,False,False,False,False,False,True,True,False,False,True,False],[True,False,True,True,True,False,False,True,False,True,False,False,False,False,True],[True,True,True,True,True,True,False,True,True,False,True,False,False,True,False]],[[False,False,False,True,False,True,True,False,False,False,False,False,False,False,True],[True,True,False,False,True,True,True,True,False,True,True,True,True,True,False],[True,False,True,False,True,True,True,True,True,False,True,True,False,True,False],[True,False,True,True,True,False,False,False,True,True,True,False,False,True,False],[True,False,False,False,False,True,True,False,False,False,False,True,False,False,False],[False,False,True,True,True,False,False,False,False,True,True,False,False,True,True],[False,False,True,False,False,False,True,True,False,False,False,False,True,False,False],[False,False,False,True,True,False,True,True,False,True,True,True,True,True,False],[False,True,True,False,True,True,False,False,True,False,False,True,False,False,True],[False,False,True,True,True,False,True,False,False,True,True,True,False,True,False],[False,True,True,True,True,False,True,True,False,False,True,True,True,True,True],[False,False,True,True,True,False,True,False,False,True,True,True,False,True,False]],[[False,True,False,True,True,True,True,False,True,False,False,False,True,True,False],[False,True,False,True,False,True,True,True,True,True,True,False,False,True,True],[True,False,False,True,True,True,False,True,True,True,True,True,False,False,False],[False,False,True,False,True,True,True,False,True,False,True,False,False,True,True],[True,False,True,True,True,True,True,False,False,False,True,True,False,True,True],[False,True,True,False,True,False,True,False,False,False,False,True,False,False,False],[False,True,True,True,True,False,False,False,False,False,False,False,True,False,True],[False,True,True,True,True,False,True,False,True,True,True,True,False,True,False],[True,True,True,False,True,False,False,True,False,True,False,True,True,True,True],[False,False,False,True,True,True,False,True,False,True,False,True,False,True,False],[False,False,False,False,False,True,False,False,False,True,True,False,False,False,False],[True,True,False,False,False,True,True,False,False,True,True,True,False,False,False]],[[True,False,False,True,False,False,False,True,False,False,False,False,True,False,False],[True,True,True,True,True,False,False,True,False,True,False,False,False,True,False],[False,False,False,False,True,True,False,True,False,False,True,False,False,False,False],[True,True,True,False,False,True,False,True,False,True,False,False,True,False,True],[True,False,True,True,False,False,False,False,True,False,False,True,False,True,True],[False,False,True,False,False,True,True,True,False,True,False,False,True,True,False],[True,False,False,False,True,False,True,False,False,False,False,True,True,True,False],[True,True,False,False,True,False,True,False,True,False,True,True,False,True,False],[True,False,False,True,False,False,False,True,False,False,False,False,True,True,True],[True,False,True,True,False,False,False,False,True,True,False,False,True,False,True],[True,True,True,False,True,False,False,True,True,False,True,True,False,True,True],[False,False,True,True,False,False,True,False,False,False,True,False,True,False,False]],[[False,False,False,False,False,True,False,False,False,True,False,True,True,False,False],[False,False,True,True,True,True,True,True,True,True,True,False,True,False,True],[False,True,True,False,True,True,True,True,True,True,False,True,False,True,True],[True,True,False,False,True,True,True,False,False,False,False,False,False,True,False],[True,True,True,False,True,False,True,False,True,False,True,False,True,False,True],[True,True,True,True,True,False,False,False,False,True,False,False,True,False,False],[True,False,True,True,False,True,True,False,True,True,False,True,True,False,True],[False,True,False,True,False,True,True,False,True,False,True,True,False,False,True],[False,False,True,False,True,False,True,False,False,False,True,False,True,False,False],[False,True,True,False,False,True,True,False,False,False,False,True,True,False,False],[True,True,False,False,True,True,False,False,True,False,False,True,True,False,True],[True,False,False,True,True,True,False,False,True,False,True,True,False,False,True]],[[False,True,False,False,False,True,True,False,True,False,True,False,True,False,False],[True,True,False,True,False,True,False,True,False,True,True,True,False,True,True],[False,True,True,False,True,True,False,False,True,True,True,False,True,False,False],[True,True,False,False,True,False,True,True,True,True,True,True,False,True,False],[False,True,False,True,False,True,False,False,False,True,True,True,False,True,True],[False,False,True,False,False,False,True,False,True,False,True,False,True,False,False],[False,False,True,False,True,True,True,True,True,True,False,True,False,False,False],[False,True,False,True,True,True,True,False,True,False,True,False,True,False,False],[True,False,False,False,False,True,False,False,False,True,True,True,False,False,True],[False,False,False,True,True,False,False,False,False,True,False,True,True,True,False],[False,False,False,False,True,True,False,True,True,False,False,False,True,True,False],[True,True,False,True,False,True,True,False,True,False,True,False,True,True,True]],[[True,True,False,False,True,True,True,True,False,False,False,False,False,True,True],[True,False,True,True,False,True,True,True,False,False,True,True,False,True,False],[False,False,True,False,False,True,True,True,False,True,True,False,True,False,False],[True,True,False,False,False,False,True,True,False,True,False,True,True,False,False],[True,False,True,True,False,True,False,True,True,False,False,False,True,False,False],[True,True,True,True,True,False,False,False,True,False,False,True,True,True,False],[False,False,False,True,True,True,False,True,False,True,False,True,False,True,True],[False,False,False,False,True,True,False,True,True,True,True,True,True,True,False],[True,True,True,True,False,False,False,False,False,True,False,False,False,False,True],[True,False,True,True,False,False,False,False,False,True,False,True,True,True,False],[True,False,True,False,True,True,True,False,False,True,True,False,True,True,False],[False,False,False,True,True,True,True,True,True,True,False,True,True,True,False]]], dtype = "bool")#candidate|317|(9, 12, 15)|const|bool
bop_318 = relay.left_shift(call_305.astype('int64'), const_317.astype('int64')) # shape=(9, 12, 15)
bop_321 = relay.left_shift(call_306.astype('int64'), const_317.astype('int64')) # shape=(9, 12, 15)
output = bop_318
output2 = bop_321
func_325 = relay.Function([], output)
mod['func_325'] = func_325
mod = relay.transform.InferType()(mod)
output = func_325()
func_326 = relay.Function([], output)
mutated_mod['func_326'] = func_326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_346 = relay.TupleGetItem(func_303_call(), 0)
call_347 = relay.TupleGetItem(func_304_call(), 0)
func_174_call = mod.get_global_var('func_174')
func_176_call = mutated_mod.get_global_var('func_176')
var_388 = relay.var("var_388", dtype = "bool", shape = ())#candidate|388|()|var|bool
call_387 = relay.TupleGetItem(func_174_call(relay.reshape(var_388.astype('bool'), [])), 0)
call_389 = relay.TupleGetItem(func_176_call(relay.reshape(var_388.astype('bool'), [])), 0)
func_174_call = mod.get_global_var('func_174')
func_176_call = mutated_mod.get_global_var('func_176')
call_390 = relay.TupleGetItem(func_174_call(relay.reshape(var_388.astype('bool'), [])), 0)
call_391 = relay.TupleGetItem(func_176_call(relay.reshape(var_388.astype('bool'), [])), 0)
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_393 = func_325_call()
call_394 = func_325_call()
func_52_call = mod.get_global_var('func_52')
func_54_call = mutated_mod.get_global_var('func_54')
call_398 = relay.TupleGetItem(func_52_call(relay.reshape(call_346.astype('float64'), [12, 2, 10])), 0)
call_399 = relay.TupleGetItem(func_54_call(relay.reshape(call_346.astype('float64'), [12, 2, 10])), 0)
output = relay.Tuple([call_346,call_387,var_388,call_390,call_393,call_398,])
output2 = relay.Tuple([call_347,call_389,var_388,call_391,call_394,call_399,])
func_408 = relay.Function([var_388,], output)
mod['func_408'] = func_408
mod = relay.transform.InferType()(mod)
mutated_mod['func_408'] = func_408
mutated_mod = relay.transform.InferType()(mutated_mod)
var_409 = relay.var("var_409", dtype = "bool", shape = ())#candidate|409|()|var|bool
func_408_call = mutated_mod.get_global_var('func_408')
call_410 = func_408_call(var_409)
output = call_410
func_411 = relay.Function([var_409], output)
mutated_mod['func_411'] = func_411
mutated_mod = relay.transform.InferType()(mutated_mod)
var_459 = relay.var("var_459", dtype = "float32", shape = (11, 6, 13))#candidate|459|(11, 6, 13)|var|float32
var_460 = relay.var("var_460", dtype = "float32", shape = (11, 6, 13))#candidate|460|(11, 6, 13)|var|float32
bop_461 = relay.not_equal(var_459.astype('bool'), relay.reshape(var_460.astype('bool'), relay.shape_of(var_459))) # shape=(11, 6, 13)
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_475 = func_325_call()
call_476 = func_325_call()
func_52_call = mod.get_global_var('func_52')
func_54_call = mutated_mod.get_global_var('func_54')
var_482 = relay.var("var_482", dtype = "float64", shape = (240, 1))#candidate|482|(240, 1)|var|float64
call_481 = relay.TupleGetItem(func_52_call(relay.reshape(var_482.astype('float64'), [12, 2, 10])), 0)
call_483 = relay.TupleGetItem(func_54_call(relay.reshape(var_482.astype('float64'), [12, 2, 10])), 0)
output = relay.Tuple([bop_461,call_475,call_481,var_482,])
output2 = relay.Tuple([bop_461,call_476,call_483,var_482,])
func_493 = relay.Function([var_459,var_460,var_482,], output)
mod['func_493'] = func_493
mod = relay.transform.InferType()(mod)
var_494 = relay.var("var_494", dtype = "float32", shape = (11, 6, 13))#candidate|494|(11, 6, 13)|var|float32
var_495 = relay.var("var_495", dtype = "float32", shape = (11, 6, 13))#candidate|495|(11, 6, 13)|var|float32
var_496 = relay.var("var_496", dtype = "float64", shape = (240, 1))#candidate|496|(240, 1)|var|float64
output = func_493(var_494,var_495,var_496,)
func_497 = relay.Function([var_494,var_495,var_496,], output)
mutated_mod['func_497'] = func_497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_508 = relay.TupleGetItem(func_303_call(), 1)
call_509 = relay.TupleGetItem(func_304_call(), 1)
output = call_508
output2 = call_509
func_514 = relay.Function([], output)
mod['func_514'] = func_514
mod = relay.transform.InferType()(mod)
mutated_mod['func_514'] = func_514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_514_call = mutated_mod.get_global_var('func_514')
call_515 = func_514_call()
output = call_515
func_516 = relay.Function([], output)
mutated_mod['func_516'] = func_516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_514_call = mod.get_global_var('func_514')
func_516_call = mutated_mod.get_global_var('func_516')
call_575 = func_514_call()
call_576 = func_514_call()
var_587 = relay.var("var_587", dtype = "float64", shape = (240,))#candidate|587|(240,)|var|float64
bop_588 = relay.maximum(call_575.astype('int8'), relay.reshape(var_587.astype('int8'), relay.shape_of(call_575))) # shape=(240,)
bop_591 = relay.maximum(call_576.astype('int8'), relay.reshape(var_587.astype('int8'), relay.shape_of(call_576))) # shape=(240,)
func_52_call = mod.get_global_var('func_52')
func_54_call = mutated_mod.get_global_var('func_54')
call_594 = relay.TupleGetItem(func_52_call(relay.reshape(var_587.astype('float64'), [12, 2, 10])), 0)
call_595 = relay.TupleGetItem(func_54_call(relay.reshape(var_587.astype('float64'), [12, 2, 10])), 0)
output = relay.Tuple([bop_588,call_594,])
output2 = relay.Tuple([bop_591,call_595,])
func_607 = relay.Function([var_587,], output)
mod['func_607'] = func_607
mod = relay.transform.InferType()(mod)
var_608 = relay.var("var_608", dtype = "float64", shape = (240,))#candidate|608|(240,)|var|float64
output = func_607(var_608)
func_609 = relay.Function([var_608], output)
mutated_mod['func_609'] = func_609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_617 = func_325_call()
call_618 = func_325_call()
func_52_call = mod.get_global_var('func_52')
func_54_call = mutated_mod.get_global_var('func_54')
const_639 = relay.const([-5.075053,9.497542,8.412756,-3.548935,-4.974361,-2.843514,6.930202,5.970204,-5.568756,-4.725305,8.487731,-5.151680,-2.854258,-2.701602,6.461765,-6.617975,2.004135,-7.883010,-9.185186,-4.912283,-1.110121,-4.012407,8.551640,1.247724,1.925330,-3.464087,8.007639,6.585018,-3.698205,6.417827,2.360305,4.930773,2.122791,0.109648,-0.009090,7.377575,1.620237,7.028143,5.149993,-4.660001,-3.984719,7.735867,2.307957,6.499626,-8.560302,1.182973,7.178981,-8.941716,5.120846,-7.987037,-8.515600,-5.284608,7.118440,-9.278355,3.898143,1.773641,4.187602,7.417951,1.406075,-9.758563,2.103405,3.129851,0.416071,-2.355128,-5.227160,-2.253811,-0.168769,-0.048306,-4.922952,-7.098927,7.480309,1.795541,-4.788235,-7.131274,-0.502098,7.188429,-4.547522,-7.533153,-4.680880,-1.777220,2.902276,0.882785,-8.779429,7.779790,-6.360471,-6.958608,-8.370795,-7.366719,-9.767649,-1.566711,-6.146124,-8.429569,7.330522,-9.224339,1.217632,-5.671401,3.448886,-1.482546,6.354516,9.158149,8.579487,7.732274,5.826375,-0.135333,-4.562030,-4.703921,-2.950419,-9.584541,7.477867,-9.682644,2.460599,3.892906,-8.520951,-8.316691,-9.530244,-8.803131,5.967639,3.947363,8.852498,-2.165088,-3.007101,-2.373486,-4.468857,-5.202052,2.769417,-3.061687,1.744917,-8.251953,-2.087493,7.809124,-9.966943,-1.774836,-8.188002,-5.397760,-5.547676,2.519871,-2.883343,0.940538,-6.520075,-3.240193,-7.042150,1.369905,3.242871,-7.901931,-7.674495,-8.528792,2.559715,5.387574,-3.332804,1.217886,-8.243985,0.076586,5.564485,4.178979,2.227666,0.328528,9.616064,7.999767,-9.338321,-8.007096,-3.216300,5.911677,8.440161,7.480140,3.273592,-6.897523,3.240254,-7.838148,3.930650,6.026767,8.988395,-1.927265,4.696978,1.189626,8.510771,-6.811159,-9.922352,3.925498,-6.459839,0.848673,-1.342578,-7.098878,-0.242660,-0.703667,-3.809281,-0.864409,-8.790204,-3.501129,-6.319771,-2.650061,6.261471,4.726711,-8.808425,-3.065169,7.788244,-7.757415,7.075924,-9.774009,6.377538,6.336648,-5.318198,-7.108115,9.108678,-2.503012,-7.245332,6.837123,6.136955,-8.738664,-2.345386,3.850366,-9.342338,2.060855,-0.294435,8.808673,-1.188772,9.039798,-1.825096,9.328408,2.402433,-8.300098,-0.462422,0.699088,-8.891372,-8.208962,-9.861350,1.201406,5.782737,8.469379,-9.128273,-5.762888,2.530200,5.959158,5.164814,2.322610,-9.720599,-4.022401,-7.677998,-2.256005,4.000722,8.432366], dtype = "float64")#candidate|639|(240,)|const|float64
call_638 = relay.TupleGetItem(func_52_call(relay.reshape(const_639.astype('float64'), [12, 2, 10])), 0)
call_640 = relay.TupleGetItem(func_54_call(relay.reshape(const_639.astype('float64'), [12, 2, 10])), 0)
output = relay.Tuple([call_617,call_638,const_639,])
output2 = relay.Tuple([call_618,call_640,const_639,])
func_641 = relay.Function([], output)
mod['func_641'] = func_641
mod = relay.transform.InferType()(mod)
mutated_mod['func_641'] = func_641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_641_call = mutated_mod.get_global_var('func_641')
call_642 = func_641_call()
output = call_642
func_643 = relay.Function([], output)
mutated_mod['func_643'] = func_643
mutated_mod = relay.transform.InferType()(mutated_mod)
const_688 = relay.const([[[8,1,1,6,4,10,8,6,-10,10,10],[3,-6,4,-3,3,2,-5,7,-8,-5,-4],[-10,3,-1,-7,6,5,-2,1,-10,9,8],[3,-5,8,-9,-1,1,10,-8,5,8,-5],[-8,10,-3,-8,-10,8,-3,-5,7,1,1],[-1,10,-10,5,1,-6,-1,-9,-9,3,-6],[4,-9,7,-10,-3,7,5,2,-5,-3,-3],[7,5,-2,-5,-5,8,-1,-3,-3,-10,-8]],[[8,-6,2,-3,6,-10,9,-9,8,5,-7],[-1,7,-7,-6,5,4,8,-1,-4,4,7],[-3,10,-2,7,1,-8,-6,7,-9,-6,4],[-2,7,-1,7,4,6,-3,-7,6,10,8],[10,-8,8,3,-7,4,-10,-5,-4,-8,1],[7,-4,7,8,2,1,-8,-3,8,7,-6],[-8,5,-7,10,-8,7,-1,-8,2,-8,1],[1,-8,-7,-2,5,1,-3,5,-6,2,5]],[[-10,4,-6,-4,-10,-4,-5,-7,-2,-8,-10],[-3,6,-10,-5,-2,9,-8,10,-5,-8,-9],[9,-1,-6,-6,-1,3,-8,-6,9,9,-3],[4,-8,4,-7,-10,-8,-7,-1,-5,2,2],[3,3,5,10,9,-3,-5,3,-1,6,4],[-6,-8,9,-8,-8,-8,-3,-4,-1,8,-8],[-3,5,-5,-1,-6,-6,-9,2,6,10,-2],[-5,7,9,-1,10,-9,-6,-6,5,-8,-6]],[[-6,6,-2,-5,1,-3,7,-6,9,4,9],[-4,9,-8,-10,5,5,-7,-6,-3,2,5],[-6,-10,7,4,-6,-2,10,3,6,-8,-7],[-10,-7,2,-7,-1,-10,-9,-6,4,5,-8],[-5,7,-9,4,1,-3,-7,10,-3,-10,-3],[-1,-3,-3,-10,5,2,-9,-8,8,-9,8],[5,-3,-8,-5,-9,9,1,10,3,-7,9],[5,-10,-7,-4,-6,-4,9,-9,4,-1,2]],[[7,5,9,-2,-9,6,-9,-8,-1,-2,-1],[-6,5,10,4,-2,-6,-8,1,3,-8,9],[3,2,4,-8,5,7,5,8,9,-10,-6],[-10,-10,-7,2,-8,7,-1,-4,-6,-5,10],[2,9,9,8,10,2,-3,-10,7,1,10],[5,-1,4,5,5,-4,-3,-4,8,-1,3],[1,10,-3,-2,-5,6,9,1,4,3,2],[10,-9,1,-1,3,-10,-10,3,6,10,-3]],[[4,4,2,5,-3,10,-5,1,5,-8,6],[8,3,-7,-5,-3,-6,8,-4,10,10,-9],[-10,3,-4,-8,2,-10,-9,-9,7,5,8],[-9,-6,10,-10,-3,9,4,8,4,8,-4],[-8,3,-4,9,2,4,9,-6,-5,7,-6],[7,-3,-5,-4,-9,-3,-8,-1,-10,-6,-2],[10,-2,-8,9,10,-9,9,-7,4,-5,-8],[-3,1,5,10,2,5,5,3,-7,-3,9]],[[10,-5,1,1,-5,2,10,5,3,1,1],[1,-1,-8,-7,-6,-2,3,-3,5,-1,-5],[-4,-2,-8,-7,1,3,-8,-6,-10,6,-3],[5,3,3,-9,-8,1,-2,-5,7,8,-7],[1,-3,-6,-2,8,-5,1,9,-10,-5,-7],[9,-5,-5,6,-9,-5,-9,3,-10,-1,4],[-4,-4,-9,5,-5,7,9,-2,4,-4,-6],[-10,4,-10,4,9,-8,-2,3,3,10,-9]],[[-4,5,-4,8,2,9,-7,-5,2,9,-8],[-6,-8,10,-9,-8,9,10,4,3,6,-6],[-10,6,-6,1,5,6,6,-1,4,-7,-5],[-8,7,-9,-3,7,-5,-7,-7,-4,6,6],[-5,-7,8,-3,1,6,-3,2,-9,1,-4],[-4,7,-3,-9,2,-8,4,-3,1,-6,-5],[-1,5,7,-5,-4,-10,-10,-1,4,2,6],[-7,10,-4,-8,-7,5,-10,-10,3,-5,-5]],[[8,1,-3,3,10,-8,-10,9,3,-7,-10],[1,4,-3,9,-4,-6,-8,-10,10,-10,2],[-1,10,-7,-2,-7,-4,-9,10,7,-4,10],[5,4,2,2,-8,3,6,-6,-6,5,4],[8,-3,-9,-1,-10,9,-10,8,4,-4,3],[-8,2,3,-5,1,-4,-10,1,2,-6,5],[-3,-7,-8,-6,4,-3,-10,-2,-5,10,-7],[-2,4,10,-8,-5,8,10,4,1,3,-4]],[[10,10,1,5,-2,8,5,-5,3,-4,5],[-8,-3,9,-1,-9,-9,6,-10,-9,2,-8],[5,7,-5,-10,-8,-9,7,7,1,1,-4],[1,2,6,-9,-8,-8,-2,-10,3,-3,9],[10,-10,-1,-10,-1,-8,-3,4,9,-6,-9],[-9,-3,6,-5,-5,-8,-6,9,-3,7,3],[8,-3,1,3,10,-8,-4,-8,-9,4,10],[-8,5,9,-5,-3,-10,-9,8,3,-1,10]],[[7,-4,10,6,7,-9,5,4,10,2,-6],[1,2,1,-4,9,-8,8,1,10,-7,-8],[-8,-4,-10,8,-9,9,2,-5,10,10,6],[-7,-1,3,-7,2,-3,-4,5,2,-3,-5],[10,3,-3,9,-2,-4,-5,-3,-10,-10,3],[10,7,2,-3,-7,7,3,3,-9,8,10],[-2,6,7,-9,-1,8,10,-10,-7,6,-6],[-3,-10,-6,6,2,8,-4,-5,5,1,-5]],[[-3,4,1,5,-6,6,1,-6,7,-6,7],[10,-2,-9,-8,2,1,-3,-5,-10,7,8],[-8,-4,2,2,2,1,-6,-7,-7,10,-6],[-10,1,1,-6,7,-3,10,3,-5,3,8],[-6,-6,3,-1,-8,9,9,-9,-9,8,7],[7,10,-6,-8,4,1,-7,7,5,-6,-9],[4,-9,-4,5,7,-3,6,1,6,-7,9],[-1,-1,4,-1,-4,10,-8,-10,-8,-8,3]],[[-2,7,-2,-3,8,7,-2,-9,-3,10,4],[-10,2,1,-8,-4,-1,-8,-5,3,-7,-5],[9,-4,6,-8,1,-7,5,-4,4,-3,9],[7,-2,-9,9,10,9,2,7,6,-7,2],[10,-5,4,-7,-9,6,3,2,1,-1,7],[6,3,-5,-2,10,-5,-6,3,1,-8,-5],[4,4,-3,-6,8,6,1,-10,10,-8,-5],[1,8,1,-1,-10,8,-10,10,-1,7,8]],[[9,-4,-9,4,-7,-3,-9,2,5,-2,-7],[-1,-10,5,-10,-5,2,7,-2,-5,-8,-3],[-7,4,8,-4,-10,-3,-7,-8,-3,7,-2],[7,7,-2,-4,-1,-9,-2,3,-3,-1,5],[-5,9,6,5,2,4,8,6,9,3,-2],[-7,1,2,-6,-1,2,1,6,7,-10,9],[9,9,1,-7,9,10,4,3,10,1,6],[9,-9,-1,-1,6,4,-7,-9,1,-8,9]],[[4,-10,-10,6,4,-7,4,-2,6,5,3],[-8,6,-2,10,-4,5,-9,-4,10,-10,1],[-5,-1,10,5,-7,10,10,-6,5,-5,4],[7,8,-8,-6,-6,-3,-4,-4,10,9,5],[-2,-10,-10,9,-8,4,6,6,-2,-5,-9],[9,9,3,9,-9,-8,10,-3,-4,7,-7],[-3,-7,5,-1,2,-6,-1,-10,8,1,-8],[5,-10,-4,-8,-4,-6,-5,4,5,-8,-8]]], dtype = "uint8")#candidate|688|(15, 8, 11)|const|uint8
var_689 = relay.var("var_689", dtype = "uint8", shape = (15, 8, 11))#candidate|689|(15, 8, 11)|var|uint8
bop_690 = relay.right_shift(const_688.astype('uint8'), relay.reshape(var_689.astype('uint8'), relay.shape_of(const_688))) # shape=(15, 8, 11)
output = relay.Tuple([bop_690,])
output2 = relay.Tuple([bop_690,])
func_693 = relay.Function([var_689,], output)
mod['func_693'] = func_693
mod = relay.transform.InferType()(mod)
mutated_mod['func_693'] = func_693
mutated_mod = relay.transform.InferType()(mutated_mod)
var_694 = relay.var("var_694", dtype = "uint8", shape = (15, 8, 11))#candidate|694|(15, 8, 11)|var|uint8
func_693_call = mutated_mod.get_global_var('func_693')
call_695 = func_693_call(var_694)
output = call_695
func_696 = relay.Function([var_694], output)
mutated_mod['func_696'] = func_696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_711 = func_325_call()
call_712 = func_325_call()
output = relay.Tuple([call_711,])
output2 = relay.Tuple([call_712,])
func_723 = relay.Function([], output)
mod['func_723'] = func_723
mod = relay.transform.InferType()(mod)
mutated_mod['func_723'] = func_723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mutated_mod.get_global_var('func_723')
call_724 = func_723_call()
output = call_724
func_725 = relay.Function([], output)
mutated_mod['func_725'] = func_725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_797 = relay.TupleGetItem(func_723_call(), 0)
call_798 = relay.TupleGetItem(func_725_call(), 0)
var_806 = relay.var("var_806", dtype = "int64", shape = (9, 12, 15))#candidate|806|(9, 12, 15)|var|int64
bop_807 = relay.power(call_797.astype('float32'), relay.reshape(var_806.astype('float32'), relay.shape_of(call_797))) # shape=(9, 12, 15)
bop_810 = relay.power(call_798.astype('float32'), relay.reshape(var_806.astype('float32'), relay.shape_of(call_798))) # shape=(9, 12, 15)
bop_811 = relay.add(call_797.astype('uint16'), relay.reshape(var_806.astype('uint16'), relay.shape_of(call_797))) # shape=(9, 12, 15)
bop_814 = relay.add(call_798.astype('uint16'), relay.reshape(var_806.astype('uint16'), relay.shape_of(call_798))) # shape=(9, 12, 15)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_815 = relay.TupleGetItem(func_303_call(), 0)
call_816 = relay.TupleGetItem(func_304_call(), 0)
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
const_819 = relay.const(False, dtype = "bool")#candidate|819|()|const|bool
call_818 = relay.TupleGetItem(func_408_call(relay.reshape(const_819.astype('bool'), [])), 5)
call_820 = relay.TupleGetItem(func_411_call(relay.reshape(const_819.astype('bool'), [])), 5)
func_493_call = mod.get_global_var('func_493')
func_497_call = mutated_mod.get_global_var('func_497')
const_847 = relay.const([-3.142523,-7.102956,-0.232101,9.491413,1.446958,2.566808,1.767051,6.453674,8.287287,8.881718,-0.747191,-4.014749,6.344207,-7.842557,7.932522,-2.225441,-8.058603,-7.649561,7.315291,-1.656975,-5.491865,-8.772114,0.893528,-7.889069,2.640572,0.300574,0.528978,-9.683123,1.715845,6.513608,-4.145900,6.395155,-2.308901,7.485748,5.362783,8.928903,4.332063,-5.385255,1.274485,-3.973271,-3.399604,-3.434583,6.568217,-4.722104,-2.607490,-8.882898,-3.790736,5.377396,3.478662,-0.138232,-7.674843,9.619527,1.024918,-6.346400,-9.687799,1.667693,-7.284016,-9.063010,9.662824,8.626842,-4.413356,-7.783340,8.473275,-1.054821,2.765465,2.538210,-9.389910,4.802309,-6.993621,-3.512582,-9.276129,-7.452422,7.906487,5.034122,3.371088,-9.386709,-3.184376,-7.513576,-3.103198,-3.036579,6.708642,-3.677768,-7.176267,-1.604103,1.968459,-4.891284,-0.309875,0.396056,7.877862,-1.760830,4.607189,3.937800,-0.991804,5.101699,-9.320673,-6.596013,9.631900,4.066469,-1.785398,9.022481,-4.201197,-6.720039,-0.317506,-1.956031,-4.963209,-0.244115,-2.435825,5.579795,-0.452244,1.514464,-6.765180,-4.493374,-7.054149,-4.419411,6.816609,9.646935,3.471592,3.520890,3.481652,0.215562,-9.744895,6.764087,6.347161,5.995891,6.361044,-1.408294,-7.664684,7.851706,-7.405214,-1.883744,2.328593,6.792629,2.714920,-9.505787,6.665265,-2.961323,-6.606700,-9.270538,-0.946846,7.977491,-5.631067,4.219429,-5.546544,-4.615457,-9.292597,4.761360,-3.043466,-3.209668,7.068323,-0.989760,8.970539,-3.037178,-6.874816,8.999854,5.568691,-1.956522,1.580150,-9.932413,-8.950377,-4.552995,9.517114,8.492448,0.690833,6.461250,-9.309214,9.744805,-6.814270,5.293233,-3.148893,7.149780,0.164553,1.915650,-4.594086,1.713528,-9.686848,5.048857,0.913250,1.928093,5.382986,0.579682,-8.378475,4.348307,-9.879183,9.102030,0.697848,-4.882515,-1.316736,7.156533,-5.557796,-4.914364,1.337669,-1.303846,-2.835781,6.342491,0.910945,3.814052,9.023887,-2.014677,-7.564403,-6.796684,2.313659,-3.164447,-2.728244,-9.431717,-6.383490,-7.311057,-2.210605,-7.708055,-5.279280,-2.887688,-7.912266,-7.521328,-8.586148,-8.233407,-9.562834,2.360827,3.543776,-7.804901,3.539203,-1.946295,8.519640,5.643407,-1.941967,-8.472282,4.486715,-5.249153,-8.372608,0.060378,5.301529,3.639061,-9.129295,0.746141,0.251735,-8.111928,-3.083749,-6.501865,8.287916,-8.367406,-6.616256,-7.760051,1.364038,5.736774,1.353700,1.996163,-6.913209,2.541837,1.876184,9.065414,-7.566710,1.122896,-7.857246,-4.849933,-0.984927,3.714478,4.651796,-1.352647,-4.903805,-0.141690,0.114927,1.876867,8.715664,-0.710295,3.925935,4.846223,1.376095,5.968829,-8.503167,3.115987,-1.203858,6.575570,4.408745,-5.560844,-8.120923,8.007776,-6.092226,8.850005,7.834229,-7.633370,9.525179,-0.835265,2.230607,8.828942,3.194190,-4.255813,9.611099,7.877278,4.042294,0.720480,2.219877,9.412945,3.296260,8.847284,0.211884,7.271046,8.213843,2.204120,3.653134,-6.954831,-8.651888,-1.250353,1.700266,-8.487777,-8.824142,-0.994127,-2.632058,4.838648,-7.343139,0.186041,8.522788,7.263095,-6.851300,9.698739,7.198735,3.974270,-7.784241,5.236497,3.530174,-0.958842,5.474787,0.589785,6.295867,0.393583,6.874669,4.637319,-9.672541,7.564934,3.912144,-2.695407,1.289768,-6.144681,-4.290969,0.584794,7.706938,8.198373,-0.212138,4.521074,9.955397,4.281066,4.711180,2.099391,2.729081,-0.221211,7.556205,1.975908,-3.013478,-2.925651,-1.162106,1.250035,-2.520729,-6.921743,2.206404,-0.521266,9.210079,-3.566774,-7.638519,-1.825139,-9.250443,-0.017573,1.445005,-1.655498,-7.302265,-9.274420,-9.668215,-4.438985,-0.758132,8.629359,-2.853557,5.515387,-0.464991,-7.273966,1.613369,-7.138338,-2.730909,-8.759200,8.373401,2.293656,1.064654,-4.008924,5.609372,-6.670825,9.554440,-9.302798,5.445533,1.490977,5.343924,-9.985372,-2.481373,-5.332955,-6.295742,2.983117,-3.312146,3.626775,-6.160792,6.381344,-9.689497,-3.961586,-0.791560,-6.675249,-6.435727,7.517464,8.023382,-6.324167,-1.040447,-1.754593,4.400834,-0.179296,6.039006,-1.010284,2.437726,8.115860,4.184614,-7.780380,-7.367215,-9.656152,-3.464997,-8.206726,2.029292,-2.947065,-6.334561,-0.650974,-9.219788,9.963253,-7.509680,1.707583,8.944919,-5.104289,-1.842416,-5.672502,2.768013,4.435072,-1.778963,7.761733,0.401311,-8.870714,1.113550,5.728497,1.356484,1.576711,-8.247075,-7.853018,5.395585,8.316584,0.005090,0.858946,-6.953757,-6.741006,-6.805039,-8.162475,9.735408,2.848500,-1.399349,-8.212981,1.560845,0.077713,5.392170,-9.074143,-3.586471,-7.179596,9.272059,-3.858877,0.199835,0.701524,6.289031,5.951516,-3.415911,4.319897,7.540879,-7.144139,8.033490,1.672806,8.598563,5.442988,2.118140,1.447208,3.763255,-2.653222,6.487072,9.616345,2.474797,5.274189,9.721613,-1.993713,4.293826,-7.929863,6.648065,8.284638,8.446636,-5.932075,-0.908706,3.872369,-4.930996,-0.457612,2.860604,-7.956531,-4.845337,-4.536699,-3.350925,6.138055,-0.364648,-4.002351,1.694362,-3.960096,-9.012913,1.391042,2.247920,2.496750,-2.264143,1.114727,0.792803,-2.075915,5.389795,8.471518,-9.655615,9.780942,-3.910016,-1.659235,2.355334,-2.205882,1.243579,6.604199,0.449732,-9.523873,-4.604203,4.946107,8.615148,-0.263027,9.408546,-1.633159,-8.110368,-3.623884,6.377128,-3.447734,1.359524,2.278538,-2.595535,5.294360,8.237778,0.098638,7.632522,4.753127,-4.896784,-4.126827,1.627477,3.769533,-2.971533,2.481631,-4.894021,9.203451,-5.816963,3.978267,7.075012,-6.688484,-4.678622,-4.442915,7.127963,9.620622,9.856886,5.508771,-6.632686,-9.970662,-7.909657,2.473665,2.434672,-1.244136,8.861014,-4.487998,0.790596,7.605902,-8.037439,5.246298,7.115165,-0.191841,-0.770666,8.964550,-2.884315,-6.221456,8.953707,-7.882919,-2.491621,4.135965,-7.831119,-0.732179,-8.298276,9.957615,5.725480,-0.295474,2.083166,-4.891620,-6.523277,2.258434,7.728420,9.714757,8.893872,-4.511525,8.353248,6.375219,1.506711,1.094136,2.474119,7.415285,9.246756,9.832441,-6.672306,2.615438,7.047346,1.319042,-7.187823,-4.573812,-1.380840,8.800814,-7.677990,5.848556,-1.385497,4.402891,-6.832330,-9.658996,4.192611,-0.001223,9.381832,-4.701881,-3.977774,-2.231851,2.521869,-7.340312,6.148723,1.002587,-6.366235,6.276019,8.774557,-7.220570,0.508059,9.892262,-4.495686,-1.496959,3.490264,2.212699,4.895335,-3.080654,-7.520782,-0.797910,-5.605758,4.284385,1.461894,9.100435,3.350681,-0.196227,8.033045,4.134570,2.323962,6.098591,1.873842,2.761354,-3.151417,1.539547,-6.807945,-9.234398,5.125820,-2.832811,1.391043,4.814073,5.204100,0.173428,2.407603,9.394183,1.936457,-3.797603,8.076887,3.088909,3.839380,-2.492444,-7.050573,7.435287,-4.566709,-4.768397,5.344819,-8.321169,2.251112,3.996962,7.844415,-2.439651,-0.999011,5.051872,-7.725000,3.628200,6.358325,2.914979,7.311054,1.323131,-2.137617,5.824488,1.137262,8.059660,2.272047,3.948638,7.473153,3.543118,-6.150176,0.726021,7.788190,1.229251,-3.910981,8.434318,3.579655,5.880558,-1.848147,2.930895,-5.034776,6.126857,-8.750747,-3.542414,-4.076745,6.207074,-7.878284,6.727135,7.032257,-7.487920,0.873734,4.316400,-6.851398,8.279180,0.379809,-3.403648,3.531852,-7.352521,0.666636,0.386189,-9.153394,-1.678493,6.090761,6.514224,-8.642847,-4.656123,5.483804,-5.931384,-2.862102,-7.807834,6.864636,7.329373,-0.693053,-8.161295,3.965141,8.492434,-9.012947,-5.330840,9.384326,-9.423842,-7.713922,-4.579610,0.030019,4.046922,-5.133838,7.142970,0.785861,-7.571152,-8.316888,7.377424,-3.984239,-1.484568,-3.115210,-2.278438,-8.851163,-7.023624,5.683313,-0.372051,4.677413,-8.746484,0.748073,4.064706,-2.396477,2.168258,-5.650746,-0.828827,5.972535,0.928357,-4.042207,-1.105521,3.500106,6.803429,2.144324,2.181422,2.056931,-6.581575,4.057946,3.340156,6.574681,1.780594,1.158469,-2.260942,-0.122077,2.314227,3.666199,2.209787,-4.869414,0.317509,-3.929701,-0.814986,-0.781559,-5.709631,2.751667,2.746438,-5.106786,-1.195259,9.333527,4.401279,2.741371,-1.813687,-0.161490,0.846648,-0.542682,-2.593221,7.392959,-7.469942,2.379406,9.634018,6.344037,9.463466,2.015175,9.907731,-1.284262,-3.109793,1.867091,-0.736875,-9.302243,-9.575981,-5.362684,3.496318,-9.204226,8.128165,0.045431,-7.395307,6.230314,-9.100273,5.109887,2.554450,-8.088022,8.274909,-4.141909,7.952407,9.515446,7.738387,-4.904986,8.550207,6.794042,-9.259330,-3.514446,8.991597,-4.073041,-3.732014,0.864983,9.576204,-8.711545,-7.109049,-6.607546,0.033258,5.413176,6.580668,-0.706436,-0.237011], dtype = "float32")#candidate|847|(858,)|const|float32
call_846 = relay.TupleGetItem(func_493_call(relay.reshape(const_847.astype('float32'), [11, 6, 13]), relay.reshape(const_847.astype('float32'), [11, 6, 13]), relay.reshape(call_818.astype('float64'), [240, 1]), ), 2)
call_848 = relay.TupleGetItem(func_497_call(relay.reshape(const_847.astype('float32'), [11, 6, 13]), relay.reshape(const_847.astype('float32'), [11, 6, 13]), relay.reshape(call_818.astype('float64'), [240, 1]), ), 2)
uop_852 = relay.cos(const_847.astype('float32')) # shape=(858,)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_857 = relay.TupleGetItem(func_303_call(), 0)
call_858 = relay.TupleGetItem(func_304_call(), 0)
uop_865 = relay.tan(uop_852.astype('float32')) # shape=(858,)
bop_877 = relay.floor_divide(uop_865.astype('float64'), const_819.astype('float64')) # shape=(858,)
output = relay.Tuple([bop_807,bop_811,call_815,call_818,call_846,call_857,bop_877,])
output2 = relay.Tuple([bop_810,bop_814,call_816,call_820,call_848,call_858,bop_877,])
func_887 = relay.Function([var_806,], output)
mod['func_887'] = func_887
mod = relay.transform.InferType()(mod)
mutated_mod['func_887'] = func_887
mutated_mod = relay.transform.InferType()(mutated_mod)
var_888 = relay.var("var_888", dtype = "int64", shape = (9, 12, 15))#candidate|888|(9, 12, 15)|var|int64
func_887_call = mutated_mod.get_global_var('func_887')
call_889 = func_887_call(var_888)
output = call_889
func_890 = relay.Function([var_888], output)
mutated_mod['func_890'] = func_890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_641_call = mod.get_global_var('func_641')
func_643_call = mutated_mod.get_global_var('func_643')
call_906 = relay.TupleGetItem(func_641_call(), 2)
call_907 = relay.TupleGetItem(func_643_call(), 2)
output = relay.Tuple([call_906,])
output2 = relay.Tuple([call_907,])
func_937 = relay.Function([], output)
mod['func_937'] = func_937
mod = relay.transform.InferType()(mod)
output = func_937()
func_938 = relay.Function([], output)
mutated_mod['func_938'] = func_938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_992 = relay.TupleGetItem(func_723_call(), 0)
call_993 = relay.TupleGetItem(func_725_call(), 0)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_1007 = relay.TupleGetItem(func_723_call(), 0)
call_1008 = relay.TupleGetItem(func_725_call(), 0)
output = relay.Tuple([call_992,call_1007,])
output2 = relay.Tuple([call_993,call_1008,])
func_1010 = relay.Function([], output)
mod['func_1010'] = func_1010
mod = relay.transform.InferType()(mod)
output = func_1010()
func_1011 = relay.Function([], output)
mutated_mod['func_1011'] = func_1011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1051 = relay.var("var_1051", dtype = "float32", shape = (14, 15, 1))#candidate|1051|(14, 15, 1)|var|float32
uop_1052 = relay.log2(var_1051.astype('float32')) # shape=(14, 15, 1)
func_937_call = mod.get_global_var('func_937')
func_938_call = mutated_mod.get_global_var('func_938')
call_1057 = relay.TupleGetItem(func_937_call(), 0)
call_1058 = relay.TupleGetItem(func_938_call(), 0)
bop_1068 = relay.greater(uop_1052.astype('bool'), relay.reshape(var_1051.astype('bool'), relay.shape_of(uop_1052))) # shape=(14, 15, 1)
bop_1075 = relay.floor_divide(var_1051.astype('float64'), relay.reshape(uop_1052.astype('float64'), relay.shape_of(var_1051))) # shape=(14, 15, 1)
var_1083 = relay.var("var_1083", dtype = "float64", shape = (14, 15, 3))#candidate|1083|(14, 15, 3)|var|float64
bop_1084 = relay.equal(bop_1075.astype('bool'), var_1083.astype('bool')) # shape=(14, 15, 3)
output = relay.Tuple([call_1057,bop_1068,bop_1084,])
output2 = relay.Tuple([call_1058,bop_1068,bop_1084,])
func_1087 = relay.Function([var_1051,var_1083,], output)
mod['func_1087'] = func_1087
mod = relay.transform.InferType()(mod)
var_1088 = relay.var("var_1088", dtype = "float32", shape = (14, 15, 1))#candidate|1088|(14, 15, 1)|var|float32
var_1089 = relay.var("var_1089", dtype = "float64", shape = (14, 15, 3))#candidate|1089|(14, 15, 3)|var|float64
output = func_1087(var_1088,var_1089,)
func_1090 = relay.Function([var_1088,var_1089,], output)
mutated_mod['func_1090'] = func_1090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_1115 = func_325_call()
call_1116 = func_325_call()
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_1120 = func_325_call()
call_1121 = func_325_call()
func_887_call = mod.get_global_var('func_887')
func_890_call = mutated_mod.get_global_var('func_890')
call_1129 = relay.TupleGetItem(func_887_call(relay.reshape(call_1115.astype('int64'), [9, 12, 15])), 2)
call_1130 = relay.TupleGetItem(func_890_call(relay.reshape(call_1115.astype('int64'), [9, 12, 15])), 2)
func_887_call = mod.get_global_var('func_887')
func_890_call = mutated_mod.get_global_var('func_890')
call_1137 = relay.TupleGetItem(func_887_call(relay.reshape(call_1115.astype('int64'), [9, 12, 15])), 1)
call_1138 = relay.TupleGetItem(func_890_call(relay.reshape(call_1115.astype('int64'), [9, 12, 15])), 1)
func_937_call = mod.get_global_var('func_937')
func_938_call = mutated_mod.get_global_var('func_938')
call_1140 = relay.TupleGetItem(func_937_call(), 0)
call_1141 = relay.TupleGetItem(func_938_call(), 0)
var_1151 = relay.var("var_1151", dtype = "uint16", shape = (9, 12, 15))#candidate|1151|(9, 12, 15)|var|uint16
bop_1152 = relay.less_equal(call_1137.astype('bool'), relay.reshape(var_1151.astype('bool'), relay.shape_of(call_1137))) # shape=(9, 12, 15)
bop_1155 = relay.less_equal(call_1138.astype('bool'), relay.reshape(var_1151.astype('bool'), relay.shape_of(call_1138))) # shape=(9, 12, 15)
bop_1163 = relay.equal(call_1129.astype('bool'), relay.reshape(call_1140.astype('bool'), relay.shape_of(call_1129))) # shape=(12, 2, 10)
bop_1166 = relay.equal(call_1130.astype('bool'), relay.reshape(call_1141.astype('bool'), relay.shape_of(call_1130))) # shape=(12, 2, 10)
output = relay.Tuple([call_1115,call_1120,bop_1152,bop_1163,])
output2 = relay.Tuple([call_1116,call_1121,bop_1155,bop_1166,])
func_1176 = relay.Function([var_1151,], output)
mod['func_1176'] = func_1176
mod = relay.transform.InferType()(mod)
var_1177 = relay.var("var_1177", dtype = "uint16", shape = (9, 12, 15))#candidate|1177|(9, 12, 15)|var|uint16
output = func_1176(var_1177)
func_1178 = relay.Function([var_1177], output)
mutated_mod['func_1178'] = func_1178
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1188 = relay.var("var_1188", dtype = "float32", shape = (5, 14, 7))#candidate|1188|(5, 14, 7)|var|float32
var_1189 = relay.var("var_1189", dtype = "float32", shape = (5, 14, 7))#candidate|1189|(5, 14, 7)|var|float32
bop_1190 = relay.floor_mod(var_1188.astype('float32'), relay.reshape(var_1189.astype('float32'), relay.shape_of(var_1188))) # shape=(5, 14, 7)
func_1010_call = mod.get_global_var('func_1010')
func_1011_call = mutated_mod.get_global_var('func_1011')
call_1198 = relay.TupleGetItem(func_1010_call(), 0)
call_1199 = relay.TupleGetItem(func_1011_call(), 0)
bop_1200 = relay.greater_equal(bop_1190.astype('bool'), relay.reshape(var_1189.astype('bool'), relay.shape_of(bop_1190))) # shape=(5, 14, 7)
output = relay.Tuple([call_1198,bop_1200,])
output2 = relay.Tuple([call_1199,bop_1200,])
func_1210 = relay.Function([var_1188,var_1189,], output)
mod['func_1210'] = func_1210
mod = relay.transform.InferType()(mod)
var_1211 = relay.var("var_1211", dtype = "float32", shape = (5, 14, 7))#candidate|1211|(5, 14, 7)|var|float32
var_1212 = relay.var("var_1212", dtype = "float32", shape = (5, 14, 7))#candidate|1212|(5, 14, 7)|var|float32
output = func_1210(var_1211,var_1212,)
func_1213 = relay.Function([var_1211,var_1212,], output)
mutated_mod['func_1213'] = func_1213
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1241 = relay.const([[-1.543566,-3.970322,-5.128533,-9.424510,-1.116824],[5.139854,6.004186,1.537218,-2.353926,-4.727471],[-1.670689,8.947283,-1.612602,2.735946,-3.748670],[-9.471462,5.573821,9.935004,-6.929900,-6.824315],[-8.075268,0.017532,-3.403993,-0.622384,-1.402584],[2.772532,-5.419506,8.699118,-2.883970,-8.714609],[5.515127,-2.097733,6.134296,6.845674,9.306703],[-0.455474,2.994344,-9.213469,-1.661715,5.086938],[1.887802,2.360978,7.777318,-0.926510,-5.050934],[-4.377017,-7.392812,-7.037635,-4.324157,6.549113]], dtype = "float64")#candidate|1241|(10, 5)|const|float64
uop_1242 = relay.atan(const_1241.astype('float64')) # shape=(10, 5)
func_1210_call = mod.get_global_var('func_1210')
func_1213_call = mutated_mod.get_global_var('func_1213')
var_1251 = relay.var("var_1251", dtype = "float32", shape = (490,))#candidate|1251|(490,)|var|float32
call_1250 = relay.TupleGetItem(func_1210_call(relay.reshape(var_1251.astype('float32'), [5, 14, 7]), relay.reshape(var_1251.astype('float32'), [5, 14, 7]), ), 0)
call_1252 = relay.TupleGetItem(func_1213_call(relay.reshape(var_1251.astype('float32'), [5, 14, 7]), relay.reshape(var_1251.astype('float32'), [5, 14, 7]), ), 0)
func_937_call = mod.get_global_var('func_937')
func_938_call = mutated_mod.get_global_var('func_938')
call_1274 = relay.TupleGetItem(func_937_call(), 0)
call_1275 = relay.TupleGetItem(func_938_call(), 0)
output = relay.Tuple([uop_1242,call_1250,var_1251,call_1274,])
output2 = relay.Tuple([uop_1242,call_1252,var_1251,call_1275,])
func_1283 = relay.Function([var_1251,], output)
mod['func_1283'] = func_1283
mod = relay.transform.InferType()(mod)
var_1284 = relay.var("var_1284", dtype = "float32", shape = (490,))#candidate|1284|(490,)|var|float32
output = func_1283(var_1284)
func_1285 = relay.Function([var_1284], output)
mutated_mod['func_1285'] = func_1285
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1329 = relay.var("var_1329", dtype = "uint32", shape = (6, 10, 13))#candidate|1329|(6, 10, 13)|var|uint32
var_1330 = relay.var("var_1330", dtype = "uint32", shape = (6, 10, 13))#candidate|1330|(6, 10, 13)|var|uint32
bop_1331 = relay.multiply(var_1329.astype('uint32'), relay.reshape(var_1330.astype('uint32'), relay.shape_of(var_1329))) # shape=(6, 10, 13)
func_1087_call = mod.get_global_var('func_1087')
func_1090_call = mutated_mod.get_global_var('func_1090')
var_1339 = relay.var("var_1339", dtype = "float32", shape = (210,))#candidate|1339|(210,)|var|float32
const_1340 = relay.const([[-1.410301,-4.471821,5.302391,-0.326762,-1.810962,1.617890,-2.208938,0.941943,8.855978],[-6.466102,3.329213,-0.856390,7.180249,-4.835977,5.683005,-1.158925,-2.373665,3.562935],[2.482348,8.030803,-4.010097,8.044451,9.258407,4.862948,-4.332686,7.391560,4.565595],[-9.263178,-3.011601,-2.423257,-3.390991,3.726386,7.322374,-2.142232,-5.345103,-5.302730],[-3.434457,2.067726,-8.103372,-7.639232,-6.635906,6.945528,9.669612,-4.581523,-1.970018],[3.252492,-9.234402,3.050377,-2.787030,-6.719053,9.679517,7.442879,-8.274825,-9.488325],[-9.176641,6.838723,-5.810599,-4.180624,6.443118,4.887658,2.639449,-4.046352,-7.049827],[-1.437111,8.807379,3.298505,6.136617,-7.284076,-1.625841,6.146991,-6.405406,3.665900],[1.996591,-0.550283,9.681783,-0.743618,2.474498,-7.724077,-4.106877,-2.434464,6.395592],[1.356357,-5.661275,-1.414761,-6.605188,9.393921,9.108820,5.111186,-1.281661,2.759413],[-2.058173,4.785260,-6.929342,3.419804,-9.145994,-2.674136,6.978161,-9.170405,4.779079],[-9.465805,-3.618158,-9.355295,2.948837,-4.466661,-2.798014,3.869455,7.322091,-9.045274],[-6.148954,9.836540,5.502447,-5.699689,0.977055,-5.554759,1.654360,-2.832029,0.232239],[1.006392,-6.384887,-2.309523,8.069322,9.491826,-0.214561,-3.225572,0.025414,7.894993],[2.169037,-6.437234,4.357658,-9.069572,4.017009,-6.700476,6.864451,0.742856,-2.872798],[-5.926470,4.780280,-5.004901,5.624158,-5.299509,-6.858679,1.863360,8.526208,-1.825701],[9.100733,-7.052036,8.038858,0.786418,-6.810504,6.760818,-4.219689,6.191842,7.680657],[-8.236968,-6.337811,-0.175464,-5.221316,0.209989,4.076857,-8.914526,-8.384254,2.697542],[-1.482387,-4.757433,-3.490957,5.037372,-0.816987,-4.380578,-5.508462,-2.560513,-1.063800],[-9.460156,5.952499,-2.258909,5.450174,7.958292,0.555073,-3.097389,1.941547,4.134334],[-1.380480,-4.197216,5.109355,-1.887433,7.290100,-1.606474,5.266003,8.959860,-6.725588],[2.373672,-1.444922,6.062017,-8.330901,6.589277,9.623445,2.793135,1.722883,-4.635176],[-4.602599,9.154500,6.012260,7.284011,-4.018383,2.723629,5.840178,-7.701939,6.864797],[9.094546,9.192955,0.432371,0.677048,-6.779874,3.881207,0.835899,-5.536771,0.696158],[3.774747,-2.338754,8.420620,-3.953433,3.304145,9.400583,4.221058,-1.323794,9.213022],[9.744253,-4.796013,-7.376384,-8.293969,0.293228,-5.608676,-7.685542,-0.821706,9.467405],[1.528044,-0.957843,-3.694670,0.012691,-4.284598,3.168584,-9.235152,1.613120,-8.427731],[-3.522700,6.304955,0.111650,-0.982118,1.863710,3.854450,7.602654,0.384209,7.378691],[3.461257,7.388659,-0.010331,2.998816,1.714517,9.711297,-0.686040,-5.845452,3.444207],[4.835992,9.824153,-0.539188,0.494652,8.132874,2.712222,5.821630,-1.033441,3.329664],[5.211297,9.729497,9.679127,-8.771035,-9.888859,0.323258,5.968039,6.807611,-1.793439],[3.649067,9.924879,-2.621144,8.883539,0.945205,-8.891448,-3.873980,-7.201229,-1.976638],[-1.854185,9.224675,7.607184,-2.064681,-2.271834,4.833390,-8.481077,-0.104408,-2.273988],[-5.501696,-3.874563,0.473618,-2.859954,-9.314273,9.421613,-9.639382,-3.882915,-7.259940],[6.894260,-3.347410,-9.217285,-0.562070,-7.530682,2.531276,8.598609,-0.381932,3.038250],[-1.542351,5.593687,-9.242582,6.739574,-3.070749,3.959856,0.154577,2.453893,-1.144119],[7.849786,-8.310477,1.852040,-5.715780,-6.633471,9.965189,-2.184570,5.968664,-9.087593],[-6.881428,0.282898,8.776949,9.844660,3.331525,-1.958903,3.319806,-6.751633,7.277899],[9.584351,-5.413980,-8.389626,0.073333,0.145448,-3.177914,3.036419,2.941130,5.302375],[0.394261,6.465393,-2.636803,-2.099389,4.699563,4.570266,-5.426930,2.758259,-1.348228],[-7.998748,-9.696083,6.791039,-0.653947,-1.472928,5.802472,-0.076564,-6.419825,3.812838],[-1.161745,-5.691948,-6.511158,-6.765032,-4.810301,8.776784,-8.791084,8.290135,4.167636],[9.425407,6.559642,1.784280,-2.650104,8.552298,0.902895,5.511418,-2.487055,4.478310],[7.013084,3.407728,3.341927,5.172470,9.843064,8.416721,7.960493,-1.738751,-7.975235],[6.726367,0.457441,8.089851,2.406045,-9.621746,0.755624,-2.790563,-4.174230,-7.231690],[-5.255764,1.856069,-8.651388,-7.184723,7.328835,-3.920081,-0.195599,-1.470897,-0.200753],[-5.837084,-6.494890,6.378415,-5.174708,8.437838,-8.526573,7.383438,4.473118,-0.228450],[3.712531,3.648827,5.254895,-3.501024,3.454394,3.616267,-1.407891,6.233685,9.898422],[-1.543253,-2.112859,-6.342763,-4.552557,5.578367,-6.384881,3.042393,-9.310655,-2.025649],[8.168195,4.747304,-7.963632,-8.704279,-0.435353,4.721032,2.981875,4.266199,8.349990],[-3.790927,5.785016,7.066714,2.718540,1.436464,5.979658,6.127135,-5.913915,7.581836],[2.747945,-0.335349,1.918031,4.715776,4.832467,-4.490600,-4.956689,-0.006846,-0.416670],[1.427924,1.843070,3.834924,1.840831,5.856543,4.555713,-5.787503,-4.060116,-6.810183],[-1.769980,-4.802607,4.223233,2.792722,4.716862,4.907109,7.375550,8.307577,-1.053627],[-5.980057,5.884440,5.724196,-2.445754,-6.008042,-1.798877,4.216999,-2.483571,3.227365],[-1.277494,-9.931294,-6.605187,-7.613660,-0.193121,-4.643389,-4.429726,-0.002976,-2.001918],[2.244869,9.124427,-0.944439,-5.450480,9.805299,5.349290,-9.275966,7.878268,-0.249748],[0.738816,5.134374,-2.944762,-5.436202,-3.389410,7.694653,-4.117006,-3.447423,-0.755144],[-2.960569,-6.515981,6.532522,-3.532136,9.973701,-7.113541,1.694967,-2.109389,-5.705861],[3.793071,-0.050749,0.278018,-7.062380,-5.631753,-2.704924,5.634292,5.388309,-6.788180],[-7.537740,1.899453,-2.244370,6.545402,0.908875,-0.824960,-8.922547,-3.660548,-0.952967],[-5.300039,7.692615,9.601110,7.133420,-1.648090,-5.475898,-6.176868,4.155719,-1.268171],[2.387918,-6.591767,-6.875286,-1.122360,-7.751007,7.982387,0.449982,9.732489,-6.362833],[-0.111778,-8.178755,-6.939490,5.570993,1.958570,-5.150507,-8.347069,6.524168,-3.282057],[8.074394,-3.207058,8.728353,-6.015815,-8.877889,-5.255244,-2.145138,-6.188712,6.441625],[5.976039,2.338840,-3.595039,1.103761,-2.260061,0.095551,-1.292962,6.751327,-6.988918],[-2.768052,5.978965,-5.212504,1.778321,-8.183962,3.973741,-0.245973,-7.017282,6.285624],[-7.029967,7.723973,3.446374,4.516426,-1.590359,3.258454,-4.827034,9.581295,-3.910285],[6.058884,3.284643,3.431500,8.826784,2.021872,-1.769244,-2.726137,7.940236,5.568456],[-8.194249,-0.850794,6.056353,0.043794,2.854125,-1.751691,3.220406,3.755217,8.843563]], dtype = "float64")#candidate|1340|(70, 9)|const|float64
call_1338 = relay.TupleGetItem(func_1087_call(relay.reshape(var_1339.astype('float32'), [14, 15, 1]), relay.reshape(const_1340.astype('float64'), [14, 15, 3]), ), 1)
call_1341 = relay.TupleGetItem(func_1090_call(relay.reshape(var_1339.astype('float32'), [14, 15, 1]), relay.reshape(const_1340.astype('float64'), [14, 15, 3]), ), 1)
func_641_call = mod.get_global_var('func_641')
func_643_call = mutated_mod.get_global_var('func_643')
call_1342 = relay.TupleGetItem(func_641_call(), 0)
call_1343 = relay.TupleGetItem(func_643_call(), 0)
output = relay.Tuple([bop_1331,call_1338,var_1339,const_1340,call_1342,])
output2 = relay.Tuple([bop_1331,call_1341,var_1339,const_1340,call_1343,])
func_1347 = relay.Function([var_1329,var_1330,var_1339,], output)
mod['func_1347'] = func_1347
mod = relay.transform.InferType()(mod)
mutated_mod['func_1347'] = func_1347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1347_call = mutated_mod.get_global_var('func_1347')
var_1349 = relay.var("var_1349", dtype = "uint32", shape = (6, 10, 13))#candidate|1349|(6, 10, 13)|var|uint32
var_1350 = relay.var("var_1350", dtype = "uint32", shape = (6, 10, 13))#candidate|1350|(6, 10, 13)|var|uint32
var_1351 = relay.var("var_1351", dtype = "float32", shape = (210,))#candidate|1351|(210,)|var|float32
call_1348 = func_1347_call(var_1349,var_1350,var_1351,)
output = call_1348
func_1352 = relay.Function([var_1349,var_1350,var_1351,], output)
mutated_mod['func_1352'] = func_1352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_1354 = relay.TupleGetItem(func_723_call(), 0)
call_1355 = relay.TupleGetItem(func_725_call(), 0)
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_1373 = func_325_call()
call_1374 = func_325_call()
func_1347_call = mod.get_global_var('func_1347')
func_1352_call = mutated_mod.get_global_var('func_1352')
const_1384 = relay.const([7,-5,-1,8,-2,-7,2,-1,-6,-5,-4,5,-1,-3,4,4,-9,6,4,4,-2,10,4,10,-6,1,1,8,-10,4,2,5,-7,-3,-2,6,-9,-6,6,1,3,2,9,-4,2,2,8,-9,-8,-7,-1,-2,7,-1,8,-7,-5,2,10,2,-8,7,-4,2,-9,10,-9,-10,4,9,5,-2,-4,2,-4,5,-1,-5,-9,6,-5,-7,1,-9,9,9,-6,4,-7,4,-3,1,-1,10,7,-9,-2,-5,4,-10,-3,-8,-9,-1,-1,10,-5,-1,-9,-8,6,-9,4,3,-9,2,1,-3,4,-9,-10,-2,-9,-3,5,7,9,-2,-9,10,8,-9,5,3,7,-6,-2,2,-5,-4,-6,-2,8,-7,-10,4,-2,9,7,7,-6,9,-3,-9,-5,9,-3,-6,6,7,-4,-4,-6,-2,-6,6,-3,-10,-7,-7,2,-6,8,6,-7,9,-4,8,7,2,10,-7,-3,1,4,4,3,-10,10,-4,9,-10,8,2,7,-1,3,10,-3,-8,9,2,10,5,-8,-8,-4,-9,-6,10,-8,-10,10,-7,-3,1,-4,5,7,-5,1,-3,2,1,-4,1,5,2,-3,8,3,7,-2,-3,-4,-5,10,4,-9,-1,-8,-6,-6,-6,-7,-5,4,8,-8,-7,7,-9,-2,-2,8,6,6,8,-10,10,-9,-6,1,-10,-4,1,-3,-2,-5,-7,-8,10,-7,-5,-5,2,2,-8,3,1,-7,1,-5,6,-7,-3,-8,-10,-3,1,2,1,-3,-6,-7,4,-9,7,-9,-4,-5,-1,1,-9,-6,2,4,-1,-2,-1,-6,-4,-1,-9,-3,-7,9,3,-1,4,-3,-5,-10,3,-5,-1,-3,-6,-6,-3,9,9,-9,-9,7,8,-2,8,-1,-3,9,-7,-9,-5,1,5,-9,9,-1,8,4,9,-9,7,1,-6,4,-1,10,9,7,1,-10,-5,9,-10,-1,10,-7,-2,6,9,5,10,-9,7,3,-3,8,-4,5,-1,-3,8,5,10,-2,-1,8,-2,-10,-2,-7,-8,5,2,-7,6,-4,-2,6,2,9,-7,-3,-6,8,-8,3,7,-9,7,2,6,2,4,-9,8,-8,-7,-1,-5,-10,-3,-10,-2,9,-3,-7,-6,-8,-6,7,-7,6,9,8,8,9,-3,-2,-8,-6,-2,1,-9,8,-5,7,3,5,-5,-6,-3,4,3,-8,-7,-1,7,-6,-10,2,-1,-7,-4,-4,7,2,4,3,2,-8,8,-7,-3,1,-7,-9,2,3,-10,7,-9,-7,-6,2,-4,8,-4,-8,8,-10,-2,3,5,-4,-5,2,1,-8,-2,7,-3,-9,-2,1,6,-4,2,-4,5,4,8,-5,7,-8,-4,-4,-1,-3,10,2,-7,4,-6,-6,6,-3,6,-5,-1,-4,9,-3,3,-5,2,-8,-4,8,-3,-10,-4,7,-1,5,-7,-1,8,-9,10,1,1,-10,-4,-6,-5,-7,-1,1,7,6,-6,10,-10,3,3,3,5,-1,-4,-7,-5,-7,9,10,5,-7,4,-5,6,-4,5,-3,3,-1,-10,7,3,2,4,-7,8,2,-3,6,-8,-8,-10,-1,-2,-3,1,8,3,-5,1,-10,5,-1,-10,8,9,-8,7,-3,4,-3,-5,-10,-10,7,-6,-2,-8,1,-2,-5,7,2,-5,-4,1,5,-8,-6,9,-2,10,-9,-7,-8,9,9,-9,9,8,-4,-1,-6,-3,9,-8,8,-5,8,-9,-10,-4,-4,10,6,9,8,8,-10,6,4,2,-2,10,6,8,8,5,-4,9,4,3,-9,5,3,-1,-5,-10,-8,9,-10,2,-1,-3,-3,-9,10,10,-3,9,6,3,-2,10,-3,-6,6,-4,6,-5,2,7,-6,-1,1,4,-1,9,-10,-3,-8,10,6,4,-1,-2,-1,-7,7,-5,-10,-6,-6,4,5,-2,6,-8,6,-6,-9,2,-9,-6,-6,3,-9,-9,-5,4,-10,-5,-8,1,-5,3,-5,-5,-3,-9,3,9,2,-9,-10,-8,-9,9,6,-3,6,4,-10,-8,-1,6,-10,5,10,2,1,2], dtype = "uint32")#candidate|1384|(780,)|const|uint32
var_1385 = relay.var("var_1385", dtype = "float32", shape = (210,))#candidate|1385|(210,)|var|float32
call_1383 = relay.TupleGetItem(func_1347_call(relay.reshape(const_1384.astype('uint32'), [6, 10, 13]), relay.reshape(const_1384.astype('uint32'), [6, 10, 13]), relay.reshape(var_1385.astype('float32'), [210,]), ), 3)
call_1386 = relay.TupleGetItem(func_1352_call(relay.reshape(const_1384.astype('uint32'), [6, 10, 13]), relay.reshape(const_1384.astype('uint32'), [6, 10, 13]), relay.reshape(var_1385.astype('float32'), [210,]), ), 3)
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_1395 = relay.TupleGetItem(func_1176_call(relay.reshape(call_1373.astype('uint16'), [9, 12, 15])), 0)
call_1396 = relay.TupleGetItem(func_1178_call(relay.reshape(call_1373.astype('uint16'), [9, 12, 15])), 0)
output = relay.Tuple([call_1354,call_1373,call_1383,const_1384,var_1385,call_1395,])
output2 = relay.Tuple([call_1355,call_1374,call_1386,const_1384,var_1385,call_1396,])
func_1397 = relay.Function([var_1385,], output)
mod['func_1397'] = func_1397
mod = relay.transform.InferType()(mod)
var_1398 = relay.var("var_1398", dtype = "float32", shape = (210,))#candidate|1398|(210,)|var|float32
output = func_1397(var_1398)
func_1399 = relay.Function([var_1398], output)
mutated_mod['func_1399'] = func_1399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_1442 = relay.TupleGetItem(func_723_call(), 0)
call_1443 = relay.TupleGetItem(func_725_call(), 0)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_1444 = relay.TupleGetItem(func_723_call(), 0)
call_1445 = relay.TupleGetItem(func_725_call(), 0)
bop_1449 = relay.not_equal(call_1442.astype('bool'), relay.reshape(call_1444.astype('bool'), relay.shape_of(call_1442))) # shape=(9, 12, 15)
bop_1452 = relay.not_equal(call_1443.astype('bool'), relay.reshape(call_1445.astype('bool'), relay.shape_of(call_1443))) # shape=(9, 12, 15)
output = relay.Tuple([bop_1449,])
output2 = relay.Tuple([bop_1452,])
func_1454 = relay.Function([], output)
mod['func_1454'] = func_1454
mod = relay.transform.InferType()(mod)
output = func_1454()
func_1455 = relay.Function([], output)
mutated_mod['func_1455'] = func_1455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_1472 = relay.TupleGetItem(func_303_call(), 1)
call_1473 = relay.TupleGetItem(func_304_call(), 1)
output = call_1472
output2 = call_1473
func_1482 = relay.Function([], output)
mod['func_1482'] = func_1482
mod = relay.transform.InferType()(mod)
mutated_mod['func_1482'] = func_1482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1482_call = mutated_mod.get_global_var('func_1482')
call_1483 = func_1482_call()
output = call_1483
func_1484 = relay.Function([], output)
mutated_mod['func_1484'] = func_1484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_1502 = func_325_call()
call_1503 = func_325_call()
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
const_1521 = relay.const([[-2.794400],[5.148207],[0.200698],[-5.557395],[4.464115],[1.227899],[1.664372],[4.207981],[4.170268],[-8.391188],[-9.134827],[-5.619844],[-7.196128],[-2.110372],[6.306919],[9.416744],[-0.414418],[0.468384],[-3.784196],[-9.413216],[-2.713101],[-8.536672],[9.268554],[7.336289],[-3.386688],[9.472555],[3.599074],[9.740566],[-0.674813],[-8.606761],[-2.679522],[6.937960],[-0.915551],[-5.872061],[0.615558],[-1.006334],[6.364297],[5.373758],[1.404813],[5.793549],[-6.514209],[-0.406396],[5.108615],[8.080307],[2.399250],[5.446594],[-5.843749],[-2.309496],[2.944023],[7.922266],[-8.166030],[2.784326],[-4.662314],[-1.159552],[1.364695],[-0.891160],[7.455962],[1.159988],[-7.259796],[-4.865879],[3.017435],[8.909796],[-0.254859],[-4.396830],[6.205031],[-8.670250],[-4.248394],[9.809650],[7.137840],[-4.036902],[6.252389],[-5.093757],[0.665061],[5.304766],[2.990077],[5.125735],[8.819286],[-5.572105],[2.235318],[-5.106573],[-3.470672],[-3.302965],[-4.918008],[-4.195385],[3.962105],[-6.230925],[6.976377],[7.919408],[6.427929],[-6.712058],[-1.665905],[3.909531],[0.552367],[-2.330677],[-1.938046],[3.123369],[3.602362],[5.638537],[8.885922],[9.167587],[-6.857386],[6.408964],[0.718475],[-3.830545],[-0.128578],[6.368252],[9.083422],[-4.354292],[-0.994075],[7.108519],[9.067844],[4.574094],[-9.707758],[-3.073493],[-5.750245],[-7.449938],[-5.837218],[-5.791447],[4.962015],[-2.933095],[-6.355111],[-8.003441],[-7.749627],[-9.589530],[0.221783],[5.371210],[-4.581427],[-6.113759],[-3.272153],[-5.416238],[-8.352847],[0.555198],[-6.525797],[-9.095513],[6.741774],[3.159821],[-2.848944],[7.233129],[5.785939],[4.700518],[0.088155],[1.537695],[-3.323771],[-7.987402],[7.101699],[9.421139],[4.476250],[-7.802106],[1.497365],[9.562882],[0.944640],[-4.179074],[2.491151],[-3.600184],[6.593104],[8.896443],[-4.332221],[-7.983142],[-6.570308],[7.784469],[4.215607],[-2.770187],[-8.495735],[-4.159865],[3.973771],[-1.939388],[5.985109],[6.044253],[-0.010416],[4.700475],[3.736561],[-5.730944],[1.405488],[-4.153236],[8.384106],[1.338313],[3.062420],[7.341749],[-0.485462],[6.634281],[-8.148387],[-0.583301],[-5.552302],[-9.617766],[4.416520],[-5.915169],[-4.551025],[2.472744],[4.296868],[-0.385663],[3.686180],[9.057468],[3.068691],[-4.524273],[-4.916580],[6.781375],[6.791238],[-3.055329],[4.990900],[-8.136737],[-4.102477],[-2.089225],[2.018034],[3.000520],[4.454460],[0.525988],[1.034295],[1.547930],[-0.378433],[9.315307]], dtype = "float32")#candidate|1521|(210, 1)|const|float32
call_1520 = relay.TupleGetItem(func_1397_call(relay.reshape(const_1521.astype('float32'), [210,])), 5)
call_1522 = relay.TupleGetItem(func_1399_call(relay.reshape(const_1521.astype('float32'), [210,])), 5)
bop_1529 = relay.minimum(call_1502.astype('uint32'), relay.reshape(call_1520.astype('uint32'), relay.shape_of(call_1502))) # shape=(9, 12, 15)
bop_1532 = relay.minimum(call_1503.astype('uint32'), relay.reshape(call_1522.astype('uint32'), relay.shape_of(call_1503))) # shape=(9, 12, 15)
output = relay.Tuple([const_1521,bop_1529,])
output2 = relay.Tuple([const_1521,bop_1532,])
func_1533 = relay.Function([], output)
mod['func_1533'] = func_1533
mod = relay.transform.InferType()(mod)
mutated_mod['func_1533'] = func_1533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1533_call = mutated_mod.get_global_var('func_1533')
call_1534 = func_1533_call()
output = call_1534
func_1535 = relay.Function([], output)
mutated_mod['func_1535'] = func_1535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1010_call = mod.get_global_var('func_1010')
func_1011_call = mutated_mod.get_global_var('func_1011')
call_1592 = relay.TupleGetItem(func_1010_call(), 1)
call_1593 = relay.TupleGetItem(func_1011_call(), 1)
func_514_call = mod.get_global_var('func_514')
func_516_call = mutated_mod.get_global_var('func_516')
call_1603 = func_514_call()
call_1604 = func_514_call()
output = relay.Tuple([call_1592,call_1603,])
output2 = relay.Tuple([call_1593,call_1604,])
func_1629 = relay.Function([], output)
mod['func_1629'] = func_1629
mod = relay.transform.InferType()(mod)
mutated_mod['func_1629'] = func_1629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1629_call = mutated_mod.get_global_var('func_1629')
call_1630 = func_1629_call()
output = call_1630
func_1631 = relay.Function([], output)
mutated_mod['func_1631'] = func_1631
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1637 = relay.var("var_1637", dtype = "int16", shape = ())#candidate|1637|()|var|int16
const_1638 = relay.const([[[-9,4,-1,-4,4,6,4,-6,2,8,8,-1,7,3],[6,-7,-6,-8,-9,-5,-6,9,-2,2,9,-7,-1,-6],[-4,8,6,2,-6,9,5,-10,-7,-2,-6,-5,4,3],[-2,6,8,3,9,6,-10,-3,-10,-5,-2,6,-3,4],[-10,-5,-8,8,6,9,-1,-3,1,5,8,6,8,1],[-2,-1,4,7,-8,7,8,-9,1,9,9,1,3,9],[-1,3,7,-8,-1,-2,-1,4,5,10,9,-5,-3,-6],[-8,-8,-7,-4,8,-7,8,9,-8,-1,-10,8,2,8]],[[2,2,10,8,-4,4,-4,-10,-10,-2,-3,1,5,3],[-3,-1,-4,6,4,3,-6,-9,-8,3,-7,8,7,7],[9,9,10,10,4,10,-7,5,2,4,-10,-9,3,1],[5,3,-8,9,-2,-4,2,-4,6,4,1,7,-6,-2],[-4,-8,3,-4,-4,10,1,-2,-9,1,6,-5,-5,10],[-9,-2,-7,3,-4,10,-9,5,6,2,-6,3,10,10],[-10,-1,-3,1,5,-10,10,-8,2,-10,3,-6,-7,-2],[6,-4,-2,-5,-8,-7,-2,-2,8,-5,3,3,-7,6]],[[7,-3,-8,9,-4,5,5,-4,10,1,-8,-2,-2,-9],[-3,5,1,-5,6,8,-10,-1,8,2,-3,-8,9,-4],[-5,2,-5,8,-6,6,-8,-2,-1,3,-10,7,-8,-6],[7,10,2,9,-10,3,1,9,-6,-8,-6,4,6,9],[8,-2,7,6,5,-7,4,2,3,-5,-4,4,3,-8],[-1,4,-4,6,-10,3,10,10,-3,-9,6,3,-6,2],[7,10,-6,-1,5,-4,-2,8,-6,-7,-3,-3,-10,-8],[5,8,1,2,-6,-8,2,6,8,7,-4,-4,1,-5]],[[6,-9,-5,-3,-9,-2,7,6,5,-3,-5,8,5,6],[9,-8,5,6,-8,-4,3,2,9,1,-7,6,5,1],[8,-7,-9,2,6,-1,6,-9,-3,-8,8,-6,-4,-7],[8,10,-7,1,-5,9,-2,4,-8,-4,6,3,1,-9],[2,5,-7,-6,-3,-10,1,-10,2,8,6,2,5,-6],[-5,-3,-2,-8,5,-3,2,-9,-5,-5,-2,8,6,2],[5,10,-4,10,-3,-6,4,-9,5,9,-6,8,9,5],[-7,-1,-6,6,-5,-7,7,-9,3,9,-7,-7,-5,10]],[[-2,-1,6,1,2,2,-4,-10,-10,-3,-6,-8,-1,7],[-1,-9,-3,-2,-4,-1,-10,6,9,6,4,4,-10,-4],[-9,-6,-7,3,-7,1,6,10,2,-4,3,-2,-9,-8],[1,9,-4,-10,10,-2,-6,10,2,2,5,7,-5,-4],[7,3,-3,-10,7,-7,3,6,4,-5,-6,-2,-2,9],[-2,-2,-3,9,-9,-5,8,3,-3,5,5,-4,7,-1],[7,-8,1,7,9,1,4,-2,8,-8,-8,-10,2,-3],[-2,-10,4,-9,10,-10,4,4,-9,-2,6,10,2,-7]]], dtype = "int16")#candidate|1638|(5, 8, 14)|const|int16
bop_1639 = relay.bitwise_or(var_1637.astype('int16'), const_1638.astype('int16')) # shape=(5, 8, 14)
bop_1644 = relay.add(bop_1639.astype('uint64'), var_1637.astype('uint64')) # shape=(5, 8, 14)
output = relay.Tuple([bop_1644,])
output2 = relay.Tuple([bop_1644,])
func_1656 = relay.Function([var_1637,], output)
mod['func_1656'] = func_1656
mod = relay.transform.InferType()(mod)
mutated_mod['func_1656'] = func_1656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1657 = relay.var("var_1657", dtype = "int16", shape = ())#candidate|1657|()|var|int16
func_1656_call = mutated_mod.get_global_var('func_1656')
call_1658 = func_1656_call(var_1657)
output = call_1658
func_1659 = relay.Function([var_1657], output)
mutated_mod['func_1659'] = func_1659
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1689 = relay.var("var_1689", dtype = "float32", shape = (4, 10, 12))#candidate|1689|(4, 10, 12)|var|float32
uop_1690 = relay.sigmoid(var_1689.astype('float32')) # shape=(4, 10, 12)
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
const_1705 = relay.const([-3.010643,-4.196287,-5.647499,3.063267,-0.496398,-6.516525,-5.332349,8.085451,-1.670174,0.736924,7.367079,4.380209,-5.765128,6.706093,-9.054767,5.994771,9.718801,6.909505,-0.671836,-1.301546,7.839707,7.055390,0.316062,-7.287497,-0.542904,-3.387362,-7.121354,1.282296,-5.009165,-9.644916,1.641094,-5.449170,7.924467,2.211279,-3.049075,5.086555,-5.509882,1.346424,1.144158,-6.163132,-5.615468,5.832230,-2.519363,5.415238,9.797190,0.317889,3.675756,6.989045,8.704649,8.871767,5.138700,4.501467,9.246020,4.822770,7.127154,-9.809889,-1.998697,-4.572999,6.727056,-4.243970,3.546568,5.492951,6.577349,5.025944,2.596238,-3.372314,2.747162,1.885464,0.528347,8.753980,-5.228168,-5.591561,6.935128,6.487797,-5.539206,-0.868376,-8.972264,2.715349,-8.471113,-1.378930,0.546656,-2.155864,2.942713,1.789608,-9.079034,0.827532,7.948236,-6.546288,-4.465852,8.135574,1.862338,-0.970409,5.655146,9.515672,-6.545446,-5.282796,-1.328415,9.567057,-1.843559,-8.732833,7.051647,2.473723,8.363728,-9.669441,1.786471,3.658824,3.002035,-7.208218,3.199068,-0.101783,-3.245720,3.842090,-4.383048,-0.286476,2.525895,1.538250,-2.121535,0.148030,-8.312859,0.164689,6.366772,-9.965998,-5.044613,-5.544076,-5.976027,1.227750,9.288301,-2.148668,8.497980,-3.153535,9.638539,-7.449679,-9.009421,-7.378107,7.000487,-0.111157,-6.475846,8.476607,-2.604404,-1.793422,-3.668504,1.644127,-7.651637,3.045602,-3.384436,-5.865466,-6.418594,3.325082,4.660976,9.328720,4.393774,8.438101,9.336602,-2.682451,-0.917205,-2.540940,-6.417832,-7.410309,4.357042,3.847693,0.575894,-0.779450,-1.890756,-6.438183,8.788568,-3.076901,-4.522690,-9.953054,-7.240219,2.188679,5.340463,4.044950,9.378258,-3.405690,-1.634768,-0.536860,2.002374,0.011674,-6.078421,5.011239,2.342279,-0.076192,-0.213110,4.659271,8.738984,4.172174,0.678024,-7.991594,5.964081,8.809640,-4.409812,8.034308,-7.135889,5.473666,0.446516,-3.748671,-3.618094,-9.695002,7.922053,2.875704,-6.665487,4.665845,-5.269138,-7.513159,-6.359828,6.896172,8.165277,6.162377,4.408698,-0.945200], dtype = "float32")#candidate|1705|(210,)|const|float32
call_1704 = relay.TupleGetItem(func_1397_call(relay.reshape(const_1705.astype('float32'), [210,])), 2)
call_1706 = relay.TupleGetItem(func_1399_call(relay.reshape(const_1705.astype('float32'), [210,])), 2)
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
var_1708 = relay.var("var_1708", dtype = "bool", shape = ())#candidate|1708|()|var|bool
call_1707 = relay.TupleGetItem(func_408_call(relay.reshape(var_1708.astype('bool'), [])), 2)
call_1709 = relay.TupleGetItem(func_411_call(relay.reshape(var_1708.astype('bool'), [])), 2)
output = relay.Tuple([uop_1690,call_1704,const_1705,call_1707,var_1708,])
output2 = relay.Tuple([uop_1690,call_1706,const_1705,call_1709,var_1708,])
func_1712 = relay.Function([var_1689,var_1708,], output)
mod['func_1712'] = func_1712
mod = relay.transform.InferType()(mod)
var_1713 = relay.var("var_1713", dtype = "float32", shape = (4, 10, 12))#candidate|1713|(4, 10, 12)|var|float32
var_1714 = relay.var("var_1714", dtype = "bool", shape = ())#candidate|1714|()|var|bool
output = func_1712(var_1713,var_1714,)
func_1715 = relay.Function([var_1713,var_1714,], output)
mutated_mod['func_1715'] = func_1715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1629_call = mod.get_global_var('func_1629')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_1832 = relay.TupleGetItem(func_1629_call(), 1)
call_1833 = relay.TupleGetItem(func_1631_call(), 1)
output = call_1832
output2 = call_1833
func_1840 = relay.Function([], output)
mod['func_1840'] = func_1840
mod = relay.transform.InferType()(mod)
mutated_mod['func_1840'] = func_1840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1840_call = mutated_mod.get_global_var('func_1840')
call_1841 = func_1840_call()
output = call_1841
func_1842 = relay.Function([], output)
mutated_mod['func_1842'] = func_1842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_1904 = relay.TupleGetItem(func_303_call(), 1)
call_1905 = relay.TupleGetItem(func_304_call(), 1)
output = call_1904
output2 = call_1905
func_1908 = relay.Function([], output)
mod['func_1908'] = func_1908
mod = relay.transform.InferType()(mod)
mutated_mod['func_1908'] = func_1908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1908_call = mutated_mod.get_global_var('func_1908')
call_1909 = func_1908_call()
output = call_1909
func_1910 = relay.Function([], output)
mutated_mod['func_1910'] = func_1910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1840_call = mod.get_global_var('func_1840')
func_1842_call = mutated_mod.get_global_var('func_1842')
call_1978 = func_1840_call()
call_1979 = func_1840_call()
func_1629_call = mod.get_global_var('func_1629')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_1980 = relay.TupleGetItem(func_1629_call(), 0)
call_1981 = relay.TupleGetItem(func_1631_call(), 0)
func_693_call = mod.get_global_var('func_693')
func_696_call = mutated_mod.get_global_var('func_696')
var_2006 = relay.var("var_2006", dtype = "uint8", shape = (6, 220))#candidate|2006|(6, 220)|var|uint8
call_2005 = relay.TupleGetItem(func_693_call(relay.reshape(var_2006.astype('uint8'), [15, 8, 11])), 0)
call_2007 = relay.TupleGetItem(func_696_call(relay.reshape(var_2006.astype('uint8'), [15, 8, 11])), 0)
func_514_call = mod.get_global_var('func_514')
func_516_call = mutated_mod.get_global_var('func_516')
call_2027 = func_514_call()
call_2028 = func_514_call()
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
var_2031 = relay.var("var_2031", dtype = "float32", shape = (210,))#candidate|2031|(210,)|var|float32
call_2030 = relay.TupleGetItem(func_1397_call(relay.reshape(var_2031.astype('float32'), [210,])), 2)
call_2032 = relay.TupleGetItem(func_1399_call(relay.reshape(var_2031.astype('float32'), [210,])), 2)
uop_2034 = relay.erf(call_2005.astype('float32')) # shape=(15, 8, 11)
uop_2036 = relay.erf(call_2007.astype('float32')) # shape=(15, 8, 11)
output = relay.Tuple([call_1978,call_1980,var_2006,call_2027,call_2030,var_2031,uop_2034,])
output2 = relay.Tuple([call_1979,call_1981,var_2006,call_2028,call_2032,var_2031,uop_2036,])
func_2072 = relay.Function([var_2006,var_2031,], output)
mod['func_2072'] = func_2072
mod = relay.transform.InferType()(mod)
mutated_mod['func_2072'] = func_2072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mutated_mod.get_global_var('func_2072')
var_2074 = relay.var("var_2074", dtype = "uint8", shape = (6, 220))#candidate|2074|(6, 220)|var|uint8
var_2075 = relay.var("var_2075", dtype = "float32", shape = (210,))#candidate|2075|(210,)|var|float32
call_2073 = func_2072_call(var_2074,var_2075,)
output = call_2073
func_2076 = relay.Function([var_2074,var_2075,], output)
mutated_mod['func_2076'] = func_2076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_2121 = func_325_call()
call_2122 = func_325_call()
output = relay.Tuple([call_2121,])
output2 = relay.Tuple([call_2122,])
func_2128 = relay.Function([], output)
mod['func_2128'] = func_2128
mod = relay.transform.InferType()(mod)
output = func_2128()
func_2129 = relay.Function([], output)
mutated_mod['func_2129'] = func_2129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1533_call = mod.get_global_var('func_1533')
func_1535_call = mutated_mod.get_global_var('func_1535')
call_2179 = relay.TupleGetItem(func_1533_call(), 1)
call_2180 = relay.TupleGetItem(func_1535_call(), 1)
func_52_call = mod.get_global_var('func_52')
func_54_call = mutated_mod.get_global_var('func_54')
var_2182 = relay.var("var_2182", dtype = "float64", shape = (240,))#candidate|2182|(240,)|var|float64
call_2181 = relay.TupleGetItem(func_52_call(relay.reshape(var_2182.astype('float64'), [12, 2, 10])), 0)
call_2183 = relay.TupleGetItem(func_54_call(relay.reshape(var_2182.astype('float64'), [12, 2, 10])), 0)
func_607_call = mod.get_global_var('func_607')
func_609_call = mutated_mod.get_global_var('func_609')
call_2188 = relay.TupleGetItem(func_607_call(relay.reshape(var_2182.astype('float64'), [240,])), 0)
call_2189 = relay.TupleGetItem(func_609_call(relay.reshape(var_2182.astype('float64'), [240,])), 0)
output = relay.Tuple([call_2179,call_2181,var_2182,call_2188,])
output2 = relay.Tuple([call_2180,call_2183,var_2182,call_2189,])
func_2192 = relay.Function([var_2182,], output)
mod['func_2192'] = func_2192
mod = relay.transform.InferType()(mod)
var_2193 = relay.var("var_2193", dtype = "float64", shape = (240,))#candidate|2193|(240,)|var|float64
output = func_2192(var_2193)
func_2194 = relay.Function([var_2193], output)
mutated_mod['func_2194'] = func_2194
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2199 = relay.var("var_2199", dtype = "float32", shape = (2, 9, 12))#candidate|2199|(2, 9, 12)|var|float32
uop_2200 = relay.acos(var_2199.astype('float32')) # shape=(2, 9, 12)
output = relay.Tuple([uop_2200,])
output2 = relay.Tuple([uop_2200,])
func_2205 = relay.Function([var_2199,], output)
mod['func_2205'] = func_2205
mod = relay.transform.InferType()(mod)
var_2206 = relay.var("var_2206", dtype = "float32", shape = (2, 9, 12))#candidate|2206|(2, 9, 12)|var|float32
output = func_2205(var_2206)
func_2207 = relay.Function([var_2206], output)
mutated_mod['func_2207'] = func_2207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1908_call = mod.get_global_var('func_1908')
func_1910_call = mutated_mod.get_global_var('func_1910')
call_2215 = func_1908_call()
call_2216 = func_1908_call()
func_1454_call = mod.get_global_var('func_1454')
func_1455_call = mutated_mod.get_global_var('func_1455')
call_2227 = relay.TupleGetItem(func_1454_call(), 0)
call_2228 = relay.TupleGetItem(func_1455_call(), 0)
func_1840_call = mod.get_global_var('func_1840')
func_1842_call = mutated_mod.get_global_var('func_1842')
call_2229 = func_1840_call()
call_2230 = func_1840_call()
func_174_call = mod.get_global_var('func_174')
func_176_call = mutated_mod.get_global_var('func_176')
var_2236 = relay.var("var_2236", dtype = "bool", shape = ())#candidate|2236|()|var|bool
call_2235 = relay.TupleGetItem(func_174_call(relay.reshape(var_2236.astype('bool'), [])), 0)
call_2237 = relay.TupleGetItem(func_176_call(relay.reshape(var_2236.astype('bool'), [])), 0)
output = relay.Tuple([call_2215,call_2227,call_2229,call_2235,var_2236,])
output2 = relay.Tuple([call_2216,call_2228,call_2230,call_2237,var_2236,])
func_2256 = relay.Function([var_2236,], output)
mod['func_2256'] = func_2256
mod = relay.transform.InferType()(mod)
var_2257 = relay.var("var_2257", dtype = "bool", shape = ())#candidate|2257|()|var|bool
output = func_2256(var_2257)
func_2258 = relay.Function([var_2257], output)
mutated_mod['func_2258'] = func_2258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1010_call = mod.get_global_var('func_1010')
func_1011_call = mutated_mod.get_global_var('func_1011')
call_2339 = relay.TupleGetItem(func_1010_call(), 1)
call_2340 = relay.TupleGetItem(func_1011_call(), 1)
output = relay.Tuple([call_2339,])
output2 = relay.Tuple([call_2340,])
func_2343 = relay.Function([], output)
mod['func_2343'] = func_2343
mod = relay.transform.InferType()(mod)
mutated_mod['func_2343'] = func_2343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2343_call = mutated_mod.get_global_var('func_2343')
call_2344 = func_2343_call()
output = call_2344
func_2345 = relay.Function([], output)
mutated_mod['func_2345'] = func_2345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1908_call = mod.get_global_var('func_1908')
func_1910_call = mutated_mod.get_global_var('func_1910')
call_2348 = func_1908_call()
call_2349 = func_1908_call()
output = relay.Tuple([call_2348,])
output2 = relay.Tuple([call_2349,])
func_2352 = relay.Function([], output)
mod['func_2352'] = func_2352
mod = relay.transform.InferType()(mod)
mutated_mod['func_2352'] = func_2352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2352_call = mutated_mod.get_global_var('func_2352')
call_2353 = func_2352_call()
output = call_2353
func_2354 = relay.Function([], output)
mutated_mod['func_2354'] = func_2354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1908_call = mod.get_global_var('func_1908')
func_1910_call = mutated_mod.get_global_var('func_1910')
call_2432 = func_1908_call()
call_2433 = func_1908_call()
output = call_2432
output2 = call_2433
func_2436 = relay.Function([], output)
mod['func_2436'] = func_2436
mod = relay.transform.InferType()(mod)
output = func_2436()
func_2437 = relay.Function([], output)
mutated_mod['func_2437'] = func_2437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1629_call = mod.get_global_var('func_1629')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_2462 = relay.TupleGetItem(func_1629_call(), 0)
call_2463 = relay.TupleGetItem(func_1631_call(), 0)
func_2436_call = mod.get_global_var('func_2436')
func_2437_call = mutated_mod.get_global_var('func_2437')
call_2466 = func_2436_call()
call_2467 = func_2436_call()
func_1087_call = mod.get_global_var('func_1087')
func_1090_call = mutated_mod.get_global_var('func_1090')
const_2502 = relay.const([5.362131,4.749111,6.722768,9.947826,5.353839,7.186480,-1.846980,-0.747065,0.817974,-8.663741,-9.388045,-7.164523,-5.698845,-4.131108,-8.938617,5.261692,-6.271048,0.255699,-7.391951,3.250460,9.022144,2.265331,-4.070756,-7.085277,0.219603,-4.047536,8.155403,0.072186,9.323534,-8.579442,-2.063686,5.077872,-4.185447,-4.980108,9.911169,-0.985414,-2.579273,0.436526,6.223875,4.307094,-6.927747,2.093963,-2.663740,5.587815,-7.721819,3.427408,7.537939,0.874177,9.134551,7.772208,9.636412,-7.677186,4.005298,3.601114,3.600499,7.462494,-8.899917,-0.045368,-4.287656,-3.489432,7.620259,3.355727,8.229426,-4.249555,-8.710850,7.656574,-0.632675,-1.497526,1.909338,-7.388613,-7.801083,8.451391,-3.445648,3.906912,9.641308,1.938715,6.754604,-5.803484,7.601303,-8.032531,-5.268271,-4.374137,9.862089,-5.479762,-0.404218,7.701196,-0.077916,0.597492,-5.585833,5.952129,-3.411418,-2.965428,9.369129,-2.972378,-5.755147,9.096734,1.662047,5.823264,-7.857222,6.543488,-0.503694,2.349610,9.028084,-7.687310,9.855036,-0.183812,-1.153996,4.271791,4.775807,0.339775,-3.048918,-1.917116,-4.744337,-3.513330,7.550758,3.564002,0.955918,-6.152668,9.064742,-4.236358,8.270418,-3.746288,-6.866780,9.361877,-6.152993,5.206480,2.063784,-3.667474,0.512902,-2.921287,-3.204782,-2.998169,-4.029297,4.221240,3.287036,-6.185465,-3.281439,4.502840,8.036538,-5.581586,8.197312,-4.988911,7.821241,-0.330911,-7.844769,5.306932,-1.603804,-5.857212,-3.438121,-4.914691,1.114908,-1.802093,5.533545,-6.381532,6.426266,-1.861359,-1.991659,2.889552,3.409413,-7.696331,6.451614,4.605678,-6.803010,-1.495128,2.918108,-1.090947,-1.398591,-7.992284,-5.793720,-5.745740,0.988663,-3.785043,4.170538,8.223435,5.831832,-9.363826,1.126815,-8.433685,4.304896,-4.451528,8.836841,-0.139623,-4.977559,-5.747699,7.531394,-5.436388,3.265920,4.177009,-2.392682,-3.023049,-0.623862,-4.707924,-3.893551,5.098676,-0.855086,-5.311371,0.063855,8.751492,3.885660,-0.627024,-9.135519,8.271482,-7.641206,-4.790287,3.731061,-1.362288,-3.108534,7.339315,-4.955256,-4.270765], dtype = "float32")#candidate|2502|(210,)|const|float32
var_2503 = relay.var("var_2503", dtype = "float64", shape = (630,))#candidate|2503|(630,)|var|float64
call_2501 = relay.TupleGetItem(func_1087_call(relay.reshape(const_2502.astype('float32'), [14, 15, 1]), relay.reshape(var_2503.astype('float64'), [14, 15, 3]), ), 0)
call_2504 = relay.TupleGetItem(func_1090_call(relay.reshape(const_2502.astype('float32'), [14, 15, 1]), relay.reshape(var_2503.astype('float64'), [14, 15, 3]), ), 0)
var_2505 = relay.var("var_2505", dtype = "int64", shape = (9, 12, 15))#candidate|2505|(9, 12, 15)|var|int64
bop_2506 = relay.mod(call_2462.astype('float64'), relay.reshape(var_2505.astype('float64'), relay.shape_of(call_2462))) # shape=(9, 12, 15)
bop_2509 = relay.mod(call_2463.astype('float64'), relay.reshape(var_2505.astype('float64'), relay.shape_of(call_2463))) # shape=(9, 12, 15)
func_2205_call = mod.get_global_var('func_2205')
func_2207_call = mutated_mod.get_global_var('func_2207')
const_2512 = relay.const([-0.777270,0.663557,6.588617,3.242112,5.843654,-2.886135,4.053315,5.422804,-1.299102,-0.653939,4.824617,7.180386,8.222064,-0.779126,-1.639142,-6.772383,7.528591,0.276316,4.418988,-1.230994,-5.284094,-4.255435,8.770366,-1.210513,-5.046996,-4.571569,5.243521,1.349012,4.334901,7.972647,-5.901358,7.625038,2.650312,3.789147,8.862162,1.806371,-5.348089,5.522746,0.111231,2.100311,-4.024586,8.169096,7.575727,6.042424,-4.160936,0.635248,-6.237940,-3.702923,1.905558,-3.571022,-7.547240,-9.913318,4.183564,-0.724204,7.606833,-7.564133,6.206900,2.733899,6.805489,-5.897016,8.390948,-2.211814,-2.169297,2.420967,-1.975411,-0.334293,8.352014,-1.888336,9.271734,7.882568,-9.909441,-3.701411,3.699073,2.123531,-4.107199,-5.951964,4.475629,6.422658,-0.629810,3.609061,-9.345353,3.096697,-9.161761,-6.906830,-2.259035,-4.369958,-4.935169,9.563058,-0.055662,-9.863174,-9.457454,-5.687815,6.313921,6.546472,-9.820266,0.370485,-6.463564,-9.776367,-2.415938,-2.416207,-1.735831,6.590077,-3.658751,-0.671442,7.032111,4.717775,4.350182,9.088813,-6.428917,-8.996819,0.671448,4.821475,-8.695895,-3.896543,3.312851,-9.480033,1.321727,-8.280446,-0.858587,-4.522965,2.292062,5.898291,2.667427,7.785323,4.473863,-8.811183,2.034667,-5.539510,9.166182,-8.690006,-7.520189,-1.640677,2.336355,0.178685,5.903328,8.236172,4.295781,-3.918544,-9.628724,-2.689354,3.000180,-6.931273,5.470852,6.306178,-6.326031,4.626085,-1.538634,-6.240417,-7.563081,7.950952,-6.665412,-8.255539,9.314282,-7.843034,-4.946469,0.097713,-3.326857,6.029360,-8.674159,-3.549198,-2.706477,4.215661,-0.664853,-7.145981,2.047424,-2.439064,5.407884,-1.225433,0.963848,-0.142884,2.523628,-5.152377,2.615941,3.209085,-1.122855,-5.253735,8.008171,2.836254,-6.601801,-3.589863,6.772239,5.564981,5.268233,7.288526,-1.476076,4.771184,0.800320,2.923144,2.273118,-0.384826,6.913969,-9.341788,5.424761,-0.373407,-0.056775,1.910442,4.436620,-8.745315,-6.074934,-7.410748,5.683118,6.328736,5.341358,4.093322,3.276177,-9.875718,4.447517,-2.540966,-7.607475,-2.499176,3.259979,-2.010011,-4.062187,-2.650089,-3.324296,4.783929], dtype = "float32")#candidate|2512|(216,)|const|float32
call_2511 = relay.TupleGetItem(func_2205_call(relay.reshape(const_2512.astype('float32'), [2, 9, 12])), 0)
call_2513 = relay.TupleGetItem(func_2207_call(relay.reshape(const_2512.astype('float32'), [2, 9, 12])), 0)
func_1176_call = mod.get_global_var('func_1176')
func_1178_call = mutated_mod.get_global_var('func_1178')
call_2514 = relay.TupleGetItem(func_1176_call(relay.reshape(call_2462.astype('uint16'), [9, 12, 15])), 3)
call_2515 = relay.TupleGetItem(func_1178_call(relay.reshape(call_2462.astype('uint16'), [9, 12, 15])), 3)
func_1656_call = mod.get_global_var('func_1656')
func_1659_call = mutated_mod.get_global_var('func_1659')
var_2523 = relay.var("var_2523", dtype = "int16", shape = ())#candidate|2523|()|var|int16
call_2522 = relay.TupleGetItem(func_1656_call(relay.reshape(var_2523.astype('int16'), [])), 0)
call_2524 = relay.TupleGetItem(func_1659_call(relay.reshape(var_2523.astype('int16'), [])), 0)
func_1656_call = mod.get_global_var('func_1656')
func_1659_call = mutated_mod.get_global_var('func_1659')
call_2526 = relay.TupleGetItem(func_1656_call(relay.reshape(var_2523.astype('int16'), [])), 0)
call_2527 = relay.TupleGetItem(func_1659_call(relay.reshape(var_2523.astype('int16'), [])), 0)
func_1454_call = mod.get_global_var('func_1454')
func_1455_call = mutated_mod.get_global_var('func_1455')
call_2529 = relay.TupleGetItem(func_1454_call(), 0)
call_2530 = relay.TupleGetItem(func_1455_call(), 0)
output = relay.Tuple([call_2466,call_2501,const_2502,var_2503,bop_2506,call_2511,const_2512,call_2514,call_2522,var_2523,call_2526,call_2529,])
output2 = relay.Tuple([call_2467,call_2504,const_2502,var_2503,bop_2509,call_2513,const_2512,call_2515,call_2524,var_2523,call_2527,call_2530,])
func_2532 = relay.Function([var_2503,var_2505,var_2523,], output)
mod['func_2532'] = func_2532
mod = relay.transform.InferType()(mod)
var_2533 = relay.var("var_2533", dtype = "float64", shape = (630,))#candidate|2533|(630,)|var|float64
var_2534 = relay.var("var_2534", dtype = "int64", shape = (9, 12, 15))#candidate|2534|(9, 12, 15)|var|int64
var_2535 = relay.var("var_2535", dtype = "int16", shape = ())#candidate|2535|()|var|int16
output = func_2532(var_2533,var_2534,var_2535,)
func_2536 = relay.Function([var_2533,var_2534,var_2535,], output)
mutated_mod['func_2536'] = func_2536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2343_call = mod.get_global_var('func_2343')
func_2345_call = mutated_mod.get_global_var('func_2345')
call_2549 = relay.TupleGetItem(func_2343_call(), 0)
call_2550 = relay.TupleGetItem(func_2345_call(), 0)
output = relay.Tuple([call_2549,])
output2 = relay.Tuple([call_2550,])
func_2551 = relay.Function([], output)
mod['func_2551'] = func_2551
mod = relay.transform.InferType()(mod)
mutated_mod['func_2551'] = func_2551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2551_call = mutated_mod.get_global_var('func_2551')
call_2552 = func_2551_call()
output = call_2552
func_2553 = relay.Function([], output)
mutated_mod['func_2553'] = func_2553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2343_call = mod.get_global_var('func_2343')
func_2345_call = mutated_mod.get_global_var('func_2345')
call_2564 = relay.TupleGetItem(func_2343_call(), 0)
call_2565 = relay.TupleGetItem(func_2345_call(), 0)
uop_2567 = relay.erf(call_2564.astype('float32')) # shape=(9, 12, 15)
uop_2569 = relay.erf(call_2565.astype('float32')) # shape=(9, 12, 15)
output = relay.Tuple([uop_2567,])
output2 = relay.Tuple([uop_2569,])
func_2579 = relay.Function([], output)
mod['func_2579'] = func_2579
mod = relay.transform.InferType()(mod)
mutated_mod['func_2579'] = func_2579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2579_call = mutated_mod.get_global_var('func_2579')
call_2580 = func_2579_call()
output = call_2580
func_2581 = relay.Function([], output)
mutated_mod['func_2581'] = func_2581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1629_call = mod.get_global_var('func_1629')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_2668 = relay.TupleGetItem(func_1629_call(), 0)
call_2669 = relay.TupleGetItem(func_1631_call(), 0)
output = relay.Tuple([call_2668,])
output2 = relay.Tuple([call_2669,])
func_2672 = relay.Function([], output)
mod['func_2672'] = func_2672
mod = relay.transform.InferType()(mod)
output = func_2672()
func_2673 = relay.Function([], output)
mutated_mod['func_2673'] = func_2673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2128_call = mod.get_global_var('func_2128')
func_2129_call = mutated_mod.get_global_var('func_2129')
call_2700 = relay.TupleGetItem(func_2128_call(), 0)
call_2701 = relay.TupleGetItem(func_2129_call(), 0)
output = call_2700
output2 = call_2701
func_2711 = relay.Function([], output)
mod['func_2711'] = func_2711
mod = relay.transform.InferType()(mod)
mutated_mod['func_2711'] = func_2711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2711_call = mutated_mod.get_global_var('func_2711')
call_2712 = func_2711_call()
output = call_2712
func_2713 = relay.Function([], output)
mutated_mod['func_2713'] = func_2713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_2748 = relay.TupleGetItem(func_723_call(), 0)
call_2749 = relay.TupleGetItem(func_725_call(), 0)
func_514_call = mod.get_global_var('func_514')
func_516_call = mutated_mod.get_global_var('func_516')
call_2750 = func_514_call()
call_2751 = func_514_call()
func_1283_call = mod.get_global_var('func_1283')
func_1285_call = mutated_mod.get_global_var('func_1285')
var_2765 = relay.var("var_2765", dtype = "float32", shape = (1, 490))#candidate|2765|(1, 490)|var|float32
call_2764 = relay.TupleGetItem(func_1283_call(relay.reshape(var_2765.astype('float32'), [490,])), 0)
call_2766 = relay.TupleGetItem(func_1285_call(relay.reshape(var_2765.astype('float32'), [490,])), 0)
output = relay.Tuple([call_2748,call_2750,call_2764,var_2765,])
output2 = relay.Tuple([call_2749,call_2751,call_2766,var_2765,])
func_2781 = relay.Function([var_2765,], output)
mod['func_2781'] = func_2781
mod = relay.transform.InferType()(mod)
mutated_mod['func_2781'] = func_2781
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2782 = relay.var("var_2782", dtype = "float32", shape = (1, 490))#candidate|2782|(1, 490)|var|float32
func_2781_call = mutated_mod.get_global_var('func_2781')
call_2783 = func_2781_call(var_2782)
output = call_2783
func_2784 = relay.Function([var_2782], output)
mutated_mod['func_2784'] = func_2784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1533_call = mod.get_global_var('func_1533')
func_1535_call = mutated_mod.get_global_var('func_1535')
call_2834 = relay.TupleGetItem(func_1533_call(), 1)
call_2835 = relay.TupleGetItem(func_1535_call(), 1)
func_1397_call = mod.get_global_var('func_1397')
func_1399_call = mutated_mod.get_global_var('func_1399')
var_2837 = relay.var("var_2837", dtype = "float32", shape = (210,))#candidate|2837|(210,)|var|float32
call_2836 = relay.TupleGetItem(func_1397_call(relay.reshape(var_2837.astype('float32'), [210,])), 0)
call_2838 = relay.TupleGetItem(func_1399_call(relay.reshape(var_2837.astype('float32'), [210,])), 0)
output = relay.Tuple([call_2834,call_2836,var_2837,])
output2 = relay.Tuple([call_2835,call_2838,var_2837,])
func_2857 = relay.Function([var_2837,], output)
mod['func_2857'] = func_2857
mod = relay.transform.InferType()(mod)
mutated_mod['func_2857'] = func_2857
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2858 = relay.var("var_2858", dtype = "float32", shape = (210,))#candidate|2858|(210,)|var|float32
func_2857_call = mutated_mod.get_global_var('func_2857')
call_2859 = func_2857_call(var_2858)
output = call_2859
func_2860 = relay.Function([var_2858], output)
mutated_mod['func_2860'] = func_2860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1629_call = mod.get_global_var('func_1629')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_2877 = relay.TupleGetItem(func_1629_call(), 0)
call_2878 = relay.TupleGetItem(func_1631_call(), 0)
output = call_2877
output2 = call_2878
func_2881 = relay.Function([], output)
mod['func_2881'] = func_2881
mod = relay.transform.InferType()(mod)
mutated_mod['func_2881'] = func_2881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2881_call = mutated_mod.get_global_var('func_2881')
call_2882 = func_2881_call()
output = call_2882
func_2883 = relay.Function([], output)
mutated_mod['func_2883'] = func_2883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2551_call = mod.get_global_var('func_2551')
func_2553_call = mutated_mod.get_global_var('func_2553')
call_2884 = relay.TupleGetItem(func_2551_call(), 0)
call_2885 = relay.TupleGetItem(func_2553_call(), 0)
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
var_2902 = relay.var("var_2902", dtype = "bool", shape = ())#candidate|2902|()|var|bool
call_2901 = relay.TupleGetItem(func_408_call(relay.reshape(var_2902.astype('bool'), [])), 5)
call_2903 = relay.TupleGetItem(func_411_call(relay.reshape(var_2902.astype('bool'), [])), 5)
uop_2909 = relay.asin(call_2901.astype('float32')) # shape=(12, 2, 10)
uop_2911 = relay.asin(call_2903.astype('float32')) # shape=(12, 2, 10)
output = relay.Tuple([call_2884,var_2902,uop_2909,])
output2 = relay.Tuple([call_2885,var_2902,uop_2911,])
func_2915 = relay.Function([var_2902,], output)
mod['func_2915'] = func_2915
mod = relay.transform.InferType()(mod)
mutated_mod['func_2915'] = func_2915
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2916 = relay.var("var_2916", dtype = "bool", shape = ())#candidate|2916|()|var|bool
func_2915_call = mutated_mod.get_global_var('func_2915')
call_2917 = func_2915_call(var_2916)
output = call_2917
func_2918 = relay.Function([var_2916], output)
mutated_mod['func_2918'] = func_2918
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3038 = relay.var("var_3038", dtype = "uint64", shape = ())#candidate|3038|()|var|uint64
var_3039 = relay.var("var_3039", dtype = "uint64", shape = (3, 1, 1))#candidate|3039|(3, 1, 1)|var|uint64
bop_3040 = relay.bitwise_and(var_3038.astype('uint64'), var_3039.astype('uint64')) # shape=(3, 1, 1)
output = relay.Tuple([bop_3040,])
output2 = relay.Tuple([bop_3040,])
func_3043 = relay.Function([var_3038,var_3039,], output)
mod['func_3043'] = func_3043
mod = relay.transform.InferType()(mod)
mutated_mod['func_3043'] = func_3043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3043_call = mutated_mod.get_global_var('func_3043')
var_3045 = relay.var("var_3045", dtype = "uint64", shape = ())#candidate|3045|()|var|uint64
var_3046 = relay.var("var_3046", dtype = "uint64", shape = (3, 1, 1))#candidate|3046|(3, 1, 1)|var|uint64
call_3044 = func_3043_call(var_3045,var_3046,)
output = call_3044
func_3047 = relay.Function([var_3045,var_3046,], output)
mutated_mod['func_3047'] = func_3047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2128_call = mod.get_global_var('func_2128')
func_2129_call = mutated_mod.get_global_var('func_2129')
call_3057 = relay.TupleGetItem(func_2128_call(), 0)
call_3058 = relay.TupleGetItem(func_2129_call(), 0)
output = relay.Tuple([call_3057,])
output2 = relay.Tuple([call_3058,])
func_3060 = relay.Function([], output)
mod['func_3060'] = func_3060
mod = relay.transform.InferType()(mod)
output = func_3060()
func_3061 = relay.Function([], output)
mutated_mod['func_3061'] = func_3061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1908_call = mod.get_global_var('func_1908')
func_1910_call = mutated_mod.get_global_var('func_1910')
call_3153 = func_1908_call()
call_3154 = func_1908_call()
func_2192_call = mod.get_global_var('func_2192')
func_2194_call = mutated_mod.get_global_var('func_2194')
call_3156 = relay.TupleGetItem(func_2192_call(relay.reshape(call_3153.astype('float64'), [240,])), 2)
call_3157 = relay.TupleGetItem(func_2194_call(relay.reshape(call_3153.astype('float64'), [240,])), 2)
output = relay.Tuple([call_3153,call_3156,])
output2 = relay.Tuple([call_3154,call_3157,])
func_3158 = relay.Function([], output)
mod['func_3158'] = func_3158
mod = relay.transform.InferType()(mod)
mutated_mod['func_3158'] = func_3158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3158_call = mutated_mod.get_global_var('func_3158')
call_3159 = func_3158_call()
output = call_3159
func_3160 = relay.Function([], output)
mutated_mod['func_3160'] = func_3160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2711_call = mod.get_global_var('func_2711')
func_2713_call = mutated_mod.get_global_var('func_2713')
call_3163 = func_2711_call()
call_3164 = func_2711_call()
func_937_call = mod.get_global_var('func_937')
func_938_call = mutated_mod.get_global_var('func_938')
call_3169 = relay.TupleGetItem(func_937_call(), 0)
call_3170 = relay.TupleGetItem(func_938_call(), 0)
func_493_call = mod.get_global_var('func_493')
func_497_call = mutated_mod.get_global_var('func_497')
var_3172 = relay.var("var_3172", dtype = "float32", shape = (1, 858))#candidate|3172|(1, 858)|var|float32
call_3171 = relay.TupleGetItem(func_493_call(relay.reshape(var_3172.astype('float32'), [11, 6, 13]), relay.reshape(var_3172.astype('float32'), [11, 6, 13]), relay.reshape(call_3169.astype('float64'), [240, 1]), ), 3)
call_3173 = relay.TupleGetItem(func_497_call(relay.reshape(var_3172.astype('float32'), [11, 6, 13]), relay.reshape(var_3172.astype('float32'), [11, 6, 13]), relay.reshape(call_3169.astype('float64'), [240, 1]), ), 3)
output = relay.Tuple([call_3163,call_3169,call_3171,var_3172,])
output2 = relay.Tuple([call_3164,call_3170,call_3173,var_3172,])
func_3182 = relay.Function([var_3172,], output)
mod['func_3182'] = func_3182
mod = relay.transform.InferType()(mod)
mutated_mod['func_3182'] = func_3182
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3183 = relay.var("var_3183", dtype = "float32", shape = (1, 858))#candidate|3183|(1, 858)|var|float32
func_3182_call = mutated_mod.get_global_var('func_3182')
call_3184 = func_3182_call(var_3183)
output = call_3184
func_3185 = relay.Function([var_3183], output)
mutated_mod['func_3185'] = func_3185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_3225 = func_2881_call()
call_3226 = func_2881_call()
func_1087_call = mod.get_global_var('func_1087')
func_1090_call = mutated_mod.get_global_var('func_1090')
const_3259 = relay.const([2.044264,5.867768,-8.473977,-8.815133,-3.549694,2.545091,2.085346,2.298450,0.111643,5.657645,8.605237,-8.510158,8.326191,-5.934287,0.656066,-9.906145,6.234441,-2.748845,-1.733128,-7.912015,0.301247,-5.349390,-2.865263,7.890254,9.478505,-2.691101,-8.773486,4.548006,0.517446,-0.275286,8.205330,4.369786,-5.232317,-5.310245,7.861450,1.029390,9.535619,7.386967,5.227661,0.116492,5.772598,6.978469,-4.935878,-7.597728,7.024062,-3.947700,9.717194,3.721118,8.727862,-2.505629,-0.401499,5.044641,7.436616,-3.040400,-1.848328,6.069011,4.111393,1.145294,-0.843196,3.968072,-3.903848,-2.567113,-8.354536,0.471119,-4.654301,-0.769463,3.986830,-5.504283,-0.140100,4.893753,-4.643232,-1.712404,0.596340,6.709174,8.404798,8.590285,-2.548901,3.427734,-4.749113,-5.816973,2.367530,4.545322,5.523309,6.156438,-1.268808,-4.016083,-7.087062,9.114750,-0.006542,3.124065,4.565119,7.299578,-1.278380,-2.159032,3.086512,1.998828,6.347283,4.547470,-9.100190,-2.152190,4.955775,0.691551,-5.161201,7.417428,0.108248,-3.789715,-1.835425,-5.537931,9.793486,8.295405,-0.070401,7.514873,3.903577,-5.428251,9.530942,0.291280,6.765973,-2.814600,7.667887,-6.057006,-3.195879,0.563187,-2.408021,-5.127681,4.332570,-8.761187,-2.339655,3.311247,-5.210694,-6.203563,1.903145,-9.232968,-2.215370,-3.642877,-7.050448,3.243947,7.864429,0.756681,-2.763547,4.978104,9.227743,0.659168,3.952601,-1.016642,-1.724327,-4.649028,-1.147950,-9.643539,9.142991,-7.298986,8.557126,8.859532,-7.558899,-5.316683,-6.027697,-6.421098,8.254416,2.536332,6.099746,-1.920853,-6.950638,3.121871,6.477008,-5.761437,-4.188745,6.921874,-2.928044,-2.963490,0.328152,9.384556,3.965022,-5.658669,-8.569663,9.230541,6.505507,3.091215,-7.417812,-2.078647,0.860358,7.948023,9.585368,3.153557,8.631733,-1.474196,5.842122,-3.331148,-2.167165,7.662573,-6.881574,-3.267612,5.316580,-8.561584,-5.351608,3.942718,4.417305,9.352147,5.270166,-5.174445,-8.511320,-9.912422,-1.282509,-7.586691,1.536362,3.149683,9.324483,3.011060,-8.550476,-6.645905,-3.468330,-6.852941], dtype = "float32")#candidate|3259|(210,)|const|float32
var_3260 = relay.var("var_3260", dtype = "float64", shape = (630,))#candidate|3260|(630,)|var|float64
call_3258 = relay.TupleGetItem(func_1087_call(relay.reshape(const_3259.astype('float32'), [14, 15, 1]), relay.reshape(var_3260.astype('float64'), [14, 15, 3]), ), 2)
call_3261 = relay.TupleGetItem(func_1090_call(relay.reshape(const_3259.astype('float32'), [14, 15, 1]), relay.reshape(var_3260.astype('float64'), [14, 15, 3]), ), 2)
func_937_call = mod.get_global_var('func_937')
func_938_call = mutated_mod.get_global_var('func_938')
call_3262 = relay.TupleGetItem(func_937_call(), 0)
call_3263 = relay.TupleGetItem(func_938_call(), 0)
func_937_call = mod.get_global_var('func_937')
func_938_call = mutated_mod.get_global_var('func_938')
call_3270 = relay.TupleGetItem(func_937_call(), 0)
call_3271 = relay.TupleGetItem(func_938_call(), 0)
uop_3297 = relay.erf(call_3258.astype('float32')) # shape=(14, 15, 3)
uop_3299 = relay.erf(call_3261.astype('float32')) # shape=(14, 15, 3)
func_2343_call = mod.get_global_var('func_2343')
func_2345_call = mutated_mod.get_global_var('func_2345')
call_3301 = relay.TupleGetItem(func_2343_call(), 0)
call_3302 = relay.TupleGetItem(func_2345_call(), 0)
output = relay.Tuple([call_3225,const_3259,var_3260,call_3262,call_3270,uop_3297,call_3301,])
output2 = relay.Tuple([call_3226,const_3259,var_3260,call_3263,call_3271,uop_3299,call_3302,])
func_3311 = relay.Function([var_3260,], output)
mod['func_3311'] = func_3311
mod = relay.transform.InferType()(mod)
var_3312 = relay.var("var_3312", dtype = "float64", shape = (630,))#candidate|3312|(630,)|var|float64
output = func_3311(var_3312)
func_3313 = relay.Function([var_3312], output)
mutated_mod['func_3313'] = func_3313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3361 = relay.var("var_3361", dtype = "float64", shape = ())#candidate|3361|()|var|float64
var_3362 = relay.var("var_3362", dtype = "float64", shape = (5, 4, 1))#candidate|3362|(5, 4, 1)|var|float64
bop_3363 = relay.power(var_3361.astype('float64'), var_3362.astype('float64')) # shape=(5, 4, 1)
uop_3368 = relay.exp(var_3362.astype('float64')) # shape=(5, 4, 1)
uop_3381 = relay.atanh(uop_3368.astype('float64')) # shape=(5, 4, 1)
output = relay.Tuple([bop_3363,uop_3381,])
output2 = relay.Tuple([bop_3363,uop_3381,])
func_3383 = relay.Function([var_3361,var_3362,], output)
mod['func_3383'] = func_3383
mod = relay.transform.InferType()(mod)
var_3384 = relay.var("var_3384", dtype = "float64", shape = ())#candidate|3384|()|var|float64
var_3385 = relay.var("var_3385", dtype = "float64", shape = (5, 4, 1))#candidate|3385|(5, 4, 1)|var|float64
output = func_3383(var_3384,var_3385,)
func_3386 = relay.Function([var_3384,var_3385,], output)
mutated_mod['func_3386'] = func_3386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1629_call = mod.get_global_var('func_1629')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_3388 = relay.TupleGetItem(func_1629_call(), 0)
call_3389 = relay.TupleGetItem(func_1631_call(), 0)
var_3394 = relay.var("var_3394", dtype = "int64", shape = (9, 12, 15))#candidate|3394|(9, 12, 15)|var|int64
bop_3395 = relay.logical_or(call_3388.astype('bool'), relay.reshape(var_3394.astype('bool'), relay.shape_of(call_3388))) # shape=(9, 12, 15)
bop_3398 = relay.logical_or(call_3389.astype('bool'), relay.reshape(var_3394.astype('bool'), relay.shape_of(call_3389))) # shape=(9, 12, 15)
func_3043_call = mod.get_global_var('func_3043')
func_3047_call = mutated_mod.get_global_var('func_3047')
const_3405 = relay.const(2, dtype = "uint64")#candidate|3405|()|const|uint64
const_3406 = relay.const([10,-8,6], dtype = "uint64")#candidate|3406|(3,)|const|uint64
call_3404 = relay.TupleGetItem(func_3043_call(relay.reshape(const_3405.astype('uint64'), []), relay.reshape(const_3406.astype('uint64'), [3, 1, 1]), ), 0)
call_3407 = relay.TupleGetItem(func_3047_call(relay.reshape(const_3405.astype('uint64'), []), relay.reshape(const_3406.astype('uint64'), [3, 1, 1]), ), 0)
output = relay.Tuple([bop_3395,call_3404,const_3405,const_3406,])
output2 = relay.Tuple([bop_3398,call_3407,const_3405,const_3406,])
func_3408 = relay.Function([var_3394,], output)
mod['func_3408'] = func_3408
mod = relay.transform.InferType()(mod)
mutated_mod['func_3408'] = func_3408
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3409 = relay.var("var_3409", dtype = "int64", shape = (9, 12, 15))#candidate|3409|(9, 12, 15)|var|int64
func_3408_call = mutated_mod.get_global_var('func_3408')
call_3410 = func_3408_call(var_3409)
output = call_3410
func_3411 = relay.Function([var_3409], output)
mutated_mod['func_3411'] = func_3411
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3444 = relay.var("var_3444", dtype = "float64", shape = ())#candidate|3444|()|var|float64
const_3445 = relay.const([[[8.716417,6.658624,9.372240,2.665289,1.750177,3.147814,-4.054490,5.552383,-3.530276,9.900908,-3.939156,-9.212280,1.418647],[0.457650,3.517621,9.584093,-7.529609,7.518984,9.326668,0.310348,8.957655,-0.848675,2.500212,2.368508,7.402619,8.835179],[-6.761911,5.157879,6.011909,-0.909473,-0.835408,5.716887,-6.853519,-8.116247,4.363601,-0.192117,-0.366639,-3.961232,-3.542248],[2.666658,-2.516911,3.827960,-8.308127,-8.122696,4.484468,-3.989263,2.607808,5.114730,-4.177286,8.972502,5.966683,-3.531101],[-7.400235,0.418346,-9.518321,-0.740024,0.194811,2.783247,6.245886,9.117570,-9.572625,-9.087875,-8.233483,-1.955309,0.711330],[-3.417663,7.362164,0.475870,-9.357041,5.376553,5.118625,1.604705,9.492919,6.536260,4.933803,-6.763143,-2.845830,4.055362],[-4.442189,-0.498530,4.950736,-3.711368,7.522629,-7.780481,9.220409,4.185027,-4.444128,7.079629,7.581793,-1.222944,-9.148316],[4.213681,3.780436,6.841436,-5.490842,0.826723,-2.350285,-7.392959,9.798739,0.375752,-0.795055,-5.483203,-4.031172,6.354036],[-4.003565,-3.347989,-7.583044,6.383619,-9.819785,3.360155,-0.726134,-9.352125,-4.290066,6.666520,7.784144,-3.502192,7.667999],[-4.582118,5.796129,0.518564,1.486351,-4.762542,5.183815,3.163184,-6.503014,-6.396021,-7.406299,8.027891,-1.260796,-0.256826],[-9.065814,7.033593,5.085112,2.778459,9.723413,-6.734652,-8.966639,-1.084038,9.386416,8.565029,-9.608126,-9.540408,-5.846167],[-2.776762,-6.040196,-3.333244,3.774419,-6.486805,-7.147136,4.932973,8.605096,-2.242100,-5.389296,2.527513,6.114118,1.308452],[3.175604,-0.882622,-6.994879,-6.309901,1.827288,8.576312,-7.339275,-8.270434,7.425822,4.114326,0.050137,-5.739010,-7.898994]],[[9.284812,-1.243982,-1.673383,7.751838,0.402684,9.445135,-5.324600,-7.459064,3.953070,-3.597358,5.848935,-1.144983,-1.542176],[7.537852,6.971268,-9.480830,0.947478,-2.765578,-2.873173,-8.324685,2.621401,8.001228,-5.531159,5.400198,2.945607,4.996900],[4.567645,9.053509,-2.715353,-6.980632,-9.707705,-3.971121,2.264521,1.009935,-0.074441,5.790768,2.087310,-3.527823,-1.834660],[-6.502089,1.482946,5.601029,0.957190,-7.948119,9.297801,5.780968,8.924364,9.922247,-6.523265,8.133003,-8.025021,-6.669551],[7.244119,3.267967,-6.191876,6.657496,-1.348043,-3.770978,6.727761,2.198583,4.901658,5.321346,-1.511820,8.378624,9.268980],[-8.011655,4.389428,-6.494045,9.000875,2.049473,6.532963,1.486333,5.840616,3.601003,-7.705886,0.184997,7.743284,-6.951125],[5.084553,5.559926,-5.648616,-5.404629,-1.490888,4.623689,-8.181420,-8.623145,1.132801,8.188738,3.481267,-5.588135,4.053080],[-0.155058,-6.987521,2.003067,-3.563740,-0.936864,-5.275674,9.901401,9.811935,-6.052747,9.041442,3.255612,-4.640019,2.671414],[6.710182,6.905950,7.696681,-5.460814,-8.974849,8.770609,-7.012865,-9.888715,-3.313954,9.893131,-6.180205,5.142721,-1.194142],[-7.378951,-7.344202,5.332945,9.715964,-7.499503,-5.274785,-3.667468,-8.356510,4.154380,-2.748829,8.177257,9.873361,-9.042594],[-6.207775,9.063363,4.181293,8.001372,9.037084,7.278168,8.151831,2.294525,-2.301491,4.743405,6.522541,5.351117,-9.273231],[-5.819408,-2.691934,9.756328,0.389093,7.683670,-7.585213,-2.124137,7.177173,2.804903,0.136373,-2.921514,-1.476965,1.615257],[7.754283,8.083529,6.868015,4.519525,6.623170,7.689230,-4.384706,8.278227,7.454045,-8.251042,6.107497,-1.713284,3.182220]],[[5.255730,-7.122920,0.096335,3.967762,3.991004,1.678037,-5.015546,2.819309,5.720249,1.754196,-8.048202,-3.401850,1.748157],[-6.646411,-3.015130,8.183686,-5.631436,-3.837407,7.496426,-6.033486,0.059022,0.282663,-0.135217,5.581256,-3.186577,-7.773970],[4.529178,-3.159789,2.505104,-5.161585,-2.153572,2.680915,2.332752,-5.395214,7.115861,4.630659,-8.244799,4.101977,3.898994],[-2.178406,5.579778,1.623385,7.897281,8.063078,-6.043731,1.577734,4.767496,6.480694,-5.328815,6.529082,5.643991,-5.537351],[-4.039932,-9.047533,-8.362282,2.165636,-6.059713,8.651587,-3.673526,-3.632553,-3.855226,6.587356,-7.221603,6.091396,7.441782],[-5.645985,3.557641,-7.588528,-3.151545,-3.714207,-3.187547,-1.633039,-7.631949,-3.738399,1.384701,7.037866,-6.981622,7.806479],[-5.431881,-5.589358,-4.213679,-0.935557,1.752503,4.054163,9.697860,3.176427,2.384762,-1.293179,5.618531,9.743188,7.546324],[-5.360456,7.386998,-3.783108,-6.265742,5.869110,-5.686025,7.604264,5.038839,7.152565,-8.742554,-9.907144,8.653155,6.059504],[8.870508,6.404612,2.034934,6.928604,8.254508,-3.762257,-4.101842,-0.972426,4.607844,-3.237934,-5.852672,-0.575521,-9.390044],[6.599169,7.967102,-5.147497,4.189385,-6.281802,-6.590839,0.331221,4.606416,1.600043,-5.683040,-9.576377,2.213649,-7.505633],[0.657593,-0.806281,9.085540,4.664759,-5.291780,7.226796,5.698766,7.073981,6.182549,6.526409,-3.449319,-3.604002,5.200566],[5.087082,-6.402156,-0.687020,-7.091920,9.623536,-5.057172,-0.441062,1.660603,-4.679482,8.193259,-1.406580,3.917483,-1.376384],[-9.121116,-5.874910,4.890602,3.046296,6.051921,5.785179,-9.224095,9.829120,7.449424,-1.100059,4.893597,1.416004,-8.722586]],[[-5.465345,-3.974266,6.800824,3.547218,-9.234449,3.645668,-6.973053,0.644258,-9.556603,3.001418,7.365097,-6.072097,2.623343],[-4.720741,-3.271711,-2.637737,-5.904913,7.876809,9.925171,0.438294,-2.718411,1.544755,6.138250,-9.815022,4.382675,8.833467],[0.258252,-6.676403,-2.311882,7.449408,5.039727,6.440732,-2.932035,2.141835,1.204387,7.530523,-5.354807,5.561553,-0.466589],[0.053450,9.961753,-5.394064,-3.604965,7.518275,9.072123,-0.672376,-4.000339,2.166696,-1.529535,-5.967033,3.509992,8.702897],[6.335992,-4.415268,2.212708,2.818985,-4.107160,0.861240,-2.409348,0.037261,0.213226,-3.653775,8.878088,4.177244,-9.927580],[-4.643615,9.550135,5.125631,-1.066896,-7.695774,-6.533590,-3.447825,4.481873,9.864649,-9.656371,-4.063669,-7.660581,4.688856],[-6.408284,-0.191794,-9.383152,-8.578505,-4.418781,-7.365287,3.650365,-4.736091,-5.407260,3.429360,-1.987281,3.089148,0.178109],[0.642524,-7.706421,-1.227963,7.100719,-0.036469,2.461302,7.129321,-4.172412,-6.730476,6.196430,7.631908,5.148335,0.060434],[-0.361480,-7.749383,-9.770884,5.864477,-6.570159,9.650764,-9.547618,2.050832,7.884798,-0.100233,0.601711,4.580131,5.162419],[-8.983349,9.481439,6.442194,8.769201,-9.791821,4.608244,-6.194443,8.008142,7.026431,0.207012,1.817626,3.636422,6.387671],[-0.269448,0.931058,7.757553,-1.915543,-4.102315,-7.999612,7.520126,7.126358,7.394814,-7.072438,-0.249153,-8.763004,-1.014106],[-9.862212,8.304357,-0.075406,-9.210769,-2.984246,-4.538626,1.593746,-3.326827,-5.280497,-4.061673,-9.197280,6.409201,-7.824442],[-6.402449,-9.809524,-5.570900,-3.036355,-5.138752,2.730463,6.650429,-0.721516,-1.922961,-9.578859,-7.214698,-8.770870,-9.053659]],[[-0.272058,8.001361,0.114273,8.244102,-7.029218,-3.287187,-0.118821,-6.128165,-5.438417,7.554060,2.980309,-4.220528,-3.264545],[-9.070000,7.380642,0.202072,-1.109196,-9.466938,-3.675413,2.616768,0.974532,4.075567,-0.035052,1.290378,6.461734,-2.850225],[-8.664639,-3.695503,8.559862,7.779125,-4.660107,-6.204636,7.896894,-7.907694,-2.849808,-1.005040,-3.953371,9.269266,7.442702],[1.362348,1.649235,9.158191,-1.709022,-2.522010,-1.332044,-8.333172,-4.941225,-7.271269,2.467403,3.765740,-3.502021,7.164747],[-3.597028,-3.641678,5.831153,-4.722794,9.563412,-1.393416,-7.594787,8.559024,-8.201334,1.643572,-3.862606,-4.480732,-2.198326],[3.125135,1.738201,0.316636,-8.242990,-4.875682,7.444022,-6.690702,-9.898558,-8.589012,-2.883721,-9.110086,2.255801,6.939605],[5.020555,2.253270,-0.774638,-2.673124,5.091230,4.215786,6.690773,3.649535,-1.082509,5.629486,-4.555594,6.287208,6.094807],[3.789218,4.643620,-7.752352,-3.305880,2.368441,9.182051,7.272143,2.929931,-4.296538,-9.061468,-7.445834,1.235266,0.996892],[3.311840,-3.993301,-9.079582,-0.286103,0.500174,-2.307797,-9.145370,-6.589456,-8.820295,8.393436,-5.845054,-6.237999,9.056425],[1.681834,6.077737,9.940683,-4.618620,9.430771,2.794052,-8.648455,7.080631,8.187183,-3.090239,7.904152,9.321806,0.963506],[-6.366887,-8.665612,-5.285385,-7.206341,-1.502570,-0.098514,-9.262265,-2.292254,0.588784,-4.171722,3.267410,4.685936,8.773489],[-5.964715,5.329454,-5.504809,-4.710418,2.238501,-6.806232,-8.404166,9.723193,1.224638,-4.004527,-0.425920,9.036893,-6.039203],[-2.389781,-3.927309,-5.537419,-1.578441,-4.993877,2.135525,6.085872,3.253423,0.304652,-7.311247,4.136533,-1.650068,5.173508]],[[9.586834,5.210820,-0.528791,6.442901,3.191545,7.073070,5.055410,-4.421468,-6.808415,-0.658012,2.247360,6.772239,-9.665408],[-3.878427,8.489100,3.330915,-9.294680,-4.938154,-8.358658,9.474009,-1.953646,0.512912,3.734372,-0.701688,3.840035,2.201119],[-9.147042,9.143760,8.437379,5.395013,6.965325,-1.965733,9.054021,-2.670099,-8.339165,7.306662,2.147449,1.609960,-0.263823],[-5.479438,-3.613710,0.306800,4.003116,5.132194,-0.095271,8.265613,-1.102179,7.788415,-0.173784,1.316216,6.068633,2.343355],[-4.079046,2.105797,5.550518,-7.908578,-4.159946,-4.780321,-1.566188,-2.515619,7.360013,6.641180,1.000932,2.284772,-2.721953],[0.476542,-5.441797,-1.364103,9.467644,7.586118,-8.171973,-6.709719,9.631715,-0.066181,-7.297851,-0.128869,-2.870599,6.715368],[-2.740724,0.414369,-1.597649,9.855114,-6.560634,7.754641,5.183548,-7.571871,-2.089569,-5.304862,4.057436,-8.603376,-9.946948],[1.016055,-6.159243,-4.899846,-8.816206,6.548565,-4.377030,9.299377,2.749841,-7.673226,5.698070,-9.571404,8.698868,-3.356472],[5.283117,6.258964,5.604105,-5.640020,3.548659,0.609535,-1.604052,-9.639124,5.429393,5.351781,-3.935366,7.466064,-5.068723],[-3.384374,9.211341,4.677232,4.636618,-6.730483,7.816888,-9.837096,6.726139,-3.504008,-4.646778,1.896617,-7.010375,-9.774470],[-8.285122,9.249380,6.163838,3.913029,-5.508386,8.761599,2.142800,-9.990035,-1.566734,7.813297,-4.565803,-8.326295,7.000610],[-1.304379,-1.859030,-3.547153,4.217934,-3.954944,1.070354,0.847828,-6.617677,2.943193,-4.570528,-8.004792,-8.958995,-9.017106],[-9.255470,-9.877884,-6.377061,7.697670,0.471586,-3.741816,3.576686,-2.531481,-5.468418,-7.098528,-4.578295,-0.825971,-3.317323]],[[-3.355213,-2.546892,4.642721,9.773554,-7.017136,6.695515,-8.721555,-2.798496,7.816015,7.380791,-3.128037,8.987516,-4.364809],[7.592021,-6.582399,-0.116447,-3.216014,9.394896,0.208866,0.570433,6.643368,1.028034,-3.158784,-5.535775,-0.570162,2.830438],[3.945477,7.425188,-4.356381,-6.513362,-9.439198,0.393962,0.859363,1.607863,0.586596,4.868781,6.343123,0.892256,-8.500130],[1.385940,2.106399,3.905978,7.044004,6.023322,0.605610,-7.843665,-7.784823,1.327190,-5.703262,-5.036733,8.315806,-1.775745],[-3.180322,-8.000095,2.415953,3.271642,-8.582552,3.794162,-9.299348,-4.315659,-9.387120,5.714892,-2.526880,2.922403,7.724811],[7.606297,3.791919,6.415077,0.269677,-2.310960,2.460825,6.082026,-1.330506,4.427256,0.793524,2.199499,-7.454012,-0.270531],[6.101082,-1.846845,9.211344,6.052500,8.200246,6.284107,8.072855,-5.958301,0.102514,-3.131252,-2.883295,-7.514841,7.386533],[-7.632498,2.523630,2.643834,-3.475346,1.529187,6.973178,-7.053123,-7.267479,0.464414,5.003194,-0.275590,3.613051,-8.650293],[2.057040,-5.285305,-1.086034,-9.603895,3.108105,-5.032007,8.851622,-1.354952,4.490242,-3.760427,-6.947400,7.401356,8.876165],[-7.589271,-2.238997,-6.601424,-5.802849,8.399942,5.105019,-5.363470,1.507788,-1.303092,-0.744488,7.366539,3.214556,8.044314],[6.669955,4.522412,3.018984,7.051543,7.141864,1.425839,-3.876171,-5.699981,-4.356601,7.830659,-2.746457,9.538973,-8.718915],[-9.722160,-1.664928,1.656835,-9.708607,-6.521426,-5.958900,7.005149,6.440574,8.932530,8.941511,-9.009109,-0.946753,0.711817],[4.331132,-2.408432,0.378624,-1.547743,-6.847387,4.841297,-5.805510,-7.358579,-5.420344,-3.431911,-0.996503,1.201622,-7.475753]],[[-7.376325,3.837276,7.814332,-8.111012,-7.889245,-3.164656,0.885349,-3.600326,5.073280,-7.195473,-5.461507,7.070486,-1.186579],[-2.697013,-0.220159,2.015972,-9.314264,-0.685472,-6.282239,0.262714,5.519263,3.966730,-6.668957,7.904176,-4.255952,-1.288487],[-8.888246,-1.586094,0.146435,4.237624,5.418979,-5.110426,1.389924,7.955881,5.639957,2.580671,-8.669143,5.240005,-5.340509],[-4.813509,-8.980620,0.439427,-4.272680,-9.017616,5.320009,6.005459,-2.706714,-0.002274,9.717057,8.141326,-4.029536,3.363551],[9.505406,6.386709,3.685885,4.887025,-0.390014,2.625317,-0.875515,5.049702,8.537260,-5.911570,-3.148426,3.037903,-8.427831],[8.215717,6.204313,4.538637,6.048197,2.173831,-0.187308,6.442844,6.956192,7.762152,-1.913052,8.908760,-0.135853,9.284009],[-2.494963,-9.299351,-8.937582,2.751033,-5.737728,-8.942090,-6.093827,-5.208834,-2.499909,9.129741,-5.292716,6.172942,4.766847],[-6.033305,-0.017928,5.419992,1.107066,1.669479,6.853202,1.449988,7.593349,0.816839,3.181981,-2.367422,6.555766,-2.372500],[4.073744,-0.276899,-9.243084,-3.222210,9.814008,-6.517158,0.952643,-2.710760,-7.351915,-7.879924,8.364994,5.012355,6.033350],[9.045797,-6.351017,2.638040,1.436903,-6.054547,-9.618801,2.459908,-9.099793,-5.928559,8.870717,-8.614197,1.300545,-8.516018],[5.613315,4.344211,2.356787,3.209035,-3.285203,7.919026,5.103997,-0.739754,-6.653766,7.892900,8.934310,-1.072961,-2.962716],[-2.230099,5.636100,-2.327190,4.384066,-5.231782,-1.404142,-8.814766,-8.523279,6.183265,7.249153,4.693134,6.145206,7.351060],[6.059052,7.800266,-0.697078,5.718776,-7.934862,-3.893851,8.158403,8.038298,8.235193,2.341637,1.115060,9.863149,-5.032192]],[[3.957715,6.319573,-4.675103,-1.783713,-1.047064,2.338648,6.918953,3.635324,3.273643,-8.395003,6.685969,-6.993171,7.653067],[2.736352,0.672299,0.020956,5.766352,4.504784,8.714875,1.545920,-0.523914,3.843979,5.488922,-0.488732,-2.727151,9.834794],[-0.663819,-3.099433,8.283243,-6.229856,5.616742,0.515488,-0.869745,-7.546889,6.777935,2.901700,-5.199771,3.304210,4.749428],[7.563591,-1.487904,6.859853,-5.515534,-8.705099,6.985456,-8.304071,-8.523351,8.341552,-4.303202,0.506061,-7.843656,-6.745980],[7.867445,-0.444210,8.255197,-1.089945,-5.737238,-2.279664,7.244106,-0.117078,0.225072,7.597330,0.132057,-9.396183,-2.255995],[0.385367,-6.247206,-7.617763,7.022736,-9.397998,-6.869117,-4.145006,8.518162,9.790034,3.682098,4.249229,9.587107,-9.487333],[-1.459992,-0.338877,-6.368470,6.301884,5.010261,0.756222,-5.452355,8.322459,-1.322817,1.598541,-7.236102,3.999246,-2.661335],[-3.431023,5.437787,-3.564982,9.759694,8.041856,-8.328379,-5.332903,-4.583877,-1.830172,-0.677667,8.571670,2.512476,-1.548528],[8.691763,9.012057,-1.588319,3.776987,7.055192,5.620702,5.400457,-4.683543,0.292035,8.289816,-7.985811,-8.985628,-0.297470],[-3.959016,-0.432381,5.968467,-1.535069,-7.609560,2.108355,-1.102784,7.499691,9.021630,-4.201416,4.845675,5.972065,2.965027],[-1.785870,-9.927737,1.999654,8.730082,0.802081,-7.325362,3.145426,-4.906248,-2.785177,6.468688,1.852656,-0.799577,9.632560],[0.679778,4.411158,-1.151640,5.476983,-5.875885,3.274423,-3.771976,-0.750094,-4.115372,6.880291,-6.493257,-1.891999,-3.363385],[9.858876,3.594004,-4.114691,8.543153,-0.350797,6.287016,-6.825902,-2.466066,6.587440,-6.716945,9.550644,-0.263181,0.543121]],[[4.686226,-0.731895,5.181089,-9.999199,-5.912278,-9.384592,-9.312943,-6.921573,-8.588316,6.724473,-6.143530,6.911962,0.236428],[-9.811344,-0.068382,-4.694293,1.114941,9.233670,-5.818021,0.003540,-7.215894,-8.522765,-4.423888,-4.297593,2.675623,-0.683055],[5.718097,-6.502350,-9.335521,-7.477996,7.932100,-8.057423,6.682192,3.267279,-0.176077,2.225958,-3.405067,4.237456,-1.562550],[7.167128,-2.130188,0.573626,-4.259633,-2.370899,-1.738946,7.285701,9.485668,-5.647908,2.527428,6.016901,5.117400,-2.892240],[-0.680930,-0.444822,2.705897,4.526933,6.504391,4.590553,-4.243332,3.917843,-9.815608,-4.165069,-7.829658,3.774596,6.615067],[0.547329,0.207210,-9.445884,-3.418769,-3.115908,7.379662,9.682799,-6.060109,-5.076842,-3.059663,-8.464055,-9.965005,-4.950492],[3.476627,-3.301419,-8.261983,3.154414,3.631683,-5.884818,8.998073,6.156775,-4.759264,1.111211,-9.334630,4.336919,0.757552],[5.721597,7.226152,0.838043,3.397580,6.907864,6.209733,4.803036,-9.274899,-4.392601,-6.313142,-7.615831,-7.038191,-1.581894],[1.831875,8.509565,3.607122,-9.297619,7.122637,2.891125,1.623476,-6.215147,-9.761095,6.417884,1.017730,-7.477732,-7.324101],[-4.437958,-8.819631,6.139002,2.180249,7.056956,6.268838,5.001127,2.519653,-2.250477,6.172757,5.422052,-8.933085,-9.940236],[9.730900,-6.762698,-3.305530,-6.053149,1.845452,-5.424223,7.862279,8.865081,-7.137415,0.864340,8.412922,-2.920980,-9.755075],[-4.704428,6.309064,5.929605,7.101907,-3.232846,-8.738681,8.851146,-4.167053,-4.788956,7.239163,-4.527543,-0.159054,7.543097],[2.246971,-5.447697,1.242527,4.448659,-3.186525,5.036699,-2.640804,9.257331,7.617073,-8.557307,-0.878837,5.138200,-6.781651]],[[6.083380,6.383082,-4.769288,1.563428,-2.160882,-7.185009,2.875118,-9.759797,-2.351669,-4.710532,-2.621580,-1.239778,3.169154],[3.892864,-8.255360,-6.853210,5.729593,-4.919506,8.586870,-3.395081,1.793373,7.033762,8.781579,0.067664,-8.658948,8.092166],[3.243973,9.690752,9.271736,4.826712,-5.420048,4.640549,9.407676,9.915526,3.382317,5.599838,-3.062756,1.076049,-7.486365],[-2.658280,-5.289888,4.055197,9.945874,-4.568537,-3.561821,3.214920,-8.417511,-1.816702,-0.026530,-8.789129,1.474795,-6.814086],[-7.883534,-5.693515,4.077508,8.579427,-1.449340,6.243096,6.191038,-0.071459,-7.103236,-5.702493,0.139600,-2.564456,-0.580604],[8.248644,-9.256003,-6.488941,-3.616099,-2.859206,9.298690,1.425210,-0.284839,6.385114,6.844576,1.849919,8.235145,-5.455146],[-3.637432,3.407046,8.671567,7.637844,-6.437537,-5.847542,-3.277534,-5.104790,-7.063386,5.166935,6.165545,-7.718945,4.175136],[-5.766944,8.953282,9.512177,2.770155,-3.184079,2.526734,5.382606,3.792421,-1.520698,-5.085152,7.318378,9.118068,8.555475],[-1.932712,2.269389,-6.121922,-9.050598,-9.284570,8.024532,-7.890612,-2.320723,7.964488,-5.213737,3.292782,-1.676023,8.267211],[-0.443307,2.824851,2.719785,7.281389,4.016146,-1.643075,8.673906,5.977539,9.506392,-3.630712,9.281990,9.213511,2.510995],[7.394819,-7.607523,3.611283,4.420184,-8.125025,-3.767611,1.192550,0.410158,-1.804829,-9.975394,-4.369025,6.089150,2.986086],[-2.747075,-3.000044,2.451957,-4.994232,2.564687,-5.793290,-1.348773,6.631060,-7.276106,-3.339062,5.413074,-8.738120,-1.549042],[5.611514,5.721496,-5.536077,6.593231,2.085406,-3.674950,-9.091644,-5.979248,-5.434331,8.322510,8.538927,-5.901849,-8.032648]],[[-9.607070,6.659739,5.257036,7.574547,6.662593,-1.989729,-6.780622,3.448853,9.482355,-2.655421,-8.968534,-7.393139,3.441801],[5.195639,2.313154,2.567753,-6.825103,-5.659427,0.501306,9.867411,-2.733706,7.392414,0.620286,6.698607,-8.135529,-0.461322],[0.636634,-8.622083,7.785680,-3.516528,9.866843,-2.408954,4.288387,2.156648,-6.708711,3.657836,4.997601,-9.926004,-7.225648],[1.298144,5.687425,0.007424,0.280116,2.746197,-3.425602,3.138123,7.316210,5.924400,1.381071,1.198564,5.205495,-1.573279],[9.193951,-2.958042,-1.958601,-6.367421,8.745795,-2.783768,-9.537038,0.128276,-4.748344,-5.609366,5.442468,-5.788594,5.642774],[-1.318712,-9.725169,1.629301,1.753318,6.705394,4.370442,-0.931340,-7.687732,5.493582,-0.186454,2.677600,-0.321470,1.813890],[1.749264,-8.982938,7.222773,-6.547224,5.787789,-1.954111,3.020423,-2.069388,4.270593,9.565600,-3.550033,-6.430291,-0.209409],[2.847766,-7.153086,-5.097120,-8.596578,-9.926007,3.504651,4.427046,-6.276946,-2.251552,-9.141410,-6.295510,3.681429,5.696531],[5.734917,-5.680014,3.910436,-2.091213,-5.969602,7.620682,4.771046,1.184019,-1.894635,7.022756,-4.435067,-9.380407,-8.671171],[-2.291761,5.605673,7.833111,-2.552711,-4.652230,0.771723,7.339864,5.792148,-7.219481,-2.881521,6.340685,2.064067,7.215766],[-9.027159,-6.245752,-7.956118,-4.547658,-8.598866,-2.861116,-3.467109,-3.797317,1.283469,0.536153,-3.204729,2.118193,4.942064],[-0.051670,0.138565,-4.418858,9.829853,4.737795,-1.928172,4.838980,2.767033,8.387440,-1.061445,-6.888189,4.171819,-7.369231],[7.926379,-5.333164,9.243405,4.851253,-7.514558,-8.596788,-3.184937,1.222806,-7.128983,3.846498,8.513102,6.067096,-6.619436]],[[2.310411,3.575758,-8.836579,-6.077881,-7.677760,1.538004,-9.795097,9.796300,0.160118,-8.628055,-9.185758,-0.128232,9.952338],[-0.668273,8.093310,-3.483439,-9.462150,3.139681,-5.264811,7.091297,5.290822,0.045083,-3.038083,-1.181695,-1.489774,0.062926],[4.282085,4.832164,8.933620,4.355485,-6.443830,1.371109,-7.463955,6.619574,-2.076745,8.278547,6.719200,-5.046094,1.062862],[-0.172395,7.349592,4.199452,0.690681,6.555172,-4.416467,4.467495,-4.778957,-2.227755,5.892044,-4.352794,-7.042093,2.527832],[-5.760780,-1.708008,4.310660,4.598409,-3.856549,1.083115,0.645774,-0.117591,-4.037407,5.859275,-6.801137,2.449470,4.767259],[-0.194927,2.478093,-6.160525,2.297757,6.780760,5.438498,0.796403,8.960995,1.462951,-4.701609,2.841553,4.565734,9.244772],[-4.544649,-2.456397,-7.662587,1.194425,-7.446524,9.791871,-5.277260,-1.307281,-7.575816,2.272960,1.787456,-7.358029,-7.703077],[-5.032321,-2.613585,-3.946500,-4.272071,5.247743,1.686033,-8.695554,-0.148331,3.370615,-6.243663,-8.376365,9.084900,6.302260],[-1.210523,-5.758228,3.570792,-1.725922,5.385705,-5.957322,1.937703,-1.159895,-1.244379,0.565146,1.293871,-9.282726,-4.066813],[-1.572894,-4.847388,-8.255592,8.729401,-8.172390,9.165228,0.116144,8.102990,-1.747403,9.208251,6.872050,3.453715,-3.937531],[7.652476,5.444419,7.613177,0.573873,5.323657,-6.561370,1.920253,7.737366,2.425568,6.224404,-0.868877,-9.438148,-7.090977],[7.381435,-1.360856,-3.409784,-4.765608,3.494681,7.183070,-3.056694,2.378603,-5.753874,8.347347,4.517032,-7.068487,4.245622],[1.082954,-5.987766,8.736025,0.058968,2.406684,5.723748,8.658314,8.578914,0.132296,9.733333,-1.680132,9.247230,5.309526]]], dtype = "float64")#candidate|3445|(13, 13, 13)|const|float64
bop_3446 = relay.not_equal(var_3444.astype('bool'), const_3445.astype('bool')) # shape=(13, 13, 13)
func_3043_call = mod.get_global_var('func_3043')
func_3047_call = mutated_mod.get_global_var('func_3047')
var_3454 = relay.var("var_3454", dtype = "uint64", shape = (3,))#candidate|3454|(3,)|var|uint64
call_3453 = relay.TupleGetItem(func_3043_call(relay.reshape(var_3444.astype('uint64'), []), relay.reshape(var_3454.astype('uint64'), [3, 1, 1]), ), 0)
call_3455 = relay.TupleGetItem(func_3047_call(relay.reshape(var_3444.astype('uint64'), []), relay.reshape(var_3454.astype('uint64'), [3, 1, 1]), ), 0)
uop_3458 = relay.sqrt(const_3445.astype('float32')) # shape=(13, 13, 13)
func_2532_call = mod.get_global_var('func_2532')
func_2536_call = mutated_mod.get_global_var('func_2536')
var_3462 = relay.var("var_3462", dtype = "float64", shape = (630,))#candidate|3462|(630,)|var|float64
var_3463 = relay.var("var_3463", dtype = "int64", shape = (1620,))#candidate|3463|(1620,)|var|int64
call_3461 = relay.TupleGetItem(func_2532_call(relay.reshape(var_3462.astype('float64'), [630,]), relay.reshape(var_3463.astype('int64'), [9, 12, 15]), relay.reshape(var_3444.astype('int16'), []), ), 4)
call_3464 = relay.TupleGetItem(func_2536_call(relay.reshape(var_3462.astype('float64'), [630,]), relay.reshape(var_3463.astype('int64'), [9, 12, 15]), relay.reshape(var_3444.astype('int16'), []), ), 4)
func_3043_call = mod.get_global_var('func_3043')
func_3047_call = mutated_mod.get_global_var('func_3047')
call_3473 = relay.TupleGetItem(func_3043_call(relay.reshape(var_3444.astype('uint64'), []), relay.reshape(call_3453.astype('uint64'), [3, 1, 1]), ), 0)
call_3474 = relay.TupleGetItem(func_3047_call(relay.reshape(var_3444.astype('uint64'), []), relay.reshape(call_3453.astype('uint64'), [3, 1, 1]), ), 0)
uop_3475 = relay.atan(uop_3458.astype('float64')) # shape=(13, 13, 13)
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
const_3491 = relay.const([1.671560,-4.772839,8.727104,-1.349588,6.591771,-7.851932,-4.387828,-4.339263,7.011809,-4.430206,-7.946070,2.888213,6.884083,1.180098,-3.870209,0.743841,-5.785527,6.110391,-2.412669,6.772742,4.990199,-3.686507,-3.354865,-4.574959,-2.547713,9.999539,0.992381,0.540661,4.534079,0.432337,-6.166985,-8.464178,2.126698,3.782669,8.559476,9.388728,-1.643994,-7.979067,-3.761080,-6.173187,7.817229,3.826438,-5.903600,2.786276,8.641243,3.861666,-6.530846,-3.673154,7.906322,4.652267,-9.627975,-4.702449,-0.347006,-7.489137,0.286476,3.042919,-4.038671,7.612636,1.829493,-9.338306,-1.568590,-3.251205,5.882716,-6.989645,-8.245111,0.359961,-6.379745,4.053404,7.260315,0.931698,-9.194918,2.614068,6.606566,-6.772655,-7.437004,-0.734369,-9.756425,0.095772,2.460663,4.826424,4.002269,2.053105,-5.433193,-7.881793,-9.756928,-1.231923,-7.890655,4.972459,8.216616,-2.367229,-2.956588,-3.443169,6.092051,0.241195,5.181285,7.227716,6.350647,-7.742466,2.449928,4.296806,-9.949689,6.957833,-8.834738,-8.217437,-9.177358,3.888558,8.271058,4.490173,5.832752,-1.667345,7.847430,5.481789,-4.461078,-0.778257,-4.752742,0.516931,-2.856222,0.782997,5.727723,-8.874591,-6.685471,-1.625715,3.264716,-5.292852,-8.454282,7.433012,-7.151063,4.778508,-2.043364,9.502045,7.800426,4.563766,9.253497,-3.876097,-7.346167,-5.147735,-3.594037,0.638279,-2.452208,-8.654131,-4.884329,9.735929,-0.599078,6.583039,-8.281738,0.493180,5.996159,5.148876,5.375189,5.507906,-1.261493,-6.964211,-6.168127,-2.539233,-5.455776,-5.020337,-3.518712,4.504635,-3.748912,4.378854,8.661408,-2.391428,8.943596,7.738513,-2.071721,1.034647,-1.144890,9.447230,5.614703,-5.067515,9.088394,-0.652267,-8.071116,-6.714639,-5.836279,6.387830,9.279872,-3.784660,-9.146897,6.007933,-0.053547,9.359005,2.531692,2.955292,0.796904,-3.318040,-5.854433,-8.277602,-8.972951,1.453439,6.694017,5.731448,6.522835,9.500470,9.130901,-5.490207,0.426962,2.895702,-3.102600,3.906134,-1.363813,-2.079266,-7.080356,3.440651,-4.232119,3.194081,9.315883,-2.706601,-3.678209,-0.518840,-7.150385,7.744186,0.348768,-5.546123,-2.287639,6.273070,7.030612,8.318269,-5.126340,8.141223,-5.766555,-8.018330,5.652870,-3.305908,8.734537,2.600910,4.638079,9.463014,8.782515,-5.740710,-4.445624,-6.596531,-5.097221,4.538763,-8.230833,4.510342,-1.735327,2.205138,-2.195183,1.114534,-2.125043,6.484279,-0.641313,-2.806181,3.079132,6.425419,-6.195871,5.896623,2.003443,-5.227720,6.816723,-2.657740,4.852889,2.345975,9.877998,7.466802,-0.090331,3.800039,-5.611889,-5.197918,0.188932,4.131923,-8.903194,-3.354615,2.003940,7.347201,-4.392120,-9.801829,3.245352,7.084319,8.354297,7.155741,7.314723,-4.829933,-5.163910,5.872798,-8.403683,-8.936619,-8.262955,-9.995722,3.872960,-8.033424,-2.442873,5.865926,9.851718,-3.391147,-6.632465,-9.626704,3.652112,5.300676,2.570263,0.327270,2.793426,-0.687376,-4.823909,6.098289,7.492201,0.585508,2.488159,0.758336,3.141614,2.117016,5.524831,4.481100,-3.462441,1.008850,-9.022473,1.970142,-3.364056,4.625143,-3.917461,-5.994847,-7.608996,7.545579,-4.966799,-6.057979,2.241592,0.482422,3.176843,7.114904,6.416668,-9.114044,8.214808,9.763512,5.895650,-6.367099,-0.750277,4.468502,-9.308235,-9.106425,-3.151979,-0.324857,-2.535164,-5.176185,-7.899049,8.468100,-3.321336,6.828545,1.988474,1.006342,6.390014,-3.210691,-1.098695,8.311282,3.114540,-7.347304,-8.614813,5.471444,-9.847886,1.747436,9.395749,8.819246,-1.619434,9.935825,5.232048,-4.918871,-5.332707,-3.399906,2.517840,5.893944,1.862758,-3.435351,-8.806393,-1.378896,8.386483,6.791902,-9.322919,3.504669,-1.625892,-4.621456,2.333280,-0.854093,-8.715149,9.037491,-5.537534,-8.458274,-4.560542,-3.847280,-1.560901,8.569512,-1.224124,-3.815965,6.863711,2.724081,-2.405122,-4.939636,-4.333201,5.801168,3.302971,-1.124708,7.793051,-9.073352,8.271702,-3.088461,8.074810,-7.663889,-9.319078,2.143254,-9.317276,9.871286,-8.231765,-5.477727,5.805289,2.131880,-0.757415,-4.623629,-9.748961,7.129733,6.646146,0.607036,-1.553696,-6.771255,-9.511255,-2.236431,-3.163240,5.403549,2.698680,-1.325447,2.951197,-1.443458,8.394211,3.299518,6.447719,-2.023395,-8.915951,9.831876,6.097587,-8.168868,3.476210,-5.346031,-0.452775,0.583325,2.751498,-9.817229,1.987351,5.001387,-5.463468,7.194763,5.195359,-3.340216,9.106640,-4.522875,-1.648103,3.100343,-0.909802,8.726406,6.616403,-0.179131,-0.758782,-2.620211,6.175459,3.168679,-6.722114,0.642474,-2.679165,-9.971624,-6.178751,-0.970611,1.410019,-9.858769,1.593966,-4.200853,-3.997471,3.450365,-6.449352,1.027641,6.501440,3.123187,4.711914,-2.264948,-3.662512,4.269870,7.986950,0.831452,2.602749,-0.635618,-8.587813,-1.812417,-6.473100,2.228963], dtype = "float32")#candidate|3491|(480,)|const|float32
call_3490 = relay.TupleGetItem(func_1712_call(relay.reshape(const_3491.astype('float32'), [4, 10, 12]), relay.reshape(var_3444.astype('bool'), []), ), 2)
call_3492 = relay.TupleGetItem(func_1715_call(relay.reshape(const_3491.astype('float32'), [4, 10, 12]), relay.reshape(var_3444.astype('bool'), []), ), 2)
output = relay.Tuple([bop_3446,call_3453,var_3454,call_3461,var_3462,var_3463,call_3473,uop_3475,call_3490,const_3491,])
output2 = relay.Tuple([bop_3446,call_3455,var_3454,call_3464,var_3462,var_3463,call_3474,uop_3475,call_3492,const_3491,])
func_3495 = relay.Function([var_3444,var_3454,var_3462,var_3463,], output)
mod['func_3495'] = func_3495
mod = relay.transform.InferType()(mod)
var_3496 = relay.var("var_3496", dtype = "float64", shape = ())#candidate|3496|()|var|float64
var_3497 = relay.var("var_3497", dtype = "uint64", shape = (3,))#candidate|3497|(3,)|var|uint64
var_3498 = relay.var("var_3498", dtype = "float64", shape = (630,))#candidate|3498|(630,)|var|float64
var_3499 = relay.var("var_3499", dtype = "int64", shape = (1620,))#candidate|3499|(1620,)|var|int64
output = func_3495(var_3496,var_3497,var_3498,var_3499,)
func_3500 = relay.Function([var_3496,var_3497,var_3498,var_3499,], output)
mutated_mod['func_3500'] = func_3500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1533_call = mod.get_global_var('func_1533')
func_1535_call = mutated_mod.get_global_var('func_1535')
call_3531 = relay.TupleGetItem(func_1533_call(), 0)
call_3532 = relay.TupleGetItem(func_1535_call(), 0)
var_3534 = relay.var("var_3534", dtype = "float32", shape = (210, 9))#candidate|3534|(210, 9)|var|float32
bop_3535 = relay.right_shift(call_3531.astype('uint64'), var_3534.astype('uint64')) # shape=(210, 9)
bop_3538 = relay.right_shift(call_3532.astype('uint64'), var_3534.astype('uint64')) # shape=(210, 9)
output = bop_3535
output2 = bop_3538
func_3541 = relay.Function([var_3534,], output)
mod['func_3541'] = func_3541
mod = relay.transform.InferType()(mod)
mutated_mod['func_3541'] = func_3541
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3542 = relay.var("var_3542", dtype = "float32", shape = (210, 9))#candidate|3542|(210, 9)|var|float32
func_3541_call = mutated_mod.get_global_var('func_3541')
call_3543 = func_3541_call(var_3542)
output = call_3543
func_3544 = relay.Function([var_3542], output)
mutated_mod['func_3544'] = func_3544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mod.get_global_var('func_1454')
func_1455_call = mutated_mod.get_global_var('func_1455')
call_3546 = relay.TupleGetItem(func_1454_call(), 0)
call_3547 = relay.TupleGetItem(func_1455_call(), 0)
output = relay.Tuple([call_3546,])
output2 = relay.Tuple([call_3547,])
func_3549 = relay.Function([], output)
mod['func_3549'] = func_3549
mod = relay.transform.InferType()(mod)
output = func_3549()
func_3550 = relay.Function([], output)
mutated_mod['func_3550'] = func_3550
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3593 = relay.var("var_3593", dtype = "float32", shape = (12, 14, 12))#candidate|3593|(12, 14, 12)|var|float32
uop_3594 = relay.log10(var_3593.astype('float32')) # shape=(12, 14, 12)
uop_3598 = relay.exp(uop_3594.astype('float32')) # shape=(12, 14, 12)
uop_3605 = relay.acos(uop_3594.astype('float32')) # shape=(12, 14, 12)
bop_3612 = relay.greater_equal(uop_3598.astype('bool'), relay.reshape(uop_3594.astype('bool'), relay.shape_of(uop_3598))) # shape=(12, 14, 12)
output = relay.Tuple([uop_3605,bop_3612,])
output2 = relay.Tuple([uop_3605,bop_3612,])
func_3622 = relay.Function([var_3593,], output)
mod['func_3622'] = func_3622
mod = relay.transform.InferType()(mod)
var_3623 = relay.var("var_3623", dtype = "float32", shape = (12, 14, 12))#candidate|3623|(12, 14, 12)|var|float32
output = func_3622(var_3623)
func_3624 = relay.Function([var_3623], output)
mutated_mod['func_3624'] = func_3624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3061_call = mutated_mod.get_global_var('func_3061')
call_3775 = relay.TupleGetItem(func_3060_call(), 0)
call_3776 = relay.TupleGetItem(func_3061_call(), 0)
uop_3779 = relay.sigmoid(call_3775.astype('float32')) # shape=(9, 12, 15)
uop_3781 = relay.sigmoid(call_3776.astype('float32')) # shape=(9, 12, 15)
func_3495_call = mod.get_global_var('func_3495')
func_3500_call = mutated_mod.get_global_var('func_3500')
var_3785 = relay.var("var_3785", dtype = "float64", shape = ())#candidate|3785|()|var|float64
var_3786 = relay.var("var_3786", dtype = "uint64", shape = (3,))#candidate|3786|(3,)|var|uint64
const_3787 = relay.const([-3.024207,5.028642,-1.809097,8.434958,8.543148,0.564443,-1.028648,4.011239,-6.302254,-9.620778,-2.909112,-9.407086,-1.156896,-5.360493,-5.626991,7.043052,-7.855530,4.977372,-3.814834,2.036955,-7.088170,2.331297,9.470921,5.517251,4.691454,6.390299,-9.287075,-4.102384,-1.771916,-5.651098,0.745077,8.945060,-8.008158,-9.746528,0.427759,-0.525516,0.591400,1.378604,3.437112,-0.416999,-0.392575,-1.100666,2.280147,5.901801,8.982922,-5.002990,4.432869,3.179924,-3.469504,2.479471,7.678326,-9.254421,8.628253,7.590664,-2.625594,0.004265,-0.445367,9.841181,-9.635479,1.890148,-0.631320,-6.218304,2.448555,5.488893,-4.684320,0.989972,-5.042243,-3.300480,5.578514,-0.292390,5.692320,-4.328850,-6.057015,-7.188542,6.219319,-1.309025,6.069877,7.945591,-8.175412,9.644229,3.217296,3.885058,-4.517587,1.004989,5.487105,2.660931,0.822904,-0.313057,5.156258,0.240992,-3.856871,-3.991464,-7.779560,-1.681674,-8.259839,2.707384,8.277653,4.948664,-9.702614,2.216366,9.195085,6.233325,5.885356,-4.705422,-4.373781,2.187964,9.923131,-9.624838,4.825386,7.074083,-1.495084,-1.617746,3.270980,5.440427,-6.089503,2.442182,8.122245,8.297169,5.500413,6.266728,0.791044,-6.078218,-3.445602,-0.482238,-8.446865,4.106506,4.130950,-2.498803,-8.198843,-4.397988,-1.665326,-6.919291,-9.197290,-5.040783,1.866246,7.134001,-4.982513,3.277118,8.258751,6.327991,6.977957,-3.323300,-2.396082,6.063062,6.756450,5.281568,-6.812374,2.211927,5.561049,-8.910836,-0.711657,2.616746,3.508326,1.201695,8.070334,-1.201133,-0.599401,8.674367,3.579831,6.282090,-4.905726,8.083815,-7.962512,-7.315405,-2.359391,-9.096024,-6.159470,-7.574520,-8.477658,-8.914623,-2.930888,8.963116,-3.179951,2.310947,3.282575,-8.589770,0.463131,-0.447154,-8.980286,-0.980252,1.524229,0.089742,-1.608583,-4.104744,-8.797026,-4.608996,5.255678,7.046094,-3.856901,-6.078829,9.864613,-9.528564,-4.095384,-2.151964,3.826617,3.183715,5.153650,-3.813998,-2.884157,-3.093415,-5.897781,3.424733,-8.180004,7.146649,8.967349,8.900199,-2.125942,-0.499139,-2.887414,9.842132,6.842415,2.973808,-8.670147,-7.333804,-3.766622,3.804963,-2.434393,-6.601968,2.790547,2.721586,5.009572,4.692182,-4.148341,-4.062526,-4.439134,-0.434836,7.366034,-8.531003,-9.976482,-7.234372,0.673198,6.040030,7.798436,5.610267,1.418748,0.454690,3.340089,-8.398611,-5.001666,-6.262598,-2.197139,-1.151563,-5.324186,5.813984,-9.961914,3.032337,7.409681,6.211821,4.739454,8.265362,3.253792,4.345220,1.706065,1.259164,7.473638,-5.560646,-2.177967,4.209572,5.105620,7.100223,-0.677366,-1.500037,9.469622,-8.777819,-9.939871,9.899871,9.598097,-3.763057,-9.374753,-7.513611,0.783155,-6.599342,-3.562421,6.486816,-8.437624,1.517273,9.800888,5.308403,6.579728,7.022578,4.425916,6.815991,-5.510101,-5.816930,9.885866,-2.053138,8.853951,0.932371,-4.579858,-7.516682,9.079976,1.461702,5.870918,-8.872850,7.775612,-5.135477,-2.865608,4.205139,9.490663,-8.471551,-1.361824,9.019443,2.380979,8.769108,0.889140,-8.142597,5.275381,-2.754835,-5.464358,2.756322,-4.364527,2.534076,-4.131751,7.941162,-8.706201,-7.099559,-5.355135,-5.500052,-4.664610,9.166705,7.557303,1.691208,-1.675206,1.655350,-8.891072,-4.018474,-9.200023,1.585388,-7.965792,-9.575579,-1.746650,3.944765,5.260682,-0.945772,-2.389747,4.976858,-9.261076,-1.044357,-7.901258,1.584768,4.929751,-2.442297,3.024777,-7.791864,-9.207653,-6.687776,4.487566,-3.819360,-4.680385,1.298097,-2.931639,-1.442266,1.460441,6.087481,4.512283,-9.173193,-0.039691,-2.566364,-5.349195,7.285531,-2.830358,-3.113100,-7.305395,-8.539093,5.858862,6.555592,-1.704482,-3.474015,-9.447064,-8.342547,2.658311,-6.058143,8.636356,9.411932,8.135624,-7.498188,9.134970,-7.134726,6.841438,-6.151130,-4.825999,8.245876,0.555151,-4.510147,2.893574,3.750064,8.978714,7.188743,6.797024,-5.203500,4.100958,-2.548729,9.168870,-2.923395,3.273576,-4.173034,-3.283595,-4.195910,8.377074,-9.234954,2.277966,3.957550,6.988145,8.491597,-5.270956,-5.982359,5.555940,-1.054516,5.843286,8.991228,3.455633,-8.700909,4.490306,1.412466,1.159784,-4.669653,-3.334470,9.453539,-5.973552,-9.056771,-0.329736,-4.079285,3.358275,3.274650,-0.403839,2.460659,-9.671881,3.867663,-4.775680,-9.409851,-6.289463,4.944821,8.192328,7.723246,6.082964,-1.884289,-1.718020,9.482112,2.908996,-6.357679,-3.840300,6.262139,1.564094,-0.736797,2.055266,0.698130,1.617434,-9.421620,0.389390,-5.152520,4.566693,-4.677123,-0.504077,1.242755,-5.894790,2.201663,3.636548,2.513490,0.648564,4.878007,2.197996,3.040962,1.335942,0.127315,8.157105,6.274795,-7.938080,-4.259457,-6.847229,-8.061306,1.264851,1.197895,-8.987604,1.142168,-9.871688,-1.425326,5.099483,7.763828,-9.359621,0.363930,-3.142284,-8.101920,-0.693693,8.661790,5.785750,-1.544624,6.591317,6.015434,-0.373875,-4.060952,5.976354,-6.643871,-1.495992,9.113211,-6.256059,-7.704842,-4.365078,7.502216,2.802248,2.583034,-6.693806,1.407604,9.983609,3.522559,6.438932,-0.571091,9.169915,5.365757,-5.373603,-9.352925,1.095124,-3.162431,4.949456,-5.157269,-1.184565,5.457082,9.307063,4.126167,-0.434655,1.314159,-5.695802,-7.570084,-6.386130,7.321786,6.892477,-0.402833,-0.918534,-4.092674,-6.565603,-1.272908,-6.490139,-1.856117,-1.192730,-7.139160,-5.690902,-5.569992,5.941039,-4.811702,-1.402507,9.009055,0.644253,-4.152431,-9.044008,-0.152250,5.456031,0.399096,-1.469057,-5.853423,4.489317,1.794743,-3.551414,-2.751040,9.324901,2.484743,-8.423872,8.938095,-2.283569,2.973410,-8.069501,-3.681952,-3.883842,6.445544,2.412234,4.201882,-4.131959,-4.813868,-3.384644,-0.369772,-8.422063,1.078430,-3.862292,-6.706267,-3.306571,1.849118,6.560100,2.741172,-0.942539,2.020127,-1.293501,-3.064915,8.704132,5.750548,-4.738483,3.030460,5.147343,8.203558,6.192779,7.800648,-1.281959,-8.688006,-8.423854,7.348240,-1.265932,-5.167740,-3.076894,5.320578,7.798563,0.004635,7.275932,-2.270293,-3.236191,-2.738783,-0.874572,0.811579,5.777598,-8.404084,5.247159,-6.858957,-6.705842,-2.233315,0.691108,1.793532,-5.142802,-9.352395,6.411980,2.861722,7.036021,-5.676032,0.558977,-2.831131,2.534016,-8.841831,-2.399016,7.359516,6.229757,6.782892,2.677079,6.047630,-6.822255,8.911715], dtype = "float64")#candidate|3787|(630,)|const|float64
call_3784 = relay.TupleGetItem(func_3495_call(relay.reshape(var_3785.astype('float64'), []), relay.reshape(var_3786.astype('uint64'), [3,]), relay.reshape(const_3787.astype('float64'), [630,]), relay.reshape(call_3775.astype('int64'), [1620,]), ), 0)
call_3788 = relay.TupleGetItem(func_3500_call(relay.reshape(var_3785.astype('float64'), []), relay.reshape(var_3786.astype('uint64'), [3,]), relay.reshape(const_3787.astype('float64'), [630,]), relay.reshape(call_3775.astype('int64'), [1620,]), ), 0)
const_3789 = relay.const([[[-8.592895,-1.778640,6.349885,8.608544,-5.503316,9.787458,6.991492,-6.184106,4.703932,6.917595,-9.508824,-3.761056,7.302999,9.680194,5.821358],[-9.646764,-8.474446,7.066178,-9.802612,5.947228,0.256574,-6.970590,-9.690145,-4.871080,-4.178233,-1.418791,-1.971529,1.407206,-4.490845,-6.943191],[-4.765662,3.658527,6.124016,-6.312825,-9.991893,-6.676497,-2.089500,-3.368694,3.269501,-3.832680,-5.425021,-1.425681,-1.250139,-0.418507,-4.398170],[-8.754541,9.036984,-9.024892,-4.508986,-8.750098,-1.070258,-0.875571,5.755189,8.372759,0.935062,2.544687,-1.084890,-0.441891,5.890594,3.506453],[2.313896,-3.894877,-0.999800,3.601838,3.364664,7.183763,0.563768,-4.606288,-8.480745,0.179875,-9.377115,2.091383,0.630798,4.486934,-3.680918],[-1.284720,-6.796209,-7.664294,5.413464,5.497093,0.046757,-3.399471,-9.297235,5.585498,-4.385747,1.538994,9.457638,7.552673,-9.751622,-2.578433],[-9.090699,0.308048,4.900724,6.292989,6.786320,-4.096572,4.160269,2.407926,1.942029,-4.884142,-2.271024,-4.286926,-1.021562,-4.357874,-0.997458],[2.173962,6.996949,3.218400,-6.325611,-3.142037,8.598981,-3.879870,6.895869,6.159154,-6.925940,1.460981,6.505735,0.605727,6.623680,-2.060704],[-4.103746,-7.964647,-4.375170,-4.389685,-0.009297,1.853606,3.915746,-4.615345,8.781026,-2.161267,5.008854,-9.628354,3.455228,-7.691195,1.552951],[6.734094,-5.555521,-4.183982,3.472947,1.649190,1.551096,-7.541357,-5.930487,8.204495,-5.132013,-2.371574,5.145723,-1.825884,-2.766647,-1.145250],[3.069549,1.270231,6.896176,1.611456,-9.060138,4.419212,9.396592,6.618830,-3.042868,0.715726,-5.443231,0.527856,9.066795,-5.759127,-2.828372],[9.434640,-6.204030,-6.811669,-7.593521,0.091194,-4.322008,-3.460611,-7.133343,-5.612831,7.910995,6.407656,5.054353,5.065437,-2.149052,-0.364499]],[[-5.500016,-5.637289,-3.586968,2.328165,-0.413705,0.256486,2.195930,-0.167326,0.155059,-7.978058,2.060266,-1.049054,-8.323406,8.292666,-0.379423],[-3.617673,2.166461,4.405541,2.488505,8.730232,9.505326,-7.194329,-6.301374,-5.739918,0.909183,-4.619916,-0.966133,4.006729,6.105390,4.883240],[-9.766096,-8.000179,1.686008,4.740887,-7.074426,-9.610270,-8.281906,-5.440394,-2.438767,-5.101853,-8.846663,-4.591839,-6.562932,9.989148,-4.076914],[5.272113,-2.356958,-7.541134,5.904413,-7.090551,-8.902070,-5.618836,-8.794723,-6.522823,5.450285,-2.162023,3.415672,3.551966,4.045559,5.650578],[6.708129,-3.859377,9.067214,5.404892,7.732695,-5.716095,5.201552,-9.828579,-8.826183,-0.966302,8.276338,2.519588,5.297525,-5.292350,5.029235],[-4.580496,-7.189637,4.923850,4.836109,6.370278,-8.109514,4.263053,-3.612497,7.709878,-6.860823,-4.748924,6.390350,-3.861294,-6.420407,0.809903],[7.064598,6.441602,-9.048195,2.471370,5.442544,-6.634320,-0.407227,9.658467,4.617605,7.721040,-4.897962,-0.209546,8.394668,-0.852911,2.310724],[-0.627109,4.862313,0.972367,-6.682332,-7.068867,8.349164,6.412274,-8.964940,-9.805516,-4.961677,4.691919,4.848933,-9.988105,-1.279834,1.828118],[-9.731557,-9.810776,0.200943,4.396426,-3.056776,1.885515,2.265565,-1.149429,-3.793444,0.039463,-9.946728,1.390107,-7.319089,6.414782,2.542076],[9.640737,-1.995432,7.976466,0.046765,1.259008,-1.231293,9.651561,1.573696,0.109004,-7.271667,-2.441851,0.395624,-4.381334,1.799449,8.487959],[-3.926123,-5.276696,-2.385607,-2.419110,7.209504,-2.446590,9.408831,5.370504,3.295864,-1.606960,6.970919,-3.100512,-6.522725,1.116463,-2.377463],[-5.267490,3.684158,5.819832,6.442378,5.507632,4.015257,-8.599396,0.057275,-7.782181,2.927335,-2.151016,3.336087,1.488826,9.789594,-4.095706]],[[6.240609,6.956628,7.325238,5.309255,-1.562939,6.808489,-8.169598,-1.205964,6.229586,-3.382213,6.244493,-7.136523,0.035105,4.363235,-3.770560],[3.254726,-7.423739,-4.186636,7.247551,-9.214502,-4.416593,-2.592938,-6.739360,-6.895278,3.491647,-8.650322,6.541186,2.921436,-1.526529,1.297646],[-5.293034,4.336152,1.068212,1.579848,2.619196,5.191762,9.393596,-1.585954,-3.207875,-2.221505,8.126192,3.539224,9.194973,7.068919,8.641235],[-8.902555,3.447861,-3.465048,7.088534,-1.371144,-5.911243,-5.192459,0.071872,1.346044,1.443533,2.173674,-0.487253,6.204295,4.261599,3.958296],[0.177850,8.232852,6.391804,-4.597277,4.631941,5.968502,-0.405852,3.332580,-1.532725,0.017316,-7.319925,-8.078286,4.341675,-8.961671,3.829428],[9.420956,3.885738,8.237918,5.686657,0.153006,-2.818788,-8.585058,-5.562854,-7.889676,-8.173026,-1.015778,-5.456734,4.429799,-2.844594,7.561547],[6.766407,4.356959,8.200518,-5.372818,-5.384054,7.516648,-7.175518,9.557571,8.657700,-4.559799,6.941137,3.551697,0.306079,-0.209841,-8.545413],[9.763042,-1.052073,9.141057,-9.749990,-6.423125,1.438522,5.017752,2.580392,7.460184,1.854774,-4.862404,-2.124307,-8.444520,-1.867430,-9.758719],[-9.328533,1.336704,-8.053204,-3.652558,-9.607674,0.109613,-3.581856,0.250388,8.113913,8.461785,-4.818817,9.819444,0.554341,2.181878,-0.542148],[-4.669041,0.821613,-7.983774,-2.515494,-0.714290,9.653898,0.432774,0.254615,-5.006327,2.133593,2.702560,0.388143,-0.571951,-1.815777,1.683023],[4.255671,-7.480052,9.692133,-6.957557,4.802147,-6.284081,-9.869631,8.746646,-4.843391,-7.935818,9.794359,-2.158583,7.412350,8.382117,-1.993917],[-8.956909,-0.745598,-6.952292,4.348728,-7.327201,-3.764977,-6.932584,-9.433677,-5.542348,6.671319,-2.436731,-9.585665,0.319652,0.791034,4.311248]],[[9.720989,-4.108661,-7.369704,2.122333,0.582285,3.014051,-5.046419,1.405892,3.954659,-4.652655,-2.082745,1.690644,2.453446,-6.826432,8.408380],[-3.117693,-6.654969,-1.963919,5.174570,-2.945054,8.118145,-4.270997,0.586026,-9.268627,4.127452,6.590126,3.556063,-0.887248,-5.917542,-2.504584],[5.015063,-1.650399,0.745971,-0.682102,3.215937,0.606879,-2.577659,-3.984603,1.354386,-6.869456,3.734531,6.685708,-8.251302,1.113940,-7.184740],[-0.856701,-4.108889,0.555966,-3.081340,2.567661,2.629012,-4.624097,-0.452441,5.086170,-2.693757,3.527386,-6.758516,-9.043826,-0.930988,9.527941],[5.648032,-4.684142,-3.431627,6.563978,-1.986586,-0.057834,-0.631706,7.072539,-8.718767,-4.089962,9.811758,-7.310983,-6.727439,-7.169293,7.937130],[-5.269342,-4.228012,-4.419610,-2.438699,4.776743,-2.607759,-1.815716,-7.468536,-6.845882,1.566487,1.953185,-8.781486,-8.371620,7.238988,3.392665],[-5.306704,2.190580,4.002670,6.011463,-5.819887,-6.935740,2.333375,9.571656,-0.326840,-0.552520,-4.153536,-0.367211,4.028448,-5.546054,-8.201038],[9.127996,8.461612,2.225925,2.125177,-2.796052,9.489237,-8.263915,-9.308986,-0.701106,6.856380,-3.900108,1.106235,-6.621736,5.751171,9.789087],[7.831732,-4.513523,6.798906,3.973631,-4.026847,-5.837051,-9.687329,-4.530976,-6.554363,7.545633,7.239914,-5.757229,8.477691,-1.753466,4.546221],[-1.695264,-9.030932,2.278634,-5.089252,-7.733128,-2.465046,-1.435393,-8.350775,0.527581,2.684103,-8.249149,-3.168453,0.975901,-0.525462,-6.966559],[8.563649,-2.547649,1.597037,-5.478421,-8.851478,0.468909,8.657205,2.467713,-5.155879,9.728546,5.540961,8.894542,-3.002108,9.907371,-0.422317],[-1.133420,-8.959553,3.898615,-3.519143,8.298323,5.510426,3.630660,-6.221787,-5.333530,-8.228092,9.139217,7.874345,7.199061,8.241913,-3.201288]],[[4.456026,-7.142520,4.859484,0.106030,1.111650,-4.211686,8.275958,2.770674,-7.528299,4.384020,7.055328,0.266494,8.602736,-7.833490,6.494849],[-0.663134,5.232439,3.719825,-1.983355,-5.417743,1.825677,-3.279729,1.222734,9.350438,3.144406,-0.286160,8.937035,-1.449472,-4.359378,6.571609],[5.727065,-5.119575,-7.430835,-6.563581,8.301617,-6.862259,1.424371,8.297100,9.293630,8.087280,1.816455,2.308007,4.922690,1.997082,8.118024],[9.426703,-3.049048,1.241709,7.163148,-7.459775,5.247681,-4.189083,2.766172,0.837488,-7.896343,-5.554005,-0.806797,-8.783293,8.172045,8.983941],[-7.149531,5.140512,5.554159,-4.896973,-0.862293,2.267312,8.131567,0.370047,6.531176,4.205875,7.965746,-2.657324,-6.148269,9.210465,-9.500078],[-3.081948,7.550669,-9.550255,-0.033359,-7.597640,1.828947,-3.904186,2.695130,7.380884,-7.434005,-2.109876,-8.387834,2.184743,4.722361,-4.090290],[-7.292864,-3.936685,0.469563,-5.992382,4.064098,-1.214049,-8.663535,-5.121469,-3.499617,-1.694029,-7.817662,-0.196168,2.691622,0.547275,-5.823442],[2.961809,-4.030967,7.347494,-7.126794,-0.182299,-8.385498,-8.765351,6.104081,-9.260912,-7.065507,6.820306,1.614544,-7.219892,0.157784,4.379570],[9.079275,-6.295686,-8.239911,1.790176,3.597637,7.867581,4.939235,-7.389070,-4.951468,-3.763978,-8.178389,9.009736,-4.997668,-2.397769,-7.727844],[9.207759,-7.183912,1.321467,5.233910,7.358408,-1.119689,-1.611648,-7.210568,8.368700,7.905345,-4.803166,9.611960,4.084307,6.018205,2.234058],[2.647317,1.623713,5.508703,8.719423,-3.121497,1.782204,4.689313,-5.527414,4.939603,-7.957057,7.075336,-0.950420,-9.309568,-4.551975,5.832093],[5.409222,2.489949,7.452055,-8.454572,7.877545,5.797613,7.023200,8.890121,1.914079,5.970413,5.552172,-4.444985,9.705401,-5.118949,-0.057416]],[[-7.787736,-4.112381,-2.909646,-5.219227,-2.259023,1.018612,-6.123978,-1.355353,-2.018465,-4.993992,7.406236,2.990203,5.421029,8.341916,-2.727867],[-5.398608,8.894190,-4.909049,-2.878397,-7.202508,0.979249,-2.598699,5.421976,8.595192,-9.867956,5.761287,0.009335,8.192250,-3.389540,-8.864248],[-3.219164,8.786232,-9.312093,-1.322177,-4.176267,2.504971,-2.315741,8.929597,1.510538,-6.092025,9.598599,9.048839,-9.176042,5.867577,8.677881],[1.494341,-4.959317,-3.399608,8.025929,8.185177,4.915631,9.028076,2.570470,5.293346,6.790260,-5.175654,-3.470939,8.136755,8.705169,7.839347],[4.948409,-3.314684,3.847969,-4.786300,9.846485,-0.372770,-3.294651,7.484178,-1.271391,-6.420199,-5.770073,-5.850814,1.128550,2.187198,4.954561],[6.979652,2.561210,-8.257909,-9.469147,5.941507,7.514714,4.047528,1.773616,1.700999,1.656574,3.616484,-7.795277,-9.704512,-0.460331,-6.170144],[-2.724114,-7.859980,-0.590840,-3.502986,5.518445,-7.830610,2.180810,-3.762021,-8.507681,9.203143,-1.756114,5.470070,-1.786989,-6.520502,1.203617],[-0.470373,-1.322947,-4.992941,-5.483554,-8.365722,-6.448661,-4.391648,-6.580470,7.018891,-2.992565,-7.342821,0.542290,6.858891,-7.136659,-2.259666],[5.692868,4.117494,7.215673,-7.072323,1.477613,9.929360,8.563529,8.245539,5.899029,1.806369,4.164778,-0.904770,5.362419,0.718107,4.448374],[-1.097536,-4.127727,-7.346047,2.189618,6.662322,4.262341,-6.961645,-4.369397,-3.973612,-2.081640,6.324238,-2.676573,9.053711,-7.130870,0.041137],[-6.848875,-7.858953,4.601497,9.834475,2.292946,0.796863,3.936374,5.143466,-3.355548,9.514817,4.717430,-8.572143,-4.109809,-9.800172,-6.618685],[-6.101727,8.554156,-2.532594,-1.289421,2.321005,-5.317443,-4.162793,-1.767194,-6.736677,-9.448808,-6.461233,-2.311838,5.847061,-8.618590,5.002868]],[[8.793156,8.965667,-2.565604,6.865245,0.675233,-6.853156,-5.682179,-8.042428,5.481058,3.777710,-9.259029,4.811477,-7.695623,-4.091637,-9.226756],[-0.479862,4.843136,-7.522408,5.529366,-7.758680,-6.395162,-0.824536,-6.785695,-1.683226,4.554366,1.821658,1.579144,7.923311,6.516891,-7.824355],[9.071013,5.217283,-2.881285,5.869703,1.336458,6.841311,-8.387137,-4.809674,-9.864479,-2.153048,-1.604121,8.957362,8.434710,-6.943233,-3.923649],[-0.105318,3.128331,0.830266,-2.270024,3.310984,-3.719439,9.572169,-6.432349,0.162572,-7.770881,7.882843,5.302971,-1.705666,8.885607,5.301928],[0.274400,7.136709,0.095608,4.993847,4.268096,-7.219943,9.892088,7.169693,7.026531,-9.541519,-4.175918,0.737939,-3.447567,-8.211969,-2.977113],[-4.301167,-4.331018,-3.795296,-6.773313,9.478029,-1.697920,7.965838,2.014846,1.379716,-2.950077,6.396699,6.205877,-9.823583,-0.957139,2.812126],[7.243833,8.983297,-8.980541,1.924110,5.828275,-9.978444,-7.720032,9.494726,-1.979994,6.032786,-1.189780,-2.363468,6.638596,9.971810,0.462674],[-8.253066,-9.937601,-2.900569,1.312099,5.316382,-0.147577,-5.781890,-9.093702,1.135166,-7.145128,8.179149,5.353743,8.771302,-2.630701,-4.983036],[5.029780,-7.596089,-8.934769,-4.141286,4.860541,-4.142299,-0.664732,-2.077800,-0.129795,7.974500,-3.631808,5.795956,-3.697408,-4.164107,-3.545210],[0.952666,1.709740,7.331070,-9.435112,1.061397,-7.329977,-5.610962,-9.764807,3.268422,-2.672281,-0.613879,4.895059,-9.583205,-6.610480,-0.139167],[0.310571,-8.080828,-0.734798,1.248496,-2.908017,-2.241319,-9.681606,8.892765,6.105706,-9.830282,3.317332,1.844431,-6.643774,2.550906,-9.406643],[4.644396,5.688461,1.456377,-3.127571,-9.397755,0.733483,5.697127,2.190332,0.102018,6.900411,-0.133286,-2.510254,2.012690,3.691871,4.419699]],[[-8.814206,-3.536863,-4.489434,9.524116,-0.587940,4.164393,-1.336363,3.398332,6.978614,2.019565,-6.096433,-7.559070,3.524135,-3.562930,-4.496844],[-3.915917,-1.627693,-0.422442,-0.207625,1.111100,4.724500,4.713765,5.602306,-6.590783,6.385407,3.826060,6.459001,-2.769024,6.447185,-0.999381],[-3.599158,5.230144,4.235756,1.199215,8.681961,-8.364948,-6.816492,3.215458,-7.894834,-4.443508,3.324243,-0.100090,8.342075,7.620826,3.898844],[-2.673480,-4.316244,-0.245892,3.814931,-9.165032,8.805348,-9.989718,-8.788890,0.999677,1.062180,-7.663163,-4.278352,1.032304,9.256494,-0.306314],[-3.510536,-6.425497,-1.174743,-5.854008,-2.628154,3.244176,7.818289,1.627363,4.744268,9.998005,1.458906,9.093796,-6.400481,9.254242,0.536171],[-0.259786,3.014459,-7.596249,2.266035,9.189856,1.206217,7.322591,-9.677861,-7.456803,-2.726688,-1.222219,9.946156,9.338155,5.004542,7.500584],[-1.380881,-3.135353,-3.679935,-0.460384,-6.966036,-8.323282,-3.714405,-9.189725,-0.550125,-5.864990,-8.408617,-2.432110,-5.598202,6.428783,0.639636],[-2.508795,-5.103569,8.679615,7.045260,0.401476,8.688111,-5.893897,6.341527,7.284756,9.512652,-4.639882,-5.123904,-3.474572,-0.085796,-3.817176],[-2.768364,-4.388816,-3.597386,-2.758733,6.138438,9.990756,8.640697,-4.049909,-5.238629,-8.557701,0.937184,-2.055440,-6.534540,-8.106065,-3.638049],[-2.233195,2.875049,-4.594343,-6.630505,9.841020,-4.963782,-5.490838,-3.093564,-4.479745,-5.700179,0.663910,-9.577291,-2.247360,-1.217379,3.547907],[3.489395,8.059777,-8.546264,-9.358929,-6.915667,-2.465042,-4.199605,-6.126512,1.030458,-0.516285,-6.194869,1.927795,4.245153,8.179113,-2.222315],[-5.618170,-7.126033,-9.631710,1.372823,1.111021,7.419773,-0.112410,-6.039620,-9.999048,-3.982996,-2.387446,-1.642062,7.232047,4.394350,5.701811]],[[4.412137,4.052048,-4.253599,5.002543,5.880980,7.471854,-3.553145,-9.733313,7.172242,0.457971,1.859404,-1.167692,7.676702,3.238465,-7.856795],[5.824483,0.683718,7.049632,-9.456374,1.986834,7.189524,-2.414772,2.032046,-8.179468,-3.406081,-2.325752,2.860717,6.111553,-8.367802,0.428432],[-7.966711,-5.747282,-6.534447,2.846679,-0.234046,-4.916045,0.385725,-6.159935,9.196301,3.201963,-2.058768,-2.147778,-4.010710,-5.651078,-6.920621],[1.239886,-8.587819,-8.704608,0.672987,-2.020048,2.665472,1.772748,3.410118,9.983955,2.315417,-1.687652,-4.805439,5.616083,6.186504,0.664819],[-1.671106,-3.521431,-2.775030,9.003811,-9.001732,-0.053548,-1.331774,-6.693141,3.249307,-5.892814,5.803975,-6.136946,0.730351,-7.753247,8.365693],[1.399660,8.405487,6.245600,-8.968735,8.511451,-8.350496,-0.605912,-9.534954,-3.393576,-2.759928,-0.579783,-1.051895,0.595878,-3.228520,-9.694705],[9.213755,5.373417,5.565198,3.919549,2.003240,-4.277018,-8.671773,-1.346436,2.244218,-5.736753,-9.535170,9.176964,5.011996,-7.934406,3.803264],[2.993955,-6.244752,6.141176,0.662985,-5.599589,4.124613,-5.052009,2.745985,-7.409534,-4.633079,0.158744,5.870518,4.601378,7.323058,6.436799],[-9.595623,-5.871077,1.164448,-9.266081,-3.514274,-5.722708,2.122992,0.407309,1.041520,4.432850,-6.329517,-6.825833,-1.945267,-7.658800,-6.241119],[-5.354067,-7.700849,2.400960,-8.810891,6.481145,-3.021378,-2.605509,-7.641518,3.771337,-5.074212,3.547852,4.512242,-0.040211,7.281132,7.374161],[-5.647997,-8.273346,-5.999328,6.224521,5.018557,0.337037,-2.278596,9.101504,8.522339,-8.443216,-4.162299,-0.695817,-8.219985,4.704876,5.294260],[0.959214,-4.988715,6.415557,0.892880,7.181485,4.437962,2.769287,-2.537506,-9.810497,2.471271,3.146201,2.233906,8.598608,9.040145,2.047550]]], dtype = "float32")#candidate|3789|(9, 12, 15)|const|float32
bop_3790 = relay.less(uop_3779.astype('bool'), relay.reshape(const_3789.astype('bool'), relay.shape_of(uop_3779))) # shape=(9, 12, 15)
bop_3793 = relay.less(uop_3781.astype('bool'), relay.reshape(const_3789.astype('bool'), relay.shape_of(uop_3781))) # shape=(9, 12, 15)
uop_3797 = relay.rsqrt(bop_3790.astype('float32')) # shape=(9, 12, 15)
uop_3799 = relay.rsqrt(bop_3793.astype('float32')) # shape=(9, 12, 15)
output = relay.Tuple([call_3784,var_3785,var_3786,const_3787,uop_3797,])
output2 = relay.Tuple([call_3788,var_3785,var_3786,const_3787,uop_3799,])
func_3802 = relay.Function([var_3785,var_3786,], output)
mod['func_3802'] = func_3802
mod = relay.transform.InferType()(mod)
var_3803 = relay.var("var_3803", dtype = "float64", shape = ())#candidate|3803|()|var|float64
var_3804 = relay.var("var_3804", dtype = "uint64", shape = (3,))#candidate|3804|(3,)|var|uint64
output = func_3802(var_3803,var_3804,)
func_3805 = relay.Function([var_3803,var_3804,], output)
mutated_mod['func_3805'] = func_3805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2352_call = mod.get_global_var('func_2352')
func_2354_call = mutated_mod.get_global_var('func_2354')
call_3810 = relay.TupleGetItem(func_2352_call(), 0)
call_3811 = relay.TupleGetItem(func_2354_call(), 0)
uop_3821 = relay.sin(call_3810.astype('float64')) # shape=(240,)
uop_3823 = relay.sin(call_3811.astype('float64')) # shape=(240,)
func_514_call = mod.get_global_var('func_514')
func_516_call = mutated_mod.get_global_var('func_516')
call_3825 = func_514_call()
call_3826 = func_514_call()
output = relay.Tuple([uop_3821,call_3825,])
output2 = relay.Tuple([uop_3823,call_3826,])
func_3831 = relay.Function([], output)
mod['func_3831'] = func_3831
mod = relay.transform.InferType()(mod)
mutated_mod['func_3831'] = func_3831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3831_call = mutated_mod.get_global_var('func_3831')
call_3832 = func_3831_call()
output = call_3832
func_3833 = relay.Function([], output)
mutated_mod['func_3833'] = func_3833
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3854 = relay.var("var_3854", dtype = "float32", shape = (7, 5, 6))#candidate|3854|(7, 5, 6)|var|float32
var_3855 = relay.var("var_3855", dtype = "float32", shape = (7, 5, 6))#candidate|3855|(7, 5, 6)|var|float32
bop_3856 = relay.less(var_3854.astype('bool'), relay.reshape(var_3855.astype('bool'), relay.shape_of(var_3854))) # shape=(7, 5, 6)
uop_3871 = relay.asinh(var_3854.astype('float32')) # shape=(7, 5, 6)
func_2205_call = mod.get_global_var('func_2205')
func_2207_call = mutated_mod.get_global_var('func_2207')
const_3892 = relay.const([-5.636413,-8.443123,-7.985772,-3.783772,7.373801,2.774848,7.025265,-6.807711,-4.791938,-9.523207,6.968307,2.171320,-5.840639,-8.184746,2.841384,-8.618428,3.019868,2.303423,-8.695906,-7.219409,-9.676662,3.713913,-0.807102,1.474304,8.670691,6.807666,-4.685338,-2.761270,2.939606,2.411022,-2.782071,-6.153495,-1.536416,7.766443,5.123560,-4.824708,7.554996,1.632406,2.010287,1.082320,-2.849377,7.348132,6.320373,9.938448,-7.902577,8.853141,-7.733126,6.597258,-2.010642,-5.840048,-4.422806,8.212279,-6.460666,1.272178,9.664110,8.595066,-8.470288,-8.627934,-2.448401,-8.568212,-8.316183,0.096968,-2.188078,-2.056022,-7.763437,-5.581404,0.600200,-5.762072,1.284894,-0.613673,-6.544623,-1.392512,-0.412586,5.348677,2.013927,-7.202955,6.525674,-6.387873,-6.726085,-8.476519,5.803283,1.579712,-5.142996,7.694743,8.931774,-8.094489,1.787064,-2.251181,-3.853068,-6.470040,-3.391657,3.636340,6.075400,4.115369,-1.915417,-0.792093,-0.869904,3.355525,5.768847,-3.816770,-5.517418,3.267324,-3.971439,7.322583,3.798648,-4.300148,-4.383854,7.759632,9.852830,3.466624,3.344798,-6.606928,3.337247,-5.024919,-3.676662,-2.344535,-0.769237,-8.803045,0.692028,6.316298,3.989183,-5.364040,1.753588,8.229602,-3.345582,8.765184,-8.226926,-8.125541,1.985444,5.368665,1.194937,-7.656446,1.456339,-5.606237,-3.556305,8.901943,5.689143,-8.525467,5.605765,-9.518728,-6.896195,6.223169,6.461726,1.277268,7.872788,-0.690778,-7.993042,-9.501318,9.963926,-2.275637,-9.091277,8.091240,-3.507820,-9.115728,-2.271567,0.766040,-8.647802,0.962280,-7.897454,-5.130938,6.244252,9.100282,3.946660,8.211521,-3.241576,7.832367,0.887222,5.136212,-1.219034,-6.403657,-2.028358,0.464035,-0.455367,-0.517718,9.114389,-1.153175,7.585391,-5.242656,3.343752,9.501100,-9.992440,-7.352286,9.673353,5.451445,-3.622083,-0.137017,9.666477,1.586058,0.637695,2.313537,1.798473,3.919798,4.924664,2.320860,-0.887943,-3.666430,0.788678,-1.649789,-8.747625,-6.790290,7.111433,0.654010,8.367571,3.074907,-8.651387,8.454415,-3.180595,-9.033937,0.345376,1.820290,-4.933512,-4.640899,-4.501888,9.599310,-7.844243,2.641540], dtype = "float32")#candidate|3892|(216,)|const|float32
call_3891 = relay.TupleGetItem(func_2205_call(relay.reshape(const_3892.astype('float32'), [2, 9, 12])), 0)
call_3893 = relay.TupleGetItem(func_2207_call(relay.reshape(const_3892.astype('float32'), [2, 9, 12])), 0)
output = relay.Tuple([bop_3856,uop_3871,call_3891,const_3892,])
output2 = relay.Tuple([bop_3856,uop_3871,call_3893,const_3892,])
func_3894 = relay.Function([var_3854,var_3855,], output)
mod['func_3894'] = func_3894
mod = relay.transform.InferType()(mod)
var_3895 = relay.var("var_3895", dtype = "float32", shape = (7, 5, 6))#candidate|3895|(7, 5, 6)|var|float32
var_3896 = relay.var("var_3896", dtype = "float32", shape = (7, 5, 6))#candidate|3896|(7, 5, 6)|var|float32
output = func_3894(var_3895,var_3896,)
func_3897 = relay.Function([var_3895,var_3896,], output)
mutated_mod['func_3897'] = func_3897
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3984 = relay.var("var_3984", dtype = "int16", shape = (10, 11, 10))#candidate|3984|(10, 11, 10)|var|int16
const_3985 = relay.const([[[-3,6,4,-9,2,-7,2,2,-4,4],[2,4,1,4,-5,3,3,-1,9,-7],[5,-6,10,6,6,1,-9,10,7,9],[-1,1,2,-3,3,3,-2,8,7,-5],[3,-3,-3,6,8,-3,8,5,7,4],[-5,-1,-8,-10,-4,-7,3,9,6,-7],[1,-3,5,10,5,-3,2,9,4,4],[6,-4,3,6,-9,4,-2,-10,7,8],[-5,-4,6,7,-5,-9,4,2,7,7],[-3,-9,-9,2,8,-10,3,-9,7,3],[9,-3,-5,8,-2,-1,7,-10,8,4]],[[3,8,8,-9,5,7,3,-7,-2,4],[2,-1,-5,7,2,-9,5,-5,7,10],[-3,8,-4,6,-9,-3,6,-10,-4,2],[8,3,9,8,9,9,-4,9,9,-7],[-6,7,-4,-2,-4,4,-6,-7,4,-2],[-5,8,8,-9,-5,-3,-5,-4,9,-7],[10,7,8,-4,1,-9,7,-6,-5,1],[-1,2,7,5,3,3,5,1,5,-8],[-3,5,-4,-4,7,-10,2,-4,-9,-6],[-5,6,-8,3,-4,2,-10,9,9,3],[-1,-6,-5,1,-1,4,8,4,-9,-1]],[[-10,2,3,3,5,10,1,8,-6,9],[7,-3,-5,1,6,9,-7,5,2,-2],[6,-2,7,2,-10,1,4,10,-3,-3],[3,6,-1,-7,-10,10,10,4,4,1],[7,-9,9,10,10,-2,3,2,8,-9],[-8,-8,-2,8,-8,-2,-4,-4,10,-5],[-7,-5,5,-6,-7,-5,7,7,-6,7],[-5,-7,-10,2,-6,2,3,6,5,1],[1,8,9,-7,-10,9,3,-4,8,3],[-4,1,-4,-5,1,10,-4,-7,-2,8],[-9,7,4,5,9,9,-4,-3,5,5]],[[6,7,-4,4,9,5,-10,9,6,-7],[-3,8,-5,4,-9,-8,-6,6,7,5],[-4,5,-5,-10,-10,5,3,9,-6,-10],[5,1,-2,1,-9,-7,-9,8,9,-4],[-7,2,-4,-10,7,-5,-9,-4,-3,2],[3,6,-6,-7,-6,-5,10,5,-2,4],[6,-2,6,-5,2,5,-1,-9,-7,1],[7,-6,-5,3,-5,-7,-8,5,-4,7],[2,-5,-10,7,3,1,-3,-7,8,-6],[-8,-4,-9,-10,-1,-2,8,-5,2,-8],[-1,-4,-7,-3,-2,-10,9,9,-4,4]],[[8,8,3,-4,5,-1,10,1,8,-2],[2,-3,5,2,10,5,-1,-4,6,1],[-10,8,-10,7,2,8,-3,-6,4,-10],[-3,4,9,10,6,9,-4,5,-5,-1],[6,-2,4,-9,-7,5,-7,-5,9,-2],[-7,-10,-7,6,-9,-8,6,-6,-9,9],[8,-7,4,-9,-7,9,-1,8,6,-9],[-9,-2,6,-7,4,10,-3,5,9,2],[7,4,10,6,-4,-3,-4,1,-2,7],[-6,6,-6,-7,-6,-4,2,-1,-8,10],[-3,-8,-7,-9,9,5,-6,7,3,-6]],[[-4,-10,-8,9,-7,1,-2,-9,10,-6],[-5,-6,-3,3,-6,-2,1,9,10,-5],[-6,7,5,-5,-5,6,3,2,-5,-1],[-6,-3,3,-6,9,2,-8,-3,6,-10],[2,-2,7,10,-1,-3,4,-3,8,-1],[-1,-10,3,-3,-3,1,-10,10,-1,7],[3,-8,-6,5,-10,-10,-9,-1,-6,-3],[-1,4,-1,9,7,1,-8,9,2,7],[-10,5,7,-4,-2,2,3,-5,2,-4],[9,-9,8,2,-1,4,-8,-1,-4,-10],[3,-2,-9,1,-10,-10,-4,-8,8,2]],[[1,-1,4,-3,-8,-7,-4,7,5,-7],[-5,-3,-6,9,1,3,7,10,-7,-10],[-6,4,-7,5,9,4,-9,-2,10,-10],[3,2,9,-1,-2,9,-7,10,-4,-5],[-7,8,8,2,9,6,5,-4,-9,-1],[4,-1,-3,-7,3,3,-3,-7,-8,6],[1,1,-1,2,-10,2,-3,6,-1,-4],[-7,8,7,-8,6,-4,7,5,-2,7],[-2,-5,2,-10,6,-9,2,-2,5,-3],[5,8,-5,-9,1,-7,5,-7,-3,9],[-2,2,-8,-2,8,1,-5,7,-1,-4]],[[-2,-5,-1,5,-9,3,5,-5,4,3],[7,5,-3,9,-9,-8,4,-2,-6,-10],[1,6,1,-8,-3,4,5,9,4,-3],[10,7,-3,-10,-6,-3,4,-5,-3,7],[-2,-3,2,6,-1,-10,10,-7,-6,3],[-7,-1,6,-3,6,6,-1,-8,2,-1],[-3,-3,6,-6,-7,6,-5,-5,2,-1],[-10,-10,-7,-5,2,-9,-5,-8,4,-7],[2,7,10,-10,1,-1,-10,3,-9,6],[4,-8,10,2,-1,5,2,-3,-5,3],[4,-9,6,2,8,-7,-5,-1,-1,9]],[[4,5,7,6,-1,-9,4,-1,-8,6],[-3,10,7,1,6,10,-3,4,1,1],[9,-8,8,3,-2,-3,9,-3,5,-6],[3,1,-9,7,4,-3,-9,-8,-10,-4],[8,-7,3,7,5,8,-7,5,3,7],[1,-2,3,-1,1,-5,-5,7,-4,5],[-8,-7,-4,-1,8,6,-10,-2,-8,-3],[-8,-7,-3,-8,-1,-6,8,1,10,8],[-2,7,-3,-4,-2,2,-7,3,-5,7],[-6,4,6,3,-9,-4,-5,4,10,1],[-5,1,1,-2,-7,-4,-9,6,-6,-3]],[[-1,-8,8,6,-10,-1,1,-6,8,-9],[-6,9,-3,-3,5,6,7,-4,-5,-4],[-9,-9,6,3,5,10,-6,7,3,8],[9,2,7,-10,6,9,-8,-6,-6,-10],[-10,2,-9,-7,2,8,9,-7,8,1],[3,1,-8,8,7,-5,-8,5,8,10],[7,-1,-2,5,8,-5,-5,2,5,-7],[8,1,1,-5,-10,-8,5,-7,8,6],[-9,-4,-9,-8,-8,9,9,4,-10,8],[4,-8,5,-5,-7,-6,-3,-1,-9,-7],[7,3,-7,-7,-7,-6,-3,1,2,-1]]], dtype = "int16")#candidate|3985|(10, 11, 10)|const|int16
bop_3986 = relay.bitwise_and(var_3984.astype('int16'), relay.reshape(const_3985.astype('int16'), relay.shape_of(var_3984))) # shape=(10, 11, 10)
uop_3991 = relay.log(const_3985.astype('float32')) # shape=(10, 11, 10)
func_493_call = mod.get_global_var('func_493')
func_497_call = mutated_mod.get_global_var('func_497')
const_3995 = relay.const([[-0.529321,-4.292816,-2.667538,9.172658,3.977567,-2.571632,5.559545,-8.859484,3.133062,0.463736,-6.563876,-8.388589,-1.897706,4.707536,-6.937620,1.944946,-7.195857,-0.764135,6.071233,9.778522,-2.841920,-4.855295,8.409694,0.327096,4.835868,-3.623397,4.736796,8.073851,-5.601642,-6.425579,-6.759067,-0.900250,7.385943,7.305144,-4.674865,8.572603,-7.808294,-0.861931,3.380170,-1.049522,7.262852,-5.830222,2.260107,-5.028575,6.146935,5.699041,-5.408481,-5.876888,-8.153832,8.199583,3.041952,-9.478459,-3.376033,2.656977,-1.326376,-3.339249,-3.358020,-7.829838,-6.089161,2.947752,4.336621,3.780834,-2.724132,-5.848310,7.510074,-7.193063,-9.058634,-5.055884,6.878264,-0.959282,-1.103493,2.394313,-0.905692,-2.771472,-0.096424,-5.263539,-7.221139,-2.044723],[8.498828,-2.955619,-5.210423,1.061369,1.069724,2.347022,2.589855,-9.830229,-1.599915,-7.601308,-5.559682,5.380554,6.876189,-3.960520,-8.597935,-0.769643,7.403178,-0.787149,1.559558,3.626947,-2.137439,-1.258005,-3.668149,3.384117,-8.341639,8.256971,-7.110269,-0.992966,-7.792076,-5.148622,7.895912,3.019425,9.099800,-6.695343,6.665054,7.162753,-5.750420,-6.310423,-6.542981,2.077126,9.726459,6.826650,1.913014,1.840398,1.870546,-5.888477,6.249065,3.116846,-3.328802,7.248879,1.698048,8.449361,-9.811561,0.390261,4.085701,-4.414197,3.813844,-4.346527,9.899800,4.571941,6.455720,0.202527,1.465345,6.415112,-7.525932,6.196580,0.858833,6.961266,-8.502392,9.918829,2.940701,6.905807,4.760308,2.429312,4.887945,8.718525,5.539227,6.624364],[-1.746586,-4.373904,-0.309024,-5.754967,-7.300222,9.352403,-8.460411,-3.920102,-5.936323,2.978787,5.781095,-3.453836,2.210736,-7.313097,-0.203397,3.223858,-6.805121,8.131757,6.765790,1.558265,6.171972,0.377713,9.764605,4.484244,2.079642,3.720249,-6.564248,7.468179,-2.142253,-2.800764,-1.281953,2.410645,7.449039,6.446289,-6.232245,-0.043391,4.307840,-4.606774,4.874431,3.204115,-3.634055,8.243696,-2.648524,-3.767240,-6.057911,-9.735731,-1.566784,-0.480644,-0.114023,-7.822072,-6.326703,8.962646,-6.445195,-5.688177,4.541321,-4.077012,-8.452970,-3.428686,1.253023,8.396704,5.960328,-8.392634,9.122810,9.911528,-8.211142,5.182736,-4.264319,-1.853422,-7.146987,-5.181404,-8.984456,5.566541,6.797302,-2.481966,-2.989608,-0.277166,3.863493,7.517570],[0.033378,-6.812343,-5.184260,-3.015052,-6.902152,-7.089835,6.007087,0.567672,4.724701,2.549035,-9.706231,4.288448,7.209520,6.458518,-3.885827,-7.873409,8.143610,4.921660,-7.795707,4.565170,7.531589,6.296274,-0.658258,-2.239256,7.092262,-4.984763,8.348143,-3.857234,-1.499716,4.081421,-6.180420,-8.519973,9.624160,9.338487,-5.690340,-3.831801,-2.381347,-0.889842,-4.851156,1.223765,-5.909179,-1.814952,5.386694,6.273969,-6.745970,8.365522,-7.061585,-2.449915,7.762506,1.016697,-4.142174,4.022279,7.215141,-5.510530,4.272942,0.459223,3.723080,5.971880,-0.927197,-3.578340,-7.453074,5.146084,-6.166018,-0.333006,2.463340,5.879842,9.496591,4.178772,-7.576477,2.361672,0.201573,-3.634005,-1.275205,5.929612,-5.994788,3.427366,8.452712,0.263943],[-7.581181,-9.307928,4.879256,-4.594946,-2.777279,7.449585,0.323398,-2.567467,2.601027,7.983434,4.915651,-9.838900,9.625834,-8.827887,-8.370288,-8.310633,4.347690,-6.013534,-5.508416,3.044556,-5.793182,2.849896,6.649980,-6.544468,-7.991814,-0.811923,2.104050,2.525862,-6.648890,5.852959,7.504229,-0.041368,-0.317785,0.278407,1.334443,-1.929953,3.036612,9.626036,8.491862,6.226629,4.373537,8.641357,-1.134693,0.829964,-0.468766,3.378801,-2.886062,-5.770564,3.516952,2.297471,0.768749,-3.175395,-9.146765,1.336494,-6.674053,4.109112,7.141754,-9.187111,-2.166848,-9.717634,-3.983504,-1.401490,3.816546,-7.118022,0.858043,3.286036,9.096334,6.208477,2.320288,2.722157,-2.860208,-5.781516,-4.709307,1.209876,-9.045703,5.243752,-2.013569,-5.134714],[8.942127,-3.431655,-4.939337,9.865340,5.162932,2.841723,5.788009,-0.175968,-3.100582,6.461486,8.672549,9.006751,7.119607,4.350726,-8.111411,2.465811,-2.553840,-1.571831,-8.612601,-5.288989,3.208805,-2.772437,-2.938600,-3.899017,0.278983,2.953938,-0.555764,8.649586,-9.963355,5.376218,-2.800102,-7.068227,-8.455218,5.778306,-9.702301,7.855484,-7.850491,-6.854986,-8.029874,6.107215,2.099399,0.203066,0.347795,6.024228,0.749159,-3.942354,2.700395,-3.419298,-6.209530,-6.001376,6.230760,-2.852765,-9.417535,-4.341405,5.273061,-6.273774,7.943078,-0.267149,-1.780562,-2.649016,9.147484,3.363974,6.692240,-8.948566,-6.880120,-5.979603,-6.456999,9.458536,9.665243,-7.079291,4.343868,9.762791,-2.180193,3.591026,2.693164,-6.845701,-4.204099,-5.646173],[1.028172,6.823438,7.102740,5.618896,-5.718493,-2.331236,-2.298249,-8.775478,-6.683502,-5.699308,-6.428899,5.236826,7.765623,-5.795291,-6.100265,4.889190,7.193178,3.559629,-1.560844,8.223401,6.947434,7.031943,-6.560764,6.668317,1.468453,7.066838,7.759254,-7.278104,-5.494081,-0.693497,9.757750,-7.682306,7.101239,5.086436,-6.370749,-3.625762,8.220511,5.777201,-1.564282,-6.764370,2.443692,1.752633,-3.756947,7.391393,-8.078250,2.678241,-8.717100,-5.270184,2.870958,7.259206,-8.935999,7.600797,2.722937,0.869529,2.660170,-1.269573,6.368701,8.669072,0.424782,-6.919000,6.290603,0.143405,6.902219,2.176190,0.789682,-4.412712,-5.544293,1.138426,2.434771,5.489946,-3.367652,7.160579,6.369852,-4.147784,9.466916,-2.933586,-8.003352,-3.314493],[-2.325142,0.673113,7.963212,2.505057,9.956664,0.370989,-6.814165,-7.609675,-8.455298,-9.808948,-9.427292,-7.479594,-5.386150,-5.307775,-2.530011,-0.270197,-8.823797,1.593887,-9.284544,-7.539810,4.358604,-0.943780,-1.847584,8.778996,-7.032840,8.207894,-5.001377,-7.045187,-7.288185,3.921507,-1.539298,1.388058,9.879666,-5.413030,-6.180388,-1.234097,-0.660167,4.526440,0.562369,-1.773324,-6.881243,-7.907233,5.245349,8.384607,-2.830020,3.596017,8.873658,7.640582,9.661097,-3.009622,-0.223159,6.754269,4.686117,-3.226386,1.771546,-2.367881,-5.431079,-6.431947,5.557097,3.920184,2.100545,-8.576663,-1.051934,0.103603,0.913470,3.293162,-3.715597,0.538951,4.080418,-8.019723,-1.156052,-1.163441,-5.545207,-6.318773,2.000185,6.189837,-2.509354,7.929615],[7.883324,-0.299828,-5.383652,3.626780,6.079762,-2.334754,-6.844729,9.386123,0.073922,1.687011,5.173199,0.120761,5.780364,6.612258,8.715216,-5.297643,4.517723,5.869360,-8.850894,9.480640,4.899587,-8.831654,-4.130377,-9.654880,-2.006892,4.271242,-1.298827,-8.934458,2.923937,0.777233,-4.006408,-3.468279,4.598771,7.483568,-9.257231,2.522016,-1.665762,1.167489,4.906371,-9.281926,2.978681,6.268921,-4.325776,1.024819,6.575266,-2.966736,7.211913,-0.503083,4.229251,-2.357142,-7.575840,8.428003,-6.569910,2.879792,7.651911,9.792828,-9.478315,-9.237772,-2.887525,-9.140151,-3.312552,8.575979,4.805713,-9.057820,3.624825,-7.007220,-4.417103,-9.938552,-7.019469,5.279715,8.533838,-9.851161,1.462615,-4.493919,7.105705,-0.633022,-9.135138,2.310432],[9.143996,-3.540764,-0.474975,-2.647735,-5.477310,7.639857,-9.684796,-1.601219,1.014323,9.835036,0.095219,-0.815082,3.958487,0.590723,-9.253107,8.944718,-5.309250,-6.793776,2.927355,-3.141662,3.754866,-7.580370,-6.145392,4.754074,-8.674169,-2.392200,1.398449,-4.428659,4.288303,-2.435400,-2.969275,8.179543,2.863468,4.393747,-2.950998,-7.624598,-1.320372,-1.728148,-8.050709,-8.676359,-9.953903,-3.116558,-4.316444,-8.800117,-8.494118,0.198962,0.932623,-3.360381,4.365753,1.862560,8.755584,9.679435,-5.789414,-9.207228,-3.910199,5.423349,0.299082,-8.199309,-8.440919,-1.790769,5.877173,6.654128,-2.719052,7.065709,-8.037034,-5.953395,-8.844045,1.978922,9.668693,1.665089,-0.596836,-8.192456,9.134965,8.090163,-1.069575,-7.039715,-0.641143,-8.628793],[3.403905,-3.462273,-1.933571,8.578397,-1.936687,3.107731,-9.270884,6.287382,-3.070840,8.453009,-4.232153,8.845073,-3.867261,-4.640764,-0.980048,7.075240,-9.211982,0.095182,-6.902400,-5.179686,5.293442,-9.825139,-0.532233,-7.603950,-9.113029,-7.322054,2.636623,5.761921,-9.280848,-4.891963,-4.703990,-8.410865,4.996792,2.429381,6.537040,-9.784446,1.059637,-1.950696,7.564201,-4.829900,-6.866307,-2.443909,1.923942,3.486033,-8.322167,-8.564637,-9.534386,9.814383,-3.821401,3.143433,-8.071059,-0.685661,1.323592,-6.931184,3.397154,-4.409600,5.698181,5.564460,-2.311657,-7.814000,-2.509471,5.989810,-8.004402,-7.217449,7.909275,-4.164396,-4.662303,8.498010,2.390600,-1.285871,1.756547,8.036679,5.586129,4.444548,1.990759,-5.727138,-5.663392,-8.476762]], dtype = "float32")#candidate|3995|(11, 78)|const|float32
const_3996 = relay.const([-7.090601,-5.847076,0.998235,9.580912,-8.502256,-1.367987,-8.933608,7.316134,9.705553,1.324694,-9.289381,1.034738,-2.415933,-3.333298,0.531460,2.779697,3.982563,1.842673,-7.212465,-0.453538,1.737754,-5.591522,-5.046882,4.498800,-4.761964,-8.467095,-5.386397,-6.609953,-5.823471,-9.156717,-6.562278,9.268145,6.628824,-7.356405,-7.739279,6.947029,4.322864,6.905127,5.157108,7.434698,9.135926,-6.317963,1.231886,2.682820,0.451742,8.689839,9.955656,6.741193,7.261262,-2.148461,-3.840226,-2.144935,1.466406,-8.749645,-2.039804,8.957153,7.883901,-0.773963,-2.817084,-8.838741,4.974559,7.644177,-6.717105,-0.921593,-3.163333,2.723176,-6.356082,-8.609566,3.993289,-1.050427,-0.449163,-7.703667,2.190611,-4.923657,-8.319813,-5.384415,-1.376314,-9.963612,-8.754145,-9.105921,-0.327640,-6.794676,8.355400,-6.859295,7.411976,0.059727,-5.282853,8.403980,-9.959559,7.050505,-5.262654,-6.150219,7.834222,4.808664,1.596696,-4.694547,-1.366129,-2.718483,6.721747,-8.682160,7.129869,-6.557915,9.937494,-3.129605,6.523695,-1.845418,7.874903,-3.202660,-1.557823,-2.934736,-9.135272,9.691200,4.497888,-2.608541,-2.712013,0.038832,-9.290308,-1.794204,8.972307,7.050805,-0.077463,-3.339573,4.251489,4.027468,9.492087,0.638767,-9.647374,-6.818759,9.041085,1.395903,6.633946,7.524658,-4.411672,-5.172607,-9.581519,8.186383,3.843972,-4.375152,-6.433049,-6.382418,-2.389384,6.348757,-1.574623,-1.704915,4.679166,-7.615406,5.668431,-8.176484,9.969819,4.735137,6.261020,-1.880272,2.652871,9.329487,-4.773560,6.311963,6.439909,-1.233556,-1.566430,4.851285,-9.104571,-2.917868,-9.684800,6.365268,1.705865,5.880913,2.262658,-3.652562,1.240628,9.968802,9.507720,-6.657854,6.671557,7.634837,7.733802,9.669670,-9.683013,9.005447,8.299625,-8.326107,-4.859454,1.617983,5.122146,-5.425501,9.095249,0.635398,-0.888181,4.591401,-2.872451,6.153378,-9.556329,0.853938,-5.762183,6.624230,9.336142,7.191195,4.937885,-4.900001,-3.547907,1.591160,-3.731724,-9.072348,-2.503639,-9.876951,-3.861591,7.024885,9.383721,1.524614,6.148481,3.888946,-7.406646,-0.215791,1.588141,3.430711,6.426690,3.798140,3.786387,-0.730789,3.669393,-3.216705,-5.374866,-2.477678,-0.701284,-2.241808,-7.239507,-4.776272,-7.586856,1.763621,0.197572,8.157022,5.944008,-1.851497,-3.053931,7.461592,-8.638854,-6.157621,5.182942,-5.467364,-4.197963,3.293801], dtype = "float64")#candidate|3996|(240,)|const|float64
call_3994 = relay.TupleGetItem(func_493_call(relay.reshape(const_3995.astype('float32'), [11, 6, 13]), relay.reshape(const_3995.astype('float32'), [11, 6, 13]), relay.reshape(const_3996.astype('float64'), [240, 1]), ), 2)
call_3997 = relay.TupleGetItem(func_497_call(relay.reshape(const_3995.astype('float32'), [11, 6, 13]), relay.reshape(const_3995.astype('float32'), [11, 6, 13]), relay.reshape(const_3996.astype('float64'), [240, 1]), ), 2)
func_1347_call = mod.get_global_var('func_1347')
func_1352_call = mutated_mod.get_global_var('func_1352')
var_4006 = relay.var("var_4006", dtype = "uint32", shape = (780,))#candidate|4006|(780,)|var|uint32
const_4007 = relay.const([[3.998535,-7.081273,5.250501,-2.581731,3.351238,-2.736608,5.477351,7.798252,7.746256,-2.160110,-9.971424,-6.862866,-0.287287,1.703111,-7.768490,6.540439,-4.425996,-4.927962,1.353351,0.287973,-4.284088,-5.959281,-3.411212,-6.871043,7.140793,-9.579390,-1.012574,-1.050748,-7.518608,-0.966554,8.642997,-0.632336,3.081331,9.538486,0.135549,8.604649,4.639578,7.531701,8.091666,8.919207,2.608905,-2.727700,-9.954573,-7.281882,-4.786943,8.913688,-2.533118,5.283885,-7.094576,-8.745611,2.794020,-0.797348,7.892270,5.054630,1.557256,5.659526,-1.074965,-5.067728,4.452289,8.414473,8.588725,3.138129,-9.779897,1.087538,0.436196,-1.692896,0.416591,8.124808,6.027543,-2.200432,8.364818,0.017673,2.176903,-2.364793,-1.625775,5.078451,6.515243,0.466371,8.276704,-3.750564,-6.430207,-7.741427,7.146482,-5.151910,-8.040967,7.756172,0.810922,6.145164,6.247070,3.627733,8.926455,2.346673,2.331317,-5.523349,-1.013517,3.446854,3.630778,-0.128631,-0.470970,5.370999,6.840087,-3.304959,5.769542,-8.014978,-1.808169,-4.324771,-9.603010,-4.452855,-3.947484,-1.552624,4.936262,1.385333,1.529972,-4.669692,2.854116,-0.943808,-9.268623,2.387526,-8.727763,-1.651605,4.919934,-3.570933,8.949144,1.273245,5.156543,-3.906914,5.537689,-2.246047,8.828491,-8.226694,-0.117671,-6.577644,-6.896955,2.078588,3.228032,8.159044,-3.806008,-1.053753,-6.306720,-2.233636,4.843116,-3.352354,-9.405427,-0.526377,9.663360,-2.094494,8.756882,9.157754,-7.140301,6.993513,-6.665110,-8.278555,-4.612049,-6.493083,-3.049850,8.930528,8.154873,8.561506,-4.827360,-7.724269,-5.327997,7.591651,4.431923,8.583660,6.897366,0.017741,3.319415,2.020966,-7.883157,-1.613823,-8.765708,-5.731764,-4.640465,0.003658,8.579053,-4.836633,0.416712,-3.354223,-7.409004,-1.853961,-4.594470,-6.701183,-8.723245,3.698238,9.777904,7.471423,9.991827,-0.412535,7.143710,-7.224434,6.019701,9.382480,7.018566,4.228171,5.852855,9.387334,7.165154,-1.678470,6.202107,-1.613474,8.826551,-1.498272,0.971388,-8.837073,2.381951,-7.442310,-3.854592,0.340685,6.721909,6.976007]], dtype = "float32")#candidate|4007|(1, 210)|const|float32
call_4005 = relay.TupleGetItem(func_1347_call(relay.reshape(var_4006.astype('uint32'), [6, 10, 13]), relay.reshape(var_4006.astype('uint32'), [6, 10, 13]), relay.reshape(const_4007.astype('float32'), [210,]), ), 2)
call_4008 = relay.TupleGetItem(func_1352_call(relay.reshape(var_4006.astype('uint32'), [6, 10, 13]), relay.reshape(var_4006.astype('uint32'), [6, 10, 13]), relay.reshape(const_4007.astype('float32'), [210,]), ), 2)
output = relay.Tuple([bop_3986,uop_3991,call_3994,const_3995,const_3996,call_4005,var_4006,const_4007,])
output2 = relay.Tuple([bop_3986,uop_3991,call_3997,const_3995,const_3996,call_4008,var_4006,const_4007,])
func_4011 = relay.Function([var_3984,var_4006,], output)
mod['func_4011'] = func_4011
mod = relay.transform.InferType()(mod)
mutated_mod['func_4011'] = func_4011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4011_call = mutated_mod.get_global_var('func_4011')
var_4013 = relay.var("var_4013", dtype = "int16", shape = (10, 11, 10))#candidate|4013|(10, 11, 10)|var|int16
var_4014 = relay.var("var_4014", dtype = "uint32", shape = (780,))#candidate|4014|(780,)|var|uint32
call_4012 = func_4011_call(var_4013,var_4014,)
output = call_4012
func_4015 = relay.Function([var_4013,var_4014,], output)
mutated_mod['func_4015'] = func_4015
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4020 = relay.var("var_4020", dtype = "float64", shape = (2, 1, 11))#candidate|4020|(2, 1, 11)|var|float64
uop_4021 = relay.log(var_4020.astype('float64')) # shape=(2, 1, 11)
output = relay.Tuple([uop_4021,])
output2 = relay.Tuple([uop_4021,])
func_4024 = relay.Function([var_4020,], output)
mod['func_4024'] = func_4024
mod = relay.transform.InferType()(mod)
mutated_mod['func_4024'] = func_4024
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4025 = relay.var("var_4025", dtype = "float64", shape = (2, 1, 11))#candidate|4025|(2, 1, 11)|var|float64
func_4024_call = mutated_mod.get_global_var('func_4024')
call_4026 = func_4024_call(var_4025)
output = call_4026
func_4027 = relay.Function([var_4025], output)
mutated_mod['func_4027'] = func_4027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2579_call = mod.get_global_var('func_2579')
func_2581_call = mutated_mod.get_global_var('func_2581')
call_4050 = relay.TupleGetItem(func_2579_call(), 0)
call_4051 = relay.TupleGetItem(func_2581_call(), 0)
output = relay.Tuple([call_4050,])
output2 = relay.Tuple([call_4051,])
func_4052 = relay.Function([], output)
mod['func_4052'] = func_4052
mod = relay.transform.InferType()(mod)
mutated_mod['func_4052'] = func_4052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4052_call = mutated_mod.get_global_var('func_4052')
call_4053 = func_4052_call()
output = call_4053
func_4054 = relay.Function([], output)
mutated_mod['func_4054'] = func_4054
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4072 = relay.var("var_4072", dtype = "float64", shape = (2, 2, 13))#candidate|4072|(2, 2, 13)|var|float64
const_4073 = relay.const([[[-4.618006,2.610902,-3.668509,-3.058445,2.339225,4.995179,-4.755394,-9.399689,9.830814,-7.628490,-6.151868,5.744618,5.111516],[-2.701272,4.273235,0.421693,4.426125,-8.705522,3.457197,-7.550383,-3.550822,0.123424,7.406139,-6.790827,7.519411,1.831377]],[[8.682165,7.730536,6.393404,-4.983986,7.739378,2.327849,-3.214415,6.247939,-7.423718,-5.909454,4.954016,1.955265,1.442555],[-8.185144,-1.008383,-5.367006,-3.396808,-1.975233,-8.421833,9.002541,-1.158612,-0.458744,-4.062296,-8.627502,8.744931,1.540606]]], dtype = "float64")#candidate|4073|(2, 2, 13)|const|float64
bop_4074 = relay.subtract(var_4072.astype('float64'), relay.reshape(const_4073.astype('float64'), relay.shape_of(var_4072))) # shape=(2, 2, 13)
func_2436_call = mod.get_global_var('func_2436')
func_2437_call = mutated_mod.get_global_var('func_2437')
call_4078 = func_2436_call()
call_4079 = func_2436_call()
var_4084 = relay.var("var_4084", dtype = "float64", shape = (2, 2, 13))#candidate|4084|(2, 2, 13)|var|float64
bop_4085 = relay.less(var_4072.astype('bool'), relay.reshape(var_4084.astype('bool'), relay.shape_of(var_4072))) # shape=(2, 2, 13)
output = relay.Tuple([bop_4074,call_4078,bop_4085,])
output2 = relay.Tuple([bop_4074,call_4079,bop_4085,])
func_4091 = relay.Function([var_4072,var_4084,], output)
mod['func_4091'] = func_4091
mod = relay.transform.InferType()(mod)
mutated_mod['func_4091'] = func_4091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4091_call = mutated_mod.get_global_var('func_4091')
var_4093 = relay.var("var_4093", dtype = "float64", shape = (2, 2, 13))#candidate|4093|(2, 2, 13)|var|float64
var_4094 = relay.var("var_4094", dtype = "float64", shape = (2, 2, 13))#candidate|4094|(2, 2, 13)|var|float64
call_4092 = func_4091_call(var_4093,var_4094,)
output = call_4092
func_4095 = relay.Function([var_4093,var_4094,], output)
mutated_mod['func_4095'] = func_4095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3831_call = mod.get_global_var('func_3831')
func_3833_call = mutated_mod.get_global_var('func_3833')
call_4105 = relay.TupleGetItem(func_3831_call(), 0)
call_4106 = relay.TupleGetItem(func_3833_call(), 0)
output = relay.Tuple([call_4105,])
output2 = relay.Tuple([call_4106,])
func_4128 = relay.Function([], output)
mod['func_4128'] = func_4128
mod = relay.transform.InferType()(mod)
output = func_4128()
func_4129 = relay.Function([], output)
mutated_mod['func_4129'] = func_4129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_4143 = relay.TupleGetItem(func_723_call(), 0)
call_4144 = relay.TupleGetItem(func_725_call(), 0)
output = relay.Tuple([call_4143,])
output2 = relay.Tuple([call_4144,])
func_4156 = relay.Function([], output)
mod['func_4156'] = func_4156
mod = relay.transform.InferType()(mod)
mutated_mod['func_4156'] = func_4156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4156_call = mutated_mod.get_global_var('func_4156')
call_4157 = func_4156_call()
output = call_4157
func_4158 = relay.Function([], output)
mutated_mod['func_4158'] = func_4158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2579_call = mod.get_global_var('func_2579')
func_2581_call = mutated_mod.get_global_var('func_2581')
call_4188 = relay.TupleGetItem(func_2579_call(), 0)
call_4189 = relay.TupleGetItem(func_2581_call(), 0)
uop_4200 = relay.acosh(call_4188.astype('float64')) # shape=(9, 12, 15)
uop_4202 = relay.acosh(call_4189.astype('float64')) # shape=(9, 12, 15)
output = relay.Tuple([uop_4200,])
output2 = relay.Tuple([uop_4202,])
func_4209 = relay.Function([], output)
mod['func_4209'] = func_4209
mod = relay.transform.InferType()(mod)
mutated_mod['func_4209'] = func_4209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4209_call = mutated_mod.get_global_var('func_4209')
call_4210 = func_4209_call()
output = call_4210
func_4211 = relay.Function([], output)
mutated_mod['func_4211'] = func_4211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2436_call = mod.get_global_var('func_2436')
func_2437_call = mutated_mod.get_global_var('func_2437')
call_4226 = func_2436_call()
call_4227 = func_2436_call()
func_1283_call = mod.get_global_var('func_1283')
func_1285_call = mutated_mod.get_global_var('func_1285')
var_4229 = relay.var("var_4229", dtype = "float32", shape = (490,))#candidate|4229|(490,)|var|float32
call_4228 = relay.TupleGetItem(func_1283_call(relay.reshape(var_4229.astype('float32'), [490,])), 1)
call_4230 = relay.TupleGetItem(func_1285_call(relay.reshape(var_4229.astype('float32'), [490,])), 1)
func_3158_call = mod.get_global_var('func_3158')
func_3160_call = mutated_mod.get_global_var('func_3160')
call_4271 = relay.TupleGetItem(func_3158_call(), 0)
call_4272 = relay.TupleGetItem(func_3160_call(), 0)
var_4283 = relay.var("var_4283", dtype = "int64", shape = (9, 12, 15))#candidate|4283|(9, 12, 15)|var|int64
bop_4284 = relay.bitwise_xor(call_4228.astype('uint8'), relay.reshape(var_4283.astype('uint8'), relay.shape_of(call_4228))) # shape=(9, 12, 15)
bop_4287 = relay.bitwise_xor(call_4230.astype('uint8'), relay.reshape(var_4283.astype('uint8'), relay.shape_of(call_4230))) # shape=(9, 12, 15)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_4295 = relay.TupleGetItem(func_723_call(), 0)
call_4296 = relay.TupleGetItem(func_725_call(), 0)
func_1533_call = mod.get_global_var('func_1533')
func_1535_call = mutated_mod.get_global_var('func_1535')
call_4304 = relay.TupleGetItem(func_1533_call(), 1)
call_4305 = relay.TupleGetItem(func_1535_call(), 1)
output = relay.Tuple([call_4226,var_4229,call_4271,bop_4284,call_4295,call_4304,])
output2 = relay.Tuple([call_4227,var_4229,call_4272,bop_4287,call_4296,call_4305,])
func_4306 = relay.Function([var_4229,var_4283,], output)
mod['func_4306'] = func_4306
mod = relay.transform.InferType()(mod)
mutated_mod['func_4306'] = func_4306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4306_call = mutated_mod.get_global_var('func_4306')
var_4308 = relay.var("var_4308", dtype = "float32", shape = (490,))#candidate|4308|(490,)|var|float32
var_4309 = relay.var("var_4309", dtype = "int64", shape = (9, 12, 15))#candidate|4309|(9, 12, 15)|var|int64
call_4307 = func_4306_call(var_4308,var_4309,)
output = call_4307
func_4310 = relay.Function([var_4308,var_4309,], output)
mutated_mod['func_4310'] = func_4310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2343_call = mod.get_global_var('func_2343')
func_2345_call = mutated_mod.get_global_var('func_2345')
call_4348 = relay.TupleGetItem(func_2343_call(), 0)
call_4349 = relay.TupleGetItem(func_2345_call(), 0)
output = relay.Tuple([call_4348,])
output2 = relay.Tuple([call_4349,])
func_4350 = relay.Function([], output)
mod['func_4350'] = func_4350
mod = relay.transform.InferType()(mod)
output = func_4350()
func_4351 = relay.Function([], output)
mutated_mod['func_4351'] = func_4351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3061_call = mutated_mod.get_global_var('func_3061')
call_4367 = relay.TupleGetItem(func_3060_call(), 0)
call_4368 = relay.TupleGetItem(func_3061_call(), 0)
output = call_4367
output2 = call_4368
func_4380 = relay.Function([], output)
mod['func_4380'] = func_4380
mod = relay.transform.InferType()(mod)
mutated_mod['func_4380'] = func_4380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4380_call = mutated_mod.get_global_var('func_4380')
call_4381 = func_4380_call()
output = call_4381
func_4382 = relay.Function([], output)
mutated_mod['func_4382'] = func_4382
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4396 = relay.var("var_4396", dtype = "int64", shape = (6, 13, 1))#candidate|4396|(6, 13, 1)|var|int64
var_4397 = relay.var("var_4397", dtype = "int64", shape = (6, 13, 7))#candidate|4397|(6, 13, 7)|var|int64
bop_4398 = relay.logical_xor(var_4396.astype('int64'), var_4397.astype('int64')) # shape=(6, 13, 7)
uop_4407 = relay.atanh(var_4397.astype('float32')) # shape=(6, 13, 7)
output = relay.Tuple([bop_4398,uop_4407,])
output2 = relay.Tuple([bop_4398,uop_4407,])
func_4410 = relay.Function([var_4396,var_4397,], output)
mod['func_4410'] = func_4410
mod = relay.transform.InferType()(mod)
var_4411 = relay.var("var_4411", dtype = "int64", shape = (6, 13, 1))#candidate|4411|(6, 13, 1)|var|int64
var_4412 = relay.var("var_4412", dtype = "int64", shape = (6, 13, 7))#candidate|4412|(6, 13, 7)|var|int64
output = func_4410(var_4411,var_4412,)
func_4413 = relay.Function([var_4411,var_4412,], output)
mutated_mod['func_4413'] = func_4413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2711_call = mod.get_global_var('func_2711')
func_2713_call = mutated_mod.get_global_var('func_2713')
call_4430 = func_2711_call()
call_4431 = func_2711_call()
func_3622_call = mod.get_global_var('func_3622')
func_3624_call = mutated_mod.get_global_var('func_3624')
var_4437 = relay.var("var_4437", dtype = "float32", shape = (2016,))#candidate|4437|(2016,)|var|float32
call_4436 = relay.TupleGetItem(func_3622_call(relay.reshape(var_4437.astype('float32'), [12, 14, 12])), 0)
call_4438 = relay.TupleGetItem(func_3624_call(relay.reshape(var_4437.astype('float32'), [12, 14, 12])), 0)
func_2436_call = mod.get_global_var('func_2436')
func_2437_call = mutated_mod.get_global_var('func_2437')
call_4440 = func_2436_call()
call_4441 = func_2436_call()
output = relay.Tuple([call_4430,call_4436,var_4437,call_4440,])
output2 = relay.Tuple([call_4431,call_4438,var_4437,call_4441,])
func_4444 = relay.Function([var_4437,], output)
mod['func_4444'] = func_4444
mod = relay.transform.InferType()(mod)
var_4445 = relay.var("var_4445", dtype = "float32", shape = (2016,))#candidate|4445|(2016,)|var|float32
output = func_4444(var_4445)
func_4446 = relay.Function([var_4445], output)
mutated_mod['func_4446'] = func_4446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1010_call = mod.get_global_var('func_1010')
func_1011_call = mutated_mod.get_global_var('func_1011')
call_4448 = relay.TupleGetItem(func_1010_call(), 1)
call_4449 = relay.TupleGetItem(func_1011_call(), 1)
output = call_4448
output2 = call_4449
func_4466 = relay.Function([], output)
mod['func_4466'] = func_4466
mod = relay.transform.InferType()(mod)
mutated_mod['func_4466'] = func_4466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4466_call = mutated_mod.get_global_var('func_4466')
call_4467 = func_4466_call()
output = call_4467
func_4468 = relay.Function([], output)
mutated_mod['func_4468'] = func_4468
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4475 = relay.var("var_4475", dtype = "float64", shape = (7, 3, 14))#candidate|4475|(7, 3, 14)|var|float64
uop_4476 = relay.acosh(var_4475.astype('float64')) # shape=(7, 3, 14)
func_1908_call = mod.get_global_var('func_1908')
func_1910_call = mutated_mod.get_global_var('func_1910')
call_4480 = func_1908_call()
call_4481 = func_1908_call()
var_4492 = relay.var("var_4492", dtype = "float64", shape = (7, 3, 14))#candidate|4492|(7, 3, 14)|var|float64
bop_4493 = relay.logical_or(uop_4476.astype('bool'), relay.reshape(var_4492.astype('bool'), relay.shape_of(uop_4476))) # shape=(7, 3, 14)
uop_4497 = relay.sigmoid(uop_4476.astype('float32')) # shape=(7, 3, 14)
bop_4525 = relay.mod(uop_4497.astype('float32'), relay.reshape(var_4475.astype('float32'), relay.shape_of(uop_4497))) # shape=(7, 3, 14)
output = relay.Tuple([call_4480,bop_4493,bop_4525,])
output2 = relay.Tuple([call_4481,bop_4493,bop_4525,])
func_4536 = relay.Function([var_4475,var_4492,], output)
mod['func_4536'] = func_4536
mod = relay.transform.InferType()(mod)
var_4537 = relay.var("var_4537", dtype = "float64", shape = (7, 3, 14))#candidate|4537|(7, 3, 14)|var|float64
var_4538 = relay.var("var_4538", dtype = "float64", shape = (7, 3, 14))#candidate|4538|(7, 3, 14)|var|float64
output = func_4536(var_4537,var_4538,)
func_4539 = relay.Function([var_4537,var_4538,], output)
mutated_mod['func_4539'] = func_4539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4555 = relay.var("var_4555", dtype = "float32", shape = (3, 1, 9))#candidate|4555|(3, 1, 9)|var|float32
uop_4556 = relay.exp(var_4555.astype('float32')) # shape=(3, 1, 9)
uop_4559 = relay.cos(uop_4556.astype('float32')) # shape=(3, 1, 9)
uop_4561 = relay.asinh(uop_4559.astype('float64')) # shape=(3, 1, 9)
output = relay.Tuple([uop_4561,])
output2 = relay.Tuple([uop_4561,])
func_4574 = relay.Function([var_4555,], output)
mod['func_4574'] = func_4574
mod = relay.transform.InferType()(mod)
var_4575 = relay.var("var_4575", dtype = "float32", shape = (3, 1, 9))#candidate|4575|(3, 1, 9)|var|float32
output = func_4574(var_4575)
func_4576 = relay.Function([var_4575], output)
mutated_mod['func_4576'] = func_4576
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4578 = relay.var("var_4578", dtype = "float64", shape = (8, 7, 6))#candidate|4578|(8, 7, 6)|var|float64
uop_4579 = relay.exp(var_4578.astype('float64')) # shape=(8, 7, 6)
uop_4581 = relay.tan(var_4578.astype('float64')) # shape=(8, 7, 6)
func_4024_call = mod.get_global_var('func_4024')
func_4027_call = mutated_mod.get_global_var('func_4027')
const_4587 = relay.const([[-1.347313],[3.337339],[-8.192915],[3.339116],[4.875704],[-5.479613],[2.176091],[7.999596],[-1.880546],[-3.789691],[5.936578],[-3.902599],[3.739921],[-5.210648],[-8.236186],[1.674612],[-6.132313],[-8.925806],[6.764044],[5.712866],[-6.358938],[2.151393]], dtype = "float64")#candidate|4587|(22, 1)|const|float64
call_4586 = relay.TupleGetItem(func_4024_call(relay.reshape(const_4587.astype('float64'), [2, 1, 11])), 0)
call_4588 = relay.TupleGetItem(func_4027_call(relay.reshape(const_4587.astype('float64'), [2, 1, 11])), 0)
uop_4604 = relay.sigmoid(var_4578.astype('float64')) # shape=(8, 7, 6)
output = relay.Tuple([uop_4579,uop_4581,call_4586,const_4587,uop_4604,])
output2 = relay.Tuple([uop_4579,uop_4581,call_4588,const_4587,uop_4604,])
func_4609 = relay.Function([var_4578,], output)
mod['func_4609'] = func_4609
mod = relay.transform.InferType()(mod)
var_4610 = relay.var("var_4610", dtype = "float64", shape = (8, 7, 6))#candidate|4610|(8, 7, 6)|var|float64
output = func_4609(var_4610)
func_4611 = relay.Function([var_4610], output)
mutated_mod['func_4611'] = func_4611
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4711 = relay.var("var_4711", dtype = "int32", shape = (1, 9, 3))#candidate|4711|(1, 9, 3)|var|int32
var_4712 = relay.var("var_4712", dtype = "int32", shape = (14, 9, 3))#candidate|4712|(14, 9, 3)|var|int32
bop_4713 = relay.maximum(var_4711.astype('int32'), var_4712.astype('int32')) # shape=(14, 9, 3)
func_3622_call = mod.get_global_var('func_3622')
func_3624_call = mutated_mod.get_global_var('func_3624')
var_4719 = relay.var("var_4719", dtype = "float32", shape = (1, 2016))#candidate|4719|(1, 2016)|var|float32
call_4718 = relay.TupleGetItem(func_3622_call(relay.reshape(var_4719.astype('float32'), [12, 14, 12])), 1)
call_4720 = relay.TupleGetItem(func_3624_call(relay.reshape(var_4719.astype('float32'), [12, 14, 12])), 1)
output = relay.Tuple([bop_4713,call_4718,var_4719,])
output2 = relay.Tuple([bop_4713,call_4720,var_4719,])
func_4724 = relay.Function([var_4711,var_4712,var_4719,], output)
mod['func_4724'] = func_4724
mod = relay.transform.InferType()(mod)
var_4725 = relay.var("var_4725", dtype = "int32", shape = (1, 9, 3))#candidate|4725|(1, 9, 3)|var|int32
var_4726 = relay.var("var_4726", dtype = "int32", shape = (14, 9, 3))#candidate|4726|(14, 9, 3)|var|int32
var_4727 = relay.var("var_4727", dtype = "float32", shape = (1, 2016))#candidate|4727|(1, 2016)|var|float32
output = func_4724(var_4725,var_4726,var_4727,)
func_4728 = relay.Function([var_4725,var_4726,var_4727,], output)
mutated_mod['func_4728'] = func_4728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1908_call = mod.get_global_var('func_1908')
func_1910_call = mutated_mod.get_global_var('func_1910')
call_4735 = func_1908_call()
call_4736 = func_1908_call()
func_2551_call = mod.get_global_var('func_2551')
func_2553_call = mutated_mod.get_global_var('func_2553')
call_4738 = relay.TupleGetItem(func_2551_call(), 0)
call_4739 = relay.TupleGetItem(func_2553_call(), 0)
output = relay.Tuple([call_4735,call_4738,])
output2 = relay.Tuple([call_4736,call_4739,])
func_4757 = relay.Function([], output)
mod['func_4757'] = func_4757
mod = relay.transform.InferType()(mod)
mutated_mod['func_4757'] = func_4757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4757_call = mutated_mod.get_global_var('func_4757')
call_4758 = func_4757_call()
output = call_4758
func_4759 = relay.Function([], output)
mutated_mod['func_4759'] = func_4759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2343_call = mod.get_global_var('func_2343')
func_2345_call = mutated_mod.get_global_var('func_2345')
call_4770 = relay.TupleGetItem(func_2343_call(), 0)
call_4771 = relay.TupleGetItem(func_2345_call(), 0)
func_4350_call = mod.get_global_var('func_4350')
func_4351_call = mutated_mod.get_global_var('func_4351')
call_4780 = relay.TupleGetItem(func_4350_call(), 0)
call_4781 = relay.TupleGetItem(func_4351_call(), 0)
output = relay.Tuple([call_4770,call_4780,])
output2 = relay.Tuple([call_4771,call_4781,])
func_4797 = relay.Function([], output)
mod['func_4797'] = func_4797
mod = relay.transform.InferType()(mod)
output = func_4797()
func_4798 = relay.Function([], output)
mutated_mod['func_4798'] = func_4798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4156_call = mod.get_global_var('func_4156')
func_4158_call = mutated_mod.get_global_var('func_4158')
call_4857 = relay.TupleGetItem(func_4156_call(), 0)
call_4858 = relay.TupleGetItem(func_4158_call(), 0)
output = call_4857
output2 = call_4858
func_4875 = relay.Function([], output)
mod['func_4875'] = func_4875
mod = relay.transform.InferType()(mod)
output = func_4875()
func_4876 = relay.Function([], output)
mutated_mod['func_4876'] = func_4876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4466_call = mod.get_global_var('func_4466')
func_4468_call = mutated_mod.get_global_var('func_4468')
call_4907 = func_4466_call()
call_4908 = func_4466_call()
func_2711_call = mod.get_global_var('func_2711')
func_2713_call = mutated_mod.get_global_var('func_2713')
call_4909 = func_2711_call()
call_4910 = func_2711_call()
output = relay.Tuple([call_4907,call_4909,])
output2 = relay.Tuple([call_4908,call_4910,])
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
func_2711_call = mod.get_global_var('func_2711')
func_2713_call = mutated_mod.get_global_var('func_2713')
call_4927 = func_2711_call()
call_4928 = func_2711_call()
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_4931 = relay.TupleGetItem(func_723_call(), 0)
call_4932 = relay.TupleGetItem(func_725_call(), 0)
output = relay.Tuple([call_4927,call_4931,])
output2 = relay.Tuple([call_4928,call_4932,])
func_4950 = relay.Function([], output)
mod['func_4950'] = func_4950
mod = relay.transform.InferType()(mod)
mutated_mod['func_4950'] = func_4950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4950_call = mutated_mod.get_global_var('func_4950')
call_4951 = func_4950_call()
output = call_4951
func_4952 = relay.Function([], output)
mutated_mod['func_4952'] = func_4952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_4953 = relay.TupleGetItem(func_303_call(), 1)
call_4954 = relay.TupleGetItem(func_304_call(), 1)
output = relay.Tuple([call_4953,])
output2 = relay.Tuple([call_4954,])
func_4964 = relay.Function([], output)
mod['func_4964'] = func_4964
mod = relay.transform.InferType()(mod)
output = func_4964()
func_4965 = relay.Function([], output)
mutated_mod['func_4965'] = func_4965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4466_call = mod.get_global_var('func_4466')
func_4468_call = mutated_mod.get_global_var('func_4468')
call_4969 = func_4466_call()
call_4970 = func_4466_call()
func_2579_call = mod.get_global_var('func_2579')
func_2581_call = mutated_mod.get_global_var('func_2581')
call_4997 = relay.TupleGetItem(func_2579_call(), 0)
call_4998 = relay.TupleGetItem(func_2581_call(), 0)
output = relay.Tuple([call_4969,call_4997,])
output2 = relay.Tuple([call_4970,call_4998,])
func_5000 = relay.Function([], output)
mod['func_5000'] = func_5000
mod = relay.transform.InferType()(mod)
output = func_5000()
func_5001 = relay.Function([], output)
mutated_mod['func_5001'] = func_5001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4380_call = mod.get_global_var('func_4380')
func_4382_call = mutated_mod.get_global_var('func_4382')
call_5015 = func_4380_call()
call_5016 = func_4380_call()
output = relay.Tuple([call_5015,])
output2 = relay.Tuple([call_5016,])
func_5021 = relay.Function([], output)
mod['func_5021'] = func_5021
mod = relay.transform.InferType()(mod)
output = func_5021()
func_5022 = relay.Function([], output)
mutated_mod['func_5022'] = func_5022
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5064 = relay.var("var_5064", dtype = "uint64", shape = ())#candidate|5064|()|var|uint64
var_5065 = relay.var("var_5065", dtype = "uint64", shape = (6, 2, 3))#candidate|5065|(6, 2, 3)|var|uint64
bop_5066 = relay.multiply(var_5064.astype('uint64'), var_5065.astype('uint64')) # shape=(6, 2, 3)
func_4011_call = mod.get_global_var('func_4011')
func_4015_call = mutated_mod.get_global_var('func_4015')
var_5070 = relay.var("var_5070", dtype = "int16", shape = (1100,))#candidate|5070|(1100,)|var|int16
var_5071 = relay.var("var_5071", dtype = "uint32", shape = (10, 78))#candidate|5071|(10, 78)|var|uint32
call_5069 = relay.TupleGetItem(func_4011_call(relay.reshape(var_5070.astype('int16'), [10, 11, 10]), relay.reshape(var_5071.astype('uint32'), [780,]), ), 1)
call_5072 = relay.TupleGetItem(func_4015_call(relay.reshape(var_5070.astype('int16'), [10, 11, 10]), relay.reshape(var_5071.astype('uint32'), [780,]), ), 1)
output = relay.Tuple([bop_5066,call_5069,var_5070,var_5071,])
output2 = relay.Tuple([bop_5066,call_5072,var_5070,var_5071,])
func_5074 = relay.Function([var_5064,var_5065,var_5070,var_5071,], output)
mod['func_5074'] = func_5074
mod = relay.transform.InferType()(mod)
mutated_mod['func_5074'] = func_5074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5074_call = mutated_mod.get_global_var('func_5074')
var_5076 = relay.var("var_5076", dtype = "uint64", shape = ())#candidate|5076|()|var|uint64
var_5077 = relay.var("var_5077", dtype = "uint64", shape = (6, 2, 3))#candidate|5077|(6, 2, 3)|var|uint64
var_5078 = relay.var("var_5078", dtype = "int16", shape = (1100,))#candidate|5078|(1100,)|var|int16
var_5079 = relay.var("var_5079", dtype = "uint32", shape = (10, 78))#candidate|5079|(10, 78)|var|uint32
call_5075 = func_5074_call(var_5076,var_5077,var_5078,var_5079,)
output = call_5075
func_5080 = relay.Function([var_5076,var_5077,var_5078,var_5079,], output)
mutated_mod['func_5080'] = func_5080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2343_call = mod.get_global_var('func_2343')
func_2345_call = mutated_mod.get_global_var('func_2345')
call_5113 = relay.TupleGetItem(func_2343_call(), 0)
call_5114 = relay.TupleGetItem(func_2345_call(), 0)
output = relay.Tuple([call_5113,])
output2 = relay.Tuple([call_5114,])
func_5125 = relay.Function([], output)
mod['func_5125'] = func_5125
mod = relay.transform.InferType()(mod)
output = func_5125()
func_5126 = relay.Function([], output)
mutated_mod['func_5126'] = func_5126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4156_call = mod.get_global_var('func_4156')
func_4158_call = mutated_mod.get_global_var('func_4158')
call_5181 = relay.TupleGetItem(func_4156_call(), 0)
call_5182 = relay.TupleGetItem(func_4158_call(), 0)
output = relay.Tuple([call_5181,])
output2 = relay.Tuple([call_5182,])
func_5183 = relay.Function([], output)
mod['func_5183'] = func_5183
mod = relay.transform.InferType()(mod)
mutated_mod['func_5183'] = func_5183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5183_call = mutated_mod.get_global_var('func_5183')
call_5184 = func_5183_call()
output = call_5184
func_5185 = relay.Function([], output)
mutated_mod['func_5185'] = func_5185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4964_call = mod.get_global_var('func_4964')
func_4965_call = mutated_mod.get_global_var('func_4965')
call_5209 = relay.TupleGetItem(func_4964_call(), 0)
call_5210 = relay.TupleGetItem(func_4965_call(), 0)
func_1347_call = mod.get_global_var('func_1347')
func_1352_call = mutated_mod.get_global_var('func_1352')
const_5220 = relay.const([-8,6,8,-10,8,7,-5,-2,2,-7,-4,1,3,-2,-1,10,-7,3,-4,4,-7,3,6,6,-5,6,1,1,9,2,-6,7,-1,-1,-5,7,5,-3,-9,-8,-10,-6,-4,-9,-2,-2,3,2,-4,-9,7,1,9,-3,-5,-5,-5,-7,9,5,7,8,9,-6,-4,-1,4,-2,-8,-1,8,-7,6,4,-2,-7,-6,-10,6,7,-2,10,10,9,9,-2,-6,9,-5,-9,2,7,-10,5,5,-9,-10,-5,1,2,-3,-6,-3,3,10,4,-8,9,10,-6,-6,3,4,-10,-1,-8,7,5,10,6,10,1,-3,-5,-6,7,8,2,8,-8,4,-5,-9,-9,-8,9,8,-5,-2,-3,3,-2,2,2,4,10,7,9,6,7,4,2,-5,5,7,-8,10,9,2,1,-3,-3,6,6,-9,-6,8,7,4,3,-9,-10,-8,10,-2,5,-2,6,2,10,5,-6,-3,-8,-6,6,1,6,-7,-1,-9,-6,7,-9,-6,-10,-4,-5,9,1,6,3,-5,9,5,-3,-6,-5,3,-2,4,1,8,2,1,3,3,5,4,2,-3,6,-5,2,7,-8,-6,9,-7,1,6,-5,1,7,-3,-7,-5,8,5,8,6,7,7,3,-8,-3,-10,3,2,9,10,-4,10,-5,-1,-1,10,-6,3,-2,8,3,-8,1,10,-5,-5,-5,8,4,-2,-6,-10,-9,4,1,-9,-1,-5,-4,10,5,-6,-4,10,-4,10,7,2,4,7,9,-2,-10,-1,-9,-4,10,-5,-6,10,-1,10,2,-4,-10,-2,9,-1,10,-5,-5,-5,1,-9,7,7,-2,6,8,10,10,-1,5,-10,-4,-6,-4,-3,-1,9,4,5,-2,-9,10,-2,-3,-1,-3,-5,-4,5,4,-2,-4,2,-9,-3,-8,5,4,-10,8,-7,-2,7,5,-5,-2,3,-2,-4,-2,3,-9,-7,6,2,-1,-3,1,-1,2,7,-5,-1,-5,-9,2,-6,2,6,3,10,-4,6,-2,6,-5,9,-3,-8,-5,-3,10,-8,3,10,1,-9,-2,-2,6,-10,1,2,2,-2,10,4,5,2,-7,5,2,-2,-10,9,-2,-6,10,7,-1,-1,-4,-1,-8,-8,-5,4,6,-10,-10,-2,-9,7,8,3,5,-10,-8,8,4,-2,9,-4,2,1,6,6,4,7,7,3,4,1,-4,10,6,-7,-10,10,-9,-5,4,10,-5,10,-7,-6,-6,-2,7,-10,-6,8,10,-7,10,-3,5,2,10,-2,5,-7,6,-5,1,-5,-2,10,-2,-2,3,5,-1,-6,1,10,-7,-8,6,5,9,-2,-1,-5,-3,5,4,-2,9,8,9,5,-4,-8,-6,-8,2,-4,-6,8,-5,7,-3,6,8,-9,1,2,6,-8,4,-5,-9,1,-9,-7,10,-6,5,-4,-6,-10,8,4,6,6,1,-8,2,6,-8,8,8,-2,5,-6,2,10,1,-4,10,-7,-3,1,-4,-7,-1,2,-8,-2,2,-6,7,-4,1,-5,10,-2,-9,-8,-10,-7,7,-10,-4,8,2,8,-1,8,-2,5,-5,5,-9,-6,8,-2,3,-2,6,-10,-5,8,3,-9,6,-9,2,6,-6,2,8,-3,-8,7,-6,-2,7,10,-5,7,3,-4,-9,-8,-3,-3,6,1,10,8,6,8,8,-5,6,-6,-7,8,1,3,8,-4,-1,-10,4,8,6,3,-5,-6,-10,4,3,7,7,7,-7,2,5,-8,8,8,3,7,-10,1,-7,9,-4,-3,8,8,10,-1,10,5,7,-9,5,-10,-10,4,3,-5,-2,2,8,-5,-8,3,-8,-5,2,-7,1,-1,-8,8,8,2,2,2,-4,8,3,-9,2,10,-9,2,-6,-2,-7,8,2,7,-4,5,6,-9,7,-4,3,6,2,-3,-2,-3,-3,-4,10,2,4,3,3,3,-9,2,10,7,7,-8,-5,5,3,7,-5,-9,-6,-1,4,10,8,7,-9,9,4,-4,2,1,1,9,6,-6,-10,-3,10,8,-7,-7,-9,2,-6], dtype = "uint32")#candidate|5220|(780,)|const|uint32
const_5221 = relay.const([[9.393014,-3.886415],[-8.164400,8.579894],[-0.741082,-4.937723],[-7.498107,7.700496],[9.568077,1.896802],[1.464129,6.588798],[-6.792190,-0.010281],[8.249210,3.548728],[1.295826,-9.395545],[5.165610,9.511939],[3.785354,9.217783],[-6.927128,-8.328276],[4.933554,8.816115],[1.715560,0.841716],[-7.704254,-0.568506],[-1.088822,-9.401003],[7.443680,-0.275279],[5.110702,-9.436428],[8.135251,-8.689619],[5.308684,1.175811],[-1.365851,1.034000],[3.527470,-1.417827],[-5.050776,-8.212015],[-5.524905,-6.375686],[8.510964,-6.812281],[6.503639,5.746993],[2.065874,-9.346986],[-2.239668,6.677772],[3.584726,7.677945],[8.966628,-1.651807],[-2.922508,1.370061],[7.573028,9.796709],[-7.688913,6.102079],[-3.796918,-7.457758],[-8.547994,-9.178543],[-5.230953,-0.670296],[-5.659946,-2.768757],[7.379250,-0.154999],[5.873951,-9.556644],[6.516903,6.314829],[-9.328517,7.634339],[6.103850,-9.411553],[0.778029,2.136965],[-3.401410,0.461438],[3.082233,8.408971],[-7.173799,-1.540951],[9.603595,-9.005552],[-3.810669,-0.023478],[5.818313,-3.285260],[4.940839,-9.538986],[0.930076,-5.863198],[8.297697,9.132326],[4.861748,5.615364],[-9.782050,-1.122060],[0.775649,-0.328072],[-6.950711,-1.371703],[4.374808,0.902728],[6.144630,4.739191],[4.719248,-8.139583],[6.086814,2.788575],[-7.893874,-4.560132],[-5.764725,-9.617571],[3.321561,-1.237220],[8.085508,0.456727],[8.223928,0.779544],[1.038275,8.968500],[-0.749321,7.978428],[8.238892,9.247455],[-1.773725,-9.839349],[-5.199389,-2.867625],[-1.452675,5.030038],[8.328469,-3.251754],[8.136189,2.043603],[-0.015476,4.451693],[-4.870604,-0.349945],[6.990906,-7.877260],[4.656720,1.953512],[8.413969,2.886965],[-7.199513,-8.988395],[-6.333598,-5.227461],[-2.257371,-3.954866],[-6.838796,-8.023044],[-3.056983,4.751069],[-5.370263,3.133016],[-0.399068,6.550415],[-5.333480,3.810936],[5.020543,-7.730605],[-2.512790,-7.955738],[-0.628183,6.594364],[-0.284964,-7.867096],[-4.232231,4.565783],[5.949911,-4.118666],[1.344358,1.861443],[2.721959,-0.155113],[-3.782011,-0.444916],[3.627289,-0.452512],[5.336728,-6.281704],[2.258983,-8.509037],[-6.876131,-3.433115],[2.040945,-2.860061],[-7.414507,-2.065053],[-0.158812,-9.476812],[-7.416692,-0.067746],[0.293388,6.077626],[-7.332362,0.860736]], dtype = "float32")#candidate|5221|(105, 2)|const|float32
call_5219 = relay.TupleGetItem(func_1347_call(relay.reshape(const_5220.astype('uint32'), [6, 10, 13]), relay.reshape(const_5220.astype('uint32'), [6, 10, 13]), relay.reshape(const_5221.astype('float32'), [210,]), ), 0)
call_5222 = relay.TupleGetItem(func_1352_call(relay.reshape(const_5220.astype('uint32'), [6, 10, 13]), relay.reshape(const_5220.astype('uint32'), [6, 10, 13]), relay.reshape(const_5221.astype('float32'), [210,]), ), 0)
output = relay.Tuple([call_5209,call_5219,const_5220,const_5221,])
output2 = relay.Tuple([call_5210,call_5222,const_5220,const_5221,])
func_5223 = relay.Function([], output)
mod['func_5223'] = func_5223
mod = relay.transform.InferType()(mod)
output = func_5223()
func_5224 = relay.Function([], output)
mutated_mod['func_5224'] = func_5224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2352_call = mod.get_global_var('func_2352')
func_2354_call = mutated_mod.get_global_var('func_2354')
call_5246 = relay.TupleGetItem(func_2352_call(), 0)
call_5247 = relay.TupleGetItem(func_2354_call(), 0)
output = relay.Tuple([call_5246,])
output2 = relay.Tuple([call_5247,])
func_5250 = relay.Function([], output)
mod['func_5250'] = func_5250
mod = relay.transform.InferType()(mod)
output = func_5250()
func_5251 = relay.Function([], output)
mutated_mod['func_5251'] = func_5251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1010_call = mod.get_global_var('func_1010')
func_1011_call = mutated_mod.get_global_var('func_1011')
call_5308 = relay.TupleGetItem(func_1010_call(), 1)
call_5309 = relay.TupleGetItem(func_1011_call(), 1)
uop_5313 = relay.log(call_5308.astype('float64')) # shape=(9, 12, 15)
uop_5315 = relay.log(call_5309.astype('float64')) # shape=(9, 12, 15)
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
var_5329 = relay.var("var_5329", dtype = "bool", shape = ())#candidate|5329|()|var|bool
call_5328 = relay.TupleGetItem(func_408_call(relay.reshape(var_5329.astype('bool'), [])), 2)
call_5330 = relay.TupleGetItem(func_411_call(relay.reshape(var_5329.astype('bool'), [])), 2)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_5332 = func_2881_call()
call_5333 = func_2881_call()
output = relay.Tuple([uop_5313,call_5328,var_5329,call_5332,])
output2 = relay.Tuple([uop_5315,call_5330,var_5329,call_5333,])
func_5335 = relay.Function([var_5329,], output)
mod['func_5335'] = func_5335
mod = relay.transform.InferType()(mod)
mutated_mod['func_5335'] = func_5335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5336 = relay.var("var_5336", dtype = "bool", shape = ())#candidate|5336|()|var|bool
func_5335_call = mutated_mod.get_global_var('func_5335')
call_5337 = func_5335_call(var_5336)
output = call_5337
func_5338 = relay.Function([var_5336], output)
mutated_mod['func_5338'] = func_5338
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5342 = relay.var("var_5342", dtype = "float64", shape = (1, 11, 14))#candidate|5342|(1, 11, 14)|var|float64
uop_5343 = relay.exp(var_5342.astype('float64')) # shape=(1, 11, 14)
uop_5349 = relay.log(var_5342.astype('float64')) # shape=(1, 11, 14)
output = relay.Tuple([uop_5343,uop_5349,])
output2 = relay.Tuple([uop_5343,uop_5349,])
func_5352 = relay.Function([var_5342,], output)
mod['func_5352'] = func_5352
mod = relay.transform.InferType()(mod)
var_5353 = relay.var("var_5353", dtype = "float64", shape = (1, 11, 14))#candidate|5353|(1, 11, 14)|var|float64
output = func_5352(var_5353)
func_5354 = relay.Function([var_5353], output)
mutated_mod['func_5354'] = func_5354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3061_call = mutated_mod.get_global_var('func_3061')
call_5375 = relay.TupleGetItem(func_3060_call(), 0)
call_5376 = relay.TupleGetItem(func_3061_call(), 0)
output = call_5375
output2 = call_5376
func_5379 = relay.Function([], output)
mod['func_5379'] = func_5379
mod = relay.transform.InferType()(mod)
output = func_5379()
func_5380 = relay.Function([], output)
mutated_mod['func_5380'] = func_5380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2579_call = mod.get_global_var('func_2579')
func_2581_call = mutated_mod.get_global_var('func_2581')
call_5417 = relay.TupleGetItem(func_2579_call(), 0)
call_5418 = relay.TupleGetItem(func_2581_call(), 0)
func_5223_call = mod.get_global_var('func_5223')
func_5224_call = mutated_mod.get_global_var('func_5224')
call_5420 = relay.TupleGetItem(func_5223_call(), 3)
call_5421 = relay.TupleGetItem(func_5224_call(), 3)
func_693_call = mod.get_global_var('func_693')
func_696_call = mutated_mod.get_global_var('func_696')
const_5431 = relay.const([-8,8,-6,-5,-3,-6,8,4,-6,-10,7,5,-8,6,-1,-7,-3,2,2,-8,6,4,5,6,4,-6,-7,-6,3,9,1,3,-9,-5,-4,-7,-9,4,8,7,7,-4,-4,1,4,-3,4,-9,3,-7,7,7,5,-9,-3,-7,-10,7,1,3,-8,10,-4,-8,-3,4,-6,-5,2,6,-10,8,-5,-8,-4,2,7,5,-3,8,7,5,1,-8,1,2,8,3,-6,-10,2,-2,5,2,-2,3,10,-7,-5,-8,7,-2,-2,8,6,8,-9,-10,-2,4,1,-5,3,-4,7,9,-1,-10,-5,-1,-6,10,-3,-2,3,9,1,-4,8,-5,1,-8,2,-5,4,-8,7,6,10,-5,3,-6,-9,-1,10,1,-9,-4,-7,-7,-7,3,-7,-5,8,10,5,-8,-6,-1,-6,-6,3,7,10,-1,3,2,5,-6,9,-8,10,9,6,2,4,8,-9,7,1,6,-4,-3,-10,-3,3,-3,7,10,-4,7,10,7,-10,-9,-2,4,-5,-4,4,-4,-1,1,-1,-3,-3,6,6,5,6,7,-10,4,8,10,7,10,-3,8,-3,-10,9,-4,-9,-1,2,3,-6,7,6,5,-1,3,-9,-7,-10,-1,-5,6,-3,-9,4,6,10,6,-1,1,-8,-6,-3,-9,10,-4,4,-8,-8,1,2,1,-1,10,-8,3,-3,-2,2,9,-1,8,4,2,7,-3,-1,1,-1,-5,9,-4,-9,-9,8,-4,5,-4,-9,3,10,-5,8,4,-6,-8,-6,-9,9,-7,-8,-7,2,1,10,7,10,10,7,-9,2,2,-10,-5,9,-9,3,-1,7,-6,6,6,5,-3,-9,-7,-10,1,10,-10,-7,9,4,7,-1,-8,-8,4,2,10,-2,2,-8,1,-8,8,-1,-7,6,-8,-1,-6,3,-6,7,-6,-3,-10,-3,8,5,9,2,1,-2,-6,7,3,2,-5,-3,8,3,-6,1,10,-1,-10,-6,2,-1,-2,10,10,-3,9,-8,-4,6,-7,-4,-1,-5,10,5,9,8,-6,-7,8,-1,-5,-7,2,-9,-8,-8,-9,-9,4,1,-2,7,7,2,3,4,4,9,5,-7,-2,-2,-7,2,-5,-9,1,-4,-7,4,2,7,1,4,-3,-7,-3,8,1,5,2,-4,-7,9,-5,-5,-3,2,8,10,-6,-8,7,1,7,-4,10,-2,-4,-3,6,-5,10,-2,5,10,8,-2,-6,-1,-1,-2,2,-7,6,7,-8,10,-2,-6,6,-10,-8,9,7,6,8,-6,1,7,5,-1,8,3,-6,9,-9,-6,3,-10,9,8,-2,-6,-2,-2,8,-2,-5,-6,-7,4,-8,-2,10,-3,8,4,6,6,-6,-6,2,-1,-4,1,-4,9,7,-2,5,-4,7,-4,-2,2,9,-4,-6,1,4,5,-6,1,-8,-8,10,-8,2,1,-2,-3,1,-3,2,10,5,3,10,3,-9,-4,3,-6,-4,10,-2,-1,8,-1,-8,-6,8,2,-5,7,6,-3,-3,-7,-7,-5,9,1,9,-10,5,-10,5,-1,9,-4,-9,-5,9,-9,8,-5,-1,-6,2,-9,-10,-10,-5,5,10,10,-10,4,-6,6,-9,2,-1,2,2,10,4,-7,4,-4,5,6,8,5,-2,-9,5,-3,-10,10,10,-2,-2,3,4,2,1,7,9,5,-4,-4,-8,7,-4,7,-7,-8,1,6,-1,5,8,1,-3,-9,-3,-7,-2,6,-1,9,4,-8,-1,8,-5,-3,-4,-10,-5,5,-2,8,7,9,6,6,9,5,-2,-3,-8,2,3,3,1,-5,-10,-8,-6,7,-8,2,-10,-7,-1,-9,-7,5,3,9,5,8,6,4,-2,1,-5,7,-1,-8,-5,3,8,-3,5,-6,5,-6,9,-2,-3,2,8,-3,-4,-3,-8,2,-4,10,8,-8,1,5,-5,2,1,-8,-3,-8,-10,9,-7,5,-7,-1,-10,-1,6,-10,4,1,-7,-2,7,-9,-3,6,-9,-3,7,-3,-4,5,-10,-1,8,8,10,-6,-2,-8,3,-6,9,1,1,1,8,-7,3,-3,-1,-6,2,2,9,10,-5,6,-4,-8,-3,-2,6,-7,7,-2,10,-1,-2,-8,-2,4,-5,-9,-9,5,5,1,9,2,10,6,2,4,-10,-4,1,10,-8,6,-8,-9,10,-6,-8,7,-10,9,10,-5,-6,-5,-7,-4,3,-2,2,-4,1,-1,6,-8,1,-10,1,-3,4,-5,-2,6,10,6,9,-2,10,1,1,6,-7,5,2,4,-6,7,-9,-3,10,8,-1,-2,-6,-9,-10,-1,1,-6,3,-1,10,-9,2,5,3,-3,-8,5,8,10,-9,7,-8,3,3,-2,-3,-2,-5,8,2,2,6,3,1,2,-6,-10,-1,6,8,-9,-9,7,-7,1,6,-7,-1,8,4,2,10,4,6,9,8,-6,-6,2,-5,1,8,-6,10,1,-6,6,4,1,-2,5,-6,-6,3,6,-2,-1,-8,-9,3,-4,2,6,2,7,6,3,-2,-4,8,3,8,-2,1,5,-1,2,1,-1,-3,-6,-8,-1,-7,-5,7,-6,-2,-1,10,-6,5,6,5,-8,4,9,2,-4,7,5,-9,-8,9,-3,-5,2,8,5,-5,-2,-6,3,-1,6,-10,1,-2,-10,8,4,4,-5,-3,-6,3,9,8,-7,3,-8,-4,10,-10,9,-8,3,-8,-6,9,1,-1,3,-4,-10,-4,10,9,-4,-2,9,5,-2,10,-5,-10,-3,9,-2,-4,2,1,8,1,1,4,-5,-1,3,5,-10,-4,-7,9,-10,2,-3,-3,4,-2,1,-4,6,-3,5,-6,-4,10,-5,-3,-5,6,-1,-8,5,10,7,-10,7,3,3,1,-10,-1,3,2,2,-6,7,7,-6,-7,1,8,-1,4,-10,3,7,7,-9,-7,-6,-3,-7,-4,7,5,-9,8,6,5,-6,-8,-2,4,-5,-2,2,-6,6,-1,1,1,-3,-1,-10,6,3,-10,10,-6,-4,8,6,6,-3,-4,-5,4,1,-6,2,-6,6,1,9,3,-8,9,4,-5,-2,-1,4,-6,3,-8,4,1,10,-7,7,-10,8,8,-3,-9,2,4,5,10,2,4,-2,5,5,10,-2,7,-10,-4,-8,9,-2,5,-3,-7,5,-8,-4,-8,8,1,8,10,4,2,6,3,4,-5,-5,1,-2,4,5,5,1,1,-5,-9,6,1,3,-8,-2,-6,-5,-4,8,-5,3,4,7,3,-10,-8,-4,-6,3,-7,-7,1,-2,1,4,-2,-5,10,6,3,-8,10,-2,-10,-2,-1,10,1,6,1,-7,8,1,-5,3,-3,-2,2,1,10,-7,-10,-10,10,-4,-7,-5,-4,-3,5,8,-5,-1,6,-9,3,7,4,8,-3,-6,-3,5,7,-6,-2,-10,-7,-5,3,9,-9,-1,2,-8,2,-7,-3,2,-10,4,-5,8,7], dtype = "uint8")#candidate|5431|(1320,)|const|uint8
call_5430 = relay.TupleGetItem(func_693_call(relay.reshape(const_5431.astype('uint8'), [15, 8, 11])), 0)
call_5432 = relay.TupleGetItem(func_696_call(relay.reshape(const_5431.astype('uint8'), [15, 8, 11])), 0)
func_4410_call = mod.get_global_var('func_4410')
func_4413_call = mutated_mod.get_global_var('func_4413')
const_5437 = relay.const([3,-10,8,5,10,8,3,3,-7,-3,-9,2,2,7,-8,-7,-4,7,-7,-2,4,6,7,-9,2,-9,-2,8,1,-5,-4,9,1,8,8,-4,-3,-2,-2,7,2,4,9,9,7,-8,-8,9,-2,-9,8,-5,-6,3,9,-3,-6,-4,-8,4,6,-6,-10,6,-3,-6,-8,4,-9,3,7,-10,2,-9,-6,-6,6,9], dtype = "int64")#candidate|5437|(78,)|const|int64
const_5438 = relay.const([[1,7,-7,8,9,4,-1,-7,2,4,9,-8,-4,-2,6,3,5,1,-8,-4,2,5,8,8,-3,3,-10,-6,10,5,5,-3,9,2,4,-4,-3,2,2,3,-2,-1,5,-7,5,-1,10,-1,-10,6,-9,2,3,5,-4,5,5,8,-3,-3,7,-7,7,-5,10,-3,-4,-5,7,-4,-10,-6,-3,3,9,2,-9,2,8,-5,1,-1,10,-3,6,7,6,-9,10,-5,-7,5,-10,5,6,-8,7,5,-3,-6,6,5,9,-1,5,7,4,1,1,-10,6,-8,-7,-10,-3,-9,2,-3,7,9,9,-7,10,-5,-4,9,-6,2,-10,-4,-1,-2,-9,3,8,-10,-9,-9,5,-1,-2,-6,9,-2,10,-2,10,-3,10,7,-9,-6,-5,9,-1,-8,1,3,-4,9,-10,-5,8,1,6,-7,-8,3,-7,5,5,5,9,-7,3,-9,8,5,-3,-5,6,-4,-4,10,-1,3,2,1,-6,-6,-4,-1,-10,10,3,-4,9,5,-5,7,4,4,-10,7,3,4,-8,-4,1,2,1,-5,4,-6,-9,-6,4,8,5,1,-9,-7,-10,-5,-5,7,5,-8,3,9,-6,-4,-7,6,8,-1,-4,3,-9,7,9,4,5,2,-4,10,8,-4,-4,6,-10,8,7,-8,-2,-2,10,-3,-8,2,8,3,6,10,10,2,2,3,-1,-6,9,-2,-4,3,3,-5,9,-6,7,-7,-1,6,6,3,-4,10,8,2,8,5,5,10,-8,-1,2,10,4,7,7,9,10,7,-9,10,-4,-9,-5,-5,7,5,-3,-3,3,8,1,-3,7,8,9,-5,3,4,-5,8,-4,-3,10,-5,-7,2,2,-8,-7,5,4,-9,-4,-4,1,-10,7,-5,1,-9,-4,-8,-8,7,3,-1,2,6,2,-4,4,-1,9,-7,7,9,-6,-10,-3,2,-9,-5,-3,-8,2,2,-7,-8,-1,5,2,-9,-8,5,-8,-7,1,9,-4,-1,-10,-4,-7,1,9,4,-9,10,-4,9,3,8,-10,8,-5,-10,-3,1,-7,8,10,7,-6,9,1,9,-5,-6,5,9,-4,-4,3,6,10,8,-7,9,2,-3,-7,-7,-1,-5,8,6,-5,8,8,10,2,-7,-4,2,8,9,8,-6,-8,3,7,7,-2,9,-2,9,8,-1,-6,-8,-6,8,2,3,8,-5,7,-6,6,-10,-8,-2,-7,-1,-6,7,-8,8,-10,-10,-8,3,5,-4,-7,-1,5,3,6,5,3,-6,7,-10,6,5,-3,9,8,-2,10,-1,-7,-7,8,-7,-3,1,8,7,1,5,-10,5,8,4,1,4,-10,10,-4,9,1,-7,3,-2,8,2,2,8,3,9,-7,-1,-4,5,10,-5,-5,-10,8,5,-9,-4,2,-2,-3,-8,-4,7,10,7]], dtype = "int64")#candidate|5438|(1, 546)|const|int64
call_5436 = relay.TupleGetItem(func_4410_call(relay.reshape(const_5437.astype('int64'), [6, 13, 1]), relay.reshape(const_5438.astype('int64'), [6, 13, 7]), ), 0)
call_5439 = relay.TupleGetItem(func_4413_call(relay.reshape(const_5437.astype('int64'), [6, 13, 1]), relay.reshape(const_5438.astype('int64'), [6, 13, 7]), ), 0)
bop_5442 = relay.less(call_5436.astype('bool'), relay.reshape(const_5438.astype('bool'), relay.shape_of(call_5436))) # shape=(6, 13, 7)
bop_5445 = relay.less(call_5439.astype('bool'), relay.reshape(const_5438.astype('bool'), relay.shape_of(call_5439))) # shape=(6, 13, 7)
func_2857_call = mod.get_global_var('func_2857')
func_2860_call = mutated_mod.get_global_var('func_2860')
call_5478 = relay.TupleGetItem(func_2857_call(relay.reshape(call_5420.astype('float32'), [210,])), 2)
call_5479 = relay.TupleGetItem(func_2860_call(relay.reshape(call_5420.astype('float32'), [210,])), 2)
func_4024_call = mod.get_global_var('func_4024')
func_4027_call = mutated_mod.get_global_var('func_4027')
const_5504 = relay.const([9.056236,-3.074270,-6.351890,-1.921946,9.772165,-9.584583,-5.931168,4.269525,8.943468,-2.243016,-0.376010,9.314293,9.787943,3.151622,7.552968,4.163958,4.256550,-6.930490,5.207354,8.560453,6.049525,-8.007232], dtype = "float64")#candidate|5504|(22,)|const|float64
call_5503 = relay.TupleGetItem(func_4024_call(relay.reshape(const_5504.astype('float64'), [2, 1, 11])), 0)
call_5505 = relay.TupleGetItem(func_4027_call(relay.reshape(const_5504.astype('float64'), [2, 1, 11])), 0)
output = relay.Tuple([call_5417,call_5420,call_5430,const_5431,const_5437,bop_5442,call_5478,call_5503,const_5504,])
output2 = relay.Tuple([call_5418,call_5421,call_5432,const_5431,const_5437,bop_5445,call_5479,call_5505,const_5504,])
func_5506 = relay.Function([], output)
mod['func_5506'] = func_5506
mod = relay.transform.InferType()(mod)
mutated_mod['func_5506'] = func_5506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5506_call = mutated_mod.get_global_var('func_5506')
call_5507 = func_5506_call()
output = call_5507
func_5508 = relay.Function([], output)
mutated_mod['func_5508'] = func_5508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4797_call = mod.get_global_var('func_4797')
func_4798_call = mutated_mod.get_global_var('func_4798')
call_5514 = relay.TupleGetItem(func_4797_call(), 0)
call_5515 = relay.TupleGetItem(func_4798_call(), 0)
output = call_5514
output2 = call_5515
func_5536 = relay.Function([], output)
mod['func_5536'] = func_5536
mod = relay.transform.InferType()(mod)
mutated_mod['func_5536'] = func_5536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5536_call = mutated_mod.get_global_var('func_5536')
call_5537 = func_5536_call()
output = call_5537
func_5538 = relay.Function([], output)
mutated_mod['func_5538'] = func_5538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1482_call = mod.get_global_var('func_1482')
func_1484_call = mutated_mod.get_global_var('func_1484')
call_5566 = func_1482_call()
call_5567 = func_1482_call()
func_5223_call = mod.get_global_var('func_5223')
func_5224_call = mutated_mod.get_global_var('func_5224')
call_5585 = relay.TupleGetItem(func_5223_call(), 1)
call_5586 = relay.TupleGetItem(func_5224_call(), 1)
func_4924_call = mod.get_global_var('func_4924')
func_4926_call = mutated_mod.get_global_var('func_4926')
call_5590 = relay.TupleGetItem(func_4924_call(), 0)
call_5591 = relay.TupleGetItem(func_4926_call(), 0)
func_4410_call = mod.get_global_var('func_4410')
func_4413_call = mutated_mod.get_global_var('func_4413')
var_5632 = relay.var("var_5632", dtype = "int64", shape = (78,))#candidate|5632|(78,)|var|int64
var_5633 = relay.var("var_5633", dtype = "int64", shape = (546,))#candidate|5633|(546,)|var|int64
call_5631 = relay.TupleGetItem(func_4410_call(relay.reshape(var_5632.astype('int64'), [6, 13, 1]), relay.reshape(var_5633.astype('int64'), [6, 13, 7]), ), 0)
call_5634 = relay.TupleGetItem(func_4413_call(relay.reshape(var_5632.astype('int64'), [6, 13, 1]), relay.reshape(var_5633.astype('int64'), [6, 13, 7]), ), 0)
var_5635 = relay.var("var_5635", dtype = "uint32", shape = (6, 10, 13))#candidate|5635|(6, 10, 13)|var|uint32
bop_5636 = relay.power(call_5585.astype('float32'), relay.reshape(var_5635.astype('float32'), relay.shape_of(call_5585))) # shape=(6, 10, 13)
bop_5639 = relay.power(call_5586.astype('float32'), relay.reshape(var_5635.astype('float32'), relay.shape_of(call_5586))) # shape=(6, 10, 13)
output = relay.Tuple([call_5566,call_5590,call_5631,var_5632,var_5633,bop_5636,])
output2 = relay.Tuple([call_5567,call_5591,call_5634,var_5632,var_5633,bop_5639,])
func_5650 = relay.Function([var_5632,var_5633,var_5635,], output)
mod['func_5650'] = func_5650
mod = relay.transform.InferType()(mod)
var_5651 = relay.var("var_5651", dtype = "int64", shape = (78,))#candidate|5651|(78,)|var|int64
var_5652 = relay.var("var_5652", dtype = "int64", shape = (546,))#candidate|5652|(546,)|var|int64
var_5653 = relay.var("var_5653", dtype = "uint32", shape = (6, 10, 13))#candidate|5653|(6, 10, 13)|var|uint32
output = func_5650(var_5651,var_5652,var_5653,)
func_5654 = relay.Function([var_5651,var_5652,var_5653,], output)
mutated_mod['func_5654'] = func_5654
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5662 = relay.const([[[0.153640],[-4.399469],[3.165344],[-3.903714],[8.609877],[5.611259],[-5.728393],[0.050857],[-1.599838],[0.910955],[3.166261],[7.437989],[-2.177192]],[[2.524293],[-0.700270],[-7.988308],[-5.689821],[-0.330652],[7.409072],[-6.084627],[-1.439934],[-0.664436],[3.756896],[-5.221382],[-6.335170],[-4.064855]],[[9.314673],[-2.079216],[-6.634802],[6.380494],[9.142509],[-1.756932],[-5.154531],[5.160261],[4.202432],[-2.783755],[6.107223],[5.798816],[-5.461959]],[[-5.047867],[0.590241],[-2.115416],[-0.052396],[-4.233575],[-4.736240],[-2.405156],[8.703937],[4.642643],[1.905099],[4.358059],[-8.673908],[1.077769]],[[-7.262415],[-5.830324],[-6.145469],[-0.914901],[-1.288201],[-1.169991],[2.838339],[0.162402],[-4.108966],[5.264571],[8.260793],[2.840606],[-8.758442]],[[5.362836],[-6.689209],[-5.940985],[2.149978],[7.837899],[-2.623267],[2.889439],[4.027807],[0.585540],[-9.839152],[-0.331814],[-0.822256],[1.271617]],[[8.982634],[2.825008],[2.766498],[-8.829324],[4.916824],[9.199836],[-6.839167],[-3.503526],[-8.330431],[6.915319],[4.805052],[-1.659671],[7.888265]],[[-7.471772],[6.360419],[3.589751],[-5.925603],[-4.597896],[-2.759926],[4.819362],[0.700613],[-3.608611],[2.907488],[-5.707305],[3.500829],[3.875710]],[[9.667092],[-1.486141],[8.757165],[-1.196793],[-2.856412],[2.881139],[-7.108679],[0.087767],[-8.240866],[-4.610764],[5.910752],[8.314929],[0.390525]],[[-3.360216],[7.682418],[3.101903],[4.783639],[-7.851234],[-3.804738],[1.511410],[-9.143743],[6.895974],[-5.737202],[7.071307],[0.240859],[0.904826]],[[7.613078],[-2.185803],[-4.546331],[3.249222],[-8.149629],[-1.969614],[-3.445805],[-5.459342],[-5.309565],[-4.231445],[-1.754363],[7.618768],[-7.867744]],[[-8.057121],[6.519988],[-8.077426],[-1.497313],[2.645022],[9.803524],[8.348076],[-6.682481],[1.956796],[-3.978397],[0.819538],[-4.990691],[8.961286]],[[-9.955297],[9.063107],[-8.576402],[-9.745571],[1.745783],[-6.566698],[9.249347],[6.471455],[-3.500675],[9.895852],[-1.182184],[8.007778],[-8.335404]]], dtype = "float32")#candidate|5662|(13, 13, 1)|const|float32
var_5663 = relay.var("var_5663", dtype = "float32", shape = (13, 13, 15))#candidate|5663|(13, 13, 15)|var|float32
bop_5664 = relay.divide(const_5662.astype('float32'), var_5663.astype('float32')) # shape=(13, 13, 15)
var_5671 = relay.var("var_5671", dtype = "float32", shape = (13, 13, 15))#candidate|5671|(13, 13, 15)|var|float32
bop_5672 = relay.floor_divide(bop_5664.astype('float64'), relay.reshape(var_5671.astype('float64'), relay.shape_of(bop_5664))) # shape=(13, 13, 15)
bop_5675 = relay.floor_mod(bop_5672.astype('float32'), relay.reshape(var_5663.astype('float32'), relay.shape_of(bop_5672))) # shape=(13, 13, 15)
bop_5678 = relay.bitwise_and(bop_5672.astype('int32'), relay.reshape(bop_5664.astype('int32'), relay.shape_of(bop_5672))) # shape=(13, 13, 15)
output = relay.Tuple([bop_5675,bop_5678,])
output2 = relay.Tuple([bop_5675,bop_5678,])
func_5683 = relay.Function([var_5663,var_5671,], output)
mod['func_5683'] = func_5683
mod = relay.transform.InferType()(mod)
var_5684 = relay.var("var_5684", dtype = "float32", shape = (13, 13, 15))#candidate|5684|(13, 13, 15)|var|float32
var_5685 = relay.var("var_5685", dtype = "float32", shape = (13, 13, 15))#candidate|5685|(13, 13, 15)|var|float32
output = func_5683(var_5684,var_5685,)
func_5686 = relay.Function([var_5684,var_5685,], output)
mutated_mod['func_5686'] = func_5686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_641_call = mod.get_global_var('func_641')
func_643_call = mutated_mod.get_global_var('func_643')
call_5713 = relay.TupleGetItem(func_641_call(), 0)
call_5714 = relay.TupleGetItem(func_643_call(), 0)
func_4306_call = mod.get_global_var('func_4306')
func_4310_call = mutated_mod.get_global_var('func_4310')
var_5737 = relay.var("var_5737", dtype = "float32", shape = (7, 70))#candidate|5737|(7, 70)|var|float32
call_5736 = relay.TupleGetItem(func_4306_call(relay.reshape(var_5737.astype('float32'), [490,]), relay.reshape(call_5713.astype('int64'), [9, 12, 15]), ), 5)
call_5738 = relay.TupleGetItem(func_4310_call(relay.reshape(var_5737.astype('float32'), [490,]), relay.reshape(call_5713.astype('int64'), [9, 12, 15]), ), 5)
uop_5745 = relay.sinh(var_5737.astype('float32')) # shape=(7, 70)
output = relay.Tuple([call_5713,call_5736,uop_5745,])
output2 = relay.Tuple([call_5714,call_5738,uop_5745,])
func_5750 = relay.Function([var_5737,], output)
mod['func_5750'] = func_5750
mod = relay.transform.InferType()(mod)
var_5751 = relay.var("var_5751", dtype = "float32", shape = (7, 70))#candidate|5751|(7, 70)|var|float32
output = func_5750(var_5751)
func_5752 = relay.Function([var_5751], output)
mutated_mod['func_5752'] = func_5752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2551_call = mod.get_global_var('func_2551')
func_2553_call = mutated_mod.get_global_var('func_2553')
call_5764 = relay.TupleGetItem(func_2551_call(), 0)
call_5765 = relay.TupleGetItem(func_2553_call(), 0)
output = relay.Tuple([call_5764,])
output2 = relay.Tuple([call_5765,])
func_5772 = relay.Function([], output)
mod['func_5772'] = func_5772
mod = relay.transform.InferType()(mod)
mutated_mod['func_5772'] = func_5772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5772_call = mutated_mod.get_global_var('func_5772')
call_5773 = func_5772_call()
output = call_5773
func_5774 = relay.Function([], output)
mutated_mod['func_5774'] = func_5774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5843 = relay.var("var_5843", dtype = "int16", shape = (6, 11, 8))#candidate|5843|(6, 11, 8)|var|int16
var_5844 = relay.var("var_5844", dtype = "int16", shape = (6, 11, 8))#candidate|5844|(6, 11, 8)|var|int16
bop_5845 = relay.add(var_5843.astype('int16'), relay.reshape(var_5844.astype('int16'), relay.shape_of(var_5843))) # shape=(6, 11, 8)
uop_5850 = relay.erf(bop_5845.astype('float64')) # shape=(6, 11, 8)
var_5854 = relay.var("var_5854", dtype = "float64", shape = (6, 11, 8))#candidate|5854|(6, 11, 8)|var|float64
bop_5855 = relay.minimum(uop_5850.astype('float32'), relay.reshape(var_5854.astype('float32'), relay.shape_of(uop_5850))) # shape=(6, 11, 8)
output = bop_5855
output2 = bop_5855
func_5863 = relay.Function([var_5843,var_5844,var_5854,], output)
mod['func_5863'] = func_5863
mod = relay.transform.InferType()(mod)
mutated_mod['func_5863'] = func_5863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5863_call = mutated_mod.get_global_var('func_5863')
var_5865 = relay.var("var_5865", dtype = "int16", shape = (6, 11, 8))#candidate|5865|(6, 11, 8)|var|int16
var_5866 = relay.var("var_5866", dtype = "int16", shape = (6, 11, 8))#candidate|5866|(6, 11, 8)|var|int16
var_5867 = relay.var("var_5867", dtype = "float64", shape = (6, 11, 8))#candidate|5867|(6, 11, 8)|var|float64
call_5864 = func_5863_call(var_5865,var_5866,var_5867,)
output = call_5864
func_5868 = relay.Function([var_5865,var_5866,var_5867,], output)
mutated_mod['func_5868'] = func_5868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mod.get_global_var('func_1454')
func_1455_call = mutated_mod.get_global_var('func_1455')
call_5902 = relay.TupleGetItem(func_1454_call(), 0)
call_5903 = relay.TupleGetItem(func_1455_call(), 0)
output = relay.Tuple([call_5902,])
output2 = relay.Tuple([call_5903,])
func_5924 = relay.Function([], output)
mod['func_5924'] = func_5924
mod = relay.transform.InferType()(mod)
output = func_5924()
func_5925 = relay.Function([], output)
mutated_mod['func_5925'] = func_5925
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5991 = relay.var("var_5991", dtype = "float64", shape = (14, 1, 4))#candidate|5991|(14, 1, 4)|var|float64
uop_5992 = relay.log10(var_5991.astype('float64')) # shape=(14, 1, 4)
func_2881_call = mod.get_global_var('func_2881')
func_2883_call = mutated_mod.get_global_var('func_2883')
call_5994 = func_2881_call()
call_5995 = func_2881_call()
output = relay.Tuple([uop_5992,call_5994,])
output2 = relay.Tuple([uop_5992,call_5995,])
func_6004 = relay.Function([var_5991,], output)
mod['func_6004'] = func_6004
mod = relay.transform.InferType()(mod)
var_6005 = relay.var("var_6005", dtype = "float64", shape = (14, 1, 4))#candidate|6005|(14, 1, 4)|var|float64
output = func_6004(var_6005)
func_6006 = relay.Function([var_6005], output)
mutated_mod['func_6006'] = func_6006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mod.get_global_var('func_723')
func_725_call = mutated_mod.get_global_var('func_725')
call_6048 = relay.TupleGetItem(func_723_call(), 0)
call_6049 = relay.TupleGetItem(func_725_call(), 0)
func_5223_call = mod.get_global_var('func_5223')
func_5224_call = mutated_mod.get_global_var('func_5224')
call_6050 = relay.TupleGetItem(func_5223_call(), 0)
call_6051 = relay.TupleGetItem(func_5224_call(), 0)
output = relay.Tuple([call_6048,call_6050,])
output2 = relay.Tuple([call_6049,call_6051,])
func_6074 = relay.Function([], output)
mod['func_6074'] = func_6074
mod = relay.transform.InferType()(mod)
output = func_6074()
func_6075 = relay.Function([], output)
mutated_mod['func_6075'] = func_6075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5223_call = mod.get_global_var('func_5223')
func_5224_call = mutated_mod.get_global_var('func_5224')
call_6087 = relay.TupleGetItem(func_5223_call(), 2)
call_6088 = relay.TupleGetItem(func_5224_call(), 2)
func_2857_call = mod.get_global_var('func_2857')
func_2860_call = mutated_mod.get_global_var('func_2860')
var_6093 = relay.var("var_6093", dtype = "float32", shape = (210,))#candidate|6093|(210,)|var|float32
call_6092 = relay.TupleGetItem(func_2857_call(relay.reshape(var_6093.astype('float32'), [210,])), 0)
call_6094 = relay.TupleGetItem(func_2860_call(relay.reshape(var_6093.astype('float32'), [210,])), 0)
output = relay.Tuple([call_6087,call_6092,var_6093,])
output2 = relay.Tuple([call_6088,call_6094,var_6093,])
func_6099 = relay.Function([var_6093,], output)
mod['func_6099'] = func_6099
mod = relay.transform.InferType()(mod)
var_6100 = relay.var("var_6100", dtype = "float32", shape = (210,))#candidate|6100|(210,)|var|float32
output = func_6099(var_6100)
func_6101 = relay.Function([var_6100], output)
mutated_mod['func_6101'] = func_6101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mod.get_global_var('func_1454')
func_1455_call = mutated_mod.get_global_var('func_1455')
call_6128 = relay.TupleGetItem(func_1454_call(), 0)
call_6129 = relay.TupleGetItem(func_1455_call(), 0)
output = call_6128
output2 = call_6129
func_6161 = relay.Function([], output)
mod['func_6161'] = func_6161
mod = relay.transform.InferType()(mod)
output = func_6161()
func_6162 = relay.Function([], output)
mutated_mod['func_6162'] = func_6162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3549_call = mod.get_global_var('func_3549')
func_3550_call = mutated_mod.get_global_var('func_3550')
call_6206 = relay.TupleGetItem(func_3549_call(), 0)
call_6207 = relay.TupleGetItem(func_3550_call(), 0)
output = call_6206
output2 = call_6207
func_6232 = relay.Function([], output)
mod['func_6232'] = func_6232
mod = relay.transform.InferType()(mod)
mutated_mod['func_6232'] = func_6232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6232_call = mutated_mod.get_global_var('func_6232')
call_6233 = func_6232_call()
output = call_6233
func_6234 = relay.Function([], output)
mutated_mod['func_6234'] = func_6234
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6238 = relay.const([[[2.802704,5.145533,-5.521316,7.690582],[1.052880,-3.843359,-9.875164,0.952541],[-9.701869,7.220276,6.914386,8.118546],[-7.282073,-3.612913,7.773045,-6.113699],[0.306461,0.272476,-8.008199,-9.628478],[-4.608826,-6.962984,-4.826152,-3.238974],[-9.788226,-8.203038,2.619570,9.506242],[3.726521,-0.135647,6.161918,9.566256],[-7.893328,-4.618632,6.706517,5.255239],[3.141818,-7.106023,9.761264,4.392272],[8.990131,6.928811,4.434134,-9.116783],[-2.813547,1.934724,-6.374449,-0.467594],[3.342330,2.782869,-5.266136,-5.473031],[-0.686006,7.723544,0.032294,-8.611701]],[[-6.134997,-1.939342,-1.325280,6.150368],[6.412799,-8.550329,2.844949,3.902560],[-7.389006,-6.204763,0.740774,-1.443506],[4.289678,0.386045,-0.535717,3.769346],[3.790731,-4.568821,3.738304,8.906765],[9.600597,-8.325080,-8.215144,6.557516],[-8.959241,1.855088,5.894721,-1.704031],[6.584383,9.019018,6.933110,3.683668],[-6.824417,-3.780780,7.729536,2.340042],[1.697576,2.665724,5.665911,-7.236700],[-7.557489,6.550035,-3.891461,2.882460],[6.465960,5.227795,8.493236,8.050231],[9.764020,5.276424,4.581940,5.126521],[-5.995023,2.334638,8.728062,-1.695432]],[[2.213406,1.666972,9.564587,-0.404113],[-4.675934,7.988274,-0.697534,8.056492],[-6.037968,-2.581869,5.094774,-8.243860],[-2.800568,1.664805,-3.836609,-7.238814],[9.883569,7.016538,-3.820745,8.496172],[2.970089,-7.893165,-4.077462,1.767574],[0.022057,-3.493176,3.678122,-2.687149],[-8.917788,-3.865959,0.644168,1.846908],[-5.305245,2.752138,-5.394026,5.751978],[2.332007,4.878811,-1.657548,-4.792500],[-1.159615,-2.017591,-6.010185,0.886200],[7.485159,9.376992,-6.526680,9.958506],[1.488795,0.065527,-7.507341,7.837238],[2.322715,7.076773,-8.912396,5.140186]],[[-5.674525,-9.328457,-4.887384,-5.460831],[3.769010,2.183166,-0.937984,1.129933],[4.079393,0.762318,3.495822,-5.308263],[2.231281,-8.182373,8.843291,-0.643796],[-6.906173,-0.910996,-7.506763,-1.650095],[-3.558916,-1.844886,-0.615093,-7.294499],[-1.665153,0.186430,2.185551,-6.556266],[4.726932,-6.193162,-5.342188,0.515055],[0.942563,-4.214777,-2.745818,-7.460988],[-9.570846,4.895123,-6.776600,-9.066179],[6.381880,-8.362335,1.948622,0.933589],[-8.747924,-5.764777,-0.610183,0.577470],[4.559450,3.779257,-5.338692,5.576444],[-6.703930,2.882516,-9.064418,-3.564216]],[[-2.822424,-1.358527,6.136224,-8.647148],[3.048079,3.426612,-0.807789,-0.363981],[-4.947658,5.514330,1.183910,3.292884],[9.791330,-5.736936,-3.284752,5.795532],[8.975219,2.830361,5.835078,-7.785061],[-9.505593,-5.505041,-3.057067,-5.316038],[5.110843,7.798448,-1.678369,-8.100866],[-8.632367,-1.445002,2.804358,8.551232],[8.251619,-5.651413,-1.119254,-5.594453],[-2.924401,-2.375023,1.360945,5.035684],[-6.898395,3.247604,3.661479,5.466433],[-3.309847,-4.447843,1.353117,-0.711673],[-8.295197,-6.962227,-8.537705,4.873005],[7.199263,9.047459,0.028497,4.294865]],[[-4.874315,-7.544054,7.542509,3.456444],[3.355673,1.177511,0.806904,-8.830051],[-4.113159,-6.059937,7.888325,4.301881],[4.477034,1.225473,5.468569,8.802243],[0.133077,1.117904,4.654513,-7.205875],[4.066319,6.668644,9.321060,-9.067626],[-5.408712,-0.411140,7.834043,8.599417],[7.464015,6.475518,6.893742,-1.766059],[-2.879930,1.836108,-2.394282,6.562763],[-6.737849,-3.905277,-4.469066,1.792320],[7.418977,-9.735160,-6.618785,-0.745727],[-1.173797,-3.511100,-0.558792,-8.338330],[0.244074,-8.877521,6.783065,9.872598],[-2.891102,3.609528,-3.813669,-3.049462]],[[2.257217,-2.889632,-1.252561,5.456007],[-4.748416,-6.081295,-0.323714,-0.212738],[7.201460,5.427518,-4.153707,-1.317096],[-4.647763,1.123242,-1.218925,-8.711726],[-8.192888,3.850749,2.007256,1.775711],[9.737958,-8.519187,-4.176209,0.714511],[9.636756,-9.993618,5.133514,3.302741],[-5.942033,-7.946238,-6.835644,-1.875627],[-3.930665,2.951563,-0.958087,6.613201],[-8.479195,9.202351,-8.635805,-4.250189],[9.649562,2.010435,9.624394,-1.836281],[1.719056,8.332450,-6.501785,-6.633876],[4.330843,-7.031701,-6.716209,7.313378],[-4.412695,6.341100,1.324700,-2.247193]],[[-8.122997,0.017400,-0.567367,-5.293621],[1.708165,0.853851,5.448280,-1.791939],[2.876775,8.930010,-0.676621,8.573601],[7.396696,-3.445175,-8.505498,-2.484766],[-3.412228,7.950774,7.709266,1.833511],[2.473622,-2.326332,-9.378779,8.988309],[-3.358349,-6.878024,-1.762355,3.905819],[-0.249932,-0.219936,-3.375329,-5.043241],[0.949499,-6.333179,2.587480,2.598716],[-9.426141,7.399058,-1.297610,1.736920],[3.545492,4.951430,0.762355,-9.318011],[-9.803811,-1.723921,5.424336,-7.812503],[-4.905802,0.084209,-3.702384,-7.142293],[7.782894,4.224110,3.095214,-1.826125]],[[-2.574471,-7.454712,-0.472089,-4.677994],[6.521214,9.275529,7.661916,5.277972],[-1.128674,5.115208,5.075816,-2.673176],[5.621260,-0.708311,-3.648535,-2.928548],[9.775588,-9.040942,1.961843,-6.785301],[7.785566,9.339793,6.951120,5.391545],[1.643884,-6.988247,-9.500605,2.110162],[9.579221,-5.913251,-1.899237,-1.993983],[6.768558,9.271059,9.725529,-2.373070],[-3.684141,6.011762,-9.492160,7.989744],[2.052719,1.586799,-0.195147,-5.604038],[-4.600694,8.754277,8.336707,-7.948315],[-7.287187,9.551065,-5.456139,9.145778],[5.006873,-4.814786,6.925854,8.934251]]], dtype = "float64")#candidate|6238|(9, 14, 4)|const|float64
var_6239 = relay.var("var_6239", dtype = "float64", shape = (9, 14, 4))#candidate|6239|(9, 14, 4)|var|float64
bop_6240 = relay.add(const_6238.astype('float64'), relay.reshape(var_6239.astype('float64'), relay.shape_of(const_6238))) # shape=(9, 14, 4)
uop_6245 = relay.cosh(var_6239.astype('float32')) # shape=(9, 14, 4)
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
const_6252 = relay.const(False, dtype = "bool")#candidate|6252|()|const|bool
call_6251 = relay.TupleGetItem(func_408_call(relay.reshape(const_6252.astype('bool'), [])), 5)
call_6253 = relay.TupleGetItem(func_411_call(relay.reshape(const_6252.astype('bool'), [])), 5)
output = relay.Tuple([bop_6240,uop_6245,call_6251,const_6252,])
output2 = relay.Tuple([bop_6240,uop_6245,call_6253,const_6252,])
func_6267 = relay.Function([var_6239,], output)
mod['func_6267'] = func_6267
mod = relay.transform.InferType()(mod)
mutated_mod['func_6267'] = func_6267
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6268 = relay.var("var_6268", dtype = "float64", shape = (9, 14, 4))#candidate|6268|(9, 14, 4)|var|float64
func_6267_call = mutated_mod.get_global_var('func_6267')
call_6269 = func_6267_call(var_6268)
output = call_6269
func_6270 = relay.Function([var_6268], output)
mutated_mod['func_6270'] = func_6270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3061_call = mutated_mod.get_global_var('func_3061')
call_6288 = relay.TupleGetItem(func_3060_call(), 0)
call_6289 = relay.TupleGetItem(func_3061_call(), 0)
output = relay.Tuple([call_6288,])
output2 = relay.Tuple([call_6289,])
func_6296 = relay.Function([], output)
mod['func_6296'] = func_6296
mod = relay.transform.InferType()(mod)
mutated_mod['func_6296'] = func_6296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6296_call = mutated_mod.get_global_var('func_6296')
call_6297 = func_6296_call()
output = call_6297
func_6298 = relay.Function([], output)
mutated_mod['func_6298'] = func_6298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5536_call = mod.get_global_var('func_5536')
func_5538_call = mutated_mod.get_global_var('func_5538')
call_6321 = func_5536_call()
call_6322 = func_5536_call()
output = relay.Tuple([call_6321,])
output2 = relay.Tuple([call_6322,])
func_6325 = relay.Function([], output)
mod['func_6325'] = func_6325
mod = relay.transform.InferType()(mod)
mutated_mod['func_6325'] = func_6325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6325_call = mutated_mod.get_global_var('func_6325')
call_6326 = func_6325_call()
output = call_6326
func_6327 = relay.Function([], output)
mutated_mod['func_6327'] = func_6327
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6340 = relay.var("var_6340", dtype = "float32", shape = (15, 12))#candidate|6340|(15, 12)|var|float32
uop_6341 = relay.sin(var_6340.astype('float32')) # shape=(15, 12)
func_2672_call = mod.get_global_var('func_2672')
func_2673_call = mutated_mod.get_global_var('func_2673')
call_6356 = relay.TupleGetItem(func_2672_call(), 0)
call_6357 = relay.TupleGetItem(func_2673_call(), 0)
func_2128_call = mod.get_global_var('func_2128')
func_2129_call = mutated_mod.get_global_var('func_2129')
call_6373 = relay.TupleGetItem(func_2128_call(), 0)
call_6374 = relay.TupleGetItem(func_2129_call(), 0)
output = relay.Tuple([uop_6341,call_6356,call_6373,])
output2 = relay.Tuple([uop_6341,call_6357,call_6374,])
func_6379 = relay.Function([var_6340,], output)
mod['func_6379'] = func_6379
mod = relay.transform.InferType()(mod)
mutated_mod['func_6379'] = func_6379
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6380 = relay.var("var_6380", dtype = "float32", shape = (15, 12))#candidate|6380|(15, 12)|var|float32
func_6379_call = mutated_mod.get_global_var('func_6379')
call_6381 = func_6379_call(var_6380)
output = call_6381
func_6382 = relay.Function([var_6380], output)
mutated_mod['func_6382'] = func_6382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2343_call = mod.get_global_var('func_2343')
func_2345_call = mutated_mod.get_global_var('func_2345')
call_6395 = relay.TupleGetItem(func_2343_call(), 0)
call_6396 = relay.TupleGetItem(func_2345_call(), 0)
output = relay.Tuple([call_6395,])
output2 = relay.Tuple([call_6396,])
func_6403 = relay.Function([], output)
mod['func_6403'] = func_6403
mod = relay.transform.InferType()(mod)
mutated_mod['func_6403'] = func_6403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6403_call = mutated_mod.get_global_var('func_6403')
call_6404 = func_6403_call()
output = call_6404
func_6405 = relay.Function([], output)
mutated_mod['func_6405'] = func_6405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6406 = relay.var("var_6406", dtype = "float64", shape = (4, 8, 6))#candidate|6406|(4, 8, 6)|var|float64
uop_6407 = relay.cosh(var_6406.astype('float64')) # shape=(4, 8, 6)
func_2256_call = mod.get_global_var('func_2256')
func_2258_call = mutated_mod.get_global_var('func_2258')
const_6422 = relay.const(True, dtype = "bool")#candidate|6422|()|const|bool
call_6421 = relay.TupleGetItem(func_2256_call(relay.reshape(const_6422.astype('bool'), [])), 2)
call_6423 = relay.TupleGetItem(func_2258_call(relay.reshape(const_6422.astype('bool'), [])), 2)
bop_6426 = relay.not_equal(uop_6407.astype('bool'), relay.reshape(var_6406.astype('bool'), relay.shape_of(uop_6407))) # shape=(4, 8, 6)
output = relay.Tuple([call_6421,const_6422,bop_6426,])
output2 = relay.Tuple([call_6423,const_6422,bop_6426,])
func_6431 = relay.Function([var_6406,], output)
mod['func_6431'] = func_6431
mod = relay.transform.InferType()(mod)
mutated_mod['func_6431'] = func_6431
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6432 = relay.var("var_6432", dtype = "float64", shape = (4, 8, 6))#candidate|6432|(4, 8, 6)|var|float64
func_6431_call = mutated_mod.get_global_var('func_6431')
call_6433 = func_6431_call(var_6432)
output = call_6433
func_6434 = relay.Function([var_6432], output)
mutated_mod['func_6434'] = func_6434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_325_call = mod.get_global_var('func_325')
func_326_call = mutated_mod.get_global_var('func_326')
call_6448 = func_325_call()
call_6449 = func_325_call()
output = call_6448
output2 = call_6449
func_6462 = relay.Function([], output)
mod['func_6462'] = func_6462
mod = relay.transform.InferType()(mod)
mutated_mod['func_6462'] = func_6462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6462_call = mutated_mod.get_global_var('func_6462')
call_6463 = func_6462_call()
output = call_6463
func_6464 = relay.Function([], output)
mutated_mod['func_6464'] = func_6464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mod.get_global_var('func_1454')
func_1455_call = mutated_mod.get_global_var('func_1455')
call_6498 = relay.TupleGetItem(func_1454_call(), 0)
call_6499 = relay.TupleGetItem(func_1455_call(), 0)
output = relay.Tuple([call_6498,])
output2 = relay.Tuple([call_6499,])
func_6509 = relay.Function([], output)
mod['func_6509'] = func_6509
mod = relay.transform.InferType()(mod)
mutated_mod['func_6509'] = func_6509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6509_call = mutated_mod.get_global_var('func_6509')
call_6510 = func_6509_call()
output = call_6510
func_6511 = relay.Function([], output)
mutated_mod['func_6511'] = func_6511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_641_call = mod.get_global_var('func_641')
func_643_call = mutated_mod.get_global_var('func_643')
call_6539 = relay.TupleGetItem(func_641_call(), 2)
call_6540 = relay.TupleGetItem(func_643_call(), 2)
func_4350_call = mod.get_global_var('func_4350')
func_4351_call = mutated_mod.get_global_var('func_4351')
call_6553 = relay.TupleGetItem(func_4350_call(), 0)
call_6554 = relay.TupleGetItem(func_4351_call(), 0)
output = relay.Tuple([call_6539,call_6553,])
output2 = relay.Tuple([call_6540,call_6554,])
func_6557 = relay.Function([], output)
mod['func_6557'] = func_6557
mod = relay.transform.InferType()(mod)
mutated_mod['func_6557'] = func_6557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6557_call = mutated_mod.get_global_var('func_6557')
call_6558 = func_6557_call()
output = call_6558
func_6559 = relay.Function([], output)
mutated_mod['func_6559'] = func_6559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5000_call = mod.get_global_var('func_5000')
func_5001_call = mutated_mod.get_global_var('func_5001')
call_6565 = relay.TupleGetItem(func_5000_call(), 1)
call_6566 = relay.TupleGetItem(func_5001_call(), 1)
uop_6573 = relay.log10(call_6565.astype('float64')) # shape=(9, 12, 15)
uop_6575 = relay.log10(call_6566.astype('float64')) # shape=(9, 12, 15)
output = relay.Tuple([uop_6573,])
output2 = relay.Tuple([uop_6575,])
func_6579 = relay.Function([], output)
mod['func_6579'] = func_6579
mod = relay.transform.InferType()(mod)
mutated_mod['func_6579'] = func_6579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6579_call = mutated_mod.get_global_var('func_6579')
call_6580 = func_6579_call()
output = call_6580
func_6581 = relay.Function([], output)
mutated_mod['func_6581'] = func_6581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3061_call = mutated_mod.get_global_var('func_3061')
call_6600 = relay.TupleGetItem(func_3060_call(), 0)
call_6601 = relay.TupleGetItem(func_3061_call(), 0)
func_2857_call = mod.get_global_var('func_2857')
func_2860_call = mutated_mod.get_global_var('func_2860')
const_6604 = relay.const([8.303577,-8.973040,2.429280,-2.591121,7.704959,-0.613830,-8.084993,-1.804895,5.395297,1.854999,5.357344,-0.363580,0.282466,0.290051,-9.941038,-4.014945,3.622504,-4.928785,-8.952273,7.808623,2.095515,3.628919,5.504790,1.302664,0.265367,2.988409,-9.852884,-1.636375,-5.038105,-8.686986,-7.901432,-2.108807,0.270835,-3.256275,6.098498,-7.094249,-1.731137,-6.161150,4.812665,-9.726976,-0.067033,8.246792,1.542977,0.391795,5.225401,-0.281153,-4.133789,9.923657,-6.627781,0.918114,7.802298,-8.081889,8.836036,-2.727251,-8.387851,-2.744696,-5.149472,5.943102,6.206026,8.044398,-6.655286,-7.325347,-6.189321,6.474936,-1.256838,1.221075,-0.196813,0.780327,-7.671523,-0.366665,-2.158077,-8.594934,-2.910169,0.153605,-1.450289,-3.881227,-9.792277,6.750735,-3.787940,1.197327,2.748424,-2.679677,-0.891854,-9.325285,7.844434,-3.024375,8.126293,6.111147,-0.277408,2.679211,3.532366,-9.175093,-7.733832,8.841948,-7.197331,7.253879,9.164595,0.176406,8.558639,-2.334114,-9.784485,9.814851,3.320578,3.195487,1.079561,-2.023316,-0.390415,-6.880908,-7.080930,1.377438,6.213948,9.746015,-8.357146,-2.076582,-6.556216,4.518693,5.249128,-6.643884,3.760237,0.595962,-1.717064,7.236571,-8.720545,7.215308,1.642499,6.021588,-5.777834,3.429297,2.499214,-6.358145,4.415845,-6.426893,-4.121128,1.391272,-6.232165,-4.861298,0.391966,8.736785,-7.402547,-9.958918,7.125727,-9.773044,-3.001012,-3.617350,5.399668,6.339119,-1.271010,-7.567817,-7.862030,-5.990899,-9.265664,6.811083,2.915173,4.253847,-9.278359,7.022579,6.346221,6.668107,-8.102828,6.763428,-9.232117,-9.954456,-5.101946,-5.907487,-4.942648,4.668220,7.089704,-1.898187,7.406708,-7.123014,-2.526123,6.181995,4.782760,7.246636,-4.641783,-6.068663,-2.261768,-3.989673,2.667411,4.425951,9.192912,-7.185170,-7.410404,2.789993,-9.368195,6.028853,-2.615803,-8.115512,8.415373,2.711860,-3.692078,-1.799153,-2.420262,4.942000,8.573638,7.476894,5.636853,-4.624170,6.980803,8.397924,4.386173,-9.824559,7.197223,-6.786144,-3.482895,-8.982823,1.774106,9.745823,0.872031,6.881902], dtype = "float32")#candidate|6604|(210,)|const|float32
call_6603 = relay.TupleGetItem(func_2857_call(relay.reshape(const_6604.astype('float32'), [210,])), 0)
call_6605 = relay.TupleGetItem(func_2860_call(relay.reshape(const_6604.astype('float32'), [210,])), 0)
output = relay.Tuple([call_6600,call_6603,const_6604,])
output2 = relay.Tuple([call_6601,call_6605,const_6604,])
func_6609 = relay.Function([], output)
mod['func_6609'] = func_6609
mod = relay.transform.InferType()(mod)
output = func_6609()
func_6610 = relay.Function([], output)
mutated_mod['func_6610'] = func_6610
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6697 = relay.var("var_6697", dtype = "float32", shape = (2, 15, 7))#candidate|6697|(2, 15, 7)|var|float32
uop_6698 = relay.atan(var_6697.astype('float32')) # shape=(2, 15, 7)
uop_6702 = relay.sinh(uop_6698.astype('float32')) # shape=(2, 15, 7)
func_6267_call = mod.get_global_var('func_6267')
func_6270_call = mutated_mod.get_global_var('func_6270')
const_6705 = relay.const([-7.251767,6.589561,-5.950401,9.630345,-4.854988,-1.484064,-6.108197,3.482355,1.104792,-5.370808,-2.614124,4.661127,0.614799,6.023393,0.741362,2.773166,5.758150,4.817928,0.695639,-7.464499,-9.822710,-7.804321,7.101243,-5.590996,-4.920975,-4.715922,0.317833,8.020141,7.220006,1.405826,-5.267835,-7.895907,8.584000,1.574428,3.758011,-8.201977,3.358461,-7.978741,-9.093656,1.790075,4.956604,3.348600,0.534014,6.848190,-3.100357,-9.941792,-5.885818,-7.812320,-7.238109,-1.326911,-3.487596,-2.367114,-4.062858,-8.751615,6.392194,6.271735,0.452318,1.269804,-4.785630,-0.516754,3.729173,9.261201,1.880057,4.305003,8.985654,4.895970,6.844326,5.715553,-7.104760,-8.161361,-0.247857,-6.508606,6.642053,-5.367913,0.688818,-2.506028,4.503020,-7.187380,3.503516,1.722153,9.389064,-1.326333,-9.250402,-6.344355,-5.845020,-3.312568,6.295291,-3.539097,8.039992,-6.967143,4.427177,2.169040,-1.066645,-1.103108,-6.280480,-9.857626,-6.301659,-0.661376,3.582715,-4.867298,5.362794,-1.274451,3.361584,2.163948,7.998838,2.878482,-8.932953,-0.598968,-0.476835,0.849643,-2.979836,3.533196,-9.092911,3.538072,-0.237789,7.568947,-3.921228,-3.273476,3.872392,-1.087553,8.420079,1.588816,8.299465,-4.153761,-3.089444,-9.835188,-1.160399,-9.747818,6.762504,-7.958155,0.567927,1.102423,1.736819,5.387550,-0.438662,1.123441,-9.261204,4.347264,-4.678794,0.779805,1.551944,5.752182,7.023532,9.700195,4.021007,5.053165,2.651269,9.428734,-6.886100,2.162721,-9.014366,2.738525,-8.879058,-3.313616,-7.597616,6.912314,0.914921,8.490263,-2.958557,5.042910,-9.380304,-9.813013,-4.540589,-9.981246,0.042668,6.155297,2.597027,-1.711325,9.417475,-7.723649,-6.147729,-7.261893,6.080278,2.227486,-1.176445,8.440023,2.933761,-5.371756,5.471878,-7.414786,2.273268,0.240067,-0.178147,-1.206799,-7.136436,-2.561845,-7.761399,9.619066,-5.079811,-4.168665,3.722965,-5.641315,1.179765,-9.364117,6.517354,9.306717,-2.235847,5.957648,-3.824122,9.590322,7.870850,-7.208577,-6.337884,1.634309,-8.056968,1.676790,1.624578,-1.054287,-1.333806,-7.273863,1.062160,-9.178576,-4.275327,5.271484,7.485915,9.004930,-5.224024,8.185925,0.773497,4.609946,-5.064698,-6.792992,-4.629981,-9.149768,5.569675,9.679793,4.578243,1.838666,4.825462,-9.940536,0.162453,3.971115,1.127715,-5.847354,0.869460,-1.036780,-0.110984,-8.395210,6.020616,4.407054,8.051027,-3.739911,1.927208,-6.019645,-1.154493,4.075151,-7.246442,2.066911,3.548102,7.646177,7.774776,-8.018886,-1.893556,8.404615,-4.355251,-3.452839,3.871442,-6.757506,-3.879552,7.646862,0.372739,-6.158826,-2.879243,-0.478983,3.245456,-4.332723,2.832667,-4.702081,0.509613,-0.097315,7.763787,4.529509,9.076011,8.437141,-4.038487,-8.367801,9.979426,-9.381673,-9.035918,-1.512276,-7.097714,-5.837084,3.046966,5.924029,-4.338866,-8.881241,-1.450920,-0.209565,0.950480,-5.785516,3.643020,-4.461841,4.558221,-3.917639,8.174816,-9.696861,8.170454,8.056673,2.857600,-2.213542,-9.585831,1.181778,-5.205057,-7.190351,5.236191,-3.006282,2.241651,-7.959999,4.543185,-7.543000,5.233454,-8.450293,-5.778735,2.857754,-2.329012,6.357720,7.648128,4.942137,8.949111,3.234673,-7.026966,1.614048,-0.698833,3.768027,-0.145375,-8.627000,-6.432918,-4.243967,2.510954,-0.762641,2.068724,-7.977988,2.024310,3.568351,-9.184214,0.609043,-0.931117,-7.477763,-0.300956,-0.975273,-2.021848,-7.656615,7.290624,8.997329,3.843800,-6.224977,1.723304,5.804757,-2.876874,1.119257,2.303301,-4.968014,9.094435,7.472530,-2.614627,-6.593901,-7.590498,8.070817,-0.702318,-6.258955,-9.460601,-9.333742,-5.056145,-5.466460,-6.928955,9.828758,9.942778,9.787304,-8.180414,-5.534107,-4.919249,1.067607,-2.272333,-4.919516,3.483207,-8.622730,5.583138,-8.263488,-3.055093,0.431631,-2.187111,-6.386277,-1.630628,5.182887,-0.196905,3.189682,-2.426567,-8.457147,4.125106,9.958852,1.987724,-5.466277,1.642712,-4.394388,-6.498726,-8.785645,-9.538214,-7.876809,1.484870,-8.226764,7.412254,-4.924736,-3.943724,-0.158349,-2.149494,9.410675,3.279990,-5.015547,-5.612898,-2.341197,-1.714251,1.699352,-7.059816,9.595724,2.649622,1.877421,3.295363,3.279881,-1.449474,2.682363,8.724789,6.873825,2.297372,9.505488,-3.634199,-0.048038,3.443634,-1.812225,6.206677,3.685855,2.063774,1.016337,-4.245059,-2.351669,4.472127,6.844658,-6.268225,9.604528,5.671674,4.981075,8.379286,-0.644556,-7.512172,-5.527732,5.792905,-5.876878,-3.403265,6.680703,-1.295656,-7.673409,-2.770128,2.414898,-2.698951,-6.582803,1.011860,9.940162,8.489752,5.326181,-0.149614,9.666985,3.255030,-8.100118,6.871381,6.729197,-4.228596,8.409958,1.877374,8.741545,-2.427638,2.186460,-8.495091,-2.729153,7.429906,8.883358,6.435360,9.397830,-4.224593,-0.882786,3.209491,-8.810742,9.323779,-1.937001,-3.076918,-8.493078,6.565528,-9.247330,2.769489,0.911558,2.582564,-5.967869,8.501703,8.078145,-9.692780,-6.345948,7.192813,1.936185,-7.017365,-0.860688,1.863333,9.216542,-2.301606,-5.138448,-9.063321,-3.798965], dtype = "float64")#candidate|6705|(504,)|const|float64
call_6704 = relay.TupleGetItem(func_6267_call(relay.reshape(const_6705.astype('float64'), [9, 14, 4])), 1)
call_6706 = relay.TupleGetItem(func_6270_call(relay.reshape(const_6705.astype('float64'), [9, 14, 4])), 1)
uop_6708 = relay.acosh(uop_6702.astype('float64')) # shape=(2, 15, 7)
func_2551_call = mod.get_global_var('func_2551')
func_2553_call = mutated_mod.get_global_var('func_2553')
call_6713 = relay.TupleGetItem(func_2551_call(), 0)
call_6714 = relay.TupleGetItem(func_2553_call(), 0)
output = relay.Tuple([call_6704,const_6705,uop_6708,call_6713,])
output2 = relay.Tuple([call_6706,const_6705,uop_6708,call_6714,])
func_6717 = relay.Function([var_6697,], output)
mod['func_6717'] = func_6717
mod = relay.transform.InferType()(mod)
var_6718 = relay.var("var_6718", dtype = "float32", shape = (2, 15, 7))#candidate|6718|(2, 15, 7)|var|float32
output = func_6717(var_6718)
func_6719 = relay.Function([var_6718], output)
mutated_mod['func_6719'] = func_6719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6557_call = mod.get_global_var('func_6557')
func_6559_call = mutated_mod.get_global_var('func_6559')
call_6780 = relay.TupleGetItem(func_6557_call(), 0)
call_6781 = relay.TupleGetItem(func_6559_call(), 0)
output = call_6780
output2 = call_6781
func_6795 = relay.Function([], output)
mod['func_6795'] = func_6795
mod = relay.transform.InferType()(mod)
output = func_6795()
func_6796 = relay.Function([], output)
mutated_mod['func_6796'] = func_6796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_6881 = relay.TupleGetItem(func_303_call(), 1)
call_6882 = relay.TupleGetItem(func_304_call(), 1)
output = relay.Tuple([call_6881,])
output2 = relay.Tuple([call_6882,])
func_6889 = relay.Function([], output)
mod['func_6889'] = func_6889
mod = relay.transform.InferType()(mod)
mutated_mod['func_6889'] = func_6889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6889_call = mutated_mod.get_global_var('func_6889')
call_6890 = func_6889_call()
output = call_6890
func_6891 = relay.Function([], output)
mutated_mod['func_6891'] = func_6891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_641_call = mod.get_global_var('func_641')
func_643_call = mutated_mod.get_global_var('func_643')
call_6911 = relay.TupleGetItem(func_641_call(), 1)
call_6912 = relay.TupleGetItem(func_643_call(), 1)
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
var_6927 = relay.var("var_6927", dtype = "float32", shape = (40, 12))#candidate|6927|(40, 12)|var|float32
const_6928 = relay.const(False, dtype = "bool")#candidate|6928|()|const|bool
call_6926 = relay.TupleGetItem(func_1712_call(relay.reshape(var_6927.astype('float32'), [4, 10, 12]), relay.reshape(const_6928.astype('bool'), []), ), 4)
call_6929 = relay.TupleGetItem(func_1715_call(relay.reshape(var_6927.astype('float32'), [4, 10, 12]), relay.reshape(const_6928.astype('bool'), []), ), 4)
output = relay.Tuple([call_6911,call_6926,var_6927,const_6928,])
output2 = relay.Tuple([call_6912,call_6929,var_6927,const_6928,])
func_6931 = relay.Function([var_6927,], output)
mod['func_6931'] = func_6931
mod = relay.transform.InferType()(mod)
var_6932 = relay.var("var_6932", dtype = "float32", shape = (40, 12))#candidate|6932|(40, 12)|var|float32
output = func_6931(var_6932)
func_6933 = relay.Function([var_6932], output)
mutated_mod['func_6933'] = func_6933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5021_call = mod.get_global_var('func_5021')
func_5022_call = mutated_mod.get_global_var('func_5022')
call_6946 = relay.TupleGetItem(func_5021_call(), 0)
call_6947 = relay.TupleGetItem(func_5022_call(), 0)
func_3408_call = mod.get_global_var('func_3408')
func_3411_call = mutated_mod.get_global_var('func_3411')
call_6961 = relay.TupleGetItem(func_3408_call(relay.reshape(call_6946.astype('int64'), [9, 12, 15])), 3)
call_6962 = relay.TupleGetItem(func_3411_call(relay.reshape(call_6946.astype('int64'), [9, 12, 15])), 3)
func_408_call = mod.get_global_var('func_408')
func_411_call = mutated_mod.get_global_var('func_411')
var_6964 = relay.var("var_6964", dtype = "bool", shape = ())#candidate|6964|()|var|bool
call_6963 = relay.TupleGetItem(func_408_call(relay.reshape(var_6964.astype('bool'), [])), 0)
call_6965 = relay.TupleGetItem(func_411_call(relay.reshape(var_6964.astype('bool'), [])), 0)
const_6966 = relay.const([[[-3,-1,-5,4,10,-6,-3,2,10,3],[9,-9,8,5,-2,8,-4,-4,7,-6]],[[1,7,-8,6,-7,1,6,-6,-1,6],[4,3,-6,4,4,-2,3,-10,8,-10]],[[-4,-3,-10,-5,-2,6,-9,-3,-5,-10],[-10,-7,2,5,-3,9,5,-10,-2,7]],[[9,1,2,5,-4,8,7,-6,-3,1],[7,5,-3,-10,3,-1,1,-2,-6,2]],[[-2,-4,6,-8,-5,6,8,-8,8,7],[5,4,8,1,-3,-5,-5,-3,-3,1]],[[9,-9,-9,-9,-5,8,4,6,-8,-7],[-1,-5,5,7,-9,3,-8,-7,1,5]],[[2,-6,5,-10,10,-3,4,-7,-8,-5],[5,-4,-2,1,9,-9,-7,-9,8,5]],[[-9,-9,8,9,10,-2,-4,9,9,1],[-4,-1,7,5,-1,3,9,-10,8,3]],[[-5,-5,5,-7,4,4,-8,10,7,9],[6,-6,6,3,9,-1,5,5,8,4]],[[-10,1,-5,1,8,10,6,10,5,-3],[3,9,10,10,6,1,4,3,-2,-1]],[[-8,4,-8,3,2,-8,-2,5,-10,9],[8,-5,-9,-2,-5,-1,6,7,2,7]],[[-10,10,-1,1,1,9,-9,2,3,10],[6,2,-7,-6,-3,-6,8,-2,-3,10]]], dtype = "uint8")#candidate|6966|(12, 2, 10)|const|uint8
bop_6967 = relay.maximum(call_6963.astype('float32'), relay.reshape(const_6966.astype('float32'), relay.shape_of(call_6963))) # shape=(12, 2, 10)
bop_6970 = relay.maximum(call_6965.astype('float32'), relay.reshape(const_6966.astype('float32'), relay.shape_of(call_6965))) # shape=(12, 2, 10)
output = relay.Tuple([call_6946,call_6961,var_6964,bop_6967,])
output2 = relay.Tuple([call_6947,call_6962,var_6964,bop_6970,])
F = relay.Function([var_6964,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6964,], output2)
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
